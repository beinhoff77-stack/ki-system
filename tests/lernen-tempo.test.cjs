// TEMPO (Ladezeiten, Entwurf): Abruf-Speicher in lernen.js (Zusammenlegen, kurz merken, Vergessen) und sw.js (versionierte Hülle zuerst aus dem Cache).
// lernen-api wird hier nachgestellt (Zähler je Aktion, feste Verzögerung); keine echten Daten.
const { test, before, after } = require('node:test');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
let browser, server, origin;
// Release-Nachstellung für den Service-Worker-Test: 'alt' = Dateien wie im Repo, 'neu' = alle ?v=0.96.0 → ?v=9.9.9, Cache-Name neu, lernen.js mit Marke
let release = 'alt'; const abrufe = [];
const VERSION = (fs.readFileSync(path.join(root, 'index.html'), 'utf8').match(/lernen\.js\?v=([\w.-]+)/) || [])[1];
const CACHE_NR = (fs.readFileSync(path.join(root, 'sw.js'), 'utf8').match(/CACHE_PREFIX \+ '(v\d+)'/) || [])[1];
before(async () => {
  server = http.createServer((req, res) => {
    const u = new URL(req.url, 'http://localhost'); const name = u.pathname;
    abrufe.push(name + u.search);
    const file = path.join(root, name.endsWith('/') ? name + 'index.html' : name);
    if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); res.end(); return; }
    const types = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.svg': 'image/svg+xml', '.png': 'image/png', '.webmanifest': 'application/manifest+json', '.woff2': 'font/woff2' };
    res.setHeader('Content-Type', types[path.extname(file)] || 'text/plain');
    let body = fs.readFileSync(file);
    if (release === 'neu' && ['.html', '.js'].includes(path.extname(file))) {
      let s = body.toString('utf8');
      if (['/index.html', '/', '/sw.js', '/lernen/', '/lernen/index.html'].includes(name)) s = s.split('?v=' + VERSION).join('?v=9.9.9');
      if (name === '/sw.js') s = s.replace(`CACHE_PREFIX + '${CACHE_NR}'`, "CACHE_PREFIX + 'v999'");
      if (name === '/lernen.js' && u.searchParams.get('v') === '9.9.9') s += '\n;window.__TEMPO_NEU = true;\n';
      body = Buffer.from(s, 'utf8');
    }
    res.end(body);
  });
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  origin = `http://127.0.0.1:${server.address().port}`;
  try { browser = await chromium.launch({ headless: true, ...(process.env.PW_TEST_EXECUTABLE ? { executablePath: process.env.PW_TEST_EXECUTABLE } : {}) }); }
  catch { browser = await chromium.launch({ headless: true, channel: 'msedge' }); }
});
after(async () => { await browser?.close(); await new Promise((resolve) => server?.close(resolve)); });

// Seite mit nachgestelltem lernen-api: zählt jede Aktion (Name + Daten), Antwort nach `ms`, Ergebnis enthält eine laufende Nummer (frisch oder gemerkt?)
async function seite(t, { ms = 150 } = {}) {
  const context = await browser.newContext({ serviceWorkers: 'block' });
  t.after(() => context.close());
  await context.addInitScript(() => { localStorage.setItem('ks_token', 'synthetic-test-session'); });
  const page = await context.newPage();
  const errors = []; page.on('pageerror', (e) => errors.push(e.message)); t.after(() => assert.deepEqual(errors, []));
  await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.route('**/functions/v1/app-api/**', (r) => r.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: {} }) }));
  const netz = []; let nr = 0; const srv = { stand: 0, msJe: {}, abgelaufen: null };
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); netz.push(b.aktion + JSON.stringify(b.daten || {})); const n = ++nr;
    const tok = (route.request().headers().authorization || '').replace('Bearer ', '');
    const liest = /^schule_(merkheft|konto|wiederholung|einheit_lesen|uebersicht|eltern|rueckmeldungen)$|_lesen$/.test(b.aktion);
    if (!liest) srv.stand++; // schreibende Aktion: Stand am Server steigt sofort
    const stand = srv.stand;
    await new Promise((r) => setTimeout(r, srv.msJe[b.aktion] ?? ms));
    if (srv.abgelaufen && tok === srv.abgelaufen) { await route.fulfill({ status: 401, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'abgelaufen' }) }); return; }
    await route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, nr: n, aktion: b.aktion, stand } }) });
  });
  await page.goto(origin + '/#/meldungen'); await page.waitForFunction(() => typeof lernCall === 'function');
  await page.waitForTimeout(300); netz.length = 0;
  const zahl = (a) => netz.filter((x) => x.startsWith(a + '{')).length;
  const zahlKind = (a, k) => netz.filter((x) => x.startsWith(a + '{') && JSON.parse(x.slice(a.length)).lernender_id === k).length;
  return { page, netz, zahl, zahlKind, srv };
}

