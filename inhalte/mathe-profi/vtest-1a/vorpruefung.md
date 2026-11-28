# Vorprüfung Runde VT1A (unabhängig, alle 77 Aufgaben VT1A-001 bis VT1A-077)

Stand 28.11.2026. Prüfer: unabhängig vom Autor, keine Aufgabe geändert. Eigene Rechnung: `vorpruefung_rechnen.py` (liegt neben dieser Datei; Aufruf `python3 -I inhalte/mathe-profi/vtest-1a/vorpruefung_rechnen.py` im Wurzelordner). Alle 77 Aufgaben mit Text, Optionen, Fehlbildern und Lösungsweg von Hand gelesen.

Kennzeichnung: **[F]** = Tatsache (nachgerechnet, im Repo gelesen, von Werkzeug ausgegeben) · **[A]** = Annahme oder Einschätzung.

## Gesamturteil: bereit für die Gegenprüfung **nach Korrektur**

[F] Keine Sollantwort ist rechnerisch falsch. Alle 77 Sollantworten stimmen mit meiner eigenen Rechnung überein (38 Zahl-Aufgaben mit eigener Formel oder Zählschleife; 39 Auswahl-Aufgaben: bei 36 Optionen einzeln ausgerechnet bzw. alle Klammer-Stellungen aufgezählt, bei 061, 064, 069 von Hand entschieden). Das Skript meldet 0 Abweichungen.

[A] Trotzdem nicht ohne Korrektur einspielbar: ein Befund A (Mehrdeutigkeit), 29 Aufgaben mit Befund B, davon ein großer Block „im Kern Rechnen“ und mehrere Doppelungen mit dem Bestand, die das Werkzeug nicht erkennt. Der Auftrag „Verstehen, schwerer als bisherige Tests“ ist bei etwa 12 Aufgaben nicht erfüllt (Abschnitt „Verstehen wirklich geprüft?“).

| Zahl | Wert |
|---|---|
| geprüfte Aufgaben | 77 |
| Sollantwort nach eigener Rechnung richtig und eindeutig | 76 (VT1A-040 nur unter einer Zusatzannahme eindeutig) |
| Aufgaben mit Befund A (muss korrigiert werden) | 1 (VT1A-040) |
| Aufgaben mit Befund B (sollte korrigiert werden) | 29 (001, 002, 003, 004, 006, 007, 016, 017, 018, 020, 026, 030, 031, 034, 037, 039, 041, 042, 044, 045, 046, 047, 048, 053, 055, 066, 067, 068, 069) |
| Aufgaben mit Befund C (Hinweis) | 25 (005, 008, 009, 011, 012, 013, 024, 029, 032, 036, 043, 049, 050, 054, 059, 060, 061, 062, 063, 065, 070, 071, 073, 074, 075) |
| Aufgaben ganz ohne Befund | 22 (010, 014, 015, 019, 021, 022, 023, 025, 027, 028, 033, 035, 038, 051, 052, 056, 057, 058, 064, 072, 076, 077) |

(Zählung nach dem jeweils schwersten Befund je Aufgabe.)

## Werkzeuge, selbst ausgeführt

| Werkzeug | Ergebnis |
|---|---|
| `python3 -I tools/vtest_pruefen.py --runde 1a` | [F] 77 Aufgaben, 2 Einheiten, „OK – keine Fehler“, 3 Hinweise: Abweichung vom Vorschlag in beiden Einheiten, Rhythmus RVVVRVRRRVVRRV bei `zahlen.rechengesetze` |
| `python3 -I inhalte/mathe-profi/vtest-1a/bauen.py` | [F] läuft durch, Ausgabe wie in der README (77 Aufgaben, 230 Fehlbilder/falsche Optionen geprüft, Hinweise zu gleicher Sollantwort in `schreibweise`, `zehner`, `termaufbau`); `git status` danach ohne Änderung (die Datei-Erzeugung ist stabil) |
| `python3 -I inhalte/mathe-profi/vtest-1a/gegenrechnung.py` | [F] „77 Sollantworten neu gerechnet, 0 Abweichungen“ |
| mein `vorpruefung_rechnen.py` | [F] 0 Abweichungen; Eindeutigkeit der Suchaufgaben per Schleife bestätigt (002 → 3, 012 → 14, 037 → 6, 057 → 4, 071 → 38, 075 → 58, 076 → 25); Optionen: 38 Aufgaben mit 4, eine (029) mit 5 Optionen, richtige Option verteilt (0: 9, 1: 10, 2: 9, 3: 11), keine doppelte Option; alle Rechenbehauptungen in Texten, Optionen, Lösungswegen und Fehlbildern gegen die eigene Rechnung gehalten – jede Abweichung ist ein gewollter Fehler (Ablenker) |

[F] Grenze der Werkzeuge: Der Doppelungs-Vergleich in `bauen.py` und in `vtest_pruefen.py` sieht nur den Fragetext und rechnet mit Wort-/Zahlenähnlichkeit; Optionen, Zahlengleichheit unter drei Zahlen und Ideengleichheit erkennt er nicht (siehe Abschnitt „Abgrenzung zum Bestand“).

## Befundtabelle

Schweregrad: A = fachlich falsch/mehrdeutig, muss korrigiert werden; B = sollte korrigiert werden; C = Hinweis.

