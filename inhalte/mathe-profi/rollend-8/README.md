# rollend-8: Vorrat neue Formen, Klasse 7 (Auftrag 21)

Je Lernkarte genau drei Aufgaben in neuer Form, `K7-V001` bis `K7-V156`. Inhalt von Hand in
`teile/<kurz>.py`; `bauen.py` rechnet jede Lösung nach, prüft die Mischung und schreibt eine JSON je
Thema: `python3 -I inhalte/mathe-profi/rollend-8/bauen.py` (endet mit „OK"), einzelne Themen durch
Anhängen der Modulnamen. Nur Inhalte, nichts eingespielt.

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

Stufen 1/2/3: 48/82/26 (nach der Selbstprüfung: reine Methodenauswahl ist Stufe 1/`erkennen`). Antwortformen luecken 33, zahl 63, auswahl 60 – kein `bedingung`, keine neuen
Bauteile, keine Zeichnungen. Jede Aufgabe trägt `thema`; bei Schrägbilder Teil 2 steht dort
`raum.schraegbilder_teil2`, obwohl der Bestand in `raum.schraegbilder` liegt.

## Mischung je Lernkarte

Für alle 52 Lernkarten vom Programm geprüft: höchstens ein Lückenweg (Stufe 1, `zaehlt = nein`),
höchstens ein Fehler-Detektiv (Stufe 3), mindestens eine zählende Aufgabe aus Umkehren / Zwei Wege /
Brücke / Verfahren wählen / Anwenden; je Thema kommen Umkehren, Zwei Wege, Brücke und Anwenden
mindestens zweimal vor. **Zurückgestellt: keine Lernkarte.** Wo eine Form fachlich nicht passte:
- `daten.kennwerte`, `terme.potenzgesetze`: nur drei Lernkarten, also neun Plätze; je zweimal
  Umkehren/Zwei Wege/Brücke/Anwenden braucht acht davon. Vorrang hatte diese Vorgabe, deshalb nur ein
  Lückenweg und kein Fehler-Detektiv – der Bestand hat dort schon `fehler`-Aufgaben in jeder Lernkarte.
- `zahlen.potenzen_zehner`/`vergleichen_pruefen`: kein Fehler-Detektiv (drei im Bestand), dafür
  Verfahren wählen, Zwei Wege, Anwenden. `raum.schraegbilder`/`lage`, `daten.stichproben`/
  `repraesentativ` und `fehlerquellen` sind qualitativ: kein Lückenweg, keine sinnvollen Zahlenlücken.

## Geprüft

- Jede Rechenaufgabe: `c` mit Brüchen ausgerechnet und mit dem Handwert verglichen, Abweichung bricht
  ab; bei Vielecken zusätzlich eine zweite Rechnung im Lösungsweg.
- Lückenweg: Kästchen = Werte, ganze Zahlen, kein Kleinbuchstabe in der Schablone (sonst Term-Vorlage),
  kein Komma neben einer Lücke, gesuchte Zahl nicht im Aufgabentext.
- Auswahl: genau eine richtige Antwort, je falsche ein Fehlbild mit demselben Text. Keine Dopplung zum
  Bestand (wörtlich und mit nur anderen Zahlen), Kennungen eindeutig, `regel` im Regel-Universum.
- `tools/inhalt_pruefen.py` an Kopien der zehn Themen-Dateien: Code 0. `typ` und `zaehlt` aller 156
  Aufgaben gegen die acht erlaubten Formen aus `tools/rollend_sql.py` geprüft.

**Annahme** – Stufen und `g` nach `form-takt.md` und `rollend-2/verhaeltnis.md`: LW Stufe 1/`nein`/`direkt`, FD Stufe 3/`fehler`,
VW (reine Methodenauswahl) Stufe 1 `erkennen`, ZW Stufe 2 `mehrschritt`, UM `umkehr`, BR `darstellung`,
AN `einkleidung` (Stufe 2; drei Aufgaben mit mehreren Modellschritten Stufe 3 `transfer`).

## Offene Punkte (nichts geändert)
- `tools/rollend_sql.py` meldet alle zehn Dateien als „ohne Zuordnung": die Themen fehlen in
  `inhalte/plan/rollend-einheiten.json`; beides darf ich nicht ändern (anderer Helfer). Erwartet, wie
  bei rollend-3. Keine Prüfung in der App, keine Prüfung durch Kinder.
- Befund im Bestand, außerhalb meines Ordners: In `daten.boxplot` begründet der Hinweis zur Spannweite
  bei negativen Werten eine Strichrechnung mit der Vorzeichenregel der Punktrechnung. Das sind zwei
  getrennte Kennungen (`rr.plusminus`, `rr.vorzeichen`).

## Selbstprüfung nach den Maßstäben der Gegenprüfung, Werkstatt 1041–1052

Alle 156 Aufgaben einzeln gegengelesen, nachdem die Lehren aus den Schwester-Runden vorlagen. Geändert wurde
je Muster (Kennungen K7-V…):
- **Lückenwege (33 von 33 neu gebaut):** keine Lücke steht mehr als Zahl, Zahlwort oder Umschreibung in Text, Schablone oder
  Tipp; bei allen hängt die letzte Lücke rechnerisch von einer früheren ab; je eine Lücke an der entscheidenden Stelle
  (Feld `entscheidend`, mit Fehlbild). 28 mit drei, eine (082) mit vier, vier (091, 094, 139, 145) mit zwei Lücken.
- **Fehlbilder (16 berichtigt):** 011, 014, 020, 029, 032, 044, 045, 046, 053, 094, 101, 105, 120, 129, 132, 146
  (Beschreibung oder Wert passte nicht zur gespeicherten Fehlantwort). Alle 193 Fehlbilder von Zahl- und Lückenaufgaben
  tragen jetzt eine `rechnung`, die das Programm nachrechnet.
- **Fehler-Detektive (23, alle nach dem ERSTEN Fehler fragend):** 14 inhaltlich umgebaut (003, 009, 015, 027, 030, 033, 036, 048,
  063, 075, 081, 099, 123, 147), damit Fehlerzeile und Folgezeilen stimmen; die übrigen 9 nur Frage und Tipp. Fehlerzeilen
  vorher 0/4/19, jetzt 8/8/7 (Zeile 1/2/3).
- **Eindeutigkeit, Voraussetzungen, Tipps:** in 89 Aufgaben Tipp geändert (verriet die Regel oder das Ergebnis), Voraussetzungen
  ergänzt u. a. in 002, 004, 020, 021, 023, 043, 048, 060, 080, 095, 096, 104, 105, 113, 131, 141, 146, 152; zwei gleiche
  falsche Auswahlantworten ersetzt in 017, 042, 114 (und 029/039 bleiben bewusst gleichwertig, nur eine ist „wissenschaftlich“).
- **Form und `g`:** „Zwei Wege“ neu, weil derselbe Weg: 060, 065, 068, 077, 083, 110, 140, 152, 156. „Brücke“ mit echtem
  Darstellungswechsel (Koordinaten, Gleichung, Zahlenreihe, Tabelle): 050, 062, 072, 079, 093, 097, 122, 136.
  15 „Verfahren wählen“ von Stufe 2/`mehrschritt` auf Stufe 1/`erkennen`; 6 „Anwenden“ ohne Modellbildung von 3 auf 2
  (045, 057, 071, 087, 096, 153). Aufgabe 071 war inhaltlich gleich zu 070 und fragt jetzt nach der Änderung des Mittelwerts.

**Maschinell geprüft (`bauen.py`, endet mit „OK“):** Lückenwerte nicht im Text/Schablone/Tipp/Eingabehinweis (Ziffer, Hochzahl,
Tausendergruppe, Zahlwort bis Million); mindestens zwei Lücken; Abhängigkeit durch Einsetzen (Lücke ± 420 ändert die spätere);
letzte Lücke abhängig; entscheidende Lücke hat ein Fehlbild; jede Fehlbild-`rechnung` ergibt genau die gespeicherte Fehlantwort
und nie die richtige; Auswahl mit `a_rechnung`: alle Antworten rechnerisch verschieden, nur die richtige ergibt `a_wert`;
Fehler-Detektiv fragt nach dem ersten Fehler und hat so viele Antworten wie Zeilen; Verteilung der Fehlerzeilen wird ausgegeben.

**Nur von Hand geprüft:** Fehlerzeile für sich falsch und Folgezeilen folgerichtig; Grammatik (Singular/Plural) verrät nichts;
Eindeutigkeit der Auswahl ohne Rechnung; Voraussetzungen; ob zwei Wege wirklich verschiedene Verfahren sind; Darstellungswechsel;
Eignung von Stufe und `g`.

**Offen / Einschätzung:** 083 Weg B nutzt die Positionsregel (n + 1) : 4, die nicht überall im Unterricht vorkommt und nur hier mit
Weg A übereinstimmt; 152 Weg B (Streifen) steht dem Weg A nah; 061 Lücke ③ (Summe der Koordinaten) ist eine künstliche
Abhängigkeit. Keine Prüfung in der App und durch Kinder.
