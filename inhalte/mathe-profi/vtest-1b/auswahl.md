# vtest-1b – Auswahl der Lernziele (vor dem Schreiben der Aufgaben)

Runde „Verstehen in Tests“, Teil 1b (Kennungen `VT1B-001` ff.). Auftrag: `auftrag.md`. Nichts davon ist eingespielt; nur neue Dateien in diesem Ordner.
Je Einheit die Hälfte der **Pflicht**-Lernziele (`bewertung.lernziele_pflicht` in `inhalte/themen/<einheit>.json`, aufgerundet), je gewähltem Lernziel 6 Aufgaben (1 test, 2 korrektur, 3 sicherung).

## Abweichung von der Vorgabe (Zahl der Pflicht-Lernziele)

`terme.potenzgesetze` hat nur **2** Pflicht-Lernziele (`potenz_begriff`, `negativer_exponent`); `fehler_finden` ist dort Vertiefung (laut `inhalte/README.md`: „nicht testrelevant“). Auftragsregel: Hälfte der tatsächlichen Pflichtzahl, aufgerundet = **1** Lernziel (nicht 2). Alle anderen Zahlen stimmen mit der Vorgabe überein (`messen.flaechen_vielecke`: 7 Pflicht + Vertiefung `drachen_raute`, Hälfte aufgerundet = 4).
Folge: 16 Lernziele und **96** Aufgaben statt 17 und 102. Wird ein zweites Lernziel für `terme.potenzgesetze` gewünscht (dann `potenz_begriff`), ist das ein eigener kleiner Nachtrag.

## Auswahl

| Einheit | Lehrplan-Ort (laut Repo) | Pflicht | gewählt | Aufgaben |
|---|---|---|---|---|
| `bruch.prozent` | M6 3 Prozentrechnung | 6 | `prozentsatz`, `rabatt_aufschlag`, `verstehen` | 18 |
| `gleichungen.bruch` | M8 4 Bruchterme und Bruchgleichungen | 7 | `definitionsmenge`, `ueber_kreuz`, `scheinloesung`, `verhaeltnis` | 24 |
| `terme.potenzgesetze` | M6 1 Rationale Zahlen | 2 (+1 Vertiefung) | `negativer_exponent` | 6 |
| `zahlen.potenzen_zehner` | M6 1 Rationale Zahlen | 7 | `gross_wissenschaftlich`, `negativer_exponent`, `vorsilben_klein`, `vergleichen_pruefen` | 24 |
| `messen.flaechen_vielecke` | M6 2 Flächeninhalt und Volumen | 7 (+1 Vertiefung) | `parallelogramm`, `trapez`, `zusammengesetzt`, `verstehen` | 24 |

## Begründung je Lernziel

**bruch.prozent**
- `prozentsatz`: Hier steckt die Grundwert-Falle „Teil durch Ganzes, nicht umgekehrt“ und der Vergleich zweier Ganzer (Anteile statt absoluter Zahlen), also Begründen und Vergleichen statt Einsetzen.
- `rabatt_aufschlag`: Der Faktor 100 % ± p % und die Frage, welche Größe der Grundwert ist, lassen Umkehren (neuer Preis → alter Preis) und den Vergleich zweier Angebote mit Begründung zu.
- `verstehen`: Prozentaussagen prüfen (Prozent wovon? Änderung hin und zurück, Prozentpunkte) ist selbst ein Verstehens-Lernziel; die Aufgaben dazu müssen im Test hart genug sein.
- Nicht gewählt: `prozent_bedeutung` (Darstellungswechsel steckt teilweise in den gewählten), `prozentwert` und `grundwert` (Grundwert-Fallen kommen in `rabatt_aufschlag` und `verstehen` vor).

**gleichungen.bruch**
- `definitionsmenge`: Warum Nenner nicht 0 sein dürfen und was das für die Gleichung bedeutet (Parameter, Aufstellen aus einem Sachverhalt) ist Verstehen statt Nenner-gleich-0-Rechnen.
- `ueber_kreuz`: Verfahren wählen (über Kreuz nur bei je einem Bruch pro Seite), Fehler bei Summen finden, Rückwärts-Aufgaben (Parameter aus bekannter Lösung).
- `scheinloesung`: Kernverstehen der Einheit: Eine gerechnete Zahl ist erst nach der Prüfung gegen D eine Lösung; Begründen und Fehler richtigstellen.
- `verhaeltnis`: Aufstellen einer Verhältnisgleichung aus einem Sachverhalt (Mischung, Maßstab, Proportionalität) ist der typische Transfer.
- Nicht gewählt: `ein_bruch`, `hauptnenner` (reine Rechenverfahren, ihre Idee steckt in den gewählten) und `graphisch` (braucht eine Zeichnung; die App zeichnet Graphen, aber ohne Bild eindeutig zu bleiben ist hier unnötig riskant).

**terme.potenzgesetze**
- `negativer_exponent`: Die typischen Fehlvorstellungen (negative Hochzahl ≠ negative Zahl, Hoch 0 ist 1 und nicht 0, negative Basis in Klammern, Kehrbruch) lassen sich gut als Begründen, Fehler richtigstellen und Größenvergleich prüfen. `potenz_begriff` wird dabei mitgeprüft ((−2)⁴ gegen −2⁴), ist aber nicht eigenes Lernziel dieser Runde.

**zahlen.potenzen_zehner**
- `gross_wissenschaftlich`: Warum „15 · 10⁷“ nicht wissenschaftlich ist, Umschreiben und Rechnen mit Zehnerpotenzen, Größenordnung – Begründen und Fehler finden.
- `negativer_exponent`: Minus im Exponenten heißt klein, nicht negativ; Umkehren (n aus dem Wert) und Darstellungswechsel.
- `vorsilben_klein`: Einheiten umrechnen über Zehnerpotenzen (µ, n, m) ist Transfer auf Sachzusammenhänge und verlangt Umkehren (welche Vorsilbe passt?).
- `vergleichen_pruefen`: Größenordnungen vergleichen und einordnen („wie viel mal so groß?“) ist das Verstehens-Lernziel der Einheit.
- Nicht gewählt: `zehnerpotenz`, `vorsilben_gross`, `klein_wissenschaftlich` (Grundformen, ihre Einsicht steckt in den gewählten).

**messen.flaechen_vielecke** (Leitgedanke: Formeln logisch erklären können)
- `parallelogramm`: Warum die Höhe zählt und nicht die schräge Seite (Scherung/Umlegen eines Dreiecks), und dass die Fläche bei gleicher Grundseite und Höhe gleich bleibt.
- `trapez`: Zwei gleiche Trapeze ergeben ein Parallelogramm; Zerlegung in Dreiecke; Mittellinie als Mittelwert von a und c.
- `zusammengesetzt`: Zerlegen oder Ergänzen und zwei Wege vergleichen; Figur nur in Worten/Koordinaten.
- `verstehen`: Selbst das Verstehens-Lernziel (Herleitungen, Fehlvorstellungen, Vergleiche ohne Rechnen).
- Nicht gewählt: `dreieck` (die Einsicht „zwei gleiche Dreiecke ergeben ein Parallelogramm“ steckt in `parallelogramm` und `verstehen`), `rueckwaerts` (Umkehren kommt als Aufgabenform in jedem gewählten Lernziel vor), `oberflaeche` (Netze brauchen Bilder).
