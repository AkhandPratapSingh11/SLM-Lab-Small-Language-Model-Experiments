"""Validate constructor keywords in EVERY code branch against installed pinned APIs."""
from pathlib import Path
import json,ast,inspect
from trl import PPOTrainer,PPOConfig,DPOTrainer,DPOConfig,GRPOTrainer,GRPOConfig,ORPOTrainer,ORPOConfig,RewardTrainer,RewardConfig
ROOT=Path(__file__).resolve().parent
classes={c.__name__:c for c in [PPOTrainer,PPOConfig,DPOTrainer,DPOConfig,GRPOTrainer,GRPOConfig,ORPOTrainer,ORPOConfig,RewardTrainer,RewardConfig]}
checks=[];errors=[]
for p in ROOT.glob('*.ipynb'):
 nb=json.loads(p.read_text())
 for i,c in enumerate(nb['cells'],1):
  if c['cell_type']!='code':continue
  for n in ast.walk(ast.parse(''.join(c['source']))):
   if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id in classes:
    sig=inspect.signature(classes[n.func.id]);unknown=[k.arg for k in n.keywords if k.arg and k.arg not in sig.parameters]
    checks.append({'notebook':p.name,'cell':i,'constructor':n.func.id,'unknown_keywords':unknown})
    if unknown:errors.append(checks[-1])
(ROOT/'api_call_validation.json').write_text(json.dumps({'calls_checked':len(checks),'errors':errors,'checks':checks},indent=2))
print('Trainer/config calls checked:',len(checks),'unknown keywords:',errors)
raise SystemExit(bool(errors))
