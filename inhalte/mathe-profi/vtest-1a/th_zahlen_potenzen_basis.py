T = "zahlen.potenzen_basis"
P = "rr.potenz"
# ═════════ schreibweise ═════════
neu(T, "schreibweise", "test", "begruenden", W(
    "Mia sagt: „2⁵ ist 10.“ Welche Aussage über Mias Satz ist richtig?",
    "Mia irrt sich. 2⁵ heißt 2 · 2 · 2 · 2 · 2 = 32. Die 5 sagt, wie oft die 2 als Faktor dasteht.",
    [("Mia hat recht. Die 5 sagt, wie oft gerechnet wird: 2 · 5 = 10.", "Basis mal Hochzahl gerechnet (2 · 5 = 10)", 2 * 5 == 10 and 2 ** 5 != 10),
     ("Mia hat recht. 2⁵ ist 2 + 2 + 2 + 2 + 2, und das sind 10.", "Die Hochzahl als wiederholtes Plus gedeutet (2 + 2 + 2 + 2 + 2 = 10)", 2 + 2 + 2 + 2 + 2 == 10 and 2 ** 5 != 10),
     ("Mia irrt sich. 2⁵ heißt 5 · 5 = 25, denn die Hochzahl wird mit sich selbst malgenommen.", "Die Hochzahl mit sich selbst malgenommen (5 · 5 = 25)", 5 * 5 == 25 and 2 ** 5 != 25)],
    "Die Hochzahl 5 zählt die Faktoren: 2⁵ = 2 · 2 · 2 · 2 · 2. Schritt für Schritt: 2 · 2 = 4, 4 · 2 = 8, 8 · 2 = 16, 16 · 2 = 32. Mit 2 · 5 = 10 würde man nur zwei Zahlen malnehmen. 2 + 2 + 2 + 2 + 2 wäre eine Plusrechnung. Und 5 · 5 vertauscht die Rolle von Basis und Hochzahl.",
    2 ** 5 == 32 and 2 * 2 * 2 * 2 * 2 == 32), regel=P, lehrplan="M5 3")
neu(T, "schreibweise", "korrektur", "umkehr", Z(
    "Dieselbe natürliche Zahl steht 4-mal als Faktor da: □ · □ · □ · □. Das Produkt ist 81. Welche Zahl steht im Kästchen?",
    3, "3", lambda: next(b for b in range(1, 50) if b * b * b * b == 81),
    "Gesucht ist eine Zahl b mit b · b · b · b = 81. Probiere: 2 · 2 · 2 · 2 = 16 ist zu klein, 3 · 3 · 3 · 3 = 9 · 9 = 81 passt. Die Zahl ist 3, denn 3⁴ = 81.",
    [(20, "81 durch 4 geteilt (ganzzahlig): die Zahl 4-mal addiert statt malgenommen", "81 // 4"),
     (77, "4 von 81 abgezogen", "81 - 4"),
     (324, "81 mit 4 malgenommen", "81 * 4")]), form="umkehren", regel=P)
neu(T, "schreibweise", "korrektur", "darstellung", Z(
    "Du hast 2 Eltern. Jede Person hat wieder 2 Eltern. Die Tabelle zeigt, wie viele Personen es in den ersten Generationen vor dir gibt (Eltern = 1. Generation). Wie viele Personen sind es in der 4. Generation (Ururgroßeltern)? Doppelt vorkommende Personen werden nicht beachtet.",
    16, "2 ** 4", lambda: __import__("functools").reduce(lambda a, _: a * 2, range(4), 1),
    "1. Generation: 2 Personen. 2. Generation: 2 · 2 = 4. 3. Generation: 2 · 2 · 2 = 8. 4. Generation: 2 · 2 · 2 · 2 = 2⁴ = 16.",
    [(8, "Basis mal Hochzahl: 2 · 4 gerechnet", "2 * 4"), (32, "Eine Generation zu weit gezählt: 2⁵", "2 ** 5"), (64, "Basis und Hochzahl vertauscht: 4³", "4 ** 3")], einheit="Personen",
    grafik={"typ": "tabelle", "kopf": ["Generation", "1", "2", "3"], "zeilen": [["Personen", "2", "4", "8"]]}), form="bruecke", regel=P)
