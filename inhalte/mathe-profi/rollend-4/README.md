# rollend-4: Vorrat an neuen Formen

Ziel: Jede Lernkarte der 16 Flüge aus rollend-1 bis rollend-3 hat mindestens drei Aufgaben in neuer Form (Lückenweg, Fehler-Detektiv, Verfahren wählen, Zwei Wege vergleichen, Brücke) mit den alten Antwortformen (zahl, auswahl, luecken; keine `bedingung`). "Umkehren" und "Anwenden" zählen nicht.

Neu bauen und prüfen: `python3 -I inhalte/mathe-profi/rollend-4/bauen.py` (muss mit "OK" enden). **Seit dem Nachtrag 27.11. (Mischung) gilt das nicht mehr:** Die Dateien `<flug>.json` sind von Hand geändert und maßgeblich; `bauen.py` bricht deshalb ohne `--ueberschreiben` ab. Prüfen geht über den Abschnitt „Prüfen“ im Nachtrag. Kennungen je Flug fortlaufend mit V, z. B. `A1-V01`.

## Bedarf und Stand

```
Flug      Lernkarten  vorher≥3  Fehlbedarf  neu  jetzt≥3  Rest
ge1               13         0          32   32       13     0
z2                 7         0          14   14        7     0
ge2               12         0          28   28       12     0
a4                11         0          26   26       11     0
a1                 5         1           5    5        5     0
d1                 6         0           9    9        6     0
g1                 8         0          15   15        8     0
g8                 8         0          13   13        8     0
g2-teil2           3         3           0    0        3     0
f1                 9         0          17   17        9     0
ge3                7         0          12   12        7     0
r1                 7         0          10   10        7     0
g2                 5         1           5    5        5     0
ge4               16         0          37   37       16     0
f2                11         0          21   21       11     0
a6                 9         0          17   17        9     0
Summe      137 5 261 261 137 0
```

Gesamt: 261 neue Aufgaben (137 Lernkarten; 6 davon die beiden „verstehen“-Karten von ge1, siehe Nachtrag).

Nach Form und Stufe (Stand 27.11. nach Mischung, 314 Aufgaben in rollend-4): Lückenweg 93, alle Stufe 1, zählt nein; Fehler-Detektiv 95, alle Stufe 3; Verfahren wählen 63 (Stufe 2: 59, Stufe 1: 2, Stufe 3: 2); Zwei Wege vergleichen 22 (Stufe 2: 21, Stufe 1: 1); Umkehren 22 (Stufe 2: 17, Stufe 3: 5); Brücke 19 (Stufe 2: 13, Stufe 1: 4, Stufe 3: 2). Die frühere Angabe zur Stufe der Fehler-Detektive und zur Zahl der Zwei-Wege-Aufgaben galt nur für den ersten Stand.

## Zurückgestellt

Nichts mehr (die beiden ge1-Karten „verstehen“ sind seit dem Nachtrag 27.11. gebaut).

## Geprüft

- Jede Lösung wird vom Programm berechnet und auf zwei Wegen nachgerechnet.
- Lückenweg: ganze Zahl je Lücke, gesuchte Zahl steht nicht im Text, kein Komma neben einer Lücke.
- Auswahl: genau eine richtige Antwort, die falschen sind nachweislich falsch, die richtige Position wechselt.
- Fehler-Detektiv: genau eine fehlerhafte Zeile.
- Keine Dopplung zum Bestand (rollend-1 bis 3, Themen-Dateien).
- Kopien der Themen-Dateien mit den neuen Aufgaben: `tools/inhalt_pruefen.py` ohne Fehler.

## Nicht geprüft

- `tools/rollend_sql.py`: Die Flüge von rollend-3 (a6, f2, g2, ge3, r1, ge4) haben noch keinen Eintrag in `plan/rollend-einheiten.json`; deshalb meldet das Werkzeug dort "ohne Zuordnung". Das ist erwartet und wird mit der Planung behoben.
- Keine Prüfung in der App und keine Prüfung durch Kinder. Kein Flug hat eine Zeichnung.

## Nachtrag 27.11.2026: ge1 „verstehen“, Mischung der Formen

### Zuordnung ge1 „verstehen“ (6 Aufgaben)
Die Lernkarte `verstehen` gibt es in `geometrie.grundbegriffe` (Einheit 47) und `geometrie.ortslinien` (Einheit 48). Lösung: Jeder Eintrag hat schon das Feld `thema`. `tools/rollend_sql.py` wertet es jetzt aus, **aber nur**, wenn das Lernziel zu mehr als einer Einheit des Flugs passt. Sonst bleibt alles wie vorher (bei den anderen Flügen nennt `thema` die Themen-Datei, nicht die Einheit; dort darf es nicht entscheiden). Keine neue Spalte, keine Änderung an der Datenbank.

