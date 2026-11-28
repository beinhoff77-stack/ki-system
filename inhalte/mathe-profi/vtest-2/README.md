# Verstehen in Tests, Stufe 1, Runde 2 (VT2-001 bis VT2-133)

Nicht eingespielt. 19 Lernziele je 7 Aufgaben: 1 Test (`ersetzt_test: true`), 3 Korrektur, 3 Sicherung. Auswahl und Gründe stehen in `auswahl.md`. Die Überarbeitung nach der Vorprüfung (Zweig `vorpruefer-vt2`) steht Kennung für Kennung in `korrektur-nach-vorpruefung.md`.

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
- Stufe: 2 hat 79, 3 hat 54. Alle 19 Tests sind Stufe 3.
- Antwortform gesamt: auswahl 47, zahl 45, luecken 41. Im Test-Pool: zahl 10, luecken 5, auswahl 4.
- Platz der richtigen Möglichkeit bei den 47 Auswahlaufgaben: A 12, B 13, C 9, D 13. Mittlere Länge der richtigen 60 Zeichen, der falschen 61; nur in 1 von 47 ist sie die eindeutig längste.
- Typ: begruenden 33, transfer 30, fehler 19, rueckwaerts 12, darstellung 12, parameter 12, umkehr 11, pruefung 4.
- Form: ohne 86, fehler_detektiv 19, anwenden 18, umkehren 4, bruecke 2, verfahren_waehlen 2, zwei_wege 2.

## Denkfiguren

Jede Aufgabe trägt das Feld `idee` (Liste in `ideen.py`). Je Lernziel gibt es sieben verschiedene, keine öfter als zweimal; das prüft `bauen.py` fest. Umkehr- und Rückwärtsaufgaben zählen als eine Idee. Der Vorprüfer hatte bei umkehrung und jahreszinsen_komma nur 2–3 echte Denkfiguren gesehen; beide Lernziele wurden neu aufgebaut:
- umkehrung: Länge MC aus rechtem Winkel (064), Koordinate (065), Umkreisradius und Hypotenuse (066), Fehlersuche Radius/Durchmesser (067), Ortslinie aller Punkte mit rechtem Winkel (068), Hypotenuse als Durchmesser des Umkreises (069), Winkel in den gleichschenkligen Teildreiecken (070).
- jahreszinsen_komma: Fehlersuche Faktor (008), Zehnerpotenzen (009), Zinssatz als Faktor (010), Ergebnis mit Begründung (011), Zinssatz aus dem Zinsbetrag (012), Kapital und Zinssatz verrechnen (013), Zinssatz zerlegen (014).

## Feste Prüfungen

- `python3 -I inhalte/mathe-profi/vtest-2/bauen.py` baut die JSON-Dateien und bricht mit Fehler ab, wenn: die richtige Möglichkeit in mehr als 35 % der Auswahlaufgaben die eindeutig längste ist, ein Platz A bis D unter 16 % oder über 34 % liegt, mehr als die Hälfte aller Aufgaben Auswahl ist, mehr als 7 Test-Aufgaben Auswahl sind, oder ein Lernziel weniger als 5 verschiedene Ideen oder eine Idee öfter als zweimal hat.
- `python3 -I tools/vtest_pruefen.py --runde 2`: keine Fehler, fünf Hinweise „Text verlangt Runden, Feld runden fehlt“ (VT2-106, 108, 112, 113, 118). Falscher Alarm: Gerundet wird nur in der Voraussetzung, die Soll-Antwort ist eine exakte ganze Zahl (Anzahl, größte Abweichung, Euro-Unterschied). Ein Feld `runden` würde die Prüfung der Fehlbilder verfälschen.
- `python3 -I inhalte/mathe-profi/vtest-2/gegenrechnung.py`: rechnet alle 133 Sollwerte auf einem anderen Weg nach (Bruchrechnung, Aufzählen, Einsetzen, Zeichenketten), prüft zusätzlich, dass jede Aufgabe abgedeckt ist und keine zwei Aufgaben im selben Pool und Lernziel dieselbe Sollantwort haben. Ausgabe: „0 Abweichungen“.
- `sonderfaelle.md`: zu jeder Aufgabe ein Satz zum geprüften Sonderfall.

