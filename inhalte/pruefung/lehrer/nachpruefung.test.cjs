'use strict';
const { test } = require('node:test');
const Module = require('node:module'); const fs = require('node:fs'); const path = require('node:path');
const root = path.resolve(__dirname, '..');
const quelle = path.join(root, 'tests/lernen.test.cjs'); const text = fs.readFileSync(quelle, 'utf8');
const m = new Module(quelle, module); m.filename = quelle; m.paths = Module._nodeModulePaths(path.dirname(quelle));
const vor = text.slice(0, text.indexOf("\ntest('"));
const la = text.slice(text.indexOf('const tagVor ='), text.indexOf("\ntest('LA-2: Startseite"));
const lp = text.slice(text.indexOf('const laPlan ='), text.indexOf("\ntest('LA-4: Plan zweispaltig"));
m._compile(vor + '\n' + la + '\n' + lp + '\nmodule.exports = { setup, laLage, laUebersicht, laPlan, get origin() { return origin; } };', quelle);
const H = m.exports;
const AUS = '/tmp/la/bilder'; fs.mkdirSync(AUS, { recursive: true });
const OUT = {}; process.on('exit', () => fs.writeFileSync('/tmp/la/mess.json', JSON.stringify(OUT, null, 1)));
const W = [['400', 400, 860], ['820', 820, 1180], ['1280', 1280, 800]];
const kombi = (opt = {}) => { const p = H.laPlan(opt); return (a, e) => H.laUebersicht(a, e) ?? p(a, e); };
const txt = (p) => p.evaluate(() => document.querySelector('#main').innerText);
const ruhe = (p, ms = 400) => p.waitForTimeout(ms);
for (const rolle of ['eltern', 'lehrer']) for (const [g, w, h] of W) {
  test(`${rolle} ${g}`, async (t) => {
    const lehrer = rolle === 'lehrer';
    const { page: p, calls } = await H.setup(t, lehrer ? { lernSeite: true, rolle: 'lehrer', anpassen: kombi() } : { anpassen: kombi() });
    if (lehrer) await p.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
    await H.laLage(p);
    await p.setViewportSize({ width: w, height: h });
    const B = H.origin + (lehrer ? '/lernen/#/' : '/#/');
    const r = OUT[`${rolle}-${g}`] = { texte: {} };
    const bild = (n, voll = true) => p.screenshot({ path: path.join(AUS, `${rolle}-${n}-${g}.png`), fullPage: voll });
    // 1 Startseite
    await p.goto(B + 'lernen'); await p.locator('.lern-zutun').waitFor(); await ruhe(p, 700);
    await bild('1-start', false); await bild('1-start-ganz');
    r.texte.start = await txt(p);
    r.zutun = await p.locator('.lern-zutun li').evaluateAll((ls) => ls.map((l) => [l.className, l.innerText.replace(/\s+/g, ' ').trim(), l.querySelector('a')?.getAttribute('href')]));
    const tab = p.locator('.lern-kinder-tabelle'); r.tabelleSichtbar = await tab.isVisible();
    const ziel = r.tabelleSichtbar ? tab : p.locator('.lern-kind-karte').last();
    const bb = await ziel.boundingBox().catch(() => null); r.tabelleUnten = bb ? Math.round(bb.y + bb.height) : null; r.fenster = h;
    r.kopf = r.tabelleSichtbar ? await tab.locator('thead th').allInnerTexts() : null;
    r.zeilen = r.tabelleSichtbar ? await tab.locator('tbody tr').evaluateAll((rs) => rs.map((x) => [...x.querySelectorAll('td,th')].map((c) => c.className + '|' + c.innerText.replace(/\s+/g, ' ').trim()))) : await p.locator('.lern-kind-karte').evaluateAll((ks) => ks.map((k) => k.innerText.replace(/\s+/g, ' ')));
    r.lernenStarten = await p.getByText('Lernen starten').count(); r.lernreiseAnsehen = await p.getByText(/Lernreise ansehen/).count();
    r.nachschlagen = await p.locator('#main').getByText('Nachschlagen').count();
    r.querRollen = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth);
    // Zu-tun-Einträge anklicken
    r.zutunZiel = [];
    for (let i = 0; i < r.zutun.length; i++) { await p.goto(B + 'lernen'); await p.locator('.lern-zutun li').nth(i).locator('a').click(); await ruhe(p, 500);
      r.zutunZiel.push([p.url().split('#')[1], await p.locator('.lern-reiter a[aria-current]').innerText().catch(() => '-'), (await p.locator('h1,h2').first().innerText().catch(() => '')).slice(0, 60)]); }
    // Zeile antippen
    await p.goto(B + 'lernen'); await ruhe(p, 500);
    if (r.tabelleSichtbar) await tab.locator('tbody tr', { hasText: 'Kind B' }).locator('td').nth(2).click(); else await p.locator('.lern-kind-karte', { hasText: 'Kind B' }).locator('a', { hasText: 'Kind B' }).first().click().catch(() => {});
    await ruhe(p); r.zeileZiel = p.url().split('#')[1];
    // 2 Kind-Seite
    for (const [k, n] of [['ueberblick', '2a-ueberblick'], ['wackelt', '2b-wackelt'], ['stand', '2c-stand'], ['plan', '2d-plan']]) {
      await p.goto(B + 'kind/1-' + k); await ruhe(p, 800);
      if (k === 'plan') { const rom = p.locator('.lern-plan-zeile', { hasText: 'Rom' }); await rom.locator('.lern-plan-ort').click().catch(() => {}); await ruhe(p); }
      await bild(n); r.texte[k] = await txt(p);
      if (k === 'ueberblick') r.kopfKind = await p.locator('.lern-kind-kopf').innerText().catch(() => '');
    }
    await p.goto(B + 'kind/2-ueberblick'); await ruhe(p, 800); await bild('2a-ueberblick-kindB'); r.texte.ueberblickB = await txt(p);
    r.umleitung = [];
    for (const alt of ['lernstand/1', 'wackelt/1', 'plan/1', 'lernstand/1-rs_by', 'lernstand/1-gym_by-7', 'schulstand']) { await p.goto(B + alt); await ruhe(p, 500); r.umleitung.push([alt, p.url().split('#')[1]]); }
    // 3 Besprochen
    await p.goto(B + 'kind/1-wackelt-1.runden'); await p.locator('.ls-detail').waitFor().catch(() => {}); await ruhe(p);
    await bild('3a-wackelt-offen');
    const bsp = p.locator('.ls-detail').getByRole('button', { name: 'Besprochen ✓' });
    if (await bsp.count()) { await bsp.click(); await ruhe(p, 600); r.besprochen = (await p.locator('.ls-tabelle tbody tr.ls-zeile').first().innerText()).replace(/\s+/g, ' '); r.besprochenCall = calls.filter((c) => c.aktion === 'schule_notiz_setzen').at(-1)?.daten; await bild('3b-besprochen'); }
    // kann schon je Flug
    await p.goto(B + 'kind/1-plan'); await ruhe(p, 800);
    const rom = p.locator('.lern-plan-zeile', { hasText: 'Rom' }); await rom.locator('.lern-plan-ort').click().catch(() => {});
    const ks = rom.getByLabel('Ganze Zahlen: kann schon'); r.kannSchonDa = await ks.count();
    if (r.kannSchonDa) { await ks.check(); await ruhe(p, 800); r.kannSchonCall = calls.filter((c) => c.aktion === 'schule_plan_setzen').at(-1)?.daten?.eintraege?.[0]; r.romNach = await rom.locator('.lern-plan-ort').innerText(); await bild('3c-kann-schon'); }
    r.spalten = await p.evaluate(() => { const a = document.querySelector('ol.lern-plan')?.getBoundingClientRect(), b = document.querySelector('.lern-plan-lehrplan')?.getBoundingClientRect(); return a && b ? (b.x > a.x + a.width - 5 ? 'zwei' : 'eine') : '?'; });
    // Einstellen
    await p.goto(B + 'kind/1-ueberblick'); await ruhe(p, 600);
    const eb = p.locator('.lern-kind-kopf').getByRole('button', { name: /einstellen/ });
    if (await eb.count()) { await eb.click(); await p.getByRole('dialog').waitFor(); await ruhe(p, 500); await bild('3d-einstellen', false); r.texte.blatt = await p.getByRole('dialog').innerText(); await p.keyboard.press('Escape'); }
    // Lehrplan
    await p.goto(B + 'lehrplan'); await ruhe(p, 900); await bild('3e-lehrplan'); r.texte.lehrplan = await txt(p);
    r.lehrplanQuer = await p.evaluate(() => { const t = document.querySelector('.lp-tabelle-lehrplan'); return t ? [Math.round(t.scrollWidth), Math.round(t.parentElement.clientWidth)] : null; });
    // Info-Seite
    await p.goto(B + 'info'); await ruhe(p, 500); r.texte.info = await txt(p);
  });
  test(`${rolle} ${g} geschafft`, async (t) => {
    const lehrer = rolle === 'lehrer';
    const { page: p } = await H.setup(t, lehrer ? { lernSeite: true, rolle: 'lehrer', anpassen: kombi({ romFertig: true }) } : { anpassen: kombi({ romFertig: true }) });
    if (lehrer) await p.addInitScript(() => localStorage.setItem('lern_token', 't'.repeat(64)));
    await p.setViewportSize({ width: w, height: h });
    await p.goto(H.origin + (lehrer ? '/lernen/#/' : '/#/') + 'kind/1-plan'); await p.locator('.lern-plan-zeile').first().waitFor().catch(() => {});
    const g2 = p.locator('details.lern-geschafft'); if (await g2.count()) { await g2.locator('summary').click(); }
    await p.waitForTimeout(500); await p.screenshot({ path: path.join(AUS, `${rolle}-3f-geschafft-${g}.png`), fullPage: true });
    OUT[`${rolle}-${g}-geschafft`] = await p.locator('#main').innerText();
  });
}
