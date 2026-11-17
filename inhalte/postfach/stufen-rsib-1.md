# Postfach stufen-rsib-1 (Zwanzigste Runde, Zusatz Realschule und IB, Chat 1)

Neueste Meldung oben.

## 2026-11-17 22:40 – FERTIG
Abschlussbericht Zwanzigste Runde, Zusatz Realschule/IB, Chat 1: alle 12 Themen erledigt. Zweig `stufen-rsib-1`, ein Commit je Thema, kein Merge. Keine Datenbank, kein App-Code, keine Tests.

**Gesamt:** 342 neue Übungen, 138 Knobel-Bordkarten (Pool bonus, g knobel, jede mit Tipp und ausführlichem Weg), 330 überzählige Übungen gemeldet (ohne g, nicht gelöscht). Liste: `inhalte/postfach/stufen-rsib-1-ueberzaehlig.md`.

**Prüfung je Thema (alle 12):**
- `tools/inhalt_pruefen.py`: OK, 0 Gruppen „gleich gebaut hintereinander“.
- `inhalte/generatoren/_stufen_rsib1.py nachweis <thema>`: NACHWEIS OK. Das Werkzeug ist dasselbe wie in Klasse 9 (`_stufen_kl9.py`). Geprüft wird:
  - Alte Aufgaben sind gegen origin/lernen-app nur in g und s geändert; Lernkarten-Texte und alle übrigen Felder sind unverändert.
  - S1 ≥ 4 Übungen aus ≥ 2 Typen, S2 ≥ 6 aus ≥ 3 Typen, S3 ≥ 8 aus ≥ 4 Typen.
  - Auf S3 höchstens 3 Übungen je Typ; je Stufe und Typ höchstens 2 gleich gebaute Übungen.
  - Nie zwei Übungen gleichen Typs direkt hintereinander; 1–3 Knobel-Bordkarten je Lernkarte.
- Jede c-Formel rechnet die Lösung nach (Generator-Assert in `_befunde.py`); jede neue Aufgabe von Hand gelesen.

**Umgang mit Überzähligen:** wie in Klasse 9. Ab der 3. gleich gebauten Übung je Stufe und Typ bzw. auf S3 ab der 4. Übung desselben Typs bleibt die Übung unverändert und ohne g. Der Haupt-Chat sperrt sie.

**Abweichungen und Annahmen:**
- Berichtigung: In der STATUS-Zeile zu abbildungen.vektoren steht „30 neue Übungen“. Richtig sind 29 (+ 12 Knobel-Bordkarten).
- Typ-Zuordnung alter Aufgaben (Annahme, wie in Klasse 9): Dieselbe Rechnung wie im Beispiel, nur mit negativen Zahlen oder Dezimalzahlen, bekommt `mehrschritt` (S2) oder bleibt `direkt` (S1). Alte S3-Aufgaben, die nur „x aus einem Wert“ verlangen, sind als `umkehr` auf S2 umgestuft.
- In mengen.grundbegriffe und groessen.verhaeltnisse hat der Generator keinen `__main__`-Block. Der Stufen-Block steht dort am Dateiende, nach `durchsicht(d)`.
- Die Themen haben keine Gymnasium-Klasse. Stufe 2 und 3 nutzen deshalb neben der Lernkarte nur Stoff, der laut Spalte (a) unten ohnehin vorausgesetzt ist. Ausnahmen, je eine Aufgabe: Satz des Pythagoras in abbildungen.vektoren nicht verwendet; in funktionen.umkehr/spiegeln eine Transfer-Aufgabe mit Pythagoras; in abbildungen.matrizen der Betrag eines Vektors mit Pythagoras.
- Keine Lernkarte hat weniger als 2 Knobel-Bordkarten.

### (a)/(b) Vorwissen und frühestmögliche Gymnasium-Klasse je Thema

| Thema | (a) vorausgesetzte Themen (Schlüssel, Gymnasium-Klasse) | (b) frühestens lösbar ab Gymnasium-Klasse |
|---|---|---|
| abbildungen.determinanten2 | zahlen.ganz (Kl. 5), messen.flaechen_vielecke (Kl. 6), bruch.rechnen (Kl. 6), abbildungen.vektoren (RS, Spitze minus Fuß), gleichungen.linear (Kl. 7, für x-Aufgaben) | Kl. 7 (nach Flächen von Parallelogramm/Dreieck in Kl. 6 und linearen Gleichungen in Kl. 7) |
| abbildungen.vektoren | zahlen.ganz (Kl. 5), Koordinatensystem aus geometrie.grundbegriffe (Kl. 5), abbildungen.kongruenz (Kl. 7, Verschiebung als Abbildung), gleichungen.linear (Kl. 7, nur Parameter- und Knobelaufgaben) | Kl. 6 für den Kern (Rechnen mit Koordinaten), Kl. 7 für Parameter- und Knobelaufgaben |
| daten.stichproben | bruch.prozent (Kl. 6), daten.kennwerte (Kl. 6, Anteile/Mittelwert), daten.darstellen (Kl. 6, Kreisdiagramm), stochastik.kombinatorik (Kl. 5, eine Knobel-Bordkarte) | Kl. 6 (nach der Prozentrechnung); Bewertungsaufgaben eher ab Kl. 7 |
| funktionen.scharen | funktionen.linear (Kl. 8: Steigung, Achsenabschnitt), gleichungen.linear (Kl. 7), gleichungen.ungleichungen (Kl. 8, Bereiche für k), terme.umformen (Kl. 7, Ausklammern; Binom in einer Knobel-Bordkarte) | Kl. 8 (nach den linearen Funktionen) |
| terme.quadratische_extreme | terme.umformen (Kl. 7: Ausmultiplizieren, Ausklammern; binomische Formeln), messen.flaechen (Kl. 5, Rechteck), gleichungen.linear (Kl. 7) | Kl. 8 (binomische Formeln vorausgesetzt); im Gymnasium regulär in Kl. 9 bei funktionen.quadratisch |
| funktionen.transformation | funktionen.quadratisch (Kl. 9: Normalparabel, Scheitelform), abbildungen.kongruenz (Kl. 7: Verschiebung, Achsenspiegelung), funktionen.grundbegriffe (Kl. 8: f(x)-Schreibweise), zahlen.wurzeln_basis (Kl. 9, für Nullstellen) | Kl. 9 (zusammen mit funktionen.quadratisch) |
| gleichungen.reinquadratisch | zahlen.wurzeln_basis (Kl. 9: Quadratwurzel, Schätzen), gleichungen.linear (Kl. 7: Äquivalenzumformungen), messen.kreisberechnung (Kl. 8: Kreisfläche), terme.umformen (Kl. 7/8: binomischer Term) | Kl. 9 (nach zahlen.wurzeln_basis) |
| gleichungen.wurzel | zahlen.wurzeln_basis (Kl. 9), gleichungen.linear (Kl. 7), gleichungen.ungleichungen (Kl. 8, Definitionsmenge), gleichungen.quadratisch (Kl. 9, Karte zwei_seiten), terme.umformen (binomische Formeln) | Kl. 9 (Karte zwei_seiten erst nach gleichungen.quadratisch) |
| abbildungen.matrizen | abbildungen.vektoren und abbildungen.determinanten2 (RS), abbildungen.kongruenz (Kl. 7: Spiegelungen, Drehungen), trigo.allgemein (Kl. 9: sin/cos beliebiger Winkel, für drehung und Winkel im Skalarprodukt), trigo.pythagoras (Kl. 9: Betrag), gleichungen.lgs2 (Kl. 8) | Kl. 9 (Karten drehung und skalarprodukt brauchen sin/cos); bildpunkt, rechnen, inverse ab Kl. 8 |
| funktionen.umkehr | funktionen.grundbegriffe (Kl. 8: Definitions-/Wertemenge), funktionen.linear (Kl. 8), funktionen.quadratisch (Kl. 9: Scheitelform, Parabelast), zahlen.wurzeln_basis (Kl. 9), funktionen.exponential_log (Kl. 10: Logarithmus) | Kl. 10 (Karte exp_log); umkehrbar, werte, linear, spiegeln ab Kl. 8; quadratisch ab Kl. 9 |
| mengen.grundbegriffe | zahlen.teilbarkeit (Kl. 5: Teiler, Vielfache, Primzahlen), zahlen.natuerlich (Kl. 5), zahlen.potenzen_basis (Kl. 5: Quadratzahlen), bruch.prozent (Kl. 6, nur eine Venn-Aufgabe) | Kl. 5 (Prozentaufgabe im Venn-Diagramm ab Kl. 6) |
| groessen.verhaeltnisse | zahlen.teilbarkeit (Kl. 5: ggT zum Kürzen), groessen.proportional (Kl. 5: Dreisatz), groessen.einheiten (Kl. 5), bruch.brueche und bruch.dezimal (Kl. 6), groessen.indirekt (Kl. 8, nur eine Aufgabe), gleichungen.linear (Kl. 7, Knobel-Bordkarten) | Kl. 6 (Kern ab Kl. 5 mit Dreisatz; Brüche und Dezimalzahlen im Verhältnis ab Kl. 6) |

