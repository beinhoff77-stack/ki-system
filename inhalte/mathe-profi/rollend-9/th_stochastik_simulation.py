T = "stochastik.simulation"
AN = "id.daten.anteil"
ST = "id.daten.stufen"
Z20 = "52803917614298907845"
def treffer20():
    return sum(1 for ch in Z20 if ch in "0123")

# ───────── zufallsgeraet ─────────
neu(T, "zufallsgeraet", "lueckenweg", L(
    "Ein Glücksrad soll einen Treffer mit der Wahrscheinlichkeit 0,35 simulieren. Das Trefferfeld hat den Mittelpunktswinkel ① Grad. Dann hat der Rest des Rades ② Grad. Also ist die Wahrscheinlichkeit für keinen Treffer ③ %.",
    KOMM(3), [126, 234, 65], ["360 * 35 // 100", "360 - {1}", "{2} * 100 // 360"],
    ["360 * 7 // 20", "360 * 13 // 20", "100 - 35"],
    "Das ganze Rad hat 360 Grad. Das Trefferfeld ist 0,35 vom ganzen Rad.",
    "Trefferfeld: 0,35 · 360° = 126°. Rest: 360° − 126° = 234°. Kein Treffer: 234 : 360 = 0,65 = 65 %. Probe: 100 % − 35 % = 65 %.",
    {0: [(35, None, "die Prozentzahl als Winkel genommen", "35")],
     1: [(126, None, "den Winkel des Trefferfeldes statt des Rests genannt", "{1}"), (325, None, "von 360 Grad nur die Prozentzahl abgezogen", "360 - 35")],
     2: [(35, None, "die Wahrscheinlichkeit für einen Treffer statt für keinen genannt", "{1} * 100 // 360")]}), regel=AN)
neu(T, "zufallsgeraet", "anwenden", Z(
    "Ein Fußballspieler verwandelt Elfmeter mit der Wahrscheinlichkeit 75 %. Du simulierst ihn mit einem Glücksrad, das in 8 gleich große Felder eingeteilt ist. Wie viele Felder müssen Treffer sein?",
    6, "8 * 75 / 100", lambda: F(8) * F(3, 4),
    "Welcher Anteil der Felder muss Treffer sein? Rechne den Anteil auf 8 Felder um.",
    "75 % sind drei Viertel. Drei Viertel von 8 Feldern sind 6 Felder. Die übrigen 2 Felder sind kein Treffer.",
    [(2, None, "die Felder für einen Fehlschuss gezählt", "8 - 6"), (75, None, "den Prozentwert als Zahl der Felder genommen", "75"), (4, None, "die Hälfte der Felder genommen", "8 / 2")]), g="einkleidung", regel=AN)
neu(T, "zufallsgeraet", "umkehren", Z(
    "Ein Glücksrad hat zwei Felder, ein Trefferfeld und ein Restfeld. Das Trefferfeld ist um 108° größer als das Restfeld. Welche Trefferwahrscheinlichkeit in Prozent simuliert das Rad?",
    65, "(360 + 108) / 2 * 100 / 360", lambda: F(100) * (F(360 - 108, 2) + 108) / 360,
    "Beide Felder zusammen haben 360°. Wie groß ist das Restfeld, wenn das Trefferfeld um 108° mehr hat?",
    "Das Restfeld hat (360° − 108°) : 2 = 126°. Das Trefferfeld hat 126° + 108° = 234°. Es gilt 234 : 360 = 0,65, also 65 %.",
    [(30, None, "den Winkelunterschied als Anteil am ganzen Rad genommen", "108 * 100 / 360"), (35, None, "den Anteil des Restfeldes angegeben", "126 * 100 / 360"), (70, None, "den Winkelunterschied vom ganzen Rad abgezogen und dann durch das ganze Rad geteilt", "(360 - 108) * 100 / 360")], "%"), g="rueckwaerts", regel=AN)

