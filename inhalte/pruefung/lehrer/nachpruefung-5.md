# Nachprüfung 5 – Lehrer-Ansicht und Info-Seite, App 0.83.0

Stand: `main` c9c5f0d (App 0.83.0, Cache v150), geprüft am 20.11.
Vorgabe: `nachpruefung-4.md` (N1–N5), LB Teil 6 Punkt 6 (Rückgängig, Rückfall), `info-seite-update.md` (LB Teil 7) und die Meldung in `inhalte/postfach/bau-motivation.md`.
Geprüft mit Playwright/Chrome auf 400, 820 und 1280 px, mit erfundenem Lernstand eines Testkinds auf der echten Themenliste (gleiches Skript wie Nachprüfung 4: `n5/n5.test.cjs`, Messwerte `n5/mess.json`). Dazu habe ich die Tests des Bau-Chats für Teil 6 und 7 selbst laufen lassen: 7 von 7 grün. Keine Kinderdaten.

**Nicht geprüft:** echte Geräte und Safari (Silbentrennung auf dem iPad), echter Server (Rückfall-Hinweis und Rückgängig-Ablehnung kommen erst mit der eingespielten LB-3-Nachbesserung).

## Punkte aus Nachprüfung 4

| Punkt | Stand | Messung / Beleg |
|---|---|---|
| N1 (Muss) „Nach Themengebiet“ ohne gebrochene Wörter | **erledigt** | gebrochene Wörter vorher 400: 2, 820: 16 → jetzt 0 / 0 / 0 in allen 8 Gebieten. `n5/themengebiet-820.png`, `n5/themengebiet-geometrie-400.png` |
| N2 (Sollte) Plan links: Titel abgeschnitten | **teilweise erledigt** | Rechner und Tablet gut, auf 820 nur noch wenige mit „…“. Handy siehe N7. `n5/plan-820.png`, `n5/plan-400.png` |
| N3 (Sollte) Kopf und Abschnitt zählen gleich | **erledigt** | Kopf „21 ↻“ ↔ Abschnitt „16 Orte · 21 Flüge in Wiederholung (davon 1 in Orten weiter oben)“; ebenso ▶ 1 und ○ 9 |
| N4 (Kann) eingeplante Zeilen nicht blass | **erledigt** | Deckkraft 1, gleiche Titelfarbe |
| N5 (Kann) Stand der Etappe in der Titelzeile | **erledigt** | „offen“ rechtsbündig in der ersten Zeile. `n5/klasse-gym8-auf-400.png` |
| Rückgängig nur für den jüngsten Schritt | **erledigt** | Nach einem Rückgängig ist der Knopf gesperrt. Lehnt der Server ab: „Rückgängig geht nur für die letzte Änderung. Inzwischen wurde etwas anderes geändert.“ mit „Neu laden“ (Test des Bau-Chats, bei mir grün) |
| Rückfall-Hinweis bei ◉ | **erledigt** (mit nachgebildeter Server-Antwort) | rot „gesetzt · Rückfall: 1 Etappe wieder offen“ im Lehrplan „Nach Klasse“ |
| Lange Wörter mit Trennstrich | **erledigt** | Trennungen sitzen richtig („Verhält-nisse“, „Bruch-terme“, „Unglei-chungen“, „Gleichungssys-teme“, „Gebrochen-ra-tionale“). Nur in Chrome geprüft, Safari offen |

## Info-Seite (LB Teil 7)

| Punkt | Stand |
|---|---|
| 1–7 aus `info-seite-update.md` | **erledigt**, Texte im Code gelesen und gegen die App gehalten. Die alten Doppel-Einträge „Lernstand:“ und „Was wackelt?:“ sind weg |
| Abweichung 1: „eines Themengebiets“ statt „eines Gebiets“, „ein Flug“ statt „ein Thema“ (Reisewörter-Test) | **einverstanden**: passt zu den Knöpfen „Nach Themengebiet“ in der App |
| Abweichung 2: Knopftext „Weiter: Flug-Test“ statt „Jetzt zum Test ›“ | **einverstanden**: so heißt der Knopf auf dem Abschluss-Bildschirm wirklich |
| Abweichung 3: neuer Eintrag „Abschluss einer Etappe“ | **einverstanden**, stimmt mit der App überein (drei Fassungen, Sturmflug ohne Fehlerzahl und Knobel nur als Link, ein Knopf, Flug geschafft → Bordkarte, Stempel) |
| Punkt 3 an anderer Stelle im Satz | **einverstanden** |

Zwei kleine Anmerkungen zur Info-Seite, beide Kann:
- Schritt 1 sagt „Rechts der Lehrplan“. Auf dem Handy steht er darunter. Vorschlag: „Rechts (auf dem Handy darunter) der Lehrplan“.
- Mit Bau-Auftrag LB Teil 8 (kompakte Themen-Karte, 0.83.1) ändern sich nur Darstellung und Größe der Knöpfe, die Namen bleiben. Der Text muss dafür nicht geändert werden.

## Neu aufgefallen

**N6 (Sollte) – Gewählter Themengebiet-Knopf unter dem Mauszeiger unlesbar.** Nachgestellt auf 400 px: „Geometrie“ antippen. Solange der Zeiger darauf liegt, steht weiße Schrift auf hellem Beige (`rgb(238,234,224)`). Ohne Zeiger ist er dunkelgrün und lesbar. Auf dem Rechner sieht man das bei jedem Klick. Auf Tablets bleibt der Hover-Zustand nach dem Antippen oft hängen; das ist eine Vermutung, auf dem Gerät nicht geprüft. Abhilfe: für den gewählten Knopf (`aria-pressed="true"`) beim Hover die dunkle Hintergrundfarbe behalten. Bild: `n5/knopf-gewaehlt-maus.png`, sichtbar auch in `n5/themengebiet-geometrie-400.png` oben.

**N7 (Sollte) – Plan links auf dem Handy: Titel fast immer gekürzt.** Auf 400 px sind die Titel jetzt zweizeilig, enden aber meist trotzdem mit „…“: „Algebra – Lineare Ungleichungen u…“, „Geld und Verhält-nisse – Indirekte…“, „Algebra – Bruch-terme, Potenzge-…“ (Trennstrich und „…“ hintereinander). Auch die Stufenzeile darunter ist gekürzt („Gerade dran · Gym…“). Ursache: Griff ⠿, Nummer, Klassen-Kasten und zwei große Pfeil-Knöpfe ↑ ↓ nehmen über die Hälfte der Breite ein. Dazu steht das Themengebiet als Vorsatz vor jedem Titel. Vorschlag für Handy (< 560 px):
1. Titel nur das Thema, das Themengebiet klein und grau in die Zeile darunter (wie die Themen-Karten rechts: „Funktionen · RS 8 · MYP 4“).
2. ↑ ↓ kleiner (32 px statt etwa 46 px) oder untereinander.
Bild: `n5/plan-400.png`.

**N8 (Kann) – „Themen“ statt „Flüge“ in der Lehrer-Ansicht.** Im Lehrplan des Plans steht „Gym 8: 13 von 15 Themen im Plan oder schon gekonnt“. Die Info-Seite musste wegen der Reisewörter „Thema“ vermeiden. Eines von beiden sollte angeglichen werden. Mein Vorschlag: in der Lehrer-Ansicht „Themen“ erlauben (Lehrer denken in Themen) und den Test der Reisewörter nur auf die Kinderseiten anwenden. Das ist eine Entscheidung für Sebastian.
