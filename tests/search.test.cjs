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
  try { browser = await chromium.launch({ headless: true, ...(process.env.PW_TEST_EXECUTABLE ? {executablePath:process.env.PW_TEST_EXECUTABLE} : {}) }); }
  catch { browser = await chromium.launch({ headless: true, channel: 'msedge' }); }
});
after(async () => { await browser?.close(); await new Promise((resolve) => server?.close(resolve)); });
const hit = (id, list, price, extra = {}) => ({ treffer_id: id, name: 'Unterkunft ' + id, quelle: 'hasdata_booking', topf: 'shortlist', bewertungen: 35,
  angebot: { preis_gesamt_eur: price, link: 'https://example.com/angebot' }, bewertung: { liste: list, score: 80 + id, datenlage: 70, warnungen: [], ampel: 'gelb' }, ...extra });
const result = (status = 'fertig') => ({ ok: true, suchauftrag: { id: 2, ziel: 'Tokyo', anreise: '2026-11-01', abreise: '2026-11-08', erwachsene: 2, kinder_alter: [11], status, schrittkette: [{ quelle: 'hasdata_booking', status, treffer: 4 }] },
  kosten: { ist_usd: 0.062, limit_usd: 1.5, ist_einheiten: 20, limit_einheiten: 30 },
  treffer: [hit(1, 'A', 200), hit(2, 'A', 100), hit(3, 'A', null), hit(4, 'B', 300, { quelle: 'rakuten_travel', angebot: { preis_gesamt_eur: 300, preis_art: 'geschaetzt', schaetz_basis: 'Erste Nacht × 7', link: 'javascript:alert(1)' }, bewertung: { liste: 'B', score: 95, warnungen: ['futon', 'steuern_unklar', 'neue_warnung'] } }), hit(5, 'A', 10, { topf: 'ausgeschlossen' })] });
const profileCatalog = (profile=[]) => ({ok:true,profile,reisearten:{hauptart:['staedte'],hauptart_ab_v11:['roadtrip','strand','erholung','tauchen','natur'],nebenart:['erholung','strand','tauchen','natur','roadtrip'],nebenart_anteil:{min:10,max:50,standard:30}},unterkunftsform:['alle','hotel','apartment','haus'],kriterien_katalog:{
  raum:{schlafzimmer:{typ:'zahl',label:'Schlafzimmer mindestens'},flaeche_m2:{typ:'zahl',label:'Wohnfläche mindestens (m²)'},echte_betten:{typ:'ja',label:'Echte Betten für alle'}},
  lage:{gehzeit_max_min:{typ:'zahl',label:'Gehzeit zur Station höchstens (Min.)'},luftlinie_max_km:{typ:'zahl',label:'Luftlinie zum Ziel höchstens (km)'}},
  preis:{storno_kostenlos:{typ:'ja',label:'Kostenlose Stornierung'}},bewertungen:{note_min:{typ:'zahl',label:'Note mindestens (0–10)'},bewertungen_min:{typ:'zahl',label:'Anzahl Bewertungen mindestens'}},
  ausstattung:{suite:{typ:'ja',label:'Suite (nur Wunsch)'},balkon:{typ:'ja',label:'Balkon'},pool:{typ:'ja',label:'Pool'},klima:{typ:'ja',label:'Klimaanlage'},kueche:{typ:'ja',label:'Küche'},parkplatz:{typ:'ja',label:'Parkplatz'},waschmaschine:{typ:'ja',label:'Waschmaschine'}} }});
const districtCatalog = (profile=[]) => {
  const data=profileCatalog(profile);
  data.kriterien_katalog.viertel={viertel_auswahl:{typ:'liste',label:'Viertelauswahl'},viertel_ruhig:{typ:'ja',label:'Ruhiges Viertel'},viertel_oepnv_min:{typ:'zahl',label:'ÖPNV im Viertel mindestens'},viertel_gruen_min:{typ:'zahl',label:'Grün im Viertel mindestens'}};
  return data;
};
const districts = () => ({ok:true,stadt:'kyoto',hinweis:'Automatische Vorschläge sind ungeprüft. © OpenStreetMap-Mitwirkende (ODbL).',noten_regeln:'Startannahmen aus der Umgebung; Ruhe ist eine KI-Einschätzung.',filter_katalog:[],
  letzter_lauf:{id:1,status:'fertig',kosten_usd:0.06},gestrichen:[],viertel:[
    {id:21,name:'Parkviertel',name_lokal:'公園',lat:35,lon:135,radius_m:800,laerm:'ruhig',laerm_nacht:'ruhig',status:'vorschlag',charakter:'Wohnviertel',preisniveau:'mittel',beschreibung:'Ruhige Seitenstraßen.',familien_hinweis:'Wege am Fluss.',highlights:['Park'],noten:{oepnv:8,ruhe:9,nahversorgung:0},vertrauen:'mittel',koordinaten_quelle:'osm',quellen:['https://example.com/viertel','javascript:alert(1)'],suche:{treffer:12,liste_a:4,bester_rang:2,preis_nacht_median_eur:150}},
    {id:22,name:'Altstadt',lat:35.01,lon:135.01,radius_m:500,laerm:'belebt',status:'bestaetigt',noten:{oepnv:9,gruen:0,gastronomie:8},suche:{treffer:20,liste_a:5,bester_rang:1,preis_nacht_median_eur:100}},
    {id:23,name:'Hafen',lat:95,lon:135,radius_m:600,laerm:'laut',status:'vorschlag',noten:{oepnv:2,gruen:8},suche:{treffer:0,liste_a:0,bester_rang:null,preis_nacht_median_eur:null}}
  ]});
test('Viertel: KI-Fehler bleibt auch bei abgeschlossenem Umgebungslauf sichtbar', async (t) => {
  const data = districts(); data.letzter_lauf.ki = {fehler:'Budget aufgebraucht <script>window.injected=true</script>'};
  const {page,calls} = await setup(t, () => data);
  await page.goto(origin+'/#/viertel/?stadt=kyoto');
  await page.getByRole('alert').filter({hasText:'Viertel konnten nicht ermittelt werden: Budget aufgebraucht'}).waitFor();
  assert.equal(await page.locator('[data-district="21"]').count(),1);
  assert.equal(await page.evaluate(()=>window.injected),undefined);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_viertel_erstellen').length,0);
  delete data.letzter_lauf.ki;
  await page.getByRole('button',{name:'Viertel aktualisieren',exact:true}).click();
  await page.getByText('Viertel aktualisiert.',{exact:true}).waitFor();
  assert.equal(await page.getByRole('alert').count(),0);
});
async function setup(t, handler, viewport) {
  const context = await browser.newContext({ viewport: viewport || { width: 1440, height: 1000 }, serviceWorkers: 'block' });
  t.after(() => context.close());
  await context.addInitScript(() => localStorage.setItem('ks_token', 'synthetic-test-session'));
  const page = await context.newPage(); page.setDefaultTimeout(5000);
  if (process.env.PW_TEST_OFFLINE_ASSETS === '1') await page.route(origin + '/**', async route => {
    const pathname = new URL(route.request().url()).pathname;
    const file = path.resolve(root, '.' + (pathname === '/' ? '/index.html' : pathname));
    if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) return route.fulfill({status:404,body:''});
    const types = {'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png'};
    await route.fulfill({body:fs.readFileSync(file),contentType:types[path.extname(file)] || 'application/octet-stream'});
  });
  const errors = []; page.on('pageerror', (e) => errors.push(e.message)); t.after(() => assert.deepEqual(errors, []));
  const calls = [];
  await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.route('**/functions/v1/app-api/**', async (route) => {
    const request = route.request();
    const payload = request.method() === 'POST' ? request.postDataJSON() : {};
    calls.push(payload);
    let value = await handler(payload, calls);
    if (payload.aktion === 'unterkunft_suchprofile_lesen' && (value?.suchauftrag || Array.isArray(value?.suchauftraege))) value = profileCatalog();
    if (payload.aktion === 'unterkunft_lueckenfueller_lesen' && (value?.suchauftrag || Array.isArray(value?.suchauftraege))) value = {ok:true,auftraege:[]};
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
async function openHitDetails(page) {
  await page.locator('[data-hit]').first().waitFor();
  while (await page.locator('.hit-toggle:visible[aria-expanded="false"]').count()) await page.locator('.hit-toggle:visible[aria-expanded="false"]').first().click();
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
  await page.getByRole('heading', { name: 'Passende Treffer (3)' }).waitFor();
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
  await a.getByRole('button', { name: /Preis gesamt/ }).click();
  assert.deepEqual(await a.locator('tbody tr[data-hit] td:first-child strong').allTextContents(), ['Unterkunft 2', '<img src=x onerror=alert(1)>', 'Unterkunft 3']);
  await a.getByRole('button', { name: /Preis gesamt/ }).click();
  assert.deepEqual(await a.locator('tbody tr[data-hit] td:first-child strong').allTextContents(), ['<img src=x onerror=alert(1)>', 'Unterkunft 2', 'Unterkunft 3']);
  assert.equal(await page.locator('.suche img').count(), 0);
  assert.equal(await page.locator('a[href^="javascript:"]').count(), 0);
  await page.getByText('Supported by Rakuten Developers').waitFor();
  await page.getByText('ca. 300,00 €', { exact: true }).waitFor();
  await page.locator('[data-hit="4"] .hit-toggle').click();
  await page.getByText('neue_warnung', { exact: true }).waitFor();
  assert.equal(await page.locator('[data-group=ausgeschlossen] tbody tr[data-hit]').count(), 1);
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
  assert.equal(await page.locator('[data-group=A] tbody tr[data-hit]').count(), 3);
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
  const cached = await page.evaluate(async () => (await (await caches.open('ki-system:' + location.origin + '/:v30')).keys()).map((r) => new URL(r.url).pathname + new URL(r.url).search));
  assert(cached.includes('/icon-512.png')); assert(cached.includes('/app.js?v=0.18.2')); assert(cached.includes('/style.css?v=0.18.2'));
  assert(cached.includes('/stay-tools.js?v=0.18.2')); assert(cached.includes('/vendor/leaflet-1.9.4/leaflet.js')); assert(cached.includes('/vendor/leaflet-1.9.4/leaflet.css'));
  assert(cached.includes('/stay-research.js?v=0.18.2'));
  assert(cached.includes('/stay-form.js?v=0.18.2'));
  assert(cached.includes('/stay-details.js?v=0.18.2'));
  assert(cached.includes('/stay-districts.js?v=0.18.2'));
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
  await page.getByRole('heading', {name:'Passende Treffer – vorläufig (3)'}).waitFor();
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
  await page.goto(origin + '/#/suche/2'); await openHitDetails(page); const a = page.locator('[data-group=A]'); await a.waitFor();
  assert.deepEqual(await a.locator('tbody tr[data-hit] td:first-child strong').allTextContents(), ['Unterkunft 2','Unterkunft 1','Unterkunft 3']);
  const row = page.locator('#hit-detail-1');
  assert.match(await row.textContent(), /Datenlage: 65 %/);
  assert.equal(await row.locator('.score-bars').first().locator('.score-bar-row').count(), 5);
  assert.equal(await row.locator('.score-bars').first().getByText('unbekannt', { exact: true }).count(), 1);
  assert.equal(await row.locator('meter[value="0"]').count(), 1);
  await row.locator('.review-objection').getByText('Bettenzahl nicht belegt').waitFor();
  assert.equal(await page.locator('.suche img').count(), 0);
  await row.locator('[data-detail="1"] > summary').click(); await row.getByText('Helles Zimmer.', { exact: true }).waitFor();
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
  await page.getByRole('heading',{name:'Passende Treffer – vorläufig (3)'}).waitFor();
  malformed = true;
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await page.getByRole('status').filter({hasText:'Statusantwort unvollständig'}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchlauf_lesen').length,1);
  assert.equal(await page.locator('[data-group=A] tbody tr[data-hit]').count(),3);
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
      return fail ? 'abort' : {ok:true,id:101,treffer_id:p.daten.treffer_id,urteil:p.daten.urteil};
    }
    return r;
  });
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  let box=page.locator('[data-feedback="1"]');
  await box.getByRole('button',{name:'Passt',exact:true}).waitFor();
  assert.equal(await box.getByRole('button',{name:'Passt',exact:true}).getAttribute('aria-pressed'),'true');
  await box.locator('textarea').fill('Zu weit vom Bahnhof');
  await page.locator('[data-group=A]').getByRole('button',{name:/Preis gesamt/}).click();
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
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  assert.match(await page.locator('[data-hit="1"] [data-field="gehzeit"]').textContent(),/ca\. 7 Min\. zu Fuß · Testbahnhof \(geschätzt\)/);
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
    await page.goto(origin+'/#/suche/2'); await openHitDetails(page); await page.locator('[data-group=A]').waitFor();
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
    const buttons=page.locator('[data-group=A] thead button:visible, [data-group=A] caption button:visible, [data-feedback="1"] button:visible');
    for(const size of await buttons.evaluateAll(nodes=>nodes.map(n=>n.getBoundingClientRect().height))) assert(size>=44);
    assert.equal(await page.locator('[data-group=A] td').first().evaluate(n=>parseFloat(getComputedStyle(n).fontSize)>=14),true);
    await page.goto(origin+'/#/suche'); await page.locator('[name=ziel]').waitFor();
    await page.locator('[name=ziel]').focus(); await page.keyboard.press('Tab');
    assert.equal(await page.locator('[name=land]').evaluate(n=>document.activeElement===n),true);
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  }
  await page.setViewportSize({width:390,height:844});
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page); await page.locator('[data-feedback="1"]').waitFor();
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
  assert.equal(await a.locator('tbody tr[data-hit]').count(),10);
  await a.getByRole('button',{name:'Nächste Seite'}).click();
  assert.equal(await a.locator('tbody tr[data-hit] td:first-child strong').first().textContent(),'Unterkunft 11');
  await page.getByLabel('Sortieren nach',{exact:true}).selectOption('note_raum');
  assert.equal(await a.locator('tbody tr[data-hit] td:first-child strong').first().textContent(),'Unterkunft 105');
  await page.getByLabel('Sortieren nach',{exact:true}).selectOption('gehzeit');
  assert.equal(await a.locator('tbody tr[data-hit] td:first-child strong').first().textContent(),'Unterkunft 105');
  await page.getByLabel('Treffer filtern',{exact:true}).fill('Unterkunft 105');
  assert.equal(await a.locator('tbody tr[data-hit]').count(),1);
  await page.getByLabel('Treffer filtern',{exact:true}).fill('Kein solcher Name');
  await a.getByText('Keine Treffer für diesen Filter.').waitFor();
  await page.getByLabel('Treffer filtern',{exact:true}).fill('');
  await page.getByLabel('Treffer je Liste und Seite').selectOption('25');
  assert.equal(await a.locator('tbody tr[data-hit]').count(),25);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.evaluate(()=>scrollTo(0,0));
  await page.screenshot({path:path.join(root,'test-results/review-mobile.png')});
  await page.setViewportSize({width:768,height:1024});
  await a.locator('tbody tr[data-hit]').first().scrollIntoViewIfNeeded();
  await page.screenshot({path:path.join(root,'test-results/review-tablet.png')});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  for (const width of [600,768,1024]) {
    await page.setViewportSize({width,height:1024});
    await page.getByRole('button',{name:'Liste',exact:true}).click();
    assert.equal(await a.locator('tbody tr[data-hit]').first().evaluate(n=>getComputedStyle(n).display),'grid');
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  }
});