# ───────── regel ─────────
neu(T, "regel", "lueckenweg", L(
    "Mit zweistelligen Zufallszahlen von 00 bis 99 soll ein Ereignis mit p = 3/20 simuliert werden. Dafür zählen ① Zahlen als Treffer. Dann sind die Zahlen von 00 bis ② Treffer. Also sind ③ Zahlen kein Treffer.",
    KOMM(3), [15, 14, 85], ["100 * 3 // 20", "{1} - 1", "100 - {1}"],
    ["15", "14", "100 - 15"],
    "Wie viele der 100 Zahlen entsprechen dem Anteil 3/20? Die Zahl 00 zählt mit.",
    "100 · 3/20 = 15 Zahlen sind Treffer. Weil 00 mitzählt, sind es die Zahlen 00 bis 14. Kein Treffer sind 100 − 15 = 85 Zahlen.",
    {0: [(3, None, "den Zähler als Anzahl genommen", "3"), (20, None, "den Nenner als Anzahl genommen", "20")],
     1: [(15, None, "die Anzahl als Obergrenze genommen, dann wären es eine Zahl zu viel", "{1}")],
     2: [(15, None, "die Zahl der Treffer statt der Nichttreffer genannt", "{1}"), (86, None, "die Zahl 00 doppelt berücksichtigt", "100 - {2}")]}), regel=AN)
neu(T, "regel", "bruecke", Z(
    "Die Tabelle legt fest, welche der Zufallsziffern 0 bis 9 als Treffer zählen. Welche Wahrscheinlichkeit wird so simuliert? Gib sie in Prozent an.",
    40, "4 * 100 / 10", lambda: F(len([x for x in "jjjnnnnjnn" if x == "j"]) * 100, 10),
    "Zähle die Ziffern mit „ja“. Alle zehn Ziffern sind gleich wahrscheinlich.",
    "Treffer sind die Ziffern 0, 1, 2 und 7, also 4 von 10 Ziffern. Das sind 4 : 10 = 0,4 = 40 %.",
    [(60, None, "die Ziffern ohne Treffer gezählt", "6 * 100 / 10"), (4, None, "die Zahl der Treffer ohne Umrechnung angegeben", "4"), (30, None, "nur die ersten drei Ziffern gezählt", "3 * 100 / 10")], "%",
    grafik=TAB(["Ziffer", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], ["Treffer", "ja", "ja", "ja", "nein", "nein", "nein", "nein", "ja", "nein", "nein"])), g="darstellung", regel=AN)
neu(T, "regel", "fehler_detektiv", FD(
    "Mit zweistelligen Zufallszahlen von 00 bis 99 soll ein Ereignis mit p = 0,08 simuliert werden. Lara legt die Regel fest.",
    [("Bei 8 % sind 8 von 100 Zahlen Treffer.", True, None),
     ("Die Zahlen von 00 bis 07 sind genau 8 Zahlen und zählen als Treffer.", True, None),
     ("Alle anderen Zahlen, also 08 bis 99, sind kein Treffer.", True, None),
     ("Das sind 91 Zahlen, also ist die Wahrscheinlichkeit für keinen Treffer 0,91.", False, None)],
    "Zähle nach: Wie viele Zahlen liegen von 08 bis 99? Es sind 100 Zahlen insgesamt, 8 davon sind Treffer.",
    "Die Zeilen 1 bis 3 stimmen. Von 08 bis 99 sind es 92 Zahlen, denn 100 − 8 = 92. Die Wahrscheinlichkeit für keinen Treffer ist 0,92."), regel=AN)

# ───────── zufallsziffern ─────────
neu(T, "zufallsziffern", "lueckenweg", L(
    "Die Ziffern 0 bis 3 sind Treffer. Zufallsziffern in vier Gruppen: 52803 91761 42989 07845. Von diesen 20 Ziffern sind ① Treffer. Dann sind ② Ziffern kein Treffer. Also ist die relative Häufigkeit der Treffer ③ %.",
    KOMM(3), [7, 13, 35], ["7", "20 - {1}", "{1} * 100 / 20"],
    [treffer20, lambda: 20 - treffer20(), lambda: F(treffer20() * 100, 20)],
    "Gehe die Ziffern der Reihe nach durch und markiere jede Ziffer von 0 bis 3.",
    "Treffer sind 2, 0, 3 | 1, 1 | 2 | 0, das sind 7 Ziffern. Kein Treffer: 20 − 7 = 13. Relative Häufigkeit: 7 : 20 = 0,35 = 35 %.",
    {0: [(13, None, "die Ziffern gezählt, die kein Treffer sind", "13"), (9, None, "auch die Ziffer 4 als Treffer gezählt", "9")],
     1: [(7, None, "die Zahl der Treffer statt der Nichttreffer genannt", "{1}")],
     2: [(65, None, "die relative Häufigkeit der Nichttreffer angegeben", "{2} * 100 / 20"), (7, None, "die Trefferzahl als Prozentwert übernommen", "{1}")]}), regel=AN)
