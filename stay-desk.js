'use strict';
// W98 (Claude 20.10.2026): Tabelle am Rechner (kleine Zeilen, Spalten wählbar, sortieren, filtern, markieren, Massenbewertung)
// und Gründe/Notiz zu jedem Urteil inkl. Fakten-Schnappschuss fürs spätere Lernen. Kein Score, keine Automatik.

const STAY_GRUENDE_MINUS = [['preis','zu teuer'],['zu_klein','zu klein'],['lage','Lage'],['betten','Betten/Futon'],['stil','Stil'],['fotos','Fotos'],['bewertungen','Bewertungen'],['laerm','Lärm'],['storno','Storno'],['ausstattung','Ausstattung'],['sonstiges','Sonstiges']];
const STAY_GRUENDE_PLUS = [['plus_preis','Preis'],['plus_groesse','Größe'],['plus_lage','Lage'],['plus_stil','Stil'],['plus_fotos','Fotos'],['plus_ausstattung','Ausstattung'],['plus_betten','Betten'],['plus_bewertungen','Bewertungen'],['plus_storno','Storno']];
const STAY_GRUND_TEXT = Object.fromEntries([...STAY_GRUENDE_MINUS, ...STAY_GRUENDE_PLUS, ['groesse','Größe']]);
const STAY_URTEIL_STATUS = { favorit: 'favorit', vielleicht: 'vielleicht', weg: 'ausgeschlossen', offen: 'aktiv' };
const STAY_STATUS_URTEIL = { favorit: 'favorit', vielleicht: 'vielleicht', ausgeschlossen: 'weg' };
const STAY_URTEIL_ZEICHEN = { favorit: '★', vielleicht: '~', ausgeschlossen: '✕' };
const STAY_TYPEN = { apartment: 'Apartment', haus: 'Haus', machiya: 'Machiya', aparthotel: 'Aparthotel', hotel: 'Hotel', ryokan: 'Ryokan', hostel: 'Hostel', guesthouse: 'Gästehaus' };

function stayGruendeFuer(urteil) { return urteil === 'favorit' ? STAY_GRUENDE_PLUS : STAY_GRUENDE_MINUS; }
function stayNotiz(t) { const g = t?.rueckmeldung?.grund; return typeof g === 'string' && g.trim() ? g.trim() : null; }
function stayWarumText(t) { return (Array.isArray(t?.urteil_gruende) ? t.urteil_gruende : []).map(k => STAY_GRUND_TEXT[k] || k).join(' · ') || null; }
function stayTyp(t) { return STAY_TYPEN[t?.typ] || (typeof t?.typ === 'string' && t.typ ? t.typ : null); }
function stayNaechte(trip) { const n = (Date.parse(trip?.abreise) - Date.parse(trip?.anreise)) / 86400000; return n > 0 ? n : null; }
function stayNachtpreis(t, trip) { return stayFieldValue(t, 'nacht', trip || {}); }
function stayBesterTarif(t) { const g = t?.detail?.guenstigster; return g && sucheZahl(g.gesamt_eur) !== null ? g : null; }

// Storno: Tage zwischen Ende der kostenlosen Stornierung und Anreise (je kleiner, desto besser). null = unbekannt.
function stayStorno(t, trip) {
  const arrive = Date.parse(trip?.anreise);
  const text = typeof t?.angebot?.storno === 'string' ? t.angebot.storno : '';
  const tage = iso => { const until = Date.parse(String(iso).slice(0, 10) + 'T00:00:00Z'); return Number.isFinite(until) && Number.isFinite(arrive) ? { tage: Math.max(0, Math.round((arrive - until) / 86400000)), nein: false, bis: String(iso).slice(0, 10) } : null; };
  // 1) Angebot aus der Suche: „kostenlos bis 2026-10-29T15:00:00Z“
  const iso = (text.match(/\d{4}-\d{2}-\d{2}/) || [])[0];
  if (iso && !/nicht/i.test(text)) { const x = tage(iso); if (x) return x; }
  // 2) Detailabruf: günstigster kostenlos stornierbarer Tarif für die ganze Gruppe
  const d = t?.detail;
  if (d?.guenstigster_stornierbar?.storno_bis) { const x = tage(d.guenstigster_stornierbar.storno_bis); if (x) return x; }
  if (d?.guenstigster && !d.guenstigster_stornierbar) return { tage: null, nein: true, bis: null }; // Detailseite: kein kostenloser Tarif für die Gruppe
  return { tage: null, nein: false, bis: null };
}

// Preis im Vergleich zu Unterkünften derselben Art (nur unter den geladenen Treffern).
function stayVergleich(rows, trip) {
  const byTyp = new Map();
  for (const t of rows) { const p = stayNachtpreis(t, trip), k = stayTyp(t) || '?'; if (p !== null) { if (!byTyp.has(k)) byTyp.set(k, []); byTyp.get(k).push(p); } }
  const median = new Map([...byTyp].map(([k, xs]) => { const s = [...xs].sort((a, b) => a - b), m = s.length % 2 ? s[(s.length - 1) / 2] : (s[s.length / 2 - 1] + s[s.length / 2]) / 2; return [k, { m, n: s.length }]; }));
  return t => {
    const p = stayNachtpreis(t, trip), x = median.get(stayTyp(t) || '?');
    if (p === null || !x || x.n < 3) return null; // zu wenige Vergleichsfälle
    const ratio = p / x.m;
    return { ratio, label: ratio < 0.85 ? 'günstig' : ratio > 1.15 ? 'teuer' : 'normal', art: stayTyp(t) || 'Art unbekannt', n: x.n };
  };
}

function stayFakten(t, trip, vergleich) {
  const room = sucheZimmerKurz(t), st = stayStorno(t, trip), cmp = vergleich ? vergleich(t) : null, tarif = stayBesterTarif(t), n = sucheZahl;
  const f = {
    preis_nacht: n(stayNachtpreis(t, trip)) !== null ? Math.round(stayNachtpreis(t, trip)) : null, preis_gesamt: n(t.angebot?.preis_gesamt_eur),
    bester_tarif: tarif ? n(tarif.gesamt_eur) : null, tarif_storno: n(t.detail?.guenstigster_stornierbar?.gesamt_eur), m2: room.m2, schlafzimmer: room.schlafzimmer, betten: room.anzahl,
    betten_text: room.typen ? String(room.typen).slice(0, 120) : null, note: n(t.note) !== null ? Math.round(t.note * 100) / 100 : null, note_skala: n(t.note_skala), bewertungen: n(t.bewertungen),
    km: n(t.luftlinie_ziel_m) !== null ? Math.round(t.luftlinie_ziel_m / 100) / 10 : null, gehzeit_min: n(t.gehzeit_min),
    typ: t.typ || null, quelle: t.quelle || null, storno_tage: st.tage, storno_nein: st.nein || null,
    preis_vergleich: cmp ? cmp.label : null, viertel: t.zone?.name || null,
    kueche: t.detail?.merkmale?.kueche ?? null, waschmaschine: t.detail?.merkmale?.waschmaschine ?? null, balkon: stayFieldValue(t, 'balkon', trip || {}),
  };
  for (const k of Object.keys(f)) if (f[k] === null || f[k] === undefined) delete f[k];
  return f;
}

