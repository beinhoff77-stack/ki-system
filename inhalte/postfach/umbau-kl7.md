# Postfach umbau-kl7 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Klasse 7)

Neueste Meldung oben.

Hinweis zum Start: Laut AUFTRAEGE.md soll U7 erst nach dem Test mit den Kindern starten. Sebastian hat den Auftrag am 16.11. um 02:52 ausdrücklich erteilt – als Freigabe gewertet.
Umsetzung wie U8: Abschnitt UMBAU im Generator, eingesetzt nach dem Erzeugen der Aufgaben (Helfer inhalte/generatoren/_umbau_kl7.py, gleicher Aufbau wie _umbau_kl8.py).
KLAR aus Runde 7 bleibt stehen (die Generatoren nutzen die Beispieltexte beim Vermeiden von Dopplungen). Die alte „probe“ entfällt; Kontrollen stehen wo nötig als Schritt.
Prüfung je Thema: Aufgaben Feld für Feld gegen `git show origin/lernen-app:inhalte/themen/<thema>.json`, lernziel/titel unverändert, inhalt_pruefen ohne Fehler und ohne Hinweise (Ausnahmen begründet).

## Status

## 2026-11-16 05:00 – STATUS
daten.boxplot umgebaut (6 Karten): Zahlenstrahl mit Punkten und Bereich (neu seit 16.11.) für Median (Werte → mittlerer Bereich 5–7 → Median 6), Ausreißer (Mittelwert 30 und Median 12 als Punkte), Quartile (Median → untere/obere Hälfte als Bereich → Boxplot). Säulen (Kennwerte), Boxplot (ablesen), zwei Boxplots (vergleichen). Ohne fehler_bild: alle sechs Fehler sind Lese-/Rechenfehler, die im Bild der Karte schon sichtbar sind.
Aufgaben: 144, 0 Unterschiede. inhalt_pruefen: 0 Fehler, 0 Hinweise.

## 2026-11-16 04:45 – STATUS
geometrie.kreis umgebaut (6 Karten): Thaleskreis (35° → rechter Winkel bei C → β = 55°), Koordinatenbild zur Umkehrung (A, B, C → M → Kreis mit r = 4), Beweisfigur (Radius MC → Winkel α, β bei C), Kreis und Gerade mit Abstand d (→ Schnittpunkte), Tangentenfigur (50° → rechte Winkel → 130°), Umkreis über die Mittelsenkrechten von [AB] und [AC] (→ M(3 | 1) → Kreis). fehler_bild bei thales ([AB] kein Durchmesser), lage (d = r berührt nur).
Aufgaben: 144, 0 Unterschiede. inhalt_pruefen: 0 Fehler, 0 Hinweise.

## 2026-11-16 04:25 – STATUS
geometrie.konstruktion umgebaut (7 Karten): Parallelenbild mit nacheinander markierten Stufen-/Wechselwinkeln, Giebel (γ gesucht → 55° → Begründung mit Parallele durch C), gleichschenkliger Giebel (? → 70°), Holzleisten für SWS (zwei Seiten → Winkel → dritte Seite), Zirkelbögen 3 cm/4 cm um die Enden von c = 8 cm, Parallelogramm mit nacheinander eingetragenen Winkeln, Tabelle Satz/Kehrsatz/Gegenbeispiel. fehler_bild bei parallelen (nicht parallele Geraden, 55° ≠ 65°), kongruenzsatz (zwei gleichseitige Dreiecke verschiedener Größe), konstruierbar (Bögen 3 cm/5 cm berühren sich nur).
Karte vierecke: Merksatz nennt Parallelogramm und Drachenviereck; das gleichschenklige Trapez steht wegen der 25-Wörter-Grenze nicht mehr im Merksatz (Aufgaben dazu gibt es weiter; ggf. eigene Karte erwägen).
Helfer _umbau_kl7.py ergänzt: Ein Schrittbild mit „typ“ gilt als vollständiger Ersatz – Felder des vorigen Zustands, die fehlen, werden auf null gesetzt (sonst blieben in der App z. B. Winkel zu nicht mehr vorhandenen Punkten stehen). Die drei schon fertigen Themen sind davon nicht betroffen (JSON unverändert).
Aufgaben: 168, 0 Unterschiede. inhalt_pruefen: 0 Fehler, 0 Hinweise.

## 2026-11-16 04:00 – STATUS
abbildungen.kongruenz umgebaut (7 Karten): Koordinatenbilder mit Schritt-Zuständen (Abstand zur Achse → Bildpunkt; Weg P→Z → doppelter Weg; Verschiebungsweg mit Pfeil v; Weg O→P und mitgedrehter Weg), Rechteck mit nacheinander eingezeichneten Symmetrieachsen, Dreiecke um eine Parkett-Ecke (1 → 6), zwei Spiegelungen an parallelen Achsen (Dreieck → Bild 1 → Bild 2). fehler_bild bei achsenspiegelung (Spiegeln an der x-Achse), drehung (180° statt 90°), symmetrie (Diagonale ist keine Achse).
Aufgaben: 168, 0 Unterschiede. inhalt_pruefen: 0 Fehler, 0 Hinweise.

## 2026-11-16 03:45 – STATUS
terme.aufstellen umgebaut (6 Karten), durchgehend Fahrradverleih. Bilder: sich füllende Tabellen (Termart, Wertetabelle, Übersetzung, Preistafel, Deutung), Streichholz-Figuren 1 → 2 → 3 als Bildfolge. fehler_bild bei struktur (Gegenbeispiel 3x + 4 als Tabelle) und uebersetzen (falsch/richtig). Beispiel der Karte termwert jetzt in der Verleih-Situation (3x + 5 für 1, 2, 4 Stunden); die Klammerregel für negative Zahlen steht im Merksatz.
Aufgaben: 144, 0 Unterschiede. inhalt_pruefen: 0 Fehler, 0 Hinweise.

## 2026-11-16 03:30 – STATUS
bruch.prozent_grundwert umgebaut (7 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler, regel (erster Satz = Kurz gesagt). Bilder: Prozentstreifen (figur) mit Zuständen 100 % → 115 % → 85 %, Bruchstreifen in Zehnteln (Rabatt), Säulen, Tabelle (Mehrwertsteuer). fehler_bild bei vermehrt und vermindert; bei den übrigen ist der Fehler ein Rechen- oder Begründungsfehler ohne sinnvolles eigenes Bild.
Aufgaben: 168, 0 Unterschiede. inhalt_pruefen: 0 Fehler, 0 Hinweise.
