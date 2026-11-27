# Klassen-Zuordnung Realschule und IB MYP – Vorschlag an den Nutzer (Neunzehnte Runde, Teil C)

Stand: 2026-11-17. Zweig `lehrplan-rsib`. **Nur ein Vorschlag.** Nichts an `themenliste.json`, Generatoren, Datenbank, App oder Tests geändert.
Aufbau wie der Gymnasium-Vorschlag (`inhalte/pruefung/klassen/vorschlag.md` im Zweig `daten-klassen`).

**Wörter in dieser Datei**
- **Klasse** = Jahrgangsstufe an der bayerischen Realschule (Feld `klasse.rs_by`). **MYP-Jahr** = Jahr 1–5 im IB Middle Years Programme (Feld `klasse.ib_myp`; MYP 1 ≈ Klasse 6).
- **Gruppe I** = Wahlpflichtfächergruppe I (mathematisch-technischer Zweig). **Gruppe II/III** = wirtschaftlicher bzw. sprachlicher/musischer Zweig. Ab Klasse 7 gibt es zwei Mathe-Lehrpläne. **Gruppe I ist hier der Hauptfall.**
- **Lernbereich** = Kapitel im LehrplanPLUS. „M7 LB6 (I)“ heißt: Mathematik, Klasse 7, Lernbereich 6, Gruppe I. „M5 1.3“ = Klasse 5, Lernbereich 1, Unterkapitel 3.
- **Framework** = das MYP-Rahmenwerk Mathematik des IB (Mathematics guide, gültig ab 2020/21). Es teilt den Stoff in vier Zweige und in Stufen: **MYP 1–3**, **Standard** (MYP 4–5, alle), **Extended** (MYP 4–5, Zusatz für Stärkere), **Enrichment** (freiwillig, nicht prüfungsrelevant).
- **H1 … H5E** = Lehrwerk Haese „Mathematics 6 (MYP 1)“ … „Mathematics 10 (MYP 5 Extended)“, 3. Auflage (2021/2022), Kapitelnummer dahinter. „H5E-2014“ = ältere Auflage „10E (MYP 5 Extended)“ von 2014.
- **[Name]** in eckigen Klammern = Thema, das heute **kein** Feld `rs_by` bzw. `ib_myp` hat, aber laut Lehrplan dazugehört (Vorschlag: nachtragen).

**Wie sicher ist das?**
- Realschule, gesichert: Lernbereiche und Inhalte aller Klassen 5–10, beide Gruppen, von lehrplanplus.bayern.de (abgerufen 17.11.2026). Einschränkung wie beim Gymnasium: Das Abruf-Werkzeug fasst den Text zusammen. Titel, Nummern und Kernsätze sind stimmig, wörtlich nachgeprüft ist nicht jeder Satz.
- Realschule, Annahme: Wo ein Thema über den Lehrplan hinausgeht, habe ich das an den **Etappen-Titeln und Merksätzen** festgemacht, nicht an jeder Aufgabe.
- IB: Das MYP legt **keinen Stoff je Jahr** fest. Der Guide sagt nur, dass im Lauf der fünf Jahre alle vier Zweige vorkommen und dass die Schule Standard/Extended selbst abgrenzt. Jede Jahreszahl unten stützt sich deshalb auf (a) die **Stufe im Framework** und (b) die **Kapitel im Lehrwerk Haese**. Die Framework-Tabelle habe ich nur als Zusammenfassung lesen können (Spaltenzuordnung laut Werkzeug „stellenweise unklar“).
  - **sicher** = Framework-Stufe eindeutig, und das Jahr liegt darin.
  - **üblich** = Lehrwerk legt es in dieses Jahr, Framework widerspricht nicht.
  - **Annahme** = nur ein Beleg, oder Framework und Lehrwerk widersprechen sich.
- „Kein Beleg gefunden“ heißt: In den gelesenen Quellen stand es nicht. Das heißt nicht sicher, dass es fehlt.

---

## Teil 1 – Realschule Bayern: Klasse je Thema (68 Themen mit `rs_by`)

Spalte **Nr.** = Vorschlag für `reihenfolge.rs_by`: laufende Nummer in Lehrplan-Reihenfolge innerhalb der **vorgeschlagenen** Klasse (Gruppe I). Lücken in der Nummerierung sind für die [nachzutragenden] Themen aus Teil 2 reserviert.
Spalte **II/III** = Klasse, in der Gruppe II/III den Stoff hat (nur wo abweichend oder wichtig).

Quellen-Kürzel (volle Adressen unten): **RS5**, **RS6** = …/fachlehrplan/realschule/5 bzw. 6/mathematik · **RS7-I** … **RS10-I** = …/realschule/<Kl>/mathematik/wpfg1 · **RS7-II** … **RS10-II** = …/realschule/<Kl>/mathematik/wpfg2-3

### Klasse 5

| Nr. | Thema | heute | laut Lehrplan | II/III | Lernbereich | Quelle | Vorschlag |
|---|---|---|---|---|---|---|---|
| 2 | `zahlen.ganz` | 5 | 5 | 5 | M5 LB2 Ganze Zahlen | RS5 | **bleibt 5.** Steht im Lehrplan nach M5 1.3, muss aber vor `zahlen.rechengesetze` kommen (dort Etappen „Ganze Zahlen multiplizieren/dividieren“). |
| 3 | `zahlen.rechengesetze` | 5 | 5 | 5 | M5 1.3 Grundrechenarten und Rechengesetze; ·/: ganzer Zahlen in M5 LB2 | RS5 | **bleibt 5** |
| 4 | `zahlen.potenzen_basis` | 5 | 5 | 5 | M5 1.3 (Potenzen, Quadratzahlen bis 400, große Zahlen als Zehnerpotenz) | RS5 | **bleibt 5** |
| 6 | `stochastik.kombinatorik` | 5 | 5 | 5 | M5 1.4 Kombinatorik (systematisch, Zählprinzip, Baumdiagramm) | RS5 | **bleibt 5** |
| 7 | `geometrie.grundbegriffe` | 5 | 5 | 5 | M5 LB3 Geometrische Grundvorstellungen und Grundbegriffe | RS5 | **bleibt 5** |
| 8 | `geometrie.winkel` | 5 | 5 | 5 | M5 LB3 (Winkel 0°–360°; **Scheitel- und Nebenwinkel**) | RS5 | **bleibt 5.** Die Etappe „Winkel an einer Geradenkreuzung“ ist hier **Pflichtstoff** (heute Vertiefung). |
| 9 | `messen.koerper_darstellung` | 5 | 5 (Teile 7, 9) | 5 | M5 LB3 (Körper beschreiben; Netze/Schrägbilder von Würfel und Quader). Schrägbilder von Prismen: M7 LB4 (I) / M8 LB2 (II). Netze von Prisma/Zylinder: M9 LB5 (I). Ansichten: kein Beleg | RS5, RS7-I, RS9-I | **bleibt 5.** Etappen „Netze von Prismen“, „Zylinder und sein Netz“ gehen über Klasse 5 hinaus. |
| 10 | `groessen.einheiten` | 5 | 5 | 5 | M5 LB4 Größen | RS5 | **bleibt 5** |
| 11 | `messen.flaechen` | 5 | 5 | 5 | M5 LB5 Umfang und Flächeninhalt (Rechteck, Quadrat, Zerlegen) | RS5 | **bleibt 5.** `umfang` nennt Dreieck/Parallelogramm/Trapez (= M6 LB3) – die Etappen enthalten das nicht (siehe Teil 2, Nr. 4). |
| 12 | `daten.darstellen` | 5 | 5 (Teile 6, 8) | 5 | M5 LB6 Auswertung von Daten (Diagramme, Vierfeldertafel, Verzerrungen). Relative Häufigkeit: M8 LB7 (I) / M8 LB6 (II) | RS5, RS8-I | **bleibt 5.** Etappen „Relative Häufigkeit“ und „Kreisdiagramme berechnen“ brauchen Bruchrechnung (M6 LB1). |

### Klasse 6

