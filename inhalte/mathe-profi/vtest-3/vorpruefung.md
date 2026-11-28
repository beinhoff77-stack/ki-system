# Vorprüfung Runde VT3 (unabhängig, alle 126 Aufgaben VT3-001 bis VT3-126)

Stand 28.11.2026. Prüfer: unabhängig vom Autor, keine Aufgabe und kein fremder Code geändert. Jede Aufgabe mit Text, Optionen, Fehlbildern und Lösungsweg von Hand gelesen. Eigene Rechnung: `vorpruefung_rechnen.py` (liegt neben dieser Datei; Aufruf `python3 -I inhalte/mathe-profi/vtest-3/vorpruefung_rechnen.py` im Wurzelordner).

Kennzeichnung: **[F]** = Tatsache (nachgerechnet, im Repo gelesen, von Werkzeug ausgegeben) · **[A]** = Annahme oder Einschätzung.

## Gesamturteil: bereit für die Gegenprüfung **nach Korrektur**

[F] Keine Sollantwort ist rechnerisch falsch. Alle Sollantworten stimmen mit meiner eigenen Rechnung überein (siehe Werkzeuge). Alle Fehlbilder in Zahl- und Lückenaufgaben ergeben mit ihrer `rechnung` exakt die gespeicherte `antwort`; keines gleicht der Lösung.

[A] Nicht ohne Korrektur einspielbar, weil (1) ein Fehler-Detektiv (VT3-067) zwei vertretbare „erste Fehler“ hat, (2) **14 Aufgaben dem Bestand so nahe sind, dass sie keine neue Denkfigur bringen**, darunter drei mit demselben Aufbau wie eine Übung der Etappe (VT3-055, VT3-089, VT3-037), und das Werkzeug das nicht erkennt, (3) die richtige Option in 34 von 49 Auswahl-Aufgaben die **längste** und in 41 von 49 an **Platz 2 oder 3** steht (ein Kind kann ohne Rechnen raten), (4) drei Fehlbild-Zuordnungen nicht zur gespeicherten Zahl führen, (5) mehrere Lernziele im Kern aus einer einzigen Denkfigur bestehen, obwohl die Kategorien im Feld `idee` verschieden heißen.

| Zahl | Wert |
|---|---|
| geprüfte Aufgaben | 126 |
| Sollantwort nach eigener Rechnung richtig | 126 (von 126; bei VT3-067 ist aber der Fehlerort mehrdeutig) |
| Aufgaben mit Befund A (muss korrigiert werden) | 1 (VT3-067) |
| Aufgaben mit Befund B (sollte korrigiert werden) | 36 (003, 005, 006, 008, 009, 012, 025, 026, 033, 036, 037, 041, 044, 046, 048, 050, 055, 059, 062, 064, 065, 071, 075, 079, 086, 089, 093, 100, 105, 109, 110, 113, 114, 115, 116, 123) |
| Aufgaben mit Befund C (Hinweis) | 58 |
| Aufgaben ganz ohne Befund | 31 (002, 007, 016, 017, 018, 022, 024, 028, 030, 031, 035, 038, 040, 047, 051, 054, 056, 061, 066, 076, 078, 080, 088, 090, 091, 092, 096, 101, 103, 119, 122) |

(Zählung nach dem jeweils schwersten Befund je Aufgabe. Zusätzlich drei übergreifende Befunde ohne einzelne Kennung, siehe Tabelle: Optionslänge/-platz, README-Tabelle „verstehen“, `idee`-Beschriftungen.)

## Werkzeuge, selbst ausgeführt

| Werkzeug | Ergebnis |
|---|---|
| `python3 -I tools/vtest_pruefen.py --runde 3` | [F] „OK – keine Fehler“, 2 HINWEISE. **VT3-010: Fehlalarm bestätigt.** 50 · 30 · 40 = 60 000 stimmt; das Werkzeug liest „60000cm³“ wegen der angeklebten Einheit nicht als Zahl. Zeile 1 ist richtig, der erste Fehler ist Zeile 2 (Liter = 100 cm³). **VT3-073: Fehlalarm bestätigt.** Zeile 1 „3x + 6 = 15“ ist die angesetzte Gleichung (keine Rechenkette); der Hinweis „+ 6 = 15“ entsteht durch das Abschneiden am Gleichheitszeichen. Erster Fehler Zeile 2 (15 + 6 statt 15 − 6), verlangter Wert x = 3 eindeutig. |
| `python3 -I inhalte/mathe-profi/vtest-3/gegenrechnung.py` | [F] „126 Aufgaben geprüft, 0 Abweichungen“. [A] Die Skripte des Autors setzen bei logischen Aufgaben Indizes fest; diese habe ich selbst geprüft (nächste Zeile). |
| mein `vorpruefung_rechnen.py` | [F] „125 Prüfungen, 0 Abweichungen“. Zahl-/Lückenaufgaben mit eigener Formel und exakten Brüchen bzw. Zählschleife (Quersumme 068, Wertemengen 067/070, Nullstellen/Stellen 069/071/072/075 per Suchschleife über −60…60, Parkplatz 077 minutengenau, Uhren 106/108/112 über Winkelfunktion mit 0,5° je Minute, **VT3-110 stetig gerechnet**: Relativgeschwindigkeit 5,5°/min, rechter Winkel bei 5,5·t = 90 + 180·j, 0 ≤ t < 720 ⇒ j = 0…21 ⇒ **22**; Mitternacht und Mittag haben 0°, die Randfrage ist also eindeutig, der Satz „Mitternacht würde mitzählen …“ ist für das Ergebnis ohne Wirkung). Auswahl-Aufgaben: jede Option einzeln gerechnet bzw. Gegenbeispiele durch Aufzählung (VT3-065 über ℚ-Gitter, VT3-103/105 über alle Kreuzungen a = 1…179°, VT3-116 über Rechtecke 1…11 × 1…11, VT3-118 über **alle** ganzzahligen Zerlegungen von 90° in drei positive Teile, VT3-120 über alle spitz + stumpf). Nicht per Skript, nur von Hand: 099, 114, 121 und die Wortlaut-Prüfung aller Erklärtexte. |
| eigene Fehlbild-Prüfung | [F] Für alle Zahl-/Lückenaufgaben die `rechnung` jedes Fehlbilds mit eigenem Ausdrucksrechner ausgewertet: 0 Abweichungen zur gespeicherten `antwort`. Bei Auswahl: zu jeder falschen Option genau ein Fehlbild, Indizes vollständig. (Die Mängel unten betreffen Zuordnung/Erklärtext, nicht die Rechnung.) |
| Ähnlichkeitssuche gegen den Bestand | [F] Eigenes Skript: Wort- plus Zahlenüberlappung aller 126 Aufgaben (Text + Optionen) gegen 1 459 Bestandsaufgaben (`inhalte/themen/` der fünf Einheiten und alle `rollend-*` mit diesen Einheiten). Treffer wurden von Hand gelesen; Ergebnis im Abschnitt „Doppelungen“. |

