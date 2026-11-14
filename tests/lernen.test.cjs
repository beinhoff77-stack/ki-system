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
    if (b.aktion === 'schule_lehrplan_uebersicht') e = { ok: true, kinder: [{ id: 1, name: 'Kind A', klasse: 5, schulart: 'gym_by' }, { id: 2, name: 'Kind B', klasse: 8, schulart: 'gym_by' }],
      themen: [
        { thema_id: 1, titel: 'Große natürliche Zahlen', gebiet: 'Zahlen', ort: 'Rom', block_id: 49, jahrgang: { gym_by: 5, rs_by: 5, ib_myp: 1 }, einheit: { id: 1, status: 'geprueft', karten: 3, aufgaben: 24, neu: 6 }, stand: { 1: 'erledigt', 2: 'keine_einheit' }, geplant: [], rueckmeldungen: 1 },
        { thema_id: 2, titel: 'Teilbarkeit', gebiet: 'Zahlen', ort: 'Athen', block_id: 48, jahrgang: { gym_by: 5, rs_by: 6 }, einheit: { id: 4, status: 'entwurf', karten: 8, aufgaben: 96, neu: 96 }, stand: { 1: 'offen' }, geplant: [1], rueckmeldungen: 0 },
        { thema_id: 3, titel: 'Brüche addieren', gebiet: 'Zahlen', ort: 'Pisa', block_id: 47, jahrgang: { gym_by: 6, rs_by: 6, ib_myp: 2 }, einheit: null, stand: {}, geplant: [], rueckmeldungen: 0 },
        { thema_id: 4, titel: 'Lineare Funktionen', gebiet: 'Funktionen', ort: 'Kairo', block_id: 70, jahrgang: { gym_by: 8, rs_by: 8, ib_myp: 3 }, einheit: null, stand: {}, geplant: [], rueckmeldungen: 0 },
        { thema_id: 5, titel: 'Nur Realschule', gebiet: 'Geld', ort: 'Lima', block_id: 71, jahrgang: { rs_by: 7 }, einheit: null, stand: {}, geplant: [], rueckmeldungen: 0 }] };
    if (b.aktion === 'schule_inhalt_lesen') e = { ok: true, einheit_id: d.einheit_id, status: 'geprueft', ort: { stadt: 'Rom', titel: 'Natürliche Zahlen' },
      thema: { titel: 'Große natürliche Zahlen', jahrgang: { gym_by: 5, rs_by: 5 } }, inhalt: { ziel: 'Große Zahlen lesen.', etappen: ETAPPEN },
      aufgaben: [{ ...AUFG[11], pool: 'uebung', stufe: 1, freigegeben: true, loesungsweg: 'Tausender-Stelle.' }, { ...AUFG[12], pool: 'uebung', stufe: 2, freigegeben: false },
        { ...AUFG[11], id: 99, pool: 'test', freigegeben: true }],
      rueckmeldungen: [{ id: 4, art: 'mehr_aufgaben', text: 'Mehr Aufgaben zum Runden.', status: 'offen', lernziel: 'stellenwert', am: '2026-11-14T09:00:00Z' }] };
    if (b.aktion === 'schule_plan_lesen') e = { ok: true, kind: { id: 1, name: 'Kind A', klasse: 5 }, revision: 1,
      plan: [{ route_id: 1, block_id: 49, position: 1, art: 'normal', status: 'offen', kann_schon: false }, { route_id: 2, block_id: 52, position: 2, art: 'normal', status: 'offen', kann_schon: false }],
      orte: [{ block_id: 49, titel: 'Natürliche Zahlen', stadt: 'Rom', kontinent: 'Zahlen', ziel_klasse: 5, einheiten: [{ id: 1, status: 'geprueft', titel: 'Große Zahlen', pflicht: 4, fertig: 2, fehler: 1 }] },
        { block_id: 48, titel: 'Teilbarkeit', stadt: 'Athen', kontinent: 'Zahlen', ziel_klasse: 5, einheiten: [] },
        { block_id: 52, titel: 'Zinsen', stadt: 'New York', kontinent: 'Geld', ziel_klasse: 7, einheiten: [{ id: 2, status: 'geprueft', titel: 'Zinsen', pflicht: 6, fertig: 0, fehler: 0 }] }],
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
      uebungen: [zeig(AUFG[11]), zeig(AUFG[12]), zeig(AUFG[13])], stand: ETAPPEN.map((x) => ({ lernziel: x.lernziel, pflicht: true, status: 'offen' })),
      etappen_stand: { stellenwert: { fertig: false, ziel: 2 }, strahl: { fertig: false, ziel: 2 }, binomisch: { fertig: false, ziel: 2 } }, laufender_test: null };
    else if (b.aktion === 'schule_merkheft') e = { ok: true, einheiten: [{ einheit_id: 1, block_id: 49, stadt: 'Rom', ort_titel: 'Natürliche und ganze Zahlen', etappen: ETAPPEN,
      stand: { stellenwert: { fertig: true }, strahl: { fertig: true } }, blocktest_fertig: false, nachtest: { grund: 'einheit_offen' } },
      { einheit_id: 2, block_id: 52, stadt: 'New York', ort_titel: 'Zinsen', etappen: ETAPPEN.slice(0, 2), stand: { stellenwert: { fertig: true } }, blocktest_fertig: false, nachtest: { grund: 'einheit_offen' } }] };
    else if (b.aktion === 'schule_uebung_pruefen') {
      const a = AUFG[d.aufgabe_id]; const r = bewerte(a, d.antwort);
      const k = stand.karten[a.lernziel] ||= { serie: 0, ziel: 2, sitzt: false };
      let neu = false;
      if (r.format_ok) { if (r.richtig && !d.hilfe) k.serie++; else if (!r.richtig) k.serie = 0; if (!k.sitzt && k.serie >= k.ziel) { k.sitzt = true; neu = true; } }
      e = { ok: true, ...r, loesung: a.loesung, loesungsweg: 'Weg zur Lösung.', karte: { ...k, neu_sitzt: neu } };
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
  await page.getByRole('heading', { name: 'Mathe Klasse 7/8' }).waitFor();
  await page.getByText('Jetzt: Rom · Natürliche Zahlen (2/4)').waitFor();
  await page.getByText('möchte „Eis“').waitFor();
  await page.getByRole('button', { name: 'Bestätigen' }).click();
  await page.locator('#bl-titel').fill('Kinoabend');
  await page.locator('#bl-stempel').fill('3');
  await page.getByRole('button', { name: 'Hinzufügen' }).click();
  await page.waitForTimeout(200);
  assert.deepEqual(calls.filter((c) => c.aktion === 'schule_einloesung_entscheiden').map((c) => c.daten), [{ id: 9, status: 'bestaetigt' }]);
  assert.equal(calls.find((c) => c.aktion === 'schule_belohnung_setzen').daten.kosten_stempel, 3);
});

