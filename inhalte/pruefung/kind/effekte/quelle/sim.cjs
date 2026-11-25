const { chromium } = require('/home/claude/wt/node_modules/playwright');
(async () => { const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const p = await br.newPage({ viewport: { width: 1280, height: 900 } }); const f = []; p.on('pageerror', (e) => f.push(e.message));
 for (const d of ['2026-12-20', '2027-03-20']) { await p.goto(`file:///home/claude/ki-system/inhalte/pruefung/kind/effekte/entwurf/effekte.html?fx=clip&datum=${d}`); await p.waitForTimeout(1500); console.log((await p.locator('table').innerText()).split('\n').slice(0, 13).join('\n')); }
 await p.screenshot({ path: '/home/claude/ki-system/inhalte/pruefung/kind/effekte/bilder/uebersicht-1280.png', fullPage: true }); console.log('Fehler', f); await br.close(); })();