| Nr. | Thema | heute | laut Lehrplan | II/III | Lernbereich | Quelle | Vorschlag |
|---|---|---|---|---|---|---|---|
| 1 | `bruch.brueche` | 6 | 6 | 6 | M6 LB1 Rationale Zahlen | RS6 | **bleibt 6** |
| 2 | `bruch.dezimal` | 6 | 6 | 6 | M6 LB1 | RS6 | **bleibt 6** |
| 3 | `bruch.rechnen` | 6 | 6 | 6 | M6 LB1 | RS6 | **bleibt 6** |
| 4 | `abbildungen.kongruenz` | 6 | 6 (Teile 7, 8) | 6 | M6 LB2 Achsenspiegelung und Symmetrie (auch Mittelsenkrechte, Lot, Winkelhalbierende). Verschiebung: M7 LB2. Drehung, Punktspiegelung: M8 LB2 (nur I). Parkett: kein Beleg | RS6, RS7-I, RS8-I | **bleibt 6.** Etappen „An einem Punkt spiegeln“, „Figuren verschieben“, „Um einen Punkt drehen“ gehen über Klasse 6 hinaus. |
| 5 | `messen.koerper_berechnung` | 6 | 6 | 6 | M6 LB3 (Oberfläche Quader/Würfel), M6 LB4 Raumgeometrie (Volumen) | RS6 | **bleibt 6.** „Volumen von Quader und Würfel“ ist hier **Pflicht** (heute Vertiefung). |
| 6 | `terme.aufstellen` | 6 | 6 | 6 | M6 LB5 Terme und Gleichungen | RS6 | **bleibt 6** |
| 7 | `gleichungen.einfach` | 6 | 6 | 6 | M6 LB5 (a · x = c, x + b = c). Zwei Schritte (ax + b = c): M7 LB6 (I) / LB4 (II) | RS6, RS7-I | **bleibt 6** |
| 8 | `groessen.proportional` | 5 | **6** (Dreisatz schon 5) | 6 | M6 LB6 Direkte Proportionalität. Dreisatz allein: M5 LB4 | RS6, RS5 | **ändern auf 6.** 3 der 7 Etappen behandeln den Begriff „proportional“, der erst in M6 LB6 steht. |
| 9 | `bruch.prozent` | 6 | 6 (Teile 7) | 6 | M6 LB6 (Prozentwert, Grundwert, Prozentsatz). Rabatt/Aufschlag als vermehrter/verminderter Grundwert und Zinsen: M7 LB7 (I) / LB5 (II) | RS6, RS7-I | **bleibt 6.** 2 Etappen („Rabatt und Aufschlag“, „Zinsen berechnen“) sind Stoff 7. |

### Klasse 7 (Gruppe I)

| Nr. | Thema | heute | laut Lehrplan | II/III | Lernbereich | Quelle | Vorschlag |
|---|---|---|---|---|---|---|---|
| 1 | `terme.potenzgesetze` | 7 | 7 | 7 | M7 LB1 Potenzen | RS7-I, RS7-II | **bleibt 7** (rationale Exponenten aus `umfang` = M10 LB3 (I), nicht in den Etappen) |
| 2 | `zahlen.potenzen_zehner` | 5 | **7** (große Zahlen: 5) | 7 | M7 LB1 (negative Exponenten; Vorsilben 10⁻¹⁸ bis 10¹⁸). M5 1.3 nur große Zahlen als Zehnerpotenz | RS7-I, RS5 | **ändern auf 7.** 4 von 7 Etappen brauchen negative Exponenten oder Vorsilben, eine weitere teilweise. |
| 3 | `abbildungen.vektoren` | 7 | 7 | 7 | M7 LB2 Parallelverschiebung | RS7-I, RS7-II | **bleibt 7** (Skalarprodukt aus `umfang` = M10 LB1 (I), nicht in den Etappen) |
| 4 | `abbildungen.determinanten2` | 7 | 7 | 7 | M7 LB2 (Fläche mit zweireihigen Determinanten; Vielecke nur I); wieder in M8 LB6 (I) / M9 LB5 (II) | RS7-I | **bleibt 7** |
| 6 | `geometrie.konstruktion` | 6 | **7** | 7 und 8 | M7 LB2 (Winkel an Parallelen, Innenwinkelsumme), M7 LB3 Dreiecke (Konstruktion, Kongruenzsätze). II/III: Dreiecke in M8 LB1. Vierecke: M8 LB1 | RS7-I, RS8-II | **ändern auf 7.** Keine Etappe ist Stoff der Klasse 6. |
| 7 | `geometrie.ortslinien` | 7 | 7 | 7 | M7 LB5 (I) / M7 LB3 (II) Geometrische Ortslinien und Ortsbereiche | RS7-I, RS7-II | **bleibt 7** |
| 8 | `geometrie.kreis` | 7 | 7 | 7 | M7 LB5 (I) / LB3 (II): Thaleskreis, Tangente, Umkreis, Inkreis | RS7-I, RS7-II | **bleibt 7** |
| 10 | `zahlen.intervalle` | 7 | 7 | 7 | M7 LB6 (I) / LB4 (II): Lösungsmenge in **Intervall- und Mengenschreibweise** | RS7-I, RS7-II | **bleibt 7.** Anders als beim Gymnasium gibt es hier einen Beleg. |
| 11 | `gleichungen.linear` | 7 | 7 und 8 | 7 und 8 | M7 LB6 (ax + b = c). Variable auf beiden Seiten, Klammern: M8 LB4 (I) / LB3 (II) | RS7-I, RS8-I | **bleibt 7.** 3 von 6 Etappen sind Stoff 8 (siehe Entscheidung 3). |
| 12 | `gleichungen.ungleichungen` | 7 | 7 (Teile 8) | 7 | M7 LB6 (ax + b ⋚ c). Beide Seiten: M8 LB4 (I). Graph: M8 LB6 (I) | RS7-I, RS8-I | **bleibt 7.** „Klammern und x auf beiden Seiten“, „Ungleichung am Graphen lösen“ sind Stoff 8. |
| 13 | `bruch.prozent_grundwert` | 7 | 7 | 7 | M7 LB7 (I) / LB5 (II) Proportionalitäten | RS7-I, RS7-II | **bleibt 7** |
| 15 | `groessen.indirekt` | 7 | 7 | 7 | M7 LB7 (I) / LB5 (II) (Produktgleichheit, Hyperbelast) | RS7-I, RS7-II | **bleibt 7** |
| 16 | `daten.kennwerte` | 7 | 7 | 7 | M7 LB8 (I) / LB6 (II) (Mittel, Zentralwert, Modalwert, Spannweite) | RS7-I, RS7-II | **bleibt 7.** Modalwert und Median sind hier **Pflicht** (heute Vertiefung). |
| 17 | `daten.boxplot` | 7 | 7 (Quartile, Boxplot: kein Beleg) | 7 | M7 LB8 (I). Quartile, Boxplot: kein Beleg in RS 5–10 | RS7-I | **bleibt 7.** Überschneidet sich stark mit `daten.kennwerte` (siehe Entscheidung 4). |
| 18 | `daten.stichproben` | 7 | 7 | 7 | M7 LB8 (I) / LB6 (II) (Stichprobe repräsentativ?) | RS7-I, RS7-II | **bleibt 7** |

### Klasse 8 (Gruppe I)

