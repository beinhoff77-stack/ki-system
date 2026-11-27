# Rollendes System, Stufe 3 – Aufgaben auf Vorrat, dritte Runde

Auftrag 19, Stand 27.11.2026. Nur Inhalte. **Nichts ist eingespielt.** Erzeugt und geprüft von `bauen.py` (endet mit „OK“).
Zeichen: **[G]** gesichert (vom Programm geprüft oder in einer Datei nachgesehen), **[A]** Annahme, **[M]** meine Einschätzung.

## Was hier liegt

| Datei | Flug | für | Themen | ohne Bau | `bedingung` | Lernkarten | mit Zeichnung |
|---|---|---|---|---|---|---|---|
| `ge3.json` | Winkel | Kind 1 | `geometrie.winkel` | 15 | 5 | 7 von 7 | 0 |
| `r1.json` | Umfang und Fläche | Kind 1 | `messen.flaechen` | 15 | 5 | 7 von 7 | 0 |
| `g2.json` | Dreisatz, Teil 1 | Kind 1 | `groessen.proportional` (fünf Lernkarten) | 15 | 5 | 5 von 5 | 1 |
| `ge4.json` | Dreiecke, Vierecke, Konstruktion | Kind 2 | `geometrie.winkelsaetze`, `geometrie.konstruktion` | 18 | 5 | 16 von 16 | 3 |
| `f2.json` | Lineare Funktionen | Kind 2 | `funktionen.linear` | 18 | 5 | 11 von 11 | 1 |
| `a6.json` | Gleichungssysteme | Kind 2 | `gleichungen.lgs2` | 16 | 5 | 9 von 9 | 1 |

Zusammen **127 Aufgaben**: 97 ohne Bau, 30 des Typs `bedingung`. Aufbau der Dateien wie in `rollend-1` und `rollend-2`.

**Typen der 97 Aufgaben ohne Bau:** Umkehren 27, Verfahren wählen 16, Fehler-Detektiv 16, Brücke 15, Lückenweg 10, Zwei Wege vergleichen 6, Anwenden 7.
Gewöhnliche Anwendungsaufgaben: `GE3-11`, `R1-10`, `R1-11`, `G2-15`, `F2-11`, `A6-08`, `A6-16`.

## Woraus die Reihenfolge der Flüge kommt

**[G]** Aus `lehrplan-kinder/route.md` (erzeugt von `plan.py`, Aufträge 8 und 9; dort gegen die Voraussetzungen der App geprüft). Die Route je Kind, mit dem, was schon geliefert ist:

| Kind 1 | | Kind 2 | |
|---|---|---|---|
| 1 `z1` | *nicht geliefert, siehe unten* | 1 `a5` | *nicht geliefert, siehe unten* |
| 2 `ge1`, 3 `z2` | rollend-1 | 2 `ge2`, 3 `a4` | rollend-1 |
| 4 `a1`, 5 `d1`, 6 `g1` | rollend-2 | 4 `g8`, 5 `g2-teil2`, 6 `f1` | rollend-2 |
| **7 `ge3`, 8 `r1`, 9 `g2`** | **rollend-3** | **7 `ge4`, 8 `f2`, 9 `a6`** | **rollend-3** |
| 10 `g2-teil2`, 11 `d2`, 12 `r3` | als Nächstes | 10 `g7`, 11 `f3`, 12 `d5` | als Nächstes |

**[A] Wo die Reihenfolge nicht feststeht:**
- **Ob die Route in der App so eingestellt ist**, steht nicht im Repo. Ich nehme an, dass die Einstell-Liste aus Auftrag 9 gilt; Auftrag 18 hat dieselben Kürzel benutzt.
- **`ge4` hängt an der Diagnose.** Laut Route steht er „hinter ge2 und – falls die Diagnose es verlangt – hinter ge3“. Fällt die Diagnose so aus, kommt für Kind 2 erst `ge3`. Die Datei `ge3.json` passt dann auch für Kind 2 (Klasse-5-Stoff).
- **`f2`:** Die Route lässt `funktionen.scharen` aus. Die Datei `funktionen.linear` enthält aber selbst drei Lernkarten mit Parameter (`einsetzen`, `wirkung`, `bueschel`). Ich habe sie mit je einer Aufgabe bedient, weil der Auftrag „jede Lernkarte“ sagt.
- **`g2` für Kind 1** sind die fünf Lernkarten von Teil 1 (`einheit`, `dreisatz`, `geschickt`, `sach`, `aenderung`). Die drei von Teil 2 sind in `rollend-2/g2-teil2.json` – für Kind 2 gebaut, für Kind 1 ebenso brauchbar (Flug 10).
- **Für die ersten Flüge `z1` (Kind 1) und `a5` (Kind 2) gibt es keine Vorrats-Aufgaben.** Die Route nennt sie „zu Ende bringen“; die Aufträge 14 und 18 haben danach begonnen. Wenn sie noch laufen, fehlen dort neue Aufgabentypen.