test('TEMPO: gleichzeitige gleiche Lese-Abrufe teilen sich eine Antwort; verschiedene Daten bleiben getrennt; Aufrufer bekommen Kopien', async (t) => {
  const { page, zahl } = await seite(t);
  const r = await page.evaluate(async () => {
    const xs = await Promise.all([lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 }), lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 }),
      lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 6 }), lernCall('schule_wiederholung', { lernender_id: 1 }), lernCall('schule_wiederholung', { lernender_id: 1 })]);
    xs[0].nr = -1; // verändert nur die eigene Kopie
    return { nr: xs.map((x) => x.nr) };
  });
  assert.equal(zahl('schule_einheit_lesen'), 2, 'Einheit 5 einmal, Einheit 6 einmal'); assert.equal(zahl('schule_wiederholung'), 1);
  assert.equal(r.nr[1] === r.nr[2], false); assert.notEqual(r.nr[1], -1, 'Kopie je Aufrufer');
  // danach (nichts läuft mehr): wiederholung und einheit_lesen kommen wieder frisch vom Server (kein Speicher – Zufall/Ausgabe am Server)
  await page.evaluate(() => Promise.all([lernCall('schule_wiederholung', { lernender_id: 1 }), lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 })]));
  assert.equal(zahl('schule_wiederholung'), 2); assert.equal(zahl('schule_einheit_lesen'), 3);
});

test('TEMPO: Merkheft/Konto kurz gemerkt; jede schreibende Aktion (vorher und nachher), Kindwechsel, Ablauf und Abmelden vergessen', async (t) => {
  const { page, zahl } = await seite(t);
  const nrVon = (a, d) => page.evaluate(([a, d]) => lernCall(a, d).then((x) => x.nr), [a, d]);
  const m1 = await nrVon('schule_merkheft', { lernender_id: 1 }); const k1 = await nrVon('schule_konto', { lernender_id: 1 });
  assert.equal(await nrVon('schule_merkheft', { lernender_id: 1 }), m1, 'zweiter Abruf aus dem Speicher'); assert.equal(await nrVon('schule_konto', { lernender_id: 1 }), k1);
  assert.equal(zahl('schule_merkheft'), 1); assert.equal(zahl('schule_konto'), 1);
  // eine beantwortete Aufgabe: danach alles frisch – auch eine Antwort, die WÄHREND des Schreibens lief, wird nicht gemerkt
  await page.evaluate(async () => { const w = lernCall('schule_uebung_pruefen', { lernender_id: 1, aufgabe_id: 9, antwort: { wert: 1 } }); const l = lernCall('schule_merkheft', { lernender_id: 1 }); await Promise.all([w, l]); });
  const m2 = await nrVon('schule_merkheft', { lernender_id: 1 });
  assert.equal(zahl('schule_merkheft'), 3, 'nach dem Schreiben neu (auch der gleichzeitige Abruf zählt nicht)'); assert.ok(m2 > m1);
  assert.notEqual(await nrVon('schule_konto', { lernender_id: 1 }), k1); assert.equal(zahl('schule_konto'), 2);
  // Schreiben ohne Kind (z. B. Belohnung pflegen) vergisst alles
  await page.evaluate(() => lernCall('schule_belohnung_setzen', { titel: 'x' }));
  await nrVon('schule_merkheft', { lernender_id: 1 }); assert.equal(zahl('schule_merkheft'), 4);
  // Kindwechsel: Kind 2 lesen vergisst das kurz Gemerkte von Kind 1
  await nrVon('schule_merkheft', { lernender_id: 2 }); await nrVon('schule_merkheft', { lernender_id: 1 }); assert.equal(zahl('schule_merkheft'), 6);
  // Ablauf: nach LERN_KURZ_MS wieder vom Server
  await page.evaluate(() => { for (const e of lernSpeicher.values()) if (e.fertig) e.fertig -= LERN_KURZ_MS + 1; });
  await nrVon('schule_merkheft', { lernender_id: 1 }); assert.equal(zahl('schule_merkheft'), 7);
  // Abmelden / anderer Zugang: nichts aus der alten Sitzung
  await page.evaluate(() => { store.token = 'synthetic-andere-sitzung'; });
  await nrVon('schule_merkheft', { lernender_id: 1 }); assert.equal(zahl('schule_merkheft'), 8);
  // Rückmeldungen lesen vergisst nichts mehr (vorher als schreibend behandelt)
  await page.evaluate(() => lernCall('schule_rueckmeldungen'));
  await nrVon('schule_merkheft', { lernender_id: 1 }); assert.equal(zahl('schule_merkheft'), 8);
});

