# Korrektur nach der zweiten Vorprüfung (vorpruefung-2.md, Commit 75324ae3)

Form: Befund, dann „geschlossen wie“. Alle Nummern sind VT1B-Nummern. Stand der Prüfläufe am Ende: `bauen.py` OK (119 Aufgaben), `gegenrechnung.py` 0 Abweichungen, `tools/vtest_pruefen.py --runde 1b` ohne Fehler.

## A (6)

- A1, 080 wörtliche Bestandsdoppelung: Aufgabe ersetzt (Umrechnung in wissenschaftliche Schreibweise mit anderem Sachverhalt und anderen Zahlen, Z = −3); bauen.py meldet keine Doppelung.
- A2, 043 Test ersetzt: neuer Test mit neuer Einsicht, nicht mehr als Umbenennung einer Bestandsaufgabe.
- A3, 060 gab beide Ergebnisse vor: Aufgabe so umgebaut, dass nur ein Ergebnis gefragt und gegeben wird.
- A4, 105: genau eine Option ist als Aussage richtig („Nein, denn die Höhe ist nicht länger als …“). Alle Auswahl-Aufgaben der Runde auf „richtiger Schluss, falsche Begründung“ durchgesehen; betroffene Optionen umformuliert (Liste in `auswahl.md`).
- A5, vorsilben_klein (078 bis 084): höchstens 2 Schema-nahe Aufgaben, 5 oder mehr verschiedene Denkfiguren; 079, 081, 083, 084 neu gefasst, Tabelle im README.
- A6, negativer_exponent (071 bis 077): ebenso; 072 bis 075 und 077 neu bzw. umgebaut. Tabelle im README.

## B (16)

- B1 bis B5, Bestandsdoppelungen: ersetzt oder in deutlich anderer Form neu gebaut: 001, 009, 015, 035, 039, 045, 048, 049, 054, 056, 063, 066, 068, 075, 081, 096, 110 sowie 067, 085, 087, 088, 108, 109, 112 bis 119. Wo dieselbe Einsicht in klar anderer Form bleibt, steht sie im README als Hinweis für die Gegenprüfung. Die Aussage „kein Bestandsfünfeck“ im README ist korrigiert.
- B6, Doppelungen innerhalb der Runde und h = A : g gestreut: gleiche Sachverhalte in der Runde getauscht; Rückrechnungen von Höhe aus Fläche kommen nur noch einmal je Lernziel vor (101 ohne Division, Z = 96).
- B7, Denkfigur höchstens zweimal je Lernziel: Tabelle im README neu, per Hand nachgezählt.
- B8, Schema höchstens 2 je Lernziel in allen 17 Lernzielen: nachgezählt, README-Satz bleibt.
- B9, Tests 029, 057, 106: 029 und 036 und 050 und 022 anspruchsvoller bzw. weniger ratbar (siehe C5); 057 und 106 schwerer gefasst (106 mit Lücken [8, 11]).
- B10, 029 eindeutig: Bereich, Grenzen und „mindestens eine Lösung“ ausdrücklich genannt.
- B11, Textklarheit 035, 066, 099: Wortlaut präzisiert (099 mit „D oberhalb der x-Achse“).
- B12, Fehlbilder: 027 und 042 überarbeitet; jede Lücke einer Fehler-Detektiv-Aufgabe hat ein eigenes Fehlbild (bauen.py prüft das).
- B13, Lecks: 079, 078, 082 sowie 066/070 gegenüber 067/069 so gefasst, dass keine Aufgabe die Lösung der anderen verrät.
- B14, 062/063 unter fehler_finden: 063 ist ein echter Fehler-Detektiv; 062 widerlegt eine Behauptung. Beides bleibt unter fehler_finden.
- B15, Lehrplan: 053, 061, 058, 059 angepasst. Parameteraufgaben 024, 029, 034, 036, 039, 043 bleiben; im Bestand gibt es solche Fragen nur außerhalb der Jahrgangsstufe 6, ein Lehrplanbeleg dafür liegt mir nicht vor (offen, ich habe nichts erraten). README: Prozentpunkte stehen in M6 Lernbereich 3, nicht „Klasse 7“. Offen gelassen: wissenschaftliche Schreibweise, Vorsilben nano und mikro (in der Jahrgangsstufe 6 nicht belegt).
- B16, 002 und 032 echt auf zwei Wegen lösbar: beide Wege liefern wirklich verschiedene Rechnungen.

## Auswahl

- Verneinung angeglichen: 2 bis 3 richtige Optionen mit Verneinung.
- Positionen: `POSITION4` in `kern.py` ohne Periode 12 (feste Folge, danach 2, 0, 3, 1); 061 setzt pos selbst.
- Verteilung der Positionen in den 35 Auswahl-Aufgaben: 8/9/9/9.

## C

- C1 Beschreibungen: 005, 031 (Vierfache), 071, 109.
- C2: 090 Fehlbild ist jetzt 6 statt Gleitkommawert 6e-07.
- C3: 087 ohne gleichwertige Optionen.
- C4: 017 behält „Prozentpunkte“ in der Lösung, Vorrat geprüft.
- C5, kleine Zählantworten (neu in diesem Schritt):
  - 022: Bereich −12 bis 12, Antwort 24.
  - 029: k von −5 bis 14, Antwort 18.
  - 036: b von −9 bis 9, Antwort 18.
  - 050: jetzt Lücken-Aufgabe (kleinster und größter Exponent mit 1/200 < 2ⁿ < 40, Lücken [−7, 5]), weil die Zählvariante mit Bestandsaufgaben (3ˣ-Aufgabe, reinquadratisch) doppelte.
  - gegenrechnung.py entsprechend angepasst, 0 Abweichungen.
- C6 Positionen: siehe Auswahl.
- C8: 024 bleibt Stufe 2, weil der Korrektur-Pool nur Stufe 2 enthält.

## Offene Zweifel

- Parameteraufgaben (024, 029, 036, 039, 043, 050) ohne Lehrplanbeleg für Jahrgangsstufe 6; Entscheidung bei der Sammelprüfung.
- Schema-nah und Denkfiguren sind von Hand eingeschätzt.