| Kennung | Grad | Befund | Korrekturvorschlag |
|---|---|---|---|
| VT1A-040 | A | Mehrdeutig. „Erste Stunde 4 €, jede weitere Stunde 2 €“, gefragt „Wie viele ganze Stunden hat es geparkt?“ Bei Parkgebühr zählt in der Praxis jede angefangene Stunde. Dann sind 14 € eine Parkdauer von mehr als 5 bis höchstens 6 Stunden, und „ganze Stunden“ wären 5 – das ist genau das Fehlbild „5“. Soll 6 gilt nur unter der Annahme, dass genau ganze Stunden bezahlt werden; sie steht nicht im Text. Ein aufmerksames Kind kann richtig denken und falsch gewertet werden. | Text ändern: „Es wird nur für volle Stunden bezahlt: 4 € für die erste, 2 € für jede weitere. Auf der Rechnung stehen 14 €. Für wie viele Stunden wurde bezahlt?“ Fehlbild 5 bleibt (nur weitere Stunden gezählt). |
| VT1A-001 | B | Test-Aufgabe (Stufe 3) ist die Standard-Fehlvorstellung 2⁵ = 10. Der Bestand hat eine gleichartige Fehlerdiagnose schon als Übung der Stufe 3 („5 + 5 + 5 = 5³, was ist falsch?“); als Ersatz für eine Test-Aufgabe zu leicht, wenig über Schulaufgabe hinaus. | Anspruchsvoller: zwei Fehlvorstellungen in einer Rechnung (z. B. „3² + 2³ = 5⁵“, welche Aussage ist richtig begründet) oder Vergleich zweier Potenzen mit Begründung. |
| VT1A-002, VT1A-004 | B | Bestand-Niveau, kein neues Verstehen: Die Übungen haben schon „Eine Potenz hat den Exponenten 3 und den Wert 1 000. Wie heißt die Basis?“ (≈ 002) und „5 hoch wie viel ergibt 125?“ (≈ 004); der alte Test war „4 hoch wie viel ergibt 256?“. Die Abgrenzung („Übungen lassen Potenzen schreiben und lesen“) trifft hier nicht. Beide Korrektur-Aufgaben haben außerdem die Sollantwort 3 und stehen im selben Pool: wer 002 falsch hatte und 3 gesehen hat, kann bei 004 „3“ raten. | 004 ersetzen (z. B. Wert 128 mit Basis 2, gesucht Exponent 7, oder eine Begründungs-Aufgabe); 002 anders einkleiden (Würfel/Reihen) oder Basis mit Sollantwort ≠ 3. |
| VT1A-003 | B | Fehlbild 64 (4³) ist mit „Basis und Hochzahl vertauscht“ falsch erklärt: Vertauschen von 2⁴ ergäbe 4² = 16, und das ist sogar die richtige Zahl. 4³ entsteht aus „4. Generation“ als Basis und „3 Spalten“ als Hochzahl. Zusätzlich liegt die Tabelle als `grafik` (Bild im Sinn der App) vor, der Text sagt die Verdopplungs-Regel aber selbst; die Tabelle trägt nichts. | Beschreibung: „Die Nummer der Generation (4) als Basis und die Zahl der Tabellenspalten (3) als Hochzahl genommen: 4³“ oder das Fehlbild ersetzen. Tabelle weglassen oder ganz in den Text. |
| VT1A-006 | B | Im Kern Rechnen: das Kind rechnet alle acht Potenzen aus (9 gegen 8, 25 gegen 32, 64 gegen 81, 16 gleich 16). Der Bestand hat dieselbe Idee in `vertauschen` („Bei welchem Paar sind beide Potenzen gleich groß? 3⁴ und 4³, 2⁴ und 4², 2⁵ und 5²“, Sicherung, gleiche Lösung 2⁴ = 4²). Der Vorspann „Trotzdem stimmt eine“ verrät, dass es genau eine gibt. | Als echte Einsicht: „Warum sind 2⁴ und 4² gleich, obwohl man nicht vertauschen darf?“ (Begründung wählen, 4 Optionen) oder Zahlen ändern (z. B. 2⁶ und 8²) und Vorspann streichen. |
| VT1A-007 | B | Dieselbe Aufgabe wie 001 mit anderen Zahlen (Tom 3⁴ = 12, vier Optionen „Fehler: … Richtig wäre …“). Bei Nachtest nach dem Test fällt das als Wiederholung auf; „verschieden bauen“ ist nicht erfüllt. | Andere Form: Potenz in einer Rechnung mit weiterem Schritt (z. B. 2 · 3² = 36 oder 6 ≠ 2³) oder Fehler in einer Rechnung mit drei Zeilen. |
| VT1A-016 | B | Bestand-Nähe: rollend-5/zehner hat „Welche Schreibweise ist gleich der Zahl 3 400 000?“ mit 34 · 10⁶ / 34 · 10⁵ / 34 · 10⁴ / 3 400 · 10⁵; 016 ist dieselbe Zahl und dieselben Schreibweisen, nur verneint. Der automatische Vergleich prüft nur den Fragetext, nicht die Optionen. Verneint gestellt (zulässig und eindeutig, aber ein Kind mit Lesefehler verliert hier). | Andere Zahl und andere Schreibweisen (z. B. 56 000 000). Die Verneinung selbst ist zulässig und eindeutig. |
| VT1A-017 | B | Fehlbild 3 „Nur die Nullen von 500 gezählt und 1 000 vergessen (2 + 1)“: Wer die 1 000 vergisst, rechnet 500 : 5 = 100, also n = 2, nicht 3. Das „+ 1“ ist nicht erklärt. Erklärtext führt nicht zur gespeicherten Zahl. | Fehlbild 3 ersetzen durch n = 2 mit Rechnung 500 : 5 = 100 = 10² und Text „die Umrechnung in Gramm (mal 1 000) vergessen“; dann führt der Text genau zur Zahl. |
| VT1A-018 | B | Kein Verstehen: „Mal 10⁴ ergibt 370 000, welche Zahl?“ = vier Nullen streichen. Stufe 2, im Kopf in Sekunden; Bestand hat Stufe-3-Übungen derselben Art („mal 10³, dann durch 10, 52 000“). | Ersetzen durch eine Begründungs-/Darstellungs-Aufgabe (z. B. warum 10⁴ · 10² nicht 10⁸ ist) oder Zweischritt-Umkehrung mit 10ⁿ. |
| VT1A-020 | B | Fast gleich einer Übung derselben Etappe: rollend-12/potenzen_basis „Licht legt in einer Sekunde etwa 3 · 10⁵ Kilometer zurück. Wie viele Kilometer in 10 Sekunden?“ – 020 ändert nur 10 s → 60 s. Außerdem Rechnen nach Schema (3 · 60 = 180, fünf Nullen), kein Verstehen; Stufe 3 überhöht. Das Werkzeug erkennt es nicht (Wortähnlichkeit unter der Schwelle). | Ersetzen (anderer Sachverhalt) und Stufe/Typ ehrlich als Stufe 2 führen oder eine Aufgabe, bei der die Zehnerpotenz gedeutet werden muss. |
| VT1A-026 | B | Nahezu dieselbe Aufgabe wie rollend-5/schreibweise „Die Zahl 3 kommt sechsmal als Faktor vor. Welche Schreibweise gehört dazu? 6³ / 3 · 6 / 3 + 6 / 3⁶“ (gleiche vier Ausdrücke, 3⁵ statt 3 + 6); dazu im Bestand die Folge 3, 9, 27, 81, … (6. Stelle = 729). Die Regel „verdreifacht sich“ steht nicht im Text; aus drei Tabellenwerten folgt sie streng genommen nicht (nur die Optionen machen sie eindeutig). Tabelle als `grafik` – ohne sie ist die Aufgabe nicht lösbar (Test „ohne Bild“). | Die Werte in den Text schreiben („Am 1. Tag hat das Netzwerk 3 Mitglieder, am 2. Tag 9, am 3. Tag 27 …“), „und so geht es weiter“ ergänzen, andere Zahlen und andere Ausdrücke (z. B. 4er-Folge). |
| VT1A-030 / 034 / 067 / 068 | B | Rechnen nach Schema. 030: alle vier Terme ausrechnen und den größten nehmen. 034: beide Terme ausrechnen und abziehen. 067: 48 · 52 ausrechnen, zwei Abstände bilden, subtrahieren. 068: Überschlag und genaue Summe ausrechnen, abziehen. Die Form `zwei_wege` ist nur formal (es gibt keinen zweiten Zugang, der etwas anderes einsieht). Im Test zählt das als Verstehen, wäre aber Rechnen. | 030: „Ohne auszurechnen: Warum hat (8 + 4) · 5 − 3 den größten Wert?“ (Begründung wählen). 034: „Welche Klammer ändert den Wert?“ o. ä. 067/068: Aussage über Überschläge begründen („Der Überschlag mit 40 · 50 ist zu grob, weil …“, Optionen) statt ausrechnen. |
| VT1A-031 | B | Passt nicht zum Lernziel `klammern`: Sachaufgabe „Gesamt minus Teil“, die Klammer taucht nur in der Probe auf. Gleiche Schablone wie 037, 040, 045, 059, 072, 076 (Gesamt, minus Teil, durch Anzahl). | Ersetzen durch eine Aufgabe, in der die Klammer das Entscheidende ist (z. B. Term für „Summe der beiden Klassen geteilt durch Zahl der Busse“ ergänzen, oder zwei Klammern vergleichen). |
| VT1A-037 | B | Mehrdeutiger Satz: „6 Tische mit je 8 Gästen und 4 Tische mit gleich vielen Gästen.“ Ein Kind kann „gleich viele wie die 6 Tische“ (also 8) lesen; dann stimmt die Summe 72 nicht, und es steht verwirrt da. Gemeint ist „gleich viele je Tisch untereinander“. Außerdem gleiche Schablone wie 031 (siehe dort). | „… und 4 weitere Tische, an denen jeweils gleich viele Gäste sitzen (aber nicht unbedingt 8)“. |
| VT1A-039 | B | Lösungsweg behauptet „Die Klammer braucht man, weil beide Beträge abgezogen werden.“ Das ist falsch: 20 − 4 · 3 − 2 · 2 = 4 geht ohne Klammer. Der Satz lehrt eine falsche Regel (Klammer nötig). | Lösungsweg: „Die Klammer fasst beide Ausgaben zusammen; ohne Klammer müsste vor den Stiften ein zweites Minus stehen: 20 − 4 · 3 − 2 · 2.“ |
| VT1A-041 | B | Im Kern Stufe 1: „Punkt vor Strich“ ist die Standard-Regel, die Optionen sind nicht geprüft schwer („immer die größeren Zahlen“). Als Sicherung mit Stufe 3 gekennzeichnet; zu leicht für „schwerer als bisherige Tests“. | Echter Zusammenhang: „Warum ergibt 8 + 5 · 3 und (8 + 5) · 3 nicht dasselbe, und wann wäre es gleich?“ oder Term in eine Sachgeschichte ändern lassen. |
| VT1A-042, VT1A-055 | B | 042: mehrschrittige Sachrechnung ohne eigenes Aufstellen (alles ist vorgegeben, nur ausrechnen); 055: „Berechne mit einem Rechenvorteil“ gibt das Verfahren vor (Ausklammern); beide als `transfer`/`anwenden` Stufe 3 geführt. Das ist Rechnen nach Schema. | 042: nach dem Term fragen oder Rechenweg wählen lassen. 055: ohne Verfahrens-Hinweis „Welcher Rechenweg ist am geschicktesten und warum?“ oder Lücke im Term (19 · □ + 19 · 64 − 19 · 50 = 950). |
| VT1A-044, VT1A-066 | B | 044: „Ohne auszurechnen: welcher Term hat denselben Wert wie 37 + 58 + 63?“ – die einzige Option ohne Minus ist richtig (Mustererkennung); im Bestand gibt es dieselbe Form in `differenz_summe`. 066: Standard-Runden auf Zehner, die Ablenker (40 · 5, 30 · 50) sind offensichtlich; Stufe 2 kaum Schulaufgabe. | Ablenker anspruchsvoller (alle mit Plus und Minus, nur einer gleichwertig) bzw. Begründung verlangen; 066 mit Zahlen, bei denen zwei Rundungen plausibel sind (z. B. 48 · 45) und die Begründung zählt. |
| VT1A-045 | B | Zwei Schritte (5 · 20 = 100, 1 500 : 100); „geschickt“ nur im Lösungsweg erwähnt, nicht verlangt; kaum Bezug zum Tauschen/Verbinden. Sollantwort 15 ist auch durch zweimaliges Teilen (1 500 : 20 : 5) gleich leicht. | Aufgabe so stellen, dass Verbinden nötig ist (z. B. 25 · 17 · 4 geschickt mit begründeter Wahl) oder ersetzen. |
| VT1A-046, VT1A-048 | B | Gleiche Zahlen 2, 37, 50 und gleiche Einsicht (Faktoren tauschen, 100 · 37 = 3 700). 046 (Korrektur) sagt in der richtigen Option „Beide bekommen 3 700“, 048 (Sicherung) hat „100 · 37 = 3 700“ als richtige Korrektur. Wer 046 in einer Verbesserung gesehen hat, kann 048 aus dem Gedächtnis lösen („Antwort ablesbar“). | 048 mit anderen Zahlen (z. B. 4 · 18 · 25) und anderem Fehlertyp; 046 behalten. |
| VT1A-047, VT1A-053 | B | Nah am Bestand: 047 ≈ Übung „□ + 64 + 36 = □ + 100 = 147“ (zahlen.rechengesetze/vorteil); 053 ≈ Übung „12 · a + 8 · a = 300“ (verteilen, gleiche Zahlen 12 und 8). Ein Rechenschritt, Stufe 2. | Andere Einkleidung und Zahlen; 053 z. B. mit Differenz oder als Flächenaufgabe. |
| VT1A-069 | B | Die als richtig markierte Option nennt als Fehler „12 zu grob auf 10 gerundet“. Aber Mias Rundung (596 → 600, 12 → 10) ist die übliche Rundung auf die erste Stelle; der Fehler ist ihr Schluss („passt nicht, also falsch“), denn 6 000 und 7 152 liegen für einen Überschlag nahe genug. Die Rückmeldung „Fehler: 12 zu grob“ stempelt richtiges Runden als falsch. Im Lösungsweg steht „zwei von zwölf sind 17 %“: Prozent ist Klasse 6. Option 0 („596 auf 500 runden“) ist keine echte Fehlvorstellung. | Option 1: „Der Überschlag ist zu grob, um 7 152 abzulehnen: Mit 600 · 12 = 7 200 liegt er ganz in der Nähe.“ Lösungsweg ohne Prozent („12 auf 10 ist ein großer Sprung“). Option 0 ersetzen („nur 596 aufgerundet, 12 weggelassen“). |
| VT1A-005, VT1A-011 | C | Sehr nah beieinander (Was bedeutet 4⁶ / welche Aussage stimmt für 8²: Basis mal Hochzahl, Plus statt Mal). 011 ist mit 8² = 64 sehr leicht (Stufe 2, Standardwissen). | Eine der beiden anders gestalten. |
| VT1A-008 | C | Text fast identisch mit dem Bestand `gleichungen.quadratisch` („Ein quadratischer Garten hat 225 m² Fläche. Wie viele Meter Zaun …“, Klasse 9). Andere Einheit und Klasse, daher nur Hinweis; für ein Kind, das später in Klasse 9 kommt, eine Doppelung. | Zahl und Einkleidung ändern (z. B. 144 m², Spielfeld). |
| VT1A-009 | C | Erkennen einer Quadratzahl (121) – Stufe 2, Ablenker 99/48/150 leicht; als `verfahren_waehlen` geführt, ist es eigentlich Wissen (Quadratzahlen bis 400 auswendig). | Ablenker näher an Quadratzahlen (120, 122, 143) und Begründung über Nachbarquadrate. |
| VT1A-012, VT1A-013 | C | Gleiche Idee (Reihe + Spalte weg/dazu, Ecke nicht doppelt) in zwei Sicherungs-Aufgaben desselben Lernziels; der Lösungsweg von 012 („neue Reihe 14, neue Spalte 13 weitere“) hilft bei 013 direkt. 012: „Probiere“ im Lösungsweg – die Zahl 27 = 2n − 1 wird nicht benutzt; Sollantwort eindeutig (nachgerechnet). | Eine ersetzen, z. B. 013 durch Quadrat-Differenz mit Nachbarquadraten oder Rahmen-Aufgabe. |
| VT1A-024 | C | Ähnlich rollend-5/kombinatorik (Nummernschloss mit 3 Rädchen, Zählprinzip). Andere Einheit; nur Hinweis. | Einkleidung wechseln (z. B. Passwort aus Ziffern). |
| VT1A-029 | C | Einzige Auswahl-Aufgabe mit 5 Optionen; die README behauptet „immer 4“. Der Ablenker (20 − 4) · (3 + 2) hat zwei Klammerpaare und fällt schon durch den Text („genau ein Klammerpaar“). | README korrigieren oder Option 5 streichen. |
| VT1A-032 / 059 / 065 | C | Fehlbild-Texte ungenau: 032 Option 2 „Nur 3 geteilt und Summe zuletzt“ (gemeint: 3 durch das Produkt 4 · 2); 059 FB 9 „aufgerundet“ (43 : 5 hat Rest, kein Dezimalbruch, Klasse 5 kennt Rest); 065 FB 29 „Eine zu wenig als gerundete Zahl“ unklar. | Texte umformulieren. |
| VT1A-036 / 043 / 050 | C | Als Test-Aufgaben mit Stufe 3 geführt, aber Stufe 2: 036 (Term → Geschichte, Ablenker 1 klar falsch), 043 (Tauschen der Summanden, Allgemeinwissen), 050 (Anna/Ben, Option 0 ist die Aussage der Aufgabe selbst). | Schwieriger machen oder Stufe 2 eintragen (alle Tests = Stufe 3 gleicht nicht dem Plan „2–3“). |
| VT1A-049 | C | Frage „Welche Aussage über die Werte stimmt?“ – Option 3 („Beide gleich, weil in beiden 25 vorkommt“) hat die richtige Behauptung mit falscher Begründung; deutlicher: „Welche Aussage ist richtig begründet?“ | Frage umformulieren. |
| VT1A-050, VT1A-054 | C | Gleiche Idee (Rechteck in zwei Teile, 9 · 20 + 3 ohne 9 vor der 3 ist falsch). Option 1 von 050 („8 · 30 + 2“) zeigt den Fehler, den 054 abfragt; wer 050 im Test sah, hat 054 im Nachtest schon geklärt. | 054 anders bauen (z. B. Zahlenwert Flächen mit drei Teilen). |
| VT1A-054 | C | Verneinte Frage („NICHT richtig“); eindeutig (nur 9 · 20 + 3), fair, aber Lesefehler-Risiko. | Nur Hinweis. Will die App keine Verneinungen: „Welche Rechnung gibt die Gesamtfläche an?“ mit einer richtigen und drei falschen Optionen. |
| VT1A-060 / 061 / 062 / 063 | C | Variable x (und in 063 ein zweiter Parameter a) statt Kästchen □; die README sagt, Kästchen stünden für gesuchte Zahlen. Nach Lehrplan (M5 3.1: Gleichungen a · x = b, x : a = b, a : x = b) in Klasse 5 erlaubt; nur uneinheitlich. 062 Option 1 „man darf nicht durch 7 teilen“ meint „es geht nicht auf“, ein Kind kann „geht nicht“ ankreuzen wollen. | Einheitlich □ oder x wählen. 062 Option 1 durch einen eindeutig falschen Ablenker ersetzen (z. B. „Weil 7 eine Primzahl ist.“). |
| VT1A-070 | C | Sollantwort 100 (Hunderter-Runden) ist auch ohne Verstehen erratbar; Ablenker 99/101/50 sind „eine daneben“. Gegenstand Runden, nicht Überschlag; zählt trotzdem (Lehrplan). | Als Doppel-Lücke „kleinste und größte Zahl“ (4 550 und 4 649) fragen; das lässt sich nicht erraten. |
| VT1A-071, VT1A-075 | C | Gleiche Idee: „Hälfte der übrigen“ rückwärts (Test 071, Sicherung 075), beide mit +/− Zwischenschritt. Nicht dieselbe Rechnung, aber im Nachtest kurz nach dem Test sehr ähnlich. | Eine mit anderem Schritt (z. B. Drittel) oder ohne Halbieren. |
| VT1A-073 | C | Rückmeldung zu Option 3 „Lösung wäre 10,5“: Dezimalzahl in der Fehlerbeschreibung für Klasse 5. | Text: „Lösung wäre keine natürliche Zahl“. |
| VT1A-074 | C | Fast gleich Bestand `geometrie.grundbegriffe/vierecke` („Rechteck hat den Umfang 18 cm, eine Seite 5 cm, andere?“). Andere Einheit, andere Zahlen; gehört fachlich zu Umfang und nicht zu `sach` der Rechengesetze. | Andere Sachsituation (rückwärts, drei Schritte). |


