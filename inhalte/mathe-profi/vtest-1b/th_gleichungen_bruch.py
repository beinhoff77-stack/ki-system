T = "gleichungen.bruch"
LP = "M8 4 Bruchterme und Bruchgleichungen (Bruchgleichungen, Definitionsmenge, Verhältnisgleichungen)"
# Stand nach Vorprüfung W1 (vorpruefung-w1.md, 9 A, 10 B): je Lernziel 1 Test + 2 Korrektur + 2 Sicherung, neu gebaut bis auf 024 (a aus D) und 040 ((a + b) : b).
# Abarbeitung der Befunde: korrektur-nach-vorpruefung-w1.md. Alle Auswahl-Aufgaben setzen ihren Platz selbst (pos=); am Dateiende werden genau so viele
# Werte aus POSITION4 verbraucht wie in der vorigen Fassung (10), damit die Plätze der folgenden Einheiten unverändert bleiben.


def bruch_gl(links, rechts, x):
    """Wert beider Seiten einer Gleichung (Python-Ausdrücke in x, exakte Brüche); None, wenn ein Nenner 0 ist."""
    try:
        return eval(links, {"F": F}, {"x": F(x)}), eval(rechts, {"F": F}, {"x": F(x)})
    except ZeroDivisionError:
        return None


def loesungen(links, rechts, bereich=range(-60, 61)):
    """Ganze Zahlen im Bereich, die die Gleichung erfüllen (mit Nennerprüfung)."""
    r = []
    for x in bereich:
        v = bruch_gl(links, rechts, x)
        if v is not None and v[0] == v[1]:
            r.append(x)
    return r


def loesungen_q(links, rechts, nenner=range(1, 7), bis=20):
    """Rationale Zahlen p/q (|p/q| ≤ bis, q aus nenner), die die Gleichung erfüllen (mit Nennerprüfung)."""
    kand = sorted({F(p, q) for q in nenner for p in range(-bis * q, bis * q + 1)})
    return [x for x in kand if (lambda v: v is not None and v[0] == v[1])(bruch_gl(links, rechts, x))]


def nullstellen_q(*nenner_ausdruecke, nenner=range(1, 7), bis=20):
    """Rationale Zahlen, für die einer der Nenner-Ausdrücke 0 wird."""
    kand = sorted({F(p, q) for q in nenner for p in range(-bis * q, bis * q + 1)})
    return sorted({x for x in kand for a in nenner_ausdruecke if eval(a, {"F": F}, {"x": x}) == 0})


REGEL[(T, "definitionsmenge")] = REGEL[(T, "scheinloesung")] = "id.algebra.erlaubte_zahlen"
REGEL[(T, "ueber_kreuz")] = "rr.waage"
REGEL[(T, "verhaeltnis")] = "rr.verhaeltnis"
ABG[(T, "definitionsmenge")] = "Die Übungen bestimmen D an einer gegebenen Gleichung; hier wird untersucht, wie Umformungen D verändern, wie D von der Lösungsmenge und von der Grundmenge abhängt und wie sich D von den sachlich sinnvollen Werten unterscheidet."
ABG[(T, "ueber_kreuz")] = "Die Übungen lösen mit dem Über-Kreuz-Verfahren; hier wird entschieden, wann das Verfahren direkt erlaubt ist, was über Kreuz aus Zählern und Nennern folgt und wann eine solche Gleichung keine Lösung hat."
ABG[(T, "scheinloesung")] = "Die Übungen prüfen einen Kandidaten gegen D; hier wird gesucht, an welchem Schritt eine Scheinlösung entsteht, eine Gleichung mit vorgegebener Scheinlösung gebaut und eine Regel über Scheinlösungen an Beispielen geprüft."
ABG[(T, "verhaeltnis")] = "Die Übungen lösen eine Verhältnisgleichung; hier wird zwischen additivem und multiplikativem Modell gewählt, zwischen Verhältnis und Anteil gewechselt und mit Mischungen und umgekehrten Verhältnissen argumentiert."
# ───────── definitionsmenge ─────────
# Test: Umformungen verändern D (Lösung geht beim Addieren eines Bruchs verloren, beim Malnehmen fällt eine Einschränkung weg)
_L_LEA = ("F(6)/(x-2) + F(1)/x", "F(3)/(x-1) + F(1)/x")
neu(T, "definitionsmenge", "test", "transfer", L(
    "Die Gleichung 6/(x − 2) = 3/(x − 1) hat in der Grundmenge ℚ die Lösung x = 0. Lea addiert auf beiden Seiten den Bruch 1/x und erhält Gleichung (L). "
    "Tom multipliziert beide Seiten der Ausgangsgleichung mit (x − 2) und erhält Gleichung (T). Wie viele Lösungen hat Gleichung (L), und wie viele Zahlen schließt die Definitionsmenge von Gleichung (T) aus?",
    "Gleichung (L): □ Lösungen; Gleichung (T): □ ausgeschlossene Zahlen", [0, 1], ["1 - 1", "2 - 1"],
    [len(loesungen_q(*_L_LEA)), len(nullstellen_q("x-1"))],
    "Die Ausgangsgleichung hat D = ℚ \\ {1; 2}, und 0 ist ihre Lösung: 6/(−2) = −3 und 3/(−1) = −3. Lea addiert 1/x. Dadurch steht der Nenner x in der Gleichung, und die Zahl 0 ist in (L) verboten. "
    "Für jede andere Zahl sagt (L) dasselbe wie die Ausgangsgleichung, deren einzige Lösung aber gerade 0 war. (L) hat also keine Lösung: Durch das Addieren ist die Lösung verloren gegangen. "
    "Tom erhält 6 = 3(x − 2)/(x − 1). Dort steht nur noch der Nenner x − 1; die Definitionsmenge von (T) schließt nur die Zahl 1 aus, die 2 ist plötzlich erlaubt. "
    "Umformungen können also die Definitionsmenge verkleinern oder vergrößern. Darum bestimmt man D an der Ausgangsgleichung und prüft am Ende gegen dieses D.",
    {0: [(1, "geglaubt, das Addieren desselben Bruchs auf beiden Seiten ändere die Lösungsmenge nie; die Lösung 0 ist in (L) aber verboten", "1")],
     1: [(2, "geglaubt, das Malnehmen ändere die Definitionsmenge nicht, und weiter 1 und 2 ausgeschlossen", "1 + 1"),
         (0, "geglaubt, nach dem Malnehmen stehe gar kein Nenner mehr da", "1 - 1")]}),
    lp=LP, idee="umformung_aendert_D")
# Korrektur 1: unverändert aus der vorigen Fassung (ohne A-/B-Befund)
neu(T, "definitionsmenge", "korrektur", "umkehr", Z(
    "Die Gleichung 6/(2x − a) + 4/(x + 3) = 2 hat die Definitionsmenge ℚ \\ {−3; 7}. Welche Zahl ist a?",
    14, "2 * 7", "14",
    "Die Zahl −3 kommt vom Nenner x + 3. Die Zahl 7 muss vom Nenner 2x − a kommen: 2 · 7 − a = 0, also a = 14. Probe: 2x − 14 = 0 gibt x = 7. Mit a = 7 wäre 2x − 7 = 0 bei x = 3,5, nicht bei 7.",
    [B("7", "a gleich der ausgeschlossenen Zahl 7 gesetzt; der Faktor 2 vor dem x wurde übersehen"),
     B("-2 * 7", "den Wert a mit falschem Vorzeichen übernommen: −(2 · 7)"),
     B("7 / 2", "durch 2 geteilt statt mit 2 malgenommen: 7 : 2")]), form="umkehren", lp=LP, idee="umkehr_D")
