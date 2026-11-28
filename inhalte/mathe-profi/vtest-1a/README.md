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
| `sonderfaelle.md`, `korrektur-nach-vorpruefung.md`, `vorpruefung.md` | Sonderfall-Durchsicht, Korrekturbericht, Bericht der Vorprüfung |

Aufrufe vom Wurzelordner des Repos: `python3 -I inhalte/mathe-profi/vtest-1a/bauen.py`, `python3 -I inhalte/mathe-profi/vtest-1a/gegenrechnung.py`, `python3 -I tools/vtest_pruefen.py --runde 1a`.

## Zahlen

### Je Lernziel

| Einheit | Lernziel | test | korrektur | sicherung | Stufe 2 | Stufe 3 | zahl | auswahl | Ideen |
|---|---|---|---|---|---|---|---|---|---|
| zahlen.potenzen_basis | schreibweise | 1 | 3 | 3 | 4 | 3 | 2 | 5 | 7 |
| zahlen.potenzen_basis | quadrat | 1 | 3 | 3 | 4 | 3 | 3 | 4 | 7 |
| zahlen.potenzen_basis | zehner | 1 | 3 | 3 | 4 | 3 | 3 | 4 | 7 |
| zahlen.potenzen_basis | sach | 1 | 3 | 3 | 4 | 3 | 4 | 3 | 5 |
| zahlen.rechengesetze | klammern | 1 | 3 | 3 | 4 | 3 | 1 | 6 | 5 |
| zahlen.rechengesetze | termaufbau | 1 | 3 | 3 | 4 | 3 | 2 | 5 | 6 |
| zahlen.rechengesetze | vorteil | 1 | 3 | 3 | 4 | 3 | 1 | 6 | 7 |
| zahlen.rechengesetze | verteilen | 1 | 3 | 3 | 4 | 3 | 1 | 6 | 7 |
| zahlen.rechengesetze | umkehraufgabe_mal | 1 | 3 | 3 | 4 | 3 | 3 | 4 | 6 |
| zahlen.rechengesetze | ueberschlag | 1 | 3 | 3 | 4 | 3 | 2 | 5 | 6 |
| zahlen.rechengesetze | sach | 1 | 3 | 3 | 4 | 3 | 5 | 2 | 6 |

### Verteilung

| Pool | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| korrektur | 12 | 21 | 33 |
| sicherung | 12 | 21 | 33 |
| test | 4 | 7 | 11 |

| Stufe | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| 2 | 16 | 28 | 44 |
| 3 | 12 | 21 | 33 |

| Typ | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| begruenden | 8 | 9 | 17 |
| darstellung | 8 | 10 | 18 |
| mehrschritt | 1 | 5 | 6 |
| parameter | 1 | 3 | 4 |
| pruefung | 0 | 1 | 1 |
| rueckwaerts | 2 | 3 | 5 |
| transfer | 0 | 4 | 4 |
| umkehr | 7 | 13 | 20 |
| verknuepfen | 1 | 1 | 2 |

| Form | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| bruecke | 5 | 8 | 13 |
| ohne Form | 13 | 17 | 30 |
| umkehren | 8 | 17 | 25 |
| verfahren_waehlen | 0 | 2 | 2 |
| zwei_wege | 2 | 5 | 7 |

| Antwortform | zahlen.potenzen_basis | zahlen.rechengesetze | gesamt |
|---|---|---|---|
| auswahl | 16 | 34 | 50 |
| zahl | 12 | 15 | 27 |

## Aufbau der Pools

- **test** (Stufe 3): eine Aufgabe je Lernziel, die die alte Test-Aufgabe ersetzen soll; verlangt Begründen, Rückwärtsdenken oder Übertragen.
- **korrektur** (Stufe 2): Umkehraufgaben, Darstellungswechsel (Rechnung ↔ Text, Brücke), zwei Rechenwege vergleichen. Keine Rechenhilfe im Text.
- **sicherung** (Stufe 2 und 3 gemischt): Begründen mit echten Fehlvorstellungen als Möglichkeiten, Fehler in einer Rechnung finden und berichtigen (als Auswahl vollständiger Aussagen), Parameter, Rückwärts, Transfer.
- Antworttypen: nur `zahl` und `auswahl`. Auswahl mit 4 Möglichkeiten (VT1A-029 hat 5), die Lage der richtigen Antwort ist über die Aufgaben verteilt. Kein Tipp (`h`), keine Toleranz, kein Lückenweg.
- Fehlbilder: zu jeder falschen Zahl und jeder falschen Möglichkeit steht die Beschreibung des Denkfehlers; bei Zahlantworten zusätzlich eine `rechnung`, die genau die Fehlantwort ergibt (von `tools/vtest_pruefen.py` nachgerechnet). Die Katalog-Kennungen `fb.*` sind nicht vergeben.

## Lehrplan-Bezug

