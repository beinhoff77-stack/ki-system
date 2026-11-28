# Korrektur nach Vorprüfung W1 – Einheit 20 `gleichungen.bruch` (VT1B-022 bis 041)

Grundlage: `vorpruefung-w1.md` (9 A, 10 B, 10 C), Urteil 1222 und `vtest-1/auftrag.md`. Umfang wie vorher: 4 Lernziele × (1 Test + 2 Korrektur + 2 Sicherung) = 20 Aufgaben. Behalten wurden nur zwei Aufgaben ohne A- oder B-Befund: die Rückwärts-Aufgabe „a aus D“ (vorher 024, jetzt 023) und „(a + b) : b aus a : b“ (vorher 040, jetzt 041). Die anderen 18 Aufgaben sind neu. Die Ersatzvorschläge der Vorprüfung habe ich vorher gegen den ganzen Bestand geprüft; fünf davon stehen im Bestand oder treffen einen gesperrten Kern und wurden darum nicht übernommen (siehe A1, A2, A4, A5, A6).

Gelesener Bestand und Doppelungsabgleich je Aufgabe: `bestandsvergleich.md`, Abschnitt „Einheit 20 nach Vorprüfung W1“.

## Geänderte Dateien (nur Einheit 20)

- `th_gleichungen_bruch.py`: Aufgaben der Einheit neu. Die 8 Vorrat-Aufgaben stehen unverändert am Ende der Datei. Ihre Plätze der richtigen Möglichkeit sind mit `pos=` festgeschrieben, sie bleiben also wie bisher. Am Dateiende werden genau 10 Werte aus `POSITION4` verbraucht, so viele wie in der vorigen Fassung. Dadurch bleiben die Plätze in den folgenden Einheiten byte-gleich: Die JSON-Dateien von `bruch.prozent`, `terme.potenzgesetze`, `zahlen.potenzen_zehner` und `messen.flaechen_vielecke` sind unverändert, das ist mit `cmp` geprüft.
- `gleichungen.bruch.json`, `README.md`, `sonderfaelle.md`: von `bauen.py` neu erzeugt. In `README.md` und `sonderfaelle.md` ändern sich nur die Zeilen der Einheit 20 und die Summen.
- `vorrat-folgerunde/gleichungen.bruch_vorrat.json`: neu erzeugt. Inhaltlich gleich, nur das Feld `abgrenzung` folgt dem neuen Lernziel-Satz.
- `readme_vorlage.md`: die vier Zeilen zur Einheit 20 in „Denkfiguren je Lernziel“ und die Kennungen der Parameter-Aufgaben unter „Lehrplan, weiter offen“.
- `gegenrechnung.py`: Ich habe nur einen abgegrenzten Block `NEU.update({...})` vor `dateien = …` angehängt, mit eigener Neuberechnung von 12 Aufgaben. Die älteren Schlüssel der Einheit passen auf keinen Text mehr; ich habe sie nicht gelöscht, damit die Datei möglichst wenig geändert wird.
- `bestandsvergleich.md`: die vier Zeilen der Einheit 20 in der Tabelle verweisen jetzt auf den neuen Abschnitt am Ende.
- Nicht geändert: `bauen.py`, `kern.py`, `pruefhilfen.py`, `vorrat_liste.py`, `tools/`, alle anderen Einheiten.

## Befunde A (Muss)

