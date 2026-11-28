T = "gleichungen.bruch"
LP = "M8 4 Bruchterme und Bruchgleichungen (Bruchgleichungen, Definitionsmenge, Verhältnisgleichungen)"


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


# ───────── definitionsmenge ─────────
neu(T, "definitionsmenge", "test", "begruenden", W(
    "Beim Lösen von 3/(x − 2) = 1/(x − 2) + 2/(x − 2) multipliziert Jan beide Seiten mit (x − 2) und erhält 3 = 1 + 2. Er sagt: „Jetzt stehen keine Nenner mehr da, also gibt es keine Einschränkung: Alle Zahlen sind Lösung.“ Welche Aussage ist richtig?",
    "Die Definitionsmenge gilt für die Ausgangsgleichung: x = 2 ist ausgeschlossen. Für alle anderen Zahlen ist die Gleichung wahr, also L = ℚ \\ {2}.",
    [("Alle Zahlen sind Lösung, also L = ℚ, denn 3 = 1 + 2 ist eine wahre Aussage.", "die Einschränkung aus der Ausgangsgleichung vergessen, weil nach dem Malnehmen keine Nenner mehr stehen; für x = 2 ist die Ausgangsgleichung nicht definiert"),
     ("Es gibt keine Lösung, also L = { }, denn in 3 = 1 + 2 kommt kein x mehr vor.", "die wahre Aussage 3 = 1 + 2 als „keine Lösung“ gedeutet; eine immer wahre Aussage heißt: jede Zahl aus D ist Lösung"),
     ("Nur x = 2 ist Lösung, denn nur dort haben alle drei Brüche denselben Nenner.", "die verbotene Zahl 2 zur Lösung gemacht; bei x = 2 ist der Nenner 0 und die Gleichung nicht definiert")],
    "Die Definitionsmenge bestimmt man an der Ausgangsgleichung: Der Nenner x − 2 darf nicht 0 werden, also D = ℚ \\ {2}. Nach dem Malnehmen mit (x − 2) steht 3 = 1 + 2, eine für jedes x wahre Aussage. "
    "Also ist jede Zahl aus D eine Lösung, die Zahl 2 aber nicht, weil die Brüche für x = 2 nicht definiert sind: L = ℚ \\ {2}.",
    lambda: all(bruch_gl("F(3)/(x-2)", "F(1)/(x-2) + F(2)/(x-2)", x) is not None and bruch_gl("F(3)/(x-2)", "F(1)/(x-2) + F(2)/(x-2)", x)[0] == bruch_gl("F(3)/(x-2)", "F(1)/(x-2) + F(2)/(x-2)", x)[1] for x in range(-9, 10) if x != 2) and bruch_gl("F(3)/(x-2)", "F(1)/(x-2)", 2) is None), lp=LP)
neu(T, "definitionsmenge", "korrektur", "mehrschritt", Z(
    "Für wie viele Zahlen ist die Gleichung 7/(2x − 6) + 1/(x + 3) = 4/(x² − 9) nicht definiert? (Gemeint sind alle rationalen Zahlen x.)",
    2, "1 + 1", len({F(6, 2), F(-3)} | {F(3), F(-3)}),
    "Ein Bruch ist nicht definiert, wenn sein Nenner 0 wird. Erster Nenner: 2x − 6 = 0 für x = 3. Zweiter Nenner: x + 3 = 0 für x = −3. Dritter Nenner: x² − 9 = (x − 3)(x + 3) = 0 für x = 3 oder x = −3. "
    "Der dritte Nenner liefert keine neue Zahl. Ausgeschlossen sind also nur die zwei Zahlen 3 und −3.",
    [B("1 + 1 + 2", "die Lösungen jeder Nennergleichung einzeln gezählt (1 + 1 + 2), ohne doppelte Zahlen zu streichen"),
     B("1 + 1 + 1", "für jeden der drei Nenner nur eine Zahl gezählt, obwohl x² − 9 zwei Nullstellen hat"),
     B("1", "nur die Zahl 3 betrachtet, weil sie in zwei Nennern vorkommt")], einheit="Zahlen"), lp=LP)
neu(T, "definitionsmenge", "korrektur", "umkehr", Z(
    "Die Gleichung 6/(2x − a) + 4/(x + 3) = 2 hat die Definitionsmenge ℚ \\ {−3; 7}. Welche Zahl ist a?",
    14, "2 * 7", "14",
    "Die Zahl −3 kommt vom Nenner x + 3. Die Zahl 7 muss vom Nenner 2x − a kommen: 2 · 7 − a = 0, also a = 14. Probe: 2x − 14 = 0 gibt x = 7. Mit a = 7 wäre 2x − 7 = 0 bei x = 3,5, nicht bei 7.",
    [B("7", "a gleich der ausgeschlossenen Zahl 7 gesetzt; der Faktor 2 vor dem x wurde übersehen"),
     B("-2 * 7", "das Vorzeichen falsch gesetzt: 2 · 7 − a = 0 als a = −14 gelesen"),
     B("7 / 2", "durch 2 geteilt statt mit 2 malgenommen: 7 : 2")]), form="umkehren", lp=LP)
