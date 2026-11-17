'use strict';
// Nachprüfung N1/N8: echte Etappen in der Abflug-Gestaltung rendern (Mock aus tests/lernen.test.cjs)
const { test } = require('node:test'); const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = process.env.REPO; const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; } };', quelle);
const H = m.exports; const AUS = process.env.AUS; fs.mkdirSync(AUS, { recursive: true });
const FAELLE = JSON.parse(process.env.FAELLE); const ERG = {};
for (const [name, datei, titel, breite, g] of FAELLE) test(name, async (t) => {
  const et = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themen', datei), 'utf8')).inhalt.etappen.find((e) => e.titel.includes(titel));
  const { page } = await H.setup(t, { gestaltung: g || 'tag' }); await page.setViewportSize({ width: breite, height: 900 });
  await page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion !== 'schule_einheit_lesen') return route.fallback();
    return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, einheit_id: 1, status: 'geprueft', inhalt: { ziel: 'Test', etappen: [et] }, uebungen: [], stand: [{ lernziel: et.lernziel, pflicht: true, status: 'offen' }], etappen_stand: {}, laufender_test: null } }) }); });
  await page.goto(H.origin + '/#/lerneinheit/1-1-erklaeren-1'); await page.locator('.lr-erklaert').waitFor(); await page.waitForTimeout(300);
  ERG[name] = { hoehe: await page.evaluate(() => document.documentElement.scrollHeight), titel: et.titel, bilder: await page.locator('.lr-erklaert .lr-bild').count(), neu: await page.locator('.lr-sogehts .neu').count(), mitNeu: await page.locator('.lr-sogehts .mit-neu').count() };
  await page.screenshot({ path: path.join(AUS, name + '.png'), fullPage: true });
});
test('ende', () => fs.writeFileSync(path.join(AUS, 'messung.json'), JSON.stringify(ERG, null, 1)));
