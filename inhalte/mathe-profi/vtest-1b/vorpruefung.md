# Vorprüfung Runde VT1B (unabhängig, alle 119 Aufgaben VT1B-001 bis VT1B-119)

Stand 28.11.2026. Prüfer: unabhängig vom Autor; keine Aufgabe und kein fremder Code geändert. Eigene Rechnung: `vorpruefung_rechnen.py` (liegt neben dieser Datei; Aufruf `python3 -I inhalte/mathe-profi/vtest-1b/vorpruefung_rechnen.py [--bestand]` im Wurzelordner). Alle 119 Aufgaben mit Text, Möglichkeiten, Fehlbildern und Lösungsweg von Hand gelesen.

Kennzeichnung: **[F]** = Tatsache (nachgerechnet, im Repo gelesen, Werkzeug-Ausgabe) · **[A]** = Annahme oder Einschätzung.

## Gesamturteil: bereit für die Gegenprüfung **nach Korrektur**

[F] Alle 119 Sollantworten stimmen mit meiner eigenen, aus dem Aufgabentext hergeleiteten Rechnung überein (81 Zahl-/Lückenaufgaben mit exakten Brüchen, Gauß-Formel und Zählschleifen; 38 Auswahl-Aufgaben von Hand und per Rechnung der Behauptungen). Alle Fehlbild-Rechnungen ergeben die gespeicherte Antwort (Werkzeug und eigene Prüfung). Alle Figuren der Geometrie existieren (Höhe ≤ schräge Seite, positive Koordinaten).

[F] Ein Befund A: **VT1B-090** (Fehler-Detektiv: die als „erster Fehler“ gespeicherte Zeile 2 ist eine wahre Aussage, falsch ist erst Zeile 3).

[A] Trotzdem nicht ohne Korrektur einspielbar, weil (1) 090 falsch gewertet würde, (2) rund ein Drittel der Aufgaben im Kern Rechnen nach Schema ist, obwohl `typ`/`form` Verstehen behaupten, (3) mindestens 22 Aufgaben Bestandsübungen so nahe sind, dass sie „dieselbe Aufgabe mit anderen Zahlen“ sind (das Werkzeug erkennt sie nicht), (4) in elf von siebzehn Lernzielen dieselbe Denkfigur drei- bis viermal vorkommt, obwohl das Feld `idee` verschiedene Namen trägt, (5) bei den Tests in 11 von 17 Lernzielen eine leichtere Aufgabe als Test steht, als das Lernziel hergibt, und (6) die Lehrplanzuordnung zweier Einheiten im Repo selbst widersprüchlich ist.

| Zahl | Wert |
|---|---|
| geprüfte Aufgaben | 119 |
| Sollantwort nach eigener Rechnung richtig und eindeutig | 118 (VT1B-090: Soll stimmt als Zahl, die Zeile nicht) |
| Befund A (muss korrigiert werden) | 1 (090) |
| Befund B (sollte korrigiert werden) | 60 (001, 002, 003, 004, 008, 009, 010, 011, 016, 017, 018, 020, 025, 026, 027, 029, 030, 031, 032, 036, 037, 038, 039, 043, 044, 046, 047, 093, 096, 099, 103, 107, 110, 116, 117, 050, 051, 055, 057, 060, 061, 062, 063, 065, 066, 067, 068, 070, 071, 073, 075, 078, 079, 080, 081, 082, 084, 085, 086, 089) |
| Befund C (Hinweis) | 43 (005, 006, 012, 013, 015, 019, 021, 022, 023, 024, 028, 033, 035, 040, 042, 049, 092, 095, 100, 101, 102, 104, 106, 108, 109, 112, 113, 114, 118, 119, 052, 054, 058, 059, 064, 069, 072, 074, 076, 077, 083, 088, 091) |
| ohne Befund | 15 (007, 014, 034, 041, 045, 048, 094, 097, 098, 105, 111, 115, 053, 056, 087) |

(Zählung nach dem jeweils schwersten Befund je Aufgabe. Dazu die übergreifenden Befunde G1–G8 weiter unten.)

## Werkzeuge, selbst ausgeführt

| Werkzeug | Ergebnis |
|---|---|
| `python3 -I tools/vtest_pruefen.py --runde 1b` | [F] 119 Aufgaben, 17 Lernziele, „OK – keine Fehler“, 108 Hinweise: 105 × „Regel fehlt“, 1 × Rhythmus RRVRVV bei `bruch.prozent`, 2 × Abweichung vom Vorschlag (`bruch.prozent`, `gleichungen.bruch`). Keine der Hinweise ist ein Fehlalarm. |
| `python3 -I inhalte/mathe-profi/vtest-1b/gegenrechnung.py` | [F] „119 Aufgaben nachgerechnet, davon 24 zusätzlich ganz neu …, 0 Abweichungen“. |
| `python3 -I inhalte/mathe-profi/vtest-1b/bauen.py` | [F] „119 Aufgaben geprüft, 0 Meldungen“, endet „OK“; `git status` danach ohne Änderung (Erzeugung stabil). |
| mein `vorpruefung_rechnen.py` | [F] Teil A: 81 Zahl-/Lückenaufgaben mit eigenem Sollwert aus dem Text, 0 Abweichungen (Prozente, Prozentketten, Brüche, Zählaufgaben 023, 035, 038, 042, 074, 087, 088 per Schleife/Brute-Force; Flächen 093, 107, 112 mit Gauß-Formel). Teil B: Platz und Länge der richtigen Möglichkeit, Ähnlichkeit der Möglichkeiten. Teil C: kein Fehlbild gleich dem Soll; keine gleiche Sollantwort zweier Zahl-/Lückenaufgaben im selben Lernziel. Teil D (`--bestand`): Ähnlichkeit gegen 28 906 Bestandsaufgaben (viele Zufallstreffer, die Treffer unten habe ich von Hand gelesen). |

## Befundtabelle

Schweregrad: A = fachlich falsch/mehrdeutig, muss korrigiert werden; B = sollte korrigiert werden; C = Hinweis. (Alle Befunde auf einen Blick, nach Kennung; Aufgaben ohne Eintrag: siehe „ohne Befund“.)

