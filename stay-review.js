/* Wunsch 71: gerätebezogene Anzeige, Galerie und persönliche Endrunde. */
'use strict';
function sucheBettenDeutsch(value) {
  return String(value || '').replace(/\bBedroom\b/gi,'Schlafzimmer').replace(/\bLiving room\b/gi,'Wohnzimmer').replace(/\bsofa beds?\b/gi, 'Schlafsofa').replace(/\b(?:double|full) beds?\b/gi, 'Doppelbett')
    .replace(/\b(?:single|twin) beds?\b/gi, 'Einzelbett').replace(/\bqueen beds?\b/gi, 'Queensize-Bett')
    .replace(/\bking beds?\b/gi, 'Kingsize-Bett').replace(/\bbunk beds?\b/gi, 'Etagenbett')
    .replace(/\bfuton beds?\b/gi, 'Futon').replace(/\bfutons?\b/gi, 'Futon').replace(/\btwin\b/gi,'Einzelbett').replace(/\bdouble\b/gi,'Doppelbett').replace(/\band\b/gi, 'und');
}
function sucheWegText(t) {
  const min = sucheZahl(t.gehzeit_min), rawStation = typeof t.station_name === 'string' && t.station_name.trim();
  const station = rawStation && !/^(station|bahnhof|unknown|unbekannt)$/i.test(rawStation) ? rawStation : null;
  if (min === null || min < 0) return station ? 'Fußweg zu ' + station + ' unbekannt' : 'Fußweg und Station unbekannt';
  const rounded = Math.round(min), time = rounded >= 60 ? Math.floor(rounded / 60) + ' Std. ' + rounded % 60 + ' Min.' : rounded + ' Min.';
  return (t.gehzeit_art === 'geschaetzt' ? 'ca. ' : '') + time + ' zu Fuß · ' + (station || 'Zielstation nicht angegeben') +
    (t.gehzeit_art === 'geschaetzt' ? ' (geschätzt)' : !['route', 'ors'].includes(t.gehzeit_art) ? ' (Berechnung unbekannt)' : '');
}
function sucheAnbieterLink(t) {
  const original = sucheLink(t.angebot?.link);
  if (!original) return null;
  const u = new URL(original), id = u.searchParams.get('f_no');
  // Rakuten API redirects may lead to login. The hotel ID identifies the public overview, not an offer.
  if (['img.travel.rakuten.co.jp', 'hotel.travel.rakuten.co.jp'].includes(u.hostname) && /^[1-9]\d*$/.test(id || '')) {
    return { url: 'https://travel.rakuten.co.jp/HOTEL/' + id + '/' + id + '.html', label: 'Hotel bei Rakuten ansehen ↗', overview: true };
  }
  return { url: original, label: 'Bei ' + (t.angebot?.anbieter || SUCHE_QUELLEN[t.quelle] || 'Anbieter') + ' ansehen ↗', overview: false };
}
const STAY_FIELDS = {
  preis: 'Preis gesamt', nacht: 'Preis/Nacht', tarif: 'Bester Tarif', vergleich: 'Preis ggü. gleicher Art', storno: 'Storno',
  art: 'Unterkunftsart', schlafzimmer: 'Schlafzimmer', betten: 'Betten/Schlafplätze', m2: 'Zimmergröße m²', balkon: 'Balkon', kueche: 'Küche', waschmaschine: 'Waschmaschine', raucher: 'Raucher',
  gaestenote: 'Gästenote', bewertungen: 'Bewertungen',
  entfernung: 'Entfernung zum Ziel', gehzeit: 'Gehzeit zur Station', viertel: 'Viertel',
  anbieter: 'Quelle', datenlage: 'Datenlage'
};
// W98b: Themen für Einstellung und Info-Box – immer dieselbe Reihenfolge und Struktur (Sebastian 20.10.).
const STAY_THEMEN = [
  ['Preis & Buchung', ['nacht','preis','tarif','vergleich','storno']],
  ['Wohnen', ['art','schlafzimmer','betten','m2','balkon','kueche','waschmaschine','raucher']],
  ['Bewertungen', ['gaestenote','bewertungen']],
  ['Lage', ['entfernung','gehzeit','viertel']],
  ['Quelle', ['anbieter','datenlage']],
];
const STAY_IMMER = ['preis','nacht']; // Name und Preis stehen immer auf der Karte
const STAY_DIREKT_MAX = 6;
const STAY_DEFAULT_KARTEN = { direkt: ['schlafzimmer','betten','m2','gaestenote','storno','gehzeit'], aus: ['datenlage','raucher'] };
const STAY_DEFAULT_FIELDS = STAY_DEFAULT_KARTEN.direkt; // ältere Aufrufer
const STAY_WAEHLBAR = Object.keys(STAY_FIELDS).filter(k => !STAY_IMMER.includes(k));
function stayRead(key, fallback) { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } }
function stayWrite(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; } }
let stayKartenMemory = null;
// Einstellung für Liste, Karte und Durchsehen: je Angabe Direkt (max. 6, mit Reihenfolge) / Details (Info-Box) / Aus.
function stayKarten() {
  const ok = v => v && Array.isArray(v.direkt) && Array.isArray(v.aus) && v.direkt.length <= STAY_DIREKT_MAX && [...v.direkt, ...v.aus].every(k => STAY_WAEHLBAR.includes(k)) && new Set([...v.direkt, ...v.aus]).size === v.direkt.length + v.aus.length;
  let v = stayKartenMemory ?? stayRead('ks_karten', null);
  if (!ok(v)) { // Übernahme der früheren Auswahl (ks_anzeige), sonst Standard
    const alt = stayRead('ks_anzeige', null);
    v = Array.isArray(alt) ? { direkt: alt.filter(k => STAY_WAEHLBAR.includes(k)).slice(0, STAY_DIREKT_MAX), aus: [...STAY_DEFAULT_KARTEN.aus].filter(k => !alt.includes(k)) } : null;
    if (!ok(v)) v = { direkt: [...STAY_DEFAULT_KARTEN.direkt], aus: [...STAY_DEFAULT_KARTEN.aus] };
  }
  return { direkt: [...v.direkt], aus: [...v.aus] };
}
function stayStufe(key, karten = stayKarten()) { return STAY_IMMER.includes(key) ? 'immer' : karten.direkt.includes(key) ? 'direkt' : karten.aus.includes(key) ? 'aus' : 'details'; }
function stayFields() { return [...STAY_IMMER, ...stayKarten().direkt]; }
function stayMove(list, from, to) { const copy=[...list]; if(from<0 || to<0 || from>=copy.length || to>=copy.length) return copy; copy.splice(to,0,copy.splice(from,1)[0]); return copy; }
function viewAnzeige() {
  setChrome('Anzeige', {back:true});
  let karten=stayKarten(), drag=null;
  const box=el('section',{class:'card display-settings'}), status=el('p',{role:'status'});
  function save() { stayKartenMemory={direkt:[...karten.direkt],aus:[...karten.aus]}; status.textContent=stayWrite('ks_karten',karten) ? 'Auf diesem Gerät gespeichert.' : 'Gerätespeicher nicht verfügbar. Auswahl gilt bis zum Neuladen.'; draw(); }
  function setze(key, stufe) {
    karten.direkt=karten.direkt.filter(k=>k!==key); karten.aus=karten.aus.filter(k=>k!==key);
    if(stufe==='direkt'){ if(karten.direkt.length>=STAY_DIREKT_MAX){status.textContent='Höchstens '+STAY_DIREKT_MAX+' Schnell-Infos. Erst eine andere auf „Details“ stellen.';return draw();} karten.direkt.push(key); }
    if(stufe==='aus') karten.aus.push(key);
    save();
  }
  function move(i,j) {karten.direkt=stayMove(karten.direkt,i,j);save();}
  function draw() {
    box.replaceChildren(el('h2',{},'Anzeige'),
      el('h3',{},'Karten: Liste, Karte und Durchsehen'),
      el('p',{class:'small'},'Name und Preis (gesamt und pro Nacht) stehen immer da. Direkt = Schnell-Info auf der Karte (höchstens '+STAY_DIREKT_MAX+'), Details = in der Info-Box, Aus = nicht anzeigen.'),
      el('p',{},karten.direkt.length+' / '+STAY_DIREKT_MAX+' Schnell-Infos'),
      el('ol',{class:'display-order','aria-label':'Reihenfolge der Schnell-Infos'},karten.direkt.map((key,i)=>el('li',{draggable:'true','data-field':key,
        ondragstart:e=>{drag=i;e.dataTransfer.setData('text/plain',key);},ondragover:e=>e.preventDefault(),ondrop:e=>{e.preventDefault();if(drag!==null)move(drag,i);drag=null;},ondragend:()=>{drag=null;}},
        STAY_FIELDS[key],el('button',{type:'button',disabled:i===0,'aria-label':STAY_FIELDS[key]+' nach oben',onclick:()=>move(i,i-1)},'↑'),
        el('button',{type:'button',disabled:i===karten.direkt.length-1,'aria-label':STAY_FIELDS[key]+' nach unten',onclick:()=>move(i,i+1)},'↓')))),
      ...STAY_THEMEN.map(([thema,keys])=>el('fieldset',{class:'display-thema'},el('legend',{},thema),...keys.filter(k=>STAY_WAEHLBAR.includes(k)).map(key=>{
        const stufe=stayStufe(key,karten);
        return el('div',{class:'display-row','data-field':key},el('span',{},STAY_FIELDS[key]),el('div',{class:'display-stufen',role:'radiogroup','aria-label':STAY_FIELDS[key]},
          ...[['direkt','Direkt'],['details','Details'],['aus','Aus']].map(([s,label])=>el('button',{type:'button',role:'radio','aria-checked':String(stufe===s),'aria-label':STAY_FIELDS[key]+': '+label,
            disabled:s==='direkt'&&stufe!=='direkt'&&karten.direkt.length>=STAY_DIREKT_MAX,onclick:()=>{if(stufe!==s)setze(key,s);}},label))));
      }))),
      el('button',{type:'button',onclick:()=>{karten={direkt:[...STAY_DEFAULT_KARTEN.direkt],aus:[...STAY_DEFAULT_KARTEN.aus]};save();}},'Standard wiederherstellen'),status);
  }
  // Tabelle am Rechner: eigene Spalten, dieselbe Einstellung wie der Knopf „Spalten“ in der Tabelle
  const tabBox=el('section',{class:'card display-settings display-tabelle'}), tabStatus=el('p',{role:'status'});
  function tabSave(n){tabStatus.textContent=stayWrite('ks_tabelle_spalten',n)?'Auf diesem Gerät gespeichert.':'Gerätespeicher nicht verfügbar.';tabDraw();}
  function tabDraw(){
    const spalten=stayDeskSpalten();
    tabBox.replaceChildren(el('h2',{},'Tabelle (Rechner)'),el('p',{class:'small'},'Eigene Spalten, unabhängig von den Karten. Gleich wie der Knopf „Spalten“ in der Tabelle.'),
      el('ol',{class:'display-order'},spalten.map((k,i)=>{const s=STAY_DESK_SPALTEN.find(x=>x.key===k);return el('li',{'data-spalte':k},el('label',{},el('input',{type:'checkbox',checked:true,'aria-label':'Tabelle: '+s.label,onchange:()=>tabSave(spalten.filter(x=>x!==k))}),s.label),
        el('button',{type:'button',disabled:i===0,'aria-label':'Tabelle: '+s.label+' nach vorne',onclick:()=>tabSave(stayMove(spalten,i,i-1))},'↑'),
        el('button',{type:'button',disabled:i===spalten.length-1,'aria-label':'Tabelle: '+s.label+' nach hinten',onclick:()=>tabSave(stayMove(spalten,i,i+1))},'↓'));})),
      el('div',{class:'display-options'},STAY_DESK_SPALTEN.filter(s=>!spalten.includes(s.key)).map(s=>el('label',{},el('input',{type:'checkbox','aria-label':'Tabelle: '+s.label,onchange:()=>tabSave([...spalten,s.key])}),s.label))),
      el('button',{type:'button',onclick:()=>tabSave([...STAY_DESK_STANDARD])},'Tabelle: Standard'),tabStatus);
  }
  main.replaceChildren(box,tabBox);draw();tabDraw();
}
let stayVergleichFn = null; // wird von der Ergebnisansicht für die geladenen Treffer gesetzt (Preis ggü. gleicher Art)
function stayFieldValue(t,key,trip={}) {
  const a=t.angebot||{}, k=sucheAngebotsKategorie(t), room=sucheZimmerKurz(t), n=sucheZahl;
  const category=k?.konflikt ? null : k;
  const yes=v=>v===true||v==='ja'?'ja':v===false||v==='nein'?'nein':null;
  switch(key) {
    case 'preis': return n(a.preis_gesamt_eur);
    case 'nacht': { const nights=(Date.parse(trip.abreise || t._trip?.abreise)-Date.parse(trip.anreise || t._trip?.anreise))/86400000; return n(a.preis_nacht_eur) ?? (n(a.preis_gesamt_eur)!==null&&nights>0?a.preis_gesamt_eur/nights:null); }
    case 'tarif': { const g=typeof stayBesterTarif==='function'?stayBesterTarif(t):null; return g?n(g.gesamt_eur):null; }
    case 'vergleich': { const x=stayVergleichFn?stayVergleichFn(t):null; return x?x.label:null; }
    case 'gaestenote': return n(t.note_geeicht);
    case 'bewertungen': return n(t.bewertungen);
    case 'm2': return n(category?.m2);
    case 'schlafzimmer': return room.schlafzimmer;
    case 'betten': return (room.typen ? sucheBettenDeutsch(room.typen) : null) ?? (room.anzahl!==null?room.anzahl+' Betten':null);
    case 'art': return typeof stayTyp==='function'?stayTyp(t):null;
    case 'balkon': return yes(category?.balkon) ?? (t.detail?.merkmale?.balkon?'ja':null);
    case 'kueche': return t.detail?.merkmale?.kueche?'ja':null;
    case 'waschmaschine': return t.detail?.merkmale?.waschmaschine?'ja':null;
    case 'raucher': return yes(category?.raucher ?? t.raucher);
    case 'storno': { if(typeof stayStorno==='function'){const s=stayStorno(t,trip.anreise?trip:(t._trip||trip));if(s.tage!==null)return 'kostenlos bis '+s.tage+' Tage vor Anreise';if(s.nein)return 'nicht kostenlos';} return typeof a.storno==='string' && a.storno.trim() && !/^(unbekannt|nicht kostenlos\/unklar)$/.test(a.storno.trim()) ? a.storno : null; }
    case 'entfernung': return n(t.luftlinie_ziel_m)===null?null:Math.round(t.luftlinie_ziel_m/100)/10;
    case 'gehzeit': return n(t.gehzeit_min);
    case 'viertel': return t.zone?.name || null;
    case 'anbieter': return SUCHE_QUELLEN[t.quelle] || t.quelle || null;
    case 'datenlage': return sucheDatenlage(t);
    default: return null;
  }
}
function stayField(t,key,trip) {
  const value=stayFieldValue(t,key,trip), box=el('span');
  if(value===null) box.append('–');
  else if(['preis','nacht','tarif'].includes(key)) box.append((key!=='tarif'&&t.angebot?.preis_art==='geschaetzt'?'ca. ':'')+sucheEuro(value));
  else if(key==='gaestenote') box.append(Number(value).toLocaleString('de-DE',{maximumFractionDigits:2})+' / 10');
  else if(key==='gehzeit') box.append(sucheWegText(t));
  else if(key==='entfernung') box.append(Number(value).toLocaleString('de-DE')+' km');
  else box.append((key==='m2'?Number(value).toLocaleString('de-DE'):String(value))+(key==='m2'?' m²':key==='datenlage'?' %':''));
  if(key==='gaestenote') box.append(el('small',{}, value===null?'Eichung nicht verfügbar.':'geeicht'));
  if(key==='gehzeit' && value!==null) box.append(el('small',{},t.station_name?'Zur Station '+t.station_name:'Ziel nicht benannt'),el('small',{},t.gehzeit_art==='geschaetzt'?'geschätzt':['route','ors'].includes(t.gehzeit_art)?'berechneter Fußweg':'Art unbekannt'));
  return box;
}
function stayInfo(t,trip) {return el('dl',{class:'stay-info'},stayFields().flatMap(key=>[el('dt',{},STAY_FIELDS[key]),el('dd',{'data-field':key},stayField(t,key,trip))]));}
// Anzeige-Text einer Angabe (für Schnell-Info und Info-Box); fehlt sie: „unbekannt“.
function stayAnzeigeText(t,key,trip) {
  const value=stayFieldValue(t,key,trip);
  if(value===null) return 'unbekannt';
  if(['preis','nacht','tarif'].includes(key)) return (key!=='tarif'&&t.angebot?.preis_art==='geschaetzt'?'ca. ':'')+sucheEuro(value);
  if(key==='m2') return Number(value).toLocaleString('de-DE')+' m²';
  if(key==='datenlage') return value+' %';
  if(key==='entfernung') return Number(value).toLocaleString('de-DE')+' km';
  if(key==='gaestenote') return Number(value).toLocaleString('de-DE',{maximumFractionDigits:2})+' / 10';
  if(key==='gehzeit') return (t.gehzeit_art==='geschaetzt'?'ca. ':'')+(value>=60?Math.floor(value/60)+' Std. '+Math.round(value%60)+' Min.':Math.round(value)+' Min.')+(t.station_name?' · '+t.station_name:'');
  return String(value);
}
// Info-Box: alle „Details“-Angaben nach Themen, immer gleiche Struktur und Reihenfolge, kompakt.
function stayInfoBox(t,trip,{alle=false}={}) {
  const karten=stayKarten();
  const themen=STAY_THEMEN.map(([thema,keys])=>[thema,keys.filter(k=>alle?stayStufe(k,karten)!=='aus':stayStufe(k,karten)==='details')]).filter(([,keys])=>keys.length);
  return el('div',{class:'stay-infobox'},themen.map(([thema,keys])=>el('section',{class:'infobox-thema'},el('h4',{},thema),
    el('dl',{},keys.map(key=>el('div',{'data-field':key,class:stayFieldValue(t,key,trip)===null?'is-unbekannt':null},el('dt',{},STAY_FIELDS[key]),el('dd',{},stayAnzeigeText(t,key,trip))))))));
}
// Kurzform für die Schnell-Info-Zeile beim Durchsehen
function stayKurz(t,key,trip) {
  const v=stayFieldValue(t,key,trip); if(v===null) return null;
  const n=x=>Number(x).toLocaleString('de-DE',{maximumFractionDigits:1});
  switch(key){
    case 'schlafzimmer': return v+' Schlafzimmer'; case 'm2': return n(v)+' m²'; case 'gaestenote': return '★ '+n(v);
    case 'bewertungen': return n(v)+' Bewertungen'; case 'entfernung': return n(v)+' km zum Ziel'; case 'gehzeit': return Math.round(v)+' Min. zur Station';
    case 'storno': { const s=typeof stayStorno==='function'?stayStorno(t,trip):null; return s?.tage!=null?'Storno bis '+s.tage+' T. vor Anreise':s?.nein?'nicht kostenlos stornierbar':String(v); }
    case 'tarif': return 'bester Tarif '+sucheEuro(v); case 'vergleich': return v+' für die Art';
    case 'balkon': case 'kueche': case 'waschmaschine': case 'raucher': return v==='ja'?STAY_FIELDS[key]:null;
    default: return String(v);
  }
}
function stayReviewFields(){return stayKarten().direkt;}
// Durchsehen-Details: oben Preis + Schnell-Infos, darunter die Info-Box nach Themen.
function stayReviewInfo(t,trip) {
  const nights=(Date.parse(trip.abreise)-Date.parse(trip.anreise))/86400000;
  const labels={preis:nights>0?'Gesamt · '+nights+' Nächte':'Gesamtpreis',nacht:'Pro Nacht'};
  return el('div',{class:'review-info'},
    el('dl',{class:'review-schnell'},[...STAY_IMMER,...stayKarten().direkt].map(key=>el('div',{'data-field':key},el('dt',{},labels[key]||STAY_FIELDS[key]),el('dd',{},stayAnzeigeText(t,key,trip))))),
    stayInfoBox(t,trip));
}
function stayCardPhoto(card, gallery) {
  card.querySelector(':scope > .review-backdrop')?.remove();
  if(card.classList.contains('photo-first'))return;
  const source=gallery.querySelector('img');
  if(!source)return;
  const image=el('img',{class:'review-backdrop',alt:'','aria-hidden':'true',referrerpolicy:'no-referrer',src:source.src,onerror:()=>image.remove()});
  card.prepend(image);
}
function stayGallery(t) {
  const urls=[...new Set([...(Array.isArray(t.bilder)?t.bilder:[]),t.bild].map(v=>sucheLink(v)).filter(Boolean))].slice(0,10);
  const box=el('section',{class:'stay-gallery'+(!urls.length?' gallery-empty':''),'aria-label':'Fotogalerie'});
  if(!urls.length) {box.append(sucheFoto(t));return box;}
  let index=0,start=null;const preloaded=new Set();
  const dots=el('div',{class:'gallery-dots','aria-hidden':'true'},...urls.map(()=>el('span')));
  function preload(url){if(!url||preloaded.has(url))return;preloaded.add(url);const img=new Image();img.referrerPolicy='no-referrer';img.src=url;}
  const photo=el('div'), count=el('span',{'aria-live':'polite'});
  const prev=el('button',{type:'button','aria-label':'Vorheriges Foto',onclick:()=>show(index-1)},'‹');
  const next=el('button',{type:'button','aria-label':'Nächstes Foto',onclick:()=>show(index+1)},'›');
  function show(i) {index=Math.max(0,Math.min(urls.length-1,i));photo.replaceChildren(sucheFoto({...t,bild:urls[index]}));count.textContent=`${index+1} / ${urls.length}`;box.dataset.photo=`Foto ${index+1}/${urls.length}`;dots.querySelectorAll('span').forEach((d,n)=>d.classList.toggle('active',n===index));preload(urls[index+1]);box.onPhotoChange?.();prev.disabled=index===0;next.disabled=index===urls.length-1;const card=box.closest('.review-card');if(card)stayCardPhoto(card,box);const img=photo.querySelector('img');if(img)img.loading='eager';if(img)img.addEventListener('error',()=>{box.classList.add('gallery-empty');card?.querySelector(':scope > .review-backdrop')?.remove();});box.classList.remove('gallery-empty');}
  photo.addEventListener('pointerdown',e=>{if(start||e.isPrimary===false||e.button!==0){start=null;return;}start={id:e.pointerId,x:e.clientX,y:e.clientY};try{photo.setPointerCapture(e.pointerId);}catch{}});
  photo.addEventListener('pointerup',e=>{if(!start||start.id!==e.pointerId)return;const dx=e.clientX-start.x,dy=e.clientY-start.y;start=null;if(Math.abs(dx)>50&&Math.abs(dy)<50)show(index+(dx<0?1:-1));else if(Math.abs(dx)<12&&Math.abs(dy)<12){const rect=photo.getBoundingClientRect();show(index+(e.clientX<rect.left+rect.width/2?-1:1));}});
  photo.addEventListener('pointercancel',()=>{start=null;});
  const controls=el('div',{class:'actions gallery-controls'},urls.length>1?prev:null,count,urls.length>1?next:null);
  photo.tabIndex=0;photo.setAttribute('aria-label','Foto ansehen');photo.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();show(index+(e.key==='ArrowRight'?1:-1));}});
  const large=el('button',{type:'button',class:'photo-large',onclick:()=>{const d=el('dialog',{class:'trip-dialog photo-dialog','aria-label':'Foto groß'});d.append(el('button',{onclick:()=>d.close()},'Schließen'),sucheFoto({...t,bild:urls[index]}));main.append(d);d.addEventListener('close',()=>{d.remove();large.focus();});d.showModal();}},'Foto groß');
  box.append(photo,controls,dots,large);show(0);return box;
}
function stayEndrunde(hits,id,call,live,onSaved) {
  let order=hits.filter(t=>t.status==='favorit').sort((a,b)=>(a.eigener_rang??Infinity)-(b.eigener_rang??Infinity)||(a.bewertung?.rang??Infinity)-(b.bewertung?.rang??Infinity));
  const dialog=el('dialog',{class:'stay-candidate endrunde','aria-label':'Endrunde'}), body=el('div'), status=el('p',{role:'status'});
  let drag=null, pending=false, ranked=[], queue=[], candidate=null, position=0, low=0, high=0;
  const save=el('button',{type:'button',class:'primary',onclick:async()=>{
    if(pending||candidate||!order.length)return;pending=true;save.disabled=true;close.disabled=true;body.inert=true;status.textContent='Speichere …';
    try {const r=await call('unterkunft_eigenes_ranking_setzen',{suchauftrag_id:id,reihenfolge:order.map(t=>t.treffer_id)});if(!live())return;if(r.ok!==true)throw Error('Nicht bestätigt.');order.forEach((t,i)=>t.eigener_rang=i+1);onSaved();dialog.close();}
    catch(e){status.textContent='Rangfolge nicht bestätigt: '+e.message;}
    finally{pending=false;save.disabled=false;close.disabled=false;body.inert=false;}
  }},'Rangfolge speichern');
  const close=el('button',{type:'button',onclick:()=>dialog.close()},'Endrunde schließen');
  dialog.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
  function list() {candidate=null;save.disabled=order.length===0;body.replaceChildren(el('p',{},'Ziehe deine Favoriten in die gewünschte Reihenfolge oder nutze die Pfeile.'),el('ol',{},order.map((t,i)=>el('li',{'data-final-hit':t.treffer_id,draggable:'true',ondragstart:e=>{drag=i;e.dataTransfer.setData('text/plain',String(t.treffer_id));},ondragover:e=>e.preventDefault(),ondrop:e=>{e.preventDefault();if(drag!==null){order=stayMove(order,drag,i);list();}drag=null;},ondragend:()=>drag=null},
    el('span',{class:'final-name'},`${i+1}. ${t.name}`),el('button',{type:'button',disabled:i===0,'aria-label':t.name+' nach oben',onclick:()=>{order=stayMove(order,i,i-1);list();}},'↑'),el('button',{type:'button',disabled:i===order.length-1,'aria-label':t.name+' nach unten',onclick:()=>{order=stayMove(order,i,i+1);list();}},'↓')))),
    el('button',{type:'button',disabled:order.length<2,onclick:()=>{queue=[...order];ranked=[queue.shift()];advance();}},'Paarvergleich starten')); }
  function advance(){candidate=queue.shift();low=0;high=ranked.length;position=Math.floor((low+high)/2);if(!candidate){order=[...ranked];list();status.textContent='Paarvergleich abgeschlossen. Bitte Rangfolge speichern.';}else pair();}
  function pair(){save.disabled=true;const other=ranked[position];body.replaceChildren(el('h3',{},'A oder B?'),el('p',{},'Welche Unterkunft gefällt dir besser?'),el('div',{class:'pair-options'},[candidate,other].map(t=>el('section',{},stayGallery(t),el('h4',{},t.name),stayInfo(t),el('button',{type:'button',onclick:()=>{
    if(t===candidate)high=position;else low=position+1;
    if(low===high){ranked.splice(low,0,candidate);advance();}else{position=Math.floor((low+high)/2);pair();}
  }},t.name+' wählen')))));}
  dialog.append(el('h2',{},'Endrunde · Favoriten'),close,body,status,save);list();return dialog;
}
function stayReview({getSnapshot,getGroup=()=>null,getRows=()=>getSnapshot()?.treffer,call,live,changed,scope,onRefresh,onClose,menuItems=()=>[],isBlocked=()=>false}) {
  let pending=false, last=null, reasonFor=null, awaitingReturn=null, revision=0, gallery=null, galleryId=null, reasonsDialog=null;
  const box=el('section',{class:'stay-review'}), message=el('p',{class:'review-message',role:'status'});
  const minus=[['preis','Preis'],['zu_klein','Zu klein'],['lage','Lage'],['stil','Stil'],['betten','Betten'],['fotos','Fotos'],['laerm','Lärm'],['ausstattung','Ausstattung'],['sonstiges','Sonstiges']];
  const plus=[['plus_groesse','Größe'],['plus_lage','Lage'],['plus_stil','Stil'],['plus_preis','Preis'],['plus_ausstattung','Ausstattung'],['plus_fotos','Fotos'],['plus_betten','Betten']];
  let needsRefresh=false, activeGroup=null, restored=false, stampFresh=null, holding=false, holdTimer=null, currentId=null, lastIndex=0, nextAfterVote=null, mode=stayRead('ks_review_mode','alle');
  if(!['alle','offen','favorit'].includes(mode))mode='alle';
  const positionKey=()=>'ks_review_pos:'+(getSnapshot()?.suchauftrag?.id??'etappe');
  function savePosition(){if(currentId)stayWrite(positionKey(),currentId);}
  const judged=t=>['favorit','vielleicht','ausgeschlossen'].includes(t.status);
  const reduceMotion=()=>{try{return matchMedia('(prefers-reduced-motion: reduce)').matches;}catch{return false;}};
  const rank=(a,b)=>(b.runde||1)-(a.runde||1)||(a.bewertung?.rang??Infinity)-(b.bewertung?.rang??Infinity)||a.treffer_id-b.treffer_id;
  function currentList(keep=true){
    const all=getRows()||[], group=activeGroup;
    if(group)return all.filter(t=>t.status===group||reviewed.has(t.treffer_id)).sort(rank);
    const base=all.filter(t=>t.topf!=='ausgeschlossen'||judged(t));
    const list=mode==='offen'?base.filter(t=>!judged(t)||(t.status==='aktiv'&&t.urteil_uebernommen?.hinweis)||(keep&&t.treffer_id===currentId)):mode==='favorit'?base.filter(t=>t.status==='favorit'||(keep&&t.treffer_id===currentId)):base;
    return list.sort(rank);
  }
  function go(delta){if(holding){clearTimeout(holdTimer);holding=false;stampFresh=null;}message.textContent='';const list=currentList();if(!list.length)return;let i=list.findIndex(t=>t.treffer_id===currentId);if(i<0)i=Math.min(lastIndex,list.length-1);i=Math.max(0,Math.min(list.length-1,i+delta));currentId=list[i].treffer_id;savePosition();draw();box.querySelector('.review-swipe h3')?.focus({preventScroll:true});}
  function setMode(next){if(pending||mode===next)return;mode=next;stayWrite('ks_review_mode',mode);const list=currentList(false);if(!list.some(t=>t.treffer_id===currentId)){currentId=list[0]?.treffer_id??null;lastIndex=0;}draw();}
  const reviewed=new Set();
  let leiste=null, leisteFor=null; // W98
  async function vote(t,urteil,gruende=[],withReasons=true,restoring=false){
    if(pending||(holding&&!restoring)||needsRefresh||isBlocked())return;const focusDecision=document.activeElement?.dataset.decision;const previous={status:t.status||'aktiv',gruende:[...(t.urteil_gruende||[])],uebernommen:t.urteil_uebernommen};pending=true;revision++;draw();
    try {const daten={treffer_id:t.treffer_id,urteil,gruende};if(urteil!=='offen')daten.fakten=stayFakten(t,getSnapshot()?.suchauftrag||{}); // W98: Fakten-Schnappschuss
      const r=await call('unterkunft_durchsehen_urteil',daten);if(!live())return;
      if(r.ok!==true || r.treffer_id!==t.treffer_id || r.urteil!==urteil || r.status!==({favorit:'favorit',vielleicht:'vielleicht',weg:'ausgeschlossen',offen:'aktiv'}[urteil]))throw Error('Urteil nicht eindeutig bestätigt.');
      t.status={favorit:'favorit',vielleicht:'vielleicht',weg:'ausgeschlossen',offen:'aktiv'}[urteil];t.urteil_gruende=gruende;
      if(restoring){reviewed.delete(t.treffer_id);t.urteil_uebernommen=previousRestore;last=null;reasonFor=null;}else if(urteil==='offen'){t.urteil_uebernommen=null;last=null;reasonFor=null;}else {if(withReasons){last={t,previous};if(activeGroup)reviewed.add(t.treffer_id);}reasonFor=withReasons?{t,urteil,gruende}:null;}
      if(reasonsDialog){reasonsDialog.close();reasonsDialog.remove();reasonsDialog=null;}
      awaitingReturn=null;message.textContent=restoring||urteil==='offen'?'Entscheidung zurückgenommen.':({favorit:'♥ Als Favorit gemerkt.',vielleicht:'≈ Als Na ja gemerkt.',weg:'× Aussortiert.'})[urteil];
      if(!restoring&&urteil!=='offen'){stampFresh=t.treffer_id;const target=nextAfterVote;if(target){holding=true;clearTimeout(holdTimer);holdTimer=setTimeout(()=>{holding=false;stampFresh=null;if(!live())return;currentId=target;savePosition();draw();box.querySelector('.review-swipe h3')?.focus({preventScroll:true});},reduceMotion()?250:700);}}nextAfterVote=null;
    }catch(e){needsRefresh=true;if(reasonsDialog){reasonsDialog.close();reasonsDialog.remove();reasonsDialog=null;}message.textContent='Speichern nicht bestätigt: '+e.message+' Bitte aktualisieren, bevor du erneut entscheidest.';}
    finally{pending=false;revision++;if(live()){changed(t);draw();if(focusDecision)box.querySelector('.review-swipe h3')?.focus({preventScroll:true});}}
  }
  let previousRestore=null;
  function undoVote(){if(!last)return;const {t,previous}=last;currentId=t.treffer_id;savePosition();previousRestore=previous.uebernommen;void vote(t,({aktiv:'offen',favorit:'favorit',vielleicht:'vielleicht',ausgeschlossen:'weg'})[previous.status]||'offen',previous.gruende,false,true);}
  function buttons(t){const current={favorit:'favorit',vielleicht:'vielleicht',ausgeschlossen:'weg'}[t.status]||null;return el('div',{class:'actions review-actions'},[['weg','Weg'],['vielleicht','Na ja'],['favorit','Favorit']].map(([key,label])=>el('button',{type:'button',class:'decision-'+key,'aria-label':current===key?label+' zurücknehmen':label,'aria-pressed':String(current===key),'data-decision':key,disabled:pending||holding||needsRefresh||isBlocked(),onclick:()=>{const list=currentList();const i=list.findIndex(x=>x.treffer_id===t.treffer_id);nextAfterVote=current===key?null:(list[i+1]?.treffer_id??(mode==='offen'&&!activeGroup?list.find(x=>x.treffer_id!==t.treffer_id)?.treffer_id??-1:null));void vote(t,current===key?'offen':key);}},el('span',{'aria-hidden':'true'},({weg:'×',vielleicht:'≈',favorit:'♥'})[key]+' '),label)));}
  function openReasons(){
    if(!reasonFor||pending||needsRefresh||isBlocked())return;
    const r=reasonFor, dialog=el('dialog',{class:'stay-candidate review-reasons','aria-label':'Gründe ergänzen'});
    reasonsDialog=dialog;
    const close=el('button',{type:'button',onclick:()=>dialog.close()},'Schließen');
    const save=el('button',{type:'button',class:'primary',onclick:()=>{dialog.querySelectorAll('button').forEach(b=>b.disabled=true);void vote(r.t,r.urteil,r.gruende,false);}},'Gründe speichern');
    dialog.append(el('h2',{},'Gründe ergänzen'),el('p',{},r.t.name+' · '+({favorit:'Favorit',weg:'Weg',vielleicht:'Na ja'}[r.urteil])),
      el('p',{class:'small'},'Optional. Deine Entscheidung ist bereits gespeichert.'),
      el('div',{class:'actions'},(r.urteil==='favorit'?plus:minus).map(([key,label])=>el('button',{type:'button','aria-pressed':r.gruende.includes(key),onclick:e=>{r.gruende=r.gruende.includes(key)?r.gruende.filter(k=>k!==key):[...r.gruende,key];e.currentTarget.setAttribute('aria-pressed',String(r.gruende.includes(key)));}},label))),
      el('div',{class:'actions'},close,save));
    dialog.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
    dialog.addEventListener('close',()=>{dialog.remove();if(reasonsDialog===dialog)reasonsDialog=null;box.querySelector('.review-reason-open')?.focus({preventScroll:true});});
    scope.append(dialog);dialog.showModal();
  }
  function draw(){
    const snapshot=getSnapshot();if(!snapshot)return;
    const group=getGroup();if(group!==activeGroup){activeGroup=group;reviewed.clear();last=null;reasonFor=null;currentId=null;}
    if(!restored&&!group){restored=true;const saved=stayRead(positionKey(),null);if(Number.isSafeInteger(saved))currentId=saved;}
    const all=getRows()||[], list=currentList();
    if(!list.some(t=>t.treffer_id===currentId)&&lastIndex===0){const open=list.find(t=>!judged(t)||(t.status==='aktiv'&&t.urteil_uebernommen?.hinweis));if(open)currentId=open.treffer_id;}
    let index=list.findIndex(t=>t.treffer_id===currentId);
    if(index<0){index=Math.min(lastIndex,Math.max(0,list.length-1));if(!pending)currentId=list[index]?.treffer_id??null;}
    if(!pending||list[index]?.treffer_id===currentId)lastIndex=index;const t=list[index]||null;
    if(t&&group)reviewed.add(t.treffer_id);
    const base=all.filter(x=>x.topf!=='ausgeschlossen'||judged(x)), counts={alle:base.length,offen:base.filter(x=>!judged(x)).length,favorit:base.filter(x=>x.status==='favorit').length};
    const progress=el('span',{class:'review-position','aria-live':'polite'});
    const prevHit=el('button',{type:'button',class:'review-nav','aria-label':'Vorherige Unterkunft',disabled:pending||index<=0,onclick:()=>go(-1)},'‹');
    const nextHit=el('button',{type:'button',class:'review-nav','aria-label':'Nächste Unterkunft',disabled:pending||index>=list.length-1,onclick:()=>go(1)},'›');
    const undo=el('button',{type:'button',class:'review-undo',disabled:!last||pending||needsRefresh||isBlocked(),'aria-label':'Letzte Entscheidung rückgängig',onclick:undoVote},'↶');
    const menu=el('details',{class:'review-menu'},el('summary',{'aria-label':'Durchsehen-Menü'},'•••'),el('div',{class:'review-menu-panel'},...menuItems(),el('p',{class:'review-progress'},`${counts.offen} noch offen · ${all.filter(judged).length} bewertet`),el('button',{type:'button',class:'review-reason-open',disabled:!reasonFor||pending||needsRefresh||isBlocked(),onclick:openReasons},'Gründe ergänzen')));
    const header=el('header',{class:'review-overlay-header'},el('button',{type:'button',class:'review-back','aria-label':'Zur Übersicht',disabled:pending,onclick:()=>onClose(t)},'←'),prevHit,progress,nextHit,undo,menu);
    const modes=group?null:el('div',{class:'review-modes',role:'group','aria-label':'Welche Unterkünfte'},[['alle','Alle'],['offen','Noch offen'],['favorit','♥ Favoriten']].map(([key,label])=>el('button',{type:'button','aria-pressed':String(mode===key),disabled:pending,onclick:()=>setMode(key)},`${label} ${counts[key]}`)));
    box.replaceChildren(message);
    if(pending)message.textContent='Speichere …';
    if((needsRefresh||isBlocked())&&!pending&&onRefresh)box.append(el('button',{type:'button',class:'review-reload',onclick:onRefresh},'Aktualisieren'));
    if(!t){progress.textContent=mode==='offen'?'Alles bewertet':'Keine Unterkunft';const empty=el('article',{class:'review-card photo-first review-empty'},header,modes,el('div',{class:'review-done'},el('h3',{},mode==='offen'?'Alle Unterkünfte bewertet.':mode==='favorit'?'Noch keine Favoriten.':'Keine Unterkünfte in dieser Auswahl.'),el('p',{},mode==='favorit'?'Markiere beim Durchsehen Unterkünfte mit ♥.':'In der Endrunde kannst du deine Favoriten vergleichen.'),mode!=='alle'&&!group?el('button',{type:'button',onclick:()=>setMode('alle')},'Alle ansehen'):null));box.append(empty);return;}
    savePosition();
    if(galleryId!==t.treffer_id){galleryId=t.treffer_id;gallery=stayGallery(t);}
    const article=el('article',{class:'review-card photo-first','data-review-hit':t.treffer_id});
    menu.querySelector('.review-menu-panel').append(el('button',{type:'button',onclick:event=>{const trigger=event.currentTarget;gallery.querySelector('.photo-large')?.click();const dialog=main.querySelector('.photo-dialog');dialog?.addEventListener('close',()=>trigger.focus({preventScroll:true}),{once:true});}},'Foto groß'));
    gallery.onPhotoChange=()=>{progress.replaceChildren(`${index+1} / ${list.length}`,el('span',{class:'sr-only'},` · Unterkunft ${index+1}/${list.length} · ${gallery.dataset.photo||'Kein Foto'}`));};gallery.onPhotoChange();
    for(const n of [list[index+1],list[index-1]]){const url=sucheLink(n?.bilder?.[0]||n?.bild);if(url){const img=new Image();img.referrerPolicy='no-referrer';img.src=url;}}
    const content=el('div',{class:'review-content',tabindex:0,'aria-label':'Unterkunft ansehen'},gallery);
    const price=t.currentOfferUnavailable?el('span',{},'Preis nicht bestätigt'):el('span',{},stayField(t,'preis',snapshot.suchauftrag),' gesamt · ',stayField(t,'nacht',snapshot.suchauftrag),' / Nacht');
    const wohnform=sucheWohnform(t);
    // W98b: Schnell-Infos = die bis zu 6 „Direkt“-Angaben aus der Einstellung „Anzeige“ (gleich wie Liste und Karte)
    const facts=[wohnform?wohnform.text+(wohnform.grund?' – '+wohnform.grund:''):null,...stayKarten().direkt.filter(k=>!(wohnform&&k==='schlafzimmer')).map(k=>stayKurz(t,k,snapshot.suchauftrag))].filter(Boolean);
    const verdict={favorit:'♥ Favorit',vielleicht:'≈ Na ja',ausgeschlossen:'× Weg'}[t.status];
    const swipe=el('div',{class:'review-swipe'},el('div',{class:'review-title'},refreshIsNew(t,snapshot.suchauftrag.id)?el('span',{class:'pill'},'NEU'):null,verdict?el('span',{class:'review-verdict verdict-'+t.status},verdict):null,el('h3',{tabindex:-1},t.name)),el('p',{class:'review-price'},price),el('p',{class:'review-bedroom'},facts.length?facts.join(' · '):'Angaben noch unbekannt'));
    let point=null, swiped=false;
    swipe.addEventListener('pointerdown',e=>{if(point){point=null;return;}if(e.isPrimary===false || e.button!==0 || e.target.closest('button,a') || document.querySelector('dialog[open]'))return;point={id:e.pointerId,x:e.clientX,y:e.clientY};try{swipe.setPointerCapture?.(e.pointerId);}catch{/* Synthetic events may lack an active pointer. */}});
    swipe.addEventListener('pointercancel',()=>point=null);
    swipe.addEventListener('pointerup',e=>{if(!point||point.id!==e.pointerId)return;const dx=e.clientX-point.x,dy=e.clientY-point.y;point=null;if(Math.max(Math.abs(dx),Math.abs(dy))<60)return;if(Math.abs(dx)>Math.abs(dy)*1.3){swiped=true;go(dx<0?1:-1);}});
    swipe.addEventListener('click',e=>{if(swiped){e.preventDefault();e.stopPropagation();swiped=false;}},true);
    const warnings=[...(t.currentOfferUnavailable?['Für aktuelle Tage nicht gefunden']:[]),...(t.urteil_uebernommen?.hinweis?['Jetzt günstiger · '+t.urteil_uebernommen.hinweis]:[]),...sucheWarnungen(t).map(w=>SUCHE_WARNUNGEN[w]||w),...['m2','schlafzimmer','gehzeit'].filter(k=>stayFieldValue(t,k,snapshot.suchauftrag)===null).map(k=>({m2:'Fläche: unbekannt',schlafzimmer:'Schlafzimmer: unbekannt',gehzeit:'Station: unbekannt'})[k])];
    if(warnings.length)swipe.append(el('p',{class:'review-warning'},'⚠ '+warnings[0]));
    const provider=sucheAnbieterLink(t), url=provider?.url;
    content.append(swipe,el('div',{class:'review-links'},url?el('a',{href:url,target:'_blank',rel:'noopener noreferrer',onclick:()=>{awaitingReturn=t.treffer_id;}},provider.label):null,
      el('button',{type:'button',onclick:event=>{const trigger=event.currentTarget,dialog=sucheKandidat(t,snapshot.suchauftrag.status==='fertig',snapshot.suchauftrag.id);dialog.append(SUCHE_SCORE_AN?el('p',{class:'review-score'},`Passung ${t.bewertung?.score??'–'}/100`):'',stayReviewInfo(t,snapshot.suchauftrag),el('section',{'aria-label':'Offene Angaben'},warnings.map(w=>el('p',{},w))));scope.append(dialog);dialog.addEventListener('close',()=>{dialog.remove();if(trigger.isConnected)trigger.focus({preventScroll:true});});dialog.showModal();}},'Details')));
    if(awaitingReturn===t.treffer_id)content.append(el('p',{role:'status'},'Und? Wie gefällt dir die Unterkunft?'));
    gallery.querySelector(':scope > .review-modes')?.remove();if(modes)gallery.append(modes);gallery.querySelector(':scope > .review-stamp')?.remove();if(judged(t))gallery.append(el('span',{class:'review-stamp stamp-'+t.status+(stampFresh===t.treffer_id?' is-fresh':''),'aria-hidden':'true'},{favorit:'♥ Favorit',vielleicht:'≈ Na ja',ausgeschlossen:'× Weg'}[t.status]));article.append(header,content,buttons(t));stayCardPhoto(article,gallery);box.append(article);
    // W98: Gründe-Leiste nach dem Urteil – bleibt stehen, während schon die nächste Unterkunft erscheint; ein Tipp genügt.
    if(reasonFor&&reasonFor.urteil!=='offen'&&!isBlocked()){
      if(leisteFor!==reasonFor){leisteFor=reasonFor;leiste=stayGrundLeiste(reasonFor,{call,live,trip:snapshot.suchauftrag,onDone:()=>{reasonFor=null;leisteFor=null;leiste=null;draw();}});}
      const active=leiste.contains(document.activeElement)?document.activeElement:null, pos=active?.selectionStart;
      box.append(leiste);
      if(active){active.focus({preventScroll:true});try{if(pos!=null)active.setSelectionRange(pos,pos);}catch{/* kein Textfeld */}}
    }
    article.addEventListener('keydown',e=>{if(e.target.closest('input,select,textarea,.stay-gallery'))return;if(e.key==='ArrowRight'||e.key==='ArrowLeft'){e.preventDefault();go(e.key==='ArrowRight'?1:-1);}});
  }
  const returned=()=>{if(!document.hidden && awaitingReturn && live())draw();};document.addEventListener('visibilitychange',returned);
  return {node:box,draw,get currentId(){return currentId;},show(id){currentId=id;savePosition();},get revision(){return revision;},get pending(){return pending;},get blocked(){return needsRefresh;},refreshed(){if(!pending){needsRefresh=false;last=null;reasonFor=null;}},dispose(){clearTimeout(holdTimer);reasonsDialog?.close();reasonsDialog?.remove();document.removeEventListener('visibilitychange',returned);}};
}
function stayConfigureTable(wrapper,items,sort,onSort,trip,select) {
  const table=wrapper.querySelector('table'), head=table.tHead.rows[0], fields=stayFields();
  const heading=(key,label)=>el('th',{scope:'col','aria-sort':sort.key===key?sort.direction===1?'ascending':'descending':'none'},el('button',{type:'button','data-sort':key,onclick:()=>onSort(key)},label));
  head.replaceChildren(heading('name','Unterkunft'),...fields.map(key=>heading(key,STAY_FIELDS[key])),el('th',{scope:'col'},'Details'));
  for(const t of items){const row=wrapper.querySelector(`tr[data-hit="${t.treffer_id}"]`), identity=row.cells[0], detail=row.lastElementChild;
    if(refreshIsNew(t,trip.id))identity.append(el('span',{class:'pill'},'NEU'));
    const scoreBox=el('div',{class:'small hit-score'},(trip.status==='fertig' && ['A','B'].includes(sucheGruppe(t))?'Passung: ':'Vorläufige Passung: ')+(sucheZahl(t.bewertung?.score)??'–')+'/100');if(SUCHE_SCORE_AN)identity.append(scoreBox);
    const wohnform=sucheWohnform(t);if(wohnform)identity.append(el('p',{class:'small hit-wohnform'},wohnform.text,wohnform.grund?el('span',{class:'wo-grund'},' – '+wohnform.grund):null)); // W96
    if(t.eigener_rang)identity.append(el('p',{class:'small'},'Dein Rang '+t.eigener_rang));
    if(t.urteil_uebernommen)identity.append(el('p',{class:'small'},'aus früherer Suche'));
    if(t.status==='vielleicht')identity.append(el('p',{class:'small'},'Na ja'));
    const provider=sucheAnbieterLink(t);if(provider)identity.querySelector('.hit-identity > div').append(el('a',{class:'hit-provider',href:provider.url,target:'_blank',rel:'noopener noreferrer'},provider.label));
    identity.append(select(t));
    row.replaceChildren(identity,...fields.map(key=>el('td',{'data-label':STAY_FIELDS[key],'data-field':key},stayField(t,key,trip))),detail);
    row.nextElementSibling.cells[0].colSpan=fields.length+2;
    // W98b: Info-Box (Details-Angaben nach Themen) immer oben in den Details – gleiche Struktur bei jeder Unterkunft
    const content=row.nextElementSibling.querySelector('.hit-detail-content');if(content&&!content.querySelector(':scope > .stay-infobox'))content.prepend(stayInfoBox(t,trip));
  }
  return wrapper;
}
