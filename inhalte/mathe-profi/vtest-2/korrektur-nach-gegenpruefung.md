# Korrektur nach Urteil 1222 (Runde 2, Verstehen in Tests)

Stand: Welle 1 (zahlen.natuerlich, terme.umformen) und die übrigen Einheiten im Code umgesetzt; Dokumentation der übrigen Einheiten folgt.

| Befund (Urteil 1222) | geschlossen wie |
|---|---|
| Schema zu günstig gezählt (mehr als zwei Routinen je Lernziel) | streng nachgezählt; Routinen durch Verstehens-Aufgaben ersetzt: 004, 012, 013, 023, 026 (Zinsen), 030, 035, 036, 040, 042 (umformen), 053, 061, 062 (umformen_teil2), 079, 080 (Kreis), 087, 090, 093, 098, 101, 104, 107, 112 (natürliche Zahlen) |
| Bestandsaufgaben 036 und 062 (gleiche Rechnung, gleicher Fehler) | 036: zwei Parameter per Koeffizientenvergleich (Test); 062: Unterschied zweier Terme als Term mit x |
| verbotene Ablenker (richtiges Urteil, falscher Grund) | 039, 069, 082, 117 neu gebaut: jede falsche Möglichkeit hat ein falsches Urteil; alle 43 Auswahl-Aufgaben durchgesehen |
| 063 Voraussetzung, 054 unpräzise | 063: x positiv vorgegeben; 054: Antwort präzisiert |
| 042, 116, 079 | 042 als Rückwärtsaufgabe; 116: Bedingung (voller Preis) genannt; 079 neu (Randfall 45°) |
| 067 verrät Radius von 064 | anderer Kontext, 14 cm |
| Tests nicht die schwersten | 070 und 118 im Test-Pool, 064 und 113 in der Sicherung |
| Lehrplan: 071–080 sind Ableitungen | Begriffe und Kriterium (Sekante/Tangente/Passante; Lage des Umkreismittelpunkts) in der Aufgabe eingeführt |
| Bauart-Muster | neue feste Prüfung in bauen.py („=“, „<“, „>“, kleiner/größer/gleich/nicht nur in der richtigen Möglichkeit: höchstens 10 %); Stand 0 |
| Bestandsvergleich inkl. Runde 15 | neue Kerne gegen Bestand geprüft; 090 wegen gleicher Ziffern geändert (0, 4, 6) |

Prüfungen: vtest_pruefen --runde 2 ohne Fehler, bauen.py ok, gegenrechnung 0 Abweichungen.