// Speichert ein Urteil mit Gründen/Notiz/Fakten und aktualisiert den Treffer im Speicher.
async function staySaveUrteil(call, t, urteil, { gruende = [], notiz, fakten } = {}) {
  const daten = { treffer_id: t.treffer_id, urteil, gruende };
  if (notiz !== undefined) daten.notiz = notiz;
  if (fakten) daten.fakten = fakten;
  const r = await call('unterkunft_durchsehen_urteil', daten);
  if (r?.ok !== true || r.urteil !== urteil) throw Error('Urteil nicht eindeutig bestätigt.');
  t.status = STAY_URTEIL_STATUS[urteil]; t.urteil_gruende = urteil === 'offen' ? null : (gruende.length ? gruende : null);
  if (urteil !== 'offen') t.rueckmeldung = { ...(t.rueckmeldung || {}), urteil, grund: r.notiz ?? (notiz !== undefined ? (notiz || null) : stayNotiz(t)) };
  return r;
}

// Kleiner Dialog: Urteil, Gründe und Notiz für eine Unterkunft.
function stayUrteilDialog(t, { call, live, trip, vergleich, onSaved, scope }) {
  let urteil = STAY_STATUS_URTEIL[t.status] || null;
  let gruende = [...(Array.isArray(t.urteil_gruende) ? t.urteil_gruende : [])];
  const dialog = el('dialog', { class: 'stay-candidate desk-urteil', 'aria-label': 'Urteil und Gründe' });
  const status = el('p', { role: 'status', class: 'small' });
  const notiz = el('textarea', { rows: 3, maxlength: 1000, 'aria-label': 'Notiz', placeholder: 'Notiz (optional) – z. B. „Balkon zum Fluss, Kinder hätten eigenes Zimmer“' });
  notiz.value = stayNotiz(t) || '';
  const chips = el('div', { class: 'desk-chips', role: 'group', 'aria-label': 'Gründe' });
  const urteile = el('div', { class: 'desk-urteile', role: 'group', 'aria-label': 'Urteil' });
  const save = el('button', { type: 'button', class: 'primary' }, 'Speichern');
  function draw() {
    urteile.replaceChildren(...[['favorit','★ Favorit'],['vielleicht','~ Na ja'],['weg','✕ Raus']].map(([k, label]) => el('button', { type: 'button', class: 'desk-u-' + k, 'aria-pressed': String(urteil === k), onclick: () => {
      if (urteil !== k) gruende = gruende.filter(g => stayGruendeFuer(k).some(([x]) => x === g)); urteil = k; draw(); } }, label)));
    chips.replaceChildren(...(urteil ? stayGruendeFuer(urteil) : []).map(([k, label]) => el('button', { type: 'button', 'aria-pressed': String(gruende.includes(k)), onclick: () => { gruende = gruende.includes(k) ? gruende.filter(x => x !== k) : [...gruende, k]; draw(); } }, label)));
    if (!urteil) chips.append(el('span', { class: 'small muted' }, 'Erst ein Urteil wählen.'));
    save.disabled = !urteil;
  }
  save.onclick = async () => {
    if (!urteil) return; save.disabled = true; status.textContent = 'Speichere …';
    try { await staySaveUrteil(call, t, urteil, { gruende, notiz: notiz.value.trim(), fakten: stayFakten(t, trip, vergleich) }); if (!live()) return; dialog.close(); onSaved?.(t); }
    catch (e) { if (live()) { status.textContent = 'Nicht gespeichert: ' + e.message; save.disabled = false; } }
  };
  dialog.append(el('h2', {}, t.name || 'Unterkunft'), urteile, el('h3', {}, 'Warum?'), chips, notiz, status,
    el('div', { class: 'actions' }, el('button', { type: 'button', onclick: () => dialog.close() }, 'Abbrechen'), save));
  draw();
  (scope || document.body).append(dialog); dialog.addEventListener('close', () => dialog.remove()); dialog.showModal();
  return dialog;
}

