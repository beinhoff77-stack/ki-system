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

## 22.11.2026 – Nachtrag: Ziel 50 Arbeiten je Klasse – FERTIG: PM RS (Nachtrag)

- **Stoff 7: 50 Arbeiten** (49 mit Einzelaufgaben). **Stoff 8: 73** (44 mit Einzelaufgaben, 29 nur auf Themenebene). Katalog insgesamt: 125 Arbeiten, 1389 Einzelaufgaben.
- **Neu:**
  - 18 Arbeiten (Kl. 7) und 21 (Kl. 8) von den Übersichtsseiten von klassenarbeiten.de, im Browser durchgesehen.
  - Ältere ISB-Tests: Jahrgangsstufentest 8 von 2007 I und II/III, 2009 II/III, 2011 II/III, 2016 I, 2017 I; Grundwissentest 9 von 2017 und 2018, jeweils I und II/III. Alle nach altem Lehrplan, so gekennzeichnet.
- **Einschränkung:** Nur 40 (Kl. 7) bzw. 51 (Kl. 8) Arbeiten stammen sicher oder wahrscheinlich aus Bayern. Die übrigen kommen von klassenarbeiten.de ohne Angabe des Bundeslands. Arbeiten aus eindeutig anderen Ländern, aus der Mittelschule und Dubletten stehen nur in `quellen.md`.
- **Neue Erkenntnis:** Lehrergemachte Arbeiten sind zu etwa 50 % reine Rechenaufgaben. Schulaufgaben mischen 3–6 Themen.
- Die Etappen-Lücken bleiben dieselben, mit höheren Zahlen: Mittelpunkt einer Strecke 13×, Seiten-Winkel-Beziehung 6×. Die Prozentwerte für LehrplanPLUS sind unverändert.

## 22.11.2026 – FERTIG: PM 2 RS (Auftrag PM 2, Teil B: Nachbau)

- **Lieferung:**
  - `inhalte/pruefmaterial/rs/nachbau/<arbeit_id>.md`: 95 druckbare Arbeiten, je Arbeit Aufgabenblatt, Lösungsblatt mit Lösungsweg und Teilpunkten sowie eine Zuordnungstabelle.
  - `nachbau/README.md`: Übersicht nach Stoff-Klasse und Gruppe (I, II/III, ohne Angabe).
  - `nachbau.json`: maschinenlesbar, eine Arbeit je Zeile.
- **Umfang:**
  - Stoff 7: 49 Arbeiten mit 727 Aufgaben. Stoff 8: 44 Arbeiten mit 616 Aufgaben.
  - Zusätzlich 2 Grundwissentests 7 (Stoff bis 6) mit 46 Aufgaben.
  - Erfasst sind alle Arbeiten mit Einzelaufgaben, in der Reihenfolge Stoff 7, dann Stoff 8. Die 29 Verlagsarbeiten, die nur auf Themenebene katalogisiert sind, haben keinen Nachbau.
- **Nachbau-Regeln:**
  - Jede Aufgabe ist neu erzeugt, mit gleichem Typ, gleicher Kompetenz, gleichem Niveau, gleichem Thema und gleicher Etappe wie das Vorbild, aber mit eigenem Text, eigenen Zahlen und eigenem Kontext.
  - Keine Originaltexte, keine Originalzahlen.
  - Vier Vorlagen, die einer gelesenen Originalaufgabe zu nahe kamen (runder Tisch, Preisrätsel mit Füller, Altersrätsel mit Mutter, wortgleiches Zahlenrätsel), habe ich durch eigene Aufbauten ersetzt.
- **Rahmen der Arbeit:**
  - Punktesumme wie im Original, wo das Original sie nennt (53 Arbeiten). Sonst Punkte nach Niveau (I = 2, II = 3, III = 4 Punkte).
  - Arbeitszeit wie im Original. Wo sie fehlt (48 Arbeiten), gilt als Annahme 45 bzw. 20 Minuten, gekennzeichnet.
  - Niveauverteilung und Themenmix entsprechen dem Original.
  - Jede Aufgabe ist Thema und Etappe zugeordnet. Für die 395 Aufgaben in geteilten Themen ist zusätzlich der Teil nach `lk_teilung_2211.json` angegeben. Aufgaben ohne passende Etappe stehen als „LÜCKE: … (vorgeschlagen)“ beim vorgeschlagenen Thema.
- **Nachgerechnet:**
  - `_nachbau.py` rechnet jede Lösung unabhängig nach. Dafür wird sympy benötigt (`pip install sympy`). Ergebnis: 1507 Prüfungen, 0 Fehler.
  - Geprüft werden: Probe durch Einsetzen, symbolisches Ausmultiplizieren und Lösen, Abzählen von Wahrscheinlichkeiten, Winkelsummen, Abstände, Flächeninhalte mit einer zweiten Formel, Punktesummen.
  - 97 Aufgaben sind reine Wissens- oder Konstruktionsfragen ohne Rechnung und in `nachbau.json` als „WISSEN“ markiert. Bei Konstruktionen sind nur die Kontrollwerte nachgerechnet, nicht die Zeichnung selbst.
- Merge lernen-app → pruefmaterial-rs: Konflikte nur in RS-Dateien; der neuere Stand dieses Zweigs wurde behalten.
