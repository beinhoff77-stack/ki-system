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
- Stufe: 3 → 55 (alle 18 Tests, 37 Sicherungen), 2 → 71 (alle 54 Korrekturen, 17 Sicherungen).
- Antwortform: zahl 45 · auswahl 49 · luecken 32 (keine Toleranz).
- Typ: begruenden 33 · umkehr 21 · transfer 21 · fehler 19 · darstellung 13 · parameter 12 · verknuepfen 6 · pruefung 1.
- Form: ohne 58 · anwenden 21 (nur mit typ transfer) · fehler_detektiv 19 · umkehren 18 · bruecke 5 · zwei_wege 3 · verfahren_waehlen 2. Fehler-Detektive: 18 als Lücken („Zeile □, richtig □“), 1 als Auswahl mit vier Zeilen und Optionen aus Zeile + Begründung (VT3-114).

## Ideen je Lernziel (Feld `idee`, Kategorie vor dem Strich)

Verlangt: mindestens 5 verschiedene Kategorien je Lernziel; `umkehr` zählt auch für „rückwärts“. Umkehr und Fehler kommen höchstens zweimal je Lernziel vor. Im Lernziel messen.volumen/verstehen kommen `was_waere_wenn` und `immer_nie` dreimal vor (jeweils andere Situation: Räume, Würfel, Prozentzuwachs).

| Lernziel | Kategorien | Verteilung |
|---|---|---|
| quader | 5 | was_waere_wenn 2, immer_nie, umkehr 2, fehler, groessenvergleich |
| liter | 7 | bruecke, begruenden, fehler, umkehr, zwei_wege, darstellung, transfer |
| rueckwaerts | 6 | umkehr 2, fehler, rechnung_waehlen, groessenvergleich, was_waere_wenn, transfer |
| verstehen | 7 | was_waere_wenn 3, immer_nie 3, fehler 2, transfer 2, groessenvergleich, begruenden 2, umkehr |
| relative_haeufigkeit | 5 | groessenvergleich 2, darstellung 2, fehler, umkehr, was_waere_wenn |
| saeulendiagramm | 6 | darstellung 2, fehler, umkehr, begruenden, zwei_wege, transfer |
| irrefuehrend | 5 | darstellung 2, begruenden 2, fehler, was_waere_wenn, zwei_wege |
| mittelwert | 6 | was_waere_wenn 2, immer_nie, fehler, begruenden, transfer, groessenvergleich |
| mittel_rueckwaerts | 6 | umkehr 2, was_waere_wenn, fehler, begruenden, zwei_wege, transfer |
| mengen | 6 | begruenden, immer_nie, umkehr, fehler, transfer 2, mengen_deuten |
| stelle | 6 | umkehr 2, groessenvergleich, fehler, rechnung_waehlen, begruenden, transfer |
| graph_lesen | 5 | darstellung 2, fehler, begruenden 2, gegenbeispiel, transfer |
| punkt_graph | 6 | was_waere_wenn, begruenden, fehler, pruefen, transfer 2, immer_nie |
| sachzusammenhang | 5 | darstellung 2, fehler, transfer 2, umkehr, groessenvergleich |
| kreuzung | 5 | immer_nie 2, umkehr 2, fehler, transfer, darstellung |
| uhr | 6 | umkehr, zusammenhang, fehler, begruenden, transfer 2, groessenvergleich |
| figuren | 5 | fehler 2, transfer, begruenden, umkehr 2, immer_nie |

## Lehrplan-Bezug (LehrplanPLUS Gymnasium Bayern, G9)

Feld `lehrplan` = nur der Lernbereich der Einheit (M5 2, M6 2, M6 3, M8 1), wie er im Repo steht. Unterpunkte (z. B. 2.1) habe ich nicht angegeben, weil ich sie nicht sicher aus dem Repo belegen konnte. Inhaltlich nur Stoff der jeweiligen Klasse: bei Winkel keine Winkelsumme im Dreieck (Klasse 7), bei Funktionen nur lineare Terme, f(x) = x² in Wertetabellen und einfache Bruchterme mit ausgeschlossener Zahl (wie im Bestand), bei Daten nur Mittelwert, relative Häufigkeit, Säulendiagramm.

## Bilder im Test

Es gibt kein Bild und kein `grafik`-Feld. Diagramme sind durch Maßstab und Säulenhöhen in cm, Wertetabellen oder Zahlenangaben beschrieben („Hochachse beginnt bei …, 1 cm steht für …“), Graphen durch Punkte, Wertetabellen oder Steigung und Achsenabschnitt, Winkel an der Kreuzung durch die Reihenfolge α, β, γ, δ um den Schnittpunkt, Uhren durch Uhrzeiten.

