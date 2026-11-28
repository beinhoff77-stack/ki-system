# Runde vtest-3 (VT3) – Verstehen in Tests, Stufe 1

126 neue Aufgaben (VT3-001 … VT3-126), nichts eingespielt. 18 Verstehens-Lernziele laut `inhalte/mathe-profi/vtest-1/auswahl.json`, keine Abweichung (siehe `auswahl.md`). Je Lernziel: 1 `test` (`ersetzt_test`), 3 `korrektur`, 3 `sicherung`.

Dateien: `auswahl.md`, fünf Aufgabendateien `<einheit>.json`, Bauskript `bauen.py` mit `kern.py`, `ideen.py` und `e_*.py` (Quelltexte), `gegenrechnung.py`, `sonderfaelle.md`, `bestandsvergleich.md`, `korrektur-nach-vorpruefung.md` und `korrektur-nach-vorpruefung-2.md` (Überarbeitungen), `vorpruefung*.md` (Berichte der Vorprüfer, nur zum Nachlesen). Jede Aufgabe trägt ein Zusatzfeld `idee` (Denkfigur: Kategorie | Kurzbeschreibung).

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
- Stufe: 3 → 54 (alle 18 Tests, 36 Sicherungen), 2 → 72.
- Antwortform: zahl 36 · auswahl 64 · luecken 26 (keine Toleranz).
- Typ: begruenden 47 · fehler 19 · transfer 18 · darstellung 14 · umkehr 12 · parameter 11 · verknuepfen 4 · rueckwaerts 1.
- Form: ohne 74 · fehler_detektiv 19 · anwenden 17 · umkehren 10 · bruecke 3 · verfahren_waehlen 2 · zwei_wege 1. Fehler-Detektive: 18 als Lücken („Zeile □, richtig □“), 1 als Auswahl mit vier Zeilen und Optionen aus Zeile + Begründung (VT3-114).

## Ideen je Lernziel (Feld `idee`, Kategorie vor dem Strich)

Fest geprüft in `bauen.py` (Abbruch bei Verstoß): je Lernziel mindestens 5 verschiedene Denkfiguren, keine mehr als zweimal. Die Kategorie beschreibt, was beim Lösen gedacht werden muss, nicht das Aufgabenformat. Die beiden Lernziele „verstehen“ werden getrennt gezählt. Nach Vorprüfung 2 hat jedes Lernziel 6 oder 7 Kategorien.

| Lernziel | Kategorien | Verteilung |
|---|---|---|
| quader | 6 | transfer 2, fehler, groessenvergleich, rechnung_waehlen, was_waere_wenn, zusammenhang |
| liter | 7 | begruenden, bruecke, darstellung, fehler, groessenvergleich, pruefen, transfer |
| rueckwaerts | 7 | fehler, gegenbeispiel, groessenvergleich, rechnung_waehlen, transfer, umkehr, was_waere_wenn |
| verstehen (Volumen) | 7 | begruenden, fehler, groessenvergleich, pruefen, transfer, umkehr, was_waere_wenn |
| relative_haeufigkeit | 7 | darstellung, fehler, groessenvergleich, immer_nie, pruefen, umkehr, was_waere_wenn |
| saeulendiagramm | 7 | begruenden, darstellung, fehler, groessenvergleich, rechnung_waehlen, was_waere_wenn, zusammenhang |
| irrefuehrend | 6 | darstellung 2, begruenden, fehler, groessenvergleich, pruefen, zwei_wege |
| mittelwert | 6 | zusammenhang 2, begruenden, fehler, groessenvergleich, immer_nie, was_waere_wenn |
| mittel_rueckwaerts | 7 | begruenden, darstellung, fehler, gegenbeispiel, umkehr, was_waere_wenn, zusammenhang |
| mengen | 6 | mengen_deuten 2, begruenden, fehler, gegenbeispiel, immer_nie, umkehr |
| stelle | 6 | umkehr 2, begruenden, fehler, rechnung_waehlen, transfer, zusammenhang |
| graph_lesen | 6 | begruenden 2, darstellung, fehler, gegenbeispiel, pruefen, zusammenhang |
| punkt_graph | 7 | begruenden, bruecke, darstellung, fehler, immer_nie, pruefen, umkehr |
| sachzusammenhang | 7 | darstellung, fehler, gegenbeispiel, groessenvergleich, pruefen, transfer, was_waere_wenn |
| kreuzung | 7 | begruenden, darstellung, fehler, immer_nie, transfer, umkehr, zusammenhang |
| uhr | 7 | fehler, groessenvergleich, immer_nie, pruefen, transfer, umkehr, zusammenhang |
| figuren | 6 | fehler 2, begruenden, groessenvergleich, immer_nie, transfer, umkehr |
| verstehen (Winkel) | 6 | begruenden 2, fehler, immer_nie, transfer, umkehr, was_waere_wenn |

