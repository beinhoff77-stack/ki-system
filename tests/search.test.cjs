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
  try { browser = await chromium.launch({ headless: true }); }
  catch { browser = await chromium.launch({ headless: true, channel: 'msedge' }); }
});
after(async () => { await browser?.close(); await new Promise((resolve) => server?.close(resolve)); });
const hit = (id, list, price, extra = {}) => ({ treffer_id: id, name: 'Unterkunft ' + id, quelle: 'hasdata_booking', topf: 'shortlist', bewertungen: 35,
  angebot: { preis_gesamt_eur: price, link: 'https://example.com/angebot' }, bewertung: { liste: list, score: 80 + id, datenlage: 70, warnungen: [], ampel: 'gelb' }, ...extra });
const result = (status = 'fertig') => ({ ok: true, suchauftrag: { id: 2, ziel: 'Tokyo', anreise: '2026-11-01', abreise: '2026-11-08', erwachsene: 2, kinder_alter: [11], status, schrittkette: [{ quelle: 'hasdata_booking', status, treffer: 4 }] },
  kosten: { ist_usd: 0.062, limit_usd: 1.5, ist_einheiten: 20, limit_einheiten: 30 },
  treffer: [hit(1, 'A', 200), hit(2, 'A', 100), hit(3, 'A', null), hit(4, 'B', 300, { quelle: 'rakuten_travel', angebot: { preis_gesamt_eur: 300, preis_art: 'geschaetzt', schaetz_basis: 'Erste Nacht × 7', link: 'javascript:alert(1)' }, bewertung: { liste: 'B', score: 95, warnungen: ['futon', 'steuern_unklar', 'neue_warnung'] } }), hit(5, 'A', 10, { topf: 'ausgeschlossen' })] });
