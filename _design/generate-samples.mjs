import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
await fs.mkdir(path.join(root,'_local'),{recursive:true});
const out=path.join(root,'shared/sample-files');
await fs.mkdir(out,{recursive:true});
const teams=['Planning','Procurement','Site Coordination'];
const owners=['Aina Rahman','Bala Kumar','Siti Aminah'];
const tasks=['Confirm reporting fields','Draft status definitions','Review pilot brief','Prepare register template','Check dropdown choices','Collect sample update','Review sample chart','Prepare team guidance','Check hub navigation','Rehearse sponsor update','Review final submissions','Record pilot lessons'];
const planned=[600,800,500,900,1200,700,1500,600,1000,800,1100,700];
const actual=[550,700,0,850,1050,0,1400,500,0,750,1000,0];
const statuses=['Complete','In Progress','Not Started'];
const taskRows=tasks.map((t,i)=>[`T${String(i+1).padStart(3,'0')}`,teams[Math.floor(i/4)],t,owners[i%3],Math.floor(i/3)+1,statuses[i%3],planned[i],actual[i]]);
const rateRows=[['IT01','Display adapter',45,'Equipment'],['IT02','Training notebook',12,'Stationery'],['IT03','Cable pack',30,'Equipment'],['IT04','Marker set',18,'Stationery'],['IT05','Desk sign',25,'Print'],['IT06','Quick guide',8,'Print']];
const orderRows=Array.from({length:24},(_,i)=>{const r=rateRows[i%6];return [`PO${String(i+1).padStart(3,'0')}`,['PJ-A','PJ-B','PJ-C'][Math.floor(i/8)],teams[i%3],r[0],(i%5+1)*2,r[2],['Delivered','Pending','Cancelled','Delivered'][i%4],Math.floor(i/6)+1,`${r[1]} for ${['briefing','pilot team','review session'][i%3]}`]});
const datasets=[{name:'TaskRegister',sheets:[['Tasks',[['TaskID','Team','Task','Owner','DueWeek','Status','PlannedCost','ActualCost'],...taskRows]],['Summary',[['Status','TaskCount'],['Complete',null],['In Progress',null],['Not Started',null]]]]},{name:'ProcurementRegister',sheets:[['Orders',[['OrderID','Project','Team','ItemCode','Quantity','UnitCost','Status','Week','Description'],...orderRows]],['Rates',[['ItemCode','Item','UnitCost','Category'],...rateRows]]]}];
for(const d of datasets){
 const wb=Workbook.create();
 for(const [name,values] of d.sheets){
  const s=wb.worksheets.add(name); const end=String.fromCharCode(64+values[0].length);const last=values.length;
  s.getRange(`A1:${end}${last}`).values=values;
  s.getRange(`A1:${end}${last}`).format.font={name:'Arial',size:11,color:'#172b4d'};
  s.getRange(`A1:${end}1`).format={fill:'#174ea6',font:{name:'Arial',size:11,bold:true,color:'#ffffff'},rowHeight:30};
  s.getRange(`A1:${end}${last}`).format.columnWidth=17;
  s.getRange(`A2:${end}${last}`).format.rowHeight=25;
  s.getRange(`A1:${end}1`).format.wrapText=true;
  s.getRange(`A1:${end}${last}`).format.verticalAlignment='center';
  s.showGridLines=false;s.freezePanes.freezeRows(1);
  if(name==='Tasks'){s.getRange('C1:C13').format.columnWidth=32;s.getRange('D1:D13').format.columnWidth=20;s.getRange('F1:F13').format.columnWidth=18;s.getRange('G2:H13').setNumberFormat('"RM "#,##0');}
  if(name==='Orders'){s.getRange('I1:I25').format.columnWidth=40;s.getRange('F2:F25').setNumberFormat('"RM "#,##0.00');}
  if(name==='Rates'){s.getRange('B1:B7').format.columnWidth=27;s.getRange('C2:C7').setNumberFormat('"RM "#,##0.00');}
  if(name==='Summary'){s.getRange('A1:A4').format.columnWidth=20;}
  s.getRange(`${String.fromCharCode(66+values[0].length)}1`).values=[['Fictional training data']];
 }
 wb.recalculate();
 console.log(d.name,(await wb.inspect({kind:'table',range:d.sheets[0][0]+'!A1:I4',tableMaxRows:4,tableMaxCols:9,maxChars:1700})).ndjson);
 const file=await SpreadsheetFile.exportXlsx(wb);await file.save(path.join(out,d.name+'.xlsx'));
 for(const [name,values] of d.sheets){const preview=await wb.render({sheetName:name,range:`A1:${String.fromCharCode(64+values[0].length)}${Math.min(values.length,8)}`,scale:1,format:'png'});await fs.writeFile(path.join(root,`_local/${d.name}-${name}.png`),new Uint8Array(await preview.arrayBuffer()));}
}
const csv=rows=>rows.map(row=>row.map(v=>'"'+String(v??'').replaceAll('"','""')+'"').join(',')).join('\n')+'\n';
await fs.writeFile(path.join(out,'Tasks.csv'),csv(datasets[0].sheets[0][1]));
await fs.writeFile(path.join(out,'Orders.csv'),csv(datasets[1].sheets[0][1]));
await fs.writeFile(path.join(out,'Rates.csv'),csv(datasets[1].sheets[1][1]));
await fs.writeFile(path.join(out,'DirtyText.csv'),csv([['TaskID','Team','Status'],['T001',' Planning ','complete'],['T002','Procurement','In Progress'],['T003','Site Coordination ','Not Started']]));
const keys={taskCount:12,plannedTotal:planned.reduce((a,b)=>a+b,0),actualTotal:actual.reduce((a,b)=>a+b,0),statusCounts:Object.fromEntries(statuses.map(s=>[s,taskRows.filter(r=>r[5]===s).length])),teamTotals:Object.fromEntries(teams.map(t=>[t,{planned:taskRows.filter(r=>r[1]===t).reduce((s,r)=>s+r[6],0),actual:taskRows.filter(r=>r[1]===t).reduce((s,r)=>s+r[7],0)}])),orderCount:24,orderTotal:orderRows.reduce((s,r)=>s+r[4]*r[5],0),deliveredTotal:orderRows.filter(r=>r[6]==='Delivered').reduce((s,r)=>s+r[4]*r[5],0)};
await fs.mkdir(path.join(root,'_trainer'),{recursive:true});await fs.writeFile(path.join(root,'_trainer/answer-controls.json'),JSON.stringify(keys,null,2));
await fs.writeFile(path.join(root,'_local/sample-controls.json'),JSON.stringify(keys,null,2));
console.log('Independent controls:',keys);
