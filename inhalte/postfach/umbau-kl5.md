# Postfach umbau-kl5 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Paket U5, Klasse 5)

Technik: je Generator ein Abschnitt KARTEN (ersetzt den Abschnitt KLAR der Runde 7), eingesetzt über `inhalte/generatoren/_umbau_kl5.py`
erst NACH dem Erzeugen der Aufgaben – so bleiben die Aufgaben wörtlich gleich. `_umbau_kl5.py` prüft die Regeln der Vorgabe 16.11. streng
(alles, was `inhalt_pruefen.py` als Hinweis meldet, bricht dort ab) und spielt die Bildzustände der Schritte wie die App nach
(Werte im Zahlenstrahl-Bereich, Thermometer-Stand, Figur-Punkte, Tabellenbreite). `probe` entfällt bei umgebauten Karten (kommt im neuen Muster nicht vor).
Vergleich je Thema: `aufgaben` und alle Felder außer `inhalt.etappen` und `offen` gegen den Ausgangsstand bc7a754 (lernen-app).

## 2026-11-16 03:12 – FERTIG
Paket U5 (Klasse 5) umgebaut: 14 Themen, 101 Lernkarten. Jede Karte hat einstieg (≤ 35 Wörter, 2–3 Sätze), woerter (1–3), Kartenbild,
schritte als Objekte mit Bild je Bildänderung, fehler (≤ 30 Wörter), regel (≤ 25 Wörter, erster Satz ≤ 12 Wörter als „Kurz gesagt“); fehler_bild bei 41 Karten.

| Thema | Karten | Aufgaben | wörtlich gleich (gegen bc7a754) | inhalt_pruefen |
|---|---|---|---|---|
| zahlen.ganz | 8 | 224 | ja | OK, 0 Hinweise |
| zahlen.rechengesetze | 10 | 250 | ja | OK, 0 Hinweise |
| zahlen.potenzen_basis | 7 | 175 | ja | OK, 0 Hinweise |
| groessen.einheiten | 8 | 224 | ja | OK, 0 Hinweise |
| groessen.proportional | 7 | 175 | ja | OK, 0 Hinweise |
| geometrie.grundbegriffe | 7 | 196 | ja | OK, 0 Hinweise |
| geometrie.winkel | 7 | 196 | ja | OK, 0 Hinweise |
| geometrie.ortslinien | 6 | 168 | ja | OK, 0 Hinweise |
| messen.flaechen | 7 | 196 | ja | OK, 0 Hinweise |
| messen.koerper_berechnung | 6 | 168 | ja | OK, 0 Hinweise |
| stochastik.kombinatorik | 7 | 196 | ja | OK, 0 Hinweise |
| gleichungen.einfach | 7 | 189 | ja | OK, 0 Hinweise |
| zahlen.natuerlich (Überlagerung) | 12 | – | nicht berührt | Regeln mit _umbau_kl5.pruefe_karte geprüft |
| zahlen.teilbarkeit (Überlagerung) | 8 | – | nicht berührt | Regeln mit _umbau_kl5.pruefe_karte geprüft |

Prüfungen:
- Vergleich je Thema: `aufgaben`, alle Felder außer `inhalt.etappen` und `offen`, titel und lernziel gleich dem Ausgangsstand. Generatoren laufen reproduzierbar (zweiter Lauf ändert nichts).
- Render-Probe: Alle 507 Bildzustände (Kartenbild, jeder Schritt kumuliert wie lernSchrittBild, fehler_bild) mit lernBild aus lernen.js unter jsdom gezeichnet – 0 Fehler, kein NaN/undefined im SVG.
  Nicht geprüft: das Aussehen auf dem Handy (Abstände, Überlappungen von Beschriftungen). Bitte bei der Abnahme ansehen, besonders das Baumdiagramm mit 8 Pfad-Blättern
  (kombinatorik/baumdiagramm, letzter Schritt) und die breiteren Tabellen (Bakterien mit 7 Spalten, Rechenkette mit 6 Spalten).
- Alle Zahlen der Situationen nachgerechnet; Laut-Lese-Durchgang über alle Schritte gemacht.

