/* Erfundene Daten für das Klickmuster „Was wackelt?“ – KEIN echter Lernstand, KEIN echtes Kind.
   Die Felder heißen genau wie die, die schule_lernstand und schule_wackelt_lesen heute schon liefern.
   Neu gerechnet wird daraus nur das, was befund.js aus diesen Feldern ableitet. */
'use strict';

const TAG = (n) => { const d = new Date('2026-11-27T09:00:00+01:00'); d.setDate(d.getDate() - n); return d.toISOString(); };

// Eine falsche Antwort: Aufgabe, was der Nutzer geschrieben hat, was richtig gewesen wäre.
const F = (frage, antwort, loesung, vorTagen) => ({ frage, antwort, loesung, am: TAG(vorTagen) });

const THEMEN = [
  {
    thema_id: 7, titel: 'Negative Zahlen', ort: 'Rom', status: 'zu_besprechen',
    wieder_offen: false, fehler_neu: 2, letzter_fehler_am: TAG(1),
    etappen: [
      { einheit_id: 7, lernziel: 'vorzeichen_mal', titel: 'Minus mal Minus', richtig: 4, falsch: 7, mit_tipp: 3,
        regel: 'Minus mal Minus gibt Plus. Minus mal Plus gibt Minus.',
        fehler_gruende: { vorzeichen: 5, komma: 1 },
        fehler: [F('(−3) · (−4) =', '−12', '12', 1), F('(−5) · 2 =', '10', '−10', 1), F('(−2) · (−2) · (−2) =', '8', '−8', 2), F('(−6) : (−2) =', '−3', '3', 4)] },
      { einheit_id: 7, lernziel: 'vorzeichen_plus', titel: 'Plus und Minus', richtig: 9, falsch: 3, mit_tipp: 1,
        regel: 'Minus heißt umdrehen. Zweimal umdrehen ist wieder geradeaus.',
        fehler_gruende: { vorzeichen: 3 },
        fehler: [F('3 − (−2) =', '1', '5', 2), F('−4 + 7 =', '−11', '3', 3)] },
    ],
  },
  {
    thema_id: 9, titel: 'Brüche', ort: 'Lissabon', status: 'zu_besprechen',
    wieder_offen: true, fehler_neu: 2, letzter_fehler_am: TAG(1),
    etappen: [
      { einheit_id: 9, lernziel: 'bruch_dezimal', titel: 'Bruch zu Dezimalzahl', richtig: 5, falsch: 6, mit_tipp: 4,
        regel: 'Zähler durch Nenner teilen.',
        fehler_gruende: { komma: 4 },
        fehler: [F('3/4 als Dezimalzahl', '0,34', '0,75', 1), F('1/8 als Dezimalzahl', '0,18', '0,125', 1), F('2/5 als Dezimalzahl', '0,25', '0,4', 3)] },
    ],
  },
  {
    thema_id: 12, titel: 'Prozent', ort: 'Kairo', status: 'zu_besprechen',
    wieder_offen: false, fehler_neu: 0, letzter_fehler_am: TAG(6),
    etappen: [
      { einheit_id: 12, lernziel: 'prozent_von', titel: 'Prozent von einer Zahl', richtig: 3, falsch: 4, mit_tipp: 2,
        regel: 'Prozent heißt von hundert.',
        fehler_gruende: { komma: 2 },
        fehler: [F('20 % von 80 =', '1,6', '16', 6), F('5 % von 200 =', '1', '10', 7)] },
      { einheit_id: 12, lernziel: 'prozent_grund', titel: 'Grundwert suchen', richtig: 2, falsch: 2, mit_tipp: 0,
        regel: 'Vom Anteil auf das Ganze zurückrechnen.',
        fehler_gruende: {},
        fehler: [F('12 sind 25 %. Wie groß ist das Ganze?', '3', '48', 7), F('9 sind 30 %. Wie groß ist das Ganze?', '2,7', '30', 8)] },
    ],
  },
  {
    thema_id: 91, titel: 'Kürzen', ort: 'Lissabon', status: 'beobachten',
    wieder_offen: false, fehler_neu: 0, letzter_fehler_am: TAG(2),
    etappen: [
      { einheit_id: 9, lernziel: 'bruch_kuerzen', titel: 'Kürzen', richtig: 6, falsch: 5, mit_tipp: 1,
        regel: 'Zähler und Nenner durch dieselbe Zahl teilen.',
        fehler_gruende: { vertauscht: 3 },
        fehler: [F('12/18 gekürzt', '3/2', '2/3', 2), F('15/20 gekürzt', '4/3', '3/4', 4)] },
    ],
  },
  {
    thema_id: 92, titel: 'Brüche addieren', ort: 'Lissabon', status: 'besprochen', besprochen_am: TAG(2),
    wieder_offen: false, fehler_neu: 0, letzter_fehler_am: TAG(3),
    etappen: [
      { einheit_id: 9, lernziel: 'bruch_plus', titel: 'Brüche addieren', richtig: 8, falsch: 4, mit_tipp: 2,
        regel: 'Erst gleichnamig machen, dann die Zähler addieren.',
        fehler_gruende: { vertauscht: 2 },
        fehler: [F('1/2 + 1/3 =', '2/5', '5/6', 3)] },
    ],
  },
];

// Woche und Lerntage wie heute von schule_lernstand geliefert
const WOCHE = { aufgaben: 46, richtig: 31, mit_tipp: 7, lerntage: 4 };

// Zahl aller Etappen mit Stand (für den zugeklappten Teil unten)
const ETAPPEN_GESAMT = 23;