## Befundtabelle

Schweregrad: A = fachlich falsch/mehrdeutig, muss korrigiert werden; B = sollte korrigiert werden; C = Hinweis.

### A

| Kennung | Grad | Befund | Korrekturvorschlag |
|---|---|---|---|
| VT3-067 | A | Fehler-Detektiv mit **zwei vertretbaren ersten Fehlern**. Zeile 2 „W = {0; −3; −4; −3; 0}“: Eine Menge mit doppelt aufgeschriebenen Elementen ist **dieselbe Menge** wie {−4; −3; 0}; schlecht geschrieben, aber nicht falsch. Die einzige falsche Aussage ist Zeile 3 („Er zählt fünf Elemente“). Ein Kind, das Mengen kennt und „Zeile 3“ antwortet, wird als falsch gewertet; die Rückmeldung „Zeile 2 ist falsch“ widerspricht der Mengenlehre. Die Idee (doppelte Funktionswerte zählen nicht doppelt) ist gut. | Zeile 2 ohne Mengenschreibweise: „Er schreibt die Funktionswerte der Reihe nach auf: 0; −3; −4; −3; 0.“ Zeile 3: „W hat also fünf Elemente.“ Zeile 4 wie bisher. Dann ist Zeile 3 der erste Fehler: `werte [3, 3]`, Fehlbilder und `w` anpassen („Mehrfach genannte Werte zählen in W nur einmal“). |

### B

