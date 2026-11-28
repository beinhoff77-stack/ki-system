# Vorprüfung Runde VT2 (unabhängig, alle 133 Aufgaben VT2-001 bis VT2-133)

Stand 28.11.2026. Prüfer: unabhängig vom Autor, keine Aufgabe geändert. Eigene Rechnung: `vorpruefung_rechnen.py` (liegt neben dieser Datei; Aufruf `python3 -I inhalte/mathe-profi/vtest-2/vorpruefung_rechnen.py` im Wurzelordner). Alle 133 Aufgaben mit Text, Optionen, Fehlbildern und Lösungsweg von Hand gelesen.

Kennzeichnung: **[F]** = Tatsache (nachgerechnet, im Repo gelesen, vom Werkzeug ausgegeben) · **[A]** = Annahme oder Einschätzung.

## Gesamturteil: bereit für die Gegenprüfung **nach Korrektur**

[F] Keine Sollantwort ist rechnerisch falsch. Alle 70 Zahl- und Lücken-Aufgaben habe ich mit eigener Formel bzw. Aufzählung (exakte Brüche, Zählschleifen) neu gerechnet: 0 Abweichungen. Bei den 62 Auswahl-Aufgaben habe ich jede Möglichkeit von Hand entschieden, 15 zusätzlich per Skript (Terme einsetzen, Rundungen, Winkelbedingung, römische Regel): die markierte Option stimmt überall, es gibt keine zweite vertretbare, **außer** den unten genannten Grenzfällen. Alle 259 Fehlbild-Rechnungen ergeben ihre gespeicherte Antwort.

[A] Trotzdem nicht ohne Korrektur einspielbar: ein Befund A (Mehrdeutigkeit durch fehlende Angabe „einfache Verzinsung“), 56 Aufgaben mit Befund B, davon vier Fehlbild-Erklärtexte, die nicht zur Zahl führen, rund 25 Doppelungen mit dem Bestand (das Werkzeug erkennt sie nicht), mehrere „Antwort aus Nachbaraufgabe ablesbar“ und ein großer Block „im Kern Rechnen nach Schema“. Der Auftrag „Verstehen, schwerer als bisherige Tests“ ist bei etwa 50 von 133 Aufgaben nur formal erfüllt (Abschnitt „Verstehen wirklich geprüft?“). Das ist nachbesserbar, ohne dass die Runde neu geschrieben werden muss.

| Zahl | Wert |
|---|---|
| geprüfte Aufgaben | 133 |
| Sollantwort nach eigener Rechnung richtig und eindeutig | 132 (VT2-025 nur unter einer Zusatzannahme eindeutig) |
| Befund A (muss korrigiert werden) | 1: VT2-025 |
| Befund B (sollte korrigiert werden) | 56 (Liste in der Tabelle) |
| Befund C (Hinweis) | 53 |
| Aufgaben ganz ohne Befund | 23 (003, 004, 007, 011, 017, 019, 020, 021, 026, 039, 083, 088, 089, 094, 095, 098, 105, 109, 115, 117, 129, 130, 132) |
| Tests (19), die ich für Stufe 3 halte | 11; für Stufe 2 halte ich 22, 50, 71, 78, 92, 113, 120, 127 |

(Zählung nach dem jeweils schwersten Befund je Aufgabe.)

## Werkzeuge, selbst ausgeführt

| Werkzeug | Ergebnis |
|---|---|
| `python3 -I tools/vtest_pruefen.py --runde 2` | [F] 133 Aufgaben, 5 Einheiten, 19 Lernziele mit je 1/3/3; „OK – keine Fehler“; 3 Hinweise „Text verlangt Runden, Feld runden fehlt“ bei VT2-106, -112, -118. |
| Die 3 Hinweise: Fehlalarm? | [F] Ja, Fehlalarm. 106 und 112 zählen bzw. bilden Differenzen ganzer Zahlen (100 und 999); 118 fragt den Unterschied zweier ganzer Zahlen (3). Gerundet wird nur im Aufgabentext (Voraussetzung), das Ergebnis ist exakt. Ein Feld `runden` würde das Prüfwerkzeug nur beruhigen, nicht die Aufgabe verbessern. Hinweis: bei 106/112 verrät „gerundet … beide 8 000“ nichts; bei 118 muss das Kind genau rechnen (kein Näherungswert), daher kein Rundungsrisiko. |
| `python3 -I inhalte/mathe-profi/vtest-2/gegenrechnung.py` | [F] „133 Aufgaben gelesen, 0 Abweichungen“. Das Skript stammt vom Autor; mein eigenes Skript bestätigt unabhängig. |
| mein `vorpruefung_rechnen.py` | [F] 70 Zahl-/Lücken-Aufgaben: 0 Abweichungen. 15 Auswahl-Aufgaben per Code bestätigt. Römische Regel per Code: VC regelwidrig, CDXC/MCMXC/XLIV regelgerecht; DCCCC und MIM regelwidrig; MCMXCIX regelgerecht. Anzahl-Punkte Kreis/Gerade wächst mit r nie fallend (relevant für VT2-077). Platz der richtigen Möglichkeit bei 62 Auswahlaufgaben A 17, B 16, C 12, D 17 (wie README). **Richtige Möglichkeit ist in 27 von 62 Aufgaben die eindeutig längste** (Zufall wären etwa 16); in 13 ist sie mindestens das 1,3-Fache der mittleren Länge der falschen. README sagt „etwa 14 abgemildert“; das reicht nicht. |
| Doppelungs-Suche (eigen) | [F] Ähnlichkeitssuche (Wortmenge + Zahlenmenge) gegen alle JSON-Texte der Einheiten in `inhalte/themen/` und `inhalte/mathe-profi/rollend-*`; dann die Treffer von Hand gelesen (Abschnitt „Doppelungen“). Eine Bauart ohne gleichen Wortlaut (z. B. VT2-112) findet das Werkzeug des Autors nicht. |

## Befundtabelle

Schweregrad: A = fachlich falsch/mehrdeutig, muss korrigiert werden; B = sollte korrigiert werden; C = Hinweis. Doppelungen verweisen auf Fundstellen im Bestand (Pfad relativ zu `inhalte/`).

