import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
import {spawnSync} from 'node:child_process';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const require=createRequire(import.meta.url);
const kit=process.env.TRAINING_BOOK_KIT_DIR?path.resolve(process.env.TRAINING_BOOK_KIT_DIR):path.dirname(require.resolve('training-book-kit/package.json'));
const kitRequire=createRequire(path.join(kit,'package.json'));
let source=await fs.readFile(path.join(kit,'bin/build-book.mjs'),'utf8');
function replaceOnce(from,to){if(!source.includes(from))throw new Error('Shared book kit changed; review the adapter before building: '+from.slice(0,90));source=source.replace(from,to);}
replaceOnce('const kitDir = resolve(dirname(fileURLToPath(import.meta.url)), "..");','const kitDir = '+JSON.stringify(kit)+';');
replaceOnce('from "marked"','from '+JSON.stringify(pathToFileURL(kitRequire.resolve('marked')).href));
replaceOnce('import { chromium } from "playwright";', 'import playwrightPackage from '+JSON.stringify(pathToFileURL(kitRequire.resolve('playwright')).href)+';\nconst {chromium} = playwrightPackage;');
replaceOnce('const repoFileUrl = (abs) => `${cfg.repoUrl}/blob/main/${relative(repoRoot, abs).split("\\\\").join("/")}`;',
 'const repoFileUrl = (abs) => cfg.repoUrl ? `${cfg.repoUrl}/blob/main/${relative(repoRoot, abs).split("\\\\").join("/")}` : relative(dirname(resolve(here,cfg.output)),abs).split("\\\\").map(encodeURIComponent).join("/");');
replaceOnce('Microsoft updates its apps often, so labels and layouts in your tenant may differ slightly.','Google updates its apps often, so labels, availability and layouts in your account may differ. This review draft still requires full lab validation.');
replaceOnce('Online resources: ${esc(cfg.repoUrl.replace(/^https?:\\/\\//, ""))}','Resources: ${esc(cfg.repoUrl ? cfg.repoUrl.replace(/^https?:\\/\\//, "") : "Use the practice files supplied with this review package.")}');
replaceOnce('const launch = {};','const launch = { executablePath: process.env.TRAINING_CHROMIUM_PATH || undefined };');
replaceOnce('chromium.launch(launch).catch(() => chromium.launch())','chromium.launch(launch)');
replaceOnce('...c.notes.sections.map((s) =>','...c.notes.sections.filter(s => /^\\d+\\./.test(s.text)).map((s) =>');
replaceOnce('let src = readFileSync(abs, "utf8");','let src = readFileSync(abs, "utf8");\n  src = src.replace(/^Replace bracketed source placeholders before submitting\\. Keep a human check between an AI proposal and the final output\\.\\s*$/gm, "");');
source=source.replaceAll('Hands-on exercises','Prompts and values');
const build=path.join(root,'.local-build');await fs.mkdir(build,{recursive:true});const engine=path.join(build,'workspace-book-engine.mjs');await fs.writeFile(engine,source);
await fs.mkdir(path.join(root,'books'),{recursive:true});
const courses=JSON.parse(await fs.readFile(path.join(root,'planning/course-map.json'),'utf8'));
const selected=process.argv[2]?courses.filter(c=>c.path===process.argv[2]):courses;
if(!selected.length)throw new Error('Unknown course: '+process.argv[2]);
for(const c of selected){
 const result=spawnSync(process.execPath,[engine,path.join(root,'book',c.path,'book.config.json')],{stdio:'inherit',cwd:root,env:process.env});
 if(result.status!==0)process.exit(result.status||1);
}
