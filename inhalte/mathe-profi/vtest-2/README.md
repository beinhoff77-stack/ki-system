# Verstehen in Tests, Stufe 1, Runde 2 (VT2-001 bis VT2-133)

Nicht eingespielt. 19 Lernziele je 7 Aufgaben: 1 Test (`ersetzt_test: true`), 3 Korrektur, 3 Sicherung. Die Auswahl und ihre Gründe stehen in `auswahl.md`.

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

## Verteilung

- Pool: test 19, korrektur 57, sicherung 57.
- Stufe: 2 (76 Aufgaben), 3 (57 Aufgaben). Alle 19 Tests sind Stufe 3.
- Antwortform: auswahl 62, luecken 40, zahl 31. Richtige Möglichkeit bei den 62 Auswahlaufgaben: Platz A 17, B 16, C 12, D 17.
- Typ: begruenden 37, fehler 20, darstellung 15, parameter 15, umkehr 15, transfer 13, pruefung 9, rueckwaerts 8, mehrschritt 1.
- Form: ohne 86, fehler_detektiv 20, anwenden 10, umkehren 6, zwei_wege 5, bruecke 4, verfahren_waehlen 2.

## Gedanke je Aufgabe

Jede Aufgabe trägt das Feld `idee` mit der Denkfigur (Liste in `ideen.py`). Je Lernziel gibt es sieben verschiedene, nie mehr als zwei gleiche. Umkehr- und Rückwärtsaufgaben zählen als eine Idee, Fehler-Detektiv ist je Lernziel höchstens zweimal vorhanden. Keine Aufgabe hat im selben Pool und Lernziel dieselbe Sollantwort wie eine andere (per Skript geprüft).

## Prüfung

- `python3 -I tools/vtest_pruefen.py --runde 2`: keine Fehler, drei Hinweise (VT2-106, VT2-112, VT2-118, siehe Zweifel).
- `python3 -I inhalte/mathe-profi/vtest-2/gegenrechnung.py`: rechnet alle 133 Sollwerte auf einem anderen Weg nach (Bruchrechnung, Aufzählen, Einsetzen, Zeichenketten) und gibt „0 Abweichungen“ aus.
- `sonderfaelle.md`: zu jeder Aufgabe ein Satz zum geprüften Sonderfall.
- Neu bauen: `python3 -I inhalte/mathe-profi/vtest-2/bauen.py` (Module `th_*.py`, Helfer `kern.py`).

## Zweifel

1. **Hinweise „runden fehlt“** bei VT2-106, VT2-112, VT2-118: Der Text enthält das Wort Runden, aber die Lösung ist eine ganze Zahl. Ein Feld `runden` wäre falsch, deshalb bewusst weggelassen.
2. **Umkehrung des Satzes des Thales** (VT2-064 bis 070): Es wird ohne Pythagoras und ohne Wurzeln gearbeitet. Koordinatenaufgaben (VT2-065, 068) nutzen nur Abstände zum Mittelpunkt, die als Kreisradius ablesbar sind. Ob der Lehrplan der Klasse 7 die Umkehrung schon so ausdrücklich verlangt, sollte die Fachseite prüfen.
3. **Länge der richtigen Möglichkeit**: Bei den Begründungsaufgaben ist die richtige Option oft etwas ausführlicher. Das wurde an etwa 14 Aufgaben abgemildert, ist aber nicht überall behoben.
4. **Einfache Verzinsung über ein Jahr** (VT2-025, 18 Monate): Zinseszins kommt nicht vor, der Text sagt es nicht ausdrücklich.
5. **Milliarden** werden nicht benutzt (Zahlen bis zu den Millionen); das genügt für Stellenwert und Zahlwort.
6. **Einige Aufgaben bleiben nahe am Schema** (zusammenfassen S3, ausklammern K1, binomisch S1); sie sind durch Kontext und Gegenfrage verändert, aber weniger tief als die übrigen.
7. **Eigene Zahlen und Texte**: nichts aus Schulbüchern oder Prüfungen. Namen sind neutral (Mia, Ben, Jonas, Frau Berger, Familie Koch).

## Was die Vorprüfer ansehen sollten

- Geometrie: Fehlbild-Beschreibungen in VT2-064 bis 070 und die Lage der Punkte in VT2-068.
- Die vier Aufgaben mit Zeilen-Fehlersuche, in denen die Fehlerzeile nicht die letzte ist (z. B. VT2-097, VT2-130).
- Doppelte oder sehr ähnliche Sachkontexte zu den `rollend-*`-Ordnern (nur die Tool-Prüfung auf Ähnlichkeit wurde gemacht, kein Handvergleich aller Texte).
