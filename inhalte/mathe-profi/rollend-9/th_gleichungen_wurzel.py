T = "gleichungen.wurzel"
ER = "id.algebra.erlaubte_zahlen"
GL = "id.algebra.gleichung_loesen"
# ───────── definitionsmenge ─────────
neu(T, "definitionsmenge", "lueckenweg", L(
    "Bestimme die Definitionsmenge von √(3x − 15) über ℝ. Der Radikand darf nicht negativ sein. Der Radikand ist null für x = ①. Dann ist die größte ganze Zahl, die nicht in D liegt, gleich ②. Also liegen von den Zahlen 1 bis 10 genau ③ in D.",
    KOMM(3), [5, 4, 6], ["15 // 3", "{1} - 1", "10 - {1} + 1"], ["15 / 3", "15 / 3 - 1", "10 - 15 / 3 + 1"],
    "Löse 3x − 15 = 0 wie eine Waage. Ab dieser Zahl ist der Radikand nicht mehr negativ.",
    "3x − 15 = 0 gilt für x = 5. Für x ≥ 5 ist der Radikand nicht negativ, also D = {x | x ≥ 5}. Die größte ganze Zahl außerhalb ist 4. Von 1 bis 10 liegen die Zahlen 5, 6, 7, 8, 9, 10 in D, das sind 6.",
    {0: [(-5, None, "beim Umstellen von 3x − 15 = 0 die 15 mit Minus auf die andere Seite gebracht: 3x = −15 und x = −15 : 3", "-15 / 3"), (45, None, "mit 3 malgenommen statt geteilt: 15 · 3", "15 * 3")], 1: [(5, None, "die kleinste Zahl von D angegeben statt der größten Zahl außerhalb", "{1}")], 2: [(10, None, "alle zehn Zahlen gezählt", "10")]}), regel=ER)
neu(T, "definitionsmenge", "bruecke", W(
    "Der Zahlenstrahl zeigt die Definitionsmenge D einer Wurzel √T. Der schattierte Bereich gehört dazu und geht nach rechts weiter. Welcher Term T gehört dazu?",
    "x − 2", [("2 − x", "die Richtung vertauscht: dann wäre D = {x | x ≤ 2}"), ("x + 2", "die Grenze auf der falschen Seite von null: dann wäre die Grenze −2"), ("x − 6", "die falsche Zahl abgezogen: dann wäre die Grenze 6")],
    "Der Radikand darf nicht negativ sein. Setze eine Zahl links und eine rechts der Grenze ein.",
    "D beginnt bei 2 und geht nach rechts. Für T = x − 2 gilt x − 2 ≥ 0 genau für x ≥ 2. Bei 2 − x wäre der Bereich links von 2, bei x + 2 beginnt er bei −2, bei x − 6 bei 6.",
    lambda: all((x - 2 >= 0) == (x >= 2) for x in range(-5, 10)) and any((2 - x >= 0) != (x >= 2) for x in range(-5, 10)) and any((x + 2 >= 0) != (x >= 2) for x in range(-5, 10)) and any((x - 6 >= 0) != (x >= 2) for x in range(-5, 10)),
    grafik={"typ": "zahlenstrahl", "start": -4, "ende": 8, "abschnitte": 12, "bereich": {"von": 2, "bis": 8}, "beschriftet": "alle"}), g="darstellung", regel=ER)
neu(T, "definitionsmenge", "fehler_detektiv", FD(
    "Kim bestimmt die Definitionsmenge von √(10 − 2x) über ℝ.",
    [("Der Radikand darf nicht negativ sein: 10 − 2x ≥ 0, also 2x ≥ 10.", all(((10 - 2 * x) >= 0) == (2 * x >= 10) for x in range(-3, 12)), None),
     ("Daraus folgt x ≥ 5.", False, all((2 * x >= 10) == (x >= 5) for x in range(-3, 12))),
     ("Also ist D = {x | x ≥ 5}.", False, True)],
    "Prüfe die Aussage jeder Zeile an einer Zahl, die du selbst wählst.",
    "Zeile 1 enthält den Fehler: Aus 10 − 2x ≥ 0 folgt 10 ≥ 2x, also x ≤ 5. Die Zeilen 2 und 3 folgen aus Zeile 1 richtig weiter. Richtig ist D = {x | x ≤ 5}. Probe: x = 6 gibt 10 − 12 = −2 < 0."), regel=ER)

