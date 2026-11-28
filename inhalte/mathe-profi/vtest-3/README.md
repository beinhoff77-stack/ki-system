# Runde vtest-3 (VT3) – Verstehen in Tests, Stufe 1

126 neue Aufgaben (VT3-001 … VT3-126), nichts eingespielt. 18 Verstehens-Lernziele laut `inhalte/mathe-profi/vtest-1/auswahl.json`, keine Abweichung (siehe `auswahl.md`). Je Lernziel: 1 `test` (`ersetzt_test`), 3 `korrektur`, 3 `sicherung`.

Dateien: `auswahl.md`, fünf Aufgabendateien `<einheit>.json`, Bauskript `bauen.py` mit `kern.py`, `ideen.py` und `e_*.py` (Quelltexte), `gegenrechnung.py`, `sonderfaelle.md`. Jede Aufgabe trägt ein Zusatzfeld `idee` (Denkfigur: Kategorie | Kurzbeschreibung).

## Zahlen

| Einheit | Lernziele | Aufgaben |
|---|---|---|
| messen.volumen (M6 2) | quader, liter, rueckwaerts, verstehen | 28 |
| daten.darstellen (M6 3) | relative_haeufigkeit, saeulendiagramm, irrefuehrend | 21 |
| daten.kennwerte (M6 3) | mittelwert, mittel_rueckwaerts | 14 |
| funktionen.grundbegriffe (M8 1) | mengen, stelle, graph_lesen, punkt_graph, sachzusammenhang | 35 |
| geometrie.winkel (M5 2) | kreuzung, uhr, figuren, verstehen | 28 |
| **zusammen** | 18 | **126** |

- Pool: test 18 · korrektur 54 · sicherung 54.
- Stufe: 3 → 53 (alle 18 Tests, 35 Sicherungen), 2 → 73 (alle 54 Korrekturen, 19 Sicherungen).
- Antwortform: zahl 44 · auswahl 54 · luecken 28 (keine Toleranz).
- Typ: begruenden 40 · transfer 19 · fehler 19 · umkehr 18 · darstellung 14 · parameter 12 · verknuepfen 4.
- Form: ohne 66 · anwenden 19 (nur mit typ transfer) · fehler_detektiv 19 · umkehren 16 · bruecke 3 · verfahren_waehlen 2 · zwei_wege 1. Fehler-Detektive: 18 als Lücken („Zeile □, richtig □“), 1 als Auswahl mit vier Zeilen und Optionen aus Zeile + Begründung (VT3-114).

## Ideen je Lernziel (Feld `idee`, Kategorie vor dem Strich)

Fest geprüft in `bauen.py` (Abbruch bei Verstoß): je Lernziel mindestens 5 verschiedene Denkfiguren, keine mehr als zweimal. Die Kategorie beschreibt, was beim Lösen gedacht werden muss, nicht das Aufgabenformat. Die beiden Lernziele „verstehen“ (messen.volumen und geometrie.winkel) werden getrennt gezählt.

| Lernziel | Kategorien | Verteilung |
|---|---|---|
| quader | 7 | was_waere_wenn, immer_nie, transfer, fehler, rechnung_waehlen, umkehr, groessenvergleich |
| liter | 7 | bruecke, begruenden, fehler, umkehr, groessenvergleich, darstellung, transfer |
| rueckwaerts | 6 | umkehr 2, fehler, rechnung_waehlen, groessenvergleich, was_waere_wenn, transfer |
| verstehen (Volumen) | 5 | was_waere_wenn 2, transfer 2, begruenden, fehler, groessenvergleich |
| relative_haeufigkeit | 6 | umkehr 2, darstellung, fehler, groessenvergleich, immer_nie, was_waere_wenn |
| saeulendiagramm | 7 | was_waere_wenn, fehler, umkehr, begruenden, darstellung, groessenvergleich, transfer |
| irrefuehrend | 6 | darstellung 2, pruefen, begruenden, fehler, was_waere_wenn, zwei_wege |
| mittelwert | 7 | was_waere_wenn, immer_nie, fehler, zusammenhang, begruenden, transfer, groessenvergleich |
| mittel_rueckwaerts | 6 | transfer 2, umkehr, was_waere_wenn, fehler, begruenden, zwei_wege |
| mengen | 6 | mengen_deuten 2, begruenden, immer_nie, umkehr, fehler, gegenbeispiel |
| stelle | 6 | umkehr 2, zusammenhang, fehler, rechnung_waehlen, begruenden, transfer |
| graph_lesen | 5 | darstellung 2, begruenden 2, fehler, gegenbeispiel, transfer |
| punkt_graph | 7 | umkehr, begruenden, fehler, pruefen, bruecke, immer_nie, transfer |
| sachzusammenhang | 5 | darstellung 2, was_waere_wenn 2, fehler, pruefen, groessenvergleich |
| kreuzung | 6 | transfer 2, begruenden, fehler, umkehr, immer_nie, darstellung |
| uhr | 7 | umkehr, zusammenhang, fehler, pruefen, immer_nie, groessenvergleich, transfer |
| figuren | 5 | fehler 2, umkehr 2, groessenvergleich, immer_nie, transfer |
| verstehen (Winkel) | 6 | begruenden 2, immer_nie, was_waere_wenn, fehler, transfer, umkehr |

