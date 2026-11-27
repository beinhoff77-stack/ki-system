// Tafeln zum Nachschlagen (Regel-Universum): baut aus den geprüften Vorschlägen des Mathe-Profis den Teil „tafeln“ von daten/regeln-universum.json.
// Aufgerufen von tools/regeln_bauen.cjs (nicht allein). Inhalte werden wörtlich übernommen – nur Felder, die die App nicht zeigt, fallen weg
// (Belege, Prüfgleichungen, Zeichenanweisungen). Darstellung nach inhalte/design/tafeln/entwurf1/ (umsetzung1.md, index.html):
// Zeichnungen der Flächen und Körper dort übernommen (eine Strichstärke 2, Hilfslinien gestrichelt, Beschriftung Festbreite);
// für die übrigen Tafeln im selben Stil ergänzt (Winkel, Dreiecke und Vierecke aus den Beispieldaten der Vorschläge gezeichnet).
// Quellen (nur gelesen):
//   inhalte/mathe-profi/regeln-uebersicht/einheiten/einheiten.json
//   inhalte/mathe-profi/regeln-uebersicht/tafeln/<tafel>/<tafel>.json  (formeln-flaechen, formeln-koerper, zahlen, stellenwert, bruch-dezimal-prozent, figuren, zeichen-woerter)
'use strict';
const assert = require('node:assert/strict');