# Korrektur 2: Sachsituation selbst aufstellen; algebraischer Ausschluss gegen sachlich sinnvollen Bereich
neu(T, "definitionsmenge", "korrektur", "einkleidung", L(
    "Zwei Rechtecke sind gleich lang. Das erste hat den Flächeninhalt 36 cm² und ist x cm breit. Das zweite hat den Flächeninhalt 24 cm² und ist 3 cm schmaler als das erste. "
    "Stelle eine Bruchgleichung für x auf. Wie viele Zahlen schließt ihre Definitionsmenge aus, welche Zahl muss x für die Sachaufgabe übertreffen, und wie breit ist das erste Rechteck?",
    "ausgeschlossen: □ Zahlen; sinnvoll nur für x > □; Breite x = □ cm", [2, 3, 9], ["1 + 1", "3", "108 / 12"],
    [len(nullstellen_q("x", "x-3")), min(x for x in range(-10, 10) if x > 0 and x - 3 >= 0), next(x for x in loesungen("F(36)/x", "F(24)/(x-3)") if x > 3)],
    "Das erste Rechteck ist x cm breit und 36/x cm lang, das zweite ist (x − 3) cm breit und 24/(x − 3) cm lang. Gleich lang heißt: 36/x = 24/(x − 3). "
    "Die Nenner verbieten 0 und 3, also schließt die Definitionsmenge 2 Zahlen aus. Für die Sachaufgabe reicht das nicht: Beide Breiten müssen positiv sein, x > 0 und x − 3 > 0, also x > 3. "
    "Die Zahlen zwischen 0 und 3 liegen in D, sind als Breite aber sinnlos. Über Kreuz: 36(x − 3) = 24x, also 12x = 108 und x = 9. Probe: 36/9 = 4 und 24/6 = 4.",
    {0: [(1, "nur den Nenner x − 3 beachtet und die 0 vergessen", "2 - 1")],
     1: [(0, "nur verlangt, dass die erste Breite x positiv ist; auch die zweite Breite x − 3 muss positiv sein", "0")],
     2: [(-9, "das zweite Rechteck 3 cm breiter angesetzt: 36/x = 24/(x + 3)", "-108 / 12"),
         (-6, "die Flächen vertauscht: 24/x = 36/(x − 3)", "-72 / 12")]}),
    form="bruecke", lp=LP, idee="sach_D_gegen_sinnvoll")
# Sicherung 1 (Stufe 3): immer – manchmal – nie: gleiche Lösungsmenge, gleiche Definitionsmenge?
neu(T, "definitionsmenge", "sicherung", "begruenden", W(
    "Zwei Bruchgleichungen haben in der Grundmenge ℚ dieselbe Lösungsmenge. Welche Aussage über ihre Definitionsmengen ist richtig?",
    "Sie können verschieden sein, denn 2/x = 2 und 3/(x + 2) = 1 haben beide L = {1}, aber verschiedene Definitionsmengen.",
    [("Sie sind immer gleich, denn 2/x = 2 und 4/x = 4 haben beide L = {1} und auch dieselbe Definitionsmenge.",
      "aus einem einzigen passenden Beispiel auf „immer“ geschlossen; 2/x = 2 und 3/(x + 2) = 1 widerlegen das"),
     ("Sie sind nie gleich, denn zu zwei verschiedenen Gleichungen gehören immer verschiedene Nenner.",
      "geglaubt, verschiedene Gleichungen hätten verschiedene Nenner; 2/x = 2 und 4/x = 4 haben dieselbe Definitionsmenge"),
     ("Sie können nur dann verschieden sein, wenn beide Lösungsmengen leer sind, denn sonst legt die Lösung die Nenner fest.",
      "geglaubt, eine Lösung lege die Nenner fest; 2/x = 2 und 3/(x + 2) = 1 haben die Lösung 1 und trotzdem verschiedene Definitionsmengen")],
    "Die Definitionsmenge hängt nur von den Nennern ab, die Lösungsmenge von der ganzen Gleichung. 2/x = 2 hat L = {1} und D = ℚ \\ {0}; 3/(x + 2) = 1 hat ebenfalls L = {1}, aber D = ℚ \\ {−2}. "
    "Gleiche Lösungsmengen erzwingen also keine gleichen Definitionsmengen. Dass sie trotzdem gleich sein können, zeigen 2/x = 2 und 4/x = 4 (beide D = ℚ \\ {0}); „nie“ ist darum auch falsch. "
    "Und verschieden können sie nicht nur bei leerer Lösungsmenge sein: Die beiden ersten Gleichungen haben ja die Lösung 1.",
    lambda: (loesungen("F(2)/x", "F(2)") == [1] == loesungen("F(3)/(x+2)", "F(1)") == loesungen("F(4)/x", "F(4)")
             and nullstellen_q("x") == [0] and nullstellen_q("x+2") == [-2] and 0 not in nullstellen_q("x+2") and -2 not in nullstellen_q("x")), pos=1),
    lp=LP, idee="L_und_D_unabhaengig")
# Sicherung 2 (Stufe 2): rückwärts mit Grundmenge ℤ – D ist die Grundmenge ohne die Nennernullstellen, die in ihr liegen
def _b_ganz():
    """Alle ganzen b von −20 bis 20, für die D in ℤ genau zwei ganze Zahlen ausschließt, darunter 6; dazu die zweite Zahl."""
    r = []
    for b in range(-20, 21):
        aus = sorted({z for z in nullstellen_q("2*x+3", f"x*x-{b}*x") if z.denominator == 1})
        if len(aus) == 2 and 6 in aus:
            r.append((b, [z for z in aus if z != 6][0]))
    return r


neu(T, "definitionsmenge", "sicherung", "umkehr", L(
    "In der Grundmenge ℤ (ganze Zahlen) betrachtet man die Gleichung 5/(2x + 3) + 1/(x² − bx) = 2 mit einer Zahl b. Ihre Definitionsmenge schließt genau zwei ganze Zahlen aus, eine davon ist 6. "
    "Welche Zahl ist b, und welche ganze Zahl ist außer 6 ausgeschlossen?",
    "b = □; außerdem ausgeschlossen: □", [6, 0], ["6", "0"], [_b_ganz()[0][0], _b_ganz()[0][1]] if len(_b_ganz()) == 1 else [None, None],
    "Der Nenner 2x + 3 ist nur für x = −1,5 null; diese Zahl liegt nicht in ℤ und wird darum gar nicht ausgeschlossen. Die beiden ganzen Zahlen kommen also vom Nenner x² − bx = x(x − b): Er ist null für x = 0 und für x = b. "
    "Soll 6 ausgeschlossen sein, muss b = 6 sein; die zweite ausgeschlossene Zahl ist 0. In der Grundmenge ℚ wären es drei Zahlen (−1,5; 0; 6). Die Definitionsmenge ist immer die Grundmenge ohne die Zahlen, für die ein Nenner 0 wird.",
    {0: [(-6, "aus x − b = 0 bei x = 6 mit falschem Vorzeichen auf b = −6 geschlossen", "-6"),
         (36, "6 für x in x² eingesetzt und b = 6 · 6 genommen", "6 * 6")],
     1: [(-3, "aus 2x + 3 = 0 fälschlich x = −3 gemacht und diese Zahl genommen", "-3"),
         (3, "die Zahl 3 aus dem Nenner 2x + 3 als ausgeschlossene Zahl genommen", "3")]}),
    lp=LP, idee="grundmenge_Z_rueckwaerts")
