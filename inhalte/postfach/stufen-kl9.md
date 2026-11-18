# Postfach stufen-kl9 (Zwanzigste Runde, Klasse 9)

Neueste Meldung oben.

## 2026-11-18 04:20 – STATUS
Inhaltliche Prüfung aller neuen Aufgaben, Klasse 9 (Korrektur nach der Zwanzigsten Runde)

**Umfang:**
- Alle 14 Themen mit klasse.gym_by = 9.
- „Neu“: Pool uebung oder bonus, Fragetext nicht in 4eda8cb.
- Vorher `origin/lernen-app` nach `stufen-kl9` geholt; der Stand ließ sich vorspulen, es war kein Merge-Commit nötig.

**Geprüft:**
- 697 neue Aufgaben: 516 Übungen und 181 Knobel-Bordkarten.
- Je Aufgabe vollständig gelesen: Fragetext, alle Optionen, Tipp und Lösungsweg.
- Jede Lösung von Hand nachgerechnet.
- Alle Zähl-, „höchstens“- und „mindestens“-Knobel zusätzlich per Programm durchgezählt, 25 Fälle, alle bestätigt.
- Formal geprüft: keine doppelten Optionen, 3–4 Optionen je Auswahl, Typ g und Tipp h vorhanden.

**Geändert:** 40 neue Aufgaben, alte Aufgaben unverändert. Je Thema meldet inhalt_pruefen OK mit 0 Gruppen „gleich gebaut hintereinander“, der Nachweis ist OK.

| Thema | geändert |
|---|---|
| zahlen.wurzeln_basis | 3 |
| zahlen.reell | 3 |
| funktionen.quadratisch | 7 |
| gleichungen.quadratisch | 3 |
| gleichungen.lgs3 | 4 |
| stochastik.verknuepft | 3 |
| abbildungen.aehnlichkeit | 1 |
| zahlen.rationale_exponenten | 6 |
| funktionen.potenz | 1 |
| gleichungen.potenz | 2 |
| trigo.pythagoras | 3 |
| trigo.rechtwinklig | 2 |
| trigo.allgemein | 1 |
| gleichungen.trig | 1 |

**Nach Fehlerart** (je Aufgabe die Hauptart):
- **a) Falsche oder nicht eindeutige Lösung: 1**
  - funktionen.quadratisch/bestimmen. Vorher: „Stimmt: Durch zwei verschiedene Punkte geht genau eine Parabel y = ax² + bx + c?“ Die Antwort „unendlich viele“ ist falsch, wenn beide Punkte denselben x-Wert haben; dann gibt es keine.
  - Nachher: „… Durch zwei Punkte mit verschiedenen x-Werten …“
- **b) Mehrdeutige Zählweise: 0**
  - In den neuen Aufgaben der Klasse 9 kommt kein Zahlenstrahl vor und kein „k. Strich“, „k. Stelle“ oder „nach dem Anfang“. Gesucht wurde nach Strich, Stelle und Anfang.
- **c) Stoff aus späteren Themen: 11**
  - Hauptfall: Lösen über Substitution (u = x², u = sin x, u = x^(1/4), w = √x). Das ist Stoff von Kl. 10 gleichungen.polynom.
  - Beispiel gleichungen.potenz/anzahl, vorher: „Wie viele Lösungen hat x⁴ − 5x² + 4 = 0?“, Weg „Mit u = x²: u² − 5u + 4 = 0 …“.
  - Nachher: „Wie viele Lösungen hat (x² − 5)⁴ = 16?“, Weg über „die Klammer ist 2 oder −2“.
  - Ebenso: zwei Knobel in gleichungen.potenz, je einer in gleichungen.trig, funktionen.potenz, zahlen.rationale_exponenten, gleichungen.quadratisch und zahlen.wurzeln_basis.
  - Außerdem:
    - Pfadregel 0,6 · 0,5 (Kl. 10 stochastik.mehrstufig) ersetzt durch Rechnen mit 100 Kindern.
    - Bakterienwachstum innerhalb der Stunde mit 16^(1/4) (Exponentialmodell, Kl. 10) ersetzt durch Würfelkante a = V^(1/3).
    - In zahlen.wurzeln_basis (laut Umfang „ohne Irrationalität und Wurzelalgebra“): √(4n) = 2√n ersetzt; ebenso die Behauptung „sonst endet die Dezimalzahl nie“.
- **d) Unklare Fragen: 9**
  - Beispiel funktionen.quadratisch/extremwert, vorher: „Wie klein kann die Summe ihrer Quadrate höchstens werden?“ Nachher: „Wie groß ist die Summe ihrer Quadrate mindestens?“
  - Ebenso:
    - „Eine Normalparabel (a = 1) … Prüfe, für welches a …“ (Widerspruch im Text)
    - „Bei festem Umfang hat ein Rechteck höchstens 49 cm²“
    - „Nach dem Rationalmachen steht da 2√a/a. Vorher hieß … Jetzt steht …“
    - „… damit es genau ein Dreieck mit β = 90° gibt“
  - 4 Tipps verwiesen auf „die Lernkarte“ oder „das Beispiel mit 27^(2/3)“; in Mischkarten fehlt dieser Bezug. Sie sind durch eigenständige Tipps ersetzt.
- **e) Antwortoptionen: 1**
  - zahlen.reell/heron, Knobel. Vorher hatte die Ja-Option als Begründung die Behauptung selbst: „Ja, denn (x + a : x) : 2 ≥ √a gilt immer.“
  - Nachher: „Ja: Der Mittelwert von x und a : x ist nie kleiner als √a.“ Den fehlenden Schritt im Weg habe ich ergänzt.
- **f) Lösungswege mit Sprüngen: 18**
  - Beispiel gleichungen.lgs3, Knobel „100 Tiere“. Vorher: „Mit k, s ≥ 1 ganzzahlig: k = 5, s = 1.“
  - Nachher: „5s = 100 − 19k muss durch 5 teilbar sein, also auch 19k – das geht nur, wenn k durch 5 teilbar ist. k = 5 gibt s = 1, k = 10 ist zu groß.“
  - Weitere Fälle:
    - Faktorisieren von x² − 4x − 12 in funktionen.quadratisch; die Karte lehrt die Lösungsformel, Faktorisieren kommt erst im nächsten Thema. Ersetzt durch D und die Formel.
    - „Scheitel bei x = −b/(2a)“ (nicht eingeführt)
    - „Abstände der y-Werte wachsen um 2, das passt zu a = 1“
    - Eindeutigkeit bei „Durchprobieren“ (Pythagoras 25, 2¹², 64^(1/n), Quadratzahlen mit Abstand 7)
    - Kehrwerte bei tan 30° und tan 60°
    - Spinne: Weg über zwei Wände, obwohl nur Boden und eine Wand erlaubt sind

**Gewählte Lesarten:**
- **c) Maßstab:** Reihenfolge der Themen in themenliste.json. Vorgriffe auf eine spätere Lernkarte desselben Themas zählen nicht als Fehler.
- **f) Auslassungspunkte:** „…“ in Aufzählungen mit klarer Regel („45², 46², …, 54²“) und in Dezimalentwicklungen („0,1212…“) zählt nicht als Fehler. Gezählt habe ich nur ausgelassene Gedankenschritte.
- **Zinseszins:** Wachstum mit ganzzahliger Zahl von Jahren und demselben Faktor ist erlaubt, wie in alten Aufgaben.
- **Riesenrad:** Das Riesenrad-Bild in Tipps zu gleichungen.trig ist die Methode der Lernkarten und kein Verweis auf eine bestimmte Lernkarte.

**Technisch:**
- **Neuer Nachweis:** In _stufen_kl9.py gibt es jetzt den Modus `korrektur` gegen origin/lernen-app. Er prüft:
  - Alle Aufgaben, deren Text es schon in 4eda8cb gab, und alle Nicht-Übungen sind vollständig gleich, auch g und s.
  - Geänderte neue Aufgaben behalten Lernkarte, Pool, g, s und y.
  - Die Zahl der Aufgaben ist gleich.
  - Die Typregeln gelten weiter.
- **Klassenfeld:** Der Neubau gleicht in 7 Dateien das Feld klasse (rs_by/ib_myp) an themenliste.json an:
  - zahlen.reell
  - funktionen.quadratisch
  - stochastik.verknuepft
  - zahlen.rationale_exponenten
  - gleichungen.potenz
  - trigo.rechtwinklig
  - gleichungen.trig

  Die JSON-Dateien auf lernen-app waren dort veraltet. Der Nachweis lässt das nur zu, wenn der neue Wert gleich themenliste.json ist.
- **Commits:** ein Commit je Thema. Abweichungen:
  - Die vier Tipp-Korrekturen (d) in stochastik.verknuepft, zahlen.rationale_exponenten und trigo.rechtwinklig stehen gemeinsam in einem Nachtrags-Commit.
  - zahlen.wurzeln_basis hat zwei Commits.

**Nicht geprüft:**
- Wie Schablonen mit Dezimal-Lücken („□,□“) und negative Lücken in der App angezeigt werden (kein App-Code).
- Ob Rundungen mit einem anderen Taschenrechner-Modus abweichen. Alle Werte sind mit Gradmaß gerechnet; Toleranzen nach README.
- Ob jede Formulierung zum LehrplanPLUS-Wortlaut passt. Maßstab war nur themenliste.json mit umfang und lehrplan_gym.
- Alte Aufgaben, wie im Auftrag festgelegt.

## 2026-11-17 15:09 – FERTIG
Abschlussbericht Zwanzigste Runde, Klasse 9: alle 14 Themen erledigt. Zweig stufen-kl9, ein Commit je Thema, kein Merge. Keine Datenbank, kein App-Code, keine Tests.

**Gesamt:** 516 neue Übungen, 181 Knobel-Bordkarten (Pool bonus, g knobel, jede mit Tipp und ausführlichem Weg), 537 überzählige Übungen gemeldet und nicht gelöscht.

