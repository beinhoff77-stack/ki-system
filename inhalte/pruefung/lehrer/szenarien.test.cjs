// Prüfrunde Lehrer-Gesamtansicht: Rundgang durch alle Lehrer-Seiten mit echter Orte-Struktur (orte.json) und echten Lernkarten (inhalte/themen).
// Anmeldung wie ein Kind auf der Lernen-Seite (/lernen/, Lern-Code). setup() aus tests/lernen.test.cjs unverändert;
// überschrieben werden nur die Antworten der lernen-api (Testdaten unten, keine echten Kinderdaten).
// Start: PW_TEST_EXECUTABLE=/pfad/chrome node --test inhalte/pruefung/kinderansicht/rundgang.test.cjs
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

// ---------- Testdaten ----------
const O = JSON.parse(fs.readFileSync(path.join(__dirname, 'orte.json'), 'utf8'));
const TL = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/themenliste.json'), 'utf8'));
const thema = new Map(TL.map((t) => [t.thema_id, t]));
// Zwei ältere Einheiten stehen nicht in der themenliste: Titel/Klasse aus der App-Testdatei, Lernkarten stellvertretend aus einem Nachbarthema.
thema.set(15, { titel: 'Natürliche Zahlen und Stellenwertsysteme', klasse: { gym_by: 5, rs_by: 5, ib_myp: 1 }, datei: 'inhalte/themen/zahlen.rechengesetze.json', ersatz: true });
thema.set(17, { titel: 'Teilbarkeit und Primzahlen', klasse: { gym_by: 5, rs_by: 5, ib_myp: 1 }, datei: 'inhalte/themen/zahlen.ganz.json', ersatz: true });
const orte = O.orte.map(([block_id, titel, ziel_klasse, stadt, land, lat, lon, kontinent, einheiten]) => ({ block_id, titel, ziel_klasse, stadt, land, lat, lon, kontinent,
  kontinent_titel: O.kontinente[kontinent][0], erdteil: O.kontinente[kontinent][1], einheiten }));
const einheiten = orte.flatMap((o) => o.einheiten.map(([id, tid, status, karten]) => {
  const t = thema.get(tid) || {};
  return { id, thema_id: tid, status, block_id: o.block_id, ort: o.stadt, stadt: o.stadt, land: o.land, lat: o.lat, lon: o.lon, kontinent: o.kontinent_titel, erdteil: o.erdteil,
    ort_titel: o.titel, titel: t.titel || o.titel, ziel: t.umfang || '', pflicht_anzahl: karten, ziel_klasse: t.klasse?.gym_by ?? o.ziel_klasse, jahrgang: t.klasse || {}, datei: t.datei };
}));
const E = new Map(einheiten.map((e) => [e.id, e]));
const inhalt = (eid) => { const e = E.get(eid); try { return JSON.parse(fs.readFileSync(path.join(root, e.datei), 'utf8')); } catch { return null; } };

const KINDER = {
  1: { name: 'Kind A', klasse: 5, gestaltung: 'tag',
    route: [[49, 1, 'offen'], [55, 2, 'fertig'], [48, 3, 'offen'], [83, 4, 'offen'], [54, 5, 'offen'], [87, 6, 'offen'], [64, 7, 'offen'], [86, 8, 'offen'], [96, 9, 'offen'], [95, 10, 'offen']],
    stand: { 44: { fertig: 10, blocktest: true }, 39: { fertig: 3 }, 50: { fertig: 8, blocktest: true } },
    konto: { sterne: 860, stempel: 1, lerntage: 14, jahrgang: { schulart: 'gym_by', klasse: 5, themen: 14, mit_inhalt: 14, geschafft: 2 },
      orte: [{ block_id: 49, themen: 5, erledigt: 1, abgeschlossen: false }, { block_id: 55, themen: 1, erledigt: 1, abgeschlossen: true }] },
    wdh: [44] },
  2: { name: 'Kind B', klasse: 8, gestaltung: 'nacht',
    route: [[61, 0, 'offen', 'rueckreise'], [73, 1, 'fertig'], [72, 2, 'offen'], [60, 3, 'offen'], [59, 4, 'offen'], [71, 5, 'offen'], [84, 6, 'offen'], [92, 7, 'offen']],
    stand: { 16: { fertig: 8, blocktest: true }, 17: { fertig: 2 }, 27: { fertig: 7, fehler: 2, blocktest: true } },
    konto: { sterne: 420, stempel: 1, lerntage: 9, jahrgang: { schulart: 'gym_by', klasse: 8, themen: 15, mit_inhalt: 13, geschafft: 1 },
      orte: [{ block_id: 73, themen: 1, erledigt: 1, abgeschlossen: true }, { block_id: 61, themen: 3, erledigt: 0, abgeschlossen: false }] },
    wdh: [16] },
};