# ───────── ueber_kreuz ─────────
def _ohne_loesung_a():
    """Alle ganzen a von −50 bis 50, für die a/(x + 5) = 7/(x − 2) in ℚ keine Lösung hat."""
    r = []
    for a in range(-50, 51):
        # über Kreuz: a(x − 2) = 7(x + 5)  ⇔  (a − 7)x = 2a + 35
        if a == 7:
            r.append(a)          # 0 · x = 49
            continue
        x = F(2 * a + 35, a - 7)
        v = bruch_gl(f"F({a})/(x+5)", "F(7)/(x-2)", x)
        if v is None or v[0] != v[1]:
            r.append(a)
    return r


_A_OHNE = _ohne_loesung_a()
neu(T, "ueber_kreuz", "test", "parameter", L(
    "In der Gleichung a/(x + 5) = 7/(x − 2) steht a für eine Zahl (Grundmenge ℚ). Für genau zwei Zahlen a hat die Gleichung keine Lösung. Welche sind es? Gib die kleinere zuerst an.",
    "a = □ und a = □", [0, 7], ["0", "7"], [_A_OHNE[0], _A_OHNE[-1]] if len(_A_OHNE) == 2 else [None, None],
    "Über Kreuz: a(x − 2) = 7(x + 5), also ax − 2a = 7x + 35 und (a − 7)x = 2a + 35. Für a = 7 steht 0 · x = 49 da: keine Lösung, denn zwei Brüche mit gleichem Zähler und verschiedenen Nennern sind nie gleich. "
    "Für a ≠ 7 ist x = (2a + 35)/(a − 7) der einzige Kandidat. Er ist nie 2 (sonst wäre 2a + 35 = 2a − 14), aber für a = 0 ist er −5 – und −5 ist verboten: eine Scheinlösung. "
    "Das passt zur Gleichung 0/(x + 5) = 7/(x − 2): Links steht immer 0, rechts nie. Für alle anderen a gibt es genau eine Lösung. Also a = 0 und a = 7.",
    {0: [(-5, "die verbotene Zahl −5 als Wert für a genommen", "-5"),
         (-7, "beim Fall „gleiche Zähler“ das Vorzeichen falsch gesetzt", "-7")],
     1: [(2, "die verbotene Zahl 2 als Wert für a genommen", "2"),
         (5, "die Zahl 5 aus dem Nenner x + 5 als Wert für a genommen", "5")]}),
    lp=LP, idee="parameter_keine_loesung")
# Korrektur 1: rückwärts – nur das Verhältnis der Zähler zählt
neu(T, "ueber_kreuz", "korrektur", "umkehr", Z(
    "Für welche Zahl a hat die Gleichung 10/(x − 3) = a/(x + 2) dieselbe Lösung wie die Gleichung 15/(x − 3) = 9/(x + 2)?",
    6, "10 * 9 / 15", (lambda x0: 10 * (x0 + 2) / (x0 - 3))(loesungen_q("F(15)/(x-3)", "F(9)/(x+2)")[0]),
    "Über Kreuz wird aus 15/(x − 3) = 9/(x + 2) die Gleichung 15(x + 2) = 9(x − 3). Teilt man durch 3, steht 5(x + 2) = 3(x − 3) da: Es kommt nur auf das Verhältnis 15 : 9 = 5 : 3 der Zähler an. "
    "Dieselbe Gleichung entsteht aus 10/(x − 3) = a/(x + 2), wenn 10 : a = 5 : 3 ist, also a = 6. Probe: Beide Gleichungen haben die Lösung x = −9,5 (5 · (−7,5) = −37,5 = 3 · (−12,5)).",
    [B("9 - 5", "additiv gedacht: von 15 auf 10 sind es 5 weniger, also auch 9 − 5"),
     B("9", "die Zahl 9 einfach übernommen"),
     B("9 * 15 / 10", "das Verhältnis falsch herum angesetzt: 9 · 15 : 10")]), form="umkehren", lp=LP, idee="zaehlerverhaeltnis_rueckwaerts")
# Korrektur 2: zwei Wege (über Kreuz gegen Kehrwert), wann sind beide erlaubt
neu(T, "ueber_kreuz", "korrektur", "mehrschritt", W(
    "Ali und Bea lösen 3/(x − 2) = 5/(x + 4). Ali multipliziert über Kreuz. Bea nimmt auf beiden Seiten den Kehrwert, erhält (x − 2)/3 = (x + 4)/5 und multipliziert dann beide Seiten mit 15. Welche Aussage über die beiden Wege stimmt?",
    "Beide Wege sind hier erlaubt und führen auf dieselbe Gleichung ohne Brüche, denn kein Zähler ist 0.",
    [("Beide Wege sind erlaubt, führen aber auf verschiedene Lösungen, denn Bea rechnet mit den Kehrwerten weiter.",
      "geglaubt, mit Kehrwerten ändere sich die Lösung; Bea erhält 5(x − 2) = 3(x + 4), genau wie Ali"),
     ("Nur Alis Weg ist erlaubt, denn den Kehrwert darf man bei einer Gleichung nie auf beiden Seiten nehmen.",
      "das Kehrwertbilden für verboten gehalten; sind beide Seiten nicht 0, haben auch die Kehrwerte gleiche Werte"),
     ("Nur Beas Weg ist erlaubt, denn über Kreuz darf man nur multiplizieren, wenn beide Nenner gleich sind.",
      "geglaubt, über Kreuz gehe nur bei gleichen Nennern; es geht immer, wenn auf jeder Seite genau ein Bruch steht")],
    "Ali: 3(x + 4) = 5(x − 2). Bea: 15 · (x − 2)/3 = 5(x − 2) und 15 · (x + 4)/5 = 3(x + 4), also 5(x − 2) = 3(x + 4). Das ist dieselbe Gleichung, nur mit vertauschten Seiten; beide erhalten x = 11. "
    "Den Kehrwert darf man nehmen, weil beide Seiten nicht 0 sein können: Die Zähler 3 und 5 sind nie 0. Bei einem Zähler, der 0 werden kann, ginge so eine Lösung verloren. Probe: 3/9 = 1/3 = 5/15.",
    lambda: (all(3 * (x + 4) - 5 * (x - 2) == -(F(15) * (x - 2) / 3 - F(15) * (x + 4) / 5) for x in (F(-7), F(0), F(5, 2), F(11)))
             and loesungen("F(3)/(x-2)", "F(5)/(x+4)") == [11] == loesungen("(x-2)/F(3)", "(x+4)/F(5)")), pos=3),
    form="zwei_wege", lp=LP, idee="kehrwert_zwei_wege")
