# Ergänzung zum Regel-Universum: fehlende Einzelregeln (Entwurf)

Stand 27.11.2026. Nur Vorschlag und Inhalte; geändert wurden weder `daten/regeln-universum.json` noch bestehende Textdateien noch App-Code. Prüfen: `python3 -I inhalte/mathe-profi/regeln-uebersicht/ergaenzung/pruefen.py` (endet mit „OK“).

**70 Regeln** (62 neu, 8 Ausarbeitung bestehender Regeln), **25 Verweise** (Lücken, die schon unter anderem Namen im Universum stehen). Daten: `einzelregeln-neu.json`.

## So ist es gemeint
- **neu**: Die Regel fehlt im Universum. **Ausarbeitung**: Eine bestehende Regel (Spalte „ergänzt“) nennt den Stoff nur als Name oder Halbsatz; der neue Eintrag trägt Rechenweg, Beispiel und Grenze. Entscheidung, ob die bestehende Regel stattdessen selbst ausgearbeitet wird (dann derselbe Text), liegt beim Projektleiter.
- **Kennungen** `N-<Gebiet><nn>` sind vorläufig (Z Zahlen, A Algebra, V Geld und Verhältnisse, G Geometrie, F Fläche und Raum, U Funktionen, D Daten und Zufall) und kollidieren mit keiner bestehenden Kennung.
- Jede Regel hat `gehoert_zu` (Gebiet und Idee, begründet) und `lernkarten` (Thema und Lernkarte, die auf die Regel verweisen sollen). Klasse `gym` und `rs` stammen aus dem Lernkarten-Thema.
- Verweise sind **kein** neuer Eintrag: nur Stichwörter und Verknüpfung der Lernkarten mit der bestehenden Regel (Abschnitt „Nur Verweise“).

## Neue und ausgearbeitete Regeln nach Klasse (Gymnasium Bayern)

### Klasse 5 (30 Regeln)