| Nr. | Thema | heute | laut Lehrplan | II/III | Lernbereich | Quelle | Vorschlag |
|---|---|---|---|---|---|---|---|
| 1 | `raum.schraegbilder` | 5 | 7 und 8 – **Hauptklasse 8** | 8 und 10 | Pyramide beschreiben: M5 LB3. Schrägbilder Prisma/Pyramide, windschief: M7 LB4 (I). 3D-Koordinaten, Rotationskörper, Axialschnitte: M8 LB3 (I). II/III: Schrägbilder M8 LB2, Axialschnitte M10 LB2, 3D-Koordinaten kein Beleg | RS7-I, RS8-I, RS10-II | **ändern auf 8.** Erst am Ende von Klasse 8 ist jede Etappe dran. |
| 2 | `terme.quadratische_extreme` | 8 | 8 | 8 | M8 LB4 (I) / LB3 (II) (Extremwerte von ax² + bx + c) | RS8-I, RS8-II | **bleibt 8** |
| 3 | `terme.bruchterme` | 8 | 8 (nur Definitionsmenge) | 8 | M8 LB5 (I) / LB4 (II): Bruchterme erkennen, Definitionsmenge. Kürzen, Erweitern, +, −, ·, : von Bruchtermen: kein Beleg | RS8-I, RS8-II | **bleibt 8.** 5 von 7 Etappen gehen über den RS-Lehrplan hinaus (Entscheidung 3). |
| 4 | `gleichungen.bruch` | 8 | 8 | 8 | M8 LB5 (I) / LB4 (II): einfache Bruchgleichungen, Verhältnisgleichungen | RS8-I | **bleibt 8.** „Mit dem Hauptnenner multiplizieren“, „am Graphen lösen“ gehen darüber hinaus. |
| 5 | `funktionen.grundbegriffe` | 8 | 8 | 8 | M8 LB6 (I) / LB5 (II) Funktionen | RS8-I, RS8-II | **bleibt 8** |
| 6 | `funktionen.linear` | 8 | 8 | **9** | M8 LB6 (I). II/III: in M8 LB5 nur y = mx, Rest in M9 LB5 | RS8-I, RS8-II, RS9-II | **bleibt 8** |
| 7 | `funktionen.scharen` | 8 | 8 (Teile kein Beleg) | 9 | M8 LB6 (I): Parallelenscharen. Geradenbüschel, vom Parameter abhängige Lösungen: kein Beleg. Parabelscharen: M9 LB7 (I) | RS8-I, RS9-I | **bleibt 8** (Annahme) |

### Klasse 9 (Gruppe I)

| Nr. | Thema | heute | laut Lehrplan | II/III | Lernbereich | Quelle | Vorschlag |
|---|---|---|---|---|---|---|---|
| 1 | `zahlen.wurzeln_basis` | 9 | 9 | 9 | M9 LB1 Reelle Zahlen; dritte Wurzel: M10 LB3 (I) | RS9-I | **bleibt 9** |
| 2 | `zahlen.reell` | 9 | 9 | 9 | M9 LB1 („Nenner rational machen“ nur I; Heron-Verfahren: kein Beleg) | RS9-I, RS9-II | **bleibt 9** |
| 3 | `gleichungen.reinquadratisch` | 9 | 9 | 9 | M9 LB1 (x² = a lösen) | RS9-I, RS9-II | **bleibt 9** |
| 4 | `abbildungen.aehnlichkeit` | 9 | 9 | 9 | M9 LB2 Zentrische Streckung (Wirkung auf Volumen: kein Beleg) | RS9-I, RS9-II | **bleibt 9** |
| 5 | `trigo.pythagoras` | 9 | 9 | 9 | M9 LB3 Rechtwinklige Dreiecke | RS9-I, RS9-II | **bleibt 9** |
| 6 | `trigo.rechtwinklig` | 9 | 9 | 9 | M9 LB3; sin² + cos² = 1 erst M10 LB1 | RS9-I, RS10-I | **bleibt 9** |
| 7 | `messen.kreisberechnung` | 9 | 9 | 9 | M9 LB4 Kreis; Zylinder: M9 LB5 (I) / M10 LB2 (II) | RS9-I | **bleibt 9** |
| 8 | `raum.pyramide_kegel_kugel` | 9 | 9 | **10** | M9 LB5 (I) Raumgeometrie; II/III: M10 LB2 | RS9-I, RS10-II | **bleibt 9** |
| 9 | `gleichungen.lgs2` | 9 | 9 | 9 | M9 LB6 Systeme linearer Gleichungen | RS9-I, RS9-II | **bleibt 9** |
| 10 | `funktionen.transformation` | 9 | 9 (Parabeln); andere Graphen 10 | 10 | M9 LB7 (I): Parameter der Scheitelform deuten. M10 LB2 (I): Abbildungen von Graphen | RS9-I, RS10-I | **bleibt 9.** Überschneidet sich mit `funktionen.quadratisch` („Was bewirken a, d und e?“). |
| 11 | `funktionen.quadratisch` | 8 | **9** | 10 | M9 LB7 (I) Quadratische Funktionen und Gleichungen; II/III: M10 LB4. Klasse 8 hat nur Extremwerte quadratischer **Terme** (M8 LB4) | RS9-I, RS10-II | **ändern auf 9** |
| 12 | `gleichungen.quadratisch` | 9 | 9 | 10 | M9 LB7 (I) / M10 LB4 (II) | RS9-I, RS10-II | **bleibt 9** |
| 13 | `gleichungen.wurzel` | 9 | 9 | kein Beleg | M9 LB7 (I): Wurzelgleichungen mit Definitionsmenge | RS9-I | **bleibt 9** |
| 14 | `stochastik.grundbegriffe` | 8 | **9** (Teile 8) | 9 | M9 LB8 (I) / LB7 (II): Laplace, Ergebnisraum, Gegenereignis, Gesetz der großen Zahlen. M8 LB7 (I): Ergebnis, Ereignis, Häufigkeiten | RS9-I, RS8-I | **ändern auf 9.** 4 von 6 Etappen sind Stoff 9. |
| 15 | `stochastik.verknuepft` | 8 | **9** (Teile kein Beleg) | 9 | M9 LB8 (Ereignisse als Teilmengen, Gegenereignis). Vierfeldertafel: M5 LB6, M8 LB7. Additionssatz, bedingte Wahrscheinlichkeit: kein Beleg | RS9-I, RS8-I | **ändern auf 9** (Annahme). Wahrscheinlichkeiten gibt es erst in Klasse 9. |
| 16 | `stochastik.simulation` | 9 | 9 (Monte-Carlo: kein Beleg) | 9 | M9 LB8 (I) / LB7 (II): Gesetz der großen Zahlen an **simulierten** Zufallsexperimenten | RS9-I | **bleibt 9** (Annahme) |

### Klasse 10 (Gruppe I)

| Nr. | Thema | heute | laut Lehrplan | II/III | Lernbereich | Quelle | Vorschlag |
|---|---|---|---|---|---|---|---|
| 1 | `trigo.allgemein` | 10 | 10 | 10 | M10 LB1 Trigonometrie | RS10-I, RS10-II | **bleibt 10** |
| 2 | `funktionen.trig` | 10 | 10 (Teile kein Beleg) | 10 | M10 LB1 (Graphen von sin, cos, tan; periodische Vorgänge). Bogenmaß, Parameter a, b, d: kein Beleg | RS10-I | **bleibt 10** |
| 3 | `gleichungen.trig` | 10 | 10 | 10 (nur Winkel aus Werten) | M10 LB1 (I): Gleichungen mit trigonometrischen Zusammenhängen | RS10-I, RS10-II | **bleibt 10** |
| 4 | `abbildungen.matrizen` | 10 | 10 (Teile kein Beleg) | kein Beleg | M10 LB2 Abbildungen (I): Spiegelung an Ursprungsgeraden, Drehung mit Matrizen. Skalarprodukt: M10 LB1 (I). Matrizenprodukt, Umkehrmatrix: kein Beleg | RS10-I | **bleibt 10** |
| 5 | `zahlen.rationale_exponenten` | 10 | 10 | kein Beleg | M10 LB3 (I) Potenzen und Potenzfunktionen | RS10-I | **bleibt 10** |
| 6 | `gleichungen.potenz` | 10 | 10 | kein Beleg | M10 LB3 (I): n-te Wurzel als Lösung von xⁿ = a | RS10-I | **bleibt 10** |
| 7 | `funktionen.potenz` | 10 | 10 | kein Beleg | M10 LB3 (I) | RS10-I | **bleibt 10** |
| 8 | `funktionen.exponential_log` | 10 | 10 | 10 (ohne Logarithmusfunktion) | M10 LB4 (I) / LB3 (II) | RS10-I, RS10-II | **bleibt 10** |
| 9 | `gleichungen.exponential` | 10 | 10 | 10 | M10 LB4 (I) / LB3 (II) | RS10-I, RS10-II | **bleibt 10** |
| 10 | `funktionen.umkehr` | 10 | 10 | kein Beleg | M10 LB3 und LB4 (I): Umkehrfunktion | RS10-I | **bleibt 10** (nach den Exponentialfunktionen, weil eine Etappe sie braucht) |
| 11 | `stochastik.mehrstufig` | 10 | 10 | 10 | M10 LB5 Daten und Zufall (Baumdiagramm, Pfadregeln) | RS10-I, RS10-II | **bleibt 10** |

