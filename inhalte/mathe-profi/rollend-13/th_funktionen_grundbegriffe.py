T = "funktionen.grundbegriffe"
R = "id.funktionen.zuordnung"
# ───────── eindeutig ─────────
_kind = {"Kim": 4, "Tom": 7, "Ali": 4, "Zoe": 9, "Mia": 7}
neu(T, "eindeutig", "anwenden", W(
    "Fünf Kinder wohnen in einer Straße. Die Tabelle zeigt die Hausnummer jedes Kindes. Jedes Kind wohnt in genau einem Haus. Betrachte die Zuordnungen (a) Kind → Hausnummer und (b) Hausnummer → Kind (in der Tabelle vorkommende Hausnummern). Welche Aussage stimmt?",
    "Nur (a) ist eine Funktion.",
    [("Nur (b) ist eine Funktion.", "die Richtung vertauscht: in (b) gehören zu den Hausnummern 4 und 7 jeweils zwei Kinder"), ("Beide Zuordnungen sind Funktionen.", "nur auf die Eindeutigkeit von (a) geachtet: bei (b) hat die Hausnummer 4 die Kinder Kim und Ali"), ("Keine der beiden Zuordnungen ist eine Funktion.", "die Mehrfachnennung der Hausnummern als Fehler von (a) gelesen: jedes Kind hat aber nur eine Hausnummer")],
    "Eine Funktion ordnet jeder Eingabe genau eine Ausgabe zu. Prüfe, ob zu einer Eingabe zwei verschiedene Ausgaben gehören.",
    "(a) Jedes Kind hat genau eine Hausnummer: Kim 4, Tom 7, Ali 4, Zoe 9, Mia 7. Das ist eine Funktion. (b) Zur Hausnummer 4 gehören Kim und Ali, zur Hausnummer 7 gehören Tom und Mia. Eine Eingabe hat zwei Ausgaben, also keine Funktion. Dass zwei Kinder dieselbe Hausnummer haben, ist bei (a) kein Problem.",
    lambda: len({k: v for k, v in _kind.items()}) == 5 and len(set(_kind.values())) < len(_kind),
    grafik=TAB(["Kind", "Kim", "Tom", "Ali", "Zoe", "Mia"], ["Hausnummer", "4", "7", "4", "9", "7"])), g="einkleidung", regel=R)
neu(T, "eindeutig", "umkehren", Z(
    "Die Zuordnung hat die Paare (1 | 4), (2 | a + 3), (3 | 5) und (2 | 9). Sie soll eine Funktion sein. Welche Zahl muss a sein?",
    6, "9 - 3", 6, "Bei einer Funktion gehört zu jedem x genau ein y. Zu welchem x gibt es mehr als ein Paar?",
    "Zum x = 2 gibt es zwei Paare: (2 | a + 3) und (2 | 9). Eine Funktion ordnet 2 nur einen y-Wert zu, also muss a + 3 = 9 gelten und a = 6. Probe: Mit a = 6 ist (2 | 9) beide Male dasselbe Paar, das ist erlaubt.",
    [(9, None, "den y-Wert 9 selbst als a eingetragen", "9"), (12, None, "9 + 3 gerechnet statt 9 − 3", "9 + 3"), (4, None, "den y-Wert des ersten Paares genommen", "4")]), g="rueckwaerts", regel=R)
# ───────── mengen ─────────
_fm = {-2: 3, -1: 0, 0: -1, 1: 0, 2: 3}
neu(T, "mengen", "bruecke", W(
    "Die Tabelle zeigt die Funktion f(x) = x² − 1 für die Definitionsmenge D = {−2; −1; 0; 1; 2}. Welche Menge ist die Wertemenge W?",
    "W = {−1; 0; 3}",
    [("W = {−2; −1; 0; 1; 2}", "die Definitionsmenge als Wertemenge angegeben"), ("W = {0; 3}", "den kleinsten Funktionswert −1 übersehen, weil er nur einmal vorkommt")],
    "Wertemenge: Welche verschiedenen Funktionswerte stehen in der unteren Zeile? Jeder Wert wird nur einmal genannt.",
    "Die Funktionswerte sind 3, 0, −1, 0, 3. Verschiedene Werte: −1, 0 und 3. Also W = {−1; 0; 3}. Die Zahlen aus D sind die Eingaben, nicht die Funktionswerte.",
    lambda: {k: k * k - 1 for k in _fm} == _fm and set(_fm.values()) == {-1, 0, 3},
    grafik=TAB(["x", "−2", "−1", "0", "1", "2"], ["f(x)", "3", "0", "−1", "0", "3"])), g="darstellung", regel=R)