| Kennung | Grad | Befund | Korrekturvorschlag |
|---|---|---|---|
| VT3-055 | B | **Fast dieselbe Aufgabe wie eine Übung der Etappe** (`inhalte/themen/daten.kennwerte.json`): „In der 6a (20 Kinder) … im Mittel 12 Punkte, in der 6b (30 Kinder) 17 Punkte. Mittelwert aller 50 Kinder?“ = 15. VT3-055 hat dieselbe Struktur, dieselben Klassen mit 20/30 Kindern, Noten 3,0/2,0 statt Punkten. Die „neue Denkfigur“ der Überarbeitung ist nicht neu; das Werkzeug erkennt es nicht (Wortähnlichkeit zu gering). | Andere Denkfigur: z. B. „Zwei Gruppen haben denselben Mittelwert 8. Wie groß ist der Mittelwert aller, wenn eine Gruppe doppelt so groß ist?“ (Begründen, 8) oder Rückwärts: „Mittelwert 2,4 von 50 Kindern, Klasse A 20 Kinder mit 3,0; Mittelwert von B?“ |
| VT3-050 | B | Test-Aufgabe ist die Bestands-Übung „4 Kinder haben im Mittel 15 Punkte. Ein weiteres Kind kommt mit 3 Punkten dazu. Neuer Mittelwert?“ mit anderen Zahlen (7 Kinder, 18 €, 42 €). Schema (Summe + neuer Wert, durch neue Anzahl) identisch, FB „einfach Mittelwert der beiden Zahlen“ ebenso Bestand. Als Test für „schwerer als bisherige Tests“ zu leicht. | Verstehens-Wendung: „Ein achtes Kind kommt dazu. Der Mittelwert steigt dadurch von 18 € auf 21 €. Wie viel spart es?“ ist Umkehr (und gleich VT3-057 in der Idee); besser: Zwei neue Kinder sparen zusammen 84 €; steigt oder sinkt der Mittelwert, ohne zu rechnen (Begründung)? |
| VT3-089 | B | Gleiche Punkte wie die Bestands-Übung „Die Punkte A(1 \| 3) und B(3 \| 7) liegen auf dem Graphen von f(x) = m · x + t. Bestimme m und t.“ Hier nur C(5 \| y) statt m, t. Gleiche Denkfigur (Steigung aus zwei Punkten). | Andere Punkte und eine echte Wendung: „A(1\|3), B(3\|7), C(x\|11) liegen auf einer Geraden; x?“ (Steigung rückwärts) mit anderen Zahlen. |
| VT3-037 | B | Fehler-Detektiv ist fast die Bestands-Übung `rollend-4/d1`: „1 cm für 4 Kinder. Eine Säule ist 7 cm hoch. Kim … Zeile 2: Die Säule gehört also zu 7 : 4 Kindern“. VT3-037: 1 cm für 6 Stimmen, **ebenfalls 7 cm**, derselbe Fehler (Teilen statt Malnehmen). Das Kind erkennt die Vorlage. | Anderer Fehler im Säulen-Zusammenhang: z. B. Achsenbeginn ignoriert oder Höhen addiert statt Differenz (neue Zeilen, neue Zahlen). |
| VT3-100 | B | Bestand `geometrie.winkel`: „Ein Winkel ist halb so groß wie der Winkel, der ihn zu 180° ergänzt“ (Antwort 60) und „An einer Geradenkreuzung ist ein Winkel 2-mal so groß wie sein Nachbarwinkel. Wie groß ist der kleinere?“ (60). VT3-100 ist dasselbe („halb so groß wie sein Nachbarwinkel“) plus ein Schritt Scheitelwinkel. Dazu rollend-3: „um 40° größer als sein Nachbarwinkel“. Drei Bestandsaufgaben mit demselben Kern. Zusätzlich FB 240 („Scheitelwinkel noch einmal verdoppelt“) ist keine echte Fehlvorstellung. | Denkfigur wechseln, z. B.: „Vier Winkel an einer Kreuzung, einer ist um 30° größer als sein Scheitelwinkel – geht das?“ (Begründen) oder drei Geraden. |
| VT3-115 | B | Bestand: „Eine Torte wird in 10 gleiche Stücke geschnitten. Wie groß ist der Winkel eines Stücks?“ (36°). Die erste Lücke von VT3-115 ist **dieselbe Frage mit gleicher Antwort**; der Kniff „5 Schnitte durch den Mittelpunkt“ ist nur der Weg von 5 zu 10 Stücken. Zweite Lücke (3 Stücke) ist Malnehmen. Rechnen nach Schema. | Echter Zusammenhang: „Wie viele Schnitte durch den Mittelpunkt braucht man für Stücke von 20°?“ (9 Stücke … 18 Stücke → 9 Schnitte) – Umkehr mit Falle (Schnitte statt Stücke). |
| VT3-113 | B | Bestand: „Von einer Ecke eines Rechtecks gehen zwei Strecken aus … drei Teile. Zwei Teile sind 30° und 10°. Wie groß ist der dritte?“ VT3-113 ist dieselbe Situation als Fehler-Detektiv mit 27°/41°; der Fehler (180° statt 90°) ist offensichtlich. Als **Test** (Stufe 3) zu leicht. | Stärkerer Test: Fehler in einer Folgerung, z. B. Diagonale und Teilwinkel (Zeile 3: „Beide Teile sind 45°, weil die Diagonale halbiert“), oder Aussage über alle Zerlegungen. |
| VT3-123 | B | Gleicher Fehler und gleiche Schablone wie die Bestands-Übung `rollend-4/ge3`: „Jeder der drei Teile hat 180° : 3 = 60°“ (Quadrat/Eckwinkel 180° statt 90°). VT3-123: Vollwinkel mit 180° statt 360°; sonst identisch („180° : 3 = 60°“). | Anderer Fehler: z. B. Scheitelwinkel mit Nebenwinkel verwechselt, oder Winkel „ergänzen“ mit 90° statt 180°. |
| VT3-116 | B | Bestand hat **sieben** Aufgaben mit „Im Rechteck (kein Quadrat) teilt die Diagonale den Eckwinkel in … Stimmt die Aussage ‚Beide Teile sind 45°‘?“ (korrektur/sicherung). VT3-116 ist dieselbe Einsicht („nur im Quadrat gleich groß; zusammen immer 90°“) als allgemeine Frage; Option [2] („zusammen immer 90°“) ist die schon geübte Aussage. | Anders: Diagonale im Parallelogramm/Raute teilt den Winkel (nicht 90°), oder „die Winkel an A und C“ – oder diese Aufgabe streichen. |
| VT3-065 | B | Gleiches Muster wie Bestand „f(x) = x² + 1 mit D = ℚ. Welche Aussage über die Funktionswerte stimmt? Kein Funktionswert ist kleiner als 1 …“ und „f(x) = x² − 4 …“; hier 5 − x² gespiegelt, **gleiche vier Optionstypen** („kein Wert größer/kleiner …“, „kleinster Wert“, „alle positiv“). Das Kind erkennt die Schablone. | Andere Funktion/Frage, z. B. „Welcher Funktionswert kommt für f(x) = x² − 4 mit D = ℚ **nicht** vor? −5 / −4 / 0 / 5“ (Gegenbeispiel-Denken). |
| VT3-071 | B | Test-Aufgabe, Denkfigur des Bestands „f(x) = 9 bei f(x) = x² − 7, beide Stellen, kleinere zuerst“ (Stufe 3). Der Autor räumt die Nähe ein; (x − 3)² ist nur eine Verschiebung. | Test mit Einsicht in die Zwei-Stellen-Struktur: „f(x) = x² − 6x. Bei f(4) = −8 gibt es noch eine zweite Stelle. Welche?“ (Symmetrie um 3 → 2). |
| VT3-079, VT3-093 | B | Beide „Wertetabelle → Term“ mit vier Optionen aus (Steigung/Achsenabschnitt vertauscht, nur ein Wert passt). Bestand hat fünf solche Übungen („Welcher Funktionsterm passt zur Wertetabelle …“). VT3-078 (Gerade durch zwei Punkte → Term) ist dieselbe Denkfigur im selben Lernziel (graph_lesen). | In VT3-079 die Tabelle ohne Wert bei x = 0 (z. B. x = 1, 3, 5) oder Aussage „Warum kann y = 2x + 3 nicht zur Tabelle gehören?“. VT3-093 durch Stellen-/Sachfrage ersetzen. |
| VT3-110 | B | (a) Bestand: „Wie oft stehen die Zeiger zwischen 12:00 und 18:00 genau übereinander? 12:00 zählt mit, 18:00 nicht“ (6). VT3-110 ist dasselbe Verfahren (Überholungen zählen), mit Faktor 2. (b) Schwierigkeit: Die Zahl 22 verlangt den Überholungs- oder Relativwinkel-Gedanken; in Klasse 5 in 2–4 Minuten nur durch Raten oder durch Wissen aus der Übung zu lösen. (c) „Mitternacht würde mitzählen …“ ist für das Ergebnis wirkungslos und verwirrt. | Entweder Zählweise kleiner („zwischen 3:00 Uhr und 4:00 Uhr: wie oft rechter Winkel?“) oder die Randsätze streichen und als Stufe-3-Sicherung mit Begründung führen; als Test ungeeignet. |
| VT3-006 | B | Fehlbild 12 (Länge 2 · 6 statt Höhe): `luecke` ist 1 gespeichert, der Text „statt der Höhe angegeben“ gehört zu Lücke **2** (Lücken ab 1 gezählt). In Lücke 1 (Breite) wäre 12 die Länge – die Rückmeldung stimmt dann nicht zur Eingabe. | `luecke: 2`, Rechnung „216 : 36 · 2“ beibehalten. |
| VT3-075 | B | Fehlbild 80 mit `rechnung` „20 · 4“ und Text „20 mit 4 malgenommen statt durch 4 geteilt“: Wer so rechnet, hat a − 1 = 80 und damit a = **81**, nicht 80. 80 entsteht nur mit zusätzlich vergessener „+ 1“. | Fehlbild 81 mit Rechnung „20 · 4 + 1“, oder Text „mit 4 malgenommen und außerdem die 1 vergessen“. |
| VT3-114 | B | Optionen [2] („90° : 3 gleich 33°“) und [3] („3 · 30° gleich 60°“) sind **Rechenfehler, die kein Kind als Fehlvorstellung wählt**; sie sind als Zeilenfehler erkennbar falsch behauptet. Zusätzlich ist die richtige Option die längste und die einzige mit Rechnung. Die Aufgabe bleibt als Fehler-Detektiv (4 Zeilen, Option nennt Zeile + Begründung) die einzige Auswahl-Variante. | Distraktoren mit echter Fehlvorstellung: [2] „In Zeile 3, weil durch 4 geteilt werden müsste, nämlich 90° : 4 = 22,5° (Zeile 2 ist richtig)“ – das wäre die Folge von Zeile 2, also falsch begründet; [3] „In Zeile 4: der große Teil ist 3 · 22,5° = 67,5°“ – gleich lang halten. |
| VT3-048 | B | „Beide Hochachsen beginnen bei 0“, aber es ist **ein** Diagramm mit zwei Säulen. Ohne Bild unklar, ob es zwei Diagramme gibt. | „Die Hochachse beginnt bei 0.“ |
| VT3-059 | B | Gleiche Antwort 10 wie VT3-058 (beide Pool korrektur, beide Lernziel mittel_rueckwaerts): Wer 058 mit „10“ als Verbesserung gesehen hat, kann bei 059 „10“ erraten. Zusätzlich Bestand: „Mittelwert von vier Zahlen ist 7,5. Drei der Zahlen sind 6, 9, 8 …“ (gleiche Schablone). | Zahlen in 059 ändern (z. B. Mittelwert 8, Zahlen 5, 12, 6, vierte 9). |
| VT3-105 | B | Die richtige Option verwendet 65°/115°, genau die Antworten von VT3-102 (α = 65°, β = 115°); VT3-104 hat ebenfalls 65. Wer 102 gelöst hat, erkennt die Zahlen. 099 (Test) nennt in der richtigen Option den Satz „Nachbarwinkel ergeben zusammen 180°“, der gleichzeitig die Lösung von 103 ist. Dasselbe Argument „Sonderfall 90°“ trägt 099 und 103. | 105 mit anderen Winkeln (z. B. 48°/132°); 103 auf eine andere Aussage drehen (z. B. „Wenn α = γ, dann …“). |
| VT3-003, VT3-005 | B | Im Lernziel quader bestehen **002, 003, 005** (und 001) aus **derselben Denkfigur** „Kantenfaktoren multiplizieren sich“ (½·½·½; 2·2·½; 4·½·1; 2·3·½). Die Kategorien heißen immer_nie/umkehr/was_waere_wenn, das Denken ist dasselbe. | 003 oder 005 ersetzen durch eine andere Einsicht (z. B. „Warum verdoppelt sich das Volumen nicht, wenn man alle Kanten um 2 cm verlängert?“; Oberfläche ↔ Volumen). |
| VT3-033 | B | Dieselbe Denkfigur wie VT3-029 (Anteile zweier verschieden großer Gruppen vergleichen, 8 von 25 gegen 9 von 30 / 9 von 24 gegen 12 von 40). | 033 auf andere Idee drehen (z. B. relative Häufigkeit und Anzahl bei mehr Würfen). |
| VT3-041 | B | Dieselbe Denkfigur wie VT3-036 (zwei Maßstäbe, Höhe umrechnen) – Test und Sicherung; VT3-049 ebenfalls Maßstab. Im Lernziel saeulendiagramm lauten 036, 038, 039, 041, 042 im Kern „Höhe mal Maßstab“. | 041 durch eine andere Einsicht ersetzen (z. B. Säulenbreite/Fläche, oder zwei Säulen mit gleichem Anteil). |
| VT3-046 | B | Dieselbe Denkfigur wie VT3-043 (abgeschnittene Hochachse, wirklicher Zuwachs in Prozent), dazu 047 (Achsenbeginn 60). Im Lernziel irrefuehrend sind 043, 046, 047 drei von sieben „Achsenbeginn ≠ 0“. | 046 als Fehler-Detektiv mit anderem Fehler (z. B. falsche Basis für Prozent) – Zeile 3 „20 %“ statt 25 % ist als Fehlbild schon in 046 enthalten; Aufgabe auf ein Kuchendiagramm/Prozentschreibweise drehen. |
| VT3-062 | B | `zwei_wege`, aber beide Wege führen zur selben Rechnung; das Kind braucht keinen der Wege zu verstehen. Gesamt: 057, 059, 060, 061, 062, 063 sind **sechs von sieben** Aufgaben des Lernziels mittel_rueckwaerts mit gleicher Rechenfigur „Summe = Mittelwert · Anzahl, fehlende Zahl = Rest“. Nur 058 ist anders. | 062 durch eine Aufgabe ersetzen, in der die Abweichungs-Methode wirklich zwingend ist (z. B. viele Zahlen nahe 100: Mittelwert aus Abweichungen), 061 als Begründung stärken. |
| VT3-008 | B | **Test-Aufgabe** ist ein dreischrittiges Rechnen nach Schema (Volumen → ml → Gläser), Stufe 3 nur wegen der drei Schritte; „Brücke“ ist hier Umrechnen. Bestand hat „Aquarium … Wie viele Liter fasst es?“ und „Umzugskarton“. | Verstehen einbauen: „Zwei Gefäße, 2 l und 2 000 cm³ …“ oder Rückwärts-Brücke („200 ml-Gläser, Behälter 10 cm × □“) mit Begründung. |
| VT3-012 | B | `zwei_wege`, aber beide Wege sind nur Rechnen (30 000 / 30 / 30); keine Einsicht erforderlich. Gleicher Rechenkern wie 008. | Fragen, **warum** beide gleich sind, oder Aufgabe auf Fehlervermeidung drehen („Jonas rechnet 4 · 2,5 · 3 = 30 cm³“). |
| VT3-025 | B | Reines Rechnen („3 · 2 · 4 Würfel, mal 8“); Stufe 2 genügt, Denkfigur kommt im Bestand (`messen.volumen`: Treppenkörper, Schachtel-mit-Würfeln). Zwei Rechenwege führen zur Lösung. | Rückwärts: „Ein Quader aus Würfeln mit 2 cm Kante hat 192 cm³ und 3 × 2 Würfel in Länge und Breite. Wie hoch?“ |
| VT3-026 | B | Die Idee nennt „ohne Ausrechnen vergleichen“, die richtige Option **rechnet** aber 180 gegen 150 aus; ein Kind rechnet ohnehin und nimmt die einzige Option mit Zahlen. | Zahlen so wählen, dass Abschätzen genügt (Grundfläche 20 gegen 21, Höhe 10 gegen 9: „A: 20 · 10 = 200, B: 21 · 9 = 189“ → Rechnen nötig) oder Begründung ohne Zahlen. |
| VT3-036 | B | **Test-Aufgabe** saeulendiagramm: zwei Divisionen und eine Subtraktion (24 : 3 − 24 : 6). Reine Anwendung des Maßstabs, Stufe 3 nur nominal. | Mit Begründung: „Wie ändern sich die Säulenhöhen, wenn man den Maßstab halbiert (1 cm für 3 statt 6 Kinder)?“ + Zahl. |
| VT3-044 | B | Die Frage „Wie viel Mal so groß ist der zweite Wert wirklich wie der erste?“ ist **ohne Verständnis der Falle lösbar**: Wer 160 : 80 rechnet, hat recht, auch ohne die ungleiche Skala zu bemerken. Bestand: „Hochachse 0, 10, 20, 50, 100 in gleichen Abständen. Was ist falsch?“ | Die Falle muss nötig sein: „Das Diagramm zeigt zwei Säulen, die erste doppelt so hoch wie die zweite. Die Achse hat die Marken 0, 10, 20, 40, 80 in gleichen Abständen. Wie verhalten sich die Werte?“ (Antwort 4 : 1 – das Bild täuscht 2 : 1 vor). |
| VT3-009 | B | Richtige Option ist **mehr als doppelt so lang** (126 gegen 60 Zeichen) und die einzige mit voller Rechnung. | Alle vier Optionen gleich lang und mit Rechnung formulieren. |
| VT3-064 | B | Richtige Option die längste (105 gegen 65), enthält als einzige „höchstens“ und Begründung; die drei falschen sind kurze Absolutaussagen. Der Test-Charakter („schwerer als bisherige Tests“) leidet, weil ein Kind die vorsichtige, ausführliche Option wählen kann. | Alle Optionen gleich vorsichtig/lang halten; Ablenker mit „höchstens/mindestens“-Formulierungen ergänzen. |
| VT3-086 | B | Richtige Option die längste (67 gegen 43), enthält die Rechnung; die falschen sind kurz. Zusätzlich dreimal Punktprobe im Lernziel (086, 087, 088) mit gleichem Verfahren und gleichem Bestandsmuster („Liegt P auf dem Graphen? Ja/Nein mit Begründung“). | Längen angleichen; 087 oder 088 durch Parameter-/Umkehr-Idee ersetzen. |
| VT3-109 | B | Richtige Option **mehr als doppelt so lang** (122 gegen 55) und die einzige mit Zahlen. Gleiche Idee wie Bestand „Stimmt die Aussage? Um 6:00 Uhr und um 12:30 Uhr bilden die Zeiger denselben Winkel“. | Längen angleichen; andere Uhrzeiten und Frage nach der **Ursache** (Stundenzeiger bewegt sich). |
| alle Auswahl-Aufgaben | B | [F] Von 49 Auswahl-Aufgaben steht die richtige Option in **34 Fällen an der längsten Stelle** (Erwartung bei Zufall ≈ 12), bei 16 mit mehr als 30 % Vorsprung (009, 023, 039, 045, 048, 049, 060, 064, 081, 082, 084, 086, 099, 109, 114, 125). Platz der richtigen Option: Index 0: 1× (VT3-088), Index 1: 16×, Index 2: **25×**, Index 3: 7×. [A] Falls die App die Optionen nicht mischt, ist Index 2/Index 1 mit 84 % ein reiner Ratevorteil. | Optionen im Bauskript mischen (feste Zufallsreihe), Länge angleichen. Prüfen, ob die App die Reihenfolge mischt (ich konnte die App nicht sehen). |
| README `Ideen je Lernziel` | B | Die Zeile „verstehen“ fasst **zwei verschiedene Lernziele** (messen.volumen/verstehen und geometrie.winkel/verstehen) zusammen; die Zahlen „was_waere_wenn 3, immer_nie 3“ stimmen für keines. Wirklich: messen.volumen/verstehen = was_waere_wenn 2 (022, 028), immer_nie 1 (023), fehler 1, transfer 2, groessenvergleich 1 (5 Kategorien); geometrie.winkel/verstehen = immer_nie 2 (120, 124), begruenden 2, was_waere_wenn 1, fehler 1, umkehr 1 (5 Kategorien). Die Aussage im Auftrag („messen.volumen/verstehen hat was_waere_wenn und immer_nie je dreimal“) ist ein Artefakt dieser Zählung. Beide erfüllen das Minimum von 5 Kategorien, und VT3-023 trägt das Etikett `immer_nie`, ist aber ein Was-wäre-wenn. | README korrigieren, `idee` von VT3-023 auf `was_waere_wenn|…` oder inhaltlich einen echten „immer/nie“ setzen. |

