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
  assert.equal(kurz('9/12 = 11 880/20 736 = 55/96.'), '[9|12] = 11 880/20 736 = [55|96].'); // 0.93.8 (dritte Runde): zweideutige Gruppe im Zähler bleibt Text
  assert.equal(kurz('V = 2 299π/3 ≈ 2 407,5 cm³.'), 'V = [2 299π|3] ≈ 2 407,5 cm³.');
  // 0.93.8: Gruppe nur im Zähler ist zweideutig (Tausendergruppe oder gemischte Zahl) → ganzer Ausdruck bleibt Text
  for (const s of ['s(x) = 1 200/x + 15 Euro', '1 200/x', '1\u00a0200/x', '1\u202f200/x', '−1 500/x', '1 234 567/x']) assert.equal(kurz(s), s, s);
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

// Regressionstests 0.93.8 (Gegenprüfung der 0.93.7)
test('Zweideutige Gruppe im Zähler bleibt ganz Text, nie zerrissen', () => {
  for (const s of ['Als gemischte Zahl: 2 125/128', '2 125/128', '2\u00a0125/128', '1 200/x', '3 125/(x + 1)']) {
    assert.equal(kurz(s), s, s);
    assert.deepEqual(lernBruchTeile(s), [s], s);
  }
  for (const s of ['Als gemischte Zahl: 2 125/2 048', '11 880/20 736']) assert.deepEqual(lernBruchTeile(s), [s], s); // Gruppe auch im Nenner hebt die Zweideutigkeit nicht auf
  assert.deepEqual(lernBruchTeile('7/1 000'), [{ z: '7', n: '1 000' }]); // Gruppe nur im Nenner: eindeutig
});
test('Gemischte Zahlen mit ein- oder zweistelligem Zähler wie in 0.93.6', () => {
  assert.deepEqual(lernBruchTeile('2 1/2'), ['2\u202f', { z: '1', n: '2' }]);
  assert.deepEqual(lernBruchTeile('1 1/4'), ['1\u202f', { z: '1', n: '4' }]);
  assert.deepEqual(lernBruchTeile('3 25/48'), ['3\u202f', { z: '25', n: '48' }]);
});
test('Alle hochgestellten Zeichen gehören zur Basis', () => {
  assert.deepEqual(lernBruchTeile('4/xᵏ'), [{ z: '4', n: 'xᵏ' }]);
  assert.equal(kurz('xᵃ/yᵇ und 1/2ᵐ⁺¹ und 3/x⁽ⁿ⁾'), '[xᵃ|yᵇ] und [1|2ᵐ⁺¹] und [3|x⁽ⁿ⁾]');
  assert.equal(kurz('aᵗ/4 = 1/eˣ'), '[aᵗ|4] = [1|eˣ]');
});
test('Datum nach Datumswort bleibt Text, echte Brüche nicht', () => {
  for (const s of ['Termin am 27/11', 'Am 1/12 geht es los', 'vom 3/4 bis zum 5/6', 'seit 12/9']) assert.equal(kurz(s), s, s);
  assert.equal(kurz('Rechne 3/4 + 1/2'), 'Rechne [3|4] + [1|2]');
  assert.equal(kurz('den Bruch 3/4'), 'den Bruch [3|4]');
  assert.equal(kurz('von 1/3 bis 1/2'), 'von [1|3] bis [1|2]'); // „bis“ allein ist kein Datumswort (Bestand)
  assert.equal(kurz('AB 2/4 = 0,5'), 'AB [2|4] = 0,5'); // „ab“ ebenso nicht (Bestand)
  assert.equal(kurz('am 27/13'), 'am [27|13]'); // kein Monat
});
test('Auswahl-Kürzel bleiben Text, Buchstabenbrüche nicht', () => {
  for (const s of ['Auswahl: w/m', 'm/w', 'm/w/d', 'j/n', 'ja/nein', 'u/o']) assert.equal(kurz(s), s, s);
  assert.equal(kurz('x/y + a/b und p/q'), '[x|y] + [a|b] und [p|q]');
});
test('Positivkontrollen 0.93.8', () => {
  const soll = { 'x/y + a/b': '[x|y] + [a|b]', '7/1 000': '[7|1 000]', '4/x⁻²': '[4|x⁻²]',
    '1/2ⁿ⁻¹': '[1|2ⁿ⁻¹]', '(x + 1)/(x − 2)': '[x + 1|x − 2]', '2 1/2': '2\u202f[1|2]', '3/4': '[3|4]' };
  for (const [s, k] of Object.entries(soll)) assert.equal(kurz(s), k, s);
});

// Regressionstests 0.93.8, dritte Runde (Gegenprüfung): im Zweifel Text, nie raten
test('Unbekannte Hoch-/Tiefzeichen hinter dem Nenner verhindern die Umwandlung', () => {
  for (const s of ['4/xᴺ', '4/xᴬ', '4/xᵅ', '1/2₂', '4/(x)ᴺ']) assert.deepEqual(lernBruchTeile(s), [s], s);
  assert.deepEqual(lernBruchTeile('4/xᵏ'), [{ z: '4', n: 'xᵏ' }]);
  assert.deepEqual(lernBruchTeile('4/x⁻²'), [{ z: '4', n: 'x⁻²' }]);
  assert.deepEqual(lernBruchTeile('1/2ⁿ⁻¹'), [{ z: '1', n: '2ⁿ⁻¹' }]);
});
test('Datumswort mit beliebigem Leerraum, Kürzel ohne Groß-/Kleinschreibung', () => {
  for (const s of ['Termin am 27/11', 'Termin am  27/11', 'Termin am\n27/11', 'Termin am\u00a027/11', 'seit\u202f12/9']) assert.deepEqual(lernBruchTeile(s), [s], s);
  for (const s of ['Auswahl: W/m', 'w/M', 'M/W', 'J/N', 'Ja/Nein']) assert.equal(kurz(s), s, s);
});
test('Positivkontrollen 0.93.8, dritte Runde', () => {
  const soll = { 'x/y + a/b': '[x|y] + [a|b]', '7/1 000': '[7|1 000]', '(x + 1)/(x − 2)': '[x + 1|x − 2]', '2 1/2': '2\u202f[1|2]',
    'von 3/8 bis 1/2': 'von [3|8] bis [1|2]' };
  for (const [s, k] of Object.entries(soll)) assert.equal(kurz(s), k, s);
});