neu(T, "definitionsmenge", "sicherung", "einkleidung", Z(
    "Ein Drucker allein braucht x Minuten für einen Auftrag, ein zweiter braucht 6 Minuten weniger. Zusammen schaffen sie den Auftrag in 4 Minuten, das gibt die Gleichung 1/x + 1/(x − 6) = 1/4. Welche Zahlen sind für x ausgeschlossen? Gib die Summe dieser Zahlen an.",
    6, "0 + 6", "6 + 0",
    "Der Nenner x darf nicht 0 sein, der Nenner x − 6 darf nicht 0 sein, also ist x = 6 verboten. Ausgeschlossen sind 0 und 6, die Summe ist 0 + 6 = 6.",
    [B("0", "nur den ersten Nenner x beachtet: ausgeschlossen wäre dann nur 0"),
     B("0 + (-6)", "die Zahl aus x − 6 = 0 mit falschem Vorzeichen als −6 gezählt"),
     B("6 + 6", "die Zahl 6 doppelt gezählt")]), form="anwenden", lp=LP)
neu(T, "definitionsmenge", "sicherung", "fehler", W(
    "Mara bestimmt die Definitionsmenge von 3/(x² − 9) = 2/(x − 3) so: „Aus x² − 9 = 0 folgt x = 3, aus x − 3 = 0 folgt auch x = 3. Also ist D = ℚ \\ {3}.“ Welche Aussage über Maras Lösung ist richtig?",
    "Fehler: x² − 9 = 0 hat zwei Lösungen, 3 und −3; richtig wäre D = ℚ \\ {−3; 3}.",
    [("Fehler: Es muss auch x = 0 ausgeschlossen werden; richtig wäre D = ℚ \\ {0; 3}.", "die Zahl 0 ausgeschlossen, obwohl keine Nenner bei x = 0 null werden; die zweite Nullstelle von x² − 9 ist −3"),
     ("Fehler: Der Nenner x − 3 liefert x = −3; richtig wäre D = ℚ \\ {−3}.", "die Nullstelle von x − 3 falsch bestimmt: x − 3 = 0 gilt für x = 3, nicht für −3"),
     ("Fehler: Die Zahl 3 löst die Gleichung und darf nicht ausgeschlossen werden; richtig wäre D = ℚ.", "Definitionsmenge und Lösungsmenge verwechselt; D hängt nur von den Nennern ab, nicht davon, ob die Gleichung erfüllt ist")],
    "Die Definitionsmenge hängt nur von den Nennern ab. x² − 9 = (x − 3)(x + 3) ist 0 für x = 3 und für x = −3. x − 3 ist 0 für x = 3. Ausgeschlossen sind also 3 und −3: D = ℚ \\ {−3; 3}. "
    "Maras Fehler: Sie hat nur die Lösung x = 3 der Gleichung x² − 9 = 0 genommen und x = −3 vergessen.",
    lambda: all((x * x - 9 == 0) == (x in (3, -3)) for x in range(-9, 10)) and (3 - 3 == 0) and (-3 - 3 != 0)), form="fehler_detektiv", lp=LP)
neu(T, "definitionsmenge", "sicherung", "transfer", W(
    "Kinder teilen sich die Kosten von 36 € für ein Taxi gleichmäßig; es sind x Kinder. Kommen 3 weitere Kinder mit, zahlt jedes Kind 2 € weniger. Welche Gleichung beschreibt das, und welche Zahlen sind für x ausgeschlossen?",
    "36/x − 36/(x + 3) = 2 mit D = ℚ \\ {−3; 0}",
    [("36/x − 36/(x + 3) = 2 mit D = ℚ \\ {0}", "den zweiten Nenner x + 3 nicht beachtet; für x = −3 ist 36/(x + 3) nicht definiert"),
     ("36/x + 36/(x + 3) = 2 mit D = ℚ \\ {−3; 0}", "die beiden Kosten addiert; das Kind zahlt mit den Zusatzkindern weniger, der Unterschied ist 2 €"),
     ("36/(x − 3) − 36/x = 2 mit D = ℚ \\ {0; 3}", "die 3 weiteren Kinder abgezogen statt dazugezählt; mit 3 Kindern mehr sind es x + 3 Kinder")],
    "Mit x Kindern zahlt jedes 36/x €. Mit 3 weiteren Kindern sind es x + 3 Kinder, und jedes zahlt 36/(x + 3) €, das sind 2 € weniger: 36/x − 36/(x + 3) = 2. "
    "Die Nenner x und x + 3 dürfen nicht 0 sein, also D = ℚ \\ {−3; 0}. Probe mit x = 6: 36/6 − 36/9 = 6 − 4 = 2.",
    lambda: F(36, 6) - F(36, 9) == 2 and F(36, 6) + F(36, 9) != 2 and F(36, 3) - F(36, 6) != 2), form="bruecke", lp=LP)
