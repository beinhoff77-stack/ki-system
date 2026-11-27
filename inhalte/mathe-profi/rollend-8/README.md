# rollend-8: Vorrat neue Formen, Klasse 7 (Auftrag 21)

Je Lernkarte genau drei Aufgaben in neuer Form, Kennungen `K7-V001` bis `K7-V156`.
Der Inhalt steht von Hand in `teile/<kurz>.py`; `bauen.py` rechnet jede Lösung nach, prüft die
Mischungsregeln und schreibt eine JSON-Datei je Thema. Nur Inhalte, nichts eingespielt.

Bauen und prüfen: `python3 -I inhalte/mathe-profi/rollend-8/bauen.py` (muss mit „OK" enden).
Einzelne Themen: Modulnamen anhängen, z. B. `… bauen.py zinsen kreis`.

## Stand

```
Thema                        Karten  Aufg.  Formen (LW/FD/VW/ZW/UM/BR/AN)   zaehlt ja/nein
finanzen.zinsen                   8     24  6/6/3/2/2/2/3                   18/6
zahlen.potenzen_zehner            7     21  6/4/2/2/2/2/3                   15/6
geometrie.kreis                   6     18  5/3/2/2/2/2/2                   13/5
daten.kennwerte                   3      9  1/0/0/2/2/2/2                    8/1
daten.boxplot                     6     18  4/3/2/2/2/2/3                   14/4
daten.stichproben                 5     15  2/2/2/2/2/2/3                   13/2
terme.potenzgesetze               3      9  1/0/0/2/2/2/2                    8/1
abbildungen.determinanten2        6     18  4/3/2/2/2/2/3                   14/4
raum.schraegbilder                4     12  2/1/1/2/2/2/2                   10/2
raum.schraegbilder_teil2          4     12  2/1/1/2/2/2/2                   10/2
Summe                            52    156  33/23/15/20/20/20/25           123/33
```

Stufen: 1 → 33, 2 → 91, 3 → 32. Antwortformen: luecken 33, zahl 63, auswahl 60 (keine `bedingung`,
keine neuen Bauteile, keine Zeichnungen). Jede Aufgabe trägt das Feld `thema`; bei Teil 2 der
Schrägbilder steht dort `raum.schraegbilder_teil2`, obwohl der Bestand in `raum.schraegbilder` liegt.

## Mischung je Lernkarte

Gesichert für alle 52 Lernkarten (vom Programm geprüft): höchstens ein Lückenweg (Stufe 1,
`zaehlt = nein`), höchstens ein Fehler-Detektiv (Stufe 3), mindestens eine zählende Aufgabe der
Formen Umkehren / Zwei Wege / Brücke / Verfahren wählen / Anwenden. Über jedes Thema kommt jede der
Formen Umkehren, Zwei Wege, Brücke und Anwenden mindestens zweimal vor.

**Wo eine Form fachlich nicht passte:**
- `daten.kennwerte` und `terme.potenzgesetze` haben nur drei Lernkarten, also neun Plätze. Je zweimal
  Umkehren / Zwei Wege / Brücke / Anwenden braucht acht davon. Vorrang hatte diese Vorgabe; deshalb
  gibt es dort nur einen Lückenweg und keinen Fehler-Detektiv. Beide Themen haben im Bestand in jeder
  Lernkarte schon eine Aufgabe vom Typ `fehler` (bei `fehler_finden` sogar drei).
- `zahlen.potenzen_zehner`/`vergleichen_pruefen`: kein Fehler-Detektiv, der Bestand hat dort drei
  `fehler`-Aufgaben; stattdessen Verfahren wählen, Zwei Wege und Anwenden.
- `raum.schraegbilder`/`lage` und `daten.stichproben`/`repraesentativ`, `fehlerquellen` sind
  durchgehend qualitativ: dort kein Lückenweg (keine sinnvollen Zahlenlücken).

Zurückgestellte Lernkarten: **keine**. Alle 52 sind mit drei Aufgaben gebaut.

## Geprüft

- Jede Rechenaufgabe: `bauen.py` rechnet das Feld `c` mit Brüchen aus und vergleicht mit dem von Hand
  erwarteten Wert (`erwartet`). Eine Abweichung bricht ab. Bei Vielecken zusätzlich eine zweite
  Rechnung im Lösungsweg (Trapez bzw. Zerlegung).
- Lückenweg: Zahl der Kästchen gleich Zahl der Werte, ganze Zahlen, kein Kleinbuchstabe in der
  Schablone (sonst wäre es eine Term-Vorlage), kein Komma neben einer Lücke, gesuchte Zahl steht
  nicht im Aufgabentext.
- Auswahl: genau eine richtige Antwort, keine doppelten Antworten, zu jeder falschen Antwort ein
  Fehlbild mit gleichlautendem Text.
- Keine Dopplung zum Bestand: Aufgabentext weder wörtlich noch mit nur anderen Zahlen vorhanden.
- Kennungen eindeutig; alle `regel`-Angaben gibt es im Regel-Universum.
- `tools/inhalt_pruefen.py` an Kopien der zehn Themen-Dateien mit den neuen Aufgaben: Code 0.
- `tools/rollend_sql.py`: alle 156 Aufgaben haben einen gültigen `typ` (acht erlaubte Formen) und
  `zaehlt` ja/nein.

## Annahmen

- Formen und Stufen nach `form-takt.md`: Lückenweg Stufe 1 und `zaehlt = nein`, Fehler-Detektiv
  Stufe 3, die übrigen Formen Stufe 2 (Anwenden auch Stufe 3, dann `g = transfer`).
- `g` aus der Form: LW → `direkt`, FD → `fehler`, VW/ZW → `mehrschritt`, UM → `umkehr`,
  BR → `darstellung`, AN → `einkleidung` bzw. `transfer`.

## Offene Punkte (nicht geprüft, nichts geändert)

- `tools/rollend_sql.py` meldet alle zehn Dateien als „ohne Zuordnung": die Themen fehlen in
  `inhalte/plan/rollend-einheiten.json`. Das Werkzeug und diese Datei darf ich nicht ändern (anderer
  Helfer). Erwartet, wie zuvor bei rollend-3; wird mit der Planung behoben.
- Keine Prüfung in der App, keine Prüfung durch Kinder.
- Befund im Bestand, außerhalb meines Ordners: In `daten.boxplot` begründet der Hinweis von
  „Spannweite bei negativen Werten" eine **Strichrechnung** mit der Vorzeichenregel für Punktrechnung
  („minus minus wird plus"). Das sind zwei getrennte Kennungen (`rr.plusminus`, `rr.vorzeichen`) und
  gehört getrennt formuliert. Nicht geändert, weil ich nur in meinem Ordner schreibe.