Annahme zu (b): Maßgeblich ist, wann die vorausgesetzten Gymnasium-Themen in der Themenliste liegen (Spalte a). Einzelne Knobel-Bordkarten können eine Klasse später liegen.

### 1–2) Stufen-Leiter und Übungen je Stufe und Typ (vorher → nachher)

„vorher“: Übungen je Stufe auf origin/lernen-app; dort hatte keine Übung ein g. „nachher“: Übungen mit Typ, in Klammern nach Typ. Überzählige stehen ohne Typ in der letzten Spalte.

Typkürzel: dir direkt · erk erkennen · mehr mehrschritt · eink einkleidung · umk umkehr · dar darstellung · rück rueckwaerts · verk verknuepfen · begr begruenden · fehl fehler · trans transfer · par parameter · prüf pruefung

### abbildungen.determinanten2

Neue Übungen 40, Knobel-Bordkarten 12, überzählig 55.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| det_berechnen | Die Determinante zweier Vektoren über Kreuz ausrechnen und die richtige Rechnung erkennen. / Fehlende Koordinate aus dem Wert bestimmen, Pfeile aus einer Beschreibung übersetzen, Determinanten verrechnen, einfache Sachsituation. / Rechenregeln begründen (Vertauschen, Vervielfachen, Addieren), Vorzeichenfehler finden, Parameter mit Determinante 0, mehrteilige Prüfungsaufgabe. | 6 → 5 (dir 3, erk 2) | 7 → 6 (umk 3, dar 1, mehr 1, eink 1) | 9 → 8 (begr 3, par 2, fehl 2, prüf 1) | 2 | 13 |
| parallelogramm | Mit zwei gegebenen Spannvektoren die Fläche eines Parallelogramms ausrechnen; die Spannvektoren erkennen. / Spannvektoren aus Eckpunkten bilden, mit Maßstab in m² umrechnen, fehlende Koordinate aus der Fläche, Grundseite mal Höhe mit Determinante vergleichen. / Fläche in Abhängigkeit von x, Lage auf einer Geraden, Wirkung von Verdoppeln und Verschieben begründen, Fehler „Ortsvektoren statt Spannvektoren“, Höhe aus der Fläche, Prüfungsaufgabe mit C. | 6 → 4 (dir 3, erk 1) | 8 → 8 (mehr 4, eink 2, umk 1, dar 1) | 8 → 8 (par 3, begr 2, fehl 1, verk 1, prüf 1) | 2 | 10 |
| dreieck | Mit zwei Spannvektoren die Dreiecksfläche als halbe Determinante ausrechnen. / Spannvektoren aus Ecken bilden, Plan mit Maßstab, fehlende Koordinate aus der Fläche. / Fläche in Abhängigkeit von x, Verschieben und Verkleinern begründen, Fehler „Halbieren vergessen“, Mittelpunkt nutzen, Koordinaten selbst festlegen, Prüfungsaufgabe. | 6 → 4 (dir 3, erk 1) | 7 → 7 (mehr 3, eink 2, umk 2) | 8 → 8 (par 2, begr 2, fehl 1, verk 1, trans 1, prüf 1) | 2 | 9 |
| umlaufsinn | Aus dem Vorzeichen der Determinante den Umlaufsinn ablesen. / Umlaufsinn aus Eckpunkten berechnen, Fläche als Betrag, Vertauschen der Pfeile, Laufweg im Alltag. / Reihenfolge gegen den Uhrzeigersinn festlegen, Fehler mit negativer Fläche finden, Lage auf einer Geraden begründen, Parameter für Umlaufsinn und Gerade. | 6 → 4 (erk 3, dir 1) | 6 → 6 (mehr 4, umk 1, eink 1) | 8 → 8 (verk 2, fehl 2, begr 2, par 2) | 2 | 5 |
| viereck | Ein Viereck mit drei gegebenen Pfeilen AB, AC, AD in zwei Dreiecke zerlegen und die Fläche ausrechnen. / Pfeile aus den Ecken bilden, Grundstück auf einem Plan, fehlende Determinante aus der Fläche bestimmen. / Fehler „½ vergessen“ finden, Zerlegung über die andere Diagonale begründen, Drachen und Rechteck als Sonderfall, Parameter x, Prüfungsaufgabe. | 6 → 4 (dir 3, erk 1) | 8 → 7 (mehr 4, eink 2, umk 1) | 8 → 8 (fehl 2, par 2, begr 1, trans 1, verk 1, prüf 1) | 2 | 8 |
| vieleck | Ein Fünfeck mit gegebenen Pfeilen von A aus in drei Dreiecke zerlegen; wissen, wie viele Determinanten man braucht. / Pfeile aus den Ecken bilden, Sechseck, Spielplatz mit Maßstab, Ecken aus einer Tabelle, fehlende Determinante aus der Fläche. / Fehler „ein Dreieck zu viel“, Unabhängigkeit von der Startecke und Umlaufsinn nach Spiegeln begründen, L-Form mit Rechtecken prüfen, Hauswand als Modell, Parameter, Prüfungsaufgabe. | 6 → 4 (dir 2, erk 2) | 6 → 6 (mehr 3, eink 1, umk 1, dar 1) | 9 → 8 (par 2, begr 2, fehl 1, verk 1, trans 1, prüf 1) | 2 | 10 |

### abbildungen.vektoren