| Kennung | Name | Gebiet, Idee | Art | Lernkarten |
|---|---|---|---|---|
| `N-Z01` | Große Zahlen lesen und schreiben | Zahlen, I-zahlen-2 | neu | zahlen.natuerlich: zahlwort_zu_ziffern, ziffern_zu_zahlwort |
| `N-Z02` | Römische Zahlen schreiben und lesen | Zahlen, I-zahlen-2 | Ausarbeitung von Z3 | zahlen.natuerlich: roemisch_schreiben, roemisch_system |
| `N-Z03` | Zweiersystem (Dualzahlen) | Zahlen, I-zahlen-2 | Ausarbeitung von Z3 | zahlen.natuerlich: dualsystem |
| `N-Z04` | Zahlenstrahl ablesen | Zahlen, I-zahlen-1 | neu | zahlen.natuerlich: strahl_ablesen, strahl_eintragen |
| `N-Z05` | Nachfolger und „größte Zahl“ | Zahlen, I-zahlen-1 | neu | zahlen.natuerlich: unendlich |
| `N-Z06` | Teilbarkeit durch 4, 6, 8 und 25 | Zahlen, I-zahlen-3 | Ausarbeitung von Z7 | keine im Bestand |
| `N-Z07` | Schriftlich addieren | Zahlen, I-zahlen-2 | neu | zahlen.ganz: schriftlich_plus_minus |
| `N-Z08` | Schriftlich subtrahieren | Zahlen, I-zahlen-2 | neu | zahlen.ganz: schriftlich_plus_minus |
| `N-Z09` | Schriftlich multiplizieren | Zahlen, I-zahlen-2 | neu | zahlen.rechengesetze: schriftlich |
| `N-Z10` | Schriftlich dividieren mit Rest | Zahlen, I-zahlen-2 | neu | zahlen.rechengesetze: schriftlich |
| `N-Z11` | Schriftlich dividieren durch zweistellige Zahlen | Zahlen, I-zahlen-2 | neu | zahlen.rechengesetze: schriftlich_geteilt |
| `N-Z12` | Im Kopf rechnen: Zahl zerlegen | Zahlen, I-zahlen-2 | neu | zahlen.rechengesetze: kopfrechnen, vorteil, verteilen |
| `N-V01` | Größen mit Komma schreiben | Geld und Verhältnisse, I-geld-1 | neu | groessen.einheiten: kommaschreibweise |
| `N-G01` | Winkel nach der Größe benennen | Geometrie, I-geo-1 | neu | geometrie.grundbegriffe: winkelarten |
| `N-G02` | Winkel addieren und ergänzen | Geometrie, I-geo-1 | neu | geometrie.winkel: ergaenzen, um_punkt |
| `N-G03` | Winkel an der Uhr | Geometrie, I-geo-1 | neu | geometrie.winkel: uhr |
| `N-G04` | Drehung und Windrose | Geometrie, I-geo-1 | neu | geometrie.winkel: drehungen |
| `N-G05` | Strecke im Koordinatensystem messen | Geometrie, I-geo-2 | neu | geometrie.grundbegriffe: strecken |
| `N-G06` | Sekante, Tangente, Passante | Geometrie, I-geo-2 | Ausarbeitung von G13 | geometrie.grundbegriffe: kreis_lage |
| `N-G07` | Zwei Kreise: Schnittpunkte zählen | Geometrie, I-geo-2 | neu | geometrie.ortslinien: zwei_kreise, geometrie.grundbegriffe: kreis_lage |
| `N-G08` | Streifen: höchstens so weit entfernt | Geometrie, I-geo-2 | neu | geometrie.ortslinien: parallelen, kreislinie, verknuepfen |
| `N-G09` | Viereck erkennen | Geometrie, I-geo-3 | neu | geometrie.grundbegriffe: vierecke |
| `N-F01` | Ar und Hektar | Fläche und Raum, I-fur-1 | neu | messen.flaechen: einheiten |
| `N-F02` | Flächen mit Komma schreiben | Fläche und Raum, I-fur-1 | neu | messen.flaechen: kommaschreibweise |
| `N-F03` | Quader: Ecken, Kanten, Flächen und Kantenlänge | Fläche und Raum, I-fur-4 | neu | messen.koerper_berechnung: quader |
| `N-F04` | Oberfläche zusammengesetzter Körper | Fläche und Raum, I-fur-4 | neu | messen.koerper_berechnung: zusammengesetzt |
| `N-D01` | Alle Möglichkeiten systematisch aufschreiben | Daten und Zufall, I-daten-3 | neu | stochastik.kombinatorik: systematisch |
| `N-D02` | Baumdiagramm zum Zählen (Zählregel) | Daten und Zufall, I-daten-4 | neu | stochastik.kombinatorik: baumdiagramm |
| `N-D03` | Reihenfolgen ohne Wiederholung | Daten und Zufall, I-daten-3 | neu | stochastik.kombinatorik: reihenfolgen |
| `N-D04` | Wenn die Reihenfolge egal ist: Paare zählen | Daten und Zufall, I-daten-3 | neu | stochastik.kombinatorik: grenzen |

### Klasse 6 (13 Regeln)

| Kennung | Name | Gebiet, Idee | Art | Lernkarten |
|---|---|---|---|---|
| `N-Z13` | Gemischte Zahl in unechten Bruch umwandeln | Zahlen, I-zahlen-4 | neu | bruch.brueche: gemischte_zahlen |
| `N-Z14` | Unechten Bruch in gemischte Zahl umwandeln | Zahlen, I-zahlen-4 | neu | bruch.brueche: gemischte_zahlen |
| `N-Z15` | Bruchteil einer Größe berechnen | Zahlen, I-zahlen-4 | neu | bruch.brueche: bruchteil_von |
| `N-Z16` | Das Ganze aus dem Teil berechnen | Zahlen, I-zahlen-4 | neu | bruch.brueche: ganzes_bestimmen |
| `N-Z17` | Dezimalzahlen vergleichen | Zahlen, I-zahlen-1 | neu | bruch.dezimal: vergleichen_ordnen |
| `N-Z18` | Wissenschaftliche Schreibweise | Zahlen, I-zahlen-2 | neu | zahlen.potenzen_zehner: gross_wissenschaftlich, klein_wissenschaftlich |
| `N-Z19` | Vorsilben: Kilo, Mega, Milli, Mikro … | Zahlen, I-zahlen-2 | neu | zahlen.potenzen_zehner: vorsilben_gross, vorsilben_klein |
| `N-F05` | Höhe aus der Fläche berechnen | Fläche und Raum, I-fur-2 | neu | messen.flaechen_vielecke: rueckwaerts |
| `N-F06` | Höhe aus dem Volumen berechnen | Fläche und Raum, I-fur-1 | neu | messen.volumen: rueckwaerts |
| `N-D05` | Säulendiagramm zeichnen | Daten und Zufall, I-daten-1 | neu | daten.darstellen: saeulendiagramm |
| `N-D06` | Kreisdiagramm: Winkel berechnen | Daten und Zufall, I-daten-1 | neu | daten.darstellen: kreisdiagramm, relative_haeufigkeit |
| `N-D07` | Mittelwert aus einer Häufigkeitstabelle | Daten und Zufall, I-daten-1 | neu | daten.kennwerte: mittel_tabelle |
| `N-D08` | Mittelwert rückwärts: fehlender Wert | Daten und Zufall, I-daten-1 | neu | daten.kennwerte: mittel_rueckwaerts |

