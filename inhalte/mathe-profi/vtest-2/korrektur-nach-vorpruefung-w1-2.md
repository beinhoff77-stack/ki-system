# Korrektur nach der zweiten Vorprüfung Welle 1 (Runde 2)

Stand 29.11.2026, Zweig `schreiber-w1-r2` (mit `vorpruefer-w1-r2-2`, `766e2d7d`, zusammengeführt). Grundlage: `vorpruefung-w1-2.md` (8 A, 12 B, 6 C). Geändert wurde nur, was ein Befund verlangt. Die Schema-Zählung des Prüfers gilt als maßgeblich. Kennungen bleiben; ersetzte Aufgaben stehen mit dem Vermerk „Stand 9a986063“ in `vorrat-folgerunde/`, außer 040 und 118 (Bestandskern).

## Befunde → geschlossen wie

| Befund | geschlossen wie |
|---|---|
| A1 strahl_eintragen: Test 095 Schema, 097 Schema und gleiche Frage, 098 Zweifel | 095 neu (Vorschlag des Prüfers): dieselben zwei Zahlen auf zwei Strahlen, 6 cm gegen 4 cm, auf A 1 cm = 50 → 1 cm auf B = 75. Die Zahlen sind unbekannt, nur „gleicher Unterschied“ trägt; keine Bereichszählung (B9). 097 neu: Lena zählt Striche statt Abstände – Folge für alle Zahlen (immer 10 zu weit links). 098 geschärft: 0 bis 12 000 mit 60 und 80 Abschnitten; Auflisten ist zu lang, man muss den festen Abstand 600 der gemeinsamen Striche sehen (19). |
| A2 runden_sinnvoll: 108 Schema | 108 neu (Vorschlag): Lea rundet beide Faktoren auf, Tom einen auf und einen ab – Lea sicher zu groß, bei Tom ohne Zahlen nicht entscheidbar. 106 ist jetzt die eine Schema-Aufgabe. |
| A3 roemisch_schreiben: 113 Anleitung im Text | 113 nennt nur noch die Regeln (Zeichen, Reihenfolge, Abziehen, höchstens dreimal bzw. einmal, kein Zeichen über M), keine Bauanleitung. 111 bleibt die eine Schema-Aufgabe. |
| A4 118 = Kern #437 | 118 neu: Lampe für 4 kaputt – wie viele der Zahlen 0 bis 31 bleiben anzeigbar (16, jede Stelle braucht genau die Hälfte). |
| A5 031 durch Einsetzen der genannten Werte lösbar | 031 neu (Vorschlag): ein weiteres Glied a · x², a · x oder a zu 3x² + 5x − 2 – mindestens 2, höchstens 3 Glieder. Keine Testwerte im Text. |
| A6 038 einmaliges Auflösen entscheidet | 038 neu: a ≠ b aus 1 … 5, wie viele Werte hat 20 − (a − b) und welcher ist der größte (8, 24). Das Auflösen ist nur der erste Schritt; entscheidend ist, dass nur b − a zählt. |
| A7 042 Vereinfachen und Vergleichen | 042 neu (Vorschlag): a · x + 9 und 2x + b, Fallunterscheidung keine / genau eine / jede Übereinstimmung, vier Möglichkeiten mit je eigenem Urteil. |
| A8 040 = Kern #237 | 040 neu (Vorschlag): aus dem Term 4 + 3 · (n − 1) die Zählweise erschließen; alle vier Zählweisen zählen richtig, nur eine passt zum Aufbau. |
| B1 Test 110 zu lang | neu: kurzer Text, Beispiele statt zweier Regelwerke; rückwärts: Bei welchen zwei Zahlen von 10 bis 99 spart die Subtraktionsregel genau 5 Zeichen? (49, 94). Keine Maximum-Suche mehr (B9). |
| B2 Test 115 zu lang | ersetzt (zugleich B8, B9): Lisa schreibt eine fünfstellige Zweierzahl und ihre „Gegenzahl“ (0 ↔ 1); Unterschied 7 → Werte 19 und 12. Einsicht: Beide ergeben zusammen immer 31. Kurze Rechnung, kein Aufzählen. |
| B3 Test 100: Ergebnis 0 | „(Auch 0 kann als Ergebnis des Rundens herauskommen.)“ im Text. |
| B4 „nicht entscheidbar“ nie richtig | jetzt richtig in 108 (Tom) und 117 („Nichts Sicheres“, Zahl der Einsen sagt nichts über die Größe), beide inhaltlich echt. Fest geprüft in `bauen.py`: Ab 4 solchen Möglichkeiten müssen mindestens 2 Aufgaben und 20 % davon richtig sein (Stand 9 Vorkommen, 2 richtig). |
| B5 Sammel-Möglichkeit nur in der richtigen (103, 116) | 103: ein Ablenker ist ebenfalls Sammel-Aussage („Alle drei Fälle kommen vor, aber nur bei Zahlen über 100 000 …“). 116: Die richtige Möglichkeit ist keine Sammel-Aussage mehr („0111 und 111 haben denselben Wert …“). |
| B6 104 Länge | richtige Möglichkeit gekürzt, ein Ablenker ebenfalls zweiteilig („kann größer sein und ist nie gleich“). |
| B7 109 vertretbarer Rat | Ablenker ersetzt: „Mia hat sich beim Addieren verrechnet, denn … ergeben zusammen genau 14 000 und nicht 12 000.“ (falsches Urteil) |
| B8 086/117 und 093/115 | 117 neu (Zahl der Einsen und Größe), 115 neu (Gegenzahl). 086 und 093 bleiben. |
| B9 Tests in derselben Form | Bereichs-Zählung/Maximum nur noch in 090 und 100 (Einordnung des Prüfers). 095, 110 und 115 sind Umkehr- bzw. Rückwärtsaufgaben. Offen: 085 („größte Zahl“) und 105 („mindestens/höchstens“) hat der Prüfer nicht zu dieser Form gezählt. |
| B10 Schlussform 029/034/042 | 042 hat jetzt eine Fallunterscheidung (vier Fälle), nicht mehr „x-Teil gleich, es kommt auf die Zahl an“. 029 und 034 bleiben (vom Prüfer als verschiedene Einsichten bestätigt). |
| B11 Bestandsnähe | unverändert zulässig; 031, 038 sind ersetzt. Neue Nähe: 117 ↔ #442, in `bestandsvergleich.md` begründet. |
| B12 112 passt zu roemisch_system | 112 neu: Ben behauptet „plus 1 macht die römische Schreibweise nie kürzer“ (Gegenbeispiel XVIII → XIX). Die alte 112 liegt im Vorrat für die Etappe roemisch_system. |
| C3 042 | entfällt (neu). C5 117 | entfällt (neu). C1, C2, C4, C6 | unverändert. |

