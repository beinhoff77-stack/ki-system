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
        if (r.format_ok) { if (!k.sitzt) { k.n = (k.n || 0) + 1; if (!r.richtig) k.f = (k.f || 0) + 1; if (d.hilfe || d.anlauf === 2) k.um = true; }
          if (r.richtig && !d.hilfe && d.anlauf !== 2) k.serie++; else if (!r.richtig) k.serie = Math.max(0, k.serie - 2); if (!k.sitzt && k.serie >= k.ziel) { k.sitzt = true; neu = true; } }
        e = { ok: true, ...r, ...(grund ? { grund } : {}), loesung: a.loesung, loesungsweg: 'Weg zur Lösung.', karte: (({ n: _n, f: _f, um: _um, ...x }) => ({ ...x, neu_sitzt: neu }))(k) };
        // AB-S: Feld landung nur in der Antwort, mit der die Etappe landet
        if (neu) e.landung = { landung_art: !k.f && !k.um && k.n <= k.ziel ? 'direkt' : (k.f || 0) <= 2 ? 'sauber' : 'sturm', bordkarten: k.n, ziel: k.ziel, fehler_endgueltig: k.f || 0,
          mit_tipp: 0, zweite_versuche: 0, stufe_gesenkt: (k.f || 0) > 2 ? 2 : 0, lerntage: 1, wieder_gelandet: false, eigene_loesungen: k.ziel, folge_ziel: Math.min(3, k.ziel) };
      }
    }
    else if (b.aktion === 'schule_test_starten') { stand.test = 77; e = { ok: true, sitzung_id: 77, art: d.art, aufgaben: [AUFG[14], AUFG[12]].map((a) => { const { loesung, ...r } = a; return r; }), beantwortet: [] }; }
    else if (b.aktion === 'schule_test_antwort') { const a = AUFG[d.aufgabe_id]; const r = bewerte(a, d.antwort); if (r.format_ok) stand.antworten[a.id] = { w: d.antwort, ok: r.richtig }; e = { ok: true, format_ok: r.format_ok, hinweis: r.hinweis, gespeichert: r.format_ok }; }
    else if (b.aktion === 'schule_test_abschliessen') {
      const erg = [AUFG[14], AUFG[12]].map((a) => ({ aufgabe_id: a.id, lernziel: a.lernziel, frage: a.frage, antworten: a.antworten, antwort: stand.antworten[a.id]?.w ?? null, richtig: !!stand.antworten[a.id]?.ok, loesung: a.loesung, loesungsweg: 'Weg.' }));
      e = { ok: true, sitzung_id: 77, richtig: erg.filter((x) => x.richtig).length, gesamt: 2, ergebnisse: erg, lernziele: [{ lernziel: 'lesen', pflicht: true, status: 'nachgewiesen' }, { lernziel: 'strahl', pflicht: true, status: 'fehler' }], einheit_abgeschlossen: false, ort: { abgeschlossen: false } };
    }
    if (opt.anpassen && e) e = opt.anpassen(b.aktion, e, d) || e; // Schritt D: Antwort nach einer Migration nachbilden
    else if (opt.anpassen?.neueAktionen) e = opt.anpassen(b.aktion, null, d) || e; // Aktionen, die der Standard-Mock nicht kennt (LM-S)
    await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
  });
  return { page, calls, appCalls };
}

test('Lernen: Eltern sehen Kinder, Belohnungen und offene Wünsche', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lernen');
  // Was auf eine Antwort wartet, steht als blauer Eintrag in „Zu tun“ (I-2); das alte Lernblatt ist eingeklappt am Ende.
  await page.locator('.lern-zutun .zt-blau.zt-wunsch').waitFor();
  assert.equal(await page.getByText('WARTET AUF DICH').count(), 0, 'kein eigener Kasten mehr');
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
  await page.getByText('1 von 2 richtig').waitFor(); // H7: keine „Punkte“ mehr in Kindertexten
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

test('Lehrplan (LM, früher LA-7): Inhaltsstand, Aufträge, Lernstand je Kind, Inhalte ansehen und Bauen lassen im Detail der Matrix', async (t) => {
  const { page, calls } = await setup(t);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lehrplan');
  await page.getByRole('heading', { name: 'Mathe Klasse 5–10: was gelernt wird' }).waitFor();
  assert.equal(await page.locator('.mx-chip').count(), 5, 'alle Themen');
  // reines Realschul-Thema: gestrichelt in der Klasse der Realschule
  assert.match(await page.locator('.mx-chip', { hasText: 'Nur Realschule' }).getAttribute('class'), /mx-zu/);
  assert.match(await page.locator('.mx-chip', { hasText: 'Große natürliche Zahlen' }).locator('.mx-sch').innerText(), /Gym 5\s*RS 5\s*IB 1/);
  const det = page.locator('.mx-detail');
  await page.locator('.mx-chip', { hasText: 'Teilbarkeit' }).click();
  assert.match(await det.innerText(), /Inhalt: in Prüfung/);
  // kein Inhalt → „Ändern lassen“ (E-3: ein Knopf überall)
  await page.locator('.mx-chip', { hasText: 'Lineare Funktionen' }).click();
  assert.match(await det.innerText(), /Inhalt: fehlt/);
  assert.equal(await det.getByRole('button', { name: 'Bauen lassen' }).count(), 0);
  await det.getByText('✎ Ändern lassen').click();
  await det.getByRole('button', { name: 'Auftrag senden' }).click();
  await det.getByText('Danke – der Auftrag ist angekommen', { exact: false }).waitFor();
  const rm = calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten;
  assert.equal(rm.art, 'thema_fehlt'); assert.equal(rm.bezug, 'flug'); assert.equal(rm.block_id, 70); assert.match(rm.text, /Lineare Funktionen/);
  // fertig, Aufträge, Lernstand beider Kinder
  await page.locator('.mx-chip', { hasText: 'Große natürliche Zahlen' }).click();
  assert.match((await det.innerText()).replace(/\s+/g, ' '), /Inhalt: fertig · Inhalte ansehen \(3 Etappen\) › · 1 Auftrag/);
  await page.getByRole('group', { name: 'Lernstand' }).getByRole('button', { name: 'Beide vergleichen' }).click();
  assert.match(await det.locator('.mx-ls').innerText(), /Kind A[\s\S]*In Wiederholung[\s\S]*Kind B[\s\S]*Nicht im Plan/);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lehrplan-820.png'), fullPage: true });
  await det.getByRole('link', { name: /Inhalte ansehen/ }).click();
  await page.waitForURL(/#\/inhalte\/1$/);
  // Teil 4 Punkt 4: geprüfter Flug – die gesperrte Bordkarte ist „aussortiert“, nicht „in Prüfung“, und zählt nicht mit
  await page.getByText('3 Etappen · 1 Bordkarte zum Üben · 1 für Test und Nachtest · 1 aussortiert', { exact: false }).waitFor();
  await page.locator('details.lp-karte > summary').first().click();
  await page.getByText('ERKLÄRUNG, WIE DAS KIND SIE SIEHT').first().waitFor();
  await page.locator('.lp-tabelle').first().getByText('frei ✓').first().waitFor();
  assert.equal(await page.locator('details.lp-karte > summary', { hasText: 'in Prüfung' }).count(), 0);
  const weg = page.locator('details.lp-aussortiert').first();
  await weg.evaluate((d) => { d.closest('details.lp-karte').open = true; });
  assert.equal(await weg.locator('summary').innerText(), '1 aussortierte Bordkarte (ersetzt oder überzählig) anzeigen');
  assert.equal(await weg.evaluate((d) => d.open), false, 'zugeklappt');
  await weg.locator('summary').click(); await weg.getByText('aussortiert', { exact: true }).waitFor();
  assert.match(await weg.evaluate((d) => d.closest('details.lp-karte').querySelector('summary').innerText), /· 0 Bordkarten$/, 'Etappe zählt nur aktive (die einzige ist aussortiert)');
  await page.locator('.lp-tabelle').first().getByText('Tausender-Stelle.').waitFor();
  await page.getByText('Mehr Aufgaben zum Runden.').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/inhalte-390.png'), fullPage: true });
  const w = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth); assert.ok(w <= 0, 'keine Querverschiebung: ' + w);
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

test('Was wackelt? (LA-3) – Tabelle der Etappen mit Fehlern, aufgeklappt die echten falschen Antworten und „Kurz gesagt“', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/lernen');
  await page.getByRole('link', { name: 'Kind A', exact: true }).click(); // LA-1: Zeile → Seite des Kindes → Reiter „Was wackelt“
  await page.getByRole('link', { name: 'Was wackelt', exact: true }).click();
  await page.waitForURL(/#\/kind\/1-wackelt$/);
  await page.getByRole('heading', { name: 'Was wackelt?', exact: true }).waitFor();
  await page.setViewportSize({ width: 820, height: 1180 }); // Tabelle ab 560 px (I-1: darunter Karten)
  assert.match(await page.locator('.ls-woche').innerText(), /^Diese Woche: 30 Bordkarten \(Aufgabe\), 22 richtig, 4-mal mit Tipp/);
  assert.deepEqual(await page.locator('.ls-tabelle thead th').allInnerTexts(), ['ETAPPE (LERNSCHRITT)', 'RICHTIG / FALSCH', 'HÄUFIGSTER FEHLER', 'SEIT']);
  const zeilen = page.locator('.ls-tabelle tbody tr.ls-zeile');
  assert.deepEqual(await zeilen.locator('th b').allInnerTexts(), ['Runden', 'Welchen Wert hat eine Ziffer?'], 'wackelt zuerst');
  await zeilen.first().getByText('2 / 5').waitFor();
  assert.equal(await page.getByText('Was kommt wann wieder?').count(), 0, 'Regelblock steht auf „So funktioniert’s“');
  await zeilen.first().click();
  await page.locator('.ls-detail').getByText('Antwort: 929 000').waitFor();
  await page.locator('.ls-detail').getByText('richtig: 930 000').waitFor();
  await page.locator('.ls-detail').getByRole('link', { name: 'Erklärung ansehen ›' }).waitFor();
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lernstand-390.png'), fullPage: true });
});

// LA-8: rechts ist „Nach Themengebiet“ Standard – für die LA-4-Ansicht umschalten
const nachKlasse = (page) => page.locator('.lern-plan-lehrplan').getByRole('button', { name: 'Nach Klasse (Lehrplan)' }).click();
const gebietWaehlen = (page, g) => page.locator('.lern-plan-lehrplan').getByRole('group', { name: 'Themengebiet' }).getByRole('button', { name: g, exact: true }).click();
test('Kinderplan: Schulart und Klasse setzen', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/plan/1');
  // Zugeklappt eine Zeile je Ort; aufgeklappt hinter jedem Flug die Klasse je Schulart.
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.waitFor();
  assert.equal(await rom.locator('.lern-plan-themen').count(), 0); // LA-8: Flugtitel stehen in der Überschrift, die Flugliste erst aufgeklappt
  await rom.locator('.lern-plan-ort').click();
  await rom.locator('.lern-plan-themen').getByText('Ganze Zahlen').waitFor();
  await rom.getByText('Gym 5 · RS 5 · IB MYP-Jahr 2').waitFor();
  // Rechts der Lehrplan der eigenen Schulart und Klasse
  const lp = page.locator('.lern-plan-lehrplan'); // LA-4: Reiter und Klassen-Knöpfe statt Auswahllisten
  await nachKlasse(page);
  assert.equal(await lp.getByRole('group', { name: 'Schulart' }).locator('[aria-pressed=true]').innerText(), 'Gymnasium');
  assert.match(await lp.getByRole('group', { name: 'Klasse' }).locator('[aria-pressed=true]').innerText(), /^Kl\. 5\s*Kind$/, 'LB-1: Klasse des Kindes markiert');
  await page.screenshot({ path: path.join(root, 'test-results/themenplan-390.png'), fullPage: true });
  // LA-6: Klasse steht im Blatt „⚙ Einstellen“ und speichert sofort – kein eigener Knopf
  assert.equal(await page.getByRole('combobox', { name: 'Klasse des Kindes' }).count(), 0, 'nicht mehr im Plan');
  await page.locator('.lern-kind-kopf').getByRole('button', { name: 'Kind A einstellen' }).click();
  const blatt = page.getByRole('dialog', { name: 'Kind A einstellen' });
  await blatt.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: '6', exact: true }).click();
  await blatt.locator('[role=status]', { hasText: 'Gespeichert' }).first().waitFor();
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
  await page.getByRole('link', { name: 'Kind A', exact: true }).waitFor();
  assert.equal(await page.getByText('Zugänge', { exact: true }).count(), 0, 'Lehrer verwaltet keine Zugänge');
  assert.equal(await page.getByRole('heading', { name: 'Mathe Klasse 7/8' }).count(), 0);
  assert.equal(await page.getByText('Lernen starten').count(), 0, 'LA-2: kein „Lernen starten“ für Lehrer');
  await page.getByRole('link', { name: 'Kind A', exact: true }).click();
  await page.getByRole('link', { name: 'Plan', exact: true }).click();
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
  await page.locator('.lern-plan-zeile').nth(2).getByLabel('alle Flüge: kann er komplett').click(); // LB-5: der Ort rückt nach „◉ Kann er komplett“
  await page.locator('.lern-plan-komplett summary', { hasText: 'Kann er komplett · 1 Ort · 1 Flug komplett gekonnt' }).waitFor();
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
  assert.equal(await page.locator('.lern-plan-zeile').nth(2).getByLabel('alle Flüge: kann er komplett').isChecked(), false);
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
  await page.locator('.lern-zutun').waitFor();
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
  const reihenfolge = () => page.locator('.lern-plan-zeile .lern-plan-ort > b').evaluateAll((bs) => bs.map((b) => b.title)); // Teil 9 N7: auf dem Handy steht das Gebiet in der Zeile darunter
  await page.goto(origin + '/#/plan/1');
  await page.locator('.lern-plan-zeile').first().waitFor();
  await page.getByRole('button', { name: 'New York – Zinsen nach oben' }).click();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  // Seite verlassen und zurück: die Änderung ist da.
  await page.goto(origin + '/#/lernen'); await page.locator('.lern-zutun').waitFor();
  await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-zeile').first().waitFor();
  assert.deepEqual(await reihenfolge(), ['Geld – Zinsen', 'Zahlen – Natürliche Zahlen']);
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
  assert.deepEqual(await reihenfolge(), ['Zahlen – Teilbarkeit und Primzahlen', 'Geld – Zinsen', 'Zahlen – Natürliche Zahlen']);
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
  await page.locator('.lern-zutun').waitFor();
  // oben rechts, vor allem anderen
  const link = page.locator('#main .lern-was-ist-los .lern-info-oben a', { hasText: 'So funktioniert’s' }); // I-2: in der Kopfzeile rechts
  const box = await link.boundingBox(); assert.ok(box.x + box.width > 820 / 2 && box.y < 200, 'Link oben rechts: ' + JSON.stringify(box));
  await link.click();
  await page.waitForURL(/#\/info$/);
  await page.getByRole('heading', { name: 'Erste Schritte' }).waitFor();
  assert.deepEqual(await page.locator('.lern-info-schritt h3').allInnerTexts(), ['Flugplan prüfen', 'Lernstand lesen', 'Inhalte ansehen', 'Ändern lassen']);
  assert.equal(await page.locator('details.lern-info-frage').count(), 7);
  await page.getByText('Wie wird gelernt?').click();
  await page.getByText('6 eigene Lösungen (richtig im ersten Versuch ohne Tipp', { exact: false }).waitFor();
  await page.getByText('nach 1, 3, 7, 14 und 30 Lerntagen', { exact: false }).waitFor();
  await page.getByText('mindestens 6 und höchstens 12', { exact: false }).waitFor();
  await page.getByText('Zuerst kommt die Erklärung', { exact: false }).waitFor();
  await page.getByText('zuerst einen zweiten Versuch', { exact: false }).waitFor();
  const text = await page.locator('#main').innerText();
  assert.doesNotMatch(text, /Lernkarte|Aufgabe|Themenplan/, 'nur Reisewörter'); // Entscheidung 21.11.: „Thema/Themen“ auf Eltern-/Lehrerseiten erlaubt
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/info-820.png'), fullPage: true });
  // aus dem Flugplan mit einem Tipp
  await page.getByRole('link', { name: 'Plan Kind A ›' }).click();
  await page.locator('.lern-plan-zeile').first().waitFor();
  await page.locator('.lern-info-oben a', { hasText: 'So funktioniert’s' }).click();
  await page.waitForURL(/#\/info$/);
  // Kinder kommen nicht auf die Info-Seite.
});

test('Reisewörter auf allen Eltern-/Lehrerseiten', async (t) => {
  const { page } = await setup(t);
  // Entscheidung Sebastian 21.11. (Teil 9 Punkt 3 / N8): auf Eltern-/Lehrerseiten sind „Thema“, „Themen“ und „Themengebiet“ erlaubt – Lehrer denken in Themen.
  // Die übrigen Reisewörter gelten weiter; für die Kinderseiten prüfen die Tests der Kinderansicht („nur Reisewörter“).
  const verboten = /Lernkarte|Aufgabe|Themenplan|Lernziel|\bGebiet/;
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion === 'schule_zugaenge') return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, zugaenge: [{ id: 1, name: 'Herr Lehrer', rolle: 'lehrer', aktiv: true, zuletzt: null }] } }) });
    return route.fallback();
  });
  for (const [pfad, warte] of [['lernen', 'Zu tun'], ['kind/1-ueberblick', 'Wo hakt es?'], ['plan/1', 'Lehrplan'], ['lehrplan', 'Mathe Klasse 5–10'], ['inhalte/1', 'zum Üben'], ['wackelt/1', 'Was wackelt?'], ['lernstand/1', 'Einstieg prüfen'], ['schulstand', 'Alle Kinder im Vergleich'], ['lernauftraege', 'Neuer Auftrag (allgemein)'], ['zugaenge', 'Neuen Zugang anlegen'], ['info', 'Erste Schritte']]) {
    await page.goto(origin + '/#/' + pfad);
    await page.getByText(warte, { exact: false }).first().waitFor();
    await page.evaluate(() => document.querySelectorAll('#main details').forEach((d) => { d.open = true; }));
    // Inhalte der Mathematik (Titel aus der Datenbank, Texte der Kinder) sind keine App-Texte: nur feste Texte prüfen.
    const text = await page.evaluate(() => { const c = document.querySelector('#main').cloneNode(true);
      c.querySelectorAll('.lern-wort-erkl, .lp-erkl, .lp-tabelle, .lern-rm-text, .lern-rm-antwort, .ls-fehler p, .lern-plan-themen b, .lp-text > b, .ls-kopf b, .lern-katalog b').forEach((x) => x.remove());
      c.querySelectorAll('select option').forEach((o) => { o.textContent = o.textContent; });
      return c.innerText.replaceAll('Mehr Aufgaben zum Runden.', '').replaceAll('6 neue Aufgaben ergänzt.', '').replaceAll('= ein Mathe-Thema', '').replace(/Themen im Plan oder schon gekonnt/g, '') + ' ' + // die gewollte Erklärung auf der Info-Seite
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
  // Teil 4 Punkt 5g: zwei klare Wege; „Gleich verbessern ›“ ist ein Knopf (startet die Korrektur), kein Link auf die eigene Adresse
  assert.deepEqual((await knoepfe.locator('a, button').allInnerTexts()).map((x) => x.trim()), ['Erst üben: Zahlenstrahl ›', 'Gleich verbessern ›', 'Zum Flug', 'Zur Abflugtafel']);
  assert.equal(await knoepfe.locator('a.lr-knopf').getAttribute('href'), '#/lerneinheit/1-1-ueben-2');
  assert.equal(await knoepfe.locator('button.lr-knopf-zweit').innerText(), 'Gleich verbessern ›');
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
  assert.equal(await zeilen.nth(1).locator('.lern-plan-ort b').innerText(), 'Zahlen – Flug A Melbourne und Flug B Melbourne');
  // Seite verlassen und zurück: Melbourne bleibt auf Platz 2
  await page.goto(origin + '/#/lernen'); await page.locator('.lern-zutun').waitFor();
  await page.goto(origin + '/#/plan/1'); await zeilen.nth(1).waitFor();
  assert.equal(await zeilen.nth(1).locator('.lern-plan-ort b').innerText(), 'Zahlen – Flug A Melbourne und Flug B Melbourne');
  assert.equal(db.eintraege[1].block_id, 109);
});

test('E-2: Ort aus dem Lehrplan in den Plan ziehen; Finger (Touch) zieht ebenso', async (t) => {
  const { page, calls } = await setup(t);
  await page.setViewportSize({ width: 1280, height: 900 });
  await planDb(page, calls, { orte: vieleOrte(), plan: [100, 101, 102] });
  await page.goto(origin + '/#/plan/1');
  await page.locator('.lern-plan-zeile').nth(2).waitFor();
  await nachKlasse(page);
  const quelle = page.locator('.lern-plan-klasse .lern-lp-zeile', { hasText: 'Flug A Kairo' }).locator('.lern-plan-griff');
  await quelle.evaluate((x) => x.scrollIntoView({ block: 'center' })); const q = await quelle.boundingBox();
  const ziel = await page.locator('.lern-plan-zeile').nth(1).boundingBox();
  await page.mouse.move(q.x + 10, q.y + 10); await page.mouse.down();
  await page.mouse.move(ziel.x + 80, ziel.y + 4, { steps: 10 }); await page.mouse.up();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen')[0].daten.eintraege.map((x) => x.block_id), [100, 103, 101, 102]);
  // Touch: dieselben Pointer-Ereignisse mit pointerType touch (LB Teil 5 K2: die Lehrplan-Spalte rollt mit der Seite – erst nach oben)
  await page.evaluate(() => window.scrollTo(0, 0));
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
  // nach dem Speichern werden die Stufen neu gelesen und die Liste neu gezeichnet – am angehängten Griff messen
  await page.waitForFunction(() => { const g = document.querySelector('.lern-plan-griff'); return g?.isConnected && getComputedStyle(g).touchAction === 'none'; });
  await page.screenshot({ path: path.join(root, 'test-results/e2-flugplan-1280.png') });
});

test('E-2: Flug im Ort abwählen – gespeichert als ausgelassen, Kind sieht ihn nicht; ohne Migration keine Häkchen', async (t) => {
  const { page, calls } = await setup(t);
  await planDb(page, calls, { orte: vieleOrte(), plan: [100, 101] });
  await page.goto(origin + '/#/plan/1');
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.locator('.lern-plan-ort').click();
  await rom.getByRole('button', { name: 'Flug B Rom: Aus dem Plan nehmen' }).click(); // LB-2: Knopf statt Häkchen
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
  await rom.getByText('Einzelne Flüge abwählen geht hier noch nicht.').waitFor(); // I-9: ohne „Datenbank“
  assert.equal(await rom.getByRole('checkbox', { name: /im Plan/ }).count(), 0);
  await page.getByRole('button', { name: 'Athen – Flugort 2 nach oben' }).click();
  await page.locator('.lern-plan-kopf').getByText('Gespeichert', { exact: true }).waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen')[0].daten.eintraege, [{ block_id: 101, kann_schon: false }, { block_id: 100, kann_schon: false }]);
});

test('E-2/LA-2: Stand je Schulart in der Kinder-Tabelle (GYM · RS · IB, IB Klasse 5: „– (ab Kl. 6)“)', async (t) => {
  const { page } = await setup(t);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lernen');
  const a = page.locator('.lern-kinder-tabelle tr', { hasText: 'Kind A' });
  await a.waitFor();
  assert.deepEqual((await a.locator('.lern-st-zelle b').allInnerTexts()), ['Kl. 5', 'Kl. 5', '– (ab Kl. 6)']); // I-8: kurz
  await a.getByText('Rom · Natürliche Zahlen (2/4)').waitFor();
  assert.equal(await page.locator('.lern-kinder-tabelle tbody tr').count(), 2, 'je Kind eine Zeile (Testkind nicht)');
  for (const t2 of ['Lehrplan', 'Expeditionen', 'Meine Aufträge', 'So funktioniert’s']) await page.locator('.lern-nachschlagen').getByRole('link', { name: t2, exact: true }).first().waitFor();
});

test('E-3: derselbe Knopf an Erklärung, Etappe, Flug und Plan; der Auftrag trägt den Bezug', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/inhalte/1');
  await page.getByText(/Bordkarten? zum Üben/).waitFor();
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
    ['Gymnasium Klasse 5: 2 von 3 Flügen gelandet', 'Realschule Klasse 6: 1 von 1 Flügen gelandet', 'IB noch kein MYP-Jahr: 0 von 0 Flügen gelandet']);
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
  await page.goto(origin + '/#/schulstand'); // LA-1: Seite bleibt, wird aber nicht mehr verlinkt
  const felder = page.locator('.lern-stand-feld');
  await felder.first().waitFor();
  assert.equal(await felder.count(), 6, '2 Kinder × 3 Schularten (Testkind nicht)');
  assert.equal(await felder.nth(0).getAttribute('aria-label'), 'Kind A, Gymnasium Klasse 5: 2 von 3 gelandet');
  await felder.nth(0).click();
  await page.waitForURL(/#\/kind\/1-stand-gym_by$/); // alte Adresse leitet auf den Reiter „Stand“ um
  await page.locator('.lern-stand-raster').waitFor();
  await page.getByText('Orientierung, keine Einstufung durch eine Schule').first().waitFor(); // erst lesen, wenn die Seite fertig gezeichnet ist (sonst gelegentlich „Lade …“)
  assert.match(await page.locator('main').innerText(), /Orientierung, keine Einstufung durch eine Schule/);
  // Einstieg prüfen Klasse 7: alles bis Klasse 6 = 3 Flüge Kl. 5 + 1 Flug Kl. 6 → 2 von 4 gelandet = 50 % → rot
  await page.locator('.lern-chips-zeile[aria-label="Einstieg prüfen"] a', { hasText: 'Kl. 7' }).click();
  await page.waitForURL(/#\/kind\/1-stand-gym_by-7$/);
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
  await page.waitForURL(/#\/kind\/1-stand-gym_by-7-0-5$/);
  await page.locator('.lern-etappen-stand li').first().waitFor();
  assert.match(await page.locator('.lern-etappen-stand li').first().innerText(), /sitzt – nach 9 Bordkarten/);
  assert.ok(calls.some((c) => c.aktion === 'schule_lernstand' && c.daten.lernender_id === 1));
  // Lernstand zeigt die Zahl ebenfalls
  await page.getByRole('link', { name: /Was wackelt\?/ }).click();
  await page.locator('.ls-alle summary').click(); // LA-3: Stand je Etappe unter „Alle Etappen mit Stand“
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
  await page.locator('.lern-kind-kopf').getByRole('button', { name: /einstellen$/ }).click(); // LA-6: Vorlage im Blatt „⚙ Einstellen“, mit Rückfrage
  const blatt = page.getByRole('dialog');
  await blatt.locator('.lern-vorlage summary').click();
  const knopf = blatt.locator('.lern-vorlage .row > button').first();
  assert.equal(await knopf.innerText(), 'Plan ersetzen (2 Orte)');
  assert.match(await blatt.locator('.lern-vorlage-vorschau').innerText(), /in Lehrplan-Reihenfolge[\s\S]*Wien[\s\S]*Oslo/);
  await knopf.click();
  assert.equal(calls.filter((c) => c.aktion === 'schule_plan_setzen').length, 0, 'erst nach der Rückfrage');
  await blatt.getByRole('button', { name: 'Ja, Plan ersetzen' }).click();
  await blatt.getByText('Plan ersetzt und gespeichert.').waitFor();
  assert.deepEqual(db.eintraege.map((x) => [x.block_id, x.ausgelassen]), [[201, []], [200, [2]]]);
  await blatt.getByRole('button', { name: '↶ Rückgängig' }).click();
  await blatt.getByText('Rückgängig gemacht · Gespeichert').waitFor();
  assert.deepEqual(db.eintraege.map((x) => x.block_id), [202]);
  await blatt.getByRole('button', { name: 'Schließen' }).click();
  await page.waitForFunction(() => document.querySelectorAll('.lern-plan-zeile').length === 1);
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
  // M3/LB-2: aufgeklappt steht die Stufe in derselben Zeile wie der Flugname, darunter die Knöpfe (statt Häkchen)
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.locator('.lern-plan-ort').click();
  const flug = rom.locator('.lern-plan-themen li').first();
  const [h, n] = [await flug.locator('.lern-st-sym').boundingBox(), await flug.locator('.lern-plan-flug b').boundingBox()];
  assert.ok(Math.abs((h.y + h.height / 2) - (n.y + n.height / 2)) < 14 && h.x < n.x, 'Stufe links neben dem Flugnamen');
  await flug.getByRole('group', { name: /Einstellung für/ }).getByRole('button', { name: /Aus dem Plan nehmen/ }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/m3-ort-aufgeklappt-820.png') });
  // M2/LA-6: Klasse im Blatt „⚙ Einstellen“ speichert sofort; beim Schließen wird der Plan neu gezeichnet
  await page.locator('.lern-kind-kopf').getByRole('button', { name: /einstellen$/ }).click();
  await page.getByRole('dialog').getByRole('group', { name: 'Klasse' }).getByRole('button', { name: '8', exact: true }).click();
  await page.getByRole('dialog').locator('[role=status]', { hasText: 'Gespeichert' }).first().waitFor();
  assert.ok(calls.some((c) => c.aktion === 'schule_kind_setzen' && c.daten.klasse === 8));
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
  // Maus: Platz 6 (Oslo) → Platz 2 (LA-1: über dem Plan stehen Kopf und Reiter der Kind-Seite – erst ins Bild rollen)
  await page.evaluate(() => window.scrollBy(0, 200));
  const g = await zeilen.nth(5).locator('.lern-plan-griff').boundingBox(); const z = await zeilen.nth(1).boundingBox();
  await page.mouse.move(g.x + g.width / 2, g.y + g.height / 2); await page.mouse.down();
  await page.mouse.move(g.x + g.width / 2, z.y + 6, { steps: 10 }); await page.mouse.up();
  await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
  assert.deepEqual(db.eintraege.slice(0, 3).map((x) => x.block_id), [100, 105, 101]);
  // Handy, Finger: letzte Zeile (Accra) bis ganz nach oben – die Seite rollt beim Ziehen am oberen Rand mit
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(origin + '/#/lernen'); await page.locator('.lern-zutun').waitFor(); // erst weg, damit nicht die alte Liste gemessen wird
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
  const vorher = calls.filter((c) => c.aktion === 'schule_uebung_pruefen').length;
  await page.locator('.lr-knobel .lr-stufe-bonus').waitFor(); // Teil 4 Punkt 5d: kommt nach der Landung von selbst
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
  await page.goto(origin + '/#/wackelt/1'); await page.locator('.ls-alle summary').click(); await page.locator('.ls-knobel').first().waitFor();
  assert.equal(await page.locator('.ls-knobel').first().innerText(), 'Knobel: 1 von 2');
  await page.goto(origin + '/#/inhalte/1'); await page.locator('details.lp-karte summary').first().click();
  const zeilen = page.locator('details.lp-karte').first().locator('.lp-tabelle tbody tr');
  assert.match(await zeilen.first().locator('td').first().innerText(), /leicht\s*wie im Beispiel/);
  assert.match(await zeilen.last().locator('td').first().innerText(), /★ Knobel\s*freiwillig/);
});

// ---------- Zusatz 1 zu Bau-Auftrag F: „Lernstand“ öffnet die Klassen-Übersicht des Kindes ----------
test('LA-1: Seite des Kindes mit 4 Reitern; alte Adressen leiten um; Reiter „Stand“ in der Schulart des Kindes', async (t) => {
  const { page } = await setup(t, { anpassen: standAnpassen() });
  await page.goto(origin + '/#/lernen');
  await page.getByRole('link', { name: 'Kind A', exact: true }).click();
  await page.waitForURL(/#\/kind\/1-ueberblick$/);
  await page.locator('.lern-reiter a[aria-current]', { hasText: 'Überblick' }).waitFor(); // erst lesen, wenn die Reiter gezeichnet sind
  assert.deepEqual(await page.locator('.lern-reiter a').allInnerTexts(), ['Überblick', 'Was wackelt', 'Stand', 'Plan']);
  for (const f of ['Lernt es?', 'Wo hakt es?', 'Wo steht es?', 'Was kommt?']) await page.getByRole('heading', { name: f }).waitFor();
  await page.getByRole('link', { name: 'Stand', exact: true }).click();
  await page.waitForURL(/#\/kind\/1-stand$/);
  await page.locator('.lern-stand-raster').waitFor();
  assert.equal(await page.locator('.lern-reiter a[aria-current]').innerText(), 'Stand');
  assert.equal(await page.locator('.lern-chips-zeile[aria-label="Schulart"] a[aria-current]').innerText(), 'Gymnasium', 'in der Schulart des Kindes');
  await page.locator('.lern-chips-zeile[aria-label="Schulart"] a', { hasText: 'Realschule' }).click();
  await page.waitForURL(/#\/kind\/1-stand-rs_by$/);
  // alte Adressen
  for (const [alt, neu, reiter] of [['lernstand/1', /#\/kind\/1-stand$/, 'Stand'], ['wackelt/1', /#\/kind\/1-wackelt$/, 'Was wackelt'], ['lernstand/1-rs_by', /#\/kind\/1-stand-rs_by$/, 'Stand'], ['plan/1', /#\/kind\/1-plan$/, 'Plan']]) {
    await page.goto(origin + '/#/' + alt); await page.waitForURL(neu); await page.locator('.lern-reiter a[aria-current]', { hasText: reiter }).waitFor();
  }
  // „Alle Kinder im Vergleich“ ist nicht mehr verlinkt
  await page.goto(origin + '/#/lernen'); await page.locator('.lern-zutun').waitFor();
  assert.equal(await page.getByRole('link', { name: /Alle Kinder im Vergleich/ }).count(), 0);
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
  await page.goto(origin + '/#/wackelt/1'); await page.locator('.ls-alle summary').click();
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
  assert.equal(c.daten.aktuell_einheit, 1); assert.equal(c.daten.aktuell_lernziel, 'stellenwert'); // H10: der Server prüft, dass es nicht die aktuelle Etappe ist
  assert.equal(await page.locator('.lr-checkliste').innerText(), vorher, 'aktuelle Etappe unverändert');
  // Knobel-Bordkarten kommen nie als Mischkarte: die nächste Bordkarte ist eine normale aus Rom
  await page.getByRole('button', { name: /Neue Bordkarte/ }).click();
  await page.getByText(/BORDKARTE 2 · ROM/).waitFor();
});

// ---------- Wunsch 18.11.: „Lernen starten“ an der Kinderkarte ----------
test('LA-2: „Lernen starten“ bleibt für Eltern (Zeile und Seite des Kindes), entfällt für Lehrer', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  for (const [b, h] of [[390, 844], [820, 1180]]) {
    await page.setViewportSize({ width: b, height: h });
    await page.goto(origin + '/#/lernen'); await page.locator('.lern-zutun').waitFor();
    const knopf = page.getByRole('link', { name: 'Lernen starten: Kind A' });
    assert.equal(await knopf.getAttribute('href'), '#/reise/1');
  }
  await page.getByRole('link', { name: 'Lernen starten: Kind A' }).click();
  await page.waitForURL(/#\/reise\/1$/);
  await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  await page.goto(origin + '/#/kind/1-ueberblick'); await page.locator('.lern-kind-kopf').getByRole('link', { name: 'Lernen starten: Kind A' }).waitFor();
  await page.goto(origin + '/#/info');
  await page.getByText('Im Eltern-Zugang hat jede Zeile und die Seite des Kindes den Knopf „Lernen starten“', { exact: false }).waitFor();
});

test('LA-2: Lehrer – kein „Lernen starten“, auf der Seite des Kindes klein „Lernreise ansehen“', async (t) => {
  const { page } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/lernen/#/lernen'); await page.locator('.lern-zutun').waitFor();
  assert.equal(await page.getByText('Lernen starten').count(), 0);
  await page.goto(origin + '/lernen/#/kind/1-ueberblick');
  await page.locator('.lern-kind-kopf').getByRole('link', { name: 'Lernreise ansehen ›' }).waitFor();
  assert.equal(await page.getByText('Lernen starten').count(), 0);
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
  await page.getByText('EXPEDITION ABGESCHLOSSEN').waitFor();
  await page.getByText('2 von 3 Teilen selbst gelöst; bei den anderen hast du den Lösungsweg gesehen.').waitFor(); // H15: abgeschlossen ≠ selbst gelöst
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

// ---------- Bau-Auftrag H (Befunde der ChatGPT-Prüfung zu W176) ----------
const tippe = async (page, ziffern) => { for (const z of ziffern) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
  await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click(); };
const mitKarte = (lesen, karte) => (aktion, e) => {
  if (aktion === 'schule_uebung_pruefen' && e.karte) return { ...e, karte: { ...e.karte, ...karte } };
  return lesen(aktion, e);
};

test('H1: wieder geöffnete Etappe gilt in der App sofort als offen (Server-Antwort fertig = false), Checkliste statt „Gelandet“', async (t) => {
  const lesen = neueRegel({ stellenwert: { eigene_loesungen: 2, folge: 2, typen_anzahl: 1, sitzt: true, fertig: true, faellig: true } });
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mitKarte(lesen, { sitzt: false, fertig: false, eigene_loesungen: 2, folge: 0, folge_ziel: 2, typen_anzahl: 1, typen_noetig: 1, wieder_offen: true }) });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText('Gelandet – heute wiederholen').waitFor();
  for (const runde of [0, 1]) {
    await tippe(page, ['5']);
    if (runde === 0) { await page.getByText(/Versuch/).first().waitFor(); const loesch = page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: /Löschen|⌫/ }); if (await loesch.count()) await loesch.first().click(); }
  }
  await page.getByText('Die nächste zählt wieder voll.').waitFor();
  await page.locator('.lr-checkliste').waitFor();
  assert.equal(await page.getByText(/Gelandet/).count(), 0, 'nicht mehr „Gelandet“');
  assert.match(await page.locator('.lr-checkliste').innerText(), /2 in Folge: 0\/2/);
});

test('H3: dieselbe Bordkarte noch einmal richtig – „Die kennst du schon – gut wiederholt.“; ungezählte kommen zuerst', async (t) => {
  const lesen = (aktion, e) => { const x = neueRegel({ stellenwert: { eigene_loesungen: 1, folge: 1, gezaehlt: [11] } })(aktion, e); if (x) x.heute_selbst = 4; return x; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mitKarte(lesen, { neu_gezaehlt: false, eigene_loesungen: 1, folge: 2, folge_ziel: 2, typen_anzahl: 1, typen_noetig: 1, gezaehlt: [11], heute_selbst: 5 }) });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  assert.match(await page.locator('.lr-heute').innerText(), /heute 4 Aufgaben selbst gelöst/); // H6: Zähler vom Server
  await tippe(page, ['2', '0', '0', '0']);
  await page.getByText('Die kennst du schon – gut wiederholt.').waitFor();
  assert.match(await page.locator('.lr-heute').innerText(), /heute 5 Aufgaben/);
  const r = await page.evaluate(() => {
    const k = (id) => ({ id, stufe: 1, typ: 'direkt', frage: { text: `Aufgabe ${id}` } });
    const w = [k(1), k(2), k(3)]; lernWaehleBordkarte(w, { ziel: 6, neueRegel: true, eigene: 1, gezaehlt: new Set([1, 2]) }, null, new Set());
    const v = [k(1), k(2)]; lernWaehleBordkarte(v, { ziel: 6, neueRegel: true, eigene: 2, gezaehlt: new Set([1, 2]) }, null, new Set());
    return [w[0].id, v.length];
  });
  assert.deepEqual(r, [3, 2], 'ungezählte zuerst; sind alle gezählt, geht es trotzdem weiter');
});

test('I-2/H6: „heute selbst gelöst“ nach dem Tag des Servers, nicht nach dem Kalendertag des Geräts', async (t) => {
  const lesen = (aktion, e) => { const x = neueRegel({ stellenwert: { eigene_loesungen: 1, folge: 1, gezaehlt: [11] } })(aktion, e); if (x) Object.assign(x, { heute_selbst: 4, heute_tag: '2026-11-19' }); return x; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mitKarte(lesen, { neu_gezaehlt: false, eigene_loesungen: 1, folge: 2, folge_ziel: 2, typen_anzahl: 1, typen_noetig: 1, gezaehlt: [11], heute_selbst: 5, heute_tag: '2026-11-19' }) });
  // auf dem Gerät liegt ein Zähler eines anderen (Geräte-)Tags – er zählt nicht
  await page.addInitScript(() => { try { localStorage.setItem('lern.heute.1', JSON.stringify({ tag: '2000-01-01', n: 9, server: false })); } catch { /* egal */ } });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  assert.match(await page.locator('.lr-heute').innerText(), /heute 4 Aufgaben selbst gelöst/);
  assert.deepEqual(await page.evaluate(() => { const x = JSON.parse(localStorage.getItem('lern.heute.1')); return [x.tag, x.n, x.server, x.geraet === lernGeraetTag()]; }), ['2026-11-19', 4, true, true], 'Tag vom Server gespeichert');
  await tippe(page, ['2', '0', '0', '0']);
  await page.getByText('Die kennst du schon – gut wiederholt.').waitFor();
  assert.match(await page.locator('.lr-heute').innerText(), /heute 5 Aufgaben/);
  assert.equal(await page.evaluate(() => JSON.parse(localStorage.getItem('lern.heute.1')).tag), '2026-11-19');
  // ohne Server-Tag (alter Server): Gerät zählt selbst, nach Gerätetag
  assert.deepEqual(await page.evaluate(() => { localStorage.removeItem('lern.heute.1'); lernHeutePlus(1); lernHeutePlus(1); const x = JSON.parse(localStorage.getItem('lern.heute.1')); return [x.n, x.server, x.tag === lernGeraetTag(), lernHeute(1)]; }), [2, false, true, 2]);
  // I-3: Tageswechsel – Seite über Nacht offen: alter Server-Stand gilt nicht mehr; Antwort ohne Karte zählt neu; neuer Server-Tag ersetzt den Stand
  assert.deepEqual(await page.evaluate(() => {
    localStorage.setItem('lern.heute.1', JSON.stringify({ tag: '2026-11-19', n: 7, server: true, geraet: '2000-01-01' }));
    const vorher = lernHeute(1); lernHeutePlus(1); const nachPlus = lernHeute(1);
    lernHeuteSetzen(1, 2, '2026-11-20'); const neu = JSON.parse(localStorage.getItem('lern.heute.1'));
    return [vorher, nachPlus, neu.tag, neu.n, lernHeute(1)]; }), [0, 1, '2026-11-20', 2, 2]);
});

test('H4/H1: Eltern – „Flug-Nachtest bestanden“ getrennt von „sicher“, wieder geöffnete Etappe als „wieder offen“', async (t) => {
  const ls = (aktion, e) => {
    if (aktion !== 'schule_lernstand') return null; const y = structuredClone(e);
    Object.assign(y.einheiten[0].karten[0], { eigene_loesungen: 6, folge: 3, typen_anzahl: 2, sitzt: true, sicher: false, flug_nachtest: true });
    Object.assign(y.einheiten[0].karten[1], { eigene_loesungen: 4, folge: 0, typen_anzahl: 2, sitzt: false, wieder_offen: true, richtig: 6, falsch: 2 }); return y; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: ls });
  await page.goto(origin + '/#/wackelt/1'); await page.locator('.ls-alle summary').click();
  const a = page.locator('.ls-karte', { hasText: 'Welchen Wert hat eine Ziffer?' });
  await a.getByText('Flug-Nachtest bestanden').waitFor();
  assert.equal(await a.getByText('sicher', { exact: true }).count(), 0);
  const b = page.locator('.ls-karte', { hasText: 'Runden' });
  await b.getByText('wieder offen', { exact: true }).waitFor();
  await b.getByText(/War schon gelandet; in der Wiederholung zweimal falsch/).waitFor();
});

test('H7: Texte ohne „Serie“/„Punkte“ – Tipp „zählt nicht als eigene Lösung; unterbricht deine Folge nicht“', async (t) => {
  const quelle = fs.readFileSync(path.join(root, 'lernen.js'), 'utf8');
  assert.doesNotMatch(quelle, /zählt nicht für die Serie|deine Punkte bleiben|Punkte gesammelt|von \$\{[^}]+\} Punkten/);
  assert.match(quelle, /zählt nicht als eigene Lösung; unterbricht deine Folge nicht/);
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/info'); await page.getByText('Wie wird gelernt?').click();
  const info = await page.locator('#main').innerText();
  assert.doesNotMatch(info, /\bSerie\b/);
  assert.match(info, /Wieder offen:/); assert.match(info, /Flug-Nachtest bestanden/);
});

test('H13: Dosierung der Mischkarten – Klasse 5 jede 6., Klasse 8 jede 4., nie mit nur 2 gelandeten, nie bei gewählter Stufe, alle 8 verbraucht, nach Neustart wieder von vorn', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reise/1'); await page.getByRole('heading', { name: /Abflüge/ }).waitFor();
  const r = await page.evaluate(() => {
    const acht = () => Array.from({ length: 8 }, (_, i) => ({ id: 100 + i, quelle: ['flug', 'kontinent', 'aelter'][i % 3] }));
    const lauf = (jede, gelandet, n, opt = {}) => { const rest = acht(), z = { n: 0 }, treffer = [];
      for (let nr = 1; nr <= n; nr++) { const m = lernMischWahl(rest, { nr, jede, ab: 3, gelandet, zaehler: z, ...opt }); if (m) treffer.push(nr); } return [treffer, rest.length]; };
    return { kl5: lauf(6, 3, 24)[0], kl8: lauf(4, 3, 16)[0], zwei: lauf(4, 2, 40)[0], stufe: lauf(4, 5, 40, { aus: true })[0],
      alle: lauf(4, 5, 60), neustart: [lauf(4, 3, 8)[0], lauf(4, 3, 8)[0]] };
  });
  assert.deepEqual(r.kl5, [6, 12, 18, 24]);
  assert.deepEqual(r.kl8, [4, 8, 12, 16]);
  assert.deepEqual(r.zwei, []); assert.deepEqual(r.stufe, []);
  assert.deepEqual(r.alle, [[4, 8, 12, 16, 20, 24, 28, 32], 0], 'alle 8 genau einmal, danach keine mehr');
  assert.deepEqual(r.neustart[0], r.neustart[1], 'Lernkarte wechseln / Browser neu: Zählung beginnt neu, gleiche Abstände');
});

test('H13: nach einer falschen Mischkarte geht es normal weiter – dieselbe Mischkarte kommt in der Sitzung nicht wieder', async (t) => {
  const misch = (aktion, e) => {
    if (aktion !== 'schule_einheit_lesen') return null; const x = neueRegel({ strahl: { sitzt: true } })(aktion, e);
    x.mischkarten = [{ ...zeig(AUFG[14]), stufe: 2, einheit_id: 2, quelle: 'flug', stadt: 'New York', etappe: 'Große Zahlen lesen' }];
    x.misch_jede = 1; x.misch_ab = 1; return x; };
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: misch });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1');
  await page.getByText('BORDKARTE 1 · AUS DEINER REISE').waitFor();
  await page.getByText('elf Millionen vierhundertneuntausend…', { exact: true }).click(); await page.getByRole('button', { name: 'Prüfen' }).click(); // nur 2 Antworten: kein 2. Versuch
  await page.getByText('Das war: Große Zahlen lesen – New York').waitFor();
  await page.getByRole('button', { name: /Neue Bordkarte/ }).click();
  await page.getByText(/BORDKARTE 2 · ROM/).waitFor();
  assert.equal(calls.filter((c) => c.aktion === 'schule_uebung_pruefen' && c.daten.aufgabe_id === 14).length, 1, 'Mischkarte genau einmal');
});

