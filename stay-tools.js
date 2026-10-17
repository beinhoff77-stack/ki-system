/* Unterkunft: Fotos, Auswahl, Filter und Karte. Keine Schlüssel oder gespeicherten Suchdaten. */
'use strict';

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
  const favorite = el('button', { type: 'button', onclick: () => save(state.saved === 'favorit' ? 'aktiv' : 'favorit') });
  const exclude = el('button', { type: 'button', onclick: () => save(state.saved === 'ausgeschlossen' ? 'aktiv' : 'ausgeschlossen') });
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
      state.message = next === 'favorit' ? 'Als Favorit gespeichert.' : next === 'ausgeschlossen' ? 'Von dir als „Weg“ markiert.' : 'Wieder aktiv.';
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
    undo.hidden = !state.undo; undo.disabled = state.pending || state.refreshRequired;
    status.textContent = state.message || (blocked ? 'Von der Suche ausgeschlossen: ' + (t.ko_grund || 'Prüfkriterien nicht erfüllt.') : state.saved === 'ausgeschlossen' ? 'Von dir als „Weg“ markiert.' : state.saved === 'favorit' ? 'Favorit – unabhängig von der Systembewertung.' : '');
  }
  state.render = update;
  state.undoAction = () => save(state.undo, true);
  box.append(el('div', { class: 'actions' }, favorite, exclude, undo), status); update();
  return box;
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
  const types=[category?.betten_art, category?.betten_text].find(v => typeof v === 'string' && v.trim());
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
      numeric('score', 'Passung mindestens (0–100)', 100), numeric('datenlage', 'Datenlage mindestens (%)', 100),
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

function sucheKarte(container, onSelect, renderSelected) {
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
    selected.scrollIntoView({block:'nearest',behavior:'smooth'});
  }
  stationToggle.addEventListener('change', () => update(currentRows, currentData));
  container.append(heading, el('p', { class: 'map-legend' }, '● A: Rang · ● B: prüfen · ○ unvollständig · ★ Ziel · ▪ Station'),
      el('div', { class: 'actions' }, reset, el('label', { class: 'check-label' }, stationToggle, 'Stationen anzeigen')), message, canvas, tileStatus, el('label',{},'Rang und Unterkunft auswählen',picker), selected);
  function update(rows, data = {}) {
    if (destroyed) return;
    currentRows = rows; currentData = data || {};
    const active = rows.filter(t => sucheGruppe(t) !== 'ausgeschlossen');
    const valid = active.filter(t => sucheKoordinaten(t));
      picker.replaceChildren(el('option',{value:''},'Unterkunft auswählen …'),...valid.map(t=>el('option',{value:t.treffer_id},(sucheGruppe(t)==='A'?'Rang '+(t.bewertung?.rang ?? '?'):'Liste '+sucheGruppe(t))+' · '+t.name)));
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
    layer.clearLayers();
    for (const t of valid) {
      const group = sucheGruppe(t), rank = sucheZahl(t.bewertung?.rang);
      const label = group === 'A' ? rank === null ? 'A' : String(rank) : group === 'B' ? 'B' : '?';
      const icon = el('span', { 'data-map-hit': t.treffer_id }, label);
      const marker = L.marker(sucheKoordinaten(t), { title: t.name || 'Unterkunft', alt: t.name || 'Unterkunft', icon: L.divIcon({ className: 'stay-pin pin-' + group, html: icon, iconSize: [34, 34], iconAnchor: [17, 34] }) });
        marker.on('click',()=>choose(t));
        const nearby=valid.filter(other=>other!==t && map.distance(sucheKoordinaten(t),sucheKoordinaten(other)) < 80);
        marker.bindPopup(el('div', { class: 'stay-map-popup' }, el('strong', {}, t.name || 'Unterkunft'),
        el('p', {}, (t.angebot?.preis_art === 'geschaetzt' ? 'ca. ' : '') + sucheEuro(t.angebot?.preis_gesamt_eur)),
        sucheAngebotsstand(t),
        el('p', {}, group === 'A' ? 'Passende Treffer' + (rank !== null ? ' · Rang ' + rank : '') : group === 'B' ? 'Angaben offen' : 'Noch nicht vollständig bewertet'),
          el('button', { type: 'button', onclick: () => choose(t) }, 'Unterkunft unten ansehen'),
          nearby.length ? el('details',{},el('summary',{},nearby.length+' weitere Unterkünfte an dieser Stelle'),nearby.map(other=>el('button',{type:'button',onclick:()=>choose(other)},(other.bewertung?.rang != null ? 'Rang '+other.bewertung.rang+' · ':'')+other.name))) : null)).addTo(layer);
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
