# Runde 12 (R5): Reserve Klasse 5

Zwei zählende Aufgaben je Lernkarte (eine auf Stufe 2, eine auf Stufe 3) in Formen, die in den bisherigen Runden fehlen oder selten sind.
Kürzel R5, Kennungen R5-V001 bis R5-V210. Aufgaben stehen in `<thema>.json`, erzeugt aus `th_<thema>.py` durch `bauen.py`.

| Thema | Lernkarten | Aufgaben | Formen zw/um/br/an/fd | zaehlt |
|---|---|---|---|---|
| zahlen.natuerlich | 13 | 26 | 7/5/4/4/6 | ja 26 |
| zahlen.rechengesetze | 14 | 28 | 9/6/2/5/6 | ja 28 |
| zahlen.ganz | 11 | 22 | 5/3/5/3/6 | ja 22 |
| zahlen.potenzen_basis | 7 | 14 | 4/3/2/2/3 | ja 14 |
| zahlen.teilbarkeit | 7 | 14 | 5/2/2/5/0 | ja 14 |
| geometrie.grundbegriffe | 7 | 14 | 2/3/4/5/0 | ja 14 |
| geometrie.winkel | 7 | 14 | 6/2/2/4/0 | ja 14 |
| messen.flaechen | 7 | 14 | 4/3/2/4/1 | ja 14 |
| messen.koerper_darstellung | 6 | 12 | 2/2/3/2/3 | ja 12 |
| daten.darstellen | 6 | 12 | 2/4/2/4/0 | ja 12 |
| stochastik.kombinatorik | 7 | 14 | 5/3/2/4/0 | ja 14 |
| groessen.einheiten | 8 | 16 | 5/4/3/4/0 | ja 16 |
| groessen.proportional | 5 | 10 | 2/2/3/3/0 | ja 10 |
| Summe | 105 | 210 | 58/42/36/49/25 | ja 210 |

Genaue Formverteilung je Thema: `python3 -I inhalte/mathe-profi/rollend-12/bauen.py` (Tabelle am Ende der Ausgabe).
Stufen: 105 Aufgaben auf Stufe 2, 105 auf Stufe 3.

## Wie geprüft
- `bauen.py`: je Lernkarte genau 2 Aufgaben, Stufen 2 und 3, zwei verschiedene Formen, kein Lückenweg, höchstens ein Fehler-Detektiv, je Thema jede der Formen Umkehren, Zwei Wege, Brücke, Anwenden mindestens zweimal.
- Alle Lösungen zweifach nachgerechnet, 576 Fehlbilder (466 mit nachgerechneter Rechnung), Dopplungen gegen den Bestand und andere Runden geprüft.
- `tools/inhalt_pruefen.py` (Code 0) und `tools/vorrat_pruefen.py` ohne Meldungen (i) bis (iii).
- `python3 -I tools/rollend_sql.py --runden 12` läuft ohne Fehler (210 Aufgaben, 13 Einheiten).
- Zum Schluss streng durchgesehen (Checkliste B).

## Offen und Annahmen (nicht abgesichert)
- Meldungen (iv): R5-V030, R5-V064, R5-V148, R5-V154. Die Fehlerzeile enthält nur richtige Rechnungen, der Fehler ist eine falsche Behauptung (Denkfehler); von Hand geprüft.
- Einige Fehlbild-Proben sind nur `lambda: True`, wenn der Fehler keine Rechnung ist.
- Zeichnungen nur als Tabelle oder Säulen (20 Aufgaben).
- Keine Lernkarte zurückgestellt, bei jeder passte mindestens eine der gesuchten Formen.
