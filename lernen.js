/* W150: Lernen Schule – Lernreise der Kinder in der App.
   Spricht mit der Serverfunktion lernen-api (gleiche Anmeldung wie app-api). Die Datenbank prüft Zugriff,
   bewertet Antworten und führt Lernstand, Sterne und Stempel; die App zeigt nur an und schickt Eingaben.
   Ansichten:
     #/lernen                      Eltern: Mathe-Merkblatt, Lernreisen der Kinder, Belohnungen und Einlösungen
     #/reise/<kind>                Kind: Heute dran (aktueller Ort auf der echten Weltkarte)
     #/weltkarte/<kind>            Kind: Weltkarte, Kontinente und Orte
     #/weg/<kind>                  Kind: Mein Weg – kann ich · gerade dran · kommt noch
     #/merkheft/<kind>             Kind: Merkheft – Spickzettel aller geschafften Etappen, durchsuchbar
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
// Ordnet die Orte eines Kindes: Jetzt dran · Kann schon · Später (nach Route und Klassenstufe); mit Stand je Einheit.
function lernReiseDaten(u, kindId) {
  const kind = (u.lernende || []).find((k) => k.id === kindId);
  if (!kind) return null;
  const stand = new Map((kind.stand || []).map((s) => [s.einheit_id, s]));
  const route = new Map((kind.route || []).filter((r) => r.status !== 'entfernt').sort((a, b) => (a.art === 'rueckreise') - (b.art === 'rueckreise')).map((r) => [r.block_id, r]));
  const einheiten = (u.einheiten || []).filter((e) => e.status !== 'entwurf' || kind.ist_test);
  // Themenplan (Eltern/Lehrer): Gibt es ihn, kommen nur Orte aus dem Plan dran – in seiner Reihenfolge.
  const mitPlan = (kind.route || []).some((r) => r.art === 'normal' && r.status !== 'entfernt');
  const gruppe = (e) => {
    const r = route.get(e.block_id);
    if (kind.ist_test || !kind.route?.length) return 'jetzt';
    if (mitPlan && !r) { // nicht im Plan: frühere Klassen heißen „zum Auffrischen“, der Rest „später“
      const k0 = e.jahrgang?.[kind.schulart || 'gym_by'] ?? e.ziel_klasse;
      return k0 && kind.klasse && k0 < kind.klasse ? 'frueher' : 'spaeter';
    }
    if (r?.kann_schon || r?.status === 'fertig') return 'kann'; // geschaffte Orte wandern zu „zum Wiederholen“
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
  }).sort((a, b) => pos(a) - pos(b) || a.id - b.id);
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
  return { kind, mit, orte, jetzt, naechste, kann: mit.filter((e) => e.gruppe === 'kann'), frueher: mit.filter((e) => e.gruppe === 'frueher'), spaeter: mit.filter((e) => e.gruppe === 'spaeter') };
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
      ...[['reise', 'Abflugtafel'], ['weg', 'Mein Weg'], ['merkheft', 'Merkheft'], ['weltkarte', 'Weltkarte'], ['reisepass', 'Reisepass']].map(([v, t]) =>
        el('a', { href: `#/${v}/${kind.id}`, class: v === aktiv ? 'on' : '', ...(v === aktiv ? { 'aria-current': 'page' } : {}), onclick: zu }, t)),
      el('button', { type: 'button', onclick: () => { try { localStorage.setItem('lern.gestaltung.' + kind.id, g === 'nacht' ? 'tag' : 'nacht'); } catch { /* egal */ } zu(); render(); } }, g === 'nacht' ? 'Helle Ansicht' : 'Dunkle Ansicht'),
      el('button', { type: 'button', class: 'lr-blatt-zu', onclick: zu }, 'Schließen')));
    const knopf = el('button', { type: 'button', class: 'lr-menue', 'aria-label': 'Menü', 'aria-haspopup': 'dialog', onclick: () => blatt.showModal() }, el('span', { 'aria-hidden': 'true' }, '≡'));
    return el('div', { class: lernThema(kind) + ' lr-mit-menue' }, el('div', { class: 'lr-inhalt' }, ...inhalt), knopf, blatt);
  }
  const nav = el('nav', { class: 'lr-nav', 'aria-label': 'Lernreise' },
    ...[['reise', 'Heute', LI.heute], ['weg', 'Mein Weg', LI.weg], ['merkheft', 'Merkheft', LI.heft], ['weltkarte', 'Karte', LI.karte]].map(([v, t, i]) =>
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
      el('div', { class: 'lr-stats' }, s(LI.stempel, konto?.stempel ?? 0, 'Stempel'), s(LI.stern, lernZahl(konto?.sterne ?? 0), 'Sterne'), s(LI.tag, konto?.lerntage ?? 0, 'Lerntage'))),
    el('div', { class: 'lr-stats-erkl' },
      el('p', {}, el('b', {}, 'Sterne: '), '10 für jede Übungsaufgabe, die du zum ersten Mal richtig löst, 20 für jede richtige Testaufgabe. Sterne kannst du später gegen Belohnungen eintauschen.'),
      el('p', {}, el('b', {}, 'Stempel: '), 'Jeder Ort hat mehrere Themen. Hast du alle Themen eines Ortes geschafft, bekommst du seinen Stempel in den Reisepass.'),
      el('p', {}, el('b', {}, 'Lerntage: '), 'Tage, an denen du geübt hast.')));
}
async function lernLadeKind(arg) {
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return null; }
  const [u, k] = await Promise.all([lernCall('schule_uebersicht'), lernCall('schule_konto', { lernender_id: kindId }).catch(() => null)]);
  const d = lernReiseDaten(u, kindId);
  if (!d) { route('lernen'); return null; }
  if (k?.look) Object.assign(d.kind, k.look);
  d.konto = k?.konto || null; d.belohnungen = k?.belohnungen || []; d.einloesungen = k?.einloesungen || [];
  return d;
}

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
  const standKarten = u.leitung ? (u.lernende || []).filter((k) => !k.ist_test).map((k) => el('a', { class: 'card lern-kindkarte', href: `#/lernstand/${k.id}` },
    el('b', {}, `Lernstand ${k.name}`), el('p', { class: 'small muted' }, 'Was sitzt, was wackelt – mit den echten falschen Antworten.'), el('span', { class: 'lern-kindkarte-los' }, 'Ansehen ›'))) : [];
  const offen = (rm?.rueckmeldungen || []).filter((r) => ['offen', 'in_arbeit'].includes(r.status)).length;
  const planKarten = u.leitung ? (u.lernende || []).filter((k) => !k.ist_test).map((k) => el('a', { class: 'card lern-kindkarte', href: `#/plan/${k.id}` },
    el('b', {}, `Themenplan ${k.name}`),
    el('p', { class: 'small muted' }, (k.route || []).some((r) => r.art === 'normal' && r.status !== 'entfernt')
      ? `${(k.route || []).filter((r) => r.art === 'normal' && r.status !== 'entfernt').length} Orte im Plan` : 'Noch kein Plan – alle Themen sichtbar'),
    el('span', { class: 'lern-kindkarte-los' }, 'Plan bearbeiten ›'))) : [];
  const steuern = u.leitung ? [
    el('section', { class: 'start-intro lern-neu' }, el('p', { class: 'eyebrow' }, 'ELTERN UND LEHRER'), el('h2', {}, 'Themen und Rückmeldungen')),
    el('div', { class: 'lern-kinderliste' },
      el('a', { class: 'card lern-kindkarte lp-hauptkarte', href: '#/lehrplan' }, el('b', {}, 'Lehrplan-Übersicht'),
        el('p', { class: 'small muted' }, 'Alle Themen je Schulart und Klasse: was fertig ist, was in Prüfung ist, was noch fehlt – mit Inhalten zum Ansehen.'),
        el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ›')),
      ...standKarten,
      ...planKarten,
      el('a', { class: 'card lern-kindkarte', href: '#/rueckmeldungen' }, el('b', {}, 'Rückmeldungen an die Entwicklung'),
        el('p', { class: 'small muted' }, offen ? `${offen} offen` : 'Thema fehlt, zu ungenau, mehr Aufgaben … hier eintragen'), el('span', { class: 'lern-kindkarte-los' }, 'Öffnen ›')),
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
    wartet,
    el('section', { class: 'start-intro lern-neu' }, el('p', { class: 'eyebrow' }, 'LERNREISE'), el('h2', {}, 'Wer lernt heute?')),
    el('div', { class: 'lern-kinderliste' }, ...(kinder.length ? kinder : [el('p', { class: 'card muted' }, 'Kein Kind freigeschaltet.')])),
    ...steuern,
    neueAntworten.length ? el('section', { class: 'card' }, el('h3', {}, 'Antworten auf eure Anmerkungen'),
      ...neueAntworten.map((r) => el('p', { class: 'small' }, el('b', {}, (r.ort || 'Allgemein') + ': '), r.antwort)), el('a', { class: 'small', href: '#/rueckmeldungen' }, 'Alle Rückmeldungen ›')) : null,
    eltern ? lernElternBereich(eltern, { ohneWuensche: true }) : null,
    seite ? null : el('details', { class: 'card lern-weitere' }, el('summary', {}, 'Weitere Lernhilfen'),
      el('p', {}, 'Mathe-Lernblatt: Erklärungen, Aufgaben in drei Stufen und typische Fehler. Die Seite öffnet ohne Anmeldung.'),
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
  if (lernNeu(kind) && n) { lernErsetze(main, lernRahmen(kind, 'reise', ...lernAbflugtafel(d, { n, et, nWdh, wdhRest }))); return; }
  const teile = [el('header', { class: 'lr-kopf lr-kopf-kurz' }, el('p', { class: 'lr-gruss' }, `Hallo ${kind.name}!`))];
  if (n) {
    const kont = d.orte.filter((o) => o.kontinent === (d.orte.find((x) => x.block_id === n.block_id)?.kontinent));
    const ortN = d.orte.find((o) => o.block_id === n.block_id) || {};
    // Ein einziger Startknopf: erst die fälligen Wiederholungen, dann direkt ins Üben des Themas.
    const testDran = !n.laeuft && et.n > 0 && et.f >= et.n; // alle Lernkarten sitzen → als Nächstes der Test, nicht wieder üben
    const ziel = n.laeuft || testDran ? `#/lerneinheit/${kind.id}-${n.id}-test` : nWdh ? `#/wiederholen/${kind.id}` : `#/lerneinheit/${kind.id}-${n.id}-ueben`;
    teile.push(el('section', { class: 'lr-karte-box lr-haupt' },
      el('p', { class: 'lr-ueber' }, `JETZT DRAN · ${(n.stadt || '').toUpperCase()}`),
      el('h1', { class: 'lr-titel lr-titel-thema' }, n.titel),
      el('a', { class: 'lr-knopf lr-knopf-start', href: ziel }, n.laeuft ? 'Test weitermachen' : testDran ? 'Zum Test' : et.f || nWdh ? 'Weiter geht’s' : 'Los geht’s'),
      nWdh && !n.laeuft ? el('p', { class: 'lr-leise lr-start-info' }, `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'}, dann ${n.stadt}.`) : null,
      et.n ? el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${et.f} von ${et.n} Lernkarten sitzen` }, el('span', { style: `width:${Math.round(100 * et.f / et.n)}%` })), el('b', {}, `${et.f} von ${et.n} Lernkarten sitzen`)) : null,
      el('a', { class: 'lr-textlink', href: `#/lerneinheit/${kind.id}-${n.id}` }, 'Erst die Erklärungen ansehen'),
      el('div', { class: 'lr-kartenbild lr-kartenbild-klein' }, lernKarte({ orte: kont, fokus: kont.slice(0, Math.max(3, kont.indexOf(ortN) + 2)), hervor: LERN_ERDTEIL[ortN.kontinent], route: true,
        beschriftung: [{ ...ortN, text: `Du bist in ${n.stadt}`, jetzt: true, gross: true }], label: `Karte: ${n.stadt}, ${n.land}`, breite: 340, hoehe: 110 })),
      (() => { const o = ortStand(n.block_id); return o && o.themen > 1 ? el('p', { class: 'lr-leise lr-ortstand' },
        `${n.stadt} hat ${o.themen} Themen, ${o.erledigt} davon geschafft. Den Stempel gibt es, wenn alle geschafft sind.`) : null; })()));
  } else teile.push(el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Gerade ist nichts offen'), el('p', { class: 'lr-leise' }, 'Neue Orte kommen bald. '), nWdh ? el('a', { class: 'lr-knopf', href: `#/wiederholen/${kind.id}` }, `${nWdh} ${nWdh === 1 ? 'Aufgabe' : 'Aufgaben'} wiederholen`) : el('a', { class: 'lr-knopf-zweit', href: `#/reisepass/${kind.id}` }, 'Zum Reisepass')));
  teile.push(lernStats(d.konto), el('a', { class: 'lr-textlink', href: `#/reisepass/${kind.id}` }, 'Reisepass und Belohnungen ansehen'));
  const jg = d.konto?.jahrgang;
  if (jg?.themen) teile.push(el('section', { class: 'lr-karte-box lr-jgstand' },
    el('p', { class: 'lr-ueber' }, `MEIN STAND · ${(LERN_SCHULART[jg.schulart] || '').toUpperCase()} KLASSE ${jg.klasse}`),
    el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${jg.geschafft} von ${jg.themen} Themen geschafft` }, el('span', { style: `width:${Math.round(100 * jg.geschafft / jg.themen)}%` })),
      el('b', {}, `${jg.geschafft} von ${jg.themen} Themen`)),
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
    el('p', {}, 'Sitzt eine Lernkarte, kommt sie später zum Wiederholen zurück – jedes Mal mit einer Aufgabe.'),
    el('p', {}, 'Die Abstände werden größer: nach 1, 3, 7, 14 und 30 Lerntagen. Ein Lerntag ist ein Tag, an dem du übst. Machst du Pause, wartet die Karte.'),
    el('p', {}, 'Stimmt die Aufgabe nicht, kommt die Karte am nächsten Lerntag wieder. Erst beim zweiten Fehler übst du sie noch einmal von vorn.'),
    el('p', {}, 'Vor einem Thema kommen höchstens ' + LERN_WDH_RUNDE + ' Wiederholungen. Nach dem Test zu einem Thema folgt später ein kurzer Nachtest.'));
}
function lernAbflugtafel(d, { n, et, nWdh, wdhRest = 0 }) {
  const { kind } = d; const sa = kind.schulart || 'gym_by';
  const kl = (e) => e.jahrgang?.[sa] ?? e.ziel_klasse;
  const code = (e) => String(e.stadt || e.ort_titel || '').toUpperCase();
  const zeile = (e, status, klasse = '') => el('a', { class: 'lr-flug' + klasse, href: `#/lerneinheit/${kind.id}-${e.id}` },
    el('span', { class: 'lr-flug-ort' }, el('b', {}, code(e)), el('small', {}, e.titel)),
    el('span', { class: 'lr-flug-status' }, el('b', {}, status), kl(e) ? el('small', {}, `Klasse ${kl(e)}`) : null));
  const testDran = !n.laeuft && et.n > 0 && et.f >= et.n; // alle Lernkarten sitzen → als Nächstes der Test, nicht wieder üben
  const ziel = n.laeuft || testDran ? `#/lerneinheit/${kind.id}-${n.id}-test` : nWdh ? `#/wiederholen/${kind.id}` : `#/lerneinheit/${kind.id}-${n.id}-ueben`;
  const weitere = d.jetzt.filter((e) => e !== n);
  const maxZ = kind.klasse && kind.klasse <= 6 ? 3 : 6;
  const offen = Math.max(0, et.n - et.f);
  const gruppe = (titel, liste) => liste.length ? el('details', { class: 'lr-mehr' }, el('summary', {}, `${titel} (${liste.length})`), ...liste.map((e) => lernOrtZeile(kind, e))) : null;
  const jg = d.konto?.jahrgang;
  return [
    el('header', { class: 'lr-kopf lr-tafelkopf' }, el('h1', { class: 'lr-titel' }, 'Abflüge · ', kind.name),
      el('a', { class: 'lr-chip-stern', href: `#/reisepass/${kind.id}`, 'aria-label': `${lernZahl(d.konto?.sterne ?? 0)} Sterne – zum Reisepass` }, '★ ' + lernZahl(d.konto?.sterne ?? 0))),
    el('section', { class: 'lr-abflugtafel', 'aria-label': 'Abflugtafel' },
      el('a', { class: 'lr-flug lr-flug-jetzt', href: ziel },
        el('span', { class: 'lr-flug-ort' }, el('span', { class: 'lr-klapp', role: 'img', 'aria-label': code(n) }, ...[...code(n).slice(0, 9)].map((c, i) => el('i', { style: `--i:${i}` }, c))), el('small', {}, n.titel)),
        el('span', { class: 'lr-flug-status lr-einsteigen' }, el('b', {}, n.laeuft ? 'TEST LÄUFT' : testDran ? 'TEST BEREIT' : 'EINSTEIGEN'), et.n ? el('small', {}, testDran ? 'alle Karten sitzen' : `${offen} von ${et.n} Karten offen`) : null)),
      ...weitere.slice(0, maxZ).map((e) => zeile(e, e.geschafft ? 'GELANDET' : e.fertig ? 'UNTERWEGS' : 'WARTET', e.geschafft ? ' lr-flug-gelandet' : '')),
      ...d.kann.slice(0, 1).map((e) => zeile(e, 'GELANDET', ' lr-flug-gelandet')),
      ...d.spaeter.slice(0, 1).map((e) => zeile(e, `AB KLASSE ${kl(e) ?? ''}`.trim(), ' lr-flug-spaeter'))),
    et.n ? el('div', { class: 'lr-band', role: 'img', 'aria-label': `${et.f} von ${et.n} Lernkarten bis zum Stempel von ${n.stadt}` },
      ...Array.from({ length: et.n }, (_, i) => el('i', { class: i < et.f ? 'voll' : i === et.f ? 'dran' : '' })), el('span', {}, '◎'), el('small', {}, offen ? `Noch ${offen} ${offen === 1 ? 'Karte' : 'Karten'} bis zum Stempel` : 'Alle Karten sitzen')) : null,
    el('div', { class: 'lr-tafelchips' }, el('a', { href: `#/reisepass/${kind.id}` }, `◎ ${d.konto?.stempel ?? 0} Stempel`), el('span', {}, 'Abflug, wann es dir passt')),
    nWdh && !n.laeuft && !testDran ? el('p', { class: 'lr-leise lr-start-info' }, `Erst ${nWdh} ${nWdh === 1 ? 'Wiederholung' : 'Wiederholungen'}, dann ${n.stadt}.`) : null,
    wdhRest ? el('a', { class: 'lr-textlink', href: `#/wiederholen/${kind.id}` }, `Noch ${wdhRest} ${wdhRest === 1 ? 'Wiederholung' : 'Wiederholungen'} offen – wenn du magst`) : null,
    el('a', { class: 'lr-textlink', href: `#/lerneinheit/${kind.id}-${n.id}` }, 'Erst die Erklärungen ansehen'),
    gruppe('Alle offenen Flüge', weitere.length > maxZ ? weitere : []),
    gruppe('Gelandet oder kann schon – zum Wiederholen', d.kann),
    gruppe('Aus früheren Klassen – zum Auffrischen', d.frueher),
    gruppe('Später – für höhere Klassen', d.spaeter),
    lernWdhErklaert(),
    jg?.themen ? el('section', { class: 'lr-karte-box lr-jgstand' },
      el('p', { class: 'lr-ueber' }, `MEIN STAND · ${(LERN_SCHULART[jg.schulart] || '').toUpperCase()} KLASSE ${jg.klasse}`),
      el('div', { class: 'lr-fortschritt' }, el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${jg.geschafft} von ${jg.themen} Themen geschafft` }, el('span', { style: `width:${Math.round(100 * jg.geschafft / jg.themen)}%` })),
        el('b', {}, `${jg.geschafft} von ${jg.themen} Themen`))) : null,
    el('div', { class: 'lr-dock lr-dock-start' }, el('a', { class: 'lr-knopf lr-einsteigen-knopf', href: ziel },
      el('span', {}, n.laeuft ? 'Test weitermachen' : testDran ? 'Zum Test' : nWdh ? 'Erst wiederholen' : 'Einsteigen'), el('span', { class: 'lr-mono' }, code(n).slice(0, 14) + ' ›'))),
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
async function viewWeltkarte(arg) {
  setChrome('Weltkarte', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const { kind } = d;
  if (!d.orte.length) { lernErsetze(main, lernRahmen(kind, 'weltkarte', lernKopf('DEINE MATHE-WELTREISE', 'Noch keine Orte'), el('section', { class: 'lr-karte-box' }, el('p', {}, 'Deine Reise ist noch nicht geplant. Deine Eltern oder deine Lehrkraft legen bald die ersten Orte fest.'), el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Zu Heute')))); return; }
  const konts = [...new Map(d.orte.map((o) => [o.kontinent, o])).values()];
  const zaehl = (k) => { const os = d.orte.filter((o) => o.kontinent === k); return [os.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann').length, os.length]; };
  let wahl = d.orte.find((o) => o.zustand === 'jetzt')?.kontinent || konts[0]?.kontinent;
  const detail = el('section', { class: 'lr-karte-box' });
  const zeigeKontinent = () => {
    const os = d.orte.filter((o) => o.kontinent === wahl); const k0 = os[0] || {};
    lernErsetze(detail, 
      el('p', { class: 'lr-ueber' }, `${(k0.erdteil || '').toUpperCase()} · ${(k0.kontinent_titel || '').toUpperCase()}`),
      os.length && k0.erdteil !== 'Antarktis' ? el('div', { class: 'lr-kartenbild' }, lernKarte({ orte: os, fokus: os, hervor: LERN_ERDTEIL[wahl], route: true,
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
  const fertig = d.orte.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann').length;
  lernErsetze(main, lernRahmen(kind, 'weltkarte',
    lernKopf('DEINE MATHE-WELTREISE', `${fertig} von ${d.orte.length} Orten`),
    el('div', { class: 'lr-kartenbild lr-welt' }, lernKarte({ orte: d.orte, label: 'Weltkarte mit allen Orten' })),
    el('p', { class: 'lr-legende' }, el('span', { class: 'lr-dot lr-dot-fertig' }), 'geschafft', el('span', { class: 'lr-dot lr-dot-jetzt' }), 'jetzt dran', el('span', { class: 'lr-dot lr-dot-offen' }), 'noch offen'),
    knoepfe, detail));
}

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
  lernErsetze(main, lernRahmen(kind, 'weg',
    lernKopf('REISEPASS', kind.name), lernStats(konto),
    el('section', { class: 'lr-karte-box' }, el('h2', {}, 'Stempel'),
      stempel.length ? el('div', { class: 'lr-stempelraster' }, ...stempel.map((o, i) => el('div', { class: 'lr-stempel', style: `--dreh:${(i * 37) % 17 - 8}deg` }, el('b', {}, o.stadt), el('small', {}, o.kontinent_titel))))
        : el('p', { class: 'lr-leise' }, 'Noch kein Stempel. Den ersten gibt es, wenn du alle Themen eines Ortes geschafft hast.'),
      (konto?.orte || []).filter((o) => !o.abgeschlossen && o.erledigt).map((o) => { const ort = d.orte.find((x) => x.block_id === o.block_id);
        return ort ? el('p', { class: 'lr-leise' }, `${ort.stadt}: ${o.erledigt} von ${o.themen} Themen geschafft`) : null; })),
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
        onchange: (ev) => { try { localStorage.setItem('lern.kurzoben.' + kind.id, ev.target.checked ? '1' : '0'); } catch { /* egal */ } } }), ' „Kurz gesagt“ oben in jeder Lernkarte zeigen') : null),
    typeof LERN_SEITE !== 'undefined' && document.getElementById('btn-abmelden') ? el('section', { class: 'lr-karte-box lr-abmelden' },
      el('p', { class: 'lr-leise' }, 'Nur abmelden, wenn du das Gerät abgibst. Danach brauchst du deinen Lern-Code wieder.'),
      el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => document.getElementById('btn-abmelden').click() }, 'Abmelden')) : null));
}

function lernStandZeile(stand) {
  if (!stand?.length) return null;
  return el('div', { class: 'lern-stand', 'aria-label': 'Lernziele' }, ...stand.filter((s) => s.pflicht).map((s) =>
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
    mk('path', { d: `M${a.toFixed(1)} ${Y - 10} Q${((a + z) / 2).toFixed(1)} ${(my - h * 0.55).toFixed(1)} ${z.toFixed(1)} ${Y - 10}`, class: 'bogen' });
    const r = z >= a ? 1 : -1; mk('path', { d: `M${z.toFixed(1)} ${Y - 9} l${(-r * 9).toFixed(1)} -3 l${(r * 4).toFixed(1)} -7 z`, class: 'bogen-spitze' });
    if (bo.name) mk('text', { x: Math.min(B - lernBreite(bo.name) / 2 - 2, Math.max(lernBreite(bo.name) / 2 + 2, (a + z) / 2)), y: Math.max(16, my - h * 0.2 - 4), class: 'zahl fett' }, bo.name);
  });
  { // Punkte mit Namen: ohne Bögen über dem Strahl, mit Bögen darunter (zweite Zeile); Namen, die sich berühren würden, rücken eine Zeile weiter
    const unten = boegen.length > 0; const belegt = [];
    punkte.forEach((q) => { mk('circle', { cx: xv(q.wert), cy: Y, r: 6, class: 'punkt' }); if (!q.name) return;
      const w = lernBreite(q.name), m = Math.min(B - w / 2 - 2, Math.max(w / 2 + 2, xv(q.wert))); let z = 0;
      while (belegt.some(([a0, b0, z0]) => z0 === z && m - w / 2 < b0 + 4 && m + w / 2 > a0 - 4)) z++;
      belegt.push([m - w / 2, m + w / 2, z]); mk('text', { x: m, y: unten ? Y + 52 + z * 20 : Y - 14 - z * 20, class: 'zahl' }, q.name); });
    const zeilen = belegt.reduce((mx, r) => Math.max(mx, r[2] + 1), 0);
    if (unten && zeilen) svg.setAttribute('viewBox', `0 0 ${B} ${84 + oben + zeilen * 20 + 4}`);
  }
  if (g.pfeil !== undefined && g.pfeil !== null) mk('path', { d: `M${x(g.pfeil)} ${Y - 12} l-6 -12 h12 z`, class: 'pfeil' });
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
    ...zs.map((c, i) => el('span', { class: 'lr-kurs-kachel' + (c === ',' || (ln && i === lg + 1) ? ' komma' : '') + (c.trim() === '' ? ' leer' : '') + (c !== andere[i] ? ' ab' : '') }, c.trim())));
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
  gerundet: 'Fast – das ist nur ungefähr. Rechne genau oder runde so, wie es die Aufgabe verlangt.',
};
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
function lernKurzGesagt(regel) {
  const t = String(regel ?? '').replace(/⟦|⟧/g, '').trim();
  const m = t.match(/^.*?[.!?](?=\s|$)/); let k = (m ? m[0] : t).trim();
  if (k.length > 110) k = k.slice(0, 107).replace(/\s+\S*$/, '') + ' …';
  return k;
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
  if (b.stand !== undefined && b.stand !== null) { mk('path', { d: `M${X - 12} ${py(b.stand)} l-12 -6 v12 z`, class: 'pfeil' }); mk('text', { x: X - 28, y: py(b.stand) + 6, class: 'zahl rechts fett' }, b.name || lernZahlText(b.stand) + (b.einheit ? ' ' + b.einheit : '')); }
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
    el('tr', {}, ...(b.ziffern || []).map((z, i) => el('td', { class: i === b.markiert ? 'on' : '' }, z))));
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
  for (const f of b.flaechen || []) mk('polygon', { points: (f.punkte || []).map(([x, y]) => `${px(Math.min(Math.max(x, x0), x1)).toFixed(1)},${py(Math.min(Math.max(y, y0), y1)).toFixed(1)}`).join(' '), class: 'flaeche' });
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
  for (const v of b.senkrecht || []) mk('line', { x1: px(v), y1: py(y0), x2: px(v), y2: py(y1), class: 'hilfslinie' });
  for (const v of b.waagrecht || []) mk('line', { x1: px(x0), y1: py(v), x2: px(x1), y2: py(v), class: 'hilfslinie' });
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
    mk('path', { d, class: 'graph graph' + (gi % 3), 'clip-path': `url(#${clip})` });
    if (g.name) { const xn = g.name_x ?? (x1 - (x1 - x0) * 0.12); const yn = lernGraphWert(g, xn); if (Number.isFinite(yn) && yn > y0 && yn < y1) mk('text', { x: px(xn) + 4, y: py(yn) - 6, class: 'zahl kursiv graphname' + (gi % 3) }, g.name); }
  });
  for (const st of b.strecken || []) mk('line', { x1: px(st[0]), y1: py(st[1]), x2: px(st[2]), y2: py(st[3]), class: st[4] === 'gestrichelt' ? 'hilfslinie' : 'strecke' });
  for (const k of b.kreise || []) { const m = k.m || [0, 0]; mk('ellipse', { cx: px(m[0]), cy: py(m[1]), rx: Math.abs(px(m[0] + k.r) - px(m[0])), ry: Math.abs(py(m[1] + k.r) - py(m[1])), class: 'graph graph' + ((k.farbe ?? 1) % 3) }); if (k.name) mk('text', { x: px(m[0] + k.r * 0.71) + 6, y: py(m[1] + k.r * 0.71) - 4, class: 'zahl links kursiv' }, k.name); }
  for (const v of b.pfeile || []) { // Vektorpfeil [x1, y1, x2, y2, name]
    const [ax1, ay1, ax2, ay2] = [px(v[0]), py(v[1]), px(v[2]), py(v[3])]; const L = Math.hypot(ax2 - ax1, ay2 - ay1) || 1; const ux = (ax2 - ax1) / L, uy = (ay2 - ay1) / L;
    mk('line', { x1: ax1, y1: ay1, x2: ax2 - ux * 6, y2: ay2 - uy * 6, class: 'strecke' });
    mk('path', { d: `M${ax2.toFixed(1)} ${ay2.toFixed(1)} L${(ax2 - ux * 10 - uy * 4.5).toFixed(1)} ${(ay2 - uy * 10 + ux * 4.5).toFixed(1)} L${(ax2 - ux * 10 + uy * 4.5).toFixed(1)} ${(ay2 - uy * 10 - ux * 4.5).toFixed(1)} z`, class: 'spitze' });
    if (v[4]) mk('text', { x: (ax1 + ax2) / 2 - uy * 12, y: (ay1 + ay2) / 2 + ux * 12 + 4, class: 'zahl kursiv' }, v[4]);
  }
  for (const p of b.punkte || []) { mk('circle', { cx: px(p.x), cy: py(p.y), r: 4, class: p.offen ? 'punkt offen' : 'punkt' }); if (p.name) mk('text', { x: px(p.x) + 7, y: py(p.y) - 7, class: 'zahl links' }, p.name); }
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
  if (b.flaeche) mk('polygon', { points: b.flaeche.map((k) => `${px(pk(k)[0])},${py(pk(k)[1])}`).join(' '), class: 'flaeche' });
  for (const k of b.kreise || []) { const m = pk(k.m); mk('circle', { cx: px(m[0]), cy: py(m[1]), r: k.r * f, class: 'kreis' }); if (k.name) mk('text', { x: px(m[0] + k.r * 0.72) + 6, y: py(m[1] + k.r * 0.72) - 4, class: 'zahl links' }, k.name); }
  for (const [u, v, text, art] of b.linien || []) {
    const a = pk(u), c = pk(v);
    mk('line', { x1: px(a[0]), y1: py(a[1]), x2: px(c[0]), y2: py(c[1]), class: art === 'gestrichelt' ? 'hilfslinie' : 'strecke' });
    if (text) {
      const m = [(a[0] + c[0]) / 2, (a[1] + c[1]) / 2]; let n = [-(c[1] - a[1]), c[0] - a[0]]; const l = Math.hypot(...n) || 1; n = [n[0] / l, n[1] / l];
      if ((m[0] - mitte[0]) * n[0] + (m[1] - mitte[1]) * n[1] < 0) n = [-n[0], -n[1]]; // Beschriftung nach außen
      mk('text', { x: px(m[0]) + n[0] * (Math.abs(n[0]) > 0.5 ? 9 : 16), y: py(m[1]) - n[1] * 16 + 4, class: 'zahl' + (n[0] > 0.5 ? ' links' : n[0] < -0.5 ? ' rechts' : '') }, text);
    }
  }
  const richtung = (s, q) => { const a = pk(s), c = pk(q); const l = Math.hypot(c[0] - a[0], c[1] - a[1]) || 1; return [(c[0] - a[0]) / l, (c[1] - a[1]) / l]; };
  for (const [s, q1, q2] of b.rechter_winkel || []) {
    const a = pk(s), u = richtung(s, q1), v = richtung(s, q2), d = 13;
    mk('path', { d: `M${px(a[0]) + u[0] * d} ${py(a[1]) - u[1] * d} l${v[0] * d} ${-v[1] * d} l${-u[0] * d} ${u[1] * d}`, class: 'winkel' });
    mk('circle', { cx: px(a[0]) + (u[0] + v[0]) * d / 2, cy: py(a[1]) - (u[1] + v[1]) * d / 2, r: 1.6, class: 'punkt' });
  }
  for (const [s, q1, q2, text] of b.winkel || []) {
    const a = pk(s), u = richtung(s, q1), v = richtung(s, q2), d = 22;
    const kreuz = u[0] * v[1] - u[1] * v[0];
    mk('path', { d: `M${px(a[0]) + u[0] * d} ${py(a[1]) - u[1] * d} A${d} ${d} 0 0 ${kreuz > 0 ? 0 : 1} ${px(a[0]) + v[0] * d} ${py(a[1]) - v[1] * d}`, class: 'winkel' });
    const w = [u[0] + v[0], u[1] + v[1]]; const l = Math.hypot(...w) || 1;
    if (text) mk('text', { x: px(a[0]) + w[0] / l * (d + 13), y: py(a[1]) - w[1] / l * (d + 13) + 4, class: 'zahl' }, text);
  }
  for (const [name, p] of Object.entries(P)) {
    if (name.startsWith('_')) continue; // Hilfspunkte ohne Beschriftung
    let n = [p[0] - mitte[0], p[1] - mitte[1]]; const l = Math.hypot(...n) || 1; n = [n[0] / l, n[1] / l];
    mk('circle', { cx: px(p[0]), cy: py(p[1]), r: 2.5, class: 'punkt' });
    mk('text', { x: px(p[0]) + n[0] * 15, y: py(p[1]) - n[1] * 15 + 4, class: 'zahl fett' }, name);
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
    el('tbody', {}, ...(b.zeilen || []).map((z) => el('tr', {}, ...z.map((c, i) => el(i === 0 && b.erste_spalte_kopf !== false ? 'th' : 'td', {}, lernText(c)))))));
}
// Erklärung einer Etappe: Regel, vorgerechnetes Beispiel Schritt für Schritt, Probe, typischer Fehler.
function lernSchrittBild(zustand, b) {
  if (!b) return zustand;
  if (!zustand || (b.typ && b.typ !== zustand.typ)) return b;
  return { ...zustand, ...b };
}
// Eine Anzeige für alle Karten (Vorgabe 16.11.): [Kurz gesagt] → Worum geht's? → Bild → Beispiel als Bildergeschichte → „Pass auf!“ → MERKE → Wörterliste.
// Karten ohne einstieg beginnen beim Bild. Schritte sind Texte oder {text, bild}; ein Schrittbild ergänzt das Kartenbild.
function lernErklaerung(e, { kurz = false, kurzGesagt = false } = {}) {
  const wctx = { liste: lernWortListe(e.woerter), gesehen: new Set() };
  const M = (t) => lernMarkiert(t, wctx);
  const einstieg = e.einstieg ? el('div', { class: 'lr-einstieg' }, el('p', { class: 'lr-ueber' }, 'WORUM GEHT’S?'), el('p', {}, ...M(e.einstieg))) : null;
  const schritte = (e.schritte || []).map((x) => (typeof x === 'string' ? { text: x } : x || {}));
  const mitBildern = schritte.some((x) => x.bild);
  let zustand = e.bild || null;
  const li = schritte.map((x) => {
    if (mitBildern) zustand = lernSchrittBild(zustand, x.bild);
    return el('li', { class: 'lr-schritt' + (mitBildern ? ' mit-bild' : '') }, mitBildern && zustand ? lernBild(zustand) : null, el('span', { class: 'lr-schritt-text' }, ...M(x.text)));
  });
  const passauf = e.fehler && !kurz ? el('div', { class: 'lr-fehler lr-passauf' + (e.fehler_bild ? ' mit-bild' : '') },
    e.fehler_bild ? lernBild(lernSchrittBild(zustand, e.fehler_bild)) : null,
    el('p', { class: 'lr-schritt-text' }, el('b', {}, 'Pass auf! '), ...M(e.fehler))) : null;
  const probe = e.probe ? el('p', { class: 'lr-probe' }, 'Probe: ', ...M(e.probe)) : null;
  const merke = e.regel ? el('div', { class: 'lr-merke' }, el('p', { class: 'lr-ueber' }, 'MERKE'), el('p', { class: 'lr-regel' }, ...M(e.regel))) : null;
  return el('div', { class: 'lr-erklaert lr-erklaert-klar' },
    kurzGesagt && e.regel ? el('p', { class: 'lr-kurzgesagt' }, el('b', {}, 'Kurz gesagt: '), lernText(lernKurzGesagt(e.regel))) : null,
    einstieg, lernBild(e.bild),
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
      serie: Number(k.serie || 0), ziel: Number(k.ziel || 4), sitzt: !!k.sitzt, faellig: !!k.faellig, nachgewiesen: !!k.fertig && !k.sitzt,
      aufgaben: (daten.uebungen || []).filter((a) => a.lernziel === e.lernziel) };
  });
}
// Punkte für die Serie: ●●○○ (gefüllt = richtig in Folge), bei „sitzt“ alle gefüllt.
function lernPunkte(e, { gross = false } = {}) {
  const n = Math.max(1, e.ziel || 4), voll = e.sitzt || e.fertig ? n : Math.min(n, e.serie || 0);
  return el('span', { class: 'lr-punkte' + (gross ? ' gross' : ''), role: 'img', 'aria-label': e.sitzt || e.fertig ? 'sitzt' : `${voll} von ${n} richtig in Folge` },
    ...Array.from({ length: n }, (_, i) => el('i', { class: i < voll ? 'voll' : '' })));
}
const lernKartenStatus = (e) => e.faellig ? 'Wiederholen' : e.sitzt || e.fertig ? 'sitzt' : e.serie ? 'am Üben' : 'noch nicht geübt';
// Bereiche: aus inhalt.abschnitte, sonst ein Bereich mit allen Karten.
function lernBereiche(etappen) {
  const map = new Map();
  for (const e of etappen) { const t = e.abschnitt || 'Lernkarten'; if (!map.has(t)) map.set(t, []); map.get(t).push(e); }
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
  if (!pflicht.length) return el('p', { class: 'lr-gesperrt' }, 'Dieses Thema wird gerade gebaut. Schau bald wieder vorbei.');
  if (daten.laufender_test) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Angefangenen Test weitermachen');
  if (daten.blocktest_fertig) return el('a', { class: 'lr-zeile', href: `${ctx.basis}-test` }, el('span', { class: 'lr-zeile-icon' }, lernIcon(LI.stempel, 22)),
    el('span', { class: 'lr-zeile-text' }, el('b', {}, 'Test, Verbessern und Nachtests'), el('small', {}, daten.nachtest?.grund === 'faellig' ? 'Ein Nachtest ist jetzt dran.' : 'Hier siehst du, was als Nächstes kommt.')), lernIcon(LI.pfeil, 20));
  if (!offen) return el('a', { class: 'lr-knopf', href: `${ctx.basis}-test` }, 'Alle Lernkarten sitzen – Test starten');
  return el('p', { class: 'lr-gesperrt' }, lernIcon('M6 11h12v10H6z|M9 11V8a3 3 0 0 1 6 0v3', 20), `Der Test kommt, wenn alle Lernkarten sitzen (noch ${offen}).`);
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
  const fortschritt = el('div', { class: 'lr-fortschritt' });
  const zeichneFortschritt = () => lernErsetze(fortschritt, 
    el('div', { class: 'lr-balken', role: 'img', 'aria-label': `${sitzen()} von ${pflicht.length} Lernkarten sitzen` }, el('span', { style: `width:${pflicht.length ? Math.round(100 * sitzen() / pflicht.length) : 0}%` })),
    el('b', {}, `${sitzen()} von ${pflicht.length} sitzen`));
  zeichneFortschritt();
  const tabs = { erklaeren: null, ueben: null, fehler: null };
  const panels = { erklaeren: el('section', { class: 'lr-panel', role: 'tabpanel' }), ueben: el('section', { class: 'lr-panel', role: 'tabpanel' }), fehler: el('section', { class: 'lr-panel', role: 'tabpanel' }) };
  const anzahlUeben = etappen.reduce((n, e) => n + e.aufgaben.length, 0);
  const tabLeiste = el('div', { class: 'lr-tabs lr-tabs-3', role: 'tablist', 'aria-label': 'Thema' },
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
        ctx.leitung ? lernAnmerkung({ einheit_id: ctx.einheit, lernender_id: ctx.kind }, 'Anmerkung zu diesem Thema') : null);
      return;
    }
    const naechste = etappen[etappen.indexOf(e) + 1] || null;
    lernErsetze(panels.erklaeren,
      el('button', { type: 'button', class: 'lr-textlink lr-zur-uebersicht', onclick: () => { offeneKarte = null; adresse(null, false); zeichneErklaeren(); window.scrollTo(0, 0); } }, '‹ Übersicht'),
      el('article', { class: 'lr-karte-box lr-lernkarte' },
        el('div', { class: 'lr-lernkarte-kopf' }, el('h3', {}, `${e.nr} · ${e.titel}`), el('span', { class: 'lr-lk-status' }, lernPunkte(e), el('small', {}, lernKartenStatus(e)))),
        e.regel ? lernErklaerung(e, { kurzGesagt: kurzOben }) : el('p', { class: 'lr-leise' }, 'Für diese Karte gibt es noch keine Erklärung.'),
        e.aufgaben.length ? el('button', { type: 'button', class: 'lr-knopf lr-dazu', onclick: () => { erklGesehen.add(e.lernziel); zeige('ueben', { karte: e }); } }, 'Jetzt du ›') : null,
        ctx.leitung ? lernAnmerkung({ einheit_id: ctx.einheit, lernziel: e.lernziel, lernender_id: ctx.kind }, 'Anmerkung zu dieser Erklärung') : null),
      naechste ? el('button', { type: 'button', class: 'lr-knopf-zweit lr-naechste-karte', onclick: () => { offeneKarte = naechste; adresse(naechste, true); zeichneErklaeren(); window.scrollTo(0, 0); } }, `Nächste Karte: ${naechste.titel} ›`) : null);
  };
  zeichneErklaeren();

  // --- Typische Fehler
  const versucht = etappen.flatMap((e) => e.aufgaben.filter((a) => a.versuche && !a.geloest).map((a) => ({ e, a })));
  lernAnhaengen(panels.fehler, 
    el('p', { class: 'lr-leise' }, 'Die Stellen, an denen es oft schiefgeht.'),
    ...(fehlerKarten.length ? fehlerKarten.map((e) => el('article', { class: 'lr-karte-box lr-fehlerkarte' },
      el('h3', {}, `${e.nr} · ${e.titel}`), el('div', { class: 'lr-fehler' }, el('b', {}, 'Achtung: '), ...lernMarkiert(e.fehler)),
      el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { offeneKarte = e; zeichneErklaeren(); zeige('erklaeren'); adresse(e, false); } }, 'Erklärung ansehen'))) : [el('p', { class: 'lr-leise' }, 'Für dieses Thema sind noch keine typischen Fehler eingetragen.')]),
    versucht.length ? el('section', { class: 'lr-karte-box' }, el('h3', {}, `Hat bei dir noch nicht geklappt (${versucht.length})`),
      el('ul', { class: 'lr-meinefehler' }, ...versucht.slice(0, 8).map(({ e, a }) => el('li', {}, el('span', {}, lernText(a.frage?.text || '')),
        el('button', { type: 'button', class: 'lr-knopf-zweit lr-knopf-klein', onclick: () => zeige('ueben', { karte: e }) }, 'Üben'))))) : null);

  // --- Üben: eine Lernkarte, Aufgaben nacheinander; Erklärung klappt an der Aufgabe auf
  let aktKarte = null, stufe = 0;
  const erklGesehen = new Set(); // Karten, deren Erklärung das Kind in dieser Sitzung schon vor sich hatte
  let gezeichnet = null;
  const uebenOeffnen = (karte) => {
    if (karte && karte !== aktKarte) { aktKarte = karte; stufe = 0; }
    if (!aktKarte) aktKarte = (karteNr && etappen[karteNr - 1]) || empfohlen();
    if (gezeichnet !== aktKarte) zeichneUeben(); // sonst bleibt Aufgabe samt Rückmeldung stehen
  };
  const zeichneUeben = () => {
    const e = aktKarte; gezeichnet = e;
    const mitAufg = etappen.filter((x) => x.aufgaben.length); const pos = mitAufg.indexOf(e);
    const wechsel = (d) => el('button', { type: 'button', class: 'lr-pfeilknopf', 'aria-label': d < 0 ? 'Vorige Lernkarte' : 'Nächste Lernkarte', disabled: !mitAufg[pos + d],
      onclick: () => { aktKarte = mitAufg[pos + d]; stufe = 0; zeichneUeben(); } }, d < 0 ? '‹' : '›');
    const stufenDa = [1, 2, 3].filter((n) => e.aufgaben.some((a) => a.stufe === n));
    const chipsStufe = stufenDa.length > 1 ? el('div', { class: 'lr-chips lr-chips-klein', role: 'group', 'aria-label': 'Stufe' },
      ...[[0, 'alle'], [1, 'leicht'], [2, 'mittel'], [3, 'schwer']].filter(([n]) => !n || stufenDa.includes(n))
        .map(([n, t]) => el('button', { type: 'button', class: stufe === n ? 'on' : '', 'aria-pressed': String(stufe === n), onclick: () => { stufe = n; zeichneUeben(); } }, t))) : null;
    const punkte = el('div', { class: 'lr-lk-punkte' });
    const zeichnePunkte = () => lernErsetze(punkte, lernPunkte(e, { gross: true }),
      el('small', {}, e.sitzt || e.fertig ? (e.faellig ? 'Sitzt – heute wiederholen' : 'Sitzt! Du kannst trotzdem weiterüben.') : `${Math.min(e.serie, e.ziel)} von ${e.ziel} richtig hintereinander`));
    zeichnePunkte();
    const flaeche = el('div', { class: 'lr-ueben-flaeche' });
    lernErsetze(panels.ueben, el('div', { class: 'lr-karte-box lr-lk-kopf' }, wechsel(-1),
      el('div', { class: 'lr-lk-mitte' }, el('small', { class: 'lr-leise' }, neu ? `Karte ${pos + 1}/${mitAufg.length} · ${e.titel}` : `Lernkarte ${pos + 1} von ${mitAufg.length}`), neu ? null : el('b', {}, e.titel), punkte), wechsel(1)), flaeche, chipsStufe);
    if (!pflicht.some((x) => !x.fertig) && !e.faellig) // alle Lernkarten sitzen: nicht endlos weiterüben lassen, sondern den Test anbieten
      panels.ueben.prepend(el('div', { class: 'lr-karte-box lr-testbereit' }, el('p', {}, el('b', {}, 'Alle Lernkarten dieses Themas sitzen. '), 'Du musst hier nicht weiterüben – als Nächstes kommt der Test.'), lernTestTeil(ctx, etappen)));
    const pool = e.aufgaben.filter((a) => !stufe || a.stufe === stufe);
    const warte = [...pool].sort((a, b) => (a.geloest === b.geloest ? 0 : a.geloest ? 1 : -1) || (a.versuche || 0) - (b.versuche || 0) || (a.stufe || 2) - (b.stufe || 2));
    let sterne = 0, nr = 0, fehlFolge = 0; // fehlFolge: falsche Aufgaben hintereinander auf dieser Karte (V8)
    const naechsteKarte = etappen.slice(e.nr).find((x) => !x.fertig && x.aufgaben.length) || etappen.find((x) => x !== e && !x.fertig && x.aufgaben.length);
    const zeigeAufgabe = () => {
      const a = warte[0];
      if (!a) { lernErsetze(flaeche, el('p', { class: 'lr-leise' }, 'Für diese Auswahl gibt es keine Aufgaben.')); return; }
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
              el('p', {}, LERN_GRUND[r.grund] || (a.tipp ? 'Tipp: ' + lernText(a.tipp) : 'Lies die Aufgabe noch einmal genau und prüfe deine Rechnung.'))));
            if (!LERN_GRUND[r.grund] && a.tipp) tipp?.remove();
            meldung.scrollIntoView?.({ block: 'nearest', behavior: 'smooth' });
            return;
          }
          auf.sperren(); a.loesung = r.loesung; warte.shift(); a.versuche = (a.versuche || 0) + 1;
          const sterneVor = sterne;
          if (r.richtig) { if (!a.geloest && !r.wiederholt) sterne += 10; a.geloest = true; warte.push(a); }
          else { // V5: gemerkte Lösung zählt nicht – nach einem Fehler kommt eine andere Aufgabe derselben Stufe; dieselbe erst ganz am Ende
            warte.push(a);
            const j = warte.findIndex((x) => x !== a && !x.geloest && (x.stufe || 2) === (a.stufe || 2) && !x.falschHeute);
            if (j > 0) warte.unshift(...warte.splice(j, 1));
            a.falschHeute = true;
          }
          auf.zeigeLoesung(r.loesung); fehlFolge = r.richtig ? 0 : fehlFolge + 1;
          const warSitzt = e.sitzt;
          if (r.karte) { e.serie = r.karte.serie; e.ziel = r.karte.ziel; e.sitzt = r.karte.sitzt; e.fertig = e.fertig || r.karte.sitzt; if (warSitzt && r.karte.sitzt) e.faellig = false; }
          zeichnePunkte(); zeichneFortschritt();
          const jetztSitzt = !!r.karte?.neu_sitzt || (!warSitzt && e.sitzt);
          const weiter = el('button', { type: 'button', class: 'lr-knopf lr-weiter', onclick: () => { zeigeAufgabe(); window.scrollTo(0, 0); } }, neu ? 'Neue Bordkarte ›' : 'Nächste Aufgabe');
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
              e.fehler ? el('div', { class: 'lr-fehler lr-detektiv' }, el('p', { class: 'lr-ueber' }, 'IST DIR DAS PASSIERT?'), el('p', {}, ...lernMarkiert(e.fehler))) : null)
            : el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, 'Noch nicht. Richtig ist: ' + lernLoesungText(a)),
              a.antworttyp === 'luecken' && lernIstTermVorlage(a.frage?.schablone) && lernGleichwertigAusgeklammert(a.frage?.schablone, w.werte, r.loesung?.werte)
                ? el('p', {}, 'Dein Term ist gleichwertig, aber noch nicht vollständig ausgeklammert: Vor die Klammer gehört der größte gemeinsame Faktor.') : null,
              r.loesungsweg ? el('p', {}, el('b', {}, 'So geht’s: '), lernText(r.loesungsweg)) : null,
              e.fehler ? el('div', { class: 'lr-fehler lr-detektiv' }, el('p', { class: 'lr-ueber' }, 'FEHLER-DETEKTIV: IST DIR DAS PASSIERT?'), el('p', {}, ...lernMarkiert(e.fehler))) : null,
              el('p', { class: 'lr-leise' }, 'Die Punkte fangen wieder bei 0 an. Die Erklärung steht aufgeklappt bei der Aufgabe.')));
          if (!r.richtig) {
            if (LERN_GRUND[r.grund]) meldung.firstElementChild?.prepend(el('p', { class: 'lr-grund' }, LERN_GRUND[r.grund])); // V3
            if (fehlFolge >= 2) { // V8: nach 2 Fehlern in Folge ein anderer Weg, nach 3 der Hinweis auf die Eltern
              const leichter = (a.stufe || 2) > 1 ? warte.find((x) => !x.geloest && !x.falschHeute && (x.stufe || 2) < (a.stufe || 2)) : null;
              lernAnhaengen(meldung.firstElementChild, el('div', { class: 'lr-andererweg' }, el('p', {}, el('b', {}, 'Das hakt gerade. '), 'Probier einen anderen Weg:'),
                el('div', { class: 'lr-knopfzeile' },
                  leichter ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { warte.splice(warte.indexOf(leichter), 1); warte.unshift(leichter); zeigeAufgabe(); window.scrollTo(0, 0); } }, 'Leichtere Aufgabe') : null,
                  erkl ? el('button', { type: 'button', class: 'lr-knopf-zweit', onclick: () => { if (erkl.getAttribute('aria-expanded') !== 'true') erkl.click(); erklBox.scrollIntoView?.({ block: 'start', behavior: 'smooth' }); } }, 'Beispiel ansehen') : null),
                fehlFolge >= 3 ? el('p', { class: 'lr-leise' }, 'Frag Mama oder Papa – sie sehen im Lernstand, wo es hakt.') : null));
            }
          }
          if (jetztSitzt && neu) {
            lernErsetze(flaeche, el('section', { class: 'lr-gelandet' },
              el('p', { class: 'lr-ueber' }, `KARTE ${pos + 1} VON ${mitAufg.length}`),
              el('div', { class: 'lr-landestempel', 'aria-hidden': 'true' }, el('b', {}, 'GELANDET'), el('small', {}, ortCode)),
              el('h2', {}, e.titel, ' ✓'), el('p', {}, `${e.ziel || 2}-mal hintereinander richtig.`),
              sterne ? el('p', { class: 'lr-sterne-neu' }, lernIcon(LI.stern, 20), ` +${sterne} Sterne`) : null,
              el('p', { class: 'lr-leise' }, 'Die Karte kommt in ein paar Tagen zum Wiederholen.'),
              naechsteKarte ? el('button', { type: 'button', class: 'lr-knopf', onclick: () => { aktKarte = naechsteKarte; stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } }, `Anschlussflug: ${naechsteKarte.titel} ›`) : null,
              !naechsteKarte && !pflicht.some((x) => !x.fertig) ? lernTestTeil(ctx, etappen) : null,
              el('a', { class: 'lr-knopf-zweit', href: `#/reise/${ctx.kind}` }, 'Zur Abflugtafel'),
              el('a', { class: 'lr-textlink', href: `#/wiederholen/${ctx.kind}` }, 'Wiederholungen ansehen, falls noch welche offen sind')));
            window.scrollTo(0, 0); flaeche.querySelector('.lr-knopf, .lr-knopf-zweit')?.focus({ preventScroll: true });
            return;
          }
          if (neu) { meldung.scrollIntoView?.({ block: 'center', behavior: 'smooth' }); return; }
          if (jetztSitzt) lernAnhaengen(meldung, el('section', { class: 'lr-geschafft lr-sitzt' },
            el('div', { class: 'lr-geschafft-haken' }, lernIcon(LI.haken, 48)),
            el('p', { class: 'lr-ueber' }, 'LERNKARTE SITZT'), el('h2', {}, e.titel),
            sterne ? el('p', { class: 'lr-sterne-neu' }, lernIcon(LI.stern, 20), ` +${sterne} Sterne`) : null,
            el('p', { class: 'lr-leise' }, 'Sie kommt in ein paar Tagen zum Wiederholen.'),
            naechsteKarte ? el('button', { type: 'button', class: 'lr-knopf', onclick: () => { aktKarte = naechsteKarte; stufe = 0; zeichneUeben(); window.scrollTo(0, 0); } }, `Nächste Karte: ${naechsteKarte.titel}`)
              : el('button', { type: 'button', class: 'lr-knopf', onclick: () => zeige('erklaeren') }, 'Zur Themen-Übersicht')));
          (jetztSitzt ? meldung : weiter).scrollIntoView?.({ block: 'center', behavior: 'smooth' });
        } catch (err) { lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
      });
      const fein = window.matchMedia?.('(pointer: fine)').matches;
      auf.node.addEventListener('keydown', (ev) => { if (ev.key === 'Enter' && ev.target.tagName === 'INPUT') { ev.preventDefault(); if (pruefen.isConnected) pruefen.click(); } });
      if (neu) {
        lernErsetze(dock, auf.tasten ? lernTastenfeld(auf.tasten, pruefen) : pruefen);
        lernErsetze(flaeche, erkl, erklBox,
          el('section', { class: 'lr-karte-box lr-aufgabe lr-bordkarte' },
            el('div', { class: 'lr-bord-kopf' }, el('span', {}, `BORDKARTE ${nr} · ${ortCode}`), el('span', {}, a.stufe ? ['', 'LEICHT', 'MITTEL', 'SCHWER'][a.stufe] || '' : '')),
            auf.node, el('div', { class: 'lr-perforation', 'aria-hidden': 'true' }),
            tipp ? el('div', { class: 'lr-knopfzeile' }, tipp) : null),
          hilfeBox, meldung,
          ctx.leitung ? lernAnmerkung({ einheit_id: ctx.einheit, lernziel: e.lernziel, aufgabe_id: a.id, lernender_id: ctx.kind }, 'Anmerkung zu dieser Aufgabe') : null, dock);
      } else lernErsetze(flaeche,
        erkl, erklBox,
        el('section', { class: 'lr-karte-box lr-aufgabe' },
          el('p', { class: 'lr-ueber' }, `AUFGABE ${nr}` + (a.stufe ? ` · ${['', 'LEICHT', 'MITTEL', 'SCHWER'][a.stufe] || ''}` : '')), auf.node,
          pruefen, tipp ? el('div', { class: 'lr-knopfzeile' }, tipp) : null),
        hilfeBox, meldung,
        ctx.leitung ? lernAnmerkung({ einheit_id: ctx.einheit, lernziel: e.lernziel, aufgabe_id: a.id, lernender_id: ctx.kind }, 'Anmerkung zu dieser Aufgabe') : null);
      if (fein && (!neuHier || breit)) auf.node.querySelector('input')?.focus({ preventScroll: true });
    };
    zeigeAufgabe();
  };

  const flaeche = el('div', { class: 'lr-thema' },
    neu ? el('header', { class: 'lr-flugkopf' },
      el('a', { class: 'lr-x', href: `#/reise/${ctx.kind}`, 'aria-label': 'Thema schließen' }, '✕'),
      el('div', { class: 'lr-flugkopf-text' }, el('small', {}, ortCode + (lernJahrgangText(ctx.ort.jahrgang) ? ' · ' + lernJahrgangText(ctx.ort.jahrgang) : '')), el('h1', {}, ctx.titelKurz)))
    : el('header', { class: 'lr-kopf' },
      el('p', { class: 'lr-pfad' }, el('a', { href: `#/reise/${ctx.kind}` }, 'Heute'), ` › ${ctx.ort.stadt || 'Thema'}`),
      el('h1', { class: 'lr-titel' }, ctx.titelKurz),
      lernJahrgangText(ctx.ort.jahrgang) ? el('p', { class: 'lr-leise lr-jahrgang' }, lernJahrgangText(ctx.ort.jahrgang)) : null),
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
function lernJahrgangText(j) {
  if (!j || !Object.keys(j).length) return '';
  return [['gym_by', 'Gym'], ['rs_by', 'RS'], ['ib_myp', 'IB']].filter(([k]) => j[k]).map(([k, t]) => `${t} ${j[k]}`).join(' · ');
}

function lernEinheitTest(ctx) {
  const body = el('div', { class: 'lern-body' });
  lernErsetze(main, lernRahmen(ctx.kindObj, 'weg',
    el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-ueber' }, 'TEST'), el('h1', { class: 'lr-titel' }, ctx.titel)),
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

// ---------- Kind: Mein Weg ----------
async function viewWeg(arg) {
  setChrome('Mein Weg', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const d = await lernLadeKind(arg);
  if (!d || !live()) return;
  const merk = await lernMerkDaten(d).catch(() => []);
  if (!live()) return;
  const { kind } = d;
  $('#title').textContent = 'Mein Weg';
  const mm = new Map(merk.map((m) => [m.einheit_id, m]));
  const kann = d.orte.filter((o) => o.zustand === 'fertig' || o.zustand === 'kann');
  const offen = d.orte.filter((o) => o.zustand === 'offen');
  const passt = offen.filter((o) => !o.ziel_klasse || !kind.klasse || o.ziel_klasse <= kind.klasse);
  const zahl = (w, t, cls) => el('div', { class: 'lr-zahl ' + (cls || '') }, el('b', {}, String(w)), el('span', {}, t));
  const dran = d.jetzt.map((e) => {
    const { n, f } = lernEtappenZahl(mm.get(e.id));
    const info = e.laeuft ? 'Test läuft' : e.blocktest ? 'Test geschrieben' : n ? (f >= n ? 'Test offen' : `Etappe ${f + 1}/${n}`) : `${e.fertig}/${e.n}`;
    return el('a', { class: 'lr-dran', href: `#/lerneinheit/${kind.id}-${e.id}` },
      el('div', { class: 'lr-dran-kopf' }, el('b', {}, `${e.stadt}: ${e.ort_titel || e.titel}`), el('span', {}, info + ' ›')),
      el('small', {}, `${e.kontinent || ''} · Kl. ${e.ziel_klasse || '–'}`),
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
  lernErsetze(main, lernRahmen(kind, 'weg',
    el('header', { class: 'lr-kopf' }, el('p', { class: 'lr-ueber' }, `MATHE${kind.klasse ? ' · KLASSE ' + kind.klasse : ''}`), el('h1', { class: 'lr-titel' }, 'Mein Weg')),
    el('div', { class: 'lr-zahlen' }, zahl(kann.length, 'kann ich', 'gut'), zahl(d.jetzt.length, 'gerade dran'), zahl(offen.length, 'kommen noch')),
    el('h2', { class: 'lr-abschnitt lr-abschnitt-jetzt' }, 'GERADE DRAN'),
    ...(dran.length ? dran : [el('p', { class: 'lr-leise' }, 'Gerade ist nichts offen.')]),
    el('h2', { class: 'lr-abschnitt' }, `KOMMT NOCH${kind.klasse ? ' · BIS KLASSE ' + kind.klasse : ''}`),
    passt.length ? el('div', { class: 'lr-wegliste' }, ...passt.slice(0, 5).map((o) => ortZeile(o, o.hat_einheit ? 'bereit' : 'bald'))) : el('p', { class: 'lr-leise' }, 'Für deine Klasse ist alles verteilt.'),
    passt.length > 5 || offen.length > passt.length ? el('details', { class: 'lr-mehr' }, el('summary', {}, `Alle weiteren Orte (${offen.length - Math.min(5, passt.length)})`),
      el('div', { class: 'lr-wegliste' }, ...[...passt.slice(5), ...offen.filter((o) => !passt.includes(o))].map((o) => ortZeile(o, o.ziel_klasse ? 'Kl. ' + o.ziel_klasse : '')))) : null,
    el('h2', { class: 'lr-abschnitt' }, 'KANN ICH'),
    kannZeilen.length ? el('div', { class: 'lr-wegliste' }, ...kannZeilen.slice(0, 6)) : el('p', { class: 'lr-leise' }, 'Dein erster geschaffter Ort erscheint hier.'),
    kannZeilen.length > 6 ? el('details', { class: 'lr-mehr' }, el('summary', {}, `Alle ${kannZeilen.length} anzeigen`), el('div', { class: 'lr-wegliste' }, ...kannZeilen.slice(6))) : null,
    el('a', { class: 'lr-zeile', href: `#/reisepass/${kind.id}` }, el('span', { class: 'lr-zeile-icon' }, lernIcon(LI.pass, 22)),
      el('span', { class: 'lr-zeile-text' }, el('b', {}, 'Reisepass'), el('small', {}, `${d.konto?.stempel ?? 0} Stempel · ${lernZahl(d.konto?.sterne ?? 0)} Sterne · Belohnungen · Look`)), lernIcon(LI.pfeil, 20))));
}

// ---------- Kind: Merkheft ----------
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
  // Einträge: alle Lernkarten der Orte, die gerade dran oder geschafft sind – zum Nachlesen, ohne etwas zu lösen.
  const sichtbar = new Set([...d.jetzt, ...d.kann, ...d.frueher].map((e) => e.id));
  const eintraege = [];
  for (const m of merk) if (sichtbar.has(m.einheit_id)) (m.etappen || []).forEach((e, i) => {
    const k = m.stand?.[e.lernziel] || {};
    eintraege.push({ m, e, nr: i + 1, status: lernKartenStatus({ ...k, serie: Number(k.serie || 0) }) });
  });
  const suche = el('input', { type: 'search', class: 'lr-suche', placeholder: 'Suchen, z. B. runden', 'aria-label': 'Merkheft durchsuchen', autocomplete: 'off' });
  const liste = el('div', { class: 'lr-merkliste' });
  const norm = (s) => String(s || '').toLowerCase();
  const zeichne = () => {
    const q = norm(suche.value.trim());
    const treffer = eintraege.filter(({ m, e }) => !q || [e.titel, e.regel, ...(e.schritte || []).map((x) => (typeof x === 'string' ? x : x?.text)), e.fehler, m.stadt, m.ort_titel].some((t) => norm(t).includes(q)));
    if (!eintraege.length) { lernErsetze(liste, el('p', { class: 'lr-leise' }, 'Noch leer.')); return; }
    if (!treffer.length) { lernErsetze(liste, el('p', { class: 'lr-leise' }, 'Nichts gefunden.')); return; }
    const gruppen = new Map();
    for (const t of treffer) { if (!gruppen.has(t.m.einheit_id)) gruppen.set(t.m.einheit_id, []); gruppen.get(t.m.einheit_id).push(t); }
    lernErsetze(liste, ...[...gruppen.values()].map((ts) => el('section', { class: 'lr-merkgruppe' },
      el('h2', { class: 'lr-abschnitt' }, `${ts[0].m.stadt || ''} · ${ts[0].m.ort_titel || ''}`.toUpperCase()),
      ...ts.map(({ m, e, nr, status }) => el('details', { class: 'lr-merk', ...(q && treffer.length <= 3 ? { open: '' } : {}) },
        el('summary', {}, el('b', {}, e.titel), el('small', { class: 'lr-merk-status' }, status), lernIcon(LI.pfeil, 18)),
        el('div', { class: 'lr-merk-inhalt' }, lernErklaerung(e),
          el('a', { class: 'lr-knopf lr-knopf-klein', href: `#/lerneinheit/${kind.id}-${m.einheit_id}-ueben-${nr}` }, 'Üben')))))));
  };
  suche.addEventListener('input', zeichne);
  zeichne();
  lernErsetze(main, lernRahmen(kind, 'merkheft',
    el('header', { class: 'lr-kopf' }, el('h1', { class: 'lr-titel' }, 'Merkheft'), el('p', { class: 'lr-leise' }, 'Alle Erklärungen zum Nachlesen – jederzeit, ohne Aufgaben zu lösen.')),
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
          : r.grund === 'erst_korrektur' ? 'Erst die Lernziele mit „noch üben“ verbessern, dann kommt der Nachtest.'
          : r.grund === 'vorrat_erschoepft' ? 'Für ' + (r.vorrat_erschoepft || []).map(lernZielName).join(', ') + ' gibt es gerade keine neue Aufgabe. Sag Bescheid, dann kommen neue dazu.'
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
    if (!blockFertig) lernAnhaengen(box, knopf('Test', 'blocktest', 'Eine Aufgabe je Lernziel, ohne Tipps. Die Lösungen siehst du nach dem Abgeben.'));
    if (hatFehler) lernAnhaengen(box, knopf('Verbessern', 'korrektur', 'Nur die Lernziele, die noch nicht geklappt haben – mit neuen Aufgaben. Übe sie vorher noch einmal.'));
    if (nt.grund === 'faellig') lernAnhaengen(box, knopf(lernNtTitel(nt), 'nachtest',
      'Alle Lernziele der Einheit, ohne Tipps. Ab 80 % zählt die Runde. Unter 60 % geht es auf eine Rückreise zu diesem Ort.'));
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
          lernErsetze(meldung, el('div', { class: 'lr-rueck lr-rueck-falsch' }, el('b', {}, fehlt === 1 ? 'Eine Aufgabe ist noch leer.' : `${fehlt} Aufgaben sind noch leer.`),
            el('p', {}, 'Leere Aufgaben zählen als falsch.'),
            el('div', { class: 'row' }, el('button', { type: 'button', class: 'primary', onclick: () => { i = erste; zeige(); } }, `Zu Aufgabe ${erste + 1}`),
              el('button', { type: 'button', class: 'secondary', onclick: () => { abgeben.dataset.sicher = '1'; abgeben.click(); } }, 'Trotzdem abgeben'))));
          return;
        }
        abgeben.disabled = true;
        const r = await lernCall('schule_test_abschliessen', { lernender_id: ctx.kind, sitzung_id: t.sitzung_id });
        if (ctx.live()) lernTestErgebnis(ctx, box, r);
      } catch (e) { abgeben.disabled = false; lernErsetze(meldung, el('p', { class: 'err-text' }, e.message)); }
    } }, 'Abgeben');
    lernErsetze(box, el('div', { class: 'card' },
      el('p', { class: 'eyebrow' }, `${art} · Aufgabe ${i + 1} von ${aufg.length} · ${gesendet.size} beantwortet`),
      el('div', { class: 'lern-punkte' }, aufg.map((x, j) => el('button', { type: 'button', class: (j === i ? 'on ' : '') + (gesendet.has(x.id) ? 'fertig' : ''), 'aria-label': `Aufgabe ${j + 1}`, onclick: () => { i = j; geh(0); } }, String(j + 1)))),
      auf.node, meldung,
      el('div', { class: 'row lern-knoepfe' },
        el('button', { type: 'button', class: 'secondary', disabled: i === 0, onclick: () => geh(-1) }, '‹ Zurück'),
        i < aufg.length - 1 ? el('button', { type: 'button', class: 'primary', onclick: () => geh(1) }, 'Weiter ›') : abgeben),
      i < aufg.length - 1 ? el('p', { class: 'small muted' }, 'Abgeben kannst du bei der letzten Aufgabe. Bis dahin kannst du Antworten ändern.') : null));
  };
  zeige();
}

function lernTestErgebnis(ctx, box, r) {
  const ort = r.ort || {};
  lernErsetze(box, 
    el('div', { class: 'card lern-ergebnis' },
      el('h3', {}, `${r.richtig} von ${r.gesamt} richtig`),
      r.einheit_abgeschlossen ? el('p', { class: 'lern-rueck ok' }, el('b', {}, 'Einheit geschafft! 🎉')) : el('p', { class: 'small' }, 'Bei „noch üben“: die passenden Etappen noch einmal üben, dann „Verbessern“.'),
      r.nachtest_ergebnis ? el('p', { class: 'lern-rueck ' + (r.nachtest_ergebnis === 'bestanden' ? 'ok' : 'falsch') }, el('b', {}, {
        bestanden: r.nachtest?.folgerunde && r.nachtest_runde >= 3 ? 'Nachtest geschafft (ab 80 %).' : `Nachtest-Runde ${r.nachtest_runde} geschafft (ab 80 %).`,
        wiederholen: 'Unter 80 %: Diese Runde zählt noch nicht. Verbessere die falschen Lernziele, dann kommt der Nachtest noch einmal.',
        rueckreise: 'Unter 60 %: Rückreise zu diesem Ort. Erst üben und verbessern, dann den Nachtest wiederholen.' }[r.nachtest_ergebnis])) : null,
      ort.abgeschlossen ? el('div', { class: 'lr-stempel-gross' }, el('div', { class: 'lr-stempel', style: '--dreh:-8deg' }, el('b', {}, 'GESCHAFFT'), el('small', {}, 'Neuer Stempel')),
        el('p', {}, el('b', {}, 'Ort geschafft! Der Stempel ist jetzt in deinem Reisepass.'))) : null,
      lernStandZeile(r.lernziele)),
    ...(r.ergebnisse || []).map((x) => {
      const a = { ...x, antworttyp: x.antworttyp || (x.loesung?.werte ? 'luecken' : x.loesung?.index !== undefined ? (x.antworten ? 'auswahl' : 'markierung') : x.loesung?.text !== undefined ? 'text' : 'zahl') };
      return el('div', { class: 'card lern-rueck-karte ' + (x.richtig ? 'ok' : 'falsch') },
        el('p', { class: 'eyebrow' }, lernZielName(x.lernziel) + (x.richtig ? ' · ✓ richtig' : ' · ✗ falsch')),
        el('p', { class: 'lern-frage' }, lernText(x.frage?.text)),
        x.frage?.grafik ? (x.frage.grafik.typ && x.frage.grafik.typ !== 'zahlenstrahl' ? lernBild(x.frage.grafik) : lernZahlenstrahl(x.frage.grafik, false)) : null,
        el('p', { class: 'small' }, 'Deine Antwort: ', el('b', {}, lernAntwortText(a, x.antwort))),
        x.richtig ? null : el('p', { class: 'small' }, 'Richtig: ', el('b', {}, lernLoesungText(a))),
        x.loesungsweg && !x.richtig ? el('p', { class: 'small muted' }, x.loesungsweg) : null);
    }),
    el('div', { class: 'row lern-knoepfe' }, el('a', { class: 'btn primary', href: ctx.basis || `#/lerneinheit/${ctx.kind}-${ctx.einheit}` }, 'Zum Thema'),
      el('a', { class: 'btn secondary', href: `#/reise/${ctx.kind}` }, 'Zur Reise')));
}


// ---------- Eltern/Lehrer: Rückmeldungen, Themenplan, Zugänge ----------
const LERN_RM_ARTEN = [['thema_fehlt', 'Thema fehlt'], ['zu_ungenau', 'Zu ungenau'], ['mehr_aufgaben', 'Mehr Aufgaben'], ['schwieriger', 'Schwieriger'],
  ['leichter', 'Leichter'], ['erklaerung', 'Erklärung verbessern'], ['fehler', 'Fehler'], ['sonstiges', 'Sonstiges']];
const LERN_RM_STATUS = { offen: 'offen', in_arbeit: 'in Arbeit', erledigt: 'erledigt', abgelehnt: 'nicht umgesetzt' };

// Kleines Formular für Eltern/Lehrer: Anmerkung an die Entwicklung (Claude liest sie und antwortet).
function lernRueckmeldungForm(bezug, { offen = false, onGesendet } = {}) {
  let art = '';
  const chips = el('div', { class: 'lern-rm-arten', role: 'group', 'aria-label': 'Art der Anmerkung' },
    ...LERN_RM_ARTEN.map(([k, t]) => el('button', { type: 'button', class: 'lern-chip', 'aria-pressed': 'false', 'data-art': k, onclick: (ev) => {
      art = k; for (const b of chips.querySelectorAll('button')) b.setAttribute('aria-pressed', String(b === ev.currentTarget));
    } }, t)));
  const text = el('textarea', { rows: '3', maxlength: '4000', placeholder: 'Was soll anders werden? Je genauer, desto besser.', 'aria-label': 'Deine Anmerkung' });
  const status = el('p', { class: 'small muted', role: 'status' });
  const senden = el('button', { type: 'submit', class: 'primary' }, 'Senden');
  const form = el('form', { class: 'lern-rm-form' + (offen ? '' : ' lern-rm-zu') }, chips, text, el('div', { class: 'row' }, senden, status));
  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!text.value.trim()) { status.textContent = 'Bitte kurz beschreiben.'; return; }
    senden.disabled = true; status.textContent = 'Sende …';
    try {
      await lernCall('schule_rueckmeldung_geben', { ...bezug, art: art || 'sonstiges', text: text.value.trim() });
      text.value = ''; status.textContent = 'Danke – ist bei der Entwicklung angekommen.';
      if (onGesendet) onGesendet();
    } catch (err) { status.textContent = err.message; }
    senden.disabled = false;
  });
  return form;
}

