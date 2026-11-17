# Postfach umbau-rest (Paket UR, Achte Runde)

## 2026-11-17 02:22 – FERTIG
Paket UR (Zweig `umbau-rest`): alle 24 Themen ohne gym_by (Realschule/IB/ohne Klasse) mit zusammen 130 Lernkarten auf das neue Muster umgebaut. Ein Thema = ein Commit, alle gepusht.

| Thema | Karten | Aufgaben gleich | Prüfskript | Karten mit fehler_bild |
|---|---|---|---|---|
| abbildungen.determinanten2 | 6 | 168/168 | 0 Fehler, 0 Hinweise | 4 |
| abbildungen.vektoren | 6 | 168/168 | 0/0 | 3 |
| daten.stichproben | 5 | 140/140 | 0/0 | 0 |
| funktionen.scharen | 6 | 168/168 | 0/0 | 5 |
| terme.quadratische_extreme | 5 | 140/140 | 0/0 | 2 |
| funktionen.transformation | 6 | 168/168 | 0/0 | 4 |
| gleichungen.reinquadratisch | 6 | 168/168 | 0/0 | 3 |
| gleichungen.wurzel | 6 | 168/168 | 0/0 | 2 |
| abbildungen.matrizen | 6 | 168/168 | 0/0 | 2 |
| funktionen.umkehr | 6 | 168/168 | 0/0 | 1 |
| mengen.grundbegriffe | 5 | 140/140 | 0/0 | 2 |
| groessen.verhaeltnisse | 6 | 168/168 | 0/0 | 2 |
| daten.zweidimensional | 5 | 140/140 | 0/0 | 0 |
| daten.standardabweichung | 5 | 140/140 | 0/0 | 1 |
| stochastik.bedingt | 6 | 168/168 | 0/0 | 1 |
| funktionen.betrag | 5 | 140/140 | 0/0 | 3 |
| funktionen.folgen | 5 | 140/140 | 0/0 | 0 |
| funktionen.reihen | 5 | 140/140 | 0/0 | 0 |
| sonder.graphentheorie | 5 | 140/140 | 0/0 | 2 |
| sonder.optimierung | 5 | 140/140 | 0/0 | 1 |
| daten.normalverteilung | 5 | 140/140 | 0/0 | 1 |
| finanzen.zinseszins | 5 | 140/140 | 0/0 | 2 |
| sonder.logik | 5 | 140/140 | 0/0 | 2 |
| zahlen.schranken | 5 | 140/140 | 0/0 | 4 |

### Was gemacht ist
- Jede Karte: einstieg (≤ 35 Wörter, Alltagssituation, möglichst durchgehend im Thema), woerter (≤ 3, jedes im Text), Kartenbild, schritte als {text, bild} mit Bild bei jedem Bildwechsel, fehler (≤ 30 Wörter) + fehler_bild wo zeigbar, regel (erster Satz ≤ 12 Wörter als „Kurz gesagt“). Satzlänge nach Prüfskript (IB-Themen ≤ 15, RS/zusatz ≤ 20). titel, lernziel, Aufgaben, abschnitte, merke, ziel unverändert.
- Technik: neue Hilfsdatei `inhalte/generatoren/_umbau_rest.py` (`umbau_schreiben`). Die Generatoren erzeugen die Aufgaben wie bisher mit den alten Karten (dort hängt der Dopplungsabgleich dran) und ersetzen danach die Erklärfelder. Die alte `probe` fällt weg; wo nötig steht die Kontrolle als Schritt. Bilder mit `typ` in Schritten werden als vollständige Bilder behandelt (Felder des vorigen Zustands auf null), wie in `_umbau_kl7.py`.
- Nachweis je Thema: Aufgaben-Liste der neuen Datei == `git show origin/lernen-app:inhalte/themen/<thema>.json` (Vergleich des ganzen Felds `aufgaben`, plus Kopf-, abschnitte-, bewertung-Felder). Alle Zahlen der Beispiele nachgerechnet.
- Zeichnungen: jede Karte mit der App-Funktion `lernErklaerung` aus `lernen.js` im Browser (Playwright/Chrome) gerendert und angesehen; Darstellungsfehler (abgeschnittene Achsennamen, überlappende Venn-Beschriftungen, Punkte am Rand) korrigiert.

