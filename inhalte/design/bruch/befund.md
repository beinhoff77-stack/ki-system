# Bruch-Darstellung in Aufgaben – Sichtprüfung

Designer, 27.11.2026. Geprüft: `lernen-app` 7c76b324 (im Stand 2455724), App **unverändert**, Chrome, Kinderansicht „Üben“, 360 und 400 px, hell und dunkel.
Aufgabentexte **echt** aus `inhalte/themen/`; **nachgestellt** sind die Antworten des Servers (eine Etappe mit genau dieser Aufgabe, Antwort „richtig“). Die Stellenkästchen T/H/Z/E und die Kopfzeile „Rom · Natürliche Zahlen“ kommen aus dieser Nachstellung und gehören nicht zum Befund.
Bilder: `<fall>-<breite>-<hell|dunkel>.png`, Messwerte: `messung.json`, Aufnahme: `aufnehmen.cjs` (liest nur, ändert nichts).

| Fall | Aufgabe | Bild zeigt |
|---|---|---|
| a | `bruch.brueche` Nr. 13: „… 3/4 der Kinder fahren mit dem Bus …“ | Frage |
| b | `bruch.brueche` Nr. 149: „Welcher ist der größte Bruch: 3/4, 1/2, 5/6, 4/7?“ | Frage und vier Antwortknöpfe |
| c | `terme.bruchterme` Nr. 240: Lösungsweg mit „3(x − 2)/(x + 1) · 2(x + 1)/(x − 2)“ | Frage und Lösungsweg |
| c2 | `gleichungen.bruch` Nr. 202: Lösungsweg „(x + 6)/(x − 2) = 3 ⇒ …“ | Lösungsweg |
| d | `bruch.prozent` Nr. 175: „Wie viel Prozent sind 1 1/4?“ | Frage |

Einen Lösungsweg, in dem genau „(x + 1)/(x − 2)“ als eigener Bruch steht, gibt es in den Aufgaben nicht. Fall c ist die einzige Aufgabe mit dieser Zeichenfolge; c2 ist der nächste echte Lösungsweg mit einem Bruch dieser Bauart.

## Gesichert (gemessen)

| Stelle | Text | Ziffern im Bruch | Höhe Bruch | Zeilenhöhe ohne Bruch |
|---|---|---|---|---|
| Frage | 22 px | 18 px | 40 px | 27,5 px |
| Antwortknopf | 14 px | **11,5 px** | 26 px | 21,7 px |
| Lösungsweg | 16 px | 13,1 px | 30 px | 22,4 px |

- Kein Querrollen, kein Bruch ragt aus seinem Kasten, kein Umbruch **innerhalb** eines gestapelten Bruchs – in allen 20 Bildern.
- Hell und dunkel: Bruchstrich und Ziffern in Textfarbe, in beiden lesbar.
- Antwortknopf mit Bruch ist 56 px hoch.

## Was schief aussieht

1. **Bruch in Antwortknöpfen zu klein (Fall b).** Ziffern 11,5 px, unter der 13-px-Grenze der Vorgaben. Der Bruch klebt klein links oben neben dem Kreis; der Knopf ist fast leer. Das ist der deutlichste Mangel.
2. **Lösungsweg mit Vorfaktor wird nicht gestapelt (Fall c).** „3(x − 2)/(x + 1) · 2(x + 1)/(x − 2)“ bleibt Text mit Schrägstrich und bricht mitten im Nenner um („/(x“ ⏎ „− 2)“). In derselben Karte ist die Frage gestapelt, der Weg nicht. Ursache laut Kommentar im Code gewollt („Zähler nicht eindeutig“). Betrifft in den Aufgaben 24 Texte dieser Bauart, alle in `terme.bruchterme` und Nachbarn.
3. **Zeilen werden ungleich hoch (Fälle a, c).** Eine Zeile mit Bruch braucht 40 px, eine ohne 27,5 px. Bei drei, vier Zeilen wirkt der Absatz unruhig; bei a (400 px) steht der Bruch allein am Zeilenende und hebt nur die erste Zeile an.
4. **Zwei Brüche mit Rechenzeichen werden getrennt (Fall c, 360 px).** „… von (3x − 6)/(x + 1) :“ ⏎ „(x − 2)/(2x + 2) ist …“ – das Geteilt-Zeichen steht am Zeilenende, der zweite Bruch in der nächsten Zeile.
5. **Lösungsweg: Bruch mit Term wirkt gequetscht (Fall c2).** 13,1 px und enge Abstände um + und −; lesbar, aber an der Grenze.
6. **Gemischte Zahl (Fall d): in Ordnung.** „1“ und Bruch bleiben zusammen, Abstand passt. Klein: die „1“ der ganzen Zahl und die „1“ im Bruch haben verschiedene Ziffernformen (im Bruch Tabellenziffern).

## Nebenbefund aus den Aufgabentexten (nicht im Bild)
Mit der Erkennung der App über alle Aufgaben in `inhalte/themen/` gezählt: 11 485 Brüche werden gestapelt. Als Text mit Schrägstrich bleiben u. a. 94 Texte mit Klammer-Brüchen wie „1/((x + 2)(x − 1))“ oder „1/(1/2)³“, 84 mit „ / “ zwischen Leerzeichen („(−14 ± 2) / 2“, „g(x) = x / 2“) und die 24 aus Punkt 2. Hochzahlen wie x^(1/2) bleiben mit Absicht Text.

## Meinung (Reihenfolge)
1. Antwortknöpfe: Bruch dort nicht verkleinern (Ziffern mindestens 14 px) und senkrecht zur Mitte des Kreises setzen.
2. Vorfaktor-Brüche im Lösungsweg stapeln oder wenigstens den Umbruch im Bruch verbieten – das ist eine Frage an Programmierer und Mathe-Profi, nicht an mich.
3. Zeilenhöhe: entweder feste größere Zeilenhöhe für Absätze mit Bruch oder Bruch etwas kleiner in der Frage (16 px statt 18 px); erst an echten Aufgaben mit mehreren Zeilen ansehen.

## Nicht geprüft
Kein echtes Gerät, kein Safari, kein Firefox; Tipp-Kasten, Fehler-Rückmeldung („Richtig ist: …“), Tabellen, Merkheft, Erklärkarten und Lehrer-Ansicht nicht aufgenommen; Vorlesen (aria-label „3 durch 4“) nicht gehört.
