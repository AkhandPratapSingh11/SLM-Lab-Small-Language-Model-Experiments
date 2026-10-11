"""Verify authored Markdown, source hashes, ledgers, and helper syntax.
Raw notebook extracts preserve original links/HTML and are excluded from authored-link checks.
Mermaid parsing is a separate Node verification, recorded in QA_REPORT.md.
"""
from pathlib import Path
import ast,hashlib,json,re,urllib.parse
OUT=Path(__file__).resolve().parents[1];SRC=OUT.parent

def run():
 errors=[];links=0;authored=list(OUT.glob('*.md'))+[OUT/'diagrams/README.md',OUT/'assets/source_audit/PDF_PAGE_LEDGER.md',OUT/'assets/source_audit/NOTEBOOK_AUDIT.md']
 for p in authored:
  if not p.exists():errors.append(f'Missing authored document {p}');continue
  text=p.read_text();fences=re.findall(r'^\s*```',text,re.M)
  if len(fences)%2:errors.append(f'Unbalanced fences: {p.name}')
  if text.count('\\[')!=text.count('\\]'):errors.append(f'Unbalanced legacy display math: {p.name}')
  display_lines=re.findall(r'^\$\$$',text,re.M)
  if len(display_lines)%2:errors.append(f'Unpaired Markdown display math: {p.name}')
  # Strip fenced code before checking Markdown links; snippets may contain regexes/code.
  stripped=re.sub(r'```.*?```','',text,flags=re.S)
  for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',stripped):
   target=target.strip().strip('<>');url=urllib.parse.urlsplit(target)
   if url.scheme or target.startswith('#'):continue
   file=urllib.parse.unquote(url.path);dest=(p.parent/file).resolve();links+=1
   if not dest.exists():errors.append(f'Broken link {p.relative_to(OUT)} -> {target}')
   if url.fragment and dest.suffix=='.md' and dest.exists():
    heads=re.findall(r'^#+\s+(.+)$',dest.read_text(),re.M)
    anchors={re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in heads}
    if urllib.parse.unquote(url.fragment) not in anchors:errors.append(f'Missing anchor {target} in {p.name}')
 hashes=json.loads((OUT/'assets/source_audit/original_hashes.json').read_text());unchanged=[]
 for name,digest in hashes.items():
  if hashlib.sha256((SRC/name).read_bytes()).hexdigest()!=digest:errors.append(f'Original modified: {name}')
  else:unchanged.append(name)
 for p in (OUT/'assets').glob('*.py'):
  try:ast.parse(p.read_text(),str(p))
  except SyntaxError as e:errors.append(str(e))
 questions=len(re.findall(r'^### Q\d+\.',(OUT/'11_INTERVIEW_PREPARATION.md').read_text(),re.M))
 if questions<40:errors.append(f'Only {questions} interview questions')
 pages=sum(1 for _ in (OUT/'assets/source_audit').glob('*/page-[0-9][0-9].png'))
 ocr=sum(1 for _ in (OUT/'assets/source_audit').glob('*/page-[0-9][0-9].txt'))
 cellcount=sum(len(json.loads(p.read_text())['cells']) for p in SRC.glob('*.ipynb'))
 if pages!=137 or ocr!=137 or cellcount!=247:errors.append('Source coverage count mismatch')
 result={'authored_markdown_files':len(authored),'local_links_checked':links,'originals_unchanged':len(unchanged),'pdf_page_images':pages,'ocr_pages':ocr,'notebook_cells':cellcount,'interview_questions':questions,'mermaid_sources':len(list((OUT/'diagrams').glob('*.mmd'))),'errors':errors}
 (OUT/'assets/documentation_validation.json').write_text(json.dumps(result,indent=2))
 print(json.dumps(result,indent=2));return result
if __name__=='__main__':raise SystemExit(bool(run()['errors']))
