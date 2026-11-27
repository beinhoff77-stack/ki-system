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


## Berichtigungen nach der Inhaltsprüfung (Auftrag 20)

Die Muster-Suche aus Auftrag 20 (unbeabsichtigte Lösung 0, nicht-falsche Falschantwort, Ziffernfolge als Zahl, fehlende Modellvoraussetzung) lief über alle 97 Aufgaben in `zahl`, `auswahl`, `luecken` dieser Runde. Neu erzeugt sind `a6.json`, `g2.json`, `r1.json` (`bauen.py` endet mit „OK“, 127 Aufgaben, 106 Rechnungen zweifach nachgerechnet). Kennungen, Lernziele und Teilfähigkeiten sind unverändert; die 30 `bedingung`-Aufgaben sind nicht angefasst.

| Kennung | Befund | was geändert (oder „bleibt, weil …“) |
|---|---|---|
| `G2-03` | Muster 4: „3 kg Kartoffeln kosten 4,50 €“ setzt einen festen Preis je kg voraus, der nirgends steht. | Voraussetzung im Text: „Bei Preisen gilt: Jedes Stück und jedes Kilogramm kostet gleich viel, es gibt keinen Rabatt.“ Lösungsweg nennt sie. |
| `G2-11` | Muster 4: „Ein Maler … 2 Maler“ setzt gleich schnelle Maler voraus. | Text: „alle Maler arbeiten gleich schnell“. Antwort bleibt. |
| `G2-15` | Muster 4: Rezept setzt gleiche Menge je Person voraus. | Text: „jede Person bekommt gleich viel“. |
| `A6-04` | Muster 2: „Addieren“ ist nicht falsch. Nach dem Umstellen (4x − y = 1 und x + y = 9) fällt y beim Addieren sofort weg. | Antwort heißt jetzt „beide Gleichungen so addieren, wie sie dastehen“ (dann entsteht 2y = 3x + 8, nichts fällt weg). Richtige Antwort „Gleichsetzen“ bleibt. |
| `R1-04` | Muster 2: „Weil 1 m = 100 cm ist“ ist für sich wahr, nur keine Begründung. | Antwort heißt „Weil 1 dm = 100 cm ist.“ (falsch: 1 dm sind 10 cm). Fehlbild-Text angepasst. |

**Geprüft und ohne Befund:**
(1) Unbeabsichtigte Lösung 0 oder weitere Lösungen: keine. Einzeln nachgesehen u. a. `GE3-08` (150° am Minutenzeiger gleich 25 Minuten, eine volle Drehung kommt nicht vor), `GE3-10` (kürzester Weg), `GE4-12` (kleinste ganze Zahl über 5: 6), `A6-10`, `A6-14`, `A6-15`, `F2-09`, `F2-16`, `F2-18` (ab 5 Stunden, bei 4 sind beide gleich).
(2) Alle weiteren Auswahl-Aufgaben einzeln gegengelesen, keine zweite richtige Antwort gefunden (u. a. `GE4-04`, `GE4-17`, `GE3-05`, `A6-01`, `A6-03`, `F2-03`, `F2-04`).
(3) Komma an einer Lücke: keiner. Satzkommas wie `A6-05` („②, x = ③“) stehen mit Leerzeichen und sind erlaubt. `R1-08` („2 a ① m²“, „0,08 m² = ② dm²“) hat die Lücken nicht an einem Komma.
(4) Weitere Modellvoraussetzungen: `G2-12`, `G2-14`, `F2-18` nennen „gleichmäßig“ bzw. die Tarife ausdrücklich.

**Neue automatische Prüfung in `bauen.py`:** Das Programm bricht ab, wenn im Fragetext oder in der Schablone einer Lückenaufgabe ein Komma ohne Leerzeichen an einem Lückenzeichen (① … ⑨, □) steht, etwa „0,②“ oder „①,②“. Satzkommas mit Leerzeichen („①, dann …“) sind erlaubt. Zusätzlich muss jede Lücke eine ganze Zahl sein. Die alten Fassungen von `G1-07`, `G8-01` und `G8-04` würden damit abbrechen (nachgestellt mit der Regel, nicht mit dem Programm selbst).