test('Rückmeldung aktualisiert Serverstand und erhält ungespeicherten Grund', async (t) => {
  const r = result(); r.treffer[0].rueckmeldung = {urteil:'passt',grund:'Alt'};
  const {page} = await setup(t, () => r);
  await page.goto(origin + '/#/suche/2'); await openHitDetails(page);
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
      await new Promise(resolve => {releaseWrite=resolve;}); return {ok:true,id:102,treffer_id:p.daten.treffer_id,urteil:p.daten.urteil};
    }
    return r;
  });
  await page.goto(origin + '/#/suche/2'); await openHitDetails(page);
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
  await page.goto(origin + '/#/suche/2'); await openHitDetails(page);
  const box=page.locator('[data-feedback="1"]'); await box.waitFor();
  await box.getByRole('button',{name:'Passt',exact:true}).click();
  await box.getByRole('status').filter({hasText:'HTTP 503'}).waitFor();
  assert.equal(await box.getByRole('button',{name:'Gebucht',exact:true}).isDisabled(),true);
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();await page.getByRole('status').filter({hasText:'Rangliste aktualisiert'}).waitFor();
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
  const row=page.locator('[data-group=A] tbody tr[data-hit]').first();
  await row.waitFor();
  assert.equal(await row.locator('td[data-field=preis]').textContent(),'–');
  await row.locator('.hit-toggle').click();
  const detail=page.locator('#hit-detail-1');
  assert.equal(await detail.locator('meter[value="0"]').count(),1);
  await detail.getByText('Angaben und Prüfungen',{exact:true}).click();
  await detail.getByText('Helles Fenster',{exact:true}).waitFor();
  await detail.getByText('Offene Prüfpunkte: Betten fehlen',{exact:true}).waitFor();
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
  await page.locator('[data-hit="1"]').waitFor();
  assert.equal(await page.locator('[data-hit="1"] [data-field="gehzeit"]').textContent(),'8 Min. zu Fuß · Station AZur Station Station Aberechneter Fußweg');
  assert.equal(await page.locator('[data-hit="2"] [data-field="gehzeit"]').textContent(),'ca. 9 Min. zu Fuß · Station B (geschätzt)Zur Station Station Bgeschätzt');
  assert.equal(await page.locator('[data-hit="3"] [data-field="gehzeit"]').textContent(),'10 Min. zu Fuß · Station C (Berechnung unbekannt)Zur Station Station CArt unbekannt');
});

test('Unbewertete Treffer mit vorläufigem A/B-Kennzeichen bleiben außerhalb der Ranglisten', async (t) => {
  const r=result();
  r.treffer.push(hit(6,'A',100,{topf:'unbewertet'}),hit(7,'B',110,{topf:'unbewertet'}));
  const {page}=await setup(t,()=>r);
  await page.goto(origin+'/#/suche/2');
  await page.getByRole('heading',{name:'Passende Treffer (3)',exact:true}).waitFor();
  await page.getByRole('heading',{name:'Angaben offen (1)',exact:true}).waitFor();
  await page.getByRole('heading',{name:'Weitere Treffer – noch nicht vollständig bewertet (2)',exact:true}).waitFor();
  assert.deepEqual(await page.locator('[data-group=offen] tbody tr[data-hit] td:first-child strong').allTextContents(),['Unterkunft 6','Unterkunft 7']);
  assert.match(await page.locator('[data-hit="6"] .hit-score').textContent(),/Vorläufige Passung/);
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
  await page.locator('.map-selected [data-hit="12"]').waitFor();
  assert.equal(await page.getByRole('button',{name:'Karte',exact:true}).getAttribute('aria-pressed'),'true');
  assert.equal(await page.locator('.map-selected [data-hit="12"]').isVisible(),true);
  await page.getByPlaceholder('Name oder Anbieter').fill('Unterkunft 15');
  assert.equal(await page.locator('[data-map-hit]').count(),1);
  assert.equal(await page.locator('[data-map-hit="15"]').count(),1);
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['15']);
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
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  assert.equal(await page.locator('[data-group=A]').isVisible(),true);
});

test('Favorit, Weg und Rückgängig speichern bestätigte Zustände ohne doppelten Schreibaufruf', async (t) => {
  let releaseWrite;
  const {page,calls}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_durchsehen_urteil') { if(p.daten.urteil==='favorit'&&!releaseWrite) await new Promise(resolve=>{releaseWrite=resolve;}); return {ok:true,...p.daten,...(p.aktion==='unterkunft_durchsehen_urteil'?{status:{favorit:'favorit',weg:'ausgeschlossen',vielleicht:'vielleicht',offen:'aktiv'}[p.daten.urteil]}:{})}; }
    return result();
  });
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  const selection=page.locator('[data-selection="1"]');
  await selection.getByRole('button',{name:'☆ Favorit',exact:true}).dblclick();
  await waitForCallback(()=>releaseWrite);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
  assert.equal(await selection.getByRole('button',{name:'☆ Favorit',exact:true}).isDisabled(),true);
  releaseWrite(); await selection.getByRole('button',{name:'★ Favorit',exact:true}).waitFor();
  await selection.getByRole('button',{name:'Weg',exact:true}).click();
  await page.getByRole('heading',{name:'Passende Treffer (2)'}).waitFor();
  assert.equal(await page.locator('[data-group=A] [data-hit="1"]').count(),0);
  await page.getByRole('button',{name:'Letzte Auswahl rückgängig'}).click();
  await page.locator('[data-group=A] [data-selection="1"]').getByRole('button',{name:'★ Favorit',exact:true}).waitFor();
  assert.deepEqual(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').map(p=>p.daten.urteil),['favorit','weg','favorit']);
  await page.locator('.stay-filters summary').click(); await page.getByLabel('Nur Favoriten',{exact:true}).check();
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1']);
});

test('Unklare Auswahlantwort sperrt weitere Änderungen bis zum Lesen des Serverzustands', async (t) => {
  let saved=false;
  const {page,calls}=await setup(t,p=>{
    if(p.aktion==='unterkunft_durchsehen_urteil') {saved=true;return {ok:true};}
    const data=result(); if(saved)data.treffer[0].status='favorit'; return data;
  });
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  await page.locator('[data-selection="1"]').getByRole('button',{name:'☆ Favorit',exact:true}).click();
  await page.locator('[data-selection="1"]').getByText('Bitte zuerst aktualisieren.',{exact:false}).waitFor();
  assert.equal(await page.locator('[data-selection="1"]').getByRole('button',{name:'☆ Favorit',exact:true}).isDisabled(),true);
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Favorit',exact:true}).waitFor();
  assert.equal(await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Favorit',exact:true}).isDisabled(),false);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
});

test('Verspätetes Lesen überschreibt keine inzwischen gespeicherte Auswahl; neueres Lesen wird übernommen', async (t) => {
  let reads=0, releaseRead, laterStatus='aktiv';
  const {page}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_durchsehen_urteil') return {ok:true,...p.daten,...(p.aktion==='unterkunft_durchsehen_urteil'?{status:{favorit:'favorit',weg:'ausgeschlossen',vielleicht:'vielleicht',offen:'aktiv'}[p.daten.urteil]}:{})};
    if(p.aktion==='unterkunft_suchlauf_lesen'&&++reads===2) await new Promise(resolve=>{releaseRead=resolve;});
    const data=result(); data.treffer[0].status=laterStatus;return data;
  });
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page); await page.locator('[data-selection="1"]').waitFor();
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click(); await waitForCallback(()=>releaseRead);
  await page.locator('[data-selection="1"]').getByRole('button',{name:'☆ Favorit',exact:true}).click();
  await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Favorit',exact:true}).waitFor();
  releaseRead(); await page.getByRole('button',{name:'Aktualisieren',exact:true}).waitFor({state:'visible'});
  await page.waitForFunction(()=>!Array.from(document.querySelectorAll('button')).find(b=>b.textContent==='Aktualisieren')?.disabled);
  assert.equal(await page.locator('[data-selection="1"]').getByRole('button',{name:'★ Favorit',exact:true}).count(),1);
  laterStatus='ausgeschlossen'; await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();
  await page.locator('[data-group=ausgeschlossen] > summary').click();
  await page.locator('[data-selection="1"]').getByRole('button',{name:'Wiederherstellen'}).waitFor();
  assert.equal(await page.locator('[data-group=A] [data-hit="1"]').count(),0);
  await page.locator('[data-hit="5"] .hit-toggle').click();
  assert.equal(await page.locator('[data-selection="5"]').getByRole('button',{name:'☆ Favorit',exact:true}).isDisabled(),true);
});

test('Weitere Filter: vergleichbare Noten, unbekannte Zahlen, Hotelsterne und gespeicherte Ansicht', async (t) => {
  const data=result();
  data.treffer=[hit(1,'A',200,{typ:'hotel',sterne:4,note_geeicht:9,note:4.5,note_skala:5,gehzeit_min:5,bewertungen:80}),
    hit(2,'A',100,{typ:'hotel',sterne:3,note_geeicht:8,note:8,note_skala:10,gehzeit_min:10,bewertungen:30}),
    hit(3,'B',null,{typ:'apartment',sterne:null,note:null,note_skala:null,gehzeit_min:null,bewertungen:null})];
  const {page}=await setup(t,()=>data);
  await page.addInitScript(()=>{if(!sessionStorage.getItem('ks_suche_view:2'))sessionStorage.setItem('ks_suche_view:2',JSON.stringify({filters:null}));});
  await page.goto(origin+'/#/suche/2'); await page.locator('.stay-filters summary').click();
  await page.getByLabel('Gästenote mindestens (von 10)',{exact:true}).fill('8.5');
  await page.getByLabel('Hotelsterne mindestens',{exact:true}).selectOption('4');
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1','3']);
  await page.getByLabel('Unbekannte Angaben mit anzeigen',{exact:true}).uncheck();
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1']);
  await page.reload(); await page.locator('[data-hit="1"]').waitFor();
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['1']);
  await page.locator('.stay-filters summary').click();
  assert.equal(await page.getByLabel('Gästenote mindestens (von 10)',{exact:true}).inputValue(),'8.5');
  await page.getByRole('button',{name:'Weitere Filter zurücksetzen'}).click();
  await page.getByLabel('Gesamtpreis höchstens (€)',{exact:true}).fill('150');
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['2','3']);
  await page.getByLabel('Unterkunftsform',{exact:true}).selectOption('hotel');
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['2']);
  await page.getByLabel('Gehzeit zur Station höchstens (Min.)',{exact:true}).fill('0');
  assert.equal(await page.locator('tbody tr[data-hit]').count(),0);
});

test('Lückenfüller: bestätigter Auftrag, Felder, Kopiertext und Doppelklick ohne Ausführung', async (t) => {
  let releaseCreate;
  const {page,calls}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_lueckenfueller_anlegen') { await new Promise(resolve=>{releaseCreate=resolve;}); return {ok:true,id:7,status:'erzeugt',vorgefuellter_text:'Lückenfüller Auftrag 7 ausführen'}; }
    return result();
  });
  await page.addInitScript(()=>Object.defineProperty(navigator,'clipboard',{value:{writeText:async text=>{window.copiedText=text;}}}));
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  await page.getByLabel('Für Nachrecherche auswählen: Unterkunft 4',{exact:true}).check();
  await page.getByLabel('Gesamtpreis',{exact:true}).check();
  await page.getByLabel('Hinweis für die Nachrecherche').fill('Bitte echte Betten prüfen.');
  await page.getByRole('button',{name:'Lücken füllen (1)',exact:true}).dblclick();
  await waitForCallback(()=>releaseCreate);
  const writes=calls.filter(p=>p.aktion==='unterkunft_lueckenfueller_anlegen');
  assert.equal(writes.length,1);assert.deepEqual(writes[0].daten.treffer_ids,[4]);
  assert.deepEqual(writes[0].daten.felder,['zimmerkategorien','gesamtpreis']);assert.equal(writes[0].daten.hinweis,'Bitte echte Betten prüfen.');
  assert.equal(typeof writes[0].daten.idempotenz,'string');
  releaseCreate(); await page.getByLabel('Text für den Claude-Chat').waitFor();
  assert.equal(await page.getByLabel('Text für den Claude-Chat').inputValue(),'Lückenfüller Auftrag 7 ausführen');
  await page.getByRole('button',{name:'Text kopieren',exact:true}).click();
  assert.equal(await page.evaluate(()=>window.copiedText),'Lückenfüller Auftrag 7 ausführen');
  await page.locator('[data-research-status="4"]').getByText('Recherche #7: Angelegt – wartet auf Claude',{exact:false}).waitFor();
  assert.equal(await page.getByRole('button',{name:'Lücken füllen (0)',exact:true}).isDisabled(),true);
  assert(!calls.some(p=>/ausfuehren|runde_starten|suche_starten/.test(p.aktion)));
  await page.setViewportSize({width:320,height:800});
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.locator('.research-panel').screenshot({path:path.join(root,'test-results/research-mobile.png')});
});

test('Lückenfüller: Auswahl maximal 30, über Filter hinweg erhalten und bei Ausschluss bereinigt', async (t) => {
  const data={...result(),treffer:Array.from({length:32},(_,i)=>hit(i+1,'B',100))};
  const {page}=await setup(t,p=>p.aktion==='unterkunft_durchsehen_urteil'?{ok:true,...p.daten,status:{favorit:'favorit',weg:'ausgeschlossen',offen:'aktiv'}[p.daten.urteil]}:data);
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  await page.getByLabel('Treffer je Liste und Seite',{exact:true}).selectOption('50');
  await openHitDetails(page);
  for(let i=1;i<=30;i++) await page.getByLabel('Für Nachrecherche auswählen: Unterkunft '+i,{exact:true}).check();
  assert.equal(await page.getByLabel('Für Nachrecherche auswählen: Unterkunft 31',{exact:true}).isDisabled(),true);
  await page.getByPlaceholder('Name oder Anbieter').fill('Unterkunft 32');
  await page.getByRole('button',{name:'Lücken füllen (30)',exact:true}).waitFor();
  assert.equal(await page.locator('.research-selected li').count(),30);
  await page.getByPlaceholder('Name oder Anbieter').fill('');
  await openHitDetails(page);
  await page.locator('[data-selection="1"]').getByRole('button',{name:'Weg',exact:true}).click();
  await page.getByRole('button',{name:'Lücken füllen (29)',exact:true}).waitFor();
  assert.equal(await page.getByLabel('Für Nachrecherche auswählen: Unterkunft 31',{exact:true}).isDisabled(),false);
  await page.getByLabel('Zimmer und Betten',{exact:true}).uncheck();
  assert.equal(await page.getByRole('button',{name:'Lücken füllen (29)',exact:true}).isDisabled(),true);
});

test('Lückenfüller: unklare Antwort wird lesend wiedergefunden, Status und Kopieren ohne Zwischenablage', async (t) => {
  let created=false, jobStatus='erzeugt';
  const {page,calls}=await setup(t,p=>{
    if(p.aktion==='unterkunft_lueckenfueller_anlegen') {created=true;return {ok:true,id:7};}
    if(p.aktion==='unterkunft_lueckenfueller_lesen') return {ok:true,auftraege:created?[{id:7,suchauftrag_id:2,treffer_ids:[4],felder:['zimmerkategorien'],status:jobStatus}]:[]};
    return result();
  });
  await page.addInitScript(()=>Object.defineProperty(navigator,'clipboard',{value:{writeText:async()=>{throw new Error('Test: verweigert');}}}));
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page); await page.getByLabel('Für Nachrecherche auswählen: Unterkunft 4',{exact:true}).check();
  await page.getByRole('button',{name:'Lücken füllen (1)',exact:true}).click();
  await page.getByText('Anlegen nicht bestätigt:',{exact:false}).waitFor();
  assert.equal(await page.getByRole('button',{name:'Lücken füllen (1)',exact:true}).isDisabled(),true);
  await page.getByRole('button',{name:'Recherche-Status aktualisieren',exact:true}).click();
  await page.getByLabel('Text für den Claude-Chat').waitFor();
  await page.getByRole('button',{name:'Text kopieren',exact:true}).click();
  await page.getByText('Bitte den markierten Text von Hand kopieren.').waitFor();
  assert.equal(await page.getByLabel('Text für den Claude-Chat').evaluate(n=>n.selectionEnd-n.selectionStart),'Lückenfüller Auftrag 7 ausführen'.length);
  for(const [state,label] of [['in_arbeit','In Arbeit'],['teilweise','Teilweise ergänzt'],['nicht_moeglich','Nicht möglich'],['erledigt','Erledigt']]) {
    jobStatus=state; await page.getByRole('button',{name:'Recherche-Status aktualisieren',exact:true}).click();
    await page.locator('[data-research-status="4"]').getByText('Recherche #7: '+label,{exact:false}).waitFor();
  }
  assert.equal(await page.getByLabel('Text für den Claude-Chat').isVisible(),false);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_lueckenfueller_anlegen').length,1);
});