| Kennung | Grad | Befund | Korrekturvorschlag |
|---|---|---|---|
| VT1B-090 | A | Der Fehler-Detektiv hat keine falsche Zeile an der gespeicherten Stelle. Zeile 2 „Es gilt 3 > 2.“ ist eine wahre Aussage; Zeile 1 ist nur eine Ankündigung. Der erste falsche Satz ist Zeile 3 („Also ist 3 · 10⁻⁵ größer …“). Gespeichert ist aber Zeile 2. Ein Kind, das richtig „Zeile 3“ antwortet, wird als falsch gewertet, und das Fehlbild „Zeile 3 genannt, weil dort das falsche Ergebnis steht“ nennt genau die richtige Überlegung einen Fehler. | Zeile 2 wirklich falsch machen: „Zeile 2: Die Exponenten spielen für den Vergleich keine Rolle, es zählt nur 3 > 2.“ Dann ist Zeile 2 der erste Fehler (gespeichert bleibt [2; 20]); Fehlbild „3“ und Lösungsweg anpassen („Zeile 2 behauptet etwas Falsches …“). Dieselbe Denkfigur wie der Test 085 (siehe dort). |
| VT1B-001 | B | Doppelung mit dem Bestand: dieselben Zahlen 40 und 50 wie die Übungen `bruch.prozent` Stufe 3 („Spendenlauf: 40 → 50 Kinder, um wie viel Prozent gestiegen?“ und „50 → 40, gesunken?“) und `rollend-2/g8` G8-12 („50 € → 40 €, Anna sagt 25 %“). Nur als Auswahl verpackt. Zwei Möglichkeiten (0 und 2) teilen den ersten Satz; die richtige ist Teil dieses Zwillingspaars. Nicht die schwerste Aufgabe des Lernziels (006, 007 sind Stufe 3 mit mehr Denkarbeit). | Andere Zahlen und anderer Kontext (z. B. Zinssatz 2 % → 3 %: „um 1 Prozentpunkt“ gegen „um 50 %“), Ablenker ohne Zwillingspaar; als Test eher 007 (Anteil bei Zuzug gleich halten) nehmen. |
| VT1B-002 | B | Im Kern Rechnen: 85 % von 40 (Prozentwert), obwohl `typ umkehr`/`form umkehren` und Lernziel `prozentsatz` behauptet werden. Es wird kein Prozentsatz gesucht und nichts umgekehrt. | Echte Umkehrung: „34 von 40 Fragen richtig – gerade noch bestanden. Wie viel Prozent mussten es mindestens sein?“ (Prozentsatz, 85) oder Grundwert rückwärts („34 Fragen sind 85 %: Wie viele hat das Quiz?“). |
| VT1B-003 | B | Doppelung: Die Übungen (`bruch.prozent`, verstehen Stufe 3) haben „Der Anteil der Kinder mit Fahrradhelm steigt von 30 % auf 36 %. Um wie viele Prozentpunkte?“ und „20 % → 30 %“. Dieselbe Idee, hier nur mit zwei Brüchen davor. Prozentpunkte stehen im Repo nur bei der Bestands-Übung, den Lehrplanbeleg konnte ich nicht prüfen. | Andere Denkfigur: „Zwei Tests … um wie viel Prozent mehr richtige Aufgaben?“ (relative Änderung des Anteils, Grundwert 75 %) – das ist neu, aber Klasse-7-Stoff (siehe Abschnitt Lehrplan); alternativ als C belassen. |
| VT1B-004 | B | Rechnen nach Schema (126 : 360 · 100). Der „Darstellungswechsel“ ist ein Standardschritt. Kein Verstehen. | Ersetzen durch eine Aufgabe, die den Zusammenhang prüft: „Ein Sektor ist doppelt so groß wie der Sektor Bus (63°). Wie viel Prozent?“ ohne Rechenweg, oder „Welche Angabe passt nicht zum Kreisdiagramm?“. |
| VT1B-008 | B | Test-Aufgabe ist nicht die anspruchsvollste des Lernziels (011 und 013 verlangen mehr Einsicht). Der Standardfehler „Prozente auf den neuen Preis“ ist bereits eine Bestandsübung in `bruch.prozent_grundwert`; „Preis nach Rabatt → alter Preis“ hat die Bestandsdatei `bruch.prozent` ausdrücklich als Klasse-7-Stoff entfernt (Feld `offen`). | Als Korrektur/Sicherung verwenden; Test: 013 (zwei Angebote) oder eine Aufgabe mit Fehler-Detektiv in einer Zwei-Schritt-Änderung. Lehrplanfrage klären (Abschnitt Lehrplan). |
| VT1B-009 | B | Doppelung und Klasse-7-Nähe: Bestand `bruch.prozent_grundwert` Stufe 3 „Im Schlussverkauf kostet ein Rucksack nach 35 % Rabatt noch 52 €. Wie viel kostete er vorher?“ – gleicher Rabatt, gleiche Denkfigur. Rechnen nach Schema (117 : 0,65). | Entfernen oder durch eine Aufgabe ersetzen, die nicht Grundwert rückwärts ist. |
| VT1B-010 | B | Rechnen nach Schema (Aufschlag, Gesamtpreis, durch 6); `form bruecke`/`typ mehrschritt` sind Etiketten. Zeitaufwand gering. | Als Stufe-2-Rechenaufgabe belassen und nicht als Verstehen zählen, oder die Raten-Frage zur Bewertung wenden („Welches Angebot ist günstiger …?“). |
| VT1B-011 | B | Doppelung: Bestand `bruch.prozent` Bonus „Ein Händler erhöht einen Preis um 25 % und gibt danach 20 % Rabatt. Wie viel Prozent des Anfangspreises zahlt der Kunde?“ – gleiche Frage, andere Zahlen (40/25 statt 25/20). Dazu die Lehrplanfrage (Doppelrabatt als Rechenaufgabe hat die Bestandsdatei als Klasse-7-Stoff entfernt). | Zahlen und Frage ändern (z. B. „Erst 20 % billiger, dann 25 % teurer: Ist der Preis höher oder niedriger als vorher?“ als Begründung) oder streichen. |
| VT1B-016 | B | Dieselbe Denkfigur wie 015 und 017 („um 200 % steigen“ ≠ „auf 200 %“); im Kern Rechnen (30 + 2 · 30). | 016 ersetzen (z. B. Aussagen über Prozentzahl und Faktor, die nicht Zunahme/Verdopplung sind). |
| VT1B-017 | B | Gleiche Denkfigur wie 015/016 (verdoppelt = um 100 %); die Möglichkeiten sind nach Größe der Prozentzahl geordnet. | Anders gestalten oder streichen (siehe 016). |
| VT1B-018 | B | Rechnen nach Schema (40 : 0,5 oder verdoppeln); gleiche Rückrechnung wie 008 und 009. Der Lernziel-Schwerpunkt „verstehen“ ist hier nicht erkennbar. | Ersetzen durch Gegenbeispiel-Aufgabe („Warum kann ein Preis nie um 120 % gesenkt werden?“). |
| VT1B-020 | B | Doppelung: Bestand verstehen Stufe 3 „In Klasse A spielen 50 % der 20 Kinder ein Instrument, in Klasse B 40 % der 30 Kinder. Jemand sagt: In A spielen mehr Kinder ein Instrument.“ – gleiche Denkfigur (Prozent gegen Anzahl). Zeile 3 ist als Allgemeinaussage „nicht gefolgert“, falsch wird sie erst durch die nachgeschobenen Klassengrößen in der Frage (vertretbar, aber knapp). | Neue Einkleidung mit anderer Denkfigur (z. B. Abnahme in zwei Schritten) oder die Klassengrößen schon in Zeile 1 nennen, damit Zeile 3 eindeutig falsch ist. |
| VT1B-025 | B | Die richtige Möglichkeit ist die einzige mit drei Elementen und strikt die längste (18 gegen 11–15 Zeichen). Fehlbild 0 („x² − 16 = 0 als x = 16 gelesen“) erklärt nur die Zahl 16, die Möglichkeit enthält aber 4 und 16: Text führt nicht zur Möglichkeit. Nah an der Bestandsübung „Bestimme die Definitionsmenge von 1/(x² − 2x) = 4/(x − 2)“ mit vier Mengen. | Eine zweite Möglichkeit mit drei Elementen (z. B. ℚ \ {−16; 0; 16}), Fehlbild 0 neu fassen („x² = 16 zu x = 4 und 16 gemacht“ oder Möglichkeit ändern). |
| VT1B-026 | B | Die Summe der ausgeschlossenen Zahlen ist 0 + 5 = 5. Wer den Nenner x vergisst und nur x − 5 betrachtet, kommt auf dieselbe 5: Der Fehler „x ≠ 0 vergessen“ fällt nicht auf (das Fehlbild „0“ ist ein anderer Fehler). Dazu `typ einkleidung`: das Aufstellen ist vorgegeben. | Statt Summe fragen „Wie viele Zahlen sind ausgeschlossen?“ (2) oder ein Nenner x + 2, so dass die Summe 3 ist und der Fehler „nur ein Nenner“ ein anderes Ergebnis gibt. |
| VT1B-027 | B | Grenzfall (vom Autor genannt). Zeile 1 „Aus x² − 9 = 0 folgt x = 3“ ist als Folgerung falsch (x = −3 folgt ebenso), kann aber von einem Kind als „unvollständig, aber richtig für die 3“ gelesen werden; wer so liest und „Zeile 3“ antwortet, ist ebenfalls vertretbar. Zusätzlich Doppelung: `rollend-13/terme.bruchterme` R8-V032 („Aus x² = 9 folgt x = 3, also ist nur x = 3 verboten“) ist derselbe Denkfehler. Die zweite Frage („welche negative Zahl zusätzlich“) verrät den Fehler. | Zeile 1 eindeutig falsch fassen („… folgt x = 3, also ist nur 3 verboten.“) und zweite Frage neutral („Wie viele Zahlen sind richtig ausgeschlossen?“ → 2). Wegen Doppelung andere Gleichung (z. B. x² − 16). |
| VT1B-029 | B | Test ist Regelabruf („über Kreuz geht nur bei a/b = c/d“): Die richtige Möglichkeit ist die einzige mit genau einem Bruch je Seite. Deutlich leichter als 033–035. Die Frage „darf man sofort“ ist eindeutig. | Test: 035 (Parameter k) oder 034; 029 als Korrektur. Oder eine Gleichung mit versteckter Summe ((x + 2)/4 = (3x − 3)/(x − 1) · …) als Falle. |
| VT1B-030 | B | Rechnen nach Schema: Die Gleichung x/(x + 9) = 2/3 ist vorgegeben, es bleibt Über-Kreuz-Rechnen. `typ einkleidung` Etikett. | Gleichung nicht vorgeben („Stelle die Gleichung auf …“ als Auswahl) oder Typ korrigieren. |
| VT1B-031 | B | Reiner Regelabruf (Über-Kreuz-Gleichung hinschreiben); als „darstellung/bruecke“ geführt. Rechnen nach Schema. | Ersetzen durch „Welche Gleichung folgt NICHT äquivalent aus …?“ oder streichen. |
| VT1B-032 | B | Doppelung: `rollend-7/gleichungen.bruch` K8-V074 („6/(x + a) = 2/(x − 1) hat die Lösung x = 3. Wie groß ist a?“) – gleicher Aufbau, gleiches x = 3, hier 8/(x + a) = 2/x. Rechnen nach Schema. | Andere Denkfigur (z. B. a so wählen, dass die Gleichung keine Lösung hat – das ist 035) oder streichen. |
| VT1B-036 | B | Test nicht die schwerste des Lernziels (042, 038 verlangen mehr). Das Wort „Scheinlösung“ steht nur in der richtigen Möglichkeit: Standardformulierung. Dieselbe Sollantwort „L = { }“ wie die Korrektur 037. | Möglichkeiten gleichmäßig formulieren; als Test 042 (Identität mit binomischer Formel) einsetzen und 036 zur Sicherung. |
| VT1B-037 | B | Gleiche Sollantwort wie der Test 036 („L = { }“): Wer den Test falsch hatte und die Lösung gesehen hat, kann die Korrektur raten. Richtig ist die einzige Möglichkeit, die „Definitionsmenge“ nennt, und der Text nennt D bereits; Ablenker 3 („15 : 3“) ist keine echte Fehlvorstellung. | Korrektur mit Sollantwort ≠ { } (z. B. D enthält die Lösung nicht, aber eine zweite Lösung ist erlaubt: L = {…}). |
| VT1B-038 | B | Dreimal dasselbe Schema (Mal Nenner, Kandidat gegen D prüfen), dann zählen. `typ darstellung` Etikett. Im Bestand gibt es dieselbe Art als „Welche Gleichung liefert x = 4, obwohl 4 nicht zu D gehört?“. | Eine der drei Gleichungen durch eine mit Identität/ohne Lösung wegen anderer Ursache ersetzen oder die Aufgabe als Rechnen führen. |
| VT1B-039 | B | Die Aufgabe nennt den Rechenweg („Mal (x − 4) nehmen und den Kandidaten bestimmen“) – damit ist es Rechnen nach Anleitung. Dieselbe Denkfigur wie 040 (Kandidat gleich verbotener Wert). | Klammerhinweis streichen; 039 oder 040 ersetzen. |
| VT1B-043 | B | Test: Standard-Ansatz einer Verhältnisgleichung (Schatten), deutlich leichter als 049; Möglichkeit 1 (h = 0,25 m für einen Baum) ist durch Schätzen ausschließbar; kein Verstehen über Rechnen hinaus. | Als Korrektur verwenden; Test: 049 oder eine Umkehraufgabe mit zwei Unbekannten. |
| VT1B-044 | B | Rechnen nach Schema (Dreisatz); `typ einkleidung`/`bruecke` Etiketten. | Ersetzen („Warum bleibt das Verhältnis gleich, wenn man beide Seiten um 12 cm verlängert?“ – Gegenbeispiel). |
| VT1B-046 | B | Rechnen nach Schema (Dreisatz, 77 : 7 · 4); `typ umkehr` Etikett. | Streichen oder in 049-Richtung vertiefen. |
| VT1B-047 | B | Rechnen nach Schema (Aufteilen im Verhältnis); in `groessen.verhaeltnisse` gibt es dieselbe Form (Bestand „Drei Geschwister teilen Bonbons im Verhältnis 2 : 3 : 4“, gleiche Verhältniszahlen). | Andere Verhältniszahlen, Rückwärts-Frage („Der Kleinste bekommt 120 €. Wie viel ist es insgesamt?“) oder streichen. |
| VT1B-093 | B | `form zwei_wege` ist ein Etikett: Gefragt ist nur die Fläche, die Kinder brauchen weder Annas noch Bens Weg. Rechnen nach Schema 8 · 5 : 2. | Frage so ändern, dass Bens Weg gebraucht wird („Welche Fläche muss Ben von 55 cm² abziehen?“ → 35). |
| VT1B-096 | B | Formel einsetzen und mit Preis malnehmen: genau die Bauart, die der Auftrag als „Rechnen“ verbietet (Sachaufgabe, die nur eine Formel einsetzt). `typ transfer` ist Etikett. | Ersetzen durch eine Modellierungsaufgabe (z. B. unregelmäßiges Grundstück zerlegen) oder als Rechenaufgabe führen. |
| VT1B-099 | B | Test: Höhe = Fläche : Grundseite (48 : 8) ist Rechnen; der Verstehenskern liegt im Ablenker (Winkel fehlt/schräge Seite). Die richtige Möglichkeit hat die meisten Wörter, aber nicht die meisten Zeichen. Die Denkfigur „Fläche durch Grundseite“ steht in sechs von sieben Aufgaben des Lernziels. Nicht die schwierigste (101, 103 verlangen mehr). | Test: 105 oder 103; 099 als Korrektur. |
| VT1B-103 | B | Mehrdeutig formuliert: Ein Parallelogramm hat zwei Paare paralleler Seiten. „Eine der beiden parallelen Seiten ist 300 m lang … Abstand der beiden parallelen Seiten“ meint stillschweigend das Paar mit der 300-m-Seite. Dazu Umrechnung ha → m² (Schema). | „Eine Seite des Parallelogramms ist 300 m lang. Wie weit ist sie von der gegenüberliegenden Seite entfernt?“ |
| VT1B-107 | B | `zwei_wege` ist ein Etikett (gefragt ist nur die Fläche). Zwei Bestandsaufgaben `rollend-8/abbildungen.determinanten2` K7-V132 haben dasselbe Fünfeck mit vier gleichen Ecken (A(0; 0), B(8; 0), D(4; 8), E(0; 5) und C(10; 5) statt C(8; 5)). Zerlegen/Ergänzen zum dritten Mal im Lernziel. | Andere Ecken; Frage zu Bens Weg („Wie groß ist jedes der beiden abgezogenen Dreiecke?“). |
| VT1B-110 | B | Formel einsetzen (30 − 2,25) mal 40: Sachaufgabe nach Schema; `transfer/anwenden` Etikett. | Streichen oder Modellierung verlangen (Parkett in Paketen zu 1,2 m², Verschnitt – zu schwer). |
| VT1B-116 | B | Doppelung: Bestand `messen.flaechen_vielecke` verstehen Stufe 2 „Ein Rechteck (5 cm · 4 cm) wird zu einem Parallelogramm schief gedrückt; … die Höhe ist dann nur noch 1 cm. Um wie viel cm² ist die Fläche kleiner geworden?“ – gleiche Figur und Denkfigur, hier nur in Prozent. | Andere Figur (Quadrat → Raute) oder andere Frage (Umfang bleibt, Fläche ändert sich: „Kann der Umfang größer, die Fläche kleiner werden?“). |
| VT1B-117 | B | Doppelung: Bestand `bruch.prozent` Bonus „Ein Rechteck wird um 20 % länger und um 20 % schmaler. Um wie viel Prozent … Fläche kleiner?“ und `bruch.prozent_grundwert`; Denkfigur steht auch in 113 und 118. | Andere Figur/Operation (z. B. Länge +20 %, Breite −20 %: kleiner oder größer begründen). |
| VT1B-050 | B | Test ist die einfachste Idee des Lernziels (Muster fortsetzen); der Bestand hat sie als Fehler-Detektiv (`rollend-11/terme.potenzgesetze_ganzzahlig` S3-V052: „Kim setzt das Muster der Zweierpotenzen nach rechts fort“) schon in der Übung. Schwerer sind 054, 056. Dazu Lehrplanfrage (negative Exponenten, siehe Abschnitt Lehrplan). | Als Korrektur verwenden; Test: 056 oder 054. |
| VT1B-051 | B | Doppelung: Bestandsübung `terme.potenzgesetze` „Schreibe 1/36 als Potenz mit der Basis 6. Wie heißt der Exponent?“ – dieselbe Gleichung in umgekehrter Frage. Rechnen (x² = 36). | Andere Zahlen und andere Frage (z. B. „Für welche x gilt x⁻² > x⁻³?“) oder streichen. |
| VT1B-055 | B | Die richtige Möglichkeit ist die einzige, in der die Exponenten aufsteigend stehen (−3, −2, −1, 0): Mustererkennung ohne Rechnen. Doppelung: Bestandsübung `terme.potenzgesetze` „Welche der Zahlen 2⁻¹, 2⁰, 2⁻² und (−2)⁻¹ ist am kleinsten?“. | Möglichkeiten so mischen, dass keine nach Exponent geordnet ist; mit zwei Basen (2⁻³ gegen 3⁻² gegen 10⁻¹). |
| VT1B-057 | B | Test ist der leichteste Fehler-Detektiv des Lernziels („Basis mal Exponent“ ist die Standardfehlvorstellung, im Bestand als „2⁵ = 2 · 5“-Bauart in `zahlen.potenzen_basis`, als „10⁶ = 10 · 6“ in `rollend-8/zahlen.potenzen_zehner` K7-V027 und als „5⁻² = −25“ in `terme.potenzgesetze` vorhanden). | Test: 058 oder eine Aufgabe mit zwei Fehlvorstellungen; 057 als Korrektur. |
| VT1B-060 | B | Doppelung: Bestandsübung `terme.potenzgesetze` „In einem Datenblatt steht: Dicke 10⁻³ m. Ein Kind meint, das sei eine negative Dicke. Wie viele Millimeter sind 10⁻³ m wirklich?“ – derselbe Aufhänger, die Frage nur auf Nanometer verlängert. Umrechnung = Schema. | Anderen Aufhänger und eine echte Fehlerfrage („Welcher Satz des Kindes ist falsch und warum?“). |
| VT1B-061 | B | Ablenker sind arithmetisch offensichtlich falsch („4 · 2 = 6“, „2/8 = 1/8“, „gleiche Brüche nicht addieren“); wer Zeilen 2–4 kurz nachrechnet, findet Zeile 1 durch Ausschluss. Die richtige Möglichkeit hat die meisten Wörter. Gleiche Fehlvorstellung wie 057 (Basis · Exponent). | Ablenker mit echten Fehlvorstellungen (Zeile 2: Kehrwert falsch, Zeile 3: Brüche addiert 1/16 + 1/16 = 2/32); andere Fehlerart als 057. |
| VT1B-062 | B | Der Aufgabentext sagt schon „warum 5⁰ = 1 gilt“; die Möglichkeiten 0, 1 und 3 behaupten 5⁰ = 0, 5 und −1, widersprechen also dem Text. Ein Kind wählt die einzige mit 1 ohne Verständnis. Dazu hat 062 dieselbe Denkfigur wie der Test 050 (Muster nach rechts teilen). | Frage ohne Ergebnis: „Welche Begründung für den Wert von 5⁰ ist richtig?“ mit Ablenkern, die auf 1 führen, aber falsch begründen („weil 5 · 0 = 0 und 0 + 1 = 1“). |
| VT1B-063 | B | Der Text verrät, dass a ≠ 2 ist („schreibt a = 2“). Im Kern Rechnen: 1/25 als 5⁻² schreiben. Die Bestandsübungen enthalten „Schreibe 1/8 als Potenz mit der Basis 2“ und „5⁻² = −25“. Das Zeichen „5ᵃ“ (hochgestelltes a, U+1D43) wird in manchen Schriften nicht dargestellt. | „Welche Zahl ist a in 5ᵃ = 1/25?“ ohne Kind; Schreibweise „5^a“ oder Lücken mit Kästchen. |
| VT1B-065 | B | Rechnen nach Schema (Ziffern zählen) und Doppelung: Bestand `rollend-8/zahlen.potenzen_zehner` K7-V028 „Die Zahl 62 000 soll als 6,2 · 10 hoch ① geschrieben werden“ – gleicher Vorfaktor 6,2, gleiche Ziffernfolge, nur 1 000-mal größer. Auch die Idee „Anzahl der Ziffern“ steht in 067 und 068. | Streichen oder durch „Warum braucht 0,62 · 10⁸ keinen anderen Wert als 6,2 · 10⁷?“ ersetzen. |
| VT1B-066 | B | Doppelung: `rollend-8/zahlen.potenzen_zehner` K7-V029 „Welche Schreibweise von 7 300 000 ist die wissenschaftliche? 73 · 10⁵ / 7,3 · 10⁶ / 0,73 · 10⁷ / 7,3 · 10⁵“ und `rollend-5` K5A-V095 – gleiche Form, andere Zahl. Die richtige Möglichkeit ist die, die die Definition erfüllt (Rechnen nach Regel). | Streichen oder durch „Welche Zahl hat die wissenschaftliche Schreibweise 3,85 · 10⁻³?“ mit Ablenkern wie 38,5 · 10⁻⁴ (Wert gleich, Form falsch) ersetzen. |
| VT1B-067 | B | Rechnen nach Schema („Ziffern = Exponent + 1“); dritte Aufgabe zur Ziffernzahl neben 065 und 068. | Streichen. |
| VT1B-068 | B | Doppelung mit der Bestandsübung `rollend-12/zahlen.potenzen_basis` R5-V086 („Licht legt in einer Sekunde etwa 3 · 10⁵ Kilometer zurück“); Multiplikation 3 · 10⁵ · 3,2 · 10⁷ nutzt Potenzgesetze (Bestand: Klasse 7); Ziffern zählen zum dritten Mal. | Anderer Sachverhalt; Frage nach Größenordnung („Welche Zehnerpotenz liegt am nächsten?“) statt Ziffernzahl. |
| VT1B-070 | B | Fehlbilder vertauscht: 530 000 hat 4 Nullen am Ende; Antwort 4 trägt die Beschreibung „Nullen am Ende abzüglich 1“, Antwort 3 die Beschreibung „nur die Nullen am Ende gezählt“. Rechnen nach Schema. | Beschreibungen tauschen (4 = Nullen am Ende gezählt, 3 = Nullen minus 1). |
| VT1B-071 | B | Test ist Wissensabruf (10⁻³ = 0,001); leichteste Aufgabe des Lernziels, die richtige Möglichkeit ist die einzige „Dezimalzahl 0,001“. Das Stellenzählen steht in 071, 072, 073 und 077 (vier Mal). | Test: 075 oder 076; Deutungsaufgabe mit einem Ablenker, der wie 0,001 aussieht (0,0001). |
| VT1B-073 | B | Doppelung: Bestandsübung `zahlen.potenzen_zehner` „Schreibe 10⁻⁶ als Dezimalzahl. Wie viele Nullen stehen nach dem Komma vor der 1?“ (und Sicherung mit 10⁻³): dieselbe zweite Lücke. Schema. | Streichen oder auf Bruch/Dezimal wechseln mit zwei Gleichungen („10⁻⁵ gegen 5 · 10⁻⁶“). |
| VT1B-075 | B | Doppelung mit `terme.potenzgesetze_ganzzahlig` (Übung „Ein Staubkorn ist 10⁻⁴ m breit. Wie viele Staubkörner passen auf 10⁻¹ m?“) und `rollend-7` K8-V123 („Ein Haar ist 10⁻⁴ m dick. Eine Zelle ist 10⁻⁶ m breit“) – gleiche Denkfigur. Quotient von Zehnerpotenzen ist Potenzgesetz-Stoff der Klasse 7/8 (Bestand). Sachlich schief: Viren sind rund 10⁻⁷ m lang, nicht 10⁻⁹ m; „Bakterie“ → „Bakterium“. | Streichen oder Kontext ändern; Größe „Atom 10⁻¹⁰ m / Zelle 10⁻⁵ m“ mit richtigen Werten. |
| VT1B-078 | B | Test ist Alltagswissen („1 mm = 1000 µm“) und leichter als 082–084. Die richtige Möglichkeit ist die einzige mit den Potenzen 10⁻³/10⁻⁶ (Standardformulierung des Lernziels). | Test: 084 (mit schwierigerem Ordnen) oder 083; 078 als Korrektur. |
| VT1B-079 | B | Rechnen nach Schema (Umrechnung mit Zehnerpotenzen), wie der Autor selbst nennt. | Streichen oder in Fehler-Detektiv verwandeln. |
| VT1B-080 | B | Rechnen nach Schema; Fehlbild 25 beschreibt „das Komma nur um eine Stelle verschoben“ – 0,25 → 25 sind zwei Stellen (gemeint: eine Stelle zu wenig). | Streichen; Text „eine Stelle zu wenig verschoben“. |
| VT1B-081 | B | Rechnen nach Schema; `typ umkehr` ist ein Etikett (Umrechnung mit unbekanntem Faktor). | Streichen. |
| VT1B-082 | B | Rechnen nach Schema (3 000 : 5); `typ transfer` Etikett, das Modell ist vorgegeben. | Streichen oder echte Modellierung („Wie viele Zellen in einem Kubikmillimeter?“ – Klasse 6 zu schwer, also eher streichen). |
| VT1B-084 | B | Ohne Umrechnen lösbar: Es genügt die Rangfolge nm < µm < mm und innerhalb mm 0,01 < 2 – nur die richtige Möglichkeit hält diese Regel ein. Fehlbild 2 („0,01 mm … vor 2 mm eingeordnet“) widerspricht der Möglichkeit (dort steht 0,01 mm hinter 2 mm). | Werte so wählen, dass die Einheitenreihenfolge täuscht (z. B. 0,001 mm = 1 µm gegen 5 µm); Fehlbild 2 korrigieren. |
| VT1B-085 | B | Test ist leicht (0,002 gegen 0,0008). Möglichkeit 1 („−4 ist kleiner als −3 und kleiner heißt kleiner Nenner“) ist unverständlich, und das Fehlbild („kleinerer Exponent gibt kleinere Zehnerpotenz“) passt nicht zu ihr; Möglichkeit 2 („8 · 4 = 2 · 3“) ist falsch gerechnet, eine Fehlvorstellung ist das nicht. Die richtige Möglichkeit hat die meisten Wörter. Gleiche Denkfigur wie die Sicherung 090 („nur Vorfaktoren vergleichen“). | Test: 087 oder 089; 085 mit sauberen Ablenkern („Der kleinere Exponent gibt die kleinere Zahl, also 8 · 10⁻⁴“). |
| VT1B-086 | B | Rechnen nach Schema (6 : 3 und 10⁷⁻⁴); der Lösungsweg nutzt das Potenzgesetz „gleiche Basis dividieren“, das die Bestandsdatei als Klasse-7-Stoff führt; `darstellung/bruecke` Etikett. | Ohne Potenzgesetz stellen („8 · 10⁷ Ziegel auf 4 · 10⁴ Lkw“) oder streichen. |
| VT1B-089 | B | Doppelung: Bestand `terme.potenzgesetze_natuerlich` Übung „Eine Festplatte fasst 8 · 10¹² Byte, ein Film braucht 4 · 10⁹ Byte. Wie viele Filme passen auf die Festplatte?“ – gleiche Zahlen 8/4 und gleicher Aufbau. Die Masse der Sonne ist 2 · 10³⁰ kg, die Angabe 4 · 10³⁰ ist falsch (Realitätsbezug). | Anderen Aufhänger mit erfundenen Größen; nicht als reale Angabe darstellen. |
| VT1B-005 | C | Die Fehlbilder sind keine Fehlvorstellungen (bei verneinter Frage beschreiben sie nur „gesucht ist die Ausnahme“). Die richtige Möglichkeit „14 % der Kinder“ ist die einzige, die die Zahl 14 aus dem Text unverändert übernimmt; wer nur nach dem „Ausreißer“ sucht, findet sie ohne Rechnung. | Ausnahme so wählen, dass sie nicht die Textzahl wiederholt (z. B. „0,14 aller Kinder“ oder „14 von 100 Kindern“) und im Fehlbild die echte Vorstellung benennen (14 aus dem Text als Prozentzahl gelesen). |
| VT1B-006 | C | Fehler ist in Stufe 3 offensichtlich (das Ergebnis 125 % ist nach Zeile 3 ein Warnzeichen, der Lösungsweg nennt es selbst). Eher Stufe 2. | Stufe 2 eintragen oder Zeile 1 und 2 so anlegen, dass der Fehler nicht am Ergebnis zu sehen ist. |
| VT1B-012 | C | Faktorschreibweise („mit dem Faktor 0,92 malnehmen“) ist laut Bestandsdatei Stoff von `bruch.prozent_grundwert` (Klasse 7). Sachlich eindeutig; ein gutes Verstehens-Item. | Lehrplanfrage klären; wenn Klasse 6 gewünscht: „Man zahlt nur noch 92 % des Preises“ statt „Faktor“. |
| VT1B-013 | C | Form `zwei_wege` ist nur formal; es gibt keinen zweiten Zugang, nur zwei Angebote. Die Struktur „Laden A/Laden B, wo billiger“ ist Bestandsform. | Als Rechnen belassen oder Frage zuspitzen („Ab welchem Listenpreis von B wäre B teurer?“). |
| VT1B-015 | C | Gute Verstehens-Aufgabe, aber leichter als 019–021; als Test nicht die schwerste. Denkfigur „um x % mehr / auf x %“ hat auch 016 und 017. | Test-Rolle an 021 (Rosinen) oder 019 geben, 015 als Korrektur. |
| VT1B-019 | C | Anteil vom Anteil ist gut; im Bestand gibt es die Idee in Bruchform (`bruch.rechnen` sach Bonus 3/5, 1/3, 1/2) und in Prozent (Mädchen/Jungen-Chor). Kein A/B. | — |
| VT1B-021 | C | Sehr schwere Mischungsaufgabe („Rosinenaufgabe“); in Klasse 6 vermutlich über dem Lehrplan (vermehrter Grundwert); 4–5 Minuten. Rechnerisch eindeutig. | Als Sicherung mit Stufe 3 beibehalten, aber Lehrplanfrage klären. |
| VT1B-022 | C | Die richtige Möglichkeit ist die einzige, die weder „alle“, „keine“ noch „nur x = 2“ sagt; gute Aufgabe, aber Auswahl nach Ausschlussprinzip möglich. | Eine vierte Möglichkeit „L = ℚ \ {2} für Jan, aber auch x = 1 …“ oder Möglichkeit mit zwei Teilaussagen statt reiner Mengen. |
| VT1B-023 | C | `typ darstellung`/`form`-Etikett ohne Darstellungswechsel (Definitionsmenge bestimmen und abzählen). Die Idee „dritter Nenner bringt nichts Neues“ ist ein kleines Verstehen. | Typ ändern oder Frage zu „Warum genügt x ≠ 3 und x ≠ −3?“ wenden. |
| VT1B-024 | C | Nah an `rollend-7/gleichungen.bruch` K8-V074 („6/(x + a) = 2/(x − 1) hat die Lösung x = 3. Wie groß ist a?“) und an der Bestandsübung „Welche Gleichung hat die Definitionsmenge ℚ \ {−3; 3}?“. Die Aufgabe selbst ist eindeutig. | Hinweis. |
| VT1B-028 | C | Die Möglichkeiten 0 und 1 haben dieselbe Gleichung, nur die Menge unterscheidet sich: die richtige gehört zum Zwillingspaar. Sachkontext „x Kinder“ lässt D = ℚ \ {−3; 0} streng genommen nur für die Gleichung, nicht für die Sache zu; im Text ist das eindeutig („Zahlen für x ausgeschlossen“). | Hinweis. |
| VT1B-033 | C | Die richtige Möglichkeit ist die ausführlichste („… ; über Kreuz ist eine Abkürzung dafür“). 18 Wörter gegen 15–23, kein klarer Hinweis. | Hinweis. |
| VT1B-035 | C | Sehr gute Verstehens-Aufgabe (Fallunterscheidung k = 3 und k = 0), ob eine Gleichung mit Parameter und „wie viele k“ im Lehrplan M8 4 steht, konnte ich nicht belegen. Mehr als 4 Minuten. Fehlbild 3 („Randwert k = 6 mitgezählt“) ist eine Konstruktion, keine typische Fehlvorstellung. | Als Test erwägen; Zeit prüfen. |
| VT1B-040 | C | Nahe an der Bestandsübung „Welche Gleichung liefert beim Rechnen x = 4, obwohl 4 nicht zu D gehört?“ (umgekehrte Richtung). Selbst eindeutig. | Hinweis. |
| VT1B-042 | C | `typ parameter`/`idee was_waere_wenn` stimmt nicht (kein Parameter, sondern eine Identität). Sehr gute Aufgabe, anspruchsvoller als der Test 036. | Etikett korrigieren; als Test erwägen. |
| VT1B-049 | C | Anspruchsvollste Aufgabe des Lernziels, aber nur Sicherung Stufe 3; die richtige Lösung braucht eine lineare Gleichung mit Parameter k. Gut. 4+ Minuten. | Als Test erwägen. |
| VT1B-092 | C | Test gut; ohne Bild dichter Text („Parallele zur Strecke AB“, Spitze „senkrecht über der Mitte“, D „7 cm rechts von B auf der Parallelen“). Eindeutig, aber ein Kind braucht Papier. | Koordinaten angeben: A(0; 0), B(10; 0), C(5; 4), D(17; 4). |
| VT1B-095 | C | Formelerkennung, Stufe 2; die richtige Möglichkeit ist die einzige mit allen drei Maßen. | Hinweis. |
| VT1B-100 | C | Nah an der Bestandsübung `gleichungen.reinquadratisch` („Ein Rechteck ist doppelt so lang wie breit und hat 98 cm² Flächeninhalt“): gleiche Zahl 98, gleiche Idee; für Klasse 6 das Quadrat als Zahl 196 = 14 · 14 erkennen. | Andere Fläche und Verhältnis. |
| VT1B-101 | C | Formel umstellen (Schema), aber das ist das Lernziel `rueckwaerts`; Stufe 2 ok. | Hinweis. |
| VT1B-102 | C | Formel-Abruf in Auswahlform; die richtige Möglichkeit ist die einzige mit „: 2“ und „·“. | Hinweis. |
| VT1B-104 | C | Gut; Fehlbild „486“ ist offensichtlich, daher leicht. | Hinweis. |
| VT1B-106 | C | Test gut, aber leichter als 107/112; Annas Zerlegung steht nur in der richtigen Möglichkeit („10 · 5 + 6 · 3“), nicht im Text (jede Zerlegung ergibt 68, harmlos). Zerlegen/Ergänzen kommt in 106, 107 und 109 vor. | Hinweis. |
| VT1B-108 | C | Schema (Rechteckfläche minus Rest durch Länge), aber echte Umkehrung. | Hinweis. |
| VT1B-109 | C | Verneinte Frage („falsch“) eindeutig; die falsche Rechnung ist das Zwillingspaar der richtigen „9 · 7 − 3 · 2“ (nur 5 statt 2): Wer die Zahlen des Textes vergleicht, findet sie ohne Figur. | Zwei falsche Rechnungen aus verschiedenen Zerlegungen (nur eine korrekt). |
| VT1B-112 | C | Koordinaten → Trapezfläche, Schema; trägt wenig zur Idee „Formeln erklären“ bei. Gauß-Fläche 18 bestätigt. | Hinweis. |
| VT1B-113 | C | Test gut; die richtige Möglichkeit ist die einzige „multiplizieren“; leichter als 117 und 116. | Hinweis. |
| VT1B-114 | C | Trivial (60 : 24), `typ umkehr`; die Proportionalität wird gebraucht, aber nicht geprüft. | Hinweis. |
| VT1B-118 | C | Klassiker (Quadrat, Seite verdoppeln); Stufe 2. | Stufe 2 eintragen. |
| VT1B-119 | C | Gut, Sollantwort 1; trifft den Leitgedanken („Zwei gleiche Dreiecke ergeben ein Parallelogramm“) am besten. | Hinweis. |
| VT1B-052 | C | Zwei Schritte, aber Schema (1/625 auf Zehntausendstel erweitern). Wissen zum Lernziel ok. | Hinweis. |
| VT1B-054 | C | Lösbar ohne negative Exponenten (dreimal halbieren); die Verknüpfung 2⁻³ steht nur im Lösungsweg. | Frage zu „Welcher Exponent …?“ wenden, damit die Potenzschreibweise nötig wird. |
| VT1B-058 | C | Gut; Möglichkeit 3 ist als einzige wahr in beiden Teilen. Kein Befund außer: Ablenker 0 und 2 sind keine Fehlvorstellungen von Kindern der Jahrgangsstufe 6. | Hinweis. |
| VT1B-059 | C | Trivial (Stufe 2): ein Gegenbeispiel für „negativer Exponent ⇒ negativ“; `typ umkehr`. | Hinweis. |
| VT1B-064 | C | Gut. Form und Fehler ähnlich zu Bestand-Fehler-Detektiven `rollend-8/zahlen.potenzen_zehner` K7-V033/V036 (andere Fehler). | Hinweis. |
| VT1B-069 | C | Der `idee`-Eintrag „groessenordnung_abschaetzen“ passt nicht (es geht um die Bedingung 1 ≤ a < 10, wie in 064 und 066). Die richtige Möglichkeit nennt als einzige „Vorfaktor kleiner als 1“. | Idee-Beschriftung korrigieren. |
| VT1B-072 | C | Stellenzählen, Schema; echte Umkehr. Doppelt zu 071/073. | Hinweis. |
| VT1B-074 | C | Nahe an Bestand „0,0001 = 10ⁿ. Wie groß ist n?“; hier erweitert um Vergleich; ok. | Hinweis. |
| VT1B-076 | C | „Zehnmal so klein“ ist umgangssprachlich; eindeutig gemeint (÷ 10), aber Kinder lesen „zehnmal so klein“ manchmal als „um 10 kleiner“. | „Durch 10 geteilt“. |
| VT1B-077 | C | Stellenzählen, Schema in Auswahlform; sehr nah an der Bestandsübung „Welche Zahl ist gleich 10⁻⁴? −10 000 / 0,0001 / 0,00001 / −4“. | Hinweis. |
| VT1B-083 | C | Gut; Struktur wie Bestand K7-V033 (Tera). | Hinweis. |
| VT1B-088 | C | Gut (Darstellungswechsel mit einer Falle); 5 000 000 · 10⁻² braucht Geduld, aber eindeutig. | Hinweis. |
| VT1B-091 | C | Die richtige Möglichkeit ist die einzige mit demselben Exponenten wie die Grenzen: Muster ohne Verständnis erkennbar. | Beispiel mit anderer Darstellung (35 · 10⁻⁴ liegt dazwischen). |

