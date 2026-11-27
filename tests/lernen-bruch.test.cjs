// Bruch-Erkennung im Aufgabentext (lernBruchTeile in lernen.js) – reine Textfunktion, läuft ohne Browser.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const quelle = fs.readFileSync(path.resolve(__dirname, '..', 'lernen.js'), 'utf8');
const a = quelle.indexOf("const LERN_BUCHST = "); const b = quelle.indexOf('function lernBruchKnoten(s) {');
const lernBruchTeile = new Function(quelle.slice(a, b) + '\nreturn lernBruchTeile;')();
const kurz = (s) => lernBruchTeile(s).map((t) => (typeof t === 'string' ? t : `${t.vz || ''}[${t.z}|${t.n}]`)).join('');

test('Zahlenbrüche werden erkannt, auch mit Satzzeichen danach', () => {
  assert.equal(kurz('Kürze 6/8 vollständig.'), 'Kürze [6|8] vollständig.');
  assert.equal(kurz('Was ist mehr: 1/2 oder 3/4?'), 'Was ist mehr: [1|2] oder [3|4]?');
  assert.equal(kurz('Rechne 1/2, 1/3; 1/4: fertig (1/5).'), 'Rechne [1|2], [1|3]; [1|4]: fertig ([1|5]).');
  assert.equal(kurz('„1/2“ und −3/4'), '„[1|2]“ und −[3|4]');
  assert.equal(kurz('2,5/3'), '[2,5|3]');
});
test('Brüche mit Buchstaben, π, Wurzel und Hochzahl', () => {
  assert.equal(kurz('x/2 + a/b = 2x/27'), '[x|2] + [a|b] = [2x|27]');
  assert.equal(kurz('11π/6 und π/180 und 180°/π'), '[11π|6] und [π|180] und [180°|π]');
  assert.equal(kurz('1/b² und 1/√2 und p/100.'), '[1|b²] und [1|√2] und [p|100].');
  assert.equal(kurz('α/2 und 20x⁴/35'), '[α|2] und [20x⁴|35]');
  assert.equal(kurz('(1/2)² und f(1/3) und √(1/4) und cos(π/3)'), '([1|2])² und f([1|3]) und √([1|4]) und cos([π|3])');
});
test('Klammern um Zähler und Nenner fallen weg', () => {
  assert.equal(kurz('(x + 1)/(x − 2)'), '[x + 1|x − 2]');
  assert.equal(kurz('1/(2x) und −12/(x + 3) und (a + b)/2'), '[1|2x] und −[12|x + 3] und [a + b|2]');
  assert.equal(kurz('12/(−3)'), '[12|−3]');
});
test('Kein Bruch: Einheiten, Wörter, Daten, Ketten, Hochzahlen, unklare Zähler', () => {
  for (const s of ['60 km/h', '5 m/s', 'cm/h', 'ja/nein', 'und/oder', 'Mädchen/Jungen', 'Plus/Minus', 'am 3/4/2026', '68/95/99,7', 'x^(1/2)', '16^(−1/4)',
    'f(x)/2', '√(8)/2', '2(x + 1)/3', 'x/y-Ebene', '1.5/2', '/', 'a / b', '1/2x', 'Seite a/Seite b', '3/', '/4', 'g/l', '(siehe Bild)/2']) {
    assert.equal(kurz(s), s, s);
  }
});
test('Minus direkt vor dem Bruch bleibt am Bruch', () => {
  assert.deepEqual(lernBruchTeile('= −1/2 und 3 − 1/2'), ['= ', { z: '1', n: '2', vz: '−' }, ' und 3 − ', { z: '1', n: '2' }]);
});
test('Gemischte Zahl bleibt zusammen', () => {
  assert.equal(kurz('Addiere 2 1/2 und 1 3/4.'), 'Addiere 2 [1|2] und 1 [3|4].');
  assert.equal(kurz('Teile 12 durch 3/4'), 'Teile 12 durch [3|4]');
  assert.equal(kurz('von 5 6/3'), 'von 5 [6|3]');
});
test('Mehrere Brüche hintereinander und Text bleibt vollständig', () => {
  const s = 'Vergleiche 2/3 mit 4/6 und (x − 1)/4 mit 0,5.';
  assert.equal(lernBruchTeile(s).map((t) => (typeof t === 'string' ? t : (t.vz || '') + (/[ +−]/.test(t.z) ? `(${t.z})` : t.z) + '/' + t.n)).join(''), s);
});

