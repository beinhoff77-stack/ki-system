// W150: Lernen Schule – Übersicht, Üben, Test (lernen-api wird hier simuliert).
const { test, before, after } = require('node:test');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
let browser, server, origin;
const root = path.resolve(__dirname, '..');
before(async () => {
  server = http.createServer((req, res) => {
    const name = new URL(req.url, 'http://localhost').pathname;
    const file = path.join(root, name.endsWith('/') ? name + 'index.html' : name);
    if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); res.end(); return; }
    const types = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.webmanifest': 'application/manifest+json' };
    res.setHeader('Content-Type', types[path.extname(file)] || 'text/plain');
    res.end(fs.readFileSync(file));
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  origin = `http://127.0.0.1:${server.address().port}`;
  try { browser = await chromium.launch({ headless: true, ...(process.env.PW_TEST_EXECUTABLE ? { executablePath: process.env.PW_TEST_EXECUTABLE } : {}) }); }
  catch { browser = await chromium.launch({ headless: true, channel: 'msedge' }); }
});
after(async () => { await browser?.close(); await new Promise((resolve) => server?.close(resolve)); });

const AUFG = {
  11: { id: 11, lernziel: 'stellenwert', antworttyp: 'zahl', frage: { text: 'Welchen Wert hat die Ziffer 2 in 182 887?' }, loesung: { wert: 2000 } },
  12: { id: 12, lernziel: 'strahl', antworttyp: 'markierung', frage: { text: 'Tippe die Markierung an, an der 20 000 liegt.', grafik: { typ: 'zahlenstrahl', start: 0, ende: 40000, abschnitte: 8, beschriftet: 'anfang_ende' } }, loesung: { index: 4 } },
  13: { id: 13, lernziel: 'binomisch', antworttyp: 'luecken', frage: { text: 'Multipliziere aus: (x + 1)²', schablone: '□x² + □x + □' }, loesung: { werte: [1, 2, 1] } },
  15: { id: 15, lernziel: 'binomisch', stufe: 3, antworttyp: 'luecken', frage: { text: 'Kürze 6/8 vollständig.', schablone: '□/□' }, loesung: { werte: [3, 4] } },
  16: { id: 16, lernziel: 'binomisch', stufe: 3, antworttyp: 'luecken', frage: { text: 'Löse das Gleichungssystem.', schablone: 'x = □; y = □' }, loesung: { werte: [2, -1] } },
  601: { id: 601, k: 'a', expedition: 7, lernziel: 'stellenwert', antworttyp: 'zahl', frage: { text: 'Teil a: Wie viel kostet Tarif A bei 30 Minuten (5 € + 0,10 € je Minute)?' }, loesung: { wert: 8 } },
  602: { id: 602, k: 'b', expedition: 7, lernziel: 'strahl', antworttyp: 'zahl', frage: { text: 'Teil b: Tarif A kostet 8 € bei 30 Minuten. Wie viel kostet er bei 60 Minuten?' }, loesung: { wert: 11 } },
  603: { id: 603, k: 'c', expedition: 7, lernziel: 'stellenwert', antworttyp: 'zahl', frage: { text: 'Teil c: Ab wie vielen Minuten ist eine Flat für 12 € günstiger?' }, loesung: { wert: 71 } },
  501: { id: 501, lernziel: 'stellenwert', stufe: 3, typ: 'knobel', bonus: true, antworttyp: 'zahl', frage: { text: 'Knobel: Welche Zahl ist um 4 kleiner, wenn man sie erst um 20 % erhöht und dann um 20 % senkt?' }, loesung: { wert: 100 } },
  14: { id: 14, lernziel: 'lesen', antworttyp: 'auswahl', frage: { text: 'Wie liest man 11 490 051?' }, antworten: ['elf Millionen vierhundertneuntausend…', 'elf Millionen vierhundertneunzigtausendeinundfünfzig'], loesung: { index: 1 } },
};
const ETAPPEN = [
  { lernziel: 'stellenwert', titel: 'Welchen Wert hat eine Ziffer?', regel: 'Jeder Platz ist ⟦10-mal⟧ so viel wert wie der rechts daneben.', schritte: ['In 4 052 steht die ⟦4⟧ bei den Tausendern.', 'Also ist sie 4 000 wert.'],
    fehler: 'Die 0 hält einen Platz frei.', bild: { typ: 'stellentafel', stellen: ['T', 'H', 'Z', 'E'], ziffern: ['4', '0', '5', '2'], markiert: 0 } },
  { lernziel: 'strahl', titel: 'Zahlenstrahl', regel: 'Erst ausrechnen, wie viel ein Abschnitt wert ist.', schritte: ['100 : 10 = 10'], bild: { typ: 'zahlenstrahl', start: 0, ende: 100, abschnitte: 10, pfeil: 3, beschriftet: 'anfang_ende' } },
  { lernziel: 'binomisch', titel: 'Binomische Formeln', regel: '(a + b)² = a² + 2ab + b²', schritte: ['(x + 3)²', '= x² + 6x + 9'], probe: '3 · 3 = 9 ✓' }];
const zeig = (a) => { const { loesung, ...r } = a; return { ...r, tipp: 'Denk an die Stellenwerttafel.' }; };
function bewerte(a, w) {
  if (a.antworttyp === 'luecken') { if (!w?.werte || w.werte.some((x) => !String(x).trim())) return { format_ok: false, hinweis: 'Bitte fülle alle Felder aus.' }; return { format_ok: true, richtig: w.werte.every((x, i) => Number(String(x).replace('−', '-')) === a.loesung.werte[i]) }; }
  if (a.antworttyp === 'auswahl' || a.antworttyp === 'markierung') return { format_ok: true, richtig: w.index === a.loesung.index };
  if (String(w.wert).includes('.')) return { format_ok: false, hinweis: 'Bitte schreibe Dezimalzahlen mit Komma.' };
  return { format_ok: true, richtig: Number(String(w.wert).replace(/\s/g, '')) === a.loesung.wert };
}

async function setup(t, opt = {}) {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, serviceWorkers: 'block' });
  t.after(() => context.close());
  if (!opt.lernSeite) await context.addInitScript(() => { localStorage.setItem('ks_token', 'synthetic-test-session'); });
  // Die bisherigen Tests prüfen das bisherige Design; das neue („Abflug“) hat eigene Tests (opt.gestaltung).
  await context.addInitScript((g) => { localStorage.setItem('lern.gestaltung', g); }, opt.gestaltung || 'alt');
  const appCalls = [];
  const page = await context.newPage(); page.setDefaultTimeout(5000);
  const errors = []; page.on('pageerror', (e) => errors.push(e.message)); t.after(() => assert.deepEqual(errors, []));
  await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.route('**/functions/v1/app-api/**', (r) => appCalls.push(r.request().url()) && r.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: {} }) }));
  const calls = []; const stand = { test: null, antworten: {}, karten: {} };
  const rolle = opt.rolle || 'eltern';
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); const d = b.daten || {};
    const pfad = new URL(route.request().url()).pathname;
    if (pfad.endsWith('/anmelden')) {
      calls.push({ anmelden: b.code });
      const ok = b.code === 'ABCD-EFGH-JKLM';
      await route.fulfill({ contentType: 'application/json', status: ok ? 200 : 400, body: JSON.stringify(ok ? { ok: true, ergebnis: { token: 't'.repeat(64), rolle, name: rolle === 'kind' ? 'Kind A' : 'Herr Lehrer', lernender_id: rolle === 'kind' ? 1 : null } } : { ok: false, fehler: 'Code unbekannt' }) });
      return;
    }
    calls.push(b);
    let e;
    if (b.aktion === 'schule_ich') e = { ok: true, rolle, name: rolle === 'kind' ? 'Kind A' : 'Herr Lehrer', lernender_id: rolle === 'kind' ? 1 : null, app: !opt.lernSeite };
    if (b.aktion === 'schule_eltern' && rolle !== 'eltern') { await route.fulfill({ status: 400, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Nur Eltern' }) }); return; }
    if (b.aktion === 'schule_rueckmeldungen') e = { ok: true, rueckmeldungen: [{ id: 4, von: 'lehrer:Herr Lehrer', art: 'mehr_aufgaben', text: 'Mehr Aufgaben zum Runden.', status: 'erledigt', antwort: '6 neue Aufgaben ergänzt.', am: '2026-11-14T09:00:00Z', ort: 'Rom – Natürliche Zahlen' }] };
    if (['schule_rueckmeldung_geben', 'schule_plan_setzen', 'schule_notiz_setzen', 'schule_kind_setzen'].includes(b.aktion)) e = { ok: true, id: 1 };
    if (b.aktion === 'schule_lernstand') e = { ok: true, kind: { id: 1, name: 'Kind A', klasse: 5 }, lerntage: ['2026-11-14', '2026-11-12'], woche: { aufgaben: 30, richtig: 22, mit_tipp: 4 },
      einheiten: [{ einheit_id: 1, titel: 'Natürliche Zahlen', ort: 'Rom', status: 'geprueft', zuletzt: '2026-11-14T08:00:00Z', karten: [
        { lernziel: 'stellenwert', titel: 'Welchen Wert hat eine Ziffer?', serie: 2, ziel: 2, sitzt: true, richtig: 6, falsch: 1, mit_tipp: 0, faellig: false, zuletzt: '2026-11-14T08:00:00Z', fehler: [] },
        { lernziel: 'runden', titel: 'Runden', serie: 0, ziel: 4, sitzt: false, richtig: 2, falsch: 5, mit_tipp: 3, faellig: false, zuletzt: '2026-11-14T08:00:00Z',
          fehler: [{ frage: 'Runde 929 773 auf Tausender.', antwort: { wert: '929 000' }, antworttyp: 'zahl', loesung: { wert: 930000 }, am: '2026-11-14T08:00:00Z' }] },
        { lernziel: 'strahl', titel: 'Zahlenstrahl', serie: 0, ziel: 2, sitzt: false, richtig: 0, falsch: 0, mit_tipp: 0, faellig: false, fehler: [] }] }] };
    if (b.aktion === 'schule_lehrplan_uebersicht') e = { ok: true, kinder: [{ id: 1, name: 'Kind A', klasse: 5, schulart: 'gym_by' }, { id: 2, name: 'Kind B', klasse: 8, schulart: 'gym_by' }],
      themen: [
        { thema_id: 1, titel: 'Große natürliche Zahlen', gebiet: 'Zahlen', ort: 'Rom', block_id: 49, jahrgang: { gym_by: 5, rs_by: 5, ib_myp: 1 }, einheit: { id: 1, status: 'geprueft', karten: 3, aufgaben: 24, neu: 6 }, stand: { 1: 'erledigt', 2: 'keine_einheit' }, geplant: [], rueckmeldungen: 1 },
        { thema_id: 2, titel: 'Teilbarkeit', gebiet: 'Zahlen', ort: 'Athen', block_id: 48, jahrgang: { gym_by: 5, rs_by: 6 }, einheit: { id: 4, status: 'entwurf', karten: 8, aufgaben: 96, neu: 96 }, stand: { 1: 'offen' }, geplant: [1], rueckmeldungen: 0 },
        { thema_id: 3, titel: 'Brüche addieren', gebiet: 'Zahlen', ort: 'Pisa', block_id: 47, jahrgang: { gym_by: 6, rs_by: 6, ib_myp: 2 }, einheit: null, stand: {}, geplant: [], rueckmeldungen: 0 },
        { thema_id: 4, titel: 'Lineare Funktionen', gebiet: 'Funktionen', ort: 'Kairo', block_id: 70, jahrgang: { gym_by: 8, rs_by: 8, ib_myp: 3 }, einheit: null, stand: {}, geplant: [], rueckmeldungen: 0 },
        { thema_id: 5, titel: 'Nur Realschule', gebiet: 'Geld', ort: 'Lima', block_id: 71, jahrgang: { rs_by: 7 }, einheit: null, stand: {}, geplant: [], rueckmeldungen: 0 }] };
    if (b.aktion === 'schule_inhalt_lesen' && d.einheit_id === 77) e = { ok: true, einheit_id: 77, status: 'entwurf', ort: { stadt: 'Test' }, thema: { titel: 'Zeichnungen', jahrgang: { gym_by: 8 } },
      inhalt: { ziel: 'Zeichnungen', etappen: [
        { lernziel: 'gerade', titel: 'Gerade und Parabel', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'koordinaten', x: [-4, 4], y: [-3, 5], graphen: [{ art: 'linear', m: 2, t: 1, name: 'g' }, { art: 'poly', k: [-2, 0, 1], name: 'p' }], punkte: [{ x: 0, y: 1, name: 'T(0 | 1)' }, { x: 1, y: 3, name: 'P' }], strecken: [[0, 1, 1, 1, 'gestrichelt'], [1, 1, 1, 3, 'gestrichelt']] } },
        { lernziel: 'hyperbel', titel: 'Hyperbel', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'koordinaten', x: [-5, 5], y: [-5, 5], graphen: [{ art: 'hyperbel', a: 2, b: 1, c: 1 }], senkrecht: [-1], waagrecht: [1] } },
        { lernziel: 'sinus', titel: 'Sinus', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'koordinaten', x: [0, 360], y: [-1.5, 1.5], schritt_x: 90, schritt_y: 0.5, grad: true, streckung: 2.2, graphen: [{ art: 'sin', name: 'sin' }, { art: 'cos', name: 'cos', name_x: 150 }] } },
        { lernziel: 'dreieck', titel: 'Dreieck', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'figur', punkte: { A: [0, 0], B: [4, 0], C: [4, 3] }, flaeche: ['A', 'B', 'C'], linien: [['A', 'B', 'c = 4 cm'], ['B', 'C', 'a = 3 cm'], ['A', 'C', 'b = ?']], rechter_winkel: [['B', 'A', 'C']], winkel: [['A', 'B', 'C', 'α']] } },
        { lernziel: 'thales', titel: 'Thales', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'figur', punkte: { A: [-3, 0], B: [3, 0], C: [1.8, 2.4], M: [0, 0] }, kreise: [{ m: 'M', r: 3 }], linien: [['A', 'B'], ['A', 'C'], ['B', 'C']], rechter_winkel: [['C', 'A', 'B']] } },
        { lernziel: 'saeulen', titel: 'Säulen', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'saeulen', einheit: 'Kinder', werte: [{ name: 'Hund', wert: 9 }, { name: 'Katze', wert: 12 }, { name: 'Fisch', wert: 4 }, { name: 'kein Tier', wert: 7 }] } },
        { lernziel: 'kreisd', titel: 'Kreisdiagramm', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'kreisdiagramm', einheit: ' %', werte: [{ name: 'Bus', wert: 40 }, { name: 'Rad', wert: 35 }, { name: 'zu Fuß', wert: 25 }] } },
        { lernziel: 'box', titel: 'Boxplot', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'boxplot', achse: [0, 20], einheit: 'Punkte', reihen: [{ name: 'Klasse a', min: 3, q1: 8, median: 11, q3: 14, max: 19 }, { name: 'Klasse b', min: 5, q1: 7, median: 9, q3: 15, max: 17 }] } },
        { lernziel: 'baum', titel: 'Baumdiagramm', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'baum', aeste: [{ text: 'rot', p: '3/5', aeste: [{ text: 'rot', p: '2/4' }, { text: 'blau', p: '2/4' }] }, { text: 'blau', p: '2/5', aeste: [{ text: 'rot', p: '3/4' }, { text: 'blau', p: '1/4' }] }] } },
        { lernziel: 'tafel', titel: 'Vierfeldertafel', regel: 'r', schritte: ['a', 'b'], fehler: 'f', bild: { typ: 'tabelle', kopf: ['', 'Brille', 'keine Brille', 'Summe'], zeilen: [['Mädchen', '5', '9', '14'], ['Jungen', '4', '10', '14'], ['Summe', '9', '19', '28']] } }] },
      aufgaben: [{ id: 501, lernziel: 'gerade', pool: 'uebung', stufe: 1, antworttyp: 'zahl', freigegeben: true, frage: { text: 'Lies die Steigung ab.', grafik: { typ: 'koordinaten', x: [-3, 3], y: [-3, 3], graphen: [{ art: 'linear', m: 1, t: 0 }] } }, loesung: { wert: 1 } }], rueckmeldungen: [] };
    else if (b.aktion === 'schule_inhalt_lesen') e = { ok: true, einheit_id: d.einheit_id, status: 'geprueft', ort: { stadt: 'Rom', titel: 'Natürliche Zahlen' },
      thema: { titel: 'Große natürliche Zahlen', jahrgang: { gym_by: 5, rs_by: 5 } }, inhalt: { ziel: 'Große Zahlen lesen.', etappen: ETAPPEN },
      aufgaben: [{ ...AUFG[11], pool: 'uebung', stufe: 1, freigegeben: true, loesungsweg: 'Tausender-Stelle.' }, { ...AUFG[12], pool: 'uebung', stufe: 2, freigegeben: false },
        { ...AUFG[11], id: 99, pool: 'test', freigegeben: true }],
      rueckmeldungen: [{ id: 4, art: 'mehr_aufgaben', text: 'Mehr Aufgaben zum Runden.', status: 'offen', lernziel: 'stellenwert', am: '2026-11-14T09:00:00Z' }] };
    if (b.aktion === 'schule_plan_lesen') e = { ok: true, kind: { id: 1, name: 'Kind A', klasse: 5 }, revision: 1,
      plan: [{ route_id: 1, block_id: 49, position: 1, art: 'normal', status: 'offen', kann_schon: false }, { route_id: 2, block_id: 52, position: 2, art: 'normal', status: 'offen', kann_schon: false }],
      orte: [{ block_id: 49, titel: 'Natürliche Zahlen', stadt: 'Rom', kontinent: 'Zahlen', themen: [
          { thema_id: 15, titel: 'Natürliche Zahlen und Stellenwertsysteme', jahrgang: { gym_by: 5, rs_by: 5, ib_myp: 1 }, stand: 'laeuft', einheit: { id: 1, status: 'geprueft', karten: 3, aufgaben: 24, neu: 0 } },
          { thema_id: 16, titel: 'Ganze Zahlen', jahrgang: { gym_by: 5, rs_by: 5, ib_myp: 2 }, stand: 'keine_einheit', einheit: null }] },
        { block_id: 48, titel: 'Teilbarkeit', stadt: 'Athen', kontinent: 'Zahlen', themen: [{ thema_id: 17, titel: 'Teilbarkeit und Primzahlen', jahrgang: { gym_by: 5, rs_by: 5, ib_myp: 1 }, stand: 'offen', einheit: { id: 4, status: 'entwurf', karten: 8, aufgaben: 96, neu: 96 } }] },
        { block_id: 52, titel: 'Zinsen', stadt: 'New York', kontinent: 'Geld', themen: [{ thema_id: 71, titel: 'Einfache Zinsen', jahrgang: { gym_by: 6, rs_by: 7 }, stand: 'offen', einheit: { id: 2, status: 'geprueft', karten: 6, aufgaben: 40, neu: 0 } }] },
        { block_id: 61, titel: 'Ungleichungen', stadt: 'Delhi', kontinent: 'Algebra', themen: [{ thema_id: 3, titel: 'Lineare Ungleichungen', jahrgang: { gym_by: 8, rs_by: 7, ib_myp: 2 }, stand: 'keine_einheit', einheit: null }] }],
      notizen: [], verlauf: [] };
    const geo = (ort, stadt, land, lat, lon, kontinent, kt, erdteil) => ({ ort, stadt, land, lat, lon, kontinent, kontinent_titel: kt, erdteil });
    if (e) { /* oben beantwortet */ }
    else if (b.aktion === 'schule_uebersicht') e = { ok: true, leitung: true, einheiten: [
      { id: 1, status: 'geprueft', block_id: 49, ...geo('z1', 'Rom', 'Italien', 41.9, 12.5), kontinent: 'Zahlen', erdteil: 'Europa', ort_titel: 'Natürliche und ganze Zahlen', titel: 'Natürliche Zahlen', ziel: 'Große Zahlen lesen.', pflicht_anzahl: 4, ziel_klasse: 5 },
      { id: 2, status: 'geprueft', block_id: 52, ...geo('g4', 'New York', 'USA', 40.71, -74.01), kontinent: 'Geld und Verhältnisse', erdteil: 'Nordamerika', ort_titel: 'Zinsen', titel: 'Einfache Zinsen', ziel: 'Zinsen berechnen.', pflicht_anzahl: 6, ziel_klasse: 7 },
      { id: 3, status: 'entwurf', block_id: 60, ...geo('a3', 'Samarkand', 'Usbekistan', 39.65, 66.96), kontinent: 'Algebra', erdteil: 'Asien', ort_titel: 'Terme', titel: 'Terme umformen', ziel: 'Terme umformen.', pflicht_anzahl: 8, ziel_klasse: 7 }],
      orte: [
        { block_id: 49, titel: 'Natürliche und ganze Zahlen', ziel_klasse: 5, hat_einheit: true, ...geo('z1', 'Rom', 'Italien', 41.9, 12.5, 'zahlen', 'Zahlen', 'Europa') },
        { block_id: 48, titel: 'Teilbarkeit', ziel_klasse: 5, hat_einheit: false, ...geo('z2', 'Athen', 'Griechenland', 37.98, 23.73, 'zahlen', 'Zahlen', 'Europa') },
        { block_id: 47, titel: 'Brüche', ziel_klasse: 6, hat_einheit: false, ...geo('z3', 'Pisa', 'Italien', 43.72, 10.4, 'zahlen', 'Zahlen', 'Europa') },
        { block_id: 52, titel: 'Zinsen', ziel_klasse: 7, hat_einheit: true, ...geo('g4', 'New York', 'USA', 40.71, -74.01, 'geld', 'Geld und Verhältnisse', 'Nordamerika') },
        { block_id: 60, titel: 'Terme umformen', ziel_klasse: 7, hat_einheit: false, ...geo('a3', 'Samarkand', 'Usbekistan', 39.65, 66.96, 'algebra', 'Algebra', 'Asien') }],
      lernende: [{ id: 1, name: 'Kind A', klasse: 5, stil: 'entdecker', welt: 'Ozean', ist_test: false, route: [{ block_id: 49, position: 101, status: 'offen', kann_schon: false }, { block_id: 52, position: 206, status: 'offen', kann_schon: false }], stand: [{ einheit_id: 1, fertig: 2, fehler: 1, gesichert: 0, blocktest: true, laeuft: false }] },
        { id: 2, name: 'Kind B', klasse: 7, stil: 'studio', welt: 'Nacht', ist_test: false, route: [{ block_id: 49, position: 101, status: 'fertig', kann_schon: false }, { block_id: 52, position: 206, status: 'offen', kann_schon: false }], stand: [] },
        { id: 3, name: 'Testkind', ist_test: true, route: [], stand: [] }] };
    else if (b.aktion === 'schule_konto') e = { ok: true, konto: { sterne: 340, sterne_gesamt: 340, stempel: d.lernender_id === 2 ? 1 : 0, lerntage: 12, jahrgang: { schulart: 'gym_by', klasse: 5, themen: 14, mit_inhalt: 2, geschafft: 1 } },
      look: { stil: d.lernender_id === 2 ? 'studio' : 'entdecker', welt: d.lernender_id === 2 ? 'Nacht' : 'Ozean' },
      belohnungen: [{ id: 5, titel: 'Eis', kosten_sterne: 300, kosten_stempel: 0 }, { id: 6, titel: 'Kinoabend', kosten_sterne: 0, kosten_stempel: 3 }], einloesungen: [] };
    else if (b.aktion === 'schule_eltern') e = { ok: true, kinder: [{ id: 1, name: 'Kind A', konto: { sterne: 340, stempel: 0, lerntage: 12 } }], belohnungen: [{ id: 5, titel: 'Eis', kosten_sterne: 300, kosten_stempel: 0, aktiv: true }],
      einloesungen: [{ id: 9, kind: 'Kind A', titel: 'Eis', sterne: 300, status: 'beantragt' }] };
    else if (['schule_einloesen', 'schule_look_setzen', 'schule_belohnung_setzen', 'schule_einloesung_entscheiden'].includes(b.aktion)) e = { ok: true };
    else if (b.aktion === 'schule_einheit_lesen') e = { ok: true, einheit_id: d.einheit_id, status: 'geprueft', inhalt: { ziel: 'Natürliche Zahlen: große Zahlen lesen', etappen: ETAPPEN },
      uebungen: [zeig(AUFG[11]), zeig(AUFG[12]), zeig(AUFG[13]), zeig(AUFG[15]), zeig(AUFG[16])], stand: ETAPPEN.map((x) => ({ lernziel: x.lernziel, pflicht: true, status: 'offen' })),
      etappen_stand: { stellenwert: { fertig: false, ziel: 2 }, strahl: { fertig: false, ziel: 2 }, binomisch: { fertig: false, ziel: 2 } }, laufender_test: null };
    else if (b.aktion === 'schule_merkheft') e = { ok: true, einheiten: [{ einheit_id: 1, block_id: 49, stadt: 'Rom', ort_titel: 'Natürliche und ganze Zahlen', etappen: ETAPPEN,
      stand: { stellenwert: { fertig: true }, strahl: { fertig: true } }, blocktest_fertig: false, nachtest: { grund: 'einheit_offen' } },
      { einheit_id: 2, block_id: 52, stadt: 'New York', ort_titel: 'Zinsen', etappen: ETAPPEN.slice(0, 2), stand: { stellenwert: { fertig: true } }, blocktest_fertig: false, nachtest: { grund: 'einheit_offen' } }] };
    else if (b.aktion === 'schule_uebung_pruefen') {
      const a = AUFG[d.aufgabe_id]; const r = bewerte(a, d.antwort);
      if (a.expedition) { // W176 Teil 4: wie die Datenbank nach Migration T4
        e = r.format_ok && !r.richtig && d.anlauf === 1 ? { ok: true, format_ok: true, richtig: false, nochmal: true }
          : { ok: true, ...r, loesung: a.loesung, loesungsweg: 'So wird gerechnet.', expedition: { id: a.expedition, teil: a.k, erledigt: true, geschafft: a.id === 603, sterne: a.id === 603 ? 50 : 0 } };
        await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) }); return;
      }
      if (d.misch && !(r.format_ok && !r.richtig && d.anlauf === 1)) { // W176 Teil 3: Mischkarte – kein Karten-Stand der aktuellen Etappe, dafür die Herkunft
        e = { ok: true, ...r, loesung: a.loesung, loesungsweg: 'Weg zur Lösung.', misch: { etappe: 'Große Zahlen lesen', stadt: 'New York', ok: r.richtig && !d.hilfe && d.anlauf !== 2 } };
        await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) }); return;
      }
      if (a.bonus) { // F: wie die Datenbank nach Migration F – kein Karten-Stand, kein „nochmal“
        e = { ok: true, ...r, bonus: true, erster_versuch: true, sterne: r.richtig ? 30 : 0, knobel_sterne: r.richtig ? 1 : 0, loesung: a.loesung, loesungsweg: 'Erst 1,2 · x, dann 0,96 · x.' };
        await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) }); return;
      }
      const k = stand.karten[a.lernziel] ||= { serie: 0, ziel: 2, sitzt: false };
      let neu = false;
      // wie die Datenbank (R2): Fehlermuster als grund; anlauf 1 + falsch → keine Lösung, keine Buchung; anlauf 2 + richtig → Serie steigt nicht
      let grund; if (r.format_ok && !r.richtig && a.antworttyp === 'zahl') { const v = Number(String(d.antwort.wert).replace(/\s/g, '').replace(',', '.').replace('−', '-')), w = Number(a.loesung.wert);
        if (Math.abs(v) === Math.abs(w)) grund = 'vorzeichen'; else if ([10, 100, 1000, 0.1, 0.01, 0.001].includes(v / w)) grund = 'komma'; }
      if (r.format_ok && !r.richtig && d.anlauf === 1) e = { ok: true, format_ok: true, richtig: false, nochmal: true, ...(grund ? { grund } : {}) };
      else {
        if (r.format_ok) { if (r.richtig && !d.hilfe && d.anlauf !== 2) k.serie++; else if (!r.richtig) k.serie = Math.max(0, k.serie - 2); if (!k.sitzt && k.serie >= k.ziel) { k.sitzt = true; neu = true; } }
        e = { ok: true, ...r, ...(grund ? { grund } : {}), loesung: a.loesung, loesungsweg: 'Weg zur Lösung.', karte: { ...k, neu_sitzt: neu } };
      }
    }
    else if (b.aktion === 'schule_test_starten') { stand.test = 77; e = { ok: true, sitzung_id: 77, art: d.art, aufgaben: [AUFG[14], AUFG[12]].map((a) => { const { loesung, ...r } = a; return r; }), beantwortet: [] }; }
    else if (b.aktion === 'schule_test_antwort') { const a = AUFG[d.aufgabe_id]; const r = bewerte(a, d.antwort); if (r.format_ok) stand.antworten[a.id] = { w: d.antwort, ok: r.richtig }; e = { ok: true, format_ok: r.format_ok, hinweis: r.hinweis, gespeichert: r.format_ok }; }
    else if (b.aktion === 'schule_test_abschliessen') {
      const erg = [AUFG[14], AUFG[12]].map((a) => ({ aufgabe_id: a.id, lernziel: a.lernziel, frage: a.frage, antworten: a.antworten, antwort: stand.antworten[a.id]?.w ?? null, richtig: !!stand.antworten[a.id]?.ok, loesung: a.loesung, loesungsweg: 'Weg.' }));
      e = { ok: true, sitzung_id: 77, richtig: erg.filter((x) => x.richtig).length, gesamt: 2, ergebnisse: erg, lernziele: [{ lernziel: 'lesen', pflicht: true, status: 'nachgewiesen' }, { lernziel: 'strahl', pflicht: true, status: 'fehler' }], einheit_abgeschlossen: false, ort: { abgeschlossen: false } };
    }
    if (opt.anpassen && e) e = opt.anpassen(b.aktion, e) || e; // Schritt D: Antwort nach einer Migration nachbilden
    await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
  });
  return { page, calls, appCalls };
}

