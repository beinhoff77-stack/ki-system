# Korrektur nach Urteil 1222 (Runde 2, Verstehen in Tests)

Befund (nur als Urteil 1222 bezeichnet) → geschlossen wie. Prüfungen: `vtest_pruefen --runde 2` ohne Fehler, `bauen.py` ok, `gegenrechnung.py` 0 Abweichungen.

## Muss

| Befund | Kennung | geschlossen wie |
|---|---|---|
| Voraussetzung fehlt | 063 | x ist als positive Zahl vorgegeben; der Umfang 12x + 8 braucht keinen Betrag |
| Aussage zu ungenau | 054 | richtige Möglichkeit präzisiert: kein gemeinsamer ganzzahliger Faktor über 1 und kein gemeinsames x |
| Bestandsaufgabe (gleiche Rechnung, gleicher Fehler, gleiche Zeilensuche) | 036 | neuer Kern im Test: (ax + 5) − (3x − b) ≡ 2x + 9, a und b durch Koeffizientenvergleich |
| dasselbe | 062 | neuer Kern: Unterschied von (x + 3)² und x² + 9 als Term (24 und Zahl 6) |
| verbotene Ablenker (richtiges Urteil mit falschem Grund) | 039, 069, 082 | neu gebaut; jede falsche Möglichkeit hat ein falsches Urteil mit eigener Begründung |
| alle Auswahl-Aufgaben prüfen | 43 Auswahlaufgaben | alle gelesen; zusätzlich 117 neu gebaut („Mia hat recht“ ×3 mit je eigener Begründung) |
| Schema zu günstig gezählt | siehe README, Punkt 5 | streng neu gezählt (im Zweifel Schema); insgesamt 23 Routinen ersetzt: 004, 012, 013, 023, 026, 030, 035, 036, 040, 042, 053, 061, 062, 079, 080, 087, 090, 093, 098, 101, 104, 107, 112; Zählung je Lernziel mit Kennungen in der README |

## Soll

| Befund | Kennung | geschlossen wie |
|---|---|---|
| 042 | 042 | Rückwärtsaufgabe mit Minusklammer (Gleichung lösen), nicht mehr Schlüsselwort-Aufgabe |
| Voraussetzung nennen | 116 | „Jeder Besucher hat eine Karte zum vollen Preis von 15 € bezahlt (keine Ermäßigung, keine Freikarten)“ |
| 079 | 079 | neuer Kern: gleichschenkliges Dreieck, Umkreismittelpunkt außen, größtes ganzzahliges α (Randfall 45°) |
| 067 verrät Radius von 064 | 067 | Kontext gewechselt: Dreieck PQR mit PQ = 14 cm; 064 hat andere Zahlen und Aufgabentyp |
| Tests nicht die schwersten | 064/070, 113/118 | 070 (drei Winkel) wird Test, 064 Sicherung; 118 (Rundungsbereich geteilt) wird Test, 113 Sicherung |
| Lehrplan Ableitungen | 071 bis 080 | Begriffe (Sekante, Tangente, Passante) und das Kriterium Abstand gegen Radius bzw. Lage des Umkreismittelpunkts stehen in der Aufgabe selbst; Thales samt Umkehrung, Tangente, Um-/Inkreis sind M7.5 |
| Bauart-Muster | alle Auswahl | neue feste Prüfung in `bauen.py`; 13 Aufgaben (004, 019, 023, 026, 032, 039, 054, 059, 061, 064, 072, 105, 129) mussten umgebaut werden, jetzt 0 |
| jede Lücke mit eigenem Fehlbild | 013, 036, 062, 080, 107 u. a. | geprüft von `bauen.py` und `vtest_pruefen` |
| Bestand einschließlich rollend-15 | alle neuen Kerne | Nachtrag in `bestandsvergleich.md`; 090 wegen gleicher Ziffern auf 0, 4, 6 geändert |

## Offen

- Schema nach strenger Zählung noch über zwei in 14 Lernzielen (README, Punkt 5); zahlen.natuerlich und terme.umformen bis zum Ergebnis der unabhängigen Vorprüfung unverändert.
- 042 und 093 teilweise nah am Bestand.
