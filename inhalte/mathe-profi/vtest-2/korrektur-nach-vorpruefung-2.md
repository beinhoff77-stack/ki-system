# Korrektur nach der zweiten Vorprüfung (Befund → geschlossen wie)

Stand: Zweig `helfer-vtest-r2`. Prüfungen: `bauen.py` feste Prüfungen ok, `gegenrechnung.py` 0 Abweichungen, `vtest_pruefen.py --runde 2` ohne Fehler.

## B-Befunde

- Doppelung 112 und 107 → beide neu: 107 Randfälle an der Rundungsgrenze (4 499, 4 500, 5 499), 112 kleiner Unterschied, großer Sprung (1 249 und 1 250).
- Doppelung 022 und 092 (beides Tests) → 022: Laufzeit zweier Anlagen angleichen; 092: Stellenzahl und Tausenderklasse aus dem Zahlwort (204 007 005).
- 045 → Umformungskette auf Gleichwertigkeit; 083 → zuerst Rückwärtsschluss über Winkelhalbierende, dann (nach Handvergleich) drei Winkel aus zwei Teilwinkeln; 114 → gleiche Rechnung, andere Rundungsrichtung.
- Handvergleich → `bestandsvergleich.md`; dabei weitere Doppelungen gefunden und ersetzt: 015, 030, 034, 043, 064, 103, 113, 122, 126, 128, 131.
- 038 (k = 5 steht als 5 im Text) → Wert im Text jetzt 4, k = 6.
- 081/079 („Mittelsenkrechten“ im Text) → die gesuchte Nummer steht nicht mehr im Text; Fehler liegt in Zeile 2 (Inkreisgedanke beim Umkreis). Überschneidung 079/081 bleibt als offener Zweifel.
- 120 → die Regel (dieselbe Ziffer höchstens dreimal hintereinander) wird ausdrücklich genannt. 124 → Fehlbild 8 beschreibt jetzt genau die gezählten 8 (XL ohne 44 und 49).
- Muster in der Auswahl: 054, 110, 082 → Möglichkeiten gleich gebaut, 110 mit drei „manchmal/nie“-Aussagen, 082 mit zwei „Richtig“ und zwei „Falsch“.
- Gruppenbefund (043, 054, 096, 110, 111, 115, 117, 125: richtige Möglichkeit als einzige ohne denn/weil) → alle Möglichkeiten gleich gebaut; Lücke zwischen richtig und falsch jetzt 57 % zu 57 %.
- „Beide gleich …“ → Verteilung ausgeglichen: Sammel-Möglichkeiten 5, davon richtig 2 (115, 129). Absolutwörter: falsch 30 %, richtig 32 %.
- Reine Schema-Aufgaben (006, 009, 010, 029, 032, 034, 053, 056, 058, 061, 090, 104) → höchstens zwei je Lernziel behalten, die übrigen ersetzt (009, 029, 034, 053, 058 und weitere).
- runden_regel mindestens fünf Denkfiguren → sieben verschiedene, keine öfter als zweimal.
- Tests nicht die schwersten ihres Lernziels (008, 029, 043, 099, 106, 120, 127) → alle verschärft (008 Lückenform, 029 zwei Umfänge für jedes x, 043 sechs Terme, 099 Skala ohne Nullpunkt, 106 Zählen über einen Bereich, 120 Regel anwenden und Längen vergleichen, 127 Wertebereich).
- 078 (3 bis 5 Minuten) → kürzer zu zählen (Soll 38).
- 005 (vermehrter Grundwert) → in README als Lehrplanzweifel vermerkt.

## Fest im Bauskript

`bauen.py` prüft jetzt dauerhaft: denn/weil-Einzelgänger (richtige als einzige mit oder ohne), Lücke denn/weil und Absolutwörter höchstens 12 Punkte, Sammel-Möglichkeiten (ab 5 mindestens 25 % richtig), mittlere Länge richtig/falsch zwischen 0,90 und 1,15, Platzverteilung, Ideen je Lernziel.

## C-Befunde (soweit sinnvoll)

- 064, 068, 013/023, 040, 052, 037, 099, 014, 077 → Texte und Fehlbilder überarbeitet, siehe `sonderfaelle.md`.
- 042 und 075 → Stufe 2 belassen, begründet.
- Nicht geändert: reine Geschmacksfragen; offene Lehrplanzweifel stehen im README.
