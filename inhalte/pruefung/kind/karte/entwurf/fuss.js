// ---- erfundener Stand Testkind (Europa = Zahlen) ----
const ZU={Austria:{s:'gesch'},Switzerland:{s:'gold'},Slovenia:{s:'gesch'},Italy:{s:'dran'},Greece:{s:'plan',p:2},Germany:{s:'plan',p:3},Belgium:{s:'plan',p:4},'United Kingdom':{s:'offen'},France:{s:'offen'},Spain:{s:'sperr',w:'Visum fehlt: erst „Brüche und Anteile“ (Deutschland)'},Netherlands:{s:'sperr',w:'ab Klasse 9'},Poland:{s:'sperr',w:'ab Klasse 9'},Norway:{s:'sperr',w:'ab Klasse 9'}};
const TITEL={Italy:'Natürliche Zahlen',Austria:'Ganze Zahlen',Switzerland:'Grundrechenarten',Slovenia:'Potenzen als Schreibweise',Greece:'Teilbarkeit',Germany:'Brüche und Anteile',Belgium:'Dezimalzahlen','United Kingdom':'Rechnen mit rationalen Zahlen',Spain:'Zehnerpotenzen',France:'Negative Exponenten',Netherlands:'Elementare Wurzeln',Poland:'Wurzeln und reelle Zahlen',Norway:'Rationale Exponenten'};
const STAEDTE={Italy:13,Austria:11,Switzerland:14,Slovenia:7,Greece:7,Germany:14,Belgium:8,'United Kingdom':12,Spain:7,France:3,Netherlands:6,Poland:7,Norway:6};
const REISE=['Austria','Switzerland','Slovenia','Italy','Greece','Germany','Belgium'];
const IST={Rom:'abgelegt',Neapel:'gelandet',Pompei:'faellig',Bari:'gelandet',Bologna:'dran',Siena:'kuer'};
const DRAN_N=3;
const KF={eu:'#8DB8E6',as:'#EBB27A',or:'#E09A9A',af:'#E6CB72',na:'#98CF95',sa:'#BBA6DC',au:'#86CFC6',po:'#F0A9C8',ant:'#EEF3F6'};
const KN={eu:['Europa','Zahlen',3,13],as:['Asien','Algebra',1,19],or:['Orient','Funktionen',0,10],af:['Afrika','Geometrie',1,14],na:['Nordamerika','Geld und Verhältnisse',2,6],sa:['Südamerika','Fläche und Raum',1,9],au:['Australien und Ozeanien','Daten und Zufall',1,12],po:['Polynesien','Entdecker-Inseln',0,4]};
let gest='tag',knopf='karte',breite='handy',ansicht='europa',sel=null,vb=null;
const BY=n=>G.eur.find(x=>x.n===n);
const ZT={gesch:'✓ geschafft – Stempel; die Städte kommen noch zum Wiederholen',gold:'★ golden – alle Städte sind abgelegt. Hier musst du nichts mehr wiederholen.',dran:'gerade dran',plan:'im Plan',offen:'offen – kannst du wählen',sperr:'noch gesperrt'};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let flagArt='pin';
const fl=(a2,w=18)=>FLAG[a2]?`<image href="${FLAG[a2]}" width="${w}" height="${w*.75}" x="${-w/2}" y="${-w*.75}" preserveAspectRatio="none" class="flagge"/>`:'';
const plakette=(a2,d=13,x=0,y=0)=>FLAG[a2]?`<g transform="translate(${x},${y})"><circle r="${d/2+1.6}" class="plring"/><image href="${FLAG[a2]}" width="${d}" height="${d}" x="${-d/2}" y="${-d/2}" preserveAspectRatio="xMidYMid slice" clip-path="url(#rund)"/><circle r="${d/2}" fill="none" stroke="#0003" stroke-width=".6"/></g>`:'';
const flHtml=(a2,h=16)=>FLAG[a2]?`<img src="${FLAG[a2]}" style="height:${h}px;width:${h*4/3}px;border-radius:2px;box-shadow:0 0 0 1px #0002;vertical-align:-3px">`:'';
function bogen(a,b,h=.18){const mx=(a[0]+b[0])/2,my=(a[1]+b[1])/2,dx=b[0]-a[0],dy=b[1]-a[1];return `M${a} Q${mx+dy*h},${my-dx*h} ${b}`}
const flieger=(f='var(--dranR)')=>`<path d="M0,-11 L3,-3 L11,1 L11,3 L3,1 L2,8 L5,10 L5,11.5 L0,10 L-5,11.5 L-5,10 L-2,8 L-3,1 L-11,3 L-11,1 L-3,-3 Z" fill="${f}" stroke="var(--bg)" stroke-width="1.2"/>`;
const ms=(x,y,inner,cls='',da='')=>`<g transform="translate(${x},${y})" class="${cls}" ${da}><g class="ms">${inner}</g></g>`;
function stempel(gold){const c=gold?'var(--goldR)':'var(--geschR)';return `<g class="stempel" transform="rotate(-12)"><circle r="13" fill="${gold?'var(--gold)':'var(--bg)'}" stroke="${c}" stroke-width="2.5"/><circle r="9.5" fill="none" stroke="${c}" stroke-width="1" stroke-dasharray="2 2"/><text text-anchor="middle" dominant-baseline="central" font-size="12" font-weight="900" fill="${c}">${gold?'★':'✓'}</text></g>`}
// Hauptstadt-Zeichen: Ring mit Punkt (wie im Atlas) – Städte der Reise dagegen: nummerierte Haltestellen
const hsZ=`<circle r="5" class="hsring"/><circle r="2" class="hspunkt"/>`;
const landLabel=(a2,name,gross)=>{const w=name.length*(gross?8:7.7);if(flagArt==='aus')return `<g class="landlabel"><text class="lname" y="4" text-anchor="middle">${esc(name)}</text></g>`;if(flagArt==='eckig')return `<g class="landlabel">${fl(a2,gross?20:16)}<text class="lname" y="${gross?13:11}" text-anchor="middle">${esc(name)}</text></g>`;
 return `<g class="landlabel">${plakette(a2,gross?14:12,-w/2-(gross?11:10),0)}<text class="lname" y="3.6" text-anchor="middle">${esc(name)}</text></g>`};

