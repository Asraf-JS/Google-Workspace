import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const config=JSON.parse(await fs.readFile(path.join(root,'site.config.json'),'utf8'));
const base=(process.env.SITE_BASE_PATH||config.basePath||'').replace(/\/$/,'');
const out=path.join(root,'_site');
const errors=[];let pages=0,links=0;
async function walk(dir){for(const e of await fs.readdir(dir,{withFileTypes:true})){
 if(e.name==='_qa')continue;
 const p=path.join(dir,e.name);
 if(e.isDirectory()){await walk(p);continue;}
 if(!e.name.endsWith('.html'))continue;
 pages++;const html=await fs.readFile(p,'utf8');const pageUrl=new URL((base||'')+'/'+path.relative(out,p).split(path.sep).join('/'),'http://course.test');
 for(const m of html.matchAll(/<(?:a|img|script|link)\b[^>]*?\b(?:href|src)=["']([^"']+)["']/gi)){
  const href=m[1].replaceAll('&amp;','&');if(/^(?:https?:|mailto:|data:|#)/i.test(href))continue;
  let url;try{url=new URL(href,pageUrl);}catch{errors.push(path.relative(out,p)+': invalid '+href);continue;}
  if(url.origin!=='http://course.test')continue;
  let rel=decodeURIComponent(url.pathname);if(base){if(!rel.startsWith(base+'/')){errors.push(path.relative(out,p)+': outside base '+href);continue;}rel=rel.slice(base.length);}
  let target=path.resolve(out,'.'+rel);if(target!==out&&!target.startsWith(out+path.sep)){errors.push('Outside site: '+href);continue;}
  try{const st=await fs.stat(target);if(st.isDirectory())target=path.join(target,'index.html');await fs.access(target);}catch{errors.push(path.relative(out,p)+': missing '+href);}
  links++;
 }
}}
await walk(out);
if(errors.length)throw new Error('Built-site links failed:\n'+[...new Set(errors)].join('\n'));
console.log(`Built-site links pass: ${pages} pages, ${links} local references.`);