# Sicherung 1 (Stufe 3): immer – manchmal – nie bei (x + a)/(x + b) = (x + c)/(x + d)
neu(T, "ueber_kreuz", "sicherung", "begruenden", W(
    "Gleichungen der Form (x + a)/(x + b) = (x + c)/(x + d) mit Zahlen a, b, c, d und b ≠ d löst man über Kreuz (Grundmenge ℚ). Welche Aussage über solche Gleichungen stimmt?",
    "Sie können auch keine Lösung haben, denn bei (x + 1)/(x + 2) = (x + 3)/(x + 4) bleibt über Kreuz nur 4 = 6 übrig.",
    [("Sie haben immer genau eine Lösung, denn bei (x + 1)/(x + 2) = (x + 4)/(x + 3) fällt x² weg, und es bleibt x = −2,5.",
      "aus einem Beispiel mit genau einer Lösung auf „immer“ geschlossen; nach dem Wegfallen von x² kann auch 0 · x = Zahl übrig bleiben"),
     ("Sie haben immer zwei Lösungen, denn nach dem Über-Kreuz-Multiplizieren steht auf beiden Seiten ein x².",
      "übersehen, dass x² auf beiden Seiten wegfällt; übrig bleibt eine Gleichung ohne x²"),
     ("Sie können nur dann eine Lösung haben, wenn a = c ist, denn bei (x + 2)/(x + 1) = (x + 2)/(x + 5) ist x = −2 die Lösung.",
      "aus einem Beispiel mit a = c eine Bedingung gemacht; (x + 1)/(x + 2) = (x + 4)/(x + 3) hat mit a ≠ c die Lösung −2,5")],
    "Über Kreuz: (x + a)(x + d) = (x + c)(x + b). Auf beiden Seiten steht x², es fällt weg; übrig bleibt eine Gleichung ohne x². "
    "Bei (x + 1)/(x + 2) = (x + 3)/(x + 4) wird daraus x² + 5x + 4 = x² + 5x + 6, also 4 = 6: keine Lösung. Bei (x + 1)/(x + 2) = (x + 4)/(x + 3) bleibt −2x = 5, also genau die Lösung −2,5. "
    "„Immer eine“, „immer zwei“ und „nur bei a = c“ sind damit widerlegt; richtig ist: Solche Gleichungen können auch keine Lösung haben.",
    lambda: (loesungen_q("(x+1)/(x+2)", "(x+3)/(x+4)") == [] and loesungen_q("(x+1)/(x+2)", "(x+4)/(x+3)") == [F(-5, 2)]
             and loesungen_q("(x+2)/(x+1)", "(x+2)/(x+5)") == [-2] and all((x + 1) * (x + 4) - (x + 3) * (x + 2) == -2 for x in range(-5, 6))), pos=0),
    lp=LP, idee="x_quadrat_faellt_weg")
# Sicherung 2 (Stufe 2): Verfahren wählen (Schema-Aufgabe des Lernziels: Regel „auf jeder Seite genau ein Bruch“)
neu(T, "ueber_kreuz", "sicherung", "mehrschritt", W(
    "Welche der vier Gleichungen kann man ohne vorheriges Zusammenfassen direkt über Kreuz multiplizieren?",
    "(x + 3)/(x − 1) = 5/(x + 2)",
    [("4/(x − 1) + 1 = 5/(x + 2)", "die Summe links übersehen; erst muss 4/(x − 1) + 1 zu einem Bruch zusammengefasst werden"),
     ("3/x = 2/(x + 2) − 1", "die Differenz rechts übersehen; rechts steht kein einzelner Bruch"),
     ("1/x + 2/x = 6/(x − 4)", "links zwei Brüche gesehen und sie wie einen behandelt; erst zusammenfassen zu 3/x")],
    "Über Kreuz darf man nur multiplizieren, wenn auf jeder Seite genau ein Bruch steht. Bei (x + 3)/(x − 1) = 5/(x + 2) ist das so; dass im Zähler eine Summe steht, stört nicht, sie wird in Klammern gesetzt: "
    "(x + 3)(x + 2) = 5(x − 1). In den anderen drei Gleichungen steht auf einer Seite eine Summe oder Differenz; dort muss man zuerst zu einem Bruch zusammenfassen.",
    lambda: [(1, 1), (2, 1), (1, 2), (2, 1)].count((1, 1)) == 1, pos=2),
    form="verfahren_waehlen", lp=LP, idee="wann_direkt_ueber_kreuz")
# ───────── scheinloesung ─────────
# Test (Stufe 3): zwei Wege – beim Kürzen fällt die Einschränkung x ≠ 0 weg, 0 wird zur Scheinlösung
neu(T, "scheinloesung", "test", "begruenden", W(
    "Tim und Ina lösen die Gleichung (x² + 6x)/(x² − 2x) = −3 (Grundmenge ℚ). Tim kürzt zuerst mit x und erhält (x + 6)/(x − 2) = −3. Dann multipliziert er mit (x − 2), erhält x + 6 = −3x + 6 und daraus x = 0. "
    "Seine Probe in der gekürzten Gleichung, 6/(−2) = −3, stimmt; er schreibt L = {0}. Ina bestimmt zuerst die Definitionsmenge der Ausgangsgleichung und kommt auf L = { }. An welcher Stelle entsteht Tims Fehler?",
    "Beim Kürzen, denn danach verbietet seine Gleichung die Zahl 0 nicht mehr, obwohl der Nenner x² − 2x für x = 0 null ist.",
    [("Beim Multiplizieren mit (x − 2), denn das Multiplizieren mit einem Term ist der Schritt, bei dem Scheinlösungen entstehen.",
      "eine Faustregel angewandt, ohne sie zu prüfen: x − 2 ist für den Kandidaten 0 gleich −2, dieser Schritt macht hier nichts kaputt"),
     ("Beim Aufschreiben der Lösungsmenge, denn 0 steht für nichts, also bedeuten L = {0} und L = { } dasselbe.",
      "die Menge mit der Zahl 0 mit der leeren Menge verwechselt; {0} enthält eine Zahl, { } keine"),
     ("Beim Ausmultiplizieren, denn −3 · (x − 2) ergibt −3x − 6 und nicht −3x + 6.",
      "das Vorzeichen beim Ausmultiplizieren falsch nachgerechnet; −3 · (−2) = 6, Tims Zeile stimmt")],
    "Die Ausgangsgleichung hat den Nenner x² − 2x = x(x − 2); er ist für x = 0 und x = 2 null, also D = ℚ \\ {0; 2}. Kürzt Tim mit x, steht nur noch der Nenner x − 2 da, und seine Gleichung verbietet nur die 2. "
    "Ab hier rechnet Tim richtig: x + 6 = −3x + 6 gibt 4x = 0, also x = 0, und in der gekürzten Gleichung stimmt die Probe. Die Zahl 0 gehört aber nicht zu D der Ausgangsgleichung: Dort steht für x = 0 der Bruch 0/0, der nicht definiert ist. "
    "0 ist eine Scheinlösung, sie entsteht durch das Kürzen. Richtig ist L = { }.",
    lambda: (bruch_gl("(x*x+6*x)/(x*x-2*x)", "F(-3)", 0) is None and bruch_gl("(x+6)/(x-2)", "F(-3)", 0) == (-3, -3)
             and all(-3 * (x - 2) == -3 * x + 6 for x in range(-5, 6)) and loesungen_q("(x*x+6*x)/(x*x-2*x)", "F(-3)") == []
             and F(0) - 2 != 0), pos=3),
    form="zwei_wege", lp=LP, idee="kuerzen_scheinloesung")
