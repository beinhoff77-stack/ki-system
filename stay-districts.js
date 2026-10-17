/* Viertel lesen und auswählen; Entscheidungen und Ermittlung nur nach Klick. */
'use strict';
const VIERTEL_NOTEN = [['nahversorgung','Nahversorgung'],['gastronomie','Gastronomie'],['sehenswuerdigkeiten','Sehenswürdigkeiten'],['gruen','Grün'],['oepnv','ÖPNV'],['zentrumsnaehe','Zentrumsnähe'],['ruhe','Ruhe'],['strand','Strand']];
const viertelStadt = value => String(value || '').trim().toLocaleLowerCase('de');
const viertelId = value => Number.isSafeInteger(value) && value > 0;
const viertelNote = value => { const n = sucheZahl(value); return n !== null && n >= 0 && n <= 10 ? n : null; };
function viertelHref(params = {}) { return '#/viertel/?' + new URLSearchParams(params); }
function sucheViertelLink(zone, suchauftragId) {
  if (!viertelId(zone?.id) || !viertelId(suchauftragId)) return null;
  return el('p', { class: 'small stay-district-link' }, el('a', { href: viertelHref({ suche: suchauftragId, zone: zone.id }) }, 'Viertel: ' + (zone.name || 'Unbenannt')),
    zone.status === 'vorschlag' ? el('span', {}, ' · automatischer Vorschlag – ungeprüft') : null);
}
function viertelAntwort(r) {
  if (r?.ok !== true || typeof r.stadt !== 'string' || !Array.isArray(r.viertel) || !Array.isArray(r.gestrichen) ||
      [...r.viertel, ...r.gestrichen].some(z => !viertelId(z?.id) || typeof z.name !== 'string' || !['vorschlag','bestaetigt','gestrichen'].includes(z.status))) {
    throw new Error('Die Viertel-Antwort ist unvollständig.');
  }
  return r;
}
function sucheViertelForm(form, call, live, changed = () => {}) {
  let loadedCity = '', rows = [], loading = false, revision = 0;
  const selected = new Set();
  const mode = el('select', { 'aria-label': 'Bedeutung der Viertelauswahl' },
    el('option', { value: 'egal' }, 'Egal'), el('option', { value: 'pflicht' }, 'Pflicht – nur diese Viertel'), el('option', { value: 'wunsch' }, 'Wunsch – diese Viertel bevorzugen'));
  const notice = el('p', { class: 'small', role: 'status' });
  const list = el('div', { class: 'district-form-choices' });
  const reload = el('button', { type: 'button', onclick: () => load() }, 'Viertel für Zielort laden');
  const node = el('div', { class: 'district-form' }, el('label', {}, 'Viertelauswahl', mode), reload, notice, list,
    el('p', { class: 'small muted' }, 'Die Auswahl gilt nur für diesen Zielort. Bei einem Ortswechsel wird sie geleert. Ohne bekannte Zuordnung bleiben Pflicht-Treffer unter „Angaben offen“ zur Prüfung.'));
  function paint() {
    list.replaceChildren(...rows.map(z => {
      const input = el('input', { type: 'checkbox', 'aria-label': 'Suchviertel: ' + z.name, onchange: () => {
        if (input.checked) { selected.add(z.id); if (mode.value === 'egal') mode.value = 'pflicht'; } else selected.delete(z.id);
        changed();
      } }); input.checked = selected.has(z.id);
      return el('label', { class: 'check-label' }, input, z.name, z.status === 'vorschlag' ? ' · ungeprüft' : ' · bestätigt');
    }));
  }
  form.elements.ziel.addEventListener('input', () => {
    if (viertelStadt(form.elements.ziel.value) === loadedCity) return;
    revision++; loadedCity = ''; rows = []; selected.clear(); mode.value = 'egal'; paint();
    notice.textContent = 'Viertelauswahl geleert. Viertel für den neuen Zielort laden.'; changed();
  });
  mode.addEventListener('change', changed);
  async function load() {
    const city = form.elements.ziel.value.trim(), key = viertelStadt(city);
    if (loading) return;
    if (city.length < 2) { notice.textContent = 'Bitte zuerst einen Zielort eintragen.'; form.elements.ziel.focus(); return; }
    const version = ++revision; loading = true; reload.disabled = true; notice.textContent = 'Viertel werden geladen …';
    try {
      const r = viertelAntwort(await call('unterkunft_viertel_lesen', { stadt: city }));
      if (!live() || version !== revision || key !== viertelStadt(form.elements.ziel.value)) return;
      if (viertelStadt(r.stadt) !== key) throw new Error('Die Antwort gehört zu einem anderen Zielort.');
      rows = r.viertel.filter(z => z.status !== 'gestrichen'); loadedCity = key;
      let removed = 0; for (const id of selected) if (!rows.some(z => z.id === id)) { selected.delete(id); removed++; }
      paint(); notice.textContent = `${rows.length} Viertel für ${city}.` + (removed ? ` ${removed} gespeicherte Viertel passen nicht mehr und wurden aus der Auswahl entfernt.` : '') + (!rows.length ? ' In der Viertelübersicht kannst du die Ermittlung anstoßen.' : '');
    } catch (e) { if (live() && version === revision) notice.textContent = 'Viertel nicht geladen: ' + e.message; }
    finally { loading = false; if (live()) reload.disabled = false; }
  }
  return { node, load, modus: () => mode.value,
    apply(value) {
      revision++; selected.clear();
      if (Array.isArray(value?.werte)) value.werte.filter(viertelId).forEach(id => selected.add(id));
      mode.value = ['pflicht','wunsch'].includes(value?.modus) ? value.modus : 'egal';
      loadedCity = ''; rows = []; paint();
      notice.textContent = selected.size ? `${selected.size} Viertel übernommen. Bitte für den aktuellen Zielort laden und prüfen.` : 'Viertel für deinen Zielort auswählen.'; changed();
    },
    value() {
      const modus = mode.value;
      if (!['egal','pflicht','wunsch'].includes(modus)) throw new Error('Bitte die Bedeutung der Viertelauswahl prüfen.');
      if (modus === 'egal') return { modus };
      if (loading || !loadedCity || loadedCity !== viertelStadt(form.elements.ziel.value)) throw new Error('Bitte die gewählten Viertel zuerst für den aktuellen Zielort laden und prüfen.');
      if (!selected.size) throw new Error('Bitte mindestens ein Viertel auswählen oder die Viertelauswahl auf „Egal“ setzen.');
      return { modus, werte: [...selected].sort((a,b) => a-b) };
    }
  };
}

