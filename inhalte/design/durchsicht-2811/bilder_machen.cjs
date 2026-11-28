// Durchsicht 28.11.: Bildschirmfotos jeder Seite der Lern-App für den Designer.
// Nutzt die erfundenen Beispieldaten und den Server-Nachbau aus tests/lernen.test.cjs (die Testdatei wird nur gelesen, nicht verändert):
// Die Datei wird mit leeren Test-Funktionen geladen; setup(), exServer(), rkServer(), wwServer() … stehen danach zur Verfügung.
// Aufruf:  node inhalte/design/durchsicht-2811/bilder_machen.cjs [Filter]     (Filter = Teil eines Seitennamens)
// Umgebung: PW_TEST_EXECUTABLE = Pfad zu Chromium, NODE_PATH/PLAYWRIGHT_DIR = Ordner mit node_modules/playwright
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { createRequire } = require('node:module');

const WURZEL = path.resolve(__dirname, '..', '..', '..');
const TESTDATEI = path.join(WURZEL, 'tests', 'lernen.test.cjs');
const AUS = path.join(__dirname, 'bilder');
const PW_DIR = process.env.PLAYWRIGHT_DIR || '/home/claude/ki-system';
const CHROME = process.env.PW_TEST_EXECUTABLE || '/opt/pw-browsers/chromium-1243/chrome-linux64/chrome';
process.env.PW_TEST_EXECUTABLE = CHROME;

// ---- Testdatei laden (ohne Tests auszuführen) ----
const echtRequire = createRequire(path.join(PW_DIR, 'x.js'));
const haken = { before: [], after: [] };
const fakeTest = Object.assign(() => {}, {});
const requireStub = (n) => (n === 'node:test' ? { test: fakeTest, before: (f) => haken.before.push(f), after: (f) => haken.after.push(f) } : n === 'playwright' ? echtRequire('playwright') : require(n));
let quelle = fs.readFileSync(TESTDATEI, 'utf8');
quelle += '\n;module.exports = { ev: (c) => eval(c) };';
const modul = { exports: {} };
new Function('require', 'module', 'exports', '__dirname', quelle)(requireStub, modul, modul.exports, path.dirname(TESTDATEI));
const T = modul.exports; // T.ev('setup') usw.

const nachlauf = [];
const fakeT = { after: (f) => nachlauf.push(f) };
const log = (...a) => console.log(...a);
const BREITEN = [[390, 844, 'hell'], [390, 844, 'dunkel'], [1280, 800, 'hell'], [1280, 800, 'dunkel']];

async function starten() {
  for (const f of haken.before) await f();
  return { origin: T.ev('origin'), setup: T.ev('setup') };
}
async function beenden() { for (const f of nachlauf.splice(0)) { try { await f(); } catch { /* egal */ } } for (const f of haken.after) await f(); }

// ---- Foto-Hilfen ----
// Ansichten, die den ganzen Bildschirm festhalten (position: fixed) – dort zeigt fullPage nur Leere unter der Ansicht, darum nur der sichtbare Bildschirm
const UEBERLAGERT = /^(landung-|etappe-abgelegt|expedition-freigeschaltet|reisekarte-menue|einstellen)/;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const ERGEBNIS = []; // { nr, seite, adresse, dateien[], bemerkung }
let ctx = null; // { origin, setup }
const fehlerListe = [];

// Eine Fassung aufnehmen: neue Sitzung, Größe/Farbschema setzen, vorbereiten, fotografieren.
async function fassung({ nr, name, adresse, opt = {}, vor, breiten = BREITEN }) {
  const dateien = [];
  for (const [b, h, fb] of breiten) {
    const dunkel = fb === 'dunkel';
    const o = { gestaltung: dunkel ? 'nacht' : 'tag', rolle: 'kind', lernSeite: true, ...(typeof opt === 'function' ? opt(dunkel, b) : opt) };
    const ohneToken = o.ohneToken; delete o.ohneToken;
    const { page, calls } = await ctx.setup(fakeT, o);
    if (o.lernSeite && !ohneToken) await page.context().addInitScript(() => { localStorage.setItem('lern_token', 't'.repeat(64)); });
    if (process.env.DBG) { page.on('framenavigated', (f) => log('  nav', f.url())); page.on('console', (m) => log('  con', m.text().slice(0, 150))); }
    page.on('pageerror', (e) => fehlerListe.push(`${nr}-${name}-${b}-${fb}: ${e.message}`));
    await page.setViewportSize({ width: b, height: h });
    await page.emulateMedia({ colorScheme: dunkel ? 'dark' : 'light', reducedMotion: 'reduce' });
    try {
      await vor(page, { b, dunkel, calls, origin: ctx.origin + (o.lernSeite ? '/lernen/' : '/') });
      await page.waitForTimeout(700);
      const datei = `${nr}-${name}-${b}-${fb}.jpg`;
      await page.screenshot({ path: path.join(AUS, datei), fullPage: !UEBERLAGERT.test(name), type: 'jpeg', quality: 80 });
      dateien.push(datei);
    } catch (e) { try { fs.mkdirSync('/tmp/fehler', { recursive: true }); await page.screenshot({ path: `/tmp/fehler/${nr}-${name}-${b}-${fb}.png` }); fs.writeFileSync(`/tmp/fehler/${nr}-${name}-${b}-${fb}.txt`, (await page.locator('body').innerText()).slice(0, 1500) + '\n' + page.url()); } catch { /* egal */ }
      log('  FEHLER', nr, name, b, fb, e.message.split('\n')[0]); fehlerListe.push(`${nr}-${name}-${b}-${fb}: ${e.message.split('\n')[0]}`); }
    for (const f of nachlauf.splice(0)) { try { await f(); } catch { /* egal */ } }
    await page.context().close().catch(() => {});
  }
  log(nr, name, dateien.length + '/' + breiten.length);
  return dateien;
}
const gehe = (hash, warte) => async (page, { origin }) => { await page.goto(origin + '#/' + hash); if (warte) await warte(page); };
const seiten = [];
const S = (nr, name, adresse, bemerkung, def) => seiten.push({ nr, name, adresse, bemerkung, ...def });

