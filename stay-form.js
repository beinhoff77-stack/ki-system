/* Suchprofile und Reisewünsche; der Server liefert die erlaubten Kriterien. */
'use strict';
const REISE_LABEL = { staedte: 'Städtereise', erholung: 'Erholung', strand: 'Strand', tauchen: 'Tauchen', natur: 'Natur', roadtrip: 'Roadtrip' };
function sucheErweitertesFormular(form, call, live, ready, lock, profilePreset = null, districtPreset = null) {
  let catalog = null, profiles = [], loaded = false, loading = false, saving = false, uncertain = false, profileSources = null;
  let districtForm = null;
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
    el('p', { class: 'small' }, SUCHE_SCORE_AN ? 'Pflicht: Nachweislich nicht erfüllt bedeutet Ausschluss. Unbekannte Angaben bleiben unter „Angaben offen“. Wünsche beeinflussen die Bewertung. „Egal“ lässt das Kriterium außer Betracht.' : 'Pflicht: Nachweislich nicht erfüllt bedeutet Ausschluss. Unbekannte Angaben bleiben unter „Angaben offen“. „Egal“ lässt das Kriterium außer Betracht.'));
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
      if (c.shared) {
        form.elements.schlafzimmer_min.disabled = c.mode.value === 'egal';
        c.shared.textContent = c.mode.value === 'egal' ? 'Egal: keine Schlafzimmer-Vorgabe, auch Einzimmer-Angebote.' : 'Wert aus „Schlafzimmer mindestens“: ' + form.elements.schlafzimmer_min.value;
      }
    }
    for (const [block, output] of counts) {
      const modes = [...criteria.values()].filter(c => c.block === block).map(c => c.mode.value);
      if (block === 'viertel' && districtForm) modes.push(districtForm.modus());
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
    for (const [block, title] of [['raum','Raum'],['lage','Lage'],['viertel','Viertel'],['preis','Preis'],['bewertungen','Bewertungen'],['ausstattung','Ausstattung']]) {
      if (block === 'viertel' && !data.kriterien_katalog.viertel) continue;
      const count = el('span', { class: 'small muted' }); counts.set(block,count);
      const section = el('fieldset', { class: 'trip-filter-block' }, el('legend', {}, title, ' · ', count));
      if (block === 'viertel' && data.kriterien_katalog.viertel.viertel_auswahl?.typ === 'liste') {
        districtForm = sucheViertelForm(form, call, live, sync); section.append(districtForm.node);
      }
      for (const [key, spec] of Object.entries(data.kriterien_katalog[block] || {})) {
        if (!/^[a-z][a-z0-9_]{0,60}$/.test(key) || !['ja','zahl'].includes(spec?.typ) || typeof spec.label !== 'string') continue;
        if(!SUCHE_SCORE_AN&&key==='suite')continue; // Suite ist nur ein Wunsch (Score) – vorerst aus
        const wunschErlaubt=SUCHE_SCORE_AN||key==='schlafzimmer';
        const mode = select('Bedeutung: ' + spec.label, [['egal','Egal'],...(wunschErlaubt?[['wunsch','Wunsch']]:[]),...(key==='suite'?[]:[['pflicht','Pflicht']])]);
        mode.value=(SUCHE_SCORE_AN?['balkon','schlafzimmer']:['schlafzimmer']).includes(key)?'wunsch':'egal';
        const input = spec.typ==='zahl' && key!=='schlafzimmer' ? el('input', { type:'number', min:0, step:['bewertungen_min'].includes(key)?1:0.1, max:key==='note_min'||block==='viertel'?10:null, value:block==='viertel'?5:null, 'aria-label':'Wert: '+spec.label, placeholder:'Wert eintragen' }) : null;
        const shared = key==='schlafzimmer' ? el('span',{class:'small'}) : null;
        const c={key,block,spec,mode,input,shared}; criteria.set(key,c);
        mode.addEventListener('change',()=>{ if(key==='suite')suite.checked=mode.value==='wunsch'; sync(); });
        section.append(el('div',{class:'trip-criterion','data-key':key,hidden:(key==='schlafzimmer'&&form.dataset.wohnen==='1')||(!SUCHE_SCORE_AN&&MASKE_KEYS.has(key))},el('span',{},spec.label),mode,input,shared));
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
        if(entry.wert===null||entry.wert<0||((key==='note_min'||c.block==='viertel')&&entry.wert>10)) { filtersPanel.open=true; c.input?.focus(); throw new Error('Bitte einen gültigen Wert für „'+c.spec.label+'“ eintragen.'); }
      }
      d.kriterien[key]=entry;
    }
    if (districtForm) { try { d.kriterien.viertel_auswahl = districtForm.value(); } catch(e) { filtersPanel.open = true; throw e; } }
    if(profileSources)d.quellen=[...profileSources];
    if(typeof form.wohnenWerte==='function')Object.assign(d,form.wohnenWerte()); // W96
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
      c.mode.value=['pflicht','wunsch','egal'].includes(v?.modus)?key==='suite'&&v.modus==='pflicht'?'wunsch':v.modus:['balkon','schlafzimmer'].includes(key)?'wunsch':key==='suite'&&data.suite?'wunsch':'egal';
      if(![...c.mode.options].some(o=>o.value===c.mode.value))c.mode.value='egal'; // Wunsch ohne Score nicht verfügbar
      if(c.input)c.input.value=typeof v?.wert==='number'?v.wert:c.block==='viertel'?5:'';
      if(c.shared&&c.mode.value!=='egal'&&typeof v?.wert==='number')form.elements.schlafzimmer_min.value=v.wert;
    }
    suite.checked=criteria.get('suite')?.mode.value==='wunsch';
    districtForm?.apply(data.kriterien?.viertel_auswahl);
    profileSources=Array.isArray(data.quellen)&&data.quellen.every(q=>typeof q==='string')?[...data.quellen]:null;
    form.wohnenProfil?.(data); // W96
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
        buildCriteria(r); loaded=true;sync(); form.dispatchEvent(new Event('kriterien-geladen'));
      }
      uncertain=false;profileOptions();ready(true);notice.textContent=profiles.length?`${profiles.length} Suchprofile verfügbar.`:'Noch keine Suchprofile gespeichert.';
      if (profilePreset !== null) {
        const preset = profiles.find(p => String(p.id) === String(profilePreset)); profilePreset = null;
        if (preset) { profileSelect.value = String(preset.id); profileSelect.dispatchEvent(new Event('change')); }
        else notice.textContent = 'Das ausgewählte Profil ist nicht mehr verfügbar. Bitte ein anderes wählen.';
      }
      if (districtPreset !== null) {
        if (districtForm) { districtForm.apply(districtPreset); filtersPanel.open = true; void districtForm.load(); }
        else { ready(false); throw new Error('Der Server unterstützt die gewählte Viertelauswahl noch nicht.'); }
        districtPreset = null;
      }
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
  // W100: Zugriff für die Suchmaske – sie liest und schreibt direkt die Filterzeilen (eine Quelle der Wahrheit)
  const kriterien = {
    geladen: () => loaded,
    hat: key => criteria.has(key),
    get: key => { const c = criteria.get(key); return c ? { modus: c.mode.value, wert: c.input ? c.input.value : null } : null; },
    set: (key, modus, wert) => { const c = criteria.get(key); if (!c) return;
      if ([...c.mode.options].some(o => o.value === modus)) c.mode.value = modus;
      if (c.input && wert !== undefined) c.input.value = wert === null ? '' : String(wert);
      sync(); form.dispatchEvent(new Event('maske-geaendert')); },
  };
  return {profilePanel,tripPanel,qualityPanel,filtersPanel,load,values,kriterien};
}