const STAY_DESK_SPALTEN = [
  { key: 'nacht', label: '€/Nacht', num: true, klein: true, v: (t, c) => stayNachtpreis(t, c.trip), r: (t, c) => { const v = stayNachtpreis(t, c.trip); return v === null ? '?' : (t.angebot?.preis_art === 'geschaetzt' ? 'ca. ' : '') + Math.round(v).toLocaleString('de-DE') + ' €'; } },
  { key: 'preis', label: 'Gesamt', num: true, klein: true, v: t => sucheZahl(t.angebot?.preis_gesamt_eur), r: t => sucheZahl(t.angebot?.preis_gesamt_eur) === null ? '?' : Math.round(t.angebot.preis_gesamt_eur).toLocaleString('de-DE') + ' €' },
  { key: 'tarif', label: 'Günstigster Tarif', num: true, klein: true, v: t => stayBesterTarif(t)?.gesamt_eur ?? null,
    r: (t, c) => { const g = stayBesterTarif(t); if (!g) return '?'; const n = stayNaechte(c.trip); return el('span', { title: [g.zimmer, ...(g.bedingungen || [])].filter(Boolean).join(' · ') }, Math.round(g.gesamt_eur).toLocaleString('de-DE') + ' €', null); } },
  { key: 'tarif_storno', label: 'Günstigster stornierbar', num: true, klein: true, v: t => sucheZahl(t?.detail?.guenstigster_stornierbar?.gesamt_eur),
    r: (t, c) => { const g = t?.detail?.guenstigster_stornierbar; if (!g || sucheZahl(g.gesamt_eur) === null) return t?.detail?.guenstigster ? 'keiner' : '?'; const s = stayStorno(t, c.trip); return el('span', { title: g.storno_bis ? 'kostenlos bis ' + g.storno_bis : '' }, Math.round(g.gesamt_eur).toLocaleString('de-DE') + ' €'); } },
  { key: 'vergleich', label: 'Preis ggü. Art', num: true, klein: true, v: (t, c) => c.vergleich(t)?.ratio ?? null,
    r: (t, c) => { const x = c.vergleich(t); return x ? el('span', { class: 'desk-cmp desk-cmp-' + (x.label === 'günstig' ? 'g' : x.label === 'teuer' ? 't' : 'n'), title: `${Math.round(x.ratio * 100)} % vom Mittel (${x.n} × ${x.art})` }, x.label) : '?'; } },
  { key: 'art', label: 'Art', v: t => stayTyp(t), r: t => stayTyp(t) || '?' },
  { key: 'schlafzimmer', label: 'SZ', num: true, v: t => sucheZimmerKurz(t).schlafzimmer, r: t => sucheZimmerKurz(t).schlafzimmer ?? '?' },
  { key: 'betten', label: 'Betten', num: true, v: t => sucheZimmerKurz(t).anzahl, r: t => { const r = sucheZimmerKurz(t); return r.anzahl === null && !r.typen ? '?' : el('span', { title: r.typen || '' }, r.anzahl ?? '?', r.typen && /futon|sofa|bunk|etagen/i.test(r.typen) ? el('small', { class: 'desk-warn', title: r.typen }, ' (Futon/Sofa)') : null); } },
  { key: 'm2', label: 'm²', num: true, v: t => sucheZimmerKurz(t).m2, r: t => sucheZimmerKurz(t).m2 ?? '?' },
  { key: 'note', label: 'Note', num: true, v: t => sucheZahl(t.note) !== null && sucheZahl(t.note_skala) ? t.note / t.note_skala * 10 : null,
    r: t => sucheZahl(t.note) === null ? '?' : Number(t.note).toLocaleString('de-DE', { maximumFractionDigits: 2 }) + '/' + (t.note_skala ?? '?') },
  { key: 'bewertungen', label: 'Bew.', num: true, v: t => sucheZahl(t.bewertungen), r: t => sucheZahl(t.bewertungen) === null ? '?' : Number(t.bewertungen).toLocaleString('de-DE') },
  { key: 'storno', label: 'Storno', num: true, klein: true, v: (t, c) => { const s = stayStorno(t, c.trip); return s.tage ?? (s.nein ? 9999 : null); },
    r: (t, c) => { const s = stayStorno(t, c.trip); return s.tage !== null ? el('span', { title: 'kostenlos bis ' + s.bis }, 'bis ' + s.tage + ' T.') : s.nein ? 'nein' : '?'; } },
  { key: 'km', label: 'km', num: true, klein: true, v: t => sucheZahl(t.luftlinie_ziel_m) === null ? null : t.luftlinie_ziel_m / 1000, r: t => sucheZahl(t.luftlinie_ziel_m) === null ? '?' : (t.luftlinie_ziel_m / 1000).toLocaleString('de-DE', { maximumFractionDigits: 1 }) },
  { key: 'gehzeit', label: 'Station', num: true, klein: true, v: t => sucheZahl(t.gehzeit_min), r: t => sucheZahl(t.gehzeit_min) === null ? '?' : el('span', { title: t.station_name || '' }, Math.round(t.gehzeit_min) + ' Min.') },
  { key: 'viertel', label: 'Viertel', v: t => t.zone?.name || null, r: t => t.zone?.name || '?' },
  { key: 'kueche', label: 'Küche', v: t => t.detail?.merkmale?.kueche ? 'ja' : null, r: t => t.detail?.merkmale?.kueche ? 'ja' : '?' },
  { key: 'waschmaschine', label: 'Waschm.', v: t => t.detail?.merkmale?.waschmaschine ? 'ja' : null, r: t => t.detail?.merkmale?.waschmaschine ? 'ja' : '?' },
  { key: 'balkon', label: 'Balkon', v: t => stayFieldValue(t, 'balkon', {}), r: t => stayFieldValue(t, 'balkon', {}) ?? '?' },
  // W100: weitere Kriterien aus Sebastians Auswahl (ja oder ?)
  ...[['klima', 'Klima'], ['fruehstueck', 'Frühst.'], ['pool', 'Pool'], ['sauna_spa', 'Sauna/Spa'], ['fitness', 'Fitness'], ['parkplatz', 'Parken'], ['wlan', 'WLAN'], ['meerblick', 'Meerblick']]
    .map(([key, label]) => ({ key, label, v: t => stayFieldValue(t, key, {}), r: t => stayFieldValue(t, key, {}) ?? '?' })),
  { key: 'strand', label: 'Strand', num: true, klein: true, v: t => sucheZahl(t.strand_m), r: t => stayStrandText(t) }, // W100: Luftlinie, auf 50 m gerundet
  { key: 'sterne', label: '★', num: true, v: t => sucheZahl(t.sterne), r: t => sucheZahl(t.sterne) ?? '?' },
  { key: 'hotelzimmer', label: 'Zi.', num: true, v: t => stayFieldValue(t, 'hotelzimmer', {}), r: t => stayFieldValue(t, 'hotelzimmer', {}) ?? '–' },
  { key: 'quelle', label: 'Quelle', v: t => SUCHE_QUELLEN[t.quelle] || t.quelle || null, r: t => { const p = sucheAnbieterLink(t); const name = SUCHE_QUELLEN[t.quelle] || t.quelle || '?'; return p ? el('a', { href: p.url, target: '_blank', rel: 'noopener noreferrer' }, name + ' ↗') : name; } },
  { key: 'warum', label: 'Warum', v: t => stayWarumText(t), r: null },
  { key: 'notiz', label: 'Notiz', v: t => stayNotiz(t), r: null },
];
const STAY_DESK_STANDARD = ['nacht','preis','tarif','tarif_storno','vergleich','art','schlafzimmer','betten','m2','note','bewertungen','storno','km','quelle','warum','notiz'];

function stayDeskSpalten() {
  const saved = stayRead('ks_tabelle_spalten', null), known = STAY_DESK_SPALTEN.map(s => s.key);
  return Array.isArray(saved) && saved.length && saved.every(k => known.includes(k)) && new Set(saved).size === saved.length ? saved : [...STAY_DESK_STANDARD];
}

