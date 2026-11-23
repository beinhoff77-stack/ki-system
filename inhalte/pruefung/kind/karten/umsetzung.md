# Vorgabe „Drei Karten für die Kinderseite“ – Nachbessern · Mein Schuljahr · Zusatz eingeplant

Stand 23.11.2026, Grundlage `inhalte/AUFTRAEGE.md` (lernen-app 83ada52): „Entscheidung Sebastian (23.11., 02:54): wieder offene Etappe … · Auftrag NB“, „Auftrag SJ – Wie viel ist noch? je Schuljahr“, „Entscheidung Sebastian (23.11., 02:35): eingeplanter Zusatz-Teil“ (mit Rückläufer ChatGPT 963/964). Passt zu `kind/karte/umsetzung.md` (Reisekarte, §4/§11) und `kind/expedition/umsetzung.md` (EX). Entwurf zum Anklicken: `entwurf/karten.html` (Ansicht und Gerät oben umschaltbar). Bilder: `bilder/400-*.png`, `bilder/820-*.png`. Beispielzahlen aus dem Auftrag, Testkind; keine Namen.

## 0 Reihenfolge auf der Startseite (Abflugtafel heute / schwebende Zone der Reisekarte später)
1. **Nachbessern** (wenn vorhanden) – oberste Karte, immer zuerst.
2. **Expedition** (EX Ansicht 2) – steht Nachbessern an, wird sie zum Chip `⛯ Expedition wartet: {Titel} ›` (wie EX 2b), die große Karte kommt nach dem Nachbessern zurück. Kein „später“ nötig.
3. **Gerade dran** mit gelbem Startknopf (Check-in-Zeile aus WD bleibt darin).
4. **Zusatz · eingeplant** (wenn vorhanden) – unter „Gerade dran“, nie mit gelbem Hauptknopf.
5. **Mein Schuljahr** – darunter (Handy) bzw. rechte Spalte (Tablet/Rechner).
Der gelbe Knopf führt immer zum nächsten **Pflicht**-Flug; Nachbessern hat einen eigenen (orangen) Knopf. Auf 820 px zweispaltig: links 1–4, rechts 5 (Bild `820-start.png`).

## 1 Karte „Nachbessern“ (NB-App)
**Wann:** Liste `nachbessern` des Kindes (NB-S) nicht leer. Auch bei fertigem Ort und bei „Kann er“ mit Rückfall. Fahrplan, Stempel, Sterne unverändert.
**Farbe:** Orange `#C8642B` auf Hell-Apricot `#FFF1E6`, Rand `#F0B48C` – kein Rot (kein Fehler-Ton), nicht Gold (abgelegt), nicht Blau (dran).
**Texte (wörtlich):**
- Kopf: `↻ NACHBESSERN`
- Titel: `{Etappe}` (z. B. „Runden“), darunter `in {Stadt} · {Land} · {Flug-Titel}`
- Satz: `Die Etappe ist ein bisschen eingerostet. Mit 3 richtigen in Folge sitzt sie wieder.` („3 richtigen in Folge“ fett)
- Fortschritt: drei Kreise, gelöst grün mit ✓, daneben `{x} von 3`
- Knopf: `Jetzt nachbessern ›` (bei x ≥ 1: `Weiter nachbessern ›`) – führt **direkt in die Übung dieser Etappe**
- klein: `Deine Sterne und Stempel bleiben. Etwa 3 Minuten.`
- Mehrere Etappen: darunter `+{k} weitere Etappe(n) zum Nachbessern` (die älteste zuerst).
**In der Übung:** Leiste über der Bordkarte `↻ NACHBESSERN · {Etappe}` + drei Kreise + `{x} von 3 in Folge`. Falsch → Folge auf 0, Hinweis im Rückmelde-Kasten: **`Kein Problem – neuer Anlauf.`** / `Noch 3 richtige in Folge, dann sitzt die Etappe wieder.` Kein „falsch“-Wort, kein Rot außer dem üblichen Rückmelde-Zeichen. Sterne je Aufgabe wie immer.
**Bestätigung nach der dritten richtigen (kurz, ≤ 1,5 s Bewegung, kein Ganzbild-Fest):** drei Haken springen ein; Titel **`Sitzt wieder!`**; Satz `„{Etappe}“ in {Stadt} ist wieder gelandet.` / `In den nächsten Lerntagen fragen wir sie noch ein paar Mal ab.`; Knopf `Weiter in {nächste Stadt} ›` (bzw. nächste Nachbessern-Karte, falls noch eine). Keine Extra-Sterne.
**Reisekarte:** Stadt-Haltestelle in Orange mit `↻`, gestrichelter Ring, Unterzeile `wieder offen`; Land-Pin zusätzlich kleines oranges Abzeichen `↻` (neben dem Stand-Abzeichen); Legende `↻ wieder offen – nachbessern`; „📍 Zu mir“ springt zur offenen Stadt. Ergänzt `karte/umsetzung.md` §4 (Stadt-Zustand „wieder offen“).
**Lehrer:** unverändert über „Was wackelt“ / „Zu tun“; im Fahrplan kein Platzwechsel.