// Regressionstests 0.93.7 (Gegenprüfung): Die Erkennung darf keine Zahl und keine Formel verändern.
// Echte Trenner in inhalte/themen bei „/“: normales Leerzeichen; geschütztes (U+00A0) und schmales geschütztes (U+202F) zur Sicherheit mitgeprüft.
test('Tausendergruppen bleiben ganz – im Nenner', () => {
  assert.equal(kurz('Schreibe als Dezimalzahl: 5 + 9/100 + 7/1 000'), 'Schreibe als Dezimalzahl: 5 + [9|100] + [7|1 000]');
  assert.equal(kurz('0,875 = 875/1 000. Gekürzt mit 125: 7/8.'), '0,875 = [875|1 000]. Gekürzt mit 125: [7|8].');
  assert.equal(kurz('10⁻⁶ = 1/1 000 000.'), '10⁻⁶ = [1|1 000 000].');
  assert.equal(kurz('(1/4)⁶ = 1/4 096.'), '([1|4])⁶ = [1|4 096].');
  assert.equal(kurz('25/10 000'), '[25|10 000]');
  assert.equal(kurz('12 · m/1 000 + …'), '12 · [m|1 000] + …');
  assert.deepEqual(lernBruchTeile('7/1 000'), [{ z: '7', n: '1 000' }]);
  assert.deepEqual(lernBruchTeile('7/1 000'), [{ z: '7', n: '1 000' }]);
});
test('Tausendergruppen bleiben ganz – im Zähler und in beiden', () => {
  assert.equal(kurz('s(x) = 1 200/x + 15 Euro'), 's(x) = [1 200|x] + 15 Euro');
  assert.equal(kurz('9/12 = 11 880/20 736 = 55/96.'), '[9|12] = [11 880|20 736] = [55|96].');
  assert.equal(kurz('V = 2 299π/3 ≈ 2 407,5 cm³.'), 'V = [2 299π|3] ≈ 2 407,5 cm³.');
  assert.deepEqual(lernBruchTeile('1 200/x'), [{ z: '1 200', n: 'x' }]);
  assert.deepEqual(lernBruchTeile('1 200/x'), [{ z: '1 200', n: 'x' }]);
  assert.equal(kurz('−1 500/x'), '−[1 500|x]');
  // nicht eindeutig begrenzt: lieber Text als zerrissen
  for (const s of ['12,5 200/x', '1/2,5 000', '7/1 000,5', 'x/1 000x']) assert.equal(kurz(s), s, s);
});
test('Gemischte Zahl wird nicht mit Tausendergruppe verwechselt', () => {
  // (vor dem Bruch steht dann ein schmales geschütztes Leerzeichen: kein Umbruch zwischen Ganzen und Bruch)
  assert.equal(kurz('Addiere 2 1/2 und 3 12/25.'), 'Addiere 2\u202f[1|2] und 3\u202f[12|25].');
  assert.equal(kurz('2 7/1 000'), '2\u202f[7|1 000]');
});
test('Hochzahlen gehören ganz zum Nenner oder der Ausdruck bleibt Text', () => {
  assert.equal(kurz('4/x⁻²'), '[4|x⁻²]');
  assert.equal(kurz('Sₙ = 2 − 1/2ⁿ⁻¹.'), 'Sₙ = 2 − [1|2ⁿ⁻¹].');
  assert.equal(kurz('(1/2)¹⁰ = 1/2¹⁰ = 1/1 024'), '([1|2])¹⁰ = [1|2¹⁰] = [1|1 024]');
  assert.equal(kurz('8⁻¹ = 1/8¹ = 1/8.'), '8⁻¹ = [1|8¹] = [1|8].');
  assert.equal(kurz('x⁻²/4 und 1/b²'), '[x⁻²|4] und [1|b²]');
  for (const s of ['2/3^2', '3^2/4', '1/x^(1/2)', '2^(−1/2) = 1/2^(1/2)', 'x^-1/2', '1/(x + 1)^2', '1/(x + 1)⁻¹']) assert.equal(kurz(s), s, s);
});
test('Paare einzelner Großbuchstaben (römische Zahlzeichen) bleiben Text', () => {
  const s = 'Teile in Gruppen: M…, dann C/D, dann X/L, dann I/V.';
  assert.equal(kurz(s), s);
  for (const t of ['2021 A/B (Teil)', 'M/D']) assert.equal(kurz(t), t, t);
  assert.equal(kurz('x/y + a/b'), '[x|y] + [a|b]');
});
test('Kurzdaten und Jahre bleiben Text', () => {
  for (const s of ['am 03/04', 'am 3/04', 'Schuljahr 2026/27', 'Saison 2019/2020', '27/11/2026', '68/95/99,7 %', 'km/h', 'm/s', 'oben/unten', 'x^(1/2)']) {
    assert.equal(kurz(s), s, s);
  }
  assert.equal(kurz('1800/60 = 30'), '[1800|60] = 30');
  assert.equal(kurz('0,5/2'), '[0,5|2]');
});