function antworten(kid) {
  const K = KINDER[kid];
  const lernende = Object.entries(KINDER).map(([id, k]) => ({ id: Number(id), name: k.name, klasse: k.klasse, schulart: 'gym_by', ist_test: false, stil: 'entdecker', welt: 'Ozean',
    route: k.route.map(([block_id, position, status, art]) => ({ block_id, position, status, art: art || 'normal', kann_schon: false })),
    stand: Object.entries(k.stand).map(([eid, s]) => ({ einheit_id: Number(eid), fertig: s.fertig || 0, fehler: s.fehler || 0, gesichert: 0, blocktest: !!s.blocktest, laeuft: false })) }));
  const etStand = (eid) => { const d = inhalt(eid); const n = Number(K.stand[eid]?.fertig || 0);
    return Object.fromEntries((d?.inhalt?.etappen || []).map((x, i) => [x.lernziel, { fertig: i < n, sitzt: i < n, serie: i < n ? 4 : 0, ziel: 4, faellig: false }])); };
  const sichtbar = einheiten.filter((e) => K.route.some(([b]) => b === e.block_id) && e.status !== 'entwurf');
  return {
    schule_ich: { ok: true, rolle: 'kind', name: K.name, lernender_id: Number(kid), app: false },
    schule_uebersicht: { ok: true, leitung: false, einheiten: einheiten.map(({ datei, ...e }) => e), lernende: lernende.filter((l) => l.id === Number(kid)),
      orte: orte.map(({ einheiten: es, ...o }) => ({ ...o, ort: o.stadt, hat_einheit: es.some((x) => x[2] !== 'entwurf') })) },
    schule_konto: { ok: true, konto: K.konto, look: { stil: 'entdecker', welt: 'Ozean' },
      belohnungen: [{ id: 5, titel: 'Eis essen', kosten_sterne: 300, kosten_stempel: 0 }, { id: 6, titel: 'Kinoabend', kosten_sterne: 0, kosten_stempel: 3 }], einloesungen: [] },
    schule_merkheft: { ok: true, einheiten: sichtbar.map((e) => ({ einheit_id: e.id, block_id: e.block_id, stadt: e.stadt, ort_titel: e.ort_titel, kontinent: e.kontinent,
      etappen: inhalt(e.id)?.inhalt?.etappen || [], abschnitte: inhalt(e.id)?.inhalt?.abschnitte, stand: etStand(e.id), blocktest_fertig: !!K.stand[e.id]?.blocktest,
      nachtest: K.stand[e.id]?.blocktest ? { grund: 'noch_nicht_faellig', lerntage_noetig: 10, lerntage_seit: 4 } : { grund: 'einheit_offen' } })) },
    schule_wiederholung: { ok: true, faellig: K.wdh.length, aufgaben: K.wdh.map((eid, i) => { const d = inhalt(eid); const a = d.aufgaben.find((x) => x.p === 'uebung');
      return { id: 5000 + i, lernziel: a.l, antworttyp: a.y, frage: a.f, antworten: a.a, einheit_id: eid, stadt: E.get(eid).stadt, etappe: d.inhalt.etappen.find((x) => x.lernziel === a.l)?.titel }; }) },
    einheit: (eid) => { const d = inhalt(eid); const st = etStand(eid);
      return { ok: true, einheit_id: eid, status: 'freigegeben', inhalt: d.inhalt,
        uebungen: d.aufgaben.filter((a) => a.p === 'uebung').slice(0, 60).map((a, i) => ({ id: 9000 + i, lernziel: a.l, stufe: a.s, antworttyp: a.y, frage: a.f, antworten: a.a, tipp: a.h, versuche: 0, geloest: false })),
        stand: d.inhalt.etappen.map((x) => ({ lernziel: x.lernziel, pflicht: true, status: K.stand[eid]?.blocktest ? (K.stand[eid]?.fehler && x === d.inhalt.etappen[0] ? 'fehler' : 'nachgewiesen') : 'offen' })),
        etappen_stand: st, blocktest_fertig: !!K.stand[eid]?.blocktest, laufender_test: null,
        nachtest: K.stand[eid]?.blocktest ? { grund: 'noch_nicht_faellig', lerntage_noetig: 10, lerntage_seit: 4, art: 'runde', runde: 1 } : { grund: 'einheit_offen' } }; },
  };
}

