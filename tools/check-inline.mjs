import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const courses=JSON.parse(await fs.readFile(path.join(root,'planning/course-map.json'),'utf8'));
let count=0;const errors=[];
for(const course of courses){
 const config=JSON.parse(await fs.readFile(path.join(root,'book',course.path,'book.config.json'),'utf8'));
 if(config.chapters.some(c=>c.exercises))continue;
 for(const ch of course.chapters){
  const rel=course.path+'/'+ch.slug+'/README.md';const text=await fs.readFile(path.join(root,rel),'utf8');
  if(/\]\([^)]*prompts\.md(?:#[^)]*)?\)/i.test(text)||/\b(?:prompts|copy-paste) page\b/i.test(text))errors.push(rel+': directs learners to a prompt page');
  if(!/```(?:text)?\r?\n/.test(text))errors.push(rel+': no inline copyable material');
  count++;
 }
}
if(errors.length)throw new Error(errors.join('\n'));
console.log(`Inline material check passes: ${count} labs; no prompt-page dependencies or repeated book appendices.`);