test('Lernen: Eltern sehen Kinder, Belohnungen und offene Wünsche', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lernen');
  // Oben steht, was auf eine Antwort wartet; das alte Lernblatt ist eingeklappt am Ende.
  await page.getByText('WARTET AUF DICH').waitFor();
  assert.equal(await page.getByRole('heading', { name: 'Mathe Klasse 7/8' }).count(), 0);
  assert.equal(await page.locator('details.lern-weitere').count(), 1);
  await page.getByText('Jetzt: Rom · Natürliche Zahlen (2/4)').waitFor();
  await page.getByText('möchte „Eis“').waitFor();
  await page.getByRole('button', { name: 'Bestätigen' }).click();
  // Nach dem Bestätigen zeichnet die Ansicht neu – erst danach das Formular ausfüllen (sonst geht die Eingabe im Neuzeichnen verloren).
  for (let i = 0; i < 40 && !calls.some((c) => c.aktion === 'schule_einloesung_entscheiden'); i++) await page.waitForTimeout(50);
  { const n = calls.filter((c) => c.aktion === 'schule_eltern').length; for (let i = 0; i < 40 && calls.filter((c) => c.aktion === 'schule_eltern').length === n && i < 10; i++) await page.waitForTimeout(50); }
  await page.waitForTimeout(400);
  await page.locator('#bl-titel').fill('Kinoabend');
  await page.locator('#bl-stempel').fill('3');
  await page.getByRole('button', { name: 'Hinzufügen' }).click();
  for (let i = 0; i < 40 && !calls.some((c) => c.aktion === 'schule_belohnung_setzen'); i++) await page.waitForTimeout(100);
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_einloesung_entscheiden').map((c) => c.daten), [{ id: 9, status: 'bestaetigt' }]);
  assert.equal(calls.find((c) => c.aktion === 'schule_belohnung_setzen').daten.kosten_stempel, 3);
});

