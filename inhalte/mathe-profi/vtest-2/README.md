# Verstehen in Tests, Stufe 1, Runde 2 (VT2-001 bis VT2-133)

Nicht eingespielt. 19 Lernziele je 7 Aufgaben: 1 Test (`ersetzt_test: true`), 3 Korrektur, 3 Sicherung. Auswahl und Gründe stehen in `auswahl.md`. Die Überarbeitung nach der Vorprüfung (Zweig `vorpruefer-vt2`) steht Kennung für Kennung in `korrektur-nach-vorpruefung.md` und `korrektur-nach-vorpruefung-2.md`; der Handvergleich mit dem Bestand steht in `bestandsvergleich.md`.

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

## Verteilung (Stand nach der Überarbeitung)

- Pool: test 19, korrektur 57, sicherung 57.
- Stufe: 2 hat 81, 3 hat 52. Alle 19 Tests sind Stufe 3.
- Antwortform gesamt: luecken 47, auswahl 44, zahl 42. Im Test-Pool: zahl 8, luecken 9, auswahl 2.
- Platz der richtigen Möglichkeit bei den 44 Auswahlaufgaben: A 9, B 13, C 10, D 12. Richtige am längsten in 13 von 44; mittleres Längenverhältnis richtig/falsch 1,13.
- Muster: denn/weil falsch/richtig 57/57 %; Absolutwörter 30/32 %; Sammel-Möglichkeiten 5, davon 2 richtig.
- Typ: transfer 34, begruenden 33, fehler 18, darstellung 15, rueckwaerts 13, parameter 10, umkehr 7, pruefung 3.
- Form: ohne 88, anwenden 20, fehler_detektiv 18, umkehren 2, bruecke 2, verfahren_waehlen 2, zwei_wege 1.

## Denkfiguren

Jede Aufgabe trägt das Feld `idee` (Liste in `ideen.py`). Je Lernziel gibt es sieben verschiedene, keine öfter als zweimal; das prüft `bauen.py` fest. Umkehr- und Rückwärtsaufgaben zählen als eine Idee. Der Vorprüfer hatte bei umkehrung und jahreszinsen_komma nur 2–3 echte Denkfiguren gesehen; beide Lernziele wurden neu aufgebaut:
- umkehrung: Länge MC aus rechtem Winkel (064), Koordinate (065), Umkreisradius und Hypotenuse (066), Fehlersuche Radius/Durchmesser (067), Ortslinie aller Punkte mit rechtem Winkel (068), Hypotenuse als Durchmesser des Umkreises (069), Winkel in den gleichschenkligen Teildreiecken (070).
- jahreszinsen_komma: Fehlersuche Faktor (008), Zehnerpotenzen (009), Zinssatz als Faktor (010), Ergebnis mit Begründung (011), Zinssatz aus dem Zinsbetrag (012), Kapital und Zinssatz verrechnen (013), Zinssatz zerlegen (014).

## Feste Prüfungen

- `python3 -I inhalte/mathe-profi/vtest-2/bauen.py` baut die JSON-Dateien und bricht mit Fehler ab, wenn: die richtige Möglichkeit in mehr als 35 % der Auswahlaufgaben die eindeutig längste ist, ein Platz A bis D unter 16 % oder über 34 % liegt, mehr als die Hälfte aller Aufgaben Auswahl ist, mehr als 7 Test-Aufgaben Auswahl sind, ein Lernziel weniger als 5 verschiedene Ideen oder eine Idee öfter als zweimal hat, die richtige Möglichkeit als einzige mit oder ohne denn/weil gebaut ist, die Lücke bei denn/weil oder Absolutwörtern über 12 Punkte liegt, Sammel-Möglichkeiten (ab 5) unter 25 % richtig sind oder die mittlere Länge richtig/falsch außerhalb 0,90 bis 1,15 liegt.
- `python3 -I tools/vtest_pruefen.py --runde 2`: keine Fehler, drei Hinweise „Text verlangt Runden, Feld runden fehlt“ (VT2-106, 108, 118). Falscher Alarm: Gerundet wird nur in der Voraussetzung, die Soll-Antwort ist eine exakte ganze Zahl (Anzahl, größte Abweichung, Euro-Unterschied). Ein Feld `runden` würde die Prüfung der Fehlbilder verfälschen.
- `python3 -I inhalte/mathe-profi/vtest-2/gegenrechnung.py`: rechnet alle 133 Sollwerte auf einem anderen Weg nach (Bruchrechnung, Aufzählen, Einsetzen, Zeichenketten), prüft zusätzlich, dass jede Aufgabe abgedeckt ist und keine zwei Aufgaben im selben Pool und Lernziel dieselbe Sollantwort haben. Ausgabe: „0 Abweichungen“.
- `sonderfaelle.md`: zu jeder Aufgabe ein Satz zum geprüften Sonderfall.

