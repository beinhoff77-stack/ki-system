# Postfach pruefung-neu-2 (Fünfundzwanzigste Runde, unabhängige Prüfung)

Neueste Meldung oben. Dieser Chat hat keines der geprüften Themen geschrieben.

## 2026-11-20 – FERTIG: Prüfung neu, Chat 2

| Thema | gelesen | a | b | c | d | e | f | Urteil |
|---|---|---|---|---|---|---|---|---|
| zahlen.schranken | 180 | 0 | 18 | 0 | 0 | 10 | 1 | mit Korrekturen in Ordnung |
| daten.standardabweichung | 181 | 0 | 2 | 0 | 0 | 0 | 3 | mit Korrekturen in Ordnung |
| daten.normalverteilung | 178 | 0 | 1 | 0 | 0 | 0 | 0 | mit Korrekturen in Ordnung |
| daten.zweidimensional | 184 | 1 | 4 | 0 | 0 | 9 | 0 | mit Korrekturen in Ordnung |
| sonder.logik | 174 | 0 | 0 | 3 | 0 | 13 | 0 | mit Korrekturen in Ordnung |
| sonder.graphentheorie | 181 | 0 | 0 | 0 | 1 (Karte) | 0 | 0 | in Ordnung |
| sonder.optimierung | 183 | 0 | 0 | 0 | 0 | 1 | 0 | in Ordnung |

- Kein Thema „nicht freigabefähig“. Einzige fachlich falsche Lösung: daten.zweidimensional (Wirkweg als „dritte Größe“), ersetzt.
- Je Thema ein Commit auf `pruefung-neu-2`, Prüfskript jeweils OK. Kein Merge, keine Datenbank, kein App-Code, keine Kinderdaten.
- Nebenwirkung in 6 Themen: Feld `klasse` beim Neuerzeugen aus `themenliste.json` übernommen (die Dateien waren veraltet), siehe Einzelberichte.
- Offene Punkte für den Haupt-Chat: daten.zweidimensional war für MYP 3 gebaut, steht jetzt bei MYP 5 (Korrelationskoeffizient r fehlt dann vermutlich); Lehrplanbelege für alle sieben IB-Themen nur über Sekundärquellen, das IB-Originaldokument war nicht frei abrufbar.
- Nicht geprüft: Darstellung in der App (Bilder, Glocken, Graphen nur über ihre JSON-Daten geprüft).

## 2026-11-20 – sonder.optimierung (Lineare Optimierung)

**Urteil: in Ordnung** (eine Antwortoption geändert).

### Umfang (Fakt)
- Gelesen: 5 Lernkarten und alle 183 Aufgaben (123 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle 183 von Hand; zusätzlich per eigenem Skript für alle 70 Aufgaben mit zwei Bedingungen: echte Eckpunkte des Bereichs aus den Ungleichungen berechnet und mit den im Text genannten Ecken verglichen (alle gleich), Zulässigkeit jedes Punkts Q, „Welcher Punkt liegt im Bereich?“ (genau eine Option zulässig), „welche Bedingung verletzt“, Optimum und optimaler Plan (eindeutig, außer in den drei Aufgaben, die gerade nach einer ganzen optimalen Kante fragen), „Um wie viel ist der beste Plan besser?“. Eckenlisten der Optimum-Karte auf Konvexität geprüft. Ganzzahliges Knobel-Optimum (2 | 3) durch Durchprobieren aller Gitterpunkte bestätigt.
- Prüfskript nach der Änderung: OK, 0 Gruppen „gleich gebaut hintereinander“.

### Änderungen je Fehlerart (1 Aufgabe)
- **a)–d), f): 0.**
- **e) Antwortoption: 1.** bereich, Stufe 2 einkleidung (Kiosk): Die falsche Option „Nein, der Teig reicht nicht (38 > 40).“ enthielt eine falsche Rechnung als Begründung. Jetzt „Nein, der Teig reicht nicht.“