| Nr. | Befund (kurz) | geschlossen wie |
|---|---|---|
| A1 | Test scheinloesung (032) ohne Scheinlösung, Denkfigur wie Test 022 | Neuer Test 032 mit echter Scheinlösung: (x² + 6x)/(x² − 2x) = −3. Kürzt man mit x, wird 0 zum Kandidaten. Gefragt ist, an welchem Schritt die Einschränkung x ≠ 0 verloren geht (zwei Wege, Auswahl). Den Vorschlag „(x + b)/(x − 4) = 3/(x − 4) + 2, b gesucht“ habe ich nicht übernommen: Sein Kern („Parameter so, dass die Gleichung wegen einer Scheinlösung keine Lösung hat, gleiche Nenner“) steht im Bestand (T 225, `rollend-7` K8-V081). |
| A2 | Test definitionsmenge (022) = Bestand T 233/T 237 (Identität) | Neuer Test 022: Was wird aus D bei einer Umformung? Lea addiert 1/x, damit wird die einzige Lösung 0 verboten. Tom multipliziert mit (x − 2), damit fällt die Einschränkung 2 weg. Den Vorschlag (Identität mit zwei Nennern, ganze Zahlen von −12 bis 12 zählen) habe ich nicht übernommen: Identität ist der Kern von T 237, und B1 verlangt weniger Abzählen. |
| A3 | 031 (gleiche Zahl zu Zähler und Nenner) = T 143 | Gestrichen. „Verfahren wählen“ steht jetzt als 031 in der Sicherung. Die Regel stammt aus T 130, die Aufgabe ist darum ehrlich als die Schema-Aufgabe des Lernziels gezählt. |
| A4 | 028 („welche Gleichung entsteht über Kreuz“) = T 102 | Gestrichen. Den Fehler-Detektiv „x² fällt weg“ aus dem Vorschlag habe ich nicht übernommen, weil das Lösen solcher Gleichungen in T 99, T 107, T 144 steht. Stattdessen fragt 030 nach einer allgemeinen Aussage („immer genau eine Lösung?“) mit dem Gegenbeispiel 4 = 6. |
| A5 | 034 (Nenner x² − 1, Scheinlösung 1) = T 198, K8-V079 | Gestrichen. Den Vorschlag „c so wählen, dass 3/(x − 1) = c/(x² − 1) keine Lösung hat“ habe ich nicht übernommen, weil er den gesperrten Kern „Nenner x² − 1, Scheinlösung 1“ trifft. Neu ist 033: rückwärts c so wählen, dass 2 bzw. 0 Scheinlösung von 3/(x − 2) + 1/x = c/(x² − 2x) wird (Hauptnenner durch Ausklammern). |
| A6 | 038 = T 251, Test 037 und Korrektur 038 stellen dieselbe Frage | Beide gestrichen, und 037 ist zusätzlich V 36 (`groessen.verhaeltnisse`). Neuer Test 037 mischt zwei Mischungen (1 : 1 und 1 : 4 ergeben 1 : 2). Den Vorschlag „Zeiten 3 : 4, Geschwindigkeiten?“ habe ich übernommen, allerdings als Begründungsaufgabe 040 mit dem Ablenker „ohne Strecke geht es nicht“. |
| A7 | Schema definitionsmenge: 023, 025 (+ 022) | Alle drei sind gestrichen. Neu sind 022 (Umformung ändert D), 024 (Sachaufgabe mit Rechteck, Gleichung selbst aufstellen), 025 (Lösungsmenge und Definitionsmenge, immer – manchmal – nie) und 026 (Grundmenge ℤ, rückwärts). Keine davon ist sicher Schema; Grenzfälle siehe Tabelle. |
| A8 | Schema ueber_kreuz: 028, 029, 031; Sammel-Option nur richtig | Alle drei sind gestrichen. Schema ist jetzt nur noch 031 (Verfahren wählen). Die neue Zwei-Wege-Aufgabe 029 (über Kreuz gegen Kehrwert) hat „Beide …“ in der richtigen und in einer falschen Möglichkeit. Ihr Ergebnis x = 11 steht nirgends zur Auswahl, gefragt ist, ob die Wege erlaubt sind. |
| A9 | Schema scheinloesung (033, 034, 036, 035) und verhaeltnis (038, 039, 041, 040) | scheinloesung: alle gestrichen, Schema nur noch 034 (Zahlenrätsel). verhaeltnis: 038, 039 und 041 gestrichen, 040 bleibt (jetzt 041) als die eine Schema-Aufgabe des Lernziels. |

