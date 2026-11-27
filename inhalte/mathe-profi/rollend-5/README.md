# rollend-5: Vorrat an Aufgaben in neuen Formen (Klasse 5, Kürzel K5)

58 Lernkarten in 6 Themen, je Lernkarte genau 3 Aufgaben (174). Nichts ist eingespielt. Jeder Eintrag trägt `thema`, `lernkarte`, `form`, `zaehlt`, Regel-Kennung, Fehlbilder und unter `aufgabe` die Aufgabe im Format von `inhalte/README.md`. Kennungen `K5A-V001` bis `K5A-V174`, Datei je Thema.

Neu bauen und prüfen: `python3 -I inhalte/mathe-profi/rollend-5/bauen.py` (muss mit "OK" enden). Inhalte stehen in `inh_*.py`, Hilfsfunktionen in `k5basis.py`.

## Übersicht

| Thema (Datei) | Lernkarten | Aufgaben | Formen | zaehlt ja/nein |
|---|---|---|---|---|
| zahlen.natuerlich (`natuerlich.json`) | 13 | 39 | LW 7, FD 6, VW 2, ZW 4, UM 5, BR 5, AN 10 | 32 / 7 |
| zahlen.rechengesetze (`rechengesetze.json`) | 14 | 42 | LW 7, FD 7, VW 3, ZW 4, UM 7, BR 4, AN 10 | 35 / 7 |
| zahlen.potenzen_basis (`potenzen_basis.json`) | 7 | 21 | LW 3, FD 4, VW 1, ZW 2, UM 4, BR 3, AN 4 | 18 / 3 |
| zahlen.ganz (`ganz.json`) | 11 | 33 | LW 6, FD 5, VW 2, ZW 4, UM 5, BR 3, AN 8 | 27 / 6 |
| stochastik.kombinatorik (`kombinatorik.json`) | 7 | 21 | LW 3, FD 3, VW 2, ZW 2, UM 4, BR 2, AN 5 | 18 / 3 |
| messen.koerper_darstellung (`koerper_darstellung.json`) | 6 | 18 | LW 2, FD 2, VW 2, ZW 2, UM 3, BR 2, AN 5 | 16 / 2 |
| Summe | 58 | 174 | LW 28, FD 27, VW 12, ZW 18, UM 28, BR 19, AN 42 | 146 / 28 |

(LW Lückenweg, FD Fehler-Detektiv, VW Verfahren wählen, ZW zwei Wege, UM umkehren, BR Brücke, AN anwenden.) Lückenwege sind `zaehlt = nein`, alle anderen `ja`.

## Wie geprüft (vom Programm, alle Prüfungen enden mit "OK")
- Jede Zahl-, Lücken-Lösung: `c` über `tools/inhalt_pruefen.py` berechnet und mit einem zweiten, anders gebauten Ausdruck verglichen. Auswahl und Text: Wahrheitswert aus einer Python-Rechnung, genau eine richtige Antwort.
- Je Lernkarte genau 3 Aufgaben, höchstens 1 Lückenweg, höchstens 1 Fehler-Detektiv, mindestens 1 zählende Form (umkehren, zwei Wege, Brücke, Verfahren wählen, anwenden). Je Thema kommen umkehren, zwei Wege, Brücke und anwenden mindestens zweimal vor.
- Lückenwege: Antwortform `luecken`, mindestens 2 Lücken, spätere Lücken greifen im Text auf frühere zurück, kein Lückenwert steht im Text oder Tipp (ab 10 geprüft).
- Fehler-Detektiv: Frage "In welcher Zeile passiert der erste Fehler?", 3 bis 4 Zeilen, genau 1 Fehlerzeile, so viele Antworten wie Zeilen. Folgezeilen rechnen mit dem Fehler korrekt weiter. Fehlerzeile 1/2/3/4: 7/7/7/6 (keine Zeile über einem Drittel von 27).
- Ergebnis steht nicht im Text, Tipp verrät es nicht ab 10; keine Namen Leo oder Rosa; keine Dopplung zum Bestand (Fragetext und Bau ohne Zahlen).
- Kopien der Themen-Dateien mit den neuen Aufgaben: `python3 -I tools/inhalt_pruefen.py` ohne Fehler.