**Ergebnis Teil 1:** 61 Themen bleiben, **7 ändern**: `groessen.proportional` 5→6, `zahlen.potenzen_zehner` 5→7, `geometrie.konstruktion` 6→7, `raum.schraegbilder` 5→8, `funktionen.quadratisch` 8→9, `stochastik.grundbegriffe` 8→9, `stochastik.verknuepft` 8→9.

### Reihenfolge je Klasse auf einen Blick (Vorschlag `reihenfolge.rs_by`, Gruppe I)

- **5:** 1 [`zahlen.natuerlich`] · 2 `zahlen.ganz` · 3 `zahlen.rechengesetze` · 4 `zahlen.potenzen_basis` · 5 [`zahlen.teilbarkeit`] · 6 `stochastik.kombinatorik` · 7 `geometrie.grundbegriffe` · 8 `geometrie.winkel` · 9 `messen.koerper_darstellung` · 10 `groessen.einheiten` · 11 `messen.flaechen` · 12 `daten.darstellen`
- **6:** 1 `bruch.brueche` · 2 `bruch.dezimal` · 3 `bruch.rechnen` · 4 `abbildungen.kongruenz` · (hier fehlt Flächeninhalt der Vielecke, Teil 2 Nr. 4) · 5 `messen.koerper_berechnung` · 6 `terme.aufstellen` · 7 `gleichungen.einfach` · 8 `groessen.proportional` · 9 `bruch.prozent`
- **7:** 1 `terme.potenzgesetze` · 2 `zahlen.potenzen_zehner` · 3 `abbildungen.vektoren` · 4 `abbildungen.determinanten2` · 5 [`geometrie.winkelsaetze`] · 6 `geometrie.konstruktion` · 7 `geometrie.ortslinien` · 8 `geometrie.kreis` · 9 [`terme.umformen`] · 10 `zahlen.intervalle` · 11 `gleichungen.linear` · 12 `gleichungen.ungleichungen` · 13 `bruch.prozent_grundwert` · 14 [`finanzen.zinsen`] · 15 `groessen.indirekt` · 16 `daten.kennwerte` · 17 `daten.boxplot` · 18 `daten.stichproben`
- **8:** 1 `raum.schraegbilder` · 2 `terme.quadratische_extreme` · 3 `terme.bruchterme` · 4 `gleichungen.bruch` · 5 `funktionen.grundbegriffe` · 6 `funktionen.linear` · 7 `funktionen.scharen` (Lernbereiche 1 Vierecke, 2 Drehung und 7 Daten und Zufall haben kein eigenes Thema)
- **9:** 1 `zahlen.wurzeln_basis` · 2 `zahlen.reell` · 3 `gleichungen.reinquadratisch` · 4 `abbildungen.aehnlichkeit` · 5 `trigo.pythagoras` · 6 `trigo.rechtwinklig` · 7 `messen.kreisberechnung` · 8 `raum.pyramide_kegel_kugel` · 9 `gleichungen.lgs2` · 10 `funktionen.transformation` · 11 `funktionen.quadratisch` · 12 `gleichungen.quadratisch` · 13 `gleichungen.wurzel` · 14 `stochastik.grundbegriffe` · 15 `stochastik.verknuepft` · 16 `stochastik.simulation`
- **10:** 1 `trigo.allgemein` · 2 `funktionen.trig` · 3 `gleichungen.trig` · 4 `abbildungen.matrizen` · 5 `zahlen.rationale_exponenten` · 6 `gleichungen.potenz` · 7 `funktionen.potenz` · 8 `funktionen.exponential_log` · 9 `gleichungen.exponential` · 10 `funktionen.umkehr` · 11 `stochastik.mehrstufig`

Abweichungen von der reinen Lernbereichs-Folge (bewusst, damit jede Etappe nur Bekanntes nutzt): Klasse 5 `zahlen.ganz` vor M5 1.3; Klasse 7 `terme.potenzgesetze` vor `zahlen.potenzen_zehner`; Klasse 9 `funktionen.transformation` vor `funktionen.quadratisch`; Klasse 10 `funktionen.umkehr` nach den Exponentialfunktionen.

---

## Teil 2 – Was der Realschule fehlt (LehrplanPLUS Klasse 5–10, Lernbereich für Lernbereich)

„Fehlt“ = nach Etappen-Titeln, Merksätzen und einer Textsuche in allen Themendateien nicht gefunden. Dringlichkeit: **hoch** = Kernstoff (auch Jahrgangsstufentest/Abschlussprüfung – das ist meine Einschätzung, nicht geprüft), **mittel**, **niedrig**.