### Übergreifende Befunde (ohne einzelne Kennung)

| Nr. | Grad | Befund | Vorschlag |
|---|---|---|---|
| G1 | B | **Die Tests sind überwiegend Auswahl mit fertig formulierter Begründung**: 14 von 17 Test-Aufgaben sind „Welche Aussage ist richtig?“ (001, 015, 022, 029, 036, 043, 050, 071, 078, 085, 092, 099, 106, 113), nur 3 verlangen eigenes Ergebnis (008, 057, 064). Ratechance 25 %, dazu Erkennbarkeit an Formulierung (siehe 022, 036, 062, 078, 085). Eine echte Schulaufgabe verlangt mehr eigenes Rechnen/Begründen. | Mindestens die Hälfte der Tests als Lücken/Zahl mit zwei Teilantworten. |
| G2 | B | **`idee` ist nicht die Denkfigur.** Die README behauptet „mindestens 5 verschiedene Ideen, keine öfter als zweimal“; das gilt nur für die Beschriftung. In der Sache kommt in elf Lernzielen eine Denkfigur drei- bis sechsmal vor (Tabelle „Verstehen wirklich geprüft?“). | Je Lernziel zwei bis drei Aufgaben ersetzen. |
| G3 | B | **Nähe zum Bestand** (Abschnitt „Doppelungen“): mindestens 22 Aufgaben sind einer Bestandsaufgabe derselben Einheit nach Zahlen oder Denkfigur gleich. Das Werkzeug erkennt nur den Fragetext, nicht die Möglichkeiten und nicht die Idee. | Die dort genannten ersetzen. |
| G4 | B | **Lehrplan**: negative Exponenten in `terme.potenzgesetze` und `zahlen.potenzen_zehner` (Repo-intern widersprüchlich) und „Prozente mit verändertem Grundwert“ in `bruch.prozent` (die Bestandsdatei nennt es selbst Klasse-7-Stoff); siehe Abschnitt „Lehrplan“. | Entscheidung des Auftraggebers. |
| G5 | B | **Leitgedanke Flächen nur zu einem kleinen Teil geprüft** (Abschnitt „Flächen“). | 1–2 Aufgaben ersetzen. |
| G6 | C | `abgrenzung` ist je Lernziel dieselbe Textzeile bei allen 7 Aufgaben (z. B. alle Aufgaben `prozentsatz`: „Die Übungen berechnen einen Prozentsatz vorwärts …“), auch bei Aufgaben, bei denen der Satz nicht stimmt (002 berechnet einen Prozentwert). | Je Aufgabe ein eigener Satz. |
| G7 | C | Die Felder `fehlbild` und `regel_des_fehlbilds` sind überall leer, obwohl der Regel-Katalog passende Fehlbild-Kennungen kennt (Abschnitt „Regel-Kennungen“). | Nachtragen. |
| G8 | C | Länge/Platz: [F] Platz der richtigen Möglichkeit 10/9/10/9 (gleichmäßig); strikt die längste nur 025 (1 von 38, bestätigt), meiste Wörter 7 von 38; die kürzeste in 8. Aber: in 24 von 38 liegt die richtige Möglichkeit in der ähnlichsten Zweiergruppe der Möglichkeiten (Zufall 50 %), in 13 von 38 ist sie die „mittlere“ (Zufall 25 %). Schwacher Hinweis, nicht belegt (zu wenige Fälle). | Ablenker nicht als Zwillinge der richtigen bauen (001, 028, 109). |
| G9 | C | README: Tabellenkopf der Zahlen-Tabelle steht doppelt; Sonderfälle-Tabelle nennt bei Aufgaben mit Zwillings-Ablenkern „keine“ Besonderheit. | Redaktion. |

