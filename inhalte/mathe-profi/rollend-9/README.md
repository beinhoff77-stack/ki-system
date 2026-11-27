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

## Vorprüfung durch zweiten Helfer
Alle 174 Aufgaben (58 Lernkarten) wurden vollständig gelesen und von Hand nachgerechnet: Frage, alle Antworten, Schablone, Tipp, Lösungsweg und jedes Fehlbild, darunter die 117 Fehlbilder ohne Rechnung (Auswahl-Antworten und Detektiv-Zeilen). Dabei besonders geprüft: Definitionsmengen und Scheinlösungen (Probe in der Ausgangsgleichung), beide Lösungen bzw. ausdrückliche Auswahl, Diskriminante und Lösungszahl, Scheitel gegen Extremwert, Rundung gegen exakten Wert, gleich wahrscheinliche Ergebnisse, mit/ohne Zurücklegen, Richtung der bedingten Wahrscheinlichkeit, stimmige Vierfeldertafeln, Eindeutigkeit der Zufallsgeräte.
Ergebnis: Alle Lösungen, Fehlbild-Werte, Tafeln, Diagramme und Detektiv-Ketten stimmen. Gefunden und berichtigt wurden 11 Aufgaben (Kennungen unverändert, nur Wortlaut), je Muster:
- Lösung im Fragetext (1): K9A-V038 (Zwei Wege, Weg B nannte schon den Faktor a = 5).
- Fehlende Modellannahme (4): K9A-V120 („fairen“ Würfel ergänzt); „zufällig“ ergänzt in K9A-V132, K9A-V156 und K9A-V174 (Ziehung bzw. Urne ausdrücklich zufällig).
- Auswahl, zweite Antwort scheinbar richtig oder Grenzen mehrdeutig (2): K9A-V116 (letzte Antwort „kein Laplace-Experiment, weil drei Säulen gleich hoch sind“ hatte ein richtiges Ergebnis mit falscher Begründung, jetzt eindeutig falsch), K9A-V139 („zwischen 8 und 13“ jetzt „mindestens 8 und höchstens 13“).
- Tipp zu nah an der Lösung (1): K9A-V032 (nannte den Rechenschritt √36 = 6).
- Fehlbild-Beschreibung missverständlich oder zur Rechnung unpassend (2): K9A-V023, K9A-V123.
- Formulierung (1): K9A-V027 („auf zwei Nachkommastellen gerundet auf zwei Wege“).
Prüfwerkzeug: `tools/vorrat_pruefen.py` meldet auf der Runde genau eine Stelle (K9A-V054, Prüfung iv). Das ist ein Fehlalarm: Zeile 3 enthält nur richtig gerechnete Gleichungen, die falsche Folgerung („Also lösen beide Zahlen die Ausgangsgleichung“) steht aber in dieser Zeile. Sie ist in `bauen.py` als RESTMELDUNGEN einzeln begründet ausgenommen; jede andere Meldung lässt den Bau scheitern.
Fraglich / offen (nicht berichtigt):
- K9A-V135 (Zwei Wege, Simulation auswerten): „relative Häufigkeit mal 200“ und „Dreisatz“ sind rechnerisch fast dasselbe Verfahren; als zwei Wege vertretbar, aber schwach.
- K9A-V053 (Zwei Wege, Wurzelgleichung): beide Wege quadrieren; sie unterscheiden sich nur darin, wann die Bedingung „rechte Seite nicht negativ“ geprüft wird.
- K9A-V133 (Umkehren, Simulation): „vermutlich 6 Ziffern“ ist eine Schätzung aus 30 von 50; 5 oder 7 wären zufällig auch möglich, „vermutlich“ steht im Text.
- K9A-V042 (Umkehren, Beweis): der Schluss ergibt sich fast unmittelbar aus der genannten Gleichung p² = 3q².
- K9A-V065 (Anzahl der Lösungen = 2): die Antwort ist leicht zu erraten; Fehlbilder 1 und 3 stehen dagegen.
Hinweis: die Aufgabenanzahl je Muster oben ist gezählt aus der Durchsicht, nicht maschinell.