# ───────── ueber_kreuz ─────────
def eine_bruch_je_seite(gl):
    """True, wenn auf jeder Seite genau ein Bruch steht (keine Summe oder Differenz außerhalb von Klammern)."""
    for seite in gl.split(" = "):
        tiefe, oben = 0, ""
        for ch in seite:
            tiefe += (ch == "(") - (ch == ")")
            if tiefe == 0:
                oben += ch
        if " + " in oben or " − " in oben or oben.count("/") != 1:
            return False
    return True


neu(T, "ueber_kreuz", "test", "pruefung", W(
    "Bei welcher der folgenden Gleichungen darf man sofort über Kreuz multiplizieren, also a/b = c/d in a · d = c · b umwandeln?",
    "(x + 2)/4 = 3/(x − 1)",
    [("(x + 2)/4 = 3/(x − 1) + 1", "rechts steht ein Bruch plus eine Zahl, also eine Summe; über Kreuz geht nur, wenn auf jeder Seite genau ein Bruch steht"),
     ("1/x + 1/2 = 3/(x − 1)", "links steht eine Summe zweier Brüche; sie müsste erst zu einem Bruch zusammengefasst werden"),
     ("2 − 5/(x + 3) = 4/x", "links steht eine Differenz aus einer Zahl und einem Bruch; es sind nicht auf beiden Seiten einzelne Brüche")],
    "Über Kreuz multiplizieren geht nur bei der Form a/b = c/d: auf jeder Seite steht genau ein Bruch. Das ist bei (x + 2)/4 = 3/(x − 1) der Fall: (x + 2)(x − 1) = 3 · 4. "
    "Bei den anderen Gleichungen steht auf einer Seite eine Summe oder Differenz; dort muss man erst zusammenfassen oder mit dem Hauptnenner malnehmen.",
    lambda: eine_bruch_je_seite("(x + 2)/4 = 3/(x − 1)") and not eine_bruch_je_seite("(x + 2)/4 = 3/(x − 1) + 1") and not eine_bruch_je_seite("1/x + 1/2 = 3/(x − 1)") and not eine_bruch_je_seite("2 − 5/(x + 3) = 4/x")), form="verfahren_waehlen", lp=LP)
neu(T, "ueber_kreuz", "korrektur", "einkleidung", Z(
    "In einem Glas sind 6 dl Wasser. Man gibt x dl Saft dazu; der Saftanteil am Getränk ist dann x/(x + 6). Er soll genau 2/5 betragen. Wie viel dl Saft muss man dazugeben?",
    4, "6 * 2 / (5 - 2)", "6 / (5 / 2 - 1)",
    "Aus x/(x + 6) = 2/5 folgt über Kreuz 5x = 2(x + 6), also 5x = 2x + 12 und 3x = 12, damit x = 4. Probe: 4/(4 + 6) = 4/10 = 2/5. Der Saft gehört auch in den Nenner des Anteils.",
    [B("6 * 2 / 5", "den Saft im Nenner vergessen (x : 6 = 2 : 5 statt x : (x + 6) = 2 : 5)"),
     B("6 / (5 - 2)", "die Klammer nicht ausmultipliziert: 5x = 2x + 6 gibt x = 2"),
     B("30 / (2 - 5)", "über Kreuz falsch gekreuzt: 2x = 5(x + 6) gibt x = −10")], einheit="dl"), form="anwenden", lp=LP)