# Korrektur 1: rückwärts – Zahl c so wählen, dass eine vorgegebene Zahl Scheinlösung wird
def _c_fuer(schein):
    """c, für das der einzige Kandidat von 3/(x − 2) + 1/x = c/(x² − 2x) nach dem Malnehmen mit x(x − 2) die Zahl schein ist."""
    for c in range(-50, 51):
        # 3x + (x − 2) = c  ⇔  4x − 2 = c
        if F(c + 2, 4) == schein and bruch_gl("F(3)/(x-2) + F(1)/x", f"F({c})/(x*x-2*x)", schein) is None and loesungen_q("F(3)/(x-2) + F(1)/x", f"F({c})/(x*x-2*x)") == []:
            return c


neu(T, "scheinloesung", "korrektur", "umkehr", L(
    "In der Gleichung 3/(x − 2) + 1/x = c/(x² − 2x) steht c für eine Zahl (Grundmenge ℚ). Für welche Zahl c ist 2 eine Scheinlösung der Gleichung, und für welche Zahl c ist 0 eine Scheinlösung?",
    "2 ist Scheinlösung für c = □; 0 ist Scheinlösung für c = □", [6, -2], ["4 * 2 - 2", "4 * 0 - 2"], [_c_fuer(2), _c_fuer(0)],
    "Der Hauptnenner ist x² − 2x = x(x − 2); verboten sind 0 und 2. Malnehmen mit x(x − 2) gibt 3x + (x − 2) = c, also 4x − 2 = c. Der einzige Kandidat ist x = (c + 2)/4. "
    "Soll er 2 sein, muss c = 4 · 2 − 2 = 6 sein; soll er 0 sein, muss c = 4 · 0 − 2 = −2 sein. In beiden Fällen ist der Kandidat verboten, die Gleichung hat dann keine Lösung. "
    "Probe für c = 6: 4x − 2 = 6 gibt x = 2, und für x = 2 ist der Nenner x − 2 null.",
    {0: [(7, "beim Malnehmen den Bruch 1/x nur mit x statt mit x(x − 2) malgenommen: 3 · 2 + 1", "3 * 2 + 1"),
         (10, "das Minuszeichen bei (x − 2) übersehen: 4 · 2 + 2", "4 * 2 + 2")],
     1: [(1, "beim Malnehmen den Bruch 1/x nur mit x statt mit x(x − 2) malgenommen: 3 · 0 + 1", "3 * 0 + 1"),
         (2, "das Minuszeichen bei (x − 2) übersehen: 4 · 0 + 2", "4 * 0 + 2")]}),
    form="umkehren", lp=LP, idee="scheinloesung_konstruieren")
# Korrektur 2: Zahlenrätsel mit Scheinlösung (Schema-Aufgabe des Lernziels: D, Malnehmen, Kandidat prüfen)
neu(T, "scheinloesung", "korrektur", "einkleidung", Z(
    "Ali denkt sich eine Zahl. Er teilt 8 durch die um 4 verminderte Zahl und addiert 3. Dasselbe Ergebnis erhält er, wenn er die um 4 vergrößerte Zahl durch die um 4 verminderte Zahl teilt. "
    "Wie viele Zahlen kann Ali sich gedacht haben?",
    0, "4 - 4", len(loesungen_q("F(8)/(x-4) + 3", "(x+4)/(x-4)")),
    "Mit der gedachten Zahl x gilt 8/(x − 4) + 3 = (x + 4)/(x − 4). Die Zahl 4 ist verboten. Malnehmen mit (x − 4) gibt 8 + 3(x − 4) = x + 4, also 3x − 4 = x + 4 und x = 4. "
    "Der einzige Kandidat ist ausgerechnet die verbotene Zahl, eine Scheinlösung. Für jede andere Zahl ist die linke Seite um 2 größer als die rechte. Ali kann sich also keine Zahl gedacht haben.",
    [B("1", "den Kandidaten 4 als gedachte Zahl gezählt, ohne ihn zu prüfen"),
     B("4", "die Zahl 4 aus der Rechnung statt der Anzahl angegeben")], einheit="Zahlen"), form="bruecke", lp=LP, idee="raetsel_scheinloesung")
# Sicherung 1 (Stufe 3): welche Regel über Scheinlösungen ist durch die Beispiele gedeckt?
neu(T, "scheinloesung", "sicherung", "begruenden", W(
    "Vier Kinder haben je eine Bruchgleichung mit dem Hauptnenner multipliziert und aus ihrem Beispiel eine Regel über Scheinlösungen abgeleitet. Alle Rechnungen in den Beispielen stimmen. Welche Regel ist richtig?",
    "Scheinlösungen können vorkommen: Bei (2x − 1)/(x − 4) = 7/(x − 4) − 1 liefert das Multiplizieren x = 4, und 4 ist verboten.",
    [("Scheinlösungen kommen nie vor: Bei 8/(x − 1) = 2/(x − 1) + 3 liefert das Multiplizieren x = 3, und 3 ist erlaubt.",
      "aus einem Beispiel ohne Scheinlösung auf „nie“ geschlossen; das Beispiel mit x = 4 widerlegt die Regel"),
     ("Scheinlösungen kommen immer vor: Bei (x + 2)/(x − 5) = 7/(x − 5) liefert das Multiplizieren x = 5, und 5 ist verboten.",
      "aus einem Beispiel mit Scheinlösung auf „immer“ geschlossen; bei 8/(x − 1) = 2/(x − 1) + 3 ist der Kandidat 3 erlaubt"),
     ("Scheinlösungen können nur bei negativen Kandidaten vorkommen: Bei (x + 6)/(x + 3) = 3/(x + 3) liefert das Multiplizieren x = −3, und −3 ist verboten.",
      "eine Eigenschaft des einen Beispiels (negativ) zur Regel gemacht; die Scheinlösung 4 ist positiv")],
    "Ein einzelnes Beispiel kann eine Regel mit „immer“ oder „nie“ nicht beweisen, aber ein Gegenbeispiel kann sie widerlegen. Die Beispiele mit x = 4, x = 5 und x = −3 zeigen: Scheinlösungen kommen vor, also ist „nie“ falsch. "
    "Das Beispiel mit x = 3 zeigt: Der Kandidat ist nicht immer verboten, also ist „immer“ falsch. Die Scheinlösung 4 ist positiv, also ist „nur bei negativen“ falsch. "
    "Gedeckt ist nur: Scheinlösungen können vorkommen; darum prüft man jeden Kandidaten gegen D.",
    lambda: (loesungen_q("(2*x-1)/(x-4)", "F(7)/(x-4) - 1") == [] and all(2 * x - 1 - (7 - (x - 4)) == 3 * x - 12 for x in range(-5, 6))
             and loesungen("F(8)/(x-1)", "F(2)/(x-1) + 3") == [3] and loesungen_q("(x+2)/(x-5)", "F(7)/(x-5)") == []
             and loesungen_q("(x+6)/(x+3)", "F(3)/(x+3)") == []), pos=1),
    lp=LP, idee="regel_aus_beispielen")
