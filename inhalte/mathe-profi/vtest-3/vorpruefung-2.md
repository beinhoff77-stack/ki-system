# Vorprüfung 2 – Runde vtest-3 (VT3), Stand f367a0af

Zweite, unabhängige Vorprüfung nach der Einarbeitung meiner ersten Vorprüfung (`vorpruefung.md`, Stand 5bdace7c). Geprüft: der Stand `origin/helfer-vtest-r3` (f367a0af), eingemischt in `vorpruefer-vt3`. Ich habe keine Aufgabe und keinen fremden Code verändert; neu sind nur dieser Bericht und `vorpruefung_rechnen_2.py`.

## Gesamturteil

**Nach kleiner Korrektur einspielbar. 0 A, 13 B, 17 C.** Deutlich besser als Runde 1 (dort 1 A, 36 B, 58 C).

- **Rechnerisch sauber.** Alle 126 Lösungen und die Wahrheit jeder der 54 × 4 Auswahl-Optionen sind unabhängig neu gerechnet: 0 Abweichungen. 351 Fehlbilder sind geprüft (Index, Lücke, Antwort ≠ richtig; bei 189 wurde die `rechnung` ausgewertet und stimmt mit der `antwort` überein).
- **Der A-Befund ist geschlossen** (VT3-067). Es gibt keinen neuen A-Befund.
- **Von meinen 36 B-Befunden sind 24 geschlossen, 7 teilweise, 4 nicht, einer war mein Irrtum** (VT3-006, siehe unten).
- **Drei Aufgaben sind jetzt wieder Bestandsdoppelungen: VT3-100, VT3-123 und das neue VT3-047.** Bei 123 geht das auf meinen eigenen Korrekturvorschlag zurück, den ich nicht gegen den Bestand geprüft hatte.
- **Die Auswahl-Statistik stimmt** (Platz 14/14/13/13, längste Option 14 von 54). Der feste Platz-Algorithmus erzeugt aber ein Muster, das ein Kind erkennen kann (B-9).
- **Vor dem Einspielen mindestens ändern:** 100, 123, 047, 044, 053, 122 und die Platzfolge. Die übrigen B-Befunde betreffen die Mischung der Denkfiguren und sind auch nach dem Einspielen behebbar.

## Zahlen

- **Änderungen gegenüber 5bdace7c:** 98 von 126 Aufgaben unterscheiden sich im Inhalt. Davon sind 83 inhaltlich geändert (Text, Optionen oder Lösung), 8 nur in der Optionsreihenfolge (013, 017, 028, 030, 054, 066, 078, 092), 5 nur in `idee` (006, 014, 015, 020, 069) und 2 nur in den Fehlbildern (075, 111). 28 Aufgaben sind unverändert (010, 011, 019, 022, 024, 027, 031, 032, 035, 040, 042, 043, 052, 058, 073, 077, 080, 083, 087, 091, 094, 098, 101, 106, 107, 108, 122, 126). Das stimmt mit den „etwa 85" des Autors überein. Ich habe alle 98 selbst gegengelesen und nicht seine Liste benutzt.
- **Skript:** `vorpruefung_rechnen_2.py` (128 Prüfungen, 0 Abweichungen; deckt alle 126 Kennungen). Es benutzt keine `loesung_rechnung` des Autors. Nachrechnen per Formel, Aufzählung oder Modell:
  - 060: alle vier Zahlen von 0 bis 20 mit Summe 40;
  - 088: Brüche mit Nenner 1, 2 und 4;
  - 103: alle Winkel von 1° bis 179°;
  - 118: alle ganzzahligen Dreierzerlegungen von 90°;
  - 120: alle Winkelpaare aus spitz und stumpf in ganzen Grad.
- **Werkzeug:** `python3 -I tools/vtest_pruefen.py --runde 3` meldet „OK – keine Fehler" und 4 Hinweise (010, 063, 073, 115). Die Behauptung des Autors, es seien Fehlalarme, stimmt: 50 · 30 · 40 = 60 000 cm³ in Zeile 1 von 010 ist richtig, „3x + 6 = 15" in Zeile 1 von 073 ist richtig, und „Runden" meint bei 063 und 115 Laufrunden bzw. eine runde Torte.
- **Auswahl:** 54 Aufgaben. Platz der richtigen Option: 14 / 14 / 13 / 13 (Index 0 bis 3). Die längste Option ist 14-mal richtig (26 %, Zufall 25 %). Rang der richtigen Option nach Länge (1 = längste): 14 / 20 / 15 / 5. Keine richtige Option ist um mehr als 30 % länger als der Durchschnitt der falschen.

## Befunde

### A (falsch oder mehrdeutig)

Keine.

### B (sollte vor dem Einspielen geändert werden)

