/* Private stay photos: signed URLs stay in memory, never in app storage. */
async function tripPhotoPrepare(file){
 if(!file||!file.type.startsWith('image/'))throw Error('Bitte eine Bilddatei auswählen.');
 const source=URL.createObjectURL(file),img=new Image();
 try{
  img.src=source;try{await img.decode();}catch{throw Error('Dieses Bildformat lässt sich hier nicht öffnen. Bitte als JPEG oder PNG auswählen.');}
  const scale=Math.min(1,1600/Math.max(img.naturalWidth,img.naturalHeight)),canvas=document.createElement('canvas');
  canvas.width=Math.max(1,Math.round(img.naturalWidth*scale));canvas.height=Math.max(1,Math.round(img.naturalHeight*scale));
  const ctx=canvas.getContext('2d');if(!ctx)throw Error('Bildverarbeitung nicht verfügbar.');ctx.fillStyle='#fff';ctx.fillRect(0,0,canvas.width,canvas.height);ctx.drawImage(img,0,0,canvas.width,canvas.height);
  const data=canvas.toDataURL('image/jpeg',0.82).split(',')[1];if(!data||Math.ceil(data.length*3/4)>3*1024*1024)throw Error('Bild ist noch zu groß. Bitte ein kleineres Foto auswählen.');
  return {mime:'image/jpeg',daten_base64:data,breite:canvas.width,hoehe:canvas.height};
 }finally{URL.revokeObjectURL(source);}
}
function tripPhotos(etappeId,live,{lazy=false}={}){
 const node=el('section',{class:'stay-photos','aria-label':'Fotos zum Aufenthalt','data-stay-photos':etappeId}),list=el('div',{class:'stay-photo-strip'}),message=el('p',{class:'small',role:'status'});
 const input=el('input',{type:'file',accept:'image/*','aria-label':'Foto für Aufenthalt '+etappeId+' auswählen',class:'photo-file-input'});
 const add=el('button',{type:'button',onclick:()=>input.click()},'Foto hinzufügen'),reload=el('button',{type:'button',onclick:()=>load(true)},'Fotos neu laden');
 let photos=[],pending=false,uncertain=false,loaded=false,refreshUsed=false,viewer=null,viewedId=null;
 const active=()=>live()&&node.isConnected;
 node.append(el('h4',{},'Eure Fotos'),list,input,el('div',{class:'actions'},add,reload),message);
 function controls(){add.hidden=photos.length>=3;input.disabled=add.disabled=pending||uncertain||!loaded;reload.disabled=pending;list.querySelectorAll('button').forEach(b=>b.disabled=pending||uncertain);}
 function url(value){try{const u=new URL(value);return u.protocol==='https:'&&!u.username&&!u.password?u.href:null;}catch{return null;}}
 function photoImage(p){return el('img',{src:url(p.url),alt:p.titel||'Aufenthaltsfoto',loading:'lazy',referrerpolicy:'no-referrer',onerror:()=>{if(!active())return;if(!refreshUsed&&!pending){refreshUsed=true;void load(false);}else message.textContent='Foto nicht verfügbar. Bitte Fotos neu laden.';}});}
 function show(p){viewer?.d.close();viewedId=p.foto_id;viewer=tripDialog(p.titel||'Aufenthaltsfoto');viewer.body.append(photoImage(p));viewer.d.classList.add('stay-photo-viewer');viewer.d.addEventListener('close',()=>{viewer=null;viewedId=null;});}
 function draw(){list.replaceChildren(...photos.map(p=>el('figure',{},el('button',{type:'button','aria-label':'Foto groß öffnen',onclick:()=>show(p)},photoImage(p)),el('button',{type:'button',onclick:()=>remove(p)},'Foto löschen'))));controls();
  if(viewer){const p=photos.find(p=>p.foto_id===viewedId);if(p)viewer.body.replaceChildren(photoImage(p));else viewer.d.close();}
 }
 async function load(manual=false){if(pending||!active())return;pending=true;if(manual)refreshUsed=false;controls();message.textContent='Fotos werden geladen …';
  try{const r=await tripCall('unterkunft_fotos_lesen',{etappe_id:etappeId});if(!active())return;if(!Array.isArray(r.fotos)||r.fotos.length>3||r.fotos.some(p=>!tripId(p.foto_id)||p.etappe_id!==etappeId||!url(p.url)))throw Error('Fotos nicht vollständig lesbar.');photos=r.fotos;loaded=true;uncertain=false;message.textContent=photos.length+' von 3 Fotos';draw();}
  catch(e){if(active())message.textContent=e.message;}
  finally{pending=false;if(active())controls();}
 }
 input.onchange=async()=>{const file=input.files?.[0];input.value='';if(!file||pending||uncertain||!loaded||photos.length>=3)return;pending=true;controls();message.textContent='Foto wird verkleinert …';let sent=false;
  try{const data=await tripPhotoPrepare(file);if(!active())return;message.textContent='Foto wird hochgeladen …';sent=true;const r=await tripCall('unterkunft_foto_hochladen',{etappe_id:etappeId,...data});if(!active())return;if(!tripId(r.foto_id)||r.etappe_id!==etappeId)throw Error('Hochladen nicht eindeutig bestätigt.');pending=false;await load();}
  catch(e){if(active()){uncertain=sent;message.textContent=e.message+(sent?' Bitte Fotos neu laden; nicht erneut hochladen.':'');}}
  finally{pending=false;if(active())controls();}
 };
 function remove(p){if(pending||uncertain)return;const {d,body,status,close}=tripDialog('Foto löschen?');const yes=el('button',{type:'button',onclick:async()=>{if(pending)return;pending=true;controls();yes.disabled=true;close.disabled=true;cancel.disabled=true;
   try{const r=await tripCall('unterkunft_foto_loeschen',{foto_id:p.foto_id});if(r.ok!==true)throw Error('Löschen nicht eindeutig bestätigt.');d.close();if(!active())return;pending=false;await load();}
   catch(e){uncertain=true;status.textContent=e.message+' Bitte schließen und Fotos neu laden; keine automatische Wiederholung.';}
   finally{pending=false;close.disabled=false;cancel.disabled=false;if(active())controls();}
  }},'Endgültig löschen'),cancel=el('button',{type:'button',onclick:()=>d.close()},'Abbrechen');body.append(el('p',{},'Dieses Foto aus dem Aufenthalt entfernen?'),cancel,yes);d.addEventListener('cancel',e=>{if(pending)e.preventDefault();});}
 controls();
 queueMicrotask(()=>{if(!active())return;const details=node.closest('details');if(lazy&&details&&!details.open){details.addEventListener('toggle',()=>{if(details.open&&!loaded)void load();});}else void load();});
 return node;
}