test('Lückenfüller: vorhandenen Auftrag öffnen, Lesefehler erhalten Treffer, Bereichswechsel beendet Antwort', async (t) => {
  let readError=false, releaseCreate;
  const {page}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_lueckenfueller_lesen') return readError?'abort':{ok:true,auftraege:[{id:8,suchauftrag_id:2,treffer_ids:[4],felder:['zimmerkategorien'],status:'in_arbeit'}]};
    if(p.aktion==='unterkunft_lueckenfueller_anlegen') { await new Promise(resolve=>{releaseCreate=resolve;}); return {ok:true,id:8,status:'in_arbeit',schon_vorhanden:true,vorgefuellter_text:'Lückenfüller Auftrag 8 ausführen'}; }
    if(p.aktion==='auftraege_suchen')return [];
    return result();
  });
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page); await page.getByRole('button',{name:'Text für Auftrag #8',exact:true}).click();
  assert.equal(await page.getByLabel('Text für den Claude-Chat').inputValue(),'Lückenfüller Auftrag 8 ausführen');
  readError=true; await page.getByRole('button',{name:'Recherche-Status aktualisieren',exact:true}).click();
  await page.getByText('Recherche-Status nicht geladen:',{exact:false}).waitFor();
  assert.equal(await page.locator('[data-group=B] [data-hit="4"]').count(),1);
  await page.getByLabel('Für Nachrecherche auswählen: Unterkunft 4',{exact:true}).check();
  await page.getByRole('button',{name:'Lücken füllen (1)',exact:true}).click(); await waitForCallback(()=>releaseCreate);
  await page.locator('#areas [data-area=council]').click(); await page.getByRole('heading',{name:'Aufträge',exact:true}).waitFor();
  releaseCreate(); assert.equal(await page.locator('.research-panel').count(),0);
});

test('Reisewünsche: Nebenart, Mischung, Unterkunft, Qualitätsfilter und Pflichtkriterien anlegen', async (t) => {
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_suchauftrag_anlegen'?{ok:true,id:2}:p.aktion==='unterkunft_suche_starten'?{ok:true}:p.daten?.suchauftrag_id?result():{suchauftraege:[]});
  await page.goto(origin+'/#/suche');await formFill(page);
  await page.getByLabel('Nebenart',{exact:true}).selectOption('erholung');
  await page.getByLabel('Mischung der Reisearten',{exact:true}).selectOption('frei');
  await page.getByLabel('Anteil der Nebenart (%)',{exact:true}).fill('40');
  await page.getByLabel('Gewünschte Unterkunftsform',{exact:true}).selectOption('apartment');
  await page.getByLabel('Suite als Wunsch',{exact:true}).check();
  await page.getByLabel('Qualitätsfilter anwenden',{exact:true}).uncheck();
  await page.locator('.trip-criteria > summary').click();
  await page.getByLabel('Bedeutung: Echte Betten für alle',{exact:true}).selectOption('pflicht');
  await page.getByLabel('Bedeutung: Schlafzimmer mindestens',{exact:true}).selectOption('pflicht');
  await page.getByLabel('Bedeutung: Wohnfläche mindestens (m²)',{exact:true}).selectOption('pflicht');
  await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).click();
  await page.getByText('Bitte einen gültigen Wert für „Wohnfläche mindestens (m²)“ eintragen.').waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchauftrag_anlegen').length,0);
  await page.getByLabel('Wert: Wohnfläche mindestens (m²)',{exact:true}).fill('55');
  await page.getByLabel('Bedeutung: Balkon',{exact:true}).selectOption('egal');
  await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).click();
  await page.locator('[data-group=A]').waitFor();
  const d=calls.find(p=>p.aktion==='unterkunft_suchauftrag_anlegen').daten;
  assert.equal(d.profil,'staedte');assert.equal(d.nebenart,'erholung');assert.equal(d.nebenart_anteil,40);assert.equal(d.unterkunftsform,'apartment');
  assert.equal(d.suite,true);assert.equal(d.qualitaetsfilter,false);
  assert.deepEqual(d.kriterien.echte_betten,{modus:'pflicht'});assert.deepEqual(d.kriterien.flaeche_m2,{modus:'pflicht',wert:55});
  assert.deepEqual(d.kriterien.schlafzimmer,{modus:'pflicht',wert:2});assert.deepEqual(d.kriterien.suite,{modus:'wunsch'});assert.deepEqual(d.kriterien.balkon,{modus:'egal'});
});

test('Suchprofil übernehmen bewahrt Reiseziel und Daten; geleerte Felder kehren nicht aus Profil zurück', async (t) => {
  const profile={id:9,name:'Familie',felder:{erwachsene:3,kinder_alter:[9],budget_eur:9000,land:'JP',schlafzimmer_min:3,nebenart:'natur',nebenart_anteil:50,unterkunftsform:'haus',qualitaetsfilter:false,kriterien:{balkon:{modus:'egal'}},quellen:['hasdata_booking','apify_airbnb']}};
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_suchprofile_lesen'?profileCatalog([profile]):p.aktion==='unterkunft_suchauftrag_anlegen'?{ok:true,id:2}:p.aktion==='unterkunft_suche_starten'?{ok:true}:p.daten?.suchauftrag_id?result():{suchauftraege:[]});
  await page.goto(origin+'/#/suche');await formFill(page);
  await page.getByLabel('Suchprofil verwenden',{exact:true}).selectOption('9');
  assert.equal(await page.locator('[name=ziel]').inputValue(),'Kyoto');assert.equal(await page.locator('[name=anreise]').inputValue(),'2026-11-13');
  assert.equal(await page.locator('[name=erwachsene]').inputValue(),'3');assert.equal(await page.locator('[name=kinder_alter]').inputValue(),'9');
  await page.locator('[name=budget_eur]').fill('');await page.locator('[name=land]').fill('');
  await page.getByLabel('Nebenart',{exact:true}).selectOption('');
  await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).click();await page.locator('[data-group=A]').waitFor();
  const d=calls.find(p=>p.aktion==='unterkunft_suchauftrag_anlegen').daten;
  assert.equal(d.suchprofil,undefined);assert.equal(d.budget_eur,undefined);assert.equal(d.land,undefined);assert.equal(d.nebenart,undefined);
  assert.deepEqual(d.quellen,['hasdata_booking','apify_airbnb']);assert.deepEqual(d.kriterien.balkon,{modus:'egal'});
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchprofil_speichern').length,0);
});

test('Suchprofil ohne Ziel und Reisedaten speichern, Doppelklick und bewusster Ersatz', async (t) => {
  let releaseSave;
  const {page,calls}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_suchprofil_speichern'){await new Promise(resolve=>{releaseSave=resolve;});return{ok:true,id:9,name:p.daten.name,felder:p.daten.felder};}
    return {suchauftraege:[]};
  });
  await page.goto(origin+'/#/suche');
  await page.getByLabel('Name des Suchprofils',{exact:true}).fill('Familie');
  await page.getByRole('button',{name:'Als Profil speichern',exact:true}).dblclick();await waitForCallback(()=>releaseSave);
  assert.equal(await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).isDisabled(),true);
  const writes=calls.filter(p=>p.aktion==='unterkunft_suchprofil_speichern');assert.equal(writes.length,1);
  assert.equal(writes[0].daten.felder.ziel,undefined);assert.equal(writes[0].daten.felder.anreise,undefined);assert.equal(writes[0].daten.felder.abreise,undefined);
  assert.equal(writes[0].daten.felder.erwachsene,2);
  releaseSave();await page.getByText('Profil „Familie“ gespeichert.',{exact:true}).waitFor();
  await page.getByRole('button',{name:'Gleichnamiges Profil ersetzen',exact:true}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchauftrag_anlegen').length,0);
});

test('Suchprofil: unklare Speicherantwort verlangt Lesen, Entwurf bleibt erhalten', async (t) => {
  let saved;
  const {page,calls}=await setup(t,p=>{
    if(p.aktion==='unterkunft_suchprofile_lesen')return profileCatalog(saved?[saved]:[]);
    if(p.aktion==='unterkunft_suchprofil_speichern'){saved={id:9,...p.daten};return{ok:true,id:9};}
    return{suchauftraege:[]};
  });
  await page.goto(origin+'/#/suche');await page.getByLabel('Name des Suchprofils',{exact:true}).fill('Familie');
  await page.getByRole('button',{name:'Als Profil speichern',exact:true}).click();
  await page.getByText('Speichern nicht bestätigt:',{exact:false}).waitFor();
  assert.equal(await page.getByRole('button',{name:'Als Profil speichern',exact:true}).isDisabled(),true);
  await page.locator('[name=ziel]').fill('Kanazawa');await page.locator('[name=erwachsene]').fill('4');
  await page.getByRole('button',{name:'Suchprofile aktualisieren',exact:true}).click();
  await page.getByText('1 Suchprofile verfügbar.',{exact:true}).waitFor();
  assert.equal(await page.locator('[name=erwachsene]').inputValue(),'4');assert.equal(await page.locator('[name=ziel]').inputValue(),'Kanazawa');
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchprofil_speichern').length,1);
});

test('Formular-Katalogfehler blockiert Start bis zum erneuten Laden; mobile Filter ohne Überlauf', async (t) => {
  let working=false;
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_suchprofile_lesen'?(working?profileCatalog():{ok:true}):{suchauftraege:[]},{width:320,height:800});
  await page.goto(origin+'/#/suche');await formFill(page);
  await page.getByText('Suchprofile nicht geladen:',{exact:false}).waitFor();
  assert.equal(await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).isDisabled(),true);
  working=true;await page.getByRole('button',{name:'Suchprofile aktualisieren',exact:true}).click();
  await page.getByText('Noch keine Suchprofile gespeichert.').waitFor();
  assert.equal(await page.locator('[name=ziel]').inputValue(),'Kyoto');
  assert.equal(await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).isDisabled(),false);
  assert.equal(await page.getByLabel('Reiseart',{exact:true}).locator('option:disabled').count(),5);
  await page.locator('.trip-criteria > summary').click();
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  fs.mkdirSync(path.join(root,'test-results'),{recursive:true});
  await page.locator('.trip-criteria').screenshot({path:path.join(root,'test-results/trip-filters-mobile.png')});
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchauftrag_anlegen').length,0);
});

test('Vorläufige Treffer auf Klick, Deckungswarnung und laufendes Polling bis zum Endstand', async (t) => {
  let finished=false;
  const partial={vollstaendig:false,fehlend:[{quelle:'trivago_mcp',status:'offen'}],hinweis:'Eine Quelle fehlt noch.'};
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_suche_status'?{...status(finished?'fertig':'laeuft'),deckung:finished?{vollstaendig:true,fehlend:[]}:partial}:{...result(finished?'fertig':'laeuft'),deckung:finished?{vollstaendig:true,fehlend:[]}:partial});
  await page.clock.install();await page.goto(origin+'/#/suche/2');
  await page.getByText('Keine vollständige Marktsuche.',{exact:true}).waitFor();
  await page.getByText('Die Suche läuft auch ohne geöffnetes Handy weiter.',{exact:false}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchlauf_lesen').length,0);
  await page.getByRole('button',{name:'Vorläufige Treffer ansehen',exact:true}).click();
  await page.getByRole('heading',{name:'Passende Treffer – vorläufig (3)',exact:true}).waitFor();
  await page.getByText('Offen oder fehlend: Trivago',{exact:true}).waitFor();
  assert.equal(await page.getByRole('button',{name:/Passung/}).count(),0);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchlauf_lesen').length,1);
  await page.getByText('Vorläufige Treffer. Die Bewertung läuft weiter;', {exact:false}).waitFor();
  const nextPoll=page.waitForRequest(r=>r.postDataJSON()?.aktion==='unterkunft_suche_status');
  await page.clock.fastForward(7100);await nextPoll;
  await page.getByText('Suche läuft. Bewertung und Gegenprüfung werden abgewartet.',{exact:false}).waitFor();
  assert(calls.filter(p=>p.aktion==='unterkunft_suche_status').length>=2);
  finished=true;await page.clock.fastForward(7100);
  await page.getByRole('heading',{name:'Passende Treffer (3)',exact:true}).waitFor();
  await page.getByText('Alle vorgesehenen Quellen sind abgeschlossen.',{exact:true}).waitFor();
  assert.equal(await page.getByRole('button',{name:'Vorläufige Treffer ansehen',exact:true}).isVisible(),false);
});

test('Ergebnisnachweise: Preisalter, Verfügbarkeit, Balkon, Warncodes und Mindestzahl ohne Filterverwechslung', async (t) => {
  let data=result();data.deckung={vollstaendig:false,fehlend:['rakuten_travel']};
  data.treffer[0]={...data.treffer[0],preis_veraltet:true,kategorien:[{name:'Doppelzimmer',balkon:'ja'}],angebot:{preis_gesamt_eur:200,verfuegbar:'belegt',abrufzeit:'2026-10-12T12:30:00Z'}};
  data.treffer[1].angebot.verfuegbar='unbelegt';data.treffer[1].kategorien=[{balkon:'nein'},{balkon:'unklar'}];
  data.treffer[2].bewertung.warnungen=['unbewertet_chance','pflicht_unbekannt','ueber_budget'];
  const {page}=await setup(t,()=>data);await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  await page.getByText('Datenlage reicht noch nicht für 10 Empfehlungen unter den passenden Treffern (derzeit 3).',{exact:true}).waitFor();
  const first=page.locator('#hit-detail-1');
  await first.getByText('Preis veraltet – älter als 48 Stunden',{exact:true}).waitFor();
  await first.getByText('Verfügbarkeit belegt beim Abruf',{exact:true}).waitFor();
  await first.getByText('Balkon: ja',{exact:true}).waitFor();
  await page.locator('#hit-detail-2').getByText('Verfügbarkeit unbelegt',{exact:true}).waitFor();
  await page.locator('#hit-detail-2').getByText('Balkon: unbekannt',{exact:true}).waitFor();
  await page.getByText('Wenige Bewertungen – bekommt eine Chance',{exact:true}).waitFor();await page.getByText('Pflichtangabe noch ungeklärt',{exact:true}).waitFor();
  data={...result(),deckung:{vollstaendig:true,fehlend:[]},treffer:Array.from({length:12},(_,i)=>hit(i+1,'A',100))};
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();await page.getByRole('heading',{name:'Passende Treffer (12)',exact:true}).waitFor();
  await page.getByPlaceholder('Name oder Anbieter').fill('Unterkunft 12');
  assert.equal(await page.getByText('Datenlage reicht noch nicht für 10',{exact:false}).count(),0);
});

test('Kandidatendetails trennen Angebote und Noten, zeigen Gewichte/Nachweise und schließen mit Fokus', async (t) => {
  const data=result();const t1=data.treffer[0];
  t1.note=9.1;t1.note_skala=10;t1.angebot={preis_gesamt_eur:200,quelle:'hasdata_booking',verfuegbar:'belegt',abrufzeit:'2026-10-16T10:00:00Z',link:'https://example.com/primary'};
  t1.bewertung.spaltennoten={raum:8,lage:9,gewichte:{raum:25,lage:30,preis_leistung:20,bewertungen:15,eignung:10}};
  t1.bewertung.gegenpruefung={pruefung:{urteil:'einwand',einwaende:['Bettenzahl prüfen'],hinweis:'Raumaufteilung offen'}};
  t1.kategorien=[{name:'Familienzimmer',m2:42,schlafzimmer:2,betten_anzahl:4,max_personen:4,balkon:'nein',quelle:'hasdata_booking',abrufzeit:'2026-10-15T12:00:00Z'}];
  t1.weitere_angebote=[{anbieter:'Zweite Quelle',quelle:'trivago_mcp',preis_gesamt_eur:150,note:4.5,note_skala:5,bewertungen:60,link:'https://example.com/other'},{anbieter:'Ohne Nachweis',link:'javascript:alert(1)'}];
  const {page}=await setup(t,()=>data,{width:390,height:844});await page.goto(origin+'/#/suche/2'); await openHitDetails(page);
  const open=page.locator('#hit-detail-1').getByRole('button',{name:'Unterkunft im Detail',exact:true});await open.click();
  const dialog=page.getByRole('dialog',{name:'Unterkunft im Detail: Unterkunft 1',exact:true});await dialog.waitFor();
  assert(!await dialog.evaluate(n=>Array.from(n.childNodes).some(c=>c.nodeType===3 && c.textContent==='null')));
  assert.match(await dialog.textContent(), /Passung: 81\/100/);
  assert.equal(await dialog.locator('a').count(),2);
  const ratings=dialog.getByRole('region',{name:'Gästenoten nach Quelle',exact:true});
  assert.deepEqual(await ratings.locator('tbody tr').allTextContents(),['Booking9.11035','Zweite Quelle4.5560','Ohne Nachweisunbekanntunbekanntunbekannt']);
  await dialog.getByRole('region',{name:'Teilnoten und Gewichtung',exact:true}).getByRole('cell',{name:'25',exact:true}).waitFor();
  await dialog.getByText('Bettenzahl prüfen',{exact:true}).waitFor();
  await dialog.getByRole('cell',{name:'Familienzimmer',exact:true}).waitFor();
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await dialog.screenshot({path:path.join(root,'test-results/candidate-mobile.png')});
  await page.keyboard.press('Escape');assert.equal(await page.getByRole('dialog').count(),0);
  assert.equal(await open.evaluate(n=>document.activeElement===n),true);
  await open.click();await page.evaluate(()=>{location.hash='#/ergebnisse';});
  await page.getByRole('heading',{name:'Suchen & Ergebnisse',exact:true}).waitFor();assert.equal(await page.getByRole('dialog').count(),0);
});

test('Schnell-Gründe sind ein Entwurf und werden erst mit dem Urteil gespeichert', async (t) => {
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_rueckmeldung_geben'?{ok:true,id:103,treffer_id:p.daten.treffer_id,urteil:p.daten.urteil}:result());
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);const box=page.locator('[data-feedback="1"]');
  await box.getByLabel('Optionaler Grund für Unterkunft 1',{exact:true}).fill('Persönliche Notiz');
  await box.getByLabel('Schnell-Grund für Unterkunft 1',{exact:true}).selectOption('Lage');
  await box.getByLabel('Schnell-Grund für Unterkunft 1',{exact:true}).selectOption('Betten');
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_rueckmeldung_geben').length,0);
  await box.getByLabel('Schnell-Grund für Unterkunft 1',{exact:true}).selectOption('Sonstiges');
  assert.equal(await box.getByLabel('Optionaler Grund für Unterkunft 1',{exact:true}).evaluate(n=>n===document.activeElement),true);
  await box.getByRole('button',{name:'Passt nicht',exact:true}).click();await box.getByText('Gespeichert:',{exact:false}).waitFor();
  assert.equal(calls.find(p=>p.aktion==='unterkunft_rueckmeldung_geben').daten.grund,'Persönliche Notiz; Lage; Betten');
});

