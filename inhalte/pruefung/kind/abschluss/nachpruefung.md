# Nachprüfung Abschluss-Ansichten (AB-A) – App 0.83.0

Stand: `main` c9c5f0d (App 0.83.0, Cache v150), geprüft am 20.11.
Vorgabe: `umsetzung.md` (Fassung 2, Freigabe §7), `entwurf/abschluss.html`, Zusätze von Sebastian (Knobel von selbst vor dem Abschluss, Flug-Test folgt, RICHTIG/FALSCH im Ergebnis).
Geprüft mit Playwright/Chrome, Testkind und erfundenen Daten (Server-Antworten nach AB-S nachgebildet, wie in den Tests des Bau-Chats). Handy 400 × 780 und 360 × 640, Tablet 820, hell und nacht. Keine Kinderdaten.
Bilder: `nachpruefung-bilder/`. Messskript: `nachpruefung-bilder/ab1.test.cjs`, Ergebnisse `mess.json`.

**Nicht geprüft:** gegen den echten Server (AB-S und LB-3-Nachbesserung sind laut Postfach noch nicht eingespielt); echte Geräte, Safari, Bildschirmleser.

## Ergebnis

Die Vorgabe ist bis auf Kleinigkeiten erfüllt. Ich habe die AB-A-Tests des Bau-Chats selbst laufen lassen. 5 von 6 waren grün, einer wackelt (siehe N4); das ist ein Testfehler, kein App-Fehler.

| Punkt | Stand | Beleg |
|---|---|---|
| 1 Drei Fassungen mit eigener Szene, Farbe, Abzeichen | erledigt | `etappe-drei-fassungen.png` |
| 1 Schwellen (direkt / sauber / sturm, wieder gelandet) | erledigt (App folgt `landung_art` des Servers; die Schwellen selbst liegen am Server, nicht live geprüft) | Test „AB-A 1“ |
| 1 Handy ohne Scrollen, hell und nacht | erledigt, auch bei 360 × 640 | `sturm-360x640.png`, `mess.json` |
| 1 Genau ein großer Knopf, kein Weg zurück in die Übungen, Zurück-Taste nicht in die Bordkarten | erledigt | Test „AB-A 1“ |
| 1 Sturmflug ohne Fehlerzahl, Knobel nur als Textlink | erledigt | Text: „15 Bordkarten, zweimal neu angesetzt – und nicht abgedreht.“ |
| 1 Abzeichen im Reisepass gezählt | erledigt („⚡ Direkt 4 · ✓ Sauber 9 · ⚡ Ausdauer 3“) | Test „AB-A 1“ |
| 2 Flug geschafft → Bordkarte → Boarding öffnet die erste Erklärung | erledigt | `flug-bordkarte-ort.png` |
| 2 Antwortliste nur über „Test ansehen“ | erledigt | Test „AB-A 2“ |
| 2 Ohne nächsten Flug: „Alles geschafft, was im Plan steht …“ | erledigt | Test „AB-A 3“ |
| 3 Ort geschafft → Stempel → Bordkarte VON → NACH | erledigt, aber Datum falsch (N1) | `flug-bordkarte-ort.png` |
| 4 Bewegung ≤ 1,8 s, Antippen beendet sie, „weniger Bewegung“ zeigt sofort den Endzustand | erledigt | Test „AB-A 4“ |
| Zusatz: Knobel von selbst vor dem Abschluss (nicht beim Sturmflug) | erledigt | Test „Teil 4 Punkt 5d“, „AB-A 1“ |
| Zusatz: Flug-Test folgt | erledigt, als einziger Knopf „Weiter: Flug-Test“ auf dem Abschluss der letzten Pflicht-Etappe (so in umsetzung.md vorgesehen) | Code `lernen.js` 2434 |
| Zusatz: RICHTIG/FALSCH im Test-Ergebnis | erledigt (war schon aus Teil 4 da, mit „Erst üben“ / „Gleich verbessern“) | Code `lernen.js` 2968 ff. |
| „Flug geschafft“ nur beim ersten Abschluss (`flug_geschafft`) | offen: kommt laut Postfach mit 0.83.1. 0.83.0 zeigt die Ansicht bei „Flug fertig und kein Nachtest“ | Postfach bau-motivation |

## Neu aufgefallen

**N1 (Sollte) – Datum im Ort-Stempel mit zwei Punkten.** Im Stempel steht „Zahlen · 20.11..“. Ursache (nachgestellt): `lernAbschlussOrt` hängt an `toLocaleDateString('de-DE', {day:'2-digit', month:'2-digit'})` noch einen Punkt an. Chrome liefert aber schon „20.11.“. Der zusätzliche Punkt muss weg. Bild: `flug-bordkarte-ort.png`, drittes Bild.

**N2 (Kann) – Direktflug: Der Schrägstrich von „2/2“ ragt in „AUF ANHIEB“.** Auf 400 px trifft der Schrägstrich den Buchstaben A von „ANHIEB“. Abhilfe: etwas mehr Abstand unter der großen Zahl. Bild: `etappe-drei-fassungen.png`, erstes Bild.

**N3 (Kann) – Sturmflug auf kleinem Handy (360 × 640): Der Blitz läuft durch den Text.** Der Blitz kreuzt „in Folge richtig.“. Er sollte hinter dem Text liegen oder weiter rechts unten beginnen. Bild: `sturm-360x640.png`.

**N4 (Hinweis für den Bau-Chat, kein App-Fehler) – Test „AB-A 2“ wackelt.** Er schlug bei mir in 2 von 6 Läufen fehl („Ansicht geschlossen“). Nachgemessen: Nach „Boarding“ schließt die App die Ansicht 3–18 ms nach dem Adresswechsel, also immer. Der Test prüft aber sofort danach. Abhilfe im Test: auf `.lr-abschluss` mit Anzahl 0 warten statt sofort zu zählen.

**N5 (Kann) – „Überspringen ›“ auf dem Ort-Bildschirm kaum lesbar.** Heller Knopf auf Sand-Hintergrund, siehe drittes Bild in `flug-bordkarte-ort.png`. Dunklere Schrift oder Rand verwenden.

Hinweis ohne Handlungsbedarf: Im Ort-Bildschirm steht in meinen Bildern „STEMPEL 0“. Das kommt aus den erfundenen Kontodaten des Tests (`stempel: 0`), nicht aus der App.