## Lehrplan und Zweifel

1. **Umkehrung des Satzes des Thales und Lage Gerade/Kreis (VT2-064 bis 077):** Laut `inhalte/themen/geometrie.kreis.json` (Merke und Abschnitte „Satz des Thales“, „Tangenten“) und Themenliste (Lernbereich M7 5, Zeile „Satz des Thales und seine Umkehrung beweisen und anwenden“) gehören beide Teile zur Einheit. Der Vorprüfer hat den Originaltext des Lehrplans nicht abrufen können und ist nur zu etwa 75 % sicher; ich habe ihn ebenfalls nicht abgerufen. Passante/Tangente/Sekante stehen in der Merke der Einheit, im Gymnasium-Zitat der Themenliste aber nur „Tangente von einem äußeren Punkt konstruieren“. **Offen, die Gegenprüfung entscheidet.** Die Aufgaben benutzen weder Pythagoras noch Wurzeln.
2. **Sammel-Optionen:** „Beide gleich …“ ist in 4 von 5 Aufgaben falsch (019, 086, 096, 129; richtig in 115 „Beide sind richtig gerundet“). Nicht ganz ausgeglichen.
3. **Auswahlzahl:** 47 von 133 (35 %). Wo eine Zahl- oder Lückenaufgabe dieselbe Einsicht prüft, wurde sie bevorzugt. Die App mischt die Optionen im Test nach Auskunft des Koordinators nicht; die Positionen sind deshalb im Bauskript fest gesetzt, nicht erst beim Anzeigen.
4. **Handvergleich mit dem Bestand:** Ich habe jede Aufgabe gegen die Texte der Vorprüfung (Abschnitt „Doppelungen“) umgebaut und danach die Treffer der Tool-Prüfung (V15) ausgewertet. Einen vollständigen Zeile-für-Zeile-Vergleich mit allen `rollend-*`-Ordnern habe ich nicht gemacht; das Werkzeug findet nur gleiche Wörter und Zahlen. Weitere Doppelungen sind möglich.
5. **Schema-nahe Aufgaben:** höchstens zwei je Lernziel nach meiner Einschätzung; die Einschätzung ist nicht unabhängig. Zu prüfen: VT2-006, 029/032, 046/048/049, 053, 060, 087/090, 093, 099/103, 118, 123/126.
6. **Gleiche Lückenwerte:** VT2-013 und VT2-023 haben absichtlich zwei gleiche Lückenwerte (36/36 und 50/50), weil genau das die Einsicht ist; das Prüfwerkzeug nimmt es an.
7. **Zahlen ohne Zinseszins:** Alle Zinsaufgaben bleiben innerhalb eines Jahres (VT2-025 jetzt 3, 8, 9 Monate).
8. **Eigene Zahlen und Texte:** nichts aus Schulbüchern oder Prüfungen. Namen sind neutral (Mia, Ben, Jonas, Frau Berger, Familie Koch).

## Was die Gegenprüfer ansehen sollten

- Die Aufgaben der geometrie.kreis (VT2-064 bis 084): Lehrplan, Fehlbild-Texte, Lage der Punkte in 068.
- Die ersetzten Test-Aufgaben: VT2-001, 022, 050, 071, 078, 085, 092, 113, 120, 127 (Schwierigkeit, Eindeutigkeit).
- Die neuen Lücken-Aufgaben mit Zeilenfehlern (VT2-081, 120) und die Aufgaben mit zwei gleichen Lückenwerten (013, 023).
- Doppelungen mit `rollend-*` und `themen`, die das Werkzeug nicht erkennt.