| Kennung | Grad | Befund | Korrekturvorschlag |
|---|---|---|---|
| VT2-025 | A | Mehrdeutig. 18 Monate sind 1,5 Jahre; der Text sagt nicht, dass die Zinsen nach dem ersten Jahr nicht mitverzinst werden. Mit Zinseszins wären es 91,50 € statt 90 €. Die Bestandsübung `themen/finanzen.zinsen`: „3 000 € liegen 1 1/2 Jahre zu 2 % Jahreszins, die Zinsen werden jedes Jahr abgehoben“ schreibt die Klarstellung eigens hin. Zudem liegt die Etappe unter „Kürzere Zeit“; ein Zeitraum über einem Jahr fällt aus dem Rahmen. Fehlbild 20 € (`60 : 3`, „durch 3 geteilt statt 8/12“) ist ohnehin schwach begründet. | Text ergänzen („die Zinsen werden nicht mitverzinst“) oder 18 durch 9 Monate ersetzen (Soll 45 €, Fehlbild 60 · 9 = 540). Fehlbild 20 € (`60 : 3`) durch ein erklärbares ersetzen, z. B. 60 · 8 : 3 = 160 („durch 3 statt durch 12 geteilt“). |
| VT2-001 | B | Doppelung als Test: `themen/finanzen.zinsen` hat „1 000 € Sparkonto zu 1 % und gleichzeitig 1 000 € Kredit zu 8 %. Wie viel Euro verliert er in einem Jahr?“; 001 ist dieselbe Denkfigur mit Auswahl. Abgrenzung im Feld ist deshalb nicht haltbar. Stufe 3 überhöht (eine Differenz). | Beträge verschieden wählen (Kredit 2 000 € zu 6 %, Guthaben 5 000 € zu 1,2 %) und Optionen so, dass „Kredit ist immer teurer“ scheitert. |
| VT2-002, 006, 012, 014 | B | Im Kern Rechnen: 002 drei Zinsberechnungen, 006 Gleichsetzen und Teilen, 012 dreimal Faktor, 014 zerlegt 3,5 % (`zwei_wege` nur formal; beide Wege sind Rechnen). 002 ≈ `mathe-profi/rollend-8/finanzen.zinsen` („Familie: Kredit 2 000 € zu 6 % und Sparkonto 500 € zu 1 %“). | Jeweils eine Entscheidung verlangen, z. B. 002: „Zahlt die Familie netto oder bekommt sie?“ mit Begründung; 012: aus den drei Ergebnissen die Regel „5-facher Zinssatz → 5-fache Zinsen“ als Auswahl. |
| VT2-005 | B | Doppelung: `themen/finanzen.zinsen` „Du leihst dir 3 000 €, zahlst nach einem Jahr 3 270 € zurück. Wie viel Zinsen?“ und „Ein Kind leiht sich 400 €, zahlt 420 € zurück. Wer bekommt die 20 €?“. Stufe 2 trivial; richtige Option ist die ausführlichste. | Ersetzen, z. B. Rückzahlung in zwei Raten mit Zinsen auf den Rest, oder Option zur Rollenfrage mit Gegenbehauptung „Zinssatz = 480“. |
| VT2-009 | B | Der Text verrät die Strategie („Eine der vier Zahlen ist richtig, die anderen entstehen durch Kommafehler“): 150 ist die einzige Zahl der Größenordnung ≈ 2,5 % von 6 000. Bestand hat dieselbe Rechnung (`themen`: „Berechne die Jahreszinsen für 3 200 € bei 2,5 %“). | Satz streichen und eine Schätzfrage stellen („Ohne zu rechnen: Welche Zahl kann nicht stimmen, und warum?“). |
| VT2-015 | B | Zufallstreffer: Sollwert 20 000 € ist zugleich das alte Kapital (600 : 0,03). Wer nur das alte Kapital berechnet und nicht die Erhöhung, hat die „richtige“ Zahl; es gibt kein Fehlbild dafür. | Zahlen ändern (600 € bei 4 % → 2,5 %: 15 000 → 24 000, Erhöhung 9 000) und Fehlbild „altes Kapital“ aufnehmen. |
| VT2-016 | B | Option [1] („doppelt so groß, auch wenn die Zinssätze verschieden wären“) widerspricht der Voraussetzung; ihr erster Teil ist für die gegebene Lage richtig, also behaupten [0] und [1] dasselbe Ergebnis und nur die Begründung unterscheidet. Option [0] ist die längste. | [1] durch eine Behauptung mit anderem Ergebnis ersetzen („A hat 4-mal so viel Kapital, weil doppelte Zinsen doppeltes Kapital und doppelte Zeit brauchen“), [0] kürzen. |
| VT2-023, 024, 027 | B | Doppelungen in `themen/finanzen.zinsen`: 023 ≈ „Vom 1. März bis zum 1. September liegen 2 400 € zu 3 % …“; 024 ≈ „Was bringt mehr Zinsen: 3 000 € für 8 Monate zu 3 % oder 3 000 € für 1 Jahr zu 2 %?“ und „6 Monate zu 4 % oder 8 Monate zu 3 %“; 027 ≈ „Ein Kapital bringt bei 4 % in einem halben Jahr 30 € Zinsen. Wie groß ist das Kapital?“ plus „Für 7 Monate 14 € …“. | Andere Konstellation (024: Gebühr oder Laufzeit mit Vergleich, 023: Beginn/Ende mit Teilmonat und Begründung der Zählweise, 027: nur den Zeitanteil als Brücke abfragen). |
| VT2-029, 031, 033, 035, 042 | B | Im Kern Zusammenfassen nach Schema (Autor nennt S3): 029 und 032 Standardvorzeichenfehler (≈ `rollend-7`/`rollend-13` Kim-Fehlerzeilen), 031 und 035 und 042 „Sachverhalt → Summe“ ohne eigene Modellbildung, 033 vier Terme ausrechnen und vergleichen. 031 ≈ Bestand „Umfang 9x + 5y, zwei Seiten gegeben“. | 033 als echte Umkehr („Wie viele verschiedene Terme der Form … ergeben …?“) oder Gegenbeispiel-Frage; 031/035/042: Term erst aufstellen lassen und danach eine Eigenschaft begründen lassen (z. B. „Warum ist der Umfang für jedes ganzzahlige a ungerade?“). |
| VT2-034 | B | Fehlbild-Erklärtext passt nicht: antwort −8 (`−4 − 4`) beschrieben als „wie 4 − (−4) gerechnet“; 4 − (−4) ergibt +8. | Beschreibung: „von −4 noch einmal 4 abgezogen: −4 − 4“. |
| VT2-038 | B | Fehlbilder vertauscht: Für antwort 9 (`7 + 2`) steht „das Minus vor der Klammer vergessen“; wer das Minus vergisst, rechnet 7 + k = 2 und kommt auf k = −5 (das ist das Fehlbild „−5“). Antwort 9 entsteht durch „k − 7 = 2“. Zudem ≈ Bestand `themen`/`rollend-15` „Für welche Zahl a ist 3(x + a) äquivalent zu 3x + 12?“ / „13(x + 4) und 13x + k“. | 9: „7 − k = 2 falsch als k − 7 = 2 umgestellt“; −5: „Minus vor der Klammer vergessen: 7 + k = 2“. Aufgabe selbst mit anderer Denkfigur (z. B. Einsetzprobe, die Jonas’ Fehler aufdeckt). |
| VT2-040 | B | `zwei_wege` nur formal; beide „Wege“ sind das Ausrechnen derselben Zahl; Soll „0x + 1“ lässt Kinder zweifeln, ob „0“ gemeint ist. | Frage nach dem Zusammenhang („Ben setzt x = 0 ein und bekommt 1. Folgt daraus, dass Annas Ergebnis 1 ist? Begründe“) als Auswahl. |
| VT2-043, 047 | B | Gleiche Denkfigur („gleiche Werte bei einigen Zahlen beweisen nichts“), dazu Doppelung mit Bestand: `themen/terme.umformen` „Lisa sagt: x + x + x und x · x · x sind äquivalent, denn für x = 0 …“, `rollend-15` „Kim behauptet: 3x + 6 und 9x sind äquivalent“, `rollend-13` „Kim prüft … x² + 2 und 3x“. Außerdem **Antwort ablesbar**: die richtige Option von 047 formuliert die Lösung von 043. Beide korrekte Optionen sind die längsten. [A] Bei 047 ist „drei gleiche Ergebnisse reichen nicht“ für lineare Terme streng genommen falsch (zwei Stellen genügen); gemeint ist der allgemeine Fall, steht aber nicht da. | 047 durch eine andere Frage ersetzen (z. B. zu einem vorgegebenen Termpaar, das bei x = 1 und x = 2 übereinstimmt, ein Gegenbeispiel suchen lassen). Optionen von 043 kürzen. |
| VT2-044, 045, 049 | B | Drei von sieben Aufgaben mit `parameter`-Etikett sind dieselbe Rechnung (Koeffizienten vergleichen). 044 ≈ Bestand „2x + 1 und x + 2 sind nicht äquivalent. Für genau eine Zahl x haben sie trotzdem denselben Wert. Für welche?“ (`themen/terme.umformen`), 045 ≈ „Für welche Zahl a ist 3(x + a) äquivalent zu 3x + 12?“ und rollend-15 „13(x + 4) und 13x + k“. 044 lässt sich durch Probieren der vier Optionen lösen. | 045 oder 049 ersetzen; 044 so stellen, dass Gleichsetzen nötig ist (Optionen mit Brüchen/negativ), oder streichen. |
| VT2-048 | B | Vier Terme ausrechnen: Rechnen nach Schema, als Stufe 3 überhöht (Stufe 2). Ähnlich Bestand „Welche beiden Terme sind äquivalent? A: 2(x − 3) + x …“. | Stufe 2 eintragen oder nur mit Einsetzzahlen begründen lassen, warum zwei Einsetzungen genügen. |
| VT2-050 | B | Prüfen durch Ausmultiplizieren aller vier Zeilen: Rechnen; als Test Stufe 3 überhöht (Stufe 2). | Als Begründung stellen („Welche Zeile ist falsch, und woran erkennt man es ohne Ausmultiplizieren aller Zeilen?“, z. B. am Mittelglied) oder Stufe 2. |
| VT2-051, 053 | B | Doppelungen: 051 ≈ `rollend-14/terme.umformen_teil2` „Rechteck mit Fläche 6x² + 9x und Seite 3x“; 053 ≈ `themen/terme.umformen` „Berechne geschickt: 37 · 13 + 37 · 87“ (gleicher Faktor 37, gleiches Schema); 053 gibt außerdem das Verfahren vor. | 053 ersetzen (z. B. gemeinsamen Faktor selbst finden lassen: Auswahl „Welche Umformung von 18 · 25 + 18 · 75 ist geschickt, und warum?“), 051 mit Parameter. |
| VT2-054 | B | Richtige Option ist als einzige ohne Gleichung formuliert („Kein Faktor außer 1 …“), die drei falschen folgen derselben Bauart: Mustererkennung statt Prüfen. „Kein Faktor außer 1“ meint ganzzahlig; bei rationalen Faktoren lässt sich immer etwas herausziehen. | Alle Optionen als Gleichung formulieren, in der richtigen eine Probe: „Es gibt keine Ausklammerung, denn 5 enthält weder 2 noch x“; „ganzzahlig“ ergänzen. |
| VT2-055 | B | Nicht eindeutig: „k ist eine positive Zahl kleiner als 20“ lässt k = 4,5 oder k = 13,5 zu; erst „ganze Zahl“ macht „größter gemeinsamer Faktor 9x“ eindeutig (k = 9). | „k ist eine positive ganze Zahl kleiner als 20“. |
| VT2-056 | B | Schema (Fläche als Produkt, Faktor „Breite“ steht im Text vor); Fehlbild 12 beschreibt „Fläche (12 m²)“, richtig wäre 12x m² (3 · 4x). | Beschreibung korrigieren; Aufgabe: Gesamtlänge/Breite vertauschen lassen („Welche Breite hat das Beet, wenn Fläche 20x² + 12x und Länge 5x + 3“). |
| VT2-058, 061, 063 | B | Doppelungen: 058 ≈ `themen/terme.umformen` „Ergänze … x² + 12x + □ = (x + □)²“; 061 ≈ „Rechne geschickt mit einer binomischen Formel: 49 · 51“, „51² = (50 + 1)²“ und `rollend-13` „Berechne 47² auf zwei Wegen“; 063 ≈ `rollend-14` „Quadratisches Beet 4x² + 20x + k, Seitenlänge 2x + m“ (gleiche Zahlen 4x² + 20x). 061 gibt das Verfahren vor (49² geht auch direkt). | 058: Umkehrung mit drei Lücken und Begründung; 061: ohne Verfahrensvorgabe „Warum liegt 49² genau 99 unter 50²?“; 063: andere Zahlen (9x² + 12x + 4). |
| VT2-065, 068 | B | Nahezu dieselbe Aufgabe: C liegt über der Mitte M im Abstand r, y = 4 in beiden (065 Zahl, 068 Auswahl C(4 | 4)); wer 065 gesehen hat, löst 068. Dazu alle Auswahlpunkte von 068 mit x = 4: das Kind muss nur „halbe AB“ erkennen. | 068 mit Punkten abseits der Mittelsenkrechten x = 4, nur einer auf dem Kreis um M(4 | 0) mit r = 4 (z. B. C(4 + 2√… ) vermeiden; ganzzahlig: Kreis um M(4 | 0) mit r = 5 über A(−1 | 0), B(9 | 0), richtiger Punkt C(1 | 4) oder C(7 | 4)); Zahlen vor Übernahme nachrechnen. |
| VT2-069 | B | Richtige Option ist die einzige „Richtig“ gegen drei „Falsch“; wer die Behauptung kennt, wählt sie ohne Begründung. Dazu länger. | Zwei Optionen „Richtig, weil …“ mit falscher Begründung ergänzen. |
| VT2-070 | B | Der Text liefert die Thales-Folge selbst („Nach der Umkehrung … gilt MA = MB = MC“): Das Kind muss die Umkehrung nicht kennen, nur gleichschenklige Dreiecke; und der Satz beantwortet 064/066. Bestand `themen/geometrie.kreis`: „M ist die Mitte von [AB], und es gilt MC = MA. Wie groß ist γ?“ (gleiche Idee). | Voraussetzung streichen (nur „Winkel bei C ist 90°“) und nach den drei Winkeln fragen; Lösungsweg verlangt dann die Umkehrung. |
| VT2-075 | B | Doppelung Bestand `themen/geometrie.kreis`/`geometrie.grundbegriffe`: „Ein Kreis hat den Durchmesser 10 cm. Eine Gerade hat vom Mittelpunkt den Abstand 4 cm. Was ist die Gerade?“; 075 ist das Rückwärts-Gegenstück ohne neue Einsicht („Radius = d“). Stufe 2, trivial. | Als Stufe-3-Aufgabe: Tangente an zwei Kreise oder Abstand aus Koordinaten. |
| VT2-077 | B | Grenzfall zur Mehrdeutigkeit: Mias Satz „Je größer der Radius, desto mehr gemeinsame Punkte“ ist im schwachen Sinn (Anzahl fällt nie) wahr: 0, 0, 1, 2, 2, 2, … (per Skript bestätigt). Die Lösung „Falsch“ gilt nur für „immer mehr, ohne Grenze“. Ein sorgfältiges Kind kann „Richtig“ ankreuzen wollen; die dazu angebotene Option [0] ist wegen ihrer Begründung („immer öfter“) falsch, wird aber als Folge von [3] nicht wegen der Behauptung abgelehnt. Option [3] ist die längste. | Satz ändern: „… Je größer der Radius, desto mehr Schnittpunkte, ohne Grenze“, oder Aussage „Ein größerer Kreis hat mehr als zwei gemeinsame Punkte mit g“. |
| VT2-078, 082 | B | **Antwort ablesbar** und Wissensabfrage: 082 [3] nennt die komplette Regel „spitz innen, recht Mitte der Hypotenuse, stumpf außen“, die 078 (Test) und 080 beantwortet. Beide richtigen Optionen sind die längsten. 078 ist Stufe 2, nicht 3. | 082 mit anderer Fragestellung (z. B. Umkreismittelpunkt eines Dreiecks mit Seiten 5, 5, 8 – ohne Winkel, Begründung über die längste Seite) oder die Regel nicht in der Option ausschreiben. |
| VT2-081 | B | Doppelung: `mathe-profi/rollend-8/geometrie.kreis` hat „Ein Kind sucht den Mittelpunkt des Inkreises … Also zeichnet man die drei Mittelsenkrechten“ (derselbe Fehler, Fehler-Detektiv). Außerdem liefert 079 [3] die Gegenregel. | Anderer Fehler (Höhen statt Winkelhalbierenden, Berührpunkt auf Mittelsenkrechte der Seite). |
| VT2-085 | B | Fehlbild 6300 (`7 · 1000 − 7 · 100`) wird als „7 nur um eine Stelle nach links gerückt“ beschrieben; das ergäbe 63 000. Die Rechnung entspricht einer 7 von der Hunderter- zur Tausenderstelle. Stufe 3 bei einer Differenz zweier Stellenwerte überhöht. | Beschreibung: „die 7 von der Hunderter- statt der Tausenderstelle aus gerechnet: 7 000 − 700“; Test mit Rückwärtsfrage verschärfen („Welche Ziffer wurde mit der 0 vertauscht, wenn …“). |
| VT2-097 | B | Fehlbild antwort 4 („den Folgefehler in Zeile 4 für den ersten Fehler gehalten“): Zeile 4 („Einerklasse 100 heißt einhundert“) ist **richtig**, kein Folgefehler. Fehlerzeile 3 steht nicht am Ende; das Soll [3, 10] ist eindeutig. | Beschreibung: „Zeile 4 für falsch gehalten, obwohl 100 einhundert heißt“. |
| VT2-099, 100, 101, 104 | B | Doppelungen im Zahlenstrahl-Block: 104 ≈ `themen/zahlen.natuerlich` „Zwei Abschnitte nach dem Anfang steht 300, sechs Abschnitte nach dem Anfang steht 500. Welche Zahl steht neun Abschnitte nach dem Anfang?“ (gleiche Bauart); 100 ≈ `rollend-12` „Marken 4 000 und 5 000, 10 gleich große Abschnitte“; 101 ≈ „3 600 und 4 200 liegen 6 Abschnitte auseinander“; 099 ≈ „Ein Zahlenstrahl beginnt bei 0. Genau 5 Abschnitte nach der 0 steht 400“. Alle vier = Skalenschritt bestimmen und fortsetzen. | Eine Denkfigur reicht; 100/101/104 durch eine ungleiche Skala (ein Strich ohne Beschriftung) oder eine Begründung ersetzen („Zeigt dieser Strich 1 250? Begründe“). |
| VT2-107, 112 | B | 112 ist fast wortgleich mit `themen/zahlen.natuerlich`: „Zwei Zahlen ergeben auf Tausender gerundet beide 5 000. Wie groß kann ihr Unterschied höchstens sein?“ (nur 5 000 → 8 000, „natürliche“ ergänzt). Verstoß gegen Auftrag Abschnitt 5 („keine Aufgabe, die einer im Bestand gleicht“). 107 ≈ „Eine Zahl ergibt auf Zehner gerundet 1 000. Wie heißt die kleinste solche Zahl?“. 106, 107, 108, 112 sind **eine** Denkfigur (Rundungsbereich ±5). | 112 ersetzen (z. B. Runden auf zwei verschiedene Stellen: „Auf Zehner 350, auf Hunderter 400: welche Zahlen?“), 107 behalten, 108 oder 106 durch andere Idee. |
| VT2-110 | B | Richtige Option ist die einzige Nicht-Absolutaussage („manchmal … manchmal … manchmal“), die drei falschen sind „immer/nie“; dazu die längste. | Auch falsche Optionen als „manchmal“-Aussagen mit falschem Zusatz formulieren. |
| VT2-114 | B | Doppelung `mathe-profi/rollend-12/zahlen.natuerlich`: „Für 342 Personen sollen Busse bestellt werden. In jeden Bus passen 50 Personen.“ (aufrunden aus Sachgrund). | Ersetzen (z. B. die Aussage „man rundet immer sinnvoll“ an zwei Sachsituationen begründen lassen). |
| VT2-120 | B | Test ist trivial: Die Regel „höchstens dreimal hintereinander“ steht im Text, gesucht ist nur die Zeile mit DCCCC. Stufe 3 überhöht. | Regel nicht nennen; Fehlerzeile bei einer Rechnung, in der der Wert stimmt, die Schreibweise aber falsch ist (IIX), oder die Subtraktionsregel selbst. |
| VT2-124 | B | Mehrdeutig unter der wörtlich genannten Regel: „I steht nur vor V oder X“ und „höchstens dreimal hintereinander“ erlauben IXIXIX…, es gäbe keine größte Zahl. Eindeutig (39) wird es nur mit „üblichen Regeln“, die nicht ausgeschrieben sind. | Ergänzen: „Römische Zahlen werden von links nach rechts mit abnehmendem Wert geschrieben; nur ein kleineres Zeichen vor einem größeren zieht ab.“ |
| VT2-133 | B | Stoff aus späterer Etappe: Lösungsweg und Fehlbild nutzen Potenzschreibweise (2ⁿ − 1, 2⁶, 2⁷), die erst in `zahlen.potenzen_basis` (M5 3) kommt; in der Klasse-5-Einheit `zahlen.natuerlich` (M5 1.1) wird sie nicht eingeführt. Fehlbild 6 (`7 − 1`) wird mit „64 = 2⁶ als Stellenzahl gedeutet“ erklärt; die Rechnung 7 − 1 führt nicht dazu. | Lösungsweg ohne Potenzen („1, 3, 7, 15, 31, 63, 127; jede Eins mehr verdoppelt und addiert 1“); Fehlbild: „ein Wert 64 als Ziffernzahl 6 gelesen“ mit antwort 6. |
| VT2-008, 013, 032, 036, 041 | C | Fehler-Detektive mit Gerüst wie im Bestand (rollend-8 „1 % von 900 € sind 90 €, 4 % sind 4 · 90 €, Kontostand“; „Kind rechnet 3,5 % von 1 400 €: 14 € · 0,035“; rollend-13 „Kim löst die Klammer auf“; rollend-15 „Alex löst die Klammer in 9a − (2a + 7b − 3) auf“). Kein Wortlaut gleich, aber dieselbe Figur und derselbe Aufbau. Die Fehler selbst sind eindeutig; die Fehlerzeile ist nicht die letzte (Folgezeilen konsequent). 008: richtige Option ist die längste, mit Rechnung. | Zeilen anders anordnen, Fehler in Zeile 1 oder 3 setzen; 008 [1] kürzen. |
| VT2-010, 011 | C | 010: Zuordnung ist Schema (nur eine Zeile ganz richtig); 011: Idee-Etikett „auf einen Fehler zurückführen“ stimmt nicht; es wird nur das richtige Ergebnis gewählt. | Etiketten korrigieren oder in 010 pro Zeile den Fehler benennen lassen. |
| VT2-018 | C | Fehlbild 2 646 (`63 · 42`) „mit 1 000 gerechnet“: Ben schreibt 2,646 €; ein Kind trägt in ein Feld „ganze Zahl“ nie 2 646 ein. Nicht erreichbar. | Fehlbild 2 646 streichen; die übrigen zwei Fehlbilder (150, Zeilenfehler) genügen. |
| VT2-022, 028 | C | Stufe 3 überhöht: 022 ein Dreisatz mit glatten Zahlen (6 · 4 : 12), 028 „9 Monate sind dreimal 3 Monate“. | Stufe 2 eintragen. |
| VT2-030, 037, 046, 071, 072, 073, 074 | C | 037/046 zwei_wege oder Probe sind Rechnen (zwei Einsetzungen / vier Terme einsetzen). 071–074 dieselbe Figur (Abstand d mit Radius r vergleichen): 071 und 074 zählen Schnittpunkte, 072 und 073 setzen Schranken an r; 071 als Test Stufe 2. | Zwei der vier ersetzen. |
| VT2-052, 057, 059, 060, 062 | C | 052: Fehlbilder 9 (`18 : 2`) und 6 (`12 : 2`) haben keinen passenden Erklärtext („auch 18 durch 2 geteilt“ ist kein typischer Fehler). 057 ≈ `rollend-13` „Kim multipliziert (3x − 5)² … Zeile“ (anderer Fehler). 059 ≈ Bestand „Jemand rechnet (x + 6)² = x² + 36. Was stimmt?“, richtige Option die längste. 060 ≈ `rollend-14` „Quadratischer Teppich (x + 3), Fläche x² + p · x + 9“. 062 ≈ 057-Familie. | Fehlbilder bei 052 umformulieren; 059 Optionen kürzen. |
| VT2-064, 066, 067, 069 | C | Eine Figur („C auf Thaleskreis, r = AB : 2“) in 064, 065, 066, 067, 068, 069, 070; 064 [1] nennt als einzige Option das Fachwort „Umkehrung des Satzes des Thales“. 067 trivial (Radius = halber Durchmesser). | Eine Figur reicht; 066 oder 067 ersetzen. |
| VT2-076, 079, 080, 084 | C | 076: Fehlbild 3 (`1 + 1`) „einen zweiten Punkt vom kleinen Kreis“ unklar (der kleine hat 0). 079 [3] nennt die Inkreisregel, die 081 löst (Nachbarantwort). 080 ok. 084 richtige Option längste. | Beschreibung umformulieren; 079 [3] verkürzen. |
| VT2-086, 087, 090, 092, 093, 096, 103 | C | Stufe-2-Niveau (Klasse 5, einmalige Überlegung): 086 (5 000 : 5), 087 (Division durch 100/10), 090 (größte minus kleinste Zahl), 092 (Zahl lesen), 093, 096 (richtige Option länger), 103 (Mitte zweier Striche, 4 250). 092 und 090 als Tests/Sicherungen Stufe 3 überhöht. | Ehrlich Stufe 2 eintragen. |
| VT2-091, 099, 101, 102 | C | Erklärtexte der Fehlbilder arbiträr: 091 `4050 : 90`; 099 Maßstab 170 oder 50; 101 `20000 + 30000 : 6` („durch Teilstriche mal 3“); 102 `7500 : 50`. Kein typischer Fehler, nur Zahl. 102: Lösungsweg nennt 7,5 (Dezimalzahl, in Klasse 5 knapp). | Je Aufgabe mindestens ein echtes Fehlbild (z. B. 099: 3 400 : 1 200 · 6 = 17 = richtig; Fehlbild 3 400 − 1 200 = 2 200). |
| VT2-106, 108, 111, 113, 116, 118, 119 | C | 106 Test: Rundungsbereich zählen, Aufzählen im Kopf; 113 Test: Stufe 2, richtige Option offensichtlich (Kontonummer). 111 und 119 richtige Option längste. 116 gibt das Verfahren vor; 118/119 sind dieselbe Denkfigur („Rundungsfehler addieren sich/heben sich auf“). | 113 Stufe 2; 116 ohne Verfahrensvorgabe. |
| VT2-121, 122, 123, 125, 126, 127, 128, 131 | C | 121 Regeltext im Stamm, Option VC fällt auf; 122 ≈ Bestand `rollend-12` „888 braucht 3 Zeichen … DCCCLXXXVIII“ (Zeichen zählen); 123 Bausteine einzeln bewerten; 125 richtige Option längste; 126 Aufzählen von 30 Zahlen; 127 Test Stufe 2, richtige Option längste; 128 Greedy-Zerlegung, 131 Etikett `umkehren` stimmt nicht (2⁶ ausrechnen). | Etiketten korrigieren (131), Stufe 2 für 127. |

