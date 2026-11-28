# Korrektur nach der Vorprüfung (Runde VT3)

Grundlage: `vorpruefung.md` (Branch `vorpruefer-vt3`, Commit 5bdace7c). Jeder Befund steht einzeln: Kennung · Befund · alt → neu, oder warum nicht geändert. Die Kennungen bleiben, die Aufgaben tragen den neuen Inhalt (Stand der JSON-Dateien). Abnahme: `vtest_pruefen.py --runde 3` ohne Fehler, `gegenrechnung.py` 0 Abweichungen, `bauen.py` mit den festen Prüfungen (Denkfiguren, Optionslänge, Position) ohne Abbruch.

## Querschnitt zuerst

- **Rechnen nach Schema (Auftrag 2).** Ersetzt oder umgebaut wurden 008, 012, 025, 026, 036, 044, 050, 062 und die weiteren aus der Liste der Vorprüfung (Einzelnachweise unten). Je Lernziel bleiben höchstens zwei Aufgaben nahe am Schema (z. B. 004 und 010 als Fehler-Detektive mit reiner Rechenfolge, 032 und 077); jeder Test verlangt eine Einsicht (Faktoren in Prozent, Symmetrie der Parabel, Marken ungleich verteilt, Nachbarwinkel im Beweis, Zeigergeschwindigkeit, Scheitelwinkel im Sechser-Büschel usw.).
- **Denkfiguren (Auftrag 3).** `idee` ist nach dem Inhalt neu beschriftet (VT3-023 jetzt `begruenden`, vorher fälschlich `immer_nie`). Je Lernziel 5 bis 7 verschiedene Denkfiguren, keine mehr als zweimal; `bauen.py` bricht sonst ab. Die Zeile „verstehen“ der README ist in „verstehen (Volumen)“ und „verstehen (Winkel)“ getrennt.
- **Auswahl (Auftrag 6).** Die App mischt nicht; `kern.py` legt Platz der richtigen Option fest: (3 · Zähler + 1) mod 4 über alle 54 Auswahl-Aufgaben, Ergebnis 14 · 14 · 13 · 13 für Platz 1 bis 4, in keinem Lernziel zweimal derselbe Platz hintereinander. Länge: vorher in 34 von 49 die längste, jetzt in 14 von 54 (26 %, davon einige Gleichstände bei reinen Zahlenoptionen); nach Länge sortiert Rang 1 bis 4: 14 · 20 · 15 · 5. Optionen haben jetzt durchgehend dieselbe Form (Aussage + Begründung) oder sind alle reine Zahl- bzw. Termoptionen. Beide Prüfungen sind in `bauen.py` fest eingebaut.
- **Gleiche Sollantwort im Lernziel (Auftrag 7).** 008/011 (3375 gegen 40), 058/059 (10 gegen Lücke 2/40), 071/072 (2 gegen 5), 102/104 ([50; 130] gegen 55), 115/119 (9 gegen [35; 55]), 123/126 ([1; 115] gegen [90; 120]) verschieden. Zusätzlich beim Durchsuchen aller Lernziele gefunden und behoben: 016 und 020 (beide Höhe 9 → 016 jetzt 11), 037 und 038 (beide 12 → 038 jetzt 15), 067/069/070 (dreimal 3 → 070 jetzt 4).

## A

| Kennung | Befund | alt → neu |
|---|---|---|
| VT3-067 | Zwei vertretbare erste Fehler: Zeile 2 „W = {0; −3; −4; −3; 0}“ ist als Menge nicht falsch. | Zeile 2 ohne Mengenschreibweise: „Er schreibt die Funktionswerte der Reihe nach auf: 0; −3; −4; −3; 0.“ Zeile 3 „Also hat W fünf Elemente“ ist die einzige falsche Aussage, Zeile 4 Folge. Antwort [3; 3], Fehlbilder (5 Elemente, 4) bleiben. |

## B

