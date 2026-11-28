# Vorprüfung Runde 15 (unabhängig, alle 207 Aufgaben R15-V001 bis V207)

Geprüft wurde jede Aufgabe von Hand gelesen und rechnerisch nachvollzogen. Eigene Rechnung: `vorpruefung_rechnen.py` (141 Zahl- und Lückenaufgaben mit eigener Formel, exakte Brüche bzw. Zählschleifen; 66 Auswahlaufgaben mit eigener Entscheidung). Das Skript endet mit genau einer Meldung (V120, siehe unten). `python3 -I bauen.py` läuft durch und endet mit `OK` (884 Proben bestanden, `vorrat_pruefen.py` 0 Meldungen); die Lauf hat die Dateien nicht verändert.

## Gesamturteil: einspielbereit **nach Korrektur**

| Zahl | Wert |
|---|---|
| geprüft | 207 |
| Soll-Antwort nach eigener Rechnung richtig und eindeutig (ohne die A-Befunde) | 204 |
| Aufgaben mit Befund A (vor dem Einspielen korrigieren) | 3 (V120, V140, V143) |
| Aufgaben mit Befund B (sollte korrigiert werden) | 8 (V022, V031, V059, V085, V114, V153, V193, V195) |
| Aufgaben mit Befund C (Hinweis) | 20 |
| Aufgaben ganz ohne Befund | 176 |

Keine Soll-Antwort ist rechnerisch falsch. Die Mängel sind Eindeutigkeit und Bewertung (V120, V140, V143), Fehlbilder, deren Erklärtext nicht zur Rechnung passt, und Grenzen im Text. Alle Dreiecke und Figuren existieren (Dreiecksungleichung, Winkelsumme geprüft: V051, V088, V083, V173, V179 usw.).

## Befundtabelle

Schweregrad: A = fachlich falsch/mehrdeutig, vor dem Einspielen korrigieren; B = sollte korrigiert werden; C = Hinweis.

