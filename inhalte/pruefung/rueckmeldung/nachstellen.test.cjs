// Prüfrunde Rückmeldung & Lernweg: echte Aufgaben aus inhalte/themen im Üben nachstellen.
// Nutzt setup() aus tests/lernen.test.cjs unverändert. Überschrieben werden nur schule_einheit_lesen (echtes Thema),
// schule_uebung_pruefen (Bewertung und Serie wie in der Datenbank: schule.antwort_bewerten + schule.karte_buchen)
// und schule_wiederholung.
// Start: PW_TEST_EXECUTABLE=/pfad/chrome node --test inhalte/pruefung/rueckmeldung/nachstellen.test.cjs
'use strict';
const { test } = require('node:test');
const assert = require('node:assert');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; } };', quelle);
const H = m.exports;
const AUS = path.join(__dirname, 'bilder'); fs.mkdirSync(AUS, { recursive: true });
const PROTOKOLL = {};

// Bewertung wie schule.antwort_bewerten (vereinfacht, gleiche Ergebnisse für zahl/auswahl/luecken)
function bewerte(a, w) {
  if (a.y === 'luecken') {
    if (!Array.isArray(w?.werte) || w.werte.length !== a.o.werte.length) return { format_ok: false, hinweis: 'Bitte fülle alle Felder aus.' };
    const s = w.werte.map((x) => String(x).replace(/[\s ]/g, '').replace('−', '-').replace(/^\+/, ''));
    if (s.some((x) => x === '')) return { format_ok: false, hinweis: 'Bitte fülle alle Felder aus. Fehlt ein Glied, trage 0 ein.' };
    if (s.some((x) => !/^-?\d+$/.test(x))) return { format_ok: false, hinweis: 'In jedes Feld gehört eine ganze Zahl mit Vorzeichen, zum Beispiel −3.' };
    return { format_ok: true, richtig: s.every((x, i) => Number(x) === a.o.werte[i]) };
  }
  if (a.y === 'auswahl' || a.y === 'markierung') return { format_ok: true, richtig: Number(w.index) === a.o.index };
  let s = String(w?.wert ?? '').replace(/[\s ]/g, '');
  if (!s) return { format_ok: false, hinweis: 'Bitte gib eine Antwort ein.' };
  if (s.includes('.')) return { format_ok: false, hinweis: 'Bitte schreibe Dezimalzahlen mit Komma und Tausender mit Leerzeichen, zum Beispiel 4,5 oder 1 200.' };
  const e = a.o.einheit;
  if (e === '%' && s.includes('€')) return { format_ok: true, richtig: false, grund: 'falsche_einheit' };
  if (e === '€' && s.includes('%')) return { format_ok: true, richtig: false, grund: 'falsche_einheit' };
  if (e) s = s.replace(e, '');
  s = s.replace('−', '-').replace(',', '.');
  if (!/^-?\d+(\.\d+)?$/.test(s)) return { format_ok: false, hinweis: 'Bitte gib nur die Zahl ein.' };
  return { format_ok: true, richtig: Math.abs(Number(s) - a.o.wert) <= Math.max(1e-9, a.o.toleranz || 0) };
}

// Echtes Thema laden; Aufgaben-IDs 1000 + laufende Nummer
function thema(schluessel, karten) {
  const d = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themen', schluessel + '.json'), 'utf8'));
  const auf = d.aufgaben.filter((a) => a.p === 'uebung' && (!karten || karten.includes(a.l))).map((a, i) => ({ ...a, id: 1000 + i }));
  const nr = (lz) => d.inhalt.etappen.findIndex((e) => e.lernziel === lz) + 1;
  return { d, auf, nr, nachId: new Map(auf.map((a) => [a.id, a])) };
}