## Befunde B (Soll)

| Nr. | Befund (kurz) | geschlossen wie |
|---|---|---|
| B1 | drei Tests „ganze Zahlen im Intervall zählen“, zwei Tests mit Ausnahmewerten eines Parameters | Kein Test zählt mehr in einem Intervall. Nur noch ein Test hat einen Parameter (027). Die Tests haben vier Denkfiguren und drei Antwortformen: Lücken (022: Umformung und D), Lücken (027: Fallunterscheidung über Kreuz), Auswahl (032: Schritt, an dem die Scheinlösung entsteht), Zahl (037: Mischung). |
| B2 | Test ueber_kreuz trifft vor allem scheinloesung; Grundmenge fehlt | 027 ist neu, die Grundmenge ℚ steht im Text. Der Hauptfall a = 7 gehört zum Kern von Über-Kreuz: Gleiche Zähler bei verschiedenen Nennern ergeben 0 · x = 49. Der Fall a = 0 (Kandidat verboten) bleibt als Vertiefung, siehe „Offene Zweifel“. |
| B3 | 030 Ja/Nein-Lücke, Inhalt T 130, quadratische Fortsetzung | 030 gestrichen. Keine Ja/Nein-Lücke mehr in der Einheit. Alle Umformungen bleiben linear, x² fällt nur weg. |
| B4 | 036 Fehlbilder Lücke 2 unpassend | 036 gestrichen. In der neuen 036 (Differenz der Graphen) passt jedes Fehlbild zur Frage: Vorzeichen g − f, nur −2 genommen, Kandidat als Schnittpunkt gezählt. |
| B5 | 035 zwei Möglichkeiten mit derselben Folgerung | 035 gestrichen. In allen neuen Auswahl-Aufgaben haben die vier Möglichkeiten verschiedene Folgerungen. |
| B6 | 039 Ben-oder-Ida, Bauart | 039 gestrichen (außerdem V 147 im Bestand). |
| B7 | 026 richtige Möglichkeit = Schnittmenge | 026 gestrichen. Die Sachaufgabe 024 ist jetzt eine Lückenaufgabe: Gleichung selbst aufstellen, Ausschluss, Grenze, Lösung. |
| B8 | Etiketten `umkehr`/`darstellung` verdecken Schema | Alle Etiketten neu gesetzt. Rückwärts heißt `umkehr` (023, 026, 028, 033). `darstellung` steht nur bei echtem Darstellungswechsel (036 Graph, 039 Anteil und Verhältnis, 041 Teile). Sachtext oder Rätsel heißt `einkleidung` mit Form `bruecke` (024, 034, 038). Die Schema-Aufgaben sind in der Tabelle unten offen ausgewiesen. |
| B9 | 023 x² = 1 mit zwei Lösungen (M9) | 023 gestrichen. Keine Aufgabe setzt mehr eine quadratische Gleichung mit zwei Lösungen voraus. x² kommt nur vor, wo es wegfällt (030) oder ausgeklammert wird (026, 032, 033). |
| B10 | Denkfiguren scheinloesung/verhaeltnis zu wenig; 037 Bestandskern | Neu gezählt in den Tabellen unten: scheinloesung 5, verhaeltnis 5 (039 und 041 sind verwandt: Teil und Ganzes). 037 ist gegen `groessen.verhaeltnisse` geprüft (V 36 = Treffer) und ersetzt. |

## Befunde C (Kann)

C1 bis C3, C5 bis C8: Die betroffenen Aufgaben sind gestrichen. C4: Die Grundmenge steht jetzt in jeder Parameter- und Mengenaufgabe (022, 025, 026, 027, 030, 032, 033), und Fehlbilder ohne Rechnung gibt es nicht mehr. C9: Die Nenner sind gestreut, aber x − 2 kommt weiterhin in 022, 027, 029, 033 vor, jeweils in anderer Gleichung. C10: unverändert.

