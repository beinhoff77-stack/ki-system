const { chromium } = require('/home/claude/wt/node_modules/playwright');
const Z = '/home/claude/ki-system/inhalte/pruefung/kind/effekte';
const F = { legendary: [1200, 2400, 3300, 5200], respawn: [900, 1700, 2600, 3600], hacker: [1500, 3800, 5600, 8200], absturz: [1300, 2800, 4600, 6400, 10200], rec: [1500, 3000, 4800, 5600], schatten: [1300, 2400, 3500, 4600],
  mission: [1600, 2600, 3600], iq: [1200, 2200, 3000], clutch: [1200, 2300, 3000], survived: [1300, 2400, 3600], eis: [1200, 2700, 3500, 4600],
  glitch: [1500], achievement: [1000], hitmarker: [1400], krit: [900], split: [1000], nitro: [1200], opa: [1400, 2900, 3700, 4900], unbekannt: [1500, 2700], lag: [1300], drift: [1100] };
const { execSync } = require('child_process');
(async () => { const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const fehler = [];
  for (const [id, ts] of Object.entries(F)) for (const [b, hh, n] of [[400, 760, 0], [400, 760, 1]].concat(['legendary', 'absturz', 'rec'].includes(id) ? [[820, 1100, 0]] : [])) {
    const p = await br.newPage({ viewport: { width: b, height: hh } }); p.on('pageerror', (e) => fehler.push(id + ': ' + e.message));
    await p.goto(`file://${Z}/entwurf/effekte.html?fx=${id}&nacht=${n}`); const t0 = Date.now(); const files = [];
    for (const [i, t] of ts.entries()) { const w = t - (Date.now() - t0); if (w > 0) await p.waitForTimeout(w); const f = `/tmp/a-${id}-${b}-${n}-${i}.png`; files.push(f); await p.screenshot({ path: f, clip: { x: 12, y: 50, width: b >= 760 ? 420 : 376, height: 560 } }); }
    execSync(`python3 /home/claude/arbeit/fx/kleben.py ${Z}/bilder/${id}-${b}-${n ? 'nacht' : 'tag'}.png ${files.join(' ')}`);
    await p.close(); }
  const p = await br.newPage({ viewport: { width: 1280, height: 900 } }); await p.goto(`file://${Z}/entwurf/effekte.html?fx=legendary`); await p.waitForTimeout(4500); await p.screenshot({ path: `${Z}/bilder/uebersicht-1280.png`, fullPage: true });
  await p.goto(`file://${Z}/entwurf/effekte.html?fx=rec&ruhig=1`); await p.waitForTimeout(1300); await p.screenshot({ path: `${Z}/bilder/rec-400-ruhig.png`, clip: { x: 12, y: 50, width: 420, height: 560 } });
  console.log('Fehler', fehler); await br.close(); })();
