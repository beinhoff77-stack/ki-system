# Klassen-Zuordnung prüfen – Vorschlag an Sebastian (D1, Elfte Runde)

Stand: 2026-11-16. Zweig `daten-klassen`. **Nur ein Vorschlag.** Nichts an `themenliste.json`, Generatoren, Datenbank oder App geändert. Umgesetzt wird erst nach deiner Freigabe (D2).

**Wörter in dieser Datei**
- **Klasse** = Jahrgangsstufe am bayerischen Gymnasium (Feld `klasse.gym_by`).
- **Lernbereich** = Kapitel im LehrplanPLUS. Kürzel „M7 2.2“ heißt: Mathematik, Klasse 7, Lernbereich 2.2.
- **Ort** = Stadt auf der Weltkarte (in der Datenbank: Block). **Gebiet** = Kontinent.
- **Quelle** = Seite, auf der der Lehrplantext steht. Alle Seiten am 16.11.2026 abgerufen.

**Wie sicher ist das?**
- Gesichert: Klasse und Lernbereich bei allen Themen mit „bleibt“ oder „ändern“. Der Lehrplantext dazu steht auf der genannten Seite.
- Einschränkung: Die Seiten wurden über ein Abruf-Werkzeug gelesen, das den Text zusammenfasst. Kürzel, Titel und Kernsätze stimmen mit mehreren Quellen überein. Wörtlich nachgeprüft ist nicht jeder Satz.
- Klasse 8: Die Lehrplanseite selbst ließ sich nicht öffnen. Genutzt wurde der Lehrplantext Klasse 8 in einem Dokument des Staatsinstituts (ISB) von 2021. Titel und Inhalte der Lernbereiche stehen dort; Stundenzahlen fehlen.
- „Kein Beleg gefunden“ heißt: In den Lehrplänen Klasse 5 bis 10 stand der Stoff nicht. Das heißt nicht sicher, dass er fehlt.

---

## Tabelle 1 – 16 Themen ohne Lehrplan-Beleg