## Die 20 Fehler-Detektive (Prüfpunkt 4)

[F] Alle 20 (004, 008, 013, 018, 029, 032, 036, 041, 052, 057, 062, 067, 081, 088, 094, 097, 102, 109, 120, 130): genau eine erste Fehlerzeile, die übrigen Zeilen vor ihr sind richtig, die folgenden konsequent weitergeführt; das verlangte Ergebnis ist eindeutig. Die Fehlerzeile ist **nicht** die letzte bei: 008 (Z. 2 von 4), 013 (2/3), 018 (2/3), 029 (3/4), 032 (3/4), 036 (2/4), 041 (2/3), 052 (2/3), 057 (2/3), 062 (2/4), 081 (2/3), 088 (2/3), 094 (3/4), 097 (3/4), 109 (2/3), 120 (2/4), 130 (2/3). Letzte Zeile ist Fehlerzeile bei 004, 067, 102. VT2-097 und VT2-130 sind eindeutig (Z. 3 bzw. Z. 2); in 097 ist aber ein Fehlbild-Text falsch (siehe Tabelle). Bei 081 ist Zeile 2 („Deshalb konstruiert er die Mittelsenkrechten“) ein Schlussfehler, Zeile 3 aber auch für sich falsch; erste Fehlerzeile bleibt eindeutig Zeile 2.

