T = "gleichungen.bruch"
D = "ℚ \\ "
# ───────── definitionsmenge ─────────
neu(T, "definitionsmenge", "lueckenweg", L(
    "Bestimme die Definitionsmenge von 7/(2x − 10) = 1/(3x + 12). Setze jeden Nenner gleich 0. Der erste Nenner ist 0 für x = ①. Der zweite Nenner ist 0 für x = ②. Das Produkt dieser beiden verbotenen Zahlen ist ③.",
    KOMM(3), [5, -4, -20], ["10 // 2", "-12 // 3", "{1} * {2}"], ["5", "-4", "-20"], "Löse jede Nenner-Gleichung wie eine Waage.",
    "2x − 10 = 0 ergibt x = 5. 3x + 12 = 0 ergibt x = −4. 5 · (−4) = −20. D = ℚ \\ {−4; 5}.",
    {1: [(4, "fb.vorzeichen.falsches_zeichen", "das Minus der Lösung vergessen", "12 // 3"), (-12, "fb.waage.nur_ein_summand", "die 12 nicht durch 3 geteilt", "-12")], 0: [(10, None, "durch 2 nicht geteilt", "10")], 2: [(20, "fb.vorzeichen.falsches_zeichen", "das Minus des Produkts vergessen: 5 · 4", "5 * 4")]}), regel="id.algebra.erlaubte_zahlen")
neu(T, "definitionsmenge", "umkehren", W(
    "Welche dieser Gleichungen hat die Definitionsmenge ℚ \\ {−5; 2}?",
    "3/(x − 2) = 7/(x + 5)", [("3/(x + 2) = 7/(x − 5)", "die Vorzeichen der verbotenen Zahlen vertauscht"), ("3/(x − 2) = 7/x", "die zweite verbotene Zahl durch 0 ersetzt"), ("3/(x − 2) = (x + 5)/7", "nur eine verbotene Zahl, weil rechts kein x im Nenner steht")],
    "Welche Zahl macht welchen Nenner zu 0? Das müssen genau −5 und 2 sein.",
    "x − 2 ist 0 für x = 2. x + 5 ist 0 für x = −5. Nur die Gleichung 3/(x − 2) = 7/(x + 5) schließt genau diese beiden Zahlen aus.",
    lambda: pole("3/(x-2)", "7/(x+5)") == {-5, 2} and pole("3/(x+2)", "7/(x-5)") != {-5, 2} and pole("3/(x-2)", "7/x") != {-5, 2} and pole("3/(x-2)", "(x+5)/7") != {-5, 2}), g="umkehr", regel="id.algebra.erlaubte_zahlen")
neu(T, "definitionsmenge", "verfahren_waehlen", W(
    "Du sollst die Definitionsmenge von 5/(x² − 4) = 1 bestimmen. Welcher Weg ist richtig?",
    "Den Nenner gleich 0 setzen: x² − 4 = 0 hat die Lösungen 2 und −2. Beide werden ausgeschlossen.",
    [("Den Nenner gleich 0 setzen: x² − 4 = 0 führt zu x = 2. Nur 2 wird ausgeschlossen.", "die zweite Lösung der Quadratgleichung vergessen"), ("Den Zähler gleich 0 setzen: 5 ist nie 0, also wird keine Zahl ausgeschlossen.", "Zähler und Nenner verwechselt"), ("Die Gleichung zuerst lösen und die Lösung ausschließen.", "die Definitionsmenge hängt nicht von der Lösung ab")],
    "Die Definitionsmenge steht fest, bevor du die Gleichung löst. Was darf im Nenner nie herauskommen?",
    "x² − 4 = 0 gilt für x = 2 und für x = −2. Beide Zahlen machen den Nenner zu 0. D = ℚ \\ {−2; 2}.",
    lambda: pole("5/(x**2-4)") == {-2, 2}), g="erkennen", regel="id.algebra.erlaubte_zahlen")

