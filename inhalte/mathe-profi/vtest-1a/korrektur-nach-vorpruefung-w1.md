# Korrektur nach Vorprüfung W1, Runde VT1A

Stand 29.11.2026. Ausgang: `vorpruefung-w1.md` (A 17, B 17, C 7) und der Maßstab aus Urteil 1222. Neue Menge nach Entscheidung des Nutzers: je Lernziel **5 Aufgaben** (1 Test, 2 Korrektur, 2 Sicherung), 11 Lernziele, **55 Aufgaben** (`VT1A-001` bis `VT1A-055`).

Prüfläufe: `bauen.py` OK; `gegenrechnung.py` 55 Sollantworten, 0 Abweichungen; `tools/vorrat_pruefen.py` 55 Aufgaben, 0 Meldungen; `tools/vtest_pruefen.py --runde 1a` nur die erwarteten 11 Pool-Meldungen „2 sicherung-Aufgaben, Soll 3“, sonst keine Fehler (8 Hinweise wie bisher: Abweichung vom Vorschlag, Rhythmus, 5-mal „Regel fehlt“ bei `ueberschlag`).

## Vorgehen

1. Je Lernziel den Streichvorschlag genommen und nur Aufgaben ohne A- und B-Befund behalten. Nach dem strengen Maßstab (Schema auch als Zahlenvergleich, Lücke, Fehler-Detektiv oder Auswahl, die man durch Ausrechnen der Optionen löst; im Zweifel Schema) blieben davon nur wenige übrig; die meisten früheren „Fehler: … Richtig wäre …“-Aufgaben sind durch Ausrechnen lösbar.
2. Vor jeder neuen Aufgabe alle Bestandsaufgaben des Lernziels gelesen (`inhalte/themen/<einheit>.json` alle Pools, `rollend-5`, `-11`, `-12`; `rollend-15` und die übrigen `rollend-*` enthalten keine Aufgaben dieser Einheiten). Zusätzlich die R-Lernziele `vertauschen` und `berechnen` (Potenzen), weil sich Inhalte überschneiden: Dabei fiel eine geplante Aufgabe („Basis und Hochzahl vertauschen – immer, manchmal, nie?“) heraus, weil sie Kern von `vertauschen` ist.
3. Neu gebaut nach den Bauplänen a–h; je Lernziel verschiedene Baupläne und 5 verschiedene Denkfiguren. Nächstliegender Bestandskern und Unterschied stehen je Aufgabe in `bestandsvergleich.md`.
4. `bauen.py` prüft jetzt fest: 1/2/2 je Lernziel, höchstens 1 Schema, Test kein Schema, mindestens 4 Denkfiguren und keine doppelt im selben Pool, Urteile je Aufgabe verschieden (alle Optionen untereinander), kein Bauart-Merkmal nur in der richtigen Option (=, ·, darf/muss/man, denn/weil, Nebensatz, Sammelwort, Absolutwort, Verneinung, kleiner/größer; ohne Groß-/Kleinschreibung), dazu die bisherigen Prüfungen (Länge, Lage, Anfangswörter, Merkmalsverteilung, Fehlbild-Rechnungen, Zahlen in Beschreibungen).

## Befund → geschlossen wie

### A