## Verstehen wirklich geprüft?

**Im Kern Rechnen nach Schema (sollte ersetzt oder umgebaut werden):** 002, 006, 009, 012, 014, 031, 033, 035, 042, 045, 048, 049, 050, 051, 053, 056, 058, 060, 061, 063, 073, 087, 090, 093, 099, 100, 101, 103, 104, 114, 116, 118, 122, 123, 126, 128, 131. Zusätzlich schwach (Verstehen nur formal, ein Rechenschritt): 005, 022, 023, 025, 027, 029, 037, 038, 040, 044, 046, 065, 068, 071, 074, 075, 085, 107, 112, 121, 124, 132, 133.

**Die drei Schema-Aufgaben, die der Autor selbst nennt:** zusammenfassen S3 (VT2-029/031/033/035: ja, Schema, siehe Tabelle), ausklammern K1 (VT2-051/053: ja, mit Doppelung), binomisch S1 (VT2-058/061: ja, mit Doppelung). Die Zusätze „Kontext und Gegenfrage“ ändern daran wenig.

**Zwei-Wege/Umkehren-Etiketten:** `zwei_wege` (014, 040, 046, 111, 125) ist nur bei 111 (zweimal runden gegen einmal) eine echte Gegenüberstellung zweier Zugänge; 014/040/046 verlangen jeweils dasselbe Ausrechnen. `umkehren` (050, 051, 053, 070, 106, 131): echte Umkehr nur bei 051, 070, 106; 131 und 050 sind Vorwärtsrechnen.

