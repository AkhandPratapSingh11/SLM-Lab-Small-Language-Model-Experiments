from pathlib import Path
import os,json,ast,time,sys
ROOT=Path(__file__).resolve().parent
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ['JUPYTER_PATH']=str(ROOT/'.jupyter/share/jupyter')
os.environ['JUPYTER_RUNTIME_DIR']=str(ROOT/'.jupyter/runtime')
os.environ['IPYTHONDIR']=str(ROOT/'.ipython')
os.environ['MPLCONFIGDIR']=str(ROOT/'runtime/matplotlib')
os.environ['HF_HOME']=str(ROOT/'runtime/huggingface')
os.environ['HF_HUB_OFFLINE']='1'
os.environ['HF_DATASETS_OFFLINE']='1'
import nbformat
from nbclient import NotebookClient
kernel=ROOT/'.jupyter/share/jupyter/kernels/rlhf-local';kernel.mkdir(parents=True,exist_ok=True)
(kernel/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-B','-m','ipykernel_launcher','-f','{connection_file}'],'display_name':'RLHF local validation','language':'python'}))
report=json.loads((ROOT/'validation_report.json').read_text()) if len(sys.argv)>1 and (ROOT/'validation_report.json').exists() else []
for path in sorted(ROOT.glob('*.ipynb')):
 if len(sys.argv)>1 and not any(path.name.startswith(prefix) for prefix in sys.argv[1:]):continue
 report=[r for r in report if r['notebook']!=path.name]
 nb=nbformat.read(path,as_version=4);nbformat.validate(nb)
 for i,c in enumerate(nb.cells,1):
  if c.cell_type=='code':ast.parse(c.source,filename=path.name+':cell'+str(i))
 start=time.monotonic();status={'notebook':path.name,'json_schema':'passed','python_syntax':'passed'}
 try:
  NotebookClient(nb,timeout=180,kernel_name='rlhf-local',resources={'metadata':{'path':str(ROOT)}}).execute()
  status.update(execution='passed',seconds=round(time.monotonic()-start,2),code_cells=sum(c.cell_type=='code' for c in nb.cells),outputs=sum(len(c.get('outputs',[])) for c in nb.cells))
 except Exception as e:status.update(execution='failed',error=str(e),seconds=round(time.monotonic()-start,2))
 nbformat.write(nb,path);report.append(status)
 (ROOT/'validation_report.json').write_text(json.dumps(report,indent=2))
 print(path.name,status['execution'],status['seconds'],flush=True)
 if status['execution']=='failed':print(status['error'][-3000:],flush=True)
print('Validation complete:',sum(r['execution']=='passed' for r in report),'/',len(report))
raise SystemExit(any(r['execution']=='failed' for r in report))
