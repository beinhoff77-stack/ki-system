/* Reise/Etappe UI, app-api 0.12.0. Writes require an explicit user action. */
'use strict';
async function tripCall(name,data={}) {
  const r=await aktion(name,data);
  if(!r || typeof r!=='object' || r.ok===false)throw Error(r?.fehler||'Antwort nicht bestätigt. Bitte neu lesen.');
  return r;
}
function tripId(v){const n=Number(v);return Number.isSafeInteger(n)&&n>0?n:null;}
function tripStorno(b){
  if(!b?.storno_kostenlos_bis || !/^\d{4}-\d{2}-\d{2}/.test(b.storno_kostenlos_bis))return 'Stornobedingungen prüfen';
  const date=b.storno_kostenlos_bis.slice(0,10).split('-').reverse().join('.');
  return 'Kostenlos stornierbar bis '+date+' · laut '+(b.storno_quelle||b.anbieter||'Quelle');
}
function tripStart(e){stayWrite('ks_trip_context',{reise_id:e.reise_id,etappe_id:e.id,ziel:e.ziel});route('suche');}
function tripDialog(title){
 const d=el('dialog',{class:'trip-dialog','aria-label':title}),body=el('div'),status=el('p',{role:'status'});
 const close=el('button',{type:'button',onclick:()=>d.close()},'Schließen');
 d.append(el('h2',{},title),close,body,status);main.append(d);d.addEventListener('close',()=>d.remove());d.showModal();return {d,body,status,close};
}
async function tripDelete(kind,id,onSaved){
 const {d,body,status,close}=tripDialog(kind==='etappe'?'Etappe entfernen':'Suche entfernen');let pending=false,preview=null;
 d.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
 const include=el('input',{type:'checkbox'}),confirm=el('button',{type:'button',class:'danger',disabled:true},'In den Papierkorb');
 const data=()=>kind==='etappe'?{etappe_id:id,mit_suchen:include.checked}:{suchauftrag_id:id};
 const read=async()=>{confirm.disabled=true;include.disabled=true;preview=null;status.textContent='Löschfolgen werden geprüft …';try{const r=await tripCall('unterkunft_'+kind+'_loeschen',{...data(),vorschau:true});if(!d.isConnected)return;if(!r.folgen)throw Error('Löschfolgen fehlen.');preview=r.folgen;body.replaceChildren(...[kind==='etappe'&&preview.status!=='vorschlag'?el('label',{},include,' Auch zugehörige Suchen entfernen'):null,tripDeleteSummary(preview),confirm].filter(Boolean));const proposal=preview.status==='vorschlag';confirm.textContent=proposal?'Vorschlag verwerfen':'In den Papierkorb';status.textContent=proposal?'Der Vorschlag wird verworfen. Die Suchen bleiben erhalten.':'Erst deine Bestätigung verschiebt die Auswahl in den Papierkorb.';confirm.disabled=false;include.disabled=false;}catch(e){status.replaceChildren(e.message,kind==='suchauftrag'?el('a',{href:'#/suche/'+id},' Suche öffnen und bei Bedarf abbrechen'):el('a',{href:'#/reisen'},' Reisen neu lesen'));}};
 include.onchange=read;
 confirm.onclick=async()=>{if(pending||!preview)return;pending=true;confirm.disabled=true;close.disabled=true;include.disabled=true;try{const r=await tripCall('unterkunft_'+kind+'_loeschen',data());if(!r.geloescht&&!r.bereits_geloescht)throw Error('Löschen nicht eindeutig bestätigt.');d.close();await onSaved();}catch(e){status.textContent=e.message+' Bitte schließen und den gespeicherten Zustand neu lesen, bevor du erneut löschst.';}finally{pending=false;close.disabled=false;}};
 await read();
}
async function tripEdit(e,onSaved){
 const {d,body,status,close}=tripDialog('Etappe bearbeiten'),form=el('form'),inputs={};let pending=false;
 for(const [key,label,type] of [['ziel','Ort','text'],['notiz','Notiz','text']]){inputs[key]=el('input',{type,value:e[key]||'',required:key!=='notiz'});form.append(el('label',{},label,inputs[key]));}
 form.append(el('p',{},'Neue Reisetage legst du über „Andere Tage suchen“ als eigene Suchvariante an.'));
 const save=el('button',{type:'submit',class:'primary'},'Änderungen speichern');form.append(save);body.append(form);
 d.addEventListener('cancel',ev=>{if(pending)ev.preventDefault();});
 form.onsubmit=async ev=>{ev.preventDefault();if(pending)return;pending=true;save.disabled=true;close.disabled=true;try{const r=await tripCall('unterkunft_etappe_speichern',{id:e.id,version:e.version,...Object.fromEntries(Object.entries(inputs).map(([k,v])=>[k,v.value]))});if(r.etappe?.id!==e.id)throw Error('Änderung nicht bestätigt.');d.close();await onSaved();}catch(err){status.textContent=err.message+' Dein Entwurf bleibt hier. Bitte neu lesen, bevor du erneut speicherst.';}finally{pending=false;close.disabled=false;}};
}
// W131 (Sebastian 07.11.2026): Reiseplan = nur echte Buchungen. Oben Gesamtausgaben, je Land Zwischensumme,
// eine kompakte Zeile pro Unterkunft; Details und Aktionen erst nach Antippen. Pläne getrennt darunter.
function tripNights(e){const n=Number(e.naechte);if(Number.isFinite(n)&&n>0)return n;const d=Math.round((Date.parse(e.abreise)-Date.parse(e.anreise))/86400000);return d>0?d:0;}
function tripPrice(e){const v=Number(e.buchung?.preis_gesamt_eur??e.preis_gesamt_eur);return Number.isFinite(v)&&v>0?v:null;}
function tripEuro(v,digits=2){return Number(v).toLocaleString('de-DE',{style:'currency',currency:'EUR',minimumFractionDigits:digits,maximumFractionDigits:digits});}
function tripDM(iso){const d=new Date(String(iso).slice(0,10)+'T12:00:00');return String(d.getDate()).padStart(2,'0')+'.'+String(d.getMonth()+1).padStart(2,'0')+'.';}
function tripStayDates(a,b){return el('div',{class:'rp-date rp-date-io','aria-label':'Check-in '+tripDM(a)+', Check-out '+tripDM(b)},el('b',{},tripDM(a)),el('span',{class:'rp-date-arrow','aria-hidden':'true'},'↓'),el('span',{},tripDM(b)));}
function tripDateBlock(iso){const d=new Date(String(iso)+'T12:00:00');return el('div',{class:'rp-date','aria-hidden':'true'},el('b',{},String(d.getDate())),d.toLocaleDateString('de-DE',{month:'short'}).replace('.',''));}
function tripToday(){const n=new Date();return [n.getFullYear(),String(n.getMonth()+1).padStart(2,'0'),String(n.getDate()).padStart(2,'0')].join('-');}
function tripClock(v){const m=/T(\d{2}:\d{2})/.exec(String(v||''));return m?m[1]:'';}
function tripDayAdd(d,n){const x=new Date(String(d).slice(0,10)+'T12:00:00Z');x.setUTCDate(x.getUTCDate()+n);return x.toISOString().slice(0,10);}
function tripDayDiff(a,b){const x=String(a||'').slice(0,10),y=String(b||'').slice(0,10);if(!x||!y)return 0;return Math.round((Date.parse(y)-Date.parse(x))/86400000);}
function tripShortDate(v){const d=String(v||'').slice(0,10);return d?d.slice(8,10)+'.'+d.slice(5,7)+'.':'';}
function segBelongsBefore(it,items){ // Zeile bleibt in der aktuellen Gruppe, außer direkt danach beginnt eine Unterkunft (die eine neue Gruppe öffnen kann)
 const idx=items.indexOf(it),d0=it.typ==='gap'?it.g.bis:String(it.s.an||it.s.ab).slice(0,10);
 for(let j=idx+1;j<items.length;j++){if(items[j].typ==='stay')return tripDayDiff(d0,items[j].e.anreise)>1;}return true;}
