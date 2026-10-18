import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const require=createRequire(import.meta.url);
const {Marked}=await import(pathToFileURL(require.resolve('marked',{paths:[process.env.TRAINING_NODE_MODULES||root]})));
const courses=JSON.parse(await fs.readFile(path.join(root,'planning/course-map.json'),'utf8'));
const config=JSON.parse(await fs.readFile(path.join(root,'site.config.json'),'utf8'));
const base=(process.env.SITE_BASE_PATH||config.basePath||'').replace(/\/$/,'');
const out=path.join(root,'_site');await fs.mkdir(out,{recursive:true});
const template=await fs.readFile(path.join(root,'_layouts/default.html'),'utf8');
const escape=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const url=rel=>base+'/'+rel.split(path.sep).join('/');
const route=rel=>rel.endsWith('README.md')?rel.slice(0,-9)+'index.html':rel.replace(/\.md$/,'.html');
let count=0;
async function walk(dir){for(const entry of await fs.readdir(dir,{withFileTypes:true})){
 if(entry.name.startsWith('.')||entry.name==='CLAUDE.md'||['_site','_local','_trainer','node_modules','_layouts','_design','tools','book','assets'].includes(entry.name))continue;
 const p=path.join(dir,entry.name);const rel=path.relative(root,p);
 if(entry.isDirectory()){await walk(p);continue;}
 if(entry.name.endsWith('.md')){
  const c=courses.find(c=>rel.startsWith(c.path+path.sep));
  const source=await fs.readFile(p,'utf8');const title=(source.match(/^# (.+)$/m)||[])[1]||config.title;
  const marked=new Marked({gfm:true});
  marked.use({walkTokens(token){if((token.type==='link'||token.type==='image')&&token.href&&!/^(https?:|mailto:|#)/i.test(token.href)){
   const [file,anchor]=token.href.split('#');const target=path.resolve(path.dirname(p),decodeURIComponent(file));
   const r=path.relative(root,target);if(!r.startsWith('..'))token.href=url(route(r))+(anchor?'#'+anchor:'');
  }}});
  const html=marked.parse(source);
  const nav=c?c.chapters.map(ch=>`<a class="nav-item" href="${url(c.path+'/'+ch.slug+'/')}"><span class="nav-number">${String(ch.number).padStart(2,'0')}</span><span class="nav-name">${escape(ch.title)}</span></a>`).join(''):'<p class="nav-hint">Choose a course to see its chapters.</p>';
  const links=courses.map(co=>`<a class="course-link ${c===co?'active':''}" href="${url(co.path+'/')}">${escape(co.title)}</a>`).join('');
  const rendered=template.replaceAll('{{base}}',base).replace('{{title}}',escape(title)).replace('{{courseTitle}}',escape(c?.title||'Programme overview')).replace('{{courseLinks}}',links).replace('{{chapterNav}}',nav).replace('{{content}}',html);
  const dest=path.join(out,route(rel));await fs.mkdir(path.dirname(dest),{recursive:true});await fs.writeFile(dest,rendered);count++;
 }else if(/\.(xlsx|csv|txt|png|jpg|jpeg|svg|webp|pdf|zip)$/i.test(entry.name)){
  const dest=path.join(out,rel);await fs.mkdir(path.dirname(dest),{recursive:true});await fs.copyFile(p,dest);
 }
}}
await walk(root);
await fs.cp(path.join(root,'assets'),path.join(out,'assets'),{recursive:true});
await fs.writeFile(path.join(out,'.nojekyll'),'');
console.log(`Built ${count} pages in ${out}. Base path: ${base||'/'}`);