neu(T, "zufallsziffern", "zwei_wege", Z(
    "Die Ziffern 1 bis 4 sind Treffer. Ein Durchgang besteht aus drei Ziffern. Zufallsziffern, nach Durchgängen geordnet: 827 135 906 444 583 298. In wie vielen der 6 Durchgänge gibt es mindestens einen Treffer? Weg A: Prüfe jeden Durchgang einzeln. Weg B: Zähle die Durchgänge ohne Treffer und nimm das Gegenereignis.",
    5, "6 - 1", lambda: sum(1 for g in "827 135 906 444 583 298".split() if any(ch in "1234" for ch in g)),
    "Beide Wege müssen dieselbe Anzahl ergeben. Beachte: Die Ziffer 0 ist kein Treffer.",
    "Weg A: Treffer gibt es in 827 (die 2), 135, 444, 583 und 298, das sind 5 Durchgänge. Weg B: Nur 906 hat keinen Treffer, also 6 − 1 = 5.",
    [(1, None, "die Zahl der Durchgänge ohne Treffer genannt", "1"), (6, None, "alle Durchgänge gezählt", "6"), (2, None, "nur die Durchgänge mit mindestens zwei Treffern gezählt", "2")]), regel=AN)
neu(T, "zufallsziffern", "umkehren", Z(
    "Bei einer Simulation sind einige der Ziffern 0 bis 9 als Treffer festgelegt, die kleinsten zuerst. Von 50 Zufallsziffern waren 30 Treffer. Wie viele der zehn Ziffern sind vermutlich als Treffer festgelegt?",
    6, "30 * 10 / 50", lambda: F(30, 50) * 10,
    "Welcher Anteil der Ziffern waren Treffer? Rechne diesen Anteil auf zehn Ziffern um.",
    "Der Anteil der Treffer ist 30 : 50 = 0,6. Das passt zu 6 von 10 Ziffern, zum Beispiel 0 bis 5.",
    [(30, None, "die Zahl der Treffer genommen", "30"), (3, None, "die Zahl der Treffer durch zehn geteilt", "30 / 10"), (4, None, "den Anteil der Nichttreffer genommen", "20 * 10 / 50")]), g="rueckwaerts", regel=AN)

# ───────── auswerten ─────────
neu(T, "auswerten", "lueckenweg", L(
    "Eine Simulation mit 250 Durchgängen ergab 90-mal das Ereignis E. Die relative Häufigkeit ist ① %. Dann erwartet man bei 10 000 echten Durchgängen etwa ② Treffer. Also erwartet man bei 1 000 Durchgängen etwa ③ Treffer.",
    KOMM(3), [36, 3600, 360], ["90 * 100 / 250", "{1} * 10000 / 100", "{2} / 10"],
    ["36", "10000 * 90 / 250", "1000 * 90 / 250"],
    "Relative Häufigkeit = Treffer durch Durchgänge. Rechne mit derselben Häufigkeit weiter.",
    "90 : 250 = 0,36 = 36 %. Bei 10 000 Durchgängen: 0,36 · 10 000 = 3 600. Bei 1 000 Durchgängen ist das ein Zehntel: 360.",
    {0: [(90, None, "die Zahl der Treffer als Prozentwert angegeben", "90"), (64, None, "den Anteil der Durchgänge ohne Treffer angegeben", "160 * 100 / 250")],
     1: [(360, None, "mit 1 000 statt mit 10 000 Durchgängen gerechnet", "{1} * 1000 / 100")],
     2: [(36, None, "die Prozentzahl als Trefferzahl übernommen", "{1}")]}), regel=AN)
neu(T, "auswerten", "zwei_wege", Z(
    "In einer Simulation kam ein Bus in 80 Durchgängen 56-mal pünktlich. Schätze, an wie vielen von 200 Tagen der Bus pünktlich kommt. Weg A: Bilde die relative Häufigkeit und multipliziere sie mit 200. Weg B: Rechne mit einem Dreisatz von 80 auf 200 Durchgänge.",
    140, "56 / 80 * 200", lambda: F(200) * F(7, 10),
    "Beide Wege müssen dieselbe Zahl ergeben.",
    "Weg A: 56 : 80 = 0,7 und 0,7 · 200 = 140. Weg B: 80 Durchgänge entsprechen 56 Treffern, 40 Durchgänge entsprechen 28 Treffern, 200 Durchgänge entsprechen 5 · 28 = 140 Treffern.",
    [(56, None, "die Zahl der Treffer der Simulation übernommen", "56"), (70, None, "die relative Häufigkeit in Prozent als Zahl der Tage genommen", "56 * 100 / 80"), (160, None, "die Zahl der Durchgänge verdoppelt", "80 * 2")]), regel=AN)