// Filtertext je Spalte: „≥ 60“, „≤ 180“, „60–90“, Zahl allein (≤ bei Preis/Storno/km, sonst ≥), Text = enthält, „?“ = nur unbekannte.
function stayDeskFilter(text, spalte) {
  const s = String(text || '').trim(); if (!s) return null;
  if (s === '?') return v => v === null || v === undefined;
  if (!spalte.num) { const needle = s.toLocaleLowerCase('de'); return v => v === null || v === undefined || String(v).toLocaleLowerCase('de').includes(needle); }
  const num = x => Number(String(x).replace(/\./g, '').replace(',', '.'));
  let m = s.match(/^(?:(≥|>=|>|≤|<=|<))?\s*([\d.,]+)\s*$/), lo = -Infinity, hi = Infinity;
  if (m) { const x = num(m[2]); if (!Number.isFinite(x)) return null; const op = m[1] || (spalte.klein ? '≤' : '≥'); if (/[≥>]/.test(op)) lo = x; else hi = x; }
  else if ((m = s.match(/^([\d.,]+)\s*[-–]\s*([\d.,]+)$/))) { lo = num(m[1]); hi = num(m[2]); if (!Number.isFinite(lo) || !Number.isFinite(hi)) return null; }
  else return null;
  return v => v === null || v === undefined || (v >= lo && v <= hi); // unbekannte Angaben bleiben sichtbar (Sebastian 20.10.)
}