// ---------- Bau-Auftrag LA: Lehrer-Aufbau ----------
const tagVor = (n) => { const d = new Date(); d.setDate(d.getDate() - n); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };
// Kind A lernt (heute, vor 2 Tagen), „Runden“ wackelt; Kind B hat keinen Lerntag und eine Rückreise nach Pisa; eine neue Antwort auf einen Auftrag
async function laLage(page, extra = {}) {
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); const d = b.daten || {};
    const antw = (x) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, ...x } }) });
    if (b.aktion === 'schule_lernstand') {
      if (d.lernender_id === 2) return antw({ kind: { id: 2, name: 'Kind B', klasse: 7 }, lerntage: [], woche: { aufgaben: 0, richtig: 0, mit_tipp: 0 }, einheiten: [], ...(extra.b || {}) });
      return antw({ kind: { id: 1, name: 'Kind A', klasse: 5 }, lerntage: [tagVor(0), tagVor(2)], woche: { aufgaben: 30, richtig: 22, mit_tipp: 4 },
        einheiten: [{ einheit_id: 1, titel: 'Natürliche Zahlen', ort: 'Rom', status: 'geprueft', zuletzt: new Date().toISOString(), karten: [
          { lernziel: 'stellenwert', titel: 'Welchen Wert hat eine Ziffer?', serie: 2, ziel: 2, sitzt: true, sitzt_am: new Date(Date.now() - 864e5).toISOString(), richtig: 6, falsch: 1, mit_tipp: 0, faellig: false, fehler: [], fehler_gruende: { vorzeichen: 1 } },
          { lernziel: 'runden', titel: 'Runden', serie: 0, ziel: 4, sitzt: false, richtig: 2, falsch: 5, mit_tipp: 3, faellig: false, zuletzt: new Date().toISOString(), regel: 'Ab 5 wird aufgerundet.', fehler_gruende: { gerundet: 2, komma: 1 }, ...(extra.runden || {}),
            fehler: [{ frage: 'Runde 929 773 auf Tausender.', antwort: { wert: '929 000' }, antworttyp: 'zahl', loesung: { wert: 930000 }, am: new Date().toISOString(), grund: 'gerundet' },
              { frage: 'Runde 4 550 auf Hunderter.', antwort: { wert: '4 500' }, antworttyp: 'zahl', loesung: { wert: 4600 }, am: new Date().toISOString(), grund: 'gerundet' }] }] }], ...(extra.a || {}) });
    }
    if (b.aktion === 'schule_rueckmeldungen') return antw({ rueckmeldungen: [{ id: 4, von: 'lehrer:Herr Lehrer', art: 'mehr_aufgaben', text: 'Mehr Aufgaben zum Runden.', status: 'erledigt', antwort: '6 neue Aufgaben ergänzt.', am: new Date().toISOString(), ort: 'Rom – Natürliche Zahlen' }] });
    return route.fallback();
  });
}
const laUebersicht = (aktion, e) => { if (aktion !== 'schule_uebersicht') return null; const x = structuredClone(e);
  x.lernende[1].route.push({ block_id: 47, position: 1, art: 'rueckreise', status: 'offen', kann_schon: false }); return x; };

test('LA-2: Startseite „Was ist los?“ – Zu tun rot → gelb → blau, Kinder-Tabelle; Tablet ohne Rollen; Zeile öffnet das Kind', async (t) => {
  const { page } = await setup(t, { anpassen: laUebersicht });
  await laLage(page);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lernen');
  const zt = page.locator('.lern-zutun li:not(.zt-wunsch)'); // der Wunsch (I-2) wird in „I-2: Eltern-Startseite“ geprüft
  await zt.first().waitFor();
  assert.deepEqual(await zt.evaluateAll((ls) => ls.map((l) => l.className)), ['zt-rot', 'zt-rot', 'zt-gelb', 'zt-blau']);
  assert.deepEqual((await zt.allInnerTexts()).map((x) => x.replace('›', '').trim()), ['Kind B: kein Lerntag in den letzten 4 Wochen', 'Kind B: Rückreise Pisa (Wiederholung nach nicht bestandenem Nachtest)',
    'Kind A: „Runden“ wackelt (5 falsch)', 'Neue Antwort auf euren Auftrag: Rom – Natürliche Zahlen']);
  assert.deepEqual(await zt.locator('a').evaluateAll((as) => as.map((a) => a.getAttribute('href'))), ['#/kind/2-ueberblick', '#/kind/2-plan', '#/kind/1-wackelt-1.runden', '#/lernauftraege']);
  // Tabelle: Kind B rot (0 Lerntage), Kind A grün
  const b = page.locator('.lern-kinder-tabelle tbody tr', { hasText: 'Kind B' });
  assert.match(await b.locator('td').nth(0).getAttribute('class'), /amp-rot/);
  assert.match(await page.locator('.lern-kinder-tabelle tbody tr', { hasText: 'Kind A' }).locator('td').nth(0).innerText(), /2 Lerntage diese Woche · zuletzt heute/);
  assert.equal(await b.locator('td').nth(1).innerText(), 'Rückreise');
  assert.deepEqual(await page.locator('.lern-kinder-tabelle thead th').allInnerTexts().then((x) => x.slice(0, 7)), ['KIND', 'LERNT', 'WACKELT', 'GYM', 'RS', 'IB', 'JETZT']);
  // ohne Rollen: Zu tun und Tabelle auf dem Tablet sichtbar
  const unten = await page.locator('.lern-kinder-tabelle').boundingBox();
  assert.ok(unten.y + unten.height <= 1180, 'Tabelle ohne Rollen sichtbar: ' + Math.round(unten.y + unten.height));
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/la2-start-820.png') });
  await page.setViewportSize({ width: 1280, height: 800 }); await page.screenshot({ path: path.join(root, 'test-results/la2-start-1280.png'), fullPage: true });
  await page.setViewportSize({ width: 400, height: 860 });
  await page.locator('.lern-kind-karte', { hasText: 'Kind B' }).waitFor();
  assert.equal(await page.locator('.lern-kinder-tabelle').isVisible(), false, 'Handy: Karten statt Tabelle');
  await page.screenshot({ path: path.join(root, 'test-results/la2-start-400.png'), fullPage: true });
  // Zeile antippen → Überblick des Kindes
  await page.setViewportSize({ width: 820, height: 1180 });
  await b.locator('td').nth(2).click();
  await page.waitForURL(/#\/kind\/2-ueberblick$/);
  await page.locator('.lern-frage.amp-rot', { hasText: 'Lernt es?' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/la1-ueberblick-820.png'), fullPage: true });
  await page.setViewportSize({ width: 400, height: 860 }); await page.screenshot({ path: path.join(root, 'test-results/la1-ueberblick-400.png'), fullPage: true });
});

test('LA-2: „Alles ruhig.“, wenn nichts zu tun ist', async (t) => {
  const { page } = await setup(t, { anpassen: (aktion, e) => aktion === 'schule_eltern' ? { ...e, einloesungen: [] } : null }); // ohne offenen Wunsch (I-2)
  await laLage(page, { a: { einheiten: [] }, b: { lerntage: [tagVor(1)] } });
  await page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion === 'schule_rueckmeldungen') return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, rueckmeldungen: [] } }) }); return route.fallback(); });
  await page.goto(origin + '/#/lernen');
  await page.locator('.lern-zutun').getByText('Alles ruhig.').waitFor();
});

test('LA-6: ⚙ Einstellen – Blatt aus der Zeile und vom Kopf; Schule, Stand messen gegen …, Notizen, Vorlage; Esc schließt', async (t) => {
  const mitStufen = (aktion, e) => { if (aktion !== 'schule_plan_lesen') return null; const x = structuredClone(e); x.kind.stufen = {}; x.kind.schulart = 'gym_by';
    x.notizen = [{ von: 'eltern:Mama', text: 'Prüfung am 3.12.', am: '2026-11-10T08:00:00Z' }]; x.verlauf = [{ am: '2026-11-10T08:00:00Z', akteur: 'eltern:Mama', anlass: 'plan' }]; return x; };
  const { page, calls } = await setup(t, { anpassen: mitStufen });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lernen');
  await page.locator('.lern-kinder-tabelle tr', { hasText: 'Kind A' }).getByRole('button', { name: 'Kind A einstellen' }).click();
  const blatt = page.getByRole('dialog', { name: 'Kind A einstellen' });
  await blatt.getByRole('heading', { name: 'Schule' }).waitFor();
  assert.equal(await page.locator('.lern-einstellen').first().innerText(), '⚙ Einstellen', 'Zahnrad mit Text');
  assert.deepEqual(await blatt.locator('h3, summary b').allInnerTexts(), ['Schule', 'Stand messen gegen …', 'Reisetage und Pausen', 'Notizen und Verlauf (1)', 'Neuer Plan aus Lehrplan-Vorlage']);
  await blatt.getByText('Bestimmt seine Klasse in Lernreise und Plan.').waitFor();
  await blatt.getByText('Nur für die Anzeige „Wo steht es?“ – ändert nichts an der Lernreise.', { exact: false }).waitFor();
  assert.equal(await blatt.getByRole('combobox', { name: 'Stufe IB MYP' }).locator('option').first().innerText(), 'aus Klasse (noch kein MYP-Jahr)');
  assert.equal(await blatt.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: '5', exact: true }).getAttribute('aria-pressed'), 'true');
  await page.screenshot({ path: path.join(root, 'test-results/la6-blatt-820.png') });
  // Schulart wechseln speichert sofort
  await blatt.getByRole('group', { name: 'Hauptschulart' }).getByRole('button', { name: 'Realschule' }).click();
  await blatt.locator('[role=status]', { hasText: 'Gespeichert' }).first().waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_kind_setzen').at(-1).daten, { lernender_id: 1, schulart: 'rs_by' });
  await blatt.getByRole('combobox', { name: 'Stufe Gymnasium' }).selectOption('6');
  await page.waitForFunction(() => document.querySelectorAll('.lern-blatt [role=status]')[1]?.textContent === 'Gespeichert');
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_kind_setzen').at(-1).daten, { lernender_id: 1, stufen: { gym_by: 6, rs_by: null, ib_myp: null } });
  // Notizen und Verlauf zugeklappt
  assert.equal(await blatt.getByText('Prüfung am 3.12.').isVisible(), false);
  await blatt.getByText('Notizen und Verlauf (1)').click();
  await blatt.getByText('Prüfung am 3.12.').waitFor(); await blatt.getByText('Plan geändert', { exact: false }).waitFor();
  await page.keyboard.press('Escape');
  await blatt.waitFor({ state: 'detached' });
  // vom Kopf der Kind-Seite; auf dem Handy von unten
  await page.setViewportSize({ width: 400, height: 860 });
  await page.goto(origin + '/#/kind/1-plan');
  await page.locator('.lern-kind-kopf').getByRole('button', { name: 'Kind A einstellen' }).click();
  await page.getByRole('dialog').getByRole('heading', { name: 'Schule' }).waitFor();
  const b = await page.locator('.lern-blatt').boundingBox(); assert.ok(b.y > 50 && Math.round(b.y + b.height) >= 859, 'Handy: Blatt von unten');
  await page.screenshot({ path: path.join(root, 'test-results/la6-blatt-400.png') });
  // Plan-Seite hat keine Klasse, Stufen, Notizen, Vorlage mehr
  await page.getByRole('dialog').getByRole('button', { name: 'Schließen' }).click();
  for (const x of ['.lp-kindform', '.lern-plan-spalten ~ .lern-vorlage', 'textarea[aria-label="Notiz"]']) assert.equal(await page.locator('#main ' + x).count(), 0, x);
});

test('LA-3: Was wackelt – häufigster Fehler (erst ab 2), Kurz gesagt, „Besprochen ✓“ nimmt die Etappe aus „Zu tun“; von der Startseite mit einem Tipp', async (t) => {
  const { page, calls } = await setup(t, { anpassen: laUebersicht });
  await laLage(page);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lernen');
  // ein Tipp: gelber Eintrag öffnet die Etappe aufgeklappt
  await page.locator('.lern-zutun .zt-gelb a').click();
  await page.waitForURL(/#\/kind\/1-wackelt-1\.runden$/);
  const det = page.locator('.ls-detail');
  await det.getByText('Antwort: 929 000').waitFor();
  await det.getByText('Kurz gesagt: Ab 5 wird aufgerundet.').waitFor();
  const zeilen = page.locator('.ls-tabelle tbody tr.ls-zeile');
  assert.equal(await zeilen.nth(0).locator('td').nth(1).innerText(), 'falsch gerundet (2×)');
  assert.equal(await zeilen.nth(1).locator('td').nth(1).innerText(), '–', 'nur eine Antwort mit grund → „–“');
  await page.screenshot({ path: path.join(root, 'test-results/la3-wackelt-820.png'), fullPage: true });
  await det.getByRole('button', { name: 'Besprochen ✓' }).click();
  await zeilen.nth(0).getByText(/^besprochen \d/).waitFor();
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_notiz_setzen').at(-1).daten, { lernender_id: 1, besprochen: { einheit_id: 1, lernziel: 'runden' } });
  await page.setViewportSize({ width: 400, height: 860 }); await page.screenshot({ path: path.join(root, 'test-results/la3-wackelt-400.png'), fullPage: true });
});

test('LA-3: besprochene Etappe steht nicht in „Zu tun“, bleibt aber in der Tabelle', async (t) => {
  const { page } = await setup(t);
  await laLage(page, { runden: { besprochen_am: new Date().toISOString() } });
  await page.goto(origin + '/#/lernen'); await page.locator('.lern-zutun').waitFor();
  assert.equal(await page.locator('.lern-zutun .zt-gelb').count(), 0);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/kind/1-wackelt'); await page.locator('.ls-tabelle').getByText(/besprochen \d/).waitFor();
});

// LA-4/LA-5: Plan mit „kann schon“ je Flug (Datenbank nach Migration la_4) und einem geschafften Ort
const laPlan = ({ romFertig = false } = {}) => (aktion, e) => {
  const x = structuredClone(e);
  if (aktion === 'schule_plan_lesen') { x.plan = x.plan.map((r) => ({ ...r, ausgelassen: [], kann_schon_themen: [] })); if (romFertig) x.plan[0].status = 'fertig';
    for (const o of x.orte) for (const t of o.themen) t.kann_schon = false; return x; }
  if (aktion === 'schule_lernstand') { x.einheiten[0].karten = x.einheiten[0].karten.map((k, i) => ({ ...k, sitzt: true, sitzt_am: `2026-11-1${i}T08:00:00Z`, wdh_in: 3 - i })); return x; }
  if (aktion === 'schule_merkheft') { x.einheiten[0].nachtest = { grund: 'noch_nicht_faellig', lerntage_noetig: 10, lerntage_seit: 4 }; return x; }
  return null;
};

test('LA-4: Plan zweispaltig auf dem Tablet; „kann schon“ je Flug speichert; Lehrplan rechts mit Reitern, Klassen-Knöpfen und Abdeckung', async (t) => {
  const { page, calls } = await setup(t, { anpassen: laPlan() });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/kind/1-plan');
  const liste = page.locator('ol.lern-plan'); const lp = page.locator('.lern-plan-lehrplan');
  await lp.waitFor();
  const [a, b] = [await liste.boundingBox(), await lp.boundingBox()];
  assert.ok(b.x > a.x + a.width - 5 && Math.abs(b.y - a.y) < 40, 'zwei Spalten ab 700 px');
  assert.match((await page.locator('.lern-plan-kopf').textContent()).replace(/\s+/g, ' '), /Gymnasium Kl\. 5 · 1 ▶ · 2 ○ · 0 ↻ · 0 ◉/); // LB-5: Flüge je Stufe
  // LB-1: Lehrplan nach Klasse – vorbelegt Gymnasium, Klasse 5; eine Zeile je Thema mit Stufe
  await nachKlasse(page);
  assert.match(await lp.getByRole('group', { name: 'Klasse' }).locator('[aria-pressed=true]').innerText(), /^Kl\. 5\s*Kind$/);
  await lp.getByText('Gym 5: 2 von 3 Themen im Plan oder schon gekonnt').waitFor();
  assert.deepEqual(await lp.locator('.lern-plan-klasse .lern-lp-zeile .lern-lp-titel b').allInnerTexts(), ['Natürliche Zahlen und Stellenwertsysteme', 'Ganze Zahlen', 'Teilbarkeit und Primzahlen']);
  await lp.locator('.lern-lp-zeile', { hasText: 'Teilbarkeit' }).locator('.lern-st-wort', { hasText: 'Nicht im Plan' }).waitFor();
  await lp.locator('.lern-lp-zeile', { hasText: 'Teilbarkeit' }).locator('.lern-lp-titel').click();
  await lp.getByRole('button', { name: 'Teilbarkeit und Primzahlen: In den Plan nehmen' }).waitFor(); // LB Teil 8
  await lp.getByRole('group', { name: 'Schulart' }).getByRole('button', { name: 'IB MYP' }).click();
  assert.equal(await lp.getByRole('group', { name: 'Klasse' }).locator('[aria-pressed=true]').innerText(), 'MYP-Jahr 1', 'Klasse 5: noch kein MYP-Jahr → MYP-Jahr 1');
  // Rom aufklappen: „Ganze Zahlen“ kann er komplett (LB-2: Knopf statt Häkchen)
  const rom = page.locator('.lern-plan-zeile', { hasText: 'Rom' });
  await rom.locator('.lern-plan-ort').click();
  await rom.getByRole('button', { name: 'Ganze Zahlen: Kann er komplett' }).click();
  await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen').at(-1).daten.eintraege[0], { block_id: 49, kann_schon: false, ausgelassen: [], kann_schon_themen: [16] });
  await rom.locator('li', { hasText: 'Ganze Zahlen' }).locator('.lern-plan-flug-stand', { hasText: 'Kann er komplett' }).waitFor();
  assert.equal(await rom.getByRole('button', { name: 'Ganze Zahlen: Kann er komplett' }).getAttribute('aria-pressed'), 'true');
  assert.match(await rom.locator('.lern-plan-ort small').first().innerText(), /1\/2 Flüge/);
  await page.screenshot({ path: path.join(root, 'test-results/la4-plan-820.png'), fullPage: true });
  await page.setViewportSize({ width: 1280, height: 800 }); await page.screenshot({ path: path.join(root, 'test-results/la4-plan-1280.png'), fullPage: true });
  await page.setViewportSize({ width: 400, height: 860 }); await page.screenshot({ path: path.join(root, 'test-results/la4-plan-400.png'), fullPage: true });
});

test('LA-4: Flug einer höheren Klasse im Ort trägt den Hinweis; „kann schon“ je Flug zählt im Stand als gelandet (eigener Zustand)', async (t) => {
  const { page } = await setup(t, { anpassen: laPlan() });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/kind/1-plan');
  const delhi = page.getByRole('button', { name: '+ Delhi – Ungleichungen' }); // im Lehrplan unter „Algebra“
  await gebietWaehlen(page, 'Algebra');
  await delhi.click(); await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
  const z = page.locator('.lern-plan-zeile', { hasText: 'Delhi' }); await z.locator('.lern-plan-ort').click();
  await z.getByText('Gym 8 – höhere Klasse', { exact: false }).waitFor();
  const r = await page.evaluate(() => {
    const u = { einheiten: [], orte: [], themen: [{ thema_id: 16, titel: 'Ganze Zahlen', jahrgang: { gym_by: 5 }, block_id: 49, stadt: 'Rom', kontinent: 'Zahlen' }, { thema_id: 15, titel: 'Natürliche', jahrgang: { gym_by: 5 }, block_id: 49, stadt: 'Rom', kontinent: 'Zahlen' }],
      lernende: [{ id: 1, klasse: 5, schulart: 'gym_by', route: [{ block_id: 49, position: 1, art: 'normal', status: 'offen', kann_schon: false, ausgelassen: [], kann_schon_themen: [16] }], stand: [] }] };
    const m = lernStandModell(u, u.lernende[0]); return [m.zahl('gym_by', 5).f, m.themen.find((t) => t.thema_id === 16).kannSchon, m.themen.find((t) => t.thema_id === 15).st];
  });
  assert.deepEqual(r, [1, true, 'offen']);
});

test('LA-5: geschaffter Ort steht nicht im Plan, sondern zugeklappt unter „Geschafft (n)“ mit gelandet am, Nachtest, nächster Wiederholung', async (t) => {
  const { page } = await setup(t, { anpassen: laPlan({ romFertig: true }) });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/kind/1-plan');
  await page.locator('.lern-plan-zeile').first().waitFor();
  assert.deepEqual(await page.locator('ol.lern-plan > .lern-plan-zeile .lern-plan-ort b').allInnerTexts(), ['Geld – Einfache Zinsen'], 'nur offene Orte oben');
  // LB-5: der gelandete Ort steht unter „↻ In Wiederholung“ (ersetzt „Geschafft“), mit gelandet am, Nachtest und nächster Wiederholung je Flug
  const w = page.locator('.lern-plan-wdh');
  assert.match(await w.locator('.lern-plan-gruppe').textContent(), /In Wiederholung · 1 Ort · 2 Flüge in Wiederholung/);
  const romZ = w.locator('.lern-plan-zeile', { hasText: 'Rom' }); await romZ.locator('.lern-plan-ort').click();
  const zeile = romZ.locator('.lern-plan-themen li').first();
  assert.match(await zeile.locator('.lern-plan-flug-stand').innerText(), /In Wiederholung · .* · gelandet 12\.11\. · Nachtest in 6 Lerntagen · nächste Wiederholung in 1 Lerntag/);
  assert.equal(await page.locator('details.lern-geschafft').count(), 0, 'kein Block „Geschafft“ mehr');
  await page.screenshot({ path: path.join(root, 'test-results/la5-geschafft-820.png'), fullPage: true });
  // Überblick: zuletzt geschafft
  await page.getByRole('link', { name: 'Überblick', exact: true }).click();
  await page.locator('.lern-geschafft-kurz li').first().waitFor();
});

// ---------- Bau-Auftrag I, Teil 1 (20.11.): Mängel aus der Nachprüfung Lehrer-Aufbau ----------
const ohneQuerrollen = (page) => page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1);
const abgeschnitten = (loc) => loc.evaluateAll((xs) => xs.filter((x) => x.scrollWidth > x.clientWidth + 1).map((x) => x.textContent.trim()));

test('I-1: „Was wackelt“ auf dem Handy (400 px) – je Etappe eine Karte, nichts abgeschnitten, Reiterband vollständig', async (t) => {
  const { page } = await setup(t, { anpassen: laUebersicht });
  await laLage(page);
  await page.setViewportSize({ width: 400, height: 860 });
  await page.goto(origin + '/#/kind/1-wackelt');
  const karten = page.locator('.ls-karte-m'); await karten.first().waitFor();
  assert.equal(await page.locator('.ls-tabelle').isVisible(), false, 'unter 560 px keine Tabelle');
  assert.deepEqual(await karten.locator('.ls-karte-kopf b').allInnerTexts(), ['Runden', 'Welchen Wert hat eine Ziffer?'], 'wackelt zuerst');
  assert.deepEqual(await karten.first().locator('.ls-karte-werte span').allInnerTexts(), ['richtig / falsch: 2 / 5', 'häufigster Fehler: falsch gerundet (2×)', `seit: ${await page.evaluate(() => new Date().toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' }))}`]);
  assert.ok(await ohneQuerrollen(page), 'kein Querrollen');
  // Reiterband: alle vier Reiter ganz im Bild
  const rechts = await page.locator('.lern-reiter a').evaluateAll((as) => as.map((a) => Math.round(a.getBoundingClientRect().right)));
  assert.ok(Math.max(...rechts) <= 400, 'Reiter abgeschnitten: ' + rechts);
  assert.deepEqual(await abgeschnitten(page.locator('.lern-reiter a, .ls-karte-kopf b, .ls-karte-werte span')), []);
  // keine Trennung mitten im Wort: jede Kopfzeile so breit wie ihr längstes Wort
  const zuSchmal = await karten.locator('.ls-karte-kopf b').evaluateAll((bs) => bs.filter((b) => { const r = document.createRange(); r.selectNodeContents(b);
    return [...r.getClientRects()].some((q) => q.width < 20 && b.textContent.length > 3); }).length);
  assert.equal(zuSchmal, 0);
  await karten.first().locator('.ls-karte-kopf').click();
  await karten.first().getByText('Antwort: 929 000').waitFor();
  await karten.first().getByText('Kurz gesagt: Ab 5 wird aufgerundet.').waitFor();
  await karten.first().getByRole('button', { name: 'Besprochen ✓' }).waitFor();
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/i1-wackelt-400.png'), fullPage: true });
});