test('Verlauf öffnet Merkliste je Reise und gespeichertes Profil ohne Schreibaufruf', async (t) => {
  const data=result();data.treffer[1].status='favorit';
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_suchprofile_lesen'?profileCatalog([{id:7,name:'Familienprofil',felder:{erwachsene:4,kinder_alter:[10],kriterien:{balkon:{modus:'egal'}}}}]):p.daten?.suchauftrag_id?data:{merkliste:[],suchauftraege:[{id:2,ziel:'Tokyo',status:'fertig',treffer:5,gemerkt:1}]});
  await page.goto(origin+'/#/ergebnisse');
  await page.getByText('Rohdaten werden nach 30 Tagen entfernt.',{exact:false}).waitFor();
  await page.getByRole('link',{name:'Favoriten in Tokyo',exact:true}).click();await page.locator('[data-hit="2"]').waitFor();
  assert.deepEqual(await page.locator('tbody tr[data-hit]').evaluateAll(rows=>rows.map(r=>r.dataset.hit)),['2']);
  assert.equal(await page.getByLabel('Nur Favoriten',{exact:true}).isChecked(),true);
  await page.goto(origin+'/#/ergebnisse');await page.getByRole('link',{name:'Neue Suche mit Profil „Familienprofil“',exact:true}).click();
  await page.getByText('Profil „Familienprofil“ übernommen.',{exact:false}).waitFor();
  assert.equal(await page.locator('[name=erwachsene]').inputValue(),'4');assert.equal(await page.locator('[name=ziel]').inputValue(),'');
  assert(!calls.some(p=>/anlegen|speichern|status_setzen/.test(p.aktion)));
});

test('Sprunglinks öffnen Unbewertete und nach Gründen gegliederte Ausschlüsse', async (t) => {
  const data=result();data.treffer.push(hit(6,'A',100,{topf:'unbewertet'}),hit(7,'A',100,{topf:'ausgeschlossen',ko_grund:'Budget überschritten'}),hit(8,'B',100,{status:'ausgeschlossen'}));
  const {page}=await setup(t,()=>data);await page.goto(origin+'/#/suche/2');
  await page.getByRole('button',{name:'Ausgeschlossene (3) nach Grund',exact:true}).click();
  const section=page.locator('[data-group=ausgeschlossen]');assert.equal(await section.evaluate(n=>n.open),true);
  assert.deepEqual(await section.locator('h3.exclusion-reason').allTextContents(),['Grund nicht geliefert','Budget überschritten','Von dir ausgeschlossen']);
  await page.getByRole('button',{name:'Unbewertete (1)',exact:true}).click();
  assert.equal(await page.evaluate(()=>document.activeElement.parentElement.dataset.group),'offen');
});

test('Nachrecherche: verspäteter Status lässt Texteingabe, Cursor und offene Angaben stehen', async (t) => {
  let releaseStatus;
  const {page,calls}=await setup(t,async p=>p.aktion==='unterkunft_lueckenfueller_lesen'
    ? await new Promise(resolve=>{releaseStatus=()=>resolve({ok:true,auftraege:[]});}) : result(),{width:390,height:844});
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page); await waitForCallback(()=>releaseStatus);
  const info=page.locator('[data-detail="1"]'); await info.locator('summary').click();
  await page.getByLabel('Für Nachrecherche auswählen: Unterkunft 4',{exact:true}).check();
  const reason=page.getByLabel('Optionaler Grund für Unterkunft 1',{exact:true});
  await reason.fill('Ruhig und zentral');
  await reason.evaluate(n=>{n.focus();n.setSelectionRange(6,9);});
  const original=await reason.elementHandle(); const scroll=await page.evaluate(()=>scrollY);
  releaseStatus(); await page.getByText('Recherche-Status aktualisiert.',{exact:true}).waitFor();
  assert.equal(await original.evaluate(n=>n.isConnected),true,'Eine reine Statusantwort darf das Eingabefeld nicht ersetzen');
  assert.deepEqual(await reason.evaluate(n=>({focused:document.activeElement===n,start:n.selectionStart,end:n.selectionEnd})),{focused:true,start:6,end:9});
  assert.equal(await info.evaluate(n=>n.open),true);
  assert.equal(await page.getByLabel('Für Nachrecherche auswählen: Unterkunft 4',{exact:true}).isChecked(),true);
  assert(Math.abs((await page.evaluate(()=>scrollY))-scroll)<2,'Die Leseposition bleibt stehen');
  await page.keyboard.insertText('sowie'); assert.equal(await reason.inputValue(),'Ruhig sowie zentral');
  assert.equal(calls.filter(p=>p.aktion && !['unterkunft_suche_status','unterkunft_suchlauf_lesen','unterkunft_lueckenfueller_lesen'].includes(p.aktion)).length,0);
});

test('Nachrecherche: verspäteter Status erhält den Rücksprung aus der Detailansicht', async (t) => {
  let releaseStatus;
  const {page}=await setup(t,async p=>p.aktion==='unterkunft_lueckenfueller_lesen'
    ? await new Promise(resolve=>{releaseStatus=()=>resolve({ok:true,auftraege:[{id:91,suchauftrag_id:2,treffer_ids:[4],felder:['balkon'],status:'erzeugt'}]});}) : result());
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page); await waitForCallback(()=>releaseStatus);
  const open=page.locator('#hit-detail-4 .candidate-open'); await open.click();
  releaseStatus(); await page.getByText('Recherche-Status aktualisiert.',{exact:true}).waitFor({state:'attached'});
  await page.getByRole('dialog').waitFor(); await page.keyboard.press('Escape');
  assert.equal(await open.evaluate(n=>document.activeElement===n),true,'Schließen führt zum ursprünglichen Treffer zurück');
  await page.locator('[data-research-status="4"]').getByText('Recherche #91: Angelegt – wartet auf Claude',{exact:false}).waitFor();
});

test('Viertel: freier Einstieg, unbekannte Noten, lokale Filter und Sortierung', async (t) => {
  const {page,calls}=await setup(t,()=>districts());
  await page.goto(origin+'/#/viertel');await page.getByRole('heading',{name:'Welches Viertel passt zu euch?'}).waitFor();
  assert.equal(calls.length,0);assert.equal(await page.locator('#tabs [data-view=viertel]').getAttribute('aria-current'),'page');
  assert(!await page.locator('.districts-page').evaluate(n=>Array.from(n.childNodes).some(c=>c.nodeType===3 && c.textContent==='null')));
  await page.getByLabel('Stadt oder Insel',{exact:true}).fill('Kyoto');await page.getByRole('button',{name:'Viertel laden',exact:true}).click();
  await page.locator('[data-district="21"]').waitFor();assert.deepEqual(calls[0].daten,{stadt:'Kyoto'});
  const unknown=page.locator('[data-district="21"] .score-bar-row').filter({hasText:'Grün'});
  assert.equal(await unknown.getByRole('meter').count(),0);await unknown.getByText('unbekannt',{exact:true}).waitFor();
  const zero=page.locator('[data-district="22"] .score-bar-row').filter({hasText:'Grün'});
  assert.equal(await zero.getByRole('meter').getAttribute('value'),'0');
  assert.equal(await page.locator('a[href^="javascript:"]').count(),0);
  await page.getByLabel('Ruhig',{exact:true}).check();assert.equal(await page.locator('.district-cards [data-district]').count(),1);
  await page.getByLabel('Ruhig',{exact:true}).uncheck();await page.getByLabel('Grün ≥ 5',{exact:true}).check();
  assert.deepEqual(await page.locator('.district-cards [data-district]').evaluateAll(ns=>ns.map(n=>n.dataset.district)),['23']);
  await page.getByRole('button',{name:'Viertelfilter zurücksetzen',exact:true}).click();await page.getByLabel('Viertel sortieren nach',{exact:true}).selectOption('gruen');
  assert.deepEqual(await page.locator('.district-cards [data-district]').evaluateAll(ns=>ns.map(n=>n.dataset.district)),['23','22','21']);
  assert.equal(calls.length,1,'Lokales Filtern und Sortieren erzeugt keine API-Schreibvorgänge');
  await page.goto(origin+'/#/viertel/?suche=2');await page.getByLabel('Viertel sortieren nach',{exact:true}).selectOption('preis');
  await page.locator('[data-district="21"]').waitFor();
  assert.deepEqual(await page.locator('.district-cards [data-district]').evaluateAll(ns=>ns.map(n=>n.dataset.district)),['22','21','23']);
});

test('Viertelkarte: erst auf Klick, Kreise mit Status, Tastatur, fehlende Positionen und Handy', async (t) => {
  let tiles=0;
  const {page}=await setup(t,()=>districts(),{width:390,height:844});
  await page.route('https://tile.openstreetmap.org/**',r=>{tiles++;return r.abort();});
  await page.goto(origin+'/#/viertel/?suche=2');await page.locator('[data-district="21"]').waitFor();assert.equal(tiles,0);
  await page.getByRole('button',{name:'Viertelkarte anzeigen',exact:true}).click();
  const proposal=page.locator('[data-district-circle="21"]');await proposal.waitFor();
  assert.equal(await proposal.getAttribute('stroke-dasharray'),'7 6');assert.equal(await proposal.getAttribute('stroke'),'#2c6846');
  assert.equal(await page.locator('[data-district-circle="22"]').getAttribute('stroke-dasharray'),null);
  assert.equal(await page.locator('[data-district-circle]').count(),2);await page.getByText('2 von 3 Vierteln auf der Karte.',{exact:false}).waitFor();
  await proposal.focus();await page.keyboard.press('Enter');assert.equal(await page.evaluate(()=>document.activeElement.textContent),'Parkviertel');
  await page.getByText('Der Kartenhintergrund ist nicht erreichbar.',{exact:false}).waitFor();assert(tiles>0);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.locator('.stay-map-panel').screenshot({path:path.join(root,'test-results/district-map-mobile.png')});
  await page.locator('[data-district="21"]').screenshot({path:path.join(root,'test-results/district-card-mobile.png')});
  await page.setViewportSize({width:320,height:800});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.setViewportSize({width:1440,height:1000});await page.evaluate(()=>scrollTo(0,0));await page.screenshot({path:path.join(root,'test-results/district-desktop.png')});
});

