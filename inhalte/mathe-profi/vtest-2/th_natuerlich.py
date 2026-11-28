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
    Z(lz, 'sicherung', 'umkehr', None, 2, LP,
      'Dieselben zwei Zahlen sind auf zwei Zahlenstrahlen A und B mit gleichmäßiger Skala eingetragen. Auf A liegen ihre Marken 6 cm auseinander, auf B nur 4 cm. Auf A steht 1 cm für 50. Für welche Zahl steht 1 cm auf B?',
      75, '6 · 50 : 4',
      [(50, '50', 'gemeint, 1 cm stehe auf beiden Strahlen für dieselbe Zahl'),
       (300, '6 · 50', 'den Unterschied der beiden Zahlen statt des Werts je cm angegeben'),
       (200, '4 · 50', 'die 4 cm von B mit dem Maßstab von A malgenommen'),
       (100, '50 · (6 − 4)', 'mit dem Unterschied der beiden cm-Angaben malgenommen')],
      'Die beiden Zahlen sind auf beiden Strahlen dieselben, also auch ihr Unterschied. Auf A sind es 6 cm zu je 50, der Unterschied ist 6 · 50 = 300. Auf B verteilen sich dieselben 300 auf nur 4 cm: 300 : 4 = 75. '
      'Weniger cm für denselben Unterschied heißt: Jeder cm steht für mehr.',
      'Die Übungen bestimmen den Wert eines Abschnitts aus Anfang und Ende eines Strahls; hier sind die Zahlen unbekannt, und man muss erkennen, dass ihr Unterschied auf beiden Strahlen derselbe ist.')
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
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Ein Zahlenstrahl beginnt bei 0, seine Striche haben den Abstand 10. Lena trägt eine Zahl, die auf einem Strich liegt (nicht die 0), so ein: Sie teilt die Zahl durch 10 und zählt so viele Striche ab, wobei sie den Strich bei 0 als ersten Strich mitzählt. Welche Aussage über Lenas Marken stimmt?',
      ['Jede ihrer Marken liegt genau 10 zu weit links, denn Lena zählt immer einen Abstand zu wenig.',
       'Ihre Marken liegen richtig, denn sie zählt genau so viele Striche, wie die Zahl Zehner hat.',
       'Je größer die Zahl ist, desto weiter liegt ihre Marke daneben, denn der Fehler wächst mit jedem Strich.',
       'Jede ihrer Marken liegt genau 10 zu weit rechts, denn der Strich bei 0 zählt bei ihr schon als Zehner.'], 0,
      {1: 'Gezählt werden müssen die Abstände, nicht die Striche: Für 30 zählt Lena die Striche bei 0, 10 und 20 und landet bei 20.',
       2: 'Lena zählt bei jeder Zahl genau einen Abstand zu wenig; der Fehler ist immer derselbe, nämlich 10.',
       3: 'Weil der Strich bei 0 schon mitgezählt wird, landet Lena einen Strich zu früh, also links von der richtigen Stelle.'},
      'Zur Zahl 30 gehören 3 Abstände von 0 aus, also der Strich bei 30. Lena zählt Striche und beginnt beim Strich 0: 0, 10, 20 – sie landet bei 20. '
      'Weil sie bei jeder Zahl den Strich bei 0 mitzählt, fehlt ihr immer genau ein Abstand: Jede Marke liegt 10 zu weit links.',
      'Die Übungen zählen Abschnitte bei einer einzelnen Zahl; hier wird die Folge einer falschen Zählregel für alle Zahlen beurteilt.')
    Z(lz, 'test', 'transfer', None, 3, LP,
      'Anna teilt den Zahlenstrahl von 0 bis 12 000 in 60 gleich große Abschnitte, Ben teilt ihn in 80 gleich große Abschnitte. Wie viele Zahlen zwischen 0 und 12 000 (ohne 0 und 12 000) liegen bei beiden auf einem Teilstrich?',
      19, '12000 : 600 − 1',
      [(1, '1', 'nur die erste gemeinsame Zahl 600 gezählt'),
       (20, '12000 : 600', 'die 12 000 mitgezählt, obwohl sie ausgeschlossen ist'),
       (138, '59 + 79', 'die Teilstriche beider Strahlen addiert'),
       (59, '60 − 1', 'nur die Teilstriche auf Annas Strahl gezählt')],
      'Annas Abschnitte sind 12 000 : 60 = 200 lang, Bens 12 000 : 80 = 150. Zum ersten Mal treffen sich die Striche bei 600 (3 · 200 = 4 · 150), danach immer wieder nach 600: 600, 1 200, …, 11 400. '
      'Das sind 12 000 : 600 − 1 = 19 Zahlen (die 12 000 selbst zählt nicht).',
      'Die Übungen tragen Zahlen auf einer Skala ein; hier werden zwei Teilungen desselben Strahls verglichen, und man muss den Abstand der gemeinsamen Striche erkennen, weil Auflisten zu lang wäre.')
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
      'Für wie viele natürliche Zahlen von 1 bis 100 ergibt das Runden auf Zehner dieselbe Zahl wie das Runden auf Hunderter? (Auch 0 kann als Ergebnis des Rundens herauskommen.)',
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
       'Alle drei Fälle kommen vor, aber nur bei Zahlen über 100 000, denn kleinere werden stets auf 0 gerundet.'], 1,
      {0: 'Wird abgerundet, ist die gerundete Zahl kleiner: 64 000 wird zu 60 000.',
       2: 'Wird aufgerundet, ist die gerundete Zahl größer: 66 000 wird zu 70 000.',
       3: 'Auch kleine Zahlen zeigen alle drei Fälle: 3 000 wird zu 0, 6 000 zu 10 000, und 10 000 bleibt 10 000.'},
      'Beispiele: 64 000 wird zu 60 000 (kleiner), 66 000 wird zu 70 000 (größer), 60 000 bleibt 60 000 (gleich); ebenso bei kleinen Zahlen: 3 000 → 0, 6 000 → 10 000, 10 000 → 10 000. Ob auf- oder abgerundet wird, entscheidet die erste Stelle hinter der Zehntausenderstelle; gleich bleibt die Zahl nur, wenn alle Stellen dahinter 0 sind.',
      '„Immer, manchmal, nie“ mit Gegenbeispielen für alle drei Fälle; die Übungen runden eine Zahl.')
    A(lz, 'sicherung', 'begruenden', None, 3, LP,
      'Zwei natürliche Zahlen a und b mit a < b werden beide auf Hunderter gerundet. Welche Aussage über die gerundeten Zahlen stimmt?',
      ['Die gerundete Zahl von a ist nie größer als die von b und manchmal gleich, denn die Bereiche liegen in derselben Reihenfolge.',
       'Die gerundete Zahl von a ist stets kleiner als die von b, denn aus a < b folgt auch gerundet a < b.',
       'Die gerundete Zahl von a kann größer sein als die von b und ist nie gleich, denn beim Aufrunden springt a nach oben und b nicht.',
       'Die gerundeten Zahlen sind nur dann gleich, wenn a = b ist, denn verschiedene Zahlen haben verschiedene Rundungen.'], 0,
      {1: 'Nahe beieinander liegende Zahlen werden oft gleich gerundet: 4 760 und 4 770 ergeben beide 4 800.',
       2: 'a kann b nicht überholen (aus 4 849 → 4 800 und 4 850 → 4 900 sieht man, dass die kleinere Zahl höchstens denselben Wert bekommt), und gleich ist möglich: 4 760 und 4 770 ergeben beide 4 800.',
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
    A(lz, 'sicherung', 'begruenden', None, 3, LP,
      'Lea und Tom schätzen das Produkt zweier Zahlen, von denen keine eine Zehnerzahl ist, und runden dazu beide Faktoren auf Zehner. Lea rundet beide Faktoren auf. Tom rundet einen Faktor auf und den anderen ab. Was kann man über die beiden Schätzungen sagen, ohne die Zahlen zu kennen?',
      ['Leas Schätzung ist zu groß, denn beide Faktoren wachsen; ob Toms zu groß oder zu klein ist, lässt sich nicht sagen.',
       'Beide Schätzungen sind zu groß, denn beim Runden kommt bei jedem Faktor etwas dazu, und das wirkt auf das ganze Produkt.',
       'Toms Schätzung ist genau richtig, denn sein Auf- und Abrunden gleichen sich im Produkt aus, Leas dagegen nicht.',
       'Leas Schätzung ist zu groß und Toms Schätzung zu klein, denn Tom rundet einen der beiden Faktoren ab.'], 0,
      {1: 'Beim Abrunden wird ein Faktor kleiner; Toms Schätzung kann deshalb auch zu klein sein: 12 · 19 = 228, geschätzt 10 · 20 = 200.',
       2: 'Auf- und Abrunden gleichen sich im Produkt nicht aus: 12 · 19 = 228, aber 10 · 20 = 200.',
       3: 'Toms Schätzung kann auch zu groß sein: 18 · 11 = 198, geschätzt 20 · 10 = 200.'},
      'Lea macht beide Faktoren größer, also wird auch das Produkt größer: Ihre Schätzung ist sicher zu groß. Bei Tom wird ein Faktor größer und der andere kleiner. Je nach Zahlen überwiegt das eine oder das andere: '
      '12 · 19 = 228 wird zu 10 · 20 = 200 (zu klein), 18 · 11 = 198 wird zu 20 · 10 = 200 (zu groß). Ohne die Zahlen lässt sich bei Tom also nichts sagen.',
      'Die Übungen rechnen eine Schätzung aus; hier wird ohne Zahlen über die Richtung des Schätzfehlers entschieden, auch dass sie bei gemischtem Runden offen bleibt.')
    A(lz, 'sicherung', 'begruenden', None, 3, LP,
      'Mia rundet die vier Zahlen 3 460, 3 420, 3 440 und 3 470 jeweils auf Tausender und addiert die gerundeten Zahlen: 12 000. Die genaue Summe ist 13 790. Wie erklärt man den großen Unterschied?',
      ['Mia hat sich beim Addieren verrechnet, denn vier auf Tausender gerundete Zahlen wie diese ergeben zusammen genau 14 000 und nicht 12 000.',
       'Jede Zahl wurde um 420 bis 470 abgerundet, denn alle vier Fehler gehen in dieselbe Richtung und addieren sich zu 1 790.',
       'Runden auf Tausender ist immer falsch, denn beim Addieren mehrerer Zahlen wird jede Rundung zum Fehler.',
       'Der Unterschied kommt daher, dass man die Zahlen hätte aufrunden müssen, weil 13 790 größer ist.'], 1,
      {0: '3 000 + 3 000 + 3 000 + 3 000 = 12 000; Mia hat richtig addiert. 14 000 wäre die gerundete genaue Summe.',
       2: 'Runden zum Schätzen ist erlaubt; man muss nur wissen, wie genau das Ergebnis dann ist.',
       3: 'Die Zahlen werden nach der Regel gerundet: Hunderterstelle 4, also abrunden.'},
      'Jede Zahl hat die Hunderterstelle 4 und wird abgerundet: Die Rundungsfehler sind 460, 420, 440 und 470. Weil sie alle in dieselbe Richtung gehen, addieren sie sich: 460 + 420 + 440 + 470 = 1 790 = 13 790 − 12 000.',
      'Wirkung vieler gleichgerichteter Rundungsfehler; die Übungen runden einzelne Zahlen oder vergleichen nur zwei Rechenwege.')
    # ---------------- roemisch_schreiben ----------------
    lz = 'roemisch_schreiben'
    L(lz, 'test', 'rueckwaerts', None, 3, LP,
      'Lea schreibt eine Zahl römisch zuerst nur durch Addieren (zum Beispiel 4 = IIII, 9 = VIIII, 40 = XXXX, 90 = LXXXX) und dann nach den üblichen Regeln (4 = IV, 9 = IX, 40 = XL, 90 = XC). Alle anderen Ziffern schreibt sie beide Male gleich. Bei genau zwei Zahlen von 10 bis 99 spart sie dadurch genau 5 Zeichen. Welche Zahlen sind es?',
      'kleinere Zahl □, größere Zahl □', [49, 94], ['49', '94'],
      [(1, 44, '44', 'nur auf die Vieren geachtet; 44 spart 4 Zeichen (XXXXIIII gegen XLIV)'),
       (1, 19, '19', 'nur die Ersparnis bei der 9 gesehen; 19 spart 3 Zeichen (XVIIII gegen XIX)'),
       (2, 99, '99', 'die Zahl mit den meisten Neunen genommen; 99 spart 6 Zeichen'),
       (2, 90, '90', 'gemeint, bei 90 spare man am meisten; LXXXX gegen XC spart nur 3 Zeichen')],
      'Zehner und Einer werden getrennt geschrieben. Gespart wird nur bei den Ziffern 4 und 9: Bei einer 4 spart Lea 2 Zeichen (IIII → IV, XXXX → XL), bei einer 9 spart sie 3 Zeichen (VIIII → IX, LXXXX → XC). '
      'Genau 5 Zeichen = 2 + 3: Eine Ziffer muss 4, die andere 9 sein. Das sind 49 (XXXXVIIII → XLIX) und 94 (LXXXXIIII → XCIV).',
      'Die Übungen schreiben Zahlen nach den üblichen Regeln; hier wird rückwärts aus der Ersparnis der Subtraktionsregel auf die Ziffern geschlossen.')
    A(lz, 'korrektur', 'darstellung', None, 2, LP,
      'Es gelten die Regeln: Ein Zeichen steht höchstens dreimal hintereinander. Ein kleineres Zeichen links von einem größeren wird abgezogen, aber nur I vor V oder X, X vor L oder C und C vor D oder M. Welche der vier römischen Zahlen ist nicht regelgerecht geschrieben?',
      ['XLIV', 'CDXC', 'VC', 'MCMXC'], 2,
      {0: 'XLIV = 40 + 4 = 44 ist regelgerecht (XL und IV).',
       1: 'CDXC = 400 + 90 = 490 ist regelgerecht (CD und XC).',
       3: 'MCMXC = 1 000 + 900 + 90 = 1 990 ist regelgerecht (M, CM, XC).'},
      'V darf nicht vor C stehen, denn vor einem größeren Zeichen darf nur I, X oder C stehen, und V gehört nicht dazu. 95 schreibt man XCV. Die anderen drei Zahlen halten die Regeln ein.',
      'Regelgerechtheit statt Umwandlung; die Übungen schreiben eine Zahl um.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Ben behauptet: „Addiert man zu einer Zahl 1, so wird ihre römische Schreibweise (nach den üblichen Regeln) nie kürzer.“ Welche Aussage stimmt?',
      ['Ben irrt sich, denn wenn ein neues Zeichen gebraucht wird, kann eine Schreibweise auch kürzer werden.',
       'Ben hat recht, denn für eine größere Zahl braucht man nie weniger Zeichen als für eine kleinere.',
       'Ben hat recht bei Zahlen unter 10, denn erst ab dem Zeichen X kann eine Schreibweise kürzer werden.',
       'Die Schreibweise wird beim Addieren von 1 sogar immer länger, denn es kommt jedes Mal ein I dazu.'], 0,
      {1: 'Eine größere Zahl kann weniger Zeichen brauchen: XIV (14) hat drei, XV (15) nur zwei Zeichen.',
       2: 'Schon unter 10 wird es kürzer: III (3) hat drei Zeichen, IV (4) nur zwei; IV hat zwei, V (5) nur eins.',
       3: 'Aus XIV (14) wird XV (15): Es kommt kein I dazu, sondern eines fällt weg.'},
      'Beim Addieren von 1 wird die Schreibweise oft länger (XI → XII), aber nicht immer: Kommt ein neues Zeichen ins Spiel, kann sie kürzer werden. '
      'Beispiel: XIV (14) hat drei Zeichen, XV (15) nur zwei; ebenso III → IV und IV → V. Ben irrt sich.',
      'Die Übungen schreiben einzelne Zahlen; hier wird eine allgemeine Behauptung über das Schreiben nach den Regeln mit einem selbst gefundenen Gegenbeispiel geprüft.')
    Z(lz, 'sicherung', 'transfer', None, 2, LP,
      'Für römische Zahlen gelten die üblichen Regeln: Es gibt die Zeichen I, V, X, L, C, D und M (M = 1 000 ist das größte). Die Zeichen stehen der Größe nach; ein kleineres Zeichen vor einem größeren wird abgezogen, aber nur I vor V oder X, X vor L oder C und C vor D oder M. I, X, C und M stehen höchstens dreimal hintereinander, V, L und D höchstens einmal. Welches ist die größte Zahl, die man so schreiben kann?',
      3999, '3000 + 900 + 90 + 9',
      [(3000, '1000 + 1000 + 1000', 'nur die drei M gezählt und die Hunderter, Zehner und Einer vergessen'),
       (3888, '3000 + 800 + 80 + 8', 'die längste Schreibweise MMMDCCCLXXXVIII mit der größten Zahl verwechselt'),
       (4999, '4000 + 900 + 90 + 9', 'vier M zugelassen, obwohl ein Zeichen höchstens dreimal hintereinander stehen darf'),
       (3333, '3000 + 300 + 30 + 3', 'überall dreimal dasselbe Zeichen genommen')],
      'Für Tausender gibt es kein größeres Zeichen als M, und M darf höchstens dreimal stehen: mehr als 3 000 Tausender-Anteil geht nicht. Danach nimmt man die größten Hunderter, Zehner und Einer: CM = 900, XC = 90, IX = 9. '
      'Die größte Zahl ist MMMCMXCIX = 3 999; schon 4 000 bräuchte vier M.',
      'Die Übungen schreiben einzelne Zahlen; hier wird aus den Regeln selbst erschlossen, wo die römische Schrift an ihre Grenze kommt.')
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
    L(lz, 'test', 'rueckwaerts', None, 3, LP,
      'Lisa schreibt eine Zweierzahl mit genau fünf Ziffern auf (vorn darf auch eine 0 stehen). Darunter schreibt sie die Zweierzahl, die entsteht, wenn man jede 0 durch eine 1 und jede 1 durch eine 0 ersetzt. Im Zehnersystem unterscheiden sich die Werte der beiden Zahlen um 7. Welche Werte haben die beiden Zahlen?',
      'größere Zahl □, kleinere Zahl □', [19, 12], ['(31 + 7) : 2', '(31 − 7) : 2'],
      [(1, 31, '31', 'die Summe beider Zahlen für die größere Zahl gehalten'),
       (1, 35, '(63 + 7) : 2', 'mit sechs statt fünf Stellen gerechnet (Summe 63)'),
       (2, 24, '31 − 7', 'den Unterschied von der Summe abgezogen, ohne zu halbieren'),
       (2, 28, '(63 − 7) : 2', 'mit sechs statt fünf Stellen gerechnet (Summe 63)')],
      'An jeder der fünf Stellen steht in genau einer der beiden Zahlen eine 1. Zusammen sind die beiden Zahlen also 16 + 8 + 4 + 2 + 1 = 31 wert, ganz gleich, welche Zahl Lisa aufgeschrieben hat. '
      'Summe 31 und Unterschied 7: Die größere ist (31 + 7) : 2 = 19, die kleinere (31 − 7) : 2 = 12. Probe: 19 = 10011, 12 = 01100.',
      'Die Übungen rechnen einzelne Zweierzahlen um; hier muss man erkennen, dass eine Zahl und ihre „Gegenzahl“ zusammen immer 11111 ergeben, und daraus rückwärts schließen.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Welche Aussage über die Zweierzahlen 0111 und 111 stimmt?',
      ['0111 ist größer, denn sie hat vier Stellen und 111 nur drei.',
       '0111 und 111 haben denselben Wert, denn eine Null vorn ändert nichts.',
       '0111 ist kleiner, denn eine Null vorn macht die Zahl nicht gleich groß, sondern kleiner.',
       '111 ist größer, denn die Null vorn ist ein Platzhalter für den Wert 8.'], 1,
      {0: 'Eine Zweierzahl ist nicht größer, nur weil sie mehr Ziffern hat; führende Nullen tragen nichts bei.',
       2: 'Die Null vorn steht an der Achterstelle und zählt 0 · 8 = 0; sie ändert nichts.',
       3: 'Die Null an der Achterstelle liefert 0 · 8 = 0, nicht 8.'},
      '0111 = 0 · 8 + 1 · 4 + 1 · 2 + 1 · 1 = 7 und 111 = 4 + 2 + 1 = 7. Eine führende Null liefert 0 und ändert den Wert nicht, wie im Zehnersystem 007 = 7.',
      'Führende Nullen bei Zweierzahlen; die Übungen wandeln Zahl für Zahl um.')
    A(lz, 'korrektur', 'begruenden', None, 2, LP,
      'Die Zweierzahl A enthält mehr Einsen als die Zweierzahl B (beide beginnen mit 1). Was folgt daraus für ihre Werte im Zehnersystem?',
      ['Nichts Sicheres, denn für den Wert zählt, an welchen Stellen die Einsen stehen, und nicht, wie viele es sind.',
       'A ist größer, denn jede Eins bringt einen Wert dazu, eine Null an derselben Stelle dagegen nicht.',
       'A ist mindestens doppelt so groß wie B, denn jede weitere Eins verdoppelt den Wert der ganzen Zweierzahl noch einmal.',
       'B ist größer, denn wer mit weniger Einsen auskommt, braucht dafür mehr Stellen und ist deshalb größer.'], 0,
      {1: 'Es kommt darauf an, wo die Einsen stehen: 111 = 7 hat drei Einsen, 1000 = 8 nur eine und ist trotzdem größer.',
       2: 'Eine weitere Eins verdoppelt nicht: 11 = 3 und 10 = 2; 111 = 7 ist sogar kleiner als 1000 = 8.',
       3: 'Weniger Einsen bedeuten nicht mehr Stellen: 10 hat weniger Einsen als 11 und ist kleiner.'},
      'Der Wert hängt davon ab, an welchen Stellen die Einsen stehen, nicht wie viele es sind. 111 = 4 + 2 + 1 = 7 hat drei Einsen, 1000 = 8 nur eine; trotzdem ist 1000 größer. 11 = 3 hat mehr Einsen als 10 = 2 und ist größer. '
      'Aus der Zahl der Einsen allein folgt also nichts über die Größe.',
      'Die Übungen vergleichen zwei gegebene Zweierzahlen durch Umrechnen; hier wird allgemein entschieden, ob die Zahl der Einsen etwas über die Größe sagt.')
    Z(lz, 'sicherung', 'transfer', None, 3, LP,
      'Ein Zähler hat fünf Lampen für die Stellenwerte 16, 8, 4, 2 und 1; eine leuchtende Lampe bedeutet 1, eine dunkle 0. Die Lampe für den Stellenwert 4 ist kaputt und bleibt immer dunkel. Wie viele der Zahlen von 0 bis 31 kann der Zähler trotzdem richtig anzeigen?',
      16, '2 · 2 · 2 · 2',
      [(31, '32 − 1', 'nur die Zahl 4 selbst für verloren gehalten'),
       (28, '32 − 4', 'nur die Zahlen 4, 5, 6 und 7 für verloren gehalten'),
       (8, '32 : 4', 'durch den Wert der kaputten Lampe geteilt'),
       (27, '31 − 4', 'von der größten Zahl den Wert der kaputten Lampe abgezogen')],
      'Jede Zahl von 0 bis 31 hat genau eine Schreibweise mit fünf Lampen. Richtig anzeigen kann der Zähler nur die Zahlen, bei denen die Lampe für 4 dunkel ist. Für die vier übrigen Lampen gibt es je zwei Möglichkeiten: 2 · 2 · 2 · 2 = 16 Zahlen. '
      'Das ist genau die Hälfte: Zu jeder Zahl ohne die 4 gehört eine Zahl, die 4 mehr ist und die Lampe braucht (0 und 4, 1 und 5, …, 27 und 31).',
      'Die Übungen lesen eine Lampenreihe ab; hier wird überlegt, welche Zahlen eine bestimmte Stelle brauchen, und dass das genau die Hälfte ist.')
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