| Thema | Klasse heute | Klasse laut LehrplanPLUS | Lernbereich (Kürzel und Titel) | Quelle | Vorschlag |
|---|---|---|---|---|---|
| `geometrie.winkel` („Winkelsätze“) | 5 | **Inhalt der Etappen: 5.** Titel und `umfang` (Winkel an Parallelen, Winkelsummen): **7** | M5 2 Geometrische Figuren und Lagebeziehungen (Winkel bis 360° messen, zeichnen, mit Fachbegriffen beschreiben). Winkelsätze: M7 2.2 Winkelbetrachtungen an Figuren (Scheitel-, Neben-, Stufen-, Wechselwinkel, Winkelsumme im Dreieck und Vieleck) | lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik · …/gymnasium/7/mathematik | **bleibt 5.** Titel ändern auf „Mit Winkeln rechnen“, `umfang` auf Klasse-5-Stoff kürzen. Die Etappe „Winkel an einer Geradenkreuzung“ ist Vorgriff auf 7 (als Vertiefung kennzeichnen). Winkelsätze Klasse 7 fehlen als eigener Flug (siehe Entscheidung 1). |
| `geometrie.ortslinien` | 5 | **5** (Kreis, Parallele, Abstand). Mittelsenkrechte als Ortslinie: 7 | M5 2 Geometrische Figuren und Lagebeziehungen (Lage von Punkt, Gerade, Kreis; Abstand, Lot; Punkte mit vorgegebenen Bedingungen bestimmen, Eigenschaft der Kreislinie nutzen). M7 2.1 Achsen- und punktsymmetrische Figuren (Mittelsenkrechte, Winkelhalbierende, Abstandsprobleme) | …/gymnasium/5/mathematik · …/gymnasium/7/mathematik | **bleibt 5.** Die Etappen nutzen nur Kreis und Parallelen, keine Mittelsenkrechte – das passt zu Klasse 5. |
| `zahlen.potenzen_zehner` | 6 | 5 und 6 – **Hauptklasse 6** | M5 3.1 Multiplikation und Division ganzer Zahlen (große Zahlen mit Zehnerpotenzen). M6 1.4 Multiplikation und Division rationaler Zahlen (negative Exponenten, Alltagsgrößen mit Zehnerpotenzen). Vorsilben (Kilo … Nano): kein Beleg gefunden | …/gymnasium/5/mathematik · …/gymnasium/6/mathematik | **bleibt 6.** Die Hälfte der Etappen braucht negative Exponenten. |
| `bruch.dezimal` | 6 | **6** | M6 1.2 Dezimalbrüche (Stellenwerte, Runden, Umwandeln, endlich oder periodisch) | …/gymnasium/6/mathematik | **bleibt 6** |
| `zahlen.intervalle` | 8 | **kein Beleg gefunden** | – (weder in Klasse 7 noch im Lehrplantext Klasse 8; auch die lineare Ungleichung selbst nicht gefunden) | …/gymnasium/7/mathematik · ISB-Dokument Klasse 8 (siehe Quellen) | **vorläufig 8 lassen**, weil es direkt vor `gleichungen.ungleichungen` (8) gebraucht wird. Siehe Entscheidung 4. |
| `funktionen.grundbegriffe` | 8 | **8** | M8 1 Funktion und Term. Definitionsmenge und Nullstellen ausdrücklich in M8 3 Elementare gebrochen-rationale Funktionen | ISB-Dokument Klasse 8 | **bleibt 8** |
| `raum.schraegbilder` | 8 | 8 und 10 – **Hauptklasse 10** | M8 7 Kreis und Zylinder (Schrägbilder von Prismen). M10 5 Fortführung der Raumgeometrie (Schrägbilder und Netze von Pyramide und Kegel). Windschiefe Geraden, Raumkoordinaten: kein Beleg in 5–10 | ISB-Dokument Klasse 8 · …/gymnasium/10/mathematik | **ändern auf 10.** Etappen „windschief“ und „Punkte im Raum mit Koordinaten“ als Vertiefung kennzeichnen. |
| `stochastik.simulation` | 8 | 8 und 10 – **Hauptklasse 10** | M8 5 Laplace-Experimente (Simulieren mit Tabellenkalkulation). M10 2 Zusammengesetzte Zufallsexperimente und stochastische Simulationen (Simulation, Monte-Carlo-Methode) | ISB-Dokument Klasse 8 · …/gymnasium/10/mathematik | **ändern auf 10.** Die Etappen (Zufallsgerät, Simulationsregel, Monte-Carlo) entsprechen M10 2. Siehe Entscheidung 3. |
| `zahlen.wurzeln_basis` | 9 | **9** | M9 1 Quadratwurzeln. Dritte Wurzel: M9 5 Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs („allgemeine Wurzel“) | …/gymnasium/9/mathematik | **bleibt 9** |
| `zahlen.reell` | 9 | **9** | M9 1 Quadratwurzeln (irrationale Zahlen, Wurzeln zusammenfassen, Nenner rational machen, teilweise radizieren) | …/gymnasium/9/mathematik · …/fachlehrplan/lernbereich/217169 | **bleibt 9** |
| `trigo.pythagoras` | 9 | **9** | M9 6 Satz des Pythagoras (Satz und Umkehrung). Längen im Raum: Anwendung in M10 5. Abstand im Koordinatensystem: nicht wörtlich genannt | …/gymnasium/9/mathematik · …/gymnasium/10/mathematik | **bleibt 9** |
| `trigo.rechtwinklig` | 9 | **9** | M9 7.1 Trigonometrie am rechtwinkligen Dreieck | …/gymnasium/9/mathematik | **bleibt 9** |
| `abbildungen.kongruenz` | 7 | **7** (nur Achsen- und Punktspiegelung) | M7 2.1 Achsen- und punktsymmetrische Figuren. Verschiebung, Drehung, Parkett: kein Beleg in 5–10 | …/gymnasium/7/mathematik | **bleibt 7.** Verschiebung, Drehung und Parkett als Vertiefung kennzeichnen. |
| `gleichungen.einfach` | 5 | **5** | M5 1.2 Addition und Subtraktion ganzer Zahlen (a + x = b, x − a = b, a − x = b). M5 3.1 Multiplikation und Division ganzer Zahlen (a · x = b, x : a = b, a : x = b) | …/gymnasium/5/mathematik | **bleibt 5** |
| `gleichungen.linear` | 7 | **7** | M7 3 Lineare Gleichungen und Vertiefung der Prozentrechnung | …/gymnasium/7/mathematik | **bleibt 7** |
| `groessen.indirekt` | 8 | **8** | M8 3 Elementare gebrochen-rationale Funktionen (indirekte Proportionalität y = a/x) | ISB-Dokument Klasse 8 | **bleibt 8** |

**Ergebnis Teil 1:** 13 Themen bleiben, 2 ändern auf 10 (`raum.schraegbilder`, `stochastik.simulation`), 1 ohne Beleg (`zahlen.intervalle`).

**Zum Hinweis im Bericht (B8, Nachtrag):** „Winkelsätze Gym 5 ist wahrscheinlich falsch“ stimmt nur halb. Die Etappen sind Klasse-5-Stoff, nur Titel und Beschreibung versprechen Winkelsätze (Klasse 7). Falsch ist der Titel, nicht die Klasse. Das deckt sich mit `inhalte/pruefung/aufbau/klasse5.json` und `klasse7.json` (Prüfung vom 14.11.).

