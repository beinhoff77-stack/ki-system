// Motiv-Übersicht: alle Motive auf einem Blatt (4×5), 2x
const path=require('path'); const { chromium } = require('/home/claude/ki-system/node_modules/playwright');
(async()=>{ const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1243/chrome-linux64/chrome'});
 const [datei, ziel, dsf, nur] = process.argv.slice(2); // node motive-blatt.cjs $PWD/index.html bilder/motive-uebersicht.png 1
 const p=await b.newPage({viewport:{width:1000,height:800},deviceScaleFactor:Number(dsf||1)});
 await p.goto('file://'+datei+'#s=motive&foto=1');
 await p.evaluate((nur)=>{ const ids = nur ? nur.split(',') : MOTIVE.map(m=>m.id); document.body.innerHTML = `<div style="display:grid;grid-template-columns:repeat(5,180px);gap:14px;padding:18px;background:#F3F1EA;font:600 12px system-ui">${ids.map(id=>{const m=MOTIVE.find(x=>x.id===id); return `<div><div style="width:180px;height:180px;border-radius:16px;overflow:hidden">${m.svg('q'+id)}</div><div style="margin-top:4px">${m.name}</div></div>`}).join('')}</div>`; document.querySelectorAll('svg').forEach(s=>{s.style.width='100%';s.style.height='100%';s.style.display='block'}); }, nur||'');
 await p.waitForTimeout(200); await p.screenshot({path:ziel, fullPage:true}); await b.close(); })();
