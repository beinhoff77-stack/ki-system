# Vorprüfung W1, 2. Durchgang: Runde VT1A mit 55 Aufgaben (Stand df627805)

Maßstab je Lernziel (5 Aufgaben):
- höchstens eine Schema-Aufgabe (im Zweifel Schema); der Test ist nie Schema und ist die anspruchsvollste Aufgabe;
- mindestens 4 verschiedene Denkfiguren;
- kein Bestandskern;
- genau eine richtige Option, kein Ablenker mit richtigem Urteil und nur falscher Begründung, keine Teilwahrheiten, kein Bauart-Merkmal;
- eindeutig, für Klasse 5 lösbar und verständlich.

Grundlage wie im 1. Durchgang (Urteil 1222).

Geprüft habe ich alle 55 Aufgaben einzeln, die 42 neuen besonders gegen den Bestand:
- `inhalte/themen/<einheit>.json` (alle Pools), dazu `rollend-5`, `-11` und `-12`. `rollend-15` und die übrigen `rollend-*` enthalten keine Aufgaben dieser Einheiten.
- Zusätzlich die R-Lernziele `vertauschen` und `berechnen` (Potenzen).

Rechenskript `vorpruefung_w1_rechnen.py` (auf 55 Aufgaben umgestellt; die Fassung für 77 Aufgaben steht in Commit 68cffcf9):
- Es rechnet alle Aufgaben exakt nach und bestimmt Abzähl- und Grenzaufgaben durch Aufzählen.
- Jede Auswahl-Option wird einzeln bewertet.
- Bei den Kinderregel-Aufgaben prüft es, dass keine naheliegende andere Regel alle Beispiele ebenfalls erfüllt.
- Ergebnis: **0 Abweichungen**.

Ausdrücklich nachgerechnet:
- 011: □ = 7 001; 7 000 ergibt Gleichheit.
- 016: 6⁶ : (2 · 3⁶) = 2⁵ = 32.
- 021: 391 931 − 316 931 = 75 000.
- 006: 4 · n + 4 = 44, also n = 10 und 100 Plättchen; eindeutig.
- 031: 4 Paare (1·100, 2·50, 4·25, 5·20).
- 041: 7 (1, 2, 3, 4, 6, 9, 12).
- 017: 5 (48, 24, 12, 6, 3).
- 004: Unter allen Paaren mit Basis und Hochzahl von 2 bis 29 ist 2² das einzige mit Gleichheit, und es gibt keines, bei dem das Produkt größer ist.

## Urteil

| Einheit | bereit für die Gegenprüfung | Grund |
|---|---|---|
| zahlen.potenzen_basis | **ja, bedingt** | Kein A-Befund. Vorher empfohlen: B4 (Test 016 zu schwer) und B7 (Test 016 und Korrektur 018 prüfen dieselbe Fehlvorstellung). |
| zahlen.rechengesetze | **nein** | In 4 Lernzielen gibt es je 2 Schema-Aufgaben (A1–A4). |

Zahl der Befunde: **A 4, B 7, C 9**.

## Entscheidungen zu den Angriffspunkten des Schreibers