function segRow(p,s,i,today){
 if(p.art==='tauchen')return diveRow(p,s,i,today);
 const flight=p.art==='flug',plusDays=tripDayDiff(s.ab,s.an),n=p.segmente.length,price=Number(p.preis_gesamt_eur),hasPrice=Number.isFinite(price)&&price>0;
 const past=String(s.an||s.ab||'').slice(0,10)<today;
 const ic=el('span',{class:'rp-seg-ic '+(flight?'is-flug':'is-auto'),'aria-hidden':'true'},stayIcon(flight?'flug':'auto'));
 const main=flight?[s.von||'?',' ',tripClock(s.ab),' → ',s.nach||'?',' ',tripClock(s.an),plusDays>0?el('small',{},' +'+plusDays):null]
  :(tripClock(s.ab)?[tripClock(s.ab),' → ',tripShortDate(s.an),' ',tripClock(s.an)]:['bis ',tripShortDate(s.an),' · ',tripDayDiff(s.ab,s.an)+' Tage']);
 const sub=flight?[[s.nr,s.airline].filter(Boolean).join(' '),p.buchungscode].filter(Boolean).join(' · ')
  :[s.ort,s.fahrzeug,p.anbieter].filter(Boolean).join(' · ');
 const priceNode=i===0?el('div',{class:'rp-seg-price'},hasPrice?tripEuro(price,0):'? €',el('span',{},(p.preis_ca&&hasPrice?'ca. · ':'')+(n>1?n+(flight?' Flüge':' Teile'):(hasPrice?(flight?'Flug':tripDayDiff(s.ab,s.an)+' Tage'):'nachtragen'))))
  :el('div',{class:'rp-seg-price'},el('span',{},'im '+(n>3?'Ticket':'Paket')));
 const head=el('summary',{class:'rp-seg'},el('div',{class:'rp-date rp-date-seg'},el('b',{},tripDM(s.ab)),el('span',{},new Date(String(s.ab).slice(0,10)+'T12:00:00').toLocaleDateString('de-DE',{weekday:'short'}).replace('.',''))),el('div',{class:'rp-main'},el('div',{class:'rp-seg-main'},...main),el('div',{class:'rp-sub rp-seg-sub'},ic,sub)),priceNode);
 const body=el('div',{class:'rp-detail'});
 const item=el('details',{class:'rp-item rp-seg-item '+(flight?'is-flug':'is-transport')+(past?' is-past':''),'data-posten':p.id,'data-seg':i},head,body);
 item.addEventListener('toggle',()=>{if(!item.open||body.childElementCount)return;
  const facts=el('dl',{class:'rp-facts'});const add=(k,v)=>{if(v)facts.append(el('dt',{},k),el('dd',{},v));};
  add('Buchung',[p.titel,p.anbieter].filter(Boolean).join(' · '));add('Code',p.buchungscode);
  add('Preis',hasPrice?(p.preis_ca?'ca. ':'')+tripEuro(price)+(p.waehrung&&p.waehrung!=='EUR'?' ('+Number(p.preis_original).toLocaleString('de-DE')+' '+p.waehrung+')':''):'nicht eingetragen');
  if(flight){add('Abflug',[s.von_name||s.von,fmtDate(String(s.ab).slice(0,10)),tripClock(s.ab)].filter(Boolean).join(' · '));add('Ankunft',[s.nach_name||s.nach,fmtDate(String(s.an).slice(0,10)),tripClock(s.an)].filter(Boolean).join(' · '));add('Klasse',s.klasse);add('Sitze',s.sitze);}
  else{add('Abholung',fmtDate(String(s.ab).slice(0,10))+' '+tripClock(s.ab));add('Rückgabe',fmtDate(String(s.an).slice(0,10))+' '+tripClock(s.an));add('Ort',s.ort);}
  body.append(facts);
  if(n>1){const list=el('ol',{class:'rp-seg-list'});p.segmente.forEach((x,j)=>list.append(el('li',{class:j===i?'is-current':''},el('b',{},tripShortDate(x.ab)),' ',[x.nr,x.von+' '+tripClock(x.ab)+' → '+x.nach+' '+tripClock(x.an)].filter(Boolean).join(' · '))));body.append(el('details',{class:'rp-note'},el('summary',{},'Alle '+n+' Flüge dieser Buchung'),list));}
  if(p.link)body.append(el('a',{class:'rp-link',href:p.link,target:'_blank',rel:'noopener'},stayIcon('extern'),'Buchung öffnen'));
  if(p.notiz)body.append(el('details',{class:'rp-note'},el('summary',{},'Notiz'),el('p',{class:'booking-note'},p.notiz)));
 });
 return item;
}
// W142 (Sebastian 07.11.2026): Nebenkosten vor Ort je Monat und Kategorie, am Monatsende im Reiseplan
const NK_KAT={essen:'Essen & Trinken',erleben:'Erlebnisse & Wellness',unterwegs:'Unterwegs',sonst:'Sonstiges'};
const NK_KURZ={essen:'Essen',erleben:'Erlebnisse',unterwegs:'Unterwegs',sonst:'Sonstiges'};
function kostenRow(n,today){
 const kats=Array.isArray(n.kategorien)?n.kategorien:[],sum=Number(n.summe)||0,mon=new Date(String(n.bis)+'T12:00:00').toLocaleDateString('de-DE',{month:'long'});
 const open=String(n.stand||'')<String(n.bis||'');
 const ic=el('span',{class:'rp-seg-ic is-kosten','aria-hidden':'true'},stayIcon('geld'));
 const head=el('summary',{class:'rp-seg'},el('div',{class:'rp-date rp-date-seg'},el('b',{},tripDM(n.bis)),el('span',{},'Ende')),
  el('div',{class:'rp-main'},el('div',{class:'rp-seg-main'},'Nebenkosten '+mon),el('div',{class:'rp-sub rp-seg-sub'},ic,kats.map(k=>(NK_KURZ[k.key]||k.key)+' '+tripEuro(k.eur,0)).join(' · '))),
  el('div',{class:'rp-seg-price'},tripEuro(sum,0),el('span',{},open?'bis '+tripDM(n.stand):'Monat')));
 const body=el('div',{class:'rp-detail'});
 const item=el('details',{class:'rp-item rp-seg-item is-kosten'+(String(n.bis)<today?' is-past':''),'data-kosten':n.monat},head,body);
 item.addEventListener('toggle',()=>{if(!item.open||body.childElementCount)return;
  for(const k of kats){const top=Array.isArray(k.top)?k.top:[];
   body.append(el('div',{class:'rp-nk-kat'},el('div',{class:'rp-nk-head'},el('b',{},NK_KAT[k.key]||k.key),el('span',{},tripEuro(k.eur,0)+(k.anzahl?' · '+k.anzahl+(k.anzahl===1?' Buchung':' Buchungen'):''))),
    el('p',{class:'rp-nk-top'},top.map(t=>t.anbieter+' '+tripEuro(t.eur,0)).join(' · '))));}
  body.append(el('p',{class:'booking-note'},'Kreditkarte vor Ort'+(n.stand?' bis '+tripDM(n.stand):'')+'. Ohne Unterkünfte, Flüge, Mietwagen und Tauchen (stehen einzeln im Plan) und ohne private Ausgaben. Auslandsgebühr 2 % unter Sonstiges.'));
 });
 return item;
}
// W140 (Sebastian 07.11.2026): Tauchtage als eigene Art – ein Segment je Tauchtag, mit Taucher, Gebiet und Log-Werten
function diveNum(v,d=1){const n=Number(v);return Number.isFinite(n)?n.toLocaleString('de-DE',{maximumFractionDigits:d}):'';}
function diveRow(p,s,i,today){
 const price=Number(p.preis_gesamt_eur),hasPrice=Number.isFinite(price)&&price>0,tg=Array.isArray(s.tg)?s.tg:[],n=Number(s.tauchgaenge)||tg.length||0;
 const who=Array.isArray(s.taucher)?s.taucher:[],past=String(s.an||s.ab||'').slice(0,10)<today;
 const depths=tg.map(x=>Number(x.max_tiefe_m)).filter(Number.isFinite),maxD=depths.length?Math.max(...depths):null;
 const ic=el('span',{class:'rp-seg-ic is-tauchen','aria-hidden':'true'},stayIcon('tauchen'));
 const main=[n+(n===1?' Tauchgang':' Tauchgänge'),maxD!==null?' · bis '+diveNum(maxD)+' m':'',' · '+(who.length===4?'alle 4':who.length?who.join(', '):'Taucher offen')];
 const sub=[s.gebiet||s.ort,p.anbieter].filter(Boolean).join(' · ');
 const priceNode=el('div',{class:'rp-seg-price'},hasPrice?tripEuro(price,0):(p.kurs?.offen?'Kurs folgt':'? €'),el('span',{},(p.preis_ca&&hasPrice?'ca. · ':'')+(p.waehrung&&p.waehrung!=='EUR'&&p.preis_original?Number(p.preis_original).toLocaleString('de-DE')+' '+p.waehrung:'Tauchen')));
 const head=el('summary',{class:'rp-seg'},el('div',{class:'rp-date rp-date-seg'},el('b',{},tripDM(s.ab)),el('span',{},new Date(String(s.ab).slice(0,10)+'T12:00:00').toLocaleDateString('de-DE',{weekday:'short'}).replace('.',''))),el('div',{class:'rp-main'},el('div',{class:'rp-seg-main'},...main),el('div',{class:'rp-sub rp-seg-sub'},ic,sub)),priceNode);
 const body=el('div',{class:'rp-detail'});
 const item=el('details',{class:'rp-item rp-seg-item is-tauchen'+(past?' is-past':''),'data-posten':p.id,'data-seg':i},head,body);
 item.addEventListener('toggle',()=>{if(!item.open||body.childElementCount)return;
  const facts=el('dl',{class:'rp-facts'});const add=(k,v)=>{if(v)facts.append(el('dt',{},k),el('dd',{},v));};
  add('Anbieter',p.anbieter);add('Getaucht',who.join(', '));add('Gebiet',[s.gebiet,s.ort,s.land].filter(Boolean).join(' · '));
  add('Zeit',[fmtDate(String(s.ab).slice(0,10)),[tripClock(s.ab),tripClock(s.an)].filter(Boolean).join('–')].filter(Boolean).join(' · '));add('Modus',s.modus);
  add('Preis',hasPrice?(p.preis_ca?'ca. ':'')+tripEuro(price)+(p.waehrung&&p.waehrung!=='EUR'?' ('+Number(p.preis_original).toLocaleString('de-DE')+' '+p.waehrung+(p.kurs?.kurs?', Kurs '+p.kurs.datum:'')+')':''):(p.kurs?.offen?'Umrechnung folgt ('+Number(p.preis_original).toLocaleString('de-DE')+' '+p.waehrung+')':'nicht eingetragen'));
  body.append(facts);
  if(tg.length){const list=el('ol',{class:'rp-seg-list rp-dive-list'});for(const x of tg){const lat=Number(x.lat),lon=Number(x.lon),map=Number.isFinite(lat)&&Number.isFinite(lon)?el('a',{href:'https://www.google.com/maps?q='+lat+','+lon,target:'_blank',rel:'noopener'},'Karte'):null;
   list.append(el('li',{},el('b',{},'TG '+(x.nr||'')),' ',[x.start,x.dauer_min?x.dauer_min+' min':'',x.max_tiefe_m!=null?'max. '+diveNum(x.max_tiefe_m)+' m':'',x.temp_c!=null?diveNum(x.temp_c)+' °C':'',x.gebiet].filter(Boolean).join(' · '),map?' · ':'',map));}
   body.append(el('details',{class:'rp-note',open:true},el('summary',{},'Tauchgänge laut Log'),list));}
  if(p.link)body.append(el('a',{class:'rp-link',href:p.link,target:'_blank',rel:'noopener'},stayIcon('extern'),'Buchung öffnen'));
  if(p.notiz)body.append(el('details',{class:'rp-note'},el('summary',{},'Notiz'),el('p',{class:'booking-note'},p.notiz)));
 });
 return item;
}
function gapRow(g,rid,today){
 const n=tripDayDiff(g.von,g.bis),past=g.bis<=today;
 const node=el('div',{class:'rp-gap'+(past?' is-past':'')},el('span',{},el('b',{},n+(n===1?' Nacht':' Nächte')+' ohne Unterkunft'),' · '+[g.ort,tripShortDate(g.von)+'–'+tripShortDate(g.bis)].filter(Boolean).join(' · ')));
 if(!past)node.append(el('button',{class:'rp-gap-btn',onclick:()=>{stayWrite('ks_trip_context',{reise_id:rid,anreise:g.von,abreise:g.bis,...(g.ort_name?{ziel:g.ort_name}:{})});route('suche');}},stayIcon('lupe'),'Suchen'));
 return node;
}
const TRIP_LAND_ISO={'deutschland':'DE','österreich':'AT','schweiz':'CH','frankreich':'FR','italien':'IT','spanien':'ES','portugal':'PT','niederlande':'NL','belgien':'BE','luxemburg':'LU','dänemark':'DK','norwegen':'NO','schweden':'SE','finnland':'FI','island':'IS','irland':'IE','großbritannien':'GB','vereinigtes königreich':'GB','england':'GB','polen':'PL','tschechien':'CZ','ungarn':'HU','kroatien':'HR','griechenland':'GR','türkei':'TR','zypern':'CY','malta':'MT',
 'vereinigte arabische emirate':'AE','vae':'AE','katar':'QA','oman':'OM','saudi-arabien':'SA','bahrain':'BH','kuwait':'KW','jordanien':'JO','israel':'IL','ägypten':'EG','marokko':'MA','tunesien':'TN','südafrika':'ZA','kenia':'KE','tansania':'TZ','mauritius':'MU','seychellen':'SC','namibia':'NA','botswana':'BW',
 'japan':'JP','taiwan':'TW','china':'CN','hongkong':'HK','macau':'MO','südkorea':'KR','thailand':'TH','vietnam':'VN','kambodscha':'KH','laos':'LA','malaysia':'MY','singapur':'SG','indonesien':'ID','philippinen':'PH','indien':'IN','sri lanka':'LK','malediven':'MV','nepal':'NP','myanmar':'MM','mongolei':'MN',
 'australien':'AU','neuseeland':'NZ','fidschi':'FJ','samoa':'WS','französisch-polynesien':'PF','tahiti':'PF','palau':'PW','cookinseln':'CK','tonga':'TO','vanuatu':'VU','neukaledonien':'NC',
 'usa':'US','vereinigte staaten':'US','kanada':'CA','mexiko':'MX','kuba':'CU','costa rica':'CR','panama':'PA','kolumbien':'CO','ecuador':'EC','peru':'PE','bolivien':'BO','chile':'CL','argentinien':'AR','brasilien':'BR','uruguay':'UY','paraguay':'PY','venezuela':'VE'};
