# Postfach lehrplan-lb (Bau-Auftrag LB, Paket LB-4)

Neueste Meldung oben.

## 2026-11-20 – FERTIG: LB-4

Zweig `lehrplan-lb` (von `lernen-app`, Commit 752acf0). Drei Commits, je Schulart einer: Gymnasium 2d24925 · Realschule 908bb12 · IB 34cbe67. Nur `inhalte/themenliste.json` geändert (+ dieser Bericht). Kein App-Code, keine Datenbank, kein Merge. Klassen nicht geändert.

### Kurz
- **Neu in `themenliste.json`:** `lernbereich.gym_by` (71 Themen), `reihenfolge.rs_by` + `lernbereich.rs_by` + `lehrplan_rs` (76 Themen), `reihenfolge.ib_myp` + `lernbereich.ib_myp` + `lehrplan_ib` (84 Themen). Jedes Thema mit Klasse in einer Schulart hat dort Reihenfolge und Lernbereich. Themen ohne Klasse in einer Schulart haben dort keinen Eintrag. `reihenfolge.gym_by`, `lehrplan_gym`, `lehrplan_andere` und `klasse` sind unverändert.
- **Eingefügt, nicht neu formatiert:** Ein Skript hat nur Zeilen eingefügt. Der Diff zeigt neue Zeilen und Kommas am Ende der jeweils vorherigen Zeile (69 so geänderte Zeilen). Geprüft per Skript: Alle alten Werte sind gleich, neu ist nur das Erwartete. `python3 -I tools/inhalt_pruefen.py --alle` ergibt 116 × OK, Rückgabewert 0.
- **Selbstprüfung:** Alles lückenlos und eindeutig. Realschule Klasse 7 hat 18 Themen. **Ein Befund:** Gymnasium Klasse 6 – der Lernbereich M6 1 wird durch die bestehende `reihenfolge.gym_by` unterbrochen (siehe unten, Vorschlag). Den Vorschlag habe ich nicht umgesetzt, weil der Auftrag die Gym-Reihenfolge sperrt.
- **Für Sebastian zu entscheiden:** die Gym-6-Reihenfolge (1 Punkt), 9 Vorschläge zu Klassen (Liste unten, nichts geändert) und ob IB-Überschriften englisch bleiben.

### So habe ich zugeordnet (Festlegungen)
- **Lernbereich = oberste Ebene des Lehrplans**, z. B. „M8 1 Funktion und Term“, „M9 7 Trigonometrie“ (nicht 7.1/7.2). So passt jede Überschrift zu einem zusammenhängenden Block. Die Unterkapitel stehen weiter in `lehrplan_gym`.
- **Realschule:** Die Überschrift hat dieselbe Form wie beim Gymnasium: „M7 2 Parallelverschiebung“. Im Lehrplan heißt sie „M7 Lernbereich 2: Parallelverschiebung“. Ab Klasse 7 gilt **Gruppe I** (Wahlpflichtfächergruppe I). Die Reihenfolge folgt der Nummer des Lernbereichs. **Die Reihenfolge innerhalb eines Lernbereichs gibt der Lehrplan nicht vor.** Ich habe sie nach der Reihenfolge der Stichworte im Lehrplan und nach den Voraussetzungen der Etappen gesetzt (Annahme). Wo eine Etappe Stoff eines späteren Lernbereichs braucht, steht das in der Spalte „Beleg“.
- **IB:** Das MYP schreibt **weder Jahr noch Reihenfolge** vor. Der Guide gliedert in vier Zweige und in Stufen (MYP 1–3, MYP 4–5 Standard/Extended, Enrichment). Ich habe so festgelegt:
  - `lernbereich.ib_myp` = „MYP <Jahr> <Zweig>“. Der Zweig steht englisch wie im Guide, dahinter auf Deutsch, z. B. „MYP 4 Thinking with models (Funktionen und Modelle)“.
  - `reihenfolge.ib_myp` folgt den Zweigen in der Reihenfolge des Guides (Zahl/Algebra → Modelle → Geometrie → Daten). Innerhalb eines Zweigs habe ich nach Voraussetzungen sortiert. Die **ganze IB-Reihenfolge ist Annahme**.
  - Jeder Eintrag in `lehrplan_ib` beginnt mit der Stufe im Framework, z. B. „MYP 4–5 Extended: …“.
- **`lehrplan_rs` / `lehrplan_ib`:** kurz und in eigenen Worten. „kein Beleg“ und „Annahme“ stehen dort, wo der Lehrplan das Thema nicht (vollständig) nennt.
- **Die 10 aufgelösten Themen** (u. a. `groessen.verhaeltnisse`, `mengen.grundbegriffe`, `funktionen.scharen`, `funktionen.folgen`, `abbildungen.vektoren`) stehen noch mit Klasse in der Themenliste. Sie haben deshalb auch Einträge bekommen, sonst wären die Nummern lückenhaft. Die App zeigt sie laut Auftrag nirgends. Die Nummern bleiben trotzdem gültig, weil die App ohnehin nur sortiert.