test('I-2: Eltern-Startseite – Wunsch als blauer Eintrag in „Zu tun“; Kinder-Tabelle auf dem Rechner (1280 × 800) ohne Rollen', async (t) => {
  const { page, calls } = await setup(t, { anpassen: laUebersicht });
  await laLage(page);
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.goto(origin + '/#/lernen');
  const w = page.locator('.lern-zutun li.zt-blau.zt-wunsch');
  await w.getByText('Kind A möchte „Eis“ einlösen (300 Sterne)').waitFor();
  assert.equal(await page.getByText('WARTET AUF DICH').count(), 0);
  assert.deepEqual(await page.locator('.lern-zutun li').evaluateAll((ls) => ls.map((l) => l.className.split(' ')[0])), ['zt-rot', 'zt-rot', 'zt-gelb', 'zt-blau', 'zt-blau']);
  const b = await page.locator('.lern-kinder-tabelle').boundingBox();
  await page.screenshot({ path: path.join(root, 'test-results/i2-eltern-1280.png') });
  assert.ok(b.y + b.height <= 800, 'Tabelle ohne Rollen: Unterkante ' + Math.round(b.y + b.height));
  await w.getByRole('button', { name: 'Bestätigen' }).click();
  for (let i = 0; i < 40 && !calls.some((c) => c.aktion === 'schule_einloesung_entscheiden'); i++) await page.waitForTimeout(50);
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_einloesung_entscheiden').daten, { id: 9, status: 'bestaetigt' });
});

test('I-4/I-6: Reisewörter beim ersten Vorkommen erklärt; Überblick „Keine Etappe wackelt · Rückreise … offen“', async (t) => {
  const { page } = await setup(t, { anpassen: laUebersicht });
  await laLage(page);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lernen');
  await page.locator('.lern-zutun').getByText('(Wiederholung nach nicht bestandenem Nachtest)').waitFor();
  await page.goto(origin + '/#/kind/2-ueberblick');
  const hakt = page.locator('.lern-frage', { hasText: 'Wo hakt es?' });
  assert.equal((await hakt.locator('p').first().innerText()).replace(/\s+/g, ' '), 'Keine Etappe (Lernschritt) wackelt · Rückreise Pisa offen');
  assert.equal(await page.getByText('Nichts wackelt.').count(), 0);
  await hakt.getByText('(Rückreise = Wiederholung nach nicht bestandenem Nachtest)').waitFor();
  await page.goto(origin + '/#/kind/1-ueberblick');
  await page.locator('.lern-frage', { hasText: 'Lernt es?' }).getByText('(Aufgabe)').waitFor();
  await page.locator('.lern-frage', { hasText: 'Was kommt?' }).getByText('(Thema)').waitFor();
  await page.goto(origin + '/#/kind/1-wackelt');
  await page.locator('.ls-tabelle thead').getByText('(Lernschritt)').waitFor();
});

test('I-7/I-8/I-9: Geschafft „noch kein Inhalt“; Tabelle ohne Kopf „Aktionen“, ⚙-Zelle mit Zeilenlinie; Hinweis „über der Klasse“ ganz; kein „Datenbank“', async (t) => {
  const quelle = fs.readFileSync(path.join(root, 'lernen.js'), 'utf8');
  const texte = [...quelle.matchAll(/'[^'\n]*Datenbank[^'\n]*'|`[^`\n]*Datenbank[^`\n]*`/g)].map((m) => m[0]);
  assert.deepEqual(texte, [], 'Hinweise mit „Datenbank“');
  const { page } = await setup(t, { anpassen: laUebersicht });
  await laLage(page);
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/lernen');
  const tab = page.locator('.lern-kinder-tabelle'); await tab.waitFor();
  assert.equal((await tab.locator('thead th').last().innerText()).trim(), '');
  const linie = await tab.locator('tbody tr').first().evaluate((tr) => [...tr.children].map((c) => Math.round(c.getBoundingClientRect().bottom)));
  assert.equal(new Set(linie).size, 1, 'alle Zellen enden auf derselben Zeilenlinie: ' + linie);
  await page.screenshot({ path: path.join(root, 'test-results/i8-start-820.png') });
});

test('I-7: Geschafft – Flug ohne Inhalt als „noch kein Inhalt“', async (t) => {
  const { page } = await setup(t, { anpassen: laPlan({ romFertig: true }) });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/kind/1-plan');
  const g = page.locator('.lern-plan-wdh .lern-plan-zeile', { hasText: 'Rom' }); await g.locator('.lern-plan-ort').click();
  const ohne = g.locator('.lern-plan-themen li').filter({ hasNot: page.locator('a') }).filter({ hasText: 'noch kein Inhalt' });
  assert.ok(await ohne.count() >= 1, 'mindestens ein Flug ohne Inhalt');
  assert.doesNotMatch(await ohne.first().innerText(), /gelandet: –/);
});

test('I-8: Plan – Hinweis „über der Klasse des Kindes“ auf dem Tablet nicht abgeschnitten', async (t) => {
  const { page } = await setup(t, { anpassen: laPlan() });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/kind/1-plan');
  await gebietWaehlen(page, 'Algebra');
  await page.getByRole('button', { name: '+ Delhi – Ungleichungen' }).click();
  const u = page.locator('.lern-plan-ueber').first(); await u.waitFor();
  assert.match(await u.innerText(), /über der Klasse des Kindes · Kind sieht ihn unter „Später“/);
  assert.deepEqual(await abgeschnitten(page.locator('.lern-plan-ueber')), []);
});

// I-10: Reisetage und Pausen
const tagAls = (iso) => new Date(iso + 'T00:00:00').toLocaleDateString('de-DE', { day: 'numeric', month: 'numeric' });
test('I-10: Startseite – „Pause bis …“ statt rot, kein „kein Lerntag“ in Zu tun; „+ Reisetag eintragen“ für alle Kinder', async (t) => {
  const { page, calls } = await setup(t, { anpassen: laUebersicht });
  await laLage(page, { a: { pausen: [] }, b: { pausen: [{ id: 5, von: tagVor(1), bis: tagVor(-3), grund: 'Reisetag', wer: 'lehrer:Herr Lehrer', am: new Date().toISOString() }] } });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/lernen');
  const zeileB = page.locator('.lern-kinder-tabelle tr', { hasText: 'Kind B' }); await zeileB.waitFor();
  const lernt = zeileB.locator('td.amp-pause');
  assert.equal(await lernt.innerText(), `Pause bis ${tagAls(tagVor(-3))} (Reisetag)`);
  assert.equal(await zeileB.locator('td').first().getAttribute('class'), 'amp-pause', 'Lernt: Pause statt rot');
  const zuTun = await page.locator('.lern-zutun li').allInnerTexts();
  assert.ok(!zuTun.some((x) => /Kind B.*Lerntag/.test(x)), 'kein „kein Lerntag“ für Kind B: ' + zuTun);
  assert.ok(zuTun.some((x) => /Kind B.*Pisa/.test(x)), 'Rückreise bleibt');
  // kurzer Weg: für alle Kinder
  await page.getByRole('button', { name: '+ Reisetag eintragen' }).click();
  const blatt = page.getByRole('dialog', { name: 'Reisetag eintragen' });
  assert.equal(await blatt.getByRole('combobox', { name: 'Für wen' }).inputValue(), 'alle');
  await blatt.getByLabel('bis').fill(tagVor(-2));
  await blatt.getByRole('button', { name: 'krank' }).click();
  await blatt.getByRole('button', { name: 'Eintragen' }).click();
  await blatt.waitFor({ state: 'detached' });
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_notiz_setzen').at(-1).daten, { alle: true, pause: { von: tagVor(0), bis: tagVor(-2), grund: 'krank' } });
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/i10-start-1280.png') });
});

test('I-10: vergangene Pause zählt nicht für „seit … kein Lerntag“ – grün statt rot', async (t) => {
  const { page } = await setup(t, { anpassen: laUebersicht });
  await laLage(page, { a: { lerntage: [tagVor(5)], pausen: [{ id: 6, von: tagVor(4), bis: tagVor(1), grund: null, wer: 'eltern:App' }] } });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/lernen');
  const zeileA = page.locator('.lern-kinder-tabelle tr', { hasText: 'Kind A' }); await zeileA.waitFor();
  assert.equal(await zeileA.locator('td.amp-gruen', { hasText: 'zuletzt' }).count(), 1, 'nur 1 Tag ohne Pause → grün');
  assert.ok(!(await page.locator('.lern-zutun li').allInnerTexts()).some((x) => /Kind A.*Lerntag/.test(x)));
});

test('I-10: ⚙ Einstellen – Reisetage eintragen, ändern, löschen; vergangene bleiben sichtbar', async (t) => {
  const { page, calls } = await setup(t, { anpassen: laUebersicht });
  await laLage(page, { a: { pausen: [{ id: 7, von: tagVor(-5), bis: tagVor(-8), grund: 'Ferien', wer: 'eltern:Mama' }, { id: 6, von: tagVor(12), bis: tagVor(10), grund: 'krank', wer: 'eltern:App' }] } });
  await page.setViewportSize({ width: 400, height: 860 });
  await page.goto(origin + '/#/kind/1-ueberblick');
  await page.locator('.lern-kind-kopf').getByRole('button', { name: /einstellen$/ }).click();
  const karte = page.locator('.lern-pause'); await karte.getByRole('heading', { name: 'Reisetage und Pausen' }).waitFor();
  const eintraege = karte.locator('.lern-pause-liste li'); await eintraege.first().waitFor();
  assert.equal(await eintraege.count(), 2);
  assert.match(await eintraege.nth(1).innerText(), /krank · vorbei/);
  assert.equal(await eintraege.nth(1).evaluate((li) => li.classList.contains('vorbei')), true);
  // eintragen (nur dieses Kind)
  await karte.locator('.lern-pause-form').first().getByRole('button', { name: 'Reisetag' }).click();
  await karte.locator('.lern-pause-form').first().getByRole('button', { name: 'Eintragen' }).click();
  await page.waitForFunction(() => document.querySelector('.lern-pause .lern-pause-liste'));
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_notiz_setzen').at(-1).daten, { lernender_id: 1, pause: { von: tagVor(0), bis: tagVor(0), grund: 'Reisetag' } });
  // ändern
  await karte.locator('.lern-pause-liste li').first().getByRole('button', { name: 'Ändern' }).click();
  const f2 = karte.locator('.lern-pause-liste li').first().locator('.lern-pause-form');
  await f2.getByLabel('bis').fill(tagVor(-9));
  await f2.getByRole('button', { name: 'Ändern' }).click();
  await page.waitForFunction(() => document.querySelectorAll('.lern-pause .lern-pause-liste .lern-pause-form').length === 0);
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_notiz_setzen').at(-1).daten, { pause: { von: tagVor(-5), bis: tagVor(-9), grund: 'Ferien', id: 7 } });
  // löschen
  await karte.locator('.lern-pause-liste li').nth(1).getByRole('button', { name: /löschen$/ }).click();
  await page.waitForFunction(() => true);
  await page.waitForTimeout(200);
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_notiz_setzen').at(-1).daten, { pause: { id: 6, loeschen: true } });
  assert.ok(await ohneQuerrollen(page));
  await page.screenshot({ path: path.join(root, 'test-results/i10-einstellen-400.png'), fullPage: true });
});

// ---------- Teil 1b – LA-8: Lehrplan nach Themengebiet (Flugplan rechts), Überschrift „Themengebiet – Thema“, Farbe je Gymnasium-Klasse ----------
const la8Orte = (aktion, e) => { if (aktion !== 'schule_plan_lesen') return null; const x = structuredClone(e); x.kind.schulart = 'gym_by';
  x.orte.push({ block_id: 70, titel: 'Wurzeln', stadt: 'Kyoto', kontinent: 'Zahlen', reihenfolge: 9, themen: [{ thema_id: 90, titel: 'Elementare Wurzeln', jahrgang: { gym_by: 9, rs_by: 9, ib_myp: 4 }, stand: 'keine_einheit', einheit: null },
      { thema_id: 91, titel: 'Reelle Zahlen', jahrgang: { gym_by: 9, rs_by: 9, ib_myp: 4 }, stand: 'keine_einheit', einheit: null }, { thema_id: 92, titel: 'Rationale Exponenten', jahrgang: { gym_by: 10, rs_by: 10 }, stand: 'keine_einheit', einheit: null }] },
    { block_id: 71, titel: 'Brüche', stadt: 'Pisa', kontinent: 'Zahlen', reihenfolge: 5, themen: [{ thema_id: 93, titel: 'Brüche und Anteile', jahrgang: { gym_by: 6, rs_by: 6, ib_myp: 1 }, stand: 'keine_einheit', einheit: null, lehrplan_reihenfolge: { gym_by: 1 } }] },
    { block_id: 72, titel: 'Zusatz', stadt: 'Lissabon', kontinent: 'Zahlen', reihenfolge: 12, themen: [{ thema_id: 94, titel: 'Prozentrechnung im Alltag', jahrgang: { rs_by: 7 }, stand: 'keine_einheit', einheit: null }] });
  return x; };
const kontrast = (a, b) => { const L = ([r, g, bl]) => { const f = (c) => { c /= 255; return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(bl); };
  const [h, d] = [L(a), L(b)].sort((x, y) => y - x); return (h + 0.05) / (d + 0.05); };
const farbeLesen = (page, loc, prop) => loc.evaluateAll((xs, pr) => xs.map((x) => { const c = document.createElement('canvas').getContext('2d'); c.fillStyle = '#000'; c.fillStyle = getComputedStyle(x)[pr];
  c.fillRect(0, 0, 1, 1); return [...c.getImageData(0, 0, 1, 1).data].slice(0, 3); }), prop);

test('LA-8: Flugplan rechts „Nach Themengebiet“ mit dem Gebiet des aktuellen Ortes; Überschriften „Themengebiet – Thema“ ohne Ortsnamen', async (t) => {
  const { page } = await setup(t, { anpassen: la8Orte });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/plan/1');
  const lp = page.locator('.lern-plan-lehrplan'); await lp.getByRole('group', { name: 'Ansicht' }).waitFor();
  assert.deepEqual(await lp.getByRole('group', { name: 'Ansicht' }).getByRole('button').allInnerTexts(), ['Nach Themengebiet', 'Nach Klasse (Lehrplan)']);
  assert.equal(await lp.getByRole('button', { name: 'Nach Themengebiet' }).getAttribute('aria-pressed'), 'true');
  assert.equal(await lp.getByRole('group', { name: 'Themengebiet' }).locator('[aria-pressed=true]').innerText(), 'Zahlen', 'Gebiet des aktuellen Ortes (Rom)');
  assert.equal(await lp.getByRole('group', { name: 'Sortiert nach Klasse in' }).locator('[aria-pressed=true]').innerText(), 'Gymnasium');
  // Überschriften links und rechts: kein Ortsname
  const staedte = ['Rom', 'Athen', 'New York', 'Delhi', 'Kyoto', 'Pisa', 'Lissabon'];
  const links = await page.locator('.lern-plan-zeile .lern-plan-ort > b').allInnerTexts();
  const rechts = await lp.locator('.lern-plan-vorrat-zeile .lern-plan-ort > b').allInnerTexts();
  assert.deepEqual(links, ['Zahlen – Natürliche Zahlen und Stellenwertsysteme und Ganze Zahlen', 'Geld – Einfache Zinsen']);
  for (const h of [...links, ...rechts]) assert.ok(!staedte.some((st) => h.includes(st)), 'Ortsname in Überschrift: ' + h);
  assert.match(await page.locator('.lern-plan-zeile').first().locator('.lern-plan-ort small').innerText(), /^▶ Gerade dran · Gym 5 · RS 5 · MYP 1 · 0\/2 Flüge · Ort in der Reise: Rom$/); // LB-2: Stufe vorn
  // Zahlen: alle Orte aus allen Klassen, leicht → schwer; Linie über Klasse 5; drei Flüge: die ersten zwei und „…“
  assert.deepEqual(rechts, ['Zahlen – Teilbarkeit und Primzahlen', 'Zahlen – Natürliche Zahlen und Stellenwertsysteme und Ganze Zahlen', 'Zahlen – Brüche und Anteile',
    'Zahlen – Elementare Wurzeln, Reelle Zahlen …', 'Zahlen – Prozentrechnung im Alltag']);
  assert.match(await lp.locator('.lern-plan-gebiet-kopf').innerText(), /^Zahlen: 1 von 5 Orten im Plan · von leicht nach schwer/);
  assert.equal(await lp.locator('.lern-plan-ab-hier').innerText(), 'AB HIER ÜBER KLASSE 5 DES KINDES');
  assert.equal(await lp.locator('.lern-plan-ab-hier + .lern-plan-vorrat-zeile .lern-plan-ort > b').innerText(), 'Zahlen – Brüche und Anteile');
  assert.match(await lp.locator('.lern-plan-drin').first().innerText(), /Gerade dran/); // LB-2: Stufe statt „✓ im Plan“
  assert.equal(await lp.locator('.lern-plan-vorrat-zeile', { hasText: 'Brüche' }).locator('small b').innerText(), 'Gym 6', 'gewählte Schulart fett');
  // Realschule: anders sortiert, Zusatz-Ort ohne Gymnasium-Klasse mit grauem „–“
  await lp.getByRole('group', { name: 'Sortiert nach Klasse in' }).getByRole('button', { name: 'Realschule' }).click();
  assert.equal(await lp.locator('.lern-plan-vorrat-zeile').nth(3).locator('.lern-plan-ort > b').innerText(), 'Zahlen – Prozentrechnung im Alltag');
  assert.equal(await lp.locator('.lern-plan-vorrat-zeile', { hasText: 'Prozentrechnung' }).locator('.lern-kl-kasten').innerText(), '–');
  // anderes Gebiet
  await lp.getByRole('group', { name: 'Themengebiet' }).getByRole('button', { name: 'Algebra' }).click();
  assert.deepEqual(await lp.locator('.lern-plan-vorrat-zeile .lern-plan-ort > b').allInnerTexts(), ['Algebra – Lineare Ungleichungen']);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await lp.getByRole('group', { name: 'Themengebiet' }).getByRole('button', { name: 'Zahlen' }).click();
  await lp.getByRole('group', { name: 'Sortiert nach Klasse in' }).getByRole('button', { name: 'Gymnasium' }).click();
  await page.screenshot({ path: path.join(root, 'test-results/la8-plan-1280.png'), fullPage: true });
});

test('LA-8: ein Gym-9-Thema mit einem Tipp in den Plan eines Klasse-5-Kindes; „Nach Klasse (Lehrplan)“ bleibt', async (t) => {
  const { page, calls } = await setup(t, { anpassen: la8Orte });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/plan/1');
  const lp = page.locator('.lern-plan-lehrplan'); await lp.getByRole('group', { name: 'Themengebiet' }).waitFor();
  await lp.getByRole('button', { name: '+ Kyoto – Wurzeln' }).click();
  await page.waitForFunction(() => document.querySelector('.lern-plan-stand')?.textContent === 'Gespeichert');
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_plan_setzen').at(-1).daten.eintraege.map((x) => x.block_id), [49, 52, 70]);
  assert.match(await lp.locator('.lern-plan-vorrat-zeile', { hasText: 'Elementare Wurzeln' }).innerText(), /Kommt noch/);
  const neu = page.locator('.lern-plan-zeile').last();
  assert.equal(await neu.locator('.lern-plan-ort > b').innerText(), 'Zahlen – Elementare Wurzeln, Reelle Zahlen …');
  assert.match(await neu.innerText(), /Klasse 9 – über der Klasse des Kindes/);
  // Nach Klasse (Lehrplan): Schulart, Klasse, Abdeckung – mit den neuen Überschriften
  await lp.getByRole('button', { name: 'Nach Klasse (Lehrplan)' }).click();
  await lp.getByRole('group', { name: 'Schulart' }).waitFor();
  assert.equal(await lp.getByRole('group', { name: 'Themengebiet' }).count(), 0);
  assert.match(await lp.locator('.lern-plan-abdeckung').innerText(), /Gym 5: \d+ von \d+ Themen im Plan oder schon gekonnt/);
  assert.ok((await lp.locator('.lern-plan-klasse .lern-lp-zeile .lern-lp-titel b').allInnerTexts()).includes('Teilbarkeit und Primzahlen'));
  // Handy: Spalte unter dem Plan, nichts quer
  await lp.getByRole('button', { name: 'Nach Themengebiet' }).click();
  await page.setViewportSize({ width: 400, height: 860 });
  assert.ok(await ohneQuerrollen(page), 'kein Querrollen auf dem Handy');
  await page.screenshot({ path: path.join(root, 'test-results/la8-plan-400.png'), fullPage: true });
});

test('LA-8: Kästchen und Rand in der Farbe der Gymnasium-Klasse, links und rechts gleich; lesbar, auch bei dunkler Systemeinstellung', async (t) => {
  const { page } = await setup(t, { anpassen: la8Orte });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/plan/1');
  const lp = page.locator('.lern-plan-lehrplan'); await lp.getByRole('group', { name: 'Themengebiet' }).waitFor();
  const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));
  const erwartet = { 5: '#2E7D32', 6: '#0277BD', 7: '#6A1B9A', 8: '#C62828', 9: '#EF6C00', 10: '#455A64' };
  const zeilen = page.locator('.lern-plan-zeile, .lern-plan-vorrat .lern-plan-vorrat-zeile');
  const daten = await zeilen.evaluateAll((zs) => zs.map((z) => ({ kl: z.querySelector('.lern-kl-kasten').textContent, rand: getComputedStyle(z).borderLeftColor, kasten: getComputedStyle(z.querySelector('.lern-kl-kasten')).backgroundColor })));
  assert.ok(daten.length >= 6);
  for (const d of daten) {
    if (d.kl === '–') continue;
    const rgb = `rgb(${hex(erwartet[d.kl]).join(', ')})`;
    assert.equal(d.rand, rgb, `Rand Klasse ${d.kl}`); assert.equal(d.kasten, rgb, `Kästchen Klasse ${d.kl}`);
  }
  assert.deepEqual([...new Set(daten.map((d) => d.kl))].sort(), ['5', '6', '9', '–'].sort());
  await lp.locator('.lern-kl-legende > summary').click(); // LB Teil 5 K1: Legende aufklappen
  assert.deepEqual(await lp.locator('.lern-kl-legende .lern-kl-kasten').allInnerTexts(), ['5', '6', '7', '8', '9', '10', '–']);
  for (const schema of ['light', 'dark']) {
    await page.emulateMedia({ colorScheme: schema });
    const kaesten = page.locator('.lern-kl-legende .lern-kl-kasten:not(.ohne)');
    const vg = await farbeLesen(page, kaesten, 'color'); const hg = await farbeLesen(page, kaesten, 'backgroundColor');
    vg.forEach((v, i) => assert.ok(kontrast(v, hg[i]) >= 4.5, `${schema}: Kästchen ${i + 5} Kontrast ${kontrast(v, hg[i]).toFixed(2)}`));
    const flaeche = (await farbeLesen(page, lp, 'backgroundColor'))[0];
    const raender = await farbeLesen(page, page.locator('.lern-plan-zeile, .lern-plan-vorrat .lern-plan-vorrat-zeile'), 'borderLeftColor');
    // Der Eltern/Lehrer-Bereich bleibt auch bei dunkler Systemeinstellung hell. Rand ist Schmuck (die Klasse steht im Kästchen);
    // Vorgabe-Orange #EF6C00 liegt auf der hellen Fläche knapp unter 3 : 1 → mindestens 2,9
    raender.forEach((r) => assert.ok(kontrast(r, flaeche) >= 2.9, `${schema}: Rand Kontrast ${kontrast(r, flaeche).toFixed(2)} ${r} auf ${flaeche}`));
    if (schema === 'dark') await page.screenshot({ path: path.join(root, 'test-results/la8-plan-dunkel-1280.png') });
  }
});

// ---------- IB einheitlich beschriften (18.11.): MYP-Jahr = Klasse − 5, Hinweis „entspricht etwa Klasse 6–10“ ----------
test('IB: MYP-Jahr = Klasse − 5 überall gleich; Beschriftung „MYP-Jahr n“ mit Hinweis auf Klasse 6–10', async (t) => {
  const { page } = await setup(t, { anpassen: standAnpassen() });
  await page.goto(origin + '/#/lernen'); await page.locator('.lern-zutun').first().waitFor();
  const r = await page.evaluate(() => [lernStufe({ klasse: 5, schulart: 'gym_by' }, 'ib_myp'), lernStufe({ klasse: 8, schulart: 'gym_by' }, 'ib_myp'), lernStufe({ klasse: 10, schulart: 'rs_by' }, 'ib_myp'),
    lernStufe({ klasse: 8, schulart: 'gym_by', stufen: { ib_myp: 2 } }, 'ib_myp'), LERN_SYS[2].kl(1), LERN_SYS[2].kl(5), LERN_SYS[2].label(3), LERN_SYS[2].label(0)]);
  assert.deepEqual(r, [0, 3, 5, 2, 6, 10, 'MYP-Jahr 3', 'noch kein MYP-Jahr']); // LA Abweichung 6: unter Klasse 6 „noch kein MYP-Jahr“
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

// LB-3: „Kann er – aber wiederholen“ – kein Flug-Test, keine Nachtests; die Testseite sagt es dem Kind
test('LB-3: gesetzter Flug (wiederholen) – Testseite ohne Test, kein „Test starten“', async (t) => {
  const ohneTest = (aktion, e) => aktion === 'schule_einheit_lesen'
    ? { ...e, blocktest_fertig: false, ohne_test: true, nachtest: { faellig: false, grund: 'gesetzt' },
        etappen_stand: Object.fromEntries(ETAPPEN.map((x) => [x.lernziel, { fertig: true, sitzt: true, ziel: 2, serie: 0 }])) } : null;
  const { page, calls } = await setup(t, { anpassen: ohneTest });
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByText('Für diesen Flug gibt es keinen Test.', { exact: false }).waitFor();
  assert.equal(await page.getByRole('button', { name: /starten$/ }).count(), 0, 'kein Test-Knopf');
  assert.equal(calls.filter((c) => c.aktion === 'schule_test_starten').length, 0);
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
  await page.getByRole('link', { name: 'Test zu den neuen Etappen', exact: true }).waitFor(); // I-5: neutraler Text
  // ohne offene Pflicht-Etappe: kein Nachtragstest, alte Anzeige
  const zwei = await setup(t, { anpassen: mitStand(0) });
  await zwei.page.goto(origin + '/#/lerneinheit/1-1-test');
  await zwei.page.getByText('Gerade gibt es keinen Test. Üb weiter!').waitFor();
  assert.equal(await zwei.page.getByRole('heading', { name: 'Test zu den neuen Etappen' }).count(), 0);
});

// ---------- Bau-Auftrag I, Teil 4 (20.11.): Restpunkte des Gestalters aus Nachprüfung 2 ----------
// Ein Wort gilt als gebrochen, wenn es über zwei Zeilen läuft (zwei Rechtecke für denselben Wortbereich).
const gebrocheneWoerter = (loc) => loc.evaluateAll((els) => {
  const aus = [];
  for (const el of els) { if (!el.getClientRects().length) continue;
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let n = w.nextNode(); n; n = w.nextNode()) { const re = /\S+/g; let m;
      while ((m = re.exec(n.data))) { const r = document.createRange(); r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
        const zeilen = new Set([...r.getClientRects()].filter((x) => x.width > 0).map((x) => Math.round(x.top))); if (zeilen.size > 1) aus.push(m[0]); } } }
  return aus; });

test('Teil 4 Punkt 1+2: Umschalter auf dem Tablet und Plan-Überschriften auf dem Handy ohne gebrochene Wörter', async (t) => {
  const { page } = await setup(t, { anpassen: la8Orte });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/plan/1');
  const um = page.locator('.lern-plan-lehrplan [role=group][aria-label="Ansicht"] button, .lern-plan-lehrplan .lern-plan-umschalter button');
  await page.locator('.lern-plan-lehrplan').getByRole('group', { name: 'Themengebiet' }).waitFor();
  assert.ok(await um.count() >= 2, 'Umschalter da');
  assert.deepEqual(await gebrocheneWoerter(um), [], 'Umschalter 820');
  await page.setViewportSize({ width: 400, height: 860 });
  await page.locator('.lern-plan-zeile').first().waitFor();
  assert.deepEqual(await gebrocheneWoerter(page.locator('.lern-plan-gebiet-kopf, .lern-plan-vorrat-zeile .lern-plan-ort > b')), [], 'Überschriften 400');
  // LB Teil 6 N2: links höchstens zwei Zeilen, nichts seitlich abgeschnitten (lange Wörter mit Silbentrennung)
  for (const b of await page.locator('.lern-plan-zeile .lern-plan-ort > b').all()) assert.ok(await b.evaluate((x) => x.scrollWidth <= x.clientWidth + 1 && x.getBoundingClientRect().height <= 2.9 * parseFloat(getComputedStyle(x).fontSize)), await b.innerText());
  assert.ok(await ohneQuerrollen(page), 'kein Querrollen');
});

test('Teil 4 Punkt 4: Inhaltsstand zählt in fertigen Flügen nur aktive Bordkarten', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/lehrplan'); await page.getByRole('heading', { name: 'Mathe Klasse 5–10: was gelernt wird' }).waitFor();
  const r = await page.evaluate(() => [lernInhaltZustand({ einheit: { status: 'geprueft', karten: 3, aufgaben: 24, neu: 4 } }).text, lernInhaltZustand({ einheit: { status: 'entwurf', karten: 3, aufgaben: 24, neu: 24 } }).k]);
  assert.deepEqual(r, ['Fertig · 3 Etappen · 20 Bordkarten', 'pruefung']);
});

test('Teil 4 Punkt 5: nach dem Knobeln zurück auf den Landebildschirm; gelandete Etappe zeigt „Hier bist du fertig ✓“ mit dem nächsten Schritt', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mitBonus });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  for (let i = 0; i < 2; i++) {
    for (const z of ['2', '0', '0', '0']) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
    await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
    if (i === 0) { await page.getByText(/An Bord/).waitFor(); await page.getByRole('button', { name: 'Neue Bordkarte ›' }).click(); }
  }
  // a) Knobel (kommt von selbst, Punkt 5d) falsch beantwortet → „Weiter ›“ zum Landebildschirm
  await page.locator('.lr-knobel input').fill('7'); await page.locator('.lr-knobel').getByRole('button', { name: 'Prüfen' }).click();
  await page.locator('.lr-knobel-falsch').waitFor();
  await page.locator('.lr-ueben-flaeche').getByRole('button', { name: 'Weiter ›', exact: true }).click();
  await page.locator('.lr-abschluss-etappe').waitFor(); // AB-A: Abschluss-Ansicht der Etappe
  assert.equal(await page.locator('.lr-bordkarte').count(), 0);
  // b) zur nächsten Etappe und zurück auf die gelandete: fertig, großer Weiter-Knopf, „Trotzdem weiterüben“ klein
  await page.locator('.lr-abschluss-etappe .lr-ab-gross').click();
  if (await page.getByRole('button', { name: 'Jetzt du ›' }).count()) await page.getByRole('button', { name: 'Jetzt du ›' }).click(); // neue Etappe: erst die Erklärung
  await page.getByRole('button', { name: 'Vorige Etappe' }).click();
  const box = page.locator('.lr-fertig-hier'); await box.getByText('Hier bist du fertig ✓').waitFor();
  const weiter = box.locator('.lr-weiter-schritt'); assert.match(await weiter.innerText(), /^Nächste Etappe: .+ ›$/);
  assert.equal(await page.locator('.lr-bordkarte').count(), 0, 'erst der nächste Schritt');
  await box.getByRole('button', { name: 'Trotzdem weiterüben' }).click();
  await page.locator('.lr-bordkarte').waitFor();
  assert.ok(await page.locator('.lr-fertig-hier .lr-weiter-schritt').isVisible(), 'Weiter-Knopf bleibt über der Bordkarte');
  for (const z of ['2', '0', '0', '0']) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
  await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
  await page.locator('.lr-rueck').first().waitFor();
  assert.ok(await page.locator('.lr-fertig-hier .lr-weiter-schritt').isVisible(), 'auch nach einer weiteren Bordkarte');
  await page.screenshot({ path: path.join(root, 'test-results/teil4-fertig-390.png'), fullPage: true });
});

// ---------- Bau-Auftrag LB (20.11.): Lehrplan „Nach Klasse“, 4 Stufen, Plan als Cockpit ----------
const LB_G7 = [701, 702, 703, 704, 705, 706];
const lbPlan = () => { let schritt = 900; return (aktion, e) => {
  if (aktion === 'schule_plan_setzen') return { ...e, revision: 2 + (schritt - 900), schritt_id: ++schritt };
  if (aktion !== 'schule_plan_lesen') return null;
  const x = structuredClone(e); x.kind = { ...x.kind, klasse: 8, schulart: 'gym_by' }; x.kann_wdh = true; x.kann_abwaehlen = true;
  x.plan = x.plan.map((r) => ({ ...r, ausgelassen: [], kann_schon_themen: r.block_id === 49 ? [16] : [], kann_wdh_themen: [] }));
  for (const o of x.orte) for (const t of o.themen) { t.kann_schon = false; t.kann_wdh = false;
    t.stufe = t.thema_id === 16 ? { stufe: 'komplett', zeichen: '◉', gesetzt: 'komplett', im_plan: true, etappen: 3, begonnen: 0, gelandet: 3, sicher: 3 }
      : t.thema_id === 15 ? { stufe: 'dran', zeichen: '▶', gesetzt: null, im_plan: true, etappen: 4, begonnen: 2, gelandet: 1 }
        : { stufe: x.plan.some((r) => r.block_id === o.block_id) ? 'kommt' : 'nicht_im_plan', gesetzt: null, im_plan: x.plan.some((r) => r.block_id === o.block_id), etappen: 0, begonnen: 0 }; }
  x.orte.push({ block_id: 80, titel: 'Klasse 7', stadt: 'Lissabon', kontinent: 'Algebra', themen: LB_G7.map((id, i) => ({ thema_id: id, titel: `Gym-7-Flug ${i + 1}`, jahrgang: { gym_by: 7, rs_by: 7 },
    stand: 'keine_einheit', einheit: null, kann_schon: false, kann_wdh: false, stufe: { stufe: 'nicht_im_plan', gesetzt: null, im_plan: false } })) });
  return x; }; };
async function lbOeffnen(t, breite = 1280) {
  const r = await setup(t, { anpassen: lbPlan() });
  await r.page.setViewportSize({ width: breite, height: breite < 700 ? 860 : breite < 1100 ? 1180 : 900 });
  await r.page.goto(origin + '/#/plan/1');
  await r.page.locator('.lern-plan-kopf').getByText(/Gymnasium Kl\. 8/).waitFor();
  return r;
}
const lbKlasse7 = async (page) => {
  const lp = page.locator('.lern-plan-lehrplan');
  await lp.getByRole('button', { name: /Klasse/ }).first().click();
  await lp.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: /^Kl\. 7/ }).click();
  await lp.locator('.lern-lp-zeile', { hasText: 'Gym-7-Flug 6' }).waitFor();
  return lp;
};
const gespeichert = (page) => page.waitForFunction(() => /Gespeichert/.test(document.querySelector('.lern-plan-stand')?.textContent || ''));

test('LB-5: sechs Gym-7-Flüge mit einem Schritt auf „Kann er – aber wiederholen“ (Auswahlmodus, Sammelaktion)', async (t) => {
  const { page, calls } = await lbOeffnen(t);
  const kopf = async () => (await page.locator('.lern-plan-kopf').innerText()).replace(/\s+/g, ' ');
  assert.match(await kopf(), /Gymnasium Kl\. 8 · 1 ▶ · 1 ○ · 0 ↻ · 1 ◉/); // je Flug
  const lp = await lbKlasse7(page);
  await page.getByRole('button', { name: 'Auswählen' }).click();
  for (let i = 1; i <= 6; i++) await lp.getByRole('checkbox', { name: `Gym-7-Flug ${i} auswählen` }).check();
  const leiste = page.getByRole('region', { name: 'Sammelaktionen' });
  assert.match(await leiste.innerText(), /6 Flüge ausgewählt/);
  const vorher = calls.filter((c) => c.aktion === 'schule_plan_setzen').length;
  await leiste.getByRole('button', { name: 'Kann er – aber wiederholen' }).click();
  await gespeichert(page);
  const neu = calls.filter((c) => c.aktion === 'schule_plan_setzen').slice(vorher);
  assert.equal(neu.length, 1, 'ein Schritt');
  const e80 = neu[0].daten.eintraege.find((x) => x.block_id === 80);
  assert.deepEqual([...e80.kann_wdh_themen].sort(), LB_G7); assert.deepEqual(e80.ausgelassen, []);
  assert.match(await kopf(), /· 1 ▶ · 1 ○ · 6 ↻ · 1 ◉/);
  assert.equal(await lp.locator('.lern-lp-zeile .lern-st-wort', { hasText: 'In Wiederholung' }).count(), 6);
  await page.screenshot({ path: path.join(root, 'test-results/lb5-auswahl-1280.png'), fullPage: true });
});