# Sicherung 2 (Stufe 2): Darstellungswechsel – die beiden Seiten als Graphen; Differenz konstant, kein Schnittpunkt
neu(T, "scheinloesung", "sicherung", "darstellung", L(
    "Zu den beiden Seiten der Gleichung (x + 4)/(x − 3) − 2 = 7/(x − 3) zeichnet man die Graphen von f(x) = (x + 4)/(x − 3) − 2 und g(x) = 7/(x − 3). "
    "Für jede Zahl x ≠ 3 hat die Differenz f(x) − g(x) denselben Wert. Welchen? Und wie viele gemeinsame Punkte haben die beiden Graphen?",
    "f(x) − g(x) = □; gemeinsame Punkte: □", [-1, 0], ["1 - 2", "0"],
    [(lambda w: w.pop() if len(w) == 1 else None)({F(x + 4, x - 3) - 2 - F(7, x - 3) for x in range(-20, 21) if x != 3}), len(loesungen_q("(x+4)/(x-3) - 2", "F(7)/(x-3)"))],
    "f(x) − g(x) = (x + 4 − 7)/(x − 3) − 2 = (x − 3)/(x − 3) − 2 = 1 − 2 = −1 für jedes x ≠ 3. Der Graph von f liegt also überall genau 1 unter dem Graphen von g; sie haben keinen gemeinsamen Punkt. "
    "Rechnet man die Gleichung mit dem Malnehmen, erhält man x + 4 − 2(x − 3) = 7, also x = 3 – genau die Stelle, an der beide Graphen nicht definiert sind. Das Bild zeigt: 3 ist eine Scheinlösung, L = { }.",
    {0: [(1, "die Differenz andersherum gebildet, g(x) − f(x)", "1"),
         (-2, "nur die −2 betrachtet und die beiden Brüche nicht miteinander verrechnet", "-2")],
     1: [(1, "den Kandidaten x = 3 aus der Rechnung als Schnittpunkt gezählt", "1")]}),
    lp=LP, idee="graphen_differenz")
# ───────── verhaeltnis ─────────
# Test (Stufe 3): Mischung aus zwei Mischungen – Verhältnisse kann man nicht addieren, man muss auf die Mengen zurückgehen
neu(T, "verhaeltnis", "test", "transfer", Z(
    "Mischung A enthält Saft und Wasser im Verhältnis 1 : 1, Mischung B im Verhältnis 1 : 4. Zu 200 ml von Mischung A gießt man so viel von Mischung B, "
    "dass in der neuen Mischung Saft und Wasser im Verhältnis 1 : 2 stehen. Wie viele Milliliter von Mischung B braucht man?",
    250, "100 * 5 / 2", next(x for x in range(0, 2001) if F(100 + F(x, 5)) / (100 + F(4 * x, 5)) == F(1, 2)),
    "In 200 ml von A sind 100 ml Saft und 100 ml Wasser. Von x ml der Mischung B ist ein Fünftel Saft und vier Fünftel Wasser (1 + 4 = 5 Teile). Gesucht ist x mit (100 + x/5) : (100 + 4x/5) = 1 : 2. "
    "Über Kreuz: 2 · (100 + x/5) = 100 + 4x/5, also 200 + 2x/5 = 100 + 4x/5, 100 = 2x/5 und x = 250. Probe: Saft 100 + 50 = 150 ml, Wasser 100 + 200 = 300 ml, 150 : 300 = 1 : 2. "
    "Die Verhältniszahlen der beiden Mischungen darf man nicht einfach addieren; man rechnet mit den Mengen von Saft und Wasser.",
    [B("100 * 4", "das Verhältnis von Mischung B so gelesen, als sei ein Viertel davon Saft, und damit gerechnet"),
     B("100 * 5 / 4", "den Saft in Mischung B vergessen und nur verlangt, dass mit B weitere 100 ml Wasser dazukommen")], einheit="ml"),
    lp=LP, idee="mischung_aus_mischungen")
# Korrektur 1: Modellwahl – additiv (Alter) oder multiplikativ (Rezept)
neu(T, "verhaeltnis", "korrektur", "einkleidung", L(
    "Mia ist 6 Jahre alt, ihr Bruder 9 Jahre. Für einen Kuchen für 6 Personen braucht man 9 Esslöffel Zucker. In beiden Fällen stehen die Zahlen im Verhältnis 2 : 3. "
    "Wie alt ist der Bruder, wenn Mia 10 Jahre alt ist, und wie viele Esslöffel Zucker braucht man für einen solchen Kuchen für 10 Personen?",
    "Bruder: □ Jahre; Zucker: □ Esslöffel", [13, 15], ["10 + 3", "10 * 9 / 6"], ["9 + 4", "9 * 10 / 6"],
    "Beim Alter kommt bei beiden in derselben Zeit gleich viel dazu: Mia wird 4 Jahre älter, ihr Bruder auch; er ist dann 13. Der Unterschied von 3 Jahren bleibt, das Verhältnis ändert sich (10 : 13 statt 2 : 3). "
    "Beim Rezept bleibt das Verhältnis: Für 10 statt 6 Personen nimmt man alles 10/6-mal, also 9 · 10 : 6 = 15 Esslöffel. Dieselbe Zahlenangabe „2 : 3“ führt je nach Sache auf ein additives oder ein multiplikatives Modell.",
    {0: [(15, "auch beim Alter das Verhältnis beibehalten; beim Älterwerden bleibt aber der Altersunterschied gleich", "10 * 3 / 2")],
     1: [(13, "beim Rezept den Unterschied 3 beibehalten statt das Verhältnis", "10 + 3")]}),
    form="bruecke", lp=LP, idee="additiv_oder_multiplikativ_modell")
# Korrektur 2: Verhältnis und Anteil – Saftanteil halbieren
neu(T, "verhaeltnis", "korrektur", "darstellung", L(
    "Eine Schorle enthält Saft und Wasser im Verhältnis 1 : 3. Durch Zugabe von Wasser soll der Anteil des Safts an der ganzen Schorle halbiert werden. In welchem Verhältnis stehen Saft und Wasser danach?",
    "Saft : Wasser = 1 : □", [7], ["2 * (1 + 3) - 1"], [next(w for w in range(1, 100) if F(1, 1 + w) == F(1, 2) * F(1, 1 + 3))],
    "Bei 1 : 3 hat die Schorle 1 + 3 = 4 Teile, der Saftanteil ist 1/4. Halbiert ist er 1/8: Auf 1 Teil Saft kommen dann insgesamt 8 Teile Schorle, also 7 Teile Wasser. Saft : Wasser = 1 : 7. "
    "Verdoppelt man nur das Wasser (1 : 6), ist der Saftanteil 1/7, nicht die Hälfte von 1/4.",
    {0: [(6, "die Wasserteile verdoppelt; dann ist der Saftanteil ein Siebtel und nicht die Hälfte von einem Viertel", "3 * 2"),
         (8, "den halbierten Anteil (ein Achtel) bestimmt, aber 8 Teile Wasser statt 8 Teile Schorle genommen", "2 * (1 + 3)")]}),
    form="bruecke", lp=LP, idee="anteil_halbieren")