test('Lernreise: Heute dran auf der echten Karte, Weltkarte und Reisepass', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/reise/1');
  await page.getByRole('heading', { name: 'Natürliche Zahlen', exact: true }).waitFor();
  // Der Startknopf steht ganz oben, ist beim Öffnen sichtbar und führt direkt ins Üben.
  const start = page.getByRole('link', { name: /Weiter geht’s|Los geht’s/ });
  const kasten = await start.boundingBox(); assert.ok(kasten.y + kasten.height < 844 - 80, 'Startknopf über der unteren Leiste: ' + Math.round(kasten.y));
  assert.match(await start.getAttribute('href'), /#\/lerneinheit\/1-1-ueben$/);
  assert.equal(await page.locator('.notification-bell').isVisible(), false);
  await page.getByText('MEIN STAND · GYMNASIUM KLASSE 5').waitFor();
  await page.getByText('1 von 14 Flügen').waitFor();
  assert.equal(await page.locator('.lr.lr-ozean.lr-entdecker').count(), 1);
  assert.equal(await page.locator('#areas').isVisible(), false);
  await page.getByText('Du bist in Rom').waitFor();
  assert.equal(await page.locator('details.lr-mehr', { hasText: 'Später' }).count(), 1);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-heute-390.png'), fullPage: true });
  // K2: Menü ohne Weltkarte; die Karte ist ein Reiter in „Mein Weg“ und zeigt nur die Orte der eigenen Klasse.
  assert.deepEqual(await page.locator('.lr-nav a').allInnerTexts(), ['Heute', 'Mein Weg', 'Merkheft', 'Reisepass']);
  await page.getByRole('link', { name: 'Mein Weg' }).click();
  await page.getByRole('heading', { name: 'GERADE DRAN' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-weg-390.png'), fullPage: true });
  await page.locator('.lr-weg-reiter').getByRole('link', { name: 'Karte' }).click();
  await page.getByText('Klasse 5: 0 von 2 Orten geschafft').waitFor();
  await page.getByText('Rom: Natürliche und ganze Zahlen').waitFor();
  assert.equal(await page.getByText('New York', { exact: false }).count(), 0, 'Orte anderer Klassen fehlen');
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-karte-390.png'), fullPage: true });
  await page.getByRole('link', { name: /Reisepass/ }).first().click();
  await page.getByRole('heading', { name: 'Belohnungen' }).waitFor();
  await page.getByText('noch 3 Stempel').waitFor();
  await page.getByRole('button', { name: 'Einlösen' }).click();
  await page.getByText('Wunsch „Eis“ ist abgeschickt').waitFor();
  await page.getByRole('button', { name: /Nacht/ }).click();
  await page.waitForTimeout(200);
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_einloesen').daten, { lernender_id: 1, belohnung_id: 5 });
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_look_setzen').daten, { lernender_id: 1, stil: 'entdecker', welt: 'Nacht' });
  const w = await page.evaluate(() => document.documentElement.scrollWidth); assert.ok(w <= 390, 'keine Querverschiebung: ' + w);
});

test('Lernreise: Kind B (Studio, Nacht) – Rom geschafft als Stempel, Zinsen jetzt dran', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/reise/2');
  await page.getByRole('heading', { name: 'Einfache Zinsen', exact: true }).waitFor();
  assert.equal(await page.locator('.lr.lr-nacht.lr-studio').count(), 1);
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-leo-390.png'), fullPage: true });
  await page.getByText('1 von 2 Etappen sitzen').waitFor();
  await page.getByRole('link', { name: 'Mein Weg' }).click();
  await page.locator('.lr-wegzeile', { hasText: 'Natürliche und ganze Zahlen' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-leo-weg-390.png'), fullPage: true });
  await page.goto(origin + '/#/reisepass/2');
  await page.locator('.lr-stempel', { hasText: 'Rom' }).waitFor();
  await page.goto(origin + '/#/reise/3');
  await page.getByText('Terme umformen', { exact: false }).first().waitFor();
});

test('Lernen: Thema – Erklären | Üben | Typische Fehler, Punkte bis „sitzt“, Erklärung an der Aufgabe', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lerneinheit/1-1');
  await page.getByText('0 von 3 sitzen').waitFor();
  assert.equal(await page.locator('.lr-gesperrt').count(), 1);
  assert.equal(await page.locator('#title').textContent(), 'Rom');
  assert.equal(await page.getByRole('tab', { name: 'Erklären' }).getAttribute('aria-selected'), 'true');
  const sichtbar = page.locator('.lr-panel:not([hidden])');
  // Erklären (Vorgabe 16.11.): Übersicht aus Kacheln mit „Kurz gesagt“ → genau eine Karte, Zurück und Weiter.
  assert.equal(await sichtbar.locator('.lr-kachel').count(), 3);
  await sichtbar.locator('.lr-kachel-kurz').first().waitFor();
  assert.equal(await sichtbar.locator('.lr-lernkarte').count(), 0);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lernen-uebersicht-390.png'), fullPage: true });
  await sichtbar.locator('.lr-kachel').first().click();
  await page.waitForURL(/#\/lerneinheit\/1-1-erklaeren-1$/);
  assert.equal(await sichtbar.locator('.lr-lernkarte').count(), 1);
  await sichtbar.locator('.lr-stellentafel').first().waitFor();
  await sichtbar.locator('mark', { hasText: '10-mal' }).first().waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernen-erklaeren-390.png'), fullPage: true });
  await sichtbar.getByRole('button', { name: /Nächste Etappe: Zahlenstrahl/ }).click();
  await sichtbar.getByText('100 : 10 = 10').waitFor();
  await page.goBack(); await sichtbar.locator('.lr-stellentafel').first().waitFor(); // Zurück-Taste: vorige Karte
  await sichtbar.getByRole('button', { name: '‹ Übersicht' }).click();
  assert.equal(await sichtbar.locator('.lr-kachel').count(), 3);
  await sichtbar.locator('.lr-kachel').first().click();
  await sichtbar.getByRole('button', { name: 'Jetzt du ›' }).click();
  await page.waitForURL(/#\/lerneinheit\/1-1-ueben-1$/);
  { const k = await page.getByRole('button', { name: 'Prüfen' }).boundingBox(); assert.ok(k.y + k.height < 844 - 80, 'Prüfen ist beim Öffnen sichtbar: ' + Math.round(k.y)); }
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2.000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Bitte schreibe Dezimalzahlen mit Komma.').waitFor();
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2 000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.getByText('1 von 2 Punkten').waitFor();
  // Zur Erklärung und zurück: Aufgabe und Rückmeldung bleiben stehen.
  await page.getByRole('tab', { name: 'Erklären' }).click();
  await sichtbar.locator('.lr-stellentafel').first().waitFor();
  await page.getByRole('tab', { name: 'Üben' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.getByRole('button', { name: 'Nächste Bordkarte' }).click();
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('ETAPPE SITZT').waitFor();
  await page.getByText('+10 Sterne').waitFor();
  await page.getByText('1 von 3 sitzen').waitFor();
  await page.getByRole('button', { name: 'Nächste Etappe: Zahlenstrahl' }).click();
  // Neue Lernkarte: erst die Erklärung, dann die Aufgaben
  await page.getByRole('button', { name: 'Jetzt du ›' }).click();
  await page.getByRole('button', { name: 'Markierung 3' }).click();
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Noch nicht – du hast einen zweiten Versuch.').waitFor(); // V2: erst beim zweiten Fehler kommt die Lösung
  assert.equal(await page.getByText(/Richtig ist: 20 000/).count(), 0);
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig ist: 20 000 (der 4. Strich nach dem Anfang)').waitFor();
  // Üben zeigt nur die Aufgabe; die Erklärung öffnet der Link darüber.
  assert.equal(await sichtbar.locator('.lr-nochmal').isVisible(), false);
  await sichtbar.getByRole('button', { name: 'Erklärung ansehen' }).click();
  await sichtbar.locator('.lr-nochmal').getByText('100 : 10 = 10').waitFor();
  await sichtbar.getByRole('button', { name: 'Erklärung schließen' }).click();
  await page.screenshot({ path: path.join(root, 'test-results/lernen-probieren-390.png'), fullPage: true });
  await page.getByRole('tab', { name: 'Fehler' }).click();
  await sichtbar.locator('.lr-fehlerkarte').first().waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernen-fehler-390.png'), fullPage: true });
  await page.getByRole('tab', { name: 'Üben' }).click();
  await page.getByText('Richtig ist: 20 000').waitFor();
  await page.getByRole('button', { name: 'Nächste Bordkarte' }).click();
  await page.getByRole('button', { name: 'Markierung 4' }).click();
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.goto(origin + '/#/lerneinheit/1-1-3');
  await page.getByRole('button', { name: 'Erklärung ansehen' }).waitFor(); // neue Karte direkt geöffnet: nur die Bordkarte, Link zur Erklärung darüber
  assert.equal(await page.locator('.lr-panel:not([hidden]) .lr-nochmal').isVisible(), false);
  const term = page.getByRole('textbox', { name: 'Dein Term' });
  await term.fill('x²+x+x+1');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Fasse gleiche Glieder noch zusammen.').waitFor();
  await term.fill('x');
  await page.getByRole('button', { name: 'hoch 2' }).click();
  await term.press('End'); await term.type(' + 2x ');
  await page.getByRole('button', { name: 'plus' }).click();
  await term.type(' 1');
  await page.screenshot({ path: path.join(root, 'test-results/lernen-term-390.png'), fullPage: true });
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig!').waitFor();
  // Allgemeine Lücken: Bruch als Zähler/Nenner, Zahlenpaar als zwei Felder.
  await page.getByRole('button', { name: 'Nächste Bordkarte' }).click();
  await page.getByRole('textbox', { name: 'Zähler' }).fill('3');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Bitte fülle alle Felder aus.').waitFor();
  await page.getByRole('textbox', { name: 'Nenner' }).fill('4');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.getByRole('button', { name: 'Nächste Bordkarte' }).click();
  await page.getByRole('textbox', { name: 'Lücke 1' }).fill('2');
  await page.getByRole('textbox', { name: 'Lücke 2' }).fill('1');
  await page.screenshot({ path: path.join(root, 'test-results/lernen-luecken-390.png'), fullPage: true });
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Noch nicht – du hast einen zweiten Versuch.').waitFor();
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig ist: x = 2; y = −1').waitFor();
  const p = calls.filter((c) => c.aktion === 'schule_uebung_pruefen');
  assert.deepEqual(p.map((c) => c.daten.antwort), [{ wert: '2.000' }, { wert: '2 000' }, { wert: '2000' }, { index: 3 }, { index: 3 }, { index: 4 }, { werte: ['1', '2', '1'] }, { werte: ['3', '4'] }, { werte: ['2', '1'] }, { werte: ['2', '1'] }]);
  assert.ok(p.every((c) => c.daten.lernender_id === 1 && c.daten.client_id));
  const w = await page.evaluate(() => document.documentElement.scrollWidth); assert.ok(w <= 390, 'keine Querverschiebung: ' + w);
});

test('Lernen: Merkheft zeigt nur Geschafftes (Kontinent → Flug → Etappe), mit Suche und Weg zum Üben', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/merkheft/2');
  await page.locator('details.lr-merk').first().waitFor();
  assert.equal(await page.locator('.lr.lr-nacht.lr-studio').count(), 1);
  assert.equal(await page.locator('details.lr-merk').count(), 3, 'nur die drei geschafften Etappen');
  assert.equal(await page.getByText('noch nicht geübt').count(), 0);
  assert.deepEqual(await page.locator('.lr-merkgruppe > h2').allInnerTexts(), ['EUROPA · ZAHLEN', 'NORDAMERIKA · GELD UND VERHÄLTNISSE']);
  assert.deepEqual(await page.locator('.lr-merkflug-titel').allInnerTexts(), ['Natürliche Zahlen · Rom', 'Einfache Zinsen · New York']);
  assert.ok((await page.locator('.lr-suche').boundingBox()).y < (await page.locator('.lr-merkgruppe').first().boundingBox()).y, 'Suche oben');
  await page.getByRole('searchbox').fill('binomxyz');
  await page.getByText('Nichts gefunden.').waitFor();
  await page.getByRole('searchbox').fill('zahlenstrahl');
  await page.locator('details.lr-merk[open]', { hasText: 'Zahlenstrahl' }).first().waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernen-merkheft-390.png'), fullPage: true });
  await page.getByRole('link', { name: 'Üben' }).first().click();
  await page.waitForURL(/#\/lerneinheit\/2-1-ueben-2$/);
});

test('Lernen: Test ohne Lösungen bis zur Abgabe, danach Auswertung', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByRole('button', { name: 'Test starten' }).click();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
  await page.getByRole('button', { name: 'Weiter ›' }).click();
  assert.equal(await page.getByText('Richtig').count(), 0);
  await page.getByRole('button', { name: 'Markierung 2' }).click();
  await page.getByRole('button', { name: 'Abgeben' }).click();
  await page.getByText('1 von 2 richtig').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernen-ergebnis-390.png'), fullPage: true });
  await page.getByText('Richtig: ', { exact: false }).first().waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_test_antwort').map((c) => c.daten.antwort), [{ index: 1 }, { index: 2 }]);
  assert.equal(calls.filter((c) => c.aktion === 'schule_test_abschliessen').length, 1);
});

test('Lehrplan-Übersicht: Themen je Schulart und Klasse mit Inhaltsstand, Inhalte prüfen, Bauen lassen', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lehrplan');
  await page.getByRole('heading', { name: 'Lehrplan-Übersicht' }).waitFor();
  // Alle 5 Themen, nach Gymnasium-Klasse gruppiert; das reine Realschul-Thema steht am Ende.
  assert.deepEqual(await page.locator('.lp-kachel b').allTextContents(), ['5', '1', '1', '3']);
  await page.getByRole('heading', { name: /Klasse 8.*Kind B/ }).waitFor();
  await page.getByRole('heading', { name: /Nicht im Gymnasium-Lehrplan/ }).waitFor();
  await page.getByRole('heading', { name: 'Zahlen · 1 von 2 mit Inhalt' }).waitFor();
  await page.getByRole('heading', { name: /^Funktionen/ }).waitFor();
  assert.equal(await page.getByRole('button', { name: 'Realschule' }).count(), 0);
  await page.locator('.lp-zeile.lp-fertig', { hasText: 'Große natürliche Zahlen' }).getByText('Kind A: geschafft').waitFor();
  await page.locator('.lp-zeile', { hasText: 'Große natürliche Zahlen' }).getByText('Gym 5 · RS 5 · IB MYP-Jahr 1').waitFor();
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lehrplan-390.png'), fullPage: true });
  await page.getByRole('combobox', { name: 'Klasse' }).selectOption('5');
  assert.deepEqual(await page.locator('.lp-kachel b').allTextContents(), ['2', '1', '1', '0']);
  await page.getByRole('combobox', { name: 'Klasse' }).selectOption('');
  await page.getByRole('combobox', { name: 'Inhalt' }).selectOption('leer');
  const lf = page.locator('.lp-zeile', { hasText: 'Lineare Funktionen' });
  assert.equal(await lf.getByRole('button', { name: 'Bauen lassen' }).count(), 0, 'E-3: ein Knopf überall');
  await lf.getByText('✎ Ändern lassen').click();
  await lf.getByRole('button', { name: 'Auftrag senden' }).click();
  await lf.getByText('Danke – der Auftrag ist angekommen', { exact: false }).waitFor();
  const rm = calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten;
  assert.equal(rm.art, 'thema_fehlt'); assert.equal(rm.bezug, 'flug'); assert.equal(rm.block_id, 70); assert.match(rm.text, /Lineare Funktionen/);
  await page.getByRole('combobox', { name: 'Klasse' }).selectOption('99');
  await page.locator('.lp-zeile', { hasText: 'Nur Realschule' }).getByText('RS 7').waitFor();
  await page.getByRole('combobox', { name: 'Klasse' }).selectOption('');
  await page.getByRole('combobox', { name: 'Inhalt' }).selectOption('');
  await page.locator('.lp-zeile', { hasText: 'Große natürliche Zahlen' }).getByRole('link', { name: 'Inhalte ansehen' }).click();
  await page.waitForURL(/#\/inhalte\/1$/);
  await page.getByText('3 Etappen · 2 Bordkarten zum Üben · 1 für Test und Nachtest', { exact: false }).waitFor();
  await page.locator('details.lp-karte > summary').first().click();
  await page.getByText('ERKLÄRUNG, WIE DAS KIND SIE SIEHT').first().waitFor();
  await page.locator('.lp-tabelle').first().getByText('frei ✓').first().waitFor();
  await page.locator('details.lp-karte > summary', { hasText: '1 in Prüfung' }).waitFor();
  await page.locator('.lp-tabelle').first().getByText('Tausender-Stelle.').waitFor();
  await page.getByText('Mehr Aufgaben zum Runden.').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/inhalte-390.png'), fullPage: true });
  const w = await page.evaluate(() => document.documentElement.scrollWidth); assert.ok(w <= 390, 'keine Querverschiebung: ' + w);
});

test('Zeichnungen: Koordinatensystem, Figur, Diagramme und Tabelle in den Erklärungen', async (t) => {
  const { page } = await setup(t);
  await page.setViewportSize({ width: 430, height: 900 });
  await page.goto(origin + '/#/inhalte/77');
  await page.getByText('10 Etappen', { exact: false }).waitFor();
  await page.evaluate(() => document.querySelectorAll('details.lp-karte').forEach((d) => { d.open = true; }));
  assert.equal(await page.locator('svg.lern-zeichnung').count(), 9);
  assert.equal(await page.locator('svg.lern-zeichnung path.graph').count(), 5);
  assert.equal(await page.locator('table.lr-tafel td').count(), 9);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  for (const [i, n] of ['gerade', 'hyperbel', 'sinus', 'dreieck', 'thales', 'saeulen', 'kreisd', 'box', 'baum'].entries())
    await page.locator('svg.lern-zeichnung').nth(i).screenshot({ path: path.join(root, `test-results/zeichnung-${n}.png`) });
});

test('Was wackelt? – je Lernkarte mit den echten falschen Antworten (eigener Knopf an der Kinderkarte)', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/lernen');
  await page.getByRole('link', { name: 'Was wackelt? Kind A' }).click();
  await page.waitForURL(/#\/wackelt\/1$/);
  await page.getByRole('heading', { name: 'Was wackelt?', exact: true }).waitFor();
  await page.locator('.ls-wackelt .ls-karte', { hasText: 'Runden' }).getByText('5 falsch').waitFor();
  await page.getByText('Letzte 7 Tage: 30 Bordkarten, davon 22 richtig, 4-mal mit Tipp.', { exact: false }).waitFor();
  await page.getByText('Letzte falsche Antworten (1)').click();
  await page.getByText('Antwort: 929 000').waitFor();
  await page.getByText('richtig: 930 000').waitFor();
  await page.locator('.ls-karte.ls-ok', { hasText: 'Welchen Wert hat eine Ziffer?' }).waitFor();
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lernstand-390.png'), fullPage: true });
});

test('Kinderplan: Schulart und Klasse setzen', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/plan/1');
  // Zugeklappt eine Zeile je Ort; aufgeklappt hinter jedem Flug die Klasse je Schulart.
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.waitFor();
  assert.equal(await rom.getByText('Ganze Zahlen').count(), 0);
  await rom.locator('.lern-plan-ort').click();
  await rom.getByText('Ganze Zahlen').waitFor();
  await rom.getByText('Gym 5 · RS 5 · IB MYP-Jahr 2').waitFor();
  // Rechts der Lehrplan der eigenen Schulart und Klasse
  assert.equal(await page.getByRole('combobox', { name: 'Schulart' }).inputValue(), 'gym_by');
  assert.equal(await page.getByRole('combobox', { name: 'Klasse', exact: true }).inputValue(), '5');
  await page.screenshot({ path: path.join(root, 'test-results/themenplan-390.png'), fullPage: true });
  // M2: Klasse ist eine Auswahl und speichert sofort – kein eigener Knopf
  assert.equal(await page.locator('.lp-kindform button').count(), 0);
  await page.getByRole('combobox', { name: 'Klasse des Kindes' }).selectOption('6');
  await page.locator('.lp-kindform [role=status]', { hasText: 'Gespeichert' }).waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_kind_setzen').daten, { lernender_id: 1, klasse: 6 });
});

test('Lernen-Seite: Lehrer meldet sich mit Code an, ordnet den Flugplan (speichert sofort, Rückgängig) und schreibt Rückmeldungen', async (t) => {
  const { page, calls, appCalls } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.goto(origin + '/lernen/');
  await page.getByLabel('Lern-Code').fill('falsch');
  await page.getByRole('button', { name: 'Anmelden' }).click();
  await page.getByText('Code unbekannt').waitFor();
  await page.getByLabel('Lern-Code').fill('abcdefgh jklm');
  await page.getByRole('button', { name: 'Anmelden' }).click();
  await page.getByRole('link', { name: 'Flugplan Kind A' }).waitFor();
  assert.equal(await page.getByText('Zugänge', { exact: true }).count(), 0, 'Lehrer verwaltet keine Zugänge');
  assert.equal(await page.getByRole('heading', { name: 'Mathe Klasse 7/8' }).count(), 0);
  await page.getByRole('link', { name: 'Flugplan Kind A' }).click();
  await page.locator('.lern-plan-zeile').first().waitFor();
  assert.equal(await page.getByRole('button', { name: 'Plan speichern' }).count(), 0, 'kein Speichern-Knopf mehr');
  const leiste = page.locator('.lern-plan-kopf');
  assert.equal(await leiste.getByRole('button', { name: /Rückgängig/ }).isDisabled(), true, 'Rückgängig steht dauerhaft oben, anfangs ohne Schritt');
  const setzen = () => calls.filter((c) => c.aktion === 'schule_plan_setzen').map((c) => c.daten);
  // Jede Änderung speichert sofort, jeweils mit der neuen Revision.
  await page.getByRole('button', { name: 'New York – Zinsen nach oben' }).click();
  await leiste.getByText('Gespeichert', { exact: true }).waitFor();
  await page.getByRole('button', { name: '+ Athen – Teilbarkeit' }).click();
  for (let i = 0; i < 40 && setzen().length < 2; i++) await page.waitForTimeout(50);
  await leiste.getByText('Gespeichert', { exact: true }).waitFor();
  await page.locator('.lern-plan-zeile').nth(2).locator('.lern-plan-ort').click();
  await page.locator('.lern-plan-zeile').nth(2).getByLabel('kann es schon').check();
  for (let i = 0; i < 40 && setzen().length < 3; i++) await page.waitForTimeout(50);
  await leiste.getByText('Gespeichert', { exact: true }).waitFor();
  assert.deepEqual(setzen(), [
    { lernender_id: 1, revision: 1, eintraege: [{ block_id: 52, kann_schon: false }, { block_id: 49, kann_schon: false }] },
    { lernender_id: 1, revision: 2, eintraege: [{ block_id: 52, kann_schon: false }, { block_id: 49, kann_schon: false }, { block_id: 48, kann_schon: false }] },
    { lernender_id: 1, revision: 3, eintraege: [{ block_id: 52, kann_schon: false }, { block_id: 49, kann_schon: false }, { block_id: 48, kann_schon: true }] }]);
  // „Rückgängig“ stellt den Zustand vor der letzten Änderung wieder her und speichert ihn.
  await page.waitForTimeout(9000); // nach mehr als 8 Sekunden ist „Rückgängig“ weiter da (Befund 4)
  await leiste.getByRole('button', { name: /Rückgängig/ }).click();
  await leiste.getByText('Rückgängig gemacht · Gespeichert').waitFor();
  assert.deepEqual(setzen()[3], { lernender_id: 1, revision: 4, eintraege: [{ block_id: 52, kann_schon: false }, { block_id: 49, kann_schon: false }, { block_id: 48, kann_schon: false }] });
  assert.equal(await page.locator('.lern-plan-zeile').nth(2).getByLabel('kann es schon').isChecked(), false);
  await page.goto(origin + '/lernen/#/lernauftraege');
  await page.getByRole('heading', { name: 'Meine Aufträge' }).waitFor();
  await page.getByRole('button', { name: /Beantwortet/ }).click();
  await page.getByText('6 neue Aufgaben ergänzt.').waitFor();
  await page.getByText('✎ Neuer Auftrag (allgemein)').click();
  const form = page.locator('.lern-auftrag-form').first();
  await form.getByRole('button', { name: 'Neuer Flug' }).click();
  await form.getByLabel('Was soll anders sein?').fill('Prozentrechnung fehlt für Klasse 7.');
  await form.getByRole('button', { name: 'Auftrag senden' }).click();
  await page.getByText('Danke – der Auftrag ist angekommen', { exact: false }).waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten, { bezug: 'allgemein', art: 'thema_fehlt', text: 'Prozentrechnung fehlt für Klasse 7.' });
  assert.deepEqual(appCalls, [], 'Die Lernen-Seite ruft die Hauptapp-Schnittstelle nie auf');
});

test('Lernen-Seite: Anmerkung direkt an einer Aufgabe, Kind-Code nur Lernreise', async (t) => {
  const { page, calls } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.goto(origin + '/lernen/#/lerneinheit/3-1-1');
  const offen = page.locator('.lr-panel:not([hidden])');
  await offen.getByText('✎ Ändern lassen').click();
  await offen.getByText('An: Bordkarte „Welchen Wert hat die Ziffer 2 in 182 887?“').waitFor(); // der Bezug steht automatisch dabei
  await offen.getByRole('button', { name: 'Bordkarten' }).click();
  await offen.getByRole('button', { name: 'Schwieriger' }).click();
  await offen.getByLabel('Was soll anders sein?').fill('Zu leicht für Klasse 5.');
  await offen.getByRole('button', { name: 'Auftrag senden' }).click();
  await page.getByText('Danke – der Auftrag ist angekommen', { exact: false }).waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten,
    { einheit_id: 1, lernziel: 'stellenwert', aufgabe_id: 11, lernender_id: 3, bezug: 'bordkarte', art: 'schwieriger', text: 'Zu leicht für Klasse 5.' });
});

test('Lernen-Seite: Kind-Code landet in der eigenen Lernreise, Eltern-Ansichten gesperrt', async (t) => {
  const { page } = await setup(t, { lernSeite: true, rolle: 'kind' });
  await page.goto(origin + '/lernen/');
  await page.getByLabel('Lern-Code').fill('abcd efgh jklm'.toUpperCase().replace(/ /g, '-'));
  await page.getByRole('button', { name: 'Anmelden' }).click();
  await page.waitForURL(/#\/reise\/1$/);
  await page.goto(origin + '/lernen/#/plan/1');
  await page.waitForURL(/#\/reise\/1$/);
  assert.equal(await page.locator('#btn-back').isHidden(), true);
});

test('Lernreise mit Themenplan: nur Orte aus dem Plan sind dran', async (t) => {
  const { page } = await setup(t);
  // Plan-Logik direkt prüfen (lernReiseDaten)
  await page.goto(origin + '/#/lernen');
  await page.getByRole('link', { name: 'Flugplan Kind A' }).waitFor();
  const gruppen = await page.evaluate(() => {
    const u = { einheiten: [{ id: 1, block_id: 49, pflicht_anzahl: 4, ziel_klasse: 5 }, { id: 2, block_id: 52, pflicht_anzahl: 6, ziel_klasse: 7 }, { id: 4, block_id: 48, pflicht_anzahl: 6, ziel_klasse: 5 }],
      orte: [], lernende: [{ id: 1, klasse: 5, route: [{ block_id: 52, position: 1, art: 'normal', status: 'offen' }, { block_id: 49, position: 2, art: 'normal', status: 'offen', kann_schon: true }, { block_id: 48, position: 3, art: 'normal', status: 'entfernt' }], stand: [] }] };
    const d = lernReiseDaten(u, 1);
    return { jetzt: d.jetzt.map((e) => e.id), kann: d.kann.map((e) => e.id), spaeter: d.spaeter.map((e) => e.id), naechste: d.naechste.id };
  });
  assert.deepEqual(gruppen, { jetzt: [2], kann: [1], spaeter: [4], naechste: 2 });
});

test('Gestaltung Abflug: Abflugtafel, Bordkarte mit Tastenfeld, Kurskorrektur, Landung', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1');
  await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  assert.equal(await page.locator('.lr.lr-abflug.lr-abflug-nacht').count(), 1);
  const start = page.getByRole('link', { name: /Einsteigen\s*ROM/ });
  const k = await start.boundingBox(); assert.ok(k.y + k.height <= 844 && k.y > 844 / 2, 'Einsteigen im Daumenbereich: ' + Math.round(k.y));
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth), false);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/abflug-tafel-390.png') });
  // Menüblatt statt Leiste
  assert.equal(await page.locator('.lr-nav').count(), 0);
  await page.getByRole('button', { name: 'Menü', exact: true }).first().click();
  assert.deepEqual(await page.locator('.lr-blatt-liste a').allInnerTexts(), ['Abflugtafel', 'Mein Weg', 'Merkheft', 'Reisepass']); // K2: 4 Einträge
  await page.screenshot({ path: path.join(root, 'test-results/abflug-menue-390.png') });
  await page.getByRole('button', { name: 'Schließen' }).click();
  await start.click();
  // Neue Lernkarte: „Einsteigen“ zeigt zuerst die Erklärung, „Jetzt du“ führt zu den Aufgaben
  await page.waitForURL(/#\/lerneinheit\/1-1-erklaeren-1/);
  await page.getByRole('button', { name: 'Jetzt du ›' }).click();
  await page.waitForURL(/#\/lerneinheit\/1-1-ueben/);
  await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  const los = page.getByRole('button', { name: 'Verstanden – los' }); if (await los.count()) await los.click();
  const feld = page.getByRole('group', { name: 'Tastenfeld' });
  const pruefen = feld.getByRole('button', { name: 'Prüfen' });
  { const b = await pruefen.boundingBox(); assert.ok(b.y + b.height <= 844, 'Prüfen ohne Scrollen sichtbar: ' + Math.round(b.y + b.height)); }
  for (const z of ['2', '0', '0']) await feld.getByRole('button', { name: z, exact: true }).click();
  assert.equal(await page.getByRole('textbox', { name: 'Antwort' }).inputValue(), '200');
  // Stellenwert-Kacheln (Klasse 5): Spalte T antippen, Ziffer wählen, wieder zurück
  await page.getByRole('button', { name: 'T: leer' }).click();
  await feld.getByRole('button', { name: '7', exact: true }).click();
  assert.equal(await page.getByRole('textbox', { name: 'Antwort' }).inputValue(), '7200');
  await feld.getByRole('button', { name: 'löschen' }).click(); await feld.getByRole('button', { name: 'löschen' }).click(); await feld.getByRole('button', { name: 'löschen' }).click(); await feld.getByRole('button', { name: 'löschen' }).click();
  for (const z of ['2', '0', '0']) await feld.getByRole('button', { name: z, exact: true }).click();
  await page.screenshot({ path: path.join(root, 'test-results/abflug-bordkarte-390.png') });
  await pruefen.click();
  // V2/V3: erster Fehler → keine Lösung, nur der Hinweis zum Fehlermuster (200 statt 2 000 = Komma/Stelle); zweiter Versuch
  await page.getByText('Noch nicht – du hast einen zweiten Versuch.').waitFor();
  await page.getByText('Die Ziffern stimmen – schau, wo das Komma hingehört.').waitFor();
  assert.equal(await page.getByText('Richtig ist: 2 000').count(), 0);
  await pruefen.click();
  await page.getByText('FAST – KURSKORREKTUR').waitFor();
  assert.equal(await page.locator('.lr-kurs-kachel.ab').count() > 0, true);
  await page.getByText('Richtig ist: 2 000').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/abflug-kurs-390.png') });
  await page.getByRole('button', { name: 'Neue Bordkarte ›' }).click();
  for (let i = 0; i < 2; i++) {
    for (const z of ['2', '0', '0', '0']) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
    await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
    if (i === 0) { await page.getByText(/An Bord/).waitFor(); await page.getByRole('button', { name: 'Neue Bordkarte ›' }).click(); }
  }
  await page.getByText('GELANDET').waitFor();
  await page.getByRole('link', { name: 'Zur Abflugtafel' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/abflug-gelandet-390.png') });
  // Andere Aufgabenarten auf der Bordkarte: Zahlenstrahl (ohne Tastenfeld) und Lücken (mit Tastenfeld)
  for (const nr of [2, 3]) {
    await page.goto(origin + '/#/lerneinheit/1-1-ueben-' + nr); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
    const v = page.getByRole('button', { name: 'Verstanden – los' }); if (await v.count()) await v.click();
    const b = await page.locator('.lr-dock').getByRole('button', { name: 'Prüfen' }).boundingBox(); assert.ok(b.y + b.height <= 844, 'Prüfen sichtbar bei Karte ' + nr);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth), false);
    await page.screenshot({ path: path.join(root, `test-results/abflug-karte${nr}-390.png`) });
  }
  // Übrige Ansichten im neuen Stil: kein waagrechtes Scrollen, Bilder zum Ansehen
  for (const v of ['weltkarte', 'reisepass', 'merkheft', 'weg']) {
    await page.goto(origin + `/#/${v}/1`); await page.locator('.lr.lr-abflug .lr-inhalt > *').first().waitFor(); await page.waitForTimeout(300);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth), false, v);
    await page.screenshot({ path: path.join(root, `test-results/abflug-${v}-390.png`), fullPage: true });
  }
  // Wischen wechselt den Reiter: von Üben nach links wischen → Fehler, nach rechts → zurück
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  const wisch = (x1, x2) => page.evaluate(([a, b]) => { const z = document.querySelector('.lr-thema'); const t = (x) => new Touch({ identifier: 1, target: z, clientX: x, clientY: 300 });
    z.dispatchEvent(new TouchEvent('touchstart', { touches: [t(a)], changedTouches: [t(a)], bubbles: true })); z.dispatchEvent(new TouchEvent('touchend', { touches: [], changedTouches: [t(b)], bubbles: true })); }, [x1, x2]);
  await wisch(320, 80);
  assert.equal(await page.getByRole('tab', { name: /Fehler/ }).getAttribute('aria-selected'), 'true');
  await wisch(80, 320);
  assert.equal(await page.getByRole('tab', { name: /Üben/ }).getAttribute('aria-selected'), 'true');
  // Tablet und Rechner: kein waagrechtes Scrollen, Bilder zum Ansehen
  for (const [name, w, h] of [['tablet', 820, 1180], ['rechner', 1366, 800]]) {
    await page.setViewportSize({ width: w, height: h });
    await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor(); await page.waitForTimeout(500);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth), false, name + ' Tafel');
    await page.screenshot({ path: path.join(root, `test-results/abflug-tafel-${name}.png`) });
    await page.goto(origin + '/#/lerneinheit/1-1-ueben-3'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor(); await page.waitForTimeout(300);
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth), false, name + ' Bordkarte');
    await page.screenshot({ path: path.join(root, `test-results/abflug-bordkarte-${name}.png`) });
  }
  await page.setViewportSize({ width: 390, height: 844 });
  // Tag-Ansicht und Rückweg zum bisherigen Design im Reisepass
  await page.goto(origin + '/#/reisepass/1');
  await page.getByRole('button', { name: 'Abflug hell' }).click();
  await page.locator('.lr.lr-abflug.lr-abflug-tag').waitFor();
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/abflug-tafel-tag-390.png') });
  await page.goto(origin + '/#/reisepass/1');
  await page.getByRole('button', { name: 'Bisheriges Design' }).click();
  await page.locator('.lr.lr-ozean').waitFor();
});