### Geänderte Beispiele (Zahlen neu, nachgerechnet; keine Aufgabe gleicht dem neuen Beispiel)
- funktionen.scharen: durchgehende Taxi-Situation (k = 3 statt −3; P(3 | 10) statt P(3 | 1); loesung_parameter mit Taxi A y = 2x + 4 / Taxi B y = kx).
- funktionen.transformation/strecken: x = 2 statt x = 3 (passt ins Bild).
- gleichungen.reinquadratisch/umformen: 3x² + 20 = 95 statt 3x² − 20 = 55 (gleiche Zwischenschritte).
- sonder.graphentheorie/euler: 5 Knoten statt 4 (die alte Gradliste 2, 3, 4, 3 ist mit 4 Knoten nicht als einfacher Graph zeichenbar).

### Erledigte App-Wünsche aus "offen" (jetzt mit vorhandenen Zeichnungsarten gelöst, nur in den Karten)
- Vektorpfeile (determinanten2, vektoren) → `pfeile`; zulässigen Bereich füllen (optimierung) → `flaechen`; Glockenkurve (normalverteilung) → Graph-Art `glocke` + `flaechen`; Fehlerbereich auf dem Zahlenstrahl (schranken) → `bereich`. In "offen" steht jeweils, dass die Aufgaben-Grafiken unverändert die alte Darstellung behalten.

### offen
- Die Aufgaben-Grafiken (unverändert) nutzen teils noch die alten Ersatzdarstellungen (Strecken statt Pfeile, Säulen statt Glocke, Randgeraden ohne Fläche). Wer die Aufgaben-Grafiken umstellen will, ändert damit die Aufgaben – bewusst nicht gemacht.
- mengen.grundbegriffe: `venn()` aus `_ib.py` setzt die Kreisnamen für die alte, kleinere Schrift. Bei langen Namen (z. B. Fußball/Schwimmen) überlappen sie in Aufgaben-Grafiken; in den Karten sind sie verschoben. App-Wunsch: eigene Zeichnungsart „venn“.
- Zahlenstrahl-Punkte können nicht hohl gezeichnet werden (für „obere Schranke gehört nicht dazu“). App-Wunsch, falls gewünscht: `"offen": true` auch bei zahlenstrahl.punkte.
- funktionen.umkehr/quadratisch: √(x − 1) + 2 kann die App nicht als Graph zeichnen (Graph-Art wurzel nur √x).
- Einige Karten zeigen erfundene Beispieldaten (daten.zweidimensional Autos/Eis, stochastik.bedingt Hund/Spaziergänger, daten.stichproben „zum Beispiel 60 %“); jeweils in "offen" bzw. im Text als Beispiel gekennzeichnet.
- Nicht mit Kindern getestet; laut AUFTRAEGE.md läuft UR zuletzt. Kein Merge nach main oder lernen-app; keine Datenbank, kein App-Code, keine Tests geändert.

## 2026-11-17 02:22 – STATUS
zahlen.schranken umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/zahlen.schranken.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: produkt (der Fehler betrifft Geschwindigkeit, nicht die Fliese aus dem Bild). Fehlerbereiche jetzt auf dem Zahlenstrahl mit markiertem Bereich (alter App-Wunsch erledigt, aus offen entfernt). Die obere Schranke erscheint als voller Punkt; ein hohler Punkt auf dem Zahlenstrahl ist laut README nicht vorgesehen – der Text sagt „gehört nicht mehr dazu“.

## 2026-11-17 02:21 – STATUS
sonder.logik umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/sonder.logik.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: aussagen (Begriffsfehler), verknuepfen (das Kartenbild zeigt die vollständige Tafel mit beiden Wahr schon), folgerung (Umkehrschluss; das Schrittbild zeigt das Gegenbeispiel 6). Alle Bilder sind Tabellen (Wahrheitstafeln, Beispieltabellen); passende Zeichnungsarten gibt es nicht und werden nicht gebraucht.

