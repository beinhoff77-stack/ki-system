# rollend-10 – neue Aufgabenformen, Klasse 9 (Teil b), Kennung K9B-V001 … V108

Ein JSON je Thema, erzeugt mit `python3 -I inhalte/mathe-profi/rollend-10/bauen.py` (Hilfen `kern.py`, Aufgaben in `th_*.py`). Nichts eingespielt.

| Thema | Lernkarten | Aufgaben | lw/fd/vw/zw/um/br/an | zaehlt ja/nein | Stufe 1/2/3 |
|---|---|---|---|---|---|
| trigo.pythagoras | 6 | 18 | 6/2/0/2/2/2/4 | 12/6 | 6/6/6 |
| abbildungen.aehnlichkeit | 9 | 27 | 9/6/0/2/4/2/4 | 18/9 | 9/9/9 |
| trigo.rechtwinklig | 7 | 21 | 6/4/0/3/2/3/3 | 15/6 | 6/8/7 |
| messen.kreisberechnung | 6 | 18 | 6/2/0/2/3/3/2 | 12/6 | 6/6/6 |
| raum.pyramide_kegel_kugel | 7 | 21 | 7/3/0/2/4/2/3 | 14/7 | 7/7/7 |
| messen.prisma_zylinder_teil2 | 1 | 3 | 1/0/0/0/1/0/1 | 2/1 | 1/1/1 |
| Summe | 36 | 108 | 35/17/0/11/16/12/17 | 73/35 | 35/37/36 |

Formen: lw Lückenweg, fd Fehler-Detektiv, vw Verfahren wählen, zw Zwei Wege, um Umkehren, br Brücke, an Anwenden. Antwortformen: Zahl 45, Lücken 35, Auswahl 28. Keine Zeichnungen außer Tabellen (10 Aufgaben).

## Wie geprüft (maschinell, in `bauen.py`)
- Jede Zahlenlösung zweifach (Anker `c` und unabhängige Zweitrechnung mit Gleitkomma, Winkel in Grad). Gerundete Ergebnisse tragen die Rundung im Text; `rd()` bricht ab, wenn der Wert zu nah an einer Rundungsgrenze liegt. Keine Toleranzen.
- 293 Fehlbilder, alle mit Rechnung (Feld `c`), neu gerechnet; die Rechnung muss genau die gespeicherte Fehlantwort ergeben.
- Lückenwege: Antwortform Lücken, 2 bis 6 Lücken, spätere Lücke braucht den Wert einer früheren (Änderungsprobe), letzte Lücke abhängig, kein Lückenwert als Ziffer oder Zahlwort in Text, Schablone, Hinweis oder Tipp (auch `cm³`/`cm²` zählen als Zahl im Text). Gespeicherte Anker enthalten die früheren Anker verschachtelt.
- Fehler-Detektiv: je Zeile Angabe „stimmt“ und „folgt aus der Zeile davor“; Zeilen vor dem Fehler stimmen, Folgezeilen folgen richtig. Fehlerzeile Zeile 1 / 2 / 3: 6 / 5 / 6 (von 17).
- Auswahl: genau eine richtige, keine gleichen Antworten, Lage der richtigen Antwort verteilt.
- Je Lernkarte genau 3 Aufgaben; höchstens 1 Lückenweg (zaehlt nein, Stufe 1) und 1 Fehler-Detektiv; mindestens je eine zählende Aufgabe auf Stufe 2 und 3 (neue Vorgabe). `t` je Lernkarte aus dem Bestand übernommen.
- `tools/inhalt_pruefen.py` auf Kopien der Themen-Dateien mit den neuen Aufgaben: Code 0 bei allen. `tools/vorrat_pruefen.py` über den Ordner: (i) (ii) (iii) ohne Meldung.

## Gesichert und offen
- Gesichert: Rechnungen, Eindeutigkeit der Zahlenlösungen, Formregeln. Nicht gesichert: Anzeige in der App, Probe mit Kindern, Stufe nur aus `g` (Lückenweg direkt, Zwei Wege/Brücke/Anwenden einfach: Stufe 2, Umkehren rückwärts und Fehler-Detektiv: Stufe 3; „Anwenden“ mit `transfer` an drei Stellen, Umkehren mit `umkehr` an zwei Stellen: Stufe 2).
- Meldung (iv) von `vorrat_pruefen.py` (3, bewusst): K9B-V009, V030, V090 sind Denkfehler (richtig gerechnet, falsche Regel oder falscher Schluss: Quadrat als „· 2“, Streckfaktor addiert statt multipliziert, eine statt vier Seitenflächen).
- Fehlbild-Beschreibungen bei Auswahl (Antworttext) sind nicht rechnerisch; sie wurden von Hand gegen die Antwort gelesen (V008, V044, V050, V074, V077, V083, V089, V099 u. a. über die Probe-Funktion in `th_*.py`).
- Abweichungen vom Auftrag:
  - `trigo.rechtwinklig`, Lernkarte `seiten`: kein Lückenweg (Zuordnung von Gegen-/Ankathete lässt sich nicht als Zahlenlücke ohne Abschreiben bauen); Ersatz: Brücke, Anwenden, Fehler-Detektiv. Dadurch 35 statt 36 Lückenwege.
  - `messen.prisma_zylinder_teil2`: eine Lernkarte, daher kommen Umkehren, Brücke, Zwei Wege nicht je zweimal vor (Zwei Wege und Brücke fehlen, die Formen passen zu „schief“ fachlich nicht gut).
  - Verfahren wählen kommt nicht vor (Entwürfe waren nur „erkennen“, Stufe 1; durch die Stufenvorgabe ersetzt).
