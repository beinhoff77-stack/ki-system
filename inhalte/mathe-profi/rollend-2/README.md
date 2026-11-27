# Rollendes System, Stufe 2 – Aufgaben auf Vorrat für die übernächsten sechs Flüge

Auftrag 18, Stand 27.11.2026. Nur Inhalte. **Nichts ist eingespielt.** Erzeugt und geprüft von `bauen.py` (endet mit „OK“).
Zeichen: **[G]** gesichert (vom Programm geprüft oder in einer Datei nachgesehen), **[A]** Annahme, **[M]** meine Einschätzung.

## Was hier liegt

| Datei | Flug | für | Thema | ohne Bau | `bedingung` | Lernkarten | mit Zeichnung |
|---|---|---|---|---|---|---|---|
| `a1.json` | Einfache Gleichungen | Kind 1 | `gleichungen.einfach` | 15 | 5 | 5 von 5 | 0 |
| `d1.json` | Daten darstellen | Kind 1 | `daten.darstellen` | 14 | 5 | 6 von 6 | 5 |
| `g1.json` | Größen und Einheiten | Kind 1 | `groessen.einheiten` | 14 | 5 | 8 von 8 | 0 |
| `g8.json` | Prozent mit verändertem Grundwert | Kind 2 | `bruch.prozent_grundwert` | 15 | 5 | 8 von 8 | 1 |
| `g2-teil2.json` | Dreisatz · Teil 2 | Kind 2 | `groessen.proportional` (drei Lernkarten) | 13 | 5 | 3 von 3 | 2 |
| `f1.json` | Funktionsbegriff | Kind 2 | `funktionen.grundbegriffe` | 15 | 5 | 9 von 9 | 4 |

Zusammen **116 Aufgaben**: 86 ohne Bau, 30 des Typs `bedingung`. Aufbau jeder Datei wie in `rollend-1/README.md` (Zusatzangaben je Eintrag, darunter die Aufgabe im Format von `inhalte/README.md`).

**Typen der 86 Aufgaben ohne Bau:** Umkehren 21, Fehler-Detektiv 18, Lückenweg 12, Brücke 12, Verfahren wählen 9, Zwei Wege vergleichen 8, Anwenden 6.
Gewöhnliche Anwendungsaufgaben sind damit 6 von 86 (in `rollend-1` waren es 18 von 56): `A1-15`, `D1-14`, `G1-10`, `G1-12`, `G8-10`, `G2T2-13`.

## Geprüft [G]

- Jede Rechenaufgabe zweifach nachgerechnet: Feld `c` mit dem Rechner aus `tools/inhalt_pruefen.py`, dazu ein zweiter Weg im Programm (91 Rechnungen).
- Jede Auswahl-Aufgabe hat eine Probe; jede falsche Antwort ist beschrieben (194 Fehlbilder, 69 davon mit Fehlbild-Kennung aus `kennungen.json`; wo ich nicht sicher war, steht keine).
- Jede `bedingung`-Aufgabe: `pruefe_aufgabe` aus dem **aktuellen** `tools/bedingung.py` liefert eine leere Fehlerliste. Zusätzlich: Jede gute Antwort wird als richtig bewertet; jedes Gegenbeispiel scheitert genau an der genannten Bedingung und bekommt einen lesbaren Hinweis; jede Bedingung hat mindestens ein Gegenbeispiel. Höchstens vier Felder.
- Alle Aufgaben an eine Kopie ihrer Themen-Datei gehängt: `tools/inhalt_pruefen.py` meldet vorher und nachher keinen Fehler. Kein Aufgabentext steht wörtlich schon im Bestand.
- Jede Regel-Kennung und jede Fehlbild-Kennung gibt es in `regeln-uebersicht/kennungen.json`.
- Schwierigkeit in jeder Datei aufsteigend; bei Auswahl-Aufgaben liegt die richtige Antwort auf wechselnden Plätzen.

## 1. Die 20 Aufgaben aus `rollend-1` gegen den aktuellen Stand

`rollend-1/bauen.py` neu gelaufen, mit `tools/bedingung.py` vom 27.11. (Namen als nichtleerer Text, `hinweis` als Text, `min`/`max` ganzzahlig, strenge Typen in jedem Ast, ein Vorzeichen): **Alle 20 bestehen** – leere Fehlerliste, jede gute Antwort richtig bewertet. [G]