function viertelKarte(container, onSelect) {
  let map, layer, tiles, previous = '', disposed = false;
  const message = el('p', { class: 'small', role: 'status' });
  const tileStatus = el('p', { class: 'small', role: 'status' });
  const canvas = el('div', { class: 'stay-map', role: 'region', 'aria-label': 'Viertelkarte' });
  const reset = el('button', { type: 'button' }, 'Alle sichtbaren Viertel zeigen');
  container.append(el('h2', {}, 'Die Stadt im Überblick'),
    el('p', { class: 'map-legend' }, 'Grün: ruhig · Gelb: belebt · Rot: laut · Grau: unbekannt. Gestrichelt: ungeprüfter Vorschlag. Durchgezogen: bestätigt.'),
    el('p', { class: 'small muted' }, 'Die Kreise zeigen ungefähre Bereiche, keine amtlichen Grenzen.'), reset, canvas, message, tileStatus);
  return {
    update(rows) {
      if (disposed) return;
      if (!window.L) { message.textContent = 'Die Karte ist nicht verfügbar. Alle Viertel bleiben als Liste lesbar.'; canvas.hidden = true; return; }
      if (!map) {
        map = L.map(canvas, { scrollWheelZoom: false }).setView([20,0],2); layer = L.layerGroup().addTo(map);
        tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { minZoom: 2, maxZoom: 19, keepBuffer: 1,
          attribution: '© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap-Mitwirkende</a>'
        }).on('tileerror', () => { if (!disposed) tileStatus.textContent = 'Der Kartenhintergrund ist nicht erreichbar. Viertelkreise und Liste bleiben nutzbar.'; });
      }
      const key = JSON.stringify(rows.map(z => [z.id,z.lat,z.lon,z.radius_m,z.laerm,z.status,z.name]));
      map.invalidateSize({ animate: false }); if (key === previous) return; previous = key; layer.clearLayers();
      const bounds = L.latLngBounds([]); let count = 0;
      for (const z of rows) {
        const coord = sucheKoordinaten(z), radius = sucheZahl(z.radius_m);
        if (!coord || radius === null || radius <= 0 || radius > 100000) continue;
        const circle = L.circle(coord, { radius, color: ({ruhig:'#2c6846',belebt:'#946300',laut:'#ac3a42'})[z.laerm] || '#566878',
          weight: 3, fillOpacity: .12, dashArray: z.status === 'vorschlag' ? '7 6' : null }).addTo(layer);
        circle.bindPopup(el('div', { class: 'stay-map-popup' }, el('strong', {}, z.name), el('p', {}, z.charakter || 'Charakter unbekannt'),
          el('button', { type: 'button', onclick: () => onSelect(z.id) }, 'Viertel ansehen')));
        const path = circle.getElement();
        path?.setAttribute('tabindex', '0'); path?.setAttribute('role', 'button'); path?.setAttribute('aria-label', 'Viertel: ' + z.name); path?.setAttribute('data-district-circle', String(z.id));
        path?.addEventListener('keydown', event => { if (['Enter',' '].includes(event.key)) { event.preventDefault(); onSelect(z.id); } });
        bounds.extend(circle.getBounds()); count++;
      }
      message.textContent = `${count} von ${rows.length} Vierteln auf der Karte.` + (count < rows.length ? ' Fehlende oder ungültige Positionen bleiben in der Liste.' : '');
      const fit = () => bounds.isValid() ? map.fitBounds(bounds, { padding: [24,24], maxZoom: 14, animate: false }) : map.setView([20,0],2);
      reset.onclick = fit; fit(); if (!map.hasLayer(tiles)) tiles.addTo(map);
    },
    destroy() { disposed = true; map?.remove(); map = null; }
  };
}

