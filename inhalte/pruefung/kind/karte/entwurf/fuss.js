G.WL[0].a=3;
// ---- erfundener Stand Testkind (Europa = Zahlen) ----
const ZU={Austria:{s:'gesch'},Switzerland:{s:'gold'},Slovenia:{s:'gesch'},Italy:{s:'dran'},Greece:{s:'plan',p:2},Germany:{s:'plan',p:3},Belgium:{s:'plan',p:4},'United Kingdom':{s:'offen'},France:{s:'offen'},Spain:{s:'sperr',w:'Visum fehlt: erst „Brüche und Anteile“ (Deutschland)'},Netherlands:{s:'sperr',w:'ab Klasse 9'},Poland:{s:'sperr',w:'ab Klasse 9'},Norway:{s:'sperr',w:'ab Klasse 9'}};
const FLUG={};G.eur.forEach(x=>{if(x.fl>=0)FLUG[x.n]=x});
const TITEL={Italy:'Natürliche Zahlen',Austria:'Ganze Zahlen',Switzerland:'Grundrechenarten',Slovenia:'Potenzen als Schreibweise',Greece:'Teilbarkeit',Germany:'Brüche und Anteile',Belgium:'Dezimalzahlen','United Kingdom':'Rechnen mit rationalen Zahlen',Spain:'Zehnerpotenzen',France:'Negative Exponenten',Netherlands:'Elementare Wurzeln',Poland:'Wurzeln und reelle Zahlen',Norway:'Rationale Exponenten'};
const STAEDTE={Italy:13,Austria:11,Switzerland:14,Slovenia:7,Greece:7,Germany:14,Belgium:8,'United Kingdom':12,Spain:7,France:3,Netherlands:6,Poland:7,Norway:6};
const REISE=['Austria','Switzerland','Slovenia','Italy','Greece','Germany','Belgium'];
const IST={Rom:'abgelegt',Neapel:'gelandet',Pompei:'faellig',Bari:'gelandet',Bologna:'dran',Siena:'kuer'};
const DRAN_N=3;
let gest='tag',knopf='karte',breite='handy',ansicht='europa',sel=null,vb=null;
const BY=n=>G.eur.find(x=>x.n===n);
const ZT={gesch:'geschafft · Stempel',gold:'golden · alle Städte abgelegt',dran:'gerade dran',plan:'im Plan',offen:'offen – kannst du wählen',sperr:'noch gesperrt',kann:'„Kann er“ – von Eltern gesetzt'};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const KLEIN=['Luxembourg','Monaco','San Marino','Liechtenstein','Andorra','Malta','Kosovo','Montenegro','Moldova','Cyprus','Albania','Macedonia','North Macedonia','Bosnia and Herz.'];
function bogen(a,b,h=.18){const mx=(a[0]+b[0])/2,my=(a[1]+b[1])/2,dx=b[0]-a[0],dy=b[1]-a[1];return `M${a} Q${mx+dy*h},${my-dx*h} ${b}`}
const flieger=(f='var(--dranR)')=>`<path d="M0,-11 L3,-3 L11,1 L11,3 L3,1 L2,8 L5,10 L5,11.5 L0,10 L-5,11.5 L-5,10 L-2,8 L-3,1 L-11,3 L-11,1 L-3,-3 Z" fill="${f}" stroke="var(--bg)" stroke-width="1.2"/>`;
const ms=(x,y,inner,cls='')=>`<g transform="translate(${x},${y})" class="${cls}"><g class="ms">${inner}</g></g>`;
function stempel(gold){const c=gold?'var(--goldR)':'var(--geschR)';return `<g class="stempel" transform="rotate(-12)"><circle r="15" fill="${gold?'var(--gold)':'var(--bg)'}" stroke="${c}" stroke-width="2.5"/><circle r="11" fill="none" stroke="${c}" stroke-width="1" stroke-dasharray="2 2"/><text text-anchor="middle" dominant-baseline="central" font-size="13" font-weight="900" fill="${c}">${gold?'★':'✓'}</text></g>`}
// ---------- Europa ----------
function europa(){const [W,H]=G.eurWH;let s='';
 s+=`<defs><pattern id="schraffur" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="var(--sperr)"/><line x1="0" y1="0" x2="0" y2="8" stroke="var(--linie)" stroke-width="3"/></pattern></defs>`;
 s+=`<rect width="${W}" height="${H}" fill="var(--meer)"/>`;
 for(const x of G.eur){const z=ZU[x.n];const cls=['land',x.eu?'eu':'fremd',z?z.s:'',sel===x.n?'sel':''].join(' ');s+=`<path class="${cls}" d="${x.d}" data-l="${esc(x.n)}"/>`}
 // Umriss für dran / plan
 for(const x of G.eur){const z=ZU[x.n];if(z&&z.s==='dran')s+=`<path class="umriss" d="${x.d}" stroke="var(--dranR)"/>`}
 // Ländernamen
 for(const x of G.eur){if(!x.eu||!x.lp)continue;const klein=KLEIN.includes(x.n);s+=`<g transform="translate(${x.lp})"${klein?' class="nurnah"':''}><text class="lname ms2" text-anchor="middle">${esc(x.de)}</text></g>`}
 // Reiseroute (Bögen zwischen Hauptstädten)
 const P=REISE.map(n=>BY(n).hp);const iD=REISE.indexOf('Italy');
 for(let i=0;i<P.length-1;i++)s+=`<path class="route ${i<iD?'war':'kommt'}" d="${bogen(P[i],P[i+1])}"/>`;
 // Hauptstädte
 for(const x of G.eur){if(!x.hp)continue;const fl=FLUG[x.n];s+=ms(x.hp[0],x.hp[1],`<rect x="-4" y="-4" width="8" height="8" class="hsdot"/><text class="hsname" x="8" y="4">${esc(x.hs)}</text>`,fl?'':'nurnah')}
 // Marker
 for(const x of G.eur){const z=ZU[x.n];if(!z||!x.hp)continue;const [a,b]=x.hp;
  if(z.s==='gesch'||z.s==='gold')s+=ms(a,b,`<g transform="translate(-16,-20)">${stempel(z.s==='gold')}</g>`);
  if(z.s==='plan')s+=ms(a,b,`<g transform="translate(-14,-18)">`+`<g class="pin"><circle r="12" fill="var(--planR)"/><text>${z.p}</text></g></g>`);
  if(z.s==='sperr')s+=ms(a,b,`<g transform="translate(-14,-17)"><circle r="11" fill="var(--karte)" stroke="var(--linie)"/><text text-anchor="middle" dominant-baseline="central" font-size="12">🔒</text></g>`);
  if(z.s==='dran')s+=ms(a,b,`<circle class="puls" r="10"/><g transform="translate(0,-24) rotate(35)">${flieger()}</g>`)}
 return {W,H,svg:s}}
