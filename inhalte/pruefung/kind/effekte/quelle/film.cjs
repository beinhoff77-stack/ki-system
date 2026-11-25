const { chromium } = require('/home/claude/wt/node_modules/playwright');
const Z = '/home/claude/ki-system/inhalte/pruefung/kind/effekte';
const F = { tresor: [1500, 3400, 4500, 5600, 7400], koffer: [1000, 2700, 3700, 4500, 6000], hacker: [1000, 2300, 3500, 4400, 5600] };
(async () => { const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const fehler = [];
  for (const [id, ts] of Object.entries(F)) for (const [b, hh, n] of [[400, 760, 0], [400, 760, 1], [820, 1100, 0]]) {
    const p = await br.newPage({ viewport: { width: b, height: hh } }); p.on('pageerror', (e) => fehler.push(id + ': ' + e.message));
    await p.goto(`file://${Z}/entwurf/effekte.html?fx=${id}&nacht=${n}`); const t0 = Date.now();
    for (const [i, t] of ts.entries()) { const w = t - (Date.now() - t0); if (w > 0) await p.waitForTimeout(w); await p.screenshot({ path: `/tmp/film-${id}-${b}-${n}-${i}.png`, clip: { x: b >= 760 ? 12 : 12, y: 50, width: b >= 760 ? 420 : b - 24, height: 560 } }); }
    await p.close(); }
  console.log('Fehler', fehler); await br.close(); })();
