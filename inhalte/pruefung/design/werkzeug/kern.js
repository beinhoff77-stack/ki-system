/* Gemeinsamer Kern der drei Gestaltungsentwürfe (Prüfrunde Gestaltung).
   Enthält nur Beispieldaten, Prüflogik, Eingabe (Zahlentasten, Zahlenstrahl), Zeichnungen und die Weltkarte.
   Aussehen und Aufbau der Bildschirme legt jede Richtung selbst fest (Funktion zeichne()).
   Weltkarte: Natural Earth (gemeinfrei), übernommen aus lernen-welt.js. */
'use strict';
const WELT = __WELT__;

// ---------- Beispieldaten (frei erfunden) ----------
const DATEN = {
  kinder: {
    a: { id: 'a', name: 'Ida', alter: 10, klasse: 5, sterne: 340, stempel: 1, ort: 'rom' },
    b: { id: 'b', name: 'Max', alter: 13, klasse: 8, sterne: 610, stempel: 2, ort: 'kairo' },
  },
  gebiete: {
    zahlen: { name: 'Zahlen', erdteil: 'EU', erdteilName: 'Europa' },
    algebra: { name: 'Algebra', erdteil: 'AS', erdteilName: 'Asien' },
    geld: { name: 'Geld', erdteil: 'NA', erdteilName: 'Nordamerika' },
    funktionen: { name: 'Funktionen', erdteil: 'AF', erdteilName: 'Afrika' },
    geometrie: { name: 'Geometrie', erdteil: 'SA', erdteilName: 'Südamerika' },
    daten: { name: 'Daten', erdteil: 'OC', erdteilName: 'Ozeanien' },
  },
  // stand je Kind: geschafft | jetzt | offen | spaeter
  orte: [
    { id: 'lissabon', stadt: 'Lissabon', land: 'Portugal', lat: 38.72, lon: -9.14, gebiet: 'zahlen', thema: 'Rechnen mit großen Zahlen', klasse: 5, stand: { a: 'geschafft', b: 'geschafft' } },
    { id: 'rom', stadt: 'Rom', land: 'Italien', lat: 41.9, lon: 12.5, gebiet: 'zahlen', thema: 'Natürliche Zahlen', klasse: 5, stand: { a: 'jetzt', b: 'geschafft' } },
    { id: 'athen', stadt: 'Athen', land: 'Griechenland', lat: 37.98, lon: 23.73, gebiet: 'zahlen', thema: 'Teilbarkeit', klasse: 5, stand: { a: 'offen', b: 'geschafft' } },
    { id: 'pisa', stadt: 'Pisa', land: 'Italien', lat: 43.72, lon: 10.4, gebiet: 'zahlen', thema: 'Brüche', klasse: 6, stand: { a: 'spaeter', b: 'geschafft' } },
    { id: 'newyork', stadt: 'New York', land: 'USA', lat: 40.71, lon: -74.01, gebiet: 'geld', thema: 'Prozent und Zinsen', klasse: 7, stand: { a: 'spaeter', b: 'geschafft' } },
    { id: 'samarkand', stadt: 'Samarkand', land: 'Usbekistan', lat: 39.65, lon: 66.96, gebiet: 'algebra', thema: 'Terme umformen', klasse: 7, stand: { a: 'spaeter', b: 'geschafft' } },
    { id: 'kairo', stadt: 'Kairo', land: 'Ägypten', lat: 30.04, lon: 31.24, gebiet: 'funktionen', thema: 'Lineare Funktionen', klasse: 8, stand: { a: 'spaeter', b: 'jetzt' } },
    { id: 'kapstadt', stadt: 'Kapstadt', land: 'Südafrika', lat: -33.92, lon: 18.42, gebiet: 'funktionen', thema: 'Lineare Gleichungssysteme', klasse: 8, stand: { a: 'spaeter', b: 'offen' } },
    { id: 'lima', stadt: 'Lima', land: 'Peru', lat: -12.05, lon: -77.04, gebiet: 'geometrie', thema: 'Satz des Pythagoras', klasse: 8, stand: { a: 'spaeter', b: 'offen' } },
    { id: 'sydney', stadt: 'Sydney', land: 'Australien', lat: -33.87, lon: 151.21, gebiet: 'daten', thema: 'Daten darstellen', klasse: 5, stand: { a: 'offen', b: 'geschafft' } },
  ],
  // Lernkarten je Ort (nur die zwei durchspielbaren Orte)
  karten: {
    rom: [
      { id: 'stellenwert', titel: 'Welchen Wert hat eine Ziffer?', kurz: 'Stellenwert', bild: 'stellentafel',
        regel: 'Jeder Platz ist 10-mal so viel wert wie der Platz rechts daneben.',
        schritte: [
          { text: 'Schau dir die Zahl 4 052 an.', tafel: { zahl: '4052', mark: -1 } },
          { text: 'Die 4 steht bei den Tausendern (T).', tafel: { zahl: '4052', mark: 0 } },
          { text: 'Ein Tausender ist 1 000 wert.', tafel: { zahl: '4052', mark: 0, pfeil: true } },
          { text: 'Also ist die 4 genau 4 000 wert.', tafel: { zahl: '4052', mark: 0, wert: '4 000' } },
        ],
        falle: { titel: 'Die 0 hält den Platz frei', falsch: '4 052 → „vierhundertzweiundfünfzig“', richtig: '4 052 → viertausendzweiundfünfzig', warum: 'Die 0 zeigt: keine Hunderter. Ohne sie rutscht die 4 einen Platz nach rechts.' },
        aufgaben: [
          { art: 'zahl', frage: 'Welchen Wert hat die 2 in 182 887?', zahl: '182887', ziffer: 2, loesung: '2000', tipp: 'Zähl von rechts: E, Z, H, T …' },
          { art: 'zahl', frage: 'Welchen Wert hat die 7 in 74 310?', zahl: '74310', ziffer: 7, loesung: '70000', tipp: 'Die 7 steht ganz links. Wie viele Stellen hat die Zahl?' },
          { art: 'zahl', frage: 'Welchen Wert hat die 5 in 1 503 000?', zahl: '1503000', ziffer: 5, loesung: '500000', tipp: 'Die 5 steht hinter der Million.' },
        ] },
      { id: 'strahl', titel: 'Zahlen am Zahlenstrahl', kurz: 'Zahlenstrahl', bild: 'strahl',
        regel: 'Erst ausrechnen, wie viel ein Abschnitt wert ist. Dann abzählen.',
        schritte: [
          { text: 'Der Strahl geht von 0 bis 100.', strahl: { start: 0, ende: 100, n: 10 } },
          { text: 'Er hat 10 gleiche Abschnitte.', strahl: { start: 0, ende: 100, n: 10, zaehl: true } },
          { text: '100 : 10 = 10. Jeder Abschnitt ist 10 wert.', strahl: { start: 0, ende: 100, n: 10, zaehl: true, werte: true } },
          { text: 'Die 30 liegt also beim 3. Strich.', strahl: { start: 0, ende: 100, n: 10, werte: true, marker: 3 } },
        ],
        falle: { titel: 'Nicht die Striche zählen, die Abschnitte!', falsch: '0 bis 40 000, 8 Abschnitte → „ein Strich ist 1 000“', richtig: '40 000 : 8 = 5 000 je Abschnitt', warum: 'Erst die Länge eines Abschnitts ausrechnen, dann abzählen.' },
        aufgaben: [
          { art: 'strahl', frage: 'Schieb den Punkt auf 20 000.', start: 0, ende: 40000, n: 8, loesung: 4, tipp: '40 000 : 8 = ?' },
          { art: 'strahl', frage: 'Schieb den Punkt auf 600.', start: 0, ende: 1000, n: 5, loesung: 3, tipp: 'Ein Abschnitt ist 200 wert.' },
          { art: 'strahl', frage: 'Schieb den Punkt auf 70.', start: 0, ende: 100, n: 10, loesung: 7, tipp: 'Ein Abschnitt ist 10 wert.' },
        ] },
      { id: 'runden', titel: 'Runden', kurz: 'Runden', bild: 'stellentafel',
        regel: 'Schau auf die Ziffer rechts neben der Rundungsstelle: 0–4 abrunden, 5–9 aufrunden.',
        schritte: [
          { text: 'Runde 48 372 auf Tausender.', tafel: { zahl: '48372', mark: 1 } },
          { text: 'Rechts daneben steht eine 3.', tafel: { zahl: '48372', mark: 2 } },
          { text: '3 ist kleiner als 5: abrunden.', tafel: { zahl: '48372', mark: 2 } },
          { text: 'Ergebnis: 48 000.', tafel: { zahl: '48000', mark: 1, wert: '48 000' } },
        ],
        falle: { titel: 'Nur eine Ziffer entscheidet', falsch: '48 372 → 49 000, „weil 72 groß ist“', richtig: '48 372 → 48 000', warum: 'Nur die Ziffer direkt rechts (hier die 3) entscheidet.' },
        aufgaben: [
          { art: 'zahl', frage: 'Runde 48 372 auf Tausender.', loesung: '48000', tipp: 'Welche Ziffer steht rechts neben der 8?' },
          { art: 'zahl', frage: 'Runde 2 650 auf Hunderter.', loesung: '2700', tipp: 'Rechts neben der 6 steht eine 5.' },
          { art: 'zahl', frage: 'Runde 9 950 auf Tausender.', loesung: '10000', tipp: 'Aufrunden über die 9 hinaus.' },
        ] },
    ],
    kairo: [
      { id: 'steigung', titel: 'Steigung ablesen', kurz: 'Steigung', bild: 'koordinaten',
        regel: 'Die Steigung m sagt: Geh 1 nach rechts – so viel geht es nach oben (oder unten).',
        schritte: [
          { text: 'Das ist die Gerade y = 2x + 1.', koord: { m: 2, t: 1 } },
          { text: 'Start bei einem Punkt auf der Geraden: (0 | 1).', koord: { m: 2, t: 1, punkt: true } },
          { text: 'Geh 1 nach rechts …', koord: { m: 2, t: 1, punkt: true, rechts: true } },
          { text: '… dann 2 nach oben. Die Steigung ist m = 2.', koord: { m: 2, t: 1, punkt: true, rechts: true, hoch: true } },
        ],
        falle: { titel: 'Steigung ≠ Achsenabschnitt', falsch: 'y = 2x + 1 → „Steigung 1“', richtig: 'y = 2x + 1 → Steigung 2', warum: 'Die Zahl vor dem x ist die Steigung. Die Zahl allein ist der Schnittpunkt mit der y-Achse.' },
        aufgaben: [
          { art: 'zahl', frage: 'Wie groß ist die Steigung von y = 2x + 1?', loesung: '2', tipp: 'Die Zahl vor dem x.' },
          { art: 'zahl', frage: 'Wie groß ist die Steigung von y = −3x + 4?', loesung: '-3', tipp: 'Das Vorzeichen gehört dazu.' },
          { art: 'zahl', frage: 'Gerade durch (0 | 1) und (2 | 5). Steigung?', loesung: '2', tipp: '(5 − 1) : (2 − 0)' },
        ] },
      { id: 'achsenabschnitt', titel: 'Wo schneidet die Gerade die y-Achse?', kurz: 'Achsenabschnitt', bild: 'koordinaten', regel: 'Setze x = 0 ein.', schritte: [], aufgaben: [] },
      { id: 'gleichung', titel: 'Gleichung aufstellen', kurz: 'Gleichung', bild: 'koordinaten', regel: 'y = m · x + t', schritte: [], aufgaben: [] },
    ],
  },
  // Lernstand für Eltern/Lehrkraft (Beispiel)
  lernstand: {
    a: { tage: [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1], woche: { aufgaben: 30, richtig: 22, tipp: 4 },
      karten: [
        { ort: 'Rom', titel: 'Stellenwert', zustand: 'sitzt', richtig: 6, falsch: 1 },
        { ort: 'Rom', titel: 'Zahlenstrahl', zustand: 'ueben', richtig: 2, falsch: 1 },
        { ort: 'Rom', titel: 'Runden', zustand: 'wackelt', richtig: 2, falsch: 5, beispiel: '48 372 → 49 000 (statt 48 000)' },
        { ort: 'Lissabon', titel: 'Große Zahlen addieren', zustand: 'sitzt', richtig: 9, falsch: 0 }],
      wunsch: { titel: 'Eis', kosten: '300 Sterne' } },
    b: { tage: [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1], woche: { aufgaben: 41, richtig: 35, tipp: 2 },
      karten: [
        { ort: 'Kairo', titel: 'Steigung', zustand: 'ueben', richtig: 3, falsch: 1 },
        { ort: 'Kairo', titel: 'Achsenabschnitt', zustand: 'offen', richtig: 0, falsch: 0 },
        { ort: 'Kairo', titel: 'Gleichung aufstellen', zustand: 'offen', richtig: 0, falsch: 0 },
        { ort: 'Samarkand', titel: 'Klammern auflösen', zustand: 'wackelt', richtig: 4, falsch: 4, beispiel: '−(x − 3) → −x − 3 (statt −x + 3)' }],
      wunsch: null },
  },
  belohnungen: [{ titel: 'Eis', kosten: 300, art: 'sterne' }, { titel: 'Kinoabend', kosten: 3, art: 'stempel' }],
  stempel: { a: ['lissabon'], b: ['lissabon', 'newyork'] },
};