async function setup(t, handler, viewport) {
  const context = await browser.newContext({ viewport: viewport || { width: 1440, height: 1000 }, serviceWorkers: 'block' });
  t.after(() => context.close());
  await context.addInitScript(() => localStorage.setItem('ks_token', 'synthetic-test-session'));
  const page = await context.newPage();
  const errors = []; page.on('pageerror', (e) => errors.push(e.message)); t.after(() => assert.deepEqual(errors, []));
  const calls = [];
  await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.route('**/functions/v1/app-api/**', async (route) => {
    const request = route.request();
    const payload = request.method() === 'POST' ? request.postDataJSON() : {};
    calls.push(payload);
    let value = await handler(payload, calls);
    if (payload.aktion === 'unterkunft_suche_status' && value?.suchauftrag) {
      const a = value.suchauftrag;
      value = { ...a, fertig: ['fertig','fehler','abgebrochen','gestoppt_budget'].includes(a.status), phase: a.status === 'fertig' ? 'fertig' : 'sammeln', kosten: value.kosten, zaehler: {}, schritte: [] };
    }
    if (value === 'abort') return route.abort();
    if (value === 'unauthorized') return route.fulfill({ status: 401, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Nicht angemeldet' }) });
    if (value === 'server-error') return route.fulfill({ status: 503, contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true } }) });
    await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: value, eingerichtet: true }) });
  });
  return { page, calls };
}
async function waitForCallback(get) {
  const until = Date.now() + 5000;
  while (!get() && Date.now() < until) await new Promise(resolve => setTimeout(resolve, 10));
  assert.equal(typeof get(), 'function', 'Erwartete Testanfrage wurde nicht ausgelöst');
}
async function formFill(page) {
  await page.locator('[name=ziel]').fill('Kyoto');
  await page.locator('[name=anreise]').fill('2026-11-13');
  await page.locator('[name=abreise]').fill('2026-11-27');
  await page.locator('[name=kinder_alter]').fill('13, 11');
}
test('Formular validiert und ruft Anlegen → Starten → Lesen genau einmal auf', async (t) => {
  const { page, calls } = await setup(t, (p) => p.aktion === 'unterkunft_suchauftrag_anlegen' ? { ok: true, id: 2 } : p.aktion === 'unterkunft_suche_starten' ? { ok: true, status: 'laeuft' } : p.daten?.suchauftrag_id ? result() : { suchauftraege: [] });
  await page.goto(origin + '/#/suche'); await formFill(page);
  await page.locator('[name=kinder_alter]').fill('18'); await page.getByRole('button', { name: 'Anlegen und Suche starten' }).click();
  await page.getByRole('status').filter({ hasText: 'zwischen 0 und 17' }).waitFor();
  assert.equal(calls.filter((p) => p.aktion === 'unterkunft_suchauftrag_anlegen').length, 0);
  await page.locator('[name=kinder_alter]').fill('13, 11');
  await page.getByRole('button', { name: 'Anlegen und Suche starten' }).dblclick();
  await page.getByRole('heading', { name: 'Liste A – Rangliste (3)' }).waitFor();
  const writes = calls.filter((p) => ['unterkunft_suchauftrag_anlegen', 'unterkunft_suche_starten'].includes(p.aktion));
  assert.deepEqual(writes.map((p) => p.aktion), ['unterkunft_suchauftrag_anlegen', 'unterkunft_suche_starten']);
  assert.deepEqual(writes[0].daten.kinder_alter, [13, 11]);
  assert.equal(writes[0].daten.limit_usd, 1.5); assert.equal(writes[0].daten.schlafzimmer_min, 2);
});
test('A/B, Warnungen, sichere Links, numerische Sortierung und fehlende Werte', async (t) => {
  const data = result(); data.treffer[0].name = '<img src=x onerror=alert(1)>';
  const { page } = await setup(t, () => data);
  await page.goto(origin + '/#/suche/2');
  const a = page.locator('[data-group=A]'); await a.waitFor();
  await a.getByRole('button', { name: /Gesamtpreis/ }).click();
  assert.deepEqual(await a.locator('tbody tr td:first-child strong').allTextContents(), ['Unterkunft 2', '<img src=x onerror=alert(1)>', 'Unterkunft 3']);
  await a.getByRole('button', { name: /Gesamtpreis/ }).click();
  assert.deepEqual(await a.locator('tbody tr td:first-child strong').allTextContents(), ['<img src=x onerror=alert(1)>', 'Unterkunft 2', 'Unterkunft 3']);
  assert.equal(await page.locator('.suche img').count(), 0);
  assert.equal(await page.locator('a[href^="javascript:"]').count(), 0);
  await page.getByText('Supported by Rakuten Developers').waitFor();
  await page.getByText('ca. 300,00 € (geschätzt)', { exact: true }).waitFor();
  await page.getByText('neue_warnung', { exact: true }).waitFor();
  assert.equal(await page.locator('[data-group=ausgeschlossen] tbody tr').count(), 1);
  await page.locator('[data-group=ausgeschlossen] > summary').focus();
  await page.keyboard.press('Enter');
  assert.equal(await page.locator('[data-group=ausgeschlossen]').evaluate(n=>n.open),true);
});
test('Polling stoppt bei Endstatus und beim Seitenwechsel', async (t) => {
  let reads = 0;
  const { page } = await setup(t, (p) => p.aktion === 'unterkunft_suche_status' ? result(++reads > 1 ? 'gestoppt_budget' : 'laeuft') : p.aktion === 'unterkunft_suchlauf_lesen' ? result('gestoppt_budget') : []);
  await page.clock.install(); await page.goto(origin + '/#/suche/2');
  await page.getByRole('status').filter({ hasText: 'Suche läuft' }).waitFor();
  await page.clock.fastForward(7100);
  await page.getByRole('status').filter({ hasText: 'Kostenlimit erreicht' }).waitFor();
  await page.clock.fastForward(30000); assert.equal(reads, 2);
  reads = 0; await page.reload(); await page.getByRole('status').filter({ hasText: 'Suche läuft' }).waitFor();
  await page.locator('#areas [data-area=council]').click(); await page.getByRole('heading', { name: 'Aufträge', exact: true }).waitFor();
  await page.clock.fastForward(30000); assert.equal(reads, 1);
});
test('Startfehler behält ID und erzeugt keinen zweiten Auftrag', async (t) => {
  const { page, calls } = await setup(t, (p) => p.aktion === 'unterkunft_suchauftrag_anlegen' ? { ok: true, id: 2 } : p.aktion === 'unterkunft_suche_starten' ? 'abort' : { suchauftraege: [] });
  await page.goto(origin + '/#/suche'); await formFill(page);
  await page.getByRole('button', { name: 'Anlegen und Suche starten' }).click();
  await page.getByRole('link', { name: 'Gespeicherten Auftrag #2 öffnen' }).waitFor();
  assert.equal(await page.getByRole('button', { name: 'Anlegen und Suche starten' }).isVisible(), false);
  assert.equal(calls.filter((p) => p.aktion === 'unterkunft_suchauftrag_anlegen').length, 1);
});
test('Lesefehler behält Treffer, pausiert Polling; 401 führt zum Login', async (t) => {
  let mode = 'ok';
  const { page } = await setup(t, (p) => p.aktion ? mode === 'ok' ? result() : mode : {});
  await page.clock.install(); await page.goto(origin + '/#/suche/2'); await page.locator('[data-group=A]').waitFor();
  mode = 'abort'; await page.getByRole('button', { name: 'Aktualisieren', exact: true }).click();
  await page.getByRole('status').filter({ hasText: 'pausiert' }).waitFor();
  assert.equal(await page.locator('[data-group=A] tbody tr').count(), 3);
  mode = 'unauthorized'; await page.getByRole('button', { name: 'Aktualisieren', exact: true }).click();
  await page.getByRole('heading', { name: 'Anmelden' }).waitFor();
  assert.equal(await page.evaluate(() => localStorage.getItem('ks_token')), null);
});
test('Mobile Ansicht ohne Seitenüberlauf, Screenshot', async (t) => {
  const { page } = await setup(t, () => result(), { width: 390, height: 844 });
  await page.goto(origin + '/#/suche/2'); await page.locator('[data-group=A]').waitFor();
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/mobile.png'), fullPage: true });
  await page.setViewportSize({ width: 1366, height: 1000 });
  assert.equal(await page.locator('.suche-table-scroll').first().evaluate((n) => n.scrollWidth <= n.clientWidth), true);
  await page.screenshot({ path: path.join(root, 'test-results/desktop.png'), fullPage: true });
});
test('PWA installiert vollständige Offline-Hülle, API wird nicht gecacht', async (t) => {
  const context = await browser.newContext(); t.after(() => context.close());
  const page = await context.newPage();
  await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.route('**/functions/v1/app-api/**', (r) => r.fulfill({ contentType: 'application/json', body: '{"ok":true,"eingerichtet":true}' }));
  await page.goto(origin + '/icon.svg');
  await page.evaluate(async () => {
    await caches.open('other-app');
    await caches.open('ki-system:' + location.origin + '/another-app/:v1');
    await caches.open('ki-system:' + location.origin + '/:old');
  });
  await page.goto(origin + '/#/login');
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.waitForFunction(() => navigator.serviceWorker.controller);
  const cacheNames = await page.evaluate(() => caches.keys());
  assert(cacheNames.includes('other-app'));
  assert(cacheNames.includes('ki-system:' + origin + '/another-app/:v1'));
  assert(!cacheNames.includes('ki-system:' + origin + '/:old'));
  await page.evaluate(() => fetch('README.md'));
  const cached = await page.evaluate(async () => (await (await caches.open('ki-system:' + location.origin + '/:v18')).keys()).map((r) => new URL(r.url).pathname + new URL(r.url).search));
  assert(cached.includes('/icon-512.png')); assert(cached.includes('/app.js?v=0.11.0')); assert(cached.includes('/style.css?v=0.11.0'));
  assert(cached.includes('/stay-tools.js?v=0.11.0')); assert(cached.includes('/vendor/leaflet-1.9.4/leaflet.js')); assert(cached.includes('/vendor/leaflet-1.9.4/leaflet.css'));
  assert(!cached.includes('/README.md'));
  assert(!cached.some((u) => u.includes('app-api')));
  await context.setOffline(true); await page.reload();
  await page.getByRole('heading', { name: 'Anmelden' }).waitFor();
});

