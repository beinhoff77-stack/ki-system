T = "stochastik.grundbegriffe_teil2"
AN = "id.daten.anteil"
ST = "id.daten.stufen"
# ───────── laplace ─────────
neu(T, "laplace", "lueckenweg", L(
    "In einer Urne liegen 4 rote, 7 blaue und 9 grüne Kugeln. Eine Kugel wird zufällig gezogen. Die Zahl der günstigen Kugeln für „nicht blau“ ist ①. Die Zahl aller Kugeln ist ②. Also ist P(nicht blau) gleich ③ %.",
    KOMM(3), [13, 20, 65], ["4 + 9", "4 + 7 + 9", "{1} * 100 // {2}"], ["20 - 7", "4 + 7 + 9", "(20 - 7) / 20 * 100"],
    "Günstig sind alle Kugeln, die nicht blau sind. Die Wahrscheinlichkeit ist günstige Kugeln durch alle Kugeln.",
    "Nicht blau sind 4 + 9 = 13 Kugeln. Alle Kugeln: 4 + 7 + 9 = 20. P(nicht blau) = 13/20 = 0,65 = 65 %. Probe: P(blau) = 7/20 = 35 % und 35 % + 65 % = 100 %.",
    {0: [(7, None, "die blauen Kugeln gezählt statt der nicht blauen", "7")], 1: [(11, None, "nur rote und blaue Kugeln gezählt: 4 + 7", "4 + 7")], 2: [(35, None, "die Wahrscheinlichkeit für blau statt für nicht blau angegeben", "7 * 100 // 20"), (186, "fb.anteil.guenstig_durch_unguenstig", "günstige durch ungünstige Kugeln geteilt und auf ganze Prozent gerundet", "round(13 * 100 / 7, 0)")]}), regel=AN)
neu(T, "laplace", "zwei_wege", Z(
    "Aus den Zahlen 1 bis 20 wird zufällig eine gezogen. Wie groß ist die Wahrscheinlichkeit in Prozent, dass sie weder durch 2 noch durch 5 teilbar ist? Weg A: Schreibe alle passenden Zahlen auf und zähle sie. Weg B: Zähle die durch 2 oder durch 5 teilbaren Zahlen mit dem Additionssatz (Überschneidung abziehen) und nimm das Gegenereignis.",
    40, "(20 - (10 + 4 - 2)) * 100 / 20", lambda: F(sum(1 for n in range(1, 21) if n % 2 and n % 5) * 100, 20),
    "Beide Wege müssen dieselbe Wahrscheinlichkeit ergeben.",
    "Weg A: Passend sind 1, 3, 7, 9, 11, 13, 17, 19. Das sind 8 Zahlen, also 8 : 20 = 40 %. Weg B: Durch 2 teilbar sind 10 Zahlen, durch 5 teilbar 4 Zahlen, durch beides (also durch 10) 2 Zahlen. Durch 2 oder 5: 10 + 4 − 2 = 12. Gegenereignis: 20 − 12 = 8 Zahlen, also 40 %.",
    [(60, None, "die Zahlen angegeben, die durch 2 oder durch 5 teilbar sind", "12 * 100 / 20"), (50, None, "nur die Bedingung „nicht durch 2“ beachtet", "10 * 100 / 20"), (30, None, "die Zahlen, die durch beides teilbar sind, doppelt abgezogen", "(20 - 10 - 4) * 100 / 20")], "%"), regel=AN)