---

## Tabelle 2 – 13 Orte mit widersprüchlicher Klasse

Regel für die Vorschläge:
- Ort mit **einem** Flug: Der Ort bekommt die Klasse des Flugs. Niemand zieht um.
- Ort mit **mehreren** Flügen: Der abweichende Flug zieht an einen vorhandenen Ort derselben Klasse und desselben Gebiets.
- Klassen der Flüge wie in `themenliste.json`, mit den Änderungen aus Tabelle 1.

| Ort | Klasse heute | Themen mit Klasse (heute) | Vorschlag |
|---|---|---|---|
| Rom (Zahlen) | 5 | Natürliche Zahlen (5) · Ganze Zahlen (5) · Zehnerpotenzen (6) · Rechengesetze (5) · Potenzen (5) | **Rom bleibt 5.** `zahlen.potenzen_zehner` zieht nach **Paris** (6, „Potenzen“). Reihenfolge Rom: natürliche Zahlen (M5 1.1) → ganze Zahlen (M5 1.1/1.2) → Rechengesetze (M5 1.2/3.1/3.2) → Potenzen (M5 3.1). Reihenfolge Paris: Zehnerpotenzen → Potenzen und Potenzgesetze (beide M6 1.4). |
| Vancouver (Geld) | 7 | Indirekte Proportionalität (8) | **Vancouver wird 8.** Kein Umzug. |
| Teheran (Algebra) | 6 | Terme aufstellen (7) | **Teheran wird 7.** Kein Umzug. |
| Delhi (Algebra) | 7 | Lineare Ungleichungen (8) · Lineare Gleichungen (7) · Intervalle (8) | **Delhi wird 8.** `gleichungen.linear` zieht nach **Samarkand** (7, „Terme umformen“). Reihenfolge Delhi: Intervalle → Ungleichungen. Reihenfolge Samarkand: Terme umformen (M7 1.2) → lineare Gleichungen (M7 3). Ortstitel Delhi ändern auf „Lineare Ungleichungen“. |
| Marrakesch (Geometrie) | 6 | Kongruenzabbildungen (7) | **Marrakesch wird 7.** Kein Umzug. |
| Timbuktu (Geometrie) | 7 | Winkel (5) | **Timbuktu wird 5.** Kein Umzug. Der Ortstitel „Winkel“ passt zum Flug „Mit Winkeln rechnen“. |
| Alexandria (Geometrie) | 7 | Kreis und Tangenten (7) · Ortslinien (5) | **Alexandria bleibt 7.** `geometrie.ortslinien` zieht nach **Kairo** (5, „Formen und Grundbegriffe“). Reihenfolge Kairo: Grundbegriffe → Ortslinien (beide M5 2). Ortstitel Alexandria ändern auf „Kreis“. |
| Cusco (Fläche und Raum) | 5 | Körper darstellen (8) | **Cusco wird 8.** Kein Umzug. Im Lernweg nach Buenos Aires (Kreis, M8 7), weil der Zylinder den Kreis braucht. |
| Rio de Janeiro (Fläche und Raum) | 6 | Volumen und Oberfläche (5) | **Rio wird 5.** Kein Umzug. Im Lernweg nach Lima (Flächen, M5 4.2). |
| Brasília (Fläche und Raum) | 7 | Schrägbilder (8, neu 10) | **Brasília wird 10** (bei Klasse 8 laut Entscheidung 3: wird 8). Kein Umzug. Im Lernweg vor Santiago (M10 5: erst Schrägbilder und Netze, dann Volumen). |
| Santiago de Chile (Fläche und Raum) | 9 | Pyramide, Kegel, Kugel (10) | **Santiago wird 10.** Kein Umzug. |
| Adelaide (Daten und Zufall) | 5 | Daten erfassen und darstellen (6) | **Adelaide wird 6.** Kein Umzug. Im Lernweg vor Sydney (Mittelwert, beide M6 3). |
| Darwin (Daten und Zufall) | 10 | Mehrstufige Zufallsexperimente (10) · Simulation (8, neu 10) | **Darwin bleibt 10.** Kein Umzug, wenn Simulation auf 10 geht. Reihenfolge: mehrstufig → Simulation (beide M10 2). Bleibt Simulation bei 8: Simulation zieht nach **Auckland** (8, „Zufall und Laplace“), dort nach Laplace. |

