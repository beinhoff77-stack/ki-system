# Runde VT1A: Verstehens-Aufgaben für Tests, Klasse 5

Stand 28.11.2026. Nichts davon ist eingespielt; es sind nur Inhalte in `inhalte/mathe-profi/vtest-1a/`.

**77 Aufgaben** in zwei Einheiten (11 von 21 Lernzielen: `zahlen.potenzen_basis` 4 von 7, `zahlen.rechengesetze` 7 von 14). Je Lernziel 1 Test-Aufgabe (`ersetzt_test`), 3 Korrektur- und 3 Sicherungs-Aufgaben. Kennungen `VT1A-001` bis `VT1A-077`.

## Dateien

| Datei | Inhalt |
|---|---|
| `auswahl.md` | Auswahl der Lernziele, Begründung, Abweichung vom Vorschlag, Lehrplan-Bezug |
| `zahlen.potenzen_basis.json`, `zahlen.rechengesetze.json` | die Aufgaben (Format wie `rollend-15`, dazu `pool`, `abgrenzung`, `loesung_rechnung`, `rechnung` je Fehlbild) |
| `kern.py`, `th_*.py` | Quelltexte der Aufgaben (Hilfsfunktionen und Aufgaben je Einheit) |
| `bauen.py` | prüft alle Regeln des Auftrags, schreibt die JSON-Dateien und `regeln-zuordnung.md`, ruft `tools/vorrat_pruefen.py` und `tools/vtest_pruefen.py --runde 1a` auf; endet mit „OK“ |
| `gegenrechnung.py` | rechnet alle 77 Sollantworten unabhängig neu; endet mit „0 Abweichungen“ |
| `regeln-zuordnung.md` | Regel-Kennung je Aufgabe (erzeugt von `bauen.py`) |

Aufrufe vom Wurzelordner des Repos: `python3 -I inhalte/mathe-profi/vtest-1a/bauen.py`, `python3 -I inhalte/mathe-profi/vtest-1a/gegenrechnung.py`, `python3 -I tools/vtest_pruefen.py --runde 1a`.

## Zahlen

### Je Lernziel

| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 | Stufe 3 | zahl | auswahl |
|---|---|---|---|---|---|---|---|---|
| zahlen.potenzen_basis | schreibweise | 1 | 3 | 3 | 5 | 2 | 3 | 4 |
| zahlen.potenzen_basis | quadrat | 1 | 3 | 3 | 4 | 3 | 4 | 3 |
| zahlen.potenzen_basis | zehner | 1 | 3 | 3 | 4 | 3 | 5 | 2 |
| zahlen.potenzen_basis | sach | 1 | 3 | 3 | 4 | 3 | 4 | 3 |
| zahlen.rechengesetze | klammern | 1 | 3 | 3 | 4 | 3 | 2 | 5 |
| zahlen.rechengesetze | termaufbau | 1 | 3 | 3 | 4 | 3 | 3 | 4 |
| zahlen.rechengesetze | vorteil | 1 | 3 | 3 | 4 | 3 | 2 | 5 |
| zahlen.rechengesetze | verteilen | 1 | 3 | 3 | 4 | 3 | 3 | 4 |
| zahlen.rechengesetze | umkehraufgabe_mal | 1 | 3 | 3 | 4 | 3 | 3 | 4 |
| zahlen.rechengesetze | ueberschlag | 1 | 3 | 3 | 4 | 3 | 4 | 3 |
| zahlen.rechengesetze | sach | 1 | 3 | 3 | 4 | 3 | 5 | 2 |

### Verteilung

| Pool | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| korrektur | 12 | 21 | 33 |
| sicherung | 12 | 21 | 33 |
| test | 4 | 7 | 11 |

| Stufe | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| 2 | 17 | 28 | 45 |
| 3 | 11 | 21 | 32 |

