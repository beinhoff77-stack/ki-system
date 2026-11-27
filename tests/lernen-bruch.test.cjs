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
