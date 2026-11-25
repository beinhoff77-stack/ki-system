// Nachprüfung 0.74.2 (N1): alle Etappen durch lernErklaerung – Aufruf: PW_TEST_EXECUTABLE=… node n1-zaehlung-v0742.cjs <Arbeitskopie lernen-app>
'use strict';
const { chromium } = require(require('node:path').join(process.argv[2], 'node_modules/playwright'));
const http = require('node:http'), fs = require('node:fs'), path = require('node:path');
const root = process.argv[2];
(async () => {
  const server = http.createServer((req, res) => { const n = new URL(req.url, 'http://x').pathname; const f = path.join(root, n.endsWith('/') ? n + 'index.html' : n);
    if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
    res.setHeader('Content-Type', { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css' }[path.extname(f)] || 'text/plain'); res.end(fs.readFileSync(f)); });
  await new Promise((r) => server.listen(0, '127.0.0.1', r)); const origin = 'http://127.0.0.1:' + server.address().port;
  const browser = await chromium.launch({ executablePath: process.env.PW_TEST_EXECUTABLE });
  const page = await (await browser.newContext({ viewport: { width: 390, height: 844 }, serviceWorkers: 'block' })).newPage();
  await page.route('**/functions/**', (r) => r.fulfill({ contentType: 'application/json', body: '{"ok":false}' }));
  await page.route('https://cdnjs.cloudflare.com/**', (r) => r.abort());
  await page.goto(origin + '/index.html'); await page.waitForFunction(() => typeof lernErklaerung === 'function');
  const alle = [];
  for (const f of fs.readdirSync(path.join(root, 'inhalte/themen')).filter((x) => x.endsWith('.json') && fs.statSync(path.join(root, 'inhalte/themen', x)).size)) { const d = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themen', f))); for (const e of d.inhalt?.etappen || []) alle.push({ f, e }); }
  let erg = await page.evaluate((alle) => {
    const norm = (k) => { const c = k.cloneNode(true); c.querySelectorAll('.neu,.neu-text').forEach((x) => { x.classList.remove('neu', 'neu-text'); if (x.tagName === 'circle') x.removeAttribute('r'); }); c.querySelector('svg')?.classList.remove('mit-neu'); return c.outerHTML.replace(/lk[a-z0-9]{3,8}/g, ''); };
    const out = [];
    for (const { f, e } of alle) {
      const sch = (e.schritte || []).map((x) => (typeof x === 'string' ? { text: x } : x || {}));
      if (!sch.some((x) => x.bild)) continue;
      let k; try { k = lernErklaerung(e); } catch (err) { out.push({ f, t: e.titel, fehler: String(err) }); continue; }
      const wrap = document.createElement('div'); wrap.append(k);
      const lis = [...wrap.querySelectorAll('.lr-sogehts li')];
      const einstieg = [...wrap.querySelectorAll('.lr-bild')].find((b) => !b.closest('li') && !b.closest('.lr-passauf'));
      const seq = []; if (einstieg) seq.push(norm(einstieg));
      let doppelt = 0, ohneNeu = 0, mitBild = 0;
      for (const li of lis) { const b = li.querySelector(':scope > .lr-bild'); if (!b) continue; mitBild++; const t = norm(b); if (seq.length && seq.at(-1) === t) doppelt++; seq.push(t); if (!b.querySelector('.neu,.neu-text')) { ohneNeu++; (out.ohne ||= []).push({ f, t: e.titel, typ: b.querySelector('svg')?.getAttribute('class') + '|' + (b.querySelector('table')?'tabelle':''), erstes: seq.length === 1 }); } }
      out.push({ f, t: e.titel, schritte: lis.length, schrittBilder: sch.filter((x) => x.bild).length, gezeigt: mitBild, doppelt, ohneNeu, einstieg: !!einstieg });
    }
    return { out, ohne: out.ohne };
  }, alle);
  const ohne = erg.ohne; erg = erg.out;
  fs.writeFileSync('n1-ohne.json', JSON.stringify(ohne, null, 1));
  const s = (k) => erg.reduce((a, x) => a + (x[k] || 0), 0);
  console.log('Etappen mit Schrittbildern', erg.length, 'Fehler', erg.filter((x) => x.fehler).length, 'mit Doppel', erg.filter((x) => x.doppelt).length,
    'Schrittbilder Daten', s('schrittBilder'), 'gezeigt', s('gezeigt'), 'gezeigt ohne Hervorhebung', s('ohneNeu'));
  await browser.close(); server.close();
})();
