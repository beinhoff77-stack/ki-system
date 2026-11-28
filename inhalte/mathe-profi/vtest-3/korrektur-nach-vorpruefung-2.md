# Korrektur nach Vorprüfung 2 (VT3)

Quelle: `vorpruefung-2.md` (Stand `vorpruefer-vt3` 0ef6e127, 0 A, 13 B, 17 C). Jeder Befund steht mit dem, was geändert wurde. Alle Änderungen liegen in `inhalte/mathe-profi/vtest-3/`. Nummern der Aufgaben beziehen sich auf den neuen Stand.

Nach der Überarbeitung: `vtest_pruefen.py --runde 3` ohne Fehler (2 Hinweise, beide falsch-positiv), `bauen.py` OK, `gegenrechnung.py` 126 Aufgaben, 0 Abweichungen.

## B-Befunde

| Nr. | Befund | geschlossen wie |
|---|---|---|
| B-1 | VT3-100 Bestandsdoppelung („50° und 70° nebeneinander, dritter Winkel“) | Ersetzt durch „Drei verschiedene Geraden gehen durch denselben Punkt S, einer der sechs Winkel ist 100°: wie viele der sechs Winkel sind spitz?“ (Antwort 4, der Wert 100° wird für alle sechs Winkel über Scheitel- und Nebenwinkel zu Ende gedacht). Im Bestandsvergleich kein Treffer näher als „mittel“. |
| B-2 | VT3-123 Bestandsdoppelung (65°, Nebenwinkel zu 90°) | Ersetzt durch einen Fehler-Detektiv mit überstumpfem Winkel 250°: Mia ergänzt mit 180° statt 360° (Zeile 2), gesucht ist der Winkel, der zum Vollwinkel ergänzt (110°). Andere Zahl, andere Fehlvorstellung (falscher Vollwinkel statt gestreckter Winkel). Gegen den Bestand geprüft: nächste Aufgabe nur „mittel“. |
| B-3 | VT3-047 Bestandsdoppelung (Bild-Diagramm, Fläche) | Zweimal ersetzt. Der erste Ersatz folgte dem Vorschlag der Vorprüfung (Würfel mit verdoppelter Kante, Antwort 8). Beim Handvergleich fand ich, dass auch das eine Bestandsaufgabe ist (`daten.darstellen.json` #232: „Würfel mit doppelter Kantenlänge … Wie viel Mal so groß ist das Volumen“). Deshalb jetzt ein neuer Gedanke: Eine Zeitung zeigt nur die letzten drei Monate (60 → 66 Stück), im ganzen Jahr 40 → 66; Unterschied der Anstiege in Prozentpunkten (65 % − 10 % = 55). Im Bestand kein Treffer („Ausschnitt“ kommt dort nur als Zeitachse #239 vor, anderer Gedanke). |
| B-4 | VT3-044 ohne Einsicht lösbar | Umgebaut wie vorgeschlagen: Marken 0, 10, 20, 40, 80, 160 in gleichen Abständen; die erste Säule reicht bis zur vierten Marke über der 0, die zweite bis zur zweiten Marke. Die Werte 80 und 20 stehen nicht mehr im Text, man muss die Marken zählen (Antwort 4, die Säulenhöhen verhalten sich 2 : 1). |
| B-5 | VT3-053 Antwort steht im Text (Mittelwert 8) | Neue Zahlen: Gruppe A 10 Personen Mittelwert 8, Gruppe B 20 Personen Mittelwert 11. Gefragt ist eine Aussage über den Mittelwert aller 30; richtig ist „näher bei 11 als bei 8“, die Zahl 10 steht nicht im Text und ist auch keine Option. Die falschen Optionen sind Mitte (9,5), „über 11“ und „lässt sich nicht bestimmen“. |
| B-6 | VT3-022, 023, 025 dieselbe Denkfigur; Test 022 leichter als 027, 028 | 022 ist jetzt der Packungsgedanke als Test (Päckchen mit 15 cm Kante im Karton 50 · 40 · 30 cm: 3 · 2 · 2 = 12, die Volumendivision 60 000 : 3 375 führt zu 17,8 und damit falsch). 025 ist jetzt „Gleiche Höhe, Volumenunterschied zweier Quader (Grundflächen 12 und 18 cm², Unterschied 30 cm³): Höhe 5 cm“ (Umkehr). Dabei fiel mir bei der Bestandssuche auf, dass die erste Fassung von 025 (Stein, Wasserstand) im Bestand #137/#140 steht; auch deshalb ist sie weg. 023 bleibt (Schicht), 024 Einheitenfehler, 026 Faktorvergleich, 027 Größenordnung (Klassenzimmer), 028 Prozentfaktor. Sieben Denkfiguren. |
| B-7 | graph_lesen: vier von sieben „m und t bestimmen“, Test 078 zu leicht | Test 078 ist jetzt „Welche zusätzliche Angabe reicht NICHT aus, um die Gerade durch P(2 \| 5) festzulegen?“ (Q(2 \| 9) liegt senkrecht über P, keine Funktion) als Verstehensaufgabe. 079 verlangt f(0) aus einer Wertetabelle ohne x = 0 (Steigung nötig), 080 ist Fehler-Detektiv (Achsenabschnitt), 081 parallel, 082 nicht linear, 083 Auswahl über die Achsenschnittpunkte (Verwechslung von x- und y-Achse), 084 Vorzeichen der Steigung. Nur 079 bleibt schema-nah. Sechs Denkfiguren. |
| B-8 | VT3-122 Antwort steht im Text | Wie vorgeschlagen: „α wird verdreifacht, dadurch wird sein Nebenwinkel um 40° kleiner. Wie groß war α?“ Antwort 20 (2α = 40), 40 steht im Text und ist ein Fehlbild („Nebenwinkel-Änderung als α angegeben“). |
| B-9 | feste Platzfolge `1 0 3 2 …` | `kern.plaetze` ersetzt die Rechenformel: festes Seed 20261128, zufällige, aber ausgeglichene Verteilung (je Platz 16 von 64), nie zweimal hintereinander gleich (global und je Lernziel), keine drei aufeinanderfolgenden Aufgaben mit gleichem Schritt modulo 4. Optionen und Fehlbilder werden gemeinsam umsortiert, damit die Zuordnung stimmt. `bauen.py` prüft fest: Plätze gleichmäßig, nie zweimal hintereinander gleich, keine Zahlenfolge über fünf Aufgaben. |
| B-10 | figuren: nur 4 echte Denkfiguren, „Strahlen statt Stücke“ doppelt | 117 ersetzt durch „Zwei Nebenwinkel werden halbiert, wie groß ist der Winkel zwischen den Halbierungsstrahlen?“ (immer 90°, Begründung); 113 (Test) ist jetzt ein Fehler-Detektiv mit vier Teilen im Verhältnis 1 : 2 : 2 : 1 (ein Teil in der Gleichung vergessen), nicht mehr „x, x + 10, x + 20“, weil das dem Bestand (rollend-12/R5-V130) zu nah war. Sechs Denkfiguren: fehler (113, 114), umkehr (115), groessenvergleich (116), begruenden (117), immer_nie (118), transfer (119). |
| B-11 | sachzusammenhang: „Anfangswert plus Änderung“ in fünf Aufgaben | 092 Term mit sinnvollem Bereich, 093 nicht proportional (Taxi 8 km gegen 4 km), 094 Fehler-Detektiv, 095 Streichholzmuster (3n + 1), 096 Einheitenwechsel (s(t) = 90t, t in Minuten: s(t) = 1,5t), 097 „Welcher Zusammenhang ist linear?“ (Gegenbeispiele), 098 Tarifvergleich. Sieben Denkfiguren, die Kategorien stimmen mit dem Gedanken überein. |
| B-12 | quader: vier von sieben „Kantenfaktoren“ | Nur noch 001 (Test, Faktor-Falle). 002: „Würfel aus 5 · 5 · 5 Einheitswürfeln: wie viele liegen innen?“ (27); 003: Quader mit angeklebtem Würfel (87 cm³); 006: kleinster Würfel aus Quadern 1 · 2 · 4 (8 Stück); 004 Fehler-Detektiv, 005 Rechnung wählen mit Einheiten, 007 Vergleich Würfel gegen Quader. Sechs Denkfiguren. |
| B-13 | mittel_rueckwaerts: fünf von sieben Summe-Rest | 062 ersetzt durch „Eine Zahl um 18 größer, eine andere um 6 kleiner, wie ändert sich der Mittelwert?“ (Summenänderung, 22); 061 fragt jetzt nach Summe der Abweichungen und Mittelwert (5 und 101); 063 ist eine Aussage über den Mittelwert nach Streichen der größten Zahl (höchstens 12). Summe-Rest bleibt nur 057 (Test) und 059 (Fehler-Detektiv, Fehlvorstellung). Sieben Denkfiguren, schema-nah sind 057 und 061. |

### Zusätzlich verlangt: Denkfiguren je Lernziel

Mindestens fünf verschiedene, keine mehr als zweimal: jetzt 6 bis 7 Kategorien je Lernziel (Tabelle in `README.md`), von `bauen.py` fest geprüft.

### Zusätzlich verlangt: Tests anspruchsvoller

- 022 jetzt Packungsgedanke (siehe B-6), schwerer als 027 und 028.
- 078 jetzt Verstehensaussage statt Ablesen (B-7).
- 036: „Zwei Säulen unterscheiden sich um 2 cm, im neuen Maßstab um 5 cm, die kleinere ist dort 10 cm hoch: wie hoch war sie früher?“ (4). Drei Größen, Maßstabsfaktor 2,5 muss erkannt werden.
- 043: Museum, Hochachse ab 4 700, 1 cm für 100 Besucher, Säulen 1 cm und 3,4 cm; um wie viel Prozent wirklich mehr (5). Maßstab, Achsenbeginn und Prozent in einer Aufgabe.
- 106: Uhr geht jede Stunde 5 Minuten vor, nach 3 Stunden richtige Zeit 15:00 Uhr: Zeiger 3:15 Uhr (7,5°, Antwort mit Komma). Die frühere 106 (Spiegelgedanke 12 − 7) ist als 112 (Sicherung, „150° zu welcher anderen vollen Stunde“, 5) umgestellt. Test 106 ist jetzt schwerer als 112 und der Stundenzeigergedanke ist nötig; Vorbehalt: 106 bleibt trotzdem nur „mittel“, weil die Rechnung lang, aber gerade ist.

### Zusätzlich verlangt: Bauweise der Auswahl-Aufgaben (feste Prüfungen in `bauen.py`)

- **Alle Optionen gleich gebaut.** Vorher war in 8 von 10 Fällen die einzige Option ohne „denn/weil“ die richtige. Jetzt hat in jeder Aufgabe jede Option „denn/weil“ oder keine (Prüfung `Optionen ungleich gebaut`). Betroffen waren u. a. 005, 009, 012, 018, 026, 039, 045, 048, 049, 056, 081, 095, 099, 110, 121; die Texte sind einheitlich neu geschrieben.
- **Sammel-Optionen** („Beide …“, „Kein …“, „Keine“, „Alle …“): 4 von 64 richtigen, 7 von 192 falschen Optionen (6 % gegen 4 %); Prüfung: Unterschied höchstens zehn Prozentpunkte.
- **Absolutwörter** („immer“, „nie“, „alle“, „stets“): 4 von 64 richtigen, 11 von 192 falschen (6 % gegen 6 %); gleiche Prüfung.
- **„=“**: vorher 33 % der richtigen gegen 18 % der falschen; jetzt 11 von 64 (17 %) gegen 35 von 192 (18 %). Dafür wurden in elf richtigen Optionen Rechnungen mit „ergibt“ statt „=“ geschrieben (007, 009, 011, 012, 018, 033, 041, 086, 096, 114, 116). Gleiche Prüfung.
- **Richtige Option nicht auffällig lang:** 18 von 64 (28 %) sind die längste; die Grenze in `bauen.py` bleibt 35 %. Rang nach Länge 1 bis 4: 18 · 25 · 12 · 9.
- **Zufällige Zahlengleichheit** (neu, gefunden bei der Durchsicht): VT3-005 hatte mit „2 · 30 · 5“ zufällig dasselbe Ergebnis 300 wie die richtige Rechnung 20 · 3 · 5. Jetzt 2 m, 30 cm, 50 cm: die falsche Rechnung ergibt 3 000.

### Zusätzlich verlangt: Schema

49 von 126 (Zählung der Vorprüfung) → 20 von 126 nach eigener Zählung, höchstens zwei je Lernziel (Tabelle in `README.md`). Neu gebaut oder ersetzt, um unter zwei zu bleiben: 062, 025, 047 (siehe oben); die Fehler-Detektive zählen als nicht schema-nah, wenn der Fehler eine Fehlvorstellung zeigt (004 Addition statt Multiplikation, 010 falsche Einheit, 016 falsche Umkehroperation, 024 Einheit, 031 Kehrwert, 037 Maßstab vergessen, 046 Prozentpunkte, 059, 067, 073, 080, 087, 094, 101, 108, 113, 123). Nur 052 ist ein bloßer Rechenfehler und zählt als Schema.

## C-Hinweise

| Nr. | geschlossen wie |
|---|---|
| C-1 | VT3-034: Die richtige Option ist jetzt „Sie ist ein Vielfaches von 1/120, denn jede Sechs erhöht die Trefferzahl um genau 1“ (konkrete Aussage mit Begründung), die falschen sind scharfe Behauptungen wie „genau 1/6“. |
| C-2 | VT3-065: `idee` auf „welcher Wert kommt bei x² − 9 vor (−9) und welcher nicht (−10)“ umgestellt. |
| C-3 | VT3-074: Zahlen geändert (anfangs 8 Liter, 2 Liter je Minute, 30 Liter, t = 11), keine Übereinstimmung mehr mit der Bestandskerze/Pflanze. |
| C-4 | VT3-004 jetzt 8 cm · 3 cm · 5 cm (Volumen 120 cm³) statt 6 · 4 · 3; 003 ist neu (siehe B-12) und benutzt den 6-cm-Würfel nicht mehr. |
| C-5 | VT3-104: 25° statt 35° (Antwort 65, kein Zusammenfall mehr mit 119); VT3-121: 64° statt 62° (116°). |
| C-6 | 106 und 112 neu geordnet (siehe oben); der Text von 106 sagt „als Dezimalzahl mit Komma“; 112 ist ganzzahlig (5). |
| C-7 | 036 und 043 anspruchsvoller (siehe oben). |
| C-8 | VT3-110: bleibt. Die Aussage ist allgemein („Vielfaches von 30° und höchstens 180°“) und prüft drei Gegenbeispiele; Nähe zum Bestand „Nenne eine volle Stunde …“ im Bestandsvergleich als „mittel“ eingetragen. |
| C-9 | VT3-086 und 087 bleiben, beide „Punktprobe“, aber verschiedene Formen (Begründung/Fehler-Detektiv, 3² = 6 als Fehlvorstellung). 086 ist in `idee` als begruenden geführt. |
| C-10 | saeulendiagramm: bleibt. Fünf der sieben Aufgaben arbeiten mit dem Maßstab (beim Lernziel kaum vermeidbar); die Denkfiguren sind verschieden (Test Maßstab zurückrechnen, Fehler-Detektiv, Maßstab wählen, Verhältnis, Vergleich zweier Diagramme, anderer Maßstab ändert alle Höhen gleich). |
| C-11 | Siehe „=“ oben: Verteilung angeglichen und fest geprüft. |
| C-12 | Jede Sollantwort kommt je Lernziel nur noch einmal vor (Skript-Prüfung über alle Zahl- und Lückenaufgaben). |
| C-13 | VT3-099: falsche Optionen umgebaut, „Nachbarwinkel sind immer verschieden groß“ statt „in keinem Fall gleich groß“; alle Optionen mit „denn“. |
| C-14 | 090, 125: bleiben als leichte Sicherungen; bei 090 ist die richtige Option nicht mehr die längste (falsche Option verlängert). |
| C-15 | Schema: siehe Zählung oben; 124, 126, 057 bleiben als schema-nah gezählt, aber höchstens zwei je Lernziel. |
| C-16 | Die unveränderten Aufgaben wurden im Bestandsvergleich (`bestandsvergleich.md`) einzeln gelesen; Änderungen dort: 108 (Stundenzeiger bei halber Stunde stand schon in rollend-3/GE3-13) ist jetzt „kleinerer Winkel um 8:00 Uhr, überstumpfen Winkel genommen“; 031, 037 sind Fehler-Detektive mit anderer Fehlvorstellung als der Bestand (037 mit neuen Zahlen). |
| C-17 | VT3-118: bleibt unverändert (Zweifel des Autors ausgeräumt). |

## Offene Zweifel

- Der Bestandsvergleich ist ein Handvergleich anhand der zwei nächsten Kandidaten je Aufgabe plus Schlagwortsuchen; die Vorprüfungen haben zweimal Doppelungen übersehen (047-Würfel, 025-Stein), ich könnte also weitere übersehen haben.
- Die Zählung „schema-nah“ ist meine eigene Einschätzung; eine unabhängige Zählung kann abweichen, vor allem bei 001, 021, 047, 102, 104.
- Ob die Fehler-Detektive „Fehlvorstellung“ oder nur Rechenfehler zeigen, ist Auslegungssache (zum Beispiel 059, 073, 113).
