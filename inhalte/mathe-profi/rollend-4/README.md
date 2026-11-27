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

Nach Form und Stufe: Fehler-Detektiv Stufe 3: 98; Lückenweg Stufe 1: 94 (zählt nein); Verfahren wählen Stufe 2: 58, Stufe 1: 2, Stufe 3: 2; Zwei Wege vergleichen Stufe 2: 1.

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

**Liste statt Umbau:** 53 von 137 Lernkarten haben noch keine zählende Aufgabe der Formen Umkehren, Zwei Wege oder Brücke (sie haben aber mindestens zwei Formen). Nicht umgebaut, weil über die Regel hinaus: abbildungen.kongruenz (drehung, mittelsenkrechte, vektor_drehen, vektor_koordinaten, verschiebung, winkelhalbierende); bruch.prozent_grundwert (argumente, faktor, zurueck); funktionen.grundbegriffe (eindeutig, funktionswert, stelle); funktionen.linear (wirkung, zwei_punkte); geometrie.grundbegriffe (koordinaten, lagebeziehungen, vierecke, winkelarten); geometrie.konstruktion (kongruenzsatz, planfigur, satz_kehrsatz); geometrie.ortslinien (kreislinie, parallelen, sachsituationen, verknuepfen, zwei_kreise); geometrie.winkel (ergaenzen, verstehen); geometrie.winkelsaetze (beweisen, parkett, scheitel_neben); gleichungen.einfach (ohne_loesung); gleichungen.lgs2 (einsetzen, verfahren); gleichungen.ungleichungen (grafisch, intervall, klammern, pruefen, sachaufgabe, umdrehen, umformen); groessen.einheiten (schaetzen, verstehen); groessen.proportional (erkennen, sach); messen.flaechen (einheiten, sachaufgaben); zahlen.intervalle (beurteilen, enthalten, schreiben); zahlen.teilbarkeit (primzahl, teiler, vielfache).

### Prüfen (27.11.)
- `python3 -I tools/rollend_sql.py --mit-bedingung`: ohne OFFEN und ohne Fehler; **580 Aufgaben** für 22 Einheiten (rollend-1 bis -4). Form: Lückenweg 126, Fehler-Detektiv 141, Verfahren wählen 91, Umkehren 61, Zwei Wege 21, Brücke 29, Anwenden 31, Viele Antworten 80. `zaehlt`: ja 454, nein 126, folge 0. `--sql` läuft durch (rund 390 KB).
- `rollend-4` allein: 261 Aufgaben; Lückenweg 93 (alle nein), Fehler-Detektiv 95, Verfahren wählen 63, Zwei Wege 4, Umkehren 4, Brücke 2. `zaehlt`: ja 168, nein 93.
- `inhalt_pruefen.py`: alle Aufgaben aus `rollend-4` an Kopien ihrer Themen-Dateien gehängt (18 Dateien): Code 0 bei allen.
- Jede der 11 neuen oder umgewandelten Rechenaufgaben: Feld `c` nachgerechnet und mit der Lösung verglichen; die falschen Antworten sind von der Lösung verschieden.
