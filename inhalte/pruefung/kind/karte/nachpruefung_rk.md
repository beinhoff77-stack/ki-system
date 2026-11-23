# Prüfung RK-App – Reisekarte, App 0.92.0 (Zweig lernen-app, c41a3d5), 23.11.2026

Geprüft gegen `kind/karte/umsetzung.md` §1–11 (mit Nachträgen „wieder offen“ aus `kind/karten/umsetzung.md` §1) und `kind/expedition/umsetzung.md` §7. Grundlage Meldung `bau-motivation.md` „FERTIG: RK-App (0.92.0)“. Code `lernen.js` (`lernReisekarte`, `lernRkStart`), Karten `karte/`. **400 × 860, 820 × 1180, 1280 × 800, Tag und Nacht**; Maus und nachgestellter Finger (Zeiger-Ereignisse der Testsuite); Testkind, erfundener Stand auf den echten Reise-Aufbau-Daten (nachgestellter Server `rkServer`). Bilder: `nachpruefung/` (eigene), `docs/previews/la/rk-*.png`.

**Tests:** 7 RK-App- und 5 EX-App-Tests grün (`node --test --test-name-pattern="RK-App|EX-App"`).

## Erfüllt (nachgestellt)
1. **Ebenen:** Start im Kontinent des aktuellen Flugs (Europa), Pfad `WELT 🌍 Welt › KONTINENT Europa 📍` bzw. `… › LAND Italien 📍`, `📍 Zu mir`, Kontinent antippen → Kontinent, Ziehen/Rad/+ − ⤢/Zwei-Finger (Test).
2. **Zeichensprache:** Flaggen-Pin (Kopf Flagge, Spitze Hauptstadt), Schild LAND + *Hauptstadt*, graue Nadeln ohne Flug, Abzeichen ✓/★/Platz/✈/+; Städte als nummerierte Haltestellen, Kür gestrichelt, „hier bist du“ blau mit Puls.
3. **Startknopf:** schwebend unten (Handy/Tablet), rechte Spalte (Rechner); Ziel aus derselben Rechnung wie die Tafel (`lernRkStart`: Test weitermachen → Flug-Test → Wiederholungen/Check-in mit Ansage → Üben). Offene Expedition darüber, „Gerade dran“ schmal.
4. **Linien:** Bögen, geflogen grün / kommt gelb gepunktet, Reihenfolge nach Plan, keine Straßen.
6. **Teile/Zusatz:** `1/2`, Kette, Blatt mit Teil-Links; Zusatz `+`, eigene Zählung. **Antarktis:** Stationen nach Lage, geschafft/frei/gesperrt, `Expeditionen · 0 von 21 Stationen`.
7. **Abflugtafel-Schalter** hin und zurück (je Kind gemerkt); Quellen an der Karte (`Karte: Natural Earth · Orte: GeoNames (CC BY 4.0)`, Welt zusätzlich COMNAP) und auf der Info-Seite; `karte/LIZENZEN.md`.
9. **Ladezeit (nachgestellt, lokal, ohne echten Server):** Seite bis zum ersten Pin 640–850 ms; Dateigrößen wie gemeldet (Europa 72 KB gepackt). Echter Server nicht messbar.

## Abweichungen

### Muss
- **M1 – „wieder offen“ wird als gelandet gezeigt (nachgestellt, Land-Ebene 400/1280).** Eine Stadt mit Stand `wieder_offen` (Testdaten: Neapel) bekommt das Zeichen **✓** (wie gelandet) plus ein kleines `↻`; Text (Vorleser/Blatt) `heute wiederholen` (`LERN_RK_STADT.wieder_offen`, Zeichen-Zeile `zst === 'wieder_offen' ? '✓'`). Das sagt dem Kind „gelandet, nur wiederholen“ – tatsächlich ist die Etappe **nicht mehr gelandet** und muss nachgebessert werden (Entscheidung 23.11., 02:54; Vorgabe Karte §4 Stadt + Karten §1). **Änderung:** eigener Zustand: Haltestelle orange `#C8642B` mit `↻` (kein ✓), gestrichelter Ring, Unterzeile `wieder offen`; Vorleser/Blatt `wieder offen – nachbessern`; Land-Pin zusätzlich oranges `↻`-Abzeichen; Legende `↻ wieder offen – nachbessern`. Ein **„heute fällig“** (gelandet, Wiederholung heute) bleibt davon getrennt: ✓ grün + kleines gelbes `↻`. Bild `nachpruefung/1280-land.png`.

