// Prüfrunde Erklär-Darstellung: echte Themen (inhalte/themen) in der Lernen-Ansicht „Erklären“ nachstellen und messen.
// Nutzt setup() aus tests/lernen.test.cjs unverändert; nur schule_einheit_lesen liefert hier das echte Thema.
// Start: PW_TEST_EXECUTABLE=/pfad/chrome node --test inhalte/pruefung/erklaerungen/darstellung/aufnahme.test.cjs
'use strict';
const { test } = require('node:test');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '../../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; } };', quelle);
const H = m.exports;
const AUS = path.join(__dirname, 'bilder'); const MESS = path.join(root, 'test-results/erklaerung'); fs.mkdirSync(MESS, { recursive: true });
const THEMEN = ['zahlen.ganz', 'messen.flaechen', 'zahlen.rechengesetze', 'geometrie.winkel', 'gleichungen.einfach', 'funktionen.linear', 'gleichungen.lgs2', 'bruch.brueche'];
const messung = {};
async function thema(page, k) {
  const d = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themen', k + '.json'), 'utf8'));
  const auf = (d.aufgaben || []).filter((a) => a.p === 'uebung');
  const ueb = d.inhalt.etappen.map((e, i) => auf.find((a) => a.l === e.lernziel)).filter(Boolean)
    .map((a, i) => ({ id: 1000 + i, lernziel: a.l, stufe: a.s, antworttyp: a.y, frage: a.f, antworten: a.a, tipp: a.h }));
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}');
    if (b.aktion !== 'schule_einheit_lesen') return route.fallback();
    route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, einheit_id: b.daten.einheit_id, status: 'geprueft', inhalt: d.inhalt, uebungen: ueb,
      stand: d.inhalt.etappen.map((x) => ({ lernziel: x.lernziel, pflicht: true, status: 'offen' })), etappen_stand: {}, laufender_test: null } }) });
  });
}
const warte = async (p) => { await p.waitForFunction(() => !document.querySelector('#main .spinner'), null, { timeout: 5000 }).catch(() => {}); await p.waitForTimeout(350); };
for (const k of THEMEN) {
  test('Erklären ' + k, async () => {
    const nach = []; const { page } = await H.setup({ after: (fn) => nach.push(fn) });
    await thema(page, k); const r = {};
    for (const [g, w, h] of [['handy', 390, 844], ['tablet', 820, 1180]]) {
      await page.setViewportSize({ width: w, height: h });
      await page.goto(H.origin + '/#/lerneinheit/1-1'); await warte(page);
      await page.screenshot({ path: path.join(AUS, `${k}-${g}-erklaeren-ganz.png`), fullPage: true });
      await page.screenshot({ path: path.join(AUS, `${k}-${g}-erklaeren-blick.png`) });
      r[g] = await page.evaluate(() => {
        const karten = [...document.querySelectorAll('.lr-panel:not([hidden]) .lr-lernkarte')];
        const zeile = (el) => { if (!el) return null; const s = getComputedStyle(el); return { px: parseFloat(s.fontSize), zeilenhoehe: s.lineHeight, breite: Math.round(el.getBoundingClientRect().width), zeichenJeZeile: Math.round(el.getBoundingClientRect().width / (parseFloat(s.fontSize) * 0.5)) }; };
        const ersteKarte = karten[0]; const teile = ersteKarte ? [...ersteKarte.querySelectorAll('.lr-einstieg, .lr-woerter, .lr-bild, svg, .lr-sogehts, .lr-merke, .lr-regel, .lr-fehler, .lr-probe, table')].map((x) => ({ teil: x.className?.baseVal ?? x.className, y: Math.round(x.getBoundingClientRect().top + scrollY), h: Math.round(x.getBoundingClientRect().height) })) : [];
        return { seitenhoehe: document.documentElement.scrollHeight, karten: karten.map((c) => ({ titel: c.querySelector('h3')?.textContent, h: Math.round(c.getBoundingClientRect().height), worte: c.innerText.split(/\s+/).length })),
          ersteKarte: teile, text: zeile(document.querySelector('.lr-lernkarte .lr-einstieg p:last-child, .lr-lernkarte .lr-regel')), schritt: zeile(document.querySelector('.lr-lernkarte .lr-sogehts li')),
          bildSchrift: (() => { const t = [...document.querySelectorAll('.lr-panel:not([hidden]) .lr-lernkarte svg text')].map((x) => parseFloat(getComputedStyle(x).fontSize) * (x.ownerSVGElement.getScreenCTM()?.a || 1)).filter((v) => v > 0).sort((a, b) => a - b); return t.length ? { min: Math.round(t[0] * 10) / 10, median: Math.round(t[Math.floor(t.length / 2)] * 10) / 10, n: t.length } : null; })(),
          fokusKnopfY: Math.round((document.querySelector('.lr-lernkarte .lr-dazu')?.getBoundingClientRect().top ?? -1) + scrollY) };
      });
    }
    // Üben mit eingeblendeter Kurz-Erklärung (erster Besuch) und Fehler-Reiter, Handy
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(H.origin + '/#/lerneinheit/1-1-ueben-1'); await warte(page);
    await page.screenshot({ path: path.join(AUS, `${k}-handy-ueben-ganz.png`), fullPage: true });
    r.ueben = await page.evaluate(() => { const f = document.querySelector('.lr-panel:not([hidden]) .lr-aufgabe, .lr-panel:not([hidden]) [class*="frage"]'); return { aufgabeY: f ? Math.round(f.getBoundingClientRect().top + scrollY) : null, seitenhoehe: document.documentElement.scrollHeight }; });
    await page.goto(H.origin + '/#/lerneinheit/1-1-fehler'); await warte(page);
    await page.screenshot({ path: path.join(AUS, `${k}-handy-fehler-ganz.png`), fullPage: true });
    messung[k] = r;
    for (const fn of nach.reverse()) { try { await fn(); } catch { /* Seitenfehler hier nicht bewertet */ } }
  });
}
test('Messung schreiben', () => fs.writeFileSync(path.join(MESS, 'messung.json'), JSON.stringify(messung, null, 1)));