| Typ | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| begruenden | 5 | 10 | 15 |
| darstellung | 6 | 7 | 13 |
| mehrschritt | 3 | 7 | 10 |
| parameter | 1 | 3 | 4 |
| pruefung | 0 | 1 | 1 |
| rueckwaerts | 2 | 4 | 6 |
| transfer | 1 | 3 | 4 |
| umkehr | 8 | 14 | 22 |
| verknuepfen | 2 | 0 | 2 |

| Form | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| anwenden | 1 | 3 | 4 |
| bruecke | 6 | 7 | 13 |
| ohne Form | 6 | 11 | 17 |
| umkehren | 11 | 20 | 31 |
| verfahren_waehlen | 1 | 2 | 3 |
| zwei_wege | 3 | 6 | 9 |

| Antwortform | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| auswahl | 12 | 27 | 39 |
| zahl | 16 | 22 | 38 |

## Aufbau der Pools

- **test** (Stufe 3): eine Aufgabe je Lernziel, die die alte Test-Aufgabe ersetzen soll; verlangt Begründen, Rückwärtsdenken oder Übertragen.
- **korrektur** (Stufe 2): Umkehraufgaben, Darstellungswechsel (Rechnung ↔ Text, Brücke), zwei Rechenwege vergleichen. Keine Rechenhilfe im Text.
- **sicherung** (Stufe 2 und 3 gemischt): Begründen mit echten Fehlvorstellungen als Möglichkeiten, Fehler in einer Rechnung finden und berichtigen (als Auswahl vollständiger Aussagen), Parameter, Rückwärts, Transfer.
- Antworttypen: nur `zahl` und `auswahl`. Auswahl immer mit 4 Möglichkeiten (eine mit 5 ist nicht dabei), die Lage der richtigen Antwort ist über die Aufgaben verteilt. Kein Tipp (`h`), keine Toleranz, kein Lückenweg.
- Fehlbilder: zu jeder falschen Zahl und jeder falschen Möglichkeit steht die Beschreibung des Denkfehlers; bei Zahlantworten zusätzlich eine `rechnung`, die genau die Fehlantwort ergibt (von `tools/vtest_pruefen.py` nachgerechnet). Die Katalog-Kennungen `fb.*` sind nicht vergeben.

## Lehrplan-Bezug

`lehrplan` = „M5 3“ (Natürliche und ganze Zahlen – Multiplikation und Division), wie es `tools/vtest_pruefen.py` aus der Themenliste verlangt. Nur natürliche Zahlen, keine negativen Zahlen, keine Brüche, keine Variablen (die Kästchen □ stehen für gesuchte Zahlen). Potenzen mit natürlicher Hochzahl bis 6 und Zehnerpotenzen bis 10⁶; Terme bis höchstens drei Rechenschritte.

## Ehrlich: Zweifelsfälle und Grenzen

