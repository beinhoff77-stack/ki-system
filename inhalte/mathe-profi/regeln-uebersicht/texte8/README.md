# Texte, achte Runde (Mathe-Profi, 27.11.2026)

Zweig `helfer-regeltext`. Prüfen: `python3 -I inhalte/mathe-profi/regeln-uebersicht/texte8/pruefen.py` (endet mit „OK“, 211 gerechnete Zahlenprüfungen, Pflichtfelder, Längen, Kennungen, Aufgaben-Verweise). **[G]** gesichert, **[A]** Annahme.

## Geliefert (alles Daten, Kennungen wie `kennungen.json`)
| Datei | Inhalt |
|---|---|
| `kurzbeschreibungen.json` | 42 geprüft (14 Regeln, 28 Ideen): 24 in Ordnung, **18 berichtigt** (Regeln 3, 5, 8, 9, 10, 11; 12 Ideen). Feld `endfassung` ist der zu übernehmende Text. |
| `merksaetze.json` | 14 gegengelesen: **0 falsch, 0 geändert**, 25 Lücken in „Genau gesagt / Wann sie gilt / Fehler“ mit fertigem Text; Regel 10 Kurzfassung; Regel 6 optionaler Vorschlag. |
| `arbeitsweisen.json` | 8 mit Kurzbeschreibung, Beispiel (Klasse 5, nachgerechnet), Erklärung (2–3 Sätze). |
| `beispielaufgaben.json` | Regel 10 und 14: je 3 (+ weitere) aus `inhalte/themen/`; Stichprobe der bestehenden Zuordnung (5 Regeln). |
| `einzelregeln.json` | Von 103 Einzelregeln je 15 dringlichste für Klasse 5 und 8, je Beispiel und „gilt nicht / Fehler“. |
| `lehrplan.json` | Lehrplan-Bezug je Rechenregel aus Repo-Quellen mit Pfaden. |

## Was geprüft ist [G]
- Kurzbeschreibungen: Maßstab ein Satz, höchstens 110 Zeichen, sagt worum es geht, wiederholt den Merksatz nicht. Fachlich falsch ohne Bedingung: Idee Daten 3 (Wahrscheinlichkeit „Anteil an allen Möglichkeiten“ gilt nur bei gleich wahrscheinlichen Ergebnissen) und Regel 11.
- Merksätze: alle fachlich richtig. Grenzen standen meist schon in `voraus`/`fehler`; es fehlten u. a. Doppel-Minus (R2), Bruchstrich als Klammer und Potenzturm (R4), Plus vor der Klammer und Produkt in der Klammer (R6), gemischte Zahlen und falscher Kehrwert (R10), „durch x teilen“ (R14). Bestandstext R11 „gilt nur bei direkter Proportionalität“ ist für das Vorgehen „auf eins“ zu eng (geht auch umgekehrt proportional).
- Regel 10, kürzere Fassung (88 Zeichen, statt 110): „Plus, Minus: gleiche Nenner. Mal: oben mal oben, unten mal unten. Geteilt: mal Kehrwert.“ Kompakt (78): „Plus/Minus: gleiche Nenner. Mal: oben·oben, unten·unten. Geteilt: mal Kehrwert.“
- Zuordnung bestehender Aufgaben (`schritt1`): R6 passt (5 von 5), R4 2 von 3, **R9: BG-05 passt nicht** (über Kreuz = Waage), **R11: BG-01/02/09 fraglich** (über Kreuz, kein „auf eins“).
- Lehrplan: Das Thema der Einführung steht in `themenliste.json` und in der Lehrplan-Kopie. Die Regel selbst ist nirgends geprüft; der Lehrplan nennt Themen.

## Annahmen [A]
- Zeilenzahl der Kurzfassung am Handy nicht gemessen (Maßstab: die anderen Merksätze mit höchstens 75 Zeichen brauchen zwei Zeilen).
- Dringlichkeit der 30 Einzelregeln ist meine Einschätzung; Kriterium: wie viel darauf aufbaut, wie häufig der Fehler ist.
- Kennungen `aw.*` für Arbeitsweisen sind nur Vorschläge (Bestand: Arbeitsweisen haben keine).
- Beispielaufgaben sind über Datei, Lernkarte und Stelle in `aufgaben` benannt; Aufgaben haben keine eigene Kennung.

## Was der Designer-Entwurf übernehmen muss
1. `entwurf7/teile/kurz.json`: 18 Einträge durch `endfassung` ersetzen (Liste: `befund` = berichtigt).
2. Liste der 14 Regeln: Merksatz Regel 10 durch Kurzfassung ersetzen, falls der Projektleiter zustimmt (sonst drei Zeilen).
3. Regelseite „Wann sie gilt – und wann nicht“, „Genau gesagt“, „Typische Fehler“: 25 Lücken aus `merksaetze.json` (Feld `wo`) in `inhalt.json` ergänzen.
4. Arbeitsweisen (`#weise-1` bis `#weise-8`): Kurzbeschreibung, Beispiel, Erklärung; Kasten „Noch offen“ entfällt.
5. Ebene 3: für 30 der 103 Regeln Beispiel und Grenze aus `einzelregeln.json`; Regel „Satz“ steht weiter in `inhalt.json`.
6. Lehrer-Blatt: Tabelle Lehrplan aus `lehrplan.json`; Beispielaufgaben R10 und R14 aus `beispielaufgaben.json`; Zeile „nicht geprüft“ bleibt stehen.
7. `kennungen-zuordnung.json` (Mathe-Profi): BG-05 nach `rr.waage`; BG-01/02/09 Entscheidung des Projektleiters.
8. Beispiel Regel 7 in Klasse 8 steht in `inhalt.json` (älter) anders als in `klassenleiter.json`; der Entwurf nutzt für „Durch die Klassen“ die Leitern, nicht `klassen`.

## Offene Fragen an den Projektleiter
- Merksatz Regel 6 verschärfen („Der Faktor vor der Klammer wird mit jedem Summanden in der Klammer malgenommen.“)? Nicht falsch, nur missverständlich.
- Kurzfassung Regel 10: ja oder drei Zeilen behalten?
- Sollen Verhältnisgleichungen („über Kreuz“) unter Regel 11 laufen? Dann ändert sich der Satz von Regel 11, sonst gehören BG-01/02/09 zu Regel 13.
- Wer prüft LehrplanPLUS an der Quelle (im Repo liegt nur Themenliste und eine Kopie in der App-Datenbank)?
- Soll es stabile Kennungen für Aufgaben und für Arbeitsweisen geben?
- Klassenangabe Einzelregel V7 „Änderungsrate“ (Gymnasium 5) prüfen; D9 Standardabweichung nennt nur die Grundgesamtheit.