# ───────── ein_bruch ─────────
neu(T, "ein_bruch", "lueckenweg", L(
    "Löse 48/(3x) = 2 (x ≠ 0). Kürze zuerst den Bruch links mit 3. Der Zähler des gekürzten Bruchs ist ①. Dann ist x = ②. Der Nenner 3x hat für dieses x den Wert ③.",
    KOMM(3), [16, 8, 24], ["48 // 3", "{1} // 2", "3 * {2}"], ["16", "8", "24"], "Aus dem gekürzten Bruch folgt: mit x multiplizieren, dann durch die Zahl rechts teilen.",
    "48 : 3 = 16. Aus 16/x = 2 folgt 16 = 2x und x = 8. Probe: 48/24 = 2.",
    {0: [(144, None, "mit 3 malgenommen statt gekürzt", "48 * 3")], 1: [(32, None, "16 mit 2 malgenommen statt geteilt", "{1} * 2")]}), regel="id.algebra.gleichung_loesen")
neu(T, "ein_bruch", "zwei_wege", Z(
    "Löse 18/x = 3 (x ≠ 0) auf zwei Wegen. Weg A: beide Seiten mit x multiplizieren und dann durch 3 teilen. Weg B: auf beiden Seiten den Kehrwert bilden und dann mit 18 malnehmen. Wie groß ist x?",
    6, "18 / 3", "18 * (1 / 3)", "Beide Wege müssen dasselbe x ergeben.",
    "Weg A: 18 = 3x, also x = 6. Weg B: x/18 = 1/3, also x = 18 · 1/3 = 6. Probe: 18 : 6 = 3.",
    [(54, "fb.waage.nur_eine_seite", "18 · 3 gerechnet", "18 * 3"), (15, None, "18 − 3 gerechnet", "18 - 3")]), regel="id.algebra.gleichung_loesen")
assert ist_loesung("18/x", "3", 6) and ist_loesung("x/18", "1/3", 6)
neu(T, "ein_bruch", "anwenden", Z(
    "Ein Wasserhahn füllt einen Eimer mit 90 Litern in x Minuten. Dabei fließen gleichmäßig 90/x Liter in jeder Minute. Es sollen 15 Liter in jeder Minute fließen. Wie viele Minuten dauert das Füllen?",
    6, "90 / 15", 6, "Stelle die Gleichung 90/x = 15 auf. Multipliziere dann mit x.",
    "90/x = 15 ergibt 90 = 15x und x = 6. Das Füllen dauert 6 Minuten.",
    [(1350, "fb.waage.nur_eine_seite", "90 · 15 gerechnet", "90 * 15"), (75, None, "90 − 15 gerechnet", "90 - 15")], "min"), g="einkleidung", regel="id.algebra.gleichung_loesen")

# ───────── ueber_kreuz ─────────
neu(T, "ueber_kreuz", "lueckenweg", L(
    "Löse 6/(x + 1) = 4/(x − 1) (x ≠ −1 und x ≠ 1). Du multiplizierst über Kreuz und sortierst: die x links und die Zahlen rechts. Dann steht dort 2x = ①. Also ist x = ②.",
    KOMM(2), [10, 5], ["6 + 4", "{1} / 2"], ["10", "5"], "Über Kreuz: Zähler links mal Nenner rechts, Zähler rechts mal Nenner links.",
    "6(x − 1) = 4(x + 1), also 6x − 6 = 4x + 4. Dann 2x = 10 und x = 5. Probe: 6/6 = 1 und 4/4 = 1.",
    {0: [(2, "fb.waage.zeichen_nicht_gedreht", "6 − 4 gerechnet statt 6 + 4", "6 - 4")], 1: [(1, None, "mit dem falschen Wert 2 weitergerechnet: aus 2x = 2 folgt x = 1", "(6 - 4) / 2")]}), regel="id.algebra.gleichung_loesen")
