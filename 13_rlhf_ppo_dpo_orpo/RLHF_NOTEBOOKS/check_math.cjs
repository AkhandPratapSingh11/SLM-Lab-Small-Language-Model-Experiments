const fs=require('node:fs');const path=require('node:path');
// Reuse the existing notes' verified KaTeX package without modifying that directory.
const katex=require(path.resolve(__dirname,'../RLHF_COMPLETE_NOTES/assets/tooling/node_modules/katex'));
const formulas=JSON.parse(fs.readFileSync(path.join(__dirname,'math_formulas.json')));const errors=[];
for(const m of formulas){try{katex.renderToString(m.formula,{displayMode:m.display,strict:'error',throwOnError:true});}catch(e){errors.push({...m,error:String(e)});}}
fs.writeFileSync(path.join(__dirname,'math_validation.json'),JSON.stringify({expressions:formulas.length,errors},null,2));console.log('Math rendered:',formulas.length,'errors:',errors.length);if(errors.length)console.log(errors);process.exitCode=errors.length?1:0;
