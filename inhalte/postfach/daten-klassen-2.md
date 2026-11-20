# Postfach daten-klassen-2 (Vierzehnte Runde)

Neueste Meldung oben.

## 2026-11-16 07:20 – FERTIG (Teil 3 und Abschluss)
**Teil 3 – inhalte/themenliste.json** (keine Themendatei geändert):
- (a) Vier Themen aufgenommen (Angaben aus inhalte/klar/quelle.md, den Themendateien und orte.json): zahlen.natuerlich (15, Rom, Kl. 5, M5 1.1), zahlen.teilbarkeit (17, Athen, Kl. 5),
  terme.umformen (29, Samarkand, Kl. 7, M7 1.2), finanzen.zinsen (71, New York, Kl. 6, M6 3). rs_by/ib_myp dort nicht gesetzt (keine Angabe in den Quellen).
- (b) lehrplan_gym für die 15 belegten der 16 Themen aus dem Vorschlag gefüllt (Kürzel + Titel, z. B. „M9 6 Satz des Pythagoras“). Vorhandene Texte anderer Themen unverändert.
  Leer bleiben: zahlen.intervalle („kein Beleg gefunden“ laut Vorschlag) und zahlen.teilbarkeit (nicht im Vorschlag; vermutlich M5 3.1, nicht wörtlich belegt).
- (c) Neues Feld `reihenfolge` {"gym_by": n} für alle 68 Gymnasium-Themen, nach Lernbereichsnummer des LehrplanPLUS; innerhalb eines Lernbereichs nach Lernlogik bzw. Vorschlag.
  rs_by und ib_myp: nicht gesetzt – die Reihenfolge der Realschul- und IB-Pläne habe ich nicht belegen können.

| Kl. | Reihenfolge (Lernbereich) |
|---|---|
| 5 | 1 zahlen.natuerlich (1.1) · 2 zahlen.ganz (1.1/1.2) · 3 geometrie.grundbegriffe (2) · 4 geometrie.ortslinien (2) · 5 geometrie.winkel (2) · 6 zahlen.rechengesetze (1.2/3.1/3.2) · 7 zahlen.potenzen_basis (3.1) · 8 zahlen.teilbarkeit (3.1*) · 9 stochastik.kombinatorik (3.1*) · 10 gleichungen.einfach (1.2/3.1) · 11 groessen.einheiten (4.1) · 12 groessen.proportional (4.1) · 13 messen.flaechen (4.2) · 14 messen.koerper_berechnung (4.2) |
| 6 | 1 bruch.brueche (1.1) · 2 bruch.dezimal (1.2) · 3 bruch.rechnen (1.3/1.4) · 4 zahlen.potenzen_zehner (1.4) · 5 terme.potenzgesetze (1.4) · 6 bruch.prozent (3) · 7 finanzen.zinsen (3) · 8 daten.darstellen (3) · 9 daten.kennwerte (3) |
| 7 | 1 terme.aufstellen (1.1) · 2 terme.umformen (1.2) · 3 abbildungen.kongruenz (2.1) · 4 geometrie.winkelsaetze (2.2) · 5 gleichungen.linear (3) · 6 bruch.prozent_grundwert (3) · 7 daten.boxplot (4) · 8 geometrie.konstruktion (5) · 9 geometrie.kreis (5) |
| 8 | 1 funktionen.grundbegriffe (1) · 2 funktionen.linear (2) · 3 zahlen.intervalle (–*) · 4 gleichungen.ungleichungen (–*) · 5 groessen.indirekt (3) · 6 funktionen.gebrochen (3) · 7 terme.bruchterme (4) · 8 gleichungen.bruch (4) · 9 gleichungen.formeln (4*) · 10 stochastik.grundbegriffe (5) · 11 gleichungen.lgs2 (6) · 12 messen.kreisberechnung (7) · 13 messen.koerper_darstellung (7) |
| 9 | 1 zahlen.wurzeln_basis (1) · 2 zahlen.reell (1) · 3 funktionen.quadratisch (2.1) · 4 gleichungen.quadratisch (2.1) · 5 gleichungen.lgs3 (2.2*) · 6 stochastik.verknuepft (3) · 7 abbildungen.aehnlichkeit (4) · 8 funktionen.potenz (5) · 9 gleichungen.potenz (5) · 10 zahlen.rationale_exponenten (5) · 11 trigo.pythagoras (6) · 12 trigo.rechtwinklig (7.1) · 13 gleichungen.trig (7) · 14 trigo.allgemein (7*) |
| 10 | 1 funktionen.exponential_log (1) · 2 gleichungen.exponential (1) · 3 stochastik.mehrstufig (2) · 4 stochastik.simulation (2) · 5 funktionen.trig (3) · 6 funktionen.ganzrational (4) · 7 gleichungen.polynom (4) · 8 raum.schraegbilder (5) · 9 raum.pyramide_kegel_kugel (5) |