// ---- Land = Flaggen-Pin auf der Hauptstadt (Kopf = Flagge, Spitze = Hauptstadt, Schild = LAND + Hauptstadt) ----
const STF={gesch:['var(--geschR)','✓'],gold:['var(--goldR)','★'],dran:['var(--dranR)',''],plan:['var(--planR)',null],sperr:['#9AA19D','🔒'],offen:['var(--hs)','']};
function landPin(a2,name,hs,z,klein){const st=z?z.s:null;const [c,zei]=STF[st]||['#8A918D',''];const R=klein?8:11,Y=klein?-17:-23;
 let s=`<g class="pinkopf${st==='sperr'?' grau':''}">`;
 if(st==='dran')s+=`<circle class="puls" r="9"/>`;
 s+=`<g class="pinform"><path d="M0,0 L${-R*.62},${Y+R*.78} L${R*.62},${Y+R*.78} Z" fill="${c}"/><circle cy="${Y}" r="${R+2.2}" fill="${c}"/></g>`;
 s+=FLAG[a2]?`<image href="${FLAG[a2]}" width="${R*2}" height="${R*2}" x="${-R}" y="${Y-R}" preserveAspectRatio="xMidYMid slice" clip-path="url(#rund)"/>`:`<circle cy="${Y}" r="${R}" fill="var(--karte)"/>`;
 s+=`<circle cy="${Y}" r="${R}" fill="none" stroke="#0002" stroke-width=".7"/><circle r="2.2" fill="${c}" stroke="var(--bg)" stroke-width="1.2"/>`;
 if(st==='plan')s+=`<g transform="translate(${R*.85},${Y-R*.85})"><circle r="7" fill="var(--planR)" stroke="var(--bg)" stroke-width="1.5"/><text text-anchor="middle" dominant-baseline="central" font-size="9" font-weight="900" fill="#fff">${z.p}</text></g>`;
 else if(zei)s+=`<g transform="translate(${R*.85},${Y-R*.85})"><circle r="7" fill="${st==='sperr'?'var(--karte)':c}" stroke="var(--bg)" stroke-width="1.5"/><text text-anchor="middle" dominant-baseline="central" font-size="${st==='sperr'?7:8.5}" font-weight="900" fill="#fff">${zei}</text></g>`;
 if(st==='dran')s+=`<g transform="translate(${-R-14},${Y-6}) rotate(60) scale(.8)">${flieger()}</g>`;
 s+=`</g>`;
 const tx=R+6;s+=`<g class="pintext"><text class="pland${klein?' k':''}" x="${tx}" y="${Y-1}">${esc(name)}</text><text class="phs" x="${tx}" y="${Y+11}">${esc(hs||'')}</text></g>`;
 return s}