neu(T, "ueber_kreuz", "fehler_detektiv", FD(
    "Kim löst 5/(x + 2) = 3/(x − 4) (x ≠ −2 und x ≠ 4).",
    [("Über Kreuz: 5(x − 4) = 3(x + 2)", ist_loesung("5*(x-4)", "3*(x+2)", 13)), ("Ausmultiplizieren: 5x − 20 = 3x + 6", ist_loesung("5*x-20", "3*x+6", 13)),
     ("Sortieren: 2x = 26", ist_loesung("2*x", "26", 13)), ("Teilen: x = 26 · 2 = 52", ist_loesung("x", "26*2", 13))],
    "Wie bekommst du x allein, wenn 2x = 26 dasteht? Mach die Probe.",
    "2x = 26 heißt: durch 2 teilen. x = 13. Probe: 5/15 = 1/3 und 3/9 = 1/3."), regel="rr.waage")
neu(T, "ueber_kreuz", "umkehren", Z(
    "Die Gleichung 6/(x + a) = 2/(x − 1) hat die Lösung x = 3. Wie groß ist die Zahl a?",
    3, "6 / (2 / (3 - 1)) - 3", 3, "Setze x = 3 ein und rechne die rechte Seite aus. Dann steht links 6/(3 + a) = dieser Wert.",
    "Rechts: 2/(3 − 1) = 1. Links: 6/(3 + a) = 1, also 3 + a = 6 und a = 3. Probe: 6/6 = 1.",
    [(6, "fb.waage.nur_ein_summand", "nur 3 + a = 6 gelesen, die 3 nicht abgezogen", "6"), (9, None, "6 + 3 gerechnet", "6 + 3")]), g="umkehr", regel="id.algebra.gleichung_loesen")

# ───────── hauptnenner ─────────
neu(T, "hauptnenner", "lueckenweg", L(
    "Löse 3/(2x) + 1/(3x) = 22/48 (x ≠ 0). Der Hauptnenner der linken Seite ist ①x. Erweitert hat der erste Bruch dann den Zähler ②. Der Zähler der Summe der beiden erweiterten Brüche ist ③. Setze die Summe gleich 22/48 und multipliziere über Kreuz. Dann ist x = ④.",
    KOMM(4), [6, 9, 11, 4], ["6", "3 * {1} // 2", "{2} + {1} // 3", "{3} * 48 // ({1} * 22)"], ["2 * 3", "9", "9 + 2", "(11 * 48) // (6 * 22)"], "Der Hauptnenner ist das kleinste gemeinsame Vielfache von 2 und 3, mal x. Über Kreuz: Zähler mal Nenner der anderen Seite.",
    "HN = 6x. 3/(2x) = 9/(6x) und 1/(3x) = 2/(6x). Summe: 11/(6x). Aus 11/(6x) = 22/48 folgt 11 · 48 = 22 · 6x, also 528 = 132x und x = 4. Probe: 3/8 + 1/12 = 9/24 + 2/24 = 11/24 = 22/48.",
    {0: [(5, "fb.bruchrechnen.zaehler_und_nenner_addiert", "2 + 3 gerechnet", "2 + 3")], 1: [(3, None, "den Zähler nicht mit erweitert", "3")], 2: [(4, None, "die Zähler nicht mit erweitert: 3 + 1", "3 + 1")],
     3: [(24, "fb.waage.nur_eine_seite", "nur 11 · 48 : 22 gerechnet und nicht durch 6 geteilt", "{3} * 48 // 22")]}), regel="rr.bruchrechnen")
neu(T, "hauptnenner", "zwei_wege", Z(
    "Löse 1/x + 1/(2x) = 3/2 (x ≠ 0) auf zwei Wegen. Weg A: erst die Brüche links zusammenfassen. Weg B: beide Seiten sofort mit dem Hauptnenner 2x multiplizieren. Wie groß ist x?",
    1, "3 / 3", 1, "Beide Wege müssen dasselbe x ergeben.",
    "Weg A: 2/(2x) + 1/(2x) = 3/(2x) = 3/2, also 2x = 2 und x = 1. Weg B: 2 + 1 = 3x, also x = 1.",
    [(3, "fb.waage.nur_eine_seite", "die Summe 2 + 1 = 3 als Ergebnis genommen, ohne nach x aufzulösen", "2 + 1"), (2, None, "die rechte Seite nur mit x statt mit 2x multipliziert: 3 = 3x/2", "3 / (3 / 2)")]), regel="rr.bruchrechnen")
