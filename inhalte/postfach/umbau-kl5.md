# Postfach umbau-kl5 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Paket U5, Klasse 5)

Technik: je Generator ein Abschnitt KARTEN (ersetzt den Abschnitt KLAR der Runde 7), eingesetzt über `inhalte/generatoren/_umbau_kl5.py`
erst NACH dem Erzeugen der Aufgaben – so bleiben die Aufgaben wörtlich gleich. `_umbau_kl5.py` prüft die Regeln der Vorgabe 16.11. streng
(alles, was `inhalt_pruefen.py` als Hinweis meldet, bricht dort ab) und spielt die Bildzustände der Schritte wie die App nach
(Werte im Zahlenstrahl-Bereich, Thermometer-Stand, Figur-Punkte, Tabellenbreite). `probe` entfällt bei umgebauten Karten (kommt im neuen Muster nicht vor).
Vergleich je Thema: `aufgaben` und alle Felder außer `inhalt.etappen` und `offen` gegen den Ausgangsstand bc7a754 (lernen-app).

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