## 2. Namen der Bedingungen: Forderung, nicht Weg

Regel: Der Name nennt, was der Aufgabentext verlangt. Er nennt nicht, wie man es erreicht.

**In `rollend-1` geändert** (sechs Namen in drei Aufgaben; Prüf-Bäume und Hinweise unverändert, `ge2.json` neu geschrieben):

| Aufgabe | alt | neu |
|---|---|---|
| `GE2-B1` Spiegelbild an der y-Achse | „Höhe bleibt“ | „y′ gehört zum Spiegelbild“ |
| `GE2-B1` | „gleich weit auf der anderen Seite“ | „x′ gehört zum Spiegelbild“ |
| `GE2-B4` Achse und Bildpunkt | „Höhe bleibt“ | „y′ gehört zum Spiegelbild“ |
| `GE2-B4` | „Achse in der Mitte“ | „Achse passt zu A und A′“ |
| `GE2-B5` Punktspiegelung | „Z ist die Mitte in x-Richtung“ | „Z passt zu P und P′ (x-Richtung)“ |
| `GE2-B5` | „Z ist die Mitte in y-Richtung“ | „Z passt zu P und P′ (y-Richtung)“ |

Die übrigen 14 Aufgaben aus `rollend-1` habe ich gelesen: Ihre Namen wiederholen nur den Aufgabentext („Produkt ist 48“, „links von der y-Achse“). Keine Änderung.

**Muster-Fälle (`tools/tests/bedingung_faelle.json`) – nur Liste, Datei unverändert:**

| Aufgabe | Name | Befund | Vorschlag |
|---|---|---|---|
| 3 „a · x + b = 3x − 6 hat keine Lösung“ | „x fällt weg“ | verrät den ersten Gedanken | „nicht genau eine Lösung“ |
| 3 | „es bleibt eine falsche Aussage“ | verrät den zweiten Gedanken | „nicht jede Zahl ist Lösung“ |
| 1, 2, 4 bis 10 | – | Namen wiederholen den Aufgabentext | bleibt |
| 11 bis 17 | – | Prüf-Fälle ohne Inhalt für Kinder | bleibt |

**Was ich dabei nicht geändert habe [M]:** die Hinweise. Ein Hinweis darf nach einem Fehlversuch helfen. Bei den drei Spiegel-Aufgaben sagt er aber weiter, woran es liegt („nicht auf gleicher Höhe“). Wenn auch der Hinweis den Weg nicht nennen soll, ist das eine zweite Runde – dann verliert er aber seinen Nutzen.

In den 30 neuen Aufgaben sind alle Namen nach der Regel geschrieben; ich habe jeden einzeln gegen den Aufgabentext gelesen. Kein Name ist länger als 40 Zeichen. [G für die Länge, M für das Lesen]

## 3. Welche Lernkarten erst mit Grafik-Aufgaben gut abgedeckt wären

Zwei Dinge sind zu trennen. **Anzeigen** kann die App schon (Tabelle, Säulen, Kreis, Koordinatensystem) – das habe ich in 12 Aufgaben genutzt, weil es keinen Bau braucht. **Eingeben** in einer Zeichnung (Säule einstellen, Punkt setzen, Winkel abtragen) kann sie nicht; das wäre späterer Bau.

