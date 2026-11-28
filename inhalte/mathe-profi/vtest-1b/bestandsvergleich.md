# Vergleich mit dem Bestand (VT1B)

**Verfahren und Grenzen.** (1) Das Bauskript vergleicht jede Aufgabe mit `inhalte/themen` und allen `rollend-*` nach Kern (Zahlen maskiert und unmaskiert, Sollwert, Frage); Treffer brechen den Bau ab. Letzter Lauf: 0 Treffer. (2) Von Hand habe ich je Lernziel die in der Vorprüfung genannten Nachbarn und die nach Idee nächsten Bestandsaufgaben gelesen und die Ersatzaufgaben gegen sie geprüft. **Ich habe nicht alle rund 2 100 Bestandsaufgaben der Etappe einzeln von Hand gelesen**; die Behauptung „verglichen“ bezieht sich auf (1) vollständig und auf (2) die Nachbarschaft.

Bestand je Einheit (themen + rollend): bruch.prozent und bruch.prozent_grundwert 249 + 289 + 52 = 590; gleichungen.bruch 325 + 40 = 365; terme.potenzgesetze (mit ganzzahlig und natuerlich) 114 + 177 + 226 + 74 = 591; zahlen.potenzen_zehner 274 + 21 = 295; messen.flaechen_vielecke 237 + 48 = 285.