neu(T, "mengen", "zwei_wege", Z(
    "Die Funktion f(x) = x² − 4x hat die Definitionsmenge D = {−1; 0; 1; 2; 3; 4; 5}. Weg A: alle sieben Funktionswerte ausrechnen. Weg B: nur f(2) und die Hälfte der Stellen ausrechnen, denn die Werte sind symmetrisch zur Stelle x = 2: Stellen mit gleichem Abstand von 2 haben denselben Funktionswert. Wie viele Elemente hat die Wertemenge W?",
    4, "7 - 3", "4", "Beide Wege müssen dieselbe Zahl ergeben. Gleiche Funktionswerte werden in der Wertemenge nur einmal gezählt.",
    "Weg A: f(−1) = 5, f(0) = 0, f(1) = −3, f(2) = −4, f(3) = −3, f(4) = 0, f(5) = 5. Verschiedene Werte: −4, −3, 0, 5. Weg B: f(1) = f(3), f(0) = f(4), f(−1) = f(5). Nur f(−1), f(0), f(1), f(2) sind nötig: 5, 0, −3, −4. Es sind 4 Elemente.",
    [(7, None, "alle sieben Funktionswerte als verschieden gezählt", "7"), (3, None, "den Funktionswert −4 bei der Stelle 2 vergessen", "3"), (5, None, "den Wert −3 doppelt gezählt (bei x = 1 und bei x = 3)", "5")]), g="verknuepfen", regel=R)
assert {k * k - 4 * k for k in range(-1, 6)} == {5, 0, -3, -4}
# ───────── funktionswert ─────────
neu(T, "funktionswert", "anwenden", Z(
    "Ein Stein wird von einer Brücke fallen gelassen, die 120 m über dem Wasser liegt. Ohne Luftwiderstand gilt für die Höhe über dem Wasser nach t Sekunden: h(t) = 120 − 5t². Wie hoch ist der Stein nach 4 Sekunden über dem Wasser (in Metern)?",
    40, "120 - 5 * 4 ** 2", "120 - 80", "Rechne zuerst das Quadrat, dann mal 5, dann ziehe das Ergebnis von 120 ab.",
    "h(4) = 120 − 5 · 4² = 120 − 5 · 16 = 120 − 80 = 40. Nach 4 Sekunden ist der Stein noch 40 m über dem Wasser.",
    [(80, None, "die Fallstrecke statt der Höhe über dem Wasser angegeben", "5 * 4 ** 2"), (-280, "fb.reihenfolge.mal_vor_hoch", "5t zusammen quadriert statt nur t: (5t)² statt 5t²", "120 - (5 * 4) ** 2"), (100, None, "das Quadrat von t vergessen: 5t statt 5t²", "120 - 5 * 4")], "m"), g="einkleidung", regel=R)
neu(T, "funktionswert", "umkehren", Z(
    "Für welche Zahl a hat die Funktion f(x) = a · x² + 3 an der Stelle x = 2 den Funktionswert 15?",
    3, "(15 - 3) / 2 ** 2", 3, "Setze x = 2 ein und rechne 2² zuerst. Dann bleibt eine Gleichung nur mit a.",
    "f(2) = a · 2² + 3 = 4a + 3. Aus 4a + 3 = 15 folgt 4a = 12 und a = 3. Probe: f(2) = 3 · 4 + 3 = 15.",
    [(6, None, "2² als 2 gerechnet: 2a + 3 = 15", "(15 - 3) / 2"), (3.75, None, "die 3 nicht abgezogen: 4a = 15", "15 / 4"), (12, None, "nicht durch 4 geteilt: a = 15 − 3", "15 - 3")]), g="rueckwaerts", regel=R)