### Klasse 7 (6 Regeln)

| Kennung | Name | Gebiet, Idee | Art | Lernkarten |
|---|---|---|---|---|
| `N-A01` | Wortterme in Terme übersetzen | Algebra, I-algebra-1 | neu | terme.aufstellen: uebersetzen |
| `N-A02` | Figurenfolge als Term | Algebra, I-algebra-1 | neu | terme.aufstellen: muster |
| `N-V02` | Grundwert zurückrechnen (nach Rabatt oder Aufschlag) | Geld und Verhältnisse, I-geld-3 | neu | bruch.prozent_grundwert: zurueck |
| `N-G10` | Figur verschieben (Koordinaten) | Geometrie, I-geo-3 | neu | abbildungen.kongruenz: verschiebung, vektor_koordinaten |
| `N-G11` | Punkt an einem Punkt spiegeln | Geometrie, I-geo-3 | neu | abbildungen.kongruenz: punktspiegelung |
| `N-G12` | Drehung um den Ursprung (90° und 180°) | Geometrie, I-geo-3 | neu | abbildungen.kongruenz: drehung, vektor_drehen |

### Klasse 8 (16 Regeln)

| Kennung | Name | Gebiet, Idee | Art | Lernkarten |
|---|---|---|---|---|
| `N-A03` | Bruchgleichung über Kreuz lösen | Algebra, I-algebra-2 | Ausarbeitung von A12 | gleichungen.bruch: ueber_kreuz, definitionsmenge, scheinloesung, verhaeltnis |
| `N-A04` | Gleichungssystem: Wie viele Lösungen? | Algebra, I-algebra-3 | neu | gleichungen.lgs2: loesbarkeit |
| `N-A05` | Intervalle mit unendlich | Algebra, I-algebra-3 | neu | zahlen.intervalle: lesen, schreiben, beurteilen |
| `N-F07` | Prisma: Ecken, Kanten, Flächen | Fläche und Raum, I-fur-4 | neu | messen.koerper_darstellung: prisma |
| `N-F08` | Schrägbild zeichnen | Fläche und Raum, I-fur-4 | neu | messen.koerper_darstellung: schraegbild |
| `N-F09` | Ansichten von Körpern | Fläche und Raum, I-fur-4 | neu | messen.koerper_darstellung: ansichten |
| `N-F10` | Kreisring | Fläche und Raum, I-fur-2 | neu | messen.kreisberechnung: zusammengesetzt |
| `N-F11` | Kreisabschnitt | Fläche und Raum, I-fur-2 | neu | messen.kreisberechnung: zusammengesetzt |
| `N-U01` | Definitionsmenge und Wertemenge | Funktionen, I-funktionen-1 | neu | funktionen.grundbegriffe: mengen |
| `N-U02` | Wertetabelle ausfüllen | Funktionen, I-funktionen-1 | neu | funktionen.grundbegriffe: wertetabelle |
| `N-U03` | Gerade zeichnen | Funktionen, I-funktionen-2 | neu | funktionen.linear: graph_ablesen |
| `N-U04` | Steigung aus zwei Punkten | Funktionen, I-funktionen-2 | neu | funktionen.linear: zwei_punkte |
| `N-U05` | Geradengleichung aufstellen | Funktionen, I-funktionen-2 | neu | funktionen.linear: aufstellen |
| `N-U06` | Hyperbel verschieben | Funktionen, I-funktionen-3 | neu | funktionen.gebrochen: parameter, definitionsmenge |
| `N-U07` | Asymptoten der Hyperbel | Funktionen, I-funktionen-3 | neu | funktionen.gebrochen: asymptoten, achsenpunkte, beurteilen |
| `N-D09` | Vierfeldertafel ausfüllen | Daten und Zufall, I-daten-4 | Ausarbeitung von D17 | stochastik.grundbegriffe: darstellen |

