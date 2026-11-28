# Korrektur nach der zweiten Vorprüfung (Runde VT1A)

Grundlage: `vorpruefung-2.md` (Commit 076cef00, eingemischt). Stand: 77 Aufgaben, `bauen.py` OK, `gegenrechnung.py` 0 Abweichungen, `tools/vtest_pruefen.py --runde 1a` ohne Fehler (10 Hinweise wie zuvor).

## B-Befunde

| Befund | Geschlossen wie |
|---|---|
| B1 VT1A-043 (Test, Stufe 3) | Neu als Zahl: „6 482 − 1 997 + 3 518 geschickt“ (Lösung 8 003; Zahlen so gewählt, dass 6 482 + 3 518 = 10 000 trägt). Fehlbilder mit Rechnung (Zeichen nicht mitgenommen, beide Zahlen abgezogen, alles addiert). |
| B2 044, 047 Bestandsnähe; 045/047/048/049 alle über 25 · 4 | 044 neu: „94 − 37 − 23 = 94 − □“ (Zahl 60). 047 neu: „8 · □ · 125 = 4 000“ (Zahl 4). 048 jetzt 5 · 34 · 20, 049 jetzt 24 · 125 · 5 gegen 12 · 125 · 10. 25 · 4 bleibt nur in 045. |
| B3 043/044 gleiche Einsicht | 043 Zeichen beim Umstellen mitnehmen (Rechenvorteil), 044 Abziehen verbinden (Summe abziehen): zwei verschiedene Ideen (`erlaubte_umformung`, `subtraktion_verbinden`). |
| B4 011/013 gleiche Zahlen | 011 neu als Zahl mit 5 cm + 4 cm (Quadratfläche 81 cm²); 013 jetzt (3 · 4)² mit richtigem „Kein Fehler“. (3 + 4)² kommt nicht mehr vor. |
| B5 Potenzen/sach 023/024, 025/026 gleiche Figur | 024 neu: Münzwurf, 5 Würfe (32 Folgen). 026 neu: zwei Netzwerke mit Start 5 und 10, nach 4 Tagen Verhältnis 2 (Form `zwei_wege`). 023 und 025 unverändert. |
| B6 klammern 029/034, 031/032 | 032 neu: kleinster Wert durch ein Klammerpaar in 20 − 4 + 6 (10). 034 neu: Wie viele von vier Termen haben den Wert 14 (3). Jetzt je Lernziel mindestens 5 verschiedene Figuren (`idee`). |
| B7 Auswahl-Optionen: Muster, Länge, Lage | Siehe unten. |

### B7 im Einzelnen

- **Antwortform.** Von 77 Aufgaben sind jetzt 38 Auswahl, 39 Zahl, 0 Lücken. Im Test-Pool (11 Aufgaben) sind nur noch 001, 029, 036 Auswahl. Umgestellt auf Zahl: 002, 009, 011, 015, 032, 034, 043, 044, 050, 064, 066. Neu als Zahl: 024, 026, 047.
- **Ausschlussmuster.** „Keiner“ ist als Option entfernt (053, 018). Richtig sind jetzt „Kein Fehler“ in 013, 048, 077 (3 von 9 Optionen mit diesem Anfang), „Nur Anna“ in 018, „Beide“ in vier von zehn Optionen. „Nur ①/Ben/Anna“ wurde in 036 und 053 umformuliert („Genau ②“, „Ben allein hat recht“), damit das Wort „Nur“ nicht allein ein Hinweis ist.
- **Länge.** Optionen angeglichen und Zusatzsätze verteilt: richtige Option strikt die längste in 5 von 38 Aufgaben (13 %), strikt die kürzeste in 2 (Grenze je 35 %).
- **Lage.** Richtige Position bei 4 Optionen: 0: 9, 1: 10, 2: 9, 3: 9 (029 mit 5 Optionen: Position 3).
- **Dauerhafte Prüfung.** `bauen.py` bricht ab, wenn die richtige Option in mehr als 35 % der Auswahlaufgaben die längste oder die kürzeste ist, wenn die Lage mehr als 2 auseinanderliegt, oder wenn ein Anfangswort („Kein Fehler“, „Nur“, „Keiner“, „Beide“) in weniger als 20 % seiner Vorkommen richtig ist. Es gibt aus: Statistik, Längen, Lagen, Anfangswörter (`VT_TAB=1` zeigt die Längen je Aufgabe). Die Fehler-Prüfung erlaubt jetzt „Kein Fehler:“ als richtige Option.

## C-Befunde

| Befund | Umgang |
|---|---|
| C1 016 verneint | Umgesetzt: „Eine der vier Schreibweisen hat einen anderen Wert als 56 000 000. Welche?“ |
| C2 017 Fehlbild | Umgesetzt: „Die Ziffern der Zahl (6) statt der Nullen gezählt (5 + 1)“. |
| C3 004 Bestand-Niveau | Bewusst gelassen: Stufe 2, Exponent suchen; Verstehen tragen die anderen Aufgaben des Lernziels. |
| C4 001 Zusatz | Umgesetzt: der Zusatz „5⁵ wäre 3 125“ gestrichen, Optionslängen angeglichen. |
| C5 036 Ablenker | Umgesetzt: Ablenker „Genau ②: Nur ② hat eine Klammer, die beide Halte zusammenfasst“ statt „Klammer darf nicht vorkommen“. Ablenker 2 („4 addieren“) bleibt (Plus-Minus-Verwechslung, kommt bei Kindern vor). |
| C6 072/076 Schablone | Nicht geändert: das Lernziel hat sonst genug verschiedene Ideen, und eine Ersetzung ohne Rückfrage zur Kennung 072 würde Fehlbilder und Gegenrechnung neu aufrollen; offen für die nächste Runde. |
| C7 068/069/064 absurde Ablenker | Teilweise: 064 ist jetzt eine Zahl-Aufgabe (keine Ablenker); bei 068 und 069 wurden die Optionen verlängert und sachlicher gefasst („Es passt, denn 23 · 48 ist genau 1 000, das hat Mia vorher ausgerechnet“ bleibt als inhaltlich falscher Ablenker, „Überschläge sind nutzlos“ bleibt in 069). Vorschlag: bei Bedarf austauschen. |
| C8 Regel `ueberschlag` | Bewusst offen: kein Katalogeintrag trägt das Überschlagen; die sieben Hinweise bleiben. Begründung in `regeln-zuordnung.md`. |
| C9 032 | Der Hinweis „lassen“ war für die alte 032; die Aufgabe ist jetzt neu (siehe B6). |
