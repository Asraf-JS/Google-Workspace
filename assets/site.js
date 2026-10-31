document.addEventListener('DOMContentLoaded',()=>{
 const toggle=document.querySelector('.menu-toggle'),sidebar=document.querySelector('.sidebar');
 toggle?.addEventListener('click',()=>{const open=sidebar.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));});
 document.querySelectorAll('.sidebar-nav a').forEach(a=>{if(location.pathname.startsWith(new URL(a.href).pathname))a.setAttribute('aria-current','page');});
 document.querySelectorAll('pre').forEach(pre=>{const button=document.createElement('button');button.className='copy-button';button.textContent='Copy';button.type='button';button.setAttribute('aria-label','Copy this value or prompt');const code=pre.querySelector('code');button.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(code?.textContent||'');button.textContent='Copied';}catch{button.textContent='Select text to copy';} });pre.prepend(button);});
 document.querySelectorAll('.main-inner table').forEach(table=>{
  if(table.previousElementSibling?.matches('[data-no-copy]'))return;
  const heading=table.previousElementSibling?.matches('[data-copy-with-table]')?table.previousElementSibling:null;
  const tools=document.createElement('div');tools.className='table-copy-tools';
  const button=document.createElement('button');button.type='button';button.className='copy-table-button';button.textContent=heading?'Copy heading and table':'Copy table';
  const headings=Array.from(table.rows[0]?.cells||[],cell=>cell.textContent.trim()).join(', ');
  button.setAttribute('aria-label',(heading?'Copy heading and table: ':'Copy table: ')+headings);
  const status=document.createElement('span');status.className='table-copy-status';status.setAttribute('role','status');
  tools.append(button,status);table.before(tools);
  button.addEventListener('click',async()=>{
   const escape=value=>value.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
   const rows=Array.from(table.rows,row=>Array.from(row.cells,cell=>cell.innerText.trim()));
   const labels=heading?heading.innerText.trim().split('\n').filter(Boolean):[];
   const text=[...labels,rows.map(row=>row.join('\t')).join('\n')].join('\n');
   const prefix=labels.map(label=>'<p style="font-family:Arial,sans-serif;font-size:11pt;color:#111;">'+escape(label)+'</p>').join('');
   const html='<html><body>'+prefix+'<table style="border-collapse:collapse;width:100%;font-family:Arial,sans-serif;font-size:11pt;color:#111;background:#fff;">'+rows.map((row,i)=>'<tr>'+row.map(value=>'<'+(i?'td':'th')+' style="border:1px solid #555;padding:6pt;text-align:left;vertical-align:top;background:#fff;color:#111;font-weight:'+(i?'normal':'bold')+';"><p style="margin:0;">'+(escape(value).replaceAll('\n','<br>')||'&nbsp;')+'</p></'+(i?'td':'th')+'>').join('')+'</tr>').join('')+'</table></body></html>';
   try{
    await navigator.clipboard.write([new ClipboardItem({'text/html':new Blob([html],{type:'text/html'}),'text/plain':new Blob([text],{type:'text/plain'})})]);
    button.textContent=heading?'Heading and table copied':'Table copied';status.textContent='In Google Docs, click a blank line outside any table and press Ctrl+V. Use normal paste to keep the cells.';
   }catch{
    const selection=table.ownerDocument.getSelection(),range=table.ownerDocument.createRange();if(heading){range.setStartBefore(heading);range.setEndAfter(table);}else range.selectNode(table);selection.removeAllRanges();selection.addRange(range);
    button.textContent='Table selected';status.textContent='Press Ctrl+C, then paste on a blank line in Google Docs with Ctrl+V. Do not use paste without formatting.';
   }
  });
 });

});
