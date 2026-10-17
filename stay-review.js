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
  preis: 'Preis gesamt', nacht: 'Preis/Nacht', gaestenote: 'Gäste (geeicht)', bewertungen: 'Bewertungen',
  m2: 'Zimmergröße m²', schlafzimmer: 'Schlafzimmer', betten: 'Betten/Schlafplätze', balkon: 'Balkon',
  raucher: 'Raucher', storno: 'Storno', gehzeit: 'Gehzeit zur Station', viertel: 'Viertel', anbieter: 'Quelle', datenlage: 'Datenlage'
};
const STAY_DEFAULT_FIELDS = ['preis','gaestenote','m2','schlafzimmer','gehzeit','storno'];
function stayRead(key, fallback) { try { return JSON.parse(localStorage.getItem(key)) ?? fallback; } catch { return fallback; } }
function stayWrite(key, value) { try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; } }
let stayFieldsMemory = null;
function stayFields() {
  const value = stayFieldsMemory ?? stayRead('ks_anzeige', STAY_DEFAULT_FIELDS);
  return Array.isArray(value) && value.length <= 6 && new Set(value).size === value.length && value.every(k => Object.hasOwn(STAY_FIELDS,k)) ? [...value] : [...STAY_DEFAULT_FIELDS];
}
function stayMove(list, from, to) { const copy=[...list]; if(from<0 || to<0 || from>=copy.length || to>=copy.length) return copy; copy.splice(to,0,copy.splice(from,1)[0]); return copy; }
function viewAnzeige() {
  setChrome('Anzeige', {back:true});
  let fields=stayFields(), drag=null;
  const box=el('section',{class:'card display-settings'}), status=el('p',{role:'status'});
  function save() { stayFieldsMemory=[...fields]; status.textContent=stayWrite('ks_anzeige',fields) ? 'Auf diesem Gerät gespeichert.' : 'Gerätespeicher nicht verfügbar. Auswahl gilt bis zum Neuladen.'; draw(); }
  function move(i,j) {fields=stayMove(fields,i,j);save();}
  function draw() {
    box.replaceChildren(el('h2',{},'Anzeige'),el('p',{},'Höchstens 6 Infos für Liste und Tabelle. Name, Foto, Rang und Favorit bleiben immer sichtbar.'),
      el('p',{},fields.length+' / 6 ausgewählt'),el('ol',{class:'display-order'},fields.map((key,i)=>el('li',{draggable:'true','data-field':key,
        ondragstart:e=>{drag=i;e.dataTransfer.setData('text/plain',key);},ondragover:e=>e.preventDefault(),ondrop:e=>{e.preventDefault();if(drag!==null)move(drag,i);drag=null;},ondragend:()=>{drag=null;}},
        STAY_FIELDS[key],el('button',{type:'button',disabled:i===0,'aria-label':STAY_FIELDS[key]+' nach oben',onclick:()=>move(i,i-1)},'↑'),
        el('button',{type:'button',disabled:i===fields.length-1,'aria-label':STAY_FIELDS[key]+' nach unten',onclick:()=>move(i,i+1)},'↓')))),
      el('div',{class:'display-options'},Object.entries(STAY_FIELDS).map(([key,label])=>el('label',{},el('input',{type:'checkbox',checked:fields.includes(key),disabled:fields.length>=6&&!fields.includes(key),onchange:e=>{fields=e.target.checked?[...fields,key].slice(0,6):fields.filter(k=>k!==key);save();}}),label))),
      el('button',{type:'button',onclick:()=>{fields=[...STAY_DEFAULT_FIELDS];save();}},'Standard wiederherstellen'),status);
  }
  const reviewBox=el('section',{class:'card'});let optional=stayReviewFields();
  function reviewDraw(){reviewBox.replaceChildren(el('h2',{},'Durchsehen'),el('p',{},'Gesamtpreis, Fläche und Schlafzimmer bleiben sichtbar. Wähle bis zu 4 zusätzliche Infos.'),el('p',{},optional.length+' / 4 ausgewählt'),...Object.entries(STAY_FIELDS).filter(([key])=>!['preis','m2','schlafzimmer'].includes(key)).map(([key,label])=>el('label',{class:'check-label'},el('input',{type:'checkbox','aria-label':'Durchsehen: '+label,checked:optional.includes(key),disabled:optional.length>=4&&!optional.includes(key),onchange:e=>{optional=e.target.checked?[...optional,key]:optional.filter(k=>k!==key);status.textContent=stayWrite('ks_review_fields',optional)?'Auf diesem Gerät gespeichert.':'Gerätespeicher nicht verfügbar.';reviewDraw();}}),label)));}
  main.replaceChildren(box,reviewBox);draw();reviewDraw();
}
function stayFieldValue(t,key,trip={}) {
  const a=t.angebot||{}, k=sucheAngebotsKategorie(t), room=sucheZimmerKurz(t), n=sucheZahl;
  const category=k?.konflikt ? null : k;
  const yes=v=>v===true||v==='ja'?'ja':v===false||v==='nein'?'nein':null;
  switch(key) {
    case 'preis': return n(a.preis_gesamt_eur);
    case 'nacht': { const nights=(Date.parse(trip.abreise || t._trip?.abreise)-Date.parse(trip.anreise || t._trip?.anreise))/86400000; return n(a.preis_nacht_eur) ?? (n(a.preis_gesamt_eur)!==null&&nights>0?a.preis_gesamt_eur/nights:null); }
    case 'gaestenote': return n(t.note_geeicht);
    case 'bewertungen': return n(t.bewertungen);
    case 'm2': return n(category?.m2);
    case 'schlafzimmer': return room.schlafzimmer;
    case 'betten': return (room.typen ? sucheBettenDeutsch(room.typen) : null) ?? (room.anzahl!==null?room.anzahl+' Betten':null);
    case 'balkon': return yes(category?.balkon);
    case 'raucher': return yes(category?.raucher ?? t.raucher);
    case 'storno': return typeof a.storno==='string' && a.storno.trim() && a.storno!=='unbekannt' ? a.storno : null;
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
  else if(['preis','nacht'].includes(key)) box.append((t.angebot?.preis_art==='geschaetzt'?'ca. ':'')+sucheEuro(value));
  else if(key==='gaestenote') box.append(Number(value).toLocaleString('de-DE',{maximumFractionDigits:2})+' / 10');
  else if(key==='gehzeit') box.append(sucheWegText(t));
  else box.append((key==='m2'?Number(value).toLocaleString('de-DE'):String(value))+(key==='m2'?' m²':key==='datenlage'?' %':''));
  if(key==='gaestenote') box.append(el('small',{}, value===null?'Eichung nicht verfügbar.':'geeicht'));
  if(key==='gehzeit' && value!==null) box.append(el('small',{},t.station_name?'Zur Station '+t.station_name:'Ziel nicht benannt'),el('small',{},t.gehzeit_art==='geschaetzt'?'geschätzt':['route','ors'].includes(t.gehzeit_art)?'berechneter Fußweg':'Art unbekannt'));
  return box;
}
function stayInfo(t,trip) {return el('dl',{class:'stay-info'},stayFields().flatMap(key=>[el('dt',{},STAY_FIELDS[key]),el('dd',{'data-field':key},stayField(t,key,trip))]));}
function stayReviewFields(){const allowed=Object.keys(STAY_FIELDS).filter(k=>!['preis','m2','schlafzimmer'].includes(k));const saved=stayRead('ks_review_fields',['gaestenote','gehzeit']);return (Array.isArray(saved)?saved:[]).filter((k,i,a)=>allowed.includes(k)&&a.indexOf(k)===i).slice(0,4);}
function stayReviewInfo(t,trip) {
  const nights=(Date.parse(trip.abreise)-Date.parse(trip.anreise))/86400000;
  const labels={preis:nights>0?'Gesamt · '+nights+' Nächte':'Gesamtpreis',nacht:'Pro Nacht',gaestenote:'Gästenote',m2:'Fläche',schlafzimmer:'Schlafzimmer',gehzeit:'Zu Fuß zur Station'};
  return el('dl',{class:'review-info'},['preis','m2','schlafzimmer',...stayReviewFields()].map(key=>{
    const value=stayFieldValue(t,key,trip);let display=value===null?'unbekannt':String(value), note=null;
    if(value!==null){
      if(['preis','nacht'].includes(key))display=(t.angebot?.preis_art==='geschaetzt'?'ca. ':'')+sucheEuro(value);
      if(key==='m2')display=Number(value).toLocaleString('de-DE')+' m²';
      if(key==='datenlage')display=value+' %';
      if(key==='gaestenote'){display=Number(value).toLocaleString('de-DE',{maximumFractionDigits:2})+' / 10';note='geeicht · '+(SUCHE_QUELLEN[t.quelle]||t.quelle||'Quelle');}
      if(key==='gehzeit'){display=(t.gehzeit_art==='geschaetzt'?'ca. ':'')+(value>=60?Math.floor(value/60)+' Std. '+Math.round(value%60)+' Min.':Math.round(value)+' Min.');note=t.station_name||'Station unbekannt';if(!['route','ors','geschaetzt'].includes(t.gehzeit_art))note+=' · Berechnung unbekannt';}
    }
    return el('div',{'data-field':key},el('dt',{},labels[key]||STAY_FIELDS[key]),el('dd',{},display,note?el('small',{},note):null));
  }));
}
function stayCardPhoto(card, gallery) {
  card.querySelector(':scope > .review-backdrop')?.remove();
  const source=gallery.querySelector('img');
  if(!source)return;
  const image=el('img',{class:'review-backdrop',alt:'','aria-hidden':'true',referrerpolicy:'no-referrer',src:source.src,onerror:()=>image.remove()});
  card.prepend(image);
}
function stayGallery(t) {
  const urls=[...new Set([...(Array.isArray(t.bilder)?t.bilder:[]),t.bild].map(v=>sucheLink(v)).filter(Boolean))].slice(0,10);
  const box=el('section',{class:'stay-gallery'+(!urls.length?' gallery-empty':''),'aria-label':'Fotogalerie'});
  if(!urls.length) {box.append(sucheFoto(t));return box;}
  let index=0,start=null;
  const photo=el('div'), count=el('span',{'aria-live':'polite'});
  const prev=el('button',{type:'button','aria-label':'Vorheriges Foto',onclick:()=>show(index-1)},'‹');
  const next=el('button',{type:'button','aria-label':'Nächstes Foto',onclick:()=>show(index+1)},'›');
  function show(i) {index=Math.max(0,Math.min(urls.length-1,i));photo.replaceChildren(sucheFoto({...t,bild:urls[index]}));count.textContent=`${index+1} / ${urls.length}`;box.dataset.photo=`Foto ${index+1}/${urls.length}`;box.onPhotoChange?.();prev.disabled=index===0;next.disabled=index===urls.length-1;const card=box.closest('.review-card');if(card)stayCardPhoto(card,box);const img=photo.querySelector('img');if(img)img.addEventListener('error',()=>{box.classList.add('gallery-empty');card?.querySelector(':scope > .review-backdrop')?.remove();});box.classList.remove('gallery-empty');}
  photo.addEventListener('pointerdown',e=>{start={x:e.clientX,y:e.clientY};});
  photo.addEventListener('pointerup',e=>{if(start && Math.abs(e.clientX-start.x)>50 && Math.abs(e.clientY-start.y)<50)show(index+(e.clientX<start.x?1:-1));start=null;});
  photo.addEventListener('pointercancel',()=>{start=null;});
  const controls=el('div',{class:'actions gallery-controls'},urls.length>1?prev:null,count,urls.length>1?next:null);
  photo.tabIndex=0;photo.setAttribute('aria-label','Foto ansehen');photo.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'||e.key==='ArrowRight'){e.preventDefault();show(index+(e.key==='ArrowRight'?1:-1));}});
  const large=el('button',{type:'button',class:'photo-large',onclick:()=>{const d=el('dialog',{class:'trip-dialog photo-dialog','aria-label':'Foto groß'});d.append(el('button',{onclick:()=>d.close()},'Schließen'),sucheFoto({...t,bild:urls[index]}));main.append(d);d.addEventListener('close',()=>{d.remove();large.focus();});d.showModal();}},'Foto groß');
  box.append(photo,controls,large);show(0);return box;
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
  let needsRefresh=false, activeGroup=null;
  const reviewed=new Set();
  async function vote(t,urteil,gruende=[],withReasons=true,restoring=false){
    if(pending||needsRefresh||isBlocked())return;const focusDecision=document.activeElement?.dataset.decision;const previous={status:t.status||'aktiv',gruende:[...(t.urteil_gruende||[])],uebernommen:t.urteil_uebernommen};pending=true;revision++;draw();
    try {const r=await call('unterkunft_durchsehen_urteil',{treffer_id:t.treffer_id,urteil,gruende});if(!live())return;
      if(r.ok!==true || r.treffer_id!==t.treffer_id || r.urteil!==urteil || r.status!==({favorit:'favorit',vielleicht:'vielleicht',weg:'ausgeschlossen',offen:'aktiv'}[urteil]))throw Error('Urteil nicht eindeutig bestätigt.');
      t.status={favorit:'favorit',vielleicht:'vielleicht',weg:'ausgeschlossen',offen:'aktiv'}[urteil];t.urteil_gruende=gruende;
      if(restoring){reviewed.delete(t.treffer_id);t.urteil_uebernommen=previousRestore;last=null;reasonFor=null;}else if(urteil==='offen'){t.urteil_uebernommen=null;last=null;reasonFor=null;}else {if(withReasons){last={t,previous};if(activeGroup)reviewed.add(t.treffer_id);}reasonFor=withReasons?{t,urteil,gruende}:null;}
      if(reasonsDialog){reasonsDialog.close();reasonsDialog.remove();reasonsDialog=null;}
      awaitingReturn=null;message.textContent=restoring||urteil==='offen'?'Letzte Entscheidung zurückgenommen.':'Entscheidung gespeichert.';
    }catch(e){needsRefresh=true;if(reasonsDialog){reasonsDialog.close();reasonsDialog.remove();reasonsDialog=null;}message.textContent='Speichern nicht bestätigt: '+e.message+' Bitte aktualisieren, bevor du erneut entscheidest.';}
    finally{pending=false;revision++;if(live()){changed(t);draw();if(focusDecision)box.querySelector('[data-decision="'+focusDecision+'"]')?.focus({preventScroll:true});}}
  }
  let previousRestore=null;
  function undoVote(){if(!last)return;const {t,previous}=last;previousRestore=previous.uebernommen;void vote(t,({aktiv:'offen',favorit:'favorit',vielleicht:'vielleicht',ausgeschlossen:'weg'})[previous.status]||'offen',previous.gruende,false,true);}
  function buttons(t){return el('div',{class:'actions review-actions'},[['weg','Weg'],['vielleicht','Na ja'],['favorit','Favorit']].map(([key,label])=>el('button',{type:'button',class:'decision-'+key,'aria-label':label,'data-decision':key,disabled:pending||needsRefresh||isBlocked(),onclick:()=>vote(t,key)},el('span',{'aria-hidden':'true'},({weg:'×',vielleicht:'≈',favorit:'♥'})[key]+' '),label)));}
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
    const group=getGroup();if(group!==activeGroup){activeGroup=group;reviewed.clear();last=null;reasonFor=null;}
    const all=getRows()||[], queue=all.filter(t=>group ? t.status===group&&!reviewed.has(t.treffer_id) : !['favorit','vielleicht','ausgeschlossen'].includes(t.status)&&t.topf!=='ausgeschlossen'&&(!t.urteil_uebernommen || (t.status==='aktiv' && t.urteil_uebernommen.hinweis))).sort((a,b)=>(b.runde||1)-(a.runde||1)||(a.bewertung?.rang??Infinity)-(b.bewertung?.rang??Infinity)||a.treffer_id-b.treffer_id);
    const total=group?queue.length+reviewed.size:all.filter(t=>t.topf!=='ausgeschlossen').length;
    const progress=el('span',{class:'review-position','aria-live':'polite'});
    const undo=el('button',{type:'button',disabled:!last||pending||needsRefresh||isBlocked(),'aria-label':'Letzte Entscheidung rückgängig',onclick:undoVote},'↶');
    const menu=el('details',{class:'review-menu'},el('summary',{'aria-label':'Durchsehen-Menü'},'•••'),el('div',{class:'review-menu-panel'},...menuItems(),el('p',{class:'review-progress'},`${queue.length} offen · ${all.filter(t=>['favorit','vielleicht','ausgeschlossen'].includes(t.status)).length} bewertet`),el('button',{type:'button',class:'review-reason-open',disabled:!reasonFor||pending||needsRefresh||isBlocked(),onclick:openReasons},'Gründe ergänzen')));
    const header=el('header',{class:'review-overlay-header'},el('button',{type:'button','aria-label':'Durchsehen schließen',disabled:pending,onclick:onClose},'×'),progress,undo,menu);
    box.replaceChildren(message);
    if(pending)message.textContent='Speichere …';
    if((needsRefresh||isBlocked())&&!pending&&onRefresh)box.append(el('button',{type:'button',class:'review-reload',onclick:onRefresh},'Aktualisieren'));
    const t=queue[0];if(!t){progress.textContent='Durchsehen abgeschlossen';box.append(header);box.append(el('h3',{},'Alle Unterkünfte durchgesehen.'),el('p',{},'In der Endrunde kannst du deine Favoriten vergleichen.'));return;}
    if(galleryId!==t.treffer_id){galleryId=t.treffer_id;gallery=stayGallery(t);}
    const article=el('article',{class:'review-card','data-review-hit':t.treffer_id});
    gallery.onPhotoChange=()=>{progress.textContent=`Unterkunft ${Math.max(1,total-queue.length+1)}/${total} · ${gallery.dataset.photo||'Kein Foto'}`;};gallery.onPhotoChange();
    const content=el('div',{class:'review-content',tabindex:0,'aria-label':'Unterkunft ansehen'},gallery,t.urteil_uebernommen?.hinweis?el('p',{class:'warning'},'Jetzt günstiger · '+t.urteil_uebernommen.hinweis):null);
    const swipe=el('div',{class:'review-swipe'},el('h3',{tabindex:-1},t.name),el('p',{class:'review-score'},`Rang ${t.bewertung?.rang??'–'} · ${snapshot.suchauftrag.status==='fertig'&&['A','B'].includes(sucheGruppe(t))?'Passung':'Vorläufige Passung'} ${t.bewertung?.score??'–'}/100`),stayReviewInfo(t,snapshot.suchauftrag));
    let point=null, swiped=false;
    swipe.addEventListener('pointerdown',e=>{if(point){point=null;return;}if(e.isPrimary===false || e.button!==0 || e.target.closest('button,a') || document.querySelector('dialog[open]'))return;point={id:e.pointerId,x:e.clientX,y:e.clientY};try{swipe.setPointerCapture?.(e.pointerId);}catch{/* Synthetic events may lack an active pointer. */}});
    swipe.addEventListener('pointercancel',()=>point=null);
    swipe.addEventListener('pointerup',e=>{if(!point||point.id!==e.pointerId)return;const dx=e.clientX-point.x,dy=e.clientY-point.y;point=null;if(Math.max(Math.abs(dx),Math.abs(dy))<70)return;if(Math.abs(dx)>Math.abs(dy)*1.3){swiped=true;void vote(t,dx>0?'favorit':'weg');}});
    swipe.addEventListener('click',e=>{if(swiped){e.preventDefault();e.stopPropagation();swiped=false;}},true);
    const warnings=[...sucheWarnungen(t).map(w=>SUCHE_WARNUNGEN[w]||w),...['m2','schlafzimmer','gehzeit'].filter(k=>stayFieldValue(t,k,snapshot.suchauftrag)===null).map(k=>({m2:'Fläche: unbekannt',schlafzimmer:'Schlafzimmer: unbekannt',gehzeit:'Station: unbekannt'})[k])];if(warnings.length)swipe.append(el('details',{class:'warning'},el('summary',{},warnings[0]+(warnings.length>1?' · '+(warnings.length-1)+' weitere prüfen':'')),warnings.map(w=>el('p',{},w))));
    const provider=sucheAnbieterLink(t), url=provider?.url;
    content.append(swipe,el('div',{class:'review-links'},url?el('a',{href:url,target:'_blank',rel:'noopener noreferrer',onclick:()=>{awaitingReturn=t.treffer_id;}},provider.label):null,
      el('button',{type:'button',onclick:event=>{const trigger=event.currentTarget,dialog=sucheKandidat(t,snapshot.suchauftrag.status==='fertig',snapshot.suchauftrag.id);scope.append(dialog);dialog.addEventListener('close',()=>{dialog.remove();if(trigger.isConnected)trigger.focus({preventScroll:true});});dialog.showModal();}},'Details')));
    if(awaitingReturn===t.treffer_id)content.append(el('p',{role:'status'},'Und? Wie gefällt dir die Unterkunft?'));
    article.append(header,content,buttons(t));stayCardPhoto(article,gallery);box.append(article);

  }
  const returned=()=>{if(!document.hidden && awaitingReturn && live())draw();};document.addEventListener('visibilitychange',returned);
  return {node:box,draw,get revision(){return revision;},get pending(){return pending;},get blocked(){return needsRefresh;},refreshed(){if(!pending){needsRefresh=false;last=null;reasonFor=null;}},dispose(){reasonsDialog?.close();reasonsDialog?.remove();document.removeEventListener('visibilitychange',returned);}};
}
function stayConfigureTable(wrapper,items,sort,onSort,trip,select) {
  const table=wrapper.querySelector('table'), head=table.tHead.rows[0], fields=stayFields();
  const heading=(key,label)=>el('th',{scope:'col','aria-sort':sort.key===key?sort.direction===1?'ascending':'descending':'none'},el('button',{type:'button','data-sort':key,onclick:()=>onSort(key)},label));
  head.replaceChildren(heading('name','Unterkunft'),...fields.map(key=>heading(key,STAY_FIELDS[key])),el('th',{scope:'col'},'Details'));
  for(const t of items){const row=wrapper.querySelector(`tr[data-hit="${t.treffer_id}"]`), identity=row.cells[0], detail=row.lastElementChild;
    const scoreBox=el('div',{class:'small hit-score'},(trip.status==='fertig' && ['A','B'].includes(sucheGruppe(t))?'Passung: ':'Vorläufige Passung: ')+(sucheZahl(t.bewertung?.score)??'–')+'/100');identity.append(scoreBox);
    if(t.eigener_rang)identity.append(el('p',{class:'small'},'Dein Rang '+t.eigener_rang));
    if(t.urteil_uebernommen)identity.append(el('p',{class:'small'},'aus früherer Suche'));
    if(t.status==='vielleicht')identity.append(el('p',{class:'small'},'Na ja'));
    const provider=sucheAnbieterLink(t);if(provider)identity.querySelector('.hit-identity > div').append(el('a',{class:'hit-provider',href:provider.url,target:'_blank',rel:'noopener noreferrer'},provider.label));
    identity.append(select(t));
    row.replaceChildren(identity,...fields.map(key=>el('td',{'data-label':STAY_FIELDS[key],'data-field':key},stayField(t,key,trip))),detail);
    row.nextElementSibling.cells[0].colSpan=fields.length+2;
  }
  return wrapper;
}
