const { chromium } = require('/home/claude/wt/node_modules/playwright');const fs=require('fs');
(async()=>{const W=JSON.parse(fs.readFileSync('welt.json'));const ids=[...new Set(W.L.map(x=>x.a2).filter(Boolean).map(a=>a.toLowerCase()))];
const b=await chromium.launch({executablePath:'/usr/bin/google-chrome'});const p=await b.newPage({viewport:{width:72,height:54},deviceScaleFactor:1});const out={};
for(const id of ids){const f=`node_modules/flag-icons/flags/4x3/${id}.svg`;if(!fs.existsSync(f))continue;await p.setContent(`<body style="margin:0"><img src="data:image/svg+xml;base64,${fs.readFileSync(f).toString('base64')}" style="width:72px;height:54px;display:block">`);await p.waitForTimeout(20);out[id.toUpperCase()]='data:image/png;base64,'+(await p.screenshot({type:'png'})).toString('base64')}
fs.writeFileSync('flaggen.json',JSON.stringify(out));console.log(Object.keys(out).length,(JSON.stringify(out).length/1024|0)+'KB');await b.close()})();