// ---------- Italien ----------
function italien(){const [W,H]=G.itWH;let s=`<defs><pattern id="schraffur" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="var(--sperr)"/></pattern></defs><rect width="${W}" height="${H}" fill="var(--meer)"/>`;
 for(const x of G.ita){const it=x.n==='Italy';s+=`<path class="land ${it?'dran':'fremd'}" d="${x.d}" style="${it?'fill:var(--offen)':''}"/>`}
 for(const x of G.ita){if(x.n==='Italy')s+=`<path class="umriss" d="${x.d}" stroke="var(--dranR)" style="stroke-width:2"/>`}
 for(const x of G.ita){if(x.n!=='Italy'&&x.c&&x.c[0]>40&&x.c[0]<W-40&&x.c[1]>40&&x.c[1]<H-40)s+=`<text class="lname" x="${x.c[0]}" y="${x.c[1]}" text-anchor="middle" style="opacity:.45">${esc(x.de)}</text>`}
 s+=`<text class="lname" x="${G.itS[4].p[0]+90}" y="${G.itS[4].p[1]+150}" style="font-size:30px;opacity:.25">ITALIEN</text>`;
 const S=G.itS;const iD=S.findIndex(c=>IST[c.n]==='dran');
 for(let i=0;i<S.length-1;i++){const a=S[i].p,b=S[i+1].p;s+=`<path class="route ${i<iD?'war':'kommt'}" d="${bogen(a,b,.12)}" ${IST[S[i+1].n]==='kuer'?'style="stroke:var(--leise);stroke-dasharray:1 6"':''}/>`}
 S.forEach((c,i)=>{const st=IST[c.n]||(i<iD?'gelandet':'offen');const [x,y]=c.p;
  const fill={abgelegt:'var(--goldR)',gelandet:'var(--geschR)',faellig:'var(--geschR)',dran:'var(--dranR)',offen:'var(--karte)',kuer:'var(--karte)'}[st];
  let inner=`<circle r="${st==='dran'?13:10}" fill="${fill}" ${st==='offen'||st==='kuer'?'style="stroke:var(--leise);stroke-width:2"':''} ${st==='kuer'?'stroke-dasharray="3 3"':''}/>`;
  inner+=`<text text-anchor="middle" dominant-baseline="central" font-size="11" font-weight="800" fill="${st==='offen'||st==='kuer'?'var(--leise)':'#fff'}">${st==='abgelegt'?'★':st==='gelandet'||st==='faellig'?'✓':i+1}</text>`;
  if(st==='faellig')inner+=`<g transform="translate(11,-11)"><circle r="8" fill="var(--planR)" stroke="var(--bg)" stroke-width="2"/><text text-anchor="middle" dominant-baseline="central" font-size="10" font-weight="900" fill="#fff">↻</text></g>`;
  if(st==='dran')inner=`<circle class="puls" r="10"/>`+inner+`<g transform="translate(0,-30) rotate(-20)">${flieger()}</g>`;
  const lx=['Bari','Pompei','Rom','Siena','Florenz','Bologna','Venedig'].includes(c.n)?16:-16;
  inner+=`<text class="sname ${st==='offen'||st==='kuer'?'leise':''}" x="${lx}" y="5" text-anchor="${lx>0?'start':'end'}">${esc(c.n)}${st==='kuer'?' · Kür':''}${st==='dran'?` · ${DRAN_N}/6`:''}</text>`;
  s+=ms(x,y,inner)});
 return {W,H,svg:s}}
