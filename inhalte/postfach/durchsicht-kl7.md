# Postfach durchsicht-kl7 (Neunzehnte Runde, Teil A, Klasse 7)

Neueste Meldung oben.

## 2026-11-17 – FERTIG: Abschlussbericht Neunzehnte Runde, Teil A, Klasse 7

Zweig durchsicht-kl7 (von lernen-app 5a982a2; lernen-app c976669 mit dem berichtigten Bildausschnitt der Winkelhalbierenden vor abbildungen.kongruenz hereingeholt). Neun Themen, je ein Commit. Kein Merge.

**So bin ich vorgegangen (Tatsache).** Für jedes Thema habe ich alle Lernkarten ganz und alle Übungen (Pool uebung) gelesen, dazu Test, Korrektur und Sicherung (bei winkelsaetze, konstruktion und kreis nur überflogen). Jede Lösung mit Rechenausdruck rechnet das Prüfskript nach, jede neue Auswahl-Aufgabe habe ich von Hand nachgerechnet.
Den LehrplanPLUS M7 habe ich selbst gelesen (lehrplanplus.bayern.de, M7 1–5).
Die Änderungen stehen je Generator im Abschnitt „DURCHSICHT“ (Werkzeug inhalte/generatoren/_durchsicht_kl7.py). Sie werden nach allen früheren Runden auf die fertige Datei angewendet.
Nachweis je Thema: `python3 -I inhalte/generatoren/_durchsicht_nachweis.py <thema>`. Er bestätigt für alle 9 Themen: Alles außer den gemeldeten Stellen ist Zeichen für Zeichen gleich wie auf lernen-app, und jede Lernkarte hat weiter mindestens 3 Übungen je Stufe. `tools/inhalt_pruefen.py`: OK für alle 9.
Die Geradengleichungen in mittelsenkrechte, winkelhalbierende und planfigur (Prüf-Befund) habe ich direkt in den Texten der Achtzehnten Runde berichtigt; der Nachweis zeigt genau diese Aufgaben als „ersetzt“ bzw. „berichtigt“.

### (1) Urteil je Thema (Noten 1–5: Thema passt? · Erklärungen · Stufen)
Meinung, begründet:
- **terme.aufstellen** – Thema 1 (deckt M7 1.1 inkl. Tabellenkalkulation), Erklärungen 2 (Tabellenkalkulation fehlte), Stufen 2 (sachsituation S2 war Beispiel mit anderen Zahlen; deuten S3 teils Übersetzen).
- **terme.umformen** – Thema 2 (M7 1.2 ohne „Potenzen von Potenzen“; Potenzgesetze stehen in terme.potenzgesetze Kl. 6), Erklärungen 2 (klar, je Karte Beispiel mit Bild), Stufen 4 → 2 (Stufe 3 war meist Beispiel in Einkleidung oder dreimal derselbe Fehler-Typ; keine Zehnte Runde).
- **abbildungen.kongruenz** – Thema 2 (M7 2.1 vollständig seit Achtzehnter Runde; Verschiebung, Drehung, Parkett als Vertiefung; parkett nutzt Innenwinkel regelmäßiger Vielecke vor geometrie.winkelsaetze), Erklärungen 2 (Spiegeln an y = x und Drehsymmetrie fehlten in den Karten – ergänzt), Stufen 2.
- **geometrie.winkelsaetze** – Thema 1 (M7 2.2 vollständig, Außenwinkel als Vertiefung), Erklärungen 1 (nach zwei Prüfungen überarbeitet, jeder Schritt mit Bild), Stufen 2 (zwei Karten mit gleichem Typ in Stufe 2 und 3).
- **gleichungen.linear** – Thema 1 (M7 3 Gleichungen vollständig; Prozent-Teil steckt in bruch.prozent_grundwert), Erklärungen 2 (Waage gut; Stufe 1 der Karte waage ist leichter als ihr Beispiel), Stufen 2 (Stufe 3 bei klammern war vor allem „längere Rechnung“).
- **bruch.prozent_grundwert** – Thema 2 (M7 3 „komplexere Prozentaufgaben“; Grundlagen aus Kl. 6 werden wiederholt), Erklärungen 1 (durchgehende Situation, Fehler mit Zahl gedeutet), Stufen 3 → 2 (Stufe 2 war in vermehrt/prozentsatz oft Stufe 1 mit krummeren Zahlen).
- **daten.boxplot** – Thema 1 (M7 4 vollständig, Boxplots mit Zeichnung seit der Zehnten Runde), Erklärungen 2 (klar; Quartil-Verfahren weicht teils von Schulbüchern ab, steht unter „offen“), Stufen 4 → 2 (Stufen unterschieden sich oft nur in der Länge der Datenliste).
- **geometrie.konstruktion** – Thema 3 (M7 5 abgedeckt; die Karten parallelen und winkelsumme überschneiden sich stark mit geometrie.winkelsaetze; satz_kehrsatz nutzt den Satz des Thales aus geometrie.kreis, das danach kommt), Erklärungen 2, Stufen 2.
- **geometrie.kreis** – Thema 2 (M7 5: Thales, Umkehrung, Tangente; Umkreis/Inkreis nennt der Lehrplan nur als Beispiel für Geometriesoftware), Erklärungen 2, Stufen 3 → 2 (Radius = halbe Strecke stand in Stufe 2, „Liegt C auf dem Kreis?“ in Stufe 3).

