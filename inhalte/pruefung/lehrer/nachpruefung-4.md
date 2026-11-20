# Nachprüfung 4: Lehrer-Ansicht nach „Bau-Auftrag LB, Teil 5“ (App 0.82.2)

**Geprüft:** `origin/main` 24f59ec (App 0.82.2). Auftrag: `inhalte/AUFTRAEGE.md`, „Bau-Auftrag LB, Teil 5“. Grundlage: `nachpruefung-3.md`.

**Wie geprüft:**
- Playwright (Chromium) bei 400 × 860, 820 × 1180 und 1280 × 900, angemeldet als Lehrer.
- Erfundenes Testkind in Gym 8, Lehrstoff aus der echten Themenliste (95 Flüge, Titel, Lernbereiche, Reihenfolgen, Etappen-Titel).
- Lernstand erfunden, alle fünf Stufen kommen vor. Keine Kinderdaten, keine Namen.
- Skript `n4/n4.test.cjs`, Messwerte `n4/mess.json`, Bilder `n4/bilder/`.

**Gebrochene Wörter, maschinell gezählt:** Für jedes Wort mit mindestens 3 Buchstaben wird geprüft, ob es auf zwei Zeilen verteilt ist. Wörter mit Bindestrich zählen nicht.

## 1. Punkte aus Nachprüfung 3

| Punkt | Ergebnis | Gesehen | Bild |
|---|---|---|---|
| **M1** Tablet 820: Lehrplan-Spalte „Nach Klasse“ zu schmal | **erledigt** | Alle 17 Klassen (Gym 5–10, RS 5–10, MYP 1–5) bei 400, 820 und 1280: kein gebrochenes Wort, kein Querrollen. Unter 1100 px steht das Stufenwort unter dem Titel. | `820-klasse-gym8-auf.jpg`, `820-klasse-rs7.jpg` |
| **S1** Auswahlmodus kompakt | **erledigt** | Tablet: Seite 3 399 → 3 895 px (+15 %; vorher +690 %). Handy 4 944 → 6 400, Rechner 2 739 → 3 172. Orte zugeklappt, je Ort ein Häkchen und „▸ einzeln“ (22×), je Abschnitt „alle auswählen“ (4×). Keine Flug-Knöpfe und kein „alle Flüge: kann er komplett“ beim Auswählen. Die Sammelleiste bleibt beim Rollen sichtbar. | `820-auswahl-blick.jpg`, `400-auswahl-gescrollt.jpg` |
| **S2** Gleiche Einheit in Kopf und Abschnitten | **erledigt, aber neuer Widerspruch (N3)** | Abschnitte zeigen jetzt Orte und Flüge: „▶ GERADE DRAN · 1 Ort, 2 Flüge“, „○ KOMMT NOCH · 5 Orte, 8 Flüge“. | `820-plan-blick.jpg` |
| **S3** Lehrplan-Übersicht nach Lernbereich und Lehrplan-Reihenfolge | **erledigt** | Gym 8: M8 1 Zuordnung und Funktion → M8 2 Lineare Funktionen, Intervalle, Lineare Ungleichungen → … → M8 7. RS 7: M7 1 Potenzen … M7 8 in RS-Reihenfolge. Die Server-Funktion `api.schule_lehrplan_uebersicht` liefert `lernbereich`, `lehrplan_reihenfolge`, `lehrplan` und `stufe` (Funktionstext gelesen, keine Daten). | `1280-lehrplan.jpg`, `820-lehrplan-rs7.jpg` |
| **S4** Etappen mit Titel und Stand | **erledigt** | Aufgeklappt als Liste „1 Ungleichungen umformen · offen“ … „7 Sachaufgaben mit Ungleichungen · offen“. Andere Stände als „offen“ habe ich nicht gesehen, weil meine Testdaten keinen Lernstand je Etappe enthalten. | `820-klasse-gym8-auf.jpg` |
| **K1** Legende zuklappbar | **erledigt** | Eine Zeile „▶ ○ ↻ ◉ + Legende“, aufklappbar. | `820-plan-blick.jpg` |
| **K2** Keine innere Bildlaufleiste | **erledigt** | Spalte `position: static`, keine inneren Bildlaufleisten. | – |
| **K3** IB-Lernbereiche deutsch zuerst | **erledigt** | „MYP 3 Zahl und Algebra (Numerical and abstract reasoning)“. | `820-klasse-ib3.jpg` |
| **K4** Fehlender Lehrplan-Bezug | **erledigt (Ersatz)** | „Intervalle“: „Lehrplan: M8 2 Lineare Funktionen“, also der Lernbereich als Ersatz. Den eigentlichen Bezug muss weiter das Inhalts-Chat nachtragen. | – |

