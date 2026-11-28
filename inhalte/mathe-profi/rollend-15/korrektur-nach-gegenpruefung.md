# Korrektur nach der Gegenprüfung (Runde 15, Werkstatt 1197)

Grundlage: Gegenprüfung zu Stand 75cfbedb (= 2a9de0ca). Nach der Korrektur: `bauen.py` endet mit `OK`, `vorrat_pruefen` 0 Meldungen in allen vier Gruppen, Doppelungsprüfung gegen Bestand und frühere Runden ohne Fund, `gegenrechnung.py` endet mit „0 Abweichungen“.

## Neue Prüfungen

- **Toleranz:** Keine Aufgabe der Runde hat noch `toleranz`. `bauen.py` verweigert jede Toleranz bei verlangter Rundung (gerundeter Wert zählt exakt) und jede andere nur mit Einzelbegründung (`TOL_BEGRUENDET`, derzeit leer) und nur kleiner als der Abstand der Nachbarwerte der letzten Stelle. `gegenrechnung.py` prüft zusätzlich, dass kein gespeicherter Wert mehr Stellen hat als verlangt.
- **Fehlbild-Text ↔ Zahl:** (1) Alle 420 Fehlbilder der Zahl- und Lückenaufgaben sind ausführbare Rechnungen und werden gegen den gespeicherten Wert geprüft (vorher 419, V116 Lücke 1 jetzt `floor(sqrt(343))`). (2) Neu: Jede Zahl in einer Fehlbild-Beschreibung muss aus der Aufgabe oder aus den Zwischenwerten der Rechnung stammen; Ausnahmen stehen mit Nachrechnung in `FB_ZAHL_OK`. (3) Neu: „√N ≈ x“ in Beschreibungen wird nachgerechnet. Alle 585 Fehlbilder wurden danach noch einmal von Hand gelesen; gefunden wurde zusätzlich V069 ③ (Wert 242 mit „+ 62“ gerechnet, jetzt „Außenwinkel 121° statt Innenwinkel an C addiert“).
- **Prüfdatei:** `vorpruefung_rechnen.py` gehört dem Vorprüfer und bleibt unverändert. Seine drei Abweichungen (V011, V054, V203) kommen von veralteten Erwartungswerten zu den Aufgaben vor der Vorprüfungs-Korrektur (richtig: 480 · 1,12 · 1,05 = 564,48; Lücken 6 / 12 / 18; V203 war 33 : 55 = 0,6 und ist jetzt ersetzt); ebenso die Ausgaben zu V120/V140. Eigene aktuelle Prüfung: `gegenrechnung.py` rechnet alle 207 Sollwerte unabhängig neu.

## Tabelle