| Kennung | Grad | Befund | Korrekturvorschlag |
|---|---|---|---|
| V120 | A | Soll 9,2 mit `toleranz` 0,1. Die Datenbank prüft `abs(v - wert) <= toleranz` mit exakter Dezimalrechnung. Dadurch wird auch 9,3 (das Fehlbild „zu weit gerundet“) und 9,1 als richtig gewertet. Fehlbild nicht erreichbar, falsche Rundung gilt als richtig. Auch der Rundungs-Anspruch „auf eine Dezimalstelle“ ist damit aufgeweicht. | `toleranz` 0,04 (oder weglassen: √85 = 9,2195, der gerundete Wert 9,2 ist exakt vorgegeben). Allgemein: Toleranz kleiner als eine Einheit der letzten Stelle wählen, wenn ein Fehlbild genau eine Einheit daneben liegt. |
| V140 | A | Lücken ② und ③ („die beiden Lösungen sind ② und ③“): Soll ② = 7, ③ = −7. Wer −7 und 7 einträgt, hat richtig gerechnet und wird falsch gewertet; Reihenfolge ist nicht vorgegeben. | Text: „② ist die positive, ③ die negative Lösung.“ |
| V143 | A | Fehler-Detektiv, Soll Zeile 3. Der Lösungsweg selbst sagt, dass die Lösung x = 0 beim Teilen durch 6x verloren geht, also in Zeile 1. Zeile 1 ist als Rechenschritt („dann bleibt x = 3“) nur unter x ≠ 0 richtig; die falsche Aussage „nur die Lösung x = 3“ steht in Zeile 3. Antwort „Zeile 1“ ist vertretbar und bekommt die Rückmeldung „diese Zeile ist richtig“, die dem eigenen Lösungsweg widerspricht. | Zeile 1 umformulieren („Teile ich beide Seiten durch x, bleibt 6x = 18, also x = 3“ – falsch bleibt dann auch Zeile 1) oder besser Zeile 1 ohne Teilen („Ich bringe alles auf eine Seite: 6x² − 18x = 0“) und den Fehler in Zeile 2 („Teile ich durch 6x, ist x = 3“) oder die Lösungsmenge in Zeile 3 setzen; Rückmeldung für Zeile 1 anpassen. |
| V022 | B | „Für welche Zahl im Kästchen gilt 14⁴ = 2⁴ · □⁴?“ Auch −7 erfüllt das. | „natürliche Zahl“ in den Text. |
| V031 | B | Fehlbild 2048: Erklärtext „bei Potenz von Potenz die Hochzahlen addiert“ ergibt (2⁹)² → 2¹¹, dann 2¹¹ : 2¹⁰ = **2**, nicht 2048. 2048 = 2¹¹ wäre ohne die Division. | Fehlbild 2 mit diesem Text, oder Text ändern („… und das Teilen durch 2¹⁰ vergessen“). |
| V059 | B | Fehlbild 303 = 360 − 57; Erklärtext „den Winkel an einer Gerade ergänzt“ passt nicht (Gerade wären 180°). | Text: „vom Vollwinkel 360° statt von 180° gerechnet“ (360 − 57). |
| V085 | B | Lücke 3, Fehlbild 10 mit Text „die Grenzen 3 und 13 mitgezählt“: das ergäbe 11. 10 = 13 − 3 ist die Differenz der Grenzen. | Fehlbild 11 (beide Grenzen) oder Text „nur 13 − 3 gerechnet“. |
| V114 | B | Fehlbild 130 mit Text „0,0169 mit der Zahl 100 …“: 0,0169 · 100 = 1,69. 130 entsteht aus 0,13 m in **Millimeter**. Fehlbild 1,3 (Text „Wurzel mit einer Dezimalstelle zu hoch …“) ist ebenfalls unklar (0,13 · 10). | Texte: 130 „in Millimeter statt Zentimeter umgerechnet“; 1,3 „mit 10 statt mit 100 in Zentimeter umgerechnet“. |
| V153 | B | Fehlbild 12 = (9 + 39) : 4 (Vorzeichenfehler bei −b); Text „durch 4 geteilt statt durch 2“ würde 7,5 ergeben. | Text: „−b falsch gesetzt (9 statt −9) und durch 4 geteilt“ oder anderen Wert wählen (z. B. 7,5). |
| V193 | B | Fehlbild 11, Text „… 9 und 99 mitgezählt, obwohl ihre Ziffernsumme 9 und 18 ist“: 9 hat die Ziffernsumme 9; sie ist nur nicht zweistellig. Text falsch. | „die einstellige 9 und die 99 (Ziffernsumme 18) mitgezählt“ oder Fehlbild ändern. |
| V195 | B | „Vielfache von 6 bis 60“: ob 60 (und 0) dazugehört, steht nicht im Text. Ohne 60 wären es 19, mit 0 wären es 21. | „von 6 bis 60 (60 eingeschlossen, ohne 0)“ bzw. „die Vielfachen von 6 zwischen 1 und 60 einschließlich“. |
| V003/V011 | C | Gleiche Einkleidung (Mietwagen Sizilien, 320 €, 15 %/8 %) in zwei Aufgaben. Gewollt als Kontrast (addieren vs. nacheinander), aber sehr ähnlich. | Eine Einkleidung wechseln. |
| V202/V203 | C | Gleiche Hotelgäste und gleiche Zahlen 0,6/0,45 (27 bzw. 24). | Eine Einkleidung/Zahl wechseln. |
| V054/V055 | C | Beide zählen Symmetrieachsen regelmäßiger Vielecke (Achteck in beiden). | Achteck in V054 durch Zehneck/Fünfeck ersetzen. |
| V033 | C | Fehlbild 168 „als wären a und b gleichartig“: 14 · 12 (nur a); wirkt zufällig. | Text „alle Glieder zu 14a zusammengefasst“. |
| V038 | C | Fehlbild 25 (7 + 9·2) „x nur beim Zahlglied eingesetzt“ ist erklärungsarm. | Text präzisieren. |
| V066 | C | Fehlbild 10: „14 und 20 falsch zusammengefasst und halbiert“, Rechnung nicht nachvollziehbar (20 : 2). | Text oder Wert anpassen. |
| V075 | C | Fehlbild −65 (negativer Winkel) ist als Eingabe unplausibel; Text erklärt das Entstehen aus „Summe 180°“. | Fehlbild 245 ist schon vorhanden; −65 ersetzen. |
| V089 | C | Option 4 (Winkel 70° bei A, 35° bei B) liefert ein zum gesuchten Dreieck kongruentes, nur anders benanntes Dreieck. Falsch nur wegen der Bezeichnung. | Text „… α = 35° bei A“ betonen oder Option ändern. |
| V103 | C | Fehlbild 26 („beide Seiten vermischt“) schwer nachvollziehbar. | Text präzisieren. |
| V105 | C | Fehlbildtext „unendlich viele“ („stimmen … gerade nicht überein“) verworren. | Neu formulieren. |
| V108 | C | Fehlbild 6 = Kims Fahrzeit (27·2 : (27−18)); Text „Vorsprung mit Alex' Tempo“ trifft nicht genau. | „Kims Fahrzeit statt Alex' Fahrzeit angegeben“. |
| V116 | C | Fehlbild 18 aus √343 = 18,52 abgerundet; für die Lücke unplausibel. | Fehlbild 21 (343 : 16?) oder nur mit Text „Wurzel statt dritte Wurzel (≈ 18)“. |
| V121, V126, V180 | C | V121 ist „begründen“, nicht „Verfahren wählen“; V126/V180 sind Erkennen auf Stufe 1, zählen aber (`zaehlt = ja`), im Gegensatz zu den Lückenwegen auf Stufe 1. Nur Einordnung. | Form zu „Anwenden“ ändern bzw. dokumentieren. |
| V045, V131 | C | Form „Umkehren“ stimmt nur lose (V045 prüft eine Behauptung; V131 ist Anwenden eines Rechenschritts). | Form prüfen. |
| V127 | C | „√2,25“ kann als √2 und 25 gelesen werden. | „√(2,25)“ schreiben. |
| V128 | C | „①² = 9“: Lücke formal auch −3; der Folgetext („zwischen ① und ②“) schließt das aus. | Hinweis „positive Zahl“. |
| V188 | C | Optionen 110° und 160° sowie der Erklärtext („180° − 70° gilt für den Sinus“) greifen auf Winkel über 90° vor, die in Klasse 9 nicht definiert sind. | Optionen durch spitze Winkel ersetzen (z. B. 20°, 50°, 70°, 45°). |
| alle Aufgaben mit `toleranz` | C | Standard ist 1 Einheit der letzten Stelle (inclusive): V009, V012, V115, V120, V130, V184, V185, V186, V189 (Toleranz 1 m), V191, V192, V204, V205 akzeptieren Nachbarrundungen. Nur bei V120 kollidiert das mit einem Fehlbild; sonst vertretbar. | Konvention festhalten. |