test('Update lädt neue Skripte und Gestaltung trotz frischem HTTP-Cache der Altversion', async (t) => {
  let updated = false;
  const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8').replace(/<script src="https:[^>]*><\/script>/g, '');
  const oldHtml = html.replace(/(app\.js|style\.css)\?v=[^"']+/g, '$1');
  const releaseServer = http.createServer((req, res) => {
    const name = new URL(req.url, 'http://localhost').pathname;
    if (name.endsWith('.html')) {
      res.writeHead(200, { 'Content-Type': 'text/html', 'Cache-Control': 'no-store' });
      return res.end(updated ? html : oldHtml);
    }
    if (name === '/app.js') {
      res.writeHead(200, { 'Content-Type': 'text/javascript', 'Cache-Control': 'max-age=600' });
      return res.end(`document.querySelector('#ver').textContent = '${updated ? 'aktuell' : 'alt'}';`);
    }
    if (name === '/style.css') {
      res.writeHead(200, { 'Content-Type': 'text/css', 'Cache-Control': 'max-age=600' });
      return res.end(`body { color: ${updated ? 'rgb(0, 128, 0)' : 'rgb(255, 0, 0)'}; }`);
    }
    res.writeHead(404); res.end();
  });
  await new Promise(resolve => releaseServer.listen(0, '127.0.0.1', resolve));
  const context = await browser.newContext({ serviceWorkers: 'block' });
  t.after(async () => { await context.close(); releaseServer.closeAllConnections(); await new Promise(resolve => releaseServer.close(resolve)); });
  const page = await context.newPage();
  const releaseOrigin = `http://127.0.0.1:${releaseServer.address().port}`;
  // Ohne Request-Mocking: Routing würde den HTTP-Cache abschalten und den Fehler verdecken.
  await page.goto(releaseOrigin + '/warm.html');
  assert.equal(await page.locator('#ver').textContent(), 'alt');
  assert.equal(await page.evaluate(() => getComputedStyle(document.body).color), 'rgb(255, 0, 0)');
  updated = true;
  await page.goto(releaseOrigin + '/index.html');
  assert.equal(await page.locator('#ver').textContent(), 'aktuell');
  assert.equal(await page.evaluate(() => getComputedStyle(document.body).color), 'rgb(0, 128, 0)');
});

test('Startseite trennt Council und Unterkunft; Navigation und Prototyp-Design', async (t) => {
  const { page, calls } = await setup(t, (p) => p.aktion === 'auftraege_suchen' ? [] : { suchauftraege: [] });
  await page.goto(origin + '/');
  await page.getByRole('heading', { name: 'Was möchtest du heute machen?' }).waitFor();
  assert.equal(calls.length, 0);
  fs.mkdirSync(path.join(root, 'test-results'), { recursive: true });
  await page.screenshot({ path: path.join(root, 'test-results/start-desktop.png'), fullPage: true });
  await page.locator('.stay-card').click();
  await page.getByRole('heading', { name: 'Wohnen, wo sich die Reise richtig anfühlt.' }).waitFor();
  assert.equal(await page.locator('#tabs [data-view=auftraege]').isVisible(), false);
  assert.equal(await page.locator('#tabs [data-view=ergebnisse]').isVisible(), true);
  assert.equal(await page.evaluate(() => getComputedStyle(document.body).backgroundColor), 'rgb(246, 244, 236)');
  await formFill(page);
  await page.screenshot({ path: path.join(root, 'test-results/search-desktop.png'), fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  await page.screenshot({ path: path.join(root, 'test-results/search-mobile.png'), fullPage: true });
  await page.locator('#tabs [data-view=ergebnisse]').click();
  await page.getByRole('heading', { name: 'Suchen & Ergebnisse' }).waitFor();
  assert.equal(await page.locator('[name=ziel]').count(), 0);
  await page.getByRole('link', { name: 'Erste Unterkunft suchen →' }).click();
  await page.locator('[name=ziel]').waitFor();
  await page.locator('#areas [data-area=council]').click();
  await page.getByRole('heading', { name: 'Aufträge', exact: true }).waitFor();
  assert.equal(await page.locator('#tabs [data-view=suche]').isVisible(), false);
  assert.equal(await page.locator('#tabs [data-view=auftraege]').isVisible(), true);
  await page.getByRole('link', { name: 'KI-System Startseite' }).click();
  await page.getByRole('heading', { name: 'Was möchtest du heute machen?' }).waitFor();
  await page.screenshot({ path: path.join(root, 'test-results/start-mobile.png'), fullPage: true });
});

test('Warteschlange und Bewertung nutzen nur Status; Treffer erst nach Abschluss', async (t) => {
  let count = 0;
  const { page, calls } = await setup(t, p => p.aktion === 'unterkunft_suche_status'
    ? { ...status(++count > 2 ? 'fertig' : count === 1 ? 'wartet' : 'laeuft'), warteschlange_position: 2, fortschritt: count === 2 ? 'Bewerten: läuft' : 'Vorbereitung' }
    : result());
  await page.clock.install(); await page.goto(origin + '/#/suche/2');
  await page.getByText('Status: wartet · Warteschlange: Position 2').waitFor();
  assert.equal(calls.filter(p => p.aktion === 'unterkunft_suchlauf_lesen').length, 0);
  await page.clock.fastForward(7100); await page.getByText('Bewerten: läuft', {exact:true}).waitFor();
  assert.equal(calls.filter(p => p.aktion === 'unterkunft_suchlauf_lesen').length, 0);
  await page.clock.fastForward(7100); await page.locator('[data-group=A]').waitFor();
  await page.clock.fastForward(30000);
  assert.equal(count, 3);
  assert.equal(calls.filter(p => p.aktion === 'unterkunft_suchlauf_lesen').length, 1);
});
const status = (state) => ({ ok: true, id: 2, ziel: 'Tokyo', status: state, fertig: ['fertig','fehler','abgebrochen'].includes(state), phase: state === 'fertig' ? 'fertig' : 'bewerten', kosten: {}, zaehler: {} });

test('Abbrechen einmal trotz Doppelklick, Teilergebnis bleibt vorläufig', async (t) => {
  let cancelled = false;
  const { page, calls } = await setup(t, async p => {
    if (p.aktion === 'unterkunft_suche_abbrechen') { await new Promise(r => setTimeout(r, 150)); cancelled = true; return {ok:true}; }
    if (p.aktion === 'unterkunft_suche_status') return status(cancelled ? 'abgebrochen' : 'wartet');
    return result('abgebrochen');
  });
  await page.goto(origin + '/#/suche/2');
  await page.getByRole('button', {name:'Suche abbrechen',exact:true}).dblclick();
  await page.getByRole('heading', {name:'Liste A – vorläufig (3)'}).waitFor();
  assert.equal(calls.filter(p => p.aktion === 'unterkunft_suche_abbrechen').length, 1);
  assert.equal(await page.getByRole('button', {name:'Suche abbrechen',exact:true}).isVisible(), false);
});

test('Abbruchfehler wird angezeigt und Status gelesen; kein Schreib-Retry', async (t) => {
  const {page,calls} = await setup(t, p => p.aktion === 'unterkunft_suche_abbrechen' ? 'abort' : status('laeuft'));
  await page.goto(origin + '/#/suche/2');
  await page.getByRole('button',{name:'Suche abbrechen',exact:true}).click();
  await page.getByRole('status').filter({hasText:'Abbrechen nicht bestätigt'}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suche_abbrechen').length,1);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suche_status').length,2);
});

test('Endrang, Score-Abdeckung, fünf Balken, Bildurteil und sichtbare Einwände', async (t) => {
  const r = result(); r.suchauftrag.schrittkette.push({ quelle: 'bewerten', status: 'fertig' });
  Object.assign(r.treffer[0].bewertung, { rang: 2, score: 99, spaltennoten: { raum: 0, lage: 8, preis_leistung: null, bewertungen: 7, eignung: 9, datenlage_score: 65 },
    bild_urteil: { ein_satz: 'Helles Zimmer.', zeigt: ['Zimmer'], hell: 8, modern: null, gepflegt: 7, geraeumig: 6, auffaelligkeiten: ['Fenster klein'] },
    gegenpruefung: { pruefung: { urteil: 'einwand', einwaende: ['Bettenzahl nicht belegt', '<img src=x onerror=alert(1)>'], hinweis: 'Bitte prüfen.' } } });
  r.treffer[1].bewertung.rang = 1; r.treffer[1].bewertung.score = 70;
  r.treffer[2].bewertung.rang = null;
  const { page } = await setup(t, () => r);
  await page.goto(origin + '/#/suche/2'); const a = page.locator('[data-group=A]'); await a.waitFor();
  assert.deepEqual(await a.locator('tbody tr td:first-child strong').allTextContents(), ['Unterkunft 2','Unterkunft 1','Unterkunft 3']);
  const row = a.locator('tbody tr').filter({ hasText: 'Unterkunft 1' });
  assert.equal(await row.locator('td[data-label="Datenlage (%)"]').textContent(), '65');
  assert.equal(await row.locator('.score-bars').first().locator('.score-bar-row').count(), 5);
  assert.equal(await row.locator('.score-bars').first().getByText('unbekannt', { exact: true }).count(), 1);
  assert.equal(await row.locator('meter[value="0"]').count(), 1);
  await row.locator('.review-objection').getByText('Bettenzahl nicht belegt').waitFor();
  assert.equal(await page.locator('.suche img').count(), 0);
  await row.locator('summary').click(); await row.getByText('Helles Zimmer.', { exact: true }).waitFor();
  await row.getByText('Fenster klein', { exact: true }).waitFor();
  await page.evaluate(() => scrollTo(0, 0));
  await page.screenshot({ path: path.join(root, 'test-results/ranking-desktop.png'), fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.evaluate(() => scrollTo(0, 0));
  assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth), true);
  await page.screenshot({ path: path.join(root, 'test-results/ranking-mobile.png'), fullPage: true });
});


test('Fehler lädt Teilergebnis; ungültige Statusantwort lädt keine Treffer', async (t) => {
  let malformed = false;
  const {page,calls} = await setup(t, p => p.aktion === 'unterkunft_suche_status' ? malformed ? {status:'laeuft'} : status('fehler') : result('fehler'));
  await page.goto(origin + '/#/suche/2');
  await page.getByRole('heading',{name:'Liste A – vorläufig (3)'}).waitFor();
  malformed = true;
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await page.getByRole('status').filter({hasText:'Statusantwort unvollständig'}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchlauf_lesen').length,1);
  assert.equal(await page.locator('[data-group=A] tbody tr').count(),3);
});

test('Entwurf startet erst auf Klick, wartende Suche startet nicht erneut', async (t) => {
  let started=false;
  const {page,calls} = await setup(t,p=> {
    if(p.aktion==='unterkunft_suche_starten') {started=true;return {ok:true,status:'wartet'};}
    return status(started?'wartet':'entwurf');
  });
  await page.goto(origin + '/#/suche/2');
  await page.getByRole('button',{name:'Diesen Entwurf starten'}).click();
  await page.getByRole('status').filter({hasText:'startet automatisch'}).waitFor();
  assert.equal(await page.getByRole('button',{name:'Diesen Entwurf starten'}).isVisible(),false);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suche_starten').length,1);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchlauf_lesen').length,0);
});


test('Rückmeldung: bestehendes Urteil, Grund, Doppelklick, Sortieren und Fehler', async (t) => {
  const r=result(); r.treffer[0].rueckmeldung={urteil:'passt',grund:'Balkon'};
  let fail=false;
  const {page,calls}=await setup(t, async p=> {
    if(p.aktion==='unterkunft_rueckmeldung_geben') {
      await new Promise(resolve=>setTimeout(resolve,200));
      return fail ? 'abort' : {ok:true};
    }
    return r;
  });
  await page.goto(origin+'/#/suche/2');
  let box=page.locator('[data-feedback="1"]');
  await box.getByRole('button',{name:'Passt',exact:true}).waitFor();
  assert.equal(await box.getByRole('button',{name:'Passt',exact:true}).getAttribute('aria-pressed'),'true');
  await box.locator('textarea').fill('Zu weit vom Bahnhof');
  await page.locator('[data-group=A]').getByRole('button',{name:/Gesamtpreis/}).click();
  assert.equal(await box.locator('textarea').inputValue(),'Zu weit vom Bahnhof');
  await box.getByRole('button',{name:'Zu teuer',exact:true}).dblclick();
  await box.getByRole('status').filter({hasText:'Gespeichert: Zu teuer'}).waitFor();
  const writes=calls.filter(p=>p.aktion==='unterkunft_rueckmeldung_geben');
  assert.equal(writes.length,1);
  assert.deepEqual(writes[0].daten,{treffer_id:1,urteil:'zu_teuer',grund:'Zu weit vom Bahnhof'});
  fail=true;
  await box.getByRole('button',{name:'Gebucht',exact:true}).click();
  await box.getByRole('status').filter({hasText:'Speichern nicht bestätigt'}).waitFor();
  assert.equal(await box.getByRole('button',{name:'Zu teuer',exact:true}).getAttribute('aria-pressed'),'true');
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_rueckmeldung_geben').length,2);
});

test('Bericht unverändert, nur auf Klick; Gehzeit und weitere Angebote sicher', async (t) => {
  const r=result(); Object.assign(r.treffer[0],{gehzeit_min:7,gehzeit_art:'geschaetzt',station_name:'Testbahnhof',weitere_angebote:[
    {anbieter:'<img src=x onerror=alert(1)>',preis_gesamt_eur:123,preis_art:'geschaetzt',link:'javascript:alert(1)',hinweis:'Zimmer nicht abgeglichen'},
    {anbieter:'Zweitquelle',preis_gesamt_eur:150,link:'https://example.com/zweites'}]});
  let ready=false;
  const source='## Auswertung\n\n| Merkmal | Passt |\n|---|---|\n| Hell | 8 |';
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_rueckmeldung_report'?{bereit:ready,text:ready?source:'Noch zu wenige Urteile: 0 von 20.'}:r);
  await page.goto(origin+'/#/suche/2');
  await page.getByText('ca. 7 Min. zu Fuß · Testbahnhof (geschätzt)',{exact:true}).waitFor();
  await page.getByText('Weitere Angebote (2)',{exact:true}).click();
  await page.getByText('ca. 123,00 € (geschätzt)',{exact:true}).waitFor();
  assert.equal(await page.locator('a[href^="javascript:"]').count(),0);
  assert.equal(await page.locator('.suche img').count(),0);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_rueckmeldung_report').length,0);
  await page.getByText('Deine Rückmeldungen auswerten',{exact:true}).click();
  await page.getByRole('button',{name:'Rückmeldungsbericht laden'}).click();
  await page.getByText('Noch zu wenige Urteile: 0 von 20.',{exact:true}).waitFor();
  ready=true;await page.getByRole('button',{name:'Rückmeldungsbericht laden'}).click();
  await page.locator('.feedback-report pre').filter({hasText:'Auswertung'}).waitFor();
  assert.equal(await page.locator('.feedback-report').textContent(),source);
  await page.evaluate(()=>{ window.marked={parse:()=>'<h2 onclick="alert(1)">Bericht</h2><img src=x onerror="alert(1)"><a href="javascript:alert(1)">Text</a><table><tr><td>8</td></tr></table>'}; });
  await page.getByRole('button',{name:'Rückmeldungsbericht laden'}).click();
  await page.locator('.feedback-report h2').waitFor();
  assert.equal(await page.locator('.feedback-report [onclick], .feedback-report img, .feedback-report a').count(),0);
  await page.setViewportSize({width:390,height:844});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:path.join(root,'test-results/feedback-mobile.png'),fullPage:true});
});