test('Viertelentscheidungen: bestätigen, bewusst streichen, wieder aufnehmen und Name/Notiz prüfen', async (t) => {
  const data=districts();let releaseWrite;
  const {page,calls}=await setup(t,async p=>{
    if(p.aktion==='unterkunft_zone_entscheiden')return await new Promise(resolve=>{releaseWrite=()=>{
      const z=[...data.viertel,...data.gestrichen].find(z=>z.id===p.daten.id);Object.assign(z,{status:p.daten.status},p.daten.name?{name:p.daten.name}:{} ,p.daten.notiz?{notiz_nutzer:p.daten.notiz}:{});
      data.viertel=[...data.viertel,...data.gestrichen].filter(z=>z.status!=='gestrichen');data.gestrichen=z.status==='gestrichen'?[z]:[];
      resolve({ok:true,id:z.id,status:z.status});
    };});return data;
  });
  await page.goto(origin+'/#/viertel/?stadt=kyoto');const card=page.locator('[data-district="21"]');await card.waitFor();
  await card.getByRole('button',{name:'Bestätigen',exact:true}).dblclick();await waitForCallback(()=>releaseWrite);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_zone_entscheiden').length,1);releaseWrite();await page.getByText('Gespeichert: Parkviertel · bestätigt.',{exact:true}).waitFor();
  await card.getByRole('button',{name:'Streichen',exact:true}).click();assert.equal(calls.filter(p=>p.aktion==='unterkunft_zone_entscheiden').length,1);
  await card.getByRole('button',{name:'Abbrechen',exact:true}).click();assert.equal(await card.getByRole('button',{name:'Streichen',exact:true}).evaluate(n=>document.activeElement===n),true);
  await card.getByRole('button',{name:'Streichen',exact:true}).click();releaseWrite=null;await card.getByRole('button',{name:'Ja, Viertel streichen',exact:true}).click();await waitForCallback(()=>releaseWrite);releaseWrite();
  await page.getByText('Gespeichert: Parkviertel · gestrichen.',{exact:true}).waitFor();assert.equal(await page.locator('.district-removed').evaluate(n=>n.open),true);
  releaseWrite=null;await card.getByRole('button',{name:'Als Vorschlag wieder aufnehmen',exact:true}).click();await waitForCallback(()=>releaseWrite);releaseWrite();await page.getByText('Gespeichert: Parkviertel · Vorschlag.',{exact:true}).waitFor();
  await card.getByText('Umbenennen / Notiz',{exact:true}).click();await card.getByLabel('Neuer Name für Parkviertel',{exact:true}).fill('Am Park');await card.getByLabel('Notiz zu Parkviertel',{exact:true}).fill('Für die Familie vormerken');
  releaseWrite=null;await card.getByRole('button',{name:'Name und Notiz speichern',exact:true}).click();await waitForCallback(()=>releaseWrite);releaseWrite();await page.getByText('Gespeichert: Am Park · Vorschlag.',{exact:true}).waitFor();
  assert.equal(await card.getByLabel('Notiz zu Am Park',{exact:true}).inputValue(),'Für die Familie vormerken');
});

test('Viertel: unklare Schreibantwort sperrt Wiederholung bis zum Lesen', async (t) => {
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_zone_entscheiden'?{ok:true}:districts());
  await page.goto(origin+'/#/viertel/?stadt=kyoto');await page.locator('[data-district="21"]').getByRole('button',{name:'Bestätigen',exact:true}).click();
  await page.getByText('Speichern nicht bestätigt:',{exact:false}).waitFor();assert.equal(await page.locator('[data-district="21"]').getByRole('button',{name:'Bestätigen',exact:true}).isDisabled(),true);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_zone_entscheiden').length,1);
  await page.getByRole('button',{name:'Viertel aktualisieren',exact:true}).click();await page.getByText('Viertel aktualisiert.',{exact:true}).waitFor();
  assert.equal(await page.locator('[data-district="21"]').getByRole('button',{name:'Bestätigen',exact:true}).isDisabled(),false);
});

test('Viertel ermitteln: Kostenhinweis, ein Klick, alten Lauf nicht als neuen Erfolg ausgeben', async (t) => {
  let phase='old';const data=districts();data.viertel=[];
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_viertel_erstellen'?{ok:true,stadt:'kyoto',hinweis:'Ermittlung angestoßen.'}:{...data,letzter_lauf:phase==='old'?{id:1,status:'fertig'}:{id:2,status:phase}});
  await page.clock.install();await page.goto(origin+'/#/viertel/?stadt=kyoto');await page.getByText('Für diesen Ort sind noch keine Viertel vorhanden.',{exact:true}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_viertel_erstellen').length,0);
  await page.getByRole('button',{name:'Viertel ermitteln · ca. 0,06 USD',exact:true}).dblclick();await page.getByText('Ermittlung angefragt. Der Fortschritt wird automatisch gelesen;', {exact:false}).waitFor();
  const next=page.waitForRequest(r=>r.postDataJSON()?.aktion==='unterkunft_viertel_lesen');await page.clock.fastForward(3100);await next;
  await page.getByText('Ermittlung angefragt.',{exact:false}).waitFor();assert.equal(await page.getByRole('button',{name:'Viertel ermitteln · ca. 0,06 USD',exact:true}).isDisabled(),true);
  phase='osm_angefordert';await page.clock.fastForward(10100);await page.getByText('Letzte Ermittlung: Umgebungsdaten werden geladen',{exact:false}).waitFor();
  phase='fertig';await page.clock.fastForward(10100);await page.getByText('Viertel aktualisiert.',{exact:true}).waitFor();
  assert.equal(await page.getByRole('button',{name:'Viertel ermitteln · ca. 0,06 USD',exact:true}).isDisabled(),false);
  assert.deepEqual(calls.filter(p=>p.aktion==='unterkunft_viertel_erstellen').map(p=>p.daten),[{stadt:'kyoto'}]);
  const count=calls.length;await page.clock.fastForward(30100);assert.equal(calls.length,count);
});

test('Viertelauswahl übergibt Pflicht/Wunsch an eine neue Suche, Filter verlieren keine Auswahl', async (t) => {
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_viertel_lesen'?districts():p.aktion==='unterkunft_suchprofile_lesen'?districtCatalog():p.aktion==='unterkunft_suchauftrag_anlegen'?{ok:true,id:2}:p.aktion==='unterkunft_suche_starten'?{ok:true}:p.daten?.suchauftrag_id?result():{suchauftraege:[]});
  await page.goto(origin+'/#/viertel/?stadt=kyoto');await page.getByLabel('Viertel auswählen: Altstadt',{exact:true}).check();await page.getByLabel('Ruhig',{exact:true}).check();
  await page.getByLabel('Viertel auswählen: Parkviertel',{exact:true}).check();await page.getByLabel('Gewählte Viertel berücksichtigen',{exact:true}).selectOption('wunsch');
  await page.getByRole('button',{name:'Mit diesen Vierteln suchen',exact:true}).click();await page.getByLabel('Suchviertel: Altstadt',{exact:true}).waitFor();
  assert.equal(await page.locator('[name=ziel]').inputValue(),'kyoto');assert.equal(await page.getByLabel('Suchviertel: Altstadt',{exact:true}).isChecked(),true);
  await page.locator('[name=anreise]').fill('2026-11-13');await page.locator('[name=abreise]').fill('2026-11-27');
  await page.getByLabel('Bedeutung: ÖPNV im Viertel mindestens',{exact:true}).selectOption('pflicht');await page.getByLabel('Wert: ÖPNV im Viertel mindestens',{exact:true}).fill('5');
  await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).click();await page.locator('[data-group=A]').waitFor();
  const write=calls.find(p=>p.aktion==='unterkunft_suchauftrag_anlegen');assert.deepEqual(write.daten.kriterien.viertel_auswahl,{modus:'wunsch',werte:[21,22]});assert.deepEqual(write.daten.kriterien.viertel_oepnv_min,{modus:'pflicht',wert:5});
});

test('Viertel im Formular: Profil-IDs für Ziel prüfen, falsche Stadt und veraltete Antworten nicht übernehmen', async (t) => {
  let releaseKyoto;const profile={id:7,name:'Viertelprofil',felder:{kriterien:{viertel_auswahl:{modus:'pflicht',werte:[21,99]}}}};
  const {page,calls}=await setup(t,async p=>p.aktion==='unterkunft_suchprofile_lesen'?districtCatalog([profile]):p.aktion==='unterkunft_viertel_lesen'?await new Promise(resolve=>{releaseKyoto=()=>resolve(districts());}):{suchauftraege:[]});
  await page.goto(origin+'/#/suche');await formFill(page);await page.getByLabel('Suchprofil verwenden',{exact:true}).selectOption('7');
  await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).click();await page.getByText('Bitte die gewählten Viertel zuerst für den aktuellen Zielort laden und prüfen.',{exact:true}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchauftrag_anlegen').length,0);
  await page.getByRole('button',{name:'Viertel für Zielort laden',exact:true}).click();await waitForCallback(()=>releaseKyoto);releaseKyoto();await page.getByText('1 gespeicherte Viertel passen nicht mehr',{exact:false}).waitFor();
  assert.equal(await page.getByLabel('Suchviertel: Parkviertel',{exact:true}).isChecked(),true);
  releaseKyoto=null;await page.getByRole('button',{name:'Viertel für Zielort laden',exact:true}).click();await waitForCallback(()=>releaseKyoto);
  await page.locator('[name=ziel]').fill('Osaka');releaseKyoto();await page.getByRole('button',{name:'Viertel für Zielort laden',exact:true}).waitFor();
  assert.equal(await page.getByLabel('Bedeutung der Viertelauswahl',{exact:true}).inputValue(),'egal');assert.equal(await page.getByLabel('Suchviertel: Parkviertel',{exact:true}).count(),0);
});

test('Viertel-Lesefehler, Navigation und 401 lassen keine falsche Ansicht oder Polling zurück', async (t) => {
  let mode='ok',release;const data=districts();data.letzter_lauf.status='ki';
  const {page,calls}=await setup(t,async p=>p.aktion==='unterkunft_viertel_lesen'?mode==='wait'?await new Promise(resolve=>{release=()=>resolve(data);}):mode==='ok'?data:mode:p.aktion==='auftraege_suchen'?[]:result());
  await page.clock.install();await page.goto(origin+'/#/viertel/?stadt=kyoto');await page.locator('[data-district="21"]').waitFor();
  mode='abort';await page.getByRole('button',{name:'Viertel aktualisieren',exact:true}).click();await page.getByText('Viertel nicht geladen:',{exact:false}).waitFor();assert.equal(await page.locator('[data-district="21"]').count(),1);
  const total=calls.length;await page.clock.fastForward(30100);assert.equal(calls.length,total);
  mode='wait';await page.getByRole('button',{name:'Viertel aktualisieren',exact:true}).click();await waitForCallback(()=>release);await page.locator('#areas [data-area=council]').click();release();await page.getByRole('heading',{name:'Aufträge',exact:true}).waitFor();
  await page.clock.fastForward(30100);assert.equal(await page.locator('.districts-page').count(),0);
  mode='unauthorized';await page.goto(origin+'/#/viertel/?stadt=kyoto');await page.getByRole('heading',{name:'Anmelden',exact:true}).waitFor();
});

test('Viertellink aus Treffer und Detail öffnet das zugehörige Viertel', async (t) => {
  const data=result();data.treffer[0].zone={id:21,name:'Parkviertel',status:'vorschlag'};
  const {page}=await setup(t,p=>p.aktion==='unterkunft_viertel_lesen'?districts():data);
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);await page.locator('#hit-detail-1 .candidate-open').click();
  await page.getByRole('dialog').getByRole('link',{name:'Viertel: Parkviertel',exact:true}).click();await page.locator('[data-district="21"]').waitFor();
  assert.equal(await page.evaluate(()=>document.activeElement.textContent),'Parkviertel');assert.equal(await page.getByRole('dialog').count(),0);
  await page.getByRole('link',{name:'Zurück zu den Unterkünften',exact:true}).click();await openHitDetails(page);await page.locator('#hit-detail-1').getByRole('link',{name:'Viertel: Parkviertel',exact:true}).click();await page.locator('[data-district="21"]').waitFor();
});

test('Aktualisieren liest laufende Treffer neu und entsperrt eine unklare Auswahl lesend', async (t) => {
  const data=result('laeuft');
  const {page,calls}=await setup(t,p=>{
    if(p.aktion==='unterkunft_durchsehen_urteil'){data.treffer[0].status='favorit';return {ok:true};}return data;
  });
  await page.goto(origin+'/#/suche/2'); await page.getByRole('button',{name:'Vorläufige Treffer ansehen',exact:true}).click();await openHitDetails(page);
  const selection=page.locator('[data-selection="1"]');await selection.getByRole('button',{name:'☆ Favorit',exact:true}).click();
  await selection.getByText('Speichern nicht bestätigt:',{exact:false}).waitFor();assert.equal(await selection.getByRole('button',{name:'☆ Favorit',exact:true}).isDisabled(),true);
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();await selection.getByRole('button',{name:'★ Favorit',exact:true}).waitFor();
  assert.equal(await selection.getByRole('button',{name:'★ Favorit',exact:true}).isDisabled(),false);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);assert.equal(calls.filter(p=>p.aktion==='unterkunft_suchlauf_lesen').length,2);
  await page.getByRole('heading',{name:'Passende Treffer – vorläufig (3)',exact:true}).waitFor();
});

test('Rückmeldung verlangt passenden Treffer und Urteil; unklare Antwort lässt keine Wiederholung zu', async (t) => {
  let response={};
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_rueckmeldung_geben'?response:result());
  await page.goto(origin+'/#/suche/2'); await openHitDetails(page);const feedback=page.locator('[data-feedback="1"]');
  for(const value of [{},{ok:true},{ok:true,id:11,treffer_id:2,urteil:'passt'},{ok:true,id:12,treffer_id:1,urteil:'gebucht'}]) {
    response=value;await feedback.getByRole('button',{name:'Passt',exact:true}).click();await feedback.getByText('Speichern nicht bestätigt:',{exact:false}).waitFor();
    assert.equal(await feedback.getByRole('button',{name:'Passt',exact:true}).isDisabled(),true);assert.equal(await feedback.locator('[aria-pressed=true]').count(),0);
    await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();await page.getByRole('status').filter({hasText:'Rangliste aktualisiert'}).waitFor();
  }
  response={ok:true,id:13,treffer_id:1,urteil:'passt'};await feedback.getByRole('button',{name:'Passt',exact:true}).click();await feedback.getByText('Gespeichert: Passt.',{exact:false}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_rueckmeldung_geben').length,5);
});

test('Merkliste per Link verändert keine gespeicherten Normalfilter', async (t) => {
  const data=result();data.treffer[1].status='favorit';
  const {page}=await setup(t,()=>data);await page.goto(origin+'/#/suche/2');await page.getByPlaceholder('Name oder Anbieter').fill('Unterkunft');
  const before=await page.evaluate(()=>sessionStorage.getItem('ks_suche_view:2'));
  await page.goto(origin+'/#/suche/2?favoriten=1');await page.locator('[data-hit="2"]').waitFor();
  assert.equal(await page.getByLabel('Nur Favoriten',{exact:true}).isChecked(),true);assert.equal(await page.evaluate(()=>sessionStorage.getItem('ks_suche_view:2')),before);
  await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();assert.equal(await page.getByLabel('Nur Favoriten',{exact:true}).isChecked(),false);
  assert.equal(await page.getByPlaceholder('Name oder Anbieter').inputValue(),'Unterkunft');
});

test('Angebotslinks erlauben nur HTTPS ohne eingebettete Zugangsdaten', async (t) => {
  const data=result();data.treffer[0].angebot.link='https://name:passwort@example.com/angebot';data.treffer[1].angebot.link='http://example.com/angebot';
  const {page}=await setup(t,()=>data);await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();
  assert.equal(await page.locator('[data-hit="1"] a').count(),0);assert.equal(await page.locator('[data-hit="2"] a').count(),0);
  await page.locator('[data-hit="3"] .hit-toggle').click();
  assert.equal(await page.locator('#hit-detail-3 a[href="https://example.com/angebot"]').count()>0,true);
});

test('Viertel: neue Leseantwort erhält Notizentwurf und Cursor während laufender Ermittlung', async (t) => {
  let release,hold=false;const data=districts();data.letzter_lauf.status='osm_angefordert';
  const {page}=await setup(t,async()=>{if(hold)await new Promise(resolve=>{release=resolve;});return data;});
  await page.clock.install();await page.goto(origin+'/#/viertel/?stadt=kyoto');const card=page.locator('[data-district="21"]');await card.getByText('Umbenennen / Notiz',{exact:true}).click();
  const note=card.getByLabel('Notiz zu Parkviertel',{exact:true});await note.fill('Diesen Ort vergleichen');await note.evaluate(n=>n.setSelectionRange(7,10));
  hold=true;await page.clock.fastForward(10100);await waitForCallback(()=>release);assert.equal(await note.isDisabled(),false);release();await page.getByText('Viertel aktualisiert.',{exact:true}).waitFor();
  assert.deepEqual(await note.evaluate(n=>({value:n.value,focused:document.activeElement===n,start:n.selectionStart,end:n.selectionEnd})),{value:'Diesen Ort vergleichen',focused:true,start:7,end:10});
});

test('Schlafzimmer: Standard und altes Profil bleiben Wunsch, ausdrückliches Egal entfernt die Vorgabe', async (t) => {
  const profiles=[{id:1,name:'Bisheriges Profil',felder:{schlafzimmer_min:3}},{id:2,name:'Ohne Raumvorgabe',felder:{schlafzimmer_min:2,kriterien:{schlafzimmer:{modus:'egal'}}}}];
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_suchprofile_lesen'?profileCatalog(profiles):p.aktion==='unterkunft_suchauftrag_anlegen'?{ok:true,id:2}:p.aktion==='unterkunft_suche_starten'?{ok:true}:p.daten?.suchauftrag_id?result():{suchauftraege:[],merkliste:[]});
  for(const [profile,mode,bedrooms] of [['','wunsch',2],['1','wunsch',3],['2','egal',0]]) {
    await page.goto(origin+'/#/suche');await formFill(page);if(profile)await page.getByLabel('Suchprofil verwenden',{exact:true}).selectOption(profile);
    assert.equal(await page.getByLabel('Bedeutung: Schlafzimmer mindestens',{exact:true}).inputValue(),mode);
    assert.equal(await page.locator('[name=schlafzimmer_min]').isDisabled(),mode==='egal');
    if(mode==='egal'){await page.locator('.trip-criteria > summary').click();await page.getByText('Egal: keine Schlafzimmer-Vorgabe, auch Einzimmer-Angebote.',{exact:true}).waitFor();}
    await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).click();await page.locator('[data-group=A]').waitFor();
    const data=calls.filter(p=>p.aktion==='unterkunft_suchauftrag_anlegen').at(-1).daten;
    assert.equal(data.schlafzimmer_min,bedrooms);assert.deepEqual(data.kriterien.schlafzimmer,mode==='egal'?{modus:'egal'}:{modus:'wunsch',wert:bedrooms});
  }
});