function landMarke(a2,name,hs,z){const st=z?z.s:null;const [c,zei]=STF[st]||['var(--linie)',''];const w=Math.max(62,name.length*6.6+16);
 let s=`<g transform="translate(0,-48)" class="${st==='sperr'?'grau':''}"><rect x="${-w/2}" y="-2" width="${w}" height="40" rx="3" fill="var(--karte)" stroke="${z?c:'var(--linie)'}" stroke-width="${z?2:1}" class="marke"/>`;
 s+=FLAG[a2]?`<image href="${FLAG[a2]}" x="${-w/2+4}" y="2" width="${w-8}" height="13" preserveAspectRatio="xMidYMid slice"/>`:'';
 s+=`<text class="pland k" y="26" text-anchor="middle">${esc(name)}</text><text class="phs" y="35" text-anchor="middle" style="font-size:8.5px">${esc(hs||'')}</text>`;
 if(zei||st==='plan')s+=`<g transform="translate(${w/2-2},-2)"><circle r="7" fill="${st==='sperr'?'var(--karte)':c}" stroke="var(--bg)" stroke-width="1.5"/><text text-anchor="middle" dominant-baseline="central" font-size="8.5" font-weight="900" fill="#fff">${st==='plan'?z.p:zei}</text></g>`;
 s+=`</g><path d="M-5,-10 L0,0 L5,-10 Z" fill="${z?c:'var(--linie)'}"/><circle r="2.2" fill="var(--hs)"/>`;
 if(st==='dran')s=`<circle class="puls" r="9"/>`+s;return s}
// ---------- Welt ----------
function welt(){const {W,H}=GW;let s=`<path d="${GW.sph}" fill="var(--meer)"/><path d="${GW.grat}" fill="none" stroke="var(--gitter)" stroke-width="1.5"/>`;
 for(const x of GW.L)s+=`<path class="kont" d="${x.d}" fill="${KF[x.k]||'#ccc'}" fill-opacity="${x.k==='eu'?.95:.6}" stroke="var(--grenze)" stroke-width="1.6" vector-effect="non-scaling-stroke" data-k="${x.k}" data-wl="${x.a2}"/>`;
 if(flagArt==='pin'||flagArt==='marke'){for(const x of [...GW.L].filter(x=>x.hp&&x.k!=='ant').sort((a,b)=>a.hp[1]-b.hp[1]))s+=ms(x.hp[0],x.hp[1],flagArt==='marke'?landMarke(x.a2,x.de,x.hs,null):landPin(x.a2,x.de,x.hs,null,true),'zl lpin',`data-ar="${x.ar}" data-wl="${x.a2}"`)}else{for(const x of GW.L){if(x.hp)s+=ms(x.hp[0],x.hp[1],`${hsZ}<text class="hsname" x="8" y="4">${esc(x.hs)}</text>`,'zl hs',`data-ar="${x.ar}"`);}
 for(const x of GW.L){if(x.k==='ant')continue;s+=ms(x.lp[0],x.lp[1]-6,landLabel(x.a2,x.de),'zl ll',`data-ar="${x.ar}"`)}}
 const KP={eu:[15,54],as:[92,48],or:[46,31],af:[20,6],na:[-100,47],sa:[-60,-14],au:[134,-27],po:[-150,-12]};
 for(const k in KN){const [n,g,a,b]=KN[k];const pp=projW(KP[k]);s+=ms(pp[0],pp[1],`<text class="kname" style="fill:${KF[k]}">${n.toUpperCase()}</text><text class="welt-z" y="20" style="font-weight:800;fill:var(--tx)">${g} · ${a}/${b} Länder</text>`,'kont kl',`data-k="${k}"`)}
 s+=ms(W/2,H-40,`<text class="welt-l">Antarktis</text><text class="welt-z" y="16">Expeditionen · 0 von 21 Stationen</text>`,'kl');
 s+=ms(GW.du[0],GW.du[1],`<circle class="puls" r="8"/><circle r="6" fill="var(--dranR)" stroke="#fff" stroke-width="2"/>`);
 return {W,H,svg:s}}