// ---------- Zeichnungen (SVG-Text; Farben über CSS: currentColor und --ru-tafel-tint) ----------
const T = (x, y, t, a = 'middle') => `<text x="${x}" y="${y}" text-anchor="${a}" font-family="var(--mono)" font-size="13" font-weight="700" fill="currentColor">${t}</text>`;
const RW = (x, y, dx = 1, dy = -1) => `<path d="M${x + 8 * dx} ${y} V${y + 8 * dy} H${x}" fill="none" stroke="currentColor" stroke-width="1.3"/>`;
const F = 'fill="var(--ru-tafel-tint)" stroke="currentColor" stroke-width="2" stroke-linejoin="round"';
const D = 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"';
const L = 'fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"';
const svg = (vb, inhalt, name) => `<svg viewBox="${vb}" role="img" aria-label="${name}">${inhalt}</svg>`;
// Flächen und Körper: aus entwurf1/index.html (SVG), Kreisring neu im selben Stil
const BILD = {
  rechteck: `<rect x="14" y="14" width="88" height="52" ${F}/>${T(58, 82, 'a')}${T(110, 44, 'b', 'start')}`,
  quadrat: `<rect x="30" y="10" width="58" height="58" ${F}/>${T(59, 84, 'a')}${T(96, 43, 'a', 'start')}`,
  parallelogramm: `<path d="M12 66 H86 L108 16 H34 Z" ${F}/><path d="M34 16 V66" ${D}/>${RW(34, 66)}${T(49, 82, 'g')}${T(39, 48, 'h', 'start')}`,
  dreieck: `<path d="M10 66 H108 L72 12 Z" ${F}/><path d="M72 12 V66" ${D}/>${RW(72, 66)}${T(46, 82, 'g')}${T(80, 46, 'h', 'start')}`,
  trapez: `<path d="M10 66 H110 L86 18 H34 Z" ${F}/><path d="M40 18 V66" ${D}/>${RW(40, 66)}${T(60, 82, 'a')}${T(60, 13, 'c')}${T(46, 46, 'h', 'start')}`,
  drachen: `<path d="M60 6 L92 30 L60 80 L28 30 Z" ${F}/><path d="M60 6 V80 M28 30 H92" ${D}/>${T(64, 64, 'e', 'start')}${T(76, 45, 'f')}`,
  kreis: `<circle cx="58" cy="44" r="36" ${F}/><path d="M58 44 H94" ${L}/><circle cx="58" cy="44" r="2.5" fill="currentColor"/>${T(76, 39, 'r')}`,
  ausschnitt: `<path d="M22 72 L104 72 A82 82 0 0 0 74.7 9.2 Z" ${F}/><path d="M38 72 A16 16 0 0 0 32.3 59.7" fill="none" stroke="currentColor" stroke-width="1.3"/>${T(46, 64, 'α', 'start')}${T(64, 86, 'r')}${T(100, 36, 'b', 'start')}`,
  kreisring: `<path d="M22 44 A36 36 0 1 0 94 44 A36 36 0 1 0 22 44 Z M41 44 A17 17 0 1 1 75 44 A17 17 0 1 1 41 44 Z" fill-rule="evenodd" ${F}/><path d="M58 44 L83.5 18.5" ${L}/><path d="M58 44 H75" ${L}/><circle cx="58" cy="44" r="2.5" fill="currentColor"/>${T(78, 28, 'R', 'start')}${T(66, 58, 'r')}`,
  quader: `<path d="M14 40 H84 V90 H14 Z" ${F}/><path d="M14 40 L42 18 H112 L84 40 M112 18 V68 L84 90" ${L}/><path d="M14 90 L42 68 H112 M42 68 V18" ${D}/>${T(49, 104, 'a')}${T(106, 86, 'b', 'start')}${T(6, 69, 'c', 'end')}`,
  wuerfel: `<path d="M22 42 H74 V94 H22 Z" ${F}/><path d="M22 42 L44 24 H96 L74 42 M96 24 V76 L74 94" ${L}/><path d="M22 94 L44 76 H96 M44 76 V24" ${D}/>${T(48, 108, 'a')}`,
  prisma: `<path d="M12 90 H62 L37 48 Z" ${F}/><path d="M62 90 L112 66 L87 24 L37 48 M87 24 H87" ${L}/><path d="M12 90 L62 66 H112 M62 66 L87 24" ${D}/>${T(34, 84, 'G')}${T(92, 88, 'h', 'start')}`,
  zylinder: `<ellipse cx="62" cy="22" rx="38" ry="10" ${F}/><path d="M24 22 V84 M100 22 V84" ${L}/><path d="M24 84 A38 10 0 0 0 100 84" ${L}/><path d="M24 84 A38 10 0 0 1 100 84" ${D}/><path d="M62 22 H100" ${L}/>${T(82, 33, 'r')}${T(106, 56, 'h', 'start')}`,
  pyramide: `<path d="M14 88 H84 L60 14 Z" fill="var(--ru-tafel-tint)" stroke="none"/><path d="M14 88 H84 L106 70 M60 14 L14 88 M60 14 L84 88 M60 14 L106 70" ${L}/><path d="M14 88 L36 70 H106 M36 70 L60 14 M60 14 V79" ${D}/>${T(50, 104, 'G')}${T(63, 52, 'h', 'start')}`,
  kegel: `<path d="M22 84 L62 14 L102 84 Z" fill="var(--ru-tafel-tint)" stroke="none"/><path d="M22 84 L62 14 L102 84" ${L}/><path d="M22 84 A40 11 0 0 0 102 84" ${L}/><path d="M22 84 A40 11 0 0 1 102 84 M62 14 V84" ${D}/><path d="M62 84 H102" ${L}/>${T(82, 80, 'r')}${T(66, 54, 'h', 'start')}${T(90, 44, 's', 'start')}`,
  kugel: `<circle cx="62" cy="54" r="40" ${F}/><path d="M22 54 A40 11 0 0 0 102 54" ${L}/><path d="M22 54 A40 11 0 0 1 102 54" ${D}/><path d="M62 54 H102" ${L}/><circle cx="62" cy="54" r="2.5" fill="currentColor"/>${T(84, 49, 'r')}`,
};
const r1 = (x) => Math.round(x * 10) / 10;
// Winkel (Winkelarten): Scheitel S, ein Schenkel waagrecht, der zweite um „grad“ gedreht, Bogen mit Gradzahl
function winkelBild(grad, name) {
  const cx = 60, cy = 52, l = 46, rb = 16, w = (grad * Math.PI) / 180;
  const x2 = r1(cx + l * Math.cos(w)), y2 = r1(cy - l * Math.sin(w));
  let bogen;
  if (grad >= 360) bogen = `<circle cx="${cx}" cy="${cy}" r="${rb}" fill="var(--ru-tafel-tint)" stroke="currentColor" stroke-width="1.5"/>`;
  else if (grad === 90) bogen = `${RW(cx, cy, 1, -1).replace('stroke-width="1.3"', 'stroke-width="1.5"')}`;
  else { const bx = r1(cx + rb * Math.cos(w)), by = r1(cy - rb * Math.sin(w));
    bogen = `<path d="M${cx} ${cy} L${cx + rb} ${cy} A${rb} ${rb} 0 ${grad > 180 ? 1 : 0} 0 ${bx} ${by} Z" fill="var(--ru-tafel-tint)" stroke="currentColor" stroke-width="1.5"/>`; }
  const lw = (grad * Math.PI) / 360, lx = r1(cx + (rb + 14) * Math.cos(lw)), ly = r1(cy - (rb + 14) * Math.sin(lw) + 4);
  return svg('0 0 120 96', `${bogen}<path d="M${cx} ${cy} H${cx + l}" ${L}/>${grad < 360 ? `<path d="M${cx} ${cy} L${x2} ${y2}" ${L}/>` : ''}<circle cx="${cx}" cy="${cy}" r="2.5" fill="currentColor"/>${T(cx - 6, cy + 16, 'S')}${T(grad >= 360 ? cx : lx, grad >= 360 ? cy - rb - 6 : ly, grad + '°')}`, name);
}
// Dreieck aus drei Seiten (c unten) oder aus drei Winkeln (α, β an der Grundseite), eingepasst in 120 × 90
function dreieckBild(b, name) {
  let A = [0, 0], B, C;
  if (b.seiten) { const [a, bb, c] = b.seiten; B = [c, 0]; const x = (bb * bb + c * c - a * a) / (2 * c); C = [x, Math.sqrt(Math.max(0, bb * bb - x * x))]; }
  else { const [al, be] = b.winkel.map((g) => (g * Math.PI) / 180); B = [1, 0]; const x = Math.tan(be) / (Math.tan(al) + Math.tan(be));
    C = al === Math.PI / 2 ? [0, Math.tan(be)] : be === Math.PI / 2 ? [1, Math.tan(al)] : [x, x * Math.tan(al)]; }
  return polygonBild([A, B, C], name, ['A', 'B', 'C']);
}
// Vieleck aus Punkten (y nach oben), eingepasst in 120 × 90 mit Rand; Ecken beschriftet
function polygonBild(punkte, name, ecken = ['A', 'B', 'C', 'D']) {
  const xs = punkte.map((p) => p[0]), ys = punkte.map((p) => p[1]), minX = Math.min(...xs), maxX = Math.max(...xs), minY = Math.min(...ys), maxY = Math.max(...ys);
  const s = Math.min(92 / (maxX - minX || 1), 62 / (maxY - minY || 1)), ox = 60 - ((maxX - minX) * s) / 2, oy = 45 + ((maxY - minY) * s) / 2;
  const P = punkte.map(([x, y]) => [r1(ox + (x - minX) * s), r1(oy - (y - minY) * s)]);
  const mx = P.reduce((a, p) => a + p[0], 0) / P.length, my = P.reduce((a, p) => a + p[1], 0) / P.length;
  const marke = P.map(([x, y], i) => { const dx = x - mx, dy = y - my, n = Math.hypot(dx, dy) || 1; return T(r1(x + (dx / n) * 10), r1(y + (dy / n) * 10 + 4), ecken[i]); }).join('');
  return svg('0 0 120 90', `<path d="M${P.map((p) => p.join(' ')).join(' L')} Z" ${F}/>${marke}`, name);
}
// Kacheln der Tafel-Übersicht (64 × 52, entwurf1: einheiten, flaechen, koerper; übrige neu im selben Stil)
const IKON_TEXT = (t, x, y, gr = 15) => `<text x="${x}" y="${y}" text-anchor="middle" font-family="var(--mono)" font-size="${gr}" font-weight="700" fill="currentColor">${t}</text>`;
const KF = 'fill="var(--ru-tafel-tint)" stroke="currentColor" stroke-width="2"';
const IKON = {
  formeln: `<rect x="4" y="22" width="20" height="16" fill="var(--ru-tafel-tint)" stroke="currentColor" stroke-width="2"/><path d="M28 38 H48 L38 22 Z" fill="var(--ru-tafel-tint)" stroke="currentColor" stroke-width="2"/><circle cx="54" cy="30" r="8" fill="var(--ru-tafel-tint)" stroke="currentColor" stroke-width="2"/><path d="M6 14 H58" stroke="currentColor" stroke-width="2"/><path d="M6 8 H40" stroke="currentColor" stroke-width="2"/>`,
  einheiten: `<rect x="4" y="6" width="22" height="12" rx="4" fill="var(--ru-tafel-tint)" stroke="var(--ru-tafel-f)" stroke-width="2"/><rect x="20" y="22" width="22" height="12" rx="4" fill="var(--ru-tafel-tint)" stroke="var(--ru-tafel-f)" stroke-width="2"/><rect x="36" y="38" width="22" height="12" rx="4" fill="var(--ru-tafel-tint)" stroke="var(--ru-tafel-f)" stroke-width="2"/>`,
  'formeln-flaechen': `<rect x="4" y="10" width="30" height="22" ${KF}/><circle cx="46" cy="32" r="14" ${KF}/>`,
  'formeln-koerper': `<path d="M6 20 H34 V48 H6 Z" ${KF}/><path d="M6 20 L16 10 H44 L34 20 M44 10 V38 L34 48" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="52" cy="34" r="10" ${KF}/>`,
  zahlen: `<rect x="3" y="6" width="58" height="40" rx="8" ${KF}/>${IKON_TEXT('1 4 9', 32, 31, 14)}`,
  stellenwert: `<rect x="3" y="12" width="19" height="28" rx="4" ${KF}/><rect x="23" y="12" width="19" height="28" rx="4" ${KF}/><rect x="43" y="12" width="19" height="28" rx="4" ${KF}/>${IKON_TEXT('H', 12.5, 31, 13)}${IKON_TEXT('Z', 32.5, 31, 13)}${IKON_TEXT('E', 52.5, 31, 13)}`,
  'bruch-dezimal-prozent': `<circle cx="20" cy="26" r="16" ${KF}/><path d="M20 26 V10 A16 16 0 0 1 20 42 Z" fill="var(--ru-tafel-f)" stroke="currentColor" stroke-width="2"/>${IKON_TEXT('%', 50, 33, 20)}`,
  figuren: `<path d="M4 46 H40 L26 10 Z" ${KF}/><path d="M44 46 H62 M44 46 L58 30" fill="none" stroke="currentColor" stroke-width="2"/><path d="M52 46 A8 8 0 0 0 50 40" fill="none" stroke="currentColor" stroke-width="1.5"/>`,
  'zeichen-woerter': `<rect x="3" y="6" width="58" height="40" rx="8" ${KF}/>${IKON_TEXT('≤ π', 32, 32, 17)}`,
};

