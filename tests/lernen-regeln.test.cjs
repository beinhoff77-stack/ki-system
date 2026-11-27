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

test('Texte der achten Runde übernommen: Regel 10 kürzere Fassung, Regel 6 und 7 als Merksatz = Kurzfassung, 23 berichtigte Kurzbeschreibungen, 25 Lücken', () => {
  assert.equal(I.REGEL.R10.satz, 'Plus/Minus: erst gleiche Nenner. Mal: oben mal oben, unten mal unten. Geteilt: mal Kehrwert.');
  assert.equal(I.REGEL.R6.satz, 'Ein Faktor vor einer Summe multipliziert jeden Summanden.'); assert.equal(I.REGEL.R7.satz, 'Beim Auflösen einer Minusklammer wechselt jeder Summand sein Vorzeichen.');
  const kb = T8('kurzbeschreibungen.json').eintraege;
  assert.equal(kb.filter((e) => e.befund === 'berichtigt').length, 23);
  for (const e of kb) assert.equal(I.KURZ[e.entwurf_schluessel], e.endfassung, e.entwurf_schluessel);
  let n = 0;
  for (const m of T8('merksaetze.json').regeln) for (const l of m.luecken) { const t = l.text.slice(1, 40); assert.ok(I.REGEL[m.entwurf_schluessel][l.wo].includes(t), `${m.entwurf_schluessel} ${l.wo}`); n++; }
  assert.equal(n, 25);
  const er = T8('einzelregeln.json'); for (const e of [...er.klasse5, ...er.klasse8]) { const g = I.GESETZ[e.id]; assert.equal(g.beispiel, e.beispiel.text); assert.ok((g.voraus + ' ' + g.fehler).includes(e.grenze.text.slice(1, 40)), e.id); }
  // Lehrer-Blatt: Lehrplan für alle 14, Beispielaufgaben für Regel 10 und 14 aus beispielaufgaben.json, „nicht geprüft“ bleibt stehen
  for (const r of D.regeln) { const lp = D.lehrer[r.id].lehrplan; assert.ok(lp && lp.nicht_geprueft.length, r.id + ' Lehrplan'); }
  assert.equal(D.lehrer.R10.aufgaben.length, 3); assert.equal(D.lehrer.R14.aufgaben.length, 3);
  assert.equal(D.lehrer.R9.zuordnung.befund, 'passt nicht'); assert.ok(!D.lehrer.R9.aufgaben.some((a) => /BG-05/.test(a.kopf)), 'BG-05 gehört zu Regel 13, nicht zu Regel 9');
  assert.ok(D.lehrer.R13.aufgaben.length === 3 && D.lehrer.R9.aufgaben.length === 3 && D.lehrer.R11.aufgaben.length === 3);
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
  assert.match(sonne, /Plus\/Minus: erst gleiche Nenner\. Mal: oben mal oben, unten mal unten\. Geteilt: mal Kehrwert\./);
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

// ---------- Gegenprüfung (Werkstatt 1078/1079): geprüft wird, was die App anzeigt (daten/regeln-universum.json) ----------
const alleLeiterTexte = () => Object.entries(D.leitern).flatMap(([k, l]) => l.stufen.filter((s) => s.text).map((s) => ({ k, klasse: s.klasse, text: s.text })));
const text = (k, kl) => D.leitern[k].stufen.find((s) => s.klasse === kl && s.text).text;

test('Grenztexte stehen im aufgeschlagenen Text der Regel (Genau gesagt, Wann sie gilt, Typische Fehler)', () => {
  assert.match(D.regeln.find((r) => r.id === 'R4').voraus, /Beim Bruch fasst der Strich Zähler und Nenner jeweils zusammen\. Unter der Wurzel und zwischen Betragsstrichen gehört jeweils der ganze eingeschlossene Ausdruck zusammen/);
  assert.match(I.REGEL.R4.voraus, /2 hoch \(3²\) = 2 hoch 9 = 512|2 hoch \(3²\) = 2⁹ = 512/);
  assert.match(I.REGEL.R6.voraus, /5 \+ \(x − 2\) = 5 \+ x − 2/); assert.match(I.REGEL.R6.voraus, /3 · \(2 · 5\) = 3 · 10 = 30/);
  assert.match(I.REGEL.R10.voraus, /Gemischte Zahlen zuerst in einen Bruch/); assert.match(I.REGEL.R10.fehler, /Kehrwert|kehren/);
  assert.match(I.REGEL.R11.voraus, /umgekehrt\w* Proportionalität/);
  assert.doesNotMatch(Object.values(I.REGEL.R11).filter((v) => typeof v === 'string').join(' '), /nur bei direkter Proportionalität/i, 'R11: alter Bestandstext muss weg');
  assert.match(I.REGEL.R12.voraus, /Runden lässt sich nicht eindeutig rückgängig machen/); assert.match(I.REGEL.R12.voraus, /\|x\| = 3 hat die Lösungen x = −3 und x = 3/);
  assert.doesNotMatch(I.REGEL.R12.voraus, /Betrag lassen sich nicht umkehren/);
  assert.match(I.REGEL.R14.fehler, /nicht durch x teilen|durch x teilen/);
  // jeder Grenztext aus texte8 steht im Feld, das die Seite zeigt: genau → „Genau gesagt“, voraus → „Wann sie gilt“, fehler → Stufe „Typische Fehler“
  for (const m of T8('merksaetze.json').regeln) for (const l of m.luecken) assert.ok(I.REGEL[m.entwurf_schluessel][l.wo].includes(l.text.slice(1)), m.entwurf_schluessel + ' ' + l.wo);
  const S = L.ruSichten(I, (h) => '#/regeln/1-' + h, { klasse: 5, frage: '' }, 'kind');
  for (const [id, stuecke] of [['r4', ['Betragsstrichen', 'Potenzen übereinander|Hochzahlen übereinander']], ['r6', ['Plus davor']], ['r10', ['Gemischte Zahlen']], ['r11', ['umgekehrter Proportionalität']], ['r14', ['[Dd]urch x teilen']]]) {
    const html = S.seite(id).replace(/&#124;/g, '|'); for (const st of stuecke) assert.match(html, new RegExp(st), id + ': ' + st);
  }
});

test('Klassenbeispiele kommen aus einer Quelle (Leiter-Datei); regeln[].klassen ist nicht mehr in den App-Daten', () => {
  for (const r of D.regeln) assert.ok(!('klassen' in r), r.id + ' hat noch regeln[].klassen');
  const ld = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/mathe-profi/regeln-uebersicht/klassenleiter.json'), 'utf8')).leitern;
  const nachKennung = Object.fromEntries(Object.values(D.leitern).map((l) => [l.kennung, l]));
  for (const q of ld) { const l = nachKennung[q.kennung]; assert.ok(l, q.kennung); assert.deepEqual(l.stufen.map((s) => s.text || null), q.stufen.map((s) => (s.kommt_vor ? s.text : null)), q.kennung); }
  assert.equal(text('R7', 8), '7 − (2x − 6) = 7 − 2x + 6 = 13 − 2x');
});

test('Berichtigte Klassenbeispiele: Oberflächen eindeutig, Hochzahlen und Brüche mit Klammern, Nenner-Nullstellen gekennzeichnet', () => {
  assert.equal(text('I-fur-4', 5), 'Quader 5 · 4 · 3 cm: 2 · 20 + 2 · 15 + 2 · 12 = 94 cm²');
  assert.equal(2 * 20 + 2 * 15 + 2 * 12, 2 * (5 * 4 + 5 * 3 + 4 * 3)); assert.equal(2 * 6 + 18 + 24 + 30, 84); assert.equal(36 + 4 * (6 * 5 / 2), 96);
  assert.match(text('I-fur-4', 8), /^Gerades Prisma \(Dreiecksseiten 3, 4, 5 cm, Höhe 6 cm\): 2 · 6 \+ 18 \+ 24 \+ 30 = 84 cm²$/);
  assert.match(text('I-fur-4', 10), /36 \+ 60 = 96 cm²/);
  assert.equal(text('R8', 10), '2ˣ · 2³ = 2⁽ˣ⁺³⁾');
  assert.equal(text('R10', 8), '1/x + 1/(2x) = 2/(2x) + 1/(2x) = 3/(2x), für x ≠ 0');
  assert.match(text('R14', 8), /ist null für x = 0 oder x = 4: beide Werte sind ausgeschlossen/);
  assert.equal(text('R6', 8), 'x · (3/x + ½) = x · (3/x) + x · ½, für x ≠ 0');
  for (const { k, klasse, text: t } of alleLeiterTexte()) { assert.doesNotMatch(t, /\d\/\d?[a-z]\d?x|\/\d+x[ ,]|hoch x \+ 3/, `${k} Klasse ${klasse}: mehrdeutige Schreibweise ${t}`); }
  // markierte Stellen liegen im Text
  for (const [k, l] of Object.entries(D.leitern)) for (const s of l.stufen) if (s.text) for (const [a, b] of s.pos) assert.ok(a >= 0 && b <= s.text.length && b > a, `${k} ${s.klasse}`);
});

test('Nur Endfassungen der Kurzbeschreibungen werden angezeigt (nie die alte Designer-Fassung)', () => {
  const alt = JSON.parse(fs.readFileSync(path.join(root, 'inhalte/design/gesetzbuch/entwurf7/teile/kurz.json'), 'utf8')).texte;
  const kb = T8('kurzbeschreibungen.json').eintraege;
  for (const e of kb) { assert.equal(D.kurz[e.entwurf_schluessel], e.endfassung, e.entwurf_schluessel); assert.ok(e.endfassung.length <= 110, e.entwurf_schluessel + ' Länge');
    if (e.befund === 'berichtigt') assert.notEqual(D.kurz[e.entwurf_schluessel], alt[e.entwurf_schluessel].text, e.entwurf_schluessel + ' zeigt noch die alte Fassung'); }
  assert.equal(Object.keys(D.kurz).length, 42);
  const S = L.ruSichten(I, (h) => '#/regeln/1-' + h, { klasse: 5, frage: '' }, 'kind');
  for (const id of ['r3', 'r5', 'r8', 'r9', 'r10', 'r11']) assert.ok(S.seite(id).includes(D.kurz[id.toUpperCase()].replace(/&/g, '&amp;')), id);
  assert.match(D.kurz['I-algebra-2'], /Quadratwurzel über den reellen Zahlen/);
  assert.match(D.kurz['I-geo-5'], /^Mit Pythagoras berechnet man/); assert.match(D.kurz['I-daten-3'], /gleich wahrscheinlich/);
});

test('Lehrplan-Bezug ist als redaktionelle Einordnung gekennzeichnet; Arbeitsweisen und Einzelregeln berichtigt', () => {
  for (const r of D.regeln) { const lp = D.lehrer[r.id].lehrplan; assert.match(lp.befund, /Redaktionelle Einordnung/); assert.match(lp.befund, /nicht hinterlegt/); assert.doesNotMatch(lp.befund, /gegen den Lehrplan geprüft(?!“)/); }
  const S = L.ruSichten(I, (h) => '#/regeln/1-' + h, { klasse: 5, frage: '' }, 'lehrer');
  assert.match(S.seite('lehrer-r6'), /Redaktionelle Einordnung/);
  const w = D.arbeitsweisen.find((a) => a.name === 'Begründen'); assert.match(w.kurz, /allgemeine Behauptung widerlegt ein Gegenbeispiel/);
  assert.match(D.arbeitsweisen.find((a) => a.name === 'Einheiten').beispiel.text, /im Durchschnitt/);
  assert.match(I.GESETZ.V1.fehler, /Faktor 10/); assert.match(I.GESETZ.V1.fehler, /Zeit wird nicht dezimal umgerechnet/);
  assert.match(I.GESETZ.Z6.fehler, /positive natürliche Zahlen/); assert.match(I.GESETZ.V7.satz, /Klasse 5/); assert.match(I.GESETZ.D9.satz, /n − 1/);
});

// ---------- Zweite Gegenprüfung (Werkstatt 1090): wieder an den angezeigten Daten ----------
test('1090: Kurzkarten, Ideen-Texte und Einzelregeln zeigen die berichtigten Fassungen', () => {
  assert.equal(D.kurz.R6, 'Ein Faktor vor einer Summe multipliziert jeden Summanden.');
  assert.equal(D.kurz.R7, 'Beim Auflösen einer Minusklammer wechselt jeder Summand sein Vorzeichen.');
  assert.match(D.kurz.R3, /ungleich null/); assert.match(D.kurz.R8, /positiver ganzzahliger Hochzahl/);
  assert.match(D.kurz['I-funktionen-2'], /gleichen x-Schritten/); assert.match(D.kurz['I-fur-2'], /Grenzwert folgt exakt A = πr²/);
  assert.match(I.REGEL.R7.genau, /−\(a \+ \(b − c\)\) = −a − \(b − c\)/);
  assert.match(I.REGEL.R11.fehler, /Produkt beider Größen konstant/); assert.match(I.REGEL.R11.voraus, /Bei gleicher Leistung jeder Person/);
  assert.match(I.REGEL.R9.fehler, /= 3 für x ≠ −2/); assert.match(I.REGEL.R9.genau, /gemeinsamen Teiler/);
  const ide = (id) => D.planeten.flatMap((p) => p.ideen).find((i) => i.id === id);
  assert.match(ide('I-algebra-4').warum, /jeden Faktor einzeln gleich null/); assert.doesNotMatch(ide('I-algebra-4').warum, /Jeder Faktor liefert eine Lösung/);
  assert.match(ide('I-funktionen-1').warum, /y = x als auch y = x² passen zu \(0 \| 0\) und \(1 \| 1\)/);
  assert.match(ide('I-funktionen-2').genau, /A > 0.*q > 1.*0 < q < 1.*q = 1/); assert.match(ide('I-funktionen-3').genau, /a ≠ 0 und x ≠ 0/);
  assert.match(ide('I-geo-5').genau, /zwei Seiten oder eine Seite und ein spitzer Winkel/); assert.match(ide('I-geo-2').warum, /zwei Winkelhalbierende/);
  assert.match(I.GESETZ.G8.satz, /zwei Winkelhalbierende/);
  assert.match(ide('I-daten-2').genau, /keine Auswahlverzerrung/); assert.match(ide('I-daten-3').satz, /^Bei gleich wahrscheinlichen Ergebnissen: günstige durch mögliche\.$/);
  assert.match(ide('I-fur-3').satz, /Pyramide und Kegel/); assert.match(ide('I-fur-4').genau, /Kugel nicht/);
  assert.equal(I.GESETZ.A4.satz.split('<br>').length, 3); assert.doesNotMatch(I.GESETZ.A4.satz, / · /);
  assert.match(I.GESETZ.E4.satz, /beschränktes Vieleck/); assert.match(I.GESETZ.E5.satz, /höchstens eine halbe Rundungseinheit/);
  assert.match(ide('I-zahlen-5').satz, /√\(x²\) = \|x\|/); assert.match(I.GESETZ.V8.satz, /Grundwert 0/);
  assert.match(I.GESETZ.V1.satz, /1 kg = 1 000 g/); assert.match(I.GESETZ.V1.satz, /1 h = 60 min/); assert.match(I.GESETZ.V1.satz, /1 d = 24 h/);
  assert.match(I.GESETZ.D9.satz, /Nenner n/); assert.match(I.GESETZ.D9.satz, /n > 1/);
  assert.match(I.GESETZ.Z23.satz, /positive ganze Zahl n/); assert.match(I.GESETZ.G6.satz, /einfache[nm] n-Eck/); assert.match(I.GESETZ.G6.voraus, /Beim konvexen n-Eck gelingt das von jeder Ecke aus/); assert.match(I.GESETZ.G6.warum, /durch Diagonalen in n − 2 Dreiecke zerlegen/);
  assert.match(I.GESETZ.E3.satz, /zusammenhängender ungerichteter Graph.*genau dann.*jeder Knotengrad gerade/);
  assert.equal(I.GESETZ.G16.klassen.find((k) => k.klasse === 5).text, 'Ein nichtquadratisches Rechteck hat zwei Symmetrieachsen, ein Quadrat vier.');
  assert.equal(I.GESETZ.F3.klassen.find((k) => k.klasse === 9).text, 'Unter allen Rechtecken mit Umfang 20 cm hat das Quadrat die größte Fläche (25 cm²).');
  const bg = (r, k) => D.lehrer[r].aufgaben.find((a) => a.kopf.startsWith(k));
  assert.match(bg('R13', 'BG-01').text, /^Es gilt x ≠ 3 und x ≠ −3\. /); assert.match(bg('R13', 'BG-02').text, /^Es gilt x ≠ −4 und x ≠ 2\. /);
  assert.match(D.arbeitsweisen.find((a) => a.name === 'Begründen').satz, /allgemeinen Behauptung/); assert.match(D.arbeitsweisen.find((a) => a.name === 'Einheiten').satz, /unpassende Dimension.*zeigt einen Fehler an/);
  assert.match(text('I-geo-4', 10), /Schnitt parallel zur Grundfläche auf halber Höhe.*⅛ des ursprünglichen Volumens, der Stumpf ⅞/);
  assert.match(text('I-geo-3', 7), /^Spiegeln: \|AB\| = 3, danach \|A′B′\| = 3$/);
  // in den Texten der App steht kein Verweis auf interne Prüfnummern
  assert.doesNotMatch(JSON.stringify(D.lehrer), /Gegenprüfung|umhaengen|1078|1090/);
});

// ---------- Dritte Gegenprüfung (Werkstatt 1112): derselbe Inhalt in allen angezeigten Feldern ----------
test('1112: Merksatz, Kurzbeschreibung und Langtexte widersprechen sich nicht (R6, R7, Wachstum, G6, D9, Z19, Aufgaben, Einheiten)', () => {
  for (const r of ['R6', 'R7']) assert.equal(D.kurz[r], I.REGEL[r].satz, r + ': Kurzbeschreibung und Merksatz');
  assert.match(I.REGEL.R7.genau, /Alle Plus und Minus der Summanden in der gerade aufgelösten Klammer tauschen/);
  assert.match(I.REGEL.R7.warum, /jeder Summand sein Vorzeichen/); assert.doesNotMatch(JSON.stringify(D.regeln.filter((r) => ['R6', 'R7'].includes(r.id))), /nimmt jeden in der Klammer mal|dreht alle Zeichen um/);
  const w = D.planeten.flatMap((p) => p.ideen).find((i) => i.id === 'I-funktionen-2');
  assert.equal(w.satz, 'Bei y = A · qˣ mit A > 0 steigt der Graph für q > 1, fällt für 0 < q < 1 und bleibt für q = 1 konstant.');
  assert.match(w.warum, /Schrittweite h ist der Faktor qʰ/);
  assert.match(I.GESETZ.D9.satz, /unabhängigen Zufallsstichprobe \(n > 1\).*vom Stichprobenmittel durch n − 1.*korrigierte Stichprobenvarianz.*Stichprobenstandardabweichung/);
  assert.match(I.GESETZ.Z19.voraus, /erst nach einer passenden Umformung anwendbar: 2³ · 4² = 2³ · \(2²\)² = 2⁷/); assert.match(I.GESETZ.Z19.voraus, /Mit positiver Basis gelten die Potenzgesetze für alle rationalen Exponenten/); assert.match(I.GESETZ.Z19.voraus, /ungeraden Nenner/);
  // 1121/1122: stehen gebliebene pauschale Altsätze dürfen nicht wieder auftauchen
  assert.doesNotMatch(I.GESETZ.Z19.voraus, /Verschiedene Basis und verschiedene Hochzahl lassen sich nicht zusammenfassen|Für rationale Exponenten muss die Basis positiv sein/);
  assert.doesNotMatch(w.warum, /Wird in jedem gleich großen x-Schritt mit derselben Zahl q malgenommen/); assert.match(w.warum, /^.*Multipliziert sich der Funktionswert bei jedem x-Schritt der Länge 1 mit demselben positiven Faktor q, beschreibt y = A · qˣ das exponentielle Modell mit Anfangswert A > 0\./);
  assert.doesNotMatch(I.REGEL.R6.voraus, /malt man nur einen Faktor/); assert.match(I.REGEL.R6.voraus, /kann man zuerst die Faktoren in der Klammer multiplizieren: 3 · \(2 · 5\) = 3 · 10 = 30/);
  assert.equal(D.kurz['I-geo-2'], 'Kreis um einen Punkt, Mittelsenkrechte zweier Punkte, Winkelhalbierende zweier sich schneidender Geraden.');
  const bg = (k) => Object.values(D.lehrer).flatMap((l) => l.aufgaben).find((a) => a.kopf.startsWith(k));
  for (const [k, t] of [['BG-01', 'x ≠ 3 und x ≠ −3'], ['BG-02', 'x ≠ −4 und x ≠ 2'], ['BG-03', 'x ≠ 0'], ['BG-13', 'x ≠ 0 und x ≠ −9'], ['PG-01', 'a ≠ 0'], ['PG-02', 'x ≠ 0'], ['PG-03', 'a ≠ 0']]) assert.ok(bg(k).text.startsWith('Es gilt ' + t + '. '), k);
  assert.doesNotMatch(JSON.stringify(D.lehrer), /Ausgeschlossen: x|Alle Basen sind/);
  const e = D.arbeitsweisen.find((a) => a.name === 'Einheiten');
  assert.match(e.erklaerung, /umrechenbare Einheit wie cm statt m beweist keinen falschen Ansatz/); assert.doesNotMatch(JSON.stringify(e), /falsche Einheit/);
});