test('Flugplan: Änderung bleibt nach Verlassen der Seite, Versionskonflikt überschreibt nichts', async (t) => {
  const { page, calls } = await setup(t);
  // Plan wie in der Datenbank: schule_plan_setzen merkt sich den Stand und prüft die Revision.
  const db = { revision: 1, eintraege: [{ block_id: 49, kann_schon: false }, { block_id: 52, kann_schon: false }], fremd: false };
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); const d = b.daten || {};
    const antwort = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
    if (b.aktion === 'schule_plan_setzen') {
      calls.push(b);
      if (db.fremd || d.revision !== db.revision) return route.fulfill({ status: 400, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Der Plan wurde inzwischen geändert. Bitte neu laden.' }) });
      db.revision++; db.eintraege = d.eintraege; return antwort({ ok: true, revision: db.revision, anzahl: d.eintraege.length });
    }
    if (b.aktion === 'schule_plan_lesen') {
      calls.push(b);
      const orte = [{ block_id: 49, titel: 'Natürliche Zahlen', stadt: 'Rom', kontinent: 'Zahlen', themen: [] }, { block_id: 52, titel: 'Zinsen', stadt: 'New York', kontinent: 'Geld', themen: [] },
        { block_id: 48, titel: 'Teilbarkeit', stadt: 'Athen', kontinent: 'Zahlen', themen: [{ thema_id: 17, titel: 'Teilbarkeit und Primzahlen', jahrgang: { gym_by: 5 }, einheit: null }] }];
      return antwort({ ok: true, kind: { id: 1, name: 'Kind A', klasse: 5 }, revision: db.revision, orte, notizen: [], verlauf: [],
        plan: db.eintraege.map((x, i) => ({ route_id: i + 1, block_id: x.block_id, position: i + 1, art: 'normal', status: 'offen', kann_schon: x.kann_schon })) });
    }
    return route.fallback();
  });
  const reihenfolge = () => page.locator('.lern-plan-zeile .lern-plan-ort > b').allInnerTexts();
  await page.goto(origin + '/#/plan/1');
  await page.locator('.lern-plan-zeile').first().waitFor();
  await page.getByRole('button', { name: 'New York – Zinsen nach oben' }).click();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  // Seite verlassen und zurück: die Änderung ist da.
  await page.goto(origin + '/#/lernen'); await page.getByRole('link', { name: 'Flugplan Kind A' }).waitFor();
  await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-zeile').first().waitFor();
  assert.deepEqual(await reihenfolge(), ['New York – Zinsen', 'Rom – Natürliche Zahlen']);
  // Jemand anderes ändert den Plan: klare Meldung, Knopf „Neu laden“, Liste gesperrt, nichts überschrieben.
  db.fremd = true;
  await page.getByRole('button', { name: 'Rom – Natürliche Zahlen nach oben' }).click();
  await page.locator('.lern-plan-kopf').getByText('Der Plan wurde inzwischen von jemand anderem geändert', { exact: false }).waitFor();
  assert.equal(await page.locator('ol.lern-plan').evaluate((x) => x.inert), true);
  assert.deepEqual(db.eintraege.map((x) => x.block_id), [52, 49], 'nichts überschrieben');
  await page.screenshot({ path: path.join(root, 'test-results/flugplan-konflikt-390.png'), fullPage: false });
  db.fremd = false; db.revision = 7; db.eintraege = [{ block_id: 48, kann_schon: false }, { block_id: 52, kann_schon: false }, { block_id: 49, kann_schon: false }];
  await page.locator('.lern-plan-kopf').getByRole('button', { name: 'Neu laden' }).click();
  await page.locator('.lern-plan-zeile', { hasText: 'Athen' }).waitFor();
  assert.deepEqual(await reihenfolge(), ['Athen – Teilbarkeit', 'New York – Zinsen', 'Rom – Natürliche Zahlen']);
  // Danach wird mit der neuen Revision gespeichert.
  await page.locator('.lern-plan-zeile', { hasText: 'Rom' }).locator('.lern-plan-ort').click();
  await page.getByRole('button', { name: 'Rom – Natürliche Zahlen aus dem Plan nehmen' }).click();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen').at(-1).daten, { lernender_id: 1, revision: 7, eintraege: [{ block_id: 48, kann_schon: false }, { block_id: 52, kann_schon: false }] });
});

test('Info-Seite „So funktioniert’s“: ein Tipp von der Startseite und vom Flugplan, Erste Schritte und Fragen', async (t) => {
  const { page } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/lernen/#/lernen');
  await page.getByRole('link', { name: 'Flugplan Kind A' }).waitFor();
  // oben rechts, vor allem anderen
  const link = page.locator('#main > .lern-info-oben a', { hasText: 'So funktioniert’s' });
  const box = await link.boundingBox(); assert.ok(box.x + box.width > 820 / 2 && box.y < 200, 'Link oben rechts: ' + JSON.stringify(box));
  await link.click();
  await page.waitForURL(/#\/info$/);
  await page.getByRole('heading', { name: 'Erste Schritte' }).waitFor();
  assert.deepEqual(await page.locator('.lern-info-schritt h3').allInnerTexts(), ['Flugplan prüfen', 'Lernstand lesen', 'Inhalte ansehen', 'Ändern lassen']);
  assert.equal(await page.locator('details.lern-info-frage').count(), 7);
  await page.getByText('Wie wird gelernt?').click();
  await page.getByText('6 eigene Lösungen (richtig im ersten Versuch ohne Tipp', { exact: false }).waitFor();
  await page.getByText('nach 1, 3, 7, 14 und 30 Lerntagen', { exact: false }).waitFor();
  await page.getByText('höchstens 6 Wiederholungen', { exact: false }).waitFor();
  await page.getByText('Zuerst kommt die Erklärung', { exact: false }).waitFor();
  await page.getByText('zuerst einen zweiten Versuch', { exact: false }).waitFor();
  const text = await page.locator('#main').innerText();
  assert.doesNotMatch(text, /Lernkarte|Aufgabe|Thema\b|Themen|Themenplan/, 'nur Reisewörter');
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/info-820.png'), fullPage: true });
  // aus dem Flugplan mit einem Tipp
  await page.getByRole('link', { name: 'Flugplan Kind A ›' }).click();
  await page.locator('.lern-plan-zeile').first().waitFor();
  await page.locator('.lern-info-oben a', { hasText: 'So funktioniert’s' }).click();
  await page.waitForURL(/#\/info$/);
  // Kinder kommen nicht auf die Info-Seite.
});

test('Reisewörter auf allen Eltern-/Lehrerseiten', async (t) => {
  const { page } = await setup(t);
  const verboten = /Lernkarte|Aufgabe|\bThema\b|\bThemen\b|Themenplan|Lernziel|Gebiet/; // Befund 5 der Nachprüfung E-1: \bThemen?\b traf „Thema“ nicht
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion === 'schule_zugaenge') return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, zugaenge: [{ id: 1, name: 'Herr Lehrer', rolle: 'lehrer', aktiv: true, zuletzt: null }] } }) });
    return route.fallback();
  });
  for (const [pfad, warte] of [['lernen', 'Lehrplan-Übersicht'], ['plan/1', 'Lehrplan'], ['lehrplan', 'Lehrplan-Übersicht'], ['inhalte/1', 'Bordkarten zum Üben'], ['wackelt/1', 'Was wackelt?'], ['lernstand/1', 'Einstieg prüfen'], ['schulstand', 'Alle Kinder im Vergleich'], ['lernauftraege', 'Neuer Auftrag (allgemein)'], ['zugaenge', 'Neuen Zugang anlegen'], ['info', 'Erste Schritte']]) {
    await page.goto(origin + '/#/' + pfad);
    await page.getByText(warte, { exact: false }).first().waitFor();
    await page.evaluate(() => document.querySelectorAll('#main details').forEach((d) => { d.open = true; }));
    // Inhalte der Mathematik (Titel aus der Datenbank, Texte der Kinder) sind keine App-Texte: nur feste Texte prüfen.
    const text = await page.evaluate(() => { const c = document.querySelector('#main').cloneNode(true);
      c.querySelectorAll('.lp-erkl, .lp-tabelle, .lern-rm-text, .lern-rm-antwort, .ls-fehler p, .lern-plan-themen b, .lp-text > b, .ls-kopf b, .lern-katalog b').forEach((x) => x.remove());
      c.querySelectorAll('select option').forEach((o) => { o.textContent = o.textContent; });
      return c.innerText.replaceAll('Mehr Aufgaben zum Runden.', '').replaceAll('6 neue Aufgaben ergänzt.', '').replaceAll('= ein Mathe-Thema', '') + ' ' + // die gewollte Erklärung auf der Info-Seite
 [...c.querySelectorAll('[placeholder],[aria-label]')].map((x) => (x.getAttribute('placeholder') || '') + ' ' + (x.getAttribute('aria-label') || '')).join(' '); });
    const treffer = text.match(new RegExp(verboten.source, 'g'));
    assert.equal(treffer, null, `${pfad}: ${treffer && text.slice(Math.max(0, text.search(verboten) - 60), text.search(verboten) + 60)}`);
  }
});

// ---------- Bau-Auftrag Phase 2, Schritt A: Befunde N1–N8 der Nachprüfung vom 16.11. ----------
const echteEtappe = (datei, titel) => JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themen', datei), 'utf8')).inhalt.etappen.find((e) => e.titel.includes(titel));
async function erklaerSeite(t, etappen, breite = 390) {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.setViewportSize({ width: breite, height: 900 });
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion !== 'schule_einheit_lesen') return route.fallback();
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, einheit_id: 1, status: 'geprueft', inhalt: { ziel: 'Test', etappen },
      uebungen: [], stand: etappen.map((x) => ({ lernziel: x.lernziel, pflicht: true, status: 'offen' })), etappen_stand: {}, laufender_test: null } }) });
  });
  return page;
}
// Vergleich ohne die Hervorhebung des Neuen (Klasse „neu“, größere Punkte)
const bilderDerKarte = (page) => page.evaluate(() => [...document.querySelectorAll('.lr-erklaert .lr-bild')].map((b) => { const c = b.cloneNode(true);
  c.querySelectorAll('.neu, .neu-text').forEach((x) => { x.classList.remove('neu', 'neu-text'); if (x.tagName === 'circle') x.removeAttribute('r'); }); return c.innerHTML.replace(/lk[a-z0-9]{3,8}/g, ''); }));

test('N1: Bildergeschichte zeigt ein Bild nur, wenn es sich ändert; Neues ist hervorgehoben; Etappe auf dem Handy kurz', async (t) => {
  const neg = echteEtappe('zahlen.ganz.json', 'negative Zahl');
  const page = await erklaerSeite(t, [neg]);
  await page.goto(origin + '/#/lerneinheit/1-1-erklaeren-1');
  await page.locator('.lr-erklaert').waitFor();
  const bilder = await bilderDerKarte(page);
  for (let i = 1; i < bilder.length; i++) assert.notEqual(bilder[i], bilder[i - 1], `Bild ${i} gleicht dem vorigen`);
  assert.equal(await page.locator('.lr-sogehts li').count(), 3);
  assert.equal(await page.locator('.lr-sogehts li.mit-bild').count(), 1, 'nur Schritt 1 bringt ein neues Bild');
  assert.equal(await page.locator('.lr-sogehts .lern-thermo .pfeil.neu').count(), 1, 'neuer Stand in der Akzentfarbe');
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  assert.ok(h < 2400, 'Etappe auf dem Handy: ' + h + ' px');
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/n1-negative-zahl-390.png'), fullPage: true });
});

test('N1 und N8: Kerze (Kl. 8) – keine zwei gleichen Bilder, neue Punkte kräftig; Tablet: Bild links, Text rechts', async (t) => {
  const kerze = echteEtappe('funktionen.linear.json', 'Sachzusammenhang');
  const page = await erklaerSeite(t, [kerze], 820);
  await page.goto(origin + '/#/lerneinheit/1-1-erklaeren-1');
  await page.locator('.lr-erklaert').waitFor();
  const bilder = await bilderDerKarte(page);
  for (let i = 1; i < bilder.length; i++) assert.notEqual(bilder[i], bilder[i - 1], `Bild ${i} gleicht dem vorigen`);
  assert.ok(await page.locator('.lr-sogehts .punkt.neu').count() >= 2, 'neue Punkte (Start, leer) hervorgehoben');
  assert.ok(await page.locator('.lr-sogehts .hilfslinie.neu').count() >= 2, 'Steigungsdreieck hervorgehoben');
  // A2: Rest grau (nicht durchscheinend), Steigungsdreieck so breit wie im Inhalt (1 Einheit), nur Bilder mit Neuem abgeblendet
  const graph = page.locator('.lr-sogehts svg.mit-neu path.graph').first();
  assert.equal(await graph.evaluate((x) => getComputedStyle(x).opacity), '1');
  assert.equal(await graph.evaluate((x) => getComputedStyle(x).stroke), 'rgb(154, 163, 178)');
  const dreieck = await page.locator('.lr-sogehts line.hilfslinie.neu').first().evaluate((l) => Number(l.getAttribute('x2')) - Number(l.getAttribute('x1')));
  // Siebzehnte Runde: Das Dreieck steht im Inhalt jetzt 2 Einheiten breit (Text: „In 2 Stunden … 3 cm“); die App zeichnet es so, wie es im Inhalt steht.
  assert.ok(dreieck > 30 && dreieck < 44, 'zwei Einheiten breit wie im Inhalt (≈ 35 px): ' + dreieck);
  assert.equal(await page.evaluate(() => typeof lernDreieckGross), 'undefined');
  for (const li of await page.locator('.lr-sogehts li.mit-bild').all()) {
    const b = await li.locator('.lr-bild').boundingBox(), x = await li.locator('.lr-schritt-text').boundingBox();
    assert.ok(x.x >= b.x + b.width - 1, 'Text rechts neben dem Bild');
    assert.ok(x.y < b.y + b.height && x.y + x.height > b.y, 'Text und Bild in derselben Zeile');
  }
  await page.screenshot({ path: path.join(root, 'test-results/n1-n8-kerze-820.png'), fullPage: true });
});

test('A2/N2: „Kurz gesagt“ ist bei allen Merksätzen aus inhalte/themen höchstens ein Satz', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const regeln = fs.readdirSync(path.join(root, 'inhalte/themen')).filter((f) => f.endsWith('.json'))
    .flatMap((f) => JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themen', f), 'utf8')).inhalt.etappen || []).map((e) => e.regel).filter(Boolean);
  assert.ok(regeln.length > 500);
  const zwei = await page.evaluate((rs) => rs.map((r) => lernKurzGesagt(r)).filter((k) => { const e = lernSatzEnde(k); return e > 0 && e < k.length; }), regeln);
  assert.deepEqual(zwei, []);
  // unabhängige Gegenprobe: kein „Satzende + Großbuchstabe“ mehr, außer nach den Abkürzungen und Aufzählungen
  const verdacht = await page.evaluate((rs) => rs.map((r) => lernKurzGesagt(r)).filter((k) => /(?<!\b(?:z\.\s?B|d\.\s?h|u\.\s?a|bzw|ca|usw|vgl|[zdu]|(?<!:\s?)\d{1,2}|:\s?1))[.!?]\s+[A-ZÄÖÜ]/.test(k.replace(/\b\d+,\d+\./g, '#'))), regeln);
  assert.deepEqual(verdacht, []);
  assert.deepEqual(await page.evaluate(() => ['Unter null schreibst du ein Minus, z. B. −3. Das ist kalt.', 'Man rechnet ca. 5 Stück, d. h. viel. Fertig!', 'Ist das so? Ja.', 'Die 3. Wurzel ist gemeint. Mehr.',
    'Arithmetische Reihe: ⟦Sₙ = n · (a₁ + aₙ) : 2⟧. Erstes plus letztes Glied.', 'So geht es: 1. Kürzen, 2. Multiplizieren. Fertig.', 'Teile durch 2. Dann fertig.'].map(lernKurzGesagt)),
    ['Unter null schreibst du ein Minus, z. B. −3.', 'Man rechnet ca. 5 Stück, d. h. viel.', 'Ist das so?', 'Die 3. Wurzel ist gemeint.',
      'Arithmetische Reihe: Sₙ = n · (a₁ + aₙ) : 2.', 'So geht es: 1. Kürzen, 2. Multiplizieren.', 'Teile durch 2.']); // P1: „: 2.“ ist keine Aufzählung
});

