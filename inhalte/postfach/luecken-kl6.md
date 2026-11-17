# Postfach luecken-kl6 (Achtzehnte Runde, Teil B, Klasse 6)

Neueste Meldung oben.

## 2026-11-17 15:40 – FERTIG
Achtzehnte Runde, Teil B, Klasse 6 abgeschlossen. 4 Themen, je ein Commit auf `luecken-kl6`. Für alle 4: `tools/inhalt_pruefen.py` OK (ohne Hinweise),
`_merksaetze_pruefen.py` 0 Funde, Nachweis `python3 -I inhalte/generatoren/_luecken_kl6_nachweis.py <thema> <erweiterte Karten>` „NUR NEUES DAZU: JA“
(alte Aufgaben wörtlich vorn, alte Karten unverändert außer den genannten erweiterten Karten – dort nur Schritte/Wörter eingefügt, alte Schritte unverändert).
Technik: Abschnitt LUECKEN am Ende der Generatoren (nach SCHWER), eigene feste Zufallsstarts 6181–6211, Hilfsdatei `_luecken_kl6.py`.
Alle Lösungen vom Programm berechnet (bei Lücken rechnet c Zähler/Nenner bzw. Ganze aus dem Rechenausdruck nach); jede neue Aufgabe gelesen und nachgerechnet.
Lehrplan nachgelesen: https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/6/mathematik (M6 1.1–1.5, M6 3).

### Neue Lernkarten (alle Pflicht, je 28 Aufgaben: Übung 4/6/8, Test 1, Korrektur 3, Sicherung 6)
| Thema | Karte | Stelle | Lehrplan | Prüfungsvorbilder (je ≥ 2) | Knobel/Fehler |
|---|---|---|---|---|---|
| bruch.brueche | `gemischte_zahlen` – Gemischte Zahlen umwandeln | nach kuerzen | M6 1.3/1.4 | GWT Jgst. 7 RS 2015 Nr. 2 (Bruch zwischen zwei Brüchen), 2013 Nr. 2 (Mitte), 2024 Nr. 5 (Menge aus Anteil) | größte gemischte Zahl aus Ziffern; zwei Fehleraufgaben |
| bruch.brueche | `zahlbereiche` – Brüche als Zahlen, auch negativ | vor verstehen | M6 1.1 (Zusammenhang ℕ/ℤ/ℚ, negative Bruchzahlen am Zahlenstrahl ordnen), 1.2 (Bruch als Quotient) | GWT RS 7 2013 Nr. 2 und Nr. 5, 2022 Nr. 3 | „Nachfolger von 1/2?“, Anzahl Brüche zwischen −1 und 0 |
| bruch.rechnen | `potenzen` – Potenzen von Brüchen und Dezimalzahlen | nach dezimal_geteilt | M6 1.4 („Potenzen mit natürlichen Exponenten und rationalen Basen“) | BMT8 2021 Aufg. 1, 2023 Aufg. 1c | Quadrat kleiner als die Zahl; (1/2)³ vs. (1/3)² |
| bruch.rechnen | `sach` – Sachaufgaben: Anteile von Anteilen | am Ende | M6 1.5 („Anteile von Anteilen“, Skizze, Überschlag) | BMT8 2014 B Aufg. 1c, 2023 Aufg. 5a; GWT RS 7 2024 Nr. 3 | Schokoladen-Rest rückwärts |
| bruch.dezimal | `merkwerte` – Merkwerte: Bruch, Dezimalzahl, Prozent | nach dezimal_zu_bruch | M6 1.2 (Umwandlung im Kopf; Rechneranzeige 0,166666667 reflektieren), M6 1.1 (Prozent als Schreibweise) | GWT RS 7 2009 Nr. 2 / 2023 Nr. 10, 2024 Nr. 14, 2008 Nr. 3 | zweitgrößte von 0,3; 1/3; 3/8; 0,35 |