| Nr. | Was fehlt | Lehrplan-Bezug | Wohin | Dringlichkeit |
|---|---|---|---|---|
| 1 | `rs_by` fehlt, Stoff ist da: `zahlen.natuerlich` (5), `zahlen.teilbarkeit` (5), `geometrie.winkelsaetze` (7), `terme.umformen` (7; Etappe „Binomische Formeln“ = 8), `finanzen.zinsen` (7) | M5 1.1, M5 1.3, M7 LB2, M7 LB6 / M8 LB4, M7 LB7 | nur Feld nachtragen | **hoch** (wenig Aufwand) |
| 2 | Dualsystem (römische Zahlen sind da) | M5 1.2 Andere Zahlensysteme | `zahlen.natuerlich` erweitern | mittel |
| 3 | Kegel, Kugel, Zylinder nach Ecken, Kanten, Flächen beschreiben | M5 LB3 | `messen.koerper_darstellung` erweitern | niedrig |
| 4 | **Flächeninhalt von Dreieck, Parallelogramm, Trapez, Drachenviereck, Raute** mit Formel und passender Höhe; Vielecke zerlegen | M6 LB3 | **neues Thema** (fehlt in der ganzen App; Annahme: auch dem Gymnasium) | **hoch** |
| 5 | Volumeneinheiten und Hohlmaße umrechnen (m³, dm³, Liter, ml) | M5 LB4 (Hohlmaß), M6 LB4 | `groessen.einheiten` oder `messen.koerper_berechnung` erweitern | mittel |
| 6 | Raumgeometrie: Lage von Gerade und Ebene, Winkel zwischen Gerade und Ebene bzw. zwei Ebenen; Strecken und Winkel in wahrer Größe aus dem Schrägbild | M7 LB4 (I) | `raum.schraegbilder` erweitern (braucht Zeichnung, App kann keine Schrägbilder) | mittel |
| 7 | Ortslinien vollständig: Winkelhalbierende, Parallelenpaar, Thaleskreis als Ortslinie; Ortsbereiche („höchstens/mindestens“); Schwerpunkt des Dreiecks; Tangenten von einem Außenpunkt konstruieren | M7 LB5 (I) / LB3 (II) | `geometrie.ortslinien` und `geometrie.kreis` erweitern | mittel |
| 8 | **Vierecke**: Eigenschaften der Sonderformen ordnen, Vierecke konstruieren | M8 LB1 (I), M8 LB1 (II) | neues Thema oder `geometrie.konstruktion` erweitern (Konstruieren durch das Kind kann die App nicht) | mittel |
| 9 | **Drehung** als eigene Abbildung, Drehsymmetrie; Vektoren um ±90° und 180° drehen | M8 LB2 (I) | neues Thema „Drehung“ (heute nur Vertiefungs-Etappe in `abbildungen.kongruenz`) | mittel |
| 10 | Symmetrische Körper, Symmetrieebenen | M8 LB3 (I) | `raum.schraegbilder` erweitern | niedrig |
| 11 | Daten und Zufall Klasse 8 ohne eigenes Thema (Ergebnis, Ereignis, Häufigkeiten; Baumdiagramm und Vierfeldertafel als Darstellung) | M8 LB7 (I) / LB6 (II) | entsteht durch die Verschiebung von `stochastik.grundbegriffe` nach 9; deren Etappen 1–2 decken es ab | niedrig |
| 12 | **Zentrische Streckung im Koordinatensystem**: Zahl mal Vektor, Bildpunkte berechnen, Streckungsfaktor; Parameterverfahren (gestreckte Geraden/Parabeln); Strecke im Verhältnis teilen (Goldener Schnitt); Schwerpunkt rechnerisch | M9 LB2 (I) | neues Thema „Abbildungen im Koordinatensystem“ oder `abbildungen.aehnlichkeit` erweitern | **hoch** (Gruppe I) |
| 13 | Betrag eines Vektors; Extremwerte mit dem Satz des Pythagoras | M9 LB3 (I) | `trigo.pythagoras` erweitern | niedrig |
| 14 | **Prisma** (Volumen, Oberfläche); Prinzip von Cavalieri; Extremwerte bei Körpern | M9 LB5 (I) / M10 LB2 (II) | `raum.pyramide_kegel_kugel` erweitern | mittel |
| 15 | Parabelscharen, Trägergraph der Scheitelpunkte; Schnitt zweier Parabeln; Diskriminante bei Tangentenproblemen | M9 LB7 (I) | `funktionen.scharen` / `funktionen.quadratisch` erweitern | mittel |
| 16 | Trigonometrie Klasse 10: Winkel zwischen zwei Geraden (m = tan α); Graph von tan; Komplement- und Supplementbeziehungen; **Additionstheoreme**; Trägergraph; Skalarprodukt in der Geometrie (Abstand Punkt–Gerade) | M10 LB1 (I) | `trigo.allgemein` erweitern (Additionstheoreme stehen schon im `umfang`, nicht in den Etappen) oder neues Thema | **hoch** (Gruppe I) |
| 17 | Abbildungen von Graphen der Potenz-, Exponential- und Logarithmusfunktionen (verschieben, strecken, spiegeln); Trägergraphen | M10 LB2 (I) | `funktionen.transformation` erweitern (heute nur Parabeln) | mittel |
| 18 | Logarithmensätze (Produkt, Quotient); y = k · a^(x − b) + c; Logarithmusfunktion mit Parametern | M10 LB4 (I) | `gleichungen.exponential` / `funktionen.exponential_log` erweitern | mittel |
| 19 | Potenzfunktionen y = a(x + b)^c + d mit Asymptoten (Hyperbel als Sonderfall) | M10 LB3 (I) | Annahme: `funktionen.gebrochen` bekommt `rs_by` 10 | niedrig |
| 20 | Gruppe II/III: Raumgeometrie (M10 LB2) und quadratische Funktionen (M10 LB4) liegen in Klasse 10, nicht 9 | M10 (II/III) | kein Stoff fehlt – die App kennt nur **eine** RS-Klasse je Thema (Entscheidung 2) | mittel |

---

## Teil 3 – IB MYP: Jahr je Thema (61 Themen mit `ib_myp`)

**Grundlage:** IB „Mathematics guide“ (für Unterricht ab September 2020/Januar 2021), Abschnitt Framework (S. 22–29). Die vier Zweige heißen dort „Numerical and abstract reasoning“ (Zahl, Algebra), „Thinking with models“ (Funktionen, Modelle), „Spatial reasoning“ (Geometrie, Trigonometrie), „Reasoning with data“ (Statistik, Wahrscheinlichkeit).
**Wichtig:** Der Guide legt kein Jahr fest. Stufe „MYP 1–3“ heißt: irgendwo in den Jahren 1 bis 3. Für das genaue Jahr stütze ich mich auf das Lehrwerk Haese (H1–H5E).

