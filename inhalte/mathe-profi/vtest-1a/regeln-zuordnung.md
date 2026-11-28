# Runde VT1A: Regel-Kennung je Aufgabe

Maßstab: die Regel, die das Kind zum Lösen am stärksten braucht (tragender Lösungsschritt). Kennungen aus `inhalte/mathe-profi/regeln-uebersicht/kennungen.json`; `bauen.py` prüft, dass die Kennung im Katalog steht; `tools/vtest_pruefen.py` vergleicht mit der Regel der Lernkarte (`inhalte/plan/regelbezug-lernkarten.json`). Alle Aufgaben tragen die Regel ihrer Lernkarte (auch dort, wo die Aufgabe daneben noch andere Regeln braucht). Die Fehlbild-Kennungen des Katalogs (`fb.*`) sind nicht vergeben (die Fehlbilder stehen als Beschreibung mit Rechnung in den JSON-Dateien).

**50 Aufgaben mit Regel, 5 ohne.**

## Verteilung

| Regel | Name | Aufgaben |
|---|---|---|
| `rr.potenz` | Potenzen | 20 |
| `rr.gegenrechnung` | Gegenrechnung | 10 |
| `rr.reihenfolge` | Reihenfolge beim Rechnen | 10 |
| `rr.ausmultiplizieren` | Ausmultiplizieren und Ausklammern | 5 |
| `rr.tauschen` | Tauschen, Klammern, Zusammenfassen | 5 |
| – (ohne Regel) |  | 5 |

## Hinweis zur Themenliste des Katalogs

Diese Regeln der Lernkarten stehen im Katalog nicht mit der Einheit in der Themenliste: `rr.gegenrechnung` (zahlen.rechengesetze.sach); `rr.gegenrechnung` (zahlen.rechengesetze.umkehraufgabe_mal). Sie wurden trotzdem vergeben, weil die Lernkarte sie so führt (Vorgabe der Prüfung); die Themenliste des Katalogs könnte um `zahlen.rechengesetze` ergänzt werden.

## Aufgaben ohne Regel (mit Begründung)

| Aufgabe | Einheit.Lernziel | Begründung |
|---|---|---|
| VT1A-046 | zahlen.rechengesetze.ueberschlag | Kein Eintrag im Regelkatalog trägt das Überschlagen und Runden (id.zahlen.buendeln betrifft den Stellenwert, nicht den Überschlag). |
| VT1A-047 | zahlen.rechengesetze.ueberschlag | Kein Eintrag im Regelkatalog trägt das Überschlagen und Runden (id.zahlen.buendeln betrifft den Stellenwert, nicht den Überschlag). |
| VT1A-048 | zahlen.rechengesetze.ueberschlag | Kein Eintrag im Regelkatalog trägt das Überschlagen und Runden (id.zahlen.buendeln betrifft den Stellenwert, nicht den Überschlag). |
| VT1A-049 | zahlen.rechengesetze.ueberschlag | Kein Eintrag im Regelkatalog trägt das Überschlagen und Runden (id.zahlen.buendeln betrifft den Stellenwert, nicht den Überschlag). |
| VT1A-050 | zahlen.rechengesetze.ueberschlag | Kein Eintrag im Regelkatalog trägt das Überschlagen und Runden (id.zahlen.buendeln betrifft den Stellenwert, nicht den Überschlag). |

## Zweifelsfälle

| Aufgabe | Einheit.Lernziel | gewählt | Bemerkung |
|---|---|---|---|

## Alle Aufgaben

