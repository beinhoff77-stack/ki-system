# Vorprüfung 3 der Runde 3 (VT3), dritte unabhängige Prüfung

Stand: Zweig `vorpruefer-vt3c`, Basis `origin/helfer-vtest-r3`. Geprüft wurden alle 126 Aufgaben. Besonders genau die seit 0ef6e127 geänderten.

## Urteil

Nach kleiner Korrektur einspielbar: Die Mathematik aller 126 Aufgaben ist fehlerfrei, aber neun Aufgaben (002, 003, 027, 055, 057, 065, 066, 119, 123) sind inhaltliche Doppelungen zum Bestand der Einheit und das Lernziel "stelle" hat mit 3 Schema-Aufgaben eine zu viel.

Zahl der Befunde: A (Muss) 10, B (Soll) 11, C (Kann) 5.

Wichtig zur Belastbarkeit: Die Doppelungen stammen aus Handlesen des Bestands (kein Werkzeug, keine Vollabdeckung). Sie sind Funde, keine Gewähr dafür, dass sonst nichts doppelt ist. Die Bestandsvergleichs-Methode des Schreibers war rein lexikalisch und hat semantische Doppelungen übersehen.

## Methode

- Rechnung: Rechenskript `vorpruefung_rechnen_3.py` (neu, unabhängig, nutzt kein `gegenrechnung.py`, `kern.py` oder `e_*.py`). Es rechnet mit exakten Brüchen, prüft bei 64 Auswahl-Aufgaben jede Option einzeln (genau eine wahr), rechnet die Fehlbilder nach (keines gleich der Lösung) und prüft 006, 019, 060, 063, 088, 100, 118, 120 zusätzlich per Brute-Force. Lauf: "Aufgaben: 126, davon Auswahl 64, Zahl/Luecken 62 / 0 Abweichungen".
- Alles andere (Eindeutigkeit, Erratbarkeit, Schema, Denkfiguren, Doppelungen, Klassenstufe) ist Handlesen und Urteil.

## Befunde A (Muss)

Doppelungen mit gleichem Kern wie eine Bestandsaufgabe derselben Einheit, nur Zahlen oder Einkleidung geändert. Vorschlag jeweils: Aufgabe durch eine mit anderer Einsicht ersetzen (gleiches Lernziel, gleicher Pool, gleiche Stufe).

| Kennung | Beleg im Bestand | Vorschlag |
|---|---|---|
| A1 002 | messen.volumen#17 (4·4·4, innere Würfel = 8), rollend-14 R14-V147, zahlen.wurzeln_basis#97 (5·5·5, 27 identisch) | ersetzen |
| A2 003 | messen.volumen#166/175/178/179/182/184 (Würfel auf Quader geklebt), R14-V160. Im Bestandsvergleich des Schreibers nur "mittel" | ersetzen |
| A3 027 | messen.volumen#208 (Klassenzimmer 8·7·3, gleiche Zahlen, ca. 170 m³) | ersetzen |
| A4 055 | daten.kennwerte#88 (fünf aufeinanderfolgende Zahlen, Mittelwert gegeben, größte gesucht) | ersetzen |
| A5 057 | daten.kennwerte#120/#123 (Teilgruppen-Mittel, Rest-Mittel) | ersetzen |
| A6 065 | funktionen.grundbegriffe#53 (x² − 4, Aussage über Funktionswerte) | ersetzen |
| A7 066 | rollend F1-10 (Wertemenge, Definitionsmenge, linear) | ersetzen |
| A8 119 | geometrie.winkel#224 (äußere Teile gleich, mittlerer gesucht) | ersetzen. Zudem 4 von 7 Aufgaben in "figuren" zerlegen den rechten Winkel (siehe B9) |
| A9 123 | geometrie.winkel#29 (zum Vollwinkel ergänzen, Fehler mit 180°). Die Ersatzaufgabe für die frühere Doppelung ist selbst eine Doppelung | ersetzen |
| A10 073, 075, 077 | Lernziel "stelle" hat 3 Schema-Aufgaben (075 Rezept, 077 Rezept, 073 Umformungsfehler), Obergrenze ist 2 | eine davon (am ehesten 073) auf Einsichtsaufgabe umbauen |

## Befunde B (Soll)

