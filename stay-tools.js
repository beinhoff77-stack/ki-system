/* Unterkunft: Fotos, Auswahl, Filter und Karte. Keine Schlüssel oder gespeicherten Suchdaten. */
'use strict';

// W104 (Richtung A): ein Symbolsatz für die ganze Unterkunftssuche – Linien-Symbole, Farbe = Textfarbe.
const STAY_ICONS = {
  pin: '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
  kalender: '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
  personen: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
  haus: '<path d="M3 10l9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><path d="M9 22V12h6v10"/>',
  hotel: '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
  bett: '<path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20M6 8v9"/>',
  storno: '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/>',
  kueche: '<path d="M3 2v7a2 2 0 0 0 2 2h4a2 2 0 0 0 2-2V2M7 2v20M21 15V2a5 5 0 0 0-5 5v6a2 2 0 0 0 2 2h3Zm0 0v7"/>',
  pool: '<path d="M2 7c1 .6 2 1 3 1 2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2c.7 0 1.4.2 2 .5M2 13c1 .6 2 1 3 1 2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2c.7 0 1.4.2 2 .5M2 19c1 .6 2 1 3 1 2.5 0 2.5-2 5-2s2.5 2 5 2 2.5-2 5-2c.7 0 1.4.2 2 .5"/>',
  sauna: '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3a2.5 2.5 0 0 0 2.5 2.5Z"/>',
  strand: '<path d="M22 12a10 10 0 0 0-20 0Z"/><path d="M12 12v8a2 2 0 0 0 4 0M12 2v1"/>',
  stern: '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.2-6.2 3.2L7 14.2 2 9.3l6.9-1Z"/>',
  bahn: '<rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M8 21l2-5M16 21l-2-5"/>',
  herz: '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>',
  naja: '<path d="M3 13c2.5-3 4.5-3 6.5 0s4 3 6 0 4-3 5.5 0"/>',
  raus: '<path d="M18 6 6 18M6 6l12 12"/>',
  lupe: '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
  trichter: '<path d="M22 3H2l8 9.5V19l4 2v-8.5Z"/>',
  regler: '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
  plus: '<path d="M12 5v14M5 12h14"/>',
  flaeche: '<path d="M3 3h18v18H3zM3 9h18M9 21V9"/>',
  fruehstueck: '<path d="M17 8h1a4 4 0 1 1 0 8h-1M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4ZM6 2v2M10 2v2M14 2v2"/>',
  klima: '<path d="M12 2v20M4.9 4.9l14.2 14.2M2 12h20M4.9 19.1 19.1 4.9"/>',
  wlan: '<path d="M5 12.6a10 10 0 0 1 14 0M8.5 16.1a5 5 0 0 1 7 0M2 8.8a15 15 0 0 1 20 0M12 20h.01"/>',
  auto: '<path d="M19 17h2v-4l-2-5H5L3 13v4h2M5 17a2 2 0 1 0 4 0 2 2 0 1 0-4 0M15 17a2 2 0 1 0 4 0 2 2 0 1 0-4 0M9 17h6"/>',
  fitness: '<path d="M6.5 6.5h11M6.5 17.5h11M6 20V4M18 20V4M3 15V9M21 15V9"/>',
  balkon: '<path d="M4 21V11a8 8 0 0 1 16 0v10M2 21h20M8 21v-6M12 21v-6M16 21v-6"/>',
  meer: '<path d="M2 15c2 0 2-2 4.5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2M2 20c2 0 2-2 4.5-2s2.5 2 5 2 2.5-2 5-2 2.5 2 5 2M12 3a5 5 0 0 1 5 5H7a5 5 0 0 1 5-5Z"/>',
  waschen: '<rect x="3" y="2" width="18" height="20" rx="2"/><circle cx="12" cy="13" r="5"/><path d="M7 6h.01M10 6h.01"/>',
  baum: '<path d="M12 22v-6M8 16h8a4 4 0 0 0 1-7.9A5 5 0 0 0 7.1 7 4 4 0 0 0 8 16Z"/>',
  korb: '<path d="M5 9h14l-1.5 11a2 2 0 0 1-2 1.7h-7a2 2 0 0 1-2-1.7Z"/><path d="m9 9 3-6 3 6M3 9h18"/>',
  kamera: '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3Z"/><circle cx="12" cy="13" r="3"/>',
  mond: '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
  info: '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
  liste: '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
  karte: '<path d="M3 6l6-3 6 3 6-3v15l-6 3-6-3-6 3Z"/><path d="M9 3v15M15 6v15"/>',
  tabelle: '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/>',
  stapel: '<rect x="2" y="6" width="14" height="16" rx="2"/><path d="M8 2h12a2 2 0 0 1 2 2v12"/>',
  sortieren: '<path d="m21 16-4 4-4-4M17 20V4M3 8l4-4 4 4M7 4v16"/>',
  warnung: '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0Z"/><path d="M12 9v4M12 17h.01"/>',
  extern: '<path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
};
function stayIcon(name, cls = '') {
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', '0 0 24 24'); svg.setAttribute('aria-hidden', 'true'); svg.setAttribute('focusable', 'false');
  svg.setAttribute('class', ('ic ' + cls).trim()); svg.innerHTML = STAY_ICONS[name] || '';
  return svg;
}