function projW([lo,la]){// Natural Earth 1 wie im Bau (Näherung über bekannte Punkte reicht nicht) – deshalb vorab berechnet
 return PROJ[lo+','+la]}
// ---------- Europa ----------
function europa(){const [W,H]=G.eurWH;let s=`<defs><pattern id="schraffur" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="var(--sperr)"/><line x1="0" y1="0" x2="0" y2="8" stroke="var(--linie)" stroke-width="3"/></pattern></defs><rect width="${W}" height="${H}" fill="var(--meer)"/>`;
 for(const x of G.eur){const z=ZU[x.n];s+=`<path class="${['land',x.eu?'eu':'fremd',z?z.s:'',sel===x.n?'sel':''].join(' ')}" d="${x.d}" data-l="${esc(x.n)}"/>`}
 for(const x of G.eur){const z=ZU[x.n];if(z&&z.s==='dran')s+=`<path class="umriss" d="${x.d}" stroke="var(--dranR)"/>`}
 const LP=n=>{const x=BY(n);return flagArt==='pin'||flagArt==='marke'?[x.hp[0],x.hp[1]-(flagArt==='marke'?0:12)]:(x.lp||x.c)};
 const P=REISE.map(LP);const iD=REISE.indexOf('Italy');
 for(let i=0;i<P.length-1;i++)s+=`<path class="route ${i<iD?'war':'kommt'}" d="${bogen(P[i],P[i+1])}"/>`;
 if(flagArt!=='rund'&&flagArt!=='eckig'&&flagArt!=='aus'){const AR=a2=>{const w=GW.L.find(y=>y.a2===a2);return w?w.ar*4.2:500};const L=G.eur.filter(x=>x.hp).sort((a,b)=>(ZU[a.n]?1:0)-(ZU[b.n]?1:0)||b.hp[1]-a.hp[1]);
  for(const x of L){const z=ZU[x.n];s+=ms(x.hp[0],x.hp[1],flagArt==='marke'?landMarke(x.a2,x.de,x.hs,z):landPin(x.a2,x.de,x.hs,z,!z),'zl lpin',`data-ar="${z?9e9:AR(x.a2)}" data-l="${esc(x.n)}"`)}return {W,H,svg:s}}
 for(const x of G.eur){if(!x.hp)continue;s+=ms(x.hp[0],x.hp[1],`${hsZ}<text class="hsname" x="8" y="4">${esc(x.hs)}</text>`,'zl hs',`data-ar="${ZU[x.n]?9e9:9e9}"`)}
 for(const x of G.eur){if(!x.eu||!x.lp)continue;const z=ZU[x.n];const KLEIN=['LU','MC','SM','LI','AD','MT','XK','ME','MD','CY','AL','MK','BA'];
  let mark='';if(z){if(z.s==='gesch'||z.s==='gold')mark=`<g transform="translate(0,${flagArt==='eckig'?-30:-20})">${stempel(z.s==='gold')}</g>`;if(z.s==='plan')mark=`<g class="pin" transform="translate(0,${flagArt==='eckig'?-30:-19})"><circle r="11" fill="var(--planR)"/><text>${z.p}</text></g>`;if(z.s==='sperr')mark=`<g transform="translate(0,${flagArt==='eckig'?-28:-18})"><circle r="10" fill="var(--karte)" stroke="var(--linie)"/><text text-anchor="middle" dominant-baseline="central" font-size="11">🔒</text></g>`;if(z.s==='dran')mark=`<circle class="puls" r="9" cy="0"/><g transform="translate(0,${flagArt==='eckig'?-34:-22}) rotate(35)">${flieger()}</g>`}
  s+=ms(x.lp[0],x.lp[1],landLabel(x.a2,x.de,!!z)+mark,'zl ll',`data-ar="${z?9e9:(KLEIN.includes(x.a2)?50:5000)}"`)}
 return {W,H,svg:s}}