# ───────── stelle ─────────
neu(T, "stelle", "bruecke", Z(
    "Die Zeichnung zeigt den Graphen einer linearen Funktion f. Für welche Stelle x gilt f(x) = 3?",
    2, "(6 - 3) / 1.5", 2, "Suche auf der y-Achse die Höhe 3 und gehe waagerecht bis zum Graphen. Lies dort die x-Koordinate ab.",
    "Auf dem Graphen liegen zum Beispiel die Punkte (0 | 6) und (4 | 0). Bei der Höhe y = 3 liegt der Punkt (2 | 3). Die gesuchte Stelle ist x = 2. Probe mit der Gleichung f(x) = −1,5x + 6: −1,5 · 2 + 6 = 3.",
    [(3, None, "den y-Wert als Stelle angegeben", "3"), (4, None, "die Nullstelle statt der gesuchten Stelle abgelesen", "6 / 1.5"), (6, None, "den Wert bei x = 0 abgelesen", "6")],
    grafik={"typ": "koordinaten", "x": [-1, 6], "y": [-1, 8], "graphen": [{"art": "linear", "m": -1.5, "t": 6, "name": "f"}], "punkte": [{"x": 0, "y": 6}, {"x": 4, "y": 0}]}), g="darstellung", regel=R)
neu(T, "stelle", "anwenden", Z(
    "Ein Fitnessstudio berechnet für n Besuche im Monat die Kosten K(n) = 20 + 4n (in Euro). Kim möchte, dass der Preis pro Besuch, also K(n)/n, genau 6 € beträgt. Bei wie vielen Besuchen im Monat ist das der Fall?",
    10, "20 / (6 - 4)", "(6 * 10 - 20) / 4", "Wie berechnest du den Preis pro Besuch aus K(n) und n?",
    "Gleichung: (20 + 4n)/n = 6. Mal n: 20 + 4n = 6n. Dann 20 = 2n und n = 10. Probe: K(10) = 60 €, und 60 : 10 = 6 €.",
    [(5, None, "nur 20 durch 4 geteilt", "20 / 4"), (2, None, "20 durch 6 + 4 geteilt statt durch 6 − 4", "20 / (6 + 4)"), (-10, None, "den Nenner mit vertauschten Zahlen gebildet: 4 minus 6 statt 6 minus 4", "20 / (4 - 6)")], "Besuche"), g="transfer", regel=R)
# ───────── wertetabelle ─────────
neu(T, "wertetabelle", "anwenden", Z(
    "Die Temperatur in Grad Fahrenheit hängt von der Temperatur C in Grad Celsius ab: F(C) = 1,8 · C + 32. Die Tabelle zeigt einige Werte. Wie viel Grad Fahrenheit sind 25 °C?",
    77, "1.8 * 25 + 32", "45 + 32", "Setze C = 25 in die Gleichung ein. Rechne zuerst das Malnehmen, dann das Addieren.",
    "F(25) = 1,8 · 25 + 32 = 45 + 32 = 77. 25 °C sind 77 °F. Passende Kontrolle mit der Tabelle: bei 20 °C sind es 68 °F und bei 30 °C sind es 86 °F, 77 liegt genau in der Mitte.",
    [(45, None, "nur 1,8 · 25 gerechnet, die 32 vergessen", "1.8 * 25"), (57, None, "nur 25 + 32 gerechnet, das Malnehmen mit 1,8 vergessen", "25 + 32"), (845, "fb.reihenfolge.links_nach_rechts", "von links nach rechts gerechnet: (1,8 + 32) · 25 statt 1,8 · 25 + 32", "(1.8 + 32) * 25")], "°F",
    grafik=TAB(["C in °C", "0", "10", "20", "30"], ["F in °F", "32", "50", "68", "86"])), g="einkleidung", regel=R)