### Nebenwirkung (Fakt)
- Feld `klasse` aus der Themenliste übernommen: `{"ib_myp": 4}` → `{"ib_myp": 5}`. Die Datei vermerkt unter `offen` noch „Annahme MYP 4“; inhaltlich passt sie auch zu MYP 5.

### Nicht geändert, zur Kenntnis (Meinung)
- „Ja / Nein / Das lässt sich nicht entscheiden“ bei „Liegt Q im Bereich?“: Die dritte Option ist hier nie vertretbar (Einsetzen entscheidet immer). Belassen.
- „Minimum von K = x + 5y an diesen Ecken (ohne den Nullpunkt)“: inhaltlich richtig, aber ein Minimierungsproblem ohne Untergrenze wirkt künstlich. Belassen.

### Lehrplan
- Annahme: IB MYP Jahr 5 (Klasse 10), Extended. „Linear programming“ wird in Sekundärquellen als Extended-Inhalt genannt (revisiondojo.com/blog/what-topics-are-in-myp-extended-mathematics, abgerufen 20.11.2026); IB-Dokument nicht frei abrufbar. Vorausgesetzt werden lineare Gleichungssysteme (Themenliste: früher) – passt. Isogewinngeraden fehlen bewusst (unter `offen`).

## 2026-11-20 – sonder.graphentheorie (Graphentheorie)

**Urteil: in Ordnung** (eine Ergänzung in der Lernkarte, keine Aufgabe geändert).

### Umfang (Fakt)
- Gelesen: 5 Lernkarten und alle 181 Aufgaben (121 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle 181 von Hand, die Graph-Aufgaben zusätzlich mit eigenem Skript direkt aus den Kanten der Zeichnung: Grade (auch jede Gradliste im Lösungsweg), Kantenzahl, Gradsumme, ungerade Knoten, Zusammenhang, Euler-Einordnung, „welche zusätzliche Kante“ (genau eine Option richtig), alle kürzesten Wege per vollständiger Wegsuche (Länge, Eindeutigkeit des kürzesten Wegs, „zweitbester“ im Lösungsweg, Längen aller Auswahl-Wege, Sperrung, Pflichthalt, Erreichbarkeit), Kruskal (Gesamtkosten, Ersparnis, erste übersprungene Kante, teuerste Baumkante, neue Leitung). 0 Abweichungen. Gradlisten-Aufgaben („Kann es einen Graphen … geben?“) mit Havel-Hakimi geprüft.
- Prüfskript: OK, 0 Gruppen „gleich gebaut hintereinander“.

### Änderungen je Fehlerart
- **a)–c), e), f): 0.**
- **d) Lernkarte: 1.** euler, angezeigte Regel „Zähle die ungeraden Knoten: 0 heißt Eulerkreis, 2 heißt Eulerweg, sonst keiner.“ – ohne die Bedingung „zusammenhängend“ ist die Regel falsch (zwei getrennte Dreiecke: alle Grade gerade, kein Eulerkreis). Jetzt: „Ist der Graph zusammenhängend, zähle die ungeraden Knoten: …“. Alle gezeichneten Graphen der Aufgaben sind zusammenhängend (geprüft).

### Nicht geändert, zur Kenntnis
- Fakt: Zwei Kruskal-Aufgaben haben gleiche Gewichte (neue Leitung 3 neben CE 3; 4 neben CG 4); das Ergebnis hängt davon nicht ab.
- Meinung: „mindestens 3 Kanten hinzufügen“ bei 6 ungeraden Knoten setzt stillschweigend voraus, dass Mehrfachkanten erlaubt sind (falls zwei ungerade Knoten schon verbunden sind). Für das Niveau vertretbar.
- Fakt: Feld `klasse` unverändert `{"ib_myp": 4}` (stimmte schon mit der Themenliste überein).

