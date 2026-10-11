import fs from 'node:fs';import path from 'node:path';
import {unified} from 'unified';import remarkParse from 'remark-parse';import remarkMath from 'remark-math';import remarkGfm from 'remark-gfm';import remarkRehype from 'remark-rehype';import rehypeKatex from 'rehype-katex';import rehypeStringify from 'rehype-stringify';import katex from 'katex';
const root=path.resolve(import.meta.dirname,'../../..');const out=path.join(root,'RLHF_COMPLETE_NOTES');
const files=[];function scan(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())scan(p);else if(e.name.endsWith('.md'))files.push(p);}}scan(root);
const parser=unified().use(remarkParse).use(remarkGfm).use(remarkMath);
let errors=[],math=[],literalCount=0;const ignored=[];
function visit(node,file){
 if(node.type==='math'||node.type==='inlineMath'){
  try{katex.renderToString(node.value,{displayMode:node.type==='math',throwOnError:true,strict:'error',output:'htmlAndMathml'});math.push({file:path.relative(root,file),line:node.position.start.line,type:node.type,formula:node.value});}
  catch(e){errors.push({file:path.relative(root,file),line:node.position.start.line,error:String(e)});}
 }
 if(node.type==='code'||node.type==='inlineCode'){literalCount++;return;}
 if(node.type==='text' && /\\(?:\[|\]|\(|\))/.test(node.value))ignored.push({file:path.relative(root,file),line:node.position?.start.line,text:node.value.slice(0,200)});
 for(const c of node.children||[])visit(c,file);
}
for(const file of files){const source=fs.readFileSync(file,'utf8');visit(parser.parse(source),file);
 // Delimiter paragraphs must be paired and separated, outside code.
 const lines=source.split('\n');let fence=null;let open=null;
 for(let i=0;i<lines.length;i++){
  const f=lines[i].match(/^\s*(`{3,}|~{3,})/);
  if(fence){if(f&&f[1][0]===fence[0]&&f[1].length>=fence.length)fence=null;continue;}
  if(f){fence=f[1];continue;}
  if(lines[i].trim()==='$$'){
   if(open===null){open=i;if(i&&lines[i-1].trim())errors.push({file:path.relative(root,file),line:i+1,error:'Missing blank line before display'});}
   else{if(i+1<lines.length&&lines[i+1].trim())errors.push({file:path.relative(root,file),line:i+1,error:'Missing blank line after display'});open=null;}
  }
 }
 if(open!==null)errors.push({file:path.relative(root,file),line:open+1,error:'Unpaired display delimiter'});
}
// Produce standalone actual KaTeX HTML output for every formula-bearing learning chapter.
const previewDir=path.join(out,'assets/math_preview');fs.mkdirSync(previewDir,{recursive:true});
const renderer=unified().use(remarkParse).use(remarkGfm).use(remarkMath).use(remarkRehype).use(rehypeKatex,{throwOnError:true,strict:'error'}).use(rehypeStringify);
const chapters=[...new Set(math.map(m=>m.file))].filter(f=>!f.includes('node_modules/'));
for(const name of chapters){const p=path.join(root,name);const result=String(await renderer.process(fs.readFileSync(p,'utf8')));
 if(result.includes('katex-error'))errors.push({file:name,error:'Error node in HTML'});
 fs.writeFileSync(path.join(previewDir,path.basename(p,'.md')+'.html'),`<!doctype html><html><head><meta charset="utf-8"><title>${path.basename(p)}</title><link rel="stylesheet" href="../tooling/node_modules/katex/dist/katex.min.css"><style>body{max-width:1000px;margin:40px auto;padding:20px;font:16px/1.6 system-ui}.katex-display{overflow:auto}table{border-collapse:collapse}td,th{border:1px solid #ddd;padding:6px}pre{overflow:auto;background:#eee;padding:12px}</style></head><body>${result}</body></html>`);
}
const report={renderer:'remark-parse + remark-gfm + remark-math, rehype-katex',katex_version:JSON.parse(fs.readFileSync(path.join(import.meta.dirname,'node_modules/katex/package.json'))).version,markdown_files_inspected:files.length,display_equations:math.filter(m=>m.type==='math').length,inline_equations:math.filter(m=>m.type==='inlineMath').length,literal_code_nodes_preserved:literalCount,previews:chapters.length,errors,math,remaining_literal_backslashes:ignored};
fs.writeFileSync(path.join(out,'assets/math_validation.json'),JSON.stringify(report,null,2));console.log(JSON.stringify({...report,math:undefined,remaining_literal_backslashes:undefined},null,2));if(errors.length)process.exitCode=1;
