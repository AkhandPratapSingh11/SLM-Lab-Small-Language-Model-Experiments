"""Illustrative executable PyTorch helpers. Requires PyTorch; no models downloaded.
Mask construction and chat-template boundary verification remain caller responsibilities.
"""
import math
import torch
import torch.nn.functional as F

def completion_logps(logits,input_ids,completion_mask,attention_mask,average=False):
 if logits.shape[:2]!=input_ids.shape:raise ValueError('Logit/input shapes disagree')
 if completion_mask.shape!=input_ids.shape or attention_mask.shape!=input_ids.shape:raise ValueError('Mask shapes disagree')
 target=input_ids[:,1:]
 if target.numel() and (target.min()<0 or target.max()>=logits.shape[-1]):raise ValueError('Token ID outside vocabulary')
 mask=completion_mask[:,1:].bool() & attention_mask[:,1:].bool() & attention_mask[:,:-1].bool()
 count=mask.sum(-1)
 if (count==0).any():raise ValueError('Empty completion after shift/truncation')
 chosen=F.log_softmax(logits[:,:-1].float(),-1).gather(-1,target.unsqueeze(-1)).squeeze(-1)
 total=chosen.masked_fill(~mask,0).sum(-1)
 return total/count if average else total

def dpo_loss(chosen,rejected,ref_chosen,ref_rejected,beta):
 if beta<=0:raise ValueError('beta must be positive')
 margin=beta*((chosen-rejected)-(ref_chosen.detach()-ref_rejected.detach()))
 return F.softplus(-margin).mean()

def log1mexp(logp):
 """Stable log(1-exp(logp)); valid only for strictly negative logp."""
 logp=logp.float()
 if (logp>=0).any():raise ValueError('Log likelihood must be strictly negative')
 result=torch.empty_like(logp)
 far=logp < -math.log(2)
 result[far]=torch.log1p(-torch.exp(logp[far]))
 result[~far]=torch.log(-torch.expm1(logp[~far]))
 return result

def orpo_loss(chosen_mean_logp,rejected_mean_logp,coefficient):
 """Token-mean chosen NLL plus preference term; no sequence probability sum."""
 if coefficient<0:raise ValueError('Coefficient must be nonnegative')
 w=chosen_mean_logp.float();l=rejected_mean_logp.float()
 margin=(w-log1mexp(w))-(l-log1mexp(l))
 sft=-w.mean();pref=F.softplus(-margin).mean()
 return sft+coefficient*pref,{'sft':sft,'preference':pref,'log_odds_margin':margin}

if __name__=='__main__':
 logits=torch.zeros(1,4,5,requires_grad=True);ids=torch.tensor([[1,2,3,4]])
 mask=torch.tensor([[0,0,1,1]]);att=torch.ones_like(mask)
 score=completion_logps(logits,ids,mask,att)
 assert torch.allclose(score,torch.tensor([-2*math.log(5)]))
 total,parts=orpo_loss(torch.tensor([math.log(.75)]),torch.tensor([math.log(.25)]),.1)
 assert abs(total.item()-.298218124)<1e-6
 assert abs(dpo_loss(torch.tensor([0.]),torch.tensor([0.]),torch.tensor([0.]),torch.tensor([0.]),.1).item()-math.log(2))<1e-6
 (-score.mean()).backward();assert torch.isfinite(logits.grad).all()
 print('Mask/logp, DPO baseline, ORPO numeric example and finite gradient checks passed.')
