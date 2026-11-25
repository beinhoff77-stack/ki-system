// Prüfrunde Eltern-/Lehrerseite: Anmeldung als Lehrer auf /lernen/ (Lern-Code), echte Orte-Struktur (orte.json) und Themenliste.
// setup() aus tests/lernen.test.cjs unverändert; überschrieben werden nur Antworten der lernen-api (Testdaten, keine Kinderdaten).
// Start: PW_TEST_EXECUTABLE=/pfad/chrome node --test inhalte/pruefung/eltern/rundgang.test.cjs
'use strict';
const { test } = require('node:test');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '../../..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; } };', quelle);
const H = m.exports;
const AUS = path.join(__dirname, 'bilder'); fs.mkdirSync(AUS, { recursive: true });
const MESS = {};

const O = JSON.parse(fs.readFileSync(path.join(__dirname, 'orte.json'), 'utf8'));
const TL = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themenliste.json'), 'utf8'));
const thema = new Map(TL.map((t) => [t.thema_id, t]));
thema.set(15, { titel: 'Natürliche Zahlen und Stellenwertsysteme', klasse: { gym_by: 5, rs_by: 5, ib_myp: 1 }, gebiet: 'Zahlen' });
thema.set(17, { titel: 'Teilbarkeit und Primzahlen', klasse: { gym_by: 5, rs_by: 5, ib_myp: 1 }, gebiet: 'Zahlen' });
const ORTE = O.orte.map(([block_id, titel, ziel_klasse, stadt, land, lat, lon, kontinent, einheiten]) => ({ block_id, titel, ziel_klasse, stadt, land, kontinent: O.kontinente[kontinent][0],
  themen: einheiten.map(([id, tid, status, karten]) => { const t = thema.get(tid) || {}; return { thema_id: tid, titel: t.titel || titel, jahrgang: t.klasse || {}, gebiet: t.gebiet || O.kontinente[kontinent][0], ort: stadt, block_id,
    stand: id === 44 || id === 50 ? 'erledigt' : id === 39 ? 'laeuft' : 'offen', einheit: { id, status, karten, aufgaben: karten * 18, neu: 0 } }; }) }));
// Plan Kind A: Klasse-5-Orte in Lehrplan-ähnlicher Reihenfolge (Testdaten)
const PLAN = [49, 55, 48, 83, 54, 87, 64, 86, 96, 95, 81, 79];
const SETZEN = [];
const KINDER = [{ id: 1, name: 'Kind A', klasse: 5, schulart: 'gym_by' }, { id: 2, name: 'Kind B', klasse: 8, schulart: 'gym_by' }];

async function einrichten(page, calls) {
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const req = route.request(); const pfad = new URL(req.url()).pathname; const b = JSON.parse(req.postData() || '{}'); const d = b.daten || {};
    const ok = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
    if (pfad.endsWith('/anmelden')) return ok({ token: 't'.repeat(64), rolle: 'lehrer', name: 'Frau Lehrerin', lernender_id: null });
    calls.push(b.aktion);
    if (b.aktion === 'schule_ich') return ok({ ok: true, rolle: 'lehrer', name: 'Frau Lehrerin', lernender_id: null, app: false });
    if (b.aktion === 'schule_plan_lesen') return ok({ ok: true, kind: KINDER.find((k) => k.id === d.lernender_id) || KINDER[0], revision: 3,
      plan: [{ block_id: 61, position: 0, art: 'rueckreise', status: 'offen', kann_schon: false }].filter(() => d.lernender_id === 2)
        .concat((d.lernender_id === 2 ? [73, 72, 60, 59, 71, 84, 92] : PLAN).map((block_id, i) => ({ route_id: i + 1, block_id, position: i + 1, art: 'normal', status: block_id === 55 || block_id === 73 ? 'fertig' : 'offen', kann_schon: false, ausgelassen: [] }))),
      orte: ORTE, notizen: [{ id: 1, text: 'Bruchrechnen hat in der Schule gewackelt.', von: 'eltern:Papa', am: '2026-11-10T10:00:00Z' }],
      verlauf: [{ akteur: 'eltern:Papa', anlass: 'plan', am: '2026-11-14T09:00:00Z' }] });
    if (b.aktion === 'schule_plan_setzen') { SETZEN.push(d); return ok({ ok: true, revision: 4 + SETZEN.length, anzahl: (d.eintraege || []).length }); }
    if (b.aktion === 'schule_lehrplan_uebersicht') return ok({ ok: true, kinder: KINDER,
      themen: ORTE.flatMap((o) => o.themen.map((t) => ({ ...t, stand: { 1: t.stand === 'offen' ? 'offen' : t.stand }, geplant: PLAN.includes(o.block_id) ? [1] : [], rueckmeldungen: 0 }))) });
    return route.fallback();
  });
}