test('LB-5: ◉-Flug „Wieder in die Wiederholung“; ↶ Rückgängig schickt den Schritt des Servers', async (t) => {
  const { page, calls } = await lbOeffnen(t);
  await page.locator('.lern-plan-zeile', { hasText: 'Rom' }).first().locator('.lern-plan-ort').click();
  await page.getByRole('button', { name: 'Ganze Zahlen: Wieder in die Wiederholung' }).first().click();
  await gespeichert(page);
  const s1 = calls.filter((c) => c.aktion === 'schule_plan_setzen').at(-1).daten;
  const e49 = s1.eintraege.find((x) => x.block_id === 49);
  assert.deepEqual(e49.wieder_wdh_themen, [16]); assert.deepEqual(e49.kann_wdh_themen, [16]); assert.deepEqual(e49.kann_schon_themen, []);
  await page.getByRole('button', { name: '↶ Rückgängig' }).click();
  await page.waitForFunction(() => /Rückgängig gemacht/.test(document.querySelector('.lern-plan-stand')?.textContent || ''));
  const s2 = calls.filter((c) => c.aktion === 'schule_plan_setzen').at(-1).daten;
  assert.equal(s2.rueckgaengig, 901); assert.deepEqual(s2.eintraege.find((x) => x.block_id === 49).kann_schon_themen, [16]);
  assert.equal(s2.eintraege.find((x) => x.block_id === 49).wieder_wdh_themen, undefined);
  // LB-3 Nachbesserung (Sollte 4): nur der jüngste Schritt – nach einem Rückgängig ist der Knopf aus
  assert.equal(await page.getByRole('button', { name: '↶ Rückgängig' }).isDisabled(), true);
});

test('LB-1/LB-5: alle Knöpfe im Plan erreichbar; 400/820/1280 ohne Querrollen und ohne gebrochene Wörter', async (t) => {
  for (const breite of [400, 820, 1280]) {
    const { page } = await lbOeffnen(t, breite);
    // links: Ort aufklappen → je Flug die Knöpfe
    await page.locator('.lern-plan-zeile').first().locator('.lern-plan-ort').click();
    const g = page.getByRole('group', { name: 'Einstellung für Natürliche Zahlen und Stellenwertsysteme' }).first();
    for (const k of ['Lernen', 'Kann er – aber wiederholen', 'Kann er komplett', 'Aus dem Plan nehmen'])
      assert.ok(await g.getByRole('button', { name: `Natürliche Zahlen und Stellenwertsysteme: ${k}` }).isVisible(), `${breite}: ${k}`);
    // rechts: Nach Klasse, Zeile aufklappen → „+ In den Plan“ und die anderen Knöpfe
    const lp = await lbKlasse7(page);
    await lp.locator('.lern-lp-zeile', { hasText: 'Gym-7-Flug 1' }).locator('.lern-lp-titel').click();
    for (const k of ['In den Plan nehmen', 'Lernen', 'Kann er – wiederholen', 'Kann er komplett']) // LB Teil 8: kompakte Stufen-Zeile
      await lp.getByRole('button', { name: `Gym-7-Flug 1: ${k}` }).waitFor();
    assert.ok(await ohneQuerrollen(page), `${breite}: kein Querrollen`);
    assert.deepEqual(await gebrocheneWoerter(page.locator('.lern-plan-kopf, .lern-st-knopf b, .lern-lp-titel b, .lern-plan-lehrplan .lern-chip, .lern-lp-detail')), [], `${breite}: gebrochene Wörter`);
    await page.screenshot({ path: path.join(root, `test-results/lb-plan-${breite}.png`), fullPage: true });
    await page.close();
  }
});


// ---------- Teil 4 Punkt 5 d–h (Fassung 20.11. später): Knobel hinten dran, Test folgt, Ergebnis deutlicher, Verbessern ----------
const nurStellenwertOffen = (aktion, e) => { if (aktion !== 'schule_einheit_lesen') return null; const x = structuredClone(e);
  x.etappen_stand = { stellenwert: { fertig: false, ziel: 2 }, strahl: { fertig: true, sitzt: true, ziel: 2, serie: 2 }, binomisch: { fertig: true, sitzt: true, ziel: 2, serie: 2 } }; return x; };
async function landeEtappe1(page) {
  for (let i = 0; i < 2; i++) {
    for (const z of ['2', '0', '0', '0']) await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: z, exact: true }).click();
    await page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
    if (i === 0) { await page.getByText(/An Bord/).waitFor(); await page.getByRole('button', { name: 'Neue Bordkarte ›' }).click(); }
  }
}

test('Teil 4 Punkt 5d: nach der Landung kommt die Knobel-Bordkarte von selbst, danach der Landebildschirm', async (t) => {
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: mitBonus });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  await landeEtappe1(page);
  await page.getByText('Zum Schluss eine harte Nuss – falsch kostet nichts.', { exact: false }).waitFor();
  await page.locator('.lr-knobel .lr-stufe-bonus').waitFor();
  assert.equal(await page.getByRole('button', { name: '★ Knobel-Bordkarte (freiwillig)' }).count(), 0, 'kein Angebot zur Auswahl');
  assert.equal(await page.getByRole('button', { name: 'Weiter ›' }).isVisible(), false, 'Weiter erst nach dem Prüfen');
  await page.getByRole('button', { name: 'Heute keine Knobel-Bordkarte' }).waitFor();
  await page.locator('.lr-knobel input').fill('7'); await page.locator('.lr-knobel').getByRole('button', { name: 'Prüfen' }).click();
  await page.locator('.lr-knobel-falsch').waitFor();
  assert.equal(calls.filter((c) => c.aktion === 'schule_uebung_pruefen' && c.daten.aufgabe_id === 501).length, 1);
  await page.getByRole('button', { name: 'Weiter ›' }).click();
  await page.locator('.lr-abschluss-etappe').waitFor(); // AB-A: Abschluss-Ansicht der Etappe
  assert.equal(await page.locator('.lr-bordkarte').count(), 0, 'nicht zurück in die Übungen');
  assert.equal(await page.getByRole('button', { name: '★ Knobel-Bordkarte (freiwillig)' }).count(), 0, 'kein zweiter Versuch');
});

test('Teil 4 Punkt 5d: „Heute keine Knobel-Bordkarte“ führt auf den Landebildschirm', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mitBonus });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  await landeEtappe1(page);
  await page.getByRole('button', { name: 'Heute keine Knobel-Bordkarte' }).click();
  await page.locator('.lr-abschluss-etappe').waitFor(); // AB-A: Abschluss-Ansicht der Etappe
});

test('Teil 4 Punkt 5e: nach der letzten Pflicht-Etappe nur „Jetzt zum Test“; Flug mit fehlendem Test öffnet die Test-Aufforderung', async (t) => {
  let alleFertig = false;
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: (aktion, e) => { const x = nurStellenwertOffen(aktion, e);
    if (x && alleFertig) x.etappen_stand.stellenwert = { fertig: true, sitzt: true, ziel: 2, serie: 2 }; return x; } });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  await landeEtappe1(page);
  const l = page.locator('.lr-abschluss-etappe'); await l.waitFor(); // AB-A: Abschluss-Ansicht, ein großer Knopf zum Flug-Test
  assert.equal(await l.locator('.lr-ab-gross').count(), 1, 'nur ein großer Knopf');
  assert.match((await l.locator('.lr-ab-gross').innerText()).replace(/\s+/g, ' '), /^Weiter: Flug-Test 3 Bordkarten, eine je Etappe, ohne Tipps ›$/);
  assert.equal(await l.getByText('Anschlussflug', { exact: false }).count(), 0);
  await l.getByRole('link', { name: 'Pause – zur Abflugtafel' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/teil4-test-folgt-390.png') });
  await l.locator('.lr-ab-gross').click();
  await page.waitForURL(/-test$/); await page.getByRole('button', { name: 'Test starten' }).waitFor();
  // Flug öffnen (alle Pflicht-Etappen gelandet, nur der Test fehlt): erst die Aufforderung, nicht die Übungen
  alleFertig = true;
  for (const ziel of ['#/lerneinheit/1-1', '#/lerneinheit/1-1-ueben']) {
    await page.goto(origin + '/' + ziel);
    await page.getByText('Alle Etappen sind gelandet ✓').waitFor();
    await page.getByRole('button', { name: 'Test starten' }).waitFor();
    assert.equal(await page.locator('.lr-bordkarte').count(), 0);
  }
  await page.getByRole('link', { name: '‹ Zu den Etappen' }).click();
  await page.waitForURL(/-erklaeren$/); await page.locator('.lr-tab, .lr-reiter, [role=tab]').first().waitFor();
});

test('Teil 4 Punkt 5f: Test-Ergebnis – richtig/falsch mit Fläche, ✓/✗ und Wort; Summe groß; Kontrast hell und nacht', async (t) => {
  for (const gestaltung of ['entdecker', 'nacht']) {
    const { page } = await setup(t, { gestaltung });
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(origin + '/#/lerneinheit/1-1-test');
    await page.getByRole('button', { name: 'Test starten' }).click();
    await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
    await page.getByRole('button', { name: 'Weiter ›' }).click();
    await page.getByRole('button', { name: 'Markierung 2' }).click();
    await page.getByRole('button', { name: 'Abgeben' }).click();
    await page.locator('.lern-ergebnis-summe').waitFor();
    assert.equal((await page.locator('.lern-ergebnis-summe').innerText()).replace(/\s+/g, ' ').trim(), '1 von 2 richtig');
    assert.ok(parseFloat(await page.locator('.lern-ergebnis-summe b').evaluate((x) => getComputedStyle(x).fontSize)) >= 30, 'Summe groß');
    const k = page.locator('.lern-rueck-karte');
    assert.deepEqual(await k.locator('.lern-rk-wort').allInnerTexts(), ['RICHTIG', 'FALSCH']);
    assert.deepEqual(await k.locator('.lern-rk-zeichen').allInnerTexts(), ['✓', '✗']);
    const m = await k.evaluateAll((els) => els.map((x) => { const c = getComputedStyle(x); const z = getComputedStyle(x.querySelector('.lern-rk-zeichen'));
      const lum = (s) => { const [r, g, b] = s.match(/\d+(\.\d+)?/g).slice(0, 3).map((v) => { v = v / 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
      const kon = (a, b) => { const [h, d] = [lum(a), lum(b)].sort((p, q) => q - p); return (h + 0.05) / (d + 0.05); };
      return { balken: parseFloat(c.borderLeftWidth), text: kon(c.color, c.backgroundColor), zeichen: kon(z.color, z.backgroundColor), flaeche: c.backgroundColor }; }));
    for (const x of m) { assert.ok(x.balken >= 8, `${gestaltung}: Balken ${x.balken}`); assert.ok(x.text >= 4.5, `${gestaltung}: Text ${x.text}`); assert.ok(x.zeichen >= 3, `${gestaltung}: Zeichen ${x.zeichen}`); }
    assert.notEqual(m[0].flaeche, m[1].flaeche, 'Flächen unterscheiden sich');
    await page.screenshot({ path: path.join(root, `test-results/teil4-ergebnis-${gestaltung}-390.png`), fullPage: true });
    await page.close();
  }
});

test('Teil 4 Punkt 5g: Ergebnis mit Fehler → „Gleich verbessern ›“ startet die Korrektur (hell und nacht)', async (t) => {
  for (const gestaltung of ['entdecker', 'nacht']) {
    const { page, calls } = await setup(t, { gestaltung });
    await page.goto(origin + '/#/lerneinheit/1-1-test');
    await page.getByRole('button', { name: 'Test starten' }).click();
    await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
    await page.getByRole('button', { name: 'Weiter ›' }).click();
    await page.getByRole('button', { name: 'Markierung 2' }).click();
    await page.getByRole('button', { name: 'Abgeben' }).click();
    const z = page.locator('.lr-test-knoepfe'); await z.waitFor();
    assert.match(await z.locator('.lr-knopf').first().innerText(), /^Erst üben: .+ ›$/);
    // kein Knopf/Link der Ergebnisseite zeigt auf die eigene Adresse
    const eigen = await page.evaluate(() => [...document.querySelectorAll('#main a[href]')].filter((a) => a.getAttribute('href') === location.hash).map((a) => a.textContent));
    assert.deepEqual(eigen, []);
    await z.getByRole('button', { name: 'Gleich verbessern ›' }).click();
    await page.getByText(/Verbessern · Bordkarte 1 von/).waitFor();
    assert.equal(calls.filter((c) => c.aktion === 'schule_test_starten').at(-1).daten.art, 'korrektur');
    await page.close();
  }
});

test('Teil 4 Punkt 5h: Korrektur vollständig richtig → Flug geschafft, kein „Verbessern“ (Stand wird neu geladen)', async (t) => {
  let abgeschlossen = false;
  const { page, calls } = await setup(t, { anpassen: (aktion, e) => {
    if (aktion === 'schule_einheit_lesen') { const x = structuredClone(e);
      if (abgeschlossen) { x.blocktest_fertig = true; x.stand = x.stand.map((s) => ({ ...s, status: 'korrigiert' })); }
      else { x.blocktest_fertig = true; x.stand = x.stand.map((s, i) => ({ ...s, status: i === 1 ? 'fehler' : 'nachgewiesen' })); }
      return x; }
    if (aktion === 'schule_test_abschliessen') { abgeschlossen = true; // wie im Betrieb: Antwort trägt noch den alten Stand
      return { ...e, richtig: 2, gesamt: 2, ergebnisse: e.ergebnisse.map((x) => ({ ...x, richtig: true })), einheit_abgeschlossen: false }; }
    return null; } });
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByRole('button', { name: 'Verbessern starten' }).click();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
  await page.getByRole('button', { name: 'Weiter ›' }).click();
  await page.getByRole('button', { name: 'Markierung 2' }).click();
  await page.getByRole('button', { name: 'Abgeben' }).click();
  await page.getByText('Flug geschafft! 🎉').waitFor();
  assert.equal(await page.getByRole('button', { name: /verbessern/i }).count(), 0);
  assert.equal(await page.getByText(/Erst üben/).count(), 0);
  await page.getByRole('link', { name: 'Weiter zum nächsten Flug ›' }).waitFor();
  assert.ok(calls.filter((c) => c.aktion === 'schule_einheit_lesen').length >= 2, 'Stand nach dem Test neu geladen');
});

// ---------- Bau-Auftrag LB, Teil 5 (20.11.): Mängel aus der Nachprüfung 3 – gemessen mit der echten Themenliste ----------
// Lehrstoff aus inhalte/themenliste.json (95 Flüge, echte Titel, Lernbereiche, Lehrplan-Bezüge); Lernstand eines erfundenen Gym-8-Kindes.
const THEMEN_ECHT = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themenliste.json'), 'utf8'));
const echteEtappen = (t) => { try { return (JSON.parse(fs.readFileSync(path.join(root, t.datei), 'utf8')).inhalt?.etappen || []).map((e) => ({ lernziel: e.lernziel, titel: e.titel })); } catch { return []; } };
function echtePlanDaten() {
  const GEB = ['Zahlen', 'Geld und Verhältnisse', 'Algebra', 'Funktionen', 'Geometrie', 'Fläche und Raum', 'Daten und Zufall', 'Entdecker-Inseln'];
  const st = (t) => { const g = t.klasse.gym_by; const n = Math.max(echteEtappen(t).length, 1);
    const s = (stufe, x = {}) => ({ stufe, zeichen: { komplett: '◉', wiederholung: '↻', dran: '▶', kommt: '○', nicht_im_plan: '+' }[stufe], gesetzt: null, im_plan: stufe !== 'nicht_im_plan', etappen: n, begonnen: 0, gelandet: 0, sicher: 0, ...x });
    if (!g || g > 8) return s('nicht_im_plan');
    if (g <= 6) return t.thema_id % 3 ? s('komplett', { gelandet: n, sicher: n }) : s('wiederholung', { gelandet: n, wdh_nr: 4, naechste_in: 9 });
    if (g === 7) return t.thema_id % 2 ? s('wiederholung', { gelandet: n, wdh_nr: 2, naechste_in: 3 }) : s('wiederholung', { gesetzt: 'wiederholen', gelandet: n, wdh_nr: 1, naechste_in: 1 });
    const r = t.reihenfolge.gym_by; return r === 4 ? s('dran', { begonnen: 4, gelandet: 3 }) : r < 4 ? s('wiederholung', { gelandet: n, wdh_nr: 2, naechste_in: 4 }) : s('kommt'); };
  const BL = new Map();
  for (const t of THEMEN_ECHT) { const b = BL.get(t.block_id) || { block_id: t.block_id, stadt: t.ort, titel: t.titel, kontinent: t.gebiet, reihenfolge: (GEB.indexOf(t.gebiet) + 1) * 100 + BL.size, themen: [] };
    const s = st(t); const et = echteEtappen(t);
    b.themen.push({ thema_id: t.thema_id, titel: t.titel, jahrgang: t.klasse, stand: ['komplett', 'wiederholung'].includes(s.stufe) ? 'erledigt' : s.stufe === 'dran' ? 'laeuft' : 'offen',
      kann_schon: false, kann_wdh: s.gesetzt === 'wiederholen', lehrplan_reihenfolge: t.reihenfolge, stufe: s, beschreibung: t.umfang, lernbereich: t.lernbereich,
      lehrplan: { gym_by: t.lehrplan_gym, rs_by: t.lehrplan_rs, ib_myp: t.lehrplan_ib }, etappen: et, einheit: { id: t.thema_id, status: 'geprueft', karten: et.length, aufgaben: 40, neu: 0 } });
    BL.set(t.block_id, b); }
  const ORTE = [...BL.values()].sort((a, b) => a.reihenfolge - b.reihenfolge);
  const PLAN = ORTE.filter((o) => o.themen.some((t) => t.stufe.im_plan));
  return { BL, ORTE, plan: PLAN.map((o, i) => ({ route_id: i + 1, block_id: o.block_id, position: i + 1, art: 'normal', status: 'offen', kann_schon: false,
    ausgelassen: o.themen.filter((t) => !t.stufe.im_plan).map((t) => t.thema_id), kann_schon_themen: [], kann_wdh_themen: o.themen.filter((t) => t.kann_wdh).map((t) => t.thema_id) })) };
}
const echtAnpassen = () => { const D = echtePlanDaten(); return (aktion, e) => {
  if (aktion === 'schule_plan_lesen') return { ok: true, kann_abwaehlen: true, kann_wdh: true, kind: { id: 1, name: 'Kind A', klasse: 8, schulart: 'gym_by' }, revision: 1, orte: structuredClone(D.ORTE), plan: structuredClone(D.plan), notizen: [], verlauf: [] };
  if (aktion === 'schule_plan_setzen') return { ok: true, revision: 2, schritt_id: 900 };
  if (aktion === 'schule_lehrplan_uebersicht') { const x = structuredClone(e); x.themen = THEMEN_ECHT.map((t) => { const y = D.BL.get(t.block_id).themen.find((q) => q.thema_id === t.thema_id);
    return { thema_id: t.thema_id, titel: t.titel, gebiet: t.gebiet, ort: t.ort, block_id: t.block_id, jahrgang: t.klasse, einheit: y.einheit, stand: { 1: y.stand }, geplant: y.stufe.im_plan ? [1] : [], rueckmeldungen: 0,
      lernbereich: t.lernbereich, lehrplan: y.lehrplan, lehrplan_reihenfolge: t.reihenfolge, stufe: { 1: y.stufe } }; }); return x; }
  return null; }; };
// Überlappung Titel ↔ Stufenwort und überlaufende Titel je Zeile
const ueberlappt = (loc) => loc.evaluateAll((els) => els.flatMap((k) => { const a = k.querySelector('.lern-lp-titel'), b = k.querySelector('.lern-st-wort'); if (!a || !b || !a.getClientRects().length) return [];
  const r = a.getBoundingClientRect(), q = b.getBoundingClientRect(); const ue = Math.max(0, Math.min(r.right, q.right) - Math.max(r.left, q.left)) * Math.max(0, Math.min(r.bottom, q.bottom) - Math.max(r.top, q.top));
  const zu = a.scrollWidth > a.clientWidth + 1 || [...a.querySelectorAll('b, small')].some((x) => x.scrollWidth > x.clientWidth + 1);
  return ue > 1 || zu ? [`${a.querySelector('b')?.textContent} (Überlappung ${Math.round(ue)} px², Titel ${a.scrollWidth}/${a.clientWidth} px)`] : []; }));

test('LB Teil 5 M1: „Nach Klasse“ mit allen echten Thementiteln – kein Wort getrennt, keine Überlappung (400/820/1280)', async (t) => {
  const laengste = {};
  for (const [breite, hoehe] of [[400, 860], [820, 1180], [1280, 900]]) {
    const { page } = await setup(t, { anpassen: echtAnpassen() });
    await page.setViewportSize({ width: breite, height: hoehe });
    await page.goto(origin + '/#/plan/1');
    const lp = page.locator('.lern-plan-lehrplan');
    await lp.getByRole('button', { name: /Klasse/ }).first().click();
    for (const sa of ['Gymnasium', 'Realschule', 'IB MYP']) {
      await lp.getByRole('group', { name: 'Schulart' }).getByRole('button', { name: sa }).click();
      const kl = lp.getByRole('group', { name: 'Klasse' }).getByRole('button');
      for (let i = 0; i < await kl.count(); i++) {
        await kl.nth(i).click(); const name = (await kl.nth(i).innerText()).replace(/\s+/g, ' ');
        const zeilen = lp.locator('.lern-lp-zeile'); const n = await zeilen.count(); if (!n) continue;
        const titel = await lp.locator('.lern-lp-titel b').allInnerTexts(); laengste[`${sa} ${name}`] = titel.sort((a, b) => b.length - a.length)[0];
        assert.deepEqual(await gebrocheneWoerter(lp.locator('.lern-lp-titel b, .lern-lp-titel small, .lern-lp-kopf .lern-st-wort, .lern-lp-lernbereich')), [], `${breite} ${sa} ${name}`);
        assert.deepEqual(await ueberlappt(lp.locator('.lern-lp-kopf')), [], `${breite} ${sa} ${name}: Überlappung`);
      }
    }
    // aufgeklappte Zeile mit Etappen (S4) und dem längsten Gym-Titel
    await lp.getByRole('group', { name: 'Schulart' }).getByRole('button', { name: 'Gymnasium' }).click();
    await lp.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: /^Kl\. 8/ }).click();
    await lp.locator('.lern-lp-zeile', { hasText: 'Lineare Ungleichungen' }).locator('.lern-lp-titel').click();
    assert.deepEqual(await gebrocheneWoerter(lp.locator('.lern-lp-detail')), [], `${breite}: Aufgeklappt`);
    assert.ok(await ohneQuerrollen(page), `${breite}: kein Querrollen`);
    await page.screenshot({ path: path.join(root, `test-results/lb5-klasse-gym8-${breite}.png`), fullPage: true });
    await page.close();
  }
  assert.ok(Object.keys(laengste).length >= 15, 'alle Klassen gemessen: ' + Object.keys(laengste).length);
  fs.writeFileSync(path.join(root, 'test-results/lb5-laengste-titel.json'), JSON.stringify(laengste, null, 1));
});

test('LB Teil 5 S4/K3/K4: Etappen mit Titel und Stand; IB-Lernbereich deutsch zuerst; „Lehrplan:“ ohne Bezug zeigt den Lernbereich', async (t) => {
  const { page } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/plan/1');
  const lp = page.locator('.lern-plan-lehrplan');
  await lp.getByRole('button', { name: /Klasse/ }).first().click();
  await lp.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: /^Kl\. 8/ }).click();
  await lp.locator('.lern-lp-zeile', { hasText: 'Lineare Ungleichungen' }).locator('.lern-lp-titel').click();
  // LB Teil 8: die Etappen-Kästchen (S4) entfallen; die Karte nennt die Zahl der Etappen am Knopf „Inhalte ansehen“
  assert.equal(await lp.locator('.lern-lp-detail .lern-st-etappe').count(), 0);
  assert.match(await lp.locator('.lern-lp-detail .lern-lp-inhalte').innerText(), /^Inhalte ansehen \(7 Etappen\)$/);
  // K4: Thema ohne Gym-Lehrplanbezug → Lernbereich
  const ohne = THEMEN_ECHT.find((x) => x.klasse.gym_by && !(x.lehrplan_gym || []).length && x.lernbereich?.gym_by);
  if (ohne) { await lp.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: new RegExp(`^Kl\\. ${ohne.klasse.gym_by}`) }).click();
    await lp.locator('.lern-lp-zeile', { hasText: ohne.titel }).first().locator('.lern-lp-titel').click();
    assert.match(await lp.locator('.lern-lp-detail').first().innerText(), new RegExp('Lehrplan: ' + ohne.lernbereich.gym_by.slice(0, 10).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'))); }
  // K3: IB-Lernbereiche deutsch zuerst
  assert.equal(await page.evaluate(() => lernLbText('MYP 3 Numerical and abstract reasoning (Zahl und Algebra)')), 'MYP 3 Zahl und Algebra (Numerical and abstract reasoning)');
  await lp.getByRole('group', { name: 'Schulart' }).getByRole('button', { name: 'IB MYP' }).click();
  for (const h of await lp.locator('.lern-lp-lernbereich').allInnerTexts()) assert.ok(!/^MYP \d+ [A-Z][a-z]+ (and|of) /.test(h), 'englisch zuerst: ' + h);
});

test('LB Teil 5 S1/S2/K1/K2: Auswahl kompakt, Abschnitte mit Orten und Flügen, Legende einzeilig, keine innere Bildlaufleiste', async (t) => {
  const { page, calls } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-lehrplan .lern-lp-zeile, .lern-plan-lehrplan .lern-plan-vorrat-zeile').first().waitFor();
  const hoeheVorher = await page.evaluate(() => document.documentElement.scrollHeight);
  // S2: gleiche Einheit
  for (const g of await page.locator('.lern-plan-gruppe').allInnerTexts()) assert.match(g.replace(/\s+/g, ' '), /· \d+ (ORTE?|Orte?) · \d+ (FLÜGE?|Flüge?|FLUG|Flug) /i, g); // LB Teil 6 N3: „1 Ort · 2 Flüge gerade dran“
  assert.match(await page.locator('.lern-plan-komplett summary').innerText(), /Kann er komplett · \d+ Orte? · \d+ (Flüge|Flug) komplett gekonnt/);
  // K1: Legende eine Zeile
  const leg = page.locator('.lern-plan-lehrplan .lern-kl-legende > summary');
  const zeilenLeg = await leg.evaluate((x) => { const m = [...x.children].map((c) => { const r = c.getBoundingClientRect(); return r.top + r.height / 2; }); return Math.max(...m) - Math.min(...m) < 8 ? 1 : 2; }); assert.equal(zeilenLeg, 1, 'Legende einzeilig');
  assert.equal(await page.locator('.lern-plan-lehrplan .lern-kl-legende').evaluate((d) => d.open), false, 'zugeklappt');
  // K2: keine innere Bildlaufleiste
  assert.equal(await page.locator('.lern-plan-lehrplan').evaluate((x) => x.scrollHeight > x.clientHeight + 1 && getComputedStyle(x).overflowY !== 'visible'), false);
  // S1
  await page.getByRole('button', { name: 'Auswählen' }).click();
  const hoehe = await page.evaluate(() => document.documentElement.scrollHeight);
  assert.ok(hoehe < hoeheVorher * 1.6, `Seite bleibt kompakt: ${hoeheVorher} → ${hoehe}`);
  assert.equal(await page.locator('.lern-plan-spalten .lern-st-knoepfe:visible').count(), 0, 'keine Flug-Knöpfe beim Auswählen');
  assert.equal(await page.getByText('alle Flüge: kann er komplett').count(), 0);
  const wdhKopf = page.locator('.lern-plan-wdh .lern-plan-gruppe');
  await wdhKopf.getByRole('checkbox', { name: /alle .* auswählen/ }).check();
  const leiste = page.getByRole('region', { name: 'Sammelaktionen' });
  const n = Number((await leiste.innerText()).match(/(\d+) Flüge? ausgewählt/)[1]); assert.ok(n >= 10, 'ganzer Abschnitt: ' + n);
  // Ort-Häkchen und „▸ einzeln“
  const ort = page.locator('ol.lern-plan .lern-plan-zeile').first();
  await ort.getByRole('button', { name: /einzeln auswählen/ }).click();
  assert.ok(await ort.locator('.lern-plan-flug-zeile input[type=checkbox]').count() >= 1, 'einzeln: Häkchen je Flug');
  assert.equal(await ort.locator('.lern-st-knoepfe').count(), 0);
  await ort.locator('> label input[type=checkbox], > .lern-st-wahl input').first().check();
  const vorher = calls.filter((c) => c.aktion === 'schule_plan_setzen').length;
  await leiste.getByRole('button', { name: 'Kann er – aber wiederholen' }).click();
  await page.waitForFunction(() => /Gespeichert/.test(document.querySelector('.lern-plan-stand')?.textContent || ''));
  assert.equal(calls.filter((c) => c.aktion === 'schule_plan_setzen').length - vorher, 1, 'ein Schritt');
  await page.screenshot({ path: path.join(root, 'test-results/lb5-auswahl-820.png'), fullPage: true });
});

test('LB Teil 5 S3 / LM-1: in der Matrix je Zelle die Lehrplan-Reihenfolge der gewählten Schulart; Lernbereich im Detail', async (t) => {
  const { page } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/lehrplan'); await page.getByRole('heading', { name: 'Mathe Klasse 5–10: was gelernt wird' }).waitFor();
  for (const [sa, n, key] of [['Gymnasium', 8, 'gym_by'], ['Realschule', 7, 'rs_by']]) {
    await page.getByRole('group', { name: 'Einordnen nach Schulart' }).getByRole('button', { name: sa }).click();
    const ids = (await page.locator('.mx-chip').evaluateAll((els) => els.map((x) => Number(x.dataset.id))));
    for (const g of new Set(THEMEN_ECHT.map((x) => x.gebiet))) {
      const soll = THEMEN_ECHT.filter((x) => x.klasse[key] === n && x.gebiet === g).sort((a, b) => (a.reihenfolge[key] || 999) - (b.reihenfolge[key] || 999)).map((x) => x.thema_id);
      assert.deepEqual(ids.filter((i) => soll.includes(i)), soll, `${sa} ${n} ${g}`);
    }
    const x = THEMEN_ECHT.find((y) => y.klasse[key] === n);
    await page.locator(`.mx-chip[data-id="${x.thema_id}"]`).click();
    assert.match(await page.locator('.mx-detail .mx-lb').innerText(), new RegExp(`Lernbereich: M${n} \\d`));
  }
});

// ---------- Bau-Auftrag AB-A (20.11.): Abschluss nach Etappe, Flug und Ort (Entwurf 2 des Gestalters) ----------
// Server-Felder wie AB-S (Meldung „FERTIG: AB-S“ in inhalte/postfach/bau-motivation.md); Inhalte erfunden.
const abLandung = (art, x = {}) => (aktion, e) => { if (aktion === 'schule_uebung_pruefen' && e.landung) return { ...e, landung: { ...e.landung, landung_art: art, kann: 'Ziffern nach ihrem Stellenwert lesen', ...x } }; return null; };
async function abLande(t, art, { gestaltung = 'nacht', breite = 400, hoehe = 780, x = {}, anpassen = null, bewegung = 'reduce' } = {}) {
  const { page, calls } = await setup(t, { gestaltung, anpassen: (a, e) => (anpassen && anpassen(a, e)) || abLandung(art, x)(a, e) });
  await page.emulateMedia({ reducedMotion: bewegung });
  await page.setViewportSize({ width: breite, height: hoehe });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText(/BORDKARTE 1 · ROM/).waitFor();
  await landeEtappe1(page);
  if (art !== 'sturm' && await page.getByRole('button', { name: 'Heute keine Knobel-Bordkarte' }).count()) await page.getByRole('button', { name: 'Heute keine Knobel-Bordkarte' }).click();
  await page.locator('.lr-abschluss-etappe').waitFor();
  return { page, calls };
}
const abPasst = (page) => page.evaluate(() => { const h = document.querySelector('.lr-abschluss'); const b = (h.querySelector('.lr-ab-blatt') || h.querySelector('.lr-ab-pause:last-child') || h.querySelector('.lr-ab-app')).getBoundingClientRect();
  return { scroll: h.scrollHeight > h.clientHeight + 1 || document.querySelector('.lr-ab-app').scrollHeight > document.querySelector('.lr-ab-app').clientHeight + 1, unten: Math.round(b.bottom), hoehe: innerHeight }; });

test('AB-A 1: Etappe gelandet – drei Fassungen, je eigene Szene; 400 × 780 ohne Scrollen, hell und nacht; genau ein großer Knopf', async (t) => {
  const hinter = {};
  for (const art of ['direkt', 'sauber', 'sturm']) for (const g of ['tag', 'nacht']) {
    const { page } = await abLande(t, art, { gestaltung: g, x: art === 'sturm' ? { bordkarten: 15, fehler_endgueltig: 6, stufe_gesenkt: 2 } : art === 'sauber' ? { bordkarten: 8, eigene_loesungen: 6 } : { bordkarten: 2 } });
    const v = page.locator('.lr-abschluss-etappe');
    assert.equal(await v.getAttribute('data-art'), art);
    assert.equal(await page.locator('.lr-abschluss').count(), 1, 'genau eine Fassung');
    const titel = { direkt: 'DIREKTFLUG', sauber: 'SAUBERE LANDUNG', sturm: 'STURMFLUG GEMEISTERT' }[art];
    assert.equal((await v.locator('.lr-ab-titel').innerText()).trim(), titel);
    hinter[art] = await v.locator('.lr-ab-szene').evaluate((x) => getComputedStyle(x).backgroundImage);
    const p = await abPasst(page); assert.ok(!p.scroll && p.unten <= p.hoehe, `${art}/${g}: ohne Scrollen (${JSON.stringify(p)})`);
    assert.equal(await v.locator('.lr-ab-gross').count(), 1, 'genau ein großer Knopf');
    assert.equal(await page.evaluate(() => [...document.querySelectorAll('.lr-abschluss a[href]')].filter((a) => /-ueben/.test(a.getAttribute('href'))).length), 0, 'kein Weg zurück in die Übungen');
    assert.match(page.url(), /#\/lerneinheit\/1-1-erklaeren$/, 'Zurück führt nicht in die Bordkarten');
    assert.match(await v.locator('.lr-ab-kann').innerText(), /Du kannst jetzt\s*Ziffern nach ihrem Stellenwert lesen\./i);
    assert.match((await v.locator('.lr-ab-gross').innerText()).replace(/\s+/g, ' '), /^Weiter: .+ Etappe 2 von 3 ›$/);
    await v.getByRole('link', { name: 'Pause – zur Abflugtafel' }).waitFor();
    if (art === 'direkt') { assert.match(await v.locator('.lr-ab-riesig').innerText(), /^2\/2\s*AUF ANHIEB$/); assert.equal((await v.locator('.lr-ab-abz span').innerText()).trim(), 'ABZEICHEN'); }
    if (art === 'sauber') assert.deepEqual(await v.locator('.lr-ab-chips span').allInnerTexts(), ['8 Bordkarten', '6 selbst gelöst', '2 in Folge']);
    if (art === 'sturm') { // 1c: keine Fehlerzahl, keine Knobel-Bordkarte von selbst (nur als kleiner Textlink)
      assert.equal(await v.locator('.lr-ab-unter').innerText(), '15 Bordkarten, zweimal neu angesetzt – und nicht abgedreht. Am Ende 2 in Folge richtig.');
      assert.ok(!/\b6\b|Fehler/.test(await page.locator('.lr-abschluss').innerText()), 'keine Fehlerzahl');
      await v.getByText('⚡ AUSDAUER-ABZEICHEN').waitFor();
      assert.equal(await page.locator('.lr-knobel').count(), 0, 'keine Knobel-Bordkarte von selbst');
    }
    const blatt = await v.locator('.lr-ab-blatt').evaluate((x) => getComputedStyle(x).backgroundColor);
    assert.equal(blatt, g === 'nacht' ? 'rgb(18, 24, 49)' : 'rgb(255, 255, 255)', 'Blatt folgt der Gestaltung');
    await page.screenshot({ path: path.join(root, `test-results/ab-etappe-${art}-${g}-400.png`) });
    await page.close();
  }
  assert.equal(new Set(Object.values(hinter)).size, 3, 'drei verschiedene Szenen');
});

test('AB-A 1: Sturmflug – Knobel nur über den Textlink, danach wieder die Abschluss-Ansicht; Wieder gelandet; ohne AB-S-Server „sauber“', async (t) => {
  const { page } = await abLande(t, 'sturm', { anpassen: mitBonus });
  assert.equal(await page.locator('.lr-knobel').count(), 0, 'nicht von selbst');
  await page.getByRole('button', { name: 'Knobel-Bordkarte (freiwillig)' }).click();
  await page.locator('.lr-knobel input').fill('7'); await page.locator('.lr-knobel').getByRole('button', { name: 'Prüfen' }).click();
  await page.getByRole('button', { name: 'Weiter ›' }).click();
  await page.locator('.lr-abschluss-etappe[data-art="sturm"]').waitFor();
  await page.close();
  const w = await abLande(t, 'sauber', { x: { wieder_gelandet: true } });
  assert.equal((await w.page.locator('.lr-ab-titel').innerText()).trim(), 'WIEDER GELANDET');
  await w.page.close();
  const alt = await abLande(t, 'sauber', { anpassen: (a, e) => (a === 'schule_uebung_pruefen' && e.landung ? (({ landung, ...x }) => x)(e) : null) });
  assert.equal(await alt.page.locator('.lr-abschluss-etappe').getAttribute('data-art'), 'sauber');
});

test('AB-A 1: Abzeichen im Reisepass gezählt; Tablet 820', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: (a, e) => { if (a !== 'schule_konto') return null; const x = structuredClone(e); x.konto.abzeichen = { direkt: 4, sauber: 9, sturm: 3 }; return x; } });
  await page.goto(origin + '/#/reisepass/1');
  assert.equal((await page.locator('.lr-abzeichen').innerText()).replace(/\s+/g, ' ').trim(), '⚡ Direkt 4 · ✓ Sauber 9 · ⚡ Ausdauer 3');
  await page.close();
  for (const art of ['direkt', 'sauber', 'sturm']) {
    const r = await abLande(t, art, { gestaltung: 'tag', breite: 820, hoehe: 1180 });
    const p = await abPasst(r.page); assert.ok(!p.scroll, `${art}: Tablet ohne Scrollen`);
    await r.page.screenshot({ path: path.join(root, `test-results/ab-etappe-${art}-tag-820.png`) });
    await r.page.close();
  }
});

