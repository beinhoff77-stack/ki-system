// Prüfrunde App (W150, Abschnitt 4): Klick-Durchlauf aller Lernen-Ansichten als Kind und als Eltern/Lehrer,
// in 390 / 820 / 1280 px, hell und dunkel. Nutzt den lokalen Server und `setup` aus tests/lernen.test.cjs
// unverändert (die Datei wird bis zum ersten test(...) geladen). Zusätzlich nachgestellt: Wiederholen, Zugänge,
// leerer Zustand, Inhalt ohne Lernkarten und Server-Fehler.
// Start: PW_TEST_EXECUTABLE=/pfad/zu/chrome node --test inhalte/pruefung/app/durchlauf.test.cjs
// Ergebnis: test-results/durchlauf/*.png (alle Bilder) und test-results/durchlauf/messung.json (Messwerte).
'use strict';
const { test } = require('node:test');
const Module = require('node:module');
const fs = require('node:fs');
const path = require('node:path');

const root = path.resolve(__dirname, '../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs');
function ladeHelfer() {
  const text = fs.readFileSync(quelle, 'utf8');
  const kopf = text.slice(0, text.indexOf("\ntest('"));
  const m = new Module(quelle, module);
  m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
  m._compile(kopf + '\nmodule.exports = { setup, AUFG, ETAPPEN, get origin() { return origin; } };', quelle);
  return m.exports;
}
const H = ladeHelfer();
const AUS = path.join(root, 'test-results/durchlauf');
fs.mkdirSync(AUS, { recursive: true });
const messung = [];
const ablauf = []; // Beobachtungen aus den Abläufen
const merke = (o) => ablauf.push(o);

const BREITEN = [[390, 844, 'handy'], [820, 1180, 'tablet'], [1280, 800, 'rechner']];
const LOOKS = ['light', 'dark'];

// Zusätzliche Server-Antworten (spätere Routen haben in Playwright Vorrang; Rest geht an setup zurück).
async function extras(page, opt = {}) {
  const ohne = ({ loesung, ...r }) => r;
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); const d = b.daten || {};
    const antwort = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
    if (opt.kaputt && b.aktion === opt.kaputt) return route.fulfill({ status: 500, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Interner Fehler' }) });
    if (b.aktion === 'schule_wiederholung') return antwort({ ok: true, aufgaben: opt.leer ? [] : [
      { ...ohne(H.AUFG[11]), einheit_id: 1, stadt: 'Rom', etappe: 'Welchen Wert hat eine Ziffer?' },
      { ...ohne(H.AUFG[14]), einheit_id: 1, stadt: 'Rom', etappe: 'Große Zahlen lesen' }] });
    if (b.aktion === 'schule_zugaenge') return antwort({ ok: true, zugaenge: opt.leer ? [] : [
      { id: 1, name: 'Herr Lehrer', rolle: 'lehrer', aktiv: true, zuletzt: '2026-11-13T10:00:00Z' },
      { id: 2, name: 'Kind A', rolle: 'kind', kind: 'Kind A', aktiv: true, zuletzt: null },
      { id: 3, name: 'Alte Tablet-Anmeldung', rolle: 'eltern', aktiv: false }] });
    if (b.aktion === 'schule_zugang_anlegen') return antwort({ ok: true, code: 'QWER-TZUP-ASDF' });
    if (opt.leer) {
      if (b.aktion === 'schule_uebersicht') return antwort({ ok: true, leitung: true, einheiten: [], orte: [], lernende: [{ id: 1, name: 'Kind A', klasse: 5, stil: 'entdecker', welt: 'Ozean', ist_test: false, route: [], stand: [] }] });
      if (b.aktion === 'schule_konto') return antwort({ ok: true, konto: { sterne: 0, sterne_gesamt: 0, stempel: 0, lerntage: 0, jahrgang: { schulart: 'gym_by', klasse: 5, themen: 14, mit_inhalt: 0, geschafft: 0 } }, look: { stil: 'entdecker', welt: 'Ozean' }, belohnungen: [], einloesungen: [] });
      if (b.aktion === 'schule_eltern') return antwort({ ok: true, kinder: [{ id: 1, name: 'Kind A', konto: { sterne: 0, stempel: 0, lerntage: 0 } }], belohnungen: [], einloesungen: [] });
      if (b.aktion === 'schule_merkheft') return antwort({ ok: true, einheiten: [] });
      if (b.aktion === 'schule_rueckmeldungen') return antwort({ ok: true, rueckmeldungen: [] });
      if (b.aktion === 'schule_lehrplan_uebersicht') return antwort({ ok: true, kinder: [], themen: [] });
      if (b.aktion === 'schule_plan_lesen') return antwort({ ok: true, kind: { id: 1, name: 'Kind A', klasse: 5 }, revision: 0, plan: [], orte: [], notizen: [], verlauf: [] });
      if (b.aktion === 'schule_einheit_lesen') return antwort({ ok: true, einheit_id: d.einheit_id, status: 'geprueft', inhalt: { ziel: 'Leeres Thema', etappen: [] }, uebungen: [], stand: [], etappen_stand: {}, laufender_test: null });
    }
    return route.fallback();
  });
}