### Klasse 9 (3 Regeln)

| Kennung | Name | Gebiet, Idee | Art | Lernkarten |
|---|---|---|---|---|
| `N-G13` | Strahlensatz anwenden (Verhältnisse aufstellen) | Geometrie, I-geo-4 | Ausarbeitung von G21 | abbildungen.aehnlichkeit: strahlensatz1, strahlensatz2, anwendung |
| `N-G14` | Zweite Lösung bei sin, cos und tan | Geometrie, I-geo-5 | Ausarbeitung von G30 | gleichungen.trig: sinus, kosinus, tangens, anzahl |
| `N-G15` | Flächeninhalt eines Dreiecks mit dem Sinus | Geometrie, I-geo-5 | neu | trigo.allgemein: flaeche |

### Klasse 10 (2 Regeln)

| Kennung | Name | Gebiet, Idee | Art | Lernkarten |
|---|---|---|---|---|
| `N-D10` | Ziehen ohne Zurücklegen | Daten und Zufall, I-daten-4 | neu | stochastik.mehrstufig: ohne_zuruecklegen |
| `N-D11` | Erwartete Trefferzahl n · p | Daten und Zufall, I-daten-2 | neu | stochastik.mehrstufig: simulation |

## Nur Verweise (steht schon im Universum, nur unter anderem Namen oder ohne Verknüpfung)

Abgleich mit dem Bestand: `verweise-abgleich.md`. Kein neuer Text; es genügt, die Suchwörter (Spalte „Stichwörter“) auf das Ziel zu legen und die Lernkarten mit dem Ziel zu verknüpfen. Wo die bestehende Regel selbst etwas ergänzt haben möchte, steht ein Vorschlag.

