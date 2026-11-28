# Runde vtest-3 (VT3) – Verstehen in Tests, Stufe 1

126 neue Aufgaben (VT3-001 … VT3-126), nichts eingespielt. 18 Verstehens-Lernziele laut `inhalte/mathe-profi/vtest-1/auswahl.json`, keine Abweichung (siehe `auswahl.md`). Je Lernziel: 1 `test` (`ersetzt_test`), 3 `korrektur`, 3 `sicherung`.

Dateien: `auswahl.md`, fünf Aufgabendateien `<einheit>.json`, Bauskript `bauen.py` mit `kern.py`, `ideen.py` und `e_*.py` (Quelltexte), `gegenrechnung.py`, `sonderfaelle.md`, `bestandsvergleich.md`, `korrektur-nach-vorpruefung.md`, `korrektur-nach-vorpruefung-2.md` und `korrektur-nach-vorpruefung-3.md` (Überarbeitungen), `vorpruefung*.md` (Berichte der Vorprüfer, nur zum Nachlesen). Jede Aufgabe trägt ein Zusatzfeld `idee` (Denkfigur: Kategorie | Kurzbeschreibung).

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
- Stufe: 3 → 52 (alle 18 Tests, 34 Sicherungen), 2 → 74.
- Antwortform: zahl 36 · auswahl 64 · luecken 26 (keine Toleranz).
- Typ: begruenden 47 · fehler 19 · transfer 18 · darstellung 14 · umkehr 13 · parameter 10 · verknuepfen 4 · rueckwaerts 1.
- Form: ohne 73 · fehler_detektiv 19 · anwenden 17 · umkehren 10 · bruecke 3 · verfahren_waehlen 3 · zwei_wege 1. Fehler-Detektive: 18 als Lücken („Zeile □, richtig □“), 1 als Auswahl mit vier Zeilen und Optionen aus Zeile + Begründung (VT3-114).

## Ideen je Lernziel (Feld `idee`, Kategorie vor dem Strich)

Fest geprüft in `bauen.py` (Abbruch bei Verstoß): je Lernziel mindestens 5 verschiedene Denkfiguren, keine mehr als zweimal. Die Kategorie beschreibt, was beim Lösen gedacht werden muss, nicht das Aufgabenformat. Die beiden Lernziele „verstehen“ werden getrennt gezählt. Nach Vorprüfung 3 hat jedes Lernziel 6 oder 7 Kategorien. Zusätzlich wurde in Vorprüfung 3 der Inhalt geprüft: Wo mehrere Aufgaben formal verschieden etikettiert, aber dieselbe Einsicht waren (saeulendiagramm: Maßstab, figuren: Zerlegung des rechten Winkels, mittelwert/mittel_rueckwaerts: Summenänderung), wurde eine Aufgabe durch eine mit anderem Gedanken ersetzt. Inhaltlich verschieden sind jetzt: saeulendiagramm 6 (Faktor beim Neuzeichnen, Umrechnen Höhe und Wert, Maßstab wählen, Verhältnis unabhängig vom Maßstab, Vergleich verschiedener Maßstäbe, gestapelte Säule), figuren 6 (Verhältnis-Zerlegung, Torte/Vollwinkel, Bruchteile verschiedener Winkel, Quadrat auf einer Geraden, mindestens ein kleiner Teilwinkel, gedrehte Quadrate), mittelwert 7 (Rückwärtsrechnen nach Verdreifachen, Nullen zählen mit, Rechenfehler Teiler, Gesamtmittel näher an der größeren Gruppe, ein Wert gleich dem Mittelwert ändert nichts, gleichmäßiger Zuwachs, Ausreißer), mittel_rueckwaerts 7 (Zahl der Mädchen aus Mittelwerten, Abstände gleichen sich aus, Läuferin, „mindestens eine Zahl“, Abweichungen von 100, Summe ändert sich plus und minus, Streichen der größten Zahl).

