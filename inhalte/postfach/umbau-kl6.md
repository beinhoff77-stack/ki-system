# Postfach umbau-kl6 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Paket U6, Klasse 6)

Technik: je Generator ein Abschnitt KARTEN (ersetzt den Abschnitt KLAR der Runde 7), eingesetzt über `inhalte/generatoren/_umbau_kl6.py` (dieselben strengen Regeln wie `_umbau_kl5.py` aus Paket U5) erst NACH dem Erzeugen der Aufgaben – die Aufgaben bleiben wörtlich gleich. `probe` entfällt bei umgebauten Karten. finanzen.zinsen (ohne Generator): Überlagerung `inhalte/klar/finanzen.zinsen.json`, mit denselben Regeln geprüft.
Vergleich je Thema: `aufgaben`, titel/lernziel und alle Felder außer `inhalt.etappen` und `offen` gegen den Ausgangsstand bc7a754 (lernen-app).

## 2026-11-16 03:02 – STATUS
daten.kennwerte (6 Karten) umgebaut. Kartenbilder: Säulen (Punkte 7, 9, 4, 8 → alle 7; drei Tests mit fehlendem Ergebnis → 7; Schuhgrößen als Häufigkeiten; Taschengeld mit Ausreißer), Notenspiegel-Tabelle mit Zeile „Note · Anzahl“, Zahlenstrahl 0–20 mit den geordneten Schulweg-Zeiten und markiertem Median.
Neu: Kartenbilder für mittel_rueckwaerts, modal_spannweite, median, verstehen (bisher ohne Bild).
Kein fehler_bild (Rechen- und Lesefehler).
inhalt_pruefen: OK, keine Hinweise. Vergleich gegen bc7a754: 168 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.

## 2026-11-16 03:01 – STATUS
daten.darstellen (6 Karten) umgebaut. Kartenbilder: Strichliste als sich füllende Tabelle (Würfeln), Bruchstreifen Lena 7/25 gegen Tom 11/50 → Säulen 28 % / 22 %, Häufigkeitstabelle Schulweg mit Summe und Anteilen, Säulen Lieblingssport, Kreisdiagramm Schulweg, Säulen Freibad (Achse ab 960 → im letzten Schritt ab 0).
Neu: Kartenbilder für absolute_haeufigkeit und relative_haeufigkeit (bisher ohne Bild).
Kein fehler_bild in diesem Thema (Lese- und Rechenfehler; das irreführende Bild selbst ist schon das Kartenbild).
inhalt_pruefen: OK, keine Hinweise. Vergleich gegen bc7a754: 168 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.

## 2026-11-16 03:00 – STATUS
bruch.rechnen (10 Karten) umgebaut. Kartenbilder: Bruchstreifen (Wanderung 3/4 + 1/6 → Zwölftel, Schulgarten 3/4 → 9/12 → 6/12, 25-Cent-Münzen, Pizza Punkt vor Strich), Tabellen (Bäcker Komma unter Komma mit Übertrag, Aufkleber in € und Cent, Obstwaage mit Überschlag), Thermometer (−2,5 °C → −1,3 °C), Zahlenstrahl in Sechsteln mit Saft-Bereich und Becher-Bögen (Teilen durch 2/3), Figur Klebeband 0,3 m × 0,04 m.
fehler_bild: brueche_plus_minus (4/10 kleiner als 3/4), dezimal_geteilt (Komma nur beim Preis verschoben). Übrige Fehler sind Rechenregel-Fehler.
Das Raster-Bild (figur 4 × 3) bei brueche_mal ist durch zwei Bruchstreifen ersetzt.
inhalt_pruefen: OK, keine Hinweise. Vergleich gegen bc7a754: 280 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.

## 2026-11-16 02:58 – STATUS
bruch.prozent (7 Karten) umgebaut. Kartenbilder: Bruchstreifen (Akku 3/4 → 75/100, Fahrrad in 20 Teilen zu 5 %, Probe 21/25 gegen 34/40, Kartoffelernte in Zehnteln, Jacke in Vierteln), Säulen (Sparbuch 500 € → 515 €, Spielpreis 100 → 90 → 99 €); prozentsatz wechselt im letzten Schritt zu Säulen 84 % / 85 %.
fehler_bild nur bei prozent_bedeutung (0,5 = 50 %, nicht 5 %); die übrigen Fehler sind Rechenweg-Fehler.
Das Hunderterfeld (figur) der Karte prozent_bedeutung ist durch einen Bruchstreifen mit 100 Teilen ersetzt (Bildergeschichte 3/4 → 75/100).
inhalt_pruefen: OK, keine Hinweise. Vergleich gegen bc7a754: 196 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.

## 2026-11-16 02:57 – STATUS
bruch.dezimal (7 Karten) umgebaut. Kartenbilder: Stellentafel mit wanderndem Markierer (stellenwerte, dezimal_zu_bruch → wechselt im letzten Schritt zum Bruchstreifen 7/20), Zahlenstrahl-Ausschnitte mit Punkten/Bereich (vergleichen_ordnen 0,4–0,5; runden 4,3–4,4; bruch_zu_dezimal 0–1 in Achteln; verstehen 0,1–0,2), Tabelle der schriftlichen Division mit wiederkehrendem Rest (periodisch).
fehler_bild: runden (2,349 liegt in der unteren Hälfte), bruch_zu_dezimal (3,8 weit hinter 3/8), verstehen (3,14 vor 3,2). Kein fehler_bild bei stellenwerte, vergleichen_ordnen, dezimal_zu_bruch, periodisch (Lese-/Stellenfehler).
periodisch: Das Kriterium „Nenner mit anderen Primfaktoren als 2 und 5“ steht jetzt nur noch im Merksatz (Schritte hätten die Länge gesprengt).
inhalt_pruefen: OK, keine Hinweise. Vergleich gegen bc7a754: 196 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.

## 2026-11-16 02:55 – STATUS
bruch.brueche (8 Karten) umgebaut. Kartenbilder: Bruchstreifen (ersetzen die gezeichneten Raster/Streifen aus figur) für bruchteil_von, anteil_bestimmen, ganzes_bestimmen, erweitern, kuerzen, vergleichen, verstehen; Zahlenstrahl mit Bögen und Punkt für zahlenstrahl. Durchgehende Situation: Klassenfest (Kasse, Band, Schokolade, Muffins, Kuchen, Weg zur Festwiese, Pizza).
inhalt_pruefen: OK, keine Hinweise. Vergleich gegen bc7a754: 224 Aufgaben wörtlich gleich, Rest gleich, titel/lernziel gleich.
Kein fehler_bild bei bruchteil_von, anteil_bestimmen, ganzes_bestimmen, verstehen (Rechenweg-Fehler: falsche Reihenfolge Zähler/Nenner bzw. Beweis durch ein Beispiel – im Streifen nicht sinnvoll zu zeigen). Jede Karte laut gelesen.

## Ende
