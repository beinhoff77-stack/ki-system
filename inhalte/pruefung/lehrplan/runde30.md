# Dreißigste Runde (21.11.): Lehrplan-Prüfung – Zuordnungen und Voraussetzungen

Grundlage: Zweig `lernen-app` e0739529 (einschließlich Nachtrag des Gestalters), Datenbank nur gelesen. Quelle LehrplanPLUS Bayern, **abgerufen 21.11.2026** über die Suche auf lehrplanplus.bayern.de (Seitenauszüge, keine Volltextabrufe). Unbelegtes ist als **Annahme** gekennzeichnet.

## 1. Themen ohne Klasse

| Thema | Ergebnis | Beleg / Annahme |
|---|---|---|
| 12 Reinquadratische Gleichungen | **Gym 9 neu**, Lernbereich „M9 2 Quadratische Funktionen“, Reihenfolge 4 (vor 8) | Tatsache: Gym 9 M9 2.1 „Quadratische Funktionen und quadratische Gleichungen“ verlangt das Lösen quadratischer Gleichungen (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/9/mathematik). Annahme: x² = a ist dort der einfachste Fall; der Lehrplan nennt ihn nicht eigens. |
| 40 Graphentransformation | Gym bleibt ohne Klasse | Tatsache: Parameter der Scheitelform in M9 2.1, a·sin(b(x+c))+d in M10 3; allgemeine Transformationen erst Jgst. 11 (Fachprofil Gymnasium Mathematik; Servicematerial https://www.lehrplanplus.bayern.de/serviceinformation/l338447). Das Thema ist allgemein angelegt → nicht Gym 5–10. |
| 77 Umkehrfunktionen | Gym bleibt ohne Klasse | Tatsache: Term der Umkehrfunktion erst Gym 12 M12 4.2 Wurzelfunktion (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/12/mathematik). |
| 13 Wurzelgleichungen | Gym bleibt ohne Klasse | Tatsache: RS 9 (I) LB 7 „lösen Wurzelgleichungen und beachten dabei die Definitionsmenge“ (https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg1). **Annahme:** in Gym 5–10 keine Fundstelle; ein ausdrückliches „nicht“ habe ich nicht gefunden. |
| 4 Formeln umstellen (RS) | RS bleibt ohne Klasse | **Annahme:** keine eigene Kompetenzerwartung in RS 5–10 gefunden; Umstellen kommt in RS 7 LB 6 (Äquivalenzumformungen) und in 101 Prismen und Zylinder (RS 9) vor. |
| 4 Formeln umstellen (Gym) | **Lernbereich berichtigt**: „M8 1 Funktion und Term“ statt „M8 4 Bruchterme …“ | Tatsache: Gym 8 M8 1 „lösen Formeln – insbesondere aus den Naturwissenschaften – nach einer Variablen auf“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik). Reihenfolge Gym 8 (Stelle 10) **nicht** geändert, siehe Vorschlag V1. |
| Stichprobe 7 LGS mit 3 Unbekannten | Gym 9 bestätigt | Tatsache: M9 2.2 „stellen lineare Gleichungssysteme mit drei Unbekannten auf …“ (https://www.lehrplanplus.bayern.de/fachlehrplan/lernbereich/217156). |
| Stichprobe 11 Polynomgleichungen | Gym 10 bestätigt | Tatsache: M10 4 Ganzrationale Funktionen, Nullstellen auch über Substitution (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik); laut Servicematerial ohne Polynomdivision (https://www.lehrplanplus.bayern.de/serviceinformation/l301512). |

Nach der Änderung bekommt ein Gymnasiast Reinquadratische Gleichungen im Plan: `schule.thema_jahrgang(12)` liefert dann `gym_by 9` (Rauchtest a).

## 2. Realschule 7 (20 Themen) und 8 (7 Themen)

- **RS 7 = 20: stimmig.** Alle 8 Lernbereiche von RS 7 (I) sind belegt (https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1). Zwei Auffälligkeiten, nicht geändert:
  - 95 Boxplot (RS 7, Lernbereich „M7 8“) steht nicht im RS-Lehrplan; die Liste nennt es selbst „Annahme Vertiefung“. → Vorschlag V2.
  - 29 Terme umformen (RS 7) enthält Inhalte aus RS 8 LB 4 (Summe mal Summe, Faktorisieren, binomische Formeln). → Vorschlag V3.
- **RS 8 = 7: dünn wegen fehlender Themen, nicht wegen falscher Zuordnung** (https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg1). Ohne App-Thema: LB 1 Vierecke, LB 2 Drehung (46 Kongruenz steht in RS 6), LB 7 Daten und Zufall (Ergebnis/Ereignis, Baumdiagramm, Vierfeldertafel). 61 und 63 bleiben RS 9 (Laplace in RS 9 LB 8). → Vorschlag V4.

## 3. Voraussetzungen

- Vorher: 70 Verbindungen, 7 Themen ganz ohne Eintrag mit Klasse und ohne Kennzeichen. Nachher: **143 Verbindungen (73 neu)**, 7 Themen ausdrücklich **eigenständig**. Jedes Thema mit Klasse hat danach Voraussetzungen oder „eigenständig“ (Rauchtest b).
- **Ablage „eigenständig“ (Nachtrag Gestalter):**
  - Datenbank: neue Spalte **`schule.thema.eigenstaendig`** (`text`, Begründung). Nicht leer heißt: bewusst ohne Voraussetzung. Leer heißt: nicht gekennzeichnet.
  - Themenliste: Feld **`eigenstaendig`** (Text) an 15, 42, 57, 60, 65, 83, 84.
  - Damit das Übersichtsblatt das anzeigen kann, muss die Lese-Schnittstelle die Spalte mitliefern (LM-S). Das ist hier nicht gebaut.
- **Pflichtkette Potenz:** 30 → 102 → 29 (hart) und 102 → 103 (hart), dazu 30 → 103 (hart). Fehlen 102/103, überspringt die Migration diese Zeilen (Prüfung `where exists`).
- **Quelle:** Die Abhängigkeiten sind fachliche **Annahmen**, gestützt auf die Reihenfolge der Lernbereiche im LehrplanPLUS. Ausdrücklich belegt sind nur einzelne: 7 ← 6 (Servicematerial https://www.lehrplanplus.bayern.de/serviceinformation/l298115: LGS 3 greift auf M8 6 zurück), 11 ← 8 (l301512: Jgst. 10 baut auf quadratischen Gleichungen aus Jgst. 9 auf).
- **Selbstprüfung im Rauchtest** (Regeln des Gestalters):
  - b) Kein Thema mit Klasse bleibt ohne Verbindung, außer es ist eigenständig.
  - g) Keine Voraussetzung (hart oder empfohlen) liegt je Schulart in einer späteren Klasse als das Thema.
  - h) Die Themen 100–103 haben je mindestens eine Voraussetzung.
  - Dazu: a) 12 in Gym 9; c) keine Kreise; d) Reihenfolge lückenlos und eindeutig; e) die Kette 30 → 102 → 29 und 102 → 103; f) Lernbereich 4.
  - Alle Regeln sind per Skript auf die Themenliste nachgerechnet und erfüllt.
