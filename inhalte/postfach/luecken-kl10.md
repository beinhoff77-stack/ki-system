# Postfach luecken-kl10 (Achtzehnte Runde, Teil B, Klasse 10)

## 2026-11-17 15:20 – FERTIG: Abschlussbericht luecken-kl10
Zweig `luecken-kl10` (von `lernen-app`, 4 Themen-Commits). Kein Merge, keine Datenbank, kein App-Code, keine Tests.
Werkzeug: `inhalte/generatoren/_luecken_kl10.py` (Einfügen/Erweitern am Ende jedes Generators, eigener Zufallsstart; Nachweis:
`python3 -I -B inhalte/generatoren/_luecken_kl10.py <thema>` – alte Aufgaben unverändert an gleicher Stelle, neue nur hinten und nur zu neuen/erweiterten Karten,
Abschnitte/Teilfähigkeiten/Bewertung nur um neue Lernziele ergänzt, alte „offen“-Einträge unverändert). Alle vier Themen: `inhalt_pruefen` OK ohne Warnungen, NACHWEIS OK.
Jede neue Aufgabe habe ich gelesen und nachgerechnet; Lösungen rechnet der Generator, Punkte in Zeichnungen per Skript gegen die Graphen geprüft.

**Neue Lernkarten (alle Pflicht, je 28 Aufgaben: Übung 4/6/8, Test 1, Korrektur 3, Sicherung 6)**
| Thema | Lernkarte | wohin | Lehrplan-Bezug | Prüfungsvorbilder (Typ/Niveau, eigene Zahlen) / Knobelaufgabe |
|---|---|---|---|---|
| funktionen.trig | `verschiebung_x` „Verschiebung in x-Richtung“ | nach `parameter` (Abschnitt „Parameter“) | M10 3: Wirkung von a, b, c, d bei a · sin(b · (x + c)) + d; Term aus Graph | Term aus Hoch- und Tiefpunkt (Abitur Bayern Teil A, Typ wie in schwer-kl10.md notiert), Gezeiten-Modell mit Hochwasser-Uhrzeit (Grundwissen M10 Hildegardis-Gymnasium Kempten); Knobel: c mit sin(x + c) = −sin x |
| funktionen.exponential_log | `linear_oder_exponentiell` „Linear oder exponentiell?“ | nach `faktor` (Abschnitt „Exponentialfunktion“) | M10 1: exponentielles von linearem Wachstum begründet abgrenzen, Modell kritisch prüfen, Grenzen benennen | Messwert-Tabelle prüfen und Modell fortsetzen (BMT 10, ISB), zwei Modelle vergleichen mit beiden Graphen (Grundwissen M10 Gymnasium Eckental); Knobel: f(0) = 4, f(2) = 36 – f(1) linear und exponentiell |
| stochastik.mehrstufig | `pi_schaetzen` „π schätzen: Zufall oder Streifen?“ | nach `simulation` (Abschnitt „Simulation und Verstehen“) | M10 2: π zufallsbasiert nähern (Tabellenkalkulation, bedingte Anweisung) und mit nicht zufallsbasiertem Verfahren vergleichen, z. B. Streifenmethode | π mit Rechtecken von oben/unten eingrenzen, Monte-Carlo beschreiben und zweite Methode angeben (Grundwissen M10.5 Werdenfels-Gymnasium); Knobel: Streifenzahl für Abstand ≤ 0,1, „welcher Schätzwert ist bei 100 Punkten unmöglich?“ |
Name `pi_schaetzen` statt `monte_carlo`: Im selben Block (Darwin) gibt es schon stochastik.simulation/`monte_carlo` (Flächen schätzen); die neue Karte ergänzt π und den Vergleich, statt sie zu wiederholen.