### Lehrplan
- Annahme: IB MYP Jahr 4 (Klasse 9). Graphentheorie wird in Sekundärquellen als Extended-Kapitel geführt („Graph Theory and Vectors“: Netzwerktypen, Wege und Kreise – revisiondojo.com/myp/myp-extended-mathematics/notes, abgerufen 20.11.2026; IB-Dokument nicht frei abrufbar). Hamiltonkreise fehlen bewusst (unter `offen`); ob sie im Schul-Curriculum vorkommen, ist **nicht belegbar**.

## 2026-11-20 – sonder.logik (Aussagenlogik)

**Urteil: mit Korrekturen in Ordnung.**

### Umfang (Fakt)
- Gelesen: 5 Lernkarten und alle 174 Aufgaben (114 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle 174 von Hand – jeder Wahrheitswert (Teilbarkeit, Quadrate, Primzahlen), jede Wahrheitstafel-Spalte, alle Zählaufgaben (1 bis N, Ein-/Ausschluss), alle Ritter-und-Lügner-Rätsel durch alle vier Fälle, alle Kartenaufgaben (Wason), alle Gegenbeispiel-Optionen (genau eine widerlegt, „erfüllt beides“ stimmt jeweils).
- Prüfskript nach der Änderung: OK, 0 Gruppen „gleich gebaut hintereinander“.

### Änderungen je Fehlerart (16 Aufgaben)
- **a) falsche Lösung: 0.**
- **b) mehrdeutig: 0.**
- **c) Stoff einer späteren Lernkarte: 3.** Die Implikation ⇒ wird erst in der letzten Lernkarte „folgerung“ eingeführt, kam aber vorher schon vor: verknuepfen, Stufe 3 („… und q ⇒ p ist falsch“), tafel, Stufe 3 („Haben p ⇒ q und q ⇒ p … gleichwertig?“, „Welcher Ausdruck ist in allen Zeilen wahr? … (p ∧ q) ⇒ p“). Im Generator für diese Lernkarten durch gleichwertige bzw. gleich schwere Ausdrücke ohne ⇒ ersetzt (q ⇒ p → p ∨ ¬q; Paare jetzt z. B. ¬(p ∧ ¬q) / ¬p ∨ q; Tautologie ¬(p ∧ ¬p)). Lösungen jeweils neu nachgerechnet. Fakt: In den übrigen 171 Aufgaben steht ⇒ außerhalb von „folgerung“ nur noch als Folgepfeil im Lösungsweg einer Knobel-Karte.
- **d) Lernkarten: 0.**
- **e) Lösungsweg: 13.**
  - 11× „Welcher Satz ist KEINE Aussage?“: Der Lösungsweg nannte für jeden Satz pauschal „eine Frage, ein Befehl, eine Meinung oder enthält eine unbestimmte Variable“. Jetzt der passende Grund (z. B. „„n ist eine gerade Zahl.“ enthält die unbestimmte Variable n“).
  - 2× doppelte Verneinung: Weg „… (bzw. aus „höchstens“ ein „mindestens“)“ legte bei „Es ist falsch, dass höchstens 3 Plätze frei sind“ die falsche Option „mindestens 3“ nahe. Jetzt je Satz ein eigener Weg („Höchstens 3 heißt 0, 1, 2 oder 3 … das Gegenteil: 4 oder mehr“).
- **f) Stufe/Typ: 0.**

### Nebenwirkung (Fakt)
- Feld `klasse` aus der Themenliste übernommen: `{"zusatz": 10}` → `{"ib_myp": 4}`.

### Lehrplan
- Annahme: IB MYP Jahr 4 (Klasse 9). Aussagenlogik ist laut Themenliste IB-Stoff; im frei zugänglichen Material (Sekundärquellen, siehe oben) **nicht belegbar** als fester MYP-Inhalt – die Datei vermerkt „Verlagsinhalt“. Für die gewählte Tiefe fehlt nichts Wesentliches; Äquivalenz ⇔ und ausschließendes Oder sind bewusst nur am Rand (unter `offen`).

## 2026-11-20 – daten.zweidimensional (Zweidimensionale Daten)

**Urteil: mit Korrekturen in Ordnung.**