neu(T, "schreibweise", "korrektur", "umkehr", Z(
    "In einer Potenz steht die Basis 6. Der Wert der Potenz ist 216. Wie oft steht die 6 als Faktor da?",
    3, "3", lambda: next(n for n in range(1, 10) if 6 ** n == 216),
    "Probiere: 6 · 6 = 36, 6 · 6 · 6 = 216. Die 6 steht 3-mal als Faktor da, also ist die Potenz 6³ und der Exponent 3.",
    [(36, "216 durch 6 geteilt", "216 // 6"), (6, "216 durch 36 geteilt", "216 // 36"), (210, "6 von 216 abgezogen", "216 - 6")]), form="umkehren", regel=P)
neu(T, "schreibweise", "sicherung", "darstellung", W(
    "Welche Aussage über die Potenz 4⁶ stimmt?",
    "Die 4 steht 6-mal als Faktor da: 4 · 4 · 4 · 4 · 4 · 4.",
    [("Die 6 steht 4-mal als Faktor da: 6 · 6 · 6 · 6.", "Basis und Hochzahl vertauscht (6⁴ = 1 296 statt 4⁶ = 4 096)", 6 ** 4 != 4 ** 6),
     ("4⁶ ist das Sechsfache von 4, also 4 · 6 = 24.", "Hochzahl als Malnehmer gedeutet (4 · 6 = 24)", 4 * 6 != 4 ** 6),
     ("4⁶ ist 4 + 4 + 4 + 4 + 4 + 4 = 24.", "Plus statt Mal (4 + 4 + 4 + 4 + 4 + 4 = 24)", 4 + 4 + 4 + 4 + 4 + 4 == 24 and 4 ** 6 != 24)],
    "In 4⁶ ist 4 die Basis (der Faktor) und 6 der Exponent (die Zahl der Faktoren). 4⁶ = 4 · 4 · 4 · 4 · 4 · 4 = 4 096. Mit 6⁴ = 1 296 oder mit 4 · 6 = 24 kommt etwas ganz anderes heraus.",
    4 ** 6 == 4 * 4 * 4 * 4 * 4 * 4 == 4096), form="bruecke", regel=P)
neu(T, "schreibweise", "sicherung", "mehrschritt", W(
    "Man darf Basis und Hochzahl einer Potenz nicht einfach vertauschen. Trotzdem stimmt eine der folgenden Gleichungen. Welche?",
    "2⁴ = 4²",
    [("3² = 2³", "Vertauscht: 3² = 9, aber 2³ = 8", 3 ** 2 != 2 ** 3),
     ("5² = 2⁵", "Vertauscht: 5² = 25, aber 2⁵ = 32", 5 ** 2 != 2 ** 5),
     ("4³ = 3⁴", "Verglichen: 4³ = 64, aber 3⁴ = 81", 4 ** 3 != 3 ** 4)],
    "Rechne beide Seiten aus. 2⁴ = 2 · 2 · 2 · 2 = 16 und 4² = 4 · 4 = 16: gleich. Bei 3² = 9 und 2³ = 8, bei 5² = 25 und 2⁵ = 32, bei 4³ = 64 und 3⁴ = 81 sind die Seiten verschieden. Meistens ändert sich der Wert beim Vertauschen; bei 2⁴ und 4² trifft es zufällig zu.",
    2 ** 4 == 4 ** 2 == 16), form="zwei_wege", regel=P)
neu(T, "schreibweise", "sicherung", "begruenden", W(
    "Tom schreibt: „3⁴ = 3 · 4 = 12.“ Welche Aussage über Toms Rechnung stimmt?",
    "Fehler: Er hat 3 mit 4 malgenommen. Richtig wäre 3 · 3 · 3 · 3 = 81.",
    [("Fehler: Er hat 3 mit 4 malgenommen. Richtig wäre 4 · 4 · 4 = 64.", "Basis und Hochzahl vertauscht (4³ = 64)", 4 ** 3 != 3 ** 4),
     ("Fehler: Er hat 3 mit 4 malgenommen. Richtig wäre 3 · 3 · 3 = 27.", "Nur drei Faktoren gezählt (3³ = 27)", 3 ** 3 != 3 ** 4),
     ("Kein Fehler: 3⁴ heißt 3 · 4, und das ist 12.", "Toms Fehlvorstellung bestätigt (3 · 4 = 12)", 3 * 4 != 3 ** 4)],
    "Die Hochzahl 4 sagt, dass die 3 viermal als Faktor dasteht: 3 · 3 · 3 · 3 = 9 · 9 = 81. Tom hat Basis und Hochzahl malgenommen (3 · 4 = 12). Richtig ist 81, nicht 12, 64 oder 27.",
    3 ** 4 == 81), regel=P)