| Lernziel | verglichen mit | nächstliegende Bestandsaufgaben | Abstand |
|---|---|---|---|
| prozentwert | 590 | „Doppelrabatt 40/25 %“, „30 % von 50 gegen 50 % von 30“ | 001 (mehrere Ganze, Lücken), 002 (zwei Wege, Entscheidung), 003 bis 007 anderer Zugriff; 002 als Hinweis in der README |
| grundwert | 590 | `bruch.prozent_grundwert` („nach 35 % Rabatt 52 €“), „12 Kinder sind 8 %“ in anderer Zahl | 009 neu als Auswahl mit Überschlag, Fehlbetrag, gemeinsames Ganzes, Winkel zurück |
| verstehen (prozent) | 590 | „50 % von 20 gegen 40 % von 30“, Wachstum über 100 % | 015 Anteil vom Anteil (Lücken), 018 Rückwärts bei 150 %; 018 als Hinweis |
| definitionsmenge | 365 (+ `terme.bruchterme`) | siehe Abschnitt „Einheit 20 nach Vorprüfung W1“ unten | je Aufgabe einzeln |
| ueber_kreuz | 365 | siehe Abschnitt unten | je Aufgabe einzeln |
| scheinloesung | 365 | siehe Abschnitt unten | je Aufgabe einzeln |
| verhaeltnis | 365 + `groessen.verhaeltnisse` 230 + `groessen.indirekt` | siehe Abschnitt unten | je Aufgabe einzeln |
| negativer_exponent (terme) | 591 | „Muster der Zweierpotenzen nach rechts“, „Ben: 10⁻⁴ größer als 10⁻²“ | 053 Zählen mit Grenze 1/50, 054 Begründung mit Basis 2, 055 Dezimalzahl zu Potenz, 056 Stücke (Hinweis) |
| fehler_finden | 591 | Basis · Exponent (`potenzen_basis`), „5⁻² = −25“ | 057 Exponenten addiert, 060 Potenz von Summe, 061 Basis mal Hochzahl bei 4⁻², 063 Vorzeichen; 062 Hochzahl 0 (Hinweis) |
| gross_wissenschaftlich | 295 | `rollend-8` K7-V028/V029, „Die Zahl 4,5 · 10ⁿ hat genau 11 Stellen“, „Welche Darstellung von … ist die wissenschaftliche?“ | 066 rückwärts vom Doppelten, 067 Nullen-Fehlvorstellung, 068 Bücher im Speicher: weder Ziffernzahl noch Auswahl der Schreibweise im Bestandsstil |
| negativer_exponent (zehner) | 295 | „10⁻⁶ als Dezimalzahl“, „10⁻⁵ ist eine negative Zahl“, „Blatt 10⁻⁴ m“ | 072 Teilungen zählen, 073 Stücke, 074 skaliert, 075 verkettet, 077 Fehler-Detektiv (Hinweis) |
| vorsilben_klein | 295 | Tera-Umrechnungskette K7-V033, „Faden 80 µm, 1 cm“, „0,35 mm in µm“ | 080 und 081 ersetzt (Faden und 0,35 mm entfallen); 078 Modell vergrößern, 083 Zeichnung, 079/084 Maßzahl und Einheit; 082 Fehler-Detektiv anderer Kette |
| vergleichen_pruefen | 295 | „3 · 10ⁿ größer als 0,02 und kleiner als 0,5“, „Welche Zahl liegt zwischen 10⁻³ und 10⁻²“, Virus/Bakterium | 085, 087, 088 ersetzt (ordnen nicht normierter Zahlen, Salzproben, k-Raster); 085, 087, 089 als Hinweis |
| dreieck | 285 | „Spitze irgendwo auf der Linie“, „Rechtwinkliges Dreieck 6, 8, 10, Höhe auf die längste Seite“, „Jonas 6 · 8 = 48“ | 096 ersetzt (Jonas entfällt), 097 Teilverhältnis der Grundseite, 098 plus und minus 50 %; 092/096 als Hinweis |
| rueckwaerts | 285 | `gleichungen.reinquadratisch` (98 cm², doppelt so lang wie breit), „Parallelogramm 64 cm², Grundseite 8“ | 101 ohne Teilen (Umbau mit Pythagoras-Dreieck 6, 8, 10), 105 Schranke a · b; 099, 103 Höhe aus Fläche in zwei Fällen |
| zusammengesetzt | 285 | `rollend-6` „Trapez, Weg B: Zerlege in Rechteck und Dreiecke“, „Fünfeck aus Rechteck und Dreieck“ (Bestand vorhanden), „Bilderrahmen“ | 108 und 109 neu (Flaggenkreuz, Schnitt und Umfang), 110 Vorzeichen beim Ergänzen, 112 Viereck über Koordinaten; **das Fünfeck steht im Bestand (K7-V132 und Übungen), die frühere Angabe „kein Bestandsfünfeck“ war falsch**; 106 (Rechteck plus Dreieck, Höhe rückwärts) als Hinweis |
| verstehen (flaechen) | 285 | „Rechteck 5 × 4 schief gedrückt, Höhe 1“, `rollend-14` „Trapez 54 cm², Höhe 6“, „Rechteck 6 × 12, Dreieck Grundseite 16“, „Quadrat 4-mal so lange Seite“ | Alle sieben Aufgaben ersetzt: Strecken in Prozent (113, 117), Anteil im Rechteck (114), Differenzpaar (115), Zuwachs (116, 119), Höhensumme (118); 118 als Hinweis |

Mit 0 Treffern im Werkzeug heißt „Abstand“ hier: andere Zahlen, anderer Kontext oder andere Frage; die Denkfigur selbst (Schema) kann bei einzelnen Aufgaben dieselbe sein und ist dort benannt.

Fehlerberichtigung zur Vorprüfung 2: In der ersten Fassung stand bei `zusammengesetzt`, es gebe „kein Bestandsfünfeck“. Das ist falsch; das Fünfeck K7-V132 (`abbildungen.determinanten2`) und mehrere Übungen zu „Fünfeck aus Rechteck und Dreieck“ stehen im Bestand. Die frühere Aufgabe 110 war darum eine Bestandsdoppelung und ist ersetzt. Die Liste der Aufgaben mit gleicher Einsicht, aber anderer Form, steht im Abschnitt „Hinweise für die Gegenprüfung“ der README.

## Einheit 20 (gleichungen.bruch) nach Vorprüfung W1