| Kennung | Befund | alt → neu bzw. warum nicht |
|---|---|---|
| V015 | Zweite Aussage auch begründbar | Frage verlangt ausdrücklich das relative (prozentuale) Wachstum |
| V053 | Zwei Winkelhalbierende | Richtig: „beide Winkelhalbierende der Straßen“ mit der Mittelsenkrechten; Erklärung: höchstens zwei Orte |
| V058 | Parallelogramm könnte Rechteck/Raute sein | Text: „ein allgemeines Parallelogramm, das weder Rechteck noch Raute ist“ |
| V059 | Fehlbild 303 falsch erklärt | Rechnung 360 − 52 − 71 = 237 (Beschreibung „vom Vollwinkel 360° statt von 180°“ passt jetzt) |
| V072 | 15-Eck: n − 1 = 14, nicht 12 | Fehlbild 12 = n − 3 Diagonalen von einer Ecke; „konvexes Vieleck“, „durch Diagonalen von einer Ecke“ |
| V077 | innenliegende Diagonale | „eine Diagonale, die im Inneren des Vierecks liegt“ |
| V116 | 18 bei √343 ≈ 18,52 | Beschreibung „… ≈ 18,52 und auf 18 abgerundet“, Rechnung `floor(sqrt(343))` |
| V131 | 1,75 = halber Unterschied | Fehlbild 1,75 = 6,25 − 4,5 („von der neuen Länge die alte Breite abgezogen“) |
| V134 | „7 statt 49“ führt zu 7, nicht 35 | Fehlweg 245 : 7 = 35 („durch 7 statt durch 5 geteilt“) |
| V140 | 14 ≠ 7 + (−7) | Fehlwert 14 = 7 + 7 („Beträge addiert“), Rechnung `{2} + {2}` |
| V168 | 1681 : 2 = 840,5 | „(840,5) und auf 840 abgerundet“ |
| V138 | Rückmeldung dritte Option | „bei gekürztem Bruch wäre q zwar ungerade, aus p = 2k folgt aber q² = 2k², also ist q gerade: genau das ist der Widerspruch“ |
| V009 | ±0,1 unnötig | `toleranz` weg (exakt 5 %) |
| V012, V115, V130, V184, V185, V186, V189, V191, V192 | Nachbarwerte der Rundung zählten mit | `toleranz` entfernt; in den Winkel- und Seitenaufgaben zusätzlich „Runde erst das Endergebnis“ |
| V204, V205 | Toleranz / M10, M11 | ersetzt (siehe unten) |
| V193 | Duplikat von Live-ID 35894 / 38184 | ersetzt: Menge der Quadratzahlen zwischen 70 und 700 (Soll 18; Fehlbilder 17 / 19 / 26) |
| V194 | Duplikat von Live-ID 21567 / 38171 | umgebaut: Teiler von 60 und 45, gefragt „in A, aber nicht in B“ (Soll 8; Fehlbilder 12 / 4 / 2) |
| V203 | M11 (bedingte Wahrscheinlichkeit) | ersetzt: Therme, 55 % / 44 % / 33 %, „weder Frau noch Sauna“ (Anteil aller Besucher, Soll 34 %) |
| V204 | M10 (Ziehen ohne Zurücklegen) | ersetzt: Campingplatz 52 % / 31 % / 18 %, „genau eines der Geräte“ (Soll 47 %) |
| V205 | M11 (Rückschluss) | ersetzt: Additionssatz rückwärts, P(A ∩ B) = 0,42 + 0,35 − 0,61 = 0,16 |
| V206 | M11 | ersetzt: aus P(A ∪ B) = P(A) + P(B) folgt P(A ∩ B) = 0 |
| V207 | M11 | ersetzt: Fehler-Detektiv zum Additionssatz (Schnitt nicht abgezogen, Zeile 3). Die Etappen „bedingt“ und „rueckschluss“ bleiben mit Aufgaben zu Anteilen aller Gäste besetzt, weil die Etappenliste der Einheit feststeht |
| V049 | Zeile 3 unabhängig richtig, nah an Live-ID 48186 | neu: Dreieck A(2\|1), B(5\|1), C(2\|4) an der y-Achse, Fehler C′ in Zeile 2, Zeile 3 folgt daraus |
| V054 | Tipp unterschlägt Seitenmitten-Achsen | Tipp: bei geradem n Achsen durch Ecken oder Seitenmitten; „Addiere die Anzahlen der beiden einzelnen Figuren“ |
| V010 | 18 nicht der größte neue Preis | Museumsoption: „steigt mit 3 € mehr als der Bus …“, Irrtum: nur in Euro verglichen |
| V092 | Diagonalen allgemein | Optionen nennen die angebotene Raute und das Parallelogramm (7 cm / etwa 4,36 cm) |
| V106 | Fehlwert 4 | „von der 10 noch das Dreifache von 2 abgezogen“ (5 · 2 − 3 · 2); Fehlwert 7: „5 und 2 addiert“ |
| V112 | Weg fehlte | 11858 = 5929 : 2, dann mal 4; 1482,25 = Fläche durch 4 als Rundenlänge |
| V170, V174 | Rundung im Fehlbild | 62 = √(61² + 11²) ≈ 61,98 gerundet; 8,2 = √(2² + 8²) ≈ 8,246 gerundet. Gleiches bei V183 (≈ 42,7) |
| V126, V127 | „zwischen ganzen Zahlen“ beweist nichts | Begründung: 50, 20, 45 sind keine Quadratzahlen, Wurzel aus nichtquadratischer natürlicher Zahl ist irrational |
| V139 | p, q positiv | Text: „gekürzter Bruch mit positiven ganzen Zahlen p und q“ |
| V162 | 5 ist waagerechter Abstand | „waagerechten Abstand eines Schnittpunkts zur Symmetrieachse x = −2“ |
| V189 | Fußpunkt, waagerecht | „Fuß des Leuchtturms liegt auf Meereshöhe“, „waagerecht“ |
| V180–V186, V189, V190 | Regel nur Teilregel | Kennung bleibt, aber als „Nur Teilregel“ im Zweifelsfall ausgewiesen (V180/181: Seitenlage relativ zum Winkel; V182–V190: Verhältnisformeln stehen nicht im Katalogtext; die Formeln stehen in Tipp und Lösungsweg) |
| V147, V148, V151, V153 | rr.reihenfolge trägt Formelwahl nicht | als „Nur Teilregel“ ausgewiesen; V149, V161, V162 ebenso (Waage bzw. Zuordnung decken nur Teile) |
| V103, V104 | rr.waage beschreibt anderen Weg | Regel entfernt, Begründung „Probe durch Einsetzen“ (Regeln 38 ohne, 169 mit) |
| V013, V014 | Hinweis | unverändert: Probieren und Iterieren, keine Logarithmen nötig (Tipp sagt „probiere“) |
| V021 | richtiger, umständlicher Weg | Frage „am geschicktesten, also am wenigsten Rechenaufwand“; Rückmeldung nennt den Weg richtig, aber umständlich |
| V042 | schriftlicher Weg | Erklärung führt 8 · 197 schriftlich vor (Überträge) |
| V083 | vierte Option | Erklärung: 7 · sin 40° ≈ 4,5 < 5 < 7, also zwei Dreiecke; Probe im Programm |
| V085 | genau 4 bis 12 | Erklärung nennt „genau c = 4, 5, …, 12“ |
| V122 | genau 5 bis 12 | Text und Erklärung nennen bereits 5 bis 12, unverändert |
| V129 | genau 2,61 bis 2,64 | Erklärung ergänzt: 2,65 bis 2,69 haben ein Quadrat über 7 |
| V195 | genau 20 einschließlich 60 | unverändert (Text sagt „60 eingeschlossen“, Erklärung zählt 60 mit) |
| V143 | jetzt eindeutig | unverändert |
| V007, V008, V035, V052, V059, V079–V081, V090, V130, V131, V133 | in Ordnung | unverändert (Regel-Ausnahmen und Nichtzuordnung bestätigt) |
| Auswahl | Boxplot und Kreis vormerken | in `auswahl.md` vermerkt: `daten.boxplot` und `geometrie.kreis` für Runde 16 |