test('TEMPO: Vorab-Abruf (lernVorladen) wird genau einmal abgeholt – auch wenn er schon fertig ist; danach wieder vom Server', async (t) => {
  const { page, zahl } = await seite(t, { ms: 50 });
  await page.evaluate(() => lernVorladen('schule_wiederholung', { lernender_id: 1 }));
  await page.waitForTimeout(200); // schon fertig
  const a = await page.evaluate(() => lernCall('schule_wiederholung', { lernender_id: 1 }).then((x) => x.nr));
  assert.equal(zahl('schule_wiederholung'), 1, 'Vorab-Antwort abgeholt');
  const b = await page.evaluate(() => lernCall('schule_wiederholung', { lernender_id: 1 }).then((x) => x.nr));
  assert.equal(zahl('schule_wiederholung'), 2); assert.ok(b > a, 'zweiter Abruf frisch');
  // nach einem Schreiben gilt eine Vorab-Antwort nicht mehr
  await page.evaluate(() => lernVorladen('schule_wiederholung', { lernender_id: 1 })); await page.waitForTimeout(150);
  await page.evaluate(() => lernCall('schule_wiederholung_runde_fertig', { lernender_id: 1 }));
  await page.evaluate(() => lernCall('schule_wiederholung', { lernender_id: 1 }));
  assert.equal(zahl('schule_wiederholung'), 4);
});

test('1175/2: Lese-Antwort, die während einer Buchung lief, wird nicht ausgeliefert – der Aufrufer bekommt den Stand nach der Buchung', async (t) => {
  const { page, srv } = await seite(t, { ms: 50 });
  srv.msJe.schule_merkheft = 400; srv.msJe.schule_konto = 400; srv.msJe.schule_uebersicht = 400;
  const r = await page.evaluate(async () => {
    const lesen = [lernCall('schule_merkheft', { lernender_id: 1 }), lernCall('schule_konto', { lernender_id: 1 }), lernCall('schule_uebersicht')];
    await new Promise((ok) => setTimeout(ok, 50));
    await lernCall('schule_uebung_pruefen', { lernender_id: 1, aufgabe_id: 9, antwort: { wert: 1 } });
    return (await Promise.all(lesen)).map((x) => x.stand); });
  assert.deepEqual(r, [1, 1, 1], 'alle drei mit dem Stand nach der Buchung');
});
test('1175/3: Vorab an Kind gebunden (A → B → A frisch), laufendes Vorab teilen (kein Doppelabruf), Beförderung lauf → vorab behält die Antwort', async (t) => {
  const { page, zahlKind, zahl, srv } = await seite(t, { ms: 200 });
  // A → B → A
  await page.evaluate(() => lernVorladen('schule_wiederholung', { lernender_id: 1 })); await page.waitForTimeout(300);
  await page.evaluate(() => lernCall('schule_wiederholung', { lernender_id: 2 }));
  await page.evaluate(() => lernCall('schule_wiederholung', { lernender_id: 1 }));
  assert.equal(zahlKind('schule_wiederholung', 1), 2, 'nach B wird A frisch geholt (nicht die alte Vorab-Antwort)');
  // laufendes Vorab: ein Verbraucher holt ab, ein zweiter kommt dazu – ein Abruf
  const n0 = zahl('schule_einheit_lesen');
  await page.evaluate(async () => { lernVorladen('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 });
    const a = lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 }); const b = lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 }); await Promise.all([a, b]); });
  assert.equal(zahl('schule_einheit_lesen') - n0, 1, 'ein Abruf für Vorab + zwei Verbraucher');
  // Beförderung: läuft (normal), wird vorgeladen → Antwort bleibt für den nächsten Abruf liegen
  const n1 = zahl('schule_einheit_lesen');
  await page.evaluate(async () => { const a = lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 6 }); lernVorladen('schule_einheit_lesen', { lernender_id: 1, einheit_id: 6 }); await a; });
  await page.waitForTimeout(50);
  await page.evaluate(() => lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 6 }));
  assert.equal(zahl('schule_einheit_lesen') - n1, 1, 'beförderte Antwort einmal abgeholt');
});
test('1175/4: verspätetes 401 des alten Zugangs meldet den neuen nicht ab; Antwort des alten Zugangs wird verworfen', async (t) => {
  const { page, srv } = await seite(t, { ms: 300 });
  srv.abgelaufen = 'synthetic-test-session';
  const r = await page.evaluate(async () => {
    const p = lernCall('schule_konto', { lernender_id: 1 }).then(() => 'ok', (e) => e.message);
    await new Promise((ok) => setTimeout(ok, 50)); store.token = 'synthetic-neue-sitzung';
    const fehler = await p; return { fehler, token: store.token, hash: location.hash }; });
  assert.equal(r.token, 'synthetic-neue-sitzung'); assert.notEqual(r.hash, '#/login'); assert.match(r.fehler, /Zugang gewechselt/);
});

