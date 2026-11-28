# Korrektur nach der Gegenprüfung (Urteil 1222), Runde VT1A

Stand: 77 Aufgaben; `bauen.py` OK, `gegenrechnung.py` 0 Abweichungen, `tools/vtest_pruefen.py --runde 1a` ohne Fehler (10 Hinweise wie bisher). Der Bestand mit den 207 Aufgaben aus `rollend-15` ist im Kernvergleich enthalten (`bauen.py` liest alle `rollend-*`-Ordner, `tools/vtest_pruefen.py` prüft die Ähnlichkeit zum Bestand).

## Befund → geschlossen wie

| Befund | Geschlossen wie |
|---|---|
| Ablenker mit richtiger Folgerung, nur falscher Begründung: 014, 049, 001, 048, 053 | 001 ist jetzt eine Frage nach dem Wert (17, 12, 3 125, 13), jede Option nennt einen anderen Wert. 014: jede Option nennt ein anderes Ergebnis (doppelt, 5 cm² Unterschied, 100 cm² mehr, 4-mal). 049 (jetzt 043, Test): Ablenker haben andere Urteile (größer, größer, nur durch Ausrechnen entscheidbar). 048 ist als Fehler-Aufgabe entfallen (neue Zahlaufgabe). 053: Frage nach dem richtigen Ergebnis; Ablenker „Nur Anna“, „Nur Ben“, „Weder noch“. |
| Alle Auswahl-Aufgaben darauf prüfen | Maschinell in `bauen.py`: kein Ablenker mit gleichem Urteil (erster Satzteil) wie die richtige Option; bei „Fehler:“-Optionen keine gleiche Berichtigung. Von Hand: alle 39 Auswahl-Aufgaben gelesen, Handliste in `sonderfaelle.md`. |
| 045/046/048 derselbe Schritt | 045 bleibt (geschickten Weg wählen). 046 neu: Gegenbeispiel zum Vertauschen (nur Teilen widerlegt). 048 neu: gegenläufig ändern (18 · 27 = 6 · □). |
| 072/076 gleicher Rückwärtsweg | 076 neu als Modellwahl: vier Gleichungen zur Geschichte mit je eigenem Ergebnis; erst wer das richtige Modell wählt, kommt auf 25. 072 bleibt als Zahlaufgabe. |
| Test 043 erlaubt bloßes Ausrechnen; 049 verlangt mehr | Neuer Test 043 (Vergleich ohne Ausrechnen); die frühere Zahlaufgabe 043 ist jetzt 049 (Sicherung, Stufe 3). |
| Test 022 weniger anspruchsvoll als 027 | Getauscht: 022 ist jetzt der Wachstumsvergleich (zwei Wege), 027 die Rückwärtsrechnung. |
| Alle 11 Lernziele auf die anspruchsvollste Aufgabe im Test geprüft | Getauscht außerdem: 057 (Test) ist die Teiler-Aufgabe, 063 die Kettenrechnung; 071 (Test) der Tarifvergleich, 075 die Kettenrechnung; 050 (Test) neu: 36 · 99 − 36 · 9 geschickt. 001 und 043 neu aufgebaut. Übrige Tests (008, 015, 029, 036, 064) bleiben; in ihren Lernzielen gibt es keine anspruchsvollere Sicherungsaufgabe. |
| Schema streng gezählt | In den vier Lernzielen mit drei Schema-Aufgaben je eine Routine ersetzt: schreibweise 004 (Exponent suchen → □⁴ = 2⁸), quadrat 009 (Nachbar-Quadratzahl → Endziffer-Argument), vorteil 046 und 048, sach (Rechengesetze) 076. Die Zählung der Gegenprüfung kenne ich nur als Zahlen je Lernziel, nicht je Aufgabe; welche Aufgabe sie je als Schema zählt, habe ich nach eigenem Urteil bestimmt (bloßes Ausrechnen, Zahlenvergleich, Fehler-Detektiv, den man durch Rechnen löst). |
| Mindestens 5 verschiedene Denkfiguren je Lernziel | `bauen.py` verlangt mindestens 5 `idee`-Werte je Lernziel und höchstens 2-mal denselben; siehe Tabelle unten. |
| 003 Personen gegen Ahnenplätze | Text: „alle diese Vorfahren sind verschiedene Personen“, gefragt wird nach verschiedenen Personen. |
| 068/069 plausiblere Fehlvorstellungen | 068: Ablenker „nur die Aufrundung von 48 gesehen“, „Rundungen gleichen sich aus“, „Überschlag prüft keine Grenze“. 069: „Überschläge sind nutzlos“ ersetzt durch „auf 500 abrunden“. |
| Bauart-Muster „genau eine Option mit =“ | Beseitigt in allen betroffenen Aufgaben und fest geprüft. |
| Länge, denn/weil, Nebensatz, Sammel-Optionen, Absolutwörter, höchstens/mindestens, Verneinung, kleiner/größer, Platz | Fest in `bauen.py` geprüft (Liste in `sonderfaelle.md`); Platz der richtigen Antwort jetzt aus einer festen, gleichmäßigen, unregelmäßigen Folge (`kern.py`, Saat 3). |
| Fehler-Detektive mit unregelmäßiger Fehlerzeile | Es gibt keine Fehler-Detektiv-Aufgabe mit nummerierten Zeilen in der Runde. |
| Jede Lücke mit eigenem Fehlbild | Es gibt keine Lückenaufgaben; jede Zahl- und Auswahlaufgabe hat Fehlbilder. |
| Antwort nie im Text | `bauen.py` prüft bei Zahlaufgaben, dass ein Ergebnis ab 10 nicht im Fragetext steht. |