### C (Hinweise)

| Kennung | Grad | Befund | Vorschlag |
|---|---|---|---|
| VT3-001 | C | Test (Stufe 3) ist ein einziger Rechenschritt (2 · 3 · ½); für eine Schulaufgabe Klasse 6 leicht. Antwort 3 steht auch in 004 (Zeile 3) und 006 (Höhe 3). | Zwei Änderungen kombinieren, eine davon Prozent; oder in 004/006 andere Zahlen. |
| VT3-004 | C | Gleiche Zahlen 5/3/4 und Ergebnis 60 wie die Bestands-Schachtel („5 cm lang, 4 cm breit, 3 cm hoch“). | Anderes Zahlentripel. |
| VT3-010 | C | Tool-Hinweis Fehlalarm (siehe Werkzeuge). Gleiche Situation wie Bestand „Aquarium … Wie viele Liter?“. | Hinweis in der Abnahme als „erledigt“ führen. |
| VT3-011 | C | Antwort 40 wie VT3-008 (Test, gleiches Lernziel liter). | Würfel mit 125 l (50 cm) oder anderer Wert. |
| VT3-013 | C | Falsche Optionen sind richtige Umrechnungen; das „Fehlbild“ ist „hält für falsch“. Gültig, aber keine echte Fehlvorstellung. | Optionen als typische Fehlumrechnungen (0,25 m³ = 25 l o. ä.) belassen und zusätzlich eine falsche Umrechnung als Ablenker. |
| VT3-014, VT3-021, VT3-008 | C | `idee` nennt „Wanne“ (014), „Zeit gesucht“ (021: gefragt ist die Höhe), „und Zeit“ (008: keine Zeit). Beschriftungen stimmen nicht. | `idee` korrigieren. |
| VT3-015 | C | In der Idee gut (Verhältnis + Wurzel), aber „Breite · Breite = 9“ ohne Hinweis auf Probieren; Nähe zu Bestands-Rückwärts („Volumen 64, 2 cm hoch, Grundfläche?“) nur im Wortlaut. | Keine Änderung nötig. |
| VT3-019, VT3-021 | C | Beide „rechteckiges Becken, Höhenänderung ↔ Volumen“ im selben Lernziel (rueckwaerts); gleiche Denkfigur. | 021 durch andere Einkleidung (z. B. Eiswürfel) ersetzen. |
| VT3-020, VT3-023 | C | Gleiche Denkfigur „Schicht über der Grundfläche“ (020 rückwärts, 023 als Aussage) in zwei Lernzielen. | Eine auf eine andere Einsicht drehen. |
| VT3-027 | C | FB 17: `rechnung` „57375 : 3375“ passt zum Zahlenwert, der Text beschreibt 60 000 : 3 375 ≈ 17,8; ein Kind rechnet nicht mit 57 375. Konvention „Päckchen stehen gerade“ ist ausdrücklich genannt (gut). | `rechnung` „60000 : 3375 abgerundet“ im Text; Wert bleibt. |
| VT3-029 | C | Prozentpunkte stehen auch im Bestand (daten.darstellen, „8 Prozentpunkte“), also lehrplannah. Antwort 7,5: im Text steht nicht, ob das Eingabefeld „7,5“ mit Komma annimmt; Hinweis wie bei den Lücken fehlt. | Zusatz „(Dezimalzahl mit Komma)“. Gleiches bei 041, 053, 055, 112 (Dezimalantwort). |
| VT3-032, VT3-034, VT3-042, VT3-052, VT3-053, VT3-070, VT3-077, VT3-083, VT3-087, VT3-094, VT3-095, VT3-098, VT3-126 | C | Im Kern Rechnen nach Schema (Grundwert, Rest, Maßstab, Mittelwert, D ∩ W, Parkplatz, Steigung, Einsetzen, Tarife, Streichhölzer, Summe/Differenz) mit Stufe-2/3-Etikett. Keine falsche Aufgabe, aber kein Verstehens-Anteil über das Schema hinaus. | Siehe Abschnitt „Verstehen wirklich geprüft?“. |
| VT3-043 | C | `idee` korrekt, Test gut gedacht; aber Denkfigur dreimal im Lernziel (043, 046, 047). | siehe 046. |
| VT3-039, VT3-045, VT3-049, VT3-060, VT3-081, VT3-082, VT3-084, VT3-099, VT3-125 | C | Richtige Option deutlich länger (siehe Sammelbefund Optionslänge). | Längen angleichen. |
| VT3-057 | C | „Turnerin … 11 Punkte in der fünften Wertung“: Wertungen im Turnen bewegen sich bis 15; plausibel. Test (Stufe 3) ist Schema „Summe − Rest“. | Optional Begründungsteil. |
| VT3-058 | C | Gute Aufgabe; Antwort 10 wie VT3-059 (siehe dort). | – |
| VT3-063 | C | Zweite Lücke „insgesamt“ ist 70 · 5 und gibt nichts her; `idee` nennt „Spannweite“, die nicht gefragt wird. | Zweite Lücke streichen oder Spannweite einbauen. |
| VT3-068 | C | Mit VT3-064 und VT3-067 drei Aufgaben „Wertemenge hat weniger Elemente als D“ im Lernziel mengen. | 068 auf andere Idee drehen. |
| VT3-069, VT3-075 | C | Bruchterme mit Definitionslücke: stehen als Bonus/Übung auch im Bestand (`f(x) = 10/x`, `4/(x−2)+1`, `−8/x`), also vertretbar für M8 1. | – |
| VT3-072 | C | Antwort 7 ist die zweite Stelle von VT3-071 (Test). Gute Aufgabe (Differenz über die Steigung). | Andere Werte wählen, sodass die Differenz nicht 7 ist (z. B. f(a) = 8, f(b) = −2: Differenz 5). |
| VT3-073 | C | Tool-Hinweis Fehlalarm (siehe Werkzeuge). Bestand-Muster („Kim berechnet f(−2) …“) nur im Format. | – |
| VT3-074 | C | Gleiche Einkleidung (Pflanze, h(t) = 12 + 1,5t) wie Bestandsübung („Pflanze in 30 cm hohem Topf, nach 8 Wochen?“), Rückwärtsrichtung. | Andere Einkleidung. |
| VT3-085, VT3-087 | C | Antwort 3 in beiden (punkt_graph); 085 Test. | Zahlen in 087 ändern. |
| VT3-097 | C | Option [3] („verliert täglich 40 Liter und ist nach 8 Tagen leer“) ist in sich nicht schlüssig; die Fehlbildbeschreibung („zusätzlich die Leerung eingebaut“) erklärt keine Fehlvorstellung. | Option [3] als „Anfangswert 8 Liter, verliert täglich 40 Liter“ ohne Zusatz. |
| VT3-102 | C | Antworten 65°/115° kehren in 104 (65) und 105 (alle Optionen) wieder (siehe 105). | Andere Zahlen. |
| VT3-104 | C | Spitzer Winkel zwischen k und h ist 65 auf beiden Seiten von g gleich – eindeutig. | – |
| VT3-106 | C | Bestandsübung „kleinerer Winkel um 7:00 Uhr“ (150°) verrät die Ausgangsinformation. Die Fehlbilder 10 („Stunde verdoppelt“) und 2 sind schwach erklärt. Eindeutigkeit [F]: nur 5:00 Uhr (1–12 geprüft). | – |
| VT3-107, VT3-108, VT3-112 | C | Die Konvention „Stundenzeiger wandert gleichmäßig, 0,5° je Minute“ steht nur im Lösungsweg, nicht im Text. In 112 liefert die gröbere Annahme (Stundenzeiger genau auf der 3) 0° statt 7,5°. Bestand lehrt die Konvention (9:20 Uhr → 160°), daher vertretbar. | In 112 Satz „Der Stundenzeiger wandert gleichmäßig weiter.“ |
| VT3-111 | C | FB 12:15 Uhr („Stundenzeiger auf der 12 gelassen“) erklärt 82,5° nicht (so wären es 90°). Richtig bleibt die Option eindeutig; auch die grobe Annahme (Stundenzeiger auf 1 bei 1:05) führt zur selben Antwort. | Text: „den Stundenzeiger bei 12:15 Uhr nicht weitergewandert gerechnet: 90°“ (anderer Wert) oder Text kürzen. |
| VT3-117 | C | FB 3 „durch den größten Teil geteilt“ (90 : 30) ist kein typischer Fehler. Lösung 5 eindeutig (Summenfolge 6, 18, 36, 60, 90 per Schleife). | FB 6 (90 : 15 ?) oder „nur 6° bis 90° aufgezählt“. |
| VT3-118 | C | Beweis-Denken („mindestens einer ≤ 30°“) am oberen Rand von Klasse 5; Aussage und Gegenbeispiele per Aufzählung bestätigt; Teilwinkel positiv ausdrücklich im Lösungsweg („lückenlos in drei Teile“). | Im Text „positive Teilwinkel“. |
| VT3-120, VT3-124 | C | Gleiche Denkfigur („aus spitz/stumpf auf die Art des Ergebnisses schließen“) zweimal im Lernziel verstehen (Winkel). | 124 auf anderes Thema drehen. |
| VT3-121 | C | Setzt das Geodreieck mit zwei Skalen voraus; ohne Bild und ohne Gerät ist der Gedanke „falsche Skala“ nur Wissen, kein Messen. Eindeutig (118°). | – |
| VT3-082 | C | Option [3] hat eine **wahre** Schlussfolgerung („keine Gerade“) mit falscher Begründung; ein Kind, das nur die Folgerung liest, kann zögern. Aufgabe sonst eindeutig. | Option [3] mit falscher Folgerung („ist eine Gerade, denn alle y-Werte sind positiv“) formulieren. |
| VT3-084 | C | Optionen [1], [3] beginnen mit „Jonas hat nicht recht“ (wahr) – wie bei 082 nur durch die Begründung falsch. | Wie 082. |

