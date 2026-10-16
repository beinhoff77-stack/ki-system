/* Suchprofile und Reisewünsche; der Server liefert die erlaubten Kriterien. */
'use strict';
const REISE_LABEL = { staedte: 'Städtereise', erholung: 'Erholung', strand: 'Strand', tauchen: 'Tauchen', natur: 'Natur', roadtrip: 'Roadtrip' };
function sucheErweitertesFormular(form, call, live, ready, lock) {
  let catalog = null, profiles = [], loaded = false, loading = false, saving = false, uncertain = false, profileSources = null;
  const criteria = new Map(), counts = new Map();
  const select = (label, entries) => el('select', { 'aria-label': label }, entries.map(([value, text, disabled]) => el('option', { value, disabled }, text)));
  const labeled = (label, input) => el('label', {}, label, input);
  const mainType = select('Reiseart', []), sideType = select('Nebenart', []);
  const ratio = select('Mischung der Reisearten', [['30','70 % Hauptart / 30 % Nebenart'],['50','50 % / 50 %'],['frei','Anteil frei wählen']]);
  const share = el('input', { type: 'number', min: 10, max: 50, step: 1, value: 30, 'aria-label': 'Anteil der Nebenart (%)' });
  const shareLabel = labeled('Anteil der Nebenart (%)', share);
  const mixInfo = el('p', { class: 'small' });
  const formType = select('Gewünschte Unterkunftsform', []);
  const suite = el('input', { type: 'checkbox' });
  const quality = el('input', { type: 'checkbox' }); quality.checked = true;
  const note = el('input', { type: 'number', min: 0, max: 10, step: 0.1, value: 8, 'aria-label': 'Mindestnote für Qualitätsfilter (von 10)' });
  const reviews = el('input', { type: 'number', min: 0, step: 1, value: 30, 'aria-label': 'Qualitätsfilter ab Anzahl Bewertungen' });
  const tripPanel = el('section', { class: 'card stay-form-panel' }, el('h2', {}, 'Reiseart & Unterkunft'),
    el('div', { class: 'suche-grid' }, labeled('Reiseart', mainType), labeled('Nebenart', sideType), labeled('Mischung', ratio), shareLabel, labeled('Unterkunftsform', formType)),
    el('label', { class: 'check-label' }, suite, 'Suite als Wunsch'), mixInfo);
  const qualityPanel = el('section', { class: 'card stay-form-panel' }, el('h2', {}, 'Qualität der Bewertungen'),
    el('label', { class: 'check-label' }, quality, 'Qualitätsfilter anwenden'),
    el('div', { class: 'suche-grid' }, labeled('Mindestnote (von 10)', note), labeled('Ab dieser Anzahl Bewertungen', reviews)),
    el('p', { class: 'small muted' }, 'Ab dieser Bewertungsanzahl werden belegte Noten unter deiner Mindestnote aussortiert. Eigene Pflicht- und Wunschfilter unten gelten zusätzlich.'));
  const filtersPanel = el('details', { class: 'card stay-form-panel trip-criteria' }, el('summary', {}, 'Filter anpassen'),
    el('p', { class: 'small' }, 'Pflicht: Nachweislich nicht erfüllt bedeutet Ausschluss. Unbekannte Angaben bleiben in Liste B. Wünsche beeinflussen die Bewertung. „Egal“ lässt das Kriterium außer Betracht.'));
  const profileSelect = select('Suchprofil verwenden', [['','Ohne Profil / Standardwerte']]);
  const profileName = el('input', { type: 'text', maxlength: 60, 'aria-label': 'Name des Suchprofils', placeholder: 'z. B. Familienreise' });
  const notice = el('p', { class: 'small', role: 'status' });
  const sources = el('p', { class: 'small' });
  const reload = el('button', { type: 'button', onclick: () => load() }, 'Suchprofile aktualisieren');
  const save = el('button', { type: 'button', onclick: () => saveProfile() }, 'Als Profil speichern');
  const profilePanel = el('section', { class: 'card stay-form-panel search-profiles' }, el('h2', {}, 'Deine Suchprofile'),
    el('div', { class: 'suche-grid' }, labeled('Suchprofil verwenden', profileSelect), labeled('Profilname', profileName)),
    el('div', { class: 'actions' }, save, reload), notice, sources,
    el('p', { class: 'small muted' }, 'Ein Profil speichert Reisende, Budget und Wünsche. Zielort und Reisedaten bleiben bei deiner aktuellen Reise. Ein gleicher Profilname wird ersetzt.'));

  function sync() {
    const mixed = !!sideType.value;
    ratio.disabled = !mixed; shareLabel.hidden = !mixed || ratio.value !== 'frei'; share.disabled = !mixed || ratio.value !== 'frei';
    if (ratio.value !== 'frei') share.value = ratio.value;
    const part = sucheZahl(share.value);
    mixInfo.textContent = mixed && part !== null ? `${100-part} % ${REISE_LABEL[mainType.value] || mainType.value} + ${part} % ${REISE_LABEL[sideType.value] || sideType.value}. Die Aufenthaltsdauer passt die Gewichtung zusätzlich an.` : 'Städtereise. Die Aufenthaltsdauer passt die Gewichtung zusätzlich an.';
    note.disabled = reviews.disabled = !quality.checked;
    for (const [key, c] of criteria) {
      if (c.input) c.input.disabled = c.mode.value === 'egal';
      if (c.shared) c.shared.textContent = 'Wert aus „Schlafzimmer mindestens“: ' + form.elements.schlafzimmer_min.value;
    }
    for (const [block, output] of counts) {
      const modes = [...criteria.values()].filter(c => c.block === block).map(c => c.mode.value);
      output.textContent = `${modes.filter(m=>m==='pflicht').length} Pflicht · ${modes.filter(m=>m==='wunsch').length} Wunsch`;
    }
    const existing = profiles.find(p => p.name === profileName.value.trim());
    save.textContent = existing ? 'Gleichnamiges Profil ersetzen' : 'Als Profil speichern';
    save.disabled = !loaded || saving || loading || uncertain;
    reload.disabled = saving || loading; profileSelect.disabled = saving || loading || !loaded;
    sources.textContent = profileSources ? 'Quellen aus diesem Profil: ' + profileSources.map(q=>SUCHE_QUELLEN[q] || q).join(', ') : 'Quellen werden passend zum Reiseziel gewählt.';
  }
  sideType.addEventListener('change', sync); ratio.addEventListener('change', sync); share.addEventListener('input', sync);
  quality.addEventListener('change', sync); profileName.addEventListener('input', sync); form.addEventListener('input', sync);
  suite.addEventListener('change', () => { const c=criteria.get('suite'); if(c)c.mode.value=suite.checked?'wunsch':'egal'; sync(); });
  function buildCriteria(data) {
    for (const [block, title] of [['raum','Raum'],['lage','Lage'],['preis','Preis'],['bewertungen','Bewertungen'],['ausstattung','Ausstattung']]) {
      const count = el('span', { class: 'small muted' }); counts.set(block,count);
      const section = el('fieldset', { class: 'trip-filter-block' }, el('legend', {}, title, ' · ', count));
      for (const [key, spec] of Object.entries(data.kriterien_katalog[block] || {})) {
        if (!/^[a-z][a-z0-9_]{0,60}$/.test(key) || !['ja','zahl'].includes(spec?.typ) || typeof spec.label !== 'string') continue;
        const mode = select('Bedeutung: ' + spec.label, [['egal','Egal'],['wunsch','Wunsch'],...(key==='suite'?[]:[['pflicht','Pflicht']])]);
        mode.value=key==='balkon'?'wunsch':'egal';
        const input = spec.typ==='zahl' && key!=='schlafzimmer' ? el('input', { type:'number', min:0, step:['bewertungen_min'].includes(key)?1:0.1, max:key==='note_min'?10:null, 'aria-label':'Wert: '+spec.label, placeholder:'Wert eintragen' }) : null;
        const shared = key==='schlafzimmer' ? el('span',{class:'small'}) : null;
        const c={key,block,spec,mode,input,shared}; criteria.set(key,c);
        mode.addEventListener('change',()=>{ if(key==='suite')suite.checked=mode.value==='wunsch'; sync(); });
        section.append(el('div',{class:'trip-criterion'},el('span',{},spec.label),mode,input,shared));
      }
      if(block==='ausstattung')section.append(el('p',{class:'small muted'},'Ausstattung wird nur berücksichtigt, wenn die Quelle sie angibt. Suite ist immer ein Wunsch.'));
      filtersPanel.append(section);
    }
  }
  function values() {
    if (!loaded) throw new Error('Bitte zuerst Suchprofile und Filter laden.');
    const d={profil:mainType.value,unterkunftsform:formType.value,suite:suite.checked,qualitaetsfilter:quality.checked,kriterien:Object.create(null)};
    if (!catalog.reisearten.hauptart.includes(d.profil) || !catalog.unterkunftsform.includes(d.unterkunftsform)) throw new Error('Bitte Reiseart und Unterkunftsform prüfen.');
    if(sideType.value) {
      const n=sucheZahl(share.value);
      if(!catalog.reisearten.nebenart.includes(sideType.value) || !Number.isInteger(n) || n<10 || n>50)throw new Error('Nebenart-Anteil muss zwischen 10 und 50 Prozent liegen.');
      d.nebenart=sideType.value;d.nebenart_anteil=n;
    }
    const n=sucheZahl(note.value), r=sucheZahl(reviews.value);
    if(quality.checked&&(n===null||n<0||n>10||!Number.isSafeInteger(r)||r<0))throw new Error('Qualitätsfilter: Note von 0 bis 10 und eine ganze Anzahl Bewertungen eingeben.');
    if(n!==null&&n>=0&&n<=10)d.note_min=n;
    if(Number.isSafeInteger(r)&&r>=0)d.bewertungen_min=r;
    for(const [key,c] of criteria) {
      const entry={modus:c.mode.value};
      if(!['egal','wunsch','pflicht'].includes(entry.modus))throw new Error('Bitte die Bedeutung der Filter prüfen.');
      if(c.spec.typ==='zahl'&&entry.modus!=='egal') {
        entry.wert=sucheZahl(c.shared?form.elements.schlafzimmer_min.value:c.input.value);
        if(entry.wert===null||entry.wert<0||(key==='note_min'&&entry.wert>10)) { filtersPanel.open=true; c.input?.focus(); throw new Error('Bitte einen gültigen Wert für „'+c.spec.label+'“ eintragen.'); }
      }
      d.kriterien[key]=entry;
    }
    if(profileSources)d.quellen=[...profileSources];
    return d;
  }
  function applyProfile(data={}) {
    const defaults={erwachsene:2,kinder_alter:[],budget_eur:'',schlafzimmer_min:2,max_je_quelle:50,limit_usd:1.5,land:''};
    for(const [key,value] of Object.entries(defaults)) {
      const incoming=data[key]??value;
      form.elements[key].value=key==='kinder_alter'?Array.isArray(incoming)?incoming.join(', '):'':String(incoming);
    }
    mainType.value=catalog.reisearten.hauptart.includes(data.profil)?data.profil:'staedte';
    sideType.value=catalog.reisearten.nebenart.includes(data.nebenart)?data.nebenart:'';
    const n=data.nebenart_anteil??30;ratio.value=[30,50].includes(n)?String(n):'frei';share.value=n;
    formType.value=catalog.unterkunftsform.includes(data.unterkunftsform)?data.unterkunftsform:'alle';
    quality.checked=data.qualitaetsfilter!==false;note.value=data.note_min??8;reviews.value=data.bewertungen_min??30;
    for(const [key,c] of criteria) {
      const v=data.kriterien?.[key];
      c.mode.value=['pflicht','wunsch','egal'].includes(v?.modus)?key==='suite'&&v.modus==='pflicht'?'wunsch':v.modus:key==='balkon'?'wunsch':key==='suite'&&data.suite?'wunsch':'egal';
      if(c.input)c.input.value=typeof v?.wert==='number'?v.wert:'';
      if(c.shared&&c.mode.value!=='egal'&&typeof v?.wert==='number')form.elements.schlafzimmer_min.value=v.wert;
    }
    suite.checked=criteria.get('suite')?.mode.value==='wunsch';
    profileSources=Array.isArray(data.quellen)&&data.quellen.every(q=>typeof q==='string')?[...data.quellen]:null;
    form.dispatchEvent(new Event('input',{bubbles:true}));sync();
  }
  function profileOptions() {
    const previous=profileSelect.value;
    profileSelect.replaceChildren(el('option',{value:''},'Ohne Profil / Standardwerte'),...profiles.map(p=>el('option',{value:String(p.id)},p.name)));
    if(profiles.some(p=>String(p.id)===previous))profileSelect.value=previous;
  }
  profileSelect.addEventListener('change',()=>{
    const p=profiles.find(p=>String(p.id)===profileSelect.value);
    applyProfile(p?.felder||{}); profileName.value=p?.name||'';
    notice.textContent=p?`Profil „${p.name}“ übernommen. Ziel und Reisedaten sind unverändert.`:'Standardwerte übernommen. Ziel und Reisedaten sind unverändert.';sync();
  });
  async function load() {
    if(loading||saving)return; loading=true;notice.textContent='Suchprofile und Filter werden geladen …';sync();
    try {
      const r=await call('unterkunft_suchprofile_lesen');if(!live())return;
      if(r.ok!==true||!Array.isArray(r.profile)||!r.reisearten||!Array.isArray(r.reisearten.hauptart)||!Array.isArray(r.reisearten.nebenart)||!Array.isArray(r.unterkunftsform)||!r.kriterien_katalog||typeof r.kriterien_katalog!=='object')throw new Error('Suchprofile oder Kriterienkatalog unvollständig.');
      profiles=r.profile.filter(p=>Number.isSafeInteger(p?.id)&&typeof p.name==='string'&&p.felder&&typeof p.felder==='object'&&!Array.isArray(p.felder));
      if(!loaded) {
        catalog=r;
        mainType.replaceChildren(...r.reisearten.hauptart.map(v=>el('option',{value:v},REISE_LABEL[v]||v)),...(r.reisearten.hauptart_ab_v11||[]).map(v=>el('option',{value:v,disabled:true},(REISE_LABEL[v]||v)+' · ab V1.1')));
        sideType.replaceChildren(el('option',{value:''},'Keine Nebenart'),...r.reisearten.nebenart.map(v=>el('option',{value:v},REISE_LABEL[v]||v)));
        formType.replaceChildren(...r.unterkunftsform.map(v=>el('option',{value:v},({alle:'Alle',hotel:'Hotel',apartment:'Apartment',haus:'Haus'})[v]||v)));
        buildCriteria(r); loaded=true;sync();
      }
      uncertain=false;profileOptions();ready(true);notice.textContent=profiles.length?`${profiles.length} Suchprofile verfügbar.`:'Noch keine Suchprofile gespeichert.';
    } catch(e) { if(live()){notice.textContent='Suchprofile nicht geladen: '+e.message;if(!loaded)ready(false);} }
    finally {loading=false;if(live())sync();}
  }
  async function saveProfile() {
    if(saving||loading||uncertain||!loaded)return;
    const name=profileName.value.trim();if(!name||name.length>60){notice.textContent='Bitte einen Profilnamen mit 1 bis 60 Zeichen eingeben.';profileName.focus();return;}
    let data;try{data={...sucheFormDaten(form,{profileOnly:true}),...values()};}catch(e){notice.textContent=e.message;return;}
    saving=true;lock(true);sync();notice.textContent='Suchprofil wird gespeichert …';
    try {
      const r=await call('unterkunft_suchprofil_speichern',{name,felder:data});if(!live())return;
      if(r.ok!==true||!Number.isSafeInteger(r.id)||r.id<=0||r.name!==name||!r.felder||typeof r.felder!=='object'||Array.isArray(r.felder))throw new Error('Das Profil wurde nicht eindeutig bestätigt.');
      profiles=[...profiles.filter(p=>p.id!==r.id&&p.name!==name),{id:r.id,name:r.name,felder:r.felder}];profileOptions();profileSelect.value=String(r.id);
      notice.textContent=`Profil „${name}“ gespeichert.`;
    }catch(e){if(live()){uncertain=true;notice.textContent='Speichern nicht bestätigt: '+e.message+' Bitte zuerst Suchprofile aktualisieren.';}}
    finally{saving=false;if(live()){lock(false);sync();}}
  }
  ready(false);sync();
  return {profilePanel,tripPanel,qualityPanel,filtersPanel,load,values};
}
