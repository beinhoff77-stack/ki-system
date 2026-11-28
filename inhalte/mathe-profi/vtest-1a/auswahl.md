# Runde VT1A (Verstehen in Tests, Klasse 5): Auswahl der Lernziele

Stand: 28.11.2026. Die Auswahl steht vor dem Schreiben der Aufgaben. Quelle der Lernziele: `inhalte/themen/<einheit>.json`, `inhalt.bewertung.lernziele_pflicht` (Reihenfolge der Etappen).

## Zahlen im Repo (Abgleich mit dem Auftrag)

| Einheit | Pflicht-Lernziele im Repo | Auftrag nannte | Abweichung |
|---|---|---|---|
| `zahlen.potenzen_basis` | 7 | 7 | keine |
| `zahlen.rechengesetze` | 14 | 14 | keine |

Hälfte (aufgerundet): 4 bzw. 7. Je gewähltem Lernziel 6 Aufgaben (1 test, 2 korrektur, 3 sicherung): 11 Lernziele, 66 Aufgaben.

## Grundsatz: nichts aus späteren Klassen

Die Einheit `zahlen.rechengesetze` enthält im Bestand die Etappen `mal_ganz`, `geteilt_ganz` (ganze Zahlen mit Vorzeichen); `zahlen.potenzen_basis` die Etappe `negativ` (negative Basis). Das Rechnen mit negativen Zahlen steht im Lehrplan nicht in Klasse 5 (Repo-Vermerk: „Etappen zu ·/: ganzer Zahlen = M5 2, kommt im Lehrplan danach“). Diese drei Lernziele werden **nicht gewählt**. In allen gewählten Lernzielen rechnen die neuen Aufgaben nur mit natürlichen Zahlen.

## zahlen.potenzen_basis (4 von 7)

| Nr. | Lernziel | gewählt | Begründung |
|---|---|---|---|
| 1 | schreibweise | ja | Basis und Exponent gehören zusammen mit „wie oft dasteht“; hier gibt es die häufigsten Fehlvorstellungen (2⁵ = 10), also viel Begründbares. |
| 2 | berechnen | nein | Ausrechnen ist Verfahren; das Verstehen steckt schon in `schreibweise`. |
| 3 | quadrat | ja | Quadratzahl heißt „Zahl mal sich selbst“; rückwärts („welche Zahl wurde quadriert?“) und als Fläche lässt sich echtes Denken prüfen. |
| 4 | vertauschen | nein | Vertauschen von Basis und Exponent lässt sich in `schreibweise` und `zehner` mitprüfen; sonst nur Ausrechnen und Vergleichen. |
| 5 | zehner | ja | Zehnerpotenzen: Zusammenhang Exponent und Nullen, Darstellung wechseln, Größenordnung begründen. |
| 6 | negativ | nein | Negative Basis ist Stoff mit negativen Zahlen, nicht Klasse 5. |
| 7 | sach | ja | Wachstum durch wiederholtes Malnehmen: Transfer auf neue Situationen, Rückwärtsdenken. |

Gewählt: 1, 3, 5, 7 (jede zweite Etappe, `negativ` ausgelassen).

## zahlen.rechengesetze (7 von 14)

| Nr. | Lernziel | gewählt | Begründung |
|---|---|---|---|
| 1 | punkt_strich | nein | Reine Reihenfolge-Regel; das Verstehen prüfen `klammern` und `termaufbau` mit. |
| 2 | klammern | ja | Klammern setzen, damit ein vorgegebenes Ergebnis herauskommt; Wirkung der Klammer erklären. |
| 3 | termaufbau | ja | Punkt vor Strich in Sachsituationen als Term aufstellen und deuten; Term einer Rechengeschichte zuordnen. |
| 4 | vorteil | ja | Rechenvorteile erkennen und begründen; Tauschen und Verbinden zweier Wege vergleichen. |
| 5 | differenz_summe | nein | „Das Minus wandert mit“ wird in `vorteil` und `verteilen` (Fehler bei Minus) mitgeprüft. |
| 6 | verteilen | ja | Verteilungsgesetz als Flächenbild und als Rechenvorteil; typischer Fehler „nur den ersten Summanden“. |
| 7 | kopfrechnen | nein | Inhaltlich sehr nah an `verteilen` und `vorteil`; würde dieselbe Einsicht doppelt prüfen. |
| 8 | mal_ganz | nein | Ganze Zahlen (Vorzeichen), nicht Klasse 5. |
| 9 | geteilt_ganz | nein | Ganze Zahlen (Vorzeichen), nicht Klasse 5. |
| 10 | umkehraufgabe_mal | ja | Umkehren: Mal mit Geteilt, Geteilt mit Mal; „12 : □ = 3“ ist nicht „12 − 3“; nur natürliche Zahlen. |
| 11 | ueberschlag | ja | Überschlag begründen: wann ist er sinnvoll, was sagt er über das Ergebnis, Fehler erkennen. |
| 12 | schriftlich | nein | Verfahren; Verstehen nur über Fehler im Verfahren, das ist mit `ueberschlag` abgedeckt. |
| 13 | schriftlich_geteilt | nein | Verfahren (Teiler über 10). |
| 14 | sach | ja | Rückwärtsarbeiten in Sachsituationen: Schritte in umgekehrter Reihenfolge umkehren, Probe. |

Gewählt: 2, 3, 4, 6, 10, 11, 14. Nicht strikt „jede zweite“ (das hätte `mal_ganz`/`geteilt_ganz` getroffen und Verfahrens-Etappen bevorzugt); die Auswahl verteilt sich aber über alle fünf Abschnitte der Einheit (Reihenfolge, Gesetze, Umkehren, Überschlag, Sachaufgaben).

## Lehrplan-Bezug

Der Wortlaut des LehrplanPLUS war hier nicht einsehbar. Verwendet wird die Zuordnung, die das Repo führt (`inhalte/pruefung/klassen/vorschlag-rsib.md`): `zahlen.rechengesetze` und `zahlen.potenzen_basis` = **M5 1.3** (Grundrechenarten und Rechengesetze; Potenzen, Quadratzahlen bis 400, große Zahlen als Zehnerpotenz). Diese Zuordnung ist Stand des Repos, nicht amtlich nachgeprüft; Zweifel stehen in der README.