## Ohne Bild verständlich?

[F] In der Runde gibt es kein `grafik`-Feld. Fast alle Beschreibungen sind vollständig (Achsenbeginn, Maßstab, Zahlenwerte; Winkelnamen α, β, γ, δ „der Reihe nach“ mit „α gegenüber γ“ in 101/102; Wertetabellen mit allen Punkten). Unklar bzw. verbesserungsfähig ohne Zeichnung:

| Kennung | Problem | Vorschlag |
|---|---|---|
| VT3-048 | „Beide Hochachsen“ bei einem Diagramm (siehe B). | „Die Hochachse beginnt bei 0.“ |
| VT3-044 | Ungleiche Skala nur als Wortbeschreibung („gleiche Abstände“, Marken 0, 10, 20, 40, 80, 160); verständlich, aber das Kind muss sich eine Achse vorstellen. | Zusatz „Der Abstand zwischen zwei benachbarten Marken ist immer gleich lang.“ |
| VT3-119 | „der zweite Strahl (von [AB] aus gezählt)“: eindeutig, aber nur mit dem Bild im Kopf. | Zusatz „Die beiden Strahlen liegen innerhalb des Winkels bei A, der erste näher an [AB].“ |
| VT3-099, 103, 105 | Winkel „der Reihe nach“: Drehrichtung unerheblich, eindeutig. | – |
| VT3-121 | Geodreieck (Skalen) ohne Gerät. | – |
| VT3-110, 106, 109, 111, 112 | Uhren nur durch Uhrzeiten beschrieben: ausreichend und eindeutig. | – |

