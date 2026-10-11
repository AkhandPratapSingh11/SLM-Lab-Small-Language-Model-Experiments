"""One-time math-delimiter migration; preserve code/literal Markdown and formula bodies.
All reports stay within the knowledge base. Formula-bearing files are explicitly scoped
following a recursive inspection (escaped vendor arrays/URLs are not math).
"""
from pathlib import Path
import re,json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'RLHF_COMPLETE_NOTES'
NAMES=['01_REINFORCEMENT_LEARNING_FUNDAMENTALS.md','02_LLM_ALIGNMENT_AND_RLHF.md','03_PREFERENCE_DATA_AND_REWARD_MODELS.md','04_PPO_IN_DEPTH.md','05_DPO_IN_DEPTH.md','06_GRPO_IN_DEPTH.md','07_ORPO_IN_DEPTH.md','12_GLOSSARY_AND_FORMULA_CHEATSHEET.md']
def code_regions(text):
 # Protect fenced blocks and inline backtick spans, including literal LaTeX examples.
 spans=[];offset=0;fence=None;start=0
 for line in text.splitlines(keepends=True):
  match=re.match(r'^\s*(`{3,}|~{3,})',line)
  if fence:
   if match and match[1][0]==fence[0] and len(match[1])>=len(fence):spans.append((start,offset+len(line)));fence=None
  elif match:fence=match[1];start=offset
  offset+=len(line)
 if fence:spans.append((start,len(text)))
 for m in re.finditer(r'(`+)([^`]|(?!\1)`)*?\1',text):
  if not any(a<=m.start()<b for a,b in spans):spans.append(m.span())
 return spans
report=[]
for name in NAMES:
 p=OUT/name;old=p.read_text();spans=code_regions(old)
 matches=[m for m in re.finditer(r'\\\[\s*\n(.*?)\n\s*\\\]',old,re.S) if not any(a<=m.start()<b for a,b in spans)]
 new=old
 for m in reversed(matches):new=new[:m.start()]+'$$\n'+m[1]+'\n$$'+new[m.end():]
 # Preserve formula bodies; each converted block gets blank paragraph boundaries.
 for m in reversed(list(re.finditer(r'(?m)^\$\$\n(.*?)\n\$\$$',new,re.S))):
  left=new[:m.start()];right=new[m.end():]
  if left and not left.endswith('\n\n'):left+='\n'
  if right and not right.startswith('\n\n'):right='\n'+right
  new=left+m.group()+right
 formulas=re.findall(r'(?m)^\$\$\n(.*?)\n\$\$$',new,re.S)
 assert formulas==[m[1] for m in matches],name+' formula preservation failed'
 before_code=[old[a:b] for a,b in code_regions(old)];after_code=[new[a:b] for a,b in code_regions(new)]
 assert before_code==after_code,name+' literal/code preservation failed'
 p.write_text(new)
 report.append({'file':name,'display_equations':len(matches),'formula_bodies_unchanged_by_delimiter_conversion':True,'literal_code_preserved':True,'before_sha256':hashlib.sha256(old.encode()).hexdigest()})
# Fixed rollout value estimates must be the same in TD residual and return target.
p=OUT/NAMES[0];s=p.read_text();s=s.replace(r'\delta_t=R_t+\gamma(1-d_t)V_\phi(s_{t+1})-V_\phi(s_t).',r'\delta_t=R_t+\gamma(1-d_t)V_{\mathrm{old}}(s_{t+1})-V_{\mathrm{old}}(s_t).').replace('d_t is a genuine terminal indicator; φ are critic parameters. Generalized Advantage Estimation mixes short and long bootstrap estimates:',r'$d_t$ is a genuine terminal indicator. $V_{\mathrm{old}}=V_{\phi_{\mathrm{old}}}$ denotes the fixed rollout-time critic estimate, with critic parameters $\phi_{\mathrm{old}}$. Use these same detached estimates in the TD residual and return target; $V_\phi$ later denotes the critic being optimized. Generalized Advantage Estimation mixes short and long bootstrap estimates:')
p.write_text(s)
(OUT/'assets/math_migration.json').write_text(json.dumps(report,indent=2))
print('Updated',len(report),'chapters;',sum(r['display_equations'] for r in report),'display equations; code/literal regions unchanged.')