## Verstehen wirklich geprüft?

**Im Kern Rechnen nach Schema (Befund B, ersetzen oder umbauen):** 018, 020, 030, 034, 042, 044, 045, 055, 066, 067, 068. Zusätzlich schwach (Verstehen nur formal, im Kern ein Rechenschritt oder Mustererkennung): 006, 009, 031, 041, 047, 051, 053, 072, 074.

**Die sieben Grenzfälle des Autors (030, 034, 044, 046, 049, 067, 068):** [A] 030, 034, 044, 067, 068 sind Rechnen (siehe Tabelle). 046 und 049 sind echtes Verstehen: Die Optionen verlangen eine Begründung (Tauschen der Faktoren; 36 · 4 = 18 · 8 als Halbieren und Verdoppeln), und die Ablenker („weil 37 ungerade ist“, „weil 25 in beiden vorkommt“) sind echte Fehlvorstellungen. 046 hat aber das Problem mit 048 (gleiche Zahlen).

**31 von 77 mit Form `umkehren` – echte Vielfalt oder dieselbe Idee?** [A] Nach meiner Zuordnung stecken in den 31 nur wenige Ideen:

| Idee | Aufgaben | Anzahl |
|---|---|---|
| Exponent oder Basis aus dem Wert suchen (Faktoren/Nullen zählen) | 002, 004, 017, 021, 023, 024 | 6 |
| Sachschablone „Gesamt, minus Teil, geteilt durch Anzahl“ | 031, 037, 040, 045, 059, 072, 074, 076 | 8 |
| Platzhalter-Gleichung mit einem Rechenschritt | 047, 051, 053, 058, 060, 063 | 6 |
| Kette rückwärts (Schritte einzeln umkehren) | 057, 071, 075 | 3 |
| Nullen/Zehnerpotenz rückwärts | 018, 019 | 2 |
| Quadrat rückwärts | 008, 012 | 2 |
| Fenster beim Runden zählen | 065, 070 | 2 |
| Wachstum rückwärts; Klammern setzen für vorgegebenes Ergebnis | 022; 029 | 2 |