function lernAnmerkung(bezug, label) {
  const box = el('details', { class: 'lern-anmerkung' }, el('summary', {}, '✎ ' + label), lernRueckmeldungForm(bezug, { offen: true }));
  return box;
}

async function viewRueckmeldungen() {
  setChrome('Rückmeldungen', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const r = await lernCall('schule_rueckmeldungen');
  if (!live()) return;
  const liste = r.rueckmeldungen || [];
  const artText = Object.fromEntries(LERN_RM_ARTEN);
  const karte = (x) => el('article', { class: 'card lern-rm ' + 'lern-rm-' + x.status },
    el('div', { class: 'lern-einheit-kopf' }, el('b', {}, artText[x.art] || x.art), el('span', { class: 'pill' + (x.status === 'erledigt' ? ' ok' : x.status === 'offen' ? ' wartet' : '') }, LERN_RM_STATUS[x.status] || x.status)),
    el('p', { class: 'small muted' }, [x.ort, x.lernziel ? 'Etappe: ' + (x.lernziel || '') : null, x.aufgabe ? 'Aufgabe: „' + x.aufgabe + '“' : null].filter(Boolean).join(' · ') || 'Allgemein'),
    el('p', { class: 'lern-rm-text' }, x.text),
    x.antwort ? el('p', { class: 'lern-rm-antwort' }, el('b', {}, 'Antwort: '), x.antwort) : null,
    el('p', { class: 'small muted' }, `${String(x.von || '').replace(/^[a-z]+:/, '')} · ${new Date(x.am).toLocaleDateString('de-DE')}`));
  lernErsetze(main, 
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'AN DIE ENTWICKLUNG'), el('h2', {}, 'Was soll besser werden?'),
      el('p', {}, 'Allgemeine Wünsche hier. Zu einer bestimmten Einheit, Erklärung oder Aufgabe geht es direkt dort über „✎ Anmerkung“ (am einfachsten über das Testkind, das alle Themen sieht).')),
    el('div', { class: 'card' }, lernRueckmeldungForm({}, { offen: true, onGesendet: () => setTimeout(render, 900) })),
    el('h3', {}, liste.length ? `Bisherige Rückmeldungen (${liste.length})` : 'Noch keine Rückmeldungen'),
    ...liste.map(karte));
}

