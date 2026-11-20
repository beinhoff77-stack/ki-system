// Nachprüfung 3 (LB): Plan als Cockpit, Lehrplan nach Klasse, 4 Stufen – App 0.82.0 mit erfundenem Lernstand auf der echten Themenliste.
'use strict';
const { test } = require('node:test'); const assert = require('node:assert');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; } };', quelle);
const H = m.exports;
const AUS = path.join(__dirname, 'bilder'); fs.mkdirSync(AUS, { recursive: true });
const T = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themenliste.json'), 'utf8'));
const GEB = ['Zahlen', 'Geld und Verhältnisse', 'Algebra', 'Funktionen', 'Geometrie', 'Fläche und Raum', 'Daten und Zufall', 'Entdecker-Inseln'];
const etappen = (t) => { try { const d = JSON.parse(fs.readFileSync(path.join(root, t.datei), 'utf8')); return (d.inhalt?.etappen || []).map((e) => ({ lernziel: e.lernziel, titel: e.titel })); } catch { return []; } };
// Erfundener Lernstand eines Testkinds in Gym 8
const NICHT = new Set([51, 61]); // Kreisberechnungen, Zufall und Laplace: nicht im Plan
function stufeVon(t) {
  const g = t.klasse.gym_by; const n = Math.max(etappen(t).length, 1);
  const s = (stufe, x = {}) => ({ stufe, zeichen: { komplett: '◉', wiederholung: '↻', dran: '▶', kommt: '○', nicht_im_plan: '+' }[stufe], gesetzt: null, im_plan: stufe !== 'nicht_im_plan', etappen: n, begonnen: 0, gelandet: 0, sicher: 0, wieder_offen: 0, wdh_nr: null, naechste_in: null, rueckreise: false, test_offen: false, ohne_test: false, ...x });
  if (!g || g > 8 || NICHT.has(t.thema_id)) return s('nicht_im_plan', { etappen: n });
  if (g <= 6) return t.thema_id % 3 ? s('komplett', { gelandet: n, sicher: n }) : s('wiederholung', { gelandet: n, sicher: n - 1, wdh_nr: 4, naechste_in: 9 });
  if (g === 7) return t.thema_id % 2 ? s('wiederholung', { gelandet: n, sicher: 0, wdh_nr: 2, naechste_in: 3 }) : s('wiederholung', { gesetzt: 'wiederholen', gelandet: n, wdh_nr: 1, naechste_in: 1, ohne_test: true });
  const r = t.reihenfolge.gym_by;
  if (r === 1) return s('komplett', { gelandet: n, sicher: n });
  if (r === 2 || r === 3) return s('wiederholung', { gelandet: n, wdh_nr: 2, naechste_in: 4 });
  if (r === 4) return s('dran', { begonnen: 4, gelandet: 3 });
  return s('kommt');
}
const BL = new Map();
for (const t of T) { const b = BL.get(t.block_id) || { block_id: t.block_id, stadt: t.ort, titel: t.titel, kontinent: t.gebiet, kontinent_id: GEB.indexOf(t.gebiet) + 1, reihenfolge: (GEB.indexOf(t.gebiet) + 1) * 100 + BL.size, themen: [] };
  const st = stufeVon(t);
  b.themen.push({ thema_id: t.thema_id, titel: t.titel, jahrgang: t.klasse, stand: st.stufe === 'komplett' || st.stufe === 'wiederholung' ? 'erledigt' : st.stufe === 'dran' ? 'laeuft' : 'offen',
    kann_schon: false, kann_wdh: st.gesetzt === 'wiederholen', lehrplan_reihenfolge: t.reihenfolge, stufe: st, beschreibung: t.umfang, lernbereich: t.lernbereich,
    lehrplan: { gym_by: t.lehrplan_gym, rs_by: t.lehrplan_rs, ib_myp: t.lehrplan_ib }, etappen: etappen(t), einheit: { id: t.thema_id, status: 'geprueft', karten: etappen(t).length, aufgaben: 40, neu: 0 } });
  BL.set(t.block_id, b); }
const ORTE = [...BL.values()].sort((a, b) => a.reihenfolge - b.reihenfolge);
const PLAN = ORTE.filter((o) => o.themen.some((t) => t.stufe.im_plan));
const planZeilen = () => PLAN.map((o, i) => ({ route_id: i + 1, block_id: o.block_id, position: i + 1, art: 'normal',
  status: o.themen.every((t) => !t.stufe.im_plan || t.stufe.stufe === 'komplett') ? 'fertig' : 'offen', kann_schon: false,
  ausgelassen: o.themen.filter((t) => !t.stufe.im_plan).map((t) => t.thema_id), kann_schon_themen: [], kann_wdh_themen: o.themen.filter((t) => t.kann_wdh).map((t) => t.thema_id) }));
