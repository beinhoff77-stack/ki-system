// Was der Designer zum Inhalt des Mathe-Profis (inhalt.json) ergänzt hat. Alles hier ist Darstellung oder als Annahme gekennzeichnet.

// Tragende Ideen je Planet. „Fläche und Raum“: drei Ideen laut Auftrag; der Satz darunter stammt aus „Der Planet in einer Minute“ (Mathe-Profi).
// „Geometrie“: Vorschlag des Projektleiters, noch zu prüfen; die Sätze sind die Sätze der Gesetze G6, G10, G15, G20, G24 (Mathe-Profi).
// Welche Gesetze hinter welcher Idee stehen, hat der Designer zugeordnet (ANNAHME, der Mathe-Profi prüft).
const IDEEN = {
  'Fläche und Raum': [
    { id: 'I-fur-1', satz: 'Messen heißt auslegen und zählen.', dazu: 'Flächen mit Einheitsquadraten, Körper mit Einheitswürfeln. Jede Formel ist eine Abkürzung für dieses Zählen.', gesetze: ['F1', 'F3', 'F11'] },
    { id: 'I-fur-2', satz: 'Aus dem Rechteck entsteht jede Fläche.', dazu: 'Durch Zerlegen entstehen Parallelogramm, Dreieck, Trapez, Drachen und Kreis.', gesetze: ['F2', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10'] },
    { id: 'I-fur-3', satz: 'Aus dem Quader entsteht jeder Körper.', dazu: 'Durch Stapeln entstehen Prisma und Zylinder, daraus durch „ein Drittel“ Pyramide und Kegel.', gesetze: ['F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19'] },
  ],
  Geometrie: [
    { id: 'I-geo-1', satz: 'Die Winkel im Dreieck ergeben zusammen 180°.', gesetze: ['G1', 'G2', 'G3', 'G4', 'G5', 'G6'], bild: 'Ein Dreieck aus Papier: die drei Ecken abgerissen und nebeneinandergelegt ergeben eine gerade Linie.' },
    { id: 'I-geo-2', satz: 'Drei passende Angaben legen ein Dreieck fest.', gesetze: ['G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14'], bild: 'Drei Stäbe lassen sich nur zu einem einzigen Dreieck zusammenstecken.' },
    { id: 'I-geo-3', satz: 'Spiegeln, Verschieben, Drehen ändert weder Längen noch Winkel.', gesetze: ['G15', 'G16', 'G17', 'G18', 'G19'], bild: 'Dieselbe Figur dreimal: gespiegelt, verschoben, gedreht – deckungsgleich.' },
    { id: 'I-geo-4', satz: 'Ähnliche Figuren haben gleiche Winkel und alle Seiten im selben Verhältnis.', gesetze: ['G20', 'G21', 'G22', 'G23'], bild: 'Ein Dreieck und seine Vergrößerung: gleiche Winkel, jede Seite doppelt so lang.' },
    { id: 'I-geo-5', satz: 'Im rechtwinkligen Dreieck gilt a² + b² = c².', gesetze: ['G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30'], bild: 'Rechtwinkliges Dreieck mit einem Quadrat über jeder Seite: Die zwei kleinen sind zusammen so groß wie das große.' },
  ],
};
// Reihenfolge und Zeichen der Planeten (von innen nach außen, wie in inhalt.md).
const PLANET_BILD = {
  Zahlen: { farbe: '#FF8A66', zeichen: '<text y="6" text-anchor="middle" font-family="var(--mono)" font-weight="800" font-size="15" fill="#11161D">123</text>' },
  Algebra: { farbe: '#A99BFF', zeichen: '<text y="7" text-anchor="middle" font-family="var(--mono)" font-weight="800" font-size="22" fill="#11161D">x</text>' },
  'Geld und Verhältnisse': { farbe: '#B4E86A', zeichen: '<text y="7" text-anchor="middle" font-family="var(--mono)" font-weight="800" font-size="20" fill="#11161D">%</text>' },
  Geometrie: { farbe: '#3AD6C5', zeichen: '<path d="M-11 9L11 9L-3 -11Z" fill="none" stroke="#11161D" stroke-width="2.6" stroke-linejoin="round"/>' },
  'Fläche und Raum': { farbe: '#5AAEFF', zeichen: '<path d="M-10 -8H10V8H-10ZM-10 0H10M-3.300 -8V8M3.300 -8V8" fill="none" stroke="#11161D" stroke-width="2.2" stroke-linejoin="round"/>' },
  Funktionen: { farbe: '#FF9BD0', zeichen: '<path d="M-11 10V-11M-11 10H11" fill="none" stroke="#11161D" stroke-width="2.2" stroke-linecap="round"/><path d="M-9 7Q0 6 9 -9" fill="none" stroke="#11161D" stroke-width="2.6" stroke-linecap="round"/>' },
  'Daten und Zufall': { farbe: '#FFC46B', zeichen: '<path d="M-9 10V1M-3 10V-9M3 10V-3M9 10V4" fill="none" stroke="#11161D" stroke-width="4" stroke-linecap="butt"/>' },
};
// Wirkstelle in den Klassen-Beispielen: derselbe Text wie beim Mathe-Profi, nur die wirkende Stelle ist markiert.
// bauen.py prüft, dass der Text ohne Markierung wörtlich dem Beispiel in inhalt.json entspricht.
const WIRKSTELLE = {
  R6: { was: 'Gelb: der Faktor vor der Klammer.',
    5: '<b class="w">6</b> · 98 = <b class="w">6</b> · 100 − <b class="w">6</b> · 2 = 588',
    6: '<b class="w">4</b> · 2,5 = <b class="w">4</b> · 2 + <b class="w">4</b> · 0,5 = 10',
    7: '<b class="w">3</b> · (x + 2) = <b class="w">3</b>x + 6<br>(a + b)² = a² + 2ab + b²',
    8: '(3x + 6) : (x + 2) = <b class="w">3</b> · (x + 2) : (x + 2) = 3',
    9: 'x² + 5x = <b class="w">x</b> · (x + 5)',
    10: 'x³ − 4x = <b class="w">x</b> · (x² − 4)' },
  R13: { was: 'Gelb: was auf beiden Seiten getan wird.',
    5: '□ + 7 = 3: <b class="w">auf beiden Seiten 7 abziehen</b>, □ = −4',
    8: '3/x + ½ = 5/x: <b class="w">beide Seiten mal 2x</b>, dann 6 + x = 10, x = 4' },
  R2: { was: 'Gelb: das Minus, das die Richtung umdreht.',
    5: '(<b class="w">−</b>7) + 4 = −3<br>9 − (<b class="w">−</b>5) = 14' },
};