const TRIP_LAND_KURZ={'vereinigte arabische emirate':'VAE','vereinigte staaten':'USA','vereinigtes königreich':'Großbritannien','französisch-polynesien':'Franz.-Polynesien'};
function tripFlag(land){const iso=TRIP_LAND_ISO[String(land||'').trim().toLowerCase()];return iso?String.fromCodePoint(...[...iso].map(c=>0x1F1E6+c.charCodeAt(0)-65)):'';}
function tripLandShort(land){return TRIP_LAND_KURZ[String(land||'').trim().toLowerCase()]||land;}
function tripMonthYear(d){const x=new Date(String(d).slice(0,10)+'T12:00:00');return x.toLocaleDateString('de-DE',{month:'long',year:'numeric'});}
function tripRange(a,b){const x=new Date(a+'T12:00:00'),y=new Date(b+'T12:00:00'),f=(d,o)=>d.toLocaleDateString('de-DE',o);return x.getFullYear()===y.getFullYear()?f(x,{day:'numeric',month:'short'})+' – '+f(y,{day:'numeric',month:'short',year:'numeric'}):f(x,{day:'numeric',month:'short',year:'numeric'})+' – '+f(y,{day:'numeric',month:'short',year:'numeric'});}
async function viewReisen(arg){
 setChrome('Reiseplan',{tab:'reisen'});const live=viewGuard(),scope=el('section',{class:'trips-page rp'});main.replaceChildren(scope);
 const secOpen=new Map(),status=el('p',{role:'status',class:'rp-status'}),content=el('div'),selector=el('select',{'aria-label':'Reise auswählen'});let snapshot=null,pending=false;
 const reload=el('button',{onclick:load},'Aktualisieren');
 const create=el('button',{onclick:()=>{const {d,body,status:msg}=tripDialog('Neue Reise');const f=el('form'),name=el('input',{required:true,maxlength:100,'aria-label':'Reisename',placeholder:'Japan im Herbst'}),b=el('button',{type:'submit',class:'primary'},'Reise anlegen');f.append(el('label',{},'Reisename',name),b);body.append(f);f.onsubmit=async ev=>{ev.preventDefault();if(b.disabled)return;b.disabled=true;try{const created=await tripCall('unterkunft_reise_speichern',{name:name.value.trim()});if(!tripId(created.reise?.id))throw Error('Reise nicht eindeutig bestätigt.');d.close();await load();}catch(e){msg.textContent=e.message+' Bitte neu lesen, bevor du erneut anlegst.';}};}},'Neue Reise');
 const more=el('details',{class:'rp-more'},el('summary',{'aria-label':'Weitere Aktionen',title:'Weitere Aktionen'},'⋯'),el('div',{class:'rp-more-list'},create,reload,el('a',{href:'#/papierkorb'},'Papierkorb')));
 const top=el('div',{class:'rp-top'},selector);scope.append(top,status,content);
 selector.onchange=()=>{stayWrite('ks_reise',Number(selector.value));draw();};
 async function change(e,data){if(pending)return;pending=true;scope.querySelectorAll('button').forEach(b=>b.disabled=true);try{const r=await tripCall('unterkunft_etappe_speichern',{id:e.id,version:e.version,...data});if(r.etappe?.id!==e.id)throw Error('Änderung nicht bestätigt.');await load();}catch(err){status.textContent=err.message+' Bitte aktualisieren.';}finally{pending=false;scope.querySelectorAll('button').forEach(b=>b.disabled=false);}}
 function row(e,today,photos){
  const b=e.buchung||{},n=tripNights(e),p=tripPrice(e),booked=e.status==='gebucht',now=e.anreise<=today&&e.abreise>today,past=e.abreise<=today;
  const sub=[e.ziel,n+(n===1?' Nacht':' Nächte'),b.anbieter].filter(Boolean).join(' · ');
  const price=booked?el('div',{class:'rp-price'},p===null?'–':tripEuro(p,0),el('span',{},p!==null&&n?tripEuro(p/n,0)+'/N':'Preis fehlt')):el('div',{class:'rp-price rp-open'},'offen');
  const head=el('summary',{class:'rp-row'},tripStayDates(e.anreise,e.abreise),el('div',{class:'rp-main'},el('div',{class:'rp-name'},booked?(b.name||'Unterkunft'):e.ziel),el('div',{class:'rp-sub'},now?el('span',{class:'rp-now'},'jetzt'):null,booked?sub:fmtDate(e.anreise)+'–'+fmtDate(e.abreise)+' · '+n+(n===1?' Nacht':' Nächte'))),price);
  const body=el('div',{class:'rp-detail'});
  const item=el('details',{class:'rp-item'+(now?' is-now':'')+(past?' is-past':''),'data-stage':e.id},head,body);
  item.addEventListener('toggle',()=>{if(!item.open||body.childElementCount)return;
   const facts=el('dl',{class:'rp-facts'});const add=(k,v)=>{if(v)facts.append(el('dt',{},k),el('dd',{},v));};
   add('Zeitraum',fmtDate(e.anreise)+' – '+fmtDate(e.abreise));
   if(booked){add('Zimmer',b.zimmer);add('Gesamt',p===null?null:tripEuro(p)+(n?' · Ø '+tripEuro(p/n)+' pro Nacht':''));add('Storno',b.storno_kostenlos_bis?tripStorno(b):b.storno_text);}
   body.append(facts);
   if(b.link)body.append(el('a',{class:'rp-link',href:b.link,target:'_blank',rel:'noopener'},stayIcon('extern'),'Unterkunft öffnen'));
   if(b.notiz)body.append(el('details',{class:'rp-note'},el('summary',{},'Buchungsnotiz'),el('p',{class:'booking-note'},b.notiz)));
   body.append(el('div',{class:'rp-fotos'},tripPhotos(e.id,live,{initialPhotos:photos}))); // W137: Fotos sofort sichtbar
   const acts=el('div',{class:'rp-actions'});
   if(!booked&&e.status==='vorschlag')acts.append(el('button',{class:'primary',onclick:()=>change(e,{status:'geplant'})},'Bestätigen'));
   if(!booked&&!past)acts.append(el('button',{class:'primary',onclick:()=>route('etappe',e.id)},stayIcon('lupe'),'Unterkünfte suchen'),el('button',{onclick:()=>tripExternalBooking(e,load)},'Woanders gebucht'));
   if(!past&&(e.suchen||[]).length){const v=el('details',{class:'rp-variants'},el('summary',{},stayIcon('kalender'),(e.suchen||[]).length+' Suchvarianten'));for(const s of e.suchen){const active=s.id===e.aktive_suche_id;v.append(el('div',{class:'trip-variant'},el('a',{href:'#/suche/'+s.id},`${fmtDate(s.anreise)}–${fmtDate(s.abreise)} · ${s.status}`),active?el('strong',{},'Aktuell'):el('button',{onclick:()=>change(e,{aktive_suche_id:s.id})},'Diese Tage verwenden'),el('button',{onclick:()=>tripDelete('suchauftrag',s.id,load)},'Suche entfernen')));}body.append(v);}
   acts.append(el('button',{onclick:()=>tripEdit(e,load)},'Bearbeiten'),el('button',{class:'rp-danger',onclick:()=>tripDelete('etappe',e.id,load)},e.status==='vorschlag'?'Vorschlag verwerfen':'Entfernen'));
   body.append(acts);
  });
  return item;
 }
 function draw(){
  const open=new Set([...content.querySelectorAll('details.rp-item[open]')].map(n=>Number(n.dataset.stage)));
  const rid=Number(selector.value),trip=snapshot.reisen.find(x=>x.id===rid);content.replaceChildren();
  if(!trip){content.append(el('div',{class:'rp-empty'},el('p',{},'Leg deine erste Reise an. Danach kannst du Unterkünfte eintragen und suchen.'),more));return;}
  const today=tripToday(),stages=snapshot.etappen.filter(e=>e.reise_id===rid).sort((a,b)=>String(a.anreise).localeCompare(String(b.anreise))||a.id-b.id);
  const booked=stages.filter(e=>e.status==='gebucht'),plans=stages.filter(e=>e.status!=='gebucht'&&e.abreise>today);
  // W132: Flüge, Mietwagen und Tickets (snapshot.posten) – eine Zeile je Segment zwischen den Unterkünften
  const posten=(snapshot.posten||[]).filter(p=>p.reise_id===rid&&Array.isArray(p.segmente));
  const postenBooked=posten.filter(p=>p.status!=='geplant'),postenPlan=posten.filter(p=>p.status==='geplant');
  const cents=v=>Math.round(Number(v)*100),pPrice=p=>{const v=Number(p.preis_gesamt_eur);return Number.isFinite(v)&&v>0?v:null;};
  const priced=booked.filter(e=>tripPrice(e)!==null),stayTotal=priced.reduce((s,e)=>s+cents(tripPrice(e)),0)/100,nights=booked.reduce((s,e)=>s+tripNights(e),0),pricedNights=priced.reduce((s,e)=>s+tripNights(e),0);
  const sumArt=a=>postenBooked.filter(p=>p.art===a&&pPrice(p)!==null).reduce((s,p)=>s+cents(pPrice(p)),0)/100;
  const flightTotal=sumArt('flug'),carTotal=sumArt('mietwagen'),diveTotal=sumArt('tauchen'),otherTotal=postenBooked.filter(p=>!['flug','mietwagen','tauchen'].includes(p.art)&&pPrice(p)!==null).reduce((s,p)=>s+cents(pPrice(p)),0)/100;
  const tage=(snapshot.ausgaben_tage||[]).filter(t=>t.reise_id===rid),tagSum=t=>(Number(t.essen)||0)+(Number(t.erleben)||0)+(Number(t.unterwegs)||0)+(Number(t.sonst)||0);
  const tageVon=tage.length?tage[0].datum:null,tageBis=tage.length?tage[tage.length-1].datum:null;
  const essenIn=(a,b)=>{if(!tageVon)return {essen:0,neben:0,days:0};const xs=tage.filter(t=>t.datum>=a&&t.datum<b);const von=a>tageVon?a:tageVon,bisIncl=(b>tageBis?tageBis:tripDayAdd(b,-1));const days=tageVon&&von<=bisIncl?tripDayDiff(von,bisIncl)+1:0;return {essen:xs.reduce((c,t)=>c+(Number(t.essen)||0),0),neben:xs.reduce((c,t)=>c+tagSum(t),0),days};};
  const neben=(snapshot.nebenkosten||[]).filter(n=>n.reise_id===rid),nebenTotal=neben.reduce((c,n)=>c+cents(Number(n.summe)||0),0)/100,nebenStand=neben.map(n=>String(n.stand||'')).sort().pop();
  const total=Math.round((stayTotal+flightTotal+carTotal+diveTotal+otherTotal+nebenTotal)*100)/100,missing=(booked.length-priced.length)+postenBooked.filter(p=>pPrice(p)===null).length;
  const approx=postenBooked.some(p=>p.preis_ca);
  const photos=stages.length?tripCall('unterkunft_fotos_lesen',{reise_id:rid}).then(r=>{if(!Array.isArray(r.fotos))throw Error('Fotos nicht vollständig lesbar.');return r.fotos;}):null;photos?.catch(()=>{});
  // W133: Zeitleiste in Abschnitten je Land, Filter Hotel / Flug / Transport
  const items=[];
  for(const e of booked)items.push({k:String(e.anreise)+'T23:00',typ:'stay',e,von:e.anreise,bis:e.abreise,land:e.buchung?.land||e.ziel});
  for(const p of postenBooked)p.segmente.forEach((x,i)=>items.push({k:String(x.ab||p.beginn||''),typ:'seg',p,s:x,i,von:String(x.ab||'').slice(0,10),bis:String(x.an||x.ab||'').slice(0,10),land:p.art==='flug'?(x.von_land||''):(x.land||'')}));
  for(const n of neben)items.push({k:String(n.bis)+'T23:58',typ:'kosten',n,von:String(n.bis),bis:String(n.bis),land:''});
  items.sort((a,b)=>a.k.localeCompare(b.k));
  const dayAdd=(d,n)=>{const x=new Date(d+'T12:00:00Z');x.setUTCDate(x.getUTCDate()+n);return x.toISOString().slice(0,10);};
  const covered=new Set();for(const e of booked)for(let d=e.anreise;d<e.abreise;d=dayAdd(d,1))covered.add(d);
  for(const p of postenBooked)if(p.art==='flug')for(const x of p.segmente){const a=String(x.ab||'').slice(0,10),b=String(x.an||'').slice(0,10);if(a&&b)for(let d=a;d<b;d=dayAdd(d,1))covered.add(d);}
  const allDates=items.filter(it=>it.typ!=='kosten').flatMap(it=>[it.von,it.bis]).filter(Boolean).sort();
  const flights=postenBooked.filter(p=>p.art==='flug').flatMap(p=>p.segmente).filter(x=>x.ab&&x.an);
  const departs=new Set(flights.map(x=>String(x.ab).slice(0,10)));
  const placeAt=d=>{let best=null;for(const x of flights){const a=String(x.an).slice(0,10);if(a<=d&&(!best||String(x.an)>String(best.an)))best=x;}return best;};
  const gaps=[];if(allDates.length){let d=allDates[0],end=allDates[allDates.length-1],cur=null;for(;d<end;d=dayAdd(d,1)){
   if(covered.has(d)){cur=null;continue;}
   if(cur&&departs.has(d))cur=null; // an jedem Abflugtag beginnt ein neuer Ort
   if(!cur){const f=placeAt(d),stayBefore=booked.filter(e=>e.abreise<=d).pop();const fromStay=stayBefore&&(!f||stayBefore.abreise>=String(f.an).slice(0,10));
    cur={von:d,bis:dayAdd(d,1),ort:fromStay?stayBefore.ziel:(f?.nach_name||f?.nach||''),ort_name:fromStay?stayBefore.ziel:(f?.nach_name||''),land:fromStay?(stayBefore.buchung?.land||stayBefore.ziel):(f?.nach_land||f?.nach_name||'')};gaps.push(cur);}
   else cur.bis=dayAdd(d,1);}}
  for(const g of gaps)items.push({k:g.von+'T23:59',typ:'gap',g,von:g.von,bis:g.bis,land:g.land});
  items.sort((a,b)=>a.k.localeCompare(b.k)||(a.typ==='gap'?1:-1));
  // Kennzahlen
  const tripFrom=allDates[0],tripTo=allDates[allDates.length-1],tripDays=tripFrom?tripDayDiff(tripFrom,tripTo):0;
  const dayNo=tripFrom&&today>=tripFrom&&today<=tripTo?tripDayDiff(tripFrom,today)+1:null;
  const flightCount=postenBooked.filter(p=>p.art==='flug').reduce((n,p)=>n+p.segmente.length,0);
  const kpi=(v,l)=>el('span',{class:'rp-stat'},el('b',{},v),' '+l);
  content.append(el('section',{class:'rp-total rp-total-slim','aria-label':'Reise-Übersicht'},
   el('div',{class:'rp-total-head'},el('div',{},el('div',{class:'rp-total-title'},el('span',{class:'rp-total-name'},trip.name),dayNo?el('span',{class:'rp-total-day'},'Tag '+dayNo+' von '+tripDays):null),
     el('div',{class:'rp-stats'},kpi(String(booked.length),booked.length===1?'Unterkunft':'Unterkünfte'),kpi(String(flightCount),flightCount===1?'Flug':'Flüge'),kpi(String(tripDays),'Tage'))),more),
   (()=>{const all=essenIn(tageVon||'0000',tripDayAdd(tageBis||'0000-01-01',1)),tile=(lab,val,sub,cls)=>el('div',{class:'rp-tile'+(cls?' '+cls:'')},el('span',{class:'rp-tile-lab'},lab),el('b',{},val),sub?el('span',{class:'rp-tile-sub'},sub):null);
    const diveDays=postenBooked.filter(p=>p.art==='tauchen').length;
    const det=el('details',{class:'rp-total-money rp-total-fold',open:!!stayRead('ks_rp_kosten_offen',false)||null},
     el('summary',{class:'rp-total-big'},el('span',{},'Ausgegeben'),el('b',{},(approx?'ca. ':'')+tripEuro(total,0))),
     el('div',{class:'rp-tiles'},
      tile('Unterkünfte',tripEuro(stayTotal,0),pricedNights?'Ø '+tripEuro(stayTotal/pricedNights,0)+' / Nacht':null),
      flightTotal?tile('Flüge',tripEuro(flightTotal,0),flightCount+(flightCount===1?' Flug':' Flüge')):null,
      (carTotal+otherTotal)?tile('Transport',tripEuro(carTotal+otherTotal,0),'Mietwagen & Co.'):null,
      diveTotal?tile('Tauchen',tripEuro(diveTotal,0),diveDays+(diveDays===1?' Tauchtag':' Tauchtage')):null,
      nebenTotal?tile('Nebenkosten',tripEuro(nebenTotal,0),nebenStand?'bis '+tripDM(nebenStand):null):null,
      all.days?tile('Essen','Ø '+tripEuro(all.essen/all.days,0)+'/Tag',tripEuro(all.essen,0)+' gesamt','is-food'):null));
    det.addEventListener('toggle',()=>stayWrite('ks_rp_kosten_offen',det.open));return det;})(),
   missing?el('p',{class:'rp-total-hint'},missing+' Buchung(en) ohne Euro-Preis – nicht eingerechnet'+(postenBooked.some(p=>p.kurs?.offen)?' (Wechselkurs wird abgerufen).':'.')):null));
  // Filter: drei kleine Schalter, einzeln an/aus (Standard alle an)
  let filt={hotel:true,flug:true,transport:true,tauchen:true,kosten:true,...(stayRead('ks_rp_filter',{})||{})};
  const kindOf=it=>it.typ==='kosten'?'kosten':it.typ==='seg'?(it.p.art==='flug'?'flug':it.p.art==='tauchen'?'tauchen':'transport'):'hotel';
  const chip=(key,icon,label)=>{const b=el('button',{type:'button',class:'rp-chip rp-chip-ic'+(filt[key]?' on':''),'aria-pressed':String(!!filt[key]),'aria-label':label,title:label,onclick:()=>{filt={...filt,[key]:!filt[key]};stayWrite('ks_rp_filter',filt);b.classList.toggle('on',filt[key]);b.setAttribute('aria-pressed',String(filt[key]));applyFilter();}},stayIcon(icon));return b;};
  content.append(el('div',{class:'rp-filter',role:'group','aria-label':'Anzeigen'},chip('hotel','bett','Hotel'),chip('flug','flug','Flug'),chip('transport','auto','Transport'),postenBooked.some(p=>p.art==='tauchen')?chip('tauchen','tauchen','Tauchen'):null,neben.length?chip('kosten','geld','Nebenkosten'):null));
  function applyFilter(){for(const n of content.querySelectorAll('[data-kind]'))n.hidden=!filt[n.dataset.kind];for(const m of content.querySelectorAll('.rp-month')){let x=m.nextElementSibling,vis=false;while(x&&!x.classList.contains('rp-month')){if(!x.hidden&&x.dataset.kind){vis=true;break;}x=x.nextElementSibling;}m.hidden=!vis;}}
  if(!booked.length&&!postenBooked.length)content.append(el('p',{class:'rp-empty'},'Noch keine Buchung eingetragen.'));
  // Abschnitte bilden: Flüge bleiben im aktuellen Abschnitt, Unterkünfte/Lücken/Mietwagen eines anderen Landes öffnen einen neuen
  const secs=[];let curSec=null;const pend=[];
  for(const it of items){
   if(it.typ==='seg'&&it.p.art==='flug'){if(curSec)curSec.items.push(it);else pend.push(it);continue;}
   const L=it.land||(curSec?curSec.lands[curSec.lands.length-1]:'Weitere Reise');
   if(!curSec||curSec.lands[curSec.lands.length-1]!==L){curSec={lands:[L],items:[]};secs.push(curSec);}
   curSec.items.push(...pend.splice(0),it);
  }
  if(pend.length){if(!curSec){curSec={lands:['Weitere Reise'],items:[]};secs.push(curSec);}curSec.items.push(...pend);}
  const secRange=sec=>{const core=sec.items.filter(it=>it.typ!=='seg'||it.p.art!=='flug');const src=core.length?core:sec.items;const ds=src.flatMap(it=>[it.von,it.bis]).filter(Boolean).sort();return {von:ds[0],bis:ds[ds.length-1]};};
  for(const sec of secs)Object.assign(sec,secRange(sec));
  // Kurze Abschnitte (≤ 3 Nächte) mit dem kürzeren Nachbarn zusammenlegen
  for(let i=0;i<secs.length;i++){const sec=secs[i],n=tripDayDiff(sec.von,sec.bis);if(secs.length<2||n>3)continue;
   const prev=secs[i-1],next=secs[i+1],pn=prev?tripDayDiff(prev.von,prev.bis):Infinity,nn=next?tripDayDiff(next.von,next.bis):Infinity;
   const into=pn<=nn?prev:next;if(!into)continue;
   if(into===prev){prev.items.push(...sec.items);prev.lands.push(...sec.lands.filter(l=>!prev.lands.includes(l)));}else{next.items.unshift(...sec.items);next.lands.unshift(...sec.lands.filter(l=>!next.lands.includes(l)));}
   into.items.sort((x,y)=>x.k.localeCompare(y.k)||(x.typ==='gap'?1:y.typ==='gap'?-1:0));Object.assign(into,secRange(into));secs.splice(i,1);i--;}
  const horizon=dayAdd(today,28);
  for(const sec of secs){
   const n=tripDayDiff(sec.von,sec.bis),isNow=sec.von<=today&&today<sec.bis,isPast=sec.bis<=today,isSoon=!isPast&&sec.von<=horizon;
   const key=rid+':'+sec.lands.join('|')+':'+sec.von;const open=secOpen.has(key)?secOpen.get(key):(isNow||isSoon);
   const sumPlan=sec.items.reduce((c,it)=>it.typ==='stay'?c+cents(tripPrice(it.e)||0):(it.typ==='seg'&&it.i===0&&it.p.segmente.length<=3?c+cents(pPrice(it.p)||0):c),0)/100;
   const secAus=essenIn(sec.von,sec.bis),sum=Math.round((sumPlan+secAus.neben)*100)/100;
   const secStays=sec.items.filter(it=>it.typ==='stay'&&tripPrice(it.e)!==null),secStayEur=secStays.reduce((c,it)=>c+(tripPrice(it.e)||0),0),secNights=secStays.reduce((c,it)=>c+tripNights(it.e),0);
   const avg=[secNights?'Hotel Ø '+tripEuro(secStayEur/secNights,0)+'/Nacht':null,secAus.days?'Essen Ø '+tripEuro(secAus.essen/secAus.days,0)+'/Tag':null,secAus.neben?'Nebenkosten '+tripEuro(secAus.neben,0):null].filter(Boolean).join(' · ');
   const offen=sec.items.filter(it=>it.typ==='gap'&&it.bis>today).reduce((c,it)=>c+tripDayDiff(it.von>today?it.von:today,it.bis),0);
   const nFl=sec.items.filter(it=>it.typ==='seg'&&it.p.art==='flug').length,nSt=sec.items.filter(it=>it.typ==='stay').length,nTg=sec.items.filter(it=>it.typ==='seg'&&it.p.art==='tauchen').length;
   const when=isNow?'jetzt':isPast?'abgeschlossen':(()=>{const d=tripDayDiff(today,sec.von);return d<=1?'morgen':d<=31?'in '+d+' Tagen':'ab '+tripMonthYear(sec.von);})();
   const head=el('summary',{class:'rp-sec-head'},
    el('div',{class:'rp-sec-title'},el('span',{class:'rp-flags','aria-hidden':'true'},...sec.lands.map(l=>tripFlag(l)).filter(Boolean).map(f=>el('span',{},f))),el('span',{class:'rp-sec-name'},sec.lands.map(tripLandShort).join(' · ')),isNow?el('span',{class:'rp-now'},'jetzt'):null),
    el('div',{class:'rp-sec-meta'},tripRange(sec.von,sec.bis)+' · '+n+(n===1?' Nacht':' Nächte')),
    el('div',{class:'rp-sec-sum'},sum?tripEuro(sum,0):el('i',{},'offen'),el('span',{},isNow?'noch '+tripDayDiff(today,sec.bis)+(tripDayDiff(today,sec.bis)===1?' Tag':' Tage'):when)),
    avg?el('div',{class:'rp-sec-avg'},avg):null,
    el('div',{class:'rp-sec-mini'},[nSt?nSt+(nSt===1?' Unterkunft':' Unterkünfte'):null,nFl?nFl+(nFl===1?' Flug':' Flüge'):null,nTg?nTg+(nTg===1?' Tauchtag':' Tauchtage'):null,offen?el('b',{},offen+(offen===1?' Nacht offen':' Nächte offen')):null].filter(Boolean).flatMap((x,i)=>i?[' · ',x]:[x])));
   const body=el('div',{class:'rp-sec-body'});
   const secEl=el('details',{class:'rp-sec'+(isNow?' is-now':'')+(isPast?' is-past':''),open},head,body);
   secEl.addEventListener('toggle',()=>secOpen.set(key,secEl.open));
   const rowFor=it=>{const node=it.typ==='kosten'?kostenRow(it.n,today):it.typ==='stay'?row(it.e,today,photos):it.typ==='seg'?segRow(it.p,it.s,it.i,today):gapRow(it.g,rid,today);node.dataset.kind=kindOf(it);return node;};
   const withMonths=(list,target)=>{let m=null,first=null;for(const it of list){const mm=String(it.von||'').slice(0,7);if(mm&&mm!==m){m=mm;const lab=el('div',{class:'rp-month','data-month':mm},tripMonthYear(it.von));first=first||lab;target.append(lab);}target.append(rowFor(it));}return {first,last:m};};
   if(isNow||isSoon){
    const isPast=it=>it.bis<=today&&!(it.typ==='stay'&&it.e.abreise>today),isRun=it=>it.typ==='seg'&&!['flug','tauchen'].includes(it.p.art)&&it.von<today; // W137: laufender Mietwagen bleibt an seinem Startdatum
    let cut=sec.items.findIndex(it=>!isPast(it)&&!isRun(it));if(cut<0)cut=sec.items.length;
    const before=sec.items.slice(0,cut).filter(it=>it.von<=today),after=sec.items.filter(it=>it.von>horizon),mid=sec.items.filter(it=>!before.includes(it)&&!after.includes(it));
    let beforeLast=null,midRes=null;
    if(before.length){const d=el('details',{class:'rp-more-rows'},el('summary',{},'Bisher in '+sec.lands.map(tripLandShort).join(' · ')+' · '+before.length+' Einträge anzeigen'));d.addEventListener('toggle',()=>{if(d.open&&d.childElementCount===1){beforeLast=withMonths(before,d).last;applyFilter();}if(midRes?.first)midRes.first.classList.toggle('is-dup',d.open&&beforeLast===midRes.first.dataset.month);});body.append(d);}
    midRes=withMonths(mid,body);
    if(after.length){const d=el('details',{class:'rp-more-rows'},el('summary',{},'Ab '+tripShortDate(dayAdd(horizon,1))+' · '+after.length+' weitere Einträge'));d.addEventListener('toggle',()=>{if(d.open&&d.childElementCount===1){withMonths(after,d);applyFilter();}});body.append(d);}
   }else withMonths(sec.items,body);
   content.append(secEl);
  }
  applyFilter();
  const lastEnd=allDates[allDates.length-1];
  content.append(el('section',{class:'rp-plans'},
   el('div',{class:'rp-group-head'},el('span',{},stayIcon('kalender'),'Geplant'),el('span',{},(plans.length+postenPlan.length)?(plans.length+postenPlan.length)+' offen':'')),
   ...plans.map(e=>row(e,today,photos)),
   ...postenPlan.flatMap(p=>p.segmente.map((s,i)=>segRow(p,s,i,today))),
   el('div',{class:'rp-next'},
    el('button',{class:'primary',onclick:()=>{stayWrite('ks_trip_context',{reise_id:rid});route('suche');}},stayIcon('plus'),'Nächsten Aufenthalt planen'),
    el('button',{onclick:()=>tripExternalBooking({reise_id:rid},load)},'Buchung nachtragen')),
   lastEnd&&lastEnd>=today&&!plans.length&&!gaps.length?el('p',{class:'rp-sub rp-center'},'Ab '+fmtDate(lastEnd)+' noch nichts gebucht.'):null));
  for(const id of open)content.querySelector(`details.rp-item[data-stage="${id}"]`)?.setAttribute('open','');
  const loose=(snapshot.ohne_etappe||[]).filter(s=>s.reise_id===rid||!s.reise_id);if(loose.length){const box=el('details',{class:'rp-loose'},el('summary',{},'Suchen ohne Etappe ('+loose.length+')'));for(const s of loose){const target=el('select',{'aria-label':'Etappe für Suche '+s.id},el('option',{value:''},'Etappe wählen'),stages.map(e=>el('option',{value:e.id},e.ziel+' · '+fmtDate(e.anreise))));box.append(el('div',{class:'trip-variant'},el('a',{href:'#/suche/'+s.id},'Suche #'+s.id+' · '+s.ziel),target,el('button',{onclick:async ev=>{if(!tripId(target.value))return;ev.target.disabled=true;try{const r=await tripCall('unterkunft_etappe_zuordnen',{suchauftrag_id:s.id,etappe_id:Number(target.value)});if(!r.suche)throw Error('Zuordnung nicht bestätigt.');await load();}catch(e){status.textContent=e.message+' Bitte neu lesen.';}}},'Zuordnen')));}content.append(box);}
 }
 async function load(){reload.disabled=true;status.textContent='Reiseplan wird geladen …';try{const r=await tripCall('unterkunft_etappen_lesen');if(!live())return;if(!Array.isArray(r.reisen)||!Array.isArray(r.etappen))throw Error('Reiseübersicht unvollständig.');snapshot=r;const selected=tripId(arg)||Number(selector.value)||stayRead('ks_reise',null);selector.replaceChildren(...r.reisen.map(t=>el('option',{value:t.id},t.name)));if(r.reisen.some(t=>t.id===selected))selector.value=selected;top.hidden=r.reisen.length<2;draw();status.textContent='';}catch(e){if(live())status.textContent=e.message;}finally{reload.disabled=false;more.open=false;}}
 await load();
}
async function viewPapierkorb(){
 setChrome('Papierkorb',{tab:'reisen',back:true});const live=viewGuard(),scope=el('section',{class:'trips-page'}),status=el('p',{role:'status'}),list=el('div');main.replaceChildren(scope);scope.append(el('h2',{},'Papierkorb'),el('p',{},'Gelöschte Etappen und Suchen lassen sich innerhalb ihrer Frist wiederherstellen.'),el('a',{href:'#/reisen'},'Zurück zu Reisen'),status,list);
 async function load(){try{const r=await tripCall('unterkunft_etappen_lesen',{mit_papierkorb:true});if(!live())return;if(!r.papierkorb)throw Error('Papierkorb nicht vollständig geladen.');list.replaceChildren();for(const [key,kind] of [['etappen','etappe'],['suchen','suchauftrag']])for(const row of r.papierkorb[key]||[]){list.append(el('article',{class:'card'},el('h3',{},row.ziel),el('p',{},fmtDate(row.anreise)+'–'+fmtDate(row.abreise)),el('p',{},'Wiederherstellbar bis '+fmtDate(row.wiederherstellbar_bis)),el('button',{disabled:!!row.endgueltig_geloescht,onclick:async ev=>{ev.target.disabled=true;try{const result=await tripCall('unterkunft_'+kind+'_wiederherstellen',{[kind+'_id']:row.id});if(!result.etappe&&!result.suche)throw Error('Wiederherstellung nicht bestätigt.');status.textContent=result.hinweis||'Wiederhergestellt. Die aktive Suchvariante bitte prüfen.';await load();}catch(e){status.textContent=e.message+' Bitte neu laden, bevor du erneut wiederherstellst.';}}},'Wiederherstellen')));}if(!list.childElementCount)list.append(el('p',{class:'card'},'Dein Papierkorb ist leer.'));}catch(e){status.textContent=e.message;}}
 scope.append(el('button',{onclick:load},'Papierkorb aktualisieren'));await load();
}
async function viewEtappe(arg){
 setChrome('Unterkünfte der Etappe',{tab:'reisen',back:true});const live=viewGuard();loading();const r=await tripCall('unterkunft_etappe_treffer_lesen',{etappe_id:tripId(arg)});if(!live())return;if(!r.etappe||!Array.isArray(r.unterkuenfte))throw Error('Etappe unvollständig.');
 const scope=el('section',{class:'trips-page'},el('a',{href:'#/reisen/'+r.etappe.reise_id},'← Zur Reise'),el('h2',{},r.etappe.ziel),el('p',{},r.aktive_variante_bestaetigt?'Unterkünfte für die bestätigten Tage':'Bitte eine aktive Suchvariante bestätigen.'));main.replaceChildren(scope);
 for(const t of r.unterkuenfte){const active=t.in_aktiver_variante&&r.aktive_variante_bestaetigt&&r.etappe.status!=='vorschlag';scope.append(el('article',{class:'card stage-stay'},sucheFoto(t),el('h3',{},t.name),el('p',{},active?sucheEuro(t.preis_gesamt_eur)+' gesamt':'Für die aktuellen Tage nicht gefunden'),el('p',{},t.status==='favorit'?'♥ Favorit':t.status==='vielleicht'?'Na ja':''),el('a',{href:'#/suche/'+t.suchauftrag_id+'?treffer='+t.treffer_id},'Details und Suchlauf'),el('details',{},el('summary',{},'Frühere Angebote'),(t.frueher||[]).map(s=>el('p',{},fmtDate(s.anreise)+'–'+fmtDate(s.abreise)+' · '+sucheEuro(s.preis_gesamt_eur)+' damals'))),t.status==='favorit'&&active?el('button',{class:'primary',onclick:()=>tripBook(t.treffer_id,r.etappe)},'Als gebucht markieren'):null));}
}
async function tripBook(trefferId,etappe,hit={},searchId=etappe.aktive_suche_id){
 const {d,body,status,close}=tripDialog('Buchung bestätigen');let pending=false;
 const offer=hit.angebot||{},needsConfirm=etappe.status==='vorschlag'||etappe.aktive_suche_id!==searchId;
 const search=etappe.suchen?.find(s=>s.id===searchId)||etappe;
 const form=el('form'),fields={};
 body.append(el('p',{},'Hier vermerkst du eine bereits beim Anbieter abgeschlossene Buchung. Es wird keine Unterkunft gebucht.'),sucheFoto(hit),el('h3',{},hit.name||'Unterkunft'),el('p',{},etappe.ziel+' · '+fmtDate(search.anreise)+'–'+fmtDate(search.abreise)),el('p',{},'Belegung: '+(hit.belegung_text||'laut deiner Buchungsbestätigung; bitte Zimmer und Personen unten prüfen.')));
 for(const [key,label,type,value] of [['name','Unterkunft','text',hit.name||''],['zimmer','Gebuchtes Zimmer / Wohnung','text',offer.kategorie_name||''],['preis_gesamt_eur','Gebuchter Gesamtpreis (€)','number',offer.preis_gesamt_eur??hit.preis_gesamt_eur??''],['storno_text','Stornobedingungen','text',offer.storno||hit.storno||''],['storno_kostenlos_bis','Kostenlos stornierbar bis ('+Intl.DateTimeFormat().resolvedOptions().timeZone+', optional)','datetime-local',''],['notiz','Personen und Buchungsnotiz','text','']]){
  const input=el('input',{type,value,step:type==='number'?'0.01':null,min:type==='number'?0:null,required:key==='name',placeholder:key==='storno_kostenlos_bis'?'2026-11-01T18:00:00+09:00':null});fields[key]=input;form.append(el('label',{},label,input));
 }
 form.append(el('p',{class:'small'},'Preisstand des Angebots: '+sucheAbruf(offer.abrufzeit)+'. Trage die tatsächlich gebuchten Angaben ein. Eine Storno-Erinnerung braucht ein konkretes Datum.'));
 const confirmStage=el('input',{type:'checkbox',required:needsConfirm});if(needsConfirm)form.append(el('label',{},confirmStage,' Diese Etappe und diese Reisetage verbindlich übernehmen.'));
 const button=el('button',{type:'submit',class:'primary'},'Buchung vermerken');form.append(button);body.append(form);
 form.onsubmit=async ev=>{ev.preventDefault();if(pending)return;
  const date=fields.storno_kostenlos_bis.value.trim();if(date&&!Number.isFinite(Date.parse(date))){status.textContent='Bitte ein konkretes Datum mit Uhrzeit eingeben.';return;}
  if(needsConfirm&&!confirmStage.checked)return;
  if(etappe.status==='gebucht'&&etappe.aktive_suche_id!==searchId){status.textContent='Diese Etappe ist bereits für andere Tage gebucht. Bitte eine getrennte Etappe anlegen.';return;}
  const booking={treffer_id:trefferId};for(const [key,input] of Object.entries(fields))if(input.value.trim())booking[key]=key==='preis_gesamt_eur'?Number(input.value):key==='storno_kostenlos_bis'?new Date(input.value).toISOString():input.value.trim();
  pending=true;form.querySelectorAll('input,button').forEach(n=>n.disabled=true);close.disabled=true;
  try{const r=await tripCall('unterkunft_etappe_speichern',{id:etappe.id,version:etappe.version,status:'gebucht',...(needsConfirm?{aktive_suche_id:searchId}:{}),buchung:booking});if(r.etappe?.id!==etappe.id||r.etappe.status!=='gebucht')throw Error('Buchung nicht bestätigt.');d.close();route('reisen',etappe.reise_id);}
  catch(e){status.textContent=e.message+' Bitte den gespeicherten Zustand neu lesen. Dein Entwurf bleibt erhalten.';}
  finally{pending=false;close.disabled=false;}
 };d.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
}
function tripSearchChoice(form,call,live,onPaint=()=>{}){
 const ctx=stayRead('ks_trip_context',{}),reise=el('select',{'aria-label':'Reise',required:true},el('option',{value:''},'Reise wählen')),stage=el('select',{'aria-label':'Aufenthalt'},el('option',{value:''},'Getrennter / neuer Aufenthalt')),notice=el('p',{role:'status'});let data=null;
 const node=el('section',{class:'card trip-choice'},el('h2',{},'In welcher Reise?'),el('label',{},'Reise',reise),el('label',{},'Aufenthalt',stage),el('a',{href:'#/reisen'},'Reisen verwalten'),notice);
 form.querySelector('fieldset').prepend(node);
 const destination=form.querySelector('[name=ziel]');
 function normalize(x){return String(x||'').trim().toLocaleLowerCase('de').replace(/tokio/g,'tokyo').replace(/kioto/g,'kyoto');}
 function report(){const r=reise.selectedOptions[0],st=stage.selectedOptions[0];onPaint({ready:!!data,reise:reise.value?r?.textContent:'',stage:stage.value,stageText:st?.textContent||'',needsChoice:!!data&&(!reise.value||!stage.value),node});}
 function paint(){const previous=stage.value,matching=(data?.etappen||[]).filter(e=>e.reise_id===Number(reise.value)&&normalize(e.ziel)===normalize(destination.value));stage.replaceChildren(...[matching.length?el('option',{value:''},'Bestehender oder getrennter Aufenthalt?'):null,el('option',{value:'new'},'Getrennter / neuer Aufenthalt'),...matching.map(e=>el('option',{value:e.id},e.ziel+' · '+fmtDate(e.anreise)+'–'+fmtDate(e.abreise)))].filter(Boolean));if(matching.some(e=>e.id===Number(previous)))stage.value=previous;else if(matching.some(e=>e.id===ctx.etappe_id))stage.value=ctx.etappe_id;else if(!matching.length)stage.value='new';report();}
 reise.onchange=paint;stage.onchange=report;destination.addEventListener('input',paint);
 call('unterkunft_etappen_lesen').then(r=>{if(!live())return;if(!Array.isArray(r.reisen)||!Array.isArray(r.etappen))throw Error('Reisen konnten nicht geladen werden.');data=r;reise.append(...r.reisen.map(t=>el('option',{value:t.id},t.name)));if(ctx.reise_id&&r.reisen.some(t=>t.id===ctx.reise_id))reise.value=ctx.reise_id;else if(r.reisen.length===1)reise.value=r.reisen[0].id;if(ctx.ziel&&!destination.value)destination.value=ctx.ziel;if(ctx.anreise&&ctx.abreise){for(const [k,v] of [['anreise',ctx.anreise],['abreise',ctx.abreise]]){const i=form.querySelector('[name="'+k+'"]');if(i){i.value=v;i.dispatchEvent(new Event('input',{bubbles:true}));}}const {anreise,abreise,...rest}=ctx;stayWrite('ks_trip_context',rest);}paint();}).catch(e=>{if(live())notice.textContent=e.message;});
 return {node,values(){const rid=tripId(reise.value);if(!data||!rid)throw Error('Bitte zuerst eine Reise wählen.');if(!stage.value)throw Error('Bitte bestehenden oder getrennten Aufenthalt wählen.');return stage.value!=='new'?{reise_id:rid,etappe_id:Number(stage.value)}:{reise_id:rid,etappe_neu:true};},setNew(){if(stage.querySelector('option[value="new"]')){stage.value='new';report();}}};
}