# ═════════ quadrat ═════════
neu(T, "quadrat", "test", "rueckwaerts", Z(
    "Ein quadratischer Garten hat eine Fläche von 225 m². Er wird rundherum mit einem Zaun umgeben (ohne Tor). Wie viele Meter Zaun braucht man?",
    60, "15 * 4", lambda: 4 * next(s for s in range(1, 100) if s * s == 225),
    "Die Fläche eines Quadrats ist Seite mal Seite. Welche Zahl mal sich selbst ergibt 225? 15 · 15 = 225, also ist die Seite 15 m lang. Der Zaun geht um alle vier Seiten: 4 · 15 m = 60 m.",
    [(900, "Die Fläche mit 4 malgenommen (225 · 4)", "225 * 4"), (45, "Nur drei Seiten gerechnet (3 · 15)", "3 * 15"), (30, "Nur zwei Seiten gerechnet (2 · 15)", "2 * 15")], einheit="m"), form="umkehren", regel=P)
neu(T, "quadrat", "korrektur", "mehrschritt", W(
    "Welche Zahl ist eine Quadratzahl? Wähle die Aussage mit der richtigen Begründung.",
    "121, denn 11 · 11 = 121.",
    [("99, denn 9 · 9 = 99.", "9 · 9 ist 81, nicht 99 („gleiche Ziffern“ mit Quadrat verwechselt)", 9 * 9 != 99),
     ("48, denn 48 = 6 · 8.", "Produkt zweier verschiedener Zahlen für ein Quadrat gehalten", all(b * b != 48 for b in range(1, 20))),
     ("150, denn 150 ist das Doppelte von 75.", "Doppeltes einer Zahl für ein Quadrat gehalten", all(b * b != 150 for b in range(1, 20)))],
    "Eine Quadratzahl ist eine Zahl mal sich selbst. 11 · 11 = 121, also ist 121 eine Quadratzahl. 9 · 9 ist 81, nicht 99. 48 liegt zwischen 6² = 36 und 7² = 49. 150 liegt zwischen 12² = 144 und 13² = 169. Beide sind keine Quadratzahlen.",
    11 * 11 == 121), form="verfahren_waehlen", regel=P)
neu(T, "quadrat", "korrektur", "mehrschritt", Z(
    "Bild A hat 7 Reihen mit je 7 Bildpunkten. Bild B hat 11 Reihen mit je 11 Bildpunkten. Ben meint: „Der Unterschied ist 4 · 4, weil 11 − 7 = 4 ist.“ Mia rechnet beide Anzahlen aus und zieht ab. Wie viele Bildpunkte hat Bild B wirklich mehr als Bild A?",
    72, "11 ** 2 - 7 ** 2", lambda: sum(1 for _ in range(11) for _ in range(11)) - sum(1 for _ in range(7) for _ in range(7)),
    "Bild A hat 7 · 7 = 49 Bildpunkte, Bild B hat 11 · 11 = 121 Bildpunkte. Der Unterschied ist 121 − 49 = 72. Ben irrt sich: Der Unterschied der Flächen ist nicht das Quadrat des Unterschieds der Seiten (4 · 4 = 16).",
    [(16, "Wie Ben nur den Unterschied der Seiten quadriert (4 · 4)", "4 * 4"), (4, "Nur den Unterschied der Seiten genannt: 11 − 7", "11 - 7"), (28, "Nur einen Streifen gerechnet: 4 · 7", "4 * 7")], einheit="Bildpunkte"), form="zwei_wege", regel=P)