Neu in `ge1.json` (alle `zaehlt = ja`, kein Lückenweg):

| Kennung | Thema | Form | Stufe | Antwort |
|---|---|---|---|---|
| GE1-V27 | ortslinien | Verfahren wählen | 2 | auswahl |
| GE1-V28 | ortslinien | Umkehren | 2 | zahl (r = 18 : 2 = 9) |
| GE1-V29 | ortslinien | Brücke | 2 | auswahl |
| GE1-V30 | grundbegriffe | Umkehren | 2 | auswahl |
| GE1-V31 | grundbegriffe | Zwei Wege vergleichen | 2 | zahl ((24 − 8 − 8) : 2 = 4 und 24 : 2 − 8 = 4) |
| GE1-V32 | grundbegriffe | Fehler-Detektiv | 3 | auswahl |

### Mischung: Lernkarten über rollend-1 bis rollend-4
137 Lernkarten. **Keine** Lernkarte hat nur Aufgaben mit `zaehlt = nein` und **keine** hat nur eine einzige Form (jede hat mindestens Lückenweg plus Fehler-Detektiv oder Verfahren wählen). Weil das Ziel die Mischung der **zählenden** Aufgaben ist, habe ich die Regel enger gelesen: Lernkarten, deren zählende Aufgaben (`zaehlt = ja`) nur **eine** Form haben. Das sind 5. Je Karte eine Aufgabe in `rollend-4` neu geschrieben (gleiche Kennung, `zaehlt = ja`, nachgerechnet):

| Kennung | Lernkarte | vorher | jetzt |
|---|---|---|---|
| GE2-V26 | abbildungen.kongruenz / eigenschaften | Fehler-Detektiv, Stufe 3 | Umkehren, Stufe 3 (Umfang des Originals aus dem Bild) |
| GE2-V25 | abbildungen.kongruenz / symmetrie | Fehler-Detektiv, Stufe 3 | Zwei Wege, Stufe 2 (Achsen des Sechsecks) |
| A4-V24 | zahlen.intervalle / lesen | Fehler-Detektiv, Stufe 3 | Brücke, Stufe 2 (Ungleichung zu Intervall) |
| R1-V07 | messen.flaechen / einheitsquadrate | Fehler-Detektiv, Stufe 3 | Umkehren, Stufe 2 (Reihen aus 42 Quadraten) |
| R1-V02 | messen.flaechen / kommaschreibweise | Lückenweg (zählt nein), Stufe 1 | Zwei Wege, Stufe 2 (4,25 m² in dm²) |

Folgen: Bei vier Karten fehlt jetzt in `rollend-4` die Stufe-3-Aufgabe (bei GE2-V25, A4-V24, R1-V07 wurde Stufe 2 daraus); bei `kommaschreibweise` entfällt der Lückenweg für Stufe 1. Der Takt zieht dann eine normale Aufgabe (Regel 2 in `form-takt.md`).

**Liste erledigt:** Für alle 53 Lernkarten, die noch keine zählende Aufgabe der Formen Umkehren, Zwei Wege oder Brücke hatten, ist je eine neue Aufgabe in `rollend-4` ergänzt (`zaehlt = ja`, Kennung fortlaufend, Rechenaufgaben mit Feld `c` nachgerechnet, Fragetext neu). Form: Umkehren 18, Zwei Wege 18, Brücke 17. Stufe nach dem Bestand der Karte: Stufe 1 bei den Karten, die dort nur Stufe 1 haben (eindeutig, verstehen in geometrie.winkel, ohne_loesung, sach) und bei erkennen (kein Bestand in rollend-4), Stufe 3 bei den Karten mit nur Stufe 3 (faktor, stelle, ergaenzen, einheiten in messen.flaechen) sowie bei satz_kehrsatz und beweisen, sonst Stufe 2. Die Karte `erkennen` in groessen.proportional gehört zum Flug g2-teil2; dafür gibt es die neue Datei `g2-teil2.json` (Kennung G2T2-V01). Alle anderen Aufgaben stehen in der Datei ihres Flugs.

