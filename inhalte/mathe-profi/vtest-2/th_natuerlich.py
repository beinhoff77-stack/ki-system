from kern import *

# Welle 1, Runde 2 (nach Vorprüfung W1 und Urteil 1222): je Lernziel 5 Aufgaben (1 Test, 2 Korrektur, 2 Sicherung).
# Kennungen VT2-085 … VT2-119. Zuordnung alt → neu und Abarbeitung der Befunde: korrektur-nach-vorpruefung-w1.md.


def bauen():
    einheit('zahlen.natuerlich')
    LP = 'M5 1 (Natürliche Zahlen)'
    # ---------------- stellenwert ----------------
    lz = 'stellenwert'
    Z(lz, 'test', 'rueckwaerts', None, 3, LP,
      'Eine sechsstellige Zahl enthält die Ziffer 4 genau zweimal. Die vordere 4 ist 1 000-mal so viel wert wie die hintere 4. Die vier übrigen Ziffern sind alle voneinander verschieden. Wie heißt die größte Zahl, für die das alles gilt?',
      984764, '900000 + 80000 + 4000 + 700 + 60 + 4',
      [(987644, '987644', 'die beiden Vieren nebeneinander ans Ende gesetzt; dann ist die vordere 4 nur 10-mal so viel wert wie die hintere'),
       (987464, '987464', 'zwei Stellen Abstand gewählt; dann ist die vordere 4 nur 100-mal so viel wert wie die hintere'),
       (948764, '948764', 'vier Stellen Abstand gewählt, weil 1 000 vier Ziffern hat; dann ist die vordere 4 sogar 10 000-mal so viel wert'),
       (948746, '948746', 'den Abstand von drei Stellen richtig gewählt, die Vieren aber an die 2. und 5. statt an die 3. und 6. Stelle gesetzt')],
      '1 000-mal so viel wert heißt: Die vordere 4 steht drei Stellen weiter links als die hintere (zum Beispiel Tausender und Einer). '
      'In einer sechsstelligen Zahl geht das an den Stellen 1 und 4, 2 und 5 oder 3 und 6 (von links gezählt). Damit die Zahl groß wird, sollen vorn '
      'möglichst große Ziffern stehen: 9 und 8 vor der vorderen 4, dann 7 und 6 auf die übrigen Plätze: 984 764. Probe: Die vordere 4 ist 4 000 wert, '
      'die hintere 4 ist 4 wert, das ist 1 000-mal so viel. Mit den Vieren an Stelle 2 und 5 wäre die größte Zahl nur 948 746.',
      'Die Übungen fragen nach dem Wert einer Ziffer an einer genannten Stelle; hier muss aus einem Wertverhältnis der Abstand zweier Stellen erschlossen und daraus die größte passende Zahl gebaut werden.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'In einer Zahl tauschen die Ziffer an der Zehntausenderstelle und die Ziffer an der Tausenderstelle ihre Plätze; alle anderen Ziffern bleiben, wie sie sind. Dadurch wird die Zahl um genau 36 000 größer. Welche Aussage folgt sicher daraus?',
      ['Die Tausenderziffer war um 4 größer als die Zehntausenderziffer, denn jeder Unterschied von 1 bringt hier 9 000.',
       'Die beiden Ziffern waren 0 und 4, denn nur dann wird die Zahl durch den Tausch um genau 36 000 größer.',
       'Die Zehntausenderziffer war um 4 größer als die Tausenderziffer, denn sie steht weiter links und zählt deshalb mehr.',
       'Über die beiden Ziffern lässt sich nichts sagen, denn der Zuwachs hängt auch von den übrigen Ziffern ab.'], 0,
      {1: 'Hält ein passendes Beispiel für das einzige: Auch 1 und 5, 2 und 6 bis 5 und 9 ergeben 36 000, denn es zählt nur der Unterschied der beiden Ziffern.',
       2: 'Verwechselt die Richtung: Rückt die größere Ziffer von der Zehntausender- an die Tausenderstelle, wird die Zahl kleiner, nicht größer.',
       3: 'Übersieht, dass die übrigen Ziffern an ihrem Platz bleiben und zum Zuwachs nichts beitragen.'},
      'Nur die beiden getauschten Stellen ändern sich. Ist die Tausenderziffer um 1 größer als die Zehntausenderziffer, so gewinnt die Zahl nach dem Tausch an der '
      'Zehntausenderstelle 10 000 und verliert an der Tausenderstelle 1 000, zusammen 9 000. Bei einem Unterschied von 4 sind es 4 · 9 000 = 36 000. '
      'Die Tausenderziffer war also um 4 größer; welche zwei Ziffern es genau waren (0 und 4, 1 und 5, …, 5 und 9), lässt sich nicht sagen.',
      'Die Übungen tauschen zwei Ziffern einer gegebenen Zahl und rechnen den Zuwachs aus; hier wird aus dem Zuwachs geschlossen, was über die Ziffern sicher feststeht und was offen bleibt.')
    L(lz, 'korrektur', 'fehler', 'fehler_detektiv', 2, LP,
      'Ben bestimmt den Wert der Ziffer 6 in der Zahl 360 482. Zeile 1: Die 6 ist die zweite Ziffer von links. Zeile 2: Die zweite Stelle von links ist die Tausenderstelle. Zeile 3: Also ist die 6 hier 6 · 1 000 = 6 000 wert. In welcher Zeile steckt der erste Fehler, und wie viel ist die 6 wirklich wert?',
      'Fehler in Zeile □, die 6 ist □ wert', [2, 60000], ['2', '6 · 10000'],
      [(2, 6000, '6 · 1000', 'wie Ben die Tausenderstelle genommen'),
       (2, 600000, '6 · 100000', 'die Hunderttausenderstelle genommen'),
       (2, 6, '6', 'nur die Ziffer selbst als Wert genommen'),
       (1, 1, '1', 'Zeile 1 für falsch gehalten, obwohl die 6 wirklich an zweiter Stelle von links steht')],
      'Die Zahl 360 482 hat sechs Stellen: 3 Hunderttausender, 6 Zehntausender, 0 Tausender, 4 Hunderter, 8 Zehner, 2 Einer. Die zweite Stelle von links ist die Zehntausenderstelle. Die 6 ist 6 · 10 000 = 60 000 wert.',
      'Fehler-Detektiv bei der Zuordnung Stelle ↔ Stellenwert; die Übungen lesen Ziffern an einer genannten Stelle ab.')
    A(lz, 'sicherung', 'begruenden', None, 2, LP,
      'Welche Aussage über die beiden Nullen in der Zahl 7 090 stimmt?',
      ['Die Nullen sind nichts wert und dürfen weggelassen werden: 7 090 ist dasselbe wie 79.',
       'Die Nullen halten Hunderter- und Einerstelle frei, ohne sie wäre die Zahl 79.',
       'Nur die mittlere Null wird gebraucht, die Null am Ende darf wegfallen, denn 709 ist so viel wie 7 090.',
       'Nur die Null am Ende wird gebraucht, denn die mittlere Null spricht man nicht mit: 7 090 ist wie 790.'], 1,
      {0: 'Die Nullen sind selbst nichts wert, bestimmen aber, an welchen Stellen die 7 und die 9 stehen; 79 ist viel kleiner als 7 090.',
       2: 'Auch die Null am Ende hält eine Stelle frei: Ohne sie rücken 7, 0 und 9 eine Stelle nach rechts, 709 ist zehnmal kleiner als 7 090.',
       3: 'Was man nicht spricht, kann trotzdem nötig sein: Ohne die mittlere Null stünde die 7 an der Hunderterstelle, 790 ist viel kleiner.'},
      '7 090 = 7 Tausender + 0 Hunderter + 9 Zehner + 0 Einer. Beide Nullen sind Platzhalter: Lässt man eine von ihnen weg, rücken die Ziffern davor nach rechts (709 oder 790), ohne beide wird die Zahl 79.',
      'Die Rolle beider Nullen als Platzhalter wird begründet, auch der nicht gesprochenen; die Übungen lesen Ziffern ab oder schreiben eine Zahl aus einer Stellenwerttafel.')
    L(lz, 'sicherung', 'transfer', None, 3, LP,
      'In eine Stellenwerttafel mit den Spalten T (Tausender), H, Z und E werden genau 12 gleiche Plättchen gelegt. In einer Spalte dürfen höchstens 9 Plättchen liegen, eine Spalte darf auch leer bleiben. Die Zahl der Plättchen in einer Spalte ist die Ziffer an dieser Stelle. Welches ist die kleinste und welches die größte Zahl, die man so legen kann?',
      'kleinste Zahl □; größte Zahl □', [39, 9300], ['3 · 10 + 9', '9 · 1000 + 3 · 100'],
      [(1, 12, '12', 'alle 12 Plättchen in die Einerspalte gelegt und die Grenze von 9 Plättchen je Spalte übersehen'),
       (1, 93, '9 · 10 + 3', '9 Plättchen in die Zehner- und 3 in die Einerspalte gelegt; umgekehrt wird die Zahl kleiner'),
       (1, 66, '6 · 10 + 6', 'die Plättchen gleichmäßig auf Zehner und Einer verteilt'),
       (2, 3900, '3 · 1000 + 9 · 100', '9 Plättchen in die Hunderter- und nur 3 in die Tausenderspalte gelegt'),
       (2, 3333, '3 · 1000 + 3 · 100 + 3 · 10 + 3', 'die Plättchen gleichmäßig auf alle vier Spalten verteilt'),
       (2, 12000, '12 · 1000', 'alle 12 Plättchen in die Tausenderspalte gelegt, obwohl höchstens 9 erlaubt sind')],
      'Ein Plättchen ist umso weniger wert, je weiter rechts es liegt. Für die kleinste Zahl legt man so viele wie möglich nach rechts: 9 in die Einerspalte, die übrigen 3 in die Zehnerspalte: 39. '
      'Mit nur einer Spalte geht es nicht, weil dort höchstens 9 Plättchen liegen dürfen. Für die größte Zahl legt man so viele wie möglich nach links: 9 in die Tausenderspalte, 3 in die Hunderterspalte: 9 300.',
      'Die Übungen lesen eine fertige Stellenwerttafel ab; hier muss man den Wert der Spalten nutzen, um mit einer festen Zahl von Plättchen die kleinste und die größte Zahl zu bauen.')

    # ---------------- ziffern_zu_zahlwort ----------------
    lz = 'ziffern_zu_zahlwort'
    Z(lz, 'test', 'transfer', None, 3, LP,
      'Betrachtet werden alle Zahlen, die größer als eine Million und kleiner als zwei Millionen sind. Bei wie vielen dieser Zahlen kommt im Zahlwort das Wort „tausend“ nicht vor (auch nicht als Teil eines Wortes wie „dreitausend“ oder „hunderttausend“)?',
      999, '1000999 − 1000001 + 1',
      [(1000, '999 + 1', 'die Zahl 1 000 000 mitgezählt, obwohl sie nicht größer als eine Million ist'),
       (0, '0', 'gemeint, in jeder siebenstelligen Zahl komme das Wort „tausend“ vor'),
       (999000, '999999 − 999', 'die Zahlen gezählt, in denen „tausend“ vorkommt, statt die ohne')],
      'Alle diese Zahlen haben sieben Stellen: Millionenklasse 1, dann Tausenderklasse und Einerklasse. Das Wort „tausend“ fällt genau dann weg, wenn die Tausenderklasse 000 ist; '
      'eine leere Klasse wird nicht gesprochen. Das sind die Zahlen 1 000 001 („eine Million eins“) bis 1 000 999 („eine Million neunhundertneunundneunzig“), also 1 000 999 − 1 000 001 + 1 = 999 Zahlen. '
      'Schon 1 001 000 heißt „eine Million eintausend“.',
      'Die Übungen lesen einzelne Zahlen; hier muss man aus dem Aufbau des Zahlworts nach Klassen erschließen, wann ein Wort wegfällt, und alle passenden Zahlen eines Bereichs zählen.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Das Zahlwort einer Zahl beginnt mit „zehn Millionen“; danach kann noch etwas folgen oder auch nichts. Wie viele Stellen hat die Zahl, wenn man sie mit Ziffern schreibt?',
      ['Immer acht, denn hinter der Millionenklasse 10 stehen stets zwei volle Dreiergruppen, notfalls aus Nullen.',
       'Das hängt vom Rest ab, denn nur wenn danach noch Tausender und Einer genannt werden, braucht man alle Stellen.',
       'Immer sieben, denn eine Million hat sieben Stellen, und zehn Millionen gehören ebenfalls zu den Millionen.',
       'Mehr als acht, sobald noch etwas folgt, denn jedes weitere Wort wie „tausend“ oder „hundert“ hängt Stellen an.'], 0,
      {1: 'Auch Klassen, die man nicht spricht, schreibt man mit Nullen: „zehn Millionen fünf“ ist 10 000 005 mit acht Stellen.',
       2: 'Zehn Millionen sind schon 10 000 000 mit acht Stellen; die Millionenklasse ist hier zweistellig.',
       3: 'Weitere Wörter füllen nur die Nullen der Tausender- und Einerklasse; auch „zehn Millionen neunhundertneunundneunzigtausend…“ hat acht Stellen.'},
      '„zehn Millionen“ heißt: Die Millionenklasse ist 10. Dahinter kommen immer die Tausenderklasse und die Einerklasse mit je drei Stellen, auch wenn sie nur Nullen enthalten und man sie nicht spricht. '
      'Also 2 + 3 + 3 = 8 Stellen, von 10 000 000 („zehn Millionen“) bis 10 999 999.',
      'Die Übungen lesen einzelne Zahlen; hier wird allgemein begründet, dass nicht gesprochene Klassen trotzdem ihre Stellen behalten.')
    A(lz, 'korrektur', 'fehler', 'fehler_detektiv', 2, LP,
      'Nina liest die Zahl 3 000 900. Zeile 1: Die Zahl hat sieben Stellen: Millionenklasse, Tausenderklasse und Einerklasse. Zeile 2: Die Millionenklasse ist 3, die Tausenderklasse besteht nur aus Nullen. Zeile 3: Die 9 steht deshalb an der Hunderttausenderstelle: neunhunderttausend. Zeile 4: Nina liest also „drei Millionen neunhunderttausend“. In welcher Zeile steckt der erste Fehler, und warum?',
      ['In Zeile 1, weil eine siebenstellige Zahl keine Millionenklasse hat, sondern nur eine Tausenderklasse.',
       'In Zeile 2, weil eine Klasse nicht nur aus Nullen bestehen darf; man müsste dort eine Ziffer ergänzen.',
       'In Zeile 3, weil die 9 in der Einerklasse steht und nur die Tausenderklasse aus Nullen besteht.',
       'In Zeile 4, weil man das Wort „Millionen“ nie mit dem Wort „hundert“ verbinden darf.'], 2,
      {0: 'Eine siebenstellige Zahl hat sehr wohl eine Millionenklasse (7 Stellen = 1 + 3 + 3).',
       1: 'Eine Klasse kann aus Nullen bestehen; man spricht sie dann nicht aus.',
       3: 'Das Wort „Millionen“ kann mit jedem anderen Zahlwort verbunden werden; der Fehler liegt schon bei der Stelle der 9.'},
      'Von rechts in Dreiergruppen: 3 | 000 | 900. Die Tausenderklasse ist 000 und wird nicht gesprochen. Die 900 steht in der Einerklasse: neunhundert. Richtig: drei Millionen neunhundert.',
      'Fehler-Detektiv beim Lesen einer Zahl mit ausgefallener Tausenderklasse; die Übungen haben keine ganze Nullklasse.')
    Z(lz, 'sicherung', 'transfer', None, 3, LP,
      'Tim teilt eine Zahl zum Lesen von links in Dreiergruppen ein statt von rechts und liest die Gruppen dann wie üblich mit „Millionen“ und „tausend“. Aus 45 000 120 macht er so 450 | 001 | 20. Wie viele der Zahlen von 1 000 bis 999 999 liest Tim trotzdem richtig?',
      900000, '999999 − 100000 + 1',
      [(999000, '999999 − 1000 + 1', 'alle Zahlen von 1 000 bis 999 999 gezählt, als ändere die Einteilung von links nichts'),
       (0, '0', 'gemeint, eine Einteilung von links führe immer zu einem falschen Zahlwort'),
       (990000, '999999 − 10000 + 1', 'die fünfstelligen Zahlen mitgezählt; bei ihnen bekommt die erste Gruppe von links aber drei statt zwei Ziffern')],
      'Die Klassen (Einer, Tausender, Millionen) beginnen immer rechts bei den Einern. Teilt man von links ein, stimmen die Gruppen nur dann mit den Klassen überein, wenn die Stellenzahl durch 3 teilbar ist. '
      'Von 1 000 bis 999 999 sind das die sechsstelligen Zahlen 100 000 bis 999 999, also 999 999 − 100 000 + 1 = 900 000 Zahlen. Bei vier- und fünfstelligen Zahlen geht es schief: 4 500 würde zu 450 | 0, also „vierhundertfünfzigtausend“.',
      'Die Übungen teilen von rechts in Dreiergruppen; hier wird untersucht, warum gerade von rechts und wann eine falsche Einteilung zufällig dasselbe ergibt.')
    L(lz, 'sicherung', 'transfer', None, 3, LP,
      'Eine Zahl, die kleiner als eine Milliarde ist, wird laut gelesen. Wie oft kann das Wort „hundert“ im Zahlwort höchstens vorkommen (auch als Teil eines Wortes wie „dreihundert“ oder „hunderttausend“)? Wie heißt die kleinste Zahl, bei der es so oft vorkommt?',
      'höchstens □-mal; kleinste Zahl □', [3, 100100100], ['3', '100000000 + 100000 + 100'],
      [(1, 9, '9', 'für jede der neun Stellen ein „hundert“ angenommen'),
       (1, 6, '3 · 2', 'gemeint, jede Klasse könne „hundert“ zweimal enthalten'),
       (2, 111111111, '111111111', 'an jeder Stelle eine 1 gesetzt; Zehner- und Einerziffern dürfen aber 0 sein'),
       (2, 100100, '100000 + 100', 'nur Tausender- und Einerklasse beachtet, die Millionenklasse vergessen')],
      'Jede Klasse (Millionen, Tausender, Einer) wird wie eine dreistellige Zahl gelesen. „hundert“ kommt in einer Klasse genau einmal vor, wenn ihre Hunderterziffer nicht 0 ist, sonst gar nicht. '
      'Eine Zahl unter einer Milliarde hat höchstens drei Klassen, also kommt „hundert“ höchstens dreimal vor. Dafür muss in jeder Klasse die Hunderterziffer mindestens 1 sein; am kleinsten wird die Zahl, '
      'wenn alle anderen Ziffern 0 sind: 100 100 100 („einhundert Millionen einhunderttausendeinhundert“).',
      'Die Übungen zählen, wie oft ein Wort in einer gegebenen Zahl vorkommt; hier wird über alle Zahlen hinweg die Höchstzahl begründet und die kleinste passende Zahl gebaut.')

    # ---------------- strahl_eintragen ----------------
    lz = 'strahl_eintragen'
    L(lz, 'test', 'transfer', 'anwenden', 3, LP,
      'Auf einem Zahlenstrahl mit gleichmäßiger Skala liegen die Marken 1 200 und 2 000 genau 4 cm auseinander. Wie viele cm ist die Marke 3 400 von der Marke 1 200 entfernt, und welche Zahl liegt 9 cm rechts von der Marke 1 200?',
      'Entfernung □ cm; Zahl □', [11, 3000], ['2200 : 200', '1200 + 9 · 200'],
      [(1, 2200, '3400 − 1200', 'die Zahlendifferenz als Strecke in cm angegeben'),
       (1, 17, '3400 : 200', 'von 0 aus gerechnet statt ab der Marke 1 200'),
       (2, 1800, '9 · 200', 'nur den Zuwachs angegeben, die Marke 1 200 nicht dazugerechnet'),
       (2, 1236, '1200 + 9 · 4', 'die 4 cm als Wert je cm genommen')],
      '4 cm entsprechen 2 000 − 1 200 = 800, also steht 1 cm für 200. Von 1 200 bis 3 400 sind es 2 200, das sind 2 200 : 200 = 11 cm. 9 cm entsprechen 9 · 200 = 1 800; 1 200 + 1 800 = 3 000.',
      'Die Übungen markieren eine Zahl auf einer vorgegebenen Skala ab 0; hier muss ein Maßstab aus zwei Marken ohne Nullpunkt erschlossen und in beide Richtungen übertragen werden.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Ein Zahlenstrahl beginnt bei 300; die Striche haben gleiche Abstände und sind der Reihe nach mit 300, 500, 700, 900, … beschriftet. Tim behauptet: „Wenn eine Zahl auf einem Strich liegt, dann liegt auch das Doppelte dieser Zahl auf einem Strich.“ Welche Aussage stimmt?',
      ['Das stimmt nie, denn Striche tragen 3, 5, 7, … Hunderter, die Doppelten 600, 1 000, 1 400, … liegen zwischen zwei Strichen.',
       'Das stimmt immer, denn verdoppelt man eine Zahl, die auf einem Strich liegt, kommt man wieder genau auf einen Strich.',
       'Das stimmt manchmal, zum Beispiel bei 500, denn das Doppelte 1 000 ist eine runde Zahl und liegt deshalb sicher auf einem Strich.',
       'Das lässt sich nicht entscheiden, denn man weiß nicht, wie viele Zentimeter ein Abstand zwischen zwei Strichen lang ist.'], 0,
      {1: 'Das gilt nur, wenn der Strahl bei 0 beginnt; hier beginnt er bei 300, und schon 300 · 2 = 600 liegt zwischen 500 und 700.',
       2: '1 000 liegt zwischen den Strichen 900 und 1 100; eine runde Zahl muss nicht auf einem Strich liegen.',
       3: 'Ob eine Zahl auf einem Strich liegt, hängt nur von den Zahlen an den Strichen ab, nicht von der Länge in cm.'},
      'Die Striche gehören zu 300, 500, 700, 900, 1 100, …: jedes Mal eine ungerade Anzahl von Hundertern (3, 5, 7, 9, 11, …). Verdoppelt man eine solche Zahl, entsteht eine gerade Anzahl von Hundertern: '
      '600, 1 000, 1 400, 1 800, … Diese Zahlen liegen genau in der Mitte zwischen zwei Strichen. Tims Satz stimmt also für keine einzige Strichzahl.',
      'Die Übungen tragen einzelne Zahlen ein; hier wird für alle Strichzahlen entschieden, ob eine Eigenschaft gilt, wenn der Strahl nicht bei 0 beginnt.')
    A(lz, 'korrektur', 'darstellung', None, 2, LP,
      'Auf Zahlenstrahl A steht 1 cm für 50, auf Zahlenstrahl B steht 1 cm für 200. Auf beiden Strahlen werden die Zahlen 400 und 1 000 eingetragen. Welche Aussage über den Abstand der beiden Marken stimmt?',
      ['Auf A liegen die Marken 4-mal so weit auseinander wie auf B, denn dort braucht derselbe Unterschied mehr cm.',
       'Auf B liegen die Marken 4-mal so weit auseinander wie auf A, denn dort steht jeder Zentimeter für eine größere Zahl.',
       'Auf beiden liegen die Marken gleich weit auseinander, denn es sind auf beiden dieselben zwei Zahlen.',
       'Das kann man nicht sagen, denn man weiß nicht, an welcher Stelle der beiden Strahlen jeweils die 0 liegt.'], 0,
      {1: 'Steht 1 cm für mehr, braucht man für den Unterschied 600 weniger cm: auf B 3 cm, auf A 12 cm.',
       2: 'Dieselben Zahlen liegen nur bei gleichem Maßstab gleich weit auseinander: 12 cm auf A, 3 cm auf B.',
       3: 'Der Abstand zweier Marken hängt nur vom Unterschied der Zahlen (600) und vom Maßstab ab, nicht von der Lage der 0.'},
      'Der Abstand hängt nur vom Unterschied 1 000 − 400 = 600 ab. Auf A sind das 600 : 50 = 12 cm, auf B 600 : 200 = 3 cm. 12 cm sind 4-mal so viel wie 3 cm. '
      'Das sieht man auch ohne Rechnen: Auf A steht 1 cm für ein Viertel so viel wie auf B, also braucht jeder Unterschied auf A 4-mal so viel Platz.',
      'Die Übungen markieren Zahlen auf einem Strahl; hier werden zwei Maßstäbe verglichen, und es kommt nicht darauf an, wo die Zahlen genau liegen.')
    Z(lz, 'sicherung', 'transfer', None, 3, LP,
      'Anna teilt den Zahlenstrahl von 0 bis 1 200 in 6 gleich große Abschnitte, Ben teilt ihn in 8 gleich große Abschnitte. Wie viele Zahlen zwischen 0 und 1 200 (ohne 0 und 1 200) liegen bei beiden auf einem Teilstrich?',
      1, '1',
      [(5, '6 − 1', 'nur die Teilstriche auf Annas Strahl gezählt'),
       (7, '8 − 1', 'nur die Teilstriche auf Bens Strahl gezählt'),
       (12, '5 + 7', 'die Teilstriche beider Strahlen addiert')],
      'Annas Abschnitte sind 1 200 : 6 = 200 lang, Bens Abschnitte 1 200 : 8 = 150. Auf beiden Strahlen liegt eine Zahl auf einem Teilstrich, wenn sie ein Vielfaches von 200 und von 150 ist: 600 (und 1 200, das ist aber das Ende). Zwischen 0 und 1 200 ist es nur die 600.',
      'Die Übungen tragen Zahlen auf einer Skala ein; hier werden zwei verschiedene Teilungen desselben Strahls verglichen.')
    A(lz, 'sicherung', 'begruenden', None, 3, LP,
      'Mia zeichnet einen Strahl mit gleich großen Abständen zwischen den Strichen und beschriftet die Striche der Reihe nach mit 0, 10, 100 und 1 000. Welche Aussage über Mias Zahlenstrahl stimmt?',
      ['Er ist falsch beschriftet, denn gleich lange Abschnitte müssen gleich große Unterschiede haben, hier sind es 10, 90 und 900.',
       'Er ist richtig beschriftet, denn von Strich zu Strich wird die Zahl jedes Mal zehnmal so groß, und das ist doch ganz gleichmäßig.',
       'Nur der erste Abschnitt passt nicht, denn 10, 100 und 1 000 haben untereinander gleiche Abstände, nur die 0 stört.',
       'Das lässt sich nicht entscheiden, denn dafür müsste man wissen, wie viele Zentimeter ein Abschnitt lang ist.'], 0,
      {1: 'Auf einem Zahlenstrahl gehören gleich lange Strecken zu gleichen Unterschieden, nicht zu gleichen Vervielfachungen: 0 bis 10 ist ein Unterschied von 10, 100 bis 1 000 einer von 900.',
       2: 'Auch 10, 100 und 1 000 haben verschiedene Unterschiede (90 und 900); der Abschnitt von 100 bis 1 000 müsste 10-mal so lang sein wie der von 10 bis 100.',
       3: 'Die Länge in cm spielt keine Rolle; schon die Zahlen zeigen, dass gleich lange Abschnitte hier verschiedene Unterschiede hätten.'},
      'Auf einem Zahlenstrahl entspricht jeder gleich lange Abschnitt demselben Unterschied. Bei Mia sind die Unterschiede 10 − 0 = 10, 100 − 10 = 90 und 1 000 − 100 = 900, obwohl die Abschnitte gleich lang sind. '
      'Richtig wäre zum Beispiel 0, 10, 20, 30; für 0, 10, 100 und 1 000 müssten die Abschnitte 1-, 9- und 90-mal so lang sein wie der erste.',
      'Der Maßstabsgedanke (gleiche Strecken = gleiche Zahlenunterschiede) wird an einer falschen, aber „regelmäßig“ wirkenden Beschriftung begründet; die Übungen tragen Zahlen auf einer richtigen Skala ein.')

    # ---------------- runden_regel ----------------
    lz = 'runden_regel'
    Z(lz, 'test', 'transfer', None, 3, LP,
      'Für wie viele natürliche Zahlen von 1 bis 100 ergibt das Runden auf Zehner dieselbe Zahl wie das Runden auf Hunderter?',
      10, '4 + 6',
      [(6, '100 − 95 + 1', 'nur die Zahlen 95 bis 100 gezählt, die kleinen Zahlen 1 bis 4 vergessen (beide Rundungen ergeben dort 0)'),
       (4, '4', 'nur die Zahlen 1 bis 4 gezählt, die Zahlen 95 bis 100 vergessen'),
       (11, '4 + 6 + 1', 'die 5 mitgezählt, obwohl sie auf Zehner 10, auf Hunderter aber 0 ergibt')],
      'Auf Hunderter gerundet ergeben die Zahlen 1 bis 49 den Wert 0 und die Zahlen 50 bis 100 den Wert 100. Auf Zehner gerundet ergeben 1 bis 4 den Wert 0, und 95 bis 100 den Wert 100 (95 wird zu 100). Nur dort stimmen beide Rundungen überein: 1, 2, 3, 4 und 95, 96, 97, 98, 99, 100, das sind 4 + 6 = 10 Zahlen.',
      'Zwei Rundungen auf verschiedene Stellen werden für einen ganzen Zahlenbereich verglichen; die Übungen runden einzelne Zahlen oder zählen die Zahlen zu einem Rundungsergebnis.')
    Z(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Eine natürliche Zahl wird auf Hunderter gerundet. Um wie viel kann die gerundete Zahl höchstens von der ursprünglichen Zahl abweichen?',
      50, '100 : 2',
      [(49, '50 − 1', 'den Fall 4 950, der nach 5 000 aufrundet, übersehen'),
       (100, '100', 'die ganze Stufe 100 als größte Abweichung genommen'),
       (99, '100 − 1', 'die Zahl direkt unter der nächsten Stufe als Abweichung genommen')],
      'Beim Runden auf Hunderter liegt jede Zahl höchstens bis zur Mitte (50) von der gerundeten Zahl entfernt. 4 950 wird zu 5 000 aufgerundet, Abweichung 50. 4 949 wird zu 4 900 abgerundet, Abweichung 49. Größer als 50 geht nicht.',
      'Der größtmögliche Rundungsfehler wird über die Grenzfälle der Regel bestimmt; die Übungen runden einzelne Zahlen.')
    L(lz, 'korrektur', 'fehler', 'fehler_detektiv', 2, LP,
      'Jonas rundet 4 949 auf Hunderter. Zeile 1: Zum Runden auf Hunderter schaut man auf die Zehnerstelle. Zeile 2: Die Zehnerstelle ist 4, das ist kleiner als 5, also wird aufgerundet. Zeile 3: Aufgerundet ergibt 4 949 gerundet 5 000. In welcher Zeile steckt der erste Fehler, und wie lautet die richtig gerundete Zahl?',
      'Fehler in Zeile □, richtig gerundet: □', [2, 4900], ['2', '4900'],
      [(2, 5000, '5000', 'wie Jonas aufgerundet'),
       (2, 4950, '4950', 'auf Zehner statt auf Hunderter gerundet'),
       (2, 4940, '4940', 'auf Zehner abgerundet statt auf Hunderter gerundet'),
       (1, 1, '1', 'Zeile 1 für falsch gehalten, obwohl man auf die Zehnerstelle schaut')],
      'Zeile 1 stimmt. In Zeile 2: Eine Ziffer kleiner als 5 bedeutet abrunden. Die Zehnerstelle 4 gibt abrunden: 4 949 ≈ 4 900.',
      'Fehler-Detektiv beim Entscheidungsschritt der Rundungsregel (Aufrunden bei Ziffer < 5); die Übungen runden direkt.')
    A(lz, 'sicherung', 'begruenden', None, 2, LP,
      'Eine natürliche Zahl wird auf Zehntausender gerundet. Kann die gerundete Zahl größer als die ursprüngliche Zahl sein, kleiner als sie oder gleich groß? Welche Aussage stimmt?',
      ['Sie ist immer größer, denn gerundete Zahlen sind „voller“ als die ursprüngliche Zahl.',
       'Jeder der drei Fälle kommt vor, denn entscheidend sind die Stellen hinter der Zehntausenderstelle.',
       'Sie ist kleiner oder gleich, denn beim Runden werden hinten Stellen einfach weggeschnitten.',
       'Sie ist größer oder kleiner, denn eine gerundete Zahl ist stets eine andere Zahl als die Zahl vorher.'], 1,
      {0: 'Wird abgerundet, ist die gerundete Zahl kleiner: 64 000 wird zu 60 000.',
       2: 'Wird aufgerundet, ist die gerundete Zahl größer: 66 000 wird zu 70 000.',
       3: 'Liegt die Zahl schon auf einem Zehntausender, bleibt sie gleich: 60 000 bleibt 60 000.'},
      'Beispiele: 64 000 wird zu 60 000 (kleiner), 66 000 wird zu 70 000 (größer), 60 000 bleibt 60 000 (gleich). Ob auf- oder abgerundet wird, entscheidet die erste Stelle hinter der Zehntausenderstelle; gleich bleibt die Zahl nur, wenn alle Stellen dahinter 0 sind.',
      '„Immer, manchmal, nie“ mit Gegenbeispielen für alle drei Fälle; die Übungen runden eine Zahl.')
    A(lz, 'sicherung', 'begruenden', None, 3, LP,
      'Zwei natürliche Zahlen a und b mit a < b werden beide auf Hunderter gerundet. Welche Aussage über die gerundeten Zahlen stimmt?',
      ['Die gerundete Zahl von a ist nie größer als die von b und kann gleich sein, denn die Rundungsbereiche liegen in derselben Reihenfolge.',
       'Die gerundete Zahl von a ist stets kleiner als die von b, denn aus a < b folgt auch gerundet a < b.',
       'Die gerundete Zahl von a kann größer sein als die von b, denn beim Aufrunden springt a nach oben und b nicht.',
       'Die gerundeten Zahlen sind nur dann gleich, wenn a = b ist, denn verschiedene Zahlen haben verschiedene Rundungen.'], 0,
      {1: 'Nahe beieinander liegende Zahlen werden oft gleich gerundet: 4 760 und 4 770 ergeben beide 4 800.',
       2: 'a kann b nicht überholen: Aus 4 849 → 4 800 und 4 850 → 4 900 sieht man, dass die kleinere Zahl höchstens denselben Wert bekommt.',
       3: 'Verschiedene Zahlen können denselben Rundungswert haben: 4 760 und 4 770 ergeben beide 4 800.'},
      'Beim Runden auf Hunderter gehört jede Zahl zu einem Bereich, zum Beispiel 4 750 bis 4 849 zu 4 800. Die Bereiche liegen in derselben Reihenfolge wie die Zahlen. Ist a < b, liegt a im selben oder in einem früheren Bereich als b, also ist gerundet a höchstens so groß wie gerundet b. Beispiel: 4 760 und 4 770 ergeben beide 4 800.',
      'Eine Eigenschaft des Rundens (Reihenfolge bleibt erhalten, Gleichheit ist möglich) wird begründet; die Übungen runden einzelne Zahlen.')

    # ---------------- runden_sinnvoll ----------------
    lz = 'runden_sinnvoll'
    L(lz, 'test', 'transfer', 'anwenden', 3, LP,
      'Ein Schlauch ist auf Zehner gerundet 30 m lang (die Länge ist eine ganze Zahl in Metern). Er wird in Stücke zu je 3 m zerschnitten; ein Rest, der kürzer als 3 m ist, wird nicht gezählt. Wie viele Stücke sind mindestens und höchstens möglich?',
      'mindestens □ Stücke, höchstens □ Stücke', [8, 11], ['(25 − 1) : 3', '(34 − 1) : 3'],
      [(1, 10, '30 : 3', 'mit der gerundeten Länge 30 m gerechnet'),
       (1, 9, '27 : 3', 'als kleinste Länge 27 m angesetzt'),
       (2, 10, '30 : 3', 'mit der gerundeten Länge 30 m gerechnet'),
       (2, 12, '36 : 3', 'als größte Länge 36 m angesetzt')],
      'Auf Zehner gerundet 30 m heißt: von 25 m bis 34 m. Bei 25 m gibt es 25 : 3 = 8 Stücke (Rest 1 m), bei 34 m gibt es 34 : 3 = 11 Stücke (Rest 1 m). Zwischen 8 und 11 Stücke sind möglich, nicht genau 10.',
      'Ein Rundungsbereich wird durch eine Zahl geteilt, wobei der Rest wegfällt; die Übungen runden Summen und Produkte.')
    L(lz, 'korrektur', 'transfer', 'anwenden', 2, LP,
      'Beide Aufgaben beruhen auf derselben Rechnung 1 000 : 36 = 27 Rest 28. Aufgabe A: Ein Verein hat 1 000 € und kauft Trikots zu je 36 €. Wie viele Trikots kann er höchstens kaufen? Aufgabe B: 1 000 Kinder bekommen je eine Flasche, die es nur in Kisten zu je 36 Stück gibt. Wie viele Kisten muss man mindestens kaufen?',
      'Aufgabe A: □ Trikots; Aufgabe B: □ Kisten', [27, 28], ['27', '28'],
      [(1, 28, '28', 'bei A aufgerundet, obwohl 28 Trikots 1 008 € kosten'),
       (2, 27, '27', 'bei B abgerundet; dann fehlen 28 Flaschen'),
       (1, 36, '36', 'den Preis eines Trikots als Anzahl angegeben'),
       (2, 36, '36', 'die Größe einer Kiste als Anzahl der Kisten angegeben')],
      '1 000 : 36 = 27 Rest 28. A: Man kann nur ganze Trikots kaufen; 27 Trikots kosten 972 €, 28 wären mit 1 008 € zu teuer, also bleibt es bei 27. B: 27 Kisten haben nur 972 Flaschen, für die übrigen 28 Kinder braucht man noch eine Kiste, also 28 Kisten.',
      'Dieselbe Rechnung führt je nach Sachzusammenhang zu Abrunden oder Aufrunden; die Übungen runden nach der Regel oder kennen nur eine der beiden Richtungen.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Ein Marathon hatte 22 817 Läufer. Eine Zeitung schreibt „rund 23 000 Läufer“, eine andere „rund 20 000 Läufer“. Welche Aussage stimmt?',
      ['Beide Angaben sind falsch, denn eine Läuferzahl wie 22 817 darf man nie runden.',
       'Beide sind richtig gerundet, denn jede Angabe ist auf ihre Stelle gerundet, die erste ist nur genauer.',
       'Nur die erste ist richtig, denn man muss immer auf Tausender runden, auch bei kleineren Zahlen.',
       'Nur die zweite ist richtig, denn 20 000 ist eine rundere Zahl und deshalb besser zu merken.'], 1,
      {0: 'Bei einer Läuferzahl kommt es nicht auf die genaue Zahl an; Runden ist sinnvoll.',
       2: 'Es gibt keine feste Rundungsstelle; sie hängt von der gewünschten Genauigkeit ab.',
       3: '20 000 ist nicht richtiger, sondern gröber gerundet und weicht um fast 3 000 vom genauen Wert ab.'},
      '22 817 auf Tausender: Hunderterstelle 8, also aufrunden: 23 000. Auf Zehntausender: Tausenderstelle 2, also abrunden: 20 000. Beide Angaben sind richtig gerundet, die erste weicht weniger ab.',
      'Zwei Rundungsstellen werden mit der Genauigkeit begründet verglichen; die Übungen runden nach Vorgabe.')
    L(lz, 'sicherung', 'transfer', None, 3, LP,
      'In einem Saal gibt es 48 Reihen mit je 29 Plätzen. Anna schätzt die Platzzahl mit 50 · 30, Ben mit 48 · 30. Um wie viel liegt jede der beiden Schätzungen über der genauen Platzzahl?',
      'Annas Schätzung liegt □ darüber, Bens Schätzung liegt □ darüber', [108, 48], ['50 · 30 − 48 · 29', '48 · 30 − 48 · 29'],
      [(1, 60, '50 · 30 − 48 · 30', 'nur den Unterschied zu Bens Schätzung angegeben'),
       (1, 1500, '50 · 30', 'die Schätzung selbst statt der Abweichung angegeben'),
       (2, 1, '30 − 29', 'nur den Fehler je Reihe (1 Platz) angegeben'),
       (2, 1440, '48 · 30', 'die Schätzung selbst statt der Abweichung angegeben')],
      'Genau: 48 · 29 = 1 392 Plätze. Anna: 50 · 30 = 1 500, das sind 108 zu viel. Ben: 48 · 30 = 1 440, das sind 48 zu viel (1 Platz zu viel je Reihe). Wer beide Faktoren aufrundet, verstärkt den Fehler.',
      'Die Übungen runden eine Zahl oder eine Summe; hier wird beim Produkt gerundet, und der Fehler wächst, wenn beide Faktoren aufgerundet werden.')
    A(lz, 'sicherung', 'begruenden', None, 3, LP,
      'Mia rundet die vier Zahlen 3 460, 3 420, 3 440 und 3 470 jeweils auf Tausender und addiert die gerundeten Zahlen: 12 000. Die genaue Summe ist 13 790. Wie erklärt man den großen Unterschied?',
      ['Mia hätte zuerst genau addieren und erst danach die Summe runden müssen, denn dann kommt genau die richtige Summe heraus.',
       'Jede Zahl wurde um 420 bis 470 abgerundet, denn alle vier Fehler gehen in dieselbe Richtung und addieren sich zu 1 790.',
       'Runden auf Tausender ist immer falsch, denn beim Addieren mehrerer Zahlen wird jede Rundung zum Fehler.',
       'Der Unterschied kommt daher, dass man die Zahlen hätte aufrunden müssen, weil 13 790 größer ist.'], 1,
      {0: 'Auch die gerundete genaue Summe (14 000) weicht von 13 790 ab; Mias 12 000 ist richtig gerechnet, nur sind ihre Rundungsfehler groß.',
       2: 'Runden zum Schätzen ist erlaubt; man muss nur wissen, wie genau das Ergebnis dann ist.',
       3: 'Die Zahlen werden nach der Regel gerundet: Hunderterstelle 4, also abrunden.'},
      'Jede Zahl hat die Hunderterstelle 4 und wird abgerundet: Die Rundungsfehler sind 460, 420, 440 und 470. Weil sie alle in dieselbe Richtung gehen, addieren sie sich: 460 + 420 + 440 + 470 = 1 790 = 13 790 − 12 000.',
      'Wirkung vieler gleichgerichteter Rundungsfehler; die Übungen runden einzelne Zahlen oder vergleichen nur zwei Rechenwege.')

    # ---------------- roemisch_schreiben ----------------
    lz = 'roemisch_schreiben'
    L(lz, 'test', 'darstellung', None, 3, LP,
      'Eine Zahl kann man römisch auf zwei Arten schreiben. Art 1 (nur addieren): Die Zeichen I = 1, V = 5, X = 10, L = 50 und C = 100 stehen der Größe nach, ihre Werte werden addiert, ein Zeichen darf beliebig oft hintereinander stehen, und man nimmt möglichst wenige Zeichen (also V statt IIIII und L statt XXXXX). '
      'Art 2 (übliche Regeln): Ein Zeichen steht höchstens dreimal hintereinander; ein kleineres Zeichen links von einem größeren wird abgezogen, aber nur I vor V oder X und X vor L oder C. '
      'Bei welcher Zahl von 1 bis 90 spart Art 2 gegenüber Art 1 die meisten Zeichen, und wie viele Zeichen spart sie dort?',
      'Zahl □; gespart werden □ Zeichen', [49, 5], ['49', '9 − 4'],
      [(1, 90, '90', 'die größte erlaubte Zahl genommen; 90 spart nur 3 Zeichen (LXXXX gegen XC)'),
       (1, 44, '44', 'nur auf die Vieren geachtet; 44 spart 4 Zeichen (XXXXIIII gegen XLIV)'),
       (1, 9, '9', 'nur die Einerstelle betrachtet; 9 spart 3 Zeichen (VIIII gegen IX)'),
       (2, 3, '5 − 2', 'bei 49 nur die Ersparnis bei der 9 (VIIII gegen IX) gezählt, die bei der 40 vergessen'),
       (2, 2, '4 − 2', 'bei 49 nur die Ersparnis bei der 40 (XXXX gegen XL) gezählt')],
      'Beide Arten schreiben Zehner und Einer getrennt hintereinander. Unterschiede gibt es nur bei den Ziffern 4 und 9: Bei einer 4 spart Art 2 zwei Zeichen (IIII → IV, XXXX → XL), bei einer 9 drei Zeichen (VIIII → IX, LXXXX → XC), '
      'bei allen anderen Ziffern nichts. Bis 90 spart man am meisten mit der Zehnerziffer 4 und der Einerziffer 9: 49. Art 1: XXXXVIIII (9 Zeichen), Art 2: XLIX (4 Zeichen), gespart 5. Bei 90 sind es nur 3, bei 44 nur 4.',
      'Die Übungen schreiben Zahlen nach den üblichen Regeln; hier werden zwei Schreibweisen über einen ganzen Zahlenbereich verglichen, um zu sehen, wo die Subtraktionsregel am meisten spart.')
    A(lz, 'korrektur', 'darstellung', None, 2, LP,
      'Es gelten die Regeln: Ein Zeichen steht höchstens dreimal hintereinander. Ein kleineres Zeichen links von einem größeren wird abgezogen, aber nur I vor V oder X, X vor L oder C und C vor D oder M. Welche der vier römischen Zahlen ist nicht regelgerecht geschrieben?',
      ['XLIV', 'CDXC', 'VC', 'MCMXC'], 2,
      {0: 'XLIV = 40 + 4 = 44 ist regelgerecht (XL und IV).',
       1: 'CDXC = 400 + 90 = 490 ist regelgerecht (CD und XC).',
       3: 'MCMXC = 1 000 + 900 + 90 = 1 990 ist regelgerecht (M, CM, XC).'},
      'V darf nicht vor C stehen, denn vor einem größeren Zeichen darf nur I, X oder C stehen, und V gehört nicht dazu. 95 schreibt man XCV. Die anderen drei Zahlen halten die Regeln ein.',
      'Regelgerechtheit statt Umwandlung; die Übungen schreiben eine Zahl um.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Im Zehnersystem gilt: Eine Zahl mit mehr Ziffern ist größer als eine Zahl mit weniger Ziffern. Gilt bei römischen Zahlen (nach den üblichen Regeln geschrieben) entsprechend: Eine römische Zahl mit mehr Zeichen ist größer als eine mit weniger Zeichen?',
      ['Es stimmt nur manchmal, denn XII ist mit drei Zeichen größer als X, VIII mit vier Zeichen dagegen kleiner als L.',
       'Es stimmt immer, denn wie im Zehnersystem macht jedes weitere Zeichen die Zahl größer.',
       'Es stimmt nie, denn große Zahlen schreibt man römisch mit wenigen großen Zeichen, kleinere mit vielen.',
       'Es stimmt nur bei Zahlen ohne Subtraktionsregel, denn erst Paare wie IV oder IX bringen die Länge durcheinander.'], 0,
      {1: 'Römische Zeichen haben verschieden große Werte: Das eine Zeichen L (50) ist mehr als VIII (8) mit vier Zeichen.',
       2: 'Mehr Zeichen können auch mehr bedeuten: XII (12) hat mehr Zeichen als X (10) und ist größer.',
       3: 'Auch ohne Subtraktionsregel gilt es nicht: VIII (8) hat mehr Zeichen als L (50), ganz ohne abgezogenes Zeichen.'},
      'Im Zehnersystem hat jede Ziffer ihren Platz, deshalb bedeutet eine Stelle mehr eine größere Zahl. Römische Zeichen haben feste, aber verschieden große Werte: Ein einziges großes Zeichen kann mehr wert sein als viele kleine. '
      'Gegenbeispiel: VIII (4 Zeichen) = 8 ist kleiner als L (1 Zeichen) = 50. Beispiel, wo es stimmt: XII (3 Zeichen) = 12 ist größer als X = 10. Die Aussage stimmt also nur manchmal.',
      'Die Übungen schreiben einzelne Zahlen; hier wird die römische Schrift mit dem Stellenwertsystem verglichen (die Länge sagt nichts über die Größe).')
    Z(lz, 'sicherung', 'transfer', None, 2, LP,
      'Römische Zahlen werden so geschrieben: zuerst die Tausender, dann die Hunderter, die Zehner und die Einer, jede Stufe für sich (zum Beispiel 2 024 = MM + XX + IV = MMXXIV). Für die Tausender gibt es nur das Zeichen M, ein Zeichen darf höchstens dreimal hintereinander stehen, und es gibt kein Zeichen, das mehr als 1 000 wert ist. Welches ist die größte Zahl, die man so schreiben kann?',
      3999, '3000 + 900 + 90 + 9',
      [(3000, '1000 + 1000 + 1000', 'nur die drei M gezählt und die Hunderter, Zehner und Einer vergessen'),
       (3888, '3000 + 800 + 80 + 8', 'die längste Schreibweise MMMDCCCLXXXVIII mit der größten Zahl verwechselt'),
       (4999, '4000 + 900 + 90 + 9', 'vier M zugelassen, obwohl ein Zeichen höchstens dreimal hintereinander stehen darf'),
       (3333, '3000 + 300 + 30 + 3', 'in jeder Stufe dreimal dasselbe Zeichen genommen')],
      'Für die Tausender gibt es nur M, und M darf höchstens dreimal stehen: MMM = 3 000. Mehr Tausender lassen sich nicht schreiben, weil es kein größeres Zeichen gibt. Dahinter kommen die größten Hunderter, Zehner und Einer: CM = 900, XC = 90, IX = 9. '
      'Die größte Zahl ist MMMCMXCIX = 3 999; schon 4 000 bräuchte vier M.',
      'Die Übungen schreiben einzelne Zahlen; hier wird aus den Regeln erschlossen, wo die römische Schrift an ihre Grenze kommt.')
    Z(lz, 'sicherung', 'parameter', None, 3, LP,
      'Römische Zahlen werden nach den üblichen Regeln geschrieben: Ein Zeichen steht höchstens dreimal hintereinander, und ein kleineres Zeichen vor einem größeren wird abgezogen, aber nur I vor V oder X und X vor L oder C (zum Beispiel 4 = IV, 9 = IX, 19 = XIX). Wie heißt die kleinste natürliche Zahl, deren römische Schreibweise aus genau sechs Zeichen besteht?',
      28, '28',
      [(18, '18', 'XVIII für sechsstellig gehalten; es sind nur fünf Zeichen'),
       (38, '38', 'XXXVIII genommen; das hat schon sieben Zeichen, und XXVIII ist kleiner'),
       (23, '23', 'XXIII für sechsstellig gehalten; es sind nur fünf Zeichen')],
      'Bis 17 hat keine Zahl mehr als vier Zeichen (VIII, XIII, XVII). 18 = XVIII hat fünf, 23 = XXIII und 27 = XXVII haben fünf. 28 = XXVIII hat genau sechs Zeichen, und keine kleinere Zahl hat sechs.',
      'Die Zeichenzahl wird über viele Zahlen hinweg gesucht; die Übungen schreiben eine einzelne Zahl.')

    # ---------------- dualsystem ----------------
    lz = 'dualsystem'
    Z(lz, 'test', 'transfer', None, 3, LP,
      'Mia rechnet Zweierzahlen ins Zehnersystem um, ordnet die Stellenwerte 1, 2, 4, 8, 16 aber von links nach rechts zu statt von rechts nach links. Aus 110 macht sie so 1 · 1 + 1 · 2 + 0 · 4 = 3 statt 6. Betrachtet werden alle Zweierzahlen mit höchstens fünf Ziffern, die mit einer 1 beginnen (das sind die Zahlen 1 bis 31). Bei wie vielen davon bekommt Mia trotzdem den richtigen Wert?',
      10, '1 + 1 + 2 + 2 + 4',
      [(16, '32 − 16', 'alle Zahlen gezählt, die auf 1 enden; es müssen aber alle Ziffern von vorn und von hinten gelesen übereinstimmen'),
       (5, '5', 'nur die Zahlen aus lauter Einsen gezählt (1, 11, 111, 1111, 11111)'),
       (31, '31', 'gemeint, die Richtung der Stellenwerte sei egal'),
       (6, '1 + 1 + 2 + 2', 'die fünfstelligen Zahlen 10001, 10101, 11011 und 11111 vergessen')],
      'Mia bekommt den richtigen Wert genau dann, wenn die Zahl von hinten gelesen dieselbe Zweierzahl ist wie von vorn (Spiegelzahl). Endet die Zahl auf 0, beginnt sie von hinten gelesen mit 0 und ist bei Mia kleiner. '
      'Endet sie auf 1, haben beide Lesarten gleich viele Stellen, und gleich groß sind sie nur, wenn alle Ziffern übereinstimmen. Spiegelzahlen: 1; 11; 101, 111; 1001, 1111; 10001, 10101, 11011, 11111. Das sind 1 + 1 + 2 + 2 + 4 = 10.',
      'Die Übungen rechnen einzelne Zweierzahlen um; hier wird untersucht, wann eine falsche Zuordnung der Stellenwerte zufällig das Richtige liefert.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Welche Aussage über die Zweierzahlen 0111 und 111 stimmt?',
      ['0111 ist größer, denn sie hat vier Stellen und 111 nur drei.',
       'Beide sind gleich groß, denn eine Null vorn ändert den Wert nicht.',
       '0111 ist kleiner, denn eine Null vorn macht die Zahl nicht gleich groß, sondern kleiner.',
       '111 ist größer, denn die Null vorn ist ein Platzhalter für den Wert 8.'], 1,
      {0: 'Eine Zweierzahl ist nicht größer, nur weil sie mehr Ziffern hat; führende Nullen tragen nichts bei.',
       2: 'Die Null vorn steht an der Achterstelle und zählt 0 · 8 = 0; sie ändert nichts.',
       3: 'Die Null an der Achterstelle liefert 0 · 8 = 0, nicht 8.'},
      '0111 = 0 · 8 + 1 · 4 + 1 · 2 + 1 · 1 = 7 und 111 = 4 + 2 + 1 = 7. Eine führende Null liefert 0 und ändert den Wert nicht, wie im Zehnersystem 007 = 7.',
      'Führende Nullen bei Zweierzahlen; die Übungen wandeln Zahl für Zahl um.')
    Z(lz, 'korrektur', 'parameter', None, 2, LP,
      'Eine Zweierzahl hat sieben Ziffern, beginnt mit 1 und endet mit 0. Man vertauscht ihre erste und ihre letzte Ziffer; die Ziffern dazwischen bleiben stehen. Um wie viel wird der Wert der Zahl dadurch kleiner?',
      63, '64 − 1',
      [(64, '64', 'nur gesehen, dass die vordere 1 (Wert 64) wegfällt, die neue 1 an der Einerstelle aber nicht dazugezählt'),
       (999999, '1000000 − 1', 'die Stellen wie im Zehnersystem bewertet'),
       (127, '64 + 32 + 16 + 8 + 4 + 2 + 1', 'den größtmöglichen Wert einer siebenstelligen Zweierzahl angegeben'),
       (62, '64 − 2', 'der letzten Stelle den Wert 2 statt 1 gegeben')],
      'Von rechts haben die Stellen die Werte 1, 2, 4, 8, 16, 32, 64. Die erste Ziffer steht an der Stelle mit dem Wert 64, die letzte an der Stelle mit dem Wert 1. Nach dem Tausch steht an der 64er-Stelle eine 0 und an der Einerstelle eine 1: '
      '64 fallen weg, 1 kommt dazu. Die Ziffern dazwischen ändern nichts. Die Zahl wird um 64 − 1 = 63 kleiner, ganz gleich, wie die mittleren Ziffern lauten.',
      'Die Übungen wandeln eine gegebene Zahl um; hier ist die Zahl nicht bekannt, und man muss sehen, dass die Änderung nur von den beiden getauschten Stellen abhängt.')
    A(lz, 'sicherung', 'darstellung', None, 3, LP,
      'Eine Zweierzahl mit mindestens drei Ziffern endet auf 00. Welche Aussage über die Zahl im Zehnersystem folgt daraus sicher?',
      ['Sie lässt sich ohne Rest durch 4 teilen, denn alle Stellenwerte außer 1 und 2 sind Vielfache von 4.',
       'Sie endet auch im Zehnersystem auf 00, denn zwei Endnullen bedeuten in jedem Zahlsystem genau dasselbe.',
       'Sie ist eine Zweierpotenz wie 4, 8 oder 16, denn hinter ihren vorderen Ziffern stehen nur Nullen.',
       'Es folgt nichts Sicheres, denn wie groß die Zahl ist, hängt allein von ihren vorderen Ziffern ab.'], 0,
      {1: 'Im Zweiersystem bedeutet eine Endnull „verdoppelt“, nicht „mal 10“: 100 ist 4, 1100 ist 12.',
       2: 'Nur Zweierzahlen mit genau einer 1 sind Zweierpotenzen; 1100 = 12 endet auch auf 00.',
       3: 'Die vorderen Ziffern bestimmen die Größe, aber jede von ihnen steht an einer Stelle mit dem Wert 4, 8, 16, …; deshalb ist die Zahl durch 4 teilbar.'},
      'Von rechts haben die Stellen die Werte 1, 2, 4, 8, 16, … Endet die Zahl auf 00, tragen die Stellen 1 und 2 nichts bei. Alle anderen Stellenwerte (4, 8, 16, 32, …) lassen sich ohne Rest durch 4 teilen, also auch ihre Summe. Beispiele: 100 = 4, 1100 = 12, 10100 = 20.',
      'Die Übungen wandeln einzelne Zahlen um; hier wird aus den Endziffern im Zweiersystem auf eine Eigenschaft im Zehnersystem geschlossen.')
    L(lz, 'sicherung', 'darstellung', None, 2, LP,
      'Eine natürliche Zahl hat im Zweiersystem genau zehn Ziffern (die erste ist eine 1). Wie viele Ziffern kann sie im Zehnersystem mindestens und wie viele höchstens haben?',
      'mindestens □ Ziffern, höchstens □ Ziffern', [3, 4], ['3', '4'],
      [(1, 4, '4', 'nur an die größte zehnstellige Zweierzahl 1111111111 = 1 023 gedacht'),
       (1, 512, '512', 'die kleinste Zahl selbst statt ihrer Ziffernzahl angegeben'),
       (2, 3, '3', 'nur an die kleinste zehnstellige Zweierzahl 1000000000 = 512 gedacht'),
       (2, 10, '10', 'gemeint, die Zahl habe in beiden Systemen gleich viele Ziffern')],
      'Die kleinste Zweierzahl mit zehn Ziffern ist 1000000000; ihre 1 steht an der Stelle mit dem Wert 512 (1, 2, 4, …, 256, 512). Die größte ist 1111111111 = 1 023, eins weniger als 1 024. '
      'Alle Zahlen von 512 bis 1 023 haben im Zweiersystem zehn Ziffern. Im Zehnersystem haben sie 3 Ziffern (512 bis 999) oder 4 Ziffern (1 000 bis 1 023).',
      'Die Übungen bestimmen die Stellenzahl einer einzelnen Zahl; hier wird eine Stellenzahl im Zweiersystem über den Wertebereich in eine Stellenzahl im Zehnersystem übersetzt.')