## Annahmen und offene Punkte (nicht gesichert)
- Die Zuordnung Form zu `g` ist von mir festgelegt: Lückenweg direkt, Fehler-Detektiv fehler, zwei Wege mehrschritt, Verfahren wählen je nach Tätigkeit (siehe „Nach Gegenprüfung“), umkehren umkehr (zwei Aufgaben rueckwaerts), Brücke darstellung, anwenden einkleidung. Bitte gegen `verhaeltnis.md` prüfen. Alle 42 anwenden-Aufgaben sind Typ einkleidung, keine transfer/pruefung.
- Fehlbild-Kennungen sind nur gesetzt, wo ein passender Eintrag in `regeln-uebersicht/kennungen.json` existiert; sonst `null`.
- Zeichnungen: nur vorhandene Bauteile (Tabelle, Zahlenstrahl mit Pfeil/Punkten, Baum). Das Aussehen im Gerät ist nicht geprüft, ebenso nicht die Darstellung von Zahlenstrahl-`punkte` ohne Bogen.
- Zylinder-Aufgaben bleiben ohne π (Umfang wird gegeben), wie im Bestand.
- Einige "umkehren"-Aufgaben (z. B. Quadratwurzel, Fakultät, Turnier) sind durch Probieren lösbar; die Tipps nennen das Probieren.
- Nicht geprüft: Test mit Kindern, Lesbarkeit der Aufgabentexte durch Gegenprüfung (fachlich und sprachlich).

## Form passt fachlich schlecht
- ziffern_zu_zahlwort, zwei Wege: Die beiden Wege rechnen nur die Gruppengröße; die Aufgabe liest keine Zahlwörter laut.
- roemisch_system und unendlich: "zwei Wege" und "Brücke" passen nur mühsam; dort stehen Fehler-Detektiv, zwei Wege oder anwenden.
- Keine Lernkarte zurückgestellt.

## Nach Gegenprüfung (Werkstatt 1041/1042)
- Geändert: 68 von 174 Aufgaben (Inhalte in `inh_*.py`, Dateien neu gebaut). `bauen.py` endet mit OK, `inhalt_pruefen.py` ohne Fehler. Eine zweite, vollständigere Gegenprüfung (Werkstatt 1045) wurde danach abgearbeitet: Faltvorgang und Nachrichtenkette eindeutig, Bandstreifen statt Schnittmuster bei den Etiketten, Zahlwort aus Ziffern in der Lernkarte ziffern_zu_zahlwort, Überträge selbst ermitteln, Richtung beim Addieren nach Vorzeichen, Sprungbogen auf dem Zahlenstrahl, Buchstabenfolgen statt Wörter.
- Art der Änderungen: Fehlbilder neu nachgerechnet und ihre Beschreibung dem Rechenfehler angepasst (falscher Wert oder falsche Begründung); Gerüste so umgebaut, dass der Text keine Lücke mehr vorwegnimmt und spätere Lücken von früheren abhängen; fehlende Voraussetzungen im Text ergänzt (Körperform, Wiederholung, Unterscheidung nach Person, Höhenunterschied, Schnittmuster); Auswahlaufgaben mit zwei gleichwertigen oder zwei richtigen Antworten bereinigt; „Zwei Wege“, die dieselbe Rechnung zeigten, durch einen wirklich anderen zweiten Weg ersetzt; mehrdeutige Fragen und Zahlenwerte (Rundung von Geldbeträgen, Etiketten, Packungsgröße) eindeutig gemacht.
- Feld `g` der 12 Aufgaben „Verfahren wählen“ nach tatsächlicher Tätigkeit: 8 erkennen, 2 begründen, 2 mehrschritt. Die erlaubten Werte der Form stehen in `k5basis.py`.
- Zusätzlich selbst gefunden: Fehlbilder, die aus dem Gerüst gar nicht entstehen können, Gerüste mit vorgegebenem Kernschritt, eine Auswahl mit zwei gleich großen falschen Werten, „Zwei Wege“ mit gleicher Rechnung, ein Fehlbild ohne nachvollziehbaren Rechenweg.
- Noch offen: Darstellung der Aufgaben im Gerät, Test mit Kindern.