[A] Alle übrigen Aufgaben, auch die Säulendiagramm-Aufgaben (036–049), kann ein Kind ohne Zeichnung sicher verstehen, weil jede Säulenhöhe in cm oder die Zahlen ausdrücklich genannt sind.

## Verstehen wirklich geprüft?

**Gut (Verstehen über das Schema hinaus):** 002 (⅛ und nicht ½), 005, 007, 009, 013, 018, 020, 022, 023, 027, 028, 033, 039, 045, 048, 049, 051, 054, 056, 058, 060, 064, 065, 066, 072, 076, 081, 082, 084, 090, 092, 099, 103, 105, 109, 111, 112, 116, 120, 121, 122, 124, 125.

**Im Kern Rechnen (kein oder nur nominelles Verstehen), mit Stufe-Etikett 2/3:** 008, 012, 014, 019, 021, 025, 026, 029, 032, 034, 035, 036, 038, 041, 042, 044, 050, 052, 053, 057, 061, 062, 063, 070, 077, 083, 087, 089, 091, 094, 095, 096, 098, 102, 104, 115, 119, 126. [A] Von diesen sind 008, 012, 025, 026, 036, 044, 050 und 062 ein klarer Mangel gegenüber „schwerer als bisherige Tests“ (B); die übrigen sind Sachaufgaben mit Modellaufstellen und akzeptabel.