| Kennung | Befund | alt → neu |
|---|---|---|
| VT3-055 | Fast die Übung 6a/6b (20/30 Kinder, gewichteter Mittelwert). | Auch die Nuss-Mischung (gewichteter Mittelwert in anderem Kleid) wäre dieselbe Denkfigur geblieben, deshalb ganz neu: „Fünf aufeinanderfolgende gerade Zahlen haben den Mittelwert 20. Wie groß ist die größte?“ (24). Einsicht: Mittelwert gleichmäßig verteilter Zahlen ist die Mitte. Fehlbilder 20, 22, 30. |
| VT3-050 | Test = Bestandsübung „Kind kommt dazu“. | Jetzt: „Mittelwert von fünf Zahlen ist 8. Jede wird verdoppelt und dann um 3 verkleinert. Neuer Mittelwert?“ (13). Einsicht: Mittelwert folgt den Rechenschritten, keine Einzelwerte bekannt. Fehlbilder 16 (Verkleinern vergessen), 10 (3 mal fünf abgezogen) usw. |
| VT3-089 | Gleiche Punkte wie Bestand A(1\|3), B(3\|7). | Neu: S(4 \| c) liegt auf f(x) = 3x − 2 und g(x) = 2x + a, gesucht a (2). Denkfigur Brücke (gemeinsamer Punkt zweier Graphen), andere Zahlen. |
| VT3-037 | Fast `rollend-4/d1` (7 cm, Teilen statt Malnehmen). | Anderer Fehler: Säulenunterschied 4,5 − 3 = 1,5 „Kinder“ (Höhe nicht mit dem Maßstab 1 cm = 8 Kinder multipliziert), erste falsche Zeile 3, richtig 12 Kinder. Andere Zahlen, anderer Fehler. |
| VT3-100 | Dreimal Bestand „halb so groß wie Nachbarwinkel“; Fehlbild 240 keine Fehlvorstellung. | Neu: Drei Geraden durch einen Punkt, drei benachbarte Winkel bilden 180°, zwei sind 50° und 70°, gesucht der gegenüberliegende des dritten (60). Fehlbilder 130, 120, 110 sind echte Wege (nur Nebenwinkel, Summe, anderer Nebenwinkel). |
| VT3-115 | Erste Lücke = Bestand „Torte in 10 Stücke → 36°“. | Neu, Umkehr mit Falle: Schnitte durch den Mittelpunkt, Stücke von 20° (360 : 20 = 18 Stücke, 9 Schnitte). Fehlbilder 18 (Stücke = Schnitte), 17, 36. |
| VT3-113 | Bestand „drei Teile am Rechteck“; als Test zu leicht. | Neu: Mia teilt einen rechten Winkel in drei Teile, jeweils 10° größer (x, x + 10°, x + 20°). Der Fehler liegt in Zeile 3 (3x + 30° = 90° statt = 90° − 30°); x = 20°. Fehler in einer Folgerung, Gleichungsdenken, Test Stufe 3. |
| VT3-123 | Gleicher Fehler wie `rollend-4/ge3` (180° statt 90°). | Neu: Nebenwinkel zu einem spitzen Winkel mit 90° statt 180° ergänzt (α = 65°, richtig β = 115°); Zeile 1 ist der erste Fehler, Folgezeilen sind folgerichtig falsch. |
| VT3-116 | Sieben Bestandsaufgaben „Diagonale im Rechteck“. | Ersetzt: Drittel eines rechten Winkels (30°) gegen Viertel eines gestreckten (45°); größerer Bruch ist nicht der größere Winkel. |
| VT3-065 | Gleiches Muster wie Bestand x² + 1 / x² − 4 (kein Wert kleiner/größer). | Neu: f(x) = x² − 9, Aussagen über W („−9 gehört zu W, f(0) = −9“; −10 kommt nicht vor; f(3) = 0 kommt vor). Gegenbeispiel-Denken, andere Optionsform. |
| VT3-071 | Test mit der Denkfigur des Bestands (x² − 7 = 9). | Neu: f(x) = x² − 6x, f(4) = −8, zweite Stelle (2). Einsicht: Symmetrie der Parabel um 3, keine Gleichung nötig. |
| VT3-079 | Wertetabelle → Term, wie fünf Bestandsübungen; Dopplung mit 078. | Neu: Wertetabelle x = 1, 3, 5, 7 (ohne x = 0), gefragt der Wert an der Stelle 0 (7): Der Achsenabschnitt muss aus der Steigung rückwärts bestimmt werden. 078 bleibt (Term aus zwei Punkten, Auswahl). |
| VT3-093 | Wertetabelle → Term im Sachkontext. | Neu: Taxi K(x) = 3 + 2x, Fahrt über 8 km gegen 4 km: „weniger als das Doppelte, weil die Grundgebühr nur einmal anfällt“ (Auswahl). |
| VT3-110 | Verfahren wie Bestand, Randsatz wirkungslos, in Klasse 5 zu schwer. | Neu: „Welche Aussage über den kleineren Winkel zwischen den Zeigern zu den vollen Stunden stimmt?“ (Vielfaches von 30°, höchstens 180°). Zählaufgabe und Mitternachtssatz sind weg; Klasse 5 geeignet. |
| VT3-006 | Fehlbild 12: angeblich `luecke` falsch (gehört zu Lücke 2). | Im gespeicherten Stand steht `luecke` 2 bereits (Höhe), Text „statt der Höhe angegeben“ passt; Fehlbild nachgerechnet (216 : 36 · 2 = 12). Keine Änderung nötig, Befund in dieser Form nicht mehr nachvollziehbar. |
| VT3-075 | Fehlbild 80 führt zu a = 81. | Fehlbild 81 mit Rechnung „20 · 4 + 1“ („mit 4 malgenommen statt durch 4 geteilt“). |
| VT3-114 | Zwei Optionen sind Rechenfehler; richtige Option die längste. | Optionen ersetzt: Zeile 1 (große Teil nur zwei Stücke), Zeile 3 (überflüssige zweite Division), Zeile 4 (nur auf das unsinnige Ergebnis geschaut), richtige Option Zeile 2 mit Begründung. Längen angeglichen. |
| VT3-048 | „Beide Hochachsen“ unklar. | „Die Hochachse beginnt bei 0.“ |
| VT3-059 | Antwort 10 wie 058; Bestandsschablone. | Neu: Läuferin, vier Läufe im Mittel 50 s, Ziel 48 s Mittelwert nach fünf Läufen; falsche Zeile 2 („2 Sekunden schneller als der Mittelwert“), richtig 40 s. 058 bleibt (ersetzte Zahl 10). |
| VT3-105 | Zahlen 65°/115° wie 102, Argument „Sonderfall 90°“ doppelt (099/103). | 105: Winkelfolge 72°, 108°, 72°, 108°. 102: Summe dreier Winkel 310°, α = 50°, β = 130°. 104: 35° statt 25°-Rechnung (Antwort 55). 099: Beweis über Nachbarwinkel (Begründung), 103: Aussage über Scheitelwinkel und zwei Sonderfälle. |
| VT3-003, VT3-005 | 001/002/003/005 dieselbe Denkfigur „Kantenfaktoren“. | 001: Prozentänderungen (Faktoren statt Prozentzahlen), 002: Würfel, alle Kanten halbiert (Auswahl), 003: Würfel in kleine Würfel zerlegen (27 Stück), 005: gemischte Einheiten, Rechnung in dm³ auswählen. Vier verschiedene Denkfiguren statt einer. |
| VT3-033 | Wie 029 (Anteile vergleichen). | 029 ist jetzt eine Umkehr (weitere Treffer für Zielhäufigkeit 25 %: 15); 033 bleibt Vergleich mit Jonas’ falschem Argument, die Optionen sind angeglichen. |
| VT3-041 | Wie 036 (zwei Maßstäbe). | 036: Maßstab halbiert, Höhenunterschied (4 cm, Was-wäre-wenn); 041: zwei Diagramme mit verschiedenem Maßstab (Anna gegen Ben, 30 gegen 32 Kinder). Unterschiedliche Denkfiguren. |
| VT3-046 | Wie 043/047 (Achsenbeginn). | 046: Fehler-Detektiv zu Prozentpunkten (20 % → 30 %: 10 Prozentpunkte, aber 50 % mehr); 043 bleibt Achsenbeginn, 047 jetzt Seitenlänge verdreifacht, Fläche 9fach (Bild täuscht). Drei Denkfiguren. |
| VT3-062 | `zwei_wege` ohne zwei Wege; sechs von sieben dieselbe Rechenfigur. | 057 Umkehr (gestrichene Zahlen), 058 Ersetzen, 059 Fehler (Zielmittelwert), 060 Begründung, 061 zwei Wege (Abweichungen von 100), 062 Gruppen-Mittelwert (30 Personen, 10 Kinder), 063 Rundenzeiten. Mindestens fünf Denkfiguren im Lernziel. |
| VT3-008 | Test = dreischrittiges Rechnen. | Neu: Würfelbehälter 1 l/10 cm hoch, wie viele füllen einen Würfel von 1,5 m Kante (3375). Einsicht: Kantenverhältnis 15, dritte Potenz; Brücke Liter/cm³. |
| VT3-012 | `zwei_wege` nur Rechnen. | Auswahl: Quader gegen Würfel mit gleichem Fassungsvermögen (8 l), Denkfigur Größenvergleich ohne zu raten (alle Optionen begründet). |
| VT3-025 | Reines Rechnen, Stufe 2 genügt. | Neu: Würfel 10 cm, 4 cm dicke Scheibe abgeschnitten, wie viel Prozent bleiben (60 %). Einsicht: Anteil der Dicke, nicht das Volumen berechnen. Gerechnet als Transfer. |
| VT3-026 | „Ohne Ausrechnen“, richtige Option rechnet. | A (10·4·6) und B (10·6·4): dieselben drei Zahlen, gleiches Volumen; die Option begründet mit dem Vertauschen, nicht mit Ausrechnen; Optionen gleich lang. |
| VT3-036 | Test = zwei Divisionen und eine Subtraktion. | Siehe 041: Maßstab halbiert, Differenz der Säulen im neuen Diagramm (4 cm). |
| VT3-044 | Lösbar ohne Verständnis der Falle (160 : 80). | Neu: Marken 0, 10, 20, 40, 80, 160 in gleichem Abstand, Säulen bis 80 und bis 20: Verhältnis der Werte 4 (nicht der Höhen 2). Text sagt ausdrücklich „jeweils im gleichen Abstand“, so ohne Bild eindeutig. |
| VT3-009 | Richtige Option doppelt so lang. | Alle vier Optionen mit Rechnung bzw. Begründung ähnlicher Länge (89 bis 101 Zeichen). |
| VT3-064 | Richtige Option die längste, nur sie „höchstens“. | Optionen gleich lang (alle mit „denn“), die falschen mit „genau“/„mindestens“ nach demselben Muster. |
| VT3-086 | Richtige Option die längste; dreimal Punktprobe. | 086 Punktprobe mit Begründung (Länge angeglichen); 087 Fehler-Detektiv (Quadrat statt verdoppelt), 088 jetzt „P(a \| b) auf f(x) = 2x + 1, was gilt immer“ (Prüfen/Umkehren statt Einsetzen). |
| VT3-109 | Richtige Option mehr als doppelt so lang; Bestandsnähe. | Mia/Jonas: 9:00 und 3:00 Uhr gleich, 9:15 Uhr nicht (Stundenzeiger wandert), alle vier Optionen mit Begründung gleich lang. |
| alle Auswahl-Aufgaben | 34 von 49 längste, Index 2 in 25 Fällen. | Siehe Querschnitt: 14 von 54 (26 %), Plätze 14 · 14 · 13 · 13, feste Prüfung in `bauen.py`. |
| README „verstehen“ | Zwei Lernziele in einer Zeile. | README-Tabelle zeigt jetzt „verstehen (Volumen)“ (5 Denkfiguren) und „verstehen (Winkel)“ (6 Denkfiguren); `idee` der VT3-023 ist `begruenden`. |

