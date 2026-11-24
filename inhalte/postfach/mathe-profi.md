# Postfach mathe-profi

## 2026-11-24 19:30 (Adelaide) – FERTIG: Auftrag 1
Geliefert unter `inhalte/mathe-profi/` (Zweig `mathe-profi`, von `lernen-app` 8b0b83b2):
- `auftrag1.md`: Liste der heutigen Antwortformen (zahl, auswahl, luecken, markierung, text; nur 10,7 % der Aufgaben mit Bild, in keinem kann das Kind etwas tun) · Bewertung A von Kl. 5 „Rechengesetze“ (Rom, 548 Bordkarten) und Kl. 8 „Lineare Funktionen“ (445) · 4 Erklärungen (B) · 12 Aufgaben (C), davon 8 ohne reines Zahl-Tippen · 5 neue Aufgabenformen (D) mit Beispiel-Datensätzen und Prüfregeln: markieren, schieber, punkte, zuordnung, reihenfolge · Top 3 Änderungen.
- `nachrechnen.py`: alle Lösungen zweifach nachgerechnet (Lauf „OK“); erzeugt beim Lauf `aufgaben-auftrag1.json` mit den 12 Datensätzen.
- `entwurf-formen.html`: alle 5 Formen zum Anklicken, nur Antippen, getestet bei 360 und 820 px.
- `rolle.md`.

Wichtigste Befunde: (1) „Geschickt rechnen“ wird in Rom nur über das Ergebnis geprüft (79 Zahl-Aufgaben). (2) In „Lineare Funktionen“ zeichnet das Kind nie eine Gerade. (3) 19 von 46 Lage-Aufgaben sind derselbe Vierer – Raten lohnt.

Offen / App-Wunsch: neue Antworttypen D1–D5 brauchen Server (`schule.antwort_bewerten`), `lernAufgabe`/`lernAntwortText`, `tools/inhalt_pruefen.py` (TYPEN), `v_y` der Expeditionen. Empfohlene Reihenfolge: D1, D2, D3, D4, D5.
Nicht geprüft: Datenbank-Stand (nach Teilung), `inhalt_pruefen.py` für die neuen Aufgaben, Lehrplan-Zuordnung der Geradenscharen; „häufigste falsche Antwort“ ist Annahme, nicht aus Versuchsdaten.
