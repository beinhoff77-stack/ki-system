// Was der Designer zum Inhalt des Mathe-Profis (inhalt.json) ergänzt hat. Alles hier ist Darstellung oder als Annahme gekennzeichnet.

// Tragende Ideen, ihre Sätze und die Zuordnung der Gesetze kommen seit Auftrag 11 vom Mathe-Profi (ebene1.md, in inhalt.json).
// Hier steht nur noch das Kürzel je Planet für die Adresse einer Idee (#/idee/I-fur-2).
const KUERZEL = { Zahlen: 'zahlen', Algebra: 'algebra', 'Geld und Verhältnisse': 'geld', Geometrie: 'geo', 'Fläche und Raum': 'fur', Funktionen: 'funktionen', 'Daten und Zufall': 'daten' };
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
// Wirkstelle in den Klassen-Beispielen: teile/wirkstelle.json (bauen.py prüft, dass der Text wörtlich dem Beispiel des Mathe-Profis entspricht).