// ---------- Zustand ----------
const S = {
  kind: 'a', ansicht: 'heute', teil: 'erklaeren', karte: 0, schritt: 0, aufgabe: 0,
  eingabe: '', strahl: null, ergebnis: null, tipp: false, serie: {}, sitzt: {}, neuSitzt: false,
  dunkel: matchMedia('(prefers-color-scheme: dark)').matches, ziehen: false,
};
const kind = () => DATEN.kinder[S.kind];
const ortVon = (id) => DATEN.orte.find((o) => o.id === id);
const ortJetzt = () => ortVon(kind().ort);
const karten = () => DATEN.karten[kind().ort] || [];
const karteJetzt = () => karten()[S.karte];
const aufgabeJetzt = () => { const k = karteJetzt(); return k && k.aufgaben.length ? k.aufgaben[S.aufgabe % k.aufgaben.length] : null; };
const serie = () => S.serie[S.kind + karteJetzt()?.id] || 0;
const sitztKarte = (i) => !!S.sitzt[S.kind + karten()[i]?.id];
const anzahlSitzt = () => karten().filter((_, i) => sitztKarte(i)).length;

// ---------- Hilfen ----------
// Escapen; Zahlen wie 182 887 nicht umbrechen (geschütztes Leerzeichen)
const esc = (t) => String(t ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])).replace(/(\d) (?=\d{3}(?!\d))/g, '$1\u00a0');
const NB = ' ';
const gruppiere = (z) => { const neg = String(z).startsWith('-'); const [g, d] = String(z).replace('-', '').split(','); const t = g.replace(/\B(?=(\d{3})+(?!\d))/g, NB); return (neg ? '−' : '') + t + (d !== undefined ? ',' + d : ''); };
const STELLEN = ['E', 'Z', 'H', 'T', 'ZT', 'HT', 'M'];

