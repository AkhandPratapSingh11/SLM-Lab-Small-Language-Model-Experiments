import {JSDOM} from 'jsdom';
import fs from 'node:fs';
import path from 'node:path';
const dom=new JSDOM('<!DOCTYPE html><html><body></body></html>');
globalThis.window=dom.window;globalThis.document=dom.window.document;
const {default:mermaid}=await import('mermaid');
mermaid.initialize({startOnLoad:false,securityLevel:'strict'});
const dir=path.resolve(import.meta.dirname,'../../diagrams');
const results=[];
for(const name of fs.readdirSync(dir).filter(n=>n.endsWith('.mmd'))){
 try{await mermaid.parse(fs.readFileSync(path.join(dir,name),'utf8'));results.push({name,valid:true});}
 catch(e){results.push({name,valid:false,error:String(e)});}
}
fs.writeFileSync(path.resolve(import.meta.dirname,'../mermaid_validation.json'),JSON.stringify({parser:'mermaid 11.15.0',results},null,2));
console.log(JSON.stringify(results,null,2));
if(results.some(r=>!r.valid))process.exitCode=1;
