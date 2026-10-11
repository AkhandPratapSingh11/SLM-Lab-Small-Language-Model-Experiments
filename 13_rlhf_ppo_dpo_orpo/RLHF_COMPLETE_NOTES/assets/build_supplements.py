from pathlib import Path
import json,re
OUT=Path(__file__).resolve().parents[1];SRC=OUT.parent;AUD=OUT/'assets/source_audit'
def write(p,s):
 p=OUT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.strip()+'\n')
topics={
'DPO-Handwritten-Notes.pdf':['Classical alignment pipeline','Pretraining and gravity SFT example','Preference and safe medical response','SFT versus DPO diagram','RLHF recap','GRPO costs and motivation','DPO fever and synthetic preference example','Reference model','Benefits','Limitations','Data and mathematical objective','Relative comparison scores','Positive/negative score example','Symbol definitions','Paper optimal-policy versus DPO loss','Implicit reward','Rewards 8/3 versus 108/103 offset example','Paper results'],
'DPO-Updated-handwritten-notes.pdf':['Pipeline','Gravity SFT','Safe medical response','SFT versus DPO','RLHF recap','GRPO motivation','Fever and synthetic preference','Reference model','Benefits','Limitations','Implicit reward and additive offset','Score comparison','Mathematics','Relative scores','Worked numeric example','Symbols','Result scope caveat','Paper results','Blank'],
'DPO-Handwritten-final-update-Notes.pdf':['Agenda','Pipeline','Pretraining','Gravity SFT','Medical safety','SFT versus DPO diagram','RLHF','GRPO motivation','Fever and synthetic preference','Reference model','Benefits','Limitations','Implicit reward','Logistic equation and confidence example','Symbols','Dataset and score steps','Numeric example','Results','Blank','Blank','Blank'],
'GRPO-Handwritten-Final-Notes.pdf':['Agenda','DeepSeek family and coder-to-math context','Paper context and small handwritten branching note','2+2 group rewards [1,0,1,0]','Workflow','PPO versus group illustration','Benefits','Group rewards [9,6,2] illustration','Reward signal remains essential','Learned RM versus reward function','R1 rule rewards','Blank'],
'LLM-Finetuning-ORPO.pdf':['Agenda','Authors, venue and employment statements','Monolithic alignment','Workflow','Deployment claims','SFT limitations and fever example','Algorithm comparison','Reference-free design','Adoption claims','Blank','Objective','Likelihood .75/.25 and odds','Odds ratio 9 and log odds','Sigmoid and preference loss','Coefficient and reversed comparison','Reversed comparison continued','Benefits and limitations'],
'RLHF-Updated-Recent-Latest.pdf':['Agenda','Training stages and comparison','Exam-answer preference and small UI screenshot','SFT limitations','Pretraining','SFT','France/Germany example','Alignment goals','AI taxonomy','RL and games','Timeline','Deep RL and supervised comparison','Gradient intuition','Learning paradigms','Car and baby feedback','Value versus policy learning','Repeated timeline','Q, DQN and PPO','Treasure crossroad','Q values 10/50/20','Table scaling problem','DQN','DQN workflow','Replay and target networks','Grid illustration','Q=4 and reward=5','Next max=6 and target=10.4','Squared error=40.96','Continuous-action discussion and LLM motivation','PPO advantage 5-3','Actor-critic','PPO diagram','Robot policy','Ratio .72/.60','LLM reward 8/value 6','Advantage and clipping','Alignment pipeline','RLHF and RM','Classical RLHF diagram','Human labels and HH source','Reward model','Four roles and human-feedback qualification','Blank','Clipping illustration','Gradual policy updates','Blank','Blank','Blank','Blank','Blank']}
ledger=['# PDF page-by-page reading ledger','All 137 rendered page images were visually reviewed. Embedded text and OCR are supplementary: formulas were checked against readable page images and primary papers. “Blank” means no substantive teaching content. Topics are descriptive interpretations, not exact transcriptions. Small screenshot text and a few compact handwritten fragments remain uncertain; see the limitations below.']
for name,ts in topics.items():
 stem=Path(name).stem
 ledger+=['\n## '+name,'| Page | Content inspected | Reading status / trace |','|---|---|---|']
 for i,t in enumerate(ts,1):
  notes='Visually reviewed; '+('blank page.' if t=='Blank' else 'use topic with chapter corrections.')
  if (name.startswith('RLHF') and i==3) or (name.startswith('GRPO') and i==3):notes+=' Tiny inset text/handwriting not exactly transcribed.'
  ledger.append(f'| {i} | {t} | {notes} [Image]({stem}/page-{i:02d}.png) · [OCR]({stem}/page-{i:02d}.txt) |')
 ledger.append(f'\n[Embedded-text extraction]({stem}_extracted.txt). Raster OCR may omit or scramble superscripts, ratios and diagrams; do not treat it as authoritative math.')
