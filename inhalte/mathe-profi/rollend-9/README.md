# rollend-9 (K9A): Aufgaben auf Vorrat in neuen Formen, Klasse 9

58 Lernkarten, je drei Aufgaben, 174 Aufgaben (K9A-V001 bis K9A-V174). Nichts davon ist eingespielt.
Erzeugen und prüfen: `python3 -I bauen.py` (muss mit OK enden). Die Aufgaben stehen in `th_<Thema>.py`, die Ausgabe in `<Thema>.json`.

| Thema | Lernkarten | Aufgaben | Lückenweg | übrige Formen | zählt ja / nein |
|---|---|---|---|---|---|
| zahlen.wurzeln_basis | 6 | 18 | 6 | 12 | 12 / 6 |
| zahlen.reell | 8 | 24 | 6 | 18 | 18 / 6 |
| gleichungen.wurzel | 6 | 18 | 5 | 13 | 13 / 5 |
| gleichungen.quadratisch | 8 | 24 | 7 | 17 | 17 / 7 |
| funktionen.quadratisch | 9 | 27 | 9 | 18 | 18 / 9 |
| stochastik.grundbegriffe_teil2 | 4 | 12 | 3 | 9 | 9 / 3 |
| stochastik.verknuepft | 11 | 33 | 8 | 25 | 25 / 8 |
| stochastik.simulation | 6 | 18 | 5 | 13 | 13 / 5 |

Gesamt: Lückenweg 49, Zwei Wege 20, Umkehren 28, Brücke 22, Fehler-Detektiv 26, Anwenden 20, Verfahren wählen 9 (Verfahren wählen auch als Aufgabe „erkennen“ auf Stufe 1, dann zählt es als zählend).
Stufen: je 58 Aufgaben auf Stufe 1, 2 und 3 (je Lernkarte genau eine). Der Lückenweg steht immer auf Stufe 1.

## Was maschinell geprüft ist (bauen.py)
- Jede Lösung wird zweimal berechnet (Rechenanker `c` und unabhängige Zweitrechnung); jedes Fehlbild mit Rechnung wird nachgerechnet.
- Lückenaufgaben: kein Lückenwert als Ziffer, Zahlwort oder Hochzahl in Text, Schablone, Tipp; spätere Lücken hängen nachweislich an früheren.
- Fehler-Detektiv: genau eine erste Fehlerzeile (Zeile 1 bis 4 gleichmäßig verteilt), Folgezeilen rechnen aus der falschen Zeile richtig weiter.
- `tools/vorrat_pruefen.py` (i) bis (iv) meldet 0; `inhalt_pruefen` läuft auf einer Kopie des Bestands mit den neuen Aufgaben; `t` entspricht dem Bestand der Lernkarte.
- Stufe je Lernkarte: mindestens eine zählende neue Form auf Stufe 2 und eine auf Stufe 3.

## Annahmen und offene Punkte (nicht maschinell belegt)
- Sachtexte nennen die Annahmen ausdrücklich (fair, mit Zurücklegen, gleich wahrscheinlich); ob jede Formulierung für Klasse 9 gut lesbar ist, hat nur die Durchsicht geprüft.
- Einzelne Aufgaben setzen Rundung voraus („auf ganze Prozent“); die Toleranz kommt aus dem Wert, nicht aus einer eigenen Angabe.
- Die Fehlbild-Beschreibungen sind in Worten gehalten. Ob ein Kind wirklich so rechnet, ist angenommen, nicht beobachtet.

## Fehlbilder ohne Rechnung (117)
Es sind Antworten bei Auswahlaufgaben (Begründungen, Mengenschreibweisen, Aussagen über Gerätewahl) und die Zeilen im Fehler-Detektiv. Dort gibt es keine Zahl, die nachgerechnet werden kann. Bei Zahlaufgaben haben alle Fehlbilder eine Rechnung.

## Lernkarten, in denen eine Form schlecht passt
- stochastik.verknuepft / elemente und mengen_verstehen: „Zwei Wege“ und „Anwenden“ passen kaum zu reinen Mengenfragen; dort stehen Verfahren wählen, Umkehren und Fehler-Detektiv.
- zahlen.wurzeln_basis / wurzel_deuten und reell / zahlarten, irrational_beweis: statt Anwenden stehen Verfahren wählen, Umkehren und Fehler-Detektiv.
- Verfahren wählen steht nur auf erkennenden Lernkarten (Stufe 1).
