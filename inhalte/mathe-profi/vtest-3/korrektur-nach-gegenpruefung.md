# Überarbeitung nach Urteil 1222 (Gegenprüfung, Runde VT3: „Muss vorher“)

Quelle: Urteil 1222 der Gegenprüfung (privater Befund, hier nur unter diesem Namen genannt). Stand: `git fetch origin && git merge origin/lernen-app` ist gemacht. Alle Muss- und Soll-Punkte sind umgesetzt; Befund → geschlossen wie.

## Muss

| Befund | geschlossen wie |
|---|---|
| Lücken ohne eigenes Fehlbild: erste Lücke bei 004, 010, 016, 024, 031, 037, 046, 052, 059, 067, 069, 073, 080, 087, 094, 101, 108, 113, 123; zweite Lücke bei 020 | Für jede dieser 20 Lücken ein typisches falsches Eingabe-Paar mit Rechnung und Erklärung ergänzt (bei den Fehler-Detektiven: die Zeile, die man für den Fehler hält, weil sie nur das falsche Ergebnis wiederholt; bei 069 die vertauschte Reihenfolge; bei 020 die Höhenunterschied-Falle und die Höhe des falschen Quaders). Neue feste Prüfung in `bauen.py`: „jede Lücke hat ein Fehlbild“, auch die Zeilen-Lücke der Fehler-Detektive; sie bricht ab, wenn eine fehlt. |
| 027: Becken nicht als anfangs leer genannt | Text: „Ein anfangs leeres quaderförmiges Becken …“. Die Erklärung nennt das Gegenbeispiel: Stünde das Wasser anfangs schon 15 cm hoch, wären es 7,5 cm je Stunde und 90 cm erst nach 10 Stunden. |
| 049: Fragetext verrät die Antwort („denselben Verkauf“) | Neu gefasst: zwei gleich breite Liniendiagramme mit gleichem waagerechten Abstand, Hochachse 0 bis 100 über 10 cm gegen 2 cm, beide Linienzüge von 40 auf 60. Gefragt ist, welche Aussage stimmt; richtig ist „A steigt steiler, der Verkauf ist in beiden um 20 gestiegen, nur der Maßstab ist verschieden“. Weil der waagerechte Maßstab gleich ist, folgt „steiler“. Keine Option verrät das Ergebnis im Fragetext. |
| 068: „eines seiner Geschwister“ mehrdeutig (Einzelkinder) | Konkrete Gruppe: Mia, Ben und Zoe, Mia und Ben sind Geschwister, Zoe hat keines in der Gruppe; Definitionsmenge D = {Mia; Ben; Zoe}. Nur die Geschwister-Zuordnung gibt Zoe keinen Wert. |

## Soll

| Befund | geschlossen wie |
|---|---|
| 122 liegt am Bestand | Ersetzt: „Ein spitzer Winkel wird verdoppelt. Welche Aussage über den entstehenden Winkel stimmt immer?“ (kleiner als 180°; Gegenbeispiele 2 · 30°, 2 · 45°, 2 · 70°). Kern im Bestand gesucht, #261 und GE3-15 prüfen andere Aussagen. |
| 040 liegt am Bestand | Ersetzt: Säulenbreite sagt nichts über die Anzahl, nur die Höhe zählt (zwei gleich hohe, verschieden breite Säulen). Nähe zu den Piktogramm-Breiten #144 bis #151 ist in der README als Zweifel genannt. |
| 100 verlangt mehr als der Test 099 | Getauscht: Die Aufgabe mit drei Geraden und sechs Winkeln (wie viele spitz) ist jetzt der Test 099 (Stufe 3), die Begründungsaufgabe „ein Winkel 90°, alle 90°“ ist jetzt 100 (Korrektur, Stufe 2). Gegenrechnung und Ideen-Etiketten getauscht. |
| 106 über die Anzeige 15:30 | Neu gefasst: „Eine Digitaluhr zeigt 15:30 Uhr … kleinerer Winkel auf der Analoguhr mit 12-Stunden-Zifferblatt“, Ergebnis 75°. Fehlbilder: Stundenzeiger auf der 3 (90°), 15 · 30° mit überstumpfem Winkel (270°), Winkel des Stundenzeigers allein (105°). |
| 113 mit sechs gleich großen Teilen erklären | Fehler-Detektiv ohne Gleichung: ein äußerer Teil = ein Stück, ein mittlerer Teil = zwei Stücke, zusammen 1 + 2 + 2 + 1 = 6 Stücke, ein Stück 90° : 6 = 15°, mittlerer Teil 30°. Keine Variable (Klasse 5). |
| Winkelhalbieren nur mit vorgegebener Bedeutung | Ich habe keine Aufgabe gefunden, die das Halbieren eines Winkels verlangt (VT3-117 war schon früher ersetzt). Das Wort „halbiert“ steht nur noch im Fehlbild für „durch 2 geteilt“ (z. B. 113 und 120), dort mit der Bedeutung im Text. Keine Konstruktion der Winkelhalbierenden (Klasse 7). Hier dokumentiert, nichts zu ändern. |
| 057, 043, 028 dürfen bleiben | Unverändert; in der README unter den Zweifeln weitergeführt. |

## Schema streng

