# klar-kl7 – Erklärungen verständlich machen (Klasse 7)

Zweig klar-kl7, abgezweigt von lernen-app 284d809. Themen der Klasse 7 laut themenliste.json (gym_by 7): bruch.prozent_grundwert, terme.aufstellen,
abbildungen.kongruenz, geometrie.konstruktion, geometrie.kreis, daten.boxplot, gleichungen.linear.
Prüfung je Thema: Generator neu ausgeführt, Aufgaben mit einem Vergleichsskript gegen `git show HEAD:inhalte/themen/<thema>.json` verglichen
(Feld für Feld, Reihenfolge eingeschlossen), außerdem: jede Karte hat einstieg und woerter, 3–5 Schritte, keine Wörter „einfach/offensichtlich/trivial“ in einstieg/schritte.

## Status

## 2026-11-16 04:30 – FERTIG

Siebte Runde, Klasse 7 abgeschlossen. Alle 45 Lernkarten der 7 Themen haben jetzt einstieg und woerter; schritte (je 3–5 ganze Sätze), regel (als Handlungsanweisung „So …“), fehler (in der Alltagssituation gedeutet) und Bildbeschriftungen sind nach dem Maßstab überarbeitet. Technisch wie im Muster: Abschnitt KLAR im Generator, der die Kartenfelder überschreibt.

| Thema | Lernkarten | Aufgaben | Unterschiede zu lernen-app (284d809) | Situation |
|---|---|---|---|---|
| bruch.prozent_grundwert | 7 | 168 | 0 | Preise im Sportgeschäft |
| terme.aufstellen | 6 | 144 | 0 | Fahrradverleih am See |
| abbildungen.kongruenz | 7 | 168 | 0 | Klecksbild, Pfosten, Pauspapier, Fliesen |
| geometrie.konstruktion | 7 | 168 | 0 | Stadtplan, Gartenhaus-Giebel, Holzleisten, Drachen, Regen |
| geometrie.kreis | 6 | 144 | 0 | Freilichtbühne, Geodreieck zwischen Nägeln, Pfütze, Fahrrad, Treffpunkt |
| daten.boxplot | 6 | 144 | 0 | Umfragen in der Schule |
| gleichungen.linear | 6 | 162 | 0 | Balkenwaage, Obsttüten, Handytarife |

- Aufgaben: in allen 7 Themen Feld für Feld identisch mit lernen-app (Vergleichsskript gegen `git show origin/lernen-app:inhalte/themen/<thema>.json`), Generatoren reproduzierbar (zweiter Lauf ohne Änderung).
- Prüfskript `python3 -I tools/inhalt_pruefen.py`: OK für alle 7.
- Zusatzprüfung: keine Wörter „einfach/offensichtlich/trivial“ in einstieg/schritte; alle Zahlen der Alltagssituationen nachgerechnet.
- Fachlich präzisiert: geometrie.konstruktion, Karte vierecke – beim Drachenviereck sind die beiden Winkel gleich, die nicht auf der Symmetrieachse liegen (vorher „neben der Symmetrieachse“, missverständlich). geometrie.kreis: „Der Überlieferung nach“ bei Thales.
- Beispielzahlen der Karten wurden beibehalten (nur in Sachzusammenhang gestellt); _verbot-Listen unverändert.
- gleichungen.linear steht in der Klasse-7-Liste und wurde mitbearbeitet (Generator gleichungen_linear.py, Baukasten _nachbau).
- Nicht geprüft: Anzeige in der App selbst (nur JSON und Prüfskript).
- Nicht gemergt. Merge nach lernen-app/main erst nach „Live“.

## 2026-11-16 04:20 – STATUS
gleichungen.linear fertig: 6 Karten (Balkenwaage mit Dosen, Obsttüten für Klammern, Handytarife für Sonderfälle und Sachaufgaben). Aufgaben: 162, 0 Unterschiede. inhalt_pruefen: OK.

## 2026-11-16 04:00 – STATUS
daten.boxplot fertig: 6 Karten (Umfragen in der Schule: Schulweg, gelesene Bücher, Taschengeld mit Ausreißer, Quiz-Punkte, Laufzeiten zweier Klassen). Zahlen der bisherigen Beispiele beibehalten, nur in Sachzusammenhang gestellt. Bilder: Säulen mit „Anzahl Kinder“ / „… Bücher“, Boxplots mit Einheit. Aufgaben: 144, 0 Unterschiede. inhalt_pruefen: OK.

## 2026-11-16 03:40 – STATUS
geometrie.kreis fertig: 6 Karten (Freilichtbühne mit Halbkreis-Plätzen für Thales, Geodreieck zwischen zwei Nägeln für die Umkehrung, Messen mit Geometrieprogramm vs. Beweis, Ball an der Pfütze für Passante/Tangente/Sekante, Fahrrad auf der Straße für den Berührradius, Treffpunkt dreier Freunde für den Umkreis). Aufgaben: 144, 0 Unterschiede. inhalt_pruefen: OK.

## 2026-11-16 03:20 – STATUS
geometrie.konstruktion fertig: 7 Karten (Stadtplan mit parallelen Straßen, Giebel eines Gartenhauses, Dreiecke aus Holzleisten am Telefon, Drachen/Scherengitter, Regen und nasse Straße). Fachlich präzisiert: Drachenviereck – gleich sind die beiden Winkel, die nicht auf der Symmetrieachse liegen (vorher missverständlich „neben der Symmetrieachse“). Aufgaben: 168, 0 Unterschiede. inhalt_pruefen: OK.

## 2026-11-16 03:00 – STATUS
abbildungen.kongruenz fertig: 7 Karten, durchgehend Klecksbild (Achsenspiegelung), Pfosten auf dem Schulhof (Punktspiegelung), Pauspapier (Verschiebung, Drehung mit Reißzwecke, Eigenschaften), Fliesen (Parkett). Bild symmetrie: Achsen als „Symmetrieachse“ beschriftet. Aufgaben: 168, 0 Unterschiede. inhalt_pruefen: OK.

## 2026-11-16 02:40 – STATUS
terme.aufstellen fertig: 6 Karten, durchgehende Situation Fahrradverleih am See (Termart, Termwert, Übersetzen, Preistafel als Term, Streichholzmuster, Handytarif deuten). Aufgaben: 144, 0 Unterschiede. inhalt_pruefen: OK.

## 2026-11-16 02:20 – STATUS
bruch.prozent_grundwert fertig: 7 Karten mit einstieg/woerter (durchgehende Situation: Preise im Sportgeschäft), Schritte als ganze Sätze, Merksätze als Handlungsanweisung, Bildbeschriftungen sprechend (neue Tabelle bei prozentsatz). Aufgaben: 168, 0 Unterschiede. inhalt_pruefen: OK.