// ---------- Welt ----------
function welt(){const [W,H]=G.weltWH;const F={eu:'#7FB2E5',as:'#E8A65C',or:'#D98C8C',af:'#E3C35C',na:'#8CC98C',sa:'#B49BD8',au:'#7CC8C0',ant:'#E8EEF2'};
 let s=`<path d="${G.sph}" fill="var(--meer)"/><path d="${G.grat}" fill="none" stroke="var(--gitter)" stroke-width=".6"/>`;
 for(const x of G.welt)s+=`<path class="kont" d="${x.d}" fill="${F[x.k]||'#ccc'}" fill-opacity="${x.k==='eu'?1:.55}" stroke="var(--grenze)" stroke-width=".4" data-k="${x.k}"/>`;
 s+=`<circle cx="${G.poly[0]}" cy="${G.poly[1]}" r="38" fill="#F3B6D0" fill-opacity=".35" stroke="#E07AA6" stroke-dasharray="4 4"/>`;
 for(const l of G.WL)s+=`<g class="kont" data-k="${l.k}">`+ms(l.p[0],l.p[1],`<text class="welt-l">${l.n}</text><text class="welt-z" y="16">${l.g}</text><text class="welt-z" y="31" style="font-weight:800;fill:var(--tx)">${l.a} von ${l.b} Ländern</text>`)+`</g>`;
 s+=ms(W/2,H-24,`<text class="welt-l">Antarktis</text><text class="welt-z" y="16">Expeditionen · 0 von 21 Stationen</text>`);
 s+=`<g transform="translate(${G.weltDu})"><circle class="puls" r="6"/><circle r="5" fill="var(--dranR)" stroke="#fff" stroke-width="2"/></g>`;
 return {W,H,svg:s}}