## 2026-11-17 02:20 – STATUS
finanzen.zinseszins umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/finanzen.zinseszins.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: formel (Rechenfehler „mal 6“ statt Potenz), rueck (falscher Rechenweg), vergleich (Denkfehler einfache Zinsen). Zahlen der Schrittbilder nachgerechnet: 5 000 · 1,02ⁿ (n = 0…6) bis 5 630,81 €; 1,07⁸…1,07¹¹ = 1,718 / 1,838 / 1,967 / 2,105; 1,05¹⁴ ≈ 1,98 < 2 ≤ 1,05¹⁵ ≈ 2,08.

## 2026-11-17 02:18 – STATUS
daten.normalverteilung umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/daten.normalverteilung.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: regel (136 % liegt außerhalb jedes Bildes), anteile und zwert (Rechenfehler; die Schrittbilder zeigen die richtige Fläche bzw. den Abstand), vergleichen (Denkfehler). Kartenbilder jetzt echte Glockenkurven (Graph-Art glocke) mit gefärbten Flächen; der alte App-Wunsch „Glockenkurve“ ist aus offen entfernt, Hinweis für die unveränderten Aufgaben-Grafiken ergänzt.

## 2026-11-17 02:17 – STATUS
sonder.optimierung umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/sonder.optimierung.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: aufstellen (Übersetzungsfehler ≤/≥), ecken (Ablese-Risiko, zwei fast gleiche Punkte sind im Bild nicht unterscheidbar), optimum und sach (die Schrittbilder zeigen die Werte an allen Ecken schon). Zulässiger Bereich in den Karten jetzt gefüllt (flaechen); alter App-Wunsch „Bereich füllen“ aus offen entfernt, Hinweis für die unveränderten Aufgaben-Grafiken ergänzt. Beispiele durchgehend Bäckerei (kleine: Ecken (0|0), (4|0), (2|4), (0|5); größere: 2x + 3y ≤ 30, Ecken bis (6|6)).

## 2026-11-17 02:16 – STATUS
sonder.graphentheorie umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/sonder.graphentheorie.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: grundbegriffe (Zählfehler), euler (allgemeine Aussage über vier ungerade Knoten), kuerzester (das Schrittbild zeigt direkten Weg und Umweg schon). Beispiel euler neu mit 5 Knoten (Grade 2, 3, 4, 3, 2; 7 Kanten), weil das alte Beispiel (A 2, B 3, C 4, D 3) als einfacher Graph mit 4 Knoten nicht zeichenbar ist; Eulerweg B, A, C, B, D, C, E, D nachgeprüft. Gewählte Kanten durchgezogen, übrige gestrichelt.

## 2026-11-17 02:15 – STATUS
funktionen.reihen umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.reihen.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: alle 5 Karten – Fehler beim Zählen bzw. in der Formel (letztes Glied statt Summe, doppelt gezählt, qⁿ⁻¹ statt qⁿ, Ende vergessen); die Schrittbilder zeigen jeweils die richtige Rechnung.

## 2026-11-17 02:14 – STATUS
funktionen.folgen umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.folgen.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: alle 5 Karten – die Fehler sind Zähl- und Einsetzfehler (Platznummer statt Wert, n statt n − 1, Glied statt vorigem Glied, zu wenige Glieder); Säulenbilder würden nur die richtigen Werte wiederholen. Kartenbilder: Säulendiagramme der Folgenglieder (a₁, a₂, …) und eine Differenzen-/Quotiententabelle.

## 2026-11-17 02:12 – STATUS
funktionen.betrag umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.betrag.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: betrag (Rechenfehler beim Aufteilen des Betrags), verstehen (das Beispiel steht schon in den Schrittbildern). Kartenbilder nutzen jetzt die Graph-Art betrag; die Aufgaben-Grafiken bleiben unverändert (zwei Geradenstücke, offen-Hinweis bleibt).