## Ohne Bild verständlich?

[F] Alle Geometrie-Aufgaben (092–119) haben kein `grafik`-Feld; Maße und Koordinaten stehen im Text. Alle Koordinaten sind nichtnegativ (Klasse-6-tauglich).

| Aufgabe | Urteil |
|---|---|
| 092 | [A] Alle Angaben vorhanden, aber dichter Text mit Parallelen, „senkrecht über der Mitte“, „7 cm rechts von B“. Ein Kind braucht Papier; Koordinaten wären sicherer. (C) |
| 103 | Mehrdeutig formuliert (zwei Paare paralleler Seiten): (B). |
| 106 | L-Figur eindeutig beschrieben (Rechteck 10 × 8, oben rechts 4 × 3 fehlt). Annas Zerlegung steht nur in einer Möglichkeit. Ok. |
| 107 | Fünfeck mit fünf Koordinaten und Rechteck für Ben vollständig; ok. |
| 109 | „Unten rechts fehlt“ eindeutig; die Zerlegungs-Möglichkeiten kann man nur mit Skizze prüfen (Papier erlaubt). Ok. |
| 111 | Haus-Fünfeck: „Dreieck darauf mit Grundseite 12“ meint die obere Rechteckseite; eindeutig. Ok. |
| 099, 115, 116, 119 | Parallelogramm/„schräge Seite“ ohne Bild verständlich; Existenz geprüft: Höhe 6 < Seite 7 (099), Höhe 4 < Seite 5 (116); Trapez/Parallelogramm in 115 nur durch Maße beschrieben, Fläche des Parallelogramms mit schräger Seite 4 cm ist < 24 cm² (Winkel nicht 90° wegen „schräg“). Ok. |
| 098, 093, 095, 112 | Koordinaten vollständig; Gauß-Fläche 20, 20, 20, 18 stimmt. Ok. |
| „Höhe außerhalb“ | Nur 092 (D rechts von B, stumpfwinklig) und ein Fehlbild in 092 verlangen ein Dreieck mit Höhe außerhalb. [A] Das Thema ist mit einer Aufgabe dünn; Koordinaten-Dreiecke 093–098 haben alle die Höhe innen oder auf der x-Achse. |