### Soll
- **S1 – Rechner: Karte klein im schmalen Seitenrahmen (1280 × 800).** Karte etwa 440 × 370 px, rechts die Spalte, alles in der Inhaltsbreite (~900 px) unter App-Kopf, „Lernreise Kind A“, Menü-Knopf und „Meine Reise“-Zeile. Vorgabe §1: Karte volle Breite/Höhe, rechts 360-px-Spalte. **Änderung:** Reisekarte wie „Unser Lehrplan“ (LW-3b) fensterfüllend: Kopf eine Zeile (Zurück · Meine Reise · Pfad · Abflugtafel · ★), Karte bis zum unteren Rand. Bild `1280-tag-kontinent.png`.
- **S2 – Handy: Karte zwischen Kopf und schwebender Karte nur ~40 % des Bildschirms (400 × 860).** Über der Karte: „Lernreise Kind A“-Leiste, Menü-Knopf, „Meine Reise · Abflugtafel · ★“, Pfad + „Zu mir“ (~240 px); unten die schwebende Karte (~230 px). **Änderung:** eine Kopfzeile `‹ · Pfad · ★ · ≡` (Abflugtafel und „Zu mir“ als Symbole: `▤`, `📍`), schwebende Karte kompakter (eine Zeile `Bologna in Italien · 3/6` + Knopf). Mit offener Expedition (Bild `docs/previews/la/rk-expedition-400.png`) bleiben nur ~120 px Karte: Expeditions-Karte auf der Reisekarte **einzeilig** `⛯ Expedition freigeschaltet: Die Wetterstation · Starten ›`, groß erst beim Antippen (EX §3 erlaubt die schmale Form für „Gerade dran“; hier für beide).
- **S3 – „4/13“ neben „Stadt 5 von 13“ verwirrt (alle Größen).** Die schwebende Karte zeigt rechts `4/13` mit 13 Strichen und die Haltestelle `Bologna · 4/13` – gemeint sind gelandete Städte; Vorgabe §1/§4: rechts **Aufgaben der aktuellen Stadt** `3/6` mit 6 Strichen, Haltestelle `Bologna · 3/6`. Ein Kind liest „Stadt 5 von 13“ und „4/13“ als Widerspruch. **Änderung:** rechts `x/6` (Bordkarten dieser Stadt), Städte-Stand nur im Text `Stadt 5 von 13`.
- **S4 – Land-Ebene: Ausschnitt nicht auf die Route, Städtenamen fehlen (400/1280).** Italien wird ganz gezeigt, die Städte 6–13 drängen sich im Norden; Namen fehlen bei Mailand, Turin, Verona, Genua, Florenz, Siena (nur Nummern), 1–4 überdecken sich bei Rom/Neapel (gemessen: `✓ × ✓`, `↻ × Neapel`). Vorgabe §2/§6: Start auf die Städte-Route eingezoomt; Haltestellen mit Namen, Überdeckung auflösen. **Änderung:** Einstieg = Rahmen um die Städte (+ Rand), Namen nach Vorrang (hier bist du, nächste 3, gelandete) statt alles oder nichts; bei Überdeckung Name seitlich versetzen statt weglassen. Bild `400-land.png`, `1280-land.png`.
- **S5 – Welt auf dem Handy ganz herausgezoomt, 14 Überdeckungen (400).** Kontinent-Namen, Gebiete und „x/y Länder“ liegen übereinander (`ASIEN × ORIENT`, `2/13 Länder × NORDAMERIKA` …). Vorgabe §6: Welt auf dem Handy startet als Ausschnitt um den aktuellen Kontinent. **Änderung:** Einstieg Welt = Ausschnitt um den aktuellen Kontinent; Zeile „x/y Länder“ erst ab einer Zoomstufe; Orient-Beschriftung versetzen. Bild `400-welt.png`.
- **S6 – Blatt bleibt beim Wechsel in die Land-Ebene offen (400).** Nach `Städte in Italien ansehen ›` steht das Länder-Blatt „Italien“ weiter unten über der schwebenden Karte und verdeckt „Gerade dran“. **Änderung:** Blatt beim Ebenenwechsel schließen. Bild `400-land.png`.
- **S7 – Zusatz-Text (Rückfrage Bau-Chat 1): Empfehlung `Zusatz für Entdecker – muss nicht sein.`** ohne „freiwillig“ (gleiche Regel wie Expeditionen und Prüfung EX S2). Eingeplanter Zusatz nach Vorgabe Karten §3: `Zusatz · eingeplant · x/y` und `Extra-Flug, von deinen Eltern eingeplant`.

### Kann
- **K1 – Pulsierender Pin ist ein bewegtes Ziel:** Antippen des aktuellen Pins scheitert in der Testsuite an „nicht stabil“ (Puls verändert den Umriss). Für Finger meist egal; Puls als eigenes Element **unter** dem Knopf-Bereich, Trefferfläche fest (≥ 44 px).
- **K2 – Kette der Teile in Afrika kräftig schwarz gestrichelt** (Bild `docs/previews/la/rk-teile-1280.png`): laut §11 „feine graue Linie unter der Route“. Dünner, grau, 50 % Deckkraft.
- **K3 – Hauptstadt-Pin überdeckt die erste Haltestelle** (Rom), Land-Ebene: Pin um 20 px seitlich oder in der Land-Ebene nur das `◉`-Zeichen.
- **K4 – Daten fehlen (Rückfrage Bau-Chat 2):** „gesperrt“ (Visum/ab Klasse) und „abgelegt“ je Stadt kommen nicht vom Server – 🔒 und Stadt-★ fehlen deshalb. Bitte als Datenauftrag an `bau-lehrer` (Felder in `schule_reise_karte`), App-Seite ist vorbereitet.
- **K5 – Datumsgrenze (Rückfrage 3):** Pazifik/Asien am Weltrand – in Ordnung, solange der Kontinent richtig zentriert ist.

## Frage 8 – versteht ein Kind es in drei Sekunden?
Teilweise. Klar: „GERADE DRAN · Bologna in Italien“ und der gelbe Knopf; die Pfad-Zeile mit 📍. Unklar: „4/13“ (S3), der kleine Kartenausschnitt auf dem Handy (S2), Nummern ohne Namen in der Land-Ebene (S4), und dass eine wieder offene Stadt wie gelandet aussieht (M1).

## Nicht geprüft
Echter Server und echte Ladezeit, echte Geräte und echter Finger, „weniger Bewegung“ nur per Test.

FERTIG: Prüfung RK-App (0.92.0) – 1 Muss (wieder offene Stadt als ✓ gelandet gezeigt), 7 Soll, 5 Kann.