// ---------- Seite ----------
function unten(){const it=ansicht==='land';
 const jetzt=`<div class="jetzt"><div class="flagge">🇮🇹</div><div style="flex:1;min-width:0"><div class="t1">GERADE DRAN</div><div class="t2">Italien · Bologna</div><div class="t3">Natürliche Zahlen · Stadt 5 von 13</div></div><div style="text-align:right;font-weight:800">${DRAN_N}/6<div class="balken" style="width:64px;margin-top:4px">${[0,1,2,3,4,5].map(i=>`<i class="${i<DRAN_N?'g':''}"></i>`).join('')}</div></div></div>`;
 const btn=`<button class="start"><span>Weiter in Bologna<small>Stadt 5 · Welchen Wert hat eine Ziffer?</small></span><span>›</span></button>`;
 return {jetzt,btn}}
function kopf(){const crumbs=[['welt','Welt'],['europa','Europa'],['land','Italien']];
 return `<div class="kopfzeile"><h1>Meine Reise</h1><span class="st">★ 2 340</span></div><div class="brot">${crumbs.map(([v,t],i)=>`<a data-ans="${v}" class="${ansicht===v?'an':''}">${t}</a>${i<2?'<i>›</i>':''}`).join('')}</div>`}
function legende(){if(ansicht==='welt')return '';if(ansicht==='land')return `<div class="legende"><span><i style="background:var(--goldR);border-color:var(--goldR);border-radius:50%"></i>abgelegt</span><span><i style="background:var(--geschR);border-color:var(--geschR);border-radius:50%"></i>gelandet</span><span><i style="background:var(--planR);border-color:var(--planR);border-radius:50%"></i>↻ heute wiederholen</span><span><i style="background:var(--dranR);border-color:var(--dranR);border-radius:50%"></i>hier bist du</span><span><i style="border-color:var(--leise);border-style:dashed;border-radius:50%"></i>Kür</span></div>`;
 return `<div class="legende"><span><i style="background:var(--gesch);border-color:var(--geschR)"></i>geschafft</span><span><i style="background:var(--gold);border-color:var(--goldR)"></i>golden</span><span><i style="background:var(--dran);border-color:var(--dranR)"></i>gerade dran</span><span><i style="background:var(--plan);border-color:var(--planR)"></i>im Plan</span><span><i style="background:var(--offen);border-color:var(--linie)"></i>offen</span><span><i style="background:var(--sperr);border-color:var(--linie)"></i>🔒 gesperrt</span></div>`}