async function einrichten(page, th, opt = {}) {
  const stand = {}; const log = [];
  const ziel = (lz) => Math.min(4, Math.max(2, th.auf.filter((a) => a.l === lz).length));
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const b = JSON.parse(route.request().postData() || '{}'); const d = b.daten || {};
    const antw = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
    if (b.aktion === 'schule_einheit_lesen') {
      return antw({ ok: true, einheit_id: d.einheit_id, status: 'geprueft', inhalt: th.d.inhalt,
        uebungen: th.auf.map((a) => ({ id: a.id, lernziel: a.l, stufe: a.s, antworttyp: a.y, frage: a.f, antworten: a.a, tipp: a.h, versuche: 0, geloest: false })),
        stand: th.d.inhalt.etappen.map((x) => ({ lernziel: x.lernziel, pflicht: true, status: 'offen' })),
        etappen_stand: Object.fromEntries(th.d.inhalt.etappen.map((x) => [x.lernziel, { serie: 0, ziel: ziel(x.lernziel), sitzt: false, fertig: false, ...(opt.etappen?.[x.lernziel] || {}) }])),
        laufender_test: null });
    }
    if (b.aktion === 'schule_uebung_pruefen') {
      const a = th.nachId.get(d.aufgabe_id); const r = bewerte(a, d.antwort);
      if (!r.format_ok) { log.push({ id: a.id, format: r.hinweis }); return antw({ ok: true, format_ok: false, hinweis: r.hinweis }); }
      // wie schule.karte_buchen (nur Phase „noch nicht sitzt“ und Wiederholung mit Fehler)
      const k = stand[a.l] ||= { serie: 0, sitzt: !!opt.etappen?.[a.l]?.sitzt, wdh_stufe: 0 }; let neu = false;
      if (!k.sitzt) { if (!r.richtig) k.serie = 0; else if (!d.hilfe) k.serie++; if (k.serie >= ziel(a.l)) { k.sitzt = true; neu = true; } }
      else if (!r.richtig) { k.sitzt = false; k.serie = 0; }
      log.push({ id: a.id, frage: a.f.text.slice(0, 70), antwort: d.antwort, richtig: r.richtig, grund: r.grund || null, hilfe: d.hilfe || 0, serie: k.serie, sitzt: k.sitzt });
      return antw({ ok: true, format_ok: true, richtig: r.richtig, loesung: a.o, loesungsweg: a.w,
        karte: { serie: k.serie, ziel: ziel(a.l), sitzt: k.sitzt, neu_sitzt: neu, wdh_stufe: 0 } });
    }
    if (b.aktion === 'schule_wiederholung' && opt.wiederholung) {
      const a = th.auf.find((x) => x.l === opt.wiederholung);
      return antw({ ok: true, faellig: 1, aufgaben: [{ id: a.id, lernziel: a.l, antworttyp: a.y, frage: a.f, antworten: a.a, einheit_id: 1, stadt: 'Rom', etappe: th.d.inhalt.etappen.find((e) => e.lernziel === a.l).titel }] });
    }
    return route.fallback();
  });
  return { stand, log };
}

const warte = async (p, ms = 350) => { await p.waitForFunction(() => !document.querySelector('#main .spinner'), null, { timeout: 5000 }).catch(() => {}); await p.waitForTimeout(ms); };
const aufgabeText = (p) => p.locator('.lr-panel:not([hidden]) .lr-aufgabe, .lr-etappe-flaeche .lr-aufgabe').first().innerText();
async function finde(th, p) { const t = await aufgabeText(p); return th.auf.find((a) => t.includes(a.f.text.slice(0, 40))); }
async function gibEin(p, a, wert) {
  if (a.y === 'auswahl') { await p.locator('.lr-aufgabe').getByText(a.a[wert], { exact: true }).first().click(); return; }
  if (a.y === 'luecken' && await p.getByRole('textbox', { name: 'Dein Term' }).count()) { let i = 0; await p.getByRole('textbox', { name: 'Dein Term' }).fill(String(a.f.schablone).replace(/□/g, () => String(wert[i++])).replace(/^[a-z]\s*=\s*/i, '').replace(/\+\s*-/g, '− ')); return; }
  if (a.y === 'luecken') { for (let i = 0; i < wert.length; i++) await p.getByRole('textbox', { name: `Lücke ${i + 1}` }).fill(String(wert[i])); return; }
  await p.getByRole('textbox', { name: 'Antwort' }).fill(String(wert));
}
const richtigWert = (a) => a.y === 'auswahl' ? a.o.index : a.y === 'luecken' ? a.o.werte : String(a.o.wert).replace('.', ',') + (a.o.einheit ? ' ' + a.o.einheit : '');
async function pruefe(p) { await p.getByRole('button', { name: 'Prüfen' }).click(); await p.waitForTimeout(450); }
async function weiter(p) { await p.locator('.lr-weiter').first().click(); await p.waitForTimeout(350); }
const bild = (p, name, ganz = false) => p.screenshot({ path: path.join(AUS, name + '.png'), fullPage: ganz });
async function lauf(name, fn, gestaltung = 'tag') {
  test(name, async () => {
    const nach = []; const { page } = await H.setup({ after: (f) => nach.push(f) }, { gestaltung });
    await page.emulateMedia({ reducedMotion: 'reduce' });
    try { await fn(page); } finally { for (const f of nach.reverse()) { try { await f(); } catch { /* Seitenfehler hier nicht bewertet */ } } }
  });
}