// ---------- Eingabe: Zahlentasten ----------
const tastenFuer = () => (kind().klasse >= 7 ? ['7', '8', '9', '4', '5', '6', '1', '2', '3', '−', '0', ','] : ['7', '8', '9', '4', '5', '6', '1', '2', '3', '00', '0', '000']);
function taste(k) {
  if (S.ergebnis) return;
  let e = S.eingabe;
  if (k === '⌫') e = e.slice(0, -1);
  else if (k === '−') e = e.startsWith('-') ? e.slice(1) : '-' + e;
  else if (k === ',') { if (!e.includes(',')) e = (e.replace('-', '') ? e : e + '0') + ','; }
  else if (e.replace(/[-,]/g, '').length + k.length <= 9) e = (e === '0' ? '' : e) + k;
  S.eingabe = e; neu();
}

// ---------- Prüfen ----------
function istRichtig(a) {
  if (a.art === 'strahl') return S.strahl === a.loesung;
  return S.eingabe.replace(',', '.') !== '' && Number(S.eingabe.replace(',', '.')) === Number(a.loesung);
}
// Freundliche Diagnose: Was hat das Kind vermutlich gedacht?
function diagnose(a) {
  if (a.art === 'strahl') {
    if (S.strahl == null) return '';
    const schritt = (a.ende - a.start) / a.n; const wert = a.start + S.strahl * schritt;
    return `Dein Punkt liegt bei ${gruppiere(wert)}. Ein Abschnitt ist ${gruppiere(schritt)} wert.`;
  }
  if (a.zahl && a.ziffer != null) {
    const v = Number(S.eingabe); if (!v) return '';
    const stelleRichtig = String(Number(a.loesung)).length - 1; const stelleKind = String(v).length - 1;
    if (String(v)[0] === String(a.ziffer) && /^\d0*$/.test(String(v)) && stelleKind !== stelleRichtig)
      return `Du hast die ${a.ziffer} bei den ${['Einern', 'Zehnern', 'Hundertern', 'Tausendern', 'Zehntausendern', 'Hunderttausendern', 'Millionen'][stelleKind]} gelesen. Sie steht aber bei den ${['Einern', 'Zehnern', 'Hundertern', 'Tausendern', 'Zehntausendern', 'Hunderttausendern', 'Millionen'][stelleRichtig]}.`;
    if (v === a.ziffer) return `Die Ziffer ist ${a.ziffer} – gefragt ist, wie viel sie an ihrem Platz wert ist.`;
  }
  if (a.loesung === '-3' && S.eingabe === '3') return 'Fast: Das Minus gehört dazu. Die Gerade fällt.';
  return '';
}
function pruefen() {
  const a = aufgabeJetzt(); if (!a || S.ergebnis) return;
  if (a.art === 'strahl' ? S.strahl == null : !S.eingabe.replace(/[-,]/g, '')) { S.hinweis = a.art === 'strahl' ? 'Schieb zuerst den Punkt.' : 'Tipp zuerst deine Antwort ein.'; neu(); return; }
  const ok = istRichtig(a); const key = S.kind + karteJetzt().id;
  S.ergebnis = ok ? 'richtig' : 'falsch'; S.hinweis = '';
  if (ok && !S.tipp) S.serie[key] = (S.serie[key] || 0) + 1; else if (!ok) S.serie[key] = 0;
  S.neuSitzt = ok && !S.sitzt[key] && S.serie[key] >= 2; if (S.neuSitzt) { S.sitzt[key] = true; kind().sterne += 20; }
  if (ok && !S.tipp) kind().sterne += 10;
  neu();
}
function weiter() { S.aufgabe++; S.eingabe = ''; S.strahl = null; S.ergebnis = null; S.tipp = false; S.neuSitzt = false; S.hinweis = ''; neu(); }