## 2. Neu aufgefallen

**N1 – Muss: Ansicht „Nach Themengebiet“ (die Standard-Ansicht) hat denselben Fehler wie M1.**
- Auf dem Tablet (820) brechen in 7 von 8 Gebieten Wörter, insgesamt 16: „Dezimalzahle/n“, „Zehnerpotenz/en“, „wissenschaftl/iche“, „Potenzgesetze“, „Gleichungssysteme“, „Exponentialgleichungen“, „Kongruenzabbildungen“, „Proportionalität“, „Standardabweichung“, „Graphentransformation“, „Logarithmusfunktionen“ u. a.
- Auf dem Handy (400): „Kongruenzabbildu/ngen“, „Funktionenscharen“. Auf dem Rechner (1280): nichts.
- Die Ursache ist dieselbe wie bei M1: Titel und Stufenwort stehen nebeneinander in der schmalen Spalte. Teil 5 hat die Regel nur in „Nach Klasse“ umgesetzt.
- Vorschlag: Unter 1100 px steht das Stufenwort auch in „Nach Themengebiet“ unter dem Titel.
- Bilder: `820-themengebiet-Zahlen.jpg`, `820-themengebiet-Geometrie.jpg`, `400-themengebiet-Geometrie.jpg`.

**N2 – Sollte: Plan-Zeilen links auf Handy und Tablet abgeschnitten.**
- Auf dem Tablet sind 28 Titel einzeilig mit „…“ gekürzt, auf dem Handy 31.
- Beispiele: „Algebra – Lineare Ungl…“, „Algebra – Gleichungss…“, „Fläche und Raum – Kör…“.
- Der Lehrer erkennt das Thema in seinem Cockpit nicht. Vorschlag: zwei Zeilen zulassen, erst danach mit „…“ kürzen.
- Auf dem Rechner ist nichts abgeschnitten.
- Bilder: `820-plan-blick.jpg`, `400-plan-blick.jpg`.

**N3 – Sollte: Die Zahlen in Kopf und Abschnitt widersprechen sich.**
- Kopf: „20 ↻“ (Flüge nach eigener Stufe). Abschnitt: „↻ IN WIEDERHOLUNG · 16 Orte, 24 Flüge“.
- Der Abschnitt zählt alle Flüge der Orte, deren Ort-Stufe ↻ ist, also auch ◉-Flüge darin.
- Vorschlag: Im Abschnitt nur die Flüge dieser Stufe zählen („16 Orte · 20 Flüge in Wiederholung“), oder ausdrücklich „davon 20 ↻“.
- Bild: `820-plan-blick.jpg`.

**N4 – Kann: „Nach Themengebiet“ zeigt eingeplante Zeilen blass.** Graue Schrift auf hellem Verlauf, schwer lesbar. „Nach Klasse“ zeigt dieselben Themen in normaler Schrift. Besser einheitlich: Eingeplante nicht abblassen, die Stufe trägt die Information. Bild: `820-themengebiet-Zahlen.jpg`.

**N5 – Kann: Etappen-Liste auf dem Handy.** Der Stand („· offen“) rutscht bei längeren Etappen-Titeln allein in die nächste Zeile. Den Stand rechtsbündig in dieselbe Zeile setzen oder als kleines Zeichen vor die Nummer. Bild: `400-klasse-gym8-auf.jpg`.

## 3. Nicht geprüft

- Echte Kinderdaten, echte Geräte (nur Chromium), Ziehen mit dem Finger.
- Etappen-Stand außer „offen“ und Überblick/Stand des Kindes: Meine Testdaten bilden `schule_lernstand` nicht nach.
- Server-Regeln von LB-3: Die Nachbesserung läuft gerade getrennt bei `bau-motivation`.