async function viewViertel(arg) {
  setChrome('Unterkunft / Viertel', { tab: 'viertel', back: !!arg });
  const params = new URLSearchParams(String(arg || '').replace(/^\?/, ''));
  const run = params.has('suche') ? Number(params.get('suche')) : null;
  let focusZone = Number(params.get('zone')), data = null, loading = false, writing = false, uncertain = false, pendingGeneration = null, timer, disposed = false, map = null;
  const guard = viewGuard(), requests = new Set(), selected = new Set(), drafts = new Map(), filters = new Map();
  const live = () => !disposed && guard();
  const scope = el('div', { class: 'suche districts-page' }); main.replaceChildren(scope);
  disposeSuche = () => { disposed = true; clearTimeout(timer); requests.forEach(c => c.abort()); map?.destroy(); };
  async function call(name, values) {
    const c = new AbortController(); requests.add(c); const timeout = setTimeout(() => c.abort(), 25000);
    try {
      const r = await http('/aktion', { method: 'POST', body: { aktion: name, daten: values }, signal: c.signal });
      if (r?.ok !== true || !r.ergebnis || r.ergebnis.ok === false) throw new Error(r?.fehler || r?.ergebnis?.fehler || 'Die Schnittstelle konnte die Anfrage nicht bestätigen.');
      return r.ergebnis;
    } catch (e) { throw e.name === 'AbortError' ? new Error('Die Antwort dauert zu lange. Bitte den Stand erneut lesen.') : e; }
    finally { clearTimeout(timeout); requests.delete(c); }
  }
  const city = el('input', { name: 'stadt', required: true, minlength: 2, maxlength: 200, placeholder: 'z. B. Kyoto', value: params.get('stadt') || '' });
  const cityForm = el('form', { class: 'card district-city-form', onsubmit: event => { event.preventDefault(); if (cityForm.reportValidity()) route('viertel', '?' + new URLSearchParams({ stadt: city.value.trim() })); } },
    el('label', {}, 'Stadt oder Insel', city), el('button', { type: 'submit' }, 'Viertel laden'));
  const notice = el('p', { role: 'status', class: 'small district-notice' });
  const refresh = el('button', { type: 'button', onclick: () => load() }, 'Viertel aktualisieren');
  const generate = el('button', { type: 'button', class: 'primary', onclick: () => create() }, 'Viertel ermitteln · ca. 0,06 USD');
  const info = el('section', { class: 'card district-summary', hidden: true });
  const generatePanel = el('details', { class: 'card district-generation', hidden: true }, el('summary', {}, 'Viertel automatisch ermitteln'),
    el('p', {}, 'Die automatische Ermittlung kostet etwa 6 US-Cent und dauert 1–5 Minuten. Bestätigte Viertel bleiben bei einer erneuten Ermittlung erhalten.'), generate);
  const filterBox = el('fieldset', { class: 'card district-filters', hidden: true }, el('legend', {}, 'Viertel eingrenzen'),
    el('p', { class: 'small' }, 'Diese Filter ändern nur die Ansicht. Bei aktiven Notenfiltern bleiben unbekannte Werte außerhalb der Auswahl.'));
  for (const [key,label] of [['ruhig','Ruhig'],['oepnv','ÖPNV ≥ 5'],['nahversorgung','Nahversorgung ≥ 5'],['gastronomie','Gastronomie ≥ 5'],['gruen','Grün ≥ 5'],['sehenswuerdigkeiten','Sehenswürdigkeiten ≥ 5'],['zentrumsnaehe','Zentrumsnähe ≥ 5']]) {
    const input = el('input', { type: 'checkbox', onchange: () => draw() }); filters.set(key, input);
    filterBox.append(el('label', { class: 'district-chip' }, input, label));
  }
  const sort = el('select', { 'aria-label': 'Viertel sortieren nach', onchange: () => draw() }, el('option', { value: 'name' }, 'Name'),
    ...VIERTEL_NOTEN.map(([key,label]) => el('option', { value: key }, label + ' · höchste zuerst')),
    ...(run ? [el('option', { value: 'treffer' }, 'Treffer · meiste zuerst'), el('option', { value: 'preis' }, 'Median je Nacht · günstigste zuerst')] : []));
  filterBox.append(el('label', {}, 'Sortieren nach', sort), el('button', { type: 'button', onclick: () => { filters.forEach(input => { input.checked = false; }); sort.value = 'name'; draw(); } }, 'Viertelfilter zurücksetzen'));
  const count = el('p', { class: 'small', role: 'status' });
  const mode = el('select', { 'aria-label': 'Gewählte Viertel berücksichtigen' }, el('option', { value: 'pflicht' }, 'Pflicht – nur diese Viertel'), el('option', { value: 'wunsch' }, 'Wunsch – diese Viertel bevorzugen'));
  const selectedText = el('p', { class: 'small' });
  const use = el('button', { type: 'button', class: 'primary', onclick: () => {
    if (!data || !selected.size || loading || writing || uncertain) return;
    try {
      sessionStorage.setItem('ks_viertel_entwurf', JSON.stringify({ stadt: data.stadt, modus: mode.value, werte: [...selected] }));
      route('suche', 'viertel');
    } catch { notice.textContent = 'Die Auswahl konnte nicht übergeben werden. Bitte die Viertel direkt im Suchformular auswählen.'; }
  } }, 'Mit diesen Vierteln suchen');
  const selection = el('section', { class: 'card district-selection', hidden: true }, el('h2', {}, 'Nur in diesen Vierteln suchen'),
    selectedText, el('label', {}, 'Bedeutung für eine neue Suche', mode), el('div', { class: 'actions' }, use,
      el('button', { type: 'button', onclick: () => { selected.clear(); syncSelection(); } }, 'Viertelauswahl leeren')),
    el('p', { class: 'small muted' }, 'Öffnet ein neues Suchformular mit deiner Auswahl. Erst „Anlegen und Suche starten“ beginnt die Unterkunftssuche.'));
  const mapPanel = el('section', { class: 'card stay-map-panel', hidden: true });
  const mapButton = el('button', { type: 'button', hidden: true, 'aria-expanded': 'false', onclick: () => {
    mapPanel.hidden = !mapPanel.hidden; mapButton.setAttribute('aria-expanded', String(!mapPanel.hidden));
    mapButton.textContent = mapPanel.hidden ? 'Viertelkarte anzeigen' : 'Viertelkarte ausblenden'; drawMap();
    if (!mapPanel.hidden) mapPanel.scrollIntoView({ block: 'start' });
  } }, 'Viertelkarte anzeigen');
  const cards = el('div', { class: 'district-cards' });
  const removed = el('details', { class: 'card district-removed', hidden: true });
  scope.append(el('div', { class: 'stay-page-heading' }, el('p', { class: 'eyebrow' }, 'DIE UMGEBUNG ZÄHLT'), el('h2', {}, 'Welches Viertel passt zu euch?'),
    el('p', {}, 'Ruhige Straßen, kurze Wege oder mitten im Leben. Entdecke die Umgebung eurer nächsten Unterkunft.')),
    cityForm, ...[run ? el('a', { href: '#/suche/' + run }, 'Zurück zu den Unterkünften') : null].filter(Boolean),
    el('div', { class: 'actions' }, refresh, mapButton), notice, info, generatePanel, filterBox, selection, count, mapPanel, cards, removed);
  const query = run !== null ? { suchauftrag_id: run } : { stadt: (params.get('stadt') || '').trim() };
  const isRunning = () => data?.letzter_lauf && !['fertig','fehler'].includes(data.letzter_lauf.status);
  function sync() {
    refresh.disabled = loading || writing;
    generate.disabled = loading || writing || uncertain || !!pendingGeneration || !!isRunning();
    cityForm.querySelector('button').disabled = writing; city.disabled = writing;
    scope.querySelectorAll('[data-district-write]').forEach(n => { n.disabled = writing || uncertain || (loading && n.tagName === 'BUTTON'); });
    syncSelection();
  }
  function syncSelection() {
    selectedText.textContent = `${selected.size} Viertel ausgewählt. Die Auswahl bleibt bei Anzeige-Filtern erhalten.`;
    use.disabled = !selected.size || loading || writing || uncertain;
    scope.querySelectorAll('[data-select-district]').forEach(input => { input.checked = selected.has(Number(input.dataset.selectDistrict)); input.disabled = writing || uncertain; });
  }
  function visibleRows() {
    const rows = (data?.viertel || []).filter(z => z.status !== 'gestrichen' && [...filters].every(([key,input]) => !input.checked ||
      (key === 'ruhig' ? z.laerm === 'ruhig' : viertelNote(z.noten?.[key]) !== null && viertelNote(z.noten[key]) >= 5)));
    return rows.sort((a,b) => {
      if (sort.value === 'name') return a.name.localeCompare(b.name,'de');
      const get = z => sort.value === 'treffer' ? sucheZahl(z.suche?.treffer) : sort.value === 'preis' ? sucheZahl(z.suche?.preis_nacht_median_eur) : viertelNote(z.noten?.[sort.value]);
      const x = get(a), y = get(b); if (x === null || y === null) return x === y ? a.name.localeCompare(b.name,'de') : x === null ? 1 : -1;
      return (sort.value === 'preis' ? x-y : y-x) || a.name.localeCompare(b.name,'de');
    });
  }
  function drawMap() { if (data && !mapPanel.hidden) { if (!map) map = viertelKarte(mapPanel, jump); map.update(visibleRows()); } }
  function jump(id) {
    if (!scope.querySelector(`[data-district="${id}"]`)) { filters.forEach(input => { input.checked = false; }); draw(); }
    const card = scope.querySelector(`[data-district="${id}"]`);
    if (!card) { notice.textContent = 'Das verlinkte Viertel ist nicht mehr verfügbar.'; return; }
    if (card.closest('.district-removed')) removed.open = true;
    const heading = card.querySelector('h3'); heading.focus({ preventScroll: true }); card.scrollIntoView({ block: 'start' });
  }
  function card(z) {
    const result = el('article', { class: 'card district-card', 'data-district': z.id });
    const box = el('input', { type: 'checkbox', 'data-select-district': z.id, 'aria-label': 'Viertel auswählen: ' + z.name,
      onchange: () => { if (box.checked) selected.add(z.id); else selected.delete(z.id); syncSelection(); } });
    result.append(el('p', { class: 'eyebrow' }, z.charakter || 'Charakter unbekannt'), el('h3', { tabindex: -1 }, z.name),
      z.name_lokal ? el('p', { class: 'muted district-local-name' }, z.name_lokal) : null,
      el('span', { class: 'pill' }, z.status === 'bestaetigt' ? 'Von dir bestätigt' : z.status === 'gestrichen' ? 'Gestrichen' : 'Automatischer Vorschlag – ungeprüft'),
      el('p', { class: 'small' }, `Tagsüber: ${z.laerm || 'unbekannt'} · Nachts: ${z.laerm_nacht || 'unbekannt'} · Preisniveau: ${z.preisniveau || 'unbekannt'}`),
      el('p', {}, z.beschreibung || 'Noch keine Beschreibung vorhanden.'),
      el('p', {}, el('strong', {}, 'Mit Familie: '), z.familien_hinweis || 'Noch keine Angaben.'),
      el('ul', { class: 'district-highlights' }, sucheTexte(z.highlights).map(text => el('li', {}, text))),
      sucheBalken(z.noten, VIERTEL_NOTEN));
    if (run) result.append(el('p', { class: 'district-stats' }, `${sucheZahl(z.suche?.treffer) ?? 'unbekannt'} Treffer · ${sucheZahl(z.suche?.liste_a) ?? 'unbekannt'} unter den passenden Treffern · bester Rang: ${sucheZahl(z.suche?.bester_rang) ?? 'unbekannt'}`),
      el('p', { class: 'small' }, 'Median je Nacht: ' + sucheEuro(z.suche?.preis_nacht_median_eur) + ' · aus diesem Suchlauf, kein aktuelles Buchungsangebot.'));
    const links = (Array.isArray(z.quellen) ? z.quellen : []).map(sucheLink).filter(Boolean);
    result.append(el('details', { class: 'district-sources' }, el('summary', {}, 'Quellen & Einordnung'),
      el('p', { class: 'small' }, 'Vertrauen: ' + (z.vertrauen || 'unbekannt') + ' · Position: ' + (z.koordinaten_quelle || 'unbekannt')),
      el('p', { class: 'small' }, z.quelle || 'Keine Herkunftsangabe.'),
      links.length ? el('ul', {}, links.map((href,i) => el('li', {}, el('a', { href, target: '_blank', rel: 'noopener noreferrer' }, `${i+1}. ${new URL(href).hostname}`)))) : el('p', {}, 'Keine sicheren Quellenlinks geliefert.')));
    if (z.status !== 'gestrichen') result.append(el('label', { class: 'check-label' }, box, 'Für neue Unterkunftssuche auswählen'));
    const actions = el('div', { class: 'actions district-actions' });
    if (z.status !== 'bestaetigt' && z.status !== 'gestrichen') actions.append(el('button', { type: 'button', 'data-district-write': true, onclick: () => decide(z,{status:'bestaetigt'}) }, 'Bestätigen'));
    if (z.status === 'gestrichen') actions.append(el('button', { type: 'button', 'data-district-write': true, onclick: () => decide(z,{status:'vorschlag'}) }, 'Als Vorschlag wieder aufnehmen'));
    else {
      const confirmation = el('div', { class: 'district-confirm', hidden: true, role: 'group', 'aria-label': 'Viertel streichen bestätigen' });
      const cancel = el('button', { type: 'button', onclick: () => { confirmation.hidden = true; strike.focus(); } }, 'Abbrechen');
      const yes = el('button', { type: 'button', class: 'danger', 'data-district-write': true, onclick: () => decide(z,{status:'gestrichen'}) }, 'Ja, Viertel streichen');
      const strike = el('button', { type: 'button', 'data-district-write': true, onclick: () => { confirmation.hidden = false; yes.focus(); } }, 'Streichen');
      confirmation.append(el('p', {}, 'Dieses Viertel wirklich streichen? Es wird danach nicht mehr für die Zuordnung verwendet.'), yes, cancel); actions.append(strike); result.append(confirmation);
    }
    result.append(actions);
    const draft = drafts.get(z.id) || { name: z.name, notiz: z.notiz_nutzer || '' };
    const name = el('input', { required: true, maxlength: 80, value: draft.name, 'data-district-write': true, 'data-edit-field': 'name', 'aria-label': 'Neuer Name für ' + z.name });
    const note = el('textarea', { maxlength: 500, rows: 2, 'data-district-write': true, 'data-edit-field': 'notiz', 'aria-label': 'Notiz zu ' + z.name }); note.value = draft.notiz;
    const edit = el('form', { onsubmit: event => { event.preventDefault(); if (!edit.reportValidity()) return;
      if (!name.value.trim()) { notice.textContent = 'Bitte einen Namen eintragen.'; name.focus(); return; }
      if (z.notiz_nutzer && !note.value.trim()) { notice.textContent = 'Eine vorhandene Notiz kann derzeit nur durch einen neuen Text ersetzt werden.'; note.focus(); return; }
      decide(z,{status:z.status,name:name.value.trim(),...(note.value.trim()?{notiz:note.value.trim()}:{})});
    } }, el('label', {}, 'Name', name), el('label', {}, 'Deine Notiz', note), el('button', { type: 'submit', 'data-district-write': true }, 'Name und Notiz speichern'));
    edit.addEventListener('input', () => drafts.set(z.id,{name:name.value,notiz:note.value}));
    result.append(el('details', { 'data-edit': z.id }, el('summary', {}, 'Umbenennen / Notiz'), edit));
    return result;
  }
  function draw() {
    if (!data) return;
    const active = document.activeElement, focusedId = active?.closest('[data-district]')?.dataset.district, field = active?.dataset.editField;
    const range = field ? [active.selectionStart,active.selectionEnd] : null;
    const opened = new Set([...scope.querySelectorAll('details[data-edit][open]')].map(n => n.dataset.edit));
    const rows = visibleRows(); cards.replaceChildren(...rows.map(card));
    if (!rows.length) cards.append(el('p', { class: 'card' }, data.viertel.length ? 'Keine Viertel passen zu diesen Anzeige-Filtern.' : 'Für diesen Ort sind noch keine Viertel vorhanden.'));
    removed.hidden = !data.gestrichen.length; removed.replaceChildren(el('summary', {}, `Gestrichene Viertel (${data.gestrichen.length})`), ...data.gestrichen.map(card));
    count.textContent = `${rows.length} von ${data.viertel.length} aktiven Vierteln sichtbar.`;
    scope.querySelectorAll('details[data-edit]').forEach(n => { n.open = opened.has(n.dataset.edit); });
    sync(); drawMap();
    if (field && focusedId) { const replacement = scope.querySelector(`[data-district="${focusedId}"] [data-edit-field="${field}"]`); replacement?.focus({preventScroll:true}); if (replacement && range) replacement.setSelectionRange(...range); }
  }
  async function load({ afterWrite = false } = {}) {
    if (!live() || loading || (writing && !afterWrite)) return false;
    if (run !== null && !viertelId(run)) { notice.textContent = 'Ungültige Suchauftragsnummer.'; return false; }
    if (run === null && query.stadt.length < 2) { notice.textContent = 'Eine Stadt oder Insel eingeben, um vorhandene Viertel zu lesen.'; refresh.disabled = true; return false; }
    clearTimeout(timer); loading = true; sync(); notice.textContent = 'Viertel werden geladen …';
    try {
      const next = viertelAntwort(await call('unterkunft_viertel_lesen', query)); if (!live()) return false;
      if (run === null && viertelStadt(next.stadt) !== viertelStadt(query.stadt)) throw new Error('Die Antwort gehört zu einem anderen Ort.');
      data = next; uncertain = false; city.value = data.stadt;
      for (const id of selected) if (!data.viertel.some(z => z.id === id && z.status !== 'gestrichen')) selected.delete(id);
      const last = data.letzter_lauf;
      const generationError = typeof last?.ki?.fehler === 'string' ? last.ki.fehler.trim() : '';
      if (pendingGeneration && last?.id !== pendingGeneration.id && last?.id && ['fertig','fehler'].includes(last.status)) pendingGeneration = null;
      info.hidden = generatePanel.hidden = filterBox.hidden = selection.hidden = mapButton.hidden = false;
      if (!data.viertel.length) generatePanel.open = true;
      info.replaceChildren(el('h2', {}, data.stadt), el('p', {}, 'Automatische Viertelvorschläge sind ungeprüft. Beschreibungen helfen bei der Orientierung; fehlende Angaben bleiben unbekannt.'),
        el('details', {}, el('summary', {}, 'Wie entstehen die Noten?'), el('p', { class: 'small' }, data.noten_regeln || 'Noten sind Startannahmen. Fehlende Angaben bleiben unbekannt.')),
        el('p', { class: 'small' }, '© OpenStreetMap-Mitwirkende (ODbL).'),
        last ? el('p', { class: 'small' }, 'Letzte Ermittlung: ' + (({ki:'Beschreibungen werden ermittelt',osm_angefordert:'Umgebungsdaten werden geladen',fertig:'abgeschlossen',fehler:'fehlgeschlagen'})[last.status] || 'Status unbekannt') + (last.kosten_usd != null ? ' · ' + fmtUsd(last.kosten_usd) : '')) : null);
      generate.textContent = (data.viertel.length ? 'Viertel erneut ermitteln' : 'Viertel ermitteln') + ' · ca. 0,06 USD';
      if (generationError) info.append(el('p', { class: 'warning', role: 'alert' }, 'Viertel konnten nicht ermittelt werden: ' + generationError), el('p', { class: 'small' }, 'Vorhandene Viertel bleiben sichtbar. Umgebungsdaten können unabhängig davon weitergeladen werden.'));
      draw(); notice.textContent = pendingGeneration ? 'Ermittlung angefragt. Auf den neuen Lauf warten; es wird kein zweiter Auftrag ausgelöst.' : 'Viertel aktualisiert.';
      if (viertelId(focusZone)) { const id = focusZone; focusZone = null; jump(id); }
      if (pendingGeneration) { if (pendingGeneration.remaining-- > 0) timer = setTimeout(load,10000); else notice.textContent += ' Bitte später mit „Viertel aktualisieren“ nachsehen.'; }
      else if (isRunning()) timer = setTimeout(load,10000);
      return true;
    } catch (e) { if (live()) notice.textContent = 'Viertel nicht geladen: ' + e.message + ' Mit „Viertel aktualisieren“ erneut lesen.'; return false; }
    finally { loading = false; if (live()) sync(); }
  }
  async function decide(z, values) {
    if (loading || writing || uncertain) return;
    clearTimeout(timer); writing = true; sync(); notice.textContent = 'Viertel wird gespeichert …';
    try {
      const r = await call('unterkunft_zone_entscheiden', { id: z.id, ...values }); if (!live()) return;
      if (r.ok !== true || r.id !== z.id || r.status !== values.status) throw new Error('Die Änderung wurde nicht eindeutig bestätigt.');
      if (!await load({ afterWrite: true })) throw new Error('Der neue Stand konnte noch nicht gelesen werden.');
      const saved = [...data.viertel,...data.gestrichen].find(row => row.id === z.id);
      if (!saved || saved.status !== values.status || (values.name && saved.name !== values.name) || (values.notiz && saved.notiz_nutzer !== values.notiz)) throw new Error('Gelesener Stand stimmt noch nicht mit der Änderung überein.');
      drafts.delete(z.id); draw(); notice.textContent = 'Gespeichert: ' + saved.name + ' · ' + ({bestaetigt:'bestätigt',gestrichen:'gestrichen',vorschlag:'Vorschlag'})[saved.status] + '.'; jump(z.id);
    } catch (e) { if (live()) { uncertain = true; notice.textContent = 'Speichern nicht bestätigt: ' + e.message + ' Bitte zuerst den aktuellen Stand lesen.'; } }
    finally { writing = false; if (live()) sync(); }
  }
  async function create() {
    if (!data || loading || writing || uncertain || pendingGeneration || isRunning()) return;
    writing = true; pendingGeneration = { id: data.letzter_lauf?.id, remaining: 30 }; sync(); notice.textContent = 'Ermittlung wird angefragt …';
    try {
      const r = await call('unterkunft_viertel_erstellen', { stadt: data.stadt, ...(data.viertel.length ? {erneut:true} : {}) }); if (!live()) return;
      if (r.ok !== true || typeof r.hinweis !== 'string' || (r.stadt && viertelStadt(r.stadt) !== viertelStadt(data.stadt))) throw new Error('Die Ermittlung wurde nicht eindeutig bestätigt.');
      notice.textContent = 'Ermittlung angefragt. Der Fortschritt wird automatisch gelesen; bitte 1–5 Minuten einplanen.';
    } catch (e) { if (live()) notice.textContent = 'Start nicht bestätigt: ' + e.message + ' Der Status wird gelesen; es wird kein zweiter Auftrag ausgelöst.'; }
    finally { writing = false; if (live()) { sync(); timer = setTimeout(load,3000); } }
  }
  await load();
}
