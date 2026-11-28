# Verstehen in Tests, Stufe 1, Runde 2 (VT2-001 bis VT2-133)

Nicht eingespielt. 19 Lernziele je 7 Aufgaben: 1 Test (`ersetzt_test: true`), 3 Korrektur, 3 Sicherung. Auswahl und Gründe stehen in `auswahl.md`. Die Überarbeitung nach der Vorprüfung (Zweig `vorpruefer-vt2`) steht Kennung für Kennung in `korrektur-nach-vorpruefung.md` `korrektur-nach-vorpruefung-2.md` und `korrektur-nach-vorpruefung-3.md`; der Handvergleich mit dem Bestand steht in `bestandsvergleich.md`.

## Übersicht

| Einheit | Lernziele | Aufgaben | Lehrplan |
|---|---|---|---|
| finanzen.zinsen | rollen, jahreszinsen_komma, kapital, zeitanteil | 28 | M6 3 (Zinsen) |
| terme.umformen | zusammenfassen, minusklammer, aequivalenz | 21 | M7 1 (Terme) |
| terme.umformen_teil2 | ausklammern, binomisch | 14 | M7 1 (Terme) |
| geometrie.kreis | umkehrung, lage, umkreis_inkreis | 21 | M7 5 (Kreis) |
| zahlen.natuerlich | stellenwert, ziffern_zu_zahlwort, strahl_eintragen, runden_regel, runden_sinnvoll, roemisch_schreiben, dualsystem | 49 | M5 1 (Natürliche Zahlen) |
| Summe | 19 | 133 | |

Nummerierung nach der Themenliste im Repo (Gymnasium).

## Verteilung (Stand nach Urteil 1222)

- Pool: test 19, korrektur 57, sicherung 57.
- Stufe: 2 hat 84, 3 hat 49. Alle 19 Tests sind Stufe 3.
- Antwortform gesamt: luecken 47, auswahl 43, zahl 43. Im Test-Pool: luecken 12, zahl 7, auswahl 0.
- Platz der richtigen Möglichkeit bei den 43 Auswahlaufgaben: A 9, B 12, C 10, D 12. Richtige strikt am längsten in 12 von 43; mittleres Längenverhältnis richtig/falsch 1,06; mindestens 25 % länger als die längste falsche nur in 054 und 059.
- Muster: denn/weil falsch/richtig 68/67 %; Absolutwörter 35/33 %; Nebensatz-Marker (Semikolon, „aber“, „, nicht“) 9/12 %; Sammel-Möglichkeiten nach dem Anfangswort 8, davon 5 richtig. Bauart-Muster („=“, „<“, „>“, kleiner, größer, gleich, nicht nur in der richtigen Möglichkeit): 0 Aufgaben (fest geprüft, höchstens 10 % erlaubt).
- Fehler-Detektive: 15; Fehlerzeile 1 dreimal, Zeile 2 fünfmal, Zeile 3 sechsmal, Zeile 4 einmal (120). Tests: 008 Zeile 3, 057 Zeile 2, 120 Zeile 4. Aus 036 und 062 sind keine Fehler-Detektive mehr geworden (036: Parameteraufgabe als Test, 062: Term für den Unterschied).
- Typ: transfer 37, begruenden 36, fehler 15, darstellung 15, rueckwaerts 14, parameter 8, umkehr 7, pruefung 1.
- Form: ohne 96, anwenden 18, fehler_detektiv 15, umkehren 2, bruecke 1, zwei_wege 1.

## Denkfiguren

Jede Aufgabe trägt das Feld `idee` (Liste in `ideen.py`). Je Lernziel gibt es sieben verschiedene, keine öfter als zweimal; das prüft `bauen.py` fest. Umkehr- und Rückwärtsaufgaben zählen als eine Idee. Der Vorprüfer hatte bei umkehrung und jahreszinsen_komma nur 2–3 echte Denkfiguren gesehen; beide Lernziele wurden neu aufgebaut:
- umkehrung: Länge MC aus rechtem Winkel (064), Koordinate (065), Umkreisradius und Hypotenuse (066), Fehlersuche Radius/Durchmesser (067), Ortslinie aller Punkte mit rechtem Winkel (068), Hypotenuse als Durchmesser des Umkreises (069), Winkel in den gleichschenkligen Teildreiecken (070).
- jahreszinsen_komma: Fehlersuche Faktor (008), Zehnerpotenzen (009), Zinssatz als Faktor (010), Ergebnis mit Begründung (011), Zinssatz aus dem Zinsbetrag (012), Kapital und Zinssatz verrechnen (013), Zinssatz zerlegen (014).

## Feste Prüfungen

