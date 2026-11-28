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
}