async function viewPlan(arg) {
  setChrome('Themenplan', { back: true, showTabs: false });
  const live = viewGuard();
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return; }
  loading();
  const p = await lernCall('schule_plan_lesen', { lernender_id: kindId });
  if (!live()) return;
  $('#title').textContent = 'Themenplan ' + p.kind.name;
  const ortById = new Map((p.orte || []).map((o) => [o.block_id, o]));
  const normal = (p.plan || []).filter((r) => r.art === 'normal');
  const rueck = (p.plan || []).filter((r) => r.art === 'rueckreise');
  // Arbeitskopie: [{ block_id, kann_schon, status }]
  let plan = normal.map((r) => ({ block_id: r.block_id, kann_schon: r.kann_schon, status: r.status }));
  let geaendert = false;
  const status = el('p', { class: 'small muted', role: 'status' });
  const speichern = el('button', { type: 'button', class: 'primary', disabled: true }, 'Plan speichern');
  const liste = el('ol', { class: 'lern-plan' });
  const ortName = (o) => o ? `${o.stadt || o.titel}${o.stadt && o.titel !== o.stadt ? ' – ' + o.titel : ''}` : '?';
  const gymKl = (o) => Math.min(...(o?.themen || []).map((t) => t.jahrgang?.gym_by || 99));
  const standText = { erledigt: 'geschafft', laeuft: 'läuft', offen: 'noch nicht begonnen' };
  const themenListe = (o) => el('ul', { class: 'lern-plan-themen' }, ...(o?.themen || []).map((t) => {
    const z = lernInhaltZustand(t);
    return el('li', { class: 'lp-' + z.k },
      el('i', { class: 'lp-punkt', 'aria-hidden': 'true' }),
      el('span', {}, el('b', {}, t.titel), el('span', { class: 'lern-plan-jg' }, ' · ' + (lernJahrgangText(t.jahrgang) || 'ohne Lehrplan-Zuordnung'))),
      el('small', { class: 'muted' }, z.k === 'leer' ? 'noch kein Inhalt' : z.k === 'pruefung' ? 'Inhalt in Prüfung' : (standText[t.stand] || 'Inhalt fertig')),
      t.einheit ? el('a', { class: 'small', href: `#/inhalte/${t.einheit.id}` }, 'ansehen') : null);
  }));
  const markiere = () => { geaendert = true; speichern.disabled = false; status.textContent = 'Nicht gespeichert.'; };
  const zeichne = () => {
    lernErsetze(liste, ...plan.map((x, i) => {
      const o = ortById.get(x.block_id);
      const ganzHoch = el('button', { type: 'button', class: 'iconbtn', 'aria-label': `${ortName(o)} nach ganz oben`, title: 'nach ganz oben', disabled: i === 0, onclick: () => { plan.unshift(...plan.splice(i, 1)); markiere(); zeichne(); } }, '⤒');
      const hoch = el('button', { type: 'button', class: 'iconbtn', 'aria-label': `${ortName(o)} nach oben`, disabled: i === 0, onclick: () => { [plan[i - 1], plan[i]] = [plan[i], plan[i - 1]]; markiere(); zeichne(); } }, '↑');
      const runter = el('button', { type: 'button', class: 'iconbtn', 'aria-label': `${ortName(o)} nach unten`, disabled: i === plan.length - 1, onclick: () => { [plan[i + 1], plan[i]] = [plan[i], plan[i + 1]]; markiere(); zeichne(); } }, '↓');
      const kann = el('label', { class: 'lern-plan-kann' }, el('input', { type: 'checkbox', checked: !!x.kann_schon, onchange: (ev) => { x.kann_schon = ev.target.checked; markiere(); } }), ' kann es schon');
      const weg = el('button', { type: 'button', class: 'lern-plan-weg', 'aria-label': `${ortName(o)} aus dem Plan nehmen`, onclick: () => { plan.splice(i, 1); markiere(); zeichne(); zeichneVorrat(); } }, 'Entfernen');
      return el('li', { class: 'lern-plan-zeile' + (x.status === 'fertig' ? ' fertig' : '') },
        el('span', { class: 'lern-plan-nr' }, String(i + 1)),
        el('div', { class: 'lern-plan-text' }, el('b', {}, ortName(o)), el('small', {}, [o?.kontinent, x.status === 'fertig' ? 'geschafft' : null].filter(Boolean).join(' · ')),
          themenListe(o)),
        el('div', { class: 'lern-plan-knoepfe' }, ganzHoch, hoch, runter, kann, weg));
    }));
    if (!plan.length) lernAnhaengen(liste, el('li', { class: 'muted' }, 'Der Plan ist leer. Ohne Plan sieht das Kind alle Themen. Füge unten Themen hinzu.'));
  };
  const suche = el('input', { type: 'search', placeholder: 'Thema oder Ort suchen …', 'aria-label': 'Thema suchen' });
  const nurMitEinheit = el('input', { type: 'checkbox' });
  const vorrat = el('div', { class: 'lern-plan-vorrat' });
  const zeichneVorrat = () => {
    const q = suche.value.trim().toLowerCase();
    const drin = new Set(plan.map((x) => x.block_id));
    const treffer = (p.orte || []).filter((o) => !drin.has(o.block_id) && (o.themen || []).length && (!nurMitEinheit.checked || o.themen.some((t) => t.einheit))
      && (!q || `${o.stadt} ${o.titel} ${o.kontinent} ${(o.themen || []).map((t) => t.titel).join(' ')}`.toLowerCase().includes(q)));
    const gruppen = new Map();
    for (const o of treffer.sort((a, b) => gymKl(a) - gymKl(b))) { const g = gymKl(o); if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(o); }
    const kk = p.kind.klasse;
    lernErsetze(vorrat, ...[...gruppen].map(([g, os]) => el('details', { open: !!q || g === kk },
      el('summary', {}, `${g === 99 ? 'Nicht im Gymnasium-Lehrplan' : `Gymnasium Klasse ${g}`}${g === kk ? ` – ${p.kind.name}s Klasse` : ''} (${os.length} ${os.length === 1 ? 'Ort' : 'Orte'})`),
      el('ul', { class: 'lern-plan-auswahl' }, ...os.map((o) => el('li', {},
        el('button', { type: 'button', class: 'lern-chip', onclick: () => { plan.push({ block_id: o.block_id, kann_schon: false, status: 'offen' }); markiere(); zeichne(); zeichneVorrat(); } }, '+ ' + ortName(o)),
        themenListe(o)))))));
    if (!treffer.length) lernAnhaengen(vorrat, el('p', { class: 'muted small' }, 'Nichts gefunden.'));
  };
  suche.addEventListener('input', zeichneVorrat); nurMitEinheit.addEventListener('change', zeichneVorrat);
  speichern.addEventListener('click', async () => {
    speichern.disabled = true; status.textContent = 'Speichere …';
    try {
      await lernCall('schule_plan_setzen', { lernender_id: kindId, revision: p.revision, eintraege: plan.map((x) => ({ block_id: x.block_id, kann_schon: !!x.kann_schon })) });
      geaendert = false; status.textContent = 'Gespeichert.'; setTimeout(render, 700);
    } catch (err) { status.textContent = err.message; speichern.disabled = false; }
  });
  const notiz = el('textarea', { rows: '2', maxlength: '2000', placeholder: 'Notiz zum Kind (z. B. Prüfung am …, braucht mehr Zeit bei …)', 'aria-label': 'Notiz' });
  const notizStatus = el('span', { class: 'small muted', role: 'status' });
  const notizForm = el('form', { class: 'lern-rm-form' }, notiz, el('div', { class: 'row' }, el('button', { type: 'submit', class: 'secondary' }, 'Notiz speichern'), notizStatus));
  notizForm.addEventListener('submit', async (ev) => {
    ev.preventDefault(); if (!notiz.value.trim()) return;
    try { await lernCall('schule_notiz_setzen', { lernender_id: kindId, text: notiz.value.trim() }); notizStatus.textContent = 'Gespeichert.'; setTimeout(render, 700); }
    catch (err) { notizStatus.textContent = err.message; }
  });
  zeichne(); zeichneVorrat();
  const klIn = el('input', { type: 'number', min: '1', max: '13', value: p.kind.klasse || '', inputmode: 'numeric', 'aria-label': 'Klasse' });
  const kindStatus = el('span', { class: 'small muted', role: 'status' });
  const kindForm = el('form', { class: 'card lp-kindform' }, el('h3', {}, 'Klasse'), el('div', { class: 'row' }, klIn,
    el('button', { type: 'submit', class: 'secondary' }, 'Speichern'), kindStatus),
    el('p', { class: 'small muted' }, 'Gymnasium. Bestimmt, welche Themen beim Kind als „seine Klasse“ zählen.'));
  kindForm.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    try { await lernCall('schule_kind_setzen', { lernender_id: kindId, klasse: Number(klIn.value) || null }); kindStatus.textContent = 'Gespeichert.'; setTimeout(render, 700); }
    catch (err) { kindStatus.textContent = err.message; }
  });
  lernErsetze(main, ...[
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, `THEMENPLAN · GYMNASIUM KLASSE ${p.kind.klasse || '?'}`), el('h2', {}, p.kind.name),
      el('p', {}, 'Reihenfolge = Reihenfolge in der Lernreise. Hinter jedem Thema steht, in welcher Klasse es laut Lehrplan dran ist (Gym = Gymnasium, RS = Realschule, IB = MYP-Jahr). Punkt: grün = Inhalt fertig, gelb = in Prüfung, grau = noch kein Inhalt.')),
    el('p', { class: 'small' }, el('a', { href: '#/lehrplan' }, 'Welche Themen gibt es für welche Klasse? → Lehrplan-Übersicht')),
    rueck.length ? el('p', { class: 'card small' }, `Automatische Rückreise: ${rueck.map((r) => ortName(ortById.get(r.block_id))).join(', ')} – wird zuerst wiederholt, bis der Nachtest bestanden ist.`) : null,
    liste,
    el('div', { class: 'row lern-plan-speichern' }, speichern, status),
    el('section', { class: 'card' }, el('h3', {}, 'Thema hinzufügen'),
      el('div', { class: 'row' }, suche, el('label', { class: 'small' }, nurMitEinheit, ' nur Orte mit Inhalt')), vorrat,
      el('details', { class: 'lern-anmerkung' }, el('summary', {}, '✎ Thema fehlt in der Liste?'), lernRueckmeldungForm({ lernender_id: kindId }, { offen: true }))),
    kindForm,
    el('section', { class: 'card' }, el('h3', {}, 'Notizen'), notizForm,
      ...(p.notizen || []).map((n) => el('p', { class: 'small' }, el('b', {}, String(n.von || '').replace(/^[a-z]+:/, '') + ': '), n.text, el('span', { class: 'muted' }, ' · ' + new Date(n.am).toLocaleDateString('de-DE'))))),
    (p.verlauf || []).length ? el('details', { class: 'card' }, el('summary', {}, 'Verlauf'),
      ...(p.verlauf || []).map((v) => el('p', { class: 'small muted' }, `${new Date(v.am).toLocaleString('de-DE')} · ${String(v.akteur).replace(/^[a-z]+:/, '')} · ${v.anlass === 'plan' ? 'Plan geändert' : v.anlass === 'rueckreise' ? 'Rückreise nach Test' : v.anlass}`))) : null].filter(Boolean));
}

