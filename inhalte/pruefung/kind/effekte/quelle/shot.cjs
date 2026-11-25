const { chromium } = require('/home/claude/wt/node_modules/playwright');
const Z = '/home/claude/ki-system/inhalte/pruefung/kind/effekte';
const T = { tresor: 1500, hacker: 1750, f404: 1450, glitch: 1500, taube: 1300, moewe: 1180, turbulenz: 1500, comeback: 900, kaffee: 1250, koffer: 1950, gewitter: 1150 };
(async () => {
  const br = await chromium.launch({ executablePath: '/usr/bin/google-chrome' }); const fehler = [];
  const shot = async (b, hgt, q, t, name) => { const p = await br.newPage({ viewport: { width: b, height: hgt } }); p.on('pageerror', (e) => fehler.push(name + ': ' + e.message));
    await p.goto('file://' + Z + '/entwurf/effekte.html?' + q); await p.waitForTimeout(t); await p.screenshot({ path: `${Z}/bilder/${name}.png` }); await p.close(); };
  for (const [id, t] of Object.entries(T)) for (const n of [0, 1]) await shot(400, 760, `fx=${id}&nacht=${n}`, t, `${id}-400-${n ? 'nacht' : 'tag'}`);
  for (const id of Object.keys(T)) await shot(400, 760, `fx=${id}`, 6500, `${id}-400-ende`);
  for (const n of [0, 1]) { await shot(820, 1100, `fx=tresor&nacht=${n}`, 1500, `tresor-820-${n ? 'nacht' : 'tag'}`); await shot(820, 1100, `fx=f404&nacht=${n}`, 1450, `f404-820-${n ? 'nacht' : 'tag'}`); }
  await shot(400, 760, 'fx=f404&ruhig=1', 1200, 'f404-400-ruhig');
  console.log('Fehler:', fehler); await br.close();
})();
