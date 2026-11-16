# Postfach daten-klassen (Elfte Runde, D1: Klassen-Zuordnung prüfen)

Ergebnis: `inhalte/pruefung/klassen/vorschlag.md`. Neueste Meldung oben.

## 2026-11-16 06:10 – FERTIG – Abschlussbericht daten-klassen (D1)
Vorschlag liegt in `inhalte/pruefung/klassen/vorschlag.md`. Er muss vor D2 von Sebastian freigegeben werden.

**Teil 1 – 16 Themen ohne `lehrplan_gym`:** 13 bleiben, 2 sollen auf Klasse 10, 1 ohne Beleg.
| Thema | heute | Vorschlag | Lernbereich |
|---|---|---|---|
| geometrie.winkel | 5 | bleibt 5, Titel „Mit Winkeln rechnen“ | M5 2 (Winkelsätze wären M7 2.2) |
| geometrie.ortslinien | 5 | bleibt 5 | M5 2 |
| zahlen.potenzen_zehner | 6 | bleibt 6 | M5 3.1 / M6 1.4 |
| bruch.dezimal | 6 | bleibt 6 | M6 1.2 |
| zahlen.intervalle | 8 | kein Beleg gefunden, vorläufig 8 | – |
| funktionen.grundbegriffe | 8 | bleibt 8 | M8 1 / M8 3 |
| raum.schraegbilder | 8 | **ändern auf 10** | M8 7 / M10 5 |
| stochastik.simulation | 8 | **ändern auf 10** | M8 5 / M10 2 |
| zahlen.wurzeln_basis | 9 | bleibt 9 | M9 1 / M9 5 |
| zahlen.reell | 9 | bleibt 9 | M9 1 |
| trigo.pythagoras | 9 | bleibt 9 | M9 6 |
| trigo.rechtwinklig | 9 | bleibt 9 | M9 7.1 |
| abbildungen.kongruenz | 7 | bleibt 7 | M7 2.1 |
| gleichungen.einfach | 5 | bleibt 5 | M5 1.2 / M5 3.1 |
| gleichungen.linear | 7 | bleibt 7 | M7 3 |
| groessen.indirekt | 8 | bleibt 8 | M8 3 |

**Teil 2 – 13 Orte:** 3 Umzüge (Zehnerpotenzen Rom → Paris; lineare Gleichungen Delhi → Samarkand; Ortslinien Alexandria → Kairo). 10 Orte bekommen eine neue Klasse: Vancouver 8, Teheran 7, Delhi 8, Marrakesch 7, Timbuktu 5, Cusco 8, Rio 5, Brasília 10, Santiago 10, Adelaide 6. Kein neuer Ort nötig.
Nachgerechnet (Skript über `orte.json` + `themenliste.json`, mit allen Änderungen): Danach hat keiner der 13 Orte mehr einen Widerspruch.

**Zusatzfunde:**
- New York (7) mit „Zinsen“ (Klasse 6 laut quelle.md) ist ein 14. Widerspruch. Das Thema fehlt in themenliste.json.
- 4 Themen mit Ort fehlen in themenliste.json: zahlen.natuerlich, zahlen.teilbarkeit, terme.umformen, finanzen.zinsen.
- 17 Orte haben Flüge ohne Gymnasium-Klasse.

**Entscheidungen für Sebastian (6):** Ort für neuen Flug „Winkelsätze“ Kl. 7 · zwei Themen auf 10 · Simulation 8 oder 10 · Intervalle/Ungleichungen ohne Beleg · Orte zusammenlegen oder nicht · Vertiefung kennzeichnen (App-Wunsch).

**Quellen und Vorbehalte:** LehrplanPLUS Gym Mathematik 5, 6, 7, 9, 10 (lehrplanplus.bayern.de). Klasse 8 über den Lehrplantext im ISB-Dokument von 2021, weil die Lehrplanseite nicht abrufbar war. Die Seiten wurden über ein Werkzeug gelesen, das den Text zusammenfasst. Kürzel und Kernaussagen sind belegt, einzelne Sätze sind nicht wörtlich gegengeprüft.

Nicht angefasst: themenliste.json, Generatoren, Datenbank, App-Code, Tests. Kein Merge.

## 2026-11-16 05:25 – STATUS
Gestartet. Zweig daten-klassen von lernen-app (aea5ee3) angelegt. Unterlagen aus pruefung-kinderansicht gelesen: UMBAU-AUFTRAG.md, bericht.md B8/Abschnitt 7, orte.json. Die 13 Orte mit `themenliste.json` nachgerechnet; die Zählung stimmt.
