// Erzeugt die Entwurfsbilder ../bilder/stil-*.png aus index.html (lokales Chrome: PW_TEST_EXECUTABLE).
const { chromium } = require('playwright');
const path = require('node:path');
(async () => {
  const b = await chromium.launch({ headless: true, ...(process.env.PW_TEST_EXECUTABLE ? { executablePath: process.env.PW_TEST_EXECUTABLE } : {}) });
  const url = 'file://' + path.join(__dirname, 'index.html');
  const aus = (n) => path.join(__dirname, '..', 'bilder', n);
  for (const [w, h, ansicht, look, name] of [
    [390, 844, 'heute', 'ozean', 'stil-entwurf-heute-ozean-390.png'], [390, 844, 'heute', 'nacht', 'stil-entwurf-heute-nacht-390.png'],
    [390, 844, 'ueben', 'ozean', 'stil-entwurf-ueben-390.png'], [390, 844, 'richtig', 'ozean', 'stil-entwurf-richtig-390.png'],
    [390, 844, 'falsch', 'ozean', 'stil-entwurf-falsch-390.png'], [1280, 800, 'ueben', 'ozean', 'stil-entwurf-ueben-1280.png'], [820, 1180, 'heute', 'ozean', 'stil-entwurf-heute-820.png']]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, reducedMotion: 'reduce' });
    await p.goto(`${url}?ansicht=${ansicht}&look=${look}`); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
    await p.screenshot({ path: aus(name) }); await p.close();
  }
  await b.close();
})();
