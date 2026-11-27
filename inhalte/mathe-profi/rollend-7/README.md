# rollend-7 – neue Aufgabenformen, Klasse 8 (Kennung K8-V001 …)

Ein JSON je Thema, erzeugt mit `python3 -I bauen.py` (Hilfen in `kern.py`, Aufgaben in `th_*.py`).

| Thema | Lernkarten | Aufgaben | lw/fd/vw/zw/um/br/an | zaehlt ja/nein |
|---|---|---|---|---|
| terme.umformen | 5 | 15 | 5/2/0/2/2/2/2 | 10/5 |
| terme.umformen_teil2 | 4 | 12 | 3/1/0/2/2/2/2 | 9/3 |
| gleichungen.linear | 6 | 18 | 6/2/0/2/3/3/2 | 12/6 |
| terme.bruchterme | 7 | 21 | 6/3/3/3/2/2/2 | 15/6 |
| gleichungen.bruch | 7 | 21 | 7/2/1/3/3/3/2 | 14/7 |
| terme.quadratische_extreme | 5 | 15 | 5/2/0/2/2/2/2 | 10/5 |
| terme.potenzgesetze_natuerlich | 5 | 15 | 4/2/1/2/2/2/2 | 11/4 |
| terme.potenzgesetze_ganzzahlig | 5 | 15 | 3/2/2/2/2/2/2 | 12/3 |
| stochastik.grundbegriffe | 3 | 9 | 1/0/0/2/2/2/2 | 8/1 |
| messen.prisma_zylinder | 7 | 21 | 6/2/1/3/2/3/4 | 15/6 |
| groessen.indirekt | 7 | 21 | 4/2/2/3/3/3/4 | 17/4 |
| Summe | 61 | 183 | 50/20/10/26/25/26/26 | 133/50 |

Formen: lw Lückenweg, fd Fehler-Detektiv, vw Verfahren wählen, zw Zwei Wege, um Umkehren, br Brücke, an Anwenden.

## Abweichung vom Auftrag
Der Auftrag nennt 65 Lernkarten / 195 Aufgaben. Die aufgelisteten Lernkarten ergeben 61 (183 Aufgaben). Alle aufgelisteten Lernkarten sind abgedeckt, je drei Aufgaben.

## Wie geprüft
- `bauen.py` rechnet jede Lösung zweifach nach (`c` und unabhängige Zweitrechnung), bei auswahl genau eine richtige Antwort, Termgleichheit mit exakten Brüchen an mehreren Stellen.
- Fehlbilder (464) werden neu berechnet, nicht von Hand übernommen (soweit sie eine Rechnung nennen: 300 maschinell nachgerechnet).
- Mischung je Lernkarte: höchstens 1 Lückenweg (zaehlt nein), höchstens 1 Fehler-Detektiv, mindestens 1 zaehlt-ja-Aufgabe aus umkehren/zwei_wege/bruecke/verfahren_waehlen/anwenden. Je Thema umkehren, zwei_wege, bruecke, anwenden mindestens zweimal.
- Lückenweg: Antwortform luecken, mindestens zwei Lücken, verschiedene Werte, kein Lückenwert in Text, Schablone oder Hinweis.
- Fehler-Detektiv: genau ein unabhängiger Fehler, so viele Antworten wie Zeilen. Fehlerzeile: Zeile 1: 5, Zeile 2: 5, Zeile 3: 6, Zeile 4: 4 (von 20).
- `tools/inhalt_pruefen.py` (mit `-I`) läuft in `bauen.py` auf Kopien der Stoff-Themendateien mit den neuen Aufgaben; alle Themen Code 0.
- Antworttypen nur zahl, auswahl, luecken. Zeichnungen nur tabelle und koordinaten (19 Aufgaben).

## Gesichert und offen
- Gesichert: Rechnung, Eindeutigkeit der Lösung, Formregeln oben.
- Nicht gesichert: Anzeige in der App nicht getestet, keine Probe mit Kindern, Schwierigkeit (Stufe) nur aus dem Aufgabentyp abgeleitet.
- Annahmen stehen in den Aufgabentexten (zum Beispiel „indirekt proportional“, Definitionsmenge, Rundung).
- Lernkarten, bei denen eine Form nicht passte: keine zurückgestellt. Einzelne Formen fehlen bewusst, wo sie fachlich nicht passen (zum Beispiel kein Fehler-Detektiv in stochastik.grundbegriffe).

## Nach Gegenprüfung (Werkstatt 1043)

Eine unabhängige Gegenprüfung hat Aufgaben gefunden, bei denen Frage, Antworten, Tipp, Lösungsweg und Fehlbilder nicht zusammenpassten. Alles wurde neu gerechnet und korrigiert.

- Geändert: 106 Aufgaben inhaltlich (Text, Zahlen, Antworten, Tipp, Lösungsweg, Fehlbilder), weitere 11 nur im Lückenweg (echte Abhängigkeit). Bei 7 Verfahren-wählen-Aufgaben wurde `g` nach tatsächlicher Tätigkeit auf `erkennen` gesetzt; die Kennungen bleiben stabil (`rang` in `neu()`).
- Arten der Änderung: Zahlen und Fehlbilder neu berechnet; Grundmenge und Annahmen ausdrücklich genannt (für alle x, a ≠ 0, gerades Prisma, gleich leistungsfähige Arbeiter, gleichmäßiges Tempo); Lückenwege so umgebaut, dass spätere Lücken wirklich von früheren abhängen und der Text keine Lücke verrät; Toleranzen nur, wo es technisch nötig ist; Auswahlantworten mit Doppelungen oder mehreren richtigen Antworten ersetzt.
- Zusätzlich selbst gefunden (nicht aus der Gegenprüfung): 56 weitere Aufgaben, vor allem unabhängige oder erratbare Lückenwege, fehlende Annahmen, falsch beschriebene Fehlbilder und doppelte Antwortwerte.
- Neu in `bauen.py`: Fehlbilder haben eine vierte Angabe (Rechnung) und werden nachgerechnet; Lückenwege werden mit eingesetzten Vorgängerwerten gerechnet und auf Abhängigkeit geprüft (Änderung einer früheren Lücke ändert das Ergebnis); gleiche Lückenwerte sind nur mit `gleich_ok` erlaubt.
- Nicht maschinell prüfbar: 5 Fehlbilder ohne Rechnung (Wert oder Auswahl). Darstellung in der App wurde nicht getestet.

### Nachprüfung (Werkstatt 1056)

- Nachgebessert: Fehlbild und Rechenweg bei einer Bruchgleichung mit zwei Wegen (die Fehlantwort folgt jetzt wirklich aus dem beschriebenen Fehler); Wertetabellen-Aufgabe so geführt, dass beide Tabellenwerte gebraucht werden; Sonderfall-Lückenweg mit Prüfrechnung für Widerspruch (0 Lösungen) und Identität (unendlich viele, als Merkwert 99 markiert); „über ℚ“ bei einer Definitionsmenge ergänzt; Zylinder-Fehlbild ausdrücklich auf den Weg mit π ≈ 3,14 bezogen; zwei Fehlbild-Beschreibungen berichtigt, die einen richtigen Wert als falsch bezeichneten; Minimalwert und tiefster Punkt getrennt benannt.
- Alle 464 Fehlbild-Beschreibungen wurden noch einmal gegen ihre Antwort gelesen (auch die ohne Rechnung): beschriebener Fehler muss zur gespeicherten Antwort führen, und nichts Richtiges darf als falsch bezeichnet sein.
