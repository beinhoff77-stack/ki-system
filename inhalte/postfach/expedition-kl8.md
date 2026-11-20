# Postfach expedition-kl8 (Expeditionen Klasse 8, Werkstatt-Wunsch 176)

Neueste Meldung oben. Format: `inhalte/README.md`, Abschnitt „Expeditionen“. Je Expedition ein Generator `inhalte/generatoren/expedition_<name>.py`
(gemeinsame Helfer in `_exp8.py`), Prüfung mit `python3 -I tools/inhalt_pruefen.py inhalte/expeditionen/<datei>.json`.

## 2026-11-20 · FERTIG: Korrekturen 853

Umgesetzt im Zweig `expedition-kl8` (vorher auf den Stand von `lernen-app` gebracht). Nur Texte geändert, keine Rechnung, keine Lösung. Generatoren und JSON stimmen überein, `inhalt_pruefen.py --alle` ohne Fehler (alle Dateien OK). Nichts in die Datenbank geschrieben, kein Merge nach `main`.

**1. `8-radtour` (Muss) – Kilometerstein 36 ist Zwischenpunkt, See bei Kilometerstein 42**
- Teil c, alt: „Der Graph zeigt die Fahrt: Beim Start (0 Stunden) ist die Gruppe am Kilometerstein 6, nach 2 Stunden am Kilometerstein 36. Sie fährt gleichmäßig. Wie viele Kilometer schafft sie in einer Stunde?“
- Teil c, neu: „Die Route führt an einer Straße mit Kilometersteinen entlang. Sie beginnt am Kilometerstein 6; der See liegt am Kilometerstein 42 (6 km + 36 km Route). Der Graph zeigt die Fahrt: Beim Start (0 Stunden) ist die Gruppe am Kilometerstein 6, nach 2 Stunden kommt sie am Kilometerstein 36 vorbei – das ist ein Zwischenpunkt, noch nicht der See. Sie fährt gleichmäßig. Wie viele Kilometer schafft sie in einer Stunde?“
- Teil c, Lösungsweg ergänzt: „Die 30 km sind die ersten 30 der 36 km Route; bis zum See (Kilometerstein 42) fehlen noch 6 km.“
- Teil c, Grafik: zusätzlicher Punkt „See“ bei (2,4 | 42), dem Ende der eingezeichneten Geraden.
- Teil d, alt: „Die Gruppe startet um 9:00 Uhr und fährt die 36 km mit 15 km/h. …“
- Teil d, neu: „Die Gruppe startet um 9:00 Uhr am Kilometerstein 6 und fährt die ganze Route von 36 km bis zum See am Kilometerstein 42 mit 15 km/h. …“ (Rest unverändert)

**2. `8-pool` (Muss) – Segel passt nicht in den Kreis**
- Teil d, alt: „Es soll mindestens die Hälfte der Wasserfläche beschatten können (wenn es ganz über dem Wasser hängt). Reicht das Segel?“
- Teil d, neu: „Selbst wenn die gesamte Segelfläche Schatten auf das Wasser wirft: Ist das Segel groß genug, um mindestens die Hälfte der Wasserfläche zu beschatten?“
- Nebenbei, sprachlich: falsche Option alt „Ja, weil die Grundseite 4 m länger ist als der Durchmesser 3,6 m.“ → neu „Ja, weil die Grundseite mit 4 m länger ist als der Durchmesser von 3,6 m.“ (alt las sich wie „um 4 m länger“).

Nicht geprüft: wie die App den zusätzlichen Punkt „See“ beschriftet.

## 2026-11-18 · Abschlussbericht: 10 Expeditionen Klasse 8 (Zweig expedition-kl8)

**Ergebnis:** 10 neue Expeditionen, je 4 Teile, alle `inhalt_pruefen.py` = OK (Handytarif-Beispiel unverändert ebenfalls OK). Je Expedition ein Generator, ein Commit, gepusht. Kein Merge, keine Datenbank-, App- oder Server-Änderung.