**Was von Hand gelesen wurde (vollständig, nicht nur Nachbarschaft):** alle 325 Aufgaben von `inhalte/themen/gleichungen.bruch.json` (Zahlen „T n“ = Position n ab 0), alle Bruchgleichungs- und Verhältnisaufgaben aus `rollend-7` (K8-V067 bis V087), `rollend-11` (S3-V044 bis V048), `rollend-13` (R8-V045 bis V058); `rollend-15` enthält keine Datei dieser Einheit. Dazu alle Aufgaben von `inhalte/themen/groessen.verhaeltnisse.json` (Zahlen „V n“), die Definitionsmengen-Aufgaben von `terme.bruchterme`, die Aufgabentexte von `groessen.indirekt` und die Proportionalitätsaufgaben in `rollend-2/3/4/12/14`. Das Werkzeug (Bauskript und `tools/vtest_pruefen.py`) meldet 0 Treffer.

Bei der Lektüre bestätigte Doppelungen der vorigen Fassung (zusätzlich zu den Befunden der Vorprüfung): alte 037 = V 36 (`groessen.verhaeltnisse`: Verhältnis 3 : 5, je 4 dazu, dann 2 : 3); alte 039 = V 147 (Handyfoto 6 cm × 10 cm, Poster 45 cm breit, Höhe gesucht); alte 041 nahe T 250 und `rollend-10` K9B-V038 (Fläche mit Faktor zum Quadrat). Alle drei sind ersetzt.