function routeListe(){return REISE.map((n,i)=>{const z=ZU[n],x=BY(n);const c={gesch:'var(--geschR)',gold:'var(--goldR)',dran:'var(--dranR)',plan:'var(--planR)'}[z.s];return `<div class="lzeile"><span class="nr" style="background:${c}">${z.s==='gesch'?'✓':z.s==='gold'?'★':z.s==='plan'?z.p:'▶'}</span><b>${esc(x.de)}</b><span style="color:var(--leise)">· ${esc(TITEL[n])}</span></div>`}).join('')}
function stadtListe(){return G.itS.map((c,i)=>{const st=IST[c.n]||(i<4?'gelandet':'offen');return `<span class="${st==='abgelegt'?'a':st==='gelandet'||st==='faellig'?'g':st==='dran'?'d':''}">${i+1} ${esc(c.n)}${st==='faellig'?' ↻':''}${st==='kuer'?' · Kür':''}</span>`}).join('')}
function blatt(){if(!sel)return '<div class="blatt" id="blatt"></div>';const x=BY(sel);const z=ZU[sel];
 let h=`<button class="x" data-zu>✕</button><h3>${esc(x.de)}</h3><div class="sub">Hauptstadt: <b>${esc(x.hs)}</b></div>`;
 if(z){h+=`<div class="zeile"><span class="chip">✈ ${esc(TITEL[sel])}</span><span class="chip">${STAEDTE[sel]} Städte</span></div><div class="zeile"><b>${ZT[z.s]}${z.p?' · Platz '+z.p:''}</b>${z.w?`<span style="color:var(--leise)">– ${esc(z.w)}</span>`:''}</div>`;
  h+=`<div class="zeile">${sel==='Italy'?'<button class="start" data-ans="land" style="flex:1;font-size:15px;padding:11px 14px"><span>Route in Italien ansehen</span><span>›</span></button>':'<span style="color:var(--leise);font-size:12px">(Im Entwurf hat nur Italien eine Städte-Ansicht.)</span>'}</div>`}
 else h+=`<div class="zeile" style="color:var(--leise)">Hier gibt es noch keinen Mathe-Flug. Gut zu wissen: Hauptstadt ${esc(x.hs)}.</div>`;
 return `<div class="blatt auf" id="blatt">${h}</div>`}
function render(){const st=document.getElementById('buehne');const v=ansicht==='welt'?welt():ansicht==='land'?italien():europa();
 if(!vb||vb.ans!==ansicht+breite){vb={ans:ansicht+breite,x:0,y:0,w:v.W,h:v.H,W:v.W,H:v.H};const fit=(pts,pad,unten)=>{const xs=pts.map(p=>p[0]),ys=pts.map(p=>p[1]);vb.x=Math.min(...xs)-pad;vb.y=Math.min(...ys)-pad;vb.w=Math.max(...xs)-vb.x+pad;vb.h=Math.max(...ys)-vb.y+pad+unten};
  const ub=breite==='handy'&&knopf==='karte'?(ansicht==='land'?260:200):0;
  if(ansicht==='welt'&&breite==='handy'){vb.x=330;vb.y=40;vb.w=330;vb.h=520}if(ansicht==='europa')fit(REISE.map(n=>BY(n).hp),breite==='handy'?70:180,ub);if(ansicht==='land')fit(G.itS.map(c=>c.p),breite==='handy'?95:170,ub)}
 const {jetzt,btn}=unten();
 const karte=`<div class="kartenrahmen" id="kr">${legende()}<div class="zoom"><button data-z="1.4">+</button><button data-z="0.7">−</button><button data-z="0" title="ganze Karte">⤢</button></div><svg id="sv" xmlns="http://www.w3.org/2000/svg">${v.svg}</svg>${knopf==='karte'&&breite==='handy'?`<div class="schwebe">${jetzt}${btn}</div>`:''}${breite==='handy'?blatt():''}</div>`;
 let html;
 if(breite==='handy')html=`<div class="geraet handy ${gest}">${kopf()}${karte}${knopf==='unten'?`<div class="unten">${jetzt}${ansicht==='land'?`<div class="stadtliste">${stadtListe()}</div>`:''}${btn}</div>`:''}</div>`;
 else html=`<div class="geraet rechner ${gest}">${kopf()}<div class="koerper">${karte}<div class="seite"><div class="rkarte">${jetzt}<div style="margin-top:12px">${btn}</div></div>${sel?`<div class="rkarte" style="position:relative">${blatt().replace('class="blatt auf"','style=""').replace('<button class="x" data-zu>✕</button>','')}</div>`:''}<div class="rkarte"><h4>${ansicht==='land'?'STÄDTE IN ITALIEN':'MEINE ROUTE IN EUROPA'}</h4>${ansicht==='land'?`<div class="stadtliste" style="flex-wrap:wrap">${stadtListe()}</div>`:routeListe()}</div></div></div></div>`;
 st.innerHTML=html;passe()}
