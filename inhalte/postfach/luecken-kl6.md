# Postfach luecken-kl6 (Achtzehnte Runde, Teil B, Klasse 6)

Neueste Meldung oben.

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