test('AB-A 4: Bewegung höchstens 1,8 s, Antippen beendet sie, „weniger Bewegung“ zeigt sofort den Endzustand', async (t) => {
  const { page } = await abLande(t, 'direkt', { bewegung: 'no-preference' });
  const dauer = await page.evaluate(() => Math.max(0, ...document.querySelector('.lr-abschluss').getAnimations({ subtree: true }).map((a) => { const z = a.effect.getComputedTiming(); return (z.delay || 0) + (z.duration || 0); })));
  assert.ok(dauer > 0 && dauer <= 1800, 'Dauer ' + dauer);
  await page.locator('.lr-ab-szene').click({ position: { x: 20, y: 200 } });
  assert.equal(await page.evaluate(() => document.querySelector('.lr-abschluss').getAnimations({ subtree: true }).length), 0, 'Antippen beendet die Bewegung');
  await page.close();
  const ruhig = await abLande(t, 'sturm', { bewegung: 'reduce' });
  assert.equal(await ruhig.page.evaluate(() => document.querySelector('.lr-abschluss').getAnimations({ subtree: true }).length), 0);
  assert.equal(await ruhig.page.locator('.lr-ab-blatt').evaluate((x) => getComputedStyle(x).opacity), '1');
});

// Flug-Test bestanden (AB-S-Felder)
const abFlug = ({ ortGeschafft = false, naechster = 'gleich', flugGeschafft } = {}) => (aktion, e) => {
  if (aktion === 'schule_test_abschliessen') {
    const nf = naechster === null ? null : { thema_id: 7, einheit_id: 2, titel: 'Ganze Zahlen', gebiet: 'Zahlen', kurz: 'Zahlen unter null: ordnen, Betrag und Rechnen mit Vorzeichen.',
      block_id: naechster === 'anders' ? 52 : 49, ort: naechster === 'anders' ? 'Athen' : 'Rom', flug: { nr: naechster === 'anders' ? 1 : 2, von: naechster === 'anders' ? 1 : 4 }, etappen: 9, erste_etappe: { lernziel: 'lesen', titel: 'Große Zahlen lesen' } };
    return { ...e, richtig: 2, gesamt: 2, ergebnisse: e.ergebnisse.map((x) => ({ ...x, richtig: true })), lernziele: e.lernziele.map((x) => ({ ...x, status: 'nachgewiesen' })), einheit_abgeschlossen: true, ort: { abgeschlossen: ortGeschafft },
      sterne_flug: { test: 40, summe: 820 }, kurz: 'Du lernst große Zahlen lesen und schreiben.', etappen: [{ lernziel: 'stellenwert', titel: 'Stellenwert', kann: 'Ziffern nach ihrem Stellenwert lesen' }, { lernziel: 'strahl', titel: 'Zahlenstrahl', kann: null }, { lernziel: 'binomisch', titel: 'Binomisch', kann: 'Werte am Zahlenstrahl ablesen' }],
      flug: { thema_id: 1, einheit_id: 1, titel: 'Natürliche Zahlen', gebiet: 'Zahlen', ort: 'Rom', block_id: 49, flug: { nr: 1, von: 4 }, etappen: 3 },
      ort_geschafft: ortGeschafft, ort_sterne: ortGeschafft ? 100 : 0, ort_fluege: ortGeschafft ? [{ thema_id: 1, titel: 'Natürliche Zahlen', zustand: 'erledigt' }, { thema_id: 2, titel: 'Ganze Zahlen', zustand: 'erledigt' }] : [],
      naechster_flug: nf, ort_wechsel: nf ? nf.ort !== 'Rom' : null, ...(flugGeschafft !== undefined ? { flug_geschafft: flugGeschafft } : {}) }; // 0.83.1: ohne Angabe wie alter Server
  }
  if (aktion === 'schule_einheit_lesen' && e.einheit_id === 2) return { ...e, einheit_id: 2 };
  return null;
};
async function abTest(t, opt = {}, { gestaltung = 'nacht', breite = 400, hoehe = 780 } = {}) {
  const { page, calls } = await setup(t, { gestaltung, anpassen: abFlug(opt) });
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.setViewportSize({ width: breite, height: hoehe });
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByRole('button', { name: 'Test starten' }).click();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
  await page.getByRole('button', { name: 'Weiter ›' }).click();
  await page.getByRole('button', { name: 'Markierung 2' }).click();
  await page.getByRole('button', { name: 'Abgeben' }).click();
  await page.locator('.lr-abschluss-flug').waitFor();
  return { page, calls };
}

test('AB-A 2: Flug geschafft → Bordkarte zum nächsten Thema; Boarding öffnet die Erklärung der ersten Etappe; Antwortliste nur über „Test ansehen“', async (t) => {
  for (const g of ['tag', 'nacht']) {
    const { page } = await abTest(t, {}, { gestaltung: g });
    const f = page.locator('.lr-abschluss-flug');
    assert.equal((await f.locator('.lr-ab-titel').innerText()).trim(), 'FLUG GESCHAFFT');
    assert.equal(await f.locator('.lr-ab-oben').innerText(), 'ROM · FLUG 1 VON 4 · NATÜRLICHE ZAHLEN');
    assert.equal(await f.locator('.lr-ab-ringe i').count(), 3, 'je Etappe ein Licht');
    assert.match((await f.locator('.lr-ab-zaehler').innerText()).replace(/\s+/g, ' '), /^820 ★ Sterne in diesem Flug · Test 2 von 2$/);
    assert.deepEqual(await f.locator('.lr-ab-kannliste div').allInnerTexts(), ['Ziffern nach ihrem Stellenwert lesen', 'Zahlenstrahl', 'Werte am Zahlenstrahl ablesen']);
    assert.match(await f.locator('.lr-ab-wdh').innerText(), /nach 1 Lerntag\s*3\s*7\s*14\s*30/);
    assert.equal(await f.locator('.lr-ab-gross').count(), 1);
    const p = await abPasst(page); assert.ok(!p.scroll && p.unten <= p.hoehe, `${g}: Flug ohne Scrollen ${JSON.stringify(p)}`);
    assert.ok(!(await page.locator('.lern-rueck-karte').first().isVisible()) || (await page.locator('.lr-abschluss').isVisible()), 'Antwortliste verdeckt');
    await page.screenshot({ path: path.join(root, `test-results/ab-flug-${g}-400.png`) });
    if (g === 'tag') { // Test ansehen → Antwortliste
      await f.getByRole('button', { name: 'Test ansehen' }).click();
      assert.equal(await page.locator('.lr-abschluss').count(), 0); await page.locator('.lern-rueck-karte').first().waitFor();
      await page.close(); continue;
    }
    await f.getByRole('button', { name: /Weiter zum nächsten Thema/ }).click();
    const k = page.locator('.lr-abschluss-bordkarte'); await k.waitFor();
    assert.equal(await k.locator('.lr-ab-oben').innerText(), 'NEUES THEMA');
    assert.match((await k.locator('.lr-ab-route').innerText()).replace(/\s+/g, ' '), /ORT ROM ✈ FLUG 2 \/ 4/);
    assert.equal(await k.locator('.lr-ab-flugname b').innerText(), 'Ganze Zahlen');
    assert.match((await k.locator('.lr-ab-felder').innerText()).replace(/\s+/g, ' '), /ETAPPEN 9 GEBIET Zahlen FLUG 2 von 4/);
    const b = k.locator('.lr-ab-gross'); assert.match((await b.innerText()).replace(/\s+/g, ' '), /^Boarding: Ganze Zahlen Zuerst kommt die Erklärung ›$/);
    assert.equal(await b.getAttribute('href'), '#/lerneinheit/1-2-erklaeren-1');
    await k.getByRole('link', { name: 'Später – zur Abflugtafel' }).waitFor();
    const p2 = await abPasst(page); assert.ok(p2.unten <= p2.hoehe, 'Bordkarte passt');
    await page.screenshot({ path: path.join(root, `test-results/ab-bordkarte-${g}-400.png`) });
    await b.click(); await page.waitForURL(/1-2-erklaeren-1$/);
    await page.locator('.lr-abschluss').waitFor({ state: 'detached', timeout: 3000 }); // Teil 9 (Nachprüfung Abschluss N4): die App schließt die Ansicht wenige ms nach dem Adresswechsel
    assert.equal(await page.locator('.lr-abschluss').count(), 0, 'Ansicht geschlossen');
    await page.close();
  }
});

test('AB-A 3: Ort geschafft → Reisepass-Stempel → Bordkarte VON → NACH; Überspringen; ohne nächsten Flug „Alles geschafft“', async (t) => {
  const { page } = await abTest(t, { ortGeschafft: true, naechster: 'anders' });
  await page.locator('.lr-abschluss-flug').getByRole('button', { name: 'Überspringen ›' }).click();
  const o = page.locator('.lr-abschluss-ort'); await o.waitFor();
  assert.match(await o.locator('.lr-ab-passstempel').innerText(), /GESCHAFFT\s*ROM\s*Zahlen · \d\d\.\d\d\./);
  assert.equal(await o.locator('.lr-ab-titel').innerText(), 'ROM IST GESCHAFFT');
  assert.equal(await o.locator('.lr-ab-unter').innerText(), 'Alle 2 Flüge · ★ +100 Ort-Sterne');
  assert.deepEqual(await o.locator('.lr-ab-kannliste div').allInnerTexts(), ['Natürliche Zahlen', 'Ganze Zahlen']);
  assert.match((await o.locator('.lr-ab-gross').innerText()).replace(/\s+/g, ' '), /^Weiter: neuer Ort Deine Bordkarte nach Athen ›$/);
  assert.match(await o.locator('.lr-ab-oben').innerText(), /^REISEPASS · STEMPEL \d+$/);
  const p = await abPasst(page); assert.ok(!p.scroll && p.unten <= p.hoehe, 'Ort ohne Scrollen');
  await page.screenshot({ path: path.join(root, 'test-results/ab-ort-nacht-400.png') });
  await o.locator('.lr-ab-gross').click();
  const k = page.locator('.lr-abschluss-bordkarte'); await k.waitFor();
  assert.equal(await k.locator('.lr-ab-oben').innerText(), 'NEUES THEMA · NEUER ORT');
  assert.match((await k.locator('.lr-ab-route').innerText()).replace(/\s+/g, ' '), /VON ROM ✈ NACH ATHEN/);
  assert.match(await k.locator('.lr-ab-gross').innerText(), /^Abflug nach Athen/);
  await page.screenshot({ path: path.join(root, 'test-results/ab-bordkarte-ort-nacht-400.png') });
  await page.close();
  const leer = await abTest(t, { naechster: null }, { gestaltung: 'tag', breite: 820, hoehe: 1180 });
  await leer.page.screenshot({ path: path.join(root, 'test-results/ab-flug-tag-820.png') });
  await leer.page.locator('.lr-abschluss-flug .lr-ab-gross').click();
  const kl = leer.page.locator('.lr-abschluss-bordkarte'); await kl.getByText('Alles geschafft, was im Plan steht. Deine Eltern legen fest, wie es weitergeht.').waitFor();
  assert.equal(await kl.locator('.lr-ab-gross').getAttribute('href'), '#/reise/1');
});

// ---------- LB Teil 6 (Nachprüfung 4 des Gestalters) ----------
// N1 (Muss): „Nach Themengebiet“ mit allen echten Titeln – maschinell gezählt 0 gebrochene Wörter bei 400, 820, 1280 in allen Gebieten (Wörter mit Bindestrich zählen nicht, wie in der Nachprüfung).
test('LB Teil 6 N1: „Nach Themengebiet“ – kein gebrochenes Wort bei 400, 820, 1280 in allen Gebieten; N4: eingeplante Zeilen nicht blass', async (t) => {
  const gezaehlt = {};
  for (const [breite, hoehe] of [[400, 860], [820, 1180], [1280, 900]]) {
    const { page } = await setup(t, { anpassen: echtAnpassen() });
    await page.setViewportSize({ width: breite, height: hoehe });
    await page.goto(origin + '/#/plan/1');
    const lp = page.locator('.lern-plan-lehrplan'); await lp.locator('.lern-plan-vorrat-zeile').first().waitFor();
    const gebiete = await lp.getByRole('group', { name: 'Themengebiet' }).getByRole('button').allInnerTexts();
    assert.ok(gebiete.length >= 8, 'alle Gebiete: ' + gebiete.join(', '));
    gezaehlt[breite] = {};
    for (const g of gebiete) {
      await lp.getByRole('group', { name: 'Themengebiet' }).getByRole('button', { name: g, exact: true }).click();
      await lp.locator('.lern-plan-gebiet-kopf', { hasText: g + ':' }).waitFor();
      const kaputt = (await gebrocheneWoerter(lp.locator('.lern-plan-vorrat, .lern-plan-gebiet-kopf'))).filter((w) => !w.includes('-') && w.replace(/[^\p{L}]/gu, '').length >= 3);
      if (kaputt.length) gezaehlt[breite][g] = kaputt;
      // N4: eingeplante Zeilen in voller Deckkraft und mit derselben Schriftfarbe wie die übrigen
      const drin = lp.locator('.lern-plan-vorrat-zeile.lern-plan-drin');
      if (await drin.count()) {
        assert.equal(await drin.first().evaluate((x) => getComputedStyle(x).opacity), '1', `${g}: eingeplant nicht blass`);
        const farben = await lp.locator('.lern-plan-vorrat-zeile .lern-plan-ort > b').evaluateAll((bs) => [...new Set(bs.map((b) => getComputedStyle(b).color))]);
        assert.equal(farben.length, 1, `${g}: eine Titelfarbe für alle Zeilen: ${farben}`);
      }
    }
    assert.ok(await ohneQuerrollen(page), `kein Querrollen bei ${breite}`);
    if (breite === 820) { fs.mkdirSync(path.join(root, 'test-results'), { recursive: true }); await lp.screenshot({ path: path.join(root, 'test-results/lb6-themengebiet-820.png') }); }
    await page.close();
  }
  assert.deepEqual(gezaehlt, { 400: {}, 820: {}, 1280: {} }, 'gebrochene Wörter je Breite und Gebiet');
});

// N2 (Sollte): Plan-Zeilen links auf Handy und Tablet – Titel bis zu zwei Zeilen, nichts seitlich abgeschnitten
test('LB Teil 6 N2: Plan links – Titel zweizeilig statt „…“ (400 und 820)', async (t) => {
  for (const [breite, hoehe] of [[400, 860], [820, 1180]]) {
    const { page } = await setup(t, { anpassen: echtAnpassen() });
    await page.setViewportSize({ width: breite, height: hoehe });
    await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-links .lern-plan-zeile').first().waitFor();
    const r = await page.locator('.lern-plan-links .lern-plan-zeile .lern-plan-ort > b').evaluateAll((bs) => bs.filter((b) => b.getClientRects().length).map((b) => ({
      t: b.innerText, quer: b.scrollWidth > b.clientWidth + 1, zeilen: Math.round(b.getBoundingClientRect().height / parseFloat(getComputedStyle(b).lineHeight)), gekappt: b.scrollHeight > b.clientHeight + 1 })));
    assert.ok(r.length >= 5, 'Plan-Zeilen da');
    assert.deepEqual(r.filter((x) => x.quer).map((x) => x.t), [], `seitlich abgeschnitten bei ${breite}`);
    assert.ok(r.every((x) => x.zeilen <= 2), `höchstens zwei Zeilen bei ${breite}`);
    assert.ok(r.some((x) => x.zeilen === 2), `lange Titel nutzen die zweite Zeile bei ${breite}`);
    const gekappt = r.filter((x) => x.gekappt).length; console.log(`N2 ${breite}: ${gekappt} von ${r.length} Titeln nach zwei Zeilen gekürzt`);
    // Teil 9 N7: nie Trennstrich und „…“ hintereinander – an der Kürzung (Ende der zweiten Zeile) darf kein Wort getrennt sein
    const getrenntGekappt = await page.locator('.lern-plan-links .lern-plan-zeile .lern-plan-ort > b').evaluateAll((bs) => bs.filter((b) => b.getClientRects().length && b.scrollHeight > b.clientHeight + 1).filter((b) => {
      const unten = b.getBoundingClientRect().bottom; const w = document.createTreeWalker(b, NodeFilter.SHOW_TEXT); const zeichen = [];
      for (let n = w.nextNode(); n; n = w.nextNode()) for (let i = 0; i < n.data.length; i++) { const r = document.createRange(); r.setStart(n, i); r.setEnd(n, i + 1); const q = r.getClientRects()[0]; zeichen.push({ c: n.data[i], top: q ? q.top : Infinity }); }
      const k = zeichen.findIndex((z) => z.top >= unten - 1); return k > 0 && /\p{L}/u.test(zeichen[k].c) && /\p{L}/u.test(zeichen[k - 1].c);
    }).map((b) => b.title));
    assert.deepEqual(getrenntGekappt, [], `${breite}: Trennstrich und „…“ hintereinander`);
    if (breite === 400) assert.ok(gekappt <= 4, `Teil 9 N7: auf dem Handy höchstens wenige Titel mit „…“ (${gekappt}; vorher 12)`);
    assert.ok(gekappt <= r.length / 3, `erst nach zwei Zeilen „…“ – gekappt: ${gekappt} von ${r.length}`); // Nachprüfung 4: vorher einzeilig, 31 (400) bzw. 28 (820) gekürzt
    if (breite === 400) await page.screenshot({ path: path.join(root, 'test-results/lb6-plan-400.png') });
    await page.close();
  }
});

// N3 (Sollte): Abschnittszähler zählt nur die Flüge der eigenen Stufe – Kopf und Abschnitt zeigen dieselbe Zahl
test('LB Teil 6 N3: Kopf und Abschnitte zeigen dieselbe Zahl je Stufe („16 Orte · 20 Flüge in Wiederholung“)', async (t) => {
  const { page } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-gruppe').first().waitFor();
  const kopf = (await page.locator('.lern-plan-zaehler').innerText()).replace(/\s+/g, ' ');
  const zahlKopf = (z) => Number(kopf.match(new RegExp('(\\d+) ' + z))?.[1]);
  const abschnitt = async (sel) => (await page.locator(sel).innerText()).replace(/\s+/g, ' ');
  const pruefe = (txt, z, wort) => { const m = txt.match(new RegExp(`· (\\d+) (Orte?|ORTE?) · (\\d+) (Flüge?|FLÜGE?|Flug|FLUG) ${wort}`, 'i')); assert.ok(m, `${z}: ${txt}`); assert.equal(Number(m[3]), zahlKopf(z), `${z}: Kopf „${kopf}“ ↔ Abschnitt „${txt}“`); return m; };
  pruefe((await page.locator('.lern-plan > .lern-plan-gruppe', { hasText: /gerade dran/i }).first().innerText()).replace(/\s+/g, ' '), '▶', 'gerade dran');
  pruefe(await abschnitt('.lern-plan-wdh > .lern-plan-gruppe'), '↻', 'in Wiederholung');
  await page.locator('.lern-plan-komplett > summary').click();
  pruefe(await abschnitt('.lern-plan-komplett > summary'), '◉', 'komplett gekonnt');
  // Flüge einer Stufe in einem Ort mit anderer Stufe (↻-Flug in einem ▶-Ort) stehen dabei
  const r = await page.evaluate(() => [...document.querySelectorAll('.lern-plan-gruppe-zahl')].map((x) => x.textContent));
  for (const z of r) { const m = z.match(/davon (\d+) in Orten weiter oben/); if (m) assert.ok(Number(m[1]) > 0, z); }
});

// N5 (Etappen-Liste mit Stand) entfällt mit LB Teil 8 (Variante A: keine Etappen-Kästchen in der Karte).

// Punkt 6 (aus LB-3 Nachbesserung): Rückgängig nur für den jüngsten Schritt, Ablehnung verständlich; Rückfall-Hinweis; heute_bis
test('LB Teil 6 Punkt 6: „↶ Rückgängig“ nur für den jüngsten Schritt, Ablehnung des Servers verständlich', async (t) => {
  for (const ablehnen of [false, true]) {
    const { page, calls } = await setup(t);
    await page.setViewportSize({ width: 820, height: 1180 });
    let rev = 1, schritt = 900; const orte = vieleOrte().slice(0, 3);
    await page.route('**/functions/v1/lernen-api/**', async (route) => {
      const b = JSON.parse(route.request().postData() || '{}'); const d = b.daten || {};
      const antwort = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
      if (b.aktion === 'schule_plan_setzen') { calls.push(b);
        if (d.rueckgaengig && ablehnen) return route.fulfill({ status: 400, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Inzwischen wurde etwas anderes geändert.' }) });
        rev++; return antwort({ ok: true, revision: rev, schritt_id: ++schritt }); }
      if (b.aktion === 'schule_plan_lesen') return antwort({ ok: true, kann_abwaehlen: true, kind: { id: 1, name: 'Kind A', klasse: 5, schulart: 'gym_by' }, revision: rev, orte, notizen: [], verlauf: [],
        plan: orte.map((o, i) => ({ block_id: o.block_id, position: i + 1, art: 'normal', status: 'offen', kann_schon: false, ausgelassen: [] })) });
      return route.fallback();
    });
    await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-zeile').first().waitFor();
    const leiste = page.locator('.lern-plan-kopf'); const rueck = leiste.getByRole('button', { name: /Rückgängig/ });
    await page.getByRole('button', { name: 'Rom – Flugort 1 nach unten' }).click(); await leiste.getByText('Gespeichert', { exact: true }).waitFor();
    await page.getByRole('button', { name: 'Paris – Flugort 3 nach oben' }).click(); await leiste.getByText('Gespeichert', { exact: true }).waitFor();
    assert.equal(await rueck.isDisabled(), false);
    await rueck.click();
    const setzen = () => calls.filter((c) => c.aktion === 'schule_plan_setzen').map((c) => c.daten);
    for (let i = 0; i < 40 && setzen().length < 3; i++) await page.waitForTimeout(50);
    assert.equal(setzen()[2].rueckgaengig, 902, 'nur der jüngste Schritt');
    if (!ablehnen) {
      await leiste.getByText('Rückgängig gemacht · Gespeichert').waitFor();
      assert.equal(await rueck.isDisabled(), true, 'kein zweiter Schritt zurück');
    } else {
      await page.locator('.lern-plan-meldung').getByText('Rückgängig geht nur für die letzte Änderung. Inzwischen wurde etwas anderes geändert.').waitFor();
      assert.ok(await page.locator('.lern-plan-meldung').getByRole('button', { name: 'Neu laden' }).isVisible());
      assert.equal(await rueck.isDisabled(), true);
    }
    await page.close();
  }
});

test('LB Teil 6 Punkt 6: Rückfall-Hinweis bei „Kann er komplett“; „heute“ des Kindes aus heute_bis (Knobeln des Tages, Wiederholungsrunde)', async (t) => {
  const { page } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-zeile').first().waitFor();
  const r = await page.evaluate(() => {
    const z = (s) => lernStufeZusatz(s);
    const el2 = lernStufeWortEl({ stufe: 'komplett', gesetzt: 'komplett', hinweis: 'rueckfall', wieder_offen: 1 });
    const zukunft = new Date(Date.now() + 3600e3).toISOString(), vorbei = new Date(Date.now() - 3600e3).toISOString();
    localStorage.setItem('lern.heute.77', JSON.stringify({ tag: '2031-05-06', n: 2, server: true, geraet: '2031-05-05', bis: zukunft }));
    const tagServer = lernHeuteTag(77); lernWdhHeute(77, true); const runde = localStorage.getItem('lern.wdhrunde.77');
    localStorage.setItem('lern.heute.77', JSON.stringify({ tag: '2031-05-06', n: 2, server: true, geraet: '2031-05-05', bis: vorbei }));
    return { gesetzt: z({ stufe: 'komplett', gesetzt: 'komplett', hinweis: 'rueckfall', wieder_offen: 2 }), sicher: z({ stufe: 'komplett', hinweis: 'rueckfall', wieder_offen: 1 }), ohne: z({ stufe: 'komplett', gesetzt: 'komplett' }),
      klasse: el2.className, text: el2.innerText || el2.textContent, tagServer, runde, tagAbgelaufen: lernHeuteTag(77), geraet: lernGeraetTag() };
  });
  assert.equal(r.gesetzt, 'gesetzt · Rückfall: 2 Etappen wieder offen');
  assert.equal(r.sicher, 'alle Etappen sicher · Rückfall: 1 Etappe wieder offen');
  assert.equal(r.ohne, 'gesetzt');
  assert.match(r.klasse, /lern-st-rueckfall/);
  assert.equal(r.tagServer, '2031-05-06', 'Tag des Kindes vom Server, solange heute_bis nicht vorbei ist');
  assert.equal(r.runde, '2031-05-06', 'Wiederholungsrunde merkt den Tag des Kindes');
  assert.equal(r.tagAbgelaufen, r.geraet, 'nach heute_bis: Kalendertag des Geräts');
  // in der Lehrer-Ansicht sichtbar: ein Flug „komplett“ mit Rückfall
  const { page: p2 } = await setup(t, { anpassen: (aktion, e) => { const x = echtAnpassen()(aktion, e); if (aktion !== 'schule_plan_lesen' || !x) return x;
    const t1 = x.orte.flatMap((o) => o.themen).find((q) => q.stufe?.stufe === 'komplett'); t1.stufe = { ...t1.stufe, gesetzt: 'komplett', hinweis: 'rueckfall', wieder_offen: 1 };
    const ort = x.orte.find((o) => o.themen.includes(t1)); const zeile = x.plan.find((q) => q.block_id === ort.block_id); if (zeile) zeile.kann_schon_themen = [t1.thema_id];
    return x; } });
  await p2.setViewportSize({ width: 1280, height: 900 });
  await p2.goto(origin + '/#/plan/1'); const lp = p2.locator('.lern-plan-lehrplan'); await lp.getByRole('button', { name: /Klasse/ }).first().click();
  const kl = Object.keys({ 5: 1, 6: 1 }); let gefunden = false;
  for (const k of kl) { await lp.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: new RegExp('^Kl\\. ' + k) }).click();
    if (await lp.locator('.lern-st-wort.lern-st-rueckfall').count()) { gefunden = true; break; } }
  assert.ok(gefunden, 'Rückfall-Hinweis in der Lehrer-Ansicht');
  assert.match(await lp.locator('.lern-st-wort.lern-st-rueckfall').first().innerText(), /Rückfall: 1 Etappe wieder offen/);
});

// Teil 7: Info-Seite auf dem Stand 0.82.2 + Abschluss-Ansichten (AB-A)
test('LB Teil 7: Info-Seite – neue Texte, alte doppelte Einträge entfernt, Eintrag „Abschluss einer Etappe“', async (t) => {
  const { page } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.goto(origin + '/lernen/#/info'); await page.getByRole('heading', { name: 'Erste Schritte' }).waitFor();
  await page.evaluate(() => document.querySelectorAll('details.lern-info-frage').forEach((d) => { d.open = true; }));
  const text = (await page.locator('#main').innerText()).replace(/\s+/g, ' ');
  for (const s of ['Reiter „Plan“ auf der Seite des Kindes – das ist dein Arbeitsplatz.', 'Viele auf einmal: „Auswählen“.',
    '„Auswählen“: je Ort ein Häkchen (alle seine Flüge), „▸ einzeln“ für einzelne Flüge, je Abschnitt „alle auswählen“',
    'Für so gesetzte Flüge gibt es keinen Flug-Test und keine Nachtests.', 'die Wiederholungen beginnen dann wieder nach 1 Lerntag.',
    'Im Ergebnis ist jede Antwort deutlich als RICHTIG oder FALSCH markiert.', '„Erst üben: ‹Etappe›“ oder „Gleich verbessern“',
    'Nach jeder Landung kommt von selbst eine Knobel-Bordkarte der Etappe (überspringbar mit „Heute keine Knobel-Bordkarte“)',
    'Der Filter „Inhalt“ zeigt, was fertig ist (●), was in Prüfung ist (◐) und was noch fehlt (○).', 'Gymnasium und Realschule nach LehrplanPLUS Bayern, IB nach dem MYP-Rahmenplan',
    'Abschluss einer Etappe:', '⚡ Direkt, ✓ Sauber oder ⚡ Ausdauer', 'Landungen vor dieser Version haben kein Abzeichen.'])
    assert.ok(text.includes(s), 'fehlt: ' + s);
  for (const s of ['Lernstand: die Lehrplan-Landkarte', 'Was wackelt?: was sitzt', 'setzt Häkchen je Flug', 'Sie erscheinen, wenn eine Etappe sitzt', 'eine Tabelle aller Flüge', 'hake ab, was es schon kann', 'Lehrplan-Übersicht', 'Eine Zeile antippen öffnet „Inhalte ansehen“'])
    assert.ok(!text.includes(s), 'noch da: ' + s);
});