| Punkt | Entscheidung |
|---|---|
| Schema-Grenzfälle 025, 033, 045, 030 | **Alle vier sind Schema.** 025: Gegen die richtige Option tritt ernsthaft nur 97 · 348 + 6 an; der Rest ist mit zwei Malaufgaben auszurechnen, und die Einsicht steht als Bestandskern in themen klammern („(a + b) · c größer als a + b · c“). 030: Text in Term übersetzen und zwei kleine Werte ausrechnen. 045: Die vier Gleichungen sind einzeln lösbar (224 · 74, 8 288 : 74 …); „ohne zu lösen“ lässt sich nicht erzwingen. 033: zwei sechsstellige Subtraktionen genügen. Folge: In klammern, termaufbau und umkehraufgabe_mal sind es 2 Schema (A1–A3). In vorteil bleibt 033 die einzige. |
| Denkfigur-Nähe 046/050 | getrennt zählen: Schranke durch Aufrunden ist etwas anderes als die Richtung beim Teilen. Nah beieinander liegen dafür **046 und 049** (beide Schranken), das ist zweimal und damit erlaubt. |
| 053/054 | **eine Denkfigur** (Reihenfolge von + und · ist nicht vertauschbar, einmal rückwärts, einmal vorwärts). sach hat damit genau 4 (Grenze). |
| 044/045 | **eine Denkfigur** (wie die Lösung von a abhängt). umkehraufgabe_mal hat genau 4; 045 ist außerdem Schema (A3). |
| 037/040 | getrennt zählen (additive Änderung über Zerlegen gegen Skalierung des gemeinsamen Faktors), aber nah. |
| Bauplan „Kinderregel aus Beispielen erschließen“ | **wird zum erkennbaren Muster**, siehe B1. Es sind 8 Aufgaben mit nahezu gleichem Wortlaut (002, 012, 022, 029, 039, 042, 047, 053), 6 davon in der Korrektur. |
| Bestandsnähe 047, 025, 015, 039, 042 | 025: Bestandskern (siehe oben, Teil von A1). 047: gleiche Fehlvorstellung wie rollend-5 „4 987 auf Tausender: 4 000“, aber andere Leistung, darf bleiben (C). 015: gleiche Einsicht wie themen „Nullen von 50 · 10⁴“, andere Leistung, darf bleiben. 039: kein Bestandskern. 042: gleiche Fehlvorstellung wie themen „(−7) · x = 56 mit x = 56 · (−7)“, andere Leistung, darf bleiben. **Neu gefunden:** 031 benutzt dieselbe Rechnung und dieselben Zahlen wie themen vorteil „Ergänze 25 · □ · 4 = 3 700“ (3 700 = 37 · 100), siehe B5. |
| einschränkende Ablenker 004 („Fast immer …“), 015 | in Ordnung. „Fast immer“ ist dort die **richtige** Option. Kein Ablenker hat ein richtiges Urteil; jeder wird durch 2², 2³ oder 3² bzw. 3 · 10² oder 50 · 10³ widerlegt. |
| 004 für Klasse 5 beweisbar? | Nein, nur durch Beispiele plausibel zu machen („sonst immer größer“). Das genügt, weil die drei Ablenker an kleinen Beispielen widerlegbar sind und die richtige Option mathematisch wahr ist (C1). |
| Tests mit Abzähl-Antwort 031, 041, 017 | 041: in Ordnung (Teiler von 36 bis 12, Einmaleins-Wissen, Grundmenge und Grenzen genannt). 017 (Korrektur): eindeutig, wenn man stillschweigend annimmt, dass die Anfangszahl natürlich ist und nur zu vollen Stunden verdoppelt wird (C). 031: Abzählen verdeckt die Einsicht, siehe B5. |
| 011, 016, 021, 006 | alle nachgerechnet und eindeutig (siehe oben). Zu den Fallen: 011 (größer, nicht gleich) siehe C2, 016 (Schwierigkeit) siehe B4, 021 (ausrechenbar) siehe B6. |

## Befunde