Technik und Entscheidungen:
- Abschnitt KARTEN je Generator ersetzt den KLAR-Abschnitt aus Runde 7; eingesetzt über `_umbau_kl5.py` (umbau, bei gleichungen.einfach die Hülle mit_umbau um baue aus _nachbau).
  `_klar_kl5.py` wird nicht mehr gebraucht und ist gelöscht. `probe` entfällt bei umgebauten Karten (kein Platz im neuen Muster).
- 'BEHALTEN' im Feld bild übernimmt vom Generator berechnete Figuren (Fliesenraster, Winkelfiguren, Uhr, Windrose, Quader, L-Form …); die Schritte ändern dann nur Beschriftungen.
- Neue Wörter auf höchstens 3 begrenzt; was dadurch aus den Wörterlisten fiel, steht jetzt im Kartenbild (z. B. Vierecks-Übersicht, römische Zeichen) oder im Merksatz.
- Merksätze wurden kürzer; einzelne Regeln stehen nur noch in den Lösungswegen der Aufgaben (genannt in den STATUS-Meldungen: Quadrat-Formeln, Kreis im Kreis, Quader-Oberflächenformel, schriftliches Teilen nur im Fehler).
- Beispiele geändert, wo das Bild es verlangte: potenzen/schreibweise 2 · 2 · 2 statt 5 · 5 · 5, geometrie/winkelarten 135° statt 235°.

Offen:
- Keine Zeichnungsart fehlte für die Karten; kein Eintrag unter "offen" nötig. Schrägbilder/Netze (README) wären für messen.koerper_berechnung weiterhin schöner als die vorhandene Quader-Linienfigur.
- inhalt_pruefen kann die Überlagerungen (inhalte/klar/…) nicht direkt prüfen; erst nach dem Einspielen mit den Aufgaben aus der Datenbank.

## 2026-11-16 03:11 – STATUS
zahlen.teilbarkeit (8 Karten, ohne Generator) umgebaut: Überlagerung inhalte/klar/zahlen.teilbarkeit.json. quelle.md hatte für dieses Thema keine Bilder;
neu: Tabellen, die sich füllen (Teilerpaare der Muffins, Quersumme, Prüfzahlen für 53 mit Rest, Primfaktorzerlegung von 60, Teilerlisten 12 und 18, Runden von Lena und Tim),
Zahlenstrahl mit Siebenerbögen (Vielfache), Stellenwerttafel (Endziffer). Alle Reste und Ergebnisse nachgerechnet (53 = 2 · 26 + 1 = 3 · 17 + 2 = 5 · 10 + 3 = 7 · 7 + 4; 4 251 : 3 = 1 417).
Geprüft mit _umbau_kl5.pruefe_karte.

## 2026-11-16 03:10 – STATUS
zahlen.natuerlich (12 Karten, ohne Generator) umgebaut: Überlagerung inhalte/klar/zahlen.natuerlich.json mit einstieg, woerter, bild, schritte als Objekte, fehler, fehler_bild, regel.
Bilder aus quelle.md beibehalten und erweitert: Stellenwerttafeln (4 052, 12 | 008 | 000, 3 | 040 | 500, Runden 3 472 und 2 995, 333, 999 999 999 + 1), Zahlenstrahl 0–100 mit Pfeil 3 bzw. 7,
Tabellen (90 909 gegen 90 990, Runden sinnvoll, römische Zeichen, 39 = XXXIX). Beispielzahlen der Karten unverändert.
Geprüft mit _umbau_kl5.pruefe_karte (dieselben Regeln wie inhalt_pruefen + Bildzustände); inhalt_pruefen selbst braucht die Themen-Datei, die es für dieses Thema im Zweig nicht gibt.

## 2026-11-16 03:06 – STATUS
gleichungen.einfach (7 Karten) umgebaut (Generator mit baue aus _nachbau: neue Hülle mit_umbau in _umbau_kl5.py statt mit_klar). Waage-Figur mit wechselnden Schalen-Beschriftungen (waage, probe, aufstellen), gekippte Waage als fehler_bild (links 13, rechts 10); Zahlenstrahl mit Bögen (Geldbeutel, Aufzug mit schattiertem Bereich unter 0); Bruchstreifen 12 € auf 4 Hefte; Rechenketten-Tabelle vorwärts/rückwärts.
inhalt_pruefen: OK, keine Hinweise. Vergleich: 189 Aufgaben wörtlich gleich, Rest gleich.

