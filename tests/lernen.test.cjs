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
    const file = path.join(root, name === '/' ? 'index.html' : name);
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
const zeig = (a) => { const { loesung, ...r } = a; return { ...r, tipp: 'Denk an die Stellenwerttafel.' }; };
function bewerte(a, w) {
  if (a.antworttyp === 'luecken') { if (!w?.werte || w.werte.some((x) => !String(x).trim())) return { format_ok: false, hinweis: 'Bitte fülle alle Felder aus.' }; return { format_ok: true, richtig: w.werte.every((x, i) => Number(String(x).replace('−', '-')) === a.loesung.werte[i]) }; }
  if (a.antworttyp === 'auswahl' || a.antworttyp === 'markierung') return { format_ok: true, richtig: w.index === a.loesung.index };
  if (String(w.wert).includes('.')) return { format_ok: false, hinweis: 'Bitte schreibe Dezimalzahlen mit Komma.' };
  return { format_ok: true, richtig: Number(String(w.wert).replace(/\s/g, '')) === a.loesung.wert };
}

async function setup(t) {
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, serviceWorkers: 'block' });
  t.after(() => context.close());
  await context.addInitScript(() => { localStorage.setItem('ks_token', 'synthetic-test-session'); });
  const page = await context.newPage(); page.setDefaultTimeout(5000);
  const errors = []; page.on('pageerror', (e) => errors.push(e.message)); t.after(() => assert.deepEqual(errors, []));
  await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.route('**/functions/v1/app-api/**', (r) => r.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: {} }) }));
  const calls = []; const stand = { test: null, antworten: {} };
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); calls.push(b); const d = b.daten || {};
    let e;
    const geo = (ort, stadt, land, lat, lon, kontinent, kt, erdteil) => ({ ort, stadt, land, lat, lon, kontinent, kontinent_titel: kt, erdteil });
    if (b.aktion === 'schule_uebersicht') e = { ok: true, leitung: true, einheiten: [
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
    else if (b.aktion === 'schule_konto') e = { ok: true, konto: { sterne: 340, sterne_gesamt: 340, stempel: d.lernender_id === 2 ? 1 : 0, lerntage: 12 },
      look: { stil: d.lernender_id === 2 ? 'studio' : 'entdecker', welt: d.lernender_id === 2 ? 'Nacht' : 'Ozean' },
      belohnungen: [{ id: 5, titel: 'Eis', kosten_sterne: 300, kosten_stempel: 0 }, { id: 6, titel: 'Kinoabend', kosten_sterne: 0, kosten_stempel: 3 }], einloesungen: [] };
    else if (b.aktion === 'schule_eltern') e = { ok: true, kinder: [{ id: 1, name: 'Kind A', konto: { sterne: 340, stempel: 0, lerntage: 12 } }], belohnungen: [{ id: 5, titel: 'Eis', kosten_sterne: 300, kosten_stempel: 0, aktiv: true }],
      einloesungen: [{ id: 9, kind: 'Kind A', titel: 'Eis', sterne: 300, status: 'beantragt' }] };
    else if (['schule_einloesen', 'schule_look_setzen', 'schule_belohnung_setzen', 'schule_einloesung_entscheiden'].includes(b.aktion)) e = { ok: true };
    else if (b.aktion === 'schule_einheit_lesen') e = { ok: true, einheit_id: d.einheit_id, status: 'geprueft', inhalt: { ziel: 'Natürliche Zahlen: große Zahlen lesen', verstehen: [{ titel: 'Stellenwerte', text: 'Jede Stelle ist zehnmal so viel wert.', beispiel: '2 000 = 2 · 1 000' }], merke: ['Dreiergruppen lesen.'] },
      uebungen: [zeig(AUFG[11]), zeig(AUFG[12]), zeig(AUFG[13])], stand: [{ lernziel: 'stellenwert', pflicht: true, status: 'offen' }], laufender_test: null };
    else if (b.aktion === 'schule_uebung_pruefen') { const a = AUFG[d.aufgabe_id]; e = { ok: true, ...bewerte(a, d.antwort), loesung: a.loesung, loesungsweg: 'Weg zur Lösung.' }; }
    else if (b.aktion === 'schule_test_starten') { stand.test = 77; e = { ok: true, sitzung_id: 77, art: d.art, aufgaben: [AUFG[14], AUFG[12]].map((a) => { const { loesung, ...r } = a; return r; }), beantwortet: [] }; }
    else if (b.aktion === 'schule_test_antwort') { const a = AUFG[d.aufgabe_id]; const r = bewerte(a, d.antwort); if (r.format_ok) stand.antworten[a.id] = { w: d.antwort, ok: r.richtig }; e = { ok: true, format_ok: r.format_ok, hinweis: r.hinweis, gespeichert: r.format_ok }; }
    else if (b.aktion === 'schule_test_abschliessen') {
      const erg = [AUFG[14], AUFG[12]].map((a) => ({ aufgabe_id: a.id, lernziel: a.lernziel, frage: a.frage, antworten: a.antworten, antwort: stand.antworten[a.id]?.w ?? null, richtig: !!stand.antworten[a.id]?.ok, loesung: a.loesung, loesungsweg: 'Weg.' }));
      e = { ok: true, sitzung_id: 77, richtig: erg.filter((x) => x.richtig).length, gesamt: 2, ergebnisse: erg, lernziele: [{ lernziel: 'lesen', pflicht: true, status: 'nachgewiesen' }, { lernziel: 'strahl', pflicht: true, status: 'fehler' }], einheit_abgeschlossen: false, ort: { abgeschlossen: false } };
    }
    await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
  });
  return { page, calls };
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
  await page.getByRole('link', { name: 'Reisepass' }).click();
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
  await page.getByRole('link', { name: 'Reisepass' }).click();
  await page.locator('.lr-stempel', { hasText: 'Rom' }).waitFor();
  await page.goto(origin + '/#/reise/3');
  await page.getByText('Terme umformen', { exact: false }).first().waitFor();
});

test('Lernen: Üben mit Zahl, Zahlenstrahl und Lückenfeldern', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lerneinheit/1-1');
  await page.locator('.lr').waitFor();
  await page.getByText('Jede Stelle ist zehnmal so viel wert.').waitFor();
  await page.getByRole('tab', { name: 'Üben' }).click();
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2.000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Bitte schreibe Dezimalzahlen mit Komma.').waitFor();
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2 000');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('✓ Richtig!').waitFor();
  await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
  await page.getByRole('button', { name: 'Markierung 3' }).click();
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/lernen-ueben-390.png'), fullPage: true });
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('Richtig ist: Markierung 4').waitFor();
  await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
  await page.getByRole('textbox', { name: 'Feld 1' }).fill('1');
  await page.getByRole('textbox', { name: 'Feld 2' }).fill('2');
  await page.getByRole('textbox', { name: 'Feld 3' }).fill('1');
  await page.getByRole('button', { name: 'Prüfen' }).click();
  await page.getByText('✓ Richtig!').waitFor();
  const p = calls.filter((c) => c.aktion === 'schule_uebung_pruefen');
  assert.deepEqual(p.map((c) => c.daten.antwort), [{ wert: '2.000' }, { wert: '2 000' }, { index: 3 }, { werte: ['1', '2', '1'] }]);
  assert.ok(p.every((c) => c.daten.lernender_id === 1 && c.daten.client_id));
});

test('Lernen: Test ohne Lösungen bis zur Abgabe, danach Auswertung', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lerneinheit/1-1');
  await page.getByRole('tab', { name: 'Test' }).click();
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