\* = Annahme, Lernbereich nicht wörtlich belegt: Teilbarkeit und Zählprinzip in M5 3.1 (Grundwissen-Reihenfolge eines Gymnasiums: Primfaktorzerlegung und Zählprinzip direkt vor
Multiplikation ganzer Zahlen); Formeln umstellen in M8 4; Gleichungssysteme mit 3 Unbekannten (Parabel durch drei Punkte) in M9 2.2; allgemeine Trigonometrie im Lernbereich M9 7
(Unterkapitel nicht geprüft); Intervalle und lineare Ungleichungen ohne Beleg in Gym 5–10, gesetzt direkt nach M8 2, weil sie dort graphisch an Geraden gelöst werden.
Befund nebenbei: messen.koerper_berechnung (Kl. 5) enthält laut lehrplan_gym auch „Volumen“ – das steht im LehrplanPLUS in M6 2.2 Volumen, nicht in Klasse 5. Nicht geändert.

Lernbereiche nachgelesen bzw. per Websuche bestätigt: LehrplanPLUS Gymnasium M5–M10 (lehrplanplus.bayern.de/fachlehrplan/gymnasium/<5–10>/mathematik), Klasse 8 zusätzlich
Stoffverteilungsplan Lambacher Schweizer 8 Bayern (M8 2, 4, 6) und ISB-Schwerpunktsetzungen 8 (M8 1, 5, 7); Klasse 9 Lernbereiche 1–7 (mint.lentner.net, St.-Marien-Schulen Regensburg);
Klasse 6 Lambacher Schweizer 6 (M6 1.1–1.3, 2), lehrplanplus Lernbereiche M6 2.2 Volumen und M6 3; Klasse 5 Lambacher Schweizer 5 (M5 1.1–4.2).

**Zusammenfassung der Runde:** Teil 1 neuer Flug geometrie.winkelsaetze (224 Aufgaben), Teil 2 Vertiefungen in 3 Themen, Teil 3 themenliste.json. Je Teil ein Commit auf daten-klassen-2.
`tools/inhalt_pruefen.py` meldet OK für geometrie.winkelsaetze, geometrie.winkel, abbildungen.kongruenz, raum.schraegbilder. Keine Datenbank, kein App-Code, kein Merge.
Für Sebastian zu entscheiden: (1) Überschneidung geometrie.konstruktion (Karten parallelen/winkelsumme/vierecke) mit dem neuen Flug; (2) Annahmen (*) oben bestätigen;
(3) README um einen Abschnitt „Vertiefung“ ergänzen (Auftrag verweist darauf, er fehlt).

## 2026-11-16 06:55 – STATUS Teil 2
Vertiefungen gekennzeichnet (aus bewertung.lernziele_pflicht nach lernziele_vertiefung, je ein Argument `vertiefung=` im Generator):
- geometrie.winkel: kreuzung („Winkel an einer Geradenkreuzung“). In themenliste.json umfang auf Klasse-5-Stoff gekürzt; Titel „Mit Winkeln rechnen“ stand schon dort.
- abbildungen.kongruenz: verschiebung, drehung, parkett.
- raum.schraegbilder: lage (windschief), koordinaten (Punkte im Raum).
Nachweis `python3 -I inhalte/generatoren/_vertiefung_nachweis.py <thema>`: in allen drei Dateien nur inhalt.bewertung geändert, Aufgaben und Lernkarten-Texte gleich. Prüfskript OK.
Hinweis: inhalte/README.md hat (noch) keinen Abschnitt „Vertiefung“, auf den der Auftrag verweist. Ich habe das vorhandene Feld bewertung.lernziele_vertiefung benutzt.
Die Themendateien tragen eine eigene Titelzeile nicht; „offen“ in geometrie.winkel nennt noch die alte Lage („Winkelsätze Kl. 5“) – laut Auftrag nicht geändert.

## 2026-11-16 06:40 – STATUS Teil 1
Neuer Flug `geometrie.winkelsaetze` (thema_id 98, block 80 Addis Abeba, gym_by 7, LehrplanPLUS M7 2.2) fertig:
8 Lernkarten im neuen Muster (einstieg, woerter, Schritte mit Zeichnungen, fehler/fehler_bild, regel), je 18 Übungen (4/6/8), 1 Test, 3 Korrektur, 6 Sicherung = 224 Aufgaben.
Je Lernkarte 2 Stufe-3-Aufgaben nach Prüfungsvorbild und 1 Knobelaufgabe. Prüfskript OK ohne Hinweise. Eintrag in themenliste.json vor geometrie.konstruktion.
Lernkarten: Scheitel-/Nebenwinkel · Stufen-/Wechselwinkel · Parallelität prüfen · Innenwinkelsumme begründen · Außenwinkel · Winkelsumme im Vieleck · Winkel in Figuren · Begründen mit Winkelsätzen.
Offen (Entscheidung Sebastian): geometrie.konstruktion am selben Ort hat schon die Karten „parallelen“, „winkelsumme“, „vierecke“ – Überschneidung. Vorschlag: dort später auf Konstruktion/Kongruenz kürzen oder als Wiederholung lassen.