**Sind die 7 `idee`-Werte je Lernziel wirklich verschieden?** [A] Nach Denkfigur, nicht nach Etikett:

| Lernziel | verschiedene Denkfiguren | Bemerkung |
|---|---|---|
| rollen | 5 | 002 und 006 sind Rechnen, 007 und 001 gleiche Bilanzfigur |
| jahreszinsen_komma | 3 | 008, 009, 010, 011, 012, 013 sind „Komma richtig setzen“, nur anders eingekleidet |
| kapital | 5 | gut |
| zeitanteil | 5 | 022/025/027 Brücke Monate ↔ Jahr dreimal |
| zusammenfassen | 4 | 029/032 gleicher Fehler |
| minusklammer | 4 | 036/041 gleiche Fehlerfigur; 037/040 beide „Einsetzen“ |
| aequivalenz | 3 | 043/047 (Einsetzen beweist nicht), 044/045/049 (Parameter), 046/048 (Term finden) |
| ausklammern | 5 | 050 Probe, 051 Umkehr, 052 Fehler, 054 Grenze; 053/056 Schema |
| binomisch | 5 | 057/062 beides „Quadrat mit Fehler“ |
| umkehrung | 2–3 | alle Aufgaben „C liegt auf dem Thaleskreis, r = AB : 2“ |
| lage | 3 | 071–074 Abstand gegen Radius, 075/076 Radius aus Durchmesser/zwei Kreise, 077 |
| umkreis_inkreis | 4 | 078/080/082 gleiche Regel (spitz/recht/stumpf) |
| stellenwert | 5 | gut |
| ziffern_zu_zahlwort | 4 | 092/094/097/098 alles „Klassen von rechts lesen“ |
| strahl_eintragen | 3 | 099/100/101/103/104 gleicher Skalenschritt |
| runden_regel | 3 | 106/107/108/112 Rundungsbereich |
| runden_sinnvoll | 5 | gut |
| roemisch_schreiben | 4 | 121/123/125 Regel anwenden |
| dualsystem | 5 | gut |