function sucheFoto(t) {
  let url;
  try { url = new URL(t.bild); } catch { /* Platzhalter */ }
  const figure = el('figure', { class: 'stay-photo' });
  const missing = () => figure.replaceChildren(el('div', { class: 'photo-missing', role: 'img', 'aria-label': 'Kein Foto verfügbar' }, '⌂', el('span', {}, 'Kein Foto verfügbar')));
  if (!url || url.protocol !== 'https:' || url.username || url.password) { missing(); return figure; }
  const image = el('img', { alt: 'Foto von ' + (t.name || 'dieser Unterkunft'), loading: 'lazy', decoding: 'async', referrerpolicy: 'no-referrer', onerror: missing, src: url.href });
  figure.append(image, el('figcaption', {}, 'Foto: ' + (SUCHE_QUELLEN[t.bild_quelle] || t.bild_quelle || SUCHE_QUELLEN[t.quelle] || 'Anbieter')));
  return figure;
}

function sucheAuswahl(t, states, call, live, changed) {
  if (!states.has(t.treffer_id)) states.set(t.treffer_id, { saved: t.status || 'aktiv', pending: false, revision: 0, message: '', undo: null });
  const state = states.get(t.treffer_id), box = el('div', { class: 'stay-selection', 'data-selection': t.treffer_id });
  const status = el('p', { class: 'small', role: 'status' });
  const favorite = el('button', { type: 'button', class: 'sel-fav', onclick: () => save(state.saved === 'favorit' ? 'aktiv' : 'favorit') });
  const exclude = el('button', { type: 'button', class: 'sel-out', onclick: () => save(state.saved === 'ausgeschlossen' ? 'aktiv' : 'ausgeschlossen') });
  const maybe = el('button', { type: 'button', class: 'sel-maybe', onclick: () => save(state.saved === 'vielleicht' ? 'aktiv' : 'vielleicht') }); // W98c: dritte Option „Na ja“
  const undo = el('button', { type: 'button', onclick: () => save(state.undo, true) }, 'Rückgängig');
  async function save(next, isUndo = false) {
    if (state.pending || state.refreshRequired || !['aktiv', 'favorit', 'vielleicht', 'ausgeschlossen'].includes(next)) return;
    const previous = state.saved;
    state.pending = true; state.revision++; state.message = 'Auswahl wird gespeichert …'; state.render();
    try {
      const urteil={aktiv:'offen',favorit:'favorit',vielleicht:'vielleicht',ausgeschlossen:'weg'}[next];
      const r = await call('unterkunft_durchsehen_urteil', { treffer_id: t.treffer_id, urteil });
      if (!live()) return;
      if (r.ok !== true || r.status !== next || r.urteil !== urteil || r.treffer_id !== t.treffer_id) throw new Error('Die Änderung wurde nicht eindeutig bestätigt.');
      state.saved = next; state.undo = isUndo ? null : previous;
      state.message = next === 'favorit' ? 'Als Favorit gespeichert.' : next === 'ausgeschlossen' ? 'Von dir als „Weg“ markiert.' : next === 'vielleicht' ? 'Als „Na ja“ gemerkt.' : 'Wieder aktiv.';
      t.status = next; if(next==='aktiv')t.urteil_uebernommen=null;
    } catch (e) { if (live()) { state.refreshRequired = true; state.message = 'Speichern nicht bestätigt: ' + e.message + ' Bitte zuerst aktualisieren.'; } }
    finally { state.pending = false; state.revision++; if (live()) changed(t, state); }
  }
  function update() {
    const blocked = t.topf === 'ausgeschlossen';
    favorite.textContent = state.saved === 'favorit' ? '★ Favorit' : '☆ Favorit';
    favorite.setAttribute('aria-pressed', String(state.saved === 'favorit'));
    favorite.disabled = state.pending || state.refreshRequired || state.saved === 'ausgeschlossen' || blocked;
    exclude.textContent = state.saved === 'ausgeschlossen' ? 'Wiederherstellen' : 'Weg';
    exclude.hidden = blocked && state.saved !== 'ausgeschlossen'; exclude.disabled = state.pending || state.refreshRequired;
    maybe.textContent = state.saved === 'vielleicht' ? '~ Na ja ✓' : '~ Na ja';
    maybe.setAttribute('aria-pressed', String(state.saved === 'vielleicht'));
    maybe.disabled = state.pending || state.refreshRequired || state.saved === 'ausgeschlossen' || blocked;
    undo.hidden = !state.undo; undo.disabled = state.pending || state.refreshRequired;
    status.textContent = state.message || (blocked ? 'Von der Suche ausgeschlossen: ' + (t.ko_grund || 'Prüfkriterien nicht erfüllt.') : state.saved === 'ausgeschlossen' ? 'Von dir als „Weg“ markiert.' : state.saved === 'favorit' ? 'Favorit – unabhängig von der Systembewertung.' : '');
  }
  state.render = update;
  state.undoAction = () => save(state.undo, true);
  box.append(el('div', { class: 'actions' }, favorite, maybe, exclude, undo), status); update();
  return box;
}