Ausdrücklich geprüft und in Ordnung (Auswahl): Zählaufgaben mit eigener Schleife V014, V022, V025, V037, V054, V055, V058, V072, V085, V086, V093, V122, V129, V193, V194, V195; Mengen/Wahrscheinlichkeit V196–V207 (Zahlen konsistent, z. B. V198 Vereinigung 19 ≤ 25, V201 Männer 48 ≥ 19). V122 (−3 bis 12 einschließlich: 5 bis 12 = 8), V129 (2,61 bis 2,69: vier Zahlen) eindeutig. V083 Option 4 liefert nachweislich zwei Dreiecke (β = 64,1° und 115,9°), V173/V175 eindeutig (längste Seite bzw. x > 0 vorgegeben). Fehler-Detektiv: bei allen übrigen 23 Aufgaben genau eine falsche Zeile, Folgezeilen rechnen richtig weiter.

Fehlbilder generell: in allen Zahlaufgaben verschieden und ungleich der Lösung; Lückenwege je Lücke verschieden. Nur die oben genannten Erklärtexte passen nicht zur Rechnung.

## Regel-Kennungen

- **V007/V008** (`rr.gegenrechnung`): vertretbar. Der tragende Schritt ist das Teilen durch den Faktor 1,08 bzw. 1,2/0,8, also Umkehren eines Malnehmens. `id.verhaeltnisse.prozent` ginge ebenso; da alle anderen Prozent-Aufgaben der Runde diese Regel tragen, wäre sie sogar konsistenter. Empfehlung: bei Wunsch nach Einheitlichkeit auf `id.verhaeltnisse.prozent` umstellen; kein Fehler.
- **V035** (`rr.tauschen`): vertretbar (Tauschen und Zusammenfassen von Faktoren), `rr.potenz` (a·a·a = a³) trüge den Schritt gleichwertig; da hier keine negativen Zahlen vorkommen, ist `rr.vorzeichen` zu Recht nicht gewählt.
- **Sieben Trigonometrie-Aufgaben** (V182–V186, V189, V190, `id.geometrie.rechtwinklig`): Die Regel trägt nur die Lage der Seiten (Gegen-/Ankathete, Hypotenuse), nicht das Rechnen mit sin/cos/tan. Bei V180/V181 trägt sie wirklich. Bei V182, V183, V190 trägt die Seitenzuordnung einen echten Teilschritt (Wahl des Verhältnisses); bei V184, V185, V186, V189 ist die Seitenwahl der einzige regelbezogene Schritt, das Verhältnis wird danach nur eingesetzt. Urteil: **vertretbar als Teilregel**, aber nicht „trägt den Lösungsweg“. Wenn der Katalog strikt „trägt“ verlangt, bei V184–V186/V189 ohne Regel setzen. Nicht blockierend.
- **Wurzel-/Nullstellen-Aufgaben:** `id.zahlen.hoch_zurueck` bei V126–V131, V133 trägt Wurzel↔Quadrat-Rückrechnen nur teilweise (V130 Heron, V131 Flächenerhalt tragen eher nichts davon). Zumindest V130, V131, V133 sollten besser ohne Regel bleiben. V121/V122 (Definitionsbereich) tragen teilweise. `id.funktionen.zuordnung` bei V161/V162 (y = 0 setzen) vertretbar, aber das Lösen trägt die Regel nicht. `rr.waage` bei V149 (Bruchgleichung): nur der erste Schritt (mit x multiplizieren); der Hauptteil ist Nullprodukt/Faktorisieren.
- **`id.geometrie.winkel` als Ausnahme** (V052, V059, V079, V080, V081, V090): fachlich richtig, die Winkelsumme trägt die Rechnung; die Lernkarten-Vorgabe (abstand/deckungsgleich bzw. keine Liste) passt für diese Aufgaben schlechter. Ausnahmen sind gut begründet. V052 ist zudem fast reine Dreieckswinkelsumme mit Halbieren; die Lernkarte „winkelhalbierende“ wird nur am Rand bedient (C).
- **29 Aufgaben ohne Regel:** Die Begründungen stimmen. Dreiecksungleichung (V085–V087), Satz/Kehrsatz (V091–V093), Mengen (V193–V199), Vierfeldertafel (V200–V201), Beweise (V138, V139), Quadratische Ergänzung (V146), Diskriminante (V150), Gleichsetzen (V164, V165) und Tangens-Steigung (V191, V192) haben tatsächlich keine genau passende Regel. Mögliche Kandidaten, die ich nicht gegen den Katalog entscheiden konnte: `id.daten.anteil` für V200/V201 (Anteile in der Tafel; ähnlich wie bei V202).
- Aufgabe V148/V151/V153 mit `rr.reihenfolge`: schwache Zuordnung (die Diskriminante ist ein Anwenden der Reihenfolge, aber nicht der Kern); ohne Regel wäre ebenso vertretbar.