## Lehrplan und Zweifel

1. **Umkehrung des Satzes des Thales und Lage Gerade/Kreis (VT2-064 bis 077):** Laut `inhalte/themen/geometrie.kreis.json` (Merke und Abschnitte „Satz des Thales“, „Tangenten“) und Themenliste (Lernbereich M7 5, Zeile „Satz des Thales und seine Umkehrung beweisen und anwenden“) gehören beide Teile zur Einheit. Der Vorprüfer hat den Originaltext des Lehrplans nicht abrufen können und ist nur zu etwa 75 % sicher; ich habe ihn ebenfalls nicht abgerufen. Passante/Tangente/Sekante stehen in der Merke der Einheit, im Gymnasium-Zitat der Themenliste aber nur „Tangente von einem äußeren Punkt konstruieren“. **Offen, die Gegenprüfung entscheidet.** Die Aufgaben benutzen weder Pythagoras noch Wurzeln.
2. **Sammel-Möglichkeiten:** 5, davon 2 richtig (115, 129); die Verteilung wird fest geprüft.
3. **Auswahlzahl:** 44 von 133 (33 %). Wo eine Zahl- oder Lückenaufgabe dieselbe Einsicht prüft, wurde sie bevorzugt. Die App mischt die Optionen im Test nach Auskunft des Koordinators nicht; die Positionen sind deshalb im Bauskript fest gesetzt, nicht erst beim Anzeigen.
4. **Handvergleich mit dem Bestand:** je Lernziel alle sieben Aufgaben gegen Übung, Test und `rollend-*` gelesen, Ergebnis in `bestandsvergleich.md`; dabei wurden weitere Doppelungen ersetzt. Eine Restunsicherheit bleibt bei den dort genannten nahen, aber im Fragefokus verschiedenen Aufgaben.
5. **Schema-nahe Aufgaben:** höchstens zwei je Lernziel nach meiner Einschätzung; die Einschätzung ist nicht unabhängig. Zu prüfen: VT2-006, 010, 032, 046/048/049, 056, 060, 061, 087/090, 093, 104, 118.
6. **Gleiche Lückenwerte:** VT2-013 und VT2-023 haben absichtlich zwei gleiche Lückenwerte (36/36 und 50/50), weil genau das die Einsicht ist; das Prüfwerkzeug nimmt es an.
7. **Zahlen ohne Zinseszins:** Alle Zinsaufgaben bleiben innerhalb eines Jahres (VT2-025 jetzt 3, 8, 9 Monate).
8. **Lehrplanzweifel VT2-005 (vermehrter Grundwert, 5 150 : 1,03):** Ob das in M6 3 (Zinsen) vorkommt, habe ich nicht bestätigen können; die Gegenprüfung soll entscheiden, ob 005 bleibt.
9. **Überschneidung VT2-079/081:** beide behandeln die Verwechslung von Inkreis- und Umkreiskonstruktion, mit unterschiedlicher Frage.
10. **Eigene Zahlen und Texte:** nichts aus Schulbüchern oder Prüfungen. Namen sind neutral (Mia, Ben, Jonas, Frau Berger, Familie Koch).

## Was die Gegenprüfer ansehen sollten

- Die Aufgaben der geometrie.kreis (VT2-064 bis 084): Lehrplan, Fehlbild-Texte, Lage der Punkte in 068.
- Die ersetzten Test-Aufgaben: VT2-001, 008, 022, 029, 043, 050, 071, 078, 085, 092, 099, 106, 120, 127 (Schwierigkeit, Eindeutigkeit).
- Die neuen Lücken-Aufgaben mit Zeilenfehlern (VT2-081, 120) und die Aufgaben mit zwei gleichen Lückenwerten (013, 023).
- Doppelungen mit `rollend-*` und `themen`, die das Werkzeug nicht erkennt.