### A (Muss)

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| A1 | klammern: 023 und 025 | 2 Schema. 023 ist vom Schreiber selbst als Schema gezählt (Text zu Term). 025 ist durch Ausrechnen lösbar und trägt den Bestandskern „Klammer um die Summe vor dem Mal macht größer“. | 025 ersetzen, z. B. als Zahlaufgabe „Um wie viel ist 97 · (348 + 6) größer als 97 · 348 + 6?“ (576). Die Zahlen sind so groß, dass die Struktur schneller ist als das Rechnen. Oder eine Aufgabe mit einer unbekannten Zahl statt 348. |
| A2 | termaufbau: 027 und 030 | 2 Schema. 030 verlangt Text → Term (das Format der Bestand-Übung) und zwei kleine Werte (54 und 54). Außerdem hat 030 dieselbe Denkfigur wie 027 (verschiedene Terme, gleicher Wert). | 030 ersetzen durch eine Aufgabe ohne Ausrechnen, z. B. „Bei welchem Text ändert sich der Wert, wenn man ‚Summe‘ und ‚Produkt‘ vertauscht?“, oder Texte mit einer unbekannten Zahl. |
| A3 | umkehraufgabe_mal: 043 und 045 | 2 Schema. 043 ist vom Schreiber gezählt; 045 lässt sich durch Lösen der vier Gleichungen beantworten. Dazu dieselbe Denkfigur wie 044. | 045 ersetzen, mit einer anderen Denkfigur als der Abhängigkeit von a, z. B. „Welche Gleichung hat genau dann eine Lösung, wenn …“ oder zwei Geschichten zu derselben Gleichung. |
| A4 | ueberschlag: 048 und 049 | 2 Schema. 048 ist vom Schreiber gezählt. Bei 049 genügt ein einziger grober Überschlag (7 000 · 2 000 = 14 000 000, also 8 Stellen): ein bekanntes Verfahren, und die Schranken braucht man gar nicht. | 049 so bauen, dass der grobe Überschlag an einer Zehnerpotenz-Grenze liegt und erst die Schranken entscheiden, z. B. 3 162 · 3 163 (rund 10 000 000: 7 oder 8 Stellen?). Dann zählt die Einsicht. |

### B (Soll)

| Nr | Kennung | Beleg | Vorschlag |
|---|---|---|---|
| B1 | 002, 012, 022, 029, 039, 042, 047, 053 | **Kinderregel wird zur Routine:** 8 Aufgaben in 8 Lernzielen mit fast demselben Wortlaut („Ein Kind … immer nach derselben (falschen) Regel. Es schreibt: … Welches … mit seiner Regel bei …?“), 6 davon in der Korrektur. Im Verbessern trifft ein Kind damit dasselbe Format über alle Lernziele, das Lösen wird zum Verfahren: typischen Fehler raten und anwenden. Didaktisch bei den 7 Zahlaufgaben: Ausgerechnet nach einem eigenen Fehler soll das Kind ein mathematisch **falsches** Ergebnis eingeben, und das richtige Ergebnis wird als Fehlbild „richtig gerechnet“ zurückgewiesen. | Höchstens in 3–4 Lernzielen behalten, verschieden formuliert. In den übrigen nach der Regel fragen (Auswahl wie 029) oder nach dem richtigen Wert *und* der Regel. In der Korrektur möglichst keine Aufgabe, deren Lösung ein falscher Wert ist. |
| B2 | 005, 018, 023, 034, 038, 055 | **Neues Bauart-Muster „Zwillings-Ablenker“:** In diesen 6 Auswahl-Aufgaben beginnen genau zwei Optionen gleich (mindestens 5 Wörter), und die richtige ist **jedes Mal** eine der beiden (6 von 6; zufällig wären es 50 %, also 1 : 64). Der Ablenker ist als kleinste Abwandlung der richtigen Option gebaut. Sonst ist die Bauart jetzt sauber: „=“ 4 %/4 %, „·“ 14 %/12 %, denn/weil 11 %/12 %, darf/muss/man 4 %/7 %, Absolutwörter 36 %/36 %; die richtige Option ist 3-mal allein die längste und 5-mal allein die kürzeste (von 34). | In mindestens der Hälfte dieser Aufgaben zwei *falsche* Zwillinge bauen oder die Anfänge auflösen. Prüfung in `bauen.py`: „Paar mit gleichem Anfang enthält die richtige Option“ höchstens in der Hälfte der Aufgaben. |
| B3 | Tests 001, 036, 046 (dazu 009) | Gleiche Test-Vorlage „Drei der vier … Welche … ist anders / muss genau gerechnet werden?“ in 3 von 11 Tests. Der Flugtest zieht alle Tests nacheinander, die Vorlage wird erkennbar. | Einen der drei Tests (am ehesten 046 oder 036) in eine andere Form bringen (Zahl oder Urteil mit Begründung). |
| B4 | 016 (Test sach) | Zu schwer, nur sehr starke Kinder lösen es in 2–3 Minuten. Nötig ist (2 · 3)⁶ = 2⁶ · 3⁶ und das Kürzen gegen 2 · 3⁶; der Rechenweg 46 656 : 1 458 überfordert in Klasse 5. Zusätzlich gehen ein „Wievielmal“ großer Zahlen und eine Potenz-Einsicht zusammen. | Nach der Zahl der überzähligen Faktoren fragen: „Wie viele Faktoren 2 stehen in 6⁶ mehr als in der richtigen Rechnung?“ (5). Oder 4 Tage statt 6 und Auswahl mit Begründungen. |
| B5 | 031 (Test vorteil) | Die Abzähl-Antwort verdeckt das Verstehen: Wer 3 700 = 37 · 100 erkennt, kann trotzdem ein Paar übersehen (meist 4 · 25), und das Ergebnis ist falsch. Außerdem ist der Kernschritt mit denselben Zahlen (3 700, 37, 100) die Bestand-Übung „25 · □ · 4 = 3 700“. | Zahlen ändern und so einschränken, dass genau ein Paar bleibt, z. B. „□ · 23 · △ = 4 600, □ und △ größer als 5, □ < △“: Es bleibt nur 8 · 25, gefragt wird nach △. |
| B6 | 021 (Test klammern) | Ohne Einsicht lösbar: drei sechsstellige Strichrechnungen sind in Klasse 5 schriftlich machbar (gut 2 Minuten). Nach dem Maßstab „Test nie Schema“ ist das ein Risiko. | Die erste Zahl unbekannt lassen („Von einer Zahl wird 129 486 abgezogen und 37 500 addiert. Nun wird eine Klammer um 129 486 + 37 500 gesetzt …“); dann geht es nur über die Struktur. |
| B7 | 016 / 018 | Test und Korrektur prüfen teilweise dieselbe Einzelfrage: 016 handelt von der Fehlvorstellung „Startzahl und Faktor zur Basis 6 zusammenfassen“, 018 hat genau diese als Ablenker („versechsfacht“, 6⁵). | Den Ablenker in 018 durch eine andere Fehlvorstellung ersetzen (z. B. Hochzahl als Zahl der Blätter am Ende). |

