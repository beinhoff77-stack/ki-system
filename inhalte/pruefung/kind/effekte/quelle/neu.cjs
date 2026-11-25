const { chromium } = require('/home/claude/wt/node_modules/playwright');
const { execSync } = require('child_process');
const Z = '/home/claude/ki-system/inhalte/pruefung/kind/effekte';
const F = { boss: [1500, 2600, 3800], rang: [1200, 2000, 2900, 3600], replay: [1300, 2400, 3500], klopfen: [1400, 2800, 3300, 4400], streamchat: [1500, 2700], levelup: [1000, 1800], clip: [800], slice: [900], spiegel: [700, 1800],
  advent: [1000, 1800, 2700, '2026-12-10'], nikolaus: [1300, 2300, '2026-12-06'], weihnachten: [1500, 2600, 3700, 4400, '2026-12-24'], silvester: [1500, 3400, 4300, '2026-12-31'], ostern: [1500, 2600, 3500, '2027-03-28'], eiersuche: [1300, '2027-03-23'], halloween: [1200, 2900, 3800, 4600, '2027-10-30'], fasching: [1200, '2027-02-05'] };
(async () => { const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const fehler = [];
  for (const [id, liste] of Object.entries(F)) { const datum = typeof liste.at(-1) === 'string' ? liste.at(-1) : ''; const ts = liste.filter((x) => typeof x === 'number');
    for (const n of [0, 1]) { const p = await br.newPage({ viewport: { width: 400, height: 760 } }); p.on('pageerror', (e) => fehler.push(id + ': ' + e.message));
      await p.goto(`file://${Z}/entwurf/effekte.html?fx=${id}&nacht=${n}${datum ? '&datum=' + datum : ''}`); const t0 = Date.now(); const files = [];
      for (const [i, t] of ts.entries()) { const w = t - (Date.now() - t0); if (w > 0) await p.waitForTimeout(w); const f = `/tmp/n-${id}-${n}-${i}.png`; files.push(f); await p.screenshot({ path: f, clip: { x: 12, y: 50, width: 376, height: 560 } }); }
      execSync(`python3 /home/claude/arbeit/fx/kleben.py ${Z}/bilder/${id}-400-${n ? 'nacht' : 'tag'}.png ${files.join(' ')}`);
      if (n === 0) { await p.waitForTimeout(6000); if (!(await p.locator('.sticker').count())) fehler.push(id + ': kein Sticker'); } await p.close(); } }
  const p = await br.newPage({ viewport: { width: 1280, height: 900 } }); p.on('pageerror', (e) => fehler.push('panel: ' + e.message)); await p.goto(`file://${Z}/entwurf/effekte.html?fx=clip&datum=2026-12-01`); await p.waitForTimeout(3000);
  console.log(await p.locator('table').innerText()); await p.screenshot({ path: `${Z}/bilder/uebersicht-1280.png`, fullPage: true });
  console.log('Fehler', fehler); await br.close(); })();