// ---------- 0.83.1: LB Teil 8 (Themen-Karte kompakter, Variante A) und Nachtrag B (flug_geschafft) ----------
test('LB Teil 8: aufgeklappte Karte – „Inhalte ansehen (n Etappen)“ · Ort, Stufe ⓘ mit drei schmalen Knöpfen, roter Textlink; 400/820/1280 ohne gebrochene Wörter', async (t) => {
  for (const breite of [400, 820, 1280]) {
    const { page, calls } = await lbOeffnen(t, breite);
    const lp = await lbKlasse7(page);
    const zeile = (n) => lp.locator('.lern-lp-zeile', { hasText: `Gym-7-Flug ${n}` });
    const zuHoehe = await zeile(2).evaluate((x) => Math.round(x.getBoundingClientRect().height));
    assert.equal(await zeile(1).locator('.lern-lp-detail').count(), 0, 'zugeklappt ohne Karte');
    await zeile(1).locator('.lern-lp-titel').click();
    const karte = zeile(1).locator('.lern-lp-detail'); await karte.waitFor();
    // 3. Inhalte ansehen + Ort, keine Etappen-Kästchen, keine Erklärungszeilen unter den Knöpfen
    const inh = karte.locator('.lern-lp-inhalte');
    if (await inh.count()) { assert.match(await inh.innerText(), /^Inhalte ansehen \(\d+ Etappen?\)$/); assert.match(await inh.getAttribute('href'), /^#\/inhalte\/\d+$/);
      assert.equal(await inh.evaluate((x) => getComputedStyle(x).borderTopStyle), 'solid', 'Knopf mit Rahmen'); }
    else assert.match(await karte.locator('.lern-lp-inhalt').innerText(), /^noch kein Inhalt/); // Flug ohne Inhalt
    assert.match(await karte.locator('.lern-lp-ort').innerText(), /^Ort: /);
    assert.equal(await karte.locator('.lern-st-etappe, .lern-st-knopf small').count(), 0);
    // 4./5. Stufe ⓘ, drei Knöpfe, rechts „In den Plan nehmen“ (nicht im Plan)
    assert.equal(await karte.locator('.lern-lp-info').getAttribute('href'), '#/info/stufen');
    assert.deepEqual(await karte.locator('.lern-lp-stufe-knopf').allInnerTexts(), ['Lernen', 'Kann er – wiederholen', 'Kann er komplett']);
    const rein = karte.getByRole('button', { name: 'Gym-7-Flug 1: In den Plan nehmen' });
    assert.deepEqual(await rein.evaluate((x) => [getComputedStyle(x).borderTopWidth, getComputedStyle(x).textDecorationLine]), ['0px', 'underline'], 'Textlink, kein Kasten');
    assert.deepEqual(await gebrocheneWoerter(karte), [], `${breite}: gebrochene Wörter in der Karte`);
    assert.ok(await ohneQuerrollen(page), `${breite}: kein Querrollen`);
    // Wirkung wie bisher: „Kann er – wiederholen“ nimmt den Flug als „wiederholen“ in den Plan; aktiver Knopf grün mit ✓
    await karte.getByRole('button', { name: 'Gym-7-Flug 1: Kann er – wiederholen' }).click();
    await page.waitForFunction(() => document.querySelector('.lern-plan-stand').textContent === 'Gespeichert');
    const setzen = calls.filter((c) => c.aktion === 'schule_plan_setzen').map((c) => c.daten); const letzte = setzen.at(-1);
    assert.ok(letzte.eintraege.some((x) => (x.kann_wdh_themen || []).length), 'kann_wdh_themen gespeichert');
    const k2 = zeile(1).locator('.lern-lp-detail');
    const aktiv = k2.locator('.lern-lp-stufe-knopf[aria-pressed=true]');
    assert.equal(await aktiv.innerText(), '✓ Kann er – wiederholen');
    assert.equal(await aktiv.evaluate((x) => getComputedStyle(x).backgroundColor), await page.evaluate(() => { const d = document.createElement('i'); d.style.background = 'var(--st1h)'; document.body.append(d); const c = getComputedStyle(d).backgroundColor; d.remove(); return c; }), 'grün hinterlegt');
    const raus = k2.getByRole('button', { name: 'Gym-7-Flug 1: Aus dem Plan nehmen' }); await raus.waitFor();
    assert.equal(await raus.evaluate((x) => getComputedStyle(x).color), await page.evaluate(() => { const d = document.createElement('i'); d.style.color = 'var(--st5)'; document.body.append(d); const c = getComputedStyle(d).color; d.remove(); return c; }), 'rot');
    { // rechts als Textlink: in derselben Zeile wie die Knöpfe oder (schmale Spalte, Handy) in eigener Zeile darunter – immer rechtsbündig
      const [kn, ra, st] = await Promise.all([k2.locator('.lern-lp-stufe-knoepfe').boundingBox(), raus.boundingBox(), k2.locator('.lern-lp-stufen').boundingBox()]);
      assert.ok(Math.abs((ra.x + ra.width) - (st.x + st.width)) <= 2, `${breite}: rechtsbündig`);
      assert.ok(Math.abs(ra.y - kn.y) <= 6 || ra.y >= kn.y + kn.height - 1, `${breite}: dieselbe Zeile oder eigene Zeile darunter`);
      if (breite === 400) assert.ok(ra.y >= kn.y + kn.height - 1, 'Handy: eigene Zeile');
    }
    assert.deepEqual(await gebrocheneWoerter(k2), [], `${breite}: gebrochene Wörter nach dem Umschalten`);
    await k2.screenshot({ path: path.join(root, `test-results/lb8-karte-${breite}.png`) });
    // zugeklappt unverändert
    await zeile(1).locator('.lern-lp-titel').click(); await zeile(1).locator('.lern-lp-detail').waitFor({ state: 'detached' });
    assert.equal(await zeile(2).evaluate((x) => Math.round(x.getBoundingClientRect().height)), zuHoehe, 'zugeklappte Zeilen unverändert');
    assert.equal(await zeile(1).locator('.lern-lp-detail').count(), 0);
    await page.close();
  }
});

test('LB Teil 8: Themengebiet aufgeklappt mit derselben Stufen-Zeile; Rückfall bleibt sichtbar; „ⓘ“ öffnet die Stufen auf „So funktioniert’s“', async (t) => {
  const { page } = await setup(t, { anpassen: (aktion, e) => { const x = echtAnpassen()(aktion, e); if (aktion !== 'schule_plan_lesen' || !x) return x;
    const t1 = x.orte.flatMap((o) => o.themen).find((q) => q.stufe?.stufe === 'komplett'); t1.stufe = { ...t1.stufe, gesetzt: 'komplett', hinweis: 'rueckfall', wieder_offen: 1 };
    const ort = x.orte.find((o) => o.themen.includes(t1)); const zeile = x.plan.find((q) => q.block_id === ort.block_id); if (zeile) zeile.kann_schon_themen = [t1.thema_id]; return x; } });
  await page.setViewportSize({ width: 820, height: 1180 });
  await page.goto(origin + '/#/plan/1');
  const lp = page.locator('.lern-plan-lehrplan'); const ort = lp.locator('.lern-plan-vorrat-zeile').first(); await ort.waitFor();
  await ort.locator('.lern-plan-ort').click();
  const fl = lp.locator('.lern-plan-vorrat-ort .lern-plan-flug-zeile').first(); await fl.waitFor();
  assert.equal(await fl.locator('.lern-lp-stufe-knopf').count(), 3);
  assert.equal(await fl.locator('.lern-st-knopf').count(), 0, 'keine großen Felder mehr');
  assert.match(await fl.locator('.lern-lp-inhalte').innerText(), /^Inhalte ansehen \(\d+ Etappen?\)$/);
  // Rückfall bleibt sichtbar (Nach Klasse, Kopf der Zeile)
  await lp.getByRole('button', { name: /Klasse/ }).first().click(); let da = false;
  for (const k of ['5', '6']) { await lp.getByRole('group', { name: 'Klasse' }).getByRole('button', { name: new RegExp('^Kl\\. ' + k) }).click(); if (await lp.locator('.lern-st-rueckfall').count()) { da = true; break; } }
  assert.ok(da, 'Rückfall-Hinweis');
  const z = lp.locator('.lern-lp-zeile', { has: page.locator('.lern-st-rueckfall') }).first(); await z.locator('.lern-lp-titel').click();
  assert.match(await z.locator('.lern-st-rueckfall').innerText(), /Rückfall: 1 Etappe wieder offen/);
  // ⓘ → So funktioniert’s, Frage mit den Stufen offen
  await z.locator('.lern-lp-info').click(); await page.waitForURL(/#\/info\/stufen$/);
  const d = page.locator('details.lern-info-frage', { hasText: 'Was kann ich selbst ändern?' });
  await d.locator('summary').waitFor(); assert.equal(await d.evaluate((x) => x.open), true);
  assert.ok(await d.getByText('Jeder Flug hat eine von vier Stufen', { exact: false }).isVisible());
});

test('Nachtrag B (0.83.1): Flug-Abschluss hängt an flug_geschafft bzw. ort_geschafft; ohne das Feld wie 0.83.0', async (t) => {
  const abgeben = async (opt) => {
    const { page } = await setup(t, { gestaltung: 'nacht', anpassen: abFlug(opt) });
    await page.emulateMedia({ reducedMotion: 'reduce' }); await page.setViewportSize({ width: 400, height: 780 });
    await page.goto(origin + '/#/lerneinheit/1-1-test');
    await page.getByRole('button', { name: 'Test starten' }).click();
    await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
    await page.getByRole('button', { name: 'Weiter ›' }).click();
    await page.getByRole('button', { name: 'Markierung 2' }).click();
    await page.getByRole('button', { name: 'Abgeben' }).click();
    await page.locator('.lern-rueck-karte').first().waitFor(); await page.waitForTimeout(400);
    const n = await page.locator('.lr-abschluss-flug').count(); await page.close(); return n;
  };
  assert.equal(await abgeben({ flugGeschafft: true }), 1, 'flug_geschafft → Flug-Abschluss');
  assert.equal(await abgeben({ flugGeschafft: false }), 0, 'flug_geschafft false (z. B. zweites Verbessern) → keine Ansicht, auch wenn einheit_abgeschlossen');
  assert.equal(await abgeben({ flugGeschafft: true, ortGeschafft: true }), 1, 'flug_geschafft und ort_geschafft → zuerst „Flug geschafft“');
  assert.equal(await abgeben({}), 1, 'alter Server ohne flug_geschafft → wie 0.83.0 (einheit_abgeschlossen)');
});

// ---------- 0.83.2: LB Teil 9 (Nachprüfung 5 Lehrer, Nachprüfung Abschluss Kind) ----------
const farbeVon = (page, v) => page.evaluate((v) => { const d = document.createElement('i'); d.style.color = v; document.body.append(d); const c = getComputedStyle(d).color; d.remove(); return c; }, v);
const luminanz = (rgb) => { const [r, g, b] = rgb.match(/[\d.]+/g).slice(0, 3).map(Number).map((c) => { c /= 255; return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
const kontrastRgb = (a, b) => { const [x, y] = [luminanz(a), luminanz(b)].sort((p, q) => q - p); return (x + 0.05) / (y + 0.05); };

test('LB Teil 9 N6: gewählter Themengebiet-Knopf bleibt unter dem Mauszeiger dunkel mit weißer Schrift', async (t) => {
  const { page } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 400, height: 860 });
  await page.goto(origin + '/#/plan/1');
  const g = page.locator('.lern-plan-lehrplan').getByRole('group', { name: 'Themengebiet' });
  const k = g.getByRole('button', { name: 'Geometrie', exact: true }); await k.click(); await k.hover();
  assert.equal(await k.getAttribute('aria-pressed'), 'true');
  const [bg, fg] = await k.evaluate((x) => [getComputedStyle(x).backgroundColor, getComputedStyle(x).color]);
  assert.equal(fg, 'rgb(255, 255, 255)');
  assert.equal(bg, await page.evaluate(() => { const d = document.createElement('i'); d.style.background = 'var(--accent, #1b2a41)'; document.body.append(d); const c = getComputedStyle(d).backgroundColor; d.remove(); return c; }), 'dunkel wie ohne Zeiger');
  assert.ok(kontrastRgb(bg, fg) >= 4.5, `Kontrast ${kontrastRgb(bg, fg).toFixed(1)}`);
  // ein nicht gewählter Knopf bekommt beim Hover weiter die helle Fläche
  const n = g.getByRole('button', { name: 'Algebra', exact: true }); await n.hover();
  assert.notEqual(await n.evaluate((x) => getComputedStyle(x).backgroundColor), bg);
});

test('LB Teil 9 N7: Plan links auf dem Handy – Titel nur das Thema, Gebiet klein darunter, ↑ ↓ 32 px; Messung „…“', async (t) => {
  const { page } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 400, height: 860 });
  await page.goto(origin + '/#/plan/1'); await page.locator('.lern-plan-links .lern-plan-zeile').first().waitFor();
  const z = page.locator('.lern-plan-links .lern-plan-zeile').first();
  const b = z.locator('.lern-plan-ort > b'); const titel = await b.getAttribute('title');
  assert.match(titel, / – /, 'Titel-Attribut mit Gebiet (für den Zeiger)');
  const [gebiet, thema] = titel.split(' – ');
  assert.equal((await b.innerText()).trim(), thema, 'sichtbar nur das Thema');
  assert.ok((await z.locator('.lern-plan-ort > small').innerText()).startsWith(`${gebiet} · `), 'Gebiet klein in der Zeile darunter');
  assert.equal(await z.locator('.lern-plan-gebiet-klein').evaluate((x) => getComputedStyle(x).color), await farbeVon(page, 'var(--text-muted)'), 'grau');
  for (const p of await z.locator('.lern-plan-pfeile .iconbtn').all()) assert.equal(Math.round((await p.boundingBox()).width), 32);
  // Messung: wie viele Titel enden auf dem Handy noch mit „…“? (Nachprüfung 5: fast alle; Ziel: höchstens wenige)
  const r = await page.locator('.lern-plan-links .lern-plan-zeile .lern-plan-ort > b').evaluateAll((bs) => bs.filter((x) => x.getClientRects().length).map((x) => x.scrollHeight > x.clientHeight + 1));
  const gekappt = r.filter(Boolean).length; console.log(`N7 400: ${gekappt} von ${r.length} Titeln mit „…“`);
  assert.ok(gekappt <= 4, `höchstens wenige mit „…“: ${gekappt}`);
  assert.equal(await page.locator('.lern-plan-links .lern-plan-zeile .lern-plan-ort > b').evaluateAll((bs) => bs.filter((x) => getComputedStyle(x).hyphens === 'auto').length), 0, 'keine automatische Trennung (also nie Trennstrich und „…“)');
  await page.screenshot({ path: path.join(root, 'test-results/lb9-plan-400.png') });
  // Rechner: Gebiet weiter als Vorsatz im Titel
  await page.setViewportSize({ width: 1280, height: 900 }); await page.waitForTimeout(100);
  assert.equal((await b.innerText()).trim(), titel);
  assert.equal(await z.locator('.lern-plan-gebiet-klein').isVisible(), false);
});

test('LB Teil 9 Info: Schritt 1 nennt „Rechts (auf dem Handy darunter) der Lehrplan“', async (t) => {
  const { page } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.goto(origin + '/lernen/#/info'); await page.getByRole('heading', { name: 'Erste Schritte' }).waitFor();
  assert.ok((await page.locator('#main').innerText()).replace(/\s+/g, ' ').includes('Rechts (auf dem Handy darunter) der Lehrplan: „Nach Themengebiet“'));
});

test('LB Teil 9 N1/N5: Ort-Stempel mit Datum „TT.MM.“ (ein Punkt am Ende); „Überspringen ›“ auf Sand lesbar', async (t) => {
  const { page } = await abTest(t, { ortGeschafft: true, naechster: 'anders' }, { gestaltung: 'tag' });
  await page.locator('.lr-abschluss-flug').getByRole('button', { name: 'Überspringen ›' }).click();
  const o = page.locator('.lr-abschluss-ort'); await o.waitFor();
  const st = (await o.locator('.lr-ab-passstempel').innerText()).replace(/\s+/g, ' ').trim();
  const heute = await page.evaluate(() => { const d = new Date(); return `${String(d.getDate()).padStart(2, '0')}.${String(d.getMonth() + 1).padStart(2, '0')}.`; });
  assert.ok(st.endsWith(`Zahlen · ${heute}`), st); assert.ok(!/\.\.$/.test(st), 'kein doppelter Punkt: ' + st);
  const skip = o.getByRole('button', { name: 'Überspringen ›' });
  const [bg, fg] = await skip.evaluate((x) => [getComputedStyle(x).backgroundColor, getComputedStyle(x).color]);
  assert.ok(kontrastRgb(bg, fg) >= 4.5, `Überspringen: Kontrast ${kontrastRgb(bg, fg).toFixed(1)} (${bg} / ${fg})`);
  const sand = await o.locator('.lr-ab-szene').evaluate(() => 'rgb(228, 207, 160)'); // mittlere Farbe des Sand-Verlaufs (#E4CFA0)
  assert.ok(kontrastRgb(bg, sand) >= 3, `Knopf hebt sich vom Sand ab: ${kontrastRgb(bg, sand).toFixed(1)}`);
  await o.screenshot({ path: path.join(root, 'test-results/lb9-ort-400.png') });
});

test('LB Teil 9 N2/N3: „2/2“ berührt „AUF ANHIEB“ nicht; Sturmflug 360 × 640 – Blitz läuft nicht durch den Text', async (t) => {
  const { page } = await abLande(t, 'direkt', { x: { bordkarten: 2 } });
  const [zahl, klein] = await page.locator('.lr-ab-riesig').evaluate((x) => { const r = document.createRange(); r.setStart(x.firstChild, 0); r.setEnd(x.firstChild, x.firstChild.length);
    const z = [...r.getClientRects()].reduce((m, q) => Math.max(m, q.bottom), 0); return [z, x.querySelector('small').getBoundingClientRect().top]; });
  assert.ok(klein - zahl >= 4, `Abstand unter „2/2“: ${Math.round(klein - zahl)} px`);
  await page.close();
  for (const g of ['tag', 'nacht']) {
    const { page: p } = await abLande(t, 'sturm', { gestaltung: g, breite: 360, hoehe: 640, x: { bordkarten: 15, stufe_gesenkt: 2 } });
    const v = p.locator('.lr-abschluss-etappe');
    const treffer = await v.evaluate((h) => {
      const pfad = h.querySelector('.lr-ab-wolken path'); const L = pfad.getTotalLength(); const m = pfad.getScreenCTM(); const svg = pfad.ownerSVGElement;
      const punkte = []; for (let i = 0; i <= 40; i++) { const q = pfad.getPointAtLength((L * i) / 40); const sp = svg.createSVGPoint(); sp.x = q.x; sp.y = q.y; const w = sp.matrixTransform(m); punkte.push(w); }
      const texte = [...h.querySelectorAll('.lr-ab-titel, .lr-ab-unter, .lr-ab-ausdauer, .lr-ab-kopf, .lr-ab-oben')].map((e) => e.getBoundingClientRect());
      return punkte.filter((q) => texte.some((r) => q.x >= r.left && q.x <= r.right && q.y >= r.top && q.y <= r.bottom)).length; });
    assert.equal(treffer, 0, `${g}: Blitz kreuzt Text`);
    await p.screenshot({ path: path.join(root, `test-results/lb9-sturm-${g}-360.png`) });
    await p.close();
  }
});

test('0.83.3 (Entscheidung 21.11.): „Etappen ▸“ in der Themen-Karte – zugeklappt, aufgeklappt mit Nummer, Titel und Stand rechts', async (t) => {
  const { page } = await setup(t, { anpassen: echtAnpassen() });
  await page.setViewportSize({ width: 400, height: 860 });
  await page.goto(origin + '/#/plan/1');
  const lp = page.locator('.lern-plan-lehrplan'); await lp.getByRole('button', { name: /Klasse/ }).first().click();
  await lp.getByText('Lineare Ungleichungen', { exact: false }).first().click();
  const karte = lp.locator('.lern-lp-detail').first(); await karte.waitFor();
  const link = karte.getByRole('button', { name: 'Etappen ▸' });
  assert.equal(await link.getAttribute('aria-expanded'), 'false');
  assert.equal(await karte.locator('.lern-st-etappe').count(), 0, 'zugeklappt');
  await link.click();
  const auf = karte.getByRole('button', { name: 'Etappen ▾' }); await auf.waitFor();
  assert.equal(await auf.getAttribute('aria-expanded'), 'true');
  assert.ok(await auf.evaluate((x) => x === document.activeElement), 'Fokus bleibt auf dem Link');
  const et = karte.locator('.lern-st-etappe'); await et.first().waitFor();
  const lage = await et.evaluateAll((es) => es.map((e) => { const t = e.querySelector('.lern-st-et-titel').getClientRects()[0], s = e.querySelector('.lern-st-et-stand').getBoundingClientRect(), b = e.getBoundingClientRect();
    return { erste: [t.top, t.bottom], stand: [s.top, s.bottom], rechts: b.right - s.right, text: e.innerText.replace(/\s+/g, ' ').trim() }; }));
  assert.ok(lage.length >= 3, 'Etappen da');
  for (const l of lage) { const m = (l.stand[0] + l.stand[1]) / 2; assert.ok(m >= l.erste[0] && m <= l.erste[1], 'Stand in der ersten Titelzeile: ' + l.text); assert.ok(l.rechts <= 12, 'rechtsbündig');
    assert.match(l.text, /^\d+ .+ (offen|begonnen|gelandet|sicher|wieder offen)$/); }
  assert.deepEqual(await gebrocheneWoerter(karte), []);
  await karte.screenshot({ path: path.join(root, 'test-results/lb9-etappen-400.png') });
  await auf.click(); await karte.getByRole('button', { name: 'Etappen ▸' }).waitFor();
  assert.equal(await karte.locator('.lern-st-etappe').count(), 0, 'wieder zugeklappt');
});

// 0.83.3 (Entscheidung 21.11., Punkt 4): Die strengen Reisewörter gelten für die Kinderseiten. Auf Eltern-/Lehrerseiten sind „Thema/Themen“ und „Themengebiet“ erlaubt.
// Auf Kinderseiten steht „Thema“ nur dort, wo die Vorgabe der Abschluss-Ansichten es selbst so vorsieht („Weiter zum nächsten Thema“, „NEUES THEMA“) – das prüfen die AB-A-Tests.
test('0.83.3: Reisewörter auf den Kinderseiten (Abflugtafel, Reisepass, Erklärung, Bordkarten, Flug-Test)', async (t) => {
  for (const gestaltung of [undefined, 'tag']) {
  const { page } = await setup(t, gestaltung ? { gestaltung } : {});
  const verboten = /Lernkarte|Aufgabe|\bThemen\b|Themenplan|Lernziel|\bGebiet\b/;
  for (const [pfad, warte] of [['reise/1', { role: 'heading', name: 'Natürliche Zahlen' }], ['reisepass/1', null], ['lerneinheit/1-1-erklaeren-1', null], ['lerneinheit/1-1-ueben-1', 'Etappe 1 von 3'], ['lerneinheit/1-1-test', 'Test starten']]) {
    await page.goto(origin + '/#/' + pfad); await page.reload();
    await page.waitForFunction(() => (document.querySelector('#main')?.innerText || '').trim().length > 40 && !/Lädt|lädt …/.test(document.querySelector('#main').innerText)); await page.waitForTimeout(300);
    const text = await page.evaluate(() => { const c = document.querySelector('#main').cloneNode(true);
      c.querySelectorAll('.lern-aufgabe-text, .lern-frage, .lr-frage, .lern-erkl, .lr-erkl, .lern-merke').forEach((x) => x.remove()); return c.innerText; });
    assert.ok(text.trim().length > 20, `${pfad}: Inhalt geladen`);
    const m = text.match(verboten); assert.equal(m, null, `${gestaltung || 'klassisch'} ${pfad}: „${m?.[0]}“ in „${m ? text.slice(Math.max(0, m.index - 40), m.index + 40).replace(/\s+/g, ' ') : ''}“`);
  }
  await page.close();
  }
});

// 0.83.3 (Nachträge aus Prüfergebnis 888): nur ort_geschafft, ohne flug_geschafft → direkt Ort-Stempel und Bordkarte, nicht noch einmal „Flug geschafft“
test('0.83.3: Server meldet nur ort_geschafft → direkt Ort-Stempel, dann Bordkarte; kein zweites „Flug geschafft“', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: abFlug({ flugGeschafft: false, ortGeschafft: true, naechster: 'anders' }) });
  await page.emulateMedia({ reducedMotion: 'reduce' }); await page.setViewportSize({ width: 400, height: 780 });
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByRole('button', { name: 'Test starten' }).click();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
  await page.getByRole('button', { name: 'Weiter ›' }).click();
  await page.getByRole('button', { name: 'Markierung 2' }).click();
  await page.getByRole('button', { name: 'Abgeben' }).click();
  const o = page.locator('.lr-abschluss-ort'); await o.waitFor();
  assert.equal(await page.locator('.lr-abschluss-flug').count(), 0, 'kein „Flug geschafft“');
  assert.equal(await o.locator('.lr-ab-titel').innerText(), 'ROM IST GESCHAFFT');
  await o.locator('.lr-ab-gross').click();
  const k = page.locator('.lr-abschluss-bordkarte'); await k.waitFor();
  assert.match((await k.locator('.lr-ab-route').innerText()).replace(/\s+/g, ' '), /VON ROM ✈ NACH ATHEN/);
  assert.equal(await page.locator('.lr-abschluss-flug').count(), 0);
});

// ---------- Bau-Auftrag LM (21.11.), Schritt 2: Lehrplan-Matrix für Eltern/Lehrer (0.84.0) ----------
// Lehrstoff aus der echten Themenliste; Verbindungen aus der Vorlage (Daten wie schule.voraussetzung); Lernstand erfunden (Kind A Gym 8, Kind B Gym 5).
const MX_K = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/pruefung/lehrer/matrix/entwurf/lehrplan-matrix.html'), 'utf8').match(/const K=(\[.*?\]\]);/)[1]);
const mxAnpassen = ({ verbindungen = true, extra = null } = {}) => { const basis = echtAnpassen(); return (aktion, e) => {
  const r = basis(aktion, e);
  if (aktion === 'schule_lehrplan_uebersicht' && r) {
    if (verbindungen) r.verbindungen = MX_K.map(([a, b, art, begruendung]) => ({ thema_id: a, braucht_id: b, art, begruendung }));
    for (const t of r.themen) { const q = THEMEN_ECHT.find((x) => x.thema_id === t.thema_id); t.beschreibung = q?.umfang; t.gliederung = echteEtappen(q).map((x) => x.titel); // wie der Server heute
      const g = t.jahrgang.gym_by; // Kind B (Gym 5): Klasse 5 zum Teil gekonnt, ein Flug dran
      t.stufe[2] = !g || g > 5 ? { stufe: 'nicht_im_plan', im_plan: false } : t.lehrplan_reihenfolge.gym_by < 3 ? { stufe: 'komplett', gesetzt: null } : t.lehrplan_reihenfolge.gym_by === 3 ? { stufe: 'dran', etappen: 6, gelandet: 2, wieder_offen: 1 } : { stufe: 'kommt', im_plan: true }; }
    const nz = r.themen.find((t) => t.thema_id === 15); nz.merke = ['Stellenwert: jede Stelle ist zehnmal so viel wert wie die rechts daneben.']; nz.beispiel = 'Runde 4 567 891 auf Tausender.';
    if (extra) extra(r);
  }
  return r; }; };
const mxOeffnen = async (t, breite, opt = {}) => { const { page, calls } = await setup(t, { anpassen: mxAnpassen(opt) }); await page.setViewportSize({ width: breite, height: breite < 760 ? 860 : 900 });
  await page.goto(origin + '/#/lehrplan' + (opt.kind ? '/' + opt.kind : '')); await page.getByRole('heading', { name: 'Mathe Klasse 5–10: was gelernt wird' }).waitFor(); return { page, calls }; };
// kein Wort ohne Trennstrich umbrochen: Silbentrennung (hyphens: auto) ist erlaubt, Überlaufen nicht
const ueberlaeuft = (loc) => loc.evaluateAll((els) => els.filter((x) => x.getClientRects().length && x.scrollWidth > x.clientWidth + 1).map((x) => x.textContent.slice(0, 40)));
const mitteImWort = (loc) => loc.evaluateAll((els) => els.filter((x) => { const s = getComputedStyle(x); return s.getClientRects !== undefined && x.getClientRects().length && (s.overflowWrap === 'anywhere' || s.wordBreak === 'break-all' || s.overflowWrap === 'break-word'); }).map((x) => x.className));

test('LM-1: Matrix unter Nachschlagen → Lehrplan – alle Themen, Zeilen/Spalten, Einordnen nach, Kopf je Klasse, Kurzbeschreibung, Suche', async (t) => {
  const { page } = await mxOeffnen(t, 1280);
  const chips = page.locator('.mx-chip');
  assert.equal(await chips.count(), THEMEN_ECHT.length, 'alle Themen der Themenliste');
  assert.deepEqual(await page.locator('.mx-geb').allInnerTexts(), ['Zahlen', 'Algebra', 'Funktionen', 'Geometrie', 'Fläche und Raum', 'Geld und Verhältnisse', 'Daten und Zufall', 'Entdecker-Inseln']);
  const gym8 = THEMEN_ECHT.filter((x) => x.klasse.gym_by === 8).length;
  assert.match(await page.locator('.mx-kl').nth(3).innerText(), new RegExp(`Kl\\. 8[\\s\\S]*\\d+ Themen[\\s\\S]*${gym8} Gym\u2011Pflicht`));
  // Thema ohne Gymnasium-Klasse: gestrichelt in der RS-Klasse, Kennzeichen „Gym – · RS n“
  const nurRs = THEMEN_ECHT.find((x) => !x.klasse.gym_by && x.klasse.rs_by && x.gebiet !== 'Entdecker-Inseln');
  const c = page.locator(`.mx-chip[data-id="${nurRs.thema_id}"]`);
  assert.match(await c.getAttribute('class'), /mx-zu/);
  assert.equal(await c.locator('.mx-sch b').first().innerText(), 'Gym –');
  // Reihenfolge in der Zelle: Lehrplan Gymnasium
  const zahlen5 = THEMEN_ECHT.filter((x) => x.klasse.gym_by === 5 && x.gebiet === 'Zahlen').sort((a, b) => a.reihenfolge.gym_by - b.reihenfolge.gym_by).map((x) => x.titel);
  const zelle = page.locator('.mx-zelle').nth(0);
  assert.deepEqual((await zelle.locator('.mx-titel').allInnerTexts()).slice(0, zahlen5.length), zahlen5);
  // Einordnen nach Realschule: Zeile wechselt
  await page.getByRole('group', { name: 'Einordnen nach Schulart' }).getByRole('button', { name: 'Realschule' }).click();
  assert.match(await page.locator('.mx-kl').nth(3).innerText(), /RS\u2011Pflicht/);
  assert.equal(await c.getAttribute('class').then((k) => /mx-zu/.test(k)), false, 'bei RS nicht mehr gestrichelt');
  // Klassen als Spalten
  await page.getByRole('button', { name: 'Klassen als Spalten' }).click();
  assert.equal(await page.locator('.mx-matrix.mx-s').count(), 1);
  assert.equal(await page.locator('.mx-kl').first().innerText().then((x) => x.startsWith('Klasse 5')), true);
  // Kurzbeschreibung und Suche
  await page.getByLabel('Kurzbeschreibung').check();
  assert.ok(await page.locator('.mx-chip .mx-u').count() > 50);
  await page.getByLabel('Thema suchen').fill('Bruch');
  const sichtbar = await page.locator('.mx-chip:not(.mx-weg)').count();
  assert.ok(sichtbar > 0 && sichtbar < 20, `Suche: ${sichtbar}`);
  // Schalter bleiben beim nächsten Öffnen (Speicher)
  await page.reload(); await page.locator('.mx-matrix').waitFor();
  assert.equal(await page.locator('.mx-matrix.mx-s').count(), 1); assert.equal(await page.getByLabel('Kurzbeschreibung').isChecked(), true);
});

test('LM-2/LM-3: Detail mit Verbindungen, Linien hinter den Karten, Blättern, ohne Verbindungsdaten ehrlicher Hinweis', async (t) => {
  const { page } = await mxOeffnen(t, 1280);
  const titel = (id) => THEMEN_ECHT.find((x) => x.thema_id === id).titel;
  await page.locator('.mx-chip[data-id="2"]').click(); // Lineare Gleichungen o. ä.: braucht 1, darauf bauen 3–8 auf
  const det = page.locator('.mx-detail');
  await det.getByRole('heading', { name: titel(2) }).waitFor();
  assert.match(await det.innerText(), /BRAUCHT VORHER[\s\S]*DARAUF BAUT AUF/i);
  assert.ok(await det.getByRole('button', { name: titel(1) }).count() >= 1, 'Voraussetzung verlinkt');
  assert.match(await page.locator('.mx-chip[data-id="1"]').getAttribute('class'), /mx-vor/);
  assert.match(await page.locator('.mx-chip[data-id="6"]').getAttribute('class'), /mx-nach/);
  assert.match(await page.locator(`.mx-chip[data-id="${MX_K.find((k) => k[0] === 1)[1]}"]`).getAttribute('class'), /mx-weg2|mx-vor/);
  // → n an Themen mit ≥ 2 Nachfolgern
  assert.match(await page.locator('.mx-chip[data-id="2"] .mx-n').first().innerText(), /→ \d/);
  // Linien: SVG unter den Karten, Pfade vorhanden, Karte oben auf
  const paths = page.locator('svg.mx-linien path'); await paths.first().waitFor({ state: 'attached' });
  assert.ok(await paths.count() >= 3);
  const z = await page.evaluate(() => [getComputedStyle(document.querySelector('svg.mx-linien')).zIndex, getComputedStyle(document.querySelector('.mx-chip')).zIndex]);
  assert.ok(Number(z[0]) < Number(z[1]), 'Linien hinter den Karten');
  const oben = await page.evaluate(() => { document.querySelector('.mx-chip[data-id="2"]').scrollIntoView({ block: 'center' }); const c = document.querySelector('.mx-chip[data-id="2"]').getBoundingClientRect(); return document.elementFromPoint(c.left + c.width / 2, c.top + c.height / 2)?.closest('.mx-chip')?.dataset.id; });
  assert.equal(oben, '2', 'Karte liegt über der Linie');
  // empfohlen gestrichelt
  await page.locator('.mx-chip[data-id="35"]').click();
  assert.ok(await page.locator('svg.mx-linien path.mx-empfohlen').count() >= 1);
  assert.match(await det.innerText(), /empfohlen/);
  // Das muss sitzen, Beispielaufgabe, Etappen, Lehrplan, Blättern
  await page.locator('.mx-chip[data-id="15"]').click();
  const text = await det.innerText();
  assert.match(text, /WAS GEFORDERT IST[\s\S]*DAS MUSS SITZEN[\s\S]*Stellenwert[\s\S]*BEISPIELAUFGABE[\s\S]*Runde 4 567 891[\s\S]*SCHRITTE IN DER APP[\s\S]*IM LEHRPLAN[\s\S]*M5 1\.1/i);
  assert.match(text, /Inhalt: fertig/); assert.ok(await det.getByRole('link', { name: /Inhalte ansehen/ }).count());
  const naechst = det.getByRole('button', { name: /^Nächstes Thema/ }); const name = (await naechst.getAttribute('aria-label')).replace('Nächstes Thema: ', '');
  await naechst.click(); await det.getByRole('heading', { name }).waitFor();
  // Klick auf das gewählte Thema schließt es wieder
  await page.locator('.mx-chip[aria-expanded="true"]').click(); assert.equal(await page.locator('svg.mx-linien path').count(), 0);
  // ohne Verbindungsdaten (Server vor LM-S): Hinweis statt „Keine Voraussetzung hinterlegt“
  const { page: p2 } = await mxOeffnen(t, 1280, { verbindungen: false });
  await p2.locator('.mx-chip[data-id="2"]').click();
  assert.match(await p2.locator('.mx-detail').innerText(), /liefert der Server noch nicht/);
  assert.doesNotMatch(await p2.locator('.mx-detail').innerText(), /Keine Voraussetzung hinterlegt|DARAUF BAUT AUF/i);
});

test('LM-4: Lernstand – Aus, ein Kind (Stufen, ▶ „hier ist …“, Balken), Beide vergleichen (Punkte), Detail mit „Im Plan öffnen“ und „Fehler besprechen“', async (t) => {
  const { page } = await mxOeffnen(t, 1280);
  const ls = page.getByRole('group', { name: 'Lernstand' });
  assert.deepEqual(await ls.getByRole('button').allInnerTexts(), ['Aus', 'Kind A', 'Kind B', 'Beide vergleichen']);
  assert.equal(await page.locator('.mx-chip.mx-st').count(), 0);
  await ls.getByRole('button', { name: 'Kind A' }).click();
  const dran = page.locator('.mx-chip.mx-dran'); await dran.first().waitFor();
  assert.match(await dran.first().locator('.mx-stand').innerText(), /▶ Etappe 4 von \d+ · hier ist Kind A/);
  assert.ok(await page.locator('.mx-chip.mx-st.st-1').count() > 5 && await page.locator('.mx-chip.mx-st.st-2').count() > 5 && await page.locator('.mx-chip.mx-st.st-5').count() > 5);
  assert.match(await page.locator('.mx-chip.mx-st.st-2 .mx-stand').first().innerText(), /↻ Wdh \d von 5/);
  // zum ▶-Thema gescrollt
  assert.ok(await dran.first().evaluate((x) => { const r = x.getBoundingClientRect(); return r.top >= 0 && r.bottom <= innerHeight; }), '▶ sichtbar');
  assert.equal(await page.locator('.mx-kl').nth(3).locator('.mx-balken').count(), 1);
  // Detail: Lernstand und Links
  await dran.first().click();
  const det = page.locator('.mx-detail');
  await det.getByRole('link', { name: 'Im Plan öffnen ›' }).waitFor();
  assert.match(await det.locator('.mx-ls').innerText(), /Kind A[\s\S]*Gerade dran/);
  assert.equal(await det.getByRole('link', { name: 'Fehler besprechen ›' }).count(), 0);
  // Beide vergleichen: Punkte je Kind, Balken je Kind, keine Stufen-Knöpfe
  await ls.getByRole('button', { name: 'Beide vergleichen' }).click();
  assert.equal(await page.locator('.mx-chip').first().locator('.mx-dot').count(), 2);
  assert.equal(await page.locator('.mx-chip').first().locator('.mx-dl').innerText(), 'A/B');
  assert.equal(await page.locator('.mx-kl').first().locator('.mx-balken').count(), 2);
  assert.equal(await det.locator('.lern-lp-stufe-knopf').count(), 0);
  assert.match(await det.innerText(), /Planen geht, wenn genau ein Kind gewählt ist/);
  // Kind B: offener Fehler beim ▶-Flug → „Fehler besprechen ›“ zu „Was wackelt“
  await ls.getByRole('button', { name: 'Kind B' }).click();
  await page.locator('.mx-chip.mx-dran').first().click();
  assert.equal(await det.getByRole('link', { name: 'Fehler besprechen ›' }).getAttribute('href'), '#/kind/2-wackelt');
  await ls.getByRole('button', { name: 'Aus' }).click();
  assert.equal(await page.locator('.mx-chip.mx-st, .mx-balken').count(), 0);
});