// ---------- Felder, die die App nicht zeigt ----------
const WEG = new Set(['beleg', 'pruefung', 'gleichungen', 'etappen_im_bestand', 'vorkommen_im_bestand', 'zeichnung', 'fehlbild', 'zerlegung', 'beispiel_daten', 'zaehler', 'nenner', 'stichwoerter']);
const schlank = (o) => (Array.isArray(o) ? o.map(schlank) : o && typeof o === 'object' ? Object.fromEntries(Object.entries(o).filter(([k]) => !WEG.has(k)).map(([k, v]) => [k, schlank(v)])) : o);
const klasse = (e) => (e.ab_klasse ? e.ab_klasse.gymnasium_by ?? null : null); // Klassenfilter: Gymnasium Bayern (entwurf1, Abschnitt 3)

// ---------- Tafeln: Reihenfolge, Titel der Kachel, Gebiet (Farbe), Stichwörter der ganzen Tafel (Suche) ----------
const TAFELN = [
  // Gesamtübersicht (Wunsch des Nutzers 27.11.): Ebene Figuren, Körper und „was man sonst noch braucht“ – nur Verweise auf vorhandene Formeln
  { id: 'formeln', titel: 'Formeln auf einen Blick', kurz: 'Flächen, Körper und was man sonst noch braucht', chip: 'A = a · b', gebiet: 'Fläche und Raum',
    stich: ['Formeln', 'Formel', 'Formelsammlung', 'Formelübersicht'] },
  { id: 'einheiten', titel: 'Maßeinheiten', kurz: 'Länge, Fläche, Volumen, Masse, Zeit, Geld, Tempo', chip: 'km · m · cm', gebiet: 'Geld und Verhältnisse',
    stich: ['Maßeinheiten', 'Einheiten', 'Einheit', 'umrechnen', 'Einheiten umrechnen', 'Umrechnungszahl', 'Umrechnungstabelle', 'Einheitentafel', 'Größen'] },
  { id: 'formeln-flaechen', titel: null, kurz: 'Figuren mit Fläche und Umfang', chip: 'A = a · b', gebiet: 'Fläche und Raum',
    stich: ['Fläche', 'Flächen', 'Flächeninhalt', 'Flächenformeln', 'Umfang', 'Formeln Flächen', 'Formelsammlung'] },
  { id: 'formeln-koerper', titel: null, kurz: 'Körper mit Volumen, Mantel und Oberfläche', chip: 'V = a · b · c', gebiet: 'Fläche und Raum',
    stich: ['Volumen', 'Rauminhalt', 'Körper', 'Körperformeln', 'Oberfläche', 'Mantel', 'Formeln Körper', 'Formelsammlung'] },
  { id: 'zahlen', titel: null, kurz: 'Quadratzahlen, Potenzen, Primzahlen, Teilbarkeit', chip: '1 4 9 16', gebiet: 'Zahlen', stich: ['Zahlen', 'Quadratzahlen', 'Primzahlen', 'Teilbarkeit', 'Potenzen'] },
  { id: 'stellenwert', titel: null, kurz: 'Stellenwerttafel, Runden, römische Zahlen, Vorsilben', chip: 'H Z E', gebiet: 'Zahlen', stich: ['Stellenwert', 'Stellenwerttafel', 'Runden', 'römische Zahlen', 'Vorsilben'] },
  { id: 'bruch-dezimal-prozent', titel: null, kurz: 'Umrechnungstabelle, Prozentrechnung, Zinsen', chip: '½ = 0,5 = 50 %', gebiet: 'Geld und Verhältnisse',
    stich: ['Prozent', 'Prozentrechnung', 'Bruch', 'Brüche', 'Dezimalzahl', 'Dezimalzahlen', 'Zinsen'] },
  { id: 'figuren', titel: null, kurz: 'Winkel, Dreiecke, Vierecke, Kongruenz', chip: 'α + β + γ = 180°', gebiet: 'Geometrie',
    stich: ['Figuren', 'Winkel', 'Winkelarten', 'Dreiecke', 'Vierecke', 'Kongruenz'] },
  { id: 'zeichen-woerter', titel: null, kurz: 'Zeichen, griechische Buchstaben, Fachwörter', chip: '≤ · π · ∈', gebiet: 'Algebra',
    stich: ['Zeichen', 'Rechenzeichen', 'Symbole', 'griechische Buchstaben', 'Fachwörter', 'Wörterbuch', 'Fachbegriffe'] },
];
// Formeltafeln: je Figur/Körper eine Karte (Zeichnung + Zeilen). „zusatz“: Zeilen im Aufklapper (formeln-koerper/tafel.md: Raumdiagonale, Kantenlänge als Zusatz).
const KARTEN = {
  'formeln-flaechen': [['rechteck', 'Rechteck', ['ff-01', 'ff-02']], ['quadrat', 'Quadrat', ['ff-03', 'ff-12']], ['parallelogramm', 'Parallelogramm', ['ff-04', 'ff-14']],
    ['dreieck', 'Dreieck', ['ff-05', 'ff-13']], ['trapez', 'Trapez', ['ff-06', 'ff-15']], ['drachen', 'Drachenviereck und Raute', ['ff-07', 'ff-16', 'ff-17']],
    ['kreis', 'Kreis', ['ff-09', 'ff-08']], ['ausschnitt', 'Kreisausschnitt', ['ff-11', 'ff-10']], ['kreisring', 'Kreisring', ['ff-18']]],
  'formeln-koerper': [['quader', 'Quader', ['fk-01', 'fk-03'], ['fk-20', 'fk-22']], ['wuerfel', 'Würfel', ['fk-02', 'fk-04'], ['fk-21']], ['prisma', 'Prisma', ['fk-05', 'fk-06', 'fk-07']],
    ['zylinder', 'Zylinder', ['fk-08', 'fk-09', 'fk-10']], ['pyramide', 'Pyramide', ['fk-11', 'fk-12', 'fk-18', 'fk-19']], ['kegel', 'Kegel', ['fk-13', 'fk-14', 'fk-15']],
    ['kugel', 'Kugel', ['fk-16', 'fk-17']]],
};
// „Was man sonst noch braucht“ (Gesamtübersicht der Formeln): vorhandene Formeln der Tafeln und Einzelregeln mit Formel im Merksatz, nach Klasse geordnet.
// kurz/bed: Kurzform des Merksatzes der Einzelregel in Formelschreibweise (nur Darstellung, Wunsch des Projektleiters 27.11.); der Merksatz steht wörtlich in den Einzelheiten.
const SONST = [{ gesetz: 'V2' }, { tafel: 'bruch-dezimal-prozent', kennung: 'bd-02' }, { tafel: 'bruch-dezimal-prozent', kennung: 'bd-03' }, { tafel: 'bruch-dezimal-prozent', kennung: 'bd-04' },
  { tafel: 'bruch-dezimal-prozent', kennung: 'bd-05' }, { gesetz: 'D3', kurz: ['Mittelwert = Summe aller Werte : Anzahl der Werte'] }, { tafel: 'figuren', kennung: 'fg-07' }, { gesetz: 'A4' },
  { tafel: 'bruch-dezimal-prozent', kennung: 'bd-06' },
  { gesetz: 'D4', kurz: ['Median: der mittlere Wert der geordneten Liste', 'Modalwert: der häufigste Wert', 'Spannweite = größter Wert − kleinster Wert'] },
  { gesetz: 'D13', kurz: ['P = günstige Ergebnisse : mögliche Ergebnisse'], bed: 'nur wenn alle Ergebnisse gleich wahrscheinlich sind' },
  { gesetz: 'U7', kurz: ['y = m · x + t'], bed: 'm ist die Steigung, t der Abschnitt auf der y-Achse' },
  { gesetz: 'G24', kurz: ['a² + b² = c²'], bed: 'nur im rechtwinkligen Dreieck; a, b Katheten, c Hypotenuse' },
  { gesetz: 'G25', kurz: ['sin α = Gegenkathete : Hypotenuse', 'cos α = Ankathete : Hypotenuse', 'tan α = Gegenkathete : Ankathete'] },
  { gesetz: 'A19', kurz: ['x = (−b ± √(b² − 4ac)) : (2a)'], bed: 'für a · x² + b · x + c = 0 mit a ≠ 0' }];
