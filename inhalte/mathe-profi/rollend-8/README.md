# rollend-8: Vorrat neue Formen, Klasse 7 (Auftrag 21)

Je Lernkarte genau drei Aufgaben in neuer Form, `K7-V001` bis `K7-V156`. Inhalt von Hand in
`teile/<kurz>.py`; `bauen.py` rechnet jede Lösung nach, prüft die Mischung und schreibt eine JSON je
Thema. Prüfen: `python3 -I inhalte/mathe-profi/rollend-8/bauen.py` (endet mit „OK"), einzelne Themen
durch Anhängen der Modulnamen. Nur Inhalte, nichts eingespielt.

```
Thema                        Karten  Aufg.  LW/FD/VW/ZW/UM/BR/AN   zaehlt ja/nein
finanzen.zinsen                   8     24  6/6/3/2/2/2/3          18/6
zahlen.potenzen_zehner            7     21  6/4/2/2/2/2/3          15/6
geometrie.kreis                   6     18  5/3/2/2/2/2/2          13/5
daten.kennwerte                   3      9  1/0/0/2/2/2/2           8/1
daten.boxplot                     6     18  4/3/2/2/2/2/3          14/4
daten.stichproben                 5     15  2/2/2/2/2/2/3          13/2
terme.potenzgesetze               3      9  1/0/0/2/2/2/2           8/1
abbildungen.determinanten2        6     18  4/3/2/2/2/2/3          14/4
raum.schraegbilder                4     12  2/1/1/2/2/2/2          10/2
raum.schraegbilder_teil2          4     12  2/1/1/2/2/2/2          10/2
Summe                            52    156  33/23/15/20/20/20/25  123/33
```

Stufen 1/2/3: 33/91/32. Antwortformen luecken 33, zahl 63, auswahl 60 – kein `bedingung`, keine neuen
Bauteile, keine Zeichnungen. Jede Aufgabe trägt `thema`; bei Teil 2 der Schrägbilder steht dort
`raum.schraegbilder_teil2`, obwohl der Bestand in `raum.schraegbilder` liegt.

## Mischung je Lernkarte

Für alle 52 Lernkarten vom Programm geprüft: höchstens ein Lückenweg (Stufe 1, `zaehlt = nein`),
höchstens ein Fehler-Detektiv (Stufe 3), mindestens eine zählende Aufgabe aus Umkehren / Zwei Wege /
Brücke / Verfahren wählen / Anwenden. Je Thema kommen Umkehren, Zwei Wege, Brücke und Anwenden
mindestens zweimal vor. **Zurückgestellt: keine Lernkarte.**

Wo eine Form fachlich nicht passte:
- `daten.kennwerte`, `terme.potenzgesetze`: nur drei Lernkarten, also neun Plätze; je zweimal
  Umkehren/Zwei Wege/Brücke/Anwenden braucht acht davon. Vorrang hatte diese Vorgabe, deshalb nur ein
  Lückenweg und kein Fehler-Detektiv – der Bestand hat dort in jeder Lernkarte schon `fehler`-Aufgaben
  (bei `fehler_finden` drei).
- `zahlen.potenzen_zehner`/`vergleichen_pruefen`: kein Fehler-Detektiv (drei im Bestand), dafür
  Verfahren wählen, Zwei Wege, Anwenden.
- `raum.schraegbilder`/`lage`, `daten.stichproben`/`repraesentativ` und `fehlerquellen` sind
  durchgehend qualitativ: kein Lückenweg, weil es keine sinnvollen Zahlenlücken gibt.

## Geprüft

- Jede Rechenaufgabe: `c` wird mit Brüchen ausgerechnet und mit dem von Hand erwarteten Wert
  verglichen, eine Abweichung bricht ab; bei Vielecken zusätzlich eine zweite Rechnung im Lösungsweg.
- Lückenweg: Kästchen = Werte, ganze Zahlen, kein Kleinbuchstabe in der Schablone (sonst Term-Vorlage),
  kein Komma neben einer Lücke, gesuchte Zahl nicht im Aufgabentext.
- Auswahl: genau eine richtige Antwort, keine Dopplung, je falsche Antwort ein Fehlbild mit demselben
  Text. Keine Dopplung zum Bestand, wörtlich und mit nur anderen Zahlen geprüft.
- Kennungen eindeutig, alle `regel`-Angaben gibt es im Regel-Universum.
- `tools/inhalt_pruefen.py` an Kopien der zehn Themen-Dateien: Code 0. `typ` und `zaehlt` aller 156
  Aufgaben gegen die acht erlaubten Formen aus `tools/rollend_sql.py` geprüft.

## Annahmen

Stufen und `g` nach `form-takt.md`: LW Stufe 1/`nein`/`direkt`, FD Stufe 3/`fehler`, VW und ZW Stufe 2
`mehrschritt`, UM `umkehr`, BR `darstellung`, AN `einkleidung` bzw. Stufe 3 `transfer`.

## Offene Punkte (nichts geändert)

- `tools/rollend_sql.py` meldet alle zehn Dateien als „ohne Zuordnung": die Themen fehlen in
  `inhalte/plan/rollend-einheiten.json`, und beides darf ich nicht ändern (anderer Helfer). Erwartet,
  wie zuvor bei rollend-3. Keine Prüfung in der App, keine Prüfung durch Kinder.
- Befund im Bestand, außerhalb meines Ordners: In `daten.boxplot` begründet der Hinweis zur Spannweite
  bei negativen Werten eine Strichrechnung mit der Vorzeichenregel der Punktrechnung („minus minus wird
  plus"). Das sind zwei getrennte Kennungen (`rr.plusminus`, `rr.vorzeichen`).