neu(T, "quadrat", "korrektur", "darstellung", W(
    "Welche Aussage über das Quadrat von 8, also 8², stimmt?",
    "8² = 8 · 8 = 64. Das ist die Zahl der Felder eines Quadrats mit 8 Feldern je Seite.",
    [("8² = 8 · 2 = 16. Die Hochzahl sagt, womit man malnimmt.", "Basis mal Hochzahl gerechnet (8 · 2 = 16)", 8 * 2 != 8 ** 2),
     ("8² = 8 + 8 = 16. Hoch 2 heißt: die Zahl doppelt nehmen.", "Plus statt Mal gerechnet (8 + 8 = 16)", 8 + 8 != 8 ** 2),
     ("8² = 2⁸ = 256. Basis und Hochzahl dürfen vertauscht werden.", "Basis und Hochzahl vertauscht (2⁸ = 256)", 2 ** 8 != 8 ** 2)],
    "Hoch 2 heißt: die Zahl mal sich selbst. 8² = 8 · 8 = 64. Ein Quadrat mit 8 Reihen zu je 8 Feldern hat 64 Felder. 8 · 2 und 8 + 8 sind 16, und 2⁸ ist 256: Alle drei sind etwas anderes.",
    8 * 8 == 64), regel=P)
neu(T, "quadrat", "sicherung", "umkehr", Z(
    "Ein quadratischer Obstgarten wird um eine Reihe und eine Spalte erweitert und bleibt dabei quadratisch. Dadurch kommen genau 27 Bäume dazu. Wie viele Reihen hat der Garten nach der Erweiterung?",
    14, "(27 + 1) // 2", lambda: next(n for n in range(1, 100) if n * n - (n - 1) * (n - 1) == 27),
    "Probiere: 13 · 13 = 169 und 14 · 14 = 196. Der Unterschied ist 196 − 169 = 27. Der Garten hat nachher 14 Reihen. (Die neue Reihe hat 14 Bäume, die neue Spalte 13 weitere.)",
    [(13, "27 durch 2 geteilt (ganzzahlig)", "27 // 2"), (28, "1 zu 27 addiert", "27 + 1"), (54, "27 mit 2 malgenommen", "27 * 2")], einheit="Reihen"), form="umkehren", regel=P)
neu(T, "quadrat", "sicherung", "verknuepfen", Z(
    "Auf einem Feld liegen 25 Reihen mit je 25 Punkten, das sind 625 Punkte. Man nimmt die unterste Reihe und die rechte Spalte weg. Wie viele Punkte bleiben liegen?",
    576, "25 ** 2 - 25 - 24", lambda: 24 * 24,
    "Die unterste Reihe hat 25 Punkte. In der rechten Spalte bleiben noch 24 weitere Punkte (der Eckpunkt gehört schon zur Reihe). 625 − 25 − 24 = 576. Das übrige Feld hat 24 Reihen mit je 24 Punkten: 24 · 24 = 576.",
    [(600, "Nur eine Reihe weggenommen: 625 − 25", "625 - 25"), (575, "Den Eckpunkt zweimal abgezogen: 625 − 25 − 25", "625 - 25 - 25"), (601, "Nur die Spalte ohne Eckpunkt weggenommen: 625 − 24", "625 - 24")], einheit="Punkte"), form="bruecke", regel=P)
neu(T, "quadrat", "sicherung", "begruenden", W(
    "Eine quadratische Platte hat die Seitenlänge 5 cm. Eine zweite hat die doppelte Seitenlänge, also 10 cm. Wie verhalten sich die Flächen? Wähle die richtige Begründung.",
    "Die große Platte hat 4-mal so viel Fläche: 10 · 10 = 100 cm² und 5 · 5 = 25 cm², und 100 ist 4-mal 25.",
    [("Die große Platte hat doppelt so viel Fläche, denn die Seite ist doppelt so lang.", "Doppelte Seite für doppelte Fläche gehalten", 10 * 10 != 2 * 5 * 5),
     ("Die große Platte hat 5 cm² mehr Fläche, denn die Seite wird um 5 cm länger.", "Zuwachs der Seite als Zuwachs der Fläche gedeutet", 10 * 10 - 5 * 5 != 5),
     ("Die große Platte hat 4-mal so viel Fläche, weil auch der Umfang 4-mal so groß ist.", "Richtiges Ergebnis, falsche Begründung (der Umfang wird nur doppelt so groß: 20 cm und 40 cm)", 4 * 10 == 2 * 4 * 5 and 4 * 10 != 4 * 4 * 5)],
    "Fläche der kleinen Platte: 5 · 5 = 25 cm². Fläche der großen Platte: 10 · 10 = 100 cm². 100 : 25 = 4. Der Umfang wächst nur von 20 cm auf 40 cm, also auf das Doppelte. Die Fläche wächst auf das Vierfache.",
    10 * 10 == 4 * 5 * 5), regel=P)
