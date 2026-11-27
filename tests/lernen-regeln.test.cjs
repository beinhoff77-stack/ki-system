// RU-App (0.95.0): Regel-Universum – Daten und Seiten ohne Browser (lernen-regeln.js, daten/regeln-universum.json, tools/regeln_bauen.cjs).
// Vorgabe inhalte/design/gesetzbuch/umsetzung7.md, Texte inhalte/mathe-profi/regeln-uebersicht/texte8/ (README: was der Bau übernehmen muss).
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const { bauen, ZIEL } = require(path.join(root, 'tools', 'regeln_bauen.cjs'));
const D = JSON.parse(fs.readFileSync(ZIEL, 'utf8'));
const L = new Function(fs.readFileSync(path.join(root, 'lernen-regeln.js'), 'utf8') + '\nreturn { ruIndex, ruSichten, ruEbene, ruKontext, ruRueckVorsatz, RU_ARTEN };')();
const I = L.ruIndex(D);
const T8 = (f) => JSON.parse(fs.readFileSync(path.join(root, 'inhalte/mathe-profi/regeln-uebersicht/texte8', f), 'utf8'));
const leer = (s) => typeof s !== 'string' || !s.replace(/<[^>]+>/g, '').trim();

test('Abgelegte Datei passt zum Bau aus den Quellen (tools/regeln_bauen.cjs)', () => {
  assert.equal(fs.readFileSync(ZIEL, 'utf8'), bauen().text, 'node tools/regeln_bauen.cjs ausführen');
});

test('Daten vollständig: 14 Regeln, 4 Schichten, 7 Gebiete, 28 Ideen, 8 Arbeitsweisen; jede Regel mit Merksatz, Kurzbeschreibung, Beispiel', () => {
  assert.equal(D.regeln.length, 14); assert.equal(D.etagen.length, 4); assert.equal(D.planeten.length, 7); assert.equal(I.IDEEN.length, 28); assert.equal(D.arbeitsweisen.length, 8);
  assert.deepEqual([1, 2, 3, 4].map((n) => D.regeln.filter((r) => r.etage === n).length).reduce((a, b) => a + b), 14);
  for (const r of D.regeln) {
    assert.ok(!leer(r.satz), r.id + ' Merksatz'); assert.ok(!leer(I.KURZ[r.id]), r.id + ' Kurzbeschreibung'); assert.ok(!leer(r.name), r.id + ' Name');
    assert.ok(I.felder(r.id).length >= 1 || I.LEITER[r.id].stufen.some((s) => s.text), r.id + ' Beispiel');
    assert.ok(I.LEITER[r.id].stufen.some((s) => s.text), r.id + ' Klassenleiter');
    assert.ok(!leer(r.fehler) && !leer(r.warum) && !leer(r.voraus), r.id + ' Fehler/Warum/Wann');
    assert.ok(D.lehrer[r.id] && D.lehrer[r.id].kennung, r.id + ' Lehrer-Blatt');
  }
  for (const i of I.IDEEN) { assert.ok(!leer(i.satz) && !leer(i.kurz) && !leer(I.KURZ[i.id]), i.id); assert.ok(I.felder(i.id).length >= 1, i.id + ' Zeichnung'); assert.ok(i.gesetze.every((g) => I.GESETZ[g]), i.id + ' Gesetze'); }
  for (const a of D.arbeitsweisen) for (const f of ['name', 'satz', 'kurz', 'erklaerung']) assert.ok(!leer(a[f]), a.name + ' ' + f);
  for (const a of D.arbeitsweisen) assert.ok(!leer(a.beispiel.text) && a.beispiel.klasse, a.name + ' Beispiel');
  assert.equal(D.gesetze.filter((g) => g.beispiel).length, 30, '30 ausgearbeitete Einzelregeln');
});