neu(T, "auswerten", "fehler_detektiv", FD(
    "Eine Simulation mit 500 Durchgängen ergab 140 Treffer. Sven schätzt die Treffer für größere Durchgangszahlen.",
    [("Relative Häufigkeit: 140 : 500 = 0,38.", False, None),
     ("Bei 3 000 Durchgängen erwartet man 0,38 · 3 000 = 1 140 Treffer.", True, True),
     ("Bei 1 000 Durchgängen erwartet man davon ein Drittel, also 380 Treffer.", True, True)],
    "Rechne 140 : 500 selbst nach, bevor du die nächste Zeile prüfst.",
    "140 : 500 = 0,28 und nicht 0,38. Die Zeilen 2 und 3 rechnen mit dem falschen Wert 0,38 richtig weiter. Richtig wären 840 Treffer bei 3 000 Durchgängen."), regel=AN)

# ───────── monte_carlo ─────────
neu(T, "monte_carlo", "lueckenweg", L(
    "Ein Quadrat hat die Seitenlänge 8 cm. Von 400 Zufallspunkten im Quadrat liegen 100 in einer Figur. Das Quadrat hat den Flächeninhalt ① cm². In der Figur liegen ② % der Punkte. Also schätzt man den Flächeninhalt der Figur auf ③ cm².",
    KOMM(3), [64, 25, 16], ["8 * 8", "100 * 100 / 400", "{1} * {2} / 100"],
    ["8 ** 2", "100 / 4", "64 / 4"],
    "Fläche des Quadrats = Seitenlänge mal Seitenlänge. Der Anteil der Punkte in der Figur entspricht dem Anteil der Fläche.",
    "Quadrat: 8 · 8 = 64 cm². Anteil der Punkte: 100 : 400 = 25 %. Figur: 25 % von 64 cm² = 16 cm².",
    {0: [(32, None, "den Umfang statt des Flächeninhalts berechnet", "8 * 4")],
     1: [(100, None, "die Zahl der Punkte in der Figur als Prozentzahl übernommen", "100"), (75, None, "den Anteil der Punkte außerhalb der Figur angegeben", "300 * 100 / 400")],
     2: [(25, None, "den Prozentwert als Flächeninhalt übernommen", "{2}"), (48, None, "den Anteil außerhalb der Figur mit der Fläche multipliziert", "{1} * 75 / 100")]}), regel=AN)
neu(T, "monte_carlo", "bruecke", Z(
    "Das Säulendiagramm zeigt, wie viele von je 100 Zufallspunkten in vier Läufen in einer Figur lagen. Alle Punkte lagen in einem Quadrat mit der Seitenlänge 10 cm. Schätze den Flächeninhalt der Figur aus allen vier Läufen zusammen in cm².",
    25, "(22 + 28 + 26 + 24) * 100 / 400", lambda: F((22 + 28 + 26 + 24) * 100, 400),
    "Fasse alle vier Läufe zusammen. Wie groß ist der Anteil der Punkte in der Figur? Das Quadrat hat 100 cm².",
    "In allen Läufen zusammen waren 22 + 28 + 26 + 24 = 100 von 400 Punkten in der Figur. Das sind 25 %. Die Figur hat etwa 25 % von 100 cm², also 25 cm².",
    [(100, None, "die Treffer aller Läufe als Fläche genommen", "22 + 28 + 26 + 24"), (28, None, "nur den besten Lauf genommen", "28"), (22, None, "nur den ersten Lauf genommen", "22")], "cm²",
    grafik={"typ": "saeulen", "einheit": " Punkte", "werte": [{"name": "Lauf 1", "wert": 22}, {"name": "Lauf 2", "wert": 28}, {"name": "Lauf 3", "wert": 26}, {"name": "Lauf 4", "wert": 24}], "zahlen": True}), g="darstellung", regel=AN)