## Prüfungen

- `python3 -I tools/vtest_pruefen.py --runde 3` → OK – keine Fehler, 2 HINWEISE (beide falsch-positiv): VT3-010 („50 · 30 · 40 = 60000cm³“ wird wegen der Einheit nicht als richtig gelesen; 50 · 30 · 40 = 60 000 stimmt) und VT3-073 (Zeile 1 „3x + 6 = 15“ ist eine anzusetzende Gleichung, keine Rechenkette).
- `python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py` → 126 Aufgaben, 0 Abweichungen (eigene Formeln, Brute-Force, eigener Ausdrucksrechner für Lösungen, Lösungsrechnungen und alle Fehlbild-Rechnungen).
- `sonderfaelle.md`: Durchsicht aller 49 Auswahl-Aufgaben.
- Eigene Zusatzprüfung gegen den Bestand (Wortüberlappung ab 40 % mit Übungs-/Test-Aufgaben derselben Lernziele in `inhalte/themen` und allen `rollend-*`): nach Überarbeitung bleiben nur Aufgaben mit anderer Denkfigur nahe (VT3-071 gegen eine Bestandsaufgabe „f(x) = 9 bei f(x) = x² − 7“, VT3-015 gegen eine Quader-Rückwärts-Übung, VT3-059 gegen eine Mittelwert-Übung mit fehlender Zahl, VT3-106 und VT3-111 gegen Uhr-Übungen). Innerhalb eines Lernziels und Pools gibt es keine zwei Aufgaben mit derselben Sollantwort.

## Überarbeitung nach Hinweisen der Schwester-Runde

Dreizehn Aufgaben waren Rechnen nach Schema oder zu nah am Bestand und wurden ersetzt: VT3-003, 020, 038, 055, 058, 072, 075, 082, 100, 107, 115, 118, 122 (je neue Denkfigur, siehe `idee`). VT3-077 (Parkplatz): „minutengenau abgerechnet“ ergänzt, damit „pro Stunde“ nicht als angefangene Stunde gelesen wird.

## Zweifelsfälle (ehrlich)

1. Hilfsausdrücke statt natürlichem Rechenweg in `loesung_rechnung`, weil der Rechner keine Wurzeln kennt: VT3-006 („216 : 36“), VT3-011 („4 · 10“, dritte Wurzel aus 64), VT3-117 („90 : 6 : 3“, Summenformel), außerdem Zählaufgaben VT3-068, 070, 106, 110 (Ergebnis als Zählausdruck). `gegenrechnung.py` prüft diese Ergebnisse unabhängig durch Aufzählung.
2. VT3-110 (22 rechtwinklige Zeigerstände in 12 Stunden) braucht die Überlegung zur Überholung der Zeiger; obere Grenze von Klasse 5. VT3-118 (Zerlegung eines rechten Winkels, „mindestens einer höchstens 30°“) verlangt Beweisdenken, ebenfalls oben. Falls zu schwer, durch eine andere Sicherung ersetzen.
3. VT3-055 (gewichteter Mittelwert zweier Klassen) liegt am oberen Rand von Klasse 6.
4. VT3-069, 075: Bruchterme mit Definitionslücke (f(x) = 20 : (x − 1)) gehen in die Richtung der Bestandsaufgaben der Klasse 8, sind aber knapp am Lernbereichsrand.
5. Konventionen: Der Stundenzeiger dreht 0,5° je Minute (VT3-107, 109, 111, 112); die Winkelgröße hängt nicht von der Schenkellänge ab (VT3-125). VT3-027 setzt voraus, dass Päckchen gerade, ohne Drehen eingeräumt werden.
6. Auswahl-Optionen, die selbst wahre Aussagen sind, aber die Frage verfehlen (z. B. VT3-099, VT3-103), haben als Fehlbild die dahinterliegende Fehlvorstellung beschrieben.
7. Alle 18 Tests sind Stufe 3; das ist erlaubt, aber schwerer als der Rest des Lernziels. Einzelne Sicherungen (Stufe 3) sind ähnlich schwer wie der Test; die Reihenfolge innerhalb des Lernziels ist daher nicht streng nach Schwierigkeit.
8. `gegenrechnung.py` hat bei rein logischen Aufgaben (Aussagen über Mengen, Winkelfolgen) feste Indizes, die nach Aufzählung oder Beweis im Skript gesetzt sind, nicht gerechnet.
9. Die Fehlbild-Beschreibungen nennen teils Zwischenergebnisse (z. B. „60 000 : 3 375 ≈ 17,8, abgerundet 17“); die gespeicherte Zahl ist das Endergebnis.