### (2) Stufen je Lernkarte (vorher → nachher)

**terme.aufstellen**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| struktur | S1 Termart einfacher Terme; S2 Punkt-vor-Strich-Fallen, Term zu Beschreibung finden; S3 verschachtelte Beschreibung, Tabellenformel prüfen, Klammer setzen | unverändert |
| termwert | S1 lineare Terme einsetzen; S2 Quadrat/zwei Variablen/Wertetabelle; S3 rückwärts (z gesucht), Definitionslücke, Tabellenformel, kleinsten Wert suchen | unverändert (Karte: Schritt Tabellenkalkulation) |
| uebersetzen | S1 Wortterm direkt; S2 Klammer/Differenz-Reihenfolge, Zahlenrätsel; S3 zusammenfassen, rückwärts, „passt NICHT“, Rätsel begründen | unverändert |
| sachsituation | vorher: S1 und S2 gleich (Grundgebühr + Preis pro Einheit) → nachher: S1 Grundgebühr + pro Einheit; S2 zwei Bezüge, Rabatt, Einheitenwechsel, Vergleich; S3 Rest-Term, Deutung, Weg um Garten | 5 umgestuft, 2 neu |
| muster | S1 Folge fortsetzen; S2 Term aus Tabelle/Bild; S3 große n, rückwärts, quadratische Folge, Vergleich zweier Folgen | unverändert |
| deuten | vorher: S3 zur Hälfte „Übersetzung prüfen“ → nachher: S1 Bedeutung einer Zahl; S2 Bedeutung einer Rechnung/eines Werts; S3 Teilterme deuten, Tarifvergleich deuten, Term zur veränderten Situation, Gegenbeispiel | 2 ersetzt |
**terme.umformen**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| zusammenfassen | vorher S3 = S1 in Einkleidung + 2× derselbe Fehler → nachher S1 zusammenfassen; S2 mit x², Einkleidung; S3 rückwärts (Term T), Dreiecksseite aus Umfang, gleichartig erkennen, Term mit Ergebnis 5x | 2 umgestuft, 1 ersetzt, 3 neu |
| produkte | vorher S3 = Rechteck-Fläche + 3× „18x statt 18x²“ → nachher S1 zwei Faktoren; S2 Vorzeichen, drei Faktoren, Fläche; S3 Volumen (a³), fehlender Faktor, Vorzeichen bei drei Minus, Verdopplung der Seiten | 1 umgestuft, 2 ersetzt, 2 neu |
| minusklammer | vorher S3 = S1-Auswahl + Klammer mit Minusfaktor → nachher S1 eine Minusklammer; S2 zwei Klammern, Minusfaktor; S3 Fehler finden, verschachtelte Klammer, Sachsituation Kasse, Lücke rückwärts | 4 umgestuft, 4 neu |
| ausmultiplizieren | vorher S3 = Einkleidung + zweischrittige Vereinfachung → nachher S1 Zahl vor Klammer; S2 x vor Klammer, negative Faktoren, zwei Klammern; S3 Flächenzuwachs unabhängig von x, Faktor rückwärts, Fehler finden, Parameter a | 4 umgestuft, 4 neu |
| summe_mal_summe | vorher S3 = 3× Garten-Einkleidung → nachher S1 (x + a)(x + b); S2 Minus, Faktoren vor x, Garten; S3 Flächenänderung als Term, fehlende Zahl rückwärts, Anzahl der Produkte, Fehler finden | 3 umgestuft, 3 neu |
| ausklammern | vorher S3 = 3× „nicht vollständig“ + S2-Aufgabe → nachher S1 Zahl ausklammern; S2 x ausklammern; S3 unvollständig erkennen, zwei Variablen, −4 ausklammern, Länge aus Fläche | 1 umgestuft, 2 ersetzt, 1 neu |
| aequivalenz | vorher S1 nur Termwerte, S2 = S1 (ausmultiplizieren erkennen), S3 zweimal (x + a)² → nachher S1 einsetzen und vergleichen, ausmultiplizieren erkennen; S2 zwei von drei Termen, Gegenbeispiel wählen; S3 Fehlschluss aus einem Beispiel, Parameter a, (x + 2)² | 3 umgestuft, 1 ersetzt, 4 neu |
| binomisch | vorher S3 zweimal „ergänze x² + bx + □“ → nachher S1 Formel anwenden; S2 mit Faktor vor x, 3. Formel; S3 geschickt rechnen (51², 49 · 51), Fehler finden, ergänzen auch vorne | 1 ersetzt, 1 neu |
**abbildungen.kongruenz**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| achsenspiegelung | S1 an den Achsen; S2 an Parallelen zu den Achsen, an der Winkelhalbierenden; S3 Achse rückwärts, Achse aus Raute, zweite Spiegelung, Verkettung, Parameter x (vorher: eine S3-Aufgabe wie S2) | 1 umgestuft, Karte |
| punktspiegelung | S1 am Ursprung; S2 an beliebigem Z; S3 Zentrum rückwärts, vierte Ecke eines Parallelogramms, Verkettung (vorher: zwei S3 wie S2) | 2 umgestuft |
| mittelsenkrechte | S1 Mitte, Schnitt mit Achse, Eigenschaft; S2 Lot, Abstand, Abstandsproblem an der Straße; S3 drei Orte, schräge Strecke, Anzahl Punkte, Lot auf Winkelhalbierende | Geradengleichungen durch Beschreibungen ersetzt |
| winkelhalbierende | S1 halbieren, gleich weit; S2 Ganzes aus Teil, Nebenwinkel, Punkte gleich weit von zwei Geraden; S3 Abstandsproblem, Begründen, Anzahl, Ecke mit gegebener Höhe | Geradengleichungen durch Beschreibungen ersetzt |
| verschiebung (Vertiefung) | S1 Pfeil anwenden; S2 Pfeil bestimmen, zwei Pfeile nacheinander; S3 Ersatzpfeil, Pfeil rückwärts, „gehört NICHT“, Quadrat verschieben (vorher: dreimal „erst …, dann …“ in S3) | 3 umgestuft |
| drehung (Vertiefung) | S1 um O 90°/180°; S2 270°, Uhrzeigersinn, Winkel bestimmen; S3 um anderes Zentrum, rückwärts, Fehler finden, Verkettung | unverändert |
| symmetrie | S1 Achsen zählen; S2 Buchstaben, Punktsymmetrie, kleinster Drehwinkel; S3 Eigenschaften kombinieren, Gegenbeispiel, Drehwinkel „NICHT“, zusammengesetzte Figur | Karte (Drehsymmetrie) |
| vierecke_ordnen | S1 Beschreibung → Viereck, wahre Aussage; S2 falsche Aussage, Bild erkennen, Achsen-Lage; S3 Gegenbeispiel, Schnittmenge zweier Vierecksarten, Eigenschaft nur bei einem | Lösungsweg und Fehler-Satz berichtigt |
| parkett (Vertiefung) | S1 Winkel an einer Ecke addieren; S2 Lücke berechnen, Innenwinkel aus Anzahl; S3 gemischte Ecken, Ecken aus Innenwinkel, Begründen | unverändert |
| eigenschaften | S1 Aussagen über Kongruenzabbildungen; S2 Abbildung im Bild erkennen, Umlaufsinn, Fläche; S3 Verkettungen, Umlaufsinn umkehren, Schnittpunkt mit Achse (vorher: dreimal „Welche Abbildung?“ wie S2) | 3 umgestuft |
**geometrie.winkelsaetze**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| scheitel_neben | S1 ein Nebenwinkel/Scheitelwinkel; S2 Lage im Bild, drei Geraden, „um 100° größer“; S3 Verhältnisse, Begründen, Summen rückwärts | unverändert |
| stufen_wechsel | vorher S3 dreimal „Nebenwinkel + Stufenwinkel“ wie S2 → nachher S1 Stufen-/Wechselwinkel direkt; S2 mit Nebenwinkel, Namen; S3 Rampe, Dreieck zwischen Parallelen, Zickzack-Weg, Verhältnis | 3 umgestuft |
| parallel_pruefen | S1 zwei gleich große Winkel?; S2 Lage beachten, Drehwinkel; S3 Begründung wählen, Schnittwinkel außerhalb, Senkrechte, welche von drei Geraden parallel (vorher dreimal „a ∥ b ∥ c“) | 2 umgestuft |
| innenwinkelsumme | S1 dritter Winkel; S2 gleichschenklig ohne Fachwort, Existenz, Beweisschritt; S3 größter Winkel ≥ 60°, Beweis-Rechnung, Fehlschluss, Verhältnis, Differenz | unverändert |
| aussenwinkel (Vertiefung) | S1 Außenwinkel aus Innenwinkeln; S2 rückwärts; S3 zwei Außenwinkel, Begründen, Verhältnis, Thaleskreis-Vorgriff | unverändert |
| vieleck | S1 vierter Winkel, Winkelsumme; S2 fehlender Winkel im n-Eck, regelmäßig; S3 Ecken aus Summe/Innenwinkel rückwärts, Begründen, Gleichung ohne x | unverändert |
| figuren | S1 ein Winkelsatz in einer Figur; S2 zwei Sätze kombiniert; S3 Hilfslinie, Zickzack, Spiegel, Diagonale im Parallelogramm | unverändert |
| beweisen | S1 passenden Satz nennen; S2 Beweiskette, Fundamentalsatz/abgeleitet; S3 Kärtchen ordnen, Begründen, Zirkelschluss, Messung vs. Beweis | unverändert |
**gleichungen.linear**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| waage | S1 ein Schritt (x ± a); S2 zwei Schritte, Dezimalzahlen, Umformung benennen; S3 Brüche als Koeffizient, Lücke so füllen, dass L = {−4}, Fehler „durch x teilen“ | unverändert |
| beide_seiten | S1/S2 x auf beiden Seiten (S2 mit negativen Zahlen, Dezimalzahlen); S3 erst zusammenfassen, Bruchlösung, Lücke rückwärts, Waage mit Kugeln/Würfeln | 2 umgestuft |
| klammern | vorher S3 = fünfmal „zwei Klammern auflösen“ → nachher S1 eine Klammer; S2 Minus vor der Klammer, zwei Klammern; S3 Fehler finden, Lücke für gegebene Lösung, Dreieck mit Umfang, Produkt (x + 3)(x − 1) | 3 umgestuft, 3 neu |
| probe | S1 Lösung prüfen; S2 Fehlerzeile finden, Probe-Schreibweise; S3 mal 0, falsches Teilen, Lücke, Quadrieren ist keine Äquivalenzumformung | 1 umgestuft |
| sonderfaelle | S1 Anzahl der Lösungen; S2 Lösungsmenge, Lücke für L = ℚ; S3 Lücke für L = { }, Grundmenge ℕ, Parameter a, Tarif deuten | 2 umgestuft |
| sach | S1 Umfang, Zahlenrätsel, Gleichung wählen; S2 Alter, Pfand, Sparen, Kino, Fünfeck, Seil; S3 rückwärts, Lösung deuten, Tarif, Theater, Gehege, Alter in 12 Jahren, Züge, Kanister (vorher fünfmal „Lena/Tom“ in S2, je zweimal derselbe Typ in S3) | 4 ersetzt |
**bruch.prozent_grundwert**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| faktor | S1 Faktor zu ±p %; S2 rückwärts Faktor → Prozent, „auf 85 %“; S3 über 100 %, Fehler finden, Gleichung zu „20 % weniger“, Umkehrfaktor | 2 umgestuft |
| vermehrt | vorher S1 = S2 → nachher S1 Grundwert · Faktor; S2 nur die Erhöhung/Steuer gesucht, Einkleidungen; S3 Faktor und feste Zulage, Term deuten, Rechnung mit Arbeitsstunden, aus Zinsen zurück, Aufschlag rückwärts | 4 umgestuft, 2 neu |
| vermindert | vorher S3 = viermal Rabatt + Skonto → nachher S1 Rabatt; S2 krumme Sätze, Fehler „nur Rabatt“, Rabatt + Skonto; S3 aus Ersparnis zurück, zwei Angebote vergleichen, Diagramm, „insgesamt halb“, zwei Jahre | 5 umgestuft, 2 neu |
| zurueck | S1 runde Faktoren; S2 Mehrwertsteuer, krumme Faktoren; S3 Anteil → Gesamtzahl, Steueranteil, falsches Rückwärtsrechnen, zwei Änderungen rückwärts | 2 umgestuft |
| prozentsatz | vorher S2 = S1 mit krummeren Zahlen → nachher S1 alt → neu; S2 nur Änderung gegeben, Anteil gleich lassen; S3 Fehler finden, zurück auf alten Wert, weniger/mehr als, Prozent vs. Prozentpunkt | 3 umgestuft, 2 neu |
| mehrfach | S1 zwei Faktoren; S2 Gesamtänderung, Mehrwertsteuer nach Rabatt; S3 rückwärts, Zinseszins, Ausgleich, Parameter p | unverändert |
| argumente | S1 passende Rechnung wählen; S2 Aussagen prüfen, Werbung, Grundwertwechsel, Zeitungsmeldung; S3 ±50 %, Prozentpunkte, Anteile ohne Gesamtzahl, Angebote vergleichen (vorher sechsmal dieselbe Frage in S2) | 2 ersetzt |
**daten.boxplot**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| median | vorher S1/S2/S3 = kurze/mittlere/lange Liste → nachher S1 Median einer Liste; S2 lange Liste, Anzahl unter dem Median, x aus Median, neuer Wert kommt dazu; S3 Häufigkeitstabelle, Diagramm, Prozentanteile, Ausreißer ändern, Mindestwert | 5 umgestuft, 1 neu |
| kennwerte | vorher S2 = S1 (Modalwert/Spannweite bestimmen) → nachher S1 Modalwert, Spannweite; S2 Mittelwert berechnen, Summe aus Mittelwert, Verschiebung; S3 fehlender Wert, gewichtetes Mittel aus Prozenten, Tabellenformel, nötiges Testergebnis | 6 umgestuft |
| mittel_median | S1 Mittelwert berechnen; S2 Unterschied Mittelwert/Median, passenden Kennwert wählen; S3 Gehälter beurteilen, gewichtete Mittel, Ausreißer entfernen, Wert passend ändern | 2 umgestuft |
| quartile | vorher S3 = lange Listen → nachher S1 geordnete Liste; S2 ungeordnet, lange Listen, Quartilsabstand; S3 Anzahl in der Box, x aus Q₁, Anzahl unter Q₁, Wirkung einer Änderung, Verschiebung aller Werte | 6 umgestuft, 3 neu |
| boxplot | S1 Kennwert ablesen; S2 Anteile ablesen; S3 passenden Boxplot zu Daten, Anzahlen aus Anteilen, Aussage NICHT, Daten zu Boxplot | unverändert |
| vergleichen | vorher S1 = S2, S3 = S2 → nachher S1 eine Aussage zu zwei Boxplots; S2 Streuung, Gesamtvergleich, Hälfte über einem Wert; S3 Aussage NICHT, Anzahlen in zwei Klassen, gleicher Median ≠ gleiche Verteilung, Quartilsabstände | 4 umgestuft |
**geometrie.konstruktion**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| parallelen | S1 Stufen-/Wechselwinkel; S2 mit Nebenwinkel, Beziehung benennen, Parallelität prüfen; S3 Gleichung mit x, Fehlaussagen, Zickzack, Dreieck zwischen Parallelen | unverändert (Überschneidung mit winkelsaetze gemeldet) |
| winkelsumme | S1 dritter Winkel; S2 rechtwinklig, Außenwinkel, Beweisschritt; S3 Vielfache, Fehler finden, größter Winkel, Pentagramm | unverändert |
| gleichschenklig | S1 Basiswinkel aus Spitze; S2 rückwärts, zwei Fälle; S3 Außenwinkel, Kreis, gleichseitig + gleichschenklig, zwei mögliche Spitzenwinkel | unverändert |
| kongruenzsatz | S1 WSW erkennen; S2 alle Sätze, WWW; S3 SsW-Anzahl (mit Zeichnung), Kongruenz zweier Dreiecke entscheiden, Drachen | unverändert |
| konstruierbar | S1 Dreiecksungleichung; S2 Winkel, Mindest-/Höchstlänge, Anzahl ganzzahliger Längen; S3 Anzahl (zwei Fälle), Abstandsprobleme, Umfang | 2 umgestuft |
| planfigur | S1 Radius, Parallele, erster Schritt, Bezeichnungen; S2 C im Koordinatensystem, fehlender Schritt, Höhen; S3 Anzahl Punkte C, stumpfer Winkel, Beschreibung wählen, gleichschenklig | Lösungswege ohne Geradengleichungen |
| vierecke | vorher S2 = viermal „360° − drei Winkel“ → nachher S1 Parallelogramm, Viereck; S2 Drachen, Trapez, Raute-Diagonale; S3 Treppengeländer, Diagonalen, Folge, Trapez rückwärts | 4 umgestuft |
| satz_kehrsatz | S1 Kehrsatz bilden; S2 Kehrsatz prüfen, Gegenbeispiel, Fehlschluss; S3 Kehrsatz zum Thalessatz, Beweisschritte, Drachen-Gegenbeispiel, Beispiele ≠ Beweis (vorher zweimal „Widerlege“ in S3 wie in S2, eine S1-Frage doppelt) | 2 umgestuft, 1 ersetzt |
**geometrie.kreis**