`lehrplan` = „M5 3“ (Natürliche und ganze Zahlen – Multiplikation und Division), wie es `tools/vtest_pruefen.py` aus der Themenliste verlangt. Nur natürliche Zahlen, keine negativen Zahlen, keine Brüche, keine Variablen (die Kästchen □ stehen für gesuchte Zahlen). Potenzen mit natürlicher Hochzahl bis 6 und Zehnerpotenzen bis 10⁶; Terme bis höchstens drei Rechenschritte.

## Ehrlich: Zweifelsfälle und Grenzen

(Stand nach der zweiten Korrektur, siehe `korrektur-nach-vorpruefung.md` und `korrektur-nach-vorpruefung-2.md`.)

1. **Lehrplan-Nummer.** „M5 3“ ist laut Vorprüfung die Nummer des Gymnasiums; „M5 1.3“ im Repo (`vorschlag-rsib.md`) gehört zur Realschule. Eigene Quelle für den Lehrplanwortlaut habe ich nicht, ich stütze mich auf die Vorprüfung.
2. **Ideen statt Typ-Etiketten.** Jede Aufgabe trägt ein Feld `idee` (Denkfigur). `bauen.py` verlangt je Lernziel mindestens 5 verschiedene Ideen und keine öfter als zweimal. Die Ideen sind meine Einteilung; die Vorprüfung sollte prüfen, ob sie die Aufgaben wirklich unterscheidet. Knapp sind `klammern` (genau 5) und `zahlen.potenzen_basis/sach` (5).
3. **Zahl-Aufgaben mit fast fester Lösungsrechnung.** Bei einigen Zählaufgaben (z. B. 004, 017, 021, 023, 024, 070) ist `loesung_rechnung` nur der Wert selbst oder eine kurze Zeile; die eigentliche Probe liefert `gegenrechnung.py` mit einer Zählschleife.
4. **Typ und Form.** Bei den mehrschritt-Aufgaben 045, 046, 053, 055, 067 trägt die Form (`verfahren_waehlen`, `zwei_wege`) den Verstehens-Anspruch; dort geht es wirklich um die Wahl oder den Vergleich zweier Wege, nicht um ein Etikett. 25 von 77 Aufgaben haben die Form `umkehren` (vorher 31).
5. **Fehler-Aufgaben.** „Finde den Fehler“ ist als Auswahl vollständiger Aussagen („Fehler: … Richtig wäre …“) gebaut, Typ `begruenden`, nicht Fehler-Detektiv (V8 verlangt dafür nummerierte Zeilen).
6. **Verneinte Frage.** Keine mehr: VT1A-016 fragt jetzt positiv nach der einen Schreibweise mit anderem Wert.
7. **Antwortformen.** 38 von 77 Aufgaben sind Auswahl (4 Möglichkeiten, nur VT1A-029 hat 5), 39 Zahl, keine Lücken. Im Test-Pool sind 3 von 11 Auswahl (001, 029, 036). Optionstexte sind in der Länge angeglichen (richtige Option die längste in 5 von 38), die Lage der richtigen Antwort ist gleichmäßig (9/10/9/9), „Kein Fehler“ und „Beide“ sind teils richtig; `bauen.py` prüft Länge, Lage und Anfangswörter dauerhaft.
8. **Regeln.** Bei `ueberschlag` steht keine Regel (kein Katalogeintrag trägt Überschlagen); Begründung in `regeln-zuordnung.md`, das Werkzeug meldet 7 Hinweise dazu. Bei `zahlen.rechengesetze` führen `umkehraufgabe_mal` und `sach` die Regel `rr.gegenrechnung`, die im Katalog die Einheit nicht in der Themenliste hat. `quadrat` (`rr.potenz`) und `termaufbau` (`rr.reihenfolge`) haben keine Lernkarten-Regel; das sind Vorschläge.
9. **x und □.** In Aufgaben zu Gleichungen (VT1A-060 bis 063) steht x (Lehrplan M5 3.1), sonst □ für eine Lücke.
10. **Auswahl.** Siehe `auswahl.md`: Abweichung vom Vorschlag des Auftraggebers; `negativ`, `mal_ganz`, `geteilt_ganz`, `vertauschen`, `schriftlich` sind für eine Folgerunde vorgemerkt.
11. **Keine Bilder.** Keine Aufgabe nutzt `grafik`; alles steht im Fragetext.

## Ergebnis der Prüfungen

- `bauen.py`: OK (77 Aufgaben, 228 Fehlbilder/falsche Möglichkeiten geprüft).
- `gegenrechnung.py`: 77 Sollantworten neu gerechnet, 0 Abweichungen.
- `tools/vorrat_pruefen.py` über die Dateien: 77 Aufgaben, 0 Meldungen.
- `tools/vtest_pruefen.py --runde 1a`: keine Fehler; 10 Hinweise (Abweichung vom Vorschlag bei beiden Einheiten, Rhythmus RVVVRVRRRVVRRV bei `zahlen.rechengesetze`, 7-mal „Regel fehlt“ bei `ueberschlag`).
- Weitere Dateien: `sonderfaelle.md` (Durchsicht der Auswahl-Aufgaben), `korrektur-nach-vorpruefung.md`, `korrektur-nach-vorpruefung-2.md`.