Maßstab: auch Zahlenvergleiche und Fehler-Detektive, die man durch bloßes Ausrechnen löst, zählen. Die Gegenprüfung zählte je Lernziel in der Kennungsfolge 2 / 4 / 3 / 2 / 2 / 4 / 1 / 2 / 2 / 2 / 3 / 2 / 3 / 2 / 2 / 2 / 2 / 2. Über zwei lagen fünf Lernziele; dort wurden Routinen durch Verstehensaufgaben mit anderer Denkfigur ersetzt (Bestandskern jeweils gesucht):

| Lernziel | vorher | ersetzt | neuer Gedanke (Denkfigur) |
|---|---|---|---|
| liter | 4 (010 bis 013) | 012, 013 | 012: ein Gefäß mit 1 Liter, die Form ist nicht festgelegt (immer_nie); 013: Reihe aus 1-cm-Würfeln, 10 m lang, wie viele Liter (zusammenhang) |
| rueckwaerts | 3 | 021 | Volumen geviertelt bei gleicher Höhe, Seite der quadratischen Grundfläche 6 cm auf 3 cm (zusammenhang) |
| saeulendiagramm | 4 | 040, 041 | 040: Säulenbreite zählt nicht (gegenbeispiel); 041: welche Säulenhöhe ergibt keine ganze Kinderzahl bei 1 cm für 4 Kinder (pruefen). Eine erste Fassung von 041 („1 cm für doppelt so viele Kinder, jede Säule halb so hoch“) stand schon im Bestand (#211) und wurde verworfen. |
| stelle | 3 | 074, 077 | 074: fallende Funktion, a < b, daraus f(a) > f(b) (immer_nie); 077: f(6) in der Mitte zweier bekannter Stellen (transfer) |
| punkt_graph | 3 | 086 | Mittelpunkt zweier Graphpunkte einer linearen Funktion liegt auf dem Graphen (zusammenhang) |

Nach dem Umbau haben alle 18 Lernziele höchstens zwei schema-nahe Aufgaben (eigene Zählung, 37 von 126, Tabelle in der README), mindestens sechs verschiedene Denkfiguren, keine mehr als zweimal (feste Prüfung in `bauen.py`). Offene Grenzfälle: 042, 104, 112, 123 (README).

## Verbotene Ablenker

Alle 63 Auswahl-Aufgaben einzeln gelesen: Eine falsche Option darf kein richtiges Urteil oder keine richtige Folgerung mit nur falscher Begründung tragen. Gefunden und so umgebaut, dass jede falsche Option auch im Urteil falsch ist:

- 099 (jetzt 100), Option 2: „Mia hat recht, denn jede Kreuzung hat vier gleiche Winkel“ → „Nur zwei der vier Winkel sind 90° groß …“.
- 086 (neu gebaut, siehe oben): die Option „Ja, denn die Koordinaten sind verschieden“ entfällt, alle drei falschen Optionen urteilen falsch.
- 084, Option 4: „Jonas hat nicht recht, denn der Graph fällt nur flach …“ (richtiges Urteil, falsche Begründung) → „Jonas hat recht, denn das Minus dreht nur die Rechenrichtung um …“.
- 121, Option 3: „falsche Skala, denn 90° − 64° = 26°“ (richtiges Urteil, falsche Rechnung) → „Der Winkel ist 26° groß …“.
- 095: drei Optionen urteilen „Mia hat nicht recht“, die falschen nennen aber einen falschen Term (3n, 4 + 3n) oder eine falsche Zahl (6 Hölzer); die Folgerung ist dort falsch. Ich habe sie so belassen und vermerke es hier.

Die Prüfung steht jetzt als Punkt (d) in `sonderfaelle.md`.

## Bestand und rollend-15

Der Kernvergleich wurde neu gerechnet (`bestandsvergleich.md`, jetzt „nach Urteil 1222“). Der Ordner `inhalte/mathe-profi/rollend-15/` mit 207 neuen Aufgaben ist einbezogen. Keine seiner Lernkarten gehört zu den fünf Einheiten dieser Runde (messen.volumen, daten.darstellen, daten.kennwerte, funktionen.grundbegriffe, geometrie.winkel); sie liegen bei terme.umformen, zahlen.*, gleichungen.* und trigo.*. Ein unmittelbarer Überschneidungskern ist daher nicht möglich; die Suche nach den Kernen der geänderten Aufgaben wurde trotzdem über den Ordner mitgeführt (ohne Treffer).

„Gleiche Einsicht bei anderer Denkleistung darf bleiben; bloßer Zahlen- oder Namenswechsel reicht nicht“: Nach dieser Regel geprüft; die einzigen Nähen in der Mitte sind VT3-040 (Piktogramm-Breite), 106 (11:30 Uhr, #127) und 077/072 (zwei Aufgaben zur Geraden, verschiedene Frage); sie stehen in der README.

## Prüfungen nach dem Umbau

- `python3 -I tools/vtest_pruefen.py --runde 3` → OK – keine Fehler.
- `python3 -I inhalte/mathe-profi/vtest-3/bauen.py` → OK, 126 Aufgaben, 63 Auswahl, Plätze 15/16/16/16, richtige Option in 29 % die längste.
- `python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py` → 126 Aufgaben, 0 Abweichungen.