Das ist 14 Mal dieselbe Rechnung in zwei Schablonen (Exponent suchen; Gesamt/Teil/Anzahl). Für die Lernziele `sach` (Rückwärtsarbeiten, Lehrplan M5 3.2) und `umkehraufgabe_mal` ist Umkehren das Thema und passt; bei `klammern` (031), `termaufbau` (037, 040), `vorteil` (045, 047), `verteilen` (051, 053) ist es fachfremd oder zu leicht (Bestand hat dazu schon Übungen). Das Wort „Vielfalt“ im README stimmt nur nach der Zählung der `typ`-Etiketten (umkehr, rueckwaerts, parameter), nicht nach der Idee.

**Eine Einsicht je Lernziel, verschieden geprüft?** [A] Gut: `quadrat` (Fläche, Umfang, Wachstum der Fläche, Reihe/Spalte, Quadratzahl erkennen, 8²), `vorteil`, `umkehraufgabe_mal` (Gleichung wählen, Geschichte, Lösbarkeit, Zählen der Teiler), `verteilen`. Schwächer: `schreibweise` (001 und 007 gleiche Aufgabe, 002 und 004 gleiche Aufgabe, 003/005 bruecke), `termaufbau` (Term ↔ Geschichte dreimal: 036, 038, 039; 037/040 gleiche Schablone), `ueberschlag` (067 und 068 rechnen nur genau nach), `sach` bei den Rechengesetzen (fünf von sieben sind „Kette rückwärts“).

