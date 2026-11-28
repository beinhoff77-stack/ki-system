# vtest-1b – Auswahl der Lernziele

Runde „Verstehen in Tests“, Teil 1b (Kennungen `VT1B-001` bis `VT1B-119`). Auftrag: `auftrag.md`. Nichts davon ist eingespielt; nur neue Dateien in diesem Ordner.
Regel (verbindlich laut Koordination): je Einheit ⌈n/2⌉ Lernziele, n = **alle** Lernziele der Einheit (`lz` in `inhalte/plan/rollend-einheiten.json`); je gewähltem Lernziel 7 Aufgaben (1 test, 3 korrektur, 3 sicherung). Ergebnis: 3 + 4 + 2 + 4 + 4 = 17 Lernziele, **119** Aufgaben. (Die frühere Fassung dieser Datei zählte nur die Pflicht-Lernziele und kam auf 16 Lernziele und 96 Aufgaben; das ist überholt.)

## Auswahl und Abgleich mit dem Vorschlag (`inhalte/mathe-profi/vtest-1/auswahl.json`)

| Einheit | Lernziele der Einheit (n) | gewählt | Vorschlag | Abweichung |
|---|---|---|---|---|
| `bruch.prozent` | 6 (prozent_bedeutung, prozentwert, prozentsatz, grundwert, rabatt_aufschlag, verstehen) | `prozentsatz`, `rabatt_aufschlag`, `verstehen` | `prozentwert`, `grundwert`, `verstehen` | ja, 2 von 3 |
| `gleichungen.bruch` | 7 | `definitionsmenge`, `ueber_kreuz`, `scheinloesung`, `verhaeltnis` | `definitionsmenge`, `ueber_kreuz`, `scheinloesung`, `graphisch` | ja, 1 von 4 |
| `terme.potenzgesetze` | 3 | `negativer_exponent`, `fehler_finden` | gleich | nein |
| `zahlen.potenzen_zehner` | 7 | `gross_wissenschaftlich`, `negativer_exponent`, `vorsilben_klein`, `vergleichen_pruefen` | gleich | nein |
| `messen.flaechen_vielecke` | 8 | `dreieck`, `rueckwaerts`, `zusammengesetzt`, `verstehen` | gleich | nein |

## Begründung der Abweichungen

- `bruch.prozent`: Die Aufgaben zu `prozentsatz` (Bezugsgröße, Prozentpunkte gegen Prozent, Vergleich zweier Anteile) und `rabatt_aufschlag` (Faktor, Umkehren auf den alten Preis, zwei Änderungen hintereinander) waren bereits geschrieben und tragen die Denkfiguren des Vorschlags (Umkehren, Fehler-Detektiv, Brücke) mit. `prozentwert` und `grundwert` kommen als Umkehr-Aufgaben in `rabatt_aufschlag` und `verstehen` vor. Folge: Das Auswahlmuster ist RRVRVV, das Prüfwerkzeug meldet „nicht abwechselnd“ nur als Hinweis; wer es beheben will, tauscht `prozentsatz` gegen `grundwert` und lässt `prozentwert` als drittes Lernziel schreiben.
- `gleichungen.bruch`: `graphisch` verlangt ein Bild; ohne Bild ist eine Aufgabe dazu nur eindeutig, wenn beide Funktionsterme angegeben sind, und damit wäre sie wieder Rechnen. Stattdessen `verhaeltnis`: Aufstellen einer Verhältnisgleichung aus einem Sachverhalt, Fehler im Ansatz, Aufteilen im Verhältnis. Das Muster VRVRVVR bleibt abwechselnd genug (kein RR, kein VVV).
- `messen.flaechen_vielecke`: Der Vorschlag wurde übernommen; die frühere eigene Wahl (`parallelogramm`, `trapez`) entfällt. Die Leitgedanken (zwei Dreiecke ergeben ein Parallelogramm, die Höhe und nicht die schräge Seite, Zerlegen gegen Ergänzen) stecken in `dreieck`, `zusammengesetzt` und `verstehen`.

## Lehrplan-Orte (laut `inhalte/themenliste.json`, am Repo nicht weiter belegbar)

`bruch.prozent`: M6 3 Prozentrechnung. `gleichungen.bruch`: M8 4 Bruchterme und Bruchgleichungen. `terme.potenzgesetze`, `zahlen.potenzen_zehner`: M6 1 Rationale Zahlen. `messen.flaechen_vielecke`: M6 2 Flächeninhalt und Volumen. Der Lehrplanbezug jeder Aufgabe beginnt mit diesem Lernbereich. Offen: ob negative Exponenten und die wissenschaftliche Schreibweise im bayerischen Gymnasium schon in M6 1 oder erst später stehen, konnte ohne Zugriff auf den Lehrplantext nicht belegt werden; das sollte die Vorprüfung klären.

## Begründung je Lernziel (Denkfiguren)

**bruch.prozent**: `prozentsatz` (Bezugsgröße, Prozentpunkte, Kreisdiagramm, Fehler beim Teil-durch-Ganzes), `rabatt_aufschlag` (Bezugspreis, Faktor, hintereinander ausgeführte Änderungen, zwei Angebote), `verstehen` (50 % billiger heißt 100 % teurer, 200 % mehr, Anteil vom Anteil, Gegenbeispiel mit Klassengrößen).
**gleichungen.bruch**: `definitionsmenge` (Begründen, Parameter, Sachsituation, Menge aus mehreren Nennern), `ueber_kreuz` (wann erlaubt, zwei Wege, Parameter, Fehler beim Ausmultiplizieren), `scheinloesung` (begründen, Bedingung für Scheinlösung, Identitäten), `verhaeltnis` (Schatten, Foto, Aufteilen, Fehler beim Kreuzen).
**terme.potenzgesetze**: `negativer_exponent` (Muster fortsetzen, Größen ordnen, Faktor bei Exponentenänderung), `fehler_finden` (Zeilen mit Fehler, Gegenbeispiel, Klammer bei negativer Basis, Hoch 0).
**zahlen.potenzen_zehner**: `gross_wissenschaftlich` (Bedingung 1 ≤ a < 10, Verschiebefehler, Ziffernzahl), `negativer_exponent` (Stellen statt Nullen, Vergleich), `vorsilben_klein` (mm gegen µm, Umrechnungskette), `vergleichen_pruefen` (Vorfaktor und Exponent zugleich, gleiche Zahl in anderer Schreibweise).
**messen.flaechen_vielecke**: `dreieck` (Höhe außerhalb, Koordinaten, zwei Wege, Verschieben der Spitze), `rueckwaerts` (kein Winkel nötig, Trapezhöhe, Gleichung aufstellen, Umstellfehler), `zusammengesetzt` (Zerlegen gegen Ergänzen, Pavillon, falsche Rechnung erkennen), `verstehen` (Faktoren statt Summen, Prozent, flächengleiche Figuren, Verdoppeln des Quadrats).