| Lernziel | Kategorien | Verteilung |
|---|---|---|
| quader | 6 | transfer 2, fehler, groessenvergleich, rechnung_waehlen, was_waere_wenn, zusammenhang |
| liter | 7 | begruenden, bruecke, darstellung, fehler, groessenvergleich, pruefen, transfer |
| rueckwaerts | 7 | fehler, gegenbeispiel, groessenvergleich, rechnung_waehlen, transfer, umkehr, was_waere_wenn |
| verstehen (Volumen) | 7 | begruenden, fehler, groessenvergleich, transfer, umkehr, was_waere_wenn, zusammenhang |
| relative_haeufigkeit | 7 | darstellung, fehler, groessenvergleich, immer_nie, pruefen, umkehr, zusammenhang |
| saeulendiagramm | 7 | begruenden, darstellung, fehler, groessenvergleich, mengen_deuten, rechnung_waehlen, was_waere_wenn |
| irrefuehrend | 6 | darstellung 2, begruenden, fehler, groessenvergleich, pruefen, zwei_wege |
| mittelwert | 6 | zusammenhang 2, begruenden, fehler, groessenvergleich, mengen_deuten, umkehr |
| mittel_rueckwaerts | 7 | begruenden, darstellung, fehler, gegenbeispiel, umkehr, was_waere_wenn, zusammenhang |
| mengen | 6 | mengen_deuten 2, begruenden, fehler, gegenbeispiel, immer_nie, umkehr |
| stelle | 6 | umkehr 2, begruenden, fehler, rechnung_waehlen, transfer, zusammenhang |
| graph_lesen | 6 | begruenden 2, darstellung, fehler, gegenbeispiel, pruefen, zusammenhang |
| punkt_graph | 7 | begruenden, bruecke, darstellung, fehler, immer_nie, pruefen, umkehr |
| sachzusammenhang | 6 | transfer 2, darstellung, fehler, gegenbeispiel, pruefen, was_waere_wenn |
| kreuzung | 7 | begruenden, darstellung, fehler, immer_nie, transfer, umkehr, zusammenhang |
| uhr | 7 | fehler, groessenvergleich, immer_nie, pruefen, transfer, umkehr, zusammenhang |
| figuren | 6 | fehler 2, begruenden, groessenvergleich, immer_nie, transfer, umkehr |
| verstehen (Winkel) | 6 | begruenden 2, fehler, immer_nie, transfer, umkehr, was_waere_wenn |

## Rechnen nach Schema (Vorprüfung 3: 19 von 126 gezählt, nach der Zählung des Vorprüfers)

Ziel: höchstens zwei schema-nahe Aufgaben je Lernziel. Eine Aufgabe zählt als schema-nah, wenn sie ohne Einsicht nach einem eingeübten Rechenablauf lösbar ist (Zahl- und Lückenaufgaben ohne Fallstrick). Ein Fehler-Detektiv zählt nur dann als nicht schema-nah, wenn der Fehler eine typische Fehlvorstellung zeigt (falsche Regel, falsche Einheit, falsche Deutung); ein bloßer Rechenfehler zählt als Schema (nur VT3-052). Stand nach Vorprüfung 3 (Vorprüfer zählte 21; VT3-035 ist ersetzt, VT3-073 ist jetzt ein Fehler-Detektiv mit Fehlvorstellung, VT3-092 ist die frühere 098):

| Lernziel | schema-nah | Aufgaben |
|---|---|---|
| quader | 1 | 001 (Kantenfaktoren, mit der Falle „Prozente addieren“) |
| liter | 1 | 014 |
| rueckwaerts | 1 | 021 (jetzt Stufe 2) |
| verstehen (Volumen) | 0 | |
| relative_haeufigkeit | 0 | |
| saeulendiagramm | 1 | 040 |
| irrefuehrend | 1 | 047 |
| mittelwert | 1 | 052 (Rechenfehler im Fehler-Detektiv) |
| mittel_rueckwaerts | 2 | 061 (jetzt Stufe 2), 062 |
| mengen | 1 | 069 |
| stelle | 2 | 075, 077 |
| graph_lesen | 1 | 079 |
| punkt_graph | 2 | 085, 089 |
| sachzusammenhang | 1 | 092 (Jahreskarte, jetzt der Test) |
| kreuzung | 2 | 102, 104 |
| uhr | 0 | |
| figuren | 0 | |
| verstehen (Winkel) | 2 | 124, 126 |

Grenzfälle, die je nach Strenge dazukommen (Vorprüfer): 030, 038, 059, 070, 106 und 005, 017; VT3-050 ist durch die Umkehraufgabe keiner mehr. Kein Lernziel hat mehr als zwei sichere.

## Lehrplan-Bezug (LehrplanPLUS Gymnasium Bayern, G9)