// W94 (Claude): Nachtband – Preisniveau je Nacht (Trivago je Nacht, Server: unterkunft_flex modus nachtband).
// Grün normal, Gelb teurer (ab +30 %), Rot sehr teuer (ab +60 %), Grau nicht geprüft. Vergleich mit den anderen Nächten des Zeitraums.
const NB_TEXT = { gruen: 'normal', gelb: 'teurer', rot: 'sehr teuer', ungeprueft: 'nicht geprüft', laeuft: 'wird geprüft' };
const NB_TAG = ['', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'];
function nachtbandAnzeige({ form, call, live, onShow = () => {} }) {
  const box = el('div', { class: 'night-band', hidden: true, 'aria-live': 'polite' });
  let timer = null, poll = null, seq = 0, lastKey = '';
  let vorher = null; // W95: Daten vor dem Antippen eines Vorschlags (für „Wie vorher“)
  const tag = d => { const x = new Date(d + 'T12:00:00'); return Number.isNaN(x.getTime()) ? d : x.toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' }); };
  const prozent = i => { const p = Math.round((Number(i) - 1) * 100); return i !== null && Number.isFinite(p) ? (p > 0 ? '+' : '') + p + ' %' : ''; };
  const euro = v => v !== null && v !== undefined && Number.isFinite(Number(v)) ? Math.round(Number(v)).toLocaleString('de-DE') + ' €' : '';
  function params() {
    const f = new FormData(form);
    const ziel = String(f.get('ziel') || '').trim(), anreise = String(f.get('anreise') || ''), abreise = String(f.get('abreise') || '');
    const n = (Date.parse(abreise) - Date.parse(anreise)) / 86400000;
    const heute = new Date().toISOString().slice(0, 10);
    if (ziel.length < 2 || !/^\d{4}-\d{2}-\d{2}$/.test(anreise) || !/^\d{4}-\d{2}-\d{2}$/.test(abreise) || !(n >= 2 && n <= 35) || abreise <= heute) return null;
    const kinder = String(f.get('kinder_alter') || '').split(',').map(v => v.trim()).filter(v => /^\d{1,2}$/.test(v)).map(Number);
    return { modus: 'nachtband', ziel, anreise, abreise, erwachsene: Number(f.get('erwachsene')) || 2, kinder_alter: kinder };
  }
  function hide() { box.hidden = true; box.replaceChildren(); onShow(false); }
  function draw(r) {
    const naechte = Array.isArray(r?.naechte) ? r.naechte.filter(x => x && typeof x.nacht === 'string') : [];
    if (!naechte.length) return hide();
    const stufe = x => NB_TEXT[x.stufe] ? x.stufe : 'ungeprueft';
    const laeuft = naechte.some(x => x.stufe === 'laeuft');
    const auffaellig = naechte.filter(x => x.stufe === 'gelb' || x.stufe === 'rot');
    const geprueft = naechte.filter(x => ['gruen', 'gelb', 'rot'].includes(x.stufe)).length;
    const feier = x => Array.isArray(x.feiertage) && x.feiertage.length ? ' · vor Feiertag: ' + x.feiertage.join(', ') : '';
    const titel = x => `${NB_TAG[x.wochentag] || ''} ${tag(x.nacht)}: ${NB_TEXT[stufe(x)]}${x.index != null && x.stufe !== 'laeuft' ? ' (' + prozent(x.index) + ')' : ''}${x.median_eur != null ? ' · Ø ' + euro(x.median_eur) + '/Nacht' : ''}${feier(x)}`;
    const strip = el('div', { class: 'nb-strip', role: 'list', 'aria-label': 'Preisniveau je Nacht' },
      naechte.map(x => el('span', { role: 'listitem', tabindex: '0', class: `nb-cell nb-${stufe(x)}${x.wochentag === 5 || x.wochentag === 6 ? ' nb-we' : ''}`, title: titel(x), 'aria-label': titel(x) })));
    let lage;
    if (laeuft) lage = `wird geprüft … ${geprueft}/${naechte.length}`;
    else if (!geprueft) lage = 'gerade nicht verfügbar';
    else if (!auffaellig.length) lage = 'keine teuren Nächte';
    else lage = `${auffaellig.length} ${auffaellig.length === 1 ? 'Nacht' : 'Nächte'} teurer`;
    const kurzListe = auffaellig.slice().sort((a, b) => (a.nacht < b.nacht ? -1 : 1));
    const liste = !laeuft && kurzListe.length ? el('p', { class: 'nb-notes small' }, 'Teurer: ', kurzListe.slice(0, 4).map((x, k) => [k ? ', ' : '',
      el('span', { class: `nb-dot nb-${x.stufe}`, 'aria-hidden': 'true' }), el('strong', {}, `${NB_TAG[x.wochentag] || ''} ${tag(x.nacht)}`), ` ${prozent(x.index)}`,
      Array.isArray(x.feiertage) && x.feiertage.length ? el('span', { class: 'nb-holiday' }, ` (vor ${x.feiertage.join(', ')})`) : '']).flat(),
      kurzListe.length > 4 ? ` und ${kurzListe.length - 4} weitere` : '', ' (Feld antippen)') : null;
    const zeit = r?.abgerufen_am ? new Date(r.abgerufen_am) : null;
    const info = el('div', { class: 'nb-info', hidden: true },
      el('p', { class: 'nb-legend small' }, ['gruen', 'gelb', 'rot', 'ungeprueft'].map(s => el('span', {}, el('span', { class: `nb-dot nb-${s}`, 'aria-hidden': 'true' }),
        { gruen: 'Normal', gelb: 'Teurer (ab +30 %)', rot: 'Sehr teuer (ab +60 %)', ungeprueft: 'Nicht geprüft' }[s]))),
      el('p', { class: 'nb-source small muted' }, `Trivago, je Nacht ca. 25 Unterkünfte für deine Belegung, verglichen mit den anderen Nächten deines Zeitraums${zeit && !Number.isNaN(zeit.getTime()) ? ' · Stand ' + zeit.toLocaleTimeString('de-DE', { hour: '2-digit', minute: '2-digit' }) : ''}. Zeigt Preise, nicht ob noch frei ist. Feiertage sind nur ein möglicher Grund. Schwellen sind Erfahrungswerte.`));
    const infoBtn = el('button', { type: 'button', class: 'nb-info-btn', 'aria-expanded': 'false', 'aria-label': 'Farben und Quelle erklären', onclick: () => { info.hidden = !info.hidden; infoBtn.setAttribute('aria-expanded', String(!info.hidden)); } }, 'i');
    const n = naechte.length;
    const row = el('div', { class: 'nb-row' }, el('span', { class: 'nb-date small muted' }, tag(naechte[0].nacht)), strip, el('span', { class: 'nb-date small muted' }, tag(naechte[n - 1].nacht)));
    box.hidden = false;
    box.replaceChildren(el('div', { class: 'nb-head' }, el('strong', {}, `${n} ${n === 1 ? 'Nacht' : 'Nächte'}`), el('span', { class: 'nb-state small' }, ' · Preise: ' + lage), infoBtn), row, liste, varianten(r), info);
    const tip = c => { box.querySelector('.nb-tip')?.remove(); row.after(el('p', { class: 'nb-tip small' }, c.getAttribute('aria-label'))); };
    for (const c of strip.children) { c.addEventListener('click', () => tip(c)); c.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); tip(c); } }); }
    onShow(true);
  }
  // W95: ± Tage – bis zu zwei bessere Reisedaten (Schätzung aus den Nachtpreisen), Antippen übernimmt die Daten.
  const spanne = (a, b) => `${tag(a)}–${tag(b)}`;
  function setzeDaten(anreise, abreise) {
    for (const [k, v] of [['anreise', anreise], ['abreise', abreise]]) { const i = form.querySelector(`[name="${k}"]`); if (i) { i.value = v; i.dispatchEvent(new Event('input', { bubbles: true })); } }
  }
  function varianten(r) {
    const v = r?.varianten; if (!v || typeof v !== 'object') return null;
    const g = v.grenzen || {};
    const fest = [g.anreise_fest ? 'Anreise fest: ' + (g.anreise_grund || 'gebuchter Aufenthalt davor') : null, g.abreise_fest ? 'Abreise fest: ' + (g.abreise_grund || 'gebuchter Aufenthalt danach') : null].filter(Boolean).join(' · ');
    const f = new FormData(form), jetzt = { anreise: String(f.get('anreise') || ''), abreise: String(f.get('abreise') || '') };
    const zurueck = vorher && (vorher.anreise !== jetzt.anreise || vorher.abreise !== jetzt.abreise)
      ? el('button', { type: 'button', class: 'nb-chip nb-chip-back', onclick: () => { const z = vorher; vorher = null; setzeDaten(z.anreise, z.abreise); } }, el('strong', {}, '↶ Wie vorher'), el('span', {}, `${spanne(vorher.anreise, vorher.abreise)} · ${vorher.naechte} N.`)) : null;
    if (v.status === 'laeuft') return el('p', { class: 'nb-alt small muted' }, 'Andere Daten werden geprüft …');
    if (v.status === 'fest') return el('p', { class: 'nb-alt small muted' }, fest ? fest + '.' : 'Daten fest.');
    if (v.status !== 'fertig') return zurueck ? el('div', { class: 'nb-alt' }, el('div', { class: 'nb-chips' }, zurueck)) : null;
    const liste = Array.isArray(v.vorschlaege) ? v.vorschlaege.filter(x => x && /^\d{4}-\d{2}-\d{2}$/.test(x.anreise) && /^\d{4}-\d{2}-\d{2}$/.test(x.abreise)) : [];
    const geplant = v.geplant || {};
    const pruef = `Anreise ±${g.spanne_anreise ?? 2} Tage, Dauer ±${g.spanne_dauer ?? 1} Nacht geprüft`;
    if (!liste.length) return el('div', { class: 'nb-alt' }, el('p', { class: 'small muted nb-alt-text' }, `Andere Daten bringen nichts (${pruef}).${fest ? ' ' + fest + '.' : ''}`), zurueck ? el('div', { class: 'nb-chips' }, zurueck) : null);
    const chips = liste.map(x => {
      const p = Number(x.ersparnis_nacht_prozent), grund = [x.meidet ? 'ohne ' + x.meidet : null, Number.isFinite(p) && p !== 0 ? `${p > 0 ? '−' : '+'}${Math.abs(p)} %` : null].filter(Boolean).join(' · ');
      const aenderung = [x.verschiebung_tage ? `${Math.abs(x.verschiebung_tage)} Tag${Math.abs(x.verschiebung_tage) === 1 ? '' : 'e'} ${x.verschiebung_tage < 0 ? 'früher' : 'später'}` : null, x.dauer_aenderung ? `${Math.abs(x.dauer_aenderung)} Nacht ${x.dauer_aenderung < 0 ? 'weniger' : 'mehr'}` : null].filter(Boolean).join(', ');
      return el('button', { type: 'button', class: 'nb-chip', 'aria-label': `Daten übernehmen: ${spanne(x.anreise, x.abreise)}, ${x.naechte} Nächte, ${aenderung}, geschätzt Ø ${euro(x.schnitt_eur)} pro Nacht${grund ? ', ' + grund : ''}`,
        onclick: () => { vorher = { ...jetzt, naechte: geplant.naechte ?? '' }; setzeDaten(x.anreise, x.abreise); } },
        el('span', {}, el('strong', {}, `${spanne(x.anreise, x.abreise)} · ${x.naechte} N.`), ` · Ø ${euro(x.schnitt_eur)}`), el('span', { class: 'nb-chip-sub' }, [aenderung, grund].filter(Boolean).join(' · ')));
    });
    return el('div', { class: 'nb-alt' }, el('p', { class: 'small nb-alt-text' }, el('strong', {}, 'Bessere Daten?'), ` Geplant Ø ${euro(geplant.schnitt_eur)} (geschätzt)`),
      el('div', { class: 'nb-chips' }, chips, zurueck), fest ? el('p', { class: 'small muted nb-alt-text' }, fest + '.') : null);
  }
  async function load(p, nurLesen, mine, runde = 0) {
    let r;
    try { r = await call('unterkunft_flex', nurLesen ? { ...p, nur_lesen: true } : p); } catch { r = null; }
    if (!live() || mine !== seq) return;
    if (!r || !Array.isArray(r.naechte)) return hide();
    draw(r);
    if (r.laeuft && runde < 30) poll = setTimeout(() => load(p, true, mine, runde + 1), runde < 5 ? 2500 : 4000);
  }
  function update() {
    const p = params(), key = p ? JSON.stringify(p) : '';
    if (key === lastKey) return;
    lastKey = key; clearTimeout(timer); clearTimeout(poll); seq++;
    if (!p) return hide();
    const mine = seq;
    timer = setTimeout(() => load(p, false, mine), 900);
  }
  form.addEventListener('input', update); form.addEventListener('change', update);
  update();
  return { node: box, update };
}