test('Schmale Handys: lesbare Karten, Touchflächen, Formular und Tastaturfokus', async (t) => {
  const {page}=await setup(t,p=>p.daten?.suchauftrag_id?result():{suchauftraege:[]});
  for(const width of [320,375,430]) {
    await page.setViewportSize({width,height:844});
    await page.goto(origin+'/#/suche/2'); await page.locator('[data-group=A]').waitFor();
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
    const buttons=page.locator('[data-group=A] thead button, [data-group=A] caption button, [data-feedback="1"] button');
    for(const size of await buttons.evaluateAll(nodes=>nodes.map(n=>n.getBoundingClientRect().height))) assert(size>=44);
    assert.equal(await page.locator('[data-group=A] td').first().evaluate(n=>parseFloat(getComputedStyle(n).fontSize)>=14),true);
    await page.goto(origin+'/#/suche'); await page.locator('[name=ziel]').waitFor();
    await page.locator('[name=ziel]').focus(); await page.keyboard.press('Tab');
    assert.equal(await page.locator('[name=land]').evaluate(n=>document.activeElement===n),true);
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  }
  await page.setViewportSize({width:390,height:844});
  await page.goto(origin+'/#/suche/2'); await page.locator('[data-feedback="1"]').waitFor();
  await page.locator('[data-feedback="1"]').scrollIntoViewIfNeeded();
  await page.screenshot({path:path.join(root,'test-results/mobile-feedback-viewport.png')});
});