Feld `lehrplan` = nur der Lernbereich der Einheit (M5 2, M6 2, M6 3, M8 1), wie er im Repo steht. Unterpunkte (z. B. 2.1) habe ich nicht angegeben, weil ich sie nicht sicher aus dem Repo belegen konnte. Inhaltlich nur Stoff der jeweiligen Klasse: bei Winkel keine Winkelsumme im Dreieck (Klasse 7), bei Funktionen nur lineare Terme, f(x) = x² in Wertetabellen und einfache Bruchterme mit ausgeschlossener Zahl (wie im Bestand), bei Daten nur Mittelwert, relative Häufigkeit, Säulendiagramm.

## Bilder im Test

Es gibt kein Bild und kein `grafik`-Feld. Diagramme sind durch Maßstab und Säulenhöhen in cm, Wertetabellen oder Zahlenangaben beschrieben („Hochachse beginnt bei …, 1 cm steht für …“), Graphen durch Punkte, Wertetabellen oder Steigung und Achsenabschnitt, Winkel an der Kreuzung durch die Reihenfolge α, β, γ, δ um den Schnittpunkt, Uhren durch Uhrzeiten.

## Prüfungen

- `python3 -I tools/vtest_pruefen.py --runde 3` → OK – keine Fehler, keine Hinweise. Die früheren Hinweise waren falsch-positiv und sind erledigt: VT3-010 („60 000 cm³“ mit Einheit las das Werkzeug als falsche Rechenzeile; der Text steht jetzt als „Das Volumen ist 60 000 cm³, denn 50 · 30 · 40 = 60 000.“, die Rechnung selbst war immer richtig), VT3-073 (Zeile 1 war eine Gleichung, die Aufgabe ist ersetzt) und VT3-115 („runde Torte“ meint kein Runden, steht jetzt „kreisförmige Torte“).
- `python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py` → 126 Aufgaben, 0 Abweichungen. Je Aufgabe ein eigener Sollwert (Formel, Aufzählung, Brute-Force); bei Auswahl wird die richtige Option über ihren Text gefunden, nicht über die Nummer.
- `python3 -I inhalte/mathe-profi/vtest-3/bauen.py` bricht ab, wenn eine der festen Prüfungen verletzt ist: je Lernziel mindestens 5 Denkfiguren und keine mehr als zweimal; Auswahl mit genau vier Optionen; richtige Option höchstens in 35 % der Fälle die längste; Plätze der richtigen Option gleichmäßig verteilt und in keinem Lernziel zweimal hintereinander gleich; **neu:** in jeder Auswahl-Aufgabe tragen alle vier Optionen „denn/weil“ oder keine; der Anteil der Optionen mit „=“, mit Sammelformeln („Beide …“, „Kein …“, „Alle …“) und mit Absolutwörtern („immer“, „nie“, „alle“, „stets“) unter den richtigen und den falschen Optionen weicht höchstens um zehn Prozentpunkte ab; **neu (Vorprüfung 3):** Abschwächungen („höchstens“, „mindestens“, „wenigstens“) weichen unter richtigen und falschen Optionen höchstens um fünf Prozentpunkte ab, Verneinungen („nicht“, „kein…“, „nie“) höchstens um zehn; keine Zahlenfolge der Plätze über fünf Aufgaben.
- Auswahl-Statistik (64 Aufgaben): richtige Option an Platz 1 bis 4 je 16 mal. Die Plätze legt `kern.plaetze` fest: festes Seed (20261128), zufällige, aber ausgeglichene Folge; nie zweimal hintereinander gleich, keine drei aufeinanderfolgenden Aufgaben mit gleichem Schritt modulo 4, je Platz höchstens ⌈n/4⌉ und mindestens ⌊n/4⌋ Aufgaben. In 18 Fällen (28 %) ist die richtige Option die längste (einschließlich Gleichstand bei kurzen Zahlenoptionen), Rang nach Länge (1 = längste) 1 bis 4: 18 · 27 · 12 · 7; mittlere Länge 74,7 gegen 73,4 Zeichen. „denn/weil“: 78 % richtig gegen 78 % falsch. „=“ steht in 9 von 64 richtigen (14 %) und 29 von 192 falschen Optionen (15 %), Sammelformeln in 4 von 64 richtigen und 6 von 192 falschen, Absolutwörter in 3 von 64 richtigen und 8 von 192 falschen, Abschwächungen („höchstens“, „mindestens“, „wenigstens“) in 6 von 64 richtigen (9 %) und 13 von 192 falschen (7 %; vorher 5 von 64 gegen 4 von 192), Verneinungen in 7 von 64 richtigen (11 %) und 32 von 192 falschen (17 %).
- `sonderfaelle.md`: Durchsicht aller 64 Auswahl-Aufgaben, auch darauf, ob eine falsche Option zufällig dieselbe Zahl liefert wie die richtige (so bei VT3-005 gefunden und geändert).
- `bestandsvergleich.md`: Handvergleich aller 126 Aufgaben gegen den Bestand des Lernziels (inhalte/themen und alle rollend-*), je Lernziel mit Zahl der verglichenen Aufgaben.