// W96 (Claude): Kennzeichnung je Treffer „Apartment · 2 SZ“ / „Hotel · 2 Zimmer“ und Grund, wenn die nicht bevorzugte Form vorn liegt.
function sucheWohnform(t) {
  const wf=t?.bewertung?.spaltennoten?.wohnform, z=sucheZahl(t?.angebot?.zimmer_anzahl);
  if(!(wf && typeof wf==='object') && !(z>=2)) return null;
  const typ=wf?.art || (['apartment','haus','machiya','aparthotel'].includes(t?.typ)?'apartment':t?.typ==='hotel'?'hotel':null);
  if(!typ) return null;
  const sz=sucheZimmerKurz(t).schlafzimmer;
  return {art:typ,text:typ==='hotel'?'Hotel'+(z>=2?' · '+z+' Zimmer':''):'Apartment'+(sz!==null?' · '+sz+' SZ':''),grund:typeof wf?.grund==='string'&&wf.grund?wf.grund:null};
}
function sucheWarnungen(t) {
  const b=t.bewertung || {}, a=t.angebot || {};
  return [...new Set([...(Array.isArray(b.warnungen) ? b.warnungen : []), ...(a.preis_art === 'geschaetzt' || b.preis_geschaetzt ? ['preis_geschaetzt'] : []), ...(b.gegenpruefung?.pruefung?.urteil === 'einwand' ? ['gegenpruefung_einwand'] : []), ...(t.preis_veraltet ? ['preis_veraltet'] : [])])];
}
function sucheAngebotsKategorie(t) {
  const a=t.angebot || {}, all=Array.isArray(t.kategorien) ? t.kategorien.filter(k => k && typeof k === 'object') : [];
  const ids=all.filter(k => k.id != null && k.id === a.kategorie_id);
  if (a.kategorie_id != null) return ids.length === 1 ? ids[0] : null;
  const normalize=value => typeof value === 'string' ? value.trim().replace(/\s+/g,' ').toLocaleLowerCase('de') : '';
  // Whole-property Airbnb data can have additional manual evidence; use only the unique primary-source category.
  const matches=all.filter(k => normalize(k.name) && normalize(k.name) === normalize(a.kategorie_name));
  const primaryCategories=all.filter(k => k.quelle === t.quelle);
  return matches.length === 1 ? matches[0] : primaryCategories.length === 1 && a.kategorie_name === 'ganze Unterkunft' && t.quelle === 'apify_airbnb' ? primaryCategories[0] : null;
}
function sucheZimmerKurz(t) {
  const k=sucheAngebotsKategorie(t);
  const category=k?.konflikt === true ? null : k;
  const types=[category?.betten_art, t?.quelle==='rakuten_travel'?null:category?.betten_text].find(v => typeof v === 'string' && v.trim()); // W101: bei Rakuten ist betten_text der Zimmer-/Planname
  return {m2:sucheZahl(category?.m2),schlafzimmer:sucheZahl(category?.schlafzimmer),anzahl:sucheZahl(category?.betten_anzahl),typen:typeof types === 'string' && types.trim() ? types : Array.isArray(types) && types.every(v => typeof v === 'string') && types.length ? types.join(', ') : null};
}
function sucheZimmerDetails(t) {
  const selected=sucheAngebotsKategorie(t), all=Array.isArray(t.kategorien) ? t.kategorien.filter(k=>k && typeof k === 'object') : [];
  const normalize=v=>String(v || '').trim().replace(/\s+/g,' ').toLocaleLowerCase('de');
  const source=v=>({booking_plugin:'Booking (Lückenfüller)',manuell:'Manueller Nachweis',...SUCHE_QUELLEN}[v] || v || 'Quelle unbekannt');
  function row(k) {
    const parts=[k.name || 'Zimmerart unbekannt'];
    for(const [field,unit] of [['m2','m²'],['schlafzimmer','Schlafzimmer'],['betten_anzahl','Betten'],['max_personen','Personen']]) {
      const value=sucheZahl(k[field]);
      if(value !== null) parts.push((field==='max_personen'?'bis ':'')+value.toLocaleString('de-DE')+' '+unit);
    }
    if(typeof k.balkon === 'boolean' || ['ja','nein','unklar'].includes(k.balkon)) parts.push('Balkon: '+(typeof k.balkon === 'boolean' ? k.balkon?'ja':'nein' : k.balkon));
    const beds=sucheZimmerKurz({angebot:{kategorie_id:k.id,kategorie_name:k.name},kategorien:[k]}).typen;
    const time=new Date(k.abrufzeit), stand=k.abrufzeit && Number.isFinite(time.getTime()) ? ' · Stand '+time.toLocaleString('de-DE',{day:'2-digit',month:'2-digit',hour:'2-digit',minute:'2-digit'}) : '';
    return el('div', {class:'room-description'}, el('p',{},parts.join(' · ')), beds?el('p',{},'Betten: '+beds):null,
      k.konflikt?el('p',{class:'warning'},'Widersprüchliche Zimmerangaben – nicht als gesichert verwenden.'):null,
      el('p',{class:'small muted'},source(k.quelle)+stand),
      Object.entries(k.ergaenzt_aus || {}).map(([field,from])=>el('p',{class:'small muted'},({m2:'Fläche',schlafzimmer:'Schlafzimmer',max_personen:'Personenzahl',balkon:'Balkon'}[field] || 'Angabe')+' ergänzt aus '+source(from))));
  }
  const others=new Map();
  for(const k of all) {
    const name=normalize(k.name);
    if(k === selected || selected && name === normalize(selected.name)) continue;
    const weight=x=>['m2','schlafzimmer','betten_anzahl','max_personen','balkon','betten_text'].filter(f=>x[f]!=null).length;
    if(!others.has(name) || weight(k)>weight(others.get(name))) others.set(name,k);
  }
  return el('div',{},el('h4',{},'Angebotene Zimmerart'),selected?row(selected):el('p',{},'Angebotene Zimmerart nicht zugeordnet'),
    others.size?el('details',{},el('summary',{},'Weitere Zimmer im Haus ('+others.size+')'),[...others.values()].map(row)):null);
}
function sucheFilterTreffer(t, f) {
  const room=sucheZimmerKurz(t);
  if (f.betten && !sucheBettenDeutsch(room.typen).toLocaleLowerCase('de').includes(sucheBettenDeutsch(f.betten).toLocaleLowerCase('de'))) return false;
  if (f.warnungen === 'mit' && !sucheWarnungen(t).length) return false;
  if (f.warnungen === 'ohne' && sucheWarnungen(t).length) return false;
  if (f.favoriten && t.status !== 'favorit') return false;
  if (f.urteil && (t.status || 'aktiv') !== f.urteil) return false;
  if (f.gruppe && sucheGruppe(t) !== f.gruppe) return false;
  if (f.typ && t.typ !== f.typ) return false;
  const unknown = f.unbekannt !== false;
  const check = (value, limit, minimum = false) => {
    if (limit === '' || limit == null) return true;
    const n = sucheZahl(value), l = sucheZahl(limit);
    return l === null || (n === null ? unknown : minimum ? n >= l : n <= l);
  };
  const note10 = sucheZahl(t.note_geeicht);
  return check(room.m2, f.m2, true) && check(room.schlafzimmer, f.schlafzimmer, true) && check(t.angebot?.preis_gesamt_eur, f.preis) && check(t.gehzeit_min, f.gehzeit) &&
    check(t.bewertungen, f.bewertungen, true) && check(note10, f.note, true) &&
    check(t.bewertung?.score, f.score, true) && check(sucheDatenlage(t), f.datenlage, true) &&
    (!['hotel', 'aparthotel', 'ryokan'].includes(t.typ) || check(t.sterne, f.sterne, true));
}