## 2026-11-17 02:11 – STATUS
stochastik.bedingt umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/stochastik.bedingt.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: tafel, formel, rueckschluss, verstehen (Fehler beim Teilen bzw. vertauschte Bedingung; die Schrittbilder zeigen die richtige Gruppe), unabhaengig (Denkfehler ohne Zahlenbild). Kartenbild formel: Bruchstreifen (0,4 der Kinder fahren Rad, davon 1/4 mit Brille). Karte verstehen mit Beispiel-Vierfeldertafel (offen-Punkt).

## 2026-11-17 02:10 – STATUS
daten.standardabweichung umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/daten.standardabweichung.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: abweichung (die Summe 0 zeigt das Schrittbild schon), sigma (Einheitenfehler), eigenschaften (Rechenfehler; das Schrittbild zeigt gleiche Abstände), deuten (Deutungsfehler).

## 2026-11-17 02:09 – STATUS
daten.zweidimensional umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/daten.zweidimensional.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: ablesen, zusammenhang, kausal (Lese- bzw. Denkfehler), gerade (140 Punkte liegen außerhalb des Bildes), ausreisser (Denkfehler; das Schrittbild zeigt den Abstand zum Muster schon). Achsennamen kurz (h, Jahre), weil die App längere Namen am rechten Rand abschneidet; offen-Hinweis ergänzt.

## 2026-11-17 02:08 – STATUS
groessen.verhaeltnisse umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/groessen.verhaeltnisse.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: kuerzen (Einheitenfehler), aufteilen (die Schrittbilder zeigen die richtige Aufteilung), einheitsrate (Denkfehler), aenderung (Rechenfehler mit Endwerten).

## 2026-11-17 02:06 – STATUS
mengen.grundbegriffe umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/mengen.grundbegriffe.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: schnitt und vereinigung (Denkfehler beim Sammeln; das Schrittbild zeigt die richtige Aufteilung), verstehen (allgemeine Aussage ohne festes Beispiel). Venn-Bilder mit venn() aus _ib.py; in den Karten sind die Kreisnamen an die Außenkanten gerückt, weil lange Namen (Fußball/Schwimmen) bei 16-px-Schrift überlappten. Die Aufgaben-Grafiken nutzen weiter venn() unverändert – dort kann dieselbe Überlappung auftreten (siehe offen im Abschlussbericht).

## 2026-11-17 02:05 – STATUS
funktionen.umkehr umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.umkehr.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: umkehrbar (Begriffsfehler), werte (Kehrwert-Verwechslung), quadratisch (Vorzeichenfehler in der Formel), exp_log (Rechenfehler), spiegeln (der falsche Punkt (−3 | −8) läge außerhalb des Bildes). Neuer offen-Punkt: √(x − 1) + 2 kann die App nicht als Graph zeichnen.

## 2026-11-17 02:03 – STATUS
abbildungen.matrizen umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/abbildungen.matrizen.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: bildpunkt (Fehler in der Rechenreihenfolge), drehung (Vorzeichenfehler in der Formel), inverse (Fehler beim Umstellen der Einträge), skalarprodukt (Fehler „Vektor statt Zahl“ hat kein Bild). Matrizen weiter als Tabellen (Zeile/Spalte); der App-Wunsch „echte 2×2-Klammer“ bleibt unter offen.

## 2026-11-17 02:02 – STATUS
gleichungen.wurzel umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/gleichungen.wurzel.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: isolieren ((a + b)² ≠ a² + b² ist ein Rechenfehler), probe und zwei_seiten (die Schrittbilder zeigen die durchgefallene Probe schon), sachaufgabe (Reihenfolgefehler). Kartenbilder meist Umformungs- und Probetabellen; die App kann √(x + 7) nicht als Graph zeichnen (nur √x), darum keine Graphen bei zwei_seiten.