## Überarbeitung nach den Vorprüfungen

- Vorprüfung 1: `korrektur-nach-vorpruefung.md` (Quelle `vorpruefung.md`).
- Vorprüfung 2: `korrektur-nach-vorpruefung-2.md` (Quelle `vorpruefung-2.md`): 13 B-Befunde und die sinnvollen C-Hinweise, Befund für Befund.
- Vorprüfung 3 (letzte Schleife vor der Sammelprüfung): `korrektur-nach-vorpruefung-3.md` (Quelle `vorpruefung-3.md`): 9 Doppelungen mit gleichem Kern ersetzt, Schema im Lernziel „stelle“ auf zwei gesenkt, B2 bis B11 und C1 bis C5 Befund für Befund.

## Zweifelsfälle (ehrlich)

1. Hilfsausdrücke statt natürlichem Rechenweg in `loesung_rechnung`, weil der Rechner keine Wurzeln und keine Zählweisen kennt (z. B. VT3-006, 115). `gegenrechnung.py` prüft diese Ergebnisse unabhängig durch Aufzählung.
2. VT3-118 (Zerlegung eines rechten Winkels) verlangt Beweisdenken und liegt oben an der Klassengrenze; falls zu schwer, durch eine andere Sicherung ersetzen.
3. VT3-044 beschreibt die ungleiche Skala in Worten und über die Lage der Säulen; ohne Bild bleibt die Aufgabe lösbar, verlangt aber, die Marken zu lesen.
4. VT3-069, 075: Bruchterme mit Definitionslücke gehen in die Richtung der Bestandsaufgaben der Klasse 8, sind aber knapp am Lernbereichsrand.
5. Konventionen: Der Stundenzeiger dreht 0,5° je Minute (VT3-106, 107, 109, 111); die Winkelgröße hängt nicht von der Schenkellänge ab (VT3-125). VT3-022 setzt voraus, dass Päckchen gerade, ohne Drehen eingeräumt werden. VT3-115: Schnitte „durch den Mittelpunkt“, ein Schnitt erzeugt zwei Kanten. VT3-106 hat jetzt die ganzzahlige Antwort 75° (10 Minuten je Stunde).
6. Die Oberfläche eines Quaders habe ich bewusst nicht aufgegriffen, obwohl die Vorprüfung sie mehrfach als Gegenbeispiel (gleiche Oberfläche, anderes Volumen) vorschlug: Der Lernbereich der Einheit ist das Volumen, und ich konnte den Bezug der Oberfläche zu diesem Lernbereich nicht sicher aus dem Repo belegen.
7. Alle 18 Tests sind Stufe 3; einzelne Sicherungen (Stufe 3) sind ähnlich schwer, die Reihenfolge im Lernziel ist daher nicht streng nach Schwierigkeit.
8. Die Fehlbild-Beschreibungen nennen teils Zwischenergebnisse; die gespeicherte Zahl ist das Endergebnis.
9. Die Auswahl-Optionen sind vom Bauskript nur formal gleich gebaut (denn/weil, Länge, Zeichen); ob eine Option einem Kind inhaltlich „auffällt“, kann nur der Test mit Kindern zeigen.
10. Der Bestandsvergleich ist ein Handvergleich mit den zwei nächsten Kandidaten je Aufgabe plus Schlagwortsuchen; eine Gewähr für jede denkbare Nähe gibt es nicht (VT3-047 und 025 wurden bei dieser Suche noch als zu nah erkannt, obwohl die Vorprüfung sie nicht beanstandet hatte).
11. Mensch vor dem Einspielen: Schwierigkeit der Stufe-3-Tests in Klasse 5 und 6 gegenlesen (besonders VT3-001, 022, 036, 043, 057, 106).