### C (Kann)

| Nr | Kennung | Beleg / Vorschlag |
|---|---|---|
| C1 | 004 | „sonst ist die Potenz größer“ ist in Klasse 5 nicht beweisbar, nur an Beispielen glaubhaft. Zulässig. Im Lösungsweg den Grund knapp nennen (eine Basis von mindestens 2 malnehmen mindestens verdoppelt). |
| C2 | 011 | Die Grenze „größer, nicht gleich“ entscheidet zwischen 7 000 und 7 001. Ein Kind mit der richtigen Einsicht, das die Grenze überliest, gilt als falsch. Die Grenze ist genannt, das ist zulässig; eventuell „größer (nicht gleich)“ fett oder ausdrücklich. |
| C3 | 033 | Ich zähle die Aufgabe als Schema (zwei Subtraktionen genügen), der Schreiber nicht. In vorteil bleibt es bei 1 und damit zulässig. |
| C4 | 038 | Term ↔ Text. Nach der eigenen Zählregel des Schreibers (005, 018, 023, 027, 043, 055) ist das Schema; in verteilen bleibt es bei 1 und damit zulässig. `schema` auf „ja“ setzen. |
| C5 | 046 | „einfacher Überschlag“ ist nicht festgelegt. Die Meta-Frage (wann entscheidet ein Überschlag sicher) ist anspruchsvoll, für gute Kinder aber lösbar. Option 3 ähnelt der themen-Übung „Kino 12 Reihen … 3 Klassen“, darf bleiben. |
| C6 | 017 | Stillschweigende Annahmen (Anfangszahl natürlich, Verdopplung zur vollen Stunde) in einem Halbsatz nennen. |
| C7 | 026 | Der Test ist ein Ein-Schritt-Gedanke (16 : 4); 029 (Regel an drei Beispielen prüfen) ist kaum leichter. Als anspruchsvollste vertretbar, aber knapp. |
| C8 | Einsicht wie im Bestand, andere Leistung (darf bleiben) | 001 (vertauschen-Bonus 4¹⁹ in 2⁴⁰; berechnen 2ⁿ = 4 · 16), 005 (berechnen „Welche Rechnung gehört zu 4³?“, andere Etappe), 006 (themen Randfliesen 15 · 15, vorwärts), 015, 021 (themen 30 − (10 − 4)), 029 (themen „7 + 3 · 5 ist ein Produkt …“), 042, 047, 050 (themen Richtung beim Überschlag einer Summe). |
| C9 | ueberschlag | Regel fehlt (laut Auftrag nur vermerkt). |

