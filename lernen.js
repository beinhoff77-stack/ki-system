/* W150: Lernen Schule – Lernreise der Kinder in der App.
   Spricht mit der Serverfunktion lernen-api (gleiche Anmeldung wie app-api). Die Datenbank prüft Zugriff,
   bewertet Antworten und führt Lernstand, Sterne und Stempel; die App zeigt nur an und schickt Eingaben.
   Ansichten:
     #/lernen                      Eltern: Mathe-Merkblatt, Lernreisen der Kinder, Belohnungen und Einlösungen
     #/reise/<kind>                Kind: Heute dran (aktueller Ort auf der echten Weltkarte)
     #/weltkarte/<kind>            → Mein Weg · Karte (K2)
     #/weg/<kind>[-stand|-kontinente|-karte] Kind: Mein Weg mit Reitern Stand · Kontinente · Karte
     #/merkheft/<kind>             Kind: Merkheft – nur Geschafftes, Kontinent → Flug → Etappe, durchsuchbar
     #/reisepass/<kind>            Kind: Stempel, Sterne, Belohnungen, Look wählen
     #/lerneinheit/<kind>-<einheit>[-<etappe>|-test] Kind: Etappen-Weg, Etappe (erklärt → selbst probieren), Test
   Karte: echte Weltkarte (lernen-welt.js), jedes Mathe-Gebiet liegt fest auf einem Erdteil, jeder Ort ist eine echte Stadt. */
'use strict';

const lernApi = () => API.replace('/app-api', '/lernen-api'); // API kommt aus app.js (wird danach geladen)
const LZ_STATUS = { offen: 'offen', nachgewiesen: 'geschafft', korrigiert: 'verbessert', gesichert: 'sicher', fehler: 'noch üben' };
const LZ_KLASSE = { offen: '', nachgewiesen: 'neu', korrigiert: 'neu', gesichert: 'neu', fehler: 'fehler' };
const LERN_ERDTEIL = { zahlen: 'EU', algebra: 'AS', geld: 'NA', geometrie: 'AF', raum: 'SA', daten: 'OC', funktionen: 'AN' };
const LERN_WELTEN = [['Ozean', 'Ozean'], ['Nacht', 'Nacht'], ['Dschungel', 'Dschungel'], ['Wüste', 'Wüste']];
const LERN_STILE = [['entdecker', 'Entdecker', 'verspielt, große Knöpfe'], ['studio', 'Studio', 'klar und sachlich']];

async function lernCall(aktion, daten = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (store.token) headers.Authorization = 'Bearer ' + store.token;
  const r = await fetch(mitRegion(lernApi() + '/aktion'), { method: 'POST', headers, body: JSON.stringify({ aktion, daten }) });
  let j; try { j = await r.json(); } catch { j = { ok: false, fehler: 'Keine Antwort (' + r.status + ')' }; }
  if (r.status === 401) { store.token = null; route('login'); throw new Error('Nicht angemeldet'); }
  if (!j.ok) throw new Error(j.fehler || 'Fehler bei ' + aktion);
  return j.ergebnis;
}
const lernCid = () => (crypto.randomUUID ? crypto.randomUUID() : Date.now() + '-' + Math.random().toString(16).slice(2));
// DOM-Helfer: null/undefined/false überspringen (sonst schreibt der Browser das Wort „null“ in die Seite).
const lernKinder = (kids) => kids.flat().filter((k) => k !== null && k !== undefined && k !== false);
const lernErsetze = (node, ...kids) => { node.replaceChildren(...lernKinder(kids)); return node; };
const lernAnhaengen = (node, ...kids) => { node.append(...lernKinder(kids)); return node; };
const lernText = (t) => String(t ?? '').replace(/(\d) (?=\d{3}(?!\d))/g, '$1 '); // Zahlen wie 20 000 nicht umbrechen
const lernZahl = (n) => Number(n).toLocaleString('de-DE').replace(/\./g, ' ').replace('-', '−'); // Tausender mit Leerzeichen, echtes Minuszeichen
const lernIcon = (d, size = 24) => {
  const s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  s.setAttribute('viewBox', '0 0 24 24'); s.setAttribute('width', size); s.setAttribute('height', size); s.setAttribute('aria-hidden', 'true');
  s.setAttribute('fill', 'none'); s.setAttribute('stroke', 'currentColor'); s.setAttribute('stroke-width', '2.2'); s.setAttribute('stroke-linecap', 'round'); s.setAttribute('stroke-linejoin', 'round');
  for (const p of d.split('|')) { const e = document.createElementNS('http://www.w3.org/2000/svg', 'path'); e.setAttribute('d', p); lernAnhaengen(s, e); }
  return s;
};
const LI = {
  heute: 'M3 11l9-7 9 7v9H5z', karte: 'M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2z|M9 4v14|M15 6v14', pass: 'M6 3h12a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z|M9 11a3 3 0 1 0 6 0a3 3 0 1 0-6 0|M9 17h6',
  stern: 'M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.4 6.7 19.4l1.2-6L3.4 9.3l6-.7z', stempel: 'M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18z|M12 8a4 4 0 1 0 0 8a4 4 0 1 0 0-8z',
  tag: 'M4 6h16v14H4z|M4 10h16|M8 3v4|M16 3v4', pfeil: 'M9 6l6 6-6 6', ort: 'M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z|M12 8a2 2 0 1 0 0 4a2 2 0 1 0 0-4z',
  zurueck: 'M3 12a9 9 0 1 0 3-6.7|M3 4v5h5', haken: 'M5 12l5 5 9-10',
  weg: 'M5 19c4 0 3-6 7-6s3-6 7-6|M3 19a2 2 0 1 0 4 0a2 2 0 1 0-4 0|M17 7a2 2 0 1 0 4 0a2 2 0 1 0-4 0', heft: 'M6 3h11a1 1 0 0 1 1 1v16H7a2 2 0 0 1-2-2V4a1 1 0 0 1 1-1z|M9 8h6|M9 12h6',
};

// ---------- Daten je Kind ----------
// Lehrplan-Reihenfolge eines Flugs im Ort (Feld „reihenfolge“ der Übersicht: Zahl oder {gym_by: 3, …}); fehlt es, bleibt die bisherige Ordnung.
const lernReihe = (e, kind) => { const r = e?.reihenfolge; if (r === null || r === undefined) return 1e9; if (typeof r === 'number') return r; return Number(r[kind?.schulart || 'gym_by'] ?? 1e9); };
// Ordnet die Orte eines Kindes: Jetzt dran · Kann schon · Später (nach Route und Klassenstufe); mit Stand je Einheit.
function lernReiseDaten(u, kindId) {
  const kind = (u.lernende || []).find((k) => k.id === kindId);
  if (!kind) return null;
  const stand = new Map((kind.stand || []).map((s) => [s.einheit_id, s]));
  const route = new Map((kind.route || []).filter((r) => r.status !== 'entfernt').sort((a, b) => (a.art === 'rueckreise') - (b.art === 'rueckreise')).map((r) => [r.block_id, r]));
  // E-2: Flüge, die Eltern/Lehrer im Plan abgewählt haben (route.ausgelassen = thema_id), sieht das Kind nicht. Ohne das Feld: alle Flüge.
  const ausgelassen = new Map((kind.route || []).filter((r) => r.art === 'normal' && r.status !== 'entfernt').map((r) => [r.block_id, r.ausgelassen || []]));
  const einheiten = (u.einheiten || []).filter((e) => (e.status !== 'entwurf' || kind.ist_test) && !(e.thema_id && ausgelassen.get(e.block_id)?.includes(e.thema_id)));
  // Themenplan (Eltern/Lehrer): Gibt es ihn, kommen nur Orte aus dem Plan dran – in seiner Reihenfolge.
  const mitPlan = (kind.route || []).some((r) => r.art === 'normal' && r.status !== 'entfernt');
  // M4: Klasse eines Ortes = kleinste Klasse seiner geplanten Flüge (Schulart des Kindes). Liegen alle über der Klasse des Kindes, kommt der Ort unter „Später“ –
  // außer Eltern/Lehrer haben ihn bewusst vorgezogen (im Plan vor einem Ort der eigenen oder einer früheren Klasse) oder das Kind hat dort schon angefangen.
  const saK = kind.schulart || 'gym_by';
  const ortKl = new Map(); const ortKlSet = new Map(); // P2: alle Klassen der geplanten Flüge je Ort (gleiche Regel wie „Stand“)
  for (const t of Array.isArray(u.themen) ? u.themen : u.einheiten || []) {
    if (!t.block_id || (t.thema_id && ausgelassen.get(t.block_id)?.includes(t.thema_id))) continue;
    const k0 = Number(t.jahrgang?.[saK] ?? (Array.isArray(u.themen) ? null : t.ziel_klasse)); if (!k0) continue;
    ortKl.set(t.block_id, Math.min(ortKl.get(t.block_id) ?? 99, k0));
    if (!ortKlSet.has(t.block_id)) ortKlSet.set(t.block_id, new Set()); ortKlSet.get(t.block_id).add(k0);
  }
  const planReihe = (kind.route || []).filter((r) => r.art === 'normal' && r.status !== 'entfernt').sort((a, b) => a.position - b.position).map((r) => r.block_id);
  const ueber = (b) => !!kind.klasse && (ortKl.get(b) ?? 0) > kind.klasse;
  const vorgezogen = (b) => { const i = planReihe.indexOf(b); return i >= 0 && planReihe.slice(i + 1).some((x) => ortKl.has(x) && !ueber(x)); };
  const gruppe = (e) => {
    const r = route.get(e.block_id);
    if (kind.ist_test || !kind.route?.length) return 'jetzt';
    if (mitPlan && !r) { // nicht im Plan: frühere Klassen heißen „zum Auffrischen“, der Rest „später“
      const k0 = e.jahrgang?.[kind.schulart || 'gym_by'] ?? e.ziel_klasse;
      return k0 && kind.klasse && k0 < kind.klasse ? 'frueher' : 'spaeter';
    }
    if (r?.kann_schon || r?.status === 'fertig') return 'kann'; // geschaffte Orte wandern zu „zum Wiederholen“
    if (mitPlan && ueber(e.block_id) && !vorgezogen(e.block_id)) { const s0 = stand.get(e.id) || {}; if (!Number(s0.fertig || 0) && !s0.laeuft && !s0.blocktest) return 'spaeter'; }
    if (mitPlan) return 'jetzt'; // im Plan: Eltern/Lehrer haben es bewusst eingeplant
    // Ohne Plan entscheidet die Klasse laut Lehrplan der Schulart: höhere Klassen später,
    // frühere Klassen nur zum Auffrischen (außer das Kind hat dort schon angefangen), die eigene Klasse ist dran.
    const kl = e.jahrgang?.[kind.schulart || 'gym_by'] ?? e.ziel_klasse;
    if (kl && kind.klasse && kl > kind.klasse) return 'spaeter';
    const s = stand.get(e.id) || {};
    if (kl && kind.klasse && kl < kind.klasse && !Number(s.fertig || 0) && !s.laeuft && !s.blocktest) return 'frueher';
    return 'jetzt';
  };
  const ortNr = new Map((u.orte || []).map((o, i) => [o.block_id, i])); // Reihenfolge der Weltreise
  const pos = (e) => route.get(e.block_id)?.position ?? (mitPlan ? 1e9 : 1e6 + (ortNr.get(e.block_id) ?? 9999));
  const mit = einheiten.map((e) => {
    const s = stand.get(e.id) || {};
    const n = e.pflicht_anzahl || 0, f = Number(s.fertig || 0);
    return { ...e, gruppe: gruppe(e), fertig: f, n, geschafft: n > 0 && f >= n, fehler: Number(s.fehler || 0), laeuft: !!s.laeuft, blocktest: !!s.blocktest, ortFertig: route.get(e.block_id)?.status === 'fertig' };
  }).sort((a, b) => pos(a) - pos(b) || lernReihe(a, kind) - lernReihe(b, kind) || a.id - b.id);
  const ortZustand = (o) => {
    const r = route.get(o.block_id);
    if (r?.status === 'fertig') return 'fertig';
    if (r?.kann_schon) return 'kann';
    if (mit.some((e) => e.block_id === o.block_id && e.gruppe === 'jetzt')) return 'jetzt';
    return 'offen';
  };
  const orte = (u.orte || []).map((o) => ({ ...o, zustand: ortZustand(o) }));
  const jetzt = mit.filter((e) => e.gruppe === 'jetzt');
  const naechste = jetzt.find((e) => !e.geschafft) || jetzt[0] || null;
  return { kind, mit, orte, jetzt, naechste, ortKlasse: (b) => ortKl.get(b) ?? null, ortKlassen: (b) => ortKlSet.get(b) || null, kann: mit.filter((e) => e.gruppe === 'kann'), frueher: mit.filter((e) => e.gruppe === 'frueher'), spaeter: mit.filter((e) => e.gruppe === 'spaeter') };
}

// W150 Gestaltung „Abflug“ (Vorschlag des Designers): nacht/tag = neues Design, alt = bisherige Welten. Je Kind auf dem Gerät gemerkt.
function lernGestaltung(kind) {
  let g = null; try { g = localStorage.getItem('lern.gestaltung.' + kind?.id) || localStorage.getItem('lern.gestaltung'); } catch { /* egal */ }
  if (!['nacht', 'tag', 'alt'].includes(g)) g = kind?.klasse && kind.klasse <= 6 ? 'tag' : 'nacht';
  return g;
}
const lernNeu = (kind) => lernGestaltung(kind) !== 'alt';
function lernThema(kind) {
  const g = lernGestaltung(kind);
  if (g !== 'alt') return `lr lr-abflug lr-abflug-${g}`;
  const welt = String(kind?.welt || 'Ozean').toLowerCase().replace('ü', 'ue');
  const stil = kind?.stil === 'studio' ? 'studio' : 'entdecker';
  return `lr lr-${['ozean', 'nacht', 'dschungel', 'wueste'].includes(welt) ? welt : 'ozean'} lr-${stil}`;
}

// ---------- Karte ----------
function lernProjektion(lon, lat) {
  const W = window.LERN_WELT; const l = lon * Math.PI / 180, f = lat * Math.PI / 180, f2 = f * f, f4 = f2 * f2;
  const x = l * (0.8707 - 0.131979 * f2 + f4 * (-0.013791 + f4 * (0.003971 * f2 - 0.001529 * f4)));
  const y = f * (1.007226 + f2 * (0.015085 + f4 * (-0.044475 + 0.028874 * f2 - 0.005916 * f4)));
  return [W.tx + W.k * x, W.ty - W.k * y];
}
// Karte als SVG: ganze Welt oder Ausschnitt um die gegebenen Orte. hervor = Erdteil-Kürzel, das farbig bleibt.
function lernKarte({ orte = [], fokus = null, hervor = null, route = false, beschriftung = [], label = 'Weltkarte', breite = 360, hoehe = 187 } = {}) {
  const W = window.LERN_WELT; const ns = 'http://www.w3.org/2000/svg';
  const svg = document.createElementNS(ns, 'svg');
  let vb = [0, 0, W.w, W.h];
  if (fokus && fokus.length) {
    const p = fokus.map((o) => lernProjektion(Number(o.lon), Number(o.lat)));
    let x0 = Math.min(...p.map((q) => q[0])), x1 = Math.max(...p.map((q) => q[0])), y0 = Math.min(...p.map((q) => q[1])), y1 = Math.max(...p.map((q) => q[1]));
    const asp = breite / hoehe; let w = Math.max((x1 - x0) * 1.6, 170), h = Math.max((y1 - y0) * 1.7, 70);
    if (w / h > asp) h = w / asp; else w = h * asp;
    vb = [(x0 + x1) / 2 - w / 2, (y0 + y1) / 2 - h / 2, w, h];
  }
  const z = vb[2] / breite; // Kartenmaß je Bildschirmpixel: Punkte, Linien und Schrift bleiben unabhängig vom Ausschnitt gleich groß
  svg.setAttribute('viewBox', vb.map((v) => v.toFixed(1)).join(' ')); svg.setAttribute('preserveAspectRatio', 'xMidYMid slice');
  svg.setAttribute('class', 'lr-karte'); svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', label);
  const mk = (tag, a) => { const e = document.createElementNS(ns, tag); for (const [k, v] of Object.entries(a)) e.setAttribute(k, v); return e; };
  svg.append(mk('rect', { x: vb[0] - 10, y: vb[1] - 10, width: vb[2] + 20, height: vb[3] + 20, class: 'lr-meer' }));
  for (const k of ['AN', 'SA', 'NA', 'AF', 'EU', 'AS', 'OC']) {
    svg.append(mk('path', { d: W.pfade[k], class: 'lr-land lr-land-' + k + (hervor && hervor !== k ? ' lr-land-blass' : ''), 'stroke-width': (1.2 * z).toFixed(2) }));
  }
  const pts = orte.filter((o) => o.lat != null).map((o) => ({ o, p: lernProjektion(Number(o.lon), Number(o.lat)) }));
  if (route && pts.length > 1) {
    svg.append(mk('path', { d: 'M' + pts.map((q) => q.p.map((v) => v.toFixed(1)).join(' ')).join(' L'), class: 'lr-route', 'stroke-width': (2.4 * z).toFixed(2), 'stroke-dasharray': `${(2 * z).toFixed(2)} ${(6 * z).toFixed(2)}` }));
  }
  for (const { o, p } of pts) {
    const r = (o.zustand === 'jetzt' ? 7 : 4.6) * z;
    svg.append(mk('circle', { cx: p[0].toFixed(1), cy: p[1].toFixed(1), r: r.toFixed(2), class: 'lr-punkt lr-punkt-' + (o.zustand || 'offen'), 'stroke-width': (1.6 * z).toFixed(2) }));
  }
  for (const b of beschriftung) {
    const p = lernProjektion(Number(b.lon), Number(b.lat));
    const t = mk('text', { x: (p[0] + (b.dx ?? 9) * z).toFixed(1), y: (p[1] + (b.dy ?? 4) * z).toFixed(1), class: 'lr-ortname' + (b.jetzt ? ' lr-ortname-jetzt' : ''), 'font-size': ((b.gross ? 15 : 12) * z).toFixed(1) });
    t.textContent = b.text; svg.append(t);
  }
  return svg;
}

// ---------- Rahmen der Kinderansicht ----------
function lernRahmen(kind, aktiv, ...inhalt) {
  if (lernNeu(kind)) {
    // W150 Abflug: keine Leiste – ein Menüknopf unten rechts öffnet ein Blatt.
    const g = lernGestaltung(kind);
    const blatt = el('dialog', { class: 'lr-blatt', 'aria-label': 'Menü' });
    const zu = () => { if (blatt.open) blatt.close(); };
    blatt.addEventListener('click', (ev) => { if (ev.target === blatt) zu(); });
    lernAnhaengen(blatt, el('div', { class: 'lr-blatt-liste' },
      ...[['reise', 'Abflugtafel'], ['weg', 'Mein Weg'], ['merkheft', 'Merkheft'], ['reisepass', 'Reisepass']].map(([v, t]) => // K2: Weltkarte ist jetzt in „Mein Weg“
        el('a', { href: `#/${v}/${kind.id}`, class: v === aktiv ? 'on' : '', ...(v === aktiv ? { 'aria-current': 'page' } : {}), onclick: zu }, t)),
      el('button', { type: 'button', onclick: () => { try { localStorage.setItem('lern.gestaltung.' + kind.id, g === 'nacht' ? 'tag' : 'nacht'); } catch { /* egal */ } zu(); render(); } }, g === 'nacht' ? 'Helle Ansicht' : 'Dunkle Ansicht'),
      el('button', { type: 'button', class: 'lr-blatt-zu', onclick: zu }, 'Schließen')));
    // M8: Der Menüknopf schwebt nicht mehr über dem Inhalt (verdeckte Text und Knöpfe) – er steht oben rechts und am Seitenende im Fluss der Seite.
    const knopf = (unten) => el('button', { type: 'button', class: 'lr-menue' + (unten ? ' lr-menue-unten' : ''), 'aria-label': 'Menü', 'aria-haspopup': 'dialog', onclick: () => blatt.showModal() },
      el('span', { 'aria-hidden': 'true' }, '≡'), unten ? el('span', {}, ' Menü') : null);
    return el('div', { class: lernThema(kind) + ' lr-mit-menue' }, el('div', { class: 'lr-inhalt' }, el('div', { class: 'lr-menue-zeile' }, knopf(false)), ...inhalt, el('div', { class: 'lr-menue-zeile unten' }, knopf(true))), blatt);
  }
  const nav = el('nav', { class: 'lr-nav', 'aria-label': 'Lernreise' },
    ...[['reise', 'Heute', LI.heute], ['weg', 'Mein Weg', LI.weg], ['merkheft', 'Merkheft', LI.heft], ['reisepass', 'Reisepass', LI.pass]].map(([v, t, i]) =>
      el('a', { href: `#/${v}/${kind.id}`, class: v === aktiv ? 'on' : '', ...(v === aktiv ? { 'aria-current': 'page' } : {}) }, lernIcon(i, 24), el('span', {}, t))));
  return el('div', { class: lernThema(kind) }, el('div', { class: 'lr-inhalt' }, ...inhalt), nav);
}
function lernKopf(gruss, titel) {
  return el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-gruss' }, gruss), el('h1', { class: 'lr-titel' }, titel));
}
function lernStats(konto) {
  const s = (icon, wert, text) => el('div', { class: 'lr-stat' }, lernIcon(icon, 22), el('div', {}, el('b', {}, String(wert)), el('span', {}, text)));
  // Antippen erklärt, was die Zahlen bedeuten.
  return el('details', { class: 'lr-stats-box' },
    el('summary', { 'aria-label': 'Stempel, Sterne und Lerntage – antippen für Erklärung' },
      el('div', { class: 'lr-stats' }, s(LI.stempel, konto?.stempel ?? 0, 'Stempel'), s(LI.stern, lernZahl(konto?.sterne ?? 0), 'Sterne'), s(LI.tag, konto?.lerntage ?? 0, 'Lerntage')),
      // F: Knobel-Sterne – nur, wenn die Datenbank sie zählt (Migration F)
      konto?.knobel_sterne ? el('p', { class: 'lr-knobel-sterne' }, `★ Knobel-Sterne: ${konto.knobel_sterne}`) : null),
    el('div', { class: 'lr-stats-erkl' },
      el('p', {}, el('b', {}, 'Sterne: '), '10 für jede Bordkarte, die du zum ersten Mal richtig löst, 20 für jede richtige Bordkarte im Test. Sterne kannst du später gegen Belohnungen eintauschen.'),
      el('p', {}, el('b', {}, 'Stempel: '), 'Jeder Ort hat einen oder mehrere Flüge. Hast du alle Flüge eines Ortes geschafft, bekommst du seinen Stempel in den Reisepass.'),
      el('p', {}, el('b', {}, 'Lerntage: '), 'Tage, an denen du geübt hast.'),
      konto?.knobel_sterne ? el('p', {}, el('b', {}, 'Knobel-Sterne: '), 'Knobel-Bordkarten sind freiwillig und richtig schwer. Löst du eine beim ersten Versuch, gibt es 30 Sterne und einen Knobel-Stern.') : null));
}
async function lernLadeKind(arg) {
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return null; }
  const [u, k] = await Promise.all([lernCall('schule_uebersicht'), lernCall('schule_konto', { lernender_id: kindId }).catch(() => null)]);
  const d = lernReiseDaten(u, kindId);
  if (!d) { route('lernen'); return null; }
  if (k?.look) Object.assign(d.kind, k.look);
  d.konto = k?.konto || null; d.belohnungen = k?.belohnungen || []; d.einloesungen = k?.einloesungen || [];
  d.knobelTag = k?.knobel_tag || null; // F: „Knobeln des Tages“ (Migration F; fehlt → nichts)
  d.u = u; // K3: für den Stand über Schularten
  return d;
}

// ---------- Stand über Schularten (K3, K4, E-2-Startseite) – Rechenregel „Stand“ ----------
// Für Schulart s und Stufe k zählen alle Flüge mit jahrgang[s] = k. Gelandet: alle Pflicht-Etappen fertig (fertig ≥ pflicht_anzahl),
// Ort geschafft oder „kann schon“. Läuft: mindestens eine Etappe fertig. Wackelt: Fehler offen oder Rückreise offen.
// Flüge: schule_uebersicht.themen (alle Mathe-Flüge, auch ohne Inhalt; Migration 20261117_w150_d_*), sonst die Flüge mit Inhalt (einheiten).
// Stufe: kind.stufen[s] (Migration D), sonst eigene Schulart = Klasse, andere = gleiche Klasse, IB MYP = Klasse − 4.
// ---------- Bau-Auftrag F: Stufen und Aufgabentypen ----------
// Typ einer Bordkarte („Gedanke“, Feld typ aus schule.aufgabe; Migration 20261118_w150_f_*). Die Stufe folgt aus dem Typ.
const LERN_TYP = {
  direkt: [1, 'wie im Beispiel'], erkennen: [1, 'erkennen'],
  mehrschritt: [2, 'mehrere Schritte'], einkleidung: [2, 'Sachaufgabe'], umkehr: [2, 'umgekehrt gefragt'], darstellung: [2, 'Darstellung wechseln'],
  rueckwaerts: [3, 'rückwärts'], verknuepfen: [3, 'mit früherem Stoff'], begruenden: [3, 'begründen'], fehler: [3, 'Fehler finden'],
  transfer: [3, 'Transfer'], parameter: [3, 'mit Variable'], pruefung: [3, 'wie in einer Prüfung'], knobel: [3, 'Knobeln'],
};
// Stufenzeichen im Kopf der Bordkarte: ● leicht · ●● mittel · ●●● schwer – ohne Druck (keine rote Farbe, kein „zu schwer“)
function lernStufeZeichen(a) {
  if (a.bonus) return el('span', { class: 'lr-stufe lr-stufe-bonus', role: 'img', 'aria-label': 'Knobel-Bordkarte, freiwillig' }, '★ KNOBEL');
  const n = Number(a.stufe); if (!(n >= 1 && n <= 3)) return el('span', {});
  const wort = ['', 'leicht', 'mittel', 'schwer'][n];
  return el('span', { class: 'lr-stufe lr-stufe-' + n, role: 'img', 'aria-label': 'Stufe: ' + wort, title: wort }, '●'.repeat(n));
}
// Knobel-Bordkarte (Pool „bonus“): freiwillig, ein Versuch, falsch kostet nichts und zeigt den Weg; richtig im ersten Versuch = 30 Sterne und ein Knobel-Stern.
// Zählt weder für „sitzt“ noch für Wiederholung oder Test (die Datenbank bucht sie nicht in den Karten-Stand).
function lernKnobelAngebot(e, oeffnen) {
  const offen = (e.bonus || []).filter((k) => !k.versuche);
  if (!offen.length) return null;
  return el('button', { type: 'button', class: 'lr-knopf-zweit lr-knobel-angebot', onclick: () => oeffnen(offen[0]) }, '★ Knobel-Bordkarte (freiwillig)');
}
function lernKnobel(ziel, a, ctx, { ortCode = '', zurueck, titel = 'KNOBEL-BORDKARTE' } = {}) {
  const auf = lernAufgabe(a, null, { tasten: false }); const cid = lernCid();
  const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
  const hilfeBox = el('div', { class: 'lr-hilfebox' });
  const tipp = a.tipp ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { tipp.remove(); lernAnhaengen(hilfeBox, el('p', { class: 'lr-tipp' }, el('b', {}, 'Tipp: '), lernText(a.tipp))); } }, 'Tipp') : null;
  const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
  const weiter = zurueck ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: zurueck }, 'Zurück') : null;
  pruefen.addEventListener('click', async () => {
    const w = auf.antwort();
    if (!w) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
    pruefen.disabled = true;
    try {
      const r = await lernCall('schule_uebung_pruefen', { lernender_id: ctx.kind, aufgabe_id: a.id, antwort: w, client_id: cid });
      if (!r.format_ok) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, r.hinweis || 'Bitte prüfe die Eingabe.')); pruefen.disabled = false; return; }
      a.versuche = (a.versuche || 0) + 1; if (r.richtig) a.geloest = true;
      auf.zeigeLoesung?.(r.loesung); pruefen.remove(); tipp?.remove();
      lernErsetze(meldung, r.richtig
        ? el('div', { class: 'lr-rueck lr-rueck-ok lr-knobel-ok' }, el('b', {}, '★ Geknackt!'), r.sterne ? el('p', { class: 'lr-sterne-neu' }, `+${r.sterne} Sterne · ein Knobel-Stern`) : null,
          r.knobel_sterne ? el('p', { class: 'lr-leise' }, `Knobel-Sterne: ${r.knobel_sterne}`) : null, r.loesungsweg ? el('p', {}, lernText(r.loesungsweg)) : null)
        : el('div', { class: 'lr-rueck lr-knobel-falsch' }, el('b', {}, 'Diesmal nicht – das war eine harte Nuss.'), el('p', {}, 'Richtig ist: ' + lernLoesungText({ ...a, loesung: r.loesung })),
          r.loesungsweg ? el('p', {}, el('b', {}, 'So geht’s: '), lernText(r.loesungsweg)) : null, el('p', { class: 'lr-leise' }, 'Knobeln kostet nichts – deine Punkte bleiben.')));
    } catch (err) { lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
  });
  lernErsetze(ziel, el('section', { class: 'lr-karte-box lr-aufgabe lr-bordkarte lr-knobel' },
      el('div', { class: 'lr-bord-kopf' }, el('span', {}, ortCode ? `${titel} · ${ortCode}` : titel), lernStufeZeichen({ ...a, bonus: true })),
      el('p', { class: 'lr-leise' }, 'Freiwillig: zählt nicht für „sitzt“ und nicht für den Test. Richtig beim ersten Versuch: 30 Sterne.'),
      auf.node, el('div', { class: 'lr-knopfzeile' }, pruefen, tipp)),
    hilfeBox, meldung, weiter);
  ziel.scrollIntoView?.({ block: 'start' });
}
// F: „Knobeln des Tages“ auf der Abflugtafel – höchstens einmal je Lerntag, aus einer sitzenden Etappe (schule_konto.knobel_tag)
function lernKnobelDesTages(d) {
  const a = d.knobelTag; if (!a) return null;
  const tag = new Date().toISOString().slice(0, 10), schl = `lern.knobel.${d.kind.id}`;
  try { if (localStorage.getItem(schl) === tag) return null; } catch { /* egal */ }
  const box = el('section', { class: 'lr-karte-box lr-knobel-tag' },
    el('p', { class: 'lr-ueber' }, '★ KNOBELN DES TAGES'),
    el('p', {}, 'Eine harte Nuss aus ', el('b', {}, a.etappe || 'einer Etappe, die schon sitzt'), a.stadt ? ` (${a.stadt})` : '', '. Freiwillig – falsch kostet nichts.'),
    el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => {
      try { localStorage.setItem(schl, tag); } catch { /* egal */ }
      lernKnobel(box, a, { kind: d.kind.id }, { titel: 'KNOBELN DES TAGES', zurueck: () => box.remove() });
    } }, 'Knobeln (freiwillig)'));
  return box;
}
// Auswahl der nächsten Bordkarte (stellt sie an den Anfang von warte). Regel „sitzt“ (16.11.): Die Stufe steigt mit den Punkten.
function lernWaehleBordkarte(warte, e, letzte, gesehenTyp = new Set()) {
  const ziel = e.ziel || 6, p = e.serie || 0, soll = p >= ziel ? 3 : Math.min(3, 1 + Math.floor(p * 3 / ziel));
  const vor = (j) => { if (j > 0) warte.unshift(...warte.splice(j, 1)); return j >= 0; };
  // Punkte voll, aber die schwere Aufgabe fehlt noch: dann kommt auf jeden Fall eine schwere
  // F: Abwechslung – nie zweimal hintereinander derselbe Typ (ohne Typ: derselbe Fragetext ohne Zahlen); Typen bevorzugen, die in dieser Etappe noch nicht dran waren
  const anders = (x) => !letzte || (x.typ && letzte.typ ? x.typ !== letzte.typ : lernBauplan(x) !== lernBauplan(letzte));
  const neuTyp = (x) => !x.typ || !gesehenTyp.has(x.typ);
  for (const ex of [(x) => anders(x) && neuTyp(x), anders]) {
    if (p >= ziel && e.schwerNoetig && !e.schwerOk && vor(warte.findIndex((x) => lernIstSchwer(x) && x !== letzte && !x.geloest && ex(x)))) return;
  }
  if (p >= ziel && e.schwerNoetig && !e.schwerOk && vor(warte.findIndex((x) => lernIstSchwer(x) && x !== letzte && !x.geloest))) return;
  if (p >= ziel && e.schwerNoetig && !e.schwerOk && vor(warte.findIndex((x) => lernIstSchwer(x) && x !== letzte))) return;
  const reihe = soll === 3 ? [3, 2, 1] : soll === 2 ? [2, 3, 1] : [1, 2, 3];
  for (const ok of [(x) => !x.geloest && !x.falschHeute, (x) => !x.geloest, (x) => x !== letzte])
    for (const st of reihe)
      for (const ex of [(x) => anders(x) && neuTyp(x), anders])
        if (vor(warte.findIndex((x) => (x.stufe || 2) === st && ok(x) && ex(x)))) return;
  for (const ok of [(x) => !x.geloest && !x.falschHeute, (x) => !x.geloest, (x) => x !== letzte])
    for (const st of reihe)
      if (vor(warte.findIndex((x) => (x.stufe || 2) === st && ok(x)))) return;
}
// Bauplan einer Bordkarte: Fragetext ohne Zahlen (gleiche Regel wie tools/inhalt_pruefen.py)
const lernBauplan = (a) => String(a?.frage?.text || '').replace(/[−-]?\d+(?:[ \u202f]\d{3})*(?:[,.]\d+)?/g, '#').replace(/\s+/g, ' ').trim();
// Zählt für „eine schwere Bordkarte im ersten Versuch“: Stufe 3 – und wenn ein Typ da ist, ein Stufe-3-Typ
const lernIstSchwer = (a) => a.stufe === 3 && (!a.typ || LERN_TYP[a.typ]?.[0] === 3) && a.typ !== 'knobel';

const LERN_SYS = [
  { sa: 'gym_by', kurz: 'GYM', name: 'Gymnasium', stufen: [5, 6, 7, 8, 9, 10], label: (n) => 'Klasse ' + n, kl: (n) => n, farbe: '#2F6FDE' },
  { sa: 'rs_by', kurz: 'RS', name: 'Realschule', stufen: [5, 6, 7, 8, 9, 10], label: (n) => 'Klasse ' + n, kl: (n) => n, farbe: '#D9482A' },
  { sa: 'ib_myp', kurz: 'IB', name: 'IB MYP', stufen: [1, 2, 3, 4, 5], label: (n) => 'MYP ' + n, kl: (n) => n + 5, farbe: '#0F8C68' }];
const LERN_KONT_REIHE = ['Zahlen', 'Geld und Verhältnisse', 'Algebra', 'Funktionen', 'Geometrie', 'Fläche und Raum', 'Daten und Zufall', 'Entdecker-Inseln'];
function lernStufe(k, sa) {
  if (!k?.klasse) return null;
  const s = Number(k.stufen?.[sa]); if (s >= 1) return s;
  const eigen = k.schulart || 'gym_by';
  const v = sa === eigen ? k.klasse : sa === 'ib_myp' ? k.klasse - 4 : k.klasse;
  return v >= 1 ? v : null;
}
function lernStandModell(u, k) {
  const einheiten = (u.einheiten || []).filter((e) => e.status !== 'entwurf' || k.ist_test);
  const proThema = new Map(); for (const e of einheiten) { const key = e.thema_id ?? 'e' + e.id; if (!proThema.has(key)) proThema.set(key, e); }
  const alle = Array.isArray(u.themen) ? u.themen : null; // ohne themen und ohne jahrgang: Klasse des Ortes in der eigenen Schulart (Balken nicht „–“)
  const themen = alle ? alle.map((t) => { const e = proThema.get(t.thema_id) || (t.einheit_id ? einheiten.find((x) => x.id === t.einheit_id) : null);
    return { thema_id: t.thema_id, titel: t.titel, jahrgang: t.jahrgang || {}, reihenfolge: t.reihenfolge || {}, block_id: t.block_id, stadt: t.stadt, kontinent: t.kontinent || 'Weitere', erdteil: t.erdteil, einheit: e || null }; })
    : [...proThema.values()].map((e) => ({ thema_id: e.thema_id, titel: e.titel, jahrgang: e.jahrgang || (e.ziel_klasse ? { [k.schulart || 'gym_by']: e.ziel_klasse } : {}), reihenfolge: {}, block_id: e.block_id, stadt: e.stadt, kontinent: e.kontinent || 'Weitere', erdteil: e.erdteil, einheit: e }));
  const stand = new Map((k.stand || []).map((s) => [s.einheit_id, s]));
  const normal = (k.route || []).filter((r) => r.art === 'normal' && r.status !== 'entfernt');
  const ortFertig = new Set(normal.filter((r) => r.status === 'fertig' || r.kann_schon).map((r) => r.block_id));
  const rueck = new Set((k.route || []).filter((r) => r.art === 'rueckreise' && !['fertig', 'entfernt'].includes(r.status)).map((r) => r.block_id));
  const aus = new Map(normal.map((r) => [r.block_id, r.ausgelassen || []]));
  const jetzt = lernReiseDaten(u, k.id)?.naechste;
  const zustand = (t) => {
    const s = t.einheit ? stand.get(t.einheit.id) : null; const n = Number(t.einheit?.pflicht_anzahl || 0); const f = Number(s?.fertig || 0);
    if ((n > 0 && f >= n) || (ortFertig.has(t.block_id) && !aus.get(t.block_id)?.includes(t.thema_id))) return 'ok';
    if (Number(s?.fehler || 0) > 0 || rueck.has(t.block_id)) return 'wackelt';
    if (jetzt && t.einheit && jetzt.id === t.einheit.id) return 'jetzt';
    if (f > 0) return 'laeuft';
    return 'offen';
  };
  for (const t of themen) { t.st = zustand(t); t.ausgelassen = !!aus.get(t.block_id)?.includes(t.thema_id); }
  const zahl = (sa, kl) => { const ts = kl ? themen.filter((t) => Number(t.jahrgang?.[sa]) === kl) : []; return { f: ts.filter((t) => t.st === 'ok').length, n: ts.length, ts }; };
  return { kind: k, themen, zahl, alleFluege: !!alle, stufe: (sa) => lernStufe(k, sa) };
}
// Rückwärts verträglich für die Startseite (E-2): drei Zeilen GYM · RS · IB
function lernStandSchularten(u, k) {
  if (!k?.klasse) return [];
  const m = lernStandModell(u, k); const eigen = k.schulart || 'gym_by';
  return LERN_SYS.map((y) => { const kl = m.stufe(y.sa); const c = m.zahl(y.sa, kl);
    return { sa: y.sa, kurz: y.kurz, name: y.name, klasse: kl || '–', n: c.n, gelandet: c.f, eigen: y.sa === eigen }; });
}
// M5: Zahl der gelandeten Flüge eines Ortes (für den Stempel)
const ortFluegeGelandet = (d, blockId) => d.mit.filter((e) => e.block_id === blockId && lernGelandet(e)).length;
const lernPz = (a, b) => (b ? Math.round(100 * a / b) : 0);
const lernSysVoll = (y, n) => (y.sa === 'ib_myp' ? 'IB MYP ' + n : `${y.name} ${y.label(n)}`);
const lernSysStufe = (y, n) => `${y.kurz} ${y.sa === 'ib_myp' ? 'MYP ' : ''}${n}`;
// K3: drei Mini-Linien (Abflugtafel und Mein Weg · Stand). href(y, stufe) → Ziel beim Antippen.
function lernMiniLinien(m, href) {
  return el('div', { class: 'lr-mini3', role: 'list', 'aria-label': 'Mein Stand in drei Schularten' }, ...LERN_SYS.map((y) => {
    const kl = m.stufe(y.sa); const c = m.zahl(y.sa, kl);
    return el('a', { class: 'lr-mini', role: 'listitem', href: href(y, kl), style: `--f:${y.farbe}`, 'aria-label': `${kl ? lernSysVoll(y, kl) : y.name}: ${c.f} von ${c.n} Flügen gelandet` },
      el('b', {}, kl ? lernSysStufe(y, kl) : y.kurz + ' –'),
      el('span', { class: 'lr-mini-balken' }, el('i', { style: `width:${lernPz(c.f, c.n)}%` })),
      el('small', {}, c.n ? `${c.f}/${c.n} gelandet` : 'keine Flüge'));
  }));
}
// K3: Linienplan – drei Linien, Haltestellen = Klassen, nach Alter ausgerichtet (MYP 1 ≈ Klasse 6), Ring je Haltestelle, „DU“ an der eigenen Stufe.
function lernLinienplan(m, href, wahl = null) {
  const ns = 'http://www.w3.org/2000/svg'; const X = (kl) => 40 + (kl - 5) * 54; const Y = { gym_by: 58, rs_by: 142, ib_myp: 226 };
  const svg = document.createElementNS(ns, 'svg'); svg.setAttribute('viewBox', '0 0 360 270'); svg.setAttribute('class', 'lr-linienplan'); svg.setAttribute('role', 'group'); svg.setAttribute('aria-label', 'Linienplan der Schularten');
  const mk = (tag, a, text, eltern = svg) => { const e = document.createElementNS(ns, tag); for (const [k2, v] of Object.entries(a)) e.setAttribute(k2, v); if (text !== undefined) e.textContent = text; eltern.append(e); return e; };
  for (const kl of [5, 6, 7, 8, 9, 10]) mk('text', { x: X(kl), y: 16, 'text-anchor': 'middle', class: 'lr-lp-kl' }, String(kl));
  mk('text', { x: 4, y: 16, class: 'lr-lp-kl' }, 'Kl.');
  for (const y of LERN_SYS) {
    const xs = y.stufen.map((n) => X(y.kl(n))).filter((x) => x <= X(10) + 1);
    // Name auf der Seite, wo das „DU“-Schild nicht steht (sonst überdecken sie sich)
    const ichX = m.stufe(y.sa) ? X(y.kl(m.stufe(y.sa))) : 0; const rechts = ichX < 220;
    mk('text', { x: rechts ? 356 : 4, y: Y[y.sa] - 28, 'text-anchor': rechts ? 'end' : 'start', class: 'lr-lp-name', fill: y.farbe }, y.name.toUpperCase());
    mk('line', { x1: xs[0], y1: Y[y.sa], x2: xs[xs.length - 1], y2: Y[y.sa], stroke: y.farbe, 'stroke-width': 8, 'stroke-linecap': 'round' });
    for (const n of y.stufen) {
      const cx = X(y.kl(n)); if (cx > X(10) + 1) continue;
      const cy = Y[y.sa]; const c = m.zahl(y.sa, n); const p = lernPz(c.f, c.n); const ich = m.stufe(y.sa) === n; const r = ich ? 19 : 15; const u = 2 * Math.PI * r;
      const a = mk('a', { href: href(y, n), class: 'lr-lp-halt' + (wahl && wahl[0] === y.sa && wahl[1] === n ? ' gewaehlt' : ''), 'aria-label': `${lernSysVoll(y, n)}: ${c.f} von ${c.n} Flügen gelandet${ich ? ' – deine Stufe' : ''}` });
      mk('circle', { cx, cy, r: r + 6, class: 'lr-lp-flaeche' }, undefined, a);
      mk('circle', { cx, cy, r, fill: 'var(--lr-flaeche, #fff)', stroke: 'var(--lr-linie, #E3DCCB)', 'stroke-width': ich ? 6 : 5 }, undefined, a);
      if (p > 0) mk('circle', { cx, cy, r, fill: 'none', stroke: y.farbe, 'stroke-width': ich ? 6 : 5, 'stroke-dasharray': `${(u * p / 100).toFixed(1)} ${u.toFixed(1)}`, transform: `rotate(-90 ${cx} ${cy})`, 'stroke-linecap': 'round' }, undefined, a);
      if (p === 100) { mk('circle', { cx, cy, r: r - 6, fill: y.farbe }, undefined, a); mk('text', { x: cx, y: cy + 4, 'text-anchor': 'middle', class: 'lr-lp-wert hell' }, '✓', a); }
      else mk('text', { x: cx, y: cy + 4, 'text-anchor': 'middle', class: 'lr-lp-wert' + (ich ? ' gross' : '') }, c.n ? p + '%' : '–', a);
      if (y.sa === 'ib_myp') mk('text', { x: cx, y: cy + 34, 'text-anchor': 'middle', class: 'lr-lp-kl' }, 'MYP ' + n, a);
      if (ich) { const g = mk('g', { transform: `translate(${cx},${cy - 31})` }, undefined, a); mk('rect', { x: -17, y: -11, width: 34, height: 18, rx: 9, class: 'lr-lp-du' }, undefined, g); mk('text', { y: 2, 'text-anchor': 'middle', class: 'lr-lp-du-text' }, 'DU', g); }
    }
  }
  return svg;
}
const lernSymbol = (s) => (s === 'ok' ? '✓' : s === 'jetzt' ? '▶' : s === 'wackelt' ? '!' : '');
const lernZaehltAuch = (t, sa) => LERN_SYS.filter((y) => y.sa !== sa && t.jahrgang?.[y.sa]).map((y) => lernSysStufe(y, t.jahrgang[y.sa])).join(' · ');
const lernKontReihe = (a, b) => (LERN_KONT_REIHE.indexOf(a) + 1 || 99) - (LERN_KONT_REIHE.indexOf(b) + 1 || 99);

// ---------- Eltern: Übersicht ----------
async function viewLernen() {
  setChrome('Lernen Schule', { tab: 'lernen' });
  const live = viewGuard();
  loading();
  const [u, eltern, rm] = await Promise.all([lernCall('schule_uebersicht'), lernCall('schule_eltern').catch(() => null),
    lernCall('schule_rueckmeldungen').catch(() => null)]);
  if (!live()) return;
  const seite = typeof LERN_SEITE !== 'undefined';
  const konten = new Map((eltern?.kinder || []).map((k) => [k.id, k.konto]));
  const url = new URL('mathe/', location.href).href;
  const status = el('span', { class: 'muted small', role: 'status' });
  const kopie = el('button', { type: 'button', class: 'secondary' }, 'Link kopieren');
  kopie.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(url); status.textContent = 'Link kopiert.'; }
    catch { status.textContent = 'Kopieren nicht möglich. Link bitte markieren und kopieren.'; }
  });
  const kinder = (u.lernende || []).map((k) => {
    const d = lernReiseDaten(u, k.id); const n = d?.naechste; const ko = konten.get(k.id);
    return el('a', { class: 'card lern-kindkarte', href: `#/reise/${k.id}` },
      el('div', { class: 'lern-einheit-kopf' }, el('b', {}, k.name), k.ist_test ? el('span', { class: 'pill wartet' }, 'zum Ausprobieren') : null),
      el('p', { class: 'small muted' }, n ? `Jetzt: ${n.stadt || n.ort_titel} · ${n.titel} (${n.fertig}/${n.n})` : 'Gerade nichts offen'),
      ko ? el('p', { class: 'small muted' }, `${ko.stempel} Stempel · ${lernZahl(ko.sterne)} Sterne · ${ko.lerntage} Lerntage`) : null,
      el('span', { class: 'lern-kindkarte-los' }, 'Lernreise öffnen ›'));
  });
  // E-2: Startseite für Eltern/Lehrer – je Kind ein Bereich (Klasse, Stand in drei Schularten, Jetzt, Knöpfe); darunter „Für alle Kinder“.
  const kindBereich = (k) => {
    const d = lernReiseDaten(u, k.id); const n = d?.naechste; const ko = konten.get(k.id);
    const linien = lernStandSchularten(u, k);
    return el('section', { class: 'card lern-kindbereich', 'aria-label': k.name },
      el('div', { class: 'lern-kindbereich-kopf' }, el('h3', {}, k.name),
        el('span', { class: 'small muted' }, k.klasse ? `${LERN_SCHULART[k.schulart || 'gym_by'] || 'Gymnasium'} · Klasse ${k.klasse}` : 'Klasse nicht gesetzt')),
      linien.length ? el('div', { class: 'lern-mini-linien', role: 'list', 'aria-label': 'Stand in drei Schularten' }, ...linien.map((l) => el('a', { class: 'lern-mini-linie' + (l.eigen ? ' eigen' : ''), role: 'listitem', href: `#/lernstand/${k.id}-${l.sa}` },
        el('span', { class: 'lern-mini-name' }, `${l.kurz} ${l.klasse}`),
        el('span', { class: 'lern-mini-balken', role: 'img', 'aria-label': `${l.name} Klasse ${l.klasse}: ${l.gelandet} von ${l.n} Flügen gelandet` }, el('i', { style: `width:${l.n ? Math.round(100 * l.gelandet / l.n) : 0}%` })),
        el('span', { class: 'lern-mini-zahl' }, l.n ? `${l.gelandet}/${l.n}` : '–')))) : null,
      el('p', { class: 'small' }, n ? `Jetzt: ${n.stadt || n.ort_titel} · ${n.titel} (${n.fertig}/${n.n})` : 'Gerade nichts offen'),
      ko ? el('p', { class: 'small muted' }, `${ko.stempel} Stempel · ${lernZahl(ko.sterne)} Sterne · ${ko.lerntage} Lerntage`) : null,
      el('div', { class: 'lern-kindbereich-knoepfe' },
        el('a', { class: 'btn secondary', href: `#/lernstand/${k.id}`, 'aria-label': `Lernstand ${k.name}` }, 'Lernstand'),
        el('a', { class: 'btn secondary', href: `#/wackelt/${k.id}`, 'aria-label': `Was wackelt? ${k.name}` }, 'Was wackelt?'),
        el('a', { class: 'btn secondary', href: `#/plan/${k.id}`, 'aria-label': `Flugplan ${k.name}` }, 'Flugplan'),
        el('a', { class: 'btn secondary', href: `#/reise/${k.id}`, 'aria-label': `Lernreise ${k.name} ansehen` }, 'Lernreise ansehen')));
  };
  const offen = (rm?.rueckmeldungen || []).filter((r) => ['offen', 'in_arbeit'].includes(r.status)).length;
  const testkinder = (u.lernende || []).filter((k) => k.ist_test);
  const steuern = u.leitung ? [
    el('section', { class: 'start-intro lern-neu' }, el('p', { class: 'eyebrow' }, 'FÜR ALLE KINDER')),
    el('div', { class: 'lern-kinderliste' },
      el('a', { class: 'card lern-kindkarte lp-hauptkarte', href: '#/lehrplan' }, el('b', {}, 'Lehrplan-Übersicht'),
        el('p', { class: 'small muted' }, 'Alle Flüge je Schulart und Klasse: was fertig ist, was in Prüfung ist, was noch fehlt – mit Inhalten zum Ansehen.'),
        el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ›')),
      el('a', { class: 'card lern-kindkarte', href: '#/schulstand' }, el('b', {}, 'Alle Kinder im Vergleich'),
        el('p', { class: 'small muted' }, 'Alle Kinder × Gymnasium, Realschule, IB MYP; den Lernstand eines Kindes öffnet „Lernstand“ an seiner Karte'), el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ›')),
      el('a', { class: 'card lern-kindkarte', href: '#/lernauftraege' }, el('b', {}, 'Meine Aufträge'),
        el('p', { class: 'small muted' }, offen ? `${offen} offen` : 'Was ihr ändern lassen wollt – mit Status und Antwort'), el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ›')),
      el('a', { class: 'card lern-kindkarte', href: '#/info' }, el('b', {}, 'So funktioniert’s'),
        el('p', { class: 'small muted' }, 'Erste Schritte und Antworten auf die häufigsten Fragen'), el('span', { class: 'lern-kindkarte-los' }, 'Lesen ›')),
      ...testkinder.map((k) => el('a', { class: 'card lern-kindkarte', href: `#/reise/${k.id}` }, el('b', {}, k.name),
        el('p', { class: 'small muted' }, 'Sieht alle Flüge, auch die in Prüfung – zum Ausprobieren und für „✎ Ändern lassen“ an Bordkarten.'), el('span', { class: 'lern-kindkarte-los' }, 'Lernreise öffnen ›'))),
      eltern ? el('a', { class: 'card lern-kindkarte', href: '#/zugaenge' }, el('b', {}, 'Zugänge'),
        el('p', { class: 'small muted' }, 'Codes für Lehrer, Eltern und Kinder – nur für den Bereich Lernen'), el('span', { class: 'lern-kindkarte-los' }, 'Verwalten ›')) : null,
      !seite ? el('a', { class: 'card lern-kindkarte', href: 'lernen/', target: '_blank', rel: 'noopener' }, el('b', {}, 'Eigene Lernen-Seite'),
        el('p', { class: 'small muted' }, 'Für Lehrer und Kinder: Anmeldung mit Lern-Code, ohne Zugriff auf den Rest der App.'), el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ↗')) : null)] : [];
  // Reihenfolge nach Dringlichkeit: erst, was auf eine Antwort wartet, dann die Kinder, dann Verwalten.
  const offeneWuensche = (eltern?.einloesungen || []).filter((x) => x.status === 'beantragt');
  const meldung = el('p', { class: 'small muted', role: 'status' });
  const entscheide = async (id, status) => { try { await lernCall('schule_einloesung_entscheiden', { id, status }); render(); } catch (err) { meldung.textContent = err.message; } };
  const neueAntworten = (rm?.rueckmeldungen || []).filter((r) => r.antwort && r.status !== 'offen').slice(0, 3);
  const wartet = offeneWuensche.length ? el('section', { class: 'card lern-wartet' }, el('p', { class: 'eyebrow' }, 'WARTET AUF DICH'),
    ...offeneWuensche.map((x) => el('div', { class: 'lern-wunsch' }, el('span', {}, el('b', {}, x.kind), ` möchte „${x.titel}“ einlösen (${lernZahl(x.sterne)} Sterne)`),
      el('div', { class: 'row' }, el('button', { type: 'button', class: 'primary', onclick: () => entscheide(x.id, 'bestaetigt') }, 'Bestätigen'),
        el('button', { type: 'button', class: 'secondary', onclick: () => entscheide(x.id, 'abgelehnt') }, 'Ablehnen')))), meldung) : null;
  lernErsetze(main, ...[
    u.leitung ? lernInfoLink() : null,
    wartet,
    el('section', { class: 'start-intro lern-neu' }, el('p', { class: 'eyebrow' }, 'LERNREISE'), el('h2', {}, u.leitung ? 'Die Kinder' : 'Wer lernt heute?')),
    u.leitung ? el('div', { class: 'lern-kindbereiche' }, ...((u.lernende || []).filter((k) => !k.ist_test).map(kindBereich)), ...((u.lernende || []).some((k) => !k.ist_test) ? [] : [el('p', { class: 'card muted' }, 'Kein Kind freigeschaltet.')]))
      : el('div', { class: 'lern-kinderliste' }, ...(kinder.length ? kinder : [el('p', { class: 'card muted' }, 'Kein Kind freigeschaltet.')])),
    neueAntworten.length ? el('section', { class: 'card' }, el('h3', {}, 'Neue Antworten auf eure Aufträge'),
      ...neueAntworten.map((r) => el('p', { class: 'small' }, el('b', {}, (r.flug || r.ort || 'Allgemein') + ': '), r.antwort)), el('a', { class: 'small', href: '#/lernauftraege' }, 'Meine Aufträge ›')) : null,
    ...steuern,
    eltern ? lernElternBereich(eltern, { ohneWuensche: true }) : null,
    seite ? null : el('details', { class: 'card lern-weitere' }, el('summary', {}, 'Weitere Lernhilfen'),
      el('p', {}, 'Mathe-Lernblatt: Erklärungen, Übungen in drei Stufen und typische Fehler. Die Seite öffnet ohne Anmeldung.'),
      el('div', { class: 'row' }, el('a', { class: 'btn secondary', href: 'mathe/', target: '_blank', rel: 'noopener' }, 'Mathe-Lernblatt öffnen ↗'), kopie, status),
      el('p', { class: 'muted small learn-url' }, url))].filter(Boolean));
}

function lernElternBereich(e, { ohneWuensche = false } = {}) {
  const box = el('section', { class: 'lern-eltern' });
  const offen = (e.einloesungen || []).filter((x) => x.status === 'beantragt');
  const meldung = el('p', { class: 'small muted', role: 'status' });
  const entscheide = async (id, status) => {
    try { await lernCall('schule_einloesung_entscheiden', { id, status }); render(); } catch (err) { meldung.textContent = err.message; }
  };
  lernAnhaengen(box, el('h2', {}, 'Belohnungen'),
    el('p', { class: 'small muted' }, 'Die Kinder sammeln Sterne (Üben, Tests) und Stempel (geschaffte Orte) und lösen sie hier ein. Du bestätigst. Abgelehnt gibt die Sterne zurück.'));
  if (offen.length && !ohneWuensche) lernAnhaengen(box, el('div', { class: 'card' }, el('h3', {}, `Offene Wünsche (${offen.length})`),
    ...offen.map((x) => el('div', { class: 'lern-wunsch' }, el('span', {}, el('b', {}, x.kind), ` möchte „${x.titel}“ (${lernZahl(x.sterne)} Sterne)`),
      el('div', { class: 'row' }, el('button', { type: 'button', class: 'primary', onclick: () => entscheide(x.id, 'bestaetigt') }, 'Bestätigen'),
        el('button', { type: 'button', class: 'secondary', onclick: () => entscheide(x.id, 'abgelehnt') }, 'Ablehnen'))))));
  const liste = (e.belohnungen || []);
  lernAnhaengen(box, el('div', { class: 'card' }, el('h3', {}, 'Katalog'),
    liste.length ? el('ul', { class: 'lern-katalog' }, ...liste.map((b) => el('li', { class: b.aktiv ? '' : 'muted' },
      el('span', {}, el('b', {}, b.titel), ` · ${b.kosten_sterne ? lernZahl(b.kosten_sterne) + ' Sterne' : ''}${b.kosten_sterne && b.kosten_stempel ? ' + ' : ''}${b.kosten_stempel ? b.kosten_stempel + ' Stempel' : ''}${b.kosten_sterne || b.kosten_stempel ? '' : 'gratis'}`),
      el('button', { type: 'button', class: 'secondary', onclick: async () => { try { await lernCall('schule_belohnung_setzen', { id: b.id, aktiv: !b.aktiv }); render(); } catch (err) { meldung.textContent = err.message; } } }, b.aktiv ? 'Ausblenden' : 'Wieder anbieten'))))
      : el('p', { class: 'small muted' }, 'Noch keine Belohnungen angelegt.'),
    lernBelohnungFormular(meldung), meldung));
  return box;
}

function lernBelohnungFormular(meldung) {
  const titel = el('input', { type: 'text', id: 'bl-titel', placeholder: 'z. B. Eis, Kinoabend, Ausflug', autocomplete: 'off' });
  const sterne = el('input', { type: 'number', id: 'bl-sterne', min: '0', step: '10', value: '300', inputmode: 'numeric' });
  const stempel = el('input', { type: 'number', id: 'bl-stempel', min: '0', step: '1', value: '0', inputmode: 'numeric' });
  const f = el('form', { class: 'lern-bl-form' },
    el('label', { for: 'bl-titel' }, 'Belohnung'), titel,
    el('div', { class: 'row' }, el('label', { for: 'bl-sterne' }, 'Sterne', sterne), el('label', { for: 'bl-stempel' }, 'Stempel', stempel)),
    el('button', { type: 'submit', class: 'primary' }, 'Hinzufügen'));
  f.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!titel.value.trim()) { meldung.textContent = 'Bitte einen Namen eingeben.'; return; }
    try { await lernCall('schule_belohnung_setzen', { titel: titel.value.trim(), kosten_sterne: Number(sterne.value) || 0, kosten_stempel: Number(stempel.value) || 0 }); render(); }
    catch (err) { meldung.textContent = err.message; }
  });
  return f;
}

// ---------- Kind: Heute dran ----------
async function viewReise(arg) {
  setChrome('Lernreise', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const [merk, wdh] = await Promise.all([lernMerkDaten(d).catch(() => []), lernCall('schule_wiederholung', { lernender_id: d.kind.id, anzahl: LERN_WDH_RUNDE }).catch(() => null)]);
  if (!live()) return;
  const { kind, naechste: n } = d;
  $('#title').textContent = 'Lernreise ' + kind.name;
  const ortStand = (blockId) => (d.konto?.orte || []).find((o) => o.block_id === blockId);
  const et = n ? lernEtappenZahl(merk.find((m) => m.einheit_id === n.id)) : { n: 0, f: 0 };
  const wdhGemacht = lernWdhHeute(kind.id); // Runde heute schon gemacht → Start führt ins Thema, der Rest wird nur angeboten
  const nWdh = wdhGemacht ? 0 : wdh?.aufgaben?.length || 0; const wdhRest = wdhGemacht ? Number(wdh?.faellig || 0) : 0;
  // K1/U1: Den Stempel gibt es erst, wenn alle Flüge des Ortes geschafft sind – das Band zählt deshalb alle Etappen des Ortes.
  const ortFluege = n ? d.mit.filter((e) => e.block_id === n.block_id) : [];
  const ort = ortFluege.reduce((z, e) => { const m = merk.find((x) => x.einheit_id === e.id); const q = m ? lernEtappenZahl(m) : { n: e.n, f: e.fertig }; return { n: z.n + q.n, f: z.f + Math.min(q.f, q.n), fluege: z.fluege + 1 }; }, { n: 0, f: 0, fluege: 0 });
  if (lernNeu(kind) && n) { lernErsetze(main, lernRahmen(kind, 'reise', ...lernAbflugtafel(d, { n, et, nWdh, wdhRest, wdhFertig: wdhGemacht, ort }))); return; }
  const teile = [el('header', { class: 'lr-kopf lr-kopf-kurz' }, el('p', { class: 'lr-gruss' }, `Hallo ${kind.name}!`))];
  if (n) {
    const kont = d.orte.filter((o) => o.kontinent === (d.orte.find((x) => x.block_id === n.block_id)?.kontinent));
    const ortN = d.orte.find((o) => o.block_id === n.block_id) || {};
    // Ein einziger Startknopf: erst die fälligen Wiederholungen, dann direkt ins Üben des Themas.
    const testDran = !n.laeuft && et.n > 0 && et.f >= et.n; // alle Etappen sitzen → als Nächstes der Test, nicht wieder üben
    const ziel = n.laeuft || testDran ? `#/lerneinheit/${kind.id}-${n.id}-test` : nWdh ? `#/wiederholen/${kind.id}` : `#/lerneinheit/${kind.id}-${n.id}-ueben`;
    teile.push(el('section', { class: 'lr-karte-box lr-haupt' },
      el('p', { class: 'lr-ueber' }, `JETZT DRAN · ${(n.stadt || '').toUpperCase()}`),
      el('h1', { class: 'lr-titel lr-titel-thema' }, n.titel),
      el('a', { class: 'lr-knopf lr-knopf-start', href: ziel }, n.laeuft ? 'Test weitermachen' : testDran ? 'Zum Test' : et.f || nWdh ? 'Weiter geht’s' : 'Los geht’s'),
      nWdh && !n.laeuft ? el('p', { class: 'lr-leise lr-start-info' }, `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'}, dann ${n.stadt}.`) : null,
      et.n ? el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${et.f} von ${et.n} Etappen sitzen` }, el('span', { style: `width:${Math.round(100 * et.f / et.n)}%` })), el('b', {}, `${et.f} von ${et.n} Etappen sitzen`)) : null,
      el('a', { class: 'lr-textlink', href: `#/lerneinheit/${kind.id}-${n.id}` }, 'Erst die Erklärungen ansehen'),
      el('div', { class: 'lr-kartenbild lr-kartenbild-klein' }, lernKarte({ orte: kont, fokus: kont.slice(0, Math.max(3, kont.indexOf(ortN) + 2)), hervor: LERN_ERDTEIL[ortN.kontinent], route: true,
        beschriftung: [{ ...ortN, text: `Du bist in ${n.stadt}`, jetzt: true, gross: true }], label: `Karte: ${n.stadt}, ${n.land}`, breite: 340, hoehe: 110 })),
      (() => { const o = ortStand(n.block_id); return o && o.themen > 1 ? el('p', { class: 'lr-leise lr-ortstand' },
        `${n.stadt} hat ${o.themen} Flüge, ${o.erledigt} davon geschafft. Den Stempel gibt es, wenn alle geschafft sind.`) : null; })()));
  } else teile.push(el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Gerade ist nichts offen'), el('p', { class: 'lr-leise' }, 'Neue Orte kommen bald. '), nWdh ? el('a', { class: 'lr-knopf', href: `#/wiederholen/${kind.id}` }, `${nWdh} ${nWdh === 1 ? 'Bordkarte' : 'Bordkarten'} wiederholen`) : el('a', { class: 'lr-knopf-zweit', href: `#/reisepass/${kind.id}` }, 'Zum Reisepass')));
  teile.push(lernStats(d.konto), el('a', { class: 'lr-textlink', href: `#/reisepass/${kind.id}` }, 'Reisepass und Belohnungen ansehen'));
  const jg = d.konto?.jahrgang;
  if (jg?.themen) teile.push(el('section', { class: 'lr-karte-box lr-jgstand' },
    el('p', { class: 'lr-ueber' }, `MEIN STAND · ${(LERN_SCHULART[jg.schulart] || '').toUpperCase()} KLASSE ${jg.klasse}`),
    el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${jg.geschafft} von ${jg.themen} Flügen geschafft` }, el('span', { style: `width:${Math.round(100 * jg.geschafft / jg.themen)}%` })),
      el('b', {}, `${jg.geschafft} von ${jg.themen} Flügen`)),
    el('p', { class: 'lr-leise' }, `${jg.mit_inhalt} davon kannst du schon lernen, die anderen kommen nach und nach dazu.`)));
  const weitere = d.jetzt.filter((e) => e !== n);
  if (weitere.length) teile.push(el('h2', { class: 'lr-zwischen' }, 'Auch offen'), ...weitere.map((e) => lernOrtZeile(kind, e)));
  if (d.kann.length) teile.push(el('details', { class: 'lr-mehr' }, el('summary', {}, `Geschafft oder kann schon – zum Wiederholen (${d.kann.length})`), ...d.kann.map((e) => lernOrtZeile(kind, e))));
  if (d.frueher.length) teile.push(el('details', { class: 'lr-mehr' }, el('summary', {}, `Aus früheren Klassen – zum Auffrischen (${d.frueher.length})`), ...d.frueher.map((e) => lernOrtZeile(kind, e))));
  if (d.spaeter.length) teile.push(el('details', { class: 'lr-mehr' }, el('summary', {}, `Später – für höhere Klassen (${d.spaeter.length})`), ...d.spaeter.map((e) => lernOrtZeile(kind, e))));
  lernErsetze(main, lernRahmen(kind, 'reise', ...teile));
}

// W150 Abflug: Startseite als Abflugtafel. Oberste Zeile = jetzt dran, ein gelber Knopf im Daumenbereich.
// V9: Vor dem Thema höchstens eine Runde Wiederholungen am Tag (bis zu 6 Karten). Ist die Runde heute gemacht, führt der Startknopf ins Thema.
const LERN_WDH_RUNDE = 6;
function lernWdhHeute(kindId, setzen) {
  const heute = new Date().toLocaleDateString('sv-SE');
  try { if (setzen) localStorage.setItem('lern.wdhrunde.' + kindId, heute); return localStorage.getItem('lern.wdhrunde.' + kindId) === heute; } catch { return false; }
}
// V12: „Was kommt wann wieder?“ in einfachen Worten (Kindansicht)
function lernWdhErklaert() {
  return el('details', { class: 'lr-mehr lr-wdh-erklaert' }, el('summary', {}, 'Was kommt wann wieder?'),
    el('p', {}, 'Sitzt eine Etappe, kommt sie später zum Wiederholen zurück – jedes Mal mit einer Bordkarte.'),
    el('p', {}, 'Die Abstände werden größer: nach 1, 3, 7, 14 und 30 Lerntagen. Ein Lerntag ist ein Tag, an dem du übst. Machst du Pause, wartet die Etappe.'),
    el('p', {}, 'Stimmt die Bordkarte nicht, kommt die Etappe am nächsten Lerntag wieder. Erst beim zweiten Fehler übst du sie noch einmal von vorn.'),
    el('p', {}, 'Vor einem Flug kommen höchstens ' + LERN_WDH_RUNDE + ' Wiederholungen. Nach dem Test zu einem Flug folgt später ein kurzer Nachtest.'));
}
function lernAbflugtafel(d, { n, et, nWdh, wdhRest = 0, wdhFertig = false, ort = null }) {
  const { kind } = d; const sa = kind.schulart || 'gym_by';
  const kl = (e) => e.jahrgang?.[sa] ?? e.ziel_klasse;
  const code = (e) => String(e.stadt || e.ort_titel || '').toUpperCase();
  const zeile = (e, status, klasse = '') => el('a', { class: 'lr-flug' + klasse, href: `#/lerneinheit/${kind.id}-${e.id}` },
    el('span', { class: 'lr-flug-ort' }, el('b', {}, code(e)), el('small', {}, e.titel)),
    el('span', { class: 'lr-flug-status' }, el('b', {}, status), kl(e) ? el('small', {}, `Klasse ${kl(e)}`) : null));
  const testDran = !n.laeuft && et.n > 0 && et.f >= et.n; // alle Etappen sitzen → als Nächstes der Test, nicht wieder üben
  const ziel = n.laeuft || testDran ? `#/lerneinheit/${kind.id}-${n.id}-test` : nWdh ? `#/wiederholen/${kind.id}` : `#/lerneinheit/${kind.id}-${n.id}-ueben`;
  const weitere = d.jetzt.filter((e) => e !== n);
  const maxZ = kind.klasse && kind.klasse <= 6 ? 3 : 6;
  const offen = Math.max(0, et.n - et.f);
  const gruppe = (titel, liste) => liste.length ? el('details', { class: 'lr-mehr' }, el('summary', {}, `${titel} (${liste.length})`), ...liste.map((e) => lernOrtZeile(kind, e))) : null;
  const jg = d.konto?.jahrgang;
  // M5: Ziel ist das nächste Zwischenziel – die Etappen des aktuellen Flugs bis „gelandet“. Der Stempel des Ortes (alle Flüge) steht klein darunter und im Reisepass.
  const bo = et.n ? et : { n: n.n || 0, f: Math.min(n.fertig || 0, n.n || 0) }; const rest = Math.max(0, bo.n - bo.f);
  const bandText = rest ? `Noch ${rest} ${rest === 1 ? 'Etappe' : 'Etappen'} bis ›${n.titel}‹ gelandet` : `Alle Etappen sitzen – jetzt der Test für ›${n.titel}‹`;
  const ortGel = ortFluegeGelandet(d, n.block_id);
  const stempelText = ort && ort.fluege > 1 ? `Stempel ${n.stadt}: ${ortGel} von ${ort.fluege} Flügen gelandet` : null;
  const band = !bo.n ? null : el('div', { class: 'lr-band-box' }, bo.n <= 14
    ? el('div', { class: 'lr-band', role: 'img', 'aria-label': `${bo.f} von ${bo.n} Etappen bis ${n.titel} gelandet` },
      ...Array.from({ length: bo.n }, (_, i) => el('i', { class: i < bo.f ? 'voll' : i === bo.f ? 'dran' : '' })), el('span', {}, '✈'), el('small', {}, bandText))
    : el('div', { class: 'lr-band lr-band-lang', role: 'img', 'aria-label': `${bo.f} von ${bo.n} Etappen bis ${n.titel} gelandet` },
      el('div', { class: 'lr-balken' }, el('span', { style: `width:${Math.round(100 * bo.f / bo.n)}%` })), el('span', {}, '✈'), el('small', {}, bandText)),
    stempelText ? el('p', { class: 'lr-leise lr-band-stempel' }, stempelText) : null);
  // K1/U8: Rückreise erklären – warum es kurz zurückgeht und wie es danach weitergeht
  const rr = (kind.route || []).find((r) => r.block_id === n.block_id && r.art === 'rueckreise' && r.status !== 'entfernt' && r.status !== 'fertig');
  const danach = d.jetzt.find((e) => e !== n && !e.geschafft && e.block_id !== n.block_id);
  const frueher = !rr && kl(n) && kind.klasse && kl(n) < kind.klasse;
  const rueckKarte = rr ? el('section', { class: 'lr-karte-box lr-rueckreise' },
      el('p', { class: 'lr-ueber' }, `KURZ ZURÜCK NACH ${code(n)}`),
      el('p', {}, el('b', {}, n.titel), ' sitzt noch nicht ganz sicher – das hat der Nachtest gezeigt. Wir frischen es kurz auf.'),
      danach ? el('p', { class: 'lr-leise' }, `Danach geht es weiter mit ${danach.stadt}: ${danach.titel}.`) : null)
    : frueher ? el('p', { class: 'lr-leise lr-rueckreise-hinweis' }, `${n.titel} ist Stoff aus Klasse ${kl(n)}. Du brauchst ihn für das, was danach kommt.`) : null;
  return [
    el('header', { class: 'lr-kopf lr-tafelkopf' }, el('h1', { class: 'lr-titel' }, 'Abflüge · ', kind.name),
      el('a', { class: 'lr-chip-stern', href: `#/reisepass/${kind.id}`, 'aria-label': `${lernZahl(d.konto?.sterne ?? 0)} Sterne – zum Reisepass` }, '★ ' + lernZahl(d.konto?.sterne ?? 0))),
    // K3: oben drei Mini-Linien GYM · RS · IB; Antippen öffnet „Mein Weg · Stand“ bei dieser Schulart
    d.u && kind.klasse ? lernMiniLinien(lernStandModell(d.u, kind), (y, kl) => `#/weg/${kind.id}-stand${kl ? `-${y.sa}-${kl}` : ''}`) : null,
    rueckKarte,
    el('section', { class: 'lr-abflugtafel', 'aria-label': 'Abflugtafel' },
      el('a', { class: 'lr-flug lr-flug-jetzt', href: ziel },
        el('span', { class: 'lr-flug-ort' }, el('span', { class: 'lr-klapp', role: 'img', 'aria-label': code(n) }, ...[...code(n).slice(0, 9)].map((c, i) => el('i', { style: `--i:${i}` }, c))), el('small', {}, n.titel)),
        el('span', { class: 'lr-flug-status lr-einsteigen' }, el('b', {}, n.laeuft ? 'TEST LÄUFT' : testDran ? 'TEST BEREIT' : 'EINSTEIGEN'), et.n ? el('small', {}, testDran ? 'alle Etappen sitzen' : `${offen} von ${et.n} Etappen offen`) : null)),
      ...weitere.slice(0, maxZ).map((e) => zeile(e, e.geschafft ? 'GELANDET' : e.fertig ? 'UNTERWEGS' : 'WARTET', e.geschafft ? ' lr-flug-gelandet' : '')),
      ...d.kann.slice(0, 1).map((e) => zeile(e, 'GELANDET', ' lr-flug-gelandet')),
      ...d.spaeter.slice(0, 1).map((e) => zeile(e, `AB KLASSE ${kl(e) ?? ''}`.trim(), ' lr-flug-spaeter'))),
    band,
    el('div', { class: 'lr-tafelchips' }, el('a', { href: `#/reisepass/${kind.id}` }, `◎ ${d.konto?.stempel ?? 0} Stempel`), el('span', {}, 'Abflug, wann es dir passt')),
    lernKnobelDesTages(d),
    nWdh && !n.laeuft && !testDran ? el('p', { class: 'lr-leise lr-start-info' }, `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'}, dann ${n.stadt}.`) : null,
    wdhRest ? el('a', { class: 'lr-textlink', href: `#/wiederholen/${kind.id}` }, `Noch ${wdhRest} ${wdhRest === 1 ? 'Wiederholung' : 'Wiederholungen'} offen – wenn du magst`) : null,
    el('a', { class: 'lr-textlink', href: `#/lerneinheit/${kind.id}-${n.id}` }, 'Erst die Erklärungen ansehen'),
    gruppe('Alle offenen Flüge', weitere.length > maxZ ? weitere : []),
    gruppe('Gelandet oder kann schon – zum Wiederholen', d.kann),
    gruppe('Aus früheren Klassen – zum Auffrischen', d.frueher),
    gruppe('Später – für höhere Klassen', d.spaeter),
    lernWdhErklaert(),
    jg?.themen && !(d.u && kind.klasse) ? el('section', { class: 'lr-karte-box lr-jgstand' },
      el('p', { class: 'lr-ueber' }, `MEIN STAND · ${(LERN_SCHULART[jg.schulart] || '').toUpperCase()} KLASSE ${jg.klasse}`),
      el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${jg.geschafft} von ${jg.themen} Flügen geschafft` }, el('span', { style: `width:${Math.round(100 * jg.geschafft / jg.themen)}%` })),
        el('b', {}, `${jg.geschafft} von ${jg.themen} Flügen`))) : null,
    el('div', { class: 'lr-dock lr-dock-start' }, el('a', { class: 'lr-knopf lr-einsteigen-knopf', href: ziel },
      // N4: Die Wiederholung kann aus einem anderen Ort stammen – der Knopf nennt deshalb die Anzahl, nicht das Ziel.
      ...(n.laeuft || testDran ? [el('span', {}, n.laeuft ? 'Test weitermachen' : 'Zum Test'), el('span', { class: 'lr-mono' }, code(n).slice(0, 14) + ' ›')]
        : nWdh ? [el('span', {}, `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'} ›`)]
        : wdhFertig ? [el('span', {}, `Weiter nach ${n.stadt || n.ort_titel || n.titel} ›`)]
        : [el('span', {}, 'Einsteigen'), el('span', { class: 'lr-mono' }, code(n).slice(0, 14) + ' ›')]))),
  ];
}

function lernOrtZeile(kind, e) {
  const zustand = e.laeuft ? 'Test läuft' : e.geschafft ? 'geschafft' : e.fehler ? 'noch üben' : e.n ? `${e.fertig}/${e.n}` : '';
  return el('a', { class: 'lr-zeile', href: `#/lerneinheit/${kind.id}-${e.id}` },
    el('span', { class: 'lr-zeile-icon' }, lernIcon(e.geschafft ? LI.haken : LI.ort, 22)),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, `${e.stadt || e.ort_titel}: ${e.titel}`), el('small', {}, `${e.erdteil || ''} · ${e.kontinent || ''}${e.status === 'entwurf' ? ' · Entwurf' : ''}`)),
    zustand ? el('span', { class: 'lr-zeile-zustand' }, zustand) : null, lernIcon(LI.pfeil, 20));
}

// ---------- Kind: Weltkarte ----------
// K2: Die Weltkarte ist der Reiter „Karte“ in „Mein Weg“; alte Links führen dorthin.
async function viewWeltkarte(arg) { route('weg', `${Number(arg) || ''}-karte`); }

// ---------- Kind: Reisepass ----------
async function viewReisepass(arg) {
  setChrome('Reisepass', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const { kind, konto } = d;
  const meldung = el('p', { class: 'lr-meldung', role: 'status', 'aria-live': 'polite' });
  const fertigeOrte = new Set((konto?.orte || []).filter((o) => o.abgeschlossen).map((o) => o.block_id));
  const stempel = d.orte.filter((o) => o.zustand === 'fertig' || fertigeOrte.has(o.block_id));
  const belohnungen = d.belohnungen.map((b) => {
    const fehltS = Math.max(0, b.kosten_sterne - (konto?.sterne || 0)), fehltP = Math.max(0, b.kosten_stempel - (konto?.stempel || 0));
    const kann = !fehltS && !fehltP;
    return el('div', { class: 'lr-belohnung' },
      el('div', {}, el('b', {}, b.titel), el('small', {}, [b.kosten_sterne ? `${lernZahl(b.kosten_sterne)} Sterne` : '', b.kosten_stempel ? `${b.kosten_stempel} Stempel` : ''].filter(Boolean).join(' + ') || 'gratis')),
      kann ? el('button', { type: 'button', class: 'lr-knopf lr-knopf-klein', onclick: async (ev) => {
        ev.target.disabled = true;
        try { await lernCall('schule_einloesen', { lernender_id: kind.id, belohnung_id: b.id }); meldung.textContent = `Wunsch „${b.titel}“ ist abgeschickt. Mama oder Papa bestätigen ihn.`; setTimeout(render, 1200); }
        catch (err) { meldung.textContent = err.message; ev.target.disabled = false; }
      } }, 'Einlösen') : el('small', { class: 'lr-fehlt' }, `noch ${[fehltS ? lernZahl(fehltS) + ' Sterne' : '', fehltP ? fehltP + ' Stempel' : ''].filter(Boolean).join(' + ')}`));
  });
  const look = el('div', { class: 'lr-look' });
  const setze = async (stil, welt) => {
    try { await lernCall('schule_look_setzen', { lernender_id: kind.id, stil, welt }); render(); } catch (err) { meldung.textContent = err.message; }
  };
  lernAnhaengen(look, el('p', { class: 'lr-ueber' }, 'WELT'), el('div', { class: 'lr-chips' }, ...LERN_WELTEN.map(([w, t]) =>
    el('button', { type: 'button', class: (kind.welt === w ? 'on ' : '') + 'lr-welt-' + w.toLowerCase().replace('ü', 'ue'), 'aria-pressed': String(kind.welt === w), onclick: () => setze(kind.stil || 'entdecker', w) }, t))),
  el('p', { class: 'lr-ueber' }, 'STIL'), el('div', { class: 'lr-chips' }, ...LERN_STILE.map(([s, t, h]) =>
    el('button', { type: 'button', class: kind.stil === s ? 'on' : '', 'aria-pressed': String(kind.stil === s), onclick: () => setze(s, kind.welt || 'Ozean') }, t, el('small', {}, ' · ' + h)))));
  lernErsetze(main, lernRahmen(kind, 'reisepass',
    lernKopf('REISEPASS', kind.name), lernStats(konto),
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Stempel'),
      stempel.length ? el('div', { class: 'lr-stempelraster' }, ...stempel.map((o, i) => el('div', { class: 'lr-stempel', style: `--dreh:${(i * 37) % 17 - 8}deg` }, el('b', {}, o.stadt), el('small', {}, o.kontinent_titel))))
        : el('p', { class: 'lr-leise' }, 'Noch kein Stempel. Den ersten gibt es, wenn du alle Flüge eines Ortes geschafft hast.'),
      (konto?.orte || []).filter((o) => !o.abgeschlossen && o.erledigt).map((o) => { const ort = d.orte.find((x) => x.block_id === o.block_id);
        return ort ? el('p', { class: 'lr-leise' }, `${ort.stadt}: ${o.erledigt} von ${o.themen} Flügen geschafft`) : null; })),
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Belohnungen'),
      belohnungen.length ? el('div', { class: 'lr-belohnungen' }, ...belohnungen) : el('p', { class: 'lr-leise' }, 'Mama oder Papa legen hier bald Belohnungen an.'),
      d.einloesungen.length ? el('ul', { class: 'lr-wuensche' }, ...d.einloesungen.slice(0, 5).map((x) => el('li', {}, `${x.titel}: `, el('b', {}, { beantragt: 'wartet auf Bestätigung', bestaetigt: 'bestätigt', abgelehnt: 'abgelehnt' }[x.status] || x.status)))) : null,
      meldung),
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Gestaltung'),
      el('div', { class: 'lr-chips', role: 'group', 'aria-label': 'Gestaltung' }, ...[['nacht', 'Abflug dunkel'], ['tag', 'Abflug hell'], ['alt', 'Bisheriges Design']].map(([g, t]) =>
        el('button', { type: 'button', class: lernGestaltung(kind) === g ? 'on' : '', 'aria-pressed': String(lernGestaltung(kind) === g),
          onclick: () => { try { localStorage.setItem('lern.gestaltung.' + kind.id, g); } catch { /* egal */ } render(); } }, t))),
      lernNeu(kind) ? null : look,
      kind.klasse >= 7 ? el('label', { class: 'lr-schalter' }, el('input', { type: 'checkbox', ...(lernKurzOben(kind) ? { checked: '' } : {}),
        onchange: (ev) => { try { localStorage.setItem('lern.kurzoben.' + kind.id, ev.target.checked ? '1' : '0'); } catch { /* egal */ } } }), ' „Kurz gesagt“ oben in jeder Etappe zeigen') : null),
    typeof LERN_SEITE !== 'undefined' && document.getElementById('btn-abmelden') ? el('section', { class: 'lr-karte-box lr-abmelden' },
      el('p', { class: 'lr-leise' }, 'Nur abmelden, wenn du das Gerät abgibst. Danach brauchst du deinen Lern-Code wieder.'),
      el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => document.getElementById('btn-abmelden').click() }, 'Abmelden')) : null));
}

function lernStandZeile(stand) {
  if (!stand?.length) return null;
  return el('div', { class: 'lern-stand', 'aria-label': 'Etappen' }, ...stand.filter((s) => s.pflicht).map((s) =>
    el('span', { class: 'pill ' + (LZ_KLASSE[s.status] || ''), title: s.lernziel }, lernZielName(s.lernziel) + ': ' + (LZ_STATUS[s.status] || s.status))));
}
let lernTitel = new Map(); // Lernziel → Etappentitel der zuletzt geöffneten Einheit
const lernZielName = (k) => lernTitel.get(k) || String(k).replace(/_/g, ' ').replace(/ae/g, 'ä').replace(/oe/g, 'ö').replace(/ue/g, 'ü').replace(/^./, (c) => c.toUpperCase());

// ---------- Aufgaben-Darstellung ----------
// Zahlenstrahl: Markierungen 0..abschnitte; bei antworttyp markierung antippbar; pfeil zeigt auf eine Markierung.
function lernZahlenstrahl(g, waehlbar, onWahl) {
  // Seit 16.11. zusätzlich: punkte [{wert, name}], boegen [{von, bis, name}] (Sprung mit Pfeil), bereich {von, bis} oder Liste davon (schattiert), beschriftet: 'alle'.
  const punkte = g.punkte || [], boegen = g.boegen || [], bereiche = g.bereich ? (Array.isArray(g.bereich) ? g.bereich : [g.bereich]) : [];
  const oben = boegen.length ? 62 : punkte.some((q) => q.name) ? 30 : 0;
  const ns = 'http://www.w3.org/2000/svg', B = 340, L = 30, R = B - 40, Y = 44 + oben, n = Math.max(1, Number(g.abschnitte) || 1);
  const x = (i) => L + (R - L) * i / n;
  const xv = (v) => L + (R - L) * (v - g.start) / ((g.ende - g.start) || 1);
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', `0 0 ${B} ${84 + oben}`); svg.setAttribute('class', 'lern-strahl'); svg.setAttribute('role', waehlbar ? 'group' : 'img');
  svg.setAttribute('aria-label', `Zahlenstrahl von ${lernZahl(g.start)} bis ${lernZahl(g.ende)} mit ${n} gleichen Abschnitten`);
  const mk = (tag, a, txt) => { const e = document.createElementNS(ns, tag); for (const [k, v] of Object.entries(a)) e.setAttribute(k, v); if (txt !== undefined) e.textContent = txt; svg.append(e); return e; };
  mk('line', { x1: L - 6, y1: Y, x2: R + 14, y2: Y, class: 'achse' });
  mk('path', { d: `M${R + 14} ${Y} l-7 -4 v8 z`, class: 'spitze' });
  const knoepfe = [];
  for (let i = 0; i <= n; i++) {
    mk('line', { x1: x(i), y1: Y - 8, x2: x(i), y2: Y + 8, class: 'strich' });
    if (waehlbar) {
      const marke = mk('circle', { cx: x(i), cy: Y, r: 11, class: 'ziel-marke' });
      // Tippfläche: volle Höhe, halber Strichabstand nach links und rechts
      const bw = (R - L) / n;
      const k = mk('rect', { x: x(i) - bw / 2, y: 2, width: bw, height: 80, class: 'ziel', tabindex: 0, role: 'button', 'aria-label': `Markierung ${i}` });
      const w = () => { knoepfe.forEach((c, j) => c.classList.toggle('on', j === i)); onWahl(i); };
      k.addEventListener('click', w); k.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); w(); } });
      knoepfe.push(marke);
    }
  }
  for (const r of bereiche) { const e = document.createElementNS(ns, 'rect'); const xa = Math.min(xv(r.von), xv(r.bis));
    for (const [k, v] of Object.entries({ x: xa, y: Y - 12, width: Math.abs(xv(r.bis) - xv(r.von)), height: 24, class: 'bereich' })) e.setAttribute(k, v); svg.insertBefore(e, svg.firstChild); }
  { // Zahlen unter dem Strahl: Anfang und Ende immer; die 0 und (bei beschriftet: 'alle') weitere, soweit Platz ist
    const text = (v) => lernZahl(v).replace('-', '−'); const belegt = [];
    const setze = (v) => { const t = text(v), w = lernBreite(t), px0 = xv(v); if (belegt.some(([a, b]) => px0 - w / 2 < b + 4 && px0 + w / 2 > a - 4)) return; belegt.push([px0 - w / 2, px0 + w / 2]); mk('text', { x: px0, y: Y + 30, class: 'zahl' }, t); };
    setze(g.start); setze(g.ende);
    if (g.start < 0 && g.ende > 0) setze(0);
    for (const q of punkte) if (q.zahl !== false) setze(q.wert);
    if (g.beschriftet === 'alle') for (let i = 1; i < n; i++) setze(g.start + (g.ende - g.start) * i / n);
  }
  boegen.forEach((bo, j) => { // Sprung von → bis als Bogen mit Pfeilspitze
    const a = xv(bo.von), z = xv(bo.bis), h = Math.min(40, 14 + Math.abs(z - a) * 0.28) + (j % 2 ? 0 : 0), my = Y - 10 - h;
    mk('path', { d: `M${a.toFixed(1)} ${Y - 10} Q${((a + z) / 2).toFixed(1)} ${(my - h * 0.55).toFixed(1)} ${z.toFixed(1)} ${Y - 10}`, class: 'bogen' + lernNeu1(g, 'boegen', bo) });
    const r = z >= a ? 1 : -1; mk('path', { d: `M${z.toFixed(1)} ${Y - 9} l${(-r * 9).toFixed(1)} -3 l${(r * 4).toFixed(1)} -7 z`, class: 'bogen-spitze' });
    if (bo.name) mk('text', { x: Math.min(B - lernBreite(bo.name) / 2 - 2, Math.max(lernBreite(bo.name) / 2 + 2, (a + z) / 2)), y: Math.max(16, my - h * 0.2 - 4), class: 'zahl fett' }, bo.name);
  });
  { // Punkte mit Namen: ohne Bögen über dem Strahl, mit Bögen darunter (zweite Zeile); Namen, die sich berühren würden, rücken eine Zeile weiter
    const unten = boegen.length > 0; const belegt = [];
    punkte.forEach((q) => { mk('circle', { cx: xv(q.wert), cy: Y, r: lernNeu1(g, 'punkte', q) ? 8 : 6, class: 'punkt' + lernNeu1(g, 'punkte', q) }); if (!q.name) return;
      const w = lernBreite(q.name), m = Math.min(B - w / 2 - 2, Math.max(w / 2 + 2, xv(q.wert))); let z = 0;
      while (belegt.some(([a0, b0, z0]) => z0 === z && m - w / 2 < b0 + 4 && m + w / 2 > a0 - 4)) z++;
      belegt.push([m - w / 2, m + w / 2, z]); mk('text', { x: m, y: unten ? Y + 52 + z * 20 : Y - 14 - z * 20, class: 'zahl' }, q.name); });
    const zeilen = belegt.reduce((mx, r) => Math.max(mx, r[2] + 1), 0);
    if (unten && zeilen) svg.setAttribute('viewBox', `0 0 ${B} ${84 + oben + zeilen * 20 + 4}`);
  }
  if (g.pfeil !== undefined && g.pfeil !== null) mk('path', { d: `M${x(g.pfeil)} ${Y - 12} l-6 -12 h12 z`, class: 'pfeil' });
  // N7: Testergebnis – gewählte falsche Markierung rot, richtige grün eingezeichnet
  if (Number.isInteger(g._gewaehlt) && g._gewaehlt !== g._richtig) mk('circle', { cx: x(g._gewaehlt), cy: Y, r: 9, class: 'marke-falsch' });
  if (Number.isInteger(g._richtig)) { mk('circle', { cx: x(g._richtig), cy: Y, r: 10, class: 'marke-richtig' }); mk('text', { x: x(g._richtig), y: Y - 16, class: 'zahl fett marke-richtig-text' }, '✓'); }
  return svg;
}

// ---------- Terme lesen (W150) ----------
// Liest einen frei getippten Term und füllt damit die Vorlage der Aufgabe (z. B. „□x(□x + □)“) – die Datenbank prüft wie bisher die Zahlen.
const lernTermNorm = (t) => String(t ?? '').replace(/\s+/g, '').replace(/[−–]/g, '-').replace(/[·*⋅×]/g, '').replace(/\^2/g, '²').replace(/\^3/g, '³')
  .replace(/\+-|-\+/g, '-').replace(/--/g, '+').replace(/\.(?=\d)/g, ',');
function lernMonoKey(v) {
  const m = [...v.matchAll(/([a-z])([²³]?)/g)];
  if (m.map((x) => x[0]).join('') !== v) return null;
  const pot = {};
  for (const [, b, e] of m) pot[b] = (pot[b] || 0) + (e === '²' ? 2 : e === '³' ? 3 : 1);
  return Object.keys(pot).sort().map((b) => b + (pot[b] === 1 ? '' : pot[b] === 2 ? '²' : pot[b] === 3 ? '³' : '^' + pot[b])).join('');
}
function lernMono(t) {
  const m = t.match(/^([+-]?)(\d+(?:,\d+)?)?([a-z²³]*)$/);
  if (!m || (!m[2] && !m[3])) return null;
  const key = lernMonoKey(m[3]); if (key === null) return null;
  let c = m[2] ? Number(m[2].replace(',', '.')) : 1; if (m[1] === '-') c = -c;
  return { key, c };
}
function lernPoly(t) {
  const glieder = t.match(/[+-]?[^+-]+/g);
  if (!glieder || glieder.join('') !== t) return null;
  const map = new Map();
  for (const g of glieder) { const mo = lernMono(g); if (!mo) return null; if (map.has(mo.key)) return { doppelt: true }; map.set(mo.key, mo.c); }
  return map;
}
function lernVorlage(schablone) {
  const s = lernTermNorm(schablone); const k = s.indexOf('(');
  const keys = (x) => (x.match(/[+-]?[^+-]+/g) || []).map((g) => lernMonoKey(g.replace(/^[+-]?□/, '')));
  return k < 0 ? { prefix: null, inner: keys(s) } : { prefix: lernMonoKey(s.slice(0, k).replace('□', '')), inner: keys(s.slice(k + 1, s.lastIndexOf(')'))) };
}
const lernZahlText = (n) => (n < 0 ? '−' : '') + String(Math.abs(Math.round(n * 1e6) / 1e6)).replace('.', ',');
function lernTermWerte(schablone, eingabe) {
  const v = lernVorlage(schablone); const s = lernTermNorm(eingabe); let innen = s; let vor = [];
  if (v.prefix !== null) {
    const k = s.indexOf('(');
    if (k < 0 || !s.endsWith(')')) return { fehler: 'klammer' };
    const p = s.slice(0, k); innen = s.slice(k + 1, -1);
    const mo = p === '' || p === '+' ? { key: '', c: 1 } : p === '-' ? { key: '', c: -1 } : lernMono(p);
    if (!mo || mo.key !== v.prefix) return { fehler: 'form' };
    vor = [mo.c];
  } else if (/[()]/.test(s)) return { fehler: 'ohneklammer' };
  const map = lernPoly(innen);
  if (!map) return { fehler: 'lesen' };
  if (map.doppelt) return { fehler: 'doppelt' };
  for (const k of map.keys()) if (!v.inner.includes(k)) return { fehler: 'form' };
  return { werte: [...vor, ...v.inner.map((k) => (map.has(k) ? map.get(k) : 0))].map(lernZahlText) };
}
// Ist eine (falsche) Antwort zu einer Ausklammer-Vorlage trotzdem gleichwertig zur Lösung? Dann fehlt nur der größte Faktor.
function lernGleichwertigAusgeklammert(schablone, werte, loesung) {
  const v = lernVorlage(schablone);
  if (v.prefix === null || !Array.isArray(werte) || !Array.isArray(loesung)) return false;
  const zahl = (x) => Number(String(x).replace('−', '-').replace(',', '.'));
  const aus = (w) => { const m = new Map(); v.inner.forEach((k, i) => { const key = lernMonoKey(v.prefix + k); m.set(key, (m.get(key) || 0) + zahl(w[0]) * zahl(w[i + 1])); }); return m; };
  const a = aus(werte), b = aus(loesung);
  return [...new Set([...a.keys(), ...b.keys()])].every((k) => Math.abs((a.get(k) || 0) - (b.get(k) || 0)) < 1e-9);
}
// Term-Vorlage (Polynom wie „□x² + □x + □“ oder „□(□x + □)“): frei eintippen. Alles andere: je Lücke ein Feld.
const lernIstTermVorlage = (schablone) => { const t = String(schablone || ''); return /[a-z]/.test(t) && /^[\s□+\-−·()a-z²³]*$/.test(t); };
function lernTermFehler(f, schablone) {
  const form = String(schablone).replace(/□/g, '…');
  return { klammer: `Hier gehört eine Klammer in die Antwort, so: ${form}`, ohneklammer: 'Die Antwort soll ohne Klammer sein. Rechne die Klammer aus.',
    form: `So kann ich das nicht prüfen. Die Antwort soll so aussehen: ${form}`, doppelt: 'Fasse gleiche Glieder noch zusammen.',
    lesen: 'Das kann ich nicht lesen. Schreib zum Beispiel 3x² − 2x + 5.' }[f] || 'Bitte prüfe deine Eingabe.';
}
function lernVorlageFuellen(schablone, werte) {
  const st = String(schablone).split('□');
  return st.map((t, i) => t + (i < st.length - 1 ? String(werte[i] ?? '') : '')).join('').replace(/\+ ?[−-]/g, '− ');
}

// Liefert { node, antwort(), sperren() }; antwort() ist null, solange nichts eingegeben ist.
function lernAufgabe(a, vorher, opts = {}) {
  const f = a.frage || {};
  let wert = vorher ?? null; let fehler = null; let stellenTipp = null, stellenNeu = null; const optionen = [];
  const teile = [el('p', { class: 'lern-frage' }, lernText(f.text))];
  if (f.hinweis && a.antworttyp !== 'luecken') teile.push(el('p', { class: 'small muted' }, f.hinweis));
  const felder = [];
  if (a.antworttyp === 'markierung') {
    const strahl = lernZahlenstrahl(f.grafik || {}, true, (i) => { wert = { index: i }; });
    if (wert) strahl.querySelectorAll('.ziel')[wert.index]?.classList.add('on');
    teile.push(strahl);
  } else if (f.grafik) teile.push(f.grafik.typ && f.grafik.typ !== 'zahlenstrahl' ? lernBild(f.grafik) : lernZahlenstrahl(f.grafik, false));
  if (a.antworttyp === 'auswahl') {
    const name = 'a' + a.id + '-' + Math.random().toString(36).slice(2, 7);
    teile.push(el('div', { class: 'lern-auswahl', role: 'radiogroup' }, (a.antworten || []).map((t, i) => {
      const inp = el('input', { type: 'radio', name, value: String(i) });
      if (wert?.index === i) inp.checked = true;
      inp.addEventListener('change', () => { wert = { index: i }; });
      felder.push(inp);
      const lab = el('label', { class: 'lern-option' }, inp, el('span', {}, t)); optionen.push(lab); return lab;
    })));
  } else if (a.antworttyp === 'zahl' || a.antworttyp === 'text') {
    const inp = el('input', { type: 'text', autocomplete: 'off', autocapitalize: a.antworttyp === 'text' ? 'characters' : 'off',
      spellcheck: 'false', 'aria-label': 'Antwort', class: 'lern-eingabe' });
    if (wert?.wert) inp.value = wert.wert;
    inp.addEventListener('input', () => { wert = inp.value.trim() ? { wert: inp.value } : null; });
    felder.push(inp);
    if (opts.stellen && a.antworttyp === 'zahl') {
      // W150 Abflug (Klasse 5/6): ganze Zahlen laufen in Stellenwert-Kacheln; Spalte antippen, dann Ziffer wählen.
      const KOEPFE = ['E', 'Z', 'H', 'T', 'ZT', 'HT', 'M', 'ZM', 'HM'];
      const st = el('div', { class: 'lern-stellen', role: 'group', 'aria-label': 'Stellenwerte' });
      let pos = null;
      const zeichne = () => {
        const v = inp.value.replace(/\s/g, ''); const ok = /^\d{0,9}$/.test(v);
        st.hidden = !ok; inp.classList.toggle('lern-verdeckt', ok);
        if (!ok) { pos = null; return; }
        const n = Math.max(4, v.length);
        lernErsetze(st, ...Array.from({ length: n }, (_, i) => { const p = n - 1 - i; const z = p < v.length ? v[v.length - 1 - p] : '';
          return el('button', { type: 'button', class: 'lern-stelle' + (pos === p ? ' dran' : '') + (z ? '' : ' leer'), disabled: inp.disabled, 'aria-label': `${KOEPFE[p]}: ${z || 'leer'}`, 'aria-pressed': String(pos === p),
            onmousedown: (ev) => ev.preventDefault(), onclick: () => { pos = pos === p ? null : p; zeichne(); } }, el('small', {}, KOEPFE[p]), el('b', {}, z)); }));
      };
      stellenTipp = (t) => {
        if (pos === null || !/^\d$/.test(t)) { pos = null; return false; }
        const v = inp.value.replace(/\s/g, '');
        inp.value = pos < v.length ? v.slice(0, v.length - 1 - pos) + t + v.slice(v.length - pos) : t + '0'.repeat(pos - v.length) + v;
        pos = pos > 0 ? pos - 1 : null; return true;
      };
      inp.addEventListener('input', zeichne);
      stellenNeu = zeichne; zeichne();
      teile.push(st);
    }
    teile.push(el('div', { class: 'lern-zeile' }, inp, a.einheit ? el('span', { class: 'lern-einheit-zeichen' }, a.einheit) : null));
  } else if (a.antworttyp === 'luecken' && !lernIstTermVorlage(f.schablone)) {
    // W150: allgemeine Lücken (Bruch □/□, Zahlenpaar x = □; y = □, Punkt S(□ | □) …): je Lücke ein kleines Zahlenfeld.
    const st = String(f.schablone || '□').split('□'); const n = st.length - 1;
    const bruch = String(f.schablone).trim() === '□/□';
    const eingaben = Array.from({ length: n }, (_, i) => el('input', { type: 'text', inputmode: 'text', autocomplete: 'off', class: 'lern-luecke',
      'aria-label': bruch ? (i ? 'Nenner' : 'Zähler') : `Lücke ${i + 1}`, value: wert?.werte?.[i] ?? '' }));
    const lies = () => {
      const w = eingaben.map((x) => x.value.trim());
      wert = w.every((x) => x !== '') ? { werte: w } : null;
      fehler = wert ? null : (n > 1 ? 'Bitte fülle alle Felder aus.' : 'Bitte erst antworten.');
    };
    eingaben.forEach((x) => { x.addEventListener('input', lies); felder.push(x); });
    if (f.hinweis) teile.push(el('p', { class: 'small muted' }, f.hinweis));
    teile.push(bruch
      ? el('div', { class: 'lern-bruch', role: 'group', 'aria-label': 'Bruch' }, eingaben[0], el('span', { class: 'lern-bruchstrich', 'aria-hidden': 'true' }), eingaben[1])
      : el('div', { class: 'lern-lueckenzeile' }, ...st.flatMap((t, i) => [t ? el('span', {}, t) : null, i < n ? eingaben[i] : null]).filter(Boolean)));
    lies(); fehler = null;
  } else if (a.antworttyp === 'luecken') {
    // W150: Term frei eintippen (wie im Heft); die App liest daraus die Zahlen für die Vorlage.
    const vorlage = String(f.schablone || '□');
    const inp = el('input', { type: 'text', inputmode: 'text', autocomplete: 'off', autocapitalize: 'off', spellcheck: 'false', 'aria-label': 'Dein Term', class: 'lern-term',
      placeholder: 'Term eintippen', value: wert?.werte ? lernVorlageFuellen(vorlage, wert.werte) : '' });
    const lies = () => {
      const r = inp.value.trim() ? lernTermWerte(vorlage, inp.value) : null;
      wert = r?.werte ? { werte: r.werte } : null; fehler = r?.fehler ? lernTermFehler(r.fehler, vorlage) : null;
    };
    inp.addEventListener('input', lies);
    felder.push(inp);
    const tippe = (t) => {
      const a0 = inp.selectionStart ?? inp.value.length, b0 = inp.selectionEnd ?? a0;
      inp.value = inp.value.slice(0, a0) + t + inp.value.slice(b0); inp.focus(); inp.setSelectionRange(a0 + t.length, a0 + t.length); lies();
    };
    const buchst = [...new Set((vorlage.match(/[a-z]/g) || []))];
    const tasten = [...buchst, '²', ...(vorlage.includes('(') ? ['(', ')'] : []), '+', '−'];
    teile.push(inp, el('div', { class: 'lern-tasten' }, ...tasten.map((t) => el('button', { type: 'button', class: 'lern-taste', 'aria-label': t === '²' ? 'hoch 2' : t === '−' ? 'minus' : t === '+' ? 'plus' : t === '(' ? 'Klammer auf' : t === ')' ? 'Klammer zu' : t,
      onmousedown: (ev) => ev.preventDefault(), onclick: () => tippe(t) }, t)), el('button', { type: 'button', class: 'lern-taste', 'aria-label': 'löschen',
      onmousedown: (ev) => ev.preventDefault(), onclick: () => { const a0 = inp.selectionStart ?? inp.value.length; if (a0 > 0) { inp.value = inp.value.slice(0, a0 - 1) + inp.value.slice(a0); inp.setSelectionRange(a0 - 1, a0 - 1); lies(); } } }, '⌫')));
    if (wert?.werte) lies();
  }
  // W150 Abflug: Zahlenfelder bekommen ein eigenes Tastenfeld (keine Systemtastatur auf Tippgeräten).
  const zahlFelder = opts.tasten && (a.antworttyp === 'zahl' || (a.antworttyp === 'luecken' && !lernIstTermVorlage(f.schablone))) ? felder.filter((x) => x.type === 'text') : [];
  let aktiv = zahlFelder[0] || null;
  const grob = !window.matchMedia?.('(pointer: fine)').matches;
  zahlFelder.forEach((x) => { x.classList.add('lern-kachel'); if (grob) x.setAttribute('inputmode', 'none'); x.addEventListener('focus', () => { aktiv = x; zahlFelder.forEach((y) => y.classList.toggle('dran', y === x)); }); });
  if (aktiv && zahlFelder.length > 1) aktiv.classList.add('dran');
  const melde = () => aktiv.dispatchEvent(new Event('input', { bubbles: true }));
  const tasten = zahlFelder.length ? {
    tippe: (t) => { if (aktiv.disabled) return; if (!(stellenTipp && stellenTipp(t))) aktiv.value += t; melde(); },
    loesche: () => { if (aktiv.disabled) return; if (!aktiv.value && zahlFelder.indexOf(aktiv) > 0) { aktiv = zahlFelder[zahlFelder.indexOf(aktiv) - 1]; zahlFelder.forEach((y) => y.classList.toggle('dran', y === aktiv)); } aktiv.value = aktiv.value.slice(0, -1); melde(); },
    weiter: () => { const i = zahlFelder.indexOf(aktiv); if (i < zahlFelder.length - 1) { aktiv = zahlFelder[i + 1]; zahlFelder.forEach((y) => y.classList.toggle('dran', y === aktiv)); return true; } return false; },
    system: () => { zahlFelder.forEach((x) => x.removeAttribute('inputmode')); aktiv.focus(); },
  } : null;
  // Nach dem Prüfen (Auswahl): gewählte falsche Antwort rot mit ✗, richtige grün mit ✓ – nicht nur über Farbe.
  const zeigeLoesung = (loesung) => { if (a.antworttyp !== 'auswahl' || loesung?.index === undefined) return;
    optionen.forEach((lab, i) => { const richtigHier = i === loesung.index, gewaehlt = wert?.index === i; if (!richtigHier && !gewaehlt) return;
      lab.classList.add(richtigHier ? 'ist-richtig' : 'ist-falsch'); lernAnhaengen(lab, el('span', { class: 'lern-option-zeichen', 'aria-label': richtigHier ? 'richtig' : 'falsch' }, richtigHier ? '✓' : '✗')); }); };
  return { node: el('div', { class: 'lern-aufgabe' }, ...teile), antwort: () => wert, fehlerText: () => fehler, tasten, zeigeLoesung,
    sperren: (an = true) => { felder.forEach((x) => { x.disabled = an; }); stellenNeu?.(); } };
}

// W150 Abflug: Tastenfeld im Daumenbereich. Prüfen ist die gelbe Taste.
function lernTastenfeld(t, pruefen) {
  const k = (text, fn, extra = {}) => el('button', { type: 'button', class: 'lr-taste', onmousedown: (ev) => ev.preventDefault(), onclick: fn, ...extra }, text);
  pruefen.classList.add('lr-taste-pruefen');
  return el('div', { class: 'lr-tastenfeld', role: 'group', 'aria-label': 'Tastenfeld' },
    ...['7', '8', '9'].map((z) => k(z, () => t.tippe(z))), k('⌫', () => t.loesche(), { 'aria-label': 'löschen', class: 'lr-taste lr-taste-leise' }),
    ...['4', '5', '6'].map((z) => k(z, () => t.tippe(z))), k('−', () => t.tippe('−'), { 'aria-label': 'minus', class: 'lr-taste lr-taste-leise' }),
    ...['1', '2', '3'].map((z) => k(z, () => t.tippe(z))), k(',', () => t.tippe(','), { 'aria-label': 'Komma', class: 'lr-taste lr-taste-leise' }),
    k('0', () => t.tippe('0'), { class: 'lr-taste lr-taste-null' }), pruefen,
    k('⌨', () => t.system(), { 'aria-label': 'Gerätetastatur benutzen', class: 'lr-taste lr-taste-leise lr-taste-system' }));
}
// W150 Abflug: „Kurskorrektur“ – deine Zahl und die Zielzahl stellengerecht untereinander, Abweichungen markiert.
function lernKurs(a, w) {
  if (a.antworttyp !== 'zahl' || a.loesung?.wert === undefined) return null;
  const norm = (x) => String(x ?? '').replace(/\s/g, '').replace(/[−–]/g, '-').replace(',', '.');
  const du = norm(w?.wert), ziel = norm(a.loesung.wert);
  if (!/^-?\d+(\.\d+)?$/.test(du) || !/^-?\d+(\.\d+)?$/.test(ziel) || du === ziel) return null;
  const teil = (x) => { const [g, n = ''] = x.replace('-', '').split('.'); return { neg: x.startsWith('-'), g, n }; };
  const d = teil(du), z = teil(ziel);
  const lg = Math.max(d.g.length, z.g.length), ln = Math.max(d.n.length, z.n.length);
  if (lg + ln > 9) return null;
  const zeile = (x) => [x.neg ? '−' : '', ...x.g.padStart(lg, ' '), ...(ln ? [x.n ? ',' : ' ', ...x.n.padEnd(ln, ' ')] : [])];
  const zd = zeile(d), zz = zeile(z);
  const koepfe = !ln && lg <= 7 ? ['', ...['M', 'HT', 'ZT', 'T', 'H', 'Z', 'E'].slice(7 - lg)] : null;
  const reihe = (name, zs, andere) => el('div', { class: 'lr-kurs-zeile' }, el('span', { class: 'lr-kurs-name' }, name),
    ...zs.map((c, i) => { const kp = !!ln && i === lg + 1; // N3: Komma-Platz ohne Komma bleibt leer, ohne Rahmen
      return el('span', { class: 'lr-kurs-kachel' + (kp ? ' komma' : '') + (c.trim() === '' ? ' leer' : '') + (c !== andere[i] && !(kp && c !== ',') ? ' ab' : '') }, c.trim()); }));
  return el('div', { class: 'lr-kurs', role: 'img', 'aria-label': `Deine Zahl ${w.wert}, Ziel ${lernZahl(a.loesung.wert)}` },
    koepfe ? el('div', { class: 'lr-kurs-zeile lr-kurs-kopf' }, el('span', { class: 'lr-kurs-name' }), ...koepfe.map((c) => el('span', { class: 'lr-kurs-kachel' }, c))) : null,
    reihe('DU', zd, zz), reihe('ZIEL', zz, zd));
}

// Markierung als Zahl: der i-te Strich nach dem Anfang
function lernStrichText(g, i) {
  if (!g || i === undefined || i === null) return `Strich ${i}`;
  const v = Number(g.start) + i * (Number(g.ende) - Number(g.start)) / (Number(g.abschnitte) || 1);
  return i === 0 ? `${lernZahl(v)} (der Anfang)` : `${lernZahl(v)} (der ${i}. Strich nach dem Anfang)`;
}
// Schreibweise: Minuszeichen statt Bindestrich; „+ −1“ wird „− 1“, „− −1“ wird „+ 1“ (z. B. □x + □ mit −3 und −1 → −3x − 1).
function lernVorzeichenText(t) {
  return String(t).replace(/(^|[^\w)])-(?=\d)/g, '$1−').replace(/\+ ?−\s?(?=\d)/g, '− ').replace(/− ?−\s?(?=\d)/g, '+ ');
}
// V3: erkanntes Fehlermuster (von der Datenbank als „grund“) → ein Satz als erste Zeile der Rückmeldung
const LERN_GRUND = {
  vorzeichen: 'Die Zahl stimmt – schau aufs Vorzeichen.',
  komma: 'Die Ziffern stimmen – schau, wo das Komma hingehört.',
  falsche_einheit: 'Schau auf die Einheit: Ist nach € oder nach % gefragt?',
  vertauscht: 'Die Zahlen stimmen, aber sie stehen in den falschen Feldern.',
  gerundet: 'Fast – das ist nur ungefähr. Rechne genau oder runde so, wie es die Bordkarte verlangt.',
};
// M6: Fehler-Detektiv. Bei Auswahl-Bordkarten gibt es kein Fehlermuster je falscher Option – das allgemeine Muster der Etappe passt dort oft nicht zur Wahl,
// deshalb ein neutraler Satz. Andere Bordkarten: das Muster der Etappe, wenn die Datenbank keinen eigenen Grund erkannt hat.
function lernDetektiv(a, e, r, titel) {
  if (LERN_GRUND[r.grund]) return null;
  if (a.antworttyp === 'auswahl') return el('div', { class: 'lr-fehler lr-detektiv' }, el('p', { class: 'lr-ueber' }, 'NOCH EINMAL HINSEHEN'), el('p', {}, 'Schau dir deine Wahl und die Frage noch einmal an.'));
  return e.fehler ? el('div', { class: 'lr-fehler lr-detektiv' }, el('p', { class: 'lr-ueber' }, titel), el('p', {}, ...lernMarkiert(e.fehler))) : null;
}
function lernLoesungText(a) {
  const l = a.loesung || {};
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[l.index] ?? '';
  if (a.antworttyp === 'markierung') return lernStrichText(a.frage?.grafik, l.index);
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return lernVorzeichenText(s.map((t, i) => t + (i < s.length - 1 ? String(l.werte?.[i] ?? '') : '')).join('')); }
  if (a.antworttyp === 'text') return l.text ?? '';
  return l.wert !== undefined ? lernZahl(l.wert) + (l.einheit ? ' ' + l.einheit : '') : '';
}
function lernAntwortText(a, w) {
  if (!w) return '(keine Antwort)';
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[w.index] ?? '';
  if (a.antworttyp === 'markierung') return lernStrichText(a.frage?.grafik, w.index);
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return lernVorzeichenText(s.map((t, i) => t + (i < s.length - 1 ? (w.werte?.[i] ?? '') : '')).join('')); }
  return String(w.wert ?? '').replace(/^-/, '−');
}

// ---------- Kind: Lerneinheit in Etappen ----------
// #/lerneinheit/<kind>-<einheit>         Übersicht: Etappen-Weg, danach Test
// #/lerneinheit/<kind>-<einheit>-<n>     Etappe n: Kurz erklärt → Selbst probieren → geschafft
// #/lerneinheit/<kind>-<einheit>-test    Test / Verbessern / Nachtest
// Eine Etappe ist ein Lernziel; geschafft, wenn ihre Übungsaufgaben einmal richtig gelöst sind (Datenbank: schule.etappen_stand).

// Text mit ⟦markierten⟧ Stellen als Knoten (markierte Teile hervorgehoben).
// Zusätzlich (Vorgabe Erklärungen 16.11.): Brüche a/b gestapelt; mit wctx werden neue Wörter beim ersten Vorkommen antippbar.
const LERN_BUCHST = 'A-Za-zÄÖÜäöüß';
function lernBruchKnoten(s) {
  const out = []; let last = 0; let m;
  const re = new RegExp(`(?<![\\d/.,:${LERN_BUCHST}])(\\d{1,3})/(\\d{1,3})(?![\\d/${LERN_BUCHST}]|[.,:]\\d)`, 'g'); // nicht: Daten, Uhrzeiten, km/h, Adressen
  while ((m = re.exec(s))) {
    if (m.index > last) out.push(lernText(s.slice(last, m.index)));
    out.push(el('span', { class: 'lern-bruch-text', role: 'img', 'aria-label': `${m[1]} durch ${m[2]}` }, el('span', {}, m[1]), el('span', {}, m[2])));
    last = re.lastIndex;
  }
  if (last < s.length) out.push(lernText(s.slice(last)));
  return out;
}
function lernWortListe(woerter) {
  const esc = (x) => x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return (woerter || []).filter((w) => Array.isArray(w) && w[0] && w[1]).map(([wort, text]) => {
    const kern = wort.split(' (')[0].trim();
    const nurWort = new RegExp(`^[${LERN_BUCHST}-]+( [${LERN_BUCHST}-]+)*$`).test(kern);
    // Beugungen: Wortanfang plus bis zu 3 Buchstaben („Zuordnung“ trifft auch „Zuordnungen“); Zeichenfolgen wie „(1 | 5)“ nur wörtlich.
    const re = nurWort ? new RegExp(`(?<![${LERN_BUCHST}])${esc(kern)}[a-zäöüß]{0,3}(?![${LERN_BUCHST}])`, 'i') : new RegExp(esc(wort));
    return { wort, text, re };
  });
}
function lernWortKnoten(s, wctx) {
  if (!wctx?.liste?.length) return lernBruchKnoten(s);
  let best = null;
  for (const w of wctx.liste) { if (wctx.gesehen.has(w.wort)) continue; const m = w.re.exec(s); if (m && (!best || m.index < best.m.index)) best = { w, m }; }
  if (!best) return lernBruchKnoten(s);
  wctx.gesehen.add(best.w.wort);
  const i = best.m.index, t = best.m[0];
  const knopf = el('button', { type: 'button', class: 'lr-wort', 'aria-expanded': 'false', onclick: () => {
    const block = knopf.closest('li, p, dd, div'); if (!block) return;
    const alt = block.querySelector(':scope > .lr-wort-box');
    block.querySelectorAll(':scope .lr-wort').forEach((k) => k.setAttribute('aria-expanded', 'false'));
    if (alt) { const selbe = alt.dataset.wort === best.w.wort; alt.remove(); if (selbe) return; }
    knopf.setAttribute('aria-expanded', 'true');
    const box = el('span', { class: 'lr-wort-box', role: 'note' }, el('b', {}, ...lernBruchKnoten(best.w.wort)), ' – ', ...lernBruchKnoten(best.w.text)); box.dataset.wort = best.w.wort;
    lernAnhaengen(block, box);
  } }, ...lernBruchKnoten(t));
  return [...lernBruchKnoten(s.slice(0, i)), knopf, ...lernWortKnoten(s.slice(i + t.length), wctx)];
}
function lernMarkiert(t, wctx) {
  const teile = String(t ?? '').split(/⟦|⟧/);
  return teile.flatMap((s, i) => (i % 2 ? [el('mark', {}, ...lernWortKnoten(s, wctx))] : lernWortKnoten(s, wctx)));
}
// „Kurz gesagt“: der erste Satz des Merksatzes (ohne Markierung).
// N2/A2: „Kurz gesagt“ = der erste Satz des Merksatzes. Satzende ist jedes . ! ? vor einem Leerzeichen oder dem Textende –
// aber nicht nach Abkürzungen (z. B., d. h., u. a., bzw., ca., usw., vgl. …) und nicht nach einer Ordnungszahl vor kleinem Wort („die 3. Wurzel“).
const LERN_ABK = /(?:^|[\s(„])(?:z\.\s?B|d\.\s?h|u\.\s?a|z\.\s?T|s\.\s?o|s\.\s?u|o\.\s?ä|bzw|ca|usw|vgl|etc|ggf|evtl|bspw|inkl|Nr)\.$/;
function lernSatzEnde(t, ab = 0) {
  const re = /[.!?](?=\s|$)/g; re.lastIndex = ab; let m;
  while ((m = re.exec(t))) {
    const bis = t.slice(0, m.index + 1);
    if (m[0] === '.' && LERN_ABK.test(bis)) continue;
    if (m[0] === '.' && /(?:^|[\s(„])[zdusoZDUSO]\.$/.test(bis) && /^\s?[A-Za-zä]\./.test(t.slice(m.index + 1))) continue; // erster Teil von „z. B.“, „d. h.“ …
    if (m[0] === '.' && /\d\.$/.test(bis) && /^\s+[a-zäöüß]/.test(t.slice(m.index + 1))) continue;
    // P1: Aufzählung beginnt nur mit „1.“ (am Satzanfang, nach Doppelpunkt, Strichpunkt, Klammer oder Komma) – „(a₁ + aₙ) : 2.“ ist ein Satzende
    if (m[0] === '.' && /(?:^\d{1,2}|(?:[:;(]\s*|,\s+)1|\b(?:[Dd]ie|[Dd]er|[Dd]as|[Dd]en|[Dd]em|[Dd]es|zur|zum|im|am|ein|eine|einer|jede|jeder)\s\d{1,2})\.$/.test(bis)) continue; // Aufzählung „1. …“ oder Ordnungszahl „die 3. Wurzel“
    if (m[0] === '.' && /(?:^|[;(]\s*|,\s+)\d{1,2}\.$/.test(bis) && /(?:^|[:;(]\s*|,\s+)1\.\s/.test(bis)) continue; // weitere Punkte einer Aufzählung „1. …, 2. …“ (nach Komma/Strichpunkt)
    return m.index + 1;
  }
  return -1;
}
function lernKurzGesagt(regel) { // N2: ganz zeigen, nie mit „…“ abschneiden; höchstens ein Satz
  const t = String(regel ?? '').replace(/⟦|⟧/g, '').trim();
  const e = lernSatzEnde(t); return (e > 0 ? t.slice(0, e) : t).trim();
}
// Kl. 7–10: „Kurz gesagt“ zusätzlich als erste Zeile in der Karte (Schalter je Kind und Gerät, Standard aus – Entscheidung von Sebastian offen).
function lernKurzOben(kind) {
  if (!kind?.klasse || kind.klasse < 7) return false;
  try { return localStorage.getItem('lern.kurzoben.' + kind.id) === '1'; } catch { return false; }
}
// Thermometer (senkrechter Zahlenstrahl): start, ende, schritt (Beschriftung), stand, bereich_unter_null, einheit, name
function lernThermometer(b) {
  const lo = b.start ?? -10, hi = b.ende ?? 10, B = 200, H = 300, O = 26, U = 56, X = 86;
  const py = (v) => H - U - (H - U - O) * (v - lo) / ((hi - lo) || 1);
  const { svg, mk } = lernSvg(B, H, b.label || `Thermometer von ${lo} bis ${hi}${b.stand !== undefined ? ', Stand ' + b.stand : ''}`);
  svg.classList.add('lern-thermo');
  if (b.bereich_unter_null && lo < 0) mk('rect', { x: X - 34, y: py(0), width: 120, height: py(lo) - py(0), class: 'kalt' });
  mk('rect', { x: X - 9, y: O - 10, width: 18, height: H - U - O + 22, rx: 9, class: 'rohr' });
  mk('circle', { cx: X, cy: H - U + 22, r: 17, class: 'kugel' });
  if (b.stand !== undefined && b.stand !== null) mk('rect', { x: X - 5, y: py(b.stand), width: 10, height: H - U + 14 - py(b.stand), class: 'saeule-rot' });
  const roh = (hi - lo) / 8; const p = 10 ** Math.floor(Math.log10(roh)); const sy = b.schritt || [1, 2, 5, 10].map((m) => m * p).find((m) => m >= roh);
  for (let v = Math.ceil(lo / sy) * sy; v <= hi + 1e-9; v += sy) { mk('line', { x1: X + 9, y1: py(v), x2: X + (v === 0 ? 30 : 20), y2: py(v), class: v === 0 ? 'achse' : 'strich' }); mk('text', { x: X + 34, y: py(v) + 6, class: 'zahl links' + (v === 0 ? ' fett' : '') }, lernZahlText(v) + (b.einheit ? ' ' + b.einheit : '')); }
  if (b.stand !== undefined && b.stand !== null) { const nz = b._neu?.stand ? ' neu' : ''; mk('path', { d: `M${X - 12} ${py(b.stand)} l-12 -6 v12 z`, class: 'pfeil' + nz }); mk('text', { x: X - 28, y: py(b.stand) + 6, class: 'zahl rechts fett' + (nz ? ' neu-text' : '') }, b.name || lernZahlText(b.stand) + (b.einheit ? ' ' + b.einheit : '')); }
  return svg;
}
// Bruchstreifen: teile, gefaerbt, ganzes (Text unter dem ganzen Streifen), teil_text (Text über dem gefärbten Teil), zeilen: weitere Streifen [{teile, gefaerbt, teil_text}]
function lernBruchstreifen(b) {
  const zeilen = [b, ...(b.zeilen || [])]; const B = 340, L = 14, zh = 78, H = zeilen.length * zh + (b.ganzes ? 30 : 4);
  const { svg, mk } = lernSvg(B, H, b.label || zeilen.map((z) => `Streifen mit ${z.teile} gleichen Teilen, ${z.gefaerbt ?? 0} gefärbt`).join('; '));
  zeilen.forEach((z, k) => { const n = Math.max(1, z.teile || 1), g = Math.min(n, z.gefaerbt ?? 0), w = (B - 2 * L) / n, y = k * zh + 30;
    for (let i = 0; i < n; i++) mk('rect', { x: L + i * w, y, width: w, height: 40, class: 'streifen' + (i < g ? ' voll' : '') });
    if (z.teil_text && g) { const m = L + g * w / 2; mk('text', { x: Math.min(B - lernBreite(z.teil_text) / 2 - 2, Math.max(lernBreite(z.teil_text) / 2 + 2, m)), y: y - 9, class: 'zahl fett' }, z.teil_text); } });
  if (b.ganzes) { const y = zeilen.length * zh + 2; mk('path', { d: `M${L} ${y - 6} v6 h${B - 2 * L} v-6`, class: 'klammer' }); mk('text', { x: B / 2, y: y + 22, class: 'zahl' }, b.ganzes); }
  return svg;
}
function lernStellentafel(b) {
  return el('table', { class: 'lr-stellentafel', 'aria-label': 'Stellenwerttafel' },
    el('tr', {}, ...(b.stellen || []).map((s) => el('th', {}, s))),
    el('tr', {}, ...(b.ziffern || []).map((z, i) => el('td', { class: (i === b.markiert ? 'on' : '') + (b._neu?.ziffern?.has(i) ? ' neu' : '') }, z))));
}
function lernBild(b) {
  if (!b) return null;
  if (b.typ === 'zahlenstrahl') return el('div', { class: 'lr-bild' }, lernZahlenstrahl(b, false));
  if (b.typ === 'stellentafel') return el('div', { class: 'lr-bild' }, lernStellentafel(b));
  if (b.typ === 'koordinaten') return el('div', { class: 'lr-bild' }, lernKoordinaten(b));
  if (b.typ === 'figur') return el('div', { class: 'lr-bild' }, lernFigur(b));
  if (b.typ === 'saeulen') return el('div', { class: 'lr-bild' }, lernSaeulen(b));
  if (b.typ === 'kreisdiagramm') return el('div', { class: 'lr-bild' }, lernKreisdiagramm(b));
  if (b.typ === 'tabelle') return el('div', { class: 'lr-bild lr-bild-tabelle' }, lernTabelle(b));
  if (b.typ === 'boxplot') return el('div', { class: 'lr-bild' }, lernBoxplot(b));
  if (b.typ === 'baum') return el('div', { class: 'lr-bild' }, lernBaum(b));
  if (b.typ === 'thermometer') return el('div', { class: 'lr-bild' }, lernThermometer(b));
  if (b.typ === 'bruchstreifen') return el('div', { class: 'lr-bild' }, lernBruchstreifen(b));
  return null;
}

// ---------- Zeichnungen (W150): Koordinatensystem mit Graphen, Figuren, Diagramme, Tabellen ----------
const LERN_SVG = 'http://www.w3.org/2000/svg';
// Schrift in Zeichnungen ist seit 16.11. mindestens 16 px groß – Beschriftungen brauchen Platz. Geschätzte Breite eines Textes in Zeichen-Einheiten:
const lernBreite = (t) => String(t ?? '').length * 9.6 + 4;
function lernSvg(b, h, label) {
  const svg = document.createElementNS(LERN_SVG, 'svg');
  svg.setAttribute('viewBox', `0 0 ${b} ${h}`); svg.setAttribute('class', 'lern-zeichnung'); svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', label);
  const mk = (tag, a, txt) => { const e = document.createElementNS(LERN_SVG, tag); for (const [k, v] of Object.entries(a)) e.setAttribute(k, v); if (txt !== undefined) e.textContent = txt; svg.append(e); return e; };
  return { svg, mk };
}
// Funktionswert für einen Graphen. Arten: linear (m, t) · poly (k = [c0, c1, c2 …]) · hyperbel (a/(x+b)+c) · potenz (a·x^n) · wurzel (a·√x) · sin/cos (a·sin(b·x°)+d bzw. Bogenmaß mit bogen: true) · exp (a·b^x) · log (Basis b)
function lernGraphWert(g, x) {
  const a = g.a ?? 1;
  switch (g.art) {
    case 'linear': return (g.m ?? 1) * x + (g.t ?? 0);
    case 'poly': return (g.k || []).reduce((sum, c, i) => sum + c * x ** i, 0);
    case 'hyperbel': return x + (g.b ?? 0) === 0 ? NaN : a / (x + (g.b ?? 0)) + (g.c ?? 0);
    case 'potenz': return (g.n ?? 2) < 0 && x === 0 ? NaN : a * x ** (g.n ?? 2);
    case 'wurzel': return x < 0 ? NaN : a * Math.sqrt(x);
    case 'sin': return a * Math.sin((g.b ?? 1) * (g.bogen ? x : x * Math.PI / 180) + (g.c ?? 0)) + (g.d ?? 0);
    case 'cos': return a * Math.cos((g.b ?? 1) * (g.bogen ? x : x * Math.PI / 180) + (g.c ?? 0)) + (g.d ?? 0);
    case 'exp': return a * (g.b ?? 2) ** x + (g.c ?? 0);
    case 'log': return x <= 0 ? NaN : Math.log(x) / Math.log(g.b ?? 10);
    case 'tan': { const w = (g.b ?? 1) * (g.bogen ? x : x * Math.PI / 180) + (g.c ?? 0); return Math.abs(Math.cos(w)) < 1e-9 ? NaN : a * Math.tan(w) + (g.d ?? 0); }
    case 'betrag': return a * Math.abs(x - (g.b ?? 0)) + (g.c ?? 0);
    case 'glocke': return a * Math.exp(-((x - (g.mu ?? 0)) ** 2) / (2 * (g.sigma ?? 1) ** 2));
    default: return NaN;
  }
}
function lernKoordinaten(b) {
  let [x0, x1] = b.x || [-5, 5], [y0, y1] = b.y || [-5, 5];
  // Reine Geometrie (ohne Graphen): gleicher Maßstab auf beiden Achsen, sonst werden Kreise und rechte Winkel verzerrt.
  if (!(b.graphen || []).length && !b.streckung) {
    const v = (y1 - y0) / (x1 - x0);
    if (v > 1 && v <= 4) { const m = (x0 + x1) / 2, h = (y1 - y0) / 2; x0 = m - h; x1 = m + h; }
    else if (v < 1 && v >= 0.25) { const m = (y0 + y1) / 2, h = (x1 - x0) / 2; y0 = m - h; y1 = m + h; }
  }
  const B = 340, R = 38; const geo = !(b.graphen || []).length && !b.streckung;
  // Reine Geometrie: gleiche Pixel je Einheit auf beiden Achsen (Kreise bleiben rund).
  const H = geo ? Math.round(Math.min(420, Math.max(150, 2 * R + (B - 2 * R) * (y1 - y0) / (x1 - x0)))) : Math.round(Math.min(340, Math.max(170, 300 * (y1 - y0) / (x1 - x0) * (b.streckung || 1))));
  const px = (x) => R + (B - 2 * R) * (x - x0) / (x1 - x0), py = (y) => H - R - (H - 2 * R) * (y - y0) / (y1 - y0);
  const { svg, mk } = lernSvg(B, H, b.label || `Koordinatensystem von x = ${x0} bis ${x1} und y = ${y0} bis ${y1}`);
  const schritt = (lo, hi) => { const r = (hi - lo) / 10; const p = 10 ** Math.floor(Math.log10(r)); return [1, 2, 5, 10].map((m) => m * p).find((m) => m >= r) || p * 10; };
  const sx = b.schritt_x || (b.pi ? Math.PI / 2 : schritt(x0, x1)), sy = b.schritt_y || schritt(y0, y1);
  const zahl = (v) => lernZahlText(v);
  // pi: true → x-Achse in Vielfachen von π beschriften (½π, π, 3π/2 …)
  const piText = (v) => { const k = Math.round(v / (Math.PI / 2)); const m = k < 0 ? '−' : ''; const n = Math.abs(k); return n % 2 === 0 ? m + (n === 2 ? '' : n / 2) + 'π' : m + (n === 1 ? '' : n) + 'π/2'; };
  for (const f of b.flaechen || []) mk('polygon', { points: (f.punkte || []).map(([x, y]) => `${px(Math.min(Math.max(x, x0), x1)).toFixed(1)},${py(Math.min(Math.max(y, y0), y1)).toFixed(1)}`).join(' '), class: 'flaeche' + lernNeu1(b, 'flaechen', f) });
  for (let x = Math.ceil(x0 / sx) * sx; x <= x1 + 1e-9; x += sx) mk('line', { x1: px(x), y1: py(y0), x2: px(x), y2: py(y1), class: 'gitter' });
  for (let y = Math.ceil(y0 / sy) * sy; y <= y1 + 1e-9; y += sy) mk('line', { x1: px(x0), y1: py(y), x2: px(x1), y2: py(y), class: 'gitter' });
  const ax = Math.min(Math.max(0, y0), y1), ay = Math.min(Math.max(0, x0), x1); // Achsen am Rand, wenn 0 außerhalb liegt
  mk('line', { x1: px(x0) - 6, y1: py(ax), x2: px(x1) + 10, y2: py(ax), class: 'achse' }); mk('path', { d: `M${px(x1) + 14} ${py(ax)} l-8 -4 v8 z`, class: 'spitze' });
  mk('line', { x1: px(ay), y1: py(y0) + 6, x2: px(ay), y2: py(y1) - 10, class: 'achse' }); mk('path', { d: `M${px(ay)} ${py(y1) - 14} l-4 8 h8 z`, class: 'spitze' });
  mk('text', { x: px(x1) + 14, y: py(ax) + 19, class: 'zahl kursiv' }, b.name_x || 'x'); mk('text', { x: px(ay) + 13, y: py(y1) - 8, class: 'zahl kursiv' }, b.name_y || 'y');
  const jeder = (n) => Math.max(1, Math.ceil(n / 8));
  const nx = jeder((x1 - x0) / sx), ny = jeder((y1 - y0) / sy);
  { let rechts = -1e9; const ende = px(x1) - 2; // x-Beschriftung: überspringen, was in die vorige oder in den Achsennamen ragt
    for (let i = Math.ceil(x0 / sx); i * sx <= x1 + 1e-9; i++) { if (i === 0 || i % nx) continue; const t = b.pi ? piText(i * sx) : zahl(i * sx) + (b.grad ? '°' : ''); const w = lernBreite(t), x = px(i * sx);
      if (x - w / 2 < rechts + 3 || x + w / 2 > ende) continue; mk('text', { x, y: py(ax) + 19, class: 'zahl' }, t); rechts = x + w / 2; } }
  { let unten = 1e9; // y-Beschriftung: mindestens eine Schrifthöhe Abstand
    for (let i = Math.ceil(y0 / sy); i * sy <= y1 + 1e-9; i++) { if (i === 0 || i % ny) continue; const y = py(i * sy); if (unten - y < 19 || y < py(y1) + 12) continue; mk('text', { x: px(ay) - 6, y: y + 6, class: 'zahl rechts' }, zahl(i * sy)); unten = y; } }
  for (const v of b.senkrecht || []) mk('line', { x1: px(v), y1: py(y0), x2: px(v), y2: py(y1), class: 'hilfslinie' + lernNeu1(b, 'senkrecht', v) });
  for (const v of b.waagrecht || []) mk('line', { x1: px(x0), y1: py(v), x2: px(x1), y2: py(v), class: 'hilfslinie' + lernNeu1(b, 'waagrecht', v) });
  (b.graphen || []).forEach((g, gi) => {
    let d = '', offen = false, yVor = null;
    const [gx0, gx1] = g.bereich || [x0, x1];
    for (let i = 0; i <= 400; i++) {
      const x = gx0 + (gx1 - gx0) * i / 400; const y = lernGraphWert(g, x);
      if (!Number.isFinite(y) || y < y0 - (y1 - y0) || y > y1 + (y1 - y0)) { offen = false; yVor = null; continue; }
      if (yVor !== null && Math.abs(y - yVor) > (y1 - y0)) offen = false; // Sprung an einer Polstelle (tan, Hyperbel): nicht verbinden
      d += `${offen ? 'L' : 'M'}${px(x).toFixed(1)} ${py(y).toFixed(1)}`; offen = true; yVor = y;
    }
    const clip = `lk${Math.random().toString(36).slice(2, 8)}`;
    const cp = mk('clipPath', { id: clip }); const r = document.createElementNS(LERN_SVG, 'rect');
    for (const [k, v] of Object.entries({ x: px(x0), y: py(y1), width: px(x1) - px(x0), height: py(y0) - py(y1) })) r.setAttribute(k, v); cp.append(r);
    mk('path', { d, class: 'graph graph' + (gi % 3) + lernNeu1(b, 'graphen', g), 'clip-path': `url(#${clip})` });
    if (g.name) { const xn = g.name_x ?? (x1 - (x1 - x0) * 0.12); const yn = lernGraphWert(g, xn); if (Number.isFinite(yn) && yn > y0 && yn < y1) mk('text', { x: px(xn) + 4, y: py(yn) - 6, class: 'zahl kursiv graphname' + (gi % 3) }, g.name); }
  });
  for (const st of b.strecken || []) mk('line', { x1: px(st[0]), y1: py(st[1]), x2: px(st[2]), y2: py(st[3]), class: (st[4] === 'gestrichelt' ? 'hilfslinie' : 'strecke') + lernNeu1(b, 'strecken', st) });
  for (const k of b.kreise || []) { const m = k.m || [0, 0]; mk('ellipse', { cx: px(m[0]), cy: py(m[1]), rx: Math.abs(px(m[0] + k.r) - px(m[0])), ry: Math.abs(py(m[1] + k.r) - py(m[1])), class: 'graph graph' + ((k.farbe ?? 1) % 3) + lernNeu1(b, 'kreise', k) }); if (k.name) mk('text', { x: px(m[0] + k.r * 0.71) + 6, y: py(m[1] + k.r * 0.71) - 4, class: 'zahl links kursiv' }, k.name); }
  for (const v of b.pfeile || []) { // Vektorpfeil [x1, y1, x2, y2, name]
    const [ax1, ay1, ax2, ay2] = [px(v[0]), py(v[1]), px(v[2]), py(v[3])]; const L = Math.hypot(ax2 - ax1, ay2 - ay1) || 1; const ux = (ax2 - ax1) / L, uy = (ay2 - ay1) / L;
    mk('line', { x1: ax1, y1: ay1, x2: ax2 - ux * 6, y2: ay2 - uy * 6, class: 'strecke' + lernNeu1(b, 'pfeile', v) });
    mk('path', { d: `M${ax2.toFixed(1)} ${ay2.toFixed(1)} L${(ax2 - ux * 10 - uy * 4.5).toFixed(1)} ${(ay2 - uy * 10 + ux * 4.5).toFixed(1)} L${(ax2 - ux * 10 + uy * 4.5).toFixed(1)} ${(ay2 - uy * 10 - ux * 4.5).toFixed(1)} z`, class: 'spitze' });
    if (v[4]) mk('text', { x: (ax1 + ax2) / 2 - uy * 12, y: (ay1 + ay2) / 2 + ux * 12 + 4, class: 'zahl kursiv' }, v[4]);
  }
  for (const p of b.punkte || []) { const nz = lernNeu1(b, 'punkte', p); mk('circle', { cx: px(p.x), cy: py(p.y), r: nz ? 6.5 : 4, class: (p.offen ? 'punkt offen' : 'punkt') + nz }); if (p.name) mk('text', { x: px(p.x) + 8, y: py(p.y) - 8, class: 'zahl links' + (nz ? ' fett neu-text' : '') }, p.name); }
  return svg;
}
// Figur aus benannten Punkten: linien [[A, B, 'c = 4 cm']], flaeche ['A','B','C'], rechter_winkel [[Scheitel, Schenkel1, Schenkel2]], winkel [[Scheitel, S1, S2, 'α']], kreise [{m: 'M'|[x,y], r, name}]
function lernFigur(b) {
  const P = b.punkte || {}; const pk = (k) => (Array.isArray(k) ? k : P[k]);
  const alle = [...Object.values(P), ...(b.kreise || []).flatMap((k) => { const m = pk(k.m); return [[m[0] - k.r, m[1] - k.r], [m[0] + k.r, m[1] + k.r]]; })];
  const xs = alle.map((p) => p[0]), ys = alle.map((p) => p[1]);
  const xa = Math.min(...xs), xb = Math.max(...xs), ya = Math.min(...ys), yb = Math.max(...ys);
  const B = 340, R = 38, RX = 72, f = Math.min((B - 2 * RX) / Math.max(xb - xa, 1e-9), 220 / Math.max(yb - ya, 1e-9)), H = Math.round((yb - ya) * f + 2 * R);
  const ox = (B - (xb - xa) * f) / 2; const px = (x) => ox + (x - xa) * f, py = (y) => H - R - (y - ya) * f;
  const mitte = [(xa + xb) / 2, (ya + yb) / 2];
  const { svg, mk } = lernSvg(B, H, b.label || 'Skizze');
  if (b.flaeche) mk('polygon', { points: b.flaeche.map((k) => `${px(pk(k)[0])},${py(pk(k)[1])}`).join(' '), class: 'flaeche' + (b._neu?.flaeche ? ' neu' : '') });
  for (const k of b.kreise || []) { const m = pk(k.m); mk('circle', { cx: px(m[0]), cy: py(m[1]), r: k.r * f, class: 'kreis' + lernNeu1(b, 'kreise', k) }); if (k.name) mk('text', { x: px(m[0] + k.r * 0.72) + 6, y: py(m[1] + k.r * 0.72) - 4, class: 'zahl links' }, k.name); }
  for (const lin of b.linien || []) {
    const [u, v, text, art] = lin; const a = pk(u), c = pk(v);
    mk('line', { x1: px(a[0]), y1: py(a[1]), x2: px(c[0]), y2: py(c[1]), class: (art === 'gestrichelt' ? 'hilfslinie' : 'strecke') + lernNeu1(b, 'linien', lin) });
    if (text) {
      const m = [(a[0] + c[0]) / 2, (a[1] + c[1]) / 2]; let n = [-(c[1] - a[1]), c[0] - a[0]]; const l = Math.hypot(...n) || 1; n = [n[0] / l, n[1] / l];
      if ((m[0] - mitte[0]) * n[0] + (m[1] - mitte[1]) * n[1] < 0) n = [-n[0], -n[1]]; // Beschriftung nach außen
      mk('text', { x: px(m[0]) + n[0] * (Math.abs(n[0]) > 0.5 ? 9 : 16), y: py(m[1]) - n[1] * 16 + 4, class: 'zahl' + (n[0] > 0.5 ? ' links' : n[0] < -0.5 ? ' rechts' : '') }, text);
    }
  }
  const richtung = (s, q) => { const a = pk(s), c = pk(q); const l = Math.hypot(c[0] - a[0], c[1] - a[1]) || 1; return [(c[0] - a[0]) / l, (c[1] - a[1]) / l]; };
  for (const rw of b.rechter_winkel || []) {
    const [s, q1, q2] = rw; const a = pk(s), u = richtung(s, q1), v = richtung(s, q2), d = 13;
    mk('path', { d: `M${px(a[0]) + u[0] * d} ${py(a[1]) - u[1] * d} l${v[0] * d} ${-v[1] * d} l${-u[0] * d} ${u[1] * d}`, class: 'winkel' + lernNeu1(b, 'rechter_winkel', rw) });
    mk('circle', { cx: px(a[0]) + (u[0] + v[0]) * d / 2, cy: py(a[1]) - (u[1] + v[1]) * d / 2, r: 1.6, class: 'punkt' });
  }
  for (const wk of b.winkel || []) {
    const [s, q1, q2, text] = wk; const a = pk(s), u = richtung(s, q1), v = richtung(s, q2), d = 22;
    const kreuz = u[0] * v[1] - u[1] * v[0];
    mk('path', { d: `M${px(a[0]) + u[0] * d} ${py(a[1]) - u[1] * d} A${d} ${d} 0 0 ${kreuz > 0 ? 0 : 1} ${px(a[0]) + v[0] * d} ${py(a[1]) - v[1] * d}`, class: 'winkel' + lernNeu1(b, 'winkel', wk) });
    const w = [u[0] + v[0], u[1] + v[1]]; const l = Math.hypot(...w) || 1;
    if (text) mk('text', { x: px(a[0]) + w[0] / l * (d + 13), y: py(a[1]) - w[1] / l * (d + 13) + 4, class: 'zahl' }, text);
  }
  for (const [name, p] of Object.entries(P)) {
    if (name.startsWith('_')) continue; // Hilfspunkte ohne Beschriftung
    let n = [p[0] - mitte[0], p[1] - mitte[1]]; const l = Math.hypot(...n) || 1; n = [n[0] / l, n[1] / l];
    const nz = b._neu?.punktnamen?.has(name) ? ' neu' : '';
    mk('circle', { cx: px(p[0]), cy: py(p[1]), r: nz ? 5 : 2.5, class: 'punkt' + nz });
    mk('text', { x: px(p[0]) + n[0] * 15, y: py(p[1]) - n[1] * 15 + 4, class: 'zahl fett' + (nz ? ' neu-text' : '') }, name);
  }
  return svg;
}
function lernSaeulen(b) {
  const w = b.werte || []; const B = 340, L = 44; const zweizeilig = w.some((x) => lernBreite(x.name) > (B - L - 16) / Math.max(w.length, 1)); const U = zweizeilig ? 64 : 46, H = zweizeilig ? 256 : 238;
  const y0 = b.y_start ?? 0, max = b.y_max ?? Math.max(...w.map((x) => x.wert), 1);
  const roh = (max - y0) / 5; const p = 10 ** Math.floor(Math.log10(roh)); const sy = b.schritt || [1, 2, 5, 10].map((m) => m * p).find((m) => m >= roh);
  const oben = Math.ceil(max / sy) * sy; const py = (v) => H - U - (H - U - 34) * (v - y0) / (oben - y0);
  const { svg, mk } = lernSvg(B, H, b.label || `Säulendiagramm: ${w.map((x) => `${x.name} ${x.wert}`).join(', ')}`);
  for (let v = y0; v <= oben + 1e-9; v += sy) { mk('line', { x1: L, y1: py(v), x2: B - 8, y2: py(v), class: 'gitter' }); mk('text', { x: L - 5, y: py(v) + 6, class: 'zahl rechts' }, lernZahlText(v)); }
  const bw = (B - L - 16) / Math.max(w.length, 1);
  w.forEach((x, i) => {
    mk('rect', { x: L + 8 + i * bw + bw * 0.15, y: py(x.wert), width: bw * 0.7, height: py(y0) - py(x.wert), class: 'saeule saeule' + (i % 4) });
    mk('text', { x: L + 8 + i * bw + bw / 2, y: H - U + 20 + (zweizeilig && i % 2 ? 20 : 0), class: 'zahl' }, x.name);
    if (b.zahlen !== false) mk('text', { x: L + 8 + i * bw + bw / 2, y: py(x.wert) - 4, class: 'zahl fett' }, lernZahlText(x.wert));
  });
  mk('line', { x1: L, y1: py(y0), x2: B - 8, y2: py(y0), class: 'achse' });
  if (y0 > 0) mk('path', { d: `M${L - 6} ${py(y0) - 10} l12 -5 l-12 -5 l12 -5`, class: 'winkel' }); // Achse ist abgeschnitten
  if (b.einheit) mk('text', { x: 4, y: 15, class: 'zahl links' }, b.einheit);
  return svg;
}
function lernKreisdiagramm(b) {
  const w = b.werte || []; const sum = w.reduce((a, x) => a + x.wert, 0) || 1; const B = 340, H = 220, cx = 110, cy = 110, r = 92;
  const { svg, mk } = lernSvg(B, H, b.label || `Kreisdiagramm: ${w.map((x) => `${x.name} ${x.wert}`).join(', ')}`);
  let a0 = -Math.PI / 2;
  w.forEach((x, i) => {
    const a1 = a0 + 2 * Math.PI * x.wert / sum; const gross = a1 - a0 > Math.PI ? 1 : 0;
    mk('path', { d: `M${cx} ${cy} L${cx + r * Math.cos(a0)} ${cy + r * Math.sin(a0)} A${r} ${r} 0 ${gross} 1 ${cx + r * Math.cos(a1)} ${cy + r * Math.sin(a1)} Z`, class: 'saeule sektor saeule' + (i % 4) });
    mk('rect', { x: 222, y: 24 + i * 24, width: 14, height: 14, class: 'saeule saeule' + (i % 4) });
    mk('text', { x: 242, y: 36 + i * 24, class: 'zahl links' }, x.name + (b.zahlen === false ? '' : ` (${lernZahlText(x.wert)}${b.einheit || ''})`));
    a0 = a1;
  });
  return svg;
}
// Boxplot: reihen [{name, min, q1, median, q3, max}] über einer gemeinsamen Achse [lo, hi]
function lernBoxplot(b) {
  const reihen = b.reihen || [b]; const B = 340, L = reihen.some((r) => r.name) ? Math.min(120, Math.max(64, ...reihen.map((r) => lernBreite(r.name) + 8))) : 22, R = 22, zh = 46, H = reihen.length * zh + 50;
  const lo = b.achse?.[0] ?? Math.min(...reihen.map((r) => r.min)), hi = b.achse?.[1] ?? Math.max(...reihen.map((r) => r.max));
  const px = (v) => L + (B - L - R) * (v - lo) / (hi - lo);
  const { svg, mk } = lernSvg(B, H, b.label || 'Boxplot: ' + reihen.map((r) => `${r.name || ''} Minimum ${r.min}, unteres Quartil ${r.q1}, Median ${r.median}, oberes Quartil ${r.q3}, Maximum ${r.max}`).join('; '));
  const roh = (hi - lo) / 8; const p = 10 ** Math.floor(Math.log10(roh)); const sx = b.schritt || [1, 2, 5, 10].map((m) => m * p).find((m) => m >= roh);
  const ya = H - 30;
  mk('line', { x1: L - 6, y1: ya, x2: B - R + 6, y2: ya, class: 'achse' });
  { let rechts = b.einheit ? 4 + lernBreite(b.einheit) : -1e9;
    for (let v = Math.ceil(lo / sx) * sx; v <= hi + 1e-9; v += sx) { mk('line', { x1: px(v), y1: ya - 4, x2: px(v), y2: ya + 4, class: 'achse' }); const t = lernZahlText(v), w = lernBreite(t); if (px(v) - w / 2 < rechts + 3) continue; mk('text', { x: px(v), y: ya + 22, class: 'zahl' }, t); rechts = px(v) + w / 2; } }
  if (b.einheit) mk('text', { x: 4, y: ya + 22, class: 'zahl links' }, b.einheit);
  reihen.forEach((r, i) => {
    const y = 10 + i * zh, h = 26, m = y + h / 2;
    if (r.name) mk('text', { x: 4, y: m + 6, class: 'zahl links' }, r.name);
    mk('line', { x1: px(r.min), y1: m, x2: px(r.q1), y2: m, class: 'strecke' }); mk('line', { x1: px(r.q3), y1: m, x2: px(r.max), y2: m, class: 'strecke' });
    mk('line', { x1: px(r.min), y1: m - 8, x2: px(r.min), y2: m + 8, class: 'strecke' }); mk('line', { x1: px(r.max), y1: m - 8, x2: px(r.max), y2: m + 8, class: 'strecke' });
    mk('rect', { x: px(r.q1), y, width: px(r.q3) - px(r.q1), height: h, class: 'box box' + (i % 3) });
    mk('line', { x1: px(r.median), y1: y, x2: px(r.median), y2: y + h, class: 'strecke median' });
  });
  return svg;
}
// Baumdiagramm: aeste [{text: 'rot', p: '3/5', aeste: [...]}], bis zu drei Stufen
function lernBaum(b) {
  const blaetter = []; let tiefe = 0;
  const lauf = (k, t) => { tiefe = Math.max(tiefe, t); if (!(k.aeste || []).length) { k._x = blaetter.length; blaetter.push(k); } else { k.aeste.forEach((c) => lauf(c, t + 1)); k._x = (k.aeste[0]._x + k.aeste[k.aeste.length - 1]._x) / 2; } k._t = t; };
  const wurzel = { aeste: JSON.parse(JSON.stringify(b.aeste || [])) }; lauf(wurzel, 0);
  const B = 340, n = Math.max(blaetter.length, 1), sh = tiefe > 2 ? 66 : 78, H = 26 + tiefe * sh + 40;
  const rand = Math.min(70, Math.max(24, ...blaetter.map((k) => lernBreite(k.text) / 2 + 2)));
  const eng = n > 1 && blaetter.some((k) => lernBreite(k.text) > (B - 2 * rand) / (n - 1) - 4); // Blatt-Beschriftungen abwechselnd tiefer setzen
  const px = (x) => rand + (B - 2 * rand) * (n === 1 ? 0.5 : x / (n - 1)), py = (t) => 14 + t * sh;
  const { svg, mk } = lernSvg(B, H, b.label || 'Baumdiagramm');
  const zeichne = (k) => {
    for (const c of k.aeste || []) {
      mk('line', { x1: px(k._x), y1: py(k._t) + (k._t ? 8 : 0), x2: px(c._x), y2: py(c._t) - 14, class: 'strecke duenn' });
      if (c.p) { const links = c._x <= k._x; mk('text', { x: (px(k._x) + px(c._x)) / 2 + (links ? -5 : 5), y: (py(k._t) + py(c._t)) / 2 + 1, class: 'zahl klein ' + (links ? 'rechts' : 'links') }, c.p); }
      mk('text', { x: px(c._x), y: py(c._t) + 6 + (eng && !(c.aeste || []).length && blaetter.indexOf(c) % 2 ? 20 : 0), class: 'zahl fett' }, c.text || '');
      zeichne(c);
    }
  };
  mk('circle', { cx: px(wurzel._x), cy: py(0), r: 3, class: 'punkt' });
  zeichne(wurzel);
  return svg;
}
function lernTabelle(b) {
  return el('table', { class: 'lr-tafel' },
    b.kopf ? el('thead', {}, el('tr', {}, ...b.kopf.map((k) => el('th', {}, lernText(k))))) : null,
    el('tbody', {}, ...(b.zeilen || []).map((z, r) => el('tr', {}, ...z.map((c, i) => el(i === 0 && b.erste_spalte_kopf !== false ? 'th' : 'td', b._neu?.zellen?.has(`${r},${i}`) ? { class: 'neu' } : {}, lernText(c)))))));
}
// Erklärung einer Etappe: Regel, vorgerechnetes Beispiel Schritt für Schritt, Probe, typischer Fehler.
function lernSchrittBild(zustand, b) {
  if (!b) return zustand;
  if (!zustand || (b.typ && b.typ !== zustand.typ)) return b;
  return { ...zustand, ...b };
}
// N1: Was gegenüber dem zuletzt gezeigten Bild neu ist, wird markiert (b._neu) und in der Akzentfarbe kräftig gezeichnet.
const LERN_NEU_LISTEN = ['punkte', 'strecken', 'kreise', 'pfeile', 'graphen', 'flaechen', 'senkrecht', 'waagrecht', 'linien', 'winkel', 'rechter_winkel', 'boegen'];
function lernNeuMarkieren(vorher, b) {
  if (!b || !vorher || (vorher.typ || null) !== (b.typ || null)) return b;
  const j = (x) => JSON.stringify(x); const neu = {};
  for (const f of LERN_NEU_LISTEN) {
    if (!Array.isArray(b[f])) continue;
    const alt = new Set((Array.isArray(vorher[f]) ? vorher[f] : []).map(j));
    const n = new Set(b[f].map(j).filter((x) => !alt.has(x))); if (n.size) neu[f] = n;
  }
  if (b.punkte && !Array.isArray(b.punkte)) { // Figur: Punkte als {Name: [x, y]}
    const alt = vorher.punkte && !Array.isArray(vorher.punkte) ? vorher.punkte : {};
    const n = new Set(Object.keys(b.punkte).filter((k) => j(alt[k]) !== j(b.punkte[k]))); if (n.size) neu.punktnamen = n;
  }
  if (j(b.flaeche) !== j(vorher.flaeche) && b.flaeche) neu.flaeche = true;
  for (const f of ['stand', 'pfeil', 'markiert', 'gefaerbt']) if (b[f] !== undefined && b[f] !== null && j(b[f]) !== j(vorher[f])) neu[f] = true;
  // A2: Tabelle und Stellentafel – geänderte Zellen hervorheben (neuer Wert oder neu markiert)
  if (b.typ === 'tabelle' && Array.isArray(b.zeilen)) {
    const z = new Set(); b.zeilen.forEach((r, i) => (r || []).forEach((c, k) => { if (j(c) !== j(vorher.zeilen?.[i]?.[k])) z.add(`${i},${k}`); }));
    if (z.size && z.size < b.zeilen.flat().length) neu.zellen = z;
  }
  if (b.typ === 'stellentafel') {
    const z = new Set((b.ziffern || []).map((c, k) => (j(c) !== j(vorher.ziffern?.[k]) ? k : null)).filter((k) => k !== null));
    if (b.markiert !== undefined && b.markiert !== null && b.markiert !== vorher.markiert) z.add(b.markiert);
    if (z.size) neu.ziffern = z;
  }
  return Object.keys(neu).length ? { ...b, _neu: neu } : b;
}
// Bild mit Neuem: der Rest tritt zurück (CSS .mit-neu), damit das Neue auffällt – auch wenn es dieselbe Farbe hat wie der Graph.
const lernBildNeu = (b) => { const k = lernBild(b); const svg = k?.querySelector('svg'); if (svg?.querySelector('.neu')) svg.classList.add('mit-neu'); return k; }; // A2: nur, wenn wirklich ein Element neu ist
const lernNeu1 = (b, f, x) => (b?._neu?.[f]?.has?.(JSON.stringify(x)) ? ' neu' : '');
// Vergleich zweier gezeichneter Bilder (ohne zufällige IDs): gleich → nicht noch einmal zeigen.
const lernBildText = (knoten) => (knoten ? knoten.outerHTML.replace(/lk[a-z0-9]{3,8}/g, '') : '');
// Eine Anzeige für alle Karten (Vorgabe 16.11.): [Kurz gesagt] → Worum geht's? → Bild → Beispiel als Bildergeschichte → „Pass auf!“ → MERKE → Wörterliste.
// Karten ohne einstieg beginnen beim Bild. Schritte sind Texte oder {text, bild}; ein Schrittbild ergänzt das Kartenbild.
function lernErklaerung(e, { kurz = false, kurzGesagt = false } = {}) {
  const wctx = { liste: lernWortListe(e.woerter), gesehen: new Set() };
  const M = (t) => lernMarkiert(t, wctx);
  const einstieg = e.einstieg ? el('div', { class: 'lr-einstieg' }, el('p', { class: 'lr-ueber' }, 'WORUM GEHT’S?'), el('p', {}, ...M(e.einstieg))) : null;
  const schritte = (e.schritte || []).map((x) => (typeof x === 'string' ? { text: x } : x || {}));
  const mitBildern = schritte.some((x) => x.bild);
  let zustand = e.bild || null;
  // N1: Ein Schrittbild nur zeigen, wenn es sich gegenüber dem zuletzt gezeigten Bild (auch dem Einstiegsbild) ändert; sonst nur der Text.
  let gezeigt = e.bild || null, gezeigtText = lernBildText(lernBild(e.bild));
  const li = schritte.map((x) => {
    let bild = null;
    if (mitBildern) {
      zustand = lernSchrittBild(zustand, x.bild);
      const z = zustand; // A2: so gezeichnet, wie es im Inhalt steht (Steigungsdreieck nicht vergrößern)
      const t = z ? lernBildText(lernBild(z)) : ''; // Vergleich ohne Markierung
      if (t && t !== gezeigtText) { bild = lernBildNeu(lernNeuMarkieren(gezeigt, z)); gezeigt = z; gezeigtText = t; }
    }
    return el('li', { class: 'lr-schritt' + (bild ? ' mit-bild' : '') }, bild, el('span', { class: 'lr-schritt-text' }, ...M(x.text)));
  });
  const passauf = e.fehler && !kurz ? el('div', { class: 'lr-fehler lr-passauf' + (e.fehler_bild ? ' mit-bild' : '') },
    e.fehler_bild ? lernBildNeu(lernNeuMarkieren(zustand, lernSchrittBild(zustand, e.fehler_bild))) : null,
    el('p', { class: 'lr-schritt-text' }, el('b', {}, 'Pass auf! '), ...M(e.fehler))) : null;
  const probe = e.probe ? el('p', { class: 'lr-probe' }, 'Probe: ', ...M(e.probe)) : null;
  const merke = e.regel ? el('div', { class: 'lr-merke' }, el('p', { class: 'lr-ueber' }, 'MERKE'), el('p', { class: 'lr-regel' }, ...M(e.regel))) : null;
  return el('div', { class: 'lr-erklaert lr-erklaert-klar' },
    kurzGesagt && e.regel ? el('p', { class: 'lr-kurzgesagt' }, el('b', {}, 'Kurz gesagt: '), lernText(lernKurzGesagt(e.regel))) : null,
    // M7: Ergänzt Schritt 1 das Kartenbild, steht das Bild nur dort (sonst zweimal fast dasselbe Bild direkt hintereinander)
    einstieg, e.bild && li[0]?.classList.contains('mit-bild') ? null : lernBild(e.bild),
    li.length ? el('div', { class: 'lr-sogehts' }, el('p', { class: 'lr-ueber' }, 'BEISPIEL – SCHRITT FÜR SCHRITT'), el('ol', {}, ...li)) : null,
    probe, passauf, merke,
    wctx.liste.length && !kurz ? el('details', { class: 'lr-woerter' }, el('summary', {}, `Neue Wörter (${wctx.liste.length})`),
      el('dl', {}, ...wctx.liste.flatMap((w) => [el('dt', {}, ...lernBruchKnoten(w.wort)), el('dd', {}, ...lernBruchKnoten(w.text))]))) : null);
}

// Etappen einer Einheit (Fallback ohne gepflegte Etappen: je Lernziel eine Etappe ohne Erklärung).
function lernEtappen(daten) {
  const inh = daten.inhalt || {};
  const pflicht = new Map((daten.stand || []).map((s) => [s.lernziel, s.pflicht]));
  const st = daten.etappen_stand || {};
  const liste = inh.etappen?.length ? inh.etappen
    : [...new Set((daten.uebungen || []).map((a) => a.lernziel))].map((lz) => ({ lernziel: lz, titel: lernZielName(lz), regel: '' }));
  const abschnitt = new Map();
  for (const ab of inh.abschnitte || []) for (const lz of ab.lernziele || []) abschnitt.set(lz, ab.titel);
  return liste.map((e, i) => {
    const k = st[e.lernziel] || {};
    return { ...e, nr: i + 1, fertig: !!k.fertig, extra: pflicht.get(e.lernziel) === false, abschnitt: abschnitt.get(e.lernziel) || null,
      serie: Number(k.serie || 0), ziel: Number(k.ziel || 4), sitzt: !!k.sitzt, schwerOk: !!k.schwer_ok, schwerNoetig: !!k.schwer_noetig, faellig: !!k.faellig, nachgewiesen: !!k.fertig && !k.sitzt,
      aufgaben: (daten.uebungen || []).filter((a) => a.lernziel === e.lernziel && !a.bonus),
      bonus: (daten.bonus || []).filter((a) => a.lernziel === e.lernziel) }; // F: Knobel-Bordkarten (freiwillig)
  });
}
// Punkte für die Serie: ●●○○ (gefüllt = richtig in Folge), bei „sitzt“ alle gefüllt.
function lernPunkte(e, { gross = false } = {}) {
  const n = Math.max(1, e.ziel || 4), voll = e.sitzt || e.fertig ? n : Math.min(n, e.serie || 0);
  return el('span', { class: 'lr-punkte' + (gross ? ' gross' : ''), role: 'img', 'aria-label': e.sitzt || e.fertig ? 'sitzt' : `${voll} von ${n} Punkten` },
    ...Array.from({ length: n }, (_, i) => el('i', { class: i < voll ? 'voll' : '' })));
}
const lernKartenStatus = (e) => e.faellig ? 'Wiederholen' : e.sitzt || e.fertig ? 'sitzt' : e.serie ? 'am Üben' : 'noch nicht geübt';
// Bereiche: aus inhalt.abschnitte, sonst ein Bereich mit allen Karten.
function lernBereiche(etappen) {
  const map = new Map();
  for (const e of etappen) { const t = e.abschnitt || 'Etappen'; if (!map.has(t)) map.set(t, []); map.get(t).push(e); }
  return [...map].map(([titel, karten]) => ({ titel, karten }));
}

async function viewLernEinheit(arg) {
  setChrome('Lerneinheit', { back: true, showTabs: false });
  const live = viewGuard();
  const [kindId, einheitId, teil] = String(arg || '').split('-');
  const k = Number(kindId), eId = Number(einheitId);
  if (!k || !eId) { route('lernen'); return; }
  loading();
  const [daten, konto, uebers] = await Promise.all([lernCall('schule_einheit_lesen', { lernender_id: k, einheit_id: eId }),
    lernCall('schule_konto', { lernender_id: k }).catch(() => null), lernCall('schule_uebersicht').catch(() => null)]);
  if (!live()) return;
  const kind = { id: k, ...((uebers?.lernende || []).find((x) => x.id === k) || {}), ...(konto?.look || {}) };
  const ort = (uebers?.einheiten || []).find((e) => e.id === eId) || {};
  const titel = ort.stadt ? `${ort.stadt}: ${ort.ort_titel || ort.titel || ''}` : (daten.inhalt?.ziel || 'Lerneinheit').split(/[:;.]/)[0];
  $('#title').textContent = ort.stadt || titel; // kurz: der Ort; das Thema steht als Überschrift darunter
  const ctx = { kind: k, einheit: eId, live, daten, ort, titel, kindObj: kind, basis: `#/lerneinheit/${k}-${eId}`, leitung: !!uebers?.leitung };
  const etappen = lernEtappen(daten);
  lernTitel = new Map(etappen.filter((e) => daten.inhalt?.etappen?.length).map((e) => [e.lernziel, e.titel]));
  ctx.titelKurz = ort.titel || titel;
  if (teil === 'test' || (!teil && daten.laufender_test)) { lernEinheitTest(ctx); return; }
  // #/lerneinheit/k-e[-erklaeren|-ueben[-n]|-fehler|-n]
  const rest = String(arg).split('-').slice(3);
  const n = Number(teil);
  if (n && etappen[n - 1]) { lernThemaSeite(ctx, etappen, 'ueben', n); return; }
  lernThemaSeite(ctx, etappen, ['ueben', 'fehler'].includes(teil) ? teil : 'erklaeren', Number(rest[0]) || 0);
}

// ---------- Thema: Erklären | Üben | Typische Fehler (Aufbau wie das Mathe-Lernblatt) ----------
function lernTestTeil(ctx, etappen) {
  const { daten } = ctx;
  const pflicht = etappen.filter((e) => !e.extra);
  const offen = pflicht.filter((e) => !e.fertig).length;
  if (!pflicht.length) return el('p', { class: 'lr-gesperrt' }, 'Dieser Flug wird gerade vorbereitet. Schau bald wieder vorbei.');
  if (daten.laufender_test) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Angefangenen Test weitermachen');
  if (daten.blocktest_fertig) return el('a', { class: 'lr-zeile', href: `${ctx.basis}-test` }, el('span', { class: 'lr-zeile-icon' }, lernIcon(LI.stempel, 22)),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, 'Test, Verbessern und Nachtests'), el('small', {}, daten.nachtest?.grund === 'faellig' ? 'Ein Nachtest ist jetzt dran.' : 'Hier siehst du, was als Nächstes kommt.')), lernIcon(LI.pfeil, 20));
  if (!offen) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Alle Etappen sitzen – Test starten');
  return el('p', { class: 'lr-gesperrt' }, lernIcon('M6 11h12v10H6z|M9 11V8a3 3 0 0 1 6 0v3', 20), `Der Test kommt, wenn alle Etappen sitzen (noch ${offen}).`);
}

function lernThemaSeite(ctx, etappen, start, karteNr) {
  const { daten, kindObj: kind } = ctx;
  const neu = lernNeu(kind); const ortCode = String(ctx.ort.stadt || 'Thema').toUpperCase();
  // Tabs schreiben die Adresse per replaceState um; die Ansicht bleibt gültig, bis neu gerendert wird.
  const gen = renderGeneration; ctx.live = () => gen === renderGeneration;
  const pflicht = etappen.filter((e) => !e.extra);
  const sitzen = () => pflicht.filter((e) => e.fertig).length;
  const empfohlen = () => etappen.find((e) => e.faellig) || etappen.find((e) => !e.fertig && !e.extra) || etappen.find((e) => !e.fertig) || etappen[0];
  const fehlerKarten = etappen.filter((e) => e.fehler);
  // Neue Lernkarte (noch nie geübt): erst die Erklärung zeigen, dann die Aufgaben („Jetzt du ›“).
  const erklGesehen = new Set(); // Karten, deren Erklärung das Kind in dieser Sitzung schon vor sich hatte
  const lernTypGesehen = {}; // F: je Etappe die Typen, die in dieser Sitzung schon dran waren
  const neuKarte = (e) => !!e && !e.fertig && !e.sitzt && !e.faellig && !e.serie && !!e.regel && !erklGesehen.has(e.lernziel) && !e.aufgaben.some((x) => x.versuche || x.geloest);
  const erstErklaeren = (e) => { offeneKarte = e; zeichneErklaeren(); zeige('erklaeren'); adresse(e, false); window.scrollTo(0, 0); };
  if (start === 'ueben' && !karteNr && neuKarte(empfohlen())) { karteNr = empfohlen().nr; start = 'erklaeren'; }
  const fortschritt = el('div', { class: 'lr-fortschritt' });
  const zeichneFortschritt = () => lernErsetze(fortschritt, 
    el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${sitzen()} von ${pflicht.length} Etappen sitzen` }, el('span', { style: `width:${pflicht.length ? Math.round(100 * sitzen() / pflicht.length) : 0}%` })),
    el('b', {}, `${sitzen()} von ${pflicht.length} sitzen`));
  zeichneFortschritt();
  const tabs = { erklaeren: null, ueben: null, fehler: null };
  const panels = { erklaeren: el('section', { class: 'lr-panel', role: 'tabpanel' }), ueben: el('section', { class: 'lr-panel', role: 'tabpanel' }), fehler: el('section', { class: 'lr-panel', role: 'tabpanel' }) };
  const anzahlUeben = etappen.reduce((n, e) => n + e.aufgaben.length, 0);
  const tabLeiste = el('div', { class: 'lr-tabs lr-tabs-3', role: 'tablist', 'aria-label': 'Flug' },
    ...[['erklaeren', 'Erklären', null], ['ueben', 'Üben', anzahlUeben], ['fehler', 'Fehler', fehlerKarten.length]].map(([k, t, n]) => {
      tabs[k] = el('button', { type: 'button', role: 'tab', onclick: () => zeige(k), onkeydown: (ev) => { const r = ['erklaeren', 'ueben', 'fehler']; const d = ev.key === 'ArrowRight' ? 1 : ev.key === 'ArrowLeft' ? -1 : 0; if (d) { const z = r[(r.indexOf(k) + d + 3) % 3]; zeige(z); tabs[z].focus(); } } }, t, n ? el('small', {}, ' ' + n) : null);
      return tabs[k];
    }));
  const zeige = (k, opts = {}) => {
    for (const x of Object.keys(tabs)) { tabs[x].setAttribute('aria-selected', String(x === k)); panels[x].hidden = x !== k; }
    if (k === 'ueben') uebenOeffnen(opts.karte);
    try { history.replaceState(null, '', `${ctx.basis}-${k}${k === 'ueben' && aktKarte ? '-' + aktKarte.nr : k === 'erklaeren' && offeneKarte ? '-' + offeneKarte.nr : ''}`); } catch { /* egal */ }
    if (opts.scrollZu) opts.scrollZu.scrollIntoView({ block: 'start' }); else window.scrollTo(0, 0);
  };

  // --- Erklären (Vorgabe 16.11.): Übersicht aus Kacheln (Titel, Status, „Kurz gesagt“) → genau eine Karte mit Zurück und Weiter
  const bereiche = lernBereiche(etappen);
  let offeneKarte = start === 'erklaeren' && karteNr ? etappen[karteNr - 1] || null : null;
  const kurzOben = lernKurzOben(kind);
  const adresse = (e, push) => { try { history[push ? 'pushState' : 'replaceState'](null, '', `${ctx.basis}-erklaeren${e ? '-' + e.nr : ''}`); } catch { /* egal */ } };
  const zeichneErklaeren = () => {
    const e = offeneKarte;
    if (!e) {
      lernErsetze(panels.erklaeren, ...bereiche.map((b) => el('section', { class: 'lr-bereich' },
        bereiche.length > 1 ? el('h2', { class: 'lr-abschnitt' }, b.titel.toUpperCase()) : null,
        el('div', { class: 'lr-kacheln' }, ...b.karten.map((k) => el('button', { type: 'button', class: 'lr-karte-box lr-kachel' + (k === empfohlen() ? ' jetzt' : ''),
          onclick: () => { offeneKarte = k; adresse(k, true); zeichneErklaeren(); window.scrollTo(0, 0); } },
          el('span', { class: 'lr-kachel-kopf' }, el('b', {}, `${k.nr} · ${k.titel}`), el('span', { class: 'lr-lk-status' }, lernPunkte(k), el('small', {}, lernKartenStatus(k)))),
          k.regel ? el('span', { class: 'lr-kachel-kurz' }, el('small', {}, 'Kurz gesagt: '), lernText(lernKurzGesagt(k.regel))) : null))))),
        lernTestTeil(ctx, etappen),
        ctx.leitung ? lernAendern({ einheit_id: ctx.einheit, lernender_id: ctx.kind }, { bezug: 'flug', wo: `Flug „${ctx.titelKurz}“` }) : null);
      return;
    }
    const naechste = etappen[etappen.indexOf(e) + 1] || null;
    lernErsetze(panels.erklaeren,
      el('button', { type: 'button', class: 'lr-textlink lr-zur-uebersicht', onclick: () => { offeneKarte = null; adresse(null, false); zeichneErklaeren(); window.scrollTo(0, 0); } }, '‹ Übersicht'),
      el('article', { class: 'lr-karte-box lr-lernkarte' },
        el('div', { class: 'lr-lernkarte-kopf' }, el('h3', {}, `${e.nr} · ${e.titel}`), el('span', { class: 'lr-lk-status' }, lernPunkte(e), el('small', {}, lernKartenStatus(e)))),
        e.regel ? lernErklaerung(e, { kurzGesagt: kurzOben }) : el('p', { class: 'lr-leise' }, 'Für diese Etappe gibt es noch keine Erklärung.'),
        e.aufgaben.length ? el('button', { type: 'button', class: 'lr-knopf lr-dazu', onclick: () => { erklGesehen.add(e.lernziel); zeige('ueben', { karte: e }); } }, 'Jetzt du ›') : null,
        ctx.leitung ? lernAendern({ einheit_id: ctx.einheit, lernziel: e.lernziel, lernender_id: ctx.kind }, { bezug: 'erklaerung', wo: `Erklärung „${e.titel}“` }) : null),
      naechste ? el('button', { type: 'button', class: 'lr-knopf-zweit lr-naechste-karte', onclick: () => { offeneKarte = naechste; adresse(naechste, true); zeichneErklaeren(); window.scrollTo(0, 0); } }, `Nächste Etappe: ${naechste.titel} ›`) : null);
  };
  zeichneErklaeren();

  // --- Typische Fehler
  const versucht = etappen.flatMap((e) => e.aufgaben.filter((a) => a.versuche && !a.geloest).map((a) => ({ e, a })));
  lernAnhaengen(panels.fehler, 
    el('p', { class: 'lr-leise' }, 'Die Stellen, an denen es oft schiefgeht.'),
    ...(fehlerKarten.length ? fehlerKarten.map((e) => el('article', { class: 'lr-karte-box lr-fehlerkarte' },
      el('h3', {}, `${e.nr} · ${e.titel}`), el('div', { class: 'lr-fehler' }, el('b', {}, 'Achtung: '), ...lernMarkiert(e.fehler)),
      el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { offeneKarte = e; zeichneErklaeren(); zeige('erklaeren'); adresse(e, false); } }, 'Erklärung ansehen'))) : [el('p', { class: 'lr-leise' }, 'Für diesen Flug sind noch keine typischen Fehler eingetragen.')]),
    versucht.length ? el('section', { class: 'lr-karte-box' }, el('h3', {}, `Hat bei dir noch nicht geklappt (${versucht.length})`),
      el('ul', { class: 'lr-meinefehler' }, ...versucht.slice(0, 8).map(({ e, a }) => el('li', {}, el('span', {}, lernText(a.frage?.text || '')),
        el('button', { type: 'button', class: 'lr-knopf-zweit lr-knopf-klein', onclick: () => zeige('ueben', { karte: e }) }, 'Üben'))))) : null);

  // --- Üben: eine Lernkarte, Aufgaben nacheinander; Erklärung klappt an der Aufgabe auf
  let aktKarte = null, stufe = 0;
  let gezeichnet = null;
  const uebenOeffnen = (karte) => {
    if (karte && karte !== aktKarte) { aktKarte = karte; stufe = 0; }
    if (!aktKarte) aktKarte = (karteNr && etappen[karteNr - 1]) || empfohlen();
    if (gezeichnet !== aktKarte) zeichneUeben(); // sonst bleibt Bordkarte samt Rückmeldung stehen
  };
  const zeichneUeben = () => {
    const e = aktKarte; gezeichnet = e;
    const mitAufg = etappen.filter((x) => x.aufgaben.length); const pos = mitAufg.indexOf(e);
    const wechsel = (d) => el('button', { type: 'button', class: 'lr-pfeilknopf', 'aria-label': d < 0 ? 'Vorige Etappe' : 'Nächste Etappe', disabled: !mitAufg[pos + d],
      onclick: () => { aktKarte = mitAufg[pos + d]; stufe = 0; zeichneUeben(); } }, d < 0 ? '‹' : '›');
    const stufenDa = [1, 2, 3].filter((n) => e.aufgaben.some((a) => a.stufe === n));
    const chipsStufe = stufenDa.length > 1 ? el('div', { class: 'lr-chips lr-chips-klein', role: 'group', 'aria-label': 'Stufe' },
      ...[[0, 'alle'], [1, 'leicht'], [2, 'mittel'], [3, 'schwer']].filter(([n]) => !n || stufenDa.includes(n))
        .map(([n, t]) => el('button', { type: 'button', class: stufe === n ? 'on' : '', 'aria-pressed': String(stufe === n), onclick: () => { stufe = n; zeichneUeben(); } }, t))) : null;
    const punkte = el('div', { class: 'lr-lk-punkte' });
    const zeichnePunkte = () => lernErsetze(punkte, lernPunkte(e, { gross: true }),
      el('small', {}, e.sitzt || e.fertig ? (e.faellig ? 'Sitzt – heute wiederholen' : 'Sitzt! Du kannst trotzdem weiterüben.') : e.serie >= e.ziel && e.schwerNoetig && !e.schwerOk ? 'Fast geschafft: noch eine schwere Bordkarte richtig' : `${Math.min(e.serie, e.ziel)} von ${e.ziel} Punkten`));
    zeichnePunkte();
    const flaeche = el('div', { class: 'lr-ueben-flaeche' });
    lernErsetze(panels.ueben, el('div', { class: 'lr-karte-box lr-lk-kopf' }, wechsel(-1),
      el('div', { class: 'lr-lk-mitte' }, el('small', { class: 'lr-leise' }, neu ? `Etappe ${pos + 1}/${mitAufg.length} · ${e.titel}` : `Etappe ${pos + 1} von ${mitAufg.length}`), neu ? null : el('b', {}, e.titel), punkte), wechsel(1)), flaeche, chipsStufe);
    if (!pflicht.some((x) => !x.fertig) && !e.faellig) // alle Etappen sitzen: nicht endlos weiterüben lassen, sondern den Test anbieten
      panels.ueben.prepend(el('div', { class: 'lr-karte-box lr-testbereit' }, el('p', {}, el('b', {}, 'Alle Etappen dieses Flugs sitzen. '), 'Du musst hier nicht weiterüben – als Nächstes kommt der Test.'), lernTestTeil(ctx, etappen)));
    const pool = e.aufgaben.filter((a) => !stufe || a.stufe === stufe);
    const warte = [...pool].sort((a, b) => (a.geloest === b.geloest ? 0 : a.geloest ? 1 : -1) || (a.versuche || 0) - (b.versuche || 0) || (a.stufe || 2) - (b.stufe || 2));
    let sterne = 0, nr = 0, fehlFolge = 0; // fehlFolge: falsche Bordkarten hintereinander auf dieser Karte (V8)
    const naechsteKarte = etappen.slice(e.nr).find((x) => !x.fertig && x.aufgaben.length) || etappen.find((x) => x !== e && !x.fertig && x.aufgaben.length);
    // Regel „sitzt“ (16.11.): Die Stufe steigt mit den Punkten – erst leicht, dann mittel, dann schwer. Ein Fehler kostet 2 Punkte, also geht es eine Stufe zurück.
    let letzte = null;
    const gesehenTyp = (lernTypGesehen[e.lernziel] ||= new Set()); // F: Typen, die in dieser Etappe schon dran waren
    const waehleStufe = () => { if (!stufe && !e.sitzt && !e.fertig) lernWaehleBordkarte(warte, e, letzte, gesehenTyp); };
    const zeigeAufgabe = (fest) => {
      if (fest !== true) waehleStufe();
      const a = warte[0]; letzte = a || null; if (a?.typ) gesehenTyp.add(a.typ);
      if (!a) { lernErsetze(flaeche, el('p', { class: 'lr-leise' }, 'Für diese Auswahl gibt es keine Bordkarten.')); return; }
      nr++;
      const auf = lernAufgabe(a, null, { tasten: neu, stellen: neu && kind.klasse && kind.klasse <= 6 }); let hilfe = 0; const dock = el('div', { class: 'lr-dock' }); let cid = lernCid();
      // V2: zweiter Versuch vor der Lösung (nicht bei Ja/Nein-Auswahl – dort wäre der zweite Versuch die Lösung)
      let anlauf = 1; const zweiteChance = !(a.antworttyp === 'auswahl' && (a.antworten || []).length <= 2);
      const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
      const hilfeBox = el('div', { class: 'lr-hilfebox' });
      const tipp = a.tipp ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { hilfe = 1; tipp.remove(); lernAnhaengen(hilfeBox, el('p', { class: 'lr-tipp' }, el('b', {}, 'Tipp: '), lernText(a.tipp), el('small', {}, ' (zählt nicht für die Serie)'))); } }, 'Tipp') : null;
      // Vorgabe 16.11.: Beim Üben steht nur die Aufgabe. Darüber ein gut sichtbarer Link „Erklärung ansehen“ (am Rechner klappt sie links daneben auf).
      const breit = neu && !!e.regel && !!window.matchMedia?.('(min-width: 900px)').matches;
      const erkl = e.regel ? el('button', { type: 'button', class: 'lr-erkl-link', 'aria-expanded': 'false', onclick: () => {
        const offen = erkl.getAttribute('aria-expanded') === 'true';
        erkl.setAttribute('aria-expanded', String(!offen)); erklBox.hidden = offen; erkl.firstChild.textContent = offen ? 'Erklärung ansehen' : 'Erklärung schließen';
        flaeche.classList.toggle('lr-zweispaltig', breit && !offen);
      } }, 'Erklärung ansehen') : null;
      const neuHier = false;
      erklGesehen.add(e.lernziel);
      const erklBox = el('div', { class: 'lr-karte-box lr-nochmal' + (breit ? ' lr-seite-links' : ''), hidden: true }, e.regel ? lernErklaerung(e, { kurz: true }) : null);
      flaeche.classList.remove('lr-zweispaltig');
      const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
      auf.node.addEventListener('input', () => { if (anlauf === 1 && !pruefen.disabled && pruefen.isConnected) lernErsetze(meldung); });
      pruefen.addEventListener('click', async () => {
        const w = auf.antwort();
        if (!w) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
        pruefen.disabled = true;
        try {
          const r = await lernCall('schule_uebung_pruefen', { lernender_id: ctx.kind, aufgabe_id: a.id, antwort: w, client_id: cid, hilfe, ...(zweiteChance ? { anlauf } : {}) });
          if (!ctx.live()) return;
          if (!r.format_ok) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, r.hinweis)); pruefen.disabled = false; return; }
          if (r.nochmal) { // 1. Fehler: keine Lösung, nur ein Hinweis – die Eingabe bleibt änderbar
            anlauf = 2; cid = lernCid(); pruefen.disabled = false;
            lernErsetze(meldung, el('div', { class: 'lr-rueck lr-rueck-nochmal' }, el('b', {}, 'Noch nicht – du hast einen zweiten Versuch.'),
              el('p', {}, LERN_GRUND[r.grund] || (a.tipp ? 'Tipp: ' + lernText(a.tipp) : 'Lies die Bordkarte noch einmal genau und prüfe deine Rechnung.'))));
            if (!LERN_GRUND[r.grund] && a.tipp) tipp?.remove();
            meldung.scrollIntoView?.({ block: 'nearest', behavior: 'smooth' });
            return;
          }
          auf.sperren(); a.loesung = r.loesung; warte.shift(); a.versuche = (a.versuche || 0) + 1;
          const sterneVor = sterne;
          if (r.richtig) { if (!a.geloest && !r.wiederholt) sterne += 10; a.geloest = true; warte.push(a); }
          else { // V5: gemerkte Lösung zählt nicht – nach einem Fehler kommt eine andere Bordkarte derselben Stufe; dieselbe erst ganz am Ende
            warte.push(a);
            const j = warte.findIndex((x) => x !== a && !x.geloest && (x.stufe || 2) === (a.stufe || 2) && !x.falschHeute);
            if (j > 0) warte.unshift(...warte.splice(j, 1));
            a.falschHeute = true;
          }
          auf.zeigeLoesung(r.loesung); fehlFolge = r.richtig ? 0 : fehlFolge + 1;
          const warSitzt = e.sitzt;
          if (r.karte) { e.serie = r.karte.serie; e.ziel = r.karte.ziel; e.sitzt = r.karte.sitzt; e.schwerOk = !!r.karte.schwer_ok; e.schwerNoetig = !!r.karte.schwer_noetig; e.fertig = e.fertig || r.karte.sitzt; if (warSitzt && r.karte.sitzt) e.faellig = false; }
          zeichnePunkte(); zeichneFortschritt();
          const jetztSitzt = !!r.karte?.neu_sitzt || (!warSitzt && e.sitzt);
          const weiter = el('button', { type: 'button', class: 'lr-knopf lr-weiter', onclick: () => { zeigeAufgabe(); window.scrollTo(0, 0); } }, neu ? 'Neue Bordkarte ›' : 'Nächste Bordkarte');
          if (neu) lernErsetze(dock, weiter); else { pruefen.remove(); meldung.after(weiter); }
          weiter.focus({ preventScroll: true });
          if (!neu && !r.richtig && erkl && erklBox.hidden && false) { erklBox.hidden = false; erkl.setAttribute('aria-expanded', 'true'); }
          lernErsetze(meldung, r.richtig
            ? el('div', { class: 'lr-rueck lr-rueck-ok' }, el('b', {}, neu ? '✓ An Bord' + (sterne > sterneVor ? ' · +10 Sterne' : '') : 'Richtig!'), r.loesungsweg ? el('p', {}, lernText(r.loesungsweg)) : null)
            : neu ? el('div', { class: 'lr-rueck lr-rueck-falsch lr-kursbox' }, el('p', { class: 'lr-ueber' }, a.antworttyp === 'zahl' && r.grund ? 'FAST – KURSKORREKTUR' : 'NOCH NICHT'), lernKurs(a, w),
              el('b', {}, 'Richtig ist: ' + lernLoesungText(a)),
              a.antworttyp === 'luecken' && lernIstTermVorlage(a.frage?.schablone) && lernGleichwertigAusgeklammert(a.frage?.schablone, w.werte, r.loesung?.werte)
                ? el('p', {}, 'Dein Term ist gleichwertig, aber noch nicht vollständig ausgeklammert: Vor die Klammer gehört der größte gemeinsame Faktor.') : null,
              r.loesungsweg ? el('p', {}, lernText(r.loesungsweg)) : null,
              lernDetektiv(a, e, r, 'IST DIR DAS PASSIERT?'))
            : el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, 'Noch nicht. Richtig ist: ' + lernLoesungText(a)),
              a.antworttyp === 'luecken' && lernIstTermVorlage(a.frage?.schablone) && lernGleichwertigAusgeklammert(a.frage?.schablone, w.werte, r.loesung?.werte)
                ? el('p', {}, 'Dein Term ist gleichwertig, aber noch nicht vollständig ausgeklammert: Vor die Klammer gehört der größte gemeinsame Faktor.') : null,
              r.loesungsweg ? el('p', {}, el('b', {}, 'So geht’s: '), lernText(r.loesungsweg)) : null,
              lernDetektiv(a, e, r, 'FEHLER-DETEKTIV: IST DIR DAS PASSIERT?'),
              el('p', { class: 'lr-leise' }, 'Ein Fehler kostet 2 Punkte. Die Erklärung findest du über der Bordkarte.')));
          if (!r.richtig) {
            if (LERN_GRUND[r.grund]) meldung.firstElementChild?.prepend(el('p', { class: 'lr-grund' }, LERN_GRUND[r.grund])); // V3
            if (fehlFolge >= 2) { // V8: nach 2 Fehlern in Folge ein anderer Weg, nach 3 der Hinweis auf die Eltern
              const leichter = (a.stufe || 2) > 1 ? warte.find((x) => !x.geloest && !x.falschHeute && (x.stufe || 2) < (a.stufe || 2)) : null;
              lernAnhaengen(meldung.firstElementChild, el('div', { class: 'lr-andererweg' }, el('p', {}, el('b', {}, 'Das hakt gerade. '), 'Probier einen anderen Weg:'),
                el('div', { class: 'lr-knopfzeile' },
                  leichter ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { warte.splice(warte.indexOf(leichter), 1); warte.unshift(leichter); zeigeAufgabe(true); window.scrollTo(0, 0); } }, 'Leichtere Bordkarte') : null,
                  erkl ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { if (erkl.getAttribute('aria-expanded') !== 'true') erkl.click(); erklBox.scrollIntoView?.({ block: 'start', behavior: 'smooth' }); } }, 'Beispiel ansehen') : null),
                fehlFolge >= 3 ? el('p', { class: 'lr-leise' }, 'Frag Mama oder Papa – sie sehen unter „Was wackelt?“, wo es hakt.') : null));
            }
          }
          if (jetztSitzt && neu) {
            lernErsetze(flaeche, el('section', { class: 'lr-gelandet' },
              el('p', { class: 'lr-ueber' }, `ETAPPE ${pos + 1} VON ${mitAufg.length}`),
              el('div', { class: 'lr-landestempel', 'aria-hidden': 'true' }, el('b', {}, 'GELANDET'), el('small', {}, ortCode)),
              el('h2', {}, e.titel, ' ✓'), el('p', {}, `${e.ziel || 6} Punkte gesammelt` + (e.schwerNoetig ? ' – auch eine schwere Bordkarte war dabei.' : '.')),
              sterne ? el('p', { class: 'lr-sterne-neu' }, lernIcon(LI.stern, 20), ` +${sterne} Sterne`) : null,
              el('p', { class: 'lr-leise' }, 'Die Etappe kommt in ein paar Tagen zum Wiederholen.'),
              lernKnobelAngebot(e, (k) => lernKnobel(flaeche, k, ctx, { ortCode, zurueck: () => { stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } })),
              naechsteKarte ? el('button', { type: 'button', class: 'lr-knopf', onclick: () => { if (neuKarte(naechsteKarte)) { erstErklaeren(naechsteKarte); return; } aktKarte = naechsteKarte; stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } }, `Anschlussflug: ${naechsteKarte.titel} ›`) : null,
              !naechsteKarte && !pflicht.some((x) => !x.fertig) ? lernTestTeil(ctx, etappen) : null,
              el('a', { class: 'lr-knopf-zweit', href: `#/reise/${ctx.kind}` }, 'Zur Abflugtafel'),
              el('a', { class: 'lr-textlink', href: `#/wiederholen/${ctx.kind}` }, 'Wiederholungen ansehen, falls noch welche offen sind')));
            window.scrollTo(0, 0); flaeche.querySelector('.lr-knopf, .lr-knopf-zweit')?.focus({ preventScroll: true });
            return;
          }
          if (neu) { meldung.scrollIntoView?.({ block: 'center', behavior: 'smooth' }); return; }
          if (jetztSitzt) lernAnhaengen(meldung, el('section', { class: 'lr-geschafft lr-sitzt' },
            el('div', { class: 'lr-geschafft-haken' }, lernIcon(LI.haken, 48)),
            el('p', { class: 'lr-ueber' }, 'ETAPPE SITZT'), el('h2', {}, e.titel),
            sterne ? el('p', { class: 'lr-sterne-neu' }, lernIcon(LI.stern, 20), ` +${sterne} Sterne`) : null,
            el('p', { class: 'lr-leise' }, 'Sie kommt in ein paar Tagen zum Wiederholen.'),
            lernKnobelAngebot(e, (k) => lernKnobel(flaeche, k, ctx, { ortCode, zurueck: () => { stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } })),
            naechsteKarte ? el('button', { type: 'button', class: 'lr-knopf', onclick: () => { if (neuKarte(naechsteKarte)) { erstErklaeren(naechsteKarte); return; } aktKarte = naechsteKarte; stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } }, `Nächste Etappe: ${naechsteKarte.titel}`)
              : el('button', { type: 'button', class: 'lr-knopf', onclick: () => zeige('erklaeren') }, 'Zur Übersicht der Etappen')));
          (jetztSitzt ? meldung : weiter).scrollIntoView?.({ block: 'center', behavior: 'smooth' });
        } catch (err) { lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
      });
      const fein = window.matchMedia?.('(pointer: fine)').matches;
      auf.node.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' && ev.target.tagName === 'INPUT') { ev.preventDefault(); if (pruefen.isConnected) pruefen.click(); } });
      if (neu) {
        lernErsetze(dock, auf.tasten ? lernTastenfeld(auf.tasten, pruefen) : pruefen);
        lernErsetze(flaeche, erkl, erklBox,
          el('section', { class: 'lr-karte-box lr-aufgabe lr-bordkarte' },
            el('div', { class: 'lr-bord-kopf' }, el('span', {}, `BORDKARTE ${nr} · ${ortCode}`), lernStufeZeichen(a)),
            auf.node, el('div', { class: 'lr-perforation', 'aria-hidden': 'true' }),
            tipp ? el('div', { class: 'lr-knopfzeile' }, tipp) : null),
          hilfeBox, meldung,
          ctx.leitung ? lernAendern({ einheit_id: ctx.einheit, lernziel: e.lernziel, aufgabe_id: a.id, lernender_id: ctx.kind }, { bezug: 'bordkarte', wo: `Bordkarte „${String(a.frage?.text || '').slice(0, 60)}“` }) : null, dock);
      } else lernErsetze(flaeche,
        erkl, erklBox,
        el('section', { class: 'lr-karte-box lr-aufgabe' },
          el('p', { class: 'lr-ueber' }, `AUFGABE ${nr} `, lernStufeZeichen(a)), auf.node,
          pruefen, tipp ? el('div', { class: 'lr-knopfzeile' }, tipp) : null),
        hilfeBox, meldung,
        ctx.leitung ? lernAendern({ einheit_id: ctx.einheit, lernziel: e.lernziel, aufgabe_id: a.id, lernender_id: ctx.kind }, { bezug: 'bordkarte', wo: `Bordkarte „${String(a.frage?.text || '').slice(0, 60)}“` }) : null);
      if (fein && (!neuHier || breit)) auf.node.querySelector('input')?.focus({ preventScroll: true });
    };
    zeigeAufgabe();
  };

  const flaeche = el('div', { class: 'lr-thema' },
    neu ? el('header', { class: 'lr-flugkopf' },
      el('a', { class: 'lr-x', href: `#/reise/${ctx.kind}`, 'aria-label': 'Flug schließen' }, '✕'),
      el('div', { class: 'lr-flugkopf-text' }, el('small', {}, ortCode + (lernJahrgangText(ctx.ort.jahrgang, ctx.leitung ? null : kind) ? ' · ' + lernJahrgangText(ctx.ort.jahrgang, ctx.leitung ? null : kind) : '')), el('h1', {}, ctx.titelKurz)))
    : el('header', { class: 'lr-kopf' },
      el('p', { class: 'lr-pfad' }, el('a', { href: `#/reise/${ctx.kind}` }, 'Heute'), ` › ${ctx.ort.stadt || 'Thema'}`),
      el('h1', { class: 'lr-titel' }, ctx.titelKurz),
      lernJahrgangText(ctx.ort.jahrgang, ctx.leitung ? null : kind) ? el('p', { class: 'lr-leise lr-jahrgang' }, lernJahrgangText(ctx.ort.jahrgang, ctx.leitung ? null : kind)) : null),
    fortschritt,
    daten.status === 'entwurf' ? el('p', { class: 'lr-leise' }, 'Entwurf – nur für das Testkind sichtbar.') : null,
    tabLeiste, panels.erklaeren, panels.ueben, panels.fehler);
  const rahmen = lernRahmen(kind, 'weg', flaeche);
  if (neu) rahmen.classList.add('lr-ohne-nav');
  if (neu) { // W150 Abflug: waagrecht wischen wechselt den Reiter (Erklären ↔ Üben ↔ Fehler)
    let sx = 0, sy = 0, ok = false;
    flaeche.addEventListener('touchstart', (ev) => { const t = ev.touches[0]; ok = ev.touches.length === 1 && !ev.target.closest?.('input, textarea, select, .lern-zeichnung, .lr-tafel, .lr-tastenfeld, .lr-kurs, .lern-stellen'); sx = t.clientX; sy = t.clientY; }, { passive: true });
    flaeche.addEventListener('touchend', (ev) => {
      if (!ok) return; const t = ev.changedTouches[0]; const dx = t.clientX - sx, dy = t.clientY - sy;
      if (Math.abs(dx) < 70 || Math.abs(dy) > Math.abs(dx) * 0.6) return;
      const r = ['erklaeren', 'ueben', 'fehler']; const z = r[r.findIndex((x) => !panels[x].hidden) + (dx < 0 ? 1 : -1)];
      if (!z) return; zeige(z);
      panels[z].classList.remove('lr-rein-links', 'lr-rein-rechts'); void panels[z].offsetWidth; panels[z].classList.add(dx < 0 ? 'lr-rein-rechts' : 'lr-rein-links');
    }, { passive: true });
  }
  lernErsetze(main, rahmen);
  zeige(start);
}
const LERN_SCHULART = { gym_by: 'Gymnasium', rs_by: 'Realschule', ib_myp: 'IB MYP' };
function lernJahrgangText(j, kind) {
  if (!j || !Object.keys(j).length) return '';
  if (kind && !kind.leitung) { const sa = kind.schulart || 'gym_by'; return j[sa] ? `${LERN_SCHULART[sa] || 'Gymnasium'} · Klasse ${j[sa]}` : ''; } // K1/U5: Kind sieht nur die eigene Schulart
  return [['gym_by', 'Gym'], ['rs_by', 'RS'], ['ib_myp', 'IB']].filter(([k]) => j[k]).map(([k, t]) => `${t} ${j[k]}`).join(' · ');
}

function lernEinheitTest(ctx) {
  const body = el('div', { class: 'lern-body' });
  lernErsetze(main, lernRahmen(ctx.kindObj, 'weg',
    el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-ueber' }, 'TEST'), el('h1', { class: 'lr-titel' }, ctx.ort?.stadt ? `${ctx.ort.stadt} · ${ctx.titelKurz}` : ctx.titel)), // N6: „Ort · Flug“ wie im Erklären-Reiter
    el('a', { class: 'lr-zurueck', href: ctx.basis }, '‹ Zu den Etappen'), body));
  lernAnhaengen(body, lernTestStart(ctx, body));
}

// ---------- Merkheft-Daten ----------
// Je Einheit: Etappen mit Stand. Nutzt schule_merkheft; fehlt die Aktion (Server noch alt), werden die Einheiten einzeln gelesen.
async function lernMerkDaten(d) {
  try { const r = await lernCall('schule_merkheft', { lernender_id: d.kind.id }); return r.einheiten || []; }
  catch (err) {
    if (!/Unbekannte Aktion/.test(err.message)) throw err;
    const liste = await Promise.all(d.mit.map((e) => lernCall('schule_einheit_lesen', { lernender_id: d.kind.id, einheit_id: e.id }).then((x) => ({ e, x })).catch(() => null)));
    return liste.filter((y) => y && y.x.inhalt?.etappen).map(({ e, x }) => ({ einheit_id: e.id, block_id: e.block_id, stadt: e.stadt, ort_titel: e.ort_titel, kontinent: e.kontinent,
      etappen: x.inhalt.etappen, stand: x.etappen_stand || {}, blocktest_fertig: x.blocktest_fertig, nachtest: x.nachtest }));
  }
}
const lernEtappenZahl = (m) => { const n = (m?.etappen || []).length; const f = (m?.etappen || []).filter((e) => m.stand?.[e.lernziel]?.fertig).length; return { n, f }; };

// ---------- Kind: Mein Weg (K2) – Reiter Stand · Kontinente · Karte ----------
// #/weg/<kind>[-stand|-kontinente|-karte]. Die Weltkarte (früher eigener Menüeintrag) ist der Reiter „Karte“.
const LERN_WEG_REITER = [['stand', 'Stand'], ['kontinente', 'Kontinente'], ['karte', 'Karte']];
// Ein Flug gilt als gelandet, wenn alle Pflicht-Etappen sitzen; auch „kann schon“ und geschaffte Orte zählen (Rechenregel „Stand“).
const lernGelandet = (e) => e.geschafft || e.ortFertig || e.gruppe === 'kann';
async function viewWeg(arg) {
  setChrome('Mein Weg', { back: true, showTabs: false });
  const live = viewGuard();
  const [kindArg, reiterArg, ...tiefer] = String(arg || '').split('-'); // K3: #/weg/<kind>-stand-<schulart>-<stufe>-<kontinent>
  const reiter = LERN_WEG_REITER.some(([k]) => k === reiterArg) ? reiterArg : 'stand';
  loading();
  const d = await lernLadeKind(kindArg);
  if (!d || !live()) return;
  const merk = reiter === 'stand' ? await lernMerkDaten(d).catch(() => []) : [];
  if (!live()) return;
  const { kind } = d;
  $('#title').textContent = 'Mein Weg';
  const tabs = el('nav', { class: 'lr-tabs lr-tabs-3 lr-weg-reiter', 'aria-label': 'Mein Weg' },
    ...LERN_WEG_REITER.map(([k, t]) => el('a', { href: `#/weg/${kind.id}-${k}`, class: k === reiter ? 'on' : '', ...(k === reiter ? { 'aria-current': 'page' } : {}) }, t)));
  const kopf = el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-ueber' }, `MATHE${kind.klasse ? ' · KLASSE ' + kind.klasse : ''}`), el('h1', { class: 'lr-titel' }, 'Mein Weg'));
  const teile = reiter === 'karte' ? lernWegKarte(d) : reiter === 'kontinente' ? lernWegKontinente(d) : lernWegStand(d, merk, tiefer);
  lernErsetze(main, lernRahmen(kind, 'weg', kopf, tabs, ...teile));
}

// K3: „Stand“ mit drei Ebenen – Überblick (Mini-Linien + Linienplan) → Haltestelle (Klasse mit Kontinenten, ‹ › blättert) → Kontinent (Flüge mit „zählt auch für …“)
function lernWegStand(d, merk, tiefer = []) {
  const { kind } = d;
  const m = d.u && kind.klasse ? lernStandModell(d.u, kind) : null;
  const basis = `#/weg/${kind.id}-stand`;
  const konts = m ? [...new Set(m.themen.map((t) => t.kontinent))].sort(lernKontReihe) : [];
  const [saArg, klArg, kontArg] = tiefer; const y = LERN_SYS.find((q) => q.sa === saArg); const kl = Number(klArg);
  if (m && y && kl) {
    const krumen = (teile) => el('nav', { class: 'lr-krumen', 'aria-label': 'Pfad' }, ...teile.flatMap(([t, h], i) => i < teile.length - 1 ? [el('a', { href: h }, t), el('span', { 'aria-hidden': 'true' }, '›')] : [el('b', {}, t)]));
    const c = m.zahl(y.sa, kl); const i = y.stufen.indexOf(kl);
    const nach = (dx) => y.stufen[i + dx] ? el('a', { class: 'lr-pf', href: `${basis}-${y.sa}-${y.stufen[i + dx]}`, 'aria-label': dx < 0 ? 'vorige Klasse' : 'nächste Klasse' }, dx < 0 ? '‹' : '›') : el('span', { class: 'lr-pf leer' });
    const pass = el('section', { class: 'lr-pass-karte', style: `--f:${y.farbe}` },
      el('div', { class: 'lr-pass-kopf' }, nach(-1), el('span', {}, el('small', {}, y.name.toUpperCase()), el('b', {}, y.label(kl).toUpperCase())), nach(1)),
      el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${c.f} von ${c.n} Flügen gelandet` }, el('span', { style: `width:${lernPz(c.f, c.n)}%;background:${y.farbe}` })), el('b', {}, `${c.f} von ${c.n} Flügen`)));
    const k = konts[Number(kontArg)];
    if (kontArg === undefined || !k) {
      const zeilen = konts.map((kn, ki) => { const ts = c.ts.filter((t) => t.kontinent === kn); if (!ts.length) return null; const f = ts.filter((t) => t.st === 'ok').length;
        return el('a', { class: 'lr-kontzeile', href: `${basis}-${y.sa}-${kl}-${ki}` },
          el('span', { class: 'lr-kontzeile-name' }, el('b', {}, kn), el('small', {}, [ts[0].erdteil, ts.some((t) => t.st === 'jetzt') ? 'jetzt dran' : null, ts.some((t) => t.st === 'wackelt') ? 'wackelt' : null].filter(Boolean).join(' · '))),
          el('span', { class: 'lr-kontzeile-balken' }, el('span', { class: 'lr-balken' }, el('span', { style: `width:${lernPz(f, ts.length)}%;background:${y.farbe}` })), el('small', {}, `${f}/${ts.length}`)),
          el('span', { class: 'lr-kontzeile-pfeil', 'aria-hidden': 'true' }, '›')); }).filter(Boolean);
      return [krumen([['Überblick', basis], [lernSysStufe(y, kl), null]]), pass,
        el('h2', { class: 'lr-abschnitt' }, `KONTINENTE IN ${y.label(kl).toUpperCase()}`),
        ...(zeilen.length ? zeilen : [el('p', { class: 'lr-leise' }, 'In dieser Klasse gibt es hier keine Flüge.')])];
    }
    const ts = c.ts.filter((t) => t.kontinent === k);
    const sichtbar = new Set(d.mit.map((e) => e.id));
    return [krumen([['Überblick', basis], [lernSysStufe(y, kl), `${basis}-${y.sa}-${kl}`], [k, null]]),
      el('section', { class: 'lr-karte-box' }, el('p', { class: 'lr-ueber', style: `color:${y.farbe}` }, `${k} · ${y.label(kl)}`.toUpperCase()),
        ...ts.map((t) => { const auch = lernZaehltAuch(t, y.sa); const link = t.einheit && sichtbar.has(t.einheit.id);
          return el(link ? 'a' : 'div', { class: 'lr-standzeile lr-st-' + t.st, ...(link ? { href: `#/lerneinheit/${kind.id}-${t.einheit.id}` } : {}) },
            el('span', { class: 'lr-standpunkt', 'aria-hidden': 'true' }, lernSymbol(t.st)),
            el('span', { class: 'lr-zeile-text' }, el('b', {}, t.titel), el('small', {}, [t.stadt, auch ? 'zählt auch für ' + auch : null, t.ausgelassen ? 'nicht geplant' : null, !t.einheit ? 'kommt bald' : null].filter(Boolean).join(' · '))),
            el('span', { class: 'lr-zeile-zustand' }, { ok: 'gelandet', jetzt: 'jetzt dran', wackelt: 'wackelt', laeuft: 'unterwegs', offen: '' }[t.st])); })),
      el('p', { class: 'lr-leise' }, '„Zählt auch für“ zeigt, welche anderen Linien dieser Flug voranbringt.')];
  }
  const ueberblick = m ? [
    lernMiniLinien(m, (q, k2) => (k2 ? `${basis}-${q.sa}-${k2}` : basis)),
    el('section', { class: 'lr-karte-box lr-linienbox' }, lernLinienplan(m, (q, n2) => `${basis}-${q.sa}-${n2}`)),
    el('p', { class: 'lr-leise' }, 'Tippe auf eine Haltestelle – dann siehst du, wie weit du in jedem Kontinent bist.')] : [];
  const mm = new Map(merk.map((m) => [m.einheit_id, m]));
  const kann = d.orte.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann');
  const offen = d.orte.filter((o) => o.zustand === 'offen');
  // K1/U3: „Kommt noch“ wie die Abflugtafel einteilen (lernReiseDaten): eigene Klasse / frühere Klassen / später. Orte ohne Klasse nur unter „Später“.
  const sa = kind.schulart || 'gym_by'; const klE = (e) => e.jahrgang?.[sa] ?? e.ziel_klasse;
  const ohneFlug = offen.filter((o) => !d.mit.some((e) => e.block_id === o.block_id));
  const klO = (o) => d.ortKlasse?.(o.block_id) ?? o.ziel_klasse; // P2: Klasse des Ortes in der Schulart des Kindes
  const passt = ohneFlug.filter((o) => kind.klasse && lernOrtInKlasse(d, o, kind.klasse));
  const spaeterOrte = ohneFlug.filter((o) => !passt.includes(o) && (!klO(o) || !kind.klasse || klO(o) > kind.klasse));
  const flugZeile = (e) => el('a', { class: 'lr-wegzeile', href: `#/lerneinheit/${kind.id}-${e.id}` }, el('span', { class: 'lr-wegzeile-icon' }),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, e.titel), el('small', {}, [e.kontinent, e.stadt].filter(Boolean).join(' · '))),
    klE(e) ? el('span', { class: 'lr-zeile-zustand' }, 'Kl. ' + klE(e)) : null);
  const zahl = (w, t, cls) => el('div', { class: 'lr-zahl ' + (cls || '') }, el('b', {}, String(w)), el('span', {}, t));
  // M1: „Gerade dran“ = nur der aktuelle Ort; die übrigen Orte im Plan stehen unter „Kommt noch“. Die Kacheln zählen Orte.
  const offenJetzt = d.jetzt.filter((e) => !lernGelandet(e));
  const aktOrt = (d.naechste && !lernGelandet(d.naechste) ? d.naechste : offenJetzt[0])?.block_id;
  const restOrte = [...new Set(offenJetzt.map((e) => e.block_id))].filter((b) => b !== aktOrt);
  const dran = offenJetzt.filter((e) => e.block_id === aktOrt).map((e) => {
    const { n, f } = lernEtappenZahl(mm.get(e.id));
    const info = e.laeuft ? 'Test läuft' : e.blocktest ? 'Test geschrieben' : n ? (f >= n ? 'Test offen' : `Etappe ${f + 1} von ${n}`) : `${e.fertig}/${e.n}`;
    return el('a', { class: 'lr-dran', href: `#/lerneinheit/${kind.id}-${e.id}` },
      el('div', { class: 'lr-dran-kopf' }, el('b', {}, e.titel), el('span', {}, info + ' ›')),
      el('small', {}, [e.stadt, e.kontinent, klE(e) ? 'Kl. ' + klE(e) : ''].filter(Boolean).join(' · ')),
      el('div', { class: 'lr-balken' }, el('span', { style: `width:${n ? Math.round(100 * f / n) : 0}%` })));
  });
  const ortZeile = (o, rechts, icon, href) => el(href ? 'a' : 'div', { class: 'lr-wegzeile', ...(href ? { href } : {}) },
    el('span', { class: 'lr-wegzeile-icon ' + (icon === 'haken' ? 'fertig' : '') }, icon === 'haken' ? lernIcon(LI.haken, 16) : null),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, o.titel), el('small', {}, `${o.kontinent_titel || ''} · ${o.stadt}${o.ziel_klasse ? ' · Kl. ' + o.ziel_klasse : ''}`)),
    rechts ? el('span', { class: 'lr-zeile-zustand' }, rechts) : null);
  const kannZeilen = kann.map((o) => {
    const e = d.mit.find((x) => x.block_id === o.block_id); const m = e && mm.get(e.id);
    const nt = m?.nachtest;
    const info = o.zustand === 'kann' ? 'konnte ich schon' : nt?.grund === 'faellig' ? 'Nachtest dran' : nt?.grund === 'noch_nicht_faellig' ? `Nachtest in ${nt.lerntage_noetig - nt.lerntage_seit} Lerntagen` : nt?.grund === 'gesichert' ? 'sicher' : 'Stempel';
    return ortZeile(o, info, 'haken', m ? `#/merkheft/${kind.id}` : null);
  });
  // Stand der eigenen Klasse (Rechenregel „Stand“): alle Flüge mit jahrgang[schulart] = Klasse. K3 ergänzt die anderen Schularten.
  const eigene = kind.klasse ? d.mit.filter((e) => (e.jahrgang ? e.jahrgang[sa] : e.ziel_klasse) === kind.klasse) : [];
  const gel = eigene.filter(lernGelandet).length, lauf = eigene.filter((e) => !lernGelandet(e) && e.fertig > 0).length;
  return [
    ...ueberblick,
    !m && eigene.length ? el('section', { class: 'lr-karte-box lr-jgstand' },
      el('p', { class: 'lr-ueber' }, `MEIN STAND · ${(LERN_SCHULART[sa] || '').toUpperCase()} KLASSE ${kind.klasse}`),
      el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${gel} von ${eigene.length} Flügen gelandet` }, el('span', { style: `width:${Math.round(100 * gel / eigene.length)}%` })),
        el('b', {}, `${gel} von ${eigene.length} Flügen`)),
      el('p', { class: 'lr-leise' }, `${gel} gelandet · ${lauf} unterwegs · ${eigene.length - gel - lauf} warten`)) : null,
    el('div', { class: 'lr-zahlen' }, zahl(kann.length, 'kann ich', 'gut'), zahl(aktOrt ? 1 : 0, 'gerade dran'), zahl(restOrte.length + passt.length, 'kommen noch')),
    el('h2', { class: 'lr-abschnitt lr-abschnitt-jetzt' }, 'GERADE DRAN'),
    ...(dran.length ? dran : [el('p', { class: 'lr-leise' }, 'Gerade ist nichts offen.')]),
    el('h2', { class: 'lr-abschnitt' }, 'KOMMT NOCH'),
    restOrte.length ? el('div', { class: 'lr-wegliste lr-kommt' }, ...restOrte.map((b) => { const o = d.orte.find((x) => x.block_id === b) || {}; const fl = offenJetzt.filter((e) => e.block_id === b);
      return ortZeile({ ...o, titel: o.titel || fl[0]?.ort_titel || fl[0]?.titel || '', stadt: o.stadt || fl[0]?.stadt || '', ziel_klasse: d.ortKlasse?.(b) || o.ziel_klasse }, `${fl.length} ${fl.length === 1 ? 'Flug' : 'Flüge'}`); })) : null,
    passt.length ? el('div', { class: 'lr-wegliste' }, ...passt.map((o) => ortZeile(o, 'bald'))) : null,
    // M9: verständlich für ein Kind
    !passt.length && kind.klasse ? el('p', { class: 'lr-leise' }, `Alles aus Klasse ${kind.klasse} steht schon in deinem Plan.`) : null,
    d.frueher.length ? el('details', { class: 'lr-mehr' }, el('summary', {}, `Aus früheren Klassen – zum Auffrischen (${d.frueher.length})`), el('div', { class: 'lr-wegliste' }, ...d.frueher.map(flugZeile))) : null,
    d.spaeter.length || spaeterOrte.length ? el('details', { class: 'lr-mehr' }, el('summary', {}, `Später – für höhere Klassen (${d.spaeter.length + spaeterOrte.length})`),
      el('div', { class: 'lr-wegliste' }, ...d.spaeter.map(flugZeile), ...spaeterOrte.map((o) => ortZeile(o, o.ziel_klasse ? 'Kl. ' + o.ziel_klasse : '')))) : null,
    el('h2', { class: 'lr-abschnitt' }, 'KANN ICH'),
    kannZeilen.length ? el('div', { class: 'lr-wegliste' }, ...kannZeilen.slice(0, 6)) : el('p', { class: 'lr-leise' }, 'Dein erster geschaffter Ort erscheint hier.'),
    kannZeilen.length > 6 ? el('details', { class: 'lr-mehr' }, el('summary', {}, `Alle ${kannZeilen.length} anzeigen`), el('div', { class: 'lr-wegliste' }, ...kannZeilen.slice(6))) : null,
  ];
}

// Kontinente: je Kontinent eine Karte mit eigenem Fortschritt, aufklappbar zu den Flügen.
function lernWegKontinente(d) {
  const { kind } = d; const sa = kind.schulart || 'gym_by';
  const reihe = new Map(); (d.orte || []).forEach((o) => { if (!reihe.has(o.kontinent_titel)) reihe.set(o.kontinent_titel, { erdteil: o.erdteil, n: reihe.size }); });
  const gruppen = new Map();
  for (const e of d.mit) { const k = e.kontinent || 'Weitere'; if (!gruppen.has(k)) gruppen.set(k, []); gruppen.get(k).push(e); }
  const liste = [...gruppen].sort((a, b) => (reihe.get(a[0])?.n ?? 99) - (reihe.get(b[0])?.n ?? 99));
  if (!liste.length) return [el('p', { class: 'lr-leise' }, 'Deine Reise ist noch nicht geplant.')];
  const zustand = (e) => lernGelandet(e) ? 'gelandet' : e.laeuft ? 'Test läuft' : e.fertig ? `${e.fertig}/${e.n} Etappen` : e.gruppe === 'spaeter' ? `ab Kl. ${e.jahrgang?.[sa] ?? e.ziel_klasse ?? ''}`.trim() : 'wartet';
  return [el('div', { class: 'lr-kontinente' }, ...liste.map(([k, es]) => {
    const zaehlen = es.filter((e) => e.gruppe !== 'spaeter'); const gel = zaehlen.filter(lernGelandet).length;
    const erdteil = reihe.get(k)?.erdteil || es[0]?.erdteil || '';
    return el('details', { class: 'lr-karte-box lr-kontinent', ...(es.some((e) => e === d.naechste) ? { open: '' } : {}) },
      el('summary', {},
        el('span', { class: 'lr-kontinent-kopf' }, el('small', { class: 'lr-ueber' }, erdteil.toUpperCase()), el('b', {}, k)),
        zaehlen.length ? el('span', { class: 'lr-kontinent-stand' }, el('b', {}, `${gel}/${zaehlen.length}`), el('small', {}, 'gelandet'))
          : el('span', { class: 'lr-kontinent-stand' }, el('small', {}, 'später')),
        el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${gel} von ${zaehlen.length} Flügen gelandet` }, el('span', { style: `width:${zaehlen.length ? Math.round(100 * gel / zaehlen.length) : 0}%` }))),
      el('div', { class: 'lr-wegliste' }, ...es.map((e) => el('a', { class: 'lr-wegzeile' + (e.gruppe === 'spaeter' ? ' lr-spaeter' : ''), href: `#/lerneinheit/${kind.id}-${e.id}` },
        el('span', { class: 'lr-wegzeile-icon ' + (lernGelandet(e) ? 'fertig' : '') }, lernGelandet(e) ? lernIcon(LI.haken, 16) : null),
        el('span', { class: 'lr-zeile-text' }, el('b', {}, e.titel), el('small', {}, [e.stadt, (e.jahrgang?.[sa] ?? e.ziel_klasse) ? 'Kl. ' + (e.jahrgang?.[sa] ?? e.ziel_klasse) : ''].filter(Boolean).join(' · '))),
        el('span', { class: 'lr-zeile-zustand' }, zustand(e))))));
  }))];
}

// Karte: nur die Orte der eigenen Klasse, mit Route; Antarktis als Polarkarte von oben.
const lernOrtInKlasse = (d, o, kl) => { const ks = d.ortKlassen?.(o.block_id); return ks ? ks.has(kl) : o.ziel_klasse === kl; };
function lernWegKarte(d) {
  const { kind } = d;
  // P2: dieselbe Regel wie „Stand“ – ein Ort gehört zur Klasse, wenn ein geplanter Flug dort jahrgang[schulart] = Stufe des Kindes hat (ohne Angaben: block.ziel_klasse)
  const st = lernStufe(kind, kind.schulart || 'gym_by');
  const orte = st ? d.orte.filter((o) => lernOrtInKlasse(d, o, st)) : d.orte;
  if (!orte.length) return [el('p', { class: 'lr-leise' }, kind.klasse ? `Für Klasse ${kind.klasse} sind noch keine Orte geplant.` : 'Deine Reise ist noch nicht geplant.')];
  const pos = new Map((kind.route || []).filter((r) => r.status !== 'entfernt').map((r) => [r.block_id, r.position]));
  const reise = [...orte].sort((a, b) => (pos.get(a.block_id) ?? 1e9) - (pos.get(b.block_id) ?? 1e9));
  const konts = [...new Map(reise.map((o) => [o.kontinent, o])).values()];
  const zaehl = (k) => { const os = reise.filter((o) => o.kontinent === k); return [os.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann').length, os.length]; };
  let wahl = reise.find((o) => o.zustand === 'jetzt')?.kontinent || konts[0]?.kontinent;
  const detail = el('section', { class: 'lr-karte-box' });
  const zeigeKontinent = () => {
    const os = reise.filter((o) => o.kontinent === wahl); const k0 = os[0] || {};
    const pol = k0.erdteil === 'Antarktis';
    lernErsetze(detail,
      el('p', { class: 'lr-ueber' }, `${(k0.erdteil || '').toUpperCase()} · ${(k0.kontinent_titel || '').toUpperCase()}`),
      os.length ? el('div', { class: 'lr-kartenbild' + (pol ? ' lr-polar' : '') }, pol ? lernPolarKarte(os) : lernKarte({ orte: os, fokus: os, hervor: LERN_ERDTEIL[wahl], route: true,
        beschriftung: os.filter((o) => o.zustand === 'jetzt').map((o) => ({ ...o, text: o.stadt, jetzt: true })), label: `Karte ${k0.erdteil}`, breite: 340, hoehe: 150 })) : null,
      el('ol', { class: 'lr-ortliste' }, ...os.map((o, i) => {
        const einheit = (d.mit || []).find((x) => x.block_id === o.block_id);
        const innen = [el('span', { class: 'lr-nr' }, o.zustand === 'fertig' || o.zustand === 'kann' ? lernIcon(LI.haken, 16) : String(i + 1)),
          el('span', { class: 'lr-zeile-text' }, el('b', {}, `${o.stadt}: ${o.titel}`), el('small', {}, einheit ? o.land : `${o.land} · kommt bald`)),
          el('span', { class: 'lr-zeile-zustand' }, { fertig: 'Stempel', kann: 'kann schon', jetzt: 'jetzt', offen: einheit ? '›' : '' }[o.zustand])];
        return el('li', { class: 'lr-ort-' + o.zustand }, einheit ? el('a', { class: 'lr-ortlink', href: `#/lerneinheit/${kind.id}-${einheit.id}` }, ...innen) : innen);
      })));
  };
  const knoepfe = el('div', { class: 'lr-chips', role: 'tablist', 'aria-label': 'Kontinente' });
  const zeichneKnoepfe = () => lernErsetze(knoepfe, ...konts.map((o) => {
    const [f, n] = zaehl(o.kontinent);
    return el('button', { type: 'button', role: 'tab', class: o.kontinent === wahl ? 'on' : '', 'aria-selected': String(o.kontinent === wahl),
      onclick: () => { wahl = o.kontinent; zeichneKnoepfe(); zeigeKontinent(); } }, `${o.kontinent_titel} `, el('small', {}, `${f}/${n}`));
  }));
  zeichneKnoepfe(); zeigeKontinent();
  const fertig = reise.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann').length;
  return [
    el('p', { class: 'lr-leise' }, `${kind.klasse ? `Klasse ${kind.klasse}: ` : ''}${fertig} von ${reise.length} Orten geschafft`),
    el('div', { class: 'lr-kartenbild lr-welt' }, lernKarte({ orte: reise.filter((o) => o.erdteil !== 'Antarktis'), route: true, label: `Weltkarte mit den Orten${kind.klasse ? ' der Klasse ' + kind.klasse : ''}` })),
    el('p', { class: 'lr-legende' }, el('span', { class: 'lr-dot lr-dot-fertig' }), 'geschafft', el('span', { class: 'lr-dot lr-dot-jetzt' }), 'jetzt dran', el('span', { class: 'lr-dot lr-dot-offen' }), 'noch offen'),
    knoepfe, detail];
}

// Antarktis von oben (Südpol in der Mitte, 0° oben): Umriss aus der Weltkarte zurückgerechnet (Natural Earth I umkehren) und azimutal neu gezeichnet.
function lernPolarKarte(orte) {
  const W = window.LERN_WELT; const ns = 'http://www.w3.org/2000/svg';
  const breite = (f) => { const f2 = f * f, f4 = f2 * f2; return f * (1.007226 + f2 * (0.015085 + f4 * (-0.044475 + 0.028874 * f2 - 0.005916 * f4))); };
  const laenge = (f) => { const f2 = f * f, f4 = f2 * f2; return 0.8707 - 0.131979 * f2 + f4 * (-0.013791 + f4 * (0.003971 * f2 - 0.001529 * f4)); };
  const zurueck = (x, y) => { const yy = (W.ty - y) / W.k; let f = yy; for (let i = 0; i < 25; i++) { const h = 1e-6; f -= (breite(f) - yy) / ((breite(f + h) - breite(f - h)) / (2 * h)); } return [((x - W.tx) / W.k) / laenge(f) * 180 / Math.PI, f * 180 / Math.PI]; };
  const S = 300, M = S / 2, R = M - 14, rand = 55; // Rand der Karte bei 55° Süd
  const polar = (lon, lat) => { const r = R * (90 + lat) / (90 - rand); const a = lon * Math.PI / 180; return [M + r * Math.sin(a), M - r * Math.cos(a)]; };
  const svg = document.createElementNS(ns, 'svg');
  svg.setAttribute('viewBox', `0 0 ${S} ${S}`); svg.setAttribute('class', 'lr-karte lr-karte-polar'); svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', 'Antarktis von oben, Südpol in der Mitte');
  const mk = (tag, a) => { const e = document.createElementNS(ns, tag); for (const [k, v] of Object.entries(a)) e.setAttribute(k, v); svg.append(e); return e; };
  mk('circle', { cx: M, cy: M, r: R + 8, class: 'lr-meer' });
  // Umriss: Punkte des Pfads; die künstliche Kante der Weltkarte (Breite < −85°) fällt weg
  let d = '';
  for (const teil of W.pfade.AN.split('M').filter(Boolean)) { // jede Teilfläche einzeln; Inseln jenseits des Kartenrands fallen weg
    const zahlen = (teil.match(/-?\d+(\.\d+)?/g) || []).map(Number); const pts = [];
    for (let i = 0; i + 1 < zahlen.length; i += 2) { const [lon, lat] = zurueck(zahlen[i], zahlen[i + 1]); if (lat >= -85) pts.push([lon, lat]); }
    if (pts.length < 3 || pts.some(([, lat]) => lat > -rand - 3)) continue;
    d += pts.map(([lon, lat], i) => { const [x, y] = polar(lon, lat); return `${i ? 'L' : 'M'}${x.toFixed(1)} ${y.toFixed(1)}`; }).join('') + 'Z';
  }
  mk('path', { d, class: 'lr-land lr-land-AN', 'fill-rule': 'evenodd' });
  for (const g of [-60, -70, -80]) mk('circle', { cx: M, cy: M, r: R * (90 + g) / (90 - rand), class: 'lr-polar-kreis' });
  mk('circle', { cx: M, cy: M, r: 2.5, class: 'lr-polar-pol' });
  const pts = orte.filter((o) => o.lat != null).map((o) => ({ o, p: polar(Number(o.lon), Number(o.lat)) }));
  if (pts.length > 1) mk('path', { d: 'M' + pts.map((q) => q.p.map((v) => v.toFixed(1)).join(' ')).join(' L'), class: 'lr-route', 'stroke-width': 2.4, 'stroke-dasharray': '2 6' });
  for (const { o, p } of pts) {
    mk('circle', { cx: p[0].toFixed(1), cy: p[1].toFixed(1), r: o.zustand === 'jetzt' ? 7 : 5, class: 'lr-punkt lr-punkt-' + (o.zustand || 'offen'), 'stroke-width': 1.6 });
    const t = mk('text', { x: (p[0] + (p[0] > M ? -9 : 9)).toFixed(1), y: (p[1] + 4).toFixed(1), class: 'lr-ortname' + (o.zustand === 'jetzt' ? ' lr-ortname-jetzt' : ''), 'font-size': 12, 'text-anchor': p[0] > M ? 'end' : 'start' }); t.textContent = o.stadt;
  }
  return svg;
}

// ---------- Kind: Merkheft (K2) – nur Geschafftes, Kontinent → Flug → Etappe, Suche oben ----------
async function viewMerkheft(arg) {
  setChrome('Merkheft', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const merk = await lernMerkDaten(d).catch(() => []);
  if (!live()) return;
  const { kind } = d;
  $('#title').textContent = 'Merkheft';
  const flug = new Map(d.mit.map((e) => [e.id, e]));
  const reihe = new Map((d.orte || []).map((o, i) => [o.block_id, i]));
  const eintraege = [];
  for (const m of merk) (m.etappen || []).forEach((e, i) => {
    const k = m.stand?.[e.lernziel] || {};
    if (!k.fertig && !k.sitzt) return; // nur Geschafftes
    const f = flug.get(m.einheit_id) || {};
    eintraege.push({ m, e, nr: i + 1, flug: f.titel || m.ort_titel || '', kontinent: f.kontinent || m.kontinent || 'Weitere', erdteil: f.erdteil || '', faellig: !!k.faellig });
  });
  eintraege.sort((a, b) => (reihe.get(a.m.block_id) ?? 999) - (reihe.get(b.m.block_id) ?? 999) || a.m.einheit_id - b.m.einheit_id || a.nr - b.nr);
  const suche = el('input', { type: 'search', class: 'lr-suche', placeholder: 'Suchen, z. B. runden', 'aria-label': 'Merkheft durchsuchen', autocomplete: 'off' });
  const liste = el('div', { class: 'lr-merkliste' });
  const norm = (s) => String(s || '').toLowerCase();
  const zeichne = () => {
    const q = norm(suche.value.trim());
    const treffer = eintraege.filter(({ m, e, flug: fl, kontinent }) => !q || [e.titel, e.regel, ...(e.schritte || []).map((x) => (typeof x === 'string' ? x : x?.text)), e.fehler, m.stadt, fl, kontinent].some((t) => norm(t).includes(q)));
    if (!eintraege.length) { lernErsetze(liste, el('p', { class: 'lr-leise' }, 'Noch leer. Sobald eine Etappe sitzt, steht ihre Erklärung hier.')); return; }
    if (!treffer.length) { lernErsetze(liste, el('p', { class: 'lr-leise' }, 'Nichts gefunden.')); return; }
    const konts = new Map();
    for (const t of treffer) { if (!konts.has(t.kontinent)) konts.set(t.kontinent, new Map()); const fl = konts.get(t.kontinent); if (!fl.has(t.m.einheit_id)) fl.set(t.m.einheit_id, []); fl.get(t.m.einheit_id).push(t); }
    lernErsetze(liste, ...[...konts].map(([k, fluege]) => el('section', { class: 'lr-merkgruppe' },
      el('h2', { class: 'lr-abschnitt' }, [[...fluege.values()][0][0].erdteil, k].filter(Boolean).join(' · ').toUpperCase()),
      ...[...fluege.values()].map((ts) => el('section', { class: 'lr-merkflug' },
        el('h3', { class: 'lr-merkflug-titel' }, ts[0].flug, el('small', {}, ' · ' + (ts[0].m.stadt || ''))),
        ...ts.map(({ m, e, nr, faellig }) => el('details', { class: 'lr-merk', ...(q && treffer.length <= 3 ? { open: '' } : {}) },
          el('summary', {}, el('b', {}, e.titel), el('small', { class: 'lr-merk-status' }, faellig ? 'Wiederholen' : 'sitzt'), lernIcon(LI.pfeil, 18)),
          el('div', { class: 'lr-merk-inhalt' }, lernErklaerung(e),
            el('a', { class: 'lr-knopf lr-knopf-klein', href: `#/lerneinheit/${kind.id}-${m.einheit_id}-ueben-${nr}` }, 'Üben')))))))));
  };
  suche.addEventListener('input', zeichne);
  zeichne();
  lernErsetze(main, lernRahmen(kind, 'merkheft',
    el('header', { class: 'lr-kopf' }, el('h1', { class: 'lr-titel' }, 'Merkheft'), el('p', { class: 'lr-leise' }, 'Was du geschafft hast – zum Nachlesen, jederzeit.')),
    eintraege.length ? suche : null, liste));
}

// ---------- Test ----------
const lernNtTitel = (nt) => nt.art === 'wiederholung' ? 'Nachtest wiederholen' : nt.folgerunde ? 'Weiterer Nachtest (bis alles sicher ist)' : `Nachtest ${nt.runde} von 3`;

function lernTestStart(ctx, body) {
  const box = el('div', { class: 'lern-test' });
  const stand = ctx.daten.stand || [];
  const offen = ctx.daten.laufender_test;
  const hatFehler = stand.some((s) => s.status === 'fehler');
  const blockFertig = ctx.daten.blocktest_fertig ?? stand.some((s) => s.status !== 'offen');
  const nt = ctx.daten.nachtest || {};
  const start = async (art) => {
    lernErsetze(box, el('div', { class: 'spinner' }, 'Test wird vorbereitet …'));
    try {
      const r = await lernCall('schule_test_starten', { lernender_id: ctx.kind, einheit_id: ctx.einheit, art });
      if (!ctx.live()) return;
      if (!r.ok) {
        const t = r.grund === 'noch_nicht_faellig' ? 'Der nächste Nachtest ist noch nicht dran. ' + (r.noch_nicht_faellig || []).map((x) => `Noch ${x.lerntage_noetig - x.lerntage_seit} Lerntage.`).join(' ')
          : r.grund === 'erst_korrektur' ? 'Erst die Etappen mit „noch üben“ verbessern, dann kommt der Nachtest.'
          : r.grund === 'vorrat_erschoepft' ? 'Für ' + (r.vorrat_erschoepft || []).map(lernZielName).join(', ') + ' gibt es gerade keine neue Bordkarte. Sag Bescheid, dann kommen neue dazu.'
          : 'Gerade gibt es nichts zu testen.';
        lernErsetze(box, el('p', { class: 'card' }, t)); return;
      }
      lernTestLauf(ctx, box, r);
    } catch (e) { lernErsetze(box, el('p', { class: 'card err-text' }, e.message)); }
  };
  const knopf = (t, art, text) => el('div', { class: 'card' }, el('h3', {}, t), el('p', { class: 'small' }, text),
    el('button', { type: 'button', class: 'primary', onclick: () => start(art) }, t + ' starten'));
  if (ctx.daten.verblasst) lernAnhaengen(box, el('p', { class: 'lern-hinweis' }, 'Rückreise: Diese Einheit sitzt noch nicht sicher. Erst verbessern, dann den Nachtest wiederholen.'));
  if (offen) lernAnhaengen(box, el('div', { class: 'card' }, el('h3', {}, 'Angefangener Test'), el('p', { class: 'small' }, 'Deine bisherigen Antworten sind gespeichert.'),
    el('button', { type: 'button', class: 'primary', onclick: () => start(offen.art) }, 'Weitermachen')));
  else {
    if (!blockFertig) lernAnhaengen(box, knopf('Test', 'blocktest', 'Eine Bordkarte je Etappe, ohne Tipps. Die Lösungen siehst du nach dem Abgeben.'));
    if (hatFehler) lernAnhaengen(box, knopf('Verbessern', 'korrektur', 'Nur die Etappen, die noch nicht geklappt haben – mit neuen Bordkarten. Übe sie vorher noch einmal.'));
    if (nt.grund === 'faellig') lernAnhaengen(box, knopf(lernNtTitel(nt), 'nachtest',
      'Alle Etappen des Flugs, ohne Tipps. Ab 80 % zählt die Runde. Unter 60 % geht es auf eine Rückreise zu diesem Ort.'));
    else if (nt.grund === 'noch_nicht_faellig') lernAnhaengen(box, el('div', { class: 'card' }, el('h3', {}, lernNtTitel(nt)),
      el('p', { class: 'small' }, `Dran in ${nt.lerntage_noetig - nt.lerntage_seit} Lerntag(en). Ein Lerntag zählt, wenn an dem Tag geübt oder getestet wurde.`)));
    if (nt.grund === 'gesichert') lernAnhaengen(box, el('p', { class: 'card' }, 'Alles geschafft und gesichert. 🎉'));
    if (!box.querySelector('.card')) lernAnhaengen(box, el('p', { class: 'card' }, 'Gerade gibt es keinen Test. Üb weiter!'));
  }
  return box;
}

function lernTestLauf(ctx, box, t) {
  const aufg = t.aufgaben || [];
  const antworten = new Map(); const gesendet = new Set(t.beantwortet || []);
  let i = Math.max(0, aufg.findIndex((a) => !gesendet.has(a.id)));
  const art = { blocktest: 'Test', korrektur: 'Verbessern', nachtest: 'Nachtest' }[t.art] || 'Test';
  const zeige = () => {
    const a = aufg[i]; const auf = lernAufgabe(a, antworten.get(a.id));
    const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
    const speichern = async () => {
      const w = auf.antwort();
      if (!w && auf.fehlerText()) { lernErsetze(meldung, el('p', { class: 'lern-hinweis' }, auf.fehlerText())); return null; }
      if (!w) return gesendet.has(a.id);
      const r = await lernCall('schule_test_antwort', { lernender_id: ctx.kind, sitzung_id: t.sitzung_id, aufgabe_id: a.id, antwort: w, client_id: lernCid() });
      if (!r.format_ok) { lernErsetze(meldung, el('p', { class: 'lern-hinweis' }, r.hinweis)); return null; }
      antworten.set(a.id, w); gesendet.add(a.id); return true;
    };
    const geh = async (d) => {
      try { const ok = await speichern(); if (ok === null) return; i = Math.min(aufg.length - 1, Math.max(0, i + d)); zeige(); }
      catch (e) { lernErsetze(meldung, el('p', { class: 'err-text' }, e.message)); }
    };
    const abgeben = el('button', { type: 'button', class: 'primary', onclick: async () => {
      try {
        const ok = await speichern(); if (ok === null) return;
        const fehlt = aufg.filter((x) => !gesendet.has(x.id)).length;
        if (fehlt && !abgeben.dataset.sicher) {
          const erste = aufg.findIndex((x) => !gesendet.has(x.id));
          lernErsetze(meldung, el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, fehlt === 1 ? 'Eine Bordkarte ist noch leer.' : `${fehlt} Bordkarten sind noch leer.`),
            el('p', {}, 'Leere Bordkarten zählen als falsch.'),
            el('div', { class: 'row' }, el('button', { type: 'button', class: 'primary', onclick: () => { i = erste; zeige(); } }, `Zu Bordkarte ${erste + 1}`),
              el('button', { type: 'button', class: 'secondary', onclick: () => { abgeben.dataset.sicher = '1'; abgeben.click(); } }, 'Trotzdem abgeben'))));
          return;
        }
        abgeben.disabled = true;
        const r = await lernCall('schule_test_abschliessen', { lernender_id: ctx.kind, sitzung_id: t.sitzung_id });
        if (ctx.live()) lernTestErgebnis(ctx, box, r);
      } catch (e) { abgeben.disabled = false; lernErsetze(meldung, el('p', { class: 'err-text' }, e.message)); }
    } }, 'Abgeben');
    lernErsetze(box, el('div', { class: 'card' },
      el('p', { class: 'eyebrow' }, `${art} · Bordkarte ${i + 1} von ${aufg.length} · ${gesendet.size} beantwortet`),
      el('div', { class: 'lern-punkte' }, aufg.map((x, j) => el('button', { type: 'button', class: (j === i ? 'on ' : '') + (gesendet.has(x.id) ? 'fertig' : ''), 'aria-label': `Bordkarte ${j + 1}`, onclick: () => { i = j; geh(0); } }, String(j + 1)))),
      auf.node, meldung,
      el('div', { class: 'row lern-knoepfe' },
        el('button', { type: 'button', class: 'secondary', disabled: i === 0, onclick: () => geh(-1) }, '‹ Zurück'),
        i < aufg.length - 1 ? el('button', { type: 'button', class: 'primary', onclick: () => geh(1) }, 'Weiter ›') : abgeben),
      i < aufg.length - 1 ? el('p', { class: 'small muted' }, 'Abgeben kannst du bei der letzten Bordkarte. Bis dahin kannst du Antworten ändern.') : null));
  };
  zeige();
}

function lernTestErgebnis(ctx, box, r) {
  const ort = r.ort || {};
  lernErsetze(box, 
    el('div', { class: 'card lern-ergebnis' },
      el('h3', {}, `${r.richtig} von ${r.gesamt} richtig`),
      r.einheit_abgeschlossen ? el('p', { class: 'lern-rueck ok' }, el('b', {}, 'Flug geschafft! 🎉')) : el('p', { class: 'small' }, 'Bei „noch üben“: die passenden Etappen noch einmal üben, dann „Verbessern“.'),
      r.nachtest_ergebnis ? el('p', { class: 'lern-rueck ' + (r.nachtest_ergebnis === 'bestanden' ? 'ok' : 'falsch') }, el('b', {}, {
        bestanden: r.nachtest?.folgerunde && r.nachtest_runde >= 3 ? 'Nachtest geschafft (ab 80 %).' : `Nachtest-Runde ${r.nachtest_runde} geschafft (ab 80 %).`,
        wiederholen: 'Unter 80 %: Diese Runde zählt noch nicht. Verbessere die falschen Etappen, dann kommt der Nachtest noch einmal.',
        rueckreise: 'Unter 60 %: Rückreise zu diesem Ort. Erst üben und verbessern, dann den Nachtest wiederholen.' }[r.nachtest_ergebnis])) : null,
      ort.abgeschlossen ? el('div', { class: 'lr-stempel-gross' }, el('div', { class: 'lr-stempel', style: '--dreh:-8deg' }, el('b', {}, 'GESCHAFFT'), el('small', {}, 'Neuer Stempel')),
        el('p', {}, el('b', {}, 'Ort geschafft! Der Stempel ist jetzt in deinem Reisepass.'))) : null,
      lernStandZeile(r.lernziele)),
    ...(r.ergebnisse || []).map((x) => {
      const a = { ...x, antworttyp: x.antworttyp || (x.loesung?.werte ? 'luecken' : x.loesung?.index !== undefined ? (x.antworten ? 'auswahl' : 'markierung') : x.loesung?.text !== undefined ? 'text' : 'zahl') };
      return el('div', { class: 'card lern-rueck-karte ' + (x.richtig ? 'ok' : 'falsch') },
        el('p', { class: 'eyebrow' }, lernZielName(x.lernziel) + (x.richtig ? ' · ✓ richtig' : ' · ✗ falsch')),
        el('p', { class: 'lern-frage' }, lernText(x.frage?.text)),
        x.frage?.grafik ? (x.frage.grafik.typ && x.frage.grafik.typ !== 'zahlenstrahl' ? lernBild(x.frage.grafik)
          : lernZahlenstrahl(a.antworttyp === 'markierung' ? { ...x.frage.grafik, _richtig: x.loesung?.index, _gewaehlt: x.antwort?.index } : x.frage.grafik, false)) : null,
        el('p', { class: 'small' }, 'Deine Antwort: ', el('b', {}, lernAntwortText(a, x.antwort))),
        x.richtig ? null : el('p', { class: 'small' }, 'Richtig: ', el('b', {}, lernLoesungText(a))),
        x.loesungsweg && !x.richtig ? el('p', { class: 'small muted' }, x.loesungsweg) : null);
    }),
    lernTestKnoepfe(ctx, r));
}
// N7: Knöpfe im Abflug-Stil. Bei „noch üben“: erst die Etappe üben, dann verbessern.
function lernTestKnoepfe(ctx, r) {
  const basis = ctx.basis || `#/lerneinheit/${ctx.kind}-${ctx.einheit}`;
  const etappen = ctx.daten?.inhalt?.etappen || [];
  const ueben = (r.lernziele || []).filter((s) => s.pflicht !== false && s.status === 'fehler');
  const erste = ueben[0]; const nr = erste ? etappen.findIndex((e) => e.lernziel === erste.lernziel) + 1 : 0;
  return el('div', { class: 'lr-knopfzeile lr-test-knoepfe' },
    erste ? el('a', { class: 'lr-knopf', href: nr ? `${basis}-ueben-${nr}` : `${basis}-ueben` }, `Erst üben: ${lernZielName(erste.lernziel)} ›`) : null,
    erste ? el('a', { class: 'lr-knopf-zweit', href: `${basis}-test` }, 'Verbessern ›') : null,
    el('a', { class: erste ? 'lr-textlink' : 'lr-knopf', href: basis }, erste ? 'Zum Flug' : 'Zum Flug ›'),
    el('a', { class: erste ? 'lr-textlink' : 'lr-knopf-zweit', href: `#/reise/${ctx.kind}` }, 'Zur Abflugtafel'));
}


// ---------- Eltern/Lehrer: Rückmeldungen, Themenplan, Zugänge ----------
const LERN_RM_ARTEN = [['thema_fehlt', 'Flug fehlt'], ['zu_ungenau', 'Zu ungenau'], ['mehr_aufgaben', 'Mehr Bordkarten'], ['schwieriger', 'Schwieriger'],
  ['leichter', 'Leichter'], ['erklaerung', 'Erklärung verbessern'], ['fehler', 'Fehler'], ['sonstiges', 'Sonstiges']];
const LERN_RM_STATUS = { offen: 'offen', in_arbeit: 'in Arbeit', erledigt: 'erledigt', abgelehnt: 'nicht umgesetzt' };

// ---------- E-3: „✎ Ändern lassen“ – derselbe Knopf an Erklärung, Etappe, Bordkarte, Flug und Plan; Liste „Meine Aufträge“ ----------
// Arten in der App → Art in der Datenbank (die Prüfbedingung der Tabelle bleibt unverändert); Vorlagen-Chips verfeinern die Art.
const LERN_AUFTRAG_ARTEN = [
  ['erklaerung', 'Erklärung', 'erklaerung', [['Zu ungenau', 'zu_ungenau'], ['Beispiel fehlt', 'erklaerung'], ['Bild hilft nicht', 'erklaerung']]],
  ['bordkarten', 'Bordkarten', 'mehr_aufgaben', [['Mehr Bordkarten', 'mehr_aufgaben'], ['Schwieriger', 'schwieriger'], ['Leichter', 'leichter']]],
  ['fehler', 'Fehler', 'fehler', [['Lösung falsch', 'fehler'], ['Bordkarte unklar', 'fehler'], ['Zeichnung falsch', 'fehler']]],
  ['neu', 'Neuer Flug', 'thema_fehlt', [['Flug fehlt', 'thema_fehlt'], ['Etappe fehlt', 'thema_fehlt']]],
  ['sonst', 'Sonstiges', 'sonstiges', [['Reihenfolge passt nicht', 'sonstiges'], ['Ort fehlt im Plan', 'thema_fehlt']]],
];
const LERN_AUFTRAG_START = { erklaerung: 'erklaerung', etappe: 'bordkarten', bordkarte: 'fehler', flug: 'bordkarten', plan: 'sonst', allgemein: 'neu' };
const LERN_BEZUG_TEXT = { erklaerung: 'Erklärung', etappe: 'Etappe', bordkarte: 'Bordkarte', flug: 'Flug', plan: 'Flugplan', allgemein: 'Allgemein' };
// daten: Bezugsfelder für schule_rueckmeldung_geben (einheit_id, lernziel, aufgabe_id, block_id, lernender_id). bezug: wo der Knopf steht.
function lernAuftragForm(daten, { bezug = 'allgemein', wo = '', art: artStart = null, text: textStart = '', onGesendet } = {}) {
  let artKey = artStart || LERN_AUFTRAG_START[bezug] || 'neu', dbArt = null;
  const arten = el('div', { class: 'lern-rm-arten', role: 'group', 'aria-label': 'Was soll sich ändern?' });
  const chips = el('div', { class: 'lern-rm-arten lern-rm-vorlagen', role: 'group', 'aria-label': 'Vorlagen' });
  const text = el('textarea', { rows: '3', maxlength: '4000', placeholder: 'Was soll anders sein?', 'aria-label': 'Was soll anders sein?' });
  text.value = textStart;
  const zeichne = () => {
    const a = LERN_AUFTRAG_ARTEN.find((x) => x[0] === artKey) || LERN_AUFTRAG_ARTEN[0];
    lernErsetze(arten, ...LERN_AUFTRAG_ARTEN.map(([k, t]) => el('button', { type: 'button', class: 'lern-chip', 'aria-pressed': String(k === artKey), onclick: () => { artKey = k; dbArt = null; zeichne(); } }, t)));
    lernErsetze(chips, ...a[3].map(([t, db]) => el('button', { type: 'button', class: 'lern-chip lern-chip-leise', 'aria-pressed': String(dbArt === db && text.value.startsWith(t)), onclick: () => {
      dbArt = db; if (!text.value.trim() || LERN_AUFTRAG_ARTEN.some((x) => x[3].some(([v]) => text.value.trim() === v + ':'))) text.value = t + ': '; text.focus(); zeichne(); } }, t)));
  };
  zeichne();
  const status = el('p', { class: 'small muted', role: 'status' });
  const senden = el('button', { type: 'submit', class: 'primary' }, 'Auftrag senden');
  const form = el('form', { class: 'lern-rm-form lern-auftrag-form' },
    wo ? el('p', { class: 'small lern-auftrag-bezug' }, el('b', {}, 'An: '), wo) : null,
    arten, chips, text, el('div', { class: 'row' }, senden, status));
  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const t = text.value.trim();
    if (!t || /^[^:]{1,40}:$/.test(t)) { status.textContent = 'Bitte in einem Satz sagen, was anders sein soll.'; return; }
    senden.disabled = true; status.textContent = 'Sende …';
    try {
      const a = LERN_AUFTRAG_ARTEN.find((x) => x[0] === artKey) || LERN_AUFTRAG_ARTEN[0];
      await lernCall('schule_rueckmeldung_geben', { ...daten, bezug, art: dbArt || a[2], text: t });
      text.value = ''; status.textContent = 'Danke – der Auftrag ist angekommen. Status und Antwort stehen unter „Meine Aufträge“.';
      if (onGesendet) onGesendet();
    } catch (err) { status.textContent = err.message; }
    senden.disabled = false;
  });
  return form;
}
// Der Knopf: aufklappbar, damit er auf jeder Seite wenig Platz braucht.
function lernAendern(daten, opt = {}) {
  return el('details', { class: 'lern-anmerkung lern-aendern' }, el('summary', {}, '✎ Ändern lassen'), lernAuftragForm(daten, opt));
}

async function viewRueckmeldungen() {
  setChrome('Meine Aufträge', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const r = await lernCall('schule_rueckmeldungen');
  if (!live()) return;
  const liste = r.rueckmeldungen || [];
  const artText = Object.fromEntries(LERN_RM_ARTEN);
  let filter = liste.some((x) => ['offen', 'in_arbeit'].includes(x.status)) ? 'offen' : 'alle';
  const bezugZeile = (x) => [x.bezug ? LERN_BEZUG_TEXT[x.bezug] : null, x.kind, x.flug || x.ort, x.etappe ? 'Etappe „' + x.etappe + '“' : x.lernziel ? 'Etappe ' + x.lernziel : null,
    x.aufgabe ? 'Bordkarte „' + x.aufgabe + '“' : null].filter(Boolean).join(' · ') || 'Allgemein';
  const karte = (x) => el('article', { class: 'card lern-rm lern-rm-' + x.status },
    el('div', { class: 'lern-einheit-kopf' }, el('b', {}, artText[x.art] || x.art), el('span', { class: 'pill' + (x.status === 'erledigt' ? ' ok' : x.status === 'offen' ? ' wartet' : '') }, LERN_RM_STATUS[x.status] || x.status)),
    el('p', { class: 'small muted' }, bezugZeile(x)),
    el('p', { class: 'lern-rm-text' }, x.text),
    x.antwort ? el('p', { class: 'lern-rm-antwort' }, el('b', {}, 'Antwort: '), x.antwort) : null,
    el('p', { class: 'small muted' }, `${String(x.von || '').replace(/^[a-z]+:/, '')} · ${new Date(x.am).toLocaleDateString('de-DE')}`));
  const box = el('div', { class: 'lern-auftraege' });
  const reiter = el('div', { class: 'lern-chips-zeile', role: 'group', 'aria-label': 'Filter' });
  const zeichne = () => {
    const zeigen = liste.filter((x) => filter === 'alle' || (filter === 'offen' ? ['offen', 'in_arbeit'].includes(x.status) : ['erledigt', 'abgelehnt'].includes(x.status)));
    lernErsetze(reiter, ...[['offen', 'Offen'], ['fertig', 'Beantwortet'], ['alle', 'Alle']].map(([k, t]) => el('button', { type: 'button', class: 'lern-chip', 'aria-pressed': String(filter === k), onclick: () => { filter = k; zeichne(); } },
      `${t} (${liste.filter((x) => k === 'alle' || (k === 'offen' ? ['offen', 'in_arbeit'].includes(x.status) : ['erledigt', 'abgelehnt'].includes(x.status))).length})`)));
    lernErsetze(box, ...(zeigen.length ? zeigen.map(karte) : [el('p', { class: 'muted' }, 'Hier ist nichts.')]));
  };
  zeichne();
  lernErsetze(main,
    lernInfoLink(),
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'AN DIE ENTWICKLUNG'), el('h2', {}, 'Meine Aufträge'),
      el('p', {}, 'Was ihr ändern lassen wollt, mit Status und Antwort. Zu einer bestimmten Erklärung, Etappe, Bordkarte oder einem Flug geht es direkt dort über „✎ Ändern lassen“; der Auftrag weiß dann, worum es geht.')),
    el('details', { class: 'card lern-anmerkung lern-aendern' }, el('summary', {}, '✎ Neuer Auftrag (allgemein)'), lernAuftragForm({}, { bezug: 'allgemein', onGesendet: () => setTimeout(render, 900) })),
    reiter, box);
}

async function viewPlan(arg) {
  setChrome('Flugplan', { back: true, showTabs: false });
  const live = viewGuard();
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return; }
  loading();
  const p = await lernCall('schule_plan_lesen', { lernender_id: kindId });
  if (!live()) return;
  $('#title').textContent = 'Flugplan ' + p.kind.name;
  const ortById = new Map((p.orte || []).map((o) => [o.block_id, o]));
  const normal = (p.plan || []).filter((r) => r.art === 'normal');
  const rueck = (p.plan || []).filter((r) => r.art === 'rueckreise');
  // E-2: Flüge im Ort abwählbar, sobald die Datenbank „ausgelassen“ speichert (Migration 20261117_w150_e2_*); sonst bleibt alles wie bisher.
  const kannAbwaehlen = !!p.kann_abwaehlen || normal.some((r) => Array.isArray(r.ausgelassen));
  // Arbeitskopie: [{ block_id, kann_schon, status, ausgelassen }]. E-1: Jede Änderung speichert sofort (mit revision), „Rückgängig“ holt den Zustand davor zurück.
  let plan = normal.map((r) => ({ block_id: r.block_id, kann_schon: r.kann_schon, status: r.status, ausgelassen: [...(r.ausgelassen || [])] }));
  let revision = p.revision;
  const kopie = (x) => x.map((y) => ({ ...y, ausgelassen: [...y.ausgelassen] }));
  const vorher = []; // Zustände vor den letzten Änderungen (neueste zuletzt)
  const offen = new Set(); // aufgeklappte Orte
  let laeuft = null, nochmal = false, gesperrt = false, rueckgaengig = false;
  const sa = p.kind.schulart || 'gym_by';
  const ortName = (o) => o ? `${o.stadt || o.titel}${o.stadt && o.titel !== o.stadt ? ' – ' + o.titel : ''}` : '?';
  const klasseVon = (o, s = 'gym_by') => Math.min(...(o?.themen || []).map((t) => Number(t.jahrgang?.[s]) || 99));
  const standText = { erledigt: 'geschafft', laeuft: 'läuft', offen: 'noch nicht begonnen' };

  // Kopfzeile (bleibt oben): Name, Speicherstand, „Rückgängig“ dauerhaft (Befund 4 der Nachprüfung E-1), „Ändern lassen“
  const stand = el('span', { class: 'lern-plan-stand', role: 'status', 'aria-live': 'polite' }, plan.length ? 'Alles gespeichert' : '');
  const rueckKnopf = el('button', { type: 'button', class: 'lern-plan-rueck', disabled: true, onclick: () => zuruecknehmen() }, '↶ Rückgängig');
  const meldung = el('div', { class: 'lern-plan-meldung', role: 'alert', hidden: true });
  const kopf = el('div', { class: 'lern-plan-kopf' },
    el('div', { class: 'lern-plan-kopf-text' }, el('b', {}, `Flugplan ${p.kind.name}`), stand), rueckKnopf, meldung);
  const melde = (...kids) => { meldung.hidden = !kids.length; lernErsetze(meldung, ...kids); };
  const sperren = () => { gesperrt = true; liste.inert = true; vorratSpalte.inert = true; liste.classList.add('lern-plan-gesperrt'); rueckKnopf.disabled = true; };
  const eintraege = () => plan.map((x) => ({ block_id: x.block_id, kann_schon: !!x.kann_schon, ...(kannAbwaehlen ? { ausgelassen: x.ausgelassen } : {}) }));
  const speichere = () => {
    if (gesperrt) return Promise.resolve();
    if (laeuft) { nochmal = true; return laeuft; }
    stand.textContent = 'Speichere …';
    laeuft = (async () => {
      try {
        do {
          nochmal = false;
          const r = await lernCall('schule_plan_setzen', { lernender_id: kindId, revision, eintraege: eintraege() });
          revision = r?.revision ?? revision + 1;
        } while (nochmal);
        stand.textContent = rueckgaengig ? 'Rückgängig gemacht · Gespeichert' : 'Gespeichert'; melde();
      } catch (err) {
        if (/inzwischen geändert/i.test(err.message)) {
          sperren(); stand.textContent = 'Nicht gespeichert';
          melde(el('span', {}, 'Der Plan wurde inzwischen von jemand anderem geändert. Deine letzte Änderung ist nicht gespeichert – es wird nichts überschrieben.'),
            el('button', { type: 'button', class: 'primary', onclick: () => render() }, 'Neu laden'));
        } else {
          stand.textContent = 'Nicht gespeichert';
          melde(el('span', {}, `Nicht gespeichert: ${err.message}`), el('button', { type: 'button', class: 'secondary', onclick: () => speichere() }, 'Erneut versuchen'));
        }
      } finally { laeuft = null; rueckgaengig = false; rueckKnopf.disabled = gesperrt || !vorher.length; }
    })();
    return laeuft;
  };
  const aendere = (fn) => {
    if (gesperrt) return;
    vorher.push(kopie(plan)); if (vorher.length > 30) vorher.shift();
    fn(); zeichne(); zeichneVorrat(); speichere();
  };
  function zuruecknehmen() {
    if (gesperrt || !vorher.length) return;
    plan = vorher.pop(); rueckgaengig = true; zeichne(); zeichneVorrat(); speichere();
  }

  // Linke Spalte: der Plan als kompakte Liste – ziehen am Griff ⠿ (Maus und Finger) oder ↑ ↓; aufgeklappt die Flüge mit „im Plan“
  const liste = el('ol', { class: 'lern-plan lern-plan-kompakt' });
  const fluegeListe = (o, x) => el('ul', { class: 'lern-plan-themen' }, ...(o?.themen || []).map((t) => {
    const z = lernInhaltZustand(t); const drin = !x || !x.ausgelassen.includes(t.thema_id);
    return el('li', { class: 'lp-' + z.k + (drin ? '' : ' lern-plan-aus') },
      x && kannAbwaehlen ? el('label', { class: 'lern-plan-im' }, el('input', { type: 'checkbox', checked: drin, 'aria-label': `${t.titel} im Plan`,
        onchange: (ev) => { const v = ev.target.checked; aendere(() => { const y = plan.find((q) => q.block_id === x.block_id); y.ausgelassen = v ? y.ausgelassen.filter((id) => id !== t.thema_id) : [...y.ausgelassen, t.thema_id]; }); } })) : el('i', { class: 'lp-punkt', 'aria-hidden': 'true' }),
      el('span', {}, el('b', {}, t.titel), el('span', { class: 'lern-plan-jg' }, ' · ' + (lernJahrgangText(t.jahrgang) || 'ohne Lehrplan-Zuordnung'))),
      el('small', { class: 'muted' }, !drin ? 'abgewählt' : z.k === 'leer' ? 'noch kein Inhalt' : z.k === 'pruefung' ? 'Inhalt in Prüfung' : (standText[t.stand] || 'Inhalt fertig')),
      t.einheit ? el('a', { class: 'small', href: `#/inhalte/${t.einheit.id}` }, 'ansehen') : null);
  }));
  const zeichne = () => {
    lernErsetze(liste, ...plan.map((x, i) => {
      const o = ortById.get(x.block_id); const themen = o?.themen || [];
      const geplant = themen.filter((t) => !x.ausgelassen.includes(t.thema_id));
      const gesch = geplant.filter((t) => t.stand === 'erledigt').length; const kl = klasseVon(o, sa);
      // M4: Ort, dessen geplante Flüge alle über der Klasse des Kindes liegen – sichtbar markieren; das Kind sieht ihn unter „Später“, außer er ist vorgezogen
      const klPlan = (y) => { const oo = ortById.get(y.block_id); const ks = (oo?.themen || []).filter((t) => !y.ausgelassen.includes(t.thema_id)).map((t) => Number(t.jahrgang?.[sa])).filter(Boolean); return ks.length ? Math.min(...ks) : null; };
      const klG = klPlan(x); const kk = Number(p.kind.klasse) || 0;
      const ueber = kk && klG && klG > kk;
      const vorgezogen = ueber && plan.slice(i + 1).some((y) => { const k2 = klPlan(y); return k2 && k2 <= kk; });
      const auf = offen.has(x.block_id);
      const griff = el('span', { class: 'lern-plan-griff', role: 'button', 'aria-label': `${ortName(o)} ziehen`, title: 'Ziehen zum Umsortieren' }, '⠿');
      griff.addEventListener('pointerdown', (ev) => ziehen(ev, i));
      const li = el('li', { class: 'lern-plan-zeile' + (x.status === 'fertig' ? ' fertig' : '') + (auf ? ' offen' : ''), 'data-block': String(x.block_id) },
        griff,
        el('span', { class: 'lern-plan-nr' }, String(i + 1)),
        el('button', { type: 'button', class: 'lern-plan-ort', 'aria-expanded': String(auf), onclick: () => { if (auf) offen.delete(x.block_id); else offen.add(x.block_id); zeichne(); } },
          el('b', {}, ortName(o)),
          el('small', {}, [o?.kontinent, kl < 99 ? `${{ gym_by: 'Gym', rs_by: 'RS', ib_myp: 'MYP' }[sa] || 'Gym'} ${kl}` : null,
            `${gesch}/${geplant.length} ${geplant.length === 1 ? 'Flug' : 'Flüge'}`, x.ausgelassen.length ? `${x.ausgelassen.length} abgewählt` : null,
            x.status === 'fertig' ? 'geschafft' : x.kann_schon ? 'kann schon' : null].filter(Boolean).join(' · ')),
          ueber && x.status !== 'fertig' ? el('small', { class: 'lern-plan-ueber' }, `Klasse ${klG} – über der Klasse des Kindes · ${vorgezogen ? 'vorgezogen' : 'Kind sieht ihn unter „Später“'}`) : null),
        el('span', { class: 'lern-plan-pfeile' },
          el('button', { type: 'button', class: 'iconbtn', 'aria-label': `${ortName(o)} nach oben`, disabled: i === 0, onclick: () => aendere(() => { [plan[i - 1], plan[i]] = [plan[i], plan[i - 1]]; }) }, '↑'),
          el('button', { type: 'button', class: 'iconbtn', 'aria-label': `${ortName(o)} nach unten`, disabled: i === plan.length - 1, onclick: () => aendere(() => { [plan[i + 1], plan[i]] = [plan[i], plan[i + 1]]; }) }, '↓')),
        auf ? el('div', { class: 'lern-plan-detail' },
          fluegeListe(o, x),
          kannAbwaehlen ? null : el('p', { class: 'small muted' }, 'Einzelne Flüge abwählen geht, sobald die Datenbank dafür bereit ist.'),
          el('div', { class: 'row' },
            el('label', { class: 'lern-plan-kann' }, el('input', { type: 'checkbox', checked: !!x.kann_schon, onchange: (ev) => { const v = ev.target.checked; aendere(() => { plan[i].kann_schon = v; }); } }), ' kann es schon'),
            el('button', { type: 'button', class: 'lern-plan-weg', 'aria-label': `${ortName(o)} aus dem Plan nehmen`, onclick: () => aendere(() => { plan.splice(i, 1); offen.delete(x.block_id); }) }, 'Entfernen'))) : null);
      return li;
    }));
    if (!plan.length) lernAnhaengen(liste, el('li', { class: 'muted lern-plan-leer' }, 'Der Plan ist leer. Ohne Plan sieht das Kind alle Flüge. Füge rechts (auf dem Handy unten) Orte hinzu.'));
  };
  // Ziehen im Plan: Pointer-Ereignisse (Maus, Finger, Stift). Die anderen Zeilen rücken sichtbar zur Seite; losgelassen wird einmal gespeichert.
  const ziehen = (ev, i) => {
    if (gesperrt || (ev.button !== undefined && ev.button !== 0)) return;
    ev.preventDefault();
    const zeilen = [...liste.querySelectorAll(':scope > .lern-plan-zeile')]; const li = zeilen[i]; if (!li) return;
    const mitten = zeilen.map((z) => { const b = z.getBoundingClientRect(); return b.top + window.scrollY + b.height / 2; });
    const h = li.getBoundingClientRect().height + 6; const start = ev.clientY + window.scrollY; let ziel = i, rollen = null;
    li.classList.add('zieht'); liste.classList.add('beim-ziehen');
    const lauf = (cy) => {
      const dy = cy + window.scrollY - start; li.style.transform = `translateY(${dy}px)`;
      const mitte = mitten[i] + dy; ziel = zeilen.reduce((n, z, j) => n + (j !== i && mitten[j] < mitte ? 1 : 0), 0);
      zeilen.forEach((z, j) => { if (j === i) return; z.style.transform = j > i && j <= ziel ? `translateY(${-h}px)` : j < i && j >= ziel ? `translateY(${h}px)` : ''; });
    };
    let y = ev.clientY;
    const bewegt = (e) => { y = e.clientY; lauf(y); clearInterval(rollen); rollen = null;
      const rand = 60; if (y < rand || y > window.innerHeight - rand) rollen = setInterval(() => { window.scrollBy(0, y < rand ? -12 : 12); lauf(y); }, 16); };
    const ende = () => {
      clearInterval(rollen); window.removeEventListener('pointermove', bewegt); window.removeEventListener('pointerup', ende); window.removeEventListener('pointercancel', ende);
      zeilen.forEach((z) => { z.style.transform = ''; }); li.classList.remove('zieht'); liste.classList.remove('beim-ziehen');
      if (ziel !== i) aendere(() => plan.splice(ziel, 0, plan.splice(i, 1)[0]));
    };
    window.addEventListener('pointermove', bewegt); window.addEventListener('pointerup', ende); window.addEventListener('pointercancel', ende);
  };

  // Rechte Spalte: der Lehrplan nach Schulart und Klasse – Orte mit „+“ anhängen oder in den Plan ziehen
  let vSa = sa, vKl = String(p.kind.klasse || '');
  const vorrat = el('div', { class: 'lern-plan-vorrat' });
  const suche = el('input', { type: 'search', placeholder: 'Flug oder Ort suchen …', 'aria-label': 'Flug oder Ort suchen' });
  const saWahl = el('select', { 'aria-label': 'Schulart' }, ...Object.entries(LERN_SCHULART).map(([k, t]) => el('option', { value: k, selected: k === vSa }, t)));
  const klWahl = el('select', { 'aria-label': 'Klasse' });
  const fuelleKlassen = () => lernErsetze(klWahl, el('option', { value: '' }, 'alle Klassen'),
    ...Array.from({ length: vSa === 'ib_myp' ? 5 : 6 }, (_, j) => { const k = vSa === 'ib_myp' ? j + 1 : j + 5; return el('option', { value: String(k), selected: String(k) === vKl }, (vSa === 'ib_myp' ? 'MYP ' : 'Klasse ') + k); }));
  saWahl.addEventListener('change', () => { vSa = saWahl.value; vKl = ''; fuelleKlassen(); zeichneVorrat(); });
  klWahl.addEventListener('change', () => { vKl = klWahl.value; zeichneVorrat(); });
  suche.addEventListener('input', () => zeichneVorrat());
  fuelleKlassen();
  const einfuegen = (blockId, an = plan.length) => aendere(() => plan.splice(an, 0, { block_id: blockId, kann_schon: false, status: 'offen', ausgelassen: [] }));
  const zeichneVorrat = () => {
    const q = suche.value.trim().toLowerCase(); const drin = new Set(plan.map((x) => x.block_id));
    const passt = (o) => (o.themen || []).length && !drin.has(o.block_id) && (!vKl || (o.themen || []).some((t) => String(t.jahrgang?.[vSa]) === vKl))
      && (!q || `${o.stadt} ${o.titel} ${o.kontinent} ${(o.themen || []).map((t) => t.titel).join(' ')}`.toLowerCase().includes(q));
    const treffer = (p.orte || []).filter(passt).sort((a, b) => klasseVon(a, vSa) - klasseVon(b, vSa));
    lernErsetze(vorrat, ...treffer.map((o) => {
      const griff = el('span', { class: 'lern-plan-griff', role: 'button', 'aria-label': `${ortName(o)} in den Plan ziehen`, title: 'In den Plan ziehen' }, '⠿');
      griff.addEventListener('pointerdown', (ev) => hineinziehen(ev, o));
      return el('div', { class: 'lern-plan-vorrat-zeile' }, griff,
        el('span', { class: 'lern-plan-ort' }, el('b', {}, ortName(o)), el('small', {}, [o.kontinent, klasseVon(o, vSa) < 99 ? `${vSa === 'ib_myp' ? 'MYP' : 'Kl.'} ${klasseVon(o, vSa)}` : null, `${(o.themen || []).length} ${(o.themen || []).length === 1 ? 'Flug' : 'Flüge'}`].filter(Boolean).join(' · '))),
        el('button', { type: 'button', class: 'lern-chip', 'aria-label': `+ ${ortName(o)}`, onclick: () => einfuegen(o.block_id) }, '+'));
    }));
    if (!treffer.length) lernAnhaengen(vorrat, el('p', { class: 'muted small' }, 'Keine weiteren Orte für diese Auswahl.'));
  };
  // Aus dem Lehrplan in den Plan ziehen: ein Abbild folgt dem Zeiger; losgelassen über dem Plan wird an der Stelle eingefügt.
  const hineinziehen = (ev, o) => {
    if (gesperrt || (ev.button !== undefined && ev.button !== 0)) return;
    ev.preventDefault();
    const bild = el('div', { class: 'lern-plan-geist' }, ortName(o)); document.body.append(bild);
    const zeilen = [...liste.querySelectorAll(':scope > .lern-plan-zeile')];
    const stelle = (cy) => zeilen.filter((z) => { const b = z.getBoundingClientRect(); return b.top + b.height / 2 < cy; }).length;
    const ueberPlan = (cx, cy) => { const b = liste.getBoundingClientRect(); return cx >= b.left && cx <= b.right && cy >= b.top - 30 && cy <= b.bottom + 40; };
    const lauf = (e) => { bild.style.transform = `translate(${e.clientX + 8}px, ${e.clientY - 18}px)`; liste.classList.toggle('ziel', ueberPlan(e.clientX, e.clientY)); };
    lauf(ev);
    const ende = (e) => {
      window.removeEventListener('pointermove', lauf); window.removeEventListener('pointerup', ende); window.removeEventListener('pointercancel', ende);
      bild.remove(); liste.classList.remove('ziel');
      if (e.type === 'pointerup' && ueberPlan(e.clientX, e.clientY)) einfuegen(o.block_id, stelle(e.clientY));
    };
    window.addEventListener('pointermove', lauf); window.addEventListener('pointerup', ende); window.addEventListener('pointercancel', ende);
  };
  const vorratSpalte = el('section', { class: 'card lern-plan-lehrplan' }, el('h3', {}, 'Lehrplan'),
    el('div', { class: 'row' }, saWahl, klWahl), suche, vorrat,
    lernAendern({ lernender_id: kindId }, { bezug: 'plan', wo: `Flugplan ${p.kind.name}`, art: 'sonst' }));

  const notiz = el('textarea', { rows: '2', maxlength: '2000', placeholder: 'Notiz zum Kind (z. B. Prüfung am …, braucht mehr Zeit bei …)', 'aria-label': 'Notiz' });
  const notizStatus = el('span', { class: 'small muted', role: 'status' });
  const notizForm = el('form', { class: 'lern-rm-form' }, notiz, el('div', { class: 'row' }, el('button', { type: 'submit', class: 'secondary' }, 'Notiz speichern'), notizStatus));
  notizForm.addEventListener('submit', async (ev) => {
    ev.preventDefault(); if (!notiz.value.trim()) return;
    try { await lernCall('schule_notiz_setzen', { lernender_id: kindId, text: notiz.value.trim() }); notizStatus.textContent = 'Gespeichert.'; setTimeout(render, 700); }
    catch (err) { notizStatus.textContent = err.message; }
  });
  zeichne(); zeichneVorrat();
  // E-4: Neuer Plan aus Lehrplan-Vorlage – Schulart und Klasse wählen; der Plan wird durch die Orte dieser Klasse in Lehrplan-Reihenfolge ersetzt
  // (themen[].lehrplan_reihenfolge, Migration D; fehlt sie: Reihenfolge der Orte im Lehrplan). Flüge anderer Klassen werden abgewählt, wenn die Datenbank das kann.
  const vorlage = lernPlanVorlage(p, kannAbwaehlen, (neuerPlan) => aendere(() => { const alt = new Map(plan.map((x) => [x.block_id, x]));
    plan.splice(0, plan.length, ...neuerPlan.map((x) => ({ ...x, kann_schon: alt.get(x.block_id)?.kann_schon || false, status: alt.get(x.block_id)?.status || 'offen' }))); }));
  // M2: Klasse und Stufen speichern sofort wie der Plan – kein eigener Knopf
  const auswahl = (wert, label, leer, name) => el('select', { 'aria-label': label, name }, el('option', { value: '' }, leer),
    ...Array.from({ length: 13 }, (_, j) => el('option', { value: String(j + 1), selected: Number(wert) === j + 1 }, String(j + 1))));
  const klIn = auswahl(p.kind.klasse, 'Klasse des Kindes', '–', 'klasse');
  const kindStatus = el('span', { class: 'small muted', role: 'status', 'aria-live': 'polite' });
  const stufenDa = p.kind.stufen !== undefined;
  const stufeIn = stufenDa ? Object.fromEntries(LERN_SYS.map((y) => [y.sa, auswahl(p.kind.stufen?.[y.sa], 'Stufe ' + y.name, `aus Klasse (${lernStufe({ ...p.kind, stufen: {} }, y.sa) || '–'})`, 'stufe-' + y.sa)])) : {};
  const kindSpeichern = async () => {
    const daten = { lernender_id: kindId, klasse: Number(klIn.value) || null };
    if (stufenDa) daten.stufen = Object.fromEntries(LERN_SYS.map((y) => [y.sa, Number(stufeIn[y.sa].value) || null]));
    kindStatus.textContent = 'Speichere …';
    try {
      await lernCall('schule_kind_setzen', daten); kindStatus.textContent = 'Gespeichert';
      p.kind.klasse = daten.klasse; if (stufenDa) p.kind.stufen = Object.fromEntries(Object.entries(daten.stufen).filter(([, v]) => v));
      zeichne();
      if (stufenDa) for (const y of LERN_SYS) stufeIn[y.sa].options[0].textContent = `aus Klasse (${lernStufe({ ...p.kind, stufen: {} }, y.sa) || '–'})`;
    } catch (err) { kindStatus.textContent = 'Nicht gespeichert: ' + err.message; }
  };
  klIn.addEventListener('change', kindSpeichern); for (const x of Object.values(stufeIn)) x.addEventListener('change', kindSpeichern);
  const kindForm = el('section', { class: 'card lp-kindform' }, el('h3', {}, 'Klasse'),
    el('div', { class: 'row' }, el('label', { class: 'small' }, 'Klasse ', klIn), kindStatus),
    el('p', { class: 'small muted' }, `${LERN_SCHULART[sa] || 'Gymnasium'}. Bestimmt, welche Flüge beim Kind als „seine Klasse“ zählen. Wird sofort gespeichert.`),
    // K3/E-4: Stufe je Schulart für den Lernstand (Kontinente × Klassen) – nur, wenn die Datenbank sie liefert (kind.stufen, Migration D)
    ...(stufenDa ? [el('p', { class: 'small' }, el('b', {}, 'Stufe je Schulart'), el('span', { class: 'muted' }, ' – für den Lernstand; „aus Klasse“ = Klasse, IB MYP = Klasse − 4')),
      el('div', { class: 'row lp-stufen' }, ...LERN_SYS.map((y) => el('label', { class: 'small' }, y.name + ' ', stufeIn[y.sa])))] : []));
  lernErsetze(main, ...[
    lernInfoLink(),
    kopf,
    el('p', { class: 'small muted lern-plan-hilfe' }, 'Reihenfolge = Reihenfolge in der Lernreise. Ziehen am Griff ⠿ oder ↑ ↓; einen Ort antippen zeigt seine Flüge',
      kannAbwaehlen ? ' – dort lassen sich einzelne Flüge abwählen.' : '.', ' Jede Änderung wird sofort gespeichert.'),
    rueck.length ? el('p', { class: 'card small' }, `Automatische Rückreise: ${rueck.map((r) => ortName(ortById.get(r.block_id))).join(', ')} – wird zuerst wiederholt, bis der Nachtest bestanden ist.`) : null,
    el('div', { class: 'lern-plan-spalten' }, el('div', { class: 'lern-plan-links' }, liste), vorratSpalte),
    vorlage,
    kindForm,
    el('section', { class: 'card' }, el('h3', {}, 'Notizen'), notizForm,
      ...(p.notizen || []).map((n) => el('p', { class: 'small' }, el('b', {}, String(n.von || '').replace(/^[a-z]+:/, '') + ': '), n.text, el('span', { class: 'muted' }, ' · ' + new Date(n.am).toLocaleDateString('de-DE'))))),
    (p.verlauf || []).length ? el('details', { class: 'card' }, el('summary', {}, 'Verlauf'),
      ...(p.verlauf || []).map((v) => el('p', { class: 'small muted' }, `${new Date(v.am).toLocaleString('de-DE')} · ${String(v.akteur).replace(/^[a-z]+:/, '')} · ${v.anlass === 'plan' ? 'Plan geändert' : v.anlass === 'rueckreise' ? 'Rückreise nach Test' : v.anlass}`))) : null].filter(Boolean));
}

// Info-Seite „So funktioniert’s“: oben rechts auf der Startseite der Eltern/Lehrer und im Flugplan.
const lernInfoLink = () => el('div', { class: 'lern-info-oben' }, el('a', { class: 'lern-info-link', href: '#/info' }, 'ⓘ So funktioniert’s'));

// E-4: Karte „Neuer Plan aus Lehrplan-Vorlage“ im Flugplan. ersetze(neuerPlan) übernimmt den Vorschlag (mit „Rückgängig“).
function lernPlanVorlage(p, kannAbwaehlen, ersetze) {
  let vSa = p.kind.schulart || 'gym_by';
  const startKl = () => String(lernStufe(p.kind, vSa) || '');
  const saWahl = el('select', { 'aria-label': 'Vorlage Schulart' }, ...LERN_SYS.map((y) => el('option', { value: y.sa, selected: y.sa === vSa }, y.name)));
  const klWahl = el('select', { 'aria-label': 'Vorlage Klasse' });
  const vorschau = el('div', { class: 'lern-vorlage-vorschau small' });
  const knopf = el('button', { type: 'button' }, 'Plan ersetzen');
  const y = () => LERN_SYS.find((q) => q.sa === vSa);
  const fuelle = (kl) => lernErsetze(klWahl, ...y().stufen.map((n) => el('option', { value: String(n), selected: String(n) === kl }, y().label(n))));
  const reihe = (t) => Number(t.lehrplan_reihenfolge?.[vSa]) || null;
  const vorschlag = () => {
    const kl = Number(klWahl.value);
    const passt = (t) => Number(t.jahrgang?.[vSa]) === kl;
    const orte = (p.orte || []).map((o, i) => ({ o, i, ts: (o.themen || []).filter(passt) })).filter((x) => x.ts.length);
    const min = (x) => Math.min(...x.ts.map((t) => reihe(t) ?? 999));
    orte.sort((a, b) => min(a) - min(b) || a.i - b.i);
    return orte.map((x) => ({ block_id: x.o.block_id, ausgelassen: kannAbwaehlen ? (x.o.themen || []).filter((t) => !passt(t)).map((t) => t.thema_id) : [], ort: x.o, ts: x.ts }));
  };
  const zeige = () => {
    const v = vorschlag(); const mitReihe = v.some((x) => x.ts.some((t) => reihe(t) !== null));
    const fluege = v.reduce((z, x) => z + x.ts.length, 0);
    knopf.disabled = !v.length; knopf.textContent = v.length ? `Plan ersetzen (${v.length} ${v.length === 1 ? 'Ort' : 'Orte'})` : 'Plan ersetzen';
    lernErsetze(vorschau, v.length ? el('p', {}, `${v.length} Orte mit ${fluege} Flügen für ${lernSysVoll(y(), Number(klWahl.value))}` + (mitReihe ? ', in Lehrplan-Reihenfolge' : ', Reihenfolge wie im Lehrplan-Verzeichnis (genaue Lehrplan-Reihenfolge fehlt für diese Schulart)') + '.',
        kannAbwaehlen ? ' Flüge anderer Klassen in diesen Orten werden abgewählt.' : ' Andere Flüge in diesen Orten bleiben drin.') : el('p', { class: 'muted' }, 'Für diese Auswahl gibt es noch keine Orte mit Inhalt.'),
      v.length ? el('ol', { class: 'lern-vorlage-liste' }, ...v.map((x) => el('li', {}, `${x.ort.stadt || x.ort.titel}: `, x.ts.map((t) => t.titel).join(', ')))) : null);
  };
  saWahl.addEventListener('change', () => { vSa = saWahl.value; fuelle(startKl()); zeige(); });
  klWahl.addEventListener('change', zeige);
  knopf.addEventListener('click', () => ersetze(vorschlag().map(({ block_id, ausgelassen }) => ({ block_id, ausgelassen }))));
  fuelle(startKl()); zeige();
  return el('details', { class: 'card lern-vorlage' }, el('summary', {}, el('b', {}, 'Neuer Plan aus Lehrplan-Vorlage')),
    el('p', { class: 'small muted' }, 'Ersetzt den ganzen Plan durch die Orte einer Klasse – nur Orte mit Inhalt. Geschaffte Orte bleiben geschafft; „Rückgängig“ holt den alten Plan zurück.'),
    el('div', { class: 'row' }, saWahl, klWahl, knopf), vorschau);
}

// ---------- Eltern/Lehrer: Stand über Schularten (K4) – drei Ebenen ----------
// #/schulstand                                   Ebene 1: „Alle Kinder im Vergleich“ – alle Kinder × drei Schularten
// #/lernstand/<kind>[-<schulart>][-<ziel>]       Ebene 2: „Lernstand <Name>“ – Lehrplan-Landkarte (Kontinente × Klassen), Schalter „Einstieg prüfen: Klasse X“
//                                                (Zusatz 1 zu F: der Knopf „Lernstand“ an der Kinderkarte führt direkt hierher, in der Schulart des Kindes)
// #/lernstand/<kind>-<schulart>-<ziel>-<k>-<kl>  Ebene 3: Flüge eines Feldes mit dem Stand der Etappen (inkl. Bordkarten bis „sitzt“)
// Alte Adressen #/schulstand/<kind>-… zeigen dieselbe Seite.
const LERN_ORIENTIERUNG = 'Orientierung, keine Einstufung durch eine Schule.';
const viewLernstand = (arg) => viewSchulstand(arg, true);
async function viewSchulstand(arg, alsLernstand = false) {
  setChrome(alsLernstand ? 'Lernstand' : 'Alle Kinder im Vergleich', { back: true, showTabs: false });
  const live = viewGuard();
  const [kidArg, saRoh, zielArg, kontArg, klArg] = String(arg || '').split('-');
  loading();
  const u = await lernCall('schule_uebersicht');
  if (!live()) return;
  const kinder = (u.lernende || []).filter((k) => !k.ist_test);
  const modelle = new Map(kinder.map((k) => [k.id, lernStandModell(u, k)]));
  const kind = kinder.find((k) => k.id === Number(kidArg));
  const saArg = saRoh || (kind ? kind.schulart || 'gym_by' : undefined); // „Lernstand“ ohne Schulart: die Schulart des Kindes
  const y = LERN_SYS.find((q) => q.sa === saArg);
  const krumen = (teile) => el('nav', { class: 'lern-krumen', 'aria-label': 'Pfad' }, ...teile.flatMap(([t, h], i) => i < teile.length - 1 ? [el('a', { href: h }, t), el('span', { 'aria-hidden': 'true' }, '›')] : [el('b', {}, t)]));
  const kopf = el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'ELTERN UND LEHRER'), el('h2', {}, 'Alle Kinder im Vergleich'),
    el('p', {}, 'Wie weit jedes Kind in Gymnasium, Realschule und IB MYP ist – gezählt werden alle Flüge, die laut Lehrplan in die jeweilige Klasse gehören.'));
  const hinweisFluege = modelle.size && ![...modelle.values()][0].alleFluege ? el('p', { class: 'small muted' }, 'Gezählt werden vorerst nur Flüge mit Inhalt; alle Flüge kommen, sobald die Datenbank sie liefert.') : null;
  // Ebene 1
  if (!kind || !y) {
    if (alsLernstand && kidArg) { route('schulstand'); return; } // unbekanntes Kind
    $('#title').textContent = 'Alle Kinder im Vergleich';
    lernErsetze(main, lernInfoLink(), kopf,
      el('div', { class: 'lern-tabelle-rollen' }, el('table', { class: 'lern-stand-raster lern-stand-ueber' },
        el('thead', {}, el('tr', {}, el('th', {}, ''), ...LERN_SYS.map((q) => el('th', { style: `color:${q.farbe}` }, q.name)))),
        el('tbody', {}, ...kinder.map((k) => { const m = modelle.get(k.id);
          return el('tr', {}, el('th', { scope: 'row' }, k.name), ...LERN_SYS.map((q) => { const n = m.stufe(q.sa); const c = m.zahl(q.sa, n);
            const w = m.themen.filter((t) => n && Number(t.jahrgang?.[q.sa]) <= n && t.st === 'wackelt').length;
            return el('td', {}, el('a', { class: 'lern-stand-feld', href: `#/lernstand/${k.id}-${q.sa}`, 'aria-label': `${k.name}, ${n ? lernSysVoll(q, n) : q.name}: ${c.f} von ${c.n} gelandet` },
              el('b', {}, n ? q.label(n) : '–'), el('span', { class: 'lern-mini-balken', style: `--f:${q.farbe}` }, el('i', { style: `width:${lernPz(c.f, c.n)}%;background:${q.farbe}` })),
              el('small', {}, `${c.f}/${c.n}`, w ? el('span', { class: 'lern-wackelt' }, ` · ${w} wackelt`) : null))); })); })))),
      el('p', { class: 'small muted' }, 'Feld antippen → Lehrplan-Landkarte dieses Kindes in dieser Schulart, mit „Einstieg prüfen“. Die Stufe je Schulart setzt ihr im Flugplan.'), hinweisFluege);
    return;
  }
  const m = modelle.get(kind.id); const ziel = Number(zielArg) || null;
  const basis = `#/lernstand/${kind.id}-${y.sa}`;
  $('#title').textContent = 'Lernstand ' + kind.name; // Zusatz 1 zu F
  const lsKopf = el('section', { class: 'start-intro lern-lernstand-kopf' }, el('p', { class: 'eyebrow' }, `${(LERN_SCHULART[kind.schulart || 'gym_by'] || '').toUpperCase()}${kind.klasse ? ' · KLASSE ' + kind.klasse : ''}`),
    el('h2', {}, 'Lernstand ' + kind.name),
    el('p', { class: 'small' }, el('a', { href: `#/wackelt/${kind.id}` }, 'Was wackelt? – Etappen mit den echten falschen Antworten ›')));
  const konts = [...new Set(m.themen.map((t) => t.kontinent))].sort(lernKontReihe);
  const reiter = el('div', { class: 'lern-chips-zeile', role: 'group', 'aria-label': 'Schulart' }, ...LERN_SYS.map((q) => el('a', { class: 'lern-chip', href: `#/lernstand/${kind.id}-${q.sa}`, 'aria-current': q.sa === y.sa ? 'page' : null }, q.name)));
  const check = el('div', { class: 'lern-chips-zeile', role: 'group', 'aria-label': 'Einstieg prüfen' }, el('span', { class: 'small' }, 'Einstieg prüfen:'),
    ...[null, ...y.stufen.slice(1)].map((n) => el('a', { class: 'lern-chip', href: n ? `${basis}-${n}` : basis, 'aria-current': (ziel || null) === n ? 'page' : null }, n ? (y.sa === 'ib_myp' ? 'MYP ' : 'Kl. ') + n : 'aus')));
  const davor = ziel ? m.themen.filter((t) => Number(t.jahrgang?.[y.sa]) && Number(t.jahrgang[y.sa]) < ziel) : [];
  const fehlt = davor.filter((t) => t.st !== 'ok'); const p = lernPz(davor.length - fehlt.length, davor.length);
  const ampel = ziel ? el('div', { class: 'lern-ampel ' + (p >= 90 ? 'gruen' : p >= 70 ? 'gelb' : 'rot'), role: 'status' }, el('b', {}, p + ' %'),
    el('span', {}, `Einstieg ${lernSysVoll(y, ziel)}: ${davor.length - fehlt.length} von ${davor.length} Flügen bis ${y.label(ziel - 1)} gelandet. ${p >= 90 ? 'Bereit – kleine Lücken.' : p >= 70 ? 'Fast – gezielt nacharbeiten.' : 'Noch deutliche Lücken.'}`,
      el('small', {}, ' ' + LERN_ORIENTIERUNG))) : el('p', { class: 'small muted' }, `„Einstieg prüfen“ zeigt, was bis zu einer Klasse fehlt. ${LERN_ORIENTIERUNG}`);
  const flugZeile = (t, extra) => el('div', { class: 'lern-standflug lr-st-' + t.st },
    el('span', { class: 'lr-standpunkt', 'aria-hidden': 'true' }, lernSymbol(t.st)),
    el('span', {}, el('b', {}, t.titel), el('small', { class: 'muted' }, [t.stadt, lernZaehltAuch(t, y.sa) ? 'zählt auch für ' + lernZaehltAuch(t, y.sa) : null, t.ausgelassen ? 'im Plan abgewählt' : null, !t.einheit ? 'noch kein Inhalt' : null].filter(Boolean).join(' · ')), extra || null),
    el('span', { class: 'small' }, { ok: 'gelandet', jetzt: 'jetzt dran', wackelt: 'wackelt', laeuft: 'läuft', offen: 'offen' }[t.st]));
  const k = konts[Number(kontArg)]; const kl = Number(klArg);
  if (kontArg !== undefined && k && kl) {
    // Ebene 3: Flüge des Feldes mit dem Stand der Etappen
    const ts = m.themen.filter((t) => t.kontinent === k && Number(t.jahrgang?.[y.sa]) === kl);
    const ls = await lernCall('schule_lernstand', { lernender_id: kind.id }).catch(() => null);
    if (!live()) return;
    const proEinheit = new Map((ls?.einheiten || []).map((e) => [e.einheit_id, e]));
    lernErsetze(main, lernInfoLink(), krumen([['Alle Kinder', '#/schulstand'], [`Lernstand ${kind.name} · ${y.name}`, ziel ? `${basis}-${ziel}` : basis], [`${k} · ${y.label(kl)}`, null]]),
      el('section', { class: 'card' }, el('h3', {}, `${k} · ${y.label(kl)}`),
        ...ts.map((t) => { const e = t.einheit ? proEinheit.get(t.einheit.id) : null;
          return flugZeile(t, e ? el('ul', { class: 'lern-etappen-stand' }, ...(e.karten || []).map((x) => el('li', {}, el('span', {}, x.titel || x.lernziel),
            el('small', { class: 'muted' }, lernEtappeStandText(x))))) : null); }),
        ts.length ? null : el('p', { class: 'muted' }, 'Keine Flüge in diesem Feld.')),
      el('p', {}, el('a', { href: `#/wackelt/${kind.id}` }, `Was wackelt? – ${kind.name} mit den echten falschen Antworten ›`)));
    return;
  }
  // Ebene 2: Landkarte Kontinente × Klassen
  const farbe = (ts) => { const f = ts.filter((t) => t.st === 'ok').length; const q = lernPz(f, ts.length);
    return [f, q === 100 ? 'alles' : q > 0 ? 'teil' : ts.some((t) => t.st === 'jetzt' || t.st === 'laeuft') ? 'laeuft' : 'offen']; };
  const ich = m.stufe(y.sa);
  const raster = el('table', { class: 'lern-stand-raster' },
    el('thead', {}, el('tr', {}, el('th', {}, ''), ...y.stufen.map((n) => el('th', { class: (ich === n ? 'ich' : '') + (ziel && n < ziel ? ' pruef' : '') }, (y.sa === 'ib_myp' ? 'MYP ' : 'Kl. ') + n)))),
    el('tbody', {}, ...konts.map((kn, ki) => el('tr', {}, el('th', { scope: 'row' }, kn, el('small', {}, m.themen.find((t) => t.kontinent === kn)?.erdteil || '')),
      ...y.stufen.map((n) => { const ts = m.themen.filter((t) => t.kontinent === kn && Number(t.jahrgang?.[y.sa]) === n); if (!ts.length) return el('td', { class: 'leer' }, '·');
        const [f, art] = farbe(ts); const w = ts.some((t) => t.st === 'wackelt');
        return el('td', {}, el('a', { class: `lern-zelle z-${art}${w ? ' w' : ''}${ziel && n >= ziel ? ' aus' : ''}`, href: `${basis}-${ziel || 0}-${ki}-${n}`, 'aria-label': `${kn}, ${y.label(n)}: ${f} von ${ts.length} gelandet${w ? ', wackelt' : ''}` }, `${f}/${ts.length}`)); }))),
      el('tr', { class: 'summe' }, el('th', { scope: 'row' }, 'Gesamt'), ...y.stufen.map((n) => { const c = m.zahl(y.sa, n); return el('td', {}, c.n ? lernPz(c.f, c.n) + ' %' : '–'); }))));
  lernErsetze(main, lernInfoLink(), lsKopf, krumen([['Alle Kinder im Vergleich', '#/schulstand'], [`Lernstand ${kind.name} · ${y.name}`, null]]),
    el('section', { class: 'card' }, reiter, check, ampel,
      el('div', { class: 'lern-tabelle-rollen' }, raster),
      el('p', { class: 'lern-legende small' }, ...[['offen', 'offen'], ['laeuft', 'läuft'], ['teil', 'teilweise'], ['alles', 'alles gelandet'], ['w', 'wackelt']].map(([c2, t]) => el('span', {}, el('i', { class: 'z-' + c2 }), t))),
      ziel && fehlt.length ? el('details', { class: 'lern-fehlt' }, el('summary', {}, `Für den Einstieg fehlen (${fehlt.length})`), ...fehlt.map((t) => flugZeile(t))) : null,
      el('p', { class: 'small muted' }, 'Feld antippen → Flüge in diesem Kontinent und dieser Klasse, mit dem Stand der Etappen.'), hinweisFluege));
}
// K4: Stand einer Etappe in Worten – mit der Zahl der Bordkarten bis „sitzt“ (schule_lernstand.bis_sitzt, Migration D)
function lernEtappeStandText(x) {
  if (x.sitzt) return x.bis_sitzt ? `sitzt – nach ${x.bis_sitzt} ${x.bis_sitzt === 1 ? 'Bordkarte' : 'Bordkarten'}` : 'sitzt';
  if (!x.richtig && !x.falsch) return 'noch nicht geübt';
  return `${x.serie || 0} von ${x.ziel || 6} Punkten · ${x.richtig} richtig, ${x.falsch} falsch`;
}

// ---------- Eltern/Lehrer: Info-Seite „So funktioniert’s“ (E-1). Text aus inhalte/pruefung/eltern/info-seite.md, gegen den Code geprüft (Stand 0.75.1). ----------
// Ändert sich eine Regel aus „Wie wird gelernt?“ (Etappe sitzt, Wiederholung, Tests), diesen Text im selben Schritt anpassen.
const LERN_INFO_FRAGEN = [
  ['Worauf baut die App auf?', [
    'Die App deckt Mathematik für drei Schularten ab: Gymnasium Bayern (LehrplanPLUS, Klassen 5–10), Realschule Bayern (LehrplanPLUS, Klassen 5–10) und das IB Middle Years Programme (MYP 1–4).',
    'Grundlage ist eine Liste aller Mathe-Flüge (über 90). Für jeden Flug ist hinterlegt, in welcher Klasse er in welcher Schulart dran ist, z. B. „Ganze Zahlen: Gym 5 · RS 5 · IB 2“. Die Lehrplan-Übersicht zeigt alle Flüge.',
    'Ein Kind lernt jeden Flug nur einmal; er zählt für alle Schularten.']],
  ['Wie ist die Lernreise aufgebaut?', [
    ['Kontinent', ' = ein Bereich der Mathematik (Zahlen = Europa, Geometrie = Afrika …)'],
    ['Ort', ' = eine Stadt mit einem oder mehreren Flügen. Sind alle Flüge eines Ortes geschafft, gibt es einen Stempel.'],
    ['Flug', ' = ein Mathe-Thema, z. B. „Ganze Zahlen“'],
    ['Etappe', ' = ein Lernschritt mit eigener Erklärung'],
    ['Bordkarte', ' = eine Übungsaufgabe'],
    'Jede Etappe hat eine Erklärung (Alltagseinstieg, neue Wörter, Beispiel Schritt für Schritt, typischer Fehler, Merksatz) und im Schnitt etwa 20 Bordkarten in drei Stufen.',
    ['Drei Stufen = drei Arten zu denken:', ' ● leicht – wie im Beispiel oder etwas erkennen; ●● mittel – mehrere Schritte, eine Sachaufgabe, umgekehrt gefragt oder die Darstellung wechseln; ●●● schwer – rückwärts rechnen, mit früherem Stoff verknüpfen, begründen, einen Fehler finden, ein Modell selbst aufstellen oder mit einer Variablen statt einer Zahl. Schwer heißt also ein anderer Gedanke, nicht größere Zahlen. Das Zeichen steht im Kopf jeder Bordkarte; unter „Inhalte ansehen“ steht bei jeder Bordkarte auch ihre Art.'],
    ['Knobel-Bordkarten:', ' freiwillige Zusatzaufgaben auf Wettbewerbsniveau. Sie erscheinen, wenn eine Etappe sitzt, und höchstens einmal am Tag als „Knobeln des Tages“. Ein Versuch; falsch kostet nichts und zeigt den Lösungsweg. Richtig beim ersten Versuch: 30 Sterne und ein Knobel-Stern im Reisepass. Sie zählen nicht für „sitzt“, Wiederholung oder Test.']]],
  ['Wie wird gelernt?', [
    ['Neue Etappe:', ' Zuerst kommt die Erklärung, danach die Bordkarten.'],
    ['Zweiter Versuch:', ' Bei einem Fehler gibt es zuerst einen zweiten Versuch, ohne Lösung (nicht bei Auswahl-Bordkarten mit nur zwei Antworten). Erst wenn auch er falsch ist, zeigt die App Lösung und Lösungsweg.'],
    ['Etappe sitzt:', ' nach 6 Punkten. Richtig im ersten Versuch ohne Tipp: +1 Punkt; Fehler: −2 Punkte; richtig im zweiten Versuch oder mit Tipp: kein Punkt. Zusätzlich muss mindestens eine schwere Bordkarte im ersten Versuch richtig sein (falls die Etappe schwere hat). Hat eine Etappe nur wenige Bordkarten, reichen entsprechend weniger Punkte, mindestens 2. Mit den Punkten steigt die Stufe: erst leicht, dann mittel, dann schwer.'],
    ['Wiederholung:', ' Sitzt eine Etappe, kommt sie nach 1, 3, 7, 14 und 30 Lerntagen wieder, jeweils mit einer Bordkarte. Ein Lerntag ist ein Tag, an dem das Kind Mathe übt; Reisetage ohne Mathe zählen nicht. Vor einem Flug kommen höchstens 6 Wiederholungen, weitere werden nur angeboten. Ein Fehler: Die Etappe kommt am nächsten Lerntag wieder. Zwei Fehler hintereinander: Das Kind übt sie noch einmal.'],
    ['Flug-Test:', ' wenn alle Etappen sitzen; eine Bordkarte je Etappe, ohne Tipps. Etappen mit Fehlern werden danach verbessert („Verbessern“).'],
    ['Nachtests:', ' später, nach Lerntagen gezählt (nach 10, 25 und 60 Lerntagen); alle Etappen des Flugs, ohne Tipps. Ab 80 %: bestanden. 60–79 %: wiederholen. Unter 60 %: automatische Rückreise im Flugplan.'],
    ['Belohnungen:', ' 10 Sterne für jede Bordkarte, die zum ersten Mal richtig ist, 20 Sterne für jede richtige Bordkarte im Test, 30 Sterne für eine Knobel-Bordkarte beim ersten Versuch, 100 Sterne und ein Stempel für jeden geschafften Ort. Welche Belohnungen es gibt, legen die Eltern fest, und sie bestätigen jede Einlösung.'],
    'Keine Zeitvorgaben, keine Uhr, keine Ranglisten.']],
  ['Wie entstehen die Inhalte, und wer prüft sie?', [
    'Erklärungen und Bordkarten erstellt eine KI (Claude) nach festen Regeln: Bezug zum Lehrplan, Alltagseinstieg, einfache Sprache, jede Lösung vom Programm berechnet und geprüft.',
    'Ein neuer Flug ist zuerst „in Prüfung“: Nur das Testkind sieht ihn. Nach der Freigabe ist er „fertig“ und für alle Kinder da. Die Lehrplan-Übersicht zeigt den Stand: grau = noch kein Inhalt, gelb = in Prüfung, grün = fertig.',
    'Jeder Inhalt ist mit allen Lösungen einsehbar („Inhalte ansehen“).']],
  ['Was kann ich selbst ändern?', [
    ['Flugplan je Kind:', ' Reihenfolge der Orte (am Griff ⠿ ziehen oder ↑ ↓), Orte aus dem Lehrplan hinzufügen (ziehen oder „+“) oder entfernen, „kann es schon“. Einen Ort antippen zeigt seine Flüge; einzelne Flüge lassen sich dort abwählen – ein abgewählter Flug fehlt in der Lernreise des Kindes und zählt nicht für den Stempel. Jede Änderung wird sofort gespeichert; „↶ Rückgängig“ oben im Flugplan holt den Stand davor zurück. Hat jemand anderes den Plan inzwischen geändert, meldet die App das und überschreibt nichts – dann neu laden.'],
    ['Klasse des Kindes', ' (im Flugplan)'],
    ['Notizen zum Kind', ' (im Flugplan)'],
    ['Lernstand:', ' die Lehrplan-Landkarte des Kindes (Kontinente × Klassen) mit „Einstieg prüfen“; ein Feld antippen zeigt Flüge und Etappen.'],
    ['Was wackelt?:', ' was sitzt und was wackelt, je Etappe mit den echten falschen Antworten.'],
    'Inhalte werden nicht direkt geändert, sondern beauftragt (nächste Frage). Belohnungen und Zugänge verwalten nur Eltern.']],
  ['Wie beauftrage ich eine Änderung?', [
    'An der betroffenen Stelle „✎ Ändern lassen“ tippen – derselbe Knopf an Erklärung, Etappe, Bordkarte, Flug und Flugplan; der Auftrag weiß dann, worum es geht. An einzelnen Bordkarten steht er in der Lernreise eines Kindes (am einfachsten beim Testkind). Für Flüge ohne Inhalt steht er in der Lehrplan-Übersicht, mit „Neuer Flug“ vorbelegt. Allgemeine Wünsche: „Meine Aufträge“ → „Neuer Auftrag“.',
    'Art wählen (Erklärung, Bordkarten, Fehler, Neuer Flug, Sonstiges), bei Bedarf eine Vorlage antippen (z. B. „Schwieriger“, „Lösung falsch“) und in einem Satz sagen, was anders sein soll.',
    'Die Entwicklung (Eltern mit KI) bearbeitet den Auftrag. Status: offen → in Arbeit → erledigt oder nicht umgesetzt, jeweils mit Antwort – alles unter „Meine Aufträge“.',
    'Neue Antworten stehen auf der Startseite unter „Neue Antworten auf eure Aufträge“.',
    'Gute Aufträge nennen ein Beispiel: „Bordkarte 7: Lösung muss −56 sein“ statt „Fehler im Flug“.']],
  ['Wer hat Zugang, und wie steht es um den Datenschutz?', [
    'Ein Lern-Code öffnet nur den Bereich Lernen; für alle anderen Bereiche der App lehnt der Server ihn ab. Eltern legen Codes an (für Lehrer, Eltern oder ein Kind) und können sie jederzeit sperren. Ein Kind-Code öffnet nur die eigene Lernreise.',
    'Code und Link getrennt weitergeben.']],
];

async function viewInfo() {
  setChrome('So funktioniert’s', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const u = await lernCall('schule_uebersicht').catch(() => null);
  if (!live()) return;
  const kinder = (u?.lernende || []).filter((k) => !k.ist_test);
  const jeKind = (pfad, wort) => kinder.length ? el('div', { class: 'lern-info-links' }, ...kinder.map((k) => el('a', { href: `#/${pfad}/${k.id}` }, `${wort} ${k.name} ›`)))
    : el('a', { href: '#/lernen' }, 'Zur Startseite ›');
  const schritt = (nr, titel, text, ...ziel) => el('article', { class: 'card lern-info-schritt' },
    el('span', { class: 'lern-info-nr', 'aria-hidden': 'true' }, String(nr)), el('h3', {}, titel), el('p', { class: 'small' }, text), ...ziel);
  const zeile = (x) => Array.isArray(x) ? el('li', {}, el('b', {}, x[0]), x[1]) : el('li', {}, x);
  lernErsetze(main,
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'FÜR ELTERN UND LEHRER'), el('h2', {}, 'So funktioniert’s'),
      el('p', {}, 'Die Lernreise in Kürze: erst die vier wichtigsten Schritte, darunter Antworten auf die häufigsten Fragen.')),
    el('h3', {}, 'Erste Schritte'),
    el('div', { class: 'lern-info-schritte' },
      schritt(1, 'Flugplan prüfen', 'Lege fest, welche Orte das Kind in welcher Reihenfolge bereist (ziehen oder ↑ ↓), wähle Flüge ab, die nicht dran sind, und hake ab, was es schon kann. Neu anfangen: „Neuer Plan aus Lehrplan-Vorlage“. Jede Änderung wird sofort gespeichert.', jeKind('plan', 'Flugplan')),
      schritt(2, 'Lernstand lesen', '„Lernstand“ an der Kinderkarte: die Lehrplan-Landkarte des Kindes (Kontinente × Klassen) in seiner Schulart, mit „Einstieg prüfen“ (Orientierung, keine Einstufung durch eine Schule). „Was wackelt?“: je Etappe, was sitzt und was wackelt, mit den echten falschen Antworten. Alle Kinder nebeneinander: „Alle Kinder im Vergleich“.', jeKind('lernstand', 'Lernstand'), jeKind('wackelt', 'Was wackelt?'), el('a', { href: '#/schulstand' }, 'Alle Kinder im Vergleich ›')),
      schritt(3, 'Inhalte ansehen', 'In der Lehrplan-Übersicht unter „Inhalte ansehen“: jede Etappe mit ihrer Erklärung und alle Bordkarten mit Lösung.', el('a', { href: '#/lehrplan' }, 'Lehrplan-Übersicht ›')),
      schritt(4, 'Ändern lassen', 'Fehlt etwas oder stimmt etwas nicht? Mit „✎ Ändern lassen“ direkt an der Stelle beauftragen; Status und Antwort stehen unter „Meine Aufträge“.', el('a', { href: '#/lernauftraege' }, 'Meine Aufträge ›'))),
    el('h3', {}, 'Fragen'),
    ...LERN_INFO_FRAGEN.map(([frage, teile], i) => el('details', { class: 'card lern-info-frage' },
      el('summary', {}, frage), el('ul', {}, ...teile.map(zeile)))));
}

async function viewZugaenge() {
  setChrome('Zugänge', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const [z, u] = await Promise.all([lernCall('schule_zugaenge'), lernCall('schule_uebersicht')]);
  if (!live()) return;
  const rollenText = { eltern: 'Eltern', lehrer: 'Lehrer', kind: 'Kind' };
  const name = el('input', { type: 'text', maxlength: '60', placeholder: 'Name, z. B. Herr Müller', 'aria-label': 'Name' });
  const rolle = el('select', { 'aria-label': 'Rolle' }, el('option', { value: 'lehrer' }, 'Lehrer – alle Flüge, Flugplan, Rückmeldungen'),
    el('option', { value: 'eltern' }, 'Eltern – zusätzlich Belohnungen und Zugänge'), el('option', { value: 'kind' }, 'Kind – nur die eigene Lernreise'));
  const kind = el('select', { 'aria-label': 'Kind', hidden: true }, ...(u.lernende || []).filter((k) => !k.ist_test).map((k) => el('option', { value: k.id }, k.name)));
  rolle.addEventListener('change', () => { kind.hidden = rolle.value !== 'kind'; });
  const status = el('div', { role: 'status' });
  const form = el('form', { class: 'card lern-rm-form' }, el('h3', {}, 'Neuen Zugang anlegen'), name, rolle, kind, el('button', { type: 'submit', class: 'primary' }, 'Code erzeugen'), status);
  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!name.value.trim()) { lernErsetze(status, el('p', { class: 'small' }, 'Bitte einen Namen eingeben.')); return; }
    try {
      const r = await lernCall('schule_zugang_anlegen', { name: name.value.trim(), rolle: rolle.value, lernender_id: rolle.value === 'kind' ? Number(kind.value) : null });
      const link = new URL(typeof LERN_SEITE !== 'undefined' ? './' : 'lernen/', location.href).href.replace(/#.*$/, '');
      lernErsetze(status, el('div', { class: 'lern-code-box' },
        el('p', {}, el('b', {}, 'Code (wird nur jetzt angezeigt):')), el('p', { class: 'lern-code' }, r.code),
        el('p', { class: 'small' }, 'Anmelden unter: ', el('a', { href: link, target: '_blank', rel: 'noopener' }, link)),
        el('p', { class: 'small muted' }, 'Code und Link getrennt oder persönlich weitergeben. Verloren? Zugang sperren und neu anlegen.')));
      name.value = '';
      lernZugangListe(liste, (await lernCall('schule_zugaenge')).zugaenge, rollenText);
    } catch (err) { lernErsetze(status, el('p', { class: 'err-text' }, err.message)); }
  });
  const liste = el('div');
  lernZugangListe(liste, z.zugaenge, rollenText);
  lernErsetze(main, 
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'NUR BEREICH LERNEN'), el('h2', {}, 'Zugänge'),
      el('p', {}, 'Ein Lern-Code öffnet nur die Lernen-Seite. Der Server lehnt ihn für alle anderen Bereiche der App ab.')),
    form, liste);
}

function lernZugangListe(box, zugaenge, rollenText) {
  lernErsetze(box, el('h3', {}, 'Bestehende Zugänge'), ...(zugaenge.length ? zugaenge.map((g) => el('div', { class: 'card lern-zugang' + (g.aktiv ? '' : ' aus') },
    el('div', { class: 'lern-einheit-kopf' }, el('b', {}, g.name), el('span', { class: 'pill' }, rollenText[g.rolle] + (g.kind ? ' · ' + g.kind : ''))),
    el('p', { class: 'small muted' }, g.aktiv ? (g.zuletzt ? 'Zuletzt angemeldet ' + new Date(g.zuletzt).toLocaleDateString('de-DE') : 'Noch nie angemeldet') : 'Gesperrt'),
    g.aktiv ? el('button', { type: 'button', class: 'secondary', onclick: async (ev) => {
      if (!window.confirm(`Zugang „${g.name}“ sperren? Alle Geräte mit diesem Code werden abgemeldet.`)) return;
      try { await lernCall('schule_zugang_sperren', { id: g.id }); ev.target.closest('.lern-zugang').classList.add('aus'); ev.target.remove(); } catch (err) { window.alert(err.message); }
    } }, 'Sperren') : null)) : [el('p', { class: 'muted' }, 'Noch keine Zugänge.')]));
}


// ---------- Eltern/Lehrer: Lehrplan-Übersicht (alle Themen je Schulart und Klasse, mit Inhaltsstand) ----------
const LERN_STAND = { erledigt: ['geschafft', 'ok'], laeuft: ['läuft', 'laeuft'], offen: ['offen', ''], keine_einheit: ['–', 'leer'] };
function lernInhaltZustand(t) {
  const e = t.einheit;
  if (!e) return { k: 'leer', text: 'Noch kein Inhalt' };
  if (['geprueft', 'freigegeben'].includes(e.status)) return { k: 'fertig', text: `Fertig · ${e.karten} Etappen · ${e.aufgaben} Bordkarten${e.neu ? ` (${e.neu} neu in Prüfung)` : ''}` };
  return { k: 'pruefung', text: `In Prüfung · ${e.karten} Etappen · ${e.aufgaben} Bordkarten` };
}
let lernLpFilter = null;
async function viewLehrplan() {
  setChrome('Lehrplan', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernCall('schule_lehrplan_uebersicht');
  if (!live()) return;
  const kinder = d.kinder || [];
  const f = lernLpFilter || (lernLpFilter = { kl: '', inhalt: '', q: '' });
  const gk = (t) => t.jahrgang?.gym_by || 99; // Gruppe: Klasse im Gymnasium (alle Kinder sind am Gymnasium)
  const kacheln = el('div', { class: 'lp-kacheln' });
  const liste = el('div', { class: 'lp-liste' });
  const klSel = el('select', { 'aria-label': 'Klasse' });
  const klName = (k) => k === 99 ? 'Nicht im Gymnasium-Lehrplan' : `Klasse ${k}` + kinder.filter((c) => c.klasse === k).map((c) => ' · ' + c.name).join('');
  const fuelleKlassen = () => {
    const ks = [...new Set((d.themen || []).map(gk))].sort((a, b) => a - b);
    lernErsetze(klSel, el('option', { value: '' }, 'Alle Klassen'), ...ks.map((k) => el('option', { value: k, selected: String(k) === String(f.kl) }, klName(k))));
  };
  klSel.addEventListener('change', () => { f.kl = klSel.value; zeichne(); });
  const inhSel = el('select', { 'aria-label': 'Inhalt' }, ...[['', 'Alle Flüge'], ['fertig', 'Fertig'], ['pruefung', 'In Prüfung'], ['leer', 'Noch kein Inhalt']]
    .map(([v, t]) => el('option', { value: v, selected: f.inhalt === v }, t)));
  inhSel.addEventListener('change', () => { f.inhalt = inhSel.value; zeichne(); });
  const suche = el('input', { type: 'search', placeholder: 'Flug suchen …', 'aria-label': 'Flug suchen', value: f.q });
  suche.addEventListener('input', () => { f.q = suche.value; zeichne(); });
  const status = el('p', { class: 'small muted', role: 'status' });
  const zeile = (t) => {
    const z = lernInhaltZustand(t);
    const stand = kinder.map((c) => {
      const s = t.stand?.[c.id] || 'keine_einheit'; const [txt, kl] = LERN_STAND[s] || [s, ''];
      const geplant = (t.geplant || []).includes(c.id);
      return el('span', { class: 'lp-stand ' + kl }, `${c.name}: ${txt}${geplant ? ' · im Plan' : ''}`);
    });
    return el('article', { class: 'lp-zeile lp-' + z.k },
      el('div', { class: 'lp-text' }, el('b', {}, t.titel),
        el('span', { class: 'lern-plan-jg' }, lernJahrgangText(t.jahrgang) || 'ohne Lehrplan-Zuordnung'),
        t.beschreibung ? el('small', {}, t.beschreibung) : null,
        (t.gliederung || []).length ? el('ol', { class: 'lp-gliederung' }, ...t.gliederung.map((x) => el('li', {}, x))) : null,
        t.ort ? el('small', { class: 'muted' }, 'Ort der Lernreise: ' + t.ort) : null,
        el('span', { class: 'lp-inhalt' }, el('i', { class: 'lp-punkt', 'aria-hidden': 'true' }), z.text),
        el('div', { class: 'lp-staende' }, ...stand),
        t.rueckmeldungen ? el('a', { class: 'small', href: '#/lernauftraege' }, `${t.rueckmeldungen} offene${t.rueckmeldungen > 1 ? ' Aufträge' : 'r Auftrag'}`) : null),
      el('div', { class: 'lp-aktionen' },
        t.einheit ? el('a', { class: 'btn secondary', href: `#/inhalte/${t.einheit.id}` }, 'Inhalte ansehen') : null),
      // E-3: „Bauen lassen“ ist jetzt „✎ Ändern lassen“ mit der Art „Neuer Flug“ und einem Vorschlag für den Text
      t.einheit ? null : lernAendern({ block_id: t.block_id }, { bezug: 'flug', wo: `Flug „${t.titel}“`, art: 'neu',
        text: `Bitte Inhalte bauen: „${t.titel}“ (${t.ort || t.gebiet}, ${lernJahrgangText(t.jahrgang)}).` }));
  };
  const zeichne = () => {
    const q = f.q.trim().toLowerCase();
    const basis = (d.themen || []).filter((t) => !f.kl || String(gk(t)) === String(f.kl));
    const zahl = (k) => basis.filter((t) => lernInhaltZustand(t).k === k).length;
    lernErsetze(kacheln, 
      ...[['', 'Flüge', basis.length, ''], ['fertig', 'fertig', zahl('fertig'), ' lp-fertig'], ['pruefung', 'in Prüfung', zahl('pruefung'), ' lp-pruefung'], ['leer', 'ohne Inhalt', zahl('leer'), ' lp-leer']]
        .map(([wert, text, n, kl]) => el('button', { type: 'button', class: 'lp-kachel' + kl + (f.inhalt === wert ? ' on' : ''), 'aria-pressed': String(f.inhalt === wert),
          onclick: () => { f.inhalt = wert; inhSel.value = wert; zeichne(); } }, el('b', {}, String(n)), el('small', {}, text))));
    const treffer = basis.filter((t) => (!f.inhalt || lernInhaltZustand(t).k === f.inhalt)
      && (!q || `${t.titel} ${t.ort} ${t.gebiet}`.toLowerCase().includes(q)));
    const gruppen = new Map();
    for (const t of treffer.sort((a, b) => gk(a) - gk(b))) {
      const g = gk(t); if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(t);
    }
    lernErsetze(liste, ...[...gruppen].map(([kl, ts]) => el('section', { class: 'lp-gruppe' },
      el('h3', {}, klName(kl), el('small', { class: 'muted' }, ` · ${ts.length} ${ts.length === 1 ? 'Flug' : 'Flüge'}`)),
      ...[...ts.reduce((m, t) => m.set(t.gebiet || 'Weitere', [...(m.get(t.gebiet || 'Weitere') || []), t]), new Map())].flatMap(([g, gs]) => [
        el('h4', { class: 'lp-gebiet' }, g, el('small', { class: 'muted' }, ` · ${gs.filter((t) => lernInhaltZustand(t).k === 'fertig').length} von ${gs.length} mit Inhalt`)),
        ...gs.map(zeile)]))));
    if (!treffer.length) lernAnhaengen(liste, el('p', { class: 'muted' }, 'Keine Flüge für diese Auswahl.'));
  };
  fuelleKlassen(); zeichne();
  lernErsetze(main, lernInfoLink(),
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'ELTERN UND LEHRER'), el('h2', {}, 'Lehrplan-Übersicht'),
      el('p', {}, 'Alle Mathe-Flüge, sortiert nach Klasse im Gymnasium. Hinter jedem Flug steht, wann er laut Lehrplan dran ist: Gym = Gymnasium, RS = Realschule, IB = MYP-Jahr. Grün = Inhalt fertig, gelb = gebaut und in Prüfung, grau = noch nichts da.')),
    el('div', { class: 'card lp-filter' }, el('div', { class: 'row' }, klSel, inhSel, suche)),
    kacheln, status, liste);
}

// ---------- Eltern/Lehrer: Inhalte einer Einheit prüfen (Erklärungen, Fehler, alle Aufgaben mit Lösung) ----------
async function viewInhalte(arg) {
  setChrome('Inhalte', { back: true, showTabs: false });
  const live = viewGuard();
  const id = Number(arg);
  if (!id) { route('lehrplan'); return; }
  loading();
  const d = await lernCall('schule_inhalt_lesen', { einheit_id: id });
  if (!live()) return;
  const titel = d.thema?.titel || d.inhalt?.ziel || 'Flug';
  $('#title').textContent = titel;
  const aufgaben = d.aufgaben || [];
  const etappen = lernEtappen({ inhalt: d.inhalt, uebungen: aufgaben.filter((a) => a.pool === 'uebung') });
  lernTitel = new Map(etappen.map((e) => [e.lernziel, e.titel]));
  const rmJe = (lz) => (d.rueckmeldungen || []).filter((r) => r.lernziel === lz);
  // F: Stufe und Typ je Bordkarte (typ aus Migration F; fehlt → nur die Stufe)
  const stufeText = (a) => a.pool === 'bonus' ? el('span', {}, '★ Knobel', el('small', { class: 'muted lp-typ' }, 'freiwillig'))
    : a.pool === 'uebung' ? el('span', {}, ['', 'leicht', 'mittel', 'schwer'][a.stufe] || '–', a.typ ? el('small', { class: 'muted lp-typ' }, LERN_TYP[a.typ]?.[1] || a.typ) : null)
    : a.pool === 'test' ? 'Test' : a.pool === 'nachtest' ? 'Nachtest' : a.pool;
  const tabelle = (as) => el('div', { class: 'lp-tabelle-rahmen' }, el('table', { class: 'lp-tabelle' },
    el('thead', {}, el('tr', {}, el('th', {}, 'Stufe'), el('th', {}, 'Bordkarte'), el('th', {}, 'Lösung'), el('th', {}, 'Lösungsweg'), el('th', {}, 'Status'))),
    el('tbody', {}, ...as.map((a) => el('tr', {},
      el('td', {}, stufeText(a)),
      el('td', {}, lernText(a.frage?.text || a.frage?.schablone || ''), a.antworttyp === 'auswahl' ? el('small', { class: 'muted' }, ' (' + (a.antworten || []).join(' | ') + ')') : null),
      el('td', { class: 'lp-loesung' }, lernLoesungText(a)),
      el('td', { class: 'muted' }, lernText(a.loesungsweg || '')),
      el('td', {}, a.freigegeben ? el('span', { class: 'lp-ok' }, 'frei ✓') : el('span', { class: 'lp-warte' }, 'in Prüfung')))))));
  const karten = etappen.map((e) => {
    const as = aufgaben.filter((a) => a.lernziel === e.lernziel);
    const rm = rmJe(e.lernziel);
    return el('details', { class: 'card lp-karte', id: 'k' + e.nr },
      el('summary', {}, el('b', {}, `${e.nr} · ${e.titel}`), el('small', { class: 'muted' }, ` · ${as.length} ${as.length === 1 ? 'Bordkarte' : 'Bordkarten'}${as.some((a) => !a.freigegeben) ? ` (${as.filter((a) => !a.freigegeben).length} in Prüfung)` : ''}${rm.length ? ` · ${rm.length} ${rm.length === 1 ? 'Anmerkung' : 'Anmerkungen'}` : ''}`)),
      el('div', { class: 'lp-karte-innen' },
        el('div', { class: 'lp-erkl' }, el('p', { class: 'eyebrow' }, 'ERKLÄRUNG, WIE DAS KIND SIE SIEHT'), e.regel ? lernErklaerung(e) : el('p', { class: 'muted' }, 'Keine Erklärung hinterlegt.')),
        lernAendern({ einheit_id: id, lernziel: e.lernziel }, { bezug: 'etappe', wo: `Etappe „${e.titel}“` }),
        ...rm.map((r) => el('p', { class: 'small' }, el('b', {}, (LERN_RM_STATUS[r.status] || r.status) + ': '), r.text, r.antwort ? el('span', { class: 'muted' }, ' → ' + r.antwort) : null)),
        as.length ? tabelle(as) : el('p', { class: 'muted small' }, 'Keine Bordkarten.')));
  });
  const ohneKarte = aufgaben.filter((a) => !etappen.some((e) => e.lernziel === a.lernziel));
  const zahl = (fn) => aufgaben.filter(fn).length;
  lernErsetze(main, ...[
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, [d.ort?.stadt, lernJahrgangText(d.thema?.jahrgang)].filter(Boolean).join(' · ').toUpperCase() || 'INHALTE'),
      el('h2', {}, titel),
      el('p', {}, `${['geprueft', 'freigegeben'].includes(d.status) ? 'Fertig' : 'In Prüfung'} · ${etappen.length} Etappen · ${zahl((a) => a.pool === 'uebung')} Bordkarten zum Üben · ${zahl((a) => a.pool !== 'uebung')} für Test und Nachtest`
        + (zahl((a) => !a.freigegeben) ? ` · ${zahl((a) => !a.freigegeben)} noch in Prüfung (nur für das Testkind sichtbar)` : '')),
      d.inhalt?.ziel ? el('p', { class: 'small muted' }, 'Ziel: ' + d.inhalt.ziel) : null),
    el('nav', { class: 'lp-sprung', 'aria-label': 'Etappen' }, ...etappen.map((e) => el('a', { href: '#', class: 'lern-chip', onclick: (ev) => {
      ev.preventDefault(); const k = document.getElementById('k' + e.nr); k.open = true; k.scrollIntoView({ block: 'start' });
    } }, `${e.nr} · ${e.titel}`))),
    lernAendern({ einheit_id: id }, { bezug: 'flug', wo: `Flug „${titel}“` }),
    ...karten,
    ohneKarte.length ? el('details', { class: 'card lp-karte' }, el('summary', {}, el('b', {}, `Bordkarten für Test und Nachtest ohne Etappe (${ohneKarte.length})`)), tabelle(ohneKarte)) : null].filter(Boolean));
}

// ---------- Eltern/Lehrer: „Was wackelt?“ – Lernstand je Lernkarte mit den echten falschen Antworten ----------
async function viewWackelt(arg) { // Zusatz 1 zu F: frühere Seite „Lernstand“, jetzt „Was wackelt?“ unter #/wackelt/<id>
  setChrome('Was wackelt?', { back: true, showTabs: false });
  const live = viewGuard();
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return; }
  loading();
  const d = await lernCall('schule_lernstand', { lernender_id: kindId });
  if (!live()) return;
  $('#title').textContent = 'Was wackelt? · ' + d.kind.name;
  const tag = (t) => new Date(t).toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' });
  const zustand = (k) => k.faellig ? ['wiederholen', 'wdh'] : k.sitzt ? ['sitzt', 'ok']
    : k.falsch >= 3 && k.falsch > k.richtig ? ['wackelt', 'wackelt'] : k.richtig + k.falsch ? ['am Üben', 'ueben'] : ['noch nicht geübt', 'neu'];
  const karte = (k) => {
    const [text, kl] = zustand(k);
    return el('li', { class: 'ls-karte ls-' + kl },
      el('div', { class: 'ls-kopf' }, el('b', {}, k.titel), el('span', { class: 'ls-zustand' }, text)),
      k.richtig + k.falsch ? el('small', { class: 'muted' }, `${k.richtig} richtig · ${k.falsch} falsch` + (k.mit_tipp ? ` · ${k.mit_tipp}-mal Tipp` : '') + (k.zuletzt ? ` · zuletzt ${tag(k.zuletzt)}` : '')) : null,
      // K4: wie viele Bordkarten bis „sitzt“ gebraucht wurden (zeigt, ob „6 Punkte und eine schwere Bordkarte“ zu lang ist)
      k.sitzt && k.bis_sitzt ? el('small', { class: 'muted ls-bis-sitzt' }, `sitzt nach ${k.bis_sitzt} ${k.bis_sitzt === 1 ? 'Bordkarte' : 'Bordkarten'}`) : null,
      k.knobel_gesamt ? el('small', { class: 'muted ls-knobel' }, `Knobel: ${k.knobel_geloest || 0} von ${k.knobel_gesamt}`) : null, // F
      (k.fehler || []).length ? el('details', { class: 'ls-fehler' }, el('summary', {}, `Letzte falsche Antworten (${k.fehler.length})`),
        ...k.fehler.map((f) => { const a = { antworttyp: f.antworttyp, antworten: f.antworten, loesung: f.loesung, frage: { text: f.frage, schablone: f.schablone, grafik: f.grafik } };
          return el('p', { class: 'small' }, el('span', {}, lernText(f.frage || '')), el('br'), el('span', { class: 'ls-falsch' }, 'Antwort: ' + (lernAntwortText(a, f.antwort || {}) || '–')),
            ' · ', el('span', { class: 'ls-richtig' }, 'richtig: ' + lernLoesungText(a))); })) : null);
  };
  const wackelt = (d.einheiten || []).flatMap((e) => (e.karten || []).filter((k) => zustand(k)[1] === 'wackelt').map((k) => ({ ...k, ort: e.ort, thema: e.titel })));
  const w = d.woche || {};
  lernErsetze(main,
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'LERNSTAND'), el('h2', {}, d.kind.name),
      el('p', {}, `Letzte 7 Tage: ${w.aufgaben || 0} Bordkarten, davon ${w.richtig || 0} richtig` + (w.mit_tipp ? `, ${w.mit_tipp}-mal mit Tipp` : '') + `. Lerntage in 4 Wochen: ${(d.lerntage || []).length}` + ((d.lerntage || []).length ? ` (zuletzt ${tag(d.lerntage[0])})` : '') + '.')),
    (() => { const alle = (d.einheiten || []).flatMap((e) => e.karten || []); const sitzt = alle.filter((k) => k.sitzt).length, faellig = alle.filter((k) => k.faellig).length;
      return el('details', { class: 'card ls-wdh' }, el('summary', {}, el('b', {}, 'Was kommt wann wieder? '), `${sitzt} ${sitzt === 1 ? 'Etappe sitzt' : 'Etappen sitzen'}, ${faellig} davon ${faellig === 1 ? 'ist' : 'sind'} zum Wiederholen dran`),
        el('p', {}, 'Wiederholung: Sitzt eine Etappe, kommt sie nach 1, 3, 7, 14 und 30 Lerntagen wieder – jeweils mit einer Bordkarte. Ein Lerntag ist ein Tag, an dem das Kind in Mathe übt; in Pausen (Reisetage) wartet die Etappe.'),
        el('p', {}, 'Bei einem Fehler in der Wiederholung geht die Etappe eine Stufe zurück und kommt am nächsten Lerntag wieder. Erst beim zweiten Fehler hintereinander muss das Kind sie neu üben.'),
        el('p', {}, `Vor einem Flug kommen höchstens ${LERN_WDH_RUNDE} Wiederholungen pro Tag; weitere werden nur angeboten.`),
        el('p', {}, 'Nachtest: Nach einem bestandenen Flug-Test folgt später ein kurzer Nachtest zum selben Flug, ebenfalls nach Lerntagen gezählt.')); })(),
    el('section', { class: 'card ls-wackelt' }, el('h3', {}, 'Was wackelt?'),
      wackelt.length ? el('ul', { class: 'ls-liste' }, ...wackelt.map((k) => el('li', { class: 'ls-karte ls-wackelt' }, el('div', { class: 'ls-kopf' }, el('b', {}, k.titel), el('span', { class: 'ls-zustand' }, `${k.falsch} falsch`)), el('small', { class: 'muted' }, `${k.ort || ''} · ${k.thema}`))))
        : el('p', { class: 'muted' }, 'Im Moment nichts: Keine Etappe hat deutlich mehr falsche als richtige Antworten.'),
      el('p', { class: 'small muted' }, '„Wackelt“ heißt: mindestens 3 falsche Antworten und mehr falsche als richtige. Ein Gespräch über genau diese eine Regel hilft meist mehr als weitere Bordkarten.')),
    ...((d.einheiten || []).length ? d.einheiten.map((e) => el('section', { class: 'card' },
      el('div', { class: 'lern-einheit-kopf' }, el('h3', {}, `${e.ort ? e.ort + ': ' : ''}${e.titel}`), el('a', { class: 'small', href: `#/inhalte/${e.einheit_id}` }, 'Inhalte ansehen')),
      el('p', { class: 'small muted' }, `${(e.karten || []).filter((k) => k.sitzt).length} von ${(e.karten || []).length} Etappen sitzen` + (e.zuletzt ? ` · zuletzt ${tag(e.zuletzt)}` : '')),
      el('ul', { class: 'ls-liste' }, ...(e.karten || []).map(karte)))) : [el('p', { class: 'card muted' }, 'Noch nichts gelernt.')]));
}

// ---------- Wiederholen: fällige Lernkarten, je eine Aufgabe ----------
async function viewWiederholen(arg) {
  setChrome('Wiederholen', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const r = await lernCall('schule_wiederholung', { lernender_id: d.kind.id, anzahl: LERN_WDH_RUNDE });
  if (!live()) return;
  const { kind } = d; const liste = r.aufgaben || [];
  const flaeche = el('div', { class: 'lr-etappe-flaeche' });
  let i = 0, richtig = 0;
  const zeige = () => {
    const a = liste[i];
    if (!a) {
      const offen = liste.length - richtig; // V7: der Haken nur, wenn alles richtig war
      lernWdhHeute(kind.id, true); // V9: Runde für heute gemacht
      lernErsetze(flaeche, el('section', { class: 'lr-geschafft' }, offen ? null : el('div', { class: 'lr-geschafft-haken' }, lernIcon(LI.haken, 64)),
        el('p', { class: 'lr-ueber' }, 'WIEDERHOLT'), el('h1', { class: 'lr-titel' }, `${richtig} von ${liste.length} richtig`),
        el('p', { class: 'lr-leise' }, offen ? `${offen} ${offen === 1 ? 'Etappe braucht' : 'Etappen brauchen'} noch Übung – morgen ${offen === 1 ? 'kommt sie' : 'kommen sie'} wieder. Die Erklärung findest du im Merkheft.` : 'Super – das sitzt noch.')),
        el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Weiter zu Heute'), lernWdhErklaert());
      return;
    }
    const auf = lernAufgabe(a); const cid = lernCid();
    const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
    const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
    pruefen.addEventListener('click', async () => {
      const w = auf.antwort();
      if (!w) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
      pruefen.disabled = true;
      try {
        const x = await lernCall('schule_uebung_pruefen', { lernender_id: kind.id, aufgabe_id: a.id, antwort: w, client_id: cid, hilfe: 0 });
        if (!x.format_ok) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, x.hinweis)); pruefen.disabled = false; return; }
        auf.sperren(); a.loesung = x.loesung; if (x.richtig) richtig++; auf.zeigeLoesung(x.loesung);
        lernErsetze(meldung, x.richtig ? el('div', { class: 'lr-rueck lr-rueck-ok' }, el('b', {}, 'Richtig!'))
          : el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, 'Noch nicht. Richtig ist: ' + lernLoesungText(a)), x.loesungsweg ? el('p', {}, lernText(x.loesungsweg)) : null,
            el('a', { href: `#/lerneinheit/${kind.id}-${a.einheit_id}` }, 'Zur Etappe')));
        i++; pruefen.replaceWith(el('button', { type: 'button', class: 'lr-knopf', onclick: zeige }, i < liste.length ? 'Nächste' : 'Fertig'));
      } catch (err) { lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
    });
    lernErsetze(flaeche, el('header', { class: 'lr-etappe-oben' }, el('p', { class: 'lr-ueber' }, `WIEDERHOLEN ${i + 1} VON ${liste.length} · ${(a.stadt || '').toUpperCase()}`),
      el('h1', { class: 'lr-titel' }, a.etappe || 'Bordkarte')),
      el('section', { class: 'lr-karte-box lr-aufgabe' }, auf.node), meldung, pruefen);
    window.scrollTo(0, 0);
  };
  if (!liste.length) lernErsetze(flaeche, el('p', { class: 'lr-leise' }, 'Gerade ist nichts zum Wiederholen dran.'), el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Zu Heute'));
  else zeige();
  lernErsetze(main, lernRahmen(kind, 'reise', flaeche));
}