// ---------- Italien ----------
function italien(){const [W,H]=G.itWH;let s=`<rect width="${W}" height="${H}" fill="var(--meer)"/>`;
 for(const x of G.ita){const it=x.n==='Italy';s+=`<path class="land ${it?'offen':'fremd'}" d="${x.d}"/>`}
 for(const x of G.ita){if(x.n==='Italy')s+=`<path class="umriss" d="${x.d}" stroke="var(--dranR)" style="stroke-width:2"/>`}
 for(const x of G.ita){if(x.n!=='Italy'&&x.c&&x.c[0]>40&&x.c[0]<W-40&&x.c[1]>40&&x.c[1]<H-40)s+=ms(x.c[0],x.c[1],`<g style="opacity:.55">${landLabel(x.a2,x.de)}</g>`)}
 const S=G.itS;const iD=S.findIndex(c=>IST[c.n]==='dran');
 const ne=S[1].p;s+=ms(ne[0]+150,ne[1]+230,`<g>${flagArt==='aus'?'':plakette('IT',22,-78,-6)}<text class="lname gross" y="0" text-anchor="middle">ITALIEN</text><text class="welt-z" y="18">Land · Natürliche Zahlen</text></g>`);
 for(let i=0;i<S.length-1;i++){const a=S[i].p,b=S[i+1].p;s+=`<path class="route ${i<iD?'war':'kommt'}" d="${bogen(a,b,.12)}" ${IST[S[i+1].n]==='kuer'?'style="stroke:var(--leise);stroke-dasharray:1 6"':''}/>`}
 S.forEach((c,i)=>{const st=IST[c.n]||(i<iD?'gelandet':'offen');const [x,y]=c.p;
  const fill={abgelegt:'var(--goldR)',gelandet:'var(--geschR)',faellig:'var(--geschR)',dran:'var(--dranR)',offen:'var(--karte)',kuer:'var(--karte)'}[st];const hell=st==='offen'||st==='kuer';
  let inner=`<rect x="${st==='dran'?-14:-11}" y="${st==='dran'?-14:-11}" width="${st==='dran'?28:22}" height="${st==='dran'?28:22}" rx="7" fill="${fill}" style="stroke:${hell?'var(--leise)':'var(--bg)'};stroke-width:2" ${st==='kuer'?'stroke-dasharray="3 3"':''}/>`;
  inner+=`<text text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="800" fill="${hell?'var(--leise)':'#fff'}">${st==='abgelegt'?'★':st==='gelandet'||st==='faellig'?'✓':i+1}</text>`;
  if(st==='faellig')inner+=`<g transform="translate(12,-12)"><circle r="8" fill="var(--planR)" stroke="var(--bg)" stroke-width="2"/><text text-anchor="middle" dominant-baseline="central" font-size="10" font-weight="900" fill="#fff">↻</text></g>`;
  if(st==='dran')inner=`<circle class="puls" r="10"/>`+inner+`<g transform="translate(0,-32) rotate(-20)">${flieger()}</g>`;
  if(c.n==='Rom')inner+=flagArt==='pin'||flagArt==='marke'?`<g transform="translate(-26,8) scale(.85)">${landPin('IT','','',null,true).replace(/<g class="pintext">.*<\/g>$/,'')}</g>`:`<g transform="translate(-20,10)">${hsZ}</g>`;
  const lx=['Bari','Pompei','Rom','Siena','Florenz','Bologna','Venedig'].includes(c.n)?18:-18;
  inner+=`<text class="sname ${hell?'leise':''}" x="${lx}" y="5" text-anchor="${lx>0?'start':'end'}">${esc(c.n)}${st==='kuer'?' · Kür':''}${st==='dran'?` · ${DRAN_N}/6`:''}</text>`;
  s+=ms(x,y,inner)});
 return {W,H,svg:s}}
// ---------- Rahmen ----------
function unten(){const jetzt=`<div class="jetzt"><div class="flagge">${flHtml('IT',22)}</div><div style="flex:1;min-width:0"><div class="t1">GERADE DRAN</div><div class="t2">Bologna <span style="font-weight:600;color:var(--leise);font-size:13px">in Italien</span></div><div class="t3">Natürliche Zahlen · Stadt 5 von 13</div></div><div style="text-align:right;font-weight:800">${DRAN_N}/6<div class="balken" style="width:64px;margin-top:4px">${[0,1,2,3,4,5].map(i=>`<i class="${i<DRAN_N?'g':''}"></i>`).join('')}</div></div></div>`;
 return {jetzt,btn:`<button class="start"><span>Weiter in Bologna<small>Stadt 5 · Welchen Wert hat eine Ziffer?</small></span><span>›</span></button>`}}
