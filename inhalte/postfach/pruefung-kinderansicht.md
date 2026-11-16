# Postfach pruefung-kinderansicht (Aufbau der Kinderansicht)

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