- `python3 -I inhalte/mathe-profi/vtest-2/bauen.py` baut die JSON-Dateien und bricht mit Fehler ab, wenn: die richtige Möglichkeit in mehr als 35 % der Auswahlaufgaben die eindeutig längste ist, ein Platz A bis D unter 16 % oder über 34 % liegt, mehr als die Hälfte aller Aufgaben Auswahl ist, mehr als 7 Test-Aufgaben Auswahl sind, ein Lernziel weniger als 5 verschiedene Ideen oder eine Idee öfter als zweimal hat, die richtige Möglichkeit als einzige mit oder ohne denn/weil gebaut ist, die Lücke bei denn/weil oder Absolutwörtern über 12 Punkte liegt, Sammel-Möglichkeiten (ab 5) unter 25 % richtig sind die mittlere Länge richtig/falsch außerhalb 0,90 bis 1,15 liegt, eine Lücke kein Fehlbild hat, die Fehlerzeilen der Fehler-Detektive ungünstig verteilt sind (mindestens zwei Aufgaben mit Zeile 1, keine Zeile über 45 %, in den Tests mindestens drei verschiedene Zeilen), die richtige Möglichkeit in mehr als 15 % der Auswahlaufgaben mindestens 25 % länger als die längste falsche ist oder die Nebensatz-Marker (Semikolon, „aber“, „, nicht“, „, auch“) zwischen richtigen und falschen um mehr als 12 Punkte abweichen.
- `python3 -I tools/vtest_pruefen.py --runde 2`: keine Fehler, zwei Hinweise „Text verlangt Runden, Feld runden fehlt“ (VT2-106, 108). Falscher Alarm: Gerundet wird nur in der Voraussetzung, die Soll-Antwort ist eine exakte ganze Zahl (Anzahl, größte Abweichung, Euro-Unterschied). Ein Feld `runden` würde die Prüfung der Fehlbilder verfälschen.
- `python3 -I inhalte/mathe-profi/vtest-2/gegenrechnung.py`: rechnet alle 133 Sollwerte auf einem anderen Weg nach (Bruchrechnung, Aufzählen, Einsetzen, Zeichenketten), prüft zusätzlich, dass jede Aufgabe abgedeckt ist und keine zwei Aufgaben im selben Pool und Lernziel dieselbe Sollantwort haben. Ausgabe: „0 Abweichungen“.
- `sonderfaelle.md`: zu jeder Aufgabe ein Satz zum geprüften Sonderfall.

## Lehrplan und Zweifel

1. **Umkehrung des Satzes des Thales und Lage Gerade/Kreis (VT2-064 bis 077):** Laut `inhalte/themen/geometrie.kreis.json` (Merke und Abschnitte „Satz des Thales“, „Tangenten“) und Themenliste (Lernbereich M7 5, Zeile „Satz des Thales und seine Umkehrung beweisen und anwenden“) gehören beide Teile zur Einheit. Der Vorprüfer hat den Originaltext des Lehrplans nicht abrufen können und ist nur zu etwa 75 % sicher; ich habe ihn ebenfalls nicht abgerufen. Passante/Tangente/Sekante stehen in der Merke der Einheit, im Gymnasium-Zitat der Themenliste aber nur „Tangente von einem äußeren Punkt konstruieren“. **Offen, die Gegenprüfung entscheidet.** Die Aufgaben benutzen weder Pythagoras noch Wurzeln.
2. **Sammel-Möglichkeiten:** nach dem Anfangswort 5, davon 2 richtig (115, 129); die Vorprüfung zählt 7 mit „Weder …“, davon 3 richtig (110, 115, 129). Die Verteilung wird fest geprüft.
3. **Auswahlzahl:** 41 von 133 (31 %). Wo eine Zahl- oder Lückenaufgabe dieselbe Einsicht prüft, wurde sie bevorzugt. Die App mischt die Optionen im Test nach Auskunft des Koordinators nicht; die Positionen sind deshalb im Bauskript fest gesetzt, nicht erst beim Anzeigen.
4. **Handvergleich mit dem Bestand:** je Lernziel alle sieben Aufgaben gegen Übung, Test und `rollend-*` gelesen, Ergebnis in `bestandsvergleich.md`; dabei wurden weitere Doppelungen ersetzt. Eine Restunsicherheit bleibt bei den dort genannten nahen, aber im Fragefokus verschiedenen Aufgaben.
5. **Schema-Zählung nach Urteil 1222 (streng, auch Zahlenvergleich und Fehler-Detektive, die man durch bloßes Ausrechnen löst; im Zweifel als Schema gezählt).** Schema: Aufgaben, die mit dem geübten Verfahren ohne eigene Einsicht lösbar sind. Ergebnis je Lernziel (Kennungen), Soll höchstens 2:
   - rollen 5 (001, 002, 005, 006, 007); jahreszinsen_komma 4 (008, 009, 010, 011); kapital 3 (015, 017, 018); zeitanteil 3 (022, 025, 028)
   - zusammenfassen 3 (029, 032, 033); minusklammer 4 (037, 038, 041, 042); aequivalenz 5 (043, 044, 045, 046, 049)
   - ausklammern 3 (050, 052, 056); binomisch 2 (057, 060) ok; umkehrung 2 (066, 067) ok
   - lage 5 (071, 073, 074, 075, 076); umkreis_inkreis 3 (080, 081, 083)
   - stellenwert 2 (087, 088) ok; ziffern_zu_zahlwort 5 (092, 093, 094, 097, 098); strahl_eintragen 3 (099, 101, 102)
   - runden_regel 1 (109) ok; runden_sinnvoll 1 (113) ok; roemisch_schreiben 4 (120, 121, 122, 123); dualsystem 2 (130, 131) ok
   Das sind 5 Lernziele mit höchstens zwei und 14 darüber. Meine Zählung liegt über der der Gegenprüfung (3/4/2/4/4/3/2/3/3/2/2/3/3/3/4/3/2/2/2), weil ich im Zweifel streng zähle. Offene Arbeit: für die 14 Lernziele über zwei weitere Routinen durch Verstehens-Aufgaben ersetzen; die Einheiten zahlen.natuerlich und terme.umformen sind bis zum Ergebnis der unabhängigen Vorprüfung auf Commit 67a9f804 nicht angefasst.