// ---------- Zeichnungen (SVG/HTML, Farben über CSS-Variablen der Richtung) ----------
function stellentafel(t, { gross = false } = {}) {
  const z = t.zahl.split(''); const n = z.length;
  const kopf = z.map((_, i) => STELLEN[n - 1 - i]);
  return `<table class="k-tafel${gross ? ' gross' : ''}" aria-label="Stellentafel ${esc(gruppiere(t.zahl))}"><tr>${kopf.map((k, i) => `<th class="${i === t.mark ? 'an' : ''}">${k}</th>`).join('')}</tr>
    <tr>${z.map((d, i) => `<td class="${i === t.mark ? 'an' : ''}">${d}</td>`).join('')}</tr></table>${t.pfeil ? `<p class="k-tafel-notiz">1 T = 1${NB}000</p>` : ''}${t.wert ? `<p class="k-tafel-wert">${t.wert}</p>` : ''}`;
}
// Zahlenstrahl; ziehbar = Punkt mit Finger/Maus/Pfeiltasten verschieben
function strahl(s, { ziehbar = false, wahl = null, loesung = null, breite = 340 } = {}) {
  const L = 22, R = breite - 22, Y = 46, x = (i) => L + (R - L) * i / s.n;
  let o = `<svg class="k-strahl${ziehbar ? ' ziehbar' : ''}" viewBox="0 0 ${breite} 92" ${ziehbar ? `data-strahl="${s.n}" tabindex="0" role="slider" aria-label="Punkt auf dem Zahlenstrahl" aria-valuemin="0" aria-valuemax="${s.n}" aria-valuenow="${wahl ?? 0}" aria-valuetext="${wahl == null ? 'noch nicht gesetzt' : gruppiere(s.start + wahl * (s.ende - s.start) / s.n)}"` : 'role="img" aria-label="Zahlenstrahl"'}>`;
  o += `<line x1="${L - 8}" y1="${Y}" x2="${R + 12}" y2="${Y}" class="k-achse"/><path d="M${R + 14} ${Y} l-9 -5 v10 z" class="k-spitze"/>`;
  for (let i = 0; i <= s.n; i++) {
    o += `<line x1="${x(i)}" y1="${Y - 9}" x2="${x(i)}" y2="${Y + 9}" class="k-strich"/>`;
    if (s.zaehl && i < s.n) o += `<text x="${(x(i) + x(i + 1)) / 2}" y="${Y - 16}" class="k-zaehl">${i + 1}</text>`;
    if (i === 0 || i === s.n || s.werte) o += `<text x="${x(i)}" y="${Y + 32}" class="k-wert">${gruppiere(s.start + i * (s.ende - s.start) / s.n)}</text>`;
  }
  if (s.marker != null) o += `<circle cx="${x(s.marker)}" cy="${Y}" r="9" class="k-marker"/>`;
  if (loesung != null && wahl !== loesung) o += `<circle cx="${x(loesung)}" cy="${Y}" r="11" class="k-loesung"/>`;
  if (ziehbar) {
    o += `<rect x="0" y="0" width="${breite}" height="92" fill="transparent" class="k-flaeche"/>`;
    if (wahl != null) o += `<g class="k-griff" transform="translate(${x(wahl)} ${Y})"><circle r="17" class="k-griff-ring"/><circle r="9" class="k-griff-kern"/></g>`;
    else o += `<g class="k-griff k-griff-start" transform="translate(${L} ${Y})"><circle r="17" class="k-griff-ring"/><circle r="9" class="k-griff-kern"/></g>`;
  }
  return o + '</svg>';
}
function koordinaten(k, { breite = 300 } = {}) {
  const h = breite, u = breite / 8, ox = breite * 3 / 8, oy = h * 5 / 8; const px = (x) => ox + x * u, py = (y) => oy - y * u;
  let o = `<svg class="k-koord" viewBox="0 0 ${breite} ${h}" role="img" aria-label="Gerade y = ${k.m}x + ${k.t}">`;
  for (let i = -3; i <= 5; i++) { o += `<line x1="${px(i)}" y1="0" x2="${px(i)}" y2="${h}" class="k-gitter"/><line x1="0" y1="${py(i)}" x2="${breite}" y2="${py(i)}" class="k-gitter"/>`; }
  o += `<line x1="0" y1="${oy}" x2="${breite}" y2="${oy}" class="k-achse"/><line x1="${ox}" y1="0" x2="${ox}" y2="${h}" class="k-achse"/>`;
  o += `<text x="${breite - 12}" y="${oy - 8}" class="k-wert">x</text><text x="${ox + 10}" y="16" class="k-wert">y</text>`;
  const x1 = -3, x2 = 3; o += `<line x1="${px(x1)}" y1="${py(k.m * x1 + k.t)}" x2="${px(x2)}" y2="${py(k.m * x2 + k.t)}" class="k-gerade"/>`;
  if (k.punkt) o += `<circle cx="${px(0)}" cy="${py(k.t)}" r="7" class="k-marker"/>`;
  if (k.rechts) o += `<line x1="${px(0)}" y1="${py(k.t)}" x2="${px(1)}" y2="${py(k.t)}" class="k-dreieck"/><text x="${px(0.5)}" y="${py(k.t) + 24}" class="k-wert">1</text>`;
  if (k.hoch) o += `<line x1="${px(1)}" y1="${py(k.t)}" x2="${px(1)}" y2="${py(k.t + k.m)}" class="k-dreieck"/><text x="${px(1) + 12}" y="${py(k.t + k.m / 2) + 6}" class="k-wert">${k.m}</text>`;
  return o + '</svg>';
}
function bildFuer(schritt, opt = {}) {
  if (schritt.tafel) return stellentafel(schritt.tafel, opt);
  if (schritt.strahl) return strahl(schritt.strahl, opt);
  if (schritt.koord) return koordinaten(schritt.koord, opt);
  return '';
}