| Aufgabe | Einheit.Lernziel | Regel |
|---|---|---|
| VT1A-001 | zahlen.potenzen_basis.schreibweise | `rr.potenz` |
| VT1A-002 | zahlen.potenzen_basis.schreibweise | `rr.potenz` |
| VT1A-003 | zahlen.potenzen_basis.schreibweise | `rr.potenz` |
| VT1A-004 | zahlen.potenzen_basis.schreibweise | `rr.potenz` |
| VT1A-005 | zahlen.potenzen_basis.schreibweise | `rr.potenz` |
| VT1A-006 | zahlen.potenzen_basis.quadrat | `rr.potenz` |
| VT1A-007 | zahlen.potenzen_basis.quadrat | `rr.potenz` |
| VT1A-008 | zahlen.potenzen_basis.quadrat | `rr.potenz` |
| VT1A-009 | zahlen.potenzen_basis.quadrat | `rr.potenz` |
| VT1A-010 | zahlen.potenzen_basis.quadrat | `rr.potenz` |
| VT1A-011 | zahlen.potenzen_basis.zehner | `rr.potenz` |
| VT1A-012 | zahlen.potenzen_basis.zehner | `rr.potenz` |
| VT1A-013 | zahlen.potenzen_basis.zehner | `rr.potenz` |
| VT1A-014 | zahlen.potenzen_basis.zehner | `rr.potenz` |
| VT1A-015 | zahlen.potenzen_basis.zehner | `rr.potenz` |
| VT1A-016 | zahlen.potenzen_basis.sach | `rr.potenz` |
| VT1A-017 | zahlen.potenzen_basis.sach | `rr.potenz` |
| VT1A-018 | zahlen.potenzen_basis.sach | `rr.potenz` |
| VT1A-019 | zahlen.potenzen_basis.sach | `rr.potenz` |
| VT1A-020 | zahlen.potenzen_basis.sach | `rr.potenz` |
| VT1A-021 | zahlen.rechengesetze.klammern | `rr.reihenfolge` |
| VT1A-022 | zahlen.rechengesetze.klammern | `rr.reihenfolge` |
| VT1A-023 | zahlen.rechengesetze.klammern | `rr.reihenfolge` |
| VT1A-024 | zahlen.rechengesetze.klammern | `rr.reihenfolge` |
| VT1A-025 | zahlen.rechengesetze.klammern | `rr.reihenfolge` |
| VT1A-026 | zahlen.rechengesetze.termaufbau | `rr.reihenfolge` |
| VT1A-027 | zahlen.rechengesetze.termaufbau | `rr.reihenfolge` |
| VT1A-028 | zahlen.rechengesetze.termaufbau | `rr.reihenfolge` |
| VT1A-029 | zahlen.rechengesetze.termaufbau | `rr.reihenfolge` |
| VT1A-030 | zahlen.rechengesetze.termaufbau | `rr.reihenfolge` |
| VT1A-031 | zahlen.rechengesetze.vorteil | `rr.tauschen` |
| VT1A-032 | zahlen.rechengesetze.vorteil | `rr.tauschen` |
| VT1A-033 | zahlen.rechengesetze.vorteil | `rr.tauschen` |
| VT1A-034 | zahlen.rechengesetze.vorteil | `rr.tauschen` |
| VT1A-035 | zahlen.rechengesetze.vorteil | `rr.tauschen` |
| VT1A-036 | zahlen.rechengesetze.verteilen | `rr.ausmultiplizieren` |
| VT1A-037 | zahlen.rechengesetze.verteilen | `rr.ausmultiplizieren` |
| VT1A-038 | zahlen.rechengesetze.verteilen | `rr.ausmultiplizieren` |
| VT1A-039 | zahlen.rechengesetze.verteilen | `rr.ausmultiplizieren` |
| VT1A-040 | zahlen.rechengesetze.verteilen | `rr.ausmultiplizieren` |
| VT1A-041 | zahlen.rechengesetze.umkehraufgabe_mal | `rr.gegenrechnung` |
| VT1A-042 | zahlen.rechengesetze.umkehraufgabe_mal | `rr.gegenrechnung` |
| VT1A-043 | zahlen.rechengesetze.umkehraufgabe_mal | `rr.gegenrechnung` |
| VT1A-044 | zahlen.rechengesetze.umkehraufgabe_mal | `rr.gegenrechnung` |
| VT1A-045 | zahlen.rechengesetze.umkehraufgabe_mal | `rr.gegenrechnung` |
| VT1A-046 | zahlen.rechengesetze.ueberschlag | – |
| VT1A-047 | zahlen.rechengesetze.ueberschlag | – |
| VT1A-048 | zahlen.rechengesetze.ueberschlag | – |
| VT1A-049 | zahlen.rechengesetze.ueberschlag | – |
| VT1A-050 | zahlen.rechengesetze.ueberschlag | – |
| VT1A-051 | zahlen.rechengesetze.sach | `rr.gegenrechnung` |
| VT1A-052 | zahlen.rechengesetze.sach | `rr.gegenrechnung` |
| VT1A-053 | zahlen.rechengesetze.sach | `rr.gegenrechnung` |
| VT1A-054 | zahlen.rechengesetze.sach | `rr.gegenrechnung` |
| VT1A-055 | zahlen.rechengesetze.sach | `rr.gegenrechnung` |