// ======================= Seiten =======================
const warteAuf = (sel) => (page) => page.locator(sel).first().waitFor({ timeout: 8000 });
const LEHRER = { rolle: 'lehrer' };
const ELTERN = { rolle: 'eltern' };

// 1 Anmeldung (nicht angemeldet)
S('01', 'anmeldung', 'lernen/ (ohne Anmeldung)', 'Lernen-Seite, Lern-Code-Anmeldung', { opt: { ohneToken: true }, vor: async (page, { origin }) => { await page.goto(origin); await page.getByLabel('Lern-Code').waitFor(); } });
S('01b', 'anmeldung-hauptapp', 'login (KI-System)', 'Anmeldung der Haupt-App (Passwort), nicht die Lernen-Seite', { opt: { lernSeite: false, rolle: 'eltern' }, vor: async (page, { origin }) => { await page.goto(origin + '#/login'); await page.locator('input').first().waitFor(); } });

// 2 Lehrer-Startseite
S('02', 'lehrer-start', '#/ (= #/lernen)', 'Startseite „Was ist los?“', { opt: LEHRER, vor: gehe('lernen', warteAuf('.lern-zutun')) });

// ---- Nachbauten zusammensetzen ----
const kette = (...fs) => { const f = (a, e, d) => { let r = e; for (const g of fs) { if (!g) continue; const x = g(a, r, d); if (x !== null && x !== undefined) r = x; } return r ?? null; }; f.neueAktionen = true; return f; };
const ev = (n) => T.ev(n);
const exAnp = () => ev('exServer')().anpassen;
const rkAnp = (o = {}) => ev('rkServer')(o).anpassen;
const rkExAnp = (o = {}) => ev('rkServer')({ basis: exAnp(), ...o }).anpassen;
const tasten = async (page, z) => { const tf = page.getByRole('group', { name: 'Tastenfeld' }); for (const c of String(z)) await tf.getByRole('button', { name: c, exact: true }).click(); };
const pruefen = (page) => page.getByRole('group', { name: 'Tastenfeld' }).getByRole('button', { name: 'Prüfen' }).click();
const losDann = async (page) => { await page.getByText(/BORDKARTE 1 · ROM/).waitFor(); const v = page.getByRole('button', { name: 'Verstanden – los' }); if (await v.count()) await v.click(); };
const oeffneAlles = (page) => page.evaluate(() => document.querySelectorAll('#main details').forEach((d) => { d.open = true; }));
const KIND = (anpassen) => ({ rolle: 'kind', ...(anpassen ? { anpassen } : {}) });
const kindRk = (o) => () => ({ rolle: 'kind', anpassen: rkAnp(o) });
const kindRkEx = (o) => () => ({ rolle: 'kind', anpassen: rkExAnp(o) });

