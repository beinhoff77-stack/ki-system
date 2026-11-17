# Postfach stufen-kl8 (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, Klasse 8)

## 2026-11-17 – STATUS (je Thema eine Zeile, neueste unten)
Annahme zu „überzählig“: Überzählige Übungen bleiben in der Datei (Stufe nach Typ gesetzt), bekommen aber **kein** `g`, damit das Prüfskript sie nicht mitzählt; sie stehen im Abschlussbericht und können gesperrt werden. Für die übrigen Übungen prüft `_stufen_kl8.py` die Mengenregeln des Auftrags (S1 ≥ 4/2 Typen, S2 ≥ 6/3, S3 ≥ 8/4, je S3-Typ ≤ 3, nie zwei gleiche Typen hintereinander). Nachweis: `_stufen_nachweis.py`.
- gleichungen.ungleichungen: 38 neue Übungen, 14 Knobel-Bordkarten, 13 umgestuft, 31 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- zahlen.intervalle: 25 neue Übungen, 8 Knobel-Bordkarten, 23 umgestuft, 27 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- terme.bruchterme: 39 neue Übungen, 14 Knobel-Bordkarten, 19 umgestuft, 48 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- gleichungen.formeln: 23 neue Übungen, 10 Knobel-Bordkarten, 11 umgestuft, 24 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- gleichungen.bruch: 45 neue Übungen, 14 Knobel-Bordkarten, 21 umgestuft, 52 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- gleichungen.lgs2: 53 neue Übungen, 16 Knobel-Bordkarten, 21 umgestuft, 58 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- funktionen.grundbegriffe: 38 neue Übungen, 18 Knobel-Bordkarten, 14 umgestuft, 43 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- funktionen.linear: 30 neue Übungen, 16 Knobel-Bordkarten, 13 umgestuft, 28 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- funktionen.gebrochen: 36 neue Übungen, 14 Knobel-Bordkarten, 13 umgestuft, 35 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- messen.koerper_darstellung: 19 neue Übungen, 12 Knobel-Bordkarten, 8 umgestuft, 19 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- messen.kreisberechnung: 21 neue Übungen, 14 Knobel-Bordkarten, 6 umgestuft, 28 überzählig. `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- messen.prisma_zylinder: 17 neue Übungen, 14 Knobel-Bordkarten, 10 umgestuft, 0 überzählig (alle Übungen mit Typ, strenge Prüfregeln laufen). `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- stochastik.grundbegriffe: 20 neue Übungen, 12 Knobel-Bordkarten, 0 umgestuft, 13 überzählig (ohne Typ, im Abschlussbericht). `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.
- groessen.indirekt: 16 neue Übungen, 14 Knobel-Bordkarten, 1 umgestuft, 24 überzählig (ohne Typ, im Abschlussbericht). `inhalt_pruefen` OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 – FERTIG: Abschlussbericht Zwanzigste Runde, Klasse 8

Alle 14 Kl.-8-Themen aus `themenliste.json` sind bearbeitet (je Thema ein Commit auf `stufen-kl8`, kein Merge). `raum.schraegbilder` und `stochastik.simulation` stehen in der Themenliste inzwischen bei Klasse 10 und sind deshalb nicht dabei.

**Fakten:** Für jedes Thema meldet `python3 -I tools/inhalt_pruefen.py` OK mit 0 Gruppen „gleich gebaut hintereinander“. `_stufen_nachweis.py` bestätigt gegen `origin/lernen-app`: alte Aufgaben unterscheiden sich nur in `g` und `s`; Felder außerhalb von `aufgaben` sind unverändert. Alle Werte stammen aus `c`, das neu nachgerechnet wurde; die Lösungen habe ich von Hand geprüft. Jede Lernkarte hat genau 2 Knobel-Bordkarten (kein Fall mit nur einer).

**Annahme (bitte bestätigen):** Überzählige Übungen haben kein `g` bekommen, weil der Auftrag „nicht löschen“ verlangt und die Prüfregel höchstens 2 Aufgaben je Bauplan erlaubt. Sie stehen in Liste (4). Wenn gewünscht, kann man sie sperren oder ihnen später einen Typ geben.

**Meinung:** Die vielen überzähligen Aufgaben (Tabellen- und „Ergänze“-Serien mit gleichem Wortlaut) sind kaum Lernstoff; eine spätere Runde sollte sie eher ersetzen als nur markieren.

### (1) Stufen-Leiter je Lernkarte

**gleichungen.ungleichungen**

- `umformen` — S1: eine Ungleichung mit einem Umformungsschritt lösen, Grenze am Zahlenstrahl zeigen · S2: zwei Schritte, x auf beiden Seiten, Sachsatz in Ungleichung übersetzen, Ungleichung zur Lösungsmenge finden · S3: Sonderfälle (keine/jede Zahl) begründen, Parameter, Fehler finden, Modell selbst aufstellen, mit Dreiecksungleichung verknüpfen
- `umdrehen` — S1: mit einer negativen Zahl malnehmen/teilen und dabei das Zeichen umdrehen · S2: mehrere Schritte mit negativem Faktor, Sachsatz übersetzen, Ungleichung zu einer Lösungsmenge finden · S3: allgemein begründen (a < b ⇒ −a > −b), Fehler deuten, rückwärts rechnen, Parameter, Sachmodell, mit Termen verknüpfen
- `klammern` — S1: Klammer auflösen und eine einfache Ungleichung lösen · S2: Klammern und x auf beiden Seiten, Sachaufgabe mit Klammer, fehlende Zahl so bestimmen, dass eine Lösungsmenge herauskommt · S3: Sonderfälle begründen, mit Brüchen und x² verknüpfen, Fehler beim Minus vor der Klammer finden, Parameter, rückwärts von der größten Lösung
- `intervall` — S1: eine einfache Lösungsmenge als Intervall schreiben bzw. zu einem Intervall die Ungleichung erkennen · S2: erst lösen, dann als Intervall angeben; Sachgrenzen und Zahlenstrahl-Bilder in Intervalle übersetzen · S3: Doppelungleichungen und zwei Bedingungen verknüpfen, leere Menge begründen, Klammerfehler finden, Parameter, ganze Zahlen zählen
- `pruefen` — S1: eine Zahl einsetzen und prüfen, ob sie die Ungleichung erfüllt · S2: kleinste/größte ganze Lösung bestimmen, Sachgrenze mit ganzen Zahlen, Zahl so wählen, dass eine Grenze entsteht · S3: Rechenwege beurteilen und Fehler deuten, Aussagen widerlegen, Parameter, rückwärts, mit Brüchen verknüpfen, Lösungen zählen
- `grafisch` — S1: am Graphen ablesen, wo eine Gerade über/unter der x-Achse oder einer waagrechten Geraden liegt · S2: zwei Geraden vergleichen (Schnittpunkt als Grenze), Lösungsmenge aus dem Bild, Tarife als Geraden · S3: zwischen drei Geraden verknüpfen, Ablesefehler deuten, parallele Geraden begründen, Parameter, rückwärts zur Geraden, Prüfungsaufgabe mit zwei Punkten
- `sachaufgabe` — S1: eine einfache Höchstens-/Mindestens-Situation mit einer Ungleichung lösen oder die passende Ungleichung erkennen · S2: Grundpreis plus Stückpreis, aus einer Tabelle die Ungleichung aufstellen, eine andere Größe als gewohnt berechnen · S3: zwei Tarife vergleichen, Durchschnitt/Umfang/Kosten pro Person verknüpfen, falsches Runden finden, „nie billiger“ begründen

**zahlen.intervalle**

- `lesen` — S1: Intervallschreibweise in Worte/Ungleichung übersetzen, Intervall am Bild erkennen · S2: Sachgrenzen („ab“, „bis einschließlich“) als Intervall, Intervall aus Anfang und Länge, Ungleichungspaar ↔ Intervall · S3: Mengen verknüpfen (ohne, zugleich), Parameter, Fehler beim Lesen deuten, Unendlichkeit begründen, rückwärts aus Mitte und Länge
- `schreiben` — S1: eine Doppelungleichung als Intervall schreiben, die passende Schreibweise erkennen · S2: Zahlenbereiche aus Worten, Sachbereiche und gelöste Ungleichungen als Intervall · S3: Abstand und „nicht negativ“ deuten, Brüche/Dezimalzahlen verknüpfen, Parameter, rückwärts umrechnen, begründen, wann es kein einziges Intervall gibt
- `enthalten` — S1: prüfen, ob eine Zahl im Intervall liegt, Länge eines Intervalls · S2: ganze Zahlen im Intervall zählen, Sachlänge, aus der Anzahl eine Grenze bestimmen · S3: Schnitt und Vereinigung, Parameter, Zählfehler deuten, Teilmenge begründen, Brüche zählen, Prüfungsaufgabe mit zwei Mengen
- `beurteilen` — S1: eine richtige Aussage über ein Intervall erkennen · S2: die falsche Aussage finden, Sachgrenzen und Zahlenstrahl-Bilder beurteilen, Mitte bestimmen und prüfen · S3: allgemeine Aussagen begründen, Sonderfall [a; a], Fehler deuten, Parameter, Brüche, Schnittmenge wie in einer Prüfung

**terme.bruchterme**

- `definitionsmenge` — S1: die Zahl finden, für die ein einfacher Nenner 0 wird, und D angeben · S2: Nenner mit Faktor oder Produkt, Sachterm deuten, zu einer Definitionsmenge den Term finden · S3: mehrere Nenner verknüpfen, Nenner, der nie 0 wird, begründen, Fehler beim Vorzeichen, Parameter, rückwärts, Sachmodell
- `termwert` — S1: eine Zahl in einen Bruchterm einsetzen und ausrechnen · S2: Ergebnis als gekürzter Bruch, Sachterm auswerten, gesuchtes x zu einem Wert bestimmen · S3: rückwärts aus dem Wert, verketten T(T(x)), Fehler beim Einsetzen, Parameter, Tabellenkalkulation, unmöglichen Wert begründen
- `kuerzen` — S1: gemeinsame Faktoren (Zahl, Potenz von x) in Zähler und Nenner kürzen · S2: erst ausklammern, dann kürzen; den Term finden, der gekürzt ein Ergebnis ergibt; Tabellenwerte durch Kürzen erklären · S3: binomische Formeln verknüpfen, „Summen kürzen“ als Fehler deuten, begründen, Parameter, ungekürzten Term rekonstruieren
- `erweitern` — S1: einen Bruchterm auf einen vorgegebenen Nenner erweitern · S2: den Erweiterungsfaktor bestimmen, Zähler mit Klammer erweitern, gleichwertigen Term mit gegebenem Nenner finden · S3: Nenner erst faktorisieren, Hauptnenner, Erweitern mit −1, Fehler beim Ausmultiplizieren, begründen, rückwärts zum ursprünglichen Term
- `addieren` — S1: gleichnamige Bruchterme addieren/subtrahieren und den Hauptnenner erkennen · S2: auf Hauptnenner bringen, Zahl und Bruch zusammenfassen, Sachsituation (Anteile), fehlenden Zähler bestimmen · S3: verschiedene Nenner mit Klammer, Fehler 1/x + 1/y = 2/(x + y) widerlegen, Parameter, rückwärts, Prüfungsaufgabe mit Vereinfachen
- `multiplizieren` — S1: zwei Bruchterme multiplizieren und kürzen, Kehrwert erkennen · S2: dividieren (mit dem Kehrwert malnehmen), Flächen mit Bruchtermen, fehlenden Faktor finden · S3: Klammerterme kürzen, Fehler beim Dividieren deuten, Aussagen widerlegen, Parameter, rückwärts, Ergebnis als Zahl
- `fehler_finden` — S1: eine richtige Umformung erkennen bzw. eine einfache auf Richtigkeit prüfen · S2: die falsche Umformung finden, mit einer Probezahl prüfen, Tabelle und Definitionsmenge zusammendenken · S3: begründen, warum Summanden nicht gekürzt werden, Fehler im Rechenweg deuten, Gegenbeispiele, binomische Formeln verknüpfen

**gleichungen.formeln**

- `ein_schritt` — S1: eine Formel mit einer Rechenart nach einer Größe umstellen, nach einer Größe aufgelöste Formel erkennen · S2: Umstellen am Zahlenbeispiel nachmachen, umstellen und einsetzen, Sachformel aus der Physik verwenden · S3: Proben deuten, Veränderungen (verdoppeln, dritteln) begründen, Kehrwertformeln, abschätzen wie in einer Prüfung
- `zwei_schritte` — S1: Formeln mit zwei Rechenschritten (Strich und Punkt) umstellen · S2: Klammern, Brüche in Formeln, Sachformeln (Mittelwert, Fahrenheit) rückwärts nutzen · S3: Trapezformel verknüpfen, Formel zur Umstellung finden, Parameter auf beiden Seiten, Klammerfehler deuten, Prüfungsaufgabe mit Kosten
- `pruefen` — S1: eine einfache Umstellung prüfen bzw. selbst ausführen · S2: zweischrittige Umstellungen prüfen, Sachformel prüfen, Ausgangsformel zu einer Umstellung finden · S3: Fehler mit Probezahlen aufdecken, wann eine Probe versagt, Prozentformel verknüpfen, Parameter (m ≠ 0), rückwärts, Prüfungsaufgabe
- `einsetzen` — S1: die passende Formel wählen und Werte einsetzen · S2: erst umstellen, dann einsetzen; Einheiten umrechnen (dm³, Minuten); Tarifformeln · S3: Einheiten verknüpfen, Fehler bei vertauschten Größen, Dichte begründen, rückwärts zur Dichte, Durchschnittsgeschwindigkeit wie in einer Prüfung
- `geometrie` — S1: aus Fläche und Grundseite die Höhe (bzw. aus dem Umfang die Seite) berechnen · S2: Volumenformeln von Quader, Prisma, Pyramide nach der Höhe auflösen, Sachmaße (Liter) · S3: zwei Bedingungen verknüpfen (doppelt so lang, gleiches Volumen), Halbierungsfehler beim Dreieck, begründen, Term mit Parameter, Zelt wie in einer Prüfung

**gleichungen.bruch**

- `definitionsmenge` — S1: die eine Zahl ausschließen, für die ein einfacher Nenner 0 wird · S2: mehrere Nenner, Gleichung zu einer Definitionsmenge finden, Sachgleichung und Tabelle deuten · S3: Nenner faktorisieren, Nenner ohne Nullstelle begründen, Fehler beim Nullsetzen, Parameter, rückwärts zum Nenner, Anzahl ausgeschlossener Zahlen
- `ein_bruch` — S1: a/x = b durch Malnehmen mit x lösen · S2: Nenner mit Faktor oder Summand, Sachsituation als Bruchgleichung, Gleichung zu einem Satz finden, fehlenden Zähler bestimmen · S3: leere Lösungsmenge begründen, Fehler beim Malnehmen deuten, rückwärts aus einer Denkaufgabe, Prozent verknüpfen, Parameter, Lösen mit Probe
- `ueber_kreuz` — S1: a/x = b/(x + c) über Kreuz multiplizieren und lösen · S2: zwei Klammernenner, Zähler mit x, Sachsituation und Satz als Gleichung · S3: x² hebt sich weg, begründen warum über Kreuz erlaubt ist, Fehler (über Kreuz bei Summe), Parameter, rückwärts, Anteils-Transfer
- `hauptnenner` — S1: gleichnamige Brüche zusammenfassen und mit x malnehmen · S2: Hauptnenner wie 5x, Zahl und Bruch gemischt, Arbeitsaufgaben (Pumpen, Streichen), fehlenden Zähler bestimmen · S3: gleicher Nenner als Block, binomische Formel im Nenner, Identität und leere Menge begründen, Fehler beim Malnehmen, Parameter, drei Leitungen
- `scheinloesung` — S1: lösen und prüfen, ob die Lösung zu D gehört · S2: Scheinlösung erkennen und L = { } schreiben, Bruch und Zahl gemischt, Gleichung mit Scheinlösung finden · S3: begründen, warum die Scheinlösung fällt, binomische Formeln verknüpfen, Fehler beim Aufschreiben, Parameter für leere Lösungsmenge
- `verhaeltnis` — S1: eine Verhältnisgleichung x : a = b : c lösen und erkennen · S2: x im zweiten Glied, Mischungen und Maßstab, fehlendes Glied bestimmen · S3: x auf beiden Seiten, Flächen im Maßstab, Differenz/Verhältnis verknüpfen, Fehler, Umordnen begründen, Parameter, Verhältnis ändert sich
- `graphisch` — S1: die Lösung am Schnittpunkt einer Hyperbel mit einer waagrechten Geraden ablesen · S2: Hyperbel und schräge Gerade, passende Gleichung zum Bild, Sachgraph · S3: Anzahl der Lösungen begründen, Ablesefehler (x und y vertauscht), Parameter c ohne Lösung, rückwärts zur Geraden, Prüfungsaufgabe mit Punkt

**gleichungen.lgs2**

- `pruefen` — S1: ein Zahlenpaar in beide Gleichungen einsetzen bzw. die Lösung unter mehreren Paaren erkennen · S2: Teilantworten (nur I erfüllt), Kommazahlen, Sachpreise prüfen, Paar finden, das nur eine Gleichung erfüllt · S3: Parameter c, Sachsituation als System, unvollständige Probe als Fehler, Anzahl der Lösungen begründen, mit Geraden verknüpfen
- `grafisch` — S1: den Schnittpunkt zweier gezeichneter Geraden ablesen bzw. berechnen · S2: Gleichungen zum Zeichnen umstellen, Lösungsanzahl am Bild, Tarifgeraden, Probe am abgelesenen Punkt · S3: Ablesefehler deuten, Bruch-Schnittpunkt rechnen, System zum Bild finden, Parallele ohne Lösung, Parameter, Geraden aus Punkten
- `einsetzen` — S1: einen Term y = … in die andere Gleichung einsetzen (mit Klammer) und lösen · S2: erst x = … oder Kommazahlen, Altersaufgabe, Konstante aus der Lösung bestimmen, gewöhnliches System selbst lösen · S3: Klammerfehler deuten, unendlich viele Lösungen begründen, rückwärts zu einer Konstanten, Rechteck verknüpfen, Parameter, Zahlenrätsel
- `gleichsetzen` — S1: zwei nach y aufgelöste Gleichungen gleichsetzen und lösen · S2: erst eine Gleichung umstellen, x = … gleichsetzen, Tarifvergleich, System zu einer Gleichung finden · S3: Treffpunkt und Kerzen modellieren, Rechenfehler deuten, rückwärts zur Geraden, Terme verknüpfen, keine Lösung begründen, Parameter
- `addition` — S1: zwei Gleichungen mit Gegenzahlen addieren, den passenden Faktor erkennen · S2: eine Gleichung vervielfachen, Preisaufgaben, Gleichung so ergänzen, dass eine Variable wegfällt · S3: Brüche und Dezimalzahlen verknüpfen, Fehler (rechte Seite vergessen), begründen, Parameter, rückwärts, geschickt addieren
- `verfahren` — S1: an der Form erkennen, welches Verfahren passt, und es anwenden · S2: eine Gleichung erst passend umstellen, Sachsätze als System, ein System zu einem Verfahren finden · S3: begründen, warum ein Weg umständlich ist, Faktoren wählen, drei Gleichungen, geschicktes Addieren/Subtrahieren, Methodenfehler
- `loesbarkeit` — S1: an Steigung und Achsenabschnitt erkennen: keine, eine oder unendlich viele Lösungen · S2: Vielfache von Gleichungen erkennen, Bedeutung am Bild, Sachsituation ohne Lösung · S3: Parameter für keine/unendlich viele Lösungen, zwei Lösungen ⇒ unendlich viele, drei Gleichungen, Fehldeutung von 0 = 0
- `sachaufgabe` — S1: eine vertraute Sachaufgabe (Köpfe/Beine, Münzen) mit zwei Gleichungen lösen oder das System erkennen · S2: Eintritt, Münzen mit Kommabeträgen, Zimmer, Rechteck, zu einem System die Frage finden · S3: Mischung, Alter rückwärts, Ziffernrätsel verknüpfen, Bleistift-Falle begründen, Parameter, falsche Gleichung deuten, Prüfungsaufgabe Pizza

**funktionen.grundbegriffe**

- `eindeutig` — S1: an Wertepaaren erkennen, ob jedes x genau ein y hat · S2: Alltagszuordnungen und ihre Umkehrung beurteilen, Tabelle und Graph prüfen, die Nicht-Funktion finden · S3: Rennstrecke und Kreis begründen, Fehler in einer Behauptung finden, Parameter a, rückwärts zum Urbild, Geometrie verknüpfen, Tabellen wie in einer Prüfung
- `mengen` — S1: die maximale Definitionsmenge bei einem einfachen Nenner angeben · S2: Wertemenge zu einer kleinen Definitionsmenge berechnen, Sachdefinitionsmenge, Zahl finden, die kein Funktionswert ist · S3: Nenner mit Produkt, Wertebereich von x² begründen, Fehler (D statt W), Parameter, Prüfungsaufgabe D = W
- `funktionswert` — S1: eine Zahl in einen linearen Term einsetzen · S2: Terme mit x², Brüchen, Kommazahlen; Differenz zweier Werte; Tabellenkalkulation; Sachterm · S3: gleiche Werte f(a) = f(a + 1), rückwärts zu a, Klammerfehler bei −3², Symmetrie begründen, verketten, Wurf-Modell, Prüfungsaufgabe
- `stelle` — S1: zu einem Funktionswert die Stelle bei einem linearen Term finden · S2: Klammer-, Bruch- und Kommaterme, Sachaufgabe (Handwerkerrechnung), Term erst bestimmen, dann Stelle · S3: Sonderfall „kein x“ begründen, zwei Stellen bei x², Bruchterm verknüpfen, Fehler (einsetzen statt lösen), rückwärts, Akku-Modell
- `wertetabelle` — S1: einen fehlenden y-Wert in der Wertetabelle eines linearen Terms ergänzen · S2: x²-Terme, fehlenden x-Wert finden, Nullstelle aus der Tabelle, Sachtabelle (Schneehöhe) · S3: Term zur Tabelle rückwärts finden, Parameter a, Fehler beim Quadrieren, begründen (gleiche Zuwächse), Summe wie in einer Prüfung
- `graph_lesen` — S1: einen Funktionswert am Graphen ablesen · S2: zu einem y-Wert die Stelle(n) finden, Sachgraph (Badewanne) · S3: Bereiche (unterhalb der Achse, gleichbleibend) deuten, Parameter c, x und y vertauscht als Fehler, Graph und Funktionsbegriff begründen, Fläche verknüpfen
- `nullstellen` — S1: die Nullstelle einer linearen Funktion berechnen · S2: Produktform und x² + 5, Sachfunktion (Kerze), Funktion zu einer Nullstelle finden · S3: Bruchfunktionen verknüpfen, Achsenpunkte wie in einer Prüfung, gekürzte Nullstelle begründen, Parameter b, Summe der Nullstellen
- `punkt_graph` — S1: prüfen, ob ein Punkt auf dem Graphen einer linearen Funktion liegt · S2: x²- und Bruchterme, Lage oberhalb/unterhalb, Stelle zu einem y-Wert, Sachgraph · S3: Parameter k aus einem Punkt, Fehler beim Einsetzen, rückwärts zur Koordinate, zwei Punkte verknüpfen, P(a | a), Definitionslücke begründen
- `sachzusammenhang` — S1: einen Wert aus einem Sachgraphen ablesen, Kosten berechnen, den Kostenterm erkennen · S2: Änderungen und Höchstwert am Graphen, Stundenzahl aus der Rechnung, Term aus einer Tabelle · S3: Tarife vergleichen, Aussagen über Verläufe begründen, Fehler im Kostenterm, Preiserhöhung verknüpfen, Prüfungsaufgaben mit zwei Tarifen

**funktionen.linear**

- `ablesen` — S1: m und t aus y = mx + t ablesen · S2: umsortierte Form (y = 4 − 5x), Steigungsdreieck und Bild, steilste Gerade, Sachgleichung deuten · S3: erst nach y auflösen, Prozent-Steigung, rückwärts aus Gitterpunkten, Parameter, Fehler beim Ablesen, gleiche Steigung begründen
- `graph_ablesen` — S1: t am Graphen ablesen, mit einem Steigungsdreieck (1 nach rechts) zeichnen · S2: Steigungsdreiecke aus ganzen Kästchen, Bruchsteigung, Gerade zur Gleichung finden, Treppe als Sachbild · S3: Wahl der Geraden begründen, kleinstes passendes Dreieck, große Dreiecke umrechnen, Steigung aus Gitterpunkten, Nullstelle beim Zeichnen, Zeichenfehler
- `zwei_punkte` — S1: die Steigung aus zwei gegebenen Punkten mit (y₂ − y₁) : (x₂ − x₁) berechnen · S2: Kommazahlen, drei Punkte auf einer Geraden, Beschreibung „4 nach rechts, 6 nach unten“, Höhenprofil · S3: waagrechte/senkrechte Gerade begründen, Fehler bei der Reihenfolge, Rampe nach Vorschrift, Parameter a, rückwärts zu einer Koordinate
- `proportional` — S1: mit dem Dreisatz bei einer proportionalen Zuordnung rechnen · S2: Ursprungsgerade durch einen Punkt, Verbrauch und Füllzeit, Tabellen auf Proportionalität prüfen · S3: Rezeptfehler deuten, Grundgebühr begründet ausschließen, Zuwachs nutzen, Parameter, rückwärts, Maßstab verknüpfen, mehrteilige Preisaufgabe
- `aufstellen` — S1: aus m und t die Geradengleichung bilden · S2: aus m und einem Punkt, Sachsituationen (Sparschwein, Tank), parallele Gerade · S3: aus zwei Punkten, Kostenaufgabe mit zwei Angaben, Achsenpunkte wie in einer Prüfung, x/y-Verwechslung als Fehler, warum ein Punkt nicht reicht
- `schnittpunkte` — S1: Nullstelle und y-Achsenabschnitt einer Geraden bestimmen · S2: Schnittpunkt zweier Geraden durch Gleichsetzen, Tarifvergleich, Gerade durch einen gegebenen Schnittpunkt finden · S3: Parameter a, Dreiecksfläche verknüpfen, parallele Geraden begründen, Fehler (y vergessen), Verfolgung modellieren, allgemeine Form wie in einer Prüfung
- `lage` — S1: an den Steigungen erkennen: parallel, schneidend; Steigung einer Parallelen angeben · S2: Kommazahl-Steigungen, senkrechte Steigung (m₁ · m₂ = −1), parallele Gerade auswählen, Sachsituation · S3: gleiche Gerade begründen, Senkrechte durch einen Punkt, Parameter, rechten Winkel im Dreieck prüfen, Fehler (Gegenzahl statt Kehrwert), Laser-Spiegel
- `deuten` — S1: Steigung und Achsenabschnitt im Sachzusammenhang deuten, einen Wert berechnen · S2: aus einem Betrag die Zeit/Strecke zurückrechnen, Einheiten umrechnen, wann der Tank leer ist · S3: Tarife und Kerzen vergleichen, aus zwei Messwerten rückwärts, y-Achsenabschnitt begründen, Fehldeutung, Prozentanteil verknüpfen

**funktionen.gebrochen**

- `indirekt` — S1: mit „doppelt so viele – halb so lange“ rechnen, direkte und indirekte Proportionalität erkennen · S2: Geschwindigkeit und Zeit, Tabelle ergänzen, x · y = konstant nutzen, Rechteckseite zur festen Fläche · S3: Wippe modellieren, Rechteck unter der Hyperbel, Prozent verknüpfen, Fehler (Pumpen) deuten, Graph begründen, Parameter, rückwärts zur Gruppengröße
- `indirekt_sach` — S1: den umgekehrten Dreisatz in einer vertrauten Situation anwenden · S2: Zuordnungsart begründet wählen, Tabelle ergänzen, Zahnräder und Beete, gesuchte Anzahl statt gesuchter Zeit, Mindestanzahl · S3: Gasgesetz übertragen, Verspätung in Minuten verknüpfen, Parameter x, Mischaufgaben mit zwei Größen, Ausfall unterwegs wie in einer Prüfung
- `definitionsmenge` — S1: die Zahl ausschließen, bei der x + b null wird · S2: Nenner mit Faktor (2x − 3), Nenner 3 − x, Sachfunktion, Funktion zu einer Definitionsmenge finden, Graph lesen · S3: zwei Brüche verknüpfen, x² − 4, Fehler (Konstante mitgezählt), begründen, Parameter b und a, Party-Modell, Vergleich zweier Funktionen
- `asymptoten` — S1: senkrechte und waagrechte Asymptote aus a/(x + b) + c ablesen · S2: beide Asymptoten, Kommazahlen, Asymptoten am Bild ablesen, Sachbedeutung der waagrechten Asymptote · S3: Term aus Asymptoten rückwärts, Schnitt mit einer Geraden, begründen warum y = c nie erreicht wird, Parameter, Vorzeichenfehler, Prüfungsaufgabe mit Nullstelle
- `achsenpunkte` — S1: den Schnittpunkt mit der y-Achse durch Einsetzen von x = 0 bestimmen · S2: Nullstelle berechnen, „keine Nullstelle“ erkennen, Sachfunktion auswerten, Funktion zu einem Achsenpunkt finden · S3: Lücken bei x = 0 begründen, Fehler (x = 0 statt f(x) = 0), Parameter c, rückwärts zu a, Dreiecksfläche verknüpfen, beide Achsenpunkte wie in einer Prüfung
- `parameter` — S1: eine Verschiebung nach oben/unten am Term erkennen · S2: Verschiebung nach links/rechts und oben/unten, Einfluss von a (Streckung, Spiegelung), Term zu einer Verschiebung aufstellen · S3: Term aus Asymptoten, Verschiebungen verketten, Symmetriezentrum, Spiegelung, Fehler bei „+ b nach rechts“, begründen, Spiegelung an y = x
- `beurteilen` — S1: eine richtige Aussage über Definitionslücke oder Nullstelle erkennen · S2: die falsche Aussage finden, Werte berechnen und vergleichen, Stückkosten-Sachaussage beurteilen · S3: Fehlschlüsse (fällt ⇒ größer) widerlegen, Verhalten für große x begründen, Schnittpunkte mit Geraden, Parameter, rückwärts, Abstand-Modell, Prüfungsaufgabe

**messen.koerper_darstellung**

- `prisma` — S1: Ecken, Kanten und Flächen eines n-seitigen Prismas zählen · S2: rückwärts von Kanten/Ecken auf n, Kanten aus Flächen, Sachkörper (Zelt) · S3: unmögliche Zahlen begründen, Zahlen prüfen, Kantenlängen verknüpfen, Euler, abgeschnittene Ecke, n aus einer Summe
- `netz` — S1: Netzfläche eines Quaders berechnen, Gegenflächen am Spielwürfel · S2: Würfelnetze prüfen, Prismen-Netz mit Dreieck, Geschenkpapier, Kante aus der Netzfläche · S3: Höhe rückwärts, Schachtel ohne Deckel, Gegenflächen im Netz, sechstes Quadrat, angemalte Würfel
- `zylinder` — S1: die Teile eines Zylindernetzes benennen, Länge des Mantelrechtecks angeben · S2: Mantelfläche = Umfang · Höhe, Radius aus der Mantellänge, Litfaßsäule · S3: ganze Netzfläche, Überlappung, Rechteck rollen, Mantel-Vergleiche begründen, Fehler (Durchmesser statt Umfang), Prüfungsaufgabe
- `schraegbild` — S1: Kanten nach hinten mit q = 1/2 verkürzt zeichnen, wahre Längen vorne erkennen · S2: wahre Länge rückwärts, Parallelogramme und verdeckte Kanten erkennen, Würfel zeichnen · S3: anderes q, Volumen/Oberfläche aus dem Bild, Maßstab, Fehler q = 1, Verkürzung begründen, q bestimmen
- `ansichten` — S1: die Vorder- oder Draufsicht eines einfachen Körpers nennen · S2: aus zwei Ansichten auf den Körper schließen, liegende Körper, Sachkörper (Turm) · S3: zusammengesetzte Körper verknüpfen, Körper aus drei Ansichten, Würfelgebäude zählen, Ansichten verwechseln als Fehler
- `beurteilen` — S1: eine richtige Aussage über Körper erkennen · S2: die falsche Aussage finden, Aussagen zu Netz, Verpackung und Kantenlängen prüfen · S3: Prisma-Definition begründen, Behauptungen anderer widerlegen, Volumen bei verdoppelten Kanten, 2 026 Kanten, falsche Aussagen in Prüfungsform

**messen.kreisberechnung**

- `umfang` — S1: Umfang aus d oder r berechnen, u : d ≈ 3,14 erkennen · S2: Sachkreise (Rad, Tisch, Borte), Radius/Durchmesser aus dem Umfang, Vielecke im Kreis · S3: Umdrehungen und Maßstab verknüpfen, π-Näherung rückwärts, Seil-Rätsel, π = 3 begründet ablehnen
- `flaeche` — S1: Kreisfläche aus r oder d berechnen, die Formel erkennen · S2: Radius aus der Fläche, Fläche aus dem Umfang, Teppich, Kreis und Quadrat vergleichen · S3: Pizza-Preise, gleiche Fläche wie ein Quadrat, Zaun und Anteil verknüpfen, Umfang = Fläche als Parameter, d statt r als Fehler
- `exakt` — S1: den Umfang exakt als Vielfaches von π angeben · S2: Radius aus exaktem Umfang, Fläche exakt aus d, Sachkreis exakt · S3: Fläche aus dem Umfang rückwärts, Kreisring verknüpfen, Fehler (d quadriert), zusammengesetzte Figur wie in einer Prüfung, Draht umformen
- `verstehen` — S1: den Faktor für Umfang und Fläche bei vervielfachtem Radius angeben · S2: Faktor bei 1,5, halbem Durchmesser, verdoppeltem Umfang; Fläche nach Vergrößerung; Sach- und Tabellenbeispiele · S3: Kreise über r und u vergleichen, Faktor rückwärts, Pizza und Maßstab, Prozent wie in einer Prüfung, Umfangzuwachs begründen, typische Formelfehler deuten
- `sektor` — S1: den Anteil eines Kreisausschnitts aus dem Mittelpunktswinkel bestimmen · S2: Fläche und Bogenlänge mit dem Anteil, Pizzastück, Winkel zu einem Anteil · S3: Winkel rückwärts aus Bogen oder Fläche, Scheibenwischer und Uhr, Kreisdiagramm verknüpfen, Rand wie in einer Prüfung, fehlender Anteil als Fehler
- `zusammengesetzt` — S1: einen Kreisring als Differenz zweier Kreisflächen berechnen · S2: Kreisabschnitt, Ring aus Durchmessern, Halbkreis, Weg um einen Teich, Term für einen Umfang · S3: Figuren zerlegen (Fenster, Sportplatz, Ecken), Laufbahn, Ring rückwärts, Rand eines Halbkreises wie in einer Prüfung
- `zylinder` — S1: Volumen und Mantelfläche eines Zylinders mit der Formel berechnen · S2: Oberfläche, Höhe aus dem Volumen (Regenfass), Dose, Litfaßsäule, Volumenterm erkennen · S3: Wasserspiegel, Vergleiche und gerolltes Blatt begründen, d statt r als Fehler, Grundfläche rückwärts, Parameter, Vase und Rohr wie in einer Prüfung

**messen.prisma_zylinder**

- `prisma_volumen` — S1: V = G · h für Prismen mit Dreieck- oder Trapez-Grundfläche anwenden · S2: L-Profil zerlegen, Sachprismen (Blumenkasten), Parallelogramm, Höhe aus dem Volumen · S3: Würfel und Quader durchsägen, Graben wie in einer Prüfung, Veränderungen begründen, Formelfehler beim Dreieck, Bleistift-Sechseck verknüpfen
- `prisma_oberflaeche` — S1: Mantel aus Umfang · Höhe und Oberfläche eines Dreiecksprismas berechnen · S2: Trapezprismen, offene Rinne, Zelt mit Boden, Mantel aus dem Netz, Keil · S3: Würfelkreuz, durchgesägter Quader, Lackbedarf, Dach, Höhe verdoppelt begründen, Umfang rückwärts
- `prisma_umstellen` — S1: aus V und h die Grundfläche bzw. aus V und G die Höhe berechnen · S2: Liter umrechnen (Gefäß), Seite aus dem Volumen, passende Grundfläche erkennen · S3: Trog und Rinne modellieren, volumengleicher Quader, rückwärts zur Dreiecksseite, Masse des Balkens wie in einer Prüfung, vertauschte Division als Fehler
- `zylinder_volumen` — S1: V = π · r² · h berechnen (auch aus d), Volumen als Grundfläche · Höhe erkennen · S2: halbe Zylinder, Rohre, Topf in Litern, Höhe aus exaktem Volumen, exakter Term · S3: Messbecher und Schlauch, Mindesthöhe rückwärts, Vergleiche begründen, Radius verdoppelt, Umfüllen verknüpfen, Mantel statt Volumen als Fehler
- `zylinder_oberflaeche` — S1: Mantel und Oberfläche eines Zylinders mit der Formel berechnen · S2: Etikett, Becher ohne Deckel, Rohr außen, Oberfläche aus d, Höhe aus exaktem Mantel, exakte Terme · S3: Mantel = Kreisflächen rückwärts, Vergleich begründen, Folientunnel, Radius aus dem Netz, Kreisflächen vergessen als Fehler, Parameter, Blechbedarf wie in einer Prüfung
- `sach` — S1: Volumen von Haus und Regentonne als Prisma bzw. Zylinder berechnen · S2: Säulen, Baumstamm, schräges Becken, Zelt, Treppe, Wasserhöhe rückwärts · S3: Bohrung und Rinne verknüpfen, Trog umfüllen, Dosen packen, Füllzeit und Kosten wie in einer Prüfung, Mindesthöhe rückwärts, halbvoller Tank
- `verstehen` — S1: Volumen bei verdoppelter Höhe oder Grundfläche angeben, V = G · h erkennen · S2: Grundfläche und Höhe zugleich ändern, Prisma und Zylinder mit gleichem G und h, Radius verdreifacht, Kerze, Faktor rückwärts · S3: Maßstab und alle Längen verdoppelt, Würfel und Zylinder, Prozent wie in einer Prüfung, Aussagen begründen, Mantelformel mit d als Fehler

**stochastik.grundbegriffe**

- `begriffe` — S1: Ergebnisraum einfacher Versuche nennen und zählen · S2: Ereignis als Menge schreiben, Ergebnisse eines Ereignisses zählen, anderer Ergebnisraum (Anzahl Wappen), Lose · S3: Zahlenpaare zählen, Reihenfolge begründen, Ereignis in Worten rückwärts, Ziffern zählen, zwei Bedingungen verknüpfen, Augensumme
- `rel_haeufigkeit` — S1: relative Häufigkeit = Anzahl : Gesamtzahl berechnen · S2: aus Tabelle und Säulendiagramm, Prozent, absolute Häufigkeit rückwärts, Klassen-Beispiel · S3: Gruppen zusammenlegen, Mittelwert-Fehler, Rest berechnen, Bruch/Prozent verknüpfen, nötige Treffer rückwärts, Vergleich begründen
- `laplace` — S1: P = günstige : mögliche Ergebnisse bei einer Urne berechnen · S2: Würfel, Skatblatt, Glücksrad (Bruch und Dezimalzahl), Rest-Farbe bestimmen · S3: Kugeln dazulegen rückwärts, Augensummen zweier Würfel, Säcke mischen begründen, „zweite größer“ verknüpfen
- `laplace_pruefen` — S1: entscheiden, ob alle Ergebnisse gleich wahrscheinlich sind · S2: Glücksrad mit Winkeln, Farbe statt Kugel, Augensumme als Ergebnis · S3: Lotto-Irrtum, Winkel planen, Feld gedanklich teilen, Serie deuten, Parameter für Winkel, rückwärts zur fairen Urne, Prüfungsauswahl
- `gegenereignis` — S1: P(nicht E) = 100 % − P(E) berechnen, das Gegenereignis benennen · S2: „nicht durch 3 teilbar“, „keine Primzahl“ über das Gegenereignis, Sachbeispiel, E aus dem Gegenereignis finden · S3: mindestens eine Sechs, zwei Ereignisse und Überschneidung verknüpfen, „keine 7“, P(E) = 3 · P(Ē), falsches Gegenereignis, begründen warum P + P = 1
- `grosse_zahlen` — S1: erwartete Anzahl = Versuche · Wahrscheinlichkeit · S2: Glücksrad mit Anteil, Wahrscheinlichkeit aus vielen Würfen schätzen, Winkel als Wahrscheinlichkeit · S3: Fehlvorstellungen (Roulette) begründen, Anzahl gegen Anteil, Schätzungen vergleichen, Gegenereignis aus Schätzung, „ausgleichen“ als Fehler

**groessen.indirekt**

- `erkennen` — S1: an einer Situation entscheiden, ob „doppelt → halb“ gilt · S2: passende Situation auswählen, Wertepaare mit dem Produkt prüfen, Gegenbeispiele (Quadrat, fester Umfang) · S3: „Je mehr, desto weniger“ als Fehlschluss, Bedingungen begründen, Prozentänderung, y = 2/x, Messwerte wie in einer Prüfung
- `vervielfachen` — S1: fehlenden Wert mit „doppelt → halb“ ergänzen · S2: nicht ganzzahlige Faktoren, x-Wert gesucht, Sachpaare (Pferde, Pumpen), Faktor 0,5 · S3: Zwischenschritt verknüpfen, Busse als Transfer, zwei Lücken, rückwärts zum alten y, Parameter a, Fehler „mal statt geteilt“, begründen, Prüfungsauswahl
- `produkt` — S1: konstantes Produkt bilden und damit einen y-Wert ergänzen · S2: Tabelle auf gleiche Produkte prüfen, Dezimalwerte ergänzen, unpassendes Paar finden · S3: Fehler in der Tabelle finden, Preisgeld rückwärts, Wippe und Tabellenkalkulation, Rechteck verknüpfen, x = y als Parameter
- `dreisatz` — S1: Dreisatz: auf eine Einheit (mal), dann auf den gesuchten Wert (geteilt) · S2: krumme Ergebnisse, passende Rechnung erkennen, Tiere aus Tagen rückwärts · S3: Fehler „geteilt statt mal“, Anzahl für eine Frist rückwärts, Ausfall nach Tagen verknüpfen, Geschwindigkeit, Hühner-Rätsel wie im Wettbewerb, Mindestzahl
- `graph` — S1: Punkte auf y = k : x ablesen bzw. k bestimmen · S2: Punkt auf der Hyperbel prüfen, Graph auswählen, Punkt im Sachzusammenhang deuten, y aus einem Punkt · S3: zwei Hyperbeln verknüpfen, Rechtecke begründen, Schnitt mit y = x, oberhalb einer Geraden, falsche Graphen-Aussage, k rückwärts aus Fläche, Tabelle zu Graph
- `unterscheiden` — S1: an einer Tabelle direkt, indirekt oder weder noch erkennen · S2: Terme zuordnen, fehlenden Wert passend ergänzen, Art ausschließen · S3: Begründung mit „kleiner werdend“ prüfen, lineare Funktion, zwei Zuordnungen verknüpfen, Tabellenkalkulation, Kehrwert begründen, aus Paar rückwärts
- `sach` — S1: einfache Sachaufgaben (Vorrat, Gewinn, Fahrzeit) mit indirekter Proportionalität · S2: Fliesen, Müsli, Fahrzeit, Gläser, Schritte; direkt oder indirekt? Werte rückwärts · S3: Fehler bei Grundgebühr, Wippe und Zahnrad übertragen, Bus mieten rückwärts, Prozent verknüpfen, Prüfungsaufgabe mit Zwischenstand

### (2) Übungen je Stufe und Typ, vorher → nachher

„vorher“ = Zahl der Übungen je Stufe auf `origin/lernen-app`; „nachher“ = typisierte Übungen je Typ (ohne überzählige, ohne Knobel).

**gleichungen.ungleichungen**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| umformen | 4 → 4 (direkt 2, erkennen 2) | 11 → 8 (mehrschritt 6, einkleidung 1, umkehr 1) | 5 → 8 (begruenden 2, parameter 1, rueckwaerts 1, fehler 1, transfer 1, pruefung 1, verknuepfen 1) |
| umdrehen | 4 → 5 (erkennen 3, direkt 2) | 12 → 9 (mehrschritt 7, einkleidung 1, umkehr 1) | 4 → 8 (begruenden 2, fehler 1, rueckwaerts 1, parameter 1, transfer 1, pruefung 1, verknuepfen 1) |
| klammern | 4 → 4 (direkt 3, erkennen 1) | 10 → 8 (mehrschritt 6, einkleidung 1, umkehr 1) | 6 → 8 (verknuepfen 2, begruenden 1, pruefung 1, fehler 1, parameter 1, rueckwaerts 1, transfer 1) |
| intervall | 4 → 6 (direkt 3, erkennen 3) | 8 → 6 (mehrschritt 3, umkehr 1, einkleidung 1, darstellung 1) | 8 → 8 (verknuepfen 3, transfer 1, pruefung 1, begruenden 1, fehler 1, parameter 1) |
| pruefen | 4 → 5 (erkennen 4, direkt 1) | 8 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) | 8 → 8 (fehler 3, begruenden 1, pruefung 1, parameter 1, rueckwaerts 1, verknuepfen 1) |
| grafisch | 4 → 4 (direkt 2, erkennen 2) | 12 → 11 (mehrschritt 5, darstellung 5, einkleidung 1) | 4 → 8 (verknuepfen 2, transfer 1, parameter 1, fehler 1, begruenden 1, rueckwaerts 1, pruefung 1) |
| sachaufgabe | 7 → 6 (direkt 4, erkennen 2) | 5 → 7 (einkleidung 4, mehrschritt 1, umkehr 1, darstellung 1) | 8 → 9 (transfer 3, verknuepfen 3, pruefung 1, fehler 1, begruenden 1) |

**zahlen.intervalle**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| lesen | 4 → 6 (direkt 4, erkennen 2) | 8 → 6 (einkleidung 4, umkehr 1, darstellung 1) | 8 → 8 (transfer 2, verknuepfen 1, parameter 1, fehler 1, begruenden 1, rueckwaerts 1, pruefung 1) |
| schreiben | 9 → 4 (direkt 3, erkennen 1) | 7 → 7 (darstellung 5, einkleidung 1, mehrschritt 1) | 4 → 8 (transfer 2, fehler 1, verknuepfen 1, parameter 1, rueckwaerts 1, pruefung 1, begruenden 1) |
| enthalten | 4 → 6 (erkennen 5, direkt 1) | 8 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) | 8 → 8 (verknuepfen 3, parameter 1, transfer 1, fehler 1, begruenden 1, pruefung 1) |
| beurteilen | 4 → 4 (erkennen 3, direkt 1) | 12 → 6 (umkehr 3, einkleidung 1, darstellung 1, mehrschritt 1) | 4 → 8 (begruenden 3, transfer 1, fehler 1, parameter 1, verknuepfen 1, pruefung 1) |

**terme.bruchterme**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| definitionsmenge | 4 → 4 (direkt 2, erkennen 2) | 8 → 9 (mehrschritt 6, umkehr 2, einkleidung 1) | 8 → 8 (begruenden 3, verknuepfen 1, rueckwaerts 1, parameter 1, fehler 1, transfer 1) |
| termwert | 4 → 4 (direkt 3, erkennen 1) | 12 → 7 (umkehr 3, mehrschritt 3, einkleidung 1) | 4 → 8 (begruenden 2, parameter 1, transfer 1, fehler 1, rueckwaerts 1, verknuepfen 1, pruefung 1) |
| kuerzen | 4 → 4 (direkt 3, erkennen 1) | 8 → 6 (mehrschritt 3, umkehr 1, darstellung 1, einkleidung 1) | 8 → 8 (verknuepfen 3, fehler 1, parameter 1, begruenden 1, rueckwaerts 1, pruefung 1) |
| erweitern | 4 → 4 (direkt 3, erkennen 1) | 9 → 6 (umkehr 3, mehrschritt 2, darstellung 1) | 7 → 9 (verknuepfen 3, transfer 3, rueckwaerts 1, fehler 1, begruenden 1) |
| addieren | 4 → 4 (direkt 3, erkennen 1) | 10 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) | 6 → 8 (verknuepfen 2, pruefung 1, transfer 1, begruenden 1, parameter 1, fehler 1, rueckwaerts 1) |
| multiplizieren | 4 → 4 (direkt 3, erkennen 1) | 8 → 6 (mehrschritt 4, umkehr 1, einkleidung 1) | 8 → 8 (verknuepfen 3, pruefung 1, fehler 1, begruenden 1, parameter 1, rueckwaerts 1) |
| fehler_finden | 4 → 4 (erkennen 2, direkt 2) | 11 → 6 (umkehr 3, einkleidung 1, mehrschritt 1, darstellung 1) | 5 → 8 (begruenden 3, fehler 2, transfer 1, pruefung 1, verknuepfen 1) |

**gleichungen.formeln**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| ein_schritt | 8 → 4 (direkt 3, erkennen 1) | 9 → 6 (darstellung 3, mehrschritt 2, einkleidung 1) | 5 → 8 (fehler 3, transfer 2, begruenden 2, pruefung 1) |
| zwei_schritte | 4 → 4 (direkt 3, erkennen 1) | 11 → 7 (mehrschritt 3, einkleidung 2, umkehr 2) | 5 → 8 (verknuepfen 2, transfer 1, rueckwaerts 1, parameter 1, fehler 1, begruenden 1, pruefung 1) |
| pruefen | 4 → 4 (erkennen 3, direkt 1) | 12 → 6 (mehrschritt 3, einkleidung 1, umkehr 1, darstellung 1) | 4 → 8 (fehler 2, begruenden 2, verknuepfen 1, parameter 1, rueckwaerts 1, pruefung 1) |
| einsetzen | 4 → 7 (direkt 6, erkennen 1) | 10 → 9 (mehrschritt 4, umkehr 3, einkleidung 2) | 6 → 8 (verknuepfen 2, transfer 2, fehler 1, begruenden 1, rueckwaerts 1, pruefung 1) |
| geometrie | 4 → 4 (direkt 3, erkennen 1) | 11 → 10 (mehrschritt 6, umkehr 3, einkleidung 1) | 5 → 8 (verknuepfen 2, transfer 2, fehler 1, begruenden 1, parameter 1, pruefung 1) |

**gleichungen.bruch**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| definitionsmenge | 4 → 5 (direkt 4, erkennen 1) | 8 → 6 (mehrschritt 3, umkehr 1, einkleidung 1, darstellung 1) | 8 → 8 (verknuepfen 3, parameter 1, transfer 1, fehler 1, begruenden 1, rueckwaerts 1) |
| ein_bruch | 4 → 4 (direkt 3, erkennen 1) | 12 → 6 (mehrschritt 3, einkleidung 1, umkehr 1, darstellung 1) | 4 → 8 (begruenden 2, parameter 1, transfer 1, fehler 1, rueckwaerts 1, verknuepfen 1, pruefung 1) |
| ueber_kreuz | 4 → 4 (direkt 2, erkennen 2) | 10 → 6 (mehrschritt 4, einkleidung 1, darstellung 1) | 6 → 9 (verknuepfen 3, begruenden 1, fehler 1, parameter 1, rueckwaerts 1, transfer 1, pruefung 1) |
| hauptnenner | 4 → 4 (direkt 2, erkennen 2) | 8 → 7 (mehrschritt 3, einkleidung 3, umkehr 1) | 8 → 8 (verknuepfen 2, rueckwaerts 1, begruenden 1, fehler 1, parameter 1, transfer 1, pruefung 1) |
| scheinloesung | 4 → 4 (direkt 3, erkennen 1) | 12 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) | 4 → 8 (begruenden 3, verknuepfen 2, fehler 1, parameter 1, pruefung 1) |
| verhaeltnis | 6 → 4 (direkt 3, erkennen 1) | 8 → 8 (einkleidung 5, mehrschritt 2, umkehr 1) | 6 → 8 (verknuepfen 2, transfer 2, pruefung 1, fehler 1, begruenden 1, parameter 1) |
| graphisch | 4 → 5 (erkennen 4, direkt 1) | 8 → 6 (darstellung 3, mehrschritt 1, umkehr 1, einkleidung 1) | 8 → 8 (begruenden 3, transfer 1, parameter 1, rueckwaerts 1, fehler 1, pruefung 1) |

**gleichungen.lgs2**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| pruefen | 10 → 4 (erkennen 3, direkt 1) | 6 → 6 (mehrschritt 4, umkehr 1, einkleidung 1) | 4 → 8 (transfer 2, parameter 1, rueckwaerts 1, fehler 1, begruenden 1, pruefung 1, verknuepfen 1) |
| grafisch | 10 → 5 (erkennen 4, direkt 1) | 6 → 6 (darstellung 2, mehrschritt 2, einkleidung 1, umkehr 1) | 6 → 8 (fehler 2, verknuepfen 1, rueckwaerts 1, begruenden 1, transfer 1, parameter 1, pruefung 1) |
| einsetzen | 10 → 5 (direkt 4, erkennen 1) | 6 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) | 4 → 8 (begruenden 2, fehler 1, rueckwaerts 1, verknuepfen 1, parameter 1, pruefung 1, transfer 1) |
| gleichsetzen | 10 → 6 (direkt 5, erkennen 1) | 6 → 6 (mehrschritt 3, einkleidung 1, umkehr 1, darstellung 1) | 4 → 8 (transfer 2, begruenden 1, parameter 1, fehler 1, rueckwaerts 1, verknuepfen 1, pruefung 1) |
| addition | 5 → 7 (direkt 6, erkennen 1) | 11 → 8 (mehrschritt 5, einkleidung 1, umkehr 1, darstellung 1) | 4 → 8 (verknuepfen 2, transfer 1, fehler 1, begruenden 1, parameter 1, rueckwaerts 1, pruefung 1) |
| verfahren | 5 → 4 (erkennen 3, direkt 1) | 8 → 6 (mehrschritt 2, einkleidung 2, umkehr 1, darstellung 1) | 7 → 8 (begruenden 3, transfer 1, pruefung 1, parameter 1, verknuepfen 1, fehler 1) |
| loesbarkeit | 4 → 4 (erkennen 3, direkt 1) | 10 → 6 (mehrschritt 3, darstellung 2, einkleidung 1) | 6 → 8 (parameter 3, rueckwaerts 1, begruenden 1, transfer 1, fehler 1, pruefung 1) |
| sachaufgabe | 4 → 4 (direkt 3, erkennen 1) | 10 → 10 (einkleidung 7, mehrschritt 2, umkehr 1) | 6 → 8 (transfer 2, pruefung 1, rueckwaerts 1, begruenden 1, verknuepfen 1, parameter 1, fehler 1) |

**funktionen.grundbegriffe**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| eindeutig | 7 → 4 (erkennen 3, direkt 1) | 9 → 9 (einkleidung 5, umkehr 2, darstellung 2) | 4 → 8 (begruenden 2, transfer 1, fehler 1, parameter 1, rueckwaerts 1, verknuepfen 1, pruefung 1) |
| mengen | 4 → 4 (direkt 3, erkennen 1) | 8 → 7 (mehrschritt 4, einkleidung 2, umkehr 1) | 8 → 8 (begruenden 3, verknuepfen 2, parameter 1, fehler 1, pruefung 1) |
| funktionswert | 4 → 4 (direkt 3, erkennen 1) | 13 → 7 (mehrschritt 4, darstellung 2, einkleidung 1) | 5 → 8 (begruenden 2, parameter 1, rueckwaerts 1, fehler 1, verknuepfen 1, transfer 1, pruefung 1) |
| stelle | 5 → 4 (direkt 3, erkennen 1) | 10 → 7 (mehrschritt 5, einkleidung 1, umkehr 1) | 5 → 8 (verknuepfen 2, begruenden 1, parameter 1, fehler 1, rueckwaerts 1, transfer 1, pruefung 1) |
| wertetabelle | 4 → 5 (direkt 4, erkennen 1) | 8 → 9 (mehrschritt 4, umkehr 3, darstellung 1, einkleidung 1) | 8 → 8 (rueckwaerts 2, parameter 1, transfer 1, fehler 1, begruenden 1, verknuepfen 1, pruefung 1) |
| graph_lesen | 5 → 4 (erkennen 3, direkt 1) | 11 → 6 (mehrschritt 3, umkehr 2, einkleidung 1) | 4 → 8 (transfer 2, parameter 1, fehler 1, begruenden 1, rueckwaerts 1, verknuepfen 1, pruefung 1) |
| nullstellen | 6 → 4 (direkt 3, erkennen 1) | 6 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) | 8 → 8 (verknuepfen 3, transfer 2, pruefung 1, begruenden 1, parameter 1) |
| punkt_graph | 6 → 5 (erkennen 4, direkt 1) | 6 → 6 (mehrschritt 3, umkehr 1, darstellung 1, einkleidung 1) | 8 → 8 (parameter 2, fehler 1, rueckwaerts 1, pruefung 1, verknuepfen 1, transfer 1, begruenden 1) |
| sachzusammenhang | 4 → 4 (erkennen 3, direkt 1) | 6 → 6 (darstellung 3, umkehr 2, mehrschritt 1) | 8 → 10 (transfer 3, begruenden 3, pruefung 2, fehler 1, verknuepfen 1) |

**funktionen.linear**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| ablesen | 7 → 6 (direkt 5, erkennen 1) | 6 → 6 (darstellung 3, mehrschritt 2, einkleidung 1) | 7 → 8 (verknuepfen 3, transfer 1, rueckwaerts 1, parameter 1, fehler 1, begruenden 1) |
| graph_ablesen | 4 → 4 (erkennen 3, direkt 1) | 6 → 7 (darstellung 4, mehrschritt 2, einkleidung 1) | 8 → 8 (transfer 2, verknuepfen 2, begruenden 1, rueckwaerts 1, pruefung 1, fehler 1) |
| zwei_punkte | 6 → 4 (erkennen 2, direkt 2) | 9 → 6 (mehrschritt 4, darstellung 1, einkleidung 1) | 5 → 8 (fehler 3, begruenden 2, transfer 1, parameter 1, rueckwaerts 1) |
| proportional | 4 → 6 (direkt 4, erkennen 2) | 12 → 7 (mehrschritt 3, einkleidung 2, darstellung 2) | 4 → 8 (begruenden 2, fehler 1, transfer 1, parameter 1, rueckwaerts 1, verknuepfen 1, pruefung 1) |
| aufstellen | 4 → 4 (direkt 3, erkennen 1) | 10 → 7 (mehrschritt 3, einkleidung 3, umkehr 1) | 6 → 8 (rueckwaerts 3, transfer 1, verknuepfen 1, pruefung 1, fehler 1, begruenden 1) |
| schnittpunkte | 4 → 4 (direkt 2, erkennen 2) | 12 → 9 (mehrschritt 6, einkleidung 2, umkehr 1) | 4 → 8 (verknuepfen 2, parameter 1, fehler 1, begruenden 1, rueckwaerts 1, transfer 1, pruefung 1) |
| lage | 7 → 5 (erkennen 3, direkt 2) | 9 → 7 (mehrschritt 3, umkehr 3, einkleidung 1) | 4 → 8 (begruenden 2, rueckwaerts 1, parameter 1, verknuepfen 1, fehler 1, transfer 1, pruefung 1) |
| deuten | 5 → 6 (erkennen 5, direkt 1) | 10 → 8 (umkehr 4, einkleidung 3, mehrschritt 1) | 5 → 8 (transfer 2, begruenden 2, rueckwaerts 1, fehler 1, verknuepfen 1, pruefung 1) |

**funktionen.gebrochen**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| indirekt | 4 → 6 (direkt 4, erkennen 2) | 12 → 6 (einkleidung 2, darstellung 2, mehrschritt 1, umkehr 1) | 4 → 8 (verknuepfen 2, fehler 1, transfer 1, pruefung 1, begruenden 1, parameter 1, rueckwaerts 1) |
| indirekt_sach | 4 → 6 (direkt 4, erkennen 2) | 6 → 6 (einkleidung 3, darstellung 1, umkehr 1, mehrschritt 1) | 8 → 8 (transfer 3, verknuepfen 2, pruefung 2, parameter 1) |
| definitionsmenge | 10 → 6 (direkt 3, erkennen 3) | 6 → 7 (mehrschritt 4, darstellung 1, einkleidung 1, umkehr 1) | 4 → 8 (verknuepfen 2, parameter 1, rueckwaerts 1, fehler 1, begruenden 1, transfer 1, pruefung 1) |
| asymptoten | 12 → 7 (direkt 6, erkennen 1) | 5 → 6 (mehrschritt 4, darstellung 1, einkleidung 1) | 5 → 8 (rueckwaerts 2, verknuepfen 1, begruenden 1, parameter 1, fehler 1, transfer 1, pruefung 1) |
| achsenpunkte | 4 → 4 (direkt 3, erkennen 1) | 12 → 8 (mehrschritt 6, einkleidung 1, umkehr 1) | 4 → 8 (begruenden 3, pruefung 1, parameter 1, fehler 1, rueckwaerts 1, verknuepfen 1) |
| parameter | 4 → 4 (direkt 3, erkennen 1) | 12 → 9 (umkehr 4, mehrschritt 3, darstellung 2) | 4 → 8 (transfer 2, rueckwaerts 1, verknuepfen 1, parameter 1, fehler 1, begruenden 1, pruefung 1) |
| beurteilen | 4 → 4 (erkennen 3, direkt 1) | 12 → 6 (umkehr 3, mehrschritt 1, einkleidung 1, darstellung 1) | 4 → 8 (begruenden 2, fehler 1, verknuepfen 1, parameter 1, rueckwaerts 1, transfer 1, pruefung 1) |

**messen.koerper_darstellung**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| prisma | 4 → 5 (direkt 4, erkennen 1) | 8 → 7 (umkehr 4, mehrschritt 2, einkleidung 1) | 8 → 8 (begruenden 2, verknuepfen 2, transfer 2, rueckwaerts 1, pruefung 1) |
| netz | 4 → 6 (erkennen 3, direkt 3) | 8 → 6 (darstellung 2, mehrschritt 2, einkleidung 1, umkehr 1) | 8 → 8 (transfer 3, rueckwaerts 2, begruenden 1, pruefung 1, verknuepfen 1) |
| zylinder | 4 → 4 (erkennen 2, direkt 2) | 8 → 6 (mehrschritt 3, umkehr 2, einkleidung 1) | 8 → 8 (begruenden 2, rueckwaerts 2, verknuepfen 1, transfer 1, pruefung 1, fehler 1) |
| schraegbild | 4 → 4 (erkennen 2, direkt 2) | 11 → 8 (umkehr 4, darstellung 3, mehrschritt 1) | 5 → 8 (verknuepfen 2, transfer 1, fehler 1, pruefung 1, begruenden 1, parameter 1, rueckwaerts 1) |
| ansichten | 5 → 6 (erkennen 5, direkt 1) | 8 → 9 (umkehr 6, darstellung 2, einkleidung 1) | 7 → 8 (verknuepfen 3, transfer 2, rueckwaerts 1, pruefung 1, fehler 1) |
| beurteilen | 8 → 4 (erkennen 3, direkt 1) | 5 → 7 (umkehr 3, mehrschritt 2, einkleidung 1, darstellung 1) | 7 → 8 (begruenden 2, fehler 2, verknuepfen 1, transfer 1, pruefung 1, parameter 1) |

**messen.kreisberechnung**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| umfang | 11 → 9 (direkt 5, erkennen 4) | 7 → 7 (einkleidung 3, umkehr 2, mehrschritt 1, darstellung 1) | 8 → 8 (transfer 3, rueckwaerts 2, begruenden 2, verknuepfen 1) |
| flaeche | 8 → 5 (direkt 4, erkennen 1) | 5 → 6 (umkehr 2, mehrschritt 2, einkleidung 1, darstellung 1) | 7 → 8 (transfer 3, verknuepfen 2, rueckwaerts 1, parameter 1, fehler 1) |
| exakt | 5 → 4 (direkt 3, erkennen 1) | 7 → 6 (umkehr 3, mehrschritt 2, einkleidung 1) | 8 → 8 (verknuepfen 2, pruefung 2, transfer 2, rueckwaerts 1, fehler 1) |
| verstehen | 4 → 6 (direkt 5, erkennen 1) | 8 → 6 (mehrschritt 3, umkehr 1, einkleidung 1, darstellung 1) | 8 → 10 (fehler 3, verknuepfen 2, rueckwaerts 2, transfer 2, pruefung 1) |
| sektor | 4 → 4 (direkt 3, erkennen 1) | 9 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) | 7 → 8 (rueckwaerts 3, transfer 2, verknuepfen 1, pruefung 1, fehler 1) |
| zusammengesetzt | 8 → 4 (direkt 3, erkennen 1) | 4 → 6 (mehrschritt 3, umkehr 1, einkleidung 1, darstellung 1) | 8 → 8 (verknuepfen 3, transfer 3, pruefung 1, rueckwaerts 1) |
| zylinder | 8 → 5 (direkt 4, erkennen 1) | 8 → 7 (mehrschritt 2, umkehr 2, einkleidung 2, darstellung 1) | 4 → 8 (transfer 2, begruenden 1, verknuepfen 1, fehler 1, rueckwaerts 1, parameter 1, pruefung 1) |

**messen.prisma_zylinder**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| prisma_volumen | 4 → 6 (direkt 5, erkennen 1) | 6 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) | 8 → 8 (transfer 2, begruenden 2, rueckwaerts 1, pruefung 1, fehler 1, verknuepfen 1) |
| prisma_oberflaeche | 4 → 5 (direkt 4, erkennen 1) | 6 → 6 (mehrschritt 3, einkleidung 2, darstellung 1) | 8 → 8 (transfer 3, verknuepfen 2, pruefung 1, begruenden 1, rueckwaerts 1) |
| prisma_umstellen | 4 → 7 (direkt 6, erkennen 1) | 6 → 7 (einkleidung 3, mehrschritt 2, umkehr 1, darstellung 1) | 8 → 8 (transfer 2, verknuepfen 2, rueckwaerts 2, pruefung 1, fehler 1) |
| zylinder_volumen | 4 → 5 (direkt 4, erkennen 1) | 6 → 7 (mehrschritt 3, darstellung 2, einkleidung 1, umkehr 1) | 8 → 8 (transfer 2, begruenden 2, rueckwaerts 1, parameter 1, verknuepfen 1, fehler 1) |
| zylinder_oberflaeche | 4 → 5 (direkt 4, erkennen 1) | 6 → 9 (einkleidung 3, mehrschritt 3, darstellung 2, umkehr 1) | 8 → 8 (rueckwaerts 2, begruenden 2, transfer 1, fehler 1, parameter 1, pruefung 1) |
| sach | 4 → 5 (direkt 4, erkennen 1) | 6 → 7 (mehrschritt 3, einkleidung 3, umkehr 1) | 8 → 8 (transfer 3, verknuepfen 2, pruefung 2, rueckwaerts 1) |
| verstehen | 4 → 4 (direkt 3, erkennen 1) | 6 → 6 (mehrschritt 4, einkleidung 1, umkehr 1) | 8 → 10 (verknuepfen 3, fehler 2, transfer 2, begruenden 2, pruefung 1) |

**stochastik.grundbegriffe**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| begriffe | 4 → 5 (direkt 4, erkennen 1) | 8 → 8 (darstellung 5, mehrschritt 2, einkleidung 1) | 8 → 9 (verknuepfen 2, begruenden 2, transfer 2, rueckwaerts 1, pruefung 1, parameter 1) |
| rel_haeufigkeit | 4 → 5 (direkt 3, erkennen 2) | 8 → 8 (darstellung 4, umkehr 3, einkleidung 1) | 8 → 8 (verknuepfen 3, rueckwaerts 2, fehler 1, pruefung 1, begruenden 1) |
| laplace | 4 → 5 (direkt 4, erkennen 1) | 8 → 8 (mehrschritt 5, einkleidung 2, umkehr 1) | 8 → 8 (rueckwaerts 2, transfer 2, pruefung 1, begruenden 1, verknuepfen 1, fehler 1) |
| laplace_pruefen | 7 → 8 (erkennen 7, direkt 1) | 9 → 6 (mehrschritt 3, einkleidung 1, umkehr 1, darstellung 1) | 4 → 8 (begruenden 2, fehler 1, transfer 1, verknuepfen 1, parameter 1, rueckwaerts 1, pruefung 1) |
| gegenereignis | 9 → 7 (direkt 6, erkennen 1) | 5 → 7 (mehrschritt 3, darstellung 2, einkleidung 1, umkehr 1) | 6 → 8 (transfer 3, verknuepfen 2, parameter 1, fehler 1, begruenden 1) |
| grosse_zahlen | 5 → 5 (direkt 4, erkennen 1) | 7 → 6 (mehrschritt 2, umkehr 2, einkleidung 1, darstellung 1) | 8 → 8 (begruenden 2, transfer 2, verknuepfen 1, pruefung 1, fehler 1, rueckwaerts 1) |

**groessen.indirekt**

| Lernkarte | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher |
|---|---|---|---|
| erkennen | 5 → 6 (erkennen 5, direkt 1) | 9 → 7 (mehrschritt 4, einkleidung 2, darstellung 1) | 9 → 9 (begruenden 3, transfer 2, pruefung 2, verknuepfen 1, parameter 1) |
| vervielfachen | 5 → 6 (direkt 5, erkennen 1) | 13 → 13 (mehrschritt 6, umkehr 4, einkleidung 3) | 5 → 8 (verknuepfen 2, transfer 1, rueckwaerts 1, parameter 1, fehler 1, begruenden 1, pruefung 1) |
| produkt | 5 → 4 (direkt 2, erkennen 2) | 9 → 6 (mehrschritt 3, darstellung 2, umkehr 1) | 9 → 9 (verknuepfen 2, fehler 2, rueckwaerts 2, transfer 2, parameter 1) |
| dreisatz | 5 → 6 (direkt 5, erkennen 1) | 9 → 7 (mehrschritt 5, darstellung 1, umkehr 1) | 9 → 9 (rueckwaerts 3, fehler 2, transfer 2, verknuepfen 1, pruefung 1) |
| graph | 6 → 6 (direkt 5, erkennen 1) | 12 → 6 (darstellung 3, einkleidung 2, mehrschritt 1) | 5 → 8 (verknuepfen 2, begruenden 1, pruefung 1, parameter 1, fehler 1, rueckwaerts 1, transfer 1) |
| unterscheiden | 9 → 4 (direkt 2, erkennen 2) | 9 → 7 (mehrschritt 3, darstellung 3, umkehr 1) | 7 → 8 (fehler 2, transfer 2, verknuepfen 1, pruefung 1, begruenden 1, rueckwaerts 1) |
| sach | 5 → 6 (direkt 5, erkennen 1) | 11 → 12 (einkleidung 8, mehrschritt 3, umkehr 1) | 7 → 8 (fehler 3, transfer 2, rueckwaerts 1, verknuepfen 1, pruefung 1) |

### (3) Zahlen

| Thema | neue Übungen | Knobel-Bordkarten | umgestuft | überzählig |
|---|---|---|---|---|
| gleichungen.ungleichungen | 38 | 14 | 13 | 31 |
| zahlen.intervalle | 25 | 8 | 23 | 27 |
| terme.bruchterme | 39 | 14 | 19 | 48 |
| gleichungen.formeln | 23 | 10 | 11 | 24 |
| gleichungen.bruch | 45 | 14 | 21 | 52 |
| gleichungen.lgs2 | 53 | 16 | 21 | 58 |
| funktionen.grundbegriffe | 38 | 18 | 14 | 43 |
| funktionen.linear | 30 | 16 | 13 | 28 |
| funktionen.gebrochen | 36 | 14 | 13 | 35 |
| messen.koerper_darstellung | 19 | 12 | 8 | 19 |
| messen.kreisberechnung | 21 | 14 | 6 | 28 |
| messen.prisma_zylinder | 17 | 14 | 10 | 0 |
| stochastik.grundbegriffe | 20 | 12 | 0 | 13 |
| groessen.indirekt | 16 | 14 | 1 | 24 |
| **Summe** | **420** | **190** | **173** | **430** |

### (4) Überzählig (Wortlaut; ohne `g`, nicht gelöscht)

**gleichungen.ungleichungen**

- `umformen` S2: Löse die Ungleichung 3x − 3 < −3.
- `umformen` S2: Löse 8x + 1 > 4x + 13. Die Lösung hat die Form x > □. Gib die Zahl an.
- `umformen` S2: Löse 7x − 3 ≤ 4x + 9. Die Lösung hat die Form x ≤ □. Gib die Zahl an.
- `umformen` S2: Löse die Ungleichung 7x − 11 ≤ 4x + 16.
- `umformen` S2: Löse 0,5x − 3 ≥ 1. Die Lösung hat die Form x ≥ □. Gib die Zahl an.
- `umformen` S2: Löse x/3 + 2 < 5. Die Lösung hat die Form x < □. Gib die Zahl an.
- `umdrehen` S2: Löse x + 15 ≥ 3x + 33. Die Lösung hat die Form x ≤ □. Gib die Zahl an.
- `umdrehen` S2: Löse 4x + 15 > 6x − 9. Die Lösung hat die Form x < □. Gib die Zahl an.
- `umdrehen` S2: Löse 6x + 12 > 11x − 33. Die Lösung hat die Form x < □. Gib die Zahl an.
- `umdrehen` S2: Löse 6 − 2x > 0. Die Lösung hat die Form x < □. Gib die Zahl an.
- `umdrehen` S2: Löse −x/4 ≥ 2. Die Lösung hat die Form x ≤ □. Gib die Zahl an.
- `klammern` S1: Löse die Ungleichung 2(x + 4) > 12.
- `klammern` S1: Löse die Ungleichung 5(x − 5) < −40.
- `klammern` S2: Löse 3(x − 4) − 4(x − 5) ≤ −3x + 14. Die Lösung hat die Form x ≤ □. Gib die Zahl an.
- `klammern` S2: Löse 4(x + 1) − 2(x + 4) > 3x − 2. Die Lösung hat die Form x < □. Gib die Zahl an.
- `klammern` S2: Löse die Ungleichung −3(x − 1) − 5(x + 3) < −3x − 7.
- `klammern` S2: Löse 3(2 − x) ≤ 12. Die Lösung hat die Form x ≥ □. Gib die Zahl an.
- `klammern` S2: Löse −(x − 5) > 2x − 4. Die Lösung hat die Form x < □. Gib die Zahl an.
- `intervall` S2: Löse −3x + 6 ≤ −12 und gib die Lösungsmenge als Intervall an.
- `intervall` S3: Löse −21 ≤ 5x + 9 < 14 und gib die Lösungsmenge als Intervall an.
- `intervall` S2: Löse 5 − x > 7 und gib die Lösungsmenge als Intervall an.
- `intervall` S3: Löse −3 ≤ 1 − 2x < 5 und gib die Lösungsmenge als Intervall an.
- `pruefen` S2: Gib die kleinste ganze Zahl an, die 3x − 10 > 4 erfüllt.
- `pruefen` S3: Jemand löst −6x + 11 > 17 so: − 11 ergibt −6x > 6; durch (−6) ergibt x < 1. Was stimmt?
- `pruefen` S3: Jemand löst −4x + 9 > −3 so: − 9 ergibt −4x > −12; durch (−4) ergibt x < −3. Was stimmt?
- `pruefen` S1: Welche Zahl ist eine Lösung von −2x + 3 > 10?
- `pruefen` S2: Gib die kleinste ganze Zahl an, die 2,5x − 1 ≥ 6 erfüllt.
- `grafisch` S2: Löse −2x − 2 > 3x + 3 mit den Graphen. Die Lösung hat die Form x < □. Gib die Zahl an.
- `grafisch` S2: Löse x − 1 < −x + 3 mit den Graphen. Die Lösung hat die Form x < □. Gib die Zahl an.
- `sachaufgabe` S1: Ein Aufzug darf höchstens 400 kg tragen. Eine Person (69 kg) will Kisten zu je 50 kg mitnehmen. Wie viele Kisten darf sie höchstens einladen?
- `sachaufgabe` S1: Ein Handytarif kostet im Monat 12 € Grundgebühr und 2 € je zusätzliches Datenpaket. Man will höchstens 40 € zahlen. Wie viele Datenpakete kann man höchstens kaufen?

**zahlen.intervalle**

- `lesen` S1: Was bedeutet das Intervall ]−6; −3]?
- `lesen` S1: Welches Intervall zeigt das Bild? (Gefüllter Punkt: Grenze gehört dazu. Leerer Kreis: gehört nicht dazu. Strecke bis zum Rand: unbegrenzt.)
- `lesen` S1: Welches Intervall zeigt das Bild? (Gefüllter Punkt: Grenze gehört dazu. Leerer Kreis: gehört nicht dazu. Strecke bis zum Rand: unbegrenzt.)
- `lesen` S1: Welches Intervall zeigt das Bild? (Gefüllter Punkt: Grenze gehört dazu. Leerer Kreis: gehört nicht dazu. Strecke bis zum Rand: unbegrenzt.)
- `lesen` S1: Was bedeutet das Intervall ]−∞; 2,5]?
- `lesen` S1: Was bedeutet das Intervall [−1,5; 0[?
- `schreiben` S1: Schreibe x > −9 als Intervall.
- `schreiben` S1: Schreibe x ≤ 5 als Intervall.
- `schreiben` S1: Schreibe x ≥ −3 als Intervall.
- `schreiben` S1: Schreibe x > 6 als Intervall.
- `schreiben` S1: Schreibe x ≥ −8 als Intervall.
- `schreiben` S1: Schreibe x ≥ 7 als Intervall.
- `schreiben` S1: Schreibe −4 ≤ x < −1,5 als Intervall.
- `enthalten` S1: Welche Zahl liegt im Intervall [−9; −1[?
- `enthalten` S2: Wie viele ganze Zahlen liegen im Intervall [−9; 8]?
- `enthalten` S2: Wie viele ganze Zahlen liegen im Intervall ]3; 8[?
- `enthalten` S2: Wie viele ganze Zahlen liegen im Intervall ]−5; −3[?
- `enthalten` S2: Wie viele ganze Zahlen liegen im Intervall ]−2,5; 3,5]?
- `beurteilen` S1: Welche Aussage über [4; 7[ ist richtig?
- `beurteilen` S1: Welche Aussage über [4; 7] ist richtig?
- `beurteilen` S2: Welche Aussage über [−5; −2] ist FALSCH?
- `beurteilen` S2: Welche Aussage über ]−9; −7] ist FALSCH?
- `beurteilen` S2: Welche Aussage über ]−7; 6[ ist FALSCH?
- `beurteilen` S2: Welche Aussage über ]−5; 0] ist FALSCH?
- `beurteilen` S2: Welche Aussage über [−3; 9] ist FALSCH?
- `beurteilen` S2: Welche Aussage über [−8; 3[ ist FALSCH?
- `beurteilen` S1: Welche Aussage über ]2; 3[ ist richtig?

**terme.bruchterme**

- `definitionsmenge` S2: Für welche Zahl ist der Term 6/(9 − 3x) nicht definiert?
- `definitionsmenge` S3: Gib die Definitionsmenge von (x + 2)/(x² − 4x) an.
- `definitionsmenge` S3: Gib die Definitionsmenge von x/(2x + 1) : (x − 3)/x an.
- `termwert` S1: Berechne T(−3) für T(x) = x/(x + 2).
- `termwert` S1: Berechne T(6) für T(x) = (−2x + 9)/(3x − 3).
- `termwert` S1: Berechne T(4) für T(x) = (4x + 2)/(x + 4).
- `termwert` S1: Berechne T(−6) für T(x) = (−x + 9)/(x + 2).
- `termwert` S2: Berechne T(4) für T(x) = (−x − 6)/(−x − 2). Gib das Ergebnis als vollständig gekürzten Bruch an.
- `termwert` S1: Berechne T(−3) für T(x) = (x² − 1)/(x + 2).
- `termwert` S1: Berechne T(0,5) für T(x) = (2x + 3)/(4x).
- `termwert` S2: Für welches x hat T(x) = (x + 1)/(x − 1) den Wert −1?
- `kuerzen` S1: Kürze vollständig: 16x²/(4x³)
- `kuerzen` S2: Kürze vollständig: (2x − 10)/(8x − 40)
- `kuerzen` S2: Kürze vollständig: (3x − 18)/(2x − 12)
- `kuerzen` S3: Kürze vollständig: (x² − 49)/(x + 7)
- `kuerzen` S3: Kürze vollständig: 12x²y/(18xy²)
- `kuerzen` S2: Kürze vollständig: (6x + 4)/(9x + 6)
- `kuerzen` S3: Kürze vollständig: (3x² + 9x)/(6x)
- `kuerzen` S3: Kürze vollständig: (x − 4)/(4 − x)
- `kuerzen` S3: Kürze vollständig: (x² + 6x + 9)/(2x + 6)
- `erweitern` S1: Erweitere 5/(2x) auf den Nenner 4x². Gib den neuen Zähler ein.
- `erweitern` S1: Erweitere 7/(5x) auf den Nenner 25x². Gib den neuen Zähler ein.
- `erweitern` S2: Mit welchem Term wurde 4/(2x) erweitert, wenn der neue Nenner 4x³ ist?
- `erweitern` S2: Mit welchem Term wurde 2/(4x) erweitert, wenn der neue Nenner 8x³ ist?
- `erweitern` S2: Mit welchem Term wurde (x + 1)/3 erweitert, wenn der neue Nenner 6x ist?
- `addieren` S1: Fasse zusammen: 9/(x + 6) + 1/(x + 6)
- `addieren` S2: Fasse zusammen: 8/x − 7/(2x)
- `addieren` S2: Fasse zusammen: 9/x + 8/(2x)
- `addieren` S2: Fasse zusammen: 4/x − 8/(3x)
- `addieren` S2: Fasse zusammen: (5x − 7)/x − (2x + 1)/x
- `addieren` S2: Fasse zusammen: (5x + 5)/(x + 1) − (4x − 1)/(x + 1)
- `addieren` S2: Fasse zusammen: 3/(2x) + 1/(4x)
- `multiplizieren` S2: Berechne und kürze: (7x³/4) : (5/(4x))
- `multiplizieren` S2: Berechne und kürze: (7/(9x³)) : (7x/9)
- `multiplizieren` S2: Berechne und kürze: (5x/9) : (9/(7x³))
- `multiplizieren` S2: Berechne und kürze: (6x + 12)/x · x²/(x + 2)
- `multiplizieren` S2: Berechne und kürze: (3x + 18)/x · x²/(x + 6)
- `multiplizieren` S2: Berechne und kürze: (2x/3) · (9/(4x²))
- `multiplizieren` S2: Berechne und kürze: (x + 1)/x : (x + 1)/x²
- `multiplizieren` S2: Berechne und kürze: 2x : (4/x)
- `fehler_finden` S1: Welche Umformung ist richtig (für alle x aus D)?
- `fehler_finden` S1: Welche Umformung ist richtig (für alle x aus D)?
- `fehler_finden` S1: Welche Umformung ist richtig (für alle x aus D)?
- `fehler_finden` S2: Welche Umformung ist FALSCH?
- `fehler_finden` S2: Welche Umformung ist FALSCH?
- `fehler_finden` S2: Welche Umformung ist FALSCH?
- `fehler_finden` S2: Welche Umformung ist FALSCH?
- `fehler_finden` S1: Welche Umformung ist richtig (für alle x aus D)?

**gleichungen.formeln**

- `ein_schritt` S1: Stelle V = G · h nach G um.
- `ein_schritt` S1: Stelle u = 4 · a nach a um.
- `ein_schritt` S1: Stelle d = 2 · r nach r um.
- `ein_schritt` S1: Stelle P = U · I nach I um.
- `ein_schritt` S1: Stelle m = ρ · V nach ρ um.
- `zwei_schritte` S1: Stelle A = g · h : 2 nach h um.
- `zwei_schritte` S2: Stelle y = m · x + t nach x um.
- `zwei_schritte` S2: Stelle u = 2 · (a + b) nach a um.
- `zwei_schritte` S2: Stelle u = 2 · (l + b) nach b um.
- `zwei_schritte` S2: Stelle K = 5 + 0,2 · x nach x um.
- `pruefen` S1: Jemand stellt ρ = m : V nach V um und erhält V = ρ : m. Stimmt das?
- `pruefen` S2: Jemand stellt y = m · x + t nach t um und erhält t = y − m · x. Stimmt das?
- `pruefen` S2: Jemand stellt F = 1,8 · C + 32 nach C um und erhält C = F : 1,8 − 32. Stimmt das?
- `pruefen` S1: Jemand stellt ρ = m : V nach V um und erhält V = m · ρ. Stimmt das?
- `pruefen` S2: Jemand stellt V = G · h : 3 nach h um und erhält h = V : G. Stimmt das?
- `pruefen` S2: Jemand stellt A = (a + c) · h : 2 nach a um und erhält a = 2 · A : (h − c). Stimmt das?
- `pruefen` S2: Jemand stellt Z = K · p : 100 nach K um und erhält K = 100 · Z : p. Stimmt das?
- `pruefen` S2: Jemand stellt V = G · h : 3 nach h um und erhält h = V : (3 · G). Stimmt das?
- `pruefen` S1: Jemand stellt U = R · I nach R um und erhält R = U : I. Stimmt das?
- `pruefen` S2: Jemand stellt s = v · t + 5 nach t um und erhält t = s : v − 5. Stimmt das?
- `einsetzen` S1: Ein Fahrzeug legt 75 km mit der Durchschnittsgeschwindigkeit 50 km/h zurück. Wie lange braucht es? (v = s : t)
- `geometrie` S1: Ein Parallelogramm hat A = 196 cm² und die Grundseite g = 14 cm. Berechne die Höhe h.
- `geometrie` S2: Ein Prisma hat das Volumen 495 cm³ und die Grundfläche G = 33 cm². Wie hoch ist es?
- `geometrie` S2: Ein Quader hat das Volumen 1144 cm³, die Länge 11 cm und die Breite 8 cm. Wie hoch ist er?

**gleichungen.bruch**

- `definitionsmenge` S1: Bestimme die Definitionsmenge von 5/(x + 3) = 3.
- `definitionsmenge` S2: Bestimme die Definitionsmenge von 8/(x − 3) = 2/(x − 1).
- `definitionsmenge` S2: Bestimme die Definitionsmenge von 1/(x + 6) = 3/(x − 3).
- `definitionsmenge` S2: Bestimme die Definitionsmenge von 3/(x + 7) = 4/(x − 9).
- `definitionsmenge` S3: Bestimme die Definitionsmenge von 3/(5x − 10) = 7/(x(x − 6)).
- `definitionsmenge` S2: Bestimme die Definitionsmenge von 3/(2x − 1) = 1/x.
- `definitionsmenge` S2: Bestimme die Definitionsmenge von 5/x − 2/(x − 5) = 1/(3x).
- `definitionsmenge` S3: Bestimme die Definitionsmenge von 1/(x² − 2x) = 4/(x − 2).
- `ein_bruch` S1: Löse −2 = 16/x.
- `ein_bruch` S2: Löse −4 = 24/(x + 2).
- `ein_bruch` S2: Löse 36/(3x) = 4.
- `ein_bruch` S2: Löse 2 = 10/(x + 3).
- `ein_bruch` S2: Löse (x − 3)/(x + 7) = −3.
- `ein_bruch` S2: Löse (x + 3)/(x − 9) = 3.
- `ein_bruch` S2: Löse (3x + 5)/(x − 3) = −1.
- `ein_bruch` S2: Löse (x + 3)/(x + 7) = 3.
- `ein_bruch` S2: Löse 15/(2x) = 6.
- `ein_bruch` S2: Löse 7/(x − 1) = −0,5.
- `ueber_kreuz` S1: Löse 5/x = 3/(x − 1).
- `ueber_kreuz` S1: Löse 3/x = 2/(x − 3).
- `ueber_kreuz` S2: Löse 4/(x − 4) = 2/(x − 6).
- `ueber_kreuz` S2: Löse 7/(x − 2) = 8/(x + 3).
- `ueber_kreuz` S2: Löse 2/(x + 9) = 4/(x + 1).
- `ueber_kreuz` S3: Löse (x + 5)/(x + 1) = (x − 8)/(x − 7).
- `ueber_kreuz` S2: Löse 3/(2x) = 5/(x + 7).
- `ueber_kreuz` S2: Löse (x + 1)/4 = (x − 2)/3.
- `hauptnenner` S1: Löse 1/x + 1/x = 5.
- `hauptnenner` S1: Löse 10/x + 12/x = 1.
- `hauptnenner` S2: Löse 5/x + 6/(3x) = −1.
- `hauptnenner` S2: Löse 2/x − 7/(2x) = 4.
- `hauptnenner` S2: Löse 7/x − 7/(5x) = 1.
- `hauptnenner` S2: Löse 1/2 + 1/x = 5/6.
- `hauptnenner` S2: Löse 4/x − 1 = 3/x.
- `hauptnenner` S3: Löse 2/(x − 3) − 1/x = 6/(x(x − 3)).
- `scheinloesung` S2: Gib die Lösungsmenge von (x − 6)/(x + 2) = −10/(x + 2) an.
- `scheinloesung` S2: Gib die Lösungsmenge von (x + 5)/(x + 4) = −1/(x + 4) an.
- `scheinloesung` S2: Gib die Lösungsmenge von (x − 7)/(x − 5) = 6/(x − 5) an.
- `scheinloesung` S2: Gib die Lösungsmenge von (x + 1)/(x − 6) = 3/(x − 6) an.
- `scheinloesung` S2: Gib die Lösungsmenge von (x + 7)/(x + 6) = 1/(x + 6) an.
- `scheinloesung` S2: Gib die Lösungsmenge von (x − 6)/(x − 7) = 1/(x − 7) an.
- `scheinloesung` S3: Warum ist x = 2 keine Lösung von (x − 8)/(x − 2) = −6/(x − 2), obwohl die Rechnung x = 2 ergibt?
- `scheinloesung` S2: Gib die Lösungsmenge von 6/(x − 2) = 3/(x − 2) + 3 an.
- `verhaeltnis` S1: Löse die Verhältnisgleichung x : 11 = 6 : 10.
- `verhaeltnis` S1: Löse die Verhältnisgleichung x : 2 = 11 : 10.
- `verhaeltnis` S1: Löse die Verhältnisgleichung 12 : x = 3 : 3.
- `verhaeltnis` S2: Löse die Verhältnisgleichung 5 : x = 10 : 6.
- `verhaeltnis` S1: Löse die Verhältnisgleichung x : 2,5 = 6 : 5.
- `graphisch` S1: Lies die Lösung von −8/(x + 3) = −2 am Schnittpunkt ab.
- `graphisch` S2: Löse −8/x = x − 6 mit den Graphen.
- `graphisch` S2: Löse 12/x = x + 1 mit den Graphen.
- `graphisch` S3: Wie viele Lösungen hat die Gleichung 4/x − 2 = x − 2? Entscheide am Bild.
- `graphisch` S3: Wie viele Lösungen hat die Gleichung 1/x = −x? Entscheide am Bild.

**gleichungen.lgs2**

- `pruefen` S1: Gegeben: I: −x + 6y = −17   II: −6x + 2y = −34. Welches Zahlenpaar ist die Lösung?
- `pruefen` S1: Gegeben: I: −4x − 3y = −15   II: −x + 4y = 20. Welches Zahlenpaar ist die Lösung?
- `pruefen` S1: Gegeben: I: −5x + 6y = 16   II: x + y = 10. Welches Zahlenpaar ist die Lösung?
- `pruefen` S1: Gegeben: I: 2x − 6y = 20   II: 2x − 3y = 8. Welches Zahlenpaar ist die Lösung?
- `pruefen` S1: Gegeben: I: 4x − y = 24   II: 4x − 4y = 24. Welches Zahlenpaar ist die Lösung?
- `pruefen` S1: Gegeben: I: −6x − 4y = −38   II: 5x − 6y = 13. Welches Zahlenpaar ist die Lösung?
- `pruefen` S1: Gegeben: I: −x − 3y = −2   II: 2x + y = 4. Welches Zahlenpaar ist die Lösung?
- `pruefen` S2: Gegeben: I: x − 2y = −13   II: 5x − y = −11. Ist (6 | −1) eine Lösung?
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: −x + y = 5   II: y = −2x + 5 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: y = −3x − 1   II: y = −x + 1 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: x + y = 0   II: −2x + y = 3 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: −x + 2y = 2   II: −3x + y = −4 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: y = −x + 4   II: y = 2x + 4 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: −2x + y = 5   II: y = 3x + 5 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: y = 3x − 1   II: 2x + y = 4 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: −2x + y = −3   II: y = x − 3 am Schnittpunkt ab.
- `grafisch` S1: Lies die Lösung des Gleichungssystems I: y = x − 2   II: y = −x am Schnittpunkt ab.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = 4x   II: 2x − y = −14. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = x + 2   II: 6x + y = −5. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = −x + 7   II: 4x − 3y = −49. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = 5x + 2   II: x − 2y = 23. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = −2x − 9   II: −x − 4y = 57. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = −x + 3   II: −2x + 4y = −6. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = 5x − 1   II: x + 4y = 59. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = −4x − 7   II: −3x + 2y = −91. Gib die Lösung an.
- `einsetzen` S1: Löse mit dem Einsetzungsverfahren: I: y = 0,5x + 1   II: 2x − 2y = 4. Gib die Lösung an.
- `gleichsetzen` S1: Löse mit dem Gleichsetzungsverfahren: I: y = −x − 3   II: y = x − 11. Gib die Lösung an.
- `gleichsetzen` S1: Löse mit dem Gleichsetzungsverfahren: I: y = −2x + 5   II: y = 5x − 30. Gib die Lösung an.
- `gleichsetzen` S1: Löse mit dem Gleichsetzungsverfahren: I: y = x − 8   II: y = 4x + 10. Gib die Lösung an.
- `gleichsetzen` S1: Löse mit dem Gleichsetzungsverfahren: I: y = −4x − 4   II: y = x − 19. Gib die Lösung an.
- `gleichsetzen` S1: Löse mit dem Gleichsetzungsverfahren: I: y = −5x + 3   II: y = 2x + 24. Gib die Lösung an.
- `gleichsetzen` S2: Löse mit dem Gleichsetzungsverfahren: I: y = −x + 1   II: −2x + 2y = 18. Gib die Lösung an.
- `gleichsetzen` S2: Löse mit dem Gleichsetzungsverfahren: I: x = 3y − 1   II: x = y + 5. Gib die Lösung an.
- `gleichsetzen` S1: Löse mit dem Gleichsetzungsverfahren: I: y = 0,5x + 3   II: y = −0,5x + 1. Gib die Lösung an.
- `addition` S2: Löse mit dem Additionsverfahren: I: 4x − 4y = 4   II: 3x − 2y = 6. Gib die Lösung an.
- `addition` S2: Löse mit dem Additionsverfahren: I: −4x − 3y = 11   II: −2x + y = −7. Gib die Lösung an.
- `addition` S2: Löse mit dem Additionsverfahren: I: −6x + 2y = 2   II: 3x + y = −5. Gib die Lösung an.
- `addition` S2: Löse mit dem Additionsverfahren: I: −6x + 3y = 24   II: −3x − 2y = −9. Gib die Lösung an.
- `addition` S2: Löse mit dem Additionsverfahren: I: 6x − 6y = 18   II: 6x − y = −2. Gib die Lösung an.
- `addition` S2: Löse mit dem Additionsverfahren: I: 2x + 3y = 12   II: 2x − y = 4. Gib die Lösung an.
- `addition` S2: Löse mit dem Additionsverfahren: I: 3x + 2y = 7   II: x − 2y = 5. Gib die Lösung an.
- `verfahren` S1: Welches Verfahren ist für I: y = −3x + 11   II: y = 3x − 1 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: y = −4x − 3   II: −2x + y = 9 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: x = 2y − 2   II: x = −4y − 2 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: x = 3y + 10   II: x = 2y + 7 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: −5x + 4y = 14   II: 3x − 2y = −8 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: y = 4x − 17   II: y = x − 2 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: 5x + 2y = −9   II: −4x − 2y = 6 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: 3x + 10y = 5   II: 2x − 5y = −20 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: x = 4 − 2y   II: 3x + y = 7 am geschicktesten?
- `verfahren` S1: Welches Verfahren ist für I: 2x + y = 5   II: 2x − 3y = 1 am geschicktesten?
- `loesbarkeit` S2: Wie viele Lösungen hat I: 6x − 4y = 7   II: −19x + 12y = 7?
- `loesbarkeit` S2: Wie viele Lösungen hat I: −6x − 2y = −9   II: 6x + 2y = 10?
- `loesbarkeit` S2: Wie viele Lösungen hat I: −5x + 3y = 12   II: 10x − 6y = −24?
- `loesbarkeit` S2: Wie viele Lösungen hat I: −3x − y = 5   II: 5x + 2y = 2?
- `loesbarkeit` S2: Wie viele Lösungen hat I: x − y = 2   II: y − x = −2?
- `loesbarkeit` S2: Wie viele Lösungen hat I: y = 0,5x + 1   II: x − 2y = 4?
- `sachaufgabe` S2: Eine Eintrittskarte kostet für Erwachsene 15 €, für Kinder 8 €. Eine Gruppe aus 45 Personen zahlt 563 €. Wie viele Kinder sind dabei?

**funktionen.grundbegriffe**

- `eindeutig` S1: Ist die Zuordnung (8 | −5), (0 | 0), (−1 | 8), (2 | −1), (9 | 4), (7 | 9) eine Funktion?
- `eindeutig` S1: Ist die Zuordnung (8 | 9), (−5 | 1), (4 | 0), (0 | −7), (5 | 6), (0 | −4), (−3 | 9) eine Funktion?
- `eindeutig` S1: Ist die Zuordnung (0 | 4), (7 | 5), (3 | 1), (6 | −4), (−3 | 3), (−6 | −3) eine Funktion?
- `eindeutig` S1: Ist die Zuordnung (3 | −1), (4 | 0), (−6 | 0), (2 | 7) eine Funktion?
- `mengen` S1: Gib die maximale Definitionsmenge von f(x) = 1/(x + 1) an.
- `mengen` S2: f(x) = x² − 3 mit D = {−3; 0; 2}. Gib die Wertemenge W an.
- `mengen` S2: f(x) = −3x + 4 mit D = {−1; 0; 1; 3}. Gib die Wertemenge W an.
- `mengen` S2: f(x) = −x² + 5x − 8 mit D = {−3; −1; 2; 3}. Gib die Wertemenge W an.
- `funktionswert` S1: Berechne f(5) für f(x) = −3x + 7.
- `funktionswert` S2: Berechne f(−6) für f(x) = −2x² + 4x + 4.
- `funktionswert` S2: Berechne f(4) für f(x) = 3x² − 4x + 5.
- `funktionswert` S2: Berechne f(−2) für f(x) = x² + x + 9.
- `funktionswert` S2: Berechne f(−2) für f(x) = −x² + x.
- `funktionswert` S2: Berechne f(−4) für f(x) = 3x + 5,5.
- `funktionswert` S2: Berechne f(6) für f(x) = 2/(x − 5).
- `funktionswert` S2: Berechne f(−0,5) für f(x) = 2,5x − 5.
- `funktionswert` S2: Berechne f(−1,5) für f(x) = 2x² − x.
- `funktionswert` S2: Berechne f(0,5) für f(x) = 4/x − 2x.
- `stelle` S1: Für welches x gilt f(x) = −25, wenn f(x) = −3x + 2?
- `stelle` S1: Für welches x gilt f(x) = −3,5, wenn f(x) = x − 8?
- `stelle` S2: Für welches x ist f(x) = 4, wenn f(x) = 2/x?
- `stelle` S2: Für welches x gilt f(x) = 21, wenn f(x) = 2,5x − 9?
- `stelle` S1: Für welches x gilt f(x) = −33, wenn f(x) = 3x − 3?
- `stelle` S2: Für welches x gilt f(x) = 0,5, wenn f(x) = 3/x?
- `stelle` S2: Für welches x gilt f(x) = −7, wenn f(x) = 5 − 4x?
- `wertetabelle` S3: Welcher Funktionsterm passt zur Wertetabelle (−3 | −4), (−2 | −3), (3 | 2)?
- `wertetabelle` S3: Welcher Funktionsterm passt zur Wertetabelle (−2 | 1), (−1 | 3), (1 | 7)?
- `wertetabelle` S2: Die Tabelle gehört zu f(x) = −x² + 2x. Welcher Wert gehört an die Stelle „?“?
- `graph_lesen` S1: Lies am Graphen ab: f(2) = ?
- `graph_lesen` S1: Lies am Graphen ab: f(2) = ?
- `graph_lesen` S1: Lies am Graphen ab: f(−2) = ?
- `graph_lesen` S1: Lies am Graphen ab: f(3) = ?
- `graph_lesen` S1: Lies am Graphen ab: f(1) = ?
- `graph_lesen` S2: Lies am Graphen ab: An welcher Stelle hat f den Wert −1? Gib den Punkt an.
- `graph_lesen` S1: Lies am Graphen ab: f(−2) = ?
- `graph_lesen` S2: Lies am Graphen ab: An welcher Stelle hat f den Wert 2? Gib den Punkt an.
- `nullstellen` S1: Berechne die Nullstelle von f(x) = 5x + 15.
- `nullstellen` S1: Berechne die Nullstelle von f(x) = −6x + 18.
- `nullstellen` S1: Berechne die Nullstelle von f(x) = 2x + 6.
- `nullstellen` S2: Welche Nullstellen hat f(x) = (x − 3)(x − 2)?
- `punkt_graph` S1: Welcher Punkt liegt auf dem Graphen von f(x) = 6x − 6?
- `punkt_graph` S1: Welcher Punkt liegt auf dem Graphen von f(x) = −2x − 7?
- `punkt_graph` S1: Welcher Punkt liegt auf dem Graphen von f(x) = 5x + 2?

**funktionen.linear**

- `ablesen` S1: Gib den y-Achsenabschnitt t der Geraden y = −2x − 7 an.
- `ablesen` S1: Gib den y-Achsenabschnitt t der Geraden y = 7 − 0,5x an.
- `ablesen` S3: Gib den y-Achsenabschnitt t der Geraden x − 2y = 6 an.
- `zwei_punkte` S1: Berechne die Steigung der Geraden durch P(−3 | −2) und Q(−5 | −12).
- `zwei_punkte` S1: Berechne die Steigung der Geraden durch P(3 | 3) und Q(5 | 11).
- `zwei_punkte` S1: Berechne die Steigung der Geraden durch P(1 | 1) und Q(−3 | 45).
- `zwei_punkte` S1: Berechne die Steigung der Geraden durch P(−2 | 3) und Q(4 | 0).
- `proportional` S2: Die Gerade y = k · x geht durch P(−6 | 12). Berechne y für x = −3.
- `proportional` S2: Die Gerade y = k · x geht durch P(5 | 8,75). Berechne y für x = −4.
- `proportional` S2: Ist die Zuordnung (1 | 1), (2 | 4), (5 | 25) proportional?
- `proportional` S2: Ist die Zuordnung (1 | 7), (6 | 32), (7 | 37) proportional?
- `aufstellen` S1: Eine Gerade hat die Steigung −1 und schneidet die y-Achse bei −8. Gib den Funktionsterm an.
- `aufstellen` S1: Eine Gerade hat die Steigung 1 und schneidet die y-Achse bei −2. Gib den Funktionsterm an.
- `aufstellen` S2: Eine Gerade hat die Steigung 3 und geht durch P(2 | 0). Gib den Funktionsterm an.
- `aufstellen` S2: Eine Gerade hat die Steigung −5 und geht durch P(1 | 2). Gib den Funktionsterm an.
- `aufstellen` S2: Eine Gerade hat die Steigung −4 und geht durch P(5 | −16). Gib den Funktionsterm an.
- `schnittpunkte` S2: Berechne den Schnittpunkt von g: y = 3x + 3 und h: y = 4x + 2.
- `schnittpunkte` S2: Berechne den Schnittpunkt von g: y = −3x − 3 und h: y = −2x − 2.
- `schnittpunkte` S2: Berechne den Schnittpunkt von g: y = 2x − 5 und h: y = −x − 5.
- `schnittpunkte` S2: Berechne den Schnittpunkt von g: y = −3x − 7 und h: y = 4x + 14.
- `schnittpunkte` S2: Berechne den Schnittpunkt von g: y = 3x + 2 und h: y = −5x + 10.
- `schnittpunkte` S2: Berechne den Schnittpunkt von g: y = 0,5x + 1 und h: y = −x + 4.
- `lage` S1: Wie liegen die Geraden g: y = −4x und h: y = −8x + 5 zueinander?
- `lage` S1: Wie liegen die Geraden g: y = −2x − 6 und h: y = −2x − 2 zueinander?
- `lage` S1: Wie liegen die Geraden g: y = −x − 1 und h: y = −2x + 2 zueinander?
- `lage` S1: Wie liegen die Geraden g: y = −2x − 3 und h: y = −4x + 4 zueinander?
- `lage` S1: Wie liegen die Geraden g: y = x − 5 und h: y = 2x − 6 zueinander?
- `deuten` S2: Ein Planschbecken wird befüllt: h(x) = 0,5x + 5 (x in Minuten, h in cm). Nach wie vielen Minuten steht das Wasser 30 cm hoch?

**funktionen.gebrochen**

- `indirekt` S2: Die Tabelle (12 | 1), (2 | 6), (4 | 3) gehört zu einer indirekten Proportionalität. Welcher y-Wert gehört zu x = 6?
- `indirekt` S1: Wie ist die Zuordnung (2 | 15), (3 | 13), (5 | 12)?
- `indirekt` S1: Wie ist die Zuordnung (1 | 18), (2 | 16), (3 | 15)?
- `definitionsmenge` S1: Gib die Definitionsmenge von f(x) = −5/(x + 5) + 4 an.
- `definitionsmenge` S1: Gib die Definitionsmenge von f(x) = 7/(x + 2) − 1 an.
- `definitionsmenge` S1: Gib die Definitionsmenge von f(x) = −4/(x + 5) + 3 an.
- `definitionsmenge` S1: Gib die Definitionsmenge von f(x) = −4/(x − 1) an.
- `definitionsmenge` S2: Welche Zahl gehört nicht zur Definitionsmenge von f(x) = −1/(4x + 2) − 1?
- `definitionsmenge` S2: Welche Zahl gehört nicht zur Definitionsmenge von f(x) = 5/(x + 0,5) − 2?
- `asymptoten` S1: Gib die waagrechte Asymptote von f(x) = 1/(x + 8) + 3 an. y = □
- `asymptoten` S1: Gib die senkrechte Asymptote von f(x) = −2/(x − 7) + 5 an. x = □
- `asymptoten` S1: Gib die waagrechte Asymptote von f(x) = −5/(x − 4) − 3 an. y = □
- `asymptoten` S1: Gib die waagrechte Asymptote von f(x) = −5/(x + 1) − 4 an. y = □
- `asymptoten` S1: Gib die waagrechte Asymptote von f(x) = −9/(x − 8) + 2 an. y = □
- `asymptoten` S1: Gib die waagrechte Asymptote von f(x) = 1/(x + 5) − 3 an. y = □
- `achsenpunkte` S1: In welchem Punkt schneidet der Graph von f(x) = 10/(x + 1) + 2 die y-Achse? Gib den y-Wert an.
- `achsenpunkte` S2: Berechne die Nullstelle von f(x) = 4/(x − 5) − 1.
- `achsenpunkte` S2: Welche Nullstelle hat f(x) = −7/(x + 3)?
- `achsenpunkte` S1: In welchem Punkt schneidet der Graph von f(x) = 6/(x − 3) + 4 die y-Achse? Gib den y-Wert an.
- `achsenpunkte` S2: Berechne die Nullstelle von f(x) = 3/(x + 1) + 1,5.
- `achsenpunkte` S3: Für welche Werte von c schneidet der Graph von f(x) = 2/x + c die y-Achse?
- `parameter` S1: Wie entsteht der Graph von f(x) = −6/x + 1 aus dem Graphen von g(x) = −6/x?
- `parameter` S2: Wie entsteht der Graph von f(x) = 1/(x − 4) − 1 aus dem Graphen von g(x) = 1/x?
- `parameter` S2: Wie unterscheidet sich der Graph von f(x) = −3/x vom Graphen von g(x) = 3/x?
- `parameter` S2: Wie entsteht der Graph von f(x) = 5/(x + 1) aus dem Graphen von g(x) = 5/x?
- `beurteilen` S1: Welche Aussage über f(x) = −5/(x − 1) + 2 ist richtig?
- `beurteilen` S1: Welche Aussage über f(x) = −6/(x + 6) + 4 ist richtig?
- `beurteilen` S2: Welche Aussage über f(x) = 5/(x − 1) − 4 ist FALSCH?
- `beurteilen` S2: Welche Aussage über f(x) = −7/(x − 6) − 5 ist FALSCH?
- `beurteilen` S2: Welche Aussage über f(x) = −3/(x + 4) − 1 ist FALSCH?
- `beurteilen` S2: Welche Aussage über f(x) = 3/(x − 2) − 3 ist FALSCH?
- `beurteilen` S2: Welche Aussage über f(x) = −2/(x + 6) + 1 ist FALSCH?
- `beurteilen` S2: Welche Aussage über f(x) = −1/(x − 6) − 5 ist FALSCH?
- `beurteilen` S1: Welche Aussage über f(x) = 2/x ist richtig?
- `beurteilen` S2: Welche Aussage über f(x) = −1/(x + 2) + 3 ist FALSCH?

**messen.koerper_darstellung**

- `prisma` S2: Ein Prisma hat 12 Kanten. Wie viele Ecken hat seine Grundfläche?
- `prisma` S2: Ein Prisma hat 6 Ecken. Wie viele Ecken hat seine Grundfläche?
- `netz` S2: Lässt sich das Netz aus 6 Quadraten zu einem Würfel falten?
- `netz` S2: Lässt sich das Netz aus 6 Quadraten zu einem Würfel falten?
- `zylinder` S2: Ein Zylinder ist 18 cm hoch, sein Grundkreis hat den Umfang 23 cm. Wie groß ist die Mantelfläche?
- `zylinder` S2: Ein Zylinder ist 23 cm hoch, sein Grundkreis hat den Umfang 27,2 cm. Wie groß ist die Mantelfläche?
- `zylinder` S2: Ein Zylinder ist 9 cm hoch, sein Grundkreis hat den Umfang 9,3 cm. Wie groß ist die Mantelfläche?
- `zylinder` S2: Ein Zylinder ist 24 cm hoch, sein Grundkreis hat den Umfang 11,1 cm. Wie groß ist die Mantelfläche?
- `schraegbild` S1: Eine Kante führt 7 cm nach hinten. Wie lang zeichnest du sie im Schrägbild mit q = 1/2?
- `schraegbild` S2: Im Schrägbild (q = 1/2) ist eine nach hinten laufende Kante 7,5 cm lang. Wie lang ist sie in Wirklichkeit?
- `schraegbild` S2: Im Schrägbild (q = 1/2) ist eine nach hinten laufende Kante 6 cm lang. Wie lang ist sie in Wirklichkeit?
- `schraegbild` S2: Das Schrägbild (q = 1/2, ω = 45°) zeigt einen Quader. Wie tief ist der Quader in Wirklichkeit?
- `beurteilen` S1: Welche Aussage ist richtig?
- `beurteilen` S1: Welche Aussage ist richtig?
- `beurteilen` S1: Welche Aussage ist richtig?
- `beurteilen` S1: Welche Aussage ist richtig?
- `beurteilen` S1: Welche Aussage ist richtig?
- `beurteilen` S2: Welche Aussage ist FALSCH?
- `beurteilen` S1: Welche Aussage ist richtig?

**messen.kreisberechnung**

- `umfang` S1: Ein Kreis hat den Durchmesser 3,4 cm. Berechne den Umfang. Runde auf eine Nachkommastelle.
- `umfang` S1: Ein Kreis hat den Durchmesser 43,2 cm. Berechne den Umfang. Runde auf eine Nachkommastelle.
- `flaeche` S1: Ein Kreis hat den Durchmesser 10 cm. Berechne den Flächeninhalt. Runde auf eine Nachkommastelle.
- `flaeche` S1: Berechne den Flächeninhalt eines Kreises mit r = 12 cm. Runde auf eine Nachkommastelle.
- `flaeche` S1: Berechne den Flächeninhalt eines Kreises mit r = 2 cm. Runde auf eine Nachkommastelle.
- `flaeche` S1: Berechne den Flächeninhalt eines Kreises mit r = 14 cm. Runde auf eine Nachkommastelle.
- `exakt` S1: Ein Kreis hat r = 11 cm. Gib den Umfang exakt an: u = □ · π cm. Welche Zahl gehört in das Kästchen?
- `exakt` S1: Ein Kreis hat r = 1 cm. Gib den Umfang exakt an: u = □ · π cm. Welche Zahl gehört in das Kästchen?
- `exakt` S2: Ein Kreis hat den Durchmesser 27 cm. Gib den Flächeninhalt exakt an: A = □ · π cm². Welche Zahl gehört in das Kästchen?
- `exakt` S2: Ein Kreis hat den Umfang 22π cm. Wie groß ist sein Radius?
- `verstehen` S3: Ein Kreis hat r = 9 cm. Jemand rechnet A = π · 18². Was ist der Fehler?
- `sektor` S1: Ein Kreisausschnitt hat den Mittelpunktswinkel 45°. Welcher Anteil des Kreises ist das? Gib ihn als Dezimalzahl an.
- `sektor` S2: Ein Kreisausschnitt hat r = 6 cm und α = 72°. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `sektor` S2: Ein Kreisausschnitt hat r = 15 cm und α = 135°. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `sektor` S2: Ein Kreisausschnitt hat r = 3 cm und α = 270°. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `sektor` S2: Ein Kreisausschnitt hat r = 1,9 cm und α = 210°. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `zusammengesetzt` S1: Ein Kreisring hat den Außenradius 15 cm und den Innenradius 8 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `zusammengesetzt` S1: Ein Kreisring hat den Außenradius 13 cm und den Innenradius 4 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `zusammengesetzt` S1: Ein Kreisring hat den Außenradius 11 cm und den Innenradius 7 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `zusammengesetzt` S1: Ein Kreisring hat den Außenradius 15 cm und den Innenradius 12 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `zusammengesetzt` S1: Ein Kreisring hat den Außenradius 14 cm und den Innenradius 12 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `zusammengesetzt` S1: Ein Kreisring hat den Außenradius 15 cm und den Innenradius 13 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.
- `zylinder` S1: Ein Zylinder hat r = 4 cm und h = 7 cm. Berechne seine Mantelfläche. Runde auf eine Nachkommastelle.
- `zylinder` S1: Ein Zylinder hat r = 5 cm und h = 7 cm. Berechne seine Mantelfläche. Runde auf eine Nachkommastelle.
- `zylinder` S1: Ein Zylinder hat r = 1 cm und h = 5 cm. Berechne sein Volumen. Runde auf eine Nachkommastelle.
- `zylinder` S1: Ein Zylinder hat r = 4 cm und h = 4 cm. Berechne sein Volumen. Runde auf eine Nachkommastelle.
- `zylinder` S2: Ein Zylinder hat r = 9 cm und h = 2,3 cm. Berechne seine Oberfläche. Runde auf eine Nachkommastelle.
- `zylinder` S2: Ein Zylinder hat r = 1,6 cm und h = 7,5 cm. Berechne seine Oberfläche. Runde auf eine Nachkommastelle.

**messen.prisma_zylinder**: keine

**stochastik.grundbegriffe**

- `begriffe` S2: Ein Würfel mit den Zahlen 1 bis 12 wird geworfen. Welche Menge beschreibt das Ereignis „Vielfaches von 3“?
- `rel_haeufigkeit` S1: Bei 400 Würfen kam 79-mal die Sechs. Berechne die relative Häufigkeit als Dezimalzahl.
- `rel_haeufigkeit` S1: Bei 50 Würfen kam 7-mal die Sechs. Berechne die relative Häufigkeit als Dezimalzahl.
- `laplace` S3: Zwei faire Würfel werden geworfen. Wie groß ist die Wahrscheinlichkeit, dass die Augensumme 7 ist?
- `laplace_pruefen` S2: Ein Glücksrad hat die Felder A 60°, B 60°, C 60°, D 120°, E 60°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?
- `laplace_pruefen` S2: Ein Glücksrad hat die Felder A 120°, B 180°, C 60°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?
- `laplace_pruefen` S2: Ein Glücksrad hat die Felder A 30°, B 60°, C 60°, D 150°, E 60°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?
- `laplace_pruefen` S2: Ein Glücksrad hat die Felder A 30°, B 30°, C 90°, D 180°, E 30°. Ist eine Drehung (Ergebnis: Feldname) ein Laplace-Experiment?
- `gegenereignis` S1: Die Wahrscheinlichkeit, dass ein Bus pünktlich ist, beträgt 72 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht pünktlich ist (in %)?
- `gegenereignis` S1: Die Wahrscheinlichkeit, dass ein Bus pünktlich ist, beträgt 88 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht pünktlich ist (in %)?
- `gegenereignis` S1: Die Wahrscheinlichkeit, dass ein Elfmeter verwandelt wird, beträgt 82 %. Wie groß ist die Wahrscheinlichkeit, dass er nicht verwandelt wird (in %)?
- `grosse_zahlen` S1: Wie oft erwartest du bei 100 Versuchen ungefähr Wappen beim Münzwurf?
- `grosse_zahlen` S2: Wie oft erwartest du bei 100 Versuchen ungefähr „rot“ beim Glücksrad mit 10 gleichen Feldern, davon 6 rot?

**groessen.indirekt**

- `erkennen` S2: Welche Zuordnung ist indirekt proportional?
- `erkennen` S2: Welche Zuordnung ist indirekt proportional?
- `erkennen` S2: Welche Zuordnung ist indirekt proportional?
- `produkt` S1: Die Tabelle gehört zu einer indirekten Proportionalität. Ergänze den fehlenden y-Wert.
- `produkt` S2: Ist die Zuordnung in der Tabelle indirekt proportional?
- `produkt` S2: Ist die Zuordnung in der Tabelle indirekt proportional?
- `produkt` S2: Die Tabelle gehört zu einer indirekten Proportionalität. Ergänze den fehlenden Wert.
- `dreisatz` S2: 6 Bagger heben eine Baugrube in 8 Tagen aus. Wie lange brauchen 2 Bagger?
- `dreisatz` S2: 4 gleich starke Pumpen leeren ein Becken in 9 Stunden. Wie lange brauchen 6 Pumpen?
- `graph` S1: Der Punkt P liegt auf dem Graphen einer indirekten Proportionalität y = k : x. Bestimme k.
- `graph` S2: Liegt der Punkt Q(2 | 26) auf dem Graphen von y = 48 : x?
- `graph` S2: Liegt der Punkt Q(2 | 21) auf dem Graphen von y = 40 : x?
- `graph` S2: Liegt der Punkt Q(5 | 5) auf dem Graphen von y = 30 : x?
- `graph` S2: Alle Rechtecke mit 24 cm² Flächeninhalt: Breite x → Länge y. Der Punkt P(2 | 12) liegt auf dem Graphen. Was bedeutet der Punkt?
- `graph` S2: Liegt der Punkt Q(0,5 | 48) auf dem Graphen von y = 24 : x?
- `unterscheiden` S1: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S1: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S1: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S1: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S1: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S1: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S1: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S2: Welche Art von Zuordnung zeigt die Tabelle?
- `unterscheiden` S2: Welche Art von Zuordnung zeigt die Tabelle?

### (5) Quellen der Prüfungsvorbilder (nur Typ und Niveau übernommen, kein Wortlaut, keine Zahlen)

- ISB Bayern, Jahrgangsstufenarbeit/BMT Mathematik Jgst. 8 (Gymnasium), Aufgaben und Lösungen 2008, 2009, 2012, 2015, 2019, 2021, 2022, 2023, 2024, 2025 (isb.bayern.de, Bereich Jahrgangsstufenarbeiten Mathematik)
- ISB Bayern, Jahrgangsstufentest Mathematik 8 Realschule 2014, 2022, 2023
- ISB Bayern, BMT 10 2024 (Aufgabe zu Körpern, nur Niveauvergleich), Realschulabschluss Bayern 2020 (Körperberechnung)
- IQB/VERA-8 Mathematik 2012 (freigegebene Aufgaben), Abschlussprüfung Sachsen-Anhalt (Körper) – bereits im Generator messen.prisma_zylinder als Vorbild genannt
- Känguru der Mathematik, Klassenstufe 7/8 (2013, 2014, 2015, 2017, 2021, 2023, 2024) und Kadett 2023/2025 (für Knobel-Bordkarten: nur Art der Idee)
- TU Berlin, Tag der Mathematik 2024, Klassen 7–8

**Fakt:** Diese Dokumente habe ich bei der Recherche gefunden und als Vorbilder genutzt. **Einschränkung:** Ich habe nicht jeder einzelnen `pruefung`-Aufgabe ein bestimmtes Vorbild zugeordnet.

### (6) Beispiel-Bordkarten im Wortlaut: groessen.indirekt, Lernkarte `dreisatz`

**Stufe 1**

- (direkt) 6 Bagger heben eine Baugrube in 11 Tagen aus. Wie lange braucht ein Bagger allein? — Lösung: 66 Tage
- (erkennen) 5 Helfer brauchen 12 Minuten. Was ist beim Dreisatz der erste Schritt? Auswahl: Ein Helfer braucht 12 : 5 = 2,4 Minuten. | Ein Helfer braucht 5 · 12 = 60 Minuten. | Ein Helfer braucht 12 Minuten. | Ein Helfer braucht 12 − 5 = 7 Minuten. — Lösung: Ein Helfer braucht 5 · 12 = 60 Minuten.
- (direkt) 8 gleich starke Pumpen leeren ein Becken in 5 Stunden. Wie lange brauchen 5 Pumpen? — Lösung: 8 h

**Stufe 2**

- (mehrschritt) 6 Helfer räumen eine Turnhalle in 29 Minuten auf. Wie lange brauchen 5 Helfer? — Lösung: 34,8 min
- (darstellung) 3 Bagger heben eine Baugrube in 24 Tagen aus. Mit welcher Rechnung bestimmst du die Zeit für 5 Bagger? Auswahl: 24 · 3 : 5 | 24 : 3 · 5 | 24 − 3 + 5 | 24 · 5 : 3 — Lösung: 24 · 3 : 5
- (umkehr) Ein Futtervorrat reicht für 15 Tiere 8 Tage. Für wie viele Tiere reicht er 12 Tage? — Lösung: 10 Tiere

**Stufe 3**

- (rueckwaerts) Mit 4 gleich starken Pumpen dauert das Leeren eines Beckens 9 Stunden. Es soll höchstens 6 Stunden dauern. Wie viele Pumpen braucht man mindestens? — Lösung: 6 Pumpen
- (fehler) 8 Helfer räumen eine Turnhalle in 40 Minuten auf. Wie lange brauchen 5 Helfer? Jemand rechnet: 40 : 8 · 5 = 25 Minuten. Was ist falsch? Auswahl: Der Schritt zur Einheit: Einer braucht länger, also mal statt geteilt. | Am Ende muss 5 addiert werden. | Man muss erst die Zeiten addieren. | Nichts, die Rechnung stimmt. — Lösung: Der Schritt zur Einheit: Einer braucht länger, also mal statt geteilt.
- (transfer) Bei 90 km/h dauert eine Fahrt 40 Minuten. Wie schnell muss man fahren, um 10 Minuten früher anzukommen? — Lösung: 120 km/h

**Knobel-Bordkarten (Bonus, Stufe 3)**

- Pumpe A leert ein Becken allein in 6 Stunden, Pumpe B allein in 3 Stunden. Wie viele Stunden brauchen beide zusammen? — Tipp: Welchen Teil des Beckens schafft jede Pumpe in einer Stunde? — Lösung: 2 h. Lösungsweg: In einer Stunde schafft A 1/6, B 1/3 = 2/6 des Beckens; zusammen 3/6 = 1/2. Das ganze Becken dauert also 2 Stunden.
- 6 Arbeiter wollen eine Arbeit in 10 Tagen schaffen. Nach 4 Tagen soll sie 2 Tage früher fertig werden als geplant. Wie viele Arbeiter müssen insgesamt arbeiten? — Tipp: Rechne den Rest in „Arbeitertagen“. — Lösung: 9. Lösungsweg: Rest: 6 Tage für 6 Arbeiter = 36 Arbeitertage. Neu bleiben nur 10 − 2 − 4 = 4 Tage: 36 : 4 = 9 Arbeiter.