Neue Übungen 29, Knobel-Bordkarten 12, überzählig 47.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| vektor_bestimmen | Vektor AB als Spitze minus Fuß ausrechnen und den passenden Vektor erkennen. / Mit negativen Koordinaten rechnen, Fußpunkt aus Vektor und Spitze bestimmen, Weg im Gelände als Vektor. / Fehler „Fuß minus Spitze“ finden, Vektoren verketten, Parameter, Lage auf einer Geraden begründen, gleiche Teilstrecken aus einem Gesamtweg, Prüfungsaufgabe AB + BC = AC. | 6 → 4 (dir 2, erk 2) | 8 → 7 (mehr 4, umk 2, eink 1) | 8 → 8 (par 2, fehl 1, verk 1, begr 1, rück 1, trans 1, prüf 1) | 2 | 6 |
| bildpunkt | Einen Punkt mit einem Vektor verschieben: Koordinaten addieren, Bildpunkt erkennen. / Mit negativen Koordinaten, Vektor beschrieben in Worten, mehrere Punkte einer Figur, Vektor aus Punkt und Bildpunkt, Urpunkt. / Startpunkt nach zwei Verschiebungen, Parameter, Reihenfolge begründen, Fehler „abgezogen statt addiert“, Mittelpunkt verschieben, Zugzahl bestimmen, Prüfungsaufgabe. | 6 → 4 (dir 2, erk 2) | 8 → 6 (mehr 3, umk 1, dar 1, eink 1) | 8 → 8 (par 2, rück 1, fehl 1, begr 1, trans 1, verk 1, prüf 1) | 2 | 12 |
| gegenvektor | Den Gegenvektor angeben (Vorzeichen umdrehen) und erkennen, dass er eine Verschiebung rückgängig macht. / Urpunkt aus Bildpunkt und Vektor, Rückweg nach zwei Fahrten, Rückweg in einer Sachsituation. / Verschiebung aus einem Punktpaar auf eine andere Ecke übertragen, Parameter, Nullvektor begründen, Fehler „weiter statt zurück“, Bedingung für einen zweiten Vektor, Prüfungsaufgabe. | 7 → 4 (dir 2, erk 2) | 9 → 7 (umk 4, mehr 2, eink 1) | 8 → 8 (begr 2, par 1, rück 1, verk 1, fehl 1, trans 1, prüf 1) | 2 | 9 |
| addition | Zwei Vektoren koordinatenweise addieren und eine Summe erkennen. / AB + BC = AC, drei Verschiebungen zu einer zusammenfassen, fehlenden Summanden bestimmen. / Geschlossener Weg im Viereck, Boot mit Strömung, Unabhängigkeit vom Zwischenpunkt begründen, passende Summanden suchen, Vorzeichenfehler finden, Parameter, Prüfungsaufgabe Flugroute. | 7 → 4 (dir 2, erk 2) | 8 → 6 (mehr 2, umk 2, eink 2) | 8 → 8 (begr 2, verk 1, trans 1, rück 1, fehl 1, par 1, prüf 1) | 2 | 9 |
| punkt_berechnen | Die vierte Ecke C eines Parallelogramms aus A, AB und AD bestimmen; gleiche Vektoren erkennen. / Vierte Ecke aus drei Eckpunkten, fehlende Ecke B, Pfosten eines Beets. / Mittelpunkt mit Vektoren, Parameter, drei mögliche vierte Ecken begründen, Fehler beim Vektor finden, Ecken aus dem Diagonalenschnittpunkt, Prüfungsaufgabe. | 6 → 4 (dir 3, erk 1) | 8 → 7 (mehr 4, umk 2, eink 1) | 8 → 8 (verk 2, par 2, begr 1, fehl 1, rück 1, prüf 1) | 2 | 8 |
| eigenschaften | Wissen und anwenden: Verschieben ändert Längen, Winkel und Flächen nicht. / Hin- und Rückverschiebung, Bildstrecke als Vektor, Vektor aus zwei Punkten auf eine Figur anwenden, Fläche des Bilds, Stempelmuster. / Mögliche Bildpunkte begründen, Fixpunkt, gleiche Verschiebungsweite, Parallelogramm AA′B′B, Fehler „Strecken werden länger“, Fries-Fläche, Parameter, Prüfungsaufgabe. | 6 → 9 (dir 5, erk 4) | 7 → 6 (mehr 3, dar 1, umk 1, eink 1) | 8 → 8 (begr 3, verk 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 3 |

### daten.stichproben

Neue Übungen 20, Knobel-Bordkarten 10, überzählig 10.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| begriffe | Grundgesamtheit, Stichprobe und Stichprobenumfang benennen. / Stichprobenumfang aus einem Prozentsatz, gleich viele je Klasse, Grundgesamtheit aus Umfang und Anteil zurückrechnen. / Gründe für Stichproben begründen, Zufallsstichprobe beurteilen, Anteil der Befragten, Aufwand planen, Fehler „Vollerhebung heißt Stichprobe“, Schrittweite k, geschichtete Prüfungsaufgabe. | 6 → 8 (erk 6, dir 2) | 8 → 7 (mehr 3, eink 2, umk 2) | 8 → 8 (begr 3, verk 1, trans 1, fehl 1, par 1, prüf 1) | 2 | 4 |
| hochrechnen | Den Anteil in der Stichprobe in Prozent ausrechnen. / Auf die Grundgesamtheit hochrechnen, auch aus einem Diagramm; aus der Hochrechnung auf die Stichprobe zurück; Gegenanteil. / Prozentpunkte vergleichen, Fische markieren, vertrauenswürdigere Hochrechnung begründen, fehlende Antworten rückwärts, Fehler „Anzahl mal Gesamtzahl“, Stichprobenumfang als Unbekannte, Verkehrszählung als Prüfungsaufgabe. | 6 → 5 (dir 4, erk 1) | 8 → 12 (mehr 9, umk 2, dar 1) | 8 → 8 (verk 2, trans 1, begr 1, rück 1, fehl 1, par 1, prüf 1) | 2 | 2 |
| repraesentativ | Erkennen, ob eine Stichprobe zufällig ist und alle Gruppen abdeckt. / Aus mehreren Auswahlen die beste wählen, Grund für eine Verzerrung nennen, Zusammensetzung einer Tabelle vergleichen. / Große verzerrte gegen kleine zufällige Stichprobe abwägen, Hauptproblem einer Umfrage finden, verzerrte Kanäle erkennen, passende Zusammensetzung als Prüfungsaufgabe. | 6 → 7 (erk 6, dir 1) | 6 → 7 (eink 5, umk 1, dar 1) | 8 → 9 (begr 3, fehl 3, trans 2, prüf 1) | 2 | 0 |
| fehlerquellen | Eine Fehlerquelle benennen (suggestive Frage, zu klein, einseitig, nur Freiwillige) und eine Frage neutral stellen. / Fehlerquellen in Umfragen von Sender, Zeitschrift und Verein, mehrere Fehler zugleich, passende Situation zu einer Fehlerquelle. / Wirksamste Verbesserung wählen, mehrere Mängel finden, Wirkung einer größeren Stichprobe begründen, Werbeaussage prüfen, Bewertung einer ganzen Umfrage wie in einer Prüfung. | 6 → 12 (erk 11, dir 1) | 8 → 6 (eink 4, umk 1, mehr 1) | 8 → 8 (begr 3, trans 2, fehl 2, prüf 1) | 2 | 0 |
| aussagen | Erkennen, dass ein Stichprobenergebnis ein Schätzwert ist und große Stichproben weniger schwanken. / Anteile als Schätzwert formulieren, Spannweite und Prozentpunkte berechnen, Gewicht einer Person. / Schlagzeilen beurteilen, knappe Ergebnisse abwägen, Fehlschluss bei kleinen Umfragen finden, mindestens nötige Anzahl rückwärts bestimmen, Prüfungsaufgabe mit zwei Umfragen. | 6 → 5 (erk 4, dir 1) | 8 → 7 (mehr 4, eink 2, umk 1) | 8 → 9 (begr 3, trans 2, rück 2, fehl 1, prüf 1) | 2 | 4 |

### funktionen.scharen

Neue Übungen 24, Knobel-Bordkarten 12, überzählig 16.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| einsetzen | Einen Parameterwert einsetzen und die Gleichung der Geraden angeben oder erkennen. / y-Werte für Parameter und Stelle berechnen, Punktprobe, Parameter aus einem Punkt, Tarif als Schar. / Punkt auf keiner Geraden begründen, doppelte Steigung, Bedingung für k, gleiche y-Werte, Tarif rückwärts, Wirkung von k, Fehler „k an falscher Stelle“, Prüfungsaufgabe. | 8 → 6 (dir 4, erk 2) | 8 → 9 (mehr 6, umk 2, eink 1) | 8 → 8 (begr 2, par 2, verk 1, rück 1, fehl 1, prüf 1) | 2 | 4 |
| parallelenschar | In y = mx + t den Achsenabschnitt t aus einem Punkt bestimmen; erkennen, dass alle Geraden parallel sind. / t am Bild ablesen, Parallele durch einen Punkt, t aus dem Nullpunkt der Geraden. / Fehler beim Einsetzen negativer Zahlen, Abstand zweier Parallelen, Bedingung an t, Parallelen schneiden sich nie, Paketpreis als Modell, Prüfungsaufgabe. | 6 → 6 (dir 5, erk 1) | 6 → 7 (mehr 4, dar 2, umk 1) | 8 → 8 (fehl 2, verk 2, par 1, begr 1, trans 1, prüf 1) | 2 | 4 |
| bueschel | Das Zentrum Z eines Geradenbüschels ablesen. / Zentrum bei y = m · x + t, Steigung durch einen weiteren Punkt, Lichtstrahl als Büschel. / Steigung aus zwei Punkten, senkrechte Gerade begründen, Zentrum aus versteckter Form, Gerade durch den Ursprung, Bedingung an m, Fehler beim Vorzeichen, Prüfungsaufgabe. | 7 → 6 (dir 5, erk 1) | 6 → 7 (umk 4, dar 2, eink 1) | 8 → 9 (verk 2, begr 2, par 2, trans 1, fehl 1, prüf 1) | 2 | 2 |
| wirkung | Erkennen, wo der Parameter steht; k für eine waagrechte Gerade bestimmen. / k für eine vorgegebene Steigung, Bereich fallender Geraden, k aus einem gezeichneten Graphen. / Gerade durch den Ursprung begründen, steiler als eine gegebene Gerade, Fehler beim Bereich, Nullstelle nach Punktbedingung, Prüfungsaufgabe. | 6 → 7 (dir 5, erk 2) | 6 → 8 (mehr 3, dar 3, umk 2) | 8 → 8 (begr 3, par 2, fehl 1, verk 1, prüf 1) | 2 | 1 |
| loesung_parameter | k · x = c für einen gegebenen Wert von k lösen. / Gleichungen mit k in Klammern lösen, Schnittstelle zweier Geraden, k ohne Lösung, Tarifvergleich. / Fallunterscheidung begründen, parallele Geraden, Bedingung „unendlich viele“ und „positiv“, rückwärts aus dem Schnittpunkt, Fehler „Teilen durch null“. | 6 → 4 (dir 3, erk 1) | 7 → 8 (mehr 4, umk 3, eink 1) | 8 → 9 (verk 3, begr 2, par 2, rück 1, fehl 1) | 2 | 4 |
| sachaufgabe | Kosten mit Grundgebühr und Preis je Einheit ausrechnen; den passenden Term erkennen. / Preis je Einheit aus einem Rechnungsbetrag, Verbrauch aus den Kosten, Ersparnis zweier Tarife, Tarif aus einer Tabelle. / Gleiche Kosten bestimmen, Tarif aus zwei Rechnungen, Tarifänderung, Fehler „Grundgebühr mehrfach“, Bedingung an die Grundgebühr, Tarifvergleich als Prüfungsaufgabe. | 6 → 7 (dir 6, erk 1) | 8 → 10 (umk 8, mehr 1, dar 1) | 8 → 9 (verk 2, rück 2, trans 2, fehl 1, par 1, prüf 1) | 2 | 1 |

### terme.quadratische_extreme

Neue Übungen 27, Knobel-Bordkarten 10, überzählig 27.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| ergaenzen | x² + bx mit gerader Zahl b zu einem Binom ergänzen und ein Binom erkennen. / Mit negativem b und ungeradem b (Dezimalzahl) ergänzen, ein Binom als Klammerquadrat schreiben, Eckquadrat am Bild bestimmen. / Vom Binom zurück auf den mittleren Term, Faktor vor x², Abstand zum Binom, Fehler „b statt b/2“, b für ein Binom bestimmen, Nichtnegativität begründen, Prüfungsaufgabe. | 7 → 4 (dir 2, erk 2) | 6 → 7 (mehr 5, umk 1, dar 1) | 8 → 8 (fehl 2, rück 1, trans 1, verk 1, begr 1, par 1, prüf 1) | 2 | 7 |
| scheitelform | x² + bx + c mit quadratischer Ergänzung in die Form (x + d)² + e bringen; passende Form erkennen. / Ungerade b mit Dezimalzahlen, Scheitelform ausmultiplizieren, c aus der Scheitelform, Term zu einer Wertetabelle. / Lücken rückwärts füllen, Fehler bei b/2 und beim Abziehen finden, Positivität und Gleichheit begründen, Bedingung an c, Fontäne als Modell, Prüfungsaufgabe. | 6 → 8 (dir 6, erk 2) | 9 → 7 (umk 4, mehr 2, dar 1) | 8 → 8 (fehl 2, begr 2, rück 1, par 1, trans 1, prüf 1) | 2 | 6 |
| extremwert | An (x − d)² + e bzw. −(x − d)² + e Stelle und Wert des Extremums ablesen; Minimum oder Maximum erkennen. / Erst ergänzen, dann ablesen; Parameter aus einem Extremwert; Gewinn als Sachsituation; Extremum aus einer Wertetabelle. / Größter Wert existiert nicht – begründen, Aussagen über Schranken prüfen, Fehler beim Vorzeichen in der Klammer, Bedingung für ein Maximum, Temperaturverlauf, Prüfungsaufgabe. | 6 → 11 (dir 9, erk 2) | 6 → 6 (mehr 2, umk 2, eink 1, dar 1) | 8 → 9 (begr 3, verk 2, fehl 1, par 1, trans 1, prüf 1) | 2 | 1 |
| mit_faktor | Bei a · x² + bx + c den Faktor a ausklammern, ergänzen und das Extremum angeben; Minimum oder Maximum am Vorzeichen von a erkennen. / Negative und gebrochene Faktoren, Faktor a aus der Lage des Extremums, Flächeninhalt als Term. / Fehler „Ausgleich nicht mit a malgenommen“, Lage des Extremums vergleichen, Bedingung an c, c aus dem Minimum zurück, Stückkosten als Modell, Prüfungsaufgabe. | 8 → 6 (dir 4, erk 2) | 6 → 6 (mehr 4, umk 1, eink 1) | 8 → 8 (fehl 2, begr 2, par 1, rück 1, trans 1, prüf 1) | 2 | 7 |
| optimierung | Bei Rechtecken mit festem Umfang und Zahlen mit fester Summe das größte Produkt bestimmen; den Flächenterm erkennen. / Feste Differenz, Rechteck an einer Mauer, Preiserhöhung mit weniger Käufern, gesuchte Seitenlänge statt Fläche. / Seitenlängen als Terme, Eintrittspreis, Summe von Quadraten, Hausecke als Modell, Fehler beim halben Umfang, Quadrat als bestes Rechteck begründen, Stallgehege als Prüfungsaufgabe. | 8 → 5 (dir 4, erk 1) | 7 → 8 (mehr 4, eink 3, umk 1) | 8 → 8 (trans 3, verk 2, fehl 1, begr 1, prüf 1) | 2 | 6 |

### funktionen.transformation

Neue Übungen 23, Knobel-Bordkarten 12, überzählig 18.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| nach_oben | Den Scheitel einer nach oben oder unten verschobenen Normalparabel angeben und die passende Gleichung erkennen. / Verschobene Parabeln noch einmal verschieben, Punkte mitverschieben, y-Werte berechnen, Scheitel am Bild ablesen. / Nötige Verschiebung rückwärts bestimmen, e aus Nullstellen, Abstand zweier Parabeln und Schnittpunkte begründen, Symmetrie nutzen, Fehler „− heißt oben“, Bedingung für Nullstellen. | 6 → 5 (dir 3, erk 2) | 9 → 9 (mehr 6, dar 2, umk 1) | 8 → 9 (rück 3, verk 2, begr 2, fehl 1, par 1) | 2 | 2 |
| nach_rechts | Den Scheitel von y = (x − d)² ablesen und die Gleichung zu einer Verschiebung nach links oder rechts erkennen. / Scheitel von (x − d)² + e, weiter verschieben, y-Achsenabschnitt, Gleichung zum Scheitel, Scheitel am Bild. / d aus einem Punkt rückwärts, zwei mögliche d, gleiche y-Werte zweier Parabeln, Fehler „+ heißt rechts“, (3 − x)² begründen, Rinne als Modell, Prüfungsaufgabe. | 6 → 9 (erk 6, dir 3) | 8 → 7 (mehr 4, dar 2, umk 1) | 8 → 8 (rück 2, par 1, fehl 1, verk 1, begr 1, trans 1, prüf 1) | 2 | 2 |
| strecken | y-Werte von y = a · x² berechnen und gestreckt/gestaucht/nach unten geöffnet erkennen. / a aus einem Punkt bestimmen, mit a weiterrechnen, a am Bild ablesen, Brückenbogen. / Enge begründen, Fehler „kleines a ist enger“, Bereich für a, Satellitenschüssel als Modell, Schnitt mit einer Waagrechten, Wert über a rückwärts, Prüfungsaufgabe. | 6 → 4 (dir 2, erk 2) | 6 → 6 (umk 2, dar 2, eink 1, mehr 1) | 8 → 8 (begr 2, fehl 1, par 1, trans 1, verk 1, rück 1, prüf 1) | 2 | 8 |
| spiegeln | Einen Punkt an der x- oder y-Achse spiegeln; erkennen, welche Koordinate das Vorzeichen wechselt. / Scheitel einer gespiegelten Parabel angeben, Gleichung des Bildes bestimmen. / Symmetrische Parabeln begründen, zwei Spiegelungen hintereinander, Schnittpunkt mit dem Bild, Spiegelung aus Bild und Urbild erschließen, Fehler „falsche Achse“, Parameter, Prüfungsaufgabe. | 6 → 5 (dir 4, erk 1) | 6 → 9 (mehr 6, dar 2, umk 1) | 8 → 8 (begr 2, verk 2, rück 1, fehl 1, par 1, prüf 1) | 2 | 2 |
| kombiniert | Den Scheitel von a(x − d)² + e ablesen; Öffnung und Streckung erkennen. / Gleichung aus einer Beschreibung von Spiegeln, Strecken und Verschieben, y-Werte berechnen, Scheitel am Bild, Verschiebungsvektor. / Fehler beim Scheitelablesen, Gleichung aus Scheitel und Punkt, a und e aus zwei Punkten, Nullstellen, gleicher Scheitel begründen, Bedingung ohne Nullstellen, Prüfungsaufgabe. | 6 → 6 (dir 5, erk 1) | 7 → 10 (mehr 7, dar 2, umk 1) | 8 → 8 (fehl 2, rück 2, verk 1, begr 1, par 1, prüf 1) | 2 | 1 |
| punkte | Einen Punkt bei g(x) = f(x) + c oder f(x − d) mitverschieben; Verschiebungsrichtung erkennen. / Punkte bei a · f(x − d) + e abbilden, Bildpunkt auswählen, Wert von f aus g zurückrechnen, Scheitelform aus f = x². / Fehler bei der Richtung von f(x ± d), Urpunkt aus dem Bildpunkt, Scheitel nach mehreren Schritten, Fixpunkt begründen, Parameter für die Lage auf der y-Achse, Prüfungsaufgabe. | 6 → 6 (dir 5, erk 1) | 7 → 7 (mehr 5, dar 1, umk 1) | 8 → 8 (fehl 2, rück 2, verk 1, begr 1, par 1, prüf 1) | 2 | 3 |

### gleichungen.reinquadratisch

Neue Übungen 41, Knobel-Bordkarten 12, überzählig 41.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| schaetzen | Eine Wurzel zwischen zwei ganze Zahlen setzen, näher liegende Zahl erkennen, mit dem Taschenrechner runden. / Ganze Zahlen zwischen zwei Wurzeln, Wurzeln und Dezimalzahlen ordnen, Seite eines Feldes einschätzen, auf Zehntel eingrenzen, größte Zahl unter einer Grenze. / Fehler „Wurzel ist die Hälfte“, Anzahl ganzer Zahlen zwischen Wurzeln, √(a + b) ≠ √a + √b begründen, √a < a nur für a > 1, Mindestseite eines Rahmens, Prüfungsaufgabe. | 6 → 6 (dir 4, erk 2) | 6 → 6 (mehr 3, umk 2, eink 1) | 8 → 8 (fehl 2, begr 2, verk 1, par 1, trans 1, prüf 1) | 2 | 7 |
| grundform | x² = a mit Quadratzahl a lösen; Anzahl der Lösungen erkennen. / Brüche und Dezimalzahlen, a aus den Lösungen, Schnitt einer Parabel mit einer Waagrechten, Fenster als Sachsituation. / Fehler „nur die positive Lösung“, Bedingungen an a, Summe der Lösungen begründen, Produkt aus Gegenzahlen, Umfang aus der Fläche, Prüfungsaufgabe. | 6 → 7 (dir 4, erk 3) | 7 → 6 (umk 2, mehr 2, eink 1, dar 1) | 8 → 8 (fehl 2, par 2, begr 1, trans 1, verk 1, prüf 1) | 2 | 8 |
| umformen | Gleichungen wie x² + c = d oder a · x² = b auf x² = … bringen und lösen; ersten Schritt erkennen. / x² auf beiden Seiten, Faktoren und Brüche, Fliesen als Sachsituation, c aus den Lösungen. / Fehler beim Teilen und beim gliedweisen Wurzelziehen, Sonderfall genau eine Lösung, Bedingung an c, Zahlenrätsel rückwärts, Quadrat plus Rechteck, (2x)², Prüfungsaufgabe. | 6 → 6 (dir 3, erk 3) | 6 → 10 (mehr 8, umk 1, eink 1) | 8 → 8 (fehl 2, begr 1, par 1, rück 1, trans 1, verk 1, prüf 1) | 2 | 6 |
| gerundet | Die positive Lösung von x² = a mit dem Taschenrechner auf eine Dezimale runden; die exakte Lösung √a erkennen. / Negative Lösung, zwei Dezimalen, erst umformen, Quadrat mit gleicher Fläche wie ein Rechteck, Zahl aus gerundeter Lösung. / Klammern, Kreis mit gleicher Fläche, Probe mit gerundeten Werten begründen, Rundungsfehler finden, mögliche c bei gegebenem Rundungswert, Prüfungsaufgabe. | 8 → 4 (dir 2, erk 2) | 6 → 7 (mehr 5, eink 1, umk 1) | 8 → 8 (verk 3, begr 2, fehl 1, par 1, prüf 1) | 2 | 8 |
| klammer | (x − d)² = c mit Quadratzahl c lösen: zwei Gleichungen aufschreiben. / Faktoren und Zahlen vor der Klammer, binomischen Term erkennen, vergrößerter Teppich. / Fehler „nur eine Lösung“, Bedingungen an q, Unterschied (x − 3)² = 16 und x − 3 = 4 begründen, Wurf als Modell, Abstand der Nullstellen, d aus den Lösungen, Prüfungsaufgabe. | 6 → 6 (dir 4, erk 2) | 6 → 6 (mehr 4, dar 1, eink 1) | 8 → 8 (par 2, fehl 1, begr 1, trans 1, verk 1, rück 1, prüf 1) | 2 | 8 |
| sachaufgabe | Seite eines Quadrats aus der Fläche und Fallzeit aus s = 5 · t² bestimmen; passende Gleichung erkennen. / Gerundete Seiten und Fallzeiten, Radius eines Beets, Fallweg aus der Zeit. / Verbreitertes Grundstück rückwärts, Fehler „π vergessen“, Würfel und Bremsweg als Modelle, Zeitdifferenzen, Vervierfachen begründen, Kreis mit dreifacher Fläche, Rechteck mit Seitenverhältnis, Prüfungsaufgabe Fall. | 7 → 5 (dir 4, erk 1) | 8 → 7 (eink 4, mehr 2, umk 1) | 8 → 10 (trans 3, fehl 2, verk 2, rück 1, begr 1, prüf 1) | 2 | 4 |

### gleichungen.wurzel

Neue Übungen 30, Knobel-Bordkarten 12, überzählig 22.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| definitionsmenge | Die Definitionsmenge von √(x ± c) angeben; erkennen, ob eine Zahl eingesetzt werden darf. / Radikanden mit Faktor vor x, Bereich am Zahlenstrahl, kleinste erlaubte ganze Zahl, Parameter aus der Definitionsmenge. / Definitionsmenge von Gleichungen mit zwei Wurzeln, Radikand mit −x, √(x²) begründen, Fehler beim Teilen, Bedingung an a, Prüfungsaufgabe. | 6 → 7 (dir 4, erk 3) | 9 → 7 (mehr 4, umk 2, dar 1) | 8 → 9 (verk 3, trans 2, begr 1, fehl 1, par 1, prüf 1) | 2 | 4 |
| quadrieren | √(x ± c) = d durch Quadrieren lösen und den ersten Schritt erkennen. / Faktoren und Dezimalzahlen im Radikanden, c aus einer Lösung, Zahlenrätsel. / Fehler „rechts nicht quadriert“, Wurzel aus einem Vielfachen, x² unter der Wurzel, √(x + 9) ≠ √x + 3, Parameter a, Zahlenrätsel rückwärts, Prüfungsaufgabe. | 6 → 5 (dir 4, erk 1) | 6 → 8 (mehr 6, umk 1, eink 1) | 8 → 8 (fehl 2, verk 2, begr 1, par 1, rück 1, prüf 1) | 2 | 5 |
| isolieren | Erst die Wurzel allein stellen (Zahl abziehen), dann quadrieren; ersten Schritt erkennen. / Faktoren vor der Wurzel, Teilen, Zahlenrätsel, c aus einer Lösung. / Fehler „sofort quadrieren“, Wurzel als neue Unbekannte, Wurzel mit Minus davor, Unmöglichkeit begründen, Bedingung an c, Prüfungsaufgabe mit Probe. | 6 → 5 (dir 4, erk 1) | 6 → 9 (mehr 7, umk 1, eink 1) | 8 → 9 (verk 3, fehl 2, trans 1, begr 1, par 1, prüf 1) | 2 | 2 |
| probe | Mit einer Probe prüfen, ob eine Zahl Lösung ist; leere Lösungsmenge bei negativer rechter Seite erkennen. / Definitionsmenge mitprüfen, isolieren und dann Unmöglichkeit erkennen, Gleichung zu einer Scheinlösung finden, unmögliches Zahlenrätsel. / Sinn der Probe begründen, Bedingung an c, Fehler „Scheinlösung angegeben“, Parameter aus zwei Quadrierlösungen rückwärts, quadratische Gleichung mit einer echten Lösung, Prüfungsaufgabe. | 6 → 7 (erk 4, dir 3) | 6 → 6 (mehr 4, umk 1, eink 1) | 8 → 8 (begr 2, fehl 2, par 1, rück 1, verk 1, prüf 1) | 2 | 3 |
| zwei_seiten | Gleichungen mit je einer Wurzel auf beiden Seiten quadrieren und lösen; ersten Schritt erkennen. / Wurzel = linearer Term: quadratische Gleichung lösen und Scheinlösung aussortieren, Zahlenrätsel, Parameter aus der Lösung. / Probe bei zwei Kandidaten begründen, √(2x + 3) = x, √(x²) = x begründen, Fehler beim Quadrieren von x ± 1, Parameter für jedes a, Quadrate gleicher Seite, Prüfungsaufgabe. | 6 → 7 (dir 6, erk 1) | 6 → 9 (mehr 7, eink 1, umk 1) | 8 → 8 (begr 3, verk 1, fehl 1, par 1, trans 1, prüf 1) | 2 | 3 |
| sachaufgabe | In t = √(h : 5), v = √(20h) oder a = √A eine Größe einsetzen und die andere bestimmen; die richtige Gleichung erkennen. / Vergrößertes Beet, Fallzeit aus der Höhe, Pendel und Ball als Sachsituation. / Wirkung von Verdoppeln begründen, Zeitunterschiede rückwärts, Horizont als Modell, v = h als Bedingung, Fehler „Quadrieren vergessen“, Prüfungsaufgabe. | 6 → 6 (dir 5, erk 1) | 8 → 6 (eink 3, mehr 2, umk 1) | 8 → 9 (verk 2, rück 2, trans 1, par 1, begr 1, fehl 1, prüf 1) | 2 | 5 |

### abbildungen.matrizen

Neue Übungen 33, Knobel-Bordkarten 12, überzählig 37.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| bildpunkt | Einen Punkt mit einer Matrix abbilden: Zeile mal Spalte; die richtige Rechnung erkennen. / Urpunkt aus dem Bildpunkt, Matrix aus den Abbildungsgleichungen, Bild aus den Bildern der Einheitspunkte, zweimal abbilden, Spiel-Verzerrung. / Parameter, Fixpunkt begründen, Fehler „Spalte statt Zeile“, Fläche des Bilds, Scherung als Modell, Abbilden und Verschieben rückwärts, Prüfungsaufgabe. | 6 → 5 (dir 4, erk 1) | 8 → 6 (umk 2, mehr 2, dar 1, eink 1) | 8 → 8 (par 2, begr 1, fehl 1, verk 1, trans 1, rück 1, prüf 1) | 2 | 11 |
| abbildungsmatrix | Mit gegebener Matrix spiegeln oder drehen; die Matrix einer Standardabbildung angeben und erkennen. / Streckungen und Affinitäten als Matrix, Matrix aus den Bildern von (1 | 0) und (0 | 1), Faktor aus einem Punktpaar, Bildvergrößerung. / Fehler „90° statt −90°“ und „falsche Spiegelachse“, Doppelte Abbildungen begründen, Spiegelung an y = −x herleiten, Flächenfaktor, Verkleinerung als Bedingung, Prüfungsaufgabe. | 6 → 14 (dir 9, erk 5) | 9 → 6 (mehr 2, umk 2, dar 1, eink 1) | 8 → 8 (fehl 2, begr 2, trans 1, par 1, verk 1, prüf 1) | 2 | 0 |
| drehung | Einen Punkt auf der x-Achse mit der Drehmatrix drehen und x′ oder y′ berechnen; die Drehmatrix erkennen. / Beliebige Punkte drehen, exakt um 90° drehen, Drehwinkel aus Bild und Urbild, Gondel eines Riesenrads. / Abstand bleibt – begründen und nutzen, Winkel rückwärts aus einer Koordinate, Drehsymmetrie, Fehler beim Drehsinn, Bereich der Drehwinkel, Prüfungsaufgabe. | 6 → 5 (dir 4, erk 1) | 8 → 7 (mehr 5, umk 1, eink 1) | 8 → 9 (verk 3, rück 1, begr 1, trans 1, fehl 1, par 1, prüf 1) | 2 | 5 |
| rechnen | Matrizen addieren und mit einer Zahl multiplizieren; den Eintrag eines Produkts erkennen. / Matrizen multiplizieren, fehlende Matrix bei einer Summe, Einkaufskosten als Matrix mal Vektor. / Vertauschbarkeit prüfen, Verkettung von Abbildungen, Drehung zweimal, Parameter für AB = BA, Fehler „eintragsweise multipliziert“, Prüfungsaufgabe. | 6 → 5 (dir 4, erk 1) | 7 → 6 (mehr 4, eink 1, umk 1) | 8 → 9 (begr 3, verk 3, par 1, fehl 1, prüf 1) | 2 | 6 |
| inverse | Die Determinante einer Matrix berechnen; erkennen, wann es keine Inverse gibt. / Inverse Matrix berechnen, Urpunkt mit der Inversen, einfacher Code entschlüsseln. / Parameter ohne Inverse und mit Determinante 1, Drehung rückgängig begründen, Fehler beim Bilden der Inversen, Flächenfaktor, zweimal abgebildet rückwärts, Prüfungsaufgabe. | 6 → 4 (dir 2, erk 2) | 6 → 6 (mehr 3, umk 2, eink 1) | 8 → 8 (par 3, begr 1, fehl 1, verk 1, rück 1, prüf 1) | 2 | 9 |
| skalarprodukt | Das Skalarprodukt zweier Vektoren berechnen und damit „senkrecht“ erkennen. / Parameter für senkrecht, Winkel aus dem Skalarprodukt, Betrag eines Vektors, Arbeit einer Kraft. / Fehler „Vektor statt Zahl“, rechter Winkel im Dreieck, Winkel aus Beträgen, senkrechter Vektor mit Vorgabe, Vorzeichen deuten, Prüfungsaufgabe. | 6 → 4 (dir 2, erk 2) | 6 → 6 (mehr 3, umk 2, eink 1) | 8 → 8 (fehl 2, par 2, verk 1, rück 1, begr 1, prüf 1) | 2 | 6 |

### funktionen.umkehr

Neue Übungen 28, Knobel-Bordkarten 12, überzählig 25.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| umkehrbar | Entscheiden, ob eine Funktion umkehrbar ist (jeder y-Wert nur einmal); Test mit der waagrechten Geraden. / Umkehrbarkeit an Tabelle und Graph, Einschränkung der Definitionsmenge finden, Automat als Sachsituation. / Fehler „zu jedem x genau ein y“, kleinstes a für einen Parabelast, monotone Funktionen begründen, x³ einordnen, Wert streichen, Prüfungsaufgabe. | 6 → 7 (erk 6, dir 1) | 6 → 7 (dar 4, umk 2, eink 1) | 8 → 8 (fehl 2, begr 2, par 1, verk 1, trans 1, prüf 1) | 2 | 2 |
| werte | f⁻¹ an einer Stelle aus einer Tabelle ablesen; f(a) = b ⇔ f⁻¹(b) = a erkennen. / f⁻¹(c) bei Geraden berechnen, Definitions- und Wertemenge tauschen, Taxitarif rückwärts. / f⁻¹(f(a)) begründen, f = f⁻¹ als Gleichung, doppelte Anwendung rückwärts, verschobene Umkehrfunktion, Fehler „f statt f⁻¹“, Temperatur umrechnen, Prüfungsaufgabe. | 6 → 4 (dir 2, erk 2) | 8 → 10 (mehr 6, umk 3, eink 1) | 8 → 8 (verk 2, begr 1, rück 1, par 1, fehl 1, trans 1, prüf 1) | 2 | 6 |
| linear | Die Umkehrfunktion einer Geraden durch Tauschen und Auflösen bestimmen; die richtige erkennen. / Umkehrfunktion aus zwei Punkten oder einer Tabelle, m aus der Umkehrfunktion, Steigung der Umkehrfunktion, Tarif umkehren. / Fehler mit einer Probe aufdecken, selbstumkehrende Geraden, Schnittpunkt mit f⁻¹, Parameter t, Kerze als Modell, f aus f⁻¹ zurückrechnen, Prüfungsaufgabe. | 6 → 9 (dir 7, erk 2) | 8 → 6 (umk 2, mehr 2, eink 1, dar 1) | 8 → 8 (fehl 2, begr 1, verk 1, par 1, trans 1, rück 1, prüf 1) | 2 | 5 |
| quadratisch | Bei f(x) = x² (x ≥ 0) Werte von f⁻¹ = √x berechnen und die Umkehrfunktion erkennen. / Verschobene Parabeläste, Umkehrfunktion auswählen, Punkte spiegeln. / Definitions- und Wertemenge von f⁻¹, Einschränkung begründen, rückwärts aus f⁻¹(x), linker Ast, Fehler beim Vertauschen von d und e, Prüfungsaufgabe. | 6 → 4 (dir 3, erk 1) | 6 → 8 (mehr 3, dar 3, umk 2) | 8 → 8 (verk 2, begr 2, rück 1, trans 1, fehl 1, prüf 1) | 2 | 3 |
| exp_log | Logarithmen als Werte der Umkehrfunktion von bˣ berechnen; log_b x als Umkehrfunktion erkennen. / Verschobene Exponentialfunktionen umkehren, Punkte auf den Logarithmusgraphen übertragen, Verdopplung rückwärts. / Fehler log₅ 25 = 5, Umkehrfunktion mit Verschiebung, Definitionsmenge begründen, negative Logarithmen, Basis als Parameter, rückwärts aus f⁻¹, Prüfungsaufgabe. | 6 → 7 (dir 6, erk 1) | 8 → 9 (mehr 6, dar 2, eink 1) | 8 → 8 (verk 3, fehl 1, begr 1, par 1, rück 1, prüf 1) | 2 | 2 |
| spiegeln | Einen Punkt von f auf f⁻¹ übertragen (Koordinaten tauschen) und an y = x spiegeln. / Punkte am Bild übertragen, Achsenschnittpunkte von f⁻¹ bestimmen, sichere Punkte von f⁻¹ finden. / Selbstumkehrende Funktion und Punkte auf y = x begründen, Fehler „Vorzeichen statt Tauschen“, Fläche bleibt, Parameter für einen Punkt auf y = x, Abstand gespiegelter Punkte, Spiegeln und Verschieben rückwärts, Prüfungsaufgabe. | 6 → 4 (dir 2, erk 2) | 6 → 7 (umk 3, dar 2, mehr 2) | 9 → 8 (begr 2, fehl 1, verk 1, par 1, trans 1, rück 1, prüf 1) | 2 | 7 |

### mengen.grundbegriffe

Neue Übungen 18, Knobel-Bordkarten 10, überzählig 7.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| elemente | Mit ∈ und ∉ entscheiden, ob eine Zahl zu einer Menge gehört; Elemente einer kleinen Menge zählen. / Mengen in Worten aufzählen und zählen, Beschreibung zu einer Aufzählung finden, Menge aus einer Klassenliste. / Gleiche Mengen und doppelte Elemente begründen, Fehler „1 vergessen“, Quersummen- und Quadratbedingungen als neue Beschreibung, gerade Primzahlen, Zahl mit 5 Teilern rückwärts. | 8 → 8 (erk 7, dir 1) | 8 → 8 (mehr 6, umk 1, eink 1) | 8 → 8 (begr 2, trans 2, verk 2, rück 1, fehl 1) | 2 | 2 |
| schnitt | Die Schnittmenge zweier aufgezählter Mengen bestimmen und das Zeichen ∩ erkennen. / Schnittmengen von Mengen in Worten, Kinder in zwei AGs, eine passende Menge B zu einer Schnittmenge. / Gemeinsame Teiler und Vielfache, Teilmengen begründen, Fehler „∩ mit ∪ verwechselt“, Folgerungen über eine Person, Prüfungsaufgabe. | 6 → 7 (dir 6, erk 1) | 8 → 11 (mehr 8, eink 2, umk 1) | 8 → 8 (verk 2, begr 2, trans 1, fehl 1, par 1, prüf 1) | 2 | 0 |
| vereinigung | Die Vereinigung zweier aufgezählter Mengen bilden und zählen; das Zeichen ∪ erkennen. / Vereinigungen von Mengen in Worten, Anzahlformel n(A) + n(B) − n(A ∩ B), Sachsituationen „mindestens eines“, fehlende Anzahlen rückwärts. / Disjunkte Mengen und Höchstzahl begründen, Fehler „Überlappung addiert“, Teiler zweier Zahlen, Hotelpersonal als Modell, Mengen aus Angaben rekonstruieren, Prüfungsaufgabe. | 6 → 7 (dir 6, erk 1) | 9 → 13 (mehr 6, eink 5, umk 2) | 8 → 8 (begr 2, rück 2, fehl 1, verk 1, trans 1, prüf 1) | 2 | 0 |
| venn | Anzahlen aus einem Venn-Diagramm ablesen; das richtige Feld erkennen. / Felder zusammenzählen (insgesamt, genau eins, nicht A), „nur A“ aus Angaben, weder noch, fehlende Zahl außen. / Überlappung rückwärts aus „keines“, Gleichung mit x, nur Gemüse ohne „keines“, Unmöglichkeit begründen, Prozentanteil, Mindest-Überlappung, Fehler beim Eintragen, Prüfungsaufgabe. | 6 → 7 (dir 6, erk 1) | 10 → 13 (dar 6, eink 4, mehr 2, umk 1) | 8 → 8 (rück 2, par 1, begr 1, verk 1, trans 1, fehl 1, prüf 1) | 2 | 0 |
| verstehen | Erkennen, dass A ∩ B höchstens so groß ist wie die kleinere Menge; leere Schnittmengen erkennen. / Teilmengen in Vereinigung und Schnitt nutzen, Elemente aus Bedingungen rückwärts, AG-Situation als Mengenaussage. / Mindest- und Höchstzahlen begründen, Fehler bei Formel und Venn-Diagramm finden, allgemeine Aussagen prüfen, aus n(A ∪ B) = n(A) folgern. | 6 → 5 (erk 4, dir 1) | 9 → 6 (mehr 4, umk 1, eink 1) | 8 → 10 (fehl 3, par 3, begr 3, trans 1) | 2 | 5 |

### groessen.verhaeltnisse

Neue Übungen 29, Knobel-Bordkarten 12, überzählig 25.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| kuerzen | Ein Verhältnis aus einer Sachsituation aufstellen und vollständig kürzen; das gekürzte Verhältnis erkennen. / Große Zahlen und verschiedene Einheiten kürzen, Verhältnis in einen Anteil umwandeln, ungekürzte Zahl rückwärts. / Drei Größen, Dezimalzahlen und Brüche im Verhältnis, Änderung eines Verhältnisses rückwärts, Fehler „nicht vollständig gekürzt“, Unkürzbarkeit begründen, Prüfungsaufgabe. | 6 → 6 (dir 5, erk 1) | 7 → 9 (mehr 7, dar 1, umk 1) | 8 → 8 (trans 2, verk 2, rück 1, fehl 1, begr 1, prüf 1) | 2 | 3 |
| gleichwertig | Gleichwertige Verhältnisse durch Erweitern ergänzen und erkennen. / Mischungen vergleichen, Rezept mit drei Zutaten, Gesamtzahl aus einem Teil, Modellmaßstab, Verhältnis aus einem Bild. / Fehler „addieren statt multiplizieren“, x : 3 = 12 : x, Mischung nachbessern, Prozent als Verhältnis, Sirupmenge rückwärts, Prüfungsaufgabe. | 6 → 6 (dir 4, erk 2) | 7 → 6 (eink 3, mehr 2, dar 1) | 8 → 8 (fehl 2, par 1, begr 1, trans 1, verk 1, rück 1, prüf 1) | 2 | 7 |
| aufteilen | Eine Größe im Verhältnis zweier Zahlen aufteilen; die Zahl der Teile erkennen. / Sachsituationen mit Teig, Gewinn und Seil, drei Personen, Gesamtmenge aus einem Teil. / Gesamtmenge aus Unterschied und kleinstem Anteil, Rechteck mit Umfang, Fehler „durch jede Zahl einzeln geteilt“, Hälfte begründen, Parameter k, Gewinn nach Einsatz, Prüfungsaufgabe. | 6 → 4 (dir 3, erk 1) | 6 → 9 (eink 6, umk 2, mehr 1) | 8 → 9 (rück 3, verk 1, fehl 1, begr 1, par 1, trans 1, prüf 1) | 2 | 5 |
| proportion | Eine Proportion lösen und Rezeptmengen mit dem Dreisatz umrechnen; die passende Proportion erkennen. / Krumme Faktoren, Verbrauch eines Autos, Kartenmaßstab in beide Richtungen. / Nicht proportionale Situationen begründen, indirekte Proportionalität, Wechselkurs und Poster als Modell, Maßstab rückwärts, Fehler „addiert statt multipliziert“, Prüfungsaufgabe Karte. | 6 → 4 (dir 3, erk 1) | 7 → 10 (mehr 5, eink 2, umk 2, dar 1) | 8 → 8 (begr 2, trans 2, verk 1, rück 1, fehl 1, prüf 1) | 2 | 2 |
| einheitsrate | Den Wert für eine Einheit bestimmen (pro Stunde, pro Stück, pro kg) und anwenden; eine Einheitsrate erkennen. / Preise pro 100 g, Angebote vergleichen, Aktion „4 für 3“, Reichweite aus dem Verbrauch. / Mehrere Angebote, Ersparnis pro Stück und Liter, Seiten pro Minute, Geschwindigkeiten vergleichen, Fehler „Gesamtpreis verglichen“, gleich teurer Preis als Parameter, Prüfungsaufgabe. | 8 → 9 (dir 8, erk 1) | 6 → 6 (mehr 4, eink 1, umk 1) | 8 → 10 (trans 3, verk 3, begr 1, fehl 1, par 1, prüf 1) | 2 | 1 |
| aenderung | Eine Änderungsrate aus Anfangs- und Endwert berechnen; schneller und langsamer erkennen. / Negative Raten, Werte aus der Rate berechnen, Rate aus einer Tabelle, Leerlaufen eines Pools. / Anfangswert rückwärts, gleiche Höhe zweier Kerzen, Bedeutung einer negativen Rate, Fehler beim Vorzeichen, Bereich für die Rate, Akku als Modell, Prüfungsaufgabe. | 9 → 5 (dir 4, erk 1) | 7 → 8 (mehr 3, umk 3, eink 1, dar 1) | 8 → 8 (rück 2, verk 1, begr 1, fehl 1, par 1, trans 1, prüf 1) | 2 | 7 |

### 3) Zahlen

| | Anzahl |
|---|---|
| Themen | 12 |
| Lernkarten | 68 |
| neue Übungen | 342 |
| Knobel-Bordkarten | 138 (2 je Lernkarte) |
| überzählig (ohne g) | 330 |

Je Thema (neu / Knobel / überzählig):
- abbildungen.determinanten2: 40 / 12 / 55
- abbildungen.vektoren: 29 / 12 / 47
- daten.stichproben: 20 / 10 / 10
- funktionen.scharen: 24 / 12 / 16
- terme.quadratische_extreme: 27 / 10 / 27
- funktionen.transformation: 23 / 12 / 18
- gleichungen.reinquadratisch: 41 / 12 / 41
- gleichungen.wurzel: 30 / 12 / 22
- abbildungen.matrizen: 33 / 12 / 37
- funktionen.umkehr: 28 / 12 / 25
- mengen.grundbegriffe: 18 / 10 / 7
- groessen.verhaeltnisse: 29 / 12 / 25

### 4) Überzählig
Vollständige Liste mit Fragetext: `inhalte/postfach/stufen-rsib-1-ueberzaehlig.md`. Fast alle stammen aus Vorlagen mit Zufallszahlen, z. B.:
- „Berechne die Determinante der Vektoren …“ (12-mal);
- „Löse x² = …“;
- „Ergänze zu einem vollständigen Quadrat.“

### 5) Quellen der Prüfungsvorbilder
Nachgebaut wurde der Typ, nie Wortlaut oder Zahlen.
- **Realschule Bayern, Abschlussprüfung Mathematik I (ISB):** mehrteilige Aufgaben mit a) b) c) zu Funktionen, Vektoren, Determinanten/Flächen und Abbildungen. Gelesen: Aufgabenübersicht und Lösungsmuster 2019–2025 sowie Muster 2021.
  - https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2021/2021_mi_nt_l.pdf
  - https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Leistungserhebungen/Abschlusspruefung/Mathematik/2023/2023_mi_ht_l.pdf
  - https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Muster-Abschlusspruefungen_I/mi_muster2021_a.pdf
