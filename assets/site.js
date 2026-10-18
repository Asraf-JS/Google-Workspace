document.addEventListener('DOMContentLoaded',()=>{
 const toggle=document.querySelector('.menu-toggle'),sidebar=document.querySelector('.sidebar');
 toggle?.addEventListener('click',()=>{const open=sidebar.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));});
 document.querySelectorAll('.sidebar-nav a').forEach(a=>{if(location.pathname.startsWith(new URL(a.href).pathname))a.setAttribute('aria-current','page');});
 document.querySelectorAll('pre').forEach(pre=>{const button=document.createElement('button');button.className='copy-button';button.textContent='Copy';button.type='button';button.setAttribute('aria-label','Copy this value or prompt');const code=pre.querySelector('code');button.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(code?.textContent||'');button.textContent='Copied';}catch{button.textContent='Select text to copy';} });pre.prepend(button);});
});