test('Startfehler beim gespeicherten Entwurf bleibt nach Statusabfrage sichtbar', async (t) => {
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_suche_starten'?'abort':status('entwurf'));
  await page.goto(origin+'/#/suche/2');
  await page.getByRole('button',{name:'Diesen Entwurf starten'}).click();
  await page.getByRole('status').filter({hasText:'Start nicht bestätigt'}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suche_starten').length,1);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suche_status').length,2);
});

test('Große Listen: global sortieren, filtern, blättern; Teilnoten und Gehzeit', async (t) => {
  const r = result();
  r.treffer = Array.from({length: 105}, (_, i) => hit(i + 1, 'A', i + 1, { gehzeit_min: 106 - i,
    bewertung: { liste: 'A', score: 70, rang: i + 1, spaltennoten: { raum: i === 104 ? 10 : 3 } } }));
  const {page} = await setup(t, () => r, {width:390,height:844});
  await page.goto(origin + '/#/suche/2');
  const a = page.locator('[data-group=A]'); await a.waitFor();
  assert.equal(await a.locator('tbody tr').count(),10);
  await a.getByRole('button',{name:'Nächste Seite'}).click();
  assert.equal(await a.locator('tbody tr td:first-child strong').first().textContent(),'Unterkunft 11');
  await page.getByLabel('Sortieren nach',{exact:true}).selectOption('note_raum');
  assert.equal(await a.locator('tbody tr td:first-child strong').first().textContent(),'Unterkunft 105');
  await page.getByLabel('Sortieren nach',{exact:true}).selectOption('gehzeit');
  assert.equal(await a.locator('tbody tr td:first-child strong').first().textContent(),'Unterkunft 105');
  await page.getByLabel('Treffer filtern',{exact:true}).fill('Unterkunft 105');
  assert.equal(await a.locator('tbody tr').count(),1);
  await page.getByLabel('Treffer filtern',{exact:true}).fill('Kein solcher Name');
  await a.getByText('Keine Treffer für diesen Filter.').waitFor();
  await page.getByLabel('Treffer filtern',{exact:true}).fill('');
  await page.getByLabel('Treffer je Liste und Seite').selectOption('25');
  assert.equal(await a.locator('tbody tr').count(),25);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.evaluate(()=>scrollTo(0,0));
  await page.screenshot({path:path.join(root,'test-results/review-mobile.png')});
  await page.setViewportSize({width:768,height:1024});
  await a.locator('tbody tr').first().scrollIntoViewIfNeeded();
  await page.screenshot({path:path.join(root,'test-results/review-tablet.png')});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  for (const width of [600,768,1024]) {
    await page.setViewportSize({width,height:1024});
    assert.equal(await a.locator('tbody tr').first().evaluate(n=>getComputedStyle(n).display),'grid');
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  }
});

test('Rückmeldung aktualisiert Serverstand und erhält ungespeicherten Grund', async (t) => {
  const r = result(); r.treffer[0].rueckmeldung = {urteil:'passt',grund:'Alt'};
  const {page} = await setup(t, () => r);
  await page.goto(origin + '/#/suche/2');
  const box = page.locator('[data-feedback="1"]'); await box.waitFor();
  await box.locator('textarea').fill('Mein noch nicht gespeicherter Grund');
  r.treffer[0].rueckmeldung = {urteil:'gebucht',grund:'Anderes Gerät'};
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await box.getByRole('status').filter({hasText:'Deine Rückmeldung: Gebucht'}).waitFor();
  assert.equal(await box.locator('textarea').inputValue(),'Mein noch nicht gespeicherter Grund');
  await box.locator('textarea').fill('Anderes Gerät');
  r.treffer[0].rueckmeldung = {urteil:'zu_teuer',grund:'Neuer Serverstand'};
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await box.getByRole('status').filter({hasText:'Deine Rückmeldung: Zu teuer'}).waitFor();
  assert.equal(await box.locator('textarea').inputValue(),'Neuer Serverstand');
});

