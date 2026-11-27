# rollend-11: Aufgaben Stufe 3 (Vorrat, nicht eingespielt)

Stand 27.11.2026, Kürzel `S3`, Kennungen S3-V001 bis S3-V060. Zweck: Jede Lernkarte in `rollend-5` und `rollend-7`, die keine Aufgabe der Stufe 3 hat, bekommt genau eine zählende Aufgabe (`zaehlt = ja`, `s` = 3) in einer Form, die in dieser Lernkarte noch fehlt.

## Übersicht je Thema
Spalten: Klasse, Einheit, Lernkarten ohne Stufe 3, neue Aufgaben, Formen (FD Fehler-Detektiv, UM Umkehren, ZW Zwei Wege, BR Brücke, AN Anwenden).

| Kl. | Thema | LK ohne S3 | neu | Formen |
|---|---|---|---|---|
| 5 | messen.koerper_darstellung | 3 | 3 | BR2 UM1 |
| 5 | stochastik.kombinatorik | 4 | 4 | AN1 FD1 UM1 ZW1 |
| 5 | zahlen.ganz | 6 | 6 | BR1 FD2 UM1 ZW2 |
| 5 | zahlen.natuerlich | 7 | 7 | AN2 FD2 UM1 ZW2 |
| 5 | zahlen.potenzen_basis | 3 | 3 | AN1 BR1 FD1 |
| 5 | zahlen.rechengesetze | 6 | 6 | AN1 BR2 FD1 UM2 |
| 8 | gleichungen.bruch | 5 | 5 | AN2 FD1 UM2 |
| 8 | gleichungen.linear | 4 | 4 | AN1 BR1 FD1 UM1 |
| 8 | groessen.indirekt | 1 | 1 | ZW1 |
| 8 | messen.prisma_zylinder | 2 | 2 | BR1 UM1 |
| 8 | stochastik.grundbegriffe | 3 | 3 | AN1 BR1 UM1 |
| 8 | terme.bruchterme | 4 | 4 | BR2 FD1 ZW1 |
| 8 | terme.potenzgesetze_ganzzahlig | 3 | 3 | FD2 ZW1 |
| 8 | terme.potenzgesetze_natuerlich | 2 | 2 | FD1 ZW1 |
| 8 | terme.quadratische_extreme | 1 | 1 | AN1 |
| 8 | terme.umformen | 3 | 3 | AN1 FD1 ZW1 |
| 8 | terme.umformen_teil2 | 3 | 3 | BR1 UM1 ZW1 |

Summe Klasse 5: 29 Lernkarten, 29 Aufgaben (FD 7, UM 6, ZW 5, BR 6, AN 5). Summe Klasse 8: 31 Lernkarten, 31 Aufgaben (FD 7, UM 6, ZW 6, BR 6, AN 6). Fehler-Detektive: 14 von 60, je Klasse höchstens ein Drittel. Kein Lückenweg.

## Aufbau
- Eine JSON-Datei je Thema im Format von `rollend-7`; `th_*.py` sind die Quellen, `kern.py` die Bausteine, `bauen.py` erzeugt die JSON und prüft.
- `g` (Stufe 3): Detektiv `fehler`, Umkehren `rueckwaerts`, Zwei Wege und Brücke `verknuepfen`, Anwenden `transfer`.
- Antworten nur `zahl` oder `auswahl`; Zeichnung nur `tabelle`. `thema` ist die Einheit, `l` die Lernkarte, `t` wie im Bestand.

## Prüfungen
- `python3 -I inhalte/mathe-profi/rollend-11/bauen.py` endet mit OK. Es prüft: Lösung jeder Aufgabe durch Rechnung; jedes Fehlbild mit `rechnung` ergibt die gespeicherte falsche Antwort; Fehler-Detektiv Zeile für Zeile (genau eine falsche Zeile, Rest stimmt); bei Auswahl genau eine richtige Antwort und keine zwei gleichen; Form kommt in der Lernkarte noch nicht vor; `l` und `t` gehören zur Einheit; Fragetext nicht doppelt und nicht der Bestandstext mit anderen Zahlen; Ergebnis ab 10 steht nicht in Text oder Hinweis; Verteilung von Fehlerzeile (1:4, 2:4, 3:4, 4:2) und Lage der richtigen Auswahlantwort.
- `python3 -I tools/inhalt_pruefen.py` an Kopien aller betroffenen Themen mit den neuen Aufgaben: Code 0.
- `python3 -I tools/rollend_sql.py --runden 11`: OK, 60 Aufgaben, 17 Einheiten, `zaehlt` nur ja, 12 mit Tabelle; auch mit `--runden 5,7,11` ohne Fehler. Das Werkzeug wurde nicht geändert.
- Schlussdurchsicht als strenger Gegenprüfer (Liste B: eindeutig, Voraussetzungen, allgemein gültig, Hinweis verrät nichts, Form hält ihr Versprechen): alle 60 durchgerechnet. 15 Aufgaben geändert (14 Hinweise, die Fehler oder Weg verrieten, 1 unklarer Fragetext bei S3-V037).

## Annahmen
- Die Lernkarten ohne Stufe 3 wurden aus `aufgabe.s` in `rollend-5` und `rollend-7` gezählt (29 und 31).
- `tools/vorrat_pruefen.py` erfasst nur `rollend-1` bis `-4`; es wurde nicht geändert und nicht auf `rollend-11` angewendet.

## Offen
- Fehlbild-Kennungen (`fehlbild`) sind überall `null`; sie müssen bei Bedarf einem Fehlbild-Katalog zugeordnet werden.
- Bei Fehler-Detektiven und einigen Auswahlaufgaben gibt es keine `rechnung` je Fehlbild, nur Beschreibungen (33 Fehlbilder). Einige Fehlbild-Rechnungen sind kurze Zahlen ("2", "4 + 1").
- Anzeige in der App nicht getestet (Tabellen, Index-Antworten).
- Lernkarten, die in `rollend-5/7` später noch Stufe 3 bekommen, würden hier doppelt besetzt.