**Erweiterte Karten (nur Übungen dazu; die alten Aufgaben unverändert)**
| Thema | Karte | geändert | neue Übungen (Stufe 1/2/3) |
|---|---|---|---|
| funktionen.trig | `zuordnen` | Merksatz um „Start verschoben? Dann c ablesen.“ ergänzt (jetzt 25 Wörter); kein neuer Schritt, weil die Karte schon 5 Schritte hat – die Erklärung zu c steht in `verschiebung_x` direkt davor | 6 (1/2/3), davon 3 mit Graph; Prüfungsvorbild: a, b, c, d aus dem Graphen mit markiertem Hochpunkt |
| funktionen.trig | `periode` | 5. Schritt „Volle Runden zählen nicht: 9π/4 wirkt wie π/4, −π/2 wie 3π/2.“ mit Einheitskreis | 6 (1/2/3): sin(5π/2), cos(−π/3), −3π/4 → 5π/4, sin(−17π/6), cos(100π) + sin(−101π/2), Aussagen zur Periodizität |
| raum.pyramide_kegel_kugel | `verstehen` | 5. Schritt „Schiefes Prisma: … also V = G · h.“ mit Zeichnung (gerades und schiefes Prisma, gleich breit und hoch, Schichten) | 6 (1/2/3); Prüfungsvorbild: Höhe aus Seitenkante und Neigungswinkel (M10 5 „Längen und Winkel“); Fehler „Kante statt Höhe“; schräger Münzstapel |
In jedem Thema ein neuer Eintrag unter „offen“ (alte Einträge unverändert). In funktionen.trig ist der alte Eintrag „Verschiebung in x-Richtung: … keine eigene Lernkarte“ damit überholt – der neue Eintrag sagt das; gelöscht habe ich ihn nicht.

**Offen geblieben (und warum)**
- Graph der Sinusfunktion aus dem Einheitskreis herleiten (M10 3): braucht Einheitskreis und Graph nebeneinander mit Verbindungslinien. **App-Wunsch:** Zeichnung „Einheitskreis + Graph“ (z. B. koordinaten mit zweitem Teilbild). Bis dahin nur in Worten.
- gleichungen.trig nach Klasse 10 holen und um Bogenmaß-Lösungen erweitern: Klassen-Zuordnung eines ganzen Themas, nicht Teil dieses Auftrags (Entscheidung Haupt-Chat/der Nutzer). Winkel zu gegebenen Werten im Bogenmaß üben `werte`/`eigenschaften` in funktionen.trig schon.
- Karte `monte_carlo` (stochastik.simulation) und Karten `rotation`/`axialschnitt` (raum.schraegbilder) verschieben: nicht Teil dieses Auftrags; seit D2 stehen beide Themen ohnehin in Klasse 10 (Themenliste). **Bitte klären:** In beiden Themendateien steht noch `"klasse": {"gym_by": 8, …}`.
- Schrägbild und Netz des Kegels (M10 5): **App** – kein Bildtyp für Körper/Ellipsen.
- Baumdiagramme in vorhandenen Aufgaben von stochastik.mehrstufig nachrüsten: würde freigegebene Aufgaben ändern; die Lernkarten haben die Bäume seit Runde 3.
- messen.prisma_zylinder: Teil A.
- Selbst simulieren (Zufallspunkte erzeugen) kann das Kind in der App weiter nicht (**App-Wunsch** Simulationsknopf, steht schon auf der Liste).