neu(T, "wertetabelle", "zwei_wege", Z(
    "Die Tabelle gehört zur Funktion f(x) = x² − 6x + 5. Weg A: f(6) direkt ausrechnen. Weg B: Die Werte der Tabelle sind symmetrisch zur Stelle x = 3. Lies den Wert an der Stelle ab, die genauso weit von 3 entfernt ist wie 6. Welcher Wert gehört an die Stelle x = 6?",
    5, "6 ** 2 - 6 * 6 + 5", 5, "Beide Wege müssen denselben Wert ergeben. Die Stelle 6 ist 3 Schritte rechts von 3. Welche Stelle ist 3 Schritte links davon?",
    "Weg A: f(6) = 36 − 36 + 5 = 5. Weg B: 6 hat den Abstand 3 von der Stelle 3; die Stelle 0 hat auch den Abstand 3 auf der anderen Seite. Aus der Tabelle: f(0) = 5. Also f(6) = 5.",
    [(-19, "fb.potenz.basis_mal_hochzahl", "6² mit der Hochzahl malgenommen statt potenziert", "2 * 6 - 6 * 6 + 5"), (0, None, "den Wert der Nachbarstelle x = 5 aus der Tabelle übernommen", "0"), (77, "fb.vorzeichen.falsches_zeichen", "das Minus vor dem Glied 6x übersehen und 36 + 36 + 5 gerechnet", "36 + 36 + 5")],
    grafik=TAB(["x", "0", "1", "2", "3", "4", "5", "6"], ["f(x)", "5", "0", "−3", "−4", "−3", "0", "?"])), g="verknuepfen", regel=R)
# ───────── graph_lesen ─────────
neu(T, "graph_lesen", "anwenden", Z(
    "Ein Ball wird senkrecht nach oben geworfen. Die Zeichnung zeigt seine Höhe h in Metern in Abhängigkeit von der Zeit t in Sekunden (ohne Luftwiderstand). Wie viele Meter hoch fliegt der Ball höchstens?",
    20, "-5 * 2 ** 2 + 20 * 2", 20, "Wo liegt der höchste Punkt des Graphen? Lies seine Höhe an der senkrechten Achse ab.",
    "Der höchste Punkt des Graphen liegt bei t = 2 Sekunden auf der Höhe 20 Meter. Der Ball fliegt 20 m hoch. Er landet nach 4 Sekunden wieder (Höhe 0).",
    [(2, None, "den Zeitpunkt des höchsten Punkts statt seiner Höhe abgelesen", "20 / 10"), (4, None, "die Flugdauer statt der größten Höhe abgelesen", "2 * 2"), (15, None, "die Höhe nach einer Sekunde statt der größten Höhe abgelesen", "-5 * 1 ** 2 + 20 * 1")], "m",
    grafik={"typ": "koordinaten", "x": [0, 5], "y": [-2, 25], "graphen": [{"art": "poly", "k": [0, 20, -5]}], "name_x": "t in s", "name_y": "h in m"}), g="einkleidung", regel=R)
neu(T, "graph_lesen", "zwei_wege", Z(
    "Die Zeichnung zeigt die Graphen von f(x) = 0,5x + 1 und g(x) = −x + 7. Weg A: Lies die x-Koordinate des Schnittpunkts am Bild ab. Weg B: Setze f(x) = g(x) und löse die Gleichung. Bei welcher Stelle x haben beide Funktionen denselben Funktionswert?",
    4, "(7 - 1) / (0.5 + 1)", "6 / 1.5", "Beide Wege müssen dieselbe Stelle ergeben. Bei Weg B musst du 0,5x + 1 = −x + 7 nach x auflösen.",
    "Weg A: Die Graphen schneiden sich im Punkt (4 | 3). Weg B: 0,5x + 1 = −x + 7, also 1,5x = 6 und x = 4. Probe: f(4) = 3 und g(4) = 3.",
    [(3, None, "den y-Wert des Schnittpunkts statt der Stelle angegeben", "0.5 * 4 + 1"), (6, None, "durch 1 statt durch 1,5 geteilt: 6 : 1", "6 / 1"), (-12, None, "0,5x − (−x) falsch als 0,5 − 1 berechnet: 6 : (−0,5)", "6 / (0.5 - 1)")],
    grafik={"typ": "koordinaten", "x": [-2, 8], "y": [-2, 9], "graphen": [{"art": "linear", "m": 0.5, "t": 1, "name": "f"}, {"art": "linear", "m": -1, "t": 7, "name": "g"}]}), g="verknuepfen", regel=R)