assert ist_loesung("1/x+1/(2*x)", "3/2", 1)
neu(T, "hauptnenner", "bruecke", W(
    "Eine Pumpe füllt ein Becken allein in x Stunden. Eine zweite Pumpe braucht allein 2x Stunden. Beide Pumpen fördern gleichmäßig. Zusammen füllen sie das Becken in 4 Stunden. Welche Gleichung gehört dazu (x ≠ 0)?",
    "1/x + 1/(2x) = 1/4", [("x + 2x = 4", "die Zeiten statt der Füllanteile je Stunde addiert"), ("1/x + 1/(2x) = 4", "rechts die Zeit statt des Anteils je Stunde"), ("1/x · 1/(2x) = 1/4", "die Anteile malgenommen statt addiert")],
    "Was schafft jede Pumpe in einer Stunde? Diese Anteile werden addiert.",
    "Pumpe 1 schafft 1/x je Stunde, Pumpe 2 schafft 1/(2x). Zusammen 1/4 je Stunde. Daraus folgt 3/(2x) = 1/4 und x = 6.",
    lambda: ist_loesung("1/x+1/(2*x)", "1/4", 6) and not ist_loesung("x+2*x", "4", 6) and not ist_loesung("1/x+1/(2*x)", "4", 6) and not ist_loesung("1/x*1/(2*x)", "1/4", 6)), regel="rr.bruchrechnen")

# ───────── scheinloesung ─────────
neu(T, "scheinloesung", "lueckenweg", L(
    "Löse (3x − 1)/(2x − 8) = 11/(2x − 8). Beide Seiten haben denselben Nenner. Multipliziere mit diesem Nenner und sortiere: 3x = ①. Der einzige Kandidat ist dann x = ②. Für diese Zahl hat der Nenner 2x − 8 den Wert ③. Die Gleichung hat ④ Lösungen.",
    KOMM(4), [12, 4, 0, 0], ["11 + 1", "{1} // 3", "2 * {2} - 8", "min(1, abs({3}))"], ["12", "4", "0", "0"], "Aus gleichen Nennern folgt: Die Zähler müssen gleich sein. Ein Kandidat zählt nur, wenn der Nenner für ihn nicht null wird.",
    "3x − 1 = 11 ergibt 3x = 12 und den Kandidaten x = 4. Der Nenner ist 2 · 4 − 8 = 0. Die Zahl 4 liegt nicht in der Definitionsmenge, sie ist nur ein Kandidat und keine Lösung. Es gibt 0 Lösungen: L = { }.",
    {0: [(10, "fb.waage.zeichen_nicht_gedreht", "11 − 1 gerechnet", "11 - 1")], 2: [(8, None, "nur 2 · 4 gerechnet, die 8 nicht abgezogen", "2 * {2}")], 3: [(1, "fb.erlaubte_zahlen.nullstelle_des_nenners_als_loesung", "den Kandidaten 4 als Lösung gezählt, obwohl der Nenner 0 ist", False)]}, gleich_ok=True), regel="id.algebra.gleichung_loesen")
neu(T, "scheinloesung", "fehler_detektiv", FD(
    "Kim löst x/(x − 2) = 2/(x − 2) mit der Definitionsmenge ℚ \\ {2}.",
    [("Mit (x − 2) multiplizieren: x = 2", True), ("Die Zahl 2 gehört zur Lösung, weil die Rechnung x = 2 ergeben hat.", not undef("x/(x-2)", 2)), ("Also ist L = {2}.", True)],
    "Für x = 2 ist der Nenner x − 2 gleich …? Darf man dann einsetzen?",
    "Für x = 2 ist der Nenner 0. Die Zahl 2 liegt nicht in der Definitionsmenge. Sie ist eine Scheinlösung. Richtig: L = { }."), regel="id.algebra.gleichung_loesen")