### Umfang (Fakt)
- Gelesen: 5 Lernkarten und alle 184 Aufgaben (124 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle Zahl- und Lückenaufgaben von Hand (Ablesen gegen die Punktdaten, Zählen in Vierteln, Mittelwerte/Prozente, Geradengleichungen, Ungleichungen). Per eigenem Skript zusätzlich: Korrelationskoeffizient r jeder Punktwolke gegen die Antwort „positiv/negativ/kein, stark/schwach“ (alle passend; schwächste „positiv“-Wolke r = 0,55, „kein“ immer |r| ≤ 0,18), jeder Ausreißer gegen eine Ausgleichsgerade ohne ihn (gesuchter Punkt hat immer den deutlich größten Abstand), Abstand des höchsten Punkts zum zweithöchsten.
- Prüfskript nach der Änderung: OK, 0 Gruppen „gleich gebaut hintereinander“.

### Änderungen je Fehlerart (14 Aufgaben)
- **a) fachlich falsche Lösung: 1.** kausal, Sicherung: „Kinder, die mehr Zeit im Freien verbringen, sind seltener kurzsichtig. Welche dritte Größe erklärt diesen Zusammenhang?“ – richtig sollte sein „das Tageslicht draußen und weniger Nahsehen“. Das ist keine dritte Größe, die beide Merkmale beeinflusst, sondern der Wirkweg (Zeit draußen → Tageslicht → seltener kurzsichtig); der Lösungsweg „beeinflusst beide beobachteten Größen“ war falsch. Ersetzt durch: „Städte mit mehr Kirchen haben mehr Gaststätten.“ – Lösung „die Einwohnerzahl der Stadt“.
- **b) Mehrdeutigkeit/Sprache: 4.**
  - 2× „Welchen x-Wert hat der Punkt mit dem größten y-Wert?“: höchster und zweithöchster Punkt lagen nur 4 % der Achsenhöhe auseinander (80 gegen 78; 295 gegen 293) – im Bild kaum zu unterscheiden. Generator hebt den höchsten Punkt jetzt auf mindestens 10 % Abstand (83 bzw. 298); Lösung (x-Wert) unverändert.
  - „das 1 Jahre alt ist“ → „1 Jahr“; „Alter des Geräts in Jahre“ → „in Jahren“.
- **c) späterer Stoff: 0** (lineare Funktionen, Median, Prozent – alles früher).
- **d) Lernkarten: 0.**
- **e) Lösungsweg: 9.** „x > 9,38“ war für 8x > 75 falsch gerundet (x = 9,376 erfüllt die Ungleichung, ist aber < 9,38) → exakt „x > 9,375“ (nicht abbrechende Grenzen jetzt als Bruch mit ≈). „Die Steigung -4“ mit Bindestrich → „−4“ (3×). „Davon liegen 1 …“ → „liegt“. Lösungswege der Dritte-Größe-Aufgaben begannen klein und mit falschem Numerus („ländliche Gegenden … beeinflusst“) → „Die dritte Größe ist: … Sie beeinflusst …“ (5×, ohne die ersetzte Aufgabe).
- **f) Stufe/Typ: 0.**

### Nebenwirkung (Fakt)
- Feld `klasse` aus der Themenliste übernommen: `{"ib_myp": 3}` → `{"ib_myp": 5}`.

### Lehrplan
- Annahme: Streudiagramm, Art/Stärke des Zusammenhangs, Ausgleichsgerade nach Augenmaß und „Korrelation ≠ Ursache“ passen zu IB MYP (Sekundärquelle revisiondojo.com/myp/myp-extended-mathematics/notes nennt „Covariance and Correlation“ als Extended-Kapitel, abgerufen 20.11.2026; IB-Dokument nicht frei abrufbar). **Widerspruch:** Die Datei war für MYP 3 gebaut (`offen`: „Regressionsrechnung ist nicht Stoff von MYP 3“), die Themenliste führt das Thema jetzt bei MYP 5 (Klasse 10). Für Klasse 10 fehlt dann vermutlich der Korrelationskoeffizient r (Bedeutung, grobe Einordnung) – Annahme, nicht geändert; Entscheidung beim Haupt-Chat.