// W96 (Claude): Block „Wohnen“ – Apartment/Hotel als Umschalter, ★ = bevorzugt (nur wenn beide an), Schlafzimmer –/+ für Apartments,
// Hotel mit Zimmeranzahl –/+ und Bett je Zimmer. Alles antippen, nichts tippen. Server: Feld „wohnen“ (W97); schlafzimmer_min bleibt für ältere Wege gesetzt.
const WOHNEN_STANDARD = { apartment: { an: true, schlafzimmer_min: 1 }, hotel: { an: false, zimmer: 2, bett: 'doppel' }, bevorzugt: 'apartment' };
const WOHNEN_BETT = { doppel: 'Doppelbett', einzel: '2 Einzel', egal: 'egal' };
function wohnenNormal(w) {
  const s = JSON.parse(JSON.stringify(WOHNEN_STANDARD));
  if (!w || typeof w !== 'object') return s;
  const zahl = (v, min, max, d) => { const n = Number(v); return Number.isInteger(n) && n >= min && n <= max ? n : d; };
  s.apartment.an = w.apartment?.an !== false; s.apartment.schlafzimmer_min = zahl(w.apartment?.schlafzimmer_min, 0, 6, 1);
  s.hotel.an = w.hotel?.an === true; s.hotel.zimmer = zahl(w.hotel?.zimmer, 1, 4, 2); s.hotel.bett = WOHNEN_BETT[w.hotel?.bett] ? w.hotel.bett : 'doppel';
  if (!s.apartment.an && !s.hotel.an) s.apartment.an = true;
  s.bevorzugt = w.bevorzugt === 'hotel' && s.hotel.an ? 'hotel' : s.apartment.an ? 'apartment' : 'hotel';
  return s;
}
function wohnenKurz(w) {
  const teile = [];
  const sz = n => n === 0 ? 'auch Einzimmer' : `ab ${n} SZ`;
  if (w.apartment.an) teile.push(`Apartment ${sz(w.apartment.schlafzimmer_min)}${w.hotel.an && w.bevorzugt === 'apartment' ? ' ★' : ''}`);
  if (w.hotel.an) teile.push(`Hotel ${w.hotel.zimmer} ${w.hotel.bett === 'doppel' ? 'DZ' : w.hotel.bett === 'einzel' ? 'Zi. (2 Einzel)' : 'Zi.'}${w.apartment.an && w.bevorzugt === 'hotel' ? ' ★' : ''}`);
  return teile.join(' · ');
}
function wohnenBlock(form, szInput = null) {
  let w = wohnenNormal(stayRead('ks_wohnen_last', null));
  const box = el('div', { class: 'wohnen', role: 'group', 'aria-label': 'Wohnen' });
  const schritt = (label, wert, min, max, setze, einheit) => el('span', { class: 'wo-stepper', role: 'group', 'aria-label': label },
    el('button', { type: 'button', class: 'wo-step', 'aria-label': label + ' weniger', disabled: wert <= min, onclick: () => setze(wert - 1) }, '–'),
    el('output', { class: 'wo-step-value', 'aria-live': 'polite', 'aria-label': label + ': ' + wert }, `${wert} ${einheit}`),
    el('button', { type: 'button', class: 'wo-step', 'aria-label': label + ' mehr', disabled: wert >= max, onclick: () => setze(wert + 1) }, '+'));
  function feld() { const i = szInput || form.querySelector('[name="schlafzimmer_min"]'); if (i) { i.value = String(w.apartment.an ? w.apartment.schlafzimmer_min : 0); } }
  function aendern(f) { f(); w = wohnenNormal(w); feld(); draw(); form.dispatchEvent(new Event('input', { bubbles: true })); }
  function chip(art, label, extra = null) {
    const an = w[art].an, beide = w.apartment.an && w.hotel.an, bevorzugt = w.bevorzugt === art;
    return el('span', { class: 'wo-chip-wrap' + (an ? ' is-on' : '') },
      el('button', { type: 'button', class: 'wo-chip', 'aria-pressed': String(an), onclick: () => aendern(() => {
        const ander = art === 'apartment' ? 'hotel' : 'apartment';
        if (an && !w[ander].an) return; // mindestens eine Wohnform bleibt an
        w[art].an = !an; if (!w[art].an && w.bevorzugt === art) w.bevorzugt = ander;
      }) }, stayIcon(art === 'hotel' ? 'hotel' : 'haus'), an ? '✓ ' : '', label),
      beide && SUCHE_SCORE_AN ? el('button', { type: 'button', class: 'wo-star' + (bevorzugt ? ' is-on' : ''), 'aria-pressed': String(bevorzugt), 'aria-label': label + ' bevorzugen', title: bevorzugt ? label + ' ist bevorzugt' : label + ' bevorzugen',
        onclick: () => aendern(() => { w.bevorzugt = art; }) }, bevorzugt ? '★' : '☆') : null, extra);
  }
  function draw() {
    // Eine Zeile im Normalfall: [✓ Apartment – 1 SZ +] [Hotel]; ist Hotel an: [✓ Hotel – 2 Zi. +] und darunter Bett je Zimmer.
    const sz = w.apartment.an ? schritt('Schlafzimmer mind.', w.apartment.schlafzimmer_min, 0, 6, n => aendern(() => { w.apartment.schlafzimmer_min = n; }), 'SZ') : null;
    const zi = w.hotel.an ? schritt('Zimmer', w.hotel.zimmer, 1, 4, n => aendern(() => { w.hotel.zimmer = n; }), 'Zi.') : null;
    const zeile = el('div', { class: 'wo-row' }, chip('apartment', 'Apartment', sz), chip('hotel', 'Hotel', zi));
    const bett = w.hotel.an ? el('div', { class: 'wo-row wo-sub' }, el('span', { class: 'wo-sub-name' }, stayIcon('bett'), 'Bett je Hotelzimmer'),
      el('span', { class: 'wo-seg', role: 'group', 'aria-label': 'Bett je Zimmer' }, Object.entries(WOHNEN_BETT).map(([k, t]) =>
        el('button', { type: 'button', class: 'wo-seg-btn', 'aria-pressed': String(w.hotel.bett === k), onclick: () => aendern(() => { w.hotel.bett = k; }) }, t)))) : null;
    const hinweis = SUCHE_SCORE_AN && w.apartment.an && w.hotel.an ? el('p', { class: 'wo-hint small muted', title: `${w.bevorzugt === 'hotel' ? 'Apartments' : 'Hotels'} kommen nur nach vorn, wenn sie deutlich günstiger oder besser bewertet sind.` }, `★ = bevorzugt · ${w.bevorzugt === 'hotel' ? 'Apartments' : 'Hotels'} nur, wenn klar günstiger/besser`) : null;
    box.replaceChildren(...[zeile, bett, hinweis].filter(Boolean));
  }
  feld(); draw();
  form.addEventListener('submit', () => stayWrite('ks_wohnen_last', w), true);
  return {
    node: box,
    werte: () => ({ wohnen: wohnenNormal(w) }),
    kurz: () => wohnenKurz(w),
    setzen(neu) { w = wohnenNormal(neu); feld(); draw(); },
    ausSchlafzimmer(n) { if (Number.isInteger(n) && n >= 0 && n <= 6) { w.apartment.schlafzimmer_min = n; w = wohnenNormal(w); feld(); draw(); } },
    feld,
  };
}