## Lehrplan-Bezug (LehrplanPLUS Gymnasium Bayern, G9)

Feld `lehrplan` = nur der Lernbereich der Einheit (M5 2, M6 2, M6 3, M8 1), wie er im Repo steht. Unterpunkte (z. B. 2.1) habe ich nicht angegeben, weil ich sie nicht sicher aus dem Repo belegen konnte. Inhaltlich nur Stoff der jeweiligen Klasse: bei Winkel keine Winkelsumme im Dreieck (Klasse 7), bei Funktionen nur lineare Terme, f(x) = x² in Wertetabellen und einfache Bruchterme mit ausgeschlossener Zahl (wie im Bestand), bei Daten nur Mittelwert, relative Häufigkeit, Säulendiagramm.

## Bilder im Test

Es gibt kein Bild und kein `grafik`-Feld. Diagramme sind durch Maßstab und Säulenhöhen in cm, Wertetabellen oder Zahlenangaben beschrieben („Hochachse beginnt bei …, 1 cm steht für …“), Graphen durch Punkte, Wertetabellen oder Steigung und Achsenabschnitt, Winkel an der Kreuzung durch die Reihenfolge α, β, γ, δ um den Schnittpunkt, Uhren durch Uhrzeiten.

## Prüfungen

- `python3 -I tools/vtest_pruefen.py --runde 3` → OK – keine Fehler, 4 HINWEISE, alle falsch-positiv: VT3-010 („50 · 30 · 40 = 60000cm³“ wird wegen der Einheit nicht als richtig gelesen; 60 000 stimmt), VT3-073 (Zeile 1 „3x + 6 = 15“ ist eine anzusetzende Gleichung, keine Rechenkette), VT3-063 („Runden“ im Sinn von Laufrunden) und VT3-115 („runde Torte“); beide meinen kein Runden von Zahlen, alle Ergebnisse sind exakt.
- `python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py` → 126 Aufgaben, 0 Abweichungen. Die Gegenrechnung ist nach der Überarbeitung neu geschrieben: je Aufgabe ein eigener Sollwert (Formel, Aufzählung, Brute-Force), bei Auswahl über den Text der richtigen Option statt über die Nummer, dazu alle Fehlbild-Rechnungen und Lösungsrechnungen mit eigenem Ausdrucksrechner.
- `python3 -I inhalte/mathe-profi/vtest-3/bauen.py` bricht ab, wenn eine der festen Prüfungen verletzt ist: je Lernziel mindestens 5 Denkfiguren und keine mehr als zweimal; Auswahl mit genau vier Optionen; richtige Option höchstens in 35 % der Fälle die längste; Positionen der richtigen Option gleichmäßig verteilt und in keinem Lernziel zweimal hintereinander gleich.
- Auswahl-Statistik (54 Aufgaben): richtige Option an Platz 1 bis 4 je 14 · 14 · 13 · 13 mal; in 14 Fällen (26 %) die längste (einschließlich Gleichstand bei sehr kurzen Zahlenoptionen), Rang nach Länge 1 bis 4: 14 · 20 · 15 · 5. Die App mischt die Optionen nicht; `kern.py` legt die Reihenfolge fest (Platz = (3 · Zähler + 1) mod 4 über alle Auswahl-Aufgaben).
- `sonderfaelle.md`: Durchsicht aller 54 Auswahl-Aufgaben.
- Nähe zum Bestand: die Prüfung des Werkzeugs (gleicher Text, ≥ 3 gleiche Zahlen, Wortüberlappung) ist ohne Fehler. Die Aufgaben, die in der Vorprüfung als Bestandsnähe benannt waren (037, 050, 055, 065, 071, 079, 089, 093, 100, 110, 113, 115, 116, 123), sind ersetzt oder umgebaut, siehe `korrektur-nach-vorpruefung.md`.

