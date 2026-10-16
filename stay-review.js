/* Wunsch 71: gerätebezogene Anzeige, Galerie und persönliche Endrunde. */
'use strict';
const STAY_FIELDS = {
  preis: 'Preis gesamt', nacht: 'Preis/Nacht', gaestenote: 'Note', bewertungen: 'Bewertungen',
  m2: 'Zimmergröße m²', schlafzimmer: 'Schlafzimmer', betten: 'Betten/Schlafplätze', balkon: 'Balkon',
  raucher: 'Raucher', storno: 'Storno', gehzeit: 'Gehzeit zum Ziel', viertel: 'Viertel', anbieter: 'Quelle', datenlage: 'Datenlage'
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
    box.replaceChildren(el('h2',{},'Anzeige'),el('p',{},'Höchstens 6 Infos für Liste, Tabelle und Tinder. Name, Foto, Rang und Merken bleiben immer sichtbar.'),
      el('p',{},fields.length+' / 6 ausgewählt'),el('ol',{class:'display-order'},fields.map((key,i)=>el('li',{draggable:'true','data-field':key,
        ondragstart:e=>{drag=i;e.dataTransfer.setData('text/plain',key);},ondragover:e=>e.preventDefault(),ondrop:e=>{e.preventDefault();if(drag!==null)move(drag,i);drag=null;},ondragend:()=>{drag=null;}},
        STAY_FIELDS[key],el('button',{type:'button',disabled:i===0,'aria-label':STAY_FIELDS[key]+' nach oben',onclick:()=>move(i,i-1)},'↑'),
        el('button',{type:'button',disabled:i===fields.length-1,'aria-label':STAY_FIELDS[key]+' nach unten',onclick:()=>move(i,i+1)},'↓')))),
      el('div',{class:'display-options'},Object.entries(STAY_FIELDS).map(([key,label])=>el('label',{},el('input',{type:'checkbox',checked:fields.includes(key),disabled:fields.length>=6&&!fields.includes(key),onchange:e=>{fields=e.target.checked?[...fields,key].slice(0,6):fields.filter(k=>k!==key);save();}}),label))),
      el('button',{type:'button',onclick:()=>{fields=[...STAY_DEFAULT_FIELDS];save();}},'Standard wiederherstellen'),status);
  }
  main.replaceChildren(box);draw();
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
    case 'betten': return room.typen ?? (room.anzahl!==null?room.anzahl+' Betten':null);
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
  else if(key==='gehzeit') box.append((t.gehzeit_art==='geschaetzt'?'ca. ':'')+value+' Min.');
  else box.append(String(value)+(key==='m2'?' m²':key==='datenlage'?' %':''));
  if(key==='gaestenote' && sucheZahl(t.note)!==null) box.append(el('small',{},`${t.note} / ${t.note_skala ?? '?'} bei ${SUCHE_QUELLEN[t.quelle] || t.quelle || 'Quelle'}`),el('small',{}, value===null?'Eichung nicht verfügbar.':'Auf Booking-Niveau geeicht; Airbnb-Noten liegen allgemein höher.'));
  if(key==='gehzeit' && value!==null) box.append(el('small',{},t.station_name?'Zur Station '+t.station_name:'Ziel nicht benannt'),el('small',{},t.gehzeit_art==='geschaetzt'?'geschätzt':['route','ors'].includes(t.gehzeit_art)?'berechneter Fußweg':'Art unbekannt'));
  return box;
}
function stayInfo(t,trip) {return el('dl',{class:'stay-info'},stayFields().flatMap(key=>[el('dt',{},STAY_FIELDS[key]),el('dd',{'data-field':key},stayField(t,key,trip))]));}
function stayGallery(t) {
  const urls=[...new Set([...(Array.isArray(t.bilder)?t.bilder:[]),t.bild].map(v=>sucheLink(v)).filter(Boolean))].slice(0,10);
  const box=el('section',{class:'stay-gallery','aria-label':'Fotogalerie'});
  if(!urls.length) {box.append(sucheFoto(t));return box;}
  let index=0,start=null;
  const photo=el('div'), count=el('span',{'aria-live':'polite'});
  const prev=el('button',{type:'button','aria-label':'Vorheriges Foto',onclick:()=>show(index-1)},'‹');
  const next=el('button',{type:'button','aria-label':'Nächstes Foto',onclick:()=>show(index+1)},'›');
  function show(i) {index=Math.max(0,Math.min(urls.length-1,i));photo.replaceChildren(sucheFoto({...t,bild:urls[index]}));count.textContent=`${index+1} / ${urls.length}`;prev.disabled=index===0;next.disabled=index===urls.length-1;}
  photo.addEventListener('pointerdown',e=>{start={x:e.clientX,y:e.clientY};});
  photo.addEventListener('pointerup',e=>{if(start && Math.abs(e.clientX-start.x)>50 && Math.abs(e.clientY-start.y)<50)show(index+(e.clientX<start.x?1:-1));start=null;});
  photo.addEventListener('pointercancel',()=>{start=null;});
  box.append(photo,el('div',{class:'actions'},prev,count,next));show(0);return box;
}
function stayEndrunde(hits,id,call,live,onSaved) {
  let order=hits.filter(t=>t.status==='favorit').sort((a,b)=>(a.eigener_rang??Infinity)-(b.eigener_rang??Infinity)||(a.bewertung?.rang??Infinity)-(b.bewertung?.rang??Infinity));
  const dialog=el('dialog',{class:'stay-candidate endrunde','aria-label':'Endrunde'}), body=el('div'), status=el('p',{role:'status'});
  let drag=null, pending=false, ranked=[], queue=[], candidate=null, position=0;
  const save=el('button',{type:'button',class:'primary',onclick:async()=>{
    if(pending||candidate||!order.length)return;pending=true;save.disabled=true;close.disabled=true;body.inert=true;status.textContent='Speichere …';
    try {const r=await call('unterkunft_eigenes_ranking_setzen',{suchauftrag_id:id,reihenfolge:order.map(t=>t.treffer_id)});if(!live())return;if(r.ok!==true)throw Error('Nicht bestätigt.');order.forEach((t,i)=>t.eigener_rang=i+1);onSaved();dialog.close();}
    catch(e){status.textContent='Rangfolge nicht bestätigt: '+e.message;}
    finally{pending=false;save.disabled=false;close.disabled=false;body.inert=false;}
  }},'Rangfolge speichern');
  const close=el('button',{type:'button',onclick:()=>dialog.close()},'Endrunde schließen');
  dialog.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
  function list() {candidate=null;save.disabled=order.length===0;body.replaceChildren(el('p',{},'Ziehe deine Favoriten in die gewünschte Reihenfolge oder nutze die Pfeile.'),el('ol',{},order.map((t,i)=>el('li',{'data-final-hit':t.treffer_id,draggable:'true',ondragstart:e=>{drag=i;e.dataTransfer.setData('text/plain',String(t.treffer_id));},ondragover:e=>e.preventDefault(),ondrop:e=>{e.preventDefault();if(drag!==null){order=stayMove(order,drag,i);list();}drag=null;},ondragend:()=>drag=null},
    `${i+1}. ${t.name}`,el('button',{type:'button',disabled:i===0,'aria-label':t.name+' nach oben',onclick:()=>{order=stayMove(order,i,i-1);list();}},'↑'),el('button',{type:'button',disabled:i===order.length-1,'aria-label':t.name+' nach unten',onclick:()=>{order=stayMove(order,i,i+1);list();}},'↓')))),
    el('button',{type:'button',disabled:order.length<2,onclick:()=>{queue=[...order];ranked=[queue.shift()];advance();}},'Paarvergleich starten')); }
  function advance(){candidate=queue.shift();position=0;if(!candidate){order=[...ranked];list();status.textContent='Paarvergleich abgeschlossen. Bitte Rangfolge speichern.';}else pair();}
  function pair(){save.disabled=true;const other=ranked[position];body.replaceChildren(el('h3',{},'A oder B?'),el('p',{},'Welche Unterkunft gefällt dir besser?'),el('div',{class:'pair-options'},[candidate,other].map(t=>el('section',{},stayGallery(t),el('h4',{},t.name),stayInfo(t),el('button',{type:'button',onclick:()=>{
    if(t===candidate){ranked.splice(position,0,candidate);advance();}else if(++position>=ranked.length){ranked.push(candidate);advance();}else pair();
  }},t.name+' wählen')))));}
  dialog.append(el('h2',{},'Endrunde · Favoriten'),close,body,status,save);list();return dialog;
}
function stayReview({getSnapshot,call,live,changed,scope}) {
  let pending=false, last=null, reasonFor=null, awaitingReturn=null, revision=0;
  const box=el('section',{class:'stay-review'}), message=el('p',{role:'status'});
  const minus=[['preis','Preis'],['zu_klein','Zu klein'],['lage','Lage'],['stil','Stil'],['betten','Betten'],['fotos','Fotos'],['laerm','Lärm'],['ausstattung','Ausstattung'],['sonstiges','Sonstiges']];
  const plus=[['plus_groesse','Größe'],['plus_lage','Lage'],['plus_stil','Stil'],['plus_preis','Preis'],['plus_ausstattung','Ausstattung'],['plus_fotos','Fotos'],['plus_betten','Betten']];
  let needsRefresh=false;
  async function vote(t,urteil,gruende=[],withReasons=true){
    if(pending||needsRefresh)return;pending=true;revision++;draw();
    try {const r=await call('unterkunft_durchsehen_urteil',{treffer_id:t.treffer_id,urteil,gruende});if(!live())return;
      if(r.ok!==true || r.treffer_id!==t.treffer_id || r.urteil!==urteil)throw Error('Urteil nicht eindeutig bestätigt.');
      t.status={favorit:'favorit',vielleicht:'vielleicht',weg:'ausgeschlossen',offen:'aktiv'}[urteil];t.urteil_gruende=gruende;
      if(urteil==='offen'){t.urteil_uebernommen=null;last=null;reasonFor=null;}else {last=t;reasonFor=withReasons?{t,urteil,gruende}:null;}
      awaitingReturn=null;message.textContent=urteil==='offen'?'Letzte Entscheidung zurückgenommen.':'Entscheidung gespeichert.';
    }catch(e){needsRefresh=true;message.textContent='Speichern nicht bestätigt: '+e.message+' Bitte aktualisieren, bevor du erneut entscheidest.';}
    finally{pending=false;revision++;if(live()){changed(t);draw();}}
  }
  function buttons(t){return el('div',{class:'actions review-actions'},[['favorit','Favorit'],['vielleicht','Na ja'],['weg','Weg']].map(([key,label])=>el('button',{type:'button',disabled:pending||needsRefresh,onclick:()=>vote(t,key)},label)));}
  function draw(){
    const snapshot=getSnapshot();if(!snapshot)return;
    const all=snapshot.treffer, queue=all.filter(t=>!['favorit','vielleicht','ausgeschlossen'].includes(t.status)&&t.topf!=='ausgeschlossen'&&!t.urteil_uebernommen).sort((a,b)=>(b.runde||1)-(a.runde||1)||(a.bewertung?.rang??Infinity)-(b.bewertung?.rang??Infinity)||a.treffer_id-b.treffer_id);
    box.replaceChildren(el('p',{class:'small'},`${queue.length} neu · ${all.filter(t=>['favorit','vielleicht','ausgeschlossen'].includes(t.status)||t.urteil_uebernommen).length} schon bewertet`),message,
      el('button',{type:'button',disabled:!last||pending||needsRefresh,onclick:()=>vote(last,'offen',[],false)},'Letzte Entscheidung rückgängig'));
    if(reasonFor){const r=reasonFor;box.append(el('section',{class:'review-reasons'},el('p',{},`Warum ${r.urteil==='favorit'?'Favorit':r.urteil==='weg'?'Weg':'Na ja'}? ${r.t.name} (optional)`),
      el('div',{class:'actions'},(r.urteil==='favorit'?plus:minus).map(([key,label])=>el('button',{type:'button','aria-pressed':r.gruende.includes(key),disabled:pending||needsRefresh,onclick:()=>{r.gruende=r.gruende.includes(key)?r.gruende.filter(k=>k!==key):[...r.gruende,key];draw();}},label))),
      el('button',{type:'button',disabled:pending||needsRefresh,onclick:()=>vote(r.t,r.urteil,r.gruende,false)},'Gründe speichern'),el('button',{type:'button',disabled:pending,onclick:()=>{reasonFor=null;draw();}},'Überspringen')));}
    const t=queue[0];if(!t){box.append(el('h3',{},'Alle Unterkünfte durchgesehen.'),el('p',{},'In der Endrunde kannst du deine Favoriten vergleichen.'));return;}
    const article=el('article',{class:'review-card','data-review-hit':t.treffer_id},stayGallery(t));
    const swipe=el('div',{class:'review-swipe'},el('h3',{},t.name),el('p',{},`Rang ${t.bewertung?.rang??'–'} · ${snapshot.suchauftrag.status==='fertig'&&['A','B'].includes(sucheGruppe(t))?'Endscore':'Vorläufiger Score'} ${t.bewertung?.score??'–'} %`),stayInfo(t,snapshot.suchauftrag));
    let point=null;
    swipe.addEventListener('pointerdown',e=>{if(e.button!==0 || e.target.closest('button,a'))return;point={x:e.clientX,y:e.clientY};try{swipe.setPointerCapture?.(e.pointerId);}catch{/* Synthetic events may lack an active pointer. */}});
    swipe.addEventListener('pointercancel',()=>point=null);
    swipe.addEventListener('pointerup',e=>{if(!point)return;const dx=e.clientX-point.x,dy=e.clientY-point.y;point=null;if(Math.max(Math.abs(dx),Math.abs(dy))<70)return;if(Math.abs(dx)>Math.abs(dy)*1.3)void vote(t,dx>0?'favorit':'weg');else if(dy < -70 && Math.abs(dy)>Math.abs(dx)*1.3)void vote(t,'vielleicht');});
    const url=sucheLink(t.angebot?.link);
    article.append(...[swipe,url?el('a',{href:url,target:'_blank',rel:'noopener noreferrer',onclick:()=>{awaitingReturn=t.treffer_id;}},'Beim Anbieter ansehen ↗'):null,
      awaitingReturn===t.treffer_id?el('p',{role:'status'},'Und? Wie gefällt dir die Unterkunft?'):null,buttons(t)].filter(Boolean));box.append(article);
  }
  const returned=()=>{if(!document.hidden && awaitingReturn && live())draw();};document.addEventListener('visibilitychange',returned);
  return {node:box,draw,get revision(){return revision;},get pending(){return pending;},refreshed(){if(!pending){needsRefresh=false;last=null;reasonFor=null;}},dispose(){document.removeEventListener('visibilitychange',returned);}};
}
function stayConfigureTable(wrapper,items,sort,onSort,trip,select) {
  const table=wrapper.querySelector('table'), head=table.tHead.rows[0], fields=stayFields();
  const heading=(key,label)=>el('th',{scope:'col','aria-sort':sort.key===key?sort.direction===1?'ascending':'descending':'none'},el('button',{type:'button','data-sort':key,onclick:()=>onSort(key)},label));
  head.replaceChildren(heading('name','Unterkunft'),...fields.map(key=>heading(key,STAY_FIELDS[key])),el('th',{scope:'col'},'Details'));
  for(const t of items){const row=wrapper.querySelector(`tr[data-hit="${t.treffer_id}"]`), identity=row.cells[0], detail=row.lastElementChild;
    const scoreBox=el('div',{class:'small hit-score'},(trip.status==='fertig' && ['A','B'].includes(sucheGruppe(t))?'Endscore: ':'Vorläufiger Score: ')+(sucheZahl(t.bewertung?.score)??'–')+' %');identity.append(scoreBox);
    if(t.eigener_rang)identity.append(el('p',{class:'small'},'Dein Rang '+t.eigener_rang));
    if(t.urteil_uebernommen)identity.append(el('p',{class:'small'},'aus früherer Suche'));
    if(t.status==='vielleicht')identity.append(el('p',{class:'small'},'Na ja'));
    identity.append(select(t));
    row.replaceChildren(identity,...fields.map(key=>el('td',{'data-label':STAY_FIELDS[key],'data-field':key},stayField(t,key,trip))),detail);
    row.nextElementSibling.cells[0].colSpan=fields.length+2;
  }
  return wrapper;
}