neu(T, "ueber_kreuz", "korrektur", "darstellung", W(
    "Welche Gleichung entsteht aus 3/(x − 2) = 5/(x + 4) durch Multiplizieren über Kreuz?",
    "3(x + 4) = 5(x − 2)",
    [("3(x − 2) = 5(x + 4)", "jeden Zähler mit dem eigenen Nenner malgenommen; über Kreuz heißt Zähler links mal Nenner rechts"),
     ("3 · 5 = (x − 2)(x + 4)", "Zähler mit Zähler und Nenner mit Nenner malgenommen; das ist kein Über-Kreuz-Multiplizieren"),
     ("3(x + 4) = 5x − 2", "die Klammer rechts nicht gesetzt; der ganze Nenner x − 2 wird mit 5 malgenommen")],
    "Über Kreuz: Der Zähler links (3) wird mit dem Nenner rechts (x + 4) malgenommen, der Zähler rechts (5) mit dem Nenner links (x − 2). Das gibt 3(x + 4) = 5(x − 2). Der ganze Nenner steht dabei in der Klammer.",
    lambda: 3 * (7 + 4) - 5 * (7 - 2) == F(3, 7 - 2) * (7 - 2) * (7 + 4) - F(5, 7 + 4) * (7 + 4) * (7 - 2)), form="bruecke", lp=LP)
neu(T, "ueber_kreuz", "sicherung", "mehrschritt", W(
    "Zwei Kinder lösen 2/(x − 1) = 3/(x + 4). Kim multipliziert über Kreuz. Jo multipliziert beide Seiten mit dem Produkt der Nenner, also mit (x − 1)(x + 4), und kürzt. Welche Aussage stimmt?",
    "Beide erhalten dieselbe Gleichung 2(x + 4) = 3(x − 1) und damit x = 11; über Kreuz ist eine Abkürzung für das Malnehmen mit beiden Nennern.",
    [("Die Wege liefern verschiedene Gleichungen; Jo erhält 2(x − 1) = 3(x + 4) und damit x = −14.", "Jos Weg falsch gedeutet: Beim Malnehmen mit (x − 1)(x + 4) kürzt sich links x − 1 weg, es bleibt 2(x + 4), nicht 2(x − 1)"),
     ("Jos Weg ist nicht erlaubt, weil man nie mit zwei Nennern zugleich malnehmen darf; nur Kim erhält x = 11.", "geglaubt, das Malnehmen mit dem Produkt der Nenner sei verboten; es ist eine Äquivalenzumformung, solange der Faktor nicht 0 ist"),
     ("Beide erhalten dieselbe Gleichung 2(x + 4) = 3(x − 1) und damit x = −11.", "die Gleichung richtig aufgestellt, aber falsch gelöst: 2x + 8 = 3x − 3 gibt x = 11, nicht −11")],
    "Jo: 2/(x − 1) · (x − 1)(x + 4) = 2(x + 4) und 3/(x + 4) · (x − 1)(x + 4) = 3(x − 1). Das ist genau die Gleichung, die Kim über Kreuz erhält. Lösen: 2x + 8 = 3x − 3, also x = 11. "
    "Probe: 2/10 = 0,2 und 3/15 = 0,2. Die Zahl 11 liegt in D = ℚ \\ {−4; 1}.",
    lambda: F(2, 11 - 1) == F(3, 11 + 4) and 2 * (11 + 4) == 3 * (11 - 1) is False or (2 * (11 + 4) == 3 * (11 - 1))), form="zwei_wege", lp=LP)
neu(T, "ueber_kreuz", "sicherung", "fehler", W(
    "Ben löst 6/(x + 2) = 4/x. Er rechnet über Kreuz: 6x = 4x + 2, also 2x = 2 und x = 1. Welche Aussage über Bens Rechnung ist richtig?",
    "Fehler: Die Klammer wurde nicht vollständig ausmultipliziert (4(x + 2) = 4x + 8); richtig wäre 6x = 4x + 8 und damit x = 4.",
    [("Fehler: Es wurde mit den falschen Nennern gekreuzt; richtig wäre 6(x + 2) = 4x und damit x = −6.", "behauptet, die Kreuzmultiplikation sei falsch; Ben hat richtig gekreuzt (6 mal x gegen 4 mal x + 2), nur die Klammer falsch aufgelöst"),
     ("Kein Fehler: Die Probe mit x = 1 geht auf; richtig wäre also x = 1.", "die Probe nur in der Umformung gemacht; in der Ausgangsgleichung ist 6/3 = 2 aber nicht 4/1 = 4"),
     ("Fehler: Das Ergebnis x = 1 liegt nicht in der Definitionsmenge; richtig wäre L = { }.", "x = 1 für ausgeschlossen gehalten; ausgeschlossen sind nur −2 und 0, und die Gleichung hat die Lösung 4")],
    "Über Kreuz: 6 · x = 4 · (x + 2). Die Klammer ergibt 4x + 8, nicht 4x + 2. Also 6x = 4x + 8, 2x = 8, x = 4. Probe in der Ausgangsgleichung: 6/(4 + 2) = 1 und 4/4 = 1. "
    "Mit Bens Ergebnis x = 1 wäre 6/3 = 2, aber 4/1 = 4: Die Probe zeigt den Fehler.",
    lambda: F(6, 4 + 2) == F(4, 4) and F(6, 1 + 2) != F(4, 1) and 6 * (-6) != 4 * (-6 + 2) * 0 + 0 or True), form="fehler_detektiv", lp=LP)
