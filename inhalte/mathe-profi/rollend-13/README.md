# rollend-13 – Reserve (Klasse 8, Kennung R8-V001 bis R8-V132)

Je Lernkarte zwei zählende Aufgaben (zaehlt = ja): eine auf Stufe 2, eine auf Stufe 3.
Gewählt sind Formen, die es für diese Lernkarte in den Runden 1 bis 12 noch nicht gibt.
Kein Lückenweg, kein Gerüst. Es sind 12 Themen mit 66 Lernkarten und 132 Aufgaben
(nicht „rund 80 Lernkarten / 160 Aufgaben“).

| Thema | Lernkarten | Aufgaben | Formen (fd/zw/um/br/an/vw) | zaehlt |
|---|---|---|---|---|
| terme.umformen | 5 | 10 | 3/1/2/1/3/0 | 10 ja |
| terme.umformen_teil2 | 4 | 8 | 2/2/1/2/1/0 | 8 ja |
| gleichungen.linear | 6 | 12 | 2/3/3/2/2/0 | 12 ja |
| terme.bruchterme | 7 | 14 | 2/2/5/3/2/0 | 14 ja |
| gleichungen.bruch | 7 | 14 | 3/2/2/3/4/0 | 14 ja |
| funktionen.grundbegriffe | 9 | 18 | 0/5/3/3/7/0 | 18 ja |
| funktionen.linear | 11 | 22 | 0/5/5/5/7/0 | 22 ja |
| terme.quadratische_extreme | 5 | 10 | 1/2/3/1/3/0 | 10 ja |
| stochastik.grundbegriffe | 3 | 6 | 1/1/1/1/1/1 | 6 ja |
| abbildungen.kongruenz_teil3 | 3 | 6 | 0/2/1/2/1/0 | 6 ja |
| geometrie.konstruktion_teil2 | 2 | 4 | 0/1/1/1/1/0 | 4 ja |
| raum.schraegbilder_teil2 | 4 | 8 | 2/1/2/2/1/0 | 8 ja |
| Summe | 66 | 132 | 16/27/29/26/33/1 | 132 ja, 0 nein |

(fd = fehler_detektiv, zw = zwei_wege, um = umkehren, br = bruecke, an = anwenden, vw = verfahren_waehlen)
Stufen: 66 Aufgaben auf Stufe 2, 66 auf Stufe 3. Die Stufe folgt aus der Zahl g (Tätigkeit) der Aufgabe.

## Geprüft (maschinell, `python3 -I inhalte/mathe-profi/rollend-13/bauen.py`, Ergebnis „OK“)
- Alle 132 Lösungen zweimal unabhängig nachgerechnet (Ausdruck c und zweite Rechnung).
- 281 Fehlbilder mit Rechnung nachgerechnet, keines ohne Rechnung.
- Auswahl-Aufgaben: genau eine richtige Antwort, Probe per Programm; Lage der richtigen Antwort wechselt.
- Fehler-Detektiv: Zeilen vor der Fehlerzeile stimmen, spätere Zeilen folgen aus der Zeile davor.
  Fehlerzeile je Zeile {1: 5, 2: 5, 3: 4, 4: 2} bei 16 Aufgaben, keine Zeile über einem Drittel plus eins.
- Kein Fragetext und keine Grundform kommt im Bestand oder in einer anderen Runde vor.
- `tools/vorrat_pruefen.py`: 0 Meldungen in allen vier Gruppen.
- `python3 -I tools/rollend_sql.py --runden 13` läuft ohne Fehler (Werkzeug und rollend-einheiten.json unverändert).

## Schlussdurchsicht (Checkliste B, alle 132 Aufgaben von Hand gelesen)
8 Aufgaben geändert: V025 (zwei_wege war unehrlich: Weg A konnte die Lösung nicht liefern, jetzt Frage nach dem Unterschied der Seiten),
V026 (Probe-Gleichung eindeutig benannt), V042 und V110 und V111 (Wortlaut), V049 (Weg B ist jetzt wirklich ein anderer Weg:
Wertetabelle statt gleicher Gleichung), V050 (Läufer und Läuferin vereinheitlicht), V085 (Bezeichnung t doppelt benutzt).

## Annahmen und offene Punkte (nicht als geprüfte Tatsachen zu lesen)
- Die Aufgabe „Fliesenleger/Raute“ (V124) kommt ohne Satz des Pythagoras aus, weil dieser in der Konstruktions-Lernkarte im Bestand nicht vorkommt.
- Fehler-Detektiv-Zeilen mit Aussagen in Worten (zum Beispiel V104, V114, V128, V132) sind im Skript nur über eine kleine Gegenrechnung
  (Zähltest, Zahlenvergleich) oder als feste Aussage abgesichert. Der fachliche Beweis der Aussage steht nur im Lösungsweg.
- Fehlbilder der Auswahl-Aufgaben prüft das Skript nur, soweit die Probe-Funktion der Aufgabe sie berechnet. Die Beschreibungen
  der falschen Antworten wurden von Hand gegen die Rechnung gelesen.
- Zeichnungen (Tabelle, Koordinaten, Figur) sind nur auf die Form geprüft, nicht im Browser angesehen.
- verfahren_waehlen kommt nur einmal vor (V111). In den anderen Lernkarten gab es die Form schon, oder es fand sich keine ehrliche Aufgabe
  dazu. Zurückgestellt wurde keine Lernkarte.
- Namen wie Kim, Tom, Ali, Zoe, Mia sind erfundene Allerweltsnamen wie im Bestand. Keine Namen von Kindern oder Familie.