### Leitgedanke Flächen: „Formeln erklären können“

[A] Nur 119 („Zwei gleiche Dreiecke ergeben ein Parallelogramm“ steht im Lösungsweg) und teilweise 092/098 (Spitze verschieben, Höhe bleibt) prüfen das. Das Lernziel `parallelogramm`/`trapez` ist nicht gewählt (Vorschlag übernommen), das Trapez kommt nur in 101, 112 und 115 als Rechnung vor, nie als Herleitung. Es gibt keine Aufgabe: „Zwei gleiche Trapeze ergeben ein Parallelogramm mit der Grundseite a + c – warum ist die Trapezfläche (a + c) · h : 2?“ oder „Warum hat ein schief gedrücktes Rechteck dieselbe Fläche wie vorher, solange die Höhe …?“ (116 prüft das Gegenteil). Vorschlag: eine der Aufgaben 110 oder 096 (reine Formel) durch eine Herleitungsfrage ersetzen.

## Verstehen wirklich geprüft?

### Rechnen nach Schema (Kern: ein gelerntes Verfahren, `typ`/`form` Etikett)

[A] Klar Schema (B in der Tabelle): 002, 004, 010, 018, 030, 031, 044, 046, 047, 063, 065, 066, 067, 068, 070, 073, 079, 080, 081, 082, 086, 089, 093, 096, 110. Schema, aber als C geführt, weil das Lernziel selbst Rechnen ist oder eine kleine Falle steckt: 052, 054, 072, 077, 101, 102, 108, 112, 114. Das sind 25 klare + 9 Grenzfälle = 34 von 119 (29 %), bei den 16 Korrektur-/Sicherungs-Aufgaben der Stufe 2 mit `typ umkehr`/`darstellung` besonders hoch.

