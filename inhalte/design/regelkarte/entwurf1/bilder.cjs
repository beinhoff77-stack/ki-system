// Bildschirmfotos des Entwurfs: node inhalte/design/regelkarte/entwurf1/bilder.cjs (Playwright aus dem Haupt-Checkout, lokales Chromium)
const path = require('path');
const { chromium } = require(process.env.PW || '/home/claude/ki-system/node_modules/playwright');
const hier = __dirname, datei = 'file://' + path.join(hier, 'index.html');
const faelle = [
  ['01-erst-minus', 'z=erst&r=minus'], ['02-end-minus', 'z=end&r=minus'], ['03-ohne-minus', 'z=ohne&r=minus'],
  ['04-erst-stellenwert', 'z=erst&r=stellenwert'], ['05-end-stellenwert', 'z=end&r=stellenwert'],
  ['06-end-waage-abweichend', 'z=end&r=waage'], ['07-end-prozent-ohne-bild', 'z=end&r=prozent'],
  ['08-checkin', 'z=checkin&r=minus'], ['09-misch', 'z=misch&r=stellenwert'], ['10-knobel', 'z=knobel&r=prozent'],
  ['11-test-ergebnis', 'z=test&auf=1'], ['12-regel-seite', 'z=regel&r=minus&von=erst'], ['13-erst-bild-offen', 'z=erst&r=minus&bild=auf'],
];
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome' });
  const breiten = process.argv[2] ? process.argv[2].split(',').map(Number) : [390, 820, 1280];
  for (const [name, hash] of faelle) for (const g of ['hell', 'dunkel']) for (const w of breiten) {
    if (w === 820 && g === 'dunkel') continue;
    if (w === 1280 && !/^(02|05|06|11)/.test(name)) continue;
    if (w === 820 && !/^(02|11|12)/.test(name)) continue;
    const p = await b.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1 });
    await p.goto(datei + '#' + hash + '&foto' + (g === 'dunkel' ? '&g=nacht' : ''));
    await p.waitForTimeout(150);
    await p.screenshot({ path: path.join(hier, 'bilder', `${name}-${w}-${g}.png`), fullPage: true });
    await p.close();
  }
  await b.close();
})();