# ───────── quadrieren ─────────
neu(T, "quadrieren", "lueckenweg", L(
    "Löse √(2x + 1) = 5. Beide Seiten werden quadriert: 2x + 1 = ①. Dann ist 2x = ②. Also ist x = ③.",
    KOMM(3), [25, 24, 12], ["5 ** 2", "{1} - 1", "{2} // 2"], ["5 * 5", "5 * 5 - 1", "(5 * 5 - 1) / 2"],
    "Quadrieren heißt: beide Seiten mit sich selbst malnehmen.",
    "(√(2x + 1))² = 2x + 1 und 5² = 25. Aus 2x + 1 = 25 folgt 2x = 24 und x = 12. Probe: √(2 · 12 + 1) = √25 = 5.",
    {0: [(10, None, "5 verdoppelt statt quadriert: 5 · 2", "5 * 2")], 1: [(26, None, "1 addiert statt abgezogen: 25 + 1", "{1} + 1")], 2: [(12.5, None, "die 1 vergessen: 25 : 2", "{1} / 2")]}), regel=GL)
neu(T, "quadrieren", "umkehren", Z(
    "Für welche Zahl a hat die Gleichung √(x + a) = 5 die Lösung x = 11?",
    14, "5 ** 2 - 11", lambda: next(a for a in range(-50, 50) if 11 + a >= 0 and math.isqrt(11 + a) ** 2 == 11 + a and math.isqrt(11 + a) == 5),
    "Setze x = 11 ein. Dann steht eine Wurzel, die den Wert 5 haben muss.",
    "Mit x = 11 gilt √(11 + a) = 5. Quadrieren: 11 + a = 25. Also a = 14. Probe: √(11 + 14) = √25 = 5.",
    [(36, None, "11 addiert statt abgezogen: 25 + 11", "5 ** 2 + 11"), (16, None, "ohne Quadrieren gerechnet: 5 + 11", "5 + 11"), (-14, None, "in der falschen Reihenfolge abgezogen: 11 − 25 statt 25 − 11", "11 - 25")]), g="umkehr", regel=GL)
neu(T, "quadrieren", "fehler_detektiv", FD(
    "Kim löst √(x − 1) + 3 = 7.",
    [("√(x − 1) = 7 − 3 = 4", 7 - 3 == 4, None),
     ("Quadrieren: x − 1 = 4² = 8", 4 ** 2 == 8, None),
     ("Also ist x = 8 + 1 = 9.", False, 8 + 1 == 9)],
    "Lies die Zeilen der Reihe nach und rechne jede Zeile selbst nach.",
    "Zeile 1 stimmt. In Zeile 2 steht der Fehler: 4² = 16, nicht 8. Richtig: x − 1 = 16, also x = 17. Zeile 3 rechnet mit 8 richtig weiter. Probe: √(17 − 1) + 3 = 4 + 3 = 7."), regel=GL)

# ───────── isolieren ─────────
neu(T, "isolieren", "lueckenweg", L(
    "Löse 2 + √(3x) = 8. Zuerst wird die Wurzel allein gestellt: √(3x) = ①. Dann wird quadriert: 3x = ②. Also ist x = ③.",
    KOMM(3), [6, 36, 12], ["8 - 2", "{1} ** 2", "{2} // 3"], ["8 - 2", "(8 - 2) * (8 - 2)", "(8 - 2) * (8 - 2) / 3"],
    "Bringe zuerst die Zahl vor der Wurzel auf die andere Seite. Quadriere erst danach.",
    "2 + √(3x) = 8 gibt √(3x) = 6. Quadrieren: 3x = 36. Also x = 12. Probe: 2 + √(3 · 12) = 2 + 6 = 8.",
    {0: [(10, None, "2 addiert statt abgezogen: 8 + 2", "8 + 2")], 1: [(18, None, "mit 3 malgenommen statt quadriert: 6 · 3", "{1} * 3")], 2: [(36, None, "nicht durch 3 geteilt", "{2}")]}), regel=GL)