- **IB MYP:** On-screen-Examen in Mathematik und Extended Mathematics; Typen „Sets and Venn diagrams“, Anzahlformel n(A ∪ B), Verhältnisse/Raten.
  - https://www.ibo.org/globalassets/new-structure/brochures-and-infographics/pdfs/myp-brief-mathematics-en.pdf
  - https://sites.google.com/view/mathsismybuzz/ibmyp-maths-eassessment
  - https://www.iitianacademy.com/ib-myp-3-mathematics-study-notes-topic-wise-revision/ib-myp-3-mathematics-2-4-problem-solving-with-sets-and-venn-diagrams-study-notes/
- **Knobel-Bordkarten** (Vorbild für die Art):
  - Känguru der Mathematik (Benjamin/Kadett): https://www.profved.com/wp-content/uploads/2024/12/2023_Benjamin.pdf
  - Mathematik-Olympiade, Schulrunde: https://www.gymnasiumkerpen.eu/medien/2021-2022/2021_09_15_mathematikolympiade_aufgaben.pdf

### 6) Drei Beispiel-Bordkarten je Stufe (groessen.verhaeltnisse, Lernkarte „aufteilen“, Wortlaut)
**Stufe 1**
- (direkt) „Teile 110 im Verhältnis 7 : 4 auf.“ – 70 und 40
- (erkennen) „110 € sollen im Verhältnis 7 : 4 aufgeteilt werden. In wie viele gleiche Teile teilt man zuerst?“ – in 11 Teile
- (direkt) „Verteile 60 Murmeln im Verhältnis 1 : 2.“ – 20 und 40

