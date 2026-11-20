'use strict';
const { test } = require('node:test');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
const st = (a, b) => text.slice(text.indexOf(a), b ? text.indexOf(b) : undefined);
const vor = text.slice(0, text.indexOf("\ntest('"));
const teile = [st('const tagVor =', "\ntest('LA-2: Startseite"), st('const laPlan =', "\ntest('LA-4: Plan zweispaltig"), st('const la8Orte =', "\ntest('LA-8: Flugplan rechts")];
if (!/const nachKlasse/.test(teile.join(''))) teile.push(text.slice(text.indexOf('const nachKlasse'), text.indexOf('\n', text.indexOf('const nachKlasse'))));
m._compile(vor + '\n' + teile.join('\n') + '\nmodule.exports = { setup, laLage, laUebersicht, laPlan, la8Orte, tagVor, get origin() { return origin; } };', quelle);
const H = m.exports;
const AUS = '/tmp/lb/bilder'; fs.mkdirSync(AUS, { recursive: true });
const OUT = {}; process.on('exit', () => fs.writeFileSync('/tmp/lb/mess.json', JSON.stringify(OUT, null, 1)));
const W = [['400', 400, 860], ['820', 820, 1180], ['1280', 1280, 800]];
const quer = (p) => p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
const abgeschn = (loc) => loc.evaluateAll((xs) => xs.filter((x) => x.scrollWidth > x.clientWidth + 1 || x.getBoundingClientRect().right > innerWidth + 1).map((x) => x.innerText.slice(0, 50)));
const pausenB = () => ({ a: { pausen: [] }, b: { pausen: [{ id: 5, von: H.tagVor(1), bis: H.tagVor(-3), grund: 'Reisetag', wer: 'lehrer:Herr Lehrer', am: new Date().toISOString() }] } });
async function mach(t, rolle, opt) {
  const lehrer = rolle === 'lehrer';
  const r = await H.setup(t, lehrer ? { lernSeite: true, rolle: 'lehrer', ...opt } : opt);
  if (lehrer) await r.page.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
  r.B = H.origin + (lehrer ? '/lernen/#/' : '/#/'); return r;
}
for (const [g, w, h] of W) for (const rolle of ['eltern', 'lehrer']) {
  test(`Start/Wackelt/Lehrplan ${rolle} ${g}`, async (t) => {
    const { page: p, B } = await mach(t, rolle, { anpassen: H.laUebersicht });
    await H.laLage(p, pausenB()); await p.setViewportSize({ width: w, height: h });
    const r = OUT[`a-${rolle}-${g}`] = {}; const bild = (n, voll = true) => p.screenshot({ path: path.join(AUS, `${rolle}-${n}-${g}.png`), fullPage: voll });
    await p.goto(B + 'lernen'); await p.locator('.lern-zutun').waitFor(); await p.waitForTimeout(700);
    await bild('1-start', false); await bild('1-start-ganz');
    r.zutun = await p.locator('.lern-zutun li').evaluateAll((ls) => ls.map((l) => l.className + ' | ' + l.innerText.replace(/\s+/g, ' ').trim()));
    r.zutunKopf = await p.locator('.lern-zutun').evaluate((z) => z.previousElementSibling?.innerText + ' || ' + (z.querySelector('h2,h3')?.innerText || ''));
    r.reisetagKnopf = await p.getByRole('button', { name: '+ Reisetag eintragen' }).count();
    r.wartet = await p.getByText(/WARTET AUF DICH/i).count();
    const tab = p.locator('.lern-kinder-tabelle');
    r.tabelle = await tab.isVisible() ? await tab.evaluate((t) => ({ unten: Math.round(t.getBoundingClientRect().bottom), kopf: [...t.querySelectorAll('thead th')].map((x) => x.innerText), zeilen: [...t.querySelectorAll('tbody tr')].map((tr) => [...tr.children].map((c) => c.className + '|' + c.innerText.replace(/\s+/g, ' ')).join(' ¦ ')) })) : 'Karten';
    if (r.tabelle === 'Karten') r.karten = await p.locator('.lern-kind-karte').allInnerTexts();
    r.quer = await quer(p);
    // Wackelt
    await p.goto(B + 'kind/1-wackelt'); await p.waitForTimeout(800); await bild('2-wackelt');
    r.wackeltKarten = await p.locator('.ls-karte-m').count(); r.wackeltTabelle = await p.locator('.ls-tabelle').isVisible();
    r.wackeltAbgeschn = await abgeschn(p.locator('.lern-reiter a, .ls-karte-kopf b, .ls-karte-werte span, .ls-tabelle th, .ls-tabelle td'));
    r.wackeltText = (await p.locator('#main').innerText()).slice(0, 900); r.wackeltQuer = await quer(p);
    // Überblick Kind B
    await p.goto(B + 'kind/2-ueberblick'); await p.waitForTimeout(800); await bild('3-ueberblick-B'); r.ueberblickB = (await p.locator('#main').innerText()).slice(0, 1200);
    // Lehrplan
    await p.goto(B + 'lehrplan'); await p.waitForTimeout(900); await bild('4-lehrplan');
    r.lehrplanListe = await p.locator('.lp-liste-eintrag').count(); r.lehrplanQuer = await quer(p);
    r.lehrplanAbgeschn = await abgeschn(p.locator('.lp-liste-eintrag b, .lp-liste-kinder span, .lp-tabelle-lehrplan td'));
    // Reisetag eintragen
    if (r.reisetagKnopf) { await p.goto(B + 'lernen'); await p.getByRole('button', { name: '+ Reisetag eintragen' }).click(); const bl = p.getByRole('dialog', { name: 'Reisetag eintragen' }); await bl.waitFor(); await p.waitForTimeout(400); await bild('5-reisetag-blatt', false); r.reisetagBlatt = await bl.innerText(); await p.keyboard.press('Escape'); }
    // Einstellen mit Pausen
    await p.goto(B + 'kind/2-ueberblick'); await p.waitForTimeout(600);
    await p.locator('.lern-kind-kopf').getByRole('button', { name: /einstellen/ }).click(); await p.getByRole('dialog').waitFor(); await p.waitForTimeout(400);
    const pk = p.locator('.lern-pause'); if (await pk.count()) { await pk.scrollIntoViewIfNeeded(); await p.waitForTimeout(200); }
    await bild('6-einstellen', false); r.einstellen = await p.getByRole('dialog').innerText();
    await p.keyboard.press('Escape');
    // Info
    await p.goto(B + 'info'); await p.waitForTimeout(500);
    for (const s of await p.locator('#main details summary').all()) await s.click().catch(() => {});
    const it = await p.locator('#main').innerText(); const i = it.indexOf('Reisetage'); r.info = i >= 0 ? it.slice(i, i + 700) : 'nicht gefunden';
    const j = it.indexOf('Themengebiet'); r.infoLa8 = j >= 0 ? it.slice(Math.max(0, j - 200), j + 600) : 'nicht gefunden';
  });
  test(`ohne Pausen-Migration ${rolle} ${g}`, async (t) => {
    const { page: p, B } = await mach(t, rolle, { anpassen: H.laUebersicht });
    await H.laLage(p); await p.setViewportSize({ width: w, height: h });
    const r = OUT[`b-${rolle}-${g}`] = {};
    await p.goto(B + 'lernen'); await p.locator('.lern-zutun').waitFor(); await p.waitForTimeout(500);
    r.reisetagKnopf = await p.getByRole('button', { name: '+ Reisetag eintragen' }).count();
    r.zutun = await p.locator('.lern-zutun li').allInnerTexts();
    await p.goto(B + 'kind/1-ueberblick'); await p.waitForTimeout(500);
    await p.locator('.lern-kind-kopf').getByRole('button', { name: /einstellen/ }).click(); await p.getByRole('dialog').waitFor();
    r.einstellen = await p.getByRole('dialog').innerText();
  });
  test(`LA-8 ${rolle} ${g}`, async (t) => {
    const { page: p, B, calls } = await mach(t, rolle, { anpassen: H.la8Orte });
    await p.setViewportSize({ width: w, height: h });
    const r = OUT[`c-${rolle}-${g}`] = {}; const bild = (n, voll = true) => p.screenshot({ path: path.join(AUS, `${rolle}-${n}-${g}.png`), fullPage: voll });
    await p.goto(B + 'kind/1-plan'); const lp = p.locator('.lern-plan-lehrplan'); await lp.getByRole('group', { name: 'Ansicht' }).waitFor(); await p.waitForTimeout(600);
    await bild('7-la8-gebiet');
    r.umschalter = await lp.getByRole('group', { name: 'Ansicht' }).getByRole('button').evaluateAll((b) => b.map((x) => x.innerText + (x.getAttribute('aria-pressed') === 'true' ? ' *' : '')));
    r.gebiete = await lp.getByRole('group', { name: 'Themengebiet' }).getByRole('button').evaluateAll((b) => b.map((x) => x.innerText + (x.getAttribute('aria-pressed') === 'true' ? ' *' : '')));
    r.sortiert = await lp.getByRole('group', { name: 'Sortiert nach Klasse in' }).getByRole('button').evaluateAll((b) => b.map((x) => x.innerText + (x.getAttribute('aria-pressed') === 'true' ? ' *' : '')));
    r.kopf = await lp.locator('.lern-plan-gebiet-kopf').innerText();
    r.linie = await lp.locator('.lern-plan-ab-hier').evaluate((x) => [x.innerText, getComputedStyle(x).borderTopStyle, getComputedStyle(x).borderTopColor]);
    r.links = await p.locator('.lern-plan-zeile .lern-plan-ort').evaluateAll((z) => z.map((x) => x.innerText.replace(/\s+/g, ' ')));
    r.rechts = await lp.locator('.lern-plan-vorrat-zeile').evaluateAll((z) => z.map((x) => x.innerText.replace(/\s+/g, ' ')));
    r.abgeschnLinks = await p.locator('.lern-plan-zeile .lern-plan-ort > b').evaluateAll((xs) => xs.filter((x) => x.scrollWidth > x.clientWidth + 1).map((x) => x.innerText));
    r.abgeschnRechts = await lp.locator('.lern-plan-vorrat-zeile .lern-plan-ort > b').evaluateAll((xs) => xs.filter((x) => x.scrollWidth > x.clientWidth + 1).map((x) => x.innerText));
    r.legende = await lp.locator('.lern-kl-legende').evaluate((x) => ({ text: x.innerText.replace(/\s+/g, ' '), unten: Math.round(x.getBoundingClientRect().bottom), spalteUnten: Math.round(x.closest('.lern-plan-lehrplan').getBoundingClientRect().bottom) }));
    r.farben = await p.locator('.lern-plan-zeile, .lern-plan-vorrat-zeile').evaluateAll((zs) => zs.map((z) => [z.querySelector('.lern-kl-kasten')?.textContent, getComputedStyle(z).borderLeftColor, getComputedStyle(z).backgroundImage.slice(0, 60)]));
    r.quer = await quer(p);
    r.spalten = await p.evaluate(() => { const a = document.querySelector('ol.lern-plan')?.getBoundingClientRect(), b = document.querySelector('.lern-plan-lehrplan')?.getBoundingClientRect(); return a && b ? (b.x > a.x + a.width - 5 ? 'zwei' : 'eine') : '?'; });
    // Gym-9 mit einem Tipp
    await lp.getByRole('button', { name: '+ Kyoto – Wurzeln' }).click(); await p.waitForTimeout(700);
    r.nachPlus = calls.filter((c) => c.aktion === 'schule_plan_setzen').at(-1)?.daten?.eintraege?.map((x) => x.block_id);
    r.neuLinks = await p.locator('.lern-plan-zeile').last().innerText();
    await bild('8-la8-gym9');
    // Realschule
    await lp.getByRole('group', { name: 'Sortiert nach Klasse in' }).getByRole('button', { name: 'Realschule' }).click(); await p.waitForTimeout(300);
    r.rechtsRS = await lp.locator('.lern-plan-vorrat-zeile .lern-plan-ort').evaluateAll((z) => z.map((x) => x.innerText.replace(/\s+/g, ' ')));
    r.linieRS = await lp.locator('.lern-plan-ab-hier').innerText().catch(() => '-');
    await lp.getByRole('group', { name: 'Sortiert nach Klasse in' }).getByRole('button', { name: 'IB MYP' }).click(); await p.waitForTimeout(300);
    r.linieIB = await lp.locator('.lern-plan-ab-hier').innerText().catch(() => '-');
    r.rechtsIB = await lp.locator('.lern-plan-vorrat-zeile .lern-plan-ort').evaluateAll((z) => z.map((x) => x.innerText.replace(/\s+/g, ' ')));
    // Nach Klasse
    await lp.getByRole('button', { name: 'Nach Klasse (Lehrplan)' }).click(); await p.waitForTimeout(500); await bild('9-la8-klasse');
    r.klasse = (await lp.innerText()).replace(/\s+/g, ' ').slice(0, 700);
  });
}