## Schwierigkeit (Stufe 2–3, 2–4 Minuten, Klasse 5)

- [F] Alle 11 Test-Aufgaben sind als Stufe 3 geführt, alle 33 Korrekturen als Stufe 2, Sicherungen 12 × Stufe 2 und 21 × Stufe 3.
- [A] Stufe 3 überhöht, tatsächlich Stufe 2 oder darunter: Tests 001, 036, 043, 050; Sicherungen 041, 042, 055; 020. Das erfüllt „schwerer als bisherige Tests“ nicht (der Bestand hat Stufe-3-Übungen mit demselben Niveau).
- [A] Trivial: 011 (8² = 64), 018, 041, 044, 052, 058, 066.
- [A] Obere Grenze, noch vertretbar: 027 (Verdopplungsfolge bis 2 048 mit Vergleich, 4 bis 5 Minuten), 063 (Teiler von 36 zählen), 075 (Brötchen rückwärts, zwei Rückwärtsschritte mit Hälfte und 7).
- [A] Nichts ist für Klasse 5 zu schwer (nur natürliche Zahlen, Potenzen höchstens 4⁶ oder 3⁶, Zehnerpotenzen bis 10⁶).

## Lehrplan und Auswahl der Lernziele

**Lehrplan-Angabe.** [F] Die Themenliste führt `zahlen.rechengesetze` und `zahlen.potenzen_basis` unter „M5 3 Natürliche und ganze Zahlen – Multiplikation und Division“. Nach der Seite des LehrplanPLUS Gymnasium Mathematik 5 (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/5/mathematik, von mir abgerufen; die Angaben unten sind die Auswertung der Seite durch das Abrufwerkzeug, nicht der volle Wortlaut) steht Folgendes: M5 3.1 enthält Überschlag, Teilbarkeit und Primfaktoren, Zählprinzip, Potenzen mit natürlichen Exponenten und **ganzzahligen Basen**, Zehnerpotenzen, Quadratzahlen bis 400, Gleichungen a · x = b, x : a = b, a : x = b (Probieren/Umkehraufgabe), Kommutativ- und Assoziativgesetz; M5 3.2 enthält Terme mit Klammern und „Punkt vor Strich“, Distributivgesetz, Überschlag in Anwendungen, Vorwärts- und Rückwärtsarbeiten. „M5 1.3 Grundrechenarten und Rechengesetze“ ist die Nummer der **Realschule** (so zeigt es die Suchausgabe zu lehrplanplus.bayern.de/fachlehrplan/realschule/5/mathematik); die Angabe „M5 1.3“ in `inhalte/pruefung/klassen/vorschlag-rsib.md` ist für das Gymnasium falsch. Damit ist „M5 3“ richtig; genauer wäre „M5 3.1“ für `schreibweise`, `quadrat`, `zehner`, `sach` (Potenzen), `umkehraufgabe_mal`, `ueberschlag` und „M5 3.2“ für `klammern`, `termaufbau`, `vorteil`, `verteilen`, `sach` (Rechengesetze). Das ist optional (das Werkzeug verlangt nur den Anfang „M5 3“).

