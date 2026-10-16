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
    await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: value, eingerichtet: true }) });
  });
  return { page, calls };
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
  await page.goto(origin + '/#/login');
  await page.evaluate(() => navigator.serviceWorker.ready);
  const cached = await page.evaluate(async () => (await (await caches.open('ki-system-v13')).keys()).map((r) => new URL(r.url).pathname));
  assert(cached.includes('/icon-512.png')); assert(cached.includes('/app.js'));
  assert(!cached.some((u) => u.includes('app-api')));
  await context.setOffline(true); await page.reload();
  await page.getByRole('heading', { name: 'Anmelden' }).waitFor();
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