const SETZEN = [];
const _a = 0;
const anpassen = (aktion, e) => {
  if (aktion === 'schule_uebersicht') { const x = structuredClone(e); x.lernende = (x.lernende || []).map((k) => (k.id === 1 ? { ...k, klasse: 8, schulart: 'gym_by' } : k)); return x; }
  if (aktion === 'schule_plan_lesen') return { ok: true, kann_abwaehlen: true, kann_wdh: true, kind: { id: 1, name: 'Kind A', klasse: 8, schulart: 'gym_by', stufen: {} }, revision: 1, orte: structuredClone(ORTE), plan: planZeilen(), notizen: [], verlauf: [] };
  if (aktion === 'schule_plan_setzen') { return { ok: true, revision: 2, schritt_id: 900 }; }
  if (aktion === 'schule_lehrplan_uebersicht') return { ok: true, kinder: [{ id: 1, name: 'Kind A', klasse: 8, schulart: 'gym_by' }],
    themen: T.map((t) => { const o = BL.get(t.block_id); const x = o.themen.find((y) => y.thema_id === t.thema_id);
      return { thema_id: t.thema_id, titel: t.titel, gebiet: t.gebiet, ort: t.ort, block_id: t.block_id, jahrgang: t.klasse, einheit: x.einheit, stand: { 1: x.stand }, geplant: x.stufe.im_plan ? [1] : [], rueckmeldungen: 0,
        lernbereich: t.lernbereich, lehrplan: x.lehrplan, lehrplan_reihenfolge: t.reihenfolge, stufe: { 1: x.stufe } }; }) };
  return null;
};
const MESS = {};
const breit = (p) => p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
for (const [g, w, h] of (process.env.NUR ? [['820', 820, 1180]] : [['400', 400, 860], ['820', 820, 1180], ['1280', 1280, 900]])) test(`N3 ${g}`, async (tt) => {
  const { page: p, calls } = await H.setup(tt, { lernSeite: true, rolle: 'lehrer', anpassen });
  const M = MESS[g] = {}; const fehler = []; p.on('pageerror', (x) => fehler.push(String(x)));
  await p.setViewportSize({ width: w, height: h });
  await p.goto(H.origin + '/lernen/'); await p.getByLabel('Lern-Code').fill('ABCD-EFGH-JKLM'); await p.getByRole('button', { name: 'Anmelden' }).click(); await p.waitForTimeout(900);
  await p.goto(H.origin + '/lernen/#/kind/1-plan'); await p.waitForTimeout(1400);
  await p.screenshot({ path: path.join(AUS, `${g}-plan-blick.png`) }); await p.screenshot({ path: path.join(AUS, `${g}-plan-ganz.png`), fullPage: true });
  M.plan = await p.evaluate(() => ({ hoehe: document.documentElement.scrollHeight, kopf: document.querySelector('.lern-plan-kopf, .lern-plan-oben, [class*=plan-kopf]')?.innerText,
    text: document.querySelector('#main').innerText.slice(0, 3000), zeichen: [...document.querySelectorAll('.lern-st-sym')].map((x) => x.textContent).join(''),
    farben: [...new Set([...document.querySelectorAll('.lern-st-sym')].map((x) => x.className + '=' + getComputedStyle(x).color + '/' + getComputedStyle(x).backgroundColor))] }));
  M.planBreit = await breit(p);
  // Ansicht nach Klasse: Gym 8
  const umsch = p.locator('.lern-plan-umschalter button').filter({ hasText: /Klasse/ });
  await umsch.click(); await p.waitForTimeout(400);
  const sp = p.locator('.lern-plan-lehrplan');
  M.knoepfeKlasse = await sp.locator('.lern-plan-klasse button:visible').allInnerTexts();
  const kl = async (sa, n) => { await sp.locator('.lern-plan-sa button').filter({ hasText: sa }).first().click({ timeout: 3000 }); await p.waitForTimeout(200); await sp.locator('.lern-plan-kl button').filter({ hasText: new RegExp('(^|\\D)' + n + '(\\D|$)') }).first().click({ timeout: 3000 }); await p.waitForTimeout(400); };
  await kl('Gymnasium', '8'); await sp.screenshot({ path: path.join(AUS, `${g}-klasse-gym8.png`) });
  M.gym8 = await sp.evaluate((s) => ({ text: s.innerText.slice(0, 3000), zeilen: s.querySelectorAll('.lern-lp-zeile, .lern-plan-vorrat-zeile, [data-thema]').length }));
  await kl('Realschule', '7'); await sp.screenshot({ path: path.join(AUS, `${g}-klasse-rs7.png`) });
  M.rs7 = await sp.evaluate((s) => ({ text: s.innerText.slice(0, 3500) }));
  await kl('IB MYP', '3'); M.ib3 = await sp.evaluate((s) => s.innerText.slice(0, 1500)); await sp.screenshot({ path: path.join(AUS, `${g}-klasse-ib3.png`) });
  // Aufklappen einer Zeile in Gym 8
  await kl('Gymnasium', '8');
  const zeile = sp.getByText('Lineare Ungleichungen', { exact: false }).first(); await zeile.click(); await p.waitForTimeout(400);
  await sp.screenshot({ path: path.join(AUS, `${g}-klasse-gym8-auf.png`) });
  M.auf = await sp.evaluate((s) => s.innerText.slice(0, 2500));
  M.knoepfeRechts = await sp.locator('button').allInnerTexts();
  // ◉-Zeile aufklappen
  await sp.getByText('Zuordnung und Funktion', { exact: false }).first().click(); await p.waitForTimeout(300);
  M.knoepfeKomplett = (await sp.locator('button').allInnerTexts()).filter((k) => /Wieder in die|Kann er|Lernen|Aus dem Plan/.test(k)).map((k) => k.split('\n')[0]);
  await sp.screenshot({ path: path.join(AUS, `${g}-klasse-gym8-komplett-auf.png`) });
  // links ein Ort aufklappen
  await p.locator('.lern-plan-links').getByText('Bruchterme', { exact: false }).first().click(); await p.waitForTimeout(300);
  await p.locator('.lern-plan-links').screenshot({ path: path.join(AUS, `${g}-links-ort-auf.png`) });
  M.linksAuf = (await p.locator('.lern-plan-links').innerText()).slice(0, 1500);
  // Auswahlmodus
  const ausw = p.getByRole('button', { name: /Auswählen/ }).first(); M.auswahlDa = await ausw.count();
  if (M.auswahlDa) { await ausw.click(); await p.waitForTimeout(500); await p.screenshot({ path: path.join(AUS, `${g}-auswahl-blick.png`) }); await p.screenshot({ path: path.join(AUS, `${g}-auswahl-ganz.png`), fullPage: true });
    M.auswahl = await p.evaluate(() => ({ hoehe: document.documentElement.scrollHeight, haken: document.querySelectorAll('#main input[type=checkbox]').length, leiste: document.querySelector('[class*=sammel], [class*=auswahl-leiste]')?.innerText,
      leistePos: (() => { const l = document.querySelector('[class*=sammel], [class*=auswahl-leiste]'); return l ? getComputedStyle(l).position + ' ' + Math.round(l.getBoundingClientRect().top) : null; })() }));
    const hk = p.locator('.lern-plan-links input[type=checkbox]'); await hk.nth(0).check(); await hk.nth(1).check(); await p.waitForTimeout(200);
    await p.mouse.wheel(0, 3000); await p.waitForTimeout(300); await p.screenshot({ path: path.join(AUS, `${g}-auswahl-gescrollt.png`) });
    M.leisteNachScroll = await p.evaluate(() => { const l = document.querySelector('[class*=sammel], [class*=auswahl-leiste]'); if (!l) return null; const r = l.getBoundingClientRect(); return { top: Math.round(r.top), sichtbar: r.bottom > 0 && r.top < innerHeight, text: l.innerText.split('\n')[0] }; });
    const n0 = calls.filter((c) => c.aktion === 'schule_plan_setzen').length;
    await p.getByRole('button', { name: /^Kann er – aber wiederholen/ }).last().click().catch((e) => { M.sammelFehler = String(e).slice(0, 120); }); await p.waitForTimeout(600);
    M.sammelAufrufe = calls.filter((c) => c.aktion === 'schule_plan_setzen').length - n0;
    const dd = calls.filter((c) => c.aktion === 'schule_plan_setzen').slice(-1)[0]?.daten || {}; M.sammelDaten = JSON.stringify((dd.eintraege || []).filter((x) => (x.kann_wdh_themen || []).length || (x.ausgelassen || []).length)) + ' rest:' + JSON.stringify(Object.keys(dd)); }
  // Lehrplan-Übersicht
  await p.goto(H.origin + '/lernen/#/lehrplan'); await p.waitForTimeout(1200);
  await p.screenshot({ path: path.join(AUS, `${g}-lehrplan.png`), fullPage: true });
  M.lehrplan = await p.evaluate(() => ({ hoehe: document.documentElement.scrollHeight, text: document.querySelector('#main').innerText.slice(0, 2500), zeichen: [...document.querySelectorAll('.lern-st-sym')].map((x) => x.textContent).join('') }));
  // Überblick
  await p.goto(H.origin + '/lernen/#/kind/1-ueberblick'); await p.waitForTimeout(1200);
  await p.screenshot({ path: path.join(AUS, `${g}-ueberblick.png`), fullPage: true });
  M.ueberblick = await p.evaluate(() => document.querySelector('#main').innerText.slice(0, 1800));
  M.fehler = fehler; M.setzen = calls.filter((c) => c.aktion === 'schule_plan_setzen').length;
  fs.writeFileSync(path.join(__dirname, 'mess.json'), JSON.stringify(MESS, null, 1));
});