// Messungen in der Seite: Querscrollen, kleine Tippflächen, Abgeschnittenes, Überlappung, Kontrast, Knöpfe ohne Namen.
async function miss(page) {
  return page.evaluate(() => {
    const vw = window.innerWidth;
    const sichtbar = (e) => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && !e.closest('[hidden]') && !e.closest('details:not([open]) > :not(summary)'); };
    const name = (e) => (e.getAttribute('aria-label') || e.textContent || e.value || e.placeholder || '').trim().replace(/\s+/g, ' ').slice(0, 50);
    const wo = (e) => { const r = e.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y + scrollY), w: Math.round(r.width), h: Math.round(r.height) }; };
    const bedien = [...document.querySelectorAll('a[href], button, input:not([type=hidden]), select, textarea, summary, [role=tab], [role=button], [tabindex]:not([tabindex="-1"])')].filter(sichtbar);
    const klein = bedien.map((e) => ({ e, ...wo(e) })).filter((x) => x.h < 44 || x.w < 44).map(({ e, ...r }) => ({ tag: e.tagName.toLowerCase(), klasse: String(e.className?.baseVal ?? e.className).slice(0, 40), name: name(e), ...r }));
    const ohneName = bedien.filter((e) => !name(e) && !e.labels?.length && !e.getAttribute('aria-labelledby')).map((e) => ({ tag: e.tagName.toLowerCase(), klasse: String(e.className?.baseVal ?? e.className).slice(0, 40), ...wo(e) }));
    const ueber = [];
    for (let i = 0; i < bedien.length; i++) for (let j = i + 1; j < bedien.length; j++) {
      const a = bedien[i], b = bedien[j]; if (a.contains(b) || b.contains(a)) continue;
      const r = a.getBoundingClientRect(), s = b.getBoundingClientRect();
      const fl = Math.max(0, Math.min(r.right, s.right) - Math.max(r.left, s.left)) * Math.max(0, Math.min(r.bottom, s.bottom) - Math.max(r.top, s.top));
      if (fl > 16) ueber.push({ a: name(a), b: name(b), flaeche: Math.round(fl) });
    }
    const abgeschnitten = [];
    for (const e of document.querySelectorAll('#main *, header.top *')) {
      if (!sichtbar(e) || e.closest('svg')) continue;
      const s = getComputedStyle(e); const r = e.getBoundingClientRect();
      const txt = [...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
      if (txt && (r.right > vw + 1 || r.left < -1)) abgeschnitten.push({ art: 'ausserhalb', text: name(e), ...wo(e) });
      if (['hidden', 'clip'].includes(s.overflowX) && e.scrollWidth > e.clientWidth + 2 && e.textContent.trim()) abgeschnitten.push({ art: 'overflow', text: name(e), sw: e.scrollWidth, cw: e.clientWidth });
      if (s.textOverflow === 'ellipsis' && e.scrollWidth > e.clientWidth + 1) abgeschnitten.push({ art: 'ellipse', text: name(e) });
    }
    const lum = (c) => { const m = c.match(/[\d.]+/g).map(Number); const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return { l: 0.2126 * f(m[0]) + 0.7152 * f(m[1]) + 0.0722 * f(m[2]), a: m[3] ?? 1 }; };
    const hinter = (e) => { for (let x = e; x; x = x.parentElement) { const s = getComputedStyle(x); if (s.backgroundImage !== 'none') return null; const c = lum(s.backgroundColor); if (c.a > 0.9) return s.backgroundColor; } return getComputedStyle(document.documentElement).backgroundColor; };
    const kontrast = [];
    for (const e of document.querySelectorAll('#main *, header.top *')) {
      if (!sichtbar(e) || e.closest('svg') || !(([...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())))) continue;
      const s = getComputedStyle(e); const bg = hinter(e); if (!bg) continue;
      const v = lum(s.color), h = lum(bg); if (v.a < 0.5) continue;
      const k = (Math.max(v.l, h.l) + 0.05) / (Math.min(v.l, h.l) + 0.05);
      const gross = parseFloat(s.fontSize) >= 24 || (parseFloat(s.fontSize) >= 18.6 && Number(s.fontWeight) >= 700);
      if (k < (gross ? 3 : 4.5)) kontrast.push({ text: name(e), kontrast: Math.round(k * 100) / 100, farbe: s.color, hinter: bg, groesse: s.fontSize });
    }
    // Wichtigste Handlung: erster Haupt-Knopf; ist er beim Öffnen ganz sichtbar und nicht verdeckt?
    const haupt = [...document.querySelectorAll('#main .lr-knopf, #main .btn.primary, #main button.primary, #main a.primary')].find(sichtbar);
    let hauptInfo = null;
    if (haupt) { const r = haupt.getBoundingClientRect(); const oben = document.elementFromPoint(Math.min(vw - 1, r.left + r.width / 2), Math.min(innerHeight - 1, Math.max(0, r.top + r.height / 2)));
      hauptInfo = { name: name(haupt), top: Math.round(r.top + scrollY), bottom: Math.round(r.bottom + scrollY), imBild: r.top >= 0 && r.bottom <= innerHeight, verdecktVon: oben && !haupt.contains(oben) ? (oben.closest('nav, header, .tabbar, [class*=nav]')?.className || oben.tagName) : null }; }
    return { haupt: hauptInfo, vh: innerHeight, scrollW: document.documentElement.scrollWidth, vw, klein, ohneName, ueber, abgeschnitten: abgeschnitten.slice(0, 30), kontrast: kontrast.slice(0, 30),
      text: document.querySelector('#main')?.innerText.slice(0, 400) };
  });
}

