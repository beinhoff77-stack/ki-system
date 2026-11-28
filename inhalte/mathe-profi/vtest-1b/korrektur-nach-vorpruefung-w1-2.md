# Korrektur nach Vorprüfung W1-2 – Einheit 20 `gleichungen.bruch` (VT1B-022 bis 041)

Grundlage: `vorpruefung-w1-2.md` (7 A, 7 B, 7 C, Stand 06db098c). Geändert wurde nur, was ein Befund verlangt. Unverändert sind 023, 024 (bis auf den Wortlaut, C7), 025, 029 (bis auf „hier“, C5), 031, 038, 039 und 040. Die Tabellen in `korrektur-nach-vorpruefung-w1.md` gelten für den Stand 06db098c; der aktuelle Stand steht unten.

Gemeinsame Dateien: `bauen.py`, `kern.py`, `vorrat_liste.py` und `tools/` sind unverändert. Die Einheiten 11, 35, 42 und 93 und der Vorrat der Einheit 20 sind byte-gleich. Am Dateiende von `th_gleichungen_bruch.py` steht eine neue Prüfung, die nur für diese Einheit gilt (A7). In `gegenrechnung.py` ist nur der Block der Einheit 20 neu gefasst. In `readme_vorlage.md` sind nur die Zeilen der Einheit 20 geändert.

## Befunde A

| Nr. | geschlossen wie |
|---|---|
| A1 | 022: Toms Teil ist gestrichen. Leas Gleichung steht wörtlich im Text. Die zweite Lücke lautet „Leas Gleichung schließt □ Zahlen aus“, Lösung [0; 3]. |
| A2 | 022 behandelt nur noch „Addieren eines Bruchs verkleinert D, die Lösung geht verloren“. 032 behandelt „Kürzen vergrößert D“. |
| A3 | 032 ist neu gefasst: (x² + 4x)/(x² − 4x) = −1, als Lückenaufgabe ohne Hinweis auf die Richtung und ohne Ina. Gefragt sind drei Zahlen: Lösungen der gekürzten Gleichung, Lösungen der Ausgangsgleichung, Zahl der ausgeschlossenen Zahlen; Lösung [1; 0; 2]. Damit gibt es auch keinen Nebensatz mehr in einer Möglichkeit. Der Nenner ist ein anderer als in BT 36 (x² − 2x); zur Nähe zu T 224 siehe `bestandsvergleich.md`. 033 hat jetzt nur noch einen Wert: 7/(x − 4) + 2/x = c/(x² − 4x), Scheinlösung 4, also c = 28. |
| A4 | 028 ist allgemein gestellt mit beliebigen p, q (p ≠ −q). Man kann keine Lösung ausrechnen, nur das Verhältnis der Zähler entscheidet; Lösung a = 6, nachgerechnet für alle p, q von −4 bis 4. 031 bleibt die eine Schema-Aufgabe. |
| A5 | 035 ist neu: ein Fehler-Detektiv, in dem alle Rechnungen stimmen; der Denkfehler ist die Probe in der umgeformten Gleichung. 036 ist neu: Welche Aussage ohne Brüche hat für jede Zahl c dieselbe Lösungsmenge wie 4/(x + 2) + 1/x = c/(x² + 2x)? Richtig ist die Aussage mit beiden Bedingungen. Kein Einzelfall lässt sich einfach ausrechnen, und es gibt keine Graphen-Differenz. 034 bleibt die eine Schema-Aufgabe, jetzt mit eigenem Rechenkern: zwei verschiedene lineare Nenner und ihr Produkt, Kandidat 2 verboten. |
| A6 | Die alte 036 (R8-V053) ist ersetzt, siehe A5. |
| A7 | 035 hat nicht mehr die Form „immer – manchmal – nie“. In 030 ist die richtige Aussage „Sie haben nie mehr als eine Lösung“ (Voraussetzung a ≠ b, c ≠ d, b ≠ d; geprüft für alle a, b, c, d von −4 bis 4: nur 0 oder 1 Lösung, beides kommt vor). Die Ablenker sind „immer genau eine“, „nie eine“ und „können zwei haben“. Fest geprüft wird das im Bauskript, nur für diese Einheit: Mindestens eine richtige Möglichkeit trägt ein Absolutwort, und höchstens einmal ist die richtige die einzige ohne Absolutwort. |

## Befunde B

