# Postfach luecken-kl10 (Achtzehnte Runde, Teil B, Klasse 10)

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
   - gleichungen.trig nach Klasse 10 holen: **nicht Teil dieses Auftrags** (Klassen-Zuordnung eines ganzen Themas; Entscheidung D-Runde/Sebastian). Bogenmaß-Lösungen dort einzubauen widerspräche der heutigen Zuordnung Kl. 9 („Bogenmaß gehört nicht zur 9. Klasse“).
   - Graph aus dem Einheitskreis herleiten: **offen geblieben** – braucht eine Zeichnung mit Einheitskreis und Graph nebeneinander (App-Wunsch, siehe unten).
5. **Rotationskörper, schiefe Prismen, Schrägbilder/Netze** (mittel) – **teilweise erledigt.**
   - Zylinder/Kegel/Kugel als Rotationskörper: **erledigt (raum.schraegbilder, Karten `rotation` und `axialschnitt`)** – das Thema steht seit D2 in der Themenliste bei Klasse 10. Übernehmen/Verschieben ist **nicht Teil dieses Auftrags**.
   - Volumen schiefer Prismen (G · h, Cavalieri): **offen** → `verstehen` in raum.pyramide_kegel_kugel um Schritt und Übungen erweitern.
   - Schrägbilder/Netze von Pyramide und Kegel: Pyramide **erledigt** (figur, Runde 3); Kegel **offen (App)** – kein Bildtyp für Ellipsen/Körper.
6. **Prismen und Zylinder (Kl. 8) als Voraussetzung** (hoch) – **nicht Teil dieses Auftrags** (neues Thema messen.prisma_zylinder, baut Teil A).
7. **Baumdiagramme in stochastik.mehrstufig** (mittel) – **erledigt (stochastik.mehrstufig, Runde 3):** alle sieben Lernkarten haben ein Kartenbild vom Typ `baum` (Pfad-Tabellen entfallen), Bäume auch in Aufgaben (Pfadregel Stufe 1, ohne Zurücklegen, Baum ergänzen). Weitere vorhandene Aufgaben nachträglich zu bebildern hieße, freigegebene Aufgaben zu ändern – nicht Teil dieses Auftrags.

Nebenbefund (nur melden): In inhalte/themen/raum.schraegbilder.json und stochastik.simulation.json steht noch `"klasse": {"gym_by": 8, …}`, in der Themenliste (nach D2) `gym_by: 10`. Wer gilt beim Einspielen?