async function neu(t, { breite, hoehe, look, ...opt }) {
  const nach = [];
  const r = await H.setup({ after: (fn) => nach.push(fn) }, opt);
  await extras(r.page, opt);
  const fehler = []; r.page.on('pageerror', (e) => fehler.push(e.message));
  r.page.on('console', (m) => { if (m.type() === 'error' && !/cdnjs|ERR_FAILED/.test(m.text())) fehler.push('console: ' + m.text()); });
  await r.page.setViewportSize({ width: breite, height: hoehe });
  await r.page.emulateMedia({ colorScheme: look });
  t.after(async () => { for (const fn of nach.reverse()) { try { await fn(); } catch (e) { fehler.push('setup-Prüfung: ' + e.message.split('\n')[0]); } } });
  return { ...r, fehler };
}
async function warte(page) {
  await page.waitForFunction(() => !document.querySelector('#main .spinner'), null, { timeout: 5000 }).catch(() => {});
  await page.waitForTimeout(250);
}
async function bild(page, name) { await page.screenshot({ path: path.join(AUS, name + '.png'), fullPage: true }); }

const ANSICHTEN_KIND = ['reise/1', 'reise/2', 'weg/1', 'weltkarte/1', 'reisepass/1', 'merkheft/1', 'wiederholen/1', 'lerneinheit/1-1', 'lerneinheit/1-1-ueben-1', 'lerneinheit/1-1-fehler', 'lerneinheit/1-1-test'];
const ANSICHTEN_ELTERN = ['lernen', 'lehrplan', 'inhalte/1', 'inhalte/77', 'plan/1', 'rueckmeldungen', 'zugaenge'];

for (const [breite, hoehe, geraet] of BREITEN) for (const look of LOOKS) {
  test(`Ansichten ${geraet} ${look}`, async (t) => {
    const { page, fehler } = await neu(t, { breite, hoehe, look });
    for (const a of [...ANSICHTEN_KIND, ...ANSICHTEN_ELTERN]) {
      const vorher = fehler.length;
      await page.goto(H.origin + '/#/' + a); await warte(page);
      if (a.startsWith('inhalte/')) await page.evaluate(() => document.querySelectorAll('details.lp-karte').forEach((d) => { d.open = true; }));
      const n = `${a.replace(/\//g, '_')}-${breite}-${look}`;
      await bild(page, n);
      await page.screenshot({ path: path.join(AUS, n + '-blick.png') });
      messung.push({ ansicht: a, breite, look, bild: n, fehler: fehler.slice(vorher), ...(await miss(page)) });
    }
    // Eigene Lernen-Seite: Anmeldung
    const s = await neu(t, { breite, hoehe, look, lernSeite: true, rolle: 'lehrer' });
    await s.page.goto(H.origin + '/lernen/'); await warte(s.page);
    await bild(s.page, `lernseite-anmeldung-${breite}-${look}`);
    messung.push({ ansicht: 'lernen/ (Anmeldung)', breite, look, bild: `lernseite-anmeldung-${breite}-${look}`, fehler: s.fehler.slice(), ...(await miss(s.page)) });
    await s.page.getByLabel('Lern-Code').fill('ABCD-EFGH-JKLM');
    await s.page.getByRole('button', { name: 'Anmelden' }).click(); await warte(s.page);
    await bild(s.page, `lernseite-lehrer-start-${breite}-${look}`);
    messung.push({ ansicht: 'lernen/ (Lehrer nach Anmeldung)', breite, look, bild: `lernseite-lehrer-start-${breite}-${look}`, fehler: s.fehler.slice(), ...(await miss(s.page)) });
    // Leerer Zustand
    const l = await neu(t, { breite, hoehe, look, leer: true });
    for (const a of ['lernen', 'reise/1', 'weg/1', 'weltkarte/1', 'reisepass/1', 'merkheft/1', 'wiederholen/1', 'lerneinheit/1-5', 'lehrplan', 'plan/1', 'rueckmeldungen', 'zugaenge']) {
      const vorher = l.fehler.length;
      await l.page.goto(H.origin + '/#/' + a); await warte(l.page);
      const n = `leer-${a.replace(/\//g, '_')}-${breite}-${look}`;
      await bild(l.page, n);
      await l.page.screenshot({ path: path.join(AUS, n + '-blick.png') });
      messung.push({ ansicht: 'leer: ' + a, breite, look, bild: n, fehler: l.fehler.slice(vorher), ...(await miss(l.page)) });
    }
  });
}