## 2026-11-20 – daten.normalverteilung (Normalverteilung)

**Urteil: mit Korrekturen in Ordnung** (eine Formulierung).

### Umfang (Fakt)
- Gelesen: 5 Lernkarten und alle 178 Aufgaben (118 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle 178 von Hand – Grenzen μ ± kσ, Anteile nach 68-95-99,7 (Streifen 34 / 13,5 / 2,35 / 0,15 %), Anzahlen aus Anteilen, z-Werte und Umkehrungen, alle z-Vergleiche (auch die Richtung „um wie viel ist z in X größer“). Histogramm-Tabellen auf Symmetrie/Gipfel gelesen. Grafiken: nur die JSON-Parameter (μ, σ, Höhe a) gegen Text und Lösung geprüft.
- Prüfskript nach der Änderung: OK, 0 Gruppen „gleich gebaut hintereinander“.

### Änderungen je Fehlerart (1 Aufgabe)
- **a) falsche Lösung: 0.**
- **b) mehrdeutig: 1.** anteile, Stufe 3 rueckwaerts: „Ab welchem Wert gehört man zu den 16 % mit den kleinsten Werten?“ – „ab“ meint im Deutschen „von … an aufwärts“, gemeint war die Grenze nach unten. Jetzt: „Unter welchem Wert liegen etwa die 16 % kleinsten Werte?“ (Lösung 1 400 h unverändert). Die Variante „… mit den größten Werten“ bleibt.
- **c) späterer Stoff: 0** (Standardabweichung, Median, Prozent – alles früher bzw. gleiche Klasse; keine Tabellen, kein GDC).
- **d) Lernkarten: 0. e) Tipp/Optionen: 0. f) Stufe/Typ: 0.**

### Nebenwirkung (Fakt)
- Feld `klasse` aus der Themenliste übernommen: `{"zusatz": 10}` → `{"ib_myp": 5}`.

### Nicht geändert, zur Kenntnis (Meinung)
- regel, begruenden („Fahrzeiten μ = 12 min, σ = 7 min – passt eine Normalverteilung?“): Die falsche Option „Nein, weil σ größer als 5 min ist“ hat eine wahre Prämisse und das richtige „Nein“, nur eine untaugliche Begründung. Die richtige Option ist klar überlegen; belassen.
- „|z| > 2 = ungewöhnlich“ ist eine Konvention, in der Lernkarte als solche eingeführt.

### Lehrplan
- Annahme: Passt zu IB MYP Jahr 5 (Klasse 10), Extended. Die Normalverteilung ist laut Sekundärquellen kein fester MYP-Kerninhalt, sondern schulabhängig (die Datei vermerkt „Verlagsinhalt IB Extended“); Belege: revisiondojo.com/blog/what-topics-are-in-myp-extended-mathematics (abgerufen 20.11.2026) nennt sie nicht ausdrücklich – also **nicht belegbar, Annahme**. Inhaltlich als Vorstufe zu IB DP passend; es fehlt nichts Wesentliches für die gewählte Tiefe (nur Faustregel).

## 2026-11-20 – daten.standardabweichung (Standardabweichung)

**Urteil: mit Korrekturen in Ordnung.**