## Geprüft [G]

- 106 Rechnungen zweifach nachgerechnet (Feld `c` mit dem Rechner aus `tools/inhalt_pruefen.py`, zweiter Weg im Programm).
- Alle 30 `bedingung`-Aufgaben: `pruefe_aufgabe` aus dem aktuellen `tools/bedingung.py` liefert eine leere Fehlerliste (damit auch: in der Lösung nur `bedingungen`, `beispiel`, `gut`, `gegenbeispiele`). Jede gute Antwort wird richtig bewertet; jedes Gegenbeispiel scheitert genau an der genannten Bedingung; kein Name ist länger als 40 Zeichen.
- `tools/inhalt_pruefen.py` an einer Kopie jeder der sieben Themen-Dateien: vorher und nachher kein Fehler. Kein Text steht wörtlich im Bestand.
- Jede Lernkarte jedes Flugs kommt vor (das Programm bricht sonst ab).
- 223 Fehlbilder beschrieben, 65 mit Fehlbild-Kennung. Zwei Texte mit Bruchstrich (`F2-03`: 2x/3 und 2/3), beide in erkannter Form.

## Lernkarten, die erst mit Zeichnen durch das Kind gut werden – alle drei Runden

**Anzeigen** kann die App (Tabelle, Säulen, Kreis, Koordinatensystem, Figur). **Zeichnen oder Antippen durch das Kind** kann sie nicht. Die Liste nennt, was davon abhängt.
Stufe: **A** = ohne Zeichnen nur dünn abgedeckt, hier bewusst nicht aufgefüllt · **B** = trägt, das Handwerk fehlt aber · **C** = braucht nur ein Bild zum Ansehen (kein Bau, nur Zeichnung beilegen).

| Runde | Flug | Lernkarte | Was das Kind zeichnen oder antippen müsste | Stufe | Aufgaben jetzt |
|---|---|---|---|---|---|
| 1 | ge1 | `koordinaten`, `strecken` | Punkt im Koordinatensystem setzen | B | 3, 4 |
| 1 | ge1 | `kreislinie`, `parallelen`, `zwei_kreise`, `verknuepfen` | Kreis und Parallele als Ortslinie zeichnen, Schnittpunkte markieren | **A** | 1, 2, 1, 0 |
| 1 | ge1 | `lagebeziehungen` | Senkrechte und Parallele zeichnen | **A** | 1 |
| 1 | ge2 | `achsenspiegelung`, `punktspiegelung`, `verschiebung`, `drehung` | Bildpunkt setzen, Figur abbilden | B | 5, 3, 2, 1 |
| 1 | ge2 | `mittelsenkrechte`, `winkelhalbierende` | Mit Zirkel konstruieren | **A** | 3, 1 |
| 1 | ge2 | `symmetrie`, `vierecke_ordnen` | Symmetrieachsen einzeichnen | **A** | 1, 1 |
| 2 | d1 | `saeulendiagramm` | Säule in der richtigen Höhe zeichnen | **A** | 3 |
| 2 | d1 | `kreisdiagramm` | Winkel abtragen | **A** | 4 |
| 2 | d1 | `absolute_haeufigkeit` | Strichliste führen | B | 3 |
| 2 | g1 | `massstab` | Auf einer Karte messen | B | 3 |
| 2 | g1 | `schaetzen` | – (braucht Bilder von Gegenständen) | C | 1 |
| 2 | f1 | `wertetabelle` | Aus der Tabelle den Graphen zeichnen | **A** | 2 |
| 2 | f1 | `graph_lesen` | Punkt am Graphen antippen | B | 2 |
| 2 | a1 | `waage` | Von beiden Seiten wegnehmen | C | 4 |
| 3 | ge3 | `ergaenzen`, `kreuzung`, `um_punkt`, `figuren` | Winkel mit dem Geodreieck messen und zeichnen | B | 3, 4, 3, 2 |
| 3 | ge3 | alle sieben | – (jede Aufgabe wäre mit einer Figur leichter zu lesen) | C | ohne Zeichnung |
| 3 | r1 | `einheitsquadrate` | Fläche mit Kästchen auslegen, Rechteck zu gegebener Fläche zeichnen | **A** | 2 |
| 3 | r1 | `zerlegen` | Zerlegungslinie selbst einzeichnen | B | 3 |
| 3 | ge4 | `planfigur`, `vierecke_konstruieren` | Dreieck und Viereck mit Zirkel und Geodreieck konstruieren | **A** | 1, 1 |
| 3 | ge4 | `kongruenzsatz`, `konstruierbar` | Konstruieren und sehen, ob es ein oder zwei Dreiecke gibt | B | 1, 2 |
| 3 | ge4 | `stufen_wechsel`, `figuren`, `beweisen` | Winkel in der Figur markieren, Hilfslinie einzeichnen | B | 1, 1, 1 |
| 3 | f2 | `graph_ablesen` | Gerade aus t und Steigungsdreieck zeichnen | **A** | 2 |
| 3 | f2 | `zwei_punkte`, `aufstellen` | Zwei Punkte setzen, Gerade hindurchlegen | B | 3, 3 |
| 3 | a6 | `grafisch` | Beide Geraden zeichnen, Schnittpunkt antippen | **A** | 2 |