const stayDeskState = new Map();
function stayDeskTable({ rows, trip, call, live, onChanged, openDetail, scope }) {
  const id = trip?.id ?? 'x';
  if (!stayDeskState.has(id)) stayDeskState.set(id, { sel: new Set(), last: null, filter: {}, gruppe: stayRead('ks_tabelle_gruppe', 'alle'), sort: { key: 'nacht', dir: 1 }, undo: null, msg: '', bulkGruende: [], bulkNotiz: '', pending: false });
  const st = stayDeskState.get(id), vergleich = stayVergleich(rows, trip), ctx = { trip, vergleich }, fst = stayFilterState(id); // 0.36.0: Spaltenfilter = gemeinsamer Filter
  let spalten = stayDeskSpalten();
  const box = el('section', { class: 'card desk', 'aria-label': 'Tabelle' });
  const counts = { alle: rows.length, offen: rows.filter(t => !STAY_STATUS_URTEIL[t.status]).length, favorit: rows.filter(t => t.status === 'favorit').length, vielleicht: rows.filter(t => t.status === 'vielleicht').length, ausgeschlossen: rows.filter(t => t.status === 'ausgeschlossen').length };
  const gruppen = el('div', { class: 'desk-gruppen', role: 'group', 'aria-label': 'Nach Urteil zeigen' }, [['alle','Alle'],['offen','Ohne Urteil'],['favorit','★'],['vielleicht','~'],['ausgeschlossen','✕']].map(([k, label]) =>
    el('button', { type: 'button', 'aria-pressed': String(st.gruppe === k), onclick: () => { st.gruppe = k; stayWrite('ks_tabelle_gruppe', k); onChanged(); } }, `${label} ${counts[k]}`)));
  const spaltenWahl = el('details', { class: 'desk-spalten' }, el('summary', {}, 'Spalten'), el('div', { class: 'desk-spalten-panel' },
    el('p', { class: 'small muted' }, 'Gilt nur für die Tabelle. Reihenfolge mit ↑ ↓.'),
    el('ol', {}, spalten.map((k, i) => { const s = STAY_DESK_SPALTEN.find(x => x.key === k); const move = d => { const n = stayMove(spalten, i, i + d); stayWrite('ks_tabelle_spalten', n); onChanged(); };
      return el('li', {}, el('label', {}, el('input', { type: 'checkbox', checked: true, onchange: () => { stayWrite('ks_tabelle_spalten', spalten.filter(x => x !== k)); onChanged(); } }), s.label),
        el('button', { type: 'button', 'aria-label': s.label + ' nach vorne', disabled: i === 0, onclick: () => move(-1) }, '↑'), el('button', { type: 'button', 'aria-label': s.label + ' nach hinten', disabled: i === spalten.length - 1, onclick: () => move(1) }, '↓')); })),
    el('div', { class: 'desk-spalten-aus' }, STAY_DESK_SPALTEN.filter(s => !spalten.includes(s.key)).map(s => el('label', {}, el('input', { type: 'checkbox', onchange: () => { stayWrite('ks_tabelle_spalten', [...spalten, s.key]); onChanged(); } }), s.label))),
    el('button', { type: 'button', onclick: () => { stayWrite('ks_tabelle_spalten', [...STAY_DESK_STANDARD]); onChanged(); } }, 'Standard')));
  const anzahl = el('span', { class: 'small muted', role: 'status' });
  box.append(el('div', { class: 'desk-kopf' }, gruppen, el('span', { class: 'desk-hinweis small muted' }, 'Spalte klicken = sortieren · Feld darunter = filtern (≥ 60, ≤ 180, 60–90, ? = unbekannt) · Shift-Klick = Bereich'), spaltenWahl));

  const defs = spalten.map(k => STAY_DESK_SPALTEN.find(s => s.key === k)).filter(Boolean);
  const table = el('table', { class: 'desk-table' }), tbody = el('tbody');
  const alleBox = el('input', { type: 'checkbox', 'aria-label': 'Alle sichtbaren markieren' });
  const sortBtn = (key, label) => el('th', { scope: 'col', 'aria-sort': st.sort.key === key ? (st.sort.dir === 1 ? 'ascending' : 'descending') : 'none' },
    el('button', { type: 'button', 'data-sort': key, onclick: () => { st.sort = { key, dir: st.sort.key === key ? -st.sort.dir : 1 }; onChanged(); } }, label, st.sort.key === key ? (st.sort.dir === 1 ? ' ↑' : ' ↓') : ''));
  const filterZelle = s => { const input = el('input', { type: 'text', class: 'desk-filter', 'aria-label': 'Filter ' + s.label, value: (s.key === 'name' ? st.filter.name : fst.werte[s.key]) || '', placeholder: s.num ? (s.klein ? '≤' : '≥') : 'enthält', oninput: () => { if (s.key === 'name') st.filter.name = input.value; else { if (input.value.trim()) fst.werte[s.key] = input.value; else delete fst.werte[s.key]; fst.speichern(); } body(); } }); return el('th', {}, input); };
  table.append(el('thead', {},
    el('tr', {}, el('th', { class: 'desk-sel' }, alleBox), el('th', { class: 'desk-foto' }, el('span', { class: 'sr-only' }, 'Foto')), sortBtn('name', 'Name'), sortBtn('urteil', 'Urteil'), ...defs.map(s => sortBtn(s.key, s.label))),
    el('tr', { class: 'desk-filterzeile' }, el('th'), el('th'), filterZelle({ key: 'name', label: 'Name' }), el('th'), ...defs.map(filterZelle))), tbody);
  const scroller = el('div', { class: 'desk-scroll', tabindex: 0, role: 'region', 'aria-label': 'Unterkunftstabelle' }, table);
  box.append(scroller, anzahl);

  const wert = (t, key) => key === 'name' ? (t.name || null) : key === 'urteil' ? ({ favorit: 1, vielleicht: 2, ausgeschlossen: 3 }[t.status] ?? 0) : defs.concat(STAY_DESK_SPALTEN).find(s => s.key === key)?.v(t, ctx) ?? null;
  let sichtbar = [];
  function body() {
    const filters = [['name', stayDeskFilter(st.filter.name, { num: false })], ...defs.map(s => [s.key, stayDeskFilter(fst.werte[s.key], s)])].filter(([, f]) => f);
    const ohneUnbekannt = fst.unbekannteAus ? defs.filter(s => fst.werte[s.key]).map(s => s.key) : [];
    sichtbar = rows.filter(t => st.gruppe === 'alle' ? true : st.gruppe === 'offen' ? !STAY_STATUS_URTEIL[t.status] : t.status === st.gruppe)
      .filter(t => filters.every(([k, f]) => f(wert(t, k))) && ohneUnbekannt.every(k => wert(t, k) !== null))
      .sort((a, b) => { const x = wert(a, st.sort.key), y = wert(b, st.sort.key); if (x === null || y === null) return x === null && y === null ? a.treffer_id - b.treffer_id : x === null ? 1 : -1; return (typeof x === 'string' ? x.localeCompare(String(y), 'de') : x - y) * st.sort.dir || a.treffer_id - b.treffer_id; });
    for (const tid of [...st.sel]) if (!rows.some(t => t.treffer_id === tid)) st.sel.delete(tid);
    tbody.replaceChildren(...sichtbar.map((t, i) => {
      const box = el('input', { type: 'checkbox', checked: st.sel.has(t.treffer_id), 'aria-label': 'Markieren: ' + (t.name || 'Unterkunft'), onclick: e => {
        const an = e.currentTarget.checked;
        if (e.shiftKey && st.last !== null) { const j = sichtbar.findIndex(x => x.treffer_id === st.last); if (j >= 0) for (const x of sichtbar.slice(Math.min(i, j), Math.max(i, j) + 1)) an ? st.sel.add(x.treffer_id) : st.sel.delete(x.treffer_id); }
        an ? st.sel.add(t.treffer_id) : st.sel.delete(t.treffer_id); st.last = t.treffer_id; body(); } });
      const zeichen = STAY_URTEIL_ZEICHEN[t.status];
      const bearbeiten = () => stayUrteilDialog(t, { call, live, trip, vergleich, scope, onSaved: () => { st.msg = (t.name || 'Unterkunft') + ' gespeichert.'; onChanged(); } });
      const foto = sucheLink(t.bild);
      return el('tr', { 'data-hit': t.treffer_id, class: (st.sel.has(t.treffer_id) ? 'is-sel ' : '') + 'desk-s-' + (t.status || 'aktiv') },
        el('td', { class: 'desk-sel' }, box),
        el('td', { class: 'desk-foto' }, foto ? el('img', { src: foto, alt: '', loading: 'lazy', referrerpolicy: 'no-referrer', onerror: e => e.currentTarget.remove() }) : null),
        el('td', { class: 'desk-name' }, el('button', { type: 'button', class: 'desk-name-btn', title: t.name || '', onclick: () => openDetail?.(t) }, t.name || 'Ohne Namen')),
        el('td', { class: 'desk-urteil-zelle' }, el('button', { type: 'button', class: 'desk-badge desk-b-' + (t.status || 'aktiv'), 'aria-label': 'Urteil ändern: ' + (t.name || ''), onclick: bearbeiten }, zeichen || '·')),
        ...defs.map(s => {
          if (s.key === 'warum' || s.key === 'notiz') { const text = s.key === 'warum' ? stayWarumText(t) : stayNotiz(t);
            return el('td', { 'data-field': s.key, class: 'desk-text' }, el('button', { type: 'button', class: 'desk-edit', title: text || 'Grund oder Notiz eintragen', onclick: bearbeiten }, text || '＋')); }
          const v = s.r(t, ctx); return el('td', { 'data-field': s.key, class: (s.num ? 'desk-num' : '') + (v === '?' ? ' desk-unbekannt' : '') }, v);
        }));
    }));
    alleBox.checked = sichtbar.length > 0 && sichtbar.every(t => st.sel.has(t.treffer_id));
    alleBox.indeterminate = !alleBox.checked && sichtbar.some(t => st.sel.has(t.treffer_id));
    anzahl.textContent = `${sichtbar.length} von ${rows.length} Unterkünften` + (st.sel.size ? ` · ${st.sel.size} markiert` : '');
    leiste();
  }
  alleBox.onchange = () => { for (const t of sichtbar) alleBox.checked ? st.sel.add(t.treffer_id) : st.sel.delete(t.treffer_id); body(); };

  // Massenbewertung nur über markierte Zeilen (keine Regel-Automatik)
  const bar = el('div', { class: 'desk-bar', role: 'region', 'aria-label': 'Markierte bewerten' });
  const msg = el('p', { class: 'small', role: 'status' });
  const notizBulk = el('input', { type: 'text', maxlength: 1000, 'aria-label': 'Notiz für alle markierten', placeholder: 'Notiz für alle (optional)', value: st.bulkNotiz, oninput: () => { st.bulkNotiz = notizBulk.value; } });
  async function bewerten(urteil) {
    const ids = [...st.sel]; if (!ids.length || st.pending) return;
    const gueltig = urteil === 'offen' ? [] : st.bulkGruende.filter(g => stayGruendeFuer(urteil).some(([k]) => k === g));
    const fakten = Object.fromEntries(rows.filter(t => st.sel.has(t.treffer_id)).map(t => [t.treffer_id, stayFakten(t, trip, vergleich)]));
    st.pending = true; leiste();
    try {
      const daten = { treffer_ids: ids, urteil, gruende: gueltig, fakten };
      if (st.bulkNotiz.trim() && urteil !== 'offen') daten.notiz = st.bulkNotiz.trim();
      const r = await call('unterkunft_urteile_sammeln', daten); if (!live()) return;
      if (r?.ok !== true || !Number.isInteger(r.geaendert)) throw Error('Nicht bestätigt.');
      for (const t of rows) if (st.sel.has(t.treffer_id)) { t.status = STAY_URTEIL_STATUS[urteil]; t.urteil_gruende = gueltig.length ? gueltig : null; if (daten.notiz) t.rueckmeldung = { ...(t.rueckmeldung || {}), urteil, grund: daten.notiz }; }
      st.undo = r.rueckgaengig || null; st.msg = `${r.geaendert} Unterkünfte: ${({ favorit: '★ Favorit', vielleicht: '~ Na ja', weg: '✕ Raus', offen: 'Urteil gelöscht' })[urteil]}.`;
      st.sel.clear(); st.bulkGruende = []; st.bulkNotiz = '';
    } catch (e) { st.msg = 'Nicht gespeichert: ' + e.message; }
    finally { st.pending = false; if (live()) onChanged(); }
  }
  async function rueckgaengig() {
    const u = st.undo; if (!u || st.pending) return; st.pending = true; leiste();
    try {
      const r = await call(u.aktion, u.daten); if (!live()) return; if (r?.ok !== true) throw Error('Nicht bestätigt.');
      for (const e of (u.daten?.eintraege || [])) { const t = rows.find(x => x.treffer_id === e.treffer_id); if (t) { t.status = STAY_URTEIL_STATUS[e.urteil] || 'aktiv'; t.urteil_gruende = Array.isArray(e.gruende) && e.gruende.length ? e.gruende : null; } }
      st.undo = null; st.msg = 'Rückgängig gemacht.';
    } catch (e) { st.msg = 'Rückgängig fehlgeschlagen: ' + e.message; }
    finally { st.pending = false; if (live()) onChanged(); }
  }
  function leiste() {
    msg.replaceChildren(...[st.msg || '', st.undo ? el('button', { type: 'button', class: 'desk-undo', disabled: st.pending, onclick: rueckgaengig }, 'Rückgängig') : null].filter(x => x !== null));
    const n = st.sel.size;
    bar.hidden = n === 0;
    if (!n) return;
    const chip = ([k, label]) => el('button', { type: 'button', 'aria-pressed': String(st.bulkGruende.includes(k)), disabled: st.pending, onclick: () => { st.bulkGruende = st.bulkGruende.includes(k) ? st.bulkGruende.filter(x => x !== k) : [...st.bulkGruende, k]; leiste(); } }, label);
    bar.replaceChildren(
      el('strong', {}, n + ' markiert'),
      el('div', { class: 'desk-bar-knoepfe' }, ...[['favorit','★ Favorit'],['vielleicht','~ Na ja'],['weg','✕ Raus'],['offen','Urteil löschen']].map(([k, label]) => el('button', { type: 'button', class: 'desk-u-' + k, disabled: st.pending, onclick: () => bewerten(k) }, label)),
        el('button', { type: 'button', disabled: st.pending, onclick: () => { st.sel.clear(); body(); } }, 'Markierung aufheben')),
      el('details', { class: 'desk-bar-gruende', open: st.bulkGruende.length > 0 || !!st.bulkNotiz }, el('summary', {}, 'Grund / Notiz für alle (optional)' + (st.bulkGruende.length ? ` · ${st.bulkGruende.length} gewählt` : '')),
        el('div', { class: 'desk-chips' }, el('span', { class: 'small muted' }, 'bei ✕ / ~:'), ...STAY_GRUENDE_MINUS.map(chip)),
        el('div', { class: 'desk-chips' }, el('span', { class: 'small muted' }, 'bei ★:'), ...STAY_GRUENDE_PLUS.map(chip)), notizBulk));
  }
  box.append(msg, bar);
  body();
  return box;
}