const ID_ART = { 'Länge': 'laenge', 'Fläche': 'flaeche', 'Volumen und Hohlmaße': 'volumen', 'Masse': 'masse', 'Zeit': 'zeit', 'Geld': 'geld', 'Geschwindigkeit': 'tempo', 'Dichte': 'dichte' };

function tafelnBauen(json) {
  const MP = ['inhalte', 'mathe-profi', 'regeln-uebersicht'];
  const quellen = { einheiten: json(...MP, 'einheiten', 'einheiten.json') };
  for (const t of TAFELN.slice(2)) quellen[t.id] = json(...MP, 'tafeln', t.id, t.id + '.json');
  const tafeln = TAFELN.map((t) => {
    if (t.id === 'formeln') { // nur Verweise; die App liest Formeln und Sätze aus den Tafeln und den Einzelregeln
      for (const z of SONST) assert.ok(z.gesetz || quellen[z.tafel].eintraege.some((e) => e.kennung === z.kennung), JSON.stringify(z));
      return { id: t.id, titel: t.titel, kurz: t.kurz, chip: t.chip, gebiet: t.gebiet, stich: t.stich, ikon: svg('0 0 64 52', IKON[t.id], ''), teile: ['formeln-flaechen', 'formeln-koerper'], sonst: SONST };
    }
    const q = quellen[t.id], aus = { id: t.id, titel: t.titel || q.titel, kurz: t.kurz, chip: t.chip, gebiet: t.gebiet, stich: t.stich, stand: q.stand, ikon: svg('0 0 64 52', IKON[t.id], '') };
    if (t.id === 'einheiten') {
      aus.richtung = q.regel_der_richtung; aus.nicht_aufgenommen = q.nicht_aufgenommen;
      // je Größenart: Anker, Klasse, Stichwörter (Name der Art, alle Einheiten mit Namen – Vorschlag einheiten/vorschlag.md, Abschnitt 3)
      aus.arten = q.arten.map((x) => ({ anker: ID_ART[x.art], kl: klasse(x), stich: [x.art, ...[...x.treppe, ...(x.weitere_treppen || []).flatMap((w) => w.treppe)].flatMap((s) => [s.einheit, s.name])], ...schlank(x) }));
      assert.ok(aus.arten.every((x) => x.anker), 'jede Größenart hat einen Anker');
    } else if (KARTEN[t.id]) {
      const E = Object.fromEntries(q.eintraege.map((e) => [e.kennung, e]));
      const benutzt = new Set();
      aus.groessenarten = q.groessenarten;
      aus.karten = KARTEN[t.id].map(([anker, name, zeilen, zusatz = []]) => { const alle = [...zeilen, ...zusatz]; alle.forEach((k) => { assert.ok(E[k], k); benutzt.add(k); });
        const kl = alle.map((k) => klasse(E[k])).filter((x) => x != null);
        return { anker, name, bild: svg(anker === 'kreis' || anker === 'ausschnitt' || anker === 'kreisring' || t.id === 'formeln-flaechen' ? '0 0 120 90' : '0 0 124 112', BILD[anker], name), kl: kl.length ? Math.min(...kl) : null,
          stich: [...new Set([name, ...alle.flatMap((k) => E[k].stichwoerter || [])])], zeilen: zeilen.map((k) => ({ ...schlank(E[k]), kl: klasse(E[k]) })), zusatz: zusatz.map((k) => ({ ...schlank(E[k]), kl: klasse(E[k]) })) }; });
      assert.deepEqual([...benutzt].sort(), Object.keys(E).sort(), t.id + ': jede Formel steht auf einer Karte');
    } else {
      if (q.abschnitte) aus.abschnitte = q.abschnitte;
      aus.eintraege = q.eintraege.map((e) => {
        const x = { ...schlank(e), kl: klasse(e), stich: [...new Set([e.titel, ...(e.stichwoerter || [])])] };
        if (e.art === 'winkelart') x.bild = winkelBild(e.beispiel_winkel, e.titel);
        if (e.art === 'dreieck') x.bild = dreieckBild(e.beispiele.find((b) => b.seiten) || e.beispiele[0], e.titel);
        if (e.art === 'viereck') x.bild = polygonBild(e.beispiel_punkte, e.titel);
        return x;
      });
    }
    return aus;
  });
  return tafeln;
}
module.exports = { tafelnBauen };
