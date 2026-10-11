from pathlib import Path
import json,textwrap,subprocess,uuid
OUT=Path(__file__).resolve().parent

def md(s):return {'cell_type':'markdown','metadata':{},'source':textwrap.dedent(s).strip().splitlines(keepends=True)}
def code(s):return {'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source':textwrap.dedent(s).strip().splitlines(keepends=True)}
def notebook(name,title,objectives,body,source,exercises):
 cells=[md(f'# {title}\n\n## Learning objectives\n\n{objectives}\n\nThis notebook runs a small CPU demonstration by default. Synthetic experiments are educational, not evidence of LLM alignment. Pretrained-model downloads and GPU training require explicit opt-in. All runtime outputs stay inside `RLHF_NOTEBOOKS/`.\n\n**Source connection:** {source}\n\n[Learning order and setup](README.md).'),code(SETUP)]+body+[md('## Exercises\n\n'+exercises+'\n\n## Key takeaways\n\nRecompute the worked examples, inspect masks and gradients, and evaluate independently of the training objective. A small training-loss decrease does not establish generalization or alignment. Record the model, data split, seeds and dependency versions before interpreting results.')]
 for i,c in enumerate(cells):c['id']=uuid.uuid5(uuid.NAMESPACE_URL,name+str(i)).hex[:12]
 nb={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3 (RLHF notebooks)','language':'python','name':'python3'},'language_info':{'name':'python','version':'3.13'},'source_basis':source,'validation_scope':'CPU examples; pretrained/GPU sections opt-in'},'nbformat':4,'nbformat_minor':5}
 (OUT/name).write_text(json.dumps(nb,indent=1,ensure_ascii=False)+'\n')

SETUP=r'''
from pathlib import Path
import os, sys, json, math, random, copy, re, subprocess, hashlib
# Find this collection when launched from the repository, module, or notebook directory.
candidates = [Path.cwd(), Path.cwd()/'RLHF_NOTEBOOKS', Path.cwd()/'13_rlhf_ppo_dpo_orpo/RLHF_NOTEBOOKS']
ROOT = next((p.resolve() for p in candidates if (p/'source_inspection.json').exists()), None)
if ROOT is None:
    raise RuntimeError('Launch Jupyter from RLHF_NOTEBOOKS, its parent, or the repository root.')
RUNTIME = ROOT/'runtime'; RUNTIME.mkdir(exist_ok=True)
os.environ['MPLCONFIGDIR'] = str(RUNTIME/'matplotlib')
os.environ['HF_HOME'] = str(RUNTIME/'huggingface')
os.environ['HF_DATASETS_CACHE'] = str(RUNTIME/'huggingface/datasets')
os.environ['TOKENIZERS_PARALLELISM'] = 'false'
os.environ['WANDB_DISABLED'] = 'true'
import numpy as np
import torch
from torch import nn
from torch.nn import functional as F
import matplotlib.pyplot as plt
random.seed(42); np.random.seed(42); torch.manual_seed(42)
torch.set_num_threads(1)
print('Python', sys.version.split()[0], 'PyTorch', torch.__version__, 'CUDA', torch.cuda.is_available())
'''
DATA=r'''
def read_preferences():
    path = ROOT.parent/'reward_preferences_dataset.jsonl'
    if path.exists():
        raw = path.read_bytes(); origin = str(path)
    else:
        # Originals are currently missing from the working tree. Read their Git blob;
        # never restore, overwrite or silently substitute invented preference records.
        gitroot = Path(subprocess.check_output(['git','rev-parse','--show-toplevel'], cwd=ROOT, text=True).strip())
        rel = (ROOT.parent/'reward_preferences_dataset.jsonl').relative_to(gitroot).as_posix()
        raw = subprocess.check_output(['git','show','HEAD:'+rel], cwd=gitroot)
        origin = 'HEAD:'+rel
    expected = json.loads((ROOT/'source_inspection.json').read_text())
    digest = next(r['sha256'] for r in expected if r['source']=='reward_preferences_dataset.jsonl')
    assert hashlib.sha256(raw).hexdigest() == digest, 'Dataset changed: re-audit before proceeding'
    rows = [json.loads(line) for line in raw.decode('utf-8').splitlines()]
    for row in rows:
        assert set(row)=={'prompt','chosen','rejected'}
        assert all(isinstance(row[k],str) and row[k].strip() for k in row)
        assert row['chosen'].strip()!=row['rejected'].strip()
    assert len({r['prompt'].strip().lower() for r in rows})==len(rows)
    print('Dataset origin:',origin,'records:',len(rows),'fields:',list(rows[0]))
    return rows
rows = read_preferences()
indices = np.random.default_rng(42).permutation(len(rows))
train_rows = [rows[i] for i in indices[:14]]
valid_rows = [rows[i] for i in indices[14:17]]
test_rows = [rows[i] for i in indices[17:]]
assert not ({r['prompt'] for r in train_rows} & {r['prompt'] for r in valid_rows+test_rows})
print('Prompt-separated split:',len(train_rows),len(valid_rows),len(test_rows))
'''
CAUSAL=r'''
# Character vocabulary: finite encoding avoids tokenizer downloads and boundary merges.
# This is an educational tokenizer, not a pretrained chat model's tokenizer.
CHARS = sorted(set(''.join(r[k] for r in rows for k in ('prompt','chosen','rejected'))+'Question: Answer:\n'))
vocab = {'<pad>':0,'<bos>':1,'<eos>':2,'<unk>':3, **{c:i+4 for i,c in enumerate(CHARS)}}
def encode(text): return [vocab.get(c,3) for c in text]
def pair_batch(examples, side):
    seqs=[]; response=[]
    for r in examples:
        prefix=[1]+encode('Question: '+r['prompt']+'\nAnswer: ')
        answer=encode(r[side])+[2]
        seqs.append(prefix+answer);response.append([0]*len(prefix)+[1]*len(answer))
    length=max(map(len,seqs))
    ids=torch.tensor([s+[0]*(length-len(s)) for s in seqs])
    attention=ids.ne(0)
    completion=torch.tensor([m+[0]*(length-len(m)) for m in response],dtype=torch.bool)
    return ids,attention,completion

def completion_logps(logits,ids,attention,completion,average=False):
    assert logits.shape[:2]==ids.shape==attention.shape==completion.shape
    target=ids[:,1:]
    assert (target>=0).all() and (target<logits.shape[-1]).all()
    active=completion[:,1:].bool() & attention[:,1:].bool() & attention[:,:-1].bool()
    counts=active.sum(-1)
    if (counts==0).any(): raise ValueError('Empty scored completion')
    selected=F.log_softmax(logits[:,:-1].float(),-1).gather(-1,target.unsqueeze(-1)).squeeze(-1)
    total=selected.masked_fill(~active,0).sum(-1)
    return total/counts if average else total

class TinyLM(nn.Module):
    def __init__(self):
        super().__init__();self.embedding=nn.Embedding(len(vocab),24,padding_idx=0)
        self.rnn=nn.GRU(24,32,batch_first=True);self.head=nn.Linear(32,len(vocab))
    def forward(self,ids): return self.head(self.rnn(self.embedding(ids))[0])

def score(model,batch,average=False):
    ids,att,mask=batch
    return completion_logps(model(ids),ids,att,mask,average)

def finite_step(loss,model,optimizer):
    assert torch.isfinite(loss).all()
    optimizer.zero_grad();loss.backward()
    grads=[p.grad for p in model.parameters() if p.requires_grad and p.grad is not None]
    assert grads and all(torch.isfinite(g).all() for g in grads)
    assert any(g.abs().sum()>0 for g in grads), 'No gradient signal'
    nn.utils.clip_grad_norm_(model.parameters(),1.0);optimizer.step()

# Meaningful causal-shift, prompt exclusion, padding and gradient tests.
ids=torch.tensor([[1,4,5,2,0]]); att=ids.ne(0);mask=torch.tensor([[0,0,1,1,0]],dtype=torch.bool)
logits=torch.zeros(1,5,len(vocab),requires_grad=True)
s=completion_logps(logits,ids,att,mask)
assert torch.allclose(s,torch.tensor([-2*math.log(len(vocab))]))
(-s.sum()).backward()
assert logits.grad[0,0].abs().sum()==0   # predicts masked prompt token
assert logits.grad[0,1:3].abs().sum()>0  # predicts response and EOS
assert logits.grad[0,3:].abs().sum()==0  # padding / unused last logits
assert torch.allclose(completion_logps(logits.detach(),ids,att,mask,True),s.detach()/2)
try:
    completion_logps(logits.detach(),ids,att,torch.zeros_like(mask))
    raise AssertionError('Should reject empty completions')
except ValueError: pass
print('Causal shifting, response/padding masking and gradient checks passed.')
'''
DPO=r'''
def dpo_loss(w,l,rw,rl,beta=.1):
    if beta<=0: raise ValueError('beta must be positive')
    margin=beta*((w-l)-(rw.detach()-rl.detach()))
    return F.softplus(-margin).mean(),margin
assert abs(dpo_loss(torch.zeros(1),torch.zeros(1),torch.zeros(1),torch.zeros(1))[0].item()-math.log(2))<1e-6
policy=TinyLM();reference=copy.deepcopy(policy).eval().requires_grad_(False)
chosen=pair_batch(train_rows,'chosen');rejected=pair_batch(train_rows,'rejected')
with torch.no_grad():rw=score(reference,chosen);rl=score(reference,rejected)
opt=torch.optim.Adam(policy.parameters(),lr=.003)
history=[]
for step in range(35):
    loss,margin=dpo_loss(score(policy,chosen),score(policy,rejected),rw,rl)
    finite_step(loss,policy,opt);history.append(loss.item())
assert all(p.grad is None for p in reference.parameters())
assert history[-1]<history[0]
plt.plot(history);plt.xlabel('CPU optimizer step');plt.ylabel('DPO loss');plt.title('Measured toy GRU training loss');plt.show()
print('First/final training loss:',history[0],history[-1])
'''
EVAL=r'''
@torch.no_grad()
def evaluate_pairs(model,examples,reference=None):
    model.eval();w=score(model,pair_batch(examples,'chosen'));l=score(model,pair_batch(examples,'rejected'))
    raw=w-l;out={'raw_preference_accuracy':raw.gt(0).float().mean().item(),'chosen_mean_sum_logp':w.mean().item(),'rejected_mean_sum_logp':l.mean().item()}
    if reference is not None:
        relative=raw-(score(reference,pair_batch(examples,'chosen'))-score(reference,pair_batch(examples,'rejected')))
        out['relative_margin_mean']=relative.mean().item()
        out['reference_adjusted_accuracy']=relative.gt(0).float().mean().item()
    return out
print('Train:',evaluate_pairs(policy,train_rows,reference))
print('Validation:',evaluate_pairs(policy,valid_rows,reference))
policy.train()
'''
ORPO=r'''
def log1mexp(logp):
    x=logp.float()
    if (x>=0).any():raise ValueError('Need strictly negative log likelihood')
    result=torch.empty_like(x);far=x < -math.log(2)
    result[far]=torch.log1p(-torch.exp(x[far]))
    result[~far]=torch.log(-torch.expm1(x[~far]))
    return result

def orpo_loss(w,l,coefficient=.1):
    # w/l are completion-MEAN logps. This averages NLL equally across sequences.
    margin=(w-log1mexp(w))-(l-log1mexp(l))
    sft=-w.mean();preference=F.softplus(-margin).mean()
    return sft+coefficient*preference,sft,preference
w=torch.tensor([math.log(.75)],requires_grad=True);l=torch.tensor([math.log(.25)],requires_grad=True)
toy=orpo_loss(w,l)[0];assert abs(toy.item()-.298218124)<1e-6
toy.backward();assert torch.isfinite(w.grad).all() and torch.isfinite(l.grad).all()
edge=torch.tensor([-1e-6,-.1,-1.,-30.],requires_grad=True)
log1mexp(edge).sum().backward();assert torch.isfinite(edge.grad).all()
policy=TinyLM();opt=torch.optim.Adam(policy.parameters(),lr=.003)
chosen=pair_batch(train_rows,'chosen');rejected=pair_batch(train_rows,'rejected')
history=[];parts=[]
for step in range(35):
    loss,sft,pref=orpo_loss(score(policy,chosen,True),score(policy,rejected,True))
    finite_step(loss,policy,opt);history.append(loss.item());parts.append((sft.item(),pref.item()))
plt.plot(history,label='Combined');plt.plot(np.array(parts)[:,0],label='Chosen NLL');plt.plot(np.array(parts)[:,1],label='Preference');plt.legend();plt.xlabel('Step');plt.ylabel('Loss');plt.title('Measured toy ORPO components');plt.show()
print('ORPO toy arithmetic:',toy.item(),'Training first/final:',history[0],history[-1])
'''
GAE=r'''
def gae(rewards,values,next_values,terminated,boundary,gamma=.99,lam=.95):
    # terminated: true MDP terminal -> no bootstrap.
    # boundary: terminal OR time-limit/reset boundary -> no cross-episode recursion.
    # For a truncation next_values uses the pre-reset final observation.
    assert rewards.shape==values.shape==next_values.shape==terminated.shape==boundary.shape
    delta=rewards+gamma*(~terminated).float()*next_values-values
    advantages=torch.zeros_like(rewards);carry=torch.zeros_like(rewards[-1])
    for t in reversed(range(len(rewards))):
        carry=delta[t]+gamma*lam*(~boundary[t]).float()*carry
        advantages[t]=carry
    return advantages.detach(),(advantages+values).detach()
r=torch.tensor([0.,1.]);v=torch.tensor([.4,.5]);nv=torch.tensor([.5,0.]);d=torch.tensor([False,True])
a,target=gae(r,v,nv,d,d,1.,.95)
assert torch.allclose(a,torch.tensor([.575,.5])) and torch.allclose(target,torch.tensor([.975,1.]))
# Distinguish time-limit bootstrap from true terminal.
a_tr,_=gae(torch.tensor([0.]),torch.tensor([.2]),torch.tensor([.7]),torch.tensor([False]),torch.tensor([True]),1.,.95)
assert torch.allclose(a_tr,torch.tensor([.5]))
print('GAE and truncation tests passed:',a.tolist(),target.tolist())
'''
ENV=r'''
# Synthetic chain: positions 0..4, start 2, left/right actions, terminal endpoints.
# Goal 4 earns +1; endpoint 0 earns -1; each intermediate step costs .02.
class Chain:
    def reset(self):self.position=2;self.steps=0;return self.position
    def step(self,action):
        self.steps+=1;self.position+=1 if action else -1
        terminated=self.position in (0,4);truncated=self.steps>=12 and not terminated
        reward=1. if self.position==4 else -1. if self.position==0 else -.02
        return self.position,reward,terminated,truncated

def state_tensor(states):return F.one_hot(torch.as_tensor(states),num_classes=5).float()
class ActorCritic(nn.Module):
    def __init__(self):
        super().__init__();self.shared=nn.Sequential(nn.Linear(5,24),nn.Tanh());self.actor=nn.Linear(24,2);self.critic=nn.Linear(24,1)
    def forward(self,states):
        h=self.shared(state_tensor(states));return torch.distributions.Categorical(logits=self.actor(h)),self.critic(h).squeeze(-1)
'''
PPO=r'''
model=ActorCritic();optimizer=torch.optim.Adam(model.parameters(),lr=.015)
env=Chain();state=env.reset();returns=[];losses=[];clipfractions=[];episode_return=0.
for iteration in range(45):
    states=[];actions=[];old_logps=[];values=[];next_values=[];rewards=[];ends=[];boundaries=[]
    # Store one recent rollout: the denominator is detached behavior logp, not reference logp.
    with torch.no_grad():
        for t in range(64):
            distribution,value=model(torch.tensor(state));action=distribution.sample()
            next_state,reward,terminated,truncated=env.step(action.item())
            _,next_value=model(torch.tensor(next_state))
            states.append(state);actions.append(action);old_logps.append(distribution.log_prob(action));values.append(value);next_values.append(next_value)
            rewards.append(reward);ends.append(terminated);boundaries.append(terminated or truncated)
            episode_return+=reward
            if terminated or truncated:returns.append(episode_return);episode_return=0.;state=env.reset()
            else:state=next_state
    old=torch.stack(old_logps);v=torch.stack(values)
    advantage,target=gae(torch.tensor(rewards),v,torch.stack(next_values),torch.tensor(ends),torch.tensor(boundaries))
    advantage=(advantage-advantage.mean())/(advantage.std(unbiased=False)+1e-8)
    states=torch.tensor(states);actions=torch.stack(actions)
    # Three optimization epochs, shuffled minibatches over the SAME rollout.
    for epoch in range(3):
        for idx in torch.randperm(64).split(16):
            distribution,value=model(states[idx]);ratio=(distribution.log_prob(actions[idx])-old[idx]).exp()
            unclipped=ratio*advantage[idx];clipped=ratio.clamp(.8,1.2)*advantage[idx]
            actor_loss=-torch.minimum(unclipped,clipped).mean()
            value_loss=.5*(value-target[idx]).square().mean();entropy=distribution.entropy().mean()
            loss=actor_loss+.5*value_loss-.01*entropy
            optimizer.zero_grad();loss.backward()
            assert torch.isfinite(loss) and all(torch.isfinite(p.grad).all() for p in model.parameters())
            nn.utils.clip_grad_norm_(model.parameters(),.5);optimizer.step()
            losses.append(loss.item());clipfractions.append(((ratio-1).abs()>.2).float().mean().item())
print('Mean of last 30 completed episode returns:',np.mean(returns[-30:]))
fig,axes=plt.subplots(1,2,figsize=(10,3));axes[0].plot(returns);axes[0].set(title='Measured chain returns',xlabel='Episode',ylabel='Return');axes[1].plot(clipfractions);axes[1].set(title='Measured clip fraction',xlabel='Minibatch',ylabel='Fraction');plt.show()
# Inference evaluation on new episodes without optimizer updates.
with torch.no_grad():
    evaluation=[]
    for _ in range(20):
        s=env.reset();total=0.
        while True:
            dist,_=model(torch.tensor(s));s,reward,done,trunc=env.step(dist.probs.argmax().item());total+=reward
            if done or trunc:break
        evaluation.append(total)
print('Greedy chain evaluation:',np.mean(evaluation))
'''
GROUP=r'''
def group_advantages(rewards,epsilon=1e-8):
    if rewards.ndim!=2 or rewards.shape[1]<2:raise ValueError('Need [prompts, group>=2] rewards')
    centered=rewards-rewards.mean(-1,keepdim=True)
    return centered/(rewards.std(-1,keepdim=True,unbiased=False)+epsilon)
assert torch.allclose(group_advantages(torch.tensor([[1.,0.,1.,0.]])),torch.tensor([[1.,-1.,1.,-1.]]))
assert torch.equal(group_advantages(torch.ones(2,4)),torch.zeros(2,4))
print('Source group [9,6,2]:',group_advantages(torch.tensor([[9.,6.,2.]])).tolist())
# Synthetic one-token arithmetic policy: actions represent candidate integers 0..9.
# This is a contextual bandit special case of outcome-GRPO (response length T=1).
policy_logits=nn.Parameter(torch.zeros(3,10));ref_logps=torch.full((3,10),-math.log(10))
optimizer=torch.optim.Adam([policy_logits],lr=.12);gold=torch.tensor([2,4,6]);history=[];variance=[]
for iteration in range(70):
    with torch.no_grad():
        old=torch.distributions.Categorical(logits=policy_logits.detach())
        actions=old.sample((8,)).T  # [3 prompts, 8 completions each]
        old_selected=F.log_softmax(policy_logits.detach(),-1).gather(1,actions)
        rewards=actions.eq(gold[:,None]).float();adv=group_advantages(rewards)
    for epoch in range(2):
        logps=F.log_softmax(policy_logits,-1);selected=logps.gather(1,actions)
        ratio=(selected-old_selected).exp()
        surrogate=torch.minimum(ratio*adv,ratio.clamp(.8,1.2)*adv).mean()
        # Exact full action KL removes reused-sample estimator ambiguity in this T=1 demo.
        kl=(logps.exp()*(logps-ref_logps)).sum(-1).mean()
        loss=-surrogate+.01*kl
        optimizer.zero_grad();loss.backward();assert torch.isfinite(policy_logits.grad).all();optimizer.step()
    history.append(rewards.mean().item());variance.append(rewards.std(-1,unbiased=False).mean().item())
plt.plot(history,label='Sampled correctness');plt.plot(variance,label='Within-group std');plt.xlabel('Fresh group');plt.ylabel('Metric');plt.title('Measured synthetic GRPO metrics');plt.legend();plt.show()
print('Correct-answer probabilities:',F.softmax(policy_logits,-1)[torch.arange(3),gold].detach().tolist())
'''
HF=r'''
# Local tiny GPT-2 architecture and WordLevel tokenizer: NO pretrained downloads.
from importlib import metadata
import inspect
from tokenizers import Tokenizer,models,pre_tokenizers
from transformers import PreTrainedTokenizerFast,GPT2Config,GPT2LMHeadModel,GPT2ForSequenceClassification
from datasets import Dataset
from trl import DPOTrainer,DPOConfig,GRPOTrainer,GRPOConfig,ORPOTrainer,ORPOConfig,RewardTrainer,RewardConfig,PPOTrainer,PPOConfig
VERSIONS={name:metadata.version(name) for name in ('torch','transformers','trl','datasets','peft','accelerate')}
print(VERSIONS)
assert metadata.version('trl')=='0.22.2', 'Use the pinned environment; APIs change across TRL releases.'
for cls in [DPOTrainer,GRPOTrainer,ORPOTrainer,PPOTrainer]: print(cls.__name__,inspect.signature(cls.__init__))
texts=['Question: '+r['prompt']+' Answer: '+r[s] for r in rows for s in ('chosen','rejected')]
words=sorted(set(re.findall(r'\w+|[^\w\s]', ' '.join(texts)+' What is 1 + 1 ? 2 3 4 - .')))
word_vocab={'<pad>':0,'<eos>':1,'<unk>':2,'<bos>':3,**{w:i+4 for i,w in enumerate(words)}}
backend=Tokenizer(models.WordLevel(word_vocab,unk_token='<unk>'));backend.pre_tokenizer=pre_tokenizers.Whitespace()
tokenizer=PreTrainedTokenizerFast(tokenizer_object=backend,pad_token='<pad>',eos_token='<eos>',unk_token='<unk>',bos_token='<bos>')
tokenizer.chat_template="{% for message in messages %}{{ message['role'] + ': ' + message['content'] + '\\n' }}{% endfor %}{% if add_generation_prompt %}{{ 'assistant: ' }}{% endif %}"
def lm_config():
    return GPT2Config(vocab_size=len(tokenizer),n_positions=256,n_ctx=256,n_embd=32,n_layer=1,n_head=2,pad_token_id=0,eos_token_id=1,bos_token_id=3,resid_pdrop=0.,embd_pdrop=0.,attn_pdrop=0.)
def hf_pairs(examples):
    return Dataset.from_list([{'prompt':'Question: '+r['prompt']+' Answer:','chosen':' '+r['chosen']+tokenizer.eos_token,'rejected':' '+r['rejected']+tokenizer.eos_token} for r in examples])
RUN_TRL_SMOKE = True   # two steps on randomly initialized tiny LOCAL model, CPU-friendly
RUN_PRETRAINED_GPU = False  # opt-in; downloads a real checkpoint only when True
print('Tokenizer distinct PAD/EOS:',tokenizer.pad_token_id,tokenizer.eos_token_id)
assert tokenizer.pad_token_id != tokenizer.eos_token_id
'''
HF_PAIR_TRAIN=r'''
if RUN_TRL_SMOKE:
    model=GPT2LMHeadModel(lm_config())
    args=CONFIG(output_dir=str(RUNTIME/'TAG_cpu'),max_steps=2,learning_rate=1e-4,per_device_train_batch_size=2,per_device_eval_batch_size=2,
                gradient_accumulation_steps=1,max_length=128,max_prompt_length=64,beta=.1,
                eval_strategy='steps',eval_steps=1,save_strategy='steps',save_steps=1,save_total_limit=2,
                logging_steps=1,report_to='none',use_cpu=True,bf16=False,fp16=False,remove_unused_columns=False,seed=42)
    trainer=TRAINER(model=model,args=args,processing_class=tokenizer,train_dataset=hf_pairs(train_rows),eval_dataset=hf_pairs(valid_rows))
    initial=trainer.evaluate();result=trainer.train();final=trainer.evaluate()
    trainer.save_model(str(RUNTIME/'TAG_cpu/final'));tokenizer.save_pretrained(str(RUNTIME/'TAG_cpu/final'))
    print('Actual local smoke output:',result,'Before:',initial,'After:',final)
    # Reload local model; no pretrained download; compare logits on exactly same input.
    trained=trainer.accelerator.unwrap_model(trainer.model).eval()
    reloaded=GPT2LMHeadModel.from_pretrained(str(RUNTIME/'TAG_cpu/final')).eval()
    x=tokenizer('Question: What is AI? Answer:',return_tensors='pt')
    with torch.no_grad():assert torch.allclose(trained(**x).logits,reloaded(**x).logits,atol=1e-5)
    print('Saved/reloaded logits agree.')
'''
GPU_PAIRS=r'''
# Real pretrained-model path; this block is skipped by default.
if RUN_PRETRAINED_GPU:
    assert torch.cuda.is_available(), 'This optional recipe requires CUDA; leave the flag False for CPU demos.'
    from transformers import AutoTokenizer,AutoModelForCausalLM
    from peft import LoraConfig,AutoPeftModelForCausalLM
    MODEL_ID='HuggingFaceTB/SmolLM2-135M-Instruct'
    gpu_tok=AutoTokenizer.from_pretrained(MODEL_ID)
    if gpu_tok.pad_token_id is None:gpu_tok.pad_token=gpu_tok.eos_token
    # Chat templates own formatting. Do not apply them and then template again in trainer.
    def conversational(examples):
        return Dataset.from_list([{'prompt':[{'role':'user','content':r['prompt']}],
                                  'chosen':[{'role':'assistant','content':r['chosen']}],
                                  'rejected':[{'role':'assistant','content':r['rejected']}]} for r in examples])
    dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float32
    gpu_model=AutoModelForCausalLM.from_pretrained(MODEL_ID,torch_dtype=dtype)
    gpu_model.config.use_cache=False
    config=CONFIG(output_dir=str(RUNTIME/'TAG_gpu'),max_steps=5,per_device_train_batch_size=1,gradient_accumulation_steps=4,
                  per_device_eval_batch_size=1,learning_rate=1e-5,beta=.1,max_length=256,max_prompt_length=128,
                  bf16=dtype==torch.bfloat16,fp16=False,eval_strategy='steps',eval_steps=5,save_strategy='steps',save_steps=5,
                  gradient_checkpointing=True,report_to='none',seed=42,remove_unused_columns=False)
    gpu_trainer=TRAINER(model=gpu_model,args=config,processing_class=gpu_tok,train_dataset=conversational(train_rows),
                        eval_dataset=conversational(valid_rows),peft_config=LoraConfig(task_type='CAUSAL_LM',r=8,lora_alpha=16,target_modules=['q_proj','v_proj']))
    gpu_trainer.train();print(gpu_trainer.evaluate());gpu_trainer.save_model(str(RUNTIME/'TAG_gpu/final'));gpu_tok.save_pretrained(str(RUNTIME/'TAG_gpu/final'))
    # DPO ref_model=None with a new LoRA adapter still uses adapter-disabled reference.
    # ORPO has no reference role. Do not interpret identical keyword choices as identical objectives.
    del gpu_trainer,gpu_model
    loaded=AutoPeftModelForCausalLM.from_pretrained(str(RUNTIME/'TAG_gpu/final'),torch_dtype=dtype).to('cuda').eval()
    inputs=gpu_tok.apply_chat_template([{'role':'user','content':'What is AI?'}],tokenize=True,add_generation_prompt=True,return_tensors='pt').to('cuda')
    with torch.no_grad():generated=loaded.generate(inputs,max_new_tokens=48,do_sample=False,pad_token_id=gpu_tok.pad_token_id)
    print(gpu_tok.decode(generated[0,inputs.shape[1]:],skip_special_tokens=True))
'''

notebook('01_RL_Fundamentals.ipynb','01 — Reinforcement learning fundamentals','- Describe states/actions/rewards, MDP transitions and policies.\n- Calculate returns, values and Bellman recursions.\n- Run actual state-dependent Q-learning instead of a stateless reward dictionary.',[
md(r'''## From game interaction to an MDP
An MDP is $(S,A,P,r,d_0,\gamma)$. $S$ is states, $A$ actions, $P(s'\mid s,a)$ next-state probability, $r(s,a)$ expected immediate reward, $d_0$ starting-state distribution and $\gamma$ discount. Markov means the state retains relevant predictive information. Here the game state is chain position; the agent chooses left/right. A stochastic policy samples moves; a deterministic policy chooses one move per state. An episode ends at a terminal endpoint or a time limit.

$$
G_t=\sum_{k=0}^{T-1-t}\gamma^kR_{t+k},\qquad V^\pi(s)=\mathbb E[G_t\mid s_t=s],\qquad Q^\pi(s,a)=\mathbb E[G_t\mid s_t=s,a_t=a].
$$
$R_t$ is reward after action $t$, $T$ episode length, and $G_t$ remaining return. $V$ averages actions under policy $\pi$; $Q$ fixes the first action. Discount $\gamma$ controls future weighting. For rewards $[0,0,10]$ at $\gamma=.9$, $G_0=8.1$.

$$
Q^\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^\pi(s'),\qquad V^\pi(s)=\sum_a\pi(a\mid s)Q^\pi(s,a).
$$
Split $G_t=R_t+\gamma G_{t+1}$ to derive Bellman expectation. Optimality replaces the next-state action average with $\max_{a'}Q^*(s',a')$. Terminal values are zero; a time-limit observation can still bootstrap.'''),code(ENV),
code(r'''
def discounted_returns(rewards,gamma=.9):
    result=[];carry=0.
    for reward in reversed(rewards):carry=reward+gamma*carry;result.append(carry)
    return list(reversed(result))
assert np.allclose(discounted_returns([0,0,10]),[8.1,9.,10.])
# Source crossroad example, not measured experiment data.
q=np.array([10.,50.,20.]);pi=np.array([.2,.5,.3]);value=pi@q
assert value==33 and abs(pi@(q-value))<1e-10
print('Crossroad value:',value,'advantages:',q-value)
# Bellman expectation via linear system on nonterminal states, uniform policy.
P=np.zeros((3,3));reward=np.zeros(3)
for s in range(1,4):
    for action in (0,1):
        ns=s+(1 if action else -1);r=1 if ns==4 else -1 if ns==0 else -.02
        reward[s-1]+=.5*r
        if ns not in (0,4):P[s-1,ns-1]+=.5
V=np.linalg.solve(np.eye(3)-.95*P,reward)
assert np.allclose(V,reward+.95*P@V)
print('Exact uniform-policy state values:',V)
'''),md(r'''## Q-learning implementation

$$
Q(s,a)\leftarrow Q(s,a)+\alpha\left[R+\gamma(1-d)\max_{a'}Q(s',a')-Q(s,a)\right].
$$
$\alpha$ is step size, $d$ true termination, and the bracket is TD error. This off-policy target uses the best next action even when epsilon-greedy behavior explored. SARSA would use the actual next sampled action. Monte Carlo waits for full return; TD bootstraps an estimate. Unlike the original dictionary demo, the code below has transitions, future value and a changing exploration policy.'''),
code(r'''
Q=np.zeros((5,2));env=Chain();returns=[]
for episode in range(250):
    state=env.reset();total=0.;epsilon=max(.05,.8*(.985**episode))
    while True:
        action=random.randrange(2) if random.random()<epsilon else int(Q[state].argmax())
        next_state,reward,done,truncated=env.step(action)
        target=reward+.95*(not done)*Q[next_state].max()
        Q[state,action]+=.15*(target-Q[state,action]);total+=reward
        if done or truncated:break
        state=next_state
    returns.append(total)
print('Learned Q:',Q,'greedy nonterminal actions:',Q[1:4].argmax(-1))
plt.plot(returns);plt.xlabel('Episode');plt.ylabel('Return');plt.title('Measured synthetic Q-learning');plt.show()
assert np.all(Q[1:4].argmax(-1)==1)
'''),md('## Mapping to LLMs\n\nState = prompt plus prefix; action = next token; policy = LM probability distribution; trajectory = response; terminal = EOS/stopping condition. Response reward can be terminal or token-shaped. A reward dictionary is not a full LLM RL implementation.')],
'RL_Fundamental.ipynb dictionary/DQN/racing demos; RLHF PDF crossroad Q10/50/20 and DQN target10.4; notes Chapter01. Originals read from Git without restoring missing working-tree files.',
'1. Change the terminal rewards and predict the policy before training.\n2. Implement SARSA and compare exploratory trajectories.\n3. Recompute the Bellman system for a biased policy.')

notebook('02_Policy_Gradients_Actor_Critic.ipynb','02 — Policy gradients and actor-critic','- Derive log-probability policy gradients and action-independent baselines.\n- Train REINFORCE on a contextual bandit.\n- Fit a value head and compute GAE with correct terminal handling.',[
md(r'''## REINFORCE and the score-function identity

$$
\nabla_\theta J=\mathbb E_\tau\left[G_0\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)\right].
$$
$J$ is expected return, $\theta$ policy parameters, $\tau$ a trajectory, and $\pi$ action distribution. The identity $\nabla p=p\nabla\log p$ explains log probabilities. Causality permits reward-to-go; a discounted start-state estimator also weights time $t$ by $\gamma^t$. Here episodes have one action and $\gamma=1$.

$$
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s),\qquad \mathcal L_{actor}=-\mathbb E[\log\pi_\theta(a\mid s)\hat A].
$$
$Q$ predicts action-conditioned return, $V$ average return, $A$ advantage. Subtracting an action-independent baseline does not change the expected score-function gradient. Detach estimated advantages when optimizing the actor; fit the critic separately.'''),
code(r'''
# Synthetic contextual bandit: action should match context 0 or 1.
actor=nn.Linear(2,2);critic=nn.Linear(2,1)
opt=torch.optim.Adam(list(actor.parameters())+list(critic.parameters()),lr=.04)
measured=[]
for step in range(100):
    context=torch.randint(0,2,(64,));x=F.one_hot(context,2).float()
    dist=torch.distributions.Categorical(logits=actor(x));action=dist.sample()
    reward=action.eq(context).float();value=critic(x).squeeze(-1)
    advantage=reward-value.detach()
    actor_loss=-(dist.log_prob(action)*advantage).mean()
    value_loss=.5*(value-reward).square().mean()
    loss=actor_loss+value_loss-.01*dist.entropy().mean()
    opt.zero_grad();loss.backward()
    assert actor.weight.grad.abs().sum()>0 and critic.weight.grad.abs().sum()>0
    assert torch.isfinite(loss);opt.step();measured.append(reward.mean().item())
plt.plot(measured);plt.xlabel('Step');plt.ylabel('Sampled success rate');plt.title('Measured REINFORCE with learned baseline');plt.show()
with torch.no_grad():print('Learned action probabilities:',actor(torch.eye(2)).softmax(-1))
'''),md(r'''## Generalized Advantage Estimation

$$
\delta_t=R_t+\gamma(1-d_t)V_{old}(s_{t+1})-V_{old}(s_t),\qquad
\hat A_t=\delta_t+\gamma\lambda(1-b_t)\hat A_{t+1},\qquad \hat G_t=\hat A_t^{raw}+V_{old}(s_t).
$$
$\delta$ is TD residual, $d$ true terminal, $b$ episode boundary (terminal or time-limit reset), $\lambda$ residual decay, and $\hat G$ detached value target. Fixed rollout critic $V_{old}$ must be used consistently. A truncation bootstraps its final observation but stops recursion across a reset. Normalize actor advantages only after calculating critic targets. With rewards $[0,1]$, values $[.4,.5]$, $\gamma=1$, $\lambda=.95$, advantages are $[.575,.5]$.'''),code(GAE),code(r'''
# Why detach matters: actor advantages must not turn critic into an actor-loss shortcut.
value=torch.tensor([.3],requires_grad=True);logp=torch.tensor([-.7],requires_grad=True)
actor_loss=-(logp*(torch.tensor([1.])-value).detach()).mean()
actor_loss.backward();assert value.grad is None and logp.grad is not None
print('Detached baseline blocks critic gradient from actor objective.')
''')], 'Notes Chapters01/04 and RLHF PDF actor/critic and reward8/value6 examples. This notebook adds complete trainable policy/baseline examples.', '1. Compare no baseline, moving-average baseline and learned baseline.\n2. Sweep GAE lambda and recompute targets.\n3. Remove detach in a copy and inspect which gradients change.')

notebook('03_RLHF_Reward_Modeling.ipynb','03 — RLHF preference data and reward modeling','- Inspect the real preference schema and prompt-separated split.\n- Fit Bradley–Terry scalar reward scores.\n- Distinguish a reward scorer from a prefix-conditioned critic.',[
md(r'''## Classical RLHF and four roles
Pretraining predicts tokens; SFT imitates demonstrations; comparison data trains a reward model; PPO improves sampled responses against reward and a reference anchor. This is a common pipeline, not the only alignment architecture.

| Role | Input/output | During PPO |
|---|---|---|
| Policy | Prefix → token logits | Trainable |
| Reference | Same prefix → baseline probabilities | Frozen |
| Reward model | Prompt plus completed response → scalar | Usually frozen |
| Critic | Prefix → expected remaining shaped return | Trainable |

Sharing architectures does not make reward and value targets equal. Your source PPO notebook initializes both scalar models from RM weights, then freezes the reward copy and trains the critic.

$$
P(y_w\succ y_l\mid x)=\sigma(r_\psi(x,y_w)-r_\psi(x,y_l)),\quad
\mathcal L_{RM}=-\mathbb E\log\sigma(r_w-r_l).
$$
$x$ is shared prompt, $y_w/y_l$ chosen/rejected, $r_\psi$ learned scalar utility, and $\sigma(z)=1/(1+e^{-z})$. The prompt-dependent additive offset cancels: utilities8/3 and108/103 give the same probability. Scores are not absolute truth or calibrated safety.'''),code(DATA),
code(r'''
print(rows[0])
longer=sum(len(r['chosen'])>len(r['rejected']) for r in rows)
print('Chosen longer in characters:',longer,'/',len(rows))
# Train-only bag-of-word vocabulary; no large models or tokenizers.
terms=sorted(set(re.findall(r'\w+', ' '.join(r[k].lower() for r in train_rows for k in r))))
lookup={w:i for i,w in enumerate(terms)}
def features(examples,side):
    result=torch.zeros(len(examples),len(lookup)+1)
    for i,r in enumerate(examples):
        for word in re.findall(r'\w+', (r['prompt']+' '+r[side]).lower()):
            if word in lookup:result[i,lookup[word]]+=1
        result[i,-1]=len(r[side])/100. # explicit length feature exposes confound
    return result
reward_model=nn.Sequential(nn.Linear(len(lookup)+1,24),nn.Tanh(),nn.Linear(24,1))
opt=torch.optim.Adam(reward_model.parameters(),lr=.02);history=[]
xw=features(train_rows,'chosen');xl=features(train_rows,'rejected')
for step in range(60):
    rw=reward_model(xw).squeeze(-1);rl=reward_model(xl).squeeze(-1)
    loss=F.softplus(-(rw-rl)).mean();opt.zero_grad();loss.backward()
    assert torch.isfinite(loss) and all(torch.isfinite(p.grad).all() for p in reward_model.parameters())
    opt.step();history.append(loss.item())
plt.plot(history);plt.xlabel('Step');plt.ylabel('Pairwise NLL');plt.title('Measured toy reward-model training');plt.show()
@torch.no_grad()
def rm_metrics(examples):
    d=(reward_model(features(examples,'chosen'))-reward_model(features(examples,'rejected'))).squeeze(-1)
    return {'pair_accuracy':d.gt(0).float().mean().item(),'pair_nll':F.softplus(-d).mean().item()}
print('Training:',rm_metrics(train_rows),'Validation:',rm_metrics(valid_rows))
reward_model.eval().requires_grad_(False)
assert all(not p.requires_grad for p in reward_model.parameters())
'''),md('## Bias and validation\n\nAll20 chosen answers are longer in characters. A reward model can exploit length; add balanced counterexamples, prompt diversity and independent tests. The bag-of-words scorer cannot model nuanced semantics, contradictions or prompt-dependent reasoning. Evaluate a separate task suite and scorer calibration before using rewards for RL. The local file has no numeric reward scores, reference answers, annotation confidence or splits; this notebook creates a split and does not invent those fields.')], 'Local JSONL plus reward stage of RLHF_with_PPO_Final_Code.ipynb, source README reference-free DPO correction, notes Chapters02/03.', '1. Remove length feature and compare validation rankings.\n2. Test rewards on repeated words or verbose wrong answers.\n3. Fit logistic calibration on a separate, larger comparison set.')

notebook('04_PPO_From_Scratch.ipynb','04 — PPO from scratch','- Collect recent-policy rollouts and fixed old log probabilities.\n- Calculate GAE, critic targets, clipped actor loss and entropy.\n- Run minibatch PPO on a synthetic episodic environment.',[
md(r'''## Ratio, clipping and total loss

$$
\rho_t=\frac{\pi_\theta(a_t\mid s_t)}{\pi_{old}(a_t\mid s_t)}=\exp(\ell_{new,t}-\ell_{old,t}),
$$

$$
L^{clip}=\mathbb E\min\left(\rho_t\hat A_t,\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)\hat A_t\right),\qquad
\mathcal L=-L^{clip}+c_V\tfrac12\mathbb E(V_\phi-\hat G)^2-c_H\mathbb E H(\pi_\theta).
$$
$\theta$ actor parameters, old fixed behavior policy, $\ell$ selected-action logp, $\hat A$ detached advantage, $\epsilon=.2$ surrogate clip width, $V_\phi$ current critic, $\hat G$ rollout target, $c_V=.5$ value weight and $c_H=.01$ entropy weight. Maximize the surrogate, minimize its negative. For $A=2,\rho=1.5$, clipped contribution2.4; for $A=-2,\rho=.5$, contribution−1.6. Clipping caps beneficial incentive, not parameters, probabilities or KL globally.

This is standard episodic PPO, not reward-model LLM RLHF: environment supplies rewards and no frozen RLHF reference is needed. Shared actor/critic network, no value clipping, constant coefficients and small fixed rollout are declared implementation choices.'''),code(ENV),code(GAE),
code(r'''
r=np.linspace(0,2,200)
plt.plot(r,np.minimum(r,np.clip(r,.8,1.2)),label='A=+1')
plt.plot(r,np.minimum(-r,-np.clip(r,.8,1.2)),label='A=-1')
plt.axvline(.8,color='gray',ls=':');plt.axvline(1.2,color='gray',ls=':');plt.legend();plt.xlabel('Current/old ratio');plt.ylabel('Surrogate (maximize)');plt.title('Analytical curves, not measured training');plt.show()
assert min(1.5*2,1.2*2)==2.4 and min(.5*-2,.8*-2)==-1.6
'''),code(PPO),md('## Stability checks\n\nOld logps and old values are detached; every minibatch uses the same tokens/actions from that rollout. Gradient-norm clipping differs from surrogate clipping. Critic targets use raw advantages; actor normalization is later. True terminals suppress bootstrap; time-limit truncations keep final-observation value but stop recurrence across reset. Track clip fraction, value error, entropy and task returns. Performance here only describes this toy chain.')], 'RLHF PDF PPO ratio/advantage/clipping and notes Chapter04; replaces delegated trainer internals with explicit PyTorch rollout and minibatches.', '1. Increase update epochs and log approximate old/current KL.\n2. Add optional value clipping and explain its target.\n3. Sweep entropy coefficient; compare returns and exploration.')

notebook('06_DPO_From_Scratch.ipynb','06 — DPO from scratch','- Derive optimal KL-regularized policy and implicit reward.\n- Implement response-summed logps with causal shifting and masks.\n- Train and validate a small GRU policy with a frozen reference.',[
md(r'''## Derivation and symbols
For prompt $x$, maximize $\mathbb E_{y\sim\pi}r(x,y)-\beta D_{KL}(\pi\Vert\pi_{ref})$ subject to $\sum_y\pi(y\mid x)=1$. $r$ is scalar reward, $\beta>0$ KL coefficient, and $\pi_{ref}$ fixed supported reference. A Lagrange multiplier yields:

$$
\pi^*(y\mid x)=\frac{\pi_{ref}(y\mid x)e^{r(x,y)/\beta}}{Z(x)},\qquad r=\beta\log\frac{\pi^*}{\pi_{ref}}+\beta\log Z(x).
$$
$Z$ normalizes probabilities. Pairwise rewards for the same prompt cancel $\beta\log Z(x)$, so an explicit reward network is unnecessary.

$$
\mathcal L_{DPO}=-\mathbb E\log\sigma\left(\beta[(\ell_w-\ell_{ref,w})-(\ell_l-\ell_{ref,l})]\right).
$$
$w/l$ mean preferred/rejected responses, $\ell=\sum_t m_t\log\pi(y_t\mid x,y_{<t})$, and $m_t$ completion mask. Do not confuse this sum with ORPO mean logp. Both absolute likelihoods can fall while their relative margin improves. Increasing beta changes both derived regularization interpretation and logistic gradient scale; it is not universally beneficial.'''),code(DATA),
md(r'''## Causal labels and masking
Logits at position $j$ predict token $j+1$. Attention masks exclude padding from attention; completion masks exclude prompt/padding from the objective. EOS is scored once. Pad ID0 is separate from EOS2. Full-sequence character encoding avoids boundary merges; real BPE tokenizers require checking full prompt+completion boundaries and chat-template consistency.'''),code(CAUSAL),code(DPO),code(EVAL)],
'All three DPO source notebooks; final long sources identical, compact version has precision/template issues; notes Chapters05/09. Original handwritten8/3 versus108/103 reward offsets motivate cancellation.', '1. Verify reference gradients remain absent after every update.\n2. Replace response-summed logps with means and explain why the objective changes.\n3. Create noisy pairs and compare validation loss versus raw chosen likelihood.')

notebook('08_GRPO_From_Scratch.ipynb','08 — GRPO from scratch','- Generate same-prompt groups and compute normalized outcome advantages.\n- Handle constant-reward groups without NaN.\n- Train a contextual one-token policy with PPO-style ratio updates and reference KL.',[
md(r'''## Group-relative outcome objective

$$
\mu_x=\frac1G\sum_iR_i,\quad s_x=\sqrt{\frac1G\sum_i(R_i-\mu_x)^2},\quad \hat A_i=\frac{R_i-\mu_x}{s_x+\varepsilon_{norm}}.
$$
$G$ same-prompt responses, $R_i$ outcome reward, $\mu_x$ group mean, $s_x$ population std in this demo and $\varepsilon_{norm}$ stabilizer. Rewards $[1,0,1,0]$ give advantages $[1,-1,1,-1]$. Equal rewards give zero advantages, not successful learning.

$$
J=\mathbb E\frac1G\sum_i\frac1{T_i}\sum_t\left[\min(\rho_{i,t}\hat A_i,\operatorname{clip}(\rho_{i,t},1-\epsilon,1+\epsilon)\hat A_i)-\kappa\hat K_{i,t}\right].
$$
$T_i$ response length, $\rho$ current/old token ratio, $\epsilon$ clipping and $\kappa$ reference KL weight. Original GRPO averages each response, then groups. Later DAPO/token-mean variants change weighting; your source notebook's recorded default was DAPO. No critic is learned in original GRPO, but baseline/advantage calculations remain. Original paper also allows process rewards and learned reward models.

The code simplifies responses to one categorical token ($T=1$). Exact full-distribution KL is used instead of sampled $q-\log q-1$, where $q=\pi_{ref}/\pi_\theta$, avoiding reused-old-sample expectation ambiguity in this finite action space.'''),code(GROUP)],
'GRPO PDF [1,0,1,0] and [9,6,2] examples; Final_GRPO_Practical.ipynb heuristic versus GSM8K paths; notes Chapter06; DeepSeekMath arXiv2402.03300.', '1. Force identical rewards and confirm only KL can update.\n2. Compare population and sample std.\n3. Add variable-length toy responses and contrast per-response versus batch-token weighting.')

notebook('10_ORPO_From_Scratch.ipynb','10 — ORPO from scratch','- Distinguish probability, odds and log odds.\n- Implement stable odds preference plus chosen supervised loss.\n- Train a response-masked GRU without a reference model.',[
md(r'''## Length-normalized odds

$$
\bar\ell_y=\frac{\sum_t m_t\log\pi_\theta(y_t\mid x,y_{<t})}{\sum_t m_t},\quad p_y=e^{\bar\ell_y},\quad o_y=\frac{p_y}{1-p_y}.
$$
$\bar\ell$ mean completion token logp, $m$ mask, $p$ geometric-mean token likelihood score and $o$ odds. These scores do not normalize over all response candidates. Empty completions are invalid.

$$
\Delta_{OR}=\log o_w-\log o_l,\qquad \mathcal L=\mathcal L_{SFT}+\lambda_{OR}[-\log\sigma(\Delta_{OR})].
$$
$w/l$ chosen/rejected; $\lambda_{OR}=.1$ balances imitation and preference. This code averages chosen NLL equally across sequences; TRL's token-averaged SFT can weight variable-length batches differently. TRL calls the coefficient beta, unlike DPO beta or GRPO KL weight. No reference, RM or critic is required.

For toy $p_w=.75,p_l=.25$, odds3 and1/3, ratio9, preference loss.105361, SFT.287682, total.298218. Stable `log(1-exp(logp))` is evaluated with branch indexing and FP32, avoiding inactive singular-branch gradient contamination.'''),code(DATA),code(CAUSAL),code(ORPO),code(r'''
print('Validation uses normalized chosen/rejected score differences:')
with torch.no_grad():
    w=score(policy,pair_batch(valid_rows,'chosen'),True);l=score(policy,pair_batch(valid_rows,'rejected'),True)
    print('Validation mean-logp ranking accuracy:',w.gt(l).float().mean().item())
''')], 'ORPO PDF odds.75/.25 and corrected total; Final_ORPO_Practical.ipynb two environments/inference failure; notes Chapter07; ORPO arXiv2403.07691.', '1. Sweep the preference coefficient and log both components.\n2. Use sum logps in a copy and diagnose length effects.\n3. Compare equal-sequence and equal-token SFT weighting.')

for num,alg in [(7,'DPO'),(11,'ORPO')]:
 cfg=alg+'Config';trainer=alg+'Trainer';tag=alg.lower()
 cpu=HF_PAIR_TRAIN.replace('CONFIG',cfg).replace('TRAINER',trainer).replace('TAG',tag)
 gpu=GPU_PAIRS.replace('CONFIG',cfg).replace('TRAINER',trainer).replace('TAG',tag)
 notebook(f'{num:02d}_{alg}_Using_TRL.ipynb',f'{num:02d} — {alg} using TRL','- Inspect pinned trainer signatures and tokenized preference batches.\n- Run a no-download two-step CPU trainer smoke test.\n- Save/evaluate/reload and optionally fine-tune a pretrained model.',[
 md(f'## Version and behavior boundary\n\nThis recipe targets TRL0.22.2, Transformers4.56.2, Datasets4.3.0, PEFT0.17.1 and Accelerate1.10.1. It uses `processing_class`, not a version-mixed `tokenizer` argument. The CPU model is a random small GPT-2 architecture; it cannot demonstrate useful alignment. The pretrained path is off by default. Read notebook{6 if alg=="DPO" else 10:02d} for explicit math before this abstraction. '+('DPO retains a fixed reference distribution; with a new LoRA adapter the frozen base can supply it.' if alg=='DPO' else 'ORPO combines supervised and odds preference objectives without a reference.')),
 code(DATA),code(HF),code(cpu),
 code(r'''
if RUN_TRL_SMOKE:
    batch=next(iter(trainer.get_train_dataloader()))
    print('Actual collated keys/shapes:',{k:tuple(v.shape) if hasattr(v,'shape') else type(v).__name__ for k,v in batch.items()})
    for k,v in batch.items():
        if isinstance(v,torch.Tensor) and k.endswith('input_ids'):
            assert v.min()>=0 and v.max()<len(tokenizer)
        if isinstance(v,torch.Tensor) and k.endswith('labels'):
            active=v.ne(-100);assert active.any()
    checkpoints=sorted((RUNTIME/('dpo_cpu' if isinstance(trainer,DPOTrainer) else 'orpo_cpu')).glob('checkpoint-*'))
    print('Full trainer checkpoints:',[p.name for p in checkpoints])
    # To resume training: trainer.train(resume_from_checkpoint=str(checkpoints[-1]))
    # Model-only final export is not optimizer/RNG state; resume from checkpoint-*.
'''),md('## Real-model template and memory workflow\n\nUse structured user/assistant messages, template exactly once, inspect truncation before training, mask prompts/padding, and evaluate disjoint prompts. Quantization and PEFT are distinct: this small GPU recipe uses LoRA and supported precision without bitsandbytes. No device_map="auto" is used for training. Five optimizer steps are only a smoke run; enlarge data and evaluate task quality before any alignment claim.'),code(gpu)],
 f'{alg} source notebook walkthroughs and corrected notes Chapters{5 if alg=="DPO" else 7:02d}/09. Exact TRL0.22.2 wheel source retained in api_references; runtime signatures are checked.',
 '1. Inspect the actual labels/masks and decoded prompt boundary.\n2. Reload a checkpoint and verify optimizer step/RNG state.\n3. Compare train/validation preference metrics and response length against the base model.')
PPO_HF=r'''
if RUN_TRL_SMOKE:
    # First train a small scalar RM from real pairs; never use a random RM as evidence.
    tokenizer.padding_side='right'
    rm_cfg=lm_config();rm_cfg.num_labels=1
    reward_model=GPT2ForSequenceClassification(rm_cfg)
    rm_args=RewardConfig(output_dir=str(RUNTIME/'ppo_rm_cpu'),max_steps=2,per_device_train_batch_size=2,learning_rate=1e-4,
                         max_length=128,use_cpu=True,bf16=False,fp16=False,report_to='none',save_strategy='no',remove_unused_columns=False)
    rm_trainer=RewardTrainer(model=reward_model,args=rm_args,processing_class=tokenizer,train_dataset=hf_pairs(train_rows),eval_dataset=hf_pairs(valid_rows))
    rm_trainer.train();print('Reward-model held-out ranking loss:',rm_trainer.evaluate())
    reward_model.eval().requires_grad_(False)
    value_model=copy.deepcopy(reward_model).train().requires_grad_(True)
    policy=GPT2LMHeadModel(lm_config());reference=copy.deepcopy(policy).eval().requires_grad_(False)
    tokenizer.padding_side='left'
    def prompt_dataset(examples):
        return Dataset.from_list([{'input_ids':tokenizer('Question: '+r['prompt']+' Answer:',truncation=True,max_length=64)['input_ids']} for r in examples])
    ppo_args=PPOConfig(output_dir=str(RUNTIME/'ppo_cpu'),per_device_train_batch_size=2,gradient_accumulation_steps=1,
                       total_episodes=4,num_mini_batches=1,num_ppo_epochs=1,response_length=8,
                       local_rollout_forward_batch_size=2,learning_rate=1e-5,kl_coef=.05,cliprange=.2,cliprange_value=.2,
                       gamma=1.,lam=.95,vf_coef=.1,whiten_rewards=False,temperature=1.,stop_token='eos',
                       use_cpu=True,bf16=False,fp16=False,report_to='none',save_strategy='no',logging_steps=1,seed=42)
    trainer=PPOTrainer(args=ppo_args,processing_class=tokenizer,model=policy,ref_model=reference,reward_model=reward_model,
                       value_model=value_model,train_dataset=prompt_dataset(train_rows),eval_dataset=prompt_dataset(valid_rows))
    result=trainer.train();trainer.save_model(str(RUNTIME/'ppo_cpu/final'));tokenizer.save_pretrained(str(RUNTIME/'ppo_cpu/final'))
    print('Actual tiny CPU PPO run:',result)
    # PPO rollout old-logps are not the frozen-reference logps. Critic remains trainable.
    assert all(not p.requires_grad for p in reward_model.parameters())
    assert all(not p.requires_grad for p in reference.parameters())
    assert any(p.requires_grad for p in value_model.parameters())
    trained=trainer.accelerator.unwrap_model(trainer.model).policy.eval()
    query=tokenizer('Question: What is AI? Answer:',return_tensors='pt')
    with torch.no_grad():generated=trained.generate(**query,max_new_tokens=8,do_sample=False,pad_token_id=tokenizer.pad_token_id)
    print('Random-model smoke response (not meaningful):',tokenizer.decode(generated[0,query.input_ids.shape[1]:]))
'''
PPO_GPU=r'''
if RUN_PRETRAINED_GPU:
    assert torch.cuda.is_available()
    from transformers import AutoTokenizer,AutoModelForCausalLM,AutoModelForSequenceClassification
    MODEL_ID='HuggingFaceTB/SmolLM2-135M-Instruct'
    tok=AutoTokenizer.from_pretrained(MODEL_ID)
    # Distinct padding avoids PPO final-token pooling interpreting EOS as padding.
    if tok.pad_token_id is None or tok.pad_token_id==tok.eos_token_id:tok.add_special_tokens({'pad_token':'<|rlhf_pad|>'})
    dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float32
    rm=AutoModelForSequenceClassification.from_pretrained(MODEL_ID,num_labels=1,torch_dtype=dtype)
    rm.resize_token_embeddings(len(tok));rm.config.pad_token_id=tok.pad_token_id
    def chat_pairs(examples):
        return Dataset.from_list([{'prompt':[{'role':'user','content':r['prompt']}], 'chosen':[{'role':'assistant','content':r['chosen']}],
                                   'rejected':[{'role':'assistant','content':r['rejected']}]} for r in examples])
    tok.padding_side='right'
    rm_args=RewardConfig(output_dir=str(RUNTIME/'ppo_rm_gpu'),max_steps=5,per_device_train_batch_size=1,gradient_accumulation_steps=2,
                         learning_rate=1e-5,max_length=256,bf16=dtype==torch.bfloat16,fp16=False,report_to='none',save_strategy='no',remove_unused_columns=False)
    rm_t=RewardTrainer(model=rm,args=rm_args,processing_class=tok,train_dataset=chat_pairs(train_rows),eval_dataset=chat_pairs(valid_rows))
    rm_t.train();print(rm_t.evaluate());rm.eval().requires_grad_(False)
    # Same embedding shape and pad token in all four roles; base token resize performed
    # once before copying so added token weights match the reference exactly.
    actor=AutoModelForCausalLM.from_pretrained(MODEL_ID,torch_dtype=dtype)
    actor.resize_token_embeddings(len(tok));actor.config.pad_token_id=tok.pad_token_id;actor.config.use_cache=False
    ref=copy.deepcopy(actor).eval().requires_grad_(False)
    critic=copy.deepcopy(rm).train().requires_grad_(True)
    tok.padding_side='left';tok.truncation_side='left'
    def prompts(examples):
        return Dataset.from_list([{'input_ids':tok.apply_chat_template([{'role':'user','content':r['prompt']}],tokenize=True,add_generation_prompt=True,truncation=True,max_length=128)} for r in examples])
    args=PPOConfig(output_dir=str(RUNTIME/'ppo_gpu'),total_episodes=8,per_device_train_batch_size=2,num_mini_batches=1,num_ppo_epochs=1,
                   response_length=32,local_rollout_forward_batch_size=2,learning_rate=1e-6,kl_coef=.05,cliprange=.2,gamma=1.,lam=.95,
                   bf16=dtype==torch.bfloat16,fp16=False,report_to='none',stop_token='eos',whiten_rewards=False,save_strategy='steps',save_steps=2)
    ppo=PPOTrainer(args=args,processing_class=tok,model=actor,ref_model=ref,reward_model=rm,value_model=critic,
                   train_dataset=prompts(train_rows),eval_dataset=prompts(valid_rows))
    ppo.train();ppo.save_model(str(RUNTIME/'ppo_gpu/final'));tok.save_pretrained(str(RUNTIME/'ppo_gpu/final'))
    # Compare held-out prompts and scored KL/length/task quality with the starting actor.
    # Eight episodes + a five-step RM are workflow checks, not validated alignment.
'''
notebook('05_PPO_LLM_Finetuning.ipynb','05 — PPO LLM fine-tuning','- Verify a coherent TRL PPO API environment.\n- Run local no-download reward training and four-role PPO smoke test.\n- Understand optional pretrained workflow, padding and model saving.',[
md(r'''## From explicit PPO to token generation
The token state is prompt plus prefix; action is next token. Policy generates, reference supplies KL anchor, reward model scores final response, critic predicts remaining shaped return. PPO retains old rollout logps separately.

$$
R_t=-\kappa[\log\pi_{old}(a_t\mid s_t)-\log\pi_{ref}(a_t\mid s_t)]+\mathbf1_{t=T-1}r_\psi(x,y).
$$
$\kappa$ KL coefficient, $r_\psi$ terminal reward, $T$ active response length. This expresses a common shaping implementation; TRL0.22.2 supports specified k1/k3 estimators and value clipping. Trainer owns token masks, GAE and old/current ratios. The CPU example has distinct PAD/EOS; pretrained recipe adds a new padding token before copying models. Reward is frozen, critic trainable. All four models consume matching vocabulary.

The TRL PPO trainer is not the old `.step(queries,responses,rewards)` value-head API. The source notebook used later experimental paths; this collection pins a release whose exact signatures were imported. Full-parameter small-model PPO is shown; this is not a four-bit memory recipe.'''),code(DATA),code(HF),code(PPO_HF),md('## Optional GPU pipeline\n\nDisabled by default. The reward head starts new and is trained on the real comparison pairs. A tiny RM has serious generalization and length-bias limitations. Choose disjoint prompts for assessment; do not optimize against an unchecked random scorer. Periodic trainer checkpoints enable resume where supported, while the final export saves policy weights.'),code(PPO_GPU)],
'RLHF_with_PPO_Final_Code.ipynb four roles, small RM and six-episode limits; notes Chapters02/04/09; verified TRL0.22.2 PPO source/imports.', '1. Print response masks, old/reference logps and shaped rewards for a rollout.\n2. Test RM on verbose incorrect responses.\n3. Compare saved policy with reference on held-out prompts and record length/KL.')

GRPO_HF=r'''
def integer_answer(text):
    # One final number only; supports signed integers/decimals, rejects junk/extra answers.
    from decimal import Decimal,InvalidOperation
    text=text.strip()
    if not re.fullmatch(r'[+-]?\d+(?:\.\d+)?',text):return None
    try:return Decimal(text)
    except InvalidOperation:return None

def exact_reward(completions,answer,**kwargs):
    result=[]
    for completion,gold in zip(completions,answer):
        text=completion if isinstance(completion,str) else completion[-1]['content']
        parsed=integer_answer(text);result.append(float(parsed is not None and parsed==integer_answer(str(gold))))
    return result
assert exact_reward(['-2','2.0','2 dogs',''],['-2','2','2','0'])==[1.,1.,0.,0.]
# Synthetic arithmetic task. answer is created metadata, NOT a field of local JSONL.
arithmetic=Dataset.from_list([{'prompt':f'What is {a} + {b} ? Answer only the number:', 'answer':str(a+b)} for a,b in [(1,1),(1,2),(2,2),(2,1)]])
if RUN_TRL_SMOKE:
    tokenizer.padding_side='left';model=GPT2LMHeadModel(lm_config())
    # TRL builds non-PEFT reference from config._name_or_path: save/reload local
    # random initialization so the reference resolves locally rather than the Hub.
    initial_path=RUNTIME/'grpo_initial';model.save_pretrained(str(initial_path))
    model=GPT2LMHeadModel.from_pretrained(str(initial_path),local_files_only=True)
    args=GRPOConfig(output_dir=str(RUNTIME/'grpo_cpu'),max_steps=2,per_device_train_batch_size=4,per_device_eval_batch_size=4,
                    gradient_accumulation_steps=1,num_generations=4,max_prompt_length=64,max_completion_length=4,
                    loss_type='grpo',scale_rewards='group',beta=.01,num_iterations=1,epsilon=.2,temperature=1.,
                    learning_rate=1e-4,use_cpu=True,bf16=False,fp16=False,report_to='none',save_strategy='steps',save_steps=1,logging_steps=1,
                    remove_unused_columns=False,use_vllm=False,seed=42)
    trainer=GRPOTrainer(model=model,args=args,processing_class=tokenizer,reward_funcs=exact_reward,train_dataset=arithmetic)
    result=trainer.train();trainer.save_model(str(RUNTIME/'grpo_cpu/final'));tokenizer.save_pretrained(str(RUNTIME/'grpo_cpu/final'))
    print('Actual random-model GRPO smoke:',result)
    print('Most groups may have zero correctness variance; this is API verification, not learning evidence.')
'''
GRPO_GPU=r'''
if RUN_PRETRAINED_GPU:
    assert torch.cuda.is_available()
    from transformers import AutoTokenizer,AutoModelForCausalLM
    from peft import LoraConfig
    MODEL_ID='HuggingFaceTB/SmolLM2-135M-Instruct'
    tok=AutoTokenizer.from_pretrained(MODEL_ID);tok.padding_side='left'
    if tok.pad_token_id is None:tok.pad_token=tok.eos_token
    examples=[]
    for a in range(1,6):
        for b in range(1,6):
            examples.append({'prompt':[{'role':'user','content':f'What is {a}+{b}? Return just the number.'}],'answer':str(a+b)})
    # Explicit split; these synthetic arithmetic records are not human preferences.
    training=Dataset.from_list(examples[:20]);validation=Dataset.from_list(examples[20:])
    dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float32
    model=AutoModelForCausalLM.from_pretrained(MODEL_ID,torch_dtype=dtype);model.config.use_cache=False
    config=GRPOConfig(output_dir=str(RUNTIME/'grpo_gpu'),max_steps=5,per_device_train_batch_size=4,per_device_eval_batch_size=4,
                      num_generations=4,gradient_accumulation_steps=1,max_prompt_length=128,max_completion_length=32,
                      loss_type='grpo',scale_rewards='group',beta=.01,num_iterations=1,epsilon=.2,temperature=.9,
                      learning_rate=1e-5,bf16=dtype==torch.bfloat16,fp16=False,use_vllm=False,remove_unused_columns=False,
                      eval_strategy='steps',eval_steps=5,save_strategy='steps',save_steps=5,report_to='none')
    trainer=GRPOTrainer(model=model,args=config,processing_class=tok,reward_funcs=exact_reward,train_dataset=training,eval_dataset=validation,
                        peft_config=LoraConfig(task_type='CAUSAL_LM',r=8,lora_alpha=16,target_modules=['q_proj','v_proj']))
    trainer.train();print(trainer.evaluate());trainer.save_model(str(RUNTIME/'grpo_gpu/final'));tok.save_pretrained(str(RUNTIME/'grpo_gpu/final'))
'''
notebook('09_GRPO_Using_TRL.ipynb','09 — GRPO using TRL','- Verify exact-answer rewards, parser edge cases and metadata.\n- Specify grouping, reference KL and loss variant explicitly.\n- Run local tiny trainer smoke and optional pretrained arithmetic fine-tuning.',[
md(r'''## Reward and group design
Group size $G=4$ must divide the effective generation batch. The CPU recipe uses batch4/accumulation1 on one process. In multi-process training check global generation settings. Set `loss_type='grpo'` explicitly because this release defaults to DAPO. `beta=.01` is reference KL coefficient, not DPO scaling. `scale_rewards='group'` uses within-prompt normalization, with library std conventions differing from notebook08's population std.

Correctness parses one numeric answer with decimal normalization, so `2.0` can equal `2` and negative answers are not rejected by `.isdigit()`. Extra text fails by design; format validity and task correctness remain distinct. No lexical similarity or uncertainty-penalty reward is used. A random model may produce all-wrong groups: zero variance means no correctness gradient, though KL still applies.'''),code(DATA),code(HF),code(GRPO_HF),md('## Optional reasoning workflow\n\nThe real-model branch is off. It uses synthetic arithmetic with separate validation, structured prompts, no vLLM dependency, explicit grouping and short generation. Log reward mean/std, constant-group fraction, numeric parse success, lengths and KL. Increase problem difficulty gradually; do not add random reward noise to disguise zero variance.'),code(GRPO_GPU)],
'GRPO source group examples and notebook batch1/G4, lexical correctness and `.isdigit()` pitfalls; notes Chapter06; exact TRL0.22.2 config/source.', '1. Test parser equivalence, malformed tags and empty completions.\n2. Intentionally misconfigure G and observe config validation.\n3. Compare loss_type grpo/dapo only after stating the different weighting.')

notebook('12_PPO_DPO_GRPO_ORPO_Comparison.ipynb','12 — PPO, DPO, GRPO and ORPO comparison','- Compare supervision, extra model roles and objectives.\n- Plot analytical loss/clipping/normalization behavior.\n- Make conditional resource and algorithm choices.',[
md(r'''## Component and supervision comparison
| Method | Data and computation | Reference | Learned RM | Critic |
|---|---|---|---|---|
| PPO classical RLHF | Fresh prompts/responses; reward; GAE and clipping | Usually | Classical pipeline, or replace with function | Usually |
| DPO | Offline chosen/rejected pairs; reference-adjusted sequence logp margin | Standard formulation | No explicit RM | No |
| GRPO original | Same-prompt response groups; relative rewards and clipped objective | Original KL formulation | Optional scorer | No learned critic |
| ORPO | Offline pairs; chosen NLL plus normalized-likelihood log odds | No | No | No |

PPO is a general optimizer and can use an environment reward without an RM. DPO `ref_model=None` can share the base reference with PEFT. GRPO variants can remove KL/reference when coefficient0; they are not all identical to original GRPO. No method guarantees better alignment from lower training loss.

$$
\mathcal L_{DPO}=\operatorname{softplus}(-\beta m),\quad m=(\ell_w-\ell_l)-(\ell_{ref,w}-\ell_{ref,l}),\quad
\mathcal L_{ORPO}=-\bar\ell_w+\lambda_{OR}\operatorname{softplus}(-\Delta_{OR}).
$$
$\ell$ summed completion logp, $\bar\ell$ mean logp, $m$ relative margin, $\Delta_{OR}$ log-odds difference, beta DPO scale and lambda ORPO component weight. These look like logistic losses but their inputs and regularization differ.'''),
code(r'''
margin=np.linspace(-5,5,200);ratio=np.linspace(0,2,200)
fig,ax=plt.subplots(1,3,figsize=(13,3))
for beta in [.1,.5,1.]:ax[0].plot(margin,np.logaddexp(0,-beta*margin),label=f'beta={beta}')
ax[0].set(title='Analytical DPO loss',xlabel='Relative margin',ylabel='Loss');ax[0].legend()
ax[1].plot(ratio,np.minimum(ratio,np.clip(ratio,.8,1.2)),label='A=1');ax[1].plot(ratio,np.minimum(-ratio,-np.clip(ratio,.8,1.2)),label='A=-1');ax[1].set(title='PPO clipping',xlabel='Ratio',ylabel='Surrogate');ax[1].legend()
rewards=np.array([1.,0.,1.,0.]);adv=(rewards-rewards.mean())/rewards.std()
ax[2].bar(range(4),adv);ax[2].set(title='Illustrative GRPO group',xlabel='Completion',ylabel='Relative advantage');plt.tight_layout();plt.show()
# Model-state estimate only: assumptions FP32 weights+grads+Adam moments=16 bytes
# per trainable parameter, frozen FP32 copy=4. Excludes activations, buffers, caches.
P=135_000_000
estimates={'Single trainable model':16*P/1e9,'Policy + frozen reference':20*P/1e9,'PPO 2 trainable + 2 frozen':40*P/1e9}
print('Illustrative GB (decimal), NOT measured VRAM:',estimates)
'''),md('## Selection workflow\n\nOnly offline preference pairs and a strong SFT checkpoint: start with DPO and validate the reference. Joint imitation/preference with no reference budget: consider ORPO. Verifiable reward plus generation capacity: GRPO is reasonable. Established reward model with broader online reward objective: PPO may be appropriate, with more engineering and critic overhead. Group generation cost scales with G and response length; memory scales with model states and activations, not just named roles. PEFT/reference caching/quantization can change rankings. The 20-row local dataset is educational and length-confounded; no universal winner can be concluded from it.')],
'All PDF/notebook model-role/algorithm contrasts and corrected notes Chapter08; cost figures are explicit state-only assumptions.', '1. Estimate state memory for LoRA while retaining frozen base copies.\n2. Design a fair evaluation suite rather than comparing incomparable training losses.\n3. Choose a method for offline pairs versus a unit-test correctness reward.')

notebook('13_End_to_End_LLM_Alignment.ipynb','13 — End-to-end small alignment project','- Audit and split the real dataset, then train a tiny causal policy.\n- Compare SFT baseline, DPO and ORPO with fixed evaluation prompts.\n- Save/reload models and record actual metrics without claiming LLM-scale success.',[
md(r'''## Project scope and reproducibility
This CPU project uses a random small character GRU causal LM, not a pretrained instruction model. SFT is trained first; DPO's reference is then a frozen SFT copy, while ORPO also starts from identical SFT weights without a reference in its objective. Prompt-separated train14/validation3/test3 is fixed. Vocabulary is derived from observed characters across the small file (transductive tokenizer design, not reward-label fitting); production vocabularies are fixed pretrained tokenizers.

$$
\mathcal L_{SFT}=-\mathbb E\bar\ell_w,\quad \mathcal L_{DPO}=\operatorname{softplus}(-\beta m),\quad
\mathcal L_{ORPO}=\mathcal L_{SFT}+\lambda_{OR}\operatorname{softplus}(-\Delta_{OR}).
$$
$\bar\ell_w$ mean chosen completion logp, $m$ reference-adjusted summed-logp pair margin, $\Delta_{OR}$ normalized-likelihood log odds. Full definitions/tests are repeated below so this notebook runs independently. Equal-sequence SFT averaging is an educational weighting choice; TRL averages tokens in some paths. Every measured number below comes from executed CPU code, not source saved outputs.'''),code(DATA),code(CAUSAL),
code(r'''
def dpo_objective(w,l,rw,rl,beta=.1):return F.softplus(-beta*((w-l)-(rw-rl))).mean()
def stable_log1mexp(x):
    if (x>=0).any():raise ValueError('Require negative logp')
    y=torch.empty_like(x);far=x < -math.log(2)
    y[far]=torch.log1p(-x[far].exp());y[~far]=torch.log(-torch.expm1(x[~far]));return y
def orpo_objective(w,l):return -w.mean()+.1*F.softplus(-((w-stable_log1mexp(w))-(l-stable_log1mexp(l)))).mean()
base=TinyLM();chosen=pair_batch(train_rows,'chosen');rejected=pair_batch(train_rows,'rejected')
opt=torch.optim.Adam(base.parameters(),lr=.003);curves={'SFT':[],'DPO':[],'ORPO':[]}
for step in range(25):
    loss=-score(base,chosen,True).mean();finite_step(loss,base,opt);curves['SFT'].append(loss.item())
reference=copy.deepcopy(base).eval().requires_grad_(False)
models={'SFT':copy.deepcopy(base)}
with torch.no_grad():rw=score(reference,chosen);rl=score(reference,rejected)
for name in ['DPO','ORPO']:
    model=copy.deepcopy(base);opt=torch.optim.Adam(model.parameters(),lr=.002)
    for step in range(25):
        if name=='DPO':loss=dpo_objective(score(model,chosen),score(model,rejected),rw,rl)
        else:loss=orpo_objective(score(model,chosen,True),score(model,rejected,True))
        finite_step(loss,model,opt);curves[name].append(loss.item())
    models[name]=model
assert all(p.grad is None for p in reference.parameters())
fig,axes=plt.subplots(1,3,figsize=(12,3))
for axis,(name,curve) in zip(axes,curves.items()):axis.plot(curve);axis.set(title=name+' measured training loss',xlabel='Step',ylabel='Algorithm-specific loss')
plt.tight_layout();plt.show()
'''),code(r'''
@torch.no_grad()
def metrics(model,examples):
    model.eval();cw=pair_batch(examples,'chosen');cl=pair_batch(examples,'rejected')
    w=score(model,cw);l=score(model,cl);wm=score(model,cw,True);lm=score(model,cl,True)
    rw=score(reference,cw);rl=score(reference,cl)
    return {'sum_logp_accuracy':w.gt(l).float().mean().item(),'mean_logp_accuracy':wm.gt(lm).float().mean().item(),
            'relative_margin':((w-l)-(rw-rl)).mean().item(),'chosen_nll':(-wm).mean().item()}
validation={name:metrics(model,valid_rows) for name,model in models.items()}
print('Validation:',json.dumps(validation,indent=2))
# One final fixed test comparison; do not tune against this small test set.
test={name:metrics(model,test_rows) for name,model in models.items()}
print('Test:',json.dumps(test,indent=2))
experiment={'seed':42,'origin':'real local20-row preference file (Git fallback if missing)','train_prompts':[r['prompt'] for r in train_rows],
            'validation':validation,'test':test,'torch':torch.__version__,'model':'random character GRU24/32','steps_per_stage':25,
            'limits':['three test prompts','length confound','transductive character vocabulary','no pretrained LLM','single seed']}
project=RUNTIME/'alignment_project';project.mkdir(exist_ok=True)
(project/'metrics.json').write_text(json.dumps(experiment,indent=2))
for name,model in models.items():
    path=project/(name.lower()+'.pt');torch.save({'state':model.state_dict(),'vocab':vocab},path)
    loaded=TinyLM();loaded.load_state_dict(torch.load(path,weights_only=True)['state']);loaded.eval()
    x=pair_batch(test_rows,'chosen')[0]
    with torch.no_grad():assert torch.allclose(model(x),loaded(x))
print('All local checkpoint reloads agree. Experiment:',project)
'''),md('## Extend to actual LLM alignment\n\nUse notebook07/11 to replace TinyLM with a compatible pretrained causal model and tokenizer; enable GPU only intentionally. Use notebook03 then05 for reward-model PPO, or notebook09 for verifiable group rewards. Keep SFT/reference roles and evaluation data fixed across comparisons, log resources, and perform instruction/task regressions. This project compares pair scoring, not human win rate or safety. No conclusion of universal superiority follows from three test pairs.')],
'Actual JSONL schema/audit, DPO/ORPO source practical workflows and saved-logp cautions, notes Chapters03/05/07/10. A new reproducible educational project, not reproduced original large-model training.', '1. Train a vocabulary using only train rows and add an UNK policy; compare leakage implications.\n2. Repeat three seeds and report variation, without tuning on test.\n3. Add a held-out task-generation suite and baseline length analysis.')
print('Created',len(list(OUT.glob('*.ipynb'))),'valid JSON notebook files.')