// Gründe-Leiste nach einem Urteil beim Wischen: ein Tipp genügt, wird sofort gespeichert. Kein Pflichtfeld.
function stayGrundLeiste(r, { call, live, trip, onDone }) {
  const t = r.t, urteil = r.urteil;
  let gruende = [...(Array.isArray(r.gruende) ? r.gruende : [])], timer = null;
  const status = el('span', { class: 'small muted', role: 'status' });
  const notiz = el('input', { type: 'text', maxlength: 1000, class: 'grund-notiz', 'aria-label': 'Notiz zu ' + (t.name || 'Unterkunft'), placeholder: '📝 Notiz (optional)', value: stayNotiz(t) || '' });
  const chips = el('div', { class: 'desk-chips', role: 'group', 'aria-label': 'Gründe' });
  async function speichern(mitNotiz) {
    status.textContent = 'Speichere …';
    try { await staySaveUrteil(call, t, urteil, { gruende, ...(mitNotiz ? { notiz: notiz.value.trim() } : {}), fakten: stayFakten(t, trip) }); r.gruende = gruende; if (live()) status.textContent = 'Gespeichert.'; }
    catch (e) { if (live()) status.textContent = 'Nicht gespeichert: ' + e.message; }
  }
  function draw() { chips.replaceChildren(...stayGruendeFuer(urteil).map(([k, label]) => el('button', { type: 'button', 'aria-pressed': String(gruende.includes(k)), onclick: () => { gruende = gruende.includes(k) ? gruende.filter(x => x !== k) : [...gruende, k]; draw(); clearTimeout(timer); timer = setTimeout(() => speichern(false), 500); } }, label))); }
  notiz.addEventListener('change', () => speichern(true));
  notiz.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); notiz.blur(); } });
  draw();
  return el('section', { class: 'grund-leiste', 'aria-label': 'Warum?' },
    el('div', { class: 'grund-kopf' }, el('strong', {}, ({ favorit: '★ Favorit', vielleicht: '~ Na ja', weg: '✕ Raus' })[urteil] + ' – warum?'), el('span', { class: 'small muted grund-name' }, t.name || ''),
      el('button', { type: 'button', class: 'grund-zu', 'aria-label': 'Leiste schließen', onclick: () => onDone?.() }, '✓')),
    chips, el('div', { class: 'grund-fuss' }, notiz, status));
}

