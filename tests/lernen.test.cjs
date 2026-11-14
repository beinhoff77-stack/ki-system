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
    if (b.aktion === 'schule_uebersicht') e = { ok: true, leitung: true, einheiten: [
      { id: 1, status: 'geprueft', block_id: 49, ort: 'z1', ort_titel: 'Natürliche und ganze Zahlen', titel: 'Natürliche Zahlen', ziel: 'Große Zahlen lesen.', pflicht_anzahl: 4 },
      { id: 3, status: 'entwurf', block_id: 60, ort: 'a3', ort_titel: 'Terme', titel: 'Terme umformen', ziel: 'Terme umformen.', pflicht_anzahl: 8 }],
      lernende: [{ id: 1, name: 'Kind A', ist_test: false, route: [], stand: [{ einheit_id: 1, fertig: 2, fehler: 1, gesichert: 0, blocktest: true, laeuft: false }] },
        { id: 3, name: 'Testkind', ist_test: true, route: [], stand: [] }] };
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

test('Lernen: Übersicht zeigt Kinder, Fortschritt und Entwürfe nur beim Testkind', async (t) => {
  const { page } = await setup(t);
  await page.goto(origin + '/#/lernen');
  await page.getByRole('tab', { name: 'Kind A' }).waitFor();
  await page.getByText('2 von 4 Lernzielen geschafft').waitFor();
  assert.equal(await page.getByText('Terme umformen', { exact: true }).count(), 0);
  await page.getByRole('tab', { name: /Testkind/ }).click();
  await page.getByText('Terme umformen', { exact: true }).waitFor();
  assert.equal(await page.locator('.pill', { hasText: 'Entwurf' }).count(), 1);
  const w = await page.evaluate(() => document.documentElement.scrollWidth); assert.ok(w <= 390, 'keine Querverschiebung: ' + w);
});

test('Lernen: Üben mit Zahl, Zahlenstrahl und Lückenfeldern', async (t) => {
  const { page, calls } = await setup(t);
  await page.goto(origin + '/#/lerneinheit/1-1');
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