Die README-Aussage „je Lernziel sieben verschiedene, nie mehr als zwei gleiche“ gilt für die Etiketten (`ideen.py`), nicht für die Denkfiguren.

## Eindeutigkeit, Sonderfälle, Immer/Manchmal/Nie

[F] Kein Gegenbeispiel gefunden zu: 047 (Option [2]: allgemeingültig), 054 (Option [3]: nur bei ganzzahligen Faktoren; siehe Tabelle), 069 (Hypotenuse ist Durchmesser des Umkreises in jedem rechtwinkligen Dreieck), 082 (Aussagen zu spitz/rechtwinklig/stumpf stimmen), 084, 110 (auch bei 0: 0 bleibt 0, gleich; bei Zahlen unter 5 000 abwärts), 127 (Anhängen einer 0 verdoppelt; für 0 selbst gleich – im Text „ungleich 0“ ausgeschlossen), 129 (mehr Stellen = größer, bei führender 1 richtig), 132 (Zahlen 0 bis 31 mit höchstens 5 Ziffern: 32).
[F] Grenzfälle mit Befund: 016, 047 (drei Stellen genügen bei linearen Termen nicht-mehr-als-Rhetorik), 055, 077, 124 (siehe Tabelle). Bei 071 zählt d = 0 (Gerade durch M) richtig als Sekante; 083 schließt die Ränder korrekt aus (β = 50° und 90°).
[F] Zinsen: Alle Aufgaben bis auf 025 arbeiten innerhalb eines Jahres; 360/365-Tage-Zählung kommt nicht vor; Monate werden als n/12 gerechnet (023: April bis September = 6 volle Monate, ausdrücklich „eingeschlossen“). Einfache Verzinsung wird nur bei 025 problematisch.
[F] Terme: Äquivalenz gilt in 037, 038, 040, 045, 046, 048, 049 für alle x (Koeffizientenvergleich bzw. Probe an mehreren Stellen bestätigt). Definitionsmenge spielt keine Rolle (nur Polynome).
[F] Runden: Regel „ab 5 aufrunden“ ist in 106–119 durchgehend richtig; „auf Hunderter/Tausender/Zehntausender“ steht überall im Text. Römische Zahlen: 120/121/125 nennen die Regel; 122/124/126 verlassen sich auf die „üblichen Regeln“ (siehe 124).