## 2026-11-17 02:01 – STATUS
gleichungen.reinquadratisch umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/gleichungen.reinquadratisch.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: schaetzen (falscher Rechenweg „Hälfte“, 27,5 liegt weit außerhalb des Bildes), klammer (Fehler beim Ausmultiplizieren), sachaufgabe (Deutungsfehler). Beispiel umformen: 3x² + 20 = 95 statt 3x² − 20 = 55 (passt zur Fliesen-Situation; gleiche Zwischenschritte 3x² = 75, x² = 25; keine Aufgabe gleicht dem Beispiel).

## 2026-11-17 01:59 – STATUS
funktionen.transformation umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.transformation.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: strecken (Rechenfehler beim Quadrieren), kombiniert (Vorzeichenfehler beim Ablesen; das Bild würde nur den richtigen Scheitel zeigen). Beispiel strecken: x = 2 statt x = 3 (y = 8 statt 18), damit der Punkt im Bild liegt.

## 2026-11-17 01:58 – STATUS
terme.quadratische_extreme umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/terme.quadratische_extreme.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: ergaenzen (die Zeichnung zeigt die richtige Ecke schon; eine 6 · 6-Ecke passt nicht ins Bild), extremwert (Vorzeichenfehler beim Ablesen), optimierung (Deutungsfehler Stelle/Wert). Wie bisher ohne Graphen (Thema ohne Parabellehre); Bilder sind Flächenmodell, Umformungs- und Wertetabellen. Alter Hinweis „flaeche“ für die Ecke nach Schritt 2 verlegt.

## 2026-11-17 01:57 – STATUS
funktionen.scharen umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/funktionen.scharen.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: loesung_parameter (Fehler ist ein fehlender Sonderfall; das Schrittbild 4 zeigt die parallelen Geraden schon). Beispiele in den Karten einsetzen, parallelenschar, loesung_parameter auf eine durchgehende Taxi-Situation umgestellt (k = 3 statt −3; P(3 | 10) statt P(3 | 1); Taxi A/B statt y = 2x + 1 / y = kx − 3), damit keine negativen Preise vorkommen; Zahlen nachgerechnet, keine Aufgabe gleicht den neuen Beispielen.

## 2026-11-17 01:55 – STATUS
daten.stichproben umgebaut (5 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/daten.stichproben.json`: 140 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: alle 5 Karten – die Fehler sind Denk- und Deutungsfehler (falscher Begriff, Anteil vergessen, „groß = repräsentativ“, freiwillige Antworten, Schätzwert für genau halten); ein Diagramm würde sie nicht zeigen. Kartenbild repraesentativ: der Wert 60 % für zufällig Befragte ist ausdrücklich als Beispiel bezeichnet („zum Beispiel“), keine Statistik.

## 2026-11-17 01:54 – STATUS
abbildungen.vektoren umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/abbildungen.vektoren.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Zeichnungen gerendert (app-eigenes lernErklaerung im Browser), angesehen. Ohne fehler_bild: addition (über Kreuz addieren lässt sich nicht sinnvoll zeichnen), punkt_berechnen (der falsche Punkt läge weit außerhalb), eigenschaften (Denkfehler; das Schrittbild zeigt beide Dreiecke gleich groß). Vektoren in den Karten jetzt als Pfeile; der alte App-Wunsch „Pfeilspitzen“ ist aus offen entfernt.

## 2026-11-17 01:52 – STATUS
abbildungen.determinanten2 umgebaut (6 Karten): einstieg, woerter (≤ 3), Kartenbild, Schritte als {text, bild}, fehler + fehler_bild, regel. UMBAU-Abschnitt im Generator, eingesetzt nach dem Erzeugen der Aufgaben (_umbau_rest.umbau_schreiben); probe entfällt.
Aufgaben-Vergleich gegen `git show origin/lernen-app:inhalte/themen/abbildungen.determinanten2.json`: 168 Aufgaben, alle wörtlich gleich; titel/lernziel unverändert. inhalt_pruefen: 0 Fehler, 0 Hinweise. Vektoren in den Karten jetzt als Pfeile (der alte offen-Punkt „keine Vektorpfeile“ ist erledigt). Ohne fehler_bild: det_berechnen (Vorzeichenfehler in der Rechnung), umlaufsinn (das Schrittbild zeigt den Umlauf schon).