# ═════════ zehner ═════════
neu(T, "zehner", "test", "begruenden", W(
    "Welche Zahl ist größer: 9 · 10⁵ oder 10⁶? Wähle die richtige Begründung.",
    "10⁶ ist größer: 10⁶ = 1 000 000, aber 9 · 10⁵ = 900 000.",
    [("9 · 10⁵ ist größer, denn 9 ist größer als 1.", "Nur 9 und 1 verglichen, die Hochzahlen vergessen", 9 * 10 ** 5 < 10 ** 6),
     ("9 · 10⁵ ist größer, denn 9 · 5 = 45 ist größer als 6.", "Basis und Hochzahl vermischt (9 · 5 = 45 gegen 6)", 9 * 5 > 6 and 9 * 10 ** 5 < 10 ** 6),
     ("Beide sind gleich groß, denn 9 · 10⁵ ist fast 10 · 10⁵, und das ist 10⁶.", "„Fast“ für „gleich“ gehalten", 9 * 10 ** 5 != 10 ** 6)],
    "9 · 10⁵ = 9 · 100 000 = 900 000. 10⁶ = 1 000 000. Weil 1 000 000 größer als 900 000 ist, ist 10⁶ größer. Auf die Hochzahl kommt es an: Sie sagt, wie viele Nullen hinter der Ziffer stehen.",
    10 ** 6 > 9 * 10 ** 5), regel=P)
neu(T, "zehner", "korrektur", "darstellung", W(
    "Welche Schreibweise gehört NICHT zur Zahl 3 400 000?",
    "34 · 10⁴",
    [("34 · 10⁵", "Diese Schreibweise stimmt (34 · 100 000 = 3 400 000), ist also nicht gesucht", 34 * 10 ** 5 == 3400000),
     ("340 · 10⁴", "Diese Schreibweise stimmt (340 · 10 000 = 3 400 000), ist also nicht gesucht", 340 * 10 ** 4 == 3400000),
     ("3 · 10⁶ + 4 · 10⁵", "Diese Schreibweise stimmt (3 000 000 + 400 000 = 3 400 000), ist also nicht gesucht", 3 * 10 ** 6 + 4 * 10 ** 5 == 3400000)],
    "34 · 10⁵ = 34 · 100 000 = 3 400 000: stimmt. 340 · 10⁴ = 340 · 10 000 = 3 400 000: stimmt. 3 · 10⁶ + 4 · 10⁵ = 3 000 000 + 400 000 = 3 400 000: stimmt. 34 · 10⁴ = 34 · 10 000 = 340 000: Das ist zehnmal zu klein, es gehört nicht zur Zahl.",
    34 * 10 ** 4 == 340000 != 3400000), form="bruecke", regel=P)
neu(T, "zehner", "korrektur", "umkehr", Z(
    "Eine Sammlung von Münzen wiegt zusammen 500 kg. Jede Münze wiegt 5 g (1 kg = 1 000 g). Die Zahl der Münzen lässt sich als 10ⁿ schreiben. Wie groß ist n?",
    5, "5", lambda: next(n for n in range(0, 20) if 10 ** n * 5 == 500 * 1000),
    "500 kg sind 500 · 1 000 g = 500 000 g. Dann gibt es 500 000 : 5 = 100 000 Münzen. 100 000 = 10⁵, denn 100 000 ist eine 1 mit 5 Nullen. Also ist n = 5.",
    [(6, "Die Ziffern der Zahl gezählt statt der Nullen (5 + 1)", "5 + 1"), (4, "Beim Teilen durch 5 eine Null verloren (5 − 1)", "5 - 1"), (3, "Nur die Nullen von 500 gezählt und 1 000 vergessen (2 + 1)", "2 + 1")]), form="umkehren", regel=P)