test('Profil-Rundlauf bewahrt Balkon Egal und die gemeinsame Schlafzimmerzahl', async (t) => {
  let profile;
  const {page,calls}=await setup(t,p=>{
    if(p.aktion==='unterkunft_suchprofile_lesen')return profileCatalog(profile?[profile]:[]);
    if(p.aktion==='unterkunft_suchprofil_speichern'){profile={id:8,name:p.daten.name,felder:p.daten.felder};return {ok:true,...profile};}
    if(p.aktion==='unterkunft_suchauftrag_anlegen')return {ok:true,id:2};if(p.aktion==='unterkunft_suche_starten')return {ok:true};return p.daten?.suchauftrag_id?result():{suchauftraege:[],merkliste:[]};
  });
  await page.goto(origin+'/#/suche');await page.locator('.trip-criteria > summary').click();await page.getByLabel('Bedeutung: Balkon',{exact:true}).selectOption('egal');await page.locator('[name=schlafzimmer_min]').fill('3');
  await page.getByLabel('Name des Suchprofils',{exact:true}).fill('Familie ohne Balkonwunsch');await page.getByRole('button',{name:'Als Profil speichern',exact:true}).click();await page.getByText('Profil „Familie ohne Balkonwunsch“ gespeichert.',{exact:true}).waitFor();
  await page.reload();await formFill(page);await page.getByLabel('Suchprofil verwenden',{exact:true}).selectOption('8');
  assert.equal(await page.getByLabel('Bedeutung: Balkon',{exact:true}).inputValue(),'egal');assert.equal(await page.locator('[name=schlafzimmer_min]').inputValue(),'3');
  await page.getByRole('button',{name:'Anlegen und Suche starten',exact:true}).click();await page.locator('[data-group=A]').waitFor();
  const data=calls.find(p=>p.aktion==='unterkunft_suchauftrag_anlegen').daten;assert.deepEqual(data.kriterien.balkon,{modus:'egal'});assert.deepEqual(data.kriterien.schlafzimmer,{modus:'wunsch',wert:3});assert.equal(data.schlafzimmer_min,3);
});

test('Gemeinsame Merkliste enthält ältere Reisen, öffnet den richtigen Treffer und übersteht Lesefehler', async (t) => {
  let fail=false;
  const saved=Array.from({length:12},(_,i)=>({treffer_id:i+1,suchauftrag_id:1,ziel:'Frühere Reise',anreise:'2026-03-01',abreise:'2026-03-05',name:'Gemerkt '+(i+1),quelle:'hasdata_booking',preis_gesamt_eur:400,liste:'A',rang:i+1,link:'https://example.com/angebot'}));
  saved.push({treffer_id:20,suchauftrag_id:2,ziel:'Aktuelle Reise',name:'Weiterer Favorit',topf:'ausgeschlossen',link:'https://name:pass@example.com'});
  const {page,calls}=await setup(t,p=>{
    if(p.aktion==='unterkunft_suchprofile_lesen')return profileCatalog();
    if(p.daten?.suchauftrag_id){const r=result();r.suchauftrag.id=p.daten.suchauftrag_id;r.treffer=Array.from({length:12},(_,i)=>hit(i+1,'A',400,{status:'favorit'}));return r;}
    return fail?'abort':{ok:true,suchauftraege:[{id:2,ziel:'Aktuelle Reise',gemerkt:1},{id:3,ziel:'Ohne Favoriten',gemerkt:0}],merkliste:saved};
  });
  await page.goto(origin+'/#/ergebnisse');await page.locator('[data-saved-trip="1"]').waitFor();
  assert.equal(await page.locator('.saved-stay').count(),13);assert.equal(await page.getByRole('link',{name:'Favoriten in Ohne Favoriten',exact:true}).count(),0);
  assert.equal(await page.getByRole('link',{name:'Favoriten in Aktuelle Reise',exact:true}).count(),1);
  assert.equal(calls.filter(p=>p.daten?.suchauftrag_id).length,0,'Eine Listenabfrage genügt auch für alte Reisen');
  await page.locator('[data-saved-hit="20"]').getByText('Fachlich ausgeschlossen',{exact:false}).waitFor();assert.equal(await page.locator('[data-saved-hit="20"] a[href^="https:"]').count(),0);
  fs.mkdirSync(path.join(root,'test-results'),{recursive:true});await page.screenshot({path:path.join(root,'test-results','favorites-desktop.png'),fullPage:true});
  fail=true;await page.getByRole('button',{name:'Merkliste aktualisieren',exact:true}).click();await page.getByText('Merkliste nicht aktualisiert:',{exact:false}).waitFor();assert.equal(await page.locator('.saved-stay').count(),13);
  await page.setViewportSize({width:320,height:800});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.locator('[data-saved-hit="12"]').getByRole('link',{name:'Im Suchlauf zeigen',exact:true}).click();await page.locator('[data-hit="12"]').waitFor();
  assert.equal(await page.evaluate(()=>document.activeElement.dataset.hit),'12');assert.equal(await page.locator('[data-group=A] .result-pages').textContent().then(t=>t.includes('Seite 2 / 2')),true);
});


test('Ergebnisansichten: kompakte Tabelle, Liste, Karte, gemeinsame Filter und sichere Details', async t => {
  const data=result();
  data.treffer=[hit(1,'A',200,{lat:35,lon:135,bild:'https://example.com/photo.jpg',note:9,note_skala:10,gehzeit_min:3,station_name:'Bahnhof',angebot:{preis_gesamt_eur:200,kategorie_name:'Familienzimmer',link:'https://example.com/angebot'},kategorien:[{name:'Familienzimmer',schlafzimmer:2,betten_anzahl:3,betten_art:'Doppelbett, Einzelbett'}]}),hit(2,'B',100,{lat:35.01,lon:135.01,angebot:{preis_gesamt_eur:100,kategorie_name:'Anderes Zimmer'},kategorien:[{name:'Suite',schlafzimmer:4,betten_text:'Kingsize'}]}),hit(3,'A',null)];
  const {page,calls}=await setup(t,()=>data,{width:1920,height:1080});
  await page.route('https://example.com/photo.jpg',r=>r.fulfill({contentType:'image/svg+xml',body:'<svg xmlns="http://www.w3.org/2000/svg" width="50" height="40"><rect width="50" height="40" fill="green"/></svg>'}));
  await page.route('https://*.tile.openstreetmap.org/**',r=>r.abort());
  await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();
  assert.equal(await page.getByRole('button',{name:'Tabelle',exact:true}).getAttribute('aria-pressed'),'true');
  assert.equal(await page.locator('.hit-detail-row:visible').count(),0);
  const metrics=await page.locator('[data-hit="1"]').evaluate(row=>({height:row.getBoundingClientRect().height,photo:row.querySelector('figure').getBoundingClientRect().toJSON(),width:row.closest('.suche-results').getBoundingClientRect().width}));
  assert(metrics.height<160,JSON.stringify(metrics));assert(metrics.width>1550);assert.equal(metrics.photo.width,50);assert.equal(metrics.photo.height,40);
  assert.equal(await page.locator('[data-hit="2"] [data-label="Schlafzimmer"]').textContent(),'–');
  await page.locator('.stay-filters > summary').click();
  await page.getByLabel('Schlafzimmer mindestens',{exact:true}).fill('2');await page.getByLabel('Unbekannte Angaben mit anzeigen',{exact:true}).uncheck();
  assert.deepEqual(await page.locator('[data-hit]').evaluateAll(ns=>ns.map(n=>n.dataset.hit)),['1']);
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  assert.equal(await page.locator('[data-hit="1"]').evaluate(n=>getComputedStyle(n).display),'grid');
  await page.getByRole('button',{name:'Karte',exact:true}).click();await page.locator('.stay-pin').first().waitFor();
  assert.equal(await page.locator('.stay-pin').count(),1);
  await page.getByRole('button',{name:'Tabelle',exact:true}).click();
  await page.locator('[data-hit="1"] .hit-toggle').click();await page.locator('#hit-detail-1').waitFor();
  await page.locator('[data-feedback="1"] textarea').fill('Entwurf bleibt');
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  assert.equal(await page.locator('[data-feedback="1"] textarea').inputValue(),'Entwurf bleibt');
  assert.equal(await page.locator('[data-hit="1"] .hit-toggle').getAttribute('aria-expanded'),'true');
  await page.locator('[data-hit="1"] .hit-toggle').click();assert.equal(await page.locator('#hit-detail-1').isVisible(),false);
  await page.reload();await page.locator('[data-hit="1"]').waitFor();
  assert.equal(await page.getByRole('button',{name:'Liste',exact:true}).getAttribute('aria-pressed'),'true');
  assert.equal(calls.filter(p=>p.aktion && !/lesen|status/.test(p.aktion)).length,0);
});

test('Ergebnisansichten: iPhone-Breiten, große Schrift und bedienbare Tabelle', async t => {
  const {page}=await setup(t,()=>result(),{width:390,height:844});
  await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();
  for(const width of [320,375,390,430]) {
    await page.setViewportSize({width,height:844});
    await page.getByRole('button',{name:'Liste',exact:true}).click();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    assert((await page.locator('[data-hit="1"]').boundingBox()).height<620);
    await page.getByRole('button',{name:'Tabelle',exact:true}).click();
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    assert.equal(await page.locator('[data-hit="1"]').evaluate(n=>getComputedStyle(n).display),'table-row');
    const scroller=page.locator('.suche-table-scroll').first();
    assert(await scroller.evaluate(n=>n.scrollWidth>n.clientWidth));
    await scroller.evaluate(n=>n.scrollLeft=n.scrollWidth);
    await page.locator('[data-hit="1"] .hit-toggle').click();await page.locator('#hit-detail-1').waitFor();
    await page.locator('[data-hit="1"] .hit-toggle').click();
  }
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  await page.addStyleTag({content:'.compact-results td,.compact-results strong,.compact-results .small{font-size:24px !important}'});
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
});

test('Kyoto: echte gelesene Daten auf Desktop und iPhone darstellen', {skip:process.env.KYOTO_READONLY_TEST!=='1'}, async t => {
  const data=JSON.parse(fs.readFileSync(path.join(root,'../live-data.json'),'utf8'));
  const {page,calls}=await setup(t,()=>data,{width:1920,height:1080});
  await page.route('https://*.tile.openstreetmap.org/**',r=>r.abort());
  await page.goto(origin+'/#/suche/5');await page.locator('[data-hit]').first().waitFor();
  const counts={};for(const row of data.treffer){const group=row.topf==='ausgeschlossen'||row.status==='ausgeschlossen'?'ausgeschlossen':row.topf==='unbewertet'?'offen':['A','B'].includes(row.bewertung?.liste)?row.bewertung.liste:'offen';counts[group]=(counts[group]||0)+1;}
  for(const [group,count] of Object.entries(counts)) assert((await page.locator('[data-group='+group+']').first().textContent()).includes('('+count+')'));
  const output=path.join(root,'../../outputs');fs.mkdirSync(output,{recursive:true});
  await page.locator('[data-group=A]').evaluate(n=>window.scrollTo(0,n.getBoundingClientRect().top+scrollY-145));
  await page.screenshot({path:path.join(output,'Ergebnisse-Desktop.png')});
  await page.getByRole('button',{name:'Liste',exact:true}).click();await page.setViewportSize({width:390,height:844});
  await page.locator('[data-group=A]').evaluate(n=>window.scrollTo(0,n.getBoundingClientRect().top+scrollY-145));
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.screenshot({path:path.join(output,'Ergebnisse-iPhone.png')});
  await page.getByRole('button',{name:'Karte',exact:true}).click();await page.locator('.stay-pin').first().waitFor();
  const expected=data.treffer.filter(t=>t.topf!=='ausgeschlossen'&&t.status!=='ausgeschlossen'&&typeof t.lat==='number'&&typeof t.lon==='number'&&Math.abs(t.lat)<=85.05112878&&Math.abs(t.lon)<=180).length;
  assert.equal(await page.locator('.stay-pin:not(.pin-ziel)').count(),expected);
  assert.equal(calls.filter(p=>p.aktion && !/lesen|status/.test(p.aktion)).length,0);
  console.log('Kyoto unverändert:',JSON.stringify(counts),'Marker:',expected);
});