- Wegen Regel g habe ich fünf zuerst geplante empfohlene Verbindungen weggelassen: 9 ← 96, 47 ← 5, 50 ← 25, 73 ← 46 und 103 ← 31. Die Voraussetzung läge sonst in IB, Gym oder RS eine Klasse später.
- **Geändert wegen Regel g (nur IB):** Die vorhandene harte Verbindung 33 Lineare Funktionen ← 32 Zuordnung und Funktion verstieß gegen die Regel: 32 stand in MYP 4, 33 in MYP 3.
  - Jetzt steht **32 in MYP 3** an Stelle 5, direkt vor 33. MYP 3 und MYP 4 sind neu nummeriert.
  - **Annahme:** Das IB-Framework nennt für die Funktionsschreibweise MYP 4–5. Der Lehrplantext von 32 sagt das jetzt ausdrücklich.
  - Die Alternative wäre, 33 nach MYP 4 hinter 32 zu setzen. Das ist **deine Entscheidung**, falls du es anders willst.
  - Kein Kind ist betroffen.
- **Befund, nicht geändert (alt, nur IB):** Bei 10 ← 37, 26 ← 25 und 92 ← 54 steht die harte Voraussetzung in derselben Klasse weiter hinten. Die Regeln des Gestalters erlauben das, die Reihenfolge ist aber unlogisch. → Vorschlag V5.