### Umfang (Fakt)
- Gelesen: 5 Lernkarten und alle 181 Aufgaben (121 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle 181 von Hand (Mittelwerte, Abweichungen, Varianzen, σ mit Rundung, Lineartransformationen, Bereich x̄ ± σ). Zusätzlich per eigenem Skript (unabhängig vom Generator): alle Varianz-Vergleiche A/B, alle angegebenen Mittelwerte, alle „Berechne Varianz/σ“-Aufgaben, alle Zählungen im Bereich x̄ ± σ (dort auch, ob x̄ und σ zum Datensatz passen) und „weicht am stärksten ab“ auf Gleichstand – 0 Abweichungen.
- Prüfskript nach der Änderung: OK, 0 Gruppen „gleich gebaut hintereinander“.

### Änderungen je Fehlerart (5 Aufgaben)
- **a) falsche Lösung: 0.**
- **b) unklare Angabe: 2.** varianz, Stufe 3 fehler: „Mia … erhält −15, weil sie (−12)² = −144 gesetzt hat“ – mit nur diesem Fehler käme −14,5 heraus; −15 entsteht erst, wenn *alle* negativen Abweichungen negativ quadriert werden (auch (−1)² = −1). Ebenso „erhält 18, weil sie (−7)² = −49 …“ (dort zusätzlich (−10)²). Jetzt: „… weil sie die Quadrate der negativen Abweichungen negativ gesetzt hat, z. B. (−12)² = −144.“ Lösung unverändert.
- **c) späterer Stoff: 0** (Wurzel Kl. 9, Median Kl. 7, Prozent Kl. 6 – alles früher).
- **d) Lernkarten: 0.**
- **e) Tipp/Optionen: 0.**
- **f) Typ: 3.** eigenschaften, Stufe 3: Zwei Umrechnungs-Aufgaben („Test … in Prozent umrechnen, x̄ und σ danach?“) standen als `begruenden`, sind aber reine Rechenaufgaben. Jetzt die 50-Punkte-Variante `transfer`, die 10-Punkte-Variante `verknuepfen` (Prozentrechnung). Dadurch hat sich die Reihenfolge der Stufe-3-Übungen dieser Lernkarte verschoben (gleiche Aufgaben, keine zwei gleichen Typen hintereinander); die σ-0-Aufgabe bleibt `begruenden`.

### Nebenwirkung (Fakt)
- Feld `klasse` beim Neuerzeugen aus der Themenliste übernommen: `{"ib_myp": 4}` → `{"ib_myp": 5}`.

### Nicht geändert, zur Kenntnis
- Meinung: „Test höchstens 10 Punkte, x̄ = 7, σ = 4“ ist möglich (σ ≤ √21 ≈ 4,58), aber eine sehr extreme Verteilung. Belassen.
- Fakt: Lösungswege zeigen bei „auf zwei Nachkommastellen“ z. B. „≈ 4,1“ statt „4,10“ (Zahlformat des Generators); die Eingabe 4,1 wird angenommen.

### Lehrplan
- Annahme: Passt zu IB MYP Jahr 5 (Klasse 10), Extended Mathematics („standard deviation“ als Extended-Inhalt laut Sekundärquelle revisiondojo.com/blog/myp-math-statistics-and-probability, abgerufen 20.11.2026; IB-Originaldokument nicht frei abrufbar). Rechnung mit n (Gesamtheit) ist unter `offen` begründet. Es fehlt nichts Wesentliches; der Taschenrechner-Weg (GDC) wird bewusst nicht geübt.

## 2026-11-20 – zahlen.schranken (Schranken und Genauigkeit)

**Urteil: mit Korrekturen in Ordnung.**

### Umfang (Fakt)
- Gelesen: 5 Lernkarten (Einstieg, Wörter, Regel, Schritte, Bild, Fehler) und alle 180 Aufgaben (120 Übungen, 5 Test, 15 Korrektur, 30 Sicherung, 10 Knobel).
- Nachgerechnet: alle 180 Lösungen von Hand (Schranken, Summen/Differenzen, Produkte/Quotienten, Ja/Nein-Entscheidungen über den ungünstigsten Fall); bei Quotienten zusätzlich die Rundung auf zwei Stellen.
- Prüfskript nach der Änderung: OK, 0 Gruppen „gleich gebaut hintereinander“, Mengen unverändert (S1/S2/S3 je Lernkarte wie vorher, Test 5, Korrektur 15, Sicherung 30, Knobel 10).

