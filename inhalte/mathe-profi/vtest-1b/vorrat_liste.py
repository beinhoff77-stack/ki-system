"""Aufgaben, die nach der Entscheidung „je Lernziel 5 Aufgaben (1 Test + 2 Korrektur + 2 Sicherung)“ aus der Runde genommen und in vorrat-folgerunde/ abgelegt werden.
Schlüssel: (Einheit, idee). bauen.py baut und prüft sie wie alle anderen, schreibt sie aber nur in vorrat-folgerunde/<einheit>_vorrat.json."""
VORRAT = {
    # Einheit 20 (gleichungen.bruch), Welle 1
    ("gleichungen.bruch", "menge_zuordnen"),              # Schema (Nenner gleich 0 setzen)
    ("gleichungen.bruch", "text_zu_D"),                   # gleiche Denkfigur wie die Taxi-Aufgabe (D gegen sinnvolle Werte)
    ("gleichungen.bruch", "gleichung_zur_loesung"),       # Schema (Lösung einsetzen)
    ("gleichungen.bruch", "warum_ueber_kreuz"),           # gleiche Denkfigur wie „zwei Wege“
    ("gleichungen.bruch", "kandidaten_gegen_D"),          # Schema (Kandidat gegen D)
    ("gleichungen.bruch", "fehler_nicht_alle_glieder"),   # Schema (Rezeptfehler)
    ("gleichungen.bruch", "anteil_aus_verhaeltnis"),      # Schema (Summe der Teile)
    ("gleichungen.bruch", "fehler_aussen_innen"),         # Schema (Rezeptfehler)
    # Welle 2: übrige Einheiten
    ("zahlen.potenzen_zehner", "komma_ausgleich"), ("zahlen.potenzen_zehner", "passt_wie_oft"),
    ("zahlen.potenzen_zehner", "skalierung_rueckwaerts"), ("zahlen.potenzen_zehner", "minus_macht_negativ"),
    ("zahlen.potenzen_zehner", "umrechnen_wissenschaftlich"), ("zahlen.potenzen_zehner", "fehler_kette"),
    ("zahlen.potenzen_zehner", "normalisieren_ordnen"), ("zahlen.potenzen_zehner", "angleichen_richtung"),
    ("terme.potenzgesetze", "einsetzen_luecken"), ("terme.potenzgesetze", "umrechnen_bruch"), ("terme.potenzgesetze", "kleiner_als_grenze"),
    ("terme.potenzgesetze", "basis_mal_hochzahl"), ("terme.potenzgesetze", "vorzeichen_vergessen"),
    ("bruch.prozent", "fehler_komma"), ("bruch.prozent", "grundwerte_vergleichen"),
    ("bruch.prozent", "eins_prozent"), ("bruch.prozent", "fehler_multiplizieren"),
    ("messen.flaechen_vielecke", "zwei_dreiecke_parallelogramm"), ("messen.flaechen_vielecke", "formel_aus_koordinaten"),
    ("messen.flaechen_vielecke", "hoehe_aus_flaeche"), ("messen.flaechen_vielecke", "umstellfehler"),
    ("messen.flaechen_vielecke", "ergaenzen_vorzeichen"), ("messen.flaechen_vielecke", "zerlegen_rechnungen"),
    ("messen.flaechen_vielecke", "anteil_im_rechteck"), ("messen.flaechen_vielecke", "hoehen_ergaenzen"),
}