**Ideen-Kategorien je Lernziel wirklich verschieden?**

| Lernziel | Urteil |
|---|---|
| quader | 4 von 7 Aufgaben (001, 002, 003, 005) = „Kantenfaktoren multiplizieren“. Kategorien nur formal verschieden. |
| liter | gut verschieden (Brücke, Begründen, Fehler, Umkehr, zwei Wege, Darstellung, Transfer); zwei Wege (012) nur nominell. |
| rueckwaerts | 015–018 „Höhe/Breite aus Volumen“, 019/021 „Becken“: nur 020 und 018 (Größenvergleich) sind eigene Gedanken. |
| verstehen (messen.volumen) | 5 Kategorien, aber `immer_nie` bei 023 falsch beschriftet; 025 reines Rechnen. |
| relative_haeufigkeit | gut gemischt; 029/033 gleiche Denkfigur. |
| saeulendiagramm | 036, 038, 039, 041, 042: Höhe mal Maßstab; verschieden nur in der Einkleidung. |
| irrefuehrend | 043/046/047 dreimal Achsenbeginn; 045, 048, 049 gut. |
| mittelwert | 050, 051, 053, 054, 056 alle „neue/veränderte Werte → neuer Mittelwert“. Fachlich inhaltlicher Kern des Lernziels, aber nicht fünf Denkfiguren. |
| mittel_rueckwaerts | 057, 059, 060, 061, 062, 063 = sechsmal dieselbe Rechenfigur (siehe B zu 062). |
| mengen | gut (064/067/068 teils gleiche Idee). |
| stelle | gut. |
| graph_lesen | 078/079 gleich (Term aus Punkten). |
| punkt_graph | 086/087/088 dreimal Punktprobe. |
| sachzusammenhang | gut. |
| kreuzung | 099/103 (Sonderfall 90°) und 102/105 (gleiche Zahlen). |
| uhr | gut (Zusammenhang Zeiger, Rückwärts, Zählen, Fehler). |
| figuren | 113, 114, 117, 118, 119 und 116 = „Teilwinkel ergeben das Ganze“; nur 115 (Torte) und 116 sind andere Einkleidungen. Im Kern 6 von 7 gleich. |
| verstehen (winkel) | 120/124 gleich; sonst gut. |

## Lehrplan (M5 2, M6 2, M6 3, M8 1; Klasse nach `themenliste.json`)

[F] Prozent und Prozentpunkte sind in M6 3 („Prozentrechnung, Daten und Diagramme“) enthalten; das Bestandsmaterial zu `daten.darstellen` verwendet Prozentpunkte. VT3-029/032/043/045/046 sind damit lehrplannah.

| Kennung | Urteil |
|---|---|
| VT3-110 | Aufgabe liegt über Klasse 5 (Relativbewegung der Zeiger); siehe B. |
| VT3-118 | Beweisdenken am oberen Rand von Klasse 5 (nur Aufgabe des Typs „es gilt immer“, kein Wissen aus höheren Klassen). Vertretbar. |
| VT3-055 | gewichteter Mittelwert (Summe/Anzahl) Klasse 6 vertretbar; Doppelung mit dem Bestand ist das Problem. |
| VT3-069, VT3-075 | Bruchterme/Definitionslücke: stehen im Bestand (`bonus`/`uebung`, `f(x) = 10/x`, `4/(x − 2) + 1`); in M8 1 vertretbar. |
| VT3-071, VT3-085 | x² und (x − 3)² = 16 / b · x² − 5: wie im Bestand (`f(x) = x² − 7`); kein Stoff höherer Klassen, solange „zwei Lösungen von x² = 16“ im Bestand vorkommt. |
| Konventionen | 0,5° je Minute (107, 108, 109, 111, 112) steht nur in Lösungswegen bzw. Optionen, nicht im Aufgabentext (siehe C). VT3-027 „Päckchen gerade“ ausdrücklich im Text (gut). VT3-125 (Schenkellänge) ist Klasse 5. |
| Winkelsummen im Dreieck | nirgends verwendet (korrekt, Klasse 7). |