### Selbstprüfung (Skript, Ausgabe unverändert)
```
gym_by  Kl.  5: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
gym_by  Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: NEIN (3 Überschriften)
gym_by  Kl.  7:  9 Themen · Nummern 1–9 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
gym_by  Kl.  8: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl.  9: 14 Themen · Nummern 1–14 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
gym_by  Kl. 10:  9 Themen · Nummern 1–9 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
rs_by   Kl.  5: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  6: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (6 Überschriften)
rs_by   Kl.  7: 18 Themen · Nummern 1–18 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (7 Überschriften)
rs_by   Kl.  8:  7 Themen · Nummern 1–7 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
rs_by   Kl.  9: 17 Themen · Nummern 1–17 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (8 Überschriften)
rs_by   Kl. 10: 11 Themen · Nummern 1–11 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (5 Überschriften)
ib_myp  Kl.  1: 15 Themen · Nummern 1–15 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  2: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (3 Überschriften)
ib_myp  Kl.  3: 12 Themen · Nummern 1–12 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  4: 27 Themen · Nummern 1–27 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
ib_myp  Kl.  5: 18 Themen · Nummern 1–18 lückenlos/eindeutig: ja · Lernbereiche zusammenhängend: ja (4 Überschriften)
Realschule Klasse 7: 18 Themen (soll 18)
FEHLER:
- gym_by 6: Lernbereich mehrfach unterbrochen: ['M6 1 Rationale Zahlen', 'M6 2 Flächeninhalt und Volumen', 'M6 1 Rationale Zahlen', 'M6 3 Prozentrechnung, Daten und Diagramme']
```

### Befund: Gymnasium Klasse 6 – Lernbereich M6 1 unterbrochen
Die heutige `reihenfolge.gym_by`: 1 `bruch.brueche` · 2 `bruch.dezimal` · 3 `bruch.rechnen` (M6 1) · 4 `messen.flaechen_vielecke` · 5 `messen.volumen` (M6 2) · 6 `zahlen.potenzen_zehner` · 7 `terme.potenzgesetze` (M6 1) · 8–11 (M6 3). Die Überschrift „M6 1 Rationale Zahlen“ käme also zweimal.
**Vorschlag (nicht umgesetzt):** `zahlen.potenzen_zehner` → 4, `terme.potenzgesetze` → 5, `messen.flaechen_vielecke` → 6, `messen.volumen` → 7. Das passt zum Lehrplan, weil negative Exponenten in M6 1.4 stehen und M6 2 danach kommt. Quelle: G6, GSP.

### Vorschläge zu Klassen (nichts geändert)
| Thema | Schulart | heute | Vorschlag | Quelle / Grund |
|---|---|---|---|---|
| `daten.boxplot` | RS | 7 | keine RS-Klasse oder Vertiefung | R7, M7 8: Mittelwert, Zentralwert, Modalwert, Spannweite. Quartile und Boxplot kommen in RS 7 (Gruppe I) nicht vor. Die Zusammenfassung für RS 5–10 vom 17.11. hat sie auch nicht gefunden. |
| `funktionen.gebrochen` | RS | – | 10 (Annahme) | R10, M10 3: Potenzfunktionen y = a(x + b)^c + d mit Asymptoten. Die Hyperbel ist der Fall c = −1. |
| `funktionen.linear` | IB | 3 | 4 | IBG: „Thinking with models“ gilt für MYP 1–3 als nicht altersgemäß; lineare Funktionen sind Standard (MYP 4–5). Das Lehrwerk Haese hat sie in Jahr 3 (Bericht vom 17.11.). |
| `stochastik.kombinatorik` | IB | 2 | 5 oder keine IB-Klasse | IBG: Zählprinzipien, Permutationen und Fakultät stehen nur im Enrichment. |
| `mengen.grundbegriffe` | IB | 3 | 4 | IBG: Mengen bis zu drei Mengen = Extended (MYP 4–5). Das Thema ist aufgelöst – nur von Belang, wenn es zurückkommt. |
| `stochastik.simulation` | IB | 2 | 4 (Annahme) | IBG: Theoretische und experimentelle Wahrscheinlichkeit stehen unter Standard (MYP 4–5). Die Spalte war in der Abschrift aber nicht sicher lesbar. |
| `raum.schraegbilder` | IB | 4 | 5 oder keine IB-Klasse | IBG: Dreidimensionale Koordinatengeometrie steht nur im Enrichment. Für Rotationskörper und windschiefe Geraden gibt es keinen Beleg. |
| `abbildungen.matrizen` | IB | 5 | keine IB-Klasse (Annahme) | IBG 2020: Matrizen nicht gefunden, Vektoren nur Enrichment. |
| `sonder.logik` | IB | 4 | keine IB-Klasse (Annahme) | IBG: Aussagenlogik nicht gefunden. |