| Nr. | geschlossen wie |
|---|---|
| B1 | 027: a ≠ 0 ist vorgegeben. Gefragt sind nur der Über-Kreuz-Fall (a = 7, 0 · x = 49) und die Lösung für a = 14 (x = 9); Lösung [7; 9]. Damit gibt es keine Überschneidung mehr mit 033. 037: einfachere Zahlen (200 ml A im Verhältnis 1 : 1, B im Verhältnis 1 : 3, Ziel 1 : 2, Ergebnis 400 ml, nur Viertel). Ein neues Fehlbild beschreibt das Addieren der Verhältniszahlen (C3). |
| B2 | 026 ist ohne Rückwärts-Teil: Der Term ist nur in Worten gegeben, gefragt ist die Zahl der ausgeschlossenen Zahlen in ℤ und in ℚ; Lösung [2; 3]. 023 bleibt. |
| B3 | 033 hat nur noch einen Wert, und K8-V081 ist in `abgrenzung` bzw. `bestandsvergleich.md` genannt. |
| B4 | 034 hat einen neuen Rechenkern, siehe A5. |
| B5 | 032 hat den Nenner x² − 4x statt x² − 2x. |
| B6 | **Offen, gemeldet statt gedehnt.** Ehrlich wäre für 024, 038 und 034 (Modell aufstellen bzw. Rätsel) `typ: transfer`. Das ist Stufe 3, und `bauen.py` verlangt für die Korrektur Stufe 2. Für 034 als Schema-Aufgabe wäre ehrlich, gar kein Verstehens-Etikett zu setzen, aber dann meldet `tools/vtest_pruefen.py` einen FEHLER (V5). Beides kann ich nur ändern, wenn das Bauskript oder das Werkzeug angepasst wird oder wenn diese Aufgaben ihren Pool tauschen. Ein Tausch würde die Stufenmischung der Sicherung brechen. Die Etiketten `einkleidung` + `bruecke` stehen deshalb unverändert da. |
| B7 | 041 ist neu: aus a : b = 4 : 5 bestimmen, um wie viel Prozent b größer ist als a (25 %). Es geht um den Bezugswert eines Verhältnisses; 039 (Anteil halbieren) bleibt. 041 ist die eine Schema-Aufgabe von verhaeltnis. |

## Befunde C

C1, C6: ohne Änderung. C2: Mit A7 erledigt, denn a ≠ b und c ≠ d sind vorgegeben, und der Lösungsweg nennt den ausgeschlossenen Fall „unendlich viele“. C3: siehe B1. C4: Mit A5 erledigt. C5: „hier“ steht jetzt auch im Ablenker „Beide Wege sind hier erlaubt, führen aber …“. C7: 024 fragt jetzt „wie groß muss x für die Sachaufgabe mindestens sein (x größer als welche Zahl)“.

## Neu oder geändert

- Neu: 026, 028, 032, 033, 034, 035, 036, 041 (Inhalt).
- Geändert: 022, 027, 030, 037; Wortlaut 024, 029.
- Unverändert: 023, 025, 031, 038, 039, 040.

## Schema je Lernziel (eigene Zählung)

| Lernziel | Schema | Grenzfall |
|---|---|---|
| definitionsmenge | – | 026 (Nullstellen bestimmen und mit ℤ abgleichen, nur über den Text) |
| ueber_kreuz | 031 | – |
| scheinloesung | 034 | 035 (Fehler-Detektiv, aber der Fehler ist ein Denkfehler, keine Rechnung) |
| verhaeltnis | 041 | 040 (Regel der indirekten Proportionalität) |

## Prüfläufe

- `bauen.py` endet mit `OK`: 157 Lösungen zweifach gerechnet, 398 Fehlbilder, 0 Doppelungen, `vorrat_pruefen` 0 Meldungen.
- `tools/vtest_pruefen.py --runde 1b` meldet nur die vier Pool-Meldungen.
- `gegenrechnung.py` meldet 0 Abweichungen; 14 Aufgaben der Einheit werden darin neu gerechnet.

## Offene Zweifel

- B6, siehe oben.
- 022 und 032 haben eine ähnliche Antwortform (Zahl der Lösungen, Zahl der ausgeschlossenen Zahlen), aber verschiedene Denkfiguren: Addieren verkleinert D, Kürzen vergrößert D.
- 027 ist jetzt leichter. Ob er noch die anspruchsvollste Aufgabe von ueber_kreuz ist, entscheidet sich gegen 028 (allgemein mit p, q) und 030.
- 036: Die richtige Möglichkeit ist die einzige mit zwei Bedingungen. Gleich gebaut ist sie trotzdem, denn alle vier Möglichkeiten beginnen mit „5x + 2 = c, wobei …“.
