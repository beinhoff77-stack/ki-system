// Bilder des Entwurfs + Prüfung: Hauptknopf ohne Scrollen sichtbar? Text ≥ 16 px (auch in Zeichnungen)?
// Aufruf: PW_TEST_EXECUTABLE=/pfad/chrome node inhalte/pruefung/erklaerungen/darstellung/werkzeug/bilder.cjs
const { chromium } = require('playwright'); const path = require('node:path');
const url = 'file://' + path.resolve(__dirname, '../entwurf.html'); const AUS = path.resolve(__dirname, '../bilder');
const Z = [
  ['kl5-karte1-situation', 'zahlen.ganz', { karte: 0, phase: 0 }], ['kl5-karte1-wort', 'zahlen.ganz', { karte: 0, phase: 0, wort: 'negative Zahl' }],
  ['kl5-karte1-schritt1', 'zahlen.ganz', { karte: 0, phase: 1 }], ['kl5-karte1-schritt3', 'zahlen.ganz', { karte: 0, phase: 3 }],
  ['kl5-karte1-merke', 'zahlen.ganz', { karte: 0, phase: 5, falle: true }], ['kl5-karte4-schritt2', 'zahlen.ganz', { karte: 3, phase: 2 }],
  ['kl5-karte4-schritt4', 'zahlen.ganz', { karte: 3, phase: 4 }], ['kl5-kartenliste', 'zahlen.ganz', { karte: 0, phase: 0, liste: true }],
  ['kl5-ueben', 'zahlen.ganz', { karte: 0, teil: 'ueben' }], ['kl6-bruch-schritt2', 'bruch.brueche', { karte: 0, phase: 2 }],
  ['kl8-kurz', 'funktionen.linear', { karte: 0, phase: 0 }], ['kl8-schritt3', 'funktionen.linear', { karte: 0, phase: 3 }],
];
(async () => {
  const b = await chromium.launch({ headless: true, ...(process.env.PW_TEST_EXECUTABLE ? { executablePath: process.env.PW_TEST_EXECUTABLE } : {}) });
  const fehler = [];
  for (const [g, w, h] of [['handy', 390, 844], ['tablet', 820, 1180]]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, reducedMotion: 'reduce' }); p.on('pageerror', (e) => fehler.push(e.message));
    for (const [n, thema, z] of Z) {
      await p.goto(url); await p.evaluate(([t, z]) => { document.querySelector(`[data-thema="${t}"]`).click(); window.ENTWURF.setze(z); }, [thema, z]);
      await p.screenshot({ path: path.join(AUS, `entwurf-${n}-${g}.png`) });
      const m = await p.evaluate(() => { const k = document.querySelector('.haupt'); const r = k?.getBoundingClientRect();
        const t = [...document.querySelectorAll('svg text')].map((x) => parseFloat(getComputedStyle(x).fontSize) * (x.ownerSVGElement.getScreenCTM()?.a || 1));
        const html = [...document.querySelectorAll('.app *')].filter((e) => [...e.childNodes].some((c) => c.nodeType === 3 && c.textContent.trim()) && !e.closest('svg')).map((e) => parseFloat(getComputedStyle(e).fontSize));
        return { knopfSichtbar: r ? r.bottom <= innerHeight : null, seite: document.documentElement.scrollHeight, bildMin: t.length ? Math.min(...t).toFixed(1) : null, textMin: Math.min(...html) }; });
      console.log(g, n, JSON.stringify(m));
    }
    await p.close();
  }
  console.log('Seitenfehler:', fehler); await b.close();
})();