test('Neue Spalten: echte Angebotszuordnung, Nullwerte, Gäste-Skalen, Sortierung und Filter', async t => {
  const {page}=await setup(t,()=>result());await page.goto(origin+'/#/suche/2');await page.locator('[data-hit]').first().waitFor();
  const checks=await page.evaluate(()=>{
    const a={name:'A',angebot:{kategorie_name:'Suite',anbieter:'Alpha'},kategorien:[{name:'Suite',schlafzimmer:0,betten_art:'Einzelbett'}],bewertung:{warnungen:['offen']},note_geeicht:9,note:4.5,note_skala:5};
    const b={name:'B',angebot:{kategorie_name:'Suite',anbieter:'Beta'},kategorien:[{name:'Suite',schlafzimmer:2,betten_text:'Kingsize'}],bewertung:{warnungen:[]},note_geeicht:8,note:8,note_skala:10};
    const unknown={angebot:{kategorie_name:'Zimmer'},kategorien:[{name:'Andere Kategorie',schlafzimmer:9,betten_text:'Kingsize'}]};
    const whole={quelle:'apify_airbnb',angebot:{kategorie_name:'ganze Unterkunft'},kategorien:[{quelle:'apify_airbnb',name:'2 Schlafzimmer',schlafzimmer:2},{quelle:'manuell',name:'Weitere Notiz',schlafzimmer:3}]};
    return {whole:sucheZimmerKurz(whole).schlafzimmer,zero:sucheZimmerKurz(a).schlafzimmer,conflict:sucheZimmerKurz({...b,kategorien:[{...b.kategorien[0],konflikt:true}]}).schlafzimmer,
      unknown:sucheZimmerKurz(unknown),sorts:['schlafzimmer','betten','anbieter','gaestenote','warnungen'].map(key=>[key,sucheVergleich(a,b,key,1),sucheVergleich(a,b,key,-1)]),
      nullLast:[1,-1].map(direction=>sucheVergleich(unknown,b,'schlafzimmer',direction)>0),
      filters:[sucheFilterTreffer(b,{betten:'king',schlafzimmer:'2',warnungen:'ohne'}),sucheFilterTreffer(a,{warnungen:'ohne'}),sucheFilterTreffer(unknown,{schlafzimmer:'2',unbekannt:false})]};
  });
  assert.equal(checks.whole,2);assert.equal(checks.zero,0);assert.equal(checks.conflict,null);assert.equal(checks.unknown.schlafzimmer,null);assert.equal(checks.unknown.typen,null);
  assert.deepEqual(checks.nullLast,[true,true]);assert.deepEqual(checks.filters,[true,false,false]);
  for(const [key,asc,desc] of checks.sorts){assert(asc!==0,key);assert.equal(asc,-desc,key);}
  assert(checks.sorts.find(r=>r[0]==='gaestenote')[1]>0);
});

test('Zimmervertrag: Angebots-ID vor gleichen Namen, echte Bettentypen und verständliche Details', async t => {
  const data=result();
  const categories=[{id:685,name:'Two-Bedroom Family Apartment',quelle:'hasdata_booking',m2:47.1,schlafzimmer:2,betten_anzahl:7,max_personen:7,balkon:false,betten_text:'2 twin beds, 2 sofa beds, 3 futon beds',ergaenzt_aus:{m2:'booking_plugin'}},
    {id:809,name:'Two-Bedroom Family Apartment',quelle:'booking_plugin',m2:47.1,schlafzimmer:9},
    {id:810,name:'Quadruple Room',quelle:'hasdata_booking',m2:30.9},
    {id:811,name:'Quadruple Room',quelle:'booking_plugin'}];
  data.treffer=[hit(1,'A',200,{angebot:{preis_gesamt_eur:200,kategorie_id:685,kategorie_name:'Two-Bedroom Family Apartment'},kategorien:categories})];
  const {page}=await setup(t,()=>data,{width:390,height:844});
  await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();
  assert.equal(await page.locator('[data-hit="1"] [data-label="Schlafzimmer"]').textContent(),'2');
  // Betten are optional; select them via the actual display settings.
  await page.goto(origin+'/#/anzeige');await page.getByLabel('Storno',{exact:true}).uncheck();await page.getByLabel('Betten/Schlafplätze',{exact:true}).check();await page.goto(origin+'/#/suche/2');
  assert((await page.locator('[data-hit="1"] [data-field="betten"]').textContent()).includes('2 Einzelbett'));
  await page.locator('.stay-filters > summary').click();await page.getByLabel('Bettentyp enthält',{exact:true}).fill('twin');
  assert.equal(await page.locator('[data-hit]').count(),1);
  await page.locator('[data-hit="1"] .hit-toggle').click();
  await page.locator('#hit-detail-1').getByText('Angaben und Prüfungen',{exact:true}).click();
  const detail=page.locator('#hit-detail-1');
  await detail.getByText('Two-Bedroom Family Apartment · 47,1 m² · 2 Schlafzimmer · 7 Betten · bis 7 Personen · Balkon: nein',{exact:true}).waitFor();
  await detail.getByText('Fläche ergänzt aus Booking (Lückenfüller)',{exact:true}).waitFor();
  assert.equal(await detail.getByText('Quadruple Room · 30,9 m²',{exact:true}).isVisible(),false);
  await detail.getByText('Weitere Zimmer im Haus (1)',{exact:true}).click();
  await detail.getByText('Quadruple Room · 30,9 m²',{exact:true}).waitFor();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  const checks=await page.evaluate(categories=>{
    const make=a=>({angebot:a,kategorien:categories});
    return [sucheZimmerKurz(make({kategorie_id:999,kategorie_name:categories[0].name})).schlafzimmer,
      sucheZimmerKurz(make({kategorie_name:categories[0].name})).schlafzimmer,
      sucheZimmerKurz({angebot:{kategorie_name:'  suite  '},kategorien:[{name:'Suite',betten_art:'Doppelbett',betten_text:'raw',schlafzimmer:1}]}).typen];
  },categories);
  assert.deepEqual(checks,[null,null,'Doppelbett']);
});

// Wunsch 71: These tests exercise the production UI with synthetic server responses only.
function reviewData() {
  const d=result();d.suchauftrag.runde=1;
  d.treffer=[hit(1,'A',700,{status:'aktiv',runde:1,note:4.7,note_skala:5,note_geeicht:9,quelle:'apify_airbnb'}),hit(2,'A',800,{status:'aktiv',runde:2}),hit(3,'B',900,{status:'favorit',eigener_rang:2}),hit(4,'A',1000,{status:'favorit',eigener_rang:1}),hit(5,'A',500,{status:'vielleicht',urteil_uebernommen:{urteil:'vielleicht'}})];return d;
}
function reviewHandler(d) {return p=>{
  if(p.aktion==='unterkunft_durchsehen_urteil') {const t=d.treffer.find(t=>t.treffer_id===p.daten.treffer_id);t.status={favorit:'favorit',weg:'ausgeschlossen',vielleicht:'vielleicht',offen:'aktiv'}[p.daten.urteil];t.urteil_gruende=p.daten.gruende;return {ok:true,...p.daten,status:t.status};}
  if(p.aktion==='unterkunft_eigenes_ranking_setzen')return {ok:true};return d;
};}
test('W71: Anzeige max 6, Reihenfolge, Reset, Persistenz und fehlende Werte',async t=>{
  const {page}=await setup(t,()=>reviewData());await page.goto(origin+'/#/anzeige');
  assert.equal(await page.locator('input:checked').count(),6);assert.equal(await page.getByLabel('Preis/Nacht',{exact:true}).isDisabled(),true);
  await page.getByLabel('Storno',{exact:true}).uncheck();await page.getByLabel('Preis/Nacht',{exact:true}).check();
  await page.getByRole('button',{name:'Preis/Nacht nach oben',exact:true}).click();
  await page.reload();assert.equal(await page.getByLabel('Preis/Nacht',{exact:true}).isChecked(),true);
  await page.getByRole('button',{name:'Standard wiederherstellen'}).click();
  await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();
  assert.equal(await page.locator('[data-hit="1"] td[data-field=m2]').textContent(),'–');
  assert.match(await page.locator('[data-hit="1"] td[data-field=gaestenote]').textContent(),/9 \/ 10/);
  for(const label of ['Liste','Tabelle','Tinder']){await page.getByRole('button',{name:label,exact:true}).click();assert.equal(await page.locator('[aria-label=Suchergebnisse]').getAttribute('data-result-view'),{Liste:'list',Tabelle:'table',Tinder:'tinder'}[label]);}
  await page.reload();await page.locator('[data-review-hit]').waitFor();assert.equal(await page.getByRole('button',{name:'Tinder',exact:true}).getAttribute('aria-pressed'),'true');
});
test('W71: Knöpfe, Gründe, Rückgängig, neue zuerst, übernommene nie erneut',async t=>{
  const d=reviewData(),{page,calls}=await setup(t,reviewHandler(d));await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  assert.equal(await page.locator('[data-review-hit]').getAttribute('data-review-hit'),'2');
  await page.getByRole('button',{name:'Weg',exact:true}).click();await page.locator('[data-review-hit="1"]').waitFor();
  await page.getByRole('button',{name:'Gründe ergänzen',exact:true}).click();await page.locator('.review-reasons').getByRole('button',{name:'Preis',exact:true}).click();await page.getByRole('button',{name:'Gründe speichern',exact:true}).click();
  await page.getByRole('button',{name:'Letzte Entscheidung rückgängig'}).click();await page.locator('[data-review-hit="2"]').waitFor();
  await page.getByRole('button',{name:'Na ja',exact:true}).click();await page.locator('[data-review-hit="1"]').waitFor();
  await page.getByRole('button',{name:'Favorit',exact:true}).click();await page.getByText('Alle Unterkünfte durchgesehen.',{exact:true}).waitFor();
  const writes=calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil');assert.deepEqual(writes.map(p=>p.daten.urteil),['weg','weg','offen','vielleicht','favorit']);assert.deepEqual(writes[1].daten.gruende,['preis']);assert(!writes.some(p=>p.daten.treffer_id===5));
});
test('W71: Wischen rechts, links, hoch; Galerie begrenzt auf 10 und getrennt',async t=>{
  const d=reviewData();d.treffer[1].bilder=Array.from({length:12},(_,i)=>'https://example.com/photo-'+i+'.jpg');
  const {page,calls}=await setup(t,reviewHandler(d));await page.route('https://example.com/**',r=>r.fulfill({contentType:'image/svg+xml',body:'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="200"/>'}));
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  await page.getByText('1 / 10',{exact:true}).waitFor();await page.getByRole('button',{name:'Nächstes Foto'}).click();await page.getByText('2 / 10',{exact:true}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,0);
  for(const [dx,dy,verdict] of [[100,0,'favorit'],[-100,0,'weg'],[0,-100,'vielleicht']]){
    const area=page.locator('.review-swipe');await area.dispatchEvent('pointerdown',{pointerId:1,button:0,clientX:200,clientY:200});await area.dispatchEvent('pointerup',{pointerId:1,button:0,clientX:200+dx,clientY:200+dy});
    await page.locator('[data-review-hit="1"]').waitFor();assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').at(-1).daten.urteil,verdict);
    await page.getByRole('button',{name:'Letzte Entscheidung rückgängig'}).click();await page.locator('[data-review-hit="2"]').waitFor();
  }
});
test('W71: Endrunde Ziehen und Paarvergleich speichern nur Favoriten',async t=>{
  const d=reviewData(),{page,calls}=await setup(t,reviewHandler(d));await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Endrunde',exact:true}).click();
  await page.locator('[data-final-hit="3"]').dragTo(page.locator('[data-final-hit="4"]'),{sourcePosition:{x:10,y:10},targetPosition:{x:10,y:10}});
  assert.deepEqual(await page.locator('[data-final-hit]').evaluateAll(ns=>ns.map(n=>Number(n.dataset.finalHit))),[3,4]);
  await page.getByRole('button',{name:'Rangfolge speichern',exact:true}).click();await page.locator('.endrunde').waitFor({state:'detached'});
  assert.deepEqual(calls.find(p=>p.aktion==='unterkunft_eigenes_ranking_setzen').daten.reihenfolge,[3,4]);
  await page.getByRole('button',{name:'Endrunde',exact:true}).click();await page.getByRole('button',{name:'Paarvergleich starten'}).click();
  await page.getByRole('button',{name:'Unterkunft 4 wählen'}).click();await page.getByText('Paarvergleich abgeschlossen.',{exact:false}).waitFor();
  await page.getByRole('button',{name:'Rangfolge speichern',exact:true}).click();await page.locator('.endrunde').waitFor({state:'detached'});
  assert.deepEqual(calls.filter(p=>p.aktion==='unterkunft_eigenes_ranking_setzen').at(-1).daten.reihenfolge,[4,3]);
});
for(const count of [0,2])test('W71: Weitere suchen '+count+' neue, Kostenhinweis und nur ein Start',async t=>{
  const d=reviewData();d.suchauftrag.runde=1;d.treffer.forEach(t=>t.runde=1);
  const {page,calls}=await setup(t,p=>{if(p.aktion==='unterkunft_suche_starten'){d.suchauftrag.runde=2;for(let i=0;i<count;i++)d.treffer.push(hit(20+i,'A',100,{status:'aktiv',runde:2}));return{ok:true,runde:2};}return d;});
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Weitere suchen',exact:true}).click();await page.getByText('Kostet ca. 0,05–0,50 USD;', {exact:false}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_suche_starten').length,0);await page.getByRole('button',{name:'Jetzt weitere suchen',exact:true}).dblclick();
  await page.getByRole('status').filter({hasText:count+' neue Unterkünfte'}).waitFor();assert.equal(calls.filter(p=>p.aktion==='unterkunft_suche_starten').length,1);
  if(count)assert.equal(await page.locator('[data-review-hit]').getAttribute('data-review-hit'),'20');else await page.getByText('Angebot für diese Filter ausgeschöpft',{exact:false}).waitFor();
});
test('W71: unklare Urteilsantwort sperrt weitere Entscheidungen bis Aktualisierung',async t=>{
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_durchsehen_urteil'?{ok:true}:reviewData());await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();await page.getByRole('button',{name:'Favorit',exact:true}).click();
  await page.getByText('Speichern nicht bestätigt:',{exact:false}).waitFor();assert.equal(await page.getByRole('button',{name:'Weg',exact:true}).isDisabled(),true);assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
  await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();await page.waitForFunction(()=>!Array.from(document.querySelectorAll('button')).find(b=>b.textContent==='Weg').disabled);
});
test('W71: gesperrter Gerätespeicher bleibt bedienbar, Reihenfolge per Ziehen',async t=>{
  const {page}=await setup(t,()=>reviewData());
  await page.addInitScript(()=>{const read=Storage.prototype.getItem;Storage.prototype.getItem=function(k){if(k.startsWith('ks_anzeige'))throw Error('denied');return read.call(this,k);};const write=Storage.prototype.setItem;Storage.prototype.setItem=function(k,v){if(k!=='ks_token')throw Error('denied');return write.call(this,k,v);};});
  await page.goto(origin+'/#/anzeige');await page.locator('li[data-field="storno"]').dragTo(page.locator('li[data-field="preis"]'),{sourcePosition:{x:10,y:10},targetPosition:{x:10,y:10}});
  assert.equal(await page.locator('.display-order li').first().getAttribute('data-field'),'storno');
  await page.getByText('Gerätespeicher nicht verfügbar.',{exact:false}).waitFor();
  await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();assert.equal(await page.locator('[data-hit="1"] td[data-field]').first().getAttribute('data-field'),'storno');
});
test('W71: verspätete Leseantwort verliert kein Urteil; Endrunde bleibt erreichbar',async t=>{
  const d=reviewData();let readCount=0,releaseRead;
  const handler=reviewHandler(d),{page}=await setup(t,async p=>{if(p.aktion==='unterkunft_suchlauf_lesen' && ++readCount===2){const old=structuredClone(d);return new Promise(resolve=>releaseRead=()=>resolve(old));}return handler(p);});
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  await page.locator('.review-run-tools > summary').click();await page.getByRole('button',{name:'Aktualisieren',exact:true}).click();await waitForCallback(()=>releaseRead);
  await page.getByRole('button',{name:'Favorit',exact:true}).click();await page.locator('[data-review-hit="1"]').waitFor();releaseRead();
  await page.waitForFunction(()=>!Array.from(document.querySelectorAll('button')).find(b=>b.textContent==='Aktualisieren').disabled);
  assert.equal(await page.locator('[data-review-hit]').getAttribute('data-review-hit'),'1');
  await page.getByRole('button',{name:'Endrunde',exact:true}).click();await page.locator('[data-final-hit="2"]').waitFor();
});
test('W71: mobile Tinder-Karte und Anzeige ohne Überlauf',async t=>{
  const {page}=await setup(t,reviewHandler(reviewData()),{width:390,height:844});await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  await page.locator('.review-card').scrollIntoViewIfNeeded();
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  assert.equal(await page.locator('.review-card').textContent().then(s=>s.includes('null')),false);
  fs.mkdirSync(path.join(root,'test-results'),{recursive:true});await page.screenshot({path:path.join(root,'test-results/w71-tinder-mobile.png')});
  await page.goto(origin+'/#/anzeige');await page.getByRole('heading',{name:'Anzeige',exact:true,level:2}).waitFor();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.screenshot({path:path.join(root,'test-results/w71-anzeige-mobile.png')});
});