function passe(){const kr=document.getElementById('kr'),sv=document.getElementById('sv');if(!kr)return;const W=kr.clientWidth,H=kr.clientHeight;
 sv.setAttribute('width',W);sv.setAttribute('height',H);
 // Seitenverhältnis halten
 const r=W/H;let {x,y,w,h}=vb;if(w/h>r){const nh=w/r;y-=(nh-h)/2;h=nh}else{const nw=h*r;x-=(nw-w)/2;w=nw}
 sv.setAttribute('viewBox',`${x} ${y} ${w} ${h}`);const z=Math.max(.5,(vb.W/w)*(W/vb.W)*1);sv.style.setProperty('--k',(w/W).toFixed(3));
 sv.dataset.nah=(w/W)<1.05?'ja':'nein'}
document.addEventListener('click',e=>{const t=e.target;
 const b=t.closest('[data-g]');if(b){const g=b.dataset.g,v=b.dataset.v;if(g==='gest')gest=v;if(g==='knopf')knopf=v;if(g==='breite'){breite=v;vb=null}if(g==='ans'){ansicht=v;sel=null}document.querySelectorAll(`[data-g="${g}"]`).forEach(x=>x.classList.toggle('an',x.dataset.v===v));render();return}
 const a=t.closest('[data-ans]');if(a){ansicht=a.dataset.ans;sel=null;document.querySelectorAll('[data-g="ans"]').forEach(x=>x.classList.toggle('an',x.dataset.v===ansicht));render();return}
 if(t.closest('[data-zu]')){sel=null;render();return}
 const z=t.closest('[data-z]');if(z){const f=+z.dataset.z;if(!f){vb.x=0;vb.y=0;vb.w=vb.W;vb.h=vb.H}else{const cx=vb.x+vb.w/2,cy=vb.y+vb.h/2;vb.w/=f;vb.h/=f;vb.x=cx-vb.w/2;vb.y=cy-vb.h/2}passe();return}
 const k=t.closest('.kont');if(k&&k.dataset.k==='eu'){ansicht='europa';document.querySelectorAll('[data-g="ans"]').forEach(x=>x.classList.toggle('an',x.dataset.v==='europa'));render();return}
 const l=t.closest('[data-l]');if(l&&!zug){const n=l.dataset.l;const x=BY(n);if(x&&x.eu){sel=n;render()}}});
let drag=null,zug=false;
document.addEventListener('pointerdown',e=>{const kr=e.target.closest('#kr');if(!kr||e.target.closest('button,.schwebe,.blatt,.legende'))return;drag={x:e.clientX,y:e.clientY,vx:vb.x,vy:vb.y};zug=false});
document.addEventListener('pointermove',e=>{if(!drag)return;const kr=document.getElementById('kr');const s=vb.w/kr.clientWidth*Math.max(1,(vb.h/vb.w)/(kr.clientHeight/kr.clientWidth))||1;const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>4)zug=true;const sv=document.getElementById('sv');const m=sv.viewBox.baseVal.width/kr.clientWidth;vb.x=drag.vx-dx*m;vb.y=drag.vy-dy*m;passe()});
document.addEventListener('pointerup',()=>{drag=null;setTimeout(()=>zug=false,0)});
document.addEventListener('wheel',e=>{const kr=e.target.closest('#kr');if(!kr)return;e.preventDefault();const f=e.deltaY<0?1.15:1/1.15;const sv=document.getElementById('sv');const bb=kr.getBoundingClientRect();const vbx=sv.viewBox.baseVal;const px=vbx.x+(e.clientX-bb.left)/bb.width*vbx.width,py=vbx.y+(e.clientY-bb.top)/bb.height*vbx.height;vb.x=px-(px-vb.x)/f;vb.y=py-(py-vb.y)/f;vb.w/=f;vb.h/=f;passe()},{passive:false});
render();