Zu den Selbsteinschätzungen des Autors: Umrechnungen (079–082) und Quotienten mit Zehnerpotenzen (075, 086, 089) bestätigt; „Wie viele Ziffern hat …“ (065, 067, 068) bestätigt, drei Mal im selben Lernziel; die einkleidung/mehrschritt-Aufgaben mit Form bruecke sind es überwiegend (003, 010, 016, 019?, 026, 030, 044, 047, 060): davon Schema 010, 030, 044, 047, 060, 016 (Rechnen), Verstehen steckt in 003, 019, 026 (nur halb).

### Typ `darstellung` / Form `bruecke`: Wechsel oder Etikett?

[A] 42 Aufgaben tragen `typ darstellung` oder `form bruecke`. **Echter Darstellungswechsel (≈ 15)**: 005 (Bruch/Dezimal/Prozent), 012 (Faktor ↔ Prozent), 017 (verdoppelt ↔ Prozent), 045 (Verhältnis ↔ Anteil), 066/073/077 (Schreibweisen), 088 (gleiche Zahl anders), 095 (Koordinaten ↔ Rechnung), 098 (Koordinaten ↔ Fläche), 102 (Text ↔ Gleichung), 109 (Figur ↔ Rechnung), 115 (Figur ↔ Maße), 052 (negativer Exponent ↔ Bruch ↔ Zehntausendstel), 004 (Winkel ↔ Prozent, routine). **Etikett (≈ 27)**: 003, 010, 011, 016, 019, 023, 025, 026, 028, 030, 031, 037, 038, 043, 044, 047, 055, 058, 060, 067, 074, 084, 086, 091, 101, 112, 116, 119 – hier wird gerechnet, geordnet oder verglichen, nicht die Darstellung gewechselt. Die Zählung „33 Aufgaben bruecke“ der README ist damit nur zu etwa 40 % echt.

### Je Lernziel nebeneinander: verschiedene Denkfiguren?

Regel der Runde: mindestens 5 wirklich verschiedene Denkfiguren, keine öfter als zweimal. [A] Eigene Zählung nach Sache, nicht nach `idee`:

| Lernziel | Aufgaben je Denkfigur | verschiedene | Urteil |
|---|---|---|---|
| prozentsatz | Grundwert wechseln 001; Prozentwert 002; Anteile vergleichen/Prozentpunkte 003; Winkel→% 004; Schreibweisen 005; Teil durch Ganzes (Fehler) 006; Anteil bei Zuzug 007 | 7 | ok (002 gehört nicht zum Lernziel) |
| rabatt_aufschlag | Rückrechnung 008, 009; Aufschlag+Raten 010; hintereinander 011; Faktor 012; zwei Angebote 013; Aufschlag-% 014 | 6 | ok; 008/009 gleich |
| verstehen (Prozent) | „um x % / auf x %“ 015, 016, 017; Rückrechnung 018; Anteil vom Anteil 019; Prozent gegen Anzahl 020; Rosinen 021 | 5 | knapp; 015–017 dreimal dieselbe Idee |
| definitionsmenge | D bestimmen 023, 025, 026, 027, 028 (fünfmal); Identität/L gegen D 022; Parameter 024 | 3 | **nicht erfüllt** |
| ueber_kreuz | Über kreuz anwenden 030, 031, 032, 034 (viermal); wann erlaubt 029; zwei Wege 033; Parameter/Fall 035 | 4 | **nicht erfüllt** |
| scheinloesung | Kandidat gegen D 036, 037, 038 (dreimal); Parameter für Kandidat 039, 040; Fehler 041; Identität 042 | 4 | **nicht erfüllt** |
| verhaeltnis | Dreisatz/Verhältnisgleichung 043, 044, 046, 047 (viermal); Anteil aus Verhältnis 045; Fehler Außen/Innen 048; Parameter 049 | 4 | **nicht erfüllt** |
| negativer_exponent (Potenzgesetze) | Muster/Halbieren 050, 054, 056 (dreimal); Umkehren 051, 053 (zweimal); Umrechnen 052; Ordnen 055 | 4 | **nicht erfüllt** |
| fehler_finden | Basis·Exponent 057, 061; „negativer Exponent ⇒ negativ“ 059, 060, 063; Vorzeichen/Klammer 058; Hoch 0 062 | 4 (und 059/060/063 dreimal) | **nicht erfüllt** |
| gross_wissenschaftlich | Bedingung 1 ≤ a < 10: 064, 066, 069 (dreimal); Ziffern zählen 065, 067, 068 (dreimal); Exponent suchen 070 | 3 | **nicht erfüllt** |
| negativer_exponent (Zehner) | Stellen zählen 071, 072, 073, 077 (viermal); Vergleich 074; Quotient 075; Division durch 10 076 | 4 | **nicht erfüllt** |
| vorsilben_klein | Umrechnen 079, 080, 081, 082 (viermal); Beziehung 078; Fehler 083; Ordnen 084 | 4 | **nicht erfüllt** |
| vergleichen_pruefen | Vorfaktoren/Exponenten vergleichen 085, 090 (Test und Sicherung gleich); Quotient 086, 089; kleinstes n 087; gleiche Zahl 088; zwischen 091 | 5 | ok, aber 085 und 090 wiederholen den Fehler |
| dreieck | Spitze verschieben 092, 098; zwei Wege 093; Formel A=g·h·½ 094, 095, 096; schräge Seite ≠ Höhe 097 (und Ablenker 092) | 4 | knapp |
| rueckwaerts | Höhe/Seite = Fläche : Grundseite 099, 100, 103, 104, 105 (fünfmal, 101 als Trapezvariante sechsmal); Gleichung ansetzen 102 | 2 | **nicht erfüllt** |
| zusammengesetzt | Zerlegen gegen Ergänzen 106, 107, 109 (dreimal); Umkehr 108; Sach 110; Fehler 111; Koordinaten 112 | 5 | knapp; 106/107/109 gleich |
| verstehen (Flächen) | Maße ändern, Fläche ändert sich um Faktor 113, 114, 117, 118 (fünfmal mit 116); Gleiche Fläche, andere Figur 115; Dreieck = ½ Parallelogramm 119 | 3 | **nicht erfüllt** |

Elf von siebzehn Lernzielen verfehlen die Regel (fett), vier weitere sind knapp. Das ist der Hauptgrund für „nach Korrektur“.

## Test-Aufgabe je Lernziel: wirklich die schwierigste?

[F] Alle 17 Test-Aufgaben sind Stufe 3, `ersetzt_test: true`, genau eine je Lernziel. [A] Schwierigkeit in Wirklichkeit:

| Lernziel | Test | Urteil | besserer Kandidat |
|---|---|---|---|
| prozentsatz | 001 | mittel; Doppelung | 007 |
| rabatt_aufschlag | 008 | zu leicht (Standardfehler), nicht die schwierigste | 013 oder 011 |
| verstehen | 015 | mittel; 019–021 schwerer | 021 oder 019 |
| definitionsmenge | 022 | ok, gute Aufgabe | — |
| ueber_kreuz | 029 | zu leicht (Regelabruf) | 035 oder 034 |
| scheinloesung | 036 | mittel; nicht die schwerste | 042 |
| verhaeltnis | 043 | zu leicht (Standardansatz) | 049 |
| negativer_exponent (Potenzgesetze) | 050 | zu leicht (Muster fortsetzen) | 056 oder 054 |
| fehler_finden | 057 | zu leicht (Basis·Exponent) | 058 oder 062 (nach Korrektur) |
| gross_wissenschaftlich | 064 | ok | 068 (zeitaufwendiger) |
| negativer_exponent (Zehner) | 071 | zu leicht (10⁻³ = 0,001) | 075 oder 076 |
| vorsilben_klein | 078 | zu leicht (Alltagswissen) | 084 (nach Korrektur) oder 083 |
| vergleichen_pruefen | 085 | zu leicht, Ablenker schwach | 087 oder 089 |
| dreieck | 092 | ok, gute Aufgabe | — |
| rueckwaerts | 099 | zu leicht (48 : 8) | 105 oder 103 |
| zusammengesetzt | 106 | leicht | 107 oder 112 |
| verstehen (Flächen) | 113 | ok, leichter als 116/117 | 117 |

Zeit: [A] In 2–4 Minuten mit Kopf und Papier machbar sind alle Tests; knapp darüber wären 035, 049, 021 (alle keine Tests).

## Lehrplan (Themenliste `inhalte/themenliste.json`, Lehrplan-Kopie des Repos; LehrplanPLUS selbst nicht geprüft)

[F] Zuordnung laut Themenliste: `bruch.prozent` M6 3, `gleichungen.bruch` M8 4, `terme.potenzgesetze` und `zahlen.potenzen_zehner` M6 1, `messen.flaechen_vielecke` M6 2. `lehrplan` beginnt in allen Aufgaben mit dem passenden Lernbereich.