function tripDeleteSummary(f){return el('div',{},el('h3',{},f.ziel||'Ausgewählte Etappe'),el('p',{},[fmtDate(f.anreise),fmtDate(f.abreise)].filter(Boolean).join('–')),el('p',{},(f.treffer??'–')+' Treffer · '+(f.favoriten??'–')+' Favoriten'),f.ist_aktive_variante?el('p',{},'Danach muss eine aktuelle Suchvariante neu bestätigt werden.'):null,f.letzte_suche_der_etappe?el('p',{},'Die Etappe bleibt anschließend ohne Suche bestehen.'):null,el('h4',{},'Wird entfernt'),el('ul',{},(f.wird_entfernt||[]).map(s=>el('li',{},s))),el('h4',{},'Bleibt erhalten'),el('ul',{},(f.bleibt||[]).map(s=>el('li',{},s))),f.hinweis?el('p',{},f.hinweis):null,f.suchen?el('p',{},f.suchen.length+' zugehörige Suchen · '+(f.mit_suchen?'werden ebenfalls entfernt':'bleiben erhalten')):null,el('p',{},f.status==='vorschlag'?'Die vorgeschlagene Zuordnung wird verworfen. Die Suchen bleiben erhalten.':'30 Tage im Papierkorb wiederherstellbar.'));}
async function tripBookFromSearch(t,searchId){
 const live=viewGuard();try{const r=await tripCall('unterkunft_etappen_lesen');if(!live())return;const e=r.etappen?.find(e=>e.suchen?.some(s=>s.id===searchId));if(!e){const {body}=tripDialog('Etappe zuordnen');body.append(el('p',{},'Ordne diese Suche zunächst einer Etappe zu.'),el('a',{href:'#/reisen'},'Reisen öffnen und Suche zuordnen'));return;}tripBook(t.treffer_id,e,t,searchId);}catch(e){if(live())toast(e.message,true);}
}