## Tabelle je Lernziel

| Lernziel | Schema (meine Zählung) | Denkfiguren | Test ok? | Würde ein gutes Kind der 5. Klasse den Test in 2–3 Minuten lösen? Was muss es verstanden haben? |
|---|---|---|---|---|
| schreibweise (001–005) | 005 (004 Grenzfall: Beispiele prüfen) | Faktoren umgruppieren 001 · Fehlregel vertauschen 002 · Wirkung der Hochzahl 003 · Potenz gegen Produkt 004 · Geschichte zu 4³ 005 (5) | ja | Ja (mittel). Eine Potenz zählt Faktoren, und eine Basis lässt sich in Zweier zerlegen (4 = 2 · 2, 8 = 2 · 2 · 2); dann ist 8⁵ = 2¹⁵ sofort anders. 32 und 1 024 braucht man dafür nicht. |
| quadrat (006–010) | 009 (010 Grenzfall) | Rand rückwärts 006 · Skalieren ·9 007 · (a + b)² am Bild 008 · Endziffer 009 · Nachbarquadrate 010 (5) | ja | Ja (mittel bis schwer). Der Rand besteht aus 4 Seiten zu je n und 4 Ecken; man kann auch Quadratzahlen probieren (12² − 10² = 44). |
| zehner (011–015) | 014 | Faktor und Hochzahl verrechnen 011 · Fehlregel Hochzahlen mal 012 · Wirkung auf eine Summe 013 · Stellen bündeln 014 · Nullen zählen allgemein 015 (5) | ja | Ja. 10¹¹ = 10³ · 10⁸, also 7 · 10¹¹ = 7 000 · 10⁸, und „größer“ heißt 7 001 (C2). |
| sach Potenzen (016–020) | 018 | Startzahl unter der Hochzahl 016 · rückwärts mit Wahl 017 · Term ↔ Geschichte 018 · Verhältnis bleibt 019 · linear gegen Verdoppeln 020 (5; 016 und 018 teilen eine Fehlvorstellung) | **knapp** (B4) | **Eher nein, nur sehr starke Kinder** (B4). Es braucht (2 · 3)⁶ als sechsmal 2 und sechsmal 3 und das Kürzen gegen 2 · 3⁶. |
| klammern (021–025) | 023, **025** (2) | Klammer kehrt ein Zeichen um 021 · Fehlregel Klammern weg 022 · Modell mit Klammer 023 · Verbinden in Ketten 024 · Klammer-Vergleich 025 (5) | ja, mit Risiko (B6) | Ja. Durch die Klammer wird die 37 500 abgezogen statt addiert, das macht zweimal 37 500 aus. Ausrechnen geht auch (B6). |
| termaufbau (026–030) | 027, **030** (2) | Änderungswirkung 026 · verschiedene Terme, gleicher Wert 027 und 030 · Termart herstellen 028 · Fehlregel benennen 029 (4) | ja, knapp (C7) | Ja (leicht bis mittel). Die Änderung des Rabatts wirkt durch das : 4 nur geviertelt; die großen Produkte bleiben gleich. |
| vorteil (031–035) | 033 | Zusammenfassen und Zerlegen 031 · Ausgleich beim Produkt 032 und 035 · Ausgleich bei der Differenz 033 · Umstellen mit Zeichen 034 (4) | ja, mit Risiko (B5) | Ja, aber Abzählfehler sind wahrscheinlich (B5). Faktoren vertauschen, also □ · △ = 100, und dann alle Zerlegungen von 100 ohne 10 · 10. |
| verteilen (036–040) | 038 (C4) | Zerlegung prüfen (Kreuzterme fehlen) 036 · Faktor ändern 037 · Terme deuten 038 · Fehlregel bei einem Produkt in der Klammer 039 · gemeinsamer Faktor skaliert 040 (5) | ja | Ja. Beim Verteilen wird jeder Teil mit dem ganzen anderen Faktor malgenommen; Teil mal Teil reicht nicht. |
| umkehraufgabe_mal (041–045) | 043, **045** (2) | Lösbarkeit über Teiler 041 · Fehlregel beim Divisor 042 · Gleichung zur Geschichte 043 · Abhängigkeit von a 044 und 045 (4) | ja | Ja (leicht bis mittel). a · x = 36 ist genau dann lösbar, wenn 36 in der Reihe von a steht; die Grenze 12 ist eingeschlossen. |
| ueberschlag (046–050) | 048, **049** (2) | Schranke sicher 046 und 049 · Fehlregel Abschneiden 047 · feiner runden ist genauer 048 · Richtung beim Teilen 050 (4) | ja | Ja, für gute Kinder, aber anspruchsvoll (C5). Liegt ein aufgerundeter Überschlag unter der Grenze, reicht es sicher; bei 26 · 19 entscheidet keine einfache Rundung. |
| sach Rechengesetze (051–055) | 055 (052 Grenzfall) | zwei Tarife vergleichen 051 · Rest deuten 052 · Reihenfolge der Schritte 053 und 054 · Modellwahl Gleichung 055 (4) | ja | Ja. B ist 8 € billiger, wird aber je GB 2 € teurer; nach 4 GB sind beide gleich, „teurer“ gilt ab 5. Lösbar auch mit einer kleinen Tabelle (Modell selbst aufstellen = Transfer). |