async function viewZugaenge() {
  setChrome('Zugänge', { back: true, showTabs: false });
  const live = viewGuard();
  loading();
  const [z, u] = await Promise.all([lernCall('schule_zugaenge'), lernCall('schule_uebersicht')]);
  if (!live()) return;
  const rollenText = { eltern: 'Eltern', lehrer: 'Lehrer', kind: 'Kind' };
  const name = el('input', { type: 'text', maxlength: '60', placeholder: 'Name, z. B. Herr Müller', 'aria-label': 'Name' });
  const rolle = el('select', { 'aria-label': 'Rolle' }, el('option', { value: 'lehrer' }, 'Lehrer – alle Themen, Plan, Rückmeldungen'),
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
  if (['geprueft', 'freigegeben'].includes(e.status)) return { k: 'fertig', text: `Fertig · ${e.karten} Karten · ${e.aufgaben} Aufgaben${e.neu ? ` (${e.neu} neu in Prüfung)` : ''}` };
  return { k: 'pruefung', text: `In Prüfung · ${e.karten} Karten · ${e.aufgaben} Aufgaben` };
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
  const inhSel = el('select', { 'aria-label': 'Inhalt' }, ...[['', 'Alle Themen'], ['fertig', 'Fertig'], ['pruefung', 'In Prüfung'], ['leer', 'Noch kein Inhalt']]
    .map(([v, t]) => el('option', { value: v, selected: f.inhalt === v }, t)));
  inhSel.addEventListener('change', () => { f.inhalt = inhSel.value; zeichne(); });
  const suche = el('input', { type: 'search', placeholder: 'Thema suchen …', 'aria-label': 'Thema suchen', value: f.q });
  suche.addEventListener('input', () => { f.q = suche.value; zeichne(); });
  const status = el('p', { class: 'small muted', role: 'status' });
  const bauen = async (t, knopf) => {
    knopf.disabled = true;
    try {
      await lernCall('schule_rueckmeldung_geben', { art: 'thema_fehlt', block_id: t.block_id,
        text: `Bitte Inhalte bauen: „${t.titel}“ (${t.ort || t.gebiet}, ${lernJahrgangText(t.jahrgang)}).` });
      knopf.textContent = 'Angefragt ✓'; status.textContent = 'Anfrage ist bei der Entwicklung angekommen.';
    } catch (err) { status.textContent = err.message; knopf.disabled = false; }
  };
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
        t.rueckmeldungen ? el('small', { class: 'muted' }, `${t.rueckmeldungen} offene Anmerkung${t.rueckmeldungen > 1 ? 'en' : ''}`) : null),
      el('div', { class: 'lp-aktionen' },
        t.einheit ? el('a', { class: 'btn secondary', href: `#/inhalte/${t.einheit.id}` }, 'Inhalte ansehen')
          : el('button', { type: 'button', class: 'secondary', onclick: (ev) => bauen(t, ev.currentTarget) }, 'Bauen lassen')));
  };
  const zeichne = () => {
    const q = f.q.trim().toLowerCase();
    const basis = (d.themen || []).filter((t) => !f.kl || String(gk(t)) === String(f.kl));
    const zahl = (k) => basis.filter((t) => lernInhaltZustand(t).k === k).length;
    lernErsetze(kacheln, 
      ...[['', 'Themen', basis.length, ''], ['fertig', 'fertig', zahl('fertig'), ' lp-fertig'], ['pruefung', 'in Prüfung', zahl('pruefung'), ' lp-pruefung'], ['leer', 'ohne Inhalt', zahl('leer'), ' lp-leer']]
        .map(([wert, text, n, kl]) => el('button', { type: 'button', class: 'lp-kachel' + kl + (f.inhalt === wert ? ' on' : ''), 'aria-pressed': String(f.inhalt === wert),
          onclick: () => { f.inhalt = wert; inhSel.value = wert; zeichne(); } }, el('b', {}, String(n)), el('small', {}, text))));
    const treffer = basis.filter((t) => (!f.inhalt || lernInhaltZustand(t).k === f.inhalt)
      && (!q || `${t.titel} ${t.ort} ${t.gebiet}`.toLowerCase().includes(q)));
    const gruppen = new Map();
    for (const t of treffer.sort((a, b) => gk(a) - gk(b))) {
      const g = gk(t); if (!gruppen.has(g)) gruppen.set(g, []); gruppen.get(g).push(t);
    }
    lernErsetze(liste, ...[...gruppen].map(([kl, ts]) => el('section', { class: 'lp-gruppe' },
      el('h3', {}, klName(kl), el('small', { class: 'muted' }, ` · ${ts.length} ${ts.length === 1 ? 'Thema' : 'Themen'}`)),
      ...[...ts.reduce((m, t) => m.set(t.gebiet || 'Weitere', [...(m.get(t.gebiet || 'Weitere') || []), t]), new Map())].flatMap(([g, gs]) => [
        el('h4', { class: 'lp-gebiet' }, g, el('small', { class: 'muted' }, ` · ${gs.filter((t) => lernInhaltZustand(t).k === 'fertig').length} von ${gs.length} mit Inhalt`)),
        ...gs.map(zeile)]))));
    if (!treffer.length) lernAnhaengen(liste, el('p', { class: 'muted' }, 'Keine Themen für diese Auswahl.'));
  };
  fuelleKlassen(); zeichne();
  lernErsetze(main, 
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'ELTERN UND LEHRER'), el('h2', {}, 'Lehrplan-Übersicht'),
      el('p', {}, 'Alle Mathe-Themen, sortiert nach Klasse im Gymnasium. Hinter jedem Thema steht, wann es laut Lehrplan dran ist: Gym = Gymnasium, RS = Realschule, IB = MYP-Jahr. Grün = Inhalt fertig, gelb = gebaut und in Prüfung, grau = noch nichts da.')),
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
  const titel = d.thema?.titel || d.inhalt?.ziel || 'Einheit';
  $('#title').textContent = titel;
  const aufgaben = d.aufgaben || [];
  const etappen = lernEtappen({ inhalt: d.inhalt, uebungen: aufgaben.filter((a) => a.pool === 'uebung') });
  lernTitel = new Map(etappen.map((e) => [e.lernziel, e.titel]));
  const rmJe = (lz) => (d.rueckmeldungen || []).filter((r) => r.lernziel === lz);
  const stufeText = (a) => a.pool === 'uebung' ? (['', 'leicht', 'mittel', 'schwer'][a.stufe] || '–') : a.pool === 'test' ? 'Test' : a.pool === 'nachtest' ? 'Nachtest' : a.pool;
  const tabelle = (as) => el('div', { class: 'lp-tabelle-rahmen' }, el('table', { class: 'lp-tabelle' },
    el('thead', {}, el('tr', {}, el('th', {}, 'Stufe'), el('th', {}, 'Aufgabe'), el('th', {}, 'Lösung'), el('th', {}, 'Lösungsweg'), el('th', {}, 'Status'))),
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
      el('summary', {}, el('b', {}, `${e.nr} · ${e.titel}`), el('small', { class: 'muted' }, ` · ${as.length} ${as.length === 1 ? 'Aufgabe' : 'Aufgaben'}${as.some((a) => !a.freigegeben) ? ` (${as.filter((a) => !a.freigegeben).length} in Prüfung)` : ''}${rm.length ? ` · ${rm.length} ${rm.length === 1 ? 'Anmerkung' : 'Anmerkungen'}` : ''}`)),
      el('div', { class: 'lp-karte-innen' },
        el('div', { class: 'lp-erkl' }, el('p', { class: 'eyebrow' }, 'ERKLÄRUNG, WIE DAS KIND SIE SIEHT'), e.regel ? lernErklaerung(e) : el('p', { class: 'muted' }, 'Keine Erklärung hinterlegt.')),
        lernAnmerkung({ einheit_id: id, lernziel: e.lernziel }, 'Anmerkung zu dieser Karte'),
        ...rm.map((r) => el('p', { class: 'small' }, el('b', {}, (LERN_RM_STATUS[r.status] || r.status) + ': '), r.text, r.antwort ? el('span', { class: 'muted' }, ' → ' + r.antwort) : null)),
        as.length ? tabelle(as) : el('p', { class: 'muted small' }, 'Keine Aufgaben.')));
  });
  const ohneKarte = aufgaben.filter((a) => !etappen.some((e) => e.lernziel === a.lernziel));
  const zahl = (fn) => aufgaben.filter(fn).length;
  lernErsetze(main, ...[
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, [d.ort?.stadt, lernJahrgangText(d.thema?.jahrgang)].filter(Boolean).join(' · ').toUpperCase() || 'INHALTE'),
      el('h2', {}, titel),
      el('p', {}, `${['geprueft', 'freigegeben'].includes(d.status) ? 'Fertig' : 'In Prüfung'} · ${etappen.length} Lernkarten · ${zahl((a) => a.pool === 'uebung')} Übungen · ${zahl((a) => a.pool !== 'uebung')} Test- und Nachtestaufgaben`
        + (zahl((a) => !a.freigegeben) ? ` · ${zahl((a) => !a.freigegeben)} noch in Prüfung (nur für das Testkind sichtbar)` : '')),
      d.inhalt?.ziel ? el('p', { class: 'small muted' }, 'Ziel: ' + d.inhalt.ziel) : null),
    el('nav', { class: 'lp-sprung', 'aria-label': 'Lernkarten' }, ...etappen.map((e) => el('a', { href: '#', class: 'lern-chip', onclick: (ev) => {
      ev.preventDefault(); const k = document.getElementById('k' + e.nr); k.open = true; k.scrollIntoView({ block: 'start' });
    } }, `${e.nr} · ${e.titel}`))),
    lernAnmerkung({ einheit_id: id }, 'Anmerkung zum ganzen Thema'),
    ...karten,
    ohneKarte.length ? el('details', { class: 'card lp-karte' }, el('summary', {}, el('b', {}, `Test- und Nachtestaufgaben ohne Karte (${ohneKarte.length})`)), tabelle(ohneKarte)) : null].filter(Boolean));
}