**Stufe 2**
- (einkleidung) „Für einen Teig werden Mehl und Zucker im Verhältnis 5 : 1 gemischt, zusammen 450 g. Wie viel Gramm Zucker sind es?“ – 75 g
- (umkehr) „Wasser und Saft werden im Verhältnis 2 : 1 gemischt. Es werden 200 ml Wasser verwendet. Wie viel ml Getränk entstehen insgesamt?“ – 300 ml
- (mehrschritt) „240 € werden im Verhältnis 6 : 1 : 5 auf drei Personen verteilt. Wie viel bekommt jede?“ – 120 €, 20 € und 100 €

**Stufe 3**
- (rueckwaerts) „Ein Erbe wird im Verhältnis 2 : 3 : 5 verteilt. Der kleinste Anteil beträgt 4 000 €. Wie groß ist das Erbe insgesamt?“ – 20 000 €
- (parameter) „400 € werden im Verhältnis 3 : k aufgeteilt. Der erste Anteil ist 120 €. Wie groß ist k?“ – 7
- (fehler) „Jemand teilt 90 € im Verhältnis 2 : 1 so auf: 90 : 2 = 45 € und 90 : 1 = 90 €. Was stimmt?“ – Falsch: Es gibt 3 Teile zu je 30 €, also 60 € und 30 €.