## Protokoll je Aufgabe

„R ok“ heißt: Die eigene Rechnung stimmt mit der Sollantwort überein, bei Auswahl ist genau eine Option wahr, und die Fehlbilder sind ungleich der Lösung und passen zur Rechnung.

- 001 (T): R ok (8⁵ = 2¹⁵) · Ablenker ok · Verstehen · Einsicht wie vertauschen-Bonus · B3
- 002 (K): R ok (25; Regel eindeutig) · – · Verstehen · Fehlvorstellung des R-Lernziels vertauschen · B1
- 003 (K): R ok (3¹³) · ok · Verstehen (3¹² nicht ausrechenbar) · – · ok
- 004 (S): R ok (nur 2² gleich) · keine Teilwahrheit · Grenzfall · – · C1
- 005 (S): R ok · Zwillings-Ablenker 1/3 · Schema (gezählt) · berechnen „4³“ (andere Etappe) · B2, C8
- 006 (T): R ok (100, eindeutig) · ok · Verstehen · themen Randfliesen (vorwärts) · C8
- 007 (K): R ok (450) · ok · Verstehen · – · ok
- 008 (K): R ok (zwei Rechtecke 30 × 7) · ok · Verstehen · – · ok
- 009 (S): R ok · ok · Schema (gezählt) · Einsicht wie themen Endziffer · ok
- 010 (S): R ok (immer 2n) · ok · Grenzfall · – · ok
- 011 (T): R ok (7 001) · ok · Verstehen · – · C2
- 012 (K): R ok (12; Regel eindeutig) · – · Verstehen · – · B1
- 013 (K): R ok (10-mal) · ok · Verstehen · – · ok
- 014 (S): R ok (999 000) · ok · Schema (gezählt) · nahe themen Stufenzahlen · ok
- 015 (S): R ok (manchmal) · keine Teilwahrheit · Verstehen · Einsicht wie themen 50 · 10⁴ · ok
- 016 (T): R ok (32) · ok · Verstehen · Fehlvorstellung wie berechnen 2 · 5² · B4, B7
- 017 (K): R ok (5) · ok · Verstehen · rollend-12 rückwärts (andere Leistung) · C6
- 018 (K): R ok · Zwillings-Ablenker 1/3; Ablenker 6⁵ wie Test 016 · Schema (gezählt) · – · B2, B7
- 019 (S): R ok (2) · ok · Verstehen · – · ok
- 020 (S): R ok (B überholt nach 11 Stunden und bleibt vorn) · ok · Verstehen · – · ok
- 021 (T): R ok (75 000) · ok · Verstehen mit Rechenweg-Risiko · Einsicht wie themen 30 − (10 − 4) · B6
- 022 (K): R ok (23; Regel eindeutig, auch „von links nach rechts“ scheidet aus) · – · Verstehen · – · B1
- 023 (K): R ok (29) · Zwillings-Ablenker 1/3 · Schema (gezählt) · – · B2, A1
- 024 (S): R ok (Plus nie; Minus und Geteilt ändern; Mal nicht jedes Mal) · ok · Verstehen · – · ok
- 025 (S): R ok (97 · 354) · ok · **Schema** · themen klammern „(a + b) · c > a + b · c“ · A1
- 026 (T): R ok (4 kleiner) · ok · Verstehen · – · C7
- 027 (K): R ok (① und ②) · ok · Schema (gezählt) · – · A2
- 028 (K): R ok (− durch ·) · ok · Verstehen · themen Termart (andere Leistung) · ok
- 029 (S): R ok (Zeichen ganz rechts; die anderen Regeln scheitern an einem Beispiel) · ok · Verstehen · themen „7 + 3 · 5 Produkt“ · B1, C8
- 030 (S): R ok (verschieden, gleicher Wert 54) · ok · **Schema** · Text → Term wie themen · A2
- 031 (T): R ok (4) · – · Verstehen, Abzählrisiko · gleiche Zahlen wie themen 25 · □ · 4 = 3 700 · B5
- 032 (K): R ok (gleich, 787 500) · „beide“ nur in der richtigen Option · Verstehen · – · ok
- 033 (K): R ok (6) · – · Schema (C3) · – · C3
- 034 (S): R ok (Zeichen mitnehmen) · Zwillings-Ablenker 0/1 · Verstehen · – · B2
- 035 (S): R ok (9) · – · Verstehen · – · ok
- 036 (T): R ok (300 · 40 + 68 · 7 = 12 476 ≠ 17 296) · ok · Verstehen · – · B3
- 037 (K): R ok (7 041) · – · Verstehen (Grenzfall) · – · ok
- 038 (K): R ok · Zwillings-Ablenker 1/2 · Schema (C4) · rollend-5 Rechteck-Term · B2, C4
- 039 (S): R ok (350; Regel eindeutig) · – · Verstehen · – · B1
- 040 (S): R ok (dreimal) · ok · Verstehen · – · ok
- 041 (T): R ok (7) · – · Verstehen · – · ok
- 042 (K): R ok (576) · – · Verstehen · Fehlvorstellung wie themen (−7) · x · B1, C8
- 043 (K): R ok · ok · Schema (gezählt) · – · A3
- 044 (S): R ok (dreimal so klein, für alle zulässigen a) · ok · Verstehen · – · ok
- 045 (S): R ok (x : 74 = 224) · ok · **Schema** · – · A3
- 046 (T): R ok (nur 26 · 19 offen; genau 494) · ok · Verstehen · themen Kino/Klassen · B3, C5
- 047 (K): R ok (7 000; Regel eindeutig) · – · Verstehen · rollend-5 4 987 → 4 000 · B1, C8
- 048 (K): R ok · ok · Schema (gezählt) · – · A4
- 049 (S): R ok (8 Stellen, 16 747 974) · – · **Schema** · Größenordnung wie themen · A4
- 050 (S): R ok (größer, 804) · ok · Verstehen · Einsicht Richtung wie themen (Summe) · C8
- 051 (T): R ok (5) · – · Verstehen (Modell) · – · ok
- 052 (K): R ok (4 Busse) · ok · Grenzfall · – · ok
- 053 (K): R ok (1; Regel eindeutig) · – · Verstehen · rollend-5 rückwärts · B1
- 054 (S): R ok (immer um 6, für alle Startzahlen) · ok · Verstehen · – · ok
- 055 (S): R ok (25) · Zwillings-Ablenker 2/3 · Schema (gezählt) · – · B2