test('Texte der achten Runde übernommen: Regel 10 kürzere Fassung, Regel 6 unverändert, 18 berichtigte Kurzbeschreibungen, 25 Lücken', () => {
  assert.equal(I.REGEL.R10.satz, 'Plus, Minus: gleiche Nenner. Mal: oben mal oben, unten mal unten. Geteilt: mal Kehrwert.');
  assert.equal(I.REGEL.R6.satz, 'Was vor der Klammer steht, nimmt jeden in der Klammer mal.');
  const kb = T8('kurzbeschreibungen.json').eintraege;
  assert.equal(kb.filter((e) => e.befund === 'berichtigt').length, 18);
  for (const e of kb) assert.equal(I.KURZ[e.entwurf_schluessel], e.endfassung, e.entwurf_schluessel);
  let n = 0;
  for (const m of T8('merksaetze.json').regeln) for (const l of m.luecken) { const t = l.text.slice(1, 40); assert.ok(I.REGEL[m.entwurf_schluessel][l.wo].includes(t), `${m.entwurf_schluessel} ${l.wo}`); n++; }
  assert.equal(n, 25);
  const er = T8('einzelregeln.json'); for (const e of [...er.klasse5, ...er.klasse8]) { const g = I.GESETZ[e.id]; assert.equal(g.beispiel, e.beispiel.text); assert.ok((g.voraus + ' ' + g.fehler).includes(e.grenze.text.slice(1, 40)), e.id); }
  // Lehrer-Blatt: Lehrplan für alle 14, Beispielaufgaben für Regel 10 und 14 aus beispielaufgaben.json, „nicht geprüft“ bleibt stehen
  for (const r of D.regeln) { const lp = D.lehrer[r.id].lehrplan; assert.ok(lp && lp.nicht_geprueft.length, r.id + ' Lehrplan'); }
  assert.equal(D.lehrer.R10.aufgaben.length, 3); assert.equal(D.lehrer.R14.aufgaben.length, 3);
  assert.equal(D.lehrer.R9.aufgaben.length, 0, 'BG-05 passt laut Stichprobe nicht zu Regel 9'); assert.equal(D.lehrer.R9.zuordnung.befund, 'passt nicht');
  assert.equal(D.lehrer.R6.aufgaben.length, 3);
});

test('Suche findet erwartete Treffer', () => {
  const erster = (q) => I.suche(q)[0];
  assert.equal(erster('Kegelmantel').ziel.startsWith('regel-'), true); assert.match(erster('Kegelmantel').name + erster('Kegelmantel').satz, /Kegel/);
  assert.ok(I.suche('Klammer').slice(0, 5).some((t) => ['R6', 'R7'].includes(t.id)), 'Klammer → Regel 6 oder 7');
  assert.ok(I.suche('Probe').slice(0, 3).some((t) => t.art === 'Arbeitsweise' && t.name === 'Probe'), 'Probe → Arbeitsweise');
  assert.ok(I.suche('Kehrwert').slice(0, 5).some((t) => t.id === 'R10'), 'Kehrwert → Regel 10');
  assert.ok(I.suche('Prozent').length > 0); assert.ok(I.suche('Dreisatz').slice(0, 3).some((t) => t.id === 'R11'));
  assert.deepEqual(I.suche(''), []); assert.deepEqual(I.suche('xqzv'), []);
});