function sucheFilterPanel(onChange) {
  const inputs = {};
  const numeric = (key, label, max, step = '1') => {
    const n = el('input', { type: 'number', 'aria-label': label, min: 0, max, step, placeholder: 'Egal', oninput: onChange });
    inputs[key] = n; return el('label', {}, label, n);
  };
  const select = (key, label, options) => {
    const n = el('select', { 'aria-label': label, onchange: onChange }, options.map(([value, text]) => el('option', { value }, text)));
    inputs[key] = n; return el('label', {}, label, n);
  };
  const favorite = el('input', { type: 'checkbox', onchange: onChange }); inputs.favoriten = favorite;
  const unknown = el('input', { type: 'checkbox', onchange: onChange }); unknown.checked = true; inputs.unbekannt = unknown;
  const type = select('typ', 'Unterkunftsform', [['', 'Alle Formen']]);
  const panel = el('details', { class: 'card stay-filters' }, el('summary', {}, 'Weitere Filter'),
    el('div', { class: 'stay-filter-grid' },
      select('gruppe', 'Ergebnisliste', [['', 'Alle Listen'], ['A', 'Passende Treffer'], ['B', 'Angaben offen'], ['offen', 'Noch nicht vollständig bewertet'], ['ausgeschlossen', 'Ausgeschlossen']]), type,
      select('urteil', 'Meine Entscheidung', [['','Alle Entscheidungen'],['aktiv','Noch offen'],['favorit','Favorit'],['vielleicht','Na ja'],['ausgeschlossen','Weg']]),
      numeric('schlafzimmer', 'Schlafzimmer mindestens', null), numeric('m2', 'Fläche mindestens (m²)', null),
      el('label', {}, 'Bettentyp enthält', inputs.betten = el('input', {type:'search', 'aria-label':'Bettentyp enthält', oninput:onChange})),
      select('warnungen', 'Warnungen', [['','Alle'],['mit','Mit Warnungen'],['ohne','Ohne gemeldete Warnungen']]),
      numeric('preis', 'Gesamtpreis höchstens (€)', null, '0.01'), numeric('gehzeit', 'Gehzeit zur Station höchstens (Min.)', null, '0.1'),
      numeric('note', 'Gästenote mindestens (von 10)', 10, '0.1'), numeric('bewertungen', 'Bewertungen mindestens', null),
      ...(SUCHE_SCORE_AN ? [numeric('score', 'Passung mindestens (0–100)', 100), numeric('datenlage', 'Datenlage mindestens (%)', 100)] : []),
      select('sterne', 'Hotelsterne mindestens', [['', 'Egal'], ['3', '3 Sterne'], ['4', '4 Sterne'], ['5', '5 Sterne']])),
    el('p', { class: 'small muted' }, 'Gästenoten sind auf Booking-Niveau geeicht. Sterne gelten nur für Hotels, Aparthotels und Ryokans.'),
    el('label', { class: 'check-label' }, favorite, 'Nur Favoriten'), el('label', { class: 'check-label' }, unknown, 'Unbekannte Angaben mit anzeigen'),
    el('button', { type: 'button', onclick: () => { restore({ unbekannt: true }); onChange(); } }, 'Weitere Filter zurücksetzen'));
  let knownTypes = '';
  function setTypes(rows) {
    const types = [...new Set(rows.map(t => t.typ).filter(v => typeof v === 'string' && v))].sort();
    if (JSON.stringify(types) === knownTypes) return;
    knownTypes = JSON.stringify(types); const value = inputs.typ.value;
    inputs.typ.replaceChildren(el('option', { value: '' }, 'Alle Formen'), ...types.map(t => el('option', { value: t }, ({ hotel: 'Hotel', aparthotel: 'Aparthotel', ryokan: 'Ryokan', haus: 'Haus', wohnung: 'Wohnung', apartment: 'Apartment' })[t] || t)));
    inputs.typ.value = types.includes(value) ? value : '';
  }
  const value = () => Object.fromEntries(Object.entries(inputs).map(([key, n]) => [key, n.type === 'checkbox' ? n.checked : n.value]));
  function restore(v = {}) {
    if (!v || typeof v !== 'object' || Array.isArray(v)) v = {};
    for (const [key, n] of Object.entries(inputs)) {
      if (n.type === 'checkbox') n.checked = key === 'unbekannt' ? v[key] !== false : v[key] === true;
      else n.value = ['string', 'number'].includes(typeof v[key]) ? String(v[key]) : '';
    }
  }
  return { node: panel, value, restore, setTypes };
}