## Tabellen je Lernziel (ehrlich)

Schema = durch ein bekanntes Verfahren oder bloßes Ausrechnen lösbar, im Zweifel Schema. „Grenzfall“ heißt: Der gedachte Weg ist kein Verfahren, aber wer stur rechnet, kommt auch hin.

### definitionsmenge

| Kennung | Pool | Bauplan | Denkfigur | Antwortform | Schema | nächstliegender Bestandskern |
|---|---|---|---|---|---|---|
| 022 | test | e/b | Umformungen verändern D: Addieren von 1/x vernichtet die Lösung 0, Malnehmen erlaubt wieder die 2 | Lücken | Grenzfall (man kann (L) und (T) aufstellen und mit D, Lösen, Prüfen durchrechnen) | T 183; `terme.bruchterme` „dieselbe Definitionsmenge?“ |
| 023 | korrektur | c | Nullstelle eines Nenners mit Faktor vor x, rückwärts | Zahl | nein | T 33, K8-V074 |
| 024 | korrektur | d | algebraisch ausgeschlossen (0; 3) gegen sachlich sinnvoll (x > 3), Gleichung selbst aufstellen | Lücken | nein | T 45, T 9, T 42 |
| 025 | sicherung | f | Gleiche Lösungsmenge erzwingt keine gleiche D | Auswahl | nein | T 38 |
| 026 | sicherung | c | D = Grundmenge ℤ ohne die ganzzahligen Nennernullstellen; b rückwärts | Lücken | Grenzfall (Nenner null setzen und mit ℤ abgleichen ist ein Verfahren) | T 7, T 46, T 47 |

### ueber_kreuz

| Kennung | Pool | Bauplan | Denkfigur | Antwortform | Schema | nächstliegender Bestandskern |
|---|---|---|---|---|---|---|
| 027 | test | c (Parameter, maßvoll) | Fallunterscheidung über Kreuz: gleiche Zähler ⇒ 0 · x = Zahl; Zähler 0 ⇒ verbotener Kandidat | Lücken | nein | T 225, K8-V081 |
| 028 | korrektur | c/e | Über Kreuz zählt nur das Verhältnis der Zähler | Zahl | Grenzfall (erst x = −9,5 ausrechnen, dann a wie in T 131) | T 81, T 131, T 134 |
| 029 | korrektur | g | über Kreuz gegen Kehrwert: beide erlaubt, weil kein Zähler 0 ist | Auswahl | nein | T 104, K8-V071, T 274 |
| 030 | sicherung | f | nach dem Über-Kreuz-Multiplizieren fällt x² weg: eine oder keine Lösung | Auswahl | nein | T 99, T 107, T 144 |
| 031 | sicherung | (Verfahren wählen) | Regel „auf jeder Seite genau ein Bruch“, Summe im Zähler erlaubt | Auswahl | **ja** | T 130 |

### scheinloesung

| Kennung | Pool | Bauplan | Denkfigur | Antwortform | Schema | nächstliegender Bestandskern |
|---|---|---|---|---|---|---|
| 032 | test | g | Beim Kürzen mit x geht die Einschränkung x ≠ 0 verloren, 0 wird Scheinlösung | Auswahl | nein | T 224 |
| 033 | korrektur | c | Scheinlösung gezielt bauen: c so wählen, dass der Kandidat 2 bzw. 0 ist | Lücken | nein | T 180, T 225, K8-V081 |
| 034 | korrektur | d | Zahlenrätsel ohne Lösung, weil der einzige Kandidat verboten ist | Zahl | **ja** | T 229, K8-V079 |
| 035 | sicherung | f | Regel aus Beispielen prüfen: „kann vorkommen“ ist gedeckt, „nie“, „immer“, „nur negativ“ sind widerlegt | Auswahl | nein | T 192, T 199 |
| 036 | sicherung | d (Graph) | beide Seiten als Graphen: Differenz konstant −1, kein Schnittpunkt, Kandidat 3 = gemeinsame Lücke | Lücken | Grenzfall (Bruchterme subtrahieren) | R8-V053, T 233 (als Zwischenschritt) |