// ---------- Weltkarte ----------
function projektion(lon, lat) {
  const l = lon * Math.PI / 180, f = lat * Math.PI / 180, f2 = f * f, f4 = f2 * f2;
  const x = l * (0.8707 - 0.131979 * f2 + f4 * (-0.013791 + f4 * (0.003971 * f2 - 0.001529 * f4)));
  const y = f * (1.007226 + f2 * (0.015085 + f4 * (-0.044475 + 0.028874 * f2 - 0.005916 * f4)));
  return [WELT.tx + WELT.k * x, WELT.ty - WELT.k * y];
}
// Weltkarte als SVG. ausschnitt = [x, y, w, h] im Kartenmaß; zusatz = SVG-Text über der Karte (Bögen, Punkte)
function weltkarte({ ausschnitt = [0, 20, 1000, 500], klasse = '', zusatz = '', land = true, label = 'Weltkarte' } = {}) {
  return `<svg class="k-welt ${klasse}" viewBox="${ausschnitt.join(' ')}" preserveAspectRatio="xMidYMid meet" role="img" aria-label="${esc(label)}">
    <rect x="-50" y="-50" width="1100" height="650" class="k-meer"/>
    ${land ? ['AN', 'SA', 'NA', 'AF', 'EU', 'AS', 'OC'].map((k) => `<path d="${WELT.pfade[k]}" class="k-land k-land-${k}"/>`).join('') : ''}${zusatz}</svg>`;
}
const pkt = (o) => projektion(o.lon, o.lat);
function bogen(a, b, hoehe = 0.25) { const [x1, y1] = pkt(a), [x2, y2] = pkt(b); const mx = (x1 + x2) / 2, my = (y1 + y2) / 2 - Math.hypot(x2 - x1, y2 - y1) * hoehe; return `M${x1.toFixed(1)} ${y1.toFixed(1)} Q${mx.toFixed(1)} ${my.toFixed(1)} ${x2.toFixed(1)} ${y2.toFixed(1)}`; }