// R1: Vorzeichenfehler Klasse 5 (zahlen.ganz/deuten) – was kommt zurück?
lauf('R1 Vorzeichenfehler Kl. 5', async (p) => {
  const th = thema('zahlen.ganz'); const { log } = await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/1-1-ueben-1'); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const a = await finde(th, p); assert.ok(a, 'Aufgabe erkannt');
  await gibEin(p, a, String(Math.abs(a.o.wert)));   // Minus vergessen
  await pruefe(p); await bild(p, 'r1-vorzeichen-handy', true);
  PROTOKOLL.r1 = { aufgabe: a.f.text, eingabe: Math.abs(a.o.wert), log, rueck: await p.locator('.lr-rueck').first().innerText() };
});

// R1a: dieselbe Situation in der alten Gestaltung (Eltern können umschalten)
lauf('R1a Vorzeichenfehler alt', async (p) => {
  const th = thema('zahlen.ganz'); await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/1-1-ueben-1'); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const a = await finde(th, p); await gibEin(p, a, String(Math.abs(a.o.wert))); await pruefe(p);
  await bild(p, 'r1a-vorzeichen-alt-handy', true);
}, 'alt');

// R2: Gleiche Aufgabe kommt zurück, Lösung gerade gesehen → zählt für „sitzt“
lauf('R2 Serie mit gemerkter Lösung', async (p) => {
  const th = thema('zahlen.ganz'); const { log } = await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/1-1-ueben-4'); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const folge = [];
  const erste = await finde(th, p); folge.push(erste.id);
  await gibEin(p, erste, '999'); await pruefe(p); await weiter(p);
  for (let i = 0; i < 6; i++) {
    const a = await finde(th, p); if (!a) break; folge.push(a.id);
    await gibEin(p, a, richtigWert(a)); await pruefe(p);
    if (await p.locator('.lr-gelandet, .lr-sitzt').count()) break;
    await weiter(p);
  }
  await bild(p, 'r2-gelandet-mit-wiederholter-aufgabe-handy');
  PROTOKOLL.r2 = { folge, gleicheAufgabeAnStelle: folge.indexOf(erste.id, 1), log };
  assert.ok(folge.indexOf(erste.id, 1) > 0, 'falsch beantwortete Aufgabe kommt wieder');
});

// R3: Prozent mit falscher Einheit und typischer Verwechslung (0,75 statt 75 %)
lauf('R3 Einheit und Verwechslung', async (p) => {
  const th = thema('bruch.prozent', ['prozent_bedeutung']); const { log } = await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/1-1-ueben-' + th.nr('prozent_bedeutung')); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  let a = await finde(th, p);
  await gibEin(p, a, `${String(a.o.wert)} €`); await pruefe(p); await bild(p, 'r3-einheit-handy', true);
  const r3a = await p.locator('.lr-rueck').first().innerText();
  await weiter(p); a = await finde(th, p);
  await gibEin(p, a, String(a.o.wert / 100).replace('.', ',')); await pruefe(p); await bild(p, 'r3-dezimal-statt-prozent-handy', true);
  PROTOKOLL.r3 = { log, einheit: r3a, dezimal: await p.locator('.lr-rueck').first().innerText() };
});

// R4: Tipp benutzen, dann richtig – was sieht das Kind?
lauf('R4 Tipp', async (p) => {
  const th = thema('zahlen.ganz', ['betrag']); const { log } = await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/1-1-ueben-' + th.nr('betrag')); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const a = await finde(th, p);
  await p.getByRole('button', { name: 'Tipp' }).click(); await p.waitForTimeout(200);
  await gibEin(p, a, richtigWert(a)); await pruefe(p); await bild(p, 'r4-tipp-richtig-handy', true);
  PROTOKOLL.r4 = { log, punkte: await p.locator('.lr-lk-punkte').first().innerText() };
});