test('LM-5: Stufen-Knöpfe im Detail (ein Kind) – gleiche Aufrufe und Rückgängig wie im Plan; „Im Plan öffnen“ klappt das Thema auf; „Als Matrix ansehen“ aus dem Plan', async (t) => {
  const { page, calls } = await mxOeffnen(t, 1280);
  await page.getByRole('group', { name: 'Lernstand' }).getByRole('button', { name: 'Kind A' }).click();
  const det = page.locator('.mx-detail');
  // ein Flug, der nicht im Plan ist (Gym 9)
  const neu = THEMEN_ECHT.find((x) => x.klasse.gym_by === 9);
  await page.locator(`.mx-chip[data-id="${neu.thema_id}"]`).click();
  await det.getByRole('button', { name: `${neu.titel}: In den Plan nehmen` }).click();
  await det.getByText('Gespeichert').waitFor();
  const setzen = calls.filter((c) => c.aktion === 'schule_plan_setzen');
  assert.equal(setzen.length, 1);
  const e = setzen[0].daten.eintraege.find((x) => x.block_id === neu.block_id);
  assert.ok(e && !e.ausgelassen.includes(neu.thema_id), 'Flug im Plan');
  assert.equal(setzen[0].daten.lernender_id, 1);
  assert.equal(await det.getByRole('button', { name: `${neu.titel}: Lernen` }).getAttribute('aria-pressed'), 'true');
  // Kann er komplett, dann Rückgängig (mit Schritt des Servers)
  await det.getByRole('button', { name: `${neu.titel}: Kann er komplett` }).click(); await det.getByText('Gespeichert').waitFor();
  await det.getByRole('button', { name: '↶ Rückgängig' }).click(); await det.getByText('Rückgängig gemacht · Gespeichert').waitFor();
  const letzter = calls.filter((c) => c.aktion === 'schule_plan_setzen').pop();
  assert.equal(letzter.daten.rueckgaengig, 900);
  assert.equal(await det.getByRole('button', { name: `${neu.titel}: Lernen` }).getAttribute('aria-pressed'), 'true');
  assert.ok(calls.filter((c) => c.aktion === 'schule_lehrplan_uebersicht').length >= 2, 'Stufen nach dem Speichern neu geholt');
  // „Im Plan öffnen ›“: im Plan aufgeklappt (Flug im Plan → Ort links offen)
  const imPlan = THEMEN_ECHT.find((x) => x.klasse.gym_by === 8 && x.reihenfolge.gym_by === 4);
  await page.locator(`.mx-chip[data-id="${imPlan.thema_id}"]`).click();
  await det.getByRole('link', { name: 'Im Plan öffnen ›' }).click();
  await page.waitForURL(/#\/kind\/1-plan/);
  const ziel = page.locator(`.lern-plan-links [data-thema="${imPlan.thema_id}"]`); await ziel.waitFor();
  assert.match(await ziel.getAttribute('class'), /lern-plan-ziel/);
  // nicht im Plan → rechts „Nach Klasse“ mit dem Flug aufgeklappt
  await page.goto(origin + '/#/lehrplan/1'); await page.locator('.mx-matrix').waitFor();
  const raus = THEMEN_ECHT.find((x) => x.klasse.gym_by === 10);
  await page.locator(`.mx-chip[data-id="${raus.thema_id}"]`).click();
  await page.locator('.mx-detail').getByRole('link', { name: 'Im Plan öffnen ›' }).click();
  const rechts = page.locator(`.lern-plan-lehrplan .lern-lp-zeile[data-thema="${raus.thema_id}"]`); await rechts.waitFor();
  assert.equal(await rechts.locator('.lern-lp-titel').getAttribute('aria-expanded'), 'true');
  // „Als Matrix ansehen ›“ oben im Reiter Plan → Matrix mit diesem Kind und seiner Schulart
  await page.getByRole('link', { name: 'Als Matrix ansehen ›' }).click();
  await page.waitForURL(/#\/lehrplan\/1$/); await page.locator('.mx-chip.mx-dran').first().waitFor();
  assert.equal(await page.getByRole('group', { name: 'Lernstand' }).getByRole('button', { name: 'Kind A' }).getAttribute('aria-pressed'), 'true');
  assert.equal(await page.getByRole('group', { name: 'Einordnen nach Schulart' }).getByRole('button', { name: 'Gymnasium' }).getAttribute('aria-pressed'), 'true');
  assert.equal(await page.locator('.lern-reiter a').count(), 0, 'Matrix ist eine eigene Seite, kein fünfter Reiter');
});

test('LM Abnahme: 400, 820, 1280 px – kein Wort ohne Trennstrich umbrochen, nichts läuft über, kein Querrollen, Handy als Liste ohne Linien', async (t) => {
  for (const breite of [400, 820, 1280]) {
    const { page } = await mxOeffnen(t, breite);
    for (const modus of ['Aus', 'Kind A', 'Beide vergleichen']) {
      await page.getByRole('group', { name: 'Lernstand' }).getByRole('button', { name: modus }).click();
      for (const aufbau of breite < 760 ? ['z'] : ['Klassen als Zeilen', 'Klassen als Spalten']) {
        if (breite >= 760) await page.getByRole('button', { name: aufbau }).click();
        await page.locator('.mx-chip').first().waitFor();
        assert.deepEqual(await ueberlaeuft(page.locator('.mx-chip, .mx-chip > span, .mx-geb, .mx-kl, .mx-kl small, .mx-schalter button, .mx-liste-kopf')), [], `${breite} ${modus} ${aufbau}: überläuft`);
        assert.deepEqual(await mitteImWort(page.locator('.mx-chip, .mx-chip span, .mx-geb, .mx-kl')), [], `${breite}: Umbruch mitten im Wort erlaubt`);
        assert.deepEqual(await gebrocheneWoerter(page.locator('.mx-schalter button, .mx-kl small, .mx-sch b, .mx-stand, .mx-leiste-wort, .mx-kurz')), [], `${breite} ${modus} ${aufbau}: Kennzeichen`);
        assert.ok(await ohneQuerrollen(page), `${breite} ${modus} ${aufbau}: Querrollen`);
      }
    }
    await page.getByRole('group', { name: 'Lernstand' }).getByRole('button', { name: 'Kind A' }).click();
    if (breite >= 760) await page.getByRole('button', { name: 'Klassen als Zeilen' }).click();
    await page.evaluate(() => scrollTo(0, 0)); await page.screenshot({ path: path.join(root, `test-results/lm-oben-${breite}.png`) });
    await page.locator('.mx-chip[data-id="2"]').click();
    const det = page.locator('.mx-detail'); await det.locator('h2').waitFor();
    assert.deepEqual(await ueberlaeuft(det.locator('h2, h3, p, li, button, a')), [], `${breite}: Detail`);
    assert.deepEqual(await gebrocheneWoerter(det.locator('.lern-lp-stufe-knopf, .mx-tag, .mx-ls-links a')), [], `${breite}: Detail-Knöpfe`);
    assert.ok(await ohneQuerrollen(page), `${breite}: Querrollen mit Detail`);
    if (breite < 760) {
      assert.equal(await page.locator('.mx-matrix, svg.mx-linien').count(), 0, 'Handy: Liste, keine Linien');
      assert.equal(await page.locator('.mx-chip[data-id="2"] + .mx-detail').count(), 1, 'Detail direkt unter dem Thema');
    } else assert.ok(await page.locator('svg.mx-linien path').count() >= 1);
    await page.screenshot({ path: path.join(root, `test-results/lm-matrix-${breite}.png`), fullPage: breite < 1000 ? false : false });
  }
});

test('LM-5: „Als Matrix ansehen ›“ oben rechts in der Reiterzeile des Plans – 400/820/1280 sichtbar, ohne Querrollen', async (t) => {
  for (const breite of [400, 820, 1280]) {
    const { page } = await setup(t, { anpassen: echtAnpassen() }); await page.setViewportSize({ width: breite, height: 900 });
    await page.goto(origin + '/#/kind/1-plan');
    const l = page.getByRole('link', { name: 'Als Matrix ansehen ›' }); await l.waitFor();
    assert.equal(await page.locator('.lern-reiter a:not(.lern-plan-matrix-link)').count(), 4, 'vier Reiter');
    const r = await l.boundingBox(); const n = await page.locator('.lern-reiter').boundingBox();
    assert.ok(r.x + r.width <= n.x + n.width + 1 && r.x >= 0, `${breite}: im Bild`);
    assert.ok(await ohneQuerrollen(page), `${breite}: Querrollen`);
    await page.screenshot({ path: path.join(root, `test-results/lm-plan-link-${breite}.png`) });
  }
});

// LM-S-2-Format: Raster schule_lehrplan_matrix (knapp, Verbindungen als Tripel), Detail schule_lehrplan_thema. Lehrstoff aus der echten Themenliste,
// Verbindungen aus der Vorlage, Lernstand erfunden (Kind A, Kind B, Testkind).
// Eigenständiges Thema im Test: eines ohne Voraussetzung in den Verbindungen der Vorlage (die Vorlage des Gestalters ändert sich – 22.11.: 128 Verbindungen,
// seitdem braucht Thema 22 etwas; „Eigenständig …“ steht nur, wenn ein Thema keine Voraussetzung hat). Bevorzugt 42 (Geometrie).
const LMS_EIGEN = [42, ...THEMEN_ECHT.map((q) => q.thema_id)].find((id) => THEMEN_ECHT.some((q) => q.thema_id === id) && !MX_K.some((k) => k[0] === id));
const LMS_GEB = ['Zahlen', 'Algebra', 'Funktionen', 'Geometrie', 'Fläche und Raum', 'Geld und Verhältnisse', 'Daten und Zufall', 'Entdecker-Inseln'];
const lmsAnpassen = () => { const ueb = mxAnpassen(); const f = (aktion, e, daten = {}) => {
  if (!['schule_lehrplan_matrix', 'schule_lehrplan_thema'].includes(aktion)) return e ? ueb(aktion, e) : null;
  if (aktion === 'schule_lehrplan_thema') { const q = THEMEN_ECHT.find((x) => x.thema_id === daten.thema_id); if (!q) return null;
    const name = (id) => THEMEN_ECHT.find((x) => x.thema_id === id)?.titel;
    return { ok: true, thema_id: q.thema_id, titel: q.titel, kurz: 'kurz', ort: q.ort, was_gefordert: q.umfang, einheit_id: q.thema_id,
      merke: q.thema_id === 15 ? ['Der Wert einer Ziffer hängt von ihrer Stelle ab.'] : [], beispiel: q.thema_id === 15 ? 'Runde 4 567 891 auf Tausender.' : undefined,
      etappen: echteEtappen(q).map((x, i, a) => ({ lernziel: x.lernziel, titel: x.titel, pflicht: i < a.length - 1 })),
      braucht: MX_K.filter((k) => k[0] === q.thema_id).map((k) => ({ thema_id: k[1], titel: name(k[1]), art: k[2], begruendung: k[3] })),
      baut_darauf: MX_K.filter((k) => k[1] === q.thema_id).map((k) => ({ thema_id: k[0], titel: name(k[0]), art: k[2], begruendung: k[3] })),
      lehrplan: { gym_by: (q.lehrplan_gym || []).join(' · '), rs_by: (q.lehrplan_rs || []).join(' · ') }, ...(q.thema_id === LMS_EIGEN ? { eigenstaendig: 'Einstieg in die Geometrie, baut auf Grundschulwissen auf' } : {}) }; }
  const u = ueb('schule_lehrplan_uebersicht', { ok: true, kinder: [], themen: [] });
  const themen = THEMEN_ECHT.map((q) => { const t = u.themen.find((y) => y.thema_id === q.thema_id); const n = echteEtappen(q).length;
    return { thema_id: q.thema_id, schluessel: q.thema_schluessel, titel: q.titel, gebiet_id: LMS_GEB.indexOf(q.gebiet) + 1, block_id: q.block_id,
      ...(q.thema_id === 12 ? { ohne_flug: true } : { einheit_id: q.thema_id, etappen_anzahl: n }), jahrgang: q.klasse, lehrplan_reihenfolge: q.reihenfolge, lernbereich: q.lernbereich,
      pflicht: Object.keys(q.klasse).filter((s2) => s2 !== 'ib_myp'), ...(q.thema_id === LMS_EIGEN ? { eigenstaendig: true } : {}), _st: t.stufe }; });
  const lernstand = { 1: {}, 2: {} };
  for (const t of themen) { for (const k of [1, 2]) { const s2 = t._st[k]; if (!s2) continue; const { etappen, gesetzt, ...rest } = s2; // LM-S 2 lässt etappen und gesetzt weg
    lernstand[k][t.thema_id] = { ...rest, ...(k === 1 ? { fehler_offen: s2.stufe === 'dran' } : {}), ...(s2.stufe === 'dran' ? { etappe_jetzt: 3 } : {}) }; } delete t._st; }
  const kinder = [{ id: 1, name: 'Kind A', klasse: 8, schulart: 'gym_by' }, { id: 2, name: 'Kind B', klasse: 5, schulart: 'gym_by' }];
  return { ok: true, kindsicht: false, themen, verbindungen: MX_K.map(([a, b, art]) => [a, b, art === 'empfohlen' ? 'e' : 'h']),
    gebiete: LMS_GEB.map((titel, i) => ({ gebiet_id: i + 1, titel, reihenfolge: i + 1, zusatz: titel === 'Entdecker-Inseln' })),
    kinder: daten.mit_testkind ? [...kinder, { id: 9, name: 'Testkind', klasse: 7, schulart: 'rs_by' }] : kinder, lernstand: daten.mit_testkind ? { ...lernstand, 9: {} } : lernstand };
}; f.neueAktionen = true; return f; };

test('LM-S 2: Raster aus schule_lehrplan_matrix (Tripel, gebiet_id, etappen_anzahl), Detail über schule_lehrplan_thema – Begründungen, eigenständig, freiwillige Etappen, Fehler offen, ohne Flug, Testkind', async (t) => {
  const { page, calls } = await setup(t, { anpassen: lmsAnpassen() }); await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/lehrplan'); await page.locator('.mx-matrix').waitFor();
  assert.ok(calls.some((c) => c.aktion === 'schule_lehrplan_matrix') && calls.some((c) => c.aktion === 'schule_lehrplan_uebersicht'));
  assert.equal(await page.locator('.mx-chip').count(), THEMEN_ECHT.length);
  assert.deepEqual(await page.locator('.mx-geb').allInnerTexts(), LMS_GEB, 'Gebiet-Titel aus gebiete[]');
  assert.match(await page.locator('.mx-chip[data-id="12"]').getAttribute('class'), /mx-ohne/);
  const det = page.locator('.mx-detail');
  // Detail: nachgeladen, Begründungen aus braucht/baut_darauf, Linien aus den Tripeln
  await page.locator('.mx-chip[data-id="2"]').click();
  await det.getByText('Äquivalenzumformung baut auf einfachen Gleichungen auf').waitFor();
  assert.match(await page.locator('.mx-chip[data-id="1"]').getAttribute('class'), /mx-vor/);
  assert.ok(await page.locator('svg.mx-linien path').count() >= 3);
  assert.match(await det.innerText(), /DARAUF BAUT AUF[\s\S]*Einsetzen und Umformen linearer Gleichungen/i);
  assert.equal(calls.filter((c) => c.aktion === 'schule_lehrplan_thema' && c.daten.thema_id === 2).length, 1);
  await page.locator('.mx-chip[data-id="15"]').click();
  await det.getByText('Runde 4 567 891 auf Tausender.').waitFor();
  assert.match(await det.innerText(), /WAS GEFORDERT IST[\s\S]*DAS MUSS SITZEN[\s\S]*Stelle ab[\s\S]*SCHRITTE IN DER APP[\s\S]*freiwillig[\s\S]*IM LEHRPLAN[\s\S]*M5 1\.1/i);
  await page.locator(`.mx-chip[data-id="${LMS_EIGEN}"]`).click();
  await det.getByText(/Eigenständig: braucht keine Voraussetzung – Einstieg in die Geometrie/).waitFor();
  await page.locator('.mx-chip[data-id="2"]').click(); await det.getByText('Äquivalenzumformung baut auf einfachen Gleichungen auf').waitFor();
  assert.equal(calls.filter((c) => c.aktion === 'schule_lehrplan_thema' && c.daten.thema_id === 2).length, 1, 'Detail nur einmal geladen');
  // Lernstand: Etappe x von y mit y = etappen_anzahl; Fehler besprechen nur bei fehler_offen
  const ls = page.getByRole('group', { name: 'Lernstand' });
  await ls.getByRole('button', { name: 'Kind A' }).click();
  const dran = page.locator('.mx-chip.mx-dran').first(); await dran.waitFor();
  const dranId = Number(await dran.getAttribute('data-id'));
  const n = echteEtappen(THEMEN_ECHT.find((x) => x.thema_id === dranId)).length;
  assert.match(await dran.locator('.mx-stand').innerText(), new RegExp(`▶ Etappe 3 von ${n} · hier ist Kind A`));
  await dran.click(); await det.getByRole('link', { name: 'Fehler besprechen ›' }).waitFor();
  await ls.getByRole('button', { name: 'Kind B' }).click(); await page.locator('.mx-chip.mx-dran').first().click();
  await det.getByRole('link', { name: 'Im Plan öffnen ›' }).waitFor();
  assert.equal(await det.getByRole('link', { name: 'Fehler besprechen ›' }).count(), 0);
  // Testkind: aus seinem Plan geöffnet → mit_testkind
  await page.goto(origin + '/#/lehrplan/9'); await page.locator('.mx-matrix').waitFor();
  assert.ok(calls.some((c) => c.aktion === 'schule_lehrplan_matrix' && c.daten?.mit_testkind === true));
  assert.equal(await ls.getByRole('button', { name: 'Testkind' }).getAttribute('aria-pressed'), 'true');
  assert.equal(await page.getByRole('group', { name: 'Einordnen nach Schulart' }).getByRole('button', { name: 'Realschule' }).getAttribute('aria-pressed'), 'true');
});

test('LM: Filter „Inhalt“ (was fehlt noch?) – Zähler fertig / in Prüfung / fehlt, nicht passende Themen blass, mit Suche kombiniert', async (t) => {
  const { page } = await setup(t); await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto(origin + '/#/lehrplan'); await page.locator('.mx-matrix').waitFor();
  const g = page.getByRole('group', { name: 'Inhalt' });
  assert.deepEqual(await g.getByRole('button').allInnerTexts(), ['Alle', 'fertig 1', 'in Prüfung 1', 'fehlt 3']);
  await g.getByRole('button', { name: 'fehlt: 3' }).click();
  assert.deepEqual(await page.locator('.mx-chip:not(.mx-weg) .mx-titel').allInnerTexts(), ['Brüche addieren', 'Nur Realschule', 'Lineare Funktionen']);
  await page.getByLabel('Thema suchen').fill('Lineare');
  assert.deepEqual(await page.locator('.mx-chip:not(.mx-weg) .mx-titel').allInnerTexts(), ['Lineare Funktionen']);
  await page.getByLabel('Thema suchen').fill('');
  await g.getByRole('button', { name: 'in Prüfung: 1' }).click();
  assert.deepEqual(await page.locator('.mx-chip:not(.mx-weg) .mx-titel').allInnerTexts(), ['Teilbarkeit']);
  await g.getByRole('button', { name: 'Alle Themen' }).click();
  assert.equal(await page.locator('.mx-chip.mx-weg').count(), 0);
  for (const breite of [400, 820]) { await page.setViewportSize({ width: breite, height: 900 }); await page.locator('.mx-chip').first().waitFor();
    assert.deepEqual(await gebrocheneWoerter(g.getByRole('button')), [], `${breite}: Filter`); assert.ok(await ohneQuerrollen(page), `${breite}: Querrollen`); }
});

// ---------- Bau-Auftrag WD (22.11.) – App 0.85.0, angeglichen in 0.86.1 an die Vorgabe „abgelegt“ und WD-S 2 – erfundene Daten ----------
// Nachgebildeter Server WD-S 2: Runde fest je Lerntag, aufgaben[].pflicht, „gemacht“ setzt der Server, runde_fertig bestätigt nur.
const wdhServer = ({ runde = 9, faellig = 20, erledigt = 0, gemacht = false, neu = true, sterne_je = null } = {}) => {
  const s = { runde, faellig, erledigt, gemacht, aufrufe: [], fertig: 0 };
  s.route = async (route) => {
    const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion === 'schule_wiederholung') { s.aufrufe.push(b.daten);
      if (!neu) return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, faellig: s.faellig, aufgaben: wdhAufg(Math.min(b.daten.anzahl ? Math.min(b.daten.anzahl, 6) : 3, s.faellig)) } }) });
      const offen = s.gemacht ? 0 : s.runde - s.erledigt;
      const auf = [...wdhAufg(offen).map((a) => ({ ...a, pflicht: true })), ...wdhAufg(Math.max(0, s.faellig - s.runde)).map((a) => ({ ...a, pflicht: false }))];
      return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, faellig: s.faellig, runde: s.runde, runde_gemacht: s.gemacht, gestaffelt: 3, aufgaben: auf, ...(sterne_je ? { sterne_je_richtig: sterne_je } : {}) } }) }); }
    if (b.aktion === 'schule_wiederholung_runde_fertig') { s.fertig++; return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, runde_gemacht: s.gemacht } }) }); }
    if (b.aktion === 'schule_uebung_pruefen' && s.antwort) { const e = s.antwort(b.daten); if (e) { s.erledigt++; if (s.erledigt >= s.runde) s.gemacht = true;
      return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) }); } }
    if (b.aktion === 'schule_uebung_pruefen' && neu) { s.erledigt++; if (s.erledigt >= s.runde) s.gemacht = true; } // Server zählt jede beantwortete Pflicht-Bordkarte
    return route.fallback();
  };
  return s;
};
const wdhAufg = (n) => Array.from({ length: n }, (_, i) => ({ ...AUFG[11], einheit_id: 1, stadt: 'Rom', etappe: 'Welchen Wert hat eine Ziffer?', _i: i }));
const wdhAntworten = async (page, richtig = true) => { const tf = page.getByRole('group', { name: 'Tastenfeld' }); const z = richtig ? ['2', '0', '0', '0'] : ['9'];
  if (await tf.count()) { for (const c of z) await tf.getByRole('button', { name: c, exact: true }).click(); await tf.getByRole('button', { name: 'Prüfen' }).click(); }
  else { await page.locator('main input').first().fill(z.join('')); await page.getByRole('button', { name: 'Prüfen' }).click(); } };
const wdhRichtig = (page) => wdhAntworten(page, true);
const kofferZustand = (loc) => loc.evaluate((k) => [...k.querySelectorAll('.lr-koffer-p')].map((p) => [...p.querySelectorAll('i')].map((i) => i.className.replace(/lr-k-/g, '') || '-').join(',')));

test('WD/Vorgabe 1: Ansage „Vorher kurz einchecken“ – Bordkarten, Minuten, Koffer-Leiste (Päckchen bei 6, 9, 12), Startknopf „Weiter geht’s“, keine Rückstandszahl', async (t) => {
  for (const [runde, paeckchen] of [[6, ['-,-,-,-,-,-']], [9, ['-,-,-', '-,-,-', '-,-,-']], [12, ['-,-,-,-', '-,-,-,-', '-,-,-,-']]]) {
    const { page } = await setup(t, { gestaltung: 'nacht' }); const srv = wdhServer({ runde, faellig: 41 }); await page.route('**/functions/v1/lernen-api/**', srv.route);
    await page.goto(origin + '/#/reise/1');
    const ansage = page.locator('.lr-checkin-ansage'); await ansage.waitFor();
    assert.match(await ansage.innerText(), new RegExp(`Vorher kurz einchecken[\\s\\S]*${runde} Bordkarten von früher · etwa ${Math.ceil(runde / 2)} Minuten`));
    assert.deepEqual(await kofferZustand(ansage.locator('.lr-koffer')), paeckchen);
    assert.equal((await page.locator('.lr-einsteigen-knopf').innerText()).replace(/\s+/g, ' ').trim(), 'Weiter geht’s ›');
    assert.doesNotMatch(await page.locator('#main').innerText(), /41|Wiederholungen offen|warten noch/, 'keine Rückstandszahl, keine wartenden Etappen');
    assert.equal(srv.aufrufe[0].anzahl, undefined, 'ohne anzahl');
  }
});

test('WD/Vorgabe 2–3 + WD-S 2: Check-in „3 von 9“, Koffer gold/rötlich, +★ nur vom Server, unterbrechen und fortsetzen, „Eingecheckt!“, Extra-Bordkarten – 400/820/1280', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); const srv = wdhServer({ runde: 3, faellig: 9 }); await page.route('**/functions/v1/lernen-api/**', srv.route);
  let n = 0; srv.antwort = (dd) => { n++; const ok = n !== 2; return { ok: true, format_ok: true, richtig: ok, loesung: { wert: 2000 }, ...(ok ? { wiederholung: { bestanden: true, sterne: 10, naechste_in: 7 } } : {}) }; };
  await page.goto(origin + '/#/wiederholen/1');
  await page.getByText('CHECK-IN · 1 VON 3').waitFor();
  assert.match(await page.locator('.lr-checkin-herkunft').innerText(), /Welchen Wert hat eine Ziffer\? · aus Rom/);
  await wdhRichtig(page);
  await page.locator('.lr-plus-stern', { hasText: '+10 ★' }).waitFor();
  assert.deepEqual(await kofferZustand(page.locator('.lr-koffer')), ['ok,-,-']);
  // unterbrechen: Pause → Startseite zeigt „Check-in fortsetzen“ mit Stand; zurück geht es bei 2 von 3 weiter
  await page.getByRole('link', { name: 'Pause – später weiter einchecken' }).click();
  const ansage = page.locator('.lr-checkin-ansage'); await ansage.waitFor();
  assert.match(await ansage.innerText(), /Check-in fortsetzen[\s\S]*Noch 2 von 3 Bordkarten von früher · ganz kurz/);
  await page.goto(origin + '/#/wiederholen/1'); await page.getByText('CHECK-IN · 2 VON 3').waitFor();
  assert.deepEqual(await kofferZustand(page.locator('.lr-koffer')), ['da,jetzt,-']);
  await wdhAntworten(page, false);
  await page.getByText('Kein Problem – diese Bordkarte kommt beim nächsten Mal wieder.').waitFor();
  assert.equal(await page.locator('.lr-plus-stern').count(), 0, 'falsch: keine Sterne');
  assert.deepEqual(await kofferZustand(page.locator('.lr-koffer')), ['da,nein,-']);
  await page.getByRole('button', { name: 'Nächste Bordkarte ›' }).click(); await page.getByText('CHECK-IN · 3 VON 3').waitFor();
  await wdhRichtig(page); await page.getByRole('button', { name: 'Fertig ›' }).click();
  await page.getByRole('heading', { name: 'Eingecheckt!' }).waitFor();
  assert.match(await page.locator('.lr-checkin-fertig').innerText(), /1 von 2 richtig · \+10 ★[\s\S]*Eine Bordkarte kommt beim nächsten Mal wieder\.[\s\S]*Weiter nach Rom ›[\s\S]*Noch 3 Extra-Bordkarten\?/);
  assert.equal(srv.fertig, 1, 'runde_fertig nur zum Bestätigen'); assert.equal(srv.gemacht, true, 'der Server hat selbst gesetzt');
  assert.equal(await page.evaluate(() => localStorage.getItem('lern.wdhrunde.1')), null, 'kein Merker auf dem Gerät');
  // gemacht → Startseite ohne Ansage, Startknopf ins Thema, Extra freiwillig (höchstens 3)
  await page.goto(origin + '/#/reise/1'); await page.locator('.lr-einsteigen-knopf').waitFor();
  assert.equal((await page.locator('.lr-einsteigen-knopf').innerText()).replace(/\s+/g, ' ').trim(), 'Weiter nach Rom ›');
  assert.equal(await page.locator('.lr-checkin-ansage').count(), 0);
  await page.getByRole('link', { name: 'Noch 3 Extra-Bordkarten?' }).click();
  await page.getByText('EXTRA · 1 VON 3').waitFor();
  for (const breite of [400, 820, 1280]) { await page.setViewportSize({ width: breite, height: 900 });
    assert.ok(await ohneQuerrollen(page), `${breite}: Querrollen`); assert.deepEqual(await gebrocheneWoerter(page.locator('.lr-checkin-kopf span, .lr-checkin-sterne')), [], `${breite}`); }
});

test('WD: alter Server (ohne runde) – wie 0.84.0: fragt einmal mit 6 nach, Merker auf dem Gerät, kein runde_fertig, kein Check-in', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); const srv = wdhServer({ neu: false, faellig: 8 }); await page.route('**/functions/v1/lernen-api/**', srv.route);
  await page.goto(origin + '/#/reise/1'); await page.locator('.lr-einsteigen-knopf').waitFor();
  assert.equal((await page.locator('.lr-einsteigen-knopf').innerText()).replace(/\s+/g, ' ').trim(), 'Erst 6 Wiederholungen ›');
  assert.deepEqual(srv.aufrufe.map((x) => x.anzahl), [undefined, 6]);
  await page.goto(origin + '/#/wiederholen/1'); await page.getByText('WIEDERHOLEN 1 VON 6', { exact: false }).waitFor();
  assert.equal(await page.locator('.lr-checkin-kopf, .lr-koffer').count(), 0);
  for (let i = 0; i < 6; i++) { await wdhRichtig(page); await page.getByRole('button', { name: i < 5 ? 'Nächste' : 'Fertig', exact: true }).click(); }
  await page.getByRole('heading', { name: '6 von 6 richtig' }).waitFor();
  assert.equal(srv.fertig, 0); assert.equal(await page.evaluate(() => lernWdhHeute(1)), true);
});

test('WD-6/Vorgabe 4–5: „Etappe abgelegt“ (Blatt unten auf dem Handy, Karte ab 760, Ticket, Siegel, +30, Flug-Fortschritt, „Weiter einchecken“) und „Flug abgelegt“ (ganzer Bildschirm, ohne Etappen-Blatt, 360×640 ohne Scrollen)', async (t) => {
  for (const [breite, hoehe] of [[360, 640], [400, 860], [820, 1180], [1280, 900]]) {
    const { page } = await setup(t, { gestaltung: 'nacht' }); await page.setViewportSize({ width: breite, height: hoehe });
    const srv = wdhServer({ runde: 2, faellig: 2 }); await page.route('**/functions/v1/lernen-api/**', srv.route);
    let n = 0; srv.antwort = () => { n++; return { ok: true, format_ok: true, richtig: true, loesung: { wert: 2000 }, wiederholung: { bestanden: true, sterne: 10 },
      abgelegt: n === 1 ? { etappe: { titel: 'Welchen Wert hat eine Ziffer?', sterne: 30, flug: 'Natürliche Zahlen', etappen_abgelegt: 4, etappen: 7 } }
        : { etappe: { titel: 'Zahlenstrahl', sterne: 30 }, flug: { titel: 'Natürliche Zahlen', sterne: 100, etappen: 7 }, ort_gold: true, ort: 'Rom' } }; };
    await page.goto(origin + '/#/wiederholen/1'); await wdhRichtig(page);
    const klein = page.getByRole('dialog', { name: 'Etappe abgelegt' }); await klein.waitFor();
    assert.match(await klein.innerText(), /ABGELEGT[\s\S]*Etappe abgelegt![\s\S]*Welchen Wert hat eine Ziffer\?[\s\S]*5-mal wiederholt, über 30 Lerntage\. Raus aus der regelmäßigen Wiederholung – nur noch bei Bedarf zum Auffrischen\.[\s\S]*\+30 ★[\s\S]*Sonder-Sterne fürs Ablegen[\s\S]*Natürliche Zahlen: 4 von 7 Etappen abgelegt – noch 3, dann wird der Flug golden\./);
    await klein.click({ position: { x: 5, y: 5 } }); await page.waitForTimeout(100); // Antippen beendet die Bewegung
    const box = await klein.locator('.lr-ab-abgelegt-klein').boundingBox();
    if (breite < 760) assert.ok(Math.abs(box.y + box.height - hoehe) < 2 && box.height <= hoehe * 0.75 + 1, `${breite}: Blatt von unten`);
    else assert.ok(box.width <= 520 && box.y > 10 && box.y + box.height < hoehe - 10, `${breite}: Karte in der Mitte`);
    assert.equal(await klein.locator('.lr-goldbalken span.g').count(), 4);
    assert.deepEqual(await gebrocheneWoerter(klein.locator('.lr-ab-titel, .lr-ab-ticket small, .lr-ab-flugfort, .lr-ab-gross-text')), [], `${breite}: Etappe`);
    await page.screenshot({ path: path.join(root, `test-results/wd-etappe-abgelegt-${breite}.png`) });
    await klein.getByRole('button', { name: /^Weiter einchecken/ }).click(); await klein.waitFor({ state: 'detached' });
    await page.getByRole('button', { name: 'Nächste Bordkarte ›' }).click(); await wdhRichtig(page);
    const gross = page.getByRole('dialog', { name: 'Flug abgelegt' }); await gross.waitFor();
    assert.equal(await page.getByRole('dialog', { name: 'Etappe abgelegt' }).count(), 0, 'Etappen-Blatt entfällt');
    await gross.locator('.lr-ab-szene').click({ position: { x: 20, y: 120 } }); await page.waitForTimeout(150); // Endzustand
    assert.match(await gross.innerText(), /ALLE ETAPPEN ABGELEGT[\s\S]*FLUG ABGELEGT![\s\S]*Alle 7 Etappen von Natürliche Zahlen sind abgelegt\. Im Reisepass ist der Flug jetzt golden\.[\s\S]*\+100 ★[\s\S]*für den ganzen Flug[\s\S]*\+30 ★ für die letzte Etappe[\s\S]*Alle Flüge in Rom sind abgelegt\. Dein Stempel ist jetzt golden!/i);
    assert.equal(await gross.locator('.lr-wird-gold').count(), 1);
    const knopf = await gross.getByRole('button', { name: /^Weiter/ }).last().boundingBox();
    assert.ok(knopf.y + knopf.height <= hoehe, `${breite}×${hoehe}: ohne Scrollen`);
    assert.deepEqual(await gebrocheneWoerter(gross.locator('.lr-ab-gtitel, .lr-ab-gunter, .lr-ab-ortgold, .lr-ab-leise')), [], `${breite}: Flug`);
    await page.screenshot({ path: path.join(root, `test-results/wd-flug-abgelegt-${breite}.png`) });
    await gross.getByRole('button', { name: /^Weiter/ }).last().click(); await page.locator('.lr-abschluss').waitFor({ state: 'detached' });
    await page.getByRole('button', { name: 'Fertig ›' }).click();
    assert.match(await page.locator('.lr-checkin-ergebnis').innerText(), /2 von 2 richtig · \+180 ★/, 'Summe inkl. 30/100');
  }
});

test('WD-3: Mischkarte aus einer fälligen Etappe zählt als bestandene Wiederholung – sichtbar mit Sternen', async (t) => {
  const misch = (aktion, e) => {
    if (aktion !== 'schule_einheit_lesen') return null; const x = neueRegel({ strahl: { sitzt: true } })(aktion, e);
    x.mischkarten = [{ ...zeig(AUFG[14]), stufe: 2, einheit_id: 2, quelle: 'aelter', stadt: 'New York', etappe: 'Große Zahlen lesen' }]; x.misch_jede = 1; x.misch_ab = 1; return x; };
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: misch });
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion !== 'schule_uebung_pruefen' || !b.daten?.misch) return route.fallback();
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, format_ok: true, richtig: true, loesung: AUFG[14].loesung,
      misch: { etappe: 'Große Zahlen lesen', stadt: 'New York', ok: true }, wiederholung: { bestanden: true, sterne: 5, stufe_neu: 'wiederholung', naechste_in: 14 } } }) });
  });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1');
  await page.getByText('BORDKARTE 1 · AUS DEINER REISE').waitFor();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('↻ Zählt als Wiederholung dieser Etappe').waitFor();
  assert.match(await page.locator('.lr-rueck-ok b').first().innerText(), /\+5 Sterne/i, '0.86.2: nur was der Server meldet (hier wiederholung.sterne 5), keine eigenen +10');
});


test('WD-6/Vorgabe 6: Reisepass – Flüge golden („★ ABGELEGT“), teilweise mit Gold-Leiste, „noch nichts abgelegt“, Stempel „★ GOLD ★“, Satz „Gold heißt …“; ohne Felder wie bisher', async (t) => {
  const gold = (aktion, e) => { if (aktion !== 'schule_konto') return null; const x = structuredClone(e);
    x.konto.orte = [{ block_id: 49, abgeschlossen: true, gold: true, themen: 1, erledigt: 1 }];
    x.konto.fluege = [{ thema_id: 3, einheit_id: 2, titel: 'Zinsen', abgelegt: false, etappen_abgelegt: 1, etappen: 2 }, { thema_id: 1, einheit_id: 1, titel: 'Natürliche Zahlen', abgelegt: true, etappen_abgelegt: 3, etappen: 3 },
      { thema_id: 5, einheit_id: 9, titel: 'Brüche', abgelegt: false, etappen_abgelegt: 0, etappen: 4 }];
    return x; };
  for (const breite of [400, 820, 1280]) {
    const { page } = await setup(t, { gestaltung: 'nacht', anpassen: gold }); await page.setViewportSize({ width: breite, height: 900 });
    await page.goto(origin + '/#/reisepass/1');
    const st = page.locator('.lr-stempel.lr-stempel-gold'); await st.waitFor();
    assert.match(await st.innerText(), /ROM[\s\S]*★ GOLD ★/i);
    const e = page.locator('.lr-flug-eintrag');
    assert.deepEqual(await e.allInnerTexts().then((l) => l.map((x) => x.replace(/\s+/g, ' ').trim())),
      ['✈ Natürliche Zahlen Rom · alle Etappen abgelegt ★ ABGELEGT', '✈ Zinsen New York 1 von 2 abgelegt', '✈ Brüche noch nichts abgelegt']);
    assert.equal(await e.nth(1).locator('.lr-mini-gold i.g').count(), 1);
    await page.getByText('Gold heißt: Alle Etappen sind abgelegt.').waitFor();
    assert.deepEqual(await gebrocheneWoerter(page.locator('.lr-flug-eintrag b, .lr-flug-eintrag small, .lr-flug-rechts, .lr-stempel b')), [], `${breite}`);
    assert.ok(await ohneQuerrollen(page), `${breite}: Querrollen`);
    await page.locator('.lr-pass-fluege').screenshot({ path: path.join(root, `test-results/wd-reisepass-${breite}.png`) });
  }
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.goto(origin + '/#/reisepass/1'); await page.getByRole('heading', { name: 'Stempel' }).waitFor();
  assert.equal(await page.locator('.lr-pass-fluege, .lr-stempel-gold').count(), 0);
});