# ───────── nullstellen ─────────
_fn = lambda x: x * x - x - 6
neu(T, "nullstellen", "bruecke", W(
    "Die Zeichnung zeigt den Graphen von f(x) = x² − x − 6. Welche Zahlen sind die Nullstellen von f?",
    "x = −2 und x = 3",
    [("x = 2 und x = −3", "die Vorzeichen der Nullstellen vertauscht: für x = 2 ist f(2) = −4 und nicht 0"), ("x = −6", "den Achsenabschnitt −6 als Nullstelle genommen: der Graph schneidet bei −6 die y-Achse, nicht die x-Achse")],
    "Nullstellen liegen dort, wo der Graph die x-Achse schneidet. Prüfe mit f(x) = 0 durch Einsetzen.",
    "Der Graph schneidet die x-Achse bei x = −2 und bei x = 3. Probe: f(−2) = 4 + 2 − 6 = 0 und f(3) = 9 − 3 − 6 = 0. Mit x = 2 ergibt sich 4 − 2 − 6 = −4, mit x = −3 ergibt sich 9 + 3 − 6 = 6. Die Zahl −6 ist der Wert f(0), also der Schnittpunkt mit der y-Achse.",
    lambda: _fn(-2) == 0 and _fn(3) == 0 and _fn(2) != 0 and _fn(-3) != 0 and _fn(0) == -6 and gl("x**2-x-6", "(x+2)*(x-3)"),
    grafik={"typ": "koordinaten", "x": [-4, 5], "y": [-8, 6], "graphen": [{"art": "poly", "k": [-6, -1, 1]}]}), g="darstellung", regel=R)
neu(T, "nullstellen", "umkehren", Z(
    "Die Funktion f(x) = x² + b · x − 12 hat die Nullstelle x = 3. Welche Zahl ist b?",
    1, "(12 - 3 ** 2) / 3", 1, "Setze x = 3 in die Funktion ein und setze das Ergebnis gleich 0. Es bleibt eine Gleichung nur mit b.",
    "f(3) = 3² + 3b − 12 = 9 + 3b − 12 = 3b − 3. Aus 3b − 3 = 0 folgt b = 1. Probe: f(x) = x² + x − 12, f(3) = 9 + 3 − 12 = 0.",
    [(4, None, "3² vergessen: 3b − 12 = 0", "12 / 3"), (-7, None, "die Zahl −12 mit dem falschen Vorzeichen übernommen", "(-12 - 9) / 3"), (2, "fb.potenz.basis_mal_hochzahl", "3² mit der Hochzahl malgenommen statt potenziert", "(12 - 2 * 3) / 3")]), g="rueckwaerts", regel=R)
# ───────── punkt_graph ─────────
_f = lambda x: -x * x + 4 * x
neu(T, "punkt_graph", "zwei_wege", W(
    "Gegeben sind f(x) = −x² + 4x und die Punkte A(1 | 3), B(2 | 3), C(3 | 3) und D(4 | 4). Weg A: Prüfe jeden Punkt durch Einsetzen. Weg B: Sieh im Bild nach, ob der Punkt auf der Kurve liegt. Welche der Punkte liegen auf dem Graphen von f?",
    "Nur A und C",
    [("Nur B und D", "genau die Punkte gewählt, die nicht auf dem Graphen liegen: bei x = 2 ist f(2) = 4 und nicht 3, bei x = 4 ist f(4) = 0"), ("A, B und C", "den y-Wert 3 bei allen drei Punkten für richtig gehalten, weil er bei A und C stimmt: f(2) ist aber 4"), ("Nur C", "nur einen Punkt geprüft: auch bei A ist f(1) = 3")],
    "Setze für jeden Punkt die x-Koordinate in f ein und vergleiche mit der y-Koordinate.",
    "f(1) = −1 + 4 = 3, also liegt A(1 | 3) auf dem Graphen. f(2) = −4 + 8 = 4, nicht 3, also liegt B nicht darauf. f(3) = −9 + 12 = 3, also liegt C darauf. f(4) = −16 + 16 = 0, nicht 4, also liegt D nicht darauf. Im Bild liegen A und C auf der Kurve.",
    lambda: [p for p in [(1, 3), (2, 3), (3, 3), (4, 4)] if _f(p[0]) == p[1]] == [(1, 3), (3, 3)],
    grafik={"typ": "koordinaten", "x": [-1, 5], "y": [-3, 6], "graphen": [{"art": "poly", "k": [0, 4, -1]}], "punkte": [{"x": 1, "y": 3, "name": "A"}, {"x": 2, "y": 3, "name": "B"}, {"x": 3, "y": 3, "name": "C"}, {"x": 4, "y": 4, "name": "D"}]}), g="mehrschritt", regel=R)