### Erweiterte Karten (Kartentexte sonst unverändert)
| Thema | Karte | Ergänzt |
|---|---|---|
| bruch.brueche | `vergleichen` | 2 Schritte „Hauptnenner über die Primfaktorzerlegung“ (nach Schritt 1), Wort „Primfaktorzerlegung“, 6 Übungen (S2: 3, S3: 3; Vorbild GWT RS 7 2015 Nr. 2) |
| bruch.prozent | `verstehen` | 2 Schritte mit Säulenbild (Rad-Anteil 20 % → 25 %: +5 Prozentpunkte, aber +25 %), Wort „Prozentpunkte“, 6 Übungen (S2: 2, S3: 4; Vorbilder BMT8 2021 Aufg. 6c, GWT RS 7 2019 Nr. 18) |
| bruch.rechnen | `brueche_plus_minus`, `brueche_mal`, `brueche_geteilt` | je 1 Übung S2 + 1 S3 mit gemischter Zahl als Ergebnis (Lücke „□ □/□“); keine Textänderung |

Zahlen: bruch.brueche 272 → 334 Aufgaben, bruch.rechnen 340 → 402, bruch.dezimal 238 → 266, bruch.prozent 238 → 244 (zusammen 202 neue Aufgaben, 5 neue Lernkarten).

### Was offen blieb bzw. abweicht
- Lücken 2 und 3 (Flächen, Volumen): nicht Teil dieses Auftrags (Teil A, Zweig luecken-neu).
- Lücke 7: Negative Brüche am Zahlenstrahl stehen in der neuen Karte `zahlbereiche` statt als Erweiterung von `zahlenstrahl` (so bleibt die freigegebene Karte unverändert). Falls gewünscht, später verschieben.
- Lücke 4: neue Karte in bruch.rechnen (zweite Möglichkeit unter „wohin“) statt Erweiterung von terme.potenzgesetze/potenz_begriff – Begründung: kein Eingriff in eine fremde freigegebene Karte; Potenzen rationaler Zahlen gehören laut Lehrplan zu M6 1.4 (Rechnen mit rationalen Zahlen).
- App-Wunsch: Die Lücke „□ □/□“ (gemischte Zahl) zeigt die App als drei Felder in einer Zeile mit „/“ dazwischen (lernen.js, allgemeine Lücken). Lesbar, aber schöner wäre ein gestapelter Restbruch wie bei „□/□“. Der Hinweistext sagt die Reihenfolge (Ganze, Zähler, Nenner).
- Die Einträge unter `offen` von bruch.rechnen und bruch.dezimal („gemischte Zahlen nur als unechter Bruch, weil die App kein Format □ □/□ hat“) sind dadurch teilweise überholt; nicht geändert, weil der Auftrag nur Neues erlaubt – bitte im Haupt-Chat anpassen.
- Einspielen: wie im Auftrag mit einheit_abgleichen(…, 'sperren'); die geänderten Erklärungen von `vergleichen` und `verstehen` dabei mit übernehmen.

## 2026-11-17 15:35 – STATUS
**bruch.dezimal** fertig: neue Karte `merkwerte` (nach dezimal_zu_bruch), 28 Aufgaben, Pflicht. Prüfskript OK, Nachweis JA.

## 2026-11-17 15:10 – STATUS
**bruch.prozent** fertig: Karte `verstehen` um ein zweites vorgerechnetes Beispiel (2 Schritte, Säulenbild 20 % → 25 %, Wort „Prozentpunkte“) und 6 Übungen (Prozent/Prozentpunkte, „jedes vierte“, „drei von fünf“, Zeitungsaussage prüfen) erweitert. Prüfskript OK, Nachweis JA.

## 2026-11-17 14:55 – STATUS
**bruch.rechnen** fertig: neue Karten `potenzen` (nach dezimal_geteilt) und `sach` (am Ende), je 28 Aufgaben, Pflicht; `brueche_plus_minus`, `brueche_mal`, `brueche_geteilt` je um 1 Übung Stufe 2 + 1 Stufe 3 mit gemischter Zahl als Ergebnis (Lücke „□ □/□“) erweitert, Kartentexte unverändert. Prüfskript OK, Nachweis JA.

## 2026-11-17 14:20 – STATUS
**bruch.brueche** fertig: neue Karten `gemischte_zahlen` (nach kuerzen) und `zahlbereiche` (vor verstehen), je 28 Aufgaben (Ü 4/6/8, Test 1, Korrektur 3, Sicherung 6), Pflicht; Karte `vergleichen` um 2 Schritte (Primfaktorzerlegung) und 6 Übungen erweitert. Prüfskript OK, Nachweis „nur Neues dazu“ JA (`python3 -I inhalte/generatoren/_luecken_kl6_nachweis.py bruch.brueche vergleichen`).