test('Alle Seiten bauen ohne leere Texte, ohne „undefined“/„NaN“, mit Brotkrumen ab „Universum“ und den Stufen in der Reihenfolge der Vorgabe', () => {
  const zustand = { klasse: 5, frage: 'Kegel' };
  const S = L.ruSichten(I, (h) => '#/regeln/1-' + h, zustand, 'kind');
  const adressen = ['universum', 'sonne', 'weisen', 'klassen', ...[5, 6, 7, 8, 9, 10].map((k) => 'klassen-' + k), 'suche',
    ...D.regeln.map((r) => r.id.toLowerCase()), ...I.IDEEN.map((i) => I.adr.idee(i.id)), ...D.arbeitsweisen.map((_, n) => 'weise-' + (n + 1)),
    ...D.planeten.map((p) => 'gebiet-' + p.kuerzel), ...D.gesetze.map((g) => I.adr.gesetz(g.id)), ...D.regeln.map((r) => I.adr.lehrer(r.id)), 'liste'];
  for (const h of adressen) {
    const html = S.seite(h);
    assert.doesNotMatch(html, /undefined|NaN|\[object/, h);
    assert.doesNotMatch(html, /<p class="ru-(kurz|merksatz|fliess|z-satz)"><\/p>/, h + ': leerer Text');
    if (!h.startsWith('lehrer') && h !== 'liste' && h !== 'universum') assert.match(html, /‹ Universum/, h + ': Brotkrume');
  }
  assert.equal(adressen.length, 4 + 6 + 1 + 14 + 28 + 8 + 7 + 152 + 14 + 1);
  const r6 = S.seite('r6');
  const pos = ['ru-kurz', 'Merksatz', 'Beispiel', 'data-stufe="klassen"', 'data-stufe="genau"', 'data-stufe="fehler"', 'data-stufe="aufbau"'].map((x) => r6.indexOf(x));
  assert.deepEqual([...pos].sort((a, b) => a - b), pos); assert.ok(pos.every((p) => p > 0));
  assert.doesNotMatch(r6, /<details[^>]* open/, 'Stufen 4–7 zu');
  // Liste der 14 Regeln: kein Bild, kein Beispiel; Merksatz in der Zeile (Regel 10 eine Zeile)
  const sonne = S.seite('sonne'); assert.equal((sonne.match(/class="ru-zeile ru-mit-satz"/g) || []).length, 14); assert.doesNotMatch(sonne, /ru-z-teil/);
  assert.match(sonne, /Plus, Minus: gleiche Nenner\. Mal: oben mal oben, unten mal unten\. Geteilt: mal Kehrwert\./);
  // Lehrer-Blatt: fünf Abschnitte, vier Rückmelde-Knöpfe, nichts zugeklappt, „Nicht geprüft“ offen
  const bl = S.seite('lehrer-r6'); assert.equal((bl.match(/class="ru-l-abschnitt"/g) || []).length, 5); assert.equal((bl.match(/class="ru-rueck"/g) || []).length, 4);
  assert.doesNotMatch(bl, /<details/); assert.match(bl, /Nicht geprüft:/); assert.match(bl, /Stand folgt/);
  // Ohne Lernstand: keine Platzhalter, die einen Stand vortäuschen
  for (const h of ['universum', 'sonne', 'r6', 'idee-fur-2']) assert.doesNotMatch(S.seite(h), /sitzt|geschafft|in Arbeit|Fortschritt/i, h);
  // Suche zeigt Treffer der Frage
  assert.match(S.seite('suche'), /Treffer für „Kegel“/);
});

test('Adressen und Ebenen; Rückmeldung nennt Regel, Name, Kennung und Abschnitt am Anfang des Textes', () => {
  assert.deepEqual(L.ruKontext('1'), { art: 'kind', kindId: 1, h: 'universum', praefix: '1-' });
  assert.deepEqual(L.ruKontext('12-idee-geo-1'), { art: 'kind', kindId: 12, h: 'idee-geo-1', praefix: '12-' });
  assert.equal(L.ruKontext('3-lehrer-r6').h, 'universum', 'Kind sieht kein Lehrer-Blatt');
  assert.deepEqual(L.ruKontext(null), { art: 'lehrer', h: 'liste', praefix: 'kind-' });
  assert.deepEqual(L.ruKontext('lehrer-r6'), { art: 'lehrer', h: 'lehrer-r6', praefix: 'kind-' });
  assert.equal(L.ruKontext('kind-r6').art, 'ansicht');
  assert.deepEqual(['universum', 'sonne', 'gebiet-geo', 'weisen', 'klassen-7', 'suche', 'r6', 'idee-geo-1', 'weise-3', 'lehrer-r6', 'regel-f17'].map(L.ruEbene), [0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3]);
  assert.equal(L.ruRueckVorsatz(I.REGEL.R6, 'rr.ausmultiplizieren', 'Karte')('Fehler'), 'Regel 6 · Ausmultiplizieren und Ausklammern (rr.ausmultiplizieren) · Karte · Fehler: ');
  // Arten passen zur Prüfbedingung der Tabelle schule.rueckmeldung (Migration 20261114_w150_lern_zugaenge_plan.sql)
  const erlaubt = fs.readFileSync(path.join(root, 'supabase/migrations/20261114_w150_lern_zugaenge_plan.sql'), 'utf8').match(/art text not null check \(art in \(([^)]*)\)\)/)[1];
  for (const a of L.RU_ARTEN) assert.ok(erlaubt.includes(`'${a[2]}'`), a[2]);
  assert.match(fs.readFileSync(path.join(root, 'supabase/migrations/20261117_w150_e3_auftraege_bezug.sql'), 'utf8'), /'plan', 'allgemein'\) then raise exception 'Unbekannter Bezug'/);
});