| Nr | Befund | geschlossen wie |
|---|---|---|
| A1 | Test 001 (schreibweise) bloßes Ausrechnen | 001 entfällt (Vorrat). Neuer Test VT1A-001: Welche von 4¹⁰, 8⁵, 32⁴, 1 024² ist ungleich 2²⁰ (Zweier zählen; Ausrechnen über eine Million unattraktiv). 006 nicht als Test übernommen: Der Fragetext verriet „man darf nicht vertauschen“, und der Kern gehört zum R-Lernziel `vertauschen` (Bestand „Gilt immer: Basis hoch Exponent = Exponent hoch Basis?“). |
| A2 | 005 = Bestand | gestrichen (nicht in den Vorrat). |
| A3 | schreibweise 4 Schema | Alle fünf neu: 001 (d), 002 Fehlregel „vertauscht“ (b), 003 Wirkung einer Änderung auf 3¹² (e), 004 Potenz gegen Basis · Hochzahl (f), 005 Geschichte zu 4³ (d, als Schema gezählt). Schema 1. |
| A4 | quadrat 3 Schema | 010, 011, 014 in den Vorrat; neu: 006 Rand rückwärts (Test), 007 Fläche bei verdreifachter Seite (Seite nicht natürlich), 008 Flächenbild (30 + 7)², 010 Anzahl zwischen Nachbarquadraten. 009 (Endziffer) bleibt als einziges Schema. |
| A5 | 027 = Bestand | gestrichen. |
| A6 | 016 = Bestand | gestrichen. |
| A7 | Test 029 (klammern) Schema und Bestand | gestrichen. Neuer Test VT1A-021: Wirkung einer Klammer in einer sechsstelligen Rechnung (e). Die vorgeschlagene 033 (überflüssige Klammer) war durch Ausrechnen der Optionen lösbar; ihre Einsicht steckt jetzt allgemein in VT1A-024 (Ketten, immer – nie). |
| A8 | 030 = Bestand | gestrichen. |
| A9 | 037, 038 Bestand; termaufbau 3 Schema | 037, 038 gestrichen, 039 in den Vorrat. Neu: 028 „ein Rechenzeichen ändern, damit ein Produkt entsteht“ (Vorschlag der Vorprüfung), 029 Fehlregel der Benennung, 030 „verschiedene Terme, gleicher Wert“ (Vorschlag der Vorprüfung). Schema nur 027 (früher 036). |
| A10 | 045 = Bestand | gestrichen. |
| A11 | 046 = Bestand | gestrichen. Vorschlag „umstellen, wenn jede Zahl ihr Zeichen mitnimmt“ umgesetzt als VT1A-034 (vier Regeln, f). |
| A12 | 047 = Bestand; vorteil 3 Schema | 047 gestrichen, 044 und 049 in den Vorrat. Neu: 031 Test □ · 37 · △ = 3 700 (zwei Lücken, alle Zerlegungen), 033 Ausgleich in falscher Richtung, 035 beide Faktoren durch 3 geteilt. 032 (früher 043) mit großen Zahlen. Schema 0. |
| A13 | Test 050 (verteilen) Schema und Bestand; Ausklammern viermal | 050 gestrichen, 051, 053, 055 in den Vorrat. Neuer Test VT1A-036: Welche Zerlegung von 368 · 47 stimmt nicht (beide Faktoren zerlegt). 054 nicht als Test (mit kleinen Zahlen ausrechenbar), sondern ohne Zahlen als Sicherung VT1A-040. Kein Ausklammern-Schema mehr. |
| A14 | 058 = Bestand | gestrichen. |
| A15 | 062 verbotene Ablenker | gestrichen. Die Lösbarkeit steckt im Test VT1A-041 (früher 057). |
| A16 | Test 064 (ueberschlag) Schema | 064 in den Vorrat. 068 nicht als Test: Auch nach B3 lassen sich nur drei verschiedene Urteile bilden (passt nicht / passt genau / es bleibt Platz). Neuer Test VT1A-046: Bei welcher von vier Fragen entscheidet ein Überschlag nicht sicher (h). |
| A17 | 065, 075 Bestand; sach (Rechengesetze) bündelt Rückwärtsrechnen | 065, 075 gestrichen, 072 in den Vorrat. Rückwärtsrechnen nur noch einmal (VT1A-053, als Fehlregel). Neu: 052 Rest deuten, 054 Reihenfolge der Schritte (immer um 6). |

### B

| Nr | Befund | geschlossen wie |
|---|---|---|
| B1 | Bauart-Muster (Regelwort/Rechnung) | Neue Optionen meist parallel gebaut (reine Terme, gleich gebaute Sätze). In `bauen.py` je Aufgabe: kein Merkmal nur in der richtigen Option; global die Merkmale „·“ und „darf/muss/man“ zusätzlich in der Verteilungsprüfung. Stand: „·“ richtige 0,21 / falsche 0,21; darf/muss/man 0,03 / 0,06; „=“ 0,06 / 0,06; denn/weil 0,09 / 0,10. |
| B2 | doppelte Urteile 018, 068, 028, 035 | Alle vier nicht in der Runde (018, 028, 035, 068 im Vorrat mit Vermerk). Prüfung in `bauen.py` jetzt auf „irgendwo doppelt“ (Urteil = Teil vor „Wort: “ oder vor „, denn/weil“, sonst ganze Option). |
| B3 | 068 Ablenker 0 teilweise wahr | 068 im Vorrat mit Vermerk; die Frage „wann entscheidet ein Überschlag sicher?“ ist im neuen Test VT1A-046 eigens gestellt. |
| B4 | 012 nahe Bestand | 012 im Vorrat; die Denkfigur „Zuwachs eines Quadrats rückwärts“ steckt mit anderem Modell (Rand, 4 · n + 4) im Test VT1A-006. |
| B5 | 025 nahe Bestand | Umgedreht: VT1A-018 „Zu welcher Geschichte passt 3 · 2⁵?“ (als Schema gezählt, Format Term ↔ Text). |
| B6 | 019 nahe Bestand | gestrichen. |
| B7 | Test 015 (zehner) ausrechenbar | 015 im Vorrat. Neuer Test VT1A-011: kleinstes □ mit □ · 10⁸ > 7 · 10¹¹ (Faktor und Hochzahl verrechnen, Grenze „größer, nicht gleich“). |
| B8 | 063 nahe Bestand | 063 im Vorrat (Vermerk). |
| B9 | 069, 070 nahe Bestand | 069 und 070 im Vorrat (Vermerk). |
| B10 | 074, 077 gleiche Zahlen und Denkfigur | beide im Vorrat. Reihenfolge der Schritte jetzt einmal vorwärts (VT1A-054) und einmal als falsche Umkehr-Reihenfolge (VT1A-053), mit verschiedenen Zahlen. |
| B11 | 053 nennt 108 | im Vorrat. |
| B12 | 049 Format „Rechne geschickt“ | im Vorrat. |
| B13 | 039, 073 Text → Term | beide im Vorrat. Text → Term kommt je Lernziel höchstens einmal vor und ist dann als Schema gezählt (VT1A-023 klammern, VT1A-055 sach). |
| B14 | 064 Doppelfrage | 064 im Vorrat. |
| B15 | 044 Text verrät den Weg | im Vorrat. |
| B16 | 008/014 gleiche Einzelfrage | beide im Vorrat; die Wirkung einer Seitenänderung steckt nur noch in VT1A-007 (verdreifachen, Seite nicht natürlich). |
| B17 | 004 Bestands-Tatsache | im Vorrat (Vermerk „Zahlen ändern“). |