**Prüfung je Thema:**
- tools/inhalt_pruefen.py: OK, 0 Gruppen „gleich gebaut hintereinander“.
- inhalte/generatoren/_stufen_kl9.py nachweis: OK. Geprüft wird:
  - Alte Übungen sind gegen origin/lernen-app nur in g und s geändert; Lernkartentexte sind unverändert.
  - S1 ≥ 4 Übungen mit ≥ 2 Typen, S2 ≥ 6 mit ≥ 3 Typen, S3 ≥ 8 mit ≥ 4 Typen.
  - Auf S3 höchstens 3 Übungen je Typ.
  - Je Stufe und Typ höchstens 2 gleich gebaute Übungen.
  - Nie zwei Übungen gleichen Typs direkt hintereinander.
- Jede c-Formel rechnet die Lösung nach (Generator-Assert).
- Jede neue Aufgabe von Hand gelesen.

**Umgang mit Überzähligen** (siehe FRAGE 14:21, Annahme beibehalten):
- Ab der 3. gleich gebauten Übung je Stufe und Typ, auf Stufe 3 ab der 4. Übung desselben Typs, bleibt die Übung unverändert und ohne g.
- Liste: inhalte/postfach/stufen-kl9-ueberzaehlig.md.
- Folge: inhalt_pruefen prüft die strengen Typregeln auf diesen Lernkarten nicht. Das übernimmt der Nachweis auf den Übungen mit Typ.

**Abweichungen und Hinweise:**
- gleichungen.lgs3, Karte stufenform: nur 1 Knobel-Bordkarte. Grund: Die Stufenform ist reines Rückwärtseinsetzen. Eine zweite Knobelaufgabe würde nichts Neues bieten, nur dieselbe Rechnung mit anderen Zahlen.
- trigo.rechtwinklig/anwendung S2: Eine alte Übung (Turm, 64 m, 30°) verlangt „auf eine Nachkommastelle“, die gespeicherte Lösung ist 37. Wert und Toleranz stimmen (36,95 ≈ 37,0). Nach Auftrag nicht geändert.
- Annahme: Stufe 2 und 3 nutzen nur Inhalte der jeweiligen Lernkarte und früherer Karten des Themas. Beispiele: Riesenrad- und Einheitskreis-Deutung, quadratische Gleichungen in Knobelaufgaben. Bei trigo.allgemein sind Sinus- und Kosinussatz der Inhalt der Karten selbst.

### 1–2) Stufen-Leiter und Übungen je Stufe und Typ (vorher → nachher)

„vorher“: Übungen je Stufe auf origin/lernen-app; dort hatte noch keine Übung ein g.
„nachher“: Übungen mit Typ, in Klammern nach Typ. Die überzähligen stehen ohne Typ in der letzten Spalte.

Typkürzel:
- dir: direkt
- erk: erkennen
- mehr: mehrschritt
- eink: einkleidung
- umk: umkehr
- dar: darstellung
- rück: rueckwaerts
- verk: verknuepfen
- begr: begruenden
- fehl: fehler
- trans: transfer
- par: parameter
- prüf: pruefung

### zahlen.wurzeln_basis

