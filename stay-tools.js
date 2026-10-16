/* Unterkunft: Fotos, Auswahl, Filter und Karte. Keine Schlüssel oder gespeicherten Suchdaten. */
'use strict';

function sucheFoto(t) {
  let url;
  try { url = new URL(t.bild); } catch { /* Platzhalter */ }
  const figure = el('figure', { class: 'stay-photo' });
  const missing = () => figure.replaceChildren(el('div', { class: 'photo-missing', role: 'img', 'aria-label': 'Kein Foto verfügbar' }, '⌂', el('span', {}, 'Kein Foto verfügbar')));
  if (!url || url.protocol !== 'https:' || url.username || url.password) { missing(); return figure; }
  const image = el('img', { src: url.href, alt: 'Foto von ' + (t.name || 'dieser Unterkunft'), loading: 'lazy', decoding: 'async', referrerpolicy: 'no-referrer', onerror: missing });
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
    if (state.pending || state.refreshRequired || !['aktiv', 'favorit', 'ausgeschlossen'].includes(next)) return;
    const previous = state.saved;
    state.pending = true; state.revision++; state.message = 'Auswahl wird gespeichert …'; state.render();
    try {
      const r = await call('unterkunft_treffer_status_setzen', { treffer_id: t.treffer_id, status: next });
      if (!live()) return;
      if (r.ok !== true || r.status !== next || r.treffer_id !== t.treffer_id) throw new Error('Die Änderung wurde nicht eindeutig bestätigt.');
      state.saved = next; state.undo = isUndo ? null : previous;
      state.message = next === 'favorit' ? 'Gemerkt.' : next === 'ausgeschlossen' ? 'Von dir ausgeschlossen.' : 'Wieder aktiv.';
      t.status = next;
    } catch (e) { if (live()) { state.refreshRequired = true; state.message = 'Speichern nicht bestätigt: ' + e.message + ' Bitte zuerst aktualisieren.'; } }
    finally { state.pending = false; state.revision++; if (live()) changed(t, state); }
  }
  function update() {
    const blocked = t.topf === 'ausgeschlossen';
    favorite.textContent = state.saved === 'favorit' ? '★ Gemerkt' : '☆ Merken';
    favorite.setAttribute('aria-pressed', String(state.saved === 'favorit'));
    favorite.disabled = state.pending || state.refreshRequired || state.saved === 'ausgeschlossen' || blocked;
    exclude.textContent = state.saved === 'ausgeschlossen' ? 'Wiederherstellen' : 'Ausschließen';
    exclude.hidden = blocked && state.saved !== 'ausgeschlossen'; exclude.disabled = state.pending || state.refreshRequired;
    undo.hidden = !state.undo; undo.disabled = state.pending || state.refreshRequired;
    status.textContent = state.message || (blocked ? 'Von der Suche ausgeschlossen: ' + (t.ko_grund || 'Prüfkriterien nicht erfüllt.') : state.saved === 'ausgeschlossen' ? 'Von dir ausgeschlossen.' : state.saved === 'favorit' ? 'Gemerkt – unabhängig von deiner Bewertung.' : '');
  }
  state.render = update;
  state.undoAction = () => save(state.undo, true);
  box.append(el('div', { class: 'actions' }, favorite, exclude, undo), status); update();
  return box;
}

function sucheFilterTreffer(t, f) {
  if (f.favoriten && t.status !== 'favorit') return false;
  if (f.gruppe && sucheGruppe(t) !== f.gruppe) return false;
  if (f.typ && t.typ !== f.typ) return false;
  const unknown = f.unbekannt !== false;
  const check = (value, limit, minimum = false) => {
    if (limit === '' || limit == null) return true;
    const n = sucheZahl(value), l = sucheZahl(limit);
    return l === null || (n === null ? unknown : minimum ? n >= l : n <= l);
  };
  const note = sucheZahl(t.note), scale = sucheZahl(t.note_skala);
  const note10 = note !== null && scale > 0 ? note * 10 / scale : null;
  return check(t.angebot?.preis_gesamt_eur, f.preis) && check(t.gehzeit_min, f.gehzeit) &&
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
      select('gruppe', 'Ergebnisliste', [['', 'Alle Listen'], ['A', 'Liste A'], ['B', 'Liste B'], ['offen', 'Noch nicht vollständig bewertet'], ['ausgeschlossen', 'Ausgeschlossen']]), type,
      numeric('preis', 'Gesamtpreis höchstens (€)', null, '0.01'), numeric('gehzeit', 'Gehzeit zur Station höchstens (Min.)', null, '0.1'),
      numeric('note', 'Gästenote mindestens (von 10)', 10, '0.1'), numeric('bewertungen', 'Bewertungen mindestens', null),
      numeric('score', 'Score mindestens (%)', 100), numeric('datenlage', 'Datenlage mindestens (%)', 100),
      select('sterne', 'Hotelsterne mindestens', [['', 'Egal'], ['3', '3 Sterne'], ['4', '4 Sterne'], ['5', '5 Sterne']])),
    el('p', { class: 'small muted' }, 'Gästenoten werden auf 10 umgerechnet. Sterne gelten nur für Hotels, Aparthotels und Ryokans.'),
    el('label', { class: 'check-label' }, favorite, 'Nur Gemerkte'), el('label', { class: 'check-label' }, unknown, 'Unbekannte Angaben mit anzeigen'),
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

function sucheKarte(container, onSelect) {
  let map, layer, lastBoundsKey = '', destroyed = false;
  const heading = el('h2', {}, 'Unterkünfte auf der Karte');
  const message = el('p', { class: 'small', role: 'status' });
  const tileStatus = el('p', { class: 'small', role: 'status' });
  const canvas = el('div', { class: 'stay-map', role: 'region', 'aria-label': 'Karte mit Unterkünften, Ziel und Stationen' });
  const reset = el('button', { type: 'button' }, 'Kartenausschnitt zurücksetzen');
  const stationToggle = el('input', { type: 'checkbox' }); stationToggle.checked = true;
  let currentRows = [], currentData = {};
  stationToggle.addEventListener('change', () => update(currentRows, currentData));
  container.append(heading, el('p', { class: 'map-legend' }, '● A: Rang · ● B: prüfen · ○ unvollständig · ★ Ziel · ▪ Station'),
    el('div', { class: 'actions' }, reset, el('label', { class: 'check-label' }, stationToggle, 'Stationen anzeigen')), message, canvas, tileStatus);
  function update(rows, data = {}) {
    if (destroyed) return;
    currentRows = rows; currentData = data || {};
    const active = rows.filter(t => sucheGruppe(t) !== 'ausgeschlossen');
    const valid = active.filter(t => sucheKoordinaten(t));
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
      marker.bindPopup(el('div', { class: 'stay-map-popup' }, el('strong', {}, t.name || 'Unterkunft'),
        el('p', {}, (t.angebot?.preis_art === 'geschaetzt' ? 'ca. ' : '') + sucheEuro(t.angebot?.preis_gesamt_eur)),
        sucheAngebotsstand(t),
        el('p', {}, group === 'A' ? 'Liste A' + (rank !== null ? ' · Rang ' + rank : '') : group === 'B' ? 'Liste B – Angaben prüfen' : 'Noch nicht vollständig bewertet'),
        el('button', { type: 'button', onclick: () => onSelect(t) }, 'In der Ergebnisliste zeigen'))).addTo(layer);
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