### C

| Nr | geschlossen wie |
|---|---|
| C1 | 009 (jetzt VT1A-009): Fehlbilder nennen den vermuteten Denkfehler (Endziffer 6 für unmöglich gehalten, ungerade = keine Quadratzahl, Teilbarkeit durch 4). 016, 033, 037 nicht mehr in der Runde. |
| C2 | unverändert (Einsicht wie im Bestand, aber andere Leistung); 009 jetzt ehrlich als Schema gezählt. |
| C3 | „Kultur“ durch „Schale“ ersetzt (VT1A-020). |
| C4 | 060 nicht mehr in der Runde (Vorrat). |
| C5 | Regel fehlt bei `ueberschlag`: weiterhin kein Katalogeintrag; 5 Hinweise des Werkzeugs. |
| C6 | Bestand wie oben gelesen. |
| C7 | 055 nicht mehr in der Runde (Vorrat). |

## Zuordnung alt → neu

| alt | neu | Änderung |
|---|---|---|
| VT1A-009 | VT1A-009 | Fehlbild-Beschreibungen (C1), jetzt Sicherung und Schema |
| VT1A-022 | VT1A-020 | umgebaut: statt „nach wie vielen Stunden“ (Tabelle) Aussage über das langfristige Verhalten (f); „Schale“ statt „Kultur“ |
| VT1A-025 | VT1A-018 | umgedreht: Rechnung → Geschichte (B5) |
| VT1A-026 | VT1A-019 | 20 statt 4 Tage, damit Ausrechnen nicht geht |
| VT1A-036 | VT1A-027 | Optionstexte geglättet, jetzt Korrektur und Schema |
| VT1A-042 | VT1A-026 | große Zahlen, jetzt Test; Ablenker „um 9 kleiner“ statt „um 4 größer“ |
| VT1A-043 | VT1A-032 | große Zahlen, jetzt Korrektur; „Sie sind gleich groß“ statt „Beide …“ |
| VT1A-054 | VT1A-040 | ohne Zahlen, Höhe verdreifacht |
| VT1A-057 | VT1A-041 | dritter Ablenker (9) ergänzt |
| VT1A-061 | VT1A-043 | jetzt Korrektur, als Schema gezählt |
| VT1A-067 | VT1A-048 | richtige Option gekürzt, „Gleich gut sind sie“ statt „Beide …“, als Schema gezählt |
| VT1A-071 | VT1A-051 | Frage „ab wie vielen Gigabyte teurer“ statt „gleich teuer“ |
| VT1A-076 | VT1A-055 | unverändert, als Schema gezählt |
| 001–004, 007, 008, 010–015, 017, 018, 020, 021, 023, 024, 028, 031–035, 039–041, 044, 048, 049, 051–053, 055, 056, 059, 060, 063, 064, 066, 068–070, 072–074, 077 | Vorrat | `vorrat-folgerunde/<einheit>.json`, Kennung `VT1A-ALT-nnn`, Grund je Eintrag (47 Aufgaben) |
| 005, 006, 016, 019, 027, 029, 030, 037, 038, 045, 046, 047, 050, 058, 062, 065, 075 | gestrichen | Bestand-Doppelung (A2, A5–A14, A17, B6), verbotene Ablenker (A15) oder Antwort im Text (006) |

Alle übrigen 42 Aufgaben (VT1A-001–008, 010–017, 021–025, 028–031, 033–039, 042, 044–047, 049, 050, 052–054) sind neu.
