# Postfach pruefung-kinderansicht (Aufbau der Kinderansicht)

## 2026-11-17 11:45 – NACHPRÜFUNG SCHRITT A (N1–N8, App 0.74.2)
Bericht: `inhalte/pruefung/NACHPRUEFUNG-2026-11-17-N1-N8.md` (Stand lernen-app 9d092d0). Tests lernen 24/24 grün, alle 593 Etappen gerendert.
- **Erfüllt:** N3, N4, N5 (laut Auftrag), N6, N7 (Hinweis: „grün“ ist in Ozean/Wüste Petrol), N8.
- **N1 teilweise:** Keine Doppelbilder mehr (0 von 416), „negative Zahl“ 2 286 px. Aber: Abblenden auf 40 % lässt den gelben Graphen in der Tag-Gestaltung fast verschwinden (Kerze), und das auf 2 Einheiten vergrößerte Steigungsdreieck widerspricht in 2 Etappen dem Text („Jede Stunde 1,5 cm“ – gezeichnet 2 h / 3 cm).
- **N2 nicht erfüllt (neuer Fehler):** Satzende wird nach einbuchstabigen Wörtern und vor Kleinbuchstaben nicht erkannt → 87 von 593 „Kurz gesagt“ enthalten zwei Sätze. Mit richtiger Erkennung sind nur 75 (nicht 116) Merksätze über 90 Zeichen.
- Nacharbeit-Vorschlag (Schritt A2) im Bericht; 4 Dreieck-Schritte in funktionen.linear.json gehen an einen Inhalts-Chat (Entscheidung Sebastian).

## 2026-11-16 05:55 – NACHPRÜFUNG ERGÄNZT
`NACHPRUEFUNG-2026-11-16.md` ergänzt: N1 erweitert (413 von 443 umgebauten Etappen wiederholen Bilder, Neues nicht hervorgehoben), N6 Test-Kopf mit Ortstitel, N7 Testergebnis (ungestaltete Knöpfe, kein „Verbessern“, Zahlenstrahl ohne richtige Markierung), N8 Bildergeschichte auf dem Tablet zerfällt; Schätzung zur 6-Punkte-Regel (9–14 Bordkarten je Etappe).

## 2026-11-16 05:40 – NACHPRÜFUNG
lernen-app 0.74.0 nachgeprüft: `inhalte/pruefung/NACHPRUEFUNG-2026-11-16.md`.
Umgesetzt und nachgestellt: Erklärungen A1–A12, Rückmeldung R1–R3, Kinderansicht K1 (inkl. Reisewörter, Rückreise-Karte).
Offen laut Plan: K2–K4, E-1–E-4. Neue Befunde N1–N5, wichtigster N1: Bildergeschichte wiederholt gleiche Bilder (Etappe 3 057 px).
Hinweis: neue Regel „sitzt nach 6 Punkten + schwere Bordkarte“ muss in die Info-Seite (E-1).

## 2026-11-16 04:35 – AUFTRAG
Sebastian beauftragt den Umbau aller drei Prüfrunden (Erklärungen, Rückmeldung & Lernweg, Kinderansicht & Stand).
Gesamtauftrag mit Reihenfolge: `inhalte/pruefung/UMBAU-AUFTRAG.md` (Zweig pruefung-kinderansicht).
- Phase 1: Fehler + kleine Darstellung (A2, A5–A9, A12 · R1 · K1 inkl. Reisewörter), parallel D1 Klassen-Zuordnung prüfen (Inhalts-Chat).
- Phase 2: A1, A3, A4 · R2 (nach A9) · K2; D2 Orte neu zuordnen nach Freigabe.
- Phase 3: K3 Stand (3 Ebenen) · K4 Eltern mit Einstiegs-Check · R3 · A10, A11.
- Phase 4: Inhalte U5 → … (Inhalts-Chats), R4 später.
Festgelegt: Reisewörter in allen Kindertexten (Flug/Etappe/Bordkarte/Kontinent), Menü ≡ bleibt, Weltkarte in „Mein Weg“.

## 2026-11-16 04:30 – FERTIG
Bericht `inhalte/pruefung/kinderansicht/bericht.md`, Aufteilung `…/kinderansicht/umsetzung.md`, Rundgang `…/kinderansicht/rundgang.test.cjs` (+ `orte.json`, `messung.json`, `bilder/`).
Nichts an App, Tests, Datenbank oder Inhalten geändert; Lehrstoff-Struktur (Orte, Gebiete, Einheiten) nur gelesen, keine Kinderdaten.

Wichtigste Befunde (nachgestellt):
- B1 Sechs Fortschrittsmaße nebeneinander (Sterne, Stempel, Themen, Orte, „kann ich/dran/kommt“, Kartenband); B2 „Noch N Karten bis zum Stempel“ zählt nur das aktuelle Thema (Rom: 10 statt 44).
- B3 Mein Weg/Merkheft zeigen den Ortsnamen statt des Themas (fünfmal „Rom: Natürliche und ganze Zahlen“).
- B4 „Kommt noch“ falsch gefiltert: Klasse 8 sieht Klasse 5–7 als „bereit“, Klasse 5 sieht Orte ohne Klasse.
- B8 Klasse von Ort und Thema widersprechen sich bei 13 von 65 Orten.
- B10 Navigation nur über schwebendes ≡; Menü markiert im Reisepass „Mein Weg“.
Vorschlag: Heute · Mein Weg (mit Kartenansicht) · Merkheft (nur Geschafftes) · Reisepass mit fester Leiste; ein Fortschrittsmaß „Klasse X: n von m Themen“.

## 2026-11-17 – Nachprüfung 0.74.5
- Bericht: `inhalte/pruefung/NACHPRUEFUNG-2026-11-17.md`. Umgesetzt: A, R1–R3, N5–N7, K1/K2, D2, E-1 bis E-3. Offen laut Plan: K3–K5, E-4.
- Neue Befunde M1–M9 (Gerade dran zählt alles, Klasse noch mit Speichern, Häkchen getrennt vom Flug, Klasse-8-Ort im Klasse-5-Plan, Zielangabe 29 Etappen, Detektiv bei Auswahl, doppeltes Bild, ≡ verdeckt, Text „alles verteilt“).

## 2026-11-18 – Lehrer-Aufbau ausgewählt
- Durchspielprobe 0.78.1: `inhalte/pruefung/lehrer/bericht.md` (L1–L9).
- Sebastians Auswahl 1A · 2B · 3B · 4A · 5A · 6B · 7A, Bauauftrag `inhalte/pruefung/lehrer/umsetzung.md` (LA-1 bis LA-7).