## Rechnen nach Schema (Vorprüfung 2: 49 von 126 gezählt)

Ziel: höchstens zwei schema-nahe Aufgaben je Lernziel. Eine Aufgabe zählt als schema-nah, wenn sie ohne Einsicht nach einem eingeübten Rechenablauf lösbar ist (Zahl- und Lückenaufgaben ohne Fallstrick). Ein Fehler-Detektiv zählt nur dann als nicht schema-nah, wenn der Fehler eine typische Fehlvorstellung zeigt (falsche Regel, falsche Einheit, falsche Deutung); ein bloßer Rechenfehler zählt als Schema (nur VT3-052). Stand nach Überarbeitung (eigene Zählung, 20 von 126):

| Lernziel | schema-nah | Aufgaben |
|---|---|---|
| quader | 1 | 001 (Kantenfaktoren, mit der Falle „Prozente addieren“) |
| liter | 1 | 014 |
| rueckwaerts | 1 | 021 |
| verstehen (Volumen) | 0 | |
| relative_haeufigkeit | 1 | 035 |
| saeulendiagramm | 0 | |
| irrefuehrend | 1 | 047 |
| mittelwert | 1 | 052 (Rechenfehler im Fehler-Detektiv) |
| mittel_rueckwaerts | 2 | 057, 061 |
| mengen | 1 | 069 |
| stelle | 2 | 075, 077 |
| graph_lesen | 1 | 079 |
| punkt_graph | 2 | 085, 089 |
| sachzusammenhang | 1 | 098 |
| kreuzung | 2 | 102, 104 |
| uhr | 0 | |
| figuren | 1 | 119 |
| verstehen (Winkel) | 2 | 124, 126 |

## Lehrplan-Bezug (LehrplanPLUS Gymnasium Bayern, G9)

Feld `lehrplan` = nur der Lernbereich der Einheit (M5 2, M6 2, M6 3, M8 1), wie er im Repo steht. Unterpunkte (z. B. 2.1) habe ich nicht angegeben, weil ich sie nicht sicher aus dem Repo belegen konnte. Inhaltlich nur Stoff der jeweiligen Klasse: bei Winkel keine Winkelsumme im Dreieck (Klasse 7), bei Funktionen nur lineare Terme, f(x) = x² in Wertetabellen und einfache Bruchterme mit ausgeschlossener Zahl (wie im Bestand), bei Daten nur Mittelwert, relative Häufigkeit, Säulendiagramm.

## Bilder im Test

Es gibt kein Bild und kein `grafik`-Feld. Diagramme sind durch Maßstab und Säulenhöhen in cm, Wertetabellen oder Zahlenangaben beschrieben („Hochachse beginnt bei …, 1 cm steht für …“), Graphen durch Punkte, Wertetabellen oder Steigung und Achsenabschnitt, Winkel an der Kreuzung durch die Reihenfolge α, β, γ, δ um den Schnittpunkt, Uhren durch Uhrzeiten.

## Prüfungen

- `python3 -I tools/vtest_pruefen.py --runde 3` → OK – keine Fehler, 2 HINWEISE, beide falsch-positiv: VT3-073 (Zeile 1 „3x + 6 = 15“ ist eine anzusetzende Gleichung, keine Rechenkette) und VT3-115 („runde Torte“ meint kein Runden von Zahlen). Der frühere Hinweis zu VT3-010 (Einheit in „60000cm³“) und zu VT3-063 („Runden“ im Sinn von Laufrunden) tritt in der jetzigen Fassung nicht mehr auf.
- `python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py` → 126 Aufgaben, 0 Abweichungen. Je Aufgabe ein eigener Sollwert (Formel, Aufzählung, Brute-Force); bei Auswahl wird die richtige Option über ihren Text gefunden, nicht über die Nummer.
- `python3 -I inhalte/mathe-profi/vtest-3/bauen.py` bricht ab, wenn eine der festen Prüfungen verletzt ist: je Lernziel mindestens 5 Denkfiguren und keine mehr als zweimal; Auswahl mit genau vier Optionen; richtige Option höchstens in 35 % der Fälle die längste; Plätze der richtigen Option gleichmäßig verteilt und in keinem Lernziel zweimal hintereinander gleich; **neu:** in jeder Auswahl-Aufgabe tragen alle vier Optionen „denn/weil“ oder keine; der Anteil der Optionen mit „=“, mit Sammelformeln („Beide …“, „Kein …“, „Alle …“) und mit Absolutwörtern („immer“, „nie“, „alle“, „stets“) unter den richtigen und den falschen Optionen weicht höchstens um zehn Prozentpunkte ab; keine Zahlenfolge der Plätze über fünf Aufgaben.
- Auswahl-Statistik (64 Aufgaben): richtige Option an Platz 1 bis 4 je 16 mal. Die Plätze legt `kern.plaetze` fest: festes Seed (20261128), zufällige, aber ausgeglichene Folge; nie zweimal hintereinander gleich, keine drei aufeinanderfolgenden Aufgaben mit gleichem Schritt modulo 4, je Platz höchstens ⌈n/4⌉ und mindestens ⌊n/4⌋ Aufgaben. In 18 Fällen (28 %) ist die richtige Option die längste (einschließlich Gleichstand bei kurzen Zahlenoptionen), Rang nach Länge 1 bis 4: 18 · 25 · 12 · 9. „=“ steht in 11 von 64 richtigen (17 %) und 35 von 192 falschen Optionen (18 %), Sammelformeln in 4 von 64 richtigen und 7 von 192 falschen, Absolutwörter in 4 von 64 richtigen und 11 von 192 falschen.
- `sonderfaelle.md`: Durchsicht aller 64 Auswahl-Aufgaben, auch darauf, ob eine falsche Option zufällig dieselbe Zahl liefert wie die richtige (so bei VT3-005 gefunden und geändert).
- `bestandsvergleich.md`: Handvergleich aller 126 Aufgaben gegen den Bestand des Lernziels (inhalte/themen und alle rollend-*), je Lernziel mit Zahl der verglichenen Aufgaben.