| Flug | Lernkarte | Was ohne Grafik-Eingabe fehlt | Stand in dieser Lieferung |
|---|---|---|---|
| a1 | `waage` | Die Waage sehen und selbst von beiden Seiten wegnehmen. | 3 + 1 Aufgaben, die Waage steht nur im Text. Die Aufgaben tragen, das Bild fehlt. |
| d1 | `saeulendiagramm` | Eine Säule selbst in der richtigen Höhe zeichnen; Maßstab wählen und sehen, was passiert. | Ablesen ist da (`D1-09`), Zeichnen nicht. **Schwach abgedeckt.** |
| d1 | `kreisdiagramm` | Den Winkel abtragen. | Nur Winkel ausrechnen und Diagramm lesen. **Schwach abgedeckt.** |
| d1 | `absolute_haeufigkeit` | Strichliste selbst führen. | Zählen aus einer Zahlenreihe; trägt für die Idee, nicht für das Handwerk. |
| g1 | `schaetzen` | Bilder von Gegenständen neben einer Bezugsgröße. | Nur 1 Aufgabe. **Bewusst nicht aufgefüllt.** |
| g1 | `massstab` | Auf einer Karte messen. | Rechnen mit dem Maßstab ist da; das Messen fehlt. |
| g1 | `verstehen` | – (keine Grafik nötig) | Nur 1 Aufgabe; hier fehlt mir eher eine gute Aufgabenform als ein Bild. |
| g8 | keine | – | Alle acht Lernkarten tragen ohne Grafik. |
| g2-teil2 | `erkennen` | Punkte einer Zuordnung ins Koordinatensystem setzen und sehen, ob sie auf einer Geraden durch den Ursprung liegen. | Im Text gelöst („zu 0 gehört 0“). Trägt, aber ohne Bild. |
| f1 | `graph_lesen` | Am Graphen einen Punkt antippen statt eine Zahl einzugeben. | Ablesen geht mit Anzeige (`F1-07`, `F1-08`). Gut genug. |
| f1 | `wertetabelle` | Aus der Tabelle den Graphen zeichnen. | Tabelle ↔ Term ist da, Tabelle → Graph nicht. **Schwach abgedeckt.** |
| f1 | `eindeutig` | Pfeildiagramm (gibt es als Zeichenart nicht). | Tabelle, Text und ein Kreis im Koordinatensystem. Trägt. |
| f1 | `nullstellen`, `funktionswert` | – | Je 1 + 1 Aufgabe. Der Bestand hat hier schon 42 und 49; ich habe nicht aufgefüllt. |

Kurz [M]: Wirklich auf Grafik-Eingabe warten sollten **Säulendiagramm, Kreisdiagramm (d1)** und **Wertetabelle → Graph (f1)**. Alles andere trägt mit dem, was die App heute kann.

## 4. Brüche

Acht Texte enthalten einen Bruchstrich: `D1-03` (12/18, 18/12, 12/30, 2/5), `F1-B5` (12/(x − a), 12/(2 + 1)) und seit Auftrag 20 `G8-01` (②/100) und `G8-04` (①/10). Alle stehen in einer der erkannten Formen (Zahl/Zahl, Zahl/(Klammer)). Das Programm bricht ab, wenn eine Form wie 1/2x oder eine verschachtelte Klammer im Bruch vorkommt. [G]
Sonst habe ich Brüche vermieden und „6 von 24“, „ein Viertel“ oder „:“ geschrieben.

## Nicht geprüft

- Kein Kind hat eine der Aufgaben gerechnet. Stufen und Zählvorschläge sind Einschätzungen.
- Die 12 Zeichnungen habe ich nicht in der App gesehen. Geprüft ist nur ihre Form nach `inhalte/README.md` (Art, Felder, Säulennamen höchstens 8 Zeichen, Kreis-Anteile zusammen 100).
- `bedingung`: nur gegen die Python-Referenz, nicht gegen die Fassung in der Datenbank.
- Ob der Bestand eine inhaltlich gleiche Aufgabe mit anderen Worten enthält. Geprüft ist nur der wörtlich gleiche Text. Nahe am Bestand sind nach meinem Lesen: `G8-08` (plus 20 %, minus 20 %) und `D1-01` (Würfe zählen).
- Wie die App die Brüche gestapelt darstellt.
- Lehrplan an der Quelle.

## Annahmen

- **Zeichnungen, die die App schon zeichnet, zählen als „ohne Bau“.** Falls nicht: Es entfallen `D1-05`, `D1-09`, `D1-11`, `D1-13`, `D1-14`, `G8-07`, `G2T2-06`, `G2T2-07`, `F1-05`, `F1-07`, `F1-08`, `F1-15`.
- `g2-teil2` umfasst die drei Lernkarten `erkennen`, `vervielfachen`, `pruefen` (so in der Datenbank nachgelesen, nur lesend; im Repo gibt es dafür keine eigene Datei). Aufgaben zum Dreisatz selbst gehören zu Teil 1 und fehlen hier absichtlich.
- `a1` rechnet in ℕ, wie die Lernkarte „Gibt es immer eine Lösung?“. Negative Zahlen kommen nicht vor.
- Regel-Kennungen, wo die Liste nicht genau passt: „Textaufgabe als Gleichung“ (a1) hängt an `id.algebra.term`; „irreführende Diagramme“ und „absolute Häufigkeit“ (d1) an `id.daten.kennzahl`; „relative Häufigkeit“ und „Kreisdiagramm“ an `id.daten.anteil`. Dessen Merksatz spricht von Wahrscheinlichkeit; gemeint ist hier derselbe Gedanke „Teil durch Ganzes“.
- Namen in Aufgaben (Tom, Nora, Mia, Paul …) sind erfunden.