## 4. Was den Plan eines Kindes verschieben würde (ohne Namen)

Betroffen sind nur Gymnasium-Kinder: zwei echte (Klasse 5 und Klasse 8) und das Testkind (Klasse 7). Kinder an RS oder IB gibt es nicht; die IB-Änderung (32 nach MYP 3, Reihenfolge MYP 3/4) trifft also niemanden.

1. **Thema 12 bekommt Gym-Klasse 9.** Es liegt bereits auf beiden Routen. Bisher hatte es keine Gym-Klasse, künftig steht es bei Klasse 9. **Annahme:** Ohne Klasse sortierte die App das Thema ans Ende bzw. außerhalb der Klassenlisten. Nicht im Browser geprüft.
2. **Reihenfolge Gym 9 neu nummeriert.** Die Themen 8, 7, 63, 47, 96, 36, 9, 54, 55, 56 und 14 stehen jeweils eine Stelle weiter hinten. Ihre Reihenfolge untereinander bleibt gleich.
3. **Lernbereich von 4** heißt jetzt M8 1 statt M8 4. Die Reihenfolge bleibt gleich. **Annahme:** Gruppiert eine Ansicht nach Lernbereich, wandert das Thema dort in eine andere Gruppe. Für das Kind in Klasse 8 betrifft das die laufende Klasse.
4. **Kein Einfluss** haben die Voraussetzungen und `eigenstaendig`. `lernen.js` sortiert nur nach Klasse und `lehrplan_reihenfolge`. Die Voraussetzungen liest nur `api.schule_lehrplan_lesen` (Liste „braucht“).

## 5. Vorschläge (nicht umgesetzt)

- V1: 4 Formeln umstellen in Gym 8 hinter 32 Zuordnung und Funktion setzen. Das passt zu M8 1, verschiebt aber den Plan des Kindes in Klasse 8.
- V2: 95 Boxplot in RS ohne Klasse lassen oder ausdrücklich als Vertiefung kennzeichnen.
- V3: 29 für RS teilen: RS 7 Zusammenfassen, RS 8 Ausmultiplizieren, Faktorisieren und binomische Formeln.
- V4: Neue Flüge für RS 8: Vierecke, Drehung, Baumdiagramm/Vierfeldertafel.
- V5: IB-Reihenfolge in MYP 2, 3 und 5 an die harten Voraussetzungen 26 ← 25, 92 ← 54 und 10 ← 37 anpassen. Kein IB-Kind ist betroffen.

## 6. Dateien

- `inhalte/themenliste.json`: 12 (Gym 9, Lernbereich, `lehrplan_gym`), Reihenfolge Gym 9 (12 Einträge), 4 (Lernbereich Gym), Feld `eigenstaendig` an 15, 42, 57, 60, 65, 83, 84; 32 nach IB MYP 3 (Klasse, Lernbereich, `lehrplan_ib`), Reihenfolge IB MYP 3 und 4.
- `supabase/migrations/20261121_lehrplan_zuordnung_voraussetzungen.sql`: wiederholt ausführbar, ohne DROP/DELETE, **nicht ausgeführt**. Mit Rauchtest (a–h), der bei Fehlern abbricht. Syntax mit pglast geprüft.
- Selbstprüfung: Reihenfolge je Schulart und Klasse lückenlos und eindeutig. Tests `tests/lernen.test.cjs` 135/135 grün. `tools/inhalt_pruefen.py --alle` zeigt nur dieselben Hinweise wie vorher.