| Kennung | Gesuchter Stoff | Steht in | Stichwörter | Lernkarten | Vorschlag |
|---|---|---|---|---|---|
| `V-01` | Überschlag (Kl. 5) | Arbeitsweise Überschlag | Überschlag, überschlagen, schätzen, grob rechnen, Näherung | zahlen.rechengesetze (1) |  |
| `V-05` | (−2)² und −2² (Kl. 5) | Z16 | Minus Quadrat, Klammer Potenz, negative Basis | zahlen.potenzen_basis, terme.potenzgesetze (2) | In Z16 zusätzlich (−2)² = 4 und −2² = −4 nennen (nachgerechnet: (−2) · (−2) = 4; erst 2² = 4, dann das Minus: −4). |
| `V-12` | Gleichungen mit Umkehraufgaben lösen (Kl. 5) | R12 | Umkehraufgabe, Umkehrrechnung, rückwärts rechnen | zahlen.ganz, zahlen.rechengesetze (2) |  |
| `V-13` | Zeit rechnen (2 h 30 min) (Kl. 5) | V1 | Zeitspanne, Uhrzeit, Stunden Minuten, Dauer berechnen | groessen.einheiten (1) |  |
| `V-14` | Einheitentafel (dm, t, ct, s, ha, Treppen) (Kl. 5) | T-einheiten | cm, kg, ml, ha, Zentimeter | groessen.einheiten, messen.flaechen, messen.volumen (5) |  |
| `V-16` | Quadratzahlen bis 20² (Kl. 5) | Z15 | Quadratzahlen, Quadratzahl, 14 hoch 2 | zahlen.potenzen_basis (1) |  |
| `V-23` | Fläche und Umfang verstehen (Kl. 5) | F3 | Umfang, Flächeninhalt, Fläche Umfang verwechseln | messen.flaechen (1) | F3 um das Beispiel zweier Rechtecke mit gleichem Umfang ergänzen (nachgerechnet: 2 · (4 + 2) = 12, 2 · (3 + 3) = 12; 4 · 2 = 8, 3 · 3 = 9). |
| `V-02` | Welcher Anteil? (Teil durch Ganzes) (Kl. 6) | Z10 | Anteil, welcher Anteil, Teil vom Ganzen, Anteil bestimmen | bruch.brueche (1) | Z10 um Beispiel 12 von 30 = 2/5 und den Fehler 30/12 ergänzen (nachgerechnet: 12 : 6 = 2, 30 : 6 = 5). |
| `V-03` | Rabatt und Aufschlag (Kl. 6) | V9 | Rabatt, Aufschlag, Preisnachlass, Skonto, Mehrwertsteuer | bruch.prozent, bruch.prozent_grundwert (4) |  |
| `V-15` | Merkwerte Bruch, Dezimalzahl, Prozent (Kl. 6) | Z12 | Merkwerte, Bruch Dezimalzahl Prozent, ein Viertel, drei Viertel | bruch.dezimal (1) |  |
| `V-20` | Dezimalzahlen runden, Stellen nach dem Komma (Kl. 6) | Z2 | Dezimalzahl runden, Zehntel, Hundertstel | bruch.dezimal (2) |  |
| `V-24` | Brüche am Zahlenstrahl (Kl. 6) | Z4 | Zahlenstrahl Brüche | bruch.brueche (1) |  |
| `V-04` | Prozente nicht addieren, mehrere Änderungen (Kl. 7) | V9 | mehrere Änderungen, Prozente addieren, erst plus dann minus | bruch.prozent_grundwert (2) |  |
| `V-21` | Planfigur und Konstruktionsbeschreibung (Kl. 7) | Arbeitsweise Skizze | Planfigur, Skizze, Konstruktionsbeschreibung | geometrie.konstruktion (1) |  |
| `V-22` | Gleichungen mit Klammern, keine oder unendlich viele Lösungen (eine Gleichung) (Kl. 7) | A9 | Klammern lösen, keine Lösung, unendlich viele Lösungen | gleichungen.linear (2) |  |
| `V-06` | Kürzen nur aus Produkten, nie aus Summen (Kl. 8) | A6 | aus Summen kürzen, kürzen, Bruchterm kürzen | terme.bruchterme (2) |  |
| `V-07` | Mindestens einmal (Gegenereignis) (Kl. 8) | D14 | mindestens einmal, mindestens, keinmal, Gegenereignis | stochastik.mehrstufig, stochastik.grundbegriffe (2) |  |
| `V-09` | Zylindermantel (Kl. 8) | F15 | Mantel, Mantelfläche, Zylinder Netz, Etikett | messen.koerper_darstellung (1) |  |
| `V-10` | Formeln umstellen (Kl. 8) | A13 | umstellen, Formel umstellen, nach h auflösen, Formel auflösen | gleichungen.formeln (5) |  |
| `V-11` | Funktionswert, Punktprobe, Nullstelle, Ablesen (Kl. 8) | U2 | Funktionswert, f(x) berechnen, Punkt auf dem Graphen, Nullstelle, am Graphen ablesen | funktionen.grundbegriffe (5) |  |
| `V-25` | Lineare Gleichungssysteme: Verfahren (Kl. 8) | A14 | LGS, Einsetzungsverfahren, Gleichsetzungsverfahren, Additionsverfahren, Gleichungssystem | gleichungen.lgs2 (4) |  |
| `V-17` | Schwerpunkt des Dreiecks (Kl. 9) | G23 | Schwerpunkt, Seitenhalbierende | abbildungen.aehnlichkeit (1) |  |
| `V-18` | Verknüpfte Ereignisse (Schnitt, Vereinigung, Additionssatz, Venn) (Kl. 9) | D16 | Schnitt, Vereinigung, Venn, Additionssatz | stochastik.verknuepft (11) |  |
| `V-19` | Wurzelfunktion, Umkehrfunktion, x hoch minus n (Kl. 9) | U6 | Umkehrfunktion, Wurzelfunktion, Potenzfunktion | funktionen.potenz (10) |  |
| `V-08` | π schätzen (Zufallspunkte) (Kl. 10) | D20 | π schätzen, Monte-Carlo, Zufallspunkte | stochastik.mehrstufig (1) |  |

Begründungen je Verweis stehen in `einzelregeln-neu.json` (Feld `begruendung`).