## Schema und Denkfiguren je Lernziel (Kennung, Idee; Z = Zahl, A = Auswahl; t = Test)

| Lernziel | Aufgaben |
|---|---|
| schreibweise | 001 begruenden_fehlvorstellung (A, t), 002 was_waere_wenn, 003 situation_potenz, 004 potenz_umschreiben, 005 bedeutung_lesen, 006 gleiche_werte_begruenden, 007 fehler_richtigstellen |
| quadrat | 008 umfang_flaeche (t), 009 endziffer_quadratzahl, 010 differenz_quadrate, 011 flaeche_aus_termen, 012 reihe_spalte, 013 aussage_pruefen, 014 was_waere_wenn |
| zehner | 015 groessenvergleich (t), 016 schreibweise_erkennen, 017 umrechnen_potenz, 018 darstellung_wechseln, 019 kette_rueckwaerts, 020 fehler_richtigstellen, 021 parameter_groesste_hochzahl |
| sach (Potenzen) | 022 vergleich_wachstum (t), 023 exponent_suchen, 024 moeglichkeiten_zaehlen, 025 situation_term, 026 was_waere_wenn, 027 wachstum_rueckwaerts, 028 fehler_richtigstellen |
| klammern | 029 ziel_herstellen (A, t), 030 klammer_luecke, 031 darstellung_term_text, 032 klammern_wirkung_extrem, 033 klammer_weglassen, 034 gleiche_werte_zaehlen, 035 fehler_richtigstellen |
| termaufbau | 036 terme_zur_geschichte (A, t), 037 term_struktur, 038 und 039 term_aufstellen, 040 umkehr_tarif, 041 parameter_gleich, 042 was_waere_wenn |
| vorteil | 043 gleicher_wert_begruenden (A, t), 044 subtraktion_verbinden, 045 geschickten_weg_waehlen, 046 gegenbeispiel_vertauschen, 047 luecke_rechenvorteil, 048 gegenlaeufig_aendern, 049 erlaubte_umformung |
| verteilen | 050 ausklammern_geschickt (t), 051 luecke_ausklammern, 052 situation_zu_term, 053 zwei_wege_vergleichen, 054 was_waere_wenn, 055 geschickten_weg_waehlen, 056 fehler_richtigstellen |
| umkehraufgabe_mal | 057 parameter_teiler (t), 058 und 060 gleichung_waehlen, 059 zahlen_suchen, 061 geschichte_zu_gleichung, 062 begruenden_loesbarkeit, 063 kette_rueckwaerts |
| ueberschlag | 064 kontrolle_ueberschlag (t), 065 und 070 rundungsfenster, 066 richtung_ueberschlag, 067 zwei_ueberschlaege_vergleichen, 068 ueberschlag_entscheidung, 069 fehler_richtigstellen |
| sach (Rechengesetze) | 071 gleichsetzen (t), 072 gesamt_teil_anzahl, 073 gleichung_aufstellen, 074 reihenfolge_vertauschen, 075 kette_rueckwaerts, 076 modellwahl_gleichung, 077 aussage_pruefen |

Antwortformen jetzt: 39 Auswahl, 38 Zahl, 0 Lücken; Test-Pool: 4 Auswahl (001, 029, 036, 043) von 11.

## Offen

- Die Schema-Zählung der Gegenprüfung je Aufgabe ist mir unbekannt; eine erneute Zählung kann andere Aufgaben als Schema werten (z. B. 001, 002, 003 oder 010).
- Die neuen Aufgaben (001, 004, 009, 014, 043, 046, 048, 050, 053, 076) sind nur von mir und von `gegenrechnung.py` geprüft, nicht von einer unabhängigen Vorprüfung.
- Die Prüfung „gleiches Urteil“ ist eine Heuristik (erster Satzteil); sie sieht nicht jede richtige Folgerung mit falscher Begründung. Dafür gibt es die Handliste.
