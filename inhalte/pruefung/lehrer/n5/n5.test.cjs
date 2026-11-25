// Nachprüfung 4 (LB Teil 5): Plan als Cockpit, Lehrplan nach Klasse, 4 Stufen – App 0.82.0 mit erfundenem Lernstand auf der echten Themenliste.
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
  M.abschnitte = await p.locator('.lern-plan-links').evaluate((l) => [...l.querySelectorAll('h3, h4, .lern-plan-abschnitt, [class*=abschnitt-kopf]')].map((x) => x.innerText.trim()).filter((t) => t.length < 80));
  M.kopf = (await p.locator('#main').innerText()).match(/Gymnasium Kl\. 8[^\n]*\n?[^\n]*/)?.[0];
  M.legende = await p.locator('.lern-plan-lehrplan').evaluate((s) => ({ hoehe: Math.round((s.querySelector('[class*=legende]') || {}).getBoundingClientRect?.().height || 0), text: (s.querySelector('[class*=legende]') || {}).innerText?.slice(0, 120) }));
  M.spalteRollt = await p.locator('.lern-plan-lehrplan').evaluate((s) => { const cs = getComputedStyle(s); const kinder = [...s.querySelectorAll('*')].filter((x) => /(auto|scroll)/.test(getComputedStyle(x).overflowY) && x.scrollHeight > x.clientHeight + 4).length; return { position: cs.position, overflowY: cs.overflowY, innereBildlauf: kinder }; });
  // M1: alle Klassen aller Schularten – gebrochene Wörter, Überlappung, Querrollen
  const pruefen = () => p.locator('.lern-plan-lehrplan').evaluate((s) => {
    const kaputt = []; const ueber = [];
    const w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
    let n; while ((n = w.nextNode())) { const t = n.textContent; const re = /\S{3,}/g; let mm;
      while ((mm = re.exec(t))) { const r = document.createRange(); r.setStart(n, mm.index); r.setEnd(n, mm.index + mm[0].length); const rs = [...r.getClientRects()].filter((q) => q.width > 0);
        if (rs.length > 1 && new Set(rs.map((q) => Math.round(q.top))).size > 1) kaputt.push(mm[0]); } }
    for (const z of s.querySelectorAll('.lern-lp-zeile, [class*=lp-zeile]')) { const tt = z.querySelector('b, strong, .lern-lp-titel, [class*=titel]'); const st = z.querySelector('[class*=stufe-wort], [class*=st-wort], .lern-lp-stufe, [class*=lp-stufe]');
      if (tt && st) { const a = tt.getBoundingClientRect(), b = st.getBoundingClientRect(); if (a.right > b.left + 1 && a.left < b.right - 1 && a.bottom > b.top + 1 && a.top < b.bottom - 1) ueber.push(tt.innerText.slice(0, 40)); } }
    return { kaputt: [...new Set(kaputt)].slice(0, 12), ueber: ueber.slice(0, 6), quer: document.documentElement.scrollWidth > innerWidth + 1 }; });
  M.tg = {};
  for (const gb of ['Zahlen', 'Algebra', 'Geometrie', 'Fläche und Raum', 'Geld und Verhältnisse', 'Daten und Zufall', 'Funktionen', 'Entdecker-Inseln']) { await p.locator('.lern-plan-lehrplan button').filter({ hasText: gb }).first().click(); await p.waitForTimeout(200); if (gb === 'Zahlen' || gb === 'Geometrie') await p.locator('.lern-plan-lehrplan').screenshot({ path: path.join(AUS, `${g}-themengebiet-${gb}.png`) }); const r = await pruefen(); r.kaputt = r.kaputt.filter((x) => !x.includes('-')); if (r.kaputt.length || r.ueber.length || r.quer) M.tg[gb] = r; }
  M.linksAbgeschnitten = await p.locator('.lern-plan-links').evaluate((l) => { const t = [...l.querySelectorAll('b, strong, [class*=titel]')].filter((x) => x.scrollWidth > x.clientWidth + 1); return { anzahl: t.length, bsp: t.slice(0, 4).map((x) => x.innerText.slice(0, 50)) }; });
  const umsch = p.locator('.lern-plan-umschalter button').filter({ hasText: /Klasse/ });
  await umsch.click(); await p.waitForTimeout(400);
  const sp = p.locator('.lern-plan-lehrplan');
  const kl = async (sa, n) => { await sp.locator('.lern-plan-sa button').filter({ hasText: sa }).first().click({ timeout: 3000 }); await p.waitForTimeout(150); await sp.locator('.lern-plan-kl button').filter({ hasText: new RegExp('(^|\\D)' + n + '(\\D|$)') }).first().click({ timeout: 3000 }); await p.waitForTimeout(250); };
  M.m1 = {};
  for (const [sa, ks] of [['Gymnasium', [5, 6, 7, 8, 9, 10]], ['Realschule', [5, 6, 7, 8, 9, 10]], ['IB MYP', [1, 2, 3, 4, 5]]]) for (const k of ks) { await kl(sa, String(k)); const r = await pruefen(); r.kaputt = r.kaputt.filter((x) => !x.includes('-')); if (r.kaputt.length || r.ueber.length || r.quer) M.m1[sa + ' ' + k] = r; }
  await kl('Gymnasium', '8'); await sp.screenshot({ path: path.join(AUS, `${g}-klasse-gym8.png`) });
  M.gym8 = await sp.evaluate((s) => s.innerText.slice(0, 2500));
  await kl('Realschule', '7'); await sp.screenshot({ path: path.join(AUS, `${g}-klasse-rs7.png`) });
  M.rs7zeilen = await sp.evaluate((s) => s.innerText.match(/RS 7: [^\n]*/)?.[0]);
  await kl('IB MYP', '3'); M.ib3 = await sp.evaluate((s) => [...s.querySelectorAll('h3, h4, [class*=lernbereich]')].map((x) => x.innerText).slice(0, 4)); await sp.screenshot({ path: path.join(AUS, `${g}-klasse-ib3.png`) });
  // S4/K4: Aufklappen
  await kl('Gymnasium', '8');
  await sp.getByText('Lineare Ungleichungen', { exact: false }).first().click(); await p.waitForTimeout(300);
  await sp.screenshot({ path: path.join(AUS, `${g}-klasse-gym8-auf.png`) });
  M.auf = await sp.evaluate((s) => s.innerText.slice(s.innerText.indexOf('Lehrplan:'), s.innerText.indexOf('Lehrplan:') + 700));
  await sp.getByText('Lineare Ungleichungen', { exact: false }).first().click(); await p.waitForTimeout(200);
  await sp.getByText('Intervalle', { exact: true }).first().click(); await p.waitForTimeout(300);
  M.intervalle = await sp.evaluate((s) => s.innerText.slice(s.innerText.indexOf('Lehrplan:'), s.innerText.indexOf('Lehrplan:') + 160));
  // S1: Auswahlmodus
  const hoeheVor = await p.evaluate(() => document.documentElement.scrollHeight);
  await p.getByRole('button', { name: /Auswählen/ }).first().click(); await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(AUS, `${g}-auswahl-blick.png`) }); await p.screenshot({ path: path.join(AUS, `${g}-auswahl-ganz.png`), fullPage: true });
  M.auswahl = await p.evaluate((hv) => { const L = document.querySelector('.lern-plan-links'); const sichtbar = (x) => !!(x.offsetWidth || x.offsetHeight || x.getClientRects().length);
    return { hoeheVor: hv, hoehe: document.documentElement.scrollHeight, haken: [...L.querySelectorAll('input[type=checkbox]')].filter(sichtbar).length,
      flugKnoepfe: [...L.querySelectorAll('button')].filter((b) => sichtbar(b) && /^Kann er komplett|^Lernen/.test(b.innerText)).length,
      altHaken: [...L.querySelectorAll('label')].filter((x) => sichtbar(x) && /alle Flüge: kann er komplett/.test(x.innerText)).length,
      einzeln: [...L.querySelectorAll('button, summary, a')].filter((x) => sichtbar(x) && /einzeln/.test(x.innerText)).length,
      alleAusw: [...L.querySelectorAll('label, button')].filter((x) => sichtbar(x) && /alle auswählen/i.test(x.innerText)).length }; }, hoeheVor);
  await p.locator('.lern-plan-links input[type=checkbox]').nth(1).check(); await p.mouse.wheel(0, 2500); await p.waitForTimeout(300);
  M.leiste = await p.evaluate(() => { const l = document.querySelector('[class*=sammel], [class*=auswahl-leiste]'); if (!l) return null; const r = l.getBoundingClientRect(); return { sichtbar: r.bottom > 0 && r.top < innerHeight, text: l.innerText.split('\n')[0] }; });
  await p.screenshot({ path: path.join(AUS, `${g}-auswahl-gescrollt.png`) });
  // S3: Lehrplan-Übersicht
  await p.goto(H.origin + '/lernen/#/lehrplan'); await p.waitForTimeout(1200);
  await p.screenshot({ path: path.join(AUS, `${g}-lehrplan.png`), fullPage: true });
  M.lehrplan = await p.evaluate(() => document.querySelector('#main').innerText.slice(0, 2600));
  const rs = p.getByRole('button', { name: 'Realschule' }).first(); await rs.click(); await p.waitForTimeout(200); await p.getByRole('button', { name: /^Kl\. 7/ }).first().click(); await p.waitForTimeout(400);
  M.lehrplanRs7 = await p.evaluate(() => document.querySelector('#main').innerText.slice(0, 2200)); await p.screenshot({ path: path.join(AUS, `${g}-lehrplan-rs7.png`), fullPage: true });
  M.fehler = fehler;
  fs.writeFileSync(path.join(__dirname, 'mess.json'), JSON.stringify(MESS, null, 1));
});
