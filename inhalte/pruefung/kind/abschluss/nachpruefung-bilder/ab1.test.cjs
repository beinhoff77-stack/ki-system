'use strict';
const nt = require('node:test'); const assert = require('node:assert');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); let text = fs.readFileSync(quelle, 'utf8');
text = text.replace("const { test, before, after } = require('node:test');", "const test = () => {}; const { before, after } = require('node:test');");
text += '\nmodule.exports = { setup, abLande, abTest, abFlug, mitBonus, get origin() { return origin; } };';
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle)); m._compile(text, quelle);
const H = m.exports; const AUS = path.join(__dirname, 'bilder'); fs.mkdirSync(AUS, { recursive: true });
const R = {};
nt.test('Boarding schließt die Ansicht', async (t) => {
  const zeiten = [];
  for (let i = 0; i < 8; i++) {
    const { page } = await H.abTest(t, {}, { gestaltung: 'nacht' });
    await page.locator('.lr-abschluss-flug').getByRole('button', { name: /Weiter zum nächsten Thema/ }).click();
    const k = page.locator('.lr-abschluss-bordkarte'); await k.waitFor();
    await k.locator('.lr-ab-gross').click(); await page.waitForURL(/1-2-erklaeren-1$/);
    const t0 = Date.now(); let n = await page.locator('.lr-abschluss').count();
    while (n && Date.now() - t0 < 3000) { await page.waitForTimeout(50); n = await page.locator('.lr-abschluss').count(); }
    zeiten.push(n ? 'bleibt' : Date.now() - t0);
    if (i === 0) await page.screenshot({ path: path.join(AUS, 'boarding-danach-400.png') });
    await page.close();
  }
  R.boarding = zeiten;
});
nt.test('Wortbrüche/Texte Abschluss', async (t) => {
  const brueche = async (page) => page.evaluate(() => { const out = []; const w = document.createTreeWalker(document.querySelector('.lr-abschluss'), NodeFilter.SHOW_TEXT);
    let n; while ((n = w.nextNode())) { const re = /\S+/g; let mm; while ((mm = re.exec(n.data))) { const r = document.createRange(); r.setStart(n, mm.index); r.setEnd(n, mm.index + mm[0].length);
      const rs = [...r.getClientRects()].filter((x) => x.width > 0); if (new Set(rs.map((x) => Math.round(x.top))).size > 1) out.push(mm[0]); } } return out; });
  R.texte = {};
  for (const art of ['direkt', 'sauber', 'sturm']) for (const [b, h] of [[400, 780], [360, 640]]) {
    const { page } = await H.abLande(t, art, { gestaltung: 'tag', breite: b, hoehe: h, x: art === 'sturm' ? { bordkarten: 15, fehler_endgueltig: 6, stufe_gesenkt: 2 } : art === 'sauber' ? { bordkarten: 8, eigene_loesungen: 6 } : { bordkarten: 2 } });
    const v = page.locator('.lr-abschluss-etappe');
    R.texte[art + b] = { text: (await page.locator('.lr-abschluss').innerText()).replace(/\s+/g, ' '), brueche: await brueche(page),
      passt: await page.evaluate(() => { const a = document.querySelector('.lr-ab-app'); const g = document.querySelector('.lr-ab-gross').getBoundingClientRect(); return { scroll: a.scrollHeight > a.clientHeight + 1, knopfUnten: Math.round(g.bottom), h: innerHeight }; }) };
    await page.screenshot({ path: path.join(AUS, `etappe-${art}-tag-${b}.png`) });
    await page.close();
  }
  fs.writeFileSync(path.join(__dirname, 'mess.json'), JSON.stringify(R, null, 1));
});