// Abläufe mit Klicks (Kind): alle Antwortarten, Tipp, Erklärung, falsch, Lernkarte sitzt, Test, Wiederholen, Merkheft, Reisepass.
for (const [breite, hoehe, geraet] of BREITEN) for (const look of LOOKS) {
  test(`Ablauf Kind ${geraet} ${look}`, async (t) => {
    const { page, fehler } = await neu(t, { breite, hoehe, look });
    const p = (n) => `kind-${n}-${breite}-${look}`;
    // Heute: Statistik antippen
    await page.goto(H.origin + '/#/reise/1'); await warte(page);
    await page.locator('details.lr-stats-box > summary').click(); await bild(page, p('01-heute-stats-offen'));
    // Klicks von „App öffnen“ bis zur ersten Aufgabe
    await page.getByRole('link', { name: /Losreisen|Weiter geht/ }).click(); await warte(page);
    const nachLos = await page.evaluate(() => ({ hash: location.hash, eingabe: !!document.querySelector('.lr-panel:not([hidden]) input') }));
    merke({ was: 'klicks_bis_aufgabe', breite, look, nachLosreisen: nachLos });
    await bild(page, p('02-thema-erklaeren'));
    // Erste Aufgabe: Dazu üben
    await page.locator('.lr-panel:not([hidden])').getByRole('button', { name: 'Dazu üben ▸' }).first().click(); await warte(page);
    const fokus1 = await page.evaluate(() => document.activeElement?.tagName + ' ' + (document.activeElement?.getAttribute('aria-label') || document.activeElement?.textContent?.slice(0, 30)));
    merke({ was: 'fokus_nach_dazu_ueben', breite, look, fokus: fokus1 });
    await bild(page, p('03-ueben-zahl'));
    // Tipp und Erklärung
    await page.getByRole('button', { name: 'Tipp' }).click();
    await page.getByRole('button', { name: 'Erklärung' }).click(); await page.waitForTimeout(150);
    await bild(page, p('04-tipp-erklaerung'));
    // Enter im Antwortfeld
    const feld = page.getByRole('textbox', { name: 'Antwort' });
    await feld.fill('2000'); await feld.press('Enter'); await page.waitForTimeout(400);
    const enterGeht = await page.getByText('Richtig!').count() + await page.getByText('Noch nicht').count();
    merke({ was: 'enter_prueft', breite, look, ergebnis: enterGeht > 0 });
    if (!enterGeht) await page.getByRole('button', { name: 'Prüfen' }).click();
    await page.getByText(/Richtig!|Noch nicht/).first().waitFor();
    await bild(page, p('05-richtig-mit-tipp'));
    await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
    // Falsche Antwort
    await page.getByRole('textbox', { name: 'Antwort' }).fill('200'); await page.getByRole('button', { name: 'Prüfen' }).click();
    await page.getByText('Noch nicht').first().waitFor(); await page.waitForTimeout(400);
    await bild(page, p('06-falsch'));
    // Zwei richtig hintereinander -> Lernkarte sitzt
    for (let i = 0; i < 3 && !(await page.getByText('LERNKARTE SITZT').count()); i++) {
      await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
      await page.getByRole('textbox', { name: 'Antwort' }).fill('2000'); await page.getByRole('button', { name: 'Prüfen' }).click(); await page.waitForTimeout(300);
    }
    await page.waitForTimeout(500);
    await bild(page, p('07-lernkarte-sitzt'));
    merke({ was: 'sitzt_sichtbar_ohne_scroll', breite, look, ergebnis: await page.evaluate(() => { const s = document.querySelector('.lr-sitzt'); if (!s) return 'fehlt'; const r = s.getBoundingClientRect(); return r.top < innerHeight && r.bottom > 0; }) });
    // Zahlenstrahl
    await page.getByRole('button', { name: /Nächste Karte/ }).click(); await warte(page);
    await bild(page, p('08-zahlenstrahl'));
    const strahl = await page.evaluate(() => [...document.querySelectorAll('.lern-strahl .ziel')].map((e) => { const r = e.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), tab: e.getAttribute('tabindex'), rolle: e.getAttribute('role') }; }));
    merke({ was: 'zahlenstrahl_ziele', breite, look, ziele: strahl });
    await page.getByRole('button', { name: 'Markierung 4' }).click(); await page.waitForTimeout(100);
    await bild(page, p('09-zahlenstrahl-gewaehlt'));
    await page.getByRole('button', { name: 'Prüfen' }).click(); await page.waitForTimeout(300);
    // Term, Bruch, Zahlenpaar
    await page.goto(H.origin + '/#/lerneinheit/1-1-3'); await warte(page);
    await bild(page, p('10-term'));
    await page.getByRole('button', { name: 'Prüfen' }).click(); await page.waitForTimeout(200);
    await bild(page, p('11-term-leer-pruefen'));
    await page.getByRole('textbox', { name: 'Dein Term' }).fill('x²+2x+1'); await page.getByRole('button', { name: 'Prüfen' }).click();
    await page.getByText(/Richtig!|Noch nicht/).first().waitFor();
    await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
    await bild(page, p('12-bruch'));
    await page.getByRole('textbox', { name: 'Zähler' }).fill('3'); await page.getByRole('textbox', { name: 'Nenner' }).fill('4');
    await page.getByRole('button', { name: 'Prüfen' }).click(); await page.getByText(/Richtig!/).first().waitFor();
    await page.getByRole('button', { name: 'Nächste Aufgabe' }).click();
    await bild(page, p('13-zahlenpaar'));
    await page.getByRole('textbox', { name: 'Lücke 1' }).fill('2'); await page.getByRole('textbox', { name: 'Lücke 2' }).fill('-1');
    await page.getByRole('button', { name: 'Prüfen' }).click(); await page.waitForTimeout(300);
    await bild(page, p('14-zahlenpaar-geprueft'));
    merke({ was: 'zahlenpaar_minus', breite, look, text: await page.locator('[role=status]').last().innerText().catch(() => '') });
    // Fehler-Reiter
    await page.getByRole('tab', { name: /Fehler/ }).click(); await page.waitForTimeout(200);
    await bild(page, p('15-fehler-reiter'));
    // Test mit Auswahl
    await page.goto(H.origin + '/#/lerneinheit/1-1-test'); await warte(page);
    await bild(page, p('16-test-start'));
    await page.getByRole('button', { name: 'Test starten' }).click(); await page.waitForTimeout(300);
    await bild(page, p('17-test-auswahl'));
    await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click();
    await page.getByRole('button', { name: 'Weiter ›' }).click(); await page.waitForTimeout(200);
    await bild(page, p('18-test-strahl'));
    await page.getByRole('button', { name: 'Abgeben' }).click(); await page.waitForTimeout(400);
    await bild(page, p('19-test-ergebnis'));
    // Wiederholen
    await page.goto(H.origin + '/#/reise/1'); await warte(page);
    const wdhLink = await page.getByRole('link', { name: /zum Wiederholen/ }).count();
    merke({ was: 'wiederholen_auf_heute', breite, look, ergebnis: wdhLink });
    await page.goto(H.origin + '/#/wiederholen/1'); await warte(page);
    await page.getByRole('textbox', { name: 'Antwort' }).fill('5'); await page.getByRole('button', { name: 'Prüfen' }).click(); await page.waitForTimeout(300);
    await bild(page, p('20-wiederholen-falsch'));
    await page.getByRole('button', { name: 'Nächste' }).click();
    await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click(); await page.getByRole('button', { name: 'Prüfen' }).click(); await page.waitForTimeout(300);
    await page.getByRole('button', { name: 'Fertig' }).click(); await page.waitForTimeout(200);
    await bild(page, p('21-wiederholen-fertig'));
    // Merkheft-Suche
    await page.goto(H.origin + '/#/merkheft/1'); await warte(page);
    await page.getByRole('searchbox').fill('zahlenstrahl'); await page.waitForTimeout(200);
    await bild(page, p('22-merkheft-suche'));
    // Reisepass: einlösen
    await page.goto(H.origin + '/#/reisepass/1'); await warte(page);
    await page.getByRole('button', { name: 'Einlösen' }).first().click(); await page.waitForTimeout(300);
    await bild(page, p('23-reisepass-eingeloest'));
    merke({ was: 'reisepass_ueber_nav', breite, look, ergebnis: await page.locator('.lr-nav a', { hasText: 'Reisepass' }).count() });
    // Weltkarte: Orte antippbar?
    await page.goto(H.origin + '/#/weltkarte/1'); await warte(page);
    merke({ was: 'weltkarte_links', breite, look, links: await page.locator('#main a').allTextContents() });
    merke({ was: 'fehler_kind', breite, look, fehler: fehler.slice() });
  });
}