## Offene Zweifel für die Gegenprüfung (Stand nach Vorprüfung 3)

Ehrliche Liste dessen, was ich nicht ausräumen konnte. Der Bestand der fünf Einheiten ist für diese Lernziele sehr dicht; für jede ersetzte Aufgabe habe ich den Kern gezielt im Bestand gesucht (Suchwörter stehen in `bestandsvergleich.md`), eine Gewähr gibt es nicht.

Klassenstufe und Schwierigkeit (Sicherheit nach meiner Kenntnis des Lehrplans, ohne Lehrplantext):
- VT3-001: Prozentfaktoren bei drei Kanten, etwa 60 %, dass das in Klasse 6 machbar ist.
- VT3-036: Streckfaktor 2,5 beim Neuzeichnen, etwa 55 %.
- VT3-043: mehrstufig mit Prozent, etwa 60 %; im Bestand liegen #143/#167 („wie viel Mal so hoch wirkt die zweite Säule“) im selben Gedankenfeld, die Frage hier ist aber die wahre prozentuale Änderung.
- VT3-100: Paar-Argument bei drei Geraden (sechs Winkel, wie viele spitz).
- VT3-113: Variable x und Gleichung 6x = 90 in Klasse 5, etwa 65 %; VT3-114 ist ebenfalls eine Verhältniszerlegung des rechten Winkels (zwei von sieben Aufgaben, dazu VT3-118).
- VT3-118: Taubenschlag-Argument („mindestens ein Teilwinkel höchstens 30°“) in Klasse 5, schwer einzuschätzen.
- VT3-058 ist jetzt ohne negative Zahlen formuliert („unter“, „über“). VT3-061 und VT3-062 rechnen noch mit Vorzeichen (Abweichungen −2, +1, …), vgl. Klasse 6; VT3-061 steht deshalb auf Stufe 2.
- VT3-117 (Winkelhalbierende) ist ersetzt; VT3-106 ist ganzzahlig (75°).

Nähe zum Bestand, nach Lesen als „mittel“ eingestuft (Bestandsnummer in `bestandsvergleich.md`):
- VT3-057 (Zahl der Mädchen aus drei Mittelwerten) liegt im Gedankenfeld von #116/#119 (Gruppenmittel und Gesamtmittel), gefragt wird aber das Gewicht, nicht ein Mittelwert.
- VT3-122 (spitzer und stumpfer Winkel nebeneinander) liegt nahe bei #254; hier „immer über 90°“ mit Gegenbeispielen.
- VT3-028 (Länge verdoppelt, Breite halbiert) liegt in der Familie R14-V164/#212 bis #217, Gedanke aber ein anderer (die Änderungen heben sich auf). Von VT3-001 getrennt.
- Die übrigen unter B1 genannten (VT3-014, 029, 033, 038, 039, 040, 044, 046, 053, 054, 056, 059, 062, 064, 067, 068, 076, 085, 091, 094, 095, 097, 098, 102, 103, 108, 109, 112, 114, 126; 035, 042 und 117 sind ersetzt): beim Lesen verschiedener Gedanke, Wortlaut und Zahlen teils ähnlich. Die einfache Wortähnlichkeit zum nächsten Bestandstext liegt zwischen 0,10 und 0,56; die höchsten Werte haben VT3-067 (0,56, Bestand #86 zählt die Elemente von W für x²; hier ist es ein Fehler-Detektiv mit anderer Fehlvorstellung), VT3-112 (0,51, #158: gleiche Uhrzeitfigur, andere Frage), VT3-108 (0,46) und VT3-102 (0,41). Ich habe sie nicht ersetzt, damit die Runde nicht „ins Blaue“ umgebaut wird; sie stehen hier für die Gegenprüfung. VT3-014 (Becken füllen, R14-V156) und VT3-102 (Summe dreier Winkel, GE3-B2) sind nach Lesen die nächsten.
- VT3-001 und VT3-028 sind innerhalb der Runde entwirrt (Prozentfaktoren gegen Verdoppeln und Halbieren).

Werkzeug: Der frühere Hinweis zu VT3-010 war ein Fehlalarm des Werkzeugs (Einheit „cm³“ hinter einer Zahl mit Leerzeichen), siehe Prüfungen; die Rechnung war richtig.