## 2026-11-16 03:04 – STATUS
stochastik.kombinatorik (7 Karten) umgebaut. Tabellen füllen sich Schritt für Schritt (Outfits, Menü, Siegerpodest, Stellen, zweistellige Zahlen); Baumdiagramm wächst Stufe für Stufe, am Ende stehen die ganzen Pfade an den Blättern (✓ bei genau zweimal K); Händeschütteln als Figur: erst die 4 Linien von A, dann alle 10.
inhalt_pruefen: OK, keine Hinweise. Vergleich: 196 Aufgaben wörtlich gleich, Rest gleich.
fehler_bild bei verstehen (Tabelle mit 11, 22, 33 = mit Wiederholung 9 Zahlen).

## 2026-11-16 03:02 – STATUS
messen.koerper_berechnung (6 Karten) umgebaut. Vorhandene Quader- und Würfelreihen-Figuren bleiben Kartenbild; neue Tabellen füllen sich Schritt für Schritt (Flächenpaare, Aquarium-Glas, Schichten beim Volumen); Säulen für 6 cm² gegen 24 cm² (verstehen).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 168 Aufgaben wörtlich gleich, Rest gleich.
oberflaeche: Die Quader-Formel O = 2 · a · b + 2 · a · c + 2 · b · c sprengt die Satzlänge (15 Wörter) – im Merksatz steht „alle 6 Flächen, je zwei gleich groß“; die Formel zeigt die Tabelle im Bild.
Kein fehler_bild in diesem Thema (Fehler sind Zähl- und Formelfehler); Schrägbilder/Netze als Zeichnungsart fehlen weiterhin (siehe README).

## 2026-11-16 03:01 – STATUS
messen.flaechen (7 Karten) umgebaut. Vorhandene Figuren bleiben Kartenbild (Einheitsquadrate, Rechteck, 1 m² = 100 dm², L-Form); L-Form wird im Beispiel gestrichelt zum Rechteck ergänzt und zur Probe zerlegt. Neu: Einheiten-Tabelle (kommaschreibweise, mit fehler_bild 6 | 50), Garten-Rechteck (sachaufgaben), zwei Gärten im selben Maßstab (verstehen).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 196 Aufgaben wörtlich gleich, Rest gleich.
rechteck: Merksatz ohne die Quadrat-Formeln (25-Wörter-Grenze); A = a · a und u = 4 · a stehen in den Lösungswegen der Quadrat-Aufgaben.

## 2026-11-16 02:59 – STATUS
geometrie.ortslinien (6 Karten) umgebaut. Figuren und Koordinatensysteme bauen sich Schritt für Schritt auf: Napf im Leinen-Kreis, Parallelen oben und unten, zwei Kreise mit Schnittpunkten S₁ und S₂ (nachgerechnet: x = 73/16, y ≈ ±2,05), Schatz mit Kreis und Parallelen, Sprenger mit Beet; sachsituationen und verstehen haben jetzt ein Bild.
inhalt_pruefen: OK, keine Hinweise. Vergleich: 168 Aufgaben wörtlich gleich, Rest gleich.
zwei_kreise: Merksatz nennt „meist zwei, bei Berührung einer“; der Fall „gar keiner“ steht im Fehler mit Bild (B 10 km entfernt). Der Fall „ein Kreis ganz im anderen“ passt nicht mehr in die 25 Wörter – er steht in den Lösungswegen der betreffenden Aufgaben.

## 2026-11-16 02:58 – STATUS
geometrie.winkel (7 Karten) umgebaut. Die vorhandenen Figuren bleiben Kartenbild; die Schritte tragen die ausgerechneten Winkel nach und nach ein (β = 130°, Kreuzung, Torte, Uhr 120°, Windrose 45° → 135°, Rechteck 55°). verstehen hat jetzt ein Bild (zwei stumpfe Winkel nebeneinander).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 196 Aufgaben wörtlich gleich, Rest gleich.
fehler_bild nur bei drehungen (N → O = 90°): Bei den übrigen Fehlern wäre eine falsch beschriftete, aber richtig gezeichnete Figur irreführend.