## 2 Karte „Mein Schuljahr“ (SJ-App, Kinderseite)
**Daten:** `schuljahr_stand` (SJ-S), Schulart des Kindes, Klassen −1 / Haupt / +1 soweit vorhanden. Gleiche Rechnung wie der Ring.
**Aufbau:**
- Kopf: `MEIN SCHULJAHR · {SCHULART}` (z. B. `GYMNASIUM`)
- Hauptklasse groß: Ring mit Prozent + `Klasse {n}`
- Zeile 1 (zuerst das Geschaffte): `Schon geschafft: {fertig} von {gesamt} Flügen · {gelandet} von {alle} Etappen`
- Zeile 2: `Noch {offen} Flüge und {offen} Etappen bis Klasse {n} geschafft` (Zahlen fett)
- **Nächstes Ziel** (blaues Feld): `Nächstes Ziel: {p} % – nur noch {k} Etappen!` mit p = nächster voller Zehner, k = ⌈alle × p/100⌉ − gelandet (bei k = 1: `nur noch 1 Etappe!`). Macht auch bei viel Offenem den nächsten Schritt klein.
- Nachbarklassen als schmale Balken: davor `Klasse {n−1}: noch {x} Flüge · {y} Etappen` bzw. `✓ Klasse {n−1} geschafft`; danach `Danach Klasse {n+1}: {y} Flüge · {z} Etappen`; rechts Prozent.
- Hauptklasse 100 %: `Klasse {n} geschafft!` + Stempelreihe; Ziel-Feld entfällt.
**Beispiele (Bilder `400-sj-kl5.png`, `400-sj.png`):** Kl. 5: 26 % · `Schon geschafft: 2 von 15 Flügen · 28 von 107 Etappen` · `Noch 13 Flüge und 79 Etappen bis Klasse 5 geschafft` · `Nächstes Ziel: 30 % – nur noch 5 Etappen!` · `Danach Klasse 6: 11 Flüge · 78 Etappen`. Kl. 8: 9 % · `Noch 15 Flüge und 88 Etappen …` · `Nächstes Ziel: 10 % – nur noch 1 Etappe!` · `Klasse 7: noch 7 Flüge · 38 Etappen` (38 %) · `Danach Klasse 9: 14 Flüge · 87 Etappen`.
Keine Prozent-Wertung („schlecht“, „hinterher“), keine Termine/Hochrechnung. Zusatz zählt nicht (auch kein Hinweis auf der Kinderkarte).

**Lehrer-Fassung – Karte „Stand“ im Überblick (nüchtern, Bild `400-lehrer.png`):** Tabelle je Klasse, Hauptklasse hinterlegt:
`Kl. 8 Gymnasium · 9 % · noch 15 von 16 Flügen · noch 88 von 97 Etappen` (Kl. 7: 58 % · noch 7 von 12 · noch 38 von 61; Kl. 9: 0 % · noch 14 von 14 · noch 87 von 87). Darunter: `+ Zusatz eingeplant: {Titel} ({x} von {y} Etappen) – zählt nicht mit ⓘ`.
ⓘ (schwebend, wörtlich): **`So wird gerechnet: Prozent = gelandete Etappen ÷ alle Etappen der Pflicht-Flüge dieser Klasse im Lehrplan {Schulart}. Flüge in Wiederholung und „Kann er“ zählen mit allen Etappen. „Flüge“ = Pflicht-Flüge der Klasse; fertig = alle Etappen gelandet und Flug-Test bestanden. Zusatz zählt nicht mit, auch nicht, wenn er eingeplant ist.`** Gleicher Text im ⓘ des Rings in „Unser Lehrplan“. Ersetzt die heutigen Ringe der Karte „Stand“ nicht – Ring links, Zahlen rechts (Rechner); Handy nur die Tabelle.