**Stoff aus späteren Klassen.** [F] In den Aufgaben kommen keine negativen Zahlen, Brüche oder Variablen-Umformungen vor. Ausnahmen mit Klasse-6-Wörtern in Rückmeldungen: 069 (Lösungsweg „17 %“), 073 (Fehlbild „10,5“). Die Variable x in 060 bis 063 ist nach M5 3.1 erlaubt; in 063 kommt zusätzlich der Parameter a vor (Teiler gehört zu M5 3.1).

**Die Begründung der Auswahl ist sachlich falsch.** [F] `auswahl.md` und README sagen, `negativ`, `mal_ganz`, `geteilt_ganz` seien „nicht Klasse 5“ („M5 2, kommt im Lehrplan danach“). Nach dem Lehrplan sind ganze Zahlen mit Multiplikation und Division, und Potenzen mit „ganzzahligen Basen“, Stoff der Jahrgangsstufe 5 (M5 1.1, 1.2, 3.1); die Themenliste selbst nennt den Lernbereich „Natürliche und ganze Zahlen“, und das Repo setzt `zahlen.ganz` (Klasse 5) vor `zahlen.rechengesetze`. Die Lernziele `negativ`, `mal_ganz` und `geteilt_ganz` sind also lehrplankonform; der Vorschlag des Auftraggebers war nicht fehlerhaft.