## 2026-11-17 13:30 – STATUS: Bestandsaufnahme (Schritt 1)
Grundlage: inhalte/pruefung/aufbau/klasse6.json, Feld „luecken“ (Stand 14.11.), geprüft gegen inhalte/themen und inhalte/themenliste.json auf lernen-app (4a71771).
Lehrplan-Bezug nachgelesen auf lehrplanplus.bayern.de (Fachlehrplan Mathematik Gymnasium 6): M6 1.1–1.5 und M6 3 – Wortlaut deckt alle Einträge unten.

| # | Lücke (kurz) | Dringl. | Stand heute | Plan |
|---|---|---|---|---|
| 1 | Gemischte Zahlen lesen, umwandeln, damit rechnen (M6 1.3/1.4) | hoch | **offen**. Keine Lernkarte; in bruch.rechnen nur einzelne Aufgaben mit gemischten Zahlen in der Frage (Zehnte Runde), Ergebnis immer als unechter Bruch | bruch.brueche: neue Karte `gemischte_zahlen` nach `kuerzen`; bruch.rechnen: je 1 Übung Stufe 2 + 1 Stufe 3 mit gemischter Zahl als Ergebnis in `brueche_plus_minus`, `brueche_mal`, `brueche_geteilt` (Lücke „□ □/□“) |
| 2 | Flächen Parallelogramm/Dreieck/Trapez (M6 2.1) | hoch | nicht Teil dieses Auftrags (neues Thema messen.flaechen_vielecke, Teil A) | – |
| 3 | Volumen (M6 2.2) | hoch | nicht Teil dieses Auftrags (neues Thema messen.volumen, Teil A) | – |
| 4 | Potenzen mit rationaler Basis (M6 1.4) | mittel | **offen** (teilweise: einzelne Übungen aus der Zehnten Runde, z. B. (1/10)⁴, 0,25³ · 8³; keine Erklärung) | bruch.rechnen: neue Karte `potenzen` nach `dezimal_geteilt` (zweite Möglichkeit unter „wohin“; so bleiben alle Karten von terme.potenzgesetze unverändert) |
| 5 | Prozent und Prozentpunkte; Prozentangaben in Texten prüfen (M6 3) | mittel | **offen** (teilweise: 2 Übungen zu Prozentpunkten aus der Zehnten Runde; Erklärung fehlt) | bruch.prozent: Karte `verstehen` um zweites vorgerechnetes Beispiel (2 Schritte mit Bild, Wort „Prozentpunkte“) und 6 Übungen erweitern |
| 6 | Anteile von Anteilen, Sachaufgaben mit Skizze/Überschlag (M6 1.5) | mittel | **offen** (teilweise: einzelne Übungen „Anteil vom Anteil“ in `brueche_mal`; keine Sachkarte) | bruch.rechnen: neue Karte `sach` am Ende |
| 7 | Brüche als Zahlen: negative Brüche ordnen, ℕ/ℤ/ℚ, Bruch als Quotient (M6 1.1/1.2) | mittel | **offen** | bruch.brueche: neue Karte `zahlbereiche` vor `verstehen`. Abweichung: Die negativen Brüche am Zahlenstrahl kommen in diese neue Karte statt als Erweiterung von `zahlenstrahl` – so bleibt `zahlenstrahl` unverändert (freigegeben, Fortschritt) |
| 8 | Teilbarkeit, ggT/kgV, Primfaktorzerlegung | hoch | **erledigt** (zahlen.teilbarkeit, Klasse 5, mit Karten primfaktoren, ggt, kgv); Teil „in bruch.brueche bei `vergleichen` Hauptnenner über Primfaktorzerlegung vorrechnen“: **offen** | bruch.brueche: Karte `vergleichen` um 2 Schritte (Primfaktorzerlegung) und 6 Übungen erweitern |
| 9 | Kopfrechnen mit Merkwerten 1/2 = 0,5 = 50 % … (M6 1.2) | niedrig | **offen** | bruch.dezimal: neue Karte `merkwerte` nach `dezimal_zu_bruch` |

Verschieben von Lernkarten zwischen Themen: nicht nötig, keins gemeldet.
