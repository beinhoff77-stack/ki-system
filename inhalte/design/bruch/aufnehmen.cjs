// Bruch-Darstellung prüfen: App unverändert, echte Aufgaben aus inhalte/themen, nachgestellte Server-Antworten.
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = '/home/claude/ki-system'; const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
m._compile(text.slice(0, text.indexOf("\ntest('")) + '\nmodule.exports = { setup, get origin() { return origin; }, vor: (typeof before !== "undefined") };', quelle);
const H = m.exports; const { test } = require('node:test');
const AUS = process.env.AUS || '/home/claude/rs/bruch/'; fs.mkdirSync(AUS, { recursive: true });
const lade = (f) => JSON.parse(fs.readFileSync(`${root}/inhalte/themen/${f}.json`, 'utf8'));
const FAELLE = [['a-frage-3-4', 'bruch.brueche', 13, { wert: '24' }], ['b-auswahl', 'bruch.brueche', 149, { index: 1 }], ['c-loesungsweg-bruchterm', 'terme.bruchterme', 240, { wert: '6' }],
  ['c2-loesungsweg-bruchgleichung', 'gleichungen.bruch', 202, null], ['d-gemischte-zahl', 'bruch.prozent', 175, { wert: '125' }]];
const nur = process.env.NUR ? process.env.NUR.split(',') : null; const MESS = {};
for (const [name, datei, idx] of FAELLE) for (const w of [360, 400]) for (const g of ['tag', 'nacht']) {
  if (nur && !nur.includes(`${name}-${w}-${g}`)) continue;
  test(`${name} ${w} ${g}`, async (t) => {
    const d = lade(datei); const a = d.aufgaben[idx]; const et = d.inhalt.etappen.find((x) => x.lernziel === a.l);
    const { page: p } = await H.setup(t, { lernSeite: true, rolle: 'kind', gestaltung: g });
    await p.setViewportSize({ width: w, height: 800 }); await p.emulateMedia({ reducedMotion: 'reduce' });
    const auf = { id: 11, lernziel: a.l, stufe: a.s, antworttyp: a.y, frage: a.f, antworten: a.a, tipp: a.h, versuche: 0, geloest: false };
    await p.route('**/functions/v1/lernen-api/**', async (route) => { const b = JSON.parse(route.request().postData() || '{}');
      const ok = (e) => route.fulfill({ contentType: 'application/json', body: JSON.stringify({ ok: true, ergebnis: e }) });
      if (b.aktion === 'schule_einheit_lesen') return ok({ ok: true, einheit_id: 1, status: 'freigegeben', inhalt: { ziel: d.inhalt.ziel, etappen: [et] }, uebungen: [auf, { ...auf, id: 12 }],
        stand: [{ lernziel: a.l, pflicht: true, status: 'offen' }], etappen_stand: { [a.l]: { fertig: false, ziel: 4, serie: 0 } }, laufender_test: null });
      if (b.aktion === 'schule_uebung_pruefen') return ok({ ok: true, format_ok: true, richtig: true, loesung: a.o, loesungsweg: a.w, karte: { serie: 1, ziel: 4, sitzt: false, neu_sitzt: false } });
      return route.fallback(); });
    await p.goto(H.origin + '/lernen/'); await p.getByLabel('Lern-Code').fill('ABCD-EFGH-JKLM'); await p.getByRole('button', { name: 'Anmelden' }).click(); await p.waitForURL(/#\/reise\/1$/);
    await p.goto(H.origin + '/lernen/#/lerneinheit/1-1-1'); await p.waitForTimeout(900);
    const loes = name.startsWith('c');
    if (loes) { if (a.y === 'auswahl') await p.locator('.lern-option').nth(a.o.index).click(); else await p.getByRole('textbox').first().fill(String(a.o.wert)); await p.getByRole('button', { name: 'Prüfen' }).click(); await p.locator('.lr-rueck').waitFor(); await p.waitForTimeout(300); }
    const mess = await p.evaluate(() => { const px = (e, k = 'fontSize') => Math.round(parseFloat(getComputedStyle(e)[k]) * 10) / 10; const aus = { quer: document.documentElement.scrollWidth > innerWidth, orte: [] };
      const zeilen = (e) => { const r = document.createRange(); r.selectNodeContents(e); return new Set([...r.getClientRects()].map((x) => Math.round(x.bottom))).size; };
      for (const [was, sel] of [['Frage', '.lern-frage'], ['Antwortknopf', '.lern-option'], ['Rückmeldung', '.lr-rueck p, .lr-rueck b'], ['Tipp', '.lr-tipp']]) for (const e of document.querySelectorAll(sel)) { if (!e.offsetParent) continue;
        const br = [...e.querySelectorAll('.lern-bruch-text')]; if (!br.length) { if (was === 'Antwortknopf') aus.orte.push({ was, ohneBruch: true, hoehe: Math.round(e.getBoundingClientRect().height) }); continue; }
        const b0 = br[0]; aus.orte.push({ was, text: e.innerText.replace(/\n/g, '⏎').slice(0, 60), schrift: px(e.querySelector('span:not(.lern-bruch-text)') || e), zeilenhoehe: px(e, 'lineHeight'), hoehe: Math.round(e.getBoundingClientRect().height),
          brueche: br.length, ziffer: px(b0.firstChild), bruchHoehe: Math.round(b0.getBoundingClientRect().height), bruchBreiteMax: Math.round(Math.max(...br.map((x) => x.getBoundingClientRect().width))), breite: Math.round(e.getBoundingClientRect().width),
          ragtRaus: br.some((x) => x.getBoundingClientRect().right > e.getBoundingClientRect().right + 1) }); }
      return aus; });
    MESS[`${name}-${w}-${g}`] = mess;
    const h = await p.evaluate(() => document.documentElement.scrollHeight); await p.setViewportSize({ width: w, height: Math.max(700, h) }); await p.waitForTimeout(200);
    await p.screenshot({ path: `${AUS}${name}-${w}-${g === 'tag' ? 'hell' : 'dunkel'}.png`, fullPage: true });
    const karte = p.locator('.lr-bordkarte, .lern-aufgabe, .lr-karte').first(); if (process.env.SCHAU) console.log(await p.evaluate(() => [...document.querySelectorAll('[class]')].filter((x) => x.querySelector(':scope > .lern-frage')).map((x) => x.className + ' < ' + x.parentElement.className)));
  });
}
test('Messung', () => fs.writeFileSync(AUS + 'messung.json', JSON.stringify(MESS, null, 1)));