function kopf(){const C=[['welt','🌍','WELT','Welt'],['europa','','KONTINENT','Europa'],['land',flHtml('IT',12),'LAND','Italien']];
 return `<div class="kopfzeile"><h1>Meine Reise</h1><span class="st">★ 2 340</span></div><div class="brot">${C.map(([v,ic,cap,t],i)=>`<a data-ans="${v}" class="${ansicht===v?'an':''}"><small>${cap}</small><span>${ic} ${t}${v!=='welt'?' <i class="mich">📍</i>':''}</span></a>${i<2?'<i class="pf">›</i>':''}`).join('')}<a class="zumir" data-ans="land" title="Zu mir">📍 Zu mir</a></div>`}
function legende(){if(ansicht==='welt')return `<div class="legende"><span>${'<svg width="13" height="13"><circle cx="6.5" cy="6.5" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="6.5" cy="6.5" r="2" fill="currentColor"/></svg>'}Hauptstadt</span><span><b style="font-size:9.5px;letter-spacing:.06em">NAME</b>&nbsp;Land</span><span style="color:var(--leise)">Zoomen zeigt mehr Namen</span></div>`;
 const hsL=`<span><svg width="13" height="13"><circle cx="6.5" cy="6.5" r="5" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="6.5" cy="6.5" r="2" fill="currentColor"/></svg>Hauptstadt</span>`;
 if(ansicht==='land')return `<div class="legende"><b class="lk">STÄDTE DEINER REISE</b><span><i class="q" style="background:var(--goldR)"></i>abgelegt</span><span><i class="q" style="background:var(--geschR)"></i>gelandet</span><span><i class="q" style="background:var(--planR);border-radius:50%"></i>↻ heute wiederholen</span><span><i class="q" style="background:var(--dranR)"></i>hier bist du</span><span><i class="q" style="border:1.5px dashed var(--leise)"></i>Kür</span>${hsL}</div>`;
 return `<div class="legende"><b class="lk">LÄNDER</b><span><i style="background:var(--gesch);border-color:var(--geschR)"></i>✓ geschafft – noch in Wiederholung</span><span><i style="background:var(--gold);border-color:var(--goldR)"></i>★ golden – alles sitzt</span><span><i style="background:var(--dran);border-color:var(--dranR)"></i>gerade dran</span><span><i style="background:var(--plan);border-color:var(--planR)"></i>im Plan</span><span><i style="background:var(--offen);border-color:var(--linie)"></i>offen</span><span><i style="background:var(--sperr);border-color:var(--linie)"></i>🔒 gesperrt</span>${hsL}</div>`}
function routeListe(){return REISE.map(n=>{const z=ZU[n],x=BY(n);const c={gesch:'var(--geschR)',gold:'var(--goldR)',dran:'var(--dranR)',plan:'var(--planR)'}[z.s];return `<div class="lzeile"><span class="nr" style="background:${c}">${z.s==='gesch'?'✓':z.s==='gold'?'★':z.s==='plan'?z.p:'▶'}</span>${flHtml(x.a2,13)}<b>${esc(x.de)}</b><span style="color:var(--leise)">· ${esc(TITEL[n])}</span></div>`}).join('')}
function stadtListe(){return G.itS.map((c,i)=>{const st=IST[c.n]||(i<4?'gelandet':'offen');return `<span class="${st==='abgelegt'?'a':st==='gelandet'||st==='faellig'?'g':st==='dran'?'d':''}">${i+1} ${esc(c.n)}${st==='faellig'?' ↻':''}${st==='kuer'?' · Kür':''}</span>`}).join('')}
function blattInhalt(){if(!sel)return '';let x,z,de,hs,a2;
 if(sel.startsWith('W:')){const w=GW.L.find(y=>y.a2===sel.slice(2));if(!w)return '';de=w.de;hs=w.hs;a2=w.a2;z=null;x={k:w.k}}else{x=BY(sel);z=ZU[sel];de=x.de;hs=x.hs;a2=x.a2}
 let h=`<div class="bk"><span class="cap">LAND</span></div><h3>${flHtml(a2,20)} ${esc(de)}</h3><div class="sub"><svg width="12" height="12" style="vertical-align:-1px"><circle cx="6" cy="6" r="4.5" fill="none" stroke="currentColor" stroke-width="1.5"/><circle cx="6" cy="6" r="1.8" fill="currentColor"/></svg> Hauptstadt: <b>${esc(hs||'–')}</b>${x.k&&KN[x.k]?` · Kontinent ${KN[x.k][0]}`:''}</div>`;
 if(z){h+=`<div class="zeile"><span class="chip">✈ ${esc(TITEL[sel])}</span><span class="chip">${STAEDTE[sel]} Städte</span></div><div class="zeile"><b>${ZT[z.s]}${z.p?' · Platz '+z.p:''}</b>${z.w?`<span style="color:var(--leise)">– ${esc(z.w)}</span>`:''}</div>`;
  h+=`<div class="zeile">${sel==='Italy'?'<button class="start" data-ans="land" style="flex:1;font-size:15px;padding:11px 14px"><span>Städte in Italien ansehen</span><span>›</span></button>':'<span style="color:var(--leise);font-size:12px">(Im Entwurf hat nur Italien eine Städte-Ansicht.)</span>'}</div>`}
 else h+=`<div class="zeile" style="color:var(--leise)">${sel.startsWith('W:')&&!['eu'].includes(x.k)?'Mathe-Flüge hier: siehe Kontinent.':'Hier gibt es (noch) keinen Mathe-Flug.'}</div>`;
 return h}