## 2026-11-16 02:56 – STATUS
geometrie.grundbegriffe (7 Karten) umgebaut. Koordinatensystem mit Schritt-Zuständen (Weg zum Punkt, Verschieben, Strecke in zwei Teilen, Lot), Figur mit Kreis und drei Geraden, Schere mit 45°/90°/135°, Vierecks-Übersicht als Tabelle mit Raute im Beispiel.
inhalt_pruefen: OK, keine Hinweise. Vergleich: 196 Aufgaben wörtlich gleich, Rest gleich.
winkelarten: Beispiel jetzt 135° (stumpf) statt 235° – die Figur kann keinen überstumpfen Winkelbogen zeichnen; 235° steht im Fehler.
vierecke: Kartenbild ist eine Übersichtstabelle aller sechs Vierecke (nur 3 neue Wörter erlaubt, die Aufgaben fragen alle sechs ab).

## 2026-11-16 02:55 – STATUS
groessen.proportional (7 Karten) umgebaut. Alle Bilder sind Tabellen, die sich Schritt für Schritt füllen (Brötchen, Äpfel, Hefte, Karten, Nudeln); fehler_bild zeigt jeweils die falsche oder die Gegen-Tabelle (Taxi mit Grundgebühr, Rabatt, Kochzeit).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 175 Aufgaben wörtlich gleich, Rest gleich.

## 2026-11-16 02:53 – STATUS
groessen.einheiten (8 Karten) umgebaut. Bilder: Raum mit Tür als Figur (schaetzen), Einheitentafeln (laenge, masse, kommaschreibweise), Zeitspannen-Tabelle (zeit), Zahlenstrahl mit Bögen (rechnen, massstab), Säulen (verstehen).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 224 Aufgaben wörtlich gleich, Rest gleich.
fehler_bild bei laenge und kommaschreibweise (falsch gefüllte Tafel). Merksätze nennen jetzt nur die wichtigsten Umrechnungen (Längenregel: 25 Wörter); die Umrechnungszahlen stehen vollständig in den Lösungswegen der Aufgaben.

## 2026-11-16 02:51 – STATUS
zahlen.potenzen_basis (7 Karten) umgebaut. Bilder: Baumdiagramm für das Weitererzählen in Runden (2 · 2 · 2), Tabellen (Bakterien, Fliesen), Säulen (2³ gegen 3², Papier falten), Stellentafel (Zehnerpotenz), Zahlenstrahl mit springenden Punkten (negative Basis).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 175 Aufgaben wörtlich gleich, Rest gleich.
Beispiel in schreibweise von 5 · 5 · 5 auf 2 · 2 · 2 geändert (passt zum Baumdiagramm; 3 Runden zu je 3 Kindern wären 27 Blätter). quadrat behält die Fliesen-Figur als Kartenbild.
Kein fehler_bild in diesem Thema: Die Fehler sind Rechenregel-Fehler (2³ ≠ 2 · 3, Nullen zählen, Klammer bei −3²).

## 2026-11-16 02:49 – STATUS
zahlen.rechengesetze (10 Karten) umgebaut. Kartenbilder: Rechentabellen, die sich Schritt für Schritt füllen (Kino, Einkauf, Verein); Rechenbaum (baum) für termaufbau; Zahlenstrahl mit Bögen für mal_ganz, geteilt_ganz, ueberschlag.
inhalt_pruefen: OK, keine Hinweise. Vergleich: 250 Aufgaben wörtlich gleich, Rest gleich.
Kein fehler_bild bei termaufbau, mal_ganz, geteilt_ganz, ueberschlag, schriftlich (Fehler ist eine falsche Rechenregel, im Bild nicht sinnvoll zu zeigen).
klammern: verschachtelte Klammern nur noch im Merksatz (das Beispiel hätte die Schrittlänge gesprengt). schriftlich: Beispiel nur Malnehmen, schriftliches Teilen steht im Merksatz und im Fehler (1 236 : 6 = 206).

## 2026-11-16 02:45 – STATUS
zahlen.ganz (8 Karten) umgebaut: Thermometer (deuten, ordnen-Fehler, sach), Zahlengerade mit Punkten/Bögen/Bereich (übrige Karten).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 224 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.
ketten: kein fehler_bild (der falsche Weg 12 + 5 + 9 − 4 = 22 sprengt den Zahlenstrahl 0–20 und wäre unübersichtlich).
