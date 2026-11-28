# Runde 15: Auswahl der Einheiten (Zahlen vor dem Schreiben der Aufgaben)

Stand der Zahlen: Bestand der Einheiten und Aufgaben in neuer Form aus den Runden 1 bis 14 (`tools/rollend_sql.py`-Sammlung, Zählung mit denselben Dateien; Etappen = `lz` der Einheit in `inhalte/plan/rollend-einheiten.json`).
„neu“ = Aufgaben aus den Runden 1 bis 14 in den neuen Formen (Vorrat). Anteil = neu : (Bestand + neu).

**Hinweis zum Ablauf:** Die Auswahl wurde zu Beginn der Arbeit anhand dieser Zahlen getroffen, die Datei selbst wurde erst nach dem Schreiben der Aufgaben angelegt (nicht, wie verlangt, davor). Die Zahlen unten sind aus dem Stand vor Runde 15 neu gezählt und ändern sich dadurch nicht.

## Kriterium

- **Klasse 7:** Einheiten, die in R8, R9, R10 und R14 **nicht** aufgefüllt wurden. R8 hat `geometrie.kreis` und `daten.boxplot` bedient, R14 hat `terme.aufstellen` bedient; alle drei bleiben deshalb draußen. Übrig bleiben sieben Einheiten, alle sieben sind gewählt.
- **Klasse 9:** Alle acht Einheiten, die in `rollend-einheiten.json` stehen, wurden in R9/R10 nur mit genau 3 Aufgaben je Etappe bedient (dünnster Stand). Gewählt sind die sieben mit dem niedrigsten Anteil (6,4 bis 7,4 %); `abbildungen.aehnlichkeit` (7,6 %, höchster Anteil der Klasse 9) bleibt für eine spätere Runde.
- Andere Klasse-9-Einheiten gibt es in `rollend-einheiten.json` nicht; was dort nicht steht, kann nicht eingespielt werden (nur Einheiten der Liste sind lieferbar). Deshalb gibt es keine weiteren Kandidaten.

## Zahlen vor Runde 15

| Klasse | Einheit | Aufgaben gesamt (Bestand) | in neuer Form (R1 bis R14) | Anteil neu | gewählt |
|---|---|---|---|---|---|
| 7 | `bruch.prozent_grundwert` | 289 | 36 | 11.1 % | ja |
| 7 | `terme.aufstellen` | 216 | 36 | 14.3 % | nein |
| 7 | `terme.potenzgesetze_natuerlich` | 226 | 17 | 7.0 % | ja |
| 7 | `terme.umformen` | 295 | 28 | 8.7 % | ja |
| 7 | `abbildungen.kongruenz` | 405 | 26 | 6.0 % | ja |
| 7 | `geometrie.winkelsaetze` | 315 | 37 | 10.5 % | ja |
| 7 | `geometrie.konstruktion` | 244 | 22 | 8.3 % | ja |
| 7 | `geometrie.kreis` | 216 | 18 | 7.7 % | nein |
| 7 | `daten.boxplot` | 258 | 18 | 6.5 % | nein |
| 7 | `gleichungen.linear` | 243 | 34 | 12.3 % | ja |
| 9 | `zahlen.wurzeln_basis` | 264 | 18 | 6.4 % | ja |
| 9 | `zahlen.reell` | 315 | 24 | 7.1 % | ja |
| 9 | `gleichungen.quadratisch` | 325 | 24 | 6.9 % | ja |
| 9 | `funktionen.quadratisch` | 340 | 27 | 7.4 % | ja |
| 9 | `abbildungen.aehnlichkeit` | 327 | 27 | 7.6 % | nein |
| 9 | `trigo.pythagoras` | 253 | 18 | 6.6 % | ja |
| 9 | `trigo.rechtwinklig` | 287 | 21 | 6.8 % | ja |
| 9 | `stochastik.verknuepft` | 426 | 33 | 7.2 % | ja |

## Je Etappe (Bestand / neu vor Runde 15), nur gewählte Einheiten

Nur Etappen, die zur Einheit in `rollend-einheiten.json` gehören. Nicht dazu gehören bei `terme.umformen` summe_mal_summe, ausklammern, binomisch, gleichungen_binomisch, bei `abbildungen.kongruenz` sechs weitere Etappen (Verschiebung, Drehung, Vektoren u. a.) und bei `geometrie.konstruktion` vierecke und vierecke_konstruieren; diese gehören zu anderen Einheiten des Plans.