function tripExternalBooking(etappe,onSaved){
 const existing=!!tripId(etappe.id),{d,body,status,close}=tripDialog(existing?'Woanders gebucht':'Aufenthalt nachtragen'),form=el('form'),fields={};let pending=false;
 body.append(el('p',{},'Trage eine bereits abgeschlossene Buchung ein. Auch vergangene Aufenthalte sind möglich.'));
 if(existing)body.append(el('p',{},etappe.ziel+' · '+fmtDate(etappe.anreise)+'–'+fmtDate(etappe.abreise)));
 const specs=[...(!existing?[['ziel','Ort / Stadt','text',true],['anreise','Anreise','date',true],['abreise','Abreise','date',true]]:[]),['name','Unterkunft','text',true],['anbieter','Anbieter','text',false],['preis_gesamt_eur','Gesamtpreis (€)','number',false],['link','Unterkunftslink','url',false],['storno_text','Stornobedingungen','text',false],['storno_kostenlos_bis','Kostenlos stornierbar bis','date',false],['notiz','Notiz','text',false]];
 for(const [key,label,type,required] of specs){const input=el('input',{type,required,min:type==='number'?0:null,step:type==='number'?'0.01':null});fields[key]=input;form.append(el('label',{},label,input));}
 form.append(el('p',{class:'small'},'Storno-Erinnerung nur mit konkretem Datum. Den Zeitpunkt laut Buchungsbestätigung beachten.'));
 const confirm=el('input',{type:'checkbox',required:existing});if(existing)form.append(el('label',{},confirm,etappe.status==='gebucht'?' Vorhandenen Buchungsvermerk durch diese Buchung ersetzen.':' Diese Etappe und diese Reisetage als gebucht bestätigen.'));
 const save=el('button',{type:'submit',class:'primary'},'Aufenthalt speichern');form.append(save);body.append(form);
 form.onsubmit=async event=>{event.preventDefault();if(pending||!form.reportValidity())return;
  if(!fields.name.value.trim()||!existing&&!fields.ziel.value.trim()){status.textContent='Bitte Unterkunft und Ort angeben.';return;}
  if(!existing&&fields.abreise.value<=fields.anreise.value){status.textContent='Die Abreise muss nach der Anreise liegen.';return;}
  const booking={};for(const [key,input] of Object.entries(fields)){if(['ziel','anreise','abreise'].includes(key)||!input.value.trim())continue;booking[key]=key==='preis_gesamt_eur'?Number(input.value):input.value.trim();}
  if(booking.link){try{const u=new URL(booking.link);if(u.protocol!=='https:'||u.username||u.password)throw Error();}catch{status.textContent='Bitte einen HTTPS-Unterkunftslink ohne Zugangsdaten eingeben.';return;}}
  const payload={status:'gebucht',buchung:booking,...(existing?{id:etappe.id,version:etappe.version}:{reise_id:etappe.reise_id,ziel:fields.ziel.value.trim(),anreise:fields.anreise.value,abreise:fields.abreise.value})};
  pending=true;form.querySelectorAll('input,button').forEach(n=>n.disabled=true);close.disabled=true;
  try{const r=await tripCall('unterkunft_etappe_speichern',payload);if(!tripId(r.etappe?.id)||existing&&r.etappe.id!==etappe.id||r.etappe.status!=='gebucht')throw Error('Buchungsvermerk nicht eindeutig bestätigt.');d.close();await onSaved();}
  catch(e){status.textContent=e.message+' Bitte Reisen neu lesen, bevor du erneut speicherst. Dein Entwurf bleibt erhalten.';}
  finally{pending=false;close.disabled=false;}
 };d.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
}
