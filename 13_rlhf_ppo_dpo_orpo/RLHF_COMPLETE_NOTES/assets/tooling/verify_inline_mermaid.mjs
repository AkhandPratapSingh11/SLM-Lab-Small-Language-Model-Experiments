import {JSDOM} from 'jsdom';import fs from 'node:fs';import path from 'node:path';
const dom=new JSDOM('<html><body></body></html>');globalThis.window=dom.window;globalThis.document=dom.window.document;
const {default:mermaid}=await import('mermaid');mermaid.initialize({startOnLoad:false});
const root=path.resolve(import.meta.dirname,'../..');let results=[];
for(const name of [...fs.readdirSync(root).filter(n=>n.endsWith('.md')),'diagrams/README.md']){
 const s=fs.readFileSync(path.join(root,name),'utf8');let i=0;
 for(const match of s.matchAll(/```mermaid\n([\s\S]*?)```/g)){
  i++;try{await mermaid.parse(match[1]);results.push({file:name,block:i,valid:true});}catch(e){results.push({file:name,block:i,valid:false,error:String(e)});}
 }
}
fs.writeFileSync(path.join(root,'assets/inline_mermaid_validation.json'),JSON.stringify(results,null,2));console.log('Inline Mermaid blocks:',results.length,'invalid:',results.filter(r=>!r.valid).length);
if(results.some(r=>!r.valid))process.exitCode=1;
