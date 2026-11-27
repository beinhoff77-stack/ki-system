# rollend-4: Vorrat an neuen Formen

Ziel: Jede Lernkarte der 16 Flüge aus rollend-1 bis rollend-3 hat mindestens drei Aufgaben in neuer Form (Lückenweg, Fehler-Detektiv, Verfahren wählen, Zwei Wege vergleichen, Brücke) mit den alten Antwortformen (zahl, auswahl, luecken; keine `bedingung`). "Umkehren" und "Anwenden" zählen nicht.

Neu bauen und prüfen: `python3 -I inhalte/mathe-profi/rollend-4/bauen.py` (muss mit "OK" enden). Kennungen je Flug fortlaufend mit V, z. B. `A1-V01`.

## Bedarf und Stand

```
Flug      Lernkarten  vorher≥3  Fehlbedarf  neu  jetzt≥3  Rest
ge1               11         0          26   26       11     0
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
Summe      135 5 255 255 135 0
```

Gesamt: 255 neue Aufgaben (135 Lernkarten hatten vorher nicht drei; Fehlbedarf 261 inklusive der zurückgestellten Karten).

Nach Form und Stufe: Fehler-Detektiv Stufe 3: 98; Lückenweg Stufe 1: 94 (zählt nein); Verfahren wählen Stufe 2: 58, Stufe 1: 2, Stufe 3: 2; Zwei Wege vergleichen Stufe 2: 1.

## Zurückgestellt

Flug ge1, Lernkarten `geometrie.grundbegriffe/verstehen` und `geometrie.ortslinien/verstehen`: Die Lernkarte heißt in beiden Themen gleich, die Zuordnung `l` zu Einheit ist dadurch nicht eindeutig. Es fehlen je drei Aufgaben, zusammen 6. Diese beiden Karten sind in der Tabelle nicht mitgezählt.

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