function render(){const st=document.getElementById('buehne');const v=ansicht==='welt'?welt():ansicht==='land'?italien():europa();
 if(!vb||vb.ans!==ansicht+breite+knopf){vb={ans:ansicht+breite+knopf,x:0,y:0,w:v.W,h:v.H,W:v.W,H:v.H};const fit=(pts,pad,u)=>{const xs=pts.map(p=>p[0]),ys=pts.map(p=>p[1]);vb.x=Math.min(...xs)-pad;vb.y=Math.min(...ys)-pad;vb.w=Math.max(...xs)-vb.x+pad;vb.h=Math.max(...ys)-vb.y+pad+u};
  const ub=breite==='handy'&&knopf==='karte'?(ansicht==='land'?260:200):0;
  if(ansicht==='europa')fit(REISE.map(n=>BY(n).lp),breite==='handy'?90:200,ub);if(ansicht==='land')fit(G.itS.map(c=>c.p),breite==='handy'?95:170,ub);
  if(ansicht==='welt'){if(breite==='handy'){vb.x=1700;vb.y=180;vb.w=850;vb.h=1500}}}
 const {jetzt,btn}=unten();const bi=blattInhalt();
 const karte=`<div class="kartenrahmen" id="kr">${legende()}<div class="zoom"><button data-z="1.5">+</button><button data-z="0.67">−</button><button data-z="0" title="ganze Karte">⤢</button></div><svg id="sv" xmlns="http://www.w3.org/2000/svg"><defs><clipPath id="rund" clipPathUnits="objectBoundingBox"><circle cx=".5" cy=".5" r=".5"/></clipPath></defs>${v.svg}</svg>${knopf==='karte'&&breite==='handy'?`<div class="schwebe">${jetzt}${btn}</div>`:''}${breite==='handy'?`<div class="blatt ${bi?'auf':''}" id="blatt">${bi?'<button class="x" data-zu>✕</button>'+bi:''}</div>`:''}</div>`;
 let html;
 if(breite==='handy')html=`<div class="geraet handy ${gest}">${kopf()}${karte}${knopf==='unten'?`<div class="unten">${jetzt}${ansicht==='land'?`<div class="stadtliste">${stadtListe()}</div>`:''}${btn}</div>`:''}</div>`;
 else html=`<div class="geraet rechner ${gest}">${kopf()}<div class="koerper">${karte}<div class="seite"><div class="rkarte">${jetzt}<div style="margin-top:12px">${btn}</div></div>${bi?`<div class="rkarte">${bi}</div>`:''}<div class="rkarte"><h4>${ansicht==='land'?'STÄDTE IN ITALIEN':'MEINE ROUTE · LÄNDER'}</h4>${ansicht==='land'?`<div class="stadtliste" style="flex-wrap:wrap">${stadtListe()}</div>`:routeListe()}</div></div></div></div>`;
 st.innerHTML=html;passe()}