neu(T, "zehner", "korrektur", "umkehr", Z(
    "Eine Zahl wird mit 10⁴ malgenommen. Das Ergebnis ist 370 000. Welche Zahl wurde malgenommen?",
    37, "370000 // 10 ** 4", lambda: next(n for n in range(1, 1000) if n * 10000 == 370000),
    "Malnehmen mit 10⁴ hängt 4 Nullen an. Rückwärts nimmst du 4 Nullen weg: 370 000 → 37. Probe: 37 · 10 000 = 370 000.",
    [(37000, "Nur durch 10 geteilt (eine Null weggenommen)", "370000 // 10"), (3700, "Nur zwei Nullen weggenommen (durch 10²)", "370000 // 10 ** 2"), (370, "Nur drei Nullen weggenommen (durch 10³)", "370000 // 10 ** 3")]), form="umkehren", regel=P)
neu(T, "zehner", "sicherung", "umkehr", Z(
    "Ein Land hat 10⁶ Einwohner. Das sind 10²-mal so viele wie in der Stadt. Die Stadt hat 10-mal so viele Einwohner wie das Dorf. Wie viele Einwohner hat das Dorf?",
    1000, "10 ** 6 // 10 ** 2 // 10", lambda: 1000000 // 100 // 10,
    "Land: 10⁶ = 1 000 000. Stadt: 1 000 000 : 10² = 10 000. Dorf: 10 000 : 10 = 1 000. Mit Potenzen: Rückwärts werden die Hochzahlen abgezogen: 6 − 2 − 1 = 3, also 10³.",
    [(10000, "Nur durch 10² geteilt: das Dorf mit der Stadt verwechselt", "10 ** 6 // 10 ** 2"), (100000, "Nur durch 10 geteilt", "10 ** 6 // 10"), (100, "Durch 10³ statt 10² und dann durch 10 geteilt", "10 ** 6 // 10 ** 3 // 10")], einheit="Einwohner"), form="umkehren", regel=P)
neu(T, "zehner", "sicherung", "transfer", Z(
    "Licht legt in 1 Sekunde etwa 3 · 10⁵ km zurück. Wie viele Kilometer sind das in 1 Minute (60 Sekunden)?",
    18000000, "3 * 10 ** 5 * 60", lambda: sum(300000 for _ in range(60)),
    "In einer Minute sind es 60-mal so viele Kilometer: 3 · 10⁵ · 60 = 180 · 10⁵ = 18 000 000. Rechne zuerst 3 · 60 = 180 und hänge dann 5 Nullen an.",
    [(1800000, "Eine Null verloren: nur 4 Nullen an die 180 angehängt", "180 * 10 ** 4"), (180000000, "Eine Null zu viel: 6 Nullen an die 180 angehängt", "180 * 10 ** 6"), (300060, "60 addiert statt malgenommen", "3 * 10 ** 5 + 60")], einheit="km"), form="anwenden", regel=P)
neu(T, "zehner", "sicherung", "parameter", Z(
    "Für welche größte natürliche Zahl n ist 10ⁿ kleiner als 1 000 000? („Kleiner als“ heißt: Gleich große Zahlen zählen nicht.)",
    5, "6 - 1", lambda: max(n for n in range(0, 30) if 10 ** n < 1000000),
    "10⁵ = 100 000 ist kleiner als 1 000 000. 10⁶ = 1 000 000 ist nicht kleiner, sondern gleich groß. Also ist n = 5 die größte passende Zahl.",
    [(6, "Die Nullen von 1 000 000 gezählt (7 Ziffern − 1); 10⁶ ist aber nicht kleiner als 1 000 000", "7 - 1"),
     (7, "Die Ziffern von 1 000 000 gezählt (6 Nullen + 1)", "6 + 1"),
     (4, "Eine Hochzahl zu klein: nur bis 10⁴ gegangen (5 − 1)", "5 - 1")]), form="umkehren", regel=P)