## Überarbeitung nach der Vorprüfung

Ausführlich, Befund für Befund, in `korrektur-nach-vorpruefung.md` (Quelle: `vorpruefung.md`). Kurz: Die Aufgaben mit Rechnen nach Schema, mit wiederholter Denkfigur oder mit Bestandsnähe sind ersetzt oder umgebaut, die Fehlbilder von VT3-075, 114, 048, 044, 119 und 121 sind geschärft, die Auswahl-Aufgaben haben gleich lange Optionen und eine gleichmäßig verteilte Position, die gleichen Sollantworten innerhalb eines Lernziels (008/011, 058/059, 071/072, 102/104, 115/119, 123/126) sind verschwunden.

## Zweifelsfälle (ehrlich)

1. Hilfsausdrücke statt natürlichem Rechenweg in `loesung_rechnung`, weil der Rechner keine Wurzeln und keine Zählweisen kennt: VT3-006 („216 : 36“), VT3-011 („4 · 10“, dritte Wurzel aus 64), VT3-070, 106, 115, 117 (Zählausdrücke wie „90 : 18 − 1“). `gegenrechnung.py` prüft diese Ergebnisse unabhängig durch Aufzählung.
2. VT3-118 (Zerlegung eines rechten Winkels, „mindestens einer höchstens 30°“) verlangt Beweisdenken und liegt oben an der Klassengrenze; falls zu schwer, durch eine andere Sicherung ersetzen. VT3-053 (zwei Gruppen, gleicher Mittelwert) ist ein Insight-Test, den Schülerinnen und Schüler auch durch Beispielzahlen lösen können.
3. VT3-044 (ungleiche Skala, „wie viel Mal so groß ist der Wert“) beschreibt die Skala in Worten; ohne Bild bleibt die Frage lösbar, aber die Aufgabe verlangt, die Marken zu lesen, nicht, ein Bild zu betrachten.
4. VT3-069, 075: Bruchterme mit Definitionslücke gehen in die Richtung der Bestandsaufgaben der Klasse 8, sind aber knapp am Lernbereichsrand.
5. Konventionen: Der Stundenzeiger dreht 0,5° je Minute (VT3-107, 109, 111, 112); die Winkelgröße hängt nicht von der Schenkellänge ab (VT3-125). VT3-027 setzt voraus, dass Päckchen gerade, ohne Drehen eingeräumt werden. VT3-115: Schnitte „durch den Mittelpunkt“, ein Schnitt erzeugt zwei Kanten.
6. Auswahl-Optionen, die selbst wahre Aussagen sind, aber die Frage verfehlen, tragen als Fehlbild die dahinterliegende Fehlvorstellung.
7. Alle 18 Tests sind Stufe 3; das ist erlaubt, aber schwerer als der Rest des Lernziels. Einzelne Sicherungen (Stufe 3) sind ähnlich schwer wie der Test; die Reihenfolge innerhalb des Lernziels ist daher nicht streng nach Schwierigkeit.
8. Die Fehlbild-Beschreibungen nennen teils Zwischenergebnisse; die gespeicherte Zahl ist das Endergebnis.
9. Die Aufgaben sind nur gegen den Bestand geprüft, soweit das Werkzeug und meine Durchsicht reichen. Ein Mensch sollte vor dem Einspielen die Schwierigkeit der Stufe-3-Tests in Klasse 5 und 6 gegenlesen (besonders VT3-001, 022, 057, 106, 112).