| Thema | heute | Vorschlag | Zweig | Stufe im Framework | Lehrwerk | Sicherheit | Bemerkung |
|---|---|---|---|---|---|---|---|
| `zahlen.rechengesetze` | 1 | **bleibt 1** | Zahl | MYP 1–3 | H1 Kap. 2 | üblich | Etappen „Ganze Zahlen ·/:“ brauchen `zahlen.ganz` (Jahr 2) – Reihenfolge-Konflikt |
| `zahlen.potenzen_basis` | 1 | **bleibt 1** | Zahl | MYP 1–3 | H1 Kap. 2G, 4 | üblich | Etappe „negative Basis“ braucht `zahlen.ganz` |
| `geometrie.grundbegriffe` | 1 | **bleibt 1** | Geometrie | MYP 1–3 | H1 Kap. 3, 5, 15 | üblich | |
| `geometrie.winkel` | 1 | **bleibt 1** | Geometrie | MYP 1–3 | H1 Kap. 3 | üblich | |
| `messen.flaechen` | 1 | **bleibt 1** | Geometrie | MYP 1–3 | H1 Kap. 9–10 | üblich | |
| `messen.koerper_berechnung` | 1 | **bleibt 1** | Geometrie | MYP 1–3 | H1 Kap. 10 (Quader-Volumen); Oberfläche H3 Kap. 12 | Annahme | Oberfläche im Lehrwerk erst Jahr 3 |
| `bruch.brueche` | 1 | **bleibt 1** | Zahl | MYP 1–3 | H1 Kap. 6 | üblich | |
| `bruch.dezimal` | 1 | **bleibt 1** | Zahl | MYP 1–3 | H1 Kap. 7 | üblich | |
| `bruch.rechnen` | 1 | **ändern auf 2** | Zahl | MYP 1–3 | H1 nur +/− und Bruch · ganze Zahl; H2 Kap. 6 (·, :) | üblich | braucht außerdem negative Zahlen (Jahr 2) |
| `bruch.prozent` | 1 | **bleibt 1** | Zahl | MYP 1–3 | H1 Kap. 12; Zinsen H4 Kap. 11 | üblich | Etappe „Zinsen berechnen“ im Lehrwerk erst Jahr 4 |
| `daten.darstellen` | 1 | **bleibt 1** | Statistik | MYP 1–3 (relative Häufigkeit: Standard) | H1 Kap. 18 | üblich | |
| `terme.aufstellen` | 1 | **bleibt 1** | Algebra | MYP 1–3 | H1 Kap. 14 (Muster), H2 Kap. 8 | üblich | |
| `gleichungen.einfach` | 1 | **bleibt 1** | Algebra | MYP 1–3 | H2 Kap. 10 | Annahme | Lehrwerk erst Jahr 2 |
| `zahlen.wurzeln_basis` | 1 | **bleibt 1** | Zahl | MYP 1–3 (Quadrate, Quadratwurzeln) | H3 Kap. 3L–M | Annahme | Lehrwerk erst Jahr 3 |
| `funktionen.grundbegriffe` | 1 | **ändern auf 4** | Modelle | MYP 1–3: „nicht altersgemäß“; Standard: Funktionsschreibweise; Extended: Definitions-/Wertebereich | H5E Kap. 20 | Annahme | Framework spricht klar gegen Jahr 1; Lehrwerk sogar Jahr 5 |
| `mengen.grundbegriffe` | 1 | **ändern auf 3** | Statistik | Extended (Mengen, bis drei Mengen) | H3 Kap. 2, H4 Kap. 5/7 | Annahme | Framework (Extended) und Lehrwerk (Jahr 3) widersprechen sich |
| `zahlen.ganz` | 2 | **bleibt 2** | Zahl | MYP 1–3 | H1 Kap. 13, H2 Kap. 5 | üblich | |
| `groessen.einheiten` | 2 | **bleibt 2** | Geometrie | MYP 1–3 | H1 Kap. 8–9, H2 Kap. 14 | üblich | |
| `groessen.proportional` | 2 | **bleibt 2** | Zahl | Verhältnisse MYP 1–3; direkte/indirekte Proportionalität Standard | H2 Kap. 16, H4 Kap. 25 | Annahme | |
| `groessen.verhaeltnisse` | 2 | **bleibt 2** | Zahl | MYP 1–3 | H2 Kap. 16 | üblich | |
| `daten.kennwerte` | 2 | **bleibt 2** | Statistik | MYP 1–3 | H1 Kap. 18G, H2 Kap. 18 | üblich | |
| `stochastik.grundbegriffe` | 2 | **bleibt 2** | Statistik | MYP 1–3 | H2 Kap. 17 | üblich | |
| `stochastik.simulation` | 2 | **bleibt 2** | Statistik | experimentelle Wahrscheinlichkeit MYP 1–3; Simulation, Monte-Carlo: kein Beleg | kein Beleg gefunden | Annahme | |
| `stochastik.kombinatorik` | 2 | **Entscheidung 8** | Statistik | Ergebnismengen MYP 1–3; Abzählprinzipien, Permutationen: **Enrichment** | H5E Kap. 28 („Vorbereitung Analysis HL“) | Annahme | nur Etappe „Alle Möglichkeiten systematisch finden“ passt zu Jahr 2 |
| `gleichungen.ungleichungen` | 2 | **ändern auf 4** | Zahl | einfache Ungleichungen MYP 1–3; Lösen, zusammengesetzte: Standard | H4 Kap. 6D–E | üblich | |
| `gleichungen.linear` | 2 | **bleibt 2** | Algebra | MYP 1–3 | H2 Kap. 10, H3 Kap. 7 | üblich | |
| `messen.kreisberechnung` | 2 | **ändern auf 3** | Geometrie | MYP 1–3 | H3 Kap. 11–12; Sektor H4 Kap. 12E | üblich | |
| `daten.boxplot` | 2 | **ändern auf 4** | Statistik | Standard (Quartile, Boxplots) | H4 Kap. 27H | sicher | Median-Teil passt schon früher |
| `zahlen.potenzen_zehner` | 3 | **ändern auf 4** | Zahl | Standard (Standardform) | H4 Kap. 3C–D, H5E Kap. 1C | üblich | |
| `terme.potenzgesetze` | 3 | **bleibt 3** | Zahl | Standard (ganzzahlige, negative Exponenten) | H3 Kap. 6, H4 Kap. 3 | üblich | Framework 4–5, Lehrwerk 3 |
| `gleichungen.lgs2` | 3 | **ändern auf 4** | Modelle | Standard | H4 Kap. 18 | üblich | |
| `funktionen.linear` | 3 | **bleibt 3** | Modelle/Geometrie | Standard | H3 Kap. 14, H4 Kap. 17 | üblich | Framework 4–5, Lehrwerk 3 |
| `messen.koerper_darstellung` | 3 | **bleibt 3** | Geometrie | MYP 1–3 | H1 Kap. 5, H2 Kap. 13 | Annahme | Lehrwerk Jahr 1–2 |
| `zahlen.reell` | 3 | **ändern auf 4** | Zahl | irrationale Zahlen, Surds: Standard; Nenner rational machen: **Enrichment** | H3 Kap. 3N–O, H4 Kap. 8 | üblich | |
| `abbildungen.aehnlichkeit` | 3 | **bleibt 3** | Geometrie | Standard (Ähnlichkeit); Streckung mit rationalem Faktor: Extended | H3 Kap. 19, H4 Kap. 22 | üblich | |
| `trigo.pythagoras` | 3 | **bleibt 3** | Trigonometrie | Standard | H3 Kap. 20, H4 Kap. 9 | üblich | Framework 4–5, Lehrwerk 3 |
| `trigo.rechtwinklig` | 3 | **ändern auf 4** | Trigonometrie | Standard | H4 Kap. 23 | üblich | |
| `abbildungen.kongruenz` | 3 | **bleibt 3** | Geometrie | Spiegelung MYP 1–3; Isometrien, Parkett: Standard; Drehung um einen Punkt: Extended | H1 Kap. 19, H2 Kap. 19 | Annahme | Lehrwerk Jahr 1–2 |
| `geometrie.konstruktion` | 3 | **bleibt 3** | Geometrie | Winkel an Parallelen MYP 1–3; Kongruenz Standard | H2 Kap. 3, 11; H3 Kap. 19 | üblich | |
| `raum.pyramide_kegel_kugel` | 3 | **bleibt 3** | Geometrie | MYP 1–3; weitere Körper Extended | H3 Kap. 12, H4 Kap. 13 | üblich | |
| `daten.zweidimensional` | 3 | **ändern auf 5** | Statistik | Standard (Streudiagramm, Ausgleichsgerade, qualitative Korrelation); quantitativ: Extended | H5E Kap. 19 | üblich | |
| `gleichungen.quadratisch` | 4 | **bleibt 4** | Algebra | Standard; Δ < 0: Extended | H4 Kap. 20, H5E Kap. 9 | üblich | Lösungsformel im Lehrwerk Jahr 5 |
| `funktionen.quadratisch` | 4 | **bleibt 4** | Modelle | Standard; Transformationen: Extended | H4 Kap. 21 | üblich | |
| `funktionen.gebrochen` | 4 | **bleibt 4** | Modelle | Extended (rationale Funktionen) | kein Beleg gefunden | Annahme | |
| `funktionen.potenz` | 4 | **bleibt 4** | Modelle | Extended („komplexere Funktionen“) | H4 Kap. 25B (nur Potenzen in Proportionen) | Annahme | |
| `raum.schraegbilder` | 4 | **bleibt 4** | Geometrie | 3D-Koordinaten: Enrichment; Rotationskörper, windschief: kein Beleg | H5E Kap. 10J | Annahme | |
| `trigo.allgemein` | 4 | **bleibt 4** | Trigonometrie | Sinus-/Kosinussatz: Extended (laut Lehrwerk; Framework-Zusammenfassung nennt Standard); Einheitskreis: Enrichment | H4 Kap. 29 (online), H5E Kap. 16 | üblich | |
| `stochastik.verknuepft` | 4 | **bleibt 4** | Statistik | Extended (Venn-Diagramme, Additionsregel, bedingte WK) | H4 Kap. 26, Kap. 7 | üblich | |
| `geometrie.kreis` | 4 | **bleibt 4** | Geometrie | Extended (Kreisgeometrie); Um-/Inkreis: Enrichment | H4 Kap. 24, H5E Kap. 14 | üblich | |
| `sonder.graphentheorie` | 4 | **bleibt 4** | Modelle | Extended (Netzwerke) | H4 Kap. 28 (online) | üblich | |
| `funktionen.exponential_log` | 4 | **ändern auf 5** | Modelle/Zahl | Logarithmen Extended; Exponentialfunktionen laut Guide-Zusammenfassung Enrichment | H5E Kap. 23 | üblich | |
| `funktionen.trig` | 4 | **ändern auf 5** | Modelle | Extended (Graphen trigonometrischer Funktionen); Bogenmaß Enrichment | H5E Kap. 24 | üblich | |
| `funktionen.ganzrational` | 4 | **ändern auf 5** | Modelle | Enrichment (kubische Funktionen) | H5E-2014 Kap. 24 (Polynome) | Annahme | |
| `abbildungen.matrizen` | 4 | **ändern auf 5** | Zahl/Geometrie | Guide 2020: kein Beleg gefunden; Guide 2014: Extended | H5E-2014 Kap. 28 (online) | Annahme | |
| `funktionen.umkehr` | 4 | **ändern auf 5** | Modelle | Enrichment (Umkehrfunktionen) | H5E Kap. 20H (online, „nicht im Framework“) | üblich | |
| `daten.standardabweichung` | 4 | **ändern auf 5** | Statistik | Extended | H5E Kap. 18G | üblich | |
| `stochastik.bedingt` | 4 | **ändern auf 5** | Statistik | Extended | H5E Kap. 17H; abhängige Ereignisse H4 Kap. 26E | üblich | |
| `funktionen.betrag` | 4 | **ändern auf 5** | Modelle | Betrag als Zahl MYP 1–3; Betragsfunktion: Annahme Extended | H5E Kap. 20F | üblich | |
| `funktionen.folgen` | 4 | **ändern auf 5** | Algebra | Folgen (Stufe in der Zusammenfassung unklar; andere Quellen: Extended) | H1 Kap. 14 (einfache Folgen), H5E Kap. 22A–C | Annahme | |
| `funktionen.reihen` | 4 | **ändern auf 5** | Algebra | Enrichment (Reihen, Summenzeichen) | H5E Kap. 22E–G („nicht im Framework“) | üblich | |
| `sonder.optimierung` | 4 | **ändern auf 5** | Modelle | Extended (lineare Optimierung) | H5E Kap. 12E–F | üblich | |

