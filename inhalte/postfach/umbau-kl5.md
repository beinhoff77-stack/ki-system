# Postfach umbau-kl5 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Paket U5, Klasse 5)

Technik: je Generator ein Abschnitt KARTEN (ersetzt den Abschnitt KLAR der Runde 7), eingesetzt über `inhalte/generatoren/_umbau_kl5.py`
erst NACH dem Erzeugen der Aufgaben – so bleiben die Aufgaben wörtlich gleich. `_umbau_kl5.py` prüft die Regeln der Vorgabe 16.11. streng
(alles, was `inhalt_pruefen.py` als Hinweis meldet, bricht dort ab) und spielt die Bildzustände der Schritte wie die App nach
(Werte im Zahlenstrahl-Bereich, Thermometer-Stand, Figur-Punkte, Tabellenbreite). `probe` entfällt bei umgebauten Karten (kommt im neuen Muster nicht vor).
Vergleich je Thema: `aufgaben` und alle Felder außer `inhalt.etappen` und `offen` gegen den Ausgangsstand bc7a754 (lernen-app).

## 2026-11-16 02:49 – STATUS
zahlen.rechengesetze (10 Karten) umgebaut. Kartenbilder: Rechentabellen, die sich Schritt für Schritt füllen (Kino, Einkauf, Verein); Rechenbaum (baum) für termaufbau; Zahlenstrahl mit Bögen für mal_ganz, geteilt_ganz, ueberschlag.
inhalt_pruefen: OK, keine Hinweise. Vergleich: 250 Aufgaben wörtlich gleich, Rest gleich.
Kein fehler_bild bei termaufbau, mal_ganz, geteilt_ganz, ueberschlag, schriftlich (Fehler ist eine falsche Rechenregel, im Bild nicht sinnvoll zu zeigen).
klammern: verschachtelte Klammern nur noch im Merksatz (das Beispiel hätte die Schrittlänge gesprengt). schriftlich: Beispiel nur Malnehmen, schriftliches Teilen steht im Merksatz und im Fehler (1 236 : 6 = 206).

## 2026-11-16 03:40 – STATUS
zahlen.ganz (8 Karten) umgebaut: Thermometer (deuten, ordnen-Fehler, sach), Zahlengerade mit Punkten/Bögen/Bereich (übrige Karten).
inhalt_pruefen: OK, keine Hinweise. Vergleich: 224 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.
ketten: kein fehler_bild (der falsche Weg 12 + 5 + 9 − 4 = 22 sprengt den Zahlenstrahl 0–20 und wäre unübersichtlich).