// W98c: Urteils-Filter für Liste und Karte – Chips einzeln an/aus (und/oder), „Alle“ = alles inkl. Raus.
const STAY_URTEIL_FILTER_STANDARD = ['offen', 'favorit', 'vielleicht'];
function stayUrteilKey(t) { return { favorit: 'favorit', vielleicht: 'vielleicht', ausgeschlossen: 'raus' }[t?.status] || 'offen'; }
function stayUrteilFilter() {
  const v = stayRead('ks_urteil_filter', null);
  return new Set(Array.isArray(v) && v.length && v.every(k => ['offen', 'favorit', 'vielleicht', 'raus'].includes(k)) ? v : STAY_URTEIL_FILTER_STANDARD);
}
function stayUrteilChips(rows, onChange) {
  const an = stayUrteilFilter(), relevant = rows.filter(t => t.topf !== 'ausgeschlossen' || STAY_STATUS_URTEIL[t.status]);
  const zahl = k => relevant.filter(t => stayUrteilKey(t) === k).length, alle = ['offen', 'favorit', 'vielleicht', 'raus'];
  const setze = next => { stayWrite('ks_urteil_filter', [...next]); onChange(); };
  // 0.36.0: kurze sichtbare Beschriftung (passt in eine Zeile), voller Name bleibt für Vorlesen/Tests erhalten
  const kurz = { favorit: '★', vielleicht: '~', offen: '○', raus: '✕' };
  const chip = (k, label) => el('button', { type: 'button', class: 'urteil-chip uc-' + k, 'aria-label': `${label} ${zahl(k)}`, title: label, 'aria-pressed': String(an.has(k)), onclick: () => { const n = new Set(an); n.has(k) ? n.delete(k) : n.add(k); setze(n.size ? n : new Set(STAY_URTEIL_FILTER_STANDARD)); } }, `${kurz[k]} ${zahl(k)}`);
  return el('div', { class: 'urteil-chips', role: 'group', 'aria-label': 'Nach Urteil zeigen' },
    el('button', { type: 'button', class: 'urteil-chip uc-alle', 'aria-label': `Alle ohne Raus ${relevant.length - zahl('raus')}`, 'aria-pressed': String(STAY_URTEIL_FILTER_STANDARD.every(k => an.has(k)) && !an.has('raus')), onclick: () => setze(new Set(STAY_URTEIL_FILTER_STANDARD)) }, `Ohne Raus ${relevant.length - zahl('raus')}`),
    el('button', { type: 'button', class: 'urteil-chip uc-alles', 'aria-label': `Alles inkl. Raus ${relevant.length}`, 'aria-pressed': String(alle.every(k => an.has(k))), onclick: () => setze(new Set(alle)) }, `Alle ${relevant.length}`),
    el('span', { class: 'uc-trenner', 'aria-hidden': 'true' }),
    chip('favorit', '★ Favoriten'), chip('vielleicht', '~ Na ja'), chip('offen', 'Offen'), chip('raus', '✕ Raus'));
}