| Expedition | Situation | Teile (Thema/Lernkarte) | Antwortformen | Grafik |
|---|---|---|---|---|
| 8-klassenfahrt | Bus 840 € geteilt, Herberge 28 €/Nacht, Budget 150 € | a) groessen.indirekt/sach · b) funktionen.linear/aufstellen · c) gleichungen.ungleichungen/sachaufgabe · d) bruch.prozent_grundwert/vermindert | zahl, luecken, zahl, auswahl | – |
| 8-kerzen | zwei Kerzen brennen unterschiedlich schnell ab | a) messen.volumen/quader · b) funktionen.grundbegriffe/funktionswert · c) gleichungen.ungleichungen/sachaufgabe · d) funktionen.linear/schnittpunkte | zahl, zahl, zahl, auswahl | d) koordinaten (2 Geraden) |
| 8-radtour | Radkarte, Fahrzeit, Zuganschluss | a) groessen.einheiten/massstab · b) groessen.indirekt/sach · c) funktionen.linear/zwei_punkte · d) gleichungen.ungleichungen/sachaufgabe | zahl, zahl, zahl, auswahl | c) koordinaten |
| 8-roller | du und Bruder sparen auf einen Roller | a) funktionen.grundbegriffe/wertetabelle · b) funktionen.linear/schnittpunkte · c) bruch.prozent/rabatt_aufschlag · d) gleichungen.ungleichungen/sachaufgabe | luecken, luecken, zahl, auswahl | a) tabelle |
| 8-garten | Trapezbeet, Pflanzreihen, Regentonne | a) messen.flaechen_vielecke/trapez · b) groessen.indirekt/produkt · c) funktionen.grundbegriffe/funktionswert · d) gleichungen.ungleichungen/sachaufgabe | zahl, zahl, zahl, auswahl | a) figur (Trapez) |
| 8-pool | runder Aufstellpool, Schläuche, Sonnensegel | a) messen.kreisberechnung/umfang · b) messen.prisma_zylinder/zylinder_volumen · c) groessen.indirekt/sach · d) messen.kreisberechnung/flaeche | zahl, zahl, zahl, auswahl | – |
| 8-schulfest | Glücksrad und Losbude | a) stochastik.grundbegriffe/laplace · b) stochastik.grundbegriffe/grosse_zahlen · c) gleichungen.lgs2/sachaufgabe · d) gleichungen.ungleichungen/sachaufgabe | luecken, zahl, luecken, auswahl | a) kreisdiagramm (12 Felder) |
| 8-saftbar | Schorle mischen, Fruchtgehalt, Preisvergleich | a) gleichungen.bruch/verhaeltnis · b) gleichungen.bruch/ein_bruch · c) gleichungen.lgs2/sachaufgabe · d) groessen.proportional/sach | zahl, zahl, luecken, auswahl | – |
| 8-zelt | selbst genähtes Firstzelt (Dreiecksprisma) | a) messen.koerper_darstellung/prisma · b) messen.prisma_zylinder/prisma_volumen · c) messen.prisma_zylinder/prisma_oberflaeche · d) gleichungen.ungleichungen/sachaufgabe | zahl, zahl, zahl, auswahl | b) figur (Giebeldreieck) |
| 8-schuelerzeitung | Druckkosten: Fixkosten + Stückkosten | a) terme.bruchterme/termwert · b) gleichungen.bruch/ein_bruch · c) funktionen.gebrochen/asymptoten · d) funktionen.linear/schnittpunkte | zahl, zahl, auswahl, auswahl | c) koordinaten (Hyperbel) |

**Abdeckung der frühen Themen** (Anzahl Expeditionen): gleichungen.ungleichungen 7 · funktionen.linear 5 · groessen.indirekt 4 · funktionen.grundbegriffe 3 – Vorgabe „mindestens zweimal“ erfüllt. Die ersten fünf (klassenfahrt bis garten) nutzen nur diese vier Themen plus Stoff Kl. 5–7. Jede Expedition hat 4 verschiedene Themen aus mindestens 2 Gebieten.