async function einrichten(page, kid) {
  const A = antworten(kid);
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const req = route.request(); const pfad = new URL(req.url()).pathname; const b = JSON.parse(req.postData() || '{}');
    const ok = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
    if (pfad.endsWith('/anmelden')) return ok({ token: 't'.repeat(64), rolle: 'kind', name: KINDER[kid].name, lernender_id: Number(kid) });
    if (b.aktion === 'schule_einheit_lesen') return ok(A.einheit(b.daten.einheit_id));
    if (A[b.aktion]) return ok(A[b.aktion]);
    return route.fallback();
  });
}

const ORTE2 = O.orte.map(([block_id, titel, ziel_klasse, stadt, land, lat, lon, kontinent, einheiten]) => ({ block_id, titel, ziel_klasse, stadt, land, kontinent: O.kontinente[kontinent][0],
  themen: einheiten.map(([id, tid, status, karten]) => { const t = thema.get(tid) || {}; return { thema_id: tid, titel: t.titel || titel, jahrgang: t.klasse || {}, gebiet: t.gebiet || O.kontinente[kontinent][0], ort: stadt, block_id,
    stand: id === 44 || id === 50 ? 'erledigt' : id === 39 ? 'laeuft' : 'offen', einheit: { id, status, karten, aufgaben: karten * 18, neu: 0 } }; }) }));
const PLAN = [49, 55, 48, 83, 54, 87, 64, 86, 96, 95, 81, 79]; const SETZEN = [];
const KL = [{ id: 1, name: 'Kind A', klasse: 5, schulart: 'gym_by' }, { id: 2, name: 'Kind B', klasse: 8, schulart: 'gym_by' }];
async function einrichten(page) {
  const A1 = antworten('1'), A2 = antworten('2');
  const ueb = { ...A1.schule_uebersicht, leitung: true, lernende: [...A1.schule_uebersicht.lernende, ...A2.schule_uebersicht.lernende] };
  await page.route('**/functions/v1/lernen-api/**', async (route) => {
    const req = route.request(); const pfad = new URL(req.url()).pathname; const b = JSON.parse(req.postData() || '{}'); const d = b.daten || {};
    const ok = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
    if (pfad.endsWith('/anmelden')) return ok({ token: 't'.repeat(64), rolle: 'lehrer', name: 'Frau Lehrerin', lernender_id: null });
    if (b.aktion === 'schule_ich') return ok({ ok: true, rolle: 'lehrer', name: 'Frau Lehrerin', lernender_id: null, app: false });
    if (b.aktion === 'schule_uebersicht') return ok(ueb);
    const A = d.lernender_id === 2 ? A2 : A1;
    if (b.aktion === 'schule_einheit_lesen') return ok(A.einheit(d.einheit_id));
    if (['schule_konto', 'schule_merkheft', 'schule_wiederholung'].includes(b.aktion)) return ok(A[b.aktion]);
    if (b.aktion === 'schule_plan_lesen') return ok({ ok: true, kind: { ...(KL.find((k) => k.id === d.lernender_id) || KL[0]), stufen: {} }, revision: 3,
      plan: [{ block_id: 61, position: 0, art: 'rueckreise', status: 'offen', kann_schon: false }].filter(() => d.lernender_id === 2)
        .concat((d.lernender_id === 2 ? [73, 72, 60, 59, 71, 84, 92] : PLAN).map((block_id, i) => ({ route_id: i + 1, block_id, position: i + 1, art: 'normal', status: block_id === 55 || block_id === 73 ? 'fertig' : 'offen', kann_schon: false, ausgelassen: [] }))),
      orte: ORTE2, notizen: [{ id: 1, text: 'Bruchrechnen hat in der Schule gewackelt.', von: 'eltern:Papa', am: '2026-11-10T10:00:00Z' }],
      verlauf: [{ akteur: 'eltern:Papa', anlass: 'plan', am: '2026-11-14T09:00:00Z' }] });
    if (b.aktion === 'schule_plan_setzen') { SETZEN.push(d); return ok({ ok: true, revision: 4 + SETZEN.length, anzahl: (d.eintraege || []).length }); }
    if (b.aktion === 'schule_lehrplan_uebersicht') return ok({ ok: true, kinder: KL,
      themen: ORTE2.flatMap((o) => o.themen.map((t) => ({ ...t, stand: { 1: t.stand === 'offen' ? 'offen' : t.stand }, geplant: PLAN.includes(o.block_id) ? [1] : [], rueckmeldungen: 0 }))) });
    return route.fallback();
  });
}
const warte = async (p, ms = 500) => { await p.waitForFunction(() => !document.querySelector('#main .spinner'), null, { timeout: 6000 }).catch(() => {}); await p.waitForTimeout(ms); };
const bild = (p, name, ganz = true) => p.screenshot({ path: path.join(AUS, name + '.png'), fullPage: ganz });