// ===== 0.36.0 (Sebastian 21.10.: „Spalten = Filter“): ein gemeinsamer Filter für Liste, Karte, Durchsehen und Tabelle =====
// Werte im Tabellen-Format („≤ 150“, „≥ 8“, „2–3“, Text = enthält). Unbekannte Angaben bleiben sichtbar, außer „Unbekannte ausblenden“.
const stayFilterStates = new Map();
function stayFilterState(id) {
  const key = 'ks_spaltenfilter:' + (id ?? 'x');
  if (!stayFilterStates.has(key)) {
    let v = null; try { v = JSON.parse(sessionStorage.getItem(key) || 'null'); } catch { /* ohne Speicher */ }
    const werte = v && typeof v.werte === 'object' && !Array.isArray(v.werte) ? Object.fromEntries(Object.entries(v.werte).filter(([, x]) => typeof x === 'string' && x)) : {};
    const st = { werte, unbekannteAus: v?.unbekannteAus === true, speichern() { try { sessionStorage.setItem(key, JSON.stringify({ werte: st.werte, unbekannteAus: st.unbekannteAus })); } catch { /* ohne Speicher */ } } };
    stayFilterStates.set(key, st);
  }
  return stayFilterStates.get(key);
}
function stayFilterAktiv(st) { return Object.values(st.werte).filter(Boolean).length + (st.unbekannteAus ? 1 : 0); }
function stayFilterFunktionen(st, spalten = stayDeskSpalten()) {
  return spalten.map(k => STAY_DESK_SPALTEN.find(s => s.key === k)).filter(s => s && st.werte[s.key]).map(s => [s, stayDeskFilter(st.werte[s.key], s)]).filter(([, f]) => f);
}
function stayFilterPasst(t, ctx, st, fns) {
  for (const [s, f] of fns) { const v = s.v(t, ctx); if ((v === null || v === undefined) && st.unbekannteAus) return false; if (!f(v ?? null)) return false; }
  return true;
}
// Darstellung je Spalte im Filterfenster: Chips mit Stufen, Eingabefeld oder „nur mit“
const STAY_FILTER_FORM = {
  nacht: { feld: 'bis', einheit: '€', icon: 'korb', titel: 'Preis pro Nacht bis' }, preis: { feld: 'bis', einheit: '€', icon: 'korb', titel: 'Gesamtpreis bis' },
  tarif: { feld: 'bis', einheit: '€', icon: 'korb', titel: 'Günstigster Tarif bis' }, tarif_storno: { feld: 'bis', einheit: '€', icon: 'storno', titel: 'Günstigster stornierbar bis' },
  vergleich: { icon: 'regler', titel: 'Preis ggü. gleicher Art', chips: [['≤ 0,85', 'günstig'], ['≤ 1,15', 'normal oder günstig']] },
  schlafzimmer: { icon: 'bett', titel: 'Schlafzimmer ab', chips: [['≥ 1', '1'], ['≥ 2', '2'], ['≥ 3', '3'], ['≥ 4', '4']] },
  hotelzimmer: { icon: 'hotel', titel: 'Hotelzimmer ab', chips: [['≥ 1', '1'], ['≥ 2', '2'], ['≥ 3', '3']] },
  betten: { icon: 'bett', titel: 'Schlafplätze ab', chips: [['≥ 2', '2'], ['≥ 3', '3'], ['≥ 4', '4'], ['≥ 5', '5']] },
  m2: { feld: 'ab', einheit: 'm²', icon: 'flaeche', titel: 'Fläche ab' },
  note: { icon: 'stern', titel: 'Gästenote ab', chips: [['≥ 7', '7'], ['≥ 8', '8'], ['≥ 8,5', '8,5'], ['≥ 9', '9']] },
  bewertungen: { icon: 'personen', titel: 'Bewertungen ab', chips: [['≥ 10', '10'], ['≥ 50', '50'], ['≥ 100', '100'], ['≥ 500', '500']] },
  storno: { icon: 'storno', titel: 'Stornierung', chips: [['≤ 9998', 'kostenlos stornierbar']] },
  km: { icon: 'pin', titel: 'Entfernung zum Ziel bis', chips: [['≤ 1', '1 km'], ['≤ 3', '3 km'], ['≤ 5', '5 km'], ['≤ 10', '10 km']] },
  gehzeit: { icon: 'bahn', titel: 'Zur Station bis', chips: [['≤ 5', '5 Min'], ['≤ 10', '10 Min'], ['≤ 15', '15 Min']] },
  strand: { icon: 'strand', titel: 'Strand bis', chips: [['≤ 200', '200 m'], ['≤ 500', '500 m'], ['≤ 1000', '1 km']] },
  sterne: { icon: 'hotel', titel: 'Sterne ab', chips: [['≥ 3', '3'], ['≥ 4', '4'], ['≥ 5', '5']] },
  art: { icon: 'haus', titel: 'Art', werte: true }, viertel: { icon: 'pin', titel: 'Viertel', werte: true }, quelle: { icon: 'extern', titel: 'Quelle', werte: true },
};
const STAY_FILTER_JA = ['kueche', 'waschmaschine', 'balkon', 'klima', 'fruehstueck', 'pool', 'sauna_spa', 'fitness', 'parkplatz', 'wlan', 'meerblick'];
function stayFilterBlatt({ rows: rowsQ, ctx: ctxQ, st, onChange }) {
  const R = typeof rowsQ === 'function' ? rowsQ : () => rowsQ, C = typeof ctxQ === 'function' ? ctxQ : () => ctxQ;
  const box = el('div', { class: 'af-liste' });
  function setze(key, wert) { if (wert) st.werte[key] = wert; else delete st.werte[key]; st.speichern(); onChange(); zeichnen(); }
  const chipReihe = (key, opts) => el('div', { class: 'af-chips', role: 'group' }, [['', 'Egal'], ...opts].map(([v, text]) => el('button', { type: 'button', class: 'af-chip', 'aria-pressed': String((st.werte[key] || '') === v), onclick: () => setze(key, (st.werte[key] || '') === v ? '' : v) }, text)));
  const titel = (icon, text) => el('span', { class: 'af-titel' }, stayIcon(icon), text);
  function zeichnen() {
    const spalten = stayDeskSpalten(), teile = [], ja = [], preise = [];
    const KURZ = { nacht: 'pro Nacht', preis: 'gesamt', tarif: 'günstigster Tarif', tarif_storno: 'stornierbar' };
    for (const k of spalten) {
      const s = STAY_DESK_SPALTEN.find(x => x.key === k), f = STAY_FILTER_FORM[k];
      if (!s) continue;
      if (STAY_FILTER_JA.includes(k)) { ja.push(s); continue; }
      if (!f) continue;
      if (f.feld) {
        const zahl = String(st.werte[k] || '').replace(/^[≤≥<>=]+\s*/, '');
        const input = el('input', { type: 'text', inputmode: 'decimal', placeholder: 'egal', value: zahl, 'aria-label': f.titel, onchange: () => { const x = input.value.trim(); setze(k, x ? (f.feld === 'bis' ? '≤ ' : '≥ ') + x : ''); } });
        if (KURZ[k]) { if (!preise.length) teile.push(null); preise.push(el('label', { class: 'af-preis', 'data-spalte': k }, el('span', {}, KURZ[k]), el('span', { class: 'af-eingabe' }, input, el('span', { class: 'af-einheit' }, f.einheit)))); continue; }
        teile.push(el('label', { class: 'af-zeile af-feld', 'data-spalte': k }, titel(f.icon, f.titel), el('span', { class: 'af-eingabe' }, input, el('span', { class: 'af-einheit' }, f.einheit))));
      } else if (f.werte) {
        const vals = [...new Set(R().map(t => s.v(t, C())).filter(v => typeof v === 'string' && v))].sort((a, b) => a.localeCompare(b, 'de')).slice(0, 12);
        if (!vals.length) continue;
        teile.push(el('div', { class: 'af-zeile', 'data-spalte': k }, titel(f.icon, f.titel), chipReihe(k, vals.map(v => [v, v]))));
      } else teile.push(el('div', { class: 'af-zeile', 'data-spalte': k }, titel(f.icon, f.titel), chipReihe(k, f.chips)));
    }
    if (ja.length) teile.push(el('div', { class: 'af-zeile', 'data-spalte': 'ausstattung' }, titel('pool', 'Nur mit'), el('div', { class: 'af-chips', role: 'group', 'aria-label': 'Nur mit' },
      ja.map(s => el('button', { type: 'button', class: 'af-chip', 'aria-pressed': String(st.werte[s.key] === 'ja'), onclick: () => setze(s.key, st.werte[s.key] === 'ja' ? '' : 'ja') }, STAY_FIELDS[s.key] || s.label)))));
    const pi = teile.indexOf(null); if (pi >= 0) teile[pi] = el('div', { class: 'af-zeile', 'data-spalte': 'preise' }, titel('korb', 'Preis bis'), el('div', { class: 'af-preise' }, preise));
    if (!teile.length) teile.push(el('p', { class: 'small muted' }, 'Keine filterbaren Spalten gewählt.'));
    const aus = el('input', { type: 'checkbox', onchange: () => { st.unbekannteAus = aus.checked; st.speichern(); onChange(); } }); aus.checked = st.unbekannteAus;
    const wahl = el('details', { class: 'af-mehr af-spalten' }, el('summary', {}, 'Felder wählen (gleich wie Tabellenspalten)'),
      el('div', { class: 'af-chips' }, STAY_DESK_SPALTEN.filter(s => STAY_FILTER_FORM[s.key] || STAY_FILTER_JA.includes(s.key)).map(s => el('button', { type: 'button', class: 'af-chip', 'aria-pressed': String(spalten.includes(s.key)),
        onclick: () => { const n = spalten.includes(s.key) ? spalten.filter(k => k !== s.key) : [...spalten, s.key]; if (!n.length) return; if (!n.includes(s.key)) delete st.werte[s.key]; stayWrite('ks_tabelle_spalten', n); st.speichern(); onChange(); zeichnen(); wahl.open = true; } }, STAY_FIELDS[s.key] || s.label))));
    const offen = box.querySelector('.af-spalten')?.open;
    box.replaceChildren(...teile, el('label', { class: 'af-schalter' }, aus, el('span', {}, el('b', {}, 'Unbekannte Angaben ausblenden'), el('small', {}, 'sonst bleiben z. B. Unterkünfte ohne Flächenangabe sichtbar'))), wahl);
    if (offen) wahl.open = true;
  }
  zeichnen();
  return { node: box, zeichnen, zuruecksetzen() { st.werte = {}; st.unbekannteAus = false; st.speichern(); onChange(); zeichnen(); } };
}