test('Lernreise: Heute dran auf der echten Karte, Weltkarte und Reisepass', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/reise/1');
  await page.getByRole('heading', { name: 'Rom: Natürliche Zahlen' }).waitFor();
  await page.getByText('MEIN STAND · GYMNASIUM KLASSE 5').waitFor();
  await page.getByText('1 von 14 Themen').waitFor();
  assert.equal(await page.locator('.lr.lr-ozean.lr-entdecker').count(), 1);
  assert.equal(await page.locator('#areas').isVisible(), false);
  await page.getByText('Du bist in Rom').waitFor();
  assert.equal(await page.locator('details.lr-mehr', { hasText: 'Später' }).count(), 1);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-heute-390.png'), fullPage: true });
  await page.getByRole('link', { name: 'Karte' }).click();
  await page.getByRole('heading', { name: '0 von 5 Orten' }).waitFor();
  await page.getByText('Rom: Natürliche und ganze Zahlen').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-karte-390.png'), fullPage: true });
  await page.getByRole('link', { name: 'Mein Weg' }).click();
  await page.getByRole('heading', { name: 'GERADE DRAN' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-weg-390.png'), fullPage: true });
  await page.getByRole('link', { name: /Reisepass/ }).click();
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
  await page.getByRole('heading', { name: 'New York: Einfache Zinsen' }).waitFor();
  assert.equal(await page.locator('.lr.lr-nacht.lr-studio').count(), 1);
  await page.screenshot({ path: path.join(root, 'test-results/lernreise-leo-390.png'), fullPage: true });
  await page.getByText('1 von 2 Etappen').waitFor();
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
  assert.equal(await page.locator('#title').textContent(), 'Rom: Natürliche und ganze Zahlen');
  assert.equal(await page.getByRole('tab', { name: 'Erklären' }).getAttribute('aria-selected'), 'true');
  const sichtbar = page.locator('.lr-panel:not([hidden])');
  // Erklären: alle Lernkarten untereinander, ohne Klick nachlesbar.
  await sichtbar.locator('.lr-stellentafel').first().waitFor();
  await sichtbar.locator('mark', { hasText: '10-mal' }).first().waitFor();
  await sichtbar.getByText('100 : 10 = 10').waitFor();
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lernen-erklaeren-390.png'), fullPage: true });
  await sichtbar.getByRole('button', { name: 'Dazu üben ▸' }).first().click();
  await page.waitForURL(/#\/lerneinheit\/1-1-ueben-1$/);
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2.000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Bitte schreibe Dezimalzahlen mit Komma.').waitFor();
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2 000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.getByText('1 von 2 richtig hintereinander').waitFor();
  // Zur Erklärung und zurück: Aufgabe und Rückmeldung bleiben stehen.
  await page.getByRole('tab', { name: 'Erklären' }).click();
  await sichtbar.locator('.lr-stellentafel').first().waitFor();
  await page.getByRole('tab', { name: 'Üben' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('LERNKARTE SITZT').waitFor();
  await page.getByText('+10 Sterne').waitFor();
  await page.getByText('1 von 3 sitzen').waitFor();
  await page.getByRole('button', { name: 'Nächste Karte: Zahlenstrahl' }).click();
  await page.getByRole('button', { name: 'Markierung 3' }).click();
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig ist: 20 000 (der 4. Strich nach dem Anfang)').waitFor();
  // Bei einem Fehler klappt die Erklärung direkt an der Aufgabe auf.
  await sichtbar.locator('.lr-nochmal').getByText('100 : 10 = 10').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernen-probieren-390.png'), fullPage: true });
  await page.getByRole('tab', { name: 'Fehler' }).click();
  await sichtbar.locator('.lr-fehlerkarte').first().waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/lernen-fehler-390.png'), fullPage: true });
  await page.getByRole('tab', { name: 'Üben' }).click();
  await page.getByText('Richtig ist: 20 000').waitFor();
  await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
  await page.getByRole('button', { name: 'Markierung 4' }).click();
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig!').waitFor();
  await page.goto(origin + '/#/lerneinheit/1-1-3');
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
  const p = calls.filter((c) => c.aktion === 'schule_uebung_pruefen');
  assert.deepEqual(p.map((c) => c.daten.antwort), [{ wert: '2.000' }, { wert: '2 000' }, { wert: '2000' }, { index: 3 }, { index: 4 }, { werte: ['1', '2', '1'] }]);
  assert.ok(p.every((c) => c.daten.lernender_id === 1 && c.daten.client_id));
  const w = await page.evaluate(() => document.documentElement.scrollWidth); assert.ok(w <= 390, 'keine Querverschiebung: ' + w);
});

test('Lernen: Merkheft zeigt alle Lernkarten zum Nachlesen, mit Suche und Weg zum Üben', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/merkheft/2');
  await page.locator('details.lr-merk').first().waitFor();
  assert.equal(await page.locator('.lr.lr-nacht.lr-studio').count(), 1);
  assert.equal(await page.locator('details.lr-merk').count(), 5);
  await page.getByText('am Üben').first().waitFor().catch(() => {});
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
  // Gymnasium: 4 Themen (das reine Realschul-Thema fehlt), 1 fertig, 1 in Prüfung, 2 ohne Inhalt.
  assert.deepEqual(await page.locator('.lp-kachel b').allTextContents(), ['4', '1', '1', '2']);
  await page.getByRole('heading', { name: /Klasse 8.*Kind B/ }).waitFor();
  assert.equal(await page.locator('.lp-zeile', { hasText: 'Nur Realschule' }).count(), 0);
  await page.locator('.lp-zeile.lp-fertig', { hasText: 'Große natürliche Zahlen' }).getByText('Kind A: geschafft').waitFor();
  await page.locator('.lp-zeile', { hasText: 'Große natürliche Zahlen' }).getByText('Gym 5 · RS 5 · IB 1').waitFor();
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lehrplan-390.png'), fullPage: true });
  await page.getByRole('combobox', { name: 'Klasse' }).selectOption('5');
  assert.deepEqual(await page.locator('.lp-kachel b').allTextContents(), ['2', '1', '1', '0']);
  await page.getByRole('combobox', { name: 'Klasse' }).selectOption('');
  await page.getByRole('combobox', { name: 'Inhalt' }).selectOption('leer');
  await page.locator('.lp-zeile', { hasText: 'Lineare Funktionen' }).getByRole('button', { name: 'Bauen lassen' }).click();
  await page.getByText('Angefragt ✓').waitFor();
  const rm = calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten;
  assert.equal(rm.art, 'thema_fehlt'); assert.equal(rm.block_id, 70); assert.match(rm.text, /Lineare Funktionen/);
  await page.getByRole('button', { name: 'Realschule' }).click();
  await page.locator('.lp-zeile', { hasText: 'Nur Realschule' }).waitFor();
  await page.getByRole('combobox', { name: 'Inhalt' }).selectOption('');
  await page.locator('.lp-zeile', { hasText: 'Große natürliche Zahlen' }).getByRole('link', { name: 'Inhalte ansehen' }).click();
  await page.waitForURL(/#\/inhalte\/1$/);
  await page.getByText('3 Lernkarten · 2 Übungen · 1 Test- und Nachtestaufgaben', { exact: false }).waitFor();
  await page.locator('details.lp-karte > summary').first().click();
  await page.getByText('ERKLÄRUNG, WIE DAS KIND SIE SIEHT').first().waitFor();
  await page.locator('.lp-tabelle').first().getByText('frei', { exact: true }).first().waitFor();
  await page.locator('details.lp-karte > summary', { hasText: '1 in Prüfung' }).waitFor();
  await page.locator('.lp-tabelle').first().getByText('Tausender-Stelle.').waitFor();
  await page.getByText('Mehr Aufgaben zum Runden.').waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/inhalte-390.png'), fullPage: true });
  const w = await page.evaluate(() => document.documentElement.scrollWidth); assert.ok(w <= 390, 'keine Querverschiebung: ' + w);
});

test('Kinderplan: Schulart und Klasse setzen', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/plan/1');
  await page.getByRole('combobox', { name: 'Schulart' }).selectOption('rs_by');
  await page.getByRole('spinbutton', { name: 'Klasse' }).fill('6');
  await page.getByRole('button', { name: 'Speichern', exact: true }).click();
  await page.getByText('Gespeichert.').first().waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_kind_setzen').daten, { lernender_id: 1, schulart: 'rs_by', klasse: 6 });
});

test('Lernen-Seite: Lehrer meldet sich mit Code an, ordnet den Themenplan und schreibt Rückmeldungen', async (t) => {
  const { page, calls, appCalls } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.goto(origin + '/lernen/');
  await page.getByLabel('Lern-Code').fill('falsch');
  await page.getByRole('button', { name: 'Anmelden' }).click();
  await page.getByText('Code unbekannt').waitFor();
  await page.getByLabel('Lern-Code').fill('ABCD-EFGH-JKLM');
  await page.getByRole('button', { name: 'Anmelden' }).click();
  await page.getByText('Themenplan Kind A').waitFor();
  assert.equal(await page.getByText('Zugänge', { exact: true }).count(), 0, 'Lehrer verwaltet keine Zugänge');
  assert.equal(await page.getByRole('heading', { name: 'Mathe Klasse 7/8' }).count(), 0);
  await page.getByText('Themenplan Kind A').click();
  await page.locator('.lern-plan-zeile').first().waitFor();
  await page.getByRole('button', { name: 'New York – Zinsen nach oben' }).click();
  await page.locator('summary', { hasText: 'Zahlen' }).click();
  await page.getByRole('button', { name: '+ Athen – Teilbarkeit' }).click();
  await page.locator('.lern-plan-zeile').nth(2).getByLabel('kann es schon').check();
  await page.getByRole('button', { name: 'Plan speichern' }).click();
  await page.getByText('Gespeichert.').waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_plan_setzen').daten,
    { lernender_id: 1, revision: 1, eintraege: [{ block_id: 52, kann_schon: false }, { block_id: 49, kann_schon: false }, { block_id: 48, kann_schon: true }] });
  await page.goto(origin + '/lernen/#/rueckmeldungen');
  await page.getByText('6 neue Aufgaben ergänzt.').waitFor();
  await page.locator('.lern-rm-form').first().getByRole('button', { name: 'Thema fehlt' }).click();
  await page.locator('.lern-rm-form').first().getByLabel('Deine Anmerkung').fill('Prozentrechnung fehlt für Klasse 7.');
  await page.locator('.lern-rm-form').first().getByRole('button', { name: 'Senden' }).click();
  await page.getByText('Danke – ist bei der Entwicklung angekommen.').waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten, { art: 'thema_fehlt', text: 'Prozentrechnung fehlt für Klasse 7.' });
  assert.deepEqual(appCalls, [], 'Die Lernen-Seite ruft die Hauptapp-Schnittstelle nie auf');
});

test('Lernen-Seite: Anmerkung direkt an einer Aufgabe, Kind-Code nur Lernreise', async (t) => {
  const { page, calls } = await setup(t, { lernSeite: true, rolle: 'lehrer' });
  await page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  await page.goto(origin + '/lernen/#/lerneinheit/3-1-1');
  await page.getByText('✎ Anmerkung zu dieser Aufgabe').click();
  const offen = page.locator('.lr-panel:not([hidden])');
  await offen.getByRole('button', { name: 'Schwieriger' }).click();
  await offen.getByLabel('Deine Anmerkung').fill('Zu leicht für Klasse 5.');
  await offen.getByRole('button', { name: 'Senden' }).click();
  await page.getByText('Danke – ist bei der Entwicklung angekommen.').waitFor();
  assert.deepEqual(calls.find((c) => c.aktion === 'schule_rueckmeldung_geben').daten,
    { einheit_id: 1, lernziel: 'stellenwert', aufgabe_id: 11, lernender_id: 3, art: 'schwieriger', text: 'Zu leicht für Klasse 5.' });
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
  await page.getByText('Themenplan Kind A').waitFor();
  const gruppen = await page.evaluate(() => {
    const u = { einheiten: [{ id: 1, block_id: 49, pflicht_anzahl: 4, ziel_klasse: 5 }, { id: 2, block_id: 52, pflicht_anzahl: 6, ziel_klasse: 7 }, { id: 4, block_id: 48, pflicht_anzahl: 6, ziel_klasse: 5 }],
      orte: [], lernende: [{ id: 1, klasse: 5, route: [{ block_id: 52, position: 1, art: 'normal', status: 'offen' }, { block_id: 49, position: 2, art: 'normal', status: 'offen', kann_schon: true }, { block_id: 48, position: 3, art: 'normal', status: 'entfernt' }], stand: [] }] };
    const d = lernReiseDaten(u, 1);
    return { jetzt: d.jetzt.map((e) => e.id), kann: d.kann.map((e) => e.id), spaeter: d.spaeter.map((e) => e.id), naechste: d.naechste.id };
  });
  assert.deepEqual(gruppen, { jetzt: [2], kann: [1], spaeter: [4], naechste: 2 });
});