**Folgen, [A].** Die Auswahl ist als Ergebnis nicht unbrauchbar: `schreibweise`, `quadrat`, `zehner`, `sach` sind gute Verstehens-Ziele, und `termaufbau`, `ueberschlag` sind tragfähig. Aber (1) die Begründung muss korrigiert werden (B), (2) bei `zahlen.rechengesetze` entsteht RVVVRVRRRVVRRV: drei Verstehens-Etappen in Folge (klammern, termaufbau, vorteil) und drei Rechen-Etappen in Folge (kopfrechnen, mal_ganz, geteilt_ganz) – der Plan (E2) will abwechselnd; der Vorschlag RVRVRVRVRVRVRV hätte das erfüllt, (3) `negativ` (Vorzeichen begründen) und `mal_ganz` bleiben Rechnen, obwohl sie der Verstehenskern der Einheit sind, (4) `schriftlich` fehlt (Fehler in schriftlicher Rechnung). Empfehlung: Auswahl nicht neu aufrollen, aber (a) Begründung berichtigen, (b) in einer Folgerunde `negativ` und `mal_ganz` nachholen oder in dieser Runde `termaufbau` gegen `mal_ganz` tauschen (stellt Abwechslung her, kostet 7 neue Aufgaben). Als Verstoß gegen den Auftrag zähle ich es nicht, weil der Auftrag Abweichungen mit Begründung erlaubt; die Begründung trägt aber nicht.

## Regel-Kennungen

[A] Maßstab: Trägt die Regel den Lösungsweg?

| Lernziel | Regel | Urteil |
|---|---|---|
| schreibweise, quadrat, zehner, sach (Potenzen) | `rr.potenz` | trägt (Faktoren zählen). Weniger gut bei 012, 013 (Reihe/Spalte), 008 (Fläche/Umfang), 019 und 020 (Zehnerpotenz mit Nullen) – dort trägt die Idee „Nullen zählen“, nicht „n gleiche Faktoren“. C |
| klammern, termaufbau | `rr.reihenfolge` | trägt bei 029 bis 030, 032 bis 036, 038, 039, 041, 042. Nicht bei 031, 037, 040 (Gegenrechnung) |
| vorteil | `rr.tauschen` | trägt (Merksatz „Tauschen bei Plus und Mal“) |
| verteilen | `rr.ausmultiplizieren` | trägt (vorwärts und rückwärts) |
| umkehraufgabe_mal, sach (Rechengesetze) | `rr.gegenrechnung` | trägt; die Themenliste des Katalogs nennt die Einheit nicht (so in `regeln-zuordnung.md` vermerkt), kein inhaltliches Problem |
| ueberschlag | `id.zahlen.buendeln` | **trägt den Lösungsweg nicht**: Merksatz „Zehn Einer sind ein Zehner, zehn Zehntel sind ein Einer“ betrifft den Stellenwert; Überschlag braucht Runden und eine Prüfschlussfolgerung. Bei 067, 068, 069 gar nicht. Besser eine Regel „Überschlag/Runden“ im Katalog ergänzen (nicht Sache der Aufgaben-Runde), bis dahin als vorläufig kennzeichnen. B |
| quadrat | `rr.potenz` (ohne Lernkarten-Regel) | Vorschlag des Autors ist passend |
| termaufbau | `rr.reihenfolge` (ohne Lernkarten-Regel) | Vorschlag des Autors ist passend |

## Test-Tauglichkeit