// R5: Klasse 8, Funktionsterm aufstellen (Lücken) – Steigung und Achsenabschnitt vertauscht
lauf('R5 Kl. 8 vertauscht', async (p) => {
  const th = thema('funktionen.linear', ['aufstellen']); const { log } = await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/2-1-ueben-' + th.nr('aufstellen')); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const a = await finde(th, p); assert.equal(a.y, 'luecken');
  await gibEin(p, a, [...a.o.werte].reverse()); await pruefe(p); await bild(p, 'r5-kl8-vertauscht-handy', true);
  // zweimal falsch hintereinander: ändert sich etwas?
  await weiter(p); const b = await finde(th, p); await gibEin(p, b, [...b.o.werte].reverse()); await pruefe(p);
  await bild(p, 'r5-kl8-zweiter-fehler-handy', true);
  PROTOKOLL.r5 = { log, rueck1: a.f.text, rueck2: await p.locator('.lr-rueck').first().innerText() };
}, 'nacht');

// R6: Auswahl falsch (Kl. 8, lage)
lauf('R6 Auswahl falsch', async (p) => {
  const th = thema('funktionen.linear', ['lage']); const { log } = await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/2-1-ueben-' + th.nr('lage')); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const a = await finde(th, p); await gibEin(p, a, (a.o.index + 1) % a.a.length); await pruefe(p);
  await bild(p, 'r6-auswahl-falsch-handy', true);
  PROTOKOLL.r6 = { log, optionen: a.a, gewaehlt: a.a[(a.o.index + 1) % a.a.length], rueck: await p.locator('.lr-rueck').first().innerText() };
}, 'nacht');

// R7: Wiederholung falsch – Meldung vs. was danach passiert
lauf('R7 Wiederholung falsch', async (p) => {
  const th = thema('zahlen.ganz', ['deuten']); const { log } = await einrichten(p, th, { wiederholung: 'deuten', etappen: { deuten: { sitzt: true, fertig: true } } });
  await p.goto(H.origin + '/#/wiederholen/1'); await warte(p);
  const a = await finde(th, p); await gibEin(p, a, '999'); await pruefe(p);
  await p.getByRole('button', { name: 'Fertig' }).click(); await p.waitForTimeout(300);
  await bild(p, 'r7-wiederholung-falsch-handy', true);
  PROTOKOLL.r7 = { log, ende: await p.locator('.lr-geschafft').innerText() };
});

// R8: Tablet – wo steht die Rückmeldung nach dem Prüfen?
lauf('R8 Tablet Rückmeldung', async (p) => {
  await p.setViewportSize({ width: 820, height: 1180 });
  const th = thema('zahlen.ganz', ['addieren']); await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/1-1-ueben-' + th.nr('addieren')); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const a = await finde(th, p); await gibEin(p, a, String(-a.o.wert)); await pruefe(p); await p.waitForTimeout(500);
  await bild(p, 'r8-tablet-falsch');
  PROTOKOLL.r8 = await p.evaluate(() => { const r = document.querySelector('.lr-rueck'); const b = r?.getBoundingClientRect(); return { rueckOben: Math.round(b?.top ?? -1), rueckUnten: Math.round(b?.bottom ?? -1), fenster: innerHeight }; });
});

// R9: Gefärbte Flächen in Aufgaben (Hunderterfeld) – wie gut sichtbar? hell und dunkel
for (const g of ['tag', 'nacht']) lauf('R9 Fläche sichtbar ' + g, async (p) => {
  const th = thema('bruch.prozent', ['prozent_bedeutung']); th.auf.sort((a, b) => (b.f.text.includes('Hunderterfeld') ? 1 : 0) - (a.f.text.includes('Hunderterfeld') ? 1 : 0));
  await einrichten(p, th);
  await p.goto(H.origin + '/#/lerneinheit/1-1-ueben-' + th.nr('prozent_bedeutung')); await warte(p);
  const v = p.getByRole('button', { name: /Verstanden/ }); if (await v.count()) await v.click();
  const svg = p.locator('.lr-aufgabe svg').first(); await svg.scrollIntoViewIfNeeded();
  await svg.screenshot({ path: path.join(AUS, `r9-flaeche-${g}.png`) });
  (PROTOKOLL.r9 ||= {})[g] = await p.evaluate(() => {
    const f = document.querySelector('.lr-aufgabe svg .flaeche'); const s = getComputedStyle(f);
    let el = f.closest('svg'); let bg = 'rgba(0, 0, 0, 0)'; while (el && (bg === 'rgba(0, 0, 0, 0)' || bg === 'transparent')) { bg = getComputedStyle(el).backgroundColor; el = el.parentElement; }
    return { fill: s.fill, opacity: s.fillOpacity, hintergrund: bg };
  });
}, g);

test('Protokoll schreiben', () => fs.writeFileSync(path.join(__dirname, 'protokoll.json'), JSON.stringify(PROTOKOLL, null, 1)));
