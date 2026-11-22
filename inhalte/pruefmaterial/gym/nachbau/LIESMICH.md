# Nachbau Prüfungsaufgaben Gymnasium (Auftrag PM 2, Teil B)

Stand 2026-11-22. Für jede Arbeit aus `../katalog.json` gibt es hier eine **nachgebaute Schulaufgabe** `<arbeit_id>.md` mit Lösungsblatt, dazu `nachbau.json` (maschinenlesbar).

- Klasse 8: 51 Arbeiten, 541 Aufgaben
- Klasse 5: 53 Arbeiten, 829 Aufgaben

## Wie nachgebaut wurde

- Jede Aufgabe kommt aus einem **Generator** für ihre Etappe (`_g8a.py`, `_g8b.py`, `_g8c.py`, `_g5a.py`, `_g5b.py`).
  - Bei mehreren Aufgabenarten in einer Etappe wählt der Generator die Variante über Stichworte aus der Katalogbeschreibung.
  - Text, Zahlen und Sachkontext sind eigene. Die Zahlen sind zufällig, mit festem Startwert je Aufgabe, damit der Lauf reproduzierbar ist.
  - Es werden keine Originaltexte, Originalzahlen oder Lösungen übernommen.
- Unverändert aus dem Katalog übernommen werden:
  - Niveau (I/II/III) und Kompetenz (K1–K6)
  - Typ und Punkte der Aufgabe
  - Zuordnung zu Thema und Etappe, inklusive Teil nach `lk_teilung_2211.json` (über das Katalogfeld `teil`)
- Die Punkteverteilung innerhalb einer Aufgabe verteilt das Skript auf die Lösungsschritte.
- Fehlen im Original die Punkte je Aufgabe, wird die bekannte Gesamtsumme nach Niveau verteilt. Ist keine Summe bekannt, gilt I = 2, II = 3, III = 4 Punkte (Annahme).
- Zeit, Punktesumme und Hilfsmittel entsprechen dem Vorbild. Ausnahmen:
  - Fehlt die Zeitangabe, gelten 45 min (Annahme).
  - Bei BMT10-Auszügen wird die Zeit anteilig gekürzt.
- Der Notenschlüssel ist nur ein Vorschlag (85/70/55/40/20 %).

## Lösungskontrolle (`pruefart` je Aufgabe)

| Art | Kl. 8 | Kl. 5 | Bedeutung |
|---|---|---|---|
| gegengerechnet | 357 | 642 | Das Ergebnis wird im Skript ein zweites Mal geprüft, zum Beispiel durch Einsetzprobe, Auswertung des gedruckten Rechenausdrucks, Durchprobieren aller Fälle, Rückumwandlung oder Gaußsche Flächenformel. Bei Fehlschlag verwirft das Skript die Zahlen und zieht neue. |
| Musterlösung | 124 | 173 | Zeichnungen, Konstruktionen, Begründungen und Wissensfragen. Hier gibt es nichts nachzurechnen; die Musterlösung ist von Hand formuliert. |
| vom Skript berechnet | 60 | 14 | Das Ergebnis berechnet das Skript, aber ohne zweite, unabhängige Rechnung. |

## Neu bauen

`python3 _nachbau.py alle` (oder `8` bzw. `5`) erzeugt die `.md`-Dateien und `nachbau.json` neu. Das Skript meldet fehlende Generatoren und fehlgeschlagene Prüfungen.

## Grenzen (offen)

- „Gleicher Typ“ heißt: gleiche Etappe und Aufgabenart. Mehrteilige Originalaufgaben mit durchgehendem Kontext werden teils knapper nachgebaut.
- Bei Klassenarbeiten mit 5–10 Punkten pro Aufgabe ist der Nachbau teils kürzer als das Vorbild.
- Abbildungen werden als Text, Koordinaten oder Textdiagramm beschrieben. Zeichnungen fertigt die Schülerin oder der Schüler selbst an.
- Aufgaben außerhalb des Lehrplans (z. B. Pythagoras oder Pfadregel in BMT10-Auszügen, Wahrscheinlichkeit in RS/MS-Tests) sind mit nachgebaut und als „außerhalb“ markiert.