// ---------- Steuerung ----------
const A = {}; // Aktionen: data-akt="name" data-arg="…"
Object.assign(A, {
  geh: (v) => { S.ansicht = v; S.offen = null; neu(true); },
  kind: (id) => { S.kind = id; S.karte = 0; S.aufgabe = 0; S.schritt = 0; S.eingabe = ''; S.strahl = null; S.ergebnis = null; S.ansicht = 'heute'; neu(true); },
  teil: (t) => { S.teil = t; S.ansicht = 'thema'; S.schritt = 0; neu(true); },
  karte: (i) => { S.karte = Number(i); S.aufgabe = 0; S.schritt = 0; S.eingabe = ''; S.strahl = null; S.ergebnis = null; S.tipp = false; S.neuSitzt = false; neu(true); },
  schritt: (d) => { const n = karteJetzt().schritte.length; S.schritt = Math.max(0, Math.min(n - 1, S.schritt + Number(d))); neu(); },
  taste: (k) => taste(k), pruefen, weiter,
  tipp: () => { S.tipp = true; neu(); },
  dunkel: () => { S.dunkel = !S.dunkel; neu(); },
  zeigen: (x) => { S.offen = S.offen === x ? null : x; neu(); },
  naechsteKarte: () => { A.karte(Math.min(karten().length - 1, S.karte + 1)); },
  los: () => { S.ansicht = 'thema'; S.teil = sitztKarte(S.karte) ? 'ueben' : 'erklaeren'; neu(true); },
});
document.addEventListener('click', (e) => {
  const t = e.target.closest('[data-akt]'); if (!t) return;
  e.preventDefault(); const f = A[t.dataset.akt]; if (f) f(t.dataset.arg);
});
// Zahlenstrahl ziehen (Finger, Maus) – rastet auf Strichen ein
function strahlAus(svg, clientX) {
  const r = svg.getBoundingClientRect(); const vb = svg.viewBox.baseVal; const n = Number(svg.dataset.strahl);
  const xs = (clientX - r.left) / r.width * vb.width; const L = 22, R = vb.width - 22;
  return Math.max(0, Math.min(n, Math.round((xs - L) / (R - L) * n)));
}
document.addEventListener('pointerdown', (e) => {
  const svg = e.target.closest('svg[data-strahl]'); if (!svg || S.ergebnis) return;
  S.ziehen = true; svg.setPointerCapture?.(e.pointerId); S.strahl = strahlAus(svg, e.clientX); S.hinweis = ''; neu();
});
document.addEventListener('pointermove', (e) => {
  if (!S.ziehen) return; const svg = document.querySelector('svg[data-strahl]'); if (!svg) return;
  const i = strahlAus(svg, e.clientX); if (i !== S.strahl) { S.strahl = i; neu(); }
});
document.addEventListener('pointerup', () => { S.ziehen = false; });
// Tastatur: Ziffern, Rücktaste, Enter, Pfeile; Richtungen ergänzen eigene Kürzel über TASTEN
const TASTEN = {};
document.addEventListener('keydown', (e) => {
  if (e.target.matches('input, textarea')) return;
  const a = S.ansicht === 'thema' && S.teil === 'ueben' ? aufgabeJetzt() : null;
  if (a && a.art !== 'strahl') {
    if (/^[0-9]$/.test(e.key)) { taste(e.key); e.preventDefault(); return; }
    if (e.key === 'Backspace') { taste('⌫'); e.preventDefault(); return; }
    if (e.key === '-' && kind().klasse >= 7) { taste('−'); return; }
    if (e.key === ',' && kind().klasse >= 7) { taste(','); return; }
  }
  if (a && a.art === 'strahl' && !S.ergebnis && ['ArrowLeft', 'ArrowRight'].includes(e.key)) {
    S.strahl = Math.max(0, Math.min(a.n, (S.strahl ?? 0) + (e.key === 'ArrowRight' ? 1 : -1))); neu(); e.preventDefault(); return;
  }
  if (e.key === 'Enter' && a && !e.target.matches('button, a')) { S.ergebnis ? weiter() : pruefen(); e.preventDefault(); return; }
  const f = TASTEN[e.key]; if (f) { f(e); }
});
// Wischen (horizontal/vertikal); Richtungen belegen WISCH.links/rechts/hoch/runter
const WISCH = {}; let wischStart = null;
document.addEventListener('touchstart', (e) => { if (e.target.closest('svg[data-strahl], .k-keine-geste')) return; wischStart = [e.touches[0].clientX, e.touches[0].clientY]; }, { passive: true });
document.addEventListener('touchend', (e) => {
  if (!wischStart) return; const dx = e.changedTouches[0].clientX - wischStart[0], dy = e.changedTouches[0].clientY - wischStart[1]; wischStart = null;
  if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) (dx < 0 ? WISCH.links : WISCH.rechts)?.();
  else if (Math.abs(dy) > 80 && Math.abs(dy) > Math.abs(dx) * 1.5) (dy < 0 ? WISCH.hoch : WISCH.runter)?.();
});
let fokusVorher = null;
function neu(oben = false) {
  document.documentElement.classList.toggle('dunkel', S.dunkel);
  document.documentElement.dataset.alter = kind().alter >= 12 ? 'gross' : 'klein';
  fokusVorher = document.activeElement?.dataset?.fokus || null;
  zeichne();
  if (oben) window.scrollTo(0, 0);
  const f = fokusVorher && document.querySelector(`[data-fokus="${fokusVorher}"]`); if (f) f.focus({ preventScroll: true });
}
// Für Bilder und Tests: Zustand direkt setzen
window.ENTWURF = { S, DATEN, A, neu, setze(o) { Object.assign(S, o); neu(true); } };
addEventListener('DOMContentLoaded', () => neu());