### Änderungen je Fehlerart (29 Aufgaben)
- **a) falsche Lösung: 0.**
- **b) mehrdeutig: 18.** „Ist die Fahrt sicher erlaubt? / Passt der Schrank sicher? / Reicht das Brett sicher?“ hatte die Antworten „Ja / Nein / Das lässt sich nicht entscheiden.“ In allen Nein-Fällen liegt der wahre Wert beiderseits der Grenze – dann ist „lässt sich nicht entscheiden“ ebenso vertretbar wie „Nein“. Jetzt drei klare Zustände wie bei der Zug-Aufgabe: „Ja, sicher.“ / „Nicht sicher: im ungünstigsten Fall …“ / „Sicher nicht: … auf jeden Fall …“ (Letzteres ist bei den erzeugten Zahlen nie richtig, geprüft: untere Schranke liegt immer unter der Grenze). Betrifft Lernkarte entscheiden (11 Übungen, 1 Test, 2 Korrektur, 4 Sicherung).
- **c) späterer Stoff: 0.**
- **d) Lernkarten-Erklärung: 0.**
- **e) Tipp / Antwortoptionen: 10.**
  - 6× Tipp bei „untere Schranke der Geschwindigkeit“ bzw. „Wie breit ist es mindestens?“ lautete „Für das Maximum durch die kleinste Zahl teilen“ – führt bei einer Minimum-Frage in die falsche Richtung. Jetzt richtungsabhängig („Für das Minimum durch die größte Zahl teilen“).
  - 4× „Wie genau wurde gemessen?“ (3 Übungen, 1 Korrektur): Die falschen Optionen gehörten zu anderen Größen („auf 0,1 kg genau gewogen“ bei einer Zeitmessung) und waren allein an der Einheit auszuschließen. Jetzt in derselben Einheit mit echten Denkfehlern: halbe Breite (0,05 s), zehnfach, ein Zehntel. Lösungsweg ergänzt: „Die halbe Breite ist nur der größte Fehler.“
- **f) Stufe/Typ: 1.** grenzen, Stufe 3 transfer: „Wie viele Teilnehmer waren es mindestens?“ war nur die untere Schranke (Stufe-1-Gedanke). Jetzt: „Wie viele verschiedene Werte sind für die Zahl der Teilnehmer möglich?“ (Lösung 10, Fehlerbereich 885 ≤ n < 895). Typ und Stufe bleiben.

### Nebenwirkung (Fakt)
- Beim Neuerzeugen übernimmt die Datei das Feld `klasse` aus `themenliste.json`: vorher `{"zusatz": 10}`, jetzt `{"ib_myp": 5}`. Die alte Datei war gegenüber der Themenliste veraltet; ich habe das nicht zurückgedreht.

### Nicht geändert, zur Kenntnis (Meinung)
- „höchstens/mindestens“ wird für die nicht angenommene obere Schranke verwendet (z. B. dritte Dreiecksseite „höchstens 13,5 cm“). Das ist die übliche IB/GCSE-Konvention und in der Lernkarte so eingeführt; mathematisch streng wäre „kleiner als“. Belassen.
- Knobel entscheiden „Ja, weil 12 + 27 = 39 t“ hat das richtige Ja mit unzureichender Begründung; die richtige Option ist klar besser begründet. Belassen.

### Lehrplan
- Annahme: Passt zu IB MYP Jahr 5 (Klasse 10), Extended Mathematics. Das offizielle IB-Fachdokument („MYP mathematics guide“) ist nicht frei abrufbar; Sekundärquelle RevisionDojo nennt „bounds“ als üblichen Extended-Inhalt (revisiondojo.com/blog/what-topics-are-in-myp-extended-mathematics, abgerufen 20.11.2026). Kein bayerischer Lehrplanbezug (Datei vermerkt „ohne Lehrplan-Zuordnung“). Wesentliches fehlt nicht; Schranken bei negativen Größen sind bewusst ausgelassen (unter `offen` vermerkt).

### Nicht geprüft
- Darstellung der Bilder in der App (nur die JSON-Angaben gelesen).
