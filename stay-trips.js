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
async function viewReisen(arg){
 setChrome('Deine Reisen',{tab:'reisen'});const live=viewGuard(),scope=el('section',{class:'trips-page'});main.replaceChildren(scope);
 const status=el('p',{role:'status'}),content=el('div'),selector=el('select',{'aria-label':'Reise auswählen'});let snapshot=null,pending=false;
 const header=el('header',{class:'trip-hero'},el('p',{class:'eyebrow'},'ENTDECKER'),el('h2',{},'Wohin geht es als Nächstes?'),el('p',{},'Eure Aufenthalte. Eure Favoriten. Alles an einem Ort.'));
 const reload=el('button',{onclick:load},'Reisen aktualisieren');
 const create=el('button',{class:'primary',onclick:()=>{const {d,body,status:msg}=tripDialog('Neue Reise');const f=el('form'),name=el('input',{required:true,maxlength:100,'aria-label':'Reisename',placeholder:'z. B. Japan im Herbst'}),b=el('button',{type:'submit',class:'primary'},'Reise anlegen');f.append(el('label',{},'Reisename',name),b);body.append(f);f.onsubmit=async ev=>{ev.preventDefault();if(b.disabled)return;b.disabled=true;try{const created=await tripCall('unterkunft_reise_speichern',{name:name.value.trim()});if(!tripId(created.reise?.id))throw Error('Reise nicht eindeutig bestätigt.');d.close();await load();}catch(e){msg.textContent=e.message+' Bitte neu lesen, bevor du erneut anlegst.';}};}},'Neue Reise');
 scope.append(header,el('div',{class:'trip-toolbar'},selector,create,reload,el('a',{href:'#/papierkorb'},'Papierkorb')),status,content);
 selector.onchange=()=>{stayWrite('ks_reise',Number(selector.value));draw();};
 async function change(e,data){if(pending)return;if(e.status==='gebucht'&&data.aktive_suche_id&&data.aktive_suche_id!==e.aktive_suche_id){status.textContent='Diese Etappe ist bereits gebucht. Für einen anderen gebuchten Aufenthalt bitte eine getrennte Etappe anlegen; die Buchung wird nicht still auf andere Tage übertragen.';return;}pending=true;scope.querySelectorAll('button').forEach(b=>b.disabled=true);try{const r=await tripCall('unterkunft_etappe_speichern',{id:e.id,version:e.version,...data});if(r.etappe?.id!==e.id)throw Error('Änderung nicht bestätigt.');await load();}catch(err){status.textContent=err.message+' Bitte Reisen aktualisieren.';}finally{pending=false;reload.disabled=false;}}
 function draw(){
  const expanded=new Set([...content.querySelectorAll('[data-stage] details[open]')].map(n=>Number(n.closest('[data-stage]').dataset.stage)));
  const rid=Number(selector.value),trip=snapshot.reisen.find(x=>x.id===rid);content.replaceChildren();if(!trip){content.append(el('p',{},'Lege deine erste Reise an. Danach kannst du Unterkünfte suchen.'));return;}
  const stages=snapshot.etappen.filter(e=>e.reise_id===rid).sort((a,b)=>String(a.anreise).localeCompare(String(b.anreise))||a.id-b.id);
  content.append(el('div',{class:'trip-title'},el('div',{},el('p',{class:'eyebrow'},'DEINE REISE'),el('h2',{},trip.name)),el('button',{class:'primary',onclick:()=>{stayWrite('ks_trip_context',{reise_id:rid});route('suche');}},'+ Aufenthalt suchen'),el('button',{onclick:()=>tripExternalBooking({reise_id:rid},load)},'Aufenthalt nachtragen')));
  const timeline=el('div',{class:'trip-timeline'}),proposals=el('section',{class:'trip-proposals'},el('h3',{},'Noch nicht bestätigte Vorschläge'));content.append(timeline);
  const confirmed=stages.filter(e=>e.status!=='vorschlag');
  for(const e of stages){const b=e.buchung,card=el('article',{class:'trip-stage','data-stage':e.id});
   card.append(el('div',{class:'stage-date'},el('strong',{},fmtDate(e.anreise)),el('span',{},'bis '+fmtDate(e.abreise)),el('small',{},(e.naechte??'–')+' Nächte')),
    el('div',{class:'stage-main'},el('span',{class:'trip-status '+e.status},{vorschlag:'Vorschlag · noch bestätigen',geplant:'Geplant',gebucht:'Gebucht'}[e.status]||'Status offen'),el('h3',{},e.ziel),b?el('div',{class:'booking-summary'},el('strong',{},b.name||'Unterkunft'),el('p',{},b.zimmer||''),el('p',{},sucheEuro(b.preis_gesamt_eur)+' gesamt'),el('p',{class:'storno'},tripStorno(b))):el('p',{class:'muted'},'Die Unterkunft ist noch offen.'),
    el('div',{class:'actions'},e.status==='vorschlag'?el('button',{class:'primary',onclick:()=>change(e,{status:'geplant'})},'Vorschlag bestätigen'):null,el('button',{onclick:()=>tripStart(e)},'Andere Tage suchen'),el('button',{onclick:()=>tripExternalBooking(e,load)},'Woanders gebucht'),el('button',{onclick:()=>tripEdit(e,load)},'Bearbeiten'),el('button',{onclick:()=>tripDelete('etappe',e.id,load)},e.status==='vorschlag'?'Vorschlag verwerfen':'Etappe entfernen'))));
   const searches=el('details',{open:expanded.has(e.id)},el('summary',{},(e.suchen||[]).length+' Suchvarianten'));
   for(const s of e.suchen||[]){const active=s.id===e.aktive_suche_id;searches.append(el('div',{class:'trip-variant'},el('a',{href:'#/suche/'+s.id},`${fmtDate(s.anreise)}–${fmtDate(s.abreise)} · ${s.status}`),active?el('strong',{},'Aktuelle Variante'):el('button',{onclick:()=>change(e,{aktive_suche_id:s.id})},'Diese Tage verwenden'),el('button',{onclick:()=>tripDelete('suchauftrag',s.id,load)},'Suche entfernen')));}
   card.querySelector('.stage-main').append(searches,el('a',{href:'#/etappe/'+e.id},'Unterkünfte dieser Etappe →'));if(e.status==='vorschlag')proposals.append(card);else {
    const before=confirmed[confirmed.indexOf(e)-1];
    for(const gap of snapshot.luecken||[]){if(before&&gap.zwischen?.[0]===before.id&&gap.zwischen?.[1]===e.id)timeline.append(el('div',{class:'trip-gap','data-gap-from':before.id,'data-gap-to':e.id},`${before.ziel} → ${e.ziel}: `+(gap.text||`${gap.naechte} Nächte noch offen`)));}
    timeline.append(card);
   }
  }
  if(proposals.childElementCount>1)content.append(proposals);
  if(!stages.length)timeline.append(el('p',{class:'card'},'Noch keine Etappen. Suche deinen ersten Aufenthalt.'));
  const loose=(snapshot.ohne_etappe||[]).filter(s=>s.reise_id===rid||!s.reise_id);if(loose.length){const box=el('details',{},el('summary',{},'Suchen ohne Etappe'));for(const s of loose){const target=el('select',{'aria-label':'Etappe für Suche '+s.id},el('option',{value:''},'Etappe wählen'),stages.map(e=>el('option',{value:e.id},e.ziel+' · '+fmtDate(e.anreise))));box.append(el('div',{class:'trip-variant'},el('a',{href:'#/suche/'+s.id},'Suche #'+s.id+' · '+s.ziel),target,el('button',{onclick:async ev=>{if(!tripId(target.value))return;ev.target.disabled=true;try{const r=await tripCall('unterkunft_etappe_zuordnen',{suchauftrag_id:s.id,etappe_id:Number(target.value)});if(!r.suche)throw Error('Zuordnung nicht bestätigt.');await load();}catch(e){status.textContent=e.message+' Bitte neu lesen.';}}},'Zuordnen')));}content.append(box);}
 }
 async function load(){reload.disabled=true;status.textContent='Reisen werden geladen …';try{const r=await tripCall('unterkunft_etappen_lesen');if(!live())return;if(!Array.isArray(r.reisen)||!Array.isArray(r.etappen))throw Error('Reiseübersicht unvollständig.');snapshot=r;const selected=tripId(arg)||Number(selector.value)||stayRead('ks_reise',null);selector.replaceChildren(...r.reisen.map(t=>el('option',{value:t.id},t.name)));if(r.reisen.some(t=>t.id===selected))selector.value=selected;draw();status.textContent='';}catch(e){if(live())status.textContent=e.message;}finally{reload.disabled=false;}}
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
function tripSearchChoice(form,call,live){
 const ctx=stayRead('ks_trip_context',{}),reise=el('select',{'aria-label':'Reise',required:true},el('option',{value:''},'Reise wählen')),stage=el('select',{'aria-label':'Aufenthalt'},el('option',{value:''},'Getrennter / neuer Aufenthalt')),notice=el('p',{role:'status'});let data=null;
 const node=el('section',{class:'card'},el('h2',{},'In welcher Reise?'),el('label',{},'Reise',reise),el('label',{},'Aufenthalt',stage),el('a',{href:'#/reisen'},'Reisen verwalten'),notice);
 form.querySelector('fieldset').prepend(node);
 const destination=form.querySelector('[name=ziel]');
 function normalize(x){return String(x||'').trim().toLocaleLowerCase('de').replace(/tokio/g,'tokyo').replace(/kioto/g,'kyoto');}
 function paint(){const previous=stage.value,matching=(data?.etappen||[]).filter(e=>e.reise_id===Number(reise.value)&&normalize(e.ziel)===normalize(destination.value));stage.replaceChildren(...[matching.length?el('option',{value:''},'Bestehender oder getrennter Aufenthalt?'):null,el('option',{value:'new'},'Getrennter / neuer Aufenthalt'),...matching.map(e=>el('option',{value:e.id},e.ziel+' · '+fmtDate(e.anreise)))].filter(Boolean));if(matching.some(e=>e.id===Number(previous)))stage.value=previous;else if(matching.some(e=>e.id===ctx.etappe_id))stage.value=ctx.etappe_id;}
 reise.onchange=paint;destination.addEventListener('input',paint);
 call('unterkunft_etappen_lesen').then(r=>{if(!live())return;if(!Array.isArray(r.reisen)||!Array.isArray(r.etappen))throw Error('Reisen konnten nicht geladen werden.');data=r;reise.append(...r.reisen.map(t=>el('option',{value:t.id},t.name)));if(ctx.reise_id&&r.reisen.some(t=>t.id===ctx.reise_id))reise.value=ctx.reise_id;if(ctx.ziel)destination.value=ctx.ziel;paint();}).catch(e=>{if(live())notice.textContent=e.message;});
 return {values(){const rid=tripId(reise.value);if(!data||!rid)throw Error('Bitte zuerst eine Reise wählen.');if(!stage.value)throw Error('Bitte bestehenden oder getrennten Aufenthalt wählen.');return stage.value!=='new'?{reise_id:rid,etappe_id:Number(stage.value)}:{reise_id:rid,etappe_neu:true};}};
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