test('A2/N1: Tabelle und Stellentafel – nur die geänderte Zelle ist hervorgehoben', async (t) => {
  const tab = { lernziel: 'tab', titel: 'Tabelle', regel: 'Regel.', bild: { typ: 'tabelle', kopf: ['x', 'y'], zeilen: [['1', '2'], ['2', '4'], ['3', '?']] },
    schritte: [{ text: 'Erst lesen.' }, { text: 'Dann ergänzen.', bild: { zeilen: [['1', '2'], ['2', '4'], ['3', '6']] } }] };
  const st = { lernziel: 'st', titel: 'Stellen', regel: 'Regel.', bild: { typ: 'stellentafel', stellen: ['T', 'H', 'Z', 'E'], ziffern: ['4', '0', '5', '2'], markiert: 0 },
    schritte: [{ text: 'Die 5 steht bei den Zehnern.', bild: { markiert: 2 } }] };
  const page = await erklaerSeite(t, [tab, st]);
  await page.goto(origin + '/#/lerneinheit/1-1-erklaeren-1');
  await page.locator('.lr-sogehts .lr-tafel').waitFor();
  assert.deepEqual(await page.locator('.lr-sogehts .lr-tafel .neu').allInnerTexts(), ['6']);
  await page.goto(origin + '/#/lerneinheit/1-1-erklaeren-2');
  await page.locator('.lr-sogehts .lr-stellentafel').waitFor();
  assert.deepEqual(await page.locator('.lr-sogehts .lr-stellentafel td.neu').allInnerTexts(), ['5']);
});

test('N2: „Kurz gesagt“ in der Übersicht ganz, ohne „…“', async (t) => {
  const neg = echteEtappe('zahlen.ganz.json', 'negative Zahl');
  const lang = { ...neg, lernziel: 'lang', titel: 'Lang', regel: 'Unter null schreibst du ein Minus vor die Zahl, zum Beispiel minus drei Grad, und über null kein Zeichen davor. Danach kommt mehr.' };
  const page = await erklaerSeite(t, [neg, lang]);
  await page.goto(origin + '/#/lerneinheit/1-1-erklaeren');
  const kurz = page.locator('.lr-kachel-kurz').nth(1);
  await kurz.waitFor();
  assert.equal(await kurz.innerText(), 'Kurz gesagt: Unter null schreibst du ein Minus vor die Zahl, zum Beispiel minus drei Grad, und über null kein Zeichen davor.');
  assert.equal(await kurz.evaluate((x) => getComputedStyle(x).webkitLineClamp), 'none');
});

test('N3: Kurs-Grafik – Komma-Platz ohne Komma bleibt leer (0,24 statt 24)', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1');
  await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const kurs = await page.evaluate(() => { const k = lernKurs({ antworttyp: 'zahl', loesung: { wert: 24 } }, { wert: '0,24' });
    return [...k.querySelectorAll('.lr-kurs-zeile')].map((z) => [...z.querySelectorAll('.lr-kurs-kachel')].map((c) => c.className.replace('lr-kurs-kachel', '').trim() + ':' + c.textContent)); });
  const ziel = kurs.at(-1), du = kurs.at(-2);
  assert.ok(du.some((c) => c.startsWith('komma') && c.endsWith(':,')), 'DU hat das Komma: ' + du);
  const platz = ziel.find((c) => c.startsWith('komma'));
  assert.ok(platz && !platz.includes('ab') && platz.endsWith(':'), 'ZIEL ohne Komma und ohne Rahmen am Komma-Platz: ' + ziel);
});

test('N4: Startknopf „Erst 1 Wiederholung ›“, danach „Weiter nach Rom ›“', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion !== 'schule_wiederholung') return route.fallback();
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, faellig: 1, aufgaben: [{ ...AUFG[11], einheit_id: 2, stadt: 'New York' }] } }) });
  });
  await page.goto(origin + '/#/reise/1');
  const knopf = page.locator('.lr-einsteigen-knopf');
  await knopf.waitFor();
  assert.equal((await knopf.innerText()).replace(/\s+/g, ' ').trim(), 'Erst 1 Wiederholung ›');
  await page.evaluate(() => lernWdhHeute(1, true));
  await page.reload(); await knopf.waitFor();
  assert.equal((await knopf.innerText()).replace(/\s+/g, ' ').trim(), 'Weiter nach Rom ›');
});

test('N5–N7: Detektiv nur ohne Fehlermuster; Test-Kopf „Ort · Flug“; Testergebnis mit Abflug-Knöpfen und grüner Markierung', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  // N5 (Code): der Detektiv hängt an LERN_GRUND – mit erkanntem Muster kein Detektiv
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByRole('heading', { name: 'Rom · Natürliche Zahlen' }).waitFor(); // N6
  // M6: bei Auswahl-Bordkarten ohne Muster je Option ein neutraler Satz statt des Etappen-Musters
  assert.deepEqual(await page.evaluate(() => { const e = { fehler: 'Muster X' };
    return [!!lernDetektiv({ antworttyp: 'zahl' }, e, { grund: 'vorzeichen' }, 'T'), lernDetektiv({ antworttyp: 'zahl' }, e, {}, 'T')?.textContent, lernDetektiv({ antworttyp: 'auswahl' }, e, {}, 'T')?.textContent]; }),
    [false, 'TMuster X', 'NOCH EINMAL HINSEHENSchau dir deine Wahl und die Frage noch einmal an.']);
  await page.getByRole('button', { name: 'Test starten' }).click();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
  await page.getByRole('button', { name: 'Weiter ›' }).click();
  await page.getByRole('button', { name: 'Markierung 2' }).click();
  await page.getByRole('button', { name: 'Abgeben' }).click();
  await page.getByText('1 von 2 richtig').waitFor();
  const knoepfe = page.locator('.lr-test-knoepfe');
  assert.deepEqual((await knoepfe.locator('a').allInnerTexts()).map((x) => x.trim()), ['Erst üben: Zahlenstrahl ›', 'Verbessern ›', 'Zum Flug', 'Zur Abflugtafel']);
  assert.equal(await knoepfe.locator('a.lr-knopf').getAttribute('href'), '#/lerneinheit/1-1-ueben-2');
  assert.equal(await knoepfe.locator('a.lr-knopf-zweit').getAttribute('href'), '#/lerneinheit/1-1-test');
  assert.equal(await page.locator('.btn.primary, .btn.secondary').count(), 0);
  assert.equal(await page.locator('.lern-strahl .marke-richtig').count(), 1, 'richtige Markierung grün');
  assert.equal(await page.locator('.lern-strahl .marke-richtig').evaluate((x) => getComputedStyle(x).stroke), 'rgb(46, 158, 68)', 'A2: festes Grün');
  assert.equal(await page.locator('.lern-strahl .marke-falsch').count(), 1, 'gewählte falsche Markierung');
  await page.screenshot({ path: path.join(root, 'test-results/n7-testergebnis-390.png'), fullPage: true });
});

test('K2: Mein Weg – Reiter Stand · Kontinente · Karte; Antarktis von oben; alte Weltkarte führt in den Reiter Karte', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/weg/1');
  const reiter = page.locator('.lr-weg-reiter a');
  await reiter.first().waitFor();
  assert.deepEqual(await reiter.allInnerTexts(), ['Stand', 'Kontinente', 'Karte']);
  assert.equal(await page.locator('.lr-weg-reiter a.on').innerText(), 'Stand');
  await page.locator('.lr-linienplan').waitFor(); // K3: Linienplan ersetzt die alte Box „Mein Stand · Gymnasium Klasse 5“
  assert.equal(await page.locator('.lr-mini3 .lr-mini').count(), 3);
  await reiter.nth(1).click();
  await page.waitForURL(/#\/weg\/1-kontinente$/);
  const kont = page.locator('details.lr-kontinent');
  await kont.first().waitFor();
  assert.deepEqual(await page.locator('.lr-kontinent-kopf b').allInnerTexts(), ['Zahlen', 'Geld und Verhältnisse']);
  await page.screenshot({ path: path.join(root, 'test-results/k2-kontinente-390.png'), fullPage: true });
  await page.goto(origin + '/#/weltkarte/1');
  await page.waitForURL(/#\/weg\/1-karte$/);
  await page.locator('.lr-weg-reiter a.on', { hasText: 'Karte' }).waitFor();
  // Antarktis von oben (Testdaten): eigene Karte mit dem Südpol in der Mitte
  await page.evaluate(() => { const box = document.querySelector('.lr-karte-box'); box.replaceChildren(lernPolarKarte([
    { stadt: 'Neumayer-Station III', lat: -70.67, lon: -8.27, zustand: 'jetzt' }, { stadt: 'McMurdo', lat: -77.85, lon: 166.67, zustand: 'offen' }])); });
  const polar = page.locator('svg.lr-karte-polar');
  await polar.waitFor();
  const land = await polar.locator('path.lr-land-AN').getAttribute('d');
  assert.ok(land.split('L').length > 300, 'Umriss der Antarktis');
  const box = await polar.boundingBox(); assert.ok(Math.abs(box.width - box.height) < 2, 'quadratisch, von oben');
  // Neumayer liegt bei 8° West nahe am oberen Rand (0° oben), McMurdo unten
  const [n, m] = await polar.locator('circle.lr-punkt').evaluateAll((cs) => cs.map((c) => Number(c.getAttribute('cy'))));
  assert.ok(n < 150 && m > 150, `Neumayer oben, McMurdo unten: ${n} / ${m}`);
  await polar.screenshot({ path: path.join(root, 'test-results/k2-antarktis.png') });
});

test('K2: Flüge im Ort nach Lehrplan-Reihenfolge, sobald die Übersicht sie liefert', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1');
  await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const reihe = await page.evaluate(() => {
    const u = { orte: [{ block_id: 49 }], lernende: [{ id: 1, klasse: 5, route: [{ block_id: 49, position: 1, art: 'normal', status: 'offen' }], stand: [] }],
      einheiten: [{ id: 7, block_id: 49, titel: 'B', reihenfolge: { gym_by: 2 } }, { id: 8, block_id: 49, titel: 'A', reihenfolge: { gym_by: 1 } }, { id: 6, block_id: 49, titel: 'ohne' }] };
    const ohne = { ...u, einheiten: u.einheiten.map(({ reihenfolge, ...e }) => e) };
    return [lernReiseDaten(u, 1).mit.map((e) => e.titel), lernReiseDaten(ohne, 1).mit.map((e) => e.titel)];
  });
  assert.deepEqual(reihe, [['A', 'B', 'ohne'], ['ohne', 'B', 'A']]);
});

// ---------- Schritt C: E-2 Flugplan in zwei Spalten mit Ziehen, Flüge abwählbar; E-3 „Ändern lassen“ ----------
// Plan wie in der Datenbank nach Migration 20261117_w150_e2_*: speichert Reihenfolge, kann_schon und ausgelassen, prüft die Revision.
async function planDb(page, calls, { orte, plan, kannAbwaehlen = true }) {
  const db = { revision: 1, eintraege: plan.map((b) => ({ block_id: b, kann_schon: false, ausgelassen: [] })) };
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); const d = b.daten || {};
    const antwort = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
    if (b.aktion === 'schule_plan_setzen') {
      calls.push(b);
      if (d.revision !== db.revision) return route.fulfill({ status: 400, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Der Plan wurde inzwischen geändert. Bitte neu laden.' }) });
      db.revision++; db.eintraege = d.eintraege.map((x) => ({ ausgelassen: [], ...x })); return antwort({ ok: true, revision: db.revision });
    }
    if (b.aktion === 'schule_plan_lesen') return antwort({ ok: true, ...(kannAbwaehlen ? { kann_abwaehlen: true } : {}), kind: { id: 1, name: 'Kind A', klasse: 5, schulart: 'gym_by' }, revision: db.revision, orte, notizen: [], verlauf: [],
      plan: db.eintraege.map((x, i) => ({ block_id: x.block_id, position: i + 1, art: 'normal', status: 'offen', kann_schon: x.kann_schon, ...(kannAbwaehlen ? { ausgelassen: x.ausgelassen } : {}) })) });
    return route.fallback();
  });
  return db;
}
const STAEDTE = ['Rom', 'Athen', 'Paris', 'Kairo', 'Lima', 'Oslo', 'Wien', 'Prag', 'Bern', 'Melbourne', 'Tokio', 'Quito', 'Delhi', 'Accra'];
const vieleOrte = () => STAEDTE.map((s, i) => ({ block_id: 100 + i, titel: 'Flugort ' + (i + 1), stadt: s, kontinent: 'Zahlen',
  themen: [{ thema_id: 500 + 2 * i, titel: 'Flug A ' + s, jahrgang: { gym_by: 5 }, stand: 'offen', einheit: { id: 900 + i, status: 'geprueft', karten: 6, aufgaben: 40, neu: 0 } },
    { thema_id: 501 + 2 * i, titel: 'Flug B ' + s, jahrgang: { gym_by: 6 }, stand: 'offen', einheit: null }] }));

test('E-2: Flugplan – Platz 10 → 2 mit einer Ziehbewegung, 12 Orte auf einem Tablet, Zeilen höchstens 72 px', async (t) => {
  const { page, calls } = await setup(t);
  await page.setViewportSize({ width: 820, height: 1180 });
  const db = await planDb(page, calls, { orte: vieleOrte(), plan: STAEDTE.slice(0, 12).map((_, i) => 100 + i) });
  await page.goto(origin + '/#/plan/1');
  const zeilen = page.locator('.lern-plan-zeile');
  await zeilen.nth(11).waitFor();
  const hoehen = await zeilen.evaluateAll((zs) => zs.map((z) => z.getBoundingClientRect().height));
  assert.ok(Math.max(...hoehen) <= 72, 'zugeklappt höchstens 72 px: ' + Math.max(...hoehen));
  const letzte = await zeilen.nth(11).boundingBox();
  assert.ok(letzte.y + letzte.height <= 1180, '12 Orte passen auf einen Tablet-Bildschirm: ' + Math.round(letzte.y + letzte.height));
  await page.screenshot({ path: path.join(root, 'test-results/e2-flugplan-820.png') });
  // Melbourne (Platz 10) mit einer Ziehbewegung auf Platz 2
  const griff = zeilen.nth(9).locator('.lern-plan-griff'); const g = await griff.boundingBox();
  const ziel = await zeilen.nth(1).boundingBox();
  await page.mouse.move(g.x + g.width / 2, g.y + g.height / 2); await page.mouse.down();
  await page.mouse.move(g.x + g.width / 2, ziel.y + 6, { steps: 12 }); await page.mouse.up();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  const gesetzt = calls.filter((c) => c.aktion === 'schule_plan_setzen');
  assert.equal(gesetzt.length, 1, 'eine Ziehbewegung = ein Speichern');
  assert.deepEqual(gesetzt[0].daten.eintraege.slice(0, 3).map((x) => x.block_id), [100, 109, 101]);
  assert.equal(await zeilen.nth(1).locator('.lern-plan-ort b').innerText(), 'Melbourne – Flugort 10');
  // Seite verlassen und zurück: Melbourne bleibt auf Platz 2
  await page.goto(origin + '/#/lernen'); await page.getByRole('link', { name: 'Flugplan Kind A' }).waitFor();
  await page.goto(origin + '/#/plan/1'); await zeilen.nth(1).waitFor();
  assert.equal(await zeilen.nth(1).locator('.lern-plan-ort b').innerText(), 'Melbourne – Flugort 10');
  assert.equal(db.eintraege[1].block_id, 109);
});

test('E-2: Ort aus dem Lehrplan in den Plan ziehen; Finger (Touch) zieht ebenso', async (t) => {
  const { page, calls } = await setup(t);
  await page.setViewportSize({ width: 1280, height: 900 });
  await planDb(page, calls, { orte: vieleOrte(), plan: [100, 101, 102] });
  await page.goto(origin + '/#/plan/1');
  await page.locator('.lern-plan-zeile').nth(2).waitFor();
  const quelle = page.locator('.lern-plan-vorrat-zeile', { hasText: 'Kairo' }).locator('.lern-plan-griff'); const q = await quelle.boundingBox();
  const ziel = await page.locator('.lern-plan-zeile').nth(1).boundingBox();
  await page.mouse.move(q.x + 10, q.y + 10); await page.mouse.down();
  await page.mouse.move(ziel.x + 80, ziel.y + 4, { steps: 10 }); await page.mouse.up();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen')[0].daten.eintraege.map((x) => x.block_id), [100, 103, 101, 102]);
  // Touch: dieselben Pointer-Ereignisse mit pointerType touch
  const g = await page.locator('.lern-plan-zeile').nth(3).locator('.lern-plan-griff').boundingBox();
  const oben = await page.locator('.lern-plan-zeile').nth(0).boundingBox();
  await page.evaluate(({ x, y, y2 }) => {
    const ziel = document.elementFromPoint(x, y); const opt = (yy) => ({ bubbles: true, pointerId: 7, pointerType: 'touch', isPrimary: true, clientX: x, clientY: yy, button: 0 });
    ziel.dispatchEvent(new PointerEvent('pointerdown', opt(y)));
    for (let i = 1; i <= 8; i++) window.dispatchEvent(new PointerEvent('pointermove', opt(y + (y2 - y) * i / 8)));
    window.dispatchEvent(new PointerEvent('pointerup', opt(y2)));
  }, { x: g.x + g.width / 2, y: g.y + g.height / 2, y2: oben.y + 4 });
  for (let i = 0; i < 40 && calls.filter((c) => c.aktion === 'schule_plan_setzen').length < 2; i++) await page.waitForTimeout(50);
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen')[1].daten.eintraege.map((x) => x.block_id), [102, 100, 103, 101]);
  assert.equal(await page.locator('.lern-plan-griff').first().evaluate((x) => getComputedStyle(x).touchAction), 'none');
  await page.screenshot({ path: path.join(root, 'test-results/e2-flugplan-1280.png') });
});

test('E-2: Flug im Ort abwählen – gespeichert als ausgelassen, Kind sieht ihn nicht; ohne Migration keine Häkchen', async (t) => {
  const { page, calls } = await setup(t);
  await planDb(page, calls, { orte: vieleOrte(), plan: [100, 101] });
  await page.goto(origin + '/#/plan/1');
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.locator('.lern-plan-ort').click();
  await rom.getByLabel('Flug B Rom im Plan').uncheck();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen')[0].daten.eintraege[0], { block_id: 100, kann_schon: false, ausgelassen: [501] });
  await rom.getByText('1 abgewählt', { exact: false }).waitFor();
  // Kinderansicht: ausgelassener Flug fehlt (thema_id aus der Übersicht)
  const sicht = await page.evaluate(() => {
    const u = { orte: [{ block_id: 100 }], lernende: [{ id: 1, klasse: 5, route: [{ block_id: 100, position: 1, art: 'normal', status: 'offen', ausgelassen: [501] }], stand: [] }],
      einheiten: [{ id: 1, block_id: 100, thema_id: 500, titel: 'A' }, { id: 2, block_id: 100, thema_id: 501, titel: 'B' }] };
    const ohne = { ...u, einheiten: u.einheiten.map(({ thema_id, ...e }) => e) };
    return [lernReiseDaten(u, 1).mit.map((e) => e.titel), lernReiseDaten(ohne, 1).mit.map((e) => e.titel)];
  });
  assert.deepEqual(sicht, [['A'], ['A', 'B']]);
});

test('E-2 ohne Migration: Plan läuft wie bisher, ohne Häkchen und ohne Feld ausgelassen', async (t) => {
  const { page, calls } = await setup(t);
  await planDb(page, calls, { orte: vieleOrte(), plan: [100, 101], kannAbwaehlen: false });
  await page.goto(origin + '/#/plan/1');
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.locator('.lern-plan-ort').click();
  await rom.getByText('Einzelne Flüge abwählen geht, sobald', { exact: false }).waitFor();
  assert.equal(await rom.getByRole('checkbox', { name: /im Plan/ }).count(), 0);
  await page.getByRole('button', { name: 'Athen – Flugort 2 nach oben' }).click();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen')[0].daten.eintraege, [{ block_id: 101, kann_schon: false }, { block_id: 100, kann_schon: false }]);
});

