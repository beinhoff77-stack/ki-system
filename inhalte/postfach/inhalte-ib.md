# Postfach inhalte-ib (Paket IB, Vierte Runde)

Neueste Meldung oben.

## 2026-11-14 15:43 – FERTIG
Paket IB abgeschlossen: 14 Themen, 72 Lernkarten, 2 016 Aufgaben, alle mit `python3 -I tools/inhalt_pruefen.py` OK (Zweig `inhalte-ib`, je Thema ein Commit; dazu zwei Nachbesserungs-Commits für Zeichnungen).

| Thema | klasse | Karten | Aufgaben | Lernkarten |
|---|---|---|---|---|
| mengen.grundbegriffe | ib_myp 1 | 5 | 140 | Elemente, Schnitt, Vereinigung, Venn-Diagramm, Aussagen prüfen |
| groessen.verhaeltnisse | ib_myp 2 | 6 | 168 | Kürzen, gleichwertig, aufteilen, Proportion, Einheitsrate, Änderungsrate |
| daten.zweidimensional | ib_myp 3 | 5 | 140 | Streudiagramm, Zusammenhang, Ausgleichsgerade, Ausreißer, Korrelation/Kausalität |
| daten.standardabweichung | ib_myp 4 | 5 | 140 | Abweichung, Varianz, σ, Eigenschaften, Deuten |
| stochastik.bedingt | ib_myp 4 | 6 | 168 | Vierfeldertafel, Formel, ohne Zurücklegen, Unabhängigkeit, Rückschluss (1 000 Fälle), Bedingung lesen |
| funktionen.betrag | ib_myp 4 | 5 | 140 | Betrag, Graph/Knick, stückweise, Gleichungen, Aussagen |
| funktionen.folgen | ib_myp 4 | 5 | 140 | explizit, rekursiv, arithmetisch, geometrisch, erkennen |
| funktionen.reihen | ib_myp 4 | 5 | 140 | Summenzeichen, arithm. Reihe, geom. Reihe, Sachaufgaben, Fehler finden |
| sonder.graphentheorie | ib_myp 4 | 5 | 140 | Grad/Handschlag, Euler, kürzeste Wege, Spannbaum (Kruskal), Aussagen |
| sonder.optimierung | ib_myp 4 | 5 | 140 | Bereich, Bedingungen aufstellen, Ecken, Eckenprinzip, Sachaufgaben |
| daten.normalverteilung | zusatz 10 | 5 | 140 | Glockenkurve, 68-95-99,7, Teilanteile, z-Wert, Vergleichen |
| finanzen.zinseszins | zusatz 10 | 5 | 140 | Jahr für Jahr, Faktor q, Kₙ = K₀ · qⁿ, rückwärts, Angebote/Verdopplung |
| sonder.logik | zusatz 10 | 5 | 140 | Aussagen, Verneinung, und/oder, Wahrheitstafel, wenn–dann |
| zahlen.schranken | zusatz 10 | 5 | 140 | Schranken, Messgenauigkeit, Summen/Differenzen, Produkte/Quotienten, Entscheiden |

Umgesetzt:
- Fachbegriffe deutsch, IB-Begriff beim ersten Auftreten englisch in Klammern. Jede Karte mit Alltagsbeispiel, typischem Fehler mit Zahlen; Stufe 3 mit Fehler finden, Umkehr- oder Sachaufgaben; falsche Antworten aus typischen Denkfehlern.
- Zeichnungen: Venn-Diagramme (figur, Beschriftung über unsichtbare Hilfskreise mit Radius 0 – keine Punkt-Marker), Graphen der Graphentheorie (figur mit Kantengewichten), Streudiagramme, V-Graphen der Betragsfunktion (zwei Geradenstücke), Randgeraden der Optimierung, Baumdiagramme, Tabellen. Alle Zeichenarten mit dem Original-Zeichencode aus lernen.js gerendert und angesehen.
- klasse `{"zusatz": 10}` bei den vier Themen ohne Zuordnung (bestätigt in antworten.md, 15:30).

Offen / App-Wünsche (Details je Datei unter "offen"):
- App-Wunsch: Halbebenen bzw. zulässigen Bereich füllen (sonder.optimierung).
- App-Wunsch: Graphart Glockenkurve mit färbbarer Fläche (daten.normalverteilung); bisher Säulendiagramm in Glockenform.
- App-Wunsch (optional): eigene Zeichenart „venn“; Bereich auf dem Zahlenstrahl markieren (zahlen.schranken); Formeldarstellung für ∑ mit Grenzen über/unter dem Zeichen.
- Inhaltliche Annahmen: σ der Gesamtheit (durch n); unendliche geometrische Reihen nicht enthalten; Reihen/Summen nur in funktionen.reihen (nicht in folgen); Graphentheorie ohne Hamiltonkreise; Optimierung ohne Isogewinngeraden; Normalverteilung nur mit 68-95-99,7-Regel.
- Schreibweise P(A | B) (IB) statt P_B(A); Überschneidung mit stochastik.verknuepft (Kl. 9) bewusst, hier ausführlicher.
- Indizes als Unicode (a₅, aₙ₊₁, ∑ₖ₌₁⁵) – bitte in der App-Schrift prüfen.
- Hilfsdatei: nur inhalte/generatoren/_ib.py; keine fremden Dateien geändert.