neu(T, "scheinloesung", "umkehren", Z(
    "Für welche Zahl a ist x = 3 bei der Gleichung (x + a)/(x − 3) = 7/(x − 3) eine Scheinlösung? Beim Lösen kommt dabei x = 3 heraus.",
    4, "7 - 3", 4, "Wenn nach dem Multiplizieren x = 3 herauskommt, gilt x + a = 7 für x = 3.",
    "Nach dem Multiplizieren mit (x − 3) steht x + a = 7. Mit x = 3 folgt a = 4. Dann ist 3 eine Scheinlösung, denn der Nenner ist 0.",
    [(10, "fb.waage.zeichen_nicht_gedreht", "7 + 3 gerechnet", "7 + 3"), (7, None, "die rechte Zahl abgeschrieben", "7")]), g="rueckwaerts", regel="id.algebra.gleichung_loesen")

# ───────── verhaeltnis ─────────
neu(T, "verhaeltnis", "lueckenweg", L(
    "Löse x : 8 = 15 : 12. Über Kreuz multipliziert steht links 12x. Rechts steht ①. Dann ist x = ②. Das Verhältnis x : 8 lässt sich mit diesem x zu ③ : 4 kürzen.",
    KOMM(3), [120, 10, 5], ["8 * 15", "{1} // 12", "{2} // 2"], ["120", "10", "5"], "Das Produkt der Außenglieder ist gleich dem Produkt der Innenglieder.",
    "Außenglieder sind x und 12, Innenglieder sind 8 und 15. Es gilt 12x = 8 · 15 = 120, also x = 10. Dann ist 10 : 8 = 5 : 4.",
    {0: [(23, "fb.verhaeltnis.addiert_statt_malgenommen", "8 + 15 gerechnet", "8 + 15")], 1: [(1440, None, "120 mit 12 malgenommen statt durch 12 geteilt", "{1} * 12")]}), regel="rr.verhaeltnis")
neu(T, "verhaeltnis", "bruecke", W(
    "Die Tabelle zeigt ein Rezept. Für 450 g Mehl soll die Wassermenge x bestimmt werden. Welche Verhältnisgleichung gehört dazu?",
    "x : 450 = 180 : 300", [("x : 450 = 300 : 180", "Mehl und Wasser im zweiten Verhältnis vertauscht"), ("x : 300 = 180 : 450", "die gegebenen Zahlen falsch zugeordnet"), ("x · 450 = 180 · 300", "malgenommen statt Verhältnis gleichgesetzt")],
    "Gleiche Stoffe stehen in beiden Verhältnissen an derselben Stelle.",
    "x : 450 = 180 : 300. Über Kreuz: 300x = 450 · 180 = 81 000, also x = 270. Man braucht 270 ml Wasser.",
    lambda: ist_loesung("x/450", "180/300", 270) and not ist_loesung("x/450", "300/180", 270) and not ist_loesung("x/300", "180/450", 270) and not ist_loesung("x*450", "180*300", 270),
    grafik=TAB(["", "Mehl", "Wasser"], ["Rezept", "300 g", "180 ml"], ["gesucht", "450 g", "x"])), regel="rr.verhaeltnis")
neu(T, "verhaeltnis", "anwenden", Z(
    "Auf einer Karte sind 3 cm in Wirklichkeit 12 km. Eine Wanderstrecke ist in Wirklichkeit 50 km lang. Wie viele Zentimeter lang ist sie auf der Karte?",
    12.5, "50 * 3 / 12", "50 / 4", "Stelle eine Verhältnisgleichung auf: Kartenlänge zu Wirklichkeit ist immer gleich.",
    "x : 50 = 3 : 12. Über Kreuz: 12x = 150, also x = 12,5. Die Strecke ist 12,5 cm lang.",
    [(200, "fb.verhaeltnis.falsche_richtung", "Karte und Wirklichkeit vertauscht: 50 · 12 : 3", "50 * 12 / 3"), (15, "fb.verhaeltnis.addiert_statt_malgenommen", "3 + 12 gerechnet", "3 + 12")], "cm"), g="einkleidung", regel="rr.verhaeltnis")