const warte = async (p, ms = 400) => { await p.waitForFunction(() => !document.querySelector('#main .spinner'), null, { timeout: 6000 }).catch(() => {}); await p.waitForTimeout(ms); };
const bild = (p, name, ganz = true) => p.screenshot({ path: path.join(AUS, name + '.png'), fullPage: ganz });

for (const [geraet, w, h] of [['tablet', 820, 1180], ['handy', 390, 844], ['rechner', 1280, 900]]) {
  test(`Lehrer ${geraet}`, async () => {
    const nach = []; const calls = []; const { page: p } = await H.setup({ after: (f) => nach.push(f) }, { lernSeite: true, rolle: 'lehrer' });
    const r = MESS[geraet] = {};
    try {
      await p.setViewportSize({ width: w, height: h }); await einrichten(p, calls);
      await p.goto(H.origin + '/lernen/'); await p.getByLabel('Lern-Code').fill('ABCD-EFGH-JKLM'); await p.getByRole('button', { name: 'Anmelden' }).click(); await warte(p);
      await bild(p, `${geraet}-1-start`); r.start = { url: p.url().split('#')[1], hoehe: await p.evaluate(() => document.documentElement.scrollHeight), text: await p.evaluate(() => document.querySelector('#main').innerText.slice(0, 1500)) };
      // Themenplan Kind A (E-2: zwei Spalten, Ziehen, sofort speichern)
      await p.goto(H.origin + '/lernen/#/plan/1'); await warte(p);
      await bild(p, `${geraet}-2-plan`); await bild(p, `${geraet}-2-plan-erster-blick`, false);
      r.plan = await p.evaluate(() => ({ hoehe: document.documentElement.scrollHeight, zeilen: document.querySelectorAll('.lern-plan-zeile').length,
        zeileHoehe: Math.round(document.querySelector('.lern-plan-zeile')?.getBoundingClientRect().height || 0), speichernKnopf: [...document.querySelectorAll('button')].some((b) => /Plan speichern/.test(b.textContent)) }));
      // Melbourne (Platz 10) an Platz 2 ziehen
      const namenVor = await p.locator('.lern-plan-zeile').evaluateAll((l) => l.map((x) => x.innerText.split('\n').find((t) => t.trim().length > 2)));
      const g = p.getByRole('button', { name: /^Melbourne.* ziehen$/ }); const ziel = p.locator('.lern-plan-zeile').nth(1);
      SETZEN.length = 0;
      if (await g.count()) { await g.scrollIntoViewIfNeeded(); const a = await g.boundingBox(); await ziel.scrollIntoViewIfNeeded(); const zb = await ziel.boundingBox(); const a2 = await g.boundingBox();
        await p.mouse.move(a2.x + a2.width / 2, a2.y + a2.height / 2); await p.mouse.down(); for (let k = 1; k <= 12; k++) { await p.mouse.move(a2.x + a2.width / 2, a2.y + (zb.y + 4 - a2.y) * k / 12); await p.waitForTimeout(30); } await p.mouse.up(); await p.waitForTimeout(600); }
      const namenNach = await p.locator('.lern-plan-zeile').evaluateAll((l) => l.map((x) => x.innerText.split('\n').find((t) => t.trim().length > 2)));
      r.ziehen = { vorher: namenVor.slice(0, 3), nachher: namenNach.slice(0, 3), gespeichert: SETZEN.length, toast: await p.locator('[role=status]').allInnerTexts() };
      await bild(p, `${geraet}-3-nach-ziehen`, false);
      // Flug abwählen (Rom aufklappen)
      const rom = p.locator('.lern-plan-zeile').filter({ hasText: 'Rom' }).first(); await rom.locator('button, summary').filter({ hasText: /Rom|Flüge/ }).first().click().catch(() => {}); await p.waitForTimeout(300);
      r.abwaehlbar = await p.locator('.lern-plan-im input').count();
      await bild(p, `${geraet}-4-plan-rom-auf`, false);
      // Info-Seite und Meine Aufträge
      await p.goto(H.origin + '/lernen/#/info'); await warte(p); await bild(p, `${geraet}-5-info`); r.info = { hoehe: await p.evaluate(() => document.documentElement.scrollHeight), text: await p.evaluate(() => document.querySelector('#main').innerText.slice(0, 1500)) };
      await p.goto(H.origin + '/lernen/#/lernauftraege'); await warte(p); await bild(p, `${geraet}-6-auftraege`);
    } finally { for (const f of nach.reverse()) { try { await f(); } catch { /* Seitenfehler hier nicht bewertet */ } } }
  });
}
test('Messung schreiben', () => fs.writeFileSync(path.join(__dirname, 'messung.json'), JSON.stringify(MESS, null, 1)));