neu(T, "isolieren", "zwei_wege", Z(
    "Löse 3 · √x − 5 = 10 auf zwei Wegen. Weg A: Stelle die Wurzel durch Umformen allein und quadriere. Weg B: Lege eine Wertetabelle an, in der du für x der Reihe nach Quadratzahlen einsetzt (4, 9, 16, …), und lies ab, wann der Term den Wert 10 hat. Wie groß ist x?",
    25, "((10 + 5) / 3) ** 2", lambda: next(x for x in (n * n for n in range(1, 40)) if 3 * math.isqrt(x) - 5 == 10),
    "Beide Wege müssen dasselbe x ergeben.",
    "Weg A: 3√x = 15, √x = 5, x = 25. Weg B: Für x = 16 ist 3 · 4 − 5 = 7. Für x = 25 ist 3 · 5 − 5 = 10. Probe: 3 · √25 − 5 = 10.",
    [(5, None, "die Wurzel √x = 5 als Ergebnis genommen, nicht quadriert", "(10 + 5) / 3"), (225, None, "nicht durch 3 geteilt: 15 quadriert", "(10 + 5) ** 2"), (15, None, "nur 5 addiert: 10 + 5", "10 + 5")]), regel=GL)
neu(T, "isolieren", "anwenden", Z(
    "Ein Stein fällt von einer Brücke ins Wasser. Den Aufprall hört man 3,1 s nach dem Loslassen. Der Schall braucht für den Rückweg etwa 0,1 s. Für die Fallzeit t (in s) aus der Höhe h (in m) gilt vereinfacht t = √(h : 5). Wie hoch ist die Brücke über dem Wasser?",
    45, "(3.1 - 0.1) ** 2 * 5", lambda: (F(31, 10) - F(1, 10)) ** 2 * 5,
    "Welche Zeit gehört zur Fallbewegung allein? Danach brauchst du die Formel.",
    "Fallzeit: 3,1 − 0,1 = 3 s. Aus 3 = √(h : 5) folgt 9 = h : 5, also h = 45 m.",
    [(48.05, None, "den Schall nicht abgezogen: 3,1² · 5", "3.1 ** 2 * 5"), (9, None, "nicht mit 5 malgenommen: 3²", "(3.1 - 0.1) ** 2"), (15, None, "nicht quadriert: 3 · 5", "(3.1 - 0.1) * 5")], "m"), g="transfer", regel=GL)

# ───────── probe ─────────
neu(T, "probe", "verfahren_waehlen", W(
    "Du löst √(2x + 9) = x + 3 durch Quadrieren und erhältst die Kandidaten x = 0 und x = −4. Womit machst du die Probe?",
    "Beide Zahlen in die Ausgangsgleichung √(2x + 9) = x + 3 einsetzen.",
    [("Beide Zahlen in die quadrierte Gleichung 2x + 9 = (x + 3)² einsetzen.", "mit der umgeformten Gleichung geprüft: Dort stimmen beide Zahlen immer, weil sie daraus entstanden sind"),
     ("Nur die kleinere Zahl prüfen, denn Quadrieren macht die Lösungen kleiner.", "eine Regel erfunden, die es nicht gibt"),
     ("Keine Probe machen: Quadrieren ändert die Lösungsmenge nie.", "Quadrieren ist keine Äquivalenzumformung und kann Scheinlösungen erzeugen")],
    "Quadrieren kann Zahlen hinzufügen, die zur ursprünglichen Gleichung nicht passen. Welche Gleichung ist die ursprüngliche?",
    "Probe in der Ausgangsgleichung: x = 0 gibt √9 = 3 und 0 + 3 = 3, das stimmt. x = −4 gibt √1 = 1, aber −4 + 3 = −1. Das stimmt nicht. Also ist x = −4 eine Scheinlösung. In der quadrierten Gleichung würden beide Zahlen passen.",
    lambda: math.sqrt(9) == 3 and math.sqrt(1) != -1 and 2 * (-4) + 9 == (-4 + 3) ** 2), g="erkennen", regel=GL)
neu(T, "probe", "zwei_wege", Z(
    "Löse √(x + 20) = x über ℝ und vergleiche zwei Absicherungen. Weg A (Einsetzprobe danach): Quadriere, löse die entstehende Gleichung und setze beide Kandidaten in die Ausgangsgleichung ein. Weg B (Vorzeichenbedingung vor dem Quadrieren): Halte zuerst fest, dass die rechte Seite nicht negativ sein darf. Quadriere dann und behalte nur Kandidaten, die diese Bedingung erfüllen. Wie lautet die Lösung?",
    5, "(1 + 9) / 2", lambda: next(x for x in range(0, 100) if x * x == x + 20),
    "Beide Wege müssen dieselbe Lösung ergeben.",
    "Quadrieren: x + 20 = x², also x² − x − 20 = 0 mit den Kandidaten 5 und −4. Weg A: √25 = 5 stimmt. Für x = −4 steht links √16 = 4, rechts −4, das stimmt nicht. Weg B: Die rechte Seite x muss ≥ 0 sein, also fällt −4 weg. Die Lösung ist x = 5.",
    [(-4, None, "die Scheinlösung genommen: (1 − 9) : 2", "(1 - 9) / 2"), (10, None, "den Zähler der Lösung nicht durch 2 geteilt: 1 + 9", "1 + 9"), (20, None, "die Zahl aus der Gleichung abgeschrieben", "20")]), regel=GL)
