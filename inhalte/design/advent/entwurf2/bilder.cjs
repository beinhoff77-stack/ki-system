// Bildschirmfotos von Entwurf 2: node inhalte/design/advent/entwurf2/bilder.cjs [filter] [ordner]
// Playwright aus dem Haupt-Checkout, lokales Chromium. Ohne Netz.
const path = require('path');
const { chromium } = require(process.env.PW || '/home/claude/ki-system/node_modules/playwright');
const hier = __dirname;
const datei = (d) => 'file://' + path.join(hier, '..', d, 'index.html');
// [Name, Adresse, Breiten, Höhe (0 = ganze Seite)]
const FAELLE = [
  ['karte-v4', 's=karte&v=4', [390, 1280], 844], ['karte-v5', 's=karte&v=5', [390, 1280], 844],
  ['karte-v4-tag6', 's=karte&v=4&tag=6', [390], 844], ['karte-v4-tag24', 's=karte&v=4&tag=24', [390], 844], ['karte-v4-tag31', 's=karte&v=4&tag=31', [390], 844],
  ['karte-v4-freizonen', 's=karte&v=4&frei=1', [390], 844],
  ['tuer', 's=tuer', [390, 820], 844], ['tuer-krampus', 's=tuer-krampus', [390], 844], ['tuer6', 's=tuer&tag=6', [390], 844], ['tuer24', 's=tuer&tag=24', [390], 844], ['tuer-auf', 's=tuer&auf=1', [390], 844],
  ['zweite', 's=zweite', [390], 844],
  ['inhalt-geschenk', 's=inhalt-geschenk', [390], 844], ['inhalt-bild', 's=inhalt-bild', [390], 844], ['inhalt-krampus', 's=inhalt-krampus', [390], 844], ['inhalt-jackpot', 's=inhalt-jackpot', [390], 844],
  ['inhalt-niete', 's=inhalt-niete', [390], 844], ['inhalt-sterne', 's=inhalt-sterne', [390], 844], ['inhalt-karte6', 's=inhalt-karte6', [390], 844], ['inhalt-karte24', 's=inhalt-karte24', [390], 844], ['leer', 's=leer', [390], 844],
  ['kalender', 's=kalender', [390, 1280], 0], ['kalender-bereit', 's=kalender-bereit', [390], 0], ['kalender-tuer', 's=kalender-tuer', [390], 844], ['limit', 's=limit', [390], 0], ['nach24', 's=nach24&tag=26', [390], 0], ['vor1', 's=vor1', [390], 0],
  ['gutscheine', 's=gutscheine', [390, 1280], 0], ['motive', 's=motive', [390, 1280], 0], ['eltern', 's=eltern', [390], 0],
];
(async () => {
  const filter = process.argv[2] ? new RegExp(process.argv[2]) : null; const ordner = process.argv[3] || 'entwurf2';
  const ziel = path.join(hier, 'bilder'); const b = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome' });
  for (const [name, hash, breiten, hoehe] of FAELLE) for (const w of breiten) for (const g of ['hell', 'dunkel']) {
    if (w === 820 && g === 'dunkel') continue;
    const datei2 = `${name}-${w}-${g}.png`; if (filter && !filter.test(datei2)) continue;
    const h = w === 1280 && name.startsWith('karte') ? 800 : hoehe || 900;
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: process.env.DSF ? Number(process.env.DSF) : 1 });
    await p.goto(datei(ordner) + '#' + hash + '&foto=1' + (g === 'dunkel' ? '&g=nacht' : ''));
    await p.waitForTimeout(250);
    await p.screenshot({ path: path.join(process.env.ZIEL || ziel, datei2), fullPage: !hoehe });
    await p.close(); console.log(datei2);
  }
  await b.close();
})();