## 2026-11-14 15:41 – STATUS
14/14 zahlen.schranken fertig: 5 Lernkarten (Schranken, Messgenauigkeit, Summen/Differenzen, Produkte/Quotienten, Entscheiden im ungünstigsten Fall), 140 Aufgaben, Prüfskript OK. klasse = {"zusatz": 10}.

## 2026-11-14 15:39 – STATUS
13/14 sonder.logik fertig: 5 Lernkarten (Aussagen, Verneinung, und/oder, Wahrheitstafeln, wenn–dann), 140 Aufgaben, Prüfskript OK. Wahrheitswerte in Lücken als 1/0. klasse = {"zusatz": 10}.

## 2026-11-14 15:37 – STATUS
12/14 finanzen.zinseszins fertig: 5 Lernkarten (Jahr für Jahr, Wachstumsfaktor, Kₙ = K₀ · qⁿ, rückwärts, Angebote/Verdopplung), 140 Aufgaben, Prüfskript OK. klasse = {"zusatz": 10}.

## 2026-11-14 15:35 – STATUS
11/14 daten.normalverteilung fertig: 5 Lernkarten (Glockenkurve, 68-95-99,7-Regel, Teilanteile, z-Wert, Vergleichen), 140 Aufgaben, Prüfskript OK. klasse = {"zusatz": 10} (siehe FRAGE). App-Wunsch (offen): Graphart Glockenkurve mit färbbarer Fläche.

## 2026-11-14 15:33 – STATUS
10/14 sonder.optimierung fertig: 5 Lernkarten (Punkt im Bereich, Bedingungen aufstellen, Ecken, Eckenprinzip, Sachaufgaben), 140 Aufgaben, Randgeraden gezeichnet, Prüfskript OK. App-Wunsch (offen): zulässigen Bereich füllen.

## 2026-11-14 15:29 – STATUS
9/14 sonder.graphentheorie fertig: 5 Lernkarten (Knoten/Kanten/Grad, Euler, kürzeste Wege, minimaler Spannbaum, Aussagen prüfen), 140 Aufgaben mit gezeichneten Graphen (figur), Prüfskript OK.

## 2026-11-14 15:26 – STATUS
8/14 funktionen.reihen fertig: 5 Lernkarten (Summenzeichen, arithmetische und geometrische Reihen, Sachaufgaben, Fehler finden), 140 Aufgaben, Prüfskript OK. Unendliche geometrische Reihe nicht enthalten (offen).

## 2026-11-14 15:24 – STATUS
7/14 funktionen.folgen fertig: 5 Lernkarten (explizit, rekursiv, arithmetisch, geometrisch, erkennen/Fehler finden), 140 Aufgaben, Prüfskript OK. Summen/Reihen bewusst ins Thema funktionen.reihen verschoben (offen).

## 2026-11-14 15:22 – STATUS
6/14 funktionen.betrag fertig: 5 Lernkarten (Betrag berechnen, Graph/Knickpunkt, stückweise, Betragsgleichungen, Aussagen prüfen), 140 Aufgaben, V-Graphen aus zwei Geradenstücken, Prüfskript OK.

## 2026-11-14 15:21 – STATUS
5/14 stochastik.bedingt fertig: 6 Lernkarten (Vierfeldertafel, Formel, Ziehen ohne Zurücklegen, Unabhängigkeit, Rückschluss mit 1 000 Fällen, Bedingungen lesen), 168 Aufgaben mit Tafeln und Baumdiagrammen, Prüfskript OK. Schreibweise P(A | B) wie im IB – Hinweis unter offen.

## 2026-11-14 15:18 – STATUS
4/14 daten.standardabweichung fertig: 5 Lernkarten (Abweichungen, Varianz, σ, Eigenschaften, Deuten), 140 Aufgaben, Prüfskript OK. σ der Gesamtheit (durch n), Annahme unter offen.

## 2026-11-14 15:16 – STATUS
3/14 daten.zweidimensional fertig: 5 Lernkarten (Streudiagramm lesen, Art des Zusammenhangs, Ausgleichsgerade, Ausreißer, Korrelation/Kausalität), 140 Aufgaben mit Streudiagrammen, Prüfskript OK.

## 2026-11-14 15:12 – STATUS
2/14 groessen.verhaeltnisse fertig: 6 Lernkarten (kürzen, gleichwertig, aufteilen, Proportionen, Einheitsraten, Änderungsraten), 168 Aufgaben, Prüfskript OK. Hilfsfunktion eu() für Geldbeträge in _ib.py ergänzt.

## 2026-11-14 15:09 – STATUS
1/14 mengen.grundbegriffe fertig: 5 Lernkarten, 140 Aufgaben, Prüfskript OK. Venn-Diagramme als figur (Kreise + Rechteck). Hilfsdatei inhalte/generatoren/_ib.py angelegt.

## 2026-11-14 15:09 – FRAGE
Vier Themen haben in themenliste.json `klasse: {}` (daten.normalverteilung, finanzen.zinseszins, sonder.logik, zahlen.schranken). Das Prüfskript verlangt ein nicht leeres Feld.
- Annahme: dort `"klasse": {"zusatz": 10}` (Niveau Klasse 9/10 laut Auftrag; die App wertet nur gym_by/rs_by/ib_myp als Schulart aus, der Schlüssel stört also nicht). Gesetzt in `_ib.py` (KLASSE_OHNE).
- Ich arbeite damit weiter. Bitte melden, falls ein anderer Wert gewünscht ist – dann nur KLASSE_OHNE ändern und die vier Generatoren neu laufen lassen.