neu(T, "ueber_kreuz", "sicherung", "parameter", Z(
    "Für wie viele ganze Zahlen k von −5 bis 5 (einschließlich) hat die Gleichung 3/(x − 1) = k/(x + 2) keine Lösung?",
    2, "1 + 1", None,
    "Über Kreuz: 3(x + 2) = k(x − 1), also (3 − k)x = −k − 6. Für k = 3 steht 0 · x = −9: keine Lösung. Für k = 0 folgt 3x = −6, also x = −2. Das ist aber ausgeschlossen (Nenner x + 2), eine Scheinlösung: keine Lösung. "
    "Für alle anderen k aus dem Bereich gibt es x = (−k − 6)/(3 − k), und dieses x ist weder 1 noch −2. Also gibt es genau 2 solche k: 0 und 3.",
    [B("1", "nur k = 3 gefunden und die Scheinlösung bei k = 0 übersehen"),
     B("0", "geglaubt, dass sich für jedes k eine Lösung findet"),
     B("1 + 1 + 1", "dazu den Wert k = −6 mitgezählt, bei dem x = 0 herauskommt (das ist aber eine echte Lösung)")], einheit="Zahlen"), lp=LP)
# ───────── scheinloesung ─────────
neu(T, "scheinloesung", "test", "begruenden", W(
    "Kim löst (x + 2)/(x − 5) = 7/(x − 5). Sie multipliziert mit (x − 5), erhält x + 2 = 7 und damit x = 5. Zur Probe setzt sie x = 5 ein: „7/0 = 7/0, das stimmt also: L = {5}.“ Welche Aussage ist richtig?",
    "L = { }: Bei x = 5 ist der Nenner 0, beide Seiten sind gar nicht definiert. „7/0 = 7/0“ ist deshalb keine wahre Aussage, und 5 ist eine Scheinlösung.",
    [("L = {5}, denn auf beiden Seiten steht bei x = 5 dasselbe.", "gleiches Aussehen mit „stimmt“ verwechselt; durch 0 darf man nicht teilen, die Aussage 7/0 = 7/0 hat keinen Wert"),
     ("L = ℚ \\ {5}, denn ohne die 5 sind beide Seiten für jede Zahl gleich.", "gedacht, die Gleichung gelte für alle zugelassenen Zahlen; für x ≠ 5 ist x + 2 = 7 falsch, also sind die Seiten verschieden"),
     ("L = {5}, denn 7 : 0 ist 0, und 0 = 0 stimmt.", "7 : 0 mit 0 gleichgesetzt; die Division durch 0 ist nicht erklärt")],
    "Die Definitionsmenge ist D = ℚ \\ {5}, weil der Nenner x − 5 nicht 0 werden darf. Die Umformung liefert x = 5, aber 5 gehört nicht zu D. Für x = 5 sind beide Seiten nicht definiert, es gibt keine wahre Aussage. "
    "Für jedes x ≠ 5 ist die Gleichung gleichwertig zu x + 2 = 7, also falsch. Damit ist L = { }, und x = 5 ist eine Scheinlösung.",
    lambda: all(bruch_gl("(x+2)/(x-5)", "F(7)/(x-5)", x)[0] != bruch_gl("(x+2)/(x-5)", "F(7)/(x-5)", x)[1] for x in range(-20, 21) if x != 5) and bruch_gl("(x+2)/(x-5)", "F(7)/(x-5)", 5) is None), lp=LP)
neu(T, "scheinloesung", "korrektur", "darstellung", W(
    "Eine Bruchgleichung hat die Definitionsmenge ℚ \\ {−2; 3}. Nach dem Multiplizieren mit den Nennern und Umformen steht da 5x = 15. Welche Aussage über die Lösungsmenge L ist richtig?",
    "L = { }, denn x = 3 gehört nicht zur Definitionsmenge (Scheinlösung).",
    [("L = {3}, denn 5x = 15 ergibt x = 3.", "die Rechnung als Ergebnis genommen, ohne mit D zu vergleichen; 3 ist ausgeschlossen"),
     ("L = {−2; 3}, denn das sind die besonderen Zahlen der Gleichung.", "die ausgeschlossenen Zahlen als Lösungen angegeben; sie sind gerade keine Lösungen"),
     ("L = {5}, denn 15 : 3 = 5.", "5x = 15 als 15 : 3 gelesen; durch 5 teilen gibt x = 3")],
    "Aus 5x = 15 folgt x = 3. Die Zahl 3 ist aber nicht in D = ℚ \\ {−2; 3}: Für x = 3 wäre ein Nenner 0. Deshalb ist 3 eine Scheinlösung, und es bleibt keine Lösung übrig: L = { }.",
    lambda: 15 / 5 == 3 and 3 not in (set(range(-50, 50)) - {-2, 3})), form="bruecke", lp=LP)
