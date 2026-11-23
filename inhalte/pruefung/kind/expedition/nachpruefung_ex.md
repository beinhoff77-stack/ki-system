# Prüfung EX-App – Kinderseite Expeditionen, App 0.91.1/0.91.2 (Zweig lernen-app, 600609c), 23.11.2026

Geprüft gegen `kind/expedition/umsetzung.md` §1–6, 8, 9. Grundlage Meldung `bau-motivation.md` „FERTIG: EX-App (0.91.0)“. Stand des Zweigs beim Holen: 600609c (APP_VERSION 0.91.2, enthält f0a4e4e). Code `lernen.js`. **400 × 780, 820 × 1180, 360 × 640**, Tag und Nacht, Testkind und erfundene Daten (nachgestellter EX-S-Server der Testsuite). Bilder: `nachpruefung/` (eigene), `docs/previews/la/ex-*.png` (Bau-Chat).

**Tests:** alle 5 EX-App-Tests und die 3 W176-T4-Tests grün (`node --test --test-name-pattern="EX-App|W176 T4" tests/lernen.test.cjs`).

## Erfüllt (nachgestellt)
1. **Ansicht 1 „Expedition freigeschaltet“:** Szene Polarnacht, `ANTARKTIS · STATION 9 VON 21`, `EXPEDITION FREIGESCHALTET`, Satz mit Voraussetzungs-Chips, Blatt `★ 150` / `★ 200, wenn alle Teile im ersten Versuch ohne Tipp klappen`, Stempel-Vorschau, großer Knopf `Jetzt starten` / `Teil a von 3 · etwa 10 Minuten`, kleines `Später`. Nach der auslösenden Landung führt der Landungs-Knopf zuerst hierher; „Später“ dorthin, wohin er geführt hätte (Test). 400 × 780 ohne Scrollen.
2. **Abflugtafel:** offene Expedition als größte Karte vor der Abflugtafel, `NEU` nur am Tag des Freischaltens, ✕ = Später, Einsteigen-Knopf bleibt sichtbar. Nach „Später“ Chip `⛯ Expedition wartet: Die Wetterstation ›`. **Nächster Lerntag** (angeboten gestern, nicht mehr ausgeblendet): große Karte wieder vorn, ohne `NEU` (Bild `400-2-naechster-tag.png`).
3. **„freiwillig“ bei Expeditionen:** auf Abflugtafel, Ansicht 1, in der Expedition und im Abschluss nirgends (geprüft auf dem ganzen `main`-Text).
4. **Ansicht 3:** 3a `EXPEDITION GESCHAFFT` · `★ +150` · `1 / 21 Stationen in deiner Sammlung` · Hinweis auf 200; 3b `FEHLERFREI DURCHGEKOMMEN` · `★ +200` · `150 für die Expedition + 50 fürs fehlerfreie Lösen` · Stempel mit Band `★ FEHLERFREI`; Sterne vom Server; gelber Knopf `Weiter in Rom` / `Natürliche Zahlen · Etappe 3 von 4`; `Stempel-Sammlung ansehen`; `Überspringen ›`.
5. **Sammlung:** `REISEPASS · EXPEDITIONEN` · `Antarktis` · `0 von 21 Stationen · 1 freigeschaltet`, Gruppen je Klasse, ein Platz je Station mit ganzem Kurznamen, gesperrt antippen → Blatt `STATION 8 VON 21 · GESPERRT` · `Noch 3 Etappen, dann ist sie frei:` · fehlende fett mit Flug · `Diese Etappen sind noch nicht in deinem Plan.` · `★ 150 · ★ 200 ohne Fehler`.
6. **Abbruch und Fortsetzen:** Karte `Weiter mit Teil b` / `Teil b von 3 · etwa 10 Minuten`, Kästchen a grün; in der Expedition steht Teil a mit Lösung, es geht bei `TEIL B VON 3` weiter; `Du kannst jederzeit aufhören – erledigte Teile bleiben gespeichert.`; `Zum Flug: weiter in Rom ›` (sperrt nichts).