neu(T, "monte_carlo", "umkehren", Z(
    "Ein Teich liegt in einem Rechteck von 40 m mal 25 m. Aus einer Karte weiß man, dass der Teich etwa 300 m² groß ist. Es werden 500 Zufallspunkte im Rechteck gewählt. Wie viele Punkte liegen ungefähr im Teich?",
    150, "500 * 300 / (40 * 25)", lambda: F(500) * F(300, 1000),
    "Welchen Anteil der Rechteckfläche nimmt der Teich ein? Dieser Anteil der Punkte liegt im Teich.",
    "Das Rechteck hat 40 · 25 = 1 000 m². Der Teich hat den Anteil 300 : 1 000 = 0,3. Von 500 Punkten liegen etwa 0,3 · 500 = 150 im Teich.",
    [(300, None, "die Fläche des Teichs als Zahl der Punkte genommen", "300"), (30, None, "den Anteil in Prozent statt der Zahl der Punkte angegeben", "300 * 100 / 1000"), (250, None, "die Hälfte der Punkte genommen", "500 / 2")]), g="rueckwaerts", regel=AN)

# ───────── beurteilen ─────────
neu(T, "beurteilen", "verfahren_waehlen", W(
    "Ein Bauteil ist mit der Wahrscheinlichkeit 0,25 fehlerhaft. Welches Zufallsgerät eignet sich zur Simulation?",
    "Eine Urne mit 3 weißen und 1 roten Kugel, rot ist ein Treffer, es wird mit Zurücklegen gezogen.",
    [("Ein Würfel, bei dem nur die Augenzahl 6 ein Treffer ist.", "ein Gerät mit der Wahrscheinlichkeit für einen Treffer von einem Sechstel gewählt", None, lambda: F(1, 6) != F(1, 4)),
     ("Eine Münze, bei der Kopf ein Treffer ist.", "ein Gerät mit der Wahrscheinlichkeit für einen Treffer von einer Hälfte gewählt", None, lambda: F(1, 2) != F(1, 4)),
     ("Eine Urne mit 4 weißen und 1 roten Kugel, rot ist ein Treffer, es wird mit Zurücklegen gezogen.", "ein Gerät mit der Wahrscheinlichkeit für einen Treffer von einem Fünftel gewählt", None, lambda: F(1, 5) != F(1, 4))],
    "Welche Wahrscheinlichkeit für einen Treffer hat das Gerät? Sie muss genau 0,25 sein.",
    "0,25 ist ein Viertel. Bei 1 roten von 4 Kugeln ist die Trefferwahrscheinlichkeit 1/4. Würfel (1/6), Münze (1/2) und die Urne mit 5 Kugeln (1/5) passen nicht.",
    lambda: F(1, 3 + 1) == F(25, 100) and F(1, 6) != F(25, 100) and F(1, 2) != F(25, 100) and F(1, 5) != F(25, 100)), g="erkennen", regel=AN)
neu(T, "beurteilen", "anwenden", Z(
    "Ein Ereignis tritt mit der Wahrscheinlichkeit 2/3 ein. Du simulierst es mit einem fairen Würfel. Wie viele der sechs Augenzahlen musst du als Treffer festlegen?",
    4, "6 * 2 / 3", lambda: F(6) * F(2, 3),
    "Welcher Anteil der sechs Augenzahlen muss Treffer sein?",
    "Zwei Drittel von 6 sind 4. Also zählen vier Augenzahlen als Treffer, zum Beispiel 1, 2, 3 und 4.",
    [(2, None, "den Zähler des Bruchs als Zahl der Augenzahlen genommen", "2"), (3, None, "den Nenner des Bruchs als Zahl der Augenzahlen genommen", "3"), (5, None, "eine Augenzahl weniger als alle genommen", "6 - 1")]), g="einkleidung", regel=AN)
neu(T, "beurteilen", "fehler_detektiv", FD(
    "Ein Ereignis hat die Wahrscheinlichkeit 0,4. Max simuliert es mit einer Urne mit 4 roten und 10 weißen Kugeln, es wird zufällig mit Zurücklegen gezogen.",
    [("Die Urne enthält 14 Kugeln, davon sind 4 rot.", True, None),
     ("Weil mit Zurücklegen gezogen wird, bleibt die Wahrscheinlichkeit bei jedem Zug gleich.", True, None),
     ("Die Wahrscheinlichkeit für rot ist das Verhältnis von roten zu weißen Kugeln, also 0,4.", False, None),
     ("Die Urne bildet also p = 0,4 ab und ist geeignet.", False, True)],
    "Die Wahrscheinlichkeit für rot vergleicht die roten Kugeln mit allen Kugeln in der Urne.",
    "Die Wahrscheinlichkeit für rot ist 4 : 14 und nicht 4 : 10. Das sind etwa 0,29. Die Urne ist nicht geeignet. Zeile 4 folgt aus der falschen Zeile 3."), regel=AN)
