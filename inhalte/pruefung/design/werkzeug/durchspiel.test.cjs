// Durchspielen jeder Richtung per Klick (wie ein Kind): Heute → Thema → Erklären → Üben → falsch → richtig → richtig → „Lernkarte sitzt“,
// Zahlenstrahl ziehen, Weltkarte, Reisepass, Eltern-Übersicht. Start: PW_TEST_EXECUTABLE=… node --test inhalte/pruefung/design/werkzeug/durchspiel.test.cjs
const { test } = require('node:test'); const assert = require('node:assert/strict');
const { chromium } = require('playwright'); const path = require('node:path');
const ZIEL = path.resolve(__dirname, '..');
const NAV = { heft: async (p, v) => p.click(`.register [data-akt="geh"][data-arg="${v}"]`),
  abflug: async (p, v) => { await p.click('[data-akt="zeigen"][data-arg="menue"]'); await p.click(`.blatt [data-akt="geh"][data-arg="${v}"]`); },
  linien: async (p, v) => { if (v === 'eltern') { await p.click('[data-akt="zeigen"][data-arg="menue"]'); await p.click('.menue [data-akt="geh"][data-arg="eltern"]'); } else await p.click(`.rechts [data-akt="geh"][data-arg="${v}"]`); } };
const sichtbar = (p, sel) => p.locator(sel).locator('visible=true').first();
async function tippe(p, r, zahl) { for (const d of zahl) await sichtbar(p, `[data-akt="${r === 'linien' ? 'ziffer' : 'taste'}"][data-arg="${d}"]`).click(); await sichtbar(p, '[data-akt="pruefen"]').click(); }
for (const r of ['heft', 'abflug', 'linien']) for (const [w, h] of [[390, 844], [1280, 800]]) {
  test(`${r} ${w} px durchspielen`, async () => {
    const b = await chromium.launch({ headless: true, ...(process.env.PW_TEST_EXECUTABLE ? { executablePath: process.env.PW_TEST_EXECUTABLE } : {}) });
    const p = await b.newPage({ viewport: { width: w, height: h }, reducedMotion: 'reduce' }); p.setDefaultTimeout(4000); const fehler = []; p.on('pageerror', (e) => fehler.push(e.message));
    try {
    await p.goto('file://' + path.join(ZIEL, r, 'entwurf.html'));
    if (r === 'abflug') { await sichtbar(p, '[data-akt="zeigen"][data-arg="menue"]').click(); await sichtbar(p, '.blatt [data-akt="dunkel"]').click(); await p.click('.schleier').catch(() => {}); }
    await sichtbar(p, 'main [data-fokus="los"], .einsteigen').click();                      // Heute → Thema
    const S = () => p.evaluate(() => ({ ...window.ENTWURF.S }));
    assert.equal((await S()).ansicht, 'thema');
    for (let i = 0; i < 3; i++) await sichtbar(p, '[data-akt="schritt"]').click();          // Erklärung Schritt für Schritt
    assert.equal((await S()).schritt, 3);
    if (w < 820) await sichtbar(p, '[data-akt="teil"][data-arg="ueben"]').click();
    await tippe(p, r, '200'); assert.equal((await S()).ergebnis, 'falsch');                 // falsch
    await sichtbar(p, '[data-akt="weiter"]').click();
    await tippe(p, r, '70000'); assert.equal((await S()).ergebnis, 'richtig');              // richtig
    await sichtbar(p, '[data-akt="weiter"]').click();
    await tippe(p, r, '500000'); const s = await S(); assert.equal(s.ergebnis, 'richtig'); assert.equal(s.neuSitzt, true);   // Lernkarte sitzt
    await sichtbar(p, '[data-akt="lernkarte"], [data-akt="naechsteKarte"], [data-akt="halt"]').click();                   // nächste Karte: Zahlenstrahl
    if ((await S()).teil === 'erklaeren' && w < 820) await sichtbar(p, '[data-akt="teil"][data-arg="ueben"]').click();
    const svg = sichtbar(p, 'svg[data-strahl]'); const bx = await svg.boundingBox();
    const vb = await svg.evaluate((e) => e.viewBox.baseVal.width); const x4 = bx.x + (22 + (vb - 44) * 4 / 8) / vb * bx.width;
    await p.mouse.move(bx.x + 10, bx.y + bx.height / 2); await p.mouse.down(); await p.mouse.move(x4, bx.y + bx.height / 2, { steps: 6 }); await p.mouse.up();
    assert.equal((await S()).strahl, 4);
    await sichtbar(p, '[data-akt="pruefen"]').click(); assert.equal((await S()).ergebnis, 'richtig');
    // Weltkarte, Reisepass, Eltern
    if (r === 'heft') { if (!(await p.locator('.register').count())) await sichtbar(p, '[aria-label="Zu Heute"]').click(); await sichtbar(p, '.register [data-arg="welt"]').click(); } else if (r === 'abflug') { await sichtbar(p, '[data-akt="geh"][data-arg="heute"]').click(); await NAV.abflug(p, 'welt'); } else await NAV.linien(p, 'welt');
    assert.equal((await S()).ansicht, 'welt');
    await NAV[r](p, 'pass'); assert.equal((await S()).ansicht, 'pass');
    if (r === 'heft') { await p.click('.wer'); await p.click('.menue [data-akt="geh"][data-arg="eltern"]'); } else await NAV[r](p, 'eltern');
    assert.equal((await S()).ansicht, 'eltern'); await p.getByText('Wartet auf dich').waitFor();
    assert.deepEqual(fehler, []);
    } finally { await b.close(); }
  });
}