test('WD: Info-Seite (Eltern) und Kindertext – Check-in, unterbrechen, abgelegt, Gold, Rückfall; Kindertext ohne „fällig“, „endgültig“, „Stufe“', async (t) => {
  const { page } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.goto(origin + '/lernen/#/info'); await page.getByRole('heading', { name: 'Erste Schritte' }).waitFor();
  await page.evaluate(() => document.querySelectorAll('details').forEach((d) => { d.open = true; }));
  const text = (await page.locator('#main').innerText()).replace(/\s+/g, ' ');
  for (const s of ['sonst ein Fünftel der fälligen (aufgerundet), mindestens 6 und höchstens 12 (bis Klasse 6 höchstens 10)', 'Auf der Kinderseite heißt die Runde „Check-in“',
    'nie die Zahl aller fälligen Etappen', 'auch auf einem anderen Gerät', 'Endgültig abgelegt:', 'der Flug steht im Reisepass golden', 'wird auch der Stempel des Orts golden',
    'kommt sie am nächsten Lerntag wieder zur Wiederholung; Gold und Sterne bleiben', 'zählt sie als bestandene Wiederholung dieser Etappe', 'Wiederholungen bringen 10 ★, wenn sie selbst gelöst sind',
    'je Lerntag kommen höchstens 6 solche Etappen neu in den Takt'])
    assert.ok(text.includes(s), 'fehlt: ' + s);
  const kind = await page.evaluate(() => lernWdhErklaert(true).textContent);
  assert.doesNotMatch(kind, /fällig|endgültig|Stufe|Takt/); assert.match(kind, /checkst du kurz ein/);
});

// ---------- Bau-Auftrag LM, Schritt 3: LM-6 Kinderseite „Meine Route 5–10“ (0.86.0) – erfundene Daten, Testkind ----------
const rtMock = ({ kindsicht = true, ohne = false } = {}) => async (route) => {
  const b = JSON.parse(route.request().postData() || '{}');
  if (!['schule_lehrplan_matrix', 'schule_lehrplan_thema'].includes(b.aktion)) return route.fallback();
  const antw = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
  if (ohne) return antw(undefined); // alter Server: Aktion unbekannt
  const f = lmsAnpassen();
  if (b.aktion === 'schule_lehrplan_thema') {
    const t = f('schule_lehrplan_thema', null, b.daten); const { lehrplan, eigenstaendig, ...rest } = t;
    if (b.daten.thema_id === 1) rest.etappen = ETAPPEN.map((x) => ({ lernziel: x.lernziel, titel: x.titel })); // Merkheft (Einheit 1): stellenwert, strahl gelandet
    return antw({ ...rest, kindsicht: true, braucht: rest.braucht.map(({ begruendung, ...x }) => x), baut_darauf: rest.baut_darauf.map(({ begruendung, ...x }) => x) });
  }
  const r = f('schule_lehrplan_matrix', null, {});
  r.lernstand = { 1: r.lernstand[1] };
  if (!kindsicht) { r.kinder = [r.kinder[0], { id: 2, name: 'Kind B', klasse: 5, schulart: 'gym_by' }]; return antw(r); } // Eltern sehen die Seite des Kindes: Lehrer-Sicht
  r.kinder = [{ id: 1, name: 'Kind A', klasse: 8 }];
  r.themen = r.themen.map(({ jahrgang, lehrplan_reihenfolge, lernbereich, pflicht, eigenstaendig, ...t }) => ({ ...t,
    zeile: jahrgang.gym_by ? { klasse: jahrgang.gym_by } : jahrgang.rs_by ? { klasse: jahrgang.rs_by, eingeordnet: true } : jahrgang.ib_myp ? { klasse: jahrgang.ib_myp + 5, eingeordnet: true } : { eingeordnet: true },
    reihenfolge_kind: lehrplan_reihenfolge.gym_by }));
  return antw({ ...r, kindsicht: true });
};

test('LM-6: Kinderseite „Meine Route 5–10“ – Link auf der Abflugtafel, nur das eigene Kind, Stufen in Kinder-Sprache, Kopf je Klasse, Reisewörter', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); await page.setViewportSize({ width: 1280, height: 900 });
  await page.route('**/functions/v1/lernen-api/**', rtMock());
  await page.goto(origin + '/#/reise/1');
  await page.getByRole('link', { name: 'Meine Route 5–10 ›' }).click();
  await page.waitForURL(/#\/route\/1$/);
  await page.getByRole('heading', { name: 'Deine Route durch die Mathe-Welt' }).waitFor();
  const chips = page.locator('.rt-chip'); await chips.first().waitFor();
  assert.equal(await chips.count(), THEMEN_ECHT.length, 'alle Flüge');
  assert.equal(await page.locator('.mx-sch, .mx-leiste, [aria-label="Lernstand"], .lern-lp-stufe-knopf').count(), 0, 'keine Kennzeichen, keine Leiste, nichts zum Ändern');
  const dran = page.locator('.rt-chip.mx-dran').first();
  assert.match(await dran.locator('.mx-stand').innerText(), /^▶ hier bist du – Etappe 3 von \d+$/);
  assert.ok(await dran.evaluate((x) => { const r = x.getBoundingClientRect(); return r.top >= 0 && r.bottom <= innerHeight; }), 'zum ▶-Flug gescrollt');
  assert.match(await page.locator('.rt-chip.st-1 .mx-stand').first().innerText(), /^◉ kannst du$/);
  assert.match(await page.locator('.rt-chip.st-2 .mx-stand').first().innerText(), /^↻ kommt zur Wiederholung$/);
  const blass = page.locator('.rt-chip.rt-blass').first(); assert.equal(await blass.locator('.mx-stand').count(), 0, 'nicht im Plan: ohne Text');
  assert.match(await page.locator('.mx-kl').nth(3).innerText(), /Kl\. 8[\s\S]*Du kannst schon \d+ von \d+ Flügen/);
  assert.deepEqual(await page.locator('.mx-geb').allInnerTexts(), LMS_GEB, 'Spalten = Kontinente');
  // Reisewörter: keine Lehrer-Wörter auf der Kinderseite (Flug-Titel und Kontinent-Namen aus der Datenbank ausgenommen)
  const text = await page.evaluate(() => { const c = document.querySelector('#main').cloneNode(true); c.querySelectorAll('.mx-titel, .mx-geb, .rt-ort').forEach((x) => x.remove()); return c.innerText; });
  assert.doesNotMatch(text, /Thema|Themen|Lernkarte|Aufgabe|Lehrplan|Gymnasium|Realschule|Pflicht|Lernbereich/);
});

test('LM-6: Detail eines Flugs – was du lernst, muss sitzen, brauchst du vorher (mit eigener Stufe), danach, Etappen mit ✓; „Weiter lernen ›“ nur beim ▶-Flug', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); await page.setViewportSize({ width: 1280, height: 900 });
  await page.route('**/functions/v1/lernen-api/**', rtMock());
  await page.goto(origin + '/#/route/1'); await page.locator('.rt-chip').first().waitFor();
  const det = page.locator('.rt-detail');
  await page.locator('.rt-chip[data-id="15"]').click();
  await det.getByText('Der Wert einer Ziffer hängt von ihrer Stelle ab.').waitFor();
  assert.match(await det.innerText(), /WAS DU HIER LERNST[\s\S]*DAS MUSS SITZEN/i);
  // Voraussetzungen und Nachfolger mit eigener Stufe
  await page.locator('.rt-chip[data-id="2"]').click();
  await det.getByRole('heading', { name: 'Das brauchst du vorher' }).waitFor();
  assert.ok(await det.locator('.rt-verweise .rt-zeichen').count() >= 2);
  assert.match(await det.innerText(), /DANACH GEHT’S WEITER MIT/i);
  assert.match(await page.locator('.rt-chip[data-id="1"]').getAttribute('class'), /mx-vor/);
  assert.ok(await page.locator('svg.mx-linien path').count() >= 2, 'Linien wie LM-3');
  assert.equal(await det.getByRole('link', { name: 'Weiter lernen ›' }).count(), 0, 'kein Lern-Knopf außer beim ▶-Flug');
  // Etappen mit ✓ für gelandete Etappen (Merkheft)
  await page.locator('.rt-chip[data-id="1"]').click();
  await det.locator('.rt-etappen li').first().waitFor();
  assert.deepEqual(await det.locator('.rt-etappen .rt-haken').evaluateAll((l) => l.map((x) => x.textContent)), ['✓', '✓', ''].concat(Array(ETAPPEN.length - 3).fill('')));
  // ▶-Flug: großer Knopf öffnet die nächste Etappe
  const dran = page.locator('.rt-chip.mx-dran').first(); const id = await dran.getAttribute('data-id'); await dran.click();
  const w = det.getByRole('link', { name: 'Weiter lernen ›' }); await w.waitFor();
  assert.equal(await w.getAttribute('href'), `#/lerneinheit/1-${id}-ueben`);
  assert.doesNotMatch(await det.innerText(), /Lehrplan|LehrplanPLUS|M\d \d|weil /, 'kein Wortlaut, keine Begründung');
});

test('LM-6 Abnahme: 400, 820, 1280 – Liste auf Handy und Tablet (Detail unter dem Flug, keine Linien), Matrix mit Linien ab 1000 px, nichts läuft über, kein Querrollen; hell und Nacht', async (t) => {
  for (const g of ['nacht', 'tag']) for (const breite of [400, 820, 1280]) {
    const { page } = await setup(t, { gestaltung: g }); await page.setViewportSize({ width: breite, height: breite < 760 ? 860 : 900 });
    await page.route('**/functions/v1/lernen-api/**', rtMock());
    await page.goto(origin + '/#/route/1'); await page.locator('.rt-chip').first().waitFor();
    assert.deepEqual(await ueberlaeuft(page.locator('.rt-chip, .rt-chip > span, .mx-geb, .mx-kl, .mx-liste-kopf, .rt-legende span')), [], `${g} ${breite}: überläuft`);
    assert.deepEqual(await gebrocheneWoerter(page.locator('.mx-stand, .rt-kann, .rt-legende span, .rt-ort')), [], `${g} ${breite}: gebrochene Wörter`);
    assert.ok(await ohneQuerrollen(page), `${g} ${breite}: Querrollen`);
    await page.locator('.rt-chip.mx-dran').first().click(); await page.locator('.rt-detail h2').waitFor();
    if (breite < 1000) { assert.equal(await page.locator('.mx-matrix, svg.mx-linien').count(), 0); assert.equal(await page.locator('.rt-chip.mx-dran + .rt-detail').count(), 1, 'Detail unter dem Flug'); }
    else assert.ok(await page.locator('svg.mx-linien path').count() >= 1, 'Linien');
    assert.deepEqual(await gebrocheneWoerter(page.locator('.rt-detail h3, .rt-stand, .rt-weiter')), [], `${g} ${breite}: Detail`);
    assert.ok(await ohneQuerrollen(page), `${g} ${breite}: Querrollen mit Detail`);
    if (g === 'nacht' || breite === 400) await page.screenshot({ path: path.join(root, `test-results/lm6-route-${g}-${breite}.png`) });
  }
});

test('LM-6: Eltern öffnen die Seite des Kindes (Lehrer-Sicht) – Zeile aus Klasse und Schulart, nur das eigene Kind; ohne LM-S ein Hinweis', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); await page.setViewportSize({ width: 1280, height: 900 });
  await page.route('**/functions/v1/lernen-api/**', rtMock({ kindsicht: false }));
  await page.goto(origin + '/#/route/1'); await page.locator('.rt-chip').first().waitFor();
  assert.equal(await page.locator('.rt-chip').count(), THEMEN_ECHT.length);
  const g8 = THEMEN_ECHT.find((x) => x.klasse.gym_by === 8);
  assert.equal(await page.locator('.mx-zelle').nth(3 * LMS_GEB.length + LMS_GEB.indexOf(g8.gebiet)).locator(`.rt-chip[data-id="${g8.thema_id}"]`).count(), 1, 'Gym 8 in Zeile Klasse 8');
  assert.equal(await page.getByText('Kind B').count(), 0, 'kein Geschwister');
  const { page: p2 } = await setup(t, { gestaltung: 'nacht' });
  await p2.route('**/functions/v1/lernen-api/**', rtMock({ ohne: true }));
  await p2.goto(origin + '/#/route/1'); await p2.getByText('Die Route ist bald da.').waitFor();
});

test('Nachprüfung N1: Matrix am Rechner – ohne gewähltes Thema volle Breite (keine Detail-Spalte), Detail-Spalte erst beim Antippen; Spalten breiter als vorher', async (t) => {
  const { page } = await mxOeffnen(t, 1280);
  const breite = () => page.locator('.mx-zelle').first().evaluate((x) => x.getBoundingClientRect().width);
  assert.equal(await page.locator('.mx-detail').isVisible(), false, 'keine leere Detail-Spalte');
  const ohne = await breite();
  assert.ok(ohne >= 125, `Spalte ${ohne} px (vorher rund 95)`);
  await page.locator('.mx-chip[data-id="2"]').click();
  await page.locator('.mx-detail h2').waitFor();
  assert.ok(await page.locator('.mx-haupt').evaluate((x) => getComputedStyle(x).gridTemplateColumns.split(' ').length) === 2, 'Detail als Spalte');
  await page.locator('.mx-chip[data-id="2"]').click();
  assert.equal(await page.locator('.mx-detail').isVisible(), false);
  assert.ok(await ohneQuerrollen(page));
});

test('WD: „weniger Bewegung“ – Einblendungen zeigen sofort den Endzustand (+100 ★)', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(origin + '/#/reise/1'); await page.locator('.lr-einsteigen-knopf').waitFor();
  await page.evaluate(() => { lernAbgelegtZeigen({ id: 1 }, { etappe: { titel: 'A', sterne: 30 }, flug: { titel: 'B', sterne: 100, etappen: 3 } }); });
  const g = page.getByRole('dialog', { name: 'Flug abgelegt' }); await g.waitFor();
  assert.equal(await g.locator('[data-ziel]').innerText(), '100');
  assert.equal(await g.locator('.lr-ab-strahlen').evaluate((x) => getComputedStyle(x).animationName), 'none');
});

// ---------- 0.86.2: Fehler Mischkarten (22.11.) und ChatGPT 919 – erfundene Daten ----------
const mischDrei = (aktion, e) => {
  if (aktion !== 'schule_einheit_lesen') return null; const x = neueRegel({ strahl: { sitzt: true } })(aktion, e);
  x.mischkarten = [{ ...zeig(AUFG[14]), stufe: 2, einheit_id: 2, quelle: 'flug', stadt: 'New York', etappe: 'Große Zahlen lesen' },
    { ...zeig(AUFG[11]), stufe: 2, einheit_id: 2, quelle: 'flug', stadt: 'New York', etappe: 'Stellenwert' },
    { ...zeig(AUFG[13]), stufe: 2, einheit_id: 2, quelle: 'kontinent', stadt: 'Paris', etappe: 'Ausmultiplizieren' }];
  x.misch_jede = 1; x.misch_ab = 1; return x; };

test('0.86.2: drei Etappen nacheinander – keine Mischkarte doppelt; leere Liste einmal neu vom Server, danach ohne Mischkarte', async (t) => {
  const { page, calls } = await setup(t, { gestaltung: 'nacht', anpassen: mischDrei });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1');
  const frage = async () => { await page.locator('.lr-bordkarte, .lr-trotzdem').first().waitFor();
    if (await page.locator('.lr-trotzdem').count()) await page.locator('.lr-trotzdem').click(); // gelandete Etappe: „Trotzdem weiterüben“
    await page.locator('.lr-bordkarte').first().waitFor(); return { misch: await page.getByText(/AUS DEINER REISE/).count() > 0, text: await page.locator('.lr-bordkarte').first().innerText() }; };
  const gezeigt = [];
  for (let i = 0; i < 3; i++) {
    const f = await frage(); assert.ok(f.misch, `Etappe ${i + 1}: Mischkarte`); gezeigt.push(f.text.replace(/BORDKARTE \d+ · /, ''));
    await page.getByRole('button', { name: 'Nächste Etappe' }).last().click().catch(() => page.getByRole('button', { name: 'Vorige Etappe' }).last().click());
  }
  assert.equal(new Set(gezeigt).size, 3, 'keine Mischkarte doppelt: ' + gezeigt.map((x) => x.slice(0, 40)).join(' | '));
  const lesen = calls.filter((c) => c.aktion === 'schule_einheit_lesen').length;
  // Liste leer: einmal neu holen (der Server liefert hier dieselben drei – sie bleiben verbraucht), dann ohne Mischkarte
  await page.getByRole('button', { name: 'Vorige Etappe' }).last().click();
  const f4 = await frage(); assert.equal(f4.misch, false, 'keine vierte Mischkarte');
  await page.waitForTimeout(200);
  assert.equal(calls.filter((c) => c.aktion === 'schule_einheit_lesen').length, lesen + 1, 'einmal nachgeladen');
  await page.getByRole('button', { name: 'Nächste Etappe' }).last().click();
  assert.equal((await frage()).misch, false);
  assert.equal(calls.filter((c) => c.aktion === 'schule_einheit_lesen').length, lesen + 1, 'nicht ein zweites Mal');
});

test('0.86.2: Sterne nur vom Server; misch.gueltig false ohne Lob als Wiederholung; bestanden false nach Hilfe „Richtig – morgen noch einmal ohne Hilfe“', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: mischDrei });
  let antwort = null;
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion !== 'schule_uebung_pruefen' || !b.daten?.misch || !antwort) return route.fallback();
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, format_ok: true, richtig: true, loesung: AUFG[14].loesung, ...antwort } }) });
  });
  // ungültige Ausgabe: kein „Das war …“, keine Wiederholung, Sterne laut Server 0
  antwort = { misch: { gueltig: false }, sterne: 0 };
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText('BORDKARTE 1 · AUS DEINER REISE').waitFor();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click(); await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.locator('.lr-rueck-ok').waitFor();
  assert.doesNotMatch(await page.locator('main').innerText(), /Das war:|Zählt als Wiederholung|\+10|STERNE/i);
  // richtig mit Hilfe: freundlich, keine Wiederholungs-Sterne
  antwort = { misch: { etappe: 'Große Zahlen lesen', stadt: 'New York', ok: false }, wiederholung: { bestanden: false, sterne: 0 }, sterne: 0 };
  await page.goto(origin + '/#/reise/1'); await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText('BORDKARTE 1 · AUS DEINER REISE').waitFor();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click(); await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig – morgen noch einmal ohne Hilfe.').waitFor();
  assert.doesNotMatch(await page.locator('.lr-rueck-ok').innerText(), /Sterne/i);
  // gültig und bestanden: Sterne genau wie gebucht
  antwort = { misch: { etappe: 'Große Zahlen lesen', stadt: 'New York', ok: true }, wiederholung: { bestanden: true, sterne: 10 }, sterne: 10 };
  await page.goto(origin + '/#/reise/1'); await page.goto(origin + '/#/lerneinheit/1-1-ueben-1'); await page.getByText('BORDKARTE 1 · AUS DEINER REISE').waitFor();
  await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click(); await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('↻ Zählt als Wiederholung dieser Etappe').waitFor();
  assert.match(await page.locator('.lr-rueck-ok b').first().innerText(), /\+10 STERNE/i, 'nicht 20');
});

test('0.86.2: Check-in – richtig mit Hilfe (bestanden false) freundlich, Koffer hell ohne Stern, keine Sterne', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); const srv = wdhServer({ runde: 2, faellig: 2 }); await page.route('**/functions/v1/lernen-api/**', srv.route);
  srv.antwort = () => ({ ok: true, format_ok: true, richtig: true, loesung: { wert: 2000 }, wiederholung: { bestanden: false, sterne: 0 } });
  await page.goto(origin + '/#/wiederholen/1'); await wdhRichtig(page);
  await page.getByText('Richtig – morgen noch einmal ohne Hilfe.').waitFor();
  assert.equal(await page.locator('.lr-plus-stern').count(), 0);
  assert.deepEqual(await kofferZustand(page.locator('.lr-koffer')), ['hilfe,-']);
});

// ---------- 0.86.3: Nachtrag WD-S 4 (ChatGPT 921), Teil bau-motivation – erfundene Daten ----------
test('0.86.3: Runde gemacht, noch fällig, aber keine wählbare frische Aufgabe – kein Angebot „Extra“, sondern „bleibt für später offen“', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' });
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion !== 'schule_wiederholung') return route.fallback();
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, faellig: 4, runde: 6, runde_gemacht: true, gestaffelt: 0, aufgaben: [] } }) });
  });
  await page.goto(origin + '/#/reise/1');
  for (const g of ['nacht', 'alt']) {
    await page.evaluate((x) => localStorage.setItem('lern.gestaltung.1', x), g);
    await page.reload(); await page.getByText('Heute keine passende frische Aufgabe – bleibt für später offen.').waitFor();
    assert.equal(await page.getByText(/Noch 3 Extra-Bordkarten/).count(), 0, g);
  }
  await page.goto(origin + '/#/wiederholen/1-extra');
  await page.getByText('Heute keine passende frische Aufgabe – bleibt für später offen.').waitFor();
  // Check-in fertig, Rest ohne frische Aufgabe: dasselbe statt „Extra“
  await page.unrouteAll({ behavior: 'ignoreErrors' });
  const { page: p2 } = await setup(t, { gestaltung: 'nacht' });
  await p2.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion === 'schule_wiederholung_runde_fertig') return route.fulfill({ contentType: 'application/json', body: '{"ok":true,"ergebnis":{"ok":true}}' });
    if (b.aktion !== 'schule_wiederholung') return route.fallback();
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, faellig: 5, runde: 1, runde_gemacht: false, aufgaben: wdhAufg(1).map((a) => ({ ...a, pflicht: true })) } }) });
  });
  await p2.goto(origin + '/#/wiederholen/1'); await wdhRichtig(p2); await p2.getByRole('button', { name: 'Fertig ›' }).click();
  await p2.getByRole('heading', { name: 'Eingecheckt!' }).waitFor();
  await p2.getByText('Heute keine passende frische Aufgabe – bleibt für später offen.').waitFor();
  assert.equal(await p2.getByText(/Noch 3 Extra-Bordkarten/).count(), 0);
});

test('0.86.3: kein „für immer“ mehr – Siegel und Einblendungen „ABGELEGT“; Wiederholung mit Hilfe zeigt 0 Sterne laut Server', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); await page.goto(origin + '/#/reise/1'); await page.locator('.lr-einsteigen-knopf').waitFor();
  await page.evaluate(() => { lernAbgelegtZeigen({ id: 1 }, { etappe: { titel: 'A', sterne: 30 } }); });
  const k = page.getByRole('dialog', { name: 'Etappe abgelegt' }); await k.waitFor();
  assert.doesNotMatch(await k.evaluate((x) => x.textContent), /IMMER|immer/);
  assert.match(await k.locator('.lr-ab-siegel').evaluate((x) => x.textContent), /ABGELEGT/);
  await k.getByRole('button', { name: /^Weiter/ }).click();
  await page.evaluate(() => { lernAbgelegtZeigen({ id: 1 }, { etappe: { titel: 'A', sterne: 30 }, flug: { titel: 'B', sterne: 100, etappen: 3 } }); });
  const g = page.getByRole('dialog', { name: 'Flug abgelegt' }); await g.waitFor();
  assert.doesNotMatch(await g.evaluate((x) => x.textContent), /IMMER|immer/);
  // freiwillige Wiederholung mit Hilfe: Server bucht 0 – die App zeigt keine Sterne (auch nicht, wenn wiederholung.sterne fehlt)
  const srv = wdhServer({ runde: 1, faellig: 3, gemacht: true }); const { page: p2 } = await setup(t, { gestaltung: 'nacht' }); await p2.route('**/functions/v1/lernen-api/**', srv.route);
  srv.antwort = () => ({ ok: true, format_ok: true, richtig: true, loesung: { wert: 2000 }, sterne: 0, wiederholung: { bestanden: false } });
  await p2.goto(origin + '/#/wiederholen/1-extra'); await p2.getByText('EXTRA · 1 VON').waitFor(); await wdhRichtig(p2);
  await p2.getByText('Richtig – morgen noch einmal ohne Hilfe.').waitFor();
  assert.equal(await p2.locator('.lr-plus-stern').count(), 0);
  assert.equal(await p2.locator('.lr-checkin-sterne').innerText(), '★ 340', 'Zähler unverändert');
});

// ---------- Bau-Auftrag FP – faire Punkte (0.87.0), Vorgabe inhalte/pruefung/kind/faire-punkte/umsetzung.md – erfundene Daten ----------
const fpLandung = async (page, landung, { breite = 400, hoehe = 860 } = {}) => {
  await page.setViewportSize({ width: breite, height: hoehe });
  await page.evaluate((l) => { lernAbschlussZu(); const e = { lernziel: 'stellenwert', titel: 'Welchen Wert hat eine Ziffer?', regel: 'Jeder Platz ist zehnmal so viel wert.' };
    lernAbschlussZeigen({ id: 1 }, lernAbschlussEtappe({ e, nr: 1, von: 3, landung: l, daten: {}, sterne: 60, knopf: lernGrossKnopf('Weiter: Zahlenstrahl', 'Etappe 2 von 3', { onclick: () => {} }), kind: 1 }), { label: 'Etappe gelandet' }); }, landung);
  const d = page.getByRole('dialog', { name: 'Etappe gelandet' }); await d.waitFor(); await d.locator('.lr-ab-szene').click({ position: { x: 5, y: 5 } }); await page.waitForTimeout(120); return d; };

test('FP-1: Landungs-Bonus als Kachel in allen drei Fassungen (80/40/10), eigene Wörter, Sturmflug ohne Fehlerzahl, ohne landung keine Kachel; 360×640 ohne Scrollen', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht' }); await page.goto(origin + '/#/reise/1'); await page.locator('.lr-einsteigen-knopf').waitFor();
  const faelle = [[{ landung_art: 'sauber', bonus: 80, fehler: 0, stufe: 'ohne' }, /Landungs-Bonus[\s\S]*ohne Fehler gelandet[\s\S]*\+80 ★/],
    [{ landung_art: 'direkt', bonus: 80, fehler: 0, stufe: 'ohne' }, /Landungs-Bonus[\s\S]*ohne Fehler gelandet[\s\S]*\+80 ★/],
    [{ landung_art: 'sauber', bonus: 40, fehler: 1, stufe: 'wenig' }, /Landungs-Bonus[\s\S]*mit 1 Fehler gelandet[\s\S]*\+40 ★/],
    [{ landung_art: 'sauber', bonus: 40, fehler: 2, stufe: 'wenig' }, /mit 2 Fehlern gelandet[\s\S]*\+40 ★/],
    [{ landung_art: 'sturm', bonus: 40, fehler: 2, stufe: 'wenig' }, /Landungs-Bonus[\s\S]*gelandet – geschafft![\s\S]*\+40 ★/],
    [{ landung_art: 'sturm', bonus: 10, fehler: 5, stufe: 'sonst' }, /gelandet – geschafft![\s\S]*\+10 ★/]];
  for (const [l, re] of faelle) {
    const d = await fpLandung(page, l); const k = d.locator('.lr-ab-bonus');
    assert.match(await k.innerText(), re, JSON.stringify(l));
    if (l.landung_art === 'sturm') assert.doesNotMatch(await k.innerText(), /\d Fehler/, 'Sturmflug ohne Fehlerzahl');
    assert.doesNotMatch(await d.innerText(), /Direktflug \+|hätte|wären/, 'eigene Wörter, kein Vergleich');
    const kn = await d.locator('.lr-ab-gross').boundingBox(); const kb = await k.boundingBox(); assert.ok(kb.y < kn.y, 'Kachel über dem Knopf');
  }
  for (const [b, h] of [[360, 640], [400, 860], [820, 1180], [1280, 900]]) {
    const d = await fpLandung(page, { landung_art: 'sturm', bonus: 40, fehler: 2, stufe: 'wenig', bordkarten: 14 }, { breite: b, hoehe: h });
    const kn = await d.locator('.lr-ab-gross').boundingBox(); assert.ok(kn.y + kn.height <= h, `${b}×${h}: ohne Scrollen`);
    assert.deepEqual(await gebrocheneWoerter(d.locator('.lr-ab-bonus-text b, .lr-ab-bonus-zahl')), [], `${b}`);
    if (b === 360 || b === 1280) await page.screenshot({ path: path.join(root, `test-results/fp-landung-${b}.png`) });
  }
  const ohne = await fpLandung(page, { landung_art: 'sauber' });
  assert.equal(await ohne.locator('.lr-ab-bonus').count(), 0, 'ohne bonus wie bisher');
});

test('FP-2: Sterne nach der Antwort aus dem Serverwert (ohne Landungs-Bonus); Hinweis bei 5 Sternen höchstens einmal je Etappe und Lerntag, ohne Tadel', async (t) => {
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: (aktion, e) => (aktion === 'schule_uebung_pruefen' && e.format_ok ? { ...e, sterne: 5 } : null) });
  await page.goto(origin + '/#/lerneinheit/1-1-ueben-1');
  const tf = page.getByRole('group', { name: 'Tastenfeld' }); await page.locator('.lr-bordkarte').first().waitFor();
  if (await tf.count()) { for (const z of ['2', '0', '0', '0']) await tf.getByRole('button', { name: z, exact: true }).click(); await tf.getByRole('button', { name: 'Prüfen' }).click(); }
  else { await page.locator('main input').first().fill('2000'); await page.getByRole('button', { name: 'Prüfen' }).click(); }
  await page.locator('.lr-rueck-ok').waitFor();
  assert.match(await page.locator('.lr-rueck-ok b').first().innerText(), /\+5 Sterne/i, 'Serverwert, nicht 10');
  assert.equal(await page.locator('.lr-fp-hinweis').count(), 0, 'ohne Tipp/zweiten Versuch kein Hinweis');
  // Bonus wird nicht in die Bordkarten-Sterne gerechnet
  const r = await page.evaluate(() => { const ctx = { kind: 1, regeln: { sterne_uebung_richtig: 10 } }; const e = { lernziel: 'x' };
    const a = lernFuenfHinweis(ctx, e, 5, { hilfe: true, zweiter: false })?.textContent; const b = lernFuenfHinweis(ctx, e, 5, { hilfe: true, zweiter: false });
    const c = lernFuenfHinweis(ctx, { lernziel: 'y' }, 5, { hilfe: false, zweiter: true })?.textContent; const d = lernFuenfHinweis(ctx, { lernziel: 'z' }, 10, { hilfe: true, zweiter: false });
    return [a, b, c, d]; });
  assert.deepEqual(r, ['Ganz ohne Tipp gibt es 10 ★.', null, 'Gleich beim ersten Mal gibt es 10 ★.', null]);
  assert.doesNotMatch(r.join(' '), /nur|leider|Abzug|weniger/);
});

test('FP-3: einmaliger Hinweis nach der Nachbuchung („Geschenk für deine Landungen“), „Super ›“ schließt ihn; ohne Nachbuchung nichts – 360/820/1280', async (t) => {
  const nach = (aktion, e) => (aktion === 'schule_konto' ? { ...structuredClone(e), landung_nachbuchung: { etappen: 25, sterne: 1620, am: '2026-11-22T12:00:00Z' } } : null);
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: nach });
  for (const b of [360, 820, 1280]) { await page.setViewportSize({ width: b, height: 800 });
    await page.goto(origin + '/#/reise/1'); const k = page.locator('.lr-fp-geschenk'); await k.waitFor();
    assert.match(await k.innerText(), /★ Geschenk für deine Landungen[\s\S]*Für deine bisherigen Landungen gibt es nachträglich \+1.620 ★ Landungs-Bonus\./);
    assert.ok(await ohneQuerrollen(page), `${b}`); }
  await page.getByRole('button', { name: 'Super ›' }).click(); await page.locator('.lr-fp-geschenk').waitFor({ state: 'detached' });
  await page.reload(); await page.locator('.lr-einsteigen-knopf').waitFor();
  assert.equal(await page.locator('.lr-fp-geschenk').count(), 0, 'nur einmal');
  const { page: p2 } = await setup(t, { gestaltung: 'nacht' }); await p2.goto(origin + '/#/reise/1'); await p2.locator('.lr-einsteigen-knopf').waitFor();
  assert.equal(await p2.locator('.lr-fp-geschenk').count(), 0);
});

test('FP-5 (0.87.1): „Super ›“ quittiert beim Server (schule_landung_nachbuchung_gesehen), gesehen_am vom Server blendet aus, Fehler → Rückfall Gerät', async (t) => {
  const NB = { etappen: 25, sterne: 1620, am: '2026-11-22T12:00:00Z' };
  // 1. Quittung geht an den Server; danach liefert der Server gesehen_am → auch ohne localStorage weg
  const srv = { gesehen: null, aufrufe: [] };
  const f = (aktion, e, d) => {
    if (aktion === 'schule_konto' && e) return { ...structuredClone(e), landung_nachbuchung: { ...NB, gesehen_am: srv.gesehen } };
    if (aktion === 'schule_landung_nachbuchung_gesehen') { srv.aufrufe.push(d); srv.gesehen = srv.gesehen || '2026-11-22T13:40:00Z'; return { ok: true, gesehen_am: srv.gesehen }; }
    return null; }; f.neueAktionen = true;
  const { page } = await setup(t, { gestaltung: 'nacht', anpassen: f });
  await page.goto(origin + '/#/reise/1'); await page.locator('.lr-fp-geschenk').waitFor();
  await page.getByRole('button', { name: 'Super ›' }).click(); await page.locator('.lr-fp-geschenk').waitFor({ state: 'detached' });
  for (let i = 0; i < 20 && !srv.aufrufe.length; i++) await page.waitForTimeout(50);
  assert.equal(srv.aufrufe.length, 1, 'genau eine Quittung'); assert.ok(srv.aufrufe[0]?.lernender_id, 'mit lernender_id');
  await page.evaluate(() => Object.keys(localStorage).filter((k) => k.startsWith('lern.fpnach.')).forEach((k) => localStorage.removeItem(k)));
  await page.reload(); await page.locator('.lr-einsteigen-knopf').waitFor();
  assert.equal(await page.locator('.lr-fp-geschenk').count(), 0, 'gesehen_am vom Server (zweites Gerät)');
  assert.equal(srv.aufrufe.length, 1, 'kein zweiter Aufruf');
  // 2. Server kennt die Aktion nicht / Fehler → Karte trotzdem weg, Gerät merkt es sich
  const g = (aktion, e) => {
    if (aktion === 'schule_konto' && e) return { ...structuredClone(e), landung_nachbuchung: { ...NB } };
    if (aktion === 'schule_landung_nachbuchung_gesehen') return { ok: false, fehler: 'unbekannte Aktion' };
    return null; }; g.neueAktionen = true;
  const { page: p2 } = await setup(t, { gestaltung: 'nacht', anpassen: g });
  await p2.goto(origin + '/#/reise/1'); await p2.locator('.lr-fp-geschenk').waitFor();
  await p2.getByRole('button', { name: 'Super ›' }).click(); await p2.locator('.lr-fp-geschenk').waitFor({ state: 'detached' });
  await p2.reload(); await p2.locator('.lr-einsteigen-knopf').waitFor();
  assert.equal(await p2.locator('.lr-fp-geschenk').count(), 0, 'Rückfall localStorage');
});

test('FP-4: Info-Seite „Sterne“ nach der Vorgabe', async (t) => {
  const { page } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.goto(origin + '/lernen/#/info'); await page.getByRole('heading', { name: 'Erste Schritte' }).waitFor();
  await page.evaluate(() => document.querySelectorAll('details').forEach((d) => { d.open = true; }));
  const text = (await page.locator('#main').innerText()).replace(/\s+/g, ' ');
  for (const s of ['Jede Übungsaufgabe bringt einmal Sterne: 10 ★, wenn sie im ersten Versuch ohne Tipp gelöst ist, sonst 5 ★.', 'Landungs-Bonus: +80 ★ ohne Fehler, +40 ★ mit 1–2 Fehlern, sonst +10 ★',
    'Tipps zählen nicht als Fehler.', 'Tests, Wiederholungen und Mischkarten zählen hier nicht mit.', 'Wiederholungen bringen 10 ★, wenn sie selbst gelöst sind',
    'Für Etappen, die vor dem 22.11. gelandet sind, wurde der Bonus einmal nachgetragen. Gebuchte Sterne werden nie abgezogen.'])
    assert.ok(text.includes(s), 'fehlt: ' + s);
  assert.ok(!text.includes('10 Sterne für jede Bordkarte, die zum ersten Mal richtig ist'), 'alter Satz');
});