### verhaeltnis

| Kennung | Pool | Bauplan | Denkfigur | Antwortform | Schema | nächstliegender Bestandskern |
|---|---|---|---|---|---|---|
| 037 | test | h/d | Mischung zweier Mischungen: mit Mengen rechnen, nicht mit Verhältniszahlen | Zahl | nein | T 279, V 73 |
| 038 | korrektur | h | dieselbe Angabe 2 : 3, einmal additiv (Alter), einmal multiplikativ (Rezept) | Lücken | nein | V 45, V 58, T 243 |
| 039 | korrektur | d/b | Saftanteil halbieren ist nicht „Wasser verdoppeln“ | Lücken | nein | V 16 |
| 040 | sicherung | a/h | gleiche Strecke: Geschwindigkeiten im umgekehrten Verhältnis der Zeiten | Auswahl | nein | `groessen.indirekt` |
| 041 | sicherung | (Brücke) | Ganzes : Teil aus Teil : Teil | Zahl | **ja** | V 16, V 34 |

## Prüfläufe

- `python3 -I inhalte/mathe-profi/vtest-1b/bauen.py` → `OK` (156 Lösungen zweifach gerechnet, 401 Fehlbilder, Doppelungsprüfung 0 Treffer, `tools/vorrat_pruefen.py` 0 Meldungen).
- `python3 -I tools/vtest_pruefen.py --runde 1b` → nur die erwarteten vier Pool-Meldungen „2 sicherung-Aufgaben, Soll 3“ der Einheit 20. Eine frühere Fassung von 027 wurde als zu ähnlich zu T 144 bzw. T 101 erkannt (dieselben Zahlen); die Zahlen sind geändert.
- `python3 -I inhalte/mathe-profi/vtest-1b/gegenrechnung.py` → 0 Abweichungen. 49 Aufgaben werden ganz neu gerechnet, davon 12 aus dem neuen Block dieser Einheit.

## Offene Zweifel

- 027 (Test ueber_kreuz): Der Fall a = 0 ist eine Scheinlösung und berührt damit das Lernziel scheinloesung. Der Fall a = 7 ist reiner Über-Kreuz-Kern. Beide Fälle gehören zur Antwort.
- 022, 026, 028, 036 sind Grenzfälle der Schema-Zählung (siehe Tabellen). Zählt ein Prüfer sie als Schema, liegen definitionsmenge bei 2 (022, 026), ueber_kreuz bei 2 (028, 031) und scheinloesung bei 2 (034, 036).
- 036 enthält als Zwischenschritt den Bruch (x − 3)/(x − 3). Gefragt ist aber nicht die Gleichung (x − a)/(x − a) = 1, sondern die Differenz der Graphen und die Zahl der gemeinsamen Punkte.
- 040 liegt nah an der indirekten Proportionalität (`groessen.indirekt`). Gefragt ist kein fehlender Wert, sondern das Verhältnis mit Begründung.
- 037 hat dieselbe Struktur „Ausgangsverhältnis, Zugabe, neues Verhältnis“ wie T 279 und V 73. Zugegeben wird hier aber eine zweite Mischung, kein reiner Bestandteil. Den gesperrten Kern „a : b, n dazu, dann c : d“ trifft die Aufgabe nicht, weil die beiden Bestandteile verschieden stark wachsen.
- Drei Aufgaben haben die Bauform „immer – manchmal – nie“ (025, 030, 035), je eine in einem Lernziel. Damit die richtige Möglichkeit nicht an „können“ zu erkennen ist, steht „können“ jeweils auch in einem Ablenker.
