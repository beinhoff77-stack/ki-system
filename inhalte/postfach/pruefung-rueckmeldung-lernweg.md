# Postfach pruefung-rueckmeldung-lernweg (Rückmeldung nach Fehlern und Lernweg)

## 2026-11-16 03:40 – FERTIG
Bericht: `inhalte/pruefung/rueckmeldung/bericht.md`, Nachstellung `…/rueckmeldung/nachstellen.test.cjs` (+ `protokoll.json`, `bilder/`).
Nichts an App, Tests, Datenbank oder Inhalten geändert; Datenbankfunktionen nur gelesen.

Wichtigste Befunde (nachgestellt, außer [Code]):
- F9 Gefärbte Flächen in Zeichnungen kaum sichtbar (Kontrast 1,05 : 1 hell / 1,32 : 1 dunkel) – 169 Übungsaufgaben, 41 Lernkarten; „Wie viel Prozent sind gefärbt?“ praktisch unlösbar.
- L1 Falsch gelöste Aufgabe kommt nach 3 anderen wieder; die gerade gesehene Lösung zählt für „sitzt“.
- L2 [Code] Ein Fehler in der Wiederholung setzt die Karte auf null und nimmt sie aus der Wiederholung; die App sagt dagegen „kommt bald nochmal dran“ (L3, grüner Haken bei 0 von 1).
- F1–F3 Lösung sofort, kein zweiter Versuch; Rückmeldung unabhängig vom Fehler (`grund: falsche_einheit` aus `antwort_bewerten` geht verloren); „Fehler-Detektiv“ passt oft nicht zum Fehler.
- F5/L7 Nach mehreren Fehlern in Folge kein anderer Weg für das Kind.

Vorschläge V1–V12 in bericht.md, Abschnitt 3. Zuerst: V1 Flächen, V5 gemerkte Lösung zählt nicht, V6 Wiederholungsfehler nur eine Stufe zurück, V7 ehrliche Meldungen, V10/V11 Kleinigkeiten.
Offen: Auswertung echter falscher Antworten erst mit mehr Daten und Sebastians Freigabe.
