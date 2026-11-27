# Fachwörter: Summe · Differenz · Produkt · Quotient – Wort in Term übersetzen

Stand 27.11.2026. Nur Inhalte. **Nichts ist eingespielt.** Erzeugt und geprüft von `bauen.py` (endet mit „OK“).
Zeichen: **[G]** gesichert (gezählt oder vom Programm geprüft), **[M]** meine Einschätzung.

## Warum diese Lieferung

**[G] Gemessen im Bestand:**

| Lernkarte | Thema (Flug) | Aufgaben | davon mit Fachwort | davon **Wort → Term** |
|---|---|---|---|---|
| `uebersetzen` | `terme.aufstellen` (a2, Klasse 6/7) | 36 | 27 | **24** – gut abgedeckt |
| `termaufbau` | `zahlen.rechengesetze` (z1, Klasse 5) | 42 | 12 | **3** – alle drei als Auswahl, alle auf Stufe 2 |

Die übrigen neun Aufgaben mit Fachwort in `termaufbau` lauten „Berechne die Summe aus 27 und 15“ – dort ist das Wort eine Vokabel, kein Ansatz.

**[M] Der Befund ist also nicht „der Bestand kennt die Fachwörter nicht“** – er kennt sie, aber in `terme.aufstellen`, und dieser Flug steht auf Platz 14 der Route von Kind 1. **Im Flug, der gerade läuft (`z1`), kann ein Kind die Übersetzung Wort → Term nur dreimal üben, und jedes Mal durch Ankreuzen.** Bei Auswahl kann man rückwärts prüfen oder raten; einen Term aus Worten selbst bauen muss man nie.

## Was hier liegt

`termaufbau.json` – **13 Aufgaben** für `zahlen.rechengesetze`, Lernkarte `termaufbau`, Teilfähigkeit `terme`.
Stufen 4 / 6 / 3. Antwortformen: 5 Lücken, 4 Zahl, 4 Auswahl – also **neun Aufgaben, in denen das Kind selbst schreibt**.

Schwerpunkt ist nicht die Vokabel, sondern die **Reihenfolge und die Klammer**:

- „die Differenz aus 5 und 12“ ist 5 − 12, nicht 12 − 5 (FW-01, FW-03, FW-12),
- „subtrahiere … **von** 20“ dreht die Reihenfolge um (FW-06, FW-07),
- „das Dreifache **der Summe**“ braucht eine Klammer, sonst kommt etwas anderes heraus (FW-09),
- und rückwärts: aus einem Term den Satz finden (FW-08) und Zahlen so einsetzen, dass ein Wert herauskommt (FW-13).

## Geprüft [G]

- 19 Rechnungen zweifach nachgerechnet (Feld `c` mit dem Rechner aus `tools/inhalt_pruefen.py`, zweiter Weg im Programm).
- 27 Fehlbilder beschrieben, 6 mit Kennung aus `kennungen.json`.
- `tools/inhalt_pruefen.py` an einer Kopie von `zahlen.rechengesetze.json`: vorher und nachher kein Fehler.
- Kein Aufgabentext steht wörtlich im Bestand.
- Keine Lücke hinter einem Komma; keine Schablone enthält einen Kleinbuchstaben (sonst würde die App sie als Term-Vorlage mit freier Eingabe lesen – nachgesehen in `lernen.js`, `lernIstTermVorlage`).
- Bei den Auswahl-Aufgaben liegt die richtige Antwort auf wechselnden Plätzen.

## Nicht geprüft

- Kein Kind hat die Aufgaben gerechnet; die Stufen sind Einschätzungen.
- Ob der Bestand eine inhaltlich gleiche Aufgabe mit anderen Worten enthält (nur wörtlicher Vergleich).
- Ob die Schablonen `□ : □` und `(□ − □) · (□ + □) = □` am Handy gut aussehen – die Form ist nachgesehen, das Bild nicht.

## Annahmen

- `id.algebra.term` ist die passende Regel-Kennung für die Übersetzung; wo die Klammer oder die Reihenfolge die Hürde ist, steht `rr.reihenfolge`.
- Negative Zahlen sind in `z1` erlaubt, weil der Flug `zahlen.ganz` enthält.