## Abweichungen

### Muss
– keine –

### Soll
- **S1 – 360 × 640: Voraussetzungs-Chips in Ansicht 1 verdeckt (nachgestellt).** Chip 3 („Ganze Zahlen dividieren“) liegt halb unter dem Schnee-Boden, Chip 4 („Mit Zeit rechnen“) ganz unter dem Blatt; die Szene scrollt nicht (Mausrad im Blatt ohne Wirkung). Vorgabe §9: „360 × 640 mit Blatt scrollbar“. **Stelle:** Ansicht 1 (`lr-ex-frei`, Szene/Blatt-Aufteilung). **Änderung:** unter 700 px Höhe höchstens 2 Chips + `+2 weitere`, oder die Szene oben mitscrollen lassen; Boden-Bild darf Chips nicht überdecken. Bild `nachpruefung/360-1-freigeschaltet.png`.
- **S2 – „freiwillig“ steht noch auf der Kinderseite – bei den Knobel-Bordkarten (gelesen im Code, Frage 3).** `lernKnobelAngebot` (Knopf `★ Knobel-Bordkarte (freiwillig)`), `lernKnobelDesTages` (`Knobeln (freiwillig)`), `lernAbschlussEtappe` (Link `Knobel-Bordkarte (freiwillig)`), Info-Text in `lernEinstellungen`/Kontoseite (`Knobel-Bordkarten sind freiwillig und richtig schwer`). Die EX-Vorgabe verlangt das Verbot nur bei Expeditionen – erfüllt. Gilt die Regel für die ganze Kinderseite, dann: **Änderung:** `★ Knobel-Bordkarte – für Profis` / `Knobeln für Profis` / Satz `Knobel-Bordkarten sind richtig schwer. Löst du eine beim ersten Versuch, …`. Eltern-/Lehrer-Seiten (`viewKindLehrplan` „freiwillig“ bei Kür-Etappe, Lernpfad) bleiben.

### Kann
- **K1 – Begonnene Expedition: Kopf heißt weiter `⛯ EXPEDITION FREIGESCHALTET`** – auf der Karte und als Seitenkopf in der Expedition. **Änderung:** begonnen `⛯ EXPEDITION · TEIL B VON 3`; in der Expedition selbst `⛯ EXPEDITION`. Bild `400-6a-begonnen-karte.png`, `400-6b-expedition-fortsetzen.png`.
- **K2 – Über der Expeditions-Karte stehen noch die Stand-Kacheln** (`GYM 5 0/1 gelandet · RS 5 keine Flüge · noch kein MYP-Jahr`). Die Karte ist damit nicht wörtlich „oberste“. **Änderung:** Kacheln unter die Abflugtafel oder in „Mein Schuljahr“ (Vorgabe Karten §2) überführen.
- **K3 – „Einmal je Kind und Expedition“ (Ansicht 1) nur auf dem Gerät gemerkt** (`lern.exfrei.<kind>.<id>`). Auf einem zweiten Gerät erscheint die Ansicht noch einmal. **Änderung:** Server-Feld „gesehen am“ (EX-S Nachtrag), App liest es.
- **K4 – Stationsnummer:** Daten sagen Wetterstation = Station 9, meine Vorgabe-Bilder zeigen 4 (dort nur Beispiel). Kein Fehler; Bilder gelten nur als Beispiel.

## Nicht geprüft
Echter Server (EX-S), echte Geräte, „weniger Bewegung“ visuell (nur Test), Reisekarte §7 (folgt mit RK-App).

FERTIG: Prüfung EX-App (0.91.1) – 0 Muss, 2 Soll (360×640 Chips verdeckt; „freiwillig“ noch bei Knobel-Bordkarten), 4 Kann.