| Lernkarte | Worin sich die Stufen unterscheiden (vorher → nachher) | Änderung |
|---|---|---|
| thales | vorher S2 viermal „Radius = halbe Strecke“ → nachher S1 γ = 90°, dritter Winkel, Radius; S2 rückwärts, Fenster, MC, Koordinaten; S3 Mittelpunktswinkel, Verhältnis, Geodreieck-Nägel, größte Höhe, Flächengleichheit, Rechteck im Kreis | 3 umgestuft |
| umkehrung | vorher S2 sechsmal Radius, S3 viermal Winkelsumme prüfen → nachher S1 Mittelpunkt, Radius; S2 Radius, Hypotenuse, Punkt prüfen, liegt C auf dem Kreis; S3 Begründung im Koordinatensystem, MC, C innerhalb, Gleichung mit x | 6 umgestuft |
| beweis | S1 Vermutung/Beweis; S2 Beweisschritte begründen; S3 Kärtchen ordnen, Mittelpunktswinkel, Gegenbeispiel | unverändert |
| lage | S1 Passante/Tangente aus d und r; S2 Durchmesser statt Radius, Bereich für Sekante; S3 Lage im Koordinatensystem, Abstand definieren, Punkte mit Abstand, zwei Kreise | Geradengleichungen ersetzt (6) |
| tangente | S1 halber Winkel, 90°, gleiche Abschnitte; S2 Winkel im Drachenviereck MBPB', Verlauf der Tangente; S3 Dreieck MBP, Thaleskreis-Begründung, Abstand = Radius, Riemen | 1 ersetzt |
| umkreis_inkreis | S1 welche Linien, wovon gleich weit; S2 Lage des Umkreismittelpunkts, ∠BIC; S3 ∠BIC rückwärts, Funkmast, Spielplatz, Umkreismittelpunkt auf [AB] | 2 umgestuft |