# ═════════ sach ═════════
neu(T, "sach", "test", "rueckwaerts", Z(
    "Eine Wasserpflanze verdreifacht jeden Tag ihre Blattzahl. Nach 4 Tagen hat sie 405 Blätter. Wie viele Blätter hatte sie am Anfang?",
    5, "405 // 3 ** 4", lambda: next(a for a in range(1, 405) if a * 3 * 3 * 3 * 3 == 405),
    "In 4 Tagen wurde 4-mal mit 3 malgenommen, also mit 3⁴ = 81. Rückwärts: 405 : 81 = 5. Probe: 5 → 15 → 45 → 135 → 405.",
    [(135, "Nur einmal durch 3 geteilt", "405 // 3"), (1215, "Weiter verdreifacht statt zurückgerechnet: 405 · 3", "405 * 3"), (401, "Die 4 Tage abgezogen: 405 − 4", "405 - 4")], einheit="Blätter"), form="umkehren", regel=P)
neu(T, "sach", "korrektur", "umkehr", Z(
    "Ein Papierstreifen wird mehrmals hintereinander in der Mitte gefaltet. Bei jeder Faltung liegen doppelt so viele Lagen übereinander wie vorher. Am Ende liegen 64 Lagen übereinander. Wie oft wurde gefaltet?",
    6, "6", lambda: next(n for n in range(0, 20) if 2 ** n == 64),
    "Am Anfang ist 1 Lage da. Nach jeder Faltung doppelt so viele: 2, 4, 8, 16, 32, 64. Das sind 6 Faltungen, denn 2⁶ = 64.",
    [(32, "64 durch 2 geteilt", "64 // 2"), (62, "2 von 64 abgezogen", "64 - 2"), (16, "64 durch 4 geteilt", "64 // 4")], einheit="Faltungen"), form="umkehren", regel=P)
neu(T, "sach", "korrektur", "umkehr", Z(
    "Ein Zahlenschloss hat mehrere Räder. Auf jedem Rad kann man eine der Ziffern 0 bis 9 einstellen. Insgesamt gibt es 10 000 verschiedene Einstellungen. Wie viele Räder hat das Schloss?",
    4, "5 - 1", lambda: next(n for n in range(1, 10) if 10 ** n == 10000),
    "Mit 1 Rad gibt es 10 Einstellungen, mit 2 Rädern 10 · 10 = 100, mit 3 Rädern 1 000, mit 4 Rädern 10 · 10 · 10 · 10 = 10⁴ = 10 000. Das Schloss hat 4 Räder.",
    [(5, "Die Ziffern von 10 000 gezählt (4 Nullen + 1)", "4 + 1"), (1000, "10 000 durch 10 geteilt", "10000 // 10"), (100, "10 000 durch 100 geteilt", "10000 // 100")]), form="umkehren", regel=P)
neu(T, "sach", "sicherung", "darstellung", W(
    "Die Tabelle zeigt, wie viele Mitglieder ein Netzwerk an den ersten Tagen hat. Welche Rechnung gibt die Zahl der Mitglieder am 6. Tag an?",
    "3⁶",
    [("6³", "Basis und Hochzahl vertauscht (6³ = 216)", 6 ** 3 != 3 ** 6),
     ("3 · 6", "Hochzahl als Malnehmer gedeutet (3 · 6 = 18)", 3 * 6 != 3 ** 6),
     ("3⁵", "Einen Tag zu wenig gezählt (am 1. Tag steht schon 3¹ da)", 3 ** 5 != 3 ** 6)],
    "Tag 1: 3 = 3¹. Tag 2: 9 = 3 · 3 = 3². Tag 3: 27 = 3 · 3 · 3 = 3³. Am Tag n steht die 3 genau n-mal als Faktor da. Am 6. Tag sind es 3⁶ = 729 Mitglieder.",
    3 ** 1 == 3 and 3 ** 2 == 9 and 3 ** 3 == 27 and 3 ** 6 == 729,
    grafik={"typ": "tabelle", "kopf": ["Tag", "1", "2", "3"], "zeilen": [["Mitglieder", "3", "9", "27"]]}), form="bruecke", regel=P)