neu(T, "probe", "fehler_detektiv", FD(
    "Kim löst √(x + 12) = x.",
    [("Quadrieren: x + 12 = x².", all((4 + 12 == 4 ** 2, -3 + 12 == (-3) ** 2)), None),
     ("Umstellen gibt x² − x − 12 gleich null. Die Lösungen sind x = 4 und x = −3.", all((4 ** 2 - 4 - 12 == 0, (-3) ** 2 + 3 - 12 == 0)), None),
     ("Probe mit der quadrierten Gleichung: 4 + 12 = 4² und −3 + 12 = (−3)². Also lösen beide Zahlen die Ausgangsgleichung.", math.sqrt(-3 + 12) == -3, None),
     ("Also ist L = {−3; 4}.", False, True)],
    "Lies die Zeilen der Reihe nach und prüfe, ob jede Aussage wirklich folgt.",
    "Zeile 1 und 2 stimmen. In Zeile 3 wurde mit der quadrierten Gleichung geprüft. Die Probe muss in der Ausgangsgleichung stattfinden: x = 4 gibt √16 = 4 ✓. x = −3 gibt √9 = 3, aber rechts steht −3. Das stimmt nicht. Richtig ist L = {4}. Zeile 4 folgt aus Zeile 3."), regel=GL)

# ───────── zwei_seiten ─────────
neu(T, "zwei_seiten", "lueckenweg", L(
    "Löse √(x + 8) = √(3x − 4). Quadrieren gibt x + 8 = 3x − 4. Sortiert steht dort 2x = ①. Also ist x = ②. Dann ist der Radikand auf jeder Seite ③.",
    KOMM(3), [12, 6, 14], ["8 + 4", "{1} // 2", "{2} + 8"], ["8 + 4", "(8 + 4) / 2", "(8 + 4) / 2 + 8"],
    "Bringe alle x auf eine Seite und alle Zahlen auf die andere Seite.",
    "x + 8 = 3x − 4 gibt 12 = 2x, also x = 6. Radikand links: 6 + 8 = 14. Radikand rechts: 3 · 6 − 4 = 14. Beide Seiten sind gleich, also ist x = 6 eine Lösung.",
    {0: [(4, None, "8 − 4 gerechnet", "8 - 4")], 1: [(12, None, "nicht durch 2 geteilt", "{1}")], 2: [(26, None, "rechte Seite falsch gerechnet: 3 · 6 + 8", "3 * {2} + 8")]}), regel=GL)
neu(T, "zwei_seiten", "umkehren", Z(
    "Für welche Zahl a hat die Gleichung √(x + a) = √(2x − 1) die Lösung x = 5?",
    4, "2 * 5 - 1 - 5", lambda: next(a for a in range(-20, 20) if 5 + a == 2 * 5 - 1),
    "Setze x = 5 ein. Die rechte Seite lässt sich ausrechnen.",
    "Rechts: 2 · 5 − 1 = 9. Links muss auch 9 unter der Wurzel stehen: 5 + a = 9. Also a = 4. Probe: √9 = √9.",
    [(9, None, "nur die rechte Seite gerechnet: 2 · 5 − 1", "2 * 5 - 1"), (6, None, "5 + 1 gerechnet", "5 + 1"), (-4, None, "in der falschen Reihenfolge abgezogen: 5 − 9 statt 9 − 5", "5 - 9")]), g="umkehr", regel=GL)