function sucheKoordinaten(p) {
  const lat = sucheZahl(p?.lat), lon = sucheZahl(p?.lon);
  return lat !== null && lon !== null && Math.abs(lat) <= 85.05112878 && Math.abs(lon) <= 180 ? [lat, lon] : null;
}

// W98c: Karte ohne Score – Pin = Preis pro Nacht, Farbe = Urteil, Popup mit 3 Schnell-Infos
const STAY_KARTE_ZEICHEN = { favorit: "★", vielleicht: "~", offen: '○', raus: '✕' };
const STAY_URTEIL_TEXT = { favorit: '★ Favorit', vielleicht: '~ Na ja', offen: 'noch nicht bewertet', raus: '✕ Raus' };
function sucheKartenPreis(t) { const v = stayFieldValue(t, 'nacht', t._trip || {}); return v === null ? '? €' : (t.angebot?.preis_art === 'geschaetzt' ? '~' : '') + Math.round(v) + ' €'; }
function sucheKartenSchnell(t) {
  const keys = stayFields().filter(k => !['preis', 'nacht'].includes(k)).slice(0, 3);
  return el('ul', { class: 'map-schnell' }, keys.map(k => el('li', {}, el('span', {}, STAY_FIELDS[k] + ': '), stayField(t, k, t._trip || {}))));
}
function sucheKarte(container, onSelect, renderSelected, options={}) {
  let map, layer, lastBoundsKey = '', destroyed = false;
  const heading = el('h2', {}, 'Unterkünfte auf der Karte');
  const message = el('p', { class: 'small', role: 'status' });
  const tileStatus = el('p', { class: 'small', role: 'status' });
  const canvas = el('div', { class: 'stay-map', role: 'region', 'aria-label': 'Karte mit Unterkünften, Ziel und Stationen' });
  const reset = el('button', { type: 'button' }, 'Kartenausschnitt zurücksetzen');
  const stationToggle = el('input', { type: 'checkbox' }); stationToggle.checked = true;
  let currentRows = [], currentData = {};
  let selectedId = null;
  const selected = el('section', {class:'map-selected', 'aria-label':'Ausgewählte Unterkunft', 'aria-live':'polite'});
  const picker = el('select', {'aria-label':'Unterkunft auf der Karte auswählen', onchange:()=>choose(currentRows.find(t=>String(t.treffer_id) === picker.value))});
  function choose(t) {
    if (!t) return;
    selectedId = t.treffer_id; picker.value = String(selectedId);
    selected.replaceChildren(el('h3',{tabindex:-1},t.name || 'Unterkunft'), renderSelected ? renderSelected(t) : el('button',{type:'button',onclick:()=>onSelect(t)},'In der Ergebnisliste zeigen'));
    markieren();
    selected.scrollIntoView({block:'nearest',behavior:'smooth'});
  }
  stationToggle.addEventListener('change', () => update(currentRows, currentData));
  container.append(heading, el('p', { class: 'map-legend' }, SUCHE_SCORE_AN ? '● A: Rang · ● B: prüfen · ○ unvollständig · ★ Ziel · ▪ Station' : 'Zahl = € pro Nacht · Grün = Favorit · Gelb = Na ja · Weiß = offen · Rot = Raus · ★ Ziel · ▪ Station'),
      el('div', { class: 'actions' }, reset, el('label', { class: 'check-label' }, stationToggle, 'Stationen anzeigen')), message, canvas, tileStatus, el('label',{},'Unterkunft auswählen',picker), selected);
  // W107: gewählter Pin wird hervorgehoben und nach vorn geholt
  const markers = new Map();
  function markieren() {
    canvas.querySelectorAll('.stay-pin.is-gewaehlt').forEach(n => n.classList.remove('is-gewaehlt'));
    for (const [id, m] of markers) { const on = id === selectedId; m.setZIndexOffset(on ? 1000 : 0); if (on) m.getElement()?.classList.add('is-gewaehlt'); }
  }
  function update(rows, data = {}) {
    if (destroyed) return;
    currentRows = rows; currentData = data || {};
    const active = options.includeExcluded||!SUCHE_SCORE_AN?rows:rows.filter(t => sucheGruppe(t) !== 'ausgeschlossen'); // W98c: ohne Score filtert die Urteils-Leiste
    const valid = active.filter(t => sucheKoordinaten(t));
      picker.replaceChildren(el('option',{value:''},'Unterkunft auswählen …'),...valid.map(t=>el('option',{value:t.treffer_id},!SUCHE_SCORE_AN?STAY_KARTE_ZEICHEN[stayUrteilKey(t)]+' '+sucheKartenPreis(t)+' · '+t.name:(sucheGruppe(t)==='A'?(SUCHE_SCORE_AN?'Rang '+(t.bewertung?.rang ?? '?'):'Passend'):'Liste '+sucheGruppe(t))+' · '+t.name)));
      const previouslySelected = valid.find(t=>t.treffer_id === selectedId);
      if(previouslySelected) { picker.value=String(selectedId); selected.replaceChildren(el('h3',{},previouslySelected.name),renderSelected ? renderSelected(previouslySelected) : el('p',{},'Unterkunft ausgewählt')); }
      else {selectedId=null; selected.replaceChildren(el('p',{},'Tippe auf einen Marker. Die zugehörige Unterkunft erscheint hier – ohne Ansichtswechsel.'));}
    const far = valid.filter(t => sucheZahl(t.luftlinie_ziel_m) > 25000);
    message.textContent = `${valid.length} von ${active.length} aktiven Treffern auf der Karte. ${active.length - valid.length} ohne gültige Koordinaten.` + (far.length ? ` ${far.length} weit außerhalb (über 25 km); nicht im ersten Kartenausschnitt.` : '');
    if (!window.L) { tileStatus.textContent = 'Die Karte konnte nicht geladen werden. Die Ergebnisliste bleibt verfügbar.'; canvas.hidden = true; return; }
    canvas.hidden = false;
    if (!map) {
      map = L.map(canvas, { scrollWheelZoom: false });
      L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19, minZoom: 2, keepBuffer: 1,
        attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap-Mitwirkende</a>'
      }).on('tileerror', () => { if (!destroyed) tileStatus.textContent = 'Der Kartenhintergrund ist gerade nicht erreichbar. Positionen und Ergebnisliste bleiben verfügbar.'; }).addTo(map);
      layer = L.layerGroup().addTo(map);
    }
    layer.clearLayers(); markers.clear();
    for (const t of valid) {
      const group = sucheGruppe(t), rank = sucheZahl(t.bewertung?.rang);
      const label = group === 'A' ? rank === null || !SUCHE_SCORE_AN ? 'A' : String(rank) : group === 'B' ? 'B' : '?';
      const icon = el('span', { 'data-map-hit': t.treffer_id }, SUCHE_SCORE_AN ? label : sucheKartenPreis(t));
      const marker = L.marker(sucheKoordinaten(t), { title: t.name || 'Unterkunft', alt: t.name || 'Unterkunft', icon: SUCHE_SCORE_AN ? L.divIcon({ className: 'stay-pin pin-' + group, html: icon, iconSize: [34, 34], iconAnchor: [17, 34] }) : L.divIcon({ className: 'stay-pin pin-preis u-' + stayUrteilKey(t), html: icon, iconSize: [58, 28], iconAnchor: [29, 28] }) });
        marker.on('click',()=>choose(t)); markers.set(t.treffer_id, marker);
        const nearby=valid.filter(other=>other!==t && map.distance(sucheKoordinaten(t),sucheKoordinaten(other)) < 80);
        (SUCHE_SCORE_AN || nearby.length ? marker.bindPopup(el('div', { class: 'stay-map-popup' }, el('strong', {}, t.name || 'Unterkunft'),
        SUCHE_SCORE_AN ? el('p', {}, (t.angebot?.preis_art === 'geschaetzt' ? 'ca. ' : '') + sucheEuro(t.angebot?.preis_gesamt_eur)) : el('p', {}, stayPreisZeile(t, t._trip)),
        SUCHE_SCORE_AN ? sucheAngebotsstand(t) : sucheKartenSchnell(t),
        !SUCHE_SCORE_AN ? el('p', { class: 'small' }, STAY_URTEIL_TEXT[stayUrteilKey(t)]) : el('p', {}, group === 'A' ? 'Passende Treffer' + (SUCHE_SCORE_AN && rank !== null ? ' · Rang ' + rank : '') : group === 'B' ? 'Angaben offen' : 'Noch nicht vollständig bewertet'),
          el('button', { type: 'button', onclick: () => choose(t) }, 'Unterkunft unten ansehen'),
          nearby.length ? el('details',{},el('summary',{},nearby.length+' weitere Unterkünfte an dieser Stelle'),nearby.map(other=>el('button',{type:'button',onclick:()=>choose(other)},(SUCHE_SCORE_AN && other.bewertung?.rang != null ? 'Rang '+other.bewertung.rang+' · ':'')+other.name))) : null)) : marker).addTo(layer); // W107: ohne Überlappung kein Popup – die Unterkunft erscheint unten
    }
    const target = sucheKoordinaten(data?.ziel);
    if (target) L.marker(target, { title: data.ziel.name || 'Reiseziel', icon: L.divIcon({ className: 'stay-pin pin-ziel', html: el('span', {}, '★'), iconSize: [36, 36] }) }).bindPopup(el('strong', {}, data.ziel.name || 'Reiseziel')).addTo(layer);
    for (const p of Array.isArray(data?.zielpunkte) ? data.zielpunkte : []) {
      if (sucheKoordinaten(p)) L.marker(sucheKoordinaten(p), { title: p.name || 'Zielpunkt', icon: L.divIcon({ className: 'stay-pin pin-ziel', html: el('span', {}, '★'), iconSize: [30, 30] }) }).bindPopup(el('strong', {}, p.name || 'Zielpunkt')).addTo(layer);
    }
    if (stationToggle.checked) for (const s of Array.isArray(data?.stationen) ? data.stationen : []) {
      if (sucheKoordinaten(s)) L.circleMarker(sucheKoordinaten(s), { radius: 5, color: '#566878', weight: 2, fillOpacity: 0.8 }).bindTooltip(el('span', {}, 'Station: ' + (s.name || 'unbekannt'))).addTo(layer);
    }
    const near = valid.filter(t => !(sucheZahl(t.luftlinie_ziel_m) > 25000)).map(sucheKoordinaten);
    if (target) near.push(target);
    const fit = () => {
      if (!near.length) { map.setView([20, 0], 2); return; }
      map.fitBounds(L.latLngBounds(near), { padding: [36, 36], maxZoom: 15, animate: false });
    };
    reset.onclick = fit;
    const boundsKey = JSON.stringify([valid.map(t => [t.treffer_id, t.lat, t.lon]), target]);
    map.invalidateSize({ animate: false });
    if (boundsKey !== lastBoundsKey) { lastBoundsKey = boundsKey; fit(); }
  }
  return { update, destroy: () => { destroyed = true; map?.remove(); map = null; } };
}
