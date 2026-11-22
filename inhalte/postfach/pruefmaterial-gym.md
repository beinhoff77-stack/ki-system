# Postfach pruefmaterial-gym

## FERTIG: PM Gym (22.11.)

Zweig `pruefmaterial-gym` (von lernen-app), nur `inhalte/pruefmaterial/gym/` + diese Meldung. Datenbank/App unberührt, nichts eingespielt, kein Merge.

- `katalog.json` (eine Zeile je Aufgabe), `katalog.md` (je Arbeit), `auswertung.md`, `quellen.md`, Generator `_bau.py`.
- Bestand: Kl. 5 **10 Arbeiten / 82 Aufgaben**, Kl. 8 **29 Arbeiten / 350 Aufgaben** – Ziel 30 je Klasse **nicht erreicht** (Kl. 5).
- Kl. 8: 16 davon BMT8 = Grundwissen Kl. 5–7; Kl.-8-Stoff nur 13 Arbeiten.
- Kl. 5: kein amtlicher Test; keine sicher bayerische Schulaufgabe frei gefunden.
- Kernbefund: Flug-Test (1 Aufgabe je Etappe) reicht nicht als SA-Vorbereitung; Vorschlag „Schulaufgaben-Training“ in `auswertung.md` §6.
- 33 Aufgaben als Lücke/außerhalb markiert (u. a. Beweisen mit Termen, Tabellenkalkulation, Quadernetz, Bruchgleichung aus Text).
- Niveau I/II/III und Kompetenz = eigene Einschätzung.

## FERTIG: PM Gym Runde 2 – Ziel 50 (22.11.)

- Bestand: Kl. 5 **53 Arbeiten / 829 Aufgaben**, Kl. 8 **51 Arbeiten / 541 Aufgaben** – Ziel 50 formal erreicht.
- Neues Feld `kategorie`: A Gym Bayern · B Bayern amtlich RS/MS · C sonst.
  - Kl. 5: A 1, B 28, C 24. Kl. 5 erreicht 50 nur mit Realschul-/Mittelschul-Tests Jgst. 6; eine echte bayerische Gym-SA Kl. 5 ist weiter nicht frei verfügbar.
  - Kl. 8: A 47 (20 BMT8, 18 BMT10-Auszüge), C 4. Zum laufenden Kl.-8-Stoff gibt es nur 13 echte Arbeiten.
- Neue Lücken-Schwerpunkte: Quader-/Würfelnetze, Zahlenfolgen (Kl. 5); Zahl in Gleichung passend wählen, Beweisen mit Termen (Kl. 8).
- `auswertung.md`, `quellen.md` neu; Daten der 2. Runde in `_daten2.py`.

## FERTIG: PM 2 Gym (22.11.)

Teil B (Nachbau), Zweig `pruefmaterial-gym`. Liegt unter `inhalte/pruefmaterial/gym/nachbau/` (je Arbeit `<arbeit_id>.md`, dazu `nachbau.json`, `LIESMICH.md`, Generatoren `_g*.py`, `_nachbau.py`). Datenbank und App unberührt, kein Merge.

- Kl. 8: 51 nachgebaute Schulaufgaben mit 541 Aufgaben. Kl. 5: 53 Schulaufgaben mit 829 Aufgaben. Jede hat Lösungsblatt, Lösungsweg mit Punkten und Zuordnung zu Thema/Etappe/Teil.
- Niveau, Kompetenz, Punkte und Zeit wie im Katalog. Texte, Zahlen und Kontexte sind eigene; keine Originaltexte.
- Lösungskontrolle: 999 Aufgaben unabhängig gegengerechnet, 297 Musterlösungen (Zeichnen/Begründen), 74 nur vom Skript berechnet.
- Offen: Mehrteilige Originalaufgaben sind teils knapper nachgebaut; Abbildungen sind als Text beschrieben.

## FERTIG: PM Gym Runde 3 – Kl.-8-Stoff erweitert (22.11.)

- Katalog Kl. 8: **73 Arbeiten / 854 Aufgaben** (vorher 51/541). Neu dazugekommen:
  - 10 bayerische Schulaufgaben/Exen/Stegreifaufgaben von klassenarbeiten.de (Bayern nur bei 3795 belegt, sonst angenommen; sechs aus dem alten G9)
  - 12 ISB-Grundwissentests Realschule Jgst. 9, WPFG I (Kategorie B; RS-eigene Themen als „außerhalb“ markiert)
- Zum laufenden Kl.-8-Stoff gibt es jetzt 35 Arbeiten (vorher 13).
- Nachbau neu gebaut: Kl. 8 hat 73 Schulaufgaben, davon 585 Aufgaben gegengerechnet; neuer Generator `_g8d.py`.
- Weitere RS-Tests sind verfügbar (WPFG II/III, ältere Jahrgänge), aber nicht aufgenommen.
