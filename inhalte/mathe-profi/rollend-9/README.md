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

## Fehlbilder ohne Rechnung (129 von 524)
Es sind Antworten bei Auswahlaufgaben (Begründungen, Mengenschreibweisen, Aussagen über Gerätewahl) und die Zeilen im Fehler-Detektiv. Dort gibt es keine Zahl, die nachgerechnet werden kann (Feld `c` = null). Bei Zahlaufgaben haben alle Fehlbilder eine Rechnung. (Die Zählung „117“ der Ausgabe von `bauen.py` zählt nur Auswahlantworten ohne Funktion und ist nicht die Zahl der Fehlbilder mit `c` = null.)

## Lernkarten, in denen eine Form schlecht passt
- stochastik.verknuepft / elemente und mengen_verstehen: „Zwei Wege“ und „Anwenden“ passen kaum zu reinen Mengenfragen; dort stehen Verfahren wählen, Umkehren und Fehler-Detektiv.
- zahlen.wurzeln_basis / wurzel_deuten und reell / zahlarten, irrational_beweis: statt Anwenden stehen Verfahren wählen, Umkehren und Fehler-Detektiv.
- Verfahren wählen steht nur auf erkennenden Lernkarten (Stufe 1).

## Vorprüfung durch zweiten Helfer
Alle 174 Aufgaben (58 Lernkarten) wurden vollständig gelesen und von Hand nachgerechnet: Frage, alle Antworten, Schablone, Tipp, Lösungsweg und jedes Fehlbild, darunter die 129 Fehlbilder ohne Rechnung (Auswahl-Antworten und Detektiv-Zeilen). Dabei besonders geprüft: Definitionsmengen und Scheinlösungen (Probe in der Ausgangsgleichung), beide Lösungen bzw. ausdrückliche Auswahl, Diskriminante und Lösungszahl, Scheitel gegen Extremwert, Rundung gegen exakten Wert, gleich wahrscheinliche Ergebnisse, mit/ohne Zurücklegen, Richtung der bedingten Wahrscheinlichkeit, stimmige Vierfeldertafeln, Eindeutigkeit der Zufallsgeräte.
Ergebnis: Alle Lösungen, Fehlbild-Werte, Tafeln, Diagramme und Detektiv-Ketten stimmen. Gefunden und berichtigt wurden 11 Aufgaben (Kennungen unverändert, nur Wortlaut), je Muster:
- Lösung im Fragetext (1): K9A-V038 (Zwei Wege, Weg B nannte schon den Faktor a = 5).
- Fehlende Modellannahme (4): K9A-V120 („fairen“ Würfel ergänzt); „zufällig“ ergänzt in K9A-V132, K9A-V156 und K9A-V174 (Ziehung bzw. Urne ausdrücklich zufällig).
- Auswahl, zweite Antwort scheinbar richtig oder Grenzen mehrdeutig (2): K9A-V116 (letzte Antwort „kein Laplace-Experiment, weil drei Säulen gleich hoch sind“ hatte ein richtiges Ergebnis mit falscher Begründung, jetzt eindeutig falsch), K9A-V139 („zwischen 8 und 13“ jetzt „mindestens 8 und höchstens 13“).
- Tipp zu nah an der Lösung (1): K9A-V032 (nannte den Rechenschritt √36 = 6).
- Fehlbild-Beschreibung missverständlich oder zur Rechnung unpassend (2): K9A-V023, K9A-V123.
- Formulierung (1): K9A-V027 („auf zwei Nachkommastellen gerundet auf zwei Wege“).
Prüfwerkzeug: `tools/vorrat_pruefen.py` meldet auf der Runde genau eine Stelle (K9A-V054, Prüfung iv). Das ist ein Fehlalarm: Zeile 3 enthält nur richtig gerechnete Gleichungen, die falsche Folgerung („Also lösen beide Zahlen die Ausgangsgleichung“) steht aber in dieser Zeile. Sie ist in `bauen.py` als RESTMELDUNGEN einzeln begründet ausgenommen; jede andere Meldung lässt den Bau scheitern.
Fraglich / offen (nicht berichtigt):
- K9A-V167 (Zwei Wege, Simulation auswerten): war „relative Häufigkeit“ gegen „Dreisatz“ (fast dasselbe Verfahren); jetzt Weg B über die unpünktlichen Durchgänge und das Gegenereignis (siehe Nach Gegenprüfung).
- K9A-V053 (Zwei Wege, Wurzelgleichung): beide Wege quadrieren; sie unterscheiden sich nur darin, wann die Bedingung „rechte Seite nicht negativ“ geprüft wird.
- K9A-V165 (Umkehren, Simulation): die 6 ist eine Punktschätzung aus 30 von 50; 5 oder 7 wären zufällig auch möglich. Die Frage verlangt jetzt ausdrücklich die Schätzung anhand der beobachteten relativen Häufigkeit.
- K9A-V041 (Umkehren, Beweis): der Schluss ergab sich fast unmittelbar aus der genannten Gleichung p² = 3q²; der Beweisschluss ist jetzt in Worten umschrieben („p² ist das Dreifache von q²“), bleibt aber eine leichte Aufgabe.
- K9A-V065 (Zwei Wege, x² = 6x): die Frage nach der bloßen Anzahl 2 war leicht zu erraten; jetzt wird n + g (Anzahl und größte Lösung) verlangt.
Hinweis: die Aufgabenanzahl je Muster oben ist gezählt aus der Durchsicht, nicht maschinell.