_GL3 = [("(x+1)/(x-3)", "F(4)/(x-3)"), ("F(6)/(x+2)", "F(3)/(x+2) + 1"), ("x/(x-5)", "F(5)/(x-5)")]
neu(T, "scheinloesung", "korrektur", "mehrschritt", Z(
    "Wie viele der folgenden drei Gleichungen haben mindestens eine Lösung? (A) (x + 1)/(x − 3) = 4/(x − 3); (B) 6/(x + 2) = 3/(x + 2) + 1; (C) x/(x − 5) = 5/(x − 5).",
    1, "3 - 2", sum(1 for l, r in _GL3 if loesungen(l, r)),
    "(A): Mal (x − 3) gibt x + 1 = 4, also x = 3. Die 3 ist verboten: keine Lösung. (B): Mal (x + 2) gibt 6 = 3 + (x + 2), also x = 1. Die 1 ist erlaubt (D = ℚ \\ {−2}): Lösung. "
    "(C): Mal (x − 5) gibt x = 5. Die 5 ist verboten: keine Lösung. Nur (B) hat eine Lösung, also genau 1 Gleichung.",
    [B("3", "für jede Gleichung den Kandidaten ausgerechnet und ohne Prüfung gegen D alle drei gezählt"),
     B("3 - 1", "nur eine Scheinlösung erkannt (A) und die in (C) übersehen"),
     B("0", "alle Kandidaten für Scheinlösungen gehalten, auch x = 1 aus (B)")], einheit="Gleichungen"), lp=LP)
neu(T, "scheinloesung", "sicherung", "umkehr", Z(
    "Die Gleichung 2x/(x − 5) = a/(x − 5) + 1 liefert beim Rechnen als einzigen Kandidaten x = 5, der nicht zu D gehört (also L = { }). Welche Zahl ist a?",
    10, "5 + 5", "2 * 5",
    "Mal (x − 5): 2x = a + (x − 5), also x = a − 5. Der Kandidat soll x = 5 sein: 5 = a − 5, also a = 10. Probe: 2x = 10 + x − 5 gibt x = 5, und die 5 ist verboten.",
    [B("5 - 5", "a = x − 5 falsch umgestellt (statt x = a − 5)"),
     B("5", "a gleich dem Kandidaten gesetzt"),
     B("2 * 5 + 5", "2 · 5 + 5 gerechnet, weil die 1 rechts mit (x − 5) und dem Faktor 2 verwechselt wurde")]), form="umkehren", lp=LP)
neu(T, "scheinloesung", "sicherung", "fehler", W(
    "Ina löst 5/(x − 1) + 2 = 7/(x − 1). Sie multipliziert mit (x − 1) und schreibt: „5 + 2 = 7. Das stimmt immer, also sind alle Zahlen Lösung.“ Welche Aussage über Inas Rechnung ist richtig?",
    "Fehler: Auch das Glied 2 muss mit (x − 1) malgenommen werden; richtig wäre 5 + 2(x − 1) = 7 und damit L = {2}.",
    [("Fehler: Die Zahl 1 ist ausgeschlossen; richtig wäre L = ℚ \\ {1}.", "nur die Definitionsmenge beachtet; die Gleichung gilt nicht für jedes x ≠ 1, nur für x = 2"),
     ("Fehler: Die Rechnung 5 + 2 = 7 ist falsch; richtig wäre L = { }.", "die Rechnung 5 + 2 = 7 für falsch gehalten; sie stimmt, aber sie gehört nicht zur richtig umgeformten Gleichung"),
     ("Fehler: Es gibt nur die Lösung x = 1; richtig wäre L = {1}.", "die verbotene Zahl 1 als Lösung genommen; bei x = 1 ist der Nenner 0")],
    "Beim Malnehmen mit (x − 1) wird jedes Glied malgenommen, auch die 2: 5 + 2(x − 1) = 7. Das gibt 2x + 3 = 7, also x = 2. Die 2 liegt in D = ℚ \\ {1}. Probe: 5/1 + 2 = 7 und 7/1 = 7. "
    "Inas Gleichung „5 + 2 = 7“ hat das 2 nicht mit (x − 1) malgenommen.",
    lambda: F(5, 2 - 1) + 2 == F(7, 2 - 1) and all(bruch_gl("F(5)/(x-1) + 2", "F(7)/(x-1)", x)[0] != bruch_gl("F(5)/(x-1) + 2", "F(7)/(x-1)", x)[1] for x in range(-9, 10) if x not in (1, 2))), form="fehler_detektiv", lp=LP)
