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
- Lösungen zweifach mit exaktem Bruchrechnen nachgerechnet (365); Fehlbilder mit Rechnung c nachgerechnet (431), exakt, ohne gerundete Fehlwerte.
- Lückenwege: Abhängigkeit der Lücken nachgewiesen (66), kein Lückenwert als Ziffer oder Zahlwort in Text, Schablone, Hinweis, Tipp.
- Fehler-Detektiv: Zeilen davor richtig, Fehlerzeile falsch, Folgezeilen folgerichtig. Fehlerzeile je Zeile {1: 6, 2: 5, 3: 5, 4: 6}.
- Auswahl: genau eine richtige Antwort, keine gleichen Werte (mit Einheit).
- `inhalt_pruefen` je Thema: Code 0. `vorrat_pruefen` (Hülle auf rollend-6): 79 Meldungen, alle von Hand angesehen und als Fehlalarm bewertet (Heuristik zur Lücken-Abhängigkeit, Textparsing von Fehlbildern, V030 und V099 sind Denk- bzw. Folgefehler-Zeilen, kein Fehler).

## Annahmen und offene Punkte (nicht gesichert)
- Die Schlussdurchsicht nach Checkliste B ist inzwischen für alle acht Themen von einem zweiten Helfer von Hand erfolgt (siehe unten).
- g und Stufe richten sich nach dem Standard der Form (lueckenweg direkt, fehler_detektiv fehler, zw/vw mehrschritt, um umkehr oder rueckwaerts, br darstellung, an einkleidung oder transfer).
- Keine Lernkarte zurückgestellt.

## Fehlbilder ohne Rechnung (c = null)
Insgesamt 98, alles Wahl- oder Begründungsfehler ohne Zahlenrechnung:
- Fehler-Detektiv: die Antworten „In Zeile n“ (falsche Zeile) in allen 22 Fehler-Detektiv-Aufgaben.
- Auswahl mit Aussagen als Antworten (z. B. V041, V047, V065): falsche Denkweisen als Text.
- Einzelne Lücken- oder Zahlfehlbilder ohne eindeutige Rechnung, z. B. „nur einen Teiler genommen, nicht den größten“ (V055, V004, V034, V043).
- Weitere Aufgaben mit solchen Fehlbildern: V076, V077, V095, V098, V103, V113, V122, V128, V134, V137, V143, V170, V197.

## Vorprüfung durch zweiten Helfer
Alle 198 Aufgaben (Frage, Antworten, Schablone, Tipp, Lösungsweg, jedes Fehlbild) von Hand gelesen und nachgerechnet. 55 Aufgaben geändert (Kennungen stabil, nur Inhalt), die übrigen 143 ohne Befund.
- Fehlbild passt nicht zur Beschreibung oder ist unrealistisch (gerundeter oder nicht ganzzahliger Fehlwert bei Lücken, die ganze Zahlen verlangen): V003, V043, V047, V068, V080, V083, V091, V104, V112, V119, V141, V145, V148, V172, V182, V190, V195 (17). `bauen.py` verlangt jetzt exakte Fehlwerte und ganze Zahlen bei Lücken.
- Gerüste: Der letzte Lückenwert war aus der Schablone rückrechenbar (V016, V019). Außerdem hatten 28 Lückenwege nur eine abhängige Lücke; sie haben jetzt mindestens zwei (V001, V007, V010, V016, V019, V022, V025, V037, V043, V046, V052, V058, V061, V082, V088, V097, V100, V127, V130, V148, V151, V154, V160, V178, V181, V187, V190, V196). `bauen.py` prüft: ab drei Lücken mindestens zwei abhängige. Offen: In 25 Lückenwegen sind die ersten beiden Lücken unabhängig voneinander (Teil A, Teil B, dann Verknüpfung); das ist fachlich so gewollt (zwei Teilrechnungen), „jede spätere Lücke hängt von einer früheren ab“ gilt dort nicht streng.
- Eindeutigkeit und Einkleidung: V011 (Antwort stand als Nenner im Text), V048 (Weitsprung mit Millimetern unplausibel), V063 (Folgezeilen bei 9/20 nicht folgerichtig, jetzt 7/20), V089, V123, V136, V137, V138 (Ausleihen statt Kauf).
- Brücken: V017 (Text gab den Wechsel schon vor), V023 und V035 neu gefasst; V023 Verhältnis zu Bruchteil mit Kürzen, V035 Zahlenstrahl-Abschnitte zu Dezimalzahl über gemischte Zahl.
- Tipp verriet Zwischenergebnis oder Lösungsidee: V161, V194.
- Alle 21 Restmeldungen von `tools/vorrat_pruefen.py` (über Hülle auf rollend-6) und die 4 Fehler-Detektiv-Hinweise einzeln geprüft: alles Fehlalarme (Brüche und Einheiten im Text falsch gelesen, ganzzahliger Quotient, Rechnung steht nur in der Beschreibung); V030, V099, V198 sind richtig (Zeile spricht die falsche Behauptung aus bzw. Kettenrechnung mit Einheit).
- Fehlbilder ohne Rechnung von Hand nachgerechnet: alle „In Zeile n“-Antworten, die Aussagen-Antworten (V041, V047, V065, V077, V095, V098, V113, V122, V128, V134, V137, V143, V170, V197; bei den meisten rechnet die Probe-Funktion die Aussage mit) und die „nur ein Teiler, nicht der größte“-Lücken (V004, V034, V055, V076, V103) sind richtig; eine Rechnung lässt sich dafür nicht sinnvoll hinterlegen.
- Fraglich, nicht geändert: Die sieben „Verfahren wählen“ (V041, V047, V065, V077, V098, V113, V122) tragen g = mehrschritt (Stufe 2). Sie sind reine Methodenwahl (eher „erkennen“), `erkennen` gehört aber zu Stufe 1 und würde die Stufenregel (zählende Aufgabe auf Stufe 2) brechen; Entscheidung beim Projektleiter. V088 (Potenz eines Bruchs) und V126, V135 (Gleichung durch Umkehren in terme.aufstellen) liegen am oberen Rand von Klasse 6.
