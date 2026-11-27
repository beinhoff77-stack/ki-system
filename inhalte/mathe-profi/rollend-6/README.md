# Vorrat neue Formen, Runde rollend-6 (Klasse 6, Kennung K6-V001 bis K6-V198)

Nur Aufgabenvorrat, keine App-Änderung. Je Lernkarte 3 Aufgaben (Stufe 1 / 2 / 3).

| Thema | Lernkarten | Aufgaben | Formen lw/fd/vw/zw/um/br/an | zaehlt ja/nein |
|---|---|---|---|---|
| bruch.brueche | 14 | 42 | 14/6/1/2/5/4/10 | 28/14 |
| bruch.dezimal | 8 | 24 | 8/4/2/2/2/3/3 | 16/8 |
| bruch.rechnen | 12 | 36 | 12/3/2/3/4/2/10 | 24/12 |
| bruch.prozent | 6 | 18 | 6/2/1/2/2/2/3 | 12/6 |
| terme.aufstellen | 6 | 18 | 6/2/1/2/2/3/2 | 12/6 |
| messen.flaechen_vielecke | 8 | 24 | 8/2/0/3/5/2/4 | 16/8 |
| messen.volumen | 7 | 21 | 7/2/0/3/4/2/3 | 14/7 |
| messen.koerper_berechnung | 5 | 15 | 5/1/0/2/3/2/2 | 10/5 |
| Summe | 66 | 198 | 66/22/7/19/27/20/37 | 132/66 |

lw Lückenweg, fd Fehler-Detektiv, vw verfahren_waehlen, zw zwei_wege, um umkehren, br Brücke, an anwenden.
Stufen: jede der 66 Lernkarten hat Stufe 1 (Lückenweg, zählt nicht), mindestens eine zählende Aufgabe auf Stufe 2 und eine auf Stufe 3.

## Dateien
- `th_*.py`: Inhalt je Thema. `kern.py`: Helfer. `bauen.py`: Prüfung und Erzeugung der `<thema>.json`.
- Aufruf: `python3 -I inhalte/mathe-profi/rollend-6/bauen.py --voll` (`--ohne-c` listet Fehlbilder ohne Rechnung).

## Wie geprüft (gesichert)
- `bauen.py --voll` endet mit OK: drei Aufgaben je Lernkarte, Formgrenzen, Stufen je Lernkarte, kein Duplikat zum Bestand.
- Lösungen zweifach mit exaktem Bruchrechnen nachgerechnet (337); Fehlbilder mit Rechnung c nachgerechnet (395).
- Lückenwege: Abhängigkeit der Lücken nachgewiesen (66), kein Lückenwert als Ziffer oder Zahlwort in Text, Schablone, Hinweis, Tipp.
- Fehler-Detektiv: Zeilen davor richtig, Fehlerzeile falsch, Folgezeilen folgerichtig. Fehlerzeile je Zeile {1: 6, 2: 5, 3: 5, 4: 6}.
- Auswahl: genau eine richtige Antwort, keine gleichen Werte (mit Einheit).
- `inhalt_pruefen` je Thema: Code 0. `vorrat_pruefen` (Hülle auf rollend-6): 79 Meldungen, alle von Hand angesehen und als Fehlalarm bewertet (Heuristik zur Lücken-Abhängigkeit, Textparsing von Fehlbildern, V030 und V099 sind Denk- bzw. Folgefehler-Zeilen, kein Fehler).

## Annahmen und offene Punkte (nicht gesichert)
- Die Schlussdurchsicht nach Checkliste B habe ich von Hand nur für bruch.brueche und bruch.dezimal vollständig gelesen. Die übrigen sechs Themen sind nur maschinell geprüft. Dort bitte Stichproben lesen.
- V023 und V035 sind eher schwache Brücken (Darstellungswechsel nur dünn).
- g und Stufe richten sich nach dem Standard der Form (lueckenweg direkt, fehler_detektiv fehler, zw/vw mehrschritt, um umkehr oder rueckwaerts, br darstellung, an einkleidung oder transfer).
- Keine Lernkarte zurückgestellt.

## Fehlbilder ohne Rechnung (c = null)
Insgesamt 99, alles Wahl- oder Begründungsfehler ohne Zahlenrechnung:
- Fehler-Detektiv: die Antworten „In Zeile n“ (falsche Zeile) in allen 22 Fehler-Detektiv-Aufgaben.
- Auswahl mit Aussagen als Antworten (z. B. V041, V047, V065): falsche Denkweisen als Text.
- Einzelne Lücken- oder Zahlfehlbilder ohne eindeutige Rechnung, z. B. „nur einen Teiler genommen, nicht den größten“ (V055, V004, V034, V043).
- Weitere Aufgaben mit solchen Fehlbildern: V076, V077, V095, V098, V103, V113, V122, V128, V134, V137, V143, V170, V197.
