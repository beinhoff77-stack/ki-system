// Prüfrunde Gestaltung: Bilder des Ist-Zustands (Stand lernen-app) mit den Testdaten aus tests/lernen.test.cjs.
// Start: PW_TEST_EXECUTABLE=/pfad/zu/chrome node --test inhalte/pruefung/design/ist/aufnahme.test.cjs
'use strict';
const { test } = require('node:test');
const Module = require('node:module');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs');
const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; } };', quelle);
const H = m.exports;
const ANSICHTEN = [['heute', 'reise/1'], ['heute-nacht', 'reise/2'], ['thema-erklaeren', 'lerneinheit/1-1'], ['thema-ueben', 'lerneinheit/1-1-ueben-1'],
  ['thema-fehler', 'lerneinheit/1-1-fehler'], ['weg', 'weg/1'], ['weltkarte', 'weltkarte/1'], ['reisepass', 'reisepass/1'], ['merkheft', 'merkheft/1'],
  ['eltern-uebersicht', 'lernen'], ['eltern-lernstand', 'lernstand/1'], ['eltern-lehrplan', 'lehrplan'], ['eltern-plan', 'plan/1']];
for (const [w, h, g] of [[390, 844, 'handy'], [820, 1180, 'tablet'], [1280, 800, 'rechner']]) {
  test('Ist-Zustand ' + g, async () => {
    const nach = []; const { page } = await H.setup({ after: (fn) => nach.push(fn) });
    await page.setViewportSize({ width: w, height: h });
    for (const [n, a] of ANSICHTEN) {
      await page.goto(H.origin + '/#/' + a);
      await page.waitForFunction(() => !document.querySelector('#main .spinner'), null, { timeout: 5000 }).catch(() => {});
      await page.waitForTimeout(300);
      await page.screenshot({ path: path.join(__dirname, `${g}-${n}.png`) });
      if (g === 'handy') await page.screenshot({ path: path.join(__dirname, `${g}-${n}-ganz.png`), fullPage: true });
    }
    // Aufgabe falsch beantwortet (Handy-Sicht nach dem Prüfen)
    await page.goto(H.origin + '/#/lerneinheit/1-1-ueben-1'); await page.waitForTimeout(400);
    await page.getByRole('textbox', { name: 'Antwort' }).fill('200'); await page.getByRole('textbox', { name: 'Antwort' }).press('Enter');
    await page.waitForTimeout(600);
    await page.screenshot({ path: path.join(__dirname, `${g}-aufgabe-falsch.png`) });
    for (const fn of nach.reverse()) { try { await fn(); } catch { /* Seitenfehler werden hier nicht bewertet */ } }
  });
}