### (3) Zahlen
| Thema | umgestuft | berichtigt | ersetzt | neu | Lernkarten verbessert |
|---|---|---|---|---|---|
| terme.aufstellen | 5 | 0 | 2 | 2 | 1 (termwert) |
| terme.umformen | 18 | 0 | 7 | 22 | 0 |
| abbildungen.kongruenz | 9 | 15 | 15 | 0 | 3 (achsenspiegelung, symmetrie, vierecke_ordnen) |
| geometrie.winkelsaetze | 5 | 0 | 0 | 0 | 0 |
| gleichungen.linear | 8 | 0 | 4 | 3 | 0 |
| bruch.prozent_grundwert | 16 | 0 | 2 | 6 | 0 |
| daten.boxplot | 23 | 0 | 0 | 4 | 0 |
| geometrie.konstruktion | 8 | 9 | 1 | 0 | 0 |
| geometrie.kreis | 11 | 1 | 7 | 0 | 0 |
| **Summe** | **103** | **25** | **38** | **37** | **4** |

Geänderte Lernkarten (vorher → nachher):
- terme.aufstellen / termwert: Aufgaben mit Tabellen-Formeln (=A2*(A1+4)-A1), die Karte zeigte keine → neuer Schritt „x steht in Zelle A1, der Term heißt =3*A1+5 (* heißt mal)“.
- abbildungen.kongruenz / achsenspiegelung: Aufgaben spiegeln an y = x, die Karte zeigte nur senkrechte Achsen → neuer Schritt mit Bild „x und y tauschen die Plätze“.
- abbildungen.kongruenz / symmetrie: Aufgaben fragen den kleinsten Drehwinkel (360° : n), die Karte erklärte Drehsymmetrie nicht → neuer Schritt mit Sechseck-Bild und Wort „drehsymmetrisch“.
- abbildungen.kongruenz / vierecke_ordnen: Fehler-Satz „Wie bei Fliesen zählt die Richtung des Satzes“ war unklar (Prüf-Befund) → „Nur umgekehrt stimmt es: Jedes Quadrat ist eine Raute.“