- Annahmen in den Texten: π ≈ 3,14 oder π ≈ 3 oder exakt in π, Gradmaß (DEG) am Taschenrechner, Rundung stets genannt, Figuren ausdrücklich (gerade Pyramide, Kegel, Prisma schief, Dach symmetrisch).

## Vorprüfung durch zweiten Helfer
Alle 108 Aufgaben vollständig gelesen (Frage, Antworten, Schablone, Tipp, Lösungsweg, Fehlbilder) und von Hand nachgerechnet. 16 Aufgaben geändert, Kennungen unverändert.
- Lösung falsch / mehrdeutig: 0 gefunden. Alle Zahlen- und Lückenlösungen stimmen, jede Auswahl hat genau eine richtige Antwort.
- Tabelle und Text widersprachen sich: V104 (Tabelle mit genauem π gerechnet, Text sagte π ≈ 3,14). Text berichtigt, Prüffunktion rechnet die Tabelle jetzt nach.
- Fehlbild passte nicht zur Antwort oder war unklar: V079 (Antwort 24 war kein Quadrat, jetzt 576 mit Durchmesser), V023 (Antwort 6 ohne sinnvollen Fehler, jetzt 21), V074 (Beschreibung), V029 (Beschreibung „kürzeste“ statt „beiden kürzeren“ Seiten).
- Form hielt nicht, was sie versprach: V071 (Zwei Wege war dieselbe Rechnung mit Zwischenschritt, jetzt Formel gegen Flächenfaktor), V079 (Text „der 4-te Teil“, jetzt „1/① des Kreises“).
- Sprache und Eindeutigkeit: V049 („zweites“ neben Lücke 2), V100 („Volumen der Waffel“ statt des Kegels), V018 („Decke“ statt Oberkanten der Außenwände), V057 (Zeile 3 ohne Einheit, jetzt 0,64°).
- Tipp verriet die Antwort: V024, V042 (Tipp nannte die geltende Regel bzw. welche Zeilen stimmen), jetzt neutral.
- Stufe 3 zu leicht (Einschritt-Aufgaben): V003 (Fernseher: jetzt Seitenverhältnis 16 : 9, Diagonale in Zoll, Breite gesucht), V063 (Mast mit Augenhöhe, zwei Schritte), V066 (Gerade durch Q(1 | 2), zwei Schritte), V108 (Breite aus Volumen, Höhe und Länge, zwei Schritte).
- Fehler-Detektive V009, V030, V090: bewertete Zeile spricht die falsche Behauptung ausdrücklich aus („Quadrat ist 12 · 2“, „mittlere Seite 6 + 3 = 9“, „Oberfläche = Grundfläche plus ein Seitendreieck“). Restmeldungen (iv) bleiben, sind damit begründet. Auch V006, V021, V024, V033, V036, V042, V048, V051, V057, V060, V072, V078, V096, V105 lesen: Fehlerzeile spricht die Behauptung aus, Folgezeilen folgen richtig.
- Fehlbild-Texte der Auswahl-Aufgaben (V008, V044, V050, V074, V077, V083, V089, V099 u. a.) von Hand gegen die Antwort gelesen.
- Offen / fraglich (nicht geändert): Stufe 3 bleibt eher mittelschwer bei V027, V039, V054, V069, V075, V081, V084, V087, V093 (ein bis zwei Schritte, Klasse 9 gewohnt). V023 Weg B ist dasselbe Streckungsverfahren an anderen Punkten (Verfahren, nicht Rechnung, verschieden). V095 Weg B (Abwicklung) gibt rechnerisch π · r · s. V050 falsche Antwort „Dreieck 1 und 3“: der Grund gilt auch für Dreieck 2, die Antwort bleibt falsch.
- Skript: V104 prüft jetzt die Tabellenwerte gegen π; weitere Funde waren Wortlaut, den `vorrat_pruefen.py` und `bauen.py` nicht erkennen können.