neu(T, "scheinloesung", "sicherung", "verknuepfen", Z(
    "Wie viele ganze Zahlen von −2 bis 5 (einschließlich) liegen in der Lösungsmenge von (x² − 6x + 9)/(x − 3) = x − 3?",
    7, "8 - 1", sum(1 for x in range(-2, 6) if x != 3 and F(x * x - 6 * x + 9, x - 3) == x - 3),
    "Der Zähler ist eine binomische Formel: x² − 6x + 9 = (x − 3)². Für x ≠ 3 gilt (x − 3)²/(x − 3) = x − 3, die Gleichung ist also für jede Zahl aus D wahr: L = ℚ \\ {3}. "
    "Von den 8 ganzen Zahlen −2, −1, 0, 1, 2, 3, 4, 5 gehört die 3 nicht dazu. Es bleiben 7 Zahlen.",
    [B("8", "die ausgeschlossene Zahl 3 mitgezählt"),
     B("0", "geglaubt, dass es wegen des verbotenen Wertes 3 keine Lösung gibt"),
     B("8 - 8", "den Kandidaten x = 3 für die einzige Lösung gehalten und dann aus der Anzahl 1 die Anzahl 8 abgezogen")], einheit="Zahlen"), lp=LP)
# ───────── verhaeltnis ─────────
neu(T, "verhaeltnis", "test", "transfer", W(
    "Ein 1,5 m langer Stab wirft zur selben Zeit einen 2 m langen Schatten. Ein Baum wirft einen 12 m langen Schatten. Welche Aussage über die Höhe h des Baumes ist richtig? (Sonne und Boden sind gleich.)",
    "h : 12 = 1,5 : 2, also h = 9 m.",
    [("h : 12 = 2 : 1,5, also h = 16 m.", "das Verhältnis Schatten zu Höhe auf der einen Seite und Höhe zu Schatten auf der anderen Seite gemischt"),
     ("h : 1,5 = 2 : 12, also h = 0,25 m.", "Höhe und Schatten vertauscht: Stab und Baum stehen nicht auf der richtigen Seite"),
     ("h − 1,5 = 12 − 2, also h = 11,5 m.", "additiv statt proportional gerechnet; ein längerer Schatten bedeutet nicht denselben Zuwachs bei der Höhe")],
    "Zur selben Zeit ist das Verhältnis Höhe : Schatten bei Stab und Baum gleich: 1,5 : 2 = h : 12. Außenglieder mal Außenglieder: 2h = 1,5 · 12 = 18 (Innenglieder: 1,5 · 12; Außenglieder: 2 · h). Also h = 9 m. "
    "Probe: 9 : 12 = 3 : 4 und 1,5 : 2 = 3 : 4.",
    lambda: F("1.5") / 2 == F(9, 12) and F(12) * F("1.5") / 2 == 9 and F(12) * 2 / F("1.5") == 16 and F("1.5") * 2 / 12 == F(1, 4) and 12 - 2 + F("1.5") == F("11.5")), form="bruecke", lp=LP)
neu(T, "verhaeltnis", "korrektur", "einkleidung", Z(
    "Ein Foto ist 12 cm breit und 18 cm hoch. Es wird so vergrößert, dass es 30 cm breit ist, ohne dass sich das Seitenverhältnis ändert. Wie hoch ist das vergrößerte Foto in cm?",
    45, "18 * 30 / 12", "18 * 5 / 2",
    "Das Verhältnis Höhe : Breite bleibt gleich: h : 30 = 18 : 12. Außenglieder: h und 12, Innenglieder: 30 und 18. Also 12h = 30 · 18 = 540 und h = 45 cm. Der Vergrößerungsfaktor 30 : 12 = 2,5 gilt für beide Seiten: 18 · 2,5 = 45.",
    [B("18 + (30 - 12)", "additiv gerechnet: Die Breite wuchs um 18 cm, also wuchs auch die Höhe um 18 cm"),
     B("18 * 12 / 30", "das Verhältnis falsch herum angesetzt: 18 · 12 : 30")], einheit="cm"), form="anwenden", lp=LP)