| Einheit | Etappe | Bestand | neu |
|---|---|---|---|
| `bruch.prozent_grundwert` | faktor | 39 | 5 |
| `bruch.prozent_grundwert` | vermehrt | 39 | 4 |
| `bruch.prozent_grundwert` | vermindert | 38 | 4 |
| `bruch.prozent_grundwert` | zurueck | 38 | 5 |
| `bruch.prozent_grundwert` | prozentsatz | 36 | 3 |
| `bruch.prozent_grundwert` | mehrfach | 34 | 5 |
| `bruch.prozent_grundwert` | formel | 30 | 6 |
| `bruch.prozent_grundwert` | argumente | 35 | 4 |
| `terme.potenzgesetze_natuerlich` | mal_gleiche_basis | 56 | 3 |
| `terme.potenzgesetze_natuerlich` | gleicher_exponent | 45 | 4 |
| `terme.potenzgesetze_natuerlich` | potenz_von_potenz | 35 | 4 |
| `terme.potenzgesetze_natuerlich` | geteilt_gleiche_basis | 48 | 3 |
| `terme.potenzgesetze_natuerlich` | anwenden | 42 | 3 |
| `terme.umformen` | zusammenfassen | 32 | 5 |
| `terme.umformen` | produkte | 32 | 6 |
| `terme.umformen` | minusklammer | 35 | 5 |
| `terme.umformen` | ausmultiplizieren | 36 | 6 |
| `terme.umformen` | aequivalenz | 36 | 6 |
| `abbildungen.kongruenz` | achsenspiegelung | 37 | 6 |
| `abbildungen.kongruenz` | mittelsenkrechte | 32 | 6 |
| `abbildungen.kongruenz` | winkelhalbierende | 32 | 5 |
| `abbildungen.kongruenz` | symmetrie | 34 | 3 |
| `abbildungen.kongruenz` | vierecke_ordnen | 33 | 3 |
| `abbildungen.kongruenz` | eigenschaften | 37 | 3 |
| `geometrie.winkelsaetze` | scheitel_neben | 32 | 4 |
| `geometrie.winkelsaetze` | stufen_wechsel | 42 | 3 |
| `geometrie.winkelsaetze` | parallel_pruefen | 34 | 4 |
| `geometrie.winkelsaetze` | innenwinkelsumme | 37 | 5 |
| `geometrie.winkelsaetze` | aussenwinkel | 34 | 4 |
| `geometrie.winkelsaetze` | vieleck | 33 | 5 |
| `geometrie.winkelsaetze` | parkett | 35 | 4 |
| `geometrie.winkelsaetze` | figuren | 35 | 4 |
| `geometrie.winkelsaetze` | beweisen | 33 | 4 |
| `geometrie.konstruktion` | gleichschenklig | 35 | 5 |
| `geometrie.konstruktion` | kongruenzsatz | 37 | 4 |
| `geometrie.konstruktion` | konstruierbar | 37 | 5 |
| `geometrie.konstruktion` | planfigur | 31 | 4 |
| `geometrie.konstruktion` | satz_kehrsatz | 38 | 4 |
| `gleichungen.linear` | waage | 48 | 6 |
| `gleichungen.linear` | beide_seiten | 40 | 6 |
| `gleichungen.linear` | klammern | 43 | 5 |
| `gleichungen.linear` | probe | 38 | 6 |
| `gleichungen.linear` | sonderfaelle | 37 | 5 |
| `gleichungen.linear` | sach | 37 | 6 |
| `zahlen.wurzeln_basis` | quadratwurzel | 43 | 3 |
| `zahlen.wurzeln_basis` | wurzel_dezimal | 46 | 3 |
| `zahlen.wurzeln_basis` | kubikwurzel | 45 | 3 |
| `zahlen.wurzeln_basis` | abschaetzen | 47 | 3 |
| `zahlen.wurzeln_basis` | wurzel_deuten | 41 | 3 |
| `zahlen.wurzeln_basis` | wurzel_sache | 42 | 3 |
| `zahlen.reell` | zahlarten | 39 | 3 |
| `zahlen.reell` | eingrenzen | 44 | 3 |
| `zahlen.reell` | heron | 35 | 3 |
| `zahlen.reell` | wurzel_mal | 45 | 3 |
| `zahlen.reell` | teilweise | 44 | 3 |
| `zahlen.reell` | zusammenfassen | 42 | 3 |
| `zahlen.reell` | nenner_rational | 44 | 3 |
| `zahlen.reell` | irrational_beweis | 22 | 3 |
| `gleichungen.quadratisch` | reinquadratisch | 40 | 3 |
| `gleichungen.quadratisch` | ausklammern | 42 | 3 |
| `gleichungen.quadratisch` | faktorisieren | 43 | 3 |
| `gleichungen.quadratisch` | ergaenzung | 42 | 3 |
| `gleichungen.quadratisch` | loesungsformel | 43 | 3 |
| `gleichungen.quadratisch` | bruchgleichung | 31 | 3 |
| `gleichungen.quadratisch` | diskriminante | 41 | 3 |
| `gleichungen.quadratisch` | sachaufgabe | 43 | 3 |
| `funktionen.quadratisch` | scheitel | 40 | 3 |
| `funktionen.quadratisch` | parameter | 42 | 3 |
| `funktionen.quadratisch` | spiegeln | 34 | 3 |
| `funktionen.quadratisch` | umformen | 30 | 3 |
| `funktionen.quadratisch` | nullstellen | 42 | 3 |
| `funktionen.quadratisch` | punkte | 43 | 3 |
| `funktionen.quadratisch` | bestimmen | 46 | 3 |
| `funktionen.quadratisch` | schnittpunkte | 33 | 3 |
| `funktionen.quadratisch` | extremwert | 30 | 3 |
| `trigo.pythagoras` | hypotenuse | 44 | 3 |
| `trigo.pythagoras` | kathete | 43 | 3 |
| `trigo.pythagoras` | umkehrung | 44 | 3 |
| `trigo.pythagoras` | koordinaten | 41 | 3 |
| `trigo.pythagoras` | raum | 42 | 3 |
| `trigo.pythagoras` | anwendung | 39 | 3 |
| `trigo.rechtwinklig` | seiten | 42 | 3 |
| `trigo.rechtwinklig` | verhaeltnisse | 41 | 3 |
| `trigo.rechtwinklig` | seite | 45 | 3 |
| `trigo.rechtwinklig` | winkel | 45 | 3 |
| `trigo.rechtwinklig` | beziehungen | 42 | 3 |
| `trigo.rechtwinklig` | anwendung | 42 | 3 |
| `trigo.rechtwinklig` | schnittwinkel | 30 | 3 |
| `stochastik.verknuepft` | elemente | 36 | 3 |
| `stochastik.verknuepft` | schnitt | 38 | 3 |
| `stochastik.verknuepft` | verknuepfen | 39 | 3 |
| `stochastik.verknuepft` | additionssatz | 43 | 3 |
| `stochastik.verknuepft` | venn | 40 | 3 |
| `stochastik.verknuepft` | mengen_verstehen | 33 | 3 |
| `stochastik.verknuepft` | vierfeld | 40 | 3 |
| `stochastik.verknuepft` | tafel_wkeit | 42 | 3 |
| `stochastik.verknuepft` | bedingt | 39 | 3 |
| `stochastik.verknuepft` | rueckschluss | 35 | 3 |
| `stochastik.verknuepft` | verstehen | 41 | 3 |

## Ergebnis

14 Einheiten (7 in Klasse 7, 7 in Klasse 9). Geschrieben wurden 12 bis 18 Aufgaben je Einheit, in jeder Etappe der Einheit mindestens eine zählende Aufgabe auf Stufe 2 oder 3.

Zweifel an der Auswahl für den Vorprüfer: Bei den sieben Klasse-7-Einheiten haben `bruch.prozent_grundwert` (11,1 %), `geometrie.winkelsaetze` (10,5 %) und `gleichungen.linear` (12,3 %) einen höheren Anteil als die in R8 bedienten `daten.boxplot` (6,5 %) und `geometrie.kreis` (7,7 %). Sie sind gewählt, weil sie in keiner der Runden R8, R9, R10, R14 vorkamen (Kriterium oben); wer lieber nach dem reinen Anteil auswählt, tauscht sie in einer späteren Runde gegen Boxplot und Kreis.

## Vormerkung für Runde 16 (Gegenprüfung 1197)

`daten.boxplot` und `geometrie.kreis` (Klasse 7) wurden in R15 nicht bedient und stehen für die nächste Runde vor.