Neue Übungen 47, Knobel-Bordkarten 12, überzählig 61.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| quadratwurzel | Quadratwurzel einer Quadratzahl angeben und Quadratzahlen erkennen. / Wurzeln in Rechenketten, rückwärts (√x = a) und in einfachen Sachsituationen. / Ganzzahligkeit begründen, Fehler beim Wurzelziehen finden, Bedingungen für k suchen, mehrteilige Aufgaben. | 6 → 5 (dir 3, erk 2) | 12 → 8 (mehr 5, eink 1, umk 2) | 6 → 8 (rück 1, verk 2, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 10 |
| wurzel_dezimal | Wurzel aus einer Dezimalzahl mit gerader Stellenzahl oder aus einem Bruch ziehen. / Mehrere Wurzeln verrechnen, rückwärts (√x = 0,03) und Flächen in Metern und Zentimetern. / Erkennen, wann die Wurzel keine endliche Dezimalzahl ist, Fehler finden, Bedingung für n, mehrteilige Sachaufgabe. | 7 → 4 (dir 2, erk 2) | 9 → 12 (mehr 7, eink 3, umk 2) | 8 → 8 (rück 1, verk 1, begr 2, fehl 1, trans 1, par 1, prüf 1) | 2 | 10 |
| kubikwurzel | Dritte Wurzel einer Kubikzahl angeben, Kubikzahlen erkennen. / Dritte Wurzeln aus Dezimalzahlen und Brüchen, in Rechenketten, rückwärts und bei Würfeln im Alltag. / Würfel aus Würfelchen zählen, Wachstum der Kante, Fehler 8 · 8 statt 8 · 8 · 8, Bedingung für k, mehrteilige Aufgabe. | 6 → 4 (dir 3, erk 1) | 14 → 9 (mehr 7, eink 1, umk 1) | 5 → 8 (rück 1, begr 1, fehl 1, trans 3, par 1, prüf 1) | 2 | 12 |
| abschaetzen | Die zwei Quadratzahlen um a finden und √a zwischen zwei natürliche Zahlen setzen. / Auf Zehntel genau eingrenzen, rückwärts passende n suchen, Seitenlängen von Flächen schätzen. / Dritte Wurzeln eingrenzen, nächste natürliche Zahl begründen, Fehler „halbieren“ finden, Zahlen vergleichen, mehrteilige Aufgabe. | 15 → 4 (dir 3, erk 1) | 4 → 8 (mehr 3, eink 2, umk 1, dar 2) | 5 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 15 |
| wurzel_deuten | Wissen, dass √a nie negativ ist, (√a)² = a, und x² = a zwei Lösungen hat. / Lösungen von x² = c bei Dezimalzahlen, Quadrate von Wurzeln verrechnen, Lösungen am Graphen. / Fehler wie √(a + b) = √a + √b finden, Bedingungen (für welche x erklärt), Aussagen über √(a²) prüfen, Fachsprache. | 11 → 7 (dir 1, erk 6) | 4 → 6 (mehr 3, eink 1, umk 1, dar 1) | 9 → 9 (verk 1, begr 3, fehl 3, par 2) | 2 | 7 |
| wurzel_sache | Seite eines Quadrats aus der Fläche (oder Kante eines Würfels aus dem Volumen) berechnen. / Mit Einheiten umrechnen, Umfang oder Oberfläche als Zwischenschritt, Fläche aus Umfang. / Runden, Wassertank in Litern, Zaun mit Einfahrt, Vergrößern, Fehler V : 6, Bedingung a³ = 6a², mehrteilige Aufgabe. | 6 → 4 (dir 3, erk 1) | 11 → 11 (mehr 6, eink 4, umk 1) | 7 → 8 (verk 2, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 7 |

### zahlen.reell

Neue Übungen 37, Knobel-Bordkarten 14, überzählig 63.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| zahlarten | Eine einzelne Wurzel als rational oder irrational einordnen. / Aus einer Liste die irrationale Zahl wählen, periodische Dezimalzahlen und negative Wurzeln einordnen. / Aussagen über Zahlenmengen prüfen, Fehler bei periodischen Zahlen finden, zählen, wie viele Wurzeln rational sind, Produkte von Wurzeln einordnen. | 9 → 7 (dir 1, erk 6) | 7 → 7 (mehr 4, eink 1, umk 1, dar 1) | 8 → 8 (verk 3, begr 3, fehl 1, trans 1) | 2 | 5 |
| eingrenzen | Zehntel quadrieren und eine Wurzel auf Zehntel genau eingrenzen. / Auf Hundertstel eingrenzen, Wurzel mit Dezimalzahl vergleichen, rückwärts passende Zahlen n finden. / Zahlen zwischen zwei Wurzeln finden, Sachfragen mit Mindestmaß, Fehler „1,4 ist √2“, Bedingungen für eine Ziffer, mehrteilige Aufgabe. | 6 → 4 (dir 3, erk 1) | 14 → 8 (mehr 6, eink 1, umk 1) | 5 → 8 (verk 3, fehl 1, trans 2, par 1, prüf 1) | 2 | 12 |
| wurzel_mal | Zwei Wurzeln mit √a · √b = √(a · b) malnehmen und erkennen, wann die Regel passt. / Wurzeln teilen, Rechenketten, Quadrate unter der Wurzel mit Betrag, Flächen von Rechtecken. / Terme mit Variablen, Bedingung √(x²) = x, kleinstes n für eine natürliche Wurzel, Fehler √a · √b = √(a + b), Sachformeln. | 7 → 4 (dir 2, erk 2) | 12 → 10 (mehr 6, eink 2, umk 2) | 11 → 8 (verk 3, begr 1, fehl 1, trans 1, par 2) | 2 | 11 |
| teilweise | Die größte Quadratzahl im Radikanden finden und teilweise die Wurzel ziehen. / Umgekehrt a√b als eine Wurzel schreiben, Seitenlängen exakt angeben, Produkte unter der Wurzel vereinfachen. / Terme mit Variablen, Zahlen mit Wurzeln vergleichen, Fehler √50 = 25√2 finden, besondere Zahlen suchen, mehrteilige Aufgabe. | 15 → 4 (dir 2, erk 2) | 4 → 6 (mehr 1, eink 2, umk 3) | 6 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 14 |
| zusammenfassen | Vielfache derselben Wurzel addieren und subtrahieren, erkennen, wann es nicht geht. / Erst teilweise die Wurzel ziehen, dann zusammenfassen; eine fehlende Wurzel ergänzen; Zaunlängen exakt. / Binomische Formeln mit Wurzeln, Fehler √2 + √8 = √10, Aussagen prüfen, Bedingung für a, mehrteilige Aufgabe. | 6 → 6 (dir 5, erk 1) | 8 → 9 (mehr 7, eink 1, umk 1) | 11 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 7 |
| nenner_rational | Bei a/√b mit √b erweitern und kürzen. / Nenner wie 4√7 oder √m − n, Brüche aus zwei Wurzeln, rückwärts zum alten Bruch. / Summen mit zwei Wurzeln im Nenner, Fehler „nur den Nenner malnehmen“, Vergleich mit Dezimalzahl, Bedingung für a, mehrteilige Aufgabe. | 7 → 4 (dir 3, erk 1) | 9 → 7 (mehr 5, eink 1, umk 1) | 9 → 8 (rück 1, verk 3, begr 1, fehl 1, par 1, prüf 1) | 2 | 13 |
| heron | Einen Heron-Schritt ausführen: a : x und den Mittelwert bilden. / Zwei Schritte nacheinander, Tabellen lesen, aus einem Ergebnis die Zahl a zurückgewinnen. / Aus einem Schritt rückwärts schließen, Fehler im Verfahren finden, begründen, warum es funktioniert, Startwerte deuten, mehrteilige Aufgabe. | 4 → 8 (dir 6, erk 2) | 6 → 6 (mehr 2, eink 1, umk 1, dar 2) | 8 → 8 (rück 1, verk 1, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 1 |

### funktionen.quadratisch

Neue Übungen 45, Knobel-Bordkarten 16, überzählig 23.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| scheitel | Den Scheitel aus der Scheitelform oder einem Graphen ablesen. / Umgestellte Terme (−5 + 2(x − 4)²) lesen, aus Scheitel und Öffnung die Gleichung aufstellen. / Wertemenge, Scheitel aus Nullstellen oder gleich hohen Punkten, Fehler beim Vorzeichen, Bedingung für e, mehrteilige Sachaufgabe. | 12 → 10 (dir 8, erk 2) | 8 → 8 (mehr 6, umk 1, dar 1) | 4 → 8 (rück 1, verk 3, begr 1, fehl 1, par 1, prüf 1) | 2 | 2 |
| parameter | Verschiebung und Öffnung einer Parabel aus a, d, e erkennen. / Graphen zuordnen, Nullstellenzahl ohne Rechnen, Streckung im Sachzusammenhang. / Bedingungen an a, rückwärts verschieben, Bremsweg verdoppeln, Aussagen prüfen, Fehler beim Vorzeichen, mehrteilige Aufgabe. | 9 → 11 (dir 1, erk 10) | 11 → 11 (mehr 6, eink 1, dar 4) | 4 → 8 (rück 1, verk 1, begr 2, fehl 1, trans 1, par 1, prüf 1) | 2 | 0 |
| umformen | Bei a = 1 quadratisch ergänzen oder x = −b/(2a) nutzen. / Bei a = −1 oder a ≠ 1 erst ausklammern, ausmultiplizieren rückwärts, höchster Punkt einer Bahn. / Bedingungen für b und c, Fehler bei der Ergänzung, halbe Zahlen, Aussagen über Nullstellen, Gewinn maximieren, mehrteilige Aufgabe. | 9 → 8 (dir 7, erk 1) | 8 → 15 (mehr 13, eink 1, umk 1) | 9 → 8 (rück 1, verk 1, begr 1, fehl 1, trans 1, par 2, prüf 1) | 2 | 2 |
| nullstellen | Nullstellen aus der Produktform oder einem Graphen ablesen. / Mit der Lösungsformel oder der Scheitelform rechnen, Nullstellenzahl bestimmen, Gleichung zu gegebenen Nullstellen, Landepunkt. / Zweite Nullstelle aus einer bekannten, Bedingung für c, Fehler beim Ablesen, Tor-Breite, mehrteilige Aufgabe. | 6 → 4 (dir 3, erk 1) | 11 → 16 (mehr 14, eink 1, umk 1) | 7 → 8 (rück 1, verk 2, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 2 |
| punkte | Funktionswerte berechnen und die Punktprobe machen. / Werte im Sachzusammenhang, Differenzen von Funktionswerten, rückwärts f(x) = 5 lösen, Tabelle zuordnen. / Unbekannte Koordinate oder Parameter c bestimmen, gleich hohe Punkte deuten, Fehler mit dem Minus vor x² finden. | 8 → 16 (dir 15, erk 1) | 8 → 6 (mehr 2, eink 2, umk 1, dar 1) | 8 → 8 (rück 2, verk 2, fehl 1, par 3) | 2 | 1 |
| bestimmen | Mit Scheitel und einem Punkt den Faktor a bestimmen. / Mit Nullstellen ansetzen, aus Bogenmaßen oder Tabellen den Term finden, d aus einem Punkt bestimmen. / Drei Punkte, Ansatz-Fehler finden, Aussagen über Eindeutigkeit, Bedingung für a, Wurfbahn modellieren, mehrteilige Aufgabe. | 10 → 7 (dir 6, erk 1) | 8 → 7 (mehr 4, eink 1, umk 1, dar 1) | 6 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 12 |
| extremwert | Den größten oder kleinsten Wert einer quadratischen Funktion angeben. / Zielfunktion im Sachzusammenhang aufstellen (Zaun, Summe, Hauswand), rückwärts den Umfang finden. / Bahnen und Preise modellieren, Fehler beim Aufstellen der Zielfunktion, Aussagen begründen, Rundung im Sachzusammenhang. | 8 → 8 (dir 2, erk 6) | 8 → 7 (mehr 2, eink 4, umk 1) | 8 → 8 (verk 2, begr 1, fehl 1, trans 3, prüf 1) | 2 | 4 |
| schnittpunkte | Parabel und Gerade gleichsetzen, wenn beide einfach sind. / Gleichung umformen und lösen, Zahl der gemeinsamen Punkte, Geraden durch den Scheitel, Ball trifft Rampe. / Tangenten-Bedingungen, Mittelpunkt einer Sehne, Ursprungsgerade als Tangente, Sachmodelle, Fehler beim Umformen. | 4 → 5 (dir 2, erk 3) | 6 → 7 (mehr 5, eink 1, umk 1) | 8 → 8 (verk 2, fehl 1, trans 3, par 2) | 2 | 0 |

### gleichungen.quadratisch

Neue Übungen 41, Knobel-Bordkarten 16, überzählig 34.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| reinquadratisch | ax² − c = 0 nach x² auflösen und beide Lösungen angeben. / Leere Lösungsmenge erkennen, Terme auf beiden Seiten zusammenfassen, rückwärts c bestimmen, Flächengleichheit. / Klammern wie (x + 2)² = 25, Fehler ±√5 statt ±1 finden, Gleichungen ohne Lösung erkennen, Bremsweg. | 10 → 8 (dir 7, erk 1) | 5 → 7 (mehr 4, eink 1, umk 2) | 9 → 8 (verk 3, begr 1, fehl 3, trans 1) | 2 | 5 |
| ausklammern | x ausklammern und den Satz vom Nullprodukt anwenden. / Mit Faktor vor x² oder x auf beiden Seiten lösen, Wurfhöhe null setzen, a rückwärts bestimmen. / Fehler „durch x teilen“, x³ − 9x, Bedingung für b, Aussagen über x = 0, Rechteck mit gleicher Maßzahl, mehrteilige Aufgabe. | 6 → 5 (dir 4, erk 1) | 12 → 11 (mehr 9, eink 1, umk 1) | 6 → 8 (verk 2, begr 1, fehl 2, trans 1, par 1, prüf 1) | 2 | 6 |
| faktorisieren | Den Satz vom Nullprodukt bei fertigen Produkten anwenden. / x² + bx + c in zwei Klammern zerlegen, binomische Formeln erkennen, fehlende Zahl ergänzen. / Gleichung zu gegebenen Lösungen, Anzahl passender b, Fehler bei (x − 3)², Aussagen über c, Flächenaufgabe, mehrteilige Aufgabe. | 6 → 5 (dir 4, erk 1) | 15 → 14 (mehr 12, umk 1, dar 1) | 5 → 8 (rück 1, verk 1, begr 1, fehl 1, trans 1, par 2, prüf 1) | 2 | 4 |
| ergaenzung | x² + bx + c = 0 auf die Form (x + d)² = e bringen. / Vollständig lösen, die Ergänzung bestimmen, a ≠ 1 vorher ausklammern, c rückwärts, Flächenaufgabe. / Ungerades b, Wurzel-Lösungen 4 ± √d, Fehler bei der Ergänzung, Bedingung für q, begründen, mehrteilige Aufgabe. | 13 → 10 (dir 9, erk 1) | 6 → 7 (mehr 5, eink 1, umk 1) | 5 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 5 |
| loesungsformel | a, b, c ablesen und die Diskriminante berechnen. / Mit der Formel lösen, auch mit a < 0 oder Dezimalzahlen, Gleichung aus dem Ergebnis der Formel zurückgewinnen. / Erst umformen, Fehler beim Vorzeichen von c finden, Aussagen über ganzzahlige Lösungen prüfen, Parameter mit Wurzel-Lösung, Wurfhöhe. | 7 → 8 (dir 7, erk 1) | 10 → 14 (mehr 12, eink 1, umk 1) | 7 → 8 (rück 1, verk 3, begr 1, fehl 1, trans 1, par 1) | 2 | 1 |
| diskriminante | Am Vorzeichen von D oder am Graphen die Lösungszahl ablesen. / c für genau eine Lösung bestimmen, erst umformen, Höhenfragen im Sachzusammenhang, D = 0 am Graphen deuten. / Fehler „± heißt zwei Lösungen“, Bedingungen an a, c und k, Vorzeichen-Begründung, Begegnungen in einer Wurfbahn. | 10 → 11 (dir 1, erk 10) | 7 → 7 (mehr 1, eink 1, umk 4, dar 1) | 7 → 9 (begr 2, fehl 3, trans 1, par 3) | 2 | 2 |
| sachaufgabe | Seite eines Quadrats aus der Fläche und daraus den Umfang bestimmen. / Rechteck mit „länger als breit“, Zahlenrätsel, Werte aus einer Tabelle fortsetzen. / Wege, Rahmen und Würfe modellieren, unpassende Lösungen aussortieren, Fehler bei negativen Längen, Unmöglichkeit begründen. | 6 → 4 (dir 3, erk 1) | 8 → 7 (mehr 2, eink 4, dar 1) | 10 → 9 (verk 3, begr 1, fehl 1, trans 3, prüf 1) | 2 | 11 |
| bruchgleichung | Definitionsmenge angeben, mit dem Nenner malnehmen und die quadratische Gleichung lösen. / Nenner wie x − 1, Hyperbel und Gerade schneiden, Scheinlösungen streichen, Rechteckseiten aus einer Bruchgleichung. / Zwei Brüche, Berührbedingung, Preis- und Geschwindigkeitsaufgaben, Fehler bei Scheinlösungen, Bedingung für a. | 4 → 4 (dir 3, erk 1) | 6 → 7 (mehr 5, eink 1, dar 1) | 8 → 8 (verk 3, fehl 1, trans 2, par 2) | 2 | 0 |

### gleichungen.lgs3

Neue Übungen 42, Knobel-Bordkarten 11, überzählig 21.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| pruefen | Ein Zahlentripel in eine Gleichung einsetzen. / Ein Tripel in allen drei Gleichungen prüfen, eine fehlende Koordinate bestimmen, Preise im Sachzusammenhang prüfen. / Zwei Lösungsvorschläge beurteilen, Parameter bestimmen, widersprüchliche Systeme erkennen, unvollständige Probe finden, mehrteilige Aufgabe. | 6 → 6 (dir 5, erk 1) | 14 → 16 (mehr 14, eink 1, umk 1) | 4 → 8 (verk 1, begr 2, fehl 1, trans 1, par 2, prüf 1) | 2 | 1 |
| stufenform | Ein System in Stufenform mit Koeffizient 1 von unten lösen. / Andere Koeffizienten und vertauschte Reihenfolge, ein Sachrätsel in Stufenform, ein System zur Lösung ergänzen. / Verdeckte Zahl rückwärts, Fehler beim Einsetzen, 0 · z = 5 oder 0 = 0 deuten, Parameter, Dezimalzahlen, mehrteilige Aufgabe. | 6 → 7 (dir 6, erk 1) | 11 → 19 (mehr 17, eink 1, umk 1) | 7 → 8 (rück 1, verk 1, begr 2, fehl 1, trans 1, par 1, prüf 1) | 1 | 0 |
| eliminieren | Zwei Gleichungen addieren oder subtrahieren, wenn eine Variable dabei sofort wegfällt. / Vorher eine Gleichung mit einer Zahl malnehmen, die passende Rechnung auswählen, den Faktor k rückwärts finden, Preise vergleichen. / Summen wie x + y + z ohne Einzelwerte, Fehler beim Malnehmen, Parameter für zwei wegfallende Variablen, Widerspruch 0 = 3, mehrteilige Aufgabe. | 6 → 7 (dir 6, erk 1) | 11 → 16 (mehr 14, eink 1, umk 1) | 7 → 8 (verk 1, begr 2, fehl 1, trans 2, par 1, prüf 1) | 2 | 0 |
| loesen | Ein einfaches System lösen, in dem sich Variablen schnell eliminieren lassen. / Allgemeine Systeme, den geschicktesten Weg wählen, Tieraufgaben, fehlende Zahl aus der Lösung bestimmen. / Lösungsanzahl begründen, Summen-Trick, Parameter für unendlich viele Lösungen, Winkel im Dreieck, Fehler beim Teilen, mehrteilige Aufgabe. | 6 → 7 (dir 6, erk 1) | 12 → 17 (mehr 14, eink 2, umk 1) | 6 → 8 (rück 1, verk 1, begr 2, fehl 1, trans 1, par 1, prüf 1) | 2 | 0 |
| parabel | Drei Punkte mit x = 0, 1, −1 einsetzen und a, b, c bestimmen. / Beliebige Punkte, Werte aus einer Tabelle, Scheitel als Bedingung, ein Wasserstrahl im Sachzusammenhang. / Symmetrie nutzen, Brückenbogen, c aus Nullstellen, Fehler beim Einsetzen negativer x, Parameter, mehrteilige Wurfaufgabe. | 6 → 4 (dir 2, erk 2) | 14 → 8 (mehr 5, eink 1, umk 1, dar 1) | 6 → 8 (rück 1, verk 3, fehl 1, trans 1, par 1, prüf 1) | 2 | 12 |
| sachaufgabe | Zahlenrätsel mit drei Zahlen in Gleichungen übersetzen und lösen. / Vereine, Eintrittspreise und Einkäufe mit drei Unbekannten, Gleichungen selbst aufstellen. / Münzen, Ziffern, Winkel, Mischungen und paarweise Summen modellieren, Fehler beim Aufstellen finden, mehrteilige Aufgabe. | 7 → 4 (dir 3, erk 1) | 8 → 8 (mehr 1, eink 6, umk 1) | 9 → 8 (verk 3, fehl 1, trans 3, prüf 1) | 2 | 8 |

### stochastik.verknuepft

Neue Übungen 28, Knobel-Bordkarten 12, überzählig 17.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| verknuepfen | A ∩ B, A ∪ B und Ā in Worten deuten und bei Zahlen 1 bis 20 abzählen. / Ereignisse in Zeichen schreiben, „A, aber nicht B“ abzählen, Sachsituation mit zwei Merkmalen. / „Weder noch“ und Gegenereignisse von Verknüpfungen, Bedingungen an Teiler, Fehler bei „oder“, Beschreibungen beurteilen. | 6 → 6 (dir 4, erk 2) | 12 → 13 (mehr 9, eink 1, dar 3) | 6 → 8 (verk 3, begr 2, fehl 1, trans 1, par 1) | 2 | 0 |
| additionssatz | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) mit gegebenen Werten. / Rückwärts P(A ∩ B) finden, „keines“ berechnen, Prozentangaben und Glücksräder. / Fehlende Einzelwahrscheinlichkeit, Grenzen für P(A ∩ B), Fehler ohne Schnitt, Parameter p, Mängel-Statistik, mehrteilige Aufgabe. | 6 → 4 (dir 3, erk 1) | 8 → 12 (mehr 5, eink 5, umk 2) | 10 → 8 (rück 1, verk 1, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 7 |
| vierfeld | Ein fehlendes Feld aus Zeilen- oder Spaltensumme ergänzen. / Mehrere Felder nacheinander ergänzen, aus drei Angaben die ganze Tafel bauen, ein inneres Feld rückwärts bestimmen. / Falsche Summen finden, Prozentangaben verketten, Bedingungen wie „doppelt so groß“, Unmögliches erkennen. | 6 → 7 (dir 6, erk 1) | 11 → 12 (mehr 6, umk 1, dar 5) | 7 → 8 (rück 1, verk 3, begr 1, fehl 1, trans 1, prüf 1) | 2 | 1 |
| tafel_wkeit | Ein inneres Feld oder eine Randsumme durch die Gesamtzahl teilen. / Wahrscheinlichkeiten aus Tafeln mit Anzahlen oder Wahrscheinlichkeiten, „oder“ aus der Tafel, ein Feld rückwärts. / Fehlende Felder über den Additionssatz, Fehler beim Lesen eines Feldes, Summe der Felder begründen, Parameter p, mehrteilige Aufgabe. | 6 → 7 (dir 6, erk 1) | 14 → 15 (mehr 2, umk 1, dar 12) | 4 → 8 (rück 1, verk 3, begr 1, fehl 1, par 1, prüf 1) | 2 | 0 |
| bedingt | P_B(A) in einer Tafel ablesen: nur die Spalte B zählt. / Die Bedingung aus einem Text erkennen, Tafeln mit Merkmal A als Bedingung, P(B) im Baum. / Test-Aufgaben, Baumdiagramme rückwärts, P(B) aus P(A ∩ B) und P_B(A), Verwechslung von Zeile und Spalte finden. | 6 → 4 (dir 3, erk 1) | 8 → 8 (mehr 2, eink 1, dar 5) | 10 → 8 (rück 1, verk 3, fehl 1, trans 3) | 2 | 7 |
| verstehen | Gegenereignis von „mindestens einmal“ benennen und Grenzen 0 ≤ P ≤ 1 kennen. / Behauptungen über Unvereinbarkeit prüfen, mögliche Werte für P(A ∪ B) finden, Alltagsaussagen und Tafeln deuten. / Fehler im Additionssatz und bei „bestimmt“ finden, sichere Aussagen begründen, Bedingungen an P(B), unmögliche Angaben erkennen. | 11 → 12 (dir 1, erk 11) | 5 → 6 (mehr 2, eink 2, umk 1, dar 1) | 8 → 9 (verk 3, begr 2, fehl 3, par 1) | 2 | 2 |

### abbildungen.aehnlichkeit

Neue Übungen 29, Knobel-Bordkarten 12, überzählig 52.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| streckung | Eine Strecke mit k strecken und einen Bildpunkt mit positivem k bestimmen. / Negatives oder gebrochenes k, k aus zwei Längen bestimmen, Projektor im Sachzusammenhang. / Zentrum rückwärts finden, Streckungen hintereinander, Fehler „vom Ursprung aus“, Bedingung für k, Winkeltreue begründen, mehrteilige Aufgabe. | 9 → 4 (dir 3, erk 1) | 10 → 8 (mehr 4, eink 1, umk 3) | 5 → 8 (rück 1, verk 2, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 10 |
| aehnlich | Eine Seite einer ähnlichen Figur mit k berechnen und wissen, dass Winkel gleich bleiben. / Winkel prüfen, k aus zwei entsprechenden Seiten bestimmen, Umfänge berechnen. / Fallen bei gleichschenkligen und rechtwinkligen Dreiecken, Prozent beim Umfang, DIN-Format, Rahmen, Fehler „+2 cm“. | 6 → 4 (dir 2, erk 2) | 8 → 7 (mehr 5, eink 1, umk 1) | 10 → 9 (verk 2, begr 3, fehl 1, trans 3) | 2 | 8 |
| strahlensatz1 | Mit SA, SA' und SB die Strecke SB' berechnen. / Mit AA' statt SA', rückwärts SA' oder BB', X-Figur, Sachsituation mit Wegen. / Parallelität prüfen (Umkehrung), unbekanntes x, drei Parallelen, Dachschräge, Fehler „AA' statt SA'“. | 6 → 4 (dir 2, erk 2) | 8 → 8 (mehr 4, eink 1, umk 1, dar 2) | 10 → 8 (rück 1, begr 2, fehl 1, trans 2, par 2) | 2 | 8 |
| strahlensatz2 | Mit SA, SA' und AB die Parallelstrecke A'B' berechnen. / SA rückwärts, mit AA' rechnen, X-Figur, Lampe und Schatten. / AA' aus den Parallelen, Fehler „AA' statt SA'“ und falsche Verhältnisse finden, Mond, Laterne, Trapez. | 6 → 4 (dir 2, erk 2) | 9 → 6 (mehr 2, eink 1, umk 2, dar 1) | 9 → 8 (rück 2, verk 1, fehl 3, trans 2) | 2 | 10 |
| flaeche_volumen | Fläche mit k² und Volumen mit k³ verändern. / k aus dem Flächenfaktor finden, Maßstäbe für Flächen, Pizza-Vergleich, Oberfläche nach Volumen. / Volumen im Maßstab umrechnen, Gewichte und Füllmengen ähnlicher Körper, Fehler „doppelt so viel Fläche“, Prozent, mehrteilige Aufgabe. | 7 → 6 (dir 5, erk 1) | 11 → 6 (mehr 3, eink 1, umk 2) | 6 → 8 (verk 1, begr 1, fehl 1, trans 3, par 1, prüf 1) | 2 | 10 |
| anwendung | Höhe eines Gegenstands aus Stab und Schatten bestimmen. / Daumensprung, Kartenmaßstab, Schatten rückwärts, Höhenunterschied. / Gebäude über den Daumen schätzen, Flussbreite, Mauer und Baum, Spiegel, Schattenspitzen treffen sich, Fehler im Verhältnis. | 10 → 8 (dir 7, erk 1) | 4 → 7 (mehr 1, eink 4, umk 2) | 10 → 8 (verk 2, fehl 1, trans 3, prüf 2) | 2 | 6 |

### funktionen.potenz

Neue Übungen 21, Knobel-Bordkarten 12, überzählig 14.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| werte | f(x) = a · xⁿ für positive x ausrechnen. / Negative Eingaben (Potenz vor Punkt), Vorzeichen begründen, Wertetabellen fortsetzen, Volumen eines Würfels. / Fehler mit dem Minus finden, Brüche und Dezimalzahlen ohne Taschenrechner, Symmetrie nutzen, Faktoren beim Vervielfachen, Bedingung für n, mehrteilige Aufgabe. | 6 → 7 (dir 6, erk 1) | 12 → 11 (mehr 9, eink 1, dar 1) | 7 → 8 (verk 2, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 3 |
| symmetrie | Am Exponenten die Symmetrie ablesen und f(−x) aus f(x) angeben. / Symmetrie am Graphen erkennen, f(−2) aus f(2) ohne a bestimmen, Brückenbogen. / Summen von Potenzen untersuchen, Fehler „ein Wert genügt“ finden, beide Symmetrien zugleich, Bedingung für n. | 7 → 8 (dir 1, erk 7) | 9 → 9 (eink 1, umk 3, dar 5) | 8 → 8 (verk 3, begr 2, fehl 2, par 1) | 2 | 2 |
| verlauf | Den Verlauf von xⁿ und −xⁿ am Exponenten und am Vorzeichen ablesen. / Graphen zuordnen, x⁵ und x³ zwischen 0 und 1 vergleichen, n aus Verlauf und Punkt bestimmen. / Gemeinsame Punkte berechnen, Fehler beim Vorzeichen finden, Wachstum vergleichen, Bedingung (−1 | 1), mehrteilige Aufgabe. | 9 → 11 (dir 1, erk 10) | 10 → 11 (mehr 1, umk 1, dar 9) | 5 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 0 |
| parameter | a aus einem Punkt in y = a · xⁿ bestimmen. / n aus einem Punkt oder zwei Punkten bestimmen, mit a weiterrechnen, Bremsweg und Tabellen. / n und a aus zwei Punkten mit Vorzeichen, Fehler mit (−2)³, unmögliche Punkte begründen, Fallweg und Windrad, mehrteilige Aufgabe. | 6 → 10 (dir 9, erk 1) | 12 → 8 (mehr 3, eink 1, umk 3, dar 1) | 8 → 8 (verk 3, begr 1, fehl 1, trans 2, prüf 1) | 2 | 6 |
| negativ | x⁻ⁿ als Kehrwert von xⁿ ausrechnen. / Brüche einsetzen, Symmetrie und Definitionsmenge, Punkte auf dem Graphen prüfen. / Verhalten für große x und nahe 0, Fehler 4⁻² = −16, Rechteckfläche, Bedingung für a, Beleuchtung bei verdoppeltem Abstand. | 6 → 7 (dir 6, erk 1) | 11 → 10 (mehr 4, umk 2, dar 4) | 9 → 9 (verk 3, begr 2, fehl 1, trans 2, par 1) | 2 | 1 |
| wurzelfunktion | Mit der Umkehrung von x² und x³ aus einem Funktionswert x bestimmen. / Werte von Wurzelfunktionen mit Faktor und Verschiebung, Punkte rückwärts, Gleichungen wie 3x² = 75. / Punkte durch Tauschen übertragen, Lage zu y = x begründen, Wertemenge, Schnittzahl, Fehler „Kehrwert statt Wurzel“, Pendel und Horizont. | 6 → 6 (dir 4, erk 2) | 9 → 9 (mehr 6, umk 2, dar 1) | 10 → 9 (verk 3, begr 3, fehl 1, trans 2) | 2 | 2 |

### gleichungen.potenz

Neue Übungen 36, Knobel-Bordkarten 12, überzählig 30.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| gerade | xⁿ = c mit geradem n und c > 0: beide Lösungen angeben. / Exakte Wurzel-Lösungen, c = 0 und c < 0, c rückwärts aus einer Lösung, Schnitt mit einer Waagrechten. / Fehler bei negativem c und vergessener negativer Lösung finden, Symmetrie begründen, Bedingung für eine Lösung, Flächenfaktor. | 11 → 13 (dir 12, erk 1) | 5 → 7 (mehr 4, umk 1, dar 2) | 8 → 8 (verk 2, begr 1, fehl 3, trans 1, par 1) | 2 | 2 |
| ungerade | xⁿ = c mit ungeradem n: genau eine Lösung, auch für negatives c. / Negative Dezimalzahlen, rückwärts c aus der Lösung, Kühlschrank-Volumen, Klammern umformen. / Fehler ±3 bei x³ finden, „immer genau eine Lösung“ begründen, Bedingung für gleiche Lösungen, Wachstumsfaktor, mehrteilige Aufgabe. | 9 → 4 (dir 3, erk 1) | 8 → 9 (mehr 6, eink 1, umk 1, dar 1) | 7 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 10 |
| anzahl | Am Exponenten und am Vorzeichen von c die Lösungsanzahl angeben. / Mit Graph und Waagrechter begründen, Sonderfall c = 0, Sachfrage „hoch 6 ergibt 0“. / Parameter c für genau zwei Lösungen, Fehler „aus Negativem keine Wurzel“, Folgerungen aus Bildern, Anzahl bei x³ = x. | 6 → 7 (dir 1, erk 6) | 9 → 9 (mehr 5, eink 1, dar 3) | 9 → 9 (verk 1, begr 2, fehl 3, par 3) | 2 | 1 |
| umformen | Bei a · xⁿ = c durch a teilen und die Wurzel ziehen. / Erst eine Zahl abziehen, dann teilen; negative Faktoren; Würfelsumme; c rückwärts. / Klammern, Vorgänge rückwärts machen, ausklammern, Ersetzen bei (x² − 5)², Fehler „minus statt teilen“, Parameter a. | 6 → 5 (dir 4, erk 1) | 8 → 10 (mehr 8, eink 1, umk 1) | 10 → 8 (rück 2, verk 3, fehl 1, trans 1, par 1) | 2 | 6 |
| naeherung | ⁿ√c mit dem Taschenrechner bestimmen und sinnvoll runden. / Erst umformen, negative Lösungen, zwischen ganzen Zahlen eingrenzen, Tank in cm, c rückwärts. / Fehler „nur eine Lösung“, Schätzungen begründen, Bedingung für k, vom gerundeten Wert zurückschließen, Wachstum, mehrteilige Aufgabe. | 6 → 4 (dir 2, erk 2) | 10 → 16 (mehr 14, eink 1, umk 1) | 8 → 8 (rück 1, verk 1, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 6 |
| sachaufgabe | Die Kante eines Würfels aus dem Volumen bestimmen. / Zinsfaktor über zwei Jahre, Platten zählen, Kisten und Quader umschmelzen, Endbetrag mit Zinseszins. / Glasfläche, Kugelmasse, wachsende Kanten, Fehler V : 3, Unmöglichkeit begründen, Quader mit Kanten a, 2a, 4a, mehrteilige Aufgabe. | 6 → 6 (dir 5, erk 1) | 10 → 11 (mehr 3, eink 7, umk 1) | 8 → 8 (verk 1, begr 1, fehl 1, trans 3, par 1, prüf 1) | 2 | 5 |

### zahlen.rationale_exponenten

Neue Übungen 39, Knobel-Bordkarten 12, überzählig 37.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| nte_wurzel | ⁿ√a für Potenzen natürlicher Zahlen angeben. / Dezimalzahlen, Brüche, Potenzen unter der Wurzel, Rechenketten, a rückwärts, Würfel im Alltag. / Produkte unter der Wurzel, verschachtelte Wurzeln, n suchen, Fehler „durch n teilen“, Wachstumsfaktor, mehrteilige Aufgabe. | 6 → 5 (dir 4, erk 1) | 14 → 16 (mehr 14, eink 1, umk 1) | 6 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 2 |
| potenz_wert | a^(1/n) als n-te Wurzel ausrechnen. / a^(m/n) über Wurzel und Potenz, zwei Rechenwege vergleichen, negative Exponenten, Basis rückwärts. / Summen ohne Taschenrechner, Vergleich zweier Potenzen, Formeln aus Biologie und Astronomie, Fehler (16³)/4, Bedingung für n, mehrteilige Aufgabe. | 6 → 4 (dir 2, erk 2) | 9 → 11 (mehr 5, umk 1, dar 5) | 11 → 8 (verk 2, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 9 |
| umwandeln | ⁿ√(x^m) als x^(m/n) schreiben. / Exponenten kürzen, rückwärts in eine Wurzel übersetzen, Kehrwerte als negative Exponenten, Formeln umschreiben. / Mehrere Variablen, verschachtelte Wurzeln, Fehler „Zähler und Nenner vertauscht“, n gesucht, Oberfläche als Potenz von V, mehrteilige Aufgabe. | 6 → 7 (dir 6, erk 1) | 11 → 13 (mehr 10, eink 1, umk 2) | 7 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 2 |
| zusammenfassen | x^(a) · x^(b) zu x^(a + b) zusammenfassen. / Teilen, gleiche Exponenten bei verschiedenen Basen, Wurzeln vorher umschreiben, fehlenden Exponenten ergänzen. / Potenzen von Potenzen, Fehler beim Malnehmen der Exponenten, Aussagen prüfen, Exponent r gesucht, rückwärts ergänzen, mehrteilige Aufgabe. | 6 → 4 (dir 3, erk 1) | 10 → 15 (mehr 13, umk 1, dar 1) | 8 → 8 (rück 1, verk 3, begr 1, fehl 1, par 1, prüf 1) | 2 | 6 |
| gleichung_exp | xⁿ = c oder x^(1/n) = c in einem Schritt lösen. / x^(m/n) = c mit dem Kehrwert lösen, vorher umformen, c rückwärts, Seitenlänge aus Fläche. / Schnittpunkte, zwei Potenzen in einer Gleichung, negative Exponenten, Fehler „Wurzel statt Quadrat“, Lösbarkeit begründen, Formeln rückwärts. | 11 → 8 (dir 7, erk 1) | 6 → 7 (mehr 5, eink 1, umk 1) | 8 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 9 |
| verstehen | Hoch 1/2 als Wurzel und Minus im Exponenten als Kehrwert erkennen. / Negative Bruch-Exponenten ausrechnen, Basis rückwärts, Schreibweisen wechseln, Wachstum in Viertelstunden. / Fehler „hoch 3/2 ist mal 3 : 2“, Allaussagen prüfen, falsche Gleichungen finden, Vergleich mit x, Würfelkante bei doppeltem Volumen, mehrteilige Aufgabe. | 12 → 8 (dir 1, erk 7) | 5 → 6 (mehr 3, eink 1, umk 1, dar 1) | 8 → 8 (verk 1, begr 1, fehl 3, trans 1, par 1, prüf 1) | 2 | 9 |

### trigo.pythagoras

Neue Übungen 35, Knobel-Bordkarten 12, überzählig 57.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| hypotenuse | Aus zwei Katheten die Hypotenuse berechnen. / Runden, andere Bezeichnungen (α = 90°), Sportplatz-Diagonale, gleich lange Katheten, Umweg vergleichen. / Ganzzahlige Katheten zu √13 finden, Verhältnis 3 : 4, Zoll umrechnen, Fehler c = 100 cm, Ungleichung begründen, Bedingung für b, mehrteilige Aufgabe. | 9 → 5 (dir 4, erk 1) | 9 → 8 (mehr 3, eink 1, umk 1, dar 3) | 6 → 8 (rück 1, verk 2, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 11 |
| kathete | Aus Hypotenuse und Kathete die andere Kathete berechnen. / Dezimalzahlen und Runden, Mast mit Seil, Punkt im Koordinatensystem. / Fehler „Längen abziehen“ oder „Quadrate addieren“, Tangente, gleichschenklige Fläche, rutschende Leiter, Bedingung für eine ganzzahlige Hypotenuse. | 10 → 4 (dir 3, erk 1) | 8 → 6 (mehr 4, eink 1, dar 1) | 8 → 8 (verk 1, fehl 3, trans 3, par 1) | 2 | 13 |
| umkehrung | Mit a² + b² = c² für die längste Seite prüfen, ob ein Dreieck rechtwinklig ist. / Den rechten Winkel benennen, Dezimalzahlen, Ecken in der Werkstatt prüfen, fehlende Seite ergänzen. / Stumpfe Winkel erkennen, Begründungen beurteilen, Koordinaten, Fehler mit falscher längster Seite, Knotenschnur, ganzzahlige Dreiecke, mehrteilige Aufgabe. | 6 → 5 (dir 1, erk 4) | 11 → 7 (mehr 3, eink 2, umk 1, dar 1) | 7 → 8 (verk 1, begr 3, fehl 1, trans 1, par 1, prüf 1) | 2 | 12 |
| koordinaten | Mit Δx und Δy den Abstand zweier Punkte berechnen. / Negative Koordinaten, Runden, Entfernungen auf dem Stadtplan, Punkt auf der x-Achse rückwärts. / Fehlende Koordinate aus dem Abstand, Umfänge, Gitterpunkte auf einem Kreis, Fehler „Koordinaten statt Differenzen“. | 6 → 5 (dir 3, erk 2) | 11 → 7 (mehr 5, eink 1, umk 1) | 7 → 8 (rück 2, verk 2, fehl 1, trans 3) | 2 | 9 |
| raum | Raumdiagonale eines Quaders über die Bodendiagonale berechnen. / Runden beim Würfel, Besenstiel im Karton, fehlende Höhe rückwärts, Diagonalen vergleichen, Dreieck im Würfel erkennen. / Pyramidenhöhe, Stab in der Kiste, Kantenmodell, kürzester Weg auf der Oberfläche, Becher, Fehler „Kanten addieren“. | 6 → 8 (dir 7, erk 1) | 11 → 6 (mehr 3, eink 1, umk 1, dar 1) | 7 → 8 (verk 2, begr 2, fehl 1, trans 3) | 2 | 8 |
| anwendung | Bei einer Leiter an der Wand die Höhe berechnen. / Bildschirmdiagonalen, Dreieckshöhen, Rampen, Fläche eines Quadrats aus der Diagonale. / Abkürzung über den Platz, Fähre, Sehne im Kreis, geknickter Baum, Raute, Fehler bei der Höhe im gleichseitigen Dreieck, mehrteilige Aufgabe. | 6 → 5 (dir 4, erk 1) | 12 → 10 (mehr 2, eink 7, umk 1) | 6 → 8 (verk 3, fehl 1, trans 3, prüf 1) | 2 | 4 |

### trigo.rechtwinklig

Neue Übungen 37, Knobel-Bordkarten 12, überzählig 30.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| seiten | Bei γ = 90° Hypotenuse, Gegen- und Ankathete benennen. / Andere Lage des rechten Winkels und andere Buchstaben, Figuren lesen, Seiten an einer Rampe benennen. / Dreiecke in Körpern finden, Rollentausch für α und β, Fehler bei der Hypotenuse, Bedingungen für „a ist Hypotenuse“, mehrteilige Aufgabe. | 6 → 8 (dir 1, erk 7) | 14 → 14 (mehr 10, eink 1, dar 3) | 4 → 8 (verk 2, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 0 |
| verhaeltnisse | sin, cos und tan als Seitenverhältnis bei γ = 90° aufschreiben. / Verhältnisse als Zahl ausrechnen, anderer rechter Winkel, Rampen-Sinus. / Erst eine Seite mit Pythagoras, Winkel ausschließen, Zylinder, sin aus tan, Fehler „Ankathete durch Hypotenuse“, Parameter, mehrteilige Aufgabe. | 6 → 7 (dir 1, erk 6) | 11 → 13 (mehr 10, eink 1, dar 2) | 7 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 1 |
| seite | Mit a = c · sin α die Gegenkathete berechnen. / Kosinus und Tangens wählen, durch sin oder cos teilen, Drachenschnur, Hypotenuse rückwärts. / Fläche aus Winkel, exakte Werte, Mindestlänge einer Leiter, Fehler „sin statt cos“, Bedingung a > c/2, mehrteilige Aufgabe. | 5 → 4 (dir 3, erk 1) | 16 → 14 (mehr 12, eink 1, umk 1) | 5 → 8 (verk 3, fehl 1, trans 2, par 1, prüf 1) | 2 | 7 |
| winkel | Mit tan⁻¹ einen Winkel aus zwei Katheten bestimmen. / sin⁻¹ und cos⁻¹ wählen, besondere Werte, Rampe, Winkel zu sin α = 0,5. / Raumdiagonale im Quader, Diagonalen im Rechteck, Basiswinkel, Graph lesen, Fehler „Katheten vertauscht“, Grenze bei 100 %, mehrteilige Aufgabe. | 6 → 4 (dir 3, erk 1) | 14 → 11 (mehr 8, eink 1, umk 1, dar 1) | 6 → 8 (verk 2, fehl 1, trans 3, par 1, prüf 1) | 2 | 10 |
| beziehungen | Mit sin² α + cos² α = 1 aus sin α den Kosinus berechnen. / tan aus sin und cos, Rampe waagrecht, 90° − α, Werte ohne Taschenrechner. / Exakte Werte im halben gleichseitigen Dreieck, unmögliche Wertepaare, Fehler „sin + cos = 1“, sin = cos, mehrteilige Aufgabe. | 4 → 8 (dir 4, erk 4) | 9 → 9 (mehr 7, eink 1, umk 1) | 11 → 8 (verk 2, begr 1, fehl 2, trans 1, par 1, prüf 1) | 2 | 5 |
| anwendung | Aus einer Steigung in Prozent den Steigungswinkel berechnen. / Höhenwinkel, Schatten, Wanderwege, Rampen mit vorgegebener Steigung, Weglänge rückwärts. / Tiefenwinkel, zwei Höhenwinkel, Drachen über der Hand, Basis aus Winkel, Fehler „sin statt tan“, Prozent und Winkel nicht proportional, Seilbahn. | 6 → 5 (dir 4, erk 1) | 8 → 10 (mehr 1, eink 7, umk 2) | 10 → 8 (verk 2, begr 1, fehl 1, trans 3, prüf 1) | 2 | 7 |

### gleichungen.trig

Neue Übungen 38, Knobel-Bordkarten 12, überzählig 40.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| sinus | Aus einer Lösung von sin x = v die zweite mit x₂ = 180° − x₁ bestimmen. / Ganze Gleichung lösen, auch mit negativem v und Runden, Riesenrad, Wert v aus einer Lösung. / Ohne Taschenrechner, mehrere Umdrehungen, Abstand der Lösungen, Fehler „360° − x₁“, Bedingung für zwei Lösungen, Begründung mit dem Vorzeichen. | 5 → 4 (dir 3, erk 1) | 14 → 10 (mehr 8, eink 1, umk 1) | 5 → 9 (rück 1, verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 9 |
| kosinus | Aus einer Lösung von cos x = v die zweite mit x₂ = 360° − x₁ bestimmen. / Ganze Gleichung lösen, negative Werte, mehrere Umdrehungen, waagrechter Abstand am Riesenrad, Wert v aus einer Lösung. / Ohne Taschenrechner, cos x = cos 40°, Fehler „180° − x₁“, genau eine Lösung bis 180°, Begründung bei cos x = 0, mehrteilige Aufgabe. | 6 → 5 (dir 4, erk 1) | 14 → 11 (mehr 9, eink 1, umk 1) | 5 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 8 |
| tangens | Aus einer Lösung von tan x = v die zweite mit x₂ = x₁ + 180° bestimmen, Steigungswinkel. / Ganze Gleichung mit negativem v lösen, Zeiger auf einer Geraden, Wert v aus einer Lösung. / Ohne Taschenrechner, Volumen über tan, viele Lösungen, Fehler „180° − x₁“, Lösungen für jedes v, Lage der Lösungen begründen. | 9 → 8 (dir 7, erk 1) | 11 → 7 (mehr 5, umk 1, dar 1) | 4 → 8 (verk 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 8 |
| anzahl | Am Wert v ablesen: keine, eine oder zwei Lösungen. / Sonderfälle v = ±1 und |v| > 1, Graph mit Gerade, Wert v zu genau einer Lösung, Gondel zu hoch. / Parameter für keine oder genau eine Lösung, sin x = cos x und Quadrate, Fehler bei ±1 und |v| > 1, mehrteilige Aufgabe. | 6 → 7 (dir 1, erk 6) | 8 → 9 (mehr 6, eink 1, umk 1, dar 1) | 10 → 10 (verk 3, fehl 3, par 3, prüf 1) | 2 | 2 |
| umformen | a · sin x = b durch Teilen auf sin x = v bringen und lösen. / Erst Zahl auf die andere Seite, sin x auf beiden Seiten, Kolben, Zahl in der Gleichung rückwärts. / Durch cos x teilen, Quadrate, Produkt gleich null, Fehler beim Umstellen, wann lösbar, mehrteilige Aufgabe. | 6 → 5 (dir 4, erk 1) | 12 → 14 (mehr 12, eink 1, umk 1) | 6 → 8 (verk 3, fehl 1, trans 2, par 1, prüf 1) | 2 | 3 |
| anwendung | Riesenrad-Höhe auf cos x = v umstellen und lösen. / Hafen, Tageslänge, Pendel, Winkel im Dreieck über die Winkelsumme prüfen, Faktor aus einem Wert bestimmen. / Größter oder stumpfer Winkel, Flächenformel, Drehwinkel-Bereiche, Fehler „nur eine Lösung“, Bedingung an α, mehrteilige Gondel-Aufgabe. | 6 → 4 (dir 3, erk 1) | 10 → 7 (mehr 2, eink 4, umk 1) | 8 → 9 (verk 3, fehl 1, trans 3, par 1, prüf 1) | 2 | 10 |

### trigo.allgemein

Neue Übungen 41, Knobel-Bordkarten 16, überzählig 58.

| Lernkarte | Stufen-Leiter (S1 / S2 / S3) | S1 vorher → nachher | S2 vorher → nachher | S3 vorher → nachher | Knobel | überz. |
|---|---|---|---|---|---|---|
| einheitskreis | Besondere Werte und Punkte am Einheitskreis ablesen, Vorzeichen erkennen. / Werte über Spiegelung (180° − α, 180° + α) bestimmen, Bereiche nach Vorzeichen, stumpfen Winkel zu einem Wert finden. / Aussagen prüfen, sin(α + 90°), sin α = cos α, Fehler beim Kosinus, Bereich für cos α < 0,5, mehrteilige Aufgabe. | 9 → 7 (dir 4, erk 3) | 10 → 9 (mehr 7, umk 1, dar 1) | 5 → 8 (verk 3, begr 2, fehl 1, par 1, prüf 1) | 2 | 5 |
| flaeche | A = 1/2 · a · b · sin γ mit gegebenen Werten ausrechnen, Term aufstellen. / Stumpfe Winkel, Parallelogramm, gleichseitiges Dreieck, Beet zwischen Mauern, sin γ aus der Fläche. / Seite oder Winkel aus der Fläche, größte Fläche, Fehler „1/2 vergessen“, gleiche Fläche bei γ und 180° − γ, mehrteilige Aufgabe. | 7 → 4 (dir 3, erk 1) | 10 → 7 (mehr 5, eink 1, umk 1) | 7 → 8 (rück 3, begr 1, fehl 1, trans 1, par 1, prüf 1) | 2 | 10 |
| sinussatz_seite | Mit a : sin α = b : sin β eine Seite aus zwei Winkeln und einer Seite berechnen. / Erst den dritten Winkel, dann die Seite; längste Seite, Höhe, Beobachter am See, sin α aus Seiten. / Seiten über die Höhe, Grundstück, Fehler „Winkel vertauscht“, wie b von α abhängt, mehrteilige Aufgabe. | 7 → 4 (dir 3, erk 1) | 13 → 10 (mehr 7, eink 2, umk 1) | 7 → 9 (verk 2, fehl 2, trans 3, par 1, prüf 1) | 2 | 8 |
| sinussatz_winkel | Mit sin β = b · sin α : a einen Winkel berechnen, wenn er spitz sein muss. / Zweite Lösung 180° − β prüfen, Segel, Seite aus dem Ergebnis zurückrechnen. / Alle möglichen β, Anzahl der Dreiecke begründen, Fehler „nur eine Lösung“, Bedingung für zwei Dreiecke, mehrteilige Aufgabe. | 10 → 4 (dir 3, erk 1) | 6 → 7 (mehr 5, eink 1, umk 1) | 8 → 8 (verk 3, begr 2, fehl 1, par 1, prüf 1) | 2 | 12 |
| kosinussatz_seite | c² = a² + b² − 2ab · cos γ mit eingeschlossenem Winkel anwenden. / Stumpfe Winkel, Schiffskurs, Pythagoras als Sonderfall, Winkel zu gegebener Seite zurückrechnen. / Ohne Taschenrechner, Raute und Wanderer, c² = a² + b² + ab, Fehler beim Vorzeichen, wie c von γ abhängt, mehrteilige Aufgabe. | 8 → 4 (dir 3, erk 1) | 10 → 8 (mehr 5, eink 2, umk 1) | 6 → 8 (verk 2, begr 1, fehl 1, trans 2, par 1, prüf 1) | 2 | 11 |
| kosinussatz_winkel | cos γ = (a² + b² − c²) : (2ab) aus drei Seiten berechnen. / Gerundete Winkel, Grundstücke, cos γ negativ deuten, Seite aus Winkel zurückrechnen. / Ohne Taschenrechner, Giebel, unmögliche Seiten begründen, Fehler im Nenner, wann γ stumpf ist, mehrteilige Aufgabe. | 7 → 4 (dir 3, erk 1) | 11 → 8 (mehr 5, eink 2, umk 1) | 6 → 8 (verk 2, begr 2, fehl 1, trans 1, par 1, prüf 1) | 2 | 10 |
| satz_waehlen | Am gegebenen Fall (SSS, SWS, WSW, SsW) den passenden Satz erkennen. / Den Satz begründen, Weg rückwärts lesen, Förster-Aufgabe. / Mehrschrittige Wege, Fläche ohne Winkel, nur Winkel gegeben, Fehler „Sinussatz bei SWS“, mehrteilige Zuordnung. | 8 → 8 (dir 1, erk 7) | 8 → 8 (mehr 6, eink 1, umk 1) | 8 → 10 (verk 3, begr 1, fehl 2, trans 3, prüf 1) | 2 | 2 |
| anwendung | Aus einer Planfigur den Winkel beim angepeilten Punkt und den passenden Satz bestimmen. / Flussbreite, Tunnel, Schiffsweg mit Planfigur, Wanderer mit Knick, fehlenden Peilwinkel zurückrechnen. / Turmhöhe aus zwei Peilungen, Grundstück, Segel, Dreiecksungleichung, Fehler „falscher Gegenwinkel“, mehrteilige Vermessung. | 4 → 4 (dir 2, erk 2) | 6 → 8 (mehr 1, eink 1, umk 1, dar 5) | 8 → 9 (verk 3, begr 1, fehl 1, trans 3, prüf 1) | 2 | 0 |

### 3) Anzahl

516 neue Übungen und 181 Knobel-Bordkarten. Je Thema stehen die Zahlen in den Überschriften oben.

### 4) Überzählig

537 Übungen. Die vollständige Liste mit Lernkarte, bisheriger Stufe und Text steht in inhalte/postfach/stufen-kl9-ueberzaehlig.md.

### 5) Quellen der Prüfungsvorbilder

Übernommen wurde nur der Aufgabentyp (kurze mehrteilige Aufgaben mit mehreren Eingabefeldern), nie Wortlaut oder Zahlen:
- ISB Bayern, Bayerischer Mathematik-Test für die Jahrgangsstufe 10 (BMT10): 2009 Gruppe B, 2022 Gruppe A, 2024 A/B, 2025 A/B (isb.bayern.de, Jahrgangsstufenarbeiten Mathematik)
- Mathematik-Olympiade, Schulrunde, Olympiadeklassen 9–10: 56., 58., 60., 61. und 65. Olympiade (Anregung für Knobel-Bordkarten)
- ZUM, Gymnasium Stein: Wiederholungsaufgaben Klasse 9 (unterrichten.zum.de/images/7/76/Whaufgaben9.pdf)

### 6) Beispiel-Bordkarten: trigo.rechtwinklig, Lernkarte anwendung (je Stufe drei, voller Wortlaut)

**Stufe 1**

- *direkt*: Eine Straße hat 12 % Steigung. Wie groß ist der Steigungswinkel (in Grad, auf eine Nachkommastelle)?
  - Lösung: 6,8 °
  - Lösungsweg: tan α = 12/100 = 0,12 ⇒ α ≈ 6,8°.
  - Tipp: Steigung in % ist der Tangens des Steigungswinkels mal 100.
- *erkennen*: Was bedeutet „12 % Steigung“?
  - Auswahl: Der Steigungswinkel ist 12°. | Auf 100 m waagrecht steigt die Straße 12 m. | Die Straße ist 12 % länger. | Auf 100 m Straße steigt sie 100 m.
  - Lösung: Auf 100 m waagrecht steigt die Straße 12 m.
  - Lösungsweg: Steigung in % = Höhe : waagrechte Länge · 100. 12 % heißt tan α = 0,12.
  - Tipp: Prozent bezieht sich auf die waagrechte Strecke.
- *direkt*: Eine Straße steigt auf 100 m waagrechter Strecke um 5 m. Wie groß ist der Steigungswinkel? Runde auf eine Nachkommastelle.
  - Lösung: 2,9 °
  - Lösungsweg: tan α = 5 : 100 = 0,05, α ≈ 2,9°.
  - Tipp: tan α = Höhe : waagrechte Strecke.

**Stufe 2**

- *einkleidung*: Ein Wanderweg ist 300 m lang und steigt gleichmäßig unter dem Winkel 8° an. Wie viele Höhenmeter überwindet er? Runde auf ganze Meter.
  - Lösung: 42 m
  - Lösungsweg: h = 300 · sin 8° ≈ 42 m.
  - Tipp: Die Weglänge ist die Hypotenuse (schräg), die Höhe die Gegenkathete.
- *mehrschritt*: Ein Wanderweg steigt gleichmäßig unter 5° an und überwindet 100 Höhenmeter. Wie lang ist er? Runde auf ganze Meter.
  - Lösung: 1147 m
  - Lösungsweg: Weg = Hypotenuse: sin 5° = 100 : s, s = 100 : sin 5° ≈ 1 147 m.
  - Tipp: Stelle sin α = Höhe : Weg nach dem Weg um.
- *einkleidung*: Aus 64 m Entfernung sieht man die Spitze eines Turms unter dem Höhenwinkel 30° (Augenhöhe vernachlässigt). Wie hoch ist der Turm? Runde auf eine Nachkommastelle.
  - Lösung: 37 m
  - Lösungsweg: tan 30° = h/64 ⇒ h = 64 · tan 30° ≈ 37 m.
  - Tipp: Entfernung ist die Ankathete, Turmhöhe die Gegenkathete.

**Stufe 3**

- *transfer*: Von einem Punkt sieht man die Spitze eines Turms unter 30°. Geht man 40 m näher heran, sieht man sie unter 45°. Wie hoch ist der Turm? Runde auf ganze Meter.
  - Lösung: 55 m
  - Lösungsweg: x = Abstand vom näheren Punkt: h = x · tan 45° und h = (x + 40) · tan 30°. Gleichsetzen: x = 40 · tan 30° : (tan 45° − tan 30°) ≈ 54,6 m, h ≈ 55 m.
  - Tipp: Zwei rechtwinklige Dreiecke mit derselben Höhe h: Stelle für jedes eine Gleichung auf.
- *fehler*: Ein Turm wird aus 50 m Abstand unter 40° Höhenwinkel gesehen. Jemand rechnet h = 50 · sin 40°. Was stimmt?
  - Auswahl: Richtig. | Falsch: 50 m ist die Ankathete, also h = 50 · tan 40°. | Falsch: h = 50 · cos 40°. | Falsch: h = 50 : sin 40°.
  - Lösung: Falsch: 50 m ist die Ankathete, also h = 50 · tan 40°.
  - Lösungsweg: Gegeben sind Ankathete (Abstand) und Winkel, gesucht die Gegenkathete (Höhe): tan α = h : 50.
  - Tipp: Welche Seiten sind bekannt und gesucht?
- *pruefung*: Eine Seilbahn fährt auf einem 1 200 m langen geraden Seil unter 25° nach oben. a) Wie groß ist der Höhenunterschied? b) Wie weit ist es waagrecht? (jeweils ganze Meter)
  - Eingabe: a) □ m; b) □ m
  - Lösung: a) 507 m; b) 1088 m
  - Lösungsweg: a) 1 200 · sin 25° ≈ 507 m. b) 1 200 · cos 25° ≈ 1 088 m.
  - Tipp: Das Seil ist die Hypotenuse.


## 2026-11-17 15:08 – STATUS
trigo.allgemein fertig: 41 neue Übungen, 16 Knobel-Bordkarten, 58 überzählig (ohne Typ, unverändert); inhalt_pruefen OK, 0 gleich gebaut hintereinander, Nachweis OK.

## 2026-11-17 15:03 – STATUS
gleichungen.trig fertig: 38 neue Übungen, 12 Knobel-Bordkarten, 40 überzählig (ohne Typ, unverändert); inhalt_pruefen OK, 0 gleich gebaut hintereinander, Nachweis OK.

## 2026-11-17 14:58 – STATUS
trigo.rechtwinklig fertig: 37 neue Übungen, 12 Knobel-Bordkarten, 30 überzählig (ohne Typ, unverändert); inhalt_pruefen OK, 0 gleich gebaut hintereinander, Nachweis OK.

## 2026-11-17 14:55 – STATUS
trigo.pythagoras fertig: 35 neue Übungen, 12 Knobel-Bordkarten, 57 überzählig (ohne Typ; viele gleich gebaute Vorlagen, z. B. 10× Kathete aus Hypotenuse). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:51 – STATUS
zahlen.rationale_exponenten fertig: 39 neue Übungen, 12 Knobel-Bordkarten, 37 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:48 – STATUS
gleichungen.potenz fertig: 36 neue Übungen, 12 Knobel-Bordkarten, 30 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:46 – STATUS
funktionen.potenz fertig: 21 neue Übungen, 12 Knobel-Bordkarten, 14 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:43 – STATUS
abbildungen.aehnlichkeit fertig: 29 neue Übungen, 12 Knobel-Bordkarten, 52 überzählig (ohne Typ; viele Wiederholungen derselben Vorlage). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:40 – STATUS
stochastik.verknuepft fertig: 28 neue Übungen, 12 Knobel-Bordkarten, 17 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:37 – STATUS
gleichungen.lgs3 fertig: 42 neue Übungen, 11 Knobel-Bordkarten (stufenform nur eine: Stufenform ist reines Rückwärtseinsetzen, eine zweite Idee wäre nur eine Wiederholung), 21 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:33 – STATUS
gleichungen.quadratisch fertig: 41 neue Übungen, 16 Knobel-Bordkarten, 34 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:29 – STATUS
funktionen.quadratisch fertig: 45 neue Übungen, 16 Knobel-Bordkarten, 23 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:25 – STATUS
zahlen.reell fertig: 37 neue Übungen, 14 Knobel-Bordkarten, 20 umgestuft, 63 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:21 – STATUS
zahlen.wurzeln_basis fertig: 47 neue Übungen, 12 Knobel-Bordkarten, 16 umgestuft, 61 überzählig (ohne Typ). inhalt_pruefen OK, 0 Gruppen „gleich gebaut hintereinander“, Nachweis OK.

## 2026-11-17 14:21 – FRAGE
Überzählige Übungen (dieselbe Vorlage mehrfach): Das Prüfskript erlaubt je Stufe und Typ höchstens 2 Aufgaben mit gleichem Satzbau. Gibt man allen alten Übungen einen Typ, schlagen die Wiederholungen der alten Vorlagen fehl. Meine Annahme, mit der ich weiterarbeite: Ab der dritten Übung gleicher Vorlage (und auf Stufe 3 ab der vierten desselben Typs) bleibt die Übung Zeichen für Zeichen unverändert und OHNE g in der Datei. Sie wird unter „überzählig“ gemeldet (Liste: /werk-Bericht am Ende), damit der Haupt-Chat sie sperrt. Folge: Lernkarten mit überzähligen Übungen sind im Prüfskript nicht vollständig typisiert, deshalb prüft es dort die strengen Typregeln nicht. Ich prüfe sie mit inhalte/generatoren/_stufen_kl9.py (nachweis) auf den Übungen mit Typ: S1 ≥ 4 mit ≥ 2 Typen, S2 ≥ 6 mit ≥ 3, S3 ≥ 8 mit ≥ 4 und höchstens 3 je Typ, höchstens 2 gleich gebaute je Typ, nie zwei gleiche Typen hintereinander. Die Reihenfolge innerhalb einer Lernkarte mischt die Stufen; das erlaubt erst, dass nie zwei gleiche Typen hintereinander stehen.