// Abläufe Eltern/Lehrer: Filter, Inhalte, Anmerkung, Plan ordnen + speichern, Rückmeldung, Zugang anlegen.
for (const [breite, hoehe, geraet] of BREITEN) for (const look of LOOKS) {
  test(`Ablauf Eltern/Lehrer ${geraet} ${look}`, async (t) => {
    const { page, fehler, calls } = await neu(t, { breite, hoehe, look });
    const p = (n) => `eltern-${n}-${breite}-${look}`;
    await page.goto(H.origin + '/#/lehrplan'); await warte(page);
    await page.getByRole('combobox', { name: 'Klasse' }).selectOption('5'); await page.waitForTimeout(150);
    await bild(page, p('01-lehrplan-klasse5'));
    await page.getByRole('combobox', { name: 'Klasse' }).selectOption('');
    await page.getByRole('combobox', { name: 'Inhalt' }).selectOption('leer'); await page.waitForTimeout(150);
    await page.locator('.lp-zeile', { hasText: 'Lineare Funktionen' }).getByRole('button', { name: 'Bauen lassen' }).click(); await page.waitForTimeout(300);
    await bild(page, p('02-lehrplan-bauen'));
    await page.goto(H.origin + '/#/inhalte/1'); await warte(page);
    await page.locator('details.lp-karte > summary').first().click(); await page.waitForTimeout(150);
    await bild(page, p('03-inhalte-karte'));
    const anm = page.getByText(/✎ Anmerkung/).first();
    merke({ was: 'anmerkung_in_inhalte', breite, look, ergebnis: await page.getByText(/✎ Anmerkung/).count() });
    if (await page.getByText(/✎ Anmerkung/).count()) {
      await anm.click();
      const f = page.locator('.lern-anmerkung[open]').first();
      await f.getByRole('button', { name: 'Schwieriger' }).click().catch(() => {});
      await f.getByLabel('Deine Anmerkung').fill('Bitte eine Aufgabe mit Null in der Mitte.');
      await f.getByRole('button', { name: 'Senden' }).click(); await page.waitForTimeout(300);
      await bild(page, p('04-inhalte-anmerkung'));
    }
    // Anmerkung an einer Aufgabe in der Kindansicht (Eltern sind Leitung)
    await page.goto(H.origin + '/#/lerneinheit/3-1-1'); await warte(page);
    await page.getByText('✎ Anmerkung zu dieser Aufgabe').click(); await page.waitForTimeout(150);
    await bild(page, p('05-anmerkung-aufgabe'));
    // Themenplan
    await page.goto(H.origin + '/#/plan/1'); await warte(page);
    await bild(page, p('06-plan'));
    await page.getByRole('button', { name: 'New York – Zinsen nach oben' }).click();
    await page.getByRole('button', { name: '+ Athen – Teilbarkeit' }).click(); await page.waitForTimeout(150);
    await bild(page, p('07-plan-geaendert'));
    await page.getByRole('button', { name: 'Plan speichern' }).click(); await page.waitForTimeout(300);
    await bild(page, p('08-plan-gespeichert'));
    merke({ was: 'plan_speichern', breite, look, gespeichert: calls.filter((c) => c.aktion === 'schule_plan_setzen').length });
    // Rückmeldungen
    await page.goto(H.origin + '/#/rueckmeldungen'); await warte(page);
    await page.locator('.lern-rm-form').first().getByRole('button', { name: 'Senden' }).click(); await page.waitForTimeout(200);
    await bild(page, p('09-rueckmeldung-leer-senden'));
    await page.locator('.lern-rm-form').first().getByLabel('Deine Anmerkung').fill('Prozentrechnung fehlt.');
    await page.locator('.lern-rm-form').first().getByRole('button', { name: 'Senden' }).click(); await page.waitForTimeout(300);
    await bild(page, p('10-rueckmeldung-gesendet'));
    // Zugänge
    await page.goto(H.origin + '/#/zugaenge'); await warte(page);
    await page.getByRole('button', { name: 'Code erzeugen' }).click(); await page.waitForTimeout(150);
    await bild(page, p('11-zugang-ohne-name'));
    await page.getByRole('textbox', { name: 'Name' }).fill('Frau Lehrerin');
    await page.getByRole('combobox', { name: 'Rolle' }).selectOption('kind'); await page.waitForTimeout(100);
    await page.getByRole('button', { name: 'Code erzeugen' }).click(); await page.waitForTimeout(400);
    await bild(page, p('12-zugang-code'));
    merke({ was: 'zugang_kind_name', breite, look, daten: calls.find((c) => c.aktion === 'schule_zugang_anlegen')?.daten });
    // Übersicht: Belohnung ohne Namen
    await page.goto(H.origin + '/#/lernen'); await warte(page);
    await page.getByRole('button', { name: 'Hinzufügen' }).click(); await page.waitForTimeout(150);
    await page.locator('#bl-titel').fill(''); await page.locator('#bl-titel').fill('');
    await page.locator('#bl-sterne').fill(''); await page.locator('#bl-titel').fill('Ausflug'); await page.getByRole('button', { name: 'Hinzufügen' }).click(); await page.waitForTimeout(300);
    merke({ was: 'belohnung_ohne_kosten', breite, look, daten: calls.filter((c) => c.aktion === 'schule_belohnung_setzen').map((c) => c.daten) });
    merke({ was: 'fehler_eltern', breite, look, fehler: fehler.slice() });
  });
}