| Kennung | Lernziel / Pool | nächstliegender Bestandskern | Unterschied |
|---|---|---|---|
| 022 | definitionsmenge / test | T 183 (2/x + 1 = 5/x, alle Glieder malnehmen); `terme.bruchterme` „Haben 1/(x − 2) und x/(x² − 2x) dieselbe Definitionsmenge?“ | Im Bestand wird keine Umformung auf ihre Wirkung auf D untersucht. Hier verkleinert das Addieren von 1/x die Definitionsmenge (die einzige Lösung 0 geht verloren), das Malnehmen vergrößert sie. |
| 023 | definitionsmenge / korrektur | T 33 (a in 2/(x − a) mit D = ℚ \ {−1}), `rollend-7` K8-V074 | unverändert aus der vorigen Fassung (ohne Befund): Koeffizient 2 vor x, a aus der Nullstelle 7 |
| 024 | definitionsmenge / korrektur | T 45 (Hüttenmiete), T 9, T 42, `terme.bruchterme` (Feier, Gastgeber) | Gleichung wird aus dem Text selbst aufgestellt; gefragt ist eine Grenze des sinnvollen Bereichs (beide Breiten positiv), nicht nur eine verbotene Zahl |
| 025 | definitionsmenge / sicherung | T 38 („Kann eine Bruchgleichung die Definitionsmenge ℚ haben?“) | anderer Kern: Zusammenhang von Lösungsmenge und Definitionsmenge zweier Gleichungen, Urteil über eine allgemeine Aussage |
| 026 | definitionsmenge / sicherung | T 7, T 46 („Wie viele Zahlen schließt D aus?“), T 47 | Grundmenge ℤ statt ℚ (die Nullstelle −1,5 zählt nicht), rückwärts: b aus einer vorgegebenen ausgeschlossenen Zahl; Grundmenge kommt im Bestand nicht vor |
| 027 | ueber_kreuz / test | T 225 (a, damit (x + a)/(x − 5) = 3/(x − 5) keine Lösung hat), `rollend-7` K8-V081 | dort gleiche Nenner und ein einziger Fall (Scheinlösung); hier verschiedene Nenner und zwei Fälle verschiedener Art (gleiche Zähler ⇒ 0 · x = 49; Zähler 0 ⇒ verbotener Kandidat) |
| 028 | ueber_kreuz / korrektur | T 81 (Zähler ersetzen, damit x = 4 Lösung ist), T 131, T 134 | keine Lösung vorgegeben; gesucht ist der Zähler, der dieselbe Lösung wie eine andere Gleichung liefert (Verhältnis der Zähler). Grenzfall: Wer erst x = −9,5 ausrechnet, rechnet wie T 131. |
| 029 | ueber_kreuz / korrektur | T 104 (warum a · d = c · b), `rollend-7` K8-V071 (Kehrwert als Weg B bei 18/x = 3), T 274 | Vergleich Über-Kreuz gegen Kehrwert bei zwei Nennern mit x; gefragt ist, ob beide Wege erlaubt sind und warum (Zähler nicht 0) |
| 030 | ueber_kreuz / sicherung | T 99, T 107, T 125, T 144 (Gleichungen, bei denen x² wegfällt, lösen) | Aussage über alle Gleichungen dieser Form, Gegenbeispiel ohne Lösung (4 = 6) |
| 031 | ueber_kreuz / sicherung | T 130 („Über Kreuz geht nur, wenn auf jeder Seite genau ein Bruch steht“) | gleiche Regel, hier angewandt auf vier Gleichungen, darunter eine mit Summe im Zähler (erlaubt); Schema-Aufgabe des Lernziels |
| 032 | scheinloesung / test | T 224 ((x² − 1)/(x − 1) = 2), Bestandskern (x² − a²)/(x − a) = c | andere Gleichung (Ausklammern von x, Bruch = −3), gefragt ist der Schritt, an dem die Einschränkung verloren geht (zwei Wege, Probe in der gekürzten Gleichung) |
| 033 | scheinloesung / korrektur | T 180 (2/(x − 3) − 1/x = 6/(x² − 3x) lösen), T 225, K8-V081 | rückwärts: Zahl c so bestimmen, dass eine vorgegebene verbotene Zahl als Kandidat entsteht, zwei Fälle (2 und 0) |
| 034 | scheinloesung / korrektur | T 229 (x/(x − 2) = 2/(x − 2) + 3), `rollend-7` K8-V079 (Kandidat und Zahl der Lösungen) | Zahlenrätsel, Gleichung selbst aufstellen; nur die Anzahl ist gefragt; Schema-Aufgabe des Lernziels |
| 035 | scheinloesung / sicherung | T 192, T 199, T 203 („Warum ist x = … keine Lösung?“) | Urteil über allgemeine Regeln aus Beispielen (nie, immer, nur negativ), Gegenbeispiel finden |
| 036 | scheinloesung / sicherung | `rollend-13` R8-V053 (Graphen von x/(x − 2) und 2/(x − 2)), T 233 ((x − 4)/(x − 4) = 1) | Differenz der beiden Seiten ist konstant −1; der Bruch (x − 3)/(x − 3) tritt nur als Zwischenschritt auf, gefragt sind Differenz und Zahl der gemeinsamen Punkte |
| 037 | verhaeltnis / test | T 279 (Sirup zugeben: 1 : 4 → 1 : 2), V 73 (Wasser zugeben), V 71 | dort kommt ein reiner Bestandteil dazu; hier eine zweite Mischung, beide Bestandteile wachsen verschieden; kein „a : b, n dazu, dann c : d“ |
| 038 | verhaeltnis / korrektur | V 45, V 58 (zu beiden Gliedern dieselbe Zahl addieren), T 243 (Rezept), Altersaufgaben anderer Einheiten (Summe der Alter) | Modellwahl: dieselbe Angabe 2 : 3 einmal additiv (Alter), einmal multiplikativ (Rezept) |
| 039 | verhaeltnis / korrektur | V 16 (Anteil aus Verhältnis 3 : 4) | rückwärts vom halbierten Anteil zum neuen Verhältnis; Fehlvorstellung „Wasser verdoppeln“ |
| 040 | verhaeltnis / sicherung | `groessen.indirekt` („Doppelt so schnell heißt halb so lange“, indirekt proportionale Wertepaare) | kein fehlender Wert, sondern das umgekehrte Verhältnis mit Begründung; Ablenker „man braucht die Strecke“ |
| 041 | verhaeltnis / sicherung | V 16, V 34 (Anteil als gekürzter Bruch) | unverändert aus der vorigen Fassung (Ganzes : Teil aus Teil : Teil); Schema-Aufgabe des Lernziels |