# ───────── graphisch ─────────
neu(T, "graphisch", "lueckenweg", L(
    "Du löst 36/x = 4 (x ≠ 0) mit einer Wertetabelle. Für x = 3 hat 36/x den Wert ①. Für x = 18 hat 36/x den Wert ②. Der gesuchte Wert 4 liegt dazwischen und ist doppelt so groß wie ②. Bei dieser Zuordnung halbiert sich dann x gegenüber 18. Die Lösung ist x = ③. Von x = 3 bis zur Lösung wächst x um ④.",
    KOMM(4), [12, 2, 9, 6], ["36 // 3", "36 // 18", "18 // (4 // {2})", "{3} - 3"], ["12", "2", "9", "9 - 3"], "Teile 36 durch den x-Wert. Ist der gesuchte Wert doppelt so groß wie der Wert bei x = 18, so wird x halbiert.",
    "36 : 3 = 12 und 36 : 18 = 2. Der gesuchte Wert 4 ist das Doppelte von 2, also wird x von 18 auf die Hälfte 9 verkleinert. Probe: 36 : 9 = 4. Die Lösung ist x = 9. Von x = 3 bis 9 wächst x um 6.",
    {0: [(33, None, "36 − 3 gerechnet", "36 - 3")], 1: [(54, None, "36 + 18 gerechnet", "36 + 18")], 2: [(144, None, "36 · 4 gerechnet", "36 * 4")], 3: [(3, None, "von der Lösung 9 statt der Startstelle 3 die Zahl 6 abgezogen: 9 − 6", "{3} - 6")]}), regel="id.algebra.gleichung_loesen")
neu(T, "graphisch", "bruecke", W(
    "Die Zeichnung zeigt zwei Graphen. Sie gehören zu den beiden Seiten einer Gleichung. Welche Gleichung wird mit dem Schnittpunkt gelöst?",
    "8/x = 2", [("8/x = x", "die Gerade als y = x gelesen"), ("2/x = 8", "Zähler und Zahl vertauscht"), ("8/x + 2 = 0", "die Gerade als y = −2 gelesen")],
    "Eine Seite ist die Hyperbel, die andere die waagrechte Gerade. Lies ihre Gleichungen ab.",
    "Die Hyperbel gehört zu y = 8/x, die Gerade zu y = 2. Gleichsetzen: 8/x = 2. Der Schnittpunkt liegt bei x = 4.",
    lambda: ist_loesung("8/x", "2", 4) and not ist_loesung("8/x", "x", 4) and not ist_loesung("2/x", "8", 4) and not ist_loesung("8/x+2", "0", 4),
    grafik=KO([-7, 7], [-6, 6], graphen=[{"art": "hyperbel", "a": 8, "b": 0, "c": 0, "name": "y = 8/x"}, {"art": "linear", "m": 0, "t": 2, "name": "y = 2"}])), regel="id.funktionen.zuordnung")
neu(T, "graphisch", "zwei_wege", Z(
    "Löse 12/(x + 2) = 4 (x ≠ −2) auf zwei Wegen. Weg A: rechnerisch, indem du mit dem Nenner multiplizierst. Weg B: mit einer Wertetabelle, in der du x-Werte ausprobierst. Wie groß ist x?",
    1, "12 / 4 - 2", 1, "Beide Wege müssen dasselbe x ergeben.",
    "Weg A: 12 = 4(x + 2), also x + 2 = 3 und x = 1. Weg B: Für x = 1 ist 12/3 = 4. Probe stimmt.",
    [(3, "fb.waage.nur_ein_summand", "12 : 4 = 3 gerechnet und die 2 vergessen", "12 / 4"), (5, "fb.waage.zeichen_nicht_gedreht", "3 + 2 gerechnet", "12 / 4 + 2")]), regel="id.algebra.gleichung_loesen")
assert ist_loesung("12/(x+2)", "4", 1)