function passe(){const kr=document.getElementById('kr'),sv=document.getElementById('sv');if(!kr)return;const W=kr.clientWidth,H=kr.clientHeight;
 sv.setAttribute('width',W);sv.setAttribute('height',H);const r=W/H;let {x,y,w,h}=vb;if(w/h>r){const nh=w/r;y-=(nh-h)/2;h=nh}else{const nw=h*r;x-=(nw-w)/2;w=nw}
 sv.setAttribute('viewBox',`${x} ${y} ${w} ${h}`);const k=w/W;sv.style.setProperty('--k',k.toFixed(3));
 // Namen je nach Zoom: Fläche in Bildschirm-Pixeln entscheidet
 const px=k*k;for(const g of sv.querySelectorAll('.zl.lpin')){const a=+g.dataset.ar/px;const T=ansicht==='welt'?2500:2200;g.style.display=a>(ansicht==='welt'?250:60)?'':'none';const tt=g.querySelector('.pintext');if(tt)tt.style.display=a>T?'':'none';const mk=g.querySelector('.marke');if(flagArt==='marke'&&a<=T)g.style.display=+g.dataset.ar>=9e9?'':'none'}
 for(const g of sv.querySelectorAll('.zl:not(.pin)')){const a=+g.dataset.ar/px;g.style.display=a>(g.classList.contains('hs')?(ansicht==='welt'?9000:4500):(ansicht==='welt'?1400:900))?'':'none'}
 for(const g of sv.querySelectorAll('.kl'))g.style.opacity=ansicht==='welt'&&k<1.4?0:1;if(ansicht==='welt')for(const g of sv.querySelectorAll('.ll,.zl.lpin'))if(k>=1.4&&+g.dataset.ar/px<6000)g.style.display='none'}
document.addEventListener('click',e=>{const t=e.target;
 const b=t.closest('[data-g]');if(b){const g=b.dataset.g,v=b.dataset.v;if(g==='gest')gest=v;if(g==='knopf')knopf=v;if(g==='breite')breite=v;if(g==='flagge')flagArt=v;if(g==='ans'){ansicht=v;sel=null}document.querySelectorAll(`[data-g="${g}"]`).forEach(x=>x.classList.toggle('an',x.dataset.v===v));render();return}
 const a=t.closest('[data-ans]');if(a){ansicht=a.dataset.ans;sel=null;vb=null;document.querySelectorAll('[data-g="ans"]').forEach(x=>x.classList.toggle('an',x.dataset.v===ansicht));render();return}
 if(t.closest('[data-zu]')){sel=null;render();return}
 const z=t.closest('[data-z]');if(z){const f=+z.dataset.z;if(!f){vb.x=0;vb.y=0;vb.w=vb.W;vb.h=vb.H}else{const cx=vb.x+vb.w/2,cy=vb.y+vb.h/2;vb.w/=f;vb.h/=f;vb.x=cx-vb.w/2;vb.y=cy-vb.h/2}passe();return}
 if(zug)return;
 const kl=t.closest('.kl[data-k]');if(kl&&kl.dataset.k==='eu'){ansicht='europa';vb=null;document.querySelectorAll('[data-g="ans"]').forEach(x=>x.classList.toggle('an',x.dataset.v==='europa'));render();return}
 const wl=t.closest('[data-wl]');if(wl){sel='W:'+wl.dataset.wl;render();return}
 const l=t.closest('[data-l]');if(l){const n=l.dataset.l;const x=BY(n);if(x&&x.eu){sel=n;render()}}});
let drag=null,zug=false;
document.addEventListener('pointerdown',e=>{const kr=e.target.closest('#kr');if(!kr||e.target.closest('button,.schwebe,.blatt,.legende'))return;drag={x:e.clientX,y:e.clientY,vx:vb.x,vy:vb.y};zug=false});
document.addEventListener('pointermove',e=>{if(!drag)return;const kr=document.getElementById('kr');const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>4)zug=true;const sv=document.getElementById('sv');const m=sv.viewBox.baseVal.width/kr.clientWidth;vb.x=drag.vx-dx*m;vb.y=drag.vy-dy*m;passe()});
document.addEventListener('pointerup',()=>{drag=null;setTimeout(()=>zug=false,0)});
document.addEventListener('wheel',e=>{const kr=e.target.closest('#kr');if(!kr)return;e.preventDefault();const f=e.deltaY<0?1.15:1/1.15;const sv=document.getElementById('sv');const bb=kr.getBoundingClientRect();const vbx=sv.viewBox.baseVal;const px=vbx.x+(e.clientX-bb.left)/bb.width*vbx.width,py=vbx.y+(e.clientY-bb.top)/bb.height*vbx.height;vb.x=px-(px-vb.x)/f;vb.y=py-(py-vb.y)/f;vb.w/=f;vb.h/=f;passe()},{passive:false});
render();