// W93 (Claude): Suchseite auf einen Bildschirm – Lücke antippen, Wo/Wann/Wer, Suchen. Alles Weitere unter „Mehr Optionen“.
function sucheSchnellLayout({ form, fields, sections, extended, submit, call, live, onTrip }) {
  const label = name => form.querySelector(`[name="${name}"]`)?.closest('label');
  const panel = nr => [...sections.children].find(p => p.querySelector('.step-number')?.textContent === nr);
  const setLabel = (name, text) => { const l = label(name); if (l?.firstChild?.nodeType === 3) l.firstChild.textContent = text; };
  setLabel('ziel', 'Wo?'); setLabel('anreise', 'Anreise'); setLabel('abreise', 'Abreise');
  const nights = el('p', { class: 'quick-nights', 'aria-live': 'polite' });
  const whoText = el('span', { class: 'who-text' }), whoPanel = el('div', { class: 'who-panel', hidden: true });
  const who = el('button', { type: 'button', class: 'who-chip', 'aria-expanded': 'false', onclick: () => { whoPanel.hidden = !whoPanel.hidden; who.setAttribute('aria-expanded', String(!whoPanel.hidden)); } }, el('span', { class: 'who-label' }, 'Wer & Budget'), whoText, el('span', { class: 'who-edit', 'aria-hidden': 'true' }, 'ändern'));
  for (const nr of ['02', '03']) { const p = panel(nr); if (p) { p.querySelector('h2')?.remove(); whoPanel.append(...p.children); } }
  const tripLine = el('p', { class: 'quick-trip small' });
  const cost = el('span', { class: 'quick-cost' });
  submit.textContent = 'Unterkünfte suchen';
  const when = el('div', { class: 'quick-when' }, label('anreise'), label('abreise'));
  const band = nachtbandAnzeige({ form, call, live, onShow: v => { nights.hidden = v; } });
  // W96: Wohnen ersetzt „Schlafzimmer mindestens“ (Wer & was), die Zeile in „Filter anpassen“ und die Unterkunftsform-Auswahl
  form.dataset.wohnen = '1';
  const wohnen = wohnenBlock(form, whoPanel.querySelector('[name="schlafzimmer_min"]'));
  form.wohnenWerte = wohnen.werte;
  form.wohnenProfil = data => { if (data?.wohnen) wohnen.setzen(data.wohnen); else if (Number.isInteger(data?.schlafzimmer_min)) wohnen.ausSchlafzimmer(data.schlafzimmer_min); else wohnen.feld(); };
  const szLabel = whoPanel.querySelector('[name="schlafzimmer_min"]')?.closest('label'); if (szLabel) szLabel.hidden = true;
  const formLabel = extended.tripPanel.querySelector('select[aria-label="Gewünschte Unterkunftsform"]')?.closest('label'); if (formLabel) formLabel.hidden = true;
  // W100: ohne Score Budget pro Nacht und die Suchmaske mit angehefteten Kriterien
  const gesamtFeld = whoPanel.querySelector('[name="budget_eur"]');
  const budgetNacht = !SUCHE_SCORE_AN && gesamtFeld ? sucheBudgetNacht(form, gesamtFeld) : null;
  if (budgetNacht) gesamtFeld.closest('label').before(budgetNacht.node);
  const maske = !SUCHE_SCORE_AN && extended.kriterien ? sucheMaske({ form, extended }) : null;
  // W101: Viertel vorab ansehen – direkt unter „Wo?“ (bisher nur versteckt unter Mehr Optionen)
  const viertelLink = el('button', { type: 'button', class: 'link-button viertel-link', hidden: true, title: 'Wo wohnen? Viertel ansehen', onclick: () => { const z = form.querySelector('[name="ziel"]')?.value.trim(); if (z) route('viertel', '?' + new URLSearchParams({ stadt: z })); } }, 'Viertel');
  form.addEventListener('input', e => { if (e.target?.name === 'ziel') viertelLink.hidden = (e.target.value || '').trim().length < 2; });
  const zielLabel = el('div', { class: 'mit-viertel a-zeile' }, el('span', { class: 'a-zeile-ikon' }, stayIcon('pin')), label('ziel'), viertelLink);
  // W102 (Sebastian 20.10.: „unübersichtlich, nicht kompakt“): feste Reihenfolge in drei Blöcken –
  // 1 Wo & Wann (am Rechner eine Zeile) · 2 Wohnen & Wer (eine Zeile) · 3 Wichtig für dich (Chip-Fläche) · Suchknopf bleibt sichtbar.
  const kopf = el('div', { class: 'quick-kopf' }, el('h2', {}, 'Unterkunft suchen'), el('p', { class: 'quick-meta small' }, tripLine));
  who.prepend(el('span', { class: 'a-zeile-ikon' }, stayIcon('personen'))); who.classList.add('a-zeile');
  submit.prepend(stayIcon('lupe'));
  when.classList.add('dr-felder'); // W103: echte Datumsfelder bleiben im Formular, bedient wird „Wann?“
  const ortZeit = el('div', { class: 'quick-block quick-ortzeit a-reise' }, zielLabel, when);
  // W103 (Sebastian 20.10.): Wohnform (Apartment/Schlafzimmer, Hotel/Zimmer, Bett) gehört zu den Kriterien – steht in „Wichtig für dich“ vorne
  if (maske) { maske.wohnenSlot.append(wohnen.node); wohnen.node.classList.add('wohnen-in-maske'); }
  const werWohnen = el('div', { class: 'quick-block quick-werwohnen' }, maske ? null : wohnen.node);
  ortZeit.append(who); // W104: Wo / Wann / Wer in einer Karte
  const quick = el('section', { class: 'card quick-search' }, kopf, ortZeit, band.node, whoPanel, werWohnen, maske ? maske.node : null, submit);
  const more = el('details', { class: 'card more-options' }, el('summary', {}, 'Mehr Optionen'), el('p', { class: 'small muted' }, (SUCHE_SCORE_AN ? 'Reiseart, Unterkunftsform, ' : '') + 'Suchprofile, Aufenthalt, Quellen, Suchkosten und Qualität. Die Standardwerte passen für die meisten Suchen.'));
  more.append(extended.profilePanel);
  const tripNode = fields.querySelector('.trip-choice');
  if (tripNode) more.append(tripNode);
  const landPanel = el('section', { class: 'card stay-form-panel' }, el('h2', {}, 'Land'), label('land'));
  const p4 = panel('04');
  if (SUCHE_SCORE_AN) { more.append(landPanel); if (p4) more.append(p4); more.append(extended.tripPanel, extended.qualityPanel, extended.filtersPanel); }
  else {
    // W105 (Sebastian 20.10.): „Mehr Optionen“ = Reise & Profil. Technik (Land, Quellen, Suchkosten, Zusatz-Notenfilter) zugeklappt und klar benannt –
    // keine zweite Notenauswahl neben „Gästenote ab“: der Zusatz-Notenfilter steht dort, ist aber standardmäßig aus.
    more.querySelector(':scope > summary').replaceChildren(stayIcon('regler'), 'Reise, Profil & Technik');
    more.querySelector(':scope > p').textContent = 'Welcher Reise die Suche zugeordnet wird, gespeicherte Suchprofile und selten gebrauchte Technik.';
    extended.profilePanel.querySelector('h2')?.prepend(stayIcon('personen'));
    tripNode?.querySelector('h2')?.prepend(stayIcon('karte'));
    p4?.querySelector('.step-number')?.remove(); if (p4?.querySelector('h2')) p4.querySelector('h2').lastChild.textContent = 'Quellen & Suchkosten';
    const q = extended.qualityPanel.querySelector('input[type="checkbox"]'); if (q && q.checked) { q.checked = false; q.dispatchEvent(new Event('change', { bubbles: true })); }
    extended.qualityPanel.querySelector('h2').textContent = 'Zusätzlicher Notenfilter';
    if (tripNode) more.insertBefore(tripNode, extended.profilePanel); // Reise zuerst, dann Profil
    const technik = el('details', { class: 'a-technik' }, el('summary', {}, stayIcon('info'), 'Technik · Land, Quellen, Suchkosten, Notenfilter'), landPanel, p4, extended.qualityPanel);
    more.append(technik, extended.filtersPanel);
    more.classList.add('a-mehr');
    // W105: kein zweiter Einstieg – „ändern“ in der Reisezeile öffnet diesen Bereich direkt unter dem Kopf
    quick.insertBefore(more, kopf.nextSibling);
  }
  // W102: Ohne Score stehen die Kriterien in der Suchmaske – „Filter anpassen“ nur zeigen, wenn dort noch etwas übrig ist (z. B. Viertel).
  const filterAufraeumen = () => {
    if (SUCHE_SCORE_AN) return;
    let irgendwas = false;
    for (const fs of extended.filtersPanel.querySelectorAll('fieldset.trip-filter-block')) {
      const da = [...fs.children].some(c => c.tagName !== 'LEGEND' && !(c.tagName === 'P' && c.classList.contains('small')) && !(c.classList.contains('trip-criterion') && c.hidden));
      fs.hidden = !da; if (da) irgendwas = true;
    }
    extended.filtersPanel.hidden = !irgendwas;
  };
  form.addEventListener('kriterien-geladen', filterAufraeumen); filterAufraeumen();
  const gaps = el('div', { class: 'quick-gaps' });
  const kurz = d => { const x = new Date(d + 'T12:00:00'); return Number.isNaN(x.getTime()) ? d : x.toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' }); };
  const whoKeys = ['erwachsene', 'kinder_alter', 'budget_eur', 'budget_nacht'];
  const remembered = stayRead('ks_who_last', null);
  const restoreWho = () => { if (remembered && typeof remembered === 'object') for (const k of whoKeys) { const i = form.querySelector(`[name="${k}"]`); if (i && typeof remembered[k] === 'string') i.value = remembered[k]; } wohnen.feld(); budgetNacht?.ausGesamt(); form.dispatchEvent(new Event('input')); };
  restoreWho();
  form.addEventListener('submit', () => { const v = {}; for (const k of whoKeys) v[k] = String(form.querySelector(`[name="${k}"]`)?.value ?? ''); stayWrite('ks_who_last', v); }, true);
  fields.replaceChildren(...[gaps, quick, SUCHE_SCORE_AN ? more : null].filter(Boolean));
  const datum = sucheDatumBereich(form); ortZeit.insertBefore(datum.node, who); datum.node.querySelector('.dr-knopf').after(nights); // W103/W104: Wann-Zeile mit Nächten
  wohnen.feld(); // W96: Feld erst jetzt im Formular erreichbar
  function update() {
    const f = new FormData(form), n = (Date.parse(f.get('abreise')) - Date.parse(f.get('anreise'))) / 86400000;
    nights.textContent = Number.isFinite(n) && n > 0 ? `${n} ${n === 1 ? 'Nacht' : 'Nächte'}` : '';
    const kids = String(f.get('kinder_alter') || '').split(',').map(v => v.trim()).filter(Boolean);
    const budget = f.get('budget_eur');
    const proNacht = f.get('budget_nacht');
    whoText.textContent = [`${f.get('erwachsene') || '?'} Erw.`, kids.length ? `Kinder ${kids.join(', ')}` : 'keine Kinder', budgetNacht ? (proNacht ? 'bis ' + sucheEuro(proNacht) + '/Nacht' : 'Budget offen') : budget ? 'bis ' + sucheEuro(budget) : 'Budget offen'].filter(Boolean).join(' · ');
    const limit = sucheZahl(f.get('limit_usd'));
    cost.textContent = limit === null ? '' : ` · Suche max. ${limit.toLocaleString('de-DE', { style: 'currency', currency: 'USD' })}`;
  }
  form.addEventListener('input', update); form.addEventListener('change', update); update();
  const trip = state => {
    if (!state.ready) { tripLine.textContent = 'Reise wird geladen …'; return; }
    if (state.needsChoice) { tripLine.replaceChildren('Bitte Aufenthalt wählen: '); if (state.node.parentElement !== quick) quick.insertBefore(state.node, submit); state.node.classList.add('needs-choice'); return; }
    if (state.node.parentElement === quick) { more.insertBefore(state.node, more.children[2] || null); state.node.classList.remove('needs-choice'); }
    tripLine.replaceChildren(`${state.reise} · ${state.stage === 'new' ? 'neuer Aufenthalt' : state.stageText} `, SUCHE_SCORE_AN ? el('button', { type: 'button', class: 'link-button', onclick: () => { more.open = true; tripNode?.scrollIntoView({ block: 'center' }); } }, 'ändern')
      : el('button', { type: 'button', class: 'link-button a-mehr-knopf', 'aria-expanded': String(more.open), onclick: e => { more.open = !more.open; e.currentTarget.setAttribute('aria-expanded', String(more.open)); e.currentTarget.textContent = more.open ? 'schließen' : 'ändern'; } }, more.open ? 'schließen' : 'ändern'));
  };
  onTrip(trip);
  call('unterkunft_etappen_lesen').then(r => {
    if (!live()) return;
    const today = new Date().toISOString().slice(0, 10);
    const list = (Array.isArray(r?.luecken) ? r.luecken : []).filter(l => l?.suche_vorschlag?.abreise > today);
    gaps.replaceChildren(...list.map(l => { const v = l.suche_vorschlag; const n = v.naechte ?? l.naechte;
      return el('article', { class: 'gap-card' }, el('div', {}, el('p', { class: 'eyebrow' }, 'Hier fehlt noch eine Unterkunft'), el('strong', {}, `${kurz(v.anreise)} – ${kurz(v.abreise)} · ${n} Nächte`), el('span', { class: 'small' }, [v.nach ? 'nach ' + v.nach : null, v.vor ? 'vor ' + v.vor : null].filter(Boolean).join(' · '))),
        el('button', { type: 'button', class: 'primary', onclick: () => { for (const [k, val] of [['anreise', v.anreise], ['abreise', v.abreise]]) { const i = form.querySelector(`[name="${k}"]`); i.value = val; i.dispatchEvent(new Event('input', { bubbles: true })); } onTrip.setNew?.(); const z = form.querySelector('[name="ziel"]'); z.focus(); z.scrollIntoView({ block: 'center' }); } }, 'Hier suchen')); }));
  }).catch(() => {});
  return { restoreWho, wohnenWerte: wohnen.werte };
}

// W100 (Claude, Sebastian 20.10.): Suchmaske nach Themen. Jedes Kriterium: Angeheftet (in der Maske), Weitere (aufklappbar) oder Aus (nie gesendet).
// Wirkung je Kriterium: ➜ Suche = Booking fragt schon gefiltert an · ⧩ Filter = nach dem Laden geprüft; unbekannt bleibt sichtbar (?).
const MASKE_THEMEN = [
  ['Preis & Buchung', [
    { key: 'storno_kostenlos', label: 'Kostenlos stornierbar', typ: 'ja', suche: true, text: 'Booking sucht nur stornierbare Angebote, andere Quellen werden nach dem Laden geprüft.' },
    { key: 'fruehstueck', label: 'Frühstück inklusive', typ: 'ja', suche: true, text: 'Booking sucht nur mit Frühstück, sonst aus dem Angebotstext.' },
  ]],
  ['Wohnen & Größe', [
    { key: 'flaeche_m2', label: 'Fläche mindestens', typ: 'zahl', einheit: 'm²', start: 60, schritt: 5, min: 10, max: 300, werte: [40, 50, 60, 80, 100, 120, 150], text: 'Nach dem Laden. Fläche fehlt oft, solche bleiben mit ? sichtbar.' },
    { key: 'echte_betten', label: 'Echte Betten für alle', typ: 'ja', text: 'Nach dem Laden: Futon, Schlafsofa und Etagenbett zählen nicht.' },
  ]],
  ['Ausstattung', [
    { key: 'kueche', label: 'Küche', typ: 'ja', suche: true, text: 'Booking sucht nur mit Küche, sonst aus der Ausstattung.' },
    { key: 'waschmaschine', label: 'Waschmaschine', typ: 'ja', text: 'Nach dem Laden, aus den Detailangaben.' },
    { key: 'balkon', label: 'Balkon / Terrasse', typ: 'ja', suche: true, text: 'Booking sucht nur mit Balkon – schränkt stark ein.' },
    { key: 'klima', label: 'Klimaanlage', typ: 'ja', suche: true, text: 'Booking sucht nur mit Klimaanlage.' },
    { key: 'meerblick', label: 'Meerblick', typ: 'ja', suche: true, text: 'Booking sucht nur Zimmer mit Meerblick.' },
    { key: 'wlan', label: 'WLAN kostenlos', typ: 'ja', suche: true, text: 'Booking sucht nur mit kostenlosem WLAN.' },
  ]],
  ['Haus & Freizeit', [
    { key: 'pool', label: 'Pool', typ: 'ja', suche: true, text: 'Booking sucht nur mit Pool, sonst aus der Ausstattung.' },
    { key: 'sauna_spa', label: 'Sauna / Spa', typ: 'ja', suche: true, text: 'Booking sucht „Spa“; Sauna genau nur aus dem Text.' },
    { key: 'fitness', label: 'Fitnessraum', typ: 'ja', suche: true, text: 'Booking sucht nur mit Fitnessraum.' },
    { key: 'parkplatz', label: 'Parkplatz', typ: 'ja', suche: true, text: 'Booking sucht nur mit Parkplatz.' },
  ]],
  ['Lage', [
    { key: 'strand_max_m', label: 'Strand höchstens', typ: 'stufen', stufen: [[300, '300 m'], [1000, '1 km'], [2000, '2 km']], text: 'Nach dem Laden: Luftlinie zum nächsten Strand (OpenStreetMap), kommt etwa eine halbe Minute nach den Treffern. Airbnb-Standorte sind ungenau.' },
    { key: 'luftlinie_max_km', label: 'Zum Ziel höchstens', typ: 'zahl', einheit: 'km', start: 3, schritt: 1, min: 1, max: 50, werte: [1, 2, 3, 5, 10, 20], text: 'Nach dem Laden, Luftlinie aus den Koordinaten.' },
    { key: 'gehzeit_max_min', label: 'Gehzeit zur Station höchstens', typ: 'zahl', einheit: 'Min.', start: 10, schritt: 5, min: 5, max: 60, werte: [5, 10, 15, 20, 30], text: 'Nach dem Laden, wo die Gehzeit bekannt ist.' },
    { key: 'zentrum_max_km', label: 'Zentrum höchstens', typ: 'stufen', stufen: [[1, '1 km'], [3, '3 km'], [5, '5 km']], suche: true, text: 'Booking sucht nur in dieser Nähe zum Zentrum; andere Quellen bleiben mit ? sichtbar.' },
  ]],
  ['Bewertungen', [
    { key: 'note_min', label: 'Gästenote ab', typ: 'stufen', stufen: [[6, '6'], [7, '7'], [8, '8'], [9, '9']], suche: true, text: 'Booking sucht nur ab dieser Note, andere Quellen nach dem Laden.' },
    { key: 'bewertungen_min', label: 'Bewertungen mindestens', typ: 'zahl', einheit: '', start: 30, schritt: 10, min: 10, max: 500, werte: [10, 30, 50, 100, 200], text: 'Nach dem Laden.' },
    { key: 'sterne_min', label: 'Hotelsterne ab', typ: 'stufen', stufen: [[2, '2★'], [3, '3★'], [4, '4★'], [5, '5★']], suche: true, text: 'Nur für Hotels: Booking sucht nur ab diesen Sternen. Apartments sind nicht betroffen.' },
  ]],
];
const MASKE_ALLE = MASKE_THEMEN.flatMap(([, liste]) => liste);
const MASKE_ICON = { storno_kostenlos: 'storno', fruehstueck: 'fruehstueck', flaeche_m2: 'flaeche', echte_betten: 'bett', kueche: 'kueche', waschmaschine: 'waschen', balkon: 'balkon', klima: 'klima', meerblick: 'meer', wlan: 'wlan', pool: 'pool', sauna_spa: 'sauna', fitness: 'fitness', parkplatz: 'auto', strand_max_m: 'strand', luftlinie_max_km: 'pin', gehzeit_max_min: 'bahn', zentrum_max_km: 'pin', note_min: 'stern', bewertungen_min: 'stern', sterne_min: 'hotel' };
const MASKE_KURZ = { flaeche_m2: 'Fläche ab', strand_max_m: 'Strand bis', luftlinie_max_km: 'Zum Ziel bis', gehzeit_max_min: 'Gehzeit Station bis', zentrum_max_km: 'Zentrum bis', note_min: 'Gästenote ab', bewertungen_min: 'Bewertungen ab', sterne_min: 'Sterne ab' };
const MASKE_KEYS = new Set(MASKE_ALLE.map(k => k.key));
const MASKE_STANDARD = { an: ['storno_kostenlos', 'kueche', 'pool', 'sauna_spa', 'strand_max_m', 'note_min'], aus: [] };
function maskeEinstellung() {
  const v = stayRead('ks_maske', null), ok = a => Array.isArray(a) ? a.filter(k => MASKE_KEYS.has(k)) : null;
  return v && ok(v.an) && ok(v.aus) ? { an: ok(v.an), aus: ok(v.aus) } : { an: [...MASKE_STANDARD.an], aus: [...MASKE_STANDARD.aus] };
}
function maskeStufe(key, e = maskeEinstellung()) { return e.an.includes(key) ? 'an' : e.aus.includes(key) ? 'aus' : 'weitere'; }
function maskeSpeichern(e) { return stayWrite('ks_maske', e); }

function sucheMaske({ form, extended }) {
  const api = extended.kriterien;
  // W103 (Sebastian 20.10.: „erkenne ich, was wirklich mitgesucht wird?“): zwei ruhige Gruppen statt Zeichen am Chip
  const chipsSuche = el('div', { class: 'maske-an', role: 'group', 'aria-label': 'Kriterien, die mitgesucht werden' });
  const chipsFilter = el('div', { class: 'maske-an', role: 'group', 'aria-label': 'Kriterien, die nach dem Laden geprüft werden' });
  const wohnenSlot = el('div', { class: 'maske-wohnen' });
  const kopfSuche = el('p', { class: 'mk-gruppe' }, 'Booking sucht schon danach', el('span', { class: 'muted' }, ' · andere Quellen prüfen nach dem Laden'));
  const kopfFilter = el('p', { class: 'mk-gruppe mk-gruppe-filter' }, 'Wird erst nach dem Laden geprüft', el('span', { class: 'muted' }, ' · Unbekanntes bleibt mit ? sichtbar'));
  // Wohnform geht an alle Quellen – steht ohne Überschrift ganz vorn
  const angeheftet = el('div', { class: 'maske-gruppen' }, kopfSuche, chipsSuche, kopfFilter, chipsFilter);
  const weitereInhalt = el('div', { class: 'maske-weitere-inhalt' });
  const weitereKopf = el('summary', {}, 'Weitere Kriterien');
  const weitere = el('details', { class: 'maske-weitere' }, weitereKopf, weitereInhalt);
  const aktiv = el('p', { class: 'maske-aktiv small', 'aria-live': 'polite' });
  const zustand = key => { const v = api.get(key); return v ? { an: v.modus !== 'egal', wert: v.wert } : { an: false, wert: null }; };
  const kurz = k => { const z = zustand(k.key); if (!z.an) return null; if (k.typ === 'ja') return k.label;
    const st = k.typ === 'stufen' ? k.stufen.find(([w]) => String(w) === String(z.wert))?.[1] : `${z.wert} ${k.einheit}`.trim(); return `${k.label} ${st ?? z.wert}`; };
  // W103 (Sebastian 20.10.: „zu wild“): jedes Kriterium ist ein ruhiger Chip. Ja/Nein = antippen; Stufen und Zahlen = Chip mit Auswahlliste.
  // Die Wirkung (➜ Suche / ⧩ Filter) steht in den Einstellungen und als Hinweis beim Antippen-Halten (title), nicht mehr am Chip.
  function zeile(k, mitPin) {
    const z = zustand(k.key), id = 'mk-' + k.key;
    let control;
    // W104 (Richtung A): Kachel mit Symbol; Ecke 🔍 = Booking sucht schon danach, Trichter = wird nach dem Laden geprüft
    const ikon = stayIcon(MASKE_ICON[k.key] || 'plus', 'mk-ikon');
    const mark = el('span', { class: 'mk-mark ' + (k.suche ? 'mk-mark-suche' : 'mk-mark-filter'), title: k.suche ? 'Booking sucht schon danach' : 'Wird nach dem Laden geprüft' }, stayIcon(k.suche ? 'lupe' : 'trichter'));
    if (k.typ === 'ja') control = el('button', { type: 'button', class: 'mk-chip', id, 'aria-pressed': String(z.an), onclick: () => api.set(k.key, z.an ? 'egal' : 'pflicht') }, ikon, el('span', { class: 'mk-chip-text' }, z.an ? '✓ ' : '', k.label), mark);
    else {
      const stufen = k.typ === 'stufen' ? k.stufen : (k.werte || []).map(w => [w, `${w} ${k.einheit}`.trim()]);
      const wert = z.an ? String(z.wert) : '';
      if (z.an && !stufen.some(([w]) => String(w) === wert)) stufen.push([z.wert, `${z.wert} ${k.einheit || ''}`.trim()]);
      const sel = el('select', { 'aria-label': k.label, onchange: () => sel.value === '' ? api.set(k.key, 'egal', null) : api.set(k.key, 'pflicht', Number(sel.value)) },
        el('option', { value: '' }, 'egal'), ...stufen.map(([w, t]) => el('option', { value: String(w) }, t)));
      sel.value = wert;
      control = el('label', { class: 'mk-chip mk-wahl' + (z.an ? ' is-on' : ''), id }, ikon, el('span', { class: 'mk-wahl-name' }, MASKE_KURZ[k.key] || k.label), sel, mark);
    }
    const pin = mitPin ? el('button', { type: 'button', class: 'mk-pin', title: 'In der Suchmaske anheften', 'aria-label': k.label + ' anheften', onclick: () => {
      const e = maskeEinstellung(); e.an = [...e.an.filter(x => x !== k.key), k.key]; e.aus = e.aus.filter(x => x !== k.key); maskeSpeichern(e); draw(); } }, '📌') : null;
    return el('div', { class: 'mk-row' + (z.an ? ' is-on' : '') + (k.suche ? ' mk-art-suche' : ' mk-art-filter'), 'data-key': k.key, title: (k.suche ? '➜ Suche: ' : '⧩ Filter: ') + k.text },
      el('div', { class: 'mk-ctrl' }, control, pin), el('small', { class: 'mk-wirkung' }, (k.suche ? '➜ Suche: ' : '⧩ Filter: ') + k.text));
  }
  function draw() {
    const fokus = angeheftet.contains(document.activeElement) || weitere.contains(document.activeElement) ? document.activeElement.getAttribute('aria-label') || document.activeElement.textContent : null;
    zeichne();
    if (fokus) [...angeheftet.querySelectorAll('button,select'), ...weitere.querySelectorAll('button,select')].find(b => (b.getAttribute('aria-label') || b.textContent) === fokus || b.textContent.replace('✓ ', '') === fokus.replace('✓ ', ''))?.focus({ preventScroll: true });
  }
  function zeichne() {
    if (!api.geladen()) { chipsSuche.replaceChildren(el('p', { class: 'small muted' }, 'Kriterien werden geladen …')); chipsFilter.replaceChildren(); kopfFilter.hidden = true; return; }
    const e = maskeEinstellung(), da = k => api.hat(k.key);
    // Ausgeblendete Kriterien dürfen nichts unsichtbar einschränken (ChatGPT-Hinweis 423)
    for (const k of MASKE_ALLE) if (da(k) && e.aus.includes(k.key) && zustand(k.key).an) api.set(k.key, 'egal', null);
    const an = e.an.map(key => MASKE_ALLE.find(k => k.key === key)).filter(k => k && da(k));
    chipsSuche.replaceChildren(...an.filter(k => k.suche).map(k => zeile(k, false)));
    chipsFilter.replaceChildren(...an.filter(k => !k.suche).map(k => zeile(k, false)));
    kopfFilter.hidden = !chipsFilter.children.length; kopfSuche.hidden = !chipsSuche.children.length;
    const offenWar = weitere.open;
    weitereInhalt.replaceChildren(...MASKE_THEMEN.map(([thema, liste]) => {
      const zeilen = liste.filter(k => da(k) && maskeStufe(k.key, e) === 'weitere');
      return zeilen.length ? el('fieldset', { class: 'mk-thema' }, el('legend', {}, thema), ...zeilen.map(k => zeile(k, true))) : null;
    }).filter(Boolean), el('p', { class: 'mk-legende small muted' }, 'Durchgezogener Rahmen = Booking sucht schon danach · gestrichelt = wird nach dem Laden geprüft'));
    weitere.open = offenWar;
    const aktivWeitere = MASKE_ALLE.filter(k => da(k) && maskeStufe(k.key, e) === 'weitere' && zustand(k.key).an).length;
    const anzahlWeitere = MASKE_ALLE.filter(k => da(k) && maskeStufe(k.key, e) === 'weitere').length;
    weitereKopf.textContent = 'Weitere Kriterien' + (aktivWeitere ? ` · ${aktivWeitere} aktiv` : anzahlWeitere ? ` · ${anzahlWeitere}` : '');
    // Nur was zugeklappt unter „Weitere“ aktiv ist – die angehefteten Chips zeigen ihren Zustand selbst
    const liste = MASKE_ALLE.filter(k => da(k) && maskeStufe(k.key, e) === 'weitere').map(kurz).filter(Boolean);
    aktiv.textContent = liste.length ? 'Außerdem aktiv: ' + liste.join(' · ') : ''; aktiv.hidden = !liste.length;
  }
  form.addEventListener('kriterien-geladen', draw); form.addEventListener('maske-geaendert', draw);
  form.addEventListener('input', () => { if (api.geladen()) draw(); });
  draw();
  const anpassen = el('a', { class: 'maske-anpassen small', href: '#/anzeige/suche' }, stayIcon('regler'), 'Anpassen');
  const legende = el('p', { class: 'maske-legende' }, el('span', {}, stayIcon('lupe', 'mk-mark-suche'), 'Booking sucht schon danach'), el('span', {}, stayIcon('trichter', 'mk-mark-filter'), 'nach dem Laden geprüft'));
  return { wohnenSlot, node: el('div', { class: 'maske' },
    el('p', { class: 'maske-titel' }, 'Wohnen'), wohnenSlot,
    el('div', { class: 'maske-kopf' }, el('p', { class: 'maske-titel' }, 'Wichtig für dich'), anpassen), angeheftet, legende, weitere, aktiv), draw };
}

// W100: Budget pro Nacht (für alle zusammen, alle Zimmer). Der Server bekommt wie bisher das Gesamtbudget = pro Nacht × Nächte.
function sucheBudgetNacht(form, gesamt) {
  const nacht = el('input', { name: 'budget_nacht', type: 'number', min: 1, step: 1, placeholder: 'Optional', inputmode: 'numeric' });
  const info = el('small', { class: 'muted' });
  const datum = name => form.querySelector(`[name="${name}"]`)?.value;
  const naechte = () => { const n = (Date.parse(datum('abreise')) - Date.parse(datum('anreise'))) / 86400000; return Number.isFinite(n) && n > 0 ? n : null; };
  function rechne() {
    const n = naechte(), v = Number(nacht.value);
    gesamt.value = nacht.value && v > 0 && n ? String(Math.round(v * n)) : '';
    info.textContent = nacht.value && v > 0 ? (n ? `= ${sucheEuro(v * n)} für ${n} ${n === 1 ? 'Nacht' : 'Nächte'} · Suche mit +30 % Puffer` : 'Bitte Reisedaten eintragen.') : 'Für alle zusammen, alle Zimmer. Suche mit +30 % Puffer.';
  }
  function ausGesamt() { const n = naechte(), g = Number(gesamt.value); if (!nacht.value && g > 0 && n) nacht.value = String(Math.round(g / n)); rechne(); }
  nacht.addEventListener('input', rechne);
  form.addEventListener('input', e => { if (['anreise', 'abreise'].includes(e.target?.name)) rechne(); });
  form.addEventListener('change', e => { if (['anreise', 'abreise'].includes(e.target?.name)) rechne(); });
  const label = el('label', { class: 'budget-nacht' }, 'Budget pro Nacht (€)', nacht, info);
  gesamt.closest('label').hidden = true;
  rechne();
  return { node: label, ausGesamt, rechne };
}

// W103 (Sebastian 20.10.: „Von–bis muss ich immer zweimal klicken“): ein Feld „Wann?“ mit Kalender – erst Anreise, dann Abreise antippen.
// Die echten Felder anreise/abreise bleiben (unsichtbar) im Formular; alles Weitere (Nächte, Nachtband, Budget) hört wie bisher auf sie.
function sucheDatumBereich(form) {
  const feld = n => form.querySelector(`[name="${n}"]`);
  const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const parse = v => { const d = v ? new Date(v + 'T12:00:00') : null; return d && !Number.isNaN(d.getTime()) ? d : null; };
  const kurz = v => parse(v)?.toLocaleDateString('de-DE', { weekday: 'short', day: 'numeric', month: 'numeric' }) ?? '';
  let monat = null, offen = false;
  const text = el('span', { class: 'dr-text' });
  const knopf = el('button', { type: 'button', class: 'dr-knopf a-zeile', 'aria-expanded': 'false', onclick: () => umschalten() }, el('span', { class: 'a-zeile-ikon' }, stayIcon('kalender')), el('span', { class: 'dr-label' }, 'Wann'), text);
  const hinweis = el('p', { class: 'dr-hinweis small', 'aria-live': 'polite' });
  const monate = el('div', { class: 'dr-monate' });
  const panel = el('div', { class: 'dr-panel', hidden: true, role: 'group', 'aria-label': 'Kalender Reisedaten' }, hinweis, monate);
  function setze(n, v) { const i = feld(n); if (!i) return; i.value = v; i.dispatchEvent(new Event('input', { bubbles: true })); i.dispatchEvent(new Event('change', { bubbles: true })); }
  function beschriften() {
    const a = feld('anreise')?.value, b = feld('abreise')?.value;
    text.textContent = a && b ? `${kurz(a)} – ${kurz(b)}` : a ? `${kurz(a)} – Abreise wählen` : 'Anreise – Abreise';
    knopf.classList.toggle('is-leer', !a);
    knopf.setAttribute('aria-label', 'Reisedaten: ' + text.textContent);
  }
  function umschalten(auf = !offen) {
    offen = auf; panel.hidden = !auf; knopf.setAttribute('aria-expanded', String(auf));
    if (auf) { const s = parse(feld('anreise')?.value) || new Date(); monat = new Date(s.getFullYear(), s.getMonth(), 1, 12); zeichne(); }
  }
  function waehle(v) {
    const a = feld('anreise')?.value, b = feld('abreise')?.value;
    if (!a || b || v <= a) { setze('anreise', v); setze('abreise', ''); }
    else { setze('abreise', v); umschalten(false); }
    beschriften(); if (offen) zeichne();
  }
  function zeichne() {
    const heute = iso(new Date()), a = feld('anreise')?.value || '', b = feld('abreise')?.value || '';
    hinweis.textContent = a && !b ? 'Abreise antippen' : 'Anreise antippen';
    const anzahl = window.matchMedia('(min-width: 720px)').matches ? 2 : 1;
    const erster = new Date(); erster.setDate(1);
    const zurueck = el('button', { type: 'button', class: 'dr-nav', 'aria-label': 'Monat zurück', disabled: monat.getFullYear() * 12 + monat.getMonth() <= erster.getFullYear() * 12 + erster.getMonth(),
      onclick: () => { monat = new Date(monat.getFullYear(), monat.getMonth() - 1, 1, 12); zeichne(); } }, '‹');
    const vor = el('button', { type: 'button', class: 'dr-nav', 'aria-label': 'Monat vor', onclick: () => { monat = new Date(monat.getFullYear(), monat.getMonth() + 1, 1, 12); zeichne(); } }, '›');
    const blaetter = [];
    for (let m = 0; m < anzahl; m++) {
      const start = new Date(monat.getFullYear(), monat.getMonth() + m, 1, 12);
      const tage = new Date(start.getFullYear(), start.getMonth() + 1, 0, 12).getDate();
      const leer = (start.getDay() + 6) % 7;
      const zellen = [...'MDMDFSS'].map((t, i) => el('span', { class: 'dr-wt', 'aria-hidden': 'true' }, ['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'][i]));
      for (let i = 0; i < leer; i++) zellen.push(el('span', {}));
      for (let d = 1; d <= tage; d++) {
        const v = iso(new Date(start.getFullYear(), start.getMonth(), d, 12));
        const kl = ['dr-tag', v === a ? 'is-start' : '', v === b ? 'is-ende' : '', a && b && v > a && v < b ? 'is-zwischen' : '', v === heute ? 'is-heute' : ''].filter(Boolean).join(' ');
        zellen.push(el('button', { type: 'button', class: kl, disabled: v < heute, 'aria-label': kurz(v), 'aria-pressed': String(v === a || v === b), onclick: () => waehle(v) }, String(d)));
      }
      blaetter.push(el('div', { class: 'dr-monat' }, el('p', { class: 'dr-monat-name' }, start.toLocaleDateString('de-DE', { month: 'long', year: 'numeric' })), el('div', { class: 'dr-raster' }, zellen)));
    }
    monate.replaceChildren(el('div', { class: 'dr-kopf' }, zurueck, vor), ...blaetter);
  }
  const zu = e => { if (!panel.isConnected) { document.removeEventListener('click', zu, true); return; } if (offen && !panel.contains(e.target) && !knopf.contains(e.target)) umschalten(false); };
  document.addEventListener('click', zu, true);
  panel.addEventListener('keydown', e => { if (e.key === 'Escape') { umschalten(false); knopf.focus(); } });
  form.addEventListener('input', e => { if (['anreise', 'abreise'].includes(e.target?.name)) beschriften(); });
  for (const n of ['anreise', 'abreise']) feld(n)?.addEventListener('invalid', () => umschalten(true));
  beschriften();
  return { node: el('div', { class: 'dr' }, knopf, panel), beschriften };
}