write('assets/source_audit/PDF_PAGE_LEDGER.md','\n\n'.join(ledger[:2])+'\n'+'\n'.join(ledger[2:]))
nbmeta={
'DPO_Training.ipynb':('47-cell detailed TRL DPO/QLoRA workflow; inline 4 pairs, optional JSON and external dataset; evaluation, saved metrics, adapter reload.', '05,09,10', 'Source cells exactly match Final version; output metadata differs. One held-out pair and matching metrics do not prove independent runs.'),
'DPO_Training_Final.ipynb':('Same 47 source cells as DPO_Training; recorded later dependency versions and same main metrics.','05,09,10','Final name does not imply an implementation change; tiny evaluation and T4 precision flag need qualification.'),
'Final_DPO.ipynb':('15-cell prototype: full downloaded UltraFeedback, Qwen2.5-0.5B LoRA, training and inference.','05,09,10','Inline literal unused; bad device precision branches, boundary warnings and KeyboardInterrupt. End-to-end success unverified.'),
'Final_GRPO_Practical.ipynb':('54 cells: 8-prompt SmolLM heuristic-reward workflow, then separate Unsloth Qwen/GSM8K XML reward workflow.','06,08,09,10,11','First path saved default DAPO loss; lexical reward is not correctness. Second path no outputs, batch/group and numeric parsing need verification.'),
'Final_ORPO_Practical.ipynb':('33 cells: standard experimental TRL ORPO on 100 UltraFeedback examples; separate older Unsloth environment on 500.','07,08,09,10,11','First training has output but saved inference CUDA assert; second path no outputs. State-dependent deletion, version mixing and prompt extraction issues.'),
'RL_Fundamental.ipynb':('28 cells: bandit-like dictionary, synthetic DQN update, Stable-Baselines3 PPO CarRacing demo.','01,04,11','First is not full Q-learning; DQN has no environment/replay loop; requested100 PPO steps collect2048 due rollout length.'),
'RLHF_with_PPO_Final_Code.ipynb':('23 cells: 4-pair RewardTrainer, frozen RM/reference, trainable critic, experimental PPOTrainer and final inference.','02,03,04,09,10,11','Default inline dataset rather than local file. No eval, 6 episodes, singleton variance warning, full-prompt inference; internal tensors delegated to installed TRL.')}
# Every cell has a readable description plus full source/output links. Blocks are detailed in algorithm chapters.
nb=['# Notebook cell-by-cell audit','Cell numbers are 1-based JSON order, including Markdown and commented cells. All 247 source cells and relevant outputs were read; original notebooks were not executed here. Source snippets below identify each cell, and linked extracts preserve the complete cell and outputs. Stored success is distinguished from source intent.']
for name,(desc,chs,limit) in nbmeta.items():
 data=json.loads((SRC/name).read_text());stem=Path(name).stem
 nb+=['\n## '+name,desc+' Chapters: '+chs+'. '+limit,f'[Original](../../../{name}) · [All sources]({stem}_source.txt) · [Full cells and saved outputs]({stem}_cells.md)','| Cell | Type | Source role / identifying content | Saved output |','|---|---|---|---|']
 for i,c in enumerate(data['cells'],1):
  s=''.join(c.get('source',[])).strip();lines=[x.strip() for x in s.splitlines() if x.strip()]
  ident=(lines[0] if lines else '(empty)')
  if ident in ('[','{','import os','import torch','from datasets import load_dataset') and len(lines)>1:ident+='; '+lines[1]
  if len(ident)>160:ident=ident[:157]+'…'
  ident=ident.replace('|','\\|').replace('`','').replace('<','&lt;')
  outputs=c.get('outputs',[]);types=[]
  for o in outputs:
   k=o.get('output_type','unknown')
   if k=='error':k+=': '+o.get('ename','')
   if 'image/png' in o.get('data',{}):k+=' (PNG inspected)'
   types.append(k)
  status=', '.join(dict.fromkeys(types)) or 'None stored'
  nb.append(f'| {i} | {c["cell_type"]} | {ident} | {status} |')
 nb.append('\n**How to read:** installation/import cells establish environment; dataset/template cells establish context; model/config cells determine trainable roles; trainer calls own loss/rollouts when delegated. An empty output does not verify execution. See the linked algorithm chapter for interpreted variable flow and corrections.')