## Berichtigungen nach der Inhaltsprüfung (Auftrag 20)

Stand 27.11.2026. Alle sechs Dateien sind neu erzeugt (`bauen.py` endet mit „OK“, 116 Aufgaben, 91 Rechnungen zweifach nachgerechnet, 194 Fehlbilder). Kennungen, Lernziele (`l`) und Teilfähigkeiten (`t`) sind unverändert; keine Aufgabe hinzugefügt oder gelöscht; die 30 `bedingung`-Aufgaben sind nicht angefasst.

**Muss vorher**

| Kennung | Befund | was geändert |
|---|---|---|
| `A1-04` | Die Antwort „noch einmal auf demselben Weg lösen“ ist nicht falsch, nur nicht gemeint. | Frage auf die Einsetzprobe zugeschnitten: „Bei der Einsetzprobe setzt du eine Zahl in die Gleichung ein und vergleichst. Wie machst du die Einsetzprobe für x = 9?“ Damit passt nur „9 für x einsetzen und beide Seiten vergleichen“. Tipp und Lösungsweg angepasst. |
| `G1-07` | Lücke hinter „0,“ (Weg B „= 0,② m“): Die App vergleicht die Lücke als ganze Zahl; „08“ zählte als 8, „80“ würde abgewiesen. | Weg B in Millimetern: „1 500 mm − 850 mm = ② mm“. Lücken jetzt ① = 65 (cm) und ② = 650 (mm), beide echte ganze Zahlen. Tipp („1 cm sind 10 mm“), Lösungsweg, Rechenanker (`150 - 85`, `1500 - 850`) und Fehlbilder angepasst. |
| `G8-01` | Lücke hinter „0,“ („Der Faktor ist 0,②“), gleiche Ursache wie bei `G1-07`. | „Der Faktor ist der Bruch ②/100.“ Lücken 65 und 65. Tipp und Lösungsweg nennen „Prozent heißt von Hundert“ und den Bruch 65/100. |
| `G8-04` | Zwei Lücken hinter „0,“ („Faktor war 0,①“, „: 0,①“). | „Der Faktor war der Bruch ①/10. Zurück zum alten Preis: 64 € · 10 : ① = ② €.“ Lücken 8 und 80. Tipp („80 % sind wie viele Zehntel?“) und Lösungsweg angepasst. |
| `G1-12` | Leergewicht nicht ausdrücklich genannt. | „Der leere Lieferwagen wiegt 2 800 kg; dazu kommen 900 kg Ladung.“ Lösungsweg und Fehlbild („nur den leeren Wagen gewogen“) angepasst. |
| `G2T2-03` | „gleiche Brötchen“ garantiert keine Proportionalität (Mengenrabatt). | Voraussetzung im Text: „Jedes Brötchen kostet gleich viel, es gibt keinen Mengenrabatt und keine Grundgebühr.“ Antwort heißt „Anzahl der Brötchen → Preis“. Tipp und Lösungsweg nennen die Voraussetzung. |

**Kann so – je Punkt entschieden**