### (4) Liste „ersetzt“ (alte Fragetexte bitte sperren)
- **terme.aufstellen**:
  - deuten / uebung / Stufe 3: „Jemand übersetzt „das Dreifache der Summe aus x und 5“ in den Term 3x + 5. Stimmt das?“
  - deuten / uebung / Stufe 3: „Jemand übersetzt „die Differenz aus 8 und x“ in den Term x − 8. Stimmt das?“
- **terme.umformen**:
  - zusammenfassen / uebung / Stufe 3: „Jemand rechnet: 6x + 9y = 15xy. Was stimmt?“
  - produkte / uebung / Stufe 3: „Jemand rechnet: 5x · 4x = 20x. Was stimmt?“
  - produkte / uebung / Stufe 3: „Jemand rechnet: 8x · 8x = 64x. Was stimmt?“
  - ausklammern / uebung / Stufe 3: „Jemand klammert aus: 12x + 20 = 2(6x + 10). Was stimmt?“
  - ausklammern / uebung / Stufe 3: „Jemand klammert aus: 30x + 10 = 2(15x + 5). Was stimmt?“
  - aequivalenz / uebung / Stufe 3: „Sind (x + 3)² und x² + 9 äquivalent?“
  - binomisch / uebung / Stufe 3: „Ergänze so, dass eine binomische Formel entsteht: x² + 14x + □ = (x + □)²“
