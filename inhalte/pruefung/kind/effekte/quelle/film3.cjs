const { chromium } = require('/home/claude/wt/node_modules/playwright');
const Z = '/home/claude/ki-system/inhalte/pruefung/kind/effekte';
const F = { clown: [1800, 3500, 4300, 5600], stromausfall: [1700, 2600, 3500, 4600], krake: [1500, 2400, 3400, 4300], knochenhand: [1300, 2200], spinne: [1200, 2000] };
(async () => { const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const fehler = [];
  for (const [id, ts] of Object.entries(F)) for (const n of [0, 1]) { const p = await br.newPage({ viewport: { width: 400, height: 760 } }); p.on('pageerror', (e) => fehler.push(id + ': ' + e.message));
    await p.goto(`file://${Z}/entwurf/effekte.html?fx=${id}&nacht=${n}`); const t0 = Date.now();
    for (const [i, t] of ts.entries()) { const w = t - (Date.now() - t0); if (w > 0) await p.waitForTimeout(w); await p.screenshot({ path: `/tmp/h-${id}-${n}-${i}.png`, clip: { x: 12, y: 50, width: 376, height: 560 } }); }
    await p.waitForTimeout(5000); if (!(await p.locator('.sticker').count())) fehler.push(id + ': kein Sticker'); await p.close(); }
  const p = await br.newPage({ viewport: { width: 1280, height: 900 } }); p.on('pageerror', (e) => fehler.push('panel: ' + e.message)); await p.goto(`file://${Z}/entwurf/effekte.html?fx=spinne`); await p.waitForTimeout(4500); await p.screenshot({ path: `/tmp/panel.png`, fullPage: true });
  console.log('Fehler', fehler); await br.close(); })();
