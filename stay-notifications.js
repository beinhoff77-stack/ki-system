// Mitteilungen: keine Berechtigungsabfrage ohne bewussten Tastendruck.
let notificationRead=null, notificationReadAt=0, notificationToken=null;
function notificationLink(value){
  if(typeof value!=='string')return '#/meldungen';
  try{const target=new URL(value,location.href),base=new URL('.',location.href);if(target.origin!==base.origin||target.pathname!==base.pathname&&target.pathname!==base.pathname+'index.html')return '#/meldungen';value=target.hash;}catch{return '#/meldungen';}
  if(!/^#\/(meldungen|werkstatt|suche|reisen|etappe)(\/|$)/.test(value))return '#/meldungen';
  return value;
}
function notificationData(r){
  if(r?.ok!==true||!Number.isSafeInteger(r.ungelesen)||r.ungelesen<0||!Array.isArray(r.meldungen)||r.meldungen.some(m=>!Number.isSafeInteger(m.id)||typeof m.titel!=='string'||typeof m.text!=='string'||typeof m.gelesen!=='boolean'))throw Error('Mitteilungen unvollständig. Bitte erneut laden.');
  return r;
}
function notificationBadge(count){
  const badge=document.querySelector('#notification-count'),link=document.querySelector('#notifications-link');if(!badge||!link)return;
  badge.hidden=!count;badge.textContent=count>99?'99+':String(count||'');link.setAttribute('aria-label',count?`Mitteilungen, ${count} ungelesen`:'Mitteilungen');
}
async function notificationRefresh(force=false){
  const token=store.token;
  if(!token){notificationBadge(0);notificationToken=null;return;}
  if(notificationToken===token&&notificationRead)return notificationRead;
  if(!force&&notificationToken===token&&Date.now()-notificationReadAt<30000)return;
  notificationToken=token;notificationReadAt=Date.now();
  const request=aktion('unterkunft_meldungen_lesen',{nur_ungelesen:true,limit:1}).then(notificationData).then(r=>{if(store.token===token)notificationBadge(r.ungelesen);}).catch(()=>{/* Posteingang bietet bewusstes Wiederholen. */}).finally(()=>{if(notificationRead===request)notificationRead=null;});
  notificationRead=request;return request;
}
async function viewMeldungen(){
  const live=viewGuard();setChrome('Mitteilungen',{back:true});loading();
  const scope=el('section',{'aria-label':'Mitteilungen'}),status=el('p',{role:'status'}),list=el('div',{class:'notification-list'});
  let busy=false;
  const reload=el('button',{type:'button',onclick:load},'Aktualisieren');
  const all=el('button',{type:'button',onclick:()=>mark(null)},'Alle als gelesen markieren');
  scope.append(el('h2',{},'Mitteilungen'),el('a',{href:'#/einstellungen'},'Mitteilungen auf diesem Gerät einstellen'),el('div',{class:'actions'},reload,all),status,list);main.replaceChildren(scope);
  async function mark(id){
    if(busy)return;busy=true;scope.querySelectorAll('button').forEach(b=>b.disabled=true);
    try{const r=await aktion('unterkunft_meldungen_gelesen',id?{ids:[id]}:{alle:true});if(r?.ok!==true||!Number.isSafeInteger(r.markiert))throw Error('Lesestatus nicht bestätigt.');await load();}
    catch(e){if(live())status.textContent=e.message+' Bitte aktualisieren.';}
    finally{busy=false;if(live())scope.querySelectorAll('button').forEach(b=>b.disabled=false);}
  }
  async function load(){
    reload.disabled=true;status.textContent='Lade Mitteilungen …';
    try{const r=notificationData(await aktion('unterkunft_meldungen_lesen',{limit:200}));if(!live())return;notificationBadge(r.ungelesen);all.disabled=!r.ungelesen;
      list.replaceChildren(...r.meldungen.map(m=>el('article',{class:'card notification-item'+(m.gelesen?'':' unread'),'data-notification':m.id},el('p',{class:'small'},(m.gelesen?'Gelesen':'Neu')+' · '+sucheAbruf(m.erstellt_am)),el('h3',{},m.titel),el('p',{class:'notification-text'},m.text),el('div',{class:'actions'},m.link?el('a',{href:notificationLink(m.link)},'Öffnen'):null,!m.gelesen?el('button',{type:'button',onclick:()=>mark(m.id)},'Als gelesen markieren'):null))));
      status.textContent=r.meldungen.length?`${r.ungelesen} ungelesen`:'Keine Mitteilungen.';
    }catch(e){if(live())status.textContent=e.message;}finally{if(live())reload.disabled=false;}
  }
  await load();
}
function notificationSettings(){
  const box=el('section',{class:'card','aria-label':'Mitteilungen auf diesem Gerät'}),status=el('p',{role:'status'});
  const supported='Notification' in window&&'PushManager' in window&&'serviceWorker' in navigator;
  const ios=/iPad|iPhone|iPod/.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
  const installed=matchMedia('(display-mode: standalone)').matches||navigator.standalone===true;
  let busy=false,subscription=null;
  const name=el('input',{type:'text',maxlength:120,value:'Mein Gerät','aria-label':'Gerätename für Mitteilungen'});
  const enable=el('button',{type:'button',onclick:turnOn},'Mitteilungen einschalten');
  const disable=el('button',{type:'button',onclick:turnOff,hidden:true},'Auf diesem Gerät ausschalten');
  const test=el('button',{type:'button',disabled:true,onclick:async()=>{
    if(busy)return;setBusy(true);try{const r=await aktion('unterkunft_push_test');if(r?.ok!==true||!Number.isSafeInteger(r.meldung_id))throw Error('Testmeldung nicht bestätigt.');status.textContent='Testmeldung an verbundene Geräte angefordert. Bitte Mitteilung und Posteingang prüfen.';void notificationRefresh(true);}catch(e){status.textContent=e.message;}finally{setBusy(false);}
  }},'Testmeldung');
  function setBusy(value){busy=value;enable.disabled=value||!supported||(ios&&!installed);disable.disabled=value;test.disabled=value||!subscription;}
  async function registration(){return Promise.race([navigator.serviceWorker.ready,new Promise((_,reject)=>setTimeout(()=>reject(Error('App noch nicht bereit. Bitte neu laden.')),6000))]);}
  function show(){disable.hidden=!subscription;enable.textContent=subscription?'Mitteilungen erneut verbinden':'Mitteilungen einschalten';setBusy(false);}
  async function turnOn(){
    if(busy||!supported||(ios&&!installed))return;setBusy(true);
    try{
      // Vor jedem Netzwerkzugriff, damit iOS die direkte Nutzergeste erkennt.
      const permission=await Notification.requestPermission();if(permission!=='granted')throw Error(permission==='denied'?'Mitteilungen sind blockiert. Bitte in den Geräte- bzw. Browsereinstellungen erlauben.':'Mitteilungen wurden nicht erlaubt.');
      const r=await aktion('unterkunft_push_schluessel');if(r?.ok!==true||typeof r.public_key!=='string'||!r.public_key)throw Error('Mitteilungsschlüssel fehlt.');
      const key=Uint8Array.from(atob(r.public_key.replace(/-/g,'+').replace(/_/g,'/')),c=>c.charCodeAt(0));
      const reg=await registration();subscription=await reg.pushManager.getSubscription()||await reg.pushManager.subscribe({userVisibleOnly:true,applicationServerKey:key});
      const ack=await aktion('unterkunft_push_abo_speichern',{...subscription.toJSON(),geraet:name.value.trim()||'Mein Gerät'});
      if(ack?.ok!==true||ack.aktiv!==true)throw Error('Speichern nicht bestätigt. Bitte erneut verbinden.');
      status.textContent='Mitteilungen für dieses Gerät eingeschaltet. Mit „Testmeldung“ prüfen.';
    }catch(e){status.textContent=e.message;}finally{show();}
  }
  async function turnOff(){
    if(busy||!subscription)return;setBusy(true);
    try{const ack=await aktion('unterkunft_push_abo_speichern',{endpoint:subscription.endpoint,loeschen:true});if(ack?.ok!==true||ack.aktiv!==false)throw Error('Ausschalten nicht bestätigt.');const removed=await subscription.unsubscribe();if(removed!==true)throw Error('Server-Abo aus; Browser-Abo bitte erneut ausschalten.');subscription=null;status.textContent='Mitteilungen auf diesem Gerät ausgeschaltet.';}
    catch(e){status.textContent=e.message;}finally{show();}
  }
  box.append(el('h2',{},'Mitteilungen auf diesem Gerät'),el('p',{},'Entscheidungen, fertige Pakete und Hinweise erscheinen auch im Posteingang.'),el('p',{class:'small'},'iPhone/iPad: ab iOS 16.4. Über „Teilen → Zum Home-Bildschirm“ installieren und von dort öffnen. Die Zustellung ist nicht garantiert.'),el('label',{},'Gerätename',name),el('div',{class:'actions'},enable,disable,test),status,el('a',{href:'#/meldungen'},'Posteingang öffnen'));
  show();
  if(!supported||ios&&!installed)status.textContent=ios?'Bitte die App vom Home-Bildschirm öffnen.':'Dieser Browser unterstützt keine Push-Mitteilungen. Der Posteingang bleibt verfügbar.';
  else void registration().then(r=>r.pushManager.getSubscription()).then(s=>{if(!busy){subscription=s;show();if(s)status.textContent='Dieses Gerät hat ein Browser-Abo. Mit Testmeldung die Zustellung prüfen.';}}).catch(e=>{if(!busy)status.textContent=e.message;});
  return box;
}
document.addEventListener('visibilitychange',()=>{if(!document.hidden)void notificationRefresh();});

async function notificationSignOut(){
  if(!('serviceWorker' in navigator))return;
  const reg=await navigator.serviceWorker.getRegistration();const sub=await reg?.pushManager?.getSubscription();
  if(!sub)return;
  if(await sub.unsubscribe()!==true)throw Error('Mitteilungen konnten auf diesem Gerät nicht ausgeschaltet werden. Bitte erneut versuchen.');
  try{await aktion('unterkunft_push_abo_speichern',{endpoint:sub.endpoint,loeschen:true});}catch{/* Browser subscription is already revoked. */}
}