**Quellen** (Typ und Niveau als Vorbild, keine Aufgabe übernommen)
- LehrplanPLUS Gymnasium Mathematik 10, M10 1/2/3/5: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/10/mathematik (am 17.11. gelesen)
- Bayerischer Mathematik-Test Jgst. 10 (ISB), z. B. 2016 Gruppe A (Tabelle mit Messwerten): https://www.isb.bayern.de/fileadmin/user_upload/Gymnasium/Leistungserhebungen/Jahrgangsstufenarbeiten/Mathematik/2016/bmt10_2016_aufgaben_gruppe_a.pdf
- Grundwissen M10 G9, Gymnasium Eckental (lineares/exponentielles Wachstum, Tabellen entscheiden): https://gymnasium-eckental.de/wp-content/uploads/2025/08/GW10.pdf
- Grundwissen M10 G9, Werdenfels-Gymnasium (M10.5 „Näherungsweise Bestimmung von π“): https://www.werdenfels-gymnasium.de/images/Unterricht/Mathematik/M10%20-%20Ruckseiten%20-%20G9.pdf
- Grundwissen M10 G9, Hildegardis-Gymnasium Kempten (allgemeine Sinusfunktion a · sin(b(x + c)) + d, Lösungen in [0; 2π[): https://hildegardis-gymnasium.de/wp-content/uploads/2026/07/10.-Klasse-Grundwissen-Mathe.pdf
- Abitur Bayern Prüfungsteil A (Term einer trigonometrischen Funktion aus Eigenschaften): Typ wie in inhalte/postfach/schwer-kl10.md notiert, hier nicht erneut nachgelesen.

## 2026-11-17 15:00 – STATUS: raum.pyramide_kegel_kugel fertig
- `verstehen` erweitert: 5. Schritt „Schiefes Prisma: wie ein schräg geschobener Stapel gleicher Platten, also V = G · h.“ mit Zeichnung (gerades und schiefes Prisma von der Seite, beide 2 breit und 3 hoch, Schichten gestrichelt, Höhe mit rechtem Winkel), 6 Übungen (1/2/3), u. a. Höhe aus Kante und Neigungswinkel, typischer Fehler „Kante statt Höhe“, schräger Münzstapel.
- `inhalt_pruefen`: OK, keine Warnungen. Nachweis: alle 238 alten Aufgaben unverändert, NACHWEIS OK.

## 2026-11-17 14:40 – STATUS: stochastik.mehrstufig fertig
- Neue Lernkarte `pi_schaetzen` („π schätzen: Zufall oder Streifen?“, Pflicht) nach `simulation`, Abschnitt „Simulation und Verstehen“: Viertelkreis als gefüllte Fläche, 40 Zufallspunkte (31 Treffer ⇒ π ≈ 3,1), Streifenmethode mit 4 Rechtecken über/unter dem Bogen (3,5 und 2,5). 28 Aufgaben (Übung 4/6/8, Test 1, Korrektur 3, Sicherung 6), u. a. Tabellenkalkulation mit WENN(x² + y² ≤ 1; 1; 0), Punkt im Viertelkreis per Pythagoras, Ober-/Untersumme mit 2, 4, 5 Streifen, Vergleich der Verfahren.
- `inhalt_pruefen`: OK, keine Warnungen. Nachweis: alle 238 alten Aufgaben unverändert, NACHWEIS OK.

## 2026-11-17 14:10 – STATUS: funktionen.exponential_log fertig
- Neue Lernkarte `linear_oder_exponentiell` („Linear oder exponentiell?“, Pflicht) nach `faktor`, Abschnitt „Exponentialfunktion“: Wertetabelle als `tabelle` (Differenzen/Quotienten je Schritt), beide Graphen in einem Koordinatensystem, Modellgrenze (10 Wochen Verdopplung). 28 Aufgaben (Übung 4/6/8, Test 1, Korrektur 3, Sicherung 6).
- `inhalt_pruefen`: OK, keine Warnungen. Nachweis: alle 204 alten Aufgaben unverändert, NACHWEIS OK.

## 2026-11-17 13:40 – STATUS: funktionen.trig fertig
- Neue Lernkarte `verschiebung_x` („Verschiebung in x-Richtung“, Pflicht) nach `parameter`, im Abschnitt „Parameter“: 28 Aufgaben (Übung 4/6/8, Test 1, Korrektur 3, Sicherung 6).
- `zuordnen` erweitert: 6 Übungen mit c (Stufe 1/2/3: 1/2/3), Merksatz um „Start verschoben? Dann c ablesen.“ ergänzt (25 Wörter). Kein neuer Schritt, weil die Karte schon 5 Schritte hat; die Erklärung zu c steht in `verschiebung_x` direkt davor.
- `periode` erweitert: 5. Schritt „Volle Runden zählen nicht: 9π/4 wirkt wie π/4, −π/2 wie 3π/2.“ mit Einheitskreis-Bild, 6 Übungen (1/2/3).
- `inhalt_pruefen`: OK, keine Warnungen. Nachweis (`_luecken_kl10.py funktionen.trig`): alle 294 alten Aufgaben unverändert an gleicher Stelle, NACHWEIS OK.

## 2026-11-17 13:00 – STATUS: Bestandsaufnahme (Liste „luecken“ in inhalte/pruefung/aufbau/klasse10.json vom 14.11.)
Geprüft gegen den Stand von `lernen-app` am 17.11. (inhalte/themen, inhalte/themenliste.json) und gegen LehrplanPLUS M10 (Wortlaut auf lehrplanplus.bayern.de am 17.11. nachgelesen).

1. **Parameter c bei a · sin(b · (x + c)) + d** (hoch) – **offen.** funktionen.trig hat c nur in einzelnen Zuordnungs-Übungen, keine Lernkarte („offen“ sagt ausdrücklich „keine eigene Lernkarte“). → neue Karte `verschiebung_x` nach `parameter`, `zuordnen` um c erweitern.
2. **Linear oder exponentiell begründet abgrenzen, Modellgrenzen** (hoch) – **offen.** funktionen.exponential_log hat nur einzelne Tabellen-Übungen „linear oder exponentiell?“ in `modell`, keine Erklärung. → neue Karte `linear_oder_exponentiell` nach `faktor`.
3. **Monte-Carlo-Methode für π, Vergleich mit nicht zufallsbasiertem Verfahren** (mittel) – **teilweise erledigt.** Seit D2 steht stochastik.simulation in der Themenliste bei Klasse 10 (gym_by 10); dessen Karte `monte_carlo` erklärt Flächen schätzen mit Zufallspunkten, π-Schätzung gibt es dort nur als Stufe-3-Übungen. Offen: π als Ziel und der Vergleich mit der Streifenmethode (LehrplanPLUS M10 2 nennt sie als Beispiel). → neue Karte in stochastik.mehrstufig nach `simulation` (Name `pi_schaetzen`, damit es nicht wie eine zweite `monte_carlo`-Karte im selben Block Darwin aussieht).
   **Nicht Teil dieses Auftrags:** die Karte `monte_carlo` aus stochastik.simulation verschieben (nur melden; nach D2 auch nicht mehr nötig, weil das Thema schon Klasse 10 ist).
4. **Beliebige Winkel, Graph aus dem Einheitskreis, Winkel zu gegebenen Werten im Bogenmaß** (mittel) – **teilweise offen.**
   - Winkel über 2π / negative Winkel: nur einzelne Übungen (`werte`: sin(−π/2), cos(7π/3)), keine Erklärung → **offen**, `periode` um Schritt und Übungen erweitern.
   - Winkel zu gegebenen sin-/cos-Werten im Bogenmaß: **erledigt (als Übungen)** in funktionen.trig `werte` und `eigenschaften` (z. B. cos x = −0,5 in [0; π], sin x = 0,5 in [0; 2π[, cos x = 0,5 zwei Lösungen; Zehnte und Fünfzehnte Runde).
   - gleichungen.trig nach Klasse 10 holen: **nicht Teil dieses Auftrags** (Klassen-Zuordnung eines ganzen Themas; Entscheidung D-Runde/der Nutzer). Bogenmaß-Lösungen dort einzubauen widerspräche der heutigen Zuordnung Kl. 9 („Bogenmaß gehört nicht zur 9. Klasse“).
   - Graph aus dem Einheitskreis herleiten: **offen geblieben** – braucht eine Zeichnung mit Einheitskreis und Graph nebeneinander (App-Wunsch, siehe unten).
5. **Rotationskörper, schiefe Prismen, Schrägbilder/Netze** (mittel) – **teilweise erledigt.**
   - Zylinder/Kegel/Kugel als Rotationskörper: **erledigt (raum.schraegbilder, Karten `rotation` und `axialschnitt`)** – das Thema steht seit D2 in der Themenliste bei Klasse 10. Übernehmen/Verschieben ist **nicht Teil dieses Auftrags**.
   - Volumen schiefer Prismen (G · h, Cavalieri): **offen** → `verstehen` in raum.pyramide_kegel_kugel um Schritt und Übungen erweitern.
   - Schrägbilder/Netze von Pyramide und Kegel: Pyramide **erledigt** (figur, Runde 3); Kegel **offen (App)** – kein Bildtyp für Ellipsen/Körper.
6. **Prismen und Zylinder (Kl. 8) als Voraussetzung** (hoch) – **nicht Teil dieses Auftrags** (neues Thema messen.prisma_zylinder, baut Teil A).
7. **Baumdiagramme in stochastik.mehrstufig** (mittel) – **erledigt (stochastik.mehrstufig, Runde 3):** alle fünf Lernkarten der Abschnitte „Pfadregeln“ und „Strategien“ (dazu `verstehen`) haben ein Kartenbild vom Typ `baum` (Pfad-Tabellen entfallen; `simulation` zeigt passend ein Säulendiagramm), Bäume auch in Aufgaben (Pfadregel Stufe 1, ohne Zurücklegen, Baum ergänzen). Weitere vorhandene Aufgaben nachträglich zu bebildern hieße, freigegebene Aufgaben zu ändern – nicht Teil dieses Auftrags.

Nebenbefund (nur melden): In inhalte/themen/raum.schraegbilder.json und stochastik.simulation.json steht noch `"klasse": {"gym_by": 8, …}`, in der Themenliste (nach D2) `gym_by: 10`. Wer gilt beim Einspielen?