write('assets/source_audit/NOTEBOOK_AUDIT.md','\n'.join(nb))
inv=['# Source inventory and consolidation','All 15 expected sources were inspected without modifying them. Original SHA-256 values are in [the hash manifest](assets/source_audit/original_hashes.json). Page counts: 137; notebook cells: 247. [Page ledger](assets/source_audit/PDF_PAGE_LEDGER.md) and [cell ledger](assets/source_audit/NOTEBOOK_AUDIT.md) provide granular traceability.','## PDF sources','| Source | Pages and unique contribution | Chapters | Limits / corrections |','|---|---|---|---|']
for name,ts in topics.items():
 if name.startswith('DPO'):
  ch='02,03,05,08,11,12';unique={'DPO-Handwritten-Notes.pdf':'Older equation/implicit-reward progression and additive-offset example.','DPO-Updated-handwritten-notes.pdf':'Explicit offset ambiguity and paper-result caveat.','DPO-Handwritten-final-update-Notes.pdf':'Expanded agenda and logistic numeric confidence discussion.'}[name];lim='Raster handwriting; blank pages listed in ledger. Reference and reward-ratio notation repaired, likelihood trend qualified.'
 elif name.startswith('GRPO'):ch='06,08,11,12';unique='Groups [1,0,1,0] and [9,6,2], coder-to-math context, reward versus RM distinction.';lim='Raster handwriting; mean-only advantage clarified with original std normalization. Small branching fragment uncertain; timeline claims not treated as benchmarks.'
 elif name.startswith('LLM'):ch='07,08,11,12';unique='Geometric likelihood/odds explanation, .75/.25 toy calculation and reversal, monolithic motivation.';lim='Embedded text plus formula imagery; blank p10. Odds arithmetic corrected. Adoption/employment claims unverified.'
 else:ch='01,02,03,04,08,11,12';unique='Games, treasure, Q10/50/20, DQN4→10.4/MSE40.96, PPO ratio1.2/advantage examples and four-model pipeline.';lim='Raster handwriting and blank pages. Tiny p3 screenshot uncertain. Hard-bound clipping, immediate reward advantage, taxonomy and safety claims qualified.'
 inv.append(f'| [{name}](../{name}) | {len(ts)}. {unique} | {ch} | {lim} |')
inv+=['\n## Notebook sources','| Source | Cells / actual workflow | Chapters | Limits |','|---|---|---|---|']
for name,(d,c,l) in nbmeta.items():
 n=len(json.loads((SRC/name).read_text())['cells']);inv.append(f'| [{name}](../{name}) | {n}. {d} | {c} | {l} |')
inv+=['\n## Dataset and original README','| Source | Inspection result | Chapters / limits |','|---|---|---|', '| [reward_preferences_dataset.jsonl](../reward_preferences_dataset.jsonl) | All20 lines parsed; exact fields prompt/chosen/rejected are nonempty strings; no invalid rows or exact duplicates; chosen longer in characters20/20. | 03,09,10,11. No scores, reference_answer, splits or annotation provenance. [Statistics](assets/source_audit/dataset_report.json). |','| [README.md](../README.md) | Entire existing chapter links/context read; its alignment-method framing preserved as orientation. | 00,02,08. Standard DPO incorrectly categorized reference-free; corrected here, original untouched. |','\n## Consolidation policy','The final/updated PDFs refine organization but do not erase older useful examples. DPO offset examples and final sigmoid interpretation are both retained; common pipeline material is centralized in Chapter02. The two long DPO notebook sources are identical, so one execution walkthrough is shared with separate recorded environments. Final_DPO is a distinct prototype, not automatically preferred by filename. Both GRPO and ORPO notebooks contain two materially separate environments/workflows. Historical saved outputs, current upstream implementation checks, canonical paper definitions and recommendations are explicitly separated.','\n## Extraction limits','All pages received image review and auxiliary OCR; tiny inset text and isolated handwritten fragments cannot always be transcribed exactly. Blank pages are explicitly listed. Raw extracted math is not accepted uncritically. All cell types, comments and saved text/HTML/PNG outputs were inspected, but notebooks were not retrained and outputs may be stale. This knowledge base documents runnable intent, not a claim of reproduced GPU training. See [corrections](CORRECTIONS_AND_LIMITATIONS.md) and [external verification](EXTERNAL_REFERENCES.md).']
write('SOURCE_INVENTORY.md','\n'.join(inv))
# Embed reusable Mermaid sources in a portable visual index.
diag=['# Diagram and plot library','Original educational diagrams. Mermaid sources can be reused in supported Markdown renderers; no external image attribution is needed. Analytical plots show illustrative objective behavior, not measured training results.']
for p in sorted((OUT/'diagrams').glob('*.mmd')):
 diag += ['\n## '+p.stem.replace('_',' '),f'[Reusable source]({p.name})','```mermaid\n'+p.read_text().strip()+'\n```']
diag+=['\n## Reproducible analytical plots','![PPO clipping](../assets/plots/ppo_clipping.svg)','For fixed advantages +1 and −1, clipping width0.2; current/old ratios vary independently. These curves are surrogate incentives, not hard constraints.','![Logistic preference loss](../assets/plots/preference_loss.svg)','−logσ(βm) against illustrative reference-adjusted log-probability margin m, for β0.1/0.5/1. No training data used. [Generator](../assets/plot_objectives.py).']
write('diagrams/README.md','\n\n'.join(diag))
print('Supplement inventories created: 137 PDF page entries and',sum(len(json.loads((SRC/n).read_text())['cells']) for n in nbmeta),'notebook cell entries.')