neu(T, "laplace", "umkehren", Z(
    "Eine Urne enthält 20 Kugeln in den Farben rot, blau und grün. Es gilt P(rot) = 0,4. Es gibt doppelt so viele blaue wie grüne Kugeln. Wie viele grüne Kugeln liegen in der Urne?",
    4, "(20 - 20 * 0.4) / 3", lambda: next(g for g in range(0, 21) if 20 * 2 // 5 + g + 2 * g == 20),
    "Wie viele rote Kugeln gibt es? Was bleibt dann für blau und grün zusammen? Das ist ein Vielfaches der Zahl grüner Kugeln.",
    "Rot: 0,4 · 20 = 8 Kugeln. Blau und grün zusammen: 20 − 8 = 12. Mit g grünen und 2g blauen Kugeln gilt 3g = 12, also g = 4. Probe: 8 + 8 + 4 = 20.",
    [(12, None, "alle Kugeln gezählt, die nicht rot sind", "20 - 20 * 0.4"), (6, None, "nur durch 2 geteilt: 12 : 2", "12 / 2"), (8, None, "die roten Kugeln angegeben", "20 * 0.4")]), g="rueckwaerts", regel=AN)

# ───────── laplace_pruefen ─────────
neu(T, "laplace_pruefen", "verfahren_waehlen", W(
    "Du sollst prüfen, ob ein Zufallsexperiment ein Laplace-Experiment ist. Welche Frage musst du beantworten?",
    "Haben alle möglichen Ergebnisse dieselbe Wahrscheinlichkeit?",
    [("Gibt es mehr als zwei mögliche Ergebnisse?", "die Zahl der Ergebnisse mit ihrer Gleichwahrscheinlichkeit verwechselt"), ("Kann man das Experiment beliebig oft wiederholen?", "Wiederholbarkeit gehört nicht zur Definition"), ("Ist die Zahl der möglichen Ergebnisse gerade?", "eine Eigenschaft geprüft, die damit nichts zu tun hat")],
    "Bei einem Laplace-Experiment hat jedes Ergebnis genau denselben Anteil an allen Möglichkeiten.",
    "Ein Laplace-Experiment hat endlich viele Ergebnisse, die alle gleich wahrscheinlich sind. Nur dann gilt P(A) = günstige : mögliche. Wie viele Ergebnisse es gibt, ob sie sich wiederholen lassen oder ob die Zahl gerade ist, entscheidet nichts.",
    lambda: True), g="erkennen", regel=AN)
neu(T, "laplace_pruefen", "bruecke", W(
    "Das Säulendiagramm zeigt die Wahrscheinlichkeiten der vier Ergebnisse eines Zufallsexperiments in Prozent. Welche Aussage stimmt?",
    "Es ist kein Laplace-Experiment, weil gelb eine kleinere Wahrscheinlichkeit hat.",
    [("Es ist ein Laplace-Experiment, weil die Wahrscheinlichkeiten zusammen 100 % ergeben.", "die Summe 100 % gilt immer und sagt nichts über Gleichheit"), ("Es ist ein Laplace-Experiment, weil es vier Ergebnisse gibt.", "die Anzahl der Ergebnisse mit ihrer Gleichwahrscheinlichkeit verwechselt"), ("Es ist kein Laplace-Experiment, weil drei Säulen gleich hoch sind.", "den Grund falsch benannt: gleich hohe Säulen sprechen nicht dagegen")],
    "Bei einem Laplace-Experiment müssen alle Säulen gleich hoch sein. Wie sieht es hier aus?",
    "Die Säulen zeigen 30 %, 30 %, 30 % und 10 %. Zusammen sind es 100 %, aber gelb ist kleiner als die anderen. Nicht alle Ergebnisse sind gleich wahrscheinlich, also ist es kein Laplace-Experiment.",
    lambda: 30 + 30 + 30 + 10 == 100 and len({30, 30, 30, 10}) > 1,
    grafik={"typ": "saeulen", "einheit": " %", "werte": [{"name": "rot", "wert": 30}, {"name": "blau", "wert": 30}, {"name": "grün", "wert": 30}, {"name": "gelb", "wert": 10}], "zahlen": True}), g="darstellung", regel=AN)
neu(T, "laplace_pruefen", "umkehren", Z(
    "Ein Würfel hat auf seinen sechs gleich großen Seiten die Zahlen 1, 2, 3, 4, 5 und x. Das Ergebnis ist die oben liegende Zahl. Dabei ist x eine ganze Zahl von 1 bis 12. Für wie viele Werte von x ist das Werfen ein Laplace-Experiment?",
    7, "12 - 5", lambda: sum(1 for x in range(1, 13) if len({1, 2, 3, 4, 5, x}) == 6),
    "Wann haben alle Ergebnisse dieselbe Wahrscheinlichkeit? Was passiert, wenn x schon als Zahl vorkommt?",
    "Kommt x zweimal vor, zum Beispiel x = 3, dann hat die Zahl 3 die Wahrscheinlichkeit 2/6, die anderen 1/6. Das ist kein Laplace-Experiment. Alle Zahlen sind verschieden für x = 6, 7, …, 12. Das sind 7 Werte.",
    [(5, None, "die Werte gezählt, für die es kein Laplace-Experiment ist", "5"), (12, None, "alle möglichen Werte von x gezählt", "12"), (1, None, "nur x = 6 genannt", "1")]), g="parameter", regel=AN)

# ───────── gegenereignis ─────────
neu(T, "gegenereignis", "lueckenweg", L(
    "Zwei faire Würfel werden geworfen. Das Ergebnis ist ein Zahlenpaar. A: Die Augensumme ist größer als 4. Die Zahl aller möglichen Paare ist ①. Das Gegenereignis (Augensumme höchstens 4) hat ② Paare. Also hat A genau ③ Paare.",
    KOMM(3), [36, 6, 30], ["6 * 6", "6", "{1} - {2}"], ["6 * 6", lambda: sum(1 for a in range(1, 7) for b in range(1, 7) if a + b <= 4), lambda: sum(1 for a in range(1, 7) for b in range(1, 7) if a + b > 4)],
    "Das Gegenereignis ist leichter zu zählen. Schreibe die Paare mit kleiner Summe auf.",
    "Alle Paare: 6 · 6 = 36. Summe höchstens 4: (1|1), (1|2), (2|1), (1|3), (3|1), (2|2). Das sind 6 Paare. Also hat A 36 − 6 = 30 Paare. P(A) = 30/36 = 5/6.",
    {0: [(12, None, "die Zahlen der beiden Würfel addiert: 6 + 6", "6 + 6")], 1: [(3, None, "nur die Paare mit Summe genau 4 gezählt", "3")], 2: [(6, None, "das Gegenereignis statt A angegeben", "{2}")]}), regel=AN)
neu(T, "gegenereignis", "bruecke", Z(
    "Das Kreisdiagramm zeigt, wie die Kinder einer Schule zur Schule kommen. Ein Kind wird zufällig ausgewählt. Wie groß ist die Wahrscheinlichkeit in Prozent, dass es nicht mit dem Bus kommt?",
    60, "25 + 20 + 15", lambda: 100 - 40,
    "Die Wahrscheinlichkeit für „nicht Bus“ ist die Wahrscheinlichkeit für alle anderen Möglichkeiten zusammen.",
    "Das Gegenereignis zu „Bus“ ist „nicht Bus“. P(nicht Bus) = 100 % − 40 % = 60 %. Probe: 25 % + 20 % + 15 % = 60 %.",
    [(40, None, "die Wahrscheinlichkeit für den Bus angegeben", "40"), (35, None, "nur zwei der drei anderen Gruppen addiert: 20 + 15", "20 + 15")], "%",
    grafik={"typ": "kreisdiagramm", "einheit": " %", "werte": [{"name": "Bus", "wert": 40}, {"name": "Rad", "wert": 25}, {"name": "zu Fuß", "wert": 20}, {"name": "Auto", "wert": 15}], "zahlen": True}), g="darstellung", regel=AN)
neu(T, "gegenereignis", "anwenden", Z(
    "Bei einem Brettspiel darf man dreimal würfeln. Man gewinnt, wenn mindestens eine Sechs fällt. Wie groß ist die Gewinnwahrscheinlichkeit? Runde auf ganze Prozent.",
    42, RC((1 - (5 / 6) ** 3) * 100, 0), lambda: F(round(sum(1 for a in range(1, 7) for b in range(1, 7) for c in range(1, 7) if 6 in (a, b, c)) * 100 / 216)),
    "Das Gegenereignis von „mindestens eine Sechs“ ist „keine Sechs in allen drei Würfen“.",
    "P(keine Sechs in einem Wurf) = 5/6. In drei Würfen: (5/6)³ = 125/216 ≈ 0,579. Gegenereignis: 1 − 0,579 = 0,421, also etwa 42 %.",
    [(50, None, "dreimal ein Sechstel addiert", "round(3 * 100 / 6, 0)"), (58, None, "die Wahrscheinlichkeit für keine Sechs angegeben", "round((5 / 6) ** 3 * 100, 0)"), (17, None, "nur einen Wurf betrachtet", "round(100 / 6, 0)")], "%"), g="transfer", regel=ST)

# ───────── grosse_zahlen ─────────
neu(T, "grosse_zahlen", "lueckenweg", L(
    "Ein Reißnagel landet in 500 Würfen 180-mal mit der Spitze nach oben. Die relative Häufigkeit dafür ist ① %. Damit erwartet man bei 2 000 weiteren Würfen ungefähr ② Würfe mit der Spitze nach oben. Also erwartet man bei allen 2 500 Würfen insgesamt ungefähr ③ Würfe mit der Spitze nach oben.",
    KOMM(3), [36, 720, 900], ["180 * 100 // 500", "{1} * 2000 // 100", "180 + {2}"], ["180 / 500 * 100", "180 / 500 * 2000", "180 + 180 / 500 * 2000"],
    "Relative Häufigkeit = Treffer durch Versuche. Bei weiteren Versuchen rechnest du mit derselben Häufigkeit.",
    "180 : 500 = 0,36 = 36 %. Bei 2 000 weiteren Würfen: 0,36 · 2 000 = 720. Insgesamt erwartet man 180 + 720 = 900 Würfe mit der Spitze nach oben. Das sind wieder 36 % von 2 500.",
    {0: [(0.36, None, "als Dezimalzahl statt in Prozent angegeben", "180 / 500")], 1: [(72, None, "mit 200 statt mit 2 000 gerechnet", "{1} * 200 // 100")], 2: [(720, None, "die ersten 500 Würfe vergessen", "{2}")]}), regel=AN)
neu(T, "grosse_zahlen", "anwenden", Z(
    "In einer Fabrik sind erfahrungsgemäß 3 % der gefertigten Teile defekt. Wie viele Teile muss man ungefähr prüfen, um etwa 45 defekte zu finden?",
    1500, "45 * 100 / 3", lambda: F(45) / F(3, 100),
    "Wie viele Teile gehören zu einem defekten Teil, wenn 3 von 100 defekt sind?",
    "3 % sind 0,03. Gesucht ist die Zahl n mit 0,03 · n = 45, also n = 45 : 0,03 = 1 500. Probe: 3 % von 1 500 sind 45.",
    [(135, None, "45 mit 3 malgenommen: 45 · 3", "45 * 3"), (15, None, "45 durch 3 geteilt: 45 : 3", "45 / 3"), (1.35, None, "45 mit 3 % als Dezimalzahl malgenommen: 45 · 0,03", "45 * 0.03")]), g="einkleidung", regel=AN)
neu(T, "grosse_zahlen", "zwei_wege", Z(
    "Mit einem Glücksrad wurden drei Versuchsreihen gemacht: 50 Drehungen mit 18 Treffern, 200 Drehungen mit 66 Treffern und 1 000 Drehungen mit 331 Treffern. Schätze die Wahrscheinlichkeit für einen Treffer in Prozent, auf ganze Prozent gerundet. Weg A: Nimm nur die längste Reihe. Weg B: Fasse alle drei Reihen zusammen.",
    33, RC(415 / 1250 * 100, 0), lambda: F(round(331 * 100 / 1000)),
    "Beide Wege müssen auf ganze Prozent gerundet dasselbe ergeben.",
    "Weg A: 331 : 1 000 = 33,1 %. Weg B: (18 + 66 + 331) : (50 + 200 + 1 000) = 415 : 1 250 = 33,2 %. Gerundet sind es in beiden Fällen 33 %. Je mehr Versuche, desto verlässlicher die Schätzung.",
    [(36, None, "nur die kürzeste Reihe genommen", "round(18 * 100 / 50, 0)"), (33.2, None, "nicht auf ganze Prozent gerundet", "415 * 100 / 1250"), (17, None, "die Treffer aller Reihen durch die Zahl der längsten Reihe geteilt (halbiert)", "round(331 * 100 / 2000, 0)")], "%"), g="verknuepfen", regel=AN)