neu(T, "punkt_graph", "anwenden", Z(
    "Ein Ball fliegt auf einer Bahn mit der Höhe h(x) = −0,05x² + x (x ist der waagerechte Abstand in Metern, h die Höhe in Metern). Bei x = 12 steht ein Baum, dessen Spitze in P(12 | 5,5) liegt. Um wie viele Meter liegt die Baumspitze über der Stelle des Ballgraphen bei x = 12?",
    0.7, "5.5 - (-0.05 * 12 ** 2 + 12)", "5.5 - 4.8", "Vergleiche zwei Höhen an derselben Stelle x = 12.",
    "h(12) = −0,05 · 144 + 12 = −7,2 + 12 = 4,8. Die Baumspitze liegt bei 5,5 m, der Ball fliegt dort nur 4,8 m hoch. Unterschied: 5,5 − 4,8 = 0,7 m. Der Punkt P liegt nicht auf dem Graphen, sondern 0,7 m darüber; der Ball trifft den Baum.",
    [(-0.7, None, "die Differenz in der falschen Richtung gebildet: 4,8 − 5,5", "-0.05 * 12 ** 2 + 12 - 5.5"), (4.8, None, "nur die Höhe des Balls angegeben", "-0.05 * 12 ** 2 + 12"), (-5.3, "fb.potenz.basis_mal_hochzahl", "12² mit der Hochzahl malgenommen statt potenziert", "5.5 - (-0.05 * 2 * 12 + 12)")], "m"), g="transfer", regel=R)
# ───────── sachzusammenhang ─────────
neu(T, "sachzusammenhang", "anwenden", Z(
    "Ein Wassertank enthält am Anfang 800 Liter. Er verliert gleichmäßig 50 Liter pro Stunde. Für die Wassermenge nach t Stunden gilt V(t) = 800 − 50t. Nach wie vielen Stunden ist der Tank leer?",
    16, "800 / 50", "(800 - 0) / 50", "Der Tank ist leer, wenn V(t) = 0 ist. Löse diese Gleichung nach t auf.",
    "V(t) = 0 bedeutet 800 − 50t = 0, also 50t = 800 und t = 16. Nach 16 Stunden ist der Tank leer. Probe: V(16) = 800 − 800 = 0.",
    [(0.0625, None, "50 durch 800 geteilt statt 800 durch 50", "50 / 800"), (750, None, "den Füllstand nach einer Stunde angegeben", "800 - 50"), (-16, None, "das Vorzeichen vertauscht: −800 durch 50", "-800 / 50")], "Stunden"), g="einkleidung", regel=R)
neu(T, "sachzusammenhang", "zwei_wege", Z(
    "Kerze A ist 24 cm hoch und brennt gleichmäßig um 2 cm pro Stunde ab. Kerze B ist 30 cm hoch und brennt gleichmäßig um 3 cm pro Stunde ab. Beide werden gleichzeitig angezündet. Weg A: Gleichung 24 − 2t = 30 − 3t lösen. Weg B: eine Tabelle für t = 0, 1, 2, … anlegen und die Zeile mit gleichen Höhen suchen. Nach wie vielen Stunden sind beide gleich hoch?",
    6, "(30 - 24) / (3 - 2)", "6", "Beide Wege müssen dieselbe Zahl ergeben. Bei Weg B ändert sich der Höhenunterschied der beiden Kerzen Stunde für Stunde um dieselbe Zahl.",
    "Weg A: 24 − 2t = 30 − 3t, also t = 6. Weg B: Die Höhen nach 0, 1, 2, 3, 4, 5, 6 Stunden: A: 24, 22, 20, 18, 16, 14, 12 und B: 30, 27, 24, 21, 18, 15, 12. Nach 6 Stunden sind beide 12 cm hoch.",
    [(-6, None, "die Zahlen im Nenner vertauscht: 2 minus 3 statt 3 minus 2", "(30 - 24) / (2 - 3)"), (54, None, "die Höhen addiert: (24 + 30) durch (3 − 2)", "(24 + 30) / (3 - 2)"), (3, None, "nur durch das Abbrennen von Kerze A geteilt: 6 durch 2", "(30 - 24) / 2")], "Stunden"), g="verknuepfen", regel=R)
assert 24 - 2 * 6 == 30 - 3 * 6 == 12