**Ergebnis Teil 2:** 3 Umzüge (Zehnerpotenzen → Paris, lineare Gleichungen → Samarkand, Ortslinien → Kairo), 10 Orte bekommen eine neue Klasse, kein neuer Ort nötig. Danach hat jeder der 13 Orte genau eine Klasse. Geprüft mit `orte.json` und `themenliste.json` (Rechnung siehe Postfach).

---

## Was Sebastian entscheiden muss

1. **Winkelsätze (Klasse 7) fehlen.** Vorschlag: `geometrie.winkel` bleibt Klasse 5 und heißt künftig „Mit Winkeln rechnen“. Für Klasse 7 entsteht ein neuer Flug „Winkelsätze“ (M7 2.2). Offen: Welcher Ort bekommt ihn? Timbuktu wird ja Klasse 5. Vorschlag: Addis Abeba (Klasse 7, „Dreiecke, Vierecke und Konstruktion“), vor der Konstruktion. Sonst ist ein neuer Ort nötig.
2. **Zwei Themen auf Klasse 10:** `raum.schraegbilder` und `stochastik.simulation`. Ja oder nein?
3. **Simulation:** Klasse 10 (Monte-Carlo steht in M10 2) oder Klasse 8 (erstes Simulieren in M8 5)? Vorschlag: 10. Bei 8 zieht der Flug nach Auckland.
4. **Intervalle und lineare Ungleichungen:** Im Lehrplan Gymnasium 5–10 nicht gefunden. Behalten (Klasse 8, als Zusatz) oder ausblenden?
5. **Weniger Umzüge oder bessere Titel:** Bei Orten mit einem Flug ändert sich nur die Ortsklasse. Dadurch liegen manchmal zwei Orte desselben Gebiets in einer Klasse (z. B. Brasília und Santiago in 10, Adelaide und Sydney in 6). Alternative: zusammenlegen, dann bleibt ein Ort leer. Vorschlag: so lassen.
6. **Vertiefung kennzeichnen:** Etappen über dem Lehrplan als Vertiefung markieren (bei Winkel, Kongruenzabbildungen und Schrägbildern)? Dafür ist ein Feld in der App nötig, also ein Wunsch an die App.

## Zusatzfunde (nicht Teil des Auftrags)

- **New York (Klasse 7)** enthält „Zinsen“ (`finanzen.zinsen`). Laut `inhalte/klar/quelle.md` ist das Klasse 6; im Lehrplan steht Zinsrechnung in M6 3 Prozentrechnung, Daten und Diagramme. Das ist ein 14. Widerspruch. Er fehlt in der Zählung, weil das Thema nicht in `themenliste.json` steht. Vorschlag: New York wird 6.
- **4 Themen fehlen in `themenliste.json`**, obwohl sie Orte haben: `zahlen.natuerlich` (Rom), `zahlen.teilbarkeit` (Athen), `terme.umformen` (Samarkand), `finanzen.zinsen` (New York). Für die Lehrplan-Reihenfolge (Spalte `reihenfolge`, Voraussetzung für E-4) sollten sie aufgenommen werden.
- **17 Orte haben Flüge ohne Gymnasium-Klasse.** Bei 9 davon steht daneben ein Flug mit Klasse: Shanghai, Seoul, Tokio, Neumayer-Station III, Wostok-Station, Halley-Station, Lagos, Dakar, Perth. Bei 8 hat kein Flug eine Klasse: San Francisco, Boston, Palmer-Station, Hobart, Suva, Galápagos-Inseln, Tahiti, Honolulu. Dort lässt sich „ein Ort = eine Klasse“ erst prüfen, wenn diese Flüge eine Klasse haben.

## Quellen

- LehrplanPLUS Gymnasium Mathematik 5: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik
- LehrplanPLUS Gymnasium Mathematik 6: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik
- LehrplanPLUS Gymnasium Mathematik 7: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik
- Lehrplantext Gymnasium Mathematik 8 (ISB, „Verbindliche Hinweise zu Schwerpunktsetzungen“, Stand August 2021, linke Spalte = gültiger Lehrplantext): https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Gymnasium/deutsch_englisch_mathe/M_Schwerpunktsetzungen_8.pdf
- LehrplanPLUS Gymnasium Mathematik 9: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/9/mathematik · Lernbereich M9 1: https://www.lehrplanplus.bayern.de/fachlehrplan/lernbereich/217169
- LehrplanPLUS Gymnasium Mathematik 10: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik
- Daten: `inhalte/themenliste.json` (Zweig lernen-app, Commit aea5ee3), `inhalte/pruefung/kinderansicht/orte.json` (Zweig pruefung-kinderansicht), `inhalte/pruefung/aufbau/klasse5–10.json`.