## Überarbeitung nach den Vorprüfungen

- Vorprüfung 1: `korrektur-nach-vorpruefung.md` (Quelle `vorpruefung.md`).
- Vorprüfung 2: `korrektur-nach-vorpruefung-2.md` (Quelle `vorpruefung-2.md`): 13 B-Befunde und die sinnvollen C-Hinweise, Befund für Befund.

## Zweifelsfälle (ehrlich)

1. Hilfsausdrücke statt natürlichem Rechenweg in `loesung_rechnung`, weil der Rechner keine Wurzeln und keine Zählweisen kennt (z. B. VT3-006, 115). `gegenrechnung.py` prüft diese Ergebnisse unabhängig durch Aufzählung.
2. VT3-118 (Zerlegung eines rechten Winkels) verlangt Beweisdenken und liegt oben an der Klassengrenze; falls zu schwer, durch eine andere Sicherung ersetzen.
3. VT3-044 beschreibt die ungleiche Skala in Worten und über die Lage der Säulen; ohne Bild bleibt die Aufgabe lösbar, verlangt aber, die Marken zu lesen.
4. VT3-069, 075: Bruchterme mit Definitionslücke gehen in die Richtung der Bestandsaufgaben der Klasse 8, sind aber knapp am Lernbereichsrand.
5. Konventionen: Der Stundenzeiger dreht 0,5° je Minute (VT3-106, 107, 109, 111); die Winkelgröße hängt nicht von der Schenkellänge ab (VT3-125). VT3-022 setzt voraus, dass Päckchen gerade, ohne Drehen eingeräumt werden. VT3-115: Schnitte „durch den Mittelpunkt“, ein Schnitt erzeugt zwei Kanten. VT3-106 verlangt „7,5“ mit Komma, der Text sagt es.
6. Die Oberfläche eines Quaders habe ich bewusst nicht aufgegriffen, obwohl die Vorprüfung sie mehrfach als Gegenbeispiel (gleiche Oberfläche, anderes Volumen) vorschlug: Der Lernbereich der Einheit ist das Volumen, und ich konnte den Bezug der Oberfläche zu diesem Lernbereich nicht sicher aus dem Repo belegen.
7. Alle 18 Tests sind Stufe 3; einzelne Sicherungen (Stufe 3) sind ähnlich schwer, die Reihenfolge im Lernziel ist daher nicht streng nach Schwierigkeit.
8. Die Fehlbild-Beschreibungen nennen teils Zwischenergebnisse; die gespeicherte Zahl ist das Endergebnis.
9. Die Auswahl-Optionen sind vom Bauskript nur formal gleich gebaut (denn/weil, Länge, Zeichen); ob eine Option einem Kind inhaltlich „auffällt“, kann nur der Test mit Kindern zeigen.
10. Der Bestandsvergleich ist ein Handvergleich mit den zwei nächsten Kandidaten je Aufgabe plus Schlagwortsuchen; eine Gewähr für jede denkbare Nähe gibt es nicht (VT3-047 und 025 wurden bei dieser Suche noch als zu nah erkannt, obwohl die Vorprüfung sie nicht beanstandet hatte).
11. Mensch vor dem Einspielen: Schwierigkeit der Stufe-3-Tests in Klasse 5 und 6 gegenlesen (besonders VT3-001, 022, 036, 043, 057, 106).