// ---------- sw.js ----------
test('1175/5 Release-Regel: beide HTML-Einstiege, sw.js-Hülle und App-Version nennen dieselbe Version; jede Hüllen-Datei der Einstiege steht mit ihr in sw.js', async () => {
  const lies = (f) => fs.readFileSync(path.join(root, f), 'utf8');
  const versionen = (t) => [...t.matchAll(/\?v=([\w.-]+)/g)].map((m) => m[1]);
  const sw = lies('sw.js'); const huelle = JSON.parse(sw.match(/const HUELLE = (\[[^\]]*\])/)[1].replace(/'/g, '"'));
  const v = new Set([...versionen(lies('index.html')), ...versionen(lies('lernen/index.html')), ...versionen(huelle.join(' '))]);
  assert.equal(v.size, 1, 'eine Version überall: ' + [...v].join(', '));
  const [ver] = v;
  for (const m of lies('index.html').matchAll(/(?:src|href)="([^"]+\?v=[^"]+)"/g)) assert.ok(huelle.includes('./' + m[1]), `${m[1]} fehlt in HUELLE`);
  // 1199: auch der Schul-Einstieg – jede ?v=-Datei von lernen/index.html (relativ zu lernen/) steht in HUELLE, ebenso lernen/ und lernen/index.html
  for (const m of lies('lernen/index.html').matchAll(/(?:src|href)="([^"]+\?v=[^"]+)"/g)) {
    const p = path.posix.normalize('lernen/' + m[1]); assert.ok(huelle.includes('./' + p), `lernen/index.html: ${p} fehlt in HUELLE`); }
  for (const p of ['./', './index.html', './lernen/', './lernen/index.html']) assert.ok(huelle.includes(p), `${p} fehlt in HUELLE`);
  for (const f of ['app.js', 'lernen/schule.js']) { const a = lies(f).match(/APP_VERSION\s*=\s*'([^']+)'/); assert.ok(a, `${f}: APP_VERSION fehlt`); assert.equal(a[1], ver, `${f}: APP_VERSION = ?v=`); }
});
function swLaden(cacheInhalt, netz) {
  const events = {}; const self = { registration: { scope: 'https://example.com/ki/' }, addEventListener: (n, cb) => { events[n] = cb; }, skipWaiting: () => {}, clients: { claim: () => {} } };
  const caches = { open: async () => ({ match: async (req) => cacheInhalt.get(typeof req === 'string' ? req : req.url) || undefined, put: async (req, r) => { cacheInhalt.set(req.url, r); } }) };
  const fetch = async (req) => { netz.push(req.url); return { ok: true, status: 200, url: req.url, clone() { return this; } }; };
  vm.runInNewContext(fs.readFileSync(path.join(root, 'sw.js'), 'utf8'), { self, URL, Set, caches, fetch });
  return events;
}
async function swAbruf(events, url) {
  let antwort = null, wartet = [];
  events.fetch({ request: { url, method: 'GET', mode: 'no-cors' }, respondWith: (p) => { antwort = p; }, waitUntil: (p) => wartet.push(p) });
  const r = antwort ? await antwort : 'durchgereicht'; await Promise.all(wartet); return r;
}
test('TEMPO sw.js: versionierte Hülle zuerst aus dem Cache, index.html/Daten/Karte Netz zuerst, fremde Version durchgereicht', async () => {
  const cache = new Map(); const netz = []; const ev = swLaden(cache, netz); const b = 'https://example.com/ki/';
  const lj = `${b}lernen.js?v=${VERSION}`;
  assert.equal((await swAbruf(ev, lj)).url, lj); assert.deepEqual(netz, [lj], 'nicht im Cache → Netz (und merken)');
  cache.set(lj, { gemerkt: true });
  assert.deepEqual(await swAbruf(ev, lj), { gemerkt: true }); assert.equal(netz.length, 1, 'im Cache → kein Netz');
  for (const u of [`${b}index.html`, b, `${b}icon.svg`, `${b}daten/regeln-universum.json?v=${VERSION}`, `${b}karte/welt.json`]) {
    cache.set(u, { gemerkt: true }); const n0 = netz.length; await swAbruf(ev, u); assert.equal(netz.length, n0 + 1, `${u}: Netz zuerst`);
  }
  const n0 = netz.length; assert.equal(await swAbruf(ev, `${b}lernen.js?v=9.9.9`), 'durchgereicht', 'neue Version (nicht in dieser Hülle) → Browser lädt selbst');
  assert.equal(netz.length, n0);
});

test('TEMPO sw.js im Browser: Hülle beim Neuladen aus dem Cache; ein neues Release kommt beim ersten Neuladen an, alter Cache wird gelöscht', async (t) => {
  release = 'alt'; abrufe.length = 0;
  const context = await browser.newContext({ serviceWorkers: 'allow' });
  t.after(async () => { release = 'alt'; await context.close(); });
  await context.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  const page = await context.newPage();
  const errors = []; page.on('pageerror', (e) => errors.push(e.message));
  await page.goto(origin + '/');
  await page.evaluate(() => navigator.serviceWorker.ready);
  await page.reload(); await page.waitForFunction(() => !!navigator.serviceWorker.controller);
  const lj = `/lernen.js?v=${VERSION}`, zaehle = (x) => abrufe.filter((a) => a === x).length;
  const vor = zaehle(lj), vorIndex = zaehle('/');
  await page.reload(); await page.waitForFunction(() => typeof lernCall === 'function');
  assert.equal(zaehle(lj), vor, 'lernen.js kam aus dem Cache (kein Abruf beim Server)');
  assert.ok(zaehle('/') > vorIndex, 'index.html weiter vom Netz');
  // neues Release
  release = 'neu';
  await page.reload(); await page.waitForFunction(() => typeof lernCall === 'function');
  assert.equal(await page.evaluate(() => window.__TEMPO_NEU === true), true, 'neues lernen.js schon beim ersten Neuladen');
  assert.ok(zaehle('/lernen.js?v=9.9.9') >= 1);
  // der Browser prüft sw.js beim Navigieren; hier ausdrücklich (gleicher Weg), dann warten, bis die neue Hülle aktiv ist und den alten Cache gelöscht hat
  await page.evaluate(async () => { const r = await navigator.serviceWorker.getRegistration(); await r.update(); });
  let keys = [];
  for (let i = 0; i < 100; i++) { keys = await page.evaluate(() => caches.keys()); if (keys.length === 1 && keys[0].endsWith(':v999')) break; await page.waitForTimeout(150); }
  assert.ok(keys.length === 1 && keys[0].endsWith(':v999'), 'nur noch der neue Cache: ' + keys.join(', '));
  assert.ok(abrufe.filter((a) => a === '/sw.js').length >= 2, 'sw.js neu geholt');
  const n = zaehle('/lernen.js?v=9.9.9');
  await page.reload(); await page.waitForFunction(() => typeof lernCall === 'function');
  assert.equal(await page.evaluate(() => window.__TEMPO_NEU === true), true);
  assert.equal(zaehle('/lernen.js?v=9.9.9'), n, 'neue Version jetzt aus dem neuen Cache');
  // 1199: zweiter Einstieg (Schul-Seite lernen/) bekommt dieselbe neue Version aus derselben Hülle
  await page.goto(origin + '/lernen/'); await page.waitForFunction(() => typeof lernCall === 'function');
  assert.equal(await page.evaluate(() => window.__TEMPO_NEU === true), true, 'lernen/: neues lernen.js');
  assert.equal(zaehle('/lernen.js?v=9.9.9'), n, 'lernen/: aus dem Cache der neuen Hülle');
  assert.deepEqual(errors, []);
});
test('1199/2: erschöpftes Wiederholungsbudget – überholte Antwort wird verworfen, nie ausgeliefert; Lehrer-Vorab nur mit Stand beim Abruf', async (t) => {
  const { page, srv } = await seite(t, { ms: 30 });
  srv.msJe.schule_konto = 300;
  const r = await page.evaluate(async () => {
    const p = lernCall('schule_konto', { lernender_id: 1 }).then((x) => 'stand ' + x.stand, (e) => (e.veraltet ? 'verworfen' : e.message));
    for (let i = 0; i < 4; i++) { await new Promise((ok) => setTimeout(ok, 150)); await lernCall('schule_uebung_pruefen', { lernender_id: 1, aufgabe_id: 9, antwort: { wert: i } }); }
    return p; });
  assert.equal(r, 'verworfen');
  // Ohne Stand beim Abruf hinterlegt lernVorabSetzen nichts
  const n = await page.evaluate(() => { lernVorabSetzen('schule_wiederholung', { lernender_id: 7 }, Promise.resolve({ x: 1 })); return lernSpeicher.has(lernSpeicherSchl('schule_wiederholung', { lernender_id: 7 })); });
  assert.equal(n, false);
});
test('1199/4: laufende Abfrage an das Kind gebunden (A → B → A holt für A frisch); gleiche Schreibaktion doppelt = ein POST', async (t) => {
  const { page, zahlKind, zahl } = await seite(t, { ms: 300 });
  await page.evaluate(async () => { const a1 = lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 }); await new Promise((ok) => setTimeout(ok, 30));
    const b = lernCall('schule_einheit_lesen', { lernender_id: 2, einheit_id: 5 }); await new Promise((ok) => setTimeout(ok, 30));
    const a2 = lernCall('schule_einheit_lesen', { lernender_id: 1, einheit_id: 5 }); await Promise.all([a1, b, a2]); });
  assert.equal(zahlKind('schule_einheit_lesen', 1), 2, 'A nach B neu');
  await page.evaluate(async () => { const d = { lernender_id: 1, belohnung_id: 5 }; await Promise.all([lernCall('schule_einloesen', d), lernCall('schule_einloesen', d)]); });
  assert.equal(zahl('schule_einloesen'), 1);
});
test('1199/4: app.js – verspätetes 401 einer Anfrage des alten Zugangs meldet den neuen nicht ab', async (t) => {
  const context = await browser.newContext({ serviceWorkers: 'block' }); t.after(() => context.close());
  await context.addInitScript(() => { localStorage.setItem('ks_token', 'synthetic-alt'); });
  const page = await context.newPage(); await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.route('**/functions/v1/app-api/**', async (r) => { const tok = (r.request().headers().authorization || '').replace('Bearer ', '');
    if (r.request().url().includes('/langsam')) { await new Promise((ok) => setTimeout(ok, 400)); return r.fulfill({ status: tok === 'synthetic-alt' ? 401 : 200, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'abgelaufen' }) }); }
    return r.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: {} }) }); });
  await page.route('**/functions/v1/lernen-api/**', (r) => r.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: {} }) }));
  await page.goto(origin + '/#/meldungen'); await page.waitForFunction(() => typeof http === 'function');
  const x = await page.evaluate(async () => { const p = http('/langsam').then(() => 'ok', (e) => e.message); await new Promise((ok) => setTimeout(ok, 50));
    store.token = 'synthetic-neu'; const m = await p; return { m, token: store.token }; });
  assert.equal(x.token, 'synthetic-neu'); assert.match(x.m, /Zugang gewechselt/);
});