// Szenarien: Lehrer spielt typische Aufgaben durch; gezählt werden Tipps und Scrollweg bis zur Antwort.
const ERG = {};
for (const [geraet, w, h] of [['tablet', 820, 1180], ['handy', 390, 844]]) {
  test(`Szenarien ${geraet}`, async () => {
    const nach = []; const { page: p } = await H.setup({ after: (f) => nach.push(f) }, { lernSeite: true, rolle: 'lehrer' });
    const E = ERG[geraet] = {};
    const start = async () => { await p.goto(H.origin + '/lernen/#/lernen'); await warte(p, 700); };
    const sichtbar = async (txt) => p.evaluate((t) => { const x = [...document.querySelectorAll('#main *')].find((e) => e.children.length === 0 && e.textContent.includes(t)); if (!x) return null; const r = x.getBoundingClientRect(); return { y: Math.round(r.top + scrollY), imBild: r.top >= 0 && r.bottom <= innerHeight }; }, txt);
    try {
      await p.setViewportSize({ width: w, height: h }); await einrichten(p);
      await p.goto(H.origin + '/lernen/'); await p.getByLabel('Lern-Code').fill('ABCD-EFGH-JKLM'); await p.getByRole('button', { name: 'Anmelden' }).click(); await warte(p, 900);
      // S0 erster Blick: was steht im ersten Bildschirm?
      E.s0 = await p.evaluate(() => [...document.querySelectorAll('#main h1,#main h2,#main h3,#main b,#main a,#main button')].filter((e) => { const r = e.getBoundingClientRect(); return r.top < innerHeight && r.bottom > 0 && e.textContent.trim(); }).map((e) => e.textContent.trim().slice(0, 50)));
      // S1 Hat Kind B diese Woche gelernt? -> Text „Letzte 7 Tage“
      E.s1 = { aufStart: await sichtbar('Letzte 7 Tage') };
      await p.locator('.lern-kindbereich').nth(1).getByRole('link', { name: /Was wackelt/ }).click(); await warte(p);
      E.s1.nach1Tipp = await sichtbar('Letzte 7 Tage'); await bild(p, `${geraet}-s1-wackelt-b`);
      // S2 Wo hakt es bei Kind A? welche falsche Antwort?
      await start(); await p.locator('.lern-kindbereich').first().getByRole('link', { name: /Was wackelt/ }).click(); await warte(p);
      E.s2 = { falscheSichtbar: await p.evaluate(() => [...document.querySelectorAll('#main details')].map((d) => ({ s: d.querySelector('summary')?.textContent.trim().slice(0, 60), offen: d.open }))) };
      for (const d of await p.locator('#main details:not([open]) > summary').all()) await d.click().catch(() => {});
      await p.waitForTimeout(300); await bild(p, `${geraet}-s2-wackelt-a-offen`);
      E.s2.text = await p.evaluate(() => document.querySelector('#main').innerText.replace(/\n{2,}/g, '\n').slice(0, 1800));
      // S3 Kind A kann „Teilbarkeit“ (Athen) schon -> Flugplan, Athen antippen, „kann es schon“
      await start(); let tipps = 0;
      await p.locator('.lern-kindbereich').first().getByRole('link', { name: /Flugplan/ }).click(); tipps++; await warte(p);
      await p.locator('.lern-plan-ort').filter({ hasText: 'Athen' }).click(); tipps++; await p.waitForTimeout(300);
      await bild(p, `${geraet}-s3-athen-auf`, false);
      SETZEN.length = 0; await p.locator('.lern-plan-zeile.offen .lern-plan-kann input').check(); tipps++; await p.waitForTimeout(500);
      E.s3 = { tipps, gespeichert: SETZEN.length, zeile: await p.locator('.lern-plan-zeile').nth(2).innerText() };
      // S4 Kind A kann „Ganze Zahlen“ (ein Flug in Rom) schon -> gibt es dafür etwas?
      await p.locator('.lern-plan-ort').filter({ hasText: 'Rom –' }).click(); await p.waitForTimeout(300); await bild(p, `${geraet}-s4-rom-auf`, false);
      E.s4 = { proFlug: await p.locator('.lern-plan-zeile.offen').first().evaluate((li) => [...li.querySelectorAll('label')].map((l) => l.innerText.trim() || l.querySelector('input')?.getAttribute('aria-label'))) ,
        hoeheOffen: await p.locator('.lern-plan-zeile.offen').first().evaluate((li) => Math.round(li.getBoundingClientRect().height)) };
      // S5 Melbourne (10) vor Kairo (4) -> mit Pfeilen: Anzahl Tipps
      await p.locator('.lern-plan-ort').filter({ hasText: 'Rom –' }).first().click(); await p.locator('.lern-plan-ort').filter({ hasText: 'Athen' }).first().click(); await p.waitForTimeout(200);
      let n = 0; for (let k = 0; k < 10; k++) { const nr = await p.locator('.lern-plan-zeile').evaluateAll((l) => l.findIndex((x) => x.innerText.includes('Melbourne'))); if (nr <= 3) break; await p.getByRole('button', { name: 'Melbourne – Zählen nach oben' }).click(); n++; await p.waitForTimeout(150); }
      E.s5 = { pfeilTipps: n };
      // S6 Geschaffte Orte: wo stehen sie im Plan?
      E.s6 = await p.locator('.lern-plan-zeile').evaluateAll((l) => l.map((x, i) => (x.classList.contains('fertig') ? `Platz ${i + 1} geschafft` : null)).filter(Boolean));
      // S7 Stufe je Schulart setzen: wie weit unten?
      E.s7 = { stufeY: await sichtbar('Stufe je Schulart'), seitenHoehe: await p.evaluate(() => document.documentElement.scrollHeight) };
      await bild(p, `${geraet}-s7-plan-ganz`);
      // S8 Lernstand Kind A: Feld Zahlen/Kl.5 antippen
      await start(); await p.locator('.lern-kindbereich').first().getByRole('link', { name: /^Lernstand/ }).click(); await warte(p);
      const feld = p.locator('#main a, #main button').filter({ hasText: '1/5' }).first(); E.s8 = { feldDa: await feld.count() };
      if (E.s8.feldDa) { await feld.click(); await warte(p); await bild(p, `${geraet}-s8-lernstand-feld`); E.s8.text = await p.evaluate(() => document.querySelector('#main').innerText.replace(/\n{2,}/g, '\n').slice(0, 1500)); E.s8.url = p.url().split('#')[1]; }
      // S9 Einstieg prüfen Kl. 6
      await p.goBack(); await warte(p); const kl6 = p.getByRole('button', { name: 'Kl. 6' }).or(p.getByRole('link', { name: 'Kl. 6' })).first();
      if (await kl6.count()) { await kl6.click(); await warte(p); await bild(p, `${geraet}-s9-einstieg6`); E.s9 = await p.evaluate(() => document.querySelector('#main').innerText.replace(/\n{2,}/g, '\n').slice(0, 1200)); }
      // S10 Bordkarte ändern lassen: Lehrplan -> Inhalte ansehen
      await p.goto(H.origin + '/lernen/#/lehrplan'); await warte(p); await p.getByRole('link', { name: 'Inhalte ansehen' }).first().click(); await warte(p);
      await bild(p, `${geraet}-s10-inhalte`); E.s10 = { hoehe: await p.evaluate(() => document.documentElement.scrollHeight), aendern: await p.getByText('Ändern lassen').count(), text: await p.evaluate(() => document.querySelector('#main').innerText.replace(/\n{2,}/g, '\n').slice(0, 900)) };
    } finally { for (const f of nach) await f(); fs.writeFileSync(path.join(__dirname, 'szenarien.json'), JSON.stringify(ERG, null, 1)); }
  });
}