## Anhang: Voraussetzungen je Thema

| Nr | Thema | Gym | RS | IB | direkte Voraussetzungen (Art, Begründung) |
|---|---|---|---|---|---|
| 1 | Einfache Gleichungen | 5 | 6 | 1 | 18 Grundrechenarten und Rechengesetze (hart, vorhanden) |
| 2 | Lineare Gleichungen | 7 | 7 | 2 | 1 Einfache Gleichungen (hart, vorhanden); 28 Terme aufstellen und deuten (hart, Gleichungen bestehen aus Termen mit Variablen); 16 Ganze Zahlen (hart, Lösungen und Umformungen mit negativen Zahlen) |
| 3 | Lineare Ungleichungen | 8 | 7 | 4 | 2 Lineare Gleichungen (hart, vorhanden) |
| 4 | Formeln umstellen | 8 | – | 4 | 2 Lineare Gleichungen (hart, vorhanden); 29 Terme umformen (empfohlen, beim Umstellen werden Terme umgeformt) |
| 5 | Bruch- und Verhältnisgleichungen | 8 | 8 | 4 | 2 Lineare Gleichungen (hart, vorhanden); 31 Bruchterme (hart, vorhanden) |
| 6 | Gleichungssysteme mit 2 Unbekannten | 8 | 9 | 4 | 2 Lineare Gleichungen (hart, vorhanden); 33 Lineare Funktionen (empfohlen, graphisches Lösen über den Schnittpunkt zweier Geraden) |
| 7 | Gleichungssysteme mit 3 Unbekannten | 9 | – | – | 6 Gleichungssysteme mit 2 Unbekannten (hart, vorhanden) |
| 8 | Quadratische Gleichungen (allgemein) | 9 | 9 | 4 | 2 Lineare Gleichungen (hart, vorhanden); 12 Reinquadratische Gleichungen (hart, vorhanden); 29 Terme umformen (hart, vorhanden) |
| 9 | Potenzgleichungen | 9 | 10 | 4 | 20 Wurzeln und reelle Zahlen (hart, vorhanden) |
| 10 | Exponentialgleichungen | 10 | 10 | 5 | 37 Exponential- und Logarithmusfunktionen (hart, vorhanden) |
| 11 | Polynomgleichungen | 10 | – | – | 8 Quadratische Gleichungen (allgemein) (hart, vorhanden); 39 Ganzrationale Funktionen (empfohlen, Nullstellen ganzrationaler Funktionen = Lösungen der Polynomgleichung) |
| 12 | Reinquadratische Gleichungen | 9 | 9 | 4 | 68 Elementare Wurzeln (hart, vorhanden) |
| 13 | Wurzelgleichungen | – | 9 | – | 68 Elementare Wurzeln (hart, vorhanden); 12 Reinquadratische Gleichungen (empfohlen, Quadrieren und Wurzelziehen wie bei x² = a); 8 Quadratische Gleichungen (allgemein) (empfohlen, Wurzelgleichungen führen oft auf quadratische Gleichungen) |
| 14 | Trigonometrische Gleichungen | 9 | 10 | 5 | 56 Allgemeine Trigonometrie (hart, vorhanden) |
| 15 | Natürliche Zahlen | 5 | 5 | 1 | **eigenständig** – Einstieg Klasse 5; setzt nur Grundschulwissen voraus |
| 16 | Ganze Zahlen | 5 | 5 | 2 | 15 Natürliche Zahlen (hart, vorhanden) |
| 17 | Teilbarkeit | 5 | 5 | 1 | 18 Grundrechenarten und Rechengesetze (hart, Teiler und Vielfache beruhen auf Multiplizieren und Dividieren) |
| 18 | Grundrechenarten und Rechengesetze | 5 | 5 | 1 | 15 Natürliche Zahlen (hart, Rechnen im Stellenwertsystem mit natürlichen Zahlen) |
| 19 | Zehnerpotenzen und wissenschaftliche Schreibweise | 6 | 7 | 4 | 67 Potenzen als Schreibweise (hart, Potenzbegriff: Basis und Exponent); 22 Dezimalzahlen (empfohlen, kleine Zahlen als Dezimalzahl und als Zehnerpotenz) |
| 20 | Wurzeln und reelle Zahlen | 9 | 9 | 4 | 68 Elementare Wurzeln (hart, Quadratwurzel als Grundbegriff) |
| 21 | Brüche und Anteile | 6 | 6 | 1 | 18 Grundrechenarten und Rechengesetze (hart, Bruch als Teilen; Kürzen und Erweitern durch Multiplizieren und Dividieren); 17 Teilbarkeit (empfohlen, Kürzen mit gemeinsamen Teilern) |
| 22 | Dezimalzahlen | 6 | 6 | 1 | 21 Brüche und Anteile (hart, Dezimalzahlen als Zehnerbrüche) |
| 23 | Rechnen mit rationalen Zahlen | 6 | 6 | 2 | 21 Brüche und Anteile (hart, vorhanden); 22 Dezimalzahlen (hart, rationale Zahlen auch als Dezimalzahlen); 16 Ganze Zahlen (hart, Vorzeichenregeln der ganzen Zahlen) |
| 24 | Prozent- und Zinsrechnung | 6 | 6 | 1 | 21 Brüche und Anteile (hart, vorhanden); 22 Dezimalzahlen (empfohlen, Prozentsätze als Dezimalzahl) |
| 25 | Größen und Einheiten | 5 | 5 | 2 | 18 Grundrechenarten und Rechengesetze (hart, Umrechnen durch Multiplizieren und Dividieren mit 10, 100, 1000) |
| 26 | Direkte Proportionalität und Dreisatz | 5 | 6 | 2 | 25 Größen und Einheiten (hart, vorhanden) |
| 27 | Verhältnisse und Raten | – | – | 2 | 21 Brüche und Anteile (hart, Verhältnis als Bruch) |
| 28 | Terme aufstellen und deuten | 7 | 6 | 1 | 18 Grundrechenarten und Rechengesetze (hart, Rechenarten und Rechengesetze in Termen) |
| 29 | Terme umformen | 7 | 7 | 3 | 28 Terme aufstellen und deuten (hart, vorhanden); 102 Potenzgesetze (hart, Produkte wie a · a² · a³ brauchen das Potenzgesetz) |
| 30 | Potenzen und negative Exponenten | 6 | 7 | 3 | 18 Grundrechenarten und Rechengesetze (hart, vorhanden); 67 Potenzen als Schreibweise (hart, vorhanden); 21 Brüche und Anteile (hart, negativer Exponent bedeutet Kehrbruch) |
| 31 | Bruchterme | 8 | 8 | 4 | 23 Rechnen mit rationalen Zahlen (hart, vorhanden); 29 Terme umformen (hart, Zähler und Nenner werden als Terme umgeformt) |
| 32 | Zuordnung und Funktion | 8 | 8 | 3 | 28 Terme aufstellen und deuten (hart, vorhanden) |
| 33 | Lineare Funktionen | 8 | 8 | 3 | 2 Lineare Gleichungen (hart, vorhanden); 32 Zuordnung und Funktion (hart, vorhanden) |
| 34 | Gebrochen-rationale Funktionen | 8 | – | 4 | 32 Zuordnung und Funktion (hart, Funktionsbegriff, Definitionsmenge); 93 Indirekte Proportionalität (empfohlen, indirekte Proportionalität führt auf die Hyperbel) |
| 35 | Quadratische Funktionen | 9 | 9 | 4 | 29 Terme umformen (empfohlen, vorhanden); 32 Zuordnung und Funktion (hart, vorhanden); 33 Lineare Funktionen (empfohlen, vorhanden) |
| 36 | Potenzfunktionen | 9 | 10 | 4 | 32 Zuordnung und Funktion (hart, vorhanden); 35 Quadratische Funktionen (empfohlen, Parabel als erste Potenzfunktion) |
| 37 | Exponential- und Logarithmusfunktionen | 10 | 10 | 5 | 30 Potenzen und negative Exponenten (hart, vorhanden); 32 Zuordnung und Funktion (hart, vorhanden); 103 Potenzgesetze mit ganzzahligen Exponenten (empfohlen, Potenzgesetze mit ganzzahligen Exponenten) |
| 38 | Sinus- und Kosinusfunktion | 10 | 10 | 5 | 56 Allgemeine Trigonometrie (hart, vorhanden) |
| 39 | Ganzrationale Funktionen | 10 | – | 5 | 35 Quadratische Funktionen (hart, vorhanden) |
| 40 | Graphentransformation | – | 9 | 5 | 35 Quadratische Funktionen (hart, Parameter der Scheitelform verschieben und strecken die Parabel); 33 Lineare Funktionen (empfohlen, Verschieben von Geraden als einfachster Fall) |
| 41 | Folgen | – | – | 5 | 28 Terme aufstellen und deuten (hart, Term für das n-te Glied) |
| 42 | Grundbegriffe und Figuren | 5 | 5 | 1 | **eigenständig** – Einstieg Geometrie Klasse 5; setzt nur Grundschulwissen voraus |
| 43 | Mit Winkeln rechnen | 5 | 5 | 1 | 42 Grundbegriffe und Figuren (hart, Strahl, Scheitel und Gerade) |
| 44 | Konstruktionen, Kongruenz und Beweise | 7 | 7 | 3 | 43 Mit Winkeln rechnen (hart, Winkel messen und zeichnen); 98 Winkelsätze (empfohlen, Winkelsumme bei Existenz und Konstruktion von Dreiecken); 46 Kongruenzabbildungen (empfohlen, Grundkonstruktionen (Mittelsenkrechte, Lot, Winkelhalbierende)) |
| 45 | Kreis und Tangenten | 7 | 7 | 4 | 42 Grundbegriffe und Figuren (hart, Kreis, Radius, Gerade); 98 Winkelsätze (hart, Satz des Thales wird über die Winkelsumme im Dreieck begründet); 73 Ortslinien und Ortsbereiche (empfohlen, Umkreis und Inkreis über Mittelsenkrechte und Winkelhalbierende) |
| 46 | Kongruenzabbildungen | 7 | 6 | 3 | 42 Grundbegriffe und Figuren (hart, Gerade, Senkrechte, Koordinatensystem) |
| 47 | Ähnlichkeit und Strahlensätze | 9 | 9 | 3 | 46 Kongruenzabbildungen (empfohlen, vorhanden) |
| 48 | Vektoren und Determinanten | – | 7 | – | 42 Grundbegriffe und Figuren (hart, Koordinatensystem); 46 Kongruenzabbildungen (empfohlen, Begriff Kongruenzabbildung) |
| 49 | Matrizen und Abbildungen mit Matrizen | – | 10 | 5 | 48 Vektoren und Determinanten (empfohlen, vorhanden) |
| 50 | Umfang und Flächeninhalt | 5 | 5 | 1 | 42 Grundbegriffe und Figuren (hart, Rechteck, Quadrat und Vielecke) |
| 51 | Kreisberechnungen | 8 | 9 | 3 | 50 Umfang und Flächeninhalt (hart, vorhanden) |
| 52 | Körper darstellen | 8 | 5 | 3 | 42 Grundbegriffe und Figuren (hart, ebene Figuren für Netze und Seitenflächen) |
| 53 | Volumen und Oberfläche | 5 | 6 | 1 | 50 Umfang und Flächeninhalt (hart, vorhanden) |
| 54 | Satz des Pythagoras | 9 | 9 | 3 | 68 Elementare Wurzeln (hart, vorhanden) |
| 55 | Trigonometrie im rechtwinkligen Dreieck | 9 | 9 | 4 | 47 Ähnlichkeit und Strahlensätze (hart, vorhanden); 54 Satz des Pythagoras (empfohlen, fehlende Seiten mit Pythagoras) |
| 56 | Allgemeine Trigonometrie | 9 | 10 | 4 | 55 Trigonometrie im rechtwinkligen Dreieck (hart, vorhanden) |
| 57 | Daten erfassen und darstellen | 6 | 5 | 1 | **eigenständig** – Zählen und Ablesen aus der Grundschule genügen |
| 58 | Mittelwert und Häufigkeiten | 6 | 7 | 2 | 57 Daten erfassen und darstellen (empfohlen, vorhanden); 22 Dezimalzahlen (empfohlen, Mittelwerte sind oft Dezimalzahlen) |
| 59 | Zweidimensionale Daten | – | – | 5 | 57 Daten erfassen und darstellen (hart, Daten erfassen und darstellen); 33 Lineare Funktionen (hart, Trendgerade als lineare Funktion) |
| 60 | Zählen und Kombinatorik | 5 | 5 | 2 | **eigenständig** – systematisches Zählen; setzt nur Grundschulwissen voraus |
| 61 | Zufall und Laplace | 8 | 9 | 2 | 21 Brüche und Anteile (hart, vorhanden) |
| 62 | Mehrstufige Zufallsexperimente | 10 | 10 | 4 | 23 Rechnen mit rationalen Zahlen (hart, vorhanden); 61 Zufall und Laplace (hart, vorhanden) |
| 63 | Verknüpfte Ereignisse | 9 | 9 | 4 | 61 Zufall und Laplace (hart, vorhanden) |
| 64 | Simulation | 10 | 9 | 2 | 61 Zufall und Laplace (hart, Zufallsexperiment und relative Häufigkeit) |
| 65 | Graphentheorie | – | – | 4 | **eigenständig** – Entdecker-Insel mit eigenen Begriffen (Knoten, Kanten) |
| 66 | Lineare Optimierung | – | – | 5 | 3 Lineare Ungleichungen (hart, Bedingungen als lineare Ungleichungen); 33 Lineare Funktionen (hart, Randgeraden zeichnen) |
| 67 | Potenzen als Schreibweise | 5 | 5 | 1 | 18 Grundrechenarten und Rechengesetze (hart, Potenz als wiederholtes Multiplizieren) |
| 68 | Elementare Wurzeln | 9 | 9 | 1 | 67 Potenzen als Schreibweise (hart, Quadratzahlen) |
| 69 | Intervalle | 8 | 7 | 4 | 16 Ganze Zahlen (hart, Zahlengerade mit negativen Zahlen) |
| 70 | Schranken und Genauigkeit | – | – | 5 | 22 Dezimalzahlen (hart, Runden von Dezimalzahlen) |
| 71 | Zinsen | 6 | 7 | 4 | 24 Prozent- und Zinsrechnung (hart, vorhanden) |
| 72 | Zinseszins | – | – | 4 | 67 Potenzen als Schreibweise (hart, vorhanden); 71 Zinsen (empfohlen, vorhanden) |
| 73 | Ortslinien und Ortsbereiche | 5 | 7 | – | 42 Grundbegriffe und Figuren (hart, Kreis, Gerade, Abstand) |
| 74 | Zweireihige Determinanten | – | 7 | – | 48 Vektoren und Determinanten (hart, vorhanden) |
| 75 | Betragsfunktion | – | – | 5 | 32 Zuordnung und Funktion (hart, Funktionsbegriff); 16 Ganze Zahlen (hart, Betrag einer ganzen Zahl) |
| 76 | Reihen | – | – | 5 | 41 Folgen (hart, vorhanden) |
| 77 | Umkehrfunktionen | – | 10 | 5 | 32 Zuordnung und Funktion (hart, vorhanden); 36 Potenzfunktionen (hart, Umkehrfunktion wird an Potenzfunktionen eingeführt) |
| 78 | Parameter und Funktionenscharen | – | 8 | – | 33 Lineare Funktionen (empfohlen, vorhanden) |
| 79 | Standardabweichung | – | – | 5 | 58 Mittelwert und Häufigkeiten (hart, vorhanden); 68 Elementare Wurzeln (empfohlen, vorhanden) |
| 80 | Normalverteilung | – | – | 5 | 79 Standardabweichung (hart, vorhanden) |
| 81 | Stichproben und Aussagekraft | – | 7 | 2 | 57 Daten erfassen und darstellen (hart, Daten erheben und darstellen); 58 Mittelwert und Häufigkeiten (empfohlen, Kenngrößen zum Vergleich von Stichproben) |
| 82 | Bedingte Wahrscheinlichkeit | – | – | 5 | 21 Brüche und Anteile (hart, vorhanden); 23 Rechnen mit rationalen Zahlen (hart, vorhanden); 61 Zufall und Laplace (hart, vorhanden) |
| 83 | Mengen und Venn-Diagramme | – | – | 3 | **eigenständig** – Entdecker-Insel; Mengenbegriff wird hier eingeführt |
| 84 | Aussagenlogik | – | – | 4 | **eigenständig** – Entdecker-Insel; Aussagen und Wahrheitswerte werden hier eingeführt |
| 91 | Schrägbilder und Raumdarstellung | 10 | 8 | 4 | 52 Körper darstellen (hart, vorhanden) |
| 92 | Pyramide, Kegel, Kugel | 10 | 9 | 3 | 51 Kreisberechnungen (hart, vorhanden); 54 Satz des Pythagoras (hart, vorhanden); 101 Prismen und Zylinder (empfohlen, Pyramide und Kegel im Vergleich zu Prisma und Zylinder) |
| 93 | Indirekte Proportionalität | 8 | 7 | 4 | 26 Direkte Proportionalität und Dreisatz (hart, vorhanden) |
| 94 | Vermehrter und verminderter Grundwert | 7 | 7 | 3 | 24 Prozent- und Zinsrechnung (hart, vorhanden) |
| 95 | Median, Quartile, Boxplot | 7 | 7 | 4 | 58 Mittelwert und Häufigkeiten (hart, vorhanden) |
| 96 | Rationale Exponenten und n-te Wurzel | 9 | 10 | 5 | 30 Potenzen und negative Exponenten (hart, vorhanden; Begründung neu: Potenzbegriff und negative Exponenten); 68 Elementare Wurzeln (hart, vorhanden); 103 Potenzgesetze mit ganzzahligen Exponenten (hart, Potenzgesetze werden auf rationale Exponenten erweitert) |
| 97 | Quadratische Terme und Extremwerte | – | 8 | – | 29 Terme umformen (hart, vorhanden) |
| 98 | Winkelsätze | 7 | 7 | 2 | 43 Mit Winkeln rechnen (hart, Winkel messen, Scheitel- und Nebenwinkel) |
| 99 | Flächen von Parallelogramm, Dreieck und Trapez | 6 | 6 | – | 50 Umfang und Flächeninhalt (hart, Flächeninhalt von Rechteck und Quadrat; Zerlegen) |
| 100 | Volumen | 6 | 6 | – | 50 Umfang und Flächeninhalt (hart, Grundfläche des Quaders); 25 Größen und Einheiten (hart, Einheiten umrechnen) |
| 101 | Prismen und Zylinder | 8 | 9 | – | 99 Flächen von Parallelogramm, Dreieck und Trapez (hart, Grundflächen Dreieck, Trapez, Parallelogramm); 100 Volumen (hart, Volumenbegriff und Volumeneinheiten); 51 Kreisberechnungen (hart, Kreisfläche und -umfang für den Zylinder) |
| 102 | Potenzgesetze | 7 | 7 | 3 | 30 Potenzen und negative Exponenten (hart, Potenzbegriff (Basis, Exponent, Hoch 0)); 28 Terme aufstellen und deuten (hart, Terme mit Variablen) |
| 103 | Potenzgesetze mit ganzzahligen Exponenten | 8 | 7 | 4 | 102 Potenzgesetze (hart, Potenzgesetze mit natürlichen Exponenten); 30 Potenzen und negative Exponenten (hart, negative Exponenten als Kehrbruch) |