# Sicherung 1 (Stufe 3): umgekehrtes Verhältnis bei gleicher Strecke
neu(T, "verhaeltnis", "sicherung", "begruenden", W(
    "Ina und Tom fahren dieselbe Strecke, jeder mit gleichbleibender Geschwindigkeit. Ihre Fahrzeiten stehen im Verhältnis 3 : 4 (Ina : Tom). Welche Aussage über ihre Geschwindigkeiten (Ina : Tom) stimmt?",
    "Sie stehen im Verhältnis 4 : 3, denn bei gleicher Strecke gehört zur kürzeren Zeit die größere Geschwindigkeit.",
    [("Sie stehen im Verhältnis 3 : 4, denn Zeit und Geschwindigkeit stehen bei gleicher Strecke im selben Verhältnis.",
      "das Verhältnis der Zeiten unverändert übertragen; wer weniger Zeit braucht, fährt schneller"),
     ("Ina ist genau 1 km/h schneller als Tom, denn die Verhältniszahlen 3 und 4 unterscheiden sich um 1.",
      "das Verhältnis als Unterschied gelesen; 3 : 4 sagt nichts über Kilometer pro Stunde"),
     ("Man kann kein Verhältnis angeben, denn dazu müsste man die Länge der Strecke kennen.",
      "geglaubt, ohne die Strecke gehe es nicht; bei jeder Streckenlänge kommt dasselbe Verhältnis heraus")],
    "Für dieselbe Strecke s gilt: Geschwindigkeit = s : Zeit. Braucht Ina 3 Zeiteinheiten und Tom 4, ist Inas Geschwindigkeit s/3, Toms s/4. "
    "(s/3) : (s/4) = 4 : 3, für jede Streckenlänge s. Das Verhältnis der Geschwindigkeiten ist das umgekehrte Verhältnis der Zeiten. Beispiel: 12 km in 3 h und in 4 h gibt 4 km/h und 3 km/h.",
    lambda: all((F(s) / 3) / (F(s) / 4) == F(4, 3) for s in (1, 12, 50)) and F(12, 3) - F(12, 4) == 1 and F(24, 3) - F(24, 4) != 1, pos=0),
    lp=LP, idee="umgekehrtes_verhaeltnis")
# Sicherung 2: unverändert aus der vorigen Fassung (Schema-Aufgabe des Lernziels, siehe korrektur-nach-vorpruefung-w1.md)
neu(T, "verhaeltnis", "sicherung", "darstellung", Z(
    "Für zwei Zahlen a und b gilt a : b = 7 : 12. Dann gilt (a + b) : b = □ : 12.",
    19, "7 + 12", "(7 + 12) * 12 / 12",
    "Aus a : b = 7 : 12 folgt: Auf 7 Teile von a kommen 12 Teile von b. Zusammen sind a und b dann 7 + 12 = 19 Teile, und b ist 12 Teile. Also gilt (a + b) : b = 19 : 12. Probe mit a = 14 und b = 24: (14 + 24) : 24 = 38 : 24 = 19 : 12.",
    [B("7", "den Zähler 7 unverändert gelassen, obwohl a + b statt a steht"),
     B("12 - 7", "die Differenz der Verhältniszahlen genommen"),
     B("7 + 12 + 12", "die 12 für b doppelt addiert")], einheit=""), form="bruecke", lp=LP, idee="mittelwert_summe")
# ───────── Vorrat für eine Folgerunde (unverändert aus der vorigen Fassung, Plätze der richtigen Möglichkeit festgeschrieben) ─────────
neu(T, "definitionsmenge", "korrektur", "darstellung", W(
    "Welche Menge ist die Definitionsmenge der Gleichung 4/(x² − 16) + 1/x = 2?",
    "D = ℚ \\ {−4; 0; 4}",
    [("D = ℚ \\ {−16; 0; 16}", "x² − 16 = 0 so gelesen, als sei x = 16 und x = −16 gemeint; gesucht sind aber die Zahlen, deren Quadrat 16 ist"),
     ("D = ℚ \\ {−4; 4}", "den zweiten Nenner x nicht beachtet; für x = 0 ist 1/x nicht definiert"),
     ("D = ℚ \\ {0; 4}", "von x² = 16 nur die Lösung 4 genommen und −4 vergessen")],
    "x² − 16 = (x − 4)(x + 4) ist 0 für x = 4 und x = −4; der Nenner x ist 0 für x = 0. Alle drei Zahlen müssen ausgeschlossen werden.",
    lambda: {x for x in range(-20, 21) if x * x - 16 == 0 or x == 0} == {-4, 0, 4} and {x for x in range(-20, 21) if x * x - 16 == 0 or x == 0} != {-16, 0, 16}, pos=0), lp=LP, idee="menge_zuordnen")
neu(T, "definitionsmenge", "sicherung", "einkleidung", Z(
    "Ein Drucker allein braucht x Minuten für einen Auftrag, ein zweiter braucht 5 Minuten weniger, also x − 5 Minuten. Zusammen schaffen sie den Auftrag in 3 Minuten, das gibt die Gleichung 1/x + 1/(x − 5) = 1/3. Beide Druckzeiten müssen positive Zeiten sein. Wie viele ganze Zahlen von −3 bis 9 (einschließlich) kommen für x infrage?",
    4, "9 - 5", sum(1 for x in range(-3, 10) if x > 5),
    "Die Nenner x und x − 5 dürfen nicht 0 sein, also fallen 0 und 5 weg. Das reicht hier aber nicht: Eine Druckzeit ist eine positive Zahl. Aus x > 0 und x − 5 > 0 folgt x > 5. Von den ganzen Zahlen −3 bis 9 erfüllen das nur 6, 7, 8 und 9, also 4 Zahlen. Die Definitionsmenge allein (11 Zahlen) beschreibt nur, wann die Gleichung einen Sinn hat, nicht, wann die Aufgabe einen Sinn hat.",
    [B("13 - 2", "nur die Nenner beachtet und 0 und 5 ausgeschlossen, aber nicht verlangt, dass beide Zeiten positiv sind"),
     B("9 - 5 + 1", "die Zahl 5 mitgezählt, obwohl die zweite Druckzeit dann 0 Minuten wäre"),
     B("13", "keine Bedingung beachtet und alle Zahlen gezählt")], einheit="Zahlen"), form="bruecke", lp=LP, idee="text_zu_D")
neu(T, "ueber_kreuz", "korrektur", "umkehr", W(
    "Welche der folgenden Gleichungen hat die Lösung x = 6?",
    "4/(x − 2) = 2/(x − 4)",
    [("4/(x − 2) = 2/(x + 4)", "für x = 6 links 1 und rechts einen kleineren Wert; das Vorzeichen im rechten Nenner wurde nicht beachtet"),
     ("4/(x + 2) = 2/(x − 4)", "für x = 6 links einen kleineren Wert als rechts; das Vorzeichen im linken Nenner wurde nicht beachtet"),
     ("4/(x − 4) = 2/(x − 2)", "die beiden Nenner vertauscht; für x = 6 steht links das Vierfache von rechts")],
    "Man setzt x = 6 ein. 4/(6 − 2) = 1 und 2/(6 − 4) = 1: Beide Seiten sind gleich, die erste Gleichung hat die Lösung 6. Bei den anderen steht links 4/(6 − 2) = 1 gegen 2/10, 4/8 gegen 2/2 und 4/2 gegen 2/4.",
    lambda: F(4, 6 - 2) == F(2, 6 - 4) and F(4, 6 - 2) != F(2, 6 + 4) and F(4, 6 + 2) != F(2, 6 - 4) and F(4, 6 - 4) != F(2, 6 - 2), pos=0), lp=LP, idee="gleichung_zur_loesung")
