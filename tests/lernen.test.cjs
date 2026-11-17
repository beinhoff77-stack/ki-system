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
  await page.locator('.lp-zeile', { hasText: 'Große natürliche Zahlen' }).getByText('Gym 5 · RS 5 · IB 1').waitFor();
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

test('Lernstand: Was wackelt – je Lernkarte mit den echten falschen Antworten', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/lernen');
  await page.getByRole('link', { name: /Lernstand Kind A/ }).click();
  await page.getByRole('heading', { name: 'Was wackelt?' }).waitFor();
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
  await rom.getByText('Gym 5 · RS 5 · IB 2').waitFor();
  // Rechts der Lehrplan der eigenen Schulart und Klasse
  assert.equal(await page.getByRole('combobox', { name: 'Schulart' }).inputValue(), 'gym_by');
  assert.equal(await page.getByRole('combobox', { name: 'Klasse' }).inputValue(), '5');
  await page.screenshot({ path: path.join(root, 'test-results/themenplan-390.png'), fullPage: true });
  await page.getByRole('spinbutton', { name: 'Klasse' }).fill('6');
  await page.getByRole('button', { name: 'Speichern', exact: true }).click();
  await page.getByText('Gespeichert.').first().waitFor();
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
  await page.getByRole('button', { name: 'Menü' }).click();
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
  await page.getByText('nach 6 Punkten', { exact: false }).waitFor();
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
  for (const [pfad, warte] of [['lernen', 'Lehrplan-Übersicht'], ['plan/1', 'Lehrplan'], ['lehrplan', 'Lehrplan-Übersicht'], ['inhalte/1', 'Bordkarten zum Üben'], ['lernstand/1', 'Was wackelt?'], ['lernauftraege', 'Neuer Auftrag (allgemein)'], ['zugaenge', 'Neuen Zugang anlegen'], ['info', 'Erste Schritte']]) {
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
  assert.ok(dreieck > 15 && dreieck < 22, 'eine Einheit breit (≈ 17,6 px): ' + dreieck);
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
  const verdacht = await page.evaluate((rs) => rs.map((r) => lernKurzGesagt(r)).filter((k) => /(?<!\b(?:z\.\s?B|d\.\s?h|u\.\s?a|bzw|ca|usw|vgl|[zdu]|\d{1,2}))[.!?]\s+[A-ZÄÖÜ]/.test(k.replace(/\b\d+,\d+\./g, '#'))), regeln);
  assert.deepEqual(verdacht, []);
  assert.deepEqual(await page.evaluate(() => ['Unter null schreibst du ein Minus, z. B. −3. Das ist kalt.', 'Man rechnet ca. 5 Stück, d. h. viel. Fertig!', 'Ist das so? Ja.', 'Die 3. Wurzel ist gemeint. Mehr.'].map(lernKurzGesagt)),
    ['Unter null schreibst du ein Minus, z. B. −3.', 'Man rechnet ca. 5 Stück, d. h. viel.', 'Ist das so?', 'Die 3. Wurzel ist gemeint.']);
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
  const quelle = fs.readFileSync(path.join(root, 'lernen.js'), 'utf8');
  assert.equal((quelle.match(/e\.fehler && !LERN_GRUND\[r\.grund\] \? el\('div', \{ class: 'lr-fehler lr-detektiv' \}/g) || []).length, 2);
  await page.goto(origin + '/#/lerneinheit/1-1-test');
  await page.getByRole('heading', { name: 'Rom · Natürliche Zahlen' }).waitFor(); // N6
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
  await page.getByText('MEIN STAND · GYMNASIUM KLASSE 5').waitFor();
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
  assert.deepEqual(await a.locator('.lern-mini-name').allInnerTexts(), ['GYM 5', 'RS 5', 'IB 1']);
  await a.getByText('Jetzt: Rom · Natürliche Zahlen (2/4)').waitFor();
  assert.deepEqual(await a.locator('.lern-kindbereich-knoepfe a').allInnerTexts(), ['Lernstand', 'Flugplan', 'Lernreise ansehen']);
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