// 3 Reisekarte
S('03', 'reisekarte', '#/reise/1', 'Reisekarte Europa mit Pins und Startknopf (Nachbau rkServer)', { opt: kindRk(), vor: gehe('reise/1', warteAuf('.rk .rk-pin')) });
S('03b', 'reisekarte-menue', '#/reise/1 + Menü', 'Reisekarte, Menüblatt (≡) geöffnet', { opt: kindRk(), vor: async (page, { origin }) => { await page.goto(origin + '#/reise/1'); await page.locator('.rk .rk-pin').first().waitFor(); await page.locator('.rk-menue').click(); await page.locator('dialog.lr-blatt[open]').waitFor(); } });
S('03c', 'abflugtafel', '#/reise/1 (ohne Kartendaten)', 'Abflugtafel (erscheint nur, wenn der Server keine Kartendaten liefert); Abschnitte „Später – für höhere Klassen“ und „Was kommt wann wieder?“ eingeklappt', { opt: KIND(), vor: gehe('reise/1', warteAuf('.lr-flug-jetzt')) });
S('03d', 'abflugtafel-aufgeklappt', '#/reise/1 (ohne Kartendaten)', 'Abflugtafel, alle aufklappbaren Abschnitte offen (der Abschnitt „Auch offen“ erscheint nur bei mehreren gleichzeitig offenen Orten – im Nachbau nicht erreichbar)', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/reise/1'); await page.locator('.lr-flug-jetzt').first().waitFor(); await oeffneAlles(page); } });
S('03e', 'abflugtafel-checkin', '#/reise/1 (Check-in fällig)', 'Abflugtafel mit Ansage „Vorher kurz einchecken“ (Nachbau wdhServer)', { opt: KIND(), vor: async (page, { origin }) => { const srv = ev('wdhServer')({ runde: 9, faellig: 41 }); await page.route('**/functions/v1/lernen-api/**', srv.route); await page.goto(origin + '#/reise/1'); await page.locator('.lr-checkin-ansage').waitFor(); } });

S('03f', 'expedition-freigeschaltet', '#/reise/1 (Expedition neu)', 'Ansicht „Expedition freigeschaltet“ beim Öffnen der Reisekarte', { opt: kindRkEx(), vor: gehe('reise/1', async (p) => { await p.getByText('EXPEDITION', { exact: false }).first().waitFor(); }) });

// 4 Mein Weg
for (const [n, adr, bem] of [['04a', 'weg/1', 'Mein Weg · Reiter Stand'], ['04b', 'weg/1-kontinente', 'Mein Weg · Reiter Kontinente'], ['04c', 'weg/1-karte', 'Mein Weg · Reiter Karte']])
  S(n, 'weg-' + adr.replace('weg/1', 'stand').replace('stand-', ''), '#/' + adr, bem, { opt: kindRk(), vor: gehe(adr, async (p) => { await p.waitForTimeout(800); }) });

// 5 weitere Kinderseiten
S('05a', 'reisepass', '#/reisepass/1', 'Reisepass', { opt: kindRkEx(), vor: gehe('reisepass/1', async (p) => { await p.waitForTimeout(500); }) });
S('05b', 'route', '#/route/1', 'Meine Route 5–10 (Nachbau lmsAnpassen, Kindsicht). Aufgenommen in der Haupt-App (KI-System), weil die Lernen-Seite mit Kinder-Code #/route auf die Reisekarte umleitet (route fehlt in KIND_ANSICHTEN in lernen/schule.js)', { opt: () => ({ rolle: 'kind', lernSeite: false, anpassen: kette(ev('lmsAnpassen')()) }), vor: async (page, { origin }) => { await page.route('**/functions/v1/lernen-api/**', ev('rtMock')()); await page.goto(origin + '#/route/1'); await page.locator('.rt-chip').first().waitFor(); } });
S('05c', 'wiederholen', '#/wiederholen/1', 'Wiederholen = Check-in, Bordkarte 1 von 3', { opt: KIND(), vor: async (page, { origin }) => { const srv = ev('wdhServer')({ runde: 3, faellig: 9 }); await page.route('**/functions/v1/lernen-api/**', srv.route); await page.goto(origin + '#/wiederholen/1'); await page.getByText('CHECK-IN · 1 VON 3').waitFor(); } });
S('05d', 'stationen', '#/stationen/1', 'Expeditionen: Stempel-Sammlung', { opt: kindRkEx(), vor: gehe('stationen/1', async (p) => { await p.waitForTimeout(600); }) });
S('05e', 'expedition', '#/expedition/1-7', 'Einzelne Expedition „Die Wetterstation“, Teil a offen', { opt: kindRkEx(), vor: gehe('expedition/1-7', async (p) => { await p.waitForTimeout(600); }) });
S('05f', 'merkheft', '#/merkheft/1', 'Merkheft', { opt: KIND(), vor: gehe('merkheft/1', async (p) => { await p.waitForTimeout(600); }) });
S('05g', 'merkheft-offen', '#/merkheft/1 (aufgeklappt)', 'Merkheft, alle Einträge aufgeklappt', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/merkheft/1'); await page.waitForTimeout(800); await oeffneAlles(page); } });


// 6 Lerneinheit in allen erreichbaren Zuständen (Kind, Einheit 1 = Rom · Natürliche Zahlen)
const ueb1 = async (page, origin, nr = 1) => { await page.goto(origin + '#/lerneinheit/1-1-ueben-' + nr); await losDann(page); };
S('06a', 'einheit-start', '#/lerneinheit/1-1', 'Lerneinheit: Etappen-Weg / Start', { opt: KIND(), vor: gehe('lerneinheit/1-1', async (p) => { await p.waitForTimeout(800); }) });
S('06b', 'einheit-erklaerung', '#/lerneinheit/1-1-erklaeren-1', 'Erklärung der Etappe 1', { opt: KIND(), vor: gehe('lerneinheit/1-1-erklaeren-1', async (p) => { await p.waitForTimeout(800); }) });
S('06b2', 'einheit-erklaerung-2', '#/lerneinheit/1-1-erklaeren-2', 'Erklärung der Etappe 2 (mit Zahlenstrahl-Bild)', { opt: KIND(), vor: gehe('lerneinheit/1-1-erklaeren-2', async (p) => { await p.waitForTimeout(800); }) });
S('06c', 'aufgabe-offen', '#/lerneinheit/1-1-ueben-1', 'Bordkarte (Aufgabe) offen, Zahl mit Tastenfeld', { opt: KIND(), vor: async (page, { origin }) => { await ueb1(page, origin); } });
S('06c2', 'aufgabe-zahlenstrahl', '#/lerneinheit/1-1-ueben-2', 'Bordkarte mit Zahlenstrahl (Markierung)', { opt: KIND(), vor: async (page, { origin }) => { await ueb1(page, origin, 2); } });
S('06c3', 'aufgabe-luecken', '#/lerneinheit/1-1-ueben-3', 'Bordkarte mit Lücken (Binomische Formeln)', { opt: KIND(), vor: async (page, { origin }) => { await ueb1(page, origin, 3); } });
S('06d', 'aufgabe-tipp', '#/lerneinheit/1-1-ueben-1 + Tipp', 'Tipp gezeigt', { opt: KIND(), vor: async (page, { origin }) => { await ueb1(page, origin); await page.getByRole('button', { name: /Tipp/ }).first().click(); await page.locator('.lr-tipp').waitFor(); } });
S('06e', 'aufgabe-richtig', '#/lerneinheit/1-1-ueben-1 + richtig', 'Richtig beantwortet („An Bord“)', { opt: KIND(), vor: async (page, { origin }) => { await ueb1(page, origin); await tasten(page, '2000'); await pruefen(page); await page.getByText(/An Bord/).waitFor(); } });
S('06f', 'aufgabe-falsch-1', '#/lerneinheit/1-1-ueben-1 + falsch (1. Versuch)', 'Falsch beantwortet, Hinweis zum Fehlermuster, zweiter Versuch', { opt: KIND(), vor: async (page, { origin }) => { await ueb1(page, origin); await tasten(page, '200'); await pruefen(page); await page.getByText('Noch nicht – du hast einen zweiten Versuch.').waitFor(); } });
S('06g', 'aufgabe-falsch-erklaert', '#/lerneinheit/1-1-ueben-1 + falsch (2. Versuch)', 'Falsch beantwortet mit Lösung und Erklärung („Kurskorrektur“)', { opt: KIND(), vor: async (page, { origin }) => { await ueb1(page, origin); await tasten(page, '200'); await pruefen(page); await page.getByText('Noch nicht – du hast einen zweiten Versuch.').waitFor(); await pruefen(page); await page.getByText('FAST – KURSKORREKTUR').waitFor(); } });
S('06h', 'landung-direkt', '#/lerneinheit/1-1-ueben-1 (gelandet, Direktflug)', 'Landung Etappe: Direktflug (Sterne, Abzeichen)', { opt: () => ({ rolle: 'kind', anpassen: kette(ev('abLandung')('direkt', { bordkarten: 2 })) }),
  vor: async (page, { origin }) => { await ueb1(page, origin); await ev('landeEtappe1')(page); const k = page.getByRole('button', { name: 'Heute keine Knobel-Bordkarte' }); if (await k.count()) await k.click(); await page.locator('.lr-abschluss-etappe').waitFor(); } });
S('06i', 'landung-sauber', '#/lerneinheit/1-1-ueben-1 (gelandet, saubere Landung)', 'Landung Etappe: saubere Landung', { opt: () => ({ rolle: 'kind', anpassen: ev('abLandung')('sauber', { bordkarten: 8, eigene_loesungen: 6 }) }),
  vor: async (page, { origin }) => { await ueb1(page, origin); await ev('landeEtappe1')(page); const k = page.getByRole('button', { name: 'Heute keine Knobel-Bordkarte' }); if (await k.count()) await k.click(); await page.locator('.lr-abschluss-etappe').waitFor(); } });
S('06j', 'landung-sturm', '#/lerneinheit/1-1-ueben-1 (gelandet, Sturmflug)', 'Landung Etappe: Sturmflug gemeistert', { opt: () => ({ rolle: 'kind', anpassen: ev('abLandung')('sturm', { bordkarten: 15, fehler_endgueltig: 6, stufe_gesenkt: 2 }) }),
  vor: async (page, { origin }) => { await ueb1(page, origin); await ev('landeEtappe1')(page); await page.locator('.lr-abschluss-etappe').waitFor(); } });
S('06k', 'knobel-bordkarte', '#/lerneinheit/1-1-ueben-1 (nach Landung)', 'Knobel-Bordkarte nach der Etappe (Aufgabe offen)', { opt: () => ({ rolle: 'kind', anpassen: kette(ev('mitBonus'), ev('abLandung')('sauber')) }),
  vor: async (page, { origin }) => { await ueb1(page, origin); await ev('landeEtappe1')(page); await page.locator('.lr-knobel .lr-stufe-bonus').waitFor(); } });
S('06k2', 'knobel-geloest', '#/lerneinheit/1-1-ueben-1 (Knobel gelöst)', 'Knobel-Bordkarte richtig gelöst (+30 Sterne)', { opt: () => ({ rolle: 'kind', anpassen: kette(ev('mitBonus'), ev('abLandung')('sauber')) }),
  vor: async (page, { origin }) => { await ueb1(page, origin); await ev('landeEtappe1')(page); await page.locator('.lr-knobel .lr-stufe-bonus').waitFor(); await page.locator('.lr-knobel input').fill('100'); await page.locator('.lr-knobel').getByRole('button', { name: 'Prüfen' }).click(); await page.getByText('+30 Sterne · ein Knobel-Stern').waitFor(); } });
S('06l', 'mischkarte', '#/lerneinheit/1-1-ueben-1 (Mischkarte)', 'Mischkarte „Aus deiner Reise“ (Wiederholung aus anderem Flug), Aufgabe offen', { opt: () => ({ rolle: 'kind', anpassen: kette((a, e) => { if (a !== 'schule_einheit_lesen') return null; const x = ev('neueRegel')({ strahl: { sitzt: true } })(a, e);
    x.mischkarten = [{ ...ev('zeig')(ev('AUFG')[14]), stufe: 2, einheit_id: 2, quelle: 'aelter', stadt: 'New York', etappe: 'Große Zahlen lesen' }]; x.misch_jede = 1; x.misch_ab = 1; return x; }) }),
  vor: async (page, { origin }) => { await page.goto(origin + '#/lerneinheit/1-1-ueben-1'); await page.getByText('BORDKARTE 1 · AUS DEINER REISE').waitFor(); } });
S('06m', 'checkin-bordkarte', '#/wiederholen/1', 'Bordkarten-Check-in (Wiederholung), Bordkarte 2 von 3 nach Fehler (Koffer-Leiste)', { opt: KIND(), vor: async (page, { origin }) => { const srv = ev('wdhServer')({ runde: 3, faellig: 9 }); await page.route('**/functions/v1/lernen-api/**', srv.route); let n = 0; srv.antwort = () => { n++; return { ok: true, format_ok: true, richtig: true, loesung: { wert: 2000 }, wiederholung: { bestanden: true, sterne: 10, naechste_in: 7 } }; };
  await page.goto(origin + '#/wiederholen/1'); await page.getByText('CHECK-IN · 1 VON 3').waitFor(); await ev('wdhRichtig')(page); await page.locator('.lr-plus-stern').waitFor(); } });
S('06m2', 'checkin-fertig', '#/wiederholen/1 (Eingecheckt)', 'Check-in geschafft: „Eingecheckt!“', { opt: KIND(), vor: async (page, { origin }) => { const srv = ev('wdhServer')({ runde: 3, faellig: 9 }); await page.route('**/functions/v1/lernen-api/**', srv.route); srv.antwort = () => ({ ok: true, format_ok: true, richtig: true, loesung: { wert: 2000 }, wiederholung: { bestanden: true, sterne: 10, naechste_in: 7 } });
  await page.goto(origin + '#/wiederholen/1'); await page.getByText('CHECK-IN · 1 VON 3').waitFor();
  for (let i = 0; i < 3; i++) { await ev('wdhRichtig')(page); await page.locator('.lr-plus-stern').waitFor(); await page.getByRole('button', { name: /Nächste Bordkarte|Fertig/ }).click(); }
  await page.getByRole('heading', { name: 'Eingecheckt!' }).waitFor(); } });
S('06n', 'etappe-abgelegt', '#/wiederholen/1 (Etappe abgelegt)', 'Blatt „Etappe abgelegt“ nach einer Wiederholung', { opt: KIND(), vor: async (page, { origin }) => { const srv = ev('wdhServer')({ runde: 2, faellig: 2 }); await page.route('**/functions/v1/lernen-api/**', srv.route);
  srv.antwort = () => ({ ok: true, format_ok: true, richtig: true, loesung: { wert: 2000 }, wiederholung: { bestanden: true, sterne: 10 }, abgelegt: { etappe: { titel: 'Welchen Wert hat eine Ziffer?', sterne: 30, flug: 'Natürliche Zahlen', etappen_abgelegt: 4, etappen: 7 } } });
  await page.goto(origin + '#/wiederholen/1'); await page.getByText(/CHECK-IN/).waitFor(); await ev('wdhRichtig')(page); await page.getByRole('dialog', { name: 'Etappe abgelegt' }).waitFor(); } });
S('06o', 'test-start', '#/lerneinheit/1-1-test', 'Flug-Test: Start', { opt: KIND(), vor: gehe('lerneinheit/1-1-test', async (p) => { await p.getByRole('button', { name: 'Test starten' }).waitFor(); }) });
S('06p', 'test-frage', '#/lerneinheit/1-1-test (Frage)', 'Flug-Test: Frage offen', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/lerneinheit/1-1-test'); await page.getByRole('button', { name: 'Test starten' }).click(); await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').waitFor(); } });
S('06q', 'test-ergebnis', '#/lerneinheit/1-1-test (Ergebnis)', 'Flug-Test: Auswertung (1 von 2 richtig)', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/lerneinheit/1-1-test'); await page.getByRole('button', { name: 'Test starten' }).click(); await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click(); await page.getByRole('button', { name: 'Weiter ›' }).click(); await page.getByRole('button', { name: 'Markierung 2' }).click(); await page.getByRole('button', { name: 'Abgeben' }).click(); await page.getByText('1 von 2 richtig').waitFor(); } });
const testBestanden = (opt) => async (page, { origin }) => { await page.goto(origin + '#/lerneinheit/1-1-test'); await page.getByRole('button', { name: 'Test starten' }).click(); await page.getByText('elf Millionen vierhundertneunzigtausendeinundfünfzig').click(); await page.getByRole('button', { name: 'Weiter ›' }).click(); await page.getByRole('button', { name: 'Markierung 2' }).click(); await page.getByRole('button', { name: 'Abgeben' }).click(); await page.locator('.lr-abschluss-flug').waitFor(); return page; };
S('06r', 'landung-flug', '#/lerneinheit/1-1-test (Flug geschafft)', 'Landung Flug: „Flug geschafft“ mit Sternen', { opt: () => ({ rolle: 'kind', anpassen: ev('abFlug')({}) }), vor: testBestanden() });
S('06s', 'landung-flug-naechstes', '#/lerneinheit/1-1-test (Bordkarte nächstes Thema)', 'Bordkarte zum nächsten Thema nach „Flug geschafft“', { opt: () => ({ rolle: 'kind', anpassen: ev('abFlug')({}) }), vor: async (page, o) => { await testBestanden()(page, o); await page.locator('.lr-abschluss-flug').getByRole('button', { name: /Weiter zum nächsten Thema/ }).click(); await page.locator('.lr-abschluss-bordkarte').waitFor(); } });
S('06t', 'landung-ort-stempel', '#/lerneinheit/1-1-test (Ort geschafft, Stempel)', 'Landung Ort: Reisepass-Stempel „Rom ist geschafft“', { opt: () => ({ rolle: 'kind', anpassen: ev('abFlug')({ ortGeschafft: true, naechster: 'anders' }) }), vor: async (page, o) => { await testBestanden()(page, o); await page.locator('.lr-abschluss-flug').getByRole('button', { name: 'Überspringen ›' }).click(); await page.locator('.lr-abschluss-ort').waitFor(); } });
S('06u', 'landung-ort-bordkarte', '#/lerneinheit/1-1-test (Bordkarte neuer Ort)', 'Bordkarte „Von Rom nach Athen“', { opt: () => ({ rolle: 'kind', anpassen: ev('abFlug')({ ortGeschafft: true, naechster: 'anders' }) }), vor: async (page, o) => { await testBestanden()(page, o); await page.locator('.lr-abschluss-flug').getByRole('button', { name: 'Überspringen ›' }).click(); await page.locator('.lr-abschluss-ort .lr-ab-gross').click(); await page.locator('.lr-abschluss-bordkarte').waitFor(); } });


// 7 Regel-Universum (Kind)
const ruWarte = (sel) => async (p) => { await p.locator(sel).first().waitFor(); };
const RU = (nr, name, adr, bem, def = {}) => S(nr, name, '#/regeln/1-' + adr, bem, { opt: def.opt || KIND(), vor: def.vor || gehe('regeln/1-' + adr, ruWarte(def.warte || '.ru-seite')) });
RU('07a', 'universum-aufbau', 'universum', 'Regel-Universum: Sonnensystem „Aufbau“ (mit Link „Mein Merkheft“)', { warte: '.ru-universum' });
RU('07b', 'universum-klassen', 'klassen', 'Regel-Universum: „Durch die Klassen“', { warte: '.ru-klassen-ansicht' });
RU('07c', 'gebiet', 'gebiet-fur', 'Ein Gebiet (Fläche und Raum) mit „Auf einen Blick“-Tafeln', { warte: '.ru-ideen1' });
RU('07d', 'arbeitsweisen', 'weisen', 'Arbeitsweisen', { warte: '.ru-ideen1' });
RU('07e', 'idee', 'idee-fur-2', 'Eine Idee/Regelseite (Stufen)', { warte: '.ru-regelseite' });
S('07e2', 'einzelregel', '#/regeln/1-regel-f<n>', 'Einzelne Regel (Ebene 3), erreicht über Idee → Folge → erste Karte', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/regeln/1-idee-fur-2'); await page.locator('.ru-regelseite').waitFor(); await page.locator('.ru-stufe[data-stufe="folge"] > summary').click(); await page.locator('.ru-folge .ru-karte').first().click(); await page.locator('.ru-r-kopf .ru-ueber', { hasText: /^Regel F\d+/ }).waitFor(); } });
['formeln', 'einheiten', 'formeln-flaechen', 'formeln-koerper', 'zahlen', 'stellenwert', 'bruch-dezimal-prozent', 'figuren', 'zeichen-woerter'].forEach((id, i) =>
  S('07f' + (i + 1), 'tafel-' + id, '#/regeln/1-tafel-' + id, 'Tafel ' + id, { opt: KIND(), vor: gehe('regeln/1-tafel-' + id, async (p) => { await p.locator(`.ru-tafel-seite[data-tafel="${id}"]`).waitFor(); }) }));
S('07f10', 'tafel-formeln-zeile-offen', '#/regeln/1-tafel-formeln (Zeile Kreis aufgeklappt)', 'Formeln auf einen Blick mit aufgeklappter Zeile „Kreis“', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/regeln/1-tafel-formeln'); await page.locator('#ru-tf-kreis').waitFor(); await page.locator('#ru-tf-kreis .ru-tafel-auf').click(); await page.locator('#ru-tf-kreis .ru-tafel-detail').waitFor(); } });
S('07f11', 'tafel-einheiten-offen', '#/regeln/1-tafel-einheiten (alles aufgeklappt)', 'Maßeinheiten, alle Abschnitte aufgeklappt', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/regeln/1-tafel-einheiten'); await page.locator('.ru-tafel-seite[data-tafel="einheiten"]').waitFor(); await page.evaluate(() => { document.querySelectorAll('.ru-tafel-seite details').forEach((d) => { d.open = true; }); document.querySelectorAll('.ru-tafel-auf[aria-expanded="false"]').forEach((k) => k.click()); }); } });
S('07g', 'suche-cm', '#/regeln/1-suche („cm“)', 'Suche mit Treffern für „cm“ (Tafel zuerst)', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/regeln/1-universum'); await page.locator('.ru-suche input').waitFor(); await page.locator('.ru-suche input').fill('cm'); await page.locator('.ru-suche input').press('Enter'); await page.locator('.ru-treffer .ru-karte').first().waitFor(); } });
S('07g2', 'suche-kegelmantel', '#/regeln/1-suche („Kegelmantel“)', 'Suche mit Treffern für „Kegelmantel“', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/regeln/1-universum'); await page.locator('.ru-suche input').waitFor(); await page.locator('.ru-suche input').fill('Kegelmantel'); await page.locator('.ru-treffer .ru-karte').first().waitFor(); } });
S('07h', 'regeln-aendern-lassen', '#/regeln/kind-tafel-einheiten (Ändern lassen)', 'Erwachsene sehen die Kind-Ansicht; „Ändern lassen“ an der Tafel geöffnet', { opt: { rolle: 'lehrer' }, vor: async (page, { origin }) => { await page.goto(origin + '#/regeln/kind-tafel-einheiten'); await page.locator('.ru-tafel-seite').waitFor(); await page.locator('.ru-tafel-kopf .ru-ae').click(); await page.locator('.ru-rueck-form').waitFor(); } });
S('07i', 'regeln-liste-lehrer', '#/regeln', 'Lehrer-/Eltern-Liste aller Regeln und Arbeitsweisen', { opt: { rolle: 'lehrer' }, vor: gehe('regeln', ruWarte('.ru-lehrer')) });
S('07j', 'regeln-lehrer-regelblatt', '#/regeln/lehrer-r6', 'Lehrer: Blatt einer Rechenregel (alle Stufen offen)', { opt: { rolle: 'lehrer' }, vor: gehe('regeln/lehrer-r6', async (p) => { await p.waitForTimeout(800); }) });

// 8 Lehrer
const LM = () => ({ rolle: 'lehrer', anpassen: kette(ev('lmsAnpassen')(), ev('wwServer')().anpassen) });
S('08a', 'kind-ueberblick', '#/kind/1-ueberblick', 'Lehrer: Kind-Ansicht, Reiter Überblick', { opt: LM, vor: gehe('kind/1-ueberblick', ruWarte('.lw-ue')) });
S('08b', 'kind-wackelt', '#/kind/1-wackelt', 'Lehrer: Reiter „Was wackelt“ (neue Ansicht mit Auswertung)', { opt: LM, vor: gehe('kind/1-wackelt', async (p) => { await p.locator('.ww .ww-kachel').first().waitFor(); }) });
S('08c', 'kind-wackelt-besprochen', '#/kind/1-wackelt (Besprochen)', 'Was wackelt, alle Themen aufgeklappt und etwas unter „Besprochen“ (Nachbau wwServer, vorher besprochen)', { opt: LM, vor: async (page, { origin }) => { await page.goto(origin + '#/kind/1-wackelt'); await page.locator('.ww .ww-kachel').first().waitFor(); await page.evaluate(() => { document.querySelectorAll('.ww details').forEach((d) => { d.open = true; }); document.querySelectorAll('.ww-th-titel[aria-expanded="false"]').forEach((k) => k.click()); }); } });
S('08d', 'kind-lehrplan', '#/kind/1-lehrplan', 'Lehrer: Kind-Ansicht, Reiter Lehrplan (Fahrplan + Matrix)', { opt: LM, vor: gehe('kind/1-lehrplan', ruWarte('.lw-karte')) });
S('08e', 'lehrplan', '#/lehrplan', 'Lehrer: Lehrplan (Matrix aller Themen)', { opt: LM, vor: gehe('lehrplan', ruWarte('.mx-chip')) });
S('08f', 'schulstand', '#/schulstand/1', 'Lehrer: Schulstand des Kindes', { opt: LM, vor: gehe('schulstand/1', async (p) => { await p.waitForTimeout(1200); }) });
S('08f2', 'schulstand-alle', '#/schulstand', 'Lehrer: Schulstand, alle Kinder im Vergleich', { opt: LM, vor: gehe('schulstand', async (p) => { await p.waitForTimeout(1200); }) });
S('08g', 'expeditionen', '#/expeditionen', 'Lehrer: Expeditionen, alle Einträge aufgeklappt (Nachbau expKonto)', { opt: () => ({ rolle: 'lehrer', anpassen: kette(ev('lmsAnpassen')(), ev('expKonto')()) }), vor: async (page, { origin }) => { await page.goto(origin + '#/expeditionen'); await page.locator('details.lern-exp').first().waitFor(); await oeffneAlles(page); } });
S('08h', 'lernauftraege', '#/lernauftraege', 'Lehrer: Lernaufträge', { opt: LM, vor: gehe('lernauftraege', async (p) => { await p.getByText('Neuer Auftrag').first().waitFor(); }) });
S('08i', 'info', '#/info', 'Info „So funktioniert’s“ (Fragen eingeklappt, wie beim Öffnen)', { opt: LM, vor: async (page, { origin }) => { await page.goto(origin + '#/info'); await page.getByText('Erste Schritte').first().waitFor(); } });
S('08j', 'zugaenge', '#/zugaenge', 'Eltern: Zugänge (Lehrer hat keinen Zugang zu dieser Seite)', { opt: { rolle: 'eltern' }, vor: async (page, { origin }) => { await page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion === 'schule_zugaenge') return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, zugaenge: [{ id: 1, name: 'Herr Lehrer', rolle: 'lehrer', aktiv: true, zuletzt: null }, { id: 2, name: 'Kind A', rolle: 'kind', aktiv: true, zuletzt: '2026-11-14T08:00:00Z' }] } }) }); return route.fallback(); }); await page.goto(origin + '#/zugaenge'); await page.getByText('Neuen Zugang anlegen').first().waitFor(); } });
S('08k', 'einstellen', '#/ (Einstellen-Dialog Kind A)', 'Eltern: Blatt „Kind A einstellen“ geöffnet (Lehrer hat dieses Blatt auch)', { opt: { rolle: 'eltern' }, vor: async (page, { origin, b }) => { await page.goto(origin + '#/lernen'); await page.locator('.lern-zutun').waitFor(); await page.getByRole('button', { name: 'Kind A einstellen' }).first().click(); await page.getByRole('dialog', { name: 'Kind A einstellen' }).waitFor(); } });
S('08l', 'lernen-eltern', '#/lernen (Eltern)', 'Eltern-Startseite: Zu tun mit Wunsch, Belohnungen', { opt: { rolle: 'eltern' }, vor: async (page, { origin }) => { await page.goto(origin + '#/lernen'); await page.locator('.lern-zutun').waitFor(); await oeffneAlles(page); } });
S('08m', 'inhalte', '#/inhalte/1', 'Lehrer: Inhalte ansehen (Einheit 1, Etappen und Aufgaben)', { opt: LM, vor: gehe('inhalte/1', async (p) => { await p.waitForTimeout(1200); }) });
S('08n', 'plan-lernstand', '#/lernstand/1', 'Lehrer: Lernstand des Kindes (leitet auf Kind-Ansicht um, falls veraltet)', { opt: LM, vor: gehe('lernstand/1', async (p) => { await p.waitForTimeout(1200); }) });