// PR9 scenarios adapted to the authoritative message 241 contract.
test('Durchsehen: A vor B, bestätigte Urteile, Na ja bleibt bewertet gemäß Nachricht 241, Gründe und echtes Rückgängig', async t => {
  const data=result(); data.treffer=[hit(1,'A',700,{bewertung:{liste:'A',rang:1}}),hit(2,'B',600),hit(3,'A',500,{status:'favorit'}),hit(4,'A',400,{status:'ausgeschlossen'}),hit(5,'A',300,{topf:'ausgeschlossen'})];
  let release, hold=true;
  const {page,calls}=await setup(t,async p=>{
    if(p.aktion === 'unterkunft_durchsehen_urteil') {
      if(hold) await new Promise(r=>{release=r;});
      const status={favorit:'favorit',vielleicht:'vielleicht',weg:'ausgeschlossen',offen:'aktiv'}[p.daten.urteil];
      data.treffer.find(t=>t.treffer_id===p.daten.treffer_id).status=status;
      return {ok:true,...p.daten,status};
    }
    return data;
  },{width:390,height:844});
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  const dialog=page.locator('.stay-review');
  await dialog.getByRole('heading',{name:'Unterkunft 1',exact:true}).waitFor();
  await dialog.getByRole('button',{name:'Na ja',exact:true}).dblclick();
  await waitForCallback(()=>release);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
  assert.equal(await dialog.getByRole('button',{name:'Weg',exact:true}).isDisabled(),true);

  hold=false; release();
  await dialog.getByRole('heading',{name:'Unterkunft 2',exact:true}).waitFor();
  await page.getByRole('button',{name:'Gründe ergänzen',exact:true}).click();await page.locator('.review-reasons').getByRole('button',{name:'Preis',exact:true}).click();
  await page.getByRole('button',{name:'Gründe speichern',exact:true}).click();
  await dialog.getByRole('button',{name:'Letzte Entscheidung rückgängig'}).click();
  await dialog.getByRole('heading',{name:'Unterkunft 1',exact:true}).waitFor();
  const writes=calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil');
  assert.deepEqual(writes.map(p=>[p.daten.urteil,p.daten.gruende]),[['vielleicht',[]],['vielleicht',['preis']],['offen',[]]]);
  await dialog.getByRole('button',{name:'Na ja',exact:true}).click();
  await dialog.getByRole('heading',{name:'Unterkunft 2',exact:true}).waitFor();
  await dialog.getByRole('button',{name:'Favorit',exact:true}).click();
  await dialog.getByRole('heading',{name:'Alle Unterkünfte durchgesehen.'}).waitFor();
  assert.equal(data.treffer[0].status,'vielleicht');
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  await page.locator('.stay-review').waitFor({state:'detached'});
  assert.equal(await page.locator('.stay-review').count(),0);
  await page.locator('.stay-filters > summary').click();
  await page.getByLabel('Meine Entscheidung',{exact:true}).selectOption('vielleicht');
  assert.deepEqual(await page.locator('[data-hit]').evaluateAll(rows=>rows.map(row=>row.dataset.hit)),['1']);
});

test('Durchsehen: übernommene Urteile, Preishinweis, Fehler ohne automatisches Wiederholen', async t => {
  const data=result(); data.treffer=[hit(1,'A',700,{status:'favorit',urteil_uebernommen:{urteil:'favorit',suchauftrag_id:1}}),hit(2,'A',600,{status:'aktiv',urteil_uebernommen:{urteil:'weg',hinweis:'Preis deutlich gesunken',suchauftrag_id:1}}),hit(3,'B',500,{status:'vielleicht'})];
  const {page,calls}=await setup(t,p=>p.aktion==='unterkunft_durchsehen_urteil'?{ok:true,treffer_id:999,urteil:p.daten.urteil,status:'favorit'}:data);
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  const dialog=page.locator('.stay-review');
  await dialog.getByRole('heading',{name:'Unterkunft 2',exact:true}).waitFor();
  await dialog.getByText('Jetzt günstiger · Preis deutlich gesunken',{exact:true}).waitFor();
  await dialog.getByRole('button',{name:'Favorit',exact:true}).click();
  await dialog.getByRole('status').filter({hasText:'Speichern nicht bestätigt'}).waitFor();
  assert.equal(await dialog.getByRole('button',{name:'Weg',exact:true}).isDisabled(),true);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
  assert.equal(data.treffer[1].status,'aktiv');
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  assert.equal(await page.locator('[data-selection="2"]').getByRole('button',{name:'☆ Favorit',exact:true}).isDisabled(),true);
  await page.getByRole('button',{name:'Tinder',exact:true}).click();
  assert.equal(await page.locator('.stay-review').getByRole('button',{name:'Weg',exact:true}).isDisabled(),true);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
});

test('Kernangaben: echte Fläche, deutsche Bettfilter, lange Wege und Rakuten-Hotelübersicht', async t=>{
  const data=result();data.treffer=[hit(1,'A',700,{angebot:{kategorie_id:10,link:'https://img.travel.rakuten.co.jp/image/tr/api/re/IdsCY/?f_no=167060',preis_gesamt_eur:700},kategorien:[{id:10,name:'Family',m2:47.1,betten_text:'2 twin beds, 2 sofa beds, 3 futon beds',schlafzimmer:2}],gehzeit_min:234,gehzeit_art:'geschaetzt',station_name:'Omiya'})];
  const {page,calls}=await setup(t,()=>data,{width:390,height:844});
  await page.goto(origin+'/#/suche/2');await page.locator('[data-hit="1"]').waitFor();
  assert.equal(await page.locator('[data-field="m2"]').textContent(),'47,1 m²');
  assert.match(await page.locator('[data-field="gehzeit"]').textContent(),/3 Std. 54 Min. zu Fuß · Omiya/);
  assert.equal(await page.getByRole('link',{name:'Hotel bei Rakuten ansehen ↗'}).getAttribute('href'),'https://travel.rakuten.co.jp/HOTEL/167060/167060.html');
  await page.locator('.stay-filters > summary').click();await page.getByLabel('Bettentyp enthält',{exact:true}).fill('Einzelbett');
  assert.equal(await page.locator('[data-hit]').count(),1);
  await page.getByLabel('Fläche mindestens (m²)',{exact:true}).fill('50');
  assert.equal(await page.locator('[data-hit]').count(),0);
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,0);
});

test('Integration: Anbieter-Rückkehrfrage ohne Urteil; falscher Status sperrt auch Liste',async t=>{
  const d=reviewData(),{page,calls}=await setup(t,p=>p.aktion==='unterkunft_durchsehen_urteil'?{ok:true,...p.daten,status:'aktiv'}:d);
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  await page.locator('.review-card a[target=_blank]').evaluate(a=>{a.addEventListener('click',e=>e.preventDefault(),{once:true});a.click();document.dispatchEvent(new Event('visibilitychange'));});
  await page.getByText('Und? Wie gefällt dir die Unterkunft?',{exact:true}).waitFor();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,0);
  await page.getByRole('button',{name:'Favorit',exact:true}).click();await page.getByText('Speichern nicht bestätigt:',{exact:false}).waitFor();
  await page.getByRole('button',{name:'Liste',exact:true}).click();
  assert.equal(await page.locator('[data-selection="2"]').getByRole('button',{name:'☆ Favorit',exact:true}).isDisabled(),true);
});

test('Integration: Halbierungs-Paarvergleich ordnet 10 Favoriten mit höchstens 25 Fragen',async t=>{
  const d=reviewData();d.treffer=Array.from({length:10},(_,i)=>hit(i+1,'A',100,{status:'favorit',eigener_rang:i+1}));
  const {page,calls}=await setup(t,reviewHandler(d));await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Endrunde',exact:true}).click();await page.getByRole('button',{name:'Paarvergleich starten'}).click();
  let count=0;
  while(await page.locator('.pair-options button').count()){
    assert(++count<=25);const buttons=page.locator('.pair-options button').filter({hasText:'wählen'});
    const labels=await buttons.allTextContents();const ix=Number(labels[0].match(/\d+/)[0])>Number(labels[1].match(/\d+/)[0])?0:1;
    await buttons.nth(ix).click();
  }
  await page.getByRole('button',{name:'Rangfolge speichern'}).click();
  await page.locator('.endrunde').waitFor({state:'detached'});
  assert.deepEqual(calls.filter(p=>p.aktion==='unterkunft_eigenes_ranking_setzen').at(-1).daten.reihenfolge,[10,9,8,7,6,5,4,3,2,1]);
});

test('W73: kompakte Tinder-Bedienprobe mit langen Angaben und Gründen',async t=>{
  const d=reviewData();d.treffer.forEach((hit,i)=>{
    hit.name=['Gartenhaus am Fluss – Familienapartment mit zwei Schlafzimmern','Stadthaus mit Terrasse'][i%2];
    hit.angebot={...hit.angebot,kategorie_id:i+1,storno:'Kostenlos bis 25. Oktober'};
    hit.kategorien=[{id:i+1,m2:64,schlafzimmer:2}];hit.gehzeit_min=7;hit.gehzeit_art='route';hit.station_name='Kyoto Shiyakusho-mae';hit.note_geeicht=9.2;
    hit.bilder=['https://example.com/photo-a.svg','https://example.com/photo-b.svg'];hit.bewertung.rang=i+1;
  });
  const {page,calls}=await setup(t,reviewHandler(d),{width:390,height:844});
  await page.route('https://example.com/photo-*.svg',r=>r.fulfill({contentType:'image/svg+xml',body:'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450"><rect width="800" height="450" fill="#d1d9ce"/><rect x="80" y="60" width="300" height="210" fill="#87a7a7"/><rect x="450" y="190" width="300" height="130" rx="25" fill="#b6a18b"/><path d="M0 340h800v110H0" fill="#d8cbb2"/></svg>'}));
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Tinder',exact:true}).click();
  await page.screenshot({path:path.join(root,'test-results/w73-after.png')});
  const cardTop=(await page.locator('.review-card').boundingBox()).y;
  await page.getByRole('button',{name:'Nächstes Foto',exact:true}).click();
  await page.getByRole('button',{name:'Favorit',exact:true}).click();
  await page.locator('[data-review-hit="1"]').waitFor();
  await page.screenshot({path:path.join(root,'test-results/w73-after-vote.png')});
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
  assert.equal((await page.locator('.review-card').boundingBox()).y,cardTop);
  await page.getByRole('button',{name:'Nächstes Foto',exact:true}).click();
  await page.getByRole('button',{name:'Gründe ergänzen',exact:true}).click();
  const reasons=page.getByRole('dialog',{name:'Gründe ergänzen',exact:true});
  await reasons.getByRole('button',{name:'Lage',exact:true}).click();
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,1);
  await reasons.getByRole('button',{name:'Schließen',exact:true}).click();
  assert.match(await page.locator('.review-card img').getAttribute('src'),/photo-b/);
  await page.getByRole('button',{name:'Gründe ergänzen',exact:true}).click();
  assert.equal(await reasons.getByRole('button',{name:'Lage',exact:true}).getAttribute('aria-pressed'),'true');
  await reasons.getByRole('button',{name:'Gründe speichern',exact:true}).click();
  await reasons.waitFor({state:'detached'});
  assert.deepEqual(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').at(-1).daten.gruende,['plus_lage']);
  assert.match(await page.locator('.review-card img').getAttribute('src'),/photo-b/);
  for(const size of [{width:320,height:700},{width:375,height:812},{width:390,height:844},{width:430,height:932},{width:1440,height:1000}]){
    await page.setViewportSize(size);
    assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    const metrics=await page.locator('.review-actions').evaluate(n=>{const r=n.getBoundingClientRect(),tabs=document.querySelector('#tabs').getBoundingClientRect();return{top:r.top,bottom:r.bottom,limit:tabs.width>innerWidth/2?tabs.top:innerHeight,buttons:[...n.querySelectorAll('button')].map(b=>b.getBoundingClientRect().height)};});
    assert(metrics.top>0 && metrics.bottom<=metrics.limit,JSON.stringify({size,metrics}));
    assert(metrics.buttons.every(h=>h>=44));
    if(size.width===1440)await page.screenshot({path:path.join(root,'test-results/w73-desktop.png')});
  }
  await page.setViewportSize({width:390,height:844});
  const beforeTouch=calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length;
  await page.locator('.review-swipe').dispatchEvent('pointerdown',{pointerId:4,pointerType:'touch',button:0,clientX:180,clientY:350});
  await page.locator('.review-swipe').dispatchEvent('pointerup',{pointerId:4,pointerType:'touch',button:0,clientX:180,clientY:150});
  assert.equal(calls.filter(p=>p.aktion==='unterkunft_durchsehen_urteil').length,beforeTouch);
  await page.getByRole('button',{name:'Details',exact:true}).click();
  await page.getByRole('dialog').waitFor();
  await page.keyboard.press('Escape');await page.getByRole('dialog').waitFor({state:'detached'});
  assert.equal(await page.evaluate(()=>document.activeElement.textContent),'Details');
});

test('W78: Viertelknopf, Endrunde und Seitenmarke bleiben auf schmalen Displays lesbar',async t=>{
  const d=reviewData();d.treffer.filter(x=>x.status==='favorit').forEach(x=>x.name='Sehr langes Familienapartment am Fluss mit zwei Schlafzimmern '+x.treffer_id);
  const handler=reviewHandler(d),{page}=await setup(t,p=>p.aktion==='unterkunft_viertel_lesen'?districts():handler(p),{width:320,height:700});
  await page.goto(origin+'/#/viertel');
  const load=page.getByRole('button',{name:'Viertel laden',exact:true});await load.waitFor();
  assert(await load.evaluate(n=>{const r=n.getBoundingClientRect();return r.width>100&&r.height>=44&&getComputedStyle(n).whiteSpace==='nowrap';}));
  await page.goto(origin+'/#/suche/2');await page.getByRole('button',{name:'Endrunde',exact:true}).click();
  const row=page.locator('[data-final-hit]').first();
  const rects=await row.locator('button').evaluateAll(ns=>ns.map(n=>{let r=n.getBoundingClientRect();return {y:r.y,w:r.width,h:r.height,right:r.right};}));
  assert.equal(rects[0].y,rects[1].y);assert(rects.every(r=>r.w>=44&&r.h>=44&&r.right<=320));
  assert(await row.locator('.final-name').evaluate(n=>n.getBoundingClientRect().width>=200));
  await page.screenshot({path:path.join(root,'test-results/w78-endrunde-mobile.png')});
  await page.getByRole('button',{name:'Endrunde schließen',exact:true}).click();
  for(const name of ['Liste','Tabelle','Tinder','Karte']){
    await page.getByRole('button',{name,exact:true}).click();
    assert.equal(await page.evaluate(()=>window.scrollY),0);
    assert.equal(await page.locator('#ver').isVisible(),false);
  }
  await page.setViewportSize({width:1440,height:1000});
  const brand=page.locator('#area-brand');
  assert(await brand.evaluate(n=>n.scrollWidth<=n.clientWidth));
  await page.screenshot({path:path.join(root,'test-results/w78-desktop.png')});
});