| Kennung | Befund | was geändert (oder „bleibt, weil …“) |
|---|---|---|
| `A1-12` | Stufe 3 zu hoch: ein Schritt (Probe rückwärts). | Stufe 3 → 2, Typ `parameter` → `umkehr`. Text unverändert. |
| `G1-04` | Tipp „zwei Stellen hinter dem Komma“ klingt nach fester Regel. | Tipp als Stellenwert-Beziehung: „1 cm ist 0,01 m. Wie viele Hundertstel Meter sind 7 cm?“ |
| `G1-08` | dasselbe („drei Stellen“). | Tipp: „1 g ist 0,001 kg. Wie viele Tausendstel Kilogramm sind 40 g?“ |
| `D1-12` | „wirkt größer“ braucht gleiche Zeichenfläche. | Direkt nach dem Höhenverhältnis gefragt: „Du vergleichst in jedem Diagramm die Höhe der zweiten Säule mit der Höhe der ersten.“ Die Antworten sagen „3-mal so hoch wie die erste“ statt „wirkt größer“. Richtige Antwort bleibt an Stelle 4; Lösungsweg nennt A: etwa 1,08-mal. |
| `G8-14` | 1,1 wurde über Wurzelziehen gesucht. | Tipp: Faktoren ausprobieren (1,05; 1,1; 1,2). Lösungsweg zeigt das Probieren (1,05 · 1,05 = 1,1025 zu klein; 1,2 · 1,2 = 1,44 zu groß; 1,1 · 1,1 = 1,21). Der Text nennt den Faktor jetzt „q“. Lösung 10 % bleibt. |
| `F1-07` | Achsenzahlen liegen auf dem Graphen (die Gerade läuft durch die Beschriftungen links der y-Achse). | Zeichnung mit `schritt_y: 3`: Auf der y-Achse stehen nur −3 und 3. Gefragt ist y = 3, das ist beschriftet. **In der App nicht angesehen.** |
| `F1-15` | Die Achsenzahlen ±3 liegen genau auf dem Kreis. | Zeichnung mit `schritt_x: 2` und `schritt_y: 2`: Beschriftet sind ±2 und ±4, der Kreis (Radius 3) läuft zwischen den Zahlen durch. Antwort nennt weiter die Punkte (0 | 3) und (0 | −3). **In der App nicht angesehen.** |
| `D1-02`, `-03`, `-04`, `-05`, `-06`, `-10`, `-13`, `-14` | Prozent, relative Häufigkeit und Kreisdiagramm sind am bayerischen Gymnasium Stoff der 6. Klasse. | **Vorgriff auf Klasse 6.** Der Flug erklärt das selbst. Die Aufgaben bleiben, sind aber kein Mindeststand Klasse 5. Der Zähler in der Dateiübersicht oben („für Kind 1“) bleibt; maßgeblich ist diese Kennzeichnung. Die Aufgaben selbst sind nicht geändert. |

Zusatz zur Zeichnungsprüfung in `bauen.py`: Eine Koordinaten-Zeichnung darf jetzt auch `schritt_x`, `schritt_y` enthalten (sonst wie bisher nur Art `linear`, `poly`, Kreise).
Folge für Abschnitt 4 („Brüche“): Zwei Texte kommen dazu, `G8-01` („②/100“) und `G8-04` („①/10“). Beide stehen in der erkannten Form Zahl/Zahl; das Lückenzeichen steht vor dem Strich. **Wie die App „②/100“ mit Lückenzeichen darstellt, ist nicht gesehen.** Das Programm meldet jetzt 8 Texte mit Bruchstrich, keiner zweideutig.

**Muster-Suche in dieser Runde (86 Aufgaben in `zahl`, `auswahl`, `luecken`):** Weitere Treffer außer den genannten:
(1) Unbeabsichtigte Lösung 0: keine. `A1-06`, `A1-12`, `G1-06` u. a. haben eine einzige Lösung.
(2) Falsche Auswahl-Antworten einzeln gegengelesen. Bei `A1-05` („14 ist nicht durch 6 teilbar“) bleibt es, weil als Begründung nachweislich falsch (6 · x + 2 = 14 hat die Lösung 2, obwohl 14 nicht durch 6 teilbar ist, steht im Fehlbild). `G1-12` Antwort „Ja, 2 800 kg sind weniger als 3,5 t“ ist als Urteil falsch (die Ladung fehlt).
(3) Komma an einer Lücke: nur `G1-07`, `G8-01`, `G8-04` (siehe oben). Satzkommas wie in `G2T2-02` („①, ②, ③“) stehen mit Leerzeichen und sind erlaubt. `G1-14` („□:□ Uhr“) bleibt: Doppelpunkt, und jede Lücke ist eine ganze Zahl.
(4) Modellvoraussetzung: `G2T2-03` (siehe oben). `G2T2-09` (Taxi) nennt den Grundpreis, `F1-14` und `G2T2-13` sagen „gleichmäßig“.

**Neue automatische Prüfung in `bauen.py`:** Das Programm bricht ab, wenn im Fragetext oder in der Schablone einer Lückenaufgabe ein Komma ohne Leerzeichen an einem Lückenzeichen (① … ⑨, □) steht, etwa „0,②“ oder „①,②“. Satzkommas mit Leerzeichen („①, dann …“) sind erlaubt. Zusätzlich muss jede Lücke eine ganze Zahl sein. Die alten Fassungen von `G1-07`, `G8-01` und `G8-04` würden damit abbrechen (nachgestellt mit der Regel, nicht mit dem Programm selbst).
