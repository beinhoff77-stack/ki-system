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

// LZ-App (0.91.1): Lese-Anfragen der Lehrer-Seiten je Sitzung merken (gleiche Anfrage = gleiche Antwort, auch während sie noch läuft);
// eine gemerkte Antwort wird sofort geliefert und nach 10 s im Hintergrund aufgefrischt (Ereignis „lern-frisch“, wenn sie sich geändert hat).
// Jede schreibende Aktion vergisst gezielt: alles zu diesem Kind und alle kindunabhängigen Antworten (Übersicht, Matrix-Gerüst); ohne Kind alles.
const LERN_MERKEN = new Set(['schule_uebersicht', 'schule_lehrplan_matrix', 'schule_lehrplan_uebersicht', 'schule_lernstand', 'schule_plan_lesen', 'schule_wackelt_lesen']);
const LERN_NUR_LESEN = /^schule_(ich|konto|eltern|zugaenge|merkheft|wiederholung|reise_karte|lehrplan_thema|einheit_lesen|inhalt_lesen|schulstand|lehrplan_lesen)$|_lesen$/;
const lernSpeicher = new Map(); // Schlüssel → { p, wert, t, kind, frisch }
const lernSpeicherSchl = (a, d) => a + '|' + JSON.stringify(d || {});
const lernKopie = (w) => (w && typeof w === 'object' ? structuredClone(w) : w);
function lernVergessen(kindId) {
  if (typeof lernReiseKarteVergessen === 'function') lernReiseKarteVergessen(kindId); // RK: Karte gilt als alt (wird im Hintergrund neu geholt)
  for (const [s, e] of lernSpeicher) if (kindId === undefined || kindId === null || e.kind === null || e.kind === Number(kindId)) lernSpeicher.delete(s);
}
function lernMerkeAuf(s, aktion, daten, p) {
  const e = { p, t: Date.now(), kind: daten?.lernender_id !== undefined ? Number(daten.lernender_id) : null };
  lernSpeicher.set(s, e);
  p.then((w) => { if (lernSpeicher.get(s) === e) e.wert = w; }, () => { if (lernSpeicher.get(s) === e) lernSpeicher.delete(s); });
  return e;
}
function lernAuffrischen(s, aktion, daten, alt) {
  if (alt.frisch) return; alt.frisch = true;
  lernCallNetz(aktion, daten).then((w) => {
    if (lernSpeicher.get(s) !== alt) return; // inzwischen vergessen (Änderung) – nichts überschreiben
    const anders = JSON.stringify(w) !== JSON.stringify(alt.wert);
    const e = lernMerkeAuf(s, aktion, daten, Promise.resolve(w)); e.wert = w;
    if (anders) dispatchEvent(new CustomEvent('lern-frisch', { detail: { aktion, daten } }));
  }, () => { alt.frisch = false; });
}
async function lernCall(aktion, daten = {}) {
  if (LERN_MERKEN.has(aktion)) {
    const s = lernSpeicherSchl(aktion, daten); let e = lernSpeicher.get(s);
    if (e && e.wert !== undefined && Date.now() - e.t > 10000) lernAuffrischen(s, aktion, daten, e);
    if (!e) e = lernMerkeAuf(s, aktion, daten, lernCallNetz(aktion, daten));
    return lernKopie(await e.p); // Kopie: Aufrufer dürfen die Antwort verändern
  }
  const schreibt = !LERN_NUR_LESEN.test(aktion);
  if (schreibt) lernVergessen(daten?.lernender_id);
  try { return await lernCallNetz(aktion, daten); } finally { if (schreibt) lernVergessen(daten?.lernender_id); }
}
// Hintergrund: Anfragen vorab starten (Ergebnis landet im Speicher); Fehler still
const lernVorladen = (aktion, daten = {}) => { lernCall(aktion, daten).catch(() => { /* still */ }); };
async function lernCallNetz(aktion, daten = {}) {
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
    if (e.thema_id && (r?.kann_schon_themen || []).includes(e.thema_id)) return 'kann'; // LA-4: „kann schon“ je Flug
    if (e.thema_id && (r?.kann_wdh_themen || []).includes(e.thema_id) && !Number(stand.get(e.id)?.wieder_offen || 0)) return 'kann'; // LB-3: gesetzt gelandet, nur Wiederholungen (wieder offen → üben)
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
    return { ...e, gruppe: gruppe(e), fertig: f, n, geschafft: n > 0 && f >= n, fehler: Number(s.fehler || 0), laeuft: !!s.laeuft, blocktest: !!s.blocktest, ohneTest: !!s.ohne_test, ortFertig: route.get(e.block_id)?.status === 'fertig' };
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
function lernStats(konto, ex = null) {
  const s = (icon, wert, text) => el('div', { class: 'lr-stat' }, lernIcon(icon, 22), el('div', {}, el('b', {}, String(wert)), el('span', {}, text)));
  // Antippen erklärt, was die Zahlen bedeuten.
  return el('details', { class: 'lr-stats-box' },
    el('summary', { 'aria-label': 'Stempel, Sterne und Lerntage – antippen für Erklärung' },
      el('div', { class: 'lr-stats' }, s(LI.stempel, konto?.stempel ?? 0, 'Stempel'), s(LI.stern, lernZahl(konto?.sterne ?? 0), 'Sterne'), s(LI.tag, konto?.lerntage ?? 0, 'Lerntage')),
      // F: Knobel-Sterne – nur, wenn die Datenbank sie zählt (Migration F)
      // EX-App: „⛯ Expeditionen: k von n Stationen ›“ führt in die Stempel-Sammlung
      ex?.d ? el('a', { class: 'lr-knobel-sterne lr-ex-pass-zeile', href: `#/stationen/${ex.d.kind.id}`, onclick: (ev) => ev.stopPropagation() }, `⛯ Expeditionen: ${lernExGeschafftZahl(ex.d)} von ${lernExGesamt(ex.d)} Stationen ›`)
        : konto?.expeditions_stempel ? el('p', { class: 'lr-knobel-sterne' }, `⛯ Expeditionen: ${konto.expeditions_stempel}`) : null, // W176 Teil 4
      konto?.knobel_sterne ? el('p', { class: 'lr-knobel-sterne' }, `★ Knobel-Sterne: ${konto.knobel_sterne}`) : null),
    el('div', { class: 'lr-stats-erkl' },
      el('p', {}, el('b', {}, 'Sterne: '), '10 für jede Bordkarte, die du zum ersten Mal richtig löst, 20 für jede richtige Bordkarte im Test. Sterne kannst du später gegen Belohnungen eintauschen.'),
      el('p', {}, el('b', {}, 'Stempel: '), 'Jeder Ort hat einen oder mehrere Flüge. Hast du alle Flüge eines Ortes geschafft, bekommst du seinen Stempel in den Reisepass.'),
      el('p', {}, el('b', {}, 'Lerntage: '), 'Tage, an denen du geübt hast.'),
      konto?.knobel_sterne ? el('p', {}, el('b', {}, 'Knobel-Sterne: '), 'Knobel-Bordkarten sind richtig schwer – für Profis. Löst du eine beim ersten Versuch, gibt es 30 Sterne und einen Knobel-Stern.') : null));
}
async function lernLadeKind(arg, { still = false } = {}) {
  const kindId = Number(arg); lernJwLaden(); // JW: Wortliste früh holen (Sticker erscheinen dann ohne Verzögerung)
  if (!kindId) { if (!still) route('lernen'); return null; }
  const [u, k] = await Promise.all([lernCall('schule_uebersicht'), lernCall('schule_konto', { lernender_id: kindId }).catch(() => null)]);
  lernEinheitThemenMerken(u); // WK F3: Einheit → Thema (für die Namen der Reisekarte)
  const d = lernReiseDaten(u, kindId);
  if (!d) { if (!still) route('lernen'); return null; }
  if (k?.look) Object.assign(d.kind, k.look);
  d.konto = k?.konto || null; d.belohnungen = k?.belohnungen || []; d.einloesungen = k?.einloesungen || [];
  d.regeln = k?.regeln || null; d.landungNachbuchung = k?.landung_nachbuchung || null; // FP-S: Sterne-Regeln und einmaliger Hinweis nach der Nachbuchung
  d.knobelTag = k?.knobel_tag || null; // F: „Knobeln des Tages“ (Migration F; fehlt → nichts)
  d.expeditionen = Array.isArray(k?.expeditionen) ? k.expeditionen : []; // W176 Teil 4 (fehlt → keine Expeditionen)
  d.exStand = k?.expeditionen_stand || null; // EX-S: Stationen gesamt/geschafft, oberste Karte (fehlt → wie bisher)
  d.u = u; // K3: für den Stand über Schularten
  // NB-App / SJ-App / ZP-App (0.93.0): nachbessern[] und schuljahr_stand (schule_konto, sonst je Kind in schule_uebersicht), zusatz_plan[] (je Kind in schule_uebersicht)
  d.nachbessern = Array.isArray(k?.nachbessern) ? k.nachbessern : Array.isArray(d.kind.nachbessern) ? d.kind.nachbessern : [];
  d.schuljahr = k?.schuljahr_stand || d.kind.schuljahr_stand || null;
  d.zusatzPlan = Array.isArray(d.kind.zusatz_plan) ? d.kind.zusatz_plan : [];
  return lernNamenSetzen(d); // WK F3: Namen der Reisekarte, sobald sie in dieser Sitzung geladen ist
}

// ---------- Stand über Schularten (K3, K4, E-2-Startseite) – Rechenregel „Stand“ ----------
// Für Schulart s und Stufe k zählen alle Flüge mit jahrgang[s] = k. Gelandet: alle Pflicht-Etappen fertig (fertig ≥ pflicht_anzahl),
// Ort geschafft oder „kann schon“. Läuft: mindestens eine Etappe fertig. Wackelt: Fehler offen oder Rückreise offen.
// Flüge: schule_uebersicht.themen (alle Mathe-Flüge, auch ohne Inhalt; Migration 20261117_w150_d_*), sonst die Flüge mit Inhalt (einheiten).
// Stufe: kind.stufen[s] (Migration D), sonst eigene Schulart = Klasse, andere = gleiche Klasse, IB = MYP-Jahr = Klasse − 5 (Klasse 5 steht vor MYP-Jahr 1 → 0).
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
  if (a.bonus) return el('span', { class: 'lr-stufe lr-stufe-bonus', role: 'img', 'aria-label': 'Knobel-Bordkarte für Profis' }, '★ KNOBEL');
  const n = Number(a.stufe); if (!(n >= 1 && n <= 3)) return el('span', {});
  const wort = ['', 'leicht', 'mittel', 'schwer'][n];
  return el('span', { class: 'lr-stufe lr-stufe-' + n, role: 'img', 'aria-label': 'Stufe: ' + wort, title: wort }, '●'.repeat(n));
}
// Knobel-Bordkarte (Pool „bonus“): freiwillig, ein Versuch, falsch kostet nichts und zeigt den Weg; richtig im ersten Versuch = 30 Sterne und ein Knobel-Stern.
// Zählt weder für „sitzt“ noch für Wiederholung oder Test (die Datenbank bucht sie nicht in den Karten-Stand).
function lernKnobelAngebot(e, oeffnen) {
  const offen = (e.bonus || []).filter((k) => !k.versuche);
  if (!offen.length) return null;
  return el('button', { type: 'button', class: 'lr-knopf-zweit lr-knobel-angebot', onclick: () => oeffnen(offen[0]) }, '★ Knobel-Bordkarte – für Profis');
}
function lernKnobel(ziel, a, ctx, { ortCode = '', zurueck, titel = 'KNOBEL-BORDKARTE', zurueckText = 'Zurück', nachPruefen = null } = {}) {
  const auf = lernAufgabe(a, null, { tasten: false }); const cid = lernCid();
  const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
  const hilfeBox = el('div', { class: 'lr-hilfebox' });
  const tipp = a.tipp ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { tipp.remove(); lernAnhaengen(hilfeBox, el('p', { class: 'lr-tipp' }, el('b', {}, 'Tipp: '), lernMathe(a.tipp))); } }, 'Tipp') : null;
  const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
  const weiter = zurueck ? el('button', { type: 'button', class: 'lr-knopf-zweit lr-knobel-zurueck', onclick: zurueck }, zurueckText) : null;
  pruefen.addEventListener('click', async () => {
    const w = auf.antwort();
    if (!w) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
    pruefen.disabled = true;
    try {
      const r = await lernCall('schule_uebung_pruefen', { lernender_id: ctx.kind, aufgabe_id: a.id, antwort: w, client_id: cid });
      if (!r.format_ok) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, r.hinweis || 'Bitte prüfe die Eingabe.')); pruefen.disabled = false; return; }
      a.versuche = (a.versuche || 0) + 1; if (r.richtig) a.geloest = true;
      auf.zeigeLoesung?.(r.loesung); pruefen.remove(); tipp?.remove(); nachPruefen?.(weiter);
      lernErsetze(meldung, r.richtig
        ? el('div', { class: 'lr-rueck lr-rueck-ok lr-knobel-ok' }, el('b', {}, '★ Geknackt!'), r.sterne ? el('p', { class: 'lr-sterne-neu' }, `+${r.sterne} Sterne · ein Knobel-Stern`) : null,
          r.knobel_sterne ? el('p', { class: 'lr-leise' }, `Knobel-Sterne: ${r.knobel_sterne}`) : null, r.loesungsweg ? el('p', {}, lernMathe(r.loesungsweg)) : null,
          a.versuche === 1 ? lernJwPlatz(ctx.kind, 'knobel_richtig', 'box') : null) // JW: im ersten Versuch richtig → Staunen
        : el('div', { class: 'lr-rueck lr-knobel-falsch' }, el('b', {}, 'Diesmal nicht – das war eine harte Nuss.'), el('p', {}, 'Richtig ist: ', lernMathe(lernLoesungText({ ...a, loesung: r.loesung }))),
          r.loesungsweg ? el('p', {}, el('b', {}, 'So geht’s: '), lernMathe(r.loesungsweg)) : null, el('p', { class: 'lr-leise' }, 'Knobeln kostet nichts – dein Stand bleibt.')));
    } catch (err) { if (lernGesperrt(err)) { if (zurueck) zurueck(); else render(); return; } lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
  });
  lernErsetze(ziel, el('section', { class: 'lr-karte-box lr-aufgabe lr-bordkarte lr-knobel' },
      el('div', { class: 'lr-bord-kopf' }, el('span', {}, ortCode ? `${titel} · ${ortCode}` : titel), lernStufeZeichen({ ...a, bonus: true })),
      el('p', { class: 'lr-leise' }, 'Für Profis: zählt nicht für „sitzt“ und nicht für den Test. Richtig beim ersten Versuch: 30 Sterne.'),
      auf.node, el('div', { class: 'lr-knopfzeile' }, pruefen, tipp)),
    hilfeBox, meldung, weiter);
  ziel.scrollIntoView?.({ block: 'start' });
}
// F: „Knobeln des Tages“ auf der Abflugtafel – höchstens einmal je Lerntag, aus einer sitzenden Etappe (schule_konto.knobel_tag)
function lernKnobelDesTages(d) {
  const a = d.knobelTag; if (!a) return null;
  const tag = lernHeuteTag(d.kind.id), schl = `lern.knobel.${d.kind.id}`; // Teil 6: Tag des Kindes (heute_bis), nicht UTC
  try { if (localStorage.getItem(schl) === tag) return null; } catch { /* egal */ }
  const box = el('section', { class: 'lr-karte-box lr-knobel-tag' },
    el('p', { class: 'lr-ueber' }, '★ KNOBELN DES TAGES'),
    el('p', {}, 'Eine harte Nuss aus ', el('b', {}, a.etappe || 'einer Etappe, die schon sitzt'), lernStadtName(d.kind.id, a) ? ` (${lernStadtName(d.kind.id, a)})` : '', '. Für Profis – falsch kostet nichts.'),
    el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => {
      try { localStorage.setItem(schl, tag); } catch { /* egal */ }
      lernKnobel(box, a, { kind: d.kind.id }, { titel: 'KNOBELN DES TAGES', zurueck: () => box.remove() });
    } }, 'Knobeln für Profis'));
  return box;
}
// Auswahl der nächsten Bordkarte (stellt sie an den Anfang von warte). Regel „sitzt“ (16.11.): Die Stufe steigt mit den Punkten.
function lernWaehleBordkarte(warte, e, letzte, gesehenTyp = new Set()) {
  // W176: Stufe nach eigenen Lösungen (anteilig), nach je 2 Fehlern in Folge eine Stufe leichter (stufe_senkung vom Server)
  const ziel = e.ziel || 6, p = e.neueRegel ? e.eigene : e.serie || 0;
  const soll = Math.max(1, (p >= ziel ? 3 : Math.min(3, 1 + Math.floor(p * 3 / ziel))) - (e.neueRegel ? e.stufeSenkung || 0 : 0));
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
  const neuZ = (x) => e.sitzt || !e.gezaehlt || !e.gezaehlt.has(Number(x.id)); // H3: solange es ungezählte gibt, keine schon gezählte
  for (const ok of [(x) => !x.geloest && !x.falschHeute && neuZ(x), (x) => !x.geloest && neuZ(x), (x) => !x.geloest && !x.falschHeute, (x) => !x.geloest, (x) => x !== letzte])
    for (const st of reihe)
      for (const ex of [(x) => anders(x) && neuTyp(x), anders])
        if (vor(warte.findIndex((x) => (x.stufe || 2) === st && ok(x) && ex(x)))) return;
  for (const ok of [(x) => !x.geloest && !x.falschHeute, (x) => !x.geloest, (x) => x !== letzte])
    for (const st of reihe)
      if (vor(warte.findIndex((x) => (x.stufe || 2) === st && ok(x)))) return;
}
// W176 Teil 3: Ist jetzt eine Mischkarte dran? Start erst, wenn im Flug mindestens „ab“ Etappen gelandet sind; dann jede „jede“-te Bordkarte.
// Bevorzugt gleicher Flug, dann gleicher Kontinent; jede 3. Mischkarte aus einem älteren Flug. Nimmt die Karte aus rest heraus (keine Wiederholung in der Sitzung).
function lernMischWahl(rest, { nr, jede, ab = 3, gelandet, aus = false, zaehler = { n: 0 } }) {
  if (!jede || aus || !rest.length || gelandet < ab || nr % jede) return null;
  zaehler.n++;
  const wunsch = zaehler.n % 3 === 0 ? ['aelter', 'kontinent', 'flug'] : ['flug', 'kontinent', 'aelter'];
  for (const q of wunsch) { const i = rest.findIndex((x) => x.quelle === q); if (i >= 0) return { ...rest.splice(i, 1)[0], misch: true }; }
  return { ...rest.shift(), misch: true };
}
// FP (Vorgabe „faire Punkte“ 2): Hinweis bei 5 statt 10 Sternen – höchstens einmal je Etappe und Lerntag, ohne Tadel
function lernFuenfHinweis(ctx, e, plus, { hilfe, zweiter }) {
  const voll = Number(ctx.regeln?.sterne_uebung_richtig ?? 10);
  if (!plus || plus >= voll || (!hilfe && !zweiter)) return null;
  const schl = `lern.fp5.${ctx.kind}.${e.lernziel}`; const tag = lernHeuteTag(ctx.kind);
  try { if (localStorage.getItem(schl) === tag) return null; localStorage.setItem(schl, tag); } catch { /* ohne Speicher: jedes Mal */ }
  return el('p', { class: 'lr-leise lr-fp-hinweis' }, hilfe ? `Ganz ohne Tipp gibt es ${voll} ★.` : `Gleich beim ersten Mal gibt es ${voll} ★.`);
}
// 0.86.2: leere Mischkarten-Liste einmal je Sitzung neu holen (nur die Liste wird übernommen; schon gezeigte bleiben verbraucht)
function lernMischNachladen(ctx) {
  ctx.mischNachgeladen = true;
  lernCall('schule_einheit_lesen', { lernender_id: ctx.kind, einheit_id: ctx.einheit })
    .then((x) => { if (Array.isArray(x?.mischkarten)) ctx.daten.mischkarten = x.mischkarten; }).catch(() => { /* ohne Mischkarte weiter */ });
}
// ---------- W176 Teil 4 / EX-App (0.91.0): Expeditionen (Kind) ----------
// Vorgabe inhalte/pruefung/kind/expedition/umsetzung.md: kein „freiwillig“ auf der Kinderseite; „Expedition freigeschaltet“ (Ansicht 1), oberste Karte der
// Abflugtafel (Ansicht 2), nach „Später“ ein Chip bis Lerntag-Ende (2b), Abschluss 150/200 ★ (Ansicht 3), Stempel-Sammlung „k von n Stationen“ (Ansicht 4).
// Farbe Polar (nicht Gold = abgelegt, nicht Siegelrot = Ort-Stempel). Die Expedition sperrt nichts: der nächste Flug ist überall mit einem Tipp erreichbar.
// <EX-STATIONEN> (erzeugt von tools/ex_stationen.py – nicht von Hand ändern)
// Quelle Stationen: COMNAP Antarctic Facilities 2024 (frei für Bildung/nicht kommerziell)
const LERN_EX_STATIONEN = [
  {"schluessel":"5-aquarium","nr":1,"station":"Palmer-Station","kurz":"Palmer","betreiber":"USA","breite":-64.7742,"laenge":-64.0531,"titel":"Das Aquarium","klasse":5,"teile":4,"vor":[{"thema":53,"lernziel":"quader","etappe":"Quader und Würfel beschreiben","flug":"Volumen und Oberfläche"},{"thema":53,"lernziel":"sachaufgaben","etappe":"Oberflächen im Alltag","flug":"Volumen und Oberfläche"},{"thema":1,"lernziel":"aufstellen","etappe":"Textaufgaben als Gleichung","flug":"Einfache Gleichungen"},{"thema":26,"lernziel":"einheit","etappe":"Auf die Einheit schließen","flug":"Direkte Proportionalität und Dreisatz"}]},
  {"schluessel":"5-flug_toronto","nr":2,"station":"McMurdo-Station","kurz":"McMurdo","betreiber":"USA","breite":-77.85,"laenge":166.6667,"titel":"Flug nach Toronto","klasse":5,"teile":5,"vor":[{"thema":25,"lernziel":"zeit","etappe":"Mit Zeit rechnen","flug":"Größen und Einheiten"},{"thema":16,"lernziel":"sach","etappe":"Negative Zahlen im Alltag rechnen","flug":"Ganze Zahlen"},{"thema":60,"lernziel":"zaehlprinzip","etappe":"Das Zählprinzip","flug":"Zählen und Kombinatorik"},{"thema":26,"lernziel":"dreisatz","etappe":"Der Dreisatz","flug":"Direkte Proportionalität und Dreisatz"},{"thema":25,"lernziel":"masse","etappe":"Massen umrechnen","flug":"Größen und Einheiten"}]},
  {"schluessel":"5-kettennachricht","nr":3,"station":"Amundsen-Scott-Südpolstation","kurz":"Amundsen-Scott","betreiber":"USA","breite":-89.9833,"laenge":142.2667,"titel":"Die Kettennachricht","klasse":5,"teile":5,"vor":[{"thema":67,"lernziel":"schreibweise","etappe":"Was ist eine Potenz?","flug":"Potenzen als Schreibweise"},{"thema":67,"lernziel":"berechnen","etappe":"Potenzen ausrechnen","flug":"Potenzen als Schreibweise"},{"thema":15,"lernziel":"ziffern_zu_zahlwort","etappe":"Große Zahlen lesen","flug":"Natürliche Zahlen"},{"thema":25,"lernziel":"zeit","etappe":"Mit Zeit rechnen","flug":"Größen und Einheiten"},{"thema":15,"lernziel":"vergleichen","etappe":"Welche Zahl ist größer?","flug":"Natürliche Zahlen"}]},
  {"schluessel":"5-oase","nr":4,"station":"Maitri-Station (Schirmacher-Oase)","kurz":"Maitri","betreiber":"Indien","breite":-70.7668,"laenge":11.7308,"titel":"In der Oase","klasse":5,"teile":5,"vor":[{"thema":42,"lernziel":"koordinaten","etappe":"Punkte im Koordinatensystem","flug":"Grundbegriffe und Figuren"},{"thema":25,"lernziel":"massstab","etappe":"Maßstab auf Karten und Plänen","flug":"Größen und Einheiten"},{"thema":43,"lernziel":"drehungen","etappe":"Drehungen und Himmelsrichtungen","flug":"Mit Winkeln rechnen"},{"thema":73,"lernziel":"kreislinie","etappe":"Punkte mit festem Abstand zu M","flug":"Ortslinien und Ortsbereiche"},{"thema":73,"lernziel":"zwei_kreise","etappe":"Abstand zu zwei Punkten","flug":"Ortslinien und Ortsbereiche"}]},
  {"schluessel":"5-pyramide","nr":5,"station":"Princess-Elisabeth-Station","kurz":"Princess Elisabeth","betreiber":"Belgien","breite":-71.9499,"laenge":23.3469,"titel":"Die Stufenpyramide","klasse":5,"teile":5,"vor":[{"thema":67,"lernziel":"quadrat","etappe":"Quadratzahlen bis 400","flug":"Potenzen als Schreibweise"},{"thema":18,"lernziel":"vorteil","etappe":"Geschickt: tauschen und verbinden","flug":"Grundrechenarten und Rechengesetze"},{"thema":15,"lernziel":"runden_regel","etappe":"Runden","flug":"Natürliche Zahlen"},{"thema":67,"lernziel":"zehner","etappe":"Zehnerpotenzen für große Zahlen","flug":"Potenzen als Schreibweise"},{"thema":18,"lernziel":"schriftlich","etappe":"Schriftlich mal und geteilt","flug":"Grundrechenarten und Rechengesetze"}]},
  {"schluessel":"5-roemerstrasse","nr":6,"station":"Mario-Zucchelli-Station","kurz":"Mario Zucchelli","betreiber":"Italien","breite":-74.6948,"laenge":164.1133,"titel":"Die Römerstraße","klasse":5,"teile":4,"vor":[{"thema":15,"lernziel":"roemisch_system","etappe":"Warum sind römische Zahlen anders?","flug":"Natürliche Zahlen"},{"thema":25,"lernziel":"laenge","etappe":"Längen umrechnen","flug":"Größen und Einheiten"},{"thema":15,"lernziel":"strahl_ablesen","etappe":"Zahlenstrahl ablesen","flug":"Natürliche Zahlen"},{"thema":17,"lernziel":"vielfache","etappe":"Vielfache","flug":"Teilbarkeit"}]},
  {"schluessel":"5-schatzsuche","nr":7,"station":"Esperanza-Station","kurz":"Esperanza","betreiber":"Argentinien","breite":-63.397,"laenge":-56.9981,"titel":"Die Schatzsuche","klasse":5,"teile":5,"vor":[{"thema":42,"lernziel":"koordinaten","etappe":"Punkte im Koordinatensystem","flug":"Grundbegriffe und Figuren"},{"thema":43,"lernziel":"drehungen","etappe":"Drehungen und Himmelsrichtungen","flug":"Mit Winkeln rechnen"},{"thema":60,"lernziel":"reihenfolgen","etappe":"Reihenfolgen ohne Wiederholung","flug":"Zählen und Kombinatorik"},{"thema":17,"lernziel":"neunerregel","etappe":"Teilbar durch 9","flug":"Teilbarkeit"},{"thema":25,"lernziel":"zeit","etappe":"Mit Zeit rechnen","flug":"Größen und Einheiten"}]},
  {"schluessel":"5-uhrturm","nr":8,"station":"Halley-VI-Station","kurz":"Halley VI","betreiber":"Vereinigtes Königreich","breite":-75.5711,"laenge":-25.4739,"titel":"Der Uhrturm","klasse":5,"teile":4,"vor":[{"thema":43,"lernziel":"uhr","etappe":"Winkel an der Uhr","flug":"Mit Winkeln rechnen"},{"thema":25,"lernziel":"zeit","etappe":"Mit Zeit rechnen","flug":"Größen und Einheiten"},{"thema":17,"lernziel":"vielfache","etappe":"Vielfache","flug":"Teilbarkeit"}]},
  {"schluessel":"5-wetterstation","nr":9,"station":"Neumayer-Station III","kurz":"Neumayer III","betreiber":"Deutschland","breite":-70.6605,"laenge":-8.2841,"titel":"Die Wetterstation","klasse":5,"teile":4,"vor":[{"thema":16,"lernziel":"ordnen","etappe":"Welche Zahl ist kleiner?","flug":"Ganze Zahlen"},{"thema":16,"lernziel":"sach","etappe":"Negative Zahlen im Alltag rechnen","flug":"Ganze Zahlen"},{"thema":18,"lernziel":"geteilt_ganz","etappe":"Ganze Zahlen dividieren","flug":"Grundrechenarten und Rechengesetze"},{"thema":25,"lernziel":"zeit","etappe":"Mit Zeit rechnen","flug":"Größen und Einheiten"}]},
  {"schluessel":"5-zeltplatz","nr":10,"station":"Kohnen-Station","kurz":"Kohnen","betreiber":"Deutschland","breite":-75.0019,"laenge":0.0663,"titel":"Der Zeltplatz","klasse":5,"teile":5,"vor":[{"thema":42,"lernziel":"koordinaten","etappe":"Punkte im Koordinatensystem","flug":"Grundbegriffe und Figuren"},{"thema":50,"lernziel":"rechteck","etappe":"Rechteck und Quadrat berechnen","flug":"Umfang und Flächeninhalt"},{"thema":26,"lernziel":"dreisatz","etappe":"Der Dreisatz","flug":"Direkte Proportionalität und Dreisatz"},{"thema":73,"lernziel":"kreislinie","etappe":"Punkte mit festem Abstand zu M","flug":"Ortslinien und Ortsbereiche"},{"thema":73,"lernziel":"parallelen","etappe":"Punkte mit festem Abstand zu g","flug":"Ortslinien und Ortsbereiche"}]},
  {"schluessel":"8-garten","nr":11,"station":"Troll-Station","kurz":"Troll","betreiber":"Norwegen","breite":-72.0119,"laenge":2.5331,"titel":"Gemüsegarten","klasse":8,"teile":4,"vor":[{"thema":99,"lernziel":"trapez","etappe":"Flächeninhalt des Trapezes","flug":"Flächen von Parallelogramm, Dreieck und Trapez"},{"thema":93,"lernziel":"produkt","etappe":"Produktgleichheit prüfen","flug":"Indirekte Proportionalität"},{"thema":32,"lernziel":"funktionswert","etappe":"Funktionswerte berechnen","flug":"Zuordnung und Funktion"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"}]},
  {"schluessel":"8-handytarif","nr":12,"station":"Rothera-Station","kurz":"Rothera","betreiber":"Vereinigtes Königreich","breite":-67.5695,"laenge":-68.1249,"titel":"Handytarif","klasse":8,"teile":4,"vor":[{"thema":33,"lernziel":"aufstellen","etappe":"Geradengleichung aufstellen","flug":"Lineare Funktionen"},{"thema":33,"lernziel":"graph_ablesen","etappe":"Gerade zeichnen und am Graphen ablesen","flug":"Lineare Funktionen"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"},{"thema":94,"lernziel":"vermehrt","etappe":"Den vermehrten Grundwert berechnen","flug":"Vermehrter und verminderter Grundwert"}]},
  {"schluessel":"8-kerzen","nr":13,"station":"Wostok-Station","kurz":"Wostok","betreiber":"Russland","breite":-78.4642,"laenge":106.8369,"titel":"Kerzenwerkstatt","klasse":8,"teile":4,"vor":[{"thema":100,"lernziel":"quader","etappe":"Volumen von Quader und Würfel","flug":"Volumen"},{"thema":32,"lernziel":"funktionswert","etappe":"Funktionswerte berechnen","flug":"Zuordnung und Funktion"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"},{"thema":33,"lernziel":"schnittpunkte","etappe":"Schnittpunkte berechnen","flug":"Lineare Funktionen"}]},
  {"schluessel":"8-klassenfahrt","nr":14,"station":"Dumont-d’Urville-Station","kurz":"Dumont d’Urville","betreiber":"Frankreich","breite":-66.6628,"laenge":140.0013,"titel":"Klassenfahrt","klasse":8,"teile":4,"vor":[{"thema":93,"lernziel":"sach","etappe":"Sachaufgaben lösen","flug":"Indirekte Proportionalität"},{"thema":33,"lernziel":"aufstellen","etappe":"Geradengleichung aufstellen","flug":"Lineare Funktionen"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"},{"thema":94,"lernziel":"vermindert","etappe":"Den verminderten Grundwert berechnen","flug":"Vermehrter und verminderter Grundwert"}]},
  {"schluessel":"8-pool","nr":15,"station":"Davis-Station","kurz":"Davis","betreiber":"Australien","breite":-68.5759,"laenge":77.9695,"titel":"Gartenpool","klasse":8,"teile":4,"vor":[{"thema":51,"lernziel":"umfang","etappe":"Kreisumfang berechnen","flug":"Kreisberechnungen"},{"thema":101,"lernziel":"zylinder_volumen","etappe":"Zylinder: Volumen begründen","flug":"Prismen und Zylinder"},{"thema":93,"lernziel":"sach","etappe":"Sachaufgaben lösen","flug":"Indirekte Proportionalität"},{"thema":51,"lernziel":"flaeche","etappe":"Flächeninhalt eines Kreises","flug":"Kreisberechnungen"}]},
  {"schluessel":"8-radtour","nr":16,"station":"Casey-Station","kurz":"Casey","betreiber":"Australien","breite":-66.2823,"laenge":110.5268,"titel":"Radtour zum See","klasse":8,"teile":4,"vor":[{"thema":25,"lernziel":"massstab","etappe":"Maßstab auf Karten und Plänen","flug":"Größen und Einheiten"},{"thema":93,"lernziel":"sach","etappe":"Sachaufgaben lösen","flug":"Indirekte Proportionalität"},{"thema":33,"lernziel":"zwei_punkte","etappe":"Steigung aus zwei Punkten","flug":"Lineare Funktionen"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"}]},
  {"schluessel":"8-roller","nr":17,"station":"Mawson-Station","kurz":"Mawson","betreiber":"Australien","breite":-67.6026,"laenge":62.873,"titel":"Sparen für den Roller","klasse":8,"teile":4,"vor":[{"thema":32,"lernziel":"wertetabelle","etappe":"Wertetabellen lesen und ergänzen","flug":"Zuordnung und Funktion"},{"thema":33,"lernziel":"schnittpunkte","etappe":"Schnittpunkte berechnen","flug":"Lineare Funktionen"},{"thema":24,"lernziel":"rabatt_aufschlag","etappe":"Rabatt und Aufschlag","flug":"Prozent- und Zinsrechnung"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"}]},
  {"schluessel":"8-saftbar","nr":18,"station":"Syowa-Station","kurz":"Syowa","betreiber":"Japan","breite":-69.0041,"laenge":39.5818,"titel":"Saftbar","klasse":8,"teile":4,"vor":[{"thema":5,"lernziel":"verhaeltnis","etappe":"Verhältnisgleichungen","flug":"Bruch- und Verhältnisgleichungen"},{"thema":5,"lernziel":"ein_bruch","etappe":"Bruchgleichungen mit einem Bruch","flug":"Bruch- und Verhältnisgleichungen"},{"thema":6,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit zwei Unbekannten","flug":"Gleichungssysteme mit 2 Unbekannten"},{"thema":26,"lernziel":"sach","etappe":"Sachaufgaben mit Dreisatz","flug":"Direkte Proportionalität und Dreisatz"}]},
  {"schluessel":"8-schuelerzeitung","nr":19,"station":"Zhongshan-Station","kurz":"Zhongshan","betreiber":"China","breite":-69.3732,"laenge":76.3719,"titel":"Schülerzeitung","klasse":8,"teile":4,"vor":[{"thema":31,"lernziel":"termwert","etappe":"Werte von Bruchtermen berechnen","flug":"Bruchterme"},{"thema":5,"lernziel":"ein_bruch","etappe":"Bruchgleichungen mit einem Bruch","flug":"Bruch- und Verhältnisgleichungen"},{"thema":34,"lernziel":"asymptoten","etappe":"Asymptoten bestimmen","flug":"Gebrochen-rationale Funktionen"},{"thema":33,"lernziel":"schnittpunkte","etappe":"Schnittpunkte berechnen","flug":"Lineare Funktionen"}]},
  {"schluessel":"8-schulfest","nr":20,"station":"Arctowski-Station","kurz":"Arctowski","betreiber":"Polen","breite":-62.1598,"laenge":-58.4733,"titel":"Schulfest","klasse":8,"teile":4,"vor":[{"thema":61,"lernziel":"laplace","etappe":"Laplace-Wahrscheinlichkeit","flug":"Zufall und Laplace"},{"thema":61,"lernziel":"grosse_zahlen","etappe":"Gesetz der großen Zahlen","flug":"Zufall und Laplace"},{"thema":6,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit zwei Unbekannten","flug":"Gleichungssysteme mit 2 Unbekannten"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"}]},
  {"schluessel":"8-zelt","nr":21,"station":"Scott Base","kurz":"Scott Base","betreiber":"Neuseeland","breite":-77.8494,"laenge":166.7673,"titel":"Zelt","klasse":8,"teile":4,"vor":[{"thema":52,"lernziel":"prisma","etappe":"Prismen: Ecken, Kanten, Flächen","flug":"Körper darstellen"},{"thema":101,"lernziel":"prisma_volumen","etappe":"Volumen eines Prismas","flug":"Prismen und Zylinder"},{"thema":101,"lernziel":"prisma_oberflaeche","etappe":"Oberfläche eines Prismas","flug":"Prismen und Zylinder"},{"thema":3,"lernziel":"sachaufgabe","etappe":"Sachaufgaben mit Ungleichungen","flug":"Lineare Ungleichungen"}]},
];
// </EX-STATIONEN>
const lernExStation = (x) => LERN_EX_STATIONEN.find((s) => s.schluessel === x?.schluessel) || null;
const lernExGesamt = (d) => Number(d?.exStand?.stationen_gesamt) || LERN_EX_STATIONEN.length;
const lernExGeschafftZahl = (d) => (d?.exStand ? Number(d.exStand.stationen_geschafft) || 0 : (d?.expeditionen || []).filter((x) => x.zustand === 'geschafft').length);
const lernExTeile = (x) => Number(x?.teile_gesamt) || (x?.teile || []).length || Number(lernExStation(x)?.teile) || 0;
const lernExBuchstabe = (i) => String.fromCharCode(97 + Math.max(0, i));
const lernExTeilK = (x) => { const t = x?.teile || []; const i = t.findIndex((y) => !y.erledigt); return i < 0 ? t.length : i; }; // 0-basiert: Index des nächsten Teils
const lernExMinuten = (n) => `etwa ${Math.max(5, Math.round(n * 4 / 5) * 5)} Minuten`; // Annahme Vorgabe: 4 Minuten je Teil, auf 5 gerundet
const lernExNochFehlerfrei = (x) => (x?.teile || []).every((t) => !t.erledigt || t.richtig_erst);
const lernExMitLohn = (x) => x && ('sterne_geschafft' in x || 'angeboten_am' in x); // EX-S: neue Felder; alter Server → ohne Belohnungs-Zeile
const lernExOffen = (x) => x && (x.zustand === 'angeboten' || x.zustand === 'begonnen');
const lernExOrtZeile = (x) => { const s = lernExStation(x); return s ? `${s.station} · Antarktis` : 'Antarktis'; };
// Die oberste Karte: Server (expeditionen_stand.oben_id), sonst die erste offene, nicht ausgeblendete (Liste ist schon sortiert: begonnen → angeboten)
function lernExOben(d) {
  const xs = d.expeditionen || [];
  if (d.exStand && 'oben_id' in d.exStand) return d.exStand.oben_id ? xs.find((x) => x.id === Number(d.exStand.oben_id)) || null : null;
  return xs.find((x) => lernExOffen(x) && !x.ausgeblendet) || null;
}
const lernExWartet = (d) => (d.expeditionen || []).find((x) => lernExOffen(x) && x.ausgeblendet) || null;
// Kleiner Stempel (rund, Stempel-Blau); ff = mit Band „★ FEHLERFREI“
function lernExStempel(s, { gross = false, klein = false, ff = false, datum = '' } = {}) {
  return el('span', { class: 'lr-ex-stempel' + (gross ? ' gross' : '') + (klein ? ' klein' : '') + (ff ? ' ff' : ''), 'aria-hidden': 'true' },
    el('span', { class: 'gr' }, 'ANTARKTIS'), el('b', {}, klein ? String(s?.nr ?? '') : String(s?.kurz || s?.station || 'Station').toUpperCase()),
    el('span', { class: 'nr' }, klein ? '✓' : `STATION ${s?.nr ?? '?'}${datum ? ' · ' + datum : ''}`), ff ? el('span', { class: 'band' }, '★ FEHLERFREI') : null);
}
const LERN_EX_SZENE = '<svg viewBox="0 0 400 140" preserveAspectRatio="none"><path d="M0 70 L60 44 L110 66 L170 30 L230 62 L290 40 L350 64 L400 52 L400 140 L0 140Z" fill="#DCEFF5"/><path d="M0 96 Q120 80 220 92 T400 88 L400 140 L0 140Z" fill="#F2FAFC"/></svg>';
const LERN_EX_STATION_BILD = '<svg viewBox="0 0 120 80"><rect x="8" y="34" width="84" height="26" rx="3" fill="#F2F6F8"/><rect x="8" y="30" width="84" height="7" fill="#E5484D"/><rect x="18" y="42" width="10" height="7" fill="#2FB9D6"/><rect x="36" y="42" width="10" height="7" fill="#2FB9D6"/><rect x="54" y="42" width="10" height="7" fill="#2FB9D6"/><rect x="14" y="60" width="4" height="14" fill="#9DB2C2"/><rect x="82" y="60" width="4" height="14" fill="#9DB2C2"/><rect x="104" y="12" width="2.5" height="62" fill="#F2F6F8"/><path d="M106.5 14 L120 18 L106.5 23Z" fill="#fff"/><circle cx="105" cy="10" r="3.5" fill="#4BE3A6"/></svg>';
function lernExSzene(fehlerfrei = false) {
  return [el('div', { class: 'lr-ex-licht' + (fehlerfrei ? ' voll' : ''), 'aria-hidden': 'true' }), el('div', { class: 'lr-ex-schnee', 'aria-hidden': 'true' }),
    lernGrafik(LERN_EX_SZENE, 'lr-ex-eis'), lernGrafik(LERN_EX_STATION_BILD, 'lr-ex-station')];
}
// Ansicht 1 – „Expedition freigeschaltet“ (Ereignis). bewegt: nur beim Freischalten; aus der Sammlung/dem Chip ohne Bewegung.
function lernExFreiAnsicht({ d, x, bewegt = true, weitere = 0, jetzt, spaeter }) {
  const s = lernExStation(x); const n = lernExTeile(x); const k = lernExTeilK(x); const begonnen = x.zustand === 'begonnen';
  const vor = s?.vor || [];
  const mitLohn = lernExMitLohn(x);
  const g = Number(x.sterne_geschafft ?? d.regeln?.sterne_expedition_geschafft ?? 150), f = Number(x.sterne_fehlerfrei ?? d.regeln?.sterne_expedition_fehlerfrei ?? 200);
  return el('div', { class: 'lr-ab-app lr-ex-app lr-ex-frei' + (bewegt ? ' lr-ab-anim' : '') },
    el('div', { class: 'lr-ab-szene lr-ex-szene' }, ...lernExSzene(),
      el('div', { class: 'lr-ab-oben' }, `ANTARKTIS · STATION ${s?.nr ?? '?'} VON ${lernExGesamt(d)}`),
      el('h2', { class: 'lr-ab-titel lr-ex-titel' }, 'Expedition freigeschaltet'),
      el('p', { class: 'lr-ab-unter lr-ex-satz' }, el('b', {}, x.titel), s ? ` an der ${s.station}.` : '.', n ? ` ${n} Teile, a bis ${lernExBuchstabe(n - 1)} – alles, was du dafür brauchst, hast du gelandet.` : ''),
      // EX S1: unter 700 px Höhe höchstens 2 Chips + „+n weitere“ (sonst liegen sie unter Boden und Blatt)
      vor.length ? el('div', { class: 'lr-ex-chips' }, ...(innerHeight < 700 && vor.length > 2 ? [...vor.slice(0, 2).map((v) => el('span', { class: 'lr-ex-chip' }, '✓ ', v.etappe)), el('span', { class: 'lr-ex-chip' }, `+${vor.length - 2} weitere`)]
        : vor.map((v) => el('span', { class: 'lr-ex-chip' }, '✓ ', v.etappe)))) : null),
    el('div', { class: 'lr-ab-blatt lr-ex-blatt' },
      mitLohn ? el('div', { class: 'lr-ex-lohn' },
        el('div', { class: 'lr-ex-k' }, el('span', { class: 'lr-ex-zahl' }, `★ ${lernZahl(g)}`), el('span', { class: 'lr-ex-was' }, 'für die Expedition', el('br'), `★ ${lernZahl(f)}, wenn alle Teile im ersten Versuch ohne Tipp klappen`)),
        el('div', { class: 'lr-ex-k lr-ex-k-stempel' }, lernExStempel(s, { klein: false }), el('span', { class: 'lr-ex-was' }, 'Neuer Stempel für deine Sammlung'))) : null,
      weitere > 0 ? el('p', { class: 'lr-ab-leise lr-ex-weitere' }, `+${weitere} weitere ${weitere === 1 ? 'Expedition' : 'Expeditionen'} freigeschaltet`) : null,
      lernGrossKnopf(begonnen ? `Weiter mit Teil ${lernExBuchstabe(k)}` : 'Jetzt starten', n ? `Teil ${lernExBuchstabe(k)} von ${n} · ${lernExMinuten(Math.max(1, n - k))}` : null, { class: 'lr-ex-gross', onclick: jetzt }),
      el('button', { type: 'button', class: 'lr-ab-pause lr-ex-spaeter', onclick: spaeter }, 'Später')));
}
// „Später“: Server blendet bis zum Ende des Lerntags aus (sperrt nichts). Fehler → trotzdem weiter (nichts geht verloren).
async function lernExSpaeter(kindId, x) {
  try { const r = await lernCall('schule_expedition_spaeter', { lernender_id: kindId, expedition_id: x.id }); x.ausgeblendet = true; x.spaeter_bis = r?.spaeter_bis ?? x.spaeter_bis; return r; }
  catch { return null; }
}
const lernExGesehenSchl = (kindId, id) => `lern.exfrei.${kindId}.${id}`;
const lernExGesehen = (kindId, id) => { try { return !!localStorage.getItem(lernExGesehenSchl(kindId, id)); } catch { return false; } };
const lernExGesehenSetzen = (kindId, id) => { try { localStorage.setItem(lernExGesehenSchl(kindId, id), '1'); } catch { /* egal */ } };
// Noch nicht gezeigte, frisch freigeschaltete Expeditionen (nur neuer Server: angeboten_am), kleinste Stationsnummer zuerst
function lernExNeuFrei(d) {
  const nr = (x) => lernExStation(x)?.nr ?? 999;
  return (d.expeditionen || []).filter((x) => x.zustand === 'angeboten' && x.angeboten_am && !x.ausgeblendet && !lernExGesehen(d.kind.id, x.id)).sort((a, b) => nr(a) - nr(b));
}
// Zeigt Ansicht 1 als Vollbild. weiter(): wohin „Später“ führt.
function lernExFreiZeigen(d, x, { bewegt = true, weitere = 0, weiter, spaeterRufen = true } = {}) {
  const kindId = d.kind.id;
  const h = lernAbschlussZeigen(d.kind, lernExFreiAnsicht({ d, x, bewegt, weitere,
    jetzt: () => { lernAbschlussZu(); route('expedition', `${kindId}-${x.id}`); },
    spaeter: async (ev) => { ev.currentTarget.disabled = true; if (spaeterRufen) await lernExSpaeter(kindId, x); lernAbschlussZu(); weiter?.(); } }), { label: 'Expedition freigeschaltet' });
  if (!bewegt) h.classList.add('lr-ab-fertig');
  return h;
}
// Beim Öffnen der Startseite: einmal je Kind und Expedition (Freischalten ohne Landung: Teilung, „Kann er“, neue Expedition)
function lernExFreiBeimStart(d) {
  const neu = lernExNeuFrei(d); if (!neu.length || document.querySelector('.lr-abschluss')) return;
  neu.forEach((x) => lernExGesehenSetzen(d.kind.id, x.id));
  lernExFreiZeigen(d, neu[0], { weitere: neu.length - 1, weiter: () => render() });
}
// Nach der Landung (Etappe gelandet): Der große Knopf der Landungs-Ansicht führt zuerst zu Ansicht 1, wenn diese Landung eine Expedition freigeschaltet hat.
// Der Server legt das Angebot beim Landen an (Auslöser auf karte_stand.sitzt); die App liest schule_konto einmal nach.
function lernExNachLandung(ctx) {
  return lernCall('schule_konto', { lernender_id: ctx.kind }).then((k) => {
    const d = { kind: ctx.kindObj, expeditionen: Array.isArray(k?.expeditionen) ? k.expeditionen : [], exStand: k?.expeditionen_stand || null, regeln: k?.regeln || null };
    return lernExNeuFrei(d).length ? d : null;
  }).catch(() => null);
}
function lernExVorKnopf(knopf, warten) {
  if (!knopf || !warten) return knopf;
  knopf.addEventListener('click', async (ev) => {
    if (knopf.dataset.exWeiter) return;
    ev.preventDefault(); ev.stopImmediatePropagation();
    const d = await warten; const neu = d ? lernExNeuFrei(d) : [];
    const weiter = () => { knopf.dataset.exWeiter = '1'; if (knopf.tagName === 'A') { location.hash = knopf.getAttribute('href'); } else knopf.click(); };
    if (!neu.length) { weiter(); return; }
    neu.forEach((x) => lernExGesehenSetzen(d.kind.id, x.id));
    lernExFreiZeigen(d, neu[0], { weitere: neu.length - 1, weiter });
  }, true);
  return knopf;
}
// Ansicht 2 – oberste, größte Karte der Abflugtafel; 2b – nach „Später“ ein Chip bis Lerntag-Ende
function lernExKarte(d) {
  const x = lernExOben(d); const kindId = d.kind.id;
  if (!x) {
    const w = lernExWartet(d); if (!w) return null;
    return el('button', { type: 'button', class: 'lr-ex-wartet', onclick: () => lernExFreiZeigen(d, w, { bewegt: false, spaeterRufen: false }) },
      el('span', { 'aria-hidden': 'true' }, '⛯ '), 'Expedition wartet: ', el('b', {}, w.titel), ' ›');
  }
  const s = lernExStation(x); const n = lernExTeile(x); const k = lernExTeilK(x); const begonnen = x.zustand === 'begonnen';
  const heute = d.exStand?.heute; const neu = !begonnen && heute && String(x.angeboten_am || '').slice(0, 10) === String(heute).slice(0, 10);
  const weitere = Math.max(0, (Number(d.exStand?.angeboten) || (d.expeditionen || []).filter(lernExOffen).length) - 1);
  const mitLohn = lernExMitLohn(x); const ff = lernExNochFehlerfrei(x);
  const g = Number(x.sterne_geschafft ?? 150), f = Number(x.sterne_fehlerfrei ?? 200);
  const ziel = `#/expedition/${kindId}-${x.id}`;
  return el('section', { class: 'lr-ex-karte', 'aria-label': 'Expedition freigeschaltet' },
    el('div', { class: 'lr-ex-karte-kopf' }, el('span', { class: 'lr-ex-ueber' }, el('span', { 'aria-hidden': 'true' }, '⛯ '), begonnen ? `EXPEDITION · TEIL ${lernExBuchstabe(k).toUpperCase()} VON ${n}` : 'EXPEDITION FREIGESCHALTET'), neu ? el('span', { class: 'lr-ex-neu' }, 'NEU') : null,
      x.angeboten_am !== undefined ? el('button', { type: 'button', class: 'lr-ex-zu', 'aria-label': 'Später', title: 'Später', onclick: async (ev) => { ev.currentTarget.disabled = true; await lernExSpaeter(kindId, x); render(); } }, '✕') : null),
    el('h2', { class: 'lr-ex-karte-titel' }, x.titel),
    el('p', { class: 'lr-ex-karte-ort' }, [s?.station, 'Antarktis', s ? `Station ${s.nr} von ${lernExGesamt(d)}` : null].filter(Boolean).join(' · ')),
    el('div', { class: 'lr-ex-karte-mitte' },
      el('div', { class: 'lr-ex-teile', role: 'img', 'aria-label': `${(x.teile || []).filter((t) => t.erledigt).length} von ${n} Teilen gelöst` },
        ...Array.from({ length: n }, (_, i) => el('i', { class: (x.teile?.[i]?.erledigt ? 'ok' : i === k ? 'jetzt' : '') }, lernExBuchstabe(i)))),
      mitLohn ? el('div', { class: 'lr-ex-karte-lohn' }, el('b', {}, `★ ${lernZahl(g)}`), ff ? el('small', {}, `★ ${lernZahl(f)} ohne Fehler`) : null) : null),
    el('a', { class: 'lr-ex-knopf', href: ziel }, el('span', {}, el('b', {}, begonnen ? `Weiter mit Teil ${lernExBuchstabe(k)}` : 'Expedition starten'),
      n ? el('small', {}, `Teil ${lernExBuchstabe(k)} von ${n} · ${lernExMinuten(Math.max(1, n - k))}`) : null), el('span', { 'aria-hidden': 'true' }, '›')),
    weitere ? el('a', { class: 'lr-ex-mehr', href: `#/stationen/${kindId}` }, `+${weitere} weitere ${weitere === 1 ? 'wartet' : 'warten'} im Reisepass`) : null);
}
// Ansicht 3 – nach geschaffter Expedition (3a 150 ★, 3b fehlerfrei 200 ★). Sterne kommen vom Server.
function lernExGeschafftAnsicht({ d, x, sterne, fehlerfrei }) {
  const s = lernExStation(x); const n = lernExTeile(x); const gesamt = lernExGesamt(d); const kindId = d.kind.id;
  const k = Math.max(lernExGeschafftZahl(d), 1);
  const offenNoch = gesamt > k;
  const nf = d.naechste;
  const g = Number(x.sterne_geschafft ?? 150), f = Number(x.sterne_fehlerfrei ?? 200);
  const knopf = nf ? lernGrossKnopf(nf.laeuft ? 'Weiter: Flug-Test' : `Weiter in ${nf.stadt || nf.ort_titel || nf.titel}`,
    nf.laeuft ? nf.titel : `${nf.titel}${nf.n ? ` · Etappe ${Math.min((nf.fertig || 0) + 1, nf.n)} von ${nf.n}` : ''}`, { href: nf.laeuft ? `#/lerneinheit/${kindId}-${nf.id}-test` : lernUebenZiel(kindId, nf), class: 'lr-ex-weiter' })
    : lernGrossKnopf('Zur Reise', null, { href: `#/reise/${kindId}`, class: 'lr-ex-weiter' });
  return el('div', { class: 'lr-ab-app lr-ex-app lr-ex-geschafft lr-ab-anim' + (fehlerfrei ? ' lr-ex-ff' : '') },
    el('a', { class: 'lr-ab-skip', href: `#/reise/${kindId}` }, 'Überspringen ›'),
    el('div', { class: 'lr-ab-szene lr-ex-szene lr-jw-mit' }, ...lernExSzene(fehlerfrei),
      el('div', { class: 'lr-ab-oben' }, `ANTARKTIS · STATION ${s?.nr ?? '?'} VON ${gesamt}`),
      el('h2', { class: 'lr-ab-titel lr-ex-titel' }, fehlerfrei ? 'Fehlerfrei durchgekommen' : 'Expedition geschafft'),
      el('p', { class: 'lr-ab-unter lr-ex-satz' }, el('b', {}, x.titel), fehlerfrei ? ` – alle ${n} Teile im ersten Versuch, ohne Tipp.` : ` – alle ${n} Teile gelöst.`),
      el('div', { class: 'lr-ex-knall' }, lernExStempel(s, { gross: true, ff: fehlerfrei, datum: lernStempelDatum(new Date()) })),
      lernJwPlatz(kindId, fehlerfrei ? 'expedition_fehlerfrei' : 'expedition_geschafft')),
    el('div', { class: 'lr-ab-blatt lr-ex-blatt' },
      el('div', { class: 'lr-ex-lohn' },
        el('div', { class: 'lr-ex-k' }, el('span', { class: 'lr-ex-zahl' }, '★ +', el('span', { 'data-ziel': String(sterne) }, lernZahl(sterne))),
          fehlerfrei ? el('span', { class: 'lr-ex-was' }, `${lernZahl(g)} für die Expedition`, el('br'), `+ ${lernZahl(Math.max(0, sterne - g))} fürs fehlerfreie Lösen`) : el('span', { class: 'lr-ex-was' }, 'für die Expedition')),
        el('a', { class: 'lr-ex-k lr-ex-k-samml', href: `#/stationen/${kindId}` }, el('span', { class: 'lr-ex-zahl lr-ex-zahl-blau' }, `${k} / ${gesamt}`), el('span', { class: 'lr-ex-was' }, 'Stationen in deiner Sammlung'))),
      !fehlerfrei && offenNoch ? el('p', { class: 'lr-ab-leise' }, `Bei der nächsten Expedition gibt es ★ ${lernZahl(f)}, wenn alle Teile im ersten Versuch ohne Tipp klappen.`) : null,
      knopf,
      el('a', { class: 'lr-ab-pause', href: `#/stationen/${kindId}` }, 'Stempel-Sammlung ansehen')));
}
async function viewExpedition(arg) {
  setChrome('Expedition', { back: true, showTabs: false });
  const live = viewGuard();
  const [kidArg, xArg] = String(arg || '').split('-');
  loading();
  const d = await lernLadeKind(kidArg);
  if (!d || !live()) return;
  const x = d.expeditionen.find((e) => e.id === Number(xArg));
  const { kind } = d;
  if (!x) { lernErsetze(main, lernRahmen(kind, 'reise', el('section', { class: 'lr-karte-box' }, el('p', {}, 'Diese Expedition ist gerade nicht offen.'),
    el('a', { class: 'lr-knopf-zweit', href: `#/reise/${kind.id}` }, 'Zur Abflugtafel')))); return; }
  $('#title').textContent = 'Expedition ' + x.titel;
  const s = lernExStation(x);
  const flaeche = el('div', { class: 'lr-expedition-teile' });
  const schonGeschafft = x.zustand === 'geschafft';
  let letzte = null; // Antwort des letzten Teils (Sterne, falls schule_konto nicht antwortet)
  const erledigtZeile = (t) => el('div', { class: 'lr-exp-teil erledigt' },
    el('p', { class: 'lr-ueber' }, `TEIL ${String(t.k || '').toUpperCase()}`, t.richtig_erst ? ' ✓' : ''),
    el('p', {}, ...lernMarkiert(t.frage?.text || '')),
    t.loesung ? el('p', {}, el('b', {}, 'Lösung: '), lernMathe(lernLoesungText(t))) : null,
    t.loesungsweg ? el('p', { class: 'lr-leise' }, lernMathe(t.loesungsweg)) : null);
  // Ansicht 3 einmal je Kind und Expedition: Sterne und „fehlerfrei“ aus dem Server (schule_konto), sonst aus der Antwort des letzten Teils
  const abschluss = async () => {
    let xs = x, dd = d;
    try { const k = await lernCall('schule_konto', { lernender_id: kind.id }); const y = (k?.expeditionen || []).find((e) => e.id === x.id);
      if (y) { xs = { ...x, ...y }; dd = { ...d, expeditionen: k.expeditionen, exStand: k.expeditionen_stand || d.exStand }; } } catch { /* Antwort des Teils */ }
    const sterne = Number(xs.sterne ?? letzte?.expedition?.sterne ?? 0) || Number(xs.sterne_geschafft ?? 150);
    const fehlerfrei = xs.fehlerfrei !== undefined ? !!xs.fehlerfrei : letzte?.expedition?.fehlerfrei !== undefined ? !!letzte.expedition.fehlerfrei : (x.teile || []).every((t) => t.richtig_erst);
    try { localStorage.setItem(`lern.exfertig.${kind.id}.${x.id}`, '1'); } catch { /* egal */ }
    if (!live()) return;
    lernAbschlussZeigen(kind, lernExGeschafftAnsicht({ d: dd, x: xs, sterne, fehlerfrei }), { label: fehlerfrei ? 'Fehlerfrei durchgekommen' : 'Expedition geschafft' });
  };
  const zeichne = () => {
    const teile = x.teile || []; const i = teile.findIndex((t) => !t.erledigt);
    if (i < 0) {
      const ff = x.fehlerfrei === true || (!('fehlerfrei' in x) && teile.every((t) => t.richtig_erst));
      lernErsetze(flaeche, ...teile.map(erledigtZeile), el('section', { class: 'lr-karte-box lr-expedition-fertig' },
        el('p', { class: 'lr-ueber' }, '⛯ EXPEDITION GESCHAFFT'), el('p', {}, el('b', {}, x.titel), ff ? ' – alle Teile im ersten Versuch, ohne Tipp.' : ' – alle Teile gelöst.'),
        el('a', { class: 'lr-knopf-zweit', href: `#/stationen/${kind.id}` }, 'Stempel-Sammlung ansehen ›')));
      return;
    }
    const t = teile[i]; const auf = lernAufgabe(t, null, { tasten: false }); const cid = lernCid();
    let anlauf = 1, hilfe = 0; const zweiteChance = !(t.antworttyp === 'auswahl' && (t.antworten || []).length <= 2);
    const meldung = el('div', { role: 'status', 'aria-live': 'polite' }); const hilfeBox = el('div', { class: 'lr-hilfebox' });
    const tipp = t.tipp ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { hilfe = 1; tipp.remove(); lernAnhaengen(hilfeBox, el('p', { class: 'lr-tipp' }, el('b', {}, 'Tipp: '), lernMathe(t.tipp))); } }, 'Tipp') : null;
    const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
    pruefen.addEventListener('click', async () => {
      const w = auf.antwort();
      if (!w) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
      pruefen.disabled = true;
      try {
        const r = await lernCall('schule_uebung_pruefen', { lernender_id: kind.id, aufgabe_id: t.id, antwort: w, client_id: cid + '-' + anlauf, hilfe, ...(zweiteChance ? { anlauf } : {}) });
        if (!r.format_ok) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, r.hinweis || 'Bitte prüfe die Eingabe.')); pruefen.disabled = false; return; }
        if (r.nochmal) { anlauf = 2; lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, 'Noch nicht – schau noch einmal hin. Du hast einen zweiten Versuch.')); pruefen.disabled = false; return; }
        // Teil erledigt: Lösung zeigen; der nächste Teil nennt seine Werte selbst – ein Fehler hier blockiert nichts
        t.erledigt = true; t.loesung = r.loesung; t.loesungsweg = r.loesungsweg; t.richtig_erst = !!r.richtig && !hilfe && anlauf === 1;
        letzte = r;
        auf.zeigeLoesung?.(r.loesung); pruefen.remove(); tipp?.remove();
        const naechster = (x.teile || []).find((y) => !y.erledigt);
        lernErsetze(meldung, el('div', { class: 'lr-rueck' + (r.richtig ? ' lr-rueck-ok' : '') },
          el('b', {}, r.richtig ? 'Richtig!' : 'Diesmal nicht – so geht’s:'),
          !r.richtig ? el('p', {}, 'Richtig ist: ', lernMathe(lernLoesungText(t))) : null,
          r.loesungsweg ? el('p', {}, lernMathe(r.loesungsweg)) : null,
          !r.richtig ? el('p', { class: 'lr-leise' }, 'Keine Abzüge – im nächsten Teil geht es mit den richtigen Zahlen weiter.') : null,
          el('button', { type: 'button', class: 'lr-knopf', onclick: () => { zeichne(); window.scrollTo?.(0, 0); if (!naechster) abschluss(); } }, naechster ? `Weiter mit Teil ${String(naechster.k || '').toUpperCase()} ›` : 'Zum Abschluss ›')));
      } catch (err) { if (lernGesperrt(err)) { render(); return; } lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
    });
    lernErsetze(flaeche, ...teile.slice(0, i).map(erledigtZeile),
      el('section', { class: 'lr-karte-box lr-aufgabe lr-bordkarte lr-exp-teil' },
        el('div', { class: 'lr-bord-kopf' }, el('span', {}, `TEIL ${String(t.k || i + 1).toUpperCase()} VON ${teile.length}`), el('span', { 'aria-hidden': 'true' }, '⛯')),
        auf.node, el('div', { class: 'lr-knopfzeile' }, pruefen, tipp)), hilfeBox, meldung);
  };
  zeichne();
  const nf = d.naechste; // sperrt nichts: der nächste Flug ist mit einem Tipp erreichbar
  lernErsetze(main, lernRahmen(kind, 'reise',
    el('header', { class: 'lr-kopf lr-ex-kopf' }, el('p', { class: 'lr-ueber' }, schonGeschafft ? '⛯ EXPEDITION GESCHAFFT' : x.zustand === 'begonnen' ? '⛯ EXPEDITION' : '⛯ EXPEDITION FREIGESCHALTET'), el('h1', {}, x.titel),
      s ? el('p', { class: 'lr-leise' }, `${s.station} · Antarktis · Station ${s.nr} von ${lernExGesamt(d)}`) : null),
    el('section', { class: 'lr-karte-box lr-exp-einleitung' }, el('p', {}, ...lernMarkiert(x.einleitung || '')), x.grafik ? lernBild(x.grafik) : null,
      schonGeschafft ? null : el('p', { class: 'lr-leise' }, 'Du kannst jederzeit aufhören – erledigte Teile bleiben gespeichert.')),
    flaeche,
    el('a', { class: 'lr-textlink lr-ex-flug', href: nf ? (nf.laeuft ? `#/lerneinheit/${kind.id}-${nf.id}-test` : lernUebenZiel(kind.id, nf)) : `#/reise/${kind.id}` }, nf ? `Zum Flug: weiter in ${nf.stadt || nf.titel} ›` : 'Zur Abflugtafel ›')));
}
// Ansicht 4 – Stempel-Sammlung (Reisepass · Expeditionen). Gesperrte Stationen zeigen, was fehlt (Stand je Etappe aus schule_reise_karte, wenn da).
// RK: Karten-Antwort (~170 KB) je Kind einmal je Sitzung laden und merken. Nach einer Änderung für das Kind (Landung, Plan …) gilt sie als alt:
// die Ansicht zeigt sofort die alte und holt im Hintergrund die neue (lernReiseKarteFrisch).
const lernReiseKarteSpeicher = new Map(); // Kind → Promise
const lernReiseKarteAlt = new Map(); // Kind → letzte Antwort
// ---------- WK (0.93.2): ein Name und ein Ziel je Flug – wie auf der Reisekarte ----------
// F1: Jeder Knopf, der eine Stadt nennt, führt genau in die Etappe dieser Stadt (…-ueben-<nr>): die nächste offene Pflicht-Etappe
// (Merkheft-Stand der Einheit, sonst Städte-Stand der Karte). F3: Land und Stadt kommen aus schule_reise_karte (Thema des Flugs);
// der alte Ortsname (Block-Stadt aus schule_uebersicht) nur, wenn die Karte keinen Namen liefert.
function lernRkFlugVon(kindId, themaId) {
  const k = lernReiseKarteAlt.get(Number(kindId)); if (!k || !themaId) return null;
  for (const ko of k.kontinente || []) for (const f of ko.fluege || []) if (Number(f.thema_id) === Number(themaId)) return f;
  return null;
}
function lernNaechsteEtappeNr(m) {
  const es = m?.etappen || []; if (!es.length) return null; const offen = (x) => !m.stand?.[x.lernziel]?.fertig;
  let i = es.findIndex((x) => offen(x) && x.pflicht !== false && m.stand?.[x.lernziel]?.pflicht !== false); if (i < 0) i = es.findIndex(offen);
  return i >= 0 ? i + 1 : null;
}
function lernFlugOrt(kindId, e, m = null) {
  if (!e) return { land: null, stadt: '', nr: null, flug: null };
  const f = lernRkFlugVon(kindId, e.thema_id); const st = (f?.staedte || []).slice().sort((a, b) => Number(a.nr) - Number(b.nr));
  let nr = lernNaechsteEtappeNr(m);
  if (!nr && st.length) { const c = st.find((x) => x.pflicht !== false && (!x.stand || x.stand === 'offen')) || st.find((x) => !['gelandet', 'sicher'].includes(x.stand)); nr = c ? Number(c.nr) : null; }
  const stadtK = nr ? st.find((x) => Number(x.nr) === nr)?.name : null;
  return { land: f?.land || null, stadt: stadtK || e.stadt || e.ort_titel || e.titel || '', nr, flug: f, ausKarte: !!f };
}
// Namen der Karte in die Einheiten der Kinderseite übernehmen (Kopien aus lernReiseDaten): stadt = Stadt der nächsten offenen Etappe bzw. Land,
// land = Land, etappeNr = Ziel der „Weiter in …“-Knöpfe; ortAlt behält den alten Ortsnamen (nur für Stellen ohne Karten-Namen)
function lernNamenSetzen(d) {
  for (const e of d?.mit || []) { if (e.ortAlt === undefined) e.ortAlt = e.stadt;
    const o = lernFlugOrt(d.kind.id, { ...e, stadt: e.ortAlt }, (d.merk || []).find((m) => Number(m.einheit_id) === Number(e.id)) || null);
    e.etappeNr = o.nr; if (o.ausKarte) { e.stadt = o.nr ? o.stadt : o.land || e.ortAlt; e.land = o.land || e.land; } }
  return d;
}
// ---------- WK 2 (0.93.4): ein Hauptknopf, immer der richtige nächste Schritt ----------
// Reihenfolge: (Nachbessern – eigene Karte, zuerst) · laufender Test · Flug „dran“ mit offener Pflicht-Etappe · Flug „dran“, alles gelandet, Test fehlt
// · nächster Flug laut Plan (auch der zweite Flug desselben Plan-Platzes). Abgeleitet aus den Ständen der Reisekarte (staedte[].stand, stempel),
// nicht aus naechster_start.stadt (fällt beim Server ohne offene Stadt auf Stadt 1 zurück). Ohne Karte bzw. ohne Zuordnung Flug → Einheit: null (wie bisher).
const lernStadtGelandet = (c) => !!c && (c.abgelegt || ['gelandet', 'sicher', 'wieder_offen'].includes(c.stand));
function lernSchritt(d, karte) {
  const mit = d?.mit || [];
  const lauf = mit.find((e) => e.laeuft);
  if (lauf) return { art: 'laeuft', e: lauf, f: lernRkFlugVon(d.kind.id, lauf.thema_id) || null };
  const fl = (karte?.kontinente || []).flatMap((k) => (k.fluege || []).map((f) => ({ ...f, kontinent_id: k.id })));
  const eVon = (f) => mit.find((e) => e.thema_id && Number(e.thema_id) === Number(f.thema_id)) || null;
  const nstThema = karte?.naechster_start?.grund === 'nachbessern' ? null : Number(karte?.naechster_start?.thema_id) || null;
  const kand = fl.map((f, i) => ({ f, i })).filter(({ f }) => !f.gesperrt && !f.zusatz && !f.stempel && !f.golden && (f.stufe === 'dran' || f.im_plan) && eVon(f))
    .sort((a, b) => (a.f.stufe === 'dran' ? 0 : 1) - (b.f.stufe === 'dran' ? 0 : 1) || (Number(a.f.plan_platz) || 999) - (Number(b.f.plan_platz) || 999)
      || (Number(a.f.thema_id) === nstThema ? 0 : 1) - (Number(b.f.thema_id) === nstThema ? 0 : 1) || a.i - b.i).map((x) => x.f); // gleicher Plan-Platz: zuerst der Flug, den der Server nennt
  for (const f of kand) {
    const e = eVon(f); const ps = (f.staedte || []).filter((c) => c.pflicht !== false).sort((a, b) => Number(a.nr) - Number(b.nr));
    const c = ps.find((x) => !lernStadtGelandet(x));
    if (c) return { art: f.stufe === 'dran' ? 'etappe' : 'flug', e, f, nr: Number(c.nr), stadt: c };
    if (ps.length && !e.ohneTest) return { art: 'test', e, f, n: ps.length };
  }
  return null;
}
// Schritt auf die Daten der Reise legen: n = Einheit des Schritts, et = Etappen-Stand (beim Test: alles gelandet)
function lernSchrittSetzen(d, karte, merk) {
  const s = lernSchritt(d, karte); d.schritt = s; if (!s) return null;
  const n = s.e; n.testJetzt = s.art === 'test'; if (s.nr) n.etappeNr = s.nr;
  if (s.f?.land) n.land = s.f.land;
  if (s.stadt?.name) n.stadt = s.stadt.name; else if (s.art === 'test' && s.f?.land) n.stadt = s.f.land;
  const m = (merk || []).find((x) => Number(x.einheit_id) === Number(n.id));
  const et = s.art === 'test' ? { n: s.n, f: s.n } : m ? lernEtappenZahl(m) : { n: n.n || 0, f: Math.min(n.fertig || 0, n.n || 0) };
  return { n, et };
}
// Test als nächster Schritt? (Schritt bekannt → der zählt; sonst wie bisher aus dem Merkheft)
const lernTestDran = (n, et) => (n.testJetzt !== undefined ? n.testJetzt && !n.laeuft : !n.laeuft && !n.ohneTest && et.n > 0 && et.f >= et.n);
// Ziel und Text des nächsten Schritts (für alle Knöpfe gleich): Nachbessern zuerst, dann wie der Startknopf der Reise
function lernSchrittZiel(d, karte, merk, ws) {
  const nb = (d.nachbessern || [])[0];
  if (nb) return { art: 'nb', ziel: lernNbZiel(d.kind.id, nb), text: 'Jetzt nachbessern', klein: nb.etappe || nb.titel || null };
  const g = lernSchrittSetzen(d, karte, merk);
  const n = g?.n || d.naechste; if (!n) return { art: 'nichts', ziel: `#/reise/${d.kind.id}`, text: 'Zur Reisekarte', klein: 'Gerade ist nichts offen' };
  const et = g?.et || lernEtappenZahl((merk || []).find((m) => Number(m.einheit_id) === Number(n.id))) || { n: 0, f: 0 };
  const st = lernRkStart(d, { n, et, nWdh: ws?.pflicht || 0, ws, wdhFertig: !!ws?.gemacht });
  return { art: d.schritt?.art || 'alt', ziel: st.ziel, text: st.text, klein: st.ansage || null };
}
// Frisch vom Server (nach einem Abschluss): Übersicht, Konto, Karte, Merkheft, Wiederholungen – alles gleichzeitig
async function lernSchrittLaden(kindId) {
  const k = Number(kindId); if (!k) return null;
  const [d, karte, merk, wdh] = await Promise.all([lernLadeKind(k, { still: true }).catch(() => null), lernReiseKarte(k).catch(() => null),
    lernCall('schule_merkheft', { lernender_id: k }).then((r) => r?.einheiten || []).catch(() => []), lernWdhLaden(k).catch(() => null)]);
  if (!d) return null;
  d.merk = merk; lernNamenSetzen(d);
  return lernSchrittZiel(d, karte, merk, lernWdhStand(wdh, k));
}
// Großer Knopf „nächster Schritt“: steht sofort da, aber gesperrt und ohne Stadtname (WT 0.93.5), bis Ziel und Text aus dem frischen Stand feststehen.
// Vorher war er gleich mit dem Ziel des Servers (vorher) antippbar – ein Tippen in den ersten Millisekunden konnte am Schritt vorbeiführen.
// Kommt kein brauchbarer Schritt (Fehler, ohne Stände der Karte, ausgeschlossen über ohne), gilt das Ziel vom Server bzw. „Weiter“ zur Reise.
function lernSchrittKnopf(kindId, { gross = true, klasse = '', ohne = null, vorher = null } = {}) {
  const v = vorher || { text: 'Weiter', klein: null, ziel: `#/reise/${kindId}` };
  const a = gross ? lernGrossKnopf('Weiter', null, { href: v.ziel, class: 'lr-schritt-knopf lr-schritt-wartet ' + klasse }) // als Link anlegen; href kommt erst mit dem Ziel
    : el('a', { class: 'lr-knopf lr-schritt-knopf lr-schritt-wartet ' + klasse }, 'Weiter ›');
  a.setAttribute('aria-busy', 'true'); a.setAttribute('aria-disabled', 'true'); a.removeAttribute('href');
  const sperre = (ev) => { if (a.classList.contains('lr-schritt-wartet')) { ev.preventDefault(); ev.stopImmediatePropagation(); } };
  a.addEventListener('click', sperre, true);
  const setze = (z) => {
    a.setAttribute('href', z.ziel); if (z.art) a.dataset.schritt = z.art;
    if (gross) { a.querySelector('.lr-ab-gross-text').textContent = z.text; const k0 = a.querySelector('small'); if (z.klein) { if (k0) k0.textContent = z.klein; else a.querySelector('.lr-ab-gross-text').after(el('small', {}, z.klein)); } else k0?.remove(); }
    else a.textContent = z.text + ' ›';
    a.classList.remove('lr-schritt-wartet'); a.removeAttribute('aria-busy'); a.removeAttribute('aria-disabled');
  };
  lernSchrittLaden(kindId).then((s) => {
    if (!s || (ohne && ohne(s))) return setze(v);
    if (vorher && ['alt', 'nichts'].includes(s.art)) return setze(v); // ohne Stände der Karte: das Ziel vom Server (vorher) ist besser als der alte Rückfall
    setze(s);
  }).catch(() => setze(v));
  return a;
}
// Lehrer/Eltern (WK F3, Ergänzung): Name eines Flugs wie auf der Reisekarte des Kindes – Land, bei einer Etappe „Land · Stadt“;
// alt (alter Ortsname) nur, wenn die Karte keinen Namen liefert. Einheit → Thema aus schule_uebersicht (gemerkt).
const lernEinheitThema = new Map();
const lernEinheitThemenMerken = (u) => { for (const e of u?.einheiten || []) if (e.thema_id) lernEinheitThema.set(Number(e.id), Number(e.thema_id)); return u; };
function lernFlugName(kindId, { thema_id = null, einheit_id = null, lernziel = null } = {}, alt = '') {
  const th = thema_id || lernEinheitThema.get(Number(einheit_id)) || null; const f = lernRkFlugVon(kindId, th); if (!f?.land) return alt;
  const c = lernziel ? (f.staedte || []).find((x) => x.lernziel === lernziel) : null;
  return c?.name ? `${f.land} · ${c.name}` : f.land;
}
// Stadt einer einzelnen Bordkarte (Check-in, Mischkarte, Knobeln): Stadt der Reisekarte zum Lernziel, sonst der alte Name vom Server
const lernStadtName = (kindId, x) => { if (!x) return ''; const f = lernRkFlugVon(kindId, x.thema_id || lernEinheitThema.get(Number(x.einheit_id)));
  const c = f && x.lernziel ? (f.staedte || []).find((s) => s.lernziel === x.lernziel) : null; return c?.name || x.stadt || ''; };
const lernFlugOrtD = (d, e) => lernFlugOrt(d.kind.id, e, (d.merk || []).find((m) => Number(m.einheit_id) === Number(e?.id)) || null);
const lernUebenZiel = (kindId, e, o = null) => { const nr = o ? o.nr : e?.etappeNr; return `#/lerneinheit/${kindId}-${e.id}-ueben${nr ? '-' + nr + '-start' : ''}`; }; // „-start“: neue Etappe beginnt mit ihrer Erklärung
// Name einer Etappe (Nr. 1 …) bzw. des Flugs für Kinder: Stadt der Karte, sonst der alte Ortsname
const lernEtappenStadt = (kindId, themaId, nr, alt = '') => { const f = lernRkFlugVon(kindId, themaId); return (f?.staedte || []).find((x) => Number(x.nr) === Number(nr))?.name || alt; };

// WT (0.93.5): Antworten älterer Abrufe verwerfen. Jeder Abruf bekommt eine laufende Nummer je Kind; eine Antwort ersetzt die gemerkte Karte nur,
// wenn seit ihrem Abruf nichts vergessen wurde (Landung, Plan …) und keine neuere Antwort schon da ist. Sonst konnte eine langsame alte Antwort
// nach der neuen ankommen und Namen und Stände (lernRkFlugVon) auf den alten Stand zurücksetzen.
const lernReiseKarteNr = new Map(); // Kind → { abruf, gemerkt, stand }
const lernRkNr = (k) => { if (!lernReiseKarteNr.has(k)) lernReiseKarteNr.set(k, { abruf: 0, gemerkt: 0, stand: 0 }); return lernReiseKarteNr.get(k); };
function lernReiseKarte(kindId) {
  if (!lernReiseKarteSpeicher.has(kindId)) {
    const t0 = performance.now(); const z = lernRkNr(kindId); const nr = ++z.abruf, stand = z.stand;
    const p = lernCallNetz('schule_reise_karte', { lernender_id: kindId }).then((r) => {
      if (r) { r._ladezeit = Math.round(performance.now() - t0); if (stand === z.stand && nr > z.gemerkt) { z.gemerkt = nr; lernReiseKarteAlt.set(kindId, r); } }
      return r; })
      .catch((e) => { if (lernReiseKarteSpeicher.get(kindId) === p) lernReiseKarteSpeicher.delete(kindId); throw e; });
    lernReiseKarteSpeicher.set(kindId, p);
  }
  return lernReiseKarteSpeicher.get(kindId);
}
const lernReiseKarteVergessen = (kindId) => { if (kindId === undefined || kindId === null) { lernReiseKarteSpeicher.clear(); lernReiseKarteNr.forEach((z) => { z.stand++; }); } else { lernReiseKarteSpeicher.delete(Number(kindId)); lernRkNr(Number(kindId)).stand++; } };
function lernExFehlt(s, karte) {
  if (!karte) return null;
  const fluege = (karte.kontinente || []).flatMap((k) => k.fluege || []);
  return s.vor.map((v) => {
    const fl = fluege.filter((f) => Number(f.thema_id) === v.thema || Number(f.teil_stamm) === v.thema);
    const hit = fl.map((f) => ({ f, st: (f.staedte || []).find((c) => c.lernziel === v.lernziel) })).find((q) => q.st);
    const ok = hit && ['gelandet', 'sicher'].includes(hit.st.stand);
    return { ...v, ok: !!ok, flug: hit?.f?.titel || v.flug, im_plan: hit ? !!hit.f.im_plan : null };
  });
}
async function viewStationen(arg) {
  setChrome('Expeditionen', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const { kind } = d;
  const karte = await lernReiseKarte(kind.id).catch(() => null);
  if (!live()) return;
  const gesamt = lernExGesamt(d); const k = lernExGeschafftZahl(d);
  const zuX = new Map((d.expeditionen || []).map((x) => [x.schluessel, x]));
  const frei = (d.expeditionen || []).filter(lernExOffen).length;
  const stationen = LERN_EX_STATIONEN.slice();
  for (const x of d.expeditionen || []) if (!lernExStation(x)) stationen.push({ schluessel: x.schluessel, nr: stationen.length + 1, station: x.titel, kurz: x.titel, titel: x.titel, klasse: Number(Object.values(x.klasse || {})[0]) || null, vor: [] });
  const blatt = el('dialog', { class: 'lr-blatt lr-ex-blatt-info', 'aria-label': 'Station' });
  blatt.addEventListener('click', (ev) => { if (ev.target === blatt) blatt.close(); });
  const zeigeBlatt = (...inhalt) => { lernErsetze(blatt, el('div', { class: 'lr-ex-info' }, ...inhalt, el('button', { type: 'button', class: 'lr-blatt-zu', onclick: () => blatt.close() }, 'Schließen'))); blatt.showModal(); };
  const tippen = (s, x) => {
    if (lernExOffen(x)) { lernExFreiZeigen(d, x, { bewegt: false, spaeterRufen: !x.ausgeblendet, weiter: () => render() }); return; }
    if (x?.zustand === 'geschafft') {
      zeigeBlatt(el('p', { class: 'lr-ueber' }, `STATION ${s.nr} VON ${gesamt} · GESCHAFFT`), el('h2', {}, `${s.station}: ${x.titel}`),
        el('div', { class: 'lr-ex-info-stempel' }, lernExStempel(s, { gross: true, ff: x.fehlerfrei === true })),
        el('p', {}, 'Geschafft', x.fehlerfrei ? ' · fehlerfrei' : '', x.sterne ? ` · ★ ${lernZahl(x.sterne)}` : ''),
        el('a', { class: 'lr-textlink', href: `#/expedition/${kind.id}-${x.id}` }, 'Expedition ansehen'));
      return;
    }
    const abKlasse = s.klasse && kind.klasse && s.klasse > kind.klasse;
    const f = abKlasse ? null : lernExFehlt(s, karte);
    const fehlen = f ? f.filter((v) => !v.ok) : null;
    const g = Number(d.regeln?.sterne_expedition_geschafft ?? 150), ff = Number(d.regeln?.sterne_expedition_fehlerfrei ?? 200);
    zeigeBlatt(el('p', { class: 'lr-ueber' }, `STATION ${s.nr} VON ${gesamt} · GESPERRT`), el('h2', {}, `${s.station}: ${s.titel}`),
      abKlasse ? el('p', {}, `Ab Klasse ${s.klasse}`)
        : el('div', {}, fehlen ? el('p', {}, fehlen.length ? `Noch ${fehlen.length} ${fehlen.length === 1 ? 'Etappe' : 'Etappen'}, dann ist sie frei:` : 'Gleich frei – alle Etappen sind gelandet.')
          : el('p', {}, 'Sie ist frei, sobald diese Etappen gelandet sind:'),
        el('ul', { class: 'lr-ex-vor' }, ...(f || s.vor).map((v) => el('li', { class: f ? (v.ok ? 'ok' : 'fehlt') : '' },
          el('span', { class: 'lr-ex-vor-z', 'aria-hidden': 'true' }, f ? (v.ok ? '✓' : '○') : '•'), f && !v.ok ? el('b', {}, v.etappe) : el('span', {}, v.etappe), f && !v.ok ? el('span', { class: 'lr-leise' }, ` · ${v.flug}`) : null))),
        fehlen?.length ? el('p', { class: 'lr-leise' }, fehlen.every((v) => v.im_plan !== false) ? 'Die Etappen kommen in deinem Plan.' : 'Diese Etappen sind noch nicht in deinem Plan.') : null),
      el('p', { class: 'lr-leise' }, `★ ${lernZahl(g)} · ★ ${lernZahl(ff)} ohne Fehler`));
  };
  const platz = (s) => {
    const x = zuX.get(s.schluessel); const z = x?.zustand || 'gesperrt';
    const kz = x ? lernExTeilK(x) : 0; const n = lernExTeile(x);
    const inhalt = z === 'geschafft' ? lernExStempel(s, { klein: true, ff: x.fehlerfrei === true })
      : z === 'begonnen' ? el('span', { class: 'lr-ex-luecke frei' }, el('b', {}, String(s.nr)), el('small', {}, `Teil ${kz + 1}/${n}`))
      : z === 'angeboten' ? el('span', { class: 'lr-ex-luecke frei puls' }, el('b', {}, String(s.nr)), el('small', {}, 'frei'))
      : el('span', { class: 'lr-ex-luecke' }, el('b', {}, String(s.nr)), el('small', { 'aria-hidden': 'true' }, '🔒'));
    const wort = { geschafft: 'geschafft' + (x?.fehlerfrei ? ', fehlerfrei' : ''), begonnen: `begonnen, Teil ${kz + 1} von ${n}`, angeboten: 'freigeschaltet', gesperrt: 'gesperrt' }[z];
    return el('button', { type: 'button', class: 'lr-ex-platz lr-ex-' + z, 'aria-label': `Station ${s.nr}, ${s.kurz}: ${wort}`, onclick: () => tippen(s, x) }, inhalt, el('span', { class: 'lr-ex-name' }, s.kurz));
  };
  const klassen = [...new Set(stationen.map((s) => s.klasse))].sort((a, b) => (a ?? 99) - (b ?? 99));
  lernErsetze(main, lernRahmen(kind, 'reisepass',
    el('header', { class: 'lr-kopf lr-ex-samml-kopf' }, el('p', { class: 'lr-ueber' }, 'REISEPASS · EXPEDITIONEN'), el('h1', { class: 'lr-titel' }, 'Antarktis'),
      el('p', { class: 'lr-ex-samml-zahl' }, el('b', {}, `${k} von ${gesamt} Stationen`), frei ? ` · ${frei} freigeschaltet` : ''),
      el('div', { class: 'lr-ex-balken', role: 'img', 'aria-label': `${k} von ${gesamt} Stationen` }, el('span', { style: `width:${Math.round(100 * k / Math.max(1, gesamt))}%` }))),
    ...klassen.map((kl) => { const ss = stationen.filter((s) => s.klasse === kl);
      return el('section', { class: 'lr-ex-gruppe' }, el('h2', { class: 'lr-ex-gruppe-kopf' }, kl ? `KLASSE ${kl} · ${ss.length} STATIONEN` : `${ss.length} STATIONEN`), el('div', { class: 'lr-ex-raster' }, ...ss.map(platz))); }),
    karte?.quellen?.length ? el('p', { class: 'lr-leise lr-ex-quelle' }, 'Stationen: COMNAP Antarctic Facilities (für Bildung, nicht kommerziell).') : null,
    el('a', { class: 'lr-textlink', href: `#/reisepass/${kind.id}` }, 'Zurück zum Reisepass'), blatt));
}
// Betrieb 18.11.: Wird eine Bordkarte gesperrt, während das Kind sie offen hat (neue Fassung eingespielt), antwortet der Server (alte Fassung) mit „nicht freigegeben“.
// Dann keine rote Meldung: die Seite lädt still neu und zeigt die nächste Bordkarte; gewertet wurde nichts, die Checkliste bleibt, wie sie war.
const lernGesperrt = (err) => /nicht freigegeben/i.test(String(err?.message || ''));
// Bauplan einer Bordkarte: Fragetext ohne Zahlen (gleiche Regel wie tools/inhalt_pruefen.py)
const lernBauplan = (a) => String(a?.frage?.text || '').replace(/[−-]?\d+(?:[ \u202f]\d{3})*(?:[,.]\d+)?/g, '#').replace(/\s+/g, ' ').trim();
// Zählt für „eine schwere Bordkarte im ersten Versuch“: Stufe 3 – und wenn ein Typ da ist, ein Stufe-3-Typ
const lernIstSchwer = (a) => a.stufe === 3 && (!a.typ || LERN_TYP[a.typ]?.[0] === 3) && a.typ !== 'knobel';

const LERN_SYS = [
  { sa: 'gym_by', kurz: 'GYM', name: 'Gymnasium', stufen: [5, 6, 7, 8, 9, 10], label: (n) => 'Klasse ' + n, kl: (n) => n, farbe: '#2F6FDE' },
  { sa: 'rs_by', kurz: 'RS', name: 'Realschule', stufen: [5, 6, 7, 8, 9, 10], label: (n) => 'Klasse ' + n, kl: (n) => n, farbe: '#D9482A' },
  { sa: 'ib_myp', kurz: 'IB', name: 'IB MYP', stufen: [1, 2, 3, 4, 5], label: (n) => (n >= 1 ? 'MYP-Jahr ' + n : 'noch kein MYP-Jahr'), kl: (n) => n + 5, farbe: '#0F8C68' }];
// IB einheitlich: MYP-Jahr n ≈ Klasse n + 5, also MYP-Jahr = Klasse − 5 (MYP-Jahr 1–5 entspricht etwa Klasse 6–10)
const LERN_IB_HINWEIS = 'MYP-Jahr 1–5 entspricht etwa Klasse 6–10';
const LERN_KONT_REIHE = ['Zahlen', 'Geld und Verhältnisse', 'Algebra', 'Funktionen', 'Geometrie', 'Fläche und Raum', 'Daten und Zufall', 'Entdecker-Inseln'];
function lernStufe(k, sa) {
  if (!k?.klasse) return null;
  const s = Number(k.stufen?.[sa]); if (s >= 1) return s;
  const eigen = k.schulart || 'gym_by';
  if (sa !== eigen && sa === 'ib_myp') return k.klasse ? Math.max(0, k.klasse - 5) : null; // 0 = vor MYP-Jahr 1
  const v = k.klasse;
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
  const kannT = new Map(normal.map((r) => [r.block_id, r.kann_schon_themen || []])); // LA-4: „kann schon“ je Flug – zählt wie gelandet, eigener Zustand
  const jetzt = lernReiseDaten(u, k.id)?.naechste;
  const zustand = (t) => {
    const s = t.einheit ? stand.get(t.einheit.id) : null; const n = Number(t.einheit?.pflicht_anzahl || 0); const f = Number(s?.fertig || 0);
    if ((n > 0 && f >= n) || (ortFertig.has(t.block_id) && !aus.get(t.block_id)?.includes(t.thema_id))) return 'ok';
    if (Number(s?.fehler || 0) > 0 || rueck.has(t.block_id)) return 'wackelt';
    if (jetzt && t.einheit && jetzt.id === t.einheit.id) return 'jetzt';
    if (f > 0) return 'laeuft';
    return 'offen';
  };
  for (const t of themen) { t.kannSchon = !!kannT.get(t.block_id)?.includes(t.thema_id); t.st = t.kannSchon ? 'ok' : zustand(t); t.ausgelassen = !!aus.get(t.block_id)?.includes(t.thema_id); }
  const zahl = (sa, kl) => { const ts = kl ? themen.filter((t) => Number(t.jahrgang?.[sa]) === kl) : []; return { f: ts.filter((t) => t.st === 'ok').length, n: ts.length, ts }; };
  return { kind: k, themen, zahl, alleFluege: !!alle, stufe: (sa) => lernStufe(k, sa) };
}
// Rückwärts verträglich für die Startseite (E-2): drei Zeilen GYM · RS · IB
function lernStandSchularten(u, k) {
  if (!k?.klasse) return [];
  const m = lernStandModell(u, k); const eigen = k.schulart || 'gym_by';
  return LERN_SYS.map((y) => { const kl = m.stufe(y.sa); const c = m.zahl(y.sa, kl);
    const ib = y.sa === 'ib_myp' && kl !== null; // IB: „MYP-Jahr n“ bzw. „vor MYP-Jahr 1“ statt einer Klasse
    return { sa: y.sa, kurz: ib ? 'IB' : y.kurz, name: y.name, klasse: ib ? y.label(kl) : kl || '–', stufeText: ib ? 'IB ' + y.label(kl) : `${y.name} Klasse ${kl || '–'}`, n: c.n, gelandet: c.f, eigen: y.sa === eigen }; });
}
// M5: Zahl der gelandeten Flüge eines Ortes (für den Stempel)
const ortFluegeGelandet = (d, blockId) => d.mit.filter((e) => e.block_id === blockId && lernGelandet(e)).length;
const lernPz = (a, b) => (b ? Math.round(100 * a / b) : 0);
const lernSysVoll = (y, n) => (y.sa === 'ib_myp' ? 'IB ' + y.label(n) : `${y.name} ${y.label(n)}`);
const lernSysStufe = (y, n) => (y.sa === 'ib_myp' ? y.label(n) : `${y.kurz} ${n}`);
// K3: drei Mini-Linien (Abflugtafel und Mein Weg · Stand). href(y, stufe) → Ziel beim Antippen.
function lernMiniLinien(m, href) {
  return el('div', { class: 'lr-mini3', role: 'list', 'aria-label': 'Mein Stand in drei Schularten' }, ...LERN_SYS.map((y) => {
    const kl = m.stufe(y.sa); const c = m.zahl(y.sa, kl);
    return el('a', { class: 'lr-mini', role: 'listitem', href: href(y, kl || null), style: `--f:${y.farbe}`, 'aria-label': `${kl || (kl === 0 && y.sa === 'ib_myp') ? lernSysVoll(y, kl) : y.name}: ${c.f} von ${c.n} Flügen gelandet` },
      el('b', {}, kl || (kl === 0 && y.sa === 'ib_myp') ? lernSysStufe(y, kl) : y.kurz + ' –'),
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
    mk('text', { x: rechts ? 356 : 4, y: Y[y.sa] - 28, 'text-anchor': rechts ? 'end' : 'start', class: 'lr-lp-name', fill: y.farbe }, y.name.toUpperCase() + (y.sa === 'ib_myp' ? ' · ≈ KLASSE 6–10' : ''));
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
      if (y.sa === 'ib_myp') { mk('text', { x: cx, y: cy + 31, 'text-anchor': 'middle', class: 'lr-lp-kl klein' }, 'MYP-Jahr', a); mk('text', { x: cx, y: cy + 42, 'text-anchor': 'middle', class: 'lr-lp-kl' }, String(n), a); }
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
  lernEinheitThemenMerken(u);
  // WK F3: Namen der Reisekarte je Kind (gleichzeitig, Fehler egal – dann bleibt der alte Ortsname)
  await Promise.all((u.lernende || []).filter((k) => !lernReiseKarteAlt.has(k.id)).map((k) => lernReiseKarte(k.id).catch(() => null)));
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
      el('p', { class: 'small muted' }, n ? `Jetzt: ${lernFlugName(k.id, n, n.stadt || n.ort_titel)} · ${n.titel} (${n.fertig}/${n.n})` : 'Gerade nichts offen'),
      ko ? el('p', { class: 'small muted' }, `${ko.stempel} Stempel · ${lernZahl(ko.sterne)} Sterne · ${ko.lerntage} Lerntage`) : null,
      el('span', { class: 'lern-kindkarte-los' }, 'Lernreise öffnen ›'));
  });
  const offen = (rm?.rueckmeldungen || []).filter((r) => ['offen', 'in_arbeit'].includes(r.status)).length;
  const testkinder = (u.lernende || []).filter((k) => k.ist_test);
  // Reihenfolge nach Dringlichkeit: erst, was auf eine Antwort wartet, dann die Kinder, dann Verwalten.
  const offeneWuensche = (eltern?.einloesungen || []).filter((x) => x.status === 'beantragt');
  const meldung = el('p', { class: 'small muted', role: 'status' });
  const entscheide = async (id, status) => { try { await lernCall('schule_einloesung_entscheiden', { id, status }); render(); } catch (err) { meldung.textContent = err.message; } };
  // I-2: auf der Leitungs-Startseite stehen die Wünsche als blaue Einträge in „Zu tun“; der Kasten bleibt nur für die Seite ohne Leitung
  const wuensche = offeneWuensche.map((x) => ({ text: `${x.kind} möchte „${x.titel}“ einlösen (${lernZahl(x.sterne)} Sterne)`,
    knoepfe: [el('button', { type: 'button', class: 'primary', onclick: () => entscheide(x.id, 'bestaetigt') }, 'Bestätigen'),
      el('button', { type: 'button', class: 'secondary', onclick: () => entscheide(x.id, 'abgelehnt') }, 'Ablehnen')] }));
  const wartet = offeneWuensche.length ? el('section', { class: 'card lern-wartet' }, el('p', { class: 'eyebrow' }, 'WARTET AUF DICH'),
    ...offeneWuensche.map((x) => el('div', { class: 'lern-wunsch' }, el('span', {}, el('b', {}, x.kind), ` möchte „${x.titel}“ einlösen (${lernZahl(x.sterne)} Sterne)`),
      el('div', { class: 'row' }, el('button', { type: 'button', class: 'primary', onclick: () => entscheide(x.id, 'bestaetigt') }, 'Bestätigen'),
        el('button', { type: 'button', class: 'secondary', onclick: () => entscheide(x.id, 'abgelehnt') }, 'Ablehnen')))), meldung) : null;
  const weitere = seite ? null : el('details', { class: 'card lern-weitere' }, el('summary', {}, 'Weitere Lernhilfen'),
    el('p', {}, 'Mathe-Lernblatt: Erklärungen, Übungen in drei Stufen und typische Fehler. Die Seite öffnet ohne Anmeldung.'),
    el('div', { class: 'row' }, el('a', { class: 'btn secondary', href: 'mathe/', target: '_blank', rel: 'noopener' }, 'Mathe-Lernblatt öffnen ↗'), kopie, status),
    el('p', { class: 'muted small learn-url' }, url));
  if (!u.leitung) {
    lernErsetze(main, ...[wartet,
      el('section', { class: 'start-intro lern-neu' }, el('p', { class: 'eyebrow' }, 'LERNREISE'), el('h2', {}, 'Wer lernt heute?')),
      el('div', { class: 'lern-kinderliste' }, ...(kinder.length ? kinder : [el('p', { class: 'card muted' }, 'Kein Kind freigeschaltet.')])),
      eltern ? lernElternBereich(eltern, { ohneWuensche: true }) : null, weitere].filter(Boolean));
    return;
  }
  // LA-1/LA-2: Startseite „Was ist los?“ – Zu tun · Kinder-Tabelle · Nachschlagen
  const echte = (u.lernende || []).filter((k) => !k.ist_test);
  const lsAlle = await Promise.all(echte.map((k) => lernCall('schule_lernstand', { lernender_id: k.id }).catch(() => null)));
  if (!live()) return;
  const lagen = new Map(echte.map((k, i) => [k.id, lernKindLage(u, k, lsAlle[i])]));
  const nachschlagen = el('nav', { class: 'lern-nachschlagen', 'aria-label': 'Nachschlagen' }, el('span', { class: 'eyebrow' }, 'NACHSCHLAGEN'),
    el('a', { href: '#/lehrplan' }, 'Lehrplan'), el('a', { href: '#/expeditionen' }, 'Expeditionen'),
    el('a', { href: '#/lernauftraege' }, 'Meine Aufträge' + (offen ? ` (${offen} offen)` : '')), el('a', { href: '#/info' }, 'So funktioniert’s'));
  const verwalten = [...testkinder.map((k) => el('a', { href: `#/reise/${k.id}` }, `${k.name} (zum Ausprobieren)`)),
    eltern ? el('a', { href: '#/zugaenge' }, 'Zugänge') : null,
    !seite ? el('a', { href: 'lernen/', target: '_blank', rel: 'noopener' }, 'Eigene Lernen-Seite ↗') : null].filter(Boolean);
  lernErsetze(main, ...[
    // I-2: Kopf in einer Zeile (Überschrift links, „So funktioniert’s“ rechts) – damit die Kinder-Tabelle auch auf dem Rechner ohne Rollen sichtbar ist
    el('section', { class: 'lern-neu lern-was-ist-los' }, el('h1', { class: 'lern-h-start' }, 'Was ist los?'), lernInfoLink()),
    lernZuTun(echte, lagen, rm, wuensche, meldung),
    echte.length ? lernKinderTabelle(u, echte, lagen) : el('p', { class: 'card muted' }, 'Kein Kind freigeschaltet.'),
    nachschlagen,
    verwalten.length ? el('nav', { class: 'lern-nachschlagen lern-verwalten', 'aria-label': 'Verwalten' }, el('span', { class: 'eyebrow' }, 'VERWALTEN'), ...verwalten) : null,
    eltern ? lernElternBereich(eltern, { ohneWuensche: true }) : null,
    weitere].filter(Boolean));
}

// ---------- Bau-Auftrag LA (18.11.): Lehrer-Aufbau ----------
// Rolle der Anmeldung: Lern-Seite kennt sie (schule_ich); die ganze App ist Eltern-Zugang des Nutzers.
// „Lernen starten“ bleibt für Eltern (die Kinder kommen über den Eltern-Zugang auf ihre Abflugtafel), entfällt für Lehrer.
const lernRolle = () => (typeof lernIch !== 'undefined' && lernIch?.rolle) || 'eltern';
const lernTag = (t) => new Date(t).toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' });
const lernTageSeit = (datum) => { if (!datum) return null; const h = new Date(); h.setHours(0, 0, 0, 0); const d = new Date(String(datum).slice(0, 10) + 'T00:00:00'); return Math.round((h - d) / 864e5); };
// „wackelt“ (wie bisher auf „Was wackelt?“): mindestens 3 falsche, mehr falsche als richtige – oder wieder geöffnet (H1)
const lernKarteWackelt = (k) => !k.sitzt && (!!k.wieder_offen || (k.falsch >= 3 && k.falsch > k.richtig));
// Lage eines Kindes aus schule_lernstand (Lerntage, Woche, Etappen) und schule_uebersicht (Rückreise)
function lernKindLage(u, k, ls) {
  const tage = [...(ls?.lerntage || [])].sort().reverse(); const zuletzt = tage[0] || null; const seit = lernTageSeit(zuletzt);
  const woche = tage.filter((d) => lernTageSeit(d) < 7).length;
  const karten = (ls?.einheiten || []).flatMap((e) => (e.karten || []).map((x) => ({ ...x, einheit_id: e.einheit_id, ort: lernFlugName(k.id, { einheit_id: e.einheit_id, lernziel: x.lernziel }, e.ort), thema: e.titel })));
  const wackelt = karten.filter(lernKarteWackelt);
  const ortName = new Map((u.orte || []).map((o) => [o.block_id, o.stadt || o.titel]));
  const rueck = (k.route || []).filter((r) => r.art === 'rueckreise' && !['fertig', 'entfernt'].includes(r.status)).map((r) => ortName.get(r.block_id) || 'ein Ort');
  // I-10: eingetragene Reisetage/Pausen zählen nicht für „Lernt“ (rot/gelb) und „kein Lerntag seit …“
  const pausen = ls?.pausen || []; const p = lernPauseLage(pausen, zuletzt);
  return { zuletzt, seit, seitEff: p.seitEff, pause: p.heute, woche, karten, wackelt, offen: wackelt.filter((x) => !x.besprochen_am), rueck, w: ls?.woche || {}, ls, pausen };
}
// I-10: Tage als JJJJ-MM-TT im Ortskalender; Pause heute und „Tage seit dem letzten Lerntag ohne eingetragene Pausen“
const lernIso = (d) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
function lernPauseLage(pausen, zuletzt) {
  const heute = new Date(); heute.setHours(0, 0, 0, 0); const iso = lernIso(heute);
  const inPause = (tag) => pausen.some((p) => String(p.von).slice(0, 10) <= tag && tag <= String(p.bis).slice(0, 10));
  const aktuell = pausen.filter((p) => String(p.von).slice(0, 10) <= iso && iso <= String(p.bis).slice(0, 10)).sort((a, b) => String(b.bis).localeCompare(String(a.bis)))[0] || null;
  // Tage seit dem letzten Lerntag (ohne ihn) bis heute, ohne Pausentage; ohne Lerntag: die letzten 28 Tage
  const start = zuletzt ? new Date(String(zuletzt).slice(0, 10) + 'T00:00:00') : new Date(heute.getTime() - 28 * 864e5);
  let n = 0; for (const d = new Date(start.getTime() + 864e5); d <= heute; d.setDate(d.getDate() + 1)) if (!inPause(lernIso(d))) n++;
  if (!zuletzt && n >= 3) n = null; // „kein Lerntag in 4 Wochen“ bleibt, außer die Pausen decken fast alles ab
  return { heute: aktuell, seitEff: n };
}
const lernSeitOhnePause = (l) => (l.seitEff === undefined ? l.seit : l.seitEff);
const lernLerntAmpel = (l) => { if (l.pause) return 'pause'; const s = lernSeitOhnePause(l); return s === null || s >= 3 ? 'rot' : s === 2 ? 'gelb' : 'gruen'; };
const lernLerntText = (l) => l.pause ? `Pause bis ${lernTag(String(l.pause.bis).slice(0, 10) + 'T00:00:00')}${l.pause.grund ? ` (${l.pause.grund})` : ''}`
  : l.seit === null ? 'kein Lerntag in 4 Wochen' : `${l.woche} ${l.woche === 1 ? 'Lerntag' : 'Lerntage'} diese Woche · zuletzt ${l.seit === 0 ? 'heute' : l.seit === 1 ? 'gestern' : lernTag(l.zuletzt)}`;
// Stand je Schulart als Prozent (Rechenregel K3: gelandete Flüge der Stufe / alle Flüge der Stufe). IB unter Klasse 6: „noch kein MYP-Jahr“.
function lernStandZellen(u, k) {
  if (!k?.klasse) return LERN_SYS.map((y) => ({ y, text: '–', pz: null, sa: y.sa }));
  const m = lernStandModell(u, k);
  return LERN_SYS.map((y) => { const kl = m.stufe(y.sa); const c = m.zahl(y.sa, kl);
    if (y.sa === 'ib_myp' && !kl) return { y, sa: y.sa, text: '– (ab Kl. 6)', lang: 'noch kein MYP-Jahr', pz: null }; // I-8: kurz in Tabelle und Karten
    return { y, sa: y.sa, text: y.sa === 'ib_myp' ? y.label(kl) : 'Kl. ' + kl, pz: c.n ? lernPz(c.f, c.n) : null, f: c.f, n: c.n, eigen: y.sa === (k.schulart || 'gym_by') }; });
}
// LA-2 „Zu tun“: rot (seit 3 Tagen kein Lerntag, Rückreise) → gelb (Etappe wackelt, noch nicht besprochen) → blau (neue Antwort auf einen Auftrag)
// I-4: Reisewörter beim ersten Vorkommen klein erklären
const LERN_WORT = { rueckreise: 'Wiederholung nach nicht bestandenem Nachtest', etappe: 'Lernschritt', flug: 'Thema', bordkarte: 'Aufgabe' };
const lernErklaert = (wort, art) => el('span', { class: 'lern-wort' }, wort, el('small', { class: 'lern-wort-erkl' }, ` (${LERN_WORT[art]})`));
function lernZuTun(kinder, lagen, rm, wuensche = [], meldung = null) {
  const eintraege = [];
  for (const k of kinder) { const l = lagen.get(k.id);
    if (lernLerntAmpel(l) === 'rot') eintraege.push(['rot', `${k.name}: ${l.seit === null ? 'kein Lerntag in den letzten 4 Wochen' : `seit ${l.seit} Tagen kein Lerntag`}${l.seit !== null && lernSeitOhnePause(l) !== l.seit ? ` (ohne Pausentage: ${lernSeitOhnePause(l)})` : ''}`, `#/kind/${k.id}-ueberblick`]);
    for (const o of l.rueck) eintraege.push(['rot', [`${k.name}: `, lernErklaert(`Rückreise ${o}`, 'rueckreise')], `#/kind/${k.id}-lehrplan`]); }
  for (const k of kinder) for (const x of lagen.get(k.id).offen) eintraege.push(['gelb', `${k.name}: „${x.titel}“ wackelt (${x.falsch} falsch)`, `#/kind/${k.id}-wackelt-${x.einheit_id}.${x.lernziel}`]);
  const neu = (rm?.rueckmeldungen || []).filter((r) => r.antwort && r.status !== 'offen' && (!r.am || lernTageSeit(r.beantwortet_am || r.am) <= 7));
  for (const w of wuensche) eintraege.push(['blau', w.text, null, w.knoepfe]); // I-2: Belohnung einlösen
  if (neu.length) eintraege.push(['blau', neu.length === 1 ? `Neue Antwort auf euren Auftrag: ${neu[0].flug || neu[0].ort || 'Allgemein'}` : `${neu.length} neue Antworten auf eure Aufträge`, '#/lernauftraege']);
  const kannPause = kinder.some((k) => Array.isArray(lagen.get(k.id)?.ls?.pausen));
  return el('section', { class: 'card lern-zutun', 'aria-label': 'Zu tun' },
    el('div', { class: 'lern-zutun-kopf' }, el('h2', {}, 'Zu tun'),
      kannPause ? el('button', { type: 'button', class: 'lern-einstellen lern-pause-knopf', onclick: () => lernPauseBlatt(kinder) }, '+ Reisetag eintragen') : null),
    eintraege.length ? el('ul', { class: 'lern-zutun-liste' }, ...eintraege.map(([f, t, h, knoepfe]) => el('li', { class: 'zt-' + f + (knoepfe ? ' zt-wunsch' : '') },
      knoepfe ? el('div', { class: 'zt-zeile' }, el('i', { class: 'zt-punkt', 'aria-hidden': 'true' }), el('span', {}, t), el('span', { class: 'zt-knoepfe' }, ...knoepfe))
        : el('a', { href: h }, el('i', { class: 'zt-punkt', 'aria-hidden': 'true' }), el('span', {}, ...[t].flat()), el('span', { class: 'zt-pfeil', 'aria-hidden': 'true' }, '›')))))
      : el('p', { class: 'lern-zutun-ruhig' }, 'Alles ruhig.'), meldung && wuensche.length ? meldung : null);
}
// LA-2 Kinder-Tabelle (ab 560 px) bzw. je Kind eine kompakte Karte (Handy) – dieselben Felder
function lernKinderTabelle(u, kinder, lagen) {
  const eltern = lernRolle() === 'eltern';
  const jetzt = (k) => { const n = lernReiseDaten(u, k.id)?.naechste; return n ? `${lernFlugName(k.id, n, n.stadt || n.ort_titel)} · ${n.titel} (${n.fertig}/${n.n})` : 'gerade nichts offen'; };
  const wack = (l) => [l.wackelt.length ? `${l.wackelt.length} ${l.wackelt.length === 1 ? 'Etappe' : 'Etappen'}` : null, l.rueck.length ? 'Rückreise' : null].filter(Boolean).join(' · ') || '–';
  const wackAmpel = (l) => (l.rueck.length ? 'rot' : l.offen.length ? 'gelb' : 'gruen');
  const klasse = (k) => k.klasse ? `${{ gym_by: 'Gym', rs_by: 'RS', ib_myp: 'IB' }[k.schulart || 'gym_by'] || 'Gym'} Kl. ${k.klasse}` : 'Klasse nicht gesetzt';
  const zelle = (z) => el('span', { class: 'lern-st-zelle' + (z.eigen ? ' eigen' : '') }, el('b', {}, z.text),
    z.lang ? null : z.pz === null ? el('small', {}, '–') : el('small', {}, `${z.pz} %`), z.pz === null ? null : el('i', { class: 'lern-st-balken', style: `--f:${z.y.farbe}` }, el('i', { style: `width:${z.pz}%` })));
  const einstellen = (k) => el('button', { type: 'button', class: 'lern-einstellen', 'aria-label': `${k.name} einstellen`, onclick: (ev) => { ev.preventDefault(); ev.stopPropagation(); lernEinstellenBlatt(k.id); } }, '⚙ Einstellen');
  const starten = (k) => eltern ? el('a', { class: 'btn lern-start', href: `#/reise/${k.id}`, 'aria-label': `Lernen starten: ${k.name}`, onclick: (ev) => ev.stopPropagation() }, 'Lernen starten ›') : null;
  const oeffne = (k) => (ev) => { if (ev.target.closest('a,button')) return; route('kind', `${k.id}-ueberblick`); };
  const tabelle = el('table', { class: 'lern-kinder-tabelle' },
    el('thead', {}, el('tr', {}, el('th', {}, 'Kind'), el('th', {}, 'Lernt'), el('th', {}, 'Wackelt'), ...LERN_SYS.map((y) => el('th', {}, y.kurz)), el('th', {}, 'Jetzt'), el('th', { 'aria-label': 'Lernen starten und Einstellen' }))),
    el('tbody', {}, ...kinder.map((k) => { const l = lagen.get(k.id);
      return el('tr', { class: 'lern-kind-zeile', onclick: oeffne(k) },
        el('th', { scope: 'row' }, el('a', { href: `#/kind/${k.id}-ueberblick` }, el('b', {}, k.name)), el('small', {}, klasse(k))),
        el('td', { class: 'amp-' + lernLerntAmpel(l) }, lernLerntText(l)),
        el('td', { class: 'amp-' + wackAmpel(l) }, wack(l)),
        ...lernStandZellen(u, k).map((z) => el('td', {}, zelle(z))),
        el('td', { class: 'small' }, jetzt(k)),
        el('td', { class: 'lern-zeile-zelle' }, el('div', { class: 'lern-zeile-knoepfe' }, starten(k), einstellen(k)))); })));
  const karten = el('div', { class: 'lern-kinder-karten' }, ...kinder.map((k) => { const l = lagen.get(k.id);
    return el('section', { class: 'card lern-kind-karte', 'aria-label': k.name, onclick: oeffne(k) },
      el('div', { class: 'lern-kind-karte-kopf' }, el('a', { href: `#/kind/${k.id}-ueberblick` }, el('b', {}, k.name)), el('small', {}, klasse(k)), einstellen(k)),
      el('p', { class: 'amp-' + lernLerntAmpel(l) }, el('b', {}, 'Lernt: '), lernLerntText(l)),
      el('p', { class: 'amp-' + wackAmpel(l) }, el('b', {}, 'Wackelt: '), wack(l)),
      el('div', { class: 'lern-kind-karte-stand' }, ...lernStandZellen(u, k).map((z) => el('span', {}, el('small', {}, z.y.kurz), zelle(z)))),
      el('p', { class: 'small' }, el('b', {}, 'Jetzt: '), jetzt(k)), starten(k)); }));
  return el('section', { class: 'lern-kinder', 'aria-label': 'Die Kinder' }, el('h2', {}, 'Die Kinder'), el('div', { class: 'lern-tabelle-rollen lern-kinder-breit' }, tabelle), karten);
}
// LA-1 Kind-Seite #/kind/<id>-<reiter>[-…]: Kopf (Name, Schulart/Klasse, ⚙ Einstellen, Lernreise ansehen) und 4 Reiter
// LW-1: drei Reiter – „Lehrplan“ ersetzt „Stand“ und „Plan“ (alte Adressen -stand/-plan führen dorthin)
const LERN_REITER = [['ueberblick', 'Überblick'], ['wackelt', 'Was wackelt'], ['lehrplan', 'Lehrplan']];
// LW-3 (1a): Kinder-Umschalter im Kopf – Klick auf ein Kind oder ‹ › wechselt das Kind, der gewählte Reiter bleibt; Alt+← / Alt+→
// 0.91.2: Ziel immer aus der Adresse lesen (Kind und Reiter), nie aus dem Kopf, der gerade gezeichnet ist – während eines Wechsels steht noch der
// alte Kopf da; ein zweiter Klick (A → B → A) oder Alt+←/→ muss vom neuen Kind aus rechnen.
const lernKindAktuell = () => { const m = location.hash.match(/^#\/kind\/(\d+)-([a-z]+)/); return m ? { id: Number(m[1]), reiter: m[2] } : null; };
function lernKinderUmschalter(k, reiter, kinder) {
  if (!kinder || kinder.length < 2) return null;
  const n = kinder.length; const jetzt = () => lernKindAktuell() || { id: k.id, reiter };
  const i0 = () => Math.max(0, kinder.findIndex((c) => c.id === jetzt().id));
  // LZ-App: Markierung sofort (vor dem Laden), alter Inhalt bleibt abgeblendet stehen
  const geh = (c) => { const a = jetzt(); if (!c || c.id === a.id) return;
    nav.querySelectorAll('.lw-k-chip').forEach((b) => { const an = b.dataset.id === String(c.id); b.classList.toggle('lw-k-aktiv', an); if (an) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current'); });
    lernWechselStart(); route('kind', `${c.id}-${a.reiter}`); };
  const erste = kinder.map((c) => String(c.name || '?').trim().charAt(0).toUpperCase());
  const eindeutig = new Set(erste).size === erste.length;
  const buchst = (c, j) => (eindeutig ? erste[j] : String(c.name || '').trim().split(/\s+/).pop().charAt(0).toUpperCase() || 'ABCDEFGH'[j]);
  const nav = el('nav', { class: 'lw-kinder', 'aria-label': 'Kind wechseln' },
    el('button', { type: 'button', class: 'lw-k-pfeil', 'aria-label': 'Vorheriges Kind (Alt+←)', onclick: () => geh(kinder[(i0() - 1 + n) % n]) }, '‹'),
    ...kinder.map((c, j) => el('button', { type: 'button', class: 'lw-k-chip' + (c.id === k.id ? ' lw-k-aktiv' : ''), 'aria-current': c.id === k.id ? 'page' : null, 'data-id': String(c.id),
      'aria-label': `${c.name}${c.klasse ? ` · ${LERN_SCHULART[c.schulart || 'gym_by'] || 'Gymnasium'} · Klasse ${c.klasse}` : ''}`, onclick: () => geh(c) },
      el('span', { class: 'lw-k-buchst', 'aria-hidden': 'true' }, buchst(c, j)), el('b', { class: 'lw-k-name' }, c.name),
      c.klasse ? el('small', { class: 'lw-k-info' }, `${LERN_SCHULART[c.schulart || 'gym_by'] || 'Gymnasium'} · Kl. ${c.klasse}`) : null)),
    el('button', { type: 'button', class: 'lw-k-pfeil', 'aria-label': 'Nächstes Kind (Alt+→)', onclick: () => geh(kinder[(i0() + 1) % n]) }, '›'));
  const taste = (ev) => { if (!document.body.contains(nav)) { removeEventListener('keydown', taste); return; }
    if (!ev.altKey || (ev.key !== 'ArrowLeft' && ev.key !== 'ArrowRight')) return; ev.preventDefault(); geh(kinder[(i0() + (ev.key === 'ArrowLeft' ? -1 : 1) + n) % n]); };
  addEventListener('keydown', taste);
  return nav;
}
// LW-3: Zahl „Zu besprechen“ am Reiter „Was wackelt“ (schule_wackelt_lesen; ohne Server-Aktion: keine Zahl)
let lernWackeltZahl = null; // von viewWackelt für den Kopf
function lernZbSetzen(n) { const a = document.querySelector('.lern-reiter a[href$="-wackelt"]'); if (!a) return; a.querySelector('.lw-zb')?.remove();
  if (n) a.append(el('b', { class: 'lw-zb', 'aria-label': `${n} zu besprechen` }, String(n))); }
const lernWackeltLesen = (id) => lernCall('schule_wackelt_lesen', { lernender_id: id }).then((r) => (Array.isArray(r?.eintraege) ? r : null)).catch(() => null);
// LW-3b: eine Kopfzeile – Zurück · Kinder-Umschalter (ersetzt die Überschrift) · Reiter · kleine Knöpfe; steht im App-Kopf (header.top) statt im Inhalt
function lernKindKopf(k, reiter, { kinder = null, zb = null } = {}) {
  const eltern = lernRolle() === 'eltern'; const info = k.klasse ? `${LERN_SCHULART[k.schulart || 'gym_by'] || 'Gymnasium'} · Klasse ${k.klasse}` : 'Klasse nicht gesetzt';
  return el('section', { class: 'lern-kind-kopf lw-schlank', 'aria-label': `Seite von ${k.name}` },
    lernKinderUmschalter(k, reiter, kinder) || el('div', { class: 'lw-k-einzel' }, el('b', {}, k.name), el('small', { class: 'lw-k-info' }, info)),
    el('nav', { class: 'lern-reiter', 'aria-label': 'Bereiche' }, ...LERN_REITER.map(([r, t]) => el('a', { href: `#/kind/${k.id}-${r}`, 'aria-current': r === reiter ? 'page' : null,
      onclick: (ev) => { if (ev.metaKey || ev.ctrlKey) return; // LZ-App: Reiter sofort markieren, alter Inhalt abgeblendet
        const a = lernKindAktuell() || { id: k.id, reiter }; ev.preventDefault(); if (r === a.reiter) return; // 0.91.2: Kind aus der Adresse (Wechsel läuft evtl. noch)
        ev.currentTarget.parentElement.querySelectorAll('a').forEach((x) => x.removeAttribute('aria-current')); ev.currentTarget.setAttribute('aria-current', 'page'); lernWechselStart(); route('kind', `${a.id}-${r}`); } }, t,
      r === 'wackelt' && zb ? el('b', { class: 'lw-zb', 'aria-label': `${zb} zu besprechen` }, String(zb)) : null))),
    el('div', { class: 'lern-kind-kopf-knoepfe' },
      eltern ? el('a', { class: 'btn lern-start', href: `#/reise/${k.id}`, 'aria-label': `Lernen starten: ${k.name}` }, 'Lernen starten ›') : null,
      eltern ? null : el('a', { class: 'small lern-reise-ansehen', href: `#/reise/${k.id}` }, 'Lernreise ansehen ›'),
      el('button', { type: 'button', class: 'lern-einstellen', 'aria-label': `${k.name} einstellen`, title: 'Einstellen', onclick: () => lernEinstellenBlatt(k.id) }, '⚙'),
      el('span', { class: 'lern-info-oben' }, el('a', { class: 'lern-info-link', href: '#/info', title: 'So funktioniert’s' }, 'ⓘ', el('span', { class: 'lw-vh' }, ' So funktioniert’s')))),
    lernKopfMehr(k, eltern));
}
// LZ-App S4: Handy – eine Zeile ‹ · Kinder · ⋯; „⋯“ öffnet Lernen starten, Einstellen, So funktioniert’s
function lernKopfMehr(k, eltern) {
  const menue = el('div', { class: 'lw-mehr-menue', role: 'group', 'aria-label': 'Mehr', hidden: true },
    el('a', { href: `#/reise/${k.id}`, 'aria-label': eltern ? `Lernen starten: ${k.name}` : 'Lernreise ansehen ›' }, eltern ? 'Lernen starten ›' : 'Lernreise ansehen ›'),
    el('button', { type: 'button', 'aria-label': `${k.name} einstellen`, onclick: () => { menue.hidden = true; lernEinstellenBlatt(k.id); } }, '⚙ Einstellen'),
    el('a', { href: '#/info' }, 'ⓘ So funktioniert’s'));
  const knopf = el('button', { type: 'button', class: 'lw-mehr', 'aria-label': 'Mehr', 'aria-expanded': 'false',
    onclick: (ev) => { ev.stopPropagation(); menue.hidden = !menue.hidden; knopf.setAttribute('aria-expanded', String(!menue.hidden));
      if (!menue.hidden) addEventListener('click', function zu(e) { if (!menue.contains(e.target)) { menue.hidden = true; knopf.setAttribute('aria-expanded', 'false'); } removeEventListener('click', zu); }); } }, '⋯');
  return el('span', { class: 'lw-mehr-ort' }, knopf, menue);
}
// Kopf in den App-Kopf setzen (statt der Überschrift); beim nächsten Seitenwechsel wieder heraus
function lernKopfEinsetzen(kopf) {
  const h = document.querySelector('header.top'); if (!h) { main.prepend(kopf); return; }
  h.querySelectorAll(':scope > .lern-kind-kopf').forEach((x) => x.remove());
  const t = h.querySelector('#title'); if (t) t.after(kopf); else h.prepend(kopf);
  document.body.classList.add('lw-kopf-schlank');
  lernWechselFertig();
  // LZ-App: Beim Wechsel zu einem anderen Kind/Reiter bleibt der Kopf stehen (kein Springen); der neue ersetzt ihn. Sonst heraus.
  const weg = () => { if (/^#\/kind\//.test(location.hash) && document.body.contains(kopf)) { addEventListener('hashchange', weg, { once: true }); return; }
    kopf.remove(); lernWechselFertig(); if (!document.querySelector('header.top > .lern-kind-kopf')) document.body.classList.remove('lw-kopf-schlank'); };
  addEventListener('hashchange', weg, { once: true });
}
const lernWechselStart = () => { main.classList.add('lw-wechsel'); main.setAttribute('aria-busy', 'true'); };
const lernWechselFertig = () => { main.classList.remove('lw-wechsel'); main.removeAttribute('aria-busy'); };
// Kind-Seite: kein leerer Ladebildschirm, wenn schon Inhalt da ist (Wechsel) – sonst wie bisher
const lernLaden = () => { if (!main.classList.contains('lw-wechsel') || !main.children.length) loading(); };
// LZ-App: alle Anfragen eines Reiters gleichzeitig starten (die Ansicht holt sie dann aus dem Speicher)
function lernReiterVorladen(id, reiter) {
  lernVorladen('schule_uebersicht'); lernVorladen('schule_lernstand', { lernender_id: id }); lernVorladen('schule_wackelt_lesen', { lernender_id: id });
  if (reiter !== 'wackelt') { lernVorladen('schule_plan_lesen', { lernender_id: id }); lernVorladen('schule_lehrplan_matrix'); lernVorladen('schule_lehrplan_uebersicht'); }
}
async function viewKind(arg) {
  const [idRoh, reiterRoh, ...rest] = String(arg || '').split('-');
  const id = Number(idRoh); const reiter = LERN_REITER.some(([r]) => r === reiterRoh) ? reiterRoh : 'ueberblick';
  if (!id) { route('lernen'); return; }
  // LW-1: alte Reiter „Stand“ (mit Schulart) und „Plan“ → „Lehrplan“
  if (reiterRoh === 'stand' || reiterRoh === 'plan') { route('kind', [id, 'lehrplan', ...(reiterRoh === 'stand' && LERN_MX_SA[rest[0]] ? [rest[0]] : [])].join('-')); return; }
  const geguard = viewGuard();
  // 0.91.2: eine Antwort zeichnet nur die Ansicht, für die sie angefragt wurde (gleiche Adresse, gleiches Kind, gleicher Reiter); veraltete werden verworfen
  const live = () => { const a = lernKindAktuell(); return geguard() && (!a || (a.id === id && (LERN_REITER.some(([r]) => r === a.reiter) ? a.reiter : 'ueberblick') === reiter)); };
  lernReiterVorladen(id, reiter); // LZ-App: alles gleichzeitig
  if (!main.classList.contains('lw-wechsel') && !document.querySelector('header.top > .lern-kind-kopf')) loading();
  const [u] = await Promise.all([lernCall('schule_uebersicht').catch(() => null), lernReiseKarteAlt.has(id) ? null : lernReiseKarte(id).catch(() => null)]); // WK F3: Namen der Reisekarte
  lernEinheitThemenMerken(u);
  if (!live()) return;
  const k = (u?.lernende || []).find((x) => x.id === id) || null;
  // Kopf zuerst (aus der gemerkten Übersicht), die Zahl „Zu besprechen“ kommt nach
  if (k) { main.querySelector(':scope > .lern-info-oben')?.remove();
    const kopf = lernKindKopf(k, reiter, { kinder: u.lernende, zb: lernWackeltZahl?.kind === id ? lernWackeltZahl.n : null });
    lernKopfEinsetzen(kopf); lernWechselStart(); main.classList.toggle('lw-wechsel', main.children.length > 0 && !main.querySelector(':scope > .spinner')); }
  if (reiter !== 'wackelt') lernWackeltLesen(id).then((w) => { if (live() && w) { lernWackeltZahl = { kind: id, n: Number(w.zu_besprechen) || 0 }; lernZbSetzen(lernWackeltZahl.n); } });
  try {
    if (reiter === 'ueberblick') await viewKindUeberblick(id, u);
    else if (reiter === 'wackelt') await viewWackelt([id, ...rest].join('-'));
    else await viewKindLehrplan(id, rest);
  } finally { if (live()) lernWechselFertig(); }
  if (!live()) return;
  if (!k) { route('lernen'); return; }
  // Hintergrund: gemerkte Daten hat sich geändert → Überblick/Was wackelt still neu zeichnen (Lehrplan nicht – dort wird gerade gearbeitet)
  const frisch = () => { if (!live()) { removeEventListener('lern-frisch', frisch); return; } if (reiter !== 'lehrplan') render(); };
  addEventListener('lern-frisch', frisch);
  // das andere Kind (bzw. die anderen) vorab laden – ohne Testkind
  setTimeout(() => { if (live()) (u.lernende || []).filter((c) => c.id !== id && !c.ist_test).forEach((c) => lernReiterVorladen(c.id, reiter)); }, 300);
}
async function viewKindUeberblick(id) {
  setChrome('Überblick', { back: true, showTabs: false });
  const live = viewGuard();
  lernLaden();
  const [u, ls, wk, p, mx] = await Promise.all([lernCall('schule_uebersicht'), lernCall('schule_lernstand', { lernender_id: id }).catch(() => null), lernWackeltLesen(id),
    lernCall('schule_plan_lesen', { lernender_id: id }).catch(() => null), lernMxLaden().then((d) => (d.matrix && !(d.kinder || []).some((c) => c.id === id) ? lernMxLaden(true) : d)).catch(() => null)]);
  if (!live()) return;
  const k = (u.lernende || []).find((x) => x.id === id); if (!k) { route('lernen'); return; }
  $('#title').textContent = k.name;
  // LZ-App S2: keine doppelten Karten mehr („Lernt es?“, „Wo hakt es?“, „Wo steht es?“, „Was kommt?“ sind in den neuen Karten aufgegangen)
  const l = lernKindLage(u, k, ls);
  const geschafft = lernGeschaffteFluege(u, k, ls).slice(0, 3);
  lernErsetze(main,
    lernUeberblickKarten(k, { u, ls, wk, p, mx, l, geschafft }),
    lernExpeditionenKind(u, k)); // LW-3b: Expeditionen stehen im Überblick (nicht mehr unter der Matrix)
}
// LW-3 (1a): Überblick-Karten mit Sprüngen – Gerade dran (→ Lehrplan mit dem Thema), Als Nächstes (→ Fahrplan), Zu besprechen (→ Was wackelt),
// Diese Woche, Stand um die Klasse des Kindes (Ringe wie im Reiter „Lehrplan“). Die bisherigen vier Fragen stehen darunter.
let lernLwStart = null; // { kind, fahrplan: true } – „Fahrplan ändern“ öffnet im Reiter „Lehrplan“ den Fahrplan (Handy/Tablet)
function lernUeberblickKarten(k, { u, ls, wk, p, mx, l = null, geschafft = [] }) {
  const M = mx && (mx.themen || []).length ? lernMxDaten(mx) : null; const sa = LERN_MX_SA[k.schulart] ? k.schulart : 'gym_by';
  const st = (x) => lernMxStufe(x, k);
  const lehrplan = (thema) => { if (thema) lernPlanZiel = { kind: k.id, thema }; route('kind', `${k.id}-lehrplan`); };
  // Gerade dran: Raster-Stand, sonst der nächste Flug der Lernreise
  const dranX = M?.themen.find((x) => st(x).stufe === 'dran'); const n0 = lernReiseDaten(u, k.id)?.naechste;
  let dran = null;
  if (dranX) { const s0 = st(dranX); const n = Number(dranX.roh.etappen_anzahl) || Number(s0.etappen) || dranX.etappen.length || 0; const j = Number(s0.etappe_jetzt) || Math.min((Number(s0.gelandet) || 0) + 1, n || 1);
    dran = { titel: dranX.titel, sub: `${dranX.gebiet}${n ? ` · Etappe ${j} von ${n}` : ''}`, g: Number(s0.gelandet) || 0, n, thema: dranX.id }; }
  else if (n0) dran = { titel: n0.titel, sub: `${lernFlugName(k.id, n0, n0.stadt || n0.ort_titel || '')} · ${n0.fertig}/${n0.n} Etappen`, g: n0.fertig, n: n0.n, thema: n0.thema_id || null };
  // Als Nächstes: Plätze 2–4 des Fahrplans (Reihenfolge wie im Reiter „Lehrplan“: erst ▶, dann ○ in Plan-Reihenfolge)
  const naechste = []; if (p?.orte) {
    const plan = lernPlanArbeitskopie(p); const ortById = new Map(p.orte.map((o) => [o.block_id, o]));
    const stufeT = (t) => (M?.by.get(t.thema_id) ? st(M.by.get(t.thema_id)) : t.stufe || {}).stufe;
    const fluege = plan.map((x) => { const o = ortById.get(x.block_id); const ts = (o?.themen || []).filter((t) => !x.ausgelassen.includes(t.thema_id));
      const sts = ts.map(stufeT); return { x, ts: ts.filter((t, i) => ['dran', 'kommt', 'nicht_im_plan', undefined].includes(sts[i])), art: sts.includes('dran') ? 0 : sts.some((v) => v === 'kommt' || v === 'nicht_im_plan' || v === undefined) ? 1 : 2 }; })
      .filter((f) => f.art < 2 && f.ts.length);
    const sicht = [...fluege.filter((f) => f.art === 0), ...fluege.filter((f) => f.art === 1)];
    sicht.forEach((f, i) => { if (i >= 1 && naechste.length < 3) naechste.push({ nr: i + 1, titel: f.ts.length > 1 ? `${f.ts[0].titel} und ${f.ts.length - 1} weitere` : f.ts[0].titel }); });
  }
  const zb = wk ? (wk.eintraege || []).filter((e) => e.status === 'zu_besprechen') : null;
  const w = ls?.woche || {}; const tage = (ls?.lerntage || []).filter((x) => lernTageSeit(x) < 7).length;
  const kl = Number(k.klasse) || null; const ringKl = kl ? [kl - 1, kl, kl + 1].filter((x) => LERN_MX_KL.includes(x)) : [];
  const knopf = (text, fn, cls = 'secondary') => el('button', { type: 'button', class: cls + ' lw-ue-knopf', onclick: fn }, text);
  return el('div', { class: 'lw-ue' },
    el('section', { class: 'lw-ue-karte lw-ue-dran' }, el('h3', { class: 'lw-ue-h' }, 'GERADE DRAN'),
      dran ? [el('b', { class: 'lw-ue-titel' }, dran.titel), el('small', {}, dran.sub), dran.n ? el('span', { class: 'lw-bar lw-ue-bar', role: 'img', 'aria-label': `${dran.g} von ${dran.n} Etappen gelandet` }, el('i', { style: `width:${lernPz(Math.min(dran.g, dran.n), dran.n)}%` })) : null,
        knopf('Im Lehrplan öffnen', () => lehrplan(dran.thema))] : [el('p', { class: 'muted small' }, 'Gerade nichts dran.'), knopf('Im Lehrplan öffnen', () => lehrplan(null))]),
    el('section', { class: 'lw-ue-karte' }, el('h3', { class: 'lw-ue-h' }, 'ALS NÄCHSTES'),
      naechste.length ? el('ol', { class: 'lw-ue-liste' }, ...naechste.map((x) => el('li', {}, el('span', { class: 'lw-nr' }, String(x.nr)), el('span', {}, x.titel)))) : el('p', { class: 'muted small' }, 'Nichts weiter im Fahrplan.'),
      knopf('Fahrplan ändern', () => { lernLwStart = { kind: k.id, fahrplan: true }; lehrplan(null); })),
    zb ? el('section', { class: 'lw-ue-karte' + (zb.length ? ' lw-ue-warn' : '') }, el('h3', { class: 'lw-ue-h' }, 'ZU BESPRECHEN'),
      el('b', { class: 'lw-ue-zahl' }, String(Number(wk.zu_besprechen) || zb.length)),
      el('small', {}, zb.length ? zb.slice(0, 3).map((e) => e.titel).join(' · ') + (zb.length > 3 ? ' …' : '') : 'alles besprochen'),
      knopf('Zu Was wackelt', () => route('kind', `${k.id}-wackelt`))) : null,
    // S2: „Diese Woche“ mit „zuletzt …“ und der Färbung aus „Lernt es?“; „Zuletzt geschafft“ klein daneben
    el('section', { class: 'lw-ue-karte lw-ue-woche' + (l ? ' amp-' + lernLerntAmpel(l) : '') }, el('h3', { class: 'lw-ue-h' }, 'DIESE WOCHE'),
      el('div', { class: 'lw-ue-werte' }, el('span', {}, el('b', {}, String(tage)), el('small', {}, tage === 1 ? 'Lerntag' : 'Lerntage')),
        el('span', {}, el('b', {}, String(w.aufgaben || 0)), el('small', {}, 'Bordkarten')),
        el('span', {}, el('b', {}, w.aufgaben ? `${lernPz(w.richtig || 0, w.aufgaben)} %` : '–'), el('small', {}, 'richtig'))),
      l ? el('small', { class: 'lw-ue-zuletzt' }, l.pause ? lernLerntText(l) : l.seit === null ? 'kein Lerntag in 4 Wochen' : `zuletzt ${l.seit === 0 ? 'heute' : l.seit === 1 ? 'gestern' : 'am ' + lernTag(l.zuletzt)}`) : null),
    el('section', { class: 'lw-ue-karte lw-ue-geschafft' }, el('h3', { class: 'lw-ue-h' }, 'ZULETZT GESCHAFFT'),
      geschafft.length ? el('ul', { class: 'lw-ue-gliste' }, ...geschafft.map((g) => el('li', {}, lernStufeZeichenEl(g.stufe), ' ', el('b', {}, g.titel),
        el('small', { class: 'muted' }, `${g.am ? ' · ' + lernTag(g.am) : ''}${g.kannSchon ? ' · kann schon' : ''}`)))) : el('p', { class: 'muted small' }, 'Noch kein Flug geschafft.')),
    M && ringKl.length ? el('section', { class: 'lw-ue-karte lw-ue-stand' }, el('h3', { class: 'lw-ue-h' }, `STAND ${sa === 'ib_myp' ? 'MYP-JAHR ' + (kl - 5) : 'KL. ' + kl}`),
      el('div', { class: 'lw-ue-ringe' }, ...ringKl.map((kk) => { const r = lernLwRingAusStand(k.schuljahr_stand, sa, kk) || lernLwRing(M.themen, st, sa, kk, lernKindGruppe(sa, k));
        return el('button', { type: 'button', class: 'lw-ue-ring', 'aria-label': `${r.text} – im Lehrplan ansehen`, onclick: () => { lernLwStart = { kind: k.id, klasse: kk }; lehrplan(null); } },
          el('span', { class: 'lw-kb' + (kk === 9 ? ' lw-hell' : ''), style: `background:${LERN_KL_FARBE[kk] || '#888'}` }, sa === 'ib_myp' ? `MYP ${kk - 5}` : `Kl. ${kk}`),
          lernLwRingEl(r, true), el('small', { class: 'lw-kn' }, `${r.fertig}/${r.themen} Themen`),
          el('span', { class: 'lw-rk2' }, ...Object.keys(LERN_MX_SA).filter((s2) => s2 !== sa).map((s2) => lernLwRingEl(lernLwRing(M.themen, st, s2, kk), false)))); })),
      lernLwStandTabelle(k, M, st, sa, ringKl),
      // S2: Einstufung je Schulart als eine Zeile (vorher Karte „Wo steht es?“)
      el('p', { class: 'small lw-ue-einst' }, 'Einstufung: ', lernStandZellen(u, k).map((z) => `${z.y.kurz} ${z.lang || z.text}`).join(' · '))) : null);
}
// KJ: Karte „Stand“ – je Klasse „noch x von y Flügen · noch a von b Etappen“ (Hauptklasse hinterlegt), darunter eingeplanter Zusatz (zählt nicht mit, ⓘ)
const LERN_SJ_RECHNUNG = (sa) => `So wird gerechnet: Prozent = gelandete Etappen ÷ alle Etappen der Pflicht-Flüge dieser Klasse im Lehrplan ${LERN_SCHULART[sa] || sa}. Flüge in Wiederholung und „Kann er“ zählen mit allen Etappen. „Flüge“ = Pflicht-Flüge der Klasse; fertig = alle Etappen gelandet und Flug-Test bestanden. Zusatz zählt nicht mit, auch nicht, wenn er eingeplant ist.`;
function lernLwStandTabelle(k, M, st, sa, ringKl) {
  const zeilen = ringKl.map((kk) => { const r = lernLwRingAusStand(k.schuljahr_stand, sa, kk) || lernLwRing(M.themen, st, sa, kk, lernKindGruppe(sa, k));
    return el('li', { class: 'lw-sj-zeile' + (kk === Number(k.klasse) ? ' lw-sj-haupt' : '') },
      el('b', {}, `${sa === 'ib_myp' ? `MYP-Jahr ${kk - 5}` : `Kl. ${kk}`} ${LERN_SCHULART[sa] || ''} · ${r.pz ?? 0} %`),
      el('span', {}, ` · noch ${Math.max(0, r.themen - r.fertig)} von ${r.themen} Flügen · noch ${Math.max(0, r.alle - r.gelandet)} von ${r.alle} Etappen`)); });
  const zp = (k.zusatz_plan || []).filter((z) => !z.geschafft);
  const titelVon = (z) => M.by.get(Number(z.thema_id))?.titel || `Thema ${z.thema_id}`;
  return el('div', { class: 'lw-sj' }, el('ul', { class: 'lw-sj-liste' }, ...zeilen),
    ...zp.map((z) => el('p', { class: 'small lw-sj-zus' }, `+ Zusatz eingeplant: ${titelVon(z)} (${Number(z.gelandet) || 0} von ${Number(z.etappen) || 0} Etappen) – zählt nicht mit `,
      el('button', { type: 'button', class: 'lw-info lw-sj-i', 'aria-label': 'So wird gerechnet', title: LERN_SJ_RECHNUNG(sa), onclick: (ev) => { const p0 = ev.currentTarget.nextElementSibling; if (p0) p0.hidden = !p0.hidden; } }, 'ⓘ'),
      el('span', { class: 'lw-sj-rechnung', hidden: true }, LERN_SJ_RECHNUNG(sa)))));
}
// Geschaffte Flüge: alle Etappen gelandet (Datum = letzte Landung); LA-5 ergänzt „kann schon“ je Flug
function lernGeschaffteFluege(u, k, ls) {
  const liste = (ls?.einheiten || []).filter((e) => (e.karten || []).length && e.karten.every((x) => x.sitzt))
    .map((e) => ({ einheit_id: e.einheit_id, titel: e.titel, ort: lernFlugName(k.id, { einheit_id: e.einheit_id }, e.ort || ''), am: e.karten.map((x) => x.sitzt_am).filter(Boolean).sort().pop() || null,
      // LB-2: Stufe vom Server, sonst: alle sicher → ◉, sonst ↻
      stufe: e.stufe || { stufe: e.karten.every((x) => x.sicher) ? 'komplett' : 'wiederholung' } }));
  // LA-4: „kann schon“ je Flug zählt wie geschafft (ohne Datum, hinten)
  const kann = lernStandModell(u, k).themen.filter((t) => t.kannSchon).map((t) => ({ titel: t.titel, ort: t.stadt || '', am: null, kannSchon: true, stufe: { stufe: 'komplett', gesetzt: 'komplett' } }));
  return [...liste.sort((a, b) => String(b.am || '').localeCompare(String(a.am || ''))), ...kann];
}
// I-10: Reisetage und Pausen – Formular (eintragen, ändern), Liste mit Ändern/Löschen; speichert über schule_notiz_setzen {pause}
const LERN_PAUSE_GRUND = ['Reisetag', 'krank', 'Ferien'];
function lernPauseFormular({ kinder = [], kindId = null, eintrag = null, fertig }) {
  const heute = lernIso(new Date());
  const von = el('input', { type: 'date', value: eintrag ? String(eintrag.von).slice(0, 10) : heute, 'aria-label': 'von', required: true });
  const bis = el('input', { type: 'date', value: eintrag ? String(eintrag.bis).slice(0, 10) : heute, 'aria-label': 'bis', required: true });
  const grund = el('input', { type: 'text', maxlength: '40', value: eintrag?.grund || '', placeholder: 'z. B. Reisetag', 'aria-label': 'Grund (ein Wort, freiwillig)', list: 'lern-pause-gruende' });
  const vorschlaege = el('datalist', { id: 'lern-pause-gruende' }, ...LERN_PAUSE_GRUND.map((g) => el('option', { value: g })));
  const chips = el('div', { class: 'lern-blatt-knoepfe', role: 'group', 'aria-label': 'Grund wählen' }, ...LERN_PAUSE_GRUND.map((g) => el('button', { type: 'button', class: 'lern-chip', onclick: () => { grund.value = g; } }, g)));
  const wer = !eintrag && kinder.length > 1 ? el('select', { 'aria-label': 'Für wen' }, el('option', { value: 'alle' }, 'alle Kinder'),
    ...kinder.map((k) => el('option', { value: String(k.id), selected: k.id === kindId }, k.name))) : null;
  const status = el('span', { class: 'small muted', role: 'status', 'aria-live': 'polite' });
  const form = el('form', { class: 'lern-pause-form' },
    el('div', { class: 'lern-pause-zeit' }, el('label', {}, el('span', {}, 'von'), von), el('label', {}, el('span', {}, 'bis'), bis)),
    chips, grund, vorschlaege, wer ? el('label', { class: 'lern-pause-wer' }, el('span', {}, 'für'), wer) : null,
    el('div', { class: 'row' }, el('button', { type: 'submit', class: 'primary' }, eintrag ? 'Ändern' : 'Eintragen'), status));
  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (bis.value < von.value) { status.textContent = '„bis“ darf nicht vor „von“ liegen.'; return; }
    const pause = { von: von.value, bis: bis.value, ...(grund.value.trim() ? { grund: grund.value.trim() } : {}) };
    const ziel = eintrag ? { pause: { ...pause, id: eintrag.id } } : (wer ? wer.value : String(kindId)) === 'alle' ? { alle: true, pause } : { lernender_id: Number(wer ? wer.value : kindId), pause };
    status.textContent = 'Speichere …';
    try { await lernCall('schule_notiz_setzen', ziel); status.textContent = 'Gespeichert'; fertig?.(); }
    catch (err) { status.textContent = /Notiz leer/.test(err.message) ? 'Reisetage lassen sich hier noch nicht speichern.' : 'Nicht gespeichert: ' + err.message; }
  });
  return form;
}
function lernPauseListe(pausen, { neu }) {
  const heute = lernIso(new Date());
  const tag = (d) => lernTag(String(d).slice(0, 10) + 'T00:00:00');
  if (!pausen.length) return el('p', { class: 'small muted' }, 'Noch nichts eingetragen.');
  return el('ul', { class: 'lern-pause-liste' }, ...pausen.map((p) => {
    const vorbei = String(p.bis).slice(0, 10) < heute; const platz = el('div');
    const meldung = el('span', { class: 'small muted', role: 'status' });
    return el('li', { class: vorbei ? 'vorbei' : '' },
      el('span', {}, el('b', {}, p.von === p.bis ? tag(p.von) : `${tag(p.von)}–${tag(p.bis)}`), p.grund ? ` · ${p.grund}` : '', vorbei ? el('small', { class: 'muted' }, ' · vorbei') : null,
        p.wer ? el('small', { class: 'muted' }, ` · ${String(p.wer).replace(/^[a-z]+:/, '')}`) : null),
      el('span', { class: 'lern-pause-knoepfe' },
        el('button', { type: 'button', class: 'secondary', onclick: () => lernErsetze(platz, lernPauseFormular({ eintrag: p, fertig: neu })) }, 'Ändern'),
        el('button', { type: 'button', class: 'secondary', 'aria-label': `Eintrag ${tag(p.von)} löschen`, onclick: async () => {
          try { await lernCall('schule_notiz_setzen', { pause: { id: p.id, loeschen: true } }); neu(); } catch (err) { meldung.textContent = err.message; } } }, 'Löschen'), meldung),
      platz);
  }));
}
// kurzer Weg von der Startseite: „Reisetag eintragen“ – eigenes Blatt, vorbelegt „alle Kinder“, heute
function lernPauseBlatt(kinder) {
  document.querySelector('.lern-blatt-huelle')?.remove();
  const taste = (ev) => { if (ev.key === 'Escape') zu(); };
  let geaendert = false;
  const zu = () => { huelle.remove(); document.removeEventListener('keydown', taste); if (geaendert) render(); };
  const blatt = el('section', { class: 'lern-blatt', role: 'dialog', 'aria-modal': 'true', 'aria-labelledby': 'lern-pause-titel' },
    el('div', { class: 'lern-blatt-kopf' }, el('h2', { id: 'lern-pause-titel' }, 'Reisetag eintragen'), el('button', { type: 'button', class: 'lern-blatt-zu', 'aria-label': 'Schließen', onclick: () => zu() }, '×')),
    el('section', { class: 'card lern-blatt-karte' }, el('p', { class: 'small muted' }, 'Eingetragene Tage zählen nicht für „Lernt“ und „kein Lerntag seit …“. Lernregeln, Wiederholungen und Nachtests ändern sich nicht. Ändern und löschen: „⚙ Einstellen“ des Kindes.'),
      lernPauseFormular({ kinder, kindId: kinder.length === 1 ? kinder[0].id : null, fertig: () => { geaendert = true; setTimeout(zu, 400); } })));
  const huelle = el('div', { class: 'lern-blatt-huelle', onclick: (ev) => { if (ev.target === huelle) zu(); } }, blatt);
  document.body.append(huelle); document.addEventListener('keydown', taste);
  blatt.querySelector('input')?.focus();
}
// LA-6: ⚙ Einstellen – Blatt (Tablet/Rechner von rechts, Handy von unten). Alles speichert sofort; Schließen zeichnet die Seite neu, wenn sich etwas geändert hat.
async function lernEinstellenBlatt(id) {
  document.querySelector('.lern-blatt-huelle')?.remove();
  const vorher = document.activeElement; let geaendert = false;
  const inhalt = el('div', { class: 'lern-blatt-inhalt' }, el('p', { class: 'muted' }, 'Lade …'));
  const titel = el('h2', { id: 'lern-blatt-titel' }, 'Einstellen');
  const taste = (ev) => { if (ev.key === 'Escape') zu(); };
  const zu = () => { huelle.remove(); document.removeEventListener('keydown', taste); if (geaendert) render(); else vorher?.focus?.(); };
  const schliessen = el('button', { type: 'button', class: 'lern-blatt-zu', 'aria-label': 'Schließen', onclick: zu }, '×');
  const blatt = el('section', { class: 'lern-blatt', role: 'dialog', 'aria-modal': 'true', 'aria-labelledby': 'lern-blatt-titel' }, el('div', { class: 'lern-blatt-kopf' }, titel, schliessen), inhalt);
  const huelle = el('div', { class: 'lern-blatt-huelle', onclick: (ev) => { if (ev.target === huelle) zu(); } }, blatt);
  document.body.append(huelle); document.addEventListener('keydown', taste); schliessen.focus();
  let p, ls; try { [p, ls] = await Promise.all([lernCall('schule_plan_lesen', { lernender_id: id }), lernCall('schule_lernstand', { lernender_id: id }).catch(() => null)]); }
  catch (err) { lernErsetze(inhalt, el('p', { class: 'err-text' }, err.message)); return; }
  if (!huelle.isConnected) return;
  const k = p.kind; titel.textContent = `${k.name} einstellen`;
  const speichern = async (daten, status) => {
    status.textContent = 'Speichere …';
    try { await lernCall('schule_kind_setzen', { lernender_id: id, ...daten }); Object.assign(k, daten.stufen ? { stufen: Object.fromEntries(Object.entries(daten.stufen).filter(([, v]) => v)) } : daten); geaendert = true; status.textContent = 'Gespeichert'; zeichne(); }
    catch (err) { status.textContent = 'Nicht gespeichert: ' + err.message; }
  };
  const knoepfe = (label, werte, aktiv, wahl) => el('div', { class: 'lern-blatt-knoepfe', role: 'group', 'aria-label': label },
    ...werte.map(([w, t]) => el('button', { type: 'button', class: 'lern-chip', 'aria-pressed': String(w === aktiv), onclick: () => { if (w !== aktiv) wahl(w); } }, t)));
  const s1 = el('span', { class: 'small muted', role: 'status', 'aria-live': 'polite' }); const s2 = el('span', { class: 'small muted', role: 'status', 'aria-live': 'polite' });
  const karte1 = el('section', { class: 'card lern-blatt-karte' }); const karte2 = el('section', { class: 'card lern-blatt-karte' });
  const zeichne = () => {
    const sa = k.schulart || 'gym_by';
    lernErsetze(karte1, el('h3', {}, 'Schule'),
      knoepfe('Hauptschulart', Object.entries(LERN_SCHULART), sa, (w) => speichern({ schulart: w }, s1)),
      knoepfe('Klasse', [5, 6, 7, 8, 9, 10].map((n) => [n, String(n)]), Number(k.klasse) || null, (w) => speichern({ klasse: w }, s1)),
      el('p', { class: 'small muted' }, 'Bestimmt seine Klasse in Lernreise und Plan.'), s1);
    if (k.stufen === undefined) { lernErsetze(karte2, el('h3', {}, 'Stand messen gegen …'), el('p', { class: 'small muted' }, 'Die Stufe je Schulart lässt sich hier noch nicht einstellen; gemessen wird an der Klasse.')); return; }
    const wahl = Object.fromEntries(LERN_SYS.map((y) => { const aus = lernStufe({ ...k, stufen: {} }, y.sa);
      const s = el('select', { 'aria-label': 'Stufe ' + y.name }, el('option', { value: '' }, `aus Klasse (${aus ? y.label(aus) : y.sa === 'ib_myp' && aus === 0 ? 'noch kein MYP-Jahr' : '–'})`),
        ...y.stufen.map((n) => el('option', { value: String(n), selected: Number(k.stufen?.[y.sa]) === n }, y.label(n))));
      s.addEventListener('change', () => speichern({ stufen: Object.fromEntries(LERN_SYS.map((q) => [q.sa, Number(wahl[q.sa].value) || null])) }, s2));
      return [y.sa, s]; }));
    lernErsetze(karte2, el('h3', {}, 'Stand messen gegen …'),
      el('div', { class: 'lern-blatt-stufen' }, ...LERN_SYS.map((y) => el('label', {}, el('span', {}, y.name), wahl[y.sa]))),
      el('p', { class: 'small muted' }, 'Nur für die Anzeige „Wo steht es?“ – ändert nichts an der Lernreise. IB: MYP-Jahr = Klasse − 5; unter Klasse 6: noch kein MYP-Jahr.'), s2);
  };
  zeichne();
  // 3. Notizen + Verlauf (zugeklappt)
  const notiz = el('textarea', { rows: '2', maxlength: '2000', placeholder: 'Notiz zum Kind (z. B. Prüfung am …, braucht mehr Zeit bei …)', 'aria-label': 'Notiz' });
  const notizStatus = el('span', { class: 'small muted', role: 'status' });
  const notizListe = el('div', {}, ...(p.notizen || []).map((n) => el('p', { class: 'small' }, el('b', {}, String(n.von || '').replace(/^[a-z]+:/, '') + ': '), n.text, el('span', { class: 'muted' }, ' · ' + new Date(n.am).toLocaleDateString('de-DE')))));
  const notizForm = el('form', { class: 'lern-rm-form' }, notiz, el('div', { class: 'row' }, el('button', { type: 'submit', class: 'secondary' }, 'Notiz speichern'), notizStatus));
  notizForm.addEventListener('submit', async (ev) => {
    ev.preventDefault(); const text = notiz.value.trim(); if (!text) return;
    try { await lernCall('schule_notiz_setzen', { lernender_id: id, text }); notizStatus.textContent = 'Gespeichert.'; notiz.value = '';
      lernAnhaengen(notizListe, el('p', { class: 'small' }, el('b', {}, 'Neu: '), text)); geaendert = true; }
    catch (err) { notizStatus.textContent = err.message; }
  });
  const karte3 = el('details', { class: 'card lern-blatt-karte' }, el('summary', {}, el('b', {}, `Notizen und Verlauf (${(p.notizen || []).length})`)),
    notizForm, notizListe,
    (p.verlauf || []).length ? el('div', { class: 'lern-blatt-verlauf' }, el('h4', {}, 'Verlauf'), ...(p.verlauf || []).map((v) => el('p', { class: 'small muted' }, `${new Date(v.am).toLocaleString('de-DE')} · ${String(v.akteur).replace(/^[a-z]+:/, '')} · ${v.anlass === 'plan' ? 'Plan geändert' : v.anlass === 'rueckreise' ? 'Rückreise nach Test' : v.anlass}`))) : el('p', { class: 'small muted' }, 'Noch kein Verlauf.'));
  // 4. Neuer Plan aus Lehrplan-Vorlage – mit Rückfrage und „Rückgängig“
  const normal = (p.plan || []).filter((r) => r.art === 'normal');
  const kannAbwaehlen = !!p.kann_abwaehlen || normal.some((r) => Array.isArray(r.ausgelassen));
  let revision = p.revision; let alt = normal.map((r) => ({ block_id: r.block_id, kann_schon: !!r.kann_schon, ...(kannAbwaehlen ? { ausgelassen: r.ausgelassen || [] } : {}) }));
  const rueckfrage = el('div', { class: 'lern-blatt-rueckfrage', role: 'alert', hidden: true });
  const setze = async (eintraege) => { const r = await lernCall('schule_plan_setzen', { lernender_id: id, revision, eintraege }); revision = r?.revision ?? revision + 1; geaendert = true; };
  const vorlage = lernPlanVorlage(p, kannAbwaehlen, (neuerPlan) => {
    rueckfrage.hidden = false;
    lernErsetze(rueckfrage, el('p', {}, el('b', {}, `Den ganzen Plan durch ${neuerPlan.length} ${neuerPlan.length === 1 ? 'Ort' : 'Orte'} ersetzen?`), ' Geschaffte Orte bleiben geschafft.'),
      el('div', { class: 'row' },
        el('button', { type: 'button', class: 'primary', onclick: async () => {
          const ks = new Map(alt.map((x) => [x.block_id, x.kann_schon]));
          const neu = neuerPlan.map((x) => ({ block_id: x.block_id, kann_schon: !!ks.get(x.block_id), ...(kannAbwaehlen ? { ausgelassen: x.ausgelassen } : {}) }));
          try { const vorher2 = alt; await setze(neu); alt = neu;
            lernErsetze(rueckfrage, el('p', {}, 'Plan ersetzt und gespeichert.'), el('button', { type: 'button', class: 'secondary', onclick: async () => {
              try { await setze(vorher2); alt = vorher2; lernErsetze(rueckfrage, el('p', {}, 'Rückgängig gemacht · Gespeichert')); } catch (err) { lernErsetze(rueckfrage, el('p', { class: 'err-text' }, err.message)); } } }, '↶ Rückgängig'));
          } catch (err) { lernErsetze(rueckfrage, el('p', { class: 'err-text' }, 'Nicht gespeichert: ' + err.message)); } } }, 'Ja, Plan ersetzen'),
        el('button', { type: 'button', class: 'secondary', onclick: () => { rueckfrage.hidden = true; } }, 'Abbrechen')));
  });
  lernAnhaengen(vorlage, rueckfrage);
  // 5. I-10: Reisetage und Pausen
  const karte5 = el('section', { class: 'card lern-blatt-karte lern-pause' });
  const zeichnePausen = async (neu) => {
    if (neu) { ls = await lernCall('schule_lernstand', { lernender_id: id }).catch(() => ls); geaendert = true; }
    if (!Array.isArray(ls?.pausen)) { lernErsetze(karte5, el('h3', {}, 'Reisetage und Pausen'), el('p', { class: 'small muted' }, 'Reisetage lassen sich hier noch nicht eintragen.')); return; }
    lernErsetze(karte5, el('h3', {}, 'Reisetage und Pausen'),
      el('p', { class: 'small muted' }, 'Eingetragene Tage zählen nicht für „Lernt“ und „kein Lerntag seit …“; ein Tag gilt als Kalendertag am Ort des Kindes. Lernregeln, Wiederholungen und Nachtests ändern sich nicht.'),
      lernPauseFormular({ kindId: id, fertig: () => zeichnePausen(true) }),
      lernPauseListe(ls.pausen, { neu: () => zeichnePausen(true) }));
  };
  zeichnePausen(false);
  lernErsetze(inhalt, karte1, karte2, karte5, karte3, vorlage);
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

// WT (0.93.5): Ist die Ansicht mit der gemerkten (alten) Karte gezeichnet, steht der Hauptknopf sichtbar, aber gesperrt und ohne Stadtname da,
// bis die frische Karte kommt (dann neu zeichnen). Kommt keine, gilt die alte und der Knopf wird frei. Gilt für Startkarte, „Gerade dran“, Abflugtafel und Einsteigen.
const LERN_ZIEL_KNOEPFE = '.rk-start, .rk-dran, .lr-flug-jetzt, .lr-einsteigen-knopf';
function lernZielBisFrisch(wurzel, kartePromise, karteAlt, live) {
  if (!wurzel || !kartePromise) return;
  wurzel.classList.add('lr-ziel-offen');
  const knoepfe = [...wurzel.querySelectorAll(LERN_ZIEL_KNOEPFE)]; knoepfe.forEach((k) => { k.setAttribute('aria-disabled', 'true'); k.setAttribute('tabindex', '-1'); });
  const sperre = (ev) => { if (wurzel.classList.contains('lr-ziel-offen') && ev.target.closest?.(LERN_ZIEL_KNOEPFE)) { ev.preventDefault(); ev.stopImmediatePropagation(); } };
  wurzel.addEventListener('click', sperre, true);
  const frei = () => { wurzel.classList.remove('lr-ziel-offen'); knoepfe.forEach((k) => { k.removeAttribute('aria-disabled'); k.removeAttribute('tabindex'); }); };
  kartePromise.then((k2) => { if (!live()) return; if (k2 && k2 !== karteAlt) render(); else frei(); }, () => { if (live()) frei(); });
}
// ---------- Kind: Heute dran ----------
// WK F5: letzte Reise-Ansicht je Kind – beim Rückweg sofort zeigen (gedimmt, nicht antippbar), bis der frische Stand da ist
const lernReiseLetzte = new Map();
async function viewReise(arg) {
  setChrome('Lernreise', { back: true, showTabs: false });
  const live = viewGuard();
  const letzte = lernReiseLetzte.get(Number(arg));
  if (letzte) { letzte.classList.add('lr-veraltet'); letzte.setAttribute('aria-busy', 'true'); lernErsetze(main, letzte); } else loading();
  // RK: Karten-Antwort gleichzeitig laden (je Sitzung einmal; nach einer Änderung sofort die alte zeigen, die neue im Hintergrund)
  const kidNr = Number(arg); const karteFrisch = lernReiseKarteSpeicher.has(kidNr); const karteAlt = kidNr && !karteFrisch ? lernReiseKarteAlt.get(kidNr) || null : null;
  const kartePromise = kidNr ? lernReiseKarte(kidNr).catch(() => null) : null; // WK F3: auch die Abflugtafel nennt die Namen der Karte (je Sitzung einmal)
  // WK F5: Merkheft und Wiederholungen gleichzeitig mit Übersicht/Konto holen (vorher zwei Runden nacheinander)
  const merkP = kidNr ? lernCall('schule_merkheft', { lernender_id: kidNr }).then((r) => r?.einheiten || []).catch(() => null) : null;
  const wdhP = kidNr ? lernWdhLaden(kidNr).catch(() => null) : null;
  const d = await lernLadeKind(arg);
  if (!d) { letzte?.classList.remove('lr-veraltet'); letzte?.removeAttribute('aria-busy'); }
  if (!d || !live()) return;
  const [merk, wdh] = await Promise.all([merkP ? merkP.then((x) => x ?? lernMerkDaten(d).catch(() => [])) : lernMerkDaten(d).catch(() => []), wdhP || lernWdhLaden(d.kind.id).catch(() => null)]);
  if (!live()) return;
  d.merk = merk; lernNamenSetzen(d); // WK F1/F3: nächste offene Etappe je Einheit, Namen der Reisekarte
  const { kind } = d; let n = d.naechste;
  $('#title').textContent = 'Lernreise ' + kind.name;
  const ortStand = (blockId) => (d.konto?.orte || []).find((o) => o.block_id === blockId);
  let et = n ? lernEtappenZahl(merk.find((m) => m.einheit_id === n.id)) : { n: 0, f: 0 };
  // Runde heute schon gemacht → Start führt ins Thema, der Rest wird nur angeboten (WD: Größe und „gemacht“ vom Server, sonst wie bisher)
  const ws = lernWdhStand(wdh, kind.id); const wdhGemacht = ws.gemacht, nWdh = ws.pflicht, wdhRest = ws.rest;
  // K1/U1: Den Stempel gibt es erst, wenn alle Flüge des Ortes geschafft sind – das Band zählt deshalb alle Etappen des Ortes.
  const ortVon = (n) => (n ? d.mit.filter((e) => e.block_id === n.block_id) : []).reduce((z, e) => { const m = merk.find((x) => x.einheit_id === e.id); const q = m ? lernEtappenZahl(m) : { n: e.n, f: e.fertig }; return { n: z.n + q.n, f: z.f + Math.min(q.f, q.n), fluege: z.fluege + 1 }; }, { n: 0, f: 0, fluege: 0 });
  let ort = ortVon(n);
  neuGest: if (lernNeu(kind) && (n || kartePromise)) {
    // RK-App: Reisekarte statt Anzeigetafel (nur wenn der Server die Karte liefert; Schalter „Abflugtafel“ führt zurück)
    let karte = null;
    // WK F5: Steht die letzte Ansicht schon (gedimmt) da, auf die frische Karte warten (kommt gleichzeitig mit der Übersicht) – statt mit der alten zu zeichnen und danach alles ein zweites Mal zu laden
    if (kartePromise) { karte = (letzte ? null : karteAlt) || await kartePromise; if (!karte && karteAlt) karte = karteAlt; }
    if (!live()) return;
    lernNamenSetzen(d); // WK: jetzt mit den Namen der Karte
    const mitKarte = Array.isArray(karte?.kontinente) && karte.kontinente.some((k) => (k.fluege || []).length);
    // WK 2 (A1): Hauptknopf aus den Ständen der Karte – auch ein Flug, dessen Etappen alle gelandet sind (Test fehlt), und der zweite Flug des Plan-Platzes
    const sch = mitKarte ? lernSchrittSetzen(d, karte, merk) : null;
    if (sch) { n = sch.n; et = sch.et; ort = ortVon(n); }
    if (!n) break neuGest; // nichts offen: wie bisher die schlichte Ansicht
    if (mitKarte && lernRkAnsicht(kind.id) === 'karte') {
      lernErsetze(main, lernRahmen(kind, 'reise', lernReisekarte(d, karte, lernRkStart(d, { n, et, nWdh, ws, wdhFertig: wdhGemacht }))));
      lernReiseLetzte.set(kind.id, main.firstElementChild);
      lernExFreiBeimStart(d); if (!document.querySelector('.lr-abschluss')) lernZpGeschafftZeigen(d);
      if (karte === karteAlt) lernZielBisFrisch(main.firstElementChild, kartePromise, karteAlt, live); // WT: alte Karte → Hauptknopf gesperrt, bis die neue da ist
      return;
    }
    lernErsetze(main, lernRahmen(kind, 'reise', ...lernAbflugtafel(d, { n, et, nWdh, wdhRest, wdhFertig: wdhGemacht, ort, ws }),
      (mitKarte || lernRkAnsicht(kind.id) === 'tafel') ? el('button', { type: 'button', class: 'lr-textlink rk-zur-karte', onclick: () => { lernRkAnsicht(kind.id, 'karte'); render(); } }, 'Zur Reisekarte ›') : null));
    lernDockErstNachTafel(main); // KJ 2 S6
    lernReiseLetzte.set(kind.id, main.firstElementChild);
    if (karte && karte === karteAlt) lernZielBisFrisch(main.firstElementChild, kartePromise, karteAlt, live); // WT: auch die Abflugtafel zeichnet mit der neuen Karte neu (vorher blieb der Schritt der alten stehen)
    lernExFreiBeimStart(d); if (!document.querySelector('.lr-abschluss')) lernZpGeschafftZeigen(d); return;
  }
  const teile = [el('header', { class: 'lr-kopf lr-kopf-kurz' }, el('p', { class: 'lr-gruss' }, `Hallo ${kind.name}!`)), lernExKarte(d), lernNachbuchungHinweis(d)].filter(Boolean);
  if (n) {
    const kont = d.orte.filter((o) => o.kontinent === (d.orte.find((x) => x.block_id === n.block_id)?.kontinent));
    const ortN = d.orte.find((o) => o.block_id === n.block_id) || {};
    // Ein einziger Startknopf: erst die fälligen Wiederholungen, dann direkt ins Üben des Themas.
    const testDran = lernTestDran(n, et); // alle Etappen sitzen → als Nächstes der Test, nicht wieder üben (LB-3: gesetzte Flüge ohne Test)
    const ziel = n.laeuft || testDran ? `#/lerneinheit/${kind.id}-${n.id}-test` : nWdh ? `#/wiederholen/${kind.id}` : lernUebenZiel(kind.id, n);
    teile.push(el('section', { class: 'lr-karte-box lr-haupt' },
      el('p', { class: 'lr-ueber' }, `JETZT DRAN · ${(n.stadt || '').toUpperCase()}`),
      el('h1', { class: 'lr-titel lr-titel-thema' }, n.titel),
      el('a', { class: 'lr-knopf lr-knopf-start', href: ziel }, n.laeuft ? 'Test weitermachen' : testDran ? 'Zum Test' : et.f || nWdh ? 'Weiter geht’s' : 'Los geht’s'),
      nWdh && !n.laeuft ? (ws.neu ? lernCheckinAnsage(ws) : el('p', { class: 'lr-leise lr-start-info' }, `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'}, dann ${n.stadt}.`)) : null,
      lernExtraLink(ws, kind.id),
      et.n ? el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${et.f} von ${et.n} Etappen sitzen` }, el('span', { style: `width:${Math.round(100 * et.f / et.n)}%` })), el('b', {}, `${et.f} von ${et.n} Etappen sitzen`)) : null,
      el('a', { class: 'lr-textlink', href: `#/lerneinheit/${kind.id}-${n.id}` }, 'Erst die Erklärungen ansehen'),
      el('div', { class: 'lr-kartenbild lr-kartenbild-klein' }, lernKarte({ orte: kont, fokus: kont.slice(0, Math.max(3, kont.indexOf(ortN) + 2)), hervor: LERN_ERDTEIL[ortN.kontinent], route: true,
        beschriftung: [{ ...ortN, text: `Du bist in ${n.stadt}`, jetzt: true, gross: true }], label: `Karte: ${n.stadt}, ${n.land}`, breite: 340, hoehe: 110 })),
      (() => { const o = ortStand(n.block_id); return o && o.themen > 1 ? el('p', { class: 'lr-leise lr-ortstand' },
        `${n.stadt} hat ${o.themen} Flüge, ${o.erledigt} davon geschafft. Den Stempel gibt es, wenn alle geschafft sind.`) : null; })()));
  } else teile.push(el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Gerade ist nichts offen'), el('p', { class: 'lr-leise' }, 'Neue Orte kommen bald. '), nWdh ? el('a', { class: 'lr-knopf', href: `#/wiederholen/${kind.id}` }, `${nWdh} ${nWdh === 1 ? 'Bordkarte' : 'Bordkarten'} wiederholen`) : el('a', { class: 'lr-knopf-zweit', href: `#/reisepass/${kind.id}` }, 'Zum Reisepass')));
  teile.push(lernStats(d.konto, { d }), el('a', { class: 'lr-textlink', href: `#/reisepass/${kind.id}` }, 'Reisepass und Belohnungen ansehen'),
    el('a', { class: 'lr-textlink lr-route-link', href: `#/route/${kind.id}` }, 'Meine Route 5–10 ›')); // LM-6
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
  lernExFreiBeimStart(d);
}

// W150 Abflug: Startseite als Abflugtafel. Oberste Zeile = jetzt dran, ein gelber Knopf im Daumenbereich.
// V9: Vor dem Thema höchstens eine Runde Wiederholungen am Tag (bis zu 6 Karten). Ist die Runde heute gemacht, führt der Startknopf ins Thema.
const LERN_WDH_RUNDE = 6;
// WD (22.11.) / WD-S 2: Der Server legt die Runde fest (Größe, Pflicht-Bordkarten mit `pflicht`) und setzt „Runde gemacht“ selbst, sobald alle Pflicht-Bordkarten
// beantwortet sind. Die App fragt ohne `anzahl` (der neue Server liefert alle fälligen). Der alte Server (ohne `runde`) liefert ohne `anzahl` nur 3 – dort
// fragt die App einmal mit 6 nach und verhält sich wie 0.84.0.
async function lernWdhLaden(kindId) {
  let r = await lernCall('schule_wiederholung', { lernender_id: kindId });
  if (r && (r.runde === undefined || r.runde === null) && Number(r.faellig || 0) > (r.aufgaben || []).length) r = await lernCall('schule_wiederholung', { lernender_id: kindId, anzahl: LERN_WDH_RUNDE });
  return r;
}
function lernWdhStand(wdh, kindId) {
  const auf = wdh?.aufgaben || []; const neu = !!wdh && wdh.runde !== undefined && wdh.runde !== null;
  if (!neu) { const gemacht = lernWdhHeute(kindId); return { neu, gemacht, runde: auf.length, offen: gemacht ? 0 : auf.length, erledigt: 0, pflicht: gemacht ? 0 : auf.length, rest: gemacht ? Number(wdh?.faellig || 0) : 0, liste: auf, extra: 0 }; }
  const gemacht = !!wdh.runde_gemacht; const runde = Math.max(0, Number(wdh.runde) || 0);
  const pfl = auf.some((a) => a.pflicht !== undefined) ? auf.filter((a) => a.pflicht) : auf.slice(0, runde);
  const offen = gemacht ? 0 : Math.min(pfl.length, runde || pfl.length);
  const erledigt = gemacht ? runde : Number.isFinite(Number(wdh.runde_erledigt)) ? Number(wdh.runde_erledigt) : Math.max(0, runde - offen);
  const faellig = Number(wdh.faellig || 0);
  // „Noch 3 Extra-Bordkarten?“ nur, wenn mehr fällig ist als die Runde (nach der Runde: wenn noch etwas fällig ist). Die Zahl der fälligen sieht das Kind nie.
  // 0.86.3 (ChatGPT 921, Sollte 2): Extras nur, wenn der Server dafür auch eine wählbare (frische) Bordkarte liefert; sonst ein ruhiger Hinweis
  const frei = auf.filter((a) => gemacht || !a.pflicht).length;
  const mehrFaellig = gemacht ? faellig > 0 : faellig > runde;
  const extra = mehrFaellig && frei > 0 ? 1 : 0; const keineFrische = mehrFaellig && frei === 0;
  return { neu, gemacht, runde: Math.max(runde, erledigt + offen), offen, erledigt, pflicht: offen, rest: 0, liste: pfl.slice(0, offen), extra, keineFrische, sterne: Number(wdh.sterne_je_richtig ?? wdh.sterne_wdh_richtig) || null,
    alle: auf, faellig };
}
// Koffer-Leiste (Vorgabe „abgelegt“ 1/2): je Pflicht-Bordkarte ein Koffer; bis 6 ein Päckchen, 7–9 zu 3, 10–12 zu 4 (gleichmäßig)
function lernKoffer(n, zustand = []) {
  const groesse = n <= 6 ? n : n <= 9 ? 3 : 4; const zahl = Math.max(1, Math.ceil(n / Math.max(1, groesse)));
  const teile = Array.from({ length: zahl }, (_, i) => Math.floor(n / zahl) + (i < n % zahl ? 1 : 0)); let k = 0;
  return el('div', { class: 'lr-koffer', role: 'img', 'aria-label': `${zustand.filter((z) => z === 'ok').length} von ${n} richtig` }, ...teile.map((m) => {
    const ks = Array.from({ length: m }, () => zustand[k++] || '');
    return el('span', { class: 'lr-koffer-p' + (ks.every((z) => z && z !== 'jetzt') ? ' lr-koffer-fertig' : '') }, ...ks.map((z) => el('i', { class: z ? 'lr-k-' + z.split(' ').join(' lr-k-') : '' })));
  }));
}
const lernMinuten = (n) => (n * 0.5 < 2 ? 'ganz kurz' : `etwa ${Math.ceil(n * 0.5)} Minuten`);
// Ansage auf der Startseite: „Vorher kurz einchecken“ (nur neuer Server, Runde offen)
function lernCheckinAnsage(ws) {
  if (!ws?.neu || !ws.offen) return null;
  const zahl = ws.erledigt ? `Noch ${ws.offen} von ${ws.runde} Bordkarten` : `${ws.runde} ${ws.runde === 1 ? 'Bordkarte' : 'Bordkarten'}`;
  return el('div', { class: 'lr-checkin-ansage' }, el('b', {}, ws.erledigt ? 'Check-in fortsetzen' : 'Vorher kurz einchecken'),
    el('span', { class: 'lr-leise' }, [`${zahl} von früher`, lernMinuten(ws.offen), ws.sterne ? `je richtig ★ ${ws.sterne}` : null].filter(Boolean).join(' · ')),
    lernKoffer(ws.runde, Array.from({ length: ws.runde }, (_, i) => (i < ws.erledigt ? 'da' : ''))));
}
const LERN_KEINE_FRISCHE = 'Heute keine passende frische Aufgabe – bleibt für später offen.';
const lernExtraLink = (ws, kindId) => (ws?.neu && ws.extra ? el('a', { class: 'lr-textlink lr-extra-link', href: `#/wiederholen/${kindId}-extra` }, `Noch 3 Extra-Bordkarten?${ws.sterne ? ` Je richtig ★ ${ws.sterne}` : ''}`)
  : ws?.neu && ws.gemacht && ws.keineFrische ? el('p', { class: 'lr-leise lr-keine-frische' }, LERN_KEINE_FRISCHE) : null);
function lernWdhHeute(kindId, setzen) {
  const heute = lernHeuteTag(kindId); // Teil 6: Tag des Kindes (heute_bis)
  try { if (setzen) localStorage.setItem('lern.wdhrunde.' + kindId, heute); return localStorage.getItem('lern.wdhrunde.' + kindId) === heute; } catch { return false; }
}
// V12: „Was kommt wann wieder?“ in einfachen Worten (Kindansicht)
function lernWdhErklaert(neu = false) {
  return el('details', { class: 'lr-mehr lr-wdh-erklaert' }, el('summary', {}, 'Was kommt wann wieder?'),
    el('p', {}, 'Sitzt eine Etappe, kommt sie später zum Wiederholen zurück – jedes Mal mit einer Bordkarte.'),
    el('p', {}, 'Die Abstände werden größer: nach 1, 3, 7, 14 und 30 Lerntagen. Ein Lerntag ist ein Tag, an dem du übst. Machst du Pause, wartet die Etappe.'),
    el('p', {}, 'Stimmt die Bordkarte nicht, kommt die Etappe am nächsten Lerntag wieder. Erst beim zweiten Fehler übst du sie noch einmal von vorn.'),
    neu ? el('p', {}, 'Am Anfang eines Lerntags checkst du kurz ein: ein paar Bordkarten von früher. Du kannst zwischendurch aufhören und später weitermachen. Extra-Bordkarten kannst du machen, wenn du magst.')
      : el('p', {}, 'Vor einem Flug kommen höchstens ' + LERN_WDH_RUNDE + ' Wiederholungen.'),
    neu ? el('p', {}, 'Jede richtige Bordkarte bringt Sterne. Schaffst du eine Etappe auch beim fünften Mal (nach 30 Lerntagen), ist sie abgelegt: Sie ist raus aus der regelmäßigen Wiederholung und kommt nur noch, wenn sie aufgefrischt werden muss – 30 Sterne. Sind alle Etappen eines Flugs abgelegt: 100 Sterne, und der Flug wird im Reisepass golden.') : null,
    el('p', {}, 'Nach dem Test zu einem Flug folgt später ein kurzer Nachtest.'));
}
function lernAbflugtafel(d, { n, et, nWdh, wdhRest = 0, wdhFertig = false, ort = null, ws = null }) {
  const { kind } = d; const sa = kind.schulart || 'gym_by';
  const kl = (e) => e.jahrgang?.[sa] ?? e.ziel_klasse;
  const code = (e) => String(e.stadt || e.ort_titel || '').toUpperCase();
  const zeile = (e, status, klasse = '') => el('a', { class: 'lr-flug' + klasse, href: `#/lerneinheit/${kind.id}-${e.id}` },
    el('span', { class: 'lr-flug-ort' }, el('b', {}, code(e)), el('small', {}, e.titel)),
    el('span', { class: 'lr-flug-status' }, el('b', {}, status), kl(e) ? el('small', {}, `Klasse ${kl(e)}`) : null));
  const testDran = lernTestDran(n, et); // alle Etappen sitzen → als Nächstes der Test, nicht wieder üben (WK 2: aus dem Schritt der Karte)
  const ziel = n.laeuft || testDran ? `#/lerneinheit/${kind.id}-${n.id}-test` : nWdh ? `#/wiederholen/${kind.id}` : lernUebenZiel(kind.id, n);
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
  const anrede = lernJwPlatz(kind.id, 'anrede', 'anrede', () => lernJwAnrede(kind.id));
  const ecke = (karte) => { if (karte && anrede && innerWidth < 600) { karte.classList.add('lr-jw-ecke-traeger'); anrede.classList.add('lr-jw-ecke'); karte.append(anrede); } return karte; };
  const ersteKarte = (d.nachbessern || []).length ? lernNbKarte(d) : null;
  return [
    el('header', { class: 'lr-kopf lr-tafelkopf' }, el('h1', { class: 'lr-titel' }, 'Abflüge · ', kind.name),
      innerWidth >= 600 ? anrede : null, // JW: Anrede „Digga“ einmal je Lerntag (KJ 2 S1: unter 600 px auf der Ecke der ersten Karte)
      el('a', { class: 'lr-chip-stern', href: `#/reisepass/${kind.id}`, 'aria-label': `${lernZahl(d.konto?.sterne ?? 0)} Sterne – zum Reisepass` }, '★ ' + lernZahl(d.konto?.sterne ?? 0))),
    // K3: oben drei Mini-Linien GYM · RS · IB; Antippen öffnet „Mein Weg · Stand“ bei dieser Schulart
    // KJ §0: Nachbessern immer zuerst; solange es ansteht, ist die Expedition nur ein Chip
    (d.nachbessern || []).length ? [ecke(ersteKarte), lernExChip(d)] : lernExKarte(d), // EX-App: offene Expedition = oberste, größte Karte, vor dem nächsten Flug
    rueckKarte,
    lernNachbuchungHinweis(d),
    (ersteKarte ? (x) => x : ecke)(el('section', { class: 'lr-abflugtafel', 'aria-label': 'Abflugtafel' },
      el('a', { class: 'lr-flug lr-flug-jetzt', href: ziel },
        el('span', { class: 'lr-flug-ort' }, el('span', { class: 'lr-klapp', role: 'img', 'aria-label': code(n) }, ...[...code(n).slice(0, 9)].map((c, i) => el('i', { style: `--i:${i}` }, c))), el('small', {}, n.titel)),
        el('span', { class: 'lr-flug-status lr-einsteigen' }, el('b', {}, n.laeuft ? 'TEST LÄUFT' : testDran ? 'TEST BEREIT' : 'EINSTEIGEN'), et.n ? el('small', {}, testDran ? 'alle Etappen sitzen' : `${offen} von ${et.n} Etappen offen`) : null)),
      ...weitere.slice(0, maxZ).map((e) => zeile(e, e.geschafft ? 'GELANDET' : e.fertig ? 'UNTERWEGS' : 'WARTET', e.geschafft ? ' lr-flug-gelandet' : '')),
      ...d.kann.slice(0, 1).map((e) => zeile(e, 'GELANDET', ' lr-flug-gelandet')),
      ...d.spaeter.slice(0, 1).map((e) => zeile(e, `AB KLASSE ${kl(e) ?? ''}`.trim(), ' lr-flug-spaeter')))),
    // 0.87.2 S1: Ansage direkt unter der Abflugtafel (vor Fortschritt und Stempel) – auf dem Handy im Blick
    nWdh && !n.laeuft && !testDran ? (ws?.neu ? lernCheckinAnsage(ws) : el('p', { class: 'lr-leise lr-start-info' }, `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'}, dann ${n.stadt}.`)) : null,
    band, // KJ 2 S2: Fortschrittslinie gehört zu „Gerade dran“ – vor der Zusatz-Karte
    lernZpKarte(d), // KJ §0.4: Zusatz · eingeplant unter „Gerade dran“
    lernSjKarte(d), // KJ §0.5: Mein Schuljahr
    // KJ 2 M2: keine Mini-Linien GYM · RS · IB mehr auf der Abflugtafel (widersprachen „Mein Schuljahr“); sie bleiben unter „Meine Route 5–10“ bzw. im Linienplan
    el('div', { class: 'lr-tafelchips' }, el('a', { href: `#/reisepass/${kind.id}` }, `◎ ${d.konto?.stempel ?? 0} Stempel`), el('span', {}, 'Abflug, wann es dir passt')),
    lernKnobelDesTages(d),
    wdhRest ? el('a', { class: 'lr-textlink', href: `#/wiederholen/${kind.id}` }, `Noch ${wdhRest} ${wdhRest === 1 ? 'Wiederholung' : 'Wiederholungen'} offen – wenn du magst`) : null,
    nWdh ? null : lernExtraLink(ws, kind.id),
    el('a', { class: 'lr-textlink', href: `#/lerneinheit/${kind.id}-${n.id}` }, 'Erst die Erklärungen ansehen'),
    el('a', { class: 'lr-textlink lr-route-link', href: `#/route/${kind.id}` }, 'Meine Route 5–10 ›'), // LM-6
    gruppe('Alle offenen Flüge', weitere.length > maxZ ? weitere : []),
    gruppe('Gelandet oder kann schon – zum Wiederholen', d.kann),
    gruppe('Aus früheren Klassen – zum Auffrischen', d.frueher),
    gruppe('Später – für höhere Klassen', d.spaeter),
    lernWdhErklaert(ws?.neu),
    jg?.themen && !(d.u && kind.klasse) ? el('section', { class: 'lr-karte-box lr-jgstand' },
      el('p', { class: 'lr-ueber' }, `MEIN STAND · ${(LERN_SCHULART[jg.schulart] || '').toUpperCase()} KLASSE ${jg.klasse}`),
      el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${jg.geschafft} von ${jg.themen} Flügen geschafft` }, el('span', { style: `width:${Math.round(100 * jg.geschafft / jg.themen)}%` })),
        el('b', {}, `${jg.geschafft} von ${jg.themen} Flügen`))) : null,
    el('div', { class: 'lr-dock lr-dock-start' },
      // 0.87.2 S1: eine Zeile über dem festen Knopf – das Kind weiß vor dem Tippen, dass erst der Check-in kommt (Zahl aus dem Serverwert)
      nWdh && !n.laeuft && !testDran && ws?.neu && ws.offen ? el('p', { class: 'lr-dock-ansage' }, `${ws.erledigt ? 'Noch' : 'Erst'} ${ws.offen} ${ws.offen === 1 ? 'Bordkarte' : 'Bordkarten'} Check-in · ca. ${Math.max(1, Math.ceil(ws.offen * 0.5))} Min.`)
        : testDran && !n.laeuft && et.n ? el('p', { class: 'lr-dock-ansage' }, `Alle ${et.n} ${et.n === 1 ? 'Stadt' : 'Städte'} gelandet – jetzt der Test`) : null,
      el('a', { class: 'lr-knopf lr-einsteigen-knopf', href: ziel },
      // N4: Die Wiederholung kann aus einem anderen Ort stammen – der Knopf nennt deshalb die Anzahl, nicht das Ziel.
      ...(n.laeuft || testDran ? [el('span', {}, n.laeuft ? 'Test weitermachen' : n.land ? `Flug-Test ${n.land}` : 'Zum Test'), el('span', { class: 'lr-mono' }, code(n).slice(0, 14) + ' ›')]
        : nWdh ? [el('span', {}, ws?.neu ? 'Weiter geht’s ›' : `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'} ›`)] // Vorgabe „abgelegt“ 1: Startknopf bleibt „Weiter geht’s“
        : wdhFertig ? [el('span', {}, `Weiter nach ${n.stadt || n.ort_titel || n.titel} ›`)]
        : [el('span', {}, 'Einsteigen'), el('span', { class: 'lr-mono' }, code(n).slice(0, 14) + ' ›')]))),
  ];
}

// KJ 2 S6: Die schwebende „Einsteigen“-Leiste erscheint erst, wenn die Abflugtafel (ihre Zeile mit dem gelben „EINSTEIGEN“) aus dem Bild gescrollt ist – nie zweimal derselbe Knopf übereinander.
// Ausgeblendet nur unsichtbar und nicht tippbar (bleibt im Ablauf, kein Springen); ohne IntersectionObserver wie bisher.
function lernDockErstNachTafel(wurzel) {
  const tafel = wurzel.querySelector('.lr-abflugtafel .lr-flug-jetzt') || wurzel.querySelector('.lr-abflugtafel'); const dock = wurzel.querySelector('.lr-dock-start'); if (!tafel || !dock || !('IntersectionObserver' in window)) return;
  dock.classList.add('lr-dock-weg');
  const io = new IntersectionObserver((xs) => { if (!dock.isConnected) { io.disconnect(); return; } const x = xs[xs.length - 1]; dock.classList.toggle('lr-dock-weg', x.isIntersecting); }, { threshold: 0 });
  io.observe(tafel);
}
// ---------- KJ (0.93.0): drei Karten der Kinderseite – Vorgabe inhalte/pruefung/kind/karten/umsetzung.md ----------
// Reihenfolge: Nachbessern (immer zuerst) · Expedition (bei Nachbessern nur als Chip) · Gerade dran · Zusatz · eingeplant · Mein Schuljahr.
const lernEinheitVon = (d, id) => (d.mit || []).find((x) => Number(x.id) === Number(id)) || (d.u?.einheiten || []).find((x) => Number(x.id) === Number(id)) || {};
const lernNbZiel = (kindId, n) => `#/lerneinheit/${kindId}-${n.einheit_id}-ueben${Number(n.etappe_nr) ? '-' + Number(n.etappe_nr) : ''}`;
const lernNbKreise = (folge, noetig) => el('span', { class: 'lr-nb-kreise', role: 'img', 'aria-label': `${folge} von ${noetig} richtig in Folge` },
  ...Array.from({ length: noetig }, (_, i) => el('i', { class: i < folge ? 'an' : '' }, i < folge ? '✓' : '')));
function lernNbKarte(d, { kompakt = false } = {}) {
  const liste = d.nachbessern || []; const n = liste[0]; if (!n) return null;
  const kid = d.kind.id; const folge = Math.max(0, Number(n.folge) || 0); const noetig = Number(n.folge_noetig) || 3;
  const e = lernEinheitVon(d, n.einheit_id);
  const knopf = el('a', { class: 'lr-nb-knopf', href: lernNbZiel(kid, n) }, folge >= 1 ? 'Weiter nachbessern ›' : 'Jetzt nachbessern ›');
  if (kompakt) return el('section', { class: 'lr-nb-karte lr-nb-kompakt', 'aria-label': 'Nachbessern' },
    el('span', { class: 'lr-nb-zeile' }, el('b', {}, '↻ Nachbessern: '), n.etappe || n.titel, ' ', lernNbKreise(folge, noetig)), knopf);
  const weitere = liste.length - 1;
  return el('section', { class: 'lr-nb-karte', 'aria-label': 'Nachbessern' },
    el('p', { class: 'lr-ueber lr-nb-kopf' }, '↻ NACHBESSERN'),
    el('h3', { class: 'lr-nb-titel' }, n.etappe || n.titel || 'Etappe'),
    el('p', { class: 'lr-nb-wo' }, `in ${[n.stadt || e.stadt, e.land, n.titel].filter(Boolean).join(' · ')}`),
    el('p', { class: 'lr-nb-satz' }, 'Die Etappe ist ein bisschen eingerostet. Mit ', el('b', {}, `${noetig} richtigen in Folge`), ' sitzt sie wieder.'),
    el('div', { class: 'lr-nb-stand' }, lernNbKreise(folge, noetig), el('span', {}, `${folge} von ${noetig}`)),
    knopf,
    el('p', { class: 'lr-leise lr-nb-klein' }, 'Deine Sterne und Stempel bleiben. Etwa 3 Minuten.'),
    weitere > 0 ? el('p', { class: 'lr-leise lr-nb-weitere' }, `+${weitere} weitere ${weitere === 1 ? 'Etappe' : 'Etappen'} zum Nachbessern`) : null);
}
// Expedition, solange Nachbessern ansteht: nur als Chip (wie EX 2b); die große Karte kommt danach zurück
function lernExChip(d) {
  const x = lernExOben(d); if (!x) return null;
  return el('a', { class: 'lr-ex-wartet lr-ex-chip-nb', href: `#/expedition/${d.kind.id}-${x.id}` }, `⛯ Expedition wartet: ${x.titel} ›`);
}
// Mein Schuljahr (SJ-App): Zahlen genau aus schuljahr_stand (alle Etappen, wie der Ring); Zusatz zählt nicht und wird nicht erwähnt
function lernSjZiel(alle, gelandet) {
  if (!alle) return null; const pz = (100 * gelandet) / alle; if (pz >= 100) return null;
  for (let p = Math.floor(pz / 10) * 10 + 10; p <= 100; p += 10) { const k = Math.ceil((alle * p) / 100) - gelandet; if (k > 0) return { p, k }; }
  return null;
}
// RS 2: Kurzform „Klasse 5 · 26 %“ (Hauptklasse aus schuljahr_stand) und Blatt mit der vollen Karte
function lernSjKurz(d) {
  const sj = d.schuljahr; const h = (Array.isArray(sj?.klassen) ? sj.klassen : []).find((x) => x.haupt); if (!h) return null;
  const sa = sj.schulart || d.kind.schulart || 'gym_by'; return `${sa === 'ib_myp' && h.myp_jahr ? `MYP-Jahr ${h.myp_jahr}` : `Klasse ${h.klasse}`} · ${Number(h.prozent) || 0} %`;
}
function lernSjBlatt(d, vorher, wo) {
  document.querySelectorAll('.lr-sj-blatt').forEach((x) => x.remove());
  const zu = () => { blatt.remove(); vorher?.focus?.({ preventScroll: true }); };
  const blatt = el('div', { class: 'lr-sj-blatt', role: 'dialog', 'aria-modal': 'true', 'aria-label': 'Mein Schuljahr', onclick: (ev) => { if (ev.target === blatt) zu(); } },
    el('div', { class: 'lr-sj-blatt-innen' }, lernSjKarte(d), el('button', { type: 'button', class: 'lr-knopf lr-knopf-klein lr-sj-zu', onclick: zu }, 'Schließen')));
  blatt.addEventListener('keydown', (ev) => { if (ev.key === 'Escape') zu(); });
  (wo || document.body).append(blatt); blatt.querySelector('.lr-sj-zu').focus({ preventScroll: true });
  addEventListener('hashchange', zu, { once: true });
}
function lernSjKarte(d) {
  const sj = d.schuljahr; const ks = Array.isArray(sj?.klassen) ? sj.klassen : []; const h = ks.find((x) => x.haupt) || null; if (!h) return null;
  const sa = sj.schulart || d.kind.schulart || 'gym_by'; const klName = (x) => (sa === 'ib_myp' && x.myp_jahr ? `MYP-Jahr ${x.myp_jahr}` : `Klasse ${x.klasse}`);
  const pz = Number(h.prozent) || 0; const fl = h.fluege || {}; const et = h.etappen || {};
  const vor = ks.find((x) => Number(x.klasse) === Number(h.klasse) - 1); const nach = ks.find((x) => Number(x.klasse) === Number(h.klasse) + 1);
  const ring = (p, gross) => { const r = gross ? 30 : 9; const u = 2 * Math.PI * r; const sw = gross ? 7 : 3.5; const ns = 'http://www.w3.org/2000/svg';
    const s0 = document.createElementNS(ns, 'svg'); const d0 = 2 * r + sw; s0.setAttribute('viewBox', `0 0 ${d0} ${d0}`); s0.setAttribute('width', d0); s0.setAttribute('height', d0); s0.setAttribute('aria-hidden', 'true');
    for (const [farbe, l] of [['#E6E1D4', u], ['#2E7D4F', (u * Math.min(100, p)) / 100]]) { const c = document.createElementNS(ns, 'circle'); c.setAttribute('cx', d0 / 2); c.setAttribute('cy', d0 / 2); c.setAttribute('r', r);
      c.setAttribute('fill', 'none'); c.setAttribute('stroke', farbe); c.setAttribute('stroke-width', sw); c.setAttribute('stroke-dasharray', `${l} ${u}`); c.setAttribute('transform', `rotate(-90 ${d0 / 2} ${d0 / 2})`); s0.append(c); }
    return s0; };
  const fertig = pz >= 100 || (Number(et.offen) === 0 && Number(et.gesamt) > 0);
  const ziel = fertig ? null : lernSjZiel(Number(et.gesamt) || 0, Number(et.gelandet) || 0);
  const balken = (x, text) => el('div', { class: 'lr-sj-nachbar' }, el('span', { class: 'lr-sj-nb-text' }, text),
    el('span', { class: 'lr-balken lr-sj-balken', role: 'img', 'aria-label': `${Number(x.prozent) || 0} Prozent` }, el('span', { style: `width:${Math.min(100, Number(x.prozent) || 0)}%` })), el('b', {}, `${Number(x.prozent) || 0} %`));
  return el('section', { class: 'lr-karte-box lr-sj-karte', 'aria-label': 'Mein Schuljahr' },
    el('p', { class: 'lr-ueber' }, `MEIN SCHULJAHR · ${String(LERN_SCHULART[sa] || sa).toUpperCase()}`),
    vor ? balken(vor, Number(vor.prozent) >= 100 || Number(vor.etappen?.offen) === 0 ? `✓ ${klName(vor)} geschafft` : `${klName(vor)}: noch ${Number(vor.fluege?.offen) || 0} Flüge · ${Number(vor.etappen?.offen) || 0} Etappen`) : null,
    el('div', { class: 'lr-sj-haupt' }, el('span', { class: 'lr-sj-ring' }, ring(pz, true), el('b', {}, `${pz} %`)),
      el('div', { class: 'lr-sj-text' }, el('b', { class: 'lr-sj-kl' }, fertig ? `${klName(h)} geschafft!` : klName(h)),
        el('p', {}, `Schon geschafft: ${Number(fl.fertig) || 0} von ${Number(fl.gesamt) || 0} Flügen · ${Number(et.gelandet) || 0} von ${Number(et.gesamt) || 0} Etappen`),
        fertig ? null : el('p', {}, 'Noch ', el('b', {}, `${Number(fl.offen) || 0} Flüge`), ' und ', el('b', {}, `${Number(et.offen) || 0} Etappen`), ` bis ${klName(h)} geschafft`))),
    ziel ? el('p', { class: 'lr-sj-ziel' }, `Nächstes Ziel: ${ziel.p} % – nur noch ${ziel.k} ${ziel.k === 1 ? 'Etappe' : 'Etappen'}!`) : null,
    nach ? balken(nach, `Danach ${klName(nach)}: ${Number(nach.fluege?.offen) || 0} Flüge · ${Number(nach.etappen?.offen) || 0} Etappen`) : null);
}
// Zusatz · eingeplant (ZP-App): unter „Gerade dran“, nie mit gelbem Hauptknopf; der Zusatz wird nie „nächster Flug“
function lernZpEintraege(d) {
  return (d.zusatzPlan || []).filter((z) => !z.geschafft).map((z) => { const e = lernEinheitVon(d, z.einheit_id); return { z, e }; });
}
function lernZpKarte(d, { kompakt = false } = {}) {
  const l = lernZpEintraege(d); if (!l.length) return null; const { z, e } = l[0]; const kid = d.kind.id;
  const y = Number(z.etappen) || 0, x = Math.min(y, Number(z.gelandet) || 0);
  const titel = e.titel || `Zusatz-Flug ${z.thema_id}`; const land = e.land || e.stadt || '';
  const knopf = el('a', { class: 'lr-zp-knopf', href: lernUebenZiel(kid, { id: z.einheit_id, etappeNr: e.etappeNr }) }, x ? `Weiter in ${e.stadt || land} ›` : `Nach ${land || 'dorthin'} fliegen ›`);
  if (kompakt) return el('section', { class: 'lr-zp-karte lr-zp-kompakt', 'aria-label': 'Zusatz eingeplant' }, el('span', {}, el('b', {}, '+ Zusatz: '), titel, ` · ${x}/${y}`), knopf);
  return el('section', { class: 'lr-zp-karte', 'aria-label': 'Zusatz eingeplant' },
    el('p', { class: 'lr-ueber lr-zp-kopf' }, '+ ZUSATZ · EINGEPLANT'),
    el('p', { class: 'lr-zp-titel' }, el('b', {}, titel), [e.stadt, e.land].filter(Boolean).length ? el('small', {}, [e.stadt, e.land].filter(Boolean).join(' · ')) : null),
    y ? el('div', { class: 'lr-zp-balken', role: 'img', 'aria-label': `${x} von ${y} Etappen gelandet` }, ...Array.from({ length: y }, (_, i) => el('i', { class: i < x ? 'voll' : '' }))) : null,
    el('p', { class: 'lr-zp-text' }, `${x} von ${y} Etappen · Extra-Flug, von deinen Eltern eingeplant`),
    knopf,
    el('p', { class: 'lr-leise lr-zp-klein' }, 'Ganz fertig: Stempel und ★ 100. Dein nächster Flug wartet trotzdem.'),
    l.length > 1 ? el('p', { class: 'lr-leise' }, `+${l.length - 1} weiterer Zusatz eingeplant`) : null);
}
// „Zusatz geschafft“: einmal je Teil auf diesem Gerät, sobald der Server ihn als geschafft meldet (Server bucht Stempel und ★ 100 genau einmal)
function lernZpGeschafftZeigen(d) {
  const z = (d.zusatzPlan || []).find((x) => x.geschafft && !lernZpGesehen(d.kind.id, x.thema_id)); if (!z) return false;
  try { localStorage.setItem(`lern.zp.${d.kind.id}.${z.thema_id}`, '1'); } catch { /* einmal je Sitzung */ }
  const e = lernEinheitVon(d, z.einheit_id); const land = e.land || e.stadt || ''; const nf = d.naechste;
  const y = Number(z.etappen) || 0; const sterne = Number(z.sterne) || 100;
  lernAbschlussZeigen(d.kind, el('div', { class: 'lr-ab-app lr-zp-geschafft lr-ab-anim' },
    el('a', { class: 'lr-ab-skip', href: `#/reise/${d.kind.id}`, onclick: () => lernAbschlussZu() }, 'Überspringen ›'),
    el('div', { class: 'lr-ab-szene lr-zp-szene lr-jw-mit' },
      el('div', { class: 'lr-ab-oben' }, `${land.toUpperCase()} · EXTRA-FLUG`),
      el('h2', { class: 'lr-ab-titel' }, 'Zusatz geschafft!'),
      el('p', { class: 'lr-ab-unter' }, `Alle ${y} Etappen von ${e.titel || 'diesem Zusatz-Flug'} sind gelandet.`),
      el('div', { class: 'lr-zp-stempel', 'aria-hidden': 'true' }, e.iso ? el('img', { src: lernRkFlagge(e.iso), alt: '' }) : null, el('b', {}, land.toUpperCase()), el('small', {}, 'ZUSATZ'))),
    el('div', { class: 'lr-ab-blatt' },
      el('div', { class: 'lr-ab-zeile lr-zp-lohn' }, el('span', {}, el('b', {}, 'Neuer Stempel im Reisepass'), el('br'), 'mit dem Rand „ZUSATZ“'), el('span', { class: 'lr-ab-sterne' }, `+ ★ ${lernZahl(sterne)}`)),
      nf ? lernGrossKnopf(`Weiter in ${nf.stadt || nf.ort_titel || nf.titel}`, null, { href: lernUebenZiel(d.kind.id, nf), onclick: () => lernAbschlussZu() })
        : lernGrossKnopf('Zur Reise', null, { href: `#/reise/${d.kind.id}`, onclick: () => lernAbschlussZu() }))), { label: 'Zusatz geschafft' });
  return true;
}
const lernZpGesehen = (kid, thema) => { try { return localStorage.getItem(`lern.zp.${kid}.${thema}`) === '1'; } catch { return false; } };

// ---------- RK-App (0.92.0): Reisekarte – ersetzt die Anzeigetafel der Kinderseite ----------
// Vorgabe inhalte/pruefung/kind/karte/umsetzung.md (§1–11) und EX-Vorgabe §7 (Antarktis). Ebenen Welt › Kontinent › Land, alles aus schule_reise_karte
// (keine feste Zahl an Kontinenten, Ländern, Städten). Umrisse: karte/welt.json und karte/kontinent-<id>.json (Natural Earth, im Build vorgerechnet von
// tools/karte/bauen.mjs), Flaggen karte/flaggen/<iso>.svg – erst beim Anzeigen geladen. Keine Kartenkacheln, kein Kartenserver.
// Die alte Anzeigetafel bleibt hinter dem Schalter „Abflugtafel“ erreichbar (je Kind auf dem Gerät gemerkt), bis der Nutzer die Karte freigibt.
const LERN_KARTE_BASIS = (() => { try { const s = document.currentScript?.src || [...document.scripts].map((x) => x.src).find((x) => /lernen\.js/.test(x)); return new URL('karte/', s || location.href).href; } catch { return 'karte/'; } })();
const lernKarteDateien = new Map(); // Datei → Promise (einmal je Sitzung)
const lernKarteMessung = {}; // Datei → { ms, bytes } (Ladezeit und Größe; Test/Meldung)
function lernKarteDatei(name) {
  if (!lernKarteDateien.has(name)) {
    const t0 = performance.now();
    lernKarteDateien.set(name, fetch(LERN_KARTE_BASIS + name).then(async (r) => { if (!r.ok) throw new Error('Karte fehlt: ' + name); const txt = await r.text();
      lernKarteMessung[name] = { ms: Math.round(performance.now() - t0), bytes: txt.length }; return JSON.parse(txt); })
      .catch((e) => { lernKarteDateien.delete(name); throw e; }));
  }
  return lernKarteDateien.get(name);
}
// Projektion wie im Build (d3: geoNaturalEarth1 für die Welt, geoMercator mit Drehung je Kontinent) – Probe in tools/karte/bauen.mjs
function lernKarteProj(q, lon, lat) {
  const rad = Math.PI / 180; const f = Number(lat) * rad;
  const l = ((Number(lon) - (q.art === 'merc' ? q.rot : -q.rot) + 540) % 360 - 180) * rad;
  let x, y;
  if (q.art === 'merc') { x = l; y = Math.log(Math.tan(Math.PI / 4 + Math.max(-1.5, Math.min(1.5, f)) / 2)); }
  else { const f2 = f * f, f4 = f2 * f2; x = l * (0.8707 - 0.131979 * f2 + f4 * (-0.013791 + f4 * (0.003971 * f2 - 0.001529 * f4))); y = f * (1.007226 + f2 * (0.015085 + f4 * (-0.044475 + 0.028874 * f2 - 0.005916 * f4))); }
  return [q.tx + q.k * x, q.ty - q.k * y];
}
const lernRkAnsicht = (kindId, setzen) => { try { if (setzen) localStorage.setItem('lern.rk.' + kindId, setzen); return localStorage.getItem('lern.rk.' + kindId) === 'tafel' ? 'tafel' : 'karte'; } catch { return 'karte'; } };
const lernRkSchl = (f) => (f.region ? `${f.iso}:${f.region}` : f.iso);
const lernRkKurz = (t) => String(t || '').replace(/\s*\(.*?\)\s*/g, ' ').replace(/\s+–\s+neu.*$/, '').trim();
const lernRkFlagge = (iso) => (iso ? LERN_KARTE_BASIS + 'flaggen/' + String(iso).toLowerCase() + '.svg' : '');
// Zustand eines Flugs/Landes (§4): golden · gerade dran · geschafft · „Kann er“ · im Plan · Zusatz · offen
function lernRkZustand(f, nst) {
  if (!f) return 'ohne';
  if (f.golden) return 'gold';
  if (f.stufe === 'dran' || (nst && Number(nst.thema_id) === Number(f.thema_id))) return 'dran';
  if (f.stempel) return 'gesch';
  if (f.gesetzt === 'komplett' || f.stufe === 'komplett') return 'kann';
  // RK-D (Prüfung RK-App 2, Abschnitt 3): gesperrt im Plan = wartet (graue Nummer + 🔒), gesperrt ohne Plan = nur gedämpft (kein Schloss)
  if (f.gesperrt && f.im_plan) return 'wartet';
  if (f.gesperrt) return 'gesperrt';
  if (f.zusatz) return 'zusatz';
  if (f.im_plan) return 'plan';
  return 'offen';
}
const LERN_RK_WORT = { gold: '★ golden – alles sitzt', dran: 'gerade dran', gesch: '✓ geschafft – noch in Wiederholung', kann: '◉ kannst du schon', plan: 'im Plan', wartet: '🔒 wartet', gesperrt: 'noch gesperrt', zusatz: 'Zusatz für Entdecker', offen: 'offen', ohne: '' };
const LERN_RK_STADT = { abgelegt: 'abgelegt ★', offen: 'kommt noch', begonnen: 'angefangen', gelandet: 'gelandet', sicher: 'sitzt sicher', wieder_offen: 'wieder offen – nachbessern' }; // M1: wieder offen ist nicht gelandet
// Startknopf (wie die Abflugtafel): Test läuft / Test bereit / erst Check-in / Thema
function lernRkStart(d, { n, et, nWdh, ws, wdhFertig }) {
  const kind = d.kind;
  const testDran = lernTestDran(n, et); // WK 2: aus dem Schritt (Karte), sonst aus dem Merkheft
  const ziel = n.laeuft || testDran ? `#/lerneinheit/${kind.id}-${n.id}-test` : nWdh ? `#/wiederholen/${kind.id}` : lernUebenZiel(kind.id, n);
  const stadt = n.stadt || n.ort_titel || n.titel; const land = n.land || d.schritt?.f?.land || null;
  const text = n.laeuft ? 'Test weitermachen' : testDran ? (land ? `Flug-Test ${land}` : 'Zum Flug-Test') : nWdh ? (ws?.neu ? 'Weiter geht’s' : `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'}`) : wdhFertig ? `Weiter nach ${stadt}` : `Weiter in ${stadt}`;
  const ansage = nWdh && !n.laeuft && !testDran && ws?.neu && ws.offen ? `${ws.erledigt ? 'Noch' : 'Erst'} ${ws.offen} ${ws.offen === 1 ? 'Bordkarte' : 'Bordkarten'} Check-in · ca. ${Math.max(1, Math.ceil(ws.offen * 0.5))} Min.`
    : testDran && et.n ? `Alle ${et.n} ${et.n === 1 ? 'Stadt' : 'Städte'} gelandet – jetzt der Test` : null;
  const s = d.schritt && d.schritt.e === n ? d.schritt : null;
  return { ziel, text, testDran, ansage, wdh: nWdh, einheit: n.id, flugThema: s?.f ? Number(s.f.thema_id) : null, nr: testDran ? null : s?.nr || n.etappeNr || null };
}

function lernRkGrundText(f, laender) {
  if (!f?.gesperrt) return null;
  if (f.gesperrt_grund === 'klasse') return f.ab_klasse ? `Ab Klasse ${f.ab_klasse} – kommt später.` : 'Kommt später.';
  const n = laender.map((x) => x.name);
  if (!n.length) return 'Wartet noch auf ein anderes Land.';
  const liste = n.length === 1 ? n[0] : n.length === 2 ? `${n[0]} und ${n[1]}` : `${n[0]}, ${n[1]} und ${n.length - 2} ${n.length - 2 === 1 ? 'weiteres Land' : 'weitere Länder'}`;
  return `Erst ${liste} schaffen`;
}

function lernReisekarte(d, karte, start) {
  const kind = d.kind;
  const KONT = (karte.kontinente || []).filter((k) => (k.fluege || []).length || k.laender);
  const alleFluege = KONT.flatMap((k) => (k.fluege || []).map((f) => ({ ...f, kontinent_id: k.id })));
  // RK-D: gesperrte Flüge – der Startknopf führt nie dorthin (auch nicht über naechster_start)
  const gesperrtThema = new Set(alleFluege.filter((f) => f.gesperrt).map((f) => Number(f.thema_id)));
  // NB-App: naechster_start.grund = 'nachbessern' → die wieder offene Stadt bekommt ihre eigene (orange) Karte; „Gerade dran“ bleibt der nächste Pflicht-Flug
  const nbStart = karte.naechster_start?.grund === 'nachbessern' ? karte.naechster_start : null;
  const nbFlug = nbStart ? alleFluege.find((f) => Number(f.thema_id) === Number(nbStart.thema_id)) || null : null;
  const nst = karte.naechster_start && !nbStart && !gesperrtThema.has(Number(karte.naechster_start.thema_id)) ? karte.naechster_start : null;
  // WK 2: „Gerade dran“ ist der Flug des Hauptknopfs (Schritt aus den Ständen), sonst wie bisher
  const dranFlug0 = (start?.flugThema && alleFluege.find((f) => Number(f.thema_id) === start.flugThema)) || alleFluege.find((f) => nst && Number(f.thema_id) === Number(nst.thema_id)) || alleFluege.find((f) => f.stufe === 'dran' && !f.gesperrt) || null;
  if (start && !start.wdh && start.einheit) {
    const e0 = (d.mit || []).find((e) => e.id === start.einheit);
    if (e0 && gesperrtThema.has(Number(e0.thema_id)) && !e0.laeuft) { // Ersatz: der Flug, der auf der Karte dran ist, sonst der nächste freie im Plan
      const frei0 = (e) => !e.geschafft && !gesperrtThema.has(Number(e.thema_id));
      const alt = (dranFlug0 && (d.mit || []).find((e) => frei0(e) && Number(e.thema_id) === Number(dranFlug0.thema_id))) || (d.mit || []).find((e) => e.gruppe === 'jetzt' && frei0(e));
      start = alt ? { ...start, ziel: lernUebenZiel(kind.id, alt), text: `Weiter in ${alt.stadt || alt.ort_titel || alt.titel}`, testDran: false, ansage: null, einheit: alt.id }
        : { ...start, ziel: null, text: 'Gerade wartet alles auf ein anderes Land', testDran: false, ansage: null, einheit: null };
    }
  }
  const flugVon = (kontId, gebiet) => alleFluege.find((f) => f.kontinent_id === kontId && lernRkSchl(f) === gebiet) || null;
  const dranFlug = dranFlug0;
  // Grund der Sperre: fehlendes Visum → Länder der fehlenden Orte (Orte → Flüge über schule_uebersicht.themen), sonst der Name des Ortes
  const visumLaender = (f) => { const aus = []; const fertig = (y) => ['gold', 'gesch', 'kann'].includes(lernRkZustand(y, nst));
    for (const v of f?.visum_fehlt || []) {
      const ids = new Set((d.u?.themen || []).filter((t0) => Number(t0.block_id) === Number(v.block_id)).map((t0) => Number(t0.thema_id)));
      const fl = alleFluege.filter((y) => (ids.has(Number(y.thema_id)) || ids.has(Number(y.teil_stamm))) && !fertig(y) && !y.zusatz);
      if (fl.length) { for (const y of fl) if (!aus.some((a) => a.name === y.land)) aus.push({ name: y.land, flug: y }); }
      else if (v.ort && !aus.some((a) => a.name === v.ort)) aus.push({ name: v.ort, flug: null }); }
    return aus; };
  const grundVon = (f) => lernRkGrundText(f, visumLaender(f));
  // WK F1: „Gerade dran“ nennt die Stadt der Etappe, in die der Knopf führt (nächste offene Pflicht-Etappe der Einheit), nicht eine fällige
  const startE = start?.einheit ? (d.mit || []).find((e) => Number(e.id) === Number(start.einheit)) : null;
  const startNr = start?.nr || startE?.etappeNr || null;
  const startStadt = dranFlug && startNr && (start?.flugThema === Number(dranFlug.thema_id) || (startE && Number(startE.thema_id) === Number(dranFlug.thema_id))) ? (dranFlug.staedte || []).find((s) => Number(s.nr) === Number(startNr)) : null;
  // WK 2: nie eine gelandete Stadt als „Gerade dran“ – auch nicht über naechster_start.stadt (Server-Rückfall Stadt 1); beim Flug-Test keine Stadt
  const offeneStadt = (s) => (s && !lernStadtGelandet(s) ? s : null);
  const dranStadt = start?.testDran ? null : startStadt ? startStadt : dranFlug && nst?.stadt ? offeneStadt((dranFlug.staedte || []).find((s) => Number(s.nr) === Number(nst.stadt.nr)))
    : dranFlug && nbStart ? (dranFlug.staedte || []).slice().sort((a, b) => Number(a.nr) - Number(b.nr)).find((s) => s.pflicht !== false && !['gelandet', 'sicher'].includes(s.stand)) || null : null;
  const handy = () => innerWidth < 1100;
  const rechner = () => !handy();
  // Zustand der Ansicht
  const z = { ebene: 'kontinent', kont: dranFlug?.kontinent_id ?? nst?.kontinent_id ?? KONT[0]?.id, land: null, sel: null, vb: null, daten: null, laedt: false };
  if (z.kont === undefined || z.kont === null) z.ebene = 'welt';
  const ns = 'http://www.w3.org/2000/svg';
  const s = (tag, a = {}, ...kids) => { const e = document.createElementNS(ns, tag); for (const [k, v] of Object.entries(a)) if (v !== null && v !== undefined && v !== false) e.setAttribute(k, v); for (const c of kids.flat()) if (c !== null && c !== undefined && c !== false) e.append(c); return e; };
  const svg = s('svg', { class: 'rk-svg', role: 'img', 'aria-label': 'Reisekarte' });
  const ebenen = { meer: s('g'), land: s('g', { class: 'rk-laender' }), kette: s('g', { class: 'rk-kette' }), route: s('g', { class: 'rk-routen' }), oben: s('g', { class: 'rk-oben' }) };
  svg.append(s('defs', {}, s('pattern', { id: 'rk-schraffur', width: 6, height: 6, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(45)' }, s('rect', { width: 6, height: 6, class: 'rk-schr-g' }), s('line', { x1: 0, y1: 0, x2: 0, y2: 6, class: 'rk-schr-l' })),
    s('clipPath', { id: 'rk-kreis', clipPathUnits: 'objectBoundingBox' }, s('circle', { cx: 0.5, cy: 0.5, r: 0.5 }))), ebenen.meer, ebenen.land, ebenen.kette, ebenen.route, ebenen.oben);
  const rahmen = el('div', { class: 'rk-rahmen' }, svg);
  const pfad = el('nav', { class: 'rk-pfad', 'aria-label': 'Ebene der Karte' });
  const blatt = el('section', { class: 'rk-blatt', 'aria-live': 'polite', hidden: true });
  const seite = el('aside', { class: 'rk-seite' });
  const schwebe = el('div', { class: 'rk-schwebe' });
  const zoomKnoepfe = el('div', { class: 'rk-zoom' },
    el('button', { type: 'button', 'aria-label': 'Hineinzoomen', onclick: () => zoomUm(1 / 1.5) }, '+'),
    el('button', { type: 'button', 'aria-label': 'Herauszoomen', onclick: () => zoomUm(1.5) }, '−'),
    el('button', { type: 'button', 'aria-label': 'Ganze Ebene zeigen', onclick: () => { passend(); zeichneOben(); } }, '⤢'),
    // M1 (Prüfung RK-App 2): „Zu mir“ auf dem Handy in den Kartenknöpfen unter ⤢ (im Kopf nur auf breiten Bildschirmen)
    dranFlug ? el('button', { type: 'button', class: 'rk-zumir-k', 'aria-label': 'Zu mir', title: 'Zu mir', onclick: () => zuMir() }, '📍') : null,
    // K4: kleine Legende hinter ⓘ
    el('button', { type: 'button', class: 'rk-legende-knopf', 'aria-label': 'Was die Zeichen bedeuten', 'aria-expanded': 'false', onclick: (ev) => { const zu = legende.hidden; legende.hidden = !zu; ev.currentTarget.setAttribute('aria-expanded', String(zu)); } }, 'ⓘ'));
  const legende = el('div', { class: 'rk-legende', hidden: true, role: 'note' }, el('b', {}, 'Was die Zeichen bedeuten'),
    ...[['✈', 'gerade dran', 'dran'], ['2', 'Platz im Plan', 'plan'], ['✓', 'geschafft', 'gesch'], ['★', 'golden', 'gold'], ['↻', 'wieder offen – nachbessern', 'wieder'], ['🔒', 'wartet', 'wartet'], ['+', 'Zusatz', 'zusatz']]
      .map(([z0, w, c]) => el('span', { class: 'rk-leg-zeile' }, el('i', { class: 'rk-leg-z rk-leg-' + c, 'aria-hidden': 'true' }, z0), ' ' + w)));
  const zuMir = () => { const f = nbFlug || dranFlug; if (!f) return; z.kont = f.kontinent_id; geheLand(lernRkSchl(f)); }; // NB: „Zu mir“ springt zur offenen Stadt
  const quelle = el('p', { class: 'rk-quelle' }, 'Karte: Natural Earth · Orte: GeoNames (CC BY 4.0)' + (z.ebene === 'welt' ? ' · Stationen: COMNAP' : ''));
  const kartenTeil = el('div', { class: 'rk-karte' }, rahmen, zoomKnoepfe, legende, quelle);
  // S1/S2: eine Kopfzeile im App-Kopf (wie LW-3b): ‹ · Meine Reise · Pfad · Abflugtafel · ★ · ≡ – die Karte füllt den Rest des Fensters
  const menue = () => { const dlg = wurzel.closest('.lr-mit-menue')?.querySelector('dialog.lr-blatt'); if (dlg && !dlg.open) dlg.showModal(); };
  const schmal = () => innerWidth <= 760;
  const kopf = el('div', { class: 'rk-kopf' }, el('b', { class: 'rk-titel' }, 'Meine Reise'), pfad,
    dranFlug ? el('button', { type: 'button', class: 'rk-zumir', 'aria-label': 'Zu mir', title: 'Zu mir', onclick: zuMir }, el('span', { class: 'rk-sym', 'aria-hidden': 'true' }, '📍'), el('span', { class: 'rk-wort' }, ' Zu mir')) : null,
    el('button', { type: 'button', class: 'rk-tafel-knopf', 'aria-label': 'Abflugtafel', title: 'Abflugtafel', onclick: () => { lernRkAnsicht(kind.id, 'tafel'); render(); } }, el('span', { class: 'rk-sym', 'aria-hidden': 'true' }, '▤'), el('span', { class: 'rk-wort' }, ' Abflugtafel')),
    el('a', { class: 'lr-chip-stern rk-stern', href: `#/reisepass/${kind.id}`, 'aria-label': `${lernZahl(d.konto?.sterne ?? 0)} Sterne – zum Reisepass` }, '★ ' + lernZahl(d.konto?.sterne ?? 0)),
    el('button', { type: 'button', class: 'rk-menue', 'aria-label': 'Menü', 'aria-haspopup': 'dialog', onclick: menue }, '≡'));
  const wurzel = el('div', { class: 'rk' + (handy() ? ' rk-handy' : ' rk-rechner') }, el('div', { class: 'rk-koerper' }, kartenTeil, seite));
  requestAnimationFrame(() => { const h = document.querySelector('header.top'); if (!h || !document.body.contains(wurzel)) return;
    h.querySelectorAll(':scope > .rk-kopf').forEach((x) => x.remove()); const tt = h.querySelector('#title'); if (tt) tt.after(kopf); else h.prepend(kopf);
    kopf.classList.add('lr-abflug-' + lernGestaltung(kind)); document.body.classList.add('rk-kopf-oben'); hoeheSetzen(); if (z.vb) { passend(); zeichneOben(); } });
  addEventListener('hashchange', () => { kopf.remove(); document.body.classList.remove('rk-kopf-oben'); }, { once: true });

  // ---------- Startknopf schwebend in der Karte (§1), Expedition darüber (EX §3) ----------
  // S3: rechts die Bordkarten der aktuellen Stadt (x/6 aus etappen_stand der Einheit), der Städte-Stand nur im Text „Stadt 5 von 13“
  let stadtStand = null;
  if (dranStadt && start.einheit) lernCall('schule_einheit_lesen', { lernender_id: kind.id, einheit_id: start.einheit }).then((x) => {
    const es = x?.etappen_stand?.[dranStadt.lernziel]; if (!es) return;
    const y = Number(es.ziel) || 0; const v = Number(es.eigene_loesungen ?? es.serie ?? 0); if (!y) return;
    stadtStand = { x: Math.min(v, y), y }; if (document.body.contains(wurzel)) { lernErsetze(schwebe, ...(handy() ? geradeDran() : [])); zeichneSeite(); if (z.ebene === 'land') zeichneOben(); }
  }).catch(() => { /* ohne Stand */ });
  // S2: Expedition auf der Reisekarte einzeilig, groß erst beim Antippen
  let exGross = false;
  const exZeile = () => { const x = lernExOben(d); if (!x) return lernExKarte(d); if (exGross) return lernExKarte(d);
    return el('div', { class: 'rk-ex-zeile' }, el('button', { type: 'button', class: 'rk-ex-mehr', 'aria-expanded': 'false', onclick: () => { exGross = true; lernErsetze(schwebe, ...(handy() ? geradeDran() : [])); zeichneSeite(); } },
      el('span', { 'aria-hidden': 'true' }, '⛯ '), x.zustand === 'begonnen' ? 'Expedition: ' : 'Expedition freigeschaltet: ', el('b', {}, x.titel)),
      el('a', { class: 'rk-ex-start', href: `#/expedition/${kind.id}-${x.id}` }, x.zustand === 'begonnen' ? `Teil ${lernExBuchstabe(lernExTeilK(x))} ›` : 'Starten ›')); };
  // RS 1: Anrede „Digga“ (einmal je Lerntag, gezählt mit der Abflugtafel) als Sticker auf der Ecke der Startkarte – einmal je Ansicht gezogen
  let anredeEl;
  const anredeHolen = () => { if (anredeEl === undefined && lernJwDaten) { anredeEl = lernJwStickerEl(lernJwAnrede(kind.id), 'anrede') || null; anredeEl?.classList.add('lr-jw-ecke'); } return anredeEl || null; };
  if (!lernJwDaten) lernJwLaden().then(() => { if (document.body.contains(wurzel) && anredeHolen()) { lernErsetze(schwebe, ...(handy() ? geradeDran() : [])); zeichneSeite(); } });
  // RS 2: „Mein Schuljahr“ auf Handy/Tablet als Zeile in der Startkarte, Antippen öffnet die Karte als Blatt von unten
  const sjZeile = () => { const k = lernSjKurz(d); if (!k) return null;
    return el('button', { type: 'button', class: 'rk-sj-zeile', 'aria-haspopup': 'dialog', 'aria-label': `Mein Schuljahr: ${k}`, onclick: (ev) => lernSjBlatt(d, ev.currentTarget, wurzel) },
      el('span', { class: 'rk-sj-ring', 'aria-hidden': 'true' }), el('span', {}, k), el('i', { 'aria-hidden': 'true' }, ' ›')); };
  const geradeDran = () => {
    const kompakt = handy(); const nb = (d.nachbessern || []).length;
    const ex = nb ? lernExChip(d) : exZeile(); // KJ §0: Nachbessern zuerst, Expedition dann nur als Chip
    const f = dranFlug; const st = dranStadt;
    const teil = f?.teil_von > 1 ? ` – Teil ${f.teil} von ${f.teil_von}` : '';
    const ss = stadtStand;
    const stand = ss ? el('div', { class: 'rk-dran-stand', role: 'img', 'aria-label': `${ss.x} von ${ss.y} Bordkarten in ${st.name}` }, el('b', {}, `${ss.x}/${ss.y}`),
      ss.y <= 12 ? el('span', { class: 'rk-striche' }, ...Array.from({ length: ss.y }, (_, i) => el('i', { class: i < ss.x ? 'g' : '' }))) : null) : null;
    const zeile = f ? el('div', { class: 'rk-dran' },
      f.iso ? el('img', { class: 'rk-dran-flagge', src: lernRkFlagge(f.iso), alt: '', loading: 'lazy' }) : null,
      el('div', { class: 'rk-dran-text' }, kompakt ? null : el('small', {}, 'GERADE DRAN'), el('b', {}, st?.name || f.land, st ? el('span', {}, ` in ${f.land}`) : null),
        kompakt ? null : el('span', { class: 'rk-dran-sub' }, start.testDran ? `Flug-Test · ${f.titel}${teil}` : `${f.titel}${teil}${st ? ` · Stadt ${st.nr} von ${(f.staedte || []).length}` : ''}`)),
      stand) : null;
    const text = st && !start.testDran && !start.wdh && !/Test/.test(start.text) ? `Weiter in ${st.name}` : start.text; // Name der Stadt aus der Karte (Reise-Aufbau)
    const knopf = !start.ziel ? el('p', { class: 'rk-start rk-start-zu' }, el('span', {}, el('b', {}, '🔒 ' + start.text), el('small', {}, 'Frag Mama oder Papa nach dem Plan'))) : el('a', { class: 'rk-start', href: start.ziel }, el('span', {}, el('b', {}, text + ' ›'), st && !start.testDran && !start.wdh ? el('small', {}, `Stadt ${st.nr} · ${st.titel || ''}`) : start.wdh ? el('small', {}, 'Zuerst ein paar Bordkarten von früher') : null));
    const anr = anredeHolen();
    const karteEl = el('div', { class: 'rk-schwebe-karte' + (kompakt ? ' kompakt' : '') + (anr ? ' lr-jw-ecke-traeger' : '') }, zeile, start.ansage ? el('p', { class: 'lr-dock-ansage rk-ansage' }, start.ansage) : null, knopf, kompakt ? sjZeile() : null, anr);
    return [nb ? lernNbKarte(d, { kompakt }) : null, ex, karteEl,
      lernZpKarte(d, { kompakt })]; // KJ §0.4: Zusatz · eingeplant unter „Gerade dran“
  };

  // ---------- Daten laden je Ebene ----------
  async function lade() {
    const name = z.ebene === 'welt' ? 'welt.json' : `kontinent-${z.kont}.json`;
    z.laedt = true; wurzel.classList.add('rk-laedt');
    try { z.daten = await lernKarteDatei(name); } catch { z.daten = null; }
    z.laedt = false; wurzel.classList.remove('rk-laedt');
  }
  // ---------- Ansicht (viewBox) ----------
  const groesse = () => { const r = rahmen.getBoundingClientRect(); return [Math.max(200, r.width), Math.max(200, r.height)]; };
  const unten = () => (handy() ? (schwebe.getBoundingClientRect().height || 150) + 16 : 0);
  function setzeVb(vb) { z.vb = vb; svg.setAttribute('viewBox', vb.map((v) => v.toFixed(1)).join(' ')); }
  function passeAn(box, rand = 0.12) {
    const [W, H] = groesse(); const u = unten(); const hNutz = Math.max(120, H - u);
    let [x0, y0, x1, y1] = box; const bw = Math.max(20, x1 - x0) * (1 + 2 * rand), bh = Math.max(20, y1 - y0) * (1 + 2 * rand);
    const k = Math.max(bw / W, bh / hNutz); const w = W * k, h = H * k; const cx = (x0 + x1) / 2, cy = (y0 + y1) / 2;
    setzeVb([cx - w / 2, cy - hNutz * k / 2, w, h]);
  }
  function passend() {
    const D = z.daten; if (!D) return;
    if (z.ebene === 'welt') {
      // S5: Handy startet als Ausschnitt um den aktuellen Kontinent
      const fl = handy() && dranFlug ? alleFluege.filter((f) => f.kontinent_id === dranFlug.kontinent_id && f.mitte) : [];
      if (fl.length) { const pts = fl.map((f) => lernKarteProj(D.proj, f.mitte.laenge, f.mitte.breite)); const xs = pts.map((p) => p[0]), ys = pts.map((p) => p[1]); // K2: die beiden nächsten Nachbarn mit ihrem Namen angeschnitten im Bild
        const mk = (id) => D.kontinente?.find((x) => x.id === id)?.mitte; const m0 = mk(dranFlug.kontinent_id);
        if (m0) for (const m1 of KONT.filter((kk) => kk.id !== dranFlug.kontinent_id).map((kk) => mk(kk.id)).filter(Boolean).sort((a, b) => Math.hypot(a[0] - m0[0], a[1] - m0[1]) - Math.hypot(b[0] - m0[0], b[1] - m0[1])).slice(0, 2)) { xs.push(m1[0]); ys.push(m1[1]); }
        passeAn([Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)], 0.12); z.startK = mass(); return; }
      passeAn([0, 20, D.w, D.h - 10], 0.02); z.startK = mass(); return; }
    if (z.ebene === 'land') { // S4: Einstieg = Rahmen um die Städte-Route (+ Rand), sonst das Land
      const f = flugVon(z.kont, z.land); const pts = (f?.staedte || []).map((c) => lernKarteProj(D.proj, c.laenge, c.breite));
      if (pts.length) { const xs = pts.map((p) => p[0]), ys = pts.map((p) => p[1]); passeAn([Math.min(...xs) - 10, Math.min(...ys) - 10, Math.max(...xs) + 70, Math.max(...ys) + 10], 0.18); return; }
      const g = D.gebiete.find((x) => x.id === z.land); if (g) { passeAn(g.b, 0.18); return; } }
    // Kontinent: auf die eigene Länder-Route (Pins der Flüge), sonst ganze Datei
    const pins = (D.gebiete || []).filter((g) => flugVon(z.kont, g.id)).map((g) => g.hs?.p || g.lp).filter(Boolean);
    if (pins.length) { const xs = pins.map((p) => p[0]), ys = pins.map((p) => p[1]); passeAn([Math.min(...xs), Math.min(...ys) - 40, Math.max(...xs), Math.max(...ys)], 0.12); }
    else passeAn([0, 0, D.w, D.h], 0);
  }
  const mass = () => { const [W] = groesse(); return z.vb ? z.vb[2] / W : 1; }; // Kartenmaß je Bildschirmpixel

  // ---------- Zeichnen ----------
  function zeichneLaender() {
    const D = z.daten; lernErsetze(ebenen.meer); lernErsetze(ebenen.land); lernErsetze(ebenen.kette); lernErsetze(ebenen.route);
    if (!D) { ebenen.meer.append(s('text', { x: 10, y: 30, class: 'rk-fehlt' }, 'Karte lädt nicht – bitte später noch einmal.')); return; }
    ebenen.meer.append(s('rect', { x: -5000, y: -5000, width: 12000, height: 12000, class: 'rk-meer' }));
    if (z.ebene === 'welt') {
      if (D.graticule) ebenen.meer.append(s('path', { d: D.graticule, class: 'rk-gitter' }));
      for (const g of D.gebiete) {
        const k = KONT.find((x) => x.id === g.k);
        const p = s('path', { d: g.d, class: 'rk-land rk-welt-k' + (g.k === 'ant' ? ' rk-ant' : k ? ` rk-k rk-k${(KONT.indexOf(k) % 8) + 1}` : ' rk-fremd') + (k && k.id === dranFlug?.kontinent_id ? ' rk-k-dran' : '') });
        if (k) { p.addEventListener('click', () => { if (gezogen) return; geheKontinent(k.id); }); p.setAttribute('data-k', String(k.id)); }
        if (g.k === 'ant') p.addEventListener('click', () => { if (!gezogen) route('stationen', String(kind.id)); });
        ebenen.land.append(p);
      }
      return;
    }
    for (const g of D.gebiete) {
      const f = flugVon(z.kont, g.id); const zst = lernRkZustand(f, nst);
      const eigen = g.k === z.kont;
      const cls = ['rk-land', f ? 'rk-z-' + zst : eigen ? 'rk-eigen' : 'rk-fremd'];
      if (z.ebene === 'land') cls.push(g.id === z.land ? 'rk-auf' : 'rk-gedaempft');
      if (z.sel === g.id) cls.push('rk-sel');
      const p = s('path', { d: g.d, class: cls.join(' '), 'data-id': g.id });
      p.addEventListener('click', () => { if (gezogen) return; waehle(g.id); });
      ebenen.land.append(p);
    }
    if (z.ebene === 'land') { const g = D.gebiete.find((x) => x.id === z.land); if (g) ebenen.land.append(s('path', { d: g.d, class: 'rk-umriss' })); }
  }
  // Länder-Route (§5): Bögen in der Reihenfolge des Plans; geflogen grün durchgezogen, kommt gelb gepunktet. Teile: feine graue Kette (§11).
  const reihe = (kontId) => {
    const fl = alleFluege.filter((f) => f.kontinent_id === kontId && !f.zusatz);
    const war = fl.filter((f) => ['gold', 'gesch', 'kann'].includes(lernRkZustand(f, nst))).sort((a, b) => String(a.stempel_am || '').localeCompare(String(b.stempel_am || '')));
    const dran = fl.filter((f) => lernRkZustand(f, nst) === 'dran');
    const plan = fl.filter((f) => ['plan', 'wartet'].includes(lernRkZustand(f, nst))).sort((a, b) => (Number(a.plan_platz) || 999) - (Number(b.plan_platz) || 999));
    return [...war, ...dran, ...plan];
  };
  const kopfPos = (g, k) => { const p = g.hs?.p || g.lp; return p ? [p[0], p[1] - 30 * k] : null; };
  const bogen = (a, b, k, cls) => { const mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2; const dx = b[0] - a[0], dy = b[1] - a[1]; const l = Math.hypot(dx, dy) || 1;
    return s('path', { d: `M${a[0]},${a[1]} Q${mx - dy / l * l * 0.18},${my + dx / l * l * 0.18} ${b[0]},${b[1]}`, class: cls, 'stroke-width': (2 * k).toFixed(2), ...(cls.includes('kommt') ? { 'stroke-dasharray': `${(1.5 * k).toFixed(2)} ${(6 * k).toFixed(2)}` } : {}) }); };
  function zeichneRouten() {
    lernErsetze(ebenen.route); lernErsetze(ebenen.kette); const D = z.daten; if (!D || z.ebene === 'welt') return; const k = mass();
    if (z.ebene === 'kontinent') {
      const gs = new Map(D.gebiete.map((g) => [g.id, g]));
      const r = reihe(z.kont).map((f) => ({ f, g: gs.get(lernRkSchl(f)) })).filter((x) => x.g);
      for (let i = 1; i < r.length; i++) { const a = kopfPos(r[i - 1].g, k), b = kopfPos(r[i].g, k); if (!a || !b) continue;
        const war = ['gold', 'gesch', 'kann', 'dran'].includes(lernRkZustand(r[i].f, nst)) && ['gold', 'gesch', 'kann'].includes(lernRkZustand(r[i - 1].f, nst));
        ebenen.route.append(bogen(a, b, k, 'rk-route ' + (war ? 'rk-war' : lernRkZustand(r[i].f, nst) === 'wartet' ? 'rk-kommt rk-grau-linie' : 'rk-kommt'))); } // RK-D: Route zu einem wartenden Land grau gepunktet
      // Teile eines Themas: Kette Pin zu Pin
      const stamm = new Map(); for (const f of alleFluege.filter((x) => x.kontinent_id === z.kont && Number(x.teil_von) > 1)) { const st = f.teil_stamm || f.thema_id; if (!stamm.has(st)) stamm.set(st, []); stamm.get(st).push(f); }
      for (const fs of stamm.values()) { const pts = fs.sort((a, b) => Number(a.teil) - Number(b.teil)).map((f) => gs.get(lernRkSchl(f))).filter(Boolean).map((g) => kopfPos(g, k)).filter(Boolean);
        for (let i = 1; i < pts.length; i++) { ebenen.kette.append(s('line', { x1: pts[i - 1][0], y1: pts[i - 1][1], x2: pts[i][0], y2: pts[i][1], class: 'rk-kettenlinie', 'stroke-width': (1 * k).toFixed(2), 'stroke-dasharray': `${(1 * k).toFixed(2)} ${(5 * k).toFixed(2)}` })); } }
    }
    if (z.ebene === 'land') {
      const f = flugVon(z.kont, z.land); if (!f) return;
      const st = (f.staedte || []).slice().sort((a, b) => Number(a.nr) - Number(b.nr)).map((c) => ({ c, p: lernKarteProj(D.proj, c.laenge, c.breite) }));
      const pf = st.filter((x) => x.c.pflicht !== false);
      for (let i = 1; i < pf.length; i++) { const war = ['gelandet', 'sicher'].includes(pf[i].c.stand) || (dranStadt && Number(pf[i].c.nr) <= Number(dranStadt.nr) && f === dranFlug);
        ebenen.route.append(bogen(pf[i - 1].p, pf[i].p, k, 'rk-route ' + (war ? 'rk-war' : f.gesperrt ? 'rk-kommt rk-grau-linie' : 'rk-kommt'))); }
      for (const x of st.filter((y) => y.c.pflicht === false)) { // Kür: grau gepunktet von der nächsten Pflicht-Stadt davor
        const vor = pf.filter((y) => Number(y.c.nr) < Number(x.c.nr)).pop() || pf[0]; if (vor) ebenen.route.append(bogen(vor.p, x.p, k, 'rk-route rk-kuer-linie rk-kommt')); }
    }
  }
  // Pins, Beschriftungen, Städte – gleich groß beim Zoomen (gegen den Zoom skaliert); Überdeckung: wichtigere zuerst, Berührendes weglassen (§6)
  function zeichneOben() {
    lernErsetze(ebenen.oben); const D = z.daten; if (!D || !z.vb) return; const k = mass(); const [W, H] = groesse();
    quelle.style.bottom = handy() ? `${Math.round(unten())}px` : ''; // K1: Quellen-Zeile unten links, auf dem Handy über der Schwebekarte
    zeichneRouten();
    const belegt = []; const frei = (b) => !belegt.some((x) => !(b[2] < x[0] || b[0] > x[2] || b[3] < x[1] || b[1] > x[3]));
    const bild = (p) => [(p[0] - z.vb[0]) / k, (p[1] - z.vb[1]) / k]; // Bildschirm-Pixel
    const imBild = (q) => q[0] > -60 && q[1] > -60 && q[0] < W + 60 && q[1] < H + 60;
    const gr = (p, ...kids) => s('g', { transform: `translate(${p[0].toFixed(1)},${p[1].toFixed(1)}) scale(${k.toFixed(4)})` }, ...kids);
    if (z.ebene === 'welt') {
      // S5: „x/y Länder“ erst ab einer Zoomstufe (Welt mindestens 900 px breit); Namen, die sich berühren, nach unten versetzen (Kontinent des Flugs zuerst)
      const nah = rechner() || (z.startK && k <= z.startK / 1.4);
      const reiheK = [...KONT.filter((kk) => kk.id === dranFlug?.kontinent_id), ...KONT.filter((kk) => kk.id !== dranFlug?.kontinent_id)];
      for (const kk of reiheK) { const m = D.kontinente?.find((x) => x.id === kk.id)?.mitte; if (!m) continue;
        const zus = Number(kk.zusatz_laender) || 0; const name = lernRkKurz(kk.reise).toUpperCase();
        const q = bild(m); const bw = Math.max(name.length * 11, 90) / 2; let dy = 0;
        for (let i = 0; i < 4; i++) { const b = [q[0] - bw, q[1] - 20 + dy, q[0] + bw, q[1] + (nah ? 32 : 16) + dy]; if (frei(b)) { belegt.push(b); break; } dy += 26; }
        const t = gr(m, s('text', { class: 'rk-kname', y: -6 + dy }, name), s('text', { class: 'rk-kzahl', y: 12 + dy }, `${kk.themengebiet || ''}`),
          nah ? s('text', { class: 'rk-kzahl', y: 27 + dy }, `${Number(kk.geschafft) || 0}/${Number(kk.laender) || 0} Länder${zus ? ` · +${zus} Zusatz` : ''}`) : null);
        t.classList.add('rk-klick'); t.addEventListener('click', () => { if (!gezogen) geheKontinent(kk.id); }); ebenen.oben.append(t); }
      // Antarktis: Expeditionen (EX §7) – Stationen nach Breite/Länge; geschafft blau ✓, frei grün mit Puls, gesperrt grau 🔒
      const stand = lernExGeschafftZahl(d), gesamt = lernExGesamt(d); const frei2 = (d.expeditionen || []).filter(lernExOffen).length;
      if (D.antarktis) { const t = gr(D.antarktis.mitte, s('text', { class: 'rk-kname rk-ant-name', y: -2 }, 'ANTARKTIS'), s('text', { class: 'rk-kzahl', y: 15 }, frei2 ? `⛯ ${frei2} ${frei2 === 1 ? 'Expedition' : 'Expeditionen'} freigeschaltet` : `Expeditionen · ${stand} von ${gesamt} Stationen`));
        t.classList.add('rk-klick'); t.addEventListener('click', () => { if (!gezogen) route('stationen', String(kind.id)); }); ebenen.oben.append(t); }
      for (const st of karte.antarktis?.stationen || []) { const x = (st.expeditionen || []).map((sc) => (d.expeditionen || []).find((e) => e.schluessel === sc)).find(Boolean);
        const zs = x?.zustand === 'geschafft' ? 'gesch' : lernExOffen(x) ? 'frei' : 'zu'; const p = lernKarteProj(D.proj, st.laenge, st.breite);
        const pin = gr(p, zs === 'frei' ? s('circle', { r: 9, class: 'rk-puls rk-puls-gruen' }) : null, s('circle', { r: 5.5, class: 'rk-station rk-station-' + zs }));
        pin.append(s('title', {}, `${st.name}${zs === 'gesch' ? ' – geschafft' : zs === 'frei' ? ' – freigeschaltet' : ' – gesperrt'}`)); pin.classList.add('rk-klick');
        pin.addEventListener('click', () => { if (!gezogen) route('stationen', String(kind.id)); }); ebenen.oben.append(pin); }
      // hier bist du
      if (dranStadt) ebenen.oben.append(gr(lernKarteProj(D.proj, dranStadt.laenge, dranStadt.breite), s('circle', { r: 10, class: 'rk-puls' }), s('circle', { r: 5, class: 'rk-hier' })));
      return;
    }
    // Kontinent und Land: Flaggen-Pins (Kopf = Flagge, Spitze = Hauptstadt bzw. Hauptort des Landesteils)
    // S2 (Prüfung RK-App 2, Abschnitt 2): Vorrang beim Beschriften, vier Lagen je Schild, kein Platz → Schild weglassen (Pin bleibt),
    // Hauptstadt-Zeile auf dem Handy nur für gerade dran, die nächsten 3 und das angetippte Land; Köpfe, die sich zu mehr als einem Drittel
    // überdecken, fächern bis 14 px schräg auseinander (die Nadelspitze bleibt an der Hauptstadt).
    const rb = rahmen.getBoundingClientRect(); // Kartenknöpfe, Legende und Quellen-Zeile sind für Schilder belegt
    for (const e0 of [zoomKnoepfe, quelle, legende.hidden ? null : legende]) { if (!e0) continue; const r0 = e0.getBoundingClientRect(); if (r0.width) belegt.push([r0.left - rb.left - 4, r0.top - rb.top - 4, r0.right - rb.left + 4, r0.bottom - rb.top + 4]); }
    const naechste3 = new Set(alleFluege.filter((f) => f.kontinent_id === z.kont && lernRkZustand(f, nst) === 'plan').sort((a, b) => (Number(a.plan_platz) || 999) - (Number(b.plan_platz) || 999)).slice(0, 3).map((f) => f.thema_id));
    const wiederOffenF = (f) => (f?.staedte || []).some((c) => c.stand === 'wieder_offen');
    const rang = (g, f) => { if (z.sel === g.id) return -1; if (!f) return 9; const zs = lernRkZustand(f, nst);
      if (zs === 'dran') return 0; if (naechste3.has(f.thema_id)) return 1; if (wiederOffenF(f)) return 2; if (['gesch', 'gold', 'kann'].includes(zs)) return 3;
      if (zs === 'plan' || zs === 'wartet') return 4; if (zs === 'zusatz') return 5; if (zs === 'offen') return 6; if (zs === 'gesperrt') return 7; return 8; };
    const liste = D.gebiete.filter((g) => g.hs).map((g) => { const f = flugVon(z.kont, g.id); return { g, f, rang: rang(g, f) }; })
      .sort((a, b) => a.rang - b.rang || (b.g.a || 0) - (a.g.a || 0));
    const pins = []; const koepfe = [];
    const ueber = (a, b) => Math.max(0, Math.min(a[2], b[2]) - Math.max(a[0], b[0])) * Math.max(0, Math.min(a[3], b[3]) - Math.max(a[1], b[1]));
    // Reihenfolge: erst Köpfe und Schilder der Länder mit Flug (nach Vorrang), dann Länder ohne Flug – nur wo noch Platz ist
    const kopfSetzen = (x) => { const { g, f } = x;
      if (z.ebene === 'land' && g.id !== z.land && !f) return null;
      const q = bild(g.hs.p); if (!imBild(q)) return null;
      const flaeche = (g.a || 0) / (k * k);
      if (!f && flaeche < (z.ebene === 'land' ? 2200 : 60)) return null;
      const r = f ? 13 : 9, h = f ? 30 : 22; const kb = (dx, dy) => [q[0] + dx - r - 1, q[1] - h + dy - r - 1, q[0] + dx + r + 1, q[1] - h + dy + r + 1];
      let off = [0, 0];
      if (f && !(z.ebene === 'land' && g.id === z.land)) { // Fächer: Kopf mit kleinerem Vorrang rückt bis 14 px schräg weg, wenn er mehr als ein Drittel überdeckt
        const zuViel = (b) => koepfe.some((o) => ueber(b, o) > (2 * r + 2) ** 2 / 3);
        if (zuViel(kb(0, 0))) { const kand = [[-10, -10], [10, -10], [-14, 0], [14, 0], [-10, 10], [10, 10], [0, -14]];
          let best = null, bestU = Infinity; for (const [dx, dy] of kand) { const b = kb(dx, dy); const u = koepfe.reduce((s0, o) => s0 + ueber(b, o), 0); if (u < bestU) { bestU = u; best = [dx, dy]; } if (!u) break; }
          off = best; } }
      const kopf = kb(off[0], off[1]);
      if (!f && !frei(kopf)) return null;
      koepfe.push(kopf); belegt.push(kopf);
      const p0 = { g, f, q, off, r, h, rang: x.rang, schild: f || flaeche >= 2200 }; pins.push(p0); return p0; };
    // Schilder: vier Lagen (rechts, links, oben, unten); frei = kein Schild, kein Kopf, kein Knopf darunter; kein Platz → weglassen
    const hsZeile = (x) => !!x.f && lernRkZustand(x.f, nst) !== 'gesperrt' && (!handy() || x.rang <= 1 || z.sel === x.g.id);
    const schildSetzen = (x) => { if (!x.schild || (z.ebene === 'land' && x.g.id === z.land)) return;
      const name = String(x.g.n || '').toUpperCase(); const mitHs = hsZeile(x) && !!x.g.hs.n;
      const w = Math.max(name.length * (x.f ? 8.2 : 7.2), mitHs ? String(x.g.hs.n).length * 6.4 : 0) + 6; const hh = mitHs ? 27 : 14;
      const cx = x.q[0] + x.off[0], cy = x.q[1] - x.h + x.off[1];
      const lagen = [{ a: 'start', x: x.r + 4, y: -1, b: [cx + x.r + 3, cy - 11, cx + x.r + 3 + w, cy - 11 + hh] },
        { a: 'end', x: -x.r - 4, y: -1, b: [cx - x.r - 3 - w, cy - 11, cx - x.r - 3, cy - 11 + hh] },
        { a: 'middle', x: 0, y: -x.r - 5 - (mitHs ? 13 : 0), b: [cx - w / 2, cy - x.r - 16 - (mitHs ? 13 : 0), cx + w / 2, cy - x.r - 2] },
        { a: 'middle', x: 0, y: x.h - x.off[1] + 13, b: [cx - w / 2, x.q[1] + 3, cx + w / 2, x.q[1] + 3 + hh] }];
      const l = lagen.find((y) => frei(y.b));
      if (l) { belegt.push(l.b); x.label = { a: l.a, x: l.x, y: l.y, hs: mitHs }; }
      else if (x.f && (x.rang <= 1 || z.sel === x.g.id)) { x.label = { ...lagen[0], hs: false }; } }; // gerade dran / nächste 3 / angetippt: immer beschriftet
    const mitF = liste.filter((x) => x.f).map(kopfSetzen).filter(Boolean);
    for (const x of mitF) schildSetzen(x);
    for (const x of liste.filter((y) => !y.f)) { const p0 = kopfSetzen(x); if (p0) schildSetzen(p0); }
    for (const x of pins.slice().reverse()) {
      if (z.ebene === 'land' && x.g.id === z.land) { // K3: Hauptstadt in der Land-Ebene nur als ◉ (überdeckt die erste Haltestelle nicht)
        ebenen.oben.append(gr(x.g.hs.p, s('circle', { r: 5, class: 'rk-hs-ring' }), s('circle', { r: 2, class: 'rk-hs-punkt' }), s('text', { class: 'rk-phs', x: 8, y: 16 }, x.g.hs.n))); continue; }
      ebenen.oben.append(lernRkPin(x, k, gr)); }
    // Land-Ebene: Städte der Reise als Haltestellen (§2/§4)
    if (z.ebene === 'land') {
      const f = flugVon(z.kont, z.land);
      // S4: Namen nach Vorrang – „hier bist du“, die nächsten drei, die gelandeten, dann der Rest; berührt ein Name etwas, wird er versetzt
      // (rechts, links, oben, unten), erst wenn nichts passt, bleibt nur die Nummer. Haltestellen selbst belegen ihren Platz zuerst.
      const stl = f ? (f.staedte || []).slice().sort((a, b) => Number(a.nr) - Number(b.nr)) : [];
      const hierC = stl.find((c) => dranStadt && f === dranFlug && Number(c.nr) === Number(dranStadt.nr)) || null;
      const naechste = hierC ? stl.filter((c) => Number(c.nr) > Number(hierC.nr)).slice(0, 3) : stl.filter((c) => !['gelandet', 'sicher'].includes(c.stand)).slice(0, 3);
      const vorrang = [...new Set([hierC, ...stl.filter((c) => c.stand === 'wieder_offen'), ...naechste, ...stl.filter((c) => ['gelandet', 'sicher'].includes(c.stand)), ...stl].filter(Boolean))];
      const qpos = new Map(stl.map((c) => [c, bild(lernKarteProj(D.proj, c.laenge, c.breite))]));
      // S1 (Prüfung RK-App 2): Haltestellen-Kästchen entzerren – nach Vorrang setzen; überdeckt eines ein schon gesetztes, rückt es bis 16 px weg
      // (erst wenn das nicht reicht, bis 24 px) und bekommt eine feine Linie zum echten Ort (der Punkt bleibt am Ort).
      const groesseC = (c) => (c === hierC ? 15 : 11.5) + (c.stand === 'wieder_offen' && c !== hierC ? 4 : 0);
      const kaesten = []; const versatz = new Map();
      const richt = Array.from({ length: 12 }, (_, i0) => [Math.cos(i0 * Math.PI / 6), Math.sin(i0 * Math.PI / 6)]);
      for (const c of vorrang) { const q = qpos.get(c); const g0 = groesseC(c) + 1; const kb = (dx, dy) => [q[0] + dx - g0, q[1] + dy - g0, q[0] + dx + g0, q[1] + dy + g0];
        const frei0 = (b) => !kaesten.some((o) => !(b[2] <= o[0] || b[0] >= o[2] || b[3] <= o[1] || b[1] >= o[3]));
        let off = [0, 0];
        if (!frei0(kb(0, 0))) { let gef = null;
          for (const rr of [6, 10, 13, 16, 20, 24]) { for (const [ux, uy] of richt) { const o = [Math.round(ux * rr), Math.round(uy * rr)]; if (frei0(kb(...o))) { gef = o; break; } } if (gef) break; }
          off = gef || [0, 0]; }
        versatz.set(c, off); kaesten.push(kb(...off)); }
      for (const b of kaesten) belegt.push(b);
      const namen = new Map(); // Stadt → { x, y, anker }
      const ssH = stadtStand && hierC ? ` · ${stadtStand.x}/${stadtStand.y}` : '';
      for (const c of vorrang) { const q0 = qpos.get(c); const ov = versatz.get(c); const q = [q0[0] + ov[0], q0[1] + ov[1]]; const gross = groesseC(c);
        const txt = c === hierC ? `${c.name}${ssH}` : c.pflicht === false ? `${c.name} · Kür` : c.name; const w = txt.length * 8.4 + 4; const zweite = c.stand === 'wieder_offen';
        const hh = zweite ? 30 : 18;
        const lagen = [[gross + 5, 5, 'start'], [-gross - 5, 5, 'end'], [0, -gross - 8, 'middle'], [0, gross + 17, 'middle'],
          [gross + 3, -gross - 4, 'start'], [-gross - 3, -gross - 4, 'end'], [gross + 3, gross + 14, 'start'], [-gross - 3, gross + 14, 'end'],
          [0, -gross - 26, 'middle'], [0, gross + 35, 'middle'], [gross + 5, 23, 'start'], [-gross - 5, 23, 'end'], [gross + 5, -13, 'start'], [-gross - 5, -13, 'end']];
        for (const [dx, dy, a] of lagen) { const x0 = a === 'start' ? q[0] + dx : a === 'end' ? q[0] + dx - w : q[0] - w / 2; const y0 = q[1] + dy - 13;
          const b = [x0, y0, x0 + w, y0 + hh]; if (frei(b)) { belegt.push(b); namen.set(c, { x: dx, y: dy, a }); break; } } }
      const grau = !!f?.gesperrt; // RK-D: Land-Ebene eines gesperrten Flugs grau, keine Schlösser an den Städten
      if (f) for (const c of [...vorrang].reverse()) { // Vorrang zuletzt gezeichnet = obenauf („hier“, „wieder offen“)
        const p = lernKarteProj(D.proj, c.laenge, c.breite); const hier = c === hierC; const ov = versatz.get(c);
        const kuer = c.pflicht === false;
        const zst = f.golden ? 'gold' : hier ? 'hier' : c.abgelegt ? 'abgelegt' : grau && (c.stand || 'offen') === 'offen' ? 'grau' : c.stand || 'offen';
        // M1: „wieder offen“ ist nicht gelandet – orange Haltestelle mit ↻, kein ✓, gestrichelter Ring, Unterzeile „wieder offen“; abgelegt: kleines goldenes ★
        const zeichen = zst === 'gold' || zst === 'abgelegt' ? '★' : ['gelandet', 'sicher'].includes(zst) ? '✓' : zst === 'wieder_offen' ? '↻' : String(c.nr);
        const gross = hier ? 15 : 11.5; const nm = namen.get(c);
        const kasten = s('g', { class: 'rk-st-kasten', transform: `translate(${ov[0]},${ov[1]})` }, hier ? s('circle', { r: 22, class: 'rk-puls', 'pointer-events': 'none' }) : null,
          zst === 'wieder_offen' ? s('rect', { x: -gross - 4, y: -gross - 4, width: gross * 2 + 8, height: gross * 2 + 8, rx: 8, class: 'rk-st-ring' }) : null,
          s('rect', { x: -gross, y: -gross, width: gross * 2, height: gross * 2, rx: 5, class: `rk-stadt rk-st-${zst}${kuer ? ' rk-st-kuer' : ''}` }),
          s('text', { class: 'rk-st-zahl' + (hier ? ' gross' : ''), y: 1 }, zeichen),
          nm ? s('text', { class: 'rk-st-name' + (kuer || zst === 'grau' ? ' leise' : ''), x: nm.x, y: nm.y, 'text-anchor': nm.a }, hier ? `${c.name}${ssH}` : kuer ? `${c.name} · Kür` : c.name) : null,
          nm && zst === 'wieder_offen' ? s('text', { class: 'rk-st-unter', x: nm.x, y: nm.y + 14, 'text-anchor': nm.a }, 'wieder offen') : null);
        const grp = gr(p, ov[0] || ov[1] ? s('line', { x1: 0, y1: 0, x2: ov[0], y2: ov[1], class: 'rk-st-linie' }) : null, ov[0] || ov[1] ? s('circle', { r: 2.2, class: 'rk-st-ort' }) : null, kasten);
        grp.classList.add('rk-st-g'); grp.setAttribute('data-nr', String(c.nr));
        grp.append(s('title', {}, `Stadt ${c.nr}: ${c.name} – ${c.titel || ''} (${hier ? 'hier bist du' : kuer ? 'Kür' : c.abgelegt ? LERN_RK_STADT.abgelegt : LERN_RK_STADT[c.stand] || c.stand || ''})`));
        ebenen.oben.append(grp); }
      // Teil geht weiter (§11)
      const nx = f && Number(f.teil_von) > 1 ? alleFluege.find((y) => (y.teil_stamm || y.thema_id) === (f.teil_stamm || f.thema_id) && Number(y.teil) === Number(f.teil) + 1) : null;
      lernErsetze(hinweis, f?.gesperrt ? el('p', { class: 'rk-grund rk-grund-karte' }, '🔒 ' + grundVon(f)) : null,
        nx ? el('button', { type: 'button', class: 'rk-weiter-hinweis', onclick: () => { z.kont = nx.kontinent_id; geheLand(lernRkSchl(nx)); } }, `Teil ${nx.teil} geht weiter in ${nx.land} ›`) : null);
    } else lernErsetze(hinweis);
  }
  const hinweis = el('div', { class: 'rk-hinweis' }); kartenTeil.append(hinweis);
  function lernRkPin({ g, f, label, off = [0, 0] }, k, gr) {
    const zst = lernRkZustand(f, nst); const iso = g.iso;
    const marke = zst === 'gold' ? '★' : zst === 'gesch' ? '✓' : zst === 'kann' ? '◉' : (zst === 'plan' || zst === 'wartet') && f.plan_platz ? String(f.plan_platz) : zst === 'zusatz' ? '+' : zst === 'dran' ? '✈' : null;
    const r = f ? 13 : 9; const h = f ? 30 : 22;
    const wiederOffen = f && (f.staedte || []).some((c) => c.stand === 'wieder_offen');
    const teil = f && Number(f.teil_von) > 1;
    // Kopf (bei Fächer versetzt) – Schild, Abzeichen und Trefferfläche wandern mit, die Spitze bleibt an der Hauptstadt
    const kopfKids = [
      s('circle', { cy: 4, r: 22, class: 'rk-treffer' }), // K1: feste Trefferfläche (≥ 44 px), unabhängig vom Puls
      s('path', { d: `M${-off[0]},${h - off[1]} L${-r * 0.42},${r * 0.6} A${r},${r} 0 1 1 ${r * 0.42},${r * 0.6} Z`, class: 'rk-nadel rk-n-' + (f ? zst : 'ohne') }),
      iso ? s('image', { href: lernRkFlagge(iso), x: -r + 2, y: -r + 2, width: (r - 2) * 2, height: (r - 2) * 2, 'clip-path': 'url(#rk-kreis)', preserveAspectRatio: 'xMidYMid slice', class: f && zst !== 'gesperrt' ? '' : 'rk-blass' }) : null,
      s('circle', { r: r - 2, class: 'rk-kopfring' }),
      marke ? s('g', { transform: `translate(${r * 0.8},${-r * 0.8})` }, s('circle', { r: 7.5, class: 'rk-marke rk-m-' + zst }), s('text', { class: 'rk-marke-t', y: 0.5 }, marke)) : null,
      // RK-D: im Plan und gesperrt → kleines 🔒 unten links am Kopf (gegenüber der Nummer; mit Teil-Abzeichen oben links)
      zst === 'wartet' ? s('g', { class: 'rk-schloss', transform: `translate(${-r * 0.85},${teil ? -r * 0.85 : r * 0.8})` }, s('circle', { r: 7.5, class: 'rk-marke rk-m-schloss' }), s('text', { class: 'rk-marke-t rk-schloss-t', y: 0.5 }, '🔒')) : null,
      wiederOffen ? s('g', { transform: `translate(${r * 0.8},${r * 0.8})` }, s('circle', { r: 7, class: 'rk-marke rk-m-wieder' }), s('text', { class: 'rk-marke-t', y: 0.5 }, '↻')) : null,
      teil ? s('g', { transform: `translate(${-r * 0.9},${r * 0.75})` }, s('rect', { x: -10, y: -7, width: 20, height: 14, rx: 7, class: 'rk-teil' }), s('text', { class: 'rk-teil-t', y: 0.5 }, `${f.teil}/${f.teil_von}`)) : null,
      label ? s('text', { class: 'rk-pland' + (f ? '' : ' k') + (zst === 'gesperrt' ? ' grau' : ''), x: label.x, y: label.y, 'text-anchor': label.a }, String(g.n || '').toUpperCase()) : null,
      label?.hs && g.hs.n ? s('text', { class: 'rk-phs', x: label.x, y: label.y + 12, 'text-anchor': label.a }, g.hs.n) : null];
    const kopfG = s('g', { class: 'rk-kopf-g', transform: `translate(${off[0]},${-h + off[1]})` }, ...kopfKids);
    const pin = gr(g.hs.p, off[0] || off[1] ? s('line', { x1: 0, y1: 0, x2: off[0], y2: -h + off[1] + r, class: 'rk-faecher' }) : null, kopfG, s('circle', { r: 2.2, class: 'rk-spitze' }));
    pin.classList.add('rk-pin'); if (f) pin.classList.add('rk-pin-flug'); if (zst === 'gesperrt') pin.classList.add('rk-pin-gesperrt'); if (zst === 'wartet') pin.classList.add('rk-pin-wartet');
    // K1: der Puls liegt als eigene Ebene unter dem Pin (ohne Treffer) – der Pin selbst bewegt sich nicht, die Trefferfläche bleibt fest
    if (zst === 'dran') { const pu = gr(g.hs.p, s('circle', { r: 9, class: 'rk-puls', 'pointer-events': 'none' })); pu.classList.add('rk-puls-ebene'); ebenen.oben.append(pu); }
    const grund = f?.gesperrt ? grundVon(f) : null;
    const wort = `${g.n}, ${g.region ? 'Hauptort' : 'Hauptstadt'} ${g.hs.n}${f ? ', ' + (zst === 'wartet' || zst === 'gesperrt' ? (f.gesperrt_grund === 'klasse' && f.ab_klasse ? `ab Klasse ${f.ab_klasse}` : `wartet – ${String(grund || '').replace(/^Erst/, 'erst')}`) + (zst === 'wartet' && f.plan_platz ? `, Platz ${f.plan_platz} im Plan` : '') : (LERN_RK_WORT[zst] || '')) : ''}${wiederOffen ? ', ↻ wieder offen – nachbessern' : ''}`;
    pin.setAttribute('role', 'button'); pin.setAttribute('tabindex', '0'); pin.setAttribute('aria-label', wort); pin.setAttribute('data-id', g.id);
    pin.addEventListener('click', (ev) => { ev.stopPropagation(); if (!gezogen) waehle(g.id); });
    pin.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); waehle(g.id); } });
    return pin;
  }

  // ---------- Blatt (§7) und Pfad-Zeile ----------
  function waehle(id) {
    z.sel = id; zeichneLaender(); zeichneOben(); zeigeBlatt();
  }
  function springeZu(y) { const id = lernRkSchl(y); if (z.ebene === 'kontinent' && z.kont === y.kontinent_id) { waehle(id); return; } z.kont = y.kontinent_id; geheKontinent(y.kontinent_id, id); }
  function zeigeBlatt() {
    const D = z.daten; const g = D?.gebiete?.find((x) => x.id === z.sel); if (!g) { blatt.hidden = true; lernErsetze(blatt); zeichneSeite(); return; }
    const f = flugVon(z.kont, g.id); const zst = lernRkZustand(f, nst); const kont = KONT.find((x) => x.id === z.kont);
    const teile = f && Number(f.teil_von) > 1 ? alleFluege.filter((y) => (y.teil_stamm || y.thema_id) === (f.teil_stamm || f.thema_id)).sort((a, b) => Number(a.teil) - Number(b.teil)) : [];
    const vorTeil = teile.find((y) => Number(y.teil) === Number(f?.teil) - 1);
    const inhalt = [
      el('button', { type: 'button', class: 'rk-x', 'aria-label': 'Schließen', onclick: () => { z.sel = null; blatt.hidden = true; zeichneLaender(); zeichneOben(); zeichneSeite(); } }, '✕'),
      el('p', { class: 'rk-cap' }, g.region ? 'LANDESTEIL' : 'LAND'),
      el('h3', { class: 'rk-bname' }, g.iso ? el('img', { class: 'rk-plakette', src: lernRkFlagge(g.iso), alt: '' }) : null, g.n),
      el('p', { class: 'rk-sub' }, `◉ ${g.region ? 'Hauptort' : 'Hauptstadt'}: ${g.hs?.n || '–'}${kont ? ` · Kontinent ${lernRkKurz(kont.reise)}` : ''}`),
      f ? el('p', { class: 'rk-flug' }, el('b', {}, `✈ ${f.titel}${Number(f.teil_von) > 1 ? ` – Teil ${f.teil} von ${f.teil_von}` : ''}`), ` · ${(f.staedte || []).length} Städte`) : el('p', { class: 'rk-sub' }, 'Hier gibt es (noch) keinen Mathe-Flug.'),
      f?.untertitel ? el('p', { class: 'rk-sub' }, f.untertitel) : null,
      f ? el('p', { class: 'rk-zustand rk-zw-' + zst }, (zst === 'plan' || zst === 'wartet') && f.plan_platz ? `Im Plan · Platz ${f.plan_platz}` : zst === 'gold' ? 'Alle Städte sind abgelegt. Hier musst du nichts mehr wiederholen.' : LERN_RK_WORT[zst]) : null,
      // RK-D: Grund der Sperre mit 🔒 vorne; bei fehlendem Visum ein Knopf zum (ersten) Land, das zuerst geschafft werden muss
      f?.gesperrt ? el('p', { class: 'rk-grund' }, '🔒 ' + grundVon(f)) : null,
      f?.gesperrt && f.gesperrt_grund !== 'klasse' ? (() => { const l = visumLaender(f).find((x) => x.flug); return l ? el('button', { type: 'button', class: 'rk-grund-knopf', onclick: () => springeZu(l.flug) }, `Zu ${l.name} ›`) : null; })() : null,
      // §11 Zusatz (Wortlaut der Vorgabe)
      f && zst === 'zusatz' ? el('p', { class: 'rk-sub' }, el('b', {}, 'Zusatz für Entdecker'), ' – muss nicht sein.') /* S7: ohne „freiwillig“ */ : null,
      teile.length ? el('p', { class: 'rk-teile' }, ...teile.flatMap((y, i) => [i ? ' · ' : null, el('button', { type: 'button', class: 'rk-teil-link', onclick: () => { z.kont = y.kontinent_id; z.sel = lernRkSchl(y); if (z.ebene === 'land') geheLand(lernRkSchl(y)); else geheKontinent(y.kontinent_id, lernRkSchl(y)); } },
        `Teil ${y.teil}: `, el('img', { class: 'rk-mini-flagge', src: lernRkFlagge(y.iso), alt: '' }), ` ${y.land}${y === f ? ' (hier)' : ['gesch', 'gold', 'kann'].includes(lernRkZustand(y, nst)) ? ' ✓' : ''}`)])) : null,
      vorTeil && !['gesch', 'gold', 'kann'].includes(lernRkZustand(vorTeil, nst)) && zst !== 'dran' ? el('p', { class: 'rk-sub' }, `Erst Teil ${vorTeil.teil} in ${vorTeil.land}`) : null,
      f && z.ebene !== 'land' && zst !== 'gesperrt' ? el('button', { type: 'button', class: 'rk-staedte-knopf', onclick: () => geheLand(g.id) }, `Städte in ${g.n} ansehen ›`) : null];
    if (rechner()) { blatt.hidden = true; lernErsetze(blatt); zeichneSeite(inhalt); }
    else { blatt.hidden = false; lernErsetze(blatt, ...inhalt); }
  }
  function zeichnePfad() {
    const kont = KONT.find((x) => x.id === z.kont); const D = z.daten; const g = z.ebene === 'land' ? D?.gebiete?.find((x) => x.id === z.land) : null;
    const mich = (bed) => (bed ? el('span', { class: 'rk-mich', 'aria-label': 'hier bist du' }, ' 📍') : null);
    const teil = (cap, text, aktiv, onclick, extra = null, ich = false) => el('button', { type: 'button', class: 'rk-pfad-teil' + (aktiv ? ' an' : ''), 'aria-current': aktiv ? 'page' : null, onclick }, el('small', {}, cap), el('span', {}, extra, el('span', { class: 'rk-pt-text' }, text), mich(ich)));
    const landTeil = g ? teil(g.region ? 'LANDESTEIL' : 'LAND', g.n, true, () => {}, g.iso ? el('img', { class: 'rk-mini-flagge', src: lernRkFlagge(g.iso), alt: '' }) : null, dranFlug && lernRkSchl(dranFlug) === g.id) : null;
    // M1: auf dem Handy kürzt der Pfad von links – Land-Ebene „… › 🇮🇹 Italien 📍“ („…“ führt zum Kontinent); die aktuelle Stufe steht immer ganz
    if (g && kont && schmal()) { lernErsetze(pfad, el('button', { type: 'button', class: 'rk-pfad-teil rk-pfad-kurz', 'aria-label': `Zurück zu ${lernRkKurz(kont.reise)}`, onclick: () => geheKontinent(kont.id) }, el('span', {}, '…')), el('i', { 'aria-hidden': 'true' }, '›'), landTeil); return; }
    lernErsetze(pfad, teil('WELT', 'Welt', z.ebene === 'welt', () => geheWelt(), '🌍 '),
      kont && z.ebene !== 'welt' ? [el('i', { 'aria-hidden': 'true' }, '›'), teil('KONTINENT', lernRkKurz(kont.reise), z.ebene === 'kontinent', () => geheKontinent(kont.id), null, kont.id === dranFlug?.kontinent_id)] : null,
      landTeil ? [el('i', { 'aria-hidden': 'true' }, '›'), landTeil] : null);
  }
  // Rechner: rechte Spalte – Gerade dran + Startknopf, angetipptes Land, „Meine Route · Länder“ bzw. „Städte in …“
  function zeichneSeite(blattInhalt = null) {
    if (!rechner()) { lernErsetze(seite); return; }
    const teile = [el('section', { class: 'rk-seite-karte' }, ...geradeDran()), lernSjKarte(d)]; // KJ §0.5: Mein Schuljahr in der rechten Spalte
    if (blattInhalt) teile.push(el('section', { class: 'rk-seite-karte rk-seite-blatt' }, ...blattInhalt));
    if (z.ebene === 'kontinent') { const r = reihe(z.kont);
      if (r.length) teile.push(el('section', { class: 'rk-seite-karte' }, el('h4', {}, 'MEINE ROUTE · LÄNDER'), ...r.map((f, i) => el('button', { type: 'button', class: 'rk-lzeile', onclick: () => waehle(lernRkSchl(f)) },
        el('span', { class: 'rk-nr rk-zn-' + lernRkZustand(f, nst) }, String(i + 1)), el('img', { class: 'rk-mini-flagge', src: lernRkFlagge(f.iso), alt: '' }), el('span', {}, el('b', {}, f.land), ` · ${f.titel}${Number(f.teil_von) > 1 ? ` · Teil ${f.teil} von ${f.teil_von}` : ''}`, f.gesperrt ? el('small', {}, ' 🔒 wartet') : null))))); }
    if (z.ebene === 'land') { const f = flugVon(z.kont, z.land);
      if (f) teile.push(el('section', { class: 'rk-seite-karte' }, el('h4', {}, `STÄDTE IN ${String(f.land).toUpperCase()}`), ...(f.staedte || []).slice().sort((a, b) => Number(a.nr) - Number(b.nr)).map((c) => el('div', { class: 'rk-lzeile' },
        el('span', { class: 'rk-nr rk-zs-' + (c.abgelegt ? 'abgelegt' : f.gesperrt && (c.stand || 'offen') === 'offen' ? 'grau' : c.stand || 'offen') + (c.pflicht === false ? ' kuer' : '') }, c.abgelegt ? '★' : String(c.nr)), el('span', {}, el('b', {}, c.name), ` · ${c.titel || ''}${c.pflicht === false ? ' · Kür' : ''}`, el('small', {}, ` ${c.abgelegt ? LERN_RK_STADT.abgelegt : LERN_RK_STADT[c.stand] || ''}`)))))); }
    lernErsetze(seite, ...teile);
  }
  // ---------- Ebenen wechseln (weich, ≤ 0,5 s) ----------
  async function geheWelt() { z.ebene = 'welt'; z.land = null; z.sel = null; await neu(); }
  async function geheKontinent(id, sel = null) { z.ebene = 'kontinent'; z.kont = id; z.land = null; z.sel = sel; await neu(); if (sel) zeigeBlatt(); }
  async function geheLand(id) { const war = z.daten && z.ebene !== 'welt' && z.daten.id === z.kont; z.ebene = 'land'; z.land = id; z.sel = null; blatt.hidden = true; lernErsetze(blatt); // S6: Blatt zu
    if (war) { zeichneLaender(); weich(); zeichnePfad(); zeichneSeite(); } else await neu(); }
  async function neu() {
    blatt.hidden = true; await lade(); if (!document.body.contains(wurzel)) return;
    quelle.textContent = 'Karte: Natural Earth · Orte: GeoNames (CC BY 4.0)' + (z.ebene === 'welt' ? ' · Stationen: COMNAP (Bildung, nicht kommerziell)' : '');
    zeichneLaender(); passend(); zeichneOben(); zeichnePfad(); zeichneSeite(); lernErsetze(schwebe, ...(handy() ? geradeDran() : []));
  }
  function weich() {
    const von = z.vb ? z.vb.slice() : null; passend(); const nach = z.vb.slice();
    if (!von || lernWenigBewegung()) { zeichneOben(); return; }
    const t0 = performance.now(); const lauf = (t) => { const p = Math.min(1, (t - t0) / 450); const e = 1 - Math.pow(1 - p, 3);
      setzeVb(von.map((v, i) => v + (nach[i] - v) * e)); if (p < 1) requestAnimationFrame(lauf); else zeichneOben(); };
    requestAnimationFrame(lauf);
  }
  // ---------- Verschieben (Finger/Maus), Zoomen (zwei Finger, Mausrad, + / −) ----------
  let gezogen = false; const zeiger = new Map(); let start0 = null; let neuZeichnen = 0;
  const spaeterOben = () => { cancelAnimationFrame(neuZeichnen); neuZeichnen = requestAnimationFrame(zeichneOben); };
  const zuKarte = (cx, cy) => { const r = rahmen.getBoundingClientRect(); const k = mass(); return [z.vb[0] + (cx - r.left) * k, z.vb[1] + (cy - r.top) * k]; };
  function zoomUm(f, cx, cy) { if (!z.vb) return; const r = rahmen.getBoundingClientRect(); const px = cx ?? r.left + r.width / 2, py = cy ?? r.top + r.height / 2;
    const [mx, my] = zuKarte(px, py); const w = Math.max(20, Math.min(z.ebene === 'welt' ? 1200 : 4000, z.vb[2] * f)); const k2 = w / z.vb[2];
    setzeVb([mx - (mx - z.vb[0]) * k2, my - (my - z.vb[1]) * k2, w, z.vb[3] * k2]); spaeterOben(); }
  rahmen.addEventListener('wheel', (ev) => { ev.preventDefault(); zoomUm(ev.deltaY > 0 ? 1.15 : 1 / 1.15, ev.clientX, ev.clientY); }, { passive: false });
  rahmen.addEventListener('pointerdown', (ev) => { zeiger.set(ev.pointerId, [ev.clientX, ev.clientY]); gezogen = false;
    start0 = { vb: z.vb?.slice(), pts: new Map(zeiger), moved: 0 }; });
  rahmen.addEventListener('pointermove', (ev) => {
    if (!zeiger.has(ev.pointerId) || !start0?.vb) return; zeiger.set(ev.pointerId, [ev.clientX, ev.clientY]);
    const k = start0.vb[2] / groesse()[0];
    if (zeiger.size === 1) { const a = start0.pts.get(ev.pointerId); if (!a) return; const dx = ev.clientX - a[0], dy = ev.clientY - a[1];
      if (Math.hypot(dx, dy) > 6) { gezogen = true; if (!rahmen.hasPointerCapture?.(ev.pointerId)) try { rahmen.setPointerCapture(ev.pointerId); } catch { /* egal */ } }
      if (gezogen) { setzeVb([start0.vb[0] - dx * k, start0.vb[1] - dy * k, start0.vb[2], start0.vb[3]]); spaeterOben(); } }
    else if (zeiger.size === 2) { const [p1, p2] = [...zeiger.values()]; const [q1, q2] = [...start0.pts.values()]; if (!q1 || !q2) return;
      const d0 = Math.hypot(q1[0] - q2[0], q1[1] - q2[1]) || 1, d1 = Math.hypot(p1[0] - p2[0], p1[1] - p2[1]) || 1; gezogen = true;
      const f = d0 / d1; const r = rahmen.getBoundingClientRect(); const mx0 = (q1[0] + q2[0]) / 2 - r.left, my0 = (q1[1] + q2[1]) / 2 - r.top; const mx1 = (p1[0] + p2[0]) / 2 - r.left, my1 = (p1[1] + p2[1]) / 2 - r.top;
      const ax = start0.vb[0] + mx0 * k, ay = start0.vb[1] + my0 * k; const w = Math.max(20, start0.vb[2] * f); const k2 = w / groesse()[0];
      setzeVb([ax - mx1 * k2, ay - my1 * k2, w, start0.vb[3] * f]); spaeterOben(); } });
  const los = (ev) => { zeiger.delete(ev.pointerId); if (zeiger.size === 0) { start0 = null; setTimeout(() => { gezogen = false; }, 0); } else start0 = { vb: z.vb?.slice(), pts: new Map(zeiger) }; };
  rahmen.addEventListener('pointerup', los); rahmen.addEventListener('pointercancel', los);
  // Größe: Rechner/Handy umschalten, Ansicht anpassen
  // Karte bis zum unteren Fensterrand (Rechner), auf dem Handy bleibt unten Platz für die Menüzeile
  const hoeheSetzen = () => { const top = kartenTeil.getBoundingClientRect().top + scrollY; const h = Math.max(420, innerHeight - top - (handy() ? 12 : 16));
    kartenTeil.style.height = h + 'px'; if (rechner()) seite.style.maxHeight = h + 'px'; };
  const beiGroesse = () => { if (!document.body.contains(wurzel)) { removeEventListener('resize', beiGroesse); return; } hoeheSetzen(); wurzel.classList.toggle('rk-handy', handy()); wurzel.classList.toggle('rk-rechner', rechner());
    lernErsetze(schwebe, ...(handy() ? geradeDran() : [])); zeichneSeite(); zeichnePfad(); if (z.vb) { passend(); zeichneOben(); } };
  addEventListener('resize', beiGroesse);
  kartenTeil.append(schwebe, blatt);
  // erster Aufbau, sobald die Karte im Dokument ist (Größe bekannt)
  requestAnimationFrame(() => { hoeheSetzen(); lernErsetze(schwebe, ...(handy() ? geradeDran() : [])); neu().then(() => { if (z.ebene !== 'welt' && dranFlug && z.kont === dranFlug.kontinent_id) { /* Start-Ansicht: Kontinent, eingezoomt auf die Route */ } }); });
  zeichnePfad();
  wurzel._z = z; // für Tests
  return wurzel;
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
  // WD-6: Gold im Reisepass – je Ort gold, je Flug abgelegt (etappen_abgelegt von etappen); fehlen die Felder (alter Server), bleibt alles wie bisher
  const goldOrte = new Set((konto?.orte || []).filter((o) => o.gold === true).map((o) => o.block_id));
  // Vorgabe „abgelegt“ 6: alle Flüge mit Karten (= gelandet) aus schule_konto; ganz abgelegt golden, teilweise mit Gold-Leiste, sonst „noch nichts abgelegt“
  const fluege = Array.isArray(konto?.fluege) ? konto.fluege : (konto?.orte || []).flatMap((o) => (o.fluege || []).map((f) => ({ block_id: o.block_id, ...f })));
  const blockVon = (f) => f.block_id ?? d.mit.find((e) => e.id === f.einheit_id)?.block_id;
  const flugOrt = (f) => d.orte.find((o) => o.block_id === blockVon(f))?.stadt || f.ort || '';
  const flugEintrag = (f) => { const a = Number(f.etappen_abgelegt) || 0, n = Number(f.etappen) || 0; const gold = f.abgelegt === true;
    return el('li', { class: 'lr-flug-eintrag' + (gold ? ' lr-flug-gold' : '') }, el('span', { class: 'lr-flug-symbol', 'aria-hidden': 'true' }, '✈'),
      el('span', { class: 'lr-flug-text' }, el('b', {}, f.titel || 'Flug'), el('small', {}, [flugOrt(f), gold ? 'alle Etappen abgelegt' : null].filter(Boolean).join(' · '))),
      el('span', { class: 'lr-flug-rechts' }, gold ? '★ ABGELEGT' : a ? `${a} von ${n} abgelegt` : 'noch nichts abgelegt',
        !gold && a && n ? el('span', { class: 'lr-mini-gold', 'aria-hidden': 'true' }, ...Array.from({ length: n }, (_, i) => el('i', { class: i < a ? 'g' : '' }))) : null)); };
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
    lernKopf('REISEPASS', kind.name), lernStats(konto, { d }),
    // AB-A: Abzeichen der Landungen (gleichwertig nebeneinander)
    konto?.abzeichen ? el('section', { class: 'lr-karte-box lr-abzeichen-zeile' }, el('h2', {}, 'Abzeichen'),
      el('p', { class: 'lr-abzeichen' }, el('span', { class: 'lr-abz-direkt' }, `⚡ Direkt ${lernZahl(konto.abzeichen.direkt || 0)}`), ' · ',
        el('span', { class: 'lr-abz-sauber' }, `✓ Sauber ${lernZahl(konto.abzeichen.sauber || 0)}`), ' · ',
        el('span', { class: 'lr-abz-sturm' }, `⚡ Ausdauer ${lernZahl(konto.abzeichen.sturm || 0)}`))) : null,
    fluege.length ? el('section', { class: 'lr-karte-box lr-pass-fluege' }, el('h2', {}, 'Flüge'),
      el('ul', { class: 'lr-flug-eintraege' }, ...fluege.slice().sort((x, y) => (y.abgelegt === true) - (x.abgelegt === true) || (Number(y.etappen_abgelegt) || 0) - (Number(x.etappen_abgelegt) || 0)).map(flugEintrag)),
      fluege.some((f) => f.abgelegt === true) || goldOrte.size ? el('p', { class: 'lr-leise lr-gold-hinweis' }, 'Gold heißt: Alle Etappen sind abgelegt.') : null) : null,
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Stempel'),
      stempel.length ? el('div', { class: 'lr-stempelraster' }, ...stempel.map((o, i) => { const gold = goldOrte.has(o.block_id); // WD-6: alle Flüge des Orts abgelegt → Stempel golden
        return el('div', { class: 'lr-stempel' + (gold ? ' lr-stempel-gold' : ''), style: `--dreh:${(i * 37) % 17 - 8}deg`, ...(gold ? { title: 'Alle Flüge abgelegt' } : {}) },
          el('b', {}, o.stadt), el('small', {}, gold ? '★ GOLD ★' : o.kontinent_titel)); }))
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
  const teile = [el('p', { class: 'lern-frage' }, lernMathe(f.text))];
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
      const lab = el('label', { class: 'lern-option' }, inp, el('span', {}, lernMathe(t))); optionen.push(lab); return lab;
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
  } else if (a.antworttyp === 'bedingung') {
    // Fundament Schritt 2: Aufgaben mit vielen richtigen Antworten. Ein bis sechs Zahlenfelder; die Bedingungen stehen im Aufgabentext,
    // geprüft wird nur auf dem Server (die App kennt die Prüfregeln nicht).
    const n = Math.min(6, Math.max(1, (f.felder || []).length));
    const eingaben = Array.from({ length: n }, (_, i) => el('input', { type: 'text', inputmode: 'text', autocomplete: 'off', class: 'lern-luecke lern-zahlfeld',
      'aria-label': n > 1 ? `Zahl ${i + 1} von ${n}` : 'Zahl', value: wert?.werte?.[i] ?? '' }));
    const lies = () => {
      const w = eingaben.map((x) => x.value.trim());
      wert = w.every((x) => x !== '') ? { werte: w } : null;
      fehler = wert ? null : (n > 1 ? 'Bitte fülle alle Felder aus.' : 'Bitte erst antworten.');
    };
    eingaben.forEach((x) => { x.addEventListener('input', lies); felder.push(x); });
    teile.push(el('div', { class: 'lern-zahlfelder' + (n > 3 ? ' viele' : ''), role: 'group', 'aria-label': 'Deine Zahlen' },
      ...eingaben.map((x, i) => el('label', { class: 'lern-zahlfeld-rahmen' }, n > 1 ? el('small', { 'aria-hidden': 'true' }, String(i + 1)) : null, x))));
    lies(); fehler = null;
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
  const zahlFelder = opts.tasten && (a.antworttyp === 'zahl' || a.antworttyp === 'bedingung' || (a.antworttyp === 'luecken' && !lernIstTermVorlage(f.schablone))) ? felder.filter((x) => x.type === 'text') : [];
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
const lernZahlenReihe = (werte) => (werte || []).map((x) => String(x ?? '').trim().replace(/^-/, '−')).join(';\u00a0'); // geschütztes Leerzeichen: die Reihe bricht nicht mitten um
function lernLoesungText(a) {
  const l = a.loesung || {};
  if (a.antworttyp === 'bedingung') return Array.isArray(l.beispiel) ? 'zum Beispiel ' + lernZahlenReihe(l.beispiel) : ''; // viele Antworten sind richtig: gezeigt wird ein Beispiel
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[l.index] ?? '';
  if (a.antworttyp === 'markierung') return lernStrichText(a.frage?.grafik, l.index);
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return lernVorzeichenText(s.map((t, i) => t + (i < s.length - 1 ? String(l.werte?.[i] ?? '') : '')).join('')); }
  if (a.antworttyp === 'text') return l.text ?? '';
  return l.wert !== undefined ? lernZahl(l.wert) + (l.einheit ? ' ' + l.einheit : '') : '';
}
function lernAntwortText(a, w) {
  if (a.antworttyp === 'bedingung' && w) return lernZahlenReihe(w.werte);
  if (!w) return '(keine Antwort)';
  if (a.antworttyp === 'auswahl') return (a.antworten || [])[w.index] ?? '';
  if (a.antworttyp === 'markierung') return lernStrichText(a.frage?.grafik, w.index);
  if (a.antworttyp === 'luecken') { const s = String(a.frage?.schablone || '').split('□'); return lernVorzeichenText(s.map((t, i) => t + (i < s.length - 1 ? (w.werte?.[i] ?? '') : '')).join('')); }
  return String(w.wert ?? '').replace(/^-/, '−');
}

// Typ „bedingung“: welche Bedingung nicht passt, mit der Zahl des Kindes („Deine Summe ist 1.“). Der Server nennt nur die erste.
function lernBedingungRueck(r) {
  if (!r?.verletzt) return null;
  return el('p', { class: 'lr-bedingung' }, el('b', {}, lernMathe(r.verletzt), ': '), r.hinweis ? lernMathe(r.hinweis) : 'Das passt noch nicht.');
}
// Alle Bedingungen der Aufgabe als Liste: bei „richtig“ alle abgehakt, sonst die offene mit Pfeil (über die anderen weiß die App nichts).
function lernBedingungListe(a, r) {
  if (a.antworttyp !== 'bedingung') return null;
  const namen = (r?.loesung?.bedingungen || a.loesung?.bedingungen || []).map((b) => (typeof b === 'string' ? b : b?.name)).filter(Boolean);
  if (!namen.length) return null;
  return el('ul', { class: 'lr-bedingungen', 'aria-label': 'Alle Bedingungen' }, ...namen.map((nm) => {
    const offen = !r?.richtig && nm === r?.verletzt;
    return el('li', { class: r?.richtig ? 'ok' : offen ? 'offen' : '' }, el('span', { 'aria-hidden': 'true' }, r?.richtig ? '✓' : offen ? '→' : '·'), ' ', lernMathe(nm), offen ? el('span', { class: 'lr-nur-vorlesen' }, ' (passt noch nicht)') : null);
  }));
}

// ---------- Kind: Lerneinheit in Etappen ----------
// #/lerneinheit/<kind>-<einheit>         Übersicht: Etappen-Weg, danach Test
// #/lerneinheit/<kind>-<einheit>-<n>     Etappe n: Kurz erklärt → Selbst probieren → geschafft
// #/lerneinheit/<kind>-<einheit>-test    Test / Verbessern / Nachtest
// Eine Etappe ist ein Lernziel; geschafft, wenn ihre Übungsaufgaben einmal richtig gelöst sind (Datenbank: schule.etappen_stand).

// Text mit ⟦markierten⟧ Stellen als Knoten (markierte Teile hervorgehoben).
// Zusätzlich (Vorgabe Erklärungen 16.11.): Brüche a/b gestapelt; mit wctx werden neue Wörter beim ersten Vorkommen antippbar.
const LERN_BUCHST = 'A-Za-zÄÖÜäöüß';
// Brüche im Fließtext erkennen (Wunsch eines Kindes, 27.11.: „als normalen Bruch darstellen, nicht 3/4“).
// Ergebnis: Liste aus Textstücken und { z, n } (Zähler, Nenner als Text). Reine Textfunktion, ohne Bildschirm prüfbar.
// Erkannt: 3/4 · 2,5/3 · x/2 · 2x/27 · 11π/6 · 1/b² · 1/√2 · (x + 1)/(x − 2) · 1/(2x) – die Klammern fallen weg, der Bruchstrich fasst zusammen.
// Nicht erkannt (bleibt Text): km/h, m/s, ja/nein, und/oder · Daten und Ketten wie 3/4/2026, 68/95/99,7 · Hochzahlen wie x^(1/2) ·
// f(x)/2, √(…)/2, 2(x + 1)/3 (Zähler nicht eindeutig) · 1/2x (zweideutig) · x/y-Ebene.
// 0.93.7 (Gegenprüfung): Tausendergruppen bleiben ganz (7/1 000 → 7 über 1 000; 11 880/20 736; sonst Text) ·
// Hochzahlen ganz am Nenner (4/x⁻², 1/2ⁿ⁻¹), ^-Schreibweise (2/3^2, 3^2/4) bleibt Text · C/D, X/L (einzelne Großbuchstaben) bleiben Text ·
// führende Null (03/04) und Jahr/Jahr (2026/27) bleiben Text.
// 0.93.8: „2 125/128“ ist zweideutig (Tausendergruppe oder gemischte Zahl): immer ganz Text, auch bei Gruppe im Nenner (11 880/20 736) ·
// bekannte hochgestellte Zeichen gehören zur Basis (4/xᵏ); jedes andere Hoch-/Tiefzeichen oder Modifikator-Buchstabe direkt dahinter: Text (4/xᴺ) ·
// Datum nach Datumswort („am 27/11“, beliebiger Leerraum) und Auswahl-Kürzel (w/m, W/m, j/n, u/o) bleiben Text.
const LERN_EINHEIT = new Set(['m', 'km', 'cm', 'mm', 'dm', 's', 'h', 'g', 'l']);
const LERN_HOCH = '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵃᵇᶜᵈᵉᶠᵍʰʲᵏˡᵐᵒᵖʳˢᵗᵘᵛʷˣʸᶻ'; // alle hochgestellten Zeichen: gehören ganz zur Basis
const LERN_AUSWAHL = new Set(['w/m', 'm/w', 'm/w/d', 'j/n', 'ja/nein', 'u/o']); // Auswahl-Kürzel: Text (Groß-/Kleinschreibung egal)
// Allgemeine Klasse: Modifikator-Buchstaben, Modifikator-Symbole (u. a. ^), hoch-/tiefgestellte Ziffern und Zeichen (ᴺ, ᴬ, ᵅ, ᵏ, ⁿ, ₂ …)
const LERN_HOCH_ALLG = /[\p{Lm}\p{Sk}²³¹⁰-₟]/u;
// Eng gefasst: „bis“ und „ab“ treffen echte Brüche im Bestand („von 1/3 bis 1/2“, „AB 2/4“), „den“ wäre zu riskant („den 3/4“).
const LERN_DATUMSWORT = /(?:^|[^A-Za-zÄÖÜäöüß])(?:am|vom|zum|seit)\s+$/i; // „am 27/11“, „bis zum 3/12“: Datum, Text
const LERN_LZ = '[ \\u00a0\\u202f]'; // Trenner von Tausendergruppen (Leerzeichen, geschützt, schmal geschützt)
const LERN_BRUCH_TERM = `(?:\\d{1,4}(?:,\\d{1,3})?)?(?:√\\d{1,4}|[a-zA-Zα-ω])?[${LERN_HOCH}]*°?`;
const LERN_BRUCH_LINKS = new RegExp(`(${LERN_BRUCH_TERM})$`);
const LERN_BRUCH_RECHTS = new RegExp(`^(${LERN_BRUCH_TERM})`);
function lernBruchTeile(text) {
  const s = String(text ?? ''); const aus = []; let last = 0;
  const klammerOk = (t) => t.length > 0 && t.length <= 30 && !/[/()]/.test(t) && !new RegExp(`[${LERN_BUCHST}]{3,}`).test(t);
  const kern = (t) => /[\dA-Za-zα-ω√]/.test(t);
  for (let i = s.indexOf('/'); i !== -1; i = s.indexOf('/', i + 1)) {
    if (i < last || i === 0) continue;
    let a0; let z; let zweideutig = false;
    if (s[i - 1] === ')') {
      const p = s.lastIndexOf('(', i - 1); if (p < last) continue;
      z = s.slice(p + 1, i - 1); a0 = p;
      if (!klammerOk(z) || (p > 0 && (new RegExp(`[\\d${LERN_BUCHST}α-ω√^${LERN_HOCH}]`).test(s[p - 1]) || LERN_HOCH_ALLG.test(s[p - 1])))) continue; // f(x)/2, √(…)/2, 2(x+1)/3
    } else {
      const m = LERN_BRUCH_LINKS.exec(s.slice(Math.max(last, i - 14), i)); if (!m || !kern(m[1])) continue;
      z = m[1]; a0 = i - z.length;
      if (a0 > 0 && (new RegExp(`[\\d/.,:^${LERN_BUCHST}α-ω√${LERN_HOCH}°]`).test(s[a0 - 1]) || LERN_HOCH_ALLG.test(s[a0 - 1]))) continue; // km/h, 3/4/2026, 1.5/2, 3^2/4
      if (/^\d{3}(?!\d)/.test(z) && new RegExp(`\\d${LERN_LZ}$`).test(s.slice(0, a0))) { // Tausendergruppe: 1 200/x, 11 880/…
        const g = new RegExp(`(?:^|[^\\d,.])(\\d{1,3}(?:${LERN_LZ}\\d{3})*${LERN_LZ})$`).exec(s.slice(last, a0)); if (!g) continue; // nicht eindeutig: Text
        if (/^\d{3}$/.test(z)) zweideutig = true; // 2 125/128: Tausendergruppe oder gemischte Zahl?
        z = g[1] + z; a0 -= g[1].length;
        if (a0 > 0 && (new RegExp(`[\\d/.,:^${LERN_BUCHST}α-ω√${LERN_HOCH}°]`).test(s[a0 - 1]) || LERN_HOCH_ALLG.test(s[a0 - 1]))) continue;
      }
    }
    const davor = s.slice(Math.max(0, a0 - 3), a0);
    if (/\^\($/.test(davor) || /\^\(?[−-]$/.test(davor)) continue; // Hochzahl x^(1/2), x^-1/2 bleibt, wie sie ist
    let b1; let n;
    if (s[i + 1] === '(') {
      const q = s.indexOf(')', i + 2); if (q === -1) continue;
      n = s.slice(i + 2, q); b1 = q + 1;
      if (!klammerOk(n) || LERN_HOCH_ALLG.test(s[b1] || '')) continue; // auch unbekannte Hochzeichen: Text
    } else {
      const m = LERN_BRUCH_RECHTS.exec(s.slice(i + 1, i + 15)); if (!m || !kern(m[1])) continue;
      n = m[1]; b1 = i + 1 + n.length;
      const tg = new RegExp(`^(?:${LERN_LZ}\\d{3}(?!\\d))+`).exec(s.slice(b1)); // Tausendergruppen im Nenner: 7/1 000, 1/4 096
      if (tg) { if (!/^\d{1,3}$/.test(n)) continue; n += tg[0]; b1 += tg[0].length; } // Gruppe im Nenner hebt die Zweideutigkeit im Zähler NICHT auf
      if (/^\d.*[a-zA-Zα-ω]/.test(n)) continue; // 1/2x ist zweideutig (½ · x oder 1 durch 2x): bleibt Text; eindeutig ist 1/(2x)
      const nach = s.slice(b1, b1 + 2);
      if (new RegExp(`^[\\d/(√α-ω^${LERN_HOCH}${LERN_BUCHST}]`).test(nach) || /^[.,:]\d/.test(nach) || LERN_HOCH_ALLG.test(nach[0] || '') || new RegExp(`^-[${LERN_BUCHST}]`).test(nach)) continue; // 3/4/2026, 1/2x, x/y-Ebene
    }
    if (zweideutig) continue; // 2 125/128, 1 200/x: ganz Text, nie zerreißen, nie raten
    if (LERN_EINHEIT.has(z) && LERN_EINHEIT.has(n)) continue; // m/s, g/l
    if (LERN_AUSWAHL.has(`${z}/${n}`.toLowerCase())) continue; // w/m, j/n, u/o
    if (/^\d{1,2}$/.test(z) && /^\d{1,2}$/.test(n) && +z >= 1 && +z <= 31 && +n >= 1 && +n <= 12 && LERN_DATUMSWORT.test(s.slice(0, a0))) continue; // am 27/11
    if (/^[A-ZÄÖÜ]$/.test(z) && /^[A-ZÄÖÜ]$/.test(n)) continue; // C/D, X/L, I/V (römische Zahlzeichen), Teil A/B: Text
    if (/^0\d/.test(z) || /^0\d/.test(n)) continue; // führende Null: Datum 03/04
    if (/^(?:1[89]|20)\d\d$/.test(z) && (Number(n) === Number(z) + 1 || (/^\d\d$/.test(n) && Number(n) === (Number(z) + 1) % 100))) continue; // Schuljahr 2026/27
    let vor = s.slice(last, a0);
    if (/^\d+$/.test(z) && /^\d+$/.test(n.replace(/[ \u00a0\u202f]/g, '')) && Number(z) < Number(n.replace(/[ \u00a0\u202f]/g, ''))) vor = vor.replace(/(^|[^\d,.])(\d{1,3}) $/, '$1$2 '); // gemischte Zahl 1 1/4: nicht umbrechen
    const vz = /[−-]$/.test(vor) ? vor.slice(-1) : ''; // Minus direkt davor: bleibt am Bruch (kein Zeilenumbruch dazwischen)
    if (vz) vor = vor.slice(0, -1);
    if (vor) aus.push(vor);
    aus.push(vz ? { z, n, vz } : { z, n });
    last = b1;
  }
  if (last < s.length) aus.push(s.slice(last));
  return aus;
}
function lernBruchKnoten(s) {
  return lernBruchTeile(s).map((t) => { if (typeof t === 'string') return lernText(t);
    const b = el('span', { class: 'lern-bruch-text', role: 'img', 'aria-label': `${t.z} durch ${t.n}` }, el('span', {}, lernText(t.z)), el('span', {}, lernText(t.n)));
    return t.vz ? el('span', { class: 'lern-kein-umbruch' }, t.vz === '-' ? '−' : t.vz, b) : b; });
}
// Aufgabentext, Tipp, Lösung, Lösungsweg: Text mit gestapelten Brüchen (Liste von Knoten; el() und lernAnhaengen() nehmen Listen an).
const lernMathe = (t) => lernBruchKnoten(String(t ?? ''));
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
// Kl. 7–10: „Kurz gesagt“ zusätzlich als erste Zeile in der Karte (Schalter je Kind und Gerät, Standard aus – Entscheidung vom Nutzer offen).
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
  const w = b.werte || []; const sum = w.reduce((a, x) => a + x.wert, 0) || 1;
  const beschr = (x) => x.name + (b.zahlen === false ? '' : ` (${lernZahlText(x.wert)}${b.einheit || ''})`);
  // Breite nach der längsten Beschriftung (rund 9 Einheiten je Zeichen), damit die Legende am Handy nicht abgeschnitten wird
  const B = Math.max(340, 250 + Math.ceil(Math.max(0, ...w.map((x) => beschr(x).length)) * 9)), H = Math.max(220, 40 + w.length * 24), cx = 110, cy = 110, r = 92;
  const { svg, mk } = lernSvg(B, H, b.label || `Kreisdiagramm: ${w.map((x) => `${x.name} ${x.wert}`).join(', ')}`);
  let a0 = -Math.PI / 2;
  w.forEach((x, i) => {
    const a1 = a0 + 2 * Math.PI * x.wert / sum; const gross = a1 - a0 > Math.PI ? 1 : 0;
    mk('path', { d: `M${cx} ${cy} L${cx + r * Math.cos(a0)} ${cy + r * Math.sin(a0)} A${r} ${r} 0 ${gross} 1 ${cx + r * Math.cos(a1)} ${cy + r * Math.sin(a1)} Z`, class: 'saeule sektor saeule' + (i % 4) });
    mk('rect', { x: 222, y: 24 + i * 24, width: 14, height: 14, class: 'saeule saeule' + (i % 4) });
    mk('text', { x: 242, y: 36 + i * 24, class: 'zahl links' }, beschr(x));
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
    b.kopf ? el('thead', {}, el('tr', {}, ...b.kopf.map((k) => el('th', {}, lernMathe(k))))) : null,
    el('tbody', {}, ...(b.zeilen || []).map((z, r) => el('tr', {}, ...z.map((c, i) => el(i === 0 && b.erste_spalte_kopf !== false ? 'th' : 'td', b._neu?.zellen?.has(`${r},${i}`) ? { class: 'neu' } : {}, lernMathe(c)))))));
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
    kurzGesagt && e.regel ? el('p', { class: 'lr-kurzgesagt' }, el('b', {}, 'Kurz gesagt: '), lernMathe(lernKurzGesagt(e.regel))) : null,
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
      serie: Number(k.serie || 0), ziel: Number(k.ziel || 4), sitzt: !!k.sitzt, schwerOk: !!k.schwer_ok, schwerNoetig: !!k.schwer_noetig, faellig: !!k.faellig, nachgewiesen: k.test_nachgewiesen !== undefined ? !!k.test_nachgewiesen && !k.sitzt : !!k.fertig && !k.sitzt,
      ...lernRegelFelder(k),
      aufgaben: (daten.uebungen || []).filter((a) => a.lernziel === e.lernziel && !a.bonus),
      bonus: (daten.bonus || []).filter((a) => a.lernziel === e.lernziel) }; // F: Knobel-Bordkarten (freiwillig)
  });
}
// W176 Teil 1: Regel „gelandet“ ohne Minuspunkte (Migration 20261118_w176_t1_*). Fehlen die Felder, gilt die alte Anzeige mit Punkten.
function lernRegelFelder(k) {
  if (k?.eigene_loesungen === undefined) return { neueRegel: false };
  return { neueRegel: true, eigene: Number(k.eigene_loesungen || 0), folge: Number(k.folge || 0), folgeZiel: Number(k.folge_ziel || 3), typenAnzahl: Number(k.typen_anzahl || 0),
    typenNoetig: Number(k.typen_noetig || 0), fehlerFolge: Number(k.fehler_folge || 0), stufeSenkung: Number(k.stufe_senkung || 0), sicher: !!k.sicher,
    ...(Array.isArray(k.gezaehlt) ? { gezaehlt: new Set(k.gezaehlt.map(Number)) } : {}), // H3: diese Bordkarten haben schon als eigene Lösung gezählt
    ...(k.flug_nachtest !== undefined ? { flugNachtest: !!k.flug_nachtest } : {}), ...(k.wieder_offen !== undefined ? { wiederOffen: !!k.wieder_offen } : {}) };
}
// Checkliste je Etappe: „Eigene Lösungen 4/6 · 2 Aufgabentypen ✓ · schwere ✓ · 3 in Folge: 1/3“ – nichts fällt sichtbar zurück außer „in Folge“
function lernCheckliste(e) {
  const z = e.ziel || 6;
  const teile = [
    [`Eigene Lösungen ${Math.min(e.eigene, z)}/${z}`, e.eigene >= z],
    e.typenNoetig > 1 ? [`${e.typenNoetig} Aufgabentypen`, e.typenAnzahl >= e.typenNoetig, `${Math.min(e.typenAnzahl, e.typenNoetig)}/${e.typenNoetig}`] : null,
    e.schwerNoetig ? ['schwere', e.schwerOk] : null,
    [`${e.folgeZiel} in Folge`, e.folge >= e.folgeZiel, `${Math.min(e.folge, e.folgeZiel)}/${e.folgeZiel}`],
  ].filter(Boolean);
  return el('ul', { class: 'lr-checkliste', 'aria-label': 'Bis „gelandet“' }, ...teile.map(([t, ok, stand]) =>
    el('li', { class: ok ? 'ok' : '' }, el('span', { 'aria-hidden': 'true' }, ok ? '✓' : '○'), ` ${t}`, !ok && stand && !t.includes('/') ? `: ${stand}` : '')));
}
// Aktivität heute (nur Zähler, ohne Bezug zur Schwelle): selbst gelöste Bordkarten dieses Kindes heute.
// H6: Der Server zählt die bestätigten Versuche im Tag des Kindes (Zeitzone des Kindes, heute_selbst) und nennt diesen Tag (heute_tag, I-2).
// Hier nur Zwischenspeicher {tag, n, server}. Kommt der Tag vom Server, gilt er – nicht der Kalendertag des Geräts. Nur ohne Server-Tag (alter Server) zählt das Gerät selbst.
const lernGeraetTag = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };
const lernHeuteLesen = (kind) => { try { return JSON.parse(localStorage.getItem('lern.heute.' + kind) || 'null'); } catch { return null; } };
const lernHeuteSchreiben = (kind, x) => { try { localStorage.setItem('lern.heute.' + kind, JSON.stringify(x)); } catch { /* egal */ } };
// I-3/H6: Tageswechsel – ein neuer Server-Tag ersetzt den Stand; ist seit dem letzten Server-Stand auch auf dem Gerät ein neuer Tag (Seite über Nacht offen),
// gilt der alte Stand nicht mehr (0), bis der Server beim nächsten Laden oder Antworten den neuen Tag nennt.
// AB-A / LB-3 Nachbesserung H6: kennt der Server das Tagesende des Kindes (heute_bis), gilt der Stand genau bis dahin – unabhängig von der Uhr und Zeitzone des Geräts.
const lernHeuteSetzen = (kind, n, tag, bis) => { if (n === undefined || n === null) return; lernHeuteSchreiben(kind, { tag: tag ? String(tag).slice(0, 10) : lernGeraetTag(), n: Number(n) || 0, server: !!tag, geraet: lernGeraetTag(), bis: bis || null }); };
const lernHeuteGilt = (x) => !!x && (x.bis && !isNaN(Date.parse(x.bis)) ? Date.now() < Date.parse(x.bis) : x.server ? (x.geraet || x.tag) === lernGeraetTag() : x.tag === lernGeraetTag());
const lernHeute = (kind) => { const x = lernHeuteLesen(kind); return lernHeuteGilt(x) ? Number(x.n) || 0 : 0; };
// LB Teil 6 Punkt 6: „heute“ des Kindes – der Tag vom Server, solange er gilt (bis heute_bis); sonst der Kalendertag des Geräts.
// 0.92.1: Ist heute_bis vorbei, hat beim Kind ein neuer Tag begonnen. Liegt das Gerät in einer Zeitzone hinter der des Kindes (Reise), zeigt sein Kalender
// dann noch den alten Tag – „heute“ ist aber mindestens der Tag nach dem letzten Server-Tag (sonst gälte z. B. die Wiederholungsrunde noch als gemacht).
const lernTagDanach = (tag) => { const d = new Date(String(tag).slice(0, 10) + 'T12:00:00Z'); d.setUTCDate(d.getUTCDate() + 1); return d.toISOString().slice(0, 10); };
const lernHeuteTag = (kind) => { const x = lernHeuteLesen(kind); const g = lernGeraetTag();
  if (!x?.server || !x.tag) return g;
  const tag = String(x.tag).slice(0, 10); if (lernHeuteGilt(x)) return tag;
  if (x.bis && !isNaN(Date.parse(x.bis))) return g > tag ? g : lernTagDanach(tag); // Tagesende des Kindes vorbei
  return g; };
const lernHeutePlus = (kind) => { const x = lernHeuteLesen(kind); lernHeuteSchreiben(kind, lernHeuteGilt(x) ? { ...x, n: (Number(x.n) || 0) + 1 } : { tag: lernGeraetTag(), n: 1, server: false, geraet: lernGeraetTag() }); };
// Punkte für die Serie: ●●○○ (gefüllt = richtig in Folge), bei „sitzt“ alle gefüllt.
function lernPunkte(e, { gross = false } = {}) {
  const n = Math.max(1, e.ziel || 4), voll = e.sitzt || e.fertig ? n : Math.min(n, e.serie || 0);
  return el('span', { class: 'lr-punkte' + (gross ? ' gross' : ''), role: 'img', 'aria-label': e.sitzt || e.fertig ? 'sitzt' : `${voll} von ${n} richtig` },
    ...Array.from({ length: n }, (_, i) => el('i', { class: i < voll ? 'voll' : '' })));
}
const lernKartenStatus = (e) => e.faellig ? 'Wiederholen' : e.sicher ? 'sicher' : e.sitzt || e.fertig ? (e.neueRegel ? 'gelandet' : 'sitzt') : (e.neueRegel ? e.eigene : e.serie) ? 'am Üben' : 'noch nicht geübt';
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
  lernJwLaden();
  loading();
  const [daten, konto, uebers] = await Promise.all([lernCall('schule_einheit_lesen', { lernender_id: k, einheit_id: eId }),
    lernCall('schule_konto', { lernender_id: k }).catch(() => null), lernCall('schule_uebersicht').catch(() => null),
    lernReiseKarteAlt.has(k) ? null : lernReiseKarte(k).catch(() => null)]); // WK F3: Namen der Reisekarte (je Sitzung einmal)
  if (!live()) return;
  const kind = { id: k, ...((uebers?.lernende || []).find((x) => x.id === k) || {}), ...(konto?.look || {}) };
  const ort0 = (uebers?.einheiten || []).find((e) => e.id === eId) || {};
  // WK F3: Land als Titel (aus der Karte), Stadt je Etappe; der alte Ortsname nur, wenn die Karte keinen Namen liefert
  const rkFlug = lernRkFlugVon(k, ort0.thema_id);
  const ort = rkFlug ? { ...ort0, stadtAlt: ort0.stadt, stadt: rkFlug.land, land: rkFlug.land } : ort0;
  const titel = ort.stadt ? `${ort.stadt}: ${ort.ort_titel || ort.titel || ''}` : (daten.inhalt?.ziel || 'Lerneinheit').split(/[:;.]/)[0];
  $('#title').textContent = ort.stadt || titel; // kurz: Land bzw. Ort; das Thema steht als Überschrift darunter
  const ctx = { kind: k, einheit: eId, live, daten, ort, titel, kindObj: kind, rkFlug, stadtVon: (e) => (rkFlug && e ? lernEtappenStadt(k, ort0.thema_id, e.nr, '') : '') || '', basis: `#/lerneinheit/${k}-${eId}`, leitung: !!uebers?.leitung, konto, u: uebers, regeln: konto?.regeln || null, mischGezeigt: new Set(), mischNachgeladen: false };
  lernHeuteSetzen(k, daten.heute_selbst, daten.heute_tag, daten.heute_bis); // H6: Tag (und Tagesende) vom Server
  const etappen = lernEtappen(daten);
  lernTitel = new Map(etappen.filter((e) => daten.inhalt?.etappen?.length).map((e) => [e.lernziel, e.titel]));
  ctx.titelKurz = ort.titel || titel;
  if (teil === 'test' || (!teil && daten.laufender_test)) { lernEinheitTest(ctx); return; }
  // Teil 4 Punkt 5e: Flug öffnen, wenn alle Pflicht-Etappen gelandet sind und nur der Test fehlt → zuerst die Test-Aufforderung, nicht die Übungen
  // (nur beim Öffnen ohne Ziel bzw. „üben“ ohne Etappe; „-erklaeren“ und eine gewählte Etappe bleiben erreichbar)
  if ((!teil || (teil === 'ueben' && !String(arg).split('-')[3])) && lernTestFaellig(daten, etappen)) { lernEinheitTest(ctx, lernTestFaellig(daten, etappen)); return; }
  // WK 2 (A3): Link mit Etappen-Nummer zu einer gelandeten Etappe bei fälligem Test → Test-Aufforderung groß, „Trotzdem weiterüben“ klein (kein stilles Weiterüben)
  { const nrU = teil === 'ueben' ? Number(String(arg).split('-')[3]) || 0 : 0; const tfU = nrU && etappen[nrU - 1]?.fertig ? lernTestFaellig(daten, etappen) : null;
    if (tfU) { lernEinheitTest(ctx, { ...tfU, trotzdem: `${ctx.basis}-${nrU}` }); return; } }
  // #/lerneinheit/k-e[-erklaeren|-ueben[-n]|-fehler|-n]
  const rest = String(arg).split('-').slice(3);
  const n = Number(teil);
  if (n && etappen[n - 1]) { lernThemaSeite(ctx, etappen, 'ueben', n); return; }
  lernThemaSeite(ctx, etappen, ['ueben', 'fehler'].includes(teil) ? teil : 'erklaeren', Number(rest[0]) || 0, { einsteigen: rest[1] === 'start' });
}

// ---------- Thema: Erklären | Üben | Typische Fehler (Aufbau wie das Mathe-Lernblatt) ----------
// LB Teil 5 M1: Wörter mit Bindestrich („n-te“) nicht am Bindestrich umbrechen – Text bleibt gleich
const lernOhneTrennung = (text) => String(text || '').split(/(\s+)/).map((w) => (/\S-\S/.test(w) ? el('span', { class: 'lern-kein-umbruch' }, w) : w));
// LB Teil 5 K3: IB-Lernbereich „MYP 3 Numerical and abstract reasoning (Zahl und Algebra)“ → deutsch zuerst (nur Anzeige)
function lernLbText(x) {
  const m = String(x || '').match(/^(MYP\s*\d+\s+)(.+?)\s*\(([^()]+)\)\s*$/);
  return m ? `${m[1]}${m[3]} (${m[2]})` : String(x || '');
}
// ---------- JW-App (0.93.0): Jugendwort-Sticker – Vorgabe inhalte/pruefung/kind/jugendwoerter/umsetzung.md (Fassung 2) ----------
// Ein Sticker je Geschafft-Ansicht, der Satz bleibt normales Deutsch. Keine Einstellungen, Anrede „Digga“. Wortliste: daten/jugendwoerter.json (Kopie von
// woerter.json) – Wörter mit abgelaufenem „verfall“ (Monat „JJJJ-MM“ gilt bis Monatsende) oder „ungeeignet“ werden nie gezogen.
// Auswahl nur im Gerät (localStorage lern.jw.<kind>): je Anlass ein Sack ohne Zurücklegen, nie der letzte Spruch, kein Wort aus den letzten 4 Stickern
// (solange ein anderer passender Spruch da ist; „Digga“ zählt nicht), Fehler-Sticker beim 1., 3., 5. … Fehler des Lerntags und nie ab dem 2. in Folge, Anrede einmal je Lerntag.
const LERN_JW_DATEI = LERN_KARTE_BASIS_DATEN('jugendwoerter.json');
function LERN_KARTE_BASIS_DATEN(name) { try { const s = document.currentScript?.src || [...document.scripts].map((x) => x.src).find((x) => /lernen\.js/.test(x)); return new URL('daten/' + name, s || location.href).href; } catch { return 'daten/' + name; } }
let lernJwDaten = null; let lernJwVersprechen = null;
function lernJwLaden() {
  if (!lernJwVersprechen) lernJwVersprechen = fetch(LERN_JW_DATEI).then((r) => (r.ok ? r.json() : null)).then((x) => { lernJwDaten = x && Array.isArray(x.sprueche) ? x : null; return lernJwDaten; })
    .catch(() => { lernJwVersprechen = null; return null; });
  return lernJwVersprechen;
}
function lernJwWortGueltig(w, heute) {
  if (!w || w.einsatz === 'ungeeignet' || !Array.isArray(w.einsatz) || !w.einsatz.length) return false;
  const v = String(w.verfall || ''); const h = String(heute || '').slice(0, 10);
  if (/^\d{4}-\d{2}$/.test(v)) return h.slice(0, 7) <= v; // Monat: gilt bis zum Monatsende
  if (/^\d{4}-\d{2}-\d{2}$/.test(v)) return h <= v;
  return false; // ohne Verfallsdatum nicht ziehen (Halbjahresprüfung fehlt)
}
function lernJwSprueche(daten, anlass, heute) {
  if (!daten) return []; const woerter = new Map((daten.woerter || []).map((w) => [w.id, w]));
  return (daten.sprueche || []).filter((s) => s.anlass === anlass && (s.woerter || []).length && s.woerter.every((id) => lernJwWortGueltig(woerter.get(id), heute)));
}
const lernJwSchl = (kindId) => `lern.jw.${kindId}`;
function lernJwStand(kindId) { try { const x = JSON.parse(localStorage.getItem(lernJwSchl(kindId)) || 'null'); if (x && typeof x === 'object') return { sack: {}, letzte: [], ...x }; } catch { /* neu */ } return { sack: {}, letzte: [] }; }
function lernJwSpeichern(kindId, st) { try { localStorage.setItem(lernJwSchl(kindId), JSON.stringify(st)); } catch { /* ohne Speicher: Abwechslung startet neu */ } }
const lernJwHeute = (kindId) => { try { return lernHeuteTag(kindId); } catch { return new Date().toISOString().slice(0, 10); } };
// Spruch ziehen (ohne Daten: null). zufall für Tests austauschbar.
function lernJwZiehen(kindId, anlass, { daten = lernJwDaten, heute = lernJwHeute(kindId), zufall = Math.random } = {}) {
  const kand = lernJwSprueche(daten, anlass, heute); if (!kand.length) return null;
  const st = lernJwStand(kindId); const ids = new Set(kand.map((s) => s.id));
  let sack = (st.sack[anlass] || []).filter((id) => ids.has(id)); if (!sack.length) sack = kand.map((s) => s.id);
  const letzter = st.letzte[st.letzte.length - 1]?.id;
  const gesperrt = new Set(st.letzte.slice(-4).flatMap((x) => x.woerter || []).filter((w) => w !== 'digga'));
  const nimm = (liste) => liste[Math.floor(zufall() * liste.length) % liste.length];
  const ohneLetzten = (l) => l.filter((id) => id !== letzter);
  const frei = (l) => l.filter((id) => !kand.find((s) => s.id === id).woerter.some((w) => gesperrt.has(w)));
  // erst im Sack ohne gesperrte Wörter; sonst alle passenden Sprüche ohne gesperrte Wörter (Sack neu); sonst ohne den letzten Spruch
  let id = nimm(frei(ohneLetzten(sack)));
  if (!id) { const alle = frei(ohneLetzten(kand.map((s) => s.id))); if (alle.length) { id = nimm(alle); sack = kand.map((s) => s.id); } }
  if (!id) id = nimm(ohneLetzten(sack)) || nimm(ohneLetzten(kand.map((s) => s.id))) || nimm(sack);
  const spruch = kand.find((s) => s.id === id);
  st.sack[anlass] = sack.filter((x) => x !== id); st.letzte = [...st.letzte, { id, woerter: spruch.woerter }].slice(-4);
  lernJwSpeichern(kindId, st);
  const wmap = new Map((daten.woerter || []).map((w) => [w.id, w]));
  return { ...spruch, wortListe: spruch.woerter.map((w) => wmap.get(w)).filter(Boolean) };
}
// Fehler: Sticker nur beim 1., 3., 5. … Fehler des Lerntags und nie ab dem 2. Fehler in Folge
function lernJwFehler(kindId, opts = {}) {
  const heute = opts.heute || lernJwHeute(kindId); const st = lernJwStand(kindId);
  if (st.fehlerTag !== heute) { st.fehlerTag = heute; st.fehlerN = 0; st.fehlerFolge = 0; }
  st.fehlerN = (st.fehlerN || 0) + 1; st.fehlerFolge = (st.fehlerFolge || 0) + 1; lernJwSpeichern(kindId, st);
  return st.fehlerN % 2 === 1 && st.fehlerFolge === 1 ? lernJwZiehen(kindId, 'fehler', { ...opts, heute }) : null;
}
function lernJwRichtig(kindId) { const st = lernJwStand(kindId); if (st.fehlerFolge) { st.fehlerFolge = 0; lernJwSpeichern(kindId, st); } }
// Anrede „Digga“: einmal je Lerntag auf der Abflugtafel
function lernJwAnrede(kindId, opts = {}) {
  const heute = opts.heute || lernJwHeute(kindId); const st = lernJwStand(kindId); if (st.anrede === heute) return null;
  const z = lernJwZiehen(kindId, 'anrede', { ...opts, heute }); if (!z) return null;
  const st2 = lernJwStand(kindId); st2.anrede = heute; lernJwSpeichern(kindId, st2); return z;
}
// Bedeutung: kleines Blatt mit Wort, „gesprochen …“, Bedeutung, Schließen
function lernJwBedeutung(z, vorher) {
  document.querySelectorAll('.lr-jw-blatt').forEach((x) => x.remove());
  const zu = () => { blatt.remove(); vorher?.focus?.({ preventScroll: true }); };
  const nacht = !!vorher?.closest?.('.lr-abflug-nacht, .lr-nacht, .lr-ab-nacht'); // KJ 2 K2a: nachts dunkel wie die übrigen Blätter
  const blatt = el('div', { class: 'lr-jw-blatt' + (nacht ? ' lr-jw-blatt-nacht' : ''), role: 'dialog', 'aria-modal': 'true', 'aria-label': 'Bedeutung', onclick: (ev) => { ev.stopPropagation(); if (ev.target === blatt) zu(); } },
    el('div', { class: 'lr-jw-blatt-innen' },
      el('p', { class: 'lr-jw-blatt-sticker' }, z.sticker),
      ...z.wortListe.filter((w) => !(w.id === 'digga' && z.wortListe.length > 1)).map((w) => el('div', { class: 'lr-jw-wort' }, el('b', {}, w.wort), w.gesprochen ? el('small', {}, ` · gesprochen „${w.gesprochen}“`) : null,
        el('p', {}, w.bedeutung))),
      el('button', { type: 'button', class: 'lr-knopf lr-knopf-klein lr-jw-zu', onclick: (ev) => { ev.stopPropagation(); zu(); } }, 'Schließen')));
  blatt.addEventListener('keydown', (ev) => { if (ev.key === 'Escape') zu(); });
  document.body.append(blatt); blatt.querySelector('.lr-jw-zu').focus({ preventScroll: true });
}
function lernJwStickerEl(z, art = 'szene') {
  if (!z) return null; const lang = String(z.sticker).length > 11;
  const b = el('button', { type: 'button', class: `lr-jw-sticker lr-jw-${art} lr-jw-s${z.anlass === 'fehler' ? 'f' : z.staerke}${lang ? ' lr-jw-lang' : ''}`, 'data-spruch': z.id,
    'aria-label': `Sticker: ${z.sticker}. Tippen für die Bedeutung.`, onclick: (ev) => { ev.stopPropagation(); ev.preventDefault(); lernJwBedeutung(z, b); } },
    el('span', { class: 'lr-jw-text' }, z.sticker), el('i', { class: 'lr-jw-frage', 'aria-hidden': 'true' }, '?'));
  return b;
}
// Platzhalter, der sich füllt, sobald die Wortliste da ist (ein Zug je Ansicht)
function lernJwPlatz(kindId, anlass, art = 'szene', zieh = null) {
  const ziehen = () => lernJwStickerEl(zieh ? zieh() : lernJwZiehen(kindId, anlass), art);
  if (lernJwDaten) return ziehen();
  const platz = el('span', { class: 'lr-jw-platz lr-jw-platz-' + art });
  lernJwLaden().then(() => { if (!platz.parentNode) return; const s = ziehen(); if (s) { s.classList.add(...[...platz.classList].filter((c) => !c.startsWith('lr-jw-platz'))); platz.replaceWith(s); } else platz.remove(); }); // WK: Klassen wie „lr-jw-ecke“ (KJ 2 S1) bleiben, auch wenn die Wortliste erst nach dem Zeichnen kommt
  return platz;
}

// ---------- Bau-Auftrag AB-A (20.11.): Abschluss nach Etappe, Flug und Ort (Kinderansicht, Entwurf 2 des Gestalters) ----------
// Vorgabe: inhalte/pruefung/kind/abschluss/umsetzung.md und entwurf/abschluss.html. Server-Felder aus AB-S (landung, kann, kurz, sterne_flug, naechster_flug …).
// Ganzer Bildschirm über der Seite (kein Scrollen auf 400 × 780), Bewegung nur CSS (≤ 1,8 s), Antippen beendet sie, „weniger Bewegung“ zeigt sofort den Endzustand.
const LERN_FLIEGER = '<svg viewBox="0 0 120 50" aria-hidden="true"><g fill="#fff"><path d="M12 21 L100 19 Q118 25 100 31 L12 29 Q6 25 12 21z"/><path d="M52 22 L36 0 L46 0 L74 22z M52 28 L36 50 L46 50 L74 28z"/><path d="M16 22 L8 8 L15 8 L28 22z M16 28 L8 42 L15 42 L28 28z"/></g></svg>';
const lernGrafik = (html, cls) => { const d = el('div', { class: cls, 'aria-hidden': 'true' }); d.innerHTML = html; return d; }; // nur feste Grafiken, keine Daten
const lernZufall = (a, b) => a + Math.random() * (b - a);
function lernAbschlussZu() { document.querySelectorAll('.lr-abschluss').forEach((x) => x.remove()); document.documentElement.classList.remove('lr-abschluss-offen'); }
window.addEventListener('hashchange', lernAbschlussZu); // Zurück-Taste oder ein Link: die Abschluss-Ansicht schließt
// Hülle: fester Vollbild-Rahmen; Antippen der Szene beendet die Bewegung (Endzustand)
function lernAbschlussZeigen(kindObj, inhalt, { label = 'Abschluss' } = {}) {
  lernAbschlussZu();
  const nacht = lernGestaltung(kindObj) === 'nacht';
  const huelle = el('div', { class: 'lr-abschluss ' + (nacht ? 'lr-ab-nacht' : 'lr-ab-hell'), role: 'dialog', 'aria-modal': 'true', 'aria-label': label }, inhalt);
  huelle.addEventListener('click', (ev) => { if (!ev.target.closest('button, a')) huelle.classList.add('lr-ab-fertig'); });
  document.body.append(huelle); document.documentElement.classList.add('lr-abschluss-offen');
  setTimeout(() => huelle.querySelector('.lr-ab-gross')?.focus({ preventScroll: true }), 50);
  lernAbschlussZaehlen(huelle);
  return huelle;
}
const lernWenigBewegung = () => !!window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
function lernAbschlussZaehlen(wurzel) {
  wurzel.querySelectorAll('[data-ziel]').forEach((z) => { const ziel = Number(z.dataset.ziel) || 0; if (lernWenigBewegung()) { z.textContent = lernZahl(ziel); return; }
    const t0 = performance.now(); const lauf = (t) => { if (wurzel.classList.contains('lr-ab-fertig')) { z.textContent = lernZahl(ziel); return; }
      const p = Math.min(1, Math.max(0, (t - t0 - 600) / 1000)); z.textContent = lernZahl(Math.round(ziel * (1 - Math.pow(1 - p, 3)))); if (p < 1) requestAnimationFrame(lauf); };
    z.textContent = '0'; requestAnimationFrame(lauf); });
}
const lernGrossKnopf = (text, klein, attrs) => el(attrs.href ? 'a' : 'button', { ...(attrs.href ? {} : { type: 'button' }), ...attrs, class: 'lr-ab-gross ' + (attrs.class || '') },
  el('span', { class: 'lr-ab-gross-text' }, text), klein ? el('small', {}, klein) : null, el('span', { class: 'lr-ab-pfeil', 'aria-hidden': 'true' }, '›'));
function lernAbzeichen(art) {
  if (art === 'direkt') return lernGrafik('<svg viewBox="0 0 100 110"><polygon points="50,4 94,28 94,80 50,106 6,80 6,28" fill="#FFD23F" stroke="#fff" stroke-width="4"/><text x="50" y="62" text-anchor="middle" font-size="40" font-weight="900" fill="#1B0C3A">⚡</text><text x="50" y="88" text-anchor="middle" font-size="12" font-weight="900" fill="#1B0C3A">DIREKT</text></svg><span>ABZEICHEN</span>', 'lr-ab-abz');
  return lernGrafik('<svg viewBox="0 0 100 110"><circle cx="50" cy="54" r="44" fill="#fff" stroke="#0E9F6E" stroke-width="6"/><path d="M28 56 l14 14 l30 -32" fill="none" stroke="#0E9F6E" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg><span>SAUBER</span>', 'lr-ab-abz');
}
// Fassung der Landung: Server (AB-S) zuerst, sonst gespeicherte Art, sonst „sauber“ (alter Server)
const lernLandungArt = (landung, daten, lz) => (['direkt', 'sauber', 'sturm'].includes(landung?.landung_art) ? landung.landung_art : daten?.landungen?.[lz] || 'sauber');
const lernNeuAngesetzt = (n) => (!n ? '' : n === 1 ? ', einmal neu angesetzt' : n === 2 ? ', zweimal neu angesetzt' : ', mehrmals neu angesetzt');
// „Du kannst jetzt …“: Text aus AB-I, sonst „Kurz gesagt“, sonst der Etappen-Titel
function lernKannText(e, landung, daten) {
  const t = landung?.kann || daten?.kann?.[e.lernziel];
  if (t) return String(t).replace(/\.$/, '') + '.';
  if (e.regel) return lernKurzGesagt(e.regel);
  return e.titel;
}
// 1. Etappe gelandet – drei Fassungen
function lernAbschlussEtappe({ e, nr, von, landung, daten, sterne, knopf, knobel, kind }) {
  const art = lernLandungArt(landung, daten, e.lernziel);
  const wieder = art === 'sauber' && !!landung?.wieder_gelandet;
  const ziel = landung?.ziel || e.ziel || 6, folge = landung?.folge_ziel || e.folgeZiel || Math.min(3, ziel);
  const kopf = el('div', { class: 'lr-ab-oben' }, `ETAPPE ${nr} VON ${von} · ${String(e.titel || '').toUpperCase()}`);
  let szene;
  if (art === 'direkt') {
    const funken = el('div', { class: 'lr-ab-funken', 'aria-hidden': 'true' }, ...Array.from({ length: 22 }, () => el('i', { style: `left:${lernZufall(10, 80).toFixed(1)}%;top:${lernZufall(18, 55).toFixed(1)}%;--dx:${lernZufall(-120, 120).toFixed(0)}px;--dy:${lernZufall(-120, 80).toFixed(0)}px;animation-delay:${lernZufall(0.5, 0.9).toFixed(2)}s` })));
    szene = el('div', { class: 'lr-ab-szene' },
      lernGrafik('<svg viewBox="0 0 500 120" preserveAspectRatio="none"><path class="lr-ab-spur" d="M0 110 C 160 100, 300 50, 440 26" fill="none" stroke="#FFE7A3" stroke-width="5" stroke-linecap="round" opacity=".85"/></svg>', 'lr-ab-jet'),
      lernGrafik(LERN_FLIEGER, 'lr-ab-jetflz'), funken, kopf,
      el('h2', { class: 'lr-ab-titel' }, 'Direktflug'),
      el('div', { class: 'lr-ab-riesig' }, `${ziel}/${ziel}`, el('small', {}, 'AUF ANHIEB')),
      el('p', { class: 'lr-ab-unter' }, 'Kein Fehler, kein Tipp, kein Umweg.'), lernAbzeichen('direkt'));
  } else if (art === 'sauber') {
    szene = el('div', { class: 'lr-ab-szene' }, kopf,
      el('h2', { class: 'lr-ab-titel' }, wieder ? 'Wieder gelandet' : 'Saubere Landung'),
      el('div', { class: 'lr-ab-chips' }, landung?.bordkarten ? el('span', {}, `${landung.bordkarten} Bordkarten`) : null,
        el('span', {}, `${landung?.eigene_loesungen ?? e.eigene ?? ziel} selbst gelöst`), el('span', {}, `${folge} in Folge`)),
      lernAbzeichen('sauber'),
      lernGrafik('<svg viewBox="0 0 400 150" preserveAspectRatio="none"><polygon points="150,0 250,0 400,150 0,150" fill="#3C4A57"/><polygon points="196,0 204,0 212,30 188,30" fill="#fff"/><polygon points="186,50 214,50 222,85 178,85" fill="#fff"/><polygon points="172,110 228,110 238,150 162,150" fill="#fff"/></svg>', 'lr-ab-bahn'),
      lernGrafik(LERN_FLIEGER, 'lr-ab-landeflz'));
  } else {
    szene = el('div', { class: 'lr-ab-szene' },
      lernGrafik('<svg viewBox="0 0 400 400" preserveAspectRatio="none"><g fill="#1A1633" opacity=".9"><ellipse cx="60" cy="120" rx="120" ry="50"/><ellipse cx="220" cy="90" rx="140" ry="55"/><ellipse cx="380" cy="140" rx="110" ry="50"/></g><g fill="#2E2659" opacity=".85"><ellipse cx="120" cy="210" rx="150" ry="45"/><ellipse cx="330" cy="230" rx="120" ry="40"/></g><path d="M372 250 L350 300 L366 300 L342 360" fill="none" stroke="#FFE68A" stroke-width="5" stroke-linejoin="round" opacity=".9"/></svg>', 'lr-ab-wolken'),
      el('div', { class: 'lr-ab-blitz', 'aria-hidden': 'true' }), el('div', { class: 'lr-ab-strahl', 'aria-hidden': 'true' }), kopf,
      el('h2', { class: 'lr-ab-titel' }, 'Sturmflug gemeistert'),
      // 1c: keine Fehlerzahl – nur Bordkarten, „neu angesetzt“ und die Folge am Ende
      el('p', { class: 'lr-ab-unter' }, `${landung?.bordkarten ? `${landung.bordkarten} Bordkarten` : 'Viele Bordkarten'}${lernNeuAngesetzt(landung?.stufe_gesenkt)} – und nicht abgedreht. Am Ende ${folge} in Folge richtig.`),
      el('span', { class: 'lr-ab-ausdauer' }, '⚡ AUSDAUER-ABZEICHEN'), lernGrafik(LERN_FLIEGER, 'lr-ab-sturmflz'));
  }
  const leise = art === 'direkt' ? ['Neues Abzeichen im Reisepass: ', el('b', {}, 'Direktflug'), '. In 1 Lerntag kommt die Etappe kurz zur Wiederholung.']
    : art === 'sauber' ? ['In 1 Lerntag kommt die Etappe kurz zur Wiederholung.'] : ['Das war die schwerste Strecke – und du bist angekommen. In 1 Lerntag kommt die Etappe kurz wieder.'];
  // JW: ein Sticker unten rechts in der Szene – Stärke nach dem Ergebnis (Direkt 3, sauber 2, wieder gelandet 1, Sturm 2 mit Ausdauer-Wörtern)
  szene.classList.add('lr-jw-mit'); szene.append(lernJwPlatz(kind, art === 'direkt' ? 'landung_direkt' : art === 'sturm' ? 'landung_sturm' : wieder ? 'landung_leicht' : 'landung_sauber'));
  const blatt = el('div', { class: 'lr-ab-blatt' },
    el('div', { class: 'lr-ab-kann' }, el('b', {}, 'Du kannst jetzt'), lernKannText(e, landung, daten)),
    el('div', { class: 'lr-ab-zeile' }, el('span', { class: 'lr-ab-sterne' }, `★ +${lernZahl(sterne || 0)}`),
      knobel ? el('button', { type: 'button', class: 'lr-ab-knobel-link', onclick: knobel }, 'Knobel-Bordkarte – für Profis') : null), // nur beim Sturmflug, klein
    lernLandungsBonus(landung, art), // FP: unter der großen Zahl, über dem Knopf
    el('p', { class: 'lr-ab-leise' }, ...leise),
    knopf,
    el('a', { class: 'lr-ab-pause', href: `#/reise/${kind}` }, 'Pause – zur Abflugtafel'));
  return el('div', { class: `lr-ab-app lr-ab-${art} lr-ab-anim lr-abschluss-etappe`, 'data-art': art }, szene, blatt);
}
// FP (Vorgabe „faire Punkte“ 1): Landungs-Bonus als Kachel im Blatt der Etappen-Einblendung – eigene Wörter, nicht „Direktflug“.
// Beim Sturmflug nie eine Fehlerzahl. Fehlt landung.bonus (alter Server, gesetzte Etappe), keine Kachel.
function lernLandungsBonus(landung, art) {
  const b = Number(landung?.bonus); if (!landung || !Number.isFinite(b) || !b || !landung.stufe) return null;
  const f = Number(landung.fehler) || 0;
  const zeile2 = landung.stufe === 'ohne' ? 'ohne Fehler gelandet' : landung.stufe === 'wenig' && art !== 'sturm' ? `mit ${f} ${f === 1 ? 'Fehler' : 'Fehlern'} gelandet` : 'gelandet – geschafft!';
  return el('div', { class: 'lr-ab-bonus lr-ab-bonus-' + landung.stufe, role: 'status', 'aria-label': `Landungs-Bonus plus ${b} Sterne, ${zeile2}` },
    landung.stufe === 'ohne' ? el('span', { class: 'lr-ab-bonus-funken', 'aria-hidden': 'true' }, el('i', {}, '✦'), el('i', {}, '✦'), el('i', {}, '✦')) : null,
    el('span', { class: 'lr-ab-bonus-stern', 'aria-hidden': 'true' }, '★'),
    el('span', { class: 'lr-ab-bonus-text' }, el('b', {}, 'Landungs-Bonus'), el('small', {}, zeile2)),
    el('span', { class: 'lr-ab-bonus-zahl' }, '+', el('span', { 'data-ziel': String(b) }, lernZahl(b)), ' ★'));
}
// FP (Vorgabe 3) / FP-S 3: einmaliger Hinweis nach der Nachbuchung – „Super ›“ quittiert beim Server
// (schule_landung_nachbuchung_gesehen → gesehen_am, gilt auf allen Geräten); localStorage nur als Rückfall
function lernNachbuchungHinweis(d) {
  const n = d.landungNachbuchung; const s = Number(n?.sterne || 0); if (!s || n.gesehen_am) return null;
  const schl = `lern.fpnach.${d.kind.id}.${n.am || ''}`;
  try { if (localStorage.getItem(schl)) return null; } catch { /* zeigen */ }
  const quittieren = () => {
    try { localStorage.setItem(schl, '1'); } catch { /* egal */ }
    n.gesehen_am = n.gesehen_am || new Date().toISOString(); karte.remove();
    lernCall('schule_landung_nachbuchung_gesehen', { lernender_id: d.kind.id })
      .then((r) => { if (r?.gesehen_am) n.gesehen_am = r.gesehen_am; }).catch(() => { /* Rückfall: Gerät */ });
  };
  const karte = el('section', { class: 'lr-karte-box lr-fp-geschenk', role: 'status' },
    el('span', { class: 'lr-ab-bonus-funken', 'aria-hidden': 'true' }, el('i', {}, '✦'), el('i', {}, '✦'), el('i', {}, '✦')),
    el('b', {}, '★ Geschenk für deine Landungen'),
    el('p', {}, 'Für deine bisherigen Landungen gibt es nachträglich ', el('b', {}, `+${lernZahl(s)} ★`), ' Landungs-Bonus.'),
    el('button', { type: 'button', class: 'lr-knopf lr-knopf-klein', onclick: quittieren }, 'Super ›'));
  return karte;
}
// 2. Flug geschafft (Bildschirm 1)
function lernAbschlussFlug({ ctx, r, weiter, testAnsehen }) {
  const et = Array.isArray(r.etappen) && r.etappen.length ? r.etappen
    : (ctx.daten?.inhalt?.etappen || []).map((x) => ({ lernziel: x.lernziel, titel: x.titel, kann: ctx.daten?.kann?.[x.lernziel] || null }));
  const farben = ['#FFD23F', '#FF6B6B', '#4ADE80', '#60A5FA', '#F472B6', '#fff'];
  const fl = r.flug || {};
  const verbessert = (ctx.daten?.stand || []).filter((s) => s.status === 'korrigiert').length;
  const summe = r.sterne_flug?.summe;
  return el('div', { class: 'lr-ab-app lr-ab-flug lr-ab-anim lr-abschluss-flug' },
    el('button', { type: 'button', class: 'lr-ab-skip', onclick: weiter }, 'Überspringen ›'),
    el('div', { class: 'lr-ab-szene lr-jw-mit' },
      el('div', { class: 'lr-ab-konfetti', 'aria-hidden': 'true' }, ...Array.from({ length: 36 }, (_, i) => el('i', { style: `left:${lernZufall(0, 100).toFixed(1)}%;background:${farben[i % farben.length]};animation-delay:${lernZufall(0, 0.4).toFixed(2)}s` }))), // höchstens 1,8 s
      el('div', { class: 'lr-ab-oben' }, [ctx.rkFlug?.land || fl.ort || ctx.ort?.stadt, fl.flug?.nr && fl.flug?.von ? `FLUG ${fl.flug.nr} VON ${fl.flug.von}` : null, fl.titel || ctx.titelKurz].filter(Boolean).join(' · ').toUpperCase()),
      el('h2', { class: 'lr-ab-titel' }, 'Flug geschafft'),
      el('div', { class: 'lr-ab-ringe', role: 'img', 'aria-label': `${et.length} von ${et.length} Etappen gelandet` }, ...et.map((_, i) => el('i', { style: `animation-delay:${(0.5 + i * Math.min(0.06, 0.9 / Math.max(1, et.length))).toFixed(2)}s` }))),
      el('div', { class: 'lr-ab-zaehler' }, summe !== undefined && summe !== null ? [el('span', { 'data-ziel': String(summe) }, lernZahl(summe)), ' ★'] : null,
        el('small', {}, [summe !== undefined && summe !== null ? 'Sterne in diesem Flug' : null, `Test ${r.richtig} von ${r.gesamt}${verbessert ? `, ${verbessert} verbessert` : ''}`].filter(Boolean).join(' · '))),
      lernJwPlatz(ctx.kind, 'flug_geschafft')), // JW: nach dem Konfetti
    el('div', { class: 'lr-ab-blatt' },
      el('div', { class: 'lr-ab-kann' }, el('b', {}, `Das kannst du jetzt – ${et.length} Etappen`)),
      el('div', { class: 'lr-ab-kannliste' }, ...et.map((x) => el('div', {}, x.kann || x.titel))),
      el('p', { class: 'lr-ab-leise' }, el('b', {}, 'Damit es bleibt: '), 'Jede Etappe kommt in den nächsten Wochen ein paar Mal kurz wieder – je eine Bordkarte.'),
      el('div', { class: 'lr-ab-wdh' }, ...['nach 1 Lerntag', '3', '7', '14', '30'].map((t) => el('span', {}, t))),
      lernGrossKnopf('Weiter zum nächsten Thema', 'Deine neue Bordkarte', { onclick: weiter }),
      el('button', { type: 'button', class: 'lr-ab-pause', onclick: testAnsehen }, 'Test ansehen')));
}
// 3. Ort geschafft (Reisepass-Stempel)
const lernStempelDatum = (d) => `${String(d.getDate()).padStart(2, '0')}.${String(d.getMonth() + 1).padStart(2, '0')}.`;
function lernAbschlussOrt({ ctx, r, stempelNr, weiter }) {
  const fl = r.flug || {}; const ort = ctx.rkFlug?.land || fl.ort || ctx.ort?.stadt || 'Ort'; // WK F3: Land der Karte
  const fluege = r.ort_fluege || [];
  const heute = lernStempelDatum(new Date()); // Teil 9 N1: „20.11.“, nie „20.11..“
  return el('div', { class: 'lr-ab-app lr-ab-ort lr-ab-anim lr-abschluss-ort' },
    el('button', { type: 'button', class: 'lr-ab-skip', onclick: weiter }, 'Überspringen ›'),
    el('div', { class: 'lr-ab-szene' },
      el('div', { class: 'lr-ab-oben' }, stempelNr !== null && stempelNr !== undefined ? `REISEPASS · STEMPEL ${stempelNr}` : 'REISEPASS'),
      el('div', { class: 'lr-ab-passstempel', 'aria-hidden': 'true' }, el('div', {}, el('small', {}, 'GESCHAFFT'), el('b', {}, ort.toUpperCase()), el('em', {}, `${fl.gebiet || ''}${fl.gebiet ? ' · ' : ''}${heute}`))),
      el('h2', { class: 'lr-ab-titel' }, `${ort} ist geschafft`),
      el('p', { class: 'lr-ab-unter' }, `Alle ${fluege.length || 1} ${fluege.length === 1 ? 'Flug' : 'Flüge'} · ★ +${lernZahl(r.ort_sterne || 100)} Ort-Sterne`)),
    el('div', { class: 'lr-ab-blatt' },
      el('div', { class: 'lr-ab-kann' }, el('b', {}, `Deine Flüge in ${ort}`)),
      el('div', { class: 'lr-ab-kannliste' }, ...(fluege.length ? fluege : [{ titel: fl.titel || ctx.titelKurz }]).map((x) => el('div', {}, x.titel))),
      lernGrossKnopf('Weiter: neuer Ort', r.naechster_flug?.ort ? `Deine Bordkarte nach ${r.naechster_flug.ort}` : 'Deine neue Bordkarte', { onclick: weiter }),
      el('a', { class: 'lr-ab-pause', href: `#/reisepass/${ctx.kind}` }, 'Reisepass ansehen')));
}
// WD-6 nach der Vorgabe „abgelegt“ (inhalte/pruefung/kind/abgelegt/umsetzung.md, 4–5): Gold ist die Farbe für „abgelegt“ – nur dafür.
// „Etappe abgelegt“: Handy Blatt von unten, Tablet/Rechner Karte in der Mitte (≤ 520 px), Bordkarte bleibt erkennbar; „Flug abgelegt“: ganzer Bildschirm.
const LERN_SIEGEL = '<svg viewBox="0 0 120 120"><defs><radialGradient id="lrsg" cx="40%" cy="35%"><stop offset="0" stop-color="#FFF3B0"/><stop offset=".55" stop-color="#F2C12E"/><stop offset="1" stop-color="#B88700"/></radialGradient></defs><path d="M60 4l9 9 12-4 4 12 13 2-1 13 10 8-7 11 5 12-12 5-1 13-13 0-6 11-12-5-11 7-8-10-13 1-2-13-12-5 4-12-7-11 10-8-1-13 13-2 4-12 12 4z" fill="url(#lrsg)" stroke="#8A6200" stroke-width="2"/><circle cx="60" cy="60" r="32" fill="none" stroke="#8A6200" stroke-width="2" stroke-dasharray="3 3"/><text x="60" y="56" text-anchor="middle" font-size="18" font-weight="900" fill="#5A3A00">★</text><text x="60" y="74" text-anchor="middle" font-size="12" font-weight="900" fill="#5A3A00">ABGELEGT</text></svg>';
const lernGoldStempel = (ort) => lernGrafik(`<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="#F6D25A" stroke="#8A6200" stroke-width="5" stroke-dasharray="6 4"/><text x="50" y="58" text-anchor="middle" font-size="22" font-weight="900" fill="#5A3A00">${String(ort || '★').slice(0, 3).toUpperCase().replace(/[<>&"]/g, '')}</text></svg>`, 'lr-gold-stempel-klein');
function lernAbschlussEtappeAbgelegt({ etappe, checkin, weiter }) {
  const a = Number(etappe.etappen_abgelegt), n = Number(etappe.etappen); const fort = n > 1 && a >= 1 && a <= n; // Fortschritt des Flugs (Feld-Vorschlag, sonst ohne)
  return el('div', { class: 'lr-ab-app lr-ab-abgelegt lr-ab-abgelegt-klein lr-ab-anim' },
    el('div', { class: 'lr-ab-funken-gold', 'aria-hidden': 'true' }, ...[[-60, -50], [70, -40], [10, -70]].map(([x, y]) => el('i', { style: `--x:${x}px;--y:${y}px` }, '✦'))),
    el('p', { class: 'lr-ab-oben' }, 'ABGELEGT'), // 0.86.3: nicht „für immer“ – nach einem Fehler kommt sie zurück in die Wiederholung
    el('h2', { class: 'lr-ab-titel' }, 'Etappe abgelegt!'),
    el('div', { class: 'lr-ab-ticket' }, el('b', {}, etappe.titel || 'Etappe'), el('small', {}, '5-mal wiederholt, über 30 Lerntage. Raus aus der regelmäßigen Wiederholung – nur noch bei Bedarf zum Auffrischen.'), lernGrafik(LERN_SIEGEL, 'lr-ab-siegel')),
    el('div', { class: 'lr-ab-sternzeile' }, el('span', { class: 'lr-ab-zahl' }, `+${lernZahl(etappe.sterne ?? 30)} ★`), el('span', { class: 'lr-leise' }, 'Sonder-Sterne fürs Ablegen')),
    fort ? el('div', { class: 'lr-ab-flugfort' }, `${etappe.flug || 'Dein Flug'}: `, el('b', {}, `${a} von ${n}`), ` Etappen abgelegt – noch ${n - a}, dann wird der Flug golden.`,
      el('div', { class: 'lr-goldbalken', 'aria-hidden': 'true' }, ...Array.from({ length: n }, (_, i) => el('span', { class: i < a ? 'g' + (i === a - 1 ? ' neu' : '') : '' })))) : null,
    lernGrossKnopf(checkin ? 'Weiter einchecken' : 'Weiter', null, { onclick: weiter }));
}
function lernAbschlussFlugAbgelegt({ flug, etappe, ortGold, nachbarn = [], kindId, checkin, weiter }) {
  const andere = nachbarn.filter((t) => t && t !== flug.titel).slice(0, 2);
  const zeilen = [andere[0], flug.titel, andere[1]].filter((t) => t !== undefined);
  const n = Number(flug.etappen ?? etappe?.etappen) || 0;
  return el('div', { class: 'lr-ab-app lr-ab-gold lr-ab-anim' },
    el('button', { type: 'button', class: 'lr-ab-skip', onclick: weiter }, 'Überspringen ›'),
    el('div', { class: 'lr-ab-szene' }, el('div', { class: 'lr-ab-strahlen', 'aria-hidden': 'true' }),
      el('div', { class: 'lr-ab-oben' }, 'ALLE ETAPPEN ABGELEGT'),
      el('h2', { class: 'lr-ab-gtitel' }, 'Flug abgelegt!'),
      el('p', { class: 'lr-ab-gunter' }, `Alle ${n ? n + ' ' : ''}Etappen von `, el('b', {}, flug.titel || 'deinem Flug'), ' sind abgelegt. Im Reisepass ist der Flug jetzt golden.'),
      el('div', { class: 'lr-ab-pass', 'aria-hidden': 'true' }, el('div', { class: 'lr-ab-pass-seite' }, ...zeilen.map((t) => el('div', { class: 'lr-ab-pass-zeile' + (t === flug.titel ? ' lr-wird-gold' : '') },
        el('span', {}, '✈'), t === flug.titel ? el('b', {}, t) : el('span', {}, t), t === flug.titel ? el('span', { class: 'lr-ab-pass-stern' }, '★') : null))))),
    el('div', { class: 'lr-ab-blatt lr-ab-gblatt' },
      el('div', { class: 'lr-ab-reihe' }, el('span', { class: 'lr-ab-hundert' }, '+', el('span', { 'data-ziel': String(flug.sterne ?? 100) }, lernZahl(flug.sterne ?? 100)), ' ★'),
        el('span', { class: 'lr-ab-leise' }, 'für den ganzen Flug', etappe ? el('br') : null, etappe ? `+${lernZahl(etappe.sterne ?? 30)} ★ für die letzte Etappe` : null)),
      ortGold ? el('div', { class: 'lr-ab-ortgold' }, lernGoldStempel(ortGold.ort), el('span', {}, el('b', {}, 'Und: '), `Alle Flüge ${ortGold.ort ? `in ${ortGold.ort}` : 'an diesem Ort'} sind abgelegt. Dein Stempel ist jetzt golden!`)) : null,
      lernGrossKnopf('Weiter', null, { onclick: weiter }),
      el('a', { class: 'lr-ab-pause', href: `#/reisepass/${kindId}` }, 'Reisepass ansehen')));
}
// Zeigt: Flug abgelegt (dann entfällt „Etappe abgelegt“) oder Etappe abgelegt. Promise, erfüllt nach dem Schließen.
function lernAbgelegtZeigen(kindObj, ab, { checkin = false, nachbarn = [] } = {}) {
  return new Promise((fertig) => {
    if (!ab?.etappe && !ab?.flug) { fertig(); return; }
    const zu = () => { lernAbschlussZu(); fertig(); };
    if (ab.flug) lernAbschlussZeigen(kindObj, lernAbschlussFlugAbgelegt({ flug: ab.flug, etappe: ab.etappe, ortGold: ab.ort_gold ? { ort: ab.ort || ab.flug?.ort || null } : null, nachbarn, kindId: kindObj.id, checkin, weiter: zu }), { label: 'Flug abgelegt' });
    else { const h = lernAbschlussZeigen(kindObj, lernAbschlussEtappeAbgelegt({ etappe: ab.etappe, checkin, weiter: zu }), { label: 'Etappe abgelegt' }); h.classList.add('lr-abschluss-klein'); }
  });
}
// 2/3. Bordkarte zum nächsten Flug (oder: nichts mehr im Plan)
function lernAbschlussBordkarte({ ctx, r }) {
  const n = r.naechster_flug; const alt = r.flug || {};
  const kindName = String(ctx.kindObj?.name || 'Du').toUpperCase();
  if (!n) return el('div', { class: 'lr-ab-app lr-ab-neu lr-ab-anim lr-abschluss-bordkarte' },
    el('div', { class: 'lr-ab-oben' }, 'GESCHAFFT'),
    el('div', { class: 'lr-ab-pass' }, el('div', { class: 'lr-ab-pass-kopf' }, el('span', {}, 'BORDKARTE'), el('span', {}, kindName)),
      el('div', { class: 'lr-ab-flugname' }, el('small', {}, 'FLUG'), el('b', {}, 'Kein Ziel')),
      el('p', { class: 'lr-ab-satz' }, 'Alles geschafft, was im Plan steht. Deine Eltern legen fest, wie es weitergeht.')),
    lernSchrittKnopf(ctx.kind, { vorher: { text: 'Zur Reisekarte', klein: null, ziel: `#/reise/${ctx.kind}` } })); // WK 2: steht doch noch etwas an (z. B. zweiter Flug des Platzes) → dorthin
  const nachName = n ? lernFlugName(ctx.kind, { thema_id: n.thema_id || null, einheit_id: n.einheit_id ?? n.id ?? null }, n.ort || '') : ''; // WK F3: Land der Reisekarte
  const wechsel = r.ort_wechsel === true || (r.ort_wechsel !== false && alt.ort && n.ort && alt.ort !== n.ort);
  const ziel = `#/lerneinheit/${ctx.kind}-${n.einheit_id}-erklaeren-1`; // „Boarding“: Erklärung der ersten Etappe
  return el('div', { class: 'lr-ab-app lr-ab-neu lr-ab-anim lr-abschluss-bordkarte' },
    el('div', { class: 'lr-ab-oben' }, wechsel ? 'NEUES THEMA · NEUER ORT' : 'NEUES THEMA'),
    el('div', { class: 'lr-ab-pass' },
      el('div', { class: 'lr-ab-pass-kopf' }, el('span', {}, 'BORDKARTE'), el('span', {}, kindName)),
      wechsel ? el('div', { class: 'lr-ab-route' }, el('div', {}, el('small', {}, 'VON'), el('b', {}, String(ctx.rkFlug?.land || alt.ort || ctx.ort?.stadt || '').toUpperCase())), el('div', { class: 'lr-ab-m', 'aria-hidden': 'true' }, '✈'),
          el('div', { class: 'r' }, el('small', {}, 'NACH'), el('b', {}, String(nachName || '').toUpperCase())))
        : el('div', { class: 'lr-ab-route' }, el('div', {}, el('small', {}, 'ORT'), el('b', {}, String(nachName || '').toUpperCase())), el('div', { class: 'lr-ab-m', 'aria-hidden': 'true' }, '✈'),
          el('div', { class: 'r' }, el('small', {}, 'FLUG'), el('b', {}, `${n.flug?.nr ?? '–'} / ${n.flug?.von ?? '–'}`))),
      el('div', { class: 'lr-ab-flugname' }, el('small', {}, 'FLUG'), el('b', {}, n.titel)),
      n.kurz ? el('p', { class: 'lr-ab-satz' }, n.kurz) : null,
      el('div', { class: 'lr-ab-felder' }, el('div', {}, el('small', {}, 'ETAPPEN'), el('b', {}, String(n.etappen ?? '–'))), el('div', {}, el('small', {}, 'GEBIET'), el('b', {}, n.gebiet || '–')),
        el('div', {}, el('small', {}, 'FLUG'), el('b', {}, `${n.flug?.nr ?? '–'} von ${n.flug?.von ?? '–'}`))),
      el('div', { class: 'lr-ab-riss', 'aria-hidden': 'true' }), el('div', { class: 'lr-ab-pass-unten' }, el('div', { class: 'lr-ab-strich', 'aria-hidden': 'true' }), el('b', {}, 'GATE: ERKLÄRUNG'))),
    // WK 2 (A2): der Knopf führt in die erste offene Etappe des nächsten Flugs laut Ständen (auch der zweite Flug desselben Plan-Platzes)
    lernSchrittKnopf(ctx.kind, { vorher: { text: wechsel ? `Abflug nach ${nachName || n.ort}` : `Boarding: ${n.titel}`, klein: 'Zuerst kommt die Erklärung', ziel } }),
    el('a', { class: 'lr-ab-pause', href: `#/reise/${ctx.kind}` }, 'Später – zur Abflugtafel'));
}
// Ablauf nach bestandenem Flug-Test: Flug → (Ort) → Bordkarte
async function lernAbschlussFlugStart(ctx, r) {
  // 0.83.3 (Nachtrag 888): meldet der Server nur ort_geschafft (flug_geschafft false), war „Flug geschafft“ schon – direkt Ort-Stempel und Bordkarte
  let schritt = ('flug_geschafft' in r && !r.flug_geschafft && r.ort_geschafft) ? 'ort' : 'flug'; let huelle = null; let stempelNr = null;
  if (r.ort_geschafft) { try { const k = await lernCall('schule_konto', { lernender_id: ctx.kind }); stempelNr = (k?.konto || k)?.stempel ?? null; } catch { /* ohne Nummer */ } }
  const zeige = () => {
    const weiter = () => { schritt = schritt === 'flug' && r.ort_geschafft ? 'ort' : 'karte'; zeige(); };
    const inhalt = schritt === 'flug' ? lernAbschlussFlug({ ctx, r, weiter, testAnsehen: () => { lernAbschlussZu(); window.scrollTo(0, 0); } })
      : schritt === 'ort' ? lernAbschlussOrt({ ctx, r, stempelNr, weiter }) : lernAbschlussBordkarte({ ctx, r });
    if (r.naechster_flug === undefined && schritt === 'karte') { lernAbschlussZu(); route('reise', ctx.kind); return; } // alter Server: keine Bordkarte
    huelle = lernAbschlussZeigen(ctx.kindObj, inhalt, { label: schritt === 'flug' ? 'Flug geschafft' : schritt === 'ort' ? 'Ort geschafft' : 'Neues Thema' });
  };
  if (ctx.live()) zeige();
  return huelle;
}
// Teil 4 Punkt 5e: Sind alle Pflicht-Etappen gelandet und fehlt nur der Test (oder ein Nachtragstest), kommt der Test von selbst.
function lernTestFaellig(daten, etappen) {
  const pflicht = etappen.filter((e) => !e.extra);
  if (!pflicht.length || pflicht.some((e) => !e.fertig) || daten.ohne_test) return null;
  if (daten.laufender_test) return { art: 'laeuft', n: pflicht.length };
  if (!daten.blocktest_fertig) return { art: 'test', n: pflicht.length };
  const neu = lernNeueEtappen(daten.stand); return neu ? { art: 'nachtrag', n: neu } : null;
}
// Was für den Stempel des Ortes nach diesem Flug noch fehlt (schule_konto.orte: themen, erledigt)
function lernStempelRest(ctx) {
  const o = (ctx.konto?.orte || []).find((x) => x.block_id === ctx.ort?.block_id); const stadt = ctx.ort?.stadt || 'diesem Ort';
  if (!o || !o.themen) return null;
  const rest = Math.max(0, o.themen - (o.erledigt || 0) - 1);
  return rest ? `Für den Stempel von ${stadt} fehlen danach noch ${rest} ${rest === 1 ? 'Flug' : 'Flüge'}.` : `Danach gibt es den Stempel von ${stadt}.`;
}
function lernTestAufforderung(ctx, tf) {
  const basis = ctx.basis;
  return el('section', { class: 'lr-karte-box lr-test-auf' },
    el('a', { class: 'lr-knopf lr-jetzt-test', href: `${basis}-test` }, tf.art === 'nachtrag' ? 'Test zu den neuen Etappen ›' : tf.art === 'laeuft' ? 'Angefangenen Test weitermachen ›' : 'Jetzt zum Test ›'),
    el('p', { class: 'lr-leise' }, tf.art === 'nachtrag' ? `${tf.n} ${tf.n === 1 ? 'Bordkarte' : 'Bordkarten'}, ohne Tipps – eine je neuer Etappe.` : `${tf.n} ${tf.n === 1 ? 'Bordkarte' : 'Bordkarten'}, ohne Tipps. Bestehst du ihn, ist der Flug geschafft.`),
    lernStempelRest(ctx) ? el('p', { class: 'lr-leise lr-stempel-rest' }, lernStempelRest(ctx)) : null,
    el('a', { class: 'lr-textlink lr-pause', href: `#/reise/${ctx.kind}` }, 'Pause – zur Abflugtafel'));
}
function lernTestTeil(ctx, etappen) {
  const { daten } = ctx;
  const pflicht = etappen.filter((e) => !e.extra);
  const offen = pflicht.filter((e) => !e.fertig).length;
  if (!pflicht.length) return el('p', { class: 'lr-gesperrt' }, 'Dieser Flug wird gerade vorbereitet. Schau bald wieder vorbei.');
  if (daten.laufender_test) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Angefangenen Test weitermachen');
  // I-5 (W177): nur an „Flug-Test abgeschlossen und neue offene Pflicht-Etappen“ gebunden, neutraler Text
  if (daten.blocktest_fertig && lernNeueEtappen(daten.stand)) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Test zu den neuen Etappen');
  if (daten.blocktest_fertig) return el('a', { class: 'lr-zeile', href: `${ctx.basis}-test` }, el('span', { class: 'lr-zeile-icon' }, lernIcon(LI.stempel, 22)),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, 'Test, Verbessern und Nachtests'), el('small', {}, daten.nachtest?.grund === 'faellig' ? 'Ein Nachtest ist jetzt dran.' : 'Hier siehst du, was als Nächstes kommt.')), lernIcon(LI.pfeil, 20));
  if (!offen) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Alle Etappen sitzen – Test starten');
  return el('p', { class: 'lr-gesperrt' }, lernIcon('M6 11h12v10H6z|M9 11V8a3 3 0 0 1 6 0v3', 20), `Der Test kommt, wenn alle Etappen sitzen (noch ${offen}).`);
}

function lernThemaSeite(ctx, etappen, start, karteNr, { einsteigen = false } = {}) {
  const { daten, kindObj: kind } = ctx;
  const neu = lernNeu(kind); const ortCode = String(ctx.ort.stadt || 'Thema').toUpperCase();
  // Tabs schreiben die Adresse per replaceState um; die Ansicht bleibt gültig, bis neu gerendert wird.
  const gen = renderGeneration; ctx.live = () => gen === renderGeneration;
  const pflicht = etappen.filter((e) => !e.extra);
  const sitzen = () => pflicht.filter((e) => e.fertig).length;
  // WK F1: ohne Etappen-Nummer die nächste offene Pflicht-Etappe; fällige Wiederholungen laufen über den Check-in bzw. #/wiederholen
  const empfohlen = () => etappen.find((e) => !e.fertig && !e.extra && e.aufgaben.length) || etappen.find((e) => !e.fertig && e.aufgaben.length) || etappen.find((e) => e.faellig) || etappen[0];
  const fehlerKarten = etappen.filter((e) => e.fehler);
  // Neue Lernkarte (noch nie geübt): erst die Erklärung zeigen, dann die Aufgaben („Jetzt du ›“).
  const erklGesehen = new Set(); // Karten, deren Erklärung das Kind in dieser Sitzung schon vor sich hatte
  const lernTypGesehen = {}; // F: je Etappe die Typen, die in dieser Sitzung schon dran waren
  const lernMischZaehler = {}; // W176 Teil 3
  const neuKarte = (e) => !!e && !e.fertig && !e.sitzt && !e.faellig && !e.serie && !!e.regel && !erklGesehen.has(e.lernziel) && !e.aufgaben.some((x) => x.versuche || x.geloest);
  const erstErklaeren = (e) => { offeneKarte = e; zeichneErklaeren(); zeige('erklaeren'); adresse(e, false); window.scrollTo(0, 0); };
  if (start === 'ueben' && !karteNr && neuKarte(empfohlen())) { karteNr = empfohlen().nr; start = 'erklaeren'; }
  else if (start === 'ueben' && karteNr && einsteigen && neuKarte(etappen[karteNr - 1])) start = 'erklaeren'; // WK F1: „Weiter in ‹Stadt›“ zu einer neuen Etappe – erst ihre Erklärung (wie bisher beim Einsteigen)
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
          k.regel ? el('span', { class: 'lr-kachel-kurz' }, el('small', {}, 'Kurz gesagt: '), lernMathe(lernKurzGesagt(k.regel))) : null))))),
        lernTestTeil(ctx, etappen),
        ctx.leitung ? lernAendern({ einheit_id: ctx.einheit, lernender_id: ctx.kind }, { bezug: 'flug', wo: `Flug „${ctx.titelKurz}“` }) : null);
      return;
    }
    const naechste = etappen[etappen.indexOf(e) + 1] || null;
    lernErsetze(panels.erklaeren,
      el('button', { type: 'button', class: 'lr-textlink lr-zur-uebersicht', onclick: () => { offeneKarte = null; adresse(null, false); zeichneErklaeren(); window.scrollTo(0, 0); } }, '‹ Übersicht'),
      el('article', { class: 'lr-karte-box lr-lernkarte' },
        el('div', { class: 'lr-lernkarte-kopf' }, el('h3', {}, `${e.nr} · ${ctx.stadtVon?.(e) ? ctx.stadtVon?.(e) + ' · ' : ''}${e.titel}`), el('span', { class: 'lr-lk-status' }, lernPunkte(e), el('small', {}, lernKartenStatus(e)))),
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
      el('h3', {}, `${e.nr} · ${ctx.stadtVon?.(e) ? ctx.stadtVon?.(e) + ' · ' : ''}${e.titel}`), el('div', { class: 'lr-fehler' }, el('b', {}, 'Achtung: '), ...lernMarkiert(e.fehler)),
      el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { offeneKarte = e; zeichneErklaeren(); zeige('erklaeren'); adresse(e, false); } }, 'Erklärung ansehen'))) : [el('p', { class: 'lr-leise' }, 'Für diesen Flug sind noch keine typischen Fehler eingetragen.')]),
    versucht.length ? el('section', { class: 'lr-karte-box' }, el('h3', {}, `Hat bei dir noch nicht geklappt (${versucht.length})`),
      el('ul', { class: 'lr-meinefehler' }, ...versucht.slice(0, 8).map(({ e, a }) => el('li', {}, el('span', {}, lernMathe(a.frage?.text || '')),
        el('button', { type: 'button', class: 'lr-knopf-zweit lr-knopf-klein', onclick: () => zeige('ueben', { karte: e }) }, 'Üben'))))) : null);

  // --- Üben: eine Lernkarte, Aufgaben nacheinander; Erklärung klappt an der Aufgabe auf
  let aktKarte = null, stufe = 0;
  let gezeichnet = null, weiterueben = false; // Teil 4 Punkt 5b: „Trotzdem weiterüben“ gilt nur für die gerade offene Etappe
  const uebenOeffnen = (karte) => {
    if (karte && karte !== aktKarte) { aktKarte = karte; stufe = 0; weiterueben = false; }
    if (!aktKarte) aktKarte = (karteNr && etappen[karteNr - 1]) || empfohlen();
    if (gezeichnet !== aktKarte) zeichneUeben(); // sonst bleibt Bordkarte samt Rückmeldung stehen
  };
  const zeichneUeben = () => {
    const e = aktKarte; gezeichnet = e;
    // NB-App: wieder offene Etappe (schule_konto.nachbessern) – Folge x von 3; KJ 2 S3: die Nachbessern-Leiste ersetzt den Zähler der Etappen-Leiste
    const nbE = (ctx.konto?.nachbessern || []).find((x) => Number(x.einheit_id) === Number(ctx.einheit) && x.lernziel === e.lernziel) || null;
    const nb = nbE ? { folge: Math.max(0, Number(nbE.folge) || 0), noetig: Number(nbE.folge_noetig) || 3 } : null;
    const nbLeiste = el('div', { class: 'lr-nb-leiste', role: 'status' });
    const nbZeichnen = () => { if (!nb) return; lernErsetze(nbLeiste, el('b', {}, '↻ NACHBESSERN'), lernNbKreise(Math.min(nb.folge, nb.noetig), nb.noetig), el('span', {}, `${Math.min(nb.folge, nb.noetig)} von ${nb.noetig} in Folge`)); };
    nbZeichnen();
    const mitAufg = etappen.filter((x) => x.aufgaben.length); const pos = mitAufg.indexOf(e);
    const wechsel = (d) => el('button', { type: 'button', class: 'lr-pfeilknopf', 'aria-label': d < 0 ? 'Vorige Etappe' : 'Nächste Etappe', disabled: !mitAufg[pos + d],
      onclick: () => { aktKarte = mitAufg[pos + d]; stufe = 0; weiterueben = false; zeichneUeben(); } }, d < 0 ? '‹' : '›');
    const stufenDa = [1, 2, 3].filter((n) => e.aufgaben.some((a) => a.stufe === n));
    const chipsStufe = stufenDa.length > 1 ? el('div', { class: 'lr-chips lr-chips-klein', role: 'group', 'aria-label': 'Stufe' },
      ...[[0, 'alle'], [1, 'leicht'], [2, 'mittel'], [3, 'schwer']].filter(([n]) => !n || stufenDa.includes(n))
        .map(([n, t]) => el('button', { type: 'button', class: stufe === n ? 'on' : '', 'aria-pressed': String(stufe === n), onclick: () => { stufe = n; zeichneUeben(); } }, t))) : null;
    const punkte = el('div', { class: 'lr-lk-punkte' });
    const zeichnePunkte = () => nb ? lernErsetze(punkte, nbLeiste) : e.neueRegel
      // W176: Checkliste statt Punkten; daneben der Zähler „heute selbst gelöst“
      ? lernErsetze(punkte, e.sitzt || e.fertig ? el('small', {}, e.faellig ? 'Gelandet – heute wiederholen: 1 Bordkarte, dann bist du hier fertig' : e.sicher ? 'Sicher! Du kannst trotzdem weiterüben.' : 'Gelandet! Du kannst trotzdem weiterüben.') : lernCheckliste(e),
        el('small', { class: 'lr-heute' }, `heute ${lernHeute(ctx.kind)} ${lernHeute(ctx.kind) === 1 ? 'Aufgabe' : 'Aufgaben'} selbst gelöst`))
      : lernErsetze(punkte, lernPunkte(e, { gross: true }),
        el('small', {}, e.sitzt || e.fertig ? (e.faellig ? 'Sitzt – heute wiederholen: 1 Bordkarte, dann bist du hier fertig' : 'Sitzt! Du kannst trotzdem weiterüben.') : e.serie >= e.ziel && e.schwerNoetig && !e.schwerOk ? 'Fast geschafft: noch eine schwere Bordkarte richtig' : `${Math.min(e.serie, e.ziel)} von ${e.ziel} richtig`));
    zeichnePunkte();
    const flaeche = el('div', { class: 'lr-ueben-flaeche' });
    lernErsetze(panels.ueben, el('div', { class: 'lr-karte-box lr-lk-kopf' }, wechsel(-1),
      el('div', { class: 'lr-lk-mitte' }, el('small', { class: 'lr-leise' }, neu ? `Etappe ${pos + 1}/${mitAufg.length} · ${ctx.stadtVon?.(e) ? ctx.stadtVon?.(e) + ' · ' : ''}${e.titel}` : `Etappe ${pos + 1} von ${mitAufg.length}`), neu ? null : el('b', {}, e.titel), punkte), wechsel(1)), flaeche, chipsStufe);
    // Teil 4 Punkt 5b: Eine gelandete Etappe (nicht fällig) zeigt „Hier bist du fertig ✓“ mit dem nächsten Schritt groß;
    // „Trotzdem weiterüben“ ist klein, und der Weiter-Knopf bleibt über jeder weiteren Bordkarte stehen.
    const nochOffen = etappen.find((x) => x !== e && !x.fertig && x.aufgaben.length && !x.extra) || etappen.find((x) => x !== e && !x.fertig && x.aufgaben.length);
    const fertigHier = (e.sitzt || e.fertig) && !e.faellig;
    // WK 2 (A1/A2): offene Pflicht-Etappe → Flug-Test → nächster Schritt der Reise (Extra-Etappen nur freiwillig, nie als Hauptknopf)
    const schrittKnopf = () => { const nochP = etappen.find((x) => x !== e && !x.fertig && x.aufgaben.length && !x.extra) || null; const tf = nochP ? null : lernTestFaellig(ctx.daten, etappen); const testOffen = !!tf;
      return nochP
        ? el('button', { type: 'button', class: 'lr-knopf lr-weiter-schritt', onclick: () => { if (neuKarte(nochP)) { erstErklaeren(nochP); return; } aktKarte = nochP; stufe = 0; weiterueben = false; zeichneUeben(); window.scrollTo(0, 0); } }, `Nächste Etappe: ${nochP.titel} ›`)
        : testOffen ? el('a', { class: 'lr-knopf lr-weiter-schritt', href: `${ctx.basis}-test` }, tf.art === 'laeuft' ? 'Angefangenen Test weitermachen ›' : tf.art === 'nachtrag' ? 'Test zu den neuen Etappen ›' : 'Jetzt zum Test ›')
          : lernSchrittKnopf(ctx.kind, { gross: false, klasse: 'lr-weiter-schritt' }); }; // WK 2 (A2): direkt in den nächsten Schritt der Reise, nicht zur Karte
    if (fertigHier) {
      const weiterKnopf = schrittKnopf();
      panels.ueben.prepend(el('div', { class: 'lr-karte-box lr-fertig-hier' + (weiterueben ? ' lr-fertig-klein' : '') },
        el('p', {}, el('b', {}, 'Hier bist du fertig ✓')), weiterKnopf,
        weiterueben ? null : el('button', { type: 'button', class: 'lr-textlink lr-trotzdem', onclick: () => { weiterueben = true; zeichneUeben(); } }, 'Trotzdem weiterüben')));
      if (!weiterueben) { flaeche.remove(); chipsStufe?.remove(); return; }
    } else if (!pflicht.some((x) => !x.fertig) && !e.faellig) // alle Etappen sitzen: nicht endlos weiterüben lassen, sondern den Test anbieten
      panels.ueben.prepend(el('div', { class: 'lr-karte-box lr-testbereit' }, el('p', {}, el('b', {}, 'Alle Etappen dieses Flugs sitzen. '), 'Du musst hier nicht weiterüben – als Nächstes kommt der Test.'), lernTestTeil(ctx, etappen)));
    const pool = e.aufgaben.filter((a) => !stufe || a.stufe === stufe);
    const warte = [...pool].sort((a, b) => (a.geloest === b.geloest ? 0 : a.geloest ? 1 : -1) || (a.versuche || 0) - (b.versuche || 0) || (a.stufe || 2) - (b.stufe || 2));
    let sterne = 0, nr = 0, fehlFolge = 0, richtFolge = 0; // richtFolge: JW-Serie 5/10 in Folge richtig; fehlFolge: falsche Bordkarten hintereinander auf dieser Karte (V8)
    const naechsteKarte = etappen.slice(e.nr).find((x) => !x.fertig && x.aufgaben.length) || etappen.find((x) => x !== e && !x.fertig && x.aufgaben.length);
    // NB-App: wieder offene Etappe (schule_konto.nachbessern) – Leiste über der Bordkarte, Folge x von 3; bei 3 in Folge „Sitzt wieder!“ statt der Landung
    const nbFertig = () => { // Bestätigung (kurz, ohne Extra-Sterne): drei Haken, „Sitzt wieder!“, weiter zur nächsten Nachbessern-Etappe bzw. zum nächsten Flug
      const rest = (ctx.konto?.nachbessern || []).filter((x) => x !== nbE); if (ctx.konto) ctx.konto.nachbessern = rest; lernVergessen(ctx.kind);
      const nf = ctx.u ? lernNamenSetzen(lernReiseDaten(ctx.u, ctx.kind))?.naechste : null;
      const knopf = rest.length ? lernGrossKnopf(`Weiter nachbessern: ${rest[0].etappe || rest[0].titel}`, null, { href: lernNbZiel(ctx.kind, rest[0]), onclick: () => lernAbschlussZu() })
        : lernSchrittKnopf(ctx.kind, { vorher: nf ? { text: `Weiter in ${nf.stadt || nf.ort_titel || nf.titel}`, klein: null, ziel: lernUebenZiel(ctx.kind, nf) } : { text: 'Weiter', klein: null, ziel: `#/reise/${ctx.kind}` } }); // WK 2 (A2): Schritt 1–5
      try { history.replaceState(history.state, '', `${ctx.basis}-erklaeren`); } catch { /* egal */ }
      lernAbschlussZeigen(ctx.kindObj, el('div', { class: 'lr-ab-app lr-nb-fertig lr-ab-anim' },
        el('div', { class: 'lr-ab-szene lr-nb-szene lr-jw-mit' },
          el('div', { class: 'lr-ab-oben' }, `↻ NACHBESSERN · ${String(nbE.etappe || e.titel).toUpperCase()}`),
          el('div', { class: 'lr-nb-haken', 'aria-hidden': 'true' }, el('i', {}, '✓'), el('i', {}, '✓'), el('i', {}, '✓')),
          el('h2', { class: 'lr-ab-titel' }, 'Sitzt wieder!'),
          lernJwPlatz(ctx.kind, 'nachbessern')),
        el('div', { class: 'lr-ab-blatt' },
          el('p', {}, `„${nbE.etappe || e.titel}“ in ${ctx.stadtVon?.(e) || nbE.stadt || ctx.ort.stadt || 'deiner Stadt'} ist wieder gelandet.`),
          el('p', { class: 'lr-ab-leise' }, 'In den nächsten Lerntagen fragen wir sie noch ein paar Mal ab.'),
          knopf)), { label: 'Sitzt wieder' });
    };
    // Regel „gelandet“ (W176): Die Stufe steigt mit den eigenen Lösungen – erst leicht, dann mittel, dann schwer – und fällt erst nach 2 Fehlern in Folge um 1.
    let letzte = null;
    const mischZaehler = (lernMischZaehler[e.lernziel] ||= { n: 0 }); // W176: wie viele Mischkarten in dieser Etappe schon kamen (jede 3. aus einem älteren Flug)
    const gesehenTyp = (lernTypGesehen[e.lernziel] ||= new Set()); // F: Typen, die in dieser Etappe schon dran waren
    const waehleStufe = () => { if (!stufe && !e.sitzt && !e.fertig) lernWaehleBordkarte(warte, e, letzte, gesehenTyp); };
    // W176 Teil 3: Mischkarten – jede n-te Bordkarte stammt aus einer anderen, schon gelandeten Etappe (Server: schule_einheit_lesen.mischkarten, misch_jede, misch_ab)
    // 0.86.2 (Fehler Mischkarten 22.11.): Eine gezeigte Mischkarte ist für die ganze Sitzung des Flugs verbraucht (ctx.mischGezeigt), nicht je Etappe neu.
    // Ist die Liste leer, holt die App sie einmal neu vom Server (im Hintergrund); danach geht es ohne Mischkarte weiter.
    const mischRest = () => (ctx.daten.mischkarten || []).filter((x) => !(x.einheit_id === ctx.einheit && x.lernziel === e.lernziel) && !x.bonus && !ctx.mischGezeigt.has(x.id));
    const mischDran = () => {
      const jede = Number(ctx.daten.misch_jede || 0); const rest = mischRest();
      if (!rest.length && jede && !stufe && !ctx.mischNachgeladen) lernMischNachladen(ctx);
      const k = lernMischWahl(rest, { nr: nr + 1, jede, ab: Number(ctx.daten.misch_ab || 3), gelandet: etappen.filter((x) => x.sitzt).length, aus: !!stufe, zaehler: mischZaehler });
      if (k) ctx.mischGezeigt.add(k.id);
      return k;
    };
    const zeigeAufgabe = (fest) => {
      if (fest !== true) waehleStufe();
      const misch = fest !== true ? mischDran() : null;
      const a = misch || warte[0]; if (!misch) { letzte = a || null; if (a?.typ) gesehenTyp.add(a.typ); }
      if (!a) { lernErsetze(flaeche, el('p', { class: 'lr-leise' }, 'Für diese Auswahl gibt es keine Bordkarten.')); return; }
      nr++;
      const auf = lernAufgabe(a, null, { tasten: neu, stellen: neu && kind.klasse && kind.klasse <= 6 }); let hilfe = 0; const dock = el('div', { class: 'lr-dock' }); let cid = lernCid();
      // V2: zweiter Versuch vor der Lösung (nicht bei Ja/Nein-Auswahl – dort wäre der zweite Versuch die Lösung)
      let anlauf = 1; const zweiteChance = !(a.antworttyp === 'auswahl' && (a.antworten || []).length <= 2);
      const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
      const hilfeBox = el('div', { class: 'lr-hilfebox' });
      const tipp = a.tipp ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { hilfe = 1; tipp.remove(); lernAnhaengen(hilfeBox, el('p', { class: 'lr-tipp' }, el('b', {}, 'Tipp: '), lernMathe(a.tipp), el('small', {}, ' (zählt nicht als eigene Lösung; unterbricht deine Folge nicht)'))); } }, 'Tipp') : null;
      // Vorgabe 16.11.: Beim Üben steht nur die Aufgabe. Darüber ein gut sichtbarer Link „Erklärung ansehen“ (am Rechner klappt sie links daneben auf).
      const breit = neu && !!e.regel && !!window.matchMedia?.('(min-width: 900px)').matches;
      const erkl = e.regel && !a.misch ? el('button', { type: 'button', class: 'lr-erkl-link', 'aria-expanded': 'false', onclick: () => {
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
          const r = await lernCall('schule_uebung_pruefen', { lernender_id: ctx.kind, aufgabe_id: a.id, antwort: w, client_id: cid, hilfe, ...(zweiteChance ? { anlauf } : {}), ...(a.misch ? { misch: true, aktuell_einheit: ctx.einheit, aktuell_lernziel: e.lernziel } : {}) }); // H10: Server prüft die Mischkarte
          if (!ctx.live()) return;
          if (!r.format_ok) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, r.hinweis)); pruefen.disabled = false; return; }
          if (r.nochmal) { // 1. Fehler: keine Lösung, nur ein Hinweis – die Eingabe bleibt änderbar
            anlauf = 2; cid = lernCid(); pruefen.disabled = false;
            lernErsetze(meldung, el('div', { class: 'lr-rueck lr-rueck-nochmal' }, el('b', {}, 'Noch nicht – du hast einen zweiten Versuch.'),
              r.verletzt ? [lernBedingungRueck(r), el('p', {}, 'Ändere deine Zahlen.')]
                : el('p', {}, LERN_GRUND[r.grund] || (a.tipp ? ['Tipp: ', ...lernMathe(a.tipp)] : 'Lies die Bordkarte noch einmal genau und prüfe deine Rechnung.'))));
            if (!r.verletzt && !LERN_GRUND[r.grund] && a.tipp) tipp?.remove();
            meldung.scrollIntoView?.({ block: 'nearest', behavior: 'smooth' });
            return;
          }
          auf.sperren(); a.loesung = r.loesung; if (!a.misch) warte.shift(); a.versuche = (a.versuche || 0) + 1;
          const sterneVor = sterne;
          // 0.86.2: Sterne nur aus der Antwort des Servers (`sterne` = tatsächlich gebucht; sonst `wiederholung.sterne`). Nur bei einer normalen Bordkarte
          // und einem Server ohne `sterne` bleibt die bisherige Anzeige (+10 beim ersten Richtig) – bei Mischkarten zeigt die App dann nichts.
          // FP-S: `sterne` = in diesem Aufruf gebucht (Übung + Wiederholung + Landungs-Bonus + Ablegen). Bei der Bordkarte zählt nur der Teil ohne Bonus und Ablegen –
          // der Landungs-Bonus steht in der Landungs-Einblendung, das Ablegen in seiner Einblendung.
          const gebucht = typeof r.sterne === 'number' ? Math.max(0, r.sterne - Number(r.landung?.bonus || 0) - Number(r.abgelegt?.etappe?.sterne || 0) - Number(r.abgelegt?.flug?.sterne || 0))
            : typeof r.wiederholung?.sterne === 'number' ? r.wiederholung.sterne : null;
          if (a.misch) { if (r.richtig && gebucht) sterne += gebucht; a.geloest = !!r.richtig; } // Mischkarte: nicht zurück in die Warteschlange
          else if (r.richtig) { sterne += gebucht !== null ? gebucht : (!a.geloest && !r.wiederholt ? 10 : 0); a.geloest = true; warte.push(a); }
          else { // V5: gemerkte Lösung zählt nicht – nach einem Fehler kommt eine andere Bordkarte derselben Stufe; dieselbe erst ganz am Ende
            warte.push(a);
            const j = warte.findIndex((x) => x !== a && !x.geloest && (x.stufe || 2) === (a.stufe || 2) && !x.falschHeute);
            if (j > 0) warte.unshift(...warte.splice(j, 1));
            a.falschHeute = true;
          }
          auf.zeigeLoesung(r.loesung); fehlFolge = r.richtig ? 0 : fehlFolge + 1; richtFolge = r.richtig ? richtFolge + 1 : 0;
          // JW: Sticker in der Rückmeldung – Serie 5/10, Wiederholung bestanden (Mischkarte), Fehler nach der Fehler-Regel (1., 3., 5. … nie ab dem 2. in Folge)
          if (r.richtig) lernJwRichtig(ctx.kind);
          const jwAnlass = !r.richtig ? null : a.misch && r.wiederholung?.bestanden ? 'wiederholung' : richtFolge === 10 ? 'serie_10' : richtFolge === 5 ? 'serie_5' : null;
          const jwSticker = r.richtig ? (jwAnlass ? lernJwPlatz(ctx.kind, jwAnlass, 'box') : null) : lernJwPlatz(ctx.kind, 'fehler', 'fehler', () => lernJwFehler(ctx.kind));
          const warSitzt = e.sitzt;
          if (r.karte?.heute_selbst !== undefined) lernHeuteSetzen(ctx.kind, r.karte.heute_selbst, r.karte.heute_tag, r.karte.heute_bis ?? r.heute_bis); else if (r.richtig && !hilfe && anlauf !== 2) lernHeutePlus(ctx.kind); // H6
          const mischGueltig = !(a.misch && r.misch?.gueltig === false); // ohne gültige Ausgabe: keine Mischkarte, kein Lob als Wiederholung
          const dasWar = a.misch && mischGueltig ? el('p', { class: 'lr-misch-das-war' }, `Das war: ${r.misch?.etappe || a.etappe || 'eine frühere Etappe'}` + ((lernStadtName(ctx.kind, a) || r.misch?.stadt) ? ` – ${a.lernziel && lernRkFlugVon(ctx.kind, a.thema_id || lernEinheitThema.get(Number(a.einheit_id))) ? lernStadtName(ctx.kind, a) : r.misch?.stadt || a.stadt}` : '')) : null;
          const warFaellig = e.faellig; let wdhFertigBox = null;
          if (r.karte && !a.misch) { if (r.karte.eigene_loesungen !== undefined) Object.assign(e, lernRegelFelder(r.karte)); e.serie = r.karte.serie; e.ziel = r.karte.ziel; e.sitzt = r.karte.sitzt; e.schwerOk = !!r.karte.schwer_ok; e.schwerNoetig = !!r.karte.schwer_noetig; e.fertig = r.karte.fertig !== undefined ? !!r.karte.fertig : e.fertig || r.karte.sitzt; e.wiederOffen = !r.karte.sitzt && (e.wiederOffen || warSitzt); /* H1: der Server entscheidet */ if (warSitzt && r.karte.sitzt) e.faellig = false; }
          zeichnePunkte(); zeichneFortschritt();
          const jetztSitzt = !!r.karte?.neu_sitzt || (!warSitzt && e.sitzt);
          const weiter = el('button', { type: 'button', class: 'lr-knopf lr-weiter', onclick: () => { zeigeAufgabe(); window.scrollTo(0, 0); } }, neu ? 'Neue Bordkarte ›' : 'Nächste Bordkarte');
          if (neu) lernErsetze(dock, weiter); else { pruefen.remove(); meldung.after(weiter); }
          // WK F2: Die fällige Etappe ist nach dieser Antwort wiederholt (Server: nicht mehr fällig) → sofort „Hier bist du fertig ✓“ mit dem nächsten Schritt groß
          if (warFaellig && !a.misch && !e.faellig && (e.sitzt || e.fertig) && !jetztSitzt) {
            const k0 = schrittKnopf(); const trotzdem = el('button', { type: 'button', class: 'lr-textlink lr-trotzdem', onclick: () => { weiterueben = true; zeigeAufgabe(); window.scrollTo(0, 0); } }, 'Trotzdem weiterüben');
            const box = el('div', { class: 'lr-karte-box lr-fertig-hier lr-wdh-fertig' }, el('p', {}, el('b', {}, 'Hier bist du fertig ✓')), el('p', { class: 'lr-leise' }, 'Wiederholung geschafft.'), k0, trotzdem);
            if (neu) lernErsetze(dock); else weiter.remove();
            wdhFertigBox = box; // erst nach der Rückmeldung einsetzen (die ersetzt den Inhalt von „meldung“)
          }
          weiter.focus({ preventScroll: true });
          if (!neu && !r.richtig && erkl && erklBox.hidden && false) { erklBox.hidden = false; erkl.setAttribute('aria-expanded', 'true'); }
          lernErsetze(meldung, r.richtig
            ? el('div', { class: 'lr-rueck lr-rueck-ok' }, el('b', {}, neu ? '✓ An Bord' + (sterne > sterneVor ? ` · +${sterne - sterneVor} Sterne` : '') : 'Richtig!'),
                a.misch && mischGueltig && r.wiederholung?.bestanden ? el('p', { class: 'lr-misch-wdh' }, '↻ Zählt als Wiederholung dieser Etappe' + (r.wiederholung.sterne && !neu ? ` · +${r.wiederholung.sterne} Sterne` : '')) : null,
                a.misch && mischGueltig && r.wiederholung?.bestanden === false ? el('p', { class: 'lr-misch-wdh lr-wdh-hilfe' }, 'Richtig – morgen noch einmal ohne Hilfe.') : null,
                !a.misch ? lernFuenfHinweis(ctx, e, sterne - sterneVor, { hilfe: !!hilfe, zweiter: anlauf === 2 }) : null,
                !a.misch && !warSitzt && !hilfe && anlauf !== 2 && r.karte?.neu_gezaehlt === false ? el('p', { class: 'lr-kennst' }, 'Die kennst du schon – gut wiederholt.') : null, // H3
                lernBedingungListe(a, r), r.loesungsweg ? el('p', {}, lernMathe(r.loesungsweg)) : null, jwSticker)
            : neu ? el('div', { class: 'lr-rueck lr-rueck-falsch lr-kursbox' }, el('p', { class: 'lr-ueber' }, a.antworttyp === 'zahl' && r.grund ? 'FAST – KURSKORREKTUR' : 'NOCH NICHT'), lernKurs(a, w),
              el('b', {}, 'Richtig ist: ', lernMathe(lernLoesungText(a))), lernBedingungRueck(r), lernBedingungListe(a, r),
              a.antworttyp === 'luecken' && lernIstTermVorlage(a.frage?.schablone) && lernGleichwertigAusgeklammert(a.frage?.schablone, w.werte, r.loesung?.werte)
                ? el('p', {}, 'Dein Term ist gleichwertig, aber noch nicht vollständig ausgeklammert: Vor die Klammer gehört der größte gemeinsame Faktor.') : null,
              r.loesungsweg ? el('p', {}, lernMathe(r.loesungsweg)) : null,
              lernDetektiv(a, a.misch ? {} : e, r, 'IST DIR DAS PASSIERT?'),
              el('p', { class: 'lr-leise lr-naechste-voll' }, 'Die nächste zählt wieder voll.'), jwSticker)
            : el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, 'Noch nicht. Richtig ist: ', lernMathe(lernLoesungText(a))), lernBedingungRueck(r), lernBedingungListe(a, r),
              a.antworttyp === 'luecken' && lernIstTermVorlage(a.frage?.schablone) && lernGleichwertigAusgeklammert(a.frage?.schablone, w.werte, r.loesung?.werte)
                ? el('p', {}, 'Dein Term ist gleichwertig, aber noch nicht vollständig ausgeklammert: Vor die Klammer gehört der größte gemeinsame Faktor.') : null,
              r.loesungsweg ? el('p', {}, el('b', {}, 'So geht’s: '), lernMathe(r.loesungsweg)) : null,
              lernDetektiv(a, a.misch ? {} : e, r, 'FEHLER-DETEKTIV: IST DIR DAS PASSIERT?'),
              el('p', { class: 'lr-leise' }, 'Die nächste zählt wieder voll. Die Erklärung findest du über der Bordkarte.'), jwSticker));
          if (dasWar) meldung.prepend(dasWar); // W176: nach der Mischkarte die Etappe nennen
          if (wdhFertigBox) { meldung.after(wdhFertigBox); wdhFertigBox.scrollIntoView?.({ block: 'nearest' }); wdhFertigBox.querySelector('a,button')?.focus({ preventScroll: true }); }
          if (nb && !a.misch) { // NB: eigene Lösung zählt (+1), Tipp/2. Versuch lässt die Folge stehen, Fehler → 0 („Kein Problem – neuer Anlauf.“)
            if (typeof r.karte?.folge === 'number') nb.folge = r.karte.folge; else if (r.richtig && !hilfe && anlauf !== 2) nb.folge++; else if (!r.richtig) nb.folge = 0;
            nbZeichnen();
            if (!r.richtig) meldung.firstElementChild?.prepend(el('div', { class: 'lr-nb-rueck' }, el('b', {}, 'Kein Problem – neuer Anlauf.'), el('p', {}, `Noch ${nb.noetig} richtige in Folge, dann sitzt die Etappe wieder.`)));
            if (nb.folge >= nb.noetig || jetztSitzt) { nbFertig(); return; }
          }
          if (r.abgelegt) lernAbgelegtZeigen(ctx.kindObj || { id: ctx.kind }, r.abgelegt); // WD-6 über eine Mischkarte
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
            // Teil 4 Punkt 5a: nach dem Knobeln (richtig, falsch oder abgebrochen) zurück auf diesen Landebildschirm, nicht in die Übungen
            const tf = lernTestFaellig(ctx.daten, etappen);
            const landung = r.landung || null; const art = lernLandungArt(landung, ctx.daten, e.lernziel);
            const nrNaechste = naechsteKarte ? etappen.indexOf(naechsteKarte) + 1 : 0;
            // genau ein großer Knopf zum nächsten Schritt (umsetzung.md 1): nächste Etappe · Flug-Test · Abflugtafel
            // WK 2 (A2): Pflicht fertig → direkt der Flug-Test (auch wenn noch eine Extra-Etappe offen ist); sonst nächste Etappe; sonst nächster Schritt der Reise
            const knopf = () => tf ? lernGrossKnopf(tf.art === 'nachtrag' ? 'Weiter: Test zu den neuen Etappen' : tf.art === 'laeuft' ? 'Weiter: angefangener Test' : 'Jetzt zum Flug-Test',
                  `${tf.n} ${tf.n === 1 ? 'Bordkarte' : 'Bordkarten'}, eine je Etappe, ohne Tipps`, { href: `${ctx.basis}-test` })
              : naechsteKarte ? lernGrossKnopf(`Weiter: ${naechsteKarte.titel}`, `Etappe ${nrNaechste} von ${etappen.length}`, { onclick: () => { lernAbschlussZu(); if (neuKarte(naechsteKarte)) { erstErklaeren(naechsteKarte); return; } aktKarte = naechsteKarte; stufe = 0; weiterueben = false; zeichneUeben(); window.scrollTo(0, 0); } })
                : lernSchrittKnopf(ctx.kind);
            const knobel = (e.bonus || []).find((k) => !k.versuche);
            const exFrei = lernExNachLandung(ctx); // EX-App: hat diese Landung eine Expedition freigeschaltet? (Ansicht 1 vor dem nächsten Schritt)
            const zeigeLandung = () => {
              // Zurück-Taste nach der Landung: nicht zurück in die Bordkarten dieser Etappe, sondern zur Übersicht des Flugs (umsetzung.md 5)
              try { history.replaceState(history.state, '', `${ctx.basis}-erklaeren`); } catch { /* egal */ }
              lernErsetze(flaeche, el('p', { class: 'lr-leise lr-ab-dahinter' }, `Etappe „${e.titel}“ ist gelandet.`));
              lernAbschlussZeigen(ctx.kindObj, lernAbschlussEtappe({ e, nr: pos + 1, von: mitAufg.length, landung, daten: ctx.daten, sterne, knopf: lernExVorKnopf(knopf(), exFrei), kind: ctx.kind,
                // Sturmflug: die Knobel-Bordkarte kommt nicht von selbst, nur als kleiner Textlink
                knobel: art === 'sturm' && knobel ? () => { lernAbschlussZu(); zeigeKnobel(); } : null }), { label: 'Etappe gelandet' });
            };
            // Punkt 5d / AB: Die Knobel-Bordkarte kommt von selbst hinten dran (eine noch nicht versuchte) – außer beim Sturmflug; danach die Abschluss-Ansicht
            const zeigeKnobel = () => {
              const platz = el('div', { class: 'lr-knobel-platz' });
              lernErsetze(flaeche, el('p', { class: 'lr-knobel-vorne' }, el('b', {}, `Gelandet: ${e.titel} ✓`), ' Zum Schluss eine harte Nuss – falsch kostet nichts.'), platz,
                el('button', { type: 'button', class: 'lr-textlink lr-knobel-ohne', onclick: () => { zeigeLandung(); window.scrollTo(0, 0); } }, 'Heute keine Knobel-Bordkarte'));
              // vor dem Prüfen nur der kleine Textlink; nach dem Prüfen ein großer Knopf „Weiter ›“ zur Abschluss-Ansicht
              lernKnobel(platz, knobel, ctx, { ortCode, zurueckText: 'Weiter ›', zurueck: () => { zeigeLandung(); window.scrollTo(0, 0); },
                nachPruefen: (zu) => { if (zu) { zu.hidden = false; zu.className = 'lr-knopf lr-knobel-zurueck'; } flaeche.querySelector('.lr-knobel-ohne')?.remove(); } });
              const zu = platz.querySelector('.lr-knobel-zurueck'); if (zu) zu.hidden = true;
            };
            if (knobel && art !== 'sturm') zeigeKnobel(); else zeigeLandung();
            window.scrollTo(0, 0); flaeche.querySelector('.lr-knopf, .lr-knopf-zweit')?.focus({ preventScroll: true });
            return;
          }
          if (neu) { meldung.scrollIntoView?.({ block: 'center', behavior: 'smooth' }); return; }
          if (jetztSitzt) lernAnhaengen(meldung, el('section', { class: 'lr-geschafft lr-sitzt' },
            el('div', { class: 'lr-geschafft-haken' }, lernIcon(LI.haken, 48)),
            el('p', { class: 'lr-ueber' }, 'ETAPPE SITZT'), el('h2', {}, e.titel),
            sterne ? el('p', { class: 'lr-sterne-neu' }, lernIcon(LI.stern, 20), ` +${sterne} Sterne`) : null,
            el('p', { class: 'lr-leise' }, 'Sicher wird die Etappe, wenn du sie in ein paar Tagen wieder kannst.'),
            lernKnobelAngebot(e, (k) => lernKnobel(flaeche, k, ctx, { ortCode, zurueck: () => { stufe = 0; weiterueben = false; zeichneUeben(); window.scrollTo(0, 0); } })),
            naechsteKarte ? el('button', { type: 'button', class: 'lr-knopf', onclick: () => { if (neuKarte(naechsteKarte)) { erstErklaeren(naechsteKarte); return; } aktKarte = naechsteKarte; stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } }, `Nächste Etappe: ${naechsteKarte.titel}`)
              : el('button', { type: 'button', class: 'lr-knopf', onclick: () => zeige('erklaeren') }, 'Zur Übersicht der Etappen')));
          (jetztSitzt ? meldung : weiter).scrollIntoView?.({ block: 'center', behavior: 'smooth' });
        } catch (err) { if (lernGesperrt(err)) { render(); return; } lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
      });
      const fein = window.matchMedia?.('(pointer: fine)').matches;
      auf.node.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' && ev.target.tagName === 'INPUT') { ev.preventDefault(); if (pruefen.isConnected) pruefen.click(); } });
      if (neu) {
        lernErsetze(dock, auf.tasten ? lernTastenfeld(auf.tasten, pruefen) : pruefen);
        lernErsetze(flaeche, erkl, erklBox,
          el('section', { class: 'lr-karte-box lr-aufgabe lr-bordkarte' },
            el('div', { class: 'lr-bord-kopf' }, el('span', {}, a.misch ? `BORDKARTE ${nr} · AUS DEINER REISE` : `BORDKARTE ${nr} · ${String(ctx.stadtVon?.(e) || ctx.ort.stadt || 'Thema').toUpperCase()}`), lernStufeZeichen(a)),
            a.misch ? el('p', { class: 'lr-misch-hinweis' }, 'Aus deiner Reise – erkennst du, was gefragt ist?') : null,
            auf.node, el('div', { class: 'lr-perforation', 'aria-hidden': 'true' }),
            tipp ? el('div', { class: 'lr-knopfzeile' }, tipp) : null),
          hilfeBox, meldung,
          ctx.leitung ? lernAendern({ einheit_id: ctx.einheit, lernziel: e.lernziel, aufgabe_id: a.id, lernender_id: ctx.kind }, { bezug: 'bordkarte', wo: `Bordkarte „${String(a.frage?.text || '').slice(0, 60)}“` }) : null, dock);
      } else lernErsetze(flaeche,
        erkl, erklBox,
        el('section', { class: 'lr-karte-box lr-aufgabe' },
          el('p', { class: 'lr-ueber' }, `AUFGABE ${nr} `, lernStufeZeichen(a)), a.misch ? el('p', { class: 'lr-misch-hinweis' }, 'Aus deiner Reise – erkennst du, was gefragt ist?') : null, auf.node,
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
  return [['gym_by', 'Gym'], ['rs_by', 'RS'], ['ib_myp', 'IB MYP-Jahr']].filter(([k]) => j[k]).map(([k, t]) => `${t} ${j[k]}`).join(' · ');
}

function lernEinheitTest(ctx, tf = null) {
  const body = el('div', { class: 'lern-body' });
  if (tf && tf.art !== 'laeuft') lernAnhaengen(body, el('div', { class: 'card lr-test-hinweis' }, el('b', {}, 'Alle Etappen sind gelandet ✓'),
    el('p', { class: 'small' }, tf.art === 'nachtrag' ? `Jetzt der Test zu den neuen Etappen: ${tf.n} ${tf.n === 1 ? 'Bordkarte' : 'Bordkarten'}, ohne Tipps.` : `Jetzt kommt der Test: ${tf.n} ${tf.n === 1 ? 'Bordkarte' : 'Bordkarten'}, ohne Tipps. Bestehst du ihn, ist der Flug geschafft.`),
    lernStempelRest(ctx) ? el('p', { class: 'small' }, lernStempelRest(ctx)) : null,
    tf.trotzdem ? el('a', { class: 'lr-textlink lr-trotzdem-ueben small', href: tf.trotzdem }, 'Trotzdem weiterüben') : null)); // WK 2 A3/A4: freiwillig, klein
  lernErsetze(main, lernRahmen(ctx.kindObj, 'weg',
    el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-ueber' }, 'TEST'), el('h1', { class: 'lr-titel' }, ctx.ort?.stadt ? `${ctx.ort.stadt} · ${ctx.titelKurz}` : ctx.titel)), // N6: „Ort · Flug“ wie im Erklären-Reiter
    el('a', { class: 'lr-zurueck', href: `${ctx.basis}-erklaeren` }, '‹ Zu den Etappen'), body));
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
      el('div', { class: 'lr-pass-kopf' }, nach(-1), el('span', {}, el('small', {}, y.name.toUpperCase() + (y.sa === 'ib_myp' ? ' · ≈ KLASSE ' + y.kl(kl) : '')), el('b', {}, y.label(kl).toUpperCase())), nach(1)),
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

// W177: Pflicht-Etappen, die nach dem Flugtest dazukamen und noch durch keinen Test gegangen sind
const lernNeueEtappen = (stand) => (stand || []).filter((s) => s.pflicht && s.status === 'offen').length;
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
  ctx.testStarten = start; // Teil 4 Punkt 5g: „Gleich verbessern ›“ startet die Korrektur direkt (die Adresse …-test ist schon die eigene)
  const knopf = (t, art, text) => el('div', { class: 'card' }, el('h3', {}, t), el('p', { class: 'small' }, text),
    el('button', { type: 'button', class: 'primary', onclick: () => start(art) }, t + ' starten'));
  if (ctx.daten.verblasst) lernAnhaengen(box, el('p', { class: 'lern-hinweis' }, 'Rückreise: Diese Einheit sitzt noch nicht sicher. Erst verbessern, dann den Nachtest wiederholen.'));
  if (!offen && ctx.daten.ohne_test) { // LB-3: „Kann er – aber wiederholen“ – kein Flug-Test, keine Nachtests
    lernAnhaengen(box, el('p', { class: 'card lern-ohne-test' }, 'Für diesen Flug gibt es keinen Test. Du wiederholst ihn nur – die Wiederholungen kommen von selbst.'));
    return box;
  }
  if (offen) lernAnhaengen(box, el('div', { class: 'card' }, el('h3', {}, 'Angefangener Test'), el('p', { class: 'small' }, 'Deine bisherigen Antworten sind gespeichert.'),
    el('button', { type: 'button', class: 'primary', onclick: () => start(offen.art) }, 'Weitermachen')));
  else {
    if (!blockFertig) lernAnhaengen(box, knopf('Test', 'blocktest', 'Eine Bordkarte je Etappe, ohne Tipps. Die Lösungen siehst du nach dem Abgeben.'));
    // W177: Nach dem Flugtest neu hinzugekommene Pflicht-Etappen (Status „offen“) – Nachtragstest, sonst Sackgasse („Test bereit“, aber kein Test)
    else if (lernNeueEtappen(stand)) lernAnhaengen(box, knopf('Test zu den neuen Etappen', 'blocktest', `Seit deinem Test sind ${lernNeueEtappen(stand)} neue Etappen dazugekommen. Eine Bordkarte je neuer Etappe, ohne Tipps.`));
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
      catch (e) { if (lernGesperrt(e)) { i = Math.min(aufg.length - 1, Math.max(0, i + d)); zeige(); return; } lernErsetze(meldung, el('p', { class: 'err-text' }, e.message)); }
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
        // Teil 4 Punkt 5h: Stand des Flugs neu vom Server holen, bevor Knöpfe gezeichnet werden (sonst alter Stand → wieder „Verbessern“)
        try { const neu = await lernCall('schule_einheit_lesen', { lernender_id: ctx.kind, einheit_id: ctx.einheit }); if (neu && neu.ok !== false) ctx.daten = neu; } catch { /* Ergebnis trotzdem zeigen */ }
        if (ctx.live()) { lernTestErgebnis(ctx, box, r);
          if (lernNeu(ctx.kindObj) && lernFlugAbschlussFaellig(ctx, r)) lernAbschlussFlugStart(ctx, r); } // AB-A, 0.83.1: nach flug_geschafft
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

// Teil 4 Punkt 5h: Fehler-Etappen aus dem frisch geladenen Stand (Fallback: Antwort des Tests)
const lernTestFehler = (ctx, r) => { const st = ctx.daten?.stand; // frischer Stand zählt, sobald er Test-Ergebnisse trägt
  return Array.isArray(st) && st.some((x) => x.status && x.status !== 'offen') ? st.filter((s) => s.pflicht !== false && s.status === 'fehler') : (r.lernziele || []).filter((s) => s.pflicht !== false && s.status === 'fehler'); };
// 0.83.1 (Nachtrag B): Die Abschluss-Ansicht des Flugs hängt am Server – flug_geschafft (dieser Abschluss macht den Flug zum ersten Mal fertig,
// über den Flug-Test oder über Verbessern) oder ort_geschafft. Kennt der Server das Feld nicht (alter Server), gilt die Regel von 0.83.0.
const lernFlugAbschlussFaellig = (ctx, r) => (r && 'flug_geschafft' in r) ? !!(r.flug_geschafft || r.ort_geschafft) : (lernFlugGeschafft(ctx, r) && !r.nachtest_ergebnis);
const lernFlugGeschafft = (ctx, r) => !!r.einheit_abgeschlossen || (!!ctx.daten?.blocktest_fertig && !lernTestFehler(ctx, r).length && !lernNeueEtappen(ctx.daten?.stand) && !ctx.daten?.laufender_test);
function lernTestErgebnis(ctx, box, r) {
  const ort = r.ort || {};
  const geschafft = lernFlugGeschafft(ctx, r);
  const stand = Array.isArray(ctx.daten?.stand) && ctx.daten.stand.some((x) => x.status && x.status !== 'offen') ? ctx.daten.stand : r.lernziele;
  lernErsetze(box, 
    el('div', { class: 'card lern-ergebnis' },
      el('p', { class: 'lern-ergebnis-summe' }, el('b', {}, `${r.richtig} von ${r.gesamt}`), ' richtig'),
      geschafft ? el('p', { class: 'lern-rueck ok' }, el('b', {}, 'Flug geschafft! 🎉')) : lernTestFehler(ctx, r).length ? el('p', { class: 'small' }, 'Bei „noch üben“: die passenden Etappen noch einmal üben, dann „Verbessern“.') : null,
      r.nachtest_ergebnis ? el('p', { class: 'lern-rueck ' + (r.nachtest_ergebnis === 'bestanden' ? 'ok' : 'falsch') }, el('b', {}, {
        bestanden: r.nachtest?.folgerunde && r.nachtest_runde >= 3 ? 'Nachtest geschafft (ab 80 %).' : `Nachtest-Runde ${r.nachtest_runde} geschafft (ab 80 %).`,
        wiederholen: 'Unter 80 %: Diese Runde zählt noch nicht. Verbessere die falschen Etappen, dann kommt der Nachtest noch einmal.',
        rueckreise: 'Unter 60 %: Rückreise zu diesem Ort. Erst üben und verbessern, dann den Nachtest wiederholen.' }[r.nachtest_ergebnis])) : null,
      ort.abgeschlossen ? el('div', { class: 'lr-stempel-gross' }, el('div', { class: 'lr-stempel', style: '--dreh:-8deg' }, el('b', {}, 'GESCHAFFT'), el('small', {}, 'Neuer Stempel')),
        el('p', {}, el('b', {}, 'Ort geschafft! Der Stempel ist jetzt in deinem Reisepass.'))) : null,
      lernStandZeile(stand)),
    ...(r.ergebnisse || []).map((x) => {
      const a = { ...x, antworttyp: x.antworttyp || (x.loesung?.werte ? 'luecken' : x.loesung?.index !== undefined ? (x.antworten ? 'auswahl' : 'markierung') : x.loesung?.text !== undefined ? 'text' : 'zahl') };
      return el('div', { class: 'card lern-rueck-karte ' + (x.richtig ? 'ok' : 'falsch') },
        // Teil 4 Punkt 5f: großes ✓/✗ mit Wort – nicht nur Farbe
        el('p', { class: 'lern-rk-kopf' }, el('span', { class: 'lern-rk-zeichen', 'aria-hidden': 'true' }, x.richtig ? '✓' : '✗'),
          el('b', { class: 'lern-rk-wort' }, x.richtig ? 'richtig' : 'falsch'), el('span', { class: 'lern-rk-etappe' }, ' · ' + lernZielName(x.lernziel))),
        el('p', { class: 'lern-frage' }, lernMathe(x.frage?.text)),
        x.frage?.grafik ? (x.frage.grafik.typ && x.frage.grafik.typ !== 'zahlenstrahl' ? lernBild(x.frage.grafik)
          : lernZahlenstrahl(a.antworttyp === 'markierung' ? { ...x.frage.grafik, _richtig: x.loesung?.index, _gewaehlt: x.antwort?.index } : x.frage.grafik, false)) : null,
        el('p', { class: 'small' }, 'Deine Antwort: ', el('b', {}, lernMathe(lernAntwortText(a, x.antwort)))),
        x.richtig ? null : el('p', { class: 'small' }, 'Richtig: ', el('b', {}, lernMathe(lernLoesungText(a)))),
        x.loesungsweg && !x.richtig ? el('p', { class: 'small muted' }, x.loesungsweg) : null);
    }),
    lernTestKnoepfe(ctx, r, geschafft));
}
// N7: Knöpfe im Abflug-Stil. Bei „noch üben“: erst die Etappe üben, dann verbessern.
// Teil 4 Punkt 5g/h: mit Fehlern genau zwei klare Wege (Erst üben · Gleich verbessern); geschafft → nächster Schritt, kein „Verbessern“.
function lernTestKnoepfe(ctx, r, geschafft = lernFlugGeschafft(ctx, r)) {
  const basis = ctx.basis || `#/lerneinheit/${ctx.kind}-${ctx.einheit}`;
  const etappen = ctx.daten?.inhalt?.etappen || [];
  const erste = geschafft ? null : lernTestFehler(ctx, r)[0]; const nr = erste ? etappen.findIndex((e) => e.lernziel === erste.lernziel) + 1 : 0;
  if (!erste) return el('div', { class: 'lr-knopfzeile lr-test-knoepfe' },
    lernSchrittKnopf(ctx.kind, { gross: false, vorher: { text: geschafft ? 'Weiter zum nächsten Flug' : 'Weiter', ziel: `#/reise/${ctx.kind}` } }), // WK 2 (A2): direkt der nächste Schritt
    el('a', { class: 'lr-textlink', href: `${basis}-erklaeren` }, 'Zum Flug'));
  const verbessern = el('button', { type: 'button', class: 'lr-knopf-zweit lr-gleich-verbessern', onclick: () => { if (ctx.testStarten) { window.scrollTo(0, 0); ctx.testStarten('korrektur'); } else render(); } }, 'Gleich verbessern ›');
  return el('div', { class: 'lr-knopfzeile lr-test-knoepfe' },
    el('a', { class: 'lr-knopf', href: nr ? `${basis}-ueben-${nr}` : `${basis}-ueben` }, `Erst üben: ${lernZielName(erste.lernziel)} ›`),
    verbessern,
    el('a', { class: 'lr-textlink', href: `${basis}-erklaeren` }, 'Zum Flug'),
    el('a', { class: 'lr-textlink', href: `#/reise/${ctx.kind}` }, 'Zur Abflugtafel'));
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

// LB-2: die 4 Stufen (gleiche Zeichen, Farben und Wörter überall). Der Server rechnet die Stufe (schule.thema_stufe, LB-3); ohne sie schätzt die App aus dem Stand.
const LERN_STUFE = {
  komplett: { z: '◉', wort: 'Kann er komplett', kl: 'st-1' },
  wiederholung: { z: '↻', wort: 'In Wiederholung', kl: 'st-2' },
  dran: { z: '▶', wort: 'Gerade dran', kl: 'st-3' },
  kommt: { z: '○', wort: 'Kommt noch', kl: 'st-4' },
  nicht_im_plan: { z: '+', wort: 'Nicht im Plan', kl: 'st-5' },
};
const LERN_STUFE_REIHE = ['dran', 'kommt', 'wiederholung', 'komplett', 'nicht_im_plan'];
// Stufe eines Flugs ohne Server-Stufe: aus „kann schon“ und dem Stand schätzen
function lernStufeSchaetzen(t, imPlan, ortFertig = false) {
  if (t.kann_schon) return { stufe: 'komplett', gesetzt: 'komplett', geschaetzt: true };
  if (t.stand === 'erledigt' || (ortFertig && imPlan)) return { stufe: 'wiederholung', geschaetzt: true };
  if (t.stand === 'laeuft') return { stufe: 'dran', geschaetzt: true };
  return { stufe: imPlan ? 'kommt' : 'nicht_im_plan', geschaetzt: true };
}
// LB-3 Nachbesserung (Sollte 5) / LB Teil 6 Punkt 6: „Kann er komplett“, aber eine früher gelandete Etappe ist wieder offen – die Stufe bleibt ◉ (Entscheidung des Lehrers), der Rückfall wird genannt.
const lernRueckfall = (s) => s?.hinweis === 'rueckfall' && s.stufe === 'komplett';
const lernRueckfallText = (s) => { if (!lernRueckfall(s)) return ''; const n = Number(s.wieder_offen) || 0; return n ? ` · Rückfall: ${n} ${n === 1 ? 'Etappe' : 'Etappen'} wieder offen` : ' · Rückfall: eine Etappe wieder offen'; };
// Zusatz rechts: „Wdh 3 von 5 · nächste in 4 Lerntagen“, „3 von 7 Etappen“, „wieder offen“ …
function lernStufeZusatz(s) {
  const wdh = s.wdh_nr ? `Wdh ${s.wdh_nr} von 5` + (s.naechste_in === 0 ? ' · heute fällig' : typeof s.naechste_in === 'number' ? ` · nächste in ${s.naechste_in} ${s.naechste_in === 1 ? 'Lerntag' : 'Lerntagen'}` : '') : '';
  switch (s.stufe) {
    case 'komplett': return (s.gesetzt === 'komplett' ? 'gesetzt' : 'alle Etappen sicher') + lernRueckfallText(s);
    // WD-4 (Vorschlag, optional): wartende gesetzte Etappen „3 warten · kommt ab in 2 Lerntagen“; WD-6: „2 von 7 abgelegt“
    case 'wiederholung': return [s.gesetzt === 'wiederholen' ? 'gesetzt: kann er, wird wiederholt' : null, wdh || null,
      Number(s.wartet) > 0 ? `${s.wartet} ${Number(s.wartet) === 1 ? 'Etappe wartet' : 'Etappen warten'}` + (typeof s.kommt_ab_in === 'number' ? (s.kommt_ab_in === 0 ? ' · kommt ab heute' : ` · kommt ab in ${s.kommt_ab_in} ${s.kommt_ab_in === 1 ? 'Lerntag' : 'Lerntagen'}`) : '') : null,
      Number(s.etappen_abgelegt) > 0 ? `${s.etappen_abgelegt} von ${s.etappen || '–'} abgelegt` : null].filter(Boolean).join(' · ') || 'alles gelandet';
    case 'dran': return s.wieder_offen ? 'wieder offen' : s.rueckreise ? 'Rückreise' : s.test_offen ? 'Test offen' : s.etappen ? `${s.gelandet || 0} von ${s.etappen} Etappen` : 'angefangen';
    case 'kommt': return 'im Plan';
    default: return 'fehlt';
  }
}
const lernStufeZeichenEl = (s) => el('span', { class: 'lern-st-sym ' + (LERN_STUFE[s.stufe] || LERN_STUFE.kommt).kl, 'aria-hidden': 'true' }, (LERN_STUFE[s.stufe] || LERN_STUFE.kommt).z);
const lernStufeWortEl = (s, mitZusatz = true) => el('span', { class: 'lern-st-wort ' + (LERN_STUFE[s.stufe] || LERN_STUFE.kommt).kl + (lernRueckfall(s) ? ' lern-st-rueckfall' : '') },
  el('b', {}, (LERN_STUFE[s.stufe] || LERN_STUFE.kommt).wort), mitZusatz ? el('small', {}, lernStufeZusatz(s)) : null);

// LA-8: Farbe je Klasse (Basis Gymnasium-Klasse); ohne Gymnasium-Klasse graues „–“. Orange mit dunkler Schrift (Kontrast).
const LERN_KL_FARBE = { 5: '#2E7D32', 6: '#0277BD', 7: '#6A1B9A', 8: '#C62828', 9: '#EF6C00', 10: '#455A64' };
const LERN_KONT_REIHE_LA8 = ['Zahlen', 'Algebra', 'Geometrie', 'Fläche und Raum', 'Geld und Verhältnisse', 'Daten und Zufall', 'Funktionen', 'Entdecker-Inseln'];
const lernGymKl = (o) => { const ks = (o?.themen || []).map((t) => Number(t.jahrgang?.gym_by)).filter(Boolean); return ks.length ? Math.min(...ks) : null; };
const lernKlStil = (o) => { const k = lernGymKl(o); return LERN_KL_FARBE[k] ? `--kl:${LERN_KL_FARBE[k]}` : null; };
const lernKlKasten = (o) => { const k = lernGymKl(o); const f = LERN_KL_FARBE[k];
  return el('span', { class: 'lern-kl-kasten' + (f ? '' : ' ohne') + (k === 9 ? ' hell' : ''), style: f ? `--kl:${f}` : null, title: f ? `Gymnasium Klasse ${k}` : 'ohne Gymnasium-Klasse', 'aria-hidden': 'true' }, k ? String(k) : '–'); };

// Plan-Kern (seit LM-5 gemeinsam für den Reiter „Plan“ und die Lehrplan-Matrix): Arbeitskopie, Einstellung je Flug, Einträge für schule_plan_setzen
const lernPlanArbeitskopie = (p) => (p.plan || []).filter((r) => r.art === 'normal').map((r) => ({ block_id: r.block_id, kann_schon: r.kann_schon, status: r.status,
  ausgelassen: [...(r.ausgelassen || [])], kann: [...(r.kann_schon_themen || [])], kw: [...(r.kann_wdh_themen || [])], ww: [] }));
const lernPlanKopie = (x) => x.map((y) => ({ ...y, ausgelassen: [...y.ausgelassen], kann: [...y.kann], kw: [...y.kw], ww: [] }));
const lernPlanFlags = (p) => { const normal = (p.plan || []).filter((r) => r.art === 'normal');
  return { kannAbwaehlen: !!p.kann_abwaehlen || normal.some((r) => Array.isArray(r.ausgelassen)),
    kannJeFlug: normal.some((r) => Array.isArray(r.kann_schon_themen)) || (p.orte || []).some((o) => (o.themen || []).some((t) => t.kann_schon !== undefined)), kannWdh: !!p.kann_wdh }; };
const lernPlanEintraege = (plan, { kannAbwaehlen, kannJeFlug, kannWdh }) => plan.map((x) => ({ block_id: x.block_id, kann_schon: !!x.kann_schon, ...(kannAbwaehlen ? { ausgelassen: x.ausgelassen } : {}),
  ...(kannJeFlug ? { kann_schon_themen: x.kann } : {}), ...(kannWdh ? { kann_wdh_themen: x.kw } : {}), ...(kannWdh && x.ww.length ? { wieder_wdh_themen: x.ww } : {}) }));
// Einstellung je Flug: lernen | wiederholen | komplett | aus | wieder. Gibt true zurück, wenn der Ort dadurch aus dem Plan fällt.
function lernPlanSetzeIn(plan, alle, kannAbwaehlen, blockId, themaId, wahl) {
  let i = plan.findIndex((y) => y.block_id === blockId); let x = plan[i];
  if (!x) {
    if (wahl === 'aus') return false;
    // „+ In den Plan“: der Ort kommt nur mit diesem Flug; die anderen Flüge des Ortes werden abgewählt
    x = { block_id: blockId, kann_schon: false, status: 'offen', ausgelassen: kannAbwaehlen ? alle.filter((id) => id !== themaId) : [], kann: [], kw: [], ww: [] };
    plan.push(x); i = plan.length - 1;
  }
  if (x.kann_schon && wahl !== 'komplett') { x.kann_schon = false; x.kann = alle.filter((id) => !x.ausgelassen.includes(id)); }
  const warKomplett = x.kann.includes(themaId);
  const ohne = (l) => l.filter((id) => id !== themaId);
  if (wahl !== 'wieder') { x.ausgelassen = ohne(x.ausgelassen); x.kann = ohne(x.kann); x.kw = ohne(x.kw); }
  if (wahl === 'wiederholen') x.kw.push(themaId);
  if (wahl === 'komplett') x.kann.push(themaId);
  if (wahl === 'aus') x.ausgelassen.push(themaId);
  if (wahl === 'wieder') { x.ww = [...new Set([...x.ww, themaId])]; if (warKomplett) { x.kann = ohne(x.kann); x.kw = [...new Set([...x.kw, themaId])]; } }
  // alle Flüge abgewählt → der Ort verschwindet aus dem Plan (Fortschritt bleibt gespeichert)
  if (alle.length && alle.every((id) => x.ausgelassen.includes(id))) { plan.splice(i, 1); return true; }
  return false;
}
// LW-1 (22.11.): Der frühere Reiter „Plan“ (viewPlan) ist im Reiter „Lehrplan“ aufgegangen (viewKindLehrplan).

// Info-Seite „So funktioniert’s“: oben rechts auf der Startseite der Eltern/Lehrer und im Flugplan.
const lernInfoLink = () => el('div', { class: 'lern-info-oben' }, el('a', { class: 'lern-info-link', href: '#/info' }, 'ⓘ So funktioniert’s'));

// E-4: Karte „Neuer Plan aus Lehrplan-Vorlage“ (seit LA-6 im Blatt „⚙ Einstellen“). ersetze(neuerPlan) übernimmt den Vorschlag (mit „Rückgängig“).
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
// LA-1: alte Adressen #/lernstand/<id>[-…], #/wackelt/<id>, #/plan/<id> leiten auf den passenden Reiter der Kind-Seite um
const lernUmleiten = (reiter) => (arg) => { const [id, ...rest] = String(arg || '').split('-'); if (!Number(id)) { route('lernen'); return; } route('kind', [id, reiter, ...rest].join('-')); };
const viewLernstand = lernUmleiten('lehrplan'); // LW-1
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
  const hinweisFluege = modelle.size && ![...modelle.values()][0].alleFluege ? el('p', { class: 'small muted' }, 'Gezählt werden vorerst nur Flüge mit Inhalt.') : null;
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
              el('b', {}, n || (n === 0 && q.sa === 'ib_myp') ? q.label(n) : '–'), el('span', { class: 'lern-mini-balken', style: `--f:${q.farbe}` }, el('i', { style: `width:${lernPz(c.f, c.n)}%;background:${q.farbe}` })),
              el('small', {}, `${c.f}/${c.n}`, w ? el('span', { class: 'lern-wackelt' }, ` · ${w} wackelt`) : null))); })); })))),
      el('p', { class: 'small muted' }, 'Feld antippen → Lehrplan-Landkarte dieses Kindes in dieser Schulart, mit „Einstieg prüfen“. Die Stufe je Schulart setzt ihr unter „⚙ Einstellen“.'), hinweisFluege);
    return;
  }
  const m = modelle.get(kind.id); const ziel = Number(zielArg) || null;
  const basis = `#/kind/${kind.id}-stand-${y.sa}`; // LA-1: Reiter „Stand“ der Kind-Seite
  $('#title').textContent = 'Lernstand ' + kind.name; // Zusatz 1 zu F
  const konts = [...new Set(m.themen.map((t) => t.kontinent))].sort(lernKontReihe);
  const ibHinweis = y.sa === 'ib_myp' ? el('p', { class: 'small muted lern-ib-hinweis' }, LERN_IB_HINWEIS + ' (MYP-Jahr = Klasse − 5; unter Klasse 6: noch kein MYP-Jahr).') : null;
  const reiter = el('div', { class: 'lern-chips-zeile', role: 'group', 'aria-label': 'Schulart' }, ...LERN_SYS.map((q) => el('a', { class: 'lern-chip', href: `#/kind/${kind.id}-stand-${q.sa}`, 'aria-current': q.sa === y.sa ? 'page' : null }, q.name)));
  const check = el('div', { class: 'lern-chips-zeile', role: 'group', 'aria-label': 'Einstieg prüfen' }, el('span', { class: 'small' }, 'Einstieg prüfen:'),
    ...[null, ...y.stufen.slice(1)].map((n) => el('a', { class: 'lern-chip', href: n ? `${basis}-${n}` : basis, 'aria-current': (ziel || null) === n ? 'page' : null }, n ? (y.sa === 'ib_myp' ? 'MYP-Jahr ' : 'Kl. ') + n : 'aus')));
  const davor = ziel ? m.themen.filter((t) => Number(t.jahrgang?.[y.sa]) && Number(t.jahrgang[y.sa]) < ziel) : [];
  const fehlt = davor.filter((t) => t.st !== 'ok'); const p = lernPz(davor.length - fehlt.length, davor.length);
  const ampel = ziel ? el('div', { class: 'lern-ampel ' + (p >= 90 ? 'gruen' : p >= 70 ? 'gelb' : 'rot'), role: 'status' }, el('b', {}, p + ' %'),
    el('span', {}, `Einstieg ${lernSysVoll(y, ziel)}: ${davor.length - fehlt.length} von ${davor.length} Flügen bis ${y.label(ziel - 1)} gelandet. ${p >= 90 ? 'Bereit – kleine Lücken.' : p >= 70 ? 'Fast – gezielt nacharbeiten.' : 'Noch deutliche Lücken.'}`,
      el('small', {}, ' ' + LERN_ORIENTIERUNG))) : el('p', { class: 'small muted' }, `„Einstieg prüfen“ zeigt, was bis zu einer Klasse fehlt. ${LERN_ORIENTIERUNG}`);
  const flugZeile = (t, extra) => el('div', { class: 'lern-standflug lr-st-' + t.st },
    el('span', { class: 'lr-standpunkt', 'aria-hidden': 'true' }, lernSymbol(t.st)),
    el('span', {}, el('b', {}, t.titel), el('small', { class: 'muted' }, [t.stadt, lernZaehltAuch(t, y.sa) ? 'zählt auch für ' + lernZaehltAuch(t, y.sa) : null, t.ausgelassen ? 'im Plan abgewählt' : null, !t.einheit ? 'noch kein Inhalt' : null].filter(Boolean).join(' · ')), extra || null),
    el('span', { class: 'small' }, t.kannSchon ? 'kann schon' : { ok: 'gelandet', jetzt: 'jetzt dran', wackelt: 'wackelt', laeuft: 'läuft', offen: 'offen' }[t.st]));
  const k = konts[Number(kontArg)]; const kl = Number(klArg);
  if (kontArg !== undefined && k && kl) {
    // Ebene 3: Flüge des Feldes mit dem Stand der Etappen
    const ts = m.themen.filter((t) => t.kontinent === k && Number(t.jahrgang?.[y.sa]) === kl);
    const ls = await lernCall('schule_lernstand', { lernender_id: kind.id }).catch(() => null);
    if (!live()) return;
    const proEinheit = new Map((ls?.einheiten || []).map((e) => [e.einheit_id, e]));
    lernErsetze(main, lernInfoLink(), krumen([[`Stand · ${y.name}`, ziel ? `${basis}-${ziel}` : basis], [`${k} · ${y.label(kl)}`, null]]),
      el('section', { class: 'card' }, el('h3', {}, `${k} · ${y.label(kl)}`),
        ...ts.map((t) => { const e = t.einheit ? proEinheit.get(t.einheit.id) : null;
          return flugZeile(t, e ? el('ul', { class: 'lern-etappen-stand' }, ...(e.karten || []).map((x) => el('li', {}, el('span', {}, x.titel || x.lernziel),
            el('small', { class: 'muted' }, lernEtappeStandText(x))))) : null); }),
        ts.length ? null : el('p', { class: 'muted' }, 'Keine Flüge in diesem Feld.')),
      el('p', {}, el('a', { href: `#/kind/${kind.id}-wackelt` }, `Was wackelt? – ${kind.name} mit den echten falschen Antworten ›`)));
    return;
  }
  // Ebene 2: Landkarte Kontinente × Klassen
  const farbe = (ts) => { const f = ts.filter((t) => t.st === 'ok').length; const q = lernPz(f, ts.length);
    return [f, q === 100 ? 'alles' : q > 0 ? 'teil' : ts.some((t) => t.st === 'jetzt' || t.st === 'laeuft') ? 'laeuft' : 'offen']; };
  const ich = m.stufe(y.sa);
  const raster = el('table', { class: 'lern-stand-raster' },
    el('thead', {}, el('tr', {}, el('th', {}, ''), ...y.stufen.map((n) => el('th', { class: (ich === n ? 'ich' : '') + (ziel && n < ziel ? ' pruef' : '') }, (y.sa === 'ib_myp' ? 'MYP-Jahr ' : 'Kl. ') + n)))),
    el('tbody', {}, ...konts.map((kn, ki) => el('tr', {}, el('th', { scope: 'row' }, kn, el('small', {}, m.themen.find((t) => t.kontinent === kn)?.erdteil || '')),
      ...y.stufen.map((n) => { const ts = m.themen.filter((t) => t.kontinent === kn && Number(t.jahrgang?.[y.sa]) === n); if (!ts.length) return el('td', { class: 'leer' }, '·');
        const [f, art] = farbe(ts); const w = ts.some((t) => t.st === 'wackelt');
        return el('td', {}, el('a', { class: `lern-zelle z-${art}${w ? ' w' : ''}${ziel && n >= ziel ? ' aus' : ''}`, href: `${basis}-${ziel || 0}-${ki}-${n}`, 'aria-label': `${kn}, ${y.label(n)}: ${f} von ${ts.length} gelandet${w ? ', wackelt' : ''}` }, `${f}/${ts.length}`)); }))),
      el('tr', { class: 'summe' }, el('th', { scope: 'row' }, 'Gesamt'), ...y.stufen.map((n) => { const c = m.zahl(y.sa, n); return el('td', {}, c.n ? lernPz(c.f, c.n) + ' %' : '–'); }))));
  lernErsetze(main, lernInfoLink(),
    el('section', { class: 'card' }, reiter, ibHinweis, check, ampel,
      el('div', { class: 'lern-tabelle-rollen' }, raster),
      el('p', { class: 'lern-legende small' }, ...[['offen', 'offen'], ['laeuft', 'läuft'], ['teil', 'teilweise'], ['alles', 'alles gelandet'], ['w', 'wackelt']].map(([c2, t]) => el('span', {}, el('i', { class: 'z-' + c2 }), t))),
      ziel && fehlt.length ? el('details', { class: 'lern-fehlt' }, el('summary', {}, `Für den Einstieg fehlen (${fehlt.length})`), ...fehlt.map((t) => flugZeile(t))) : null,
      el('p', { class: 'small muted' }, 'Feld antippen → Flüge in diesem Kontinent und dieser Klasse, mit dem Stand der Etappen.'), hinweisFluege),
    lernExpeditionenKind(u, kind));
}
// W176 Teil 4: Expeditionen eines Kindes im Lernstand – angeboten / begonnen / geschafft (schule_uebersicht.lernende[].expeditionen)
function lernExpeditionenKind(u, kind) {
  const es = Array.isArray(kind.expeditionen) ? kind.expeditionen : null; if (!es) return null;
  const titel = new Map((u.expeditionen || []).map((x) => [x.id, x.titel]));
  const wort = { angeboten: 'angeboten', begonnen: 'begonnen', geschafft: 'abgeschlossen ✓' };
  const selbst = (e) => e.teile_gesamt && e.zustand !== 'angeboten' ? ` · ${e.teile_selbst || 0} von ${e.teile_gesamt} Teilen selbst gelöst` : ''; // H15
  return el('section', { class: 'card lern-exp-stand' }, el('h3', {}, '⛰ Expeditionen'),
    es.length ? el('ul', { class: 'lern-exp-liste' }, ...es.map((e) => el('li', {}, el('span', {}, titel.get(e.id) || `Expedition ${e.id}`), el('span', { class: 'small lern-exp-' + e.zustand }, (wort[e.zustand] || e.zustand) + selbst(e)))))
      : el('p', { class: 'small muted' }, 'Noch keine – eine Expedition wird angeboten, sobald alle ihre Etappen beim Kind gelandet sind.'),
    el('p', { class: 'small' }, el('a', { href: '#/expeditionen' }, 'Alle Expeditionen ansehen ›')));
}
// W176 Teil 4: Expeditionen lesbar für Eltern/Lehrer (mit Lösungen)
async function viewExpeditionen() {
  setChrome('Expeditionen', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const u = await lernCall('schule_uebersicht');
  if (!live()) return;
  const xs = Array.isArray(u.expeditionen) ? u.expeditionen : [];
  const status = { entwurf: 'Entwurf (nur Testkind)', geprueft: 'geprüft', freigegeben: 'freigegeben' };
  lernErsetze(main, lernInfoLink(),
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'ELTERN UND LEHRER'), el('h2', {}, 'Expeditionen'),
      el('p', {}, 'Größere Bordkarten aus 3–5 Teilen, die Stoff aus mehreren Etappen verbinden. Ein Kind bekommt eine Expedition angeboten, sobald alle ihre Etappen bei ihm gelandet sind – freiwillig, sie zählt nicht für „gelandet“. Jeder Teil nennt seine Zahlen selbst, ein Fehler blockiert den nächsten Teil nicht.')),
    xs.length ? el('div', {}, ...xs.map((x) => el('details', { class: 'card lern-exp' },
      el('summary', {}, el('b', {}, x.titel), el('span', { class: 'small muted' }, ` · Klasse ${Object.values(x.klasse || {}).join('/') || '–'} · ${status[x.status] || x.status} · ${(x.teile || []).length} Teile`)),
      el('p', {}, x.einleitung), x.grafik ? lernBild(x.grafik) : null,
      el('p', { class: 'small' }, el('b', {}, 'Voraussetzungen: '), (x.voraussetzungen || []).map((v) => `${v.thema_schluessel} / ${v.lernziel}`).join(' · ')),
      el('ol', { class: 'lern-exp-teile', type: 'a' }, ...(x.teile || []).map((t) => el('li', {},
        el('p', {}, ...lernMarkiert(t.frage?.text || '')), t.frage?.grafik ? lernBild(t.frage.grafik) : null,
        t.antworten ? el('p', { class: 'small' }, 'Antworten: ' + t.antworten.join(' · ')) : null,
        el('p', {}, el('b', {}, 'Lösung: '), lernMathe(lernLoesungText(t))), t.loesungsweg ? el('p', { class: 'small muted' }, lernMathe(t.loesungsweg)) : null,
        el('p', { class: 'small muted' }, `Bezug: Lernkarte „${t.lernziel}“`))))))) 
      : el('p', { class: 'muted' }, Array.isArray(u.expeditionen) ? 'Noch keine Expeditionen eingespielt.' : 'Noch keine Expeditionen da.'));
}
// K4: Stand einer Etappe in Worten – mit der Zahl der Bordkarten bis „sitzt“ (schule_lernstand.bis_sitzt, Migration D)
function lernEtappeStandText(x) {
  const neu = x.eigene_loesungen !== undefined; const wort = x.sicher ? 'sicher' : neu ? 'gelandet' : 'sitzt'; // W176
  if (x.sitzt) return x.bis_sitzt ? `${wort} – nach ${x.bis_sitzt} ${x.bis_sitzt === 1 ? 'Bordkarte' : 'Bordkarten'}` : wort;
  if (!x.richtig && !x.falsch) return 'noch nicht geübt';
  if (neu) return `${x.eigene_loesungen} eigene Lösungen · ${x.folge || 0} in Folge · ${x.richtig} richtig, ${x.falsch} falsch`;
  return `${x.serie || 0} von ${x.ziel || 6} richtig · ${x.richtig} richtig, ${x.falsch} falsch`;
}

// ---------- Eltern/Lehrer: Info-Seite „So funktioniert’s“ (E-1). Text aus inhalte/pruefung/eltern/info-seite.md, gegen den Code geprüft (Stand 0.80.0). ----------
// Ändert sich eine Regel aus „Wie wird gelernt?“ (Etappe sitzt, Wiederholung, Tests), diesen Text im selben Schritt anpassen.
const LERN_INFO_FRAGEN = [
  ['Worauf baut die App auf?', [
    'Die App deckt Mathematik für drei Schularten ab: Gymnasium Bayern (LehrplanPLUS, Klassen 5–10), Realschule Bayern (LehrplanPLUS, Klassen 5–10) und das IB Middle Years Programme (MYP-Jahr 1–5; entspricht etwa Klasse 6–10, also MYP-Jahr = Klasse − 5; unter Klasse 6: noch kein MYP-Jahr).',
    'Grundlage ist eine Liste aller Mathe-Flüge (über 90). Für jeden Flug ist hinterlegt, in welcher Klasse er in welcher Schulart dran ist, z. B. „Ganze Zahlen: Gym 5 · RS 5 · IB 2“. Der Lehrplan (Nachschlagen auf der Startseite) zeigt alle Flüge auf einer Seite: Klasse 5 bis 10 und alle Themengebiete.',
    'Für jede Schulart ist die Reihenfolge des Lehrplans und der Lernbereich hinterlegt (Gymnasium und Realschule nach LehrplanPLUS Bayern, IB nach dem MYP-Rahmenplan). Beim IB sind manche Zuordnungen als „Annahme“ gekennzeichnet, weil der Rahmenplan dort nicht genau festlegt, in welchem Jahr ein Flug dran ist. Den Lehrplan-Bezug eines Flugs sieht man, wenn man ihn im Lehrplan aufklappt.',
    'Ein Kind lernt jeden Flug nur einmal; er zählt für alle Schularten.']],
  ['Wie ist die Lernreise aufgebaut?', [
    ['Kontinent', ' = ein Bereich der Mathematik (Zahlen = Europa, Geometrie = Afrika …)'],
    ['Ort', ' = eine Stadt mit einem oder mehreren Flügen. Sind alle Flüge eines Ortes geschafft, gibt es einen Stempel.'],
    ['Flug', ' = ein Mathe-Thema, z. B. „Ganze Zahlen“'],
    ['Etappe', ' = ein Lernschritt mit eigener Erklärung'],
    ['Bordkarte', ' = eine Übungsaufgabe'],
    'Jede Etappe hat eine Erklärung (Alltagseinstieg, neue Wörter, Beispiel Schritt für Schritt, typischer Fehler, Merksatz) und im Schnitt etwa 20 Bordkarten in drei Stufen.',
    ['Drei Stufen = drei Arten zu denken:', ' ● leicht – wie im Beispiel oder etwas erkennen; ●● mittel – mehrere Schritte, eine Sachaufgabe, umgekehrt gefragt oder die Darstellung wechseln; ●●● schwer – rückwärts rechnen, mit früherem Stoff verknüpfen, begründen, einen Fehler finden, ein Modell selbst aufstellen oder mit einer Variablen statt einer Zahl. Schwer heißt also ein anderer Gedanke, nicht größere Zahlen. Das Zeichen steht im Kopf jeder Bordkarte; unter „Inhalte ansehen“ steht bei jeder Bordkarte auch ihre Art.'],
    ['Knobel-Bordkarten:', ' freiwillige Zusatzaufgaben auf Wettbewerbsniveau. Nach jeder Landung kommt von selbst eine Knobel-Bordkarte der Etappe (überspringbar mit „Heute keine Knobel-Bordkarte“), außerdem höchstens einmal am Tag „Knobeln des Tages“. Ein Versuch; falsch kostet nichts und zeigt den Lösungsweg. Richtig beim ersten Versuch: 30 Sterne und ein Knobel-Stern im Reisepass. Sie zählen nicht für „sitzt“, Wiederholung oder Test.']]],
  ['Wie wird gelernt?', [
    ['Neue Etappe:', ' Zuerst kommt die Erklärung, danach die Bordkarten.'],
    ['Zweiter Versuch:', ' Bei einem Fehler gibt es zuerst einen zweiten Versuch, ohne Lösung (nicht bei Auswahl-Bordkarten mit nur zwei Antworten). Erst wenn auch er falsch ist, zeigt die App Lösung und Lösungsweg.'],
    ['Etappe gelandet:', ' wenn alles zusammenkommt: 6 eigene Lösungen (richtig im ersten Versuch ohne Tipp; bei Etappen mit wenigen Bordkarten entsprechend weniger, mindestens 2), darunter mindestens 2 verschiedene Arten von Bordkarten und eine schwere Bordkarte (falls die Etappe welche hat), und die letzten 3 Bordkarten in Folge richtig. Es gibt keine Minuspunkte: Ein Fehler setzt nur „in Folge“ auf 0, eigene Lösungen bleiben. Richtig mit Tipp oder im zweiten Versuch zählt nicht, unterbricht aber die Folge nicht. Die Stufe steigt mit den eigenen Lösungen – erst leicht, dann mittel, dann schwer – und wird erst nach 2 Fehlern in Folge eine Stufe leichter. Jede Bordkarte zählt je Etappe nur einmal als eigene Lösung; dieselbe noch einmal richtig heißt „Die kennst du schon – gut wiederholt.“ und zählt für „in Folge“. Das Kind sieht dazu eine Checkliste und, getrennt davon, wie viele Bordkarten es heute selbst gelöst hat.'],
    ['Abschluss einer Etappe:', ' Nach der Landung (und der Knobel-Bordkarte) zeigt die App eine von drei Fassungen – jede mit eigenem Bild und eigener Farbe: Direktflug (alle Bordkarten im ersten Versuch richtig, ohne Tipp, genau so viele wie nötig), Saubere Landung (höchstens 2 endgültige Fehler, Stufe nie leichter geworden, höchstens 4 Bordkarten mehr als nötig; nach „wieder offen“ heißt sie „Wieder gelandet“) oder Sturmflug gemeistert (alles darüber; ohne Fehlerzahl, die Knobel-Bordkarte kommt dann nicht von selbst, nur als Textlink). Dazu ein Abzeichen – ⚡ Direkt, ✓ Sauber oder ⚡ Ausdauer –, das im Reisepass gezählt wird, der Satz „Du kannst jetzt …“ und genau ein Knopf zum nächsten Schritt (nächste Etappe, Flug-Test oder Abflugtafel); zurück in die Übungen derselben Etappe führt von dort kein Weg. Nach dem bestandenen Flug-Test: „Flug geschafft“ mit den Sternen des Flugs und der Liste „Das kannst du jetzt“, danach eine Bordkarte zum nächsten Flug im Plan („Boarding“ öffnet seine erste Erklärung). Mit dem letzten Flug eines Orts kommt dazwischen der Reisepass-Stempel. Landungen vor dieser Version haben kein Abzeichen.'],
    ['Wieder offen:', ' Zwei Fehler in einer fälligen Wiederholung öffnen eine gelandete Etappe wieder – überall: auf der Abflugtafel, in der Etappe, bei den Eltern und für den Flug-Test. Eigene Lösungen und Arten bleiben; es fehlen nur 3 eigene Lösungen in Folge. Ein früher bestandener Test bleibt getrennt als Beleg stehen. Fehler in Mischkarten oder Expeditionen öffnen nie, sie machen die Etappe nur am nächsten Lerntag fällig.'],
    ['Etappe sicher:', ' gelandet, die Wiederholung nach 14 Lerntagen bestanden und – beides nach der letzten Landung – einmal in einer Mischkarte richtig erkannt und im Nachtest des Flugs die Bordkarte dieser Etappe richtig. Ist nur der Nachtest des Flugs bestanden, steht bei den Eltern „Flug-Nachtest bestanden“.'],
    ['Reisekarte:', ' die Startseite des Kindes ist eine echte Landkarte (ohne Google, ohne Kartenserver): Welt › Kontinent › Land. Jedes Land mit Flug ist ein Flaggen-Pin (Kopf = Flagge, Spitze = Hauptstadt, bei Landesteilen der Hauptort); die Farbe zeigt den Stand – blau gerade dran, gelb im Plan (mit Platznummer), grün geschafft (noch in Wiederholung), ◉ „kann er“, gold = alles sitzt, „+“ = Zusatz. Geteilte Themen liegen in Nachbarländern („1/2“, „2/2“, feine Kette). Land antippen → „Städte in … ansehen“: die Städte der Reise als nummerierte Haltestellen mit Stand, gestrichelt die Kür. Der gelbe Startknopf schwebt unten in der Karte (Rechner: rechte Spalte) und führt wie bisher – erst der Check-in, dann das Thema bzw. der Flug-Test; eine offene Expedition steht darüber. In der Welt-Ansicht zeigt die Antarktis die Stationen der Expeditionen. Verschieben mit Finger oder Maus, Zoomen mit zwei Fingern, Mausrad oder + / −. Der Schalter „Abflugtafel“ zeigt bis zur Freigabe die bisherige Tafel (je Kind auf dem Gerät gemerkt). Quellen: Ländergrenzen Natural Earth (gemeinfrei); Städte und ihre Lage GeoNames (CC BY 4.0); Antarktis-Stationen COMNAP Antarctic Facilities (nur private, nicht kommerzielle Bildungs-Nutzung); Flaggen flag-icons, Ländernamen i18n-iso-countries, Kontinente countries-list (MIT) – Lizenztexte in karte/LIZENZEN.md.'],
    ['Expeditionen:', ' größere Bordkarten aus 3–5 Teilen (a, b, c …), die Stoff aus mehreren Etappen verbinden – wie in einer Schulaufgabe mit Teil a, b, c. Sobald alle ihre Etappen beim Kind gelandet sind, ist die Expedition freigeschaltet: Nach der Landung, die das auslöst, kommt einmal die Ansicht „Expedition freigeschaltet“ (großer Knopf „Jetzt starten“, kleiner Textlink „Später“). Solange sie offen ist, steht sie als oberste und größte Karte auf der Abflugtafel, vor dem nächsten Flug; nach „Später“ steht bis zum Ende des Lerntags nur ein kleiner Hinweis da, am nächsten Lerntag ist die Karte wieder oben. Auf der Kinderseite steht nirgends „freiwillig“ – die Regel bleibt trotzdem: Eine Expedition sperrt nichts und zählt nicht für „gelandet“. Jeder Teil hat zwei Versuche, danach steht die Lösung da und es geht mit dem nächsten Teil weiter (jeder Teil nennt seine Zahlen selbst). Richtig im ersten Versuch ist ein Beleg für die Etappe; falsch macht sie am nächsten Lerntag zur Wiederholung fällig – ohne Abzüge. Eine begonnene Expedition kann das Kind auch dann zu Ende führen, wenn eine ihrer Etappen inzwischen wieder offen ist. Gebucht wird auf die Version der Etappe, die beim Kind gelandet ist. Geschafft: Expeditions-Stempel und 150 Sterne, 200 Sterne bei fehlerfreiem Lösen (alle Teile im ersten Versuch, ohne Tipp; Werte vom Server). Jede Expedition gehört zu einer Forschungsstation in der Antarktis; der Reisepass zeigt die Stempel-Sammlung „k von 21 Stationen“ – gesperrte Stationen zeigen, welche Etappen noch fehlen. Quelle der Stationen: COMNAP Antarctic Facilities (nur private, nicht kommerzielle Bildungs-Nutzung). Alle Expeditionen mit Lösungen: Lehrplan → „Expeditionen ansehen“.'],
    ['Mischkarten:', ' Sind im Flug mindestens 3 Etappen gelandet, ist beim Üben jede 4. Bordkarte (bis Klasse 6 jede 6.) eine aus einer anderen Etappe, die schon gelandet ist – meist aus demselben Flug oder Kontinent, manchmal aus einem älteren Flug. Sie ist gekennzeichnet („Aus deiner Reise – erkennst du, was gefragt ist?“), nach der Lösung steht, aus welcher Etappe sie kam. Das Kind soll selbst erkennen, welches Verfahren passt. Sie zählt nicht für die gerade geübte Etappe; richtig ist ein Beleg für „sicher“, falsch macht die Herkunfts-Etappe am nächsten Lerntag zur Wiederholung fällig – ohne Abzüge. Ist die Herkunfts-Etappe gerade fällig und die Mischkarte im ersten Versuch ohne Tipp richtig, zählt sie als bestandene Wiederholung dieser Etappe – Mischkarten bauen so fällige Wiederholungen mit ab. Der Server prüft jede Mischkarte (Etappe gelandet, Stufe 2–3, nicht die gerade geübte); sonst zählt sie wie eine normale Bordkarte.'],
    ['Wiederholung:', ' Ist eine Etappe gelandet, kommt sie nach 1, 3, 7, 14 und 30 Lerntagen wieder, jeweils mit einer Bordkarte. Ein Lerntag ist ein Tag, an dem das Kind Mathe übt; Reisetage ohne Mathe zählen nicht. Am Anfang eines Lerntags kommt eine Runde: sind höchstens 6 Etappen fällig, alle; sonst ein Fünftel der fälligen (aufgerundet), mindestens 6 und höchstens 12 (bis Klasse 6 höchstens 10) – zuerst Etappen mit einem Wiederholungs-Fehler, dann die am längsten fälligen. Weitere werden nur angeboten. Auf der Kinderseite heißt die Runde „Check-in“: Das Kind sieht, wie weit es ist („3 von 9“), nie die Zahl aller fälligen Etappen. Es kann unterbrechen und am selben Lerntag fortsetzen, auch auf einem anderen Gerät; erledigt ist die Runde, wenn alle ihre Bordkarten beantwortet sind (falsch zählt als bearbeitet). Ein Fehler: Die Etappe kommt am nächsten Lerntag wieder. Zwei Fehler hintereinander: Das Kind übt sie noch einmal – eigene Lösungen bleiben, es braucht wieder 3 richtige in Folge.'],
    ['Endgültig abgelegt:', ' Besteht eine Etappe auch die letzte Wiederholung (nach 30 Lerntagen), ist sie abgelegt: Sie fällt aus der regelmäßigen Wiederholung und wird nur noch bei Bedarf aufgefrischt, das Kind bekommt 30 Sterne und eine kurze Einblendung. Sind alle Etappen eines Flugs abgelegt: 100 Sterne, eine große Einblendung, und der Flug steht im Reisepass golden. Sind alle Flüge eines Orts abgelegt, wird auch der Stempel des Orts golden. Fällt eine abgelegte Etappe später im Nachtest oder beim Üben auf, kommt sie am nächsten Lerntag wieder zur Wiederholung; Gold und Sterne bleiben, ein zweites Ablegen bringt nichts.'],
    ['Flug-Test:', ' Ist die letzte Pflicht-Etappe gelandet, führt der Landebildschirm nur noch zum Test („Weiter: Flug-Test“): eine Bordkarte je Etappe, ohne Tipps. Im Ergebnis ist jede Antwort deutlich als RICHTIG oder FALSCH markiert. Bei Fehlern zwei Wege: „Erst üben: ‹Etappe›“ oder „Gleich verbessern“. Alles richtig verbessert → Flug geschafft.'],
    ['Nachtests:', ' später, nach Lerntagen gezählt (nach 10, 25 und 60 Lerntagen); alle Etappen des Flugs, ohne Tipps. Ab 80 %: bestanden. 60–79 %: wiederholen. Unter 60 %: automatische Rückreise im Flugplan.'],
    ['Sterne:', ' Jede Übungsaufgabe bringt einmal Sterne: 10 ★, wenn sie im ersten Versuch ohne Tipp gelöst ist, sonst 5 ★. Bei jeder Landung einer Etappe gibt es einmal einen Landungs-Bonus: +80 ★ ohne Fehler, +40 ★ mit 1–2 Fehlern, sonst +10 ★. Tipps zählen nicht als Fehler. Tests, Wiederholungen und Mischkarten zählen hier nicht mit. Wiederholungen bringen 10 ★, wenn sie selbst gelöst sind (mit Tipp oder im zweiten Versuch: keine Sterne, die Etappe kommt am nächsten Lerntag wieder). Für Etappen, die vor dem 22.11. gelandet sind, wurde der Bonus einmal nachgetragen. Gebuchte Sterne werden nie abgezogen.'],
    ['Belohnungen:', ' 20 Sterne für jede richtige Bordkarte im Test, 30 Sterne für eine endgültig abgelegte Etappe, 100 Sterne für einen abgelegten Flug, 30 Sterne für eine Knobel-Bordkarte beim ersten Versuch, 100 Sterne und ein Stempel für jeden geschafften Ort. Welche Belohnungen es gibt, legen die Eltern fest, und sie bestätigen jede Einlösung.'],
    'Keine Zeitvorgaben, keine Uhr, keine Ranglisten.']],
  ['Wie entstehen die Inhalte, und wer prüft sie?', [
    'Erklärungen und Bordkarten erstellt eine KI (Claude) nach festen Regeln: Bezug zum Lehrplan, Alltagseinstieg, einfache Sprache, jede Lösung vom Programm berechnet und geprüft.',
    'Ein neuer Flug ist zuerst „in Prüfung“: Nur das Testkind sieht ihn. Nach der Freigabe ist er „fertig“ und für alle Kinder da. Der Lehrplan (Nachschlagen auf der Startseite) zeigt alle Flüge als Übersicht: Zeilen Klasse 5–10, Spalten die Themengebiete, eingeordnet nach Gymnasium, Realschule oder IB, in der Reihenfolge des Lehrplans. Der Filter „Inhalt“ zeigt, was fertig ist (●), was in Prüfung ist (◐) und was noch fehlt (○). Ein Thema antippen: was gefordert ist, was es vorher braucht, worauf es aufbaut, Lernbereich und „Inhalte ansehen“. Mit „Lernstand“ steht bei jedem Thema die Stufe eines Kindes (◉ ↻ ▶ ○ +) – ist ein Kind gewählt, lässt sich der Plan dort direkt ändern.',
    'Jeder Inhalt ist mit allen Lösungen einsehbar („Inhalte ansehen“). In einem fertigen Flug sind Bordkarten, die ersetzt wurden oder überzählig sind, „aussortiert“: Sie werden nie ausgegeben, zählen nicht mit und stehen zugeklappt am Ende der Etappe.']],
  ['Was kann ich selbst ändern?', [
    ['Lehrplan je Kind', ' (Reiter „Lehrplan“ auf der Seite des Kindes – ersetzt „Stand“ und „Plan“): oben die Leiste „Lehrplan von:“ (Gymnasium | Realschule | IB MYP; Standard = Schulart des Kindes; ⓘ: nach welchem Lehrplan die Themen den Klassen zugeordnet werden – z. B. steht „Satz des Pythagoras“ im Gymnasium in Kl. 8, in der Realschule in Kl. 9; gezeigt werden immer alle Themen), „Zeigen“ (Alle Themen | Noch nicht im Plan · n | Im Plan · n – hebt hervor, nichts verschwindet), „Klassen“ 5–10 zum An- und Abschalten (Standard: Klasse des Kindes bis 10, je Kind auf dem Gerät gemerkt; ein blauer Punkt zeigt Themen aus dem Fahrplan), „Bereit für Klasse …?“ (hebt hervor, was bis zu dieser Klasse fehlt – Orientierung, keine Einstufung durch eine Schule), Suchen, „Auswählen“ und „ⓘ Farben“. Am Rechner steht das in zwei festen Zeilen; Hinweise und Farben öffnen als schwebendes Feld, die Matrix springt nicht. „Gespeichert“ erscheint nicht mehr, nur „Speichere …“ oder „Nicht gespeichert“. Links der Fahrplan: ▶ Gerade dran mit Fortschritt, darunter ○ Kommt noch nummeriert (am Griff ⋮⋮ ziehen oder ↑ ↓), unten zugeklappt ↻ In Wiederholung und ✓ Fertig (kann er) mit „Wieder in die Wiederholung“. Rechts die Matrix: Spalten = Themengebiete, Zeilen = Klassen; links je Klasse drei Ringe (groß die gewählte Schule, klein die beiden anderen): gelandete Etappen von allen Etappen der Pflichtthemen dieser Schule in dieser Klasse (IB: MYP-Jahr = Klasse − 5). Ganz gekonnte Klassen stehen eingeklappt als eine Zeile. Farben der Karten: blau = gerade dran, hellgelb mit Platznummer = im Plan, hellgrün = Wiederholung, durchsichtig = fertig, weiß = Lehrplan der gewählten Schule, grau = nur andere Schule. Ein Thema antippen öffnet rechts die Schublade (auf dem Handy ein Blatt von unten): Stand mit jeder Etappe, Planen („In den Plan: als Nächstes ▾“ mit „… ans Ende“ und „… nach Lehrplan einsortieren“; im Plan „Als Nächstes“, „Ans Ende“, „Aus dem Plan“), Stufe (Lernen | Kann er – wiederholen | Kann er komplett; bei ◉ „Wieder in die Wiederholung“), Lehrstoff und Zusammenhang. „Kann er – aber wiederholen“: keine Übung, nur die Wiederholungen; zwei Fehler hintereinander → wieder offen; je Lerntag kommen höchstens 6 solche Etappen neu in den Takt. Für so gesetzte Flüge gibt es keinen Flug-Test und keine Nachtests. Ist die Wiederholung nach 14 Lerntagen bestanden (und eine Mischkarte richtig, falls eine kam), steht der Flug auf ◉. „Wieder in die Wiederholung“ holt einen ◉-Flug zurück; die Wiederholungen beginnen dann wieder nach 1 Lerntag. „Auswählen“: Karten antippen setzt Häkchen; oben dann die Knöpfe für alle ausgewählten auf einmal (ein Schritt, ein „Rückgängig“). Jede Änderung wird sofort gespeichert; unten erscheint 5 Sekunden „↶ Rückgängig“ (oben rechts dauerhaft, nur für den letzten Schritt). Hat jemand anderes den Plan inzwischen geändert, meldet die App das und überschreibt nichts – dann „Neu laden“. Ziehen: eine Karte aus der Matrix in den Fahrplan ziehen plant sie an dieser Stelle ein (blaue Linie); einen Eintrag aus dem Fahrplan zurück in die Matrix ziehen nimmt ihn aus dem Plan (Matrix rot gestrichelt). Bei „Noch nicht im Plan“ steht oben im Fahrplan „Alle n einplanen (nach Klasse und Lehrplan)“ – nur für die gewählten Klassen, ohne Zusatz-Teile. Reihenfolge-Warnung (keine Sperre): Steht ein Thema vor seiner harten Voraussetzung, ist die Voraussetzung weder gekonnt noch im Plan oder wird sie hinter ein darauf aufbauendes Thema geschoben, erscheint unten eine dunkelrote Meldung mit Knopf zum Reparieren („… davor setzen“, „… davor einplanen“, „… dahinter setzen“); solange der Konflikt besteht, hat der Eintrag im Fahrplan einen roten Rand mit „braucht … – kommt erst auf Platz n“ bzw. „– nicht gelernt, nicht im Plan“. Empfohlene Voraussetzungen warnen nicht. Bis zum Reise-Aufbau ist ein Platz ein Ort; mehrere Themen eines Orts heißen „3a, 3b …“. Geteilte Themen: jeder Teil ist ein eigenes Thema („Terme umformen – Teil 2 von 3“, auf der Karte „2/3“); Teil 2 baut auf Teil 1 auf. „Zusatz“ = Teil ohne Lehrplan-Punkt in der gewählten Schulart: gestrichelt, zählt nicht im Ring und nicht bei „Noch nicht im Plan“. Die Seite des Kindes hat eine Kopfzeile: Zurück · Kinder-Umschalter (am Rechner mit „Schulart · Klasse“ bei jedem Kind) · Reiter Überblick | Was wackelt | Lehrplan · Lernen starten, ⚙ Einstellen und ⓘ rechts; auf Tablet und Handy eine Zeile ‹ · Kinder · ⋯ (Lernen starten, Einstellen, So funktioniert’s), darunter die Reiter. Matrix und Fahrplan füllen das Fenster bis unten. Kinder-Umschalter: ein Klick auf ein Kind (am Rechner auch Alt+← / Alt+→) wechselt das Kind, der gewählte Reiter bleibt; die Markierung wechselt sofort, der bisherige Inhalt bleibt abgeblendet stehen, bis der neue da ist. Die App merkt sich je Sitzung Übersicht, Lehrplan und die Daten je Kind und lädt das andere Kind schon vorab; nach jeder Änderung liest sie gezielt neu, im Hintergrund frischt sie alle 10 Sekunden auf; Schule und Klassen übernehmen die Werte des Kindes, Detail und Auswahl schließen, „Rückgängig“ verfällt. Auf dem Handy ist nur das aktive Kind ausgeschrieben. Tablet: Fahrplan über den Knopf „Fahrplan · n“; Tablet und Handy: „Lehrplan von“, Zeigen, Klassen, Einstieg, Suchen und Auswählen im Blatt „Filter ▾“, Farben hinter ⓘ; Handy: Umschalter „Fahrplan | Alle Themen“.'],

    ['Was wackelt', ' (Reiter auf der Seite des Kindes): eine Arbeitsliste in drei Bereichen – Zu besprechen · Beobachten · Besprochen. Je Eintrag (ein Thema, oder eine Etappe mit eigenem Status) Etappe, Anzahl Fehler und wann; Knöpfe „✓ Besprochen“, „Beobachten“ (bzw. „Zu besprechen“) und „Im Lehrplan“ (öffnet den Reiter „Lehrplan“ mit dem Thema; auf dem Handy kurz „→ Lehrplan“). Die Wochenzahlen stehen im Überblick. „Bordkarte und Antwort“ klappt die letzten falschen Antworten auf. Der Status wird gespeichert (5 Sekunden „↶ Rückgängig“); neue Fehler im selben Thema holen einen Eintrag von selbst zurück nach „Zu besprechen“ („wieder offen“). Die rote Zahl am Reiter zählt „Zu besprechen“. Darunter zugeklappt wie bisher'],
    ['Was wackelt – je Etappe', ': eine Tabelle aller Etappen mit falschen Antworten – wackelnde zuerst – mit „richtig / falsch“, dem häufigsten Fehler (Vorzeichen, Komma, vertauscht, gerundet, Einheit; nur wenn er mindestens zweimal vorkam) und seit wann. Antippen zeigt die letzten 3 falschen Antworten, „Kurz gesagt“ der Etappe und „Erklärung ansehen“. „Besprochen ✓“ merkt Datum und Person und nimmt die Etappe aus „Zu tun“ – bis wieder eine Antwort endgültig falsch ist.'],
    ['⚙ Einstellen', ' (in der Zeile des Kindes auf der Startseite und oben auf seiner Seite): Hauptschulart und Klasse („bestimmt seine Klasse in Lernreise und Plan“), Stand messen gegen … (Stufe je Schulart, nur für „Wo steht es?“), Notizen und Verlauf, Neuer Plan aus Lehrplan-Vorlage (mit Rückfrage und „↶ Rückgängig“). Alles speichert sofort.'],
    'Inhalte werden nicht direkt geändert, sondern beauftragt (nächste Frage). Belohnungen und Zugänge verwalten nur Eltern.']],
  ['Wie beauftrage ich eine Änderung?', [
    'An der betroffenen Stelle „✎ Ändern lassen“ tippen – derselbe Knopf an Erklärung, Etappe, Bordkarte, Flug und Flugplan; der Auftrag weiß dann, worum es geht. An einzelnen Bordkarten steht er in der Lernreise eines Kindes (am einfachsten beim Testkind). Für Flüge ohne Inhalt steht er im Lehrplan, wenn man das Thema antippt, mit „Neuer Flug“ vorbelegt. Allgemeine Wünsche: „Meine Aufträge“ → „Neuer Auftrag“.',
    'Art wählen (Erklärung, Bordkarten, Fehler, Neuer Flug, Sonstiges), bei Bedarf eine Vorlage antippen (z. B. „Schwieriger“, „Lösung falsch“) und in einem Satz sagen, was anders sein soll.',
    'Die Entwicklung (Eltern mit KI) bearbeitet den Auftrag. Status: offen → in Arbeit → erledigt oder nicht umgesetzt, jeweils mit Antwort – alles unter „Meine Aufträge“.',
    'Neue Antworten stehen auf der Startseite unter „Neue Antworten auf eure Aufträge“.',
    'Gute Aufträge nennen ein Beispiel: „Bordkarte 7: Lösung muss −56 sein“ statt „Fehler im Flug“.']],
  ['Wer hat Zugang, und wie steht es um den Datenschutz?', [
    'Ein Lern-Code öffnet nur den Bereich Lernen; für alle anderen Bereiche der App lehnt der Server ihn ab. Eltern legen Codes an (für Lehrer, Eltern oder ein Kind) und können sie jederzeit sperren. Ein Kind-Code öffnet nur die eigene Lernreise.',
    'Code und Link getrennt weitergeben.']],
];

async function viewInfo(arg) {
  setChrome('So funktioniert’s', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const u = await lernCall('schule_uebersicht').catch(() => null);
  if (!live()) return;
  const kinder = (u?.lernende || []).filter((k) => !k.ist_test);
  const jeKind = (reiter, wort) => kinder.length ? el('div', { class: 'lern-info-links' }, ...kinder.map((k) => el('a', { href: `#/kind/${k.id}-${reiter}` }, `${wort} ${k.name} ›`)))
    : el('a', { href: '#/lernen' }, 'Zur Startseite ›');
  const schritt = (nr, titel, text, ...ziel) => el('article', { class: 'card lern-info-schritt' },
    el('span', { class: 'lern-info-nr', 'aria-hidden': 'true' }, String(nr)), el('h3', {}, titel), el('p', { class: 'small' }, text), ...ziel);
  const zeile = (x) => Array.isArray(x) ? el('li', {}, el('b', {}, x[0]), x[1]) : el('li', {}, x);
  lernErsetze(main,
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'FÜR ELTERN UND LEHRER'), el('h2', {}, 'So funktioniert’s'),
      el('p', {}, 'Die Lernreise in Kürze: erst die vier wichtigsten Schritte, darunter Antworten auf die häufigsten Fragen.'),
      el('p', {}, el('b', {}, 'Startseite: '), 'Oben „Zu tun“ – rot: seit 3 Tagen kein Lerntag oder eine Rückreise (Nachtest nicht bestanden); gelb: eine Etappe wackelt und ist noch nicht besprochen; blau: ein Wunsch eines Kindes, eine Belohnung einzulösen (Bestätigen oder Ablehnen direkt im Eintrag), oder eine neue Antwort auf einen Auftrag. Darunter je Kind eine Zeile: Lernt (Lerntage diese Woche, zuletzt), Wackelt, Stand in Gymnasium, Realschule und IB MYP (Prozent der Flüge der Klasse, die gelandet sind) und was jetzt dran ist. Auf dem Handy steht statt der Tabelle je Kind eine Karte.'),
      el('p', {}, el('b', {}, 'Reisetage und Pausen: '), 'Über „+ Reisetag eintragen“ in „Zu tun“ oder im „⚙ Einstellen“ des Kindes lassen sich Tage ohne Lernen eintragen (für ein Kind oder alle); sie zählen nicht für „Lernt“ und „kein Lerntag seit …“, dort steht dann „Pause bis …“. Ein Pausentag gilt für den ganzen Kalendertag am Ort des Kindes (Ortszeit, nicht die Uhr der Eltern). Lernregeln, Wiederholungen und Nachtests ändern sich dadurch nicht.'),
      el('p', {}, el('b', {}, 'Seite des Kindes: '), 'Eine Zeile antippen öffnet sie, mit drei Reitern: Überblick (oben Karten mit Sprüngen: Gerade dran → „Im Lehrplan öffnen“, Als Nächstes → „Fahrplan ändern“, Zu besprechen → „Zu Was wackelt“, Diese Woche mit „zuletzt am …“ und Farbe, Zuletzt geschafft, Stand mit Ringen um die Klasse des Kindes und der Einstufung je Schulart in einer Zeile), Was wackelt und Lehrplan. „⚙ Einstellen“ in der Zeile und oben auf der Seite des Kindes: Schulart, Klasse, Stufen, Notizen.'),
      el('p', {}, el('b', {}, 'Lernen starten: '), 'Im Eltern-Zugang hat jede Zeile und die Seite des Kindes den Knopf „Lernen starten“ – er öffnet die Abflugtafel des Kindes. Im Lehrer-Zugang steht dort klein „Lernreise ansehen“.')),
    el('h3', {}, 'Erste Schritte'),
    el('div', { class: 'lern-info-schritte' },
      schritt(1, 'Lehrplan und Fahrplan', 'Reiter „Lehrplan“ auf der Seite des Kindes – das ist dein Arbeitsplatz: links der Fahrplan (▶ Gerade dran · ○ Kommt noch; ziehen oder ↑ ↓), rechts alle Themen als Matrix (Themengebiete × Klassen) mit Ringen je Klasse. Thema antippen: Stand, Planen, Stufe, Lehrstoff. Viele auf einmal: „Auswählen“. Jede Änderung wird sofort gespeichert.', jeKind('lehrplan', 'Lehrplan')),
      schritt(2, 'Lernstand lesen', 'Im Reiter „Lehrplan“ zeigen Karten und Ringe, wo das Kind steht; „Bereit für Klasse …?“ hebt hervor, was bis zu einer Klasse fehlt (Orientierung, keine Einstufung durch eine Schule). Reiter „Was wackelt“: je Etappe, was sitzt und was wackelt, mit den echten falschen Antworten. Alle Kinder nebeneinander: die Tabelle auf der Startseite.', jeKind('wackelt', 'Was wackelt')),
      schritt(3, 'Inhalte ansehen', 'Im Lehrplan ein Thema antippen, dann „Inhalte ansehen“: jede Etappe mit ihrer Erklärung und alle Bordkarten mit Lösung.', el('a', { href: '#/lehrplan' }, 'Lehrplan ›')),
      schritt(4, 'Ändern lassen', 'Fehlt etwas oder stimmt etwas nicht? Mit „✎ Ändern lassen“ direkt an der Stelle beauftragen; Status und Antwort stehen unter „Meine Aufträge“.', el('a', { href: '#/lernauftraege' }, 'Meine Aufträge ›'))),
    el('h3', {}, 'Fragen'),
    ...LERN_INFO_FRAGEN.map(([frage, teile], i) => el('details', { class: 'card lern-info-frage' },
      el('summary', {}, frage), el('ul', {}, ...teile.map(zeile)))));
  if (arg === 'stufen') { // LB Teil 8: „Stufe ⓘ“ im Lehrplan führt hierher
    const d = [...main.querySelectorAll('details.lern-info-frage')].find((x) => x.querySelector('summary')?.textContent === 'Was kann ich selbst ändern?');
    if (d) { d.open = true; d.id = 'info-stufen'; d.scrollIntoView({ block: 'start' }); }
  }
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
  // Teil 4: in fertigen Flügen sind gesperrte Bordkarten aussortiert (ersetzt oder überzählig) – gezählt werden nur aktive
  if (['geprueft', 'freigegeben'].includes(e.status)) return { k: 'fertig', text: `Fertig · ${e.karten} Etappen · ${Math.max(0, (e.aufgaben || 0) - (e.neu || 0))} Bordkarten` };
  return { k: 'pruefung', text: `In Prüfung · ${e.karten} Etappen · ${e.aufgaben} Bordkarten` };
}
// ---------- LM-1 bis LM-5 (21.11.): Lehrplan-Matrix „Mathe 5–10“ für Eltern/Lehrer – ersetzt die Lehrplan-Übersicht (LB-1) ----------
// Zeilen Klasse 5–10, Spalten Themengebiete (oder umgekehrt), alle Themen; „Einordnen nach“ bestimmt die Zeile. Thema antippen: Detail mit Verbindungen,
// Lernstand je Kind und (genau ein Kind gewählt) den Stufen-Knöpfen wie im Plan. Vorlage: inhalte/pruefung/lehrer/matrix/entwurf/lehrplan-matrix.html.
const LERN_MX_GEB = ['Zahlen', 'Algebra', 'Funktionen', 'Geometrie', 'Fläche und Raum', 'Geld und Verhältnisse', 'Daten und Zufall', 'Entdecker-Inseln'];
const LERN_MX_KL = [5, 6, 7, 8, 9, 10];
const LERN_MX_SA = { gym_by: ['Gymnasium', 'Gym'], rs_by: ['Realschule', 'RS'], ib_myp: ['IB MYP', 'IB'] };
let lernMx = null; // Zustand über Seitenwechsel: { sa, kind, sel, q }
let lernPlanZiel = null; // „Im Plan öffnen ›“: { kind, thema } – viewPlan klappt das Thema auf
const lernMxSpeicher = (k, v) => { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch { /* ohne Speicher */ } return null; };
// Laden: LM-S 2 – Raster über schule_lehrplan_matrix (themen knapp: thema_id, titel, gebiet_id, block_id, einheit_id | ohne_flug, etappen_anzahl, jahrgang …;
// verbindungen als Tripel [thema_id, braucht_id, "h"|"e"]; gebiete[] mit Titel; lernstand[kind][thema]) und dazu die Lehrplan-Übersicht (Ort, Kurzbeschreibung,
// Inhaltsstand ● ◐ ○ und Aufträge je Flug, die das Raster nicht hat). Das Detail (lernMxThema) kommt beim Antippen über schule_lehrplan_thema.
// Kennt der Server LM-S noch nicht, trägt die Übersicht allein (ohne Verbindungen).
async function lernMxLaden(mitTest = false) {
  const [m, u] = await Promise.all([lernCall('schule_lehrplan_matrix', mitTest ? { mit_testkind: true } : {}).catch(() => null), lernCall('schule_lehrplan_uebersicht').catch((err) => ({ fehler: err }))]);
  if (!Array.isArray(m?.themen)) { if (u?.fehler) throw u.fehler; return u; }
  const ueb = new Map(); for (const t of (u?.themen || [])) if (!ueb.has(t.thema_id)) ueb.set(t.thema_id, t);
  const geb = new Map((m.gebiete || []).map((g) => [g.gebiet_id, g.titel]));
  const kinder = m.kinder || [];
  const verbindungen = (m.verbindungen || []).map((v) => (Array.isArray(v) ? { thema_id: v[0], braucht_id: v[1], art: v[2] === 'e' || v[2] === 'empfohlen' ? 'empfohlen' : 'hart' } : v));
  return { kinder, gebiete: m.gebiete, verbindungen, matrix: true,
    themen: m.themen.map((t) => { const x = ueb.get(t.thema_id) || {}; const n = t.etappen_anzahl ?? (Array.isArray(t.etappen) ? t.etappen.length : 0);
      return { ...t, gebiet: t.gebiet || geb.get(t.gebiet_id) || x.gebiet, ort: t.ort ?? x.ort, beschreibung: t.was_gefordert ?? x.beschreibung,
        gliederung: t.etappen ? undefined : x.gliederung, rueckmeldungen: x.rueckmeldungen || 0, stand: x.stand, geplant: x.geplant,
        einheit: x.einheit !== undefined ? x.einheit : t.einheit_id ? { id: t.einheit_id, status: 'geprueft', karten: n, aufgaben: 0, neu: 0 } : null,
        // „Etappe x von y“: y = etappen_anzahl (LM-S 2 lässt etappen im Lernstand weg)
        stufe: Object.fromEntries(kinder.map((c) => { const s = m.lernstand?.[c.id]?.[t.thema_id]; return [c.id, s ? { ...s, etappen: s.etappen ?? (n || undefined) } : s]; }).filter(([, v]) => v)) }; }) };
}
// Adapter: Felder von schule_lehrplan_matrix (LM-S) und – ohne LM-S – von schule_lehrplan_uebersicht (beschreibung, gliederung [Titel]) an einer Stelle.
function lernMxDaten(d) {
  const liste = (v) => (Array.isArray(v) ? v.filter(Boolean) : v ? String(v).split(' · ').filter(Boolean) : []);
  const themen = (d.themen || []).map((t) => ({
    id: t.thema_id, titel: t.titel, gebiet: t.gebiet || 'Weitere', jg: t.jahrgang || {}, r: t.lehrplan_reihenfolge || {}, lb: t.lernbereich || {},
    umfang: t.umfang || t.beschreibung || '', lp: (sa) => liste(t.lehrplan?.[sa]), merke: (Array.isArray(t.merke) ? t.merke : []).map((m) => (typeof m === 'string' ? m : m?.text || '')).filter(Boolean),
    // eigenstaendig: Begründungstext (LM-S 2; gesetzt ⇒ eigenständig), früher true; ohne_flug: aufgelöster Entwurf ohne freigegebenen Inhalt → blass
    beispiel: t.beispiel || null, eigen: t.eigenstaendig === true || (typeof t.eigenstaendig === 'string' && t.eigenstaendig.trim() ? t.eigenstaendig.trim() : false),
    ohneFlug: t.ohne_flug === true, pflicht: Array.isArray(t.pflicht) ? t.pflicht : null,
    etappen: (Array.isArray(t.etappen) && t.etappen.length ? t.etappen : t.gliederung || []).map((e) => (typeof e === 'string' ? { titel: e } : { titel: e?.titel || '', pflicht: e?.pflicht })),
    roh: t }));
  const verb = Array.isArray(d.verbindungen) ? d.verbindungen : Array.isArray(d.voraussetzungen) ? d.voraussetzungen : null;
  const by = new Map(themen.map((x) => [x.id, x])); const vor = new Map(), nach = new Map();
  for (const v of verb || []) { const a = Number(v.thema_id), b = Number(v.braucht_id); if (!by.has(a) || !by.has(b)) continue;
    const e = { art: v.art === 'empfohlen' ? 'empfohlen' : 'hart', bg: v.begruendung || '' };
    vor.set(a, [...(vor.get(a) || []), { id: b, ...e }]); nach.set(b, [...(nach.get(b) || []), { id: a, ...e }]); }
  const gebiete = Array.isArray(d.gebiete) && d.gebiete.length ? [...d.gebiete].sort((a, b) => (a.reihenfolge ?? 999) - (b.reihenfolge ?? 999)).map((g) => g.titel) : null;
  return { themen, by, vor, nach, hatVerb: !!verb, gebiete };
}
// Klasse eines Themas in einer Schulart (IB: MYP-Jahr + 5) und Einordnung, wenn die Schulart es nicht hat
const lernMxKl = (x, sa) => { const v = Number(x.jg[sa]); return v ? (sa === 'ib_myp' ? v + 5 : v) : null; };
function lernMxZusatz(x, sa) {
  if (lernMxKl(x, sa)) return null;
  const [name] = LERN_MX_SA[sa]; const rein = (k) => Math.min(10, Math.max(5, k));
  const ib = Number(x.jg.ib_myp);
  if (x.gebiet === 'Entdecker-Inseln') { const k = ib ? ib + 5 : lernMxKl(x, 'gym_by') || lernMxKl(x, 'rs_by') || 10;
    return { k: rein(k), marke: 'Insel', text: `Entdecker-Insel: freiwilliges Knobelthema, in keinem bayerischen Lehrplan.${ib ? ` Eingeordnet nach IB MYP ${ib} ≈ Kl. ${ib + 5}.` : ''}` }; }
  for (const s of (sa === 'ib_myp' ? ['gym_by', 'rs_by'] : [sa === 'gym_by' ? 'rs_by' : 'gym_by', 'ib_myp'])) {
    const k = lernMxKl(x, s); if (!k) continue;
    if (s === 'ib_myp') return { k: rein(k), marke: 'IB', text: `Stoff aus dem IB-Programm (MYP ${ib} ≈ Kl. ${k}), in Bayern nicht in Klasse 5–10 vorgesehen. Eingeordnet nach dem MYP-Jahr.` };
    return { k: rein(k), marke: LERN_MX_SA[s][1], text: `Stoff der ${LERN_MX_SA[s][0]} (dort Kl. ${k}), im Lehrplan ${name} nicht vorgesehen. Eingeordnet nach der Klasse an der ${LERN_MX_SA[s][0]}.` };
  }
  return { k: 10, marke: '?', text: 'Keine Klasse hinterlegt.' };
}
const lernMxZeile = (x, sa) => lernMxKl(x, sa) || lernMxZusatz(x, sa).k;
// Stufe je Kind (Server: stufe; sonst aus Stand und Plan geschätzt – wie bisher in der Lehrplan-Übersicht)
const lernMxStufe = (x, c) => { const s = x.roh.stufe?.[c.id]; if (s) return s; const st = x.roh.stand?.[c.id]; const geplant = (x.roh.geplant || []).includes(c.id);
  return { stufe: st === 'erledigt' ? 'wiederholung' : st === 'laeuft' ? 'dran' : geplant ? 'kommt' : 'nicht_im_plan', geschaetzt: true }; };
// „▶ Etappe 3 von 7“, „↻ Wdh 2 von 5“ … – kurz auf der Karte
function lernMxStandText(s) {
  switch (s.stufe) {
    case 'komplett': return s.gesetzt === 'komplett' ? '◉ gesetzt: kann er komplett' : '◉ kann er komplett';
    case 'wiederholung': return s.wdh_nr ? `↻ Wdh ${s.wdh_nr} von 5` : '↻ in Wiederholung';
    case 'dran': return s.etappen ? `▶ Etappe ${s.etappe_jetzt || Math.min((s.gelandet || 0) + 1, s.etappen)} von ${s.etappen}` : '▶ gerade dran';
    case 'kommt': return '○ kommt noch';
    default: return '+ nicht im Plan';
  }
}
const lernMxMarke = (c) => { const w = String(c.name || '').trim().split(/\s+/); return (w.length > 1 && w[w.length - 1].length <= 2 ? w[w.length - 1] : w[0].slice(0, 1)).toUpperCase(); };

async function viewLehrplan(arg) {
  setChrome('Lehrplan', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const vorKind = Number(arg) || null;
  let mitTest = false;
  let d = await lernMxLaden();
  // aus dem Plan des Testkinds: LM-S liefert es nur auf ausdrücklichen Wunsch
  if (vorKind && d.matrix && !(d.kinder || []).some((k) => k.id === vorKind)) { mitTest = true; d = await lernMxLaden(true); }
  if (!live()) return;
  let M = lernMxDaten(d);
  const kinder = d.kinder || [];
  const zst = lernMx || (lernMx = { sa: kinder[0]?.schulart || 'gym_by', kind: null, sel: null, q: '', inhalt: '' });
  let kurz = lernMxSpeicher('mx-kurz') === '1', zeilen = lernMxSpeicher('mx-zeilen') !== '0';
  if (vorKind) { zst.kind = vorKind; zst.sel = null; const c = kinder.find((k) => k.id === vorKind); if (c?.schulart && LERN_MX_SA[c.schulart]) zst.sa = c.schulart; }
  if (zst.kind && zst.kind !== 'alle' && !kinder.some((k) => k.id === zst.kind) && !vorKind) zst.kind = null;
  if (!LERN_MX_SA[zst.sa]) zst.sa = 'gym_by';
  const gewaehlt = () => (zst.kind === 'alle' ? kinder : zst.kind ? kinder.filter((k) => k.id === zst.kind) : []);
  const einKind = () => (zst.kind && zst.kind !== 'alle' ? kinder.find((k) => k.id === zst.kind) || null : null);
  const handy = () => innerWidth < 760;

  // LW-1: Stufen-Knöpfe gibt es nur noch im Reiter „Lehrplan“ der Kind-Seite („Für ‹Kind› planen ›“). Nach dem Neuladen bleiben die Stufen aktuell.
  const neuLaden = async () => { try { const n = await lernMxLaden(mitTest); if (!live()) return; d = n; M = lernMxDaten(d); zeichne(); } catch { /* bleibt */ } };
  // ---------- Kopf: Einordnen nach · Suche · Aufbau · Kurzbeschreibung · Lernstand ----------
  const schalter = (name, wahl, ist, setze) => el('div', { class: 'mx-schalter', role: 'group', 'aria-label': name }, ...wahl.map(([w, text]) =>
    el('button', { type: 'button', 'aria-pressed': String(ist() === w), onclick: () => { setze(w); zeichne(); } }, text)));
  const suche = el('input', { type: 'search', class: 'mx-suche', placeholder: 'Suchen, z. B. Brüche', 'aria-label': 'Thema suchen', value: zst.q });
  suche.addEventListener('input', () => { zst.q = suche.value; zeichne(); });
  const kurzBox = el('input', { type: 'checkbox', checked: kurz ? true : null, onchange: (ev) => { kurz = ev.target.checked; lernMxSpeicher('mx-kurz', kurz ? '1' : '0'); zeichne(); } });
  const leiste = el('div', { class: 'mx-leiste' });
  const lernstandLeiste = el('div', { class: 'mx-leiste mx-lernstand-leiste' });
  const inhaltLeiste = el('div', { class: 'mx-leiste mx-inhalt-leiste' });
  const ansicht = el('div', { class: 'mx-ansicht' });
  const detail = el('aside', { class: 'mx-detail', 'aria-live': 'polite', 'aria-label': 'Thema im Detail' });
  const waehleKind = (w) => {
    zst.kind = w;
    const c = einKind(); if (c?.schulart && LERN_MX_SA[c.schulart]) zst.sa = c.schulart;
    zeichne();
    if (c) requestAnimationFrame(() => ansicht.querySelector('.mx-chip.mx-dran')?.scrollIntoView({ block: 'center' })); // LM-4: beim Einschalten zum ▶-Thema
  };
  const zeichneLeisten = () => {
    lernErsetze(leiste, el('span', { class: 'mx-leiste-wort' }, 'Einordnen nach'),
      schalter('Einordnen nach Schulart', Object.entries(LERN_MX_SA).map(([s, [n]]) => [s, n]), () => zst.sa, (w) => { zst.sa = w; }),
      suche, handy() ? null : schalter('Aufbau', [['z', 'Klassen als Zeilen'], ['s', 'Klassen als Spalten']], () => (zeilen ? 'z' : 's'), (w) => { zeilen = w === 'z'; lernMxSpeicher('mx-zeilen', zeilen ? '1' : '0'); }),
      el('label', { class: 'mx-kurz' }, kurzBox, ' Kurzbeschreibung'));
    // „Was fehlt noch?“ (aus LB-1): Filter nach Inhaltsstand mit Zählern; nicht passende Themen werden blass
    const zahl = (k) => M.themen.filter((x) => inhaltK(x) === k).length;
    lernErsetze(inhaltLeiste, el('span', { class: 'mx-leiste-wort' }, 'Inhalt'),
      el('div', { class: 'mx-schalter', role: 'group', 'aria-label': 'Inhalt' }, ...[['', 'Alle', null], ['fertig', 'fertig', '●'], ['pruefung', 'in Prüfung', '◐'], ['leer', 'fehlt', '○']].map(([w, text, z]) =>
        el('button', { type: 'button', 'aria-pressed': String(zst.inhalt === w), 'aria-label': w ? `${text}: ${zahl(w)}` : 'Alle Themen', onclick: () => { zst.inhalt = w; zeichne(); } },
          z ? el('i', { class: 'lp-dot lp-dot-' + w, 'aria-hidden': 'true' }) : null, z ? `${text} ${zahl(w)}` : text))));
    lernErsetze(lernstandLeiste, el('span', { class: 'mx-leiste-wort' }, 'Lernstand'),
      kinder.length ? el('div', { class: 'mx-schalter', role: 'group', 'aria-label': 'Lernstand' },
        el('button', { type: 'button', 'aria-pressed': String(!zst.kind), onclick: () => waehleKind(null) }, 'Aus'),
        ...kinder.map((c) => el('button', { type: 'button', 'aria-pressed': String(zst.kind === c.id), onclick: () => waehleKind(c.id) }, c.name)),
        kinder.length > 1 ? el('button', { type: 'button', 'aria-pressed': String(zst.kind === 'alle'), onclick: () => waehleKind('alle') }, kinder.length === 2 ? 'Beide vergleichen' : 'Alle vergleichen') : null)
        : el('span', { class: 'small muted' }, 'Keine Kinder angelegt.'),
      zst.kind && zst.kind !== 'alle' && !einKind() ? el('span', { class: 'small muted' }, 'Für dieses Kind liefert die Übersicht keinen Lernstand.') : null);
  };

  // ---------- Matrix ----------
  const inhaltK = (x) => (x.ohneFlug && !x.roh.einheit ? 'ohne' : lernInhaltZustand(x.roh).k);
  const treffer = (x) => { if (zst.inhalt && inhaltK(x) !== zst.inhalt) return false; const q = zst.q.trim().toLowerCase(); return !q || `${x.titel} ${x.umfang} ${x.gebiet} ${x.merke.join(' ')} ${x.etappen.map((e) => e.titel).join(' ')}`.toLowerCase().includes(q); };
  const weg = (id) => { const s = new Set(); const st = [id]; while (st.length) { const v = st.pop(); (M.vor.get(v) || []).forEach((e) => { if (!s.has(e.id)) { s.add(e.id); st.push(e.id); } }); } return s; };
  let WEG = new Set();
  const rolle = (x) => { const sel = zst.sel; if (!sel || !M.by.has(sel)) return ''; if (x.id === sel) return ' mx-sel'; if ((M.vor.get(sel) || []).some((e) => e.id === x.id)) return ' mx-vor';
    if ((M.nach.get(sel) || []).some((e) => e.id === x.id)) return ' mx-nach'; return WEG.has(x.id) ? ' mx-weg2' : ''; };
  const reihe = (x) => Number(x.r[zst.sa]) || Number(x.r.gym_by) || 999;
  const imFeld = (k, g) => M.themen.filter((x) => lernMxZeile(x, zst.sa) === k && x.gebiet === g).sort((a, b) => (lernMxKl(a, zst.sa) ? 0 : 1) - (lernMxKl(b, zst.sa) ? 0 : 1) || reihe(a) - reihe(b) || a.titel.localeCompare(b.titel));
  const farbe = (k) => LERN_KL_FARBE[k] || '#888';
  const schulen = (x) => el('span', { class: 'mx-sch' }, ...['gym_by', 'rs_by'].map((s) => { const v = x.jg[s];
    return el('b', { class: (s === zst.sa ? 'mx-ref' : '') + (v ? '' : ' mx-fehlt') }, `${LERN_MX_SA[s][1]} ${v || '–'}`); }),
    x.jg.ib_myp ? el('b', { class: zst.sa === 'ib_myp' ? 'mx-ref' : '' }, `IB ${x.jg.ib_myp}`) : zst.sa === 'ib_myp' ? el('b', { class: 'mx-ref mx-fehlt' }, 'IB –') : null);
  const chip = (x) => {
    const z = lernMxZusatz(x, zst.sa); const n = (M.nach.get(x.id) || []).length; const ks = gewaehlt();
    const s1 = ks.length === 1 ? lernMxStufe(x, ks[0]) : null;
    const auf = zst.sel === x.id;
    return el('button', { type: 'button', class: 'mx-chip' + (z ? ' mx-zu' : '') + (x.ohneFlug ? ' mx-ohne' : '') + (treffer(x) ? '' : ' mx-weg') + rolle(x) + (s1 ? ' mx-st ' + (LERN_STUFE[s1.stufe]?.kl || 'st-4') : '') + (s1?.stufe === 'dran' ? ' mx-dran' : '') + (ks.length > 1 ? ' mx-vergleich' : ''),
      style: `--f:${farbe(lernMxZeile(x, zst.sa))}`, 'data-id': String(x.id), 'aria-expanded': String(auf),
      onclick: () => { zst.sel = auf ? null : x.id; zeichne(); if (zst.sel && innerWidth < 1100 && !handy()) detail.scrollIntoView({ block: 'start' }); } },
      n >= 2 ? el('span', { class: 'mx-n', title: `Grundlage für ${n} Themen` }, `→ ${n}`) : null,
      z ? el('span', { class: 'mx-n mx-m' + (z.marke === '?' ? ' mx-q' : ''), title: z.text }, z.marke) : null,
      el('span', { class: 'mx-titel' }, x.titel),
      kurz && x.umfang ? el('span', { class: 'mx-u' }, x.umfang) : null,
      schulen(x),
      s1 ? el('span', { class: 'mx-stand' }, lernMxStandText(s1), s1.stufe === 'dran' ? ` · hier ist ${ks[0].name}` : '') : null,
      ks.length > 1 ? el('span', { class: 'mx-dots' }, el('span', { class: 'mx-dl' }, ks.map(lernMxMarke).join('/')),
        ...ks.map((c) => { const s = lernMxStufe(x, c); return el('span', { class: 'mx-dot ' + (LERN_STUFE[s.stufe]?.kl || 'st-4'), title: `${c.name}: ${lernMxStandText(s)}`, role: 'img', 'aria-label': `${c.name}: ${lernMxStandText(s)}` }); })) : null);
  };
  // Pflicht: Klasse in der Schulart; mit LM-S zusätzlich einer Lehrplan-Quelle dieser Schulart zugeordnet (pflicht [schularten])
  const pflicht = (k) => M.themen.filter((x) => lernMxKl(x, zst.sa) === k && (!x.pflicht || x.pflicht.includes(zst.sa)));
  const kopfTeile = (k) => { const n = M.themen.filter((x) => lernMxZeile(x, zst.sa) === k).length; const p = pflicht(k).length;
    return [`${n} Themen`, `${p} ${zst.sa === 'ib_myp' ? 'im MYP' : LERN_MX_SA[zst.sa][1] + '\u2011Pflicht'}`]; };
  const kopfText = (k) => kopfTeile(k).join(' · ');
  const balken = (k) => { const ks = gewaehlt(); if (!ks.length) return null; const l = pflicht(k);
    return el('div', { class: 'mx-balken-gruppe' }, ...ks.map((c) => { const z = { komplett: 0, wiederholung: 0, dran: 0 }; l.forEach((x) => { const s = lernMxStufe(x, c).stufe; if (s in z) z[s]++; });
      const pz = (v) => (l.length ? (v / l.length) * 100 : 0);
      const ring = lernLwRing(M.themen, (x) => lernMxStufe(x, c), zst.sa, k, lernKindGruppe(zst.sa, c.schulart === zst.sa ? c : null));
      return el('div', { class: 'mx-balken', 'data-ring': ring.pz === null ? '' : String(ring.pz), title: `${c.name}: ${z.komplett} kann er · ${z.wiederholung} Wdh · ${z.dran} dran von ${l.length} · ${ring.text}`, role: 'img', 'aria-label': `${c.name}: ${z.komplett} kann er komplett, ${z.wiederholung} in Wiederholung, ${z.dran} gerade dran von ${l.length}` },
        ks.length > 1 ? el('em', {}, lernMxMarke(c)) : null,
        el('span', {}, el('i', { class: 'st-1', style: `width:${pz(z.komplett)}%` }), el('i', { class: 'st-2', style: `width:${pz(z.wiederholung)}%` }), el('i', { class: 'st-3', style: `width:${pz(z.dran)}%` }))); })); };
  const klKopf = (k, lang) => el('div', { class: 'mx-kl' + (k === 9 ? ' mx-hell' : ''), style: `background:${farbe(k)}` },
    el('b', {}, `${lang ? 'Klasse' : 'Kl.'} ${k}`), zst.sa === 'ib_myp' && k > 5 ? el('small', {}, `MYP-Jahr ${k - 5}`) : null, ...kopfTeile(k).map((x) => el('small', { class: 'mx-kl-zahl' }, x)), balken(k));
  const gebiete = () => { const reihe = M.gebiete || LERN_MX_GEB; return [...reihe, ...new Set(M.themen.map((x) => x.gebiet).filter((g) => !reihe.includes(g)))].filter((g) => M.themen.some((x) => x.gebiet === g)); };
  let svg = null;
  const zeichneMatrix = () => {
    WEG = zst.sel ? weg(zst.sel) : new Set();
    const gebs = gebiete(); svg = null;
    if (handy()) {
      lernErsetze(ansicht, el('div', { class: 'mx-liste' + (zst.sel ? ' mx-zeigt' : '') }, ...LERN_MX_KL.map((k) => el('section', { class: 'mx-liste-klasse' },
        el('h3', { class: 'mx-liste-kopf' + (k === 9 ? ' mx-hell' : ''), style: `background:${farbe(k)}` }, el('b', {}, `Klasse ${k}`), zst.sa === 'ib_myp' && k > 5 ? el('small', {}, ` · MYP-Jahr ${k - 5}`) : null, el('small', {}, ' · ' + kopfText(k)), balken(k)),
        ...gebs.map((g) => { const l = imFeld(k, g); return l.length ? el('div', { class: 'mx-gruppe' }, el('b', { class: 'mx-gruppe-name' }, g), ...l.map(chip)) : null; })))));
      const c = zst.sel && ansicht.querySelector(`.mx-chip[data-id="${zst.sel}"]`); if (c) c.after(detail);
      return;
    }
    const zellen = [];
    if (zeilen) {
      zellen.push(el('div', { class: 'mx-ecke' }), ...gebs.map((g) => el('div', { class: 'mx-geb' }, g)));
      for (const k of LERN_MX_KL) zellen.push(klKopf(k, false), ...gebs.map((g) => el('div', { class: 'mx-zelle' }, ...imFeld(k, g).map(chip))));
    } else {
      zellen.push(el('div', { class: 'mx-ecke' }), ...LERN_MX_KL.map((k) => klKopf(k, true)));
      for (const g of gebs) zellen.push(el('div', { class: 'mx-geb' }, g), ...LERN_MX_KL.map((k) => el('div', { class: 'mx-zelle' }, ...imFeld(k, g).map(chip))));
    }
    svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); svg.setAttribute('class', 'mx-linien'); svg.setAttribute('aria-hidden', 'true');
    lernErsetze(ansicht, el('div', { class: 'mx-wrap' }, el('div', { class: 'mx-matrix ' + (zeilen ? 'mx-z' : 'mx-s') + (zst.sel ? ' mx-zeigt' : ''), style: `--n:${zeilen ? gebs.length : LERN_MX_KL.length}` }, ...zellen), svg));
    requestAnimationFrame(linien);
  };
  // LM-3: Linien hinter den Karten (SVG unter den Karten), direkte Voraussetzungen gelb, darauf aufbauend blau, „empfohlen“ gestrichelt
  function linien() {
    if (!svg || !svg.isConnected) return; svg.replaceChildren(); if (!zst.sel) return;
    const w = svg.parentNode.getBoundingClientRect();
    const r = (id) => { const c = svg.parentNode.querySelector(`.mx-chip[data-id="${id}"]`); if (!c) return null; const b = c.getBoundingClientRect(); return { x: b.left - w.left + b.width / 2, y: b.top - w.top + b.height / 2 }; };
    const s = r(zst.sel); if (!s) return;
    svg.setAttribute('viewBox', `0 0 ${w.width} ${w.height}`); svg.setAttribute('width', w.width); svg.setAttribute('height', w.height);
    const linie = (a, b, kl, art) => { const my = (a.y + b.y) / 2; const p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      p.setAttribute('d', `M${a.x},${a.y} C${a.x},${my} ${b.x},${my} ${b.x},${b.y}`); p.setAttribute('class', `mx-linie ${kl}${art === 'empfohlen' ? ' mx-empfohlen' : ''}`); svg.append(p); };
    (M.vor.get(zst.sel) || []).forEach((e) => { const a = r(e.id); if (a) linie(a, s, 'mx-l-vor', e.art); });
    (M.nach.get(zst.sel) || []).forEach((e) => { const b = r(e.id); if (b) linie(s, b, 'mx-l-nach', e.art); });
  }

  // ---------- LM-2 Detail ----------
  const reiheAlle = () => M.themen.slice().sort((a, b) => lernMxZeile(a, zst.sa) - lernMxZeile(b, zst.sa) || (lernMxKl(a, zst.sa) ? 0 : 1) - (lernMxKl(b, zst.sa) ? 0 : 1) || reihe(a) - reihe(b) || a.titel.localeCompare(b.titel));
  const kurzK = (id) => { const y = M.by.get(id); const k = lernMxKl(y, zst.sa); return k ? `Kl. ${k}` : `zusätzlich, ≈ Kl. ${lernMxZeile(y, zst.sa)}`; };
  const springe = (id) => { zst.sel = id; zeichne(); if (!handy() && innerWidth < 1100) detail.scrollIntoView({ block: 'start' }); };
  const link = (id) => el('button', { type: 'button', class: 'mx-link', onclick: () => springe(id) }, M.by.get(id).titel);
  const verbListe = (l, sel, rueck) => el('ul', { class: 'mx-dep' }, ...l.map((e) => { const bg = e.bg || begr.get(rueck ? `${e.id}-${sel}` : `${sel}-${e.id}`) || '';
    return el('li', {}, link(e.id), el('span', { class: 'mx-kk' }, ` · ${kurzK(e.id)}${e.art === 'empfohlen' ? ' · empfohlen' : ''}`), bg ? el('br') : null, bg ? el('span', { class: 'mx-kk' }, bg) : null); }));
  const nachKl = (a, b) => (lernMxZeile(M.by.get(a.id ?? a), zst.sa) - lernMxZeile(M.by.get(b.id ?? b), zst.sa));
  const inhaltZeichen = { fertig: ['●', 'fertig'], pruefung: ['◐', 'in Prüfung'], leer: ['○', 'fehlt'] };
  // LM-S 2: das Detail (kurz, ort, was_gefordert, merke, etappen, beispiel, braucht/baut_darauf mit Begründung, lehrplan, eigenstaendig als Text)
  // kommt beim Antippen über schule_lehrplan_thema { thema_id } – einmal je Thema; bis dahin zeigt das Detail, was das Raster hat.
  const geholt = new Map(); // thema_id → 'laedt' | 'ok' | 'fehler'
  const begr = new Map(); // „a-b“ → Begründung der Verbindung (aus dem Detail)
  const nachladen = (x) => {
    if (!d.matrix || geholt.has(x.id)) return geholt.get(x.id) === 'laedt' ? el('p', { class: 'small muted mx-laedt' }, 'Einzelheiten werden geladen …') : null;
    geholt.set(x.id, 'laedt');
    lernCall('schule_lehrplan_thema', { thema_id: x.id }).then((t) => {
      if (!t || !live()) return;
      const i = d.themen.findIndex((y) => y.thema_id === x.id); if (i < 0) return;
      const neu = Object.fromEntries(['kurz', 'ort', 'merke', 'etappen', 'beispiel', 'lehrplan', 'eigenstaendig', 'lernbereich'].filter((k) => t[k] !== undefined).map((k) => [k, t[k]]));
      if (t.was_gefordert) neu.beschreibung = t.was_gefordert;
      for (const v of t.braucht || []) if (v.begruendung) begr.set(`${x.id}-${v.thema_id}`, v.begruendung);
      for (const v of t.baut_darauf || []) if (v.begruendung) begr.set(`${v.thema_id}-${x.id}`, v.begruendung);
      d.themen[i] = { ...d.themen[i], ...neu }; geholt.set(x.id, 'ok');
    }).catch(() => { geholt.set(x.id, 'fehler'); }).finally(() => { if (!live()) return; M = lernMxDaten(d); if (zst.sel === x.id) zeichneDetail(); });
    return el('p', { class: 'small muted mx-laedt' }, 'Einzelheiten werden geladen …');
  };
  function zeichneDetail() {
    const x = zst.sel && M.by.get(zst.sel);
    if (!x) { lernErsetze(detail, el('p', { class: 'muted mx-leer' }, 'Ein Thema antippen: Hier steht, was gefordert ist, was es vorher braucht und worauf es vorbereitet. In der Übersicht werden die Verbindungen eingezeichnet.'));
      if (handy()) detail.remove(); return; }
    const sa = zst.sa; const k = lernMxKl(x, sa); const z = lernMxZusatz(x, sa); const t = x.roh;
    const iz = lernInhaltZustand(t); const zw = inhaltZeichen[iz.k][1];
    const vor = (M.vor.get(x.id) || []).slice().sort(nachKl); const nach = (M.nach.get(x.id) || []).slice().sort(nachKl);
    const wg = [...WEG].filter((i) => !vor.some((v) => v.id === i)).sort((a, b) => nachKl(a, b));
    const liste = reiheAlle(); const i = liste.findIndex((y) => y.id === x.id);
    const ks = gewaehlt(); const lpText = x.lp(sa);
    lernErsetze(detail,
      el('h2', {}, x.titel),
      el('div', { class: 'mx-tags' }, el('span', { class: 'mx-tag' }, x.gebiet),
        k ? el('span', { class: 'mx-tag mx-tag-k' + (lernMxZeile(x, sa) === 9 ? ' mx-hell' : ''), style: `background:${farbe(k)}` }, `${LERN_MX_SA[sa][0]} ${sa === 'ib_myp' ? `MYP-Jahr ${x.jg.ib_myp}` : 'Kl. ' + k}`)
          : el('span', { class: 'mx-tag' }, `${LERN_MX_SA[sa][0]}: zusätzlich, ≈ Kl. ${z.k}`),
        ...Object.keys(LERN_MX_SA).filter((s) => s !== sa && x.jg[s]).map((s) => el('span', { class: 'mx-tag' }, s === 'ib_myp' ? `IB MYP-Jahr ${x.jg[s]}` : `${LERN_MX_SA[s][0]} Kl. ${x.jg[s]}`))),
      x.lb[sa] ? el('p', { class: 'small mx-lb' }, el('b', {}, 'Lernbereich: '), lernLbText(x.lb[sa])) : null,
      // aus der bisherigen Lehrplan-Übersicht: Inhalt (● fertig, ◐ in Prüfung, ○ fehlt), „Inhalte ansehen“, Aufträge und „Bitte Inhalte bauen“
      el('p', { class: 'small mx-inhalt' }, el('i', { class: 'lp-dot lp-dot-' + iz.k, 'aria-hidden': 'true' }), ` Inhalt: ${zw}`,
        t.einheit ? [' · ', el('a', { href: `#/inhalte/${t.einheit.id}` }, `Inhalte ansehen (${x.etappen.length || t.einheit.karten || 0} Etappen) ›`)] : null,
        t.rueckmeldungen ? [' · ', el('a', { href: '#/lernauftraege' }, `${t.rueckmeldungen} ${t.rueckmeldungen > 1 ? 'Aufträge' : 'Auftrag'}`)] : null,
        t.ort ? el('span', { class: 'muted' }, ` · Ort: ${t.ort}`) : null),
      t.einheit ? null : lernAendern({ block_id: t.block_id }, { bezug: 'flug', wo: `Flug „${x.titel}“`, art: 'neu', text: `Bitte Inhalte bauen: „${x.titel}“ (${t.ort || x.gebiet}, ${lernJahrgangText(x.jg)}).` }),
      // LM-4: Lernstand je Kind
      ks.length ? el('section', { class: 'mx-ls' }, el('h3', {}, 'Lernstand'), el('ul', { class: 'mx-ls-liste' }, ...ks.map((c) => { const s = lernMxStufe(x, c);
        // LM-S: fehler_offen (eine Pflicht-Etappe steht nach einem Test auf „fehler“; fehlt = nein); ohne LM-S: eine Etappe ist wieder offen
        const fehler = d.matrix ? s.fehler_offen === true || Number(s.fehler_offen) > 0 : Number(s.wieder_offen) > 0;
        return el('li', {}, el('div', { class: 'mx-ls-kopf' }, lernStufeZeichenEl(s), el('b', {}, c.name), lernStufeWortEl(s)),
          el('div', { class: 'mx-ls-links' }, el('a', { href: '#/kind/' + c.id + '-lehrplan', onclick: () => { lernPlanZiel = { kind: c.id, thema: x.id }; } }, `Für ${c.name} planen ›`),
            fehler ? el('a', { href: `#/kind/${c.id}-wackelt` }, 'Fehler besprechen ›') : null)); })),
        el('p', { class: 'small muted' }, 'Planen und Stufe setzen: im Reiter „Lehrplan“ des Kindes.')) : null,
      z ? el('p', { class: 'mx-offen' }, z.text) : null,
      x.ohneFlug ? el('p', { class: 'mx-offen' }, 'Zu diesem Thema gibt es keinen freigegebenen Flug (der Stoff steckt in einem anderen Flug oder ist ein stillgelegter Entwurf).') : null,
      nachladen(x),
      el('h3', {}, 'Was gefordert ist'), x.umfang ? el('p', {}, x.umfang) : el('p', { class: 'muted' }, 'Keine Beschreibung hinterlegt.'),
      el('h3', {}, 'Braucht vorher'),
      !M.hatVerb ? el('p', { class: 'mx-offen' }, 'Die Verbindungen zwischen den Themen liefert der Server noch nicht. Sobald sie da sind, stehen hier die Voraussetzungen.')
        : vor.length ? verbListe(vor, x.id, false) : el('p', { class: 'mx-offen' }, x.eigen ? `Eigenständig: braucht keine Voraussetzung${typeof x.eigen === 'string' ? ' – ' + x.eigen : ' (so hinterlegt)'}.` : 'Keine Voraussetzung hinterlegt. Das heißt nicht sicher, dass das Thema eigenständig ist – die Verbindungen werden noch vervollständigt.'),
      wg.length ? [el('h3', {}, `Weiter zurück auf dem Weg (${wg.length})`), el('p', { class: 'mx-dep mx-weg-liste' }, ...wg.flatMap((id, j) => [j ? ' · ' : '', link(id), el('span', { class: 'mx-kk' }, ` (${kurzK(id)})`)]))] : null,
      M.hatVerb ? [el('h3', {}, 'Darauf baut auf'), nach.length ? verbListe(nach, x.id, true) : el('p', { class: 'mx-offen' }, 'Kein späteres Thema hinterlegt, das darauf aufbaut.')] : null,
      x.merke.length ? [el('h3', {}, 'Das muss sitzen'), el('ul', {}, ...x.merke.map((m) => el('li', {}, m)))] : null,
      x.beispiel ? [el('h3', {}, 'Beispielaufgabe'), el('p', { class: 'mx-beisp' }, x.beispiel)] : null,
      x.etappen.length ? [el('h3', {}, `Schritte in der App (${x.etappen.length} Etappen)`), el('ol', {}, ...x.etappen.map((e) => el('li', {}, e.titel, e.pflicht === false ? el('span', { class: 'mx-kk' }, ' · freiwillig') : null)))] : null,
      lpText.length || x.lb[sa] ? [el('h3', {}, 'Im Lehrplan'), lpText.length ? el('ul', { class: 'mx-lp' }, ...lpText.map((m) => el('li', {}, m))) : el('p', { class: 'mx-lp' }, lernLbText(x.lb[sa]))] : null,
      i >= 0 ? el('div', { class: 'mx-nav' },
        el('button', { type: 'button', disabled: i > 0 ? null : true, 'aria-label': i > 0 ? `Voriges Thema: ${liste[i - 1].titel}` : 'Kein voriges Thema', onclick: () => springe(liste[i - 1].id) }, '‹ ', i > 0 ? liste[i - 1].titel : ''),
        el('button', { type: 'button', disabled: liste[i + 1] ? null : true, 'aria-label': liste[i + 1] ? `Nächstes Thema: ${liste[i + 1].titel}` : 'Kein nächstes Thema', onclick: () => springe(liste[i + 1].id) }, liste[i + 1] ? liste[i + 1].titel : '', ' ›')) : null);
  }
  // N1 (Nachprüfung 22.11.): am Rechner die Detail-Spalte erst beim Antippen – sonst hat die Matrix die volle Breite
  function zeichne() { if (!live()) return; haupt.classList.toggle('mx-mit-detail', !!zst.sel); zeichneLeisten(); zeichneMatrix(); zeichneDetail(); if (!handy() && !detail.isConnected) haupt.append(detail); }

  const haupt = el('div', { class: 'mx-haupt' }, ansicht, detail);
  // nur bei Wechsel Handy ↔ breit neu zeichnen, sonst die Linien neu legen
  let warHandy = handy();
  const groesse = () => { if (!live()) { removeEventListener('resize', groesse); return; } if (handy() !== warHandy) { warHandy = handy(); zeichne(); } else linien(); };
  addEventListener('resize', groesse);
  lernErsetze(main, lernInfoLink(),
    el('section', { class: 'mx-kopf' }, el('h2', {}, 'Mathe Klasse 5–10: was gelernt wird'),
      el('p', { class: 'small muted' }, 'Ein Thema antippen zeigt, was gefordert ist, was es vorher braucht und worauf es vorbereitet. Grundlage sind die Themen der Lern-App mit ihrem Bezug zum LehrplanPLUS Bayern. ',
        el('a', { href: '#/expeditionen' }, '⛰ Expeditionen ansehen ›'))),
    leiste, inhaltLeiste, lernstandLeiste,
    el('div', { class: 'mx-legende small muted' }, el('span', {}, el('i', { class: 'mx-leg-vor' }), 'braucht vorher'), el('span', {}, el('i', { class: 'mx-leg-weg' }), 'weiter zurück'),
      el('span', {}, el('i', { class: 'mx-leg-nach' }), 'baut darauf auf'), el('span', {}, el('i', { class: 'mx-leg-zu' }), 'nicht im Lehrplan dieser Schulart (gestrichelt)'), el('span', {}, '→ n: Grundlage für n Themen')),
    haupt,
    el('p', { class: 'small muted mx-hinweis' }, 'Alle Themen der App stehen in der Matrix. Die Zeile richtet sich nach der Klasse der gewählten Schulart („Einordnen nach“). Hat diese Schulart das Thema nicht, steht es gestrichelt in der Klasse der anderen Schulart, sonst nach dem MYP-Jahr + 5. ',
      `IB: ${LERN_IB_HINWEIS}. Realschule: Die Wahlpflichtfächergruppen sind nicht getrennt.`));
  zeichne();
  if (einKind()) { requestAnimationFrame(() => ansicht.querySelector('.mx-chip.mx-dran')?.scrollIntoView({ block: 'center' })); }
}

// ---------- LW-1 (22.11.): Reiter „Lehrplan“ der Kind-Seite – Matrix + Fahrplan + Detail als Schublade ----------
// Vorgabe inhalte/pruefung/lehrer/werkstatt/umsetzung.md (ersetzt die Reiter „Stand“ und „Plan“). Daten: schule_lehrplan_matrix (Raster, Lernstand),
// schule_plan_lesen/schule_plan_setzen (Fahrplan mit Revision und Rückgängig wie bisher), schule_lernstand (Etappen im Detail).
const LERN_LW_SA = { gym_by: 'Gym', rs_by: 'RS', ib_myp: 'IB' };
const LERN_LW_SA_HILFE = 'Nach welchem Lehrplan die Themen den Klassen zugeordnet werden – z. B. steht „Satz des Pythagoras“ im Gymnasium in Kl. 8, in der Realschule in Kl. 9. Gezeigt werden immer alle Themen.'; // K1
const lernLwEtappen = (x, s) => Number(x.roh.etappen_anzahl) || Number(s?.etappen) || x.etappen.length || 1;
// Ring je Schule und Klasse: gelandete Etappen / alle Etappen der Pflichtthemen dieser Schule in dieser Klasse (IB: MYP-Jahr = Klasse − 5),
// unabhängig von der Zeile. Gelandet = Etappe gelandet (auch in Wiederholung); gesetzte Themen zählen mit allen Etappen; aufgelöste Themen zählen nicht.
// KJ (Muss aus ChatGPT 968): dieselbe Themen-Auswahl wie schuljahr_stand – Zusatz-Teile der Gruppe des Kindes zählen nicht
// (Gruppe: gym_by | rs_I | rs_II_III | myp_standard | myp_extended; ohne Zweig: rs_I bzw. myp_standard wie schule.kind_zweig).
const lernKindGruppe = (sa, kind = null) => (sa === 'gym_by' ? 'gym_by' : sa === 'rs_by' ? (kind?.schulart === 'rs_by' && kind?.zweig) || 'rs_I' : (kind?.schulart === 'ib_myp' && kind?.zweig) || 'myp_standard');
function lernMxZusatzGruppe(x, gruppe) {
  const z = x?.roh?.teil?.zusatz ?? x?.roh?.zusatz ?? x?.teil?.zusatz ?? x?.zusatz;
  if (Array.isArray(z)) return z.includes(gruppe);
  return !!(z && typeof z === 'object' && z[gruppe]);
}
// Ring aus schuljahr_stand (gleiche Zahlen wie „Mein Schuljahr“): null, wenn die Klasse dort fehlt
function lernLwRingAusStand(sj, sa, k) {
  if (!sj || (sj.schulart && sj.schulart !== sa)) return null; const x = (sj.klassen || []).find((y) => Number(y.klasse) === Number(k)); if (!x) return null;
  const rg = x.ring || {}; const r = { sa, k, themen: Number(x.fluege?.gesamt) || 0, fertig: Number(x.fluege?.fertig) || 0, alle: Number(x.etappen?.gesamt) || 0,
    kann: Number(rg.kann) || 0, wdh: Number(rg.wdh) || 0, an: Number(rg.an) || 0, ausStand: true };
  r.gelandet = Number(x.etappen?.gelandet) || r.kann + r.wdh + r.an; r.pz = x.prozent ?? (r.alle ? Math.round((100 * r.gelandet) / r.alle) : null);
  r.text = `${LERN_LW_SA[sa]} ${sa === 'ib_myp' ? k - 5 : k}: ${r.gelandet} von ${r.alle} Etappen gelandet · ${r.fertig}/${r.themen} Themen fertig`;
  return r;
}
function lernLwRing(themen, stufe, sa, k, gruppe = lernKindGruppe(sa)) {
  const ts = themen.filter((x) => !x.ohneFlug && lernMxKl(x, sa) === k && (sa === 'ib_myp' || !x.pflicht || x.pflicht.includes(sa)) && !lernMxZusatzGruppe(x, gruppe));
  const r = { sa, k, themen: ts.length, fertig: 0, alle: 0, kann: 0, wdh: 0, an: 0 };
  for (const x of ts) { const s = stufe(x); const n = lernLwEtappen(x, s); r.alle += n;
    if (s.stufe === 'komplett') { r.kann += n; r.fertig++; } else if (s.stufe === 'wiederholung') { r.wdh += n; r.fertig++; } else r.an += Math.min(n, Number(s.gelandet) || 0); }
  r.gelandet = r.kann + r.wdh + r.an; r.pz = r.alle ? Math.round((100 * r.gelandet) / r.alle) : null;
  r.text = `${LERN_LW_SA[sa]} ${sa === 'ib_myp' ? k - 5 : k}: ${r.gelandet} von ${r.alle} Etappen gelandet · ${r.fertig}/${r.themen} Themen fertig`;
  return r;
}
function lernLwRingSvg(r, gross) {
  const ns = 'http://www.w3.org/2000/svg'; const d = gross ? 46 : 20; const sw = gross ? 5 : 3.5; const rad = (d - sw) / 2; const u = 2 * Math.PI * rad;
  const s = document.createElementNS(ns, 'svg'); s.setAttribute('viewBox', `0 0 ${d} ${d}`); s.setAttribute('width', d); s.setAttribute('height', d); s.setAttribute('aria-hidden', 'true');
  const kreis = (farbe, laenge, ab) => { const c = document.createElementNS(ns, 'circle'); c.setAttribute('cx', d / 2); c.setAttribute('cy', d / 2); c.setAttribute('r', rad);
    c.setAttribute('fill', 'none'); c.setAttribute('stroke', farbe); c.setAttribute('stroke-width', sw);
    if (laenge !== null) { c.setAttribute('stroke-dasharray', `${laenge} ${u}`); c.setAttribute('stroke-dashoffset', String(-ab)); c.setAttribute('transform', `rotate(-90 ${d / 2} ${d / 2})`); }
    s.append(c); };
  kreis('#E6E1D4', null, 0);
  let ab = 0; for (const [teil, farbe] of [[r.kann, '#2E7D32'], [r.wdh, '#8BC34A'], [r.an, '#3F7FD0']]) { if (!teil || !r.alle) continue; const l = (u * teil) / r.alle; kreis(farbe, l, ab); ab += l; }
  return s;
}
const lernLwRingEl = (r, gross) => el('span', { class: 'lw-ring' + (gross ? ' lw-ring-gross' : ''), title: r.text, role: 'img', 'aria-label': r.text },
  lernLwRingSvg(r, gross), gross ? el('b', {}, r.pz === null ? '–' : `${r.pz} %`) : null,
  gross ? null : el('small', {}, `${LERN_LW_SA[r.sa]} ${r.sa === 'ib_myp' ? r.k - 5 : r.k} `, el('b', {}, r.pz === null ? '–' : `${r.pz} %`)));

async function viewKindLehrplan(id, rest = []) {
  setChrome('Lehrplan', { back: true, showTabs: false });
  const live = viewGuard();
  lernLaden();
  // LZ-App: Matrix gleichzeitig mit Plan, Lernstand und Übersicht
  let [p, ls, u, d] = await Promise.all([lernCall('schule_plan_lesen', { lernender_id: id }), lernCall('schule_lernstand', { lernender_id: id }).catch(() => null), lernCall('schule_uebersicht').catch(() => null),
    lernMxLaden().catch(() => ({ themen: [] }))]);
  let mitTest = false;
  if (d.matrix && !(d.kinder || []).some((c) => c.id === id)) { mitTest = true; d = await lernMxLaden(true).catch(() => d); }
  if (!live()) return;
  const kind = { ...((u?.lernende || []).find((c) => c.id === id) || {}), ...((d.kinder || []).find((c) => c.id === id) || {}), ...(p.kind || {}) };
  $('#title').textContent = 'Lehrplan ' + (kind.name || '');
  // LW-2 K2: Klasse und Schulart aus derselben Quelle wie der Kopf der Kind-Seite (schule_uebersicht); nur wenn dort nichts steht, aus Plan/Raster
  const kindU = (u?.lernende || []).find((c) => c.id === id) || {};
  const kindSa = LERN_MX_SA[kindU.schulart] ? kindU.schulart : LERN_MX_SA[kind.schulart] ? kind.schulart : 'gym_by';
  const kindKl = Number(kindU.klasse) || Number(kind.klasse) || null;

  // ---------- Daten zusammenführen ----------
  const details = new Map(); // thema_id → Felder aus schule_lehrplan_thema (bleiben beim Neuladen)
  let ortById, planT, M;
  const baue = () => {
    ortById = new Map((p.orte || []).map((o) => [o.block_id, o]));
    planT = new Map(); for (const o of p.orte || []) for (const t of o.themen || []) if (!planT.has(t.thema_id)) planT.set(t.thema_id, { t, o });
    // Flüge aus dem Plan, die das Raster nicht kennt (ohne LM-S): als Thema mit dem Kontinent als Themengebiet
    const da = new Set((d.themen || []).map((t) => t.thema_id)); d.themen = d.themen || [];
    for (const [tid, { t, o }] of planT) if (!da.has(tid)) d.themen.push({ thema_id: tid, titel: t.titel, gebiet: o.kontinent || 'Weitere', block_id: o.block_id, jahrgang: t.jahrgang || {},
      lehrplan_reihenfolge: t.lehrplan_reihenfolge || {}, lernbereich: t.lernbereich, beschreibung: t.beschreibung, einheit: t.einheit || null, etappen: t.etappen, stufe: {} });
    d.themen = d.themen.map((t) => (details.has(t.thema_id) ? { ...t, ...details.get(t.thema_id) } : t));
    M = lernMxDaten(d);
  };
  baue();
  const proEinheit = () => new Map((ls?.einheiten || []).map((e) => [e.einheit_id, e]));

  // ---------- Plan (Arbeitskopie, sofort speichern, Rückgängig – wie bisher im Reiter „Plan“) ----------
  let plan = lernPlanArbeitskopie(p); let revision = p.revision; const flags = lernPlanFlags(p);
  const { kannAbwaehlen, kannJeFlug, kannWdh } = flags;
  const vorher = []; let laeuft = null, nochmal = false, gesperrt = false, rueckgaengig = false, rueckSchritt = null;
  const blockVon = (x) => planT.get(x.id)?.o.block_id ?? x.roh.block_id;
  const alleThemen = (b) => { const o = ortById.get(b); return o ? (o.themen || []).map((t) => t.thema_id) : M.themen.filter((y) => y.roh.block_id === b).map((y) => y.id); };
  const themenImOrt = (b) => alleThemen(b).map((tid) => M.by.get(tid)).filter(Boolean);
  const setze = (b, tid, wahl) => lernPlanSetzeIn(plan, alleThemen(b), kannAbwaehlen, b, tid, wahl);
  const imPlan = (x) => { const px = plan.find((y) => y.block_id === blockVon(x)); return !!px && !px.ausgelassen.includes(x.id); };
  const stufeVon = (x) => {
    const b = blockVon(x); const px = plan.find((y) => y.block_id === b); const drin = !!px && !px.ausgelassen.includes(x.id); const pt = planT.get(x.id)?.t;
    // Raster (LM-S) und Plan liefern dieselbe Stufe; das Raster gilt (Zahlen wie unter Nachschlagen), Zusätze wie „Rückfall“ kommen aus dem Plan dazu
    const s = x.roh.stufe?.[id] || pt?.stufe ? { ...(pt?.stufe || {}), ...(x.roh.stufe?.[id] || {}) } : pt ? lernStufeSchaetzen(pt, drin, px?.status === 'fertig') : lernMxStufe(x, { id });
    if (drin && (px.kann_schon || px.kann.includes(x.id))) return { ...s, stufe: 'komplett', gesetzt: 'komplett' };
    if (drin && px.kw.includes(x.id)) return s.gesetzt === 'wiederholen' ? s : { ...s, stufe: 'wiederholung', gesetzt: 'wiederholen', wdh_nr: s.wdh_nr || 1 };
    if (!drin) return !s.gesetzt && ['komplett', 'wiederholung'].includes(s.stufe) ? s : { ...s, stufe: 'nicht_im_plan', gesetzt: null };
    if (s.gesetzt) return { ...s, stufe: s.begonnen > 0 && !s.geschaetzt ? 'dran' : 'kommt', gesetzt: null };
    if (s.stufe === 'nicht_im_plan') return { ...s, stufe: 'kommt' };
    return s;
  };
  const ortStufe = (px) => { const ts = themenImOrt(px.block_id).filter((x) => !px.ausgelassen.includes(x.id)); const st = ts.map((x) => stufeVon(x).stufe);
    return !ts.length ? 'kommt' : st.includes('dran') ? 'dran' : st.includes('kommt') ? 'kommt' : st.includes('wiederholung') ? 'wiederholung' : 'komplett'; };
  let sichtbar = []; // Indizes der ▶/○-Orte im Plan, in Reihenfolge des Fahrplans
  const ordne = () => { const mit = plan.map((x, i) => [x, i, ortStufe(x)]); sichtbar = [...mit.filter((m) => m[2] === 'dran'), ...mit.filter((m) => m[2] === 'kommt')].map((m) => m[1]); return mit; };
  // LW-2 S2: ein Platz je Ort (bis zum Reise-Aufbau); mehrere Themen eines Orts bekommen Unterbuchstaben „3a, 3b …“ in der Reihenfolge des Orts
  const fpThemen = (px) => themenImOrt(px.block_id).filter((y) => !px.ausgelassen.includes(y.id) && ['dran', 'kommt'].includes(stufeVon(y).stufe));
  const platzInfo = (x) => { if (!imPlan(x) || !['dran', 'kommt'].includes(stufeVon(x).stufe)) return null; const b = blockVon(x); const j = sichtbar.findIndex((i) => plan[i].block_id === b); if (j < 0) return null;
    const ts = fpThemen(plan[sichtbar[j]]); const k = Math.max(0, ts.findIndex((y) => y.id === x.id));
    return { nr: j + 1, pos: (j + 1) * 100 + k, text: ts.length > 1 ? `${j + 1}${'abcdefghijklmnopqrstuvwxyz'[k] || ''}` : String(j + 1) }; };
  const platz = (x) => platzInfo(x)?.text ?? null;

  const stand = el('span', { class: 'lern-plan-stand lw-stand lw-still', role: 'status', 'aria-live': 'polite' }, plan.length ? 'Gespeichert' : '');
  const rueckKnopf = el('button', { type: 'button', class: 'lern-plan-rueck lw-rueck', disabled: true, onclick: () => zuruecknehmen() }, '↶ Rückgängig');
  const meldung = el('div', { class: 'lern-plan-meldung lw-meldung', role: 'alert', hidden: true });
  const melde = (...kids) => { meldung.hidden = !kids.length; lernErsetze(meldung, ...kids); };
  const neuLaden = async () => {
    try { const [q, dn, l2] = await Promise.all([lernCall('schule_plan_lesen', { lernender_id: id }), lernMxLaden(mitTest).catch(() => null), lernCall('schule_lernstand', { lernender_id: id }).catch(() => null)]);
      if (!live() || gesperrt) return; p = { ...p, orte: q.orte || p.orte }; if (dn) d = dn; if (l2) ls = l2; baue(); zeichneAlles(); } catch { /* Stufen bleiben geschätzt */ }
  };
  const speichere = () => {
    if (gesperrt) return Promise.resolve();
    if (laeuft) { nochmal = true; return laeuft; }
    stand.textContent = 'Speichere …'; stand.classList.remove('lw-still');
    laeuft = (async () => {
      try {
        do {
          nochmal = false; const rs = rueckSchritt; rueckSchritt = null;
          const r = await lernCall('schule_plan_setzen', { lernender_id: id, revision, eintraege: lernPlanEintraege(plan, flags), ...(rs ? { rueckgaengig: rs } : {}) });
          revision = r?.revision ?? revision + 1; plan.forEach((x) => { x.ww = []; });
          if (!rs && r?.schritt_id) vorher.forEach((v) => { if (v.schritt === undefined) v.schritt = r.schritt_id; });
          if (rs) vorher.length = 0; // der Server nimmt Rückgängig nur für den jüngsten Schritt an
        } while (nochmal);
        stand.textContent = rueckgaengig ? 'Rückgängig gemacht · Gespeichert' : 'Gespeichert'; stand.classList.add('lw-still'); melde(); // S1: „Gespeichert“ still (nur für Vorleser)
        neuLaden();
      } catch (err) {
        stand.textContent = 'Nicht gespeichert'; stand.classList.remove('lw-still'); tosteWeg();
        if (/inzwischen wurde etwas anderes geändert/i.test(err.message)) { vorher.length = 0;
          melde(el('span', {}, 'Rückgängig geht nur für die letzte Änderung. Inzwischen wurde etwas anderes geändert.'), el('button', { type: 'button', class: 'primary', onclick: () => render() }, 'Neu laden'));
        } else if (/inzwischen geändert/i.test(err.message)) { gesperrt = true; koerper.inert = true; koerper.classList.add('lw-gesperrt');
          melde(el('span', {}, 'Der Plan wurde inzwischen von jemand anderem geändert. Deine letzte Änderung ist nicht gespeichert – es wird nichts überschrieben.'), el('button', { type: 'button', class: 'primary', onclick: () => render() }, 'Neu laden'));
        } else melde(el('span', {}, `Nicht gespeichert: ${err.message}`), el('button', { type: 'button', class: 'secondary', onclick: () => speichere() }, 'Erneut versuchen'));
      } finally { laeuft = null; rueckgaengig = false; rueckKnopf.disabled = gesperrt || !vorher.length; }
    })();
    return laeuft;
  };
  // LW-2 (4a): nach jeder Änderung prüfen, ob eine harte Voraussetzung neu verletzt ist → dunkelrote Einblendung mit Reparieren-Knopf (Warnung, keine Sperre)
  const kSchl = (k) => `${k.fall}:${k.x.id}:${k.v.id}`;
  const aendere = (fn, text = null, getan = null) => {
    if (gesperrt) return;
    const vorK = new Set(konflikte().map(kSchl));
    vorher.push({ plan: lernPlanKopie(plan), schritt: undefined }); if (vorher.length > 30) vorher.shift();
    fn(); ordne(); const neu = konflikte().filter((k) => !vorK.has(kSchl(k)));
    zeichneAlles(); speichere();
    const ids = new Set((Array.isArray(getan) ? getan : getan ? [getan] : []).map((y) => y.id));
    const w = ids.size ? neu.find((k) => ids.has(k.x.id)) || neu.find((k) => ids.has(k.v.id)) : neu[0];
    if (w) warne(w, text, ids); else if (text) toste(text);
  };
  function zuruecknehmen() { if (gesperrt || !vorher.length) return; const v = vorher.pop(); plan = v.plan; rueckgaengig = true; rueckSchritt = v.schritt || null; tosteWeg(); zeichneAlles(); speichere(); }
  // Meldung unten: „‹Thema› als Nächstes eingeplant · ↶ Rückgängig“ (5 s); Warnung bleibt stehen, bis sie geschlossen wird
  const toast = el('div', { class: 'lw-toast', role: 'status', hidden: true }); let toastUhr = null;
  const rueckIn = () => el('button', { type: 'button', class: 'lw-rueck-k', 'aria-label': '↶ Rückgängig', title: 'Rückgängig', onclick: () => zuruecknehmen() }, '↶ Rückgängig');
  function toste(text) { clearTimeout(toastUhr); toast.hidden = false; toast.classList.remove('lw-warn');
    lernErsetze(toast, el('span', {}, text), rueckIn());
    toastUhr = setTimeout(tosteWeg, 5000); }
  function tosteWeg() { clearTimeout(toastUhr); toast.hidden = true; toast.classList.remove('lw-warn'); }
  // LW-2b S1: kurze Namen – ohne Untertitel, bei Teilen „‹Titel› – Teil x von y“
  const kurzName = (x) => { const t = teilVon(x); return t ? `${t.grund} – Teil ${t.n} von ${t.von}` : x.titel; };
  function warne(w, text, ids) {
    clearTimeout(toastUhr); toast.hidden = false; toast.classList.add('lw-warn');
    const X = `„${kurzName(w.x)}“`, V = `„${kurzName(w.v)}“`; let msg, knopf = null;
    if (w.fall === 1 && ids.has(w.v.id) && !ids.has(w.x.id)) { msg = `⚠ ${X} baut hierauf auf und steht schon auf Platz ${platz(w.x)}`; if (blockVon(w.x) !== blockVon(w.v)) knopf = [`${X} dahinter setzen`, () => setzeHinter(w.x, w.v)]; }
    else if (w.fall === 1) { msg = `⚠ ${X} baut auf ${V} auf – das kommt erst auf Platz ${platz(w.v)}`; if (blockVon(w.x) !== blockVon(w.v)) knopf = [`${V} davor setzen`, () => setzeVor(w.v, w.x)]; }
    else if (ids.has(w.v.id)) msg = `⚠ ${X} im Plan baut darauf auf`;
    else { msg = `⚠ ${X} baut auf ${V} auf – das kann er noch nicht und es ist nicht im Plan`; knopf = [`${V} davor einplanen`, () => setzeVor(w.v, w.x)]; }
    const vorspann = !w.fall || (w.fall === 3 && ids.has(w.v.id)); // nur „… aus dem Plan genommen“ bleibt vorn stehen, sonst nennt die Warnung die Themen selbst
    lernErsetze(toast, el('span', {}, text && vorspann ? el('span', { class: 'lw-toast-was' }, text + ' · ') : null, msg),
      knopf ? el('button', { type: 'button', class: 'lw-reparier', onclick: knopf[1] }, knopf[0]) : null, rueckIn(),
      el('button', { type: 'button', class: 'lw-toast-x', 'aria-label': 'Hinweis schließen', onclick: () => tosteWeg() }, '✕'));
  }
  // Ort von v vor den Ort von x setzen (v ggf. erst einplanen) bzw. Ort von x hinter den Ort von v
  const verschiebe = (y, ziel, dahinter) => { const iy = plan.findIndex((q) => q.block_id === blockVon(y)); if (iy < 0) return; const [e] = plan.splice(iy, 1);
    const iz = plan.findIndex((q) => q.block_id === blockVon(ziel)); plan.splice(iz < 0 ? plan.length : iz + (dahinter ? 1 : 0), 0, e); };
  const setzeVor = (v, x) => aendere(() => { if (!imPlan(v)) setze(blockVon(v), v.id, 'lernen'); verschiebe(v, x, false); }, `„${kurzName(v)}“ vor „${kurzName(x)}“ gesetzt`, v);
  const setzeHinter = (x, v) => aendere(() => verschiebe(x, v, true), `„${kurzName(x)}“ hinter „${kurzName(v)}“ gesetzt`, x);

  // Einplanen: als Nächstes | ans Ende | nach Lehrplan einsortieren; im Plan verschieben; aus dem Plan
  const schluessel = (x, s2 = sa) => (lernMxZeile(x, s2) || 99) * 1000 + (Number(x.r[s2]) || Number(x.r.gym_by) || 999);
  const ortSchluessel = (px) => Math.min(...themenImOrt(px.block_id).filter((y) => !px.ausgelassen.includes(y.id)).map((y) => schluessel(y)), 99999);
  const einplanen = (x, wo) => {
    const b = blockVon(x); const vorName = { naechstes: 'als Nächstes eingeplant', ende: 'ans Ende des Fahrplans gesetzt', lehrplan: 'nach Lehrplan einsortiert' }[wo];
    aendere(() => {
      if (!imPlan(x)) setze(b, x.id, 'lernen');
      const i = plan.findIndex((y) => y.block_id === b); if (i < 0) return;
      if (wo === 'naechstes' && ortStufe(plan[i]) === 'dran') return;
      const [e] = plan.splice(i, 1); let an;
      if (wo === 'ende') an = plan.length;
      else if (wo === 'naechstes') an = plan.findIndex((y) => ortStufe(y) === 'kommt');
      else { const r = schluessel(x); an = plan.findIndex((y) => ortStufe(y) === 'kommt' && ortSchluessel(y) > r); }
      plan.splice(an < 0 ? plan.length : an, 0, e);
    }, `„${kurzName(x)}“ ${vorName}`, x);
  };
  // LW-2: aus der Matrix in den Fahrplan gezogen – vor den j-ten Platz (j = Anzahl Plätze: ans Ende)
  const einplanenAn = (x, j) => { const ziel = j < sichtbar.length ? plan[sichtbar[j]] : null; const b = blockVon(x);
    aendere(() => { if (!imPlan(x)) setze(b, x.id, 'lernen'); const i = plan.findIndex((y) => y.block_id === b); if (i < 0) return;
      if (plan[i] === ziel) return; const [e] = plan.splice(i, 1); const an = ziel ? plan.indexOf(ziel) : -1;
      if (!ziel) { const nach = plan.map((y) => ortStufe(y)).lastIndexOf('kommt'); plan.splice(nach < 0 ? plan.length : nach + 1, 0, e); } else plan.splice(an < 0 ? plan.length : an, 0, e); },
    `„${kurzName(x)}“ auf Platz ${Math.min(j, sichtbar.length) + 1} eingeplant`, x); };
  // LW-2 (Abschnitt 6): alle fehlenden Themen der gewählten Klassen in einem Schritt einplanen, sortiert nach Klasse und Lehrplan (ohne Zusatz-Teile)
  const alleEinplanen = (ts) => aendere(() => { ts.slice().sort((a, b) => schluessel(a) - schluessel(b)).forEach((x) => { if (!imPlan(x)) setze(blockVon(x), x.id, 'lernen'); }); },
    `${ts.length} ${ts.length === 1 ? 'Thema' : 'Themen'} eingeplant (nach Klasse und Lehrplan)`, ts);
  const ausDemPlan = (x) => aendere(() => { const b = blockVon(x);
    if (kannAbwaehlen) setze(b, x.id, 'aus'); else { const i = plan.findIndex((y) => y.block_id === b); if (i >= 0) plan.splice(i, 1); } }, `„${kurzName(x)}“ aus dem Plan genommen`, x);
  const stufeSetzen = (x, wahl) => aendere(() => setze(blockVon(x), x.id, wahl),
    `„${x.titel}“: ${{ lernen: 'Lernen', wiederholen: 'Kann er – wiederholen', komplett: 'Kann er komplett', wieder: 'wieder in der Wiederholung' }[wahl]}`, x);

  // ---------- Zustand der Seite ----------
  const zst = { sa: LERN_MX_SA[rest[0]] ? rest[0] : kindSa, zeigen: 'alle', q: '', sel: null, einstieg: null, handy: 'alle', fahrplanAuf: false, offenKl: new Set(), offenOrt: new Set(), auswahl: null, hl: null, filterAuf: false, legende: false };
  const klSchl = `lw.kl.${id}`;
  const klStandard = () => new Set(LERN_MX_KL.filter((k) => !kindKl || k >= Math.min(kindKl, 10)));
  let klassen = (() => { try { const v = JSON.parse(localStorage.getItem(klSchl) || 'null'); if (Array.isArray(v) && v.some((k) => LERN_MX_KL.includes(k))) return new Set(v.filter((k) => LERN_MX_KL.includes(k))); } catch { /* Standard */ } return klStandard(); })();
  const klMerken = () => { try { localStorage.setItem(klSchl, JSON.stringify([...klassen])); } catch { /* ohne Speicher */ } };
  const modus = () => (innerWidth < 760 ? 'handy' : innerWidth < 1100 ? 'tablet' : 'rechner');
  let sa = zst.sa;

  // ---------- Hervorheben: Zeigen · Einstieg prüfen · Suche ----------
  const gekonnt = (s) => s.stufe === 'komplett' || s.stufe === 'wiederholung';
  const ringStufe = (x) => stufeVon(x);
  // ---------- 12.7 Teile und Zusatz: aus den Feldern teil/teile/untertitel, sonst aus dem Titel „Grund – Teil 2 von 2 · Untertitel“ (keine feste Zahl) ----------
  const teilVon = (x) => { if (!x) return null; const r = x.roh || {};
    if (Number(r.teil) && Number(r.teile) > 1) return { n: Number(r.teil), von: Number(r.teile), grund: r.titel_grund || String(x.titel).replace(/ – Teil \d+ von \d+.*$/, ''), unter: r.untertitel || '' };
    const m = String(x.titel).match(/^(.*?) – Teil (\d+) von (\d+)(?: · (.*))?$/); return m ? { grund: m[1], n: Number(m[2]), von: Number(m[3]), unter: m[4] || r.untertitel || '' } : null; };
  const familie = (x) => { const t = teilVon(x); if (!t) return []; return M.themen.filter((y) => { const ty = teilVon(y); return ty && ty.grund === t.grund && ty.von === t.von; }).sort((a, b) => teilVon(a).n - teilVon(b).n); };
  // Zusatz: Teil ohne Lehrplan-Punkt in dieser Schulart (oder vom Server so markiert)
  const zusatz = (x, s2 = sa) => { const z = x.roh?.zusatz; if (z === true || (z && !Array.isArray(z) && typeof z === 'object' && z[s2])) return true;
    if (lernMxZusatzGruppe(x, lernKindGruppe(s2, kindU.schulart === s2 ? kindU : null))) return true; return !!teilVon(x) && !lernMxKl(x, s2); };
  // ZP-App (Muss aus ChatGPT 966): eingeplanter Zusatz-Teil – vom Server (thema_stufe.zusatz_eingeplant), sonst Zusatz in der Schulart des Kindes mit Platz im Plan
  const zusEingeplant = (x) => { const s = stufeVon(x); return !s.zusatz_geschafft && (!!s.zusatz_eingeplant || (zusatz(x, kindSa) && imPlan(x) && ['dran', 'kommt'].includes(s.stufe))); };
  const zusXY = (x) => { const s = stufeVon(x); const y = Number(s.etappen) || lernLwEtappen(x, s); return { x: Math.min(y, Number(s.gelandet) || 0), y }; };
  // harte Voraussetzungen (aus dem Raster; dazu Teil n−1 → Teil n, außer bei Zusatz in der Schulart des Kindes); aufgelöste Themen zählen nicht
  const hartVor = (x) => { const l = (M.vor.get(x.id) || []).filter((e) => e.art === 'hart' && M.by.has(e.id) && !M.by.get(e.id).ohneFlug).map((e) => e.id);
    const t = teilVon(x); if (t && t.n > 1) { const v = familie(x).find((y) => teilVon(y).n === t.n - 1); if (v && !zusatz(v, kindSa) && !zusatz(x, kindSa) && !l.includes(v.id)) l.push(v.id); }
    return l; };
  // Reihenfolge-Konflikte im Fahrplan: Fall 1 = Voraussetzung kommt später, Fall 3 = weder gekonnt noch im Plan
  const konflikte = () => { const r = []; ordne();
    for (const i of sichtbar) for (const x of fpThemen(plan[i])) { const px = platzInfo(x)?.pos; if (px == null) continue;
      for (const vid of hartVor(x)) { const v = M.by.get(vid); if (gekonnt(stufeVon(v))) continue; const pv = platzInfo(v)?.pos;
        if (pv != null) { if (pv > px) r.push({ fall: 1, x, v }); } else if (!imPlan(v) || stufeVon(v).stufe === 'nicht_im_plan') r.push({ fall: 3, x, v }); } }
    return r; };
  const fehlend = () => M.themen.filter((x) => inKlassen(x) && !x.ohneFlug && !zusatz(x) && stufeVon(x).stufe === 'nicht_im_plan');
  const einstiegListe = () => { const z = zst.einstieg; if (!z) return null;
    const ts = M.themen.filter((x) => !x.ohneFlug && lernMxKl(x, sa) && lernMxKl(x, sa) < z && (sa === 'ib_myp' || !x.pflicht || x.pflicht.includes(sa)));
    return { ts, fehlt: ts.filter((x) => !gekonnt(stufeVon(x))) }; };
  const passt = (x) => {
    const s = stufeVon(x);
    if (zst.zeigen === 'raus' && (s.stufe !== 'nicht_im_plan' || zusatz(x))) return false;
    if (zst.zeigen === 'drin' && !['dran', 'kommt'].includes(s.stufe)) return false;
    if (zst.einstieg) { const e = einstiegListe(); if (!e.fehlt.includes(x)) return false; }
    const q = zst.q.trim().toLowerCase(); return !q || `${x.titel} ${x.umfang} ${x.gebiet} ${x.etappen.map((e) => e.titel).join(' ')}`.toLowerCase().includes(q);
  };
  const inKlassen = (x) => klassen.has(lernMxZeile(x, sa));

  // ---------- Karte ----------
  const kennzeichen = (x, kurz = false) => el('span', { class: 'lw-sch' }, ...['gym_by', 'rs_by', 'ib_myp'].map((s2) => { const v = x.jg[s2];
    if (!v && s2 === 'ib_myp' && sa !== 'ib_myp') return null;
    const cls = (s2 === sa ? (v ? 'lw-ref' : 'lw-ref-fehlt') : v ? '' : 'lw-fehlt');
    return el('b', { class: cls }, el('span', { class: 'lw-lang' }, `${LERN_LW_SA[s2]} ${v || '–'}`), el('span', { class: 'lw-kurz', 'aria-hidden': 'true' }, `${LERN_LW_SA[s2][0]}${v || '–'}`)); }));
  const standText = (x, s) => {
    const n = lernLwEtappen(x, s);
    switch (s.stufe) {
      case 'komplett': return s.gesetzt === 'komplett' ? '◉ gesetzt' : '◉ kann er';
      case 'wiederholung': return s.wdh_nr ? `↻ Wdh ${s.wdh_nr}/5` : '↻ Wdh';
      case 'dran': return `▶ Etappe ${s.etappe_jetzt || Math.min((Number(s.gelandet) || 0) + 1, n)}/${n}`;
      case 'kommt': { const pl = platz(x); return pl ? `Platz ${pl}` : '○ im Plan'; }
      default: { if (zusatz(x)) return null; const g = Number(s.gelandet) || Number(s.begonnen) || 0; return g ? `${Math.min(g, n)}/${n} begonnen` : '+ einplanen'; }
    }
  };
  const art = (x, s) => (s.stufe === 'dran' ? 'dran' : s.stufe === 'kommt' ? 'plan' : s.stufe === 'wiederholung' ? 'wdh' : s.stufe === 'komplett' ? 'fertig' : lernMxKl(x, sa) ? 'raus' : 'fremd');
  let gezogen = false; // nach dem Ziehen kein Klick
  const karte = (x, famKl = '') => {
    const s = stufeVon(x); const a = art(x, s); const pl = platz(x); const b = blockVon(x); const tl = teilVon(x); const zs = zusatz(x);
    const key = `${b}:${x.id}`; const gew = zst.auswahl?.has(key); const st = standText(x, s);
    const k = el('button', { type: 'button', class: `lw-karte lw-${a}` + (zs ? ' lw-zusatz' : '') + (zusEingeplant(x) ? ' lw-zp' : '') + famKl + (x.ohneFlug ? ' lw-aufg' : '') + (passt(x) ? '' : ' lw-blass') + (zst.sel === x.id ? ' lw-sel' : '') + (zst.hl === b ? ' lw-hl' : '') + (gew ? ' lw-gew' : ''),
      'data-id': String(x.id), 'data-block': String(b), 'data-fam': tl ? tl.grund : null, 'aria-pressed': zst.auswahl ? String(!!gew) : null, 'aria-expanded': zst.auswahl ? null : String(zst.sel === x.id),
      title: tl ? `${tl.grund} – Teil ${tl.n} von ${tl.von}${tl.unter ? ' · ' + tl.unter : ''}${zs ? ' (Zusatz)' : ''}` : null,
      onmouseenter: tl ? () => matrixWrap.querySelectorAll('.lw-karte[data-fam]').forEach((c) => { if (c !== k && c.dataset.fam === tl.grund) c.classList.add('lw-fam-hl'); }) : null,
      onmouseleave: tl ? () => matrixWrap.querySelectorAll('.lw-fam-hl').forEach((c) => c.classList.remove('lw-fam-hl')) : null,
      onclick: () => { if (gezogen) { gezogen = false; return; } if (zst.auswahl) { if (gew) zst.auswahl.delete(key); else zst.auswahl.add(key); zeichneAlles(); return; } oeffne(x.id); } },
      zst.auswahl ? el('span', { class: 'lw-cb', 'aria-hidden': 'true' }, gew ? '✓' : '') : null,
      pl ? el('span', { class: 'lw-pl', title: `Platz ${pl} im Fahrplan` }, String(pl)) : s.stufe === 'nicht_im_plan' && !zs ? el('span', { class: 'lw-pl lw-plus', 'aria-hidden': 'true' }, '+') : null,
      el('span', { class: 'lw-t' }, tl ? tl.grund : x.titel, tl ? el('span', { class: 'lw-teil', 'aria-label': `Teil ${tl.n} von ${tl.von}` }, `${tl.n}/${tl.von}`) : null),
      tl?.unter ? el('span', { class: 'lw-u' }, tl.unter) : null,
      zusEingeplant(x) ? el('span', { class: 'lw-m lw-zp-m' }, el('span', { class: 'lw-zus-marke lw-zp-marke' }, 'Zusatz · eingeplant'), el('span', { class: 'lw-st' }, `${pl ? `Platz ${pl} · ` : ''}${zusXY(x).x}/${zusXY(x).y} Etappen`))
        : el('span', { class: 'lw-m' }, zs && s.stufe === 'nicht_im_plan' ? el('span', { class: 'lw-zus-marke' }, 'Zusatz') : el('span', { class: 'lw-st' }, st), zs && s.stufe !== 'nicht_im_plan' ? el('span', { class: 'lw-zus-marke' }, 'Zusatz') : null, kennzeichen(x)));
    k.addEventListener('pointerdown', (ev) => karteZiehen(ev, x, k));
    return k;
  };

  // ---------- Matrix ----------
  const gebiete = () => { const reihe = M.gebiete || LERN_MX_GEB; return [...reihe, ...new Set(M.themen.map((x) => x.gebiet).filter((g) => !reihe.includes(g)))].filter((g) => M.themen.some((x) => x.gebiet === g)); };
  const reihe = (x) => Number(x.r[sa]) || Number(x.r.gym_by) || 999;
  const imFeld = (k, g) => { const l = M.themen.filter((x) => lernMxZeile(x, sa) === k && x.gebiet === g).sort((a, b) => (lernMxKl(a, sa) ? 0 : 1) - (lernMxKl(b, sa) ? 0 : 1) || reihe(a) - reihe(b) || a.titel.localeCompare(b.titel));
    const aus = []; const da = new Set();
    for (const x of l) { if (da.has(x.id)) continue; const t = teilVon(x);
      const fam = t ? l.filter((y) => { const ty = teilVon(y); return ty && ty.grund === t.grund && ty.von === t.von; }).sort((a, b) => teilVon(a).n - teilVon(b).n) : [x];
      fam.forEach((y, i) => { da.add(y.id); y._fam = fam.length > 1 ? ' lw-fam' + (i === 0 ? ' lw-fam-a' : '') + (i === fam.length - 1 ? ' lw-fam-z' : '') : ''; aus.push(y); }); }
    // LW-2b K1: Themen desselben Platzes (3a, 3b …) stehen in der Zelle in Buchstaben-Reihenfolge
    const pi = aus.map((y) => platzInfo(y)); const proNr = new Map();
    pi.forEach((p, i) => { if (p) { if (!proNr.has(p.nr)) proNr.set(p.nr, []); proNr.get(p.nr).push(i); } });
    for (const idx of proNr.values()) { if (idx.length < 2) continue; const sortiert = idx.map((i) => aus[i]).sort((a, b) => platzInfo(a).pos - platzInfo(b).pos); idx.forEach((i, k) => { aus[i] = sortiert[k]; }); }
    return aus; };
  const karteImFeld = (x) => karte(x, x._fam || '');
  const farbe = (k) => LERN_KL_FARBE[k] || '#888';
  const andere = () => Object.keys(LERN_MX_SA).filter((s2) => s2 !== sa);
  const kasten = (k) => el('div', { class: 'lw-kz' },
    el('span', { class: 'lw-kb' + (k === 9 ? ' lw-hell' : ''), style: `background:${farbe(k)}`, title: sa === 'ib_myp' ? LERN_IB_HINWEIS : null }, el('small', {}, sa === 'ib_myp' ? 'MYP-Jahr' : LERN_LW_SA[sa]), sa === 'ib_myp' ? `${k - 5}` : `Kl. ${k}`),
    (() => { const r = lernLwRing(M.themen, ringStufe, sa, k, lernKindGruppe(sa, kindU.schulart === sa ? kindU : null)); return [lernLwRingEl(r, true), el('small', { class: 'lw-kn' }, `${r.fertig}/${r.themen} Themen`)]; })(),
    el('span', { class: 'lw-rk2' }, ...andere().map((s2) => lernLwRingEl(lernLwRing(M.themen, ringStufe, s2, k), false))));
  // ganz fertige Klasse: alle Pflichtthemen dieser Schule in der Zeile gekonnt
  const fertigeKlasse = (k) => { const ts = M.themen.filter((x) => !x.ohneFlug && lernMxKl(x, sa) === k); return ts.length && ts.every((x) => gekonnt(stufeVon(x))) ? ts : null; };
  const zuReihe = (k, ts) => el('button', { type: 'button', class: 'lw-zu-reihe', 'aria-expanded': 'false', onclick: () => { zst.offenKl.add(k); zeichneMatrix(); } },
    el('span', { class: 'lw-kb' + (k === 9 ? ' lw-hell' : ''), style: `background:${farbe(k)}` }, sa === 'ib_myp' ? `MYP-Jahr ${k - 5}` : `${LERN_LW_SA[sa]} Kl. ${k}`),
    `✓ Alles gekonnt · ${ts.length} Themen · davon ${ts.filter((x) => stufeVon(x).stufe === 'wiederholung').length} in Wiederholung`, el('span', { class: 'lw-leise' }, 'aufklappen ▾'));
  const matrixWrap = el('div', { class: 'lw-mw' });
  const zeichneMatrix = () => {
    const gebs = gebiete(); const kl = LERN_MX_KL.filter((k) => klassen.has(k));
    if (modus() === 'handy') {
      lernErsetze(matrixWrap, el('div', { class: 'lw-liste' }, ...kl.map((k) => { const f = fertigeKlasse(k);
        if (f && !zst.offenKl.has(k)) return el('section', { class: 'lw-liste-klasse', 'data-kl': String(k) }, zuReihe(k, f));
        return el('section', { class: 'lw-liste-klasse', 'data-kl': String(k) }, el('div', { class: 'lw-liste-kopf' }, kasten(k)),
          ...gebs.map((g) => { const l = imFeld(k, g); return l.length ? el('div', { class: 'lw-gruppe' }, el('b', { class: 'lw-gruppe-name' }, g), ...l.map(karteImFeld)) : null; })); })));
      return;
    }
    const zellen = [el('div', { class: 'lw-ecke' }), ...gebs.map((g) => el('div', { class: 'lw-gh' }, g))];
    for (const k of kl) { const f = fertigeKlasse(k);
      if (f && !zst.offenKl.has(k)) { zellen.push(el('div', { class: 'lw-zu-zeile', 'data-kl': String(k), style: `grid-column:1 / span ${gebs.length + 1}` }, zuReihe(k, f))); continue; }
      zellen.push(el('div', { class: 'lw-kz-zelle', 'data-kl': String(k) }, kasten(k)), ...gebs.map((g) => el('div', { class: 'lw-zel' }, ...imFeld(k, g).map(karteImFeld)))); }
    lernErsetze(matrixWrap, el('div', { class: 'lw-mx', style: `--n:${gebs.length}` }, ...zellen),
      kl.length ? null : el('p', { class: 'muted' }, 'Keine Klasse gewählt.'));
  };

  // ---------- Fahrplan (links) ----------
  const rail = el('aside', { class: 'lw-rail', 'aria-label': 'Fahrplan' });
  let zieht = false;
  const fpTitel = (px) => { const ts = themenImOrt(px.block_id).filter((y) => !px.ausgelassen.includes(y.id)); const o = ortById.get(px.block_id);
    return { ts, titel: ts.length === 1 ? ts[0].titel : ts.length ? `${ts[0].titel}${ts.length > 1 ? ` und ${ts.length - 1} weitere` : ''}` : (o?.titel || '?'), o }; };
  const fpEintrag = (px, j, gruppe) => {
    const { ts, titel, o } = fpTitel(px); const dran = gruppe === 'dran'; const auf = zst.offenOrt.has(px.block_id);
    const jetzt = ts.find((y) => stufeVon(y).stufe === 'dran') || ts.find((y) => stufeVon(y).stufe === 'kommt') || ts[0];
    const s = jetzt ? stufeVon(jetzt) : null; const n = jetzt ? lernLwEtappen(jetzt, s) : 0; const g = Math.min(n, Number(s?.gelandet) || 0);
    const fertig = ts.filter((y) => gekonnt(stufeVon(y))).length;
    const fpLand = jetzt ? lernFlugName(id, { thema_id: jetzt.id }, '') : ''; // WK F3: Land (bei „dran“ mit Stadt der Etappe) wie auf der Reisekarte
    const fpStadt = dran && jetzt && fpLand ? lernEtappenStadt(id, jetzt.id, Number(s?.etappe_jetzt) || Math.min(g + 1, n), '') : '';
    const meta = [fpLand ? (fpStadt ? `${fpLand} · ${fpStadt}` : fpLand) : null, jetzt?.gebiet || o?.kontinent, jetzt ? `${LERN_LW_SA[sa]} ${lernMxKl(jetzt, sa) || '–'}` : null, ts.length > 1 ? `${fertig}/${ts.length} Themen` : null, dran && jetzt ? `Etappe ${s.etappe_jetzt || Math.min(g + 1, n)}/${n}` : null].filter(Boolean).join(' · ');
    // LW-2 (4a): dauerhafter Hinweis, solange eine harte Voraussetzung fehlt oder später kommt
    const tsZp = ts.filter((y) => ['dran', 'kommt'].includes(stufeVon(y).stufe)); const zp = !!px.zusatz_eingeplant || (tsZp.length > 0 && tsZp.every(zusEingeplant)); const zpTeil = zp ? 0 : tsZp.filter(zusEingeplant).length; // KJ 2 S5c: Zusatz in einer Gruppe → Marke „+ n Zusatz“ // ZP: eigener Platz, keine Reihenfolge-Warnung, sperrt nichts
    const kf = zp ? [] : konfl.filter((k) => ts.includes(k.x));
    const warn = kf.map((k) => el('span', { class: 'lw-fp-warn-zeile' }, `braucht „${k.v.titel}“ – ${k.fall === 1 ? `kommt erst auf Platz ${platz(k.v)}` : 'nicht gelernt, nicht im Plan'}`));
    const griff = el('span', { class: 'lw-gr', role: 'button', 'aria-label': `${titel} ziehen`, title: 'Ziehen zum Umsortieren' }, '⋮⋮');
    griff.addEventListener('pointerdown', (ev) => ziehen(ev, j));
    const tausche = (k) => aendere(() => { [plan[sichtbar[k]], plan[sichtbar[j]]] = [plan[sichtbar[j]], plan[sichtbar[k]]]; }, `„${titel}“ auf Platz ${k + 1}`);
    return el('li', { class: 'lw-fp' + (dran ? ' lw-fp-dran' : '') + (kf.length ? ' lw-fp-warn' : '') + (zp ? ' lw-fp-zp' : ''), 'data-block': String(px.block_id),
      onmouseenter: () => { if (zieht) return; zst.hl = px.block_id; matrixWrap.querySelectorAll(`.lw-karte[data-block="${px.block_id}"]`).forEach((c) => c.classList.add('lw-hl')); },
      onmouseleave: () => { zst.hl = null; matrixWrap.querySelectorAll('.lw-karte.lw-hl').forEach((c) => c.classList.remove('lw-hl')); } },
      griff, el('span', { class: 'lw-nr' }, String(j + 1)),
      el('button', { type: 'button', class: 'lw-fp-text', onclick: () => { if (jetzt) oeffne(jetzt.id); } }, el('b', {}, titel), el('small', {}, meta),
        zpTeil ? el('span', { class: 'lw-zus-marke lw-zp-marke lw-fp-zp-teil' }, `+ ${zpTeil} Zusatz`) : null,
        zp && jetzt ? el('small', { class: 'lw-fp-zp-zeile' }, el('span', { class: 'lw-zus-marke lw-zp-marke' }, 'ZUSATZ · EINGEPLANT'), ` ${zusXY(jetzt).x} von ${zusXY(jetzt).y} Etappen · ohne Flug-Test`) : null),
      el('span', { class: 'lw-pf' },
        el('button', { type: 'button', 'aria-label': `${titel} nach oben`, disabled: j === 0 ? true : null, onclick: () => tausche(j - 1) }, '↑'),
        el('button', { type: 'button', 'aria-label': `${titel} nach unten`, disabled: j === sichtbar.length - 1 ? true : null, onclick: () => tausche(j + 1) }, '↓')),
      dran && jetzt ? el('span', { class: 'lw-bar', role: 'img', 'aria-label': `${g} von ${n} Etappen gelandet` }, el('i', { style: `width:${lernPz(g, n)}%` })) : null,
      warn.length ? el('span', { class: 'lw-fp-warn-box' }, ...warn) : null,
      ts.length > 1 ? el('button', { type: 'button', class: 'lw-fp-auf', 'aria-expanded': String(auf), onclick: () => { if (auf) zst.offenOrt.delete(px.block_id); else zst.offenOrt.add(px.block_id); zeichneRail(); } }, auf ? 'Themen ▾' : 'Themen ▸') : null,
      auf ? el('ul', { class: 'lw-fp-fluege' }, ...ts.map((y) => { const sy = stufeVon(y); const py = platz(y); return el('li', {}, el('button', { type: 'button', onclick: () => oeffne(y.id) }, py ? el('b', { class: 'lw-fp-buchst' }, py + ' ') : lernStufeZeichenEl(sy), ' ', y.titel)); })) : null);
  };
  const ausserhalb = (stufe, titel) => {
    const ts = M.themen.filter((x) => imPlan(x) && stufeVon(x).stufe === stufe);
    return el('details', { class: 'lw-zu' }, el('summary', {}, titel, el('span', {}, ` ${ts.length} ›`)),
      el('ul', { class: 'lw-zu-liste' }, ...ts.map((x) => { const s = stufeVon(x);
        return el('li', {}, el('button', { type: 'button', class: 'lw-zu-titel', onclick: () => oeffne(x.id) }, x.titel, el('small', {}, ` · ${lernStufeZusatz(s)}`)),
          kannWdh && stufe === 'komplett' ? el('button', { type: 'button', class: 'lern-lp-textlink lern-lp-wieder', 'aria-label': `${x.titel}: Wieder in die Wiederholung`, onclick: () => stufeSetzen(x, 'wieder') }, 'Wieder in die Wiederholung') : null); })));
  };
  let konfl = [];
  const zeichneRail = () => {
    const mit = ordne(); const nDran = mit.filter((m) => m[2] === 'dran').length; konfl = konflikte();
    const nZus = sichtbar.reduce((n, i) => { const ts = fpThemen(plan[i]); return n + (plan[i].zusatz_eingeplant && !ts.some(zusEingeplant) ? 1 : ts.filter(zusEingeplant).length); }, 0);
    const nThemen = sichtbar.reduce((n, i) => n + fpThemen(plan[i]).filter((x) => !zusEingeplant(x)).length, 0);
    const fehlt = zst.zeigen === 'raus' ? fehlend() : []; const bisKl = Math.max(...klassen);
    const zeilen = []; sichtbar.forEach((i, j) => { if (j === 0 && nDran) zeilen.push(el('li', { class: 'lw-rsek' }, 'GERADE DRAN')); if (j === nDran) zeilen.push(el('li', { class: 'lw-rsek' }, 'KOMMT NOCH'));
      zeilen.push(fpEintrag(plan[i], j, j < nDran ? 'dran' : 'kommt')); });
    lernErsetze(rail,
      el('div', { class: 'lw-rk' }, el('b', {}, 'Fahrplan'), el('span', { class: 'lw-rk-zahl' }, `${sichtbar.length} ${sichtbar.length === 1 ? 'Platz' : 'Plätze'} · ${nThemen} ${nThemen === 1 ? 'Thema' : 'Themen'}${nZus ? ` · + ${nZus} Zusatz` : ''}`),
        modus() === 'tablet' ? el('button', { type: 'button', class: 'lw-x', 'aria-label': 'Fahrplan schließen', onclick: () => { zst.fahrplanAuf = false; zeichneAlles(); } }, '✕') : null),
      fehlt.length ? el('div', { class: 'lw-alle' }, el('span', {}, `${fehlt.length} ${fehlt.length === 1 ? 'Thema' : 'Themen'} (bis Kl. ${bisKl}) noch nicht im Plan`),
        el('button', { type: 'button', class: 'primary', onclick: () => alleEinplanen(fehlt) }, `Alle ${fehlt.length} einplanen (nach Klasse und Lehrplan)`)) : null,
      el('ol', { class: 'lw-rliste' }, ...zeilen),
      !plan.length ? el('p', { class: 'muted small lw-leer' }, 'Der Plan ist leer. Ohne Plan sieht das Kind alle Flüge. Ein Thema antippen und „In den Plan“ wählen.')
        : !sichtbar.length ? el('p', { class: 'muted small lw-leer' }, 'Alle Orte im Plan sind gelandet. Ein Thema antippen und „In den Plan“ wählen.') : null,
      el('p', { class: 'lw-dz' }, modus() === 'handy' ? 'Einplanen: unter „Alle Themen“ ein Thema antippen' : modus() === 'rechner' ? '+ Thema hierher ziehen' : '+ Thema antippen und einplanen'),
      el('p', { class: 'lw-rsek' }, 'AUSSERHALB DES FAHRPLANS'),
      ausserhalb('wiederholung', '↻ In Wiederholung'), ausserhalb('komplett', '✓ Fertig (kann er)'),
      lernAendern({ lernender_id: id }, { bezug: 'plan', wo: `Flugplan ${kind.name || ''}`, art: 'sonst' }));
  };
  // Ziehen im Fahrplan (Maus, Finger, Stift): die anderen Einträge rücken zur Seite; losgelassen wird einmal gespeichert
  const ziehen = (ev, j) => {
    if (gesperrt || (ev.button !== undefined && ev.button !== 0)) return;
    ev.preventDefault();
    const liste = rail.querySelector('.lw-rliste'); const zeilen = [...liste.querySelectorAll(':scope > .lw-fp')]; const li = zeilen[j]; if (!li) return;
    const mitten = zeilen.map((z) => { const b = z.getBoundingClientRect(); return b.top + b.height / 2; });
    const h = li.getBoundingClientRect().height + 5; const start = ev.clientY, startX = ev.clientX; let ziel = j; zieht = true; let raus = false;
    tosteWeg(); // LW-2b K2: laufende Meldung weg, damit „Hier loslassen = aus dem Plan nehmen“ zu sehen ist
    li.classList.add('zieht');
    const lauf = (e) => { const dy = e.clientY - start, dx = e.clientX - startX;
      // LW-2 (4a): über der Matrix losgelassen = aus dem Plan nehmen (Matrix rot gestrichelt)
      const mw = matrixWrap.getBoundingClientRect(); raus = modus() !== 'handy' && e.clientX > mw.left + 8 && e.clientX < mw.right && e.clientY > mw.top && e.clientY < mw.bottom;
      matrixWrap.classList.toggle('lw-raus-ziel', raus);
      li.style.transform = `translate(${raus ? dx : 0}px, ${dy}px)`; const mitte = mitten[j] + dy;
      ziel = zeilen.reduce((n, z, k) => n + (k !== j && mitten[k] < mitte ? 1 : 0), 0);
      zeilen.forEach((z, k) => { if (k === j) return; z.style.transform = k > j && k <= ziel ? `translateY(${-h}px)` : k < j && k >= ziel ? `translateY(${h}px)` : ''; }); };
    const ende = () => { window.removeEventListener('pointermove', lauf); window.removeEventListener('pointerup', ende); window.removeEventListener('pointercancel', ende);
      zeilen.forEach((z) => { z.style.transform = ''; }); li.classList.remove('zieht'); zieht = false; matrixWrap.classList.remove('lw-raus-ziel');
      if (raus) { const von = sichtbar[j]; const px = plan[von]; const { titel, ts } = fpTitel(px); aendere(() => { const i = plan.indexOf(px); if (i >= 0) plan.splice(i, 1); }, `„${titel}“ aus dem Plan genommen`, ts); return; }
      if (ziel !== j) { const von = sichtbar[j], nach = sichtbar[ziel]; const titel = fpTitel(plan[von]).titel; aendere(() => { const [x] = plan.splice(von, 1); plan.splice(nach, 0, x); }, `„${titel}“ auf Platz ${ziel + 1}`); } };
    window.addEventListener('pointermove', lauf); window.addEventListener('pointerup', ende); window.addEventListener('pointercancel', ende);
  };

  // LW-2 (4a): Karte aus der Matrix in den Fahrplan ziehen (Rechner; Tablet bei offenem Fahrplan). Blaue Linie zeigt den Platz.
  const karteZiehen = (ev, x, k) => {
    if (gesperrt || zst.auswahl || modus() === 'handy' || (modus() === 'tablet' && !zst.fahrplanAuf) || (ev.button !== undefined && ev.button !== 0)) return;
    const sx = ev.clientX, sy = ev.clientY; let geist = null, linie = null, j = null;
    const zeilen = () => [...rail.querySelectorAll('.lw-rliste > .lw-fp')];
    const lauf = (e) => {
      if (!geist) { if (Math.hypot(e.clientX - sx, e.clientY - sy) < 7) return;
        tosteWeg(); geist = el('div', { class: 'lw-geist' }, teilVon(x) ? `${teilVon(x).grund} ${teilVon(x).n}/${teilVon(x).von}` : x.titel); document.body.append(geist); rail.classList.add('lw-ziel'); k.classList.add('lw-zieht-weg'); }
      geist.style.left = `${e.clientX + 10}px`; geist.style.top = `${e.clientY + 8}px`;
      const r = rail.getBoundingClientRect(); const drin = e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
      linie?.remove(); linie = null; j = null; if (!drin) return;
      const zs = zeilen(); j = zs.findIndex((z) => { const b = z.getBoundingClientRect(); return e.clientY < b.top + b.height / 2; }); if (j < 0) j = zs.length;
      linie = el('li', { class: 'lw-drop-linie', 'aria-hidden': 'true' }); if (zs[j]) zs[j].before(linie); else rail.querySelector('.lw-rliste')?.append(linie);
    };
    const ende = () => { removeEventListener('pointermove', lauf); removeEventListener('pointerup', ende); removeEventListener('pointercancel', ende);
      linie?.remove(); geist?.remove(); rail.classList.remove('lw-ziel'); k.classList.remove('lw-zieht-weg');
      if (!geist) return; gezogen = true; setTimeout(() => { gezogen = false; }, 0);
      if (j !== null) einplanenAn(x, j); };
    addEventListener('pointermove', lauf); addEventListener('pointerup', ende); addEventListener('pointercancel', ende);
  };

  // ---------- Detail-Schublade ----------
  const drawer = el('aside', { class: 'lw-drawer', 'aria-label': 'Thema im Detail' });
  const geholt = new Map();
  const nachladen = (x) => {
    if (!d.matrix || geholt.has(x.id)) return geholt.get(x.id) === 'laedt' ? el('p', { class: 'small muted' }, 'Einzelheiten werden geladen …') : null;
    geholt.set(x.id, 'laedt');
    lernCall('schule_lehrplan_thema', { thema_id: x.id, lernender_id: id }).then((t) => {
      if (!t || !live()) return;
      const neu = Object.fromEntries(['kurz', 'ort', 'merke', 'etappen', 'beispiel', 'lehrplan', 'eigenstaendig', 'lernbereich'].filter((k) => t[k] !== undefined).map((k) => [k, t[k]]));
      if (t.was_gefordert) neu.beschreibung = t.was_gefordert;
      details.set(x.id, neu); geholt.set(x.id, 'ok'); baue();
    }).catch(() => { geholt.set(x.id, 'fehler'); }).finally(() => { if (live() && zst.sel === x.id) zeichneDetail(); });
    return el('p', { class: 'small muted' }, 'Einzelheiten werden geladen …');
  };
  const etappenStand = (x, s) => {
    const eid = x.roh.einheit?.id ?? x.roh.einheit_id; const e = eid ? proEinheit().get(eid) : null; const ks = e?.karten || [];
    const byZiel = new Map(ks.map((k) => [k.lernziel, k]));
    const liste = x.etappen.length ? x.etappen : ks.map((k) => ({ titel: k.titel || k.lernziel, lernziel: k.lernziel }));
    // LW-2 K1: Etappen vor „etappe_jetzt“ (bzw. die ersten „gelandet“) ohne Karte zählen als gelandet – sonst widerspricht die Liste dem Kopf „3 von 7“
    const jetzt = Number(s.etappe_jetzt) || (s.stufe === 'dran' ? Math.min((Number(s.gelandet) || 0) + 1, liste.length) : 0); const gel = jetzt ? jetzt - 1 : Number(s.gelandet) || 0;
    let dranGesetzt = false;
    return liste.map((et, i) => { const k = (et.lernziel && byZiel.get(et.lernziel)) || (et.lernziel ? null : ks[i]) || null;
      let dot = '', wort = 'offen';
      if (!k?.sitzt && !k?.sicher && i < gel && !(k && (k.richtig || k.falsch))) { dot = s.stufe === 'wiederholung' ? 'w' : 'g'; wort = s.stufe === 'wiederholung' ? 'Wiederholung' : 'gelandet'; }
      else if (s.stufe === 'dran' && jetzt && i === jetzt - 1 && !k?.sitzt && !dranGesetzt) { dranGesetzt = true; dot = 'd'; wort = k && k.ziel ? `gerade dran (${Math.min(k.serie || 0, k.ziel)} von ${k.ziel})` : 'gerade dran'; }
      else if (et.pflicht === false && !k?.sitzt) { dot = ''; wort = 'freiwillig'; }
      else if (k?.sitzt || k?.sicher) { dot = s.stufe === 'wiederholung' ? 'w' : 'g'; wort = s.stufe === 'wiederholung' ? 'Wiederholung' : 'gelandet'; }
      else if (k && Number(k.falsch) > 0 && (k.fehler || []).length) { dot = 'f'; wort = `begonnen · ${k.falsch} ${Number(k.falsch) === 1 ? 'Fehler' : 'Fehler'}`; }
      else if (s.stufe === 'dran' && !jetzt && !dranGesetzt) { dranGesetzt = true; dot = 'd'; wort = k && k.ziel ? `gerade dran (${Math.min(k.serie || 0, k.ziel)} von ${k.ziel})` : 'gerade dran'; }
      else if (k && (k.richtig || k.falsch)) { dot = 'd'; wort = 'begonnen'; }
      return el('li', { class: 'lw-et' }, el('span', { class: 'lw-dot' + (dot ? ' lw-dot-' + dot : ''), 'aria-hidden': 'true' }), el('span', {}, `${i + 1} `, et.titel || `Etappe ${i + 1}`), el('small', {}, wort)); });
  };
  const fehlerOffen = (x, s) => { const eid = x.roh.einheit?.id ?? x.roh.einheit_id; const ks = (eid ? proEinheit().get(eid)?.karten : null) || [];
    const n = ks.filter((k) => !k.sitzt && (k.fehler || []).length).length; return n || (s.fehler_offen === true || Number(s.fehler_offen) > 0 || Number(s.wieder_offen) > 0 ? 1 : 0); };
  const vorKarte = (vid, art = '') => { const y = M.by.get(vid); const s = stufeVon(y); const pl = platz(y);
    const mark = (gekonnt(s) ? '✓' : pl ? `Platz ${pl}` : 'fehlt') + (art === 'empfohlen' ? ' · empfohlen' : '');
    return el('button', { type: 'button', class: 'lw-vk lw-vk-' + (gekonnt(s) ? 'ok' : pl ? 'plan' : 'fehlt'), onclick: () => oeffne(vid) }, el('b', {}, y.titel), el('small', {}, mark)); };
  let menueAuf = false;
  function zeichneDetail() {
    const x = zst.sel && M.by.get(zst.sel);
    drawer.classList.toggle('lw-auf', !!x); document.body.classList.toggle('lw-blatt-offen', !!x && modus() === 'handy');
    if (!x) { lernErsetze(drawer); return; }
    const s = stufeVon(x); const drin = imPlan(x); const pl = platz(x); const b = blockVon(x); const px = plan.find((y) => y.block_id === b);
    const aktiv = !drin ? null : px.kann_schon || px.kann.includes(x.id) ? 'komplett' : px.kw.includes(x.id) ? 'wiederholen' : 'lernen';
    const seg = (wahl, text) => el('button', { type: 'button', 'aria-pressed': String(aktiv === wahl), 'aria-label': `${x.titel}: ${text}`, onclick: () => stufeSetzen(x, wahl) }, text);
    const t = x.roh; const n = x.etappen.length || t.einheit?.karten || t.etappen_anzahl || 0; const nf = fehlerOffen(x, s);
    const vor = M.vor.get(x.id) || []; const nach = M.nach.get(x.id) || [];
    const z = lernMxZusatz(x, sa); const tl = teilVon(x); const fam = tl ? familie(x) : []; const zs = zusatz(x);
    const fehlenTeile = fam.filter((y) => !imPlan(y) && !gekonnt(stufeVon(y)) && stufeVon(y).stufe === 'nicht_im_plan');
    let auchZusatz = false;
    const teileZeile = (y) => { const ty = teilVon(y); const sy = stufeVon(y); const py = platz(y);
      const st = gekonnt(sy) ? '✓ geschafft' : sy.stufe === 'dran' ? `▶ Platz ${py || '–'}` : py ? `Platz ${py}` : 'nicht im Plan';
      return el('li', {}, el('button', { type: 'button', class: 'lw-teil-zeile' + (y.id === x.id ? ' lw-teil-hier' : ''), 'aria-current': y.id === x.id ? 'true' : null, onclick: () => oeffne(y.id) },
        el('b', {}, `Teil ${ty.n}`), ty.unter ? ` · ${ty.unter}` : '', ` · ${lernMxKl(y, sa) ? (sa === 'ib_myp' ? 'MYP-Jahr ' + (lernMxKl(y, sa) - 5) : 'Kl. ' + lernMxKl(y, sa)) : 'Zusatz'} · `, el('span', {}, st),
        zusatz(y) ? el('span', { class: 'lw-zus-marke' }, 'Zusatz') : null)); };
    lernErsetze(drawer,
      el('div', { class: 'lw-dkopf' },
        el('button', { type: 'button', class: 'lw-x', 'aria-label': 'Detail schließen', onclick: () => { zst.sel = null; menueAuf = false; zeichneAlles(); } }, '✕'),
        el('h2', {}, tl ? [tl.grund, ' – ', el('span', { class: 'lw-teil-lang' }, `Teil ${tl.n} von ${tl.von}`)] : x.titel),
        tl?.unter ? el('div', { class: 'lw-unter' }, tl.unter) : null,
        zusEingeplant(x) ? [el('p', { class: 'lw-zus-marke lw-zus-lang lw-zp-marke' }, `Zusatz · eingeplant – kein Pflichtstoff ${{ gym_by: 'im Gymnasium', rs_by: 'in der Realschule', ib_myp: 'im IB' }[kindSa]}`),
          el('p', { class: 'small lw-zp-stand' }, `${zusXY(x).x} von ${zusXY(x).y} Etappen · fertig, sobald alle gelandet (ohne Flug-Test) · dann Stempel und ★ 100, einmal`)]
        : zs ? el('p', { class: 'lw-zus-marke lw-zus-lang' }, `Zusatz – kein Pflichtstoff ${{ gym_by: 'im Gymnasium', rs_by: 'in der Realschule', ib_myp: 'im IB' }[sa]}`) : null,
        el('div', { class: 'lw-sub' }, lernFlugName(id, { thema_id: x.id }, '') ? el('span', { class: 'lw-land' }, lernFlugName(id, { thema_id: x.id }, '') + ' · ') : null, x.gebiet, z ? ` · ${z.text}` : ''), kennzeichen(x)),
      el('div', { class: 'lw-dinh' },
        el('h3', { class: 'lw-dh' }, `STAND VON ${String(kind.name || 'Kind').toUpperCase()}`),
        el('p', { class: 'lw-stpill ' + (LERN_STUFE[s.stufe]?.kl || '') }, lernStufeZeichenEl(s), ' ', el('b', {}, LERN_STUFE[s.stufe]?.wort || ''), ' · ', lernStufeZusatz(s), pl ? ` · Platz ${pl}` : ''),
        fam.length > 1 ? [el('h3', { class: 'lw-dh' }, 'TEILE DIESES THEMAS'), el('ul', { class: 'lw-teile' }, ...fam.map(teileZeile)),
          fehlenTeile.some((y) => !zusatz(y)) || fehlenTeile.length ? el('div', { class: 'lw-alle-teile' },
            fehlenTeile.some((y) => zusatz(y)) ? el('label', { class: 'small' }, el('input', { type: 'checkbox', onchange: (ev) => { auchZusatz = ev.target.checked; } }), ' auch Zusatz') : null,
            el('button', { type: 'button', onclick: () => { const ts = fehlenTeile.filter((y) => auchZusatz || !zusatz(y)); if (ts.length) aendere(() => ts.forEach((y) => setze(blockVon(y), y.id, 'lernen')), `${ts.length === 1 ? 'Ein Teil' : ts.length + ' Teile'} von „${tl.grund}“ eingeplant`, ts); } }, 'Alle Teile einplanen')) : null] : null,
        el('ol', { class: 'lw-etappen' }, ...etappenStand(x, s)),
        el('h3', { class: 'lw-dh' }, 'PLANEN'),
        el('div', { class: 'lw-planen' }, ...(drin && ['dran', 'kommt'].includes(s.stufe) ? [
          el('button', { type: 'button', onclick: () => einplanen(x, 'naechstes'), disabled: s.stufe === 'dran' || platzInfo(x)?.nr === 1 ? true : null }, 'Als Nächstes'),
          el('button', { type: 'button', onclick: () => einplanen(x, 'ende') }, 'Ans Ende'),
          el('button', { type: 'button', class: 'lw-raus', onclick: () => ausDemPlan(x) }, 'Aus dem Plan')]
          : drin ? [el('button', { type: 'button', class: 'lw-raus', onclick: () => ausDemPlan(x) }, 'Aus dem Plan')]
            : [el('span', { class: 'lw-split' },
              el('button', { type: 'button', class: 'primary', onclick: () => einplanen(x, 'naechstes') }, 'In den Plan: als Nächstes'),
              el('button', { type: 'button', class: 'primary lw-split-pfeil', 'aria-label': 'Weitere Möglichkeiten zum Einplanen', 'aria-expanded': String(menueAuf), onclick: () => { menueAuf = !menueAuf; zeichneDetail(); } }, '▾')),
            menueAuf ? el('div', { class: 'lw-menue', role: 'menu' },
              el('button', { type: 'button', role: 'menuitem', onclick: () => { menueAuf = false; einplanen(x, 'ende'); } }, '… ans Ende'),
              el('button', { type: 'button', role: 'menuitem', onclick: () => { menueAuf = false; einplanen(x, 'lehrplan'); } }, '… nach Lehrplan einsortieren')) : null])),
        el('h3', { class: 'lw-dh' }, 'STUFE ', el('a', { href: '#/info/stufen', class: 'lern-lp-info', 'aria-label': 'Was die Stufen bedeuten (So funktioniert’s)' }, 'ⓘ')),
        el('div', { class: 'lw-seg', role: 'group', 'aria-label': `Stufe für ${x.titel}` }, seg('lernen', 'Lernen'), kannWdh ? seg('wiederholen', 'Kann er – wiederholen') : null, kannJeFlug ? seg('komplett', 'Kann er komplett') : null),
        kannWdh && s.stufe === 'komplett' ? el('button', { type: 'button', class: 'lern-lp-textlink lern-lp-wieder', onclick: () => stufeSetzen(x, 'wieder') }, 'Wieder in die Wiederholung') : null,
        el('h3', { class: 'lw-dh' }, 'LEHRSTOFF'),
        x.umfang ? el('p', { class: 'small' }, x.umfang) : el('p', { class: 'small muted' }, 'Keine Beschreibung hinterlegt.'),
        el('p', { class: 'lw-links' }, t.einheit || t.einheit_id ? el('a', { href: `#/inhalte/${t.einheit?.id ?? t.einheit_id}` }, `Inhalte ansehen (${n} ${n === 1 ? 'Etappe' : 'Etappen'}) ›`) : el('span', { class: 'muted small' }, 'noch kein Inhalt'),
          nf ? el('a', { href: `#/kind/${id}-wackelt` }, `Fehler besprechen (${nf}) ›`) : null),
        t.einheit || t.einheit_id ? null : lernAendern({ block_id: b }, { bezug: 'flug', wo: `Flug „${x.titel}“`, art: 'neu', text: `Bitte Inhalte bauen: „${x.titel}“ (${t.ort || x.gebiet}, ${lernJahrgangText(x.jg)}).` }),
        nachladen(x),
        M.hatVerb ? [el('h3', { class: 'lw-dh' }, 'BRAUCHT VORHER'), vor.length ? el('div', { class: 'lw-vks' }, ...vor.map((e) => vorKarte(e.id, e.art))) : el('p', { class: 'small muted' }, 'Keine Voraussetzung hinterlegt.'),
          el('h3', { class: 'lw-dh' }, 'DARAUF BAUT AUF'), nach.length ? el('div', { class: 'lw-vks' }, ...nach.map((e) => vorKarte(e.id))) : el('p', { class: 'small muted' }, 'Kein späteres Thema hinterlegt.')] : null));
  }
  const oeffne = (tid) => { zst.sel = tid; menueAuf = false; const x = M.by.get(tid); if (x) { klassen.add(lernMxZeile(x, sa)); zst.offenKl.add(lernMxZeile(x, sa)); }
    if (modus() === 'tablet') zst.fahrplanAuf = false; zeichneAlles();
    requestAnimationFrame(() => matrixWrap.querySelector(`.lw-karte[data-id="${tid}"]`)?.scrollIntoView({ block: 'nearest', inline: 'nearest' })); };

  // ---------- Leiste ----------
  const seg = (name, wahl, ist, setze) => el('div', { class: 'lw-seg', role: 'group', 'aria-label': name }, ...wahl.map(([w, text]) =>
    el('button', { type: 'button', 'aria-pressed': String(ist() === w), onclick: () => { setze(w); zeichneAlles(); } }, text)));
  const suche = el('input', { type: 'search', class: 'lw-such', placeholder: 'Suchen', 'aria-label': 'Thema suchen' });
  suche.addEventListener('input', () => { zst.q = suche.value; zeichneMatrix(); });
  const leiste = el('div', { class: 'lw-leiste' }); const sammel = el('div', { class: 'lw-sammel lern-plan-sammel', role: 'region', 'aria-label': 'Sammelaktionen', hidden: true });
  const hinweis = el('div', { class: 'lw-hinweis' });
  const zahlen = () => { const ts = M.themen.filter(inKlassen); return { raus: ts.filter((x) => stufeVon(x).stufe === 'nicht_im_plan' && !zusatz(x)).length, drin: ts.filter((x) => ['dran', 'kommt'].includes(stufeVon(x).stufe)).length }; };
  const zeichneLeiste = () => {
    const z = zahlen(); const imFp = new Set(sichtbar.flatMap((i) => themenImOrt(plan[i].block_id).filter((y) => !plan[i].ausgelassen.includes(y.id)).map((y) => lernMxZeile(y, sa))));
    // K2: „Bereit für Klasse …?“ (vorher „Einstieg prüfen“) – zeigt, was bis zu einer Klasse fehlt
    const einstieg = el('select', { class: 'lw-einstieg', 'aria-label': 'Bereit für Klasse …?', onchange: (ev) => { zst.einstieg = Number(ev.target.value) || null; zeichneAlles(); } },
      el('option', { value: '' }, 'Bereit für Klasse …?'), ...[6, 7, 8, 9, 10].map((k) => el('option', { value: String(k), selected: zst.einstieg === k ? true : null }, sa === 'ib_myp' ? `Bereit für MYP-Jahr ${k - 5}?` : `Bereit für Kl. ${k}?`)));
    const m = modus();
    const auswahlKnopf = el('button', { type: 'button', class: 'lw-ik', 'aria-pressed': String(!!zst.auswahl), onclick: () => { zst.auswahl = zst.auswahl ? null : new Set(); zst.filterAuf = false; zeichneAlles(); } }, zst.auswahl ? 'Auswahl beenden' : 'Auswählen');
    const gruppen = [
      // LW-3b: „Lehrplan von:“ statt „Einordnen“, mit ⓘ
      el('span', { class: 'lw-lbl' }, 'Lehrplan von:'),
      seg('Lehrplan von', Object.entries(LERN_MX_SA).map(([s2, [nm]]) => [s2, nm]), () => sa, (w) => { sa = w; zst.einstieg = null; }),
      el('button', { type: 'button', class: 'lw-hilfe', 'aria-label': 'Was heißt „Lehrplan von“?', title: LERN_LW_SA_HILFE, 'aria-expanded': String(!!zst.saHilfe), onclick: () => { zst.saHilfe = !zst.saHilfe; zeichneLeiste(); } }, 'ⓘ'),
      zst.saHilfe ? el('p', { class: 'lw-sa-hilfe lw-schwebt', role: 'note' }, LERN_LW_SA_HILFE) : null, // S1: schwebendes Feld (Matrix springt nicht)
      el('span', { class: 'lw-lbl' }, 'Zeigen'),
      seg('Zeigen', [['alle', 'Alle Themen'], ['raus', `Noch nicht im Plan · ${z.raus}`], ['drin', `Im Plan · ${z.drin}`]], () => zst.zeigen, (w) => { zst.zeigen = w; }),
      el('span', { class: 'lw-lbl' }, 'Klassen'),
      el('div', { class: 'lw-kseg', role: 'group', 'aria-label': 'Klassen' }, ...LERN_MX_KL.map((k) => el('button', { type: 'button', 'aria-pressed': String(klassen.has(k)), style: `--f:${farbe(k)}`,
        'aria-label': `Klasse ${k}${imFp.has(k) ? ' (enthält Themen aus dem Fahrplan)' : ''}`,
        onclick: () => { if (klassen.has(k)) { if (klassen.size > 1) klassen.delete(k); } else klassen.add(k); klMerken(); zeichneAlles(); } }, String(k), imFp.has(k) ? el('i', { 'aria-hidden': 'true' }) : null))),
    ];
    // LW-3b: zwei Zeilen – oben Lehrplan von · Zeigen · Klassen, darunter Einstieg · Suche · Auswählen · Farben · Stand · Rückgängig (keine eigene Legendenzeile mehr)
    // LZ-App S1: fest zweizeilig – Zeile 1 Lehrplan von · Zeigen · Klassen; Zeile 2 Bereit für … · Suchen · Auswählen · ⓘ Farben · rechts ↶ Rückgängig
    if (m === 'rechner') {
      const farben = el('button', { type: 'button', class: 'lw-ik lw-leg-knopf', 'aria-expanded': String(!!zst.legende), onclick: () => { zst.legende = !zst.legende; zeichneLeiste(); } }, 'ⓘ Farben');
      legende.hidden = !zst.legende; legende.classList.add('lw-schwebt');
      lernErsetze(leiste, el('div', { class: 'lw-zeile1' }, ...gruppen),
        el('div', { class: 'lw-zeile2' }, einstieg, suche, auswahlKnopf, el('span', { class: 'lw-leg-ort' }, farben, legende), el('span', { class: 'lw-rechts' }, stand, rueckKnopf)));
    } else {
      legende.classList.remove('lw-schwebt'); if (legende.parentElement !== kopf2) kopf2.append(legende);
      // LW-2 S1: Tablet/Handy – eine Zeile; Einordnen, Zeigen, Klassen, Einstieg, Suchen, Auswählen im Blatt „Filter ▾“, Legende hinter ⓘ
      const aktiv = (sa !== kindSa ? 1 : 0) + (zst.zeigen !== 'alle' ? 1 : 0) + (zst.einstieg ? 1 : 0) + (zst.q ? 1 : 0) + (zst.auswahl ? 1 : 0);
      lernErsetze(leiste,
        m === 'tablet' ? el('button', { type: 'button', class: 'lw-ik', 'aria-expanded': String(zst.fahrplanAuf), onclick: () => { zst.fahrplanAuf = !zst.fahrplanAuf; zeichneAlles(); } }, `Fahrplan · ${sichtbar.length}`) : umschalter,
        el('button', { type: 'button', class: 'lw-ik lw-filter-knopf', 'aria-expanded': String(!!zst.filterAuf), 'aria-controls': 'lw-filterblatt', onclick: () => { zst.filterAuf = !zst.filterAuf; zeichneLeiste(); } }, aktiv ? `Filter · ${aktiv} ▾` : 'Filter ▾'),
        el('button', { type: 'button', class: 'lw-ik lw-leg-knopf', 'aria-label': 'Farben erklären', 'aria-expanded': String(!!zst.legende), onclick: () => { zst.legende = !zst.legende; legende.hidden = !zst.legende; zeichneLeiste(); } }, 'ⓘ'),
        el('span', { class: 'lw-rechts' }, stand, rueckKnopf),
        zst.filterAuf ? el('div', { class: 'lw-filterblatt', id: 'lw-filterblatt', role: 'dialog', 'aria-label': 'Filter' },
          el('div', { class: 'lw-fb-kopf' }, el('b', {}, 'Filter'), el('button', { type: 'button', class: 'lw-x', 'aria-label': 'Filter schließen', onclick: () => { zst.filterAuf = false; zeichneLeiste(); } }, '✕')),
          ...gruppen, el('span', { class: 'lw-lbl' }, 'Einstieg und Suche'), el('div', { class: 'lw-fb-zeile' }, einstieg, suche), auswahlKnopf,
          el('button', { type: 'button', class: 'primary lw-fb-fertig', onclick: () => { zst.filterAuf = false; zeichneLeiste(); } }, 'Fertig')) : null);
    }
    // Einstieg prüfen: Orientierung, keine Einstufung
    const e = einstiegListe();
    if (e) { const p2 = lernPz(e.ts.length - e.fehlt.length, e.ts.length);
      lernErsetze(hinweis, el('div', { class: 'lern-ampel ' + (p2 >= 90 ? 'gruen' : p2 >= 70 ? 'gelb' : 'rot'), role: 'status' }, el('b', {}, p2 + ' %'),
        el('span', {}, `Bereit für ${sa === 'ib_myp' ? 'MYP-Jahr ' + (zst.einstieg - 5) : 'Kl. ' + zst.einstieg}? ${e.ts.length - e.fehlt.length} von ${e.ts.length} Themen davor gekonnt. ${p2 >= 90 ? 'Bereit – kleine Lücken.' : p2 >= 70 ? 'Fast – gezielt nacharbeiten.' : 'Noch deutliche Lücken.'} Hervorgehoben: was fehlt. `,
          el('small', {}, LERN_ORIENTIERUNG)))); }
    else lernErsetze(hinweis);
    // Sammelleiste (ein Schritt, ein Rückgängig)
    sammel.hidden = !zst.auswahl; if (!zst.auswahl) return;
    const n = zst.auswahl.size;
    const tu = (wahl) => aendere(() => { [...zst.auswahl].forEach((k) => { const [b, tid] = k.split(':').map(Number); setze(b, tid, wahl); }); zst.auswahl = new Set(); }, `${n} ${n === 1 ? 'Thema' : 'Themen'} geändert`);
    const k = (wahl, text) => el('button', { type: 'button', class: 'lern-st-knopf lern-st-knopf-' + wahl, disabled: n ? null : true, onclick: () => tu(wahl) }, text);
    lernErsetze(sammel, el('b', {}, `${n} ${n === 1 ? 'Thema' : 'Themen'} ausgewählt`),
      k('lernen', 'Lernen'), kannWdh ? k('wiederholen', 'Kann er – aber wiederholen') : null, kannJeFlug ? k('komplett', 'Kann er komplett') : null,
      kannAbwaehlen ? k('aus', 'Aus dem Plan nehmen') : null, kannWdh ? k('wieder', 'Wieder in die Wiederholung') : null,
      el('button', { type: 'button', class: 'secondary', onclick: () => { zst.auswahl = null; zeichneAlles(); } }, 'Abbrechen'));
  };
  const legende = el('p', { class: 'lw-legende' }, ...[['dran', 'gerade dran'], ['plan', 'im Plan'], ['wdh', 'Wiederholung'], ['fertig', 'fertig'], ['raus', 'gewählte Schule'], ['fremd', 'nur andere Schule']]
    .map(([a, t]) => el('span', {}, el('i', { class: 'lw-leg lw-' + a }), t)), el('span', {}, el('i', { class: 'lw-leg-nr' }, '1'), 'Platz'));

  // ---------- Aufbau ----------
  const umschalter = el('div', { class: 'lw-seg lw-handy-um', role: 'group', 'aria-label': 'Ansicht' });
  const kopf2 = el('div', { class: 'lw-kopf2' }, umschalter, legende);
  const koerper = el('div', { class: 'lw-koerper' }, rail, matrixWrap, drawer);
  function zeichneAlles() {
    if (!live()) return;
    const m = modus(); koerper.dataset.modus = m;
    koerper.classList.toggle('lw-fp-auf', m === 'tablet' && zst.fahrplanAuf);
    koerper.classList.toggle('lw-waehlen', !!zst.auswahl);
    ordne(); zeichneLeiste(); zeichneRail(); zeichneMatrix(); zeichneDetail();
    lernErsetze(umschalter, ...[['fahrplan', `Fahrplan · ${sichtbar.length}`], ['alle', 'Alle Themen']].map(([w, t]) =>
      el('button', { type: 'button', 'aria-pressed': String(zst.handy === w), onclick: () => { zst.handy = w; zeichneAlles(); } }, t)));
    umschalter.hidden = m !== 'handy'; koerper.dataset.handy = zst.handy; legende.hidden = !zst.legende;
    hoehe();
  }
  const hoehe = () => { if (modus() === 'handy') { koerper.style.height = ''; return; } const top = koerper.getBoundingClientRect().top + scrollY; koerper.style.height = `${Math.max(460, innerHeight - top - 2)}px`; };
  let warModus = modus();
  const groesse = () => { if (!live()) { removeEventListener('resize', groesse); removeEventListener('keydown', taste); return; } if (modus() !== warModus) { warModus = modus(); zeichneAlles(); } else hoehe(); };
  const taste = (ev) => { if (!live()) return; if (ev.key === 'Escape' && zst.sel) { zst.sel = null; zeichneAlles(); } };
  addEventListener('resize', groesse); addEventListener('keydown', taste);
  const uKind = (u?.lernende || []).find((c) => c.id === id);
  lernErsetze(main, leiste, kopf2, hinweis, sammel, meldung, koerper, toast);
  // „Für ‹Kind› planen ›“ aus Nachschlagen → Lehrplan: Thema geöffnet
  const ziel = lernPlanZiel?.kind === id ? lernPlanZiel.thema : null; lernPlanZiel = null;
  // LW-3: Sprünge aus dem Überblick – „Fahrplan ändern“ zeigt den Fahrplan, ein Ring die Klasse
  const start = lernLwStart?.kind === id ? lernLwStart : null; lernLwStart = null;
  if (start?.fahrplan) { zst.handy = 'fahrplan'; zst.fahrplanAuf = true; }
  if (start?.klasse && LERN_MX_KL.includes(start.klasse)) { klassen.add(start.klasse); zst.offenKl.add(start.klasse); zst.scrollKl = start.klasse; }
  if (ziel && M.by.has(ziel)) { zst.sel = ziel; klassen.add(lernMxZeile(M.by.get(ziel), sa)); zst.offenKl.add(lernMxZeile(M.by.get(ziel), sa)); }
  zeichneAlles();
  // zur Klasse des Kindes (bzw. zum geöffneten Thema) scrollen
  requestAnimationFrame(() => { if (!live()) return; hoehe();
    const z = (zst.sel && matrixWrap.querySelector(`.lw-karte[data-id="${zst.sel}"]`)) || (zst.scrollKl && matrixWrap.querySelector(`[data-kl="${zst.scrollKl}"]`)) || matrixWrap.querySelector('.lw-karte.lw-dran') || matrixWrap.querySelector(`[data-kl="${kindKl}"]`);
    // S3: Höhe der klebenden Spaltenzeile abziehen – Klassen-Kopf und erste Kartenreihe ganz sichtbar
    if (z && modus() !== 'handy') { const w = matrixWrap.getBoundingClientRect(), r = (z.closest('[data-kl]') && !z.matches('[data-kl]') ? z : z).getBoundingClientRect();
      const gh = matrixWrap.querySelector('.lw-gh')?.getBoundingClientRect().height || 0; matrixWrap.scrollTop += r.top - w.top - gh - 8; } });
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
  const aufgaben = (d.aufgaben || []).filter((a) => a.pool !== 'expedition'); // W176: Expeditions-Teile stehen unter „Expeditionen“, nicht bei der Etappe ihres Bezugs
  const etappen = lernEtappen({ inhalt: d.inhalt, uebungen: aufgaben.filter((a) => a.pool === 'uebung') });
  // Teil 4: In einem fertigen Flug sind Bordkarten mit freigegeben = false aussortiert (ersetzt oder überzählig) und werden nie wieder ausgegeben;
  // „in Prüfung“ gilt nur, solange der ganze Flug noch Entwurf ist.
  const fertigFlug = ['geprueft', 'freigegeben'].includes(d.status);
  const aussortiert = (a) => fertigFlug && !a.freigegeben;
  const statusWort = (a) => a.freigegeben ? el('span', { class: 'lp-ok' }, 'frei ✓') : fertigFlug ? el('span', { class: 'lp-aus' }, 'aussortiert') : el('span', { class: 'lp-warte' }, 'in Prüfung');
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
      el('td', {}, lernMathe(a.frage?.text || a.frage?.schablone || ''), a.antworttyp === 'auswahl' ? el('small', { class: 'muted' }, ' (' + (a.antworten || []).join(' | ') + ')') : null),
      el('td', { class: 'lp-loesung' }, lernMathe(lernLoesungText(a))),
      el('td', { class: 'muted' }, lernMathe(a.loesungsweg || '')),
      el('td', {}, statusWort(a)))))));
  const karten = etappen.map((e) => {
    const alle = aufgaben.filter((a) => a.lernziel === e.lernziel);
    const as = alle.filter((a) => !aussortiert(a)); const weg = alle.filter(aussortiert);
    const rm = rmJe(e.lernziel);
    return el('details', { class: 'card lp-karte', id: 'k' + e.nr },
      el('summary', {}, el('b', {}, `${e.nr} · ${e.titel}`), el('small', { class: 'muted' }, ` · ${as.length} ${as.length === 1 ? 'Bordkarte' : 'Bordkarten'}${as.some((a) => !a.freigegeben) ? ` (${as.filter((a) => !a.freigegeben).length} in Prüfung)` : ''}${rm.length ? ` · ${rm.length} ${rm.length === 1 ? 'Anmerkung' : 'Anmerkungen'}` : ''}`)),
      el('div', { class: 'lp-karte-innen' },
        el('div', { class: 'lp-erkl' }, el('p', { class: 'eyebrow' }, 'ERKLÄRUNG, WIE DAS KIND SIE SIEHT'), e.regel ? lernErklaerung(e) : el('p', { class: 'muted' }, 'Keine Erklärung hinterlegt.')),
        lernAendern({ einheit_id: id, lernziel: e.lernziel }, { bezug: 'etappe', wo: `Etappe „${e.titel}“` }),
        ...rm.map((r) => el('p', { class: 'small' }, el('b', {}, (LERN_RM_STATUS[r.status] || r.status) + ': '), r.text, r.antwort ? el('span', { class: 'muted' }, ' → ' + r.antwort) : null)),
        as.length ? tabelle(as) : el('p', { class: 'muted small' }, 'Keine Bordkarten.'),
        weg.length ? el('details', { class: 'lp-aussortiert' }, el('summary', {}, `${weg.length} aussortierte ${weg.length === 1 ? 'Bordkarte' : 'Bordkarten'} (ersetzt oder überzählig) anzeigen`), tabelle(weg)) : null));
  });
  const ohneKarte = aufgaben.filter((a) => !etappen.some((e) => e.lernziel === a.lernziel));
  const zahl = (fn) => aufgaben.filter(fn).length;
  lernErsetze(main, ...[
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, [d.ort?.stadt, lernJahrgangText(d.thema?.jahrgang)].filter(Boolean).join(' · ').toUpperCase() || 'INHALTE'),
      el('h2', {}, titel),
      el('p', {}, `${fertigFlug ? 'Fertig' : 'In Prüfung'} · ${etappen.length} Etappen · ${zahl((a) => a.pool === 'uebung' && !aussortiert(a))} ${zahl((a) => a.pool === 'uebung' && !aussortiert(a)) === 1 ? 'Bordkarte' : 'Bordkarten'} zum Üben · ${zahl((a) => a.pool !== 'uebung' && !aussortiert(a))} für Test und Nachtest`
        + (fertigFlug ? (zahl(aussortiert) ? ` · ${zahl(aussortiert)} aussortiert (ersetzt oder überzählig, werden nicht mehr ausgegeben)` : '')
          : (zahl((a) => !a.freigegeben) ? ` · ${zahl((a) => !a.freigegeben)} noch in Prüfung (nur für das Testkind sichtbar)` : ''))),
      d.inhalt?.ziel ? el('p', { class: 'small muted' }, 'Ziel: ' + d.inhalt.ziel) : null),
    el('nav', { class: 'lp-sprung', 'aria-label': 'Etappen' }, ...etappen.map((e) => el('a', { href: '#', class: 'lern-chip', onclick: (ev) => {
      ev.preventDefault(); const k = document.getElementById('k' + e.nr); k.open = true; k.scrollIntoView({ block: 'start' });
    } }, `${e.nr} · ${e.titel}`))),
    lernAendern({ einheit_id: id }, { bezug: 'flug', wo: `Flug „${titel}“` }),
    ...karten,
    ohneKarte.length ? el('details', { class: 'card lp-karte' }, el('summary', {}, el('b', {}, `Bordkarten für Test und Nachtest ohne Etappe (${ohneKarte.length})`)), tabelle(ohneKarte)) : null].filter(Boolean));
}

// ---------- Eltern/Lehrer: „Was wackelt?“ – Lernstand je Lernkarte mit den echten falschen Antworten ----------
// LA-3: Reiter „Was wackelt“ – eine Tabelle über alle Etappen mit Fehlern (wackelt zuerst, dann nach Datum); Zeile antippen klappt auf:
// die letzten 3 falschen Antworten, „Kurz gesagt“, „Erklärung ansehen ›“, „Besprochen ✓“. arg: <kind>[-<einheit>.<etappe>] (aufgeklappt).
const LERN_FEHLERART = { vorzeichen: 'Vorzeichen', komma: 'Komma verrutscht', vertauscht: 'vertauscht', gerundet: 'falsch gerundet', falsche_einheit: 'falsche Einheit' };
// häufigster Fehler nur, wo ein grund bei mindestens zwei falschen Antworten vorkommt (Abweichung 5) – sonst „–“
function lernHaeufigsterFehler(k) {
  const g = Object.entries(k.fehler_gruende || {}).sort((a, b) => b[1] - a[1])[0];
  return g && g[1] >= 2 ? `${LERN_FEHLERART[g[0]] || g[0]} (${g[1]}×)` : '–';
}
// LW-3 (1a): „Was wackelt“ als Arbeitsliste. Einträge je Thema (oder je Etappe mit eigenem Status) vom Server, sortiert; Status speichern über
// schule_wackelt_setzen. Neue endgültig falsche Antworten holen einen Eintrag zurück nach „Zu besprechen“ – das rechnet der Server beim Lesen.
const LERN_WK_GRUPPEN = [['zu_besprechen', 'ZU BESPRECHEN'], ['beobachten', 'BEOBACHTEN'], ['besprochen', 'BESPROCHEN']];
function lernWackeltListe(kindId, wk, alleKarten, antwortZeile) {
  let eintraege = (wk.eintraege || []).slice(); let zahl = Number(wk.zu_besprechen) || 0;
  const offen = new Set(); const box = el('div', { class: 'wk-liste' });
  const toast = el('div', { class: 'lw-toast', role: 'status', hidden: true }); let uhr = null;
  const schl = (e) => `${e.thema_id}:${e.einheit_id || ''}:${e.lernziel || ''}`;
  const wann = (iso) => { if (!iso) return null; const d = new Date(iso); if (isNaN(d)) return null; d.setHours(0, 0, 0, 0); const h = new Date(); h.setHours(0, 0, 0, 0);
    const t = Math.round((h - d) / 864e5); return t <= 0 ? 'heute' : t === 1 ? 'gestern' : `vor ${t} Tagen`; }; // Ortszeit, nicht UTC-Datum
  const karten = (e) => { const et = e.etappen?.length ? e.etappen : e.etappe ? [e.etappe] : [];
    return et.map((x) => ({ et: x, k: alleKarten.find((k) => k.einheit_id === x.einheit_id && k.lernziel === x.lernziel) })); };
  const setzen = async (e, status, zurueck = false) => {
    const vorher = e.status;
    try {
      const r = await lernCall('schule_wackelt_setzen', { lernender_id: kindId, thema_id: e.thema_id, status, ...(e.einheit_id ? { einheit_id: e.einheit_id, lernziel: e.lernziel } : {}) });
      const neu = r?.eintrag ? { ...e, ...r.eintrag } : { ...e, status, quelle: 'gespeichert', wieder_offen: false, fehler_neu: 0 };
      eintraege = eintraege.map((x) => (schl(x) === schl(e) ? neu : x));
      zahl = typeof r?.zu_besprechen === 'number' ? r.zu_besprechen : eintraege.filter((x) => x.status === 'zu_besprechen').length;
      lernWackeltZahl = { kind: kindId, n: zahl }; lernZbSetzen(zahl); zeichne();
      if (!zurueck) { clearTimeout(uhr); toast.hidden = false;
        lernErsetze(toast, el('span', {}, `„${e.titel}“: ${{ zu_besprechen: 'zu besprechen', beobachten: 'beobachten', besprochen: 'besprochen' }[status]}`),
          el('button', { type: 'button', onclick: () => { toast.hidden = true; setzen(neu, vorher, true); } }, '↶ Rückgängig'));
        uhr = setTimeout(() => { toast.hidden = true; }, 5000); }
    } catch (err) { clearTimeout(uhr); toast.hidden = false; lernErsetze(toast, el('span', {}, `Nicht gespeichert: ${err.message}`)); uhr = setTimeout(() => { toast.hidden = true; }, 6000); }
  };
  const eintrag = (e) => {
    const auf = offen.has(schl(e)); const et = e.etappe || e.etappen?.[0] || null; const n = Number(e.fehler) || 0;
    const knopf = (status, text) => el('button', { type: 'button', class: 'secondary wk-knopf', 'aria-label': `${e.titel}: ${text}`, onclick: () => setzen(e, status) }, text);
    return el('section', { class: `wk-eintrag wk-${e.status}`, 'data-thema': String(e.thema_id) },
      el('div', { class: 'wk-kopf' },
        el('div', { class: 'wk-text' }, el('b', {}, e.titel),
          e.wieder_offen ? el('span', { class: 'ls-marke ls-marke-w' }, Number(e.fehler_neu) ? `wieder offen · ${e.fehler_neu} neu` : 'wieder offen') : null,
          el('small', {}, [et ? `Etappe: ${et.titel || lernZielName(et.lernziel)}` : 'ganzes Thema', `${n} ${n === 1 ? 'Fehler' : 'Fehler'}`, wann(e.letzter_fehler_am)].filter(Boolean).join(' · '))),
        el('div', { class: 'wk-knoepfe' },
          e.status !== 'besprochen' ? knopf('besprochen', '✓ Besprochen') : null,
          e.status === 'zu_besprechen' || e.status === 'besprochen' ? knopf('beobachten', 'Beobachten') : null,
          e.status === 'beobachten' ? knopf('zu_besprechen', 'Zu besprechen') : null,
          el('a', { class: 'btn secondary wk-knopf', 'aria-label': 'Im Lehrplan', href: `#/kind/${kindId}-lehrplan`, onclick: () => { lernPlanZiel = { kind: kindId, thema: e.thema_id }; } }, el('span', { class: 'wk-lang' }, 'Im Lehrplan'), el('span', { class: 'wk-kurz', 'aria-hidden': 'true' }, '→ Lehrplan')))),
      el('button', { type: 'button', class: 'wk-auf', 'aria-expanded': String(auf), onclick: () => { if (auf) offen.delete(schl(e)); else offen.add(schl(e)); zeichne(); } },
        auf ? 'Bordkarte und Antwort ▾' : 'Bordkarte und Antwort ▸'),
      auf ? el('div', { class: 'wk-detail' }, ...karten(e).map(({ et: x, k }) => el('div', {}, el('b', { class: 'small' }, `${x.titel || lernZielName(x.lernziel)} · ${x.fehler || 0} Fehler`),
        (k?.fehler || []).length ? el('ul', { class: 'ls-antworten' }, ...k.fehler.slice(0, 3).map(antwortZeile)) : el('p', { class: 'small muted' }, 'Keine falschen Antworten gespeichert.'),
        k?.regel ? el('p', { class: 'ls-kurz' }, el('b', {}, 'Kurz gesagt: '), lernMathe(k.regel)) : null,
        x.einheit_id ? el('a', { class: 'small', href: `#/inhalte/${x.einheit_id}` }, 'Erklärung ansehen ›') : null))) : null);
  };
  function zeichne() {
    lernErsetze(box, ...LERN_WK_GRUPPEN.map(([st, titel]) => { const l = eintraege.filter((e) => e.status === st);
      return el('section', { class: `wk-gruppe wk-gruppe-${st}`, 'aria-label': titel },
        el('h3', { class: 'wk-gh' }, `${titel} · ${l.length}`),
        l.length ? el('div', { class: 'wk-eintraege' }, ...l.map(eintrag)) : el('p', { class: 'small muted' }, st === 'zu_besprechen' ? 'Nichts zu besprechen.' : '–')); }),
      eintraege.length ? null : el('p', { class: 'muted' }, 'Im Moment nichts: Kein Thema hat falsche Antworten.'), toast);
  }
  zeichne();
  return el('section', { class: 'card wk-karte', 'aria-label': 'Was wackelt' }, box, // S2: keine zweite Überschrift (steht am Reiter)
    el('p', { class: 'small muted' }, 'Neue Fehler im selben Thema (bzw. in der Etappe) holen einen Eintrag von selbst zurück nach „Zu besprechen“. Die Zahl am Reiter zählt „Zu besprechen“.'));
}
async function viewWackelt(arg) {
  setChrome('Was wackelt?', { back: true, showTabs: false });
  const live = viewGuard();
  const [idRoh, aufRoh] = String(arg || '').split('-');
  const kindId = Number(idRoh);
  if (!kindId) { route('lernen'); return; }
  lernLaden();
  const [d, wk] = await Promise.all([lernCall('schule_lernstand', { lernender_id: kindId }), lernWackeltLesen(kindId)]);
  if (!live()) return;
  lernWackeltZahl = wk ? { kind: kindId, n: Number(wk.zu_besprechen) || 0 } : null; if (lernWackeltZahl) lernZbSetzen(lernWackeltZahl.n);
  $('#title').textContent = 'Was wackelt? · ' + d.kind.name;
  const zustand = (k) => k.faellig ? ['wiederholen', 'wdh'] : k.sicher ? ['sicher', 'ok'] : k.sitzt ? [k.eigene_loesungen !== undefined ? 'gelandet' : 'sitzt', 'ok']
    : k.wieder_offen ? ['wieder offen', 'wackelt'] // H1: zwei Fehler in der Wiederholung – es fehlen 3 eigene Lösungen in Folge
    : k.falsch >= 3 && k.falsch > k.richtig ? ['wackelt', 'wackelt'] : k.richtig + k.falsch ? ['am Üben', 'ueben'] : ['noch nicht geübt', 'neu'];
  const karte = (k) => {
    const [text, kl] = zustand(k);
    return el('li', { class: 'ls-karte ls-' + kl },
      el('div', { class: 'ls-kopf' }, el('b', {}, k.titel), el('span', { class: 'ls-zustand' }, text)),
      k.richtig + k.falsch ? el('small', { class: 'muted' }, `${k.richtig} richtig · ${k.falsch} falsch` + (k.mit_tipp ? ` · ${k.mit_tipp}-mal Tipp` : '') + (k.zuletzt ? ` · zuletzt ${lernTag(k.zuletzt)}` : '')) : null,
      k.sitzt && k.bis_sitzt ? el('small', { class: 'muted ls-bis-sitzt' }, `${k.eigene_loesungen !== undefined ? 'gelandet' : 'sitzt'} nach ${k.bis_sitzt} ${k.bis_sitzt === 1 ? 'Bordkarte' : 'Bordkarten'}`) : null,
      k.misch_ok ? el('small', { class: 'muted ls-misch' }, 'in einer Mischkarte erkannt ✓') : null, // W176 Teil 3
      k.sitzt && !k.sicher && k.flug_nachtest ? el('small', { class: 'muted ls-flugnachtest' }, 'Flug-Nachtest bestanden') : null, // H4: nicht dasselbe wie „sicher“
      k.wieder_offen ? el('small', { class: 'muted ls-wiederoffen' }, 'War schon gelandet; in der Wiederholung zweimal falsch – wieder offen, bis 3 eigene Lösungen in Folge gelingen.') : null, // H1
      !k.sitzt && k.eigene_loesungen !== undefined && k.richtig + k.falsch ? el('small', { class: 'muted ls-regel' }, `${k.eigene_loesungen} eigene Lösungen · ${k.folge || 0} in Folge · ${k.typen_anzahl || 0} ${k.typen_anzahl === 1 ? 'Art' : 'Arten'} von Bordkarten`) : null, // W176
      k.knobel_gesamt ? el('small', { class: 'muted ls-knobel' }, `Knobel: ${k.knobel_geloest || 0} von ${k.knobel_gesamt}`) : null); // F
  };
  const antwortZeile = (f) => { const a = { antworttyp: f.antworttyp, antworten: f.antworten, loesung: f.loesung, frage: { text: f.frage, schablone: f.schablone, grafik: f.grafik } };
    return el('li', { class: 'small' }, el('span', {}, lernMathe(f.frage || '')), el('br'), el('span', { class: 'ls-falsch' }, 'Antwort: ', lernMathe(lernAntwortText(a, f.antwort || {}) || '–')),
      ' · ', el('span', { class: 'ls-richtig' }, 'richtig: ', lernMathe(lernLoesungText(a)))); };
  const alle = (d.einheiten || []).flatMap((e) => (e.karten || []).map((k) => ({ ...k, einheit_id: e.einheit_id, ort: lernFlugName(kindId, { einheit_id: e.einheit_id, lernziel: k.lernziel }, e.ort), thema: e.titel })));
  const seit = (k) => (k.fehler || []).map((f) => f.am).filter(Boolean).sort()[0] || k.zuletzt || null; // älteste der letzten falschen Antworten
  const mitFehlern = alle.filter((k) => k.falsch > 0).sort((a, b) => (lernKarteWackelt(b) - lernKarteWackelt(a)) || String(seit(b) || '').localeCompare(String(seit(a) || '')));
  const schluessel = (k) => `${k.einheit_id}.${k.lernziel}`;
  const offen = new Set(aufRoh ? [aufRoh] : []);
  const tbody = el('tbody');
  const karten = el('div', { class: 'ls-karten' }); // I-1: unter 560 px je Etappe eine Karte statt Tabelle
  const umschalten = (k) => { if (offen.has(schluessel(k))) offen.delete(schluessel(k)); else offen.add(schluessel(k)); zeichne(); };
  const marken = (k, w) => [w ? el('span', { class: 'ls-marke ls-marke-w' }, k.wieder_offen ? 'wieder offen' : 'wackelt') : null,
    k.besprochen_am ? el('span', { class: 'ls-marke ls-marke-b' }, 'besprochen ' + lernTag(k.besprochen_am)) : null];
  const detail = (k) => {
    const meldung = el('span', { class: 'small muted', role: 'status', 'aria-live': 'polite' });
    const besprochen = el('button', { type: 'button', class: 'secondary ls-besprochen', onclick: async (ev) => {
      ev.stopPropagation(); besprochen.disabled = true; meldung.textContent = 'Speichere …';
      try { const r = await lernCall('schule_notiz_setzen', { lernender_id: kindId, besprochen: { einheit_id: k.einheit_id, lernziel: k.lernziel } });
        k.besprochen_am = r?.besprochen_am || new Date().toISOString(); zeichne(); }
      catch (err) { besprochen.disabled = false; meldung.textContent = /Notiz leer/.test(err.message) ? '„Besprochen“ lässt sich hier noch nicht speichern.' : 'Nicht gespeichert: ' + err.message; } } },
      k.besprochen_am ? 'Erneut besprochen ✓' : 'Besprochen ✓');
    return [(k.fehler || []).length ? el('div', {}, el('b', { class: 'small' }, `Letzte falsche Antworten (${k.fehler.length})`), el('ul', { class: 'ls-antworten' }, ...k.fehler.slice(0, 3).map(antwortZeile)))
        : el('p', { class: 'small muted' }, 'Keine falschen Antworten gespeichert.'),
      k.regel ? el('p', { class: 'ls-kurz' }, el('b', {}, 'Kurz gesagt: '), lernMathe(k.regel)) : null,
      el('div', { class: 'row' }, el('a', { class: 'small', href: `#/inhalte/${k.einheit_id}` }, 'Erklärung ansehen ›'), besprochen, meldung)];
  };
  const zeichne = () => {
    lernErsetze(tbody, ...mitFehlern.flatMap((k) => {
      const auf = offen.has(schluessel(k)); const w = lernKarteWackelt(k);
      const zeile = el('tr', { class: 'ls-zeile' + (w ? ' ls-zeile-wackelt' : '') + (auf ? ' offen' : ''), onclick: () => umschalten(k) },
        el('th', { scope: 'row' }, el('button', { type: 'button', class: 'ls-auf', 'aria-expanded': String(auf) }, el('b', {}, k.titel)), el('small', {}, k.ort || k.thema), ...marken(k, w)),
        el('td', {}, `${k.richtig} / ${k.falsch}`),
        el('td', {}, lernHaeufigsterFehler(k)),
        el('td', {}, seit(k) ? lernTag(seit(k)) : '–'));
      return auf ? [zeile, el('tr', { class: 'ls-detail' }, el('td', { colspan: '4' }, ...detail(k)))] : [zeile];
    }));
    lernErsetze(karten, ...mitFehlern.map((k) => {
      const auf = offen.has(schluessel(k)); const w = lernKarteWackelt(k);
      return el('section', { class: 'card ls-karte-m' + (w ? ' ls-zeile-wackelt' : '') },
        el('button', { type: 'button', class: 'ls-auf ls-karte-kopf', 'aria-expanded': String(auf), onclick: () => umschalten(k) },
          el('b', {}, k.titel), el('small', {}, k.ort || k.thema)),
        el('div', { class: 'ls-karte-marken' }, ...marken(k, w)),
        el('p', { class: 'small ls-karte-werte' }, el('span', {}, `richtig / falsch: ${k.richtig} / ${k.falsch}`), el('span', {}, `häufigster Fehler: ${lernHaeufigsterFehler(k)}`),
          el('span', {}, `seit: ${seit(k) ? lernTag(seit(k)) : '–'}`)),
        auf ? el('div', { class: 'ls-karte-detail' }, ...detail(k)) : null);
    }));
  };
  zeichne();
  const w = d.woche || {}; const tageWoche = (d.lerntage || []).filter((x) => lernTageSeit(x) < 7).length;
  const proEinheit = (d.einheiten || []).map((e) => el('section', { class: 'card' },
    el('div', { class: 'lern-einheit-kopf' }, el('h3', {}, `${lernFlugName(kindId, { einheit_id: e.einheit_id }, e.ort || '') ? lernFlugName(kindId, { einheit_id: e.einheit_id }, e.ort || '') + ': ' : ''}${e.titel}`), el('a', { class: 'small', href: `#/inhalte/${e.einheit_id}` }, 'Inhalte ansehen')),
    el('p', { class: 'small muted' }, `${(e.karten || []).filter((k) => k.sitzt).length} von ${(e.karten || []).length} Etappen sitzen` + (e.zuletzt ? ` · zuletzt ${lernTag(e.zuletzt)}` : '')),
    el('ul', { class: 'ls-liste' }, ...(e.karten || []).map(karte))));
  // ---------- LW-3: Arbeitsliste Zu besprechen · Beobachten · Besprochen (schule_wackelt_lesen / _setzen) ----------
  const liste = wk ? lernWackeltListe(kindId, wk, alle, antwortZeile) : null;
  const woche = el('p', { class: 'ls-woche' }, `Diese Woche: ${w.aufgaben || 0} `, lernErklaert('Bordkarten', 'bordkarte'), `, ${w.richtig || 0} richtig` + (w.mit_tipp ? `, ${w.mit_tipp}-mal mit Tipp` : '') + ` · ${tageWoche} ${tageWoche === 1 ? 'Lerntag' : 'Lerntage'}`);
  const tabelle = el('section', { class: 'card ls-wackelt' }, el('h3', {}, liste ? 'Je Etappe' : 'Was wackelt?'),
      mitFehlern.length ? el('div', { class: 'lern-tabelle-rollen ls-breit' }, el('table', { class: 'ls-tabelle' },
        el('thead', {}, el('tr', {}, el('th', {}, 'Etappe ', el('small', { class: 'lern-wort-erkl' }, '(Lernschritt)')), el('th', {}, 'richtig / falsch'), el('th', {}, 'häufigster Fehler'), el('th', {}, 'seit'))), tbody))
        : el('p', { class: 'muted' }, 'Im Moment nichts: Keine Etappe hat falsche Antworten.'),
      mitFehlern.length ? karten : null,
      el('p', { class: 'small muted' }, '„Wackelt“: mindestens 3 falsche und mehr falsche als richtige Antworten. Ein Gespräch über genau diese eine Regel hilft meist mehr als weitere Bordkarten. „Besprochen ✓“ nimmt die Etappe aus „Zu tun“, bis wieder eine Antwort falsch ist.'));
  const alleEtappen = proEinheit.length ? el('details', { class: 'ls-alle' }, el('summary', {}, `Alle Etappen mit Stand (${alle.length})`), ...proEinheit) : el('p', { class: 'card muted' }, 'Noch nichts gelernt.');
  // Mit Arbeitsliste: die Tabelle je Etappe (mit „Besprochen ✓“ je Etappe, LA-3) steht zugeklappt darunter
  lernErsetze(main, liste ? null : woche, liste, // S2: „Diese Woche …“ steht im Überblick
    liste ? el('details', { class: 'ls-je-etappe' }, el('summary', {}, `Je Etappe: richtig / falsch, häufigster Fehler (${mitFehlern.length})`), tabelle) : tabelle,
    alleEtappen);
}

// ---------- LM-6 (0.86.0): Kinderseite „Meine Route 5–10“ – die Lehrplan-Matrix für das eigene Kind, in Reisewörtern ----------
// Nur dieses Kind, Lernstand immer an, Schulart fest; keine Schulart-Kennzeichen, keine Pflicht-Zählung, kein Lehrplan-Wortlaut, nichts zum Ändern.
// Daten: schule_lehrplan_matrix (Lern-Zugang: Kindsicht mit zeile/reihenfolge_kind; Eltern sehen die Seite des Kindes mit der Lehrer-Sicht – dann rechnet die App
// die Zeile aus jahrgang und der Schulart des Kindes) und beim Antippen schule_lehrplan_thema. Ohne LM-S: ein ehrlicher Hinweis.
const LERN_RT_TEXT = { komplett: '◉ kannst du', wiederholung: '↻ kommt zur Wiederholung', kommt: '○ kommt noch' };
const lernRtStand = (s, n) => (!s || !s.stufe || s.stufe === 'nicht_im_plan' ? '' : s.stufe === 'dran'
  ? `▶ hier bist du${n ? ` – Etappe ${s.etappe_jetzt || Math.min((s.gelandet || 0) + 1, n)} von ${n}` : ''}` : LERN_RT_TEXT[s.stufe] || '');
async function viewRoute(arg) {
  setChrome('Meine Route', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const { kind } = d;
  let m = null;
  try { m = await lernCall('schule_lehrplan_matrix', { lernender_id: kind.id, mit_testkind: true }); } catch { m = null; }
  if (!live()) return;
  if (!Array.isArray(m?.themen)) {
    lernErsetze(main, lernRahmen(kind, 'reise', lernKopf('MEINE ROUTE 5–10', 'Deine Route durch die Mathe-Welt'),
      el('section', { class: 'lr-karte-box' }, el('p', { class: 'lr-leise' }, 'Die Route ist bald da.'), el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Zur Abflugtafel'))));
    return;
  }
  const ich = (m.kinder || []).find((c) => c.id === kind.id) || {};
  const sa = ich.schulart || kind.schulart || 'gym_by';
  const geb = new Map((m.gebiete || []).map((g) => [g.gebiet_id, g]));
  const stand = m.lernstand?.[kind.id] || {};
  const ortVon = new Map((d.orte || []).map((o) => [o.block_id, o.stadt]));
  const fluege = m.themen.map((t) => {
    const zeile = t.zeile || (t.jahrgang ? (() => { const x = { jg: t.jahrgang, gebiet: geb.get(t.gebiet_id)?.titel }; const k = lernMxKl(x, sa); return k ? { klasse: k } : { klasse: lernMxZusatz(x, sa).k, eingeordnet: true }; })() : {});
    return { id: t.thema_id, titel: t.titel, kont: geb.get(t.gebiet_id)?.titel || t.gebiet || 'Weitere', kr: geb.get(t.gebiet_id)?.reihenfolge ?? 99, block: t.block_id, einheit: t.einheit_id || null,
      ohne: t.ohne_flug === true, n: t.etappen_anzahl || 0, kl: Math.min(10, Math.max(5, Number(zeile.klasse) || 10)), eingeordnet: !!zeile.eingeordnet,
      r: Number(t.reihenfolge_kind ?? t.lehrplan_reihenfolge?.[sa]) || 999, s: stand[t.thema_id] || { stufe: 'nicht_im_plan' }, ort: ortVon.get(t.block_id) || null };
  });
  const by = new Map(fluege.map((f) => [f.id, f]));
  const vor = new Map(), nach = new Map();
  for (const v of m.verbindungen || []) { const [a, b, art] = Array.isArray(v) ? v : [v.thema_id, v.braucht_id, v.art]; if (!by.has(a) || !by.has(b)) continue;
    vor.set(a, [...(vor.get(a) || []), { id: b, art }]); nach.set(b, [...(nach.get(b) || []), { id: a, art }]); }
  const konts = [...new Set(fluege.slice().sort((a, b) => a.kr - b.kr).map((f) => f.kont))];
  const imFeld = (k, g) => fluege.filter((f) => f.kl === k && f.kont === g).sort((a, b) => (a.eingeordnet ? 1 : 0) - (b.eingeordnet ? 1 : 0) || a.r - b.r || a.titel.localeCompare(b.titel));
  const kl = (s) => LERN_STUFE[s.stufe]?.kl || 'st-5';
  let sel = null; let svg = null; const details = new Map(); let merk = null;
  const ansicht = el('div', { class: 'rt-ansicht' });
  const detail = el('section', { class: 'rt-detail lr-karte-box', 'aria-live': 'polite', 'aria-label': 'Flug im Detail' });
  const handy = () => innerWidth < 1000; // Handy und Tablet: Liste je Klasse (Vorgabe „Handy/Tablet zuerst“); die Matrix erst ab 1000 px
  const chip = (f) => el('button', { type: 'button', class: `mx-chip rt-chip mx-st ${kl(f.s)}` + (f.s.stufe === 'dran' ? ' mx-dran' : '') + (f.s.stufe === 'nicht_im_plan' || f.ohne ? ' rt-blass' : '') + rolle(f),
    style: `--f:${LERN_KL_FARBE[f.kl] || '#888'}`, 'data-id': String(f.id), 'aria-expanded': String(sel === f.id), onclick: () => { sel = sel === f.id ? null : f.id; zeichne(); if (sel && !handy()) detail.scrollIntoView({ block: 'nearest' }); } },
    (nach.get(f.id) || []).length >= 2 ? el('span', { class: 'mx-n', title: `Darauf bauen ${(nach.get(f.id) || []).length} Flüge auf` }, `→ ${(nach.get(f.id) || []).length}`) : null,
    el('span', { class: 'mx-titel' }, f.titel), f.ort ? el('span', { class: 'rt-ort' }, f.ort) : null,
    lernRtStand(f.s, f.n) ? el('span', { class: 'mx-stand' }, lernRtStand(f.s, f.n)) : null);
  const weg = (id) => { const s = new Set(); const st = [id]; while (st.length) { const v = st.pop(); (vor.get(v) || []).forEach((e) => { if (!s.has(e.id)) { s.add(e.id); st.push(e.id); } }); } return s; };
  let WEG = new Set();
  function rolle(f) { if (!sel) return ''; if (f.id === sel) return ' mx-sel'; if ((vor.get(sel) || []).some((e) => e.id === f.id)) return ' mx-vor'; if ((nach.get(sel) || []).some((e) => e.id === f.id)) return ' mx-nach'; return WEG.has(f.id) ? ' mx-weg2' : ''; }
  const kopf = (k) => { const l = fluege.filter((f) => f.kl === k && !f.eingeordnet && !f.ohne); const z = { komplett: 0, wiederholung: 0, dran: 0 }; l.forEach((f) => { if (f.s.stufe in z) z[f.s.stufe]++; });
    const pz = (v) => (l.length ? (v / l.length) * 100 : 0);
    return [el('div', { class: 'mx-balken', role: 'img', 'aria-label': `${z.komplett} kannst du, ${z.wiederholung} in Wiederholung, ${z.dran} gerade dran von ${l.length}` },
      el('span', {}, el('i', { class: 'st-1', style: `width:${pz(z.komplett)}%` }), el('i', { class: 'st-2', style: `width:${pz(z.wiederholung)}%` }), el('i', { class: 'st-3', style: `width:${pz(z.dran)}%` }))),
      el('small', { class: 'rt-kann' }, `Du kannst schon ${z.komplett} von ${l.length} ${l.length === 1 ? 'Flug' : 'Flügen'}`)]; };
  const zeichneMatrix = () => {
    WEG = sel ? weg(sel) : new Set(); svg = null;
    if (handy()) {
      lernErsetze(ansicht, el('div', { class: 'mx-liste rt-liste' + (sel ? ' mx-zeigt' : '') }, ...LERN_MX_KL.map((k) => el('section', { class: 'mx-liste-klasse rt-klasse' },
        el('h2', { class: 'mx-liste-kopf' + (k === 9 ? ' mx-hell' : ''), style: `background:${LERN_KL_FARBE[k]}` }, el('b', {}, `Klasse ${k}`), ...kopf(k)),
        ...konts.map((g) => { const l = imFeld(k, g); return l.length ? el('div', { class: 'mx-gruppe' }, el('b', { class: 'mx-gruppe-name' }, g), ...l.map(chip)) : null; })))));
      const c = sel && ansicht.querySelector(`.mx-chip[data-id="${sel}"]`); if (c) c.after(detail); else detail.remove();
      return;
    }
    const zellen = [el('div', { class: 'mx-ecke' }), ...konts.map((g) => el('div', { class: 'mx-geb' }, g))];
    for (const k of LERN_MX_KL) zellen.push(el('div', { class: 'mx-kl' + (k === 9 ? ' mx-hell' : ''), style: `background:${LERN_KL_FARBE[k]}` }, el('b', {}, `Kl. ${k}`), ...kopf(k)),
      ...konts.map((g) => el('div', { class: 'mx-zelle' }, ...imFeld(k, g).map(chip))));
    svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg'); svg.setAttribute('class', 'mx-linien'); svg.setAttribute('aria-hidden', 'true');
    lernErsetze(ansicht, el('div', { class: 'mx-wrap' }, el('div', { class: 'mx-matrix mx-z rt-matrix' + (sel ? ' mx-zeigt' : ''), style: `--n:${konts.length}` }, ...zellen), svg));
    if (!detail.isConnected) ansicht.after(detail);
    requestAnimationFrame(linien);
  };
  function linien() {
    if (!svg || !svg.isConnected) return; svg.replaceChildren(); if (!sel) return;
    const w = svg.parentNode.getBoundingClientRect();
    const r = (id) => { const c = svg.parentNode.querySelector(`.mx-chip[data-id="${id}"]`); if (!c) return null; const b = c.getBoundingClientRect(); return { x: b.left - w.left + b.width / 2, y: b.top - w.top + b.height / 2 }; };
    const s = r(sel); if (!s) return;
    svg.setAttribute('viewBox', `0 0 ${w.width} ${w.height}`); svg.setAttribute('width', w.width); svg.setAttribute('height', w.height);
    const linie = (a, b, k, art) => { const my = (a.y + b.y) / 2; const p = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      p.setAttribute('d', `M${a.x},${a.y} C${a.x},${my} ${b.x},${my} ${b.x},${b.y}`); p.setAttribute('class', `mx-linie ${k}${art === 'e' || art === 'empfohlen' ? ' mx-empfohlen' : ''}`); svg.append(p); };
    (vor.get(sel) || []).forEach((e) => { const a = r(e.id); if (a) linie(a, s, 'mx-l-vor', e.art); });
    (nach.get(sel) || []).forEach((e) => { const b = r(e.id); if (b) linie(s, b, 'mx-l-nach', e.art); });
  }
  const zeichen = (f) => el('span', { class: `rt-zeichen ${kl(f.s)}`, 'aria-hidden': 'true' }, LERN_STUFE[f.s.stufe]?.z || '+');
  const verweis = (id) => { const f = by.get(id); if (!f) return null; const t = lernRtStand(f.s, f.n);
    return el('li', {}, zeichen(f), el('button', { type: 'button', class: 'rt-link', onclick: () => { sel = id; zeichne(); } }, f.titel), t ? el('small', {}, ` · ${t.replace(/^[◉↻▶○] /, '')}`) : el('small', {}, ' · nicht in deinem Plan')); };
  const laden = (f) => {
    if (details.has(f.id)) return;
    details.set(f.id, 'laedt');
    Promise.all([lernCall('schule_lehrplan_thema', { thema_id: f.id, lernender_id: kind.id }).catch(() => null), merk ? Promise.resolve(merk) : lernMerkDaten(d).catch(() => [])])
      .then(([t, mh]) => { merk = mh; details.set(f.id, t || 'fehler'); if (live() && sel === f.id) zeichneDetail(); });
  };
  function zeichneDetail() {
    const f = sel && by.get(sel);
    if (!f) { lernErsetze(detail, el('p', { class: 'lr-leise rt-tipp' }, 'Tipp einen Flug an: Dann siehst du, was du dort lernst, was du vorher brauchst und wie es danach weitergeht.')); if (handy()) detail.remove(); return; }
    laden(f); const t = details.get(f.id); const fertig = t && typeof t === 'object';
    const mh = (merk || []).find((x) => x.einheit_id === f.einheit);
    const etappen = fertig ? t.etappen || [] : [];
    const dran = f.s.stufe === 'dran' && f.einheit;
    const st = lernRtStand(f.s, f.n);
    lernErsetze(detail,
      el('p', { class: 'lr-ueber' }, [f.kont, f.ort].filter(Boolean).join(' · ').toUpperCase()),
      el('h2', { class: 'rt-titel' }, f.titel),
      st ? el('p', { class: `rt-stand ${kl(f.s)}` }, st) : el('p', { class: 'lr-leise' }, 'Dieser Flug ist gerade nicht in deinem Plan.'),
      dran ? el('a', { class: 'lr-knopf rt-weiter', href: `#/lerneinheit/${kind.id}-${f.einheit}-ueben` }, 'Weiter lernen ›') : null,
      t === 'laedt' ? el('p', { class: 'lr-leise' }, 'Einen Moment …') : null,
      fertig && t.was_gefordert ? [el('h3', {}, 'Was du hier lernst'), el('p', {}, t.was_gefordert)] : null,
      fertig && (t.merke || []).length ? [el('h3', {}, 'Das muss sitzen'), el('ul', {}, ...t.merke.map((x) => el('li', {}, x)))] : null,
      (vor.get(f.id) || []).length ? [el('h3', {}, 'Das brauchst du vorher'), el('ul', { class: 'rt-verweise' }, ...vor.get(f.id).map((e) => verweis(e.id)))] : null,
      (nach.get(f.id) || []).length ? [el('h3', {}, 'Danach geht’s weiter mit'), el('ul', { class: 'rt-verweise' }, ...nach.get(f.id).map((e) => verweis(e.id)))] : null,
      etappen.length ? [el('h3', {}, `Die Etappen (${etappen.length})`), el('ol', { class: 'rt-etappen' }, ...etappen.map((e) => { const ok = !!mh?.stand?.[e.lernziel]?.fertig;
        return el('li', { class: ok ? 'rt-gelandet' : '' }, el('span', { class: 'rt-haken', 'aria-label': ok ? 'gelandet' : 'noch nicht gelandet' }, ok ? '✓' : ''), e.titel); }))] : null);
  }
  function zeichne() { if (!live()) return; zeichneMatrix(); zeichneDetail(); }
  let warHandy = handy();
  const groesse = () => { if (!live()) { removeEventListener('resize', groesse); return; } if (handy() !== warHandy) { warHandy = handy(); zeichne(); } else linien(); };
  addEventListener('resize', groesse);
  lernErsetze(main, lernRahmen(kind, 'reise', lernKopf('MEINE ROUTE 5–10', 'Deine Route durch die Mathe-Welt'),
    el('p', { class: 'lr-leise rt-einleitung' }, 'Jede Spalte ist ein Kontinent, jede Zeile eine Klasse. Tipp einen Flug an: Die Linien zeigen, was du vorher brauchst (gelb) und was darauf aufbaut (blau).'),
    el('div', { class: 'rt-legende lr-leise' }, ...['komplett', 'wiederholung', 'dran', 'kommt'].map((s) => el('span', {}, el('i', { class: `rt-zeichen ${LERN_STUFE[s]?.kl}`, 'aria-hidden': 'true' }, LERN_STUFE[s]?.z),
      ({ komplett: 'kannst du', wiederholung: 'kommt zur Wiederholung', dran: 'hier bist du', kommt: 'kommt noch' })[s]))),
    el('div', { class: 'rt-route' }, ansicht)));
  zeichne();
  requestAnimationFrame(() => ansicht.querySelector('.mx-chip.mx-dran')?.scrollIntoView({ block: 'center' })); // beim Öffnen zum ▶-Flug
}

// ---------- Wiederholen: fällige Lernkarten, je eine Aufgabe ----------
async function viewWiederholen(arg) {
  setChrome('Wiederholen', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const [kArg, modus] = String(arg || '').split('-'); // „<kind>-extra“: freiwillige Extra-Bordkarten (je Klick höchstens 3)
  const d = await lernLadeKind(kArg);
  if (!d || !live()) return;
  const r = await lernWdhLaden(d.kind.id);
  if (!live()) return;
  const { kind } = d;
  // Check-in (Vorgabe „abgelegt“ 2/3): neuer Server, Runde offen → die offenen Pflicht-Bordkarten; „extra“ → höchstens 3 freiwillige; alter Server → wie 0.84.0
  const ws = lernWdhStand(r, kind.id);
  const checkin = ws.neu && !ws.gemacht && modus !== 'extra' && ws.offen > 0;
  const extra = ws.neu && !checkin;
  const liste = checkin ? ws.liste : extra ? (ws.alle || []).filter((a) => !a.pflicht || ws.gemacht).slice(0, 3) : r.aufgaben || [];
  const n = d.naechste; const nach = n ? n.stadt || n.ort_titel || n.titel : null;
  const flaeche = el('div', { class: 'lr-etappe-flaeche' + (ws.neu ? ' lr-checkin' : '') });
  const zustand = Array.from({ length: checkin ? ws.runde : liste.length }, (_, i) => (checkin && i < ws.erledigt ? 'da' : ''));
  const versatz = checkin ? ws.erledigt : 0;
  let i = 0, richtig = 0, sterne = 0;
  const kontoSterne = Number(d.konto?.sterne || 0);
  const zaehler = () => el('span', { class: 'lr-checkin-sterne', 'aria-label': `${lernZahl(kontoSterne + sterne)} Sterne` }, `★ ${lernZahl(kontoSterne + sterne)}`);
  const kopfZeile = (text, plus) => el('div', { class: 'lr-checkin-kopf' }, el('span', {}, text), el('span', { class: 'lr-checkin-zaehler' }, zaehler(), plus ? el('span', { class: 'lr-fliegt', 'aria-hidden': 'true' }, `+${plus}`) : null));
  const zeige = () => {
    const a = liste[i];
    if (!a) {
      const falsch = liste.length - richtig; // V7: der Haken nur, wenn alles richtig war
      if (checkin) lernCall('schule_wiederholung_runde_fertig', { lernender_id: kind.id }).catch(() => null); // WD-S 2: der Server setzt „gemacht“ selbst; hier nur bestätigen
      else if (!ws.neu) lernWdhHeute(kind.id, true); // V9 (alter Server): Runde für heute auf diesem Gerät gemacht
      if (ws.neu) {
        const nochExtra = checkin ? ws.extra : Number(r.faellig || 0) > liste.length && (ws.alle || []).length > liste.length;
        const keineFrische = checkin ? ws.keineFrische : Number(r.faellig || 0) > liste.length && (ws.alle || []).length <= liste.length;
        lernErsetze(flaeche, kopfZeile(checkin ? 'CHECK-IN' : 'EXTRA'),
          el('section', { class: 'lr-karte-box lr-geschafft lr-checkin-fertig' }, el('div', { class: 'lr-checkin-symbol', 'aria-hidden': 'true' }, '🧳'),
            el('h1', { class: 'lr-titel' }, checkin ? 'Eingecheckt!' : 'Geschafft!'), lernKoffer(zustand.length, zustand),
            el('p', { class: 'lr-checkin-ergebnis' }, el('b', {}, `${richtig} von ${liste.length} richtig`), sterne ? [' · ', el('b', { class: 'lr-gold-text' }, `+${lernZahl(sterne)} ★`)] : null),
            el('p', { class: 'lr-leise' }, falsch ? `${falsch === 1 ? 'Eine Bordkarte kommt' : `${falsch} Bordkarten kommen`} beim nächsten Mal wieder.` : checkin ? 'Alles richtig – super eingecheckt!' : 'Alles richtig!'),
            // WK 2 (A2): direkt in den nächsten Schritt (Schritt 1–5), nie zurück in den Check-in
            lernSchrittKnopf(kind.id, { gross: false, ohne: (s) => /^#\/wiederholen\//.test(s.ziel), vorher: n ? { text: `Weiter nach ${nach}`, ziel: lernUebenZiel(kind.id, n) } : { text: 'Weiter', ziel: `#/reise/${kind.id}` } }),
            nochExtra ? el('a', { class: 'lr-textlink lr-extra-link', href: `#/wiederholen/${kind.id}-extra`, onclick: () => setTimeout(render, 0) }, `Noch 3 Extra-Bordkarten?${ws.sterne ? ` Je richtig ★ ${ws.sterne}` : ''}`)
              : keineFrische ? el('p', { class: 'lr-leise lr-keine-frische' }, LERN_KEINE_FRISCHE) : null),
          lernWdhErklaert(true));
        return;
      }
      lernErsetze(flaeche, el('section', { class: 'lr-geschafft' }, falsch ? null : el('div', { class: 'lr-geschafft-haken' }, lernIcon(LI.haken, 64)),
        el('p', { class: 'lr-ueber' }, 'WIEDERHOLT'), el('h1', { class: 'lr-titel' }, `${richtig} von ${liste.length} richtig`),
        el('p', { class: 'lr-leise' }, falsch ? `${falsch} ${falsch === 1 ? 'Etappe braucht' : 'Etappen brauchen'} noch Übung – morgen ${falsch === 1 ? 'kommt sie' : 'kommen sie'} wieder. Die Erklärung findest du im Merkheft.` : 'Super – das sitzt noch.')),
        el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Weiter zu Heute'), lernWdhErklaert());
      return;
    }
    zustand[versatz + i] = zustand[versatz + i] || 'jetzt';
    const auf = lernAufgabe(a); const cid = lernCid();
    const meldung = el('div', { role: 'status', 'aria-live': 'polite' });
    const pruefen = el('button', { type: 'button', class: 'lr-knopf' }, 'Prüfen');
    const koffer = el('div', {}, ws.neu ? lernKoffer(zustand.length, zustand) : null);
    const kopf = el('div', {}, ws.neu ? kopfZeile(checkin ? `CHECK-IN · ${versatz + i + 1} VON ${ws.runde}` : `EXTRA · ${i + 1} VON ${liste.length}`) : null);
    pruefen.addEventListener('click', async () => {
      const w = auf.antwort();
      if (!w) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, auf.fehlerText() || 'Bitte erst antworten.')); return; }
      pruefen.disabled = true;
      try {
        const x = await lernCall('schule_uebung_pruefen', { lernender_id: kind.id, aufgabe_id: a.id, antwort: w, client_id: cid, hilfe: 0 });
        if (!x.format_ok) { lernErsetze(meldung, el('p', { class: 'lr-hinweis' }, x.hinweis)); pruefen.disabled = false; return; }
        auf.sperren(); a.loesung = x.loesung; if (x.richtig) richtig++; auf.zeigeLoesung(x.loesung);
        const plus = typeof x.wiederholung?.sterne === 'number' ? x.wiederholung.sterne : typeof x.sterne === 'number' ? x.sterne : 0; // Sterne nur aus der Antwort des Servers
        const ab = Number(x.abgelegt?.etappe?.sterne || 0) + Number(x.abgelegt?.flug?.sterne || 0);
        sterne += plus + ab;
        zustand[versatz + i] = x.richtig ? 'ok' : 'nein';
        if (ws.neu) { lernErsetze(koffer, lernKoffer(zustand.length, zustand)); lernErsetze(kopf, kopfZeile(checkin ? `CHECK-IN · ${versatz + i + 1} VON ${ws.runde}` : `EXTRA · ${i + 1} VON ${liste.length}`, plus)); }
        // ChatGPT 919: richtig mit Tipp oder im zweiten Versuch zählt nicht als bestandene Wiederholung – freundlich sagen, kein Fehler
        const mitHilfe = x.richtig && x.wiederholung?.bestanden === false;
        if (mitHilfe) zustand[versatz + i] = 'hilfe';
        if (mitHilfe && ws.neu) lernErsetze(koffer, lernKoffer(zustand.length, zustand));
        if (x.richtig) lernJwRichtig(kind.id); // JW: Wiederholung bestanden (ohne Hilfe) → Sticker Stärke 1; Fehler nach der Fehler-Regel
        lernErsetze(meldung, x.richtig ? el('div', { class: 'lr-rueck lr-rueck-ok' }, el('b', {}, mitHilfe ? 'Richtig – morgen noch einmal ohne Hilfe.' : 'Richtig!'), plus ? el('span', { class: 'lr-plus-stern' }, `+${plus} ★`) : null,
            mitHilfe ? null : lernJwPlatz(kind.id, 'wiederholung', 'box'))
          : el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, 'Noch nicht. Richtig ist: ', lernMathe(lernLoesungText(a))), x.loesungsweg ? el('p', {}, lernMathe(x.loesungsweg)) : null,
            ws.neu ? el('p', { class: 'lr-leise' }, 'Kein Problem – diese Bordkarte kommt beim nächsten Mal wieder.') : null,
            el('a', { class: 'lr-klein-link', href: `#/lerneinheit/${kind.id}-${a.einheit_id}` }, 'Zur Etappe'), lernJwPlatz(kind.id, 'fehler', 'fehler', () => lernJwFehler(kind.id))));
        i++;
        const naechste = el('button', { type: 'button', class: 'lr-knopf', onclick: zeige }, ws.neu ? (i < liste.length ? 'Nächste Bordkarte ›' : 'Fertig ›') : i < liste.length ? 'Nächste' : 'Fertig');
        pruefen.replaceWith(naechste);
        if (x.abgelegt) lernAbgelegtZeigen(kind, x.abgelegt, { checkin, nachbarn: (d.mit || []).map((e) => e.titel) }).then(() => naechste.focus({ preventScroll: true })); // WD-6
      } catch (err) { if (lernGesperrt(err)) { render(); return; } lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
    });
    lernErsetze(flaeche, ws.neu ? kopf : null, ws.neu ? koffer : null,
      el('header', { class: 'lr-etappe-oben' }, ws.neu ? null : el('p', { class: 'lr-ueber' }, `WIEDERHOLEN ${i + 1} VON ${liste.length} · ${lernStadtName(kind.id, a).toUpperCase()}`),
        ws.neu ? null : el('h1', { class: 'lr-titel' }, a.etappe || 'Bordkarte')),
      el('section', { class: 'lr-karte-box lr-aufgabe' }, ws.neu ? el('p', { class: 'lr-leise lr-checkin-herkunft' }, [a.etappe, lernStadtName(kind.id, a) ? `aus ${lernStadtName(kind.id, a)}` : null].filter(Boolean).join(' · ')) : null, auf.node), meldung, pruefen,
      checkin ? el('a', { class: 'lr-ab-pause lr-checkin-pause', href: `#/reise/${kind.id}` }, 'Pause – später weiter einchecken') : null);
    window.scrollTo(0, 0);
  };
  if (!liste.length) lernErsetze(flaeche, el('p', { class: 'lr-leise' }, ws.neu && ws.keineFrische ? LERN_KEINE_FRISCHE : ws.neu && ws.gemacht && modus !== 'extra' ? 'Heute schon eingecheckt.' : 'Gerade ist nichts zum Wiederholen dran.'), el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Zu Heute'));
  else zeige();
  lernErsetze(main, lernRahmen(kind, 'reise', flaeche));
}