- **abbildungen.kongruenz**:
  - mittelsenkrechte / uebung / Stufe 1: „Die Punkte A(−4 | −5) und B(−4 | 3) liegen übereinander. Gib die Mittelsenkrechte von [AB] an.“
  - mittelsenkrechte / uebung / Stufe 1: „Die Punkte A(−5 | −1) und B(1 | −1) liegen auf einer waagrechten Linie. Gib die Mittelsenkrechte von [AB] an.“
  - mittelsenkrechte / uebung / Stufe 2: „Fälle das Lot von P(0 | 3) auf die waagrechte Gerade g: y = −2. Wo ist der Lotfußpunkt F?“
  - mittelsenkrechte / uebung / Stufe 2: „Wie weit ist Q(5 | −3) von der Geraden g: y = 2 entfernt? (1 Einheit = 1 cm)“
  - mittelsenkrechte / uebung / Stufe 3: „Fälle das Lot von P(4 | −2) auf die Gerade y = x. Wo ist der Lotfußpunkt F?“
  - mittelsenkrechte / korrektur / Stufe 2: „Wie weit ist C(4 | 3) von der Geraden g: y = 6 entfernt? (1 Einheit = 1 cm)“
  - mittelsenkrechte / sicherung / Stufe 2: „Wie weit ist C(0 | −2) von der Geraden g: y = 5 entfernt? (1 Einheit = 1 cm)“
  - mittelsenkrechte / sicherung / Stufe 2: „Fälle das Lot von P(5 | −1) auf die senkrechte Gerade g: x = 3. Wo ist der Lotfußpunkt F?“
  - mittelsenkrechte / sicherung / Stufe 2: „Wie weit ist P(6 | 7) von der Geraden g: y = 5 entfernt? (1 Einheit = 1 cm)“
  - winkelhalbierende / uebung / Stufe 2: „Gegeben sind die Geraden g: y = 2 und h: x = −3. Welcher Punkt ist von g und h gleich weit entfernt?“
  - winkelhalbierende / uebung / Stufe 3: „g: y = 2 und h: x = −2 kreuzen sich. Gesucht ist der Punkt rechts von h und oberhalb von g, der von g und h gleich weit entfernt ist und auf y = 5 liegt.“
  - winkelhalbierende / uebung / Stufe 3: „Gegeben sind die Geraden g: y = 0 und h: x = −2. Welcher Punkt ist von g und h gleich weit entfernt?“
  - winkelhalbierende / test / Stufe 2: „Gegeben sind die Geraden g: y = 3 und h: x = 2. Welcher Punkt ist von g und h gleich weit entfernt?“
  - winkelhalbierende / sicherung / Stufe 2: „Gegeben sind die Geraden g: y = 1 und h: x = −1. Welcher Punkt ist von g und h gleich weit entfernt?“
  - winkelhalbierende / sicherung / Stufe 2: „Gegeben sind die Geraden g: y = 1 und h: x = −2. Welcher Punkt ist von g und h gleich weit entfernt?“
