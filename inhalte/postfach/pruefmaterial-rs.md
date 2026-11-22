# Postfach pruefmaterial-rs

## 22.11.2026 – FERTIG: PM RS

Zweig `pruefmaterial-rs` (von lernen-app). Geändert wurden nur Dateien unter `inhalte/pruefmaterial/rs/` und diese Meldung. Datenbank, App und main sind unberührt.

**Lieferung**
- `katalog.json`: 76 Arbeiten, 1041 Zeilen. Davon sind 973 Einzelaufgaben; 68 Zeilen sind Verlags-Schulaufgaben, die nur auf Themenebene erfasst sind.
- `katalog.md`: Übersicht je Arbeit (Zeitpunkt im Schuljahr, Themen, die zusammen geprüft werden) und Aufgabentabellen.
- `auswertung.md`: Abschnitte 0–6, jeweils getrennt nach gesichert / Annahme / offen.
- `quellen.md`: alle Links mit Abrufdatum, auch nicht verwertbare Quellen mit Grund.
- `erfassung.txt` (Rohdaten) und `_bauen.py`: prüft Thema- und Etappen-Schlüssel und baut Katalog und Kennzahlen neu.

**Kernaussagen**
- Ziel ≥ 30 Arbeiten je Klasse: Stoff 7 erreicht 26 (Ziel verfehlt). Stoff 8 erreicht 48, davon aber nur 19 mit Einzelaufgaben.
- Hauptquelle sind die ISB-Tests: der Jahrgangsstufentest 8 prüft Stoff 7, der Grundwissentest 9 prüft Stoff 8.
- Lücken im Material:
  - frei zugängliche LehrplanPLUS-Schulaufgaben von Schulen: keine gefunden
  - ISB-Leistungsaufgaben für 7 II/III und 8 II/III: nicht gefunden
- Etappen-Lücken mit Vorschlag: Mittelpunkt einer Strecke (11×), Vektoraddition (4×), Seiten-Winkel-Beziehung (4×), Parabel skizzieren (3×, eine Arbeit).
- Der Flug-Test reicht als Schulaufgaben-Vorbereitung nicht. Es fehlen Themenmix, Zeitdruck, Konstruktion/Begründung (10–30 % der Punkte) und Grundwissen (7–12 %).
- Ein Vorschlag „Schulaufgaben-Training“ steht in `auswertung.md` Abschnitt 6. Nichts davon ist gebaut.