## Schwierigkeit

- [A] Von den 19 Tests halte ich 11 für berechtigt Stufe 3 (001, 008, 015, 029, 036, 043, 057, 064, 085, 099, 106). Stufe 2 sind 022 (Dreisatz), 050 (Ausmultiplizieren prüfen), 071 (Aufzählen), 078 (Wissen), 092 (Zahl lesen), 113 (Kontonummer), 120 (Regel steht im Text), 127 (Verdoppeln).
- [A] Alle Aufgaben lassen sich mit Kopf und Papier in 2 bis 4 Minuten lösen; nichts ist zu schwer. Für die Klasse-5-Einheit `zahlen.natuerlich` ist das Niveau eher zu niedrig: 17 der 49 Aufgaben (086, 087, 090, 092, 093, 096, 100, 101, 103, 108, 113, 122, 123, 127, 128, 129, 131) sind für Klasse 5 Stufe 2 oder darunter; einige davon (090, 092, 113, 127) sind als Stufe 3 eingetragen – ehrlich nachführen.
- [F] Test-Tauglichkeit: Kein Bild, kein Tipp, Eingabeformat steht bei jeder Zahl-/Lücken-Aufgabe („Je Feld eine ganze Zahl“). Alle Auswahl-Aufgaben haben genau 4 Möglichkeiten. Negative Zahlen als Eingabe (029 −4, 035 −6, 041 −4): das Format „Je Feld eine ganze Zahl“ lässt das zu; 035 „… + □ Euro“ legt aber ein positives Feld nahe (−6 neben „+“) – im Text „Vorzeichen mit eingeben“ ergänzen.

## Lehrplan

- [F] Alle Aufgaben tragen den Lernbereich der Einheit (M5 1, M6 3, M7 1, M7 5) wie in `inhalte/themenliste.json`.
- [F] `geometrie.kreis` (Themenliste, `lehrplan_gym`): „Satz des Thales und seine Umkehrung beweisen und anwenden“, Lernbereich „M7 5 Kongruenz, besondere Dreiecke und Dreieckskonstruktionen“. Danach gehört die Umkehrung in diese Einheit. **Sicherheit [A] etwa 75 %**: Das ist die Zeile aus dem Repo (selbst wohl aus dem LehrplanPLUS übernommen); den Originaltext der Seite lehrplanplus.bayern.de habe ich nicht abrufen können (Freigabe für den Abruf kam nicht zustande), also nicht gegengeprüft. Nach meiner Erinnerung an den LehrplanPLUS Gymnasium Jahrgangsstufe 7 stehen dort Satz des Thales und seine Umkehrung sowie Umkreis und Inkreis im Lernbereich 5; die Begriffe Sekante/Tangente/Passante und „Lage von Kreis und Gerade“ (Lernziel `lage`) sind dagegen in der Themenliste nur bei der Realschule ausdrücklich genannt (`lehrplan_rs`: „Lage von Kreis und Gerade, Tangente“), beim Gymnasium dort als „Tangente von einem äußeren Punkt konstruieren“. Ob 071–077 (Abstand/Radius, Passante) im Gymnasium Klasse 7 stehen oder früher, kann nur die Fachseite sagen.
- [F] Umkehrung des Thalessatzes korrekt angewandt (064, 065, 066, 067, 069, 070); Existenz der Figuren geprüft: 065 (CA · CB = 0 bei C(2 | 4), Skript), 068 (nur C(4 | 4) liegt auf dem Kreis um M(4 | 0), r = 4; (4 | 2) innerhalb, (4 | 6) und (4 | 8) außerhalb, Winkel bei C stumpf bzw. spitz), 070 (α = 40°: ACM = 40°, MCB = 50°, AMC = 100°). Umkreis/Inkreis-Aussagen 078–084 stimmen für spitz/recht/stumpf.
- [F] Stoff aus späteren Klassen: Potenzschreibweise in 133 (Lösungsweg und Fehlbild; siehe Tabelle). Variable p, q in 021 und K, p in 026 (Formel Z = K · p : 100) – im Bestand `finanzen.zinsen` schon vorhanden, daher in Ordnung. 025 (über ein Jahr hinaus) siehe A. 102 und 100 (Lösungsweg 7,5 und Bruchteile „Fünftel“) nutzen Dezimalzahlen und Brüche, die in M5 1 noch nicht eingeführt sind (nur Hinweis, C). 118 Lösungsweg mit Vorzeichen (−16, +17, −4): erlaubt (M5 1.1 „Erweiterung zu den ganzen Zahlen“). Binomische Formeln, Ausklammern, Äquivalenz in M7 1.2 laut Themenliste ok.

## Doppelungen mit dem Bestand