neu(T, "ueber_kreuz", "sicherung", "begruenden", W(
    "Kim löst 3/x = 5/(x + 2) und schreibt: „Also gilt 3 · (x + 2) = 5 · x.“ Welche Aussage über Kims Schritt stimmt?",
    "Kim hat recht, denn mit x · (x + 2) malgenommen kürzt sich auf jeder Seite ein Nenner.",
    [("Kim irrt, denn über Kreuz hätte 3 · x = 5 · (x + 2) dastehen müssen.", "die Faktoren beim Über-Kreuz-Multiplizieren falsch zugeordnet, obwohl Kims Schritt stimmt"),
     ("Kim irrt, denn über Kreuz gilt nur, wenn beide Nenner gleich sind.", "geglaubt, über Kreuz sei nur bei gleichen Nennern erlaubt"),
     ("Kim irrt, denn man muss zuerst alle Brüche addieren und dann malnehmen.", "das Addieren von Brüchen mit dem Malnehmen beim Auflösen von Gleichungen verwechselt")],
    "Multipliziert man beide Seiten mit x · (x + 2), erhält man links 3/x · x · (x + 2) = 3 · (x + 2) und rechts 5/(x + 2) · x · (x + 2) = 5 · x. Das ist genau das Kreuzprodukt. Voraussetzung ist, dass x und x + 2 nicht 0 sind. Probe mit x = 3: 3/3 = 1 und 5/5 = 1.",
    lambda: F(3, 3) == F(5, 5) and 3 * (3 + 2) == 5 * 3, pos=1), lp=LP, idee="warum_ueber_kreuz")
neu(T, "scheinloesung", "korrektur", "darstellung", W(
    "Eine Bruchgleichung hat die Definitionsmenge ℚ \\ {−2; 3}. Nach dem Multiplizieren mit den Nennern und Umformen steht da x² = 9. Welche Aussage über die Lösungsmenge L stimmt?",
    "L = {−3}, denn von den beiden Zahlen mit dem Quadrat 9 gehört nur −3 zu D.",
    [("L = {−3; 3}, denn beide Zahlen erfüllen die Gleichung x² = 9.", "die Gleichung nach dem Umformen gelöst, aber die Zahlen nicht mit D verglichen"),
     ("L = {3}, denn x² = 9 ergibt x = 3.", "die zweite Lösung −3 vergessen und die verbotene Zahl 3 als Lösung genommen"),
     ("L = { }, denn die Zahl 3 ist ausgeschlossen und deshalb gibt es keine Lösung.", "eine ausgeschlossene Zahl so gewertet, als sei die ganze Gleichung unlösbar; die zweite Zahl −3 ist erlaubt")],
    "Aus x² = 9 folgen die Kandidaten x = 3 und x = −3. Die Zahl 3 gehört nicht zu D = ℚ \\ {−2; 3}: Für x = 3 wäre ein Nenner 0 (Scheinlösung). Die Zahl −3 gehört zu D und bleibt Lösung: L = {−3}.",
    lambda: {x for x in (3, -3) if x not in (-2, 3)} == {-3} and 3 * 3 == 9 and (-3) ** 2 == 9, pos=2), lp=LP, idee="kandidaten_gegen_D")
neu(T, "scheinloesung", "sicherung", "fehler", L(
    "Ina löst 5/(x − 1) + 2 = 7/(x − 1) so: Zeile 1: Mal (x − 1) gibt 5 + 2 = 7. Zeile 2: Das stimmt für jede Zahl. Zeile 3: Also sind alle Zahlen Lösung. In welcher Zeile steckt der erste Fehler, und welche Zahl ist die einzige Lösung der Gleichung?",
    "Fehler in Zeile □, einzige Lösung: x = □", [1, 2], ["1", "2"], ["4 - 3", "(7 - 5) / 1"],
    "Beim Malnehmen mit (x − 1) muss jedes Glied malgenommen werden, auch die 2: 5 + 2(x − 1) = 7. Das gibt 2x + 3 = 7, also x = 2. Die 2 liegt in D = ℚ \\ {1}. Probe: 5/1 + 2 = 7 und 7/1 = 7. Zeile 1 ist der Fehler; Zeile 2 und 3 folgen daraus.",
    {0: [(2, "den zweiten Satz „Das stimmt für jede Zahl“ für den Fehler gehalten", "1 + 1"), (3, "die Schlusszeile genannt, weil dort „alle Zahlen“ steht", "3")], 1: [(1, "die verbotene Zahl 1 als Lösung genommen", "1"), (4, "aus 2x + 3 = 7 nur 7 − 3 gerechnet und nicht durch 2 geteilt", "7 - 3")]}), form="fehler_detektiv", lp=LP, idee="fehler_nicht_alle_glieder")
neu(T, "verhaeltnis", "korrektur", "darstellung", W(
    "In einer Farbmischung verhalten sich die roten zu den blauen Teilen wie 3 : 5. Welchen Anteil der ganzen Mischung macht das Rot aus?",
    "3/8",
    [("3/5", "das Verhältnis Rot : Blau als Anteil an der Mischung gelesen; die 5 Teile Blau gehören nicht zum Rot"),
     ("5/8", "den Anteil des Blau genommen statt des Rot"),
     ("3/2", "Rot durch die Differenz 5 − 3 geteilt")],
    "Das Verhältnis 3 : 5 vergleicht die Teile Rot und Blau. Die ganze Mischung hat 3 + 5 = 8 Teile, davon sind 3 Teile rot. Der Anteil Rot ist also 3/8 (37,5 %). Das Blau macht 5/8 aus.",
    lambda: F(3, 3 + 5) == F(3, 8) and F(3, 5) != F(3, 8) and F(5, 8) != F(3, 8), pos=3), form="bruecke", lp=LP, idee="anteil_aus_verhaeltnis")
neu(T, "verhaeltnis", "sicherung", "fehler", L(
    "Lena löst die Verhältnisgleichung 4 : x = 6 : 18 so: Zeile 1: Außenglieder sind 4 und 18, Innenglieder sind x und 6. Zeile 2: Also 4 · x = 6 · 18. Zeile 3: Also x = 108 : 4 = 27. In welcher Zeile steckt der erste Fehler, und welchen Wert hat x richtig?",
    "Fehler in Zeile □, richtig: x = □", [2, 12], ["2", "4 * 18 / 6"], ["1 + 1", "72 / 6"],
    "Außenglieder mal Außenglieder = Innenglieder mal Innenglieder. Zeile 1 stimmt: Außenglieder 4 und 18, Innenglieder x und 6. Also gilt 4 · 18 = x · 6, das heißt 72 = 6x und x = 12 (Zeile 2 ist der Fehler: Lena kreuzt x mit 4). Probe: 4 : 12 = 1 : 3 = 6 : 18.",
    {0: [(3, "die Schlusszeile genannt, weil dort der falsche Wert 27 steht", "3"), (1, "die Zuordnung der Außenglieder in Zeile 1 für falsch gehalten", "1")], 1: [(27, "wie Lena x mit 4 gekreuzt: 6 · 18 : 4", "6 * 18 / 4"), (20, "additiv gerechnet: 6 + 18 − 4", "6 + 18 - 4"), (108, "nur 6 · 18 gerechnet und nicht geteilt", "6 * 18")]}), form="fehler_detektiv", lp=LP, idee="fehler_aussen_innen")
# Platzfolge der folgenden Einheiten unverändert lassen: die vorige Fassung dieser Datei hat 10 Werte aus POSITION4 verbraucht.
for _ in range(10):
    next(POSITION4)