## Auswahl der Einheiten (`auswahl.md`)

- Die Datei wurde nachträglich angelegt (steht im Text offen). Die Zahlen in der Tabelle sind plausibel.
- Klasse 9: Auswahl nach dem niedrigsten Anteil (6,4 bis 7,4 %) ist nachvollziehbar und konsistent; `abbildungen.aehnlichkeit` (7,6 %) knapp draußen, vertretbar.
- Klasse 7: Das Kriterium „in R8/9/10/14 nicht bedient“ ist ein anderes als „dünnster Anteil“. Nach Anteil wären `abbildungen.kongruenz` (6,0 %), `daten.boxplot` (6,5 %), `terme.potenzgesetze_natuerlich` (7,0 %), `geometrie.kreis` (7,7 %), `geometrie.konstruktion` (8,3 %) vor `bruch.prozent_grundwert` (11,1 %), `geometrie.winkelsaetze` (10,5 %) und `gleichungen.linear` (12,3 %). Gewählt wurden aber die drei Einheiten mit dem höchsten Anteil, während zwei dünnere (boxplot, kreis) fehlen. Das ist ein offener Widerspruch zum Ziel der Runde („dünnster Vorrat“), aber er ist offen dokumentiert und mit der Begründung „in früheren Runden bedient“ belegt. **Vertretbar, nicht blockierend**; wer das Ziel „dünnster Anteil“ strikt will, sollte in Runde 16 `daten.boxplot` und `geometrie.kreis` nachholen.
- Zählung, ob die Etappen-Bestände in der Tabelle stimmen, konnte ich nicht gegen die Datenbank prüfen.

## Was ich nicht prüfen konnte

- Keine Datenbank, keine App, keine Council-Werkzeuge: die Bewertungslogik der App habe ich nur an den SQL-Migrationen gelesen (Toleranz `<=`), nicht ausgeführt. Anzeige von Lückenfeldern und der Eingabeformate nicht gesehen.
- Passung zum bayerischen G9-Lehrplan: nur gegen den Plan im Repo gedacht; den amtlichen Lehrplan habe ich nicht abgeglichen. Besonders unsicher: stochastische Unabhängigkeit/Unvereinbarkeit (V207), Bayes-Rückschluss (V205), Zinseszins in Klasse 7 (V013, V014) und Irrationalitätsbeweis (V138/V139) in der jeweiligen Klasse.
- Nur ein Bild (`grafik`) ist in der Runde (V010, Tabelle); Aufgaben ohne Bild, die „Dreieck mit Winkeln α, β, γ an Geraden“ beschreiben (V063, V064), sind ohne Zeichnung nur durch die Beschriftungsvorgabe im Text eindeutig. Das ist ausreichend, aber nicht geprüft mit der Anzeige.
- Verwechslungsgefahr zwischen den rund 40 früheren Runden und R15 (Doppelungsprüfung) habe ich nicht neu durchgeführt, nur innerhalb der Runde gelesen.
- Rechtschreibung ist durch Lesen geprüft, nicht maschinell.