test('Späte Leseantwort überschreibt keine gerade gespeicherte Rückmeldung', async (t) => {
  const r = result(); let hold = false, releaseRead, releaseWrite;
  const {page,calls} = await setup(t, async p => {
    if (p.aktion === 'unterkunft_suchlauf_lesen' && hold) await new Promise(resolve => {releaseRead=resolve;});
    if (p.aktion === 'unterkunft_rueckmeldung_geben') {
      await new Promise(resolve => {releaseWrite=resolve;}); return {ok:true};
    }
    return r;
  });
  await page.goto(origin + '/#/suche/2');
  const box=page.locator('[data-feedback="1"]'); await box.waitFor();
  hold=true; await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await waitForCallback(()=>releaseRead);
  await box.getByRole('button',{name:'Passt',exact:true}).click();
  await waitForCallback(()=>releaseWrite);
  await page.getByLabel('Sortieren nach',{exact:true}).selectOption('preis');
  assert.equal(await box.getByRole('button',{name:'Passt',exact:true}).isDisabled(),true);
  releaseWrite(); await box.getByRole('status').filter({hasText:'Gespeichert: Passt'}).waitFor();
  releaseRead(); await page.getByRole('status').filter({hasText:'Rangliste aktualisiert'}).waitFor();
  assert.equal(await box.getByRole('button',{name:'Passt',exact:true}).getAttribute('aria-pressed'),'true');
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_rueckmeldung_geben').length,1);
});

test('HTTP-Fehler und leere Schreibantworten werden nicht als gespeichert angezeigt', async (t) => {
  let response='server-error';
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_rueckmeldung_geben'?response:result());
  await page.goto(origin + '/#/suche/2');
  const box=page.locator('[data-feedback="1"]'); await box.waitFor();
  await box.getByRole('button',{name:'Passt',exact:true}).click();
  await box.getByRole('status').filter({hasText:'HTTP 503'}).waitFor();
  response=undefined;
  await box.getByRole('button',{name:'Gebucht',exact:true}).click();
  await box.getByRole('status').filter({hasText:'nicht bestätigen'}).waitFor();
  assert.equal(await box.locator('[aria-pressed=true]').count(),0);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_rueckmeldung_geben').length,2);
});

test('Unvollständige Bewertungsfelder und falsche Zahlen zerstören keine Trefferliste', async (t) => {
  const r=result();
  r.treffer[0].angebot.preis_gesamt_eur=false;
  r.treffer[0].bewertung.bild_urteil={auffaelligkeiten:'Helles Fenster'};
  r.treffer[0].bewertung.gegenpruefung={luecken:'Betten fehlen'};
  r.treffer[0].bewertung.spaltennoten={raum:false,lage:' ',eignung:0};
  const {page}=await setup(t,()=>r);
  await page.goto(origin+'/#/suche/2');
  const row=page.locator('[data-group=A] tbody tr').first();
  await row.waitFor();
  assert.equal(await row.locator('td[data-label=Gesamtpreis]').textContent(),'Preis unbekannt');
  assert.equal(await row.locator('meter[value="0"]').count(),1);
  await row.getByText('Angaben und Prüfungen',{exact:true}).click();
  await row.getByText('Helles Fenster',{exact:true}).waitFor();
  await row.getByText('Offene Prüfpunkte: Betten fehlen',{exact:true}).waitFor();
});

test('Council-Markdown behält sichere Links und entfernt ausführbare Inhalte', async (t) => {
  const {page}=await setup(t,()=>[]);
  await page.goto(origin+'/#/start');
  await page.evaluate(()=>{
    window.marked={parse:value=>value};
    document.querySelector('#main').replaceChildren(md('<h2 onclick="window.injected=1">Antwort</h2><a href="https://example.com/beleg">Quelle</a><a href="javascript:alert(1)">Unsicher</a><img src=x onerror="window.injected=1"><script>window.injected=1<\/script><table><tr><td>Wert</td></tr></table>'));
  });
  await page.getByRole('link',{name:'Quelle'}).waitFor();
  assert.equal(await page.locator('#main [onclick], #main img, #main script, #main a[href^="javascript:"]').count(),0);
  assert.equal(await page.evaluate(()=>window.injected),undefined);
  assert.equal(await page.getByRole('link',{name:'Quelle'}).getAttribute('rel'),'noopener noreferrer');
  await page.getByRole('cell',{name:'Wert'}).waitFor();
});

test('Gehzeit: route ist berechnet, geschaetzt trägt ca., unbekannte Arten bleiben offen', async (t) => {
  const r=result();
  Object.assign(r.treffer[0],{gehzeit_min:8,gehzeit_art:'route',station_name:'Station A'});
  Object.assign(r.treffer[1],{gehzeit_min:9,gehzeit_art:'geschaetzt',station_name:'Station B'});
  Object.assign(r.treffer[2],{gehzeit_min:10,gehzeit_art:'andere',station_name:'Station C'});
  const {page}=await setup(t,()=>r);
  await page.goto(origin+'/#/suche/2');
  await page.getByText('8 Min. zu Fuß · Station A (berechneter Fußweg)',{exact:true}).waitFor();
  await page.getByText('ca. 9 Min. zu Fuß · Station B (geschätzt)',{exact:true}).waitFor();
  await page.getByText('10 Min. zu Fuß · Station C (Art unbekannt)',{exact:true}).waitFor();
});

test('Unbewertete Treffer mit vorläufigem A/B-Kennzeichen bleiben außerhalb der Ranglisten', async (t) => {
  const r=result();
  r.treffer.push(hit(6,'A',100,{topf:'unbewertet'}),hit(7,'B',110,{topf:'unbewertet'}));
  const {page}=await setup(t,()=>r);
  await page.goto(origin+'/#/suche/2');
  await page.getByRole('heading',{name:'Liste A – Rangliste (3)',exact:true}).waitFor();
  await page.getByRole('heading',{name:'Liste B – Angaben prüfen (1)',exact:true}).waitFor();
  await page.getByRole('heading',{name:'Weitere Treffer – noch nicht vollständig bewertet (2)',exact:true}).waitFor();
  assert.deepEqual(await page.locator('[data-group=offen] tbody tr td:first-child strong').allTextContents(),['Unterkunft 6','Unterkunft 7']);
  await page.locator('[data-group=offen]').getByRole('button',{name:/Score \(Zwischenstand\)/}).waitFor();
});