**Knobel (Pool bonus)**
- „Ein Betrag wird im Verhältnis 3 : 5 geteilt. Bei einer Teilung im Verhältnis 1 : 1 bekäme der Erste 30 € mehr. Wie groß ist der Betrag?“ – 240 €
  - Tipp: Wie viele Teile bekommt der Erste jeweils?

## 2026-11-17 22:10 – STATUS
groessen.verhaeltnisse fertig: 29 neue Übungen, 12 Knobel-Bordkarten, 25 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 21:40 – STATUS
mengen.grundbegriffe fertig: 18 neue Übungen, 10 Knobel-Bordkarten, 7 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 21:05 – STATUS
funktionen.umkehr fertig: 28 neue Übungen, 12 Knobel-Bordkarten, 25 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 20:30 – STATUS
abbildungen.matrizen fertig: 33 neue Übungen, 12 Knobel-Bordkarten, 37 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 19:55 – STATUS
gleichungen.wurzel fertig: 30 neue Übungen, 12 Knobel-Bordkarten, 22 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 19:25 – STATUS
gleichungen.reinquadratisch fertig: 41 neue Übungen, 12 Knobel-Bordkarten, 41 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 18:50 – STATUS
funktionen.transformation fertig: 23 neue Übungen, 12 Knobel-Bordkarten, 18 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 18:15 – STATUS
terme.quadratische_extreme fertig: 27 neue Übungen, 10 Knobel-Bordkarten, 27 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 17:40 – STATUS
funktionen.scharen fertig: 24 neue Übungen, 12 Knobel-Bordkarten, 16 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 17:05 – STATUS
daten.stichproben fertig: 20 neue Übungen, 10 Knobel-Bordkarten, 10 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 16:35 – STATUS
abbildungen.vektoren fertig: 30 neue Übungen, 12 Knobel-Bordkarten, 47 überzählig. inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 16:10 – STATUS
abbildungen.determinanten2 fertig: 40 neue Übungen, 12 Knobel-Bordkarten, 55 überzählig (ohne g, nicht gelöscht). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis gegen origin/lernen-app OK (alte Aufgaben nur g/s geändert).