1. **Lehrplan-Nummer.** Das Repo führt zwei Zuordnungen: `inhalte/pruefung/klassen/vorschlag-rsib.md` sagt „M5 1.3“, die Themenliste (und damit das Prüfwerkzeug) „M5 3“. Verwendet ist „M5 3“; amtlich nachgeprüft ist keines von beiden (Lehrplantext nicht einsehbar). Die Vorprüfung sollte das klären.
2. **Zahl-Aufgaben mit fast fester Lösungsrechnung.** Bei einigen Rückwärts- und Zählaufgaben (z. B. VT1A-004, 017, 021, 023, 024, 027, 063, 070) ist `loesung_rechnung` nur der Wert selbst oder eine einfache Zeile; die eigentliche Probe liefert `gegenrechnung.py` mit einer Zählschleife. Das prüft die Zahl, aber nicht jeden Gedankenschritt. Entsprechend sind einige Fehlbild-`rechnung`en einfache Ausdrücke (z. B. „7“, „10“, „5 + 1“).
3. **Typ und Form.** Die Pflicht zu einem Verstehens-Typ oder einer Verstehens-Form (V5) ist bei manchen `mehrschritt`-Aufgaben nur über die Form erfüllt (`zwei_wege`, `verfahren_waehlen`): VT1A-030, 034, 044, 046, 049, 067, 068. Dort gibt es sachlich zwei Wege (alle Terme ausrechnen oder geschickt vergleichen), aber auch einen sehr direkten. 31 von 77 Aufgaben haben die Form `umkehren`; das ist viel, passt aber zu den Lernzielen (Umkehren ist hier das Verstehen).
4. **Fehler-Aufgaben.** „Finde den Fehler“ ist als Auswahl vollständiger Aussagen („Fehler: … Richtig wäre …“, daneben falsche Fehlerdiagnosen und „Kein Fehler: …“) gebaut. Das ist typ `begruenden` und nicht Fehler-Detektiv, weil V8 für diesen Typ mindestens drei nummerierte Zeilen verlangt; Aufgaben mit Zeilen wurden nicht gebaut (Klasse 5, wenige Rechnungen).
5. **Verneinte Frage.** VT1A-016 („gehört NICHT zur Zahl“) und VT1A-054 („NICHT richtig“) sind verneint gestellt, im Text ist NICHT großgeschrieben. Falls die App keine verneinten Fragen will, diese zwei tauschen.
6. **Eindeutigkeit.** Stellen, die die Vorprüfung ansehen sollte: VT1A-003 (Tabelle, Generationen: 1. Generation = Eltern, steht im Text), VT1A-012 (eine Reihe und eine Spalte kommen hinzu, 27 Bäume), VT1A-021 („kleiner als“ schließt Gleichheit aus), VT1A-065 und 070 (Rundungsregel „ab 5 bzw. ab 50 aufrunden“ steht im Text; 070 zählt die Zahlen 4 550 bis 4 649, ob die Null zu den natürlichen Zahlen gehört, spielt dort keine Rolle), VT1A-075 (Bäcker: „die Hälfte seiner Brötchen und noch 7 dazu“, die zweite Hälfte bezieht sich auf die übrigen).
7. **Regeln.** Alle Aufgaben tragen die Regel ihrer Lernkarte. Bei `zahlen.rechengesetze` führen `umkehraufgabe_mal`, `sach` (`rr.gegenrechnung`) und `ueberschlag` (`id.zahlen.buendeln`) Regeln, die im Katalog `kennungen.json` die Einheit nicht in der Themenliste haben (siehe `regeln-zuordnung.md`). Bei `zahlen.potenzen_basis` hat `quadrat` keine Lernkarten-Regel (genommen: `rr.potenz`), ebenso `termaufbau` (genommen: `rr.reihenfolge`). Diese zwei Zuordnungen sind Vorschläge.
8. **Gleiche Sollantwort im Lernziel.** `bauen.py` meldet, dass in `schreibweise` zweimal 3, in `zehner` zweimal 5 und in `termaufbau` zweimal 6 herauskommt. Die Aufgaben sind sonst verschieden; wer will, ändert Zahlen.
9. **Auswahl.** Siehe `auswahl.md`: Abweichung vom Vorschlag des Auftraggebers, weil `negativ` und `mal_ganz` nicht Klasse 5 sind.

## Ergebnis der Prüfungen

- `bauen.py`: OK (77 Aufgaben, 230 Fehlbilder/falsche Möglichkeiten, davon 112 Zahl-Fehlbilder mit nachgerechneter Rechnung, 116 falsche Möglichkeiten mit geprüfter Aussage im Quelltext, 2 nur von Hand gelesen).
- `gegenrechnung.py`: 77 Sollantworten neu gerechnet, 0 Abweichungen.
- `tools/vorrat_pruefen.py` über die Dateien: 77 Aufgaben, 0 Meldungen.
- `tools/vtest_pruefen.py --runde 1a`: keine Fehler; 3 Hinweise (Abweichung vom Vorschlag bei beiden Einheiten, Rhythmus RVVVRVRRRVVRRV bei `zahlen.rechengesetze`).