test('Bereichswechsel: verspätete Council-Antworten und Fehler lassen Unterkunft stehen', async (t) => {
  let release, response=[];
  const {page}=await setup(t,async p=>{
    if(p.aktion==='auftraege_suchen') { await new Promise(resolve=>{release=resolve;}); return response; }
    return {suchauftraege:[]};
  });
  for (response of [[], 'abort']) {
    release=null;await page.goto(origin+'/#/auftraege');
    await page.locator('#areas [data-area=unterkunft]').click();
    await page.getByRole('heading',{name:'Wohnen, wo sich die Reise richtig anfühlt.'}).waitFor();
    await waitForCallback(()=>release);
    const delivered=page.waitForEvent(response==='abort'?'requestfailed':'response', event=>{
      const request=response==='abort'?event:event.request();
      return request.postDataJSON()?.aktion==='auftraege_suchen';
    });
    release(); await delivered;
    await page.getByLabel('Zielort',{exact:true}).fill('Kyoto');
    assert.equal(await page.locator('.suche-form').count(),1);
    assert.equal(await page.locator('#main > .err-text').count(),0);
  }
});

const testPixel = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jZAAAAABJRU5ErkJggg==', 'base64');
const mapResult = () => ({ ...result(), karte: { ziel: { name: 'Testziel', lat: 35, lon: 135 }, stationen: [{ name: 'Teststation', lat: 35.002, lon: 135.002 }] },
  treffer: [ ...Array.from({length: 14}, (_, i) => hit(i+1, 'A', (i+1)*100, {lat: 35 + i*0.001, lon: 135, luftlinie_ziel_m: i*120, bewertung: {liste:'A',rang:i+1,score:90,datenlage:80}})),
    hit(15,'B',1500,{lat:35,lon:135.005}), hit(16,'A',100,{topf:'ausgeschlossen',lat:35,lon:135.006}),
    hit(17,'B',100,{status:'ausgeschlossen',lat:35,lon:135.007}), hit(18,'B',100,{lat:91,lon:135}),
    hit(19,'B',100,{lat:0,lon:0,luftlinie_ziel_m:12000000}), hit(20,'A',null,{topf:'unbewertet',lat:35,lon:135.008}) ] });

test('Fotos: HTTPS-Hotlink, kein Referrer, verzögertes Laden und sichere Platzhalter', async (t) => {
  const data = result();
  data.treffer[0].bild = 'https://images.example/photo.png'; data.treffer[0].bild_quelle = 'hasdata_booking';
  data.treffer[1].bild = 'javascript:alert(1)'; data.treffer[2].bild = 'https://u:p@images.example/private.png';
  data.treffer[3].bild = 'https://images.example/missing.png';
  const {page} = await setup(t, () => data);
  const imageRequests=[];
  await page.route('https://images.example/**', r => { imageRequests.push(r.request()); const missing=r.request().url().includes('missing'); return r.fulfill({status:missing?404:200,contentType:'image/png',body:missing?Buffer.from('missing'):testPixel}); });
  await page.goto(origin+'/#/suche/2'); await page.locator('[data-hit="1"] img').waitFor();
  const photo = page.locator('[data-hit="1"] img'); await photo.scrollIntoViewIfNeeded();
  await page.waitForFunction(()=>document.querySelector('[data-hit="1"] img')?.complete);
  assert.equal(await photo.getAttribute('loading'),'lazy'); assert.equal(await photo.getAttribute('referrerpolicy'),'no-referrer');
  assert.equal(await photo.getAttribute('alt'),'Foto von Unterkunft 1');
  assert.equal(await page.locator('[data-hit="2"] img,[data-hit="3"] img').count(),0);
  await page.locator('[data-hit="4"]').scrollIntoViewIfNeeded();
  await page.locator('[data-hit="4"] .photo-missing').waitFor();
  assert(imageRequests.some(r=>r.url().endsWith('photo.png')));
  assert(imageRequests.every(r=>!r.headers().referer));
  assert(!imageRequests.some(r=>r.url().includes('private')));
});

test('Karte lädt erst auf Klick, zeigt gefilterte aktive Treffer und springt zur richtigen Listenseite', async (t) => {
  const {page}=await setup(t,()=>mapResult()); let tiles=0;
  await page.route('https://tile.openstreetmap.org/**', r=>{tiles++;return r.fulfill({contentType:'image/png',body:testPixel});});
  await page.goto(origin+'/#/suche/2'); await page.locator('[data-group=A]').waitFor();
  assert.equal(tiles,0);
  await page.getByRole('button',{name:'Karte',exact:true}).click();
  await page.locator('[data-map-hit="12"]').waitFor();
  assert.equal(await page.locator('[data-map-hit]').count(),17);
  assert.equal(await page.locator('[data-map-hit="16"],[data-map-hit="17"],[data-map-hit="18"]').count(),0);
  assert.equal(await page.locator('[data-map-hit="19"]').count(),1);
  await page.getByText('17 von 18 aktiven Treffern auf der Karte.',{exact:false}).waitFor();
  await page.getByText('1 weit außerhalb',{exact:false}).waitFor();
  assert.equal(await page.locator('.leaflet-control-attribution a[href="https://www.openstreetmap.org/copyright"]').isVisible(),true);
  await page.locator('[data-map-hit="12"]').click();
  await page.getByRole('button',{name:'In der Ergebnisliste zeigen'}).click();
  assert.equal(await page.locator('[data-group=A] [data-hit="12"]').isVisible(),true);
  assert.equal(await page.evaluate(()=>document.activeElement.dataset.hit),'12');
  await page.getByRole('button',{name:'Karte',exact:true}).click();
  await page.getByPlaceholder('Name oder Anbieter').fill('Unterkunft 15');
  assert.equal(await page.locator('[data-map-hit]').count(),1);
  assert.equal(await page.locator('[data-map-hit="15"]').count(),1);
  await page.getByRole('button',{name:'Liste / Tabelle'}).click();
  assert.deepEqual(await page.locator('tbody tr').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['15']);
  assert(tiles>0);
  await page.locator('#areas [data-area=council]').click();
  await page.getByRole('heading',{name:'Aufträge',exact:true}).waitFor();
  assert.equal(await page.locator('.stay-map').count(),0);
});

test('Karte bleibt bei fehlendem Hintergrund nutzbar und passt auf ein schmales Handy', async (t) => {
  const {page}=await setup(t,()=>mapResult(),{width:320,height:800});
  await page.route('https://tile.openstreetmap.org/**', r=>r.abort());
  await page.goto(origin+'/#/suche/2'); await page.getByRole('button',{name:'Karte',exact:true}).click();
  await page.getByText('Der Kartenhintergrund ist gerade nicht erreichbar.',{exact:false}).waitFor();
  assert.equal(await page.locator('[data-map-hit]').count(),17);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  fs.mkdirSync(path.join(root,'test-results'),{recursive:true});
  await page.locator('.stay-map-panel').screenshot({path:path.join(root,'test-results/map-mobile.png')});
  await page.getByLabel('Stationen anzeigen').uncheck();
  assert.equal(await page.locator('.leaflet-overlay-pane path').count(),0);
  await page.getByRole('button',{name:'Liste / Tabelle'}).click();
  assert.equal(await page.locator('[data-group=A]').isVisible(),true);
});