- **gleichungen.linear**:
  - sach / uebung / Stufe 2: „Lena hat 54 € und spart jede Woche 6 € dazu. Tom hat 164 € und gibt jede Woche 5 € aus. Nach wie vielen Wochen haben beide gleich viel?“
  - sach / uebung / Stufe 2: „Lena hat 42 € und spart jede Woche 6 € dazu. Tom hat 152 € und gibt jede Woche 4 € aus. Nach wie vielen Wochen haben beide gleich viel?“
  - sach / uebung / Stufe 3: „„Zwei aufeinanderfolgende natürliche Zahlen ergeben zusammen 66.“ Die Gleichung x + (x + 1) = 66 liefert x = 32,5. Was folgt daraus?“
  - sach / uebung / Stufe 3: „Tarif A: 28 € und 2 € pro Stunde. Tarif B: 0 € und 4 € pro Stunde. Die Gleichung ergibt x = 14. Welcher Tarif ist bei 17 Stunden günstiger?“
- **bruch.prozent_grundwert**:
  - argumente / uebung / Stufe 2: „Welche Aussage ist mathematisch richtig begründet?“ (die beiden Fassungen mit der richtigen Antwort „200 € mit 19 % Mehrwertsteuer ergeben 238 € …“ bzw. „Erst 40 % Rabatt, dann 50 % Rabatt …“)
  - argumente / uebung / Stufe 2: „Welche Aussage ist mathematisch richtig begründet?“ (die beiden Fassungen mit der richtigen Antwort „200 € mit 19 % Mehrwertsteuer ergeben 238 € …“ bzw. „Erst 40 % Rabatt, dann 50 % Rabatt …“)
- **geometrie.konstruktion**:
  - satz_kehrsatz / uebung / Stufe 1: „Wie lautet der Kehrsatz zu: „Wenn ein Viereck eine Raute ist, dann ist es ein Parallelogramm.““
- **geometrie.kreis**:
  - lage / uebung / Stufe 3: „Ein Kreis hat den Mittelpunkt M(3 | 0) und den Radius r = 3. Wie viele gemeinsame Punkte haben der Kreis und die Gerade x = 0?“
  - lage / uebung / Stufe 3: „Ein Kreis hat den Mittelpunkt M(−1 | 4) und den Radius r = 2. Welche Lage hat die Gerade y = 3?“
  - lage / uebung / Stufe 3: „Ein Kreis hat den Mittelpunkt M(−2 | 0) und den Radius r = 4. Welche Lage hat die Gerade x = −6?“
  - lage / uebung / Stufe 3: „Ein Kreis hat den Mittelpunkt M(1 | −2) und den Radius r = 4. Welche Lage hat die Gerade y = −4?“
  - lage / uebung / Stufe 2: „Ein Kreis hat den Mittelpunkt M(2 | 1) und den Radius 3. Welche Lage hat die Gerade y = 4?“
  - lage / uebung / Stufe 3: „Ein Kreis hat den Mittelpunkt M(−2 | 3) und den Radius 2. Wie viele der Geraden x = 0, y = 0, y = 5 und x = −5 sind Tangenten?“
  - tangente / uebung / Stufe 2: „Ein Kreis um M(0 | 0) berührt eine Tangente im Punkt B(0 | 3). Gib die Gleichung der Tangente an.“