## Doppelungen / Nähe zum Bestand

[F] Vom Werkzeug **nicht** erkannt (zu wenig Wortüberlappung), von Hand bestätigt:

| VT3 | Bestandsaufgabe (Datei) | Nähe |
|---|---|---|
| 055 | `themen/daten.kennwerte.json`: 6a (20 Kinder) 12 Punkte, 6b (30 Kinder) 17 Punkte, Mittelwert aller 50 | gleiche Struktur und gleiche Gruppengrößen |
| 050 | `themen/daten.kennwerte.json`: 4 Kinder im Mittel 15 Punkte, weiteres Kind 3 Punkte | gleiches Schema |
| 059 | `themen/daten.kennwerte.json`: Mittelwert von vier Zahlen 7,5, drei bekannt | gleiche Schablone |
| 089 | `themen/funktionen.grundbegriffe.json`: A(1\|3), B(3\|7), m und t | gleiche Punkte |
| 037 | `rollend-4/d1.json`: 1 cm für 4 Kinder, 7 cm, „7 : 4“ | gleicher Fehler, gleiche Höhe |
| 100 | `themen/geometrie.winkel.json`: halb so groß wie der Winkel, der ihn zu 180° ergänzt; 2-mal so groß wie Nachbarwinkel | gleicher Kern |
| 115 | `themen/geometrie.winkel.json`: Torte in 10 Stücke → 36° | gleiche Frage, gleiche Antwort |
| 113 | `themen/geometrie.winkel.json`: Rechteck, drei Teile, 30° und 10° | gleiche Situation |
| 123 | `rollend-4/ge3.json`: Quadrat/Eckwinkel 180°, 180° : 3 = 60° | gleicher Fehler |
| 116 | `themen/geometrie.winkel.json`: sieben Aufgaben „Rechteck, Diagonale, Beide Teile 45°?“ | gleiche Einsicht |
| 110 | `themen/geometrie.winkel.json`: Zeiger übereinander, 12:00–18:00 | gleiches Verfahren |
| 065 | `themen/funktionen.grundbegriffe.json`: x² + 1 / x² − 4, „Welche Aussage über die Funktionswerte“ | gleiche Optionstypen |
| 067 | Bestand `bonus` (x² mit D = {−3 … 3}, Zahl der Elemente von W) und `rollend-13` (Symmetrie) | gleiche Idee (Wertemenge kleiner als D) |
| 071 | `themen/funktionen.grundbegriffe.json`: f(x) = 9 bei x² − 7 | gleiche Idee (Autor räumt ein) |
| 079, 093, 078 | `themen/funktionen.grundbegriffe.json`: fünf „Wertetabelle → Term“ | gleiche Schablone |
| 044 | `themen/daten.darstellen.json`: Hochachse 0, 10, 20, 50, 100 in gleichen Abständen | gleiche Idee |
| 109 | `themen/geometrie.winkel.json`: Um 6:00 und 12:30 Uhr derselbe Winkel? | gleiche Idee |
| 074 | `themen/funktionen.grundbegriffe.json`: Pflanze h(t) = 12 + 1,5t | gleiche Einkleidung |
| 004 | `rollend-14/messen.volumen.json`: Schachtel 5 · 4 · 3 mit Einwürfeln | gleiche Maße (anders gefragt) |

Von Hand verglichen (Test-Aufgabe und je zwei weitere je Lernziel) und **in Ordnung**: VT3-001/002/028 gegenüber Bestand „eine Kante verdoppelt“ (andere, erweiterte Denkfigur), VT3-015 gegenüber „Volumen 64, 2 cm hoch“, VT3-022, VT3-064, VT3-078, VT3-085, VT3-092, VT3-099, VT3-106, VT3-120. Die Aufgaben 071, 015, 059, 106, 111 aus dem Prüfauftrag: 071 B (siehe oben), 015 C, 059 B, 106 C, 111 in Ordnung (Bestand fragt Winkel zu einer Uhrzeit, VT3-111 vergleicht).

Innerhalb der Runde gibt es **keine zwei Aufgaben mit gleichem Text**. Gleiche Sollwerte im Lernziel: liter 40 (008, 011), kreuzung 65 (102, 104), figuren 36 (115, 119), mengen 3 (067, 069, 070), mittel_rueckwaerts 10 (058, 059), punkt_graph 3 (085, 087), quader 3 (001, 004, 006), verstehen/winkel 120 (123, 126), stelle 7 (071, 072).

## Fehler-Detektive (19: 004, 010, 016, 024, 031, 037, 046, 052, 059, 067, 073, 080, 087, 094, 101, 108, 113, 114, 123)

[F] Bei 18 von 19 genau ein erster Fehler; jede Folgezeile rechnet mit dem falschen Wert konsistent weiter (z. B. 101 Zeile 3 „δ = 48°“ ist mit γ = 132° richtig weitergerechnet, die Summe 360° bleibt wahr; 024 Zeile 3 „3 000 m³ = 3 000 000 l“ ist richtig umgerechnet). **VT3-067 ist die Ausnahme (A).** Der verlangte Wert ist überall eindeutig (VT3-073: x = 3, eine Zahl).

## Was ich NICHT prüfen konnte

- **App und Anzeige:** ob die App Optionen mischt, Dezimalkomma im Zahlfeld akzeptiert, Lückenfelder und Einheiten (`einheit`) zeigt; Eingabeformat von „7,5“, „22,5“, „2,4“ und negativen Lückenwerten (−1 in 071, −3 in 075).
- **Amtlicher Lehrplan:** nur gegen `inhalte/themenliste.json` und Bestand gedacht, nicht gegen das offizielle LehrplanPLUS.
- **Doppelungen** gegen alle früheren Runden außerhalb von `inhalte/themen/` und den `rollend-*`-Ordnern mit diesen Einheiten; die Schwesterrunden VT1A/VT1B/VT2 decken andere Einheiten ab.
- **Rechtschreibung** nur durch Lesen, nicht maschinell.
- **Schwierigkeit 2–4 Minuten** ist eine Schätzung ohne Kinder; besonders VT3-110, VT3-118, VT3-006, VT3-015 und VT3-096 könnten länger dauern.
- Keine Datenbank, keine Council-Werkzeuge, nichts eingespielt.