test('Favorit, Ausschließen und Rückgängig speichern bestätigte Zustände ohne doppelten Schreibaufruf', async (t) => {
  let releaseWrite;
  const {page,calls}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_treffer_status_setzen') { if(p.daten.status==='favorit'&&!releaseWrite) await new Promise(resolve=>{releaseWrite=resolve;}); return {ok:true,...p.daten}; }
    return result();
  });
  await page.goto(origin+'/#/suche/2');
  const selection=page.locator('[data-selection="1"]');
  await selection.getByRole('button',{name:'☆ Merken',exact:true}).dblclick();
  await waitForCallback(()=>releaseWrite);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_treffer_status_setzen').length,1);
  assert.equal(await selection.getByRole('button',{name:'☆ Merken',exact:true}).isDisabled(),true);
  releaseWrite(); await selection.getByRole('button',{name:'★ Gemerkt',exact:true}).waitFor();
  await selection.getByRole('button',{name:'Ausschließen',exact:true}).click();
  await page.getByRole('heading',{name:'Liste A – Rangliste (2)'}).waitFor();
  assert.equal(await page.locator('[data-group=A] [data-hit="1"]').count(),0);
  await page.getByRole('button',{name:'Letzte Auswahl rückgängig'}).click();
  await page.locator('[data-group=A] [data-selection="1"]').getByRole('button',{name:'★ Gemerkt',exact:true}).waitFor();
  assert.deepEqual(calls.filter(p=>p.aktion==='unterkunft_treffer_status_setzen').map(p=>p.daten.status),['favorit','ausgeschlossen','favorit']);
  await page.locator('.stay-filters summary').click(); await page.getByLabel('Nur Gemerkte',{exact:true}).check();
  assert.deepEqual(await page.locator('tbody tr').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1']);
});

test('Unklare Auswahlantwort sperrt weitere Änderungen bis zum Lesen des Serverzustands', async (t) => {
  let saved=false;
  const {page,calls}=await setup(t,p=>{
    if(p.aktion==='unterkunft_treffer_status_setzen') {saved=true;return {ok:true};}
    const data=result(); if(saved)data.treffer[0].status='favorit'; return data;
  });
  await page.goto(origin+'/#/suche/2');
  await page.locator('[data-selection="1"]').getByRole('button',{name:'☆ Merken',exact:true}).click();
  await page.locator('[data-selection="1"]').getByText('Bitte zuerst aktualisieren.',{exact:false}).waitFor();
  assert.equal(await page.locator('[data-selection="1"]').getByRole('button',{name:'☆ Merken',exact:true}).isDisabled(),true);
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Gemerkt',exact:true}).waitFor();
  assert.equal(await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Gemerkt',exact:true}).isDisabled(),false);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_treffer_status_setzen').length,1);
});

test('Verspätetes Lesen überschreibt keine inzwischen gespeicherte Auswahl; neueres Lesen wird übernommen', async (t) => {
  let reads=0, releaseRead, laterStatus='aktiv';
  const {page}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_treffer_status_setzen') return {ok:true,...p.daten};
    if(p.aktion==='unterkunft_suchlauf_lesen'&&++reads===2) await new Promise(resolve=>{releaseRead=resolve;});
    const data=result(); data.treffer[0].status=laterStatus;return data;
  });
  await page.goto(origin+'/#/suche/2'); await page.locator('[data-selection="1"]').waitFor();
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click(); await waitForCallback(()=>releaseRead);
  await page.locator('[data-selection="1"]').getByRole('button',{name:'☆ Merken',exact:true}).click();
  await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Gemerkt',exact:true}).waitFor();
  releaseRead(); await page.getByRole('button',{name:'Aktualisieren',exact:true}).waitFor({state:'visible'});
  await page.waitForFunction(()=>!Array.from(document.querySelectorAll('button')).find(b=>b.textContent==='Aktualisieren')?.disabled);
  assert.equal(await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Gemerkt',exact:true}).count(),1);
  laterStatus='ausgeschlossen'; await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await page.locator('[data-group=ausgeschlossen] > summary').click();
  await page.locator('[data-selection="1"]').getByRole('button',{name:'Wiederherstellen'}).waitFor();
  assert.equal(await page.locator('[data-group=A] [data-hit="1"]').count(),0);
  assert.equal(await page.locator('[data-selection="5"]').getByRole('button',{name:'☆ Merken',exact:true}).isDisabled(),true);
});

test('Weitere Filter: vergleichbare Noten, unbekannte Zahlen, Hotelsterne und gespeicherte Ansicht', async (t) => {
  const data=result();
  data.treffer=[hit(1,'A',200,{typ:'hotel',sterne:4,note:4.5,note_skala:5,gehzeit_min:5,bewertungen:80}),
    hit(2,'A',100,{typ:'hotel',sterne:3,note:8,note_skala:10,gehzeit_min:10,bewertungen:30}),
    hit(3,'B',null,{typ:'apartment',sterne:null,note:null,note_skala:null,gehzeit_min:null,bewertungen:null})];
  const {page}=await setup(t,()=>data);
  await page.addInitScript(()=>{if(!sessionStorage.getItem('ks_suche_view:2'))sessionStorage.setItem('ks_suche_view:2',JSON.stringify({filters:null}));});
  await page.goto(origin+'/#/suche/2'); await page.locator('.stay-filters summary').click();
  await page.getByLabel('Gästenote mindestens (von 10)',{exact:true}).fill('8.5');
  await page.getByLabel('Hotelsterne mindestens',{exact:true}).selectOption('4');
  assert.deepEqual(await page.locator('tbody tr').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1','3']);
  await page.getByLabel('Unbekannte Angaben mit anzeigen',{exact:true}).uncheck();
  assert.deepEqual(await page.locator('tbody tr').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1']);
  await page.reload(); await page.locator('[data-hit="1"]').waitFor();
  assert.deepEqual(await page.locator('tbody tr').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1']);
  await page.locator('.stay-filters summary').click();
  assert.equal(await page.getByLabel('Gästenote mindestens (von 10)',{exact:true}).inputValue(),'8.5');
  await page.getByRole('button',{name:'Weitere Filter zurücksetzen'}).click();
  await page.getByLabel('Gesamtpreis höchstens (€)',{exact:true}).fill('150');
  assert.deepEqual(await page.locator('tbody tr').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['2','3']);
  await page.getByLabel('Unterkunftsform',{exact:true}).selectOption('hotel');
  assert.deepEqual(await page.locator('tbody tr').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['2']);
  await page.getByLabel('Gehzeit zur Station höchstens (Min.)',{exact:true}).fill('0');
  assert.equal(await page.locator('tbody tr').count(),0);
});