neu(T, "zwei_seiten", "bruecke", W(
    "Die Zeichnung zeigt die Graphen von y = √x und y = x − 2. Quadrieren von √x = x − 2 führt auf die Kandidaten x = 1 und x = 4. Welche Aussage über die Gleichung √x = x − 2 stimmt?",
    "Nur x = 4 ist Lösung. Bei x = 1 liegt die Gerade unter der x-Achse, die Wurzelkurve darüber.",
    [("Beide Kandidaten sind Lösungen, denn beide stammen aus der quadrierten Gleichung.", "die Probe in der Ausgangsgleichung nicht gemacht"), ("Nur x = 1 ist Lösung, denn √1 = 1.", "nur die linke Seite berechnet: rechts steht bei x = 1 aber −1"), ("Es gibt keine Lösung, weil die Graphen sich nur berühren.", "Die Graphen schneiden sich bei x = 4, sie berühren sich nicht; und auch ein Berührpunkt wäre eine Lösung, denn dort sind die y-Werte gleich")],
    "Eine Lösung ist eine Stelle, an der beide Graphen denselben y-Wert haben. Prüfe die Kandidaten im Bild.",
    "Bei x = 4 haben beide Graphen den y-Wert 2: √4 = 2 und 4 − 2 = 2. Bei x = 1 ist √1 = 1, aber 1 − 2 = −1. Dort sind die y-Werte verschieden. Also ist x = 1 eine Scheinlösung.",
    lambda: math.sqrt(4) == 4 - 2 and math.sqrt(1) != 1 - 2,
    grafik=KO([-1, 6], [-3, 4], graphen=[{"art": "wurzel", "name": "y = √x"}, {"art": "linear", "m": 1, "t": -2, "name": "y = x − 2"}])), g="verknuepfen", regel=GL)

# ───────── sachaufgabe ─────────
neu(T, "sachaufgabe", "lueckenweg", L(
    "Für die Schwingdauer T (in s) eines Pendels der Länge l (in m) gilt vereinfacht T = 2 · √l. Ein Pendel soll 6 s schwingen. Dann ist √l = ①. Also ist l = ② m. Dann ist ein Pendel mit 8 s Schwingdauer um ③ m länger.",
    KOMM(3), [3, 9, 7], ["6 // 2", "{1} ** 2", "(8 // 2) ** 2 - {2}"], ["6 / 2", "(6 / 2) ** 2", "(8 / 2) ** 2 - (6 / 2) ** 2"],
    "Teile zuerst durch den Faktor vor der Wurzel. Die Länge folgt durch Quadrieren.",
    "6 = 2 · √l gibt √l = 3 und l = 9 m. Für 8 s: √l = 4 und l = 16 m. Der Unterschied ist 16 − 9 = 7 m.",
    {0: [(12, None, "mit 2 malgenommen statt geteilt: 6 · 2", "6 * 2")], 1: [(36, None, "die 6 quadriert statt √l", "6 ** 2")], 2: [(2, None, "nur die Schwingdauern verglichen: 8 − 6", "8 - 6"), (16, None, "die zweite Länge angegeben, nicht den Unterschied", "(8 // 2) ** 2")]}), regel=GL)
neu(T, "sachaufgabe", "anwenden", Z(
    "Für die Fläche A (in m²) eines quadratischen Teppichs gilt: Seitenlänge = √A. Ein quadratischer Raum ist 6 m breit. Der Teppich liegt so, dass ringsum 0,5 m Rand frei bleibt. Wie groß ist die Fläche A des Teppichs?",
    25, "(6 - 1) ** 2", lambda: (F(6) - 2 * F(1, 2)) ** 2,
    "Rand gibt es auf zwei gegenüberliegenden Seiten. Rechne erst die Seitenlänge des Teppichs aus.",
    "Die Seite des Teppichs ist 6 − 0,5 − 0,5 = 5 m lang. Also √A = 5 und A = 25 m².",
    [(35, None, "die Fläche des Raums genommen und 1 abgezogen", "6 ** 2 - 1"), (30.25, None, "nur einmal 0,5 m abgezogen: 5,5²", "5.5 ** 2"), (5, None, "die Seitenlänge statt der Fläche angegeben: 6 − 1", "6 - 1")], "m²"), g="einkleidung", regel=GL)
neu(T, "sachaufgabe", "fehler_detektiv", FD(
    "Kim berechnet die Länge l eines Pendels mit der Schwingdauer T = 5 s. Es gilt T = 2 · √l mit l in Metern.",
    [("2 · √l = 5", True, None), ("√l = 5 : 2 = 2,5", F(5, 2) == F("2.5"), None), ("l = 2,5² = 6,25", F("2.5") ** 2 == F("6.25"), None), ("Das Pendel ist 6,25 cm lang.", False, None)],
    "Lies die Zeilen der Reihe nach. Prüfe jede Zeile gegen die Angaben der Aufgabe.",
    "Die Zeilen 1 bis 3 stimmen: l = 6,25. In Zeile 4 steht die falsche Einheit. l ist in Metern angegeben, das Pendel ist also 6,25 m lang."), regel=GL)