Hinweis zu IB: In der Abschrift des Framework stehen Terme und Gleichungen (Algebra) unter „MYP 4–5 Standard“. Das betrifft `terme.aufstellen`, `gleichungen.einfach` (MYP 1) und `gleichungen.linear` (MYP 2). Das Werkzeug warnt selbst, dass die Spalten der Tabelle verschoben sein können. Ich schlage deshalb keine Änderung vor und habe die Stufe als „Annahme“ markiert. Vor einer Entscheidung bitte im gedruckten Guide (S. 23–24) nachsehen.

### Abweichungen der Gruppe II/III (Realschule, nur Hinweis)
Die App hat nur ein Feld `rs_by`. Alle Angaben oben gelten für Gruppe I. Gruppe II/III weicht so ab:
- **Klasse 8:** Lernbereich 1 heißt „Dreiecke und Vierecke“ (Dreieckskonstruktion erst hier, Gruppe I: M7 3). Lineare Funktionen erst in Klasse 9, Lernbereich 5 (Quellen: Mathe.Logo 8 II/III, nur Titel aus der Suche; RSP9).
- **Klasse 9:** Lernbereiche Reelle Zahlen, Zentrische Streckung, Rechtwinklige Dreiecke, Lineare Funktionen, Systeme linearer Gleichungen, Daten und Zufall. Kreis, Raumgeometrie und quadratische Funktionen fehlen dort (Quelle RSP9).
- **Klasse 10:** Lernbereich 3 „Exponentialfunktionen, Logarithmen“ und Lernbereich 4 „Quadratische Funktionen und quadratische Gleichungen“. Es gibt keinen Lernbereich „Abbildungen“ und keine Potenzfunktionen (Quelle RSP10).
- Betroffen sind also vor allem `funktionen.linear` (II/III: 9), `funktionen.quadratisch`, `gleichungen.quadratisch` und `raum.pyramide_kegel_kugel` (II/III: 10). Dazu kommen `abbildungen.matrizen`, `zahlen.rationale_exponenten`, `funktionen.potenz`, `gleichungen.potenz` und `funktionen.umkehr`: Für sie gibt es in II/III keinen Beleg. Stand 17.11. (`vorschlag-rsib.md`, Spalte II/III); heute nur für 9 und 10 neu geprüft.

### Grenzen (bitte lesen)
- Das Abruf-Werkzeug **fasst Seiten zusammen**. Nummern, Titel und Stichworte der Lernbereiche sind stimmig und decken sich mit mehreren Quellen. Nicht jeder Satz ist wörtlich nachgeprüft.
- **Nicht abrufbar heute** (das Werkzeug verlangte eine Freigabe, die niemand erteilen konnte): die LehrplanPLUS-Seiten Gymnasium 8 und 9 und Realschule 8 und 9 (wpfg1). Ersatz:
  - Gym 8/9: Lernbereiche aus dem ISB-Dokument „Schwerpunktsetzungen 5–10“ (2022). Die Inhalte je Lernbereich stammen aus den ISB-Schwerpunktsetzungen 8 und 9 (2021). Diese geben den Lehrplantext nur auszugsweise wieder.
  - RS 8/9 (Gruppe I): Titel und Inhalte aus den Stoffverteilungsplänen „Mathe.Logo 8 I / 9 I“ (C.C. Buchner). Das ist eine **Verlagsquelle**, keine amtliche. Die Titel von RS 9 decken sich mit dem ISB-Dokument RSP9.
  - Ich habe nichts aus dem Gedächtnis ergänzt. Wo ich den Bericht vom 17.11. nutze, steht das dabei.
- IB: Der Guide liegt nur als Kopie einer Schule vor (wottonhouseschool.co.uk). Die Spaltenzuordnung der Framework-Tabelle ist laut Werkzeug „stellenweise unsicher“, vor allem bei „Thinking with models“ und „Spatial reasoning“.

### Tabellen je Schulart und Klasse
Spalte „Beleg“: **belegt** = der Inhalt steht in den Stichworten des Lernbereichs der Quelle. **Annahme** = nicht wörtlich gefunden oder Zuordnung gewählt. Die Reihenfolge innerhalb eines Lernbereichs ist immer Annahme (siehe oben).

### Gymnasium (nur `lernbereich.gym_by`; `reihenfolge.gym_by` unverändert)