## 3 „Zusatz · eingeplant“ (ZP-App)
**Kinderseite – Karte unter „Gerade dran“ (Bild `400-start.png`):**
- Rand gestrichelt sand `#CDB894`, Fläche `#F6EFE2`; Kopf `+ ZUSATZ · EINGEPLANT`
- Flagge + `{Titel} – Teil {x} von {y}` (Untertitel und Land klein darunter)
- Etappen-Balken (je Etappe ein Stück), Text `{gelandet} von {alle} Etappen · Extra-Flug, von deinen Eltern eingeplant`
- Knopf (weiß, Zweitknopf): `Nach {Land} fliegen ›` (begonnen: `Weiter in {Stadt} ›`)
- klein: `Ganz fertig: Stempel und ★ 100. Dein nächster Flug wartet trotzdem.`
- Der gelbe Hauptknopf bleibt beim nächsten Pflicht-Flug; der Zusatz-Flug wird **nie** „nächster Flug“, sperrt nichts, zählt nicht für Visum.
**Reisekarte:** Pin wie §11 (Abzeichen `+`), aber Nadel in Plan-Gelb (eingeplant) und Schild-Unterzeile `Zusatz · eingeplant · {x}/{y}`; Blatt: `✈ {Titel} – Teil {x} von {y}` · `Extra-Flug, von deinen Eltern eingeplant` · `{x} von {y} Etappen` · Knopf `Hinfliegen ›`. Nicht eingeplanter Zusatz bleibt wie §11 („Zusatz – freiwillig, für Entdecker.“).
**Landungen:** wie jede Etappe (Landungs-Bonus 80/40/10 unverändert). **Kein Flug-Test.**
**Nach der letzten Landung – Ansicht „Zusatz geschafft“ (Bild `400-zus.png`):** Szene sand-gold; oben `{LAND} · EXTRA-FLUG`; Titel **`Zusatz geschafft!`**; Satz `Alle {y} Etappen von {Titel} – Teil {x} von {y} sind gelandet.`; Stempel rund mit Flagge, Landname und Rand-Wort `ZUSATZ`; Blatt `Neuer Stempel im Reisepass` / `mit dem Rand „ZUSATZ“` und rechts `+ ★ 100`; Knopf `Weiter in {Stadt} ›` (nächster Pflicht-Flug). Genau einmal (Server bucht, nicht die App). Reisepass: Stempel mit Rand `ZUSATZ`, golden wie andere nach Ablegen aller Etappen.
**Lehrer-Ansicht (Bild `400-lehrer.png`, `820-lehrer.png`):**
- **Fahrplan:** eigener Platz, sortierbar, abwählbar; Eintrag gestrichelt sand, Nummer braun `#8A6A3A`, Zeile `{Titel} – Teil x von y`, darunter Marke `ZUSATZ · EINGEPLANT` · `{x} von {y} Etappen · ohne Flug-Test`. Kopf `8 Plätze · 12 Themen · + 1 Zusatz`. Keine Reihenfolge-Warnung, sperrt nichts.
- **Matrix-Karte:** gestrichelt sand + Platz-Nummer (braun) + Marke `ZUSATZ · EINGEPLANT`, Stand `Platz {n} · {x}/{y} Etappen`. Zählt nicht in Ring/Abdeckung (außen „+ Zusatz“-Bogen wie 12.7).
- **Detail:** Kopf `{Titel} – Teil x von y` + Marke `Zusatz · eingeplant – kein Pflichtstoff im {Schulart}`; Stand `{x} von {y} Etappen · fertig, sobald alle gelandet (ohne Flug-Test) · dann Stempel und ★ 100, einmal`; Planen wie immer (Als Nächstes · Ans Ende · Aus dem Plan). „Alle einplanen“ nimmt Zusatz weiterhin nicht mit.

## 4 Prüfen nach dem Bau
400 × 860 und 820: Reihenfolge §0 mit allen Karten gleichzeitig (Nachbessern + Expedition + Zusatz) ohne dass „Gerade dran“ unter den ersten Bildschirm rutscht (Handy: Gerade dran-Knopf ≤ 700 px); Nachbessern: Folge 0→1→0 (Fehler)→1→2→3, Bestätigung, Karte weg; Mein Schuljahr: Zahlen gleich `schuljahr_stand` und Ring; Ziel-Feld bei 9 % = 1 Etappe; Zusatz: Hauptknopf zeigt nie den Zusatz-Flug, „Zusatz geschafft“ einmal mit ★ 100; Lehrer: Fahrplan-Kopf „+ 1 Zusatz“, kein Visum/keine Warnung.