- B1 Doppelungen mit gleicher Idee, anderem Format oder anderen Zahlen. Bitte prüfen und die engsten ersetzen:
  - daten.darstellen: 029 (#187/#190), 033 (#182), 035 (#185), 038 (#102/#207), 039 (#214), 040 (#85 bis #99), 042 (#212), 043 (#158/#230, R5-V170), 044 (#149), 046 (#232), 053 (#117), 054 (#119), 056 (#115/#94), 059 (#113/#121), 064 und 068 (#26/#27), 067 (#87), 076 (#137/138/141/151), 085 (#181), 091 (#313), 094 (#354), 097 (G2T2-V01/#196), 098 (#346/#352/#363), 103 (#265), 108 (#120), 109 (#146/#148), 112 (#150), 114 (#206/#213/#225).
  - kennwerte: 051 und 062 (#95).
  - terme.aufstellen: 095 (#110, Streichholz-Quadrate 3n+1, anderes Thema).
  - abbildungen.kongruenz: 117 (#267, Winkelhalbierende von Nebenwinkeln).
  - messen: 014 (#124, R14-V156 Tank leer), 028 (R14-V164).
  - geometrie.winkel: 102 (#52), 126 (#28 ff.).
  - Innerhalb VT3 selbst: 001 und 028 (Prozentänderung der Kanten).
- B2 011: Die richtige Option sticht heraus (nur dort steht ein anderes Ergebnis, "2,25 Liter"). Optionen angleichen.
- B3 019: Die richtige Option hat eine andere Bauart (Nein-Begründung) als die drei falschen ("zum Beispiel …"). Angleichen.
- B4 101: Das Ergebnis (γ = 48) steht im Text als Wert von α. Aufgabe so ändern, dass die Zahl nicht im Text vorkommt.
- B5 087: Die Antwort 8 ist die gegebene y-Koordinate von P(3|8) und damit direkt abschreibbar.
- B6 Hedge-Muster: "höchstens/mindestens" steht in 5 von 64 richtigen (060, 063, 064, 118, 034 "Vielfaches von"), aber nur in 4 von 192 falschen Optionen (8 % gegen 2 %). In 063 ist die einzig abgeschwächte Aussage die richtige. Einige falsche Optionen mit "höchstens/mindestens" ergänzen.
- B7 Klassenstufen-Zweifel (siehe unten): 001, 036, 043, 106, 113, 117, 118.
- B8 Denkfiguren "saeulendiagramm": Maßstabs-Verhältnis in 036, 039, 041, 042 ist praktisch dieselbe Einsicht. Formal 6 Kategorien, inhaltlich nur etwa 4 verschiedene.
- B9 Denkfiguren "figuren": Zerlegung des rechten Winkels in 113, 114, 118, 119 (viermal von 7).
- B10 Denkfiguren "mittelwert" und "mittel_rueckwaerts": "Summenänderung durch n" in 050, 051, 062 mehrfach.
- B11 Schwierigkeitsmarken: 021 und 061 stehen auf Stufe 3, sind aber Rezeptaufgaben (Schema). Marke senken oder Aufgabe ändern.

## Befunde C (Kann)

- C1 079: Beim zweiten Fehlbild (5 + 4) stimmt die Beschreibung "in die falsche Richtung" nicht.
- C2 025: Fehlbild 30:3 ("Faktor 3") ist unmotiviert beschrieben.
- C3 041: Fehlbild 17 (57375:3375) passt nicht zum Text ("60 000"), kleines Beschreibungsproblem bei Aufgabe 022.
- C4 099 (Option 2) und 086 (Option 3): richtige Schlussfolgerung mit falscher Begründung. Akzeptabel, nur ausdrücklich so lassen.
- C5 Test nicht die anspruchsvollste Aufgabe des Lernziels: 050 (leichter als 053/055), 092 (leichter als 096/098), 120 (leichter als 118/122). 078 ist in Ordnung.

## Schema-Zählung (eigene, unabhängige)

Sicher Schema: 001, 014, 021, 035, 040, 047, 052, 061, 062, 069, 073, 075, 077, 079, 085, 089, 098, 102, 104, 124, 126. Das sind 21 (Schreiber: 20). Grenzfälle, die je nach Strenge dazukommen: 030, 038, 050, 059, 070, 106 und 005, 017 (Lernziel nicht sicher zugeordnet). Mit Grenzfällen höchstens 29. Der Schreiber nennt als unsicher 001, 021, 047, 102, 104, 059, 073, 113. Ich zähle 001, 021, 047, 102, 104, 073 als Schema, 059 und 113 nicht.

## Tabelle: Schema-nahe und Denkfiguren je Lernziel

| Lernziel | Schema sicher | Grenzfälle | Denkfiguren formal | Denkfiguren inhaltlich |
|---|---|---|---|---|
| quader | 1 (001) | | 6 bis 7 | gut, 002 und 003 doppelt zum Bestand |
| liter | 1 (014) | | 6 bis 7 | gut |
| rueckwaerts | 1 (021) | | 6 bis 7 | gut |
| verstehen (Volumen) | 0 | 028 | 6 bis 7 | gut |
| relative_haeufigkeit | 1 (035) | 030 | 6 bis 7 | gut |
| saeulendiagramm | 1 (040) | 038 | 6 bis 7 | etwa 4 echte (B8) |
| irrefuehrend | 1 (047) | | 6 bis 7 | gut |
| mittelwert | 1 (052) | 050 | 6 bis 7 | schwach (B10) |
| mittel_rueckwaerts | 2 (061, 062) | 059 | 6 bis 7 | schwach (B10) |
| mengen | 1 (069) | 070 | 6 bis 7 | gut |
| stelle | 3 (073, 075, 077), über Ziel | | 6 bis 7 | gut |
| graph_lesen | 1 (079) | | 6 bis 7 | gut |
| punkt_graph | 2 (085, 089) | | 6 bis 7 | gut |
| sachzusammenhang | 1 (098) | | 6 bis 7 | gut |
| kreuzung | 2 (102, 104) | | 6 bis 7 | gut |
| uhr | 0 | 106 | 6 bis 7 | gut |
| figuren | 0 | 119 | 6 bis 7 | etwa 4 echte (B9) |
| verstehen (Winkel) | 2 (124, 126) | | 6 bis 7 | gut |
| Summe | 21 | bis 29 | | |

Formal hat jedes Lernziel mindestens 5 verschiedene Kategorien und keine mehr als zweimal. Inhaltlich zählen saeulendiagramm und figuren weniger.

## Auswahl-Statistik (64 Aufgaben, eigene Zählung)

- Platz der richtigen Option 1 bis 4: je 16. Folge: 2431414213421213232431241343434312434212134232324134314142121213. Kein erkennbares Muster. Pro Lernziel nie derselbe Platz zweimal hintereinander. Einzelne Lernziele wechseln allerdings regelmäßig (figuren 2,1,2,1; graph_lesen 2,1,2,1,3).
- Rang der richtigen Option nach Länge 1 bis 4 (1 = kürzeste): 18, 25, 12, 9. Mittlere Länge 73,3 (richtig) gegen 72,9 (falsch).
- "denn/weil": 78 % richtig, 78 % falsch.
- "=" in der Option: 17 % gegen 18 %.
- Sammel-Optionen: 6 % gegen 4 %.
- Breite Absolutwörter (immer, alle, jede, keine): 11 % gegen 10 %.
- "nicht/kein/nie": 8 % richtig gegen 16 % falsch (falsche häufiger negiert).
- Zahl in der Option: 89 % gegen 77 %.
- "Ja/Nein" am Anfang: 3 % gegen 3 %.
- Auffällige Startwörter der richtigen: "Er" 7 mal, "Beide" 4 mal, "Der" 4 mal.
- Hedge-Wörter: siehe B6.
- Genau eine Option ist wahr in allen 64, keine zufällig zweite richtige.

## Offene Lehrplan- und Klassenstufen-Zweifel (mit ehrlicher Sicherheit)

- 001: Prozentfaktoren bei drei Kanten. Etwa 60 % sicher, dass es für Klasse 6 machbar ist.
- 036: Streckfaktor 2,5 im Maßstab. Etwa 55 %.
- 043: mehrstufig mit Prozent. Etwa 60 %.
- 106: Dezimalwinkel 7,5° in Klasse 5. Etwa 60 %. Alternative: 10 Minuten je Stunde gibt 75°, ganzzahlig.
- 113: Variable x und Gleichung 6x = 90 in Klasse 5. Etwa 65 %.
- 118: Taubenschlag-Argument in Klasse 5, schwer einzuschätzen.
- 117: Winkelhalbierende, im Bestand erst Klasse 7.
- 100: Paar-Argument bei 3 Geraden.
- 058: negative Zahlen (Klasse 6).
- 046 und 047: Prozentpunkte stehen im Bestand der Einheit schon (daten.darstellen#229/#232), daher geringerer Zweifel.
- 022: setzt gerades Stapeln voraus (im Text gesagt, in Ordnung).

Ich habe keinen Lehrplantext vorliegen. Diese Einschätzungen beruhen auf Kenntnis des bayerischen Gymnasiallehrplans und dem Stufenvergleich mit dem Bestand.