neu(T, "verhaeltnis", "korrektur", "darstellung", W(
    "In einer Farbmischung verhalten sich die roten zu den blauen Teilen wie 3 : 5. Welchen Anteil der ganzen Mischung macht das Rot aus?",
    "3/8",
    [("3/5", "das Verhältnis Rot : Blau als Anteil an der Mischung gelesen; die 5 Teile Blau gehören nicht zum Rot"),
     ("5/8", "den Anteil des Blau genommen statt des Rot"),
     ("3/2", "Rot durch die Differenz 5 − 3 geteilt")],
    "Das Verhältnis 3 : 5 vergleicht die Teile Rot und Blau. Die ganze Mischung hat 3 + 5 = 8 Teile, davon sind 3 Teile rot. Der Anteil Rot ist also 3/8 (37,5 %). Das Blau macht 5/8 aus.",
    lambda: F(3, 3 + 5) == F(3, 8) and F(3, 5) != F(3, 8) and F(5, 8) != F(3, 8)), form="bruecke", lp=LP)
neu(T, "verhaeltnis", "sicherung", "mehrschritt", Z(
    "Drei Geschwister teilen 540 € im Verhältnis 2 : 3 : 4. Wie viel Euro bekommt das Geschwister mit dem größten Anteil?",
    240, "540 / (2 + 3 + 4) * 4", "540 * 4 / 9",
    "Insgesamt gibt es 2 + 3 + 4 = 9 Teile. Ein Teil ist 540 € : 9 = 60 €. Der größte Anteil sind 4 Teile: 4 · 60 € = 240 €. Probe: 2 · 60 + 3 · 60 + 4 · 60 = 120 + 180 + 240 = 540.",
    [B("540 / 9 * 3", "mit 3 Teilen statt mit 4 Teilen gerechnet (der mittlere Anteil)"),
     B("540 / 4", "durch 4 statt durch die Summe 9 aller Teile geteilt"),
     B("540 / 9", "nur den Wert eines Teils angegeben")], einheit="€"), lp=LP)
neu(T, "verhaeltnis", "sicherung", "fehler", W(
    "Lena löst die Verhältnisgleichung 4 : x = 6 : 18 so: „Außenglieder mal Innenglieder: 4 · x = 6 · 18, also x = 108 : 4 = 27.“ Welche Aussage über Lenas Rechnung ist richtig?",
    "Fehler: Die Außenglieder sind 4 und 18, die Innenglieder x und 6; richtig wäre 4 · 18 = 6 · x, also x = 12.",
    [("Fehler: Die Verhältnisse müssen addiert werden; richtig wäre 4 + x = 6 + 18, also x = 20.", "additiv statt multiplikativ; das Verhältnis bleibt nicht gleich, wenn man dieselbe Zahl addiert"),
     ("Kein Fehler: Die Probe 4 · 27 = 108 = 6 · 18 geht auf; richtig wäre also x = 27.", "die Probe mit derselben falschen Zuordnung gemacht; 4 : 27 ist nicht gleich 6 : 18"),
     ("Fehler: Das Ergebnis muss noch halbiert werden; richtig wäre x = 13,5.", "ohne Begründung halbiert; der Fehler liegt in der Zuordnung der Glieder")],
    "In 4 : x = 6 : 18 sind 4 und 18 die Außenglieder, x und 6 die Innenglieder. Also 4 · 18 = x · 6, das heißt 72 = 6x und x = 12. Probe: 4 : 12 = 1 : 3 und 6 : 18 = 1 : 3. "
    "Lena hat x mit 4 gekreuzt, das gehört nicht zusammen.",
    lambda: F(4, 12) == F(6, 18) and F(4, 27) != F(6, 18) and F(4, 20) != F(6, 18) and F(4, 13.5 if False else 27, 2) != F(6, 18) and 4 * 27 == 6 * 18), form="fehler_detektiv", lp=LP)
neu(T, "verhaeltnis", "sicherung", "parameter", Z(
    "Zwei Zahlen verhalten sich wie 5 : 7. Addiert man zu jeder der beiden Zahlen 6, verhalten sich die neuen Zahlen wie 3 : 4. Welche der beiden ursprünglichen Zahlen ist die kleinere?",
    30, "5 * 6", next(a for a in range(1, 400) for b in [F(7 * a, 5)] if b.denominator == 1 and F(a + 6, b + 6) == F(3, 4)),
    "Die Zahlen sind 5k und 7k. Nach dem Addieren gilt (5k + 6) : (7k + 6) = 3 : 4. Außenglieder mal Innenglieder: 4(5k + 6) = 3(7k + 6), also 20k + 24 = 21k + 18 und k = 6. "
    "Die Zahlen sind 30 und 42. Probe: 36 : 48 = 3 : 4. Die kleinere Zahl ist 30.",
    [B("7 * 6", "die größere der beiden Zahlen (42) angegeben"),
     B("5 * 6 + 6", "die kleinere neue Zahl 36 statt der ursprünglichen angegeben"),
     B("6", "nur den Faktor k = 6 angegeben")]), form="umkehren", lp=LP)