// 2b Lehrer-Startseite „nichts zu tun“
S('02b', 'lehrer-start-ruhig', '#/lernen (nichts zu tun)', 'Startseite „Alles ruhig.“ (Nachbau laLage: keine Einheit offen, Lerntag gestern)', { opt: () => ({ rolle: 'lehrer', anpassen: (a, e) => (a === 'schule_eltern' ? { ...e, einloesungen: [] } : null) }),
  vor: async (page, { origin }) => { await ev('laLage')(page, { a: { einheiten: [] }, b: { lerntage: [ev('tagVor')(1)] } });
    await page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion === 'schule_rueckmeldungen') return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, rueckmeldungen: [] } }) }); return route.fallback(); });
    await page.goto(origin + '#/lernen'); await page.locator('.lern-zutun').getByText('Alles ruhig.').waitFor(); } });

// 9 Zustände
S('09a', 'zustand-laden', '#/reise/1 (Server antwortet nicht)', 'Ladeanzeige: Server antwortet 60 s lang nicht, Aufnahme nach 0,7 s', { opt: () => ({ rolle: 'kind', verzoegerungJe: (a) => (a === 'schule_ich' ? 0 : 60000) }), vor: async (page, { origin }) => { await page.goto(origin + '#/reise/1'); await page.waitForTimeout(300); } });
S('09a2', 'zustand-laden-lehrer', '#/lernen (Server antwortet nicht)', 'Ladeanzeige Lehrer-Startseite', { opt: () => ({ rolle: 'lehrer', verzoegerungJe: (a) => (a === 'schule_ich' ? 0 : 60000) }), vor: async (page, { origin }) => { await page.goto(origin + '#/lernen'); await page.waitForTimeout(300); } });
const fehlerRoute = async (page) => page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion === 'schule_ich') return route.fallback(); return route.fulfill({ status: 500, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Serverfehler (Test)' }) }); });
S('09b', 'zustand-fehler-kind', '#/reise/1 (API-Fehler 500)', 'Fehlermeldung bei API-Fehler, Kinderseite', { opt: KIND(), vor: async (page, { origin }) => { await fehlerRoute(page); await page.goto(origin + '#/reise/1'); await page.waitForTimeout(1500); } });
S('09b2', 'zustand-fehler-lehrer', '#/lernen (API-Fehler 500)', 'Fehlermeldung bei API-Fehler, Lehrer-Startseite', { opt: { rolle: 'lehrer' }, vor: async (page, { origin }) => { await fehlerRoute(page); await page.goto(origin + '#/lernen'); await page.waitForTimeout(1500); } });
S('09b3', 'zustand-fehler-eingabe', '#/lerneinheit/1-1-ueben-1 (Prüfen schlägt fehl)', 'Fehlermeldung beim Prüfen einer Antwort (Server 500)', { opt: KIND(), vor: async (page, { origin }) => { await page.goto(origin + '#/lerneinheit/1-1-ueben-1'); await losDann(page); await page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion === 'schule_uebung_pruefen') return route.fulfill({ status: 500, contentType: 'application/json', body: JSON.stringify({ ok: false, fehler: 'Serverfehler (Test)' }) }); return route.fallback(); }); await tasten(page, '2000'); await pruefen(page); await page.waitForTimeout(1200); } });
S('09c', 'zustand-toast', '#/kind/1-lehrplan (Meldung „Gespeichert“)', 'Toast-Meldung unten mit „Rückgängig“ nach dem Einplanen eines Themas', { opt: LM, vor: async (page, { origin }) => { await page.goto(origin + '#/kind/1-lehrplan'); await page.locator('.lw-karte').first().waitFor(); const neu = ev('THEMEN_ECHT').find((x) => x.klasse.gym_by === 9); await page.locator(`.lw-karte[data-id="${neu.thema_id}"]`).click(); await page.locator('.lw-drawer.lw-auf').getByRole('button', { name: 'In den Plan: als Nächstes' }).click(); await page.locator('.lw-toast:not([hidden])').waitFor(); } });
S('09d', 'zustand-leer-auftraege', '#/lernauftraege (leer)', 'Leere Liste: keine Lernaufträge', { opt: LM, vor: async (page, { origin }) => { await page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion === 'schule_rueckmeldungen') return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, rueckmeldungen: [] } }) }); return route.fallback(); }); await page.goto(origin + '#/lernauftraege'); await page.getByText('Neuer Auftrag').first().waitFor(); } });
S('09d2', 'zustand-leer-merkheft', '#/merkheft/1 (leer)', 'Leere Liste: Merkheft ohne Geschafftes', { opt: () => ({ rolle: 'kind', anpassen: (a, e) => (a === 'schule_merkheft' ? { ...e, einheiten: [] } : null) }), vor: gehe('merkheft/1', async (p) => { await p.waitForTimeout(1000); }) });
S('09d3', 'zustand-leer-zugaenge', '#/zugaenge (leer)', 'Leere Liste: keine Zugänge', { opt: { rolle: 'eltern' }, vor: async (page, { origin }) => { await page.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}'); if (b.aktion === 'schule_zugaenge') return route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: { ok: true, zugaenge: [] } }) }); return route.fallback(); }); await page.goto(origin + '#/zugaenge'); await page.getByText('Neuen Zugang anlegen').first().waitFor(); } });
S('09d4', 'zustand-leer-wackelt', '#/kind/1-wackelt (leer)', 'Leere Liste: Was wackelt ohne Fehler', { opt: () => ({ rolle: 'lehrer', anpassen: kette(ev('lmsAnpassen')(), ev('wwServer')({ leer: true }).anpassen) }), vor: gehe('kind/1-wackelt', async (p) => { await p.waitForTimeout(1500); }) });
S('09d5', 'zustand-leer-reisepass', '#/reisepass/1 (noch nichts)', 'Leere Liste: Reisepass ohne Stempel/abgelegte Flüge', { opt: KIND(), vor: gehe('reisepass/1', async (p) => { await p.waitForTimeout(800); }) });

function schreibeTabelle() {
  const vorhanden = new Set(fs.existsSync(AUS) ? fs.readdirSync(AUS) : []);
  const zeilen = ['# Seiten und Zustände der Lern-App – Bildschirmfotos für die Durchsicht (28.11.)', '',
    'Alle Bilder liegen in `bilder/`, Dateiname `<nr>-<seite>-<breite>-<hell|dunkel>.jpg`; Breiten 390 px und 1280 px, ganze Seite (fullPage), außer bei Vollbild-Ansichten (Landung, Menü, Einstellen-Blatt, Expedition freigeschaltet): dort nur der sichtbare Bildschirm.',
    'Aufnahme mit `node inhalte/design/durchsicht-2811/bilder_machen.cjs` (nutzt den Server-Nachbau und die erfundenen Beispieldaten aus `tests/lernen.test.cjs`; Kinder heißen „Kind A“, „Kind B“, „Testkind“). Adressen gelten auf der Lernen-Seite `/lernen/` (außer wo angegeben).', '',
    'Hinweis hell/dunkel: Kinderseiten folgen der Einstellung „Tag/Nacht“ (`lern.gestaltung`), das Regel-Universum und die Haupt-App dem Farbschema des Geräts. Die Lehrer-/Eltern-Seiten sind im Nachbau immer hell – hell- und dunkel-Bilder sind dort gleich.', '',
    '| Nr | Seite | Adresse | Dateinamen | Bemerkung |', '|---|---|---|---|---|'];
  for (const x of [...seiten].sort((a, b) => a.nr.localeCompare(b.nr, 'de', { numeric: true }))) {
    const d = []; for (const b of [390, 1280]) for (const f of ['hell', 'dunkel']) d.push(`${x.nr}-${x.name}-${b}-${f}.jpg`);
    const da = d.filter((n) => vorhanden.has(n)); const fehlt = d.length - da.length;
    zeilen.push(`| ${x.nr} | ${x.name} | \`${x.adresse}\` | \`${x.nr}-${x.name}-{390,1280}-{hell,dunkel}.jpg\` (${da.length} von 4) | ${x.bemerkung}${fehlt ? ' – FEHLT: ' + fehlt + ' Bild(er)' : ''} |`);
  }
  zeilen.push('', '## Nicht (oder nur teilweise) erreichbar im Nachbau', '',
    '- „Auch offen“ auf der Abflugtafel: nur bei mehreren gleichzeitig offenen Orten im Plan – im Nachbau nicht erreichbar.',
    '- „Merkheft im Universum“: ist der Link „Mein Merkheft“ oben im Regel-Universum (zu sehen auf 07a, 07g) und führt zur Seite `05f`/`05g`; eine eigene Merkheft-Ansicht im Universum gibt es nicht.',
    '- Flug-Test „Gleich verbessern“ (Korrektur) und Nachtragstest: nicht aufgenommen.',
    '- Lehrer-/Eltern-Seiten: hell und dunkel sind gleich, weil diese Seiten kein Dunkel kennen (Bereich „Lernen“ ist fest hell).',
    '- Zustand „Ladeanzeige“ ist eine Momentaufnahme nach 0,3–0,7 s bei absichtlich ausbleibender Server-Antwort.',
    '- Einzelne Aufnahmen enthalten Zufalls-Sticker („Yo Digga!“, „GOAT“ …) und Mock-Texte; die Daten sind erfunden.');
  fs.writeFileSync(path.join(__dirname, 'seiten.md'), zeilen.join('\n') + '\n');
  console.log('seiten.md geschrieben,', seiten.length, 'Seiten');
}

// ======================= Lauf =======================
(async () => {
  if (require.main !== module) return;
  const filter = process.argv[2] || '';
  if (filter === '--md') { schreibeTabelle(); return; }
  ctx = await starten();
  fs.mkdirSync(AUS, { recursive: true });
  for (const s of seiten) {
    if (filter && !(`${s.nr}-${s.name}`).includes(filter)) continue;
    const dateien = await fassung(s);
    ERGEBNIS.push({ nr: s.nr, name: s.name, adresse: s.adresse, bemerkung: s.bemerkung, dateien });
  }
  if (fehlerListe.length) log('Seitenfehler:\n' + fehlerListe.join('\n'));
  await beenden();
})().catch((e) => { console.error(e); process.exit(1); });