[F] Verglichen: Alle 133 Aufgaben per Ähnlichkeitssuche gegen die Texte der Einheiten in `inhalte/themen/` (finanzen.zinsen, terme.umformen, geometrie.kreis, zahlen.natuerlich) und in `inhalte/mathe-profi/rollend-*` (rollend-5, -7, -8, -11, -12, -13, -14, -15), die Treffer von Hand gelesen; zusätzlich von Hand die Bestandslisten zu: Zinsen (Rollen, Kapital, Zeitanteil, Fehler-Detektive), Terme (Äquivalenz), binomische Formeln/Ausklammern, Zahlenstrahl, Runden, Römisch/Dual. Die Test-Aufgabe je Lernziel und mindestens zwei weitere habe ich in diesen Listen nachgeschlagen; vollständig Zeile für Zeile verglichen habe ich nicht alle 74 000 Bestandstexte.

| VT2 | gleicht im Bestand |
|---|---|
| 001 | `themen/finanzen.zinsen`: „1 000 € Sparkonto zu 1 % und gleichzeitig 1 000 € Kredit zu 8 %. Wie viel Euro verliert er?“ |
| 002 | `rollend-8/finanzen.zinsen`: Familie mit Kredit 2 000 € zu 6 % und Sparkonto 500 € zu 1 % |
| 005 | `themen/finanzen.zinsen`: Kind leiht 400 €, zahlt 420 € zurück; „Du leihst dir 3 000 €, zahlst 3 270 € zurück“ |
| 009 | `themen/finanzen.zinsen`: „Berechne die Jahreszinsen für 3 200 € bei 2,5 %“ |
| 023 | `themen/finanzen.zinsen`: „Vom 1. März bis zum 1. September …“ |
| 024 | `themen/finanzen.zinsen`: „Was bringt mehr Zinsen: 3 000 € für 8 Monate zu 3 % oder … 1 Jahr zu 2 %?“ |
| 025 | `themen/finanzen.zinsen`: „1 1/2 Jahre zu 2 %, die Zinsen werden jedes Jahr abgehoben“ |
| 027 | `themen/finanzen.zinsen`: Halbjahr/Zeitanteil rückwärts |
| 008, 013 | `rollend-8/finanzen.zinsen`: Fehler-Detektiv mit demselben Gerüst (1 % → p %, Kontostand) bzw. Komma-Faktor „3,5 % von 1 400 €“ |
| 038, 045, 049 | `themen`/`rollend-15/terme.umformen`: „Für welche Zahl a ist 3(x + a) äquivalent zu 3x + 12?“, „13(x + 4) und 13x + k“, „A: 2(x − 3) + x …“ |
| 043, 047 | `themen`: „Lisa … x + x + x und x · x · x“; `rollend-15`: „Kim behauptet: 3x + 6 und 9x sind äquivalent“; `rollend-13`: „Kim prüft x² + 2 und 3x“ |
| 044 | `themen`: „2x + 1 und x + 2 sind nicht äquivalent. Für genau eine Zahl x haben sie trotzdem denselben Wert. Für welche?“ |
| 051 | `rollend-14/terme.umformen_teil2`: „Rechteck … Fläche 6x² + 9x … Seite 3x“ |
| 053 | `themen/terme.umformen`: „Berechne geschickt: 37 · 13 + 37 · 87“ |
| 058 | `themen/terme.umformen`: „Ergänze … x² + 12x + □ = (x + □)²“ |
| 061 | `themen`: „49 · 51“, „51² = (50 + 1)²“; `rollend-13`: „Berechne 47² auf zwei Wegen“ |
| 063 | `rollend-14`: „Quadratisches Beet 4x² + 20x + k, Seitenlänge 2x + m“ |
| 065, 070, 075 | `themen/geometrie.kreis` und `geometrie.grundbegriffe`: „bei C rechter Winkel, Radius des Kreises“; „MC = MA, wie groß ist γ?“; „Durchmesser 10 cm, Abstand 4 cm. Was ist die Gerade?“ |
| 081 | `rollend-8/geometrie.kreis`: „Ein Kind sucht den Mittelpunkt des Inkreises … Mittelsenkrechten“ |
| 099, 100, 101, 104 | `themen/zahlen.natuerlich` und `rollend-12`: Zahlenstrahl mit Abschnitten, „zwei Abschnitte nach dem Anfang steht 300, sechs … 500; neun?“ |
| 107, 112 | `themen/zahlen.natuerlich`: „… auf Zehner gerundet 1 000. kleinste Zahl?“; „Zwei Zahlen … auf Tausender gerundet beide 5 000. größter Unterschied?“ |
| 109 | `rollend-12`: Fehler-Detektiv Runden („Mara rundet 38 428“) – gleiche Form, anderer Fehler |
| 114 | `rollend-12`: „Für 342 Personen sollen Busse bestellt werden …“ |
| 120, 122 | `rollend-12`: „Lena schreibt die Zahl 49 in römischen Zahlzeichen“ (Fehler-Detektiv), „888 … DCCCLXXXVIII“ (Zeichen zählen) |
| 130 | `rollend-12`: „Ben schreibt die Zahl 13 als Dualzahl“ (Fehler-Detektiv in Gegenrichtung) |

Innerhalb der Runde: 065 ↔ 068 (nahezu gleich), 043 ↔ 047, 078 ↔ 082 ↔ 080, 079 ↔ 081, 106 ↔ 107 ↔ 112 (Lösung von 112 steht sinngemäß im Lösungsweg von 107), 070-Text ↔ 064/066, 100/101/103/104 untereinander, 118 ↔ 119. Gleiche Sollantwort im selben Pool und Lernziel: keine (Skript des Autors, von mir bestätigt).

## Was ich NICHT prüfen konnte

- Den Originaltext des LehrplanPLUS (lehrplanplus.bayern.de) – Abruf nicht freigegeben. Aussagen zu M7 5 beruhen auf der Themenliste im Repo und meiner Erinnerung (siehe oben).
- Keine App-Oberfläche: Ob „Je Feld eine ganze Zahl“ negative Zahlen und die Eingabe „0“ annimmt, habe ich nicht in der App getestet.
- Kein Handvergleich aller Bestandstexte (74 000 Zeichenfolgen), nur Suche und Lesen der besten Treffer je Aufgabe; weitere Doppelungen sind möglich.
- Das Einspielen (`tools/vtest_sql.py`) habe ich nicht angesehen; nichts eingespielt, keine Datenbank, keine Council-Werkzeuge.
- Ob Kinder bei Zeilen-Fehlersuche tatsächlich nach Zeile gefragt werden wollen oder die Frage anders lesen, ist Einschätzung.
- `bauen.py` habe ich nicht ausgeführt (es überschreibt die Aufgabendateien); die Aufgaben-JSON ist unverändert.