| Frage | Befund |
|---|---|
| Negative Exponenten in M6 1? | [F] Die Themenliste führt `terme.potenzgesetze` (Klasse 6, M6 1) mit „Negative ganzzahlige Exponenten als Kehrbruch deuten“. [F] Zugleich steht in der Lehrplan-Kopie `terme.potenzgesetze_ganzzahlig` (Gym) als „neu“ in **Klasse 8** (M8 4: „Rechengesetze für Potenzen mit ganzzahligen Exponenten“), und `klassenleiter.md` führt „2 hoch −3 = ⅛“ als Klasse-8-Beispiel. [A] Der Widerspruch ist im Repo selbst; ich kann ihn ohne LehrplanPLUS nicht auflösen. Betroffen: 050–063 (14 Aufgaben) und negativer_exponent/vorsilben_klein/vergleichen_pruefen in `potenzen_zehner` (071–077, 078–091). **Entscheidung nötig**: Gehört der Lehrstoff zur Einheit in Klasse 6 (dann ok), oder sind die Aufgaben Klasse-8-Stoff in einer Klasse-6-Einheit? |
| Wissenschaftliche Schreibweise in M6 1? | [F] `zahlen.potenzen_zehner`: „M6 1.4 … und M5 3.1 (große Zahlen mit Zehnerpotenzen)“, Lehrplan-Kopie: Gym Klasse 6 „neu“. [A] Plausibel; Belegbarkeit wie oben. |
| Bruchgleichungen M8 4? | [F] `gleichungen.bruch` Klasse 8, M8 4. Definitionsmenge, Über-Kreuz, Scheinlösung gehören dazu. [A] **Gleichungen mit Parameter** (024, 032, 035, 039, 040, 049) und „wie viele k“ (035) sind vermutlich nicht Lehrplanstoff dieser Stufe; belegen kann ich es nicht. Mit binomischer Formel (042) ok (Klasse 7). |
| Prozente mit verändertem Grundwert | [F] Die Bestandsdatei `inhalte/themen/bruch.prozent.json` vermerkt in `offen`: „Lehrplan Kl. 6 verlangt nur einfache Prozentaufgaben (Rabatt, Zins). … vermehrter/verminderter Grundwert rückwärts (Preis nach Rabatt → alter Preis …) und Doppelrabatt als Rechenaufgabe – das ist Stoff von `bruch.prozent_grundwert` (Kl. 7)“. [F] Themenliste: `bruch.prozent_grundwert` Klasse 7, M7 3 „Prozentrechnung mit erhöhtem oder verringertem Grundwert“. Betroffen sind 008, 009, 011, 012, 016, 017, 018, 021 (und 015). [A] Obwohl die Bestandsdatei selbst solche Aufgaben noch als Übung Stufe 3 enthält, ist das ein offenes Lehrplan-Risiko (**B**). |
| Potenzgesetze in Lösungswegen | [A] 068, 075, 086, 089 rechnen Zehnerpotenzen malnehmen/teilen („Hochzahlen subtrahieren“); in der Lehrplan-Kopie `terme.potenzgesetze_natuerlich` Klasse 7 „neu“. Hinweis für die Lösungswege (wird nach dem Test gezeigt). |
| Prozentpunkte (003) | [A] Nur in der Bestandsübung belegt, nicht im Lehrplantext des Repos. |
| Flächen | [F] Alle Dreiecks-, Parallelogramm- und Trapezaufgaben passen zu M6 2.1. Koordinaten nur im ersten Quadranten. 094/100 brauchen eine Quadratzahl (g · g = 36/196): ok (Quadratzahlen bis 400, M5 3.1). |

## Lernziel-Auswahl (`auswahl.md`)

**bruch.prozent** (`prozentsatz`, `rabatt_aufschlag`, `verstehen` statt `prozentwert`, `grundwert`, `verstehen`, Muster RRVRVV). [A] Nicht vertretbar so, wie begründet: Die Begründung „Aufgaben waren bereits geschrieben“ ist keine fachliche. Das Muster hat zwei R am Anfang und zwei V am Ende (gegen E2 „abwechselnd“). Fachlich schwerer wiegt: `rabatt_aufschlag` und `verstehen` führen genau in den Stoff, den das Repo in Klasse 7 verortet (siehe Lehrplan). Der Vorschlag (V bei `prozentwert`, `grundwert`, `verstehen`; Muster RVRVRV) bleibt in Klasse 6; viele der geschriebenen Aufgaben (001, 003, 005–007, 019, 020) lassen sich auf `prozentwert`/`grundwert`/`verstehen` umwidmen. **Empfehlung: Vorschlag übernehmen.**

**gleichungen.bruch** (`verhaeltnis` statt `graphisch`). [A] Vertretbar: Ohne Bild bleibt `graphisch` nur mit zwei Funktionstermen eindeutig, das ist Rechnen. `verhaeltnis` gehört laut Themenliste zum Umfang („Verhältnisgleichungen lösen“). Der Preis: Vier der sieben Aufgaben sind Dreisatz-Schema (043, 044, 046, 047), und das Lernziel liegt nahe an Klasse-6/7-Proportionalität (`rr.verhaeltnis` Klasse 5–9). Das Muster VRVRVVR bleibt akzeptabel. Bedingung: Aufgaben 044, 046, 047 ersetzen (Schema).

## Auswahl-Aufgaben (38) und Fehler-Detektive (16)

### Auswahl

[F] Alle 38 haben 4 verschiedene Möglichkeiten, genau eine richtige, alle Rechenbehauptungen nachgerechnet (Mengen, Gleichungen, Flächen, Faktoren; jede Abweichung ist ein gewollter Ablenker). Verneinte Fragen (005 „anderen“, 109 „falsch“) sind eindeutig; 005: genau eine Möglichkeit ≠ 0,35; 109: genau eine falsche Rechnung von vier (Flächen 57, 57, 57, 48). Platz der richtigen: 10/9/10/9. Strikt die längste: nur 025 (Autor bestätigt). **Aber**: 062, 036, 037, 078, 061, 085, 084, 055, 091, 029, 022 sind an Formulierung oder Muster erkennbar (siehe Tabelle); Zwillings-Ablenker in 001, 028, 109.

### Fehler-Detektive

| Aufgabe | erster Fehler | wirklich falsch? | Urteil |
|---|---|---|---|
| VT1B-006 | Zeile 2 (Ganzes : Teil) | ja | ok |
| VT1B-008 | Zeile 2 (neuer Preis plus 25 %) | ja | ok |
| VT1B-020 | Zeile 3 (Schluss auf Anzahl) | falsch erst mit den Klassengrößen der Frage; als Allgemeinaussage „nicht gefolgert“ | vertretbar (B bei Doppelung) |
| VT1B-027 | Zeile 1 | falsche Folgerung, aber kann als „unvollständig“ gelesen werden | **Grenzfall, vertretbar**; Text schärfen (B) |
| VT1B-034 | Zeile 2 (4 · (x + 2) = 4x + 2) | ja | ok |
| VT1B-041 | Zeile 1 (nicht alle Glieder malgenommen) | ja | ok (Zeile 2 und 3 stimmen als Folge) |
| VT1B-048 | Zeile 2 (4 · x statt Außen mal Außen) | ja | ok |
| VT1B-057 | Zeile 1 | ja | ok, leicht |
| VT1B-061 | Zeile 1 | ja | ok; Ablenker schwach |
| VT1B-064 | Zeile 3 (Zehn vergessen) | ja | ok |
| VT1B-083 | Zeile 3 (10⁻⁶ : 10⁻⁹ = 10⁻³) | ja | ok |
| VT1B-090 | **Zeile 3**, gespeichert Zeile 2 | Zeile 2 ist **wahr** („3 > 2“) | **A** |
| VT1B-097 | Zeile 2 (schräge Seite) | ja | ok |
| VT1B-104 | Zeile 2 (h = A · g) | ja | ok |
| VT1B-111 | Zeile 2 (Halbieren vergessen) | ja | ok |
| VT1B-118 | Zeile 3 (Fläche nur verdoppelt) | ja | ok |

Die beiden Grenzfälle des Autors: **Definitionsmenge von x² − 9** (027) ist vertretbar, ein Kind kann aber „unvollständig“ lesen (B); „Zeile 1: x = 3, die −3 vergisst“ ist dieselbe Aufgabe. Zusätzlicher Grenzfall, den der Autor nicht nennt, ist 090 (A), und 020 (Zeile 3 wird erst durch die Frage falsch).

## Fehlbilder

[F] Zahl/Lücken: Alle `rechnung` ergeben die gespeicherte `antwort`, keine gleicht der Lösung, die Lücke ist ab 1 gezählt und passt. Auswahl: je falsche Möglichkeit ein Fehlbild. [A] Inhaltliche Mängel (Text führt nicht zur gespeicherten Zahl/Möglichkeit): **070** (Beschreibungen 3 und 4 vertauscht), **080** (Fehlbild 25 „um eine Stelle“), **084** Fehlbild für Möglichkeit 2 (Richtung widerspricht), **085** Fehlbild für Möglichkeit 1 (passt nicht zum Text), **025** Fehlbild für Möglichkeit 0 (4 nicht erklärt), **090** (A). Bei verneinten Fragen (005) beschreiben die Fehlbilder keine Fehlvorstellung. Sehr „konstruierte“ Fehlbilder: 035 (k = 6), 094/100 („2 doppelt gezählt“ nicht typisch).

## Regel-Kennungen (Vorschlag je Lernziel)

[F] 105 Aufgaben ohne `regel`, 14 (`ueber_kreuz`, `scheinloesung`) ohne Lernkarten-Regel; Katalog: `inhalte/mathe-profi/regeln-uebersicht/kennungen.json` (42 Kennungen) und die Lernkarten-Regeln des Werkzeugs. [A] Vorschlag (Lernkarten-Regel in Klammern, wo abweichend):