// ---------- Eltern/Lehrer: „Was wackelt?“ – Lernstand je Lernkarte mit den echten falschen Antworten ----------
async function viewLernstand(arg) {
  setChrome('Lernstand', { back: true, showTabs: false });
  const live = viewGuard();
  const kindId = Number(arg);
  if (!kindId) { route('lernen'); return; }
  loading();
  const d = await lernCall('schule_lernstand', { lernender_id: kindId });
  if (!live()) return;
  $('#title').textContent = 'Lernstand ' + d.kind.name;
  const tag = (t) => new Date(t).toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' });
  const zustand = (k) => k.faellig ? ['wiederholen', 'wdh'] : k.sitzt ? ['sitzt', 'ok']
    : k.falsch >= 3 && k.falsch > k.richtig ? ['wackelt', 'wackelt'] : k.richtig + k.falsch ? ['am Üben', 'ueben'] : ['noch nicht geübt', 'neu'];
  const karte = (k) => {
    const [text, kl] = zustand(k);
    return el('li', { class: 'ls-karte ls-' + kl },
      el('div', { class: 'ls-kopf' }, el('b', {}, k.titel), el('span', { class: 'ls-zustand' }, text)),
      k.richtig + k.falsch ? el('small', { class: 'muted' }, `${k.richtig} richtig · ${k.falsch} falsch` + (k.mit_tipp ? ` · ${k.mit_tipp}-mal Tipp` : '') + (k.zuletzt ? ` · zuletzt ${tag(k.zuletzt)}` : '')) : null,
      (k.fehler || []).length ? el('details', { class: 'ls-fehler' }, el('summary', {}, `Letzte falsche Antworten (${k.fehler.length})`),
        ...k.fehler.map((f) => { const a = { antworttyp: f.antworttyp, antworten: f.antworten, loesung: f.loesung, frage: { text: f.frage, schablone: f.schablone, grafik: f.grafik } };
          return el('p', { class: 'small' }, el('span', {}, lernText(f.frage || '')), el('br'), el('span', { class: 'ls-falsch' }, 'Antwort: ' + (lernAntwortText(a, f.antwort || {}) || '–')),
            ' · ', el('span', { class: 'ls-richtig' }, 'richtig: ' + lernLoesungText(a))); })) : null);
  };
  const wackelt = (d.einheiten || []).flatMap((e) => (e.karten || []).filter((k) => zustand(k)[1] === 'wackelt').map((k) => ({ ...k, ort: e.ort, thema: e.titel })));
  const w = d.woche || {};
  lernErsetze(main,
    el('section', { class: 'start-intro' }, el('p', { class: 'eyebrow' }, 'LERNSTAND'), el('h2', {}, d.kind.name),
      el('p', {}, `Letzte 7 Tage: ${w.aufgaben || 0} Aufgaben, davon ${w.richtig || 0} richtig` + (w.mit_tipp ? `, ${w.mit_tipp}-mal mit Tipp` : '') + `. Lerntage in 4 Wochen: ${(d.lerntage || []).length}` + ((d.lerntage || []).length ? ` (zuletzt ${tag(d.lerntage[0])})` : '') + '.')),
    (() => { const alle = (d.einheiten || []).flatMap((e) => e.karten || []); const sitzt = alle.filter((k) => k.sitzt).length, faellig = alle.filter((k) => k.faellig).length;
      return el('details', { class: 'card ls-wdh' }, el('summary', {}, el('b', {}, 'Was kommt wann wieder? '), `${sitzt} ${sitzt === 1 ? 'Lernkarte sitzt' : 'Lernkarten sitzen'}, ${faellig} davon ${faellig === 1 ? 'ist' : 'sind'} zum Wiederholen dran`),
        el('p', {}, 'Karten-Wiederholung: Sitzt eine Lernkarte, kommt sie nach 1, 3, 7, 14 und 30 Lerntagen wieder – jeweils mit einer Aufgabe. Ein Lerntag ist ein Tag, an dem das Kind in Mathe übt; in Pausen (Reisetage) wartet die Karte.'),
        el('p', {}, 'Bei einem Fehler in der Wiederholung geht die Karte eine Stufe zurück und kommt am nächsten Lerntag wieder. Erst beim zweiten Fehler hintereinander muss das Kind sie neu üben.'),
        el('p', {}, `Vor einem Thema kommen höchstens ${LERN_WDH_RUNDE} Wiederholungen pro Tag; weitere werden nur angeboten.`),
        el('p', {}, 'Nachtest: Nach einem bestandenen Thementest folgt später ein kurzer Nachtest zum selben Thema, ebenfalls nach Lerntagen gezählt.')); })(),
    el('section', { class: 'card ls-wackelt' }, el('h3', {}, 'Was wackelt?'),
      wackelt.length ? el('ul', { class: 'ls-liste' }, ...wackelt.map((k) => el('li', { class: 'ls-karte ls-wackelt' }, el('div', { class: 'ls-kopf' }, el('b', {}, k.titel), el('span', { class: 'ls-zustand' }, `${k.falsch} falsch`)), el('small', { class: 'muted' }, `${k.ort || ''} · ${k.thema}`))))
        : el('p', { class: 'muted' }, 'Im Moment nichts: Keine Lernkarte hat deutlich mehr falsche als richtige Antworten.'),
      el('p', { class: 'small muted' }, '„Wackelt“ heißt: mindestens 3 falsche Antworten und mehr falsche als richtige. Ein Gespräch über genau diese eine Regel hilft meist mehr als weitere Aufgaben.')),
    ...((d.einheiten || []).length ? d.einheiten.map((e) => el('section', { class: 'card' },
      el('div', { class: 'lern-einheit-kopf' }, el('h3', {}, `${e.ort ? e.ort + ': ' : ''}${e.titel}`), el('a', { class: 'small', href: `#/inhalte/${e.einheit_id}` }, 'Inhalte ansehen')),
      el('p', { class: 'small muted' }, `${(e.karten || []).filter((k) => k.sitzt).length} von ${(e.karten || []).length} Lernkarten sitzen` + (e.zuletzt ? ` · zuletzt ${tag(e.zuletzt)}` : '')),
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
        el('p', { class: 'lr-leise' }, offen ? `${offen} ${offen === 1 ? 'Karte braucht' : 'Karten brauchen'} noch Übung – morgen ${offen === 1 ? 'kommt sie' : 'kommen sie'} wieder. Die Erklärung findest du im Merkheft.` : 'Super – das sitzt noch.')),
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
            el('a', { href: `#/lerneinheit/${kind.id}-${a.einheit_id}` }, 'Zur Lernkarte')));
        i++; pruefen.replaceWith(el('button', { type: 'button', class: 'lr-knopf', onclick: zeige }, i < liste.length ? 'Nächste' : 'Fertig'));
      } catch (err) { lernErsetze(meldung, el('p', { class: 'err-text' }, err.message)); pruefen.disabled = false; }
    });
    lernErsetze(flaeche, el('header', { class: 'lr-etappe-oben' }, el('p', { class: 'lr-ueber' }, `WIEDERHOLEN ${i + 1} VON ${liste.length} · ${(a.stadt || '').toUpperCase()}`),
      el('h1', { class: 'lr-titel' }, a.etappe || 'Aufgabe')),
      el('section', { class: 'lr-karte-box lr-aufgabe' }, auf.node), meldung, pruefen);
    window.scrollTo(0, 0);
  };
  if (!liste.length) lernErsetze(flaeche, el('p', { class: 'lr-leise' }, 'Gerade ist nichts zum Wiederholen dran.'), el('a', { class: 'lr-knopf', href: `#/reise/${kind.id}` }, 'Zu Heute'));
  else zeige();
  lernErsetze(main, lernRahmen(kind, 'reise', flaeche));
}