### (5) Für den Nutzer (braucht eine Entscheidung)
- abbildungen.kongruenz / achsenspiegelung (Tatsache): 21 freigegebene Aufgaben und die Karte selbst nutzen Geradengleichungen („an der Geraden x = 3“, „y = 4“, „Winkelhalbierende y = x“). Nach dem Prüf-Befund kommen diese erst in Klasse 8. Ich habe sie nicht ersetzt, weil die ganze Karte darauf aufbaut. Ersetzen (rund 21 Aufgaben + Karte) oder als bekannte Schreibweise lassen?
- Überschneidung (Tatsache): geometrie.konstruktion hat die Karten parallelen und winkelsumme, die fast dasselbe prüfen wie geometrie.winkelsaetze (stufen_wechsel, innenwinkelsumme). Vorschlag (Meinung): in geometrie.konstruktion als Wiederholung kennzeichnen oder streichen.
- Reihenfolge (Tatsache): geometrie.konstruktion / satz_kehrsatz nutzt in Stufe 3 den Satz des Thales, der erst in geometrie.kreis (danach) kommt. abbildungen.kongruenz / parkett (Vertiefung) nutzt Innenwinkel regelmäßiger Vielecke vor geometrie.winkelsaetze.
- Lehrplan (Tatsache): M7 1.2 nennt „Produkte und Potenzen von Potenzen mit natürlichen Exponenten zusammenfassen“; terme.umformen hat dazu keine Karte (die Gesetze stehen in terme.potenzgesetze, Klasse 6). Umzug oder neue Karte entscheiden (schon in luecken-kl7 gemeldet).
- geometrie.konstruktion / kongruenzsatz: SsW-Anzahlaufgaben (Stufe 3) bleiben schwer ohne Zeichnen; als Vertiefung kennzeichnen? (offen seit der Dreizehnten Runde).
- Annahme aus der Prüfung, nicht geprüft: dieselben Karten (mittelsenkrechte, winkelhalbierende, planfigur) gelten für Realschule Klasse 6, nutzen aber negative Koordinaten.

### (6) Nicht geprüft
- Anzeige in der App: Ich habe nur JSON und Prüfskript gesehen. Die neuen Bilder (Sechseck, Spiegeln an y = x, Koordinatensysteme der Kreis-Aufgaben) sind nur rechnerisch geprüft.
- Test-, Korrektur- und Sicherungsaufgaben von geometrie.winkelsaetze, geometrie.konstruktion und geometrie.kreis nur überflogen. Ihre Rechenausdrücke prüft das Skript nach.
- Schulbuch-Abgleich (z. B. Quartil-Verfahren) nicht möglich.

## 2026-11-17 – STATUS
geometrie.kreis fertig: 11 umgestuft, 7 ersetzt (Geradengleichungen „y = 4“, „x = −6“ und „Gib die Gleichung der Tangente an“ durch Beschreibungen ersetzt – gleicher Grund wie der Prüf-Befund zu Klasse 7), 1 Lösungsweg berichtigt. Prüfer OK, Nachweis OK.

## 2026-11-17 – STATUS
geometrie.konstruktion fertig: 8 umgestuft, 1 ersetzt (doppelte Stufe-1-Frage), 9 Lösungswege in planfigur ohne Geradengleichungen (Prüf-Befund). Prüfer OK, Nachweis OK.

## 2026-11-17 – STATUS
daten.boxplot fertig: 23 umgestuft (Stufen unterschieden sich vor allem in der Länge der Datenliste), 4 neu. Prüfer OK, Nachweis OK. (Nachweis-Skript verbessert: neue Übungen direkt hinter einer umgestuften Aufgabe werden jetzt richtig zugeordnet.)

## 2026-11-17 – STATUS
bruch.prozent_grundwert fertig: 16 umgestuft, 2 ersetzt, 6 neu. Prüfer OK, Nachweis OK.

## 2026-11-17 – STATUS
gleichungen.linear fertig: 8 umgestuft, 4 ersetzt (Wiederholungen in sach), 3 neu (klammern, Stufe 3). Prüfer OK, Nachweis OK.

## 2026-11-17 – STATUS
geometrie.winkelsaetze fertig: 5 umgestuft (gleicher Aufgabentyp in Stufe 2 und 3), sonst unverändert. Prüfer OK, Nachweis OK.

## 2026-11-17 – STATUS
abbildungen.kongruenz fertig (nach Einführen von lernen-app c976669 mit dem berichtigten Bildausschnitt): 9 umgestuft, 15 ersetzt, 15 Lösungswege berichtigt, 3 Lernkarten verbessert. Dabei Prüf-Befund umgesetzt: In mittelsenkrechte und winkelhalbierende stehen statt Geradengleichungen (y = −2, x = 4, y = x, x + y = 10) jetzt Beschreibungen („waagrechte Gerade durch (0 | −2)“, „x-Wert“); vierecke_ordnen: Lösungsweg ohne „(oder ein Spezialfall davon)“, Fehler-Satz klarer. Prüfer OK, Nachweis OK.

## 2026-11-17 – STATUS
terme.umformen fertig: 18 umgestuft, 7 ersetzt, 22 neu (vor allem Stufe 3 mit anderem Gedanken). Prüfer OK, Nachweis OK.

## 2026-11-17 – STATUS
terme.aufstellen fertig: 5 umgestuft, 2 ersetzt, 2 neu, 1 Lernkarte verbessert (termwert: Schritt zur Tabellenkalkulation). Prüfer OK, Nachweis OK (`python3 -I inhalte/generatoren/_durchsicht_nachweis.py terme.aufstellen`).
