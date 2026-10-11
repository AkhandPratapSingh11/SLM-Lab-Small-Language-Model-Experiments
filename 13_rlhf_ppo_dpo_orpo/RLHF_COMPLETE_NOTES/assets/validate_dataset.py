"""Read-only validation of the actual local JSONL schema. No training dependencies."""
from pathlib import Path
import argparse,json,collections
DEFAULT=Path(__file__).resolve().parents[2]/'reward_preferences_dataset.jsonl'
def validate(path):
 rows=[];errors=[];seen=set();prompts=set();dups=0;dp=0
 for n,line in enumerate(Path(path).read_text(encoding='utf-8').splitlines(),1):
  try:row=json.loads(line)
  except json.JSONDecodeError as e:errors.append(f'Line {n}: {e}');continue
  if not isinstance(row,dict) or set(row)!={'prompt','chosen','rejected'}:
   errors.append(f'Line {n}: expected exactly prompt/chosen/rejected');continue
  if any(not isinstance(row[k],str) or not row[k].strip() for k in row):
   errors.append(f'Line {n}: non-string or empty field');continue
  if row['chosen'].strip()==row['rejected'].strip():errors.append(f'Line {n}: identical pair')
  key=tuple(row[k] for k in ('prompt','chosen','rejected'));dups+=key in seen;seen.add(key)
  prompt=row['prompt'].strip().lower();dp+=prompt in prompts;prompts.add(prompt);rows.append(row)
 return {'valid_records':len(rows),'errors':errors,'duplicate_records':dups,'duplicate_prompts':dp,
         'chosen_longer_in_characters':sum(len(r['chosen'])>len(r['rejected']) for r in rows),'verified_fields':['prompt','chosen','rejected']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('path',nargs='?',type=Path,default=DEFAULT);args=p.parse_args()
 report=validate(args.path);print(json.dumps(report,indent=2));raise SystemExit(bool(report['errors']))