**Je Expedition ein Wortlaut (Auszug):**
- klassenfahrt c): „Ein Kind zahlt 28 € pro Nacht und einmal 30 € für den Bus. Es soll höchstens 150 € zahlen. Wie viele Nächte kann die Klasse höchstens bleiben?“ → 4
- kerzen d): „Beide Kerzen werden um 18 Uhr angezündet. … Jemand sagt: „Um 6 Uhr morgens sind beide Kerzen gleich hoch.“ Was stimmt?“ → stimmt, nach 12 h je 6 cm
- radtour d) (sinngemäß): Start 9:00, 45 min Pause → Ankunft 12:09, Zug verpasst; Pause höchstens 36 min.
- roller b): „Dein Guthaben nach x Wochen ist 60 + 15x Euro, das deines Bruders 150 + 6x Euro. Nach wie vielen Wochen habt ihr gleich viel Geld, und wie viel ist das?“ → 10 Wochen, 210 €
- garten d) (sinngemäß): Reicht der Wasservorrat 12 Tage, wenn mindestens 20 l Reserve bleiben sollen? → Ja, genau 20 l
- pool d): „Ein dreieckiges Sonnensegel hat eine 4 m lange Grundseite und ist 2,4 m hoch. Es soll mindestens die Hälfte der Wasserfläche beschatten können … Reicht das Segel?“ → Nein (4,8 m² < ≈ 5,09 m²)
- schulfest c): „Ein Los für Kinder 1 €, für Erwachsene 2 €. 180 Lose verkauft, 260 € in der Kasse. Wie viele Kinderlose und wie viele Erwachsenenlose?“ → 100 / 80
- saftbar c): „10 Liter mit 70 % Fruchtgehalt aus einem 40-%-Getränk und 100-%-Saft. Wie viele Liter von jeder Sorte?“ → 5 / 5
- zelt d): „5 Personen, je mindestens 1,5 m² Boden, Breite 2,4 m. Längen 3 m, 3,2 m, 3,5 m. Welche ist die kürzeste, die ausreicht?“ → 3,2 m
- schuelerzeitung d): „160 Vorbestellungen, E(x) = 1,5x, K(x) = 180 + 0,6x. Was sollte die Redaktion tun?“ → Mehr Vorbestellungen sammeln (36 € Verlust, Grenze 200)

**Gesichert (geprüft):**
- Jede Lösung im Generator nachgerechnet (Fraction); bei höchstens/mindestens alle Fälle per Schleife durchgegangen (klassenfahrt, kerzen, radtour, garten, zelt, schuelerzeitung).
- Checker: c-Ausdrücke nachgerechnet, jeder bezug ∈ voraussetzungen, alle voraussetzungen genutzt.
- Keine Folgefehler-Kette: jeder Teil nennt die Werte, die er braucht.
- Letzter Teil ist jeweils Entscheidung/Deutung (auswahl). Falsche Optionen enthalten keine wahren Teilfakten mit falscher Schlussfolgerung und keine falschen Rechnungen als Begründung.

**Annahmen:**
- Reihenfolge der Themen nach `themenliste.json`; alle Bezüge haben Planklasse ≤ 8.
- „du“/„dein Bruder“/„der Nachbar“ statt Namen.

**Nicht geprüft:**
- Wie die App die Grafiken zeichnet (Achsenteilung, Beschriftung, `schritt_x/y`, Hyperbel-`bereich`, Kreisdiagramm ohne Zahlen); geprüft ist nur, dass der Checker das Format annimmt.
- Realismus der Zahlen (Preise, Brenndauer, Schlauchleistung) nur nach eigenem Urteil, nicht gegen Quellen.
- Schwierigkeitsanstieg a)→d) nur nach eigenem Urteil, nicht an Kindern erprobt.

**Meinung:** pool d) und schuelerzeitung c) sind die anspruchsvollsten Deutungsteile. Ein Kind aus dem frühen Kl.-8-Stand schafft die ersten fünf ohne Lücken.

## STATUS (je Expedition eine Zeile)
- 8-klassenfahrt: OK – Teile und Themen siehe Abschlussbericht.
- 8-kerzen: OK – Teile und Themen siehe Abschlussbericht.
- 8-radtour: OK – Teile und Themen siehe Abschlussbericht.
- 8-roller: OK – Teile und Themen siehe Abschlussbericht.
- 8-garten: OK – Teile und Themen siehe Abschlussbericht.
- 8-pool: OK – Teile und Themen siehe Abschlussbericht.
- 8-schulfest: OK – Teile und Themen siehe Abschlussbericht.
- 8-saftbar: OK – Teile und Themen siehe Abschlussbericht.
- 8-zelt: OK – Teile und Themen siehe Abschlussbericht.
- 8-schuelerzeitung: OK – Teile und Themen siehe Abschlussbericht.