test('E-2: Startseite je Kind ein Bereich mit drei Schularten; darunter „Für alle Kinder“', async (t) => {
  const { page } = await setup(t);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lernen');
  const a = page.locator('.lern-kindbereich', { hasText: 'Kind A' });
  await a.waitFor();
  assert.deepEqual(await a.locator('.lern-mini-name').allInnerTexts(), ['GYM 5', 'RS 5', 'IB vor MYP-Jahr 1']); // IB: MYP-Jahr = Klasse − 5 → Klasse 5 steht vor MYP-Jahr 1
  await a.getByText('Jetzt: Rom · Natürliche Zahlen (2/4)').waitFor();
  assert.deepEqual(await a.locator('.lern-kindbereich-knoepfe a').allInnerTexts(), ['Lernen starten ›', 'Lernstand', 'Was wackelt?', 'Flugplan']);
  assert.equal(await page.locator('.lern-kindbereich').count(), 2, 'je Kind ein Bereich (Testkind nicht)');
  await page.getByText('FÜR ALLE KINDER').waitFor();
  for (const t2 of ['Lehrplan-Übersicht', 'Meine Aufträge', 'So funktioniert’s']) await page.locator('.lern-kinderliste').getByText(t2, { exact: true }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/e2-startseite-820.png'), fullPage: true });
});

test('E-3: derselbe Knopf an Erklärung, Etappe, Flug und Plan; der Auftrag trägt den Bezug', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/inhalte/1');
  await page.getByText('Bordkarten zum Üben', { exact: false }).waitFor();
  await page.evaluate(() => document.querySelectorAll('details.lp-karte').forEach((d) => { d.open = true; }));
  const knoepfe = page.locator('details.lern-aendern > summary');
  assert.ok(await knoepfe.count() >= 2);
  assert.deepEqual([...new Set(await knoepfe.allInnerTexts())], ['✎ Ändern lassen']);
  await page.locator('details.lern-aendern').first().locator('summary').click(); // oben: der Flug als Ganzes
  const f = page.locator('details.lern-aendern').first();
  await f.getByText('An: Flug', { exact: false }).waitFor();
  await f.getByRole('button', { name: 'Fehler' }).click();
  await f.getByRole('button', { name: 'Lösung falsch' }).click();
  assert.equal(await f.getByLabel('Was soll anders sein?').inputValue(), 'Lösung falsch: ');
  await f.getByLabel('Was soll anders sein?').fill('Lösung falsch: Bordkarte 7 muss −56 sein.');
  await f.getByRole('button', { name: 'Auftrag senden' }).click();
  await f.getByText('Danke – der Auftrag ist angekommen', { exact: false }).waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten, { einheit_id: 1, bezug: 'flug', art: 'fehler', text: 'Lösung falsch: Bordkarte 7 muss −56 sein.' });
  // Plan: derselbe Knopf, Bezug „plan“
  await page.goto(origin + '/#/plan/1');
  await page.locator('.lern-plan-lehrplan details.lern-aendern > summary', { hasText: '✎ Ändern lassen' }).waitFor();
});


// ---------- Schritt D: K3 Stand über Schularten (Kind), K4 Eltern-Ansicht mit Einstiegs-Check, E-4 Plan aus Lehrplan-Vorlage ----------
// Übersicht wie nach Migration 20261117_w150_d_*: alle Flüge in „themen“ (auch ohne Inhalt), „stufen“ je Kind.
const D_THEMEN = [
  { thema_id: 15, titel: 'Natürliche Zahlen', jahrgang: { gym_by: 5, rs_by: 5, ib_myp: 1 }, reihenfolge: { gym_by: 1 }, block_id: 49, stadt: 'Rom', kontinent: 'Zahlen', erdteil: 'Europa', einheit_id: 1 },
  { thema_id: 16, titel: 'Ganze Zahlen', jahrgang: { gym_by: 5, rs_by: 5, ib_myp: 2 }, reihenfolge: { gym_by: 2 }, block_id: 49, stadt: 'Rom', kontinent: 'Zahlen', erdteil: 'Europa', einheit_id: null },
  { thema_id: 17, titel: 'Teilbarkeit', jahrgang: { gym_by: 5, rs_by: 6 }, reihenfolge: { gym_by: 3 }, block_id: 48, stadt: 'Athen', kontinent: 'Zahlen', erdteil: 'Europa', einheit_id: null },
  { thema_id: 71, titel: 'Einfache Zinsen', jahrgang: { gym_by: 6, rs_by: 7 }, reihenfolge: {}, block_id: 52, stadt: 'New York', kontinent: 'Geld und Verhältnisse', erdteil: 'Nordamerika', einheit_id: 2 },
  { thema_id: 30, titel: 'Terme', jahrgang: { gym_by: 7, rs_by: 7, ib_myp: 2 }, reihenfolge: {}, block_id: 60, stadt: 'Samarkand', kontinent: 'Algebra', erdteil: 'Asien', einheit_id: null }];
const standAnpassen = ({ mitThemen = true, bisSitzt } = {}) => (aktion, e) => {
  if (aktion === 'schule_uebersicht') {
    const u = structuredClone(e);
    u.lernende[0].route = [{ block_id: 49, position: 1, art: 'normal', status: 'offen', kann_schon: false }, { block_id: 48, position: 2, art: 'normal', status: 'fertig', kann_schon: false }, { block_id: 52, position: 3, art: 'normal', status: 'offen', kann_schon: false }];
    u.lernende[0].stand = [{ einheit_id: 1, fertig: 4, fehler: 0, gesichert: 4, blocktest: false, laeuft: false }, { einheit_id: 2, fertig: 1, fehler: 2, gesichert: 0, blocktest: false, laeuft: false }];
    if (mitThemen) { u.themen = D_THEMEN; u.lernende[0].stufen = { rs_by: 6 }; u.lernende[1].stufen = {}; } else u.einheiten[0].jahrgang = { gym_by: 5, rs_by: 5 }; // wie die Übersicht vor Migration D: Klasse nur an Flügen mit Inhalt
    return u;
  }
  if (aktion === 'schule_lernstand' && bisSitzt) { const l = structuredClone(e); Object.assign(l.einheiten[0].karten[0], { bis_sitzt: bisSitzt, sitzt_am: '2026-11-14T08:00:00Z' }); return l; }
  return null;
};

test('K3: Abflugtafel mit Mini-Linien GYM · RS · IB; Mein Weg · Stand in drei Ebenen (Linienplan → Klasse → Kontinent)', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: standAnpassen() });
  await page.goto(origin + '/#/reise/1');
  const mini = page.locator('.lr-mini3 .lr-mini');
  await mini.first().waitFor();
  // Rechenregel: GYM 5 = Rom (gelandet, 4/4 Etappen), Rom „Ganze Zahlen“ (offen), Athen (Ort fertig) → 2 von 3; RS Stufe 6 aus „stufen“ → Athen 1/1; IB: Klasse 5 steht vor MYP-Jahr 1 (MYP-Jahr = Klasse − 5) → 0/0
  assert.deepEqual(await mini.evaluateAll((as) => as.map((a) => a.getAttribute('aria-label'))),
    ['Gymnasium Klasse 5: 2 von 3 Flügen gelandet', 'Realschule Klasse 6: 1 von 1 Flügen gelandet', 'IB vor MYP-Jahr 1: 0 von 0 Flügen gelandet']);
  assert.equal(await page.locator('.lr-jgstand').count(), 0, 'alte Jahrgangs-Box entfällt, wenn die Linien da sind');
  await mini.first().click();
  await page.waitForURL(/#\/weg\/1-stand-gym_by-5$/);
  // Ebene 2: Passkarte mit ‹ ›, Kontinente der Klasse
  await page.locator('.lr-pass-karte').waitFor();
  assert.equal(await page.locator('.lr-pass-kopf b').innerText(), 'KLASSE 5');
  assert.deepEqual(await page.locator('.lr-kontzeile-name b').allInnerTexts(), ['Zahlen']);
  await page.locator('.lr-pf[aria-label="nächste Klasse"]').click();
  await page.waitForURL(/#\/weg\/1-stand-gym_by-6$/);
  const geld = page.locator('.lr-kontzeile', { hasText: 'Geld und Verhältnisse' });
  assert.match(await geld.innerText(), /wackelt/);
  await geld.click();
  // Ebene 3: Flüge mit „zählt auch für“
  const zeile = page.locator('.lr-standzeile');
  await zeile.first().waitFor();
  assert.match(await zeile.first().innerText(), /Einfache Zinsen[\s\S]*zählt auch für RS 7[\s\S]*wackelt/);
  assert.equal(await page.locator('.lr-krumen a').count(), 2);
  await page.locator('.lr-krumen a').first().click();
  await page.waitForURL(/#\/weg\/1-stand$/);
  await page.locator('.lr-linienplan .lr-lp-halt').first().waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/k3-stand-390.png'), fullPage: true });
});

test('K3: ohne Migration D (keine „themen“) zählen die Flüge mit Inhalt, nichts bricht', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: standAnpassen({ mitThemen: false }) });
  await page.goto(origin + '/#/weg/1-stand');
  await page.locator('.lr-mini3 .lr-mini').first().waitFor();
  assert.equal(await page.locator('.lr-mini3 .lr-mini').first().getAttribute('aria-label'), 'Gymnasium Klasse 5: 1 von 1 Flügen gelandet');
});

test('K4: Eltern – Stand über Schularten: Übersicht, Landkarte mit Einstiegs-Check und Hinweis, Feld mit Bordkarten bis „sitzt“', async (t) => {
  const { page, calls } = await setup(t, { anpassen: standAnpassen({ bisSitzt: 9 }) });
  await page.goto(origin + '/#/lernen');
  await page.getByRole('link', { name: /Alle Kinder im Vergleich/ }).click();
  await page.waitForURL(/#\/schulstand$/);
  const felder = page.locator('.lern-stand-feld');
  await felder.first().waitFor();
  assert.equal(await felder.count(), 6, '2 Kinder × 3 Schularten (Testkind nicht)');
  assert.equal(await felder.nth(0).getAttribute('aria-label'), 'Kind A, Gymnasium Klasse 5: 2 von 3 gelandet');
  await felder.nth(0).click();
  await page.waitForURL(/#\/lernstand\/1-gym_by$/);
  await page.locator('.lern-stand-raster').waitFor();
  await page.getByText('Orientierung, keine Einstufung durch eine Schule').first().waitFor(); // erst lesen, wenn die Seite fertig gezeichnet ist (sonst gelegentlich „Lade …“)
  assert.match(await page.locator('main').innerText(), /Orientierung, keine Einstufung durch eine Schule/);
  // Einstieg prüfen Klasse 7: alles bis Klasse 6 = 3 Flüge Kl. 5 + 1 Flug Kl. 6 → 2 von 4 gelandet = 50 % → rot
  await page.locator('.lern-chips-zeile[aria-label="Einstieg prüfen"] a', { hasText: 'Kl. 7' }).click();
  await page.waitForURL(/#\/lernstand\/1-gym_by-7$/);
  const ampel = page.locator('.lern-ampel');
  await ampel.waitFor();
  assert.match(await ampel.getAttribute('class'), /\brot\b/);
  assert.match(await ampel.innerText(), /50 %[\s\S]*2 von 4 Flügen bis Klasse 6[\s\S]*Orientierung, keine Einstufung durch eine Schule/);
  assert.equal(await page.locator('.lern-zelle.aus').count(), 1, 'Felder ab Klasse 7 ausgegraut (Terme)');
  await page.locator('.lern-fehlt summary').click();
  assert.equal(await page.locator('.lern-fehlt .lern-standflug').count(), 2);
  await page.screenshot({ path: path.join(root, 'test-results/k4-landkarte-390.png'), fullPage: true });
  // Ebene 3: Feld Zahlen × Klasse 5 → Flüge mit Etappen, „sitzt – nach 9 Bordkarten“
  await page.locator('.lern-zelle', { hasText: '2/3' }).click();
  await page.waitForURL(/#\/lernstand\/1-gym_by-7-0-5$/);
  await page.locator('.lern-etappen-stand li').first().waitFor();
  assert.match(await page.locator('.lern-etappen-stand li').first().innerText(), /sitzt – nach 9 Bordkarten/);
  assert.ok(calls.some((c) => c.aktion === 'schule_lernstand' && c.daten.lernender_id === 1));
  // Lernstand zeigt die Zahl ebenfalls
  await page.getByRole('link', { name: /Was wackelt\?/ }).click();
  await page.locator('.ls-bis-sitzt').waitFor();
  assert.equal(await page.locator('.ls-bis-sitzt').innerText(), 'sitzt nach 9 Bordkarten');
});

test('E-4: Neuer Plan aus Lehrplan-Vorlage – Orte der Klasse in Lehrplan-Reihenfolge, andere Flüge abgewählt, Rückgängig', async (t) => {
  const { page, calls } = await setup(t);
  const orte = [
    { block_id: 200, titel: 'B', stadt: 'Oslo', kontinent: 'Zahlen', themen: [{ thema_id: 1, titel: 'Zweiter', jahrgang: { gym_by: 5 }, lehrplan_reihenfolge: { gym_by: 2 } }, { thema_id: 2, titel: 'Später', jahrgang: { gym_by: 6 } }] },
    { block_id: 201, titel: 'A', stadt: 'Wien', kontinent: 'Zahlen', themen: [{ thema_id: 3, titel: 'Erster', jahrgang: { gym_by: 5 }, lehrplan_reihenfolge: { gym_by: 1 } }] },
    { block_id: 202, titel: 'C', stadt: 'Prag', kontinent: 'Zahlen', themen: [{ thema_id: 4, titel: 'Nur 6', jahrgang: { gym_by: 6 } }] }];
  const db = await planDb(page, calls, { orte, plan: [202] });
  await page.goto(origin + '/#/plan/1');
  await page.locator('.lern-vorlage summary').click();
  const knopf = page.locator('.lern-vorlage button');
  assert.equal(await knopf.innerText(), 'Plan ersetzen (2 Orte)');
  assert.match(await page.locator('.lern-vorlage-vorschau').innerText(), /in Lehrplan-Reihenfolge[\s\S]*Wien[\s\S]*Oslo/);
  await knopf.click();
  await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
  assert.deepEqual(db.eintraege.map((x) => [x.block_id, x.ausgelassen]), [[201, []], [200, [2]]]);
  await page.locator('.lern-plan-rueck').click();
  await page.locator('.lern-plan-stand', { hasText: 'Rückgängig gemacht · Gespeichert' }).waitFor();
  await page.waitForFunction(() => document.querySelectorAll('.lern-plan-zeile').length === 1);
  assert.deepEqual(db.eintraege.map((x) => x.block_id), [202]);
});

// ---------- Schritt E: Befunde M1–M9 der Nachprüfung 0.74.5 und P1–P3 der Nachprüfung Phase 2 ----------
// Kind A (Gym 5): Plan Rom (Kl. 5) und New York (Kl. 7). anpassen(u) verändert die Übersicht.
const planKindA = (route, mehr = (u) => u) => (aktion, e) => {
  if (aktion !== 'schule_uebersicht') return null;
  const u = structuredClone(e); u.lernende[0].route = route.map((b, i) => ({ block_id: b, position: i + 1, art: 'normal', status: 'offen', kann_schon: false })); return mehr(u);
};
const kacheln = (page) => page.locator('.lr-zahlen .lr-zahl').evaluateAll((zs) => zs.map((z) => z.innerText.replace(/\s+/g, ' ').trim()));

test('M1/M4: „Gerade dran“ nur der aktuelle Ort; Klasse-7-Ort im Klasse-5-Plan unter „Später“, außer vorgezogen', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: planKindA([49, 52]) });
  await page.goto(origin + '/#/weg/1');
  await page.locator('.lr-zahlen').waitFor();
  assert.deepEqual(await kacheln(page), ['0 kann ich', '1 gerade dran', '1 kommen noch']); // Athen (Kl. 5, noch ohne Inhalt) kommt noch
  assert.deepEqual(await page.locator('.lr-dran b').first().allInnerTexts(), ['Natürliche Zahlen']);
  assert.equal(await page.locator('.lr-dran').count(), 1);
  const spaeter = page.locator('details.lr-mehr', { hasText: 'Später' });
  await spaeter.locator('summary').click();
  assert.match(await spaeter.innerText(), /Einfache Zinsen/, 'New York (Kl. 7) steht unter „Später“');
});

test('M1/M4/M9: vorgezogener Ort ist dran, der Rest unter „Kommt noch“; Satz „Alles aus Klasse 5 …“', async (t) => {
  const ohneAthen = (u) => { u.orte = u.orte.filter((o) => o.block_id !== 48); return u; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: planKindA([52, 49], ohneAthen) });
  await page.goto(origin + '/#/weg/1');
  await page.locator('.lr-zahlen').waitFor();
  assert.deepEqual(await kacheln(page), ['0 kann ich', '1 gerade dran', '1 kommen noch']);
  assert.match(await page.locator('.lr-dran').innerText(), /Einfache Zinsen/, 'New York ist vor Rom eingeplant → vorgezogen, also dran');
  assert.match(await page.locator('.lr-kommt').innerText(), /Natürliche[\s\S]*1 Flug/);
  await page.getByText('Alles aus Klasse 5 steht schon in deinem Plan.').waitFor();
  assert.equal(await page.getByText('Für deine Klasse ist alles verteilt.').count(), 0);
});

test('M5: Abflugtafel zeigt das nächste Zwischenziel (Etappen bis der Flug gelandet ist)', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1');
  const band = page.locator('.lr-band small');
  await band.waitFor();
  assert.match(await band.innerText(), /^Noch \d+ Etappen? bis ›Natürliche Zahlen‹ gelandet$/);
  assert.equal(await page.getByText(/bis zum Stempel/).count(), 0);
});

test('M7: „Worum geht’s“ ohne Bild, wenn Schritt 1 dasselbe Bild ergänzt; sonst bleibt das Bild oben', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const n = await page.evaluate(() => {
    const bild = { typ: 'tabelle', kopf: ['x', 'y'], zeilen: [['1', '2'], ['3', '?']] };
    const zaehle = (e) => { const d = lernErklaerung(e); return [d.querySelectorAll('.lr-tafel').length, d.querySelectorAll('.lr-sogehts .lr-tafel').length]; };
    return [zaehle({ einstieg: 'Worum.', bild, regel: 'R.', schritte: [{ text: 'Ergänzen.', bild: { zeilen: [['1', '2'], ['3', '6']] } }, { text: 'Fertig.' }] }),
      zaehle({ einstieg: 'Worum.', bild, regel: 'R.', schritte: [{ text: 'Lesen.' }, { text: 'Ergänzen.', bild: { zeilen: [['1', '2'], ['3', '6']] } }] })];
  });
  assert.deepEqual(n, [[1, 1], [2, 1]]);
});

test('M2/M3/M4: Flugplan – Klasse ohne Speichern-Knopf; Häkchen in der Zeile des Flugs; Ort über der Klasse markiert', async (t) => {
  const { page, calls } = await setup(t);
  await page.setViewportSize({ width: 820, height: 1180 });
  const orte = vieleOrte().slice(0, 3);
  orte.push({ block_id: 300, titel: 'Körper', stadt: 'Cusco', kontinent: 'Raum', themen: [{ thema_id: 900, titel: 'Netze', jahrgang: { gym_by: 8 }, stand: 'offen', einheit: { id: 990, status: 'geprueft', karten: 6, aufgaben: 40, neu: 0 } }] });
  const db = await planDb(page, calls, { orte, plan: [100, 300, 101] });
  await page.goto(origin + '/#/plan/1');
  const cusco = page.locator('.lern-plan-zeile', { hasText: 'Cusco' });
  await cusco.waitFor();
  assert.equal(await cusco.locator('.lern-plan-ueber').innerText(), 'Klasse 8 – über der Klasse des Kindes · vorgezogen'); // vor Wien (Kl. 5)
  // ans Ende → Kind sieht ihn unter „Später“
  await cusco.getByRole('button', { name: 'Cusco – Körper nach unten' }).click();
  await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
  assert.deepEqual(db.eintraege.map((x) => x.block_id), [100, 101, 300]);
  assert.equal(await page.locator('.lern-plan-zeile', { hasText: 'Cusco' }).locator('.lern-plan-ueber').innerText(), 'Klasse 8 – über der Klasse des Kindes · Kind sieht ihn unter „Später“');
  assert.equal(await page.locator('.lern-plan-zeile', { hasText: 'Rom' }).locator('.lern-plan-ueber').count(), 0);
  // M3: aufgeklappt steht das Häkchen in derselben Zeile wie der Flugname
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.locator('.lern-plan-ort').click();
  const flug = rom.locator('.lern-plan-themen li').first();
  const [h, n] = [await flug.locator('input[type=checkbox]').boundingBox(), await flug.locator('b').boundingBox()];
  assert.ok(Math.abs((h.y + h.height / 2) - (n.y + n.height / 2)) < 12 && h.x < n.x, 'Häkchen links neben dem Flugnamen');
  assert.ok((await flug.boundingBox()).height <= 60, 'eine Zeile je Flug');
  await page.screenshot({ path: path.join(root, 'test-results/m3-ort-aufgeklappt-820.png') });
  // M2: kein Knopf „Speichern“, Klasse speichert sofort
  assert.equal(await page.locator('.lp-kindform button').count(), 0);
  await page.getByRole('combobox', { name: 'Klasse des Kindes' }).selectOption('8');
  await page.locator('.lp-kindform [role=status]', { hasText: 'Gespeichert' }).waitFor();
  assert.equal(await page.locator('.lern-plan-ueber').count(), 0, 'mit Klasse 8 liegt nichts mehr darüber');
});

