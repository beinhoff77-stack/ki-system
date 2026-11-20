# Postfach Chat `kann-2` (AB-I, Klasse 7 und 8)

## 2026-11-20 – FERTIG: AB-I, Chat 2

Zweig `kann-2` (von `lernen-app` @ `dc76450`). 23 Dateien `inhalte/kann/<thema_schluessel>.json` – alle Themen mit `klasse.gym_by` 7 oder 8 laut `inhalte/themenliste.json`, je mit `kurz` und `kann` für jede Etappe (165 Etappen). Grundlage je Etappe: Titel, Regel, Erklärung und die Aufgaben der Etappe (Übung Stufe 1–3, Test, Korrektur, Bonus) in `inhalte/themen/<thema>.json`.

Commits: einer für Klasse 7 (9 Themen), einer für Klasse 8 (14 Themen), dazu dieser Bericht. Nichts außerhalb von `inhalte/kann/` geändert außer dieser Meldung; keine Themendateien, Generatoren, App-Code oder Datenbank; kein Merge.

Die 10 aufgelösten Themen haben kein `gym_by` 7/8 (nur `rs_by`/`ib_myp`) – fallen in diesem Chat also ohnehin nicht an.

| Klasse | Thema | Etappen | kurz (Zeichen) | längster kann-Text |
|---|---|---|---|---|
| 7 | `bruch.prozent_grundwert` (Vermehrter und verminderter Grundwert) | 8 | 92 | 90 |
| 7 | `terme.aufstellen` (Terme aufstellen und deuten) | 6 | 85 | 83 |
| 7 | `terme.umformen` (Terme umformen) | 12 | 92 | 90 |
| 7 | `abbildungen.kongruenz` (Kongruenzabbildungen) | 10 | 90 | 84 |
| 7 | `geometrie.winkelsaetze` (Winkelsätze) | 9 | 98 | 90 |
| 7 | `geometrie.konstruktion` (Konstruktionen, Kongruenz und Beweise) | 6 | 98 | 88 |
| 7 | `geometrie.kreis` (Kreis und Tangenten) | 6 | 89 | 88 |
| 7 | `daten.boxplot` (Median, Quartile, Boxplot) | 6 | 90 | 81 |
| 7 | `gleichungen.linear` (Lineare Gleichungen) | 6 | 92 | 83 |
| 8 | `gleichungen.ungleichungen` (Lineare Ungleichungen) | 7 | 101 | 87 |
| 8 | `zahlen.intervalle` (Intervalle) | 4 | 81 | 80 |
| 8 | `terme.bruchterme` (Bruchterme) | 7 | 63 | 86 |
| 8 | `gleichungen.formeln` (Formeln umstellen) | 5 | 86 | 85 |
| 8 | `gleichungen.bruch` (Bruch- und Verhältnisgleichungen) | 7 | 95 | 81 |
| 8 | `gleichungen.lgs2` (Gleichungssysteme mit 2 Unbekannten) | 9 | 77 | 84 |
| 8 | `funktionen.grundbegriffe` (Zuordnung und Funktion) | 9 | 105 | 81 |
| 8 | `funktionen.linear` (Lineare Funktionen) | 11 | 96 | 83 |
| 8 | `funktionen.gebrochen` (Gebrochen-rationale Funktionen) | 5 | 88 | 89 |
| 8 | `messen.koerper_darstellung` (Körper darstellen) | 6 | 100 | 82 |
| 8 | `messen.kreisberechnung` (Kreisberechnungen) | 6 | 75 | 89 |
| 8 | `messen.prisma_zylinder` (Prismen und Zylinder) | 7 | 98 | 81 |
| 8 | `stochastik.grundbegriffe` (Zufall und Laplace) | 6 | 96 | 84 |
| 8 | `groessen.indirekt` (Indirekte Proportionalität) | 7 | 84 | 89 |

### Selbstprüfung (Skript, gegen die Dateien auf dem Zweig)
Geprüft: gültiges JSON; genau die Felder `thema_schluessel`, `kurz`, `etappen`; Schlüssel stimmt mit Dateiname; jede Etappe (`lernziel` aus `inhalt.etappen`) hat genau einen Eintrag, keine überzähligen; `kurz` ≤ 110 Zeichen; `kann` ≤ 90 Zeichen, klein begonnen, ohne Punkt am Ende, enthält den Etappen-Titel nicht wörtlich; keine fremden Dateien in `inhalte/kann/`.

```
Klassen [7, 8]: 23 Themen, 165 Etappen, 23 Dateien, fremde Dateien: keine
kurz: max 105 Zeichen (Grenze 110) · kann: max 90 Zeichen (Grenze 90)
Fehler: keine
```

### Entscheidungen / Hinweise
- „Klein begonnen“ streng gelesen: erstes Zeichen ist ein Kleinbuchstabe. Sätze, die mit einem Hauptwort beginnen würden („Punkte spiegeln …“), sind umgestellt („einen Punkt … spiegeln“).
- Fachwörter in `kurz` vermieden, die erst im Flug erklärt werden (z. B. kein „Median“, „Asymptote“, „Laplace“, „Thales“, „Tangente“, „Äquivalenz“).
- `terme.umformen` enthält vier Potenz-Etappen (`mal_gleiche_basis`, `gleicher_exponent`, `geteilt_gleiche_basis`, `anwenden`); die Texte beschreiben diese, `kurz` bleibt bei „Rechenausdrücke kürzer schreiben“.
- `bruch.prozent_grundwert` enthält die Etappe `formel` (Zinseszins Kₙ = K₀ · qⁿ); `kann` nennt das, `kurz` nur Erhöhung/Rabatt/Zurückrechnen.
- Fachlich bewusst knapp: Werte mit genau 90 Zeichen (Grenze eingehalten) bei `bruch.prozent_grundwert/vermindert`, `terme.umformen/ausklammern` u. a. – falls die App weniger Platz hat, bitte melden.
- Offen: keine.

FERTIG: AB-I, Chat 2