| Nr. | Aufgabe | Befund | Korrekturvorschlag |
|---|---|---|---|
| B-1 | VT3-100 | **Bestandsdoppelung mit denselben Zahlen.** Bestand `themen/geometrie.winkel.json` (uebung): „Drei Geraden schneiden sich in einem Punkt. Zwei nebeneinanderliegende Winkel sind 50° und 70° …, der dritte Winkel daneben, der mit ihnen einen gestreckten Winkel bildet?" (60°). VT3-100 ist dieselbe Aufgabe, nur mit einem zusätzlichen Schritt „gegenüberliegender Winkel gleich groß". Die erste Fassung hatte ich schon als Doppelung gemeldet; die neue ist nicht weiter weg. | Andere Winkel (z. B. 40° und 75°) und andere Frage. Besser Denkfigur wechseln: „Drei Geraden durch einen Punkt, die sechs Winkel sind der Reihe nach α, β, γ, α, β, γ. Welche Summe α + β + γ?" (180°, Begründung) oder „Einer der sechs Winkel ist 100°. Wie viele der sechs sind spitz?" |
| B-2 | VT3-123 | **Bestandsdoppelung, und zwar durch meinen Vorschlag.** Bestand `rollend-4/ge3`: „Neben einem Winkel von 65° liegt an einer Geraden ein zweiter Winkel … Zeile 2: Ein gestreckter Winkel hat 90°. Zeile 3: 90° − 65° = …". VT3-123 hat dieselben 65° und denselben Fehler (Nebenwinkel zu 90° statt 180° ergänzt). In Runde 1 habe ich „Winkel mit 90° statt 180° ergänzen" als Alternative vorgeschlagen, ohne den Bestand daraufhin zu durchsuchen. Das war mein Fehler. | Anderen Fehler wählen, z. B. Scheitelwinkel mit Nebenwinkel verwechselt (Zeile 2: „γ liegt gegenüber α, also γ = 180° − α"). Das wäre dann aber VT3-101 sehr ähnlich. Alternativ „Wenn α spitz ist, ist der Nebenwinkel stumpf" mit dem Fehler „α = 90°-Sonderfall übersehen". Mindestens 65° ändern. |
| B-3 | VT3-047 | **Neue Bestandsdoppelung.** Bestand `themen/daten.darstellen.json` (uebung): „Ein Bild-Diagramm zeigt den 3-fachen Wert durch ein Bild, das 3-mal so hoch und 3-mal so breit ist. Wie viel Mal so groß ist die Bildfläche?" (9). VT3-047 („Umsatz verdreifacht, Quadrat mit verdreifachter Seite: wie viel Mal so groß ist die Fläche?") ist dieselbe Frage mit derselben Antwort, nur mit dem Quadrat statt des Bildes. Ersetzt die Aufgabe mit Achsenbeginn 60, die ich als Doppelung zu 043 gemeldet hatte. | Andere Wendung im Lernziel irrefuehrend, z. B. 3D-Säule/Würfel: „Ein Würfel stellt den doppelten Wert dar. Wie viel Mal so groß ist sein Volumen?" (8), oder umgekehrt: „Eine Fläche ist 16-mal so groß, wie viel Mal so groß ist der dargestellte Wert, wenn die Seite verlängert wurde?" |
| B-4 | VT3-044 | **Nicht geschlossen: weiterhin ohne Einsicht lösbar.** Der Text nennt die Marken 80 und 20 selbst und fragt „Wie viel Mal so groß ist der Wert der ersten Säule wie der Wert der zweiten?" Wer 80 : 20 = 4 rechnet, hat recht und muss die ungleiche Skala nicht bemerken. Der Zusatz „gleiche Abstände" ändert das nicht. | Die Säulen über ihre Lage angeben: „Die erste Säule reicht bis zur vierten Marke über 0, die zweite bis zur zweiten Marke (Marken 0, 10, 20, 40, 80 in gleichen Abständen). Wie viel Mal so groß ist der Wert der ersten?" (Antwort 40 : 10 = 4; die Säulenhöhe täuscht 2 : 1 vor). Dann ist die Skala zu verstehen. |
| B-5 | VT3-053 | **Antwort steht im Text.** „Zwei Gruppen haben denselben Mittelwert 8 … Mittelwert aller 30?" – 8. Die Zahl 8 kommt in der Aufgabe vor, der Gedanke (gleiche Mittelwerte ⇒ derselbe Gesamtmittelwert) ist mit Beispielzahlen und schon durch Raten lösbar. Der Autor bezweifelt das selbst. | Die Aufgabe so lassen, aber die Antwort nicht abgeben: Gruppe A (10 Personen, Mittelwert 8), Gruppe B (20 Personen, Mittelwert 11): Gesamtmittelwert 10. Oder Begründung: „Welcher Wert kann der Gesamtmittelwert nicht sein: 7 / 9 / 10 / 12?" (A 8, B 11). |
| B-6 | VT3-022, 023, 025 | **Dieselbe Denkfigur („Volumen ist proportional zur Höhe / Schicht") dreimal** im Lernziel messen.volumen/verstehen: 022 (3 m gegen 2,4 m hoch, 25 %), 023 (Höhe + 2 cm, Zuwachs unabhängig von der Höhe) und 025 (4 cm von 10 cm abschneiden, 60 %). Dazu ist der **Test 022 leichter als 027 und 028** (ein Verhältnis 3 : 2,4 gegen nicht ganz passende Päckchen bzw. Prozentfaktor 2,25): nicht die anspruchsvollste Aufgabe des Lernziels. | 025 durch eine andere Einsicht ersetzen, z. B. „Die Länge wird verdoppelt, die Breite halbiert: Volumen?" (gleich, Begründung); als Test den Packungsgedanken verwenden (heutige 027 als Test, 022 als Sicherung). |
| B-7 | VT3-078 (Test), 079, 080, 083 | graph_lesen: vier von sieben Aufgaben sind **„m und t aus Daten bestimmen"** (078 zwei Punkte, 079 Wertetabelle → f(0), 080 Fehler-Detektiv Achsenabschnitt, 083 beschriebene Steigung → Wert). Der Test 078 ist dabei die leichteste: Achsenabschnitt −3 steht fast da (A(0 \| −3)), Steigung (1 + 3) : 2 = 2; die falschen Optionen sind nur Vorzeichen-/Verwechslungsfehler. Das ist leichter als der Bestand (Klasse 8, Stufe 3 nur nominal). Nur 081 (parallel), 082 (nicht-linear) und 084 (Vorzeichen) sind echte Verstehensfiguren. | Test 078 ersetzen durch 082 oder 084 (Verstehen) bzw. durch eine Aussage über zwei Geraden, z. B. „Wo schneidet die Gerade durch A(1 \| 2) und B(3 \| 6) die y-Achse?" (0). 079 auf „Warum kann y = 2x + 3 nicht zur Tabelle gehören?" drehen. |
| B-8 | VT3-122 | **Antwort steht im Text.** „Sein Nebenwinkel wird um 30° kleiner … Wie groß war α?" – 30. Der Gedanke (Nebenwinkel schrumpft um α) ist gut, aber ein Kind kann die einzige Zahl der Aufgabe abgeben. Zu den Fehlbildern gehört „30 : 2 = 15", nicht aber „30" selbst. | Verdreifachen statt verdoppeln: „α wird verdreifacht, dadurch wird der Nebenwinkel um 40° kleiner" (α = 20°, Nebenwinkel 160° → 100°). |
| B-9 | Alle 54 Auswahl-Aufgaben | **Die feste Platzfolge ist eine Zahlenreihe.** Der Platz der richtigen Option ist in Kennungsreihenfolge `1 0 3 2 1 0 3 2 …` (53 von 53 Schritten sind „einen Platz früher", modulo 4). Wer in einem Lernziel zwei Auswahl-Aufgaben gelöst hat, kann die nächste erraten: graph_lesen 3, 2, 1, 0; sachzusammenhang 0, 3, 2, 1, 0; punkt_graph 3, 2, 1; saeulendiagramm 3, 2, 1. In einem Test mit einer Aufgabe je Lernziel ist die Folge weniger leicht zu erkennen (die fünf Test-Auswahlen stehen auf 1, 3, 0, 3, 2), in Übungsfolgen aber voll sichtbar. Die Verteilung 14/14/13/13 ist nur im Mittel gleichmäßig. | Platz zufällig, aber ausgeglichen vergeben: Bauskript mit festem Seed, je Block von vier Aufgaben eine zufällige Reihenfolge der Plätze 0 bis 3, nie zwei gleiche hintereinander, und prüfen, dass keine Folge aus drei „−1"-Schritten entsteht. Besser zusätzlich: App mischt zur Laufzeit (Fehlbild-Index mitführen). |
| B-10 | figuren (113–119) | Die Kategorien sind laut README 5, die **wirklichen Denkfiguren nur 4**: (a) Teile eines Winkels aus Gleichung/Verhältnis: 113 (x, x + 10, x + 20), 114 (1 : 3), 119 (zwei gleiche äußere Teile, mittlerer 20°); (b) **dieselbe Falle „Schnitte/Strahlen statt Stücke zählen" zweimal**: 115 (18 Stücke → 9 Schnitte) und 117 (5 Teile → 4 Strahlen); (c) Bruchteile verschiedener Winkel (116); (d) Extremaussage (118). Eine dieser Mehrfachfiguren genügt. | 117 ersetzen durch eine andere Figur, z. B. „Eine Uhr zeigt 4:00 Uhr; der Minutenzeiger wird auf 4:12 vorgestellt: wie viel ist der kleinere Winkel?" (gehört zur Uhr) oder ein Winkelsatz „Winkelhalbierende von zwei Nebenwinkeln stehen senkrecht" (Begründung). Oder 119 zusammen mit 113 mischen. |
| B-11 | sachzusammenhang (092–097) | Die Kategorien sind laut README 5, die **wirklichen Denkfiguren etwa 3**: „Anfangswert plus Änderung je Einheit" (Term aufstellen, lesen, prüfen, abändern) steht in 092, 094, 095, 096 und 097. Eigene Figuren sind nur 093 (nicht proportional) und 098 (Tarifvergleich). Aufgaben wie 097 (Term → Situation) und 096 (Zufluss verdoppelt) sind für Klasse 8 sehr leicht. | 097 ersetzen durch eine Einsicht mit Fallstrick, z. B. „Ein Tarif kostet 5 € + 2 € je Stunde; ein anderer 0 € + 3 € je Stunde. Für welche Dauer ist der erste günstiger?" (Vergleich, Gleichung); 096 auf „Welche Aussage stimmt: Verdoppelt sich der Zufluss, verdoppelt sich der Inhalt nach 4 Stunden?" drehen. |
| B-12 | quader (001–007) | **Vier von sieben Aufgaben sind „Kantenfaktoren multiplizieren sich"**: 001 (+50 %, −20 %, doppelt), 002 (alle Kanten halbiert), 003 (6-cm-Würfel in 2-cm-Würfel zerlegt: 3³) und 006 (Verhältnisse zweier Kanten, b³). Drei verschiedene Kategorienamen, ein Gedanke. 003 hatte ich in Runde 1 gemeldet; die neue Fassung bleibt bei Kantenfaktor 3. Nur 004, 005 und 007 sind eigene Figuren. Der Test 001 gehört zur Figur, die schon zweimal in den Korrekturen steht. | 003 oder 006 ersetzen, z. B. „Zwei Quader haben dieselbe Oberfläche. Müssen sie dasselbe Volumen haben?" (Gegenbeispiel) oder 003 zu „Wie ändert sich die Oberfläche, wenn alle Kanten verdoppelt werden?" (4-fach, Abgrenzung zum Volumen). |
| B-13 | mittel_rueckwaerts (057–063) | Fünf von sieben bleiben **„Summe = Mittelwert · Anzahl, Rest bestimmen"** (057, 058, 059, 062, 063); 060 (Begründung) und 061 sind anders. 061 ist formal `zwei_wege`, aber die Aufgabe nennt nur einen Weg („über die Abweichungen von 100") und fragt nach der Zahl 101; das Kind kann ohne den Weg einfach den Mittelwert ausrechnen. Meine Runde-1-Befunde zu 062 und 061 sind damit nur teilweise geschlossen. | 061: beide Wege in Optionen zur Wahl stellen („Welcher Weg ist bei Zahlen nahe 100 sicher?") oder die Frage nach der Summe der Abweichungen stellen (5). 063 zu „Welche Aussage über die drei gleichen Runden stimmt: sie sind höchstens 78 s und mindestens 65 s?" |

### C (Hinweise)

| Nr. | Aufgabe | Hinweis |
|---|---|---|
| C-1 | VT3-034 | Die richtige Option („mindestens 0 %, höchstens 100 %") ist die einzige, die immer wahr ist, aber auch die einzige ohne konkrete Zahl für 120 Würfe; die drei anderen sind scharfe Behauptungen. Ein Kind „nimmt die sichere Antwort". Besser eine Aussage mit Rechnung, z. B. „Bei 120 Würfen ist die relative Häufigkeit der Sechs ein Vielfaches von 1/120" (Begründung). |
| C-2 | VT3-065 | `idee` lautet noch „welcher Wert kommt bei x² − 4 nicht vor", die Aufgabe selbst ist x² − 9 (−9 ∈ W). Beschriftung nachziehen. |
| C-3 | VT3-074 | Zahlen 12, 1,5 und 30 stimmen mit der Bestands-Pflanze („h(t) = 12 + 1,5t, 30 cm Topf") überein, nur die Einkleidung ist neu. |
| C-4 | VT3-004, 003 | 004 benutzt 6 · 4 · 3 wie die Bestands-Schachtel „6 cm lang, 4 cm breit, 3 cm hoch" (dort Würfelzahl), 003 den 6-cm-Würfel des Bestands (Bohrloch). Nur die Zahlen. |
| C-5 | VT3-104, 121 | 35° (104) und 62° (121) kommen im Bestand vor (Summe der anderen drei Winkel; Diagonale im Rechteck). Nur die Zahlen. |
| C-6 | VT3-106, 112 | 112 (Uhr geht vor, 7,5°) ist mindestens so anspruchsvoll wie der Test 106 (Spiegelgedanke 12 − 7); als Sicherung mit Stufe 3 ist das vertretbar, 106 ist nicht die schwerste Aufgabe des Lernziels. Zu 112: Das Eingabefeld muss „7,5" mit Komma annehmen; der Text sagt „als Dezimalzahl", nennt aber kein Komma. |
| C-7 | VT3-036, 043 | Test 036 (Maßstab halbieren, Höhen verdoppeln, Differenz 4 cm) und Test 043 (Achsenbeginn ist für die Prozentzahl 5 % unwichtig) sind leichter als 038/040/041 bzw. 044. Prüfen, ob die Tests im Lernziel wirklich die schwersten sind. |
| C-8 | VT3-110 | Nähe zum Bestand „Nenne eine volle Stunde, zu der der kleinere Winkel größer als 90° ist, aber kein gestreckter": dieselbe Einsicht (Winkel zur vollen Stunde ist Vielfaches von 30°), jetzt aber als allgemeine Aussage. Vertretbar, aber kein neuer Gedanke. |
| C-9 | VT3-086, 087 | Zweimal „Punktprobe durch Einsetzen" (086 mit Begründung, 087 als Fehler-Detektiv). In 087 steht die richtige Lösung f(3) = 8 im Text als y-Koordinate von P(3 \| 8) (kein Leck, da Zeile 3 ohnehin gerechnet werden muss). |
| C-10 | saeulendiagramm (036–042) | Sechs von sieben Aufgaben arbeiten mit „1 cm steht für n Kinder" (036, 037, 038, 040, 041, 042); nur 039 ist ein reines Verhältnis. Beim Lernziel „Säulendiagramm" kaum vermeidbar. |
| C-11 | VT3-007, 012, 018, 033, 041, 114, 116 | Die richtige Option ist die **einzige mit einem „="** (Rechnung). Über alle Aufgaben enthält die richtige Option in 19 von 54 Fällen ein „=" gegenüber 33 von 162 bei den falschen (35 % gegen 20 %). Ein leichter Hinweis, bei 114 zusätzlich die längste Option. |
| C-12 | VT3-004/006, 015/016, 067/069, 071/073 | Gleiche Antwort in einem Lernziel (3, 3, 3, 2). Wer die erste kennt, kann bei der zweiten raten. Zahlen leicht ändern. |
| C-13 | VT3-099 | Die falschen Optionen sind schwach: [2] „Nachbarwinkel sind in keinem Fall gleich groß" ist für ein Kind erkennbar absurd, [1] behauptet 90° für jede Kreuzung. Als Test leichter, als der Rahmen es will. |
| C-14 | VT3-090, 125 | Sehr leicht („a · 0 = 0", Schenkellänge gegen Winkelgröße); als Sicherung ausreichend, kein Test. Bei 090 ist die richtige Option außerdem die längste. |
| C-15 | VT3-124, 126, 057 | Rechnen nach Schema (Division mit Rest, Summe/Differenz, Summe − Rest). Gut gebaut, aber ohne Einsicht lösbar. |
| C-16 | Unveränderte Aufgaben | Die Hinweise aus Runde 1 zu 010, 011, 019, 022, 024, 027, 031, 032, 035, 040, 042, 043, 052, 058, 073, 077, 080, 083, 087, 091, 094, 098, 101, 106, 107, 108, 122, 126 gelten unverändert (die meisten sind C). |
| C-17 | VT3-118 | Zweifel des Autors: nicht nötig. Die Aufgabe ist durch Ausprobieren lösbar (30°/30°/30° streicht [1] und [2], 10°/10°/70° streicht [0]); sie prüft den Gedanken „nicht alle drei können größer als 30° sein". Der Zusatz „größer als 0°" ist gut. |

## Schließung meiner Befunde

Befund aus `vorpruefung.md` → Stand heute. „ja" = im neuen Stand wirklich behoben, „teilweise" = Hauptpunkt behoben, Rest offen, „nein" = nicht behoben.

| Befund (Runde 1) | geschlossen? | Begründung |
|---|---|---|
| **A: VT3-067** (zwei vertretbare erste Fehler) | **ja** | Zeile 2 schreibt die Funktionswerte als Aufzählung „0; −3; −4; −3; 0", nicht mehr als Menge. Einziger Fehler in Zeile 3 (fünf Elemente). Lösung [3, 3] stimmt (W = {−4; −3; 0}). |
| B: VT3-055 (Bestand 6a/6b) | ja | Neu: fünf aufeinanderfolgende gerade Zahlen, Mittelwert 20 → größte 24 (16, 18, 20, 22, 24). Kein Bestandstreffer; neue Denkfigur („Mittelwert = Mitte"). |
| B: VT3-050 (Bestand „ein Kind kommt dazu") | ja | Neu: Werte verdoppelt und um 3 verkleinert (2 · 8 − 3 = 13); mit mehreren Zahlenfünfern nachgeprüft. |
| B: VT3-089 (Bestand A, B → m, t) | ja | Neu: S(4 \| c) auf zwei Graphen, a = 2. Bestand nur „Welcher Punkt liegt auf …". |
| B: VT3-037 (Bestand 4 Kinder, 7 cm) | ja | Neu: 1 cm = 8 Kinder, 4,5 − 3 = 1,5 „Kinder" (Einheitenfehler); Fehlertyp und Zahlen anders. |
| B: VT3-100 | **nein** | Siehe B-1: jetzt dieselben Zahlen wie der Bestand. |
| B: VT3-115 (Bestand Torte 10 Stücke) | ja | Neu: Stücke von 20° → 18 Stücke → 9 Schnitte. |
| B: VT3-113 (Bestand drei Teile 180°) | ja | Neu: x, x + 10, x + 20 mit Gleichung 3x + 30 = 90 als Test (Zeile 3 fehlerhaft). Fehlerzeile und Lösung eindeutig. |
| B: VT3-123 (Bestand `ge3`) | **nein** | Siehe B-2 (Bestand rollend-4/ge3, 65°, 90° statt 180°). |
| B: VT3-116 (sieben Diagonalen-Aufgaben) | ja | Neu: ein Drittel eines rechten gegen ein Viertel eines gestreckten Winkels (30° gegen 45°). Kein Bestandstreffer. |
| B: VT3-065 (x² + 1, x² − 4) | ja | Jetzt „−9 ∈ W" mit Gegenbeispielen (−10, 0); Muster verlassen. `idee` noch alt (C-2). |
| B: VT3-071 (Bestand x² − 7 = 9) | ja | Neu: x² − 6x, f(4) = −8 → zweite Stelle 2 (Symmetrie um 3). |
| B: VT3-079, VT3-093 | **teilweise** | 093 ist jetzt eine Taxiaufgabe („doppelte Strecke, weniger als doppelter Preis"), also behoben. 079 fragt jetzt f(0) aus einer Tabelle ohne x = 0; das ist besser, bleibt aber im Rechenschema „m und t bestimmen" (B-7). |
| B: VT3-110 (Zählung 22) | ja | Die Zähl-Aufgabe ist weg. Neu: „Vielfaches von 30° und höchstens 180°", Gegenbeispiele 3:00 und 6:00 / 12:00; alle vier Optionen sind geprüft. Rest: C-8. |
| B: VT3-006 (Fehlbild-Lücke) | **nein – mein Irrtum** | Der Autor hat recht. Im Stand 5bdace7c war `luecke: 2` mit dem Text „statt der Höhe angegeben" gespeichert; ich hatte mein Dump falsch gelesen. Mein Befund war falsch. Das Fehlbild stimmt auch jetzt (12 = 2 · 6 gehört in Lücke 2). |
| B: VT3-075 (FB 80 statt 81) | ja | Die Fehlbilder sind jetzt zur Rechnung passend; die Rechnung wird ausgewertet und stimmt mit der Antwort überein. |
| B: VT3-114 (Rechenfehler als Optionen) | ja | Alle drei falschen Optionen sind jetzt Fehlvorstellungen mit Zeilenbezug („große Teil besteht nur aus zwei Stücken", „zweite Division", „Ergebnis unsinnig, Zeile des Fehlers verwechselt"). Rest C-11. |
| B: VT3-048 („Beide Hochachsen") | ja | Jetzt „Die Hochachse beginnt bei 0." |
| B: VT3-059 (Antwort 10 wie 058) | ja | 059 hat jetzt 50 s / 48 s, Antwort 40; 058 bleibt 10. |
| B: VT3-105 (65°/115° wie 102) | ja | 105 benutzt 72°/108°, 102 jetzt 50°/130°. C-12 betrifft nur kleine Überschneidungen. |
| B: VT3-003, VT3-005 (Kantenfaktoren) | **teilweise** | 005 ist jetzt „gemischte Einheiten, Rechnung wählen" (ja). 003 bleibt bei Kantenfaktor 3 (nein, B-12). |
| B: VT3-033 (wie 029) | ja | 029 ist jetzt „nötige weitere Treffer" (Umkehr); 033 bleibt Vergleich. Eigene Figuren. |
| B: VT3-041 (wie 036) | **teilweise** | 041 ist jetzt der Vergleich zweier Diagramme mit verschiedenem Maßstab; 036 „Maßstab halbiert". Beide bleiben im Schema „Höhe mal Maßstab" (C-10). |
| B: VT3-046 (wie 043/047) | ja | 046 jetzt Prozentpunkte gegen Prozent (20 % → 30 %: 50 %); 043 Achsenbeginn. 047 ist aber neu eine Bestandsdoppelung (B-3). |
| B: VT3-062 (`zwei_wege` ohne zwei Wege; sechs von sieben gleich) | **teilweise** | 062 ist jetzt Gruppenmittel, 061 trägt `zwei_wege`. Fünf von sieben bleiben Summe-Rest (B-13). |
| B: VT3-008 (Rechnen nach Schema) | ja | Neu: würfelförmiger Behälter, 1 l, 10 cm hoch → 1,5 m Kante → 15³ = 3 375 Behälter. Einsicht „Kantenfaktor 15, Volumenfaktor 15³" nötig. |
| B: VT3-012 (zwei_wege nur Rechnen) | ja | Neu: Quader und Würfel mit gleichem Volumen 8 000 cm³ = 8 l als Vergleichsaufgabe; Distraktoren kommen aus der Kantenlänge. |
| B: VT3-025 (reines Rechnen) | **nein** | Neu: 4 cm Scheibe von 10 cm Würfel → 60 %. Immer noch Schema; und dieselbe Denkfigur wie 022/023 (B-6). |
| B: VT3-026 (richtige Option rechnet) | ja | Jetzt „dieselben drei Zahlen malgenommen"; die richtige Option enthält keine Rechnung mehr, [3] („nicht ohne Ausrechnen") ist die Falle. |
| B: VT3-036 (Test nur nominal Stufe 3) | **teilweise** | Neu mit Maßstab halbiert (mehr Einsicht). Bleibt zweischrittig und leicht (C-7). |
| B: VT3-044 (ohne Einsicht lösbar) | **nein** | Siehe B-4. |
| B: VT3-009 (richtige Option doppelt so lang) | ja | Längen angeglichen (richtige 2. von 4 nach Länge, keine Option mehr als 30 % länger). |
| B: VT3-064 (richtige Option längste) | ja | Alle vier Optionen ähnlich lang, richtige an Platz 1 von 0 bis 3; sie ist nicht mehr die längste. |
| B: VT3-086 (längste, dreimal Punktprobe) | **teilweise** | Länge angeglichen (ja). Zweimal Punktprobe (086, 087) bleibt (C-9), 088 ist jetzt eine eigene Figur. |
| B: VT3-109 (doppelt so lang, gleiche Idee wie Bestand) | ja | Neu: Mia 9:00/3:00 gleicher Winkel, Jonas 9:15 = 90°; Optionen gleich lang. Figur „Stundenzeiger wandert weiter" ist anders als der Bestand. |
| B: alle Auswahl (34/49 längste, Platz 2 mit 25×) | **teilweise** | Verteilung behoben (14/14/13/13; längste 14/54). Dafür entsteht eine erkennbare Platzfolge (B-9). |
| B: README (zwei Lernziele „verstehen") | ja | README führt „verstehen (Volumen)" (5 Kategorien) und „verstehen (Winkel)" (6) getrennt; 023 trägt jetzt `begruenden`. Die Tabelle stimmt mit den `idee`-Feldern überein. |

Ergebnis: **24 ja, 7 teilweise (079/093, 003/005, 041, 062, 036, 086, alle Auswahl), 4 nein (100, 123, 025, 044), 1 war mein Irrtum (006).**

## Wird jetzt echtes Verstehen geprüft?

**Teilweise, deutlich mehr als in Runde 1.** Gelesen: je Lernziel alle 7 Aufgaben nebeneinander.

### Denkfiguren je Lernziel (knappe Lernziele zuerst)

| Lernziel | wirklich verschiedene Figuren | Urteil |
|---|---|---|
| verstehen (Volumen) | 5 bis 6: Volumen ∝ Höhe/Schicht (022, 023, 025), Prozentfaktor (028), Einheitenfehler (024), Faktoren in beliebiger Reihenfolge (026), Packung nicht passend (027) | knapp; 022/023/025 sind eine Figur (B-6) |
| graph_lesen | 4: m und t aus Daten (078, 079, 080, 083), parallel (081), nicht linear (082), Vorzeichen der Steigung (084) | zu wenig (B-7) |
| sachzusammenhang | etwa 3: Anfangswert plus Änderung (092, 094, 095, 096, 097), nicht proportional (093), Tarifvergleich (098) | zu wenig (B-11) |
| figuren | 4: Teile aus Gleichung/Verhältnis (113, 114, 119), Schnitte statt Stücke (115, 117), Bruchteile (116), Extremaussage (118) | knapp (B-10) |
| quader | 4: Kantenfaktoren (001, 002, 003, 006), Summe statt Produkt (004), Einheiten (005), Kantensumme (007) | zu wenig (B-12) |
| mittel_rueckwaerts | 3: Summe − Rest (057, 058, 059, 062, 063), Begründung (060), Abweichungen (061) | zu wenig (B-13) |
| rueckwaerts, liter | 5 bis 6 | in Ordnung; liter lebt von cm³/l, rueckwaerts von V : (l · b) in 015/016/017/021 (C) |
| die übrigen 11 Lernziele | 6 bis 7 | in Ordnung |

### Aufgaben, die im Kern noch Rechnen nach Schema sind

Zahl- und Lückenaufgaben ohne nötige Einsicht (34): 003, 011, 014, 019, 021, 025, 032, 035, 038, 040, 042, 043, 057, 058, 062, 063, 070, 075, 077, 078, 079, 083, 085, 089, 091, 098, 100, 102, 104, 115, 117, 119, 124, 126.

Dazu 15 Fehler-Detektive, deren Fehler ein Rechen- oder Einsetzfehler ist (kein Begriffsfehler): 004, 010, 016, 024, 031, 037, 052, 059, 073, 080, 087, 094, 101, 108, 123.

**Zusammen 49 von 126 (39 %).** In Runde 1 waren es 58 C-Aufgaben nach meiner Zählung. Ein Teil davon ist für ein Üben nach Schema in Ordnung (Sicherung Stufe 2); als Test gehört nichts davon ins Lernziel (siehe nächster Abschnitt).

### Ist die Test-Aufgabe jeweils die anspruchsvollste?

| Test | Urteil |
|---|---|
| **001** (Kanten +50 %, −20 %, doppelt) | in Ordnung. Die Falle „Prozente addieren" (130 %) ist echt; trotzdem ein Faktor-Schema, das 002/003/006 schon üben (B-12). |
| 008 | gut (Kantenfaktor 15, 15³). |
| 015 | in Ordnung (b · 3b = 27). |
| **022** | **nein**: leichter als 027 und 028 (B-6). |
| 029 | gut (Umkehr, Zielhäufigkeit). |
| 036 | leicht (C-7). |
| 043 | mittel (C-7): Der Achsenbeginn ist für die Prozentzahl unerheblich; wer das erkennt, rechnet einfach 240 : 4 800. |
| 050 | in Ordnung (mit Beispielzahlen prüfbar, aber das ist auch Einsicht). |
| **057** | **mittel**: Schema „Summe − Rest" (C-15); schwerer als 058/059, aber nicht schwerer als 062/063. |
| 064 | gut („höchstens 12" ist nicht zu raten). |
| 071 | gut (Symmetrie um 3). |
| **078** | **nein**: leichteste Aufgabe des Lernziels (B-7). |
| 085 | in Ordnung (b aus P, dann Wert). |
| 092 | gut (Term und sinnvoller Bereich). |
| 099 | in Ordnung, aber schwache Distraktoren (C-13). |
| **106** | **mittel**: lösbar mit Spiegelgedanken (12 − 7) oder Durchprobieren; 112 ist mindestens so anspruchsvoll (C-6). |
| 113 | gut (Gleichung im Fehler-Detektiv). |
| 120 | gut (immer/nie, Gegenbeispiele). |

**Fazit:** Fünf Tests sind nicht die anspruchsvollsten (022, 078, 106 bis auf Gleichstand, 036, 043). Zu 112 nach Auftrag: In Ordnung als Sicherung; der Fallstrick „Gangunterschied statt Uhrzeit" ist echt (FB 90 und 15 passen), die Dezimalantwort ist C-6.

## Einzelfragen

- **VT3-118:** Aufgabe und Optionen stimmen (Modell über alle ganzzahligen Dreierzerlegungen von 90°). Der Zusatz „größer als 0°" schließt die Lücke aus Runde 1. Zweifel des Autors unbegründet (C-17).
- **VT3-053:** Siehe B-5. Antwort lösbar durch Beispielzahlen und Raten.
- **VT3-055:** In Ordnung. Fünf aufeinanderfolgende gerade Zahlen mit Mittelwert 20: 16, 18, 20, 22, 24 → 24 (Modellrechnung, eindeutig). Neue Figur („Mittelwert = Mitte"), kein Bestandstreffer.
- **VT3-110:** Alle vier Optionen sind über die zwölf vollen Stunden geprüft: [0] 3:00 Uhr (90°) widerlegt, [1] 6:00 und 12:00 haben keine zweite Stunde, [2] 6:00 Uhr (180°) widerlegt, [3] gilt für alle zwölf. Eindeutig. Die frühere Zähl-Aufgabe (22) ist weg.

## Auswahl-Statistik und Platzmuster

- Platz der richtigen Option: 14 / 14 / 13 / 13. Längste Option richtig: 14 von 54. Rang der richtigen Option nach Länge: 14 / 20 / 15 / 5. Das ist, abgesehen von B-9 und C-11, unauffällig.
- Der Algorithmus `(3 · Zähler + 1) mod 4` erzeugt in Kennungsreihenfolge `10 3210 3210 …` (siehe B-9), also jedes Mal „einen Platz früher". Nach zwei gelösten Auswahlaufgaben ist die dritte vorhersagbar. In einem Test mit einer Aufgabe je Lernziel fällt das Muster kaum auf, die Aufgaben stehen auf anderen Zähler-Ständen (Test-Auswahlen: 064 → 1, 078 → 3, 092 → 0, 099 → 3, 120 → 2).
- Ob die App die Optionen mischt, konnte ich nicht sehen. Mischt sie, ist B-9 gegenstandslos.

## Ohne Bild verständlich? Lehrplan

- **Ohne Bild verständlich:** Alle Aufgaben sind ohne Bild eindeutig. Bei den Uhren genügen die Uhrzeiten; die Annahme „der Stundenzeiger wandert gleichmäßig" steht in 112 jetzt im Text, in 107, 108 und 111 nur im Lösungsweg (Bestand lehrt die Konvention). 121 setzt ein Geodreieck mit zwei Skalen voraus, ohne Gerät ist der Gedanke Wissen, kein Messen.
- **Lehrplan:** Keine Aufgabe liegt über der Klassenstufe. Stufe 3 bei 118 (Beweisdenken) liegt am oberen Rand von Klasse 5, aber lösbar. Prozentpunkte in M6 3 stehen im Bestand. Bruchterme in M8 1 (069, 075) stehen im Bestand.

## Was ich nicht prüfen konnte

- Wie die App Optionen anzeigt (feste Reihenfolge oder gemischt) und ob sie „7,5" mit Komma akzeptiert.
- Wie ein Test aus den Aufgaben zusammengesetzt wird (eine Aufgabe je Lernziel oder mehrere).
- Die Bilder und Lernkarten der App; Prüfung rein am Text.
- Ob Kinder die Fehlbild-Beschreibungen so wählen, wie sie gedacht sind (Erprobung).

## Keine Schönfärberei

- Ich habe in Runde 1 einen Befund (006) falsch gelesen und für 123 einen Vorschlag gemacht, der selbst eine Bestandsdoppelung ist. Beides steht oben.
- Von den 126 Aufgaben sind 49 weiter im Kern Schema; das ist für eine Lern-App normal, aber kein Verstehenstest. Die Tests 022, 078 und 036 gehören noch schwerer gemacht, wenn das Ziel „schwerer als bisherige Tests" gilt.
- Die Stärken der neuen Fassung: kein A, Verteilung der Optionen sauber, Doppelungen mit dem Bestand fast alle behoben, 118/110/055 gut.
