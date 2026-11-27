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
- 286 Fehlbilder mit Rechnung nachgerechnet; 23 davon tragen eine Fehlbild-Kennung aus dem Katalog.
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

## Vorprüfung (unabhängig, alle 132 Aufgaben einzeln gelesen und nachgerechnet)
96 Aufgaben geändert (Quelle und Neubau). Befunde nach Art, Zahlen gerundet auf die Aufgaben, die davon betroffen waren:
- Regel-Kennung passte nicht zum Thema oder zur Aufgabe: etwa 60, auf die passende Kennung gesetzt oder geleert.
- Fehlbild-Kennung passte nicht genau zur Rechnung: 23 geprüft, mehrere geleert, Texte angepasst (Vorzeichen, Richtung).
- Fehler-Detektiv: Rückmeldung für jede wählbare Zeile ergänzt (Parameter `rueck` in `kern.py`), Fragetexte eindeutig gemacht.
- Aufgabe fachlich neu gebaut, weil sie die Lernkarte nicht übte oder nicht eindeutig war: V017, V036, V047, V060, V071, V080, V084, V103, V121.
- Fragetext: Eingabefrage steht zuletzt, fehlende Vorbedingung ergänzt, Schreibweise (Klammern, Einheiten, Dezimalkomma).
- Tipp zu stark oder Stufe 3 kaum schwerer als Stufe 2: etwa 12 Tipps entschärft.
- `bauen.py` prüft jetzt: Regel-Kennung und Fehlbild-Kennung stehen im Katalog `regeln-uebersicht/kennungen.json` und gehören zum Thema
  (Ausnahmen nur über die Listen `REGEL_AUSNAHME` und `FEHLBILD_GELESEN`, von Hand gelesen).
Nicht verlässlich beurteilt:
- Zeichnungen V071, V080, V103, V121 (neu oder geändert) nicht im Browser angesehen.
- V123, V124, V017, V047 passen nur teilweise zum Titel der Lernkarte; V054 nur teilweise zur Scheinlösung.
- V107 ist eher Stufe 3, steht auf Stufe 2; V058 und V112 auf Stufe 3 bleiben recht einfach.
- V007 (zwei Wege unterscheiden sich nur in der Zerlegung), V039 und V045 (schwache Brücke), V068 (Fehlbild grenzwertig).

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