## Neue oder geänderte Kennungen

- Neu (ersetzt): 031, 038, 040, 042, 095, 097, 108, 110, 112, 115, 117, 118.
- Geändert, die Aufgabe bleibt: 098 (Zahlen, A1), 100 (Hinweis, B3), 103 (ein Ablenker, B5), 104 (Längen, B6), 109 (ein Ablenker, B7), 113 (Text ohne Anleitung, A3), 116 (Wortlaut der richtigen Möglichkeit, B5).
- Technik: `bauen.py` (Prüfung B4), `gegenrechnung.py` (eigene Rechenwege für alle neuen und geänderten Aufgaben), `ideen.py`, `sonderfaelle.md`, `bestandsvergleich.md`, `vorrat-folgerunde/`.

## Schema je Lernziel (Zählung des Prüfers, nach der Korrektur)

| Lernziel | Schema | Test | Bemerkung |
|---|---|---|---|
| stellenwert | 087 | 085 | unverändert |
| ziffern_zu_zahlwort | 092 | 090 | unverändert |
| strahl_eintragen | – (098 war Zweifel, jetzt geschärft) | 095 neu | falls 098 weiter als Zweifel gilt: eine Schema-Aufgabe |
| runden_regel | 102 | 100 | B3, B5, B6 umgesetzt |
| runden_sinnvoll | 106 | 105 | 108 ersetzt |
| roemisch_schreiben | 111 | 110 neu | 113 ohne Anleitung |
| dualsystem | 116 | 115 neu | 117, 118 ersetzt |
| zusammenfassen | 030 | 029 | 031 ersetzt |
| minusklammer | 035 | 034 | 038 ersetzt |
| aequivalenz | 043 | 039 | 040, 042 ersetzt |

## Offene Zweifel

- 095 (Test): kurz und mit Einsicht, aber zwei Rechenschritte (6 · 50, dann : 4). Ein strenger Prüfer könnte den Test für nicht schwerer halten als 096 (Strichzahlen bei verschobenem Anfang).
- 097: Wer ein oder zwei Beispiele ausrechnet, sieht das Muster; ich zähle es als Verstehen (allgemeine Folge einer Regel), ein strenger Prüfer könnte es Zweifel nennen.
- 038: Wer alle 20 Paare ausrechnet, kommt ohne Einsicht zur Antwort; zu aufwendig für bloßes Ausrechnen, aber angreifbar.
- 042: nahe an der Denkfigur des Tests 039 (Terme a · x + b), aber andere Frage (Fallunterscheidung statt Beweisidee).
- 117 ↔ #442 (gleiche Einsicht, Urteil statt Umrechnen).
- 112: Der Lösungsweg des Tests 110 zeigt, dass IX kürzer ist als VIIII; das stützt das Gegenbeispiel in 112, verrät aber nicht dessen Urteil.
- 115 (Test): Summe-und-Unterschied-Schluss ist für Klasse 5 anspruchsvoll, aber kurz; für gute Kinder in 2–3 Minuten machbar, wenn sie „zusammen immer 31“ sehen.
