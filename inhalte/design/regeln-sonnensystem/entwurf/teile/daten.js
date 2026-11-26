// Inhalte der Entwürfe. Regeln, Sätze, Grenzen und Beispiele: denkpapier-grundregeln.md (Mathe-Profi), Abschnitt 1.
// Gruppen: Vorschlag des Projektleiters. Zustände: ERFUNDEN, keine Lerndaten.
const PLANETEN = [
  { id: 'vorzeichen', name: 'Vorzeichen', zeichen: '±', hell: '#FF8A66', dunkel: '#B4472B', kurz: 'Plus und Minus: wohin es geht und was beim Malnehmen passiert.', regeln: [1, 2] },
  { id: 'klammer', name: 'Klammer', zeichen: '( )', hell: '#A99BFF', dunkel: '#5B4CC4', kurz: 'Was zuerst gerechnet wird und was mit Klammern passiert.', regeln: [3, 4, 5, 6] },
  { id: 'erde', name: 'Erde', zeichen: '', hell: '#5AAEFF', dunkel: '#1F5FA8', kurz: 'Deine Reise.', regeln: [], erde: true },
  { id: 'waage', name: 'Waage', zeichen: '=', hell: '#3AD6C5', dunkel: '#14877C', kurz: 'Gleichungen: Auf beiden Seiten steht gleich viel.', regeln: [7, 8, 9, 15] },
  { id: 'bruch', name: 'Bruch', zeichen: '÷', hell: '#FF9BD0', dunkel: '#B8487F', kurz: 'Brüche und Hochzahlen.', regeln: [10, 11, 12] },
  { id: 'verhaeltnis', name: 'Verhältnis', zeichen: ':', hell: '#B4E86A', dunkel: '#5F9A22', kurz: 'Stellen, Prozent und der Wert je Einheit.', regeln: [13, 14] },
];
const REGELN = {
  1: { name: 'Richtung', satz: 'Plus geht nach rechts, Minus nach links; eine negative Zahl dreht die Richtung um.' },
  2: { name: 'Zeichen-Paar', satz: 'Mal und geteilt: gleiche Zeichen plus, verschiedene minus.', grenze: 'Nicht beim Addieren.' },
  3: { name: 'Rangfolge', satz: 'Klammer, Potenz, Punkt, Strich. Die letzte Rechnung gibt dem Term den Namen.' },
  4: { name: 'Verteilen', satz: 'Der Faktor trifft jeden in der Klammer.', satz2: 'Rückwärts: Gemeinsames herausziehen.', grenze: 'Nicht beim Quadrat.' },
  5: { name: 'Minusklammer', satz: 'Minus vor der Klammer dreht jedes Zeichen darin.', satz2: 'Plus davor dreht nichts.' },
  6: { name: 'Tauschen und Bündeln', satz: 'Bei plus und mal darf man tauschen und zusammenfassen – nur Gleiches mit Gleichem.', grenze: 'Nicht bei minus und geteilt.' },
  7: { name: 'Waage', satz: 'Gleich heißt gleich viel. Auf beiden Seiten dasselbe tun.' },
  8: { name: 'Umkehren', satz: 'Jede Rechnung hat eine Gegenrechnung: plus/minus, mal/geteilt, Quadrat/Wurzel.' },
  9: { name: 'Einsetzen und Probe', satz: 'Zahl für den Buchstaben einsetzen prüft jede Umformung und jede Lösung.', grenze: 'Widerlegt, beweist nicht.' },
  10: { name: 'Wert bleibt', satz: 'Oben und unten mit demselben malnehmen oder teilen ändert nichts.', grenze: 'Kürzen nur Faktoren, nie aus Summen.' },
  11: { name: 'Bruchrechnen', satz: 'Plus/minus: erst gleicher Nenner. Mal: oben mal oben, unten mal unten. Geteilt: mal Kehrwert.' },
  12: { name: 'Potenz', satz: 'Wiederholtes Malnehmen; gleiche Basis: Hochzahlen addieren.', grenze: 'a · a ist a², nicht 2a.' },
  13: { name: 'Stellenwert', satz: 'Mal 10 schiebt jede Ziffer eine Stelle. Prozent heißt Hundertstel.' },
  14: { name: 'Verhältnis', satz: 'Wert je Einheit: Wächst das eine, wächst das andere mit.', grenze: 'Nicht mit Grundgebühr.' },
  15: { name: 'Nullprodukt', satz: 'Ist ein Produkt null, ist ein Faktor null.', grenze: 'Nur bei null.' },
};
// Arbeitsweisen: Namen vom Projektleiter, Sätze vom Designer (Mathe-Profi prüft).
const WERKZEUGE = [
  { name: 'Skizze', satz: 'Erst zeichnen, dann rechnen.' },
  { name: 'Überschlag', satz: 'Vorher grob schätzen, was herauskommen muss.' },
  { name: 'Einheiten prüfen', satz: 'Passt die Einheit zum Ergebnis?' },
  { name: 'Zerlegen und Ergänzen', satz: 'Schwieriges in einfache Teile schneiden oder zu etwas Einfachem auffüllen.' },
  { name: 'Darstellung wechseln', satz: 'Tabelle, Bild, Term: dieselbe Sache anders zeigen.' },
];
// ERFUNDENE Beispiel-Zustände. s = sitzt, a = in Arbeit, k = kommt später.
const STAENDE = {
  bsp5: { name: 'Beispiel A (erfunden, etwa Klasse 5)', z: { 1: 's', 2: 's', 3: 's', 4: 'a', 5: 'a', 6: 's', 7: 'a', 8: 'a', 9: 'k', 10: 'k', 11: 'k', 12: 'k', 13: 'k', 14: 'k', 15: 'k' } },
  bsp8: { name: 'Beispiel B (erfunden, etwa Klasse 8)', z: { 1: 's', 2: 's', 3: 's', 4: 's', 5: 'a', 6: 's', 7: 's', 8: 's', 9: 'a', 10: 'a', 11: 's', 12: 'a', 13: 's', 14: 's', 15: 'k' } },
  aus: { name: 'ohne Stand', z: {} },
};
// Satz für Weg b („nach einem Fehler“), je Regel fertig formuliert.
const GEKLEMMT = { 1: 'Hier hat die Richtung geklemmt.', 2: 'Hier hat das Zeichen-Paar geklemmt.', 3: 'Hier hat die Rangfolge geklemmt.', 4: 'Hier hat das Verteilen geklemmt.', 5: 'Hier hat die Minusklammer geklemmt.', 6: 'Hier hat das Bündeln geklemmt.', 7: 'Hier hat die Waage geklemmt.', 8: 'Hier hat das Umkehren geklemmt.', 9: 'Hier hat die Probe gefehlt.', 10: 'Hier hat „Wert bleibt“ geklemmt.', 11: 'Hier hat das Bruchrechnen geklemmt.', 12: 'Hier hat die Potenz geklemmt.', 13: 'Hier hat der Stellenwert geklemmt.', 14: 'Hier hat das Verhältnis geklemmt.', 15: 'Hier hat das Nullprodukt geklemmt.' };
const ZUSTAND_TEXT = { s: 'sitzt', a: 'in Arbeit', k: 'kommt später' };
const ZUSTAND_KLASSE = { s: 'sitzt', a: 'arbeit', k: 'spaeter' };

