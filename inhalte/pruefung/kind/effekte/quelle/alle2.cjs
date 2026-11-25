const { chromium } = require('/home/claude/wt/node_modules/playwright');
const Z = '/home/claude/ki-system/inhalte/pruefung/kind/effekte';
const F = { legendary: [1200, 2400, 3300, 5200], rec: [1500, 3000, 4800, 5600] };
const { execSync } = require('child_process');
(async () => { const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const fehler = [];
  for (const [id, ts] of Object.entries(F)) for (const [b, hh, n] of [[400, 760, 0], [400, 760, 1]].concat(['legendary', 'absturz', 'rec'].includes(id) ? [[820, 1100, 0]] : [])) {
    const p = await br.newPage({ viewport: { width: b, height: hh } }); p.on('pageerror', (e) => fehler.push(id + ': ' + e.message));
    await p.goto(`file://${Z}/entwurf/effekte.html?fx=${id}&nacht=${n}`); const t0 = Date.now(); const files = [];
    for (const [i, t] of ts.entries()) { const w = t - (Date.now() - t0); if (w > 0) await p.waitForTimeout(w); const f = `/tmp/a-${id}-${b}-${n}-${i}.png`; files.push(f); await p.screenshot({ path: f, clip: { x: 12, y: 50, width: b >= 760 ? 420 : 376, height: 560 } }); }
    execSync(`python3 /home/claude/arbeit/fx/kleben.py ${Z}/bilder/${id}-${b}-${n ? 'nacht' : 'tag'}.png ${files.join(' ')}`);
    await p.close(); }
  console.log('Fehler', fehler); await br.close(); })();
