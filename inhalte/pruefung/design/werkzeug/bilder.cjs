// Bilder je Richtung und Ansicht in Handy (390×844), Tablet (820×1180), Rechner (1280×800) + Kontrastprüfung.
// Aufruf: PW_TEST_EXECUTABLE=/pfad/chrome node inhalte/pruefung/design/werkzeug/bilder.cjs [richtung …]
const { chromium } = require('playwright'); const path = require('node:path'); const fs = require('node:fs');
const ZIEL = path.resolve(__dirname, '..');
const ZUSTAENDE = [
  ['heute', { ansicht: 'heute' }],
  ['erklaeren', { ansicht: 'thema', teil: 'erklaeren', schritt: 1 }],
  ['ueben', { ansicht: 'thema', teil: 'ueben', eingabe: '2000' }],
  ['richtig', { ansicht: 'thema', teil: 'ueben', eingabe: '2000' }, 'pruefen'],
  ['falsch', { ansicht: 'thema', teil: 'ueben', eingabe: '200' }, 'pruefen'],
  ['sitzt', { ansicht: 'thema', teil: 'ueben', eingabe: '2000', serie: { astellenwert: 1 } }, 'pruefen'],
  ['zahlenstrahl', { ansicht: 'thema', teil: 'ueben', karte: 1, strahl: 4 }],
  ['fehler', { ansicht: 'thema', teil: 'fehler' }],
  ['weltkarte', { ansicht: 'welt' }],
  ['reisepass', { ansicht: 'pass' }],
  ['eltern', { ansicht: 'eltern' }],
  ['heute-13', { kind: 'b', ansicht: 'heute' }],
  ['aufgabe-13', { kind: 'b', ansicht: 'thema', teil: 'ueben', eingabe: '-3' }],
  ['dunkel-heute', { ansicht: 'heute', dunkel: true }],
  ['dunkel-ueben', { ansicht: 'thema', teil: 'ueben', eingabe: '20', dunkel: true }],
];
const GERAETE = [['handy', 390, 844], ['tablet', 820, 1180], ['rechner', 1280, 800]];
const lum = `(c)=>{const m=c.match(/[\\d.]+/g).map(Number);const f=v=>{v/=255;return v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4};return {l:0.2126*f(m[0])+0.7152*f(m[1])+0.0722*f(m[2]),a:m[3]??1}}`;
async function kontrast(page) {
  return page.evaluate((lumSrc) => {
    const lum = eval(lumSrc); const out = [];
    const hinter = (e) => { for (let x = e; x; x = x.parentElement) { const s = getComputedStyle(x); if (s.backgroundImage !== 'none' && !s.backgroundImage.includes('linear-gradient(') && !s.backgroundImage.includes('radial-gradient(')) return null; const c = lum(s.backgroundColor); if (c.a > 0.9) return s.backgroundColor; } return getComputedStyle(document.body).backgroundColor; };
    for (const e of document.querySelectorAll('body *')) {
      if (!e.childNodes.length || ![...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) continue;
      const r = e.getBoundingClientRect(); const s = getComputedStyle(e); if (!r.width || s.visibility === 'hidden' || e.closest('[hidden],[aria-hidden="true"]')) continue;
      if (e.closest('svg')) continue;
      const bg = hinter(e); if (!bg || !s.color.startsWith('rgb')) continue;
      const v = lum(s.color), h = lum(bg); const k = (Math.max(v.l, h.l) + 0.05) / (Math.min(v.l, h.l) + 0.05);
      const px = parseFloat(s.fontSize);
      if (k < 4.5 || px < 16) out.push({ text: e.textContent.trim().slice(0, 40), k: Math.round(k * 100) / 100, px, farbe: s.color, hinter: bg });
    }
    const klein = [...document.querySelectorAll('button, a, [role=slider], [tabindex="0"]')].filter((b) => { const r = b.getBoundingClientRect(); return r.width && r.height && (r.width < 44 || r.height < 44) && !b.closest('[hidden]'); })
      .map((b) => ({ name: (b.getAttribute('aria-label') || b.textContent).trim().slice(0, 30), w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height) }));
    return { kontrast: out, klein, quer: document.documentElement.scrollWidth > innerWidth };
  }, lum);
}
(async () => {
  const richtungen = process.argv.slice(2).length ? process.argv.slice(2) : ['heft', 'abflug', 'linien'];
  const b = await chromium.launch({ headless: true, ...(process.env.PW_TEST_EXECUTABLE ? { executablePath: process.env.PW_TEST_EXECUTABLE } : {}) });
  for (const r of richtungen) {
    const url = 'file://' + path.join(ZIEL, r, 'entwurf.html'); const bericht = {}; const fehler = [];
    for (const [g, w, h] of GERAETE) {
      const p = await b.newPage({ viewport: { width: w, height: h }, reducedMotion: 'reduce', colorScheme: 'light' });
      p.on('pageerror', (e) => fehler.push(`${g}: ${e.message}`));
      for (let [n, z, akt] of ZUSTAENDE) {
        if (r === 'abflug' && n.startsWith('dunkel-')) { n = n.replace('dunkel-', 'hell-'); z = { ...z, dunkel: false }; }
        await p.goto(url); await p.evaluate(() => document.fonts.ready);
        await p.evaluate(([z, akt]) => { window.ENTWURF.setze(z); if (akt) window.ENTWURF.A[akt](); }, [z, akt]);
        await p.waitForTimeout(120);
        await p.screenshot({ path: path.join(ZIEL, r, `${g}-${n}.png`) });
        bericht[`${g}-${n}`] = await kontrast(p);
      }
      await p.close();
    }
    fs.writeFileSync(path.join(__dirname, `pruefung-${r}.json`), JSON.stringify({ fehler, bericht }, null, 1));
    const k = Object.entries(bericht).flatMap(([n, x]) => x.kontrast.map((y) => n + ': ' + JSON.stringify(y)));
    const kl = [...new Set(Object.values(bericht).flatMap((x) => x.klein.map((y) => JSON.stringify(y))))];
    console.log(r, 'Fehler:', fehler.length, fehler.slice(0, 3), '| Kontrast/Größe:', k.length, k.slice(0, 8), '| klein:', kl.slice(0, 8), '| quer:', Object.entries(bericht).filter(([, x]) => x.quer).map(([n]) => n));
  }
  await b.close();
})();