### Prüfen (27.11.)
- `python3 -I tools/rollend_sql.py --mit-bedingung`: ohne OFFEN und ohne Fehler; **580 Aufgaben** für 22 Einheiten (rollend-1 bis -4). Form: Lückenweg 126, Fehler-Detektiv 141, Verfahren wählen 91, Umkehren 61, Zwei Wege 21, Brücke 29, Anwenden 31, Viele Antworten 80. `zaehlt`: ja 454, nein 126, folge 0. `--sql` läuft durch (rund 390 KB).
- `rollend-4` allein: 261 Aufgaben; Lückenweg 93 (alle nein), Fehler-Detektiv 95, Verfahren wählen 63, Zwei Wege 4, Umkehren 4, Brücke 2. `zaehlt`: ja 168, nein 93.
- `inhalt_pruefen.py`: alle Aufgaben aus `rollend-4` an Kopien ihrer Themen-Dateien gehängt (18 Dateien): Code 0 bei allen.
- Jede der 11 neuen oder umgewandelten Rechenaufgaben: Feld `c` nachgerechnet und mit der Lösung verglichen; die falschen Antworten sind von der Lösung verschieden.


### Nachtrag Durchsicht nach Gegenprüfung (Werkstatt 1033/1034, Werkstatt 1036)
Die Aufgaben von rollend-1 bis rollend-4 wurden nach der Gegenprüfung (Werkstatt 1033/1034 und für rollend-3 Werkstatt 1036) durchgesehen und berichtigt: Pflichtpunkte und Kann-Punkte mit Neurechnung, bei jeder geänderten Aufgabe passen Frage, Antworten, Hinweis und Lösungsweg zusammen. Die JSON-Dateien bleiben maßgeblich.

**Fehler-Detektive (rollend-1 bis -4, 95 Zeilenaufgaben).** Wo nach dem Fehler nur noch Folgefehler kamen, lautet die Frage jetzt „In welcher Zeile passiert der erste Fehler?“. 33 Aufgaben wurden umgeschrieben. Fehlerzeile vorher/nachher:

| Fehlerzeile | vorher | nachher |
|---|---|---|
| Zeile 1 | 6 | 31 |
| Zeile 2 | 23 | 31 |
| Zeile 3 | 66 | 33 |

Größter Anteil einer Zeile: vorher 69,5 %, nachher 34,7 % (eine Aufgabe hat vier Zeilen).

**Gerüst-Aufgaben (Lückenweg), 130 Aufgaben in rollend-1 bis -4 und fachwoerter.** Regeln: Antwortform `luecken`, mindestens zwei Lücken an verschiedenen Schritten, eine davon an der entscheidenden Stelle, kein Lückenwert im Text, in der Schablone oder im Hinweis, spätere Lücken hängen von früheren ab, der Text nennt kein Zwischenergebnis, `zaehlt = nein` bleibt. 81 Aufgaben wurden neu gebaut, die Fehlbilder gelten je Lücke. Zurückgestellt: GE2-V03 (kein sauberer Entwurf gefunden).

| Lücken je Aufgabe | 1 | 2 | 3 | 4 | 5 | Mittel |
|---|---|---|---|---|---|---|
| vorher | 5 | 74 | 38 | 11 | 2 | 2,47 |
| nachher | 0 | 37 | 72 | 20 | 1 | 2,88 |

Antwortform vorher und nachher: `luecken` 130, `auswahl` 0 (Auswahl-Lückenwege fanden sich im Bestand nicht).

**Prüfen (27.11., nach der Mischung).** `python3 -I tools/rollend_sql.py --mit-bedingung`: ohne OFFEN und ohne Fehler; 633 Aufgaben (rollend-1 bis -4). Form: Lückenweg 126, Fehler-Detektiv 141, Verfahren wählen 91, Umkehren 79, Zwei Wege 39, Brücke 46, Anwenden 31, Viele Antworten 80. `zaehlt`: ja 507, nein 126. `rollend-4` allein: 314 Aufgaben (Lückenweg 93, Fehler-Detektiv 95, Verfahren wählen 63, Zwei Wege 22, Umkehren 22, Brücke 19); `zaehlt`: ja 221, nein 93. Alle Aufgaben aus `rollend-4` an Kopien der Themen-Dateien gehängt (18 Dateien): `tools/inhalt_pruefen.py` Code 0 bei allen. Die Zahlen im Abschnitt „Prüfen (27.11.)“ oben gelten für den Stand vor dieser Durchsicht.


## Zweite Nachprüfung (nach Gegenprüfung, Werkstatt 1050/1051/1052)

Stand: 633 Aufgaben (rollend-1 bis -4, `zaehlt` ja 507, nein 126), `tools/rollend_sql.py --mit-bedingung` ohne OFFEN und ohne Fehler, `tools/inhalt_pruefen.py` an allen Themenkopien Code 0 (Fehler: 0).

