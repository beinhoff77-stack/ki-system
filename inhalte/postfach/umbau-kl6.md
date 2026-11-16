# Postfach umbau-kl6 (Achte Runde: Umbau der Lernkarten auf das neue Muster, Paket U6, Klasse 6)

Technik: je Generator ein Abschnitt KARTEN (ersetzt den Abschnitt KLAR der Runde 7), eingesetzt über `inhalte/generatoren/_umbau_kl6.py` (dieselben strengen Regeln wie `_umbau_kl5.py` aus Paket U5) erst NACH dem Erzeugen der Aufgaben – die Aufgaben bleiben wörtlich gleich. `probe` entfällt bei umgebauten Karten. finanzen.zinsen (ohne Generator): Überlagerung `inhalte/klar/finanzen.zinsen.json`, mit denselben Regeln geprüft.
Vergleich je Thema: `aufgaben`, titel/lernziel und alle Felder außer `inhalt.etappen` und `offen` gegen den Ausgangsstand bc7a754 (lernen-app).

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
