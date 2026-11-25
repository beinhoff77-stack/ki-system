const { chromium } = require('/home/claude/wt/node_modules/playwright');
const Z = '/home/claude/ki-system/inhalte/pruefung/kind/effekte';
const F = { jet: [1250, 1900], applaus: [1500, 2700], gehirn: [1700, 2700], nitro: [1100, 2000], phoenix: [1500, 2400], niesen: [1500, 2300], tornado: [1600, 2600], feuerwerk: [2200, 3600] };
(async () => { const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const fehler = [];
  for (const [id, ts] of Object.entries(F)) for (const n of [0, 1]) { const p = await br.newPage({ viewport: { width: 400, height: 760 } }); p.on('pageerror', (e) => fehler.push(id + ': ' + e.message));
    await p.goto(`file://${Z}/entwurf/effekte.html?fx=${id}&nacht=${n}`); const t0 = Date.now();
    for (const [i, t] of ts.entries()) { const w = t - (Date.now() - t0); if (w > 0) await p.waitForTimeout(w); await p.screenshot({ path: `/tmp/v-${id}-${n}-${i}.png`, clip: { x: 12, y: 50, width: 376, height: 560 } }); }
    await p.waitForTimeout(4500); const st = await p.locator('.sticker').count(); if (!st && !['niesen'].includes(id)) fehler.push(id + ': kein Sticker am Ende');
    await p.close(); }
  console.log('Fehler', fehler); await br.close(); })();