**Ergebnis Teil 3:** 61 Themen: 38 bleiben, **22 ändern**, 1 offen (`stochastik.kombinatorik`). Sicherheit: 1 sicher, 44 üblich, 16 Annahme. Kein Thema ist heute auf Jahr 5 – 12 Vorschläge setzen Jahr 5 (Entscheidung 7).

### Themen ohne `ib_myp`, die laut Framework/Lehrwerk dazugehören (Vorschlag nachtragen)

| Thema | Jahr | Stufe | Lehrwerk | Sicherheit |
|---|---|---|---|---|
| `zahlen.natuerlich` | 1 | MYP 1–3 | H1 Kap. 1 | üblich |
| `zahlen.teilbarkeit` | 1 | MYP 1–3 | H1 Kap. 4 | üblich |
| `geometrie.winkelsaetze` | 2 | MYP 1–3 | H2 Kap. 3, 11 | üblich |
| `daten.stichproben` | 2 | MYP 1–3 (Stichprobenverfahren) | H2 Kap. 18A | üblich |
| `terme.umformen` | 3 | MYP 1–3 / Standard | H3 Kap. 4, 6 | üblich |
| `bruch.prozent_grundwert` | 3 | MYP 1–3 | H3 Kap. 5F–H | üblich |
| `zahlen.intervalle` | 4 | Standard | H4 Kap. 5E | üblich |
| `gleichungen.bruch` | 4 | Standard | H4 Kap. 6B | üblich |
| `gleichungen.potenz` | 4 | Standard | H4 Kap. 8E | üblich |
| `gleichungen.formeln` | 4 | Standard (Formeln umstellen) | H3 Kap. 10, H4 Kap. 10 | üblich |
| `finanzen.zinsen`, `finanzen.zinseszins` | 4 | – | H4 Kap. 11D–E | Annahme |
| `terme.bruchterme` | 4 | – | H4 Kap. 15 | üblich |
| `gleichungen.reinquadratisch` | 4 | Standard | H4 Kap. 20B | üblich |
| `groessen.indirekt` | 4 | Standard | H4 Kap. 25C | üblich |
| `stochastik.mehrstufig` | 4 | Extended (Baumdiagramme) | H4 Kap. 26F | üblich |
| `sonder.logik` | 4 | kein Beleg im Framework | H4 Kap. 30 (online) | Annahme |
| `funktionen.transformation` | 5 | Extended (Transformationen quadratischer Funktionen) | H4 Kap. 21C, H5E Kap. 20E | Annahme |
| `zahlen.rationale_exponenten` | 5 | Extended | H5E Kap. 1B | üblich |
| `gleichungen.exponential` | 5 | Extended | H5E Kap. 23C | üblich |
| `gleichungen.trig` | 5 | Extended | H5E Kap. 24G | üblich |
| `zahlen.schranken` | 5 | Extended (obere/untere Schranken) | kein Beleg in den gelesenen Haese-Bänden | Annahme |
| `daten.normalverteilung` | 5 | kein Beleg im Framework | H5E Kap. 18H | Annahme |

Kein Beleg für IB gefunden: `geometrie.ortslinien`, `abbildungen.determinanten2`, `funktionen.scharen`, `terme.quadratische_extreme` (Scheitel-Optimierung steckt in H5E Kap. 21H), `gleichungen.wurzel`, `gleichungen.lgs3`, `gleichungen.polynom`, `abbildungen.vektoren` (Vektoren: Enrichment; H5E Kap. 27 „nicht im Framework“).

### Was aus dem Framework fehlt

**Standard (und MYP 1–3):**
- Zeit: Zeitzonen, 24-Stunden-Uhr, Fahrpläne (MYP 1–3; H1 Kap. 11, H3 Kap. 13) – **fehlt**.
- Peilungen/Kurswinkel mit Trigonometrie (Standard; H4 Kap. 23G) – fehlt.
- Statistik: Stängel-Blatt-Diagramme, gruppierte Daten, kumulative Häufigkeit (Summenkurve), Perzentile, Quartilsabstand (MYP 1–3 bzw. Standard; H2 Kap. 18F, H4 Kap. 27F) – fehlt (Quartile nur in `daten.boxplot`).
- Algorithmen und Flussdiagramme (Algebra/Modelle) – fehlt.
- Zahlensysteme mit anderen Basen (Zahl, MYP 4–5) – fehlt (gleiche Lücke wie Realschule Teil 2 Nr. 2).
- Faktorisieren quadratischer Terme x² + bx + c und ax² + bx + c (H4 Kap. 14) – nur verstreut (`gleichungen.quadratisch`, `terme.umformen`), kein eigenes Thema.
- Streckungen in eine Richtung („stretches“, H4 Kap. 19E), Parkettierungen – nur Vertiefungs-Etappe.

**Extended (getrennt):**
- Kreissätze: Sehnensatz, Mittelpunkts- und Umfangswinkel, Sehnenviereck (H5E Kap. 14B–I) – fehlt (`geometrie.kreis` hat nur Thales, Tangente, Um-/Inkreis).
- Histogramme mit stetigen Klassen – nur innerhalb `daten.normalverteilung`.
- Mengen mit drei Mengen – fehlt.
- Logarithmen zu anderen Basen, Logarithmengesetze vollständig (H5E Kap. 23G–I) – nur teilweise.
- Quantitative Korrelation (Korrelationskoeffizient mit Technologie, H5E Kap. 19C) – nach Etappen-Titeln nicht enthalten.
- Obere/untere Schranken: Thema `zahlen.schranken` vorhanden, aber ohne Jahr.

### Vorschlag `reihenfolge.ib_myp` (nur wo belegbar: Reihenfolge der Haese-Kapitel im vorgeschlagenen Jahr)

- **MYP 1:** 1 [`zahlen.natuerlich`] · 2 `zahlen.rechengesetze` · 3 `zahlen.potenzen_basis` · 4 `geometrie.grundbegriffe` · 5 `geometrie.winkel` · 6 [`zahlen.teilbarkeit`] · 7 `bruch.brueche` · 8 `bruch.dezimal` · 9 `messen.flaechen` · 10 `messen.koerper_berechnung` · 11 `bruch.prozent` · 12 `terme.aufstellen` · 13 `daten.darstellen` — ohne Beleg für eine Nummer: `gleichungen.einfach`, `zahlen.wurzeln_basis`
- **MYP 2:** 1 [`geometrie.winkelsaetze`] · 2 `zahlen.ganz` · 3 `bruch.rechnen` · 4 `gleichungen.linear` · 5 `groessen.einheiten` · 6 `groessen.verhaeltnisse` · 7 `groessen.proportional` · 8 `stochastik.grundbegriffe` · 9 `daten.kennwerte` · 10 [`daten.stichproben`] — ohne Beleg: `stochastik.simulation`, `stochastik.kombinatorik`
- **MYP 3:** 1 `mengen.grundbegriffe` · 2 [`terme.umformen`] · 3 [`bruch.prozent_grundwert`] · 4 `terme.potenzgesetze` · 5 `geometrie.konstruktion` · 6 `messen.kreisberechnung` · 7 `raum.pyramide_kegel_kugel` · 8 `funktionen.linear` · 9 `abbildungen.aehnlichkeit` · 10 `trigo.pythagoras` — ohne Beleg: `abbildungen.kongruenz`, `messen.koerper_darstellung`
- **MYP 4:** 1 `zahlen.potenzen_zehner` · 2 `gleichungen.ungleichungen` · 3 `zahlen.reell` · 4 `gleichungen.lgs2` · 5 `gleichungen.quadratisch` · 6 `funktionen.quadratisch` · 7 `trigo.rechtwinklig` · 8 `geometrie.kreis` · 9 `funktionen.potenz` · 10 `stochastik.verknuepft` · 11 `daten.boxplot` · 12 `sonder.graphentheorie` · 13 `trigo.allgemein` — ohne Beleg: `funktionen.grundbegriffe`, `funktionen.gebrochen`, `raum.schraegbilder`
- **MYP 5:** 1 `sonder.optimierung` · 2 `stochastik.bedingt` · 3 `daten.standardabweichung` · 4 `daten.zweidimensional` · 5 `funktionen.betrag` · 6 `funktionen.umkehr` · 7 `funktionen.folgen` · 8 `funktionen.reihen` · 9 `funktionen.exponential_log` · 10 `funktionen.trig` — ohne Beleg: `abbildungen.matrizen`, `funktionen.ganzrational`