## Zählung
- Lernkarten, die durch neue oder ausgearbeitete Regeln eine Zielregel bekommen: **91**; durch Verweise: **69** (zusammen **159** verschiedene).
- Von den **126** Lernkarten, die `regelbezug-lernkarten.json` als „offen“ führt, bekommen **51** eine Zielregel (neu oder Verweis).

## Nicht als Einzelregel (eigene Aufgaben, nicht hier)
- **Tafeln** des Berichts (Abschnitt A, D): Einheiten (liegt in `einheiten/`), Formelübersicht, Haus der Vierecke mit Eigenschaften (hier nur das Erkennen, `N-G09`), Quadrat- und Kubikzahlen, Primzahlen bis 100, Stellenwerttafel, Merkwerte Bruch–Dezimal–Prozent, Glossar und Zeichen.
- **Suche** (Zwei-Zeichen-Wörter, Rangfolge): Bericht D, Rang 8. Die Stichwörter dieser Datei sind Vorschläge dafür.
- Nicht abgedeckt, weil nicht in Abschnitt B: Dichte, Geschwindigkeit, Skonto, Promille, Quadranten, Kubikzahlen.

## Zweifelsfälle
1. Trapez ist in `N-G09` bewusst nicht enthalten: Ob „genau ein Paar“ oder „mindestens ein Paar“ paralleler Seiten gilt, ist im Bestand nicht festgelegt (G7 nennt das Trapez nur beim Namen, F7 spricht von „den beiden parallelen Seiten“). Erst entscheiden, dann ergänzen.
2. Klassen weichen im Bestand ab: V9 (Gymnasium Klasse 7) und die Lernkarte „rabatt_aufschlag“ (Klasse 6); D17 (Klasse 9) und die Lernkarte „darstellen“ (Klasse 8); V7 steht mit Klasse 5, Steigung kommt erst in Klasse 8. Die neuen Regeln folgen der Lernkarte.
3. `N-A03` (über Kreuz) und `N-Z02`/`N-Z03` (Z3), `N-G06` (G13), `N-G13` (G21), `N-G14` (G30), `N-D09` (D17), `N-Z06` (Z7) sind Ausarbeitungen: Der Bestand nennt den Stoff schon in einem Halbsatz. Alternative: die bestehende Regel mit demselben Text ausarbeiten statt eine neue anzulegen.
4. Grundmenge in `N-U01`, `N-U06`, `N-U07`, `N-A03`: Sie steht in der Aufgabe (oft ℚ, ab Klasse 9 ℝ); die Lernkarte (Klasse 8) schreibt `D = ℚ \ {…}`. Die Wertemenge in `N-U07` hängt von D ab (ℚ \ {c} bei D = ℚ \ {−b}, ℝ \ {c} bei D = ℝ \ {−b}). Auflage aus Werkstatt 1133/1137.
5. `N-F08` Schrägbild: Winkel 45° und Verkürzungsfaktor ½ stehen so in der Lernkarte; gegen den LehrplanPLUS nicht geprüft, in der Regel ausdrücklich als übliche Vereinbarung gekennzeichnet, die in der Aufgabe abweichen kann.
6. `N-Z06` (Teilbarkeit 4, 6, 8, 25) steht in Bericht A, nicht B, und hat keine Lernkarte im Bestand (`zahlen.teilbarkeit` behandelt nur 2, 3, 5, 9, 10).
7. `N-Z12` (Im Kopf rechnen) trägt nur schwach zu einer Idee: gewählt ist „Bündeln in Zehnern“ (Zerlegen in Zehner und Einer); verwandt ist Rechenregel 6.
8. `N-Z02`: Auf Uhren steht oft IIII statt IV; die Regel nennt die übliche Schreibweise IV. `N-Z01`: „Billion“ ist im Deutschen 10¹², im Englischen „billion“ 10⁹ – steht so in der Regel.
9. `N-G14`: Rechner liefern für sin und tan bei negativem v negative Winkel; die Regel bringt x₁ zuerst in den Bereich 0° bis 360° („+ 360°“), bestimmt dann alle Lösungen dort und ordnet sie (Beispiel tan x = −1: −45° gibt 315° und 135°). Die Rechenproben prüfen die Winkelfunktionen nur auf sechs Stellen (Gleitkomma), alles andere exakt.
10. Kein Lehrplan-Abgleich: Alle Klassenangaben sind die der Lernkarten-Themen, nicht Fundstellen im Fachlehrplan.