Geändert: alle Punkte der Gegenprüfung (Lückenwerte im Text oder Tipp, Gerüste ohne abhängige Kette, Fehlbild-Beschreibungen ohne passende Rechnung, Brücken ohne echten Darstellungswechsel, Fehler-Detektive) wurden neu gerechnet; Frage, Tipp, Lösungsweg und Fehlbilder wurden jeweils zusammen angepasst. Bei der Durchsicht aller Lückenwege (126) und aller Fehlbild-Beschreibungen mit Zahlenantwort kamen weitere Fälle hinzu (Gerüste mit unabhängiger Schlusslücke, Tipps mit Lückenwert, Beschreibungen mit falscher Rechnung, fehlende Fehlbilder für einzelne Lücken); sie sind berichtigt.

Neues Prüfskript `tools/vorrat_pruefen.py` (nur Standardbibliothek, `python3 -I tools/vorrat_pruefen.py`, optional `--kennung K…`). Es prüft (i) Lückenwerte als Ziffer oder Zahlwort in Text, Schablone und Tipp, (ii) Lückenwege ohne abhängige spätere Lücke oder mit unabhängiger Schlusslücke, (iii) Fehlbild-Beschreibungen mit Rechnung gegen die gespeicherte Antwort, (iv) Fehler-Detektive mit falscher Rechnung vor der Fehlerzeile oder rechnerisch richtiger Fehlerzeile. Nicht abgedeckt: Beschreibungen nur in Worten (verdoppelt, abgerundet, „erst …, dann …“), Rechnungen mit Variablen, Denkfehler, Abhängigkeit über den Satzbau (Heuristik).

Meldungen nach der zweiten Nachprüfung (Stand dieses Abschnitts überholt durch die dritte Nachprüfung unten): Die pauschale Aussage „keine echten Fälle“ war falsch; siehe unten.

## Dritte Nachprüfung (nach Gegenprüfung, Werkstatt 1070)

Geändert: Fehler-Detektive GE1-V26 und GE1-V17 (die Schlüsselzeile spricht jetzt die falsche Behauptung selbst aus), Lückenwege Z2-V02 (erste Lücke verlangt jetzt einen echten Schritt: Teilen durch 10 statt Abschreiben der Endziffer), Z2-V03 und Z2-02 (die letzten Lücken hängen jetzt von der Quersumme ab; der Satz „Zahl minus Quersumme ist durch 9 bzw. 3 teilbar“ trägt die Folgefrage), Fehlbild-Beschreibungen F2-V01 und GE2-V04, Brücke A1-V06 (hypothetisch formuliert, keine Zeichnung nötig).

Prüfskript `tools/vorrat_pruefen.py` verbessert: (i) prüft jetzt auch die Schablone; Zahlwörter bis hundert; Hochzahlen wie (−2)² werden mitgelesen (damit ist die falsche Rechnung in F1-V12 sichtbar: (−2)² = −4; die frühere Erklärung „nur Denkfehler“ war für F1-V12 falsch, die Aufgabe selbst stimmt: die Fehlerzeile enthält die falsche Rechnung); (ii) Abhängigkeit wird am Rechenausdruck festgemacht (enthält der Ausdruck einer Lücke den Anker oder einen Wert einer früheren Lücke), nicht mehr am Anschlusswort; (iv) meldet Fehlerzeilen, die nur richtige Rechnungen enthalten, mit dem Hinweis, von Hand zu prüfen, ob genau diese Zeile die falsche Behauptung ausspricht.

Von Hand geprüft: alle 141 Fehler-Detektive (Schlüsselzeile gegen Folgezeile) und alle Lückenwege (erste Lücke als Abschreiben, letzte Lücke als unabhängige Nebenfrage). Zusätzlich gefunden und berichtigt: Z2-02 (gleiches Muster wie Z2-V03). Alle 14 Meldungen (iv) sind jetzt Fehlerzeilen, die die falsche Behauptung ausdrücklich enthalten (falscher Ansatz oder falsche Regel bei richtiger Rechnung): A6-V11, F1-V15, F2-V18, G1-V11, GE1-V17, GE1-V18, GE1-V26, GE2-V20, GE2-V21, GE3-V09, GE4-V23, GE4-V26, GE4-V30, R1-V10.

Verbleibende Meldungen und Einordnung: (ii) A6-V06, GE1-V02, GE1-V07, GE1-V08: Die letzte oder zweite Lücke ist ein Vergleichsschluss („Abstand 9 > Radius 6, also 0 Punkte“); ein falscher Wert vorne ändert den Schluss, der Rechenanker zeigt das nicht. (iii) A4-09, F2-18 (Rundung), A1-06, A1-13, A4-V02, F1-V03, F1-V06 („erst …, dann …“ mit mehreren Teilrechnungen), R1-V03 (zwei Rechnungen in einer Beschreibung): von Hand nachgerechnet, passen zur gespeicherten Antwort. Nicht abgedeckt bleiben Beschreibungen nur in Worten, Variablen und die Frage, ob eine Behauptung inhaltlich falsch ist.