neu(T, "sach", "sicherung", "verknuepfen", Z(
    "Kultur A hat am Anfang (Stunde 0) 100 Zellen und bekommt jede Stunde 100 Zellen dazu. Kultur B hat am Anfang 1 Zelle und verdoppelt sich jede Stunde. Nach wie vielen Stunden hat B zum ersten Mal mehr Zellen als A?",
    11, "11", lambda: next(n for n in range(0, 60) if 2 ** n > 100 + 100 * n),
    "Nach n Stunden hat A genau 100 + 100 · n Zellen, B hat 2ⁿ. Stunde 10: A hat 1 100, B hat 1 024: B ist noch kleiner. Stunde 11: A hat 1 200, B hat 2 048: B ist größer. Also nach 11 Stunden.",
    [(7, "B nur mit der Startzahl 100 von A verglichen: 2⁷ ist die erste Zweierpotenz über 100", "7"),
     (10, "B mit zehn Hundertern verglichen: 2¹⁰ ist die erste Zweierpotenz darüber (Startzahl von A vergessen)", "10")], einheit="Stunden"), form="zwei_wege", regel=P)
neu(T, "sach", "sicherung", "begruenden", W(
    "Eine Algenart verdreifacht jeden Tag ihre Fläche. Am Anfang bedeckt sie 2 m². Nina rechnet die Fläche nach 4 Tagen so: 2 · 3 = 6, dann 6⁴ = 1 296 m². Welche Aussage über Ninas Rechnung stimmt?",
    "Fehler: Sie hat 2 und 3 zu 6 zusammengefasst und dann 6⁴ gerechnet. Richtig wäre 2 · 3⁴ = 162 m².",
    [("Fehler: Sie hat 2 und 3 zu 6 zusammengefasst. Richtig wäre 2 · 3 · 4 = 24 m².", "Hochzahl als Malnehmer gedeutet (2 · 3 · 4 = 24)", 2 * 3 * 4 != 2 * 3 ** 4),
     ("Fehler: Die Anfangsfläche zählt nicht mit. Richtig wäre 3⁴ = 81 m².", "Anfangsfläche weggelassen (3⁴ = 81)", 3 ** 4 != 2 * 3 ** 4),
     ("Kein Fehler: 6⁴ = 1 296 m² ist richtig.", "Das Zusammenfassen von 2 und 3 für erlaubt gehalten (6⁴ = 1 296)", 6 ** 4 == 1296 and 6 ** 4 != 2 * 3 ** 4)],
    "Nach 4 Tagen wurde 4-mal mit 3 malgenommen: 2 · 3 · 3 · 3 · 3 = 2 · 81 = 162 m². Die 2 gehört nicht unter die Hochzahl: Nur die 3 wird 4-mal malgenommen. 6⁴ würde bedeuten, dass sich die Fläche 4-mal um den Faktor 6 vergrößert.",
    2 * 3 ** 4 == 162), regel=P)
neu(T, "sach", "korrektur", "darstellung", W(
    "Eine Zahl verdoppelt sich 5-mal hintereinander. Sie startet bei 3. Welche Rechnung gibt das Ergebnis an?",
    "3 · 2⁵",
    [("(3 · 2)⁵", "Die Startzahl mit in die Hochzahl-Klammer genommen (6⁵ = 7 776)", (3 * 2) ** 5 != 3 * 2 ** 5),
     ("3⁵ · 2", "Basis und Faktor vertauscht (3⁵ · 2 = 486)", 3 ** 5 * 2 != 3 * 2 ** 5),
     ("3 · 2 · 5", "Hochzahl als Malnehmer gedeutet (3 · 2 · 5 = 30)", 3 * 2 * 5 != 3 * 2 ** 5)],
    "Jede Verdopplung heißt: mal 2. Fünfmal verdoppeln heißt 5-mal mit 2 malnehmen: 3 · 2 · 2 · 2 · 2 · 2 = 3 · 2⁵ = 3 · 32 = 96. Die 3 steht nur einmal da, sie gehört nicht unter die Hochzahl.",
    3 * 2 * 2 * 2 * 2 * 2 == 3 * 2 ** 5 == 96), form="bruecke", regel=P)
