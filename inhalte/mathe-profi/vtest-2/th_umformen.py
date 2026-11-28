import kern
from kern import *

# Welle 1, Runde 2 (nach Vorprüfung W1 und Urteil 1222): je Lernziel 5 Aufgaben (1 Test, 2 Korrektur, 2 Sicherung).
# Kennungen VT2-029 … VT2-043. Damit die übrigen Einheiten (umformen_teil2, kreis) ihre Kennungen und die Plätze ihrer
# Auswahl-Möglichkeiten behalten, werden am Ende Zähler und Auswahl-Zähler auf den alten Stand (VT2-049, 2 gemischte
# Auswahlaufgaben) gesetzt. Zuordnung alt → neu: korrektur-nach-vorpruefung-w1.md.
ALT_ENDE = 49          # letzte Kennung der Einheit vor der Kürzung (VT2-049)
ALT_AUSWAHL = 2        # gemischte Auswahlaufgaben der Einheit vor der Kürzung (VT2-032, VT2-039)


def bauen():
    start_kennung, start_auswahl = kern.ZAEHLER[0], kern._AUSW[0]
    einheit('terme.umformen')
    LP = 'M7 1 (Terme)'
    # ---------------- zusammenfassen ----------------
    lz = 'zusammenfassen'
    Z(lz, 'test', 'transfer', 'anwenden', 3, LP,
      'Ein Rechteck hat die Seitenlängen (3x + 2) cm und (x + 6) cm. Ein Quadrat hat die Seitenlänge (2x + a) cm. Beide Figuren haben für jede positive Zahl x denselben Umfang. Welche Zahl ist a?',
      4, '16 : 4',
      [(16, '2 · (2 + 6)', 'den konstanten Teil 16 des Rechtecksumfangs als a eingetragen, ohne durch 4 zu teilen'),
       (8, '2 + 6', 'nur die Zahlen der beiden Rechteckseiten addiert'),
       (2, '8 : 4', 'den Faktor 8 vor x durch 4 geteilt statt den konstanten Teil')],
      'Umfang des Rechtecks: 2 · ((3x + 2) + (x + 6)) = 2 · (4x + 8) = 8x + 16. Umfang des Quadrats: 4 · (2x + a) = 8x + 4a. Die x-Glieder stimmen schon überein; beide Umfänge sind für jedes positive x gleich, wenn auch 4a = 16 gilt, also a = 4. '
      'Für positive x sind dann alle Seitenlängen positiv (das Quadrat hat die Seite 2x + 4).',
      'Die Übungen fassen gegebene Terme zusammen; hier müssen zwei Umfänge als Terme aufgestellt, zusammengefasst und für jedes positive x gleichgesetzt werden.')
    A(lz, 'korrektur', 'fehler', 'fehler_detektiv', 2, LP,
      'Tim fasst 6x − 4y + 2x + 5y zusammen. Zeile 1: Gleichartig sind 6x und 2x sowie −4y und 5y. Zeile 2: Für die x-Glieder gilt 6x + 2x = 8x. Zeile 3: Für die y-Glieder gilt −4y + 5y = −9y. Zeile 4: Also ist 6x − 4y + 2x + 5y = 8x − 9y. In welcher Zeile steckt der erste Fehler, und warum?',
      ['In Zeile 1, weil x-Glieder und y-Glieder zusammengehören, denn in beiden steht eine Variable.',
       'In Zeile 2, weil 6x + 2x = 8x nicht gilt, wenn dazwischen y-Glieder stehen.',
       'In Zeile 3, weil −4y + 5y = 1y = y ist und Tim 4 und 5 addiert hat, statt sie zu verrechnen.',
       'In Zeile 4, weil das Ergebnis nur ein x-Glied haben darf.'], 2,
      {0: 'Glaubt, alle Variablen seien gleichartig; gleichartig sind nur Glieder mit derselben Variablen (und Hochzahl).',
       1: 'Meint, die Reihenfolge im Term verbiete das Zusammenfassen; die Glieder dürfen vertauscht werden.',
       3: 'Meint, ein Ergebnis dürfe nur eine Variable enthalten; 8x und y-Glieder bleiben getrennt stehen.'},
      'Zeile 1 und 2 stimmen. In Zeile 3 gilt −4y + 5y = (−4 + 5)y = y. Das richtige Ergebnis ist 8x + y.',
      'Fehler-Detektiv mit Begründung; die Übungen enthalten keine Rechnung zum Prüfen.')
    L(lz, 'korrektur', 'darstellung', None, 2, LP,
      'Zum Term 3x² + 5x − 2 wird genau ein weiteres Glied addiert: entweder a · x² oder a · x oder eine Zahl a (a ist eine ganze Zahl, aber nicht 0). Danach wird zusammengefasst. Wie viele Glieder kann das Ergebnis mindestens haben, und wie viele höchstens?',
      'mindestens □ Glieder, höchstens □ Glieder', [2, 3], ['3 − 1', '3'],
      [(1, 3, '3', 'übersehen, dass sich ein Glied ganz aufheben kann, zum Beispiel mit −3x²'),
       (1, 1, '3 − 2', 'gemeint, das neue Glied könne zwei Glieder auf einmal aufheben'),
       (2, 4, '3 + 1', 'das neue Glied als eigenes Glied gezählt, obwohl es mit einem gleichartigen Glied zusammengefasst wird')],
      'Jedes mögliche neue Glied ist gleichartig zu einem der drei vorhandenen (x²-Glied, x-Glied, Zahl) und wird mit ihm zusammengefasst; eine neue Art kommt nicht dazu. Also höchstens 3 Glieder. '
      'Ist das neue Glied genau das Gegenteil eines vorhandenen (−3x², −5x oder +2), hebt sich dieses Glied auf, zum Beispiel 3x² + 5x − 2 − 3x² = 5x − 2: 2 Glieder. Weniger geht nicht, weil nur ein Glied verändert wird.',
      'Die Übungen fassen gegebene Terme zusammen; hier wird über alle Möglichkeiten überlegt, was ein einziges gleichartiges Glied am Ergebnis ändern kann.')
    Z(lz, 'sicherung', 'transfer', 'anwenden', 2, LP,
      'Der Term 5x − 7 + 3 − 4x − x + 10 wird zusammengefasst. Welchen Wert hat er für x = 987 654?',
      6, '−7 + 3 + 10',
      [(0, '5 − 4 − 1', 'nur die x-Glieder betrachtet und die Zahlen vergessen'),
       (20, '7 + 3 + 10', 'alle Zahlen ohne Vorzeichen addiert'),
       (987660, '987654 + 6', 'die x-Glieder zu x zusammengefasst und das −x vergessen')],
      '5x − 4x − x = 0x: Die x-Glieder heben sich auf. Die Zahlen ergeben −7 + 3 + 10 = 6. Der Term hat für jede Zahl x den Wert 6, auch für x = 987 654; einsetzen und ausrechnen ist gar nicht nötig.',
      'Alle x-Glieder heben sich auf, der Wert hängt nicht von x ab; die Übungen haben immer ein x-Glied im Ergebnis.')
    Z(lz, 'sicherung', 'parameter', None, 2, LP,
      'Gegeben ist der Term 7a − 2b + 3 − 4a + 5b − a. Die Zahl a wird um 1 größer, gleichzeitig wird die Zahl b um 1 kleiner. Um wie viel wird der Wert des Terms dadurch kleiner?',
      1, '3 − 2',
      [(5, '2 + 3', 'beide Änderungen addiert, statt die Zunahme durch a gegen die Abnahme durch b zu verrechnen'),
       (3, '3', 'nur die Änderung durch b betrachtet'),
       (0, '3 − 3', 'beim Zusammenfassen das −a vergessen (3a statt 2a); dann heben sich die Änderungen scheinbar auf')],
      'Zusammengefasst: 7a − 4a − a = 2a und −2b + 5b = 3b, also 2a + 3b + 3. Wird a um 1 größer, wächst 2a um 2. Wird b um 1 kleiner, sinkt 3b um 3. Insgesamt + 2 − 3 = −1: Der Wert wird um 1 kleiner, ganz gleich, welche Zahlen a und b vorher waren.',
      'Die Übungen fassen Terme zusammen und setzen Zahlen ein; hier wird aus den Zahlen vor den Variablen abgelesen, wie sich der Wert bei einer Änderung verhält.')

    # ---------------- minusklammer ----------------
    lz = 'minusklammer'
    Z(lz, 'test', 'rueckwaerts', None, 3, LP,
      'Tim löst Minusklammern falsch auf: Er kehrt nur das Vorzeichen des ersten Glieds in der Klammer um, beim zweiten Glied lässt er das Vorzeichen stehen. So wird bei ihm aus 20 − (x − 5) der Term 20 − x − 5. Beim Term 40 − (3x − a) ist Tims Ergebnis für jede Zahl x um 18 kleiner als das richtige; a ist eine positive Zahl. Welche Zahl ist a?',
      9, '18 : 2',
      [(18, '18', 'den Unterschied selbst als a genommen'),
       (6, '18 : 3', 'den Unterschied durch die 3 vor x geteilt'),
       (36, '2 · 18', 'den Unterschied verdoppelt statt halbiert'),
       (22, '40 − 18', 'die 18 von der 40 abgezogen')],
      'Richtig ist 40 − (3x − a) = 40 − 3x + a. Tim schreibt 40 − 3x − a. Das x-Glied ist bei beiden gleich; der Unterschied steckt nur im letzten Glied: +a gegen −a, das sind 2 · a. Aus 2 · a = 18 folgt a = 9. '
      'Probe mit x = 1: richtig 40 − (3 − 9) = 46, bei Tim 40 − 3 − 9 = 28, Unterschied 18.',
      'Die Übungen lösen Klammern richtig auf oder beurteilen eine falsche Umformung; hier wird aus der Wirkung einer falschen Regel rückwärts auf eine Zahl in der Klammer geschlossen.')
    L(lz, 'korrektur', 'fehler', 'fehler_detektiv', 2, LP,
      'Mia löst auf: 4a − (3 − 2a) + (a − 1). Zeile 1: 4a − (3 − 2a) = 4a − 3 + 2a. Zeile 2: + (a − 1) = + a + 1. Zeile 3: Zusammen 4a − 3 + 2a + a + 1 = 7a − 2. In welcher Zeile steckt der erste Fehler, und wie lautet das richtige Ergebnis?',
      'Fehler in Zeile □, richtig: □a + □', [2, 7, -4], ['2', '4 + 2 + 1', '−3 − 1'],
      [(3, -2, '−3 + 1', 'wie Mia + (a − 1) als + a + 1 gerechnet: −3 + 1 = −2'),
       (1, 3, '3', 'den Folgefehler in Zeile 3 für den ersten Fehler gehalten'),
       (2, 3, '4 − 2 + 1', 'die 2a aus der ersten Klammer abgezogen statt addiert'),
       (3, 4, '3 + 1', 'die Zahlen −3 und −1 als +3 und +1 gerechnet')],
      'Zeile 1 stimmt. Bei einer Plusklammer bleiben die Vorzeichen: + (a − 1) = + a − 1. Dann ist 4a − 3 + 2a + a − 1 = 7a − 4.',
      'Unterschied Plus- und Minusklammer im selben Term; Fehler-Detektiv mit Berichtigung der ganzen Lösung.')
    A(lz, 'korrektur', 'darstellung', None, 2, LP,
      'Lisa hat 50 €. Ihr Einkauf kostet x €; an der Kasse werden davon 3 € Pfand für zurückgegebene Flaschen abgezogen. Ben schreibt für das Geld, das Lisa danach noch hat, den Term 50 − x − 3, Mia schreibt 50 − (x − 3). Welche Aussage stimmt?',
      ['Mia hat recht, denn Lisa zahlt x − 3 €, und durch das Pfand bleibt ihr mehr Geld übrig.',
       'Ben hat recht, denn das Pfand ist ebenfalls ein Betrag, der von Lisas 50 € abgeht.',
       'Beide haben recht, denn beide Terme enthalten 50, x und 3 und dazu zweimal ein Minuszeichen.',
       'Keiner hat recht, denn Lisa hat nach dem Einkauf 50 − x €, und das Pfand ändert daran nichts.'], 0,
      {1: 'Das Pfand wird vom Preis abgezogen, Lisa zahlt also weniger; Bens Term zieht die 3 € zusätzlich ab.',
       2: 'Die Klammer ändert das Vorzeichen der 3: 50 − (x − 3) = 50 − x + 3, das ist nicht 50 − x − 3.',
       3: 'Das Pfand senkt den Betrag, den Lisa zahlt; also hat sie danach mehr als 50 − x €.'},
      'Lisa zahlt den Preis minus Pfand, also (x − 3) €. Dieser ganze Betrag geht von 50 € ab: 50 − (x − 3) = 50 − x + 3 = 53 − x. Ben zieht die 3 € zusätzlich ab, als wäre das Pfand eine weitere Ausgabe. '
      'Beispiel x = 20: Lisa zahlt 17 € und hat danach 33 € (Mias Term: 50 − 17 = 33), Bens Term ergibt nur 27.',
      'Die Übungen rechnen mit fertigen Geld-Termen; hier muss man entscheiden, welcher Term die Sachlage beschreibt, und dabei die Wirkung der Minusklammer deuten.')
    L(lz, 'sicherung', 'transfer', None, 2, LP,
      'Aus dem Term T1 = x − 1 entsteht der nächste Term, indem man ihn in eine Klammer setzt und „x −“ davorschreibt: T2 = x − (x − 1), T3 = x − (x − (x − 1)), und so weiter. Welchen Wert haben T10 und T11 für x = 50?',
      'T10: □; T11: □', [1, 49], ['50 − 49', '50 − 1'],
      [(1, 49, '50 − 1', 'gerade und ungerade Nummern verwechselt: T10 hat wie T2 den Wert 1'),
       (1, 0, '50 − 50', 'gemeint, bei so vielen x hebe sich alles auf und es bleibe 0'),
       (2, 1, '50 − 49', 'gerade und ungerade Nummern verwechselt: T11 hat wie T1 den Wert x − 1'),
       (2, 51, '50 + 1', 'beim Auflösen die 1 mit dem falschen Vorzeichen genommen: x + 1 statt x − 1')],
      'T2 = x − (x − 1) = x − x + 1 = 1. T3 = x − T2 = x − 1, also wieder T1. T4 = x − T3 = 1, und so weiter: Jede gerade Nummer ergibt 1, jede ungerade x − 1. Also T10 = 1 und T11 = x − 1 = 49 für x = 50.',
      'Die Übungen lösen höchstens doppelt geschachtelte Klammern auf; hier wird ein Muster aus immer neuen Minusklammern erkannt und fortgesetzt.')
    L(lz, 'sicherung', 'transfer', None, 3, LP,
      'Für a und b werden zwei verschiedene Zahlen aus 1, 2, 3, 4 und 5 gewählt. Wie viele verschiedene Werte kann der Term 20 − (a − b) annehmen, und welches ist der größte?',
      'verschiedene Werte: □; größter Wert: □', [8, 24], ['4 + 4', '20 − (1 − 5)'],
      [(1, 20, '5 · 4', 'alle Paare (a, b) gezählt, auch wenn verschiedene Paare denselben Wert ergeben'),
       (1, 9, '4 + 4 + 1', 'den Wert 20 mitgezählt, der nur bei a = b entstünde'),
       (1, 4, '4', 'nur die Paare mit a größer als b betrachtet'),
       (2, 16, '20 − (5 − 1)', 'a möglichst groß und b möglichst klein gewählt'),
       (2, 14, '20 − 5 − 1', 'die Klammer weggelassen, ohne das Vorzeichen von b zu ändern')],
      '20 − (a − b) = 20 − a + b = 20 + (b − a). Der Wert hängt also nur vom Unterschied b − a ab. Bei zwei verschiedenen Zahlen aus 1 bis 5 kann b − a die Werte −4, −3, −2, −1, 1, 2, 3, 4 haben, also 8 verschiedene Werte (16 bis 24 ohne 20). '
      'Am größten wird der Term für b = 5 und a = 1: 20 − (1 − 5) = 24.',
      'Die Übungen lösen eine Klammer für gegebene Zahlen auf; hier zeigt das Auflösen, dass der Wert nur vom Unterschied zweier Zahlen abhängt, und darüber wird gezählt.')
    # ---------------- aequivalenz ----------------
    lz = 'aequivalenz'
    A(lz, 'test', 'begruenden', None, 3, LP,
      'Zwei Terme haben beide die Form a · x + b (a und b stehen jeweils für feste Zahlen, zum Beispiel 3x + 5 oder 2x − 1). Sie haben für x = 0 denselben Wert und auch für x = 1 denselben Wert. Welche Aussage stimmt?',
      ['Sie sind gleichwertig, denn x = 0 zeigt, dass die Zahlen b gleich sind, und x = 1 dann, dass auch die a gleich sind.',
       'Das weiß man nicht, denn durch Einsetzen einzelner Zahlen kann man nie beweisen, dass zwei Terme gleichwertig sind.',
       'Sie sind nicht gleichwertig, denn sie stimmen nur für die Zahlen 0 und 1 überein, für andere Zahlen meist nicht.',
       'Das weiß man erst, wenn sie auch für x = 2 übereinstimmen, denn für einen Beweis braucht man drei verschiedene Zahlen.'], 0,
      {1: 'Bei Termen der Form a · x + b genügen zwei Zahlen: x = 0 liefert b, x = 1 liefert a + b und damit auch a.',
       2: 'Sind a und b bei beiden Termen gleich, stimmen die Werte für jede Zahl überein, nicht nur für 0 und 1.',
       3: 'Eine dritte Probe ist hier unnötig; schon x = 0 und x = 1 legen beide Zahlen a und b fest.'},
      'Für x = 0 hat a · x + b den Wert b. Gleiche Werte bei x = 0 heißen also: Beide Terme haben dasselbe b. Für x = 1 hat der Term den Wert a + b; sind diese Werte gleich und ist b gleich, muss auch a gleich sein. '
      'Dann sind es dieselben Terme, also gleichwertig. Vorsicht: Das gilt nur, weil beide die Form a · x + b haben. x² und 3x − 2 haben zum Beispiel für x = 1 und x = 2 denselben Wert und sind trotzdem nicht gleichwertig.',
      'Die Übungen zeigen, dass ein einzelnes Beispiel keine Gleichwertigkeit beweist; hier wird begründet, warum bei Termen der Form a · x + b zwei Einsetzungen doch genügen.')
    A(lz, 'korrektur', 'darstellung', None, 2, LP,
      'Figur n besteht aus n Quadraten aus Streichhölzern in einer Reihe; benachbarte Quadrate haben ein Streichholz gemeinsam (Figur 1: 4 Hölzer, Figur 2: 7 Hölzer). Mia hat die Hölzer von Figur n mit dem Term 4 + 3 · (n − 1) gezählt. Wie hat Mia gezählt?',
      ['Sie hat das erste Quadrat mit 4 Hölzern gezählt und für jedes weitere Quadrat 3 Hölzer dazugenommen.',
       'Sie hat für jedes Quadrat 3 Hölzer gezählt und am Ende noch ein einzelnes Holz für den Anfang dazugenommen.',
       'Sie hat jedes Quadrat mit 4 Hölzern gezählt und danach die gemeinsamen Hölzer wieder abgezogen.',
       'Sie hat die n Hölzer oben, die n Hölzer unten und die senkrechten Hölzer jeweils getrennt gezählt.'], 0,
      {1: 'Diese Zählweise führt zu 3 · n + 1; das ist gleichwertig, aber nicht Mias Term.',
       2: 'Diese Zählweise führt zu 4 · n − (n − 1); auch gleichwertig, aber anders gebaut als Mias Term.',
       3: 'Diese Zählweise führt zu n + n + (n + 1); gleichwertig, aber nicht die Form 4 + 3 · (n − 1).'},
      'In 4 + 3 · (n − 1) steht die 4 einzeln, und 3 wird (n − 1)-mal genommen: erst ein ganzes Quadrat mit 4 Hölzern, dann für jedes der n − 1 weiteren Quadrate 3 neue Hölzer. '
      'Die anderen Zählweisen ergeben 3n + 1, 4n − (n − 1) und n + n + (n + 1). Alle vier Terme sind gleichwertig (jeweils 3n + 1), denn alle zählen dieselben Hölzer richtig; nur ihr Aufbau verrät den Zählweg.',
      'Die Übungen prüfen, ob zwei Zählterme gleichwertig sind; hier wird umgekehrt aus dem Aufbau eines Terms die Zählweise erschlossen, während alle angebotenen Zählweisen richtig zählen.')
    Z(lz, 'korrektur', 'rueckwaerts', None, 2, LP,
      'Mia stellt ein Zahlenrätsel: „Denke dir eine Zahl. Verdopple sie, addiere eine Zahl k, halbiere das Ergebnis und ziehe die gedachte Zahl ab.“ Mia will, dass für jede gedachte Zahl 10 herauskommt. Welche Zahl muss sie für k wählen?',
      20, '2 · 10',
      [(10, '10', 'k gleich dem gewünschten Ergebnis gesetzt; beim Halbieren wird aber auch k halbiert'),
       (5, '10 : 2', 'das gewünschte Ergebnis halbiert statt verdoppelt'),
       (40, '4 · 10', 'zweimal verdoppelt, weil im Rätsel „verdoppeln“ und „halbieren“ vorkommen')],
      'Als Term mit der gedachten Zahl x: (2x + k) : 2 − x = x + k : 2 − x = k : 2. Die gedachte Zahl fällt heraus; übrig bleibt die Hälfte von k. Damit immer 10 herauskommt, muss k : 2 = 10 sein, also k = 20. Probe mit 7: 14, 34, 17, 17 − 7 = 10.',
      'Die Übungen vergleichen gegebene Terme; hier wird ein Zahlenrätsel als Term geschrieben, um zu sehen, warum das Ergebnis nicht von der gedachten Zahl abhängt, und rückwärts eine Zahl bestimmt.')
    A(lz, 'sicherung', 'begruenden', None, 3, LP,
      'Gegeben sind die Terme a · x + 9 und 2x + b; a und b sind feste Zahlen. Welche Aussage stimmt?',
      ['Ist a = 2 und b nicht 9, so haben die beiden Terme für keine Zahl x denselben Wert.',
       'Ist a nicht 2 und b = 9, so haben die beiden Terme für keine Zahl x denselben Wert.',
       'Ist a = 2 und b = 9, so haben die beiden Terme für genau eine Zahl x denselben Wert.',
       'Ist a nicht 2 und b nicht 9, so haben die beiden Terme für keine Zahl x denselben Wert.'], 0,
      {1: 'Für x = 0 haben beide den Wert 9; bei a nicht 2 stimmen sie genau dort überein.',
       2: 'Bei a = 2 und b = 9 sind es dieselben Terme; sie stimmen für jede Zahl x überein, nicht nur für eine.',
       3: 'Bei verschiedenen Zahlen vor x gibt es genau eine Stelle, an der beide Werte gleich sind, zum Beispiel a = 3, b = 4: 3x + 9 = 2x + 4 für x = −5.'},
      'Der Unterschied der Terme ist (a · x + 9) − (2x + b) = (a − 2) · x + (9 − b). Ist a = 2, fällt das x weg, und der Unterschied ist immer 9 − b: für b = 9 immer 0 (gleichwertig), für b nicht 9 nie 0 (keine Übereinstimmung). '
      'Ist a nicht 2, ändert sich der Unterschied mit x und ist an genau einer Stelle 0.',
      'Die Übungen suchen eine einzelne Übereinstimmung oder prüfen zwei feste Terme; hier werden alle Fälle (keine, genau eine, jede Zahl) nach den Zahlen vor x und den Zahlgliedern unterschieden.')
    Z(lz, 'sicherung', 'darstellung', None, 2, LP,
      'Anna schreibt sechs Terme auf: A = 2(x + 3), B = 2x + 6, C = 3(x + 2) − x, D = 5x − 2(x + 1), E = 3x − 2, F = 3x + 2. Zwei Terme bilden ein gleichwertiges Paar, wenn sie für jede Zahl x denselben Wert haben (zum Beispiel A und B). Wie viele solche Paare gibt es insgesamt? Jedes Paar wird nur einmal gezählt.',
      4, '3 + 1',
      [(3, '3', 'nur die Gruppe A, B, C gezählt, das Paar D und E vergessen'),
       (15, '6 · 5 : 2', 'alle Paare aus sechs Termen gezählt'),
       (2, '1 + 1', 'nur die Paare A–B und D–E gezählt, C übersehen'),
       (5, '3 + 1 + 1', 'F mit E als Paar mitgezählt, weil 3x + 2 und 3x − 2 „fast gleich“ aussehen')],
      'Zusammengefasst: A = 2x + 6, B = 2x + 6, C = 3x + 6 − x = 2x + 6, D = 5x − 2x − 2 = 3x − 2, E = 3x − 2, F = 3x + 2. A, B und C sind gleichwertig (3 Paare), D und E sind gleichwertig (1 Paar), F ist zu keinem gleichwertig. Zusammen 3 + 1 = 4 Paare.',
      'Die Übungen prüfen zwei Terme gegeneinander; hier werden sechs Terme vereinfacht, in Gruppen gleichwertiger Terme eingeordnet und die Paare gezählt.')

    # Zähler auf den alten Stand setzen (die folgenden Einheiten bleiben unverändert)
    gemischt = kern._AUSW[0] - start_auswahl
    assert kern.ZAEHLER[0] <= ALT_ENDE, kern.ZAEHLER[0]
    assert start_kennung == 28, start_kennung
    kern.ZAEHLER[0] = ALT_ENDE
    kern._AUSW[0] = start_auswahl + ALT_AUSWAHL
    return gemischt
