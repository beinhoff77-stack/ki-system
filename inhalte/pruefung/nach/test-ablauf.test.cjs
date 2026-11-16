// Nachprüfung: Test-Ablauf (Flug-Test) und Etappe auf Tablet/dunkel – Mock aus tests/lernen.test.cjs unverändert.
'use strict';
const { test } = require('node:test');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; } };', quelle);
const H = m.exports; const AUS = path.join(__dirname, 'bilder'); fs.mkdirSync(AUS, { recursive: true });
const warte = async (p, ms = 400) => { await p.waitForFunction(() => !document.querySelector('#main .spinner'), null, { timeout: 6000 }).catch(() => {}); await p.waitForTimeout(ms); };
const TEXTE = {};
for (const g of ['tag', 'nacht']) test('Test-Ablauf ' + g, async () => {
  const nach = []; const { page: p } = await H.setup({ after: (f) => nach.push(f) }, { gestaltung: g });
  try {
    await p.goto(H.origin + '/#/lerneinheit/1-1-test'); await warte(p);
    await p.screenshot({ path: path.join(AUS, `test-${g}-1-start.png`), fullPage: true }); TEXTE[g + '-start'] = await p.locator('#main').innerText();
    const s = p.getByRole('button', { name: /starten/ }).first(); if (await s.count()) { await s.click(); await warte(p); }
    await p.screenshot({ path: path.join(AUS, `test-${g}-2-frage.png`), fullPage: true }); TEXTE[g + '-frage'] = await p.locator('#main').innerText();
    // erste Frage beantworten (Auswahl), dann abgeben
    const opt = p.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig'); if (await opt.count()) await opt.first().click();
    for (const n of ['Weiter', 'Speichern', 'Nächste']) { const b = p.getByRole('button', { name: new RegExp(n) }).first(); if (await b.count()) { await b.click(); await p.waitForTimeout(300); break; } }
    const ab = p.getByRole('button', { name: /[Aa]bgeben/ }).first(); if (await ab.count()) { await ab.click(); await p.waitForTimeout(300); const ja = p.getByRole('button', { name: /[Aa]bgeben|Ja/ }).last(); if (await ja.count()) await ja.click(); await warte(p, 600); }
    const tr = p.getByRole('button', { name: 'Trotzdem abgeben' }); if (await tr.count()) { await tr.click(); await warte(p, 700); }
    await p.screenshot({ path: path.join(AUS, `test-${g}-3-ergebnis.png`), fullPage: true }); TEXTE[g + '-ergebnis'] = await p.locator('#main').innerText();
  } finally { for (const f of nach.reverse()) { try { await f(); } catch { /* egal */ } } }
});
test('Texte', () => fs.writeFileSync(path.join(__dirname, 'test-texte.json'), JSON.stringify(TEXTE, null, 1)));