## C

| Kennung | Befund | alt → neu / warum nicht |
|---|---|---|
| VT3-001 | Test nur ein Rechenschritt; Antwort 3 doppelt. | Neu (siehe oben): Länge +50 %, Breite −20 %, Höhe verdoppelt, Änderung in Prozent (140). Antwort 3 kommt in 004/006 nur als Zeilennummer bzw. Breite vor. |
| VT3-004 | Zahlen 5/3/4 wie Bestand. | Quader 6 · 4 · 3, richtig 72; Fehler Summe statt Produkt bleibt. |
| VT3-010 | Tool-Hinweis Fehlalarm. | Nicht geändert, in der README als erledigt geführt. |
| VT3-011 | Antwort 40 wie 008. | 008 jetzt 3375; 011 bleibt 40. |
| VT3-013 | Fehlbilder sind richtige Umrechnungen. | Nicht geändert: Die Frage „NICHT dasselbe“ lässt keine anderen Fehlbilder zu (die richtige Option ist die falsche Umrechnung 0,25 m³ = 250 l). Beschreibungen nennen die Fehlvorstellung. |
| VT3-014, VT3-021, VT3-008 | `idee` stimmt nicht. | Alle `idee`-Texte neu geschrieben (014 Wanne und Zufluss, 021 Quader aus Würfeln, Kantenlänge gesucht, 008 Brücke über Kantenverhältnis). |
| VT3-015 | Nähe nur im Wortlaut. | Nicht geändert (Vorprüfung: keine Änderung nötig). |
| VT3-019, VT3-021 | Gleiche Denkfigur Becken/Höhenänderung. | 021 ersetzt durch „Quader aus Würfeln, Höhe gesucht“ (andere Denkfigur: aus Schichten rückwärts). |
| VT3-020, VT3-023 | Gleiche Denkfigur „Schicht über der Grundfläche“. | 020 bleibt (Grundfläche und Höhe aus zwei Volumen), 023 ist eine Aussage über den Zuwachs (2 cm · Länge · Breite); inhaltlich zwei Denkfiguren (Gleichungspaar gegen Schichtbild), Label: 020 was_waere_wenn, 023 begruenden. |
| VT3-027 | FB 17 beschreibt anders als rechnet. | Der gespeicherte Text nennt jetzt beides („60 000 : 3 375 ≈ 17,8, abgerundet 17 (17 · 3 375 = 57 375)“), Wert bleibt. |
| VT3-029 | Dezimalhinweis; Antwort 7,5. | 029 ist jetzt ganzzahlig (15). Für VT3-112 (7,5) steht im Text „Gib das Ergebnis als Dezimalzahl an.“. 041, 053, 055 sind inzwischen ganzzahlig bzw. Auswahl. |
| VT3-032, 034, 042, 052, 053, 070, 077, 083, 087, 094, 095, 098, 126 | Rechnen nach Schema (Sammelbefund). | 034 jetzt „was gilt für jede Versuchsreihe“ (immer/nie), 053 Mittelwerte gleich, 070 Mengenschnitt (D, W; jetzt 5 Zahlen), 087 Fehler im Quadrieren, 095 Streichhölzer als Behauptungsprüfung (Auswahl), 126 Summe und Unterschied (Gleichungsdenken). 032, 042, 052, 077, 083, 094, 098 bleiben (je Lernziel höchstens zwei schema-nahe: 032/relative_haeufigkeit, 042/saeulendiagramm, 052/mittelwert, 077/stelle, 083/graph_lesen, 094/sachzusammenhang, 098/sachzusammenhang). |
| VT3-043 | Dreimal Achsenbeginn. | Siehe 046. |
| VT3-039, 045, 049, 060, 081, 082, 084, 099, 125 | Richtige Option deutlich länger. | Alle Optionen angeglichen (Längen siehe Querschnitt). |
| VT3-057 | Schema „Summe − Rest“. | Umkehr bleibt, Test jetzt mit Einsicht: Mittelwert der gestrichenen Zahlen aus zwei Mittelwerten (16). |
| VT3-058 | Gute Aufgabe, Antwort 10 wie 059. | 059 neu; 058 bleibt. |
| VT3-063 | Zweite Lücke „insgesamt“ nichtssagend, `idee` nennt Spannweite. | Einzelaufgabe: drei gleiche Runden gesucht (69 s), `idee` stimmt. |
| VT3-068 | Mit 064/067 dreimal „W kleiner als D“. | 068: „Welche Zuordnung ist keine Funktion“ (eines seiner Geschwister), Gegenbeispiel-Denken; 064 und 067 bleiben (Elementezahl von W). |
| VT3-069, VT3-075 | Bruchterme mit Definitionslücke. | Nicht geändert (vertretbar für M8 1, wie Bestand); 075 mit richtigem Fehlbild 81. |
| VT3-072 | Antwort 7 wie 071. | 072: Unterschied der Stellen über die Steigung (5), 071 jetzt 2. |
| VT3-073 | Tool-Hinweis Fehlalarm. | Nicht geändert, in der README erklärt. |
| VT3-074 | Einkleidung wie Bestand (Pflanze). | Wasserbecken, gleichmäßig gefüllt; Ansatz auswählen. |
| VT3-085, VT3-087 | Antwort 3 in beiden. | 085: P(2 \| 7), f an der Stelle −3, Ergebnis 22; 087 bleibt [3; 8] (Zeile, Wert). |
| VT3-097 | Option 3 nicht schlüssig. | Option 3 jetzt „Anfangs 8 Liter, verliert täglich 40 Liter“; Fehlbild: Anfangswert und Rate vertauscht. |
| VT3-102 | Zahlen kehren wieder. | Siehe 105. |
| VT3-104 | Eindeutig. | Nicht geändert außer Zahlen (35° gegen 55°). |
| VT3-106 | Bestandsübung 7:00 Uhr verrät die Ausgangsinformation. | Nicht geändert (Eindeutigkeit geprüft: nur 5:00 Uhr); Fehlbilder 10 und 2 sind benannt („Stunde verdoppelt“, „Schritte abgezogen“). |
| VT3-107, 108, 112 | Konvention Stundenzeiger nicht im Text. | 112 Satz „Der Stundenzeiger wandert gleichmäßig weiter.“ ergänzt; 107 und 108 behalten die Konvention im Lösungsweg und im Bestandsmuster. |
| VT3-111 | FB 12:15 Uhr erklärt 82,5° nicht. | Text: „den Stundenzeiger um 12:15 Uhr nicht weitergewandert gerechnet: Er steht schon bei 7,5°, also beträgt der Winkel 82,5° und nicht 90°“. |
| VT3-117 | FB 3 „durch den größten Teil geteilt“ unplausibel. | Aufgabe ersetzt: gleich große Teile von je 18°, Anzahl der Trennstrahlen (4); Fehlbilder: Teile = Strahlen (5), Schenkel mitgezählt (6), 90 − 18 (72). |
| VT3-118 | Beweis-Denken oben an der Klassengrenze. | „(jeder Teilwinkel ist größer als 0°)“ ergänzt; Aufgabe bleibt Sicherung (Zweifelsfall 2 in der README). |
| VT3-120, VT3-124 | Gleiche Denkfigur. | 124 ersetzt: 900° Drehung, volle Umdrehungen und Rest (2 und 180°). |
| VT3-121 | Geodreieck ohne Bild. | Text nennt die zwei Skalen („von links nach rechts und von rechts nach links“) und argumentiert nur mit stumpf/spitz; ohne Bild eindeutig (118°). |
| VT3-082 | Option 3 wahre Folgerung. | Option 3: „Der Graph ist eine Gerade, denn alle y-Werte sind positiv.“ (falsche Folgerung). |
| VT3-084 | Optionen 1 und 3 beginnen mit wahrem „nicht recht“. | Option 1 jetzt „Jonas hat recht, denn die +1 am Ende verschiebt den Graphen nach oben, also steigt er“ (Fehlbild: Achsenabschnitt als Steigung gelesen). |