6. **Gleiche Lückenwerte:** VT2-023 hat absichtlich zwei gleiche Lückenwerte (50/50), weil genau das die Einsicht ist; VT2-013 hat die Werte 36 und 39; VT2-046 hat ebenfalls zwei gleiche Werte beim Zahlenrätsel (3 und 3), weil der Wert unabhängig von der gedachten Zahl ist. Das Prüfwerkzeug nimmt es an.
7. **Zahlen ohne Zinseszins:** Alle Zinsaufgaben bleiben innerhalb eines Jahres (VT2-025 jetzt 3, 8, 9 Monate).
8. **Lehrplan (offen, nichts geraten):** (a) Lage Gerade/Kreis (VT2-071 bis 077): Der Vorprüfer fand die Wörter Passante und Sekante nicht im Text der Jahrgangsstufe 7 und kann nicht bestätigen, dass die Lage Gerade/Kreis dort steht (etwa 50 %, Jahrgangsstufe 8 nicht abrufbar). (b) Umkreis und Inkreis (VT2-078 bis 084): im Lernbereich nur als Beispielliste, die Lage des Umkreismittelpunkts nicht im Wortlaut (etwa 65 %). (c) Die Umkehrung des Satzes des Thales (VT2-064 bis 070) steht im Lehrplan (etwa 90 %). Der alte Zweifel zu VT2-005 (vermehrter Grundwert) entfällt, weil die Aufgabe ersetzt ist. Die Gegenprüfung soll (a) und (b) mit Schulbuch oder Schule klären.
9. **Überschneidung VT2-079/081 behoben:** 079 zählt Dreiecke nach der Lage des Umkreismittelpunkts, 081 (jetzt sicherung) sucht den Fehler in der Umkreiskonstruktion.
10. **Eigene Zahlen und Texte:** nichts aus Schulbüchern oder Prüfungen. Namen sind neutral (Mia, Ben, Jonas, Frau Berger, Familie Koch).

## Was die Gegenprüfer ansehen sollten

- Die Aufgaben der geometrie.kreis (VT2-064 bis 084): Lehrplan, Fehlbild-Texte, Lage der Punkte in 068.
- Die ersetzten Test-Aufgaben: VT2-001, 008, 015, 022, 029, 043, 050, 071, 078, 085, 092, 099, 106, 120, 127 (Schwierigkeit, Eindeutigkeit).
- Die Lücken-Aufgaben mit Zeilenfehlern (VT2-081, 120) und die Aufgaben mit zwei gleichen Lückenwerten (023, 046).
- Doppelungen mit `rollend-*` und `themen`, die das Werkzeug nicht erkennt.

## Urteil 1222 (Nachtrag)

- Befunde und Abhilfe Punkt für Punkt: `korrektur-nach-gegenpruefung.md`.
- Lehrplan: Thales samt Umkehrung, Tangente und Um-/Inkreis sind M7.5 und in Ordnung. Die Lage Gerade/Kreis (071 bis 077) und die Lage des Umkreismittelpunkts (078 bis 080) sind Ableitungen; Sekante, Tangente, Passante und das Kriterium (Abstand gegen Radius, Winkel gegen 90°) stehen deshalb in der Aufgabe selbst.
- 063: x ist als positive Zahl vorgegeben (kein Betrag nötig). 054: Aussage präzisiert. 067: neuer Kontext (Dreieck PQR). Pool-Tausch zum schwersten Kern im Test: 070 (Test) und 064 (Sicherung); 118 (Test) und 113 (Sicherung).
- Bestandsvergleich einschließlich `rollend-15` (207 Aufgaben): Nachtrag in `bestandsvergleich.md`.