Hinweis: Die Haese-Reihenfolge ist eine Lehrwerks-Reihenfolge, keine IB-Vorgabe. Sie verletzt an einer Stelle die Abhängigkeit (`funktionen.exponential_log` vor `funktionen.umkehr` wäre fachlich besser; Kap. 20 steht im Buch vor Kap. 23).

---

## Was der Nutzer entscheiden muss

1. **Realschule – 7 Klassen ändern?** `groessen.proportional` 5→6, `zahlen.potenzen_zehner` 5→7, `geometrie.konstruktion` 6→7, `raum.schraegbilder` 5→8, `funktionen.quadratisch` 8→9, `stochastik.grundbegriffe` 8→9, `stochastik.verknuepft` 8→9 (letzteres Annahme).
2. **Gruppe I oder II/III?** Die App hat nur ein Feld `rs_by`. Vorschlag: Gruppe I als Maßstab, Abweichungen der Gruppe II/III (Tabelle, Spalte II/III) nur als Hinweis. Alternative: zweites Feld (App-Wunsch).
3. **Etappen über dem RS-Lehrplan:** z. B. `terme.bruchterme` (5 von 7), `gleichungen.linear` (3 von 6), `abbildungen.kongruenz` (3 von 10), `bruch.prozent` (2), `gleichungen.ungleichungen` (2). „Vertiefung“ gilt heute je Thema für alle Schularten. Brauchen wir „Vertiefung je Schulart“ (App-Wunsch), oder bleibt es so?
4. **Umgekehrt:** Diese Etappen sind heute Vertiefung, an der Realschule aber Pflicht: „Winkel an einer Geradenkreuzung“ (M5 LB3), „Volumen von Quader und Würfel“ (M6 LB4), „Modalwert und Spannweite“ und „Der Median“ (M7 LB8). Dazu: `daten.boxplot` und `daten.kennwerte` überschneiden sich in Klasse 7 – zusammenlegen oder `daten.boxplot` nur für Gymnasium/IB?
5. **`rs_by` nachtragen** für `zahlen.natuerlich` (5), `zahlen.teilbarkeit` (5), `geometrie.winkelsaetze` (7), `terme.umformen` (7), `finanzen.zinsen` (7); optional `funktionen.gebrochen` (10).
6. **Neue Themen für die Realschule**, nach Dringlichkeit: (a) Flächeninhalt von Dreieck, Parallelogramm, Trapez, Drachen, Raute (M6 LB3 – fehlt in der ganzen App); (b) Zentrische Streckung im Koordinatensystem / Parameterverfahren (M9 LB2, Gruppe I); (c) Trigonometrie-Ergänzung Klasse 10 (Additionstheoreme, Winkel zwischen Geraden); (d) Vierecke und Drehung (M8 LB1/LB2).
7. **IB – Jahr 5 zulassen?** Heute nutzt kein Thema `ib_myp` = 5. 12 Vorschläge setzen 5 (Extended/Enrichment-Stoff). Dazu 10 weitere Änderungen. Soll die App „Standard / Extended / Enrichment“ kennzeichnen (App-Wunsch)?
8. **IB – zwei Widersprüche:** `stochastik.kombinatorik` (Zählprinzip/Permutationen sind im Framework nur Enrichment) und `mengen.grundbegriffe` (Framework: Extended; Lehrwerk: Jahr 3). Vorschlag: Kombinatorik für IB auf Jahr 5 oder ohne Jahr; Mengen Jahr 3.
9. **Reihenfolge-Konflikt IB Jahr 1:** `zahlen.rechengesetze` und `zahlen.potenzen_basis` (Jahr 1) enthalten Etappen mit negativen Zahlen, `zahlen.ganz` ist Jahr 2. `zahlen.ganz` auf Jahr 1 ziehen (Lehrwerk H1 Kap. 13 erlaubt das) oder die Etappen für IB als Vertiefung?

## Zusatzfunde (nicht Teil des Auftrags)

- Flächeninhalt der Vielecke (Teil 2 Nr. 4) fehlt vermutlich auch dem Gymnasium-Bestand. Im Gymnasium-Lehrplan nicht nachgeprüft – Annahme.
- `messen.flaechen` und `trigo.allgemein` versprechen im Feld `umfang` mehr, als die Etappen enthalten (Dreieck/Parallelogramm/Trapez bzw. Additionstheoreme).
- Mehrere Themen nennen im `umfang` Stoff höherer Klassen (z. B. `terme.potenzgesetze`: rationale Exponenten; `abbildungen.vektoren`: Skalarprodukt). Das betrifft nur den Beschreibungstext.

## Quellen

LehrplanPLUS Realschule Mathematik (ISB), abgerufen 17.11.2026:
- RS5: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/5/mathematik
- RS6: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/6/mathematik
- RS7-I: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg1 · RS7-II: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/7/mathematik/wpfg2-3
- RS8-I: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg1 · RS8-II: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/8/mathematik/wpfg2-3
- RS9-I: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg1 · RS9-II: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/9/mathematik/wpfg2-3
- RS10-I: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg1 · RS10-II: https://www.lehrplanplus.bayern.de/fachlehrplan/realschule/10/mathematik/wpfg2-3
- Übersicht Gleichungen (Zuordnung der Lernbereiche I und II/III): https://www.lehrplanplus.bayern.de/serviceinformation/l311733

IB MYP:
- IB, „Mathematics guide“ (MYP, für Unterricht ab Sept. 2020/Jan. 2021), Framework S. 22–29 (Kopie einer Schule): https://franklin2017.s3.amazonaws.com/2/ckeditor/Mathematics%20Sept%2020%20Jan%2021_3esOao7RJc.pdf
- IB, MYP-Mathematik Übersicht: https://ibo.org/programmes/middle-years-programme/curriculum/mathematics/
- H1: https://www.haesemathematics.com/books/mathematics-6-myp-1-3rd-edition
- H2: https://www.haesemathematics.com/books/mathematics-7-myp-2-3rd-edition
- H3: https://haesemathematics.com/books/mathematics-8-myp-3-3rd-edition
- H4: https://www.haesemathematics.com/books/mathematics-9-myp-4-3rd-edition
- H5E (3. Aufl., Kapitelübersicht): https://www.haesemathematics.com/media/W1siZiIsIjIwMjIvMDYvMTQvOWttbWdlZDdmZ19teXBfNV9leHRfM2VkX2NoYXB0ZXJfc3VtbWFyaWVzLnBkZiJdXQ/myp-5-ext-3ed-chapter-summaries.pdf?sha=3f1a7c9e45ef650e
- H5E-2014: https://www.haesemathematics.com/books/mathematics-for-the-international-student-10e-myp-5-extended

Daten: `inhalte/themenliste.json` und `inhalte/themen/*.json` (Zweig lernen-app, Commit 5a982a2).