// Tastatur, Server-Fehler, Lernen-Seite mit Kind-Code.
test('Tastatur und Fehlerfälle', async (t) => {
  const { page, fehler } = await neu(t, { breite: 1280, hoehe: 800, look: 'light' });
  await page.goto(H.origin + '/#/lerneinheit/1-1'); await warte(page);
  const weg = [];
  for (let i = 0; i < 25; i++) {
    await page.keyboard.press('Tab');
    weg.push(await page.evaluate(() => { const e = document.activeElement; const s = getComputedStyle(e); return { tag: e.tagName.toLowerCase(), name: (e.getAttribute('aria-label') || e.textContent || '').trim().slice(0, 30), sichtbar: s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0 || s.boxShadow !== 'none' }; }));
  }
  merke({ was: 'tab_reihenfolge_lerneinheit', weg });
  // Reiter mit Pfeiltasten?
  await page.getByRole('tab', { name: 'Erklären' }).focus(); await page.keyboard.press('ArrowRight'); await page.waitForTimeout(150);
  merke({ was: 'reiter_pfeiltaste', aktiv: await page.evaluate(() => document.querySelector('[role=tab][aria-selected=true]')?.textContent) });
  await page.getByRole('tab', { name: /Üben/ }).focus(); await page.keyboard.press('Enter'); await page.waitForTimeout(200);
  // Zahlenstrahl mit Tastatur
  await page.goto(H.origin + '/#/lerneinheit/1-1-ueben-2'); await warte(page);
  const zielFokus = [];
  for (let i = 0; i < 30; i++) { await page.keyboard.press('Tab'); const x = await page.evaluate(() => document.activeElement?.getAttribute('aria-label') || document.activeElement?.tagName); zielFokus.push(x); if (/Markierung 4/.test(x || '')) break; }
  await page.keyboard.press('Enter'); await page.waitForTimeout(100);
  await bild(page, 'tastatur-zahlenstrahl-1280-light');
  merke({ was: 'zahlenstrahl_tastatur', erreicht: zielFokus.some((x) => /Markierung/.test(x || '')), gedrueckt: await page.evaluate(() => document.querySelector('.lern-strahl .ziel.on, .lern-strahl [aria-pressed=true]')?.getAttribute('aria-label') || null) });
  // Fokus nach Prüfen
  await page.goto(H.origin + '/#/lerneinheit/1-1-ueben-1'); await warte(page);
  await page.getByRole('textbox', { name: 'Antwort' }).fill('2000'); await page.getByRole('button', { name: 'Prüfen' }).click(); await page.waitForTimeout(400);
  merke({ was: 'fokus_nach_pruefen', fokus: await page.evaluate(() => document.activeElement?.tagName + ' ' + (document.activeElement?.textContent || '').slice(0, 30)) });
  merke({ was: 'fehler_tastatur', fehler: fehler.slice() });

  for (const [kaputt, ansicht] of [['schule_uebersicht', 'reise/1'], ['schule_einheit_lesen', 'lerneinheit/1-1'], ['schule_uebung_pruefen', 'lerneinheit/1-1-ueben-1']]) {
    for (const breite of [390]) {
      const k = await neu(t, { breite, hoehe: 844, look: 'light', kaputt });
      await k.page.goto(H.origin + '/#/' + ansicht); await warte(k.page);
      if (kaputt === 'schule_uebung_pruefen') { await k.page.getByRole('textbox', { name: 'Antwort' }).fill('2000'); await k.page.getByRole('button', { name: 'Prüfen' }).click(); await k.page.waitForTimeout(300); }
      const n = `serverfehler-${kaputt}-${breite}-light`; await bild(k.page, n);
      merke({ was: 'serverfehler', kaputt, ansicht, text: await k.page.locator('#main').innerText(), zurueck: await k.page.locator('#btn-back').isVisible(), links: await k.page.locator('#main a, #main button').count(), fehler: k.fehler });
    }
  }
  // Kind auf der Lernen-Seite
  const kd = await neu(t, { breite: 390, hoehe: 844, look: 'light', lernSeite: true, rolle: 'kind' });
  await kd.page.goto(H.origin + '/lernen/'); await kd.page.getByLabel('Lern-Code').fill('abcd-efgh-jklm');
  await kd.page.getByRole('button', { name: 'Anmelden' }).click(); await kd.page.waitForTimeout(600);
  await bild(kd.page, 'lernseite-kind-kleinbuchstaben-390-light');
  merke({ was: 'code_kleinbuchstaben', hash: await kd.page.evaluate(() => location.hash), text: await kd.page.locator('#main').innerText() });
  await kd.page.getByLabel('Lern-Code').fill('ABCD-EFGH-JKLM').catch(() => {});
  await kd.page.getByRole('button', { name: 'Anmelden' }).click().catch(() => {}); await kd.page.waitForTimeout(600);
  await bild(kd.page, 'lernseite-kind-reise-390-light');
  merke({ was: 'kind_lernseite', hash: await kd.page.evaluate(() => location.hash), abmelden: await kd.page.locator('#btn-abmelden').isVisible(), fehler: kd.fehler });
});