**Gymnasium Klasse 5** – Quelle G5 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.natuerlich` | M5 1 Natürliche und ganze Zahlen – Addition und Subtraktion | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `zahlen.ganz` | M5 1 Natürliche und ganze Zahlen – Addition und Subtraktion | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `geometrie.grundbegriffe` | M5 2 Geometrische Figuren und Lagebeziehungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `geometrie.ortslinien` | M5 2 Geometrische Figuren und Lagebeziehungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `geometrie.winkel` | M5 2 Geometrische Figuren und Lagebeziehungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `zahlen.rechengesetze` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `zahlen.potenzen_basis` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `zahlen.teilbarkeit` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Teilbarkeitsregeln, Primfaktorzerlegung in M5 3.1) – bisher Annahme |
| 9 | `stochastik.kombinatorik` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt (Zählprinzip, Baumdiagramm in M5 3.1) – bisher Annahme |
| 10 | `gleichungen.einfach` | M5 3 Natürliche und ganze Zahlen – Multiplikation und Division | belegt: a + x = b in M5 1.2, a · x = b in M5 3.1 – zu M5 3 gesetzt |
| 11 | `groessen.einheiten` | M5 4 Größen und ihre Einheiten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 12 | `groessen.proportional` | M5 4 Größen und ihre Einheiten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 13 | `messen.flaechen` | M5 4 Größen und ihre Einheiten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 14 | `messen.koerper_berechnung` | M5 4 Größen und ihre Einheiten | belegt für Oberfläche (M5 4.2); Volumen steht erst in M6 2.2 |

**Gymnasium Klasse 6** – Quelle G6 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `bruch.brueche` | M6 1 Rationale Zahlen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `bruch.dezimal` | M6 1 Rationale Zahlen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `bruch.rechnen` | M6 1 Rationale Zahlen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `messen.flaechen_vielecke` | M6 2 Flächeninhalt und Volumen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `messen.volumen` | M6 2 Flächeninhalt und Volumen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `zahlen.potenzen_zehner` | M6 1 Rationale Zahlen | belegt (negative Exponenten in M6 1.4) |
| 7 | `terme.potenzgesetze` | M6 1 Rationale Zahlen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `bruch.prozent` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `finanzen.zinsen` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 10 | `daten.darstellen` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 11 | `daten.kennwerte` | M6 3 Prozentrechnung, Daten und Diagramme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

**Gymnasium Klasse 7** – Quelle G7 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `terme.aufstellen` | M7 1 Terme mit Variablen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `terme.umformen` | M7 1 Terme mit Variablen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `abbildungen.kongruenz` | M7 2 Geometrische Figuren: Symmetrie und Winkel | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `geometrie.winkelsaetze` | M7 2 Geometrische Figuren: Symmetrie und Winkel | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `gleichungen.linear` | M7 3 Lineare Gleichungen und Vertiefung der Prozentrechnung | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `bruch.prozent_grundwert` | M7 3 Lineare Gleichungen und Vertiefung der Prozentrechnung | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `daten.boxplot` | M7 4 Kenngrößen von Daten | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `geometrie.konstruktion` | M7 5 Kongruenz, besondere Dreiecke und Dreieckskonstruktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `geometrie.kreis` | M7 5 Kongruenz, besondere Dreiecke und Dreieckskonstruktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

**Gymnasium Klasse 8** – Quelle GSP8 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `funktionen.grundbegriffe` | M8 1 Funktion und Term | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `funktionen.linear` | M8 2 Lineare Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `zahlen.intervalle` | M8 2 Lineare Funktionen | Annahme: in M8 nicht gefunden; gesetzt zu M8 2, weil graphisch an Geraden gelöst |
| 4 | `gleichungen.ungleichungen` | M8 2 Lineare Funktionen | Annahme: in M8 nicht gefunden; zu M8 2 (graphisch an Geraden) |
| 5 | `groessen.indirekt` | M8 3 Elementare gebrochen-rationale Funktionen | belegt (y = a/x „indirekt proportional“ in M8 3) |
| 6 | `funktionen.gebrochen` | M8 3 Elementare gebrochen-rationale Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `terme.bruchterme` | M8 4 Bruchterme und Bruchgleichungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `gleichungen.bruch` | M8 4 Bruchterme und Bruchgleichungen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `gleichungen.formeln` | M8 4 Bruchterme und Bruchgleichungen | Annahme: in M8 nicht gefunden; zu M8 4 |
| 10 | `stochastik.grundbegriffe` | M8 5 Laplace-Experimente | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 11 | `gleichungen.lgs2` | M8 6 Lineare Gleichungssysteme | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 12 | `messen.kreisberechnung` | M8 7 Kreis und Zylinder | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 13 | `messen.koerper_darstellung` | M8 7 Kreis und Zylinder | belegt (Schrägbilder, Netze von Prismen/Zylindern in M8 7) |
| 14 | `messen.prisma_zylinder` | M8 7 Kreis und Zylinder | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

**Gymnasium Klasse 9** – Quelle GSP9 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.wurzeln_basis` | M9 1 Quadratwurzeln | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `zahlen.reell` | M9 1 Quadratwurzeln | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `funktionen.quadratisch` | M9 2 Quadratische Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `gleichungen.quadratisch` | M9 2 Quadratische Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `gleichungen.lgs3` | M9 2 Quadratische Funktionen | belegt (M9 2.2) |
| 6 | `stochastik.verknuepft` | M9 3 Wahrscheinlichkeit verknüpfter Ereignisse | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `abbildungen.aehnlichkeit` | M9 4 Ähnlichkeit und Strahlensatz | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `zahlen.rationale_exponenten` | M9 5 Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `funktionen.potenz` | M9 5 Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 10 | `gleichungen.potenz` | M9 5 Potenzfunktionen mit natürlichen Exponenten und Erweiterung des Potenzbegriffs | Annahme: xⁿ = c nicht wörtlich, folgt aus M9 5 (Wurzeln, Potenzbegriff) |
| 11 | `trigo.pythagoras` | M9 6 Satz des Pythagoras | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 12 | `trigo.rechtwinklig` | M9 7 Trigonometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 13 | `trigo.allgemein` | M9 7 Trigonometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 14 | `gleichungen.trig` | M9 7 Trigonometrie | Annahme: „Winkel zu Wert“ nicht wörtlich, Teil von M9 7.2 |