| Einheit / Lernziel | Vorschlag `regel` | Fehlbild-Kennungen aus dem Katalog | Bemerkung |
|---|---|---|---|
| bruch.prozent / prozentsatz, rabatt_aufschlag, verstehen | `id.verhaeltnisse.prozent` (Lernkarte hat sie) | `fb.prozent.falscher_grundwert` (001, 008, 009, 014, 018); `fb.prozent.prozente_addiert` (011, 019, 117, 020) | 005 besser `id.zahlen.schreibweisen` (Bruch/Dezimal/Prozent) |
| gleichungen.bruch / definitionsmenge | `id.algebra.erlaubte_zahlen` (Lernkarte hat sie) | `fb.erlaubte_zahlen.nullstelle_des_nenners_als_loesung` (022[2], 037[1], 041 Fehlbild 1) |  |
| gleichungen.bruch / ueber_kreuz | `rr.waage` (Gleichung als Waage; Lernkarte hat keine) | `fb.waage.nur_ein_summand` (034, 041) | Alternative `rr.ausmultiplizieren` für 034 |
| gleichungen.bruch / scheinloesung | `id.algebra.erlaubte_zahlen` | `fb.erlaubte_zahlen.nullstelle_des_nenners_als_loesung` (036, 037, 038, 040) | Lernkarte hat keine Regel |
| gleichungen.bruch / verhaeltnis | `rr.verhaeltnis` (Lernkarte hat sie) | `fb.verhaeltnis.addiert_statt_malgenommen` (044, 043[3]); `fb.verhaeltnis.falsche_richtung` (043[0,1], 044, 048) |  |
| terme.potenzgesetze / negativer_exponent | `rr.potenz` (statt Lernkarte `id.zahlen.hoch_zurueck`); für die Umkehr-Aufgaben 051, 053, 063 `id.zahlen.hoch_zurueck` passend | `fb.potenz.negative_hochzahl_als_minus` (050[0], 057, 059, 060, 063); `fb.potenz.basis_mal_hochzahl` (052, 053) | Lernkarten-Regel „Hoch und zurück“ (Potenz, Wurzel, Logarithmus) passt nur zu den Umkehr-Aufgaben |
| terme.potenzgesetze / fehler_finden | `rr.potenz`; 058 `rr.reihenfolge` | `fb.potenz.basis_mal_hochzahl` (057, 061); `fb.reihenfolge.minus_ins_quadrat` (058[1]); `fb.potenz.negative_hochzahl_als_minus` (059, 060) | 062 (5⁰) `rr.potenz` |
| zahlen.potenzen_zehner / gross_wissenschaftlich | `rr.stellenwert` (Komma verschieben) oder `id.zahlen.schreibweisen`; Lernkarte hat `rr.potenz` | — | 064, 065, 067, 068, 070 `rr.stellenwert`; 066, 069 `id.zahlen.schreibweisen` |
| zahlen.potenzen_zehner / negativer_exponent | `rr.potenz` (Lernkarte hat sie) | `fb.potenz.negative_hochzahl_als_minus` (071[1], 072 Fehlbild 7) | Alternativ `rr.stellenwert` für 072/073/077 |
| zahlen.potenzen_zehner / vorsilben_klein | `id.verhaeltnisse.groesse` (Einheit wechseln); Lernkarte hat `id.zahlen.buendeln` (Runden) | `fb.groesse.falsche_richtung` (079–082) | `id.zahlen.buendeln` passt nicht (Runden); `id.verhaeltnisse.groesse` ist laut Katalog nur Klasse 5 |
| zahlen.potenzen_zehner / vergleichen_pruefen | `id.zahlen.schreibweisen` (085, 088, 091); `rr.potenz` (086, 089) | — |  |
| messen.flaechen_vielecke / dreieck, zusammengesetzt, verstehen | `id.flaeche_raum.aus_dem_rechteck` (Lernkarte hat sie) | `fb.aus_dem_rechteck.halbieren_vergessen` (093 Fehlbild 40, 095[1], 096, 097 Fehlbild 60, 102[0], 107 Fehlbild 64, 111, 115[1]) | 113/117/118 alternativ `id.geometrie.aehnlich` (nur Klasse 8/9, daher nicht) |
| messen.flaechen_vielecke / rueckwaerts | `rr.gegenrechnung` (Rückwärts); Lernkarte hat `id.flaeche_raum.aus_dem_rechteck` | `fb.gegenrechnung.gleiche_rechnung` (104 Fehlbild 486, 103[300]) | 099–105 |

Alle Kennungen aus dem Katalog stammen aus dem Repo; Fehlbild-Kennungen habe ich nur aufgeführt, wenn die Katalogbeschreibung zur Aufgabe passt. Fehlt etwas Passendes (z. B. für „Scheinlösung nicht geprüft“ als eigene Fehlvorstellung), bleibt „ohne Regel“ besser als eine geratene Kennung.

## Doppelungen und Nähe zum Bestand

Vergleich von Hand (alle 17 Test-Aufgaben und alle Aufgaben mit auffälliger Ähnlichkeit) gegen `inhalte/themen/<Einheit>.json` und `rollend-*`; Rest per Skript (`--bestand`). [F] = im Repo gelesen.

| VT1B | Bestandsaufgabe (Datei, Nummer) | Gleichheit |
|---|---|---|
| 001 | `bruch.prozent` Übungen #201/#203 (Spendenlauf 40 → 50 und 50 → 40); `rollend-2/g8` G8-12 | gleiche Zahlen 40/50, gleiche Idee |
| 003 | `bruch.prozent` verstehen Üb. 3 („30 % auf 36 %: Prozentpunkte“) | gleiche Denkfigur |
| 009, 011, 008 | `bruch.prozent_grundwert` #84 („35 % Rabatt, 52 €“); `bruch.prozent` Bonus („erhöht um 25 %, dann 20 % Rabatt“) | gleiche Frage mit anderen Zahlen |
| 020 | `bruch.prozent` verstehen Üb. 3 („A: 50 % von 20 / B: 40 % von 30“) | gleiche Denkfigur |
| 024, 032 | `rollend-7/gleichungen.bruch` K8-V074 („6/(x + a) = 2/(x − 1) hat die Lösung x = 3, a?“) | gleicher Aufbau, 032 sogar gleiches x |
| 027 | `rollend-13/terme.bruchterme` R8-V032 („x² − 9; Aus x² = 9 folgt x = 3, nur x = 3 verboten“) | derselbe Denkfehler, dieselbe Gleichung x² − 9 |
| 040 | `gleichungen.bruch` #227 („Welche Gleichung liefert x = 4, obwohl 4 nicht zu D gehört?“) | gleiche Denkfigur, umgekehrt |
| 047 | `groessen.verhaeltnisse` #114 („Drei Geschwister, Verhältnis 2 : 3 : 4“) | gleiche Verhältniszahlen |
| 050, 061, 062 | `rollend-11/terme.potenzgesetze_ganzzahlig` S3-V052 (Zweierpotenzen nach rechts fortsetzen) | gleiche Idee wie der Test |
| 051 | `terme.potenzgesetze` #108 („1/36 als Potenz mit Basis 6“) | gleiche Gleichung, umgekehrte Frage |
| 055 | `terme.potenzgesetze` #53 („2⁻¹, 2⁰, 2⁻², (−2)⁻¹: kleinste“) | gleiche Basis, gleiche Denkfigur |
| 057 | `rollend-8/zahlen.potenzen_zehner` K7-V027 (10⁶ = 10 · 6); `terme.potenzgesetze` #90 (5⁻² = −25) | derselbe Denkfehler |
| 060 | `terme.potenzgesetze` #83 („Datenblatt, Dicke 10⁻³ m, negative Dicke“) | **gleicher Aufhänger**, Frage nur anders |
| 065 | `rollend-8/zahlen.potenzen_zehner` K7-V028 (62 000 = 6,2 · 10^①) | gleicher Vorfaktor und gleiche Ziffernfolge |
| 066 | `rollend-8` K7-V029 („wissenschaftliche Schreibweise von 7 300 000“) und `rollend-5` K5A-V095 | gleiche Form, andere Zahl |
| 068 | `rollend-12/zahlen.potenzen_basis` R5-V086 („Licht … 3 · 10⁵ Kilometer“) | gleicher Aufhänger |
| 073 | `zahlen.potenzen_zehner` #95/#108 („10⁻⁶/10⁻³ als Dezimalzahl: Nullen vor der 1“) | gleiche zweite Lücke |
| 075 | `terme.potenzgesetze_ganzzahlig` #46 (Staubkorn), `rollend-7` K8-V123 (Haar/Zelle) | gleiche Denkfigur (Längenverhältnis) |
| 089 | `terme.potenzgesetze_natuerlich` #131 („Festplatte 8 · 10¹² / Film 4 · 10⁹“) | gleiche Zahlen 8 und 4 |
| 100 | `gleichungen.reinquadratisch` #235 („Rechteck doppelt so lang wie breit, 98 cm²“) | gleiche Zahl 98, gleiche Idee |
| 107 | `rollend-8/abbildungen.determinanten2` K7-V132 (Fünfeck A(0; 0), B(8; 0), C(10; 5), D(4; 8), E(0; 5)) | vier von fünf Ecken gleich |
| 116 | `messen.flaechen_vielecke` verstehen Üb. („Rechteck 5 · 4 schief gedrückt, Höhe nur noch 1“) | gleiche Figur, gleiche Idee |
| 117 | `bruch.prozent` Bonus („Rechteck 20 % länger und 20 % schmaler“); `bruch.prozent_grundwert` faktor | gleiche Denkfigur |

[F] Das Werkzeug meldet keine dieser Nähen, weil es nur Fragetext und Zahlen ab drei Zahlen vergleicht. Die Test-Aufgaben 001, 008, 050, 057, 071, 078, 085, 099 haben jeweils eine gleiche oder gleichartige Bestands-Übung in derselben Etappe. Keine Aufgabe wiederholt eine andere Aufgabe der Runde (keine gleiche Sollantwort im Lernziel; Ausnahme siehe unten).

Innerhalb der Runde gleiche Sollantwort oder Antwort ablesbar: 036 und 037 (beide „L = { }“); 085 und 090 (gleiche Fehlvorstellung, 090 verrät den Test nach dem Test); 062 (Aufgabentext verrät das Ergebnis); 063 (Text verrät, dass a ≠ 2); 092 und 098 (gleiche Einsicht, 098 wird ohne Verständnis durch „gleiches y“ lösbar, wenn der Test 092 bekannt ist).

## Was ich NICHT prüfen konnte

- **LehrplanPLUS selbst** (kein Webzugriff erlaubt, im Repo nur Themenliste und eine Datenbank-Kopie). Insbesondere: negative Exponenten und wissenschaftliche Schreibweise in M6 1 gegen M8 4, Prozentpunkte, Gleichungen mit Parametern in M8 4.
- **App-Verhalten**: wie `luecken` mit negativen Zahlen (053, 072, 076, 083 Fehlbild, 090 Fehlbild) und Dezimalzahlen (010: 156,8; 114: 2,5) eingegeben und gewertet werden, und ob „5ᵃ“ (063) im Test sauber dargestellt wird.
- **Echte Kinder**: ob Kinder dieser Stufe die Texte (z. B. 092, 103) ohne Skizze verstehen; Zeiten sind geschätzt.
- **Sprache/Rechtschreibung** nur beiläufig (z. B. „Bakterie“ in 075).
- Doppelungsprüfung: Skript vergleicht 28 906 Bestandsaufgaben nur nach Wort-/Zahlenüberlappung; von Hand gelesen habe ich die Treffer und alle Tests. Weitere Doppelungen mit Aufgaben, die anders formuliert sind, sind möglich.
