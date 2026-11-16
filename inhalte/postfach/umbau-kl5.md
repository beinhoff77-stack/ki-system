# Postfach umbau-kl5 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Paket U5, Klasse 5)

Technik: je Generator ein Abschnitt KARTEN (ersetzt den Abschnitt KLAR der Runde 7), eingesetzt über `inhalte/generatoren/_umbau_kl5.py`
erst NACH dem Erzeugen der Aufgaben – so bleiben die Aufgaben wörtlich gleich. `_umbau_kl5.py` prüft die Regeln der Vorgabe 16.11. streng
(alles, was `inhalt_pruefen.py` als Hinweis meldet, bricht dort ab) und spielt die Bildzustände der Schritte wie die App nach
(Werte im Zahlenstrahl-Bereich, Thermometer-Stand, Figur-Punkte, Tabellenbreite). `probe` entfällt bei umgebauten Karten (kommt im neuen Muster nicht vor).
Vergleich je Thema: `aufgaben` und alle Felder außer `inhalt.etappen` und `offen` gegen den Ausgangsstand bc7a754 (lernen-app).

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