// Ausführliche Karten (nur Regel 4 und 5). „orte“ sind ERFUNDENE Beispiele; die echte Liste liefert der Mathe-Profi (Regel-Etiketten).
const B = (o, u) => `<span class="br"><i>${o}</i><i>${u}</i></span>`;
const KARTEN = {
  4: {
    bild: 'rechteck', bildtext: 'Eine Höhe, zwei Breiten: Die Höhe trifft beide Teile.',
    gewand: [
      { art: 'Zahlen', html: '<span class="f">6</span> · (20 − 2) = <span class="f">6</span> · 20 − <span class="f">6</span> · 2', bild: { f: '6', a: '20', b: '2', minus: true, fa: '6 · 20', fb: '6 · 2', rest: '18' } },
      { art: 'mit x', html: '<span class="f">3</span> · (x + 2) = <span class="f">3</span> · x + <span class="f">3</span> · 2', bild: { f: '3', a: 'x', b: '2', fa: '3 · x', fb: '3 · 2' } },
      { art: 'mit Brüchen', html: `<span class="f">${B(1, 2)}</span> · (4 + ${B(2, 3)}) = <span class="f">${B(1, 2)}</span> · 4 + <span class="f">${B(1, 2)}</span> · ${B(2, 3)}`, bild: { f: '½', a: '4', b: '⅔', fa: '½ · 4', fb: '½ · ⅔' } },
    ],
    grenze: { satz: 'Nicht beim Quadrat.', text: 'Das Quadrat trifft nicht jeden einzeln. Mit Zahlen siehst du es sofort:', rechnung: '(3 + 4)² <b class="ungleich">≠</b> 3² + 4²<br>49 <b class="ungleich">≠</b> 25' },
    probe: { text: 'Stimmt die Umformung? Setz für x eine Zahl ein – 2 oder 3, nie 0 oder 1.', links: (x) => [`3 · (${x} + 2)`, 3 * (x + 2)], rechts: (x) => [`3 · ${x} + 6`, 3 * x + 6], name: ['3 · (x + 2)', '3x + 6'] },
    orte: [['ROM', 'Geschickt rechnen', 'Kl. 5'], ['LIMA', 'Terme mit Klammern', 'Kl. 7'], ['KYOTO', 'Binomische Formeln', 'Kl. 8'], ['OSLO', 'Flächen zerlegen', 'Kl. 6']],
  },
  5: {
    bild: 'strahl', bildtext: 'Erst 8 zurück – das war zu viel. Also 3 wieder vor.',
    gewand: [
      { art: 'Zahlen', html: '20 <span class="f">−</span> (8 − 3) = 20 <span class="d">− 8 + 3</span>' },
      { art: 'mit x', html: '5x <span class="f">−</span> (3x − 2) = 5x <span class="d">− 3x + 2</span>' },
      { art: 'mit Brüchen', html: `1 <span class="f">−</span> (${B(1, 2)} − ${B(1, 4)}) = 1 <span class="d">− ${B(1, 2)} + ${B(1, 4)}</span>` },
    ],
    grenze: { satz: 'Plus davor dreht nichts.', text: 'Nur das Minus dreht. Und es dreht jedes Zeichen, nicht nur das erste:', rechnung: '20 − (8 − 3) <b class="ungleich">≠</b> 20 − 8 − 3<br>15 <b class="ungleich">≠</b> 9' },
    probe: { text: 'Stimmt die Umformung? Setz für x eine Zahl ein – 2 oder 3, nie 0 oder 1.', links: (x) => [`5 · ${x} − (3 · ${x} − 2)`, 5 * x - (3 * x - 2)], rechts: (x) => [`2 · ${x} + 2`, 2 * x + 2], name: ['5x − (3x − 2)', '2x + 2'] },
    orte: [['ROM', 'Rechnen mit Klammern', 'Kl. 5'], ['LIMA', 'Terme vereinfachen', 'Kl. 7'], ['KAIRO', 'Gleichungen lösen', 'Kl. 7'], ['KYOTO', 'Binomische Formeln', 'Kl. 8']],
  },
};
