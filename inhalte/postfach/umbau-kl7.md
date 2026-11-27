# Postfach umbau-kl7 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Klasse 7)

Neueste Meldung oben.

Hinweis zum Start: Laut AUFTRAEGE.md soll U7 erst nach dem Test mit den Kindern starten. Der Nutzer hat den Auftrag am 16.11. um 02:52 ausdrücklich erteilt – als Freigabe gewertet.
Umsetzung wie U8: Abschnitt UMBAU im Generator, eingesetzt nach dem Erzeugen der Aufgaben (Helfer inhalte/generatoren/_umbau_kl7.py, gleicher Aufbau wie _umbau_kl8.py).
KLAR aus Runde 7 bleibt stehen (die Generatoren nutzen die Beispieltexte beim Vermeiden von Dopplungen). Die alte „probe“ entfällt; Kontrollen stehen wo nötig als Schritt.
Prüfung je Thema: Aufgaben Feld für Feld gegen `git show origin/lernen-app:inhalte/themen/<thema>.json`, lernziel/titel unverändert, inhalt_pruefen ohne Fehler und ohne Hinweise (Ausnahmen begründet).

## Status

## 2026-11-16 06:00 – FERTIG (Abschlussbericht U7)
Alle 8 Themen auf dem Zweig umbau-kl7 umgebaut, je ein Commit:

| Thema | Karten | Aufgaben | Unterschiede | inhalt_pruefen |
|---|---|---|---|---|
| bruch.prozent_grundwert | 7 | 168 | 0 | 0 Fehler, 0 Hinweise |
| terme.aufstellen | 6 | 144 | 0 | 0 / 0 |
| abbildungen.kongruenz | 7 | 168 | 0 | 0 / 0 |
| geometrie.konstruktion | 7 | 168 | 0 | 0 / 0 |
| geometrie.kreis | 6 | 144 | 0 | 0 / 0 |
| daten.boxplot | 6 | 144 | 0 | 0 / 0 |
| gleichungen.linear | 6 | 162 | 0 | 0 / 0 |
| terme.umformen (Überlagerung) | 8 | – (nur in der Datenbank) | – | 0 / 0 (Ersatzprüfung, s. u.) |

Aufgaben-Vergleich: jedes Feld gegen `git show origin/lernen-app:inhalte/themen/<thema>.json`; titel und lernziel unverändert. Alle Beispielzahlen nachgerechnet (Terme zusätzlich durch Einsetzen von x = −5 … 5 geprüft).
Nur Zeichnungsarten aus README benutzt (figur, koordinaten, tabelle, saeulen, boxplot, zahlenstrahl mit punkte/bereich, bruchstreifen). Keine Datenbank, keine Serverfunktionen, kein App-Code, keine Tests, kein Merge.

offen:
- terme.umformen: Die Überlagerung enthält kein Feld „probe“ mehr (wie bei den Generator-Themen). Beim Einspielen bitte die alte probe der Karten entfernen, sonst bleibt sie neben dem neuen Muster stehen.
- terme.umformen: Prüfung ersatzweise – die acht Karten wurden in eine Kopie von gleichungen.linear.json eingesetzt und mit inhalt_pruefen geprüft (0 Fehler, 0 Hinweise). Die echte Prüfung geht erst nach dem Einspielen mit den Aufgaben aus der Datenbank (Dopplungen Beispiel/Aufgabe nicht geprüft).
- terme.umformen: Beispiele aus quelle.md beibehalten; Einstiege gekürzt. minusklammer erzählt jetzt Konto/Rechnung mit Rabatt statt Hefte-Rückgabe (die alte Geschichte ging rechnerisch nicht ganz auf). produkte: Beet 3a · 2a als Bild, dann 3a · (−2a) aus der Quelle.
- geometrie.konstruktion/vierecke: gleichschenkliges Trapez nicht mehr im Merksatz (25-Wörter-Grenze).
- fehler_bild fehlt bewusst bei Karten, deren Fehler ein Rechen- oder Lesefehler ohne eigenes Bild ist (u. a. daten.boxplot, terme.umformen/produkte, gleichungen.linear klammern/probe/sonderfaelle/sach).
- Die Kurven in koordinaten (Tarif-Geraden) habe ich nicht gerendert sehen können (eigenes Prüfbild zeichnet nur Punkte/Strecken); Format laut README.

## 2026-11-16 05:50 – STATUS
terme.umformen (ohne Generator): Überlagerung inhalte/klar/terme.umformen.json neu – 8 Karten mit bild, Schritten als {text, bild} und fehler_bild (außer produkte). Bilder: sich füllende Tabellen (Hefte/Stifte sortieren, Vorzeichenwechsel, Malkreuz-Tabellen für Ausmultiplizieren, Summe mal Summe, Ausklammern, binomische Formeln, Einsetztabelle für Äquivalenz), Beet 3a × 2a mit 6 Feldern a², Quadrat (x + 4)² mit zwei Streifen 4x und 16. fehler_bild meist als Einsetztabelle (falscher Term ergibt anderen Wert).
Prüfung: siehe offen im Abschlussbericht.

## 2026-11-16 05:30 – STATUS
gleichungen.linear umgebaut (6 Karten): Waage als Bildergeschichte (3x + 5 | 20 → 3x | 15 → x | 5; beide Seiten: 5x + 3 | 2x + 15 → 3x + 3 | 15 → 3x | 12 → x | 4) mit vorhandenem `waage()`. Neu `waage_kipp()` als fehler_bild (gekippte Waage, gleiche Zeichenart figur). Klammern: vorhandenes Flächenbild. Probe: Tabelle füllt sich (x = 1/3 falsch, x = 5 richtig). Sonderfälle und Sachaufgabe: Tarif-Geraden im Koordinatensystem (parallel → L = { }; deckungsgleich → L = ℚ; Schnittpunkt (5|20)).
Aufgaben: 162, 0 Unterschiede. inhalt_pruefen: 0 Fehler, 0 Hinweise.

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
