"""Zwanzigste Runde, Klasse 5: gleichungen.einfach – Typen, neue Übungen, Knobel-Bordkarten (siehe _stufen_kl5.py)."""
from _stufen_kl5 import A, Z

KARTEN = {
 'waage': {
  'leiter': ('An einer Waage eine einfache Gleichung ablesen und eine Lösung prüfen.',
             'Größere Zahlen, Gleichung von rechts gelesen, Dosen und Murmeln als Gleichung.',
             'Gleiches auf beiden Seiten wegnehmen, Gewichte vergleichen, Fehler beim Wegnehmen erklären.'),
  'typ': [(r'gleiche Dosen und \d+ Murmeln|Äpfel', 'transfer'), (r'mit je x|4 · 3 \+ 5', 'verknuepfen'), (r'gleiche Würfel', 'pruefung'), (r'Was ist falsch', 'fehler'),
          (r'^Ist \d+ eine Lösung', 'erkennen'), (r'S1:.', 'direkt'), (r'= x \+', 'umkehr'), (r'Probiere aus|x \+ x', 'mehrschritt'), (r'Dosen', 'einkleidung'), (r'.', 'darstellung')],
  'neu': [],
  'knobel': [
   Z('Auf einer Waage gilt: 3 Würfel wiegen so viel wie 2 Kugeln. Eine Kugel wiegt so viel wie ein Würfel und 50 g. Wie viel g wiegt ein Würfel?', 100, '2 * 50',
     '2 Kugeln = 2 Würfel + 100 g. Also 3 Würfel = 2 Würfel + 100 g. Nimm auf beiden Seiten 2 Würfel weg: 1 Würfel = 100 g.', 'Ersetze die Kugeln durch Würfel und Gramm.', einheit='g'),
   Z('Dreieck und Kreis wiegen zusammen 10 g, Kreis und Quadrat 13 g, Dreieck und Quadrat 15 g. Wie viel g wiegt das Quadrat?', 9, '(10 + 13 + 15) // 2 - 10',
     'Alle drei Paare zusammen: 38 g. Darin kommt jede Form zweimal vor, also wiegen alle drei Formen zusammen 19 g. Ohne Dreieck und Kreis (10 g) bleibt das Quadrat: 9 g.', 'Lege alle drei Paare zusammen auf eine Waage.', einheit='g'),
  ],
 },
 'umkehr_plus': {
  'leiter': ('Einfache Plus- und Minusgleichungen mit der Umkehraufgabe lösen.',
             'Größere Zahlen, x an zweiter Stelle oder rechts, die passende Umkehrrechnung wählen.',
             'Rechte Seite erst ausrechnen, negative Zahlen, Rechenketten rückwärts, Fehler bei der Umkehrung erklären.'),
  'typ': [(r'52 \+ 64', 'verknuepfen'), (r'S3:Welche Rechnung', 'begruenden'), (r'−23|1 000 subtrahieren', 'transfer'), (r'Ich denke', 'rueckwaerts'), (r'Was ist falsch', 'fehler'),
          (r'S1:.', 'direkt'), (r'Welche Rechnung', 'darstellung'), (r'\d+ − x|= x', 'umkehr'), (r'.', 'mehrschritt')],
  'neu': [
   ('erkennen', A('Welche Rechnung löst x + 15 = 40?', '40 − 15', ['40 + 15', '15 − 40', '40 : 15'], 'Die Umkehrung von „+ 15“ ist „− 15“: x = 40 − 15 = 25.', 'Was macht „+ 15“ rückgängig?')),
   ('pruefung', Z('Fülle die Lücke: 2 345 − □ + 160 = 1 900. Welche Zahl gehört in die Lücke?', 605, '2345 + 160 - 1900', '2 345 + 160 = 2 505. Davon muss man 605 abziehen, damit 1 900 herauskommt.', 'Was muss von 2 505 abgezogen werden?')),
  ],
  'knobel': [
   Z('Addiert man zu einer Zahl 1 234, erhält man dasselbe, wie wenn man von 5 000 die Zahl 2 345 abzieht. Wie heißt die Zahl?', 1421, '5000 - 2345 - 1234', '5 000 − 2 345 = 2 655. x + 1 234 = 2 655, also x = 1 421.', 'Rechne zuerst die rechte Seite aus.'),
   Z('Ich denke mir eine Zahl. Ziehe ich 99 davon ab, erhalte ich dasselbe, wie wenn ich meine Zahl von 301 abziehe. Welche Zahl ist es?', 200, '(301 + 99) // 2',
     'Die Zahl liegt genau in der Mitte zwischen 99 und 301: Sie ist von beiden gleich weit entfernt. Mitte: (99 + 301) : 2 = 200. Probe: 200 − 99 = 101 = 301 − 200.', 'Wo liegt eine Zahl, die von 99 und von 301 gleich weit entfernt ist?'),
  ],
 },
 'umkehr_mal': {
  'leiter': ('Einfache Mal- und Geteiltgleichungen mit der Umkehraufgabe lösen.',
             'Größere Zahlen, x als Teiler, die passende Umkehrrechnung wählen.',
             'Negative Teiler, Rechenketten rückwärts, Lücken auf beiden Seiten, Parameter bestimmen, Fehler bei der Umkehrung erklären.'),
  'typ': [(r'\(−4\)', 'transfer'), (r'Was ist falsch', 'fehler'), (r'Fünffache|Seil', 'verknuepfen'), (r'S1:.', 'direkt'), (r'Welche Rechnung', 'darstellung'), (r'^Löse \d+ : x', 'umkehr'), (r'.', 'mehrschritt')],
  'neu': [
   ('erkennen', A('Welche Rechnung löst 8 · x = 56?', '56 : 8', ['56 · 8', '56 − 8', '8 : 56'], 'Die Umkehrung von „· 8“ ist „: 8“: x = 7.', 'Was macht „· 8“ rückgängig?')),
   ('rueckwaerts', Z('Ich denke mir eine Zahl, teile sie durch 7 und nehme das Ergebnis mal 3. Ich erhalte 27. Welche Zahl habe ich mir gedacht?', 63, '27 // 3 * 7', 'Rückwärts: 27 : 3 = 9, dann 9 · 7 = 63.', 'Mach den letzten Schritt zuerst rückgängig.')),
   ('begruenden', A('Stimmt die Aussage? „Bei x : 8 = 5 rechnet man x = 5 : 8.“', 'Nein: Die Umkehrung von „: 8“ ist „· 8“, also x = 40.', ['Ja, das stimmt.', 'Nein: x = 8 : 5.', 'Nein: x = 8 − 5.'], 'Probe: 40 : 8 = 5. Mit 5 : 8 käme keine natürliche Zahl heraus.', 'Mach die Probe mit deinem Ergebnis.')),
   ('pruefung', Z('Fülle die Lücke: 7 · □ = 3 · 84. Welche Zahl gehört in die Lücke?', 36, '3 * 84 // 7', '3 · 84 = 252. 252 : 7 = 36.', 'Rechne zuerst die rechte Seite aus.')),
   ('parameter', Z('Für welche Zahl a hat die Gleichung a · x = 96 die Lösung x = 12?', 8, '96 // 12', 'a · 12 = 96, also a = 96 : 12 = 8.', 'Setze x = 12 ein.')),
  ],
  'knobel': [
   Z('Eine Zahl wird verdoppelt, das Ergebnis verdreifacht und dieses vervierfacht. Man erhält 600. Welche Zahl war es?', 25, '600 // 24', 'Insgesamt wurde mit 2 · 3 · 4 = 24 multipliziert. 600 : 24 = 25.', 'Mit welcher Zahl wurde insgesamt multipliziert?'),
   Z('Das Produkt aus einer Zahl und 25 ist 1 000. Welche Zahl erhält man, wenn man diese Zahl durch 8 teilt?', 5, '1000 // 25 // 8', '1 000 : 25 = 40. 40 : 8 = 5.', 'Bestimme zuerst die Zahl.'),
  ],
 },
 'zwei_schritte': {
  'leiter': ('Gleichungen mit zwei Rechenschritten (mal, dann plus oder minus) lösen.',
             'Rechenketten rückwärts lesen, Reihenfolge der Umkehrschritte wählen, mit Geteilt.',
             'Klammern, Lücken, Zahlenrätsel rückwärts, Fehler in der Reihenfolge erklären.'),
  'typ': [(r'\) : 3', 'transfer'), (r'^Löse \(', 'verknuepfen'), (r'Welche Rechnung löst', 'begruenden'), (r'Ergänze die Lücke', 'pruefung'), (r'Ich denke', 'rueckwaerts'), (r'Was ist falsch', 'fehler'),
          (r'S1:.', 'direkt'), (r'Rechenkette', 'darstellung'), (r'Wie löst du', 'umkehr'), (r'.', 'mehrschritt')],
  'neu': [
   ('erkennen', A('Bei 5 · x + 3 = 38: Was rechnet man zuerst?', '38 − 3', ['38 : 5', '38 + 3', '5 · 3'], 'Rückwärts: Zuletzt wurde „+ 3“ gerechnet, das macht man zuerst rückgängig: 35, dann 35 : 5 = 7.', 'Welcher Rechenschritt kam zuletzt?')),
  ],
  'knobel': [
   Z('Löse 3 · (2 · x − 5) = 39.', 9, '(39 // 3 + 5) // 2', 'Von außen nach innen: 39 : 3 = 13. 2 · x − 5 = 13, also 2 · x = 18 und x = 9.', 'Teile zuerst durch 3.'),
   Z('Ich denke mir eine Zahl, addiere 5, nehme das Ergebnis mal 3 und ziehe dann meine gedachte Zahl ab. Ich erhalte 35. Welche Zahl habe ich mir gedacht?', 10, '(35 - 15) // 2',
     '3 · (x + 5) − x = 3 · x + 15 − x = 2 · x + 15. Also 2 · x + 15 = 35, 2 · x = 20, x = 10. Probe: (10 + 5) · 3 − 10 = 35.', 'Probiere einige Zahlen und achte darauf, wie sich das Ergebnis ändert.'),
  ],
 },
 'probe': {
  'leiter': ('Mit der Probe prüfen, ob eine Zahl eine Gleichung löst.',
             'Lösung finden und mit der Probe bestätigen, Fehler in Lösungswegen suchen.',
             'Aus der Probe schließen, ob die Lösung größer oder kleiner ist, mehrere Kandidaten prüfen, zwischen zwei Ergebnissen entscheiden.'),
  'typ': [(r'Ist die Lösung größer', 'begruenden'), (r'links 41|noch größer', 'verknuepfen'), (r'Welche der Zahlen', 'pruefung'), (r'Für welche der Zahlen', 'transfer'),
          (r'Zwei Kinder', 'fehler'), (r'richtige L', 'rueckwaerts'), (r'S1:^Ist x', 'erkennen'), (r'S1:.', 'direkt'), (r'^Ist x', 'umkehr'), (r'So wurde', 'darstellung'), (r'.', 'mehrschritt')],
  'neu': [],
  'knobel': [
   Z('Für x = 4 ergibt die linke Seite von 3 · x + a = 29 genau 20. Welche Zahl löst die Gleichung?', 7, '(29 - (20 - 12)) // 3', 'Aus 3 · 4 + a = 20 folgt a = 8. Dann 3 · x + 8 = 29, 3 · x = 21, x = 7.', 'Bestimme zuerst a.'),
   Z('Zwei Zahlen haben die Summe 20 und den Unterschied 6. Wie heißt die größere?', 13, '(20 + 6) // 2', 'Probieren: 13 + 7 = 20 und 13 − 7 = 6. Oder: Nimmt man den Unterschied weg, bleiben 14 für zwei gleiche Zahlen, also 7 und 13.', 'Probiere Zahlenpaare mit der Summe 20.'),
  ],
 },
 'aufstellen': {
  'leiter': ('Zu einem einfachen Zahlenrätsel die Zahl finden.',
             'Sachaufgaben mit Preisen und Altern als Gleichung aufschreiben und lösen, passende Gleichung wählen.',
             'Altersrätsel, Umfang, aufeinanderfolgende Zahlen, Verteilungsaufgaben, Geschichte zur Gleichung finden.'),
  'typ': [(r'Mutter|28 Jahre älter|doppelt so alt', 'transfer'), (r'Welche Geschichte|Zimmern', 'pruefung'), (r'Rechteck|aufeinanderfolgende', 'verknuepfen'), (r'Subtrahiert man', 'rueckwaerts'),
          (r'S1:.', 'direkt'), (r'Welche Gleichung passt', 'darstellung'), (r'nehme sie mal', 'mehrschritt'), (r'.', 'einkleidung')],
  'neu': [
   ('erkennen', A('„Ich denke mir eine Zahl und addiere 15. Ich erhalte 40.“ Welche Gleichung passt?', 'x + 15 = 40', ['x · 15 = 40', '15 − x = 40', 'x − 15 = 40'], 'Gedachte Zahl x, plus 15, Ergebnis 40.', 'Schreibe den Satz Schritt für Schritt mit x.')),
  ],
  'knobel': [
   Z('Auf einem Hof gibt es Hühner (2 Beine) und Hasen (4 Beine), zusammen 10 Tiere mit 28 Beinen. Wie viele Hasen sind es?', 4, '(28 - 20) // 2',
     'Wären alle 10 Tiere Hühner, gäbe es 20 Beine. Es sind 8 Beine mehr; jeder Hase bringt 2 Beine mehr: 8 : 2 = 4 Hasen. Probe: 4 · 4 + 6 · 2 = 28.', 'Stell dir vor, alle Tiere wären Hühner.'),
   Z('Drei Geschwister sind zusammen 30 Jahre alt. Das mittlere ist 3 Jahre älter als das jüngste, das älteste 3 Jahre älter als das mittlere. Wie alt ist das älteste?', 13, '30 // 3 + 3',
     'Das mittlere ist genau der Durchschnitt: 30 : 3 = 10. Das älteste ist 13, das jüngste 7. Probe: 7 + 10 + 13 = 30.', 'Wer liegt genau in der Mitte?'),
  ],
 },
 'ohne_loesung': {
  'leiter': ('Erkennen, ob eine einfache Gleichung eine Lösung in ℕ hat.',
             'Lösbare und unlösbare Gleichungen unterscheiden, mit ganzen Zahlen lösen, Sachsituationen.',
             'Rechte Seiten so ändern, dass es eine Lösung gibt, Sonderfälle mit 0, lösbare Gleichungen zählen.'),
  'typ': [(r'nächstgrößere', 'rueckwaerts'), (r'0 · x|jede Zahl', 'begruenden'), (r'Für welche|kleinste natürliche', 'parameter'), (r'Band', 'transfer'), (r'Wie viele der Gleichungen', 'pruefung'),
          (r'S1:.', 'erkennen'), (r'Kinder|Temperatur', 'einkleidung'), (r'Welche Gleichung', 'darstellung'), (r'.', 'mehrschritt')],
  'neu': [
   ('direkt', Z('Löse 7 · x = 63 in ℕ.', 9, '63 // 7', '63 : 7 = 9, Probe 7 · 9 = 63.', 'Welche Zahl mal 7 ergibt 63?')),
  ],
  'knobel': [
   Z('Für wie viele natürliche Zahlen b von 1 bis 30 hat 4 · x = b eine Lösung in ℕ?', 7, '30 // 4', 'b muss durch 4 teilbar sein: 4, 8, 12, 16, 20, 24, 28 – das sind 7.', 'Welche b sind durch 4 teilbar?'),
   Z('Für welche kleinste natürliche Zahl c haben sowohl 6 · x = c als auch 8 · x = c eine Lösung in ℕ (mit x mindestens 1)?', 24, '24', 'c muss durch 6 und durch 8 teilbar sein. Vielfache von 8: 8, 16, 24 – 24 ist das erste, das auch durch 6 teilbar ist.', 'Gehe die Vielfachen von 8 durch.'),
  ],
 },
}