- [F] Kein Tipp (`h`), keine `toleranz`, kein `hinweis`, alle Antworttypen `zahl` oder `auswahl`, keine Lücken. Ein-Wert-Antworten haben, wo nötig, eine `einheit` (z. B. „Personen“, „m“).
- [A] Zwei Aufgaben tragen eine Tabelle als `grafik` (003, 026). Die App nennt Tabellen „Bild“ (`bild`/`grafik` in `inhalte/themen`), `lernAufgabe` in `lernen.js` zeigt `f.grafik`; ob der Test-Modus sie ebenfalls zeigt, konnte ich nicht prüfen. 026 ist ohne Tabelle unlösbar → in den Text schreiben (Befund B).
- [A] Eindeutig lesbar im Test: bis auf 040 (A), 037 (B) und 069 (B) kein Satz, den ein Kind zu Recht anders versteht. Verneinte Fragen 016 („gehört NICHT zur Zahl“) und 054 („NICHT richtig“): eindeutig (je genau eine falsche Option, die drei anderen nachgerechnet richtig) und fair gestellt, NICHT ist großgeschrieben; Risiko nur Lesefehler. Keine Änderung nötig, wenn die App Verneinungen zulässt.
- [F] Auswahl: 38 mit 4 Optionen, 029 mit 5. Die richtige Option liegt auf Platz 1 bis 4 gleichmäßig. Kein Doppel.
- [F] Eingabeformat: Zahl-Aufgaben nennen die Einheit ausdrücklich im Antwortfeld; 020 hat die Antwort 18 000 000 (Eingabe mit oder ohne Tausenderpunkt: nicht getestet).
- [A] Antwort aus anderer Aufgabe desselben Lernziels ablesbar: 046 → 048 (siehe Tabelle), 050 → 054 (Option 1 von 050 zeigt den Fehler von 054), 002/004 (gleiche Sollantwort 3), 025 (Korrektur) → 028 (Sicherung, gleiche Einsicht „Startzahl nicht unter die Hochzahl“; gewollt als Sicherung, aber Antwort ablesbar nach Korrektur). In `zehner` kommt n = 5 zweimal vor (017 Korrektur, 021 Sicherung), in `termaufbau` 6 zweimal (037, 040): unterschiedlich gemischte Pools, nur C.
- [F] „Gleiche Sollantwort im Lernziel“ nach `bauen.py`: schreibweise 2 × 3 (002 und 004 – beide Korrektur, siehe B), zehner 2 × 5 (017, 021 – Korrektur und Sicherung, nur C), termaufbau 2 × 6 (037, 040 – Korrektur und Sicherung, nur C). Die Rate-Gefahr besteht nur bei 002/004.

## Abgrenzung zum Bestand (Stichproben je Lernziel)

[F] Methode: Ich habe jede der 77 Aufgaben gegen alle Aufgaben von `inhalte/themen/zahlen.potenzen_basis.json`, `zahlen.rechengesetze.json` und die `rollend-*`-Dateien dieser zwei Einheiten sowie gegen alle `themen`-Dateien und `rollend-*`-Runden verglichen (Wortmenge und Zahlenmenge, eigenes Skript, nur Heuristik). Treffer mit echter Doppelung stehen in der Befundtabelle: 020 (rollend-12, gleiche Etappe), 026 (rollend-5), 016 (rollend-5), 047, 053, 006, 002/004 (Bestand-Übungen), dazu 008 (Klasse 9) und 074. Die Abgrenzungssätze der Autoren sind für alle Aufgaben eines Lernziels derselbe Satz und sagen nichts über die Einzelaufgabe; bei `schreibweise` stimmt er für 002 und 004 nicht („Übungen lassen Potenzen schreiben und lesen“ – der Bestand hat schon „2 hoch wie viel ergibt 256?“).

## Bauarten: Lockerung von 5 auf 4

[F] `bauen.py` (Zeile 111) verlangt jetzt mindestens 4 verschiedene `typ`-Etiketten je Lernziel. [A] Nicht vertretbar als Maß für Vielfalt: Das Etikett zählt `umkehr` und `rueckwaerts` getrennt, obwohl es dieselbe Rechnung ist. Mit gezählten *Ideen* (siehe Verstehen-Abschnitt) haben `schreibweise` nur etwa 3, `termaufbau` 3, `sach` (Rechengesetze) 3, `verteilen` 4 Ideen; mindestens 5 Bauarten in 7 Aufgaben sind erreichbar (der Autor selbst hat bei `quadrat` 7 `(typ, form)` und bei `klammern` 6). Die Lockerung hat gerade die schwächeren Lernziele durchgelassen. Empfehlung: „mindestens 5“ beibehalten und die Doppel-Aufgaben aus der Befundtabelle ersetzen (`schreibweise`: 007 und 004, `termaufbau`: 040, `verteilen`: 054).

## Was ich NICHT prüfen konnte

- [A] Ob der Test-Modus der App Tabellen (`grafik`) anzeigt und Verneinungen/Mehrzeilen-Optionen sauber umbricht (App nicht gestartet).
- [A] Den vollen Wortlaut des Lehrplans (nur die Auswertung der Seite durch das Abrufwerkzeug); die Zuordnung „M5 3.1/3.2“ je Lernziel ist eine Einschätzung auf dieser Grundlage.
- [A] Ob Kinder die Aufgaben tatsächlich in 2–4 Minuten lösen (Einschätzung, keine Erprobung); ob die Wortwahl (Hochzahl/Exponent, Faktor, Überschlag) dem Wortschatz der Zielkinder entspricht.
- [A] Vollständigkeit der Bestands-Doppelungen: meine Ähnlichkeitssuche ist eine Heuristik (Wort- und Zahlenmenge); weitere inhaltliche Doppelungen mit anderem Wortlaut sind möglich.
- [A] Eingabeformat bei großen Zahlen (Tausenderpunkt, Leerzeichen) in der Antwort-Auswertung der App.
- Einspielen, Datenbank, Testsitzungen, Rückmeldungs-Anzeige: nicht geprüft (nicht Teil des Auftrags).