test('M8: Menüknopf schwebt nicht über dem Inhalt (Handy und Tablet, beim Rollen)', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  for (const [b, h] of [[390, 844], [820, 1180]]) {
    await page.setViewportSize({ width: b, height: h });
    for (const ziel of ['/#/reise/1', '/#/weg/1']) {
      await page.goto(origin + ziel); await page.locator('.lr-menue').first().waitFor();
      for (const y of [0, 300, 900]) {
        await page.evaluate((yy) => window.scrollTo(0, yy), y);
        const ueber = await page.evaluate(() => [...document.querySelectorAll('.lr-menue')].filter((m) => getComputedStyle(m).position === 'fixed').length);
        assert.equal(ueber, 0, `${b} px ${ziel} bei ${y}`);
        // An der Stelle jedes sichtbaren Menüknopfs liegt der Knopf selbst – nichts anderes darunter oder darüber
        const frei = await page.evaluate(() => [...document.querySelectorAll('.lr-menue')].map((m) => { const r = m.getBoundingClientRect();
          if (r.bottom < 0 || r.top > innerHeight) return true;
          const neben = [...document.querySelectorAll('.lr-inhalt a, .lr-inhalt button, .lr-inhalt p, .lr-inhalt h1')].filter((x) => !m.contains(x) && !x.contains(m) && x.checkVisibility());
          const z = neben.find((x) => { const q = x.getBoundingClientRect(); return !(q.right <= r.left || q.left >= r.right || q.bottom <= r.top || q.top >= r.bottom); }); return z ? z.className + ' ' + z.textContent.slice(0, 40) : true; }).find((x) => x !== true) ?? true);
        if (frei !== true) await page.screenshot({ path: path.join(root, 'test-results/m8-fehler.png') });
        assert.ok(frei === true, `Menüknopf überdeckt nichts: ${b} px ${ziel} bei ${y}: ${frei}`);
      }
    }
  }
});

test('Flugplan ziehen: Rechner mit Maus und Handy mit Finger (mit Rollen)', async (t) => {
  const { page, calls } = await setup(t);
  await page.setViewportSize({ width: 1280, height: 800 });
  const db = await planDb(page, calls, { orte: vieleOrte(), plan: STAEDTE.slice(0, 12).map((_, i) => 100 + i) });
  await page.goto(origin + '/#/plan/1');
  const zeilen = page.locator('.lern-plan-zeile'); await zeilen.nth(11).waitFor();
  // Maus: Platz 6 (Oslo) → Platz 2
  const g = await zeilen.nth(5).locator('.lern-plan-griff').boundingBox(); const z = await zeilen.nth(1).boundingBox();
  await page.mouse.move(g.x + g.width / 2, g.y + g.height / 2); await page.mouse.down();
  await page.mouse.move(g.x + g.width / 2, z.y + 6, { steps: 10 }); await page.mouse.up();
  await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
  assert.deepEqual(db.eintraege.slice(0, 3).map((x) => x.block_id), [100, 105, 101]);
  // Handy, Finger: letzte Zeile (Accra) bis ganz nach oben – die Seite rollt beim Ziehen am oberen Rand mit
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(origin + '/#/plan/1');
  await zeilen.nth(11).waitFor();
  await zeilen.nth(11).scrollIntoViewIfNeeded();
  await page.evaluate(() => window.scrollBy(0, 200));
  const griff = await zeilen.nth(11).locator('.lern-plan-griff').boundingBox();
  assert.equal(await zeilen.nth(11).locator('.lern-plan-griff').evaluate((x) => getComputedStyle(x).touchAction), 'none');
  await page.evaluate(async ({ x, y }) => {
    const opt = (yy) => ({ bubbles: true, pointerId: 9, pointerType: 'touch', isPrimary: true, clientX: x, clientY: yy, button: 0 });
    document.elementFromPoint(x, y).dispatchEvent(new PointerEvent('pointerdown', opt(y)));
    for (let i = 1; i <= 10; i++) window.dispatchEvent(new PointerEvent('pointermove', opt(y + (20 - y) * i / 10)));
    for (let i = 0; i < 300 && window.scrollY > 0; i++) await new Promise((r) => setTimeout(r, 16)); // rollt am Rand nach oben
    const erste = document.querySelector('ol.lern-plan').getBoundingClientRect(); // Zeilen sind beim Ziehen verschoben – die Liste selbst nicht
    window.dispatchEvent(new PointerEvent('pointermove', opt(erste.top + 4)));
    window.dispatchEvent(new PointerEvent('pointerup', opt(erste.top + 4)));
  }, { x: griff.x + griff.width / 2, y: griff.y + griff.height / 2 });
  await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
  assert.equal(db.eintraege[0].block_id, 111, 'Accra steht jetzt vorn');
});

test('P2: Mein Weg · Karte wählt die Orte nach derselben Regel wie „Stand“ (Schulart des Kindes)', async (t) => {
  // RS-Kind Klasse 6: Athen (Teilbarkeit rs_by 6) gehört dazu, Rom (rs_by 5) nicht – obwohl block.ziel_klasse 5 ist
  const rs = (aktion, e) => { const u = standAnpassen()(aktion, e); if (!u || aktion !== 'schule_uebersicht') return u; Object.assign(u.lernende[0], { schulart: 'rs_by', klasse: 6, stufen: {} }); return u; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: rs });
  await page.goto(origin + '/#/weg/1-karte');
  await page.locator('.lr-ortliste li').first().waitFor();
  const orte = await page.locator('.lr-ortliste').innerText();
  assert.match(orte, /Athen/); assert.doesNotMatch(orte, /Rom/);
});

// ---------- Bau-Auftrag F Teil 2: Stufenzeichen, Abwechslung der Typen, Knobel-Bordkarten ----------
const mitBonus = (aktion, e) => {
  if (aktion === 'schule_einheit_lesen') { const x = structuredClone(e); x.uebungen = x.uebungen.map((a) => ({ ...a, stufe: a.stufe || { 11: 1, 12: 1, 13: 2 }[a.id], typ: { 11: 'direkt', 12: 'erkennen', 13: 'mehrschritt', 15: 'rueckwaerts', 16: 'fehler' }[a.id] }));
    x.bonus = [{ ...zeig(AUFG[501]), versuche: 0, geloest: false }]; return x; }
  if (aktion === 'schule_konto') { const x = structuredClone(e); x.konto.knobel_sterne = 2; return x; }
  if (aktion === 'schule_lernstand') { const x = structuredClone(e); Object.assign(x.einheiten[0].karten[0], { knobel_gesamt: 2, knobel_geloest: 1 }); return x; }
  if (aktion === 'schule_inhalt_lesen' && e.aufgaben?.length) { const x = structuredClone(e); x.aufgaben[0].typ = 'direkt';
    x.aufgaben.push({ id: 501, lernziel: x.aufgaben[0].lernziel, pool: 'bonus', stufe: 3, typ: 'knobel', antworttyp: 'zahl', frage: { text: 'Knobel?' }, loesung: { wert: 100 }, loesungsweg: 'Weg.', freigegeben: true }); return x; }
  return null;
};

test('F: Stufenzeichen im Kopf der Bordkarte (● / ●● / ●●●, mit Text für Vorleser, ohne Rot)', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mitBonus });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-3'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  const z = page.locator('.lr-bord-kopf .lr-stufe');
  assert.match(await z.getAttribute('aria-label'), /^Stufe: (leicht|mittel|schwer)$/);
  assert.match(await z.innerText(), /^●{1,3}$/);
  const farbe = await z.evaluate((x) => getComputedStyle(x).color);
  const [r, g, b] = farbe.match(/\d+/g).map(Number); assert.ok(!(r > 150 && g < 100 && b < 100), 'kein Rot: ' + farbe);
  assert.equal(await page.getByText(/^(LEICHT|MITTEL|SCHWER)$/).count(), 0);
  // ohne Stufe kein Zeichen-Text, Knobel mit Stern
  assert.deepEqual(await page.evaluate(() => [lernStufeZeichen({ stufe: 2 }).textContent, lernStufeZeichen({}).textContent, lernStufeZeichen({ stufe: 3, bonus: true }).textContent]), ['●●', '', '★ KNOBEL']);
});

test('F: Auswahl der nächsten Bordkarte – nie zweimal derselbe Typ hintereinander, neue Typen zuerst; schwere Bordkarte nur mit Stufe-3-Typ', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const r = await page.evaluate(() => {
    const k = (id, stufe, typ, text) => ({ id, stufe, typ, frage: { text: text || `Aufgabe ${id}: rechne 3 + ${id}.` } });
    // 1) Zielstufe 1, letzte war „direkt“: zwei weitere „direkt“ vorn, „erkennen“ dahinter → „erkennen“
    const e1 = { ziel: 6, serie: 0 }; const w1 = [k(2, 1, 'direkt'), k(3, 1, 'direkt'), k(4, 1, 'erkennen')];
    lernWaehleBordkarte(w1, e1, k(1, 1, 'direkt'), new Set(['direkt']));
    // 2) neue Typen zuerst: „mehrschritt“ schon gesehen, „umkehr“ noch nicht
    const e2 = { ziel: 6, serie: 3 }; const w2 = [k(5, 2, 'mehrschritt'), k(6, 2, 'umkehr')];
    lernWaehleBordkarte(w2, e2, k(9, 2, 'einkleidung'), new Set(['mehrschritt', 'einkleidung']));
    // 3) ohne Typ: nie derselbe Fragetext nach Ersetzen der Zahlen
    const e3 = { ziel: 6, serie: 0 }; const w3 = [k(7, 1, null, 'Rechne 12 + 5.'), k(8, 1, null, 'Rechne 30 + 9.'), k(10, 1, null, 'Wie viel ist das Doppelte von 7?')];
    lernWaehleBordkarte(w3, e3, k(11, 1, null, 'Rechne 4 + 4.'), new Set());
    // 4) Punkte voll, schwere Bordkarte fehlt: eine Stufe-3-Aufgabe mit Stufe-1-Typ zählt nicht
    const e4 = { ziel: 6, serie: 6, schwerNoetig: true, schwerOk: false }; const w4 = [k(12, 3, 'direkt'), k(13, 3, 'begruenden')];
    lernWaehleBordkarte(w4, e4, null, new Set());
    return [w1[0].id, w2[0].id, w3[0].id, w4[0].id, lernIstSchwer(k(1, 3, 'knobel')), lernIstSchwer(k(1, 3, null))];
  });
  assert.deepEqual(r, [4, 6, 10, 13, false, true]);
  // in der App: nach einer „direkt“-Bordkarte kommt nicht wieder „direkt“, solange es eine andere gibt
});

test('F: Knobel-Bordkarte nach der Landung – freiwillig, ein Versuch, 30 Sterne; zählt nicht für „sitzt“', async (t) => {
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: mitBonus });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  for (let i = 0; i < 2; i++) {
    for (const z of ['2', '0', '0', '0']) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
    await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
    if (i === 0) { await page.getByText(/An Bord/).waitFor(); await page.getByRole('button', { name: 'Neue Bordkarte ›' }).click(); }
  }
  await page.getByText('GELANDET').waitFor();
  const vorher = calls.filter((c) => c.aktion === 'schule_uebung_pruefen').length;
  await page.getByRole('button', { name: '★ Knobel-Bordkarte (freiwillig)' }).click();
  await page.locator('.lr-knobel .lr-stufe-bonus').waitFor();
  assert.match(await page.locator('.lr-knobel').innerText(), /zählt nicht für „sitzt“/);
  await page.locator('.lr-knobel input').fill('100');
  await page.locator('.lr-knobel').getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('+30 Sterne · ein Knobel-Stern').waitFor();
  assert.equal(await page.locator('.lr-knobel').getByRole('button', { name: 'Prüfen' }).count(), 0, 'kein zweiter Versuch');
  const c = calls.filter((x) => x.aktion === 'schule_uebung_pruefen').slice(vorher);
  assert.equal(c.length, 1); assert.equal(c[0].daten.aufgabe_id, 501); assert.equal(c[0].daten.anlauf, undefined); assert.equal(c[0].daten.hilfe, undefined);
  await page.screenshot({ path: path.join(root, 'test-results/f-knobel-390.png'), fullPage: true });
});

test('F: Knobel falsch kostet nichts und zeigt den Weg; ohne Bonus-Aufgaben kein Angebot', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mitBonus });
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  await page.evaluate(() => { const box = document.createElement('div'); box.id = 'kb'; document.querySelector('.lr-inhalt').append(box);
    lernKnobel(box, { id: 501, stufe: 3, bonus: true, antworttyp: 'zahl', frage: { text: 'Knobel?' }, tipp: 'Denk nach.' }, { kind: 1 }); });
  await page.locator('#kb input').fill('96');
  await page.locator('#kb').getByRole('button', { name: 'Prüfen' }).click();
  await page.locator('#kb .lr-knobel-falsch').waitFor();
  const r = [await page.locator('#kb .lr-knobel-falsch').innerText(), ...await page.evaluate(() => [lernKnobelAngebot({ bonus: [] }, () => {}), lernKnobelAngebot({}, () => {})])];
  assert.match(r[0], /kostet nichts[\s\S]*|So geht’s/);
  assert.match(r[0], /Richtig ist: 100/);
  assert.deepEqual(r.slice(1), [null, null]);
});

test('F: Knobeln des Tages auf der Abflugtafel (einmal je Tag), Knobel-Sterne im Reisepass, Eltern sehen Stufe, Typ und Knobel x von y', async (t) => {
  const tag = (aktion, e) => { const x = mitBonus(aktion, e); if (aktion !== 'schule_konto') return x;
    x.knobel_tag = { ...zeig(AUFG[501]), einheit_id: 1, stadt: 'Rom', etappe: 'Welchen Wert hat eine Ziffer?' }; return x; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: tag });
  await page.goto(origin + '/#/reise/1');
  const box = page.locator('.lr-knobel-tag'); await box.waitFor();
  assert.match(await box.innerText(), /KNOBELN DES TAGES[\s\S]*Welchen Wert hat eine Ziffer\?/);
  await box.getByRole('button', { name: 'Knobeln (freiwillig)' }).click();
  await box.locator('.lr-knobel input').waitFor();
  await page.reload(); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  assert.equal(await page.locator('.lr-knobel-tag').count(), 0, 'heute nur einmal');
  await page.goto(origin + '/#/reisepass/1'); await page.getByText('★ Knobel-Sterne: 2').waitFor();
  // Eltern: Lernstand und Inhalte
  await page.goto(origin + '/#/wackelt/1'); await page.locator('.ls-knobel').first().waitFor();
  assert.equal(await page.locator('.ls-knobel').first().innerText(), 'Knobel: 1 von 2');
  await page.goto(origin + '/#/inhalte/1'); await page.locator('details.lp-karte summary').first().click();
  const zeilen = page.locator('details.lp-karte').first().locator('.lp-tabelle tbody tr');
  assert.match(await zeilen.first().locator('td').first().innerText(), /leicht\s*wie im Beispiel/);
  assert.match(await zeilen.last().locator('td').first().innerText(), /★ Knobel\s*freiwillig/);
});

// ---------- Zusatz 1 zu Bau-Auftrag F: „Lernstand“ öffnet die Klassen-Übersicht des Kindes ----------
test('Zusatz 1 zu F: Knopf „Lernstand“ zeigt mit einem Klick die Tabelle des Kindes; „Was wackelt?“ eigener Knopf', async (t) => {
  const { page } = await setup(t, { anpassen: standAnpassen() });
  await page.goto(origin + '/#/lernen');
  const karte = page.locator('.lern-kindbereich', { hasText: 'Kind A' });
  await karte.getByRole('link', { name: 'Lernstand Kind A', exact: true }).click();
  await page.waitForURL(/#\/lernstand\/1$/);
  await page.locator('.lern-stand-raster').waitFor();
  await page.locator('main h2', { hasText: 'Lernstand Kind A' }).waitFor();
  assert.equal(await page.locator('#title').innerText(), 'Lernstand Kind A');
  assert.equal(await page.locator('.lern-chips-zeile[aria-label="Schulart"] a[aria-current]').innerText(), 'Gymnasium', 'in der Schulart des Kindes');
  assert.equal(await page.locator('.lern-chips-zeile[aria-label="Einstieg prüfen"]').count(), 1);
  // Schulart wechseln bleibt auf der Lernstand-Seite
  await page.locator('.lern-chips-zeile[aria-label="Schulart"] a', { hasText: 'Realschule' }).click();
  await page.waitForURL(/#\/lernstand\/1-rs_by$/);
  // Verweis auf „Was wackelt?“
  await page.getByRole('link', { name: /Was wackelt\? – Etappen/ }).click();
  await page.waitForURL(/#\/wackelt\/1$/);
  await page.getByRole('heading', { name: 'Was wackelt?', exact: true }).waitFor();
  // Vergleich aller Kinder
  await page.goto(origin + '/#/lernen');
  assert.equal(await karte.getByRole('link', { name: 'Was wackelt? Kind A', exact: true }).getAttribute('href'), '#/wackelt/1');
  await page.getByRole('link', { name: /Alle Kinder im Vergleich/ }).click();
  await page.locator('main h2', { hasText: 'Alle Kinder im Vergleich' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/f-lernstand-390.png'), fullPage: true });
});

// ---------- Bau-Auftrag G (W176) Teil 1: „gelandet“ ohne Minuspunkte ----------
const neueRegel = (felder) => (aktion, e) => {
  if (aktion !== 'schule_einheit_lesen') return null;
  const x = structuredClone(e);
  for (const lz of Object.keys(x.etappen_stand)) Object.assign(x.etappen_stand[lz], { eigene_loesungen: 0, folge: 0, folge_ziel: 2, typen_anzahl: 0, typen_noetig: 1, fehler_folge: 0, stufe_senkung: 0, sicher: false }, felder?.[lz] || {});
  return x;
};

test('W176 T1: Checkliste statt Punkten, „heute selbst gelöst“, nach Fehler „Die nächste zählt wieder voll.“', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: neueRegel({ stellenwert: { eigene_loesungen: 1, folge: 1 } }) });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  const liste = page.locator('.lr-checkliste');
  await liste.waitFor();
  assert.deepEqual((await liste.locator('li').allInnerTexts()).map((x) => x.trim()), ['○ Eigene Lösungen 1/2', '○ 2 in Folge: 1/2']);
  assert.match(await page.locator('.lr-heute').innerText(), /heute 0 Aufgaben selbst gelöst/);
  // falsch: Zahl tippen, die nicht stimmt – zweiter Versuch, dann Lösung; kein Abzug-Text
  for (const runde of [0, 1]) {
    for (const z of ['5']) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
    await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
    if (runde === 0) { await page.getByText(/Noch ein Versuch|Versuch/).first().waitFor(); const loesch = page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: /Löschen|⌫/ }); if (await loesch.count()) await loesch.first().click(); }
  }
  await page.getByText('Die nächste zählt wieder voll.').waitFor();
  assert.equal(await page.getByText(/kostet 2 Punkte|−2|Punkte verlier/).count(), 0);
});

test('W176 T1: Stufe fällt erst nach 2 Fehlern in Folge (stufe_senkung), keine Minuspunkt-Texte in der App', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const r = await page.evaluate(() => {
    const k = (id, stufe, typ) => ({ id, stufe, typ, frage: { text: `Aufgabe ${id}` } });
    const w = () => [k(1, 1, 'direkt'), k(2, 2, 'mehrschritt'), k(3, 3, 'begruenden')];
    const wahl = (e) => { const x = w(); lernWaehleBordkarte(x, e, null, new Set()); return x[0].stufe; };
    const basis = { ziel: 6, neueRegel: true, eigene: 4 }; // 4 von 6 → Stufe 3
    return [wahl({ ...basis, stufeSenkung: 0 }), wahl({ ...basis, stufeSenkung: 1 }), wahl({ ...basis, stufeSenkung: 2 }), wahl({ ziel: 6, serie: 4 })];
  });
  assert.deepEqual(r, [3, 2, 1, 3]);
  const quelle = fs.readFileSync(path.join(root, 'lernen.js'), 'utf8');
  assert.doesNotMatch(quelle, /kostet 2 Punkte|−2 Punkte|Punkte verlier/);
  await page.goto(origin + '/#/info'); await page.getByText('Wie wird gelernt?').click();
  assert.doesNotMatch(await page.locator('#main').innerText(), /−2|Minuspunkt(?!e:)/);
});

