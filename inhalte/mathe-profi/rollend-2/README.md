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
- Jede Auswahl-Aufgabe hat eine Probe; jede falsche Antwort ist beschrieben (192 Fehlbilder, 69 davon mit Fehlbild-Kennung aus `kennungen.json`; wo ich nicht sicher war, steht keine).
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

Sechs Texte enthalten einen Bruchstrich: `D1-03` (12/18, 18/12, 12/30, 2/5) und `F1-B5` (12/(x − a), 12/(2 + 1)). Alle stehen in einer der erkannten Formen (Zahl/Zahl, Zahl/(Klammer)). Das Programm bricht ab, wenn eine Form wie 1/2x oder eine verschachtelte Klammer im Bruch vorkommt. [G]
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