**Zusammengefasst [M]:** Stufe A sind 17 Lernkarten in acht Flügen. Drei Werkzeuge würden fast alles decken:
1. **Punkt setzen im Koordinatensystem** (auch: Gerade durch zwei gesetzte Punkte) – deckt ge1, ge2, f1, f2, a6. Das ist der größte Hebel: fünf Flüge, darunter die drei Funktionen-Flüge von Kind 2.
2. **Säule ziehen und Winkel im Kreis einstellen** – deckt d1.
3. **Konstruieren mit Zirkel und Geodreieck** – deckt ge1 (Ortslinien), ge2 (Mittelsenkrechte), ge4. Am teuersten zu bauen; bis dahin gehört es auf Papier.
Ohne jeden Bau lösbar ist Stufe C: Den ge3-Aufgaben eine Figur beilegen (die Zeichenart `figur` gibt es, im Bestand von `geometrie.winkel` hängen 80 Aufgaben daran).

**Lücken aus Runde 1, die mir beim Zusammenführen aufgefallen sind [G]:** In `ge1` fehlen die Lernkarten `verstehen` (in beiden Themen) und `verknuepfen`; in `ge2` die zwei Vektor-Lernkarten (dort schon als Annahme genannt). Runde 1 hatte die Prüfung „jede Lernkarte kommt vor“ noch nicht.

## Nicht geprüft

- Kein Kind hat eine Aufgabe gerechnet. Stufen und Zählvorschläge sind Einschätzungen.
- Die sechs Zeichnungen habe ich nicht in der App gesehen. Die drei Figuren (`GE4-02`, `GE4-08`, `GE4-16`) sind nach dem Muster des Bestands gerechnet (Parallelen mit Schnittgerade; Dreieck maßstäblich), aber nie gezeichnet worden.
- `bedingung` nur gegen die Python-Referenz, nicht gegen die Datenbank.
- Inhaltlich gleiche Aufgaben im Bestand: nur wörtlicher Vergleich. Der Bestand ist bei diesen Themen groß (244 bis 445 Aufgaben je Thema); Überschneidungen im Muster sind wahrscheinlich, vor allem bei `GE4-01`, `F2-01`, `A6-08`.
- Lehrplan an der Quelle. Ob die Route in der App so eingestellt ist.

## Annahmen

- Regel-Kennungen, wo die Liste nicht genau passt: Gleichungssysteme hängen an `id.algebra.gleichung_loesen` (eine eigene Kennung gibt es nicht); Kongruenz und Konstruierbarkeit an `id.geometrie.deckungsgleich`; Geradengleichung an `id.funktionen.gleichung_form`, Sachzusammenhang an `id.funktionen.wachstum`.
- `ge4` hat 16 Lernkarten; deshalb 18 statt 15 Aufgaben ohne Bau, die meisten Lernkarten nur einmal. Ebenso `f2` (11 Lernkarten, 18 Aufgaben).
- In `g2` stehen Preise in Lücken in Cent, weil Lücken nur ganze Zahlen nehmen.
- Namen in Aufgaben (Ole, Kim, Pia, Tim, Lars, Emil, Jule, Nico, Mia, Jan, Ben) sind erfunden.