test('W176 T1: gelandet und sicher – Kind sieht „Gelandet“/„Sicher“, Eltern sehen eigene Lösungen und „sicher“', async (t) => {
  const ls = (aktion, e) => { const x = neueRegel({ stellenwert: { eigene_loesungen: 6, folge: 3, sitzt: true, sicher: true }, strahl: { eigene_loesungen: 3, folge: 1 } })(aktion, e);
    if (x) return x;
    if (aktion !== 'schule_lernstand') return null; const y = structuredClone(e);
    Object.assign(y.einheiten[0].karten[0], { eigene_loesungen: 6, folge: 3, typen_anzahl: 2, sicher: true });
    Object.assign(y.einheiten[0].karten[1], { eigene_loesungen: 2, folge: 0, typen_anzahl: 1, sicher: false }); return y; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: ls });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/Sicher! Du kannst trotzdem weiterüben./).waitFor();
  await page.goto(origin + '/#/wackelt/1');
  await page.locator('.ls-karte', { hasText: 'Welchen Wert hat eine Ziffer?' }).getByText('sicher', { exact: true }).waitFor();
  await page.locator('.ls-karte', { hasText: 'Runden' }).getByText('2 eigene Lösungen · 0 in Folge · 1 Art von Bordkarten').waitFor();
});

// ---------- Bau-Auftrag G (W176) Teil 3: Mischkarten ----------
test('W176 T3: Auswahl der Mischkarte – erst ab 3 gelandeten Etappen, jede n-te, gleicher Flug zuerst, jede 3. aus einem älteren Flug', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const r = await page.evaluate(() => {
    const k = () => [{ id: 1, quelle: 'aelter' }, { id: 2, quelle: 'kontinent' }, { id: 3, quelle: 'flug' }, { id: 4, quelle: 'flug' }, { id: 5, quelle: 'aelter' }];
    const z = { n: 0 }, rest = k();
    const folge = [4, 8, 12].map((nr) => lernMischWahl(rest, { nr, jede: 4, ab: 3, gelandet: 3, zaehler: z })?.id);
    return [lernMischWahl(k(), { nr: 4, jede: 4, ab: 3, gelandet: 2 }), lernMischWahl(k(), { nr: 5, jede: 4, ab: 3, gelandet: 3 }), lernMischWahl(k(), { nr: 6, jede: 6, ab: 3, gelandet: 5 })?.misch,
      lernMischWahl(k(), { nr: 4, jede: 4, gelandet: 3, aus: true }), lernMischWahl([], { nr: 4, jede: 4, gelandet: 3 }), folge];
  });
  assert.deepEqual(r, [null, null, true, null, null, [3, 4, 1]]);
});

test('W176 T3: Mischkarte beim Üben – neutral gekennzeichnet, ohne Erklärung, nach der Lösung die Etappe; zählt nicht für die aktuelle Etappe', async (t) => {
  const misch = (aktion, e) => {
    if (aktion !== 'schule_einheit_lesen') return null; const x = neueRegel({ strahl: { sitzt: true } })(aktion, e);
    x.mischkarten = [{ ...zeig(AUFG[14]), stufe: 2, einheit_id: 2, quelle: 'aelter', stadt: 'New York', etappe: 'Große Zahlen lesen' },
      { id: 501, bonus: true, lernziel: 'x', einheit_id: 2, quelle: 'flug', frage: { text: 'Knobel' } }];
    x.misch_jede = 1; x.misch_ab = 1; return x; };
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: misch });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1');
  await page.getByText('BORDKARTE 1 · AUS DEINER REISE').waitFor();
  await page.getByText('Aus deiner Reise – erkennst du, was gefragt ist?').waitFor();
  assert.equal(await page.getByRole('button', { name: 'Erklärung ansehen' }).count(), 0);
  assert.doesNotMatch(await page.locator('.lr-bordkarte').innerText(), /Große Zahlen lesen|New York/, 'Etappe erst nach der Lösung');
  const vorher = await page.locator('.lr-checkliste').innerText();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Das war: Große Zahlen lesen – New York').waitFor();
  const c = calls.filter((x) => x.aktion === 'schule_uebung_pruefen').at(-1);
  assert.equal(c.daten.misch, true); assert.equal(c.daten.aufgabe_id, 14);
  assert.equal(await page.locator('.lr-checkliste').innerText(), vorher, 'aktuelle Etappe unverändert');
  // Knobel-Bordkarten kommen nie als Mischkarte: die nächste Bordkarte ist eine normale aus Rom
  await page.getByRole('button', { name: /Neue Bordkarte/ }).click();
  await page.getByText(/BORDKARTE 2 · ROM/).waitFor();
});

// ---------- Wunsch 18.11.: „Lernen starten“ an der Kinderkarte ----------
test('Kinderkarte: „Lernen starten“ ist der erste, hervorgehobene Knopf, auf dem Handy allein in der ersten Zeile, und öffnet die Abflugtafel', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  for (const [b, h] of [[390, 844], [820, 1180], [1280, 800]]) {
    await page.setViewportSize({ width: b, height: h });
    await page.goto(origin + '/#/lernen');
    const karte = page.locator('.lern-kindbereich', { hasText: 'Kind A' });
    const knoepfe = karte.locator('.lern-kindbereich-knoepfe a');
    await knoepfe.first().waitFor();
    assert.equal(await knoepfe.first().innerText(), 'Lernen starten ›');
    assert.equal(await knoepfe.first().getAttribute('href'), '#/reise/1');
    const [farbe, andere] = await knoepfe.evaluateAll((as) => [getComputedStyle(as[0]).backgroundColor, getComputedStyle(as[1]).backgroundColor]);
    assert.notEqual(farbe, andere, 'hervorgehoben');
    const boxen = await knoepfe.evaluateAll((as) => as.map((a) => a.getBoundingClientRect()).map((r) => ({ top: Math.round(r.top), left: Math.round(r.left), w: Math.round(r.width) })));
    assert.ok(boxen.slice(1).every((x) => x.top >= boxen[0].top), `${b} px: „Lernen starten“ steht in der ersten Zeile`);
    if (b === 390) assert.ok(boxen.slice(1).every((x) => x.top > boxen[0].top), '390 px: allein in der ersten Zeile');
  }
  await page.locator('.lern-kindbereich', { hasText: 'Kind A' }).getByRole('link', { name: 'Lernen starten: Kind A' }).click();
  await page.waitForURL(/#\/reise\/1$/);
  await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  await page.goto(origin + '/#/info');
  await page.getByText('Auf der Startseite hat jede Kinderkarte oben den Knopf „Lernen starten“', { exact: false }).waitFor();
});

// ---------- Bau-Auftrag G (W176) Teil 4: Expeditionen ----------
const expKonto = (erledigt = []) => (aktion, e) => {
  if (aktion === 'schule_konto') { const x = structuredClone(e); x.konto.expeditions_stempel = 1;
    x.expeditionen = [{ id: 7, schluessel: '8-handytarif', titel: 'Handytarif', klasse: { gym_by: 8 }, einleitung: 'Du brauchst einen neuen Handytarif. Tarif A kostet 5 € Grundgebühr und 0,10 € je Minute.',
      zustand: erledigt.length ? 'begonnen' : 'angeboten', teile_gesamt: 3, teile_erledigt: erledigt.length,
      teile: [601, 602, 603].map((id) => ({ ...zeig(AUFG[id]), k: AUFG[id].k, erledigt: erledigt.includes(id), richtig_erst: false, ...(erledigt.includes(id) ? { loesung: AUFG[id].loesung, loesungsweg: 'So wird gerechnet.' } : {}) })) }];
    return x; }
  if (aktion === 'schule_uebersicht') { const x = structuredClone(e); x.lernende[0].expeditionen = [{ id: 7, zustand: 'begonnen' }]; x.lernende[1].expeditionen = [];
    x.expeditionen = [{ id: 7, schluessel: '8-handytarif', titel: 'Handytarif', klasse: { gym_by: 8 }, status: 'entwurf', einleitung: 'Du brauchst einen neuen Handytarif.',
      voraussetzungen: [{ thema_schluessel: 'funktionen.linear', lernziel: 'aufstellen' }], teile: [601, 602, 603].map((id) => ({ ...AUFG[id], lernziel: AUFG[id].lernziel, loesungsweg: 'So wird gerechnet.' })) }];
    return x; }
  if (aktion === 'schule_inhalt_lesen' && e.aufgaben?.length) { const x = structuredClone(e); x.aufgaben.push({ id: 601, lernziel: x.aufgaben[0].lernziel, pool: 'expedition', antworttyp: 'zahl', frage: { text: 'EXPEDITIONSTEIL' }, loesung: { wert: 8 } }); return x; }
  return null;
};

test('W176 T4: Expedition – Angebot auf der Abflugtafel, Teil falsch → 2. Versuch → Lösung → nächster Teil, am Ende geschafft mit Sternen', async (t) => {
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: expKonto() });
  await page.goto(origin + '/#/reise/1');
  const box = page.locator('.lr-expedition-angebot'); await box.waitFor();
  assert.match(await box.innerText(), /EXPEDITION[\s\S]*Handytarif – 3 Teile[\s\S]*Freiwillig/);
  await box.getByRole('link', { name: 'Expedition starten ›' }).click();
  await page.waitForURL(/#\/expedition\/1-7$/);
  await page.getByText('TEIL A VON 3').waitFor();
  await page.getByText('Zählt nicht für „gelandet“', { exact: false }).waitFor();
  const eingabe = page.locator('.lr-exp-teil input');
  await eingabe.fill('9'); await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Du hast einen zweiten Versuch.', { exact: false }).waitFor();
  await eingabe.fill('7'); await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig ist: 8').waitFor();
  await page.getByText('Keine Abzüge – im nächsten Teil geht es mit den richtigen Zahlen weiter.').waitFor();
  const ca = calls.filter((c) => c.aktion === 'schule_uebung_pruefen' && c.daten.aufgabe_id === 601).map((c) => c.daten.anlauf);
  assert.deepEqual(ca, [1, 2]);
  await page.getByRole('button', { name: 'Weiter mit Teil B ›' }).click();
  await page.getByText('TEIL B VON 3').waitFor();
  assert.match(await page.locator('.lr-exp-teil.erledigt').innerText(), /TEIL A[\s\S]*Lösung: 8/);
  await page.locator('.lr-exp-teil input').fill('11'); await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.getByRole('button', { name: 'Weiter mit Teil C ›' }).click();
  await page.locator('.lr-exp-teil input').fill('71'); await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByRole('button', { name: 'Zum Abschluss ›' }).click();
  await page.getByText('EXPEDITION GESCHAFFT').waitFor();
  await page.getByText('+50 Sterne').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/w176-expedition-390.png'), fullPage: true });
  await page.goto(origin + '/#/reisepass/1'); await page.getByText('⛰ Expeditions-Stempel: 1').waitFor();
});

test('W176 T4: Abbruch verliert nichts – erledigte Teile stehen da, es geht beim offenen Teil weiter; ohne Angebot keine Karte', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: expKonto([601]) });
  await page.goto(origin + '/#/reise/1');
  await page.getByRole('link', { name: 'Expedition fortsetzen ›' }).click();
  await page.getByText('TEIL B VON 3').waitFor();
  assert.equal(await page.locator('.lr-exp-teil.erledigt').count(), 1);
  // ohne Expeditionen (Server bietet keine an, z. B. Voraussetzungen fehlen): keine Karte
  const { page: p2 } = await setup(t, { gestaltung: 'nacht' });
  await p2.goto(origin + '/#/reise/1'); await p2.getByRole('heading', { name: /Abflüge/ }).waitFor();
  assert.equal(await p2.locator('.lr-expedition-angebot').count(), 0);
  await p2.goto(origin + '/#/expedition/1-7'); await p2.getByText('Diese Expedition ist gerade nicht offen.').waitFor();
});

test('W176 T4: Eltern – Expeditionen lesbar mit Lösung, im Lernstand je Kind der Zustand, nicht bei der Etappe des Bezugs', async (t) => {
  const { page } = await setup(t, { anpassen: expKonto() });
  await page.goto(origin + '/#/lernstand/1');
  const sec = page.locator('.lern-exp-stand'); await sec.waitFor();
  assert.match(await sec.innerText(), /Handytarif\s*begonnen/);
  await sec.getByRole('link', { name: 'Alle Expeditionen ansehen ›' }).click();
  await page.waitForURL(/#\/expeditionen$/);
  await page.locator('details.lern-exp summary').click();
  assert.match(await page.locator('details.lern-exp').innerText(), /Entwurf \(nur Testkind\)[\s\S]*Voraussetzungen: funktionen.linear \/ aufstellen[\s\S]*Lösung: 8/);
  await page.goto(origin + '/#/inhalte/1'); await page.locator('details.lp-karte').first().waitFor();
  assert.equal(await page.getByText('EXPEDITIONSTEIL').count(), 0);
  await page.goto(origin + '/#/lehrplan'); await page.getByRole('link', { name: '⛰ Expeditionen ansehen ›' }).waitFor();
});

// ---------- IB einheitlich beschriften (18.11.): MYP-Jahr = Klasse − 5, Hinweis „entspricht etwa Klasse 6–10“ ----------
test('IB: MYP-Jahr = Klasse − 5 überall gleich; Beschriftung „MYP-Jahr n“ mit Hinweis auf Klasse 6–10', async (t) => {
  const { page } = await setup(t, { anpassen: standAnpassen() });
  await page.goto(origin + '/#/lernen'); await page.locator('.lern-kindbereich').first().waitFor();
  const r = await page.evaluate(() => [lernStufe({ klasse: 5, schulart: 'gym_by' }, 'ib_myp'), lernStufe({ klasse: 8, schulart: 'gym_by' }, 'ib_myp'), lernStufe({ klasse: 10, schulart: 'rs_by' }, 'ib_myp'),
    lernStufe({ klasse: 8, schulart: 'gym_by', stufen: { ib_myp: 2 } }, 'ib_myp'), LERN_SYS[2].kl(1), LERN_SYS[2].kl(5), LERN_SYS[2].label(3), LERN_SYS[2].label(0)]);
  assert.deepEqual(r, [0, 3, 5, 2, 6, 10, 'MYP-Jahr 3', 'vor MYP-Jahr 1']);
  await page.goto(origin + '/#/lernstand/2-ib_myp'); await page.locator('.lern-stand-raster').waitFor();
  assert.deepEqual(await page.locator('.lern-stand-raster thead th').allInnerTexts().then((x) => x.slice(1)), ['MYP-Jahr 1', 'MYP-Jahr 2', 'MYP-Jahr 3', 'MYP-Jahr 4', 'MYP-Jahr 5']);
  await page.getByText('MYP-Jahr 1–5 entspricht etwa Klasse 6–10', { exact: false }).first().waitFor();
  await page.goto(origin + '/#/info'); await page.getByText('Worauf baut die App auf?').click();
  assert.match(await page.locator('#main').innerText(), /MYP-Jahr 1–5; entspricht etwa Klasse 6–10/);
  const quelle = fs.readFileSync(path.join(root, 'lernen.js'), 'utf8');
  assert.doesNotMatch(quelle, /klasse - 4|Klasse − 4|'MYP ' \+/);
});

// ---------- Betrieb 18.11.: Bordkarte wurde während der Sitzung gesperrt („nicht freigegeben“) ----------
const sperre = async (page, ids, calls) => page.route('**/functions/v1/lernen-api/**', async (route) => {
  const b = JSON.parse(route.request().postData() || '{}');
  if (b.aktion === 'schule_uebung_pruefen' && ids.includes(b.daten.aufgabe_id) && !route.request().postData().includes('"x-erlaubt"')) {
    calls.push({ aktion: 'gesperrt', daten: b.daten });
    return route.fulfill({ contentType: 'application/json', status: 400, body: JSON.stringify({ ok: false, fehler: 'Diese Aufgabe ist noch nicht freigegeben' }) });
  }
  return route.fallback();
});

test('Gesperrt nach dem Laden: Üben – keine rote Meldung, Flug lädt still neu, Checkliste unverändert', async (t) => {
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: neueRegel({ stellenwert: { eigene_loesungen: 1, folge: 1 } }) });
  await sperre(page, [11], calls);
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  const vorher = await page.locator('.lr-checkliste').innerText();
  const laden = () => calls.filter((c) => c.aktion === 'schule_einheit_lesen').length;
  const l0 = laden();
  for (const z of ['2', '0', '0', '0']) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
  await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
  await page.waitForFunction((n) => true, l0);
  await page.waitForTimeout(400);
  assert.ok(calls.some((c) => c.aktion === 'gesperrt'));
  assert.ok(laden() > l0, 'Flug neu geladen');
  await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  assert.equal(await page.locator('.err-text').count(), 0, 'keine Fehlermeldung');
  assert.equal(await page.getByText(/nicht freigegeben/).count(), 0);
  assert.equal(await page.locator('.lr-checkliste').innerText(), vorher);
});

test('Gesperrt nach dem Laden: Knobel und Wiederholung – keine Fehlermeldung, es geht weiter', async (t) => {
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: mitBonus });
  await sperre(page, [501, 11, 12], calls);
  // Knobel: die Knobel-Karte schließt sich still
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  await page.evaluate(() => { const box = document.createElement('div'); box.id = 'kb'; document.querySelector('.lr-inhalt').append(box);
    lernKnobel(box, { id: 501, stufe: 3, bonus: true, antworttyp: 'zahl', frage: { text: 'Knobel?' } }, { kind: 1 }, { zurueck: () => box.remove() }); });
  await page.locator('#kb input').fill('96'); await page.locator('#kb').getByRole('button', { name: 'Prüfen' }).click();
  await page.locator('#kb').waitFor({ state: 'detached' });
  assert.equal(await page.locator('.err-text').count(), 0);
  // Wiederholung: lädt neu, keine Meldung
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion !== 'schule_wiederholung') return route.fallback();
    calls.push({ aktion: 'schule_wiederholung' });
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, faellig: 1, aufgaben: [{ ...AUFG[11], einheit_id: 1, stadt: 'Rom' }] } }) });
  });
  await page.goto(origin + '/#/wiederholen/1');
  await page.getByText('Welchen Wert hat die Ziffer 2', { exact: false }).waitFor();
  const wdh0 = calls.filter((c) => c.aktion === 'schule_wiederholung').length;
  const tf = page.getByRole('group', { name: 'Tastenfeld' });
  if (await tf.count()) { for (const z of ['2', '0', '0', '0']) await tf.getByRole('button', { name: z, exact: true }).click(); await tf.getByRole('button', { name: 'Prüfen' }).click(); }
  else { await page.locator('main input').first().fill('2000'); await page.getByRole('button', { name: 'Prüfen' }).click(); }
  await page.waitForTimeout(500);
  assert.ok(calls.filter((c) => c.aktion === 'schule_wiederholung').length > wdh0, 'Wiederholung neu geladen');
  assert.equal(await page.locator('.err-text').count(), 0);
});

// W177: Flugtest schon geschrieben, danach neue Pflicht-Etappen → Nachtragstest statt Sackgasse („Test bereit“, aber kein Test)
test('W177: Nachtragstest für Etappen, die nach dem Flugtest dazukamen', async (t) => {
  const mitStand = (offen) => (aktion, e) => aktion === 'schule_einheit_lesen'
    ? { ...e, blocktest_fertig: true, nachtest: { grund: 'einheit_offen' }, etappen_stand: Object.fromEntries(ETAPPEN.map((x) => [x.lernziel, { fertig: true, sitzt: true, ziel: 2, serie: 2 }])), stand: ETAPPEN.map((x, i) => ({ lernziel: x.lernziel, pflicht: true, status: i < offen ? 'offen' : 'nachgewiesen' })) } : null;
  const { page, calls } = await setup(t, { anpassen: mitStand(2) });
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByRole('heading', { name: 'Test zu den neuen Etappen' }).waitFor();
  assert.match(await page.locator('.lern-test').innerText(), /Seit deinem Test sind 2 neue Etappen dazugekommen/);
  assert.equal(await page.getByRole('button', { name: 'Test starten', exact: true }).count(), 0, 'kein zweiter voller Flugtest');
  await page.getByRole('button', { name: 'Test zu den neuen Etappen starten' }).click();
  await page.getByText('Wie liest man 11 490 051?').waitFor();
  assert.equal(calls.find((c) => c.aktion === 'schule_test_starten')?.daten?.art, 'blocktest');
  // Flug-Seite (Erklären): Knopf direkt zum Nachtragstest
  await page.goto(origin + '/#/lerneinheit/1-1-erklaeren');
  await page.getByRole('link', { name: 'Alle Etappen sitzen – Test zu den neuen Etappen' }).waitFor();
  // ohne offene Pflicht-Etappe: kein Nachtragstest, alte Anzeige
  const zwei = await setup(t, { anpassen: mitStand(0) });
  await zwei.page.goto(origin + '/#/lerneinheit/1-1-test');
  await zwei.page.getByText('Gerade gibt es keinen Test. Üb weiter!').waitFor();
  assert.equal(await zwei.page.getByRole('heading', { name: 'Test zu den neuen Etappen' }).count(), 0);
});