// Nachprüfungen einzelner Befunde (Bilder im Ausschnitt, Messwerte in ablauf).
test('Nachprüfungen', async (t) => {
  const { page, fehler } = await neu(t, { breite: 390, hoehe: 844, look: 'light' });
  const dialoge = []; page.on('dialog', (d) => { dialoge.push(d.message()); d.accept(); });
  // Rückmeldung leer senden
  await page.goto(H.origin + '/#/rueckmeldungen'); await warte(page);
  await page.locator('.lern-rm-form').first().getByRole('button', { name: 'Senden' }).click(); await page.waitForTimeout(200);
  merke({ was: 'rm_leer_status', text: await page.locator('.lern-rm-form [role=status]').first().innerText(), sichtbar: await page.locator('.lern-rm-form [role=status]').first().isVisible(),
    box: await page.locator('.lern-rm-form [role=status]').first().boundingBox() });
  await page.locator('.lern-rm-form').first().screenshot({ path: path.join(AUS, 'nach-rm-leer-390.png') });
  // Zugang anlegen
  await page.goto(H.origin + '/#/zugaenge'); await warte(page);
  await page.getByRole('textbox', { name: 'Name' }).fill('Frau Lehrerin');
  await page.getByRole('combobox', { name: 'Rolle' }).selectOption('kind');
  await page.getByRole('button', { name: 'Code erzeugen' }).click(); await page.waitForTimeout(500);
  merke({ was: 'zugang_status', text: await page.locator('form [role=status]').innerText(), feld: await page.getByRole('textbox', { name: 'Name' }).inputValue() });
  await page.screenshot({ path: path.join(AUS, 'nach-zugang-390.png'), fullPage: true });
  // Hover auf Haupt-Knopf (Maus) am Rechner
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.goto(H.origin + '/#/lerneinheit/1-1-ueben-1'); await warte(page);
  const k = page.getByRole('button', { name: 'Prüfen' });
  await k.scrollIntoViewIfNeeded(); await page.mouse.move(5, 5); await page.waitForTimeout(150);
  const farbe = () => k.evaluate((e) => { const s = getComputedStyle(e); return { bg: s.backgroundColor, fg: s.color }; });
  const ohne = await farbe(); await k.screenshot({ path: path.join(AUS, 'nach-pruefen-ohne-maus-1280.png') });
  await k.hover(); await page.waitForTimeout(250);
  const mit = await farbe(); await k.screenshot({ path: path.join(AUS, 'nach-pruefen-hover-1280.png') });
  merke({ was: 'hover_lr_knopf', ohne, mit });
  // Haupt-Knopf beim Öffnen: Bild nur vom Bildschirm
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(H.origin + '/#/reise/1'); await warte(page); await page.screenshot({ path: path.join(AUS, 'nach-heute-blick-390.png') });
  await page.goto(H.origin + '/#/lerneinheit/1-1-ueben-1'); await warte(page); await page.screenshot({ path: path.join(AUS, 'nach-ueben-blick-390.png') });
  // Ganz nach unten gescrollt: verdeckt die Leiste den letzten Inhalt?
  for (const a of ['reise/1', 'weg/1', 'lerneinheit/1-1']) {
    await page.goto(H.origin + '/#/' + a); await warte(page);
    await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight)); await page.waitForTimeout(200);
    merke({ was: 'unten_verdeckt', ansicht: a, info: await page.evaluate(() => { const nav = document.querySelector('.lr-nav').getBoundingClientRect(); const inh = [...document.querySelectorAll('.lr-inhalt > *, .lr-thema > *')].filter((e) => e.getBoundingClientRect().height > 0).pop(); const r = inh.getBoundingClientRect(); return { navTop: Math.round(nav.top), letztesUnten: Math.round(r.bottom), text: inh.textContent.trim().slice(0, 40) }; }) });
    await page.screenshot({ path: path.join(AUS, `nach-unten-${a.replace(/\//g, '_')}-390.png`) });
  }
  // Test abgeben mit offener Aufgabe (Dialog)
  await page.goto(H.origin + '/#/lerneinheit/1-1-test'); await warte(page);
  await page.getByRole('button', { name: 'Test starten' }).click(); await page.waitForTimeout(300);
  await page.getByRole('button', { name: 'Weiter ›' }).click(); await page.waitForTimeout(200);
  await page.getByRole('button', { name: 'Abgeben' }).click(); await page.waitForTimeout(500);
  merke({ was: 'test_abgeben_dialog', dialoge: dialoge.slice() });
  await page.screenshot({ path: path.join(AUS, 'nach-test-ergebnis-390.png'), fullPage: true });
  // Statistik-Erklärung, Kopfzeile, Zahlenstrahl-Ausschnitt
  await page.goto(H.origin + '/#/lerneinheit/1-1-ueben-2'); await warte(page);
  await page.locator('.lr-panel:not([hidden]) .lr-aufgabe .lern-strahl').first().screenshot({ path: path.join(AUS, 'nach-zahlenstrahl-390.png') });
  await page.locator('header.top').screenshot({ path: path.join(AUS, 'nach-kopf-390.png') });
  await page.locator('.lr-panel:not([hidden]) .lr-chips').first().screenshot({ path: path.join(AUS, 'nach-chips-390.png') });
  merke({ was: 'kopf_ellipse', titel: await page.locator('#title').textContent(), breiteText: await page.locator('#title').evaluate((e) => [e.scrollWidth, e.clientWidth]) });
  merke({ was: 'mitteilungen_link', href: await page.locator('header.top a').evaluateAll((l) => l.map((a) => [a.getAttribute('aria-label') || a.textContent.trim(), a.getAttribute('href')])) });
  // Glocke in der Lernreise
  await page.goto(H.origin + '/#/reise/1'); await warte(page);
  await page.getByRole('link', { name: 'Mitteilungen' }).click(); await warte(page);
  await page.screenshot({ path: path.join(AUS, 'nach-glocke-390.png') });
  merke({ was: 'glocke_ziel', hash: await page.evaluate(() => location.hash), kindmodus: await page.evaluate(() => document.body.hasAttribute('data-kindmodus')), bereiche: await page.locator('#areas').isVisible() });
  // Dunkel: Farben aus dem dunklen Schema auf hellen Flächen
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.goto(H.origin + '/#/plan/1'); await warte(page);
  await page.locator('.lern-plan-zeile').nth(1).screenshot({ path: path.join(AUS, 'nach-plan-dunkel-390.png') });
  await page.goto(H.origin + '/#/inhalte/1'); await warte(page);
  await page.locator('details.lp-karte > summary').first().click(); await page.waitForTimeout(150);
  await page.locator('.lp-tabelle').first().screenshot({ path: path.join(AUS, 'nach-inhalte-dunkel-390.png') });
  merke({ was: 'dunkel_lernen_flaeche', bg: await page.evaluate(() => getComputedStyle(document.body).backgroundColor), err: await page.evaluate(() => getComputedStyle(document.body).getPropertyValue('--err')), ok: await page.evaluate(() => getComputedStyle(document.body).getPropertyValue('--ok')) });
  merke({ was: 'fehler_nach', fehler: fehler.slice() });
});

test('Ergebnisse schreiben', () => {
  fs.writeFileSync(path.join(AUS, 'messung.json'), JSON.stringify({ messung, ablauf }, null, 1));
});