## Schärfen ohne Bild (Auftrag 5)

- VT3-044: „Marken … jeweils im gleichen Abstand“ steht ausdrücklich im Text.
- VT3-119: „Die beiden Strahlen liegen innerhalb des Winkels, der erste näher an [AB]“ legt die Reihenfolge der Teile fest; gefragt wird nach dem äußeren Teil und dem Winkel zwischen [AB] und dem zweiten Strahl (35° und 55°).
- VT3-121: beide Skalen des Geodreiecks sind beschrieben, die Entscheidung stützt sich nur auf „stumpf“ gegen „spitz“.
- VT3-048: ein Diagramm, „Die Hochachse beginnt bei 0“.
- VT3-006, 075, 114: Fehlbilder wie oben, Rechnung führt exakt zum gespeicherten Wert (`gegenrechnung.py`).

## Offen

- VT3-110 ist jetzt Klasse 5, aber die Aussage „höchstens 180°“ verlangt, 6:00 Uhr (180°) als Grenzfall zu sehen; falls zu leicht, kann eine Zählaufgabe nach Rücksprache wieder ergänzt werden.
- 053 (Gruppen mit gleichem Mittelwert) lässt sich durch Beispielzahlen lösen; als Verstehensaufgabe vertretbar, der Test des Lernziels ist 050.
- Die Hinweise des Werkzeugs zu VT3-010, 063, 073, 115 sind falsch-positiv (README).
