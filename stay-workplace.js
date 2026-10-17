/* Entscheidungsplatz je Etappe. Urteile ändern nie eine Buchung. */
async function viewDecisionPlace(arg){
  setChrome('Favoriten der Etappe',{tab:'ergebnisse',back:true});const live=viewGuard();loading();
  const r=await tripCall('unterkunft_etappe_treffer_lesen',{etappe_id:tripId(arg)});if(!live())return;
  if(!r.etappe||!Array.isArray(r.unterkuenfte))throw Error('Etappe unvollständig.');
  let full=null;
  if(tripId(r.referenz_suche_id)){try{full=await tripCall('unterkunft_suchlauf_lesen',{suchauftrag_id:r.referenz_suche_id});}catch{/* Grunddaten bleiben verfügbar. */}}
  if(!live())return;
  let refreshRun=null;
  if(tripId(r.referenz_suche_id)){try{const latest=await tripCall('unterkunft_auffrischen_lesen',{etappe_id:r.etappe.id});const run=latest.auffrischung;if(run?.suchauftrag_id===r.referenz_suche_id&&run.anreise===r.etappe.anreise&&run.abreise===r.etappe.abreise){refreshRun=run;refreshRememberNew(run);}}catch{/* Preise tragen weiterhin ihren bisherigen Zeitstand. */}}
  if(!live())return;
  const snapshot={suchauftrag:full?.suchauftrag||{...r.etappe,status:'fertig'},treffer:r.unterkuenfte.map(t=>{
    const detail=full?.treffer?.find(x=>x.treffer_id===t.treffer_id);
    const active=t.in_aktiver_variante&&r.aktive_variante_bestaetigt;
    return {...detail,...t,angebot:active?(detail?.angebot||{preis_gesamt_eur:t.preis_gesamt_eur,preis_art:t.preis_art,storno:t.storno}):{},bewertung:detail?.bewertung||{rang:t.rang,score:t.score,liste:t.liste},currentOfferUnavailable:!active};
  })};
  const scope=el('section',{class:'trips-page decision-place'}),status=el('p',{role:'status'}),toolbar=el('div',{class:'actions'}),content=el('div',{class:'decision-content'}),selected=new Set();
  let group='favorit',mode='list',pending=false,uncertain=false,lastBatch=[],undoData=null,review=null,sortKey='rang',selecting=false;
  const labels={favorit:'Favoriten',vielleicht:'Na ja',ausgeschlossen:'Weg'};
  const rows=()=>snapshot.treffer.filter(t=>t.status===group).sort((a,b)=>sucheVergleich(a,b,sortKey,1));
  const button=(label,fn)=>el('button',{type:'button',onclick:fn},label);
  const reload=button('Etappe aktualisieren',()=>render());
  const undo=button('Rückgängig',async()=>{if(pending||uncertain||!lastBatch.length)return;const saved=[...lastBatch];lastBatch=[];await move(saved,null,true);});
  const tabs=el('div',{class:'actions','aria-label':'Entscheidungsgruppen'});
  const modeButtons=el('div',{class:'actions','aria-label':'Ansichten'},...['list','table','tinder'].map(key=>button({list:'Liste',table:'Tabelle',tinder:'Durchsehen'}[key],()=>{if(pending||review?.pending)return;mode=key;draw();})));
  const sorting=el('select',{'aria-label':'Entscheidungen sortieren',onchange:e=>{sortKey=e.target.value;draw();}},...['rang','preis','name','m2','schlafzimmer'].map(k=>el('option',{value:k},{rang:'Empfohlen',preis:'Preis',name:'Name',m2:'Fläche',schlafzimmer:'Schlafzimmer'}[k])));
  const controls=el('div',{class:'decision-controls'}),sortLabel=el('label',{},'Sortieren',sorting);
  controls.append(tabs,modeButtons,sortLabel,toolbar);
  scope.append(el('a',{href:'#/reisen/'+r.etappe.reise_id},'← Zur Reise'),el('h2',{},r.etappe.ziel),el('p',{},fmtDate(r.etappe.anreise)+'–'+fmtDate(r.etappe.abreise)),controls,status,content,el('div',{class:'actions'},reload,button('Woanders gebucht',()=>tripExternalBooking(r.etappe,()=>render())),button('Suche auffrischen',()=>tripRefresh(r.etappe)),button('Keiner passt',()=>{
    const {body}=tripDialog('Andere Unterkunft finden');body.append(el('p',{},'Deine bisherigen Entscheidungen bleiben erhalten.'),button('Kriterien ändern und neu suchen',()=>tripStart(r.etappe)),button('Andere Tage als Variante suchen',()=>tripStart(r.etappe)));
  })));
  scope.append(tripPhotos(r.etappe.id,live));
  main.replaceChildren(scope);
  review=stayReview({getSnapshot:()=>snapshot,getRows:rows,getGroup:()=>group,menuItems:()=>[tabs,modeButtons],call:tripCall,live,scope,onClose:()=>{mode='list';draw();},onRefresh:()=>render(),isBlocked:()=>uncertain||pending,changed:()=>draw()});
  disposeSuche=()=>review.dispose();
  function actions(t){return el('div',{class:'actions'},...Object.entries(labels).filter(([key])=>key!==t.status).map(([key,label])=>button('Zu '+label,()=>move([{t,previous:t.status,reasons:[...(t.urteil_gruende||[])]}],key))),t.status==='favorit'&&!t.currentOfferUnavailable?button('Als gebucht markieren',()=>tripBook(t.treffer_id,r.etappe,t)):null);}
  async function move(items,target,restoring=false){
    if(pending||uncertain||review.pending)return;pending=true;scope.querySelectorAll('button,input').forEach(b=>b.disabled=true);const done=[];
    try{
      if(restoring){
        const ack=await tripCall('unterkunft_urteile_zuruecksetzen',undoData);
        if(ack.ok!==true||ack.zurueckgesetzt!==items.length)throw Error('Rücknahme nicht eindeutig bestätigt.');
        for(const item of items){const previous=undoData.eintraege.find(e=>e.treffer_id===item.t.treffer_id);item.t.status={favorit:'favorit',vielleicht:'vielleicht',weg:'ausgeschlossen',offen:'aktiv'}[previous.urteil];item.t.urteil_gruende=previous.gruende||[];item.t.eigener_rang=previous.eigener_rang;done.push(item);}
        undoData=null;selecting=false;
      }else{
        const urteil={favorit:'favorit',vielleicht:'vielleicht',ausgeschlossen:'weg',aktiv:'offen'}[target];
        const ack=await tripCall('unterkunft_urteile_sammeln',{treffer_ids:items.map(item=>item.t.treffer_id),urteil,gruende:[]});
        const restore=ack.rueckgaengig;
        if(ack.ok!==true||ack.geaendert!==items.length||ack.urteil!==urteil||restore?.aktion!=='unterkunft_urteile_zuruecksetzen'||!Array.isArray(restore.daten?.eintraege)||restore.daten.eintraege.length!==items.length||!Array.isArray(restore.daten.rueckmeldung_ids)||items.some(item=>!restore.daten.eintraege.some(e=>e.treffer_id===item.t.treffer_id&&['favorit','vielleicht','weg','offen'].includes(e.urteil))))throw Error('Änderung nicht eindeutig bestätigt.');
        undoData=restore.daten;
        for(const item of items){item.t.status=target;item.t.urteil_gruende=[];done.push(item);selected.delete(item.t.treffer_id);}
      }
      status.textContent=restoring?`${done.length} Entscheidungen zurückgenommen.`:`${done.length} Unterkünfte auf „${labels[target]}“ gesetzt.`;
    }catch(e){uncertain=true;status.textContent=`${e.message} Bitte Etappe aktualisieren; keine automatische Wiederholung.`;}
    finally{lastBatch=restoring?[]:done;pending=false;if(live()){scope.querySelectorAll('button,input').forEach(b=>b.disabled=false);draw();}}
  }
  function bulk(target){const items=rows().filter(t=>selected.has(t.treffer_id)).map(t=>({t,previous:t.status,reasons:[...(t.urteil_gruende||[])]}));if(!items.length)return;
    const {d,body}=tripDialog('Auswahl verschieben');body.append(el('p',{},`Diese ${items.length} Unterkünfte auf „${labels[target]}“ setzen?`),button('Abbrechen',()=>d.close()),button('Auf „'+labels[target]+'“ setzen',()=>{d.close();void move(items,target);}));
  }
  function draw(){
    tabs.replaceChildren(...Object.entries(labels).map(([key,label])=>el('button',{type:'button','aria-pressed':group===key,onclick:()=>{if(pending||review?.pending)return;group=key;selected.clear();draw();}},`${label} (${snapshot.treffer.filter(t=>t.status===key).length})`)));
    modeButtons.querySelectorAll('button').forEach((b,i)=>b.setAttribute('aria-pressed',String(['list','table','tinder'][i]===mode)));
    const current=rows();undo.hidden=!lastBatch.length;toolbar.replaceChildren(button(selecting?'Auswahl schließen':'Auswählen',()=>{selecting=!selecting;selected.clear();draw();}),...(selecting?[button('Alle '+current.length+' auswählen',()=>{current.forEach(t=>selected.add(t.treffer_id));draw();}),el('span',{},selected.size+' ausgewählt')]:[]),...(selected.size?Object.entries(labels).filter(([key])=>key!==group).map(([key,label])=>el('button',{type:'button',onclick:()=>bulk(key)},'Auswahl zu '+label)):[]),...(selected.size?[el('button',{type:'button',disabled:selected.size<2||selected.size>4,onclick:()=>tripCompare(snapshot.treffer.filter(t=>selected.has(t.treffer_id)))},'Vergleichen (2–4)'),button('Lage vergleichen',()=>tripSelectionMap(snapshot.treffer.filter(t=>selected.has(t.treffer_id))))]:[]),undo);
    if(mode!=='tinder'){controls.insertBefore(tabs,sortLabel);controls.insertBefore(modeButtons,sortLabel);}
    content.replaceChildren();scope.classList.toggle('tinder-mode',mode==='tinder');toolbar.hidden=mode==='tinder';
    if(mode==='tinder'){review.draw();content.append(review.node);}
    else if(mode==='table'){
      const table=el('table',{class:'decision-table'},el('thead',{},el('tr',{},['Auswahl','Unterkunft','Gesamtpreis','Fläche','Schlafzimmer','Aktionen'].map(s=>el('th',{scope:'col'},s))))),body=el('tbody');
      for(const t of current)body.append(el('tr',{},el('td',{},check(t)),el('td',{},sucheFoto(t),t.name),el('td',{},t.currentOfferUnavailable?'Für aktuelle Tage nicht gefunden':stayField(t,'preis',snapshot.suchauftrag)),el('td',{},stayField(t,'m2',snapshot.suchauftrag)),el('td',{},stayField(t,'schlafzimmer',snapshot.suchauftrag)),el('td',{},actions(t))));table.append(body);content.append(el('div',{class:'table-scroll',tabindex:0,'aria-label':'Unterkünfte vergleichen'},table));
    }else for(const t of current)content.append(el('article',{class:'card stage-stay','data-stage-hit':t.treffer_id},check(t),sucheFoto(t),el('h3',{},t.name),el('p',{},t.currentOfferUnavailable?'Für die aktuellen Tage nicht gefunden':(t.angebot.preis_art==='geschaetzt'?'ca. ':'')+sucheEuro(t.angebot.preis_gesamt_eur)+' gesamt'),el('p',{class:'small'},'Preisstand der Suche: '+sucheAbruf(t.angebot.abrufzeit)),refreshRun?.favoriten?.find(p=>p.treffer_id===t.treffer_id)?refreshPrice(refreshRun.favoriten.find(p=>p.treffer_id===t.treffer_id)):null,stayReviewInfo(t,snapshot.suchauftrag),el('p',{class:'small'},t.angebot.storno||'Stornobedingungen unbekannt'),el('a',{href:'#/suche/'+t.suchauftrag_id+'?treffer='+t.treffer_id},'Details und Suchlauf'),el('details',{},el('summary',{},'Frühere Angebote'),(t.frueher||[]).map(s=>el('p',{},fmtDate(s.anreise)+'–'+fmtDate(s.abreise)+' · '+sucheEuro(s.preis_gesamt_eur)+' damals'))),actions(t)));
    if(!current.length&&mode!=='tinder')content.append(el('p',{},'Keine Unterkünfte in „'+labels[group]+'“.'));
    if(uncertain)scope.querySelectorAll('button,input').forEach(b=>{if(b!==reload)b.disabled=true;});
  }
  function check(t){return el('input',{type:'checkbox',hidden:!selecting,checked:selected.has(t.treffer_id),'aria-label':t.name+' auswählen',onchange:e=>{if(e.target.checked)selected.add(t.treffer_id);else selected.delete(t.treffer_id);draw();}});}
  draw();
}