**Gymnasium Klasse 10** – Quelle G10 (+ GSP für die Titel)

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `funktionen.exponential_log` | M10 1 Exponentielles Wachstum und Logarithmus | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 2 | `gleichungen.exponential` | M10 1 Exponentielles Wachstum und Logarithmus | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 3 | `stochastik.mehrstufig` | M10 2 Zusammengesetzte Zufallsexperimente und stochastische Simulationen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 4 | `stochastik.simulation` | M10 2 Zusammengesetzte Zufallsexperimente und stochastische Simulationen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 5 | `funktionen.trig` | M10 3 Sinus- und Kosinusfunktion | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 6 | `funktionen.ganzrational` | M10 4 Ganzrationale Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 7 | `gleichungen.polynom` | M10 4 Ganzrationale Funktionen | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 8 | `raum.schraegbilder` | M10 5 Fortführung der Raumgeometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |
| 9 | `raum.pyramide_kegel_kugel` | M10 5 Fortführung der Raumgeometrie | belegt (Lehrplan-Stichworte des Lernbereichs, lehrplan_gym) |

### Realschule (Gruppe I ab Klasse 7)

**Realschule Klasse 5** – Quelle R5

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.natuerlich` | M5 1 Natürliche Zahlen | belegt |
| 2 | `zahlen.rechengesetze` | M5 1 Natürliche Zahlen | belegt M5 1.3; Etappen zu ·/: ganzer Zahlen = M5 2 (kommt im Lehrplan danach) |
| 3 | `zahlen.potenzen_basis` | M5 1 Natürliche Zahlen | belegt |
| 4 | `zahlen.teilbarkeit` | M5 1 Natürliche Zahlen | belegt |
| 5 | `stochastik.kombinatorik` | M5 1 Natürliche Zahlen | belegt |
| 6 | `zahlen.ganz` | M5 2 Ganze Zahlen | belegt |
| 7 | `geometrie.grundbegriffe` | M5 3 Geometrische Grundvorstellungen und Grundbegriffe | belegt |
| 8 | `geometrie.winkel` | M5 3 Geometrische Grundvorstellungen und Grundbegriffe | belegt |
| 9 | `messen.koerper_darstellung` | M5 3 Geometrische Grundvorstellungen und Grundbegriffe | belegt M5 3; Etappen zu Prismen-Netzen gehen darüber hinaus |
| 10 | `groessen.einheiten` | M5 4 Größen | belegt |
| 11 | `messen.flaechen` | M5 5 Umfang und Flächeninhalt ebener Figuren | belegt |
| 12 | `daten.darstellen` | M5 6 Auswertung von Daten | belegt |

**Realschule Klasse 6** – Quelle R6

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `bruch.brueche` | M6 1 Rationale Zahlen | belegt |
| 2 | `bruch.dezimal` | M6 1 Rationale Zahlen | belegt |
| 3 | `bruch.rechnen` | M6 1 Rationale Zahlen | belegt |
| 4 | `abbildungen.kongruenz` | M6 2 Achsenspiegelung und Symmetrie | belegt |
| 5 | `messen.flaechen_vielecke` | M6 3 Flächeninhalt ebener Figuren | belegt |
| 6 | `messen.volumen` | M6 4 Raumgeometrie | belegt |
| 7 | `messen.koerper_berechnung` | M6 4 Raumgeometrie | Annahme: Oberfläche = M6 3, Volumen = M6 4 – an das Ende von M6 4 gesetzt |
| 8 | `terme.aufstellen` | M6 5 Terme und Gleichungen | belegt |
| 9 | `gleichungen.einfach` | M6 5 Terme und Gleichungen | belegt |
| 10 | `groessen.proportional` | M6 6 Direkte Proportionalität | belegt |
| 11 | `bruch.prozent` | M6 6 Direkte Proportionalität | belegt |

**Realschule Klasse 7** – Quelle R7

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `terme.potenzgesetze` | M7 1 Potenzen | belegt |
| 2 | `zahlen.potenzen_zehner` | M7 1 Potenzen | belegt |
| 3 | `abbildungen.vektoren` | M7 2 Parallelverschiebung | belegt |
| 4 | `abbildungen.determinanten2` | M7 2 Parallelverschiebung | belegt |
| 5 | `geometrie.winkelsaetze` | M7 2 Parallelverschiebung | belegt |
| 6 | `geometrie.konstruktion` | M7 3 Dreiecke | belegt |
| 7 | `geometrie.ortslinien` | M7 5 Geometrische Ortslinien und Ortsbereiche | belegt |
| 8 | `geometrie.kreis` | M7 5 Geometrische Ortslinien und Ortsbereiche | belegt |
| 9 | `terme.umformen` | M7 6 Terme, Gleichungen und Ungleichungen | belegt (Terme vereinfachen); Etappe binomische Formeln = M8 4 |
| 10 | `gleichungen.linear` | M7 6 Terme, Gleichungen und Ungleichungen | belegt (ax + b = c); Etappen mit x auf beiden Seiten/Klammern = M8 4 |
| 11 | `zahlen.intervalle` | M7 6 Terme, Gleichungen und Ungleichungen | belegt |
| 12 | `gleichungen.ungleichungen` | M7 6 Terme, Gleichungen und Ungleichungen | belegt |
| 13 | `bruch.prozent_grundwert` | M7 7 Proportionalitäten | belegt |
| 14 | `finanzen.zinsen` | M7 7 Proportionalitäten | belegt |
| 15 | `groessen.indirekt` | M7 7 Proportionalitäten | belegt |
| 16 | `daten.kennwerte` | M7 8 Auswertung von Daten | belegt |
| 17 | `daten.boxplot` | M7 8 Auswertung von Daten | Annahme: Quartile/Boxplot im RS-Lehrplan nicht gefunden |
| 18 | `daten.stichproben` | M7 8 Auswertung von Daten | belegt |

**Realschule Klasse 8** – Quelle RML8

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `raum.schraegbilder` | M8 3 Raumgeometrie | belegt M8 3; Schrägbilder von Prismen/Pyramiden = M7 4 |
| 2 | `terme.quadratische_extreme` | M8 4 Terme, Gleichungen und Ungleichungen | belegt |
| 3 | `terme.bruchterme` | M8 5 Bruchterme und Bruchgleichungen | belegt |
| 4 | `gleichungen.bruch` | M8 5 Bruchterme und Bruchgleichungen | belegt |
| 5 | `funktionen.grundbegriffe` | M8 6 Funktionen | belegt |
| 6 | `funktionen.linear` | M8 6 Funktionen | belegt |
| 7 | `funktionen.scharen` | M8 6 Funktionen | teilweise: Parallelenscharen belegt (M8 6); Parabelscharen = M9 7 |

**Realschule Klasse 9** – Quelle RML9 · RSP9

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `zahlen.wurzeln_basis` | M9 1 Reelle Zahlen | belegt |
| 2 | `zahlen.reell` | M9 1 Reelle Zahlen | belegt |
| 3 | `gleichungen.reinquadratisch` | M9 1 Reelle Zahlen | belegt |
| 4 | `abbildungen.aehnlichkeit` | M9 2 Zentrische Streckung | belegt |
| 5 | `trigo.pythagoras` | M9 3 Rechtwinklige Dreiecke | belegt |
| 6 | `trigo.rechtwinklig` | M9 3 Rechtwinklige Dreiecke | belegt |
| 7 | `messen.kreisberechnung` | M9 4 Kreis | belegt |
| 8 | `messen.prisma_zylinder` | M9 5 Raumgeometrie | belegt |
| 9 | `raum.pyramide_kegel_kugel` | M9 5 Raumgeometrie | belegt |
| 10 | `gleichungen.lgs2` | M9 6 Systeme linearer Gleichungen | belegt |
| 11 | `funktionen.quadratisch` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt |
| 12 | `funktionen.transformation` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt (Parameter, Parabelscharen M9 7); andere Graphen = M10 2 |
| 13 | `gleichungen.quadratisch` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt |
| 14 | `gleichungen.wurzel` | M9 7 Quadratische Funktionen und quadratische Gleichungen | belegt |
| 15 | `stochastik.grundbegriffe` | M9 8 Daten und Zufall | belegt |
| 16 | `stochastik.verknuepft` | M9 8 Daten und Zufall | teilweise: Ereignis/Gegenereignis belegt; Additionssatz, bedingte WK kein Beleg |
| 17 | `stochastik.simulation` | M9 8 Daten und Zufall | belegt (Gesetz der großen Zahlen, Simulation); Monte-Carlo kein Beleg |

**Realschule Klasse 10** – Quelle R10 · RSP10

| Nr. | Thema | Lernbereich | Beleg |
|---|---|---|---|
| 1 | `trigo.allgemein` | M10 1 Trigonometrie | belegt |
| 2 | `funktionen.trig` | M10 1 Trigonometrie | belegt |
| 3 | `gleichungen.trig` | M10 1 Trigonometrie | belegt |
| 4 | `abbildungen.matrizen` | M10 2 Abbildungen | belegt |
| 5 | `zahlen.rationale_exponenten` | M10 3 Potenzen und Potenzfunktionen | belegt |
| 6 | `gleichungen.potenz` | M10 3 Potenzen und Potenzfunktionen | Annahme: aus „n-te Wurzel“ (M10 3) |
| 7 | `funktionen.potenz` | M10 3 Potenzen und Potenzfunktionen | belegt |
| 8 | `funktionen.umkehr` | M10 3 Potenzen und Potenzfunktionen | belegt M10 3 (auch M10 4); eine Etappe braucht Exponentialfunktionen (M10 4) |
| 9 | `funktionen.exponential_log` | M10 4 Exponentialfunktionen, Logarithmen und Logarithmusfunktionen | belegt |
| 10 | `gleichungen.exponential` | M10 4 Exponentialfunktionen, Logarithmen und Logarithmusfunktionen | belegt |
| 11 | `stochastik.mehrstufig` | M10 5 Daten und Zufall | belegt |

### IB MYP (Jahr = Klasse − 5)

**MYP 1** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.natuerlich` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 2 | `zahlen.rechengesetze` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 3 | `zahlen.potenzen_basis` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 4 | `zahlen.teilbarkeit` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 5 | `zahlen.wurzeln_basis` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 6 | `bruch.brueche` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 7 | `bruch.dezimal` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 8 | `bruch.prozent` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 9 | `terme.aufstellen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 10 | `gleichungen.einfach` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 11 | `geometrie.grundbegriffe` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 12 | `geometrie.winkel` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 13 | `messen.flaechen` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 14 | `messen.koerper_berechnung` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 15 | `daten.darstellen` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 |

**MYP 2** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.ganz` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 2 | `bruch.rechnen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 3 | `gleichungen.linear` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 4 | `groessen.verhaeltnisse` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 5 | `groessen.proportional` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 6 | `groessen.einheiten` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 7 | `geometrie.winkelsaetze` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 8 | `daten.stichproben` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 |
| 9 | `daten.kennwerte` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 |
| 10 | `stochastik.grundbegriffe` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 1–3 / Standard |
| 11 | `stochastik.simulation` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Standard |
| 12 | `stochastik.kombinatorik` | Reasoning with data (Daten und Wahrscheinlichkeit) | Enrichment |

**MYP 3** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `terme.umformen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 2 | `terme.potenzgesetze` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 3 | `bruch.prozent_grundwert` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 |
| 4 | `funktionen.linear` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard |
| 5 | `abbildungen.kongruenz` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 / Standard |
| 6 | `geometrie.konstruktion` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 7 | `messen.kreisberechnung` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 8 | `messen.koerper_darstellung` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 |
| 9 | `raum.pyramide_kegel_kugel` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 1–3 / Extended |
| 10 | `abbildungen.aehnlichkeit` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 11 | `trigo.pythagoras` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 12 | `mengen.grundbegriffe` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |

**MYP 4** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.potenzen_zehner` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 2 | `zahlen.reell` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 3 | `zahlen.intervalle` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 4 | `gleichungen.ungleichungen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 5 | `gleichungen.formeln` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 6 | `terme.bruchterme` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 7 | `gleichungen.bruch` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 8 | `groessen.indirekt` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 9 | `gleichungen.reinquadratisch` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 10 | `gleichungen.quadratisch` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 11 | `gleichungen.potenz` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard (Annahme) |
| 12 | `finanzen.zinsen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 1–3 (Annahme) |
| 13 | `finanzen.zinseszins` | Numerical and abstract reasoning (Zahl und Algebra) | Annahme |
| 14 | `sonder.logik` | Numerical and abstract reasoning (Zahl und Algebra) | kein Beleg |
| 15 | `funktionen.grundbegriffe` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard / Extended |
| 16 | `gleichungen.lgs2` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard |
| 17 | `funktionen.quadratisch` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Standard |
| 18 | `funktionen.potenz` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 19 | `funktionen.gebrochen` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 20 | `sonder.graphentheorie` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 21 | `trigo.rechtwinklig` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 22 | `trigo.allgemein` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Standard |
| 23 | `geometrie.kreis` | Spatial reasoning (Geometrie und Trigonometrie) | MYP 4–5 Extended |
| 24 | `raum.schraegbilder` | Spatial reasoning (Geometrie und Trigonometrie) | Enrichment |
| 25 | `daten.boxplot` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Standard |
| 26 | `stochastik.verknuepft` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |
| 27 | `stochastik.mehrstufig` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |

**MYP 5** – Quelle IBG (Framework S. 23–29), Zweige IBB

| Nr. | Thema | Zweig (Lernbereich) | Stufe im Framework |
|---|---|---|---|
| 1 | `zahlen.schranken` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Extended |
| 2 | `zahlen.rationale_exponenten` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Extended |
| 3 | `gleichungen.exponential` | Numerical and abstract reasoning (Zahl und Algebra) | Extended / Enrichment |
| 4 | `funktionen.folgen` | Numerical and abstract reasoning (Zahl und Algebra) | MYP 4–5 Standard |
| 5 | `funktionen.reihen` | Numerical and abstract reasoning (Zahl und Algebra) | Enrichment |
| 6 | `funktionen.transformation` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 7 | `funktionen.betrag` | Thinking with models (Funktionen und Modelle) | Annahme Extended |
| 8 | `funktionen.ganzrational` | Thinking with models (Funktionen und Modelle) | Enrichment |
| 9 | `funktionen.exponential_log` | Thinking with models (Funktionen und Modelle) | Extended / Enrichment |
| 10 | `funktionen.umkehr` | Thinking with models (Funktionen und Modelle) | Enrichment |
| 11 | `funktionen.trig` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 12 | `sonder.optimierung` | Thinking with models (Funktionen und Modelle) | MYP 4–5 Extended |
| 13 | `gleichungen.trig` | Spatial reasoning (Geometrie und Trigonometrie) | Annahme Extended |
| 14 | `abbildungen.matrizen` | Spatial reasoning (Geometrie und Trigonometrie) | kein Beleg |
| 15 | `daten.standardabweichung` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |
| 16 | `daten.zweidimensional` | Reasoning with data (Daten und Wahrscheinlichkeit) | Standard / Extended |
| 17 | `stochastik.bedingt` | Reasoning with data (Daten und Wahrscheinlichkeit) | MYP 4–5 Extended |
| 18 | `daten.normalverteilung` | Reasoning with data (Daten und Wahrscheinlichkeit) | Annahme |

### Quellen (alle abgerufen am 20.11.2026)
- **G5** LehrplanPLUS Gymnasium Mathematik 5 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik (M5 1–4 mit Unterkapiteln)
- **G6** … Gymnasium 6 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik (M6 1.1–1.5, 2.1–2.2, 3)
- **G7** … Gymnasium 7 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/7/mathematik (M7 1–5)
- **G10** … Gymnasium 10 – https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik (M10 1–5)
- **GSP** ISB, Verbindliche Hinweise zu Schwerpunktsetzungen, Gymnasium Mathematik 5–10, Stand August 2022 (alle Lernbereichs-Titel 5–10) – https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Gymnasium/August2022/M_Schwerpunktsetzungen_5_10_neu.pdf
- **GSP8 / GSP9** ISB, Schwerpunktsetzungen Gymnasium Mathematik 8 bzw. 9, Stand August 2021 (Inhalte von M8 3, M8 7, M9 2.2, M9 5, M9 7.2) – https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Gymnasium/deutsch_englisch_mathe/M_Schwerpunktsetzungen_8.pdf · …/M_Schwerpunktsetzungen_9.pdf
- **R5 / R6** LehrplanPLUS Realschule Mathematik 5 bzw. 6 – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/5/mathematik · …/realschule/6/mathematik
- **R7** LehrplanPLUS Realschule Mathematik 7 (I) – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1 (M7 1–8)
- **R10** LehrplanPLUS Realschule Mathematik 10 (I) – https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg1 (M10 1–5)
- **RML8 / RML9** C.C. Buchner, Stoffverteilungsplan Mathe.Logo 8 I bzw. 9 I, Realschule Bayern (Verlagsquelle; zitiert die Lernbereiche des LehrplanPLUS) – https://www.ccbuchner.de/_files_media/mediathek/downloads/15120.pdf · https://www.ccbuchner.de/_files_media/mediathek/downloads/15129.pdf
- **RSP9 / RSP10** ISB, Schwerpunktsetzungen Realschule Mathematik 9 bzw. 10, Stand 09.08.2022 (Lernbereichs-Titel I und II/III) – https://www.distanzunterricht.bayern.de/fileadmin/user_upload/lernenzuhause/Realschule/August2022/M_Schwerpunktsetzungen_9.pdf · …/M_Schwerpunktsetzungen_10.pdf
- **IBG** IB, Middle Years Programme, Mathematics guide (for use from September 2020/January 2021), Framework S. 23–29 (Kopie einer Schule) – https://wottonhouseschool.co.uk/de/_files/ugd/e64f71_44e88284d1a84f7e8779a8766a508714.pdf
- **IBB** IB, MYP Subject brief Mathematics (vier Zweige; Standard und Extended) – https://www.ibo.org/globalassets/new-structure/brochures-and-infographics/pdfs/myp-brief-mathematics-en.pdf
- Zum Abgleich: `inhalte/pruefung/klassen/vorschlag-rsib.md` (17.11., Haese-Kapitel, Spalte II/III)