## Nach Gegenprüfung (Werkstatt 1096)
Die äußere Gegenprüfung ergab „Muss vorher“ (44 von 174 mit Muss-Befund). Alles wurde in den Quellen `th_*.py` geändert und neu gebaut; Kennungen und Anzahl (174), Formen- und Stufenverteilung blieben unverändert. Von der Arbeitsliste sind alle Muss- und Auflagepunkte umgesetzt, die Lösungen jeweils nachgerechnet.
Berichtigt nach Muster:
- Fehlbild-Kennung `fb.vorzeichen.falsches_zeichen` geleert (gilt nur für Mal/Geteilt): K9A-V007, V043, V047, V056, V068, V076 (Lücke ③), V085, V091, V097, V106, V108; `fb.hoch_zurueck.wurzel_halbiert` bei V033 geleert (dort ist 900 = a², nicht eine halbierte Wurzel). Behalten bleibt falsches_zeichen nur bei echten Vorzeichenfehlern in Produkten: V073, V076 (Lücke ①), V099.
- `id.daten.teil_ganzes` (meint den Stichprobenschluss) ersetzt oder geleert bei V124 bis V132 und V136 bis V141 (V124, V126: `id.zahlen.bausteine`); bei V121 und V123 sowie in Simulation auswerten und Monte-Carlo (V165 bis V171) passt sie und steht jetzt dort. `id.daten.anteil` geleert, wo nur gezählt wird oder keine gleich wahrscheinliche Wahl vorliegt (V122, V134, V135, V142 bis V144, V146, V154, V155); V149, V151 bis V153, V156: `id.daten.stufen`.
- Fehlbild-Beschreibung nennt genau die gerechnete Rechnung: V009, V022, V023, V033, V085, V086, V096, V103, V160, V113 u. a.
- Fehler-Detektiv: Rückmeldung zu jeder wählbaren Zeile; für sich richtige Zeilen nach dem Fehler (V015, V030, V087, V150, V168) tragen „Diese Zeile ist richtig, weil …“. `kern.FD` verlangt das jetzt (`rueck=`).
- Stochastik: Voraussetzungen ausdrücklich (fair, gleich wahrscheinlich, unabhängig, gleichverteilt), u. a. V112 bis V114, V117, V118 bis V123, V145 bis V147, V155 bis V156, V160 bis V162, V169 bis V172, V174. „Verfahren wählen“ V124, V139, V154: Optionen sind jetzt Vorgehensweisen.
- Inhaltliche Berichtigungen: V022 (fragt jetzt die Grenzen 94 und 95 als ganze Zehntel ab), V040 (Widerspruchsbeweis mit vollständig gekürztem Bruch), V041/V042, V065, V070 („Zuerst x² + 6x = 7“), V085 (Tipp führte zu −4; jetzt −b : (2a)), V087 (Zeile 3 differenziert), V142 (Summe der drei Innenfelder), V148 (Schnitt 9 wird ermittelt und für beide bedingten Anteile verwendet), V141, V160, V167.
- Stufe-3-Tipps (Fehler-Detektiv und Umkehren/Anwenden) sind nur noch Anstöße und verraten weder Fehlerzeile noch Probe; die Eingabefrage steht am Textende.
Neue Prüfung in `bauen.py`: jede Regel-Kennung muss in der Themenliste des Katalogs (`kennungen.json`) stehen oder in `REGEL_AUSNAHME` (von Hand gelesen, mit Begründung); jede Fehlbild-Kennung muss in der von Hand gelesenen Liste `FB_GELESEN` stehen. 24 Aufgaben tragen keine Regel-Kennung (der Katalog hat nichts, was genau passt).
Fraglich / nicht sicher beurteilt: (1) `fb.hoch_zurueck.wurzel_halbiert` bei der dritten Wurzel (V008, „halbiert“ statt ∛) ist als dieselbe Fehlvorstellung (Wurzel = Hälfte) belassen, der Katalogtext nennt nur √16 = 8; (2) die Ausnahmen in `REGEL_AUSNAHME` (Themenliste nennt das Thema nicht, der Text der Idee passt aber); (3) V148 und V150 behalten `id.daten.anteil` (günstige durch mögliche Personen in Gruppen), ohne ausdrücklich „zufällig gewählt“.
