/* Auffrischen: Vorschau bindet Etappe, Tage und Kriterien; Start ist idempotent. */
function refreshPrice(p){
 const node=el('div',{class:'refresh-price'}),old=sucheZahl(p.vorher?.preis_eur),now=sucheZahl(p.nachher?.preis_eur),delta=sucheZahl(p.differenz_eur);
 const comparable=p.vergleichbar===true&&p.angebot_bestaetigt===true&&['geprueft_gleich','geprueft_geaendert'].includes(p.status)&&old!==null&&now!==null;
 if(comparable){const actual=now-old;node.append(el('strong',{class:actual>0?'price-up':actual<0?'price-down':'price-same'},(actual>0?'↑ ':actual<0?'↓ ':'= ')+(p.geschaetzt?'ca. ':'')+sucheEuro(now)),el('p',{},'Vorher '+sucheEuro(old)+(delta!==null?' · '+(delta>0?'+':'')+sucheEuro(delta):'')));}
 else node.append(el('strong',{},now!==null?(p.geschaetzt?'ca. ':'')+sucheEuro(now):'Kein bestätigter aktueller Preis'),el('p',{},old!==null?'Bisheriger Preis: '+sucheEuro(old)+' · historisch':'Bisheriger Preis unbekannt'),el('p',{class:'small'},p.grund||'Angebote nicht sicher vergleichbar.'));
 if(p.kurs_effekt_eur!=null)node.append(el('p',{class:'small'},'Davon Währungseffekt: '+sucheEuro(p.kurs_effekt_eur)));
 node.append(el('p',{class:'small'},p.stand_text||'Preisstand: '+sucheAbruf(p.stand)));return node;
}
async function tripRefresh(etappe){
 const {d,body,status,close}=tripDialog('Suche auffrischen');let pending=false,timer=null,preview=null;
 const key='ks_refresh:'+etappe.id;let saved=stayRead(key,null);
 d.addEventListener('close',()=>clearTimeout(timer));d.addEventListener('cancel',e=>{if(pending)e.preventDefault();});
 const active=()=>d.isConnected;
 function busy(value){pending=value;close.disabled=value;body.querySelectorAll('button,input').forEach(n=>n.disabled=value);}
 function controls(){
  const maybe=el('input',{type:'checkbox'}),round=el('input',{type:'checkbox',checked:true});
  body.replaceChildren(el('p',{},'Favoriten prüfen und mit denselben Tagen, Personen und Kriterien weitere Unterkünfte suchen.'),el('label',{},maybe,' „Na ja“ ebenfalls prüfen'),el('label',{},round,' Neue Suchrunde einschließen'),el('button',{type:'button',class:'primary',onclick:()=>loadPreview(maybe.checked,round.checked)},'Kosten und Umfang prüfen'));
 }
 async function loadPreview(maybe,round){
  if(pending)return;busy(true);status.textContent='Kosten und Umfang werden geprüft …';
  try{const r=await tripCall('unterkunft_auffrischen_vorschau',{etappe_id:etappe.id,mit_na_ja:maybe,suchrunde:round});if(!active())return;
   if(r.laeuft_bereits){if(!tripId(r.auffrischung?.auffrischung_id))throw Error('Laufnummer fehlt.');saved={id:r.auffrischung.auffrischung_id};stayWrite(key,saved);renderRun(r.auffrischung);return;}
   if(r.ok!==true||!tripId(r.auffrischung_id)||typeof r.vorschau_id!=='string'||!Number.isSafeInteger(r.version)||!Array.isArray(r.favoriten)||!r.kosten||!r.etappe)throw Error('Vorschau unvollständig.');
   preview=r;const limit=el('input',{type:'number',min:0,max:500,step:1,value:Math.min(500,r.kosten.limit_vorschlag??0),'aria-label':'Gesamtlimit HasData-Credits'});
   body.replaceChildren(el('h3',{},r.etappe.ziel),el('p',{},fmtDate(r.etappe.anreise)+'–'+fmtDate(r.etappe.abreise)+' · '+(r.suche?.erwachsene??'?')+' Erwachsene · '+(r.suche?.kinder_alter?.length??'?')+' Kinder'),el('p',{},r.kosten.text||'Kosten bitte prüfen.'),el('label',{},'Gesamtlimit HasData-Credits',limit),el('p',{class:'small'},'Das Limit gilt gemeinsam für Favoriten und neue Suchrunde. Favoriten haben Vorrang. '+(r.suchrunde?.moeglich?'Zusätzlich bis '+fmtUsd(r.kosten.suchrunde_usd_bis||0)+' für die Suchrunde.':r.suchrunde?.grund||'Keine neue Suchrunde möglich.')),el('ul',{},r.favoriten.map(f=>el('li',{},f.name+' · '+({gezielt:'gezielte Prüfung',suchrunde:'nur über Suchrunde',nicht_pruefbar:'nicht gezielt prüfbar'}[f.pruefung]||f.pruefung)+' · '+f.kosten_credits+' Credits',f.frisch?.text?' · '+f.frisch.text:'',f.grund?el('p',{class:'small'},f.grund):null))),el('p',{},'Nicht gefunden heißt nicht ausgebucht. Deine Bewertungen bleiben erhalten.'),el('button',{type:'button',class:'primary',onclick:()=>{
     if(pending||!limit.reportValidity())return;
     saved={id:r.auffrischung_id,payload:{vorschau_id:r.vorschau_id,version:r.version,idempotenz_schluessel:crypto.randomUUID(),limit_credits:Number(limit.value),suchrunde:round&&r.suchrunde?.moeglich===true}};stayWrite(key,saved);void start();
   }},'Jetzt kostenpflichtig auffrischen'),el('button',{type:'button',onclick:controls},'Zurück'));
   status.textContent='Noch nicht gestartet.';
  }catch(e){if(active())status.textContent=e.message;}finally{if(active())busy(false);}
 }
 async function start(){
  if(pending||!saved?.payload)return;busy(true);status.textContent='Start wird bestätigt …';
  try{const r=await tripCall('unterkunft_auffrischen_starten',saved.payload);if(!active())return;if(r.ok!==true||r.auffrischung_id!==saved.id||r.auffrischung?.auffrischung_id!==saved.id)throw Error('Start nicht eindeutig bestätigt.');renderRun(r.auffrischung);}
  catch(e){if(active()){status.textContent=e.message+' Keine automatische Wiederholung. Bitte den gespeicherten Startstatus abrufen.';body.replaceChildren(el('button',{type:'button',onclick:read},'Startstatus erneut abrufen'));}}
  finally{if(active())busy(false);}
 }
 async function read(){
  if(pending||!saved?.id)return;clearTimeout(timer);busy(true);
  try{const r=await tripCall('unterkunft_auffrischen_lesen',{auffrischung_id:saved.id});if(!active())return;if(r.ok!==true||r.auffrischung?.auffrischung_id!==saved.id)throw Error('Gespeicherter Lauf nicht eindeutig bestätigt.');renderRun(r.auffrischung);}
  catch(e){if(active()){status.textContent=e.message;body.replaceChildren(el('button',{type:'button',onclick:read},'Erneut lesen'));}}
  finally{if(active())busy(false);}
 }
 function renderRun(run){
  clearTimeout(timer);refreshRememberNew(run);status.textContent=run.status_text||run.status;
  const checks=Array.isArray(run.favoriten)?run.favoriten:[],fresh=Array.isArray(run.neue_unterkuenfte)?run.neue_unterkuenfte:[];
  const valid=checks.filter(p=>p.vergleichbar===true&&p.angebot_bestaetigt===true&&['geprueft_gleich','geprueft_geaendert'].includes(p.status)&&sucheZahl(p.vorher?.preis_eur)!==null&&sucheZahl(p.nachher?.preis_eur)!==null);
  body.replaceChildren(el('p',{},fmtDate(run.anreise)+'–'+fmtDate(run.abreise)+' · Lauf #'+run.auffrischung_id),el('p',{},`${fresh.length} neue Unterkünfte · ${valid.filter(p=>sucheZahl(p.nachher.preis_eur)<sucheZahl(p.vorher.preis_eur)).length} günstiger · ${valid.filter(p=>sucheZahl(p.nachher.preis_eur)>sucheZahl(p.vorher.preis_eur)).length} teurer`),el('p',{class:'small'},'Verbraucht: '+(run.kosten?.ist_credits??'–')+' / '+(run.kosten?.limit_credits??'–')+' Credits · Suchrunde '+fmtUsd(run.kosten?.suchrunde_ist_usd)),run.suchrunde?.grund?el('p',{},run.suchrunde.grund):null,...checks.map(p=>el('article',{class:'card'},el('h3',{},p.name||'Unterkunft'),el('p',{},p.status_text||p.status),refreshPrice(p),p.fehler?el('p',{class:'err-text'},p.fehler):null)),...fresh.map(t=>el('p',{},el('strong',{},'NEU · '),t.name||'Neue Unterkunft')),el('p',{class:'small'},'Nicht gefunden heißt nicht ausgebucht. Vor dem Buchen gilt der Preis beim Anbieter.'),el('button',{type:'button',onclick:read},'Status aktualisieren'));
  if(run.status==='vorschau'&&saved?.payload)body.append(el('p',{},'Dieser Lauf ist noch nicht gestartet.'),el('button',{type:'button',onclick:start},'Start erneut bestätigen'));
  if(['fertig','teilweise','abgebrochen','verfallen'].includes(run.status)){
    body.append(el('a',{href:'#/suche/'+run.suchauftrag_id},'Ergebnisse durchsehen'),el('a',{href:'#/etappe/'+etappe.id},'Favoriten und Änderungen ansehen'),el('button',{type:'button',onclick:()=>{saved=null;stayWrite(key,null);controls();status.textContent='';}},'Neue Auffrischung vorbereiten'));
  }else if(run.status==='laeuft')timer=setTimeout(()=>{if(active())void read();},5000);
 }
 if(saved?.id)await read();else controls();
}
function refreshRememberNew(run){
 if(!tripId(run?.suchauftrag_id)||!Array.isArray(run.neue_unterkuenfte))return;
 stayWrite('ks_new_hits:'+run.suchauftrag_id,run.neue_unterkuenfte.map(t=>t.treffer_id).filter(tripId));
}
function refreshIsNew(t,searchId){const ids=stayRead('ks_new_hits:'+searchId,[]);return Array.isArray(ids)&&!['favorit','vielleicht','ausgeschlossen'].includes(t.status)&&ids.includes(t.treffer_id);}
