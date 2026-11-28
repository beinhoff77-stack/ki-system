# Vergleich mit dem Bestand (VT1B)

**Verfahren und Grenzen.** (1) Das Bauskript vergleicht jede Aufgabe mit `inhalte/themen` und allen `rollend-*` nach Kern (Zahlen maskiert und unmaskiert, Sollwert, Frage); Treffer brechen den Bau ab. Letzter Lauf: 0 Treffer. (2) Von Hand habe ich je Lernziel die in der Vorprüfung genannten Nachbarn und die nach Idee nächsten Bestandsaufgaben gelesen und die Ersatzaufgaben gegen sie geprüft. **Ich habe nicht alle rund 2 100 Bestandsaufgaben der Etappe einzeln von Hand gelesen**; die Behauptung „verglichen“ bezieht sich auf (1) vollständig und auf (2) die Nachbarschaft.

Bestand je Einheit (themen + rollend): bruch.prozent und bruch.prozent_grundwert 249 + 289 + 52 = 590; gleichungen.bruch 325 + 40 = 365; terme.potenzgesetze (mit ganzzahlig und natuerlich) 114 + 177 + 226 + 74 = 591; zahlen.potenzen_zehner 274 + 21 = 295; messen.flaechen_vielecke 237 + 48 = 285.

| Lernziel | verglichen mit | nächstliegende Bestandsaufgaben | Abstand |
|---|---|---|---|
| prozentwert | 590 | „Doppelrabatt 40/25 %“, „30 % von 50 gegen 50 % von 30“ | 001 (mehrere Ganze, Lücken), 002 (zwei Wege, Entscheidung), 003 bis 007 anderer Zugriff; 002 als Hinweis in der README |
| grundwert | 590 | `bruch.prozent_grundwert` („nach 35 % Rabatt 52 €“), „12 Kinder sind 8 %“ in anderer Zahl | 009 neu als Auswahl mit Überschlag, Fehlbetrag, gemeinsames Ganzes, Winkel zurück |
| verstehen (prozent) | 590 | „50 % von 20 gegen 40 % von 30“, Wachstum über 100 % | 015 Anteil vom Anteil (Lücken), 018 Rückwärts bei 150 %; 018 als Hinweis |
| definitionsmenge | 365 | `rollend-7` K8-V074 (a mit x = 3), `rollend-13` R8-V032 | 022 identisch auf D, 023 nie null, 024 a aus D; 027 Fehler mit x² |
| ueber_kreuz | 365 | `rollend-7` K8-V074 | 029 Parameter k mit Einordnung statt a mit x = 3; 032 zwei echte Wege (Kreuzprodukt gegen Überlegung des Zählers) |
| scheinloesung | 365 | „Welche Gleichung liefert x = 4, obwohl 4 nicht zu D gehört?“ | 036 Parameter b, 039 c aus Kürzen, 042 Bruch gleich null |
| verhaeltnis | 365 | `groessen.verhaeltnisse` („3 : 5, je 4 dazu ergibt 2 : 3“, „Bonbons 2 : 3 : 4“) | 043 x in zwei Verhältnissen (neu, kein 3 : 5 mit +4), 045 Obstschale, 048 Mittelwert, 049 gemeinsames Glied (Hinweis) |
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
