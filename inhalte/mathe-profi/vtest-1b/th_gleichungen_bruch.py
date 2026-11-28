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



REGEL[(T, "definitionsmenge")] = REGEL[(T, "scheinloesung")] = "id.algebra.erlaubte_zahlen"
REGEL[(T, "ueber_kreuz")] = "rr.waage"
REGEL[(T, "verhaeltnis")] = "rr.verhaeltnis"
ABG[(T, "definitionsmenge")] = "Die Übungen bestimmen D bei einem Nenner; hier kommen mehrere Nenner, Fehlersuche, Sachaufgaben und die Frage dazu, was D mit der Lösungsmenge zu tun hat."
ABG[(T, "ueber_kreuz")] = "Die Übungen lösen mit dem Über-Kreuz-Verfahren; hier wird entschieden, wann es erlaubt ist, wie sich die Gleichung dabei umformt und wann eine Gleichung keine Lösung hat."
ABG[(T, "scheinloesung")] = "Die Übungen prüfen eine Lösung gegen D; hier wird begründet, warum eine Scheinlösung keine Lösung ist, wann eine Gleichung für alle Zahlen aus D gilt und wann kein Kandidat übrig bleibt."
ABG[(T, "verhaeltnis")] = "Die Übungen lösen eine Verhältnisgleichung; hier wird begründet, warum Verhältnisse nicht additiv wachsen, aus Teilen auf das Ganze geschlossen und ein Fehler im Ansatz gefunden."
# ───────── definitionsmenge ─────────
neu(T, "definitionsmenge", "test", "begruenden", Z(
    "Beim Lösen von 3/(x − 2) = 1/(x − 2) + 2/(x − 2) multipliziert Jan beide Seiten mit (x − 2) und erhält 3 = 1 + 2. Er sagt: „Jetzt stehen keine Nenner mehr da, also gibt es keine Einschränkung.“ Wie viele der ganzen Zahlen von −12 bis 12 (einschließlich) sind Lösung der Ausgangsgleichung?",
    24, "25 - 1", sum(1 for x in range(-12, 13) if x != 2 and F(3, x - 2) == F(1, x - 2) + F(2, x - 2)),
    "Die Definitionsmenge bestimmt man an der Ausgangsgleichung: Der Nenner x − 2 darf nicht 0 werden, also D = ℚ \\ {2}. Nach dem Malnehmen mit (x − 2) steht 3 = 1 + 2, eine für jedes x wahre Aussage. Also ist jede Zahl aus D eine Lösung, die Zahl 2 aber nicht, weil die Brüche für x = 2 nicht definiert sind. "
    "Von den 25 ganzen Zahlen −12 bis 12 bleiben 24.",
    [B("25", "die Zahl 2 mitgezählt, obwohl für x = 2 der Nenner 0 wird"),
     B("0", "die immer wahre Aussage nach dem Malnehmen als „keine Lösung“ gedeutet"),
     B("1", "nur die verbotene Zahl 2 als Lösung genommen")], einheit="Zahlen"), lp=LP, idee="identitaet_und_D")
neu(T, "definitionsmenge", "korrektur", "umkehr", L(
    "Für wie viele rationale Zahlen ist die Gleichung 5/(x² + 4) = 1 nicht definiert, und wie viele Lösungen hat sie?",
    "nicht definiert für □ Zahlen, □ Lösungen", [0, 2], ["0", "2"], ["1 - 1", "1 + 1"],
    "Der Nenner x² + 4 ist nie 0, denn x² ist nie negativ und x² + 4 ist mindestens 4. Also ist keine Zahl verboten, D = ℚ. Aus 5 = x² + 4 folgt x² = 1 und damit x = 1 oder x = −1: zwei Lösungen. Beide sind erlaubt.",
    {0: [(2, "die Nullstellen von x² + 4 wie bei x² − 4 gesucht und zwei verbotene Zahlen angegeben", "1 + 1"), (1, "nur eine verbotene Zahl, nämlich x = 0, angegeben", "1")],
     1: [(1, "nur die positive Lösung x = 1 angegeben", "1"), (0, "geglaubt, die Gleichung habe keine Lösung, weil der Nenner nie 0 wird", "1 - 1"), (4, "alle vier Zahlen ±1 und ±2 als Lösungen gezählt", "2 + 2")]}),
    lp=LP, idee="nie_null")
neu(T, "definitionsmenge", "korrektur", "umkehr", Z(
    "Die Gleichung 6/(2x − a) + 4/(x + 3) = 2 hat die Definitionsmenge ℚ \\ {−3; 7}. Welche Zahl ist a?",
    14, "2 * 7", "14",
    "Die Zahl −3 kommt vom Nenner x + 3. Die Zahl 7 muss vom Nenner 2x − a kommen: 2 · 7 − a = 0, also a = 14. Probe: 2x − 14 = 0 gibt x = 7. Mit a = 7 wäre 2x − 7 = 0 bei x = 3,5, nicht bei 7.",
    [B("7", "a gleich der ausgeschlossenen Zahl 7 gesetzt; der Faktor 2 vor dem x wurde übersehen"),
     B("-2 * 7", "den Wert a mit falschem Vorzeichen übernommen: −(2 · 7)"),
     B("7 / 2", "durch 2 geteilt statt mit 2 malgenommen: 7 : 2")]), form="umkehren", lp=LP, idee="umkehr_D")
neu(T, "definitionsmenge", "korrektur", "darstellung", W(
    "Welche Menge ist die Definitionsmenge der Gleichung 4/(x² − 16) + 1/x = 2?",
    "D = ℚ \\ {−4; 0; 4}",
    [("D = ℚ \\ {−16; 0; 16}", "x² − 16 = 0 so gelesen, als sei x = 16 und x = −16 gemeint; gesucht sind aber die Zahlen, deren Quadrat 16 ist"),
     ("D = ℚ \\ {−4; 4}", "den zweiten Nenner x nicht beachtet; für x = 0 ist 1/x nicht definiert"),
     ("D = ℚ \\ {0; 4}", "von x² = 16 nur die Lösung 4 genommen und −4 vergessen")],
    "x² − 16 = (x − 4)(x + 4) ist 0 für x = 4 und x = −4; der Nenner x ist 0 für x = 0. Alle drei Zahlen müssen ausgeschlossen werden.",
    lambda: {x for x in range(-20, 21) if x * x - 16 == 0 or x == 0} == {-4, 0, 4} and {x for x in range(-20, 21) if x * x - 16 == 0 or x == 0} != {-16, 0, 16}), lp=LP, idee="menge_zuordnen")
neu(T, "definitionsmenge", "sicherung", "einkleidung", Z(
    "Ein Drucker allein braucht x Minuten für einen Auftrag, ein zweiter braucht 5 Minuten weniger, also x − 5 Minuten. Zusammen schaffen sie den Auftrag in 3 Minuten, das gibt die Gleichung 1/x + 1/(x − 5) = 1/3. Beide Druckzeiten müssen positive Zeiten sein. Wie viele ganze Zahlen von −3 bis 9 (einschließlich) kommen für x infrage?",
    4, "9 - 5", sum(1 for x in range(-3, 10) if x > 5),
    "Die Nenner x und x − 5 dürfen nicht 0 sein, also fallen 0 und 5 weg. Das reicht hier aber nicht: Eine Druckzeit ist eine positive Zahl. Aus x > 0 und x − 5 > 0 folgt x > 5. Von den ganzen Zahlen −3 bis 9 erfüllen das nur 6, 7, 8 und 9, also 4 Zahlen. Die Definitionsmenge allein (11 Zahlen) beschreibt nur, wann die Gleichung einen Sinn hat, nicht, wann die Aufgabe einen Sinn hat.",
    [B("13 - 2", "nur die Nenner beachtet und 0 und 5 ausgeschlossen, aber nicht verlangt, dass beide Zeiten positiv sind"),
     B("9 - 5 + 1", "die Zahl 5 mitgezählt, obwohl die zweite Druckzeit dann 0 Minuten wäre"),
     B("13", "keine Bedingung beachtet und alle Zahlen gezählt")], einheit="Zahlen"), form="bruecke", lp=LP, idee="text_zu_D")
neu(T, "definitionsmenge", "sicherung", "fehler", L(
    "Mara löst 8/(x − 5) = 2 und schreibt: Zeile 1: Mal (x − 5) gibt 8 = 2 · (x − 5). Zeile 2: Also 8 = 2x − 10 und x = 9. Zeile 3: Also ist 9 die Zahl, die man nicht einsetzen darf: D = ℚ \\ {9}. In welcher Zeile steckt der erste Fehler, und welche Zahl ist richtig aus D ausgeschlossen?",
    "Fehler in Zeile □, ausgeschlossene Zahl: □", [3, 5], ["3", "10 / 2"], ["4 - 1", "9 - 4"],
    "Zeile 1 und Zeile 2 sind richtig: x = 9 ist die Lösung der Gleichung. In Zeile 3 steckt der Fehler: Die Definitionsmenge hängt nur vom Nenner ab. Der Nenner x − 5 ist für x = 5 gleich 0, also ist D = ℚ \\ {5}. Die Lösung 9 ist erlaubt und kein verbotener Wert. Probe: 8/(9 − 5) = 2.",
    {0: [(2, "den richtigen Rechenschritt in Zeile 2 für den Fehler gehalten", "1 + 1"), (1, "Zeile 1 genannt, obwohl dort richtig mit dem Nenner malgenommen wird", "1")],
     1: [(9, "die Lösung der Gleichung als ausgeschlossene Zahl genommen", "9"), (0, "geglaubt, es sei keine Zahl ausgeschlossen, weil der Nenner nicht x selbst ist", "1 - 1"), (10, "die Zahl 10 aus Zeile 2 als ausgeschlossen genommen", "10")]}), form="fehler_detektiv", lp=LP, idee="loesung_und_verbot_verwechselt")
neu(T, "definitionsmenge", "sicherung", "einkleidung", W(
    "Kinder teilen sich die Kosten von 36 € für ein Taxi gleichmäßig; es sind x Kinder. Kommen 3 weitere Kinder mit, zahlt jedes Kind 2 € weniger. Welche Gleichung beschreibt das, und welche Werte kommen für x als Kinderzahl in Frage?",
    "36/x − 36/(x + 3) = 2, und als Kinderzahl kommen nur positive ganze Zahlen in Frage, denn x zählt Kinder.",
    [("36/x − 36/(x + 3) = 2, und für x kommen alle rationalen Zahlen außer −3 und 0 in Frage, denn nur dort wird ein Nenner 0.", "die Definitionsmenge der Gleichung mit den Werten verwechselt, die in der Sachaufgabe möglich sind"),
     ("36/x + 36/(x + 3) = 2, und als Kinderzahl kommen nur positive ganze Zahlen in Frage, denn x zählt Kinder.", "die beiden Kosten addiert; mit den Zusatzkindern zahlt jedes weniger, der Unterschied ist 2 €"),
     ("36/(x − 3) − 36/x = 2, und für x kommen alle rationalen Zahlen außer 0 und 3 in Frage, denn dort wird ein Nenner 0.", "die 3 weiteren Kinder abgezogen statt dazugezählt, und die Menge der Kinderzahlen mit der Definitionsmenge verwechselt")],
    "Mit x Kindern zahlt jedes 36/x €. Mit 3 weiteren Kindern sind es x + 3 Kinder, und jedes zahlt 36/(x + 3) €, das sind 2 € weniger: 36/x − 36/(x + 3) = 2. Die Definitionsmenge der Gleichung ist ℚ \\ {−3; 0}. Für die Aufgabe ist x aber eine Kinderzahl, also eine positive ganze Zahl; Definitionsmenge und Menge der sinnvollen Werte sind zwei verschiedene Mengen. Probe mit x = 6: 36/6 − 36/9 = 6 − 4 = 2.",
    lambda: F(36, 6) - F(36, 9) == 2 and F(36, 6) + F(36, 9) != 2 and F(36, 3) - F(36, 6) != 2), form="bruecke", lp=LP, idee="modell_aufstellen")
# ───────── ueber_kreuz ─────────
def _kreuz_zahl():
    # (A) (x+2)/4 = 3/(x-1)  ja; (B) 1/x + 1/2 = 3/(x-1) nein; (C) 5/(x+1) = 2 ja (2 = 2/1); (D) 6/(x-2) = 4/x + 1 nein; (E) (2x)/3 = 5/(x+1) ja
    erlaubt = {"A": (1, 1), "B": (2, 1), "C": (1, 1), "D": (1, 2), "E": (1, 1)}   # Anzahl der obersten Brüche links/rechts: nur (1, 1) erlaubt
    return sum(1 for v in erlaubt.values() if v == (1, 1))


neu(T, "ueber_kreuz", "test", "parameter", Z(
    "Für wie viele ganze Zahlen k von −5 bis 14 (einschließlich) hat die Gleichung 4/(x − 1) = k/(x + 2) mindestens eine Lösung?",
    18, "20 - 2", "18",
    "Über Kreuz: 4(x + 2) = k(x − 1), also (4 − k)x = −k − 8. Für k = 4 steht 0 · x = −12: keine Lösung. Für k = 0 folgt 4x = −8, also x = −2; das ist aber ausgeschlossen (Nenner x + 2), eine Scheinlösung. Für alle anderen k gibt es x = (−k − 8)/(4 − k), das weder 1 noch −2 ist. Von den 20 Zahlen von −5 bis 14 haben also 20 − 2 = 18 eine Lösung (alle außer 0 und 4).",
    [B("20 - 1", "nur k = 4 als Zahl ohne Lösung gefunden und die Scheinlösung bei k = 0 übersehen"),
     B("20", "geglaubt, dass sich für jedes k eine Lösung findet"),
     B("20 - 3", "einen weiteren Wert von k ausgeschlossen, für den es doch eine Lösung gibt")], einheit="Zahlen"), lp=LP, idee="parameter_keine_loesung")
neu(T, "ueber_kreuz", "korrektur", "darstellung", W(
    "Kim will die Gleichung 4/(x − 1) = 7/(x + 3) ohne Brüche und ohne Klammern schreiben und rechnet dazu über Kreuz. Welche Gleichung steht danach da?",
    "4x + 12 = 7x − 7",
    [("4x − 4 = 7x + 21", "jeden Zähler mit dem eigenen Nenner malgenommen; über Kreuz heißt Zähler links mal Nenner rechts"),
     ("4x + 3 = 7x − 1", "beim Ausmultiplizieren nur das x mit dem Zähler malgenommen und die Zahl in der Klammer vergessen"),
     ("4x + 12 = 7x + 7", "beim Ausmultiplizieren das Minuszeichen in der Klammer verloren")],
    "Über Kreuz: Der Zähler links (4) wird mit dem Nenner rechts (x + 3) malgenommen, der Zähler rechts (7) mit dem Nenner links (x − 1): 4(x + 3) = 7(x − 1). Ausmultiplizieren gibt 4x + 12 = 7x − 7. Probe: Die Lösung dieser Gleichung ist x = 19/3, und dort gilt 4/(16/3) = 3/4 = 7/(28/3).",
    lambda: F(4) / (F(19, 3) - 1) == F(7) / (F(19, 3) + 3) and 4 * F(19, 3) + 12 == 7 * F(19, 3) - 7 and 4 * F(19, 3) - 4 != 7 * F(19, 3) + 21 and 4 * F(19, 3) + 3 != 7 * F(19, 3) - 1 and 4 * F(19, 3) + 12 != 7 * F(19, 3) + 7),
    lp=LP, idee="umformen_darstellung")
neu(T, "ueber_kreuz", "korrektur", "umkehr", W(
    "Welche der folgenden Gleichungen hat die Lösung x = 6?",
    "4/(x − 2) = 2/(x − 4)",
    [("4/(x − 2) = 2/(x + 4)", "für x = 6 links 1 und rechts einen kleineren Wert; das Vorzeichen im rechten Nenner wurde nicht beachtet"),
     ("4/(x + 2) = 2/(x − 4)", "für x = 6 links einen kleineren Wert als rechts; das Vorzeichen im linken Nenner wurde nicht beachtet"),
     ("4/(x − 4) = 2/(x − 2)", "die beiden Nenner vertauscht; für x = 6 steht links das Vierfache von rechts")],
    "Man setzt x = 6 ein. 4/(6 − 2) = 1 und 2/(6 − 4) = 1: Beide Seiten sind gleich, die erste Gleichung hat die Lösung 6. Bei den anderen steht links 4/(6 − 2) = 1 gegen 2/10, 4/8 gegen 2/2 und 4/2 gegen 2/4.",
    lambda: F(4, 6 - 2) == F(2, 6 - 4) and F(4, 6 - 2) != F(2, 6 + 4) and F(4, 6 + 2) != F(2, 6 - 4) and F(4, 6 - 4) != F(2, 6 - 2)), lp=LP, idee="gleichung_zur_loesung")
neu(T, "ueber_kreuz", "korrektur", "mehrschritt", W(
    "Zwei Kinder lösen 6/(x − 2) = 3/4. Kim multipliziert über Kreuz. Jo überlegt: „Der Zähler 6 ist doppelt so groß wie der Zähler 3, also muss auch der Nenner x − 2 doppelt so groß sein wie 4.“ Welche Aussage stimmt?",
    "Beide erhalten x = 10, denn ein doppelter Zähler verlangt auch einen doppelten Nenner.",
    [("Nur Kim darf so rechnen, denn Jos Überlegung ist keine erlaubte Rechenregel.", "Jos Überlegung für ungültig gehalten, obwohl sie dieselbe Gleichheit der Verhältnisse nutzt"),
     ("Jo erhält x = 6, denn x − 2 muss doppelt so groß sein wie 3 und nicht wie 4.", "den Nenner 3 statt 4 verdoppelt und die Brüche verwechselt"),
     ("Kim erhält x = 6, denn aus 6 · 4 = 3 · (x − 2) folgt x − 2 = 4 und damit x = 6.", "24 : 3 falsch zu 4 statt 8 gerechnet")],
    "Kim: 6 · 4 = 3 · (x − 2), also 24 = 3x − 6 und x = 10. Jo: 6/3 = 2, also muss (x − 2)/4 = 2 sein, x − 2 = 8 und x = 10. Beide Wege führen zu x = 10, und beide sind erlaubt: Aus a/b = c/d folgt a : c = b : d. Probe: 6/8 = 3/4.",
    lambda: F(6, 10 - 2) == F(3, 4) and 6 * 4 == 3 * (10 - 2) and F(6, 3) * 4 == 10 - 2 and 10 != 6), form="zwei_wege", lp=LP, idee="zwei_wege")
neu(T, "ueber_kreuz", "sicherung", "fehler", L(
    "Mara löst 4/(x − 1) + 1 = 7/(x + 3) so: Zeile 1: Über Kreuz: 4 · (x + 3) + 1 = 7 · (x − 1). Zeile 2: 4x + 13 = 7x − 7. Zeile 3: Also 3x = 20 und x = 20/3. In welcher Zeile steckt der erste Fehler, und darf man hier einfach über Kreuz multiplizieren (1 = ja, 0 = nein)?",
    "Fehler in Zeile □, über Kreuz erlaubt: □", [1, 0], ["1", "0"], ["3 - 2", "1 - 1"],
    "Über Kreuz darf man nur multiplizieren, wenn auf jeder Seite genau ein Bruch steht. Links steht aber 4/(x − 1) + 1, eine Summe. Zeile 1 ist falsch: Erst muss die linke Seite zu einem Bruch werden, 4/(x − 1) + 1 = (4 + x − 1)/(x − 1) = (x + 3)/(x − 1); dann darf man über Kreuz multiplizieren. Zeile 2 und 3 rechnen mit dem falschen Ansatz richtig weiter.",
    {0: [(2, "den Rechenschritt in Zeile 2 für falsch gehalten, obwohl er dem Ansatz folgt", "1 + 1"), (3, "die Schlusszeile genannt, weil dort das gebrochene Ergebnis steht", "3")],
     1: [(1, "geglaubt, über Kreuz sei immer erlaubt, sobald auf jeder Seite ein Bruch vorkommt", "1")]}),
    form="fehler_detektiv", lp=LP, idee="fehler_summe")

def _zaehle_ohne_loesung():
    n = 0
    for k in range(-4, 5):
        # 4/(x-1) = k/(x+2): (4 - k)x = -k - 8
        a, b = 4 - k, -k - 8
        ok = (b == 0) if a == 0 else (F(b, a) not in (1, -2))
        n += 0 if ok else 1
    return n
_ZWEIT_K = _zaehle_ohne_loesung()
neu(T, "ueber_kreuz", "sicherung", "begruenden", W(
    "Kim löst 3/x = 5/(x + 2) und schreibt: „Also gilt 3 · (x + 2) = 5 · x.“ Welche Aussage über Kims Schritt stimmt?",
    "Kim hat recht, denn mit x · (x + 2) malgenommen kürzt sich auf jeder Seite ein Nenner.",
    [("Kim irrt, denn über Kreuz hätte 3 · x = 5 · (x + 2) dastehen müssen.", "die Faktoren beim Über-Kreuz-Multiplizieren falsch zugeordnet, obwohl Kims Schritt stimmt"),
     ("Kim irrt, denn über Kreuz gilt nur, wenn beide Nenner gleich sind.", "geglaubt, über Kreuz sei nur bei gleichen Nennern erlaubt"),
     ("Kim irrt, denn man muss zuerst alle Brüche addieren und dann malnehmen.", "das Addieren von Brüchen mit dem Malnehmen beim Auflösen von Gleichungen verwechselt")],
    "Multipliziert man beide Seiten mit x · (x + 2), erhält man links 3/x · x · (x + 2) = 3 · (x + 2) und rechts 5/(x + 2) · x · (x + 2) = 5 · x. Das ist genau das Kreuzprodukt. Voraussetzung ist, dass x und x + 2 nicht 0 sind. Probe mit x = 3: 3/3 = 1 und 5/5 = 1.",
    lambda: F(3, 3) == F(5, 5) and 3 * (3 + 2) == 5 * 3), lp=LP, idee="warum_ueber_kreuz")
neu(T, "ueber_kreuz", "sicherung", "darstellung", Z(
    "Zu Zähler und Nenner des Bruchs 5/11 wird dieselbe Zahl addiert. Der neue Bruch ist gleich 2/3. Welche Zahl wurde addiert?",
    7, "22 - 15", "(2 * 11 - 3 * 5) / (3 - 2)",
    "Die gesuchte Zahl sei x. Dann gilt (5 + x)/(11 + x) = 2/3. Über Kreuz: 3 · (5 + x) = 2 · (11 + x), also 15 + 3x = 22 + 2x und x = 7. Probe: 12/18 = 2/3. Beide Zahlen werden um 7 größer, der Unterschied 6 zwischen Nenner und Zähler bleibt gleich.",
    [B("11 - 5", "die Differenz von Nenner und Zähler als gesuchte Zahl genommen"),
     B("3 * 11 - 2 * 5", "über Kreuz mit vertauschten Brüchen gerechnet und die Unbekannte nicht abgezogen"),
     B("22 - 15 + 5", "zum richtigen Ergebnis noch den Zähler 5 addiert")], einheit=""), lp=LP, idee="zahl_zu_zaehler_nenner")
# ───────── scheinloesung ─────────
neu(T, "scheinloesung", "test", "transfer", Z(
    "Für wie viele ganze Zahlen b von −9 bis 9 (einschließlich) hat die Gleichung (x + b)/(x − 4) = 3/(x − 4) + 1 keine Lösung?",
    18, "19 - 1", "18",
    "Beide Seiten mit (x − 4) malgenommen: x + b = 3 + (x − 4), also x + b = x − 1. Das x fällt weg, übrig bleibt b = −1. Für b = −1 ist die Gleichung für jedes x ≠ 4 wahr, es gibt unendlich viele Lösungen. Für jedes andere b steht eine falsche Aussage da, es gibt keine Lösung. Von den 19 Zahlen von −9 bis 9 ist nur b = −1 ausgenommen, also haben 18 keine Lösung.",
    [B("19", "geglaubt, dass die Gleichung für jedes b ohne Lösung bleibt"),
     B("1", "b = −1 als einzigen Wert ohne Lösung gezählt, den Fall mit unendlich vielen Lösungen verwechselt"),
     B("19 - 2", "zusätzlich den Wert b = 3 (Zahl im Zähler der rechten Seite) als Lösungsfall gezählt")], einheit="Zahlen"), lp=LP, idee="parameter_identitaet")
neu(T, "scheinloesung", "korrektur", "darstellung", W(
    "Eine Bruchgleichung hat die Definitionsmenge ℚ \\ {−2; 3}. Nach dem Multiplizieren mit den Nennern und Umformen steht da x² = 9. Welche Aussage über die Lösungsmenge L stimmt?",
    "L = {−3}, denn von den beiden Zahlen mit dem Quadrat 9 gehört nur −3 zu D.",
    [("L = {−3; 3}, denn beide Zahlen erfüllen die Gleichung x² = 9.", "die Gleichung nach dem Umformen gelöst, aber die Zahlen nicht mit D verglichen"),
     ("L = {3}, denn x² = 9 ergibt x = 3.", "die zweite Lösung −3 vergessen und die verbotene Zahl 3 als Lösung genommen"),
     ("L = { }, denn die Zahl 3 ist ausgeschlossen und deshalb gibt es keine Lösung.", "eine ausgeschlossene Zahl so gewertet, als sei die ganze Gleichung unlösbar; die zweite Zahl −3 ist erlaubt")],
    "Aus x² = 9 folgen die Kandidaten x = 3 und x = −3. Die Zahl 3 gehört nicht zu D = ℚ \\ {−2; 3}: Für x = 3 wäre ein Nenner 0 (Scheinlösung). Die Zahl −3 gehört zu D und bleibt Lösung: L = {−3}.",
    lambda: {x for x in (3, -3) if x not in (-2, 3)} == {-3} and 3 * 3 == 9 and (-3) ** 2 == 9), lp=LP, idee="kandidaten_gegen_D")
_GL3 = [("(x+1)/(x-3)", "F(4)/(x-3)"), ("F(6)/(x+2)", "F(3)/(x+2) + 1"), ("F(3)/(x-2)", "F(4)/(x-2)")]
neu(T, "scheinloesung", "korrektur", "darstellung", Z(
    "Wie viele der folgenden drei Gleichungen haben mindestens eine Lösung? (A) (x + 1)/(x − 3) = 4/(x − 3); (B) 6/(x + 2) = 3/(x + 2) + 1; (C) 3/(x − 2) = 4/(x − 2).",
    1, "3 - 2", sum(1 for l, r in _GL3 if loesungen(l, r)),
    "(A): Mal (x − 3) gibt x + 1 = 4, also x = 3. Die 3 ist verboten: keine Lösung. (B): Mal (x + 2) gibt 6 = 3 + (x + 2), also x = 1. Die 1 ist erlaubt (D = ℚ \\ {−2}): Lösung. "
    "(C): Mal (x − 2) gibt 3 = 4, eine falsche Aussage: Es gibt gar keinen Kandidaten. Nur (B) hat eine Lösung, also genau 1 Gleichung.",
    [B("3", "für jede Gleichung eine Lösung angenommen, ohne die Kandidaten gegen D zu prüfen"),
     B("2", "bei Gleichung (C) die falsche Aussage 3 = 4 übersehen und sie mitgezählt"),
     B("0", "alle Gleichungen als unlösbar gewertet, auch die mit dem erlaubten Kandidaten x = 1")], einheit="Gleichungen"), lp=LP, idee="gleichungen_vergleichen")
neu(T, "scheinloesung", "korrektur", "umkehr", L(
    "Man löst 3/(x − 1) = 6/(x² − 1). Dabei ist x² − 1 = (x − 1)(x + 1). Nach dem Malnehmen mit (x − 1)(x + 1) ergibt sich als einziger Kandidat x = □, und die Gleichung hat □ Lösungen.",
    "Kandidat x = □, Zahl der Lösungen: □", [1, 0], ["3 - 2", "1 - 1"], ["6 / 3 - 1", "0"],
    "Mal (x − 1)(x + 1): links bleibt 3 · (x + 1), rechts bleibt 6. Aus 3x + 3 = 6 folgt x = 1. Die Zahl 1 macht aber die Nenner x − 1 und x² − 1 zu 0, gehört also nicht zu D = ℚ \\ {−1; 1}. Sie ist eine Scheinlösung: Die Gleichung hat keine Lösung.",
    {0: [(2, "aus x + 1 = 2 die 1 nicht abgezogen und x = 2 gelesen", "6 / 3"), (-1, "die zweite verbotene Zahl als Kandidaten genannt", "0 - 1")],
     1: [(1, "den Kandidaten als Lösung gezählt, ohne ihn gegen D zu prüfen", "1"), (2, "beide Nullstellen des Nenners als Lösungen gezählt", "1 + 1")]}), form=None, lp=LP, idee="scheinloesung_kuerzen")
neu(T, "scheinloesung", "sicherung", "fehler", L(
    "Ina löst 5/(x − 1) + 2 = 7/(x − 1) so: Zeile 1: Mal (x − 1) gibt 5 + 2 = 7. Zeile 2: Das stimmt für jede Zahl. Zeile 3: Also sind alle Zahlen Lösung. In welcher Zeile steckt der erste Fehler, und welche Zahl ist die einzige Lösung der Gleichung?",
    "Fehler in Zeile □, einzige Lösung: x = □", [1, 2], ["1", "2"], ["4 - 3", "(7 - 5) / 1"],
    "Beim Malnehmen mit (x − 1) muss jedes Glied malgenommen werden, auch die 2: 5 + 2(x − 1) = 7. Das gibt 2x + 3 = 7, also x = 2. Die 2 liegt in D = ℚ \\ {1}. Probe: 5/1 + 2 = 7 und 7/1 = 7. Zeile 1 ist der Fehler; Zeile 2 und 3 folgen daraus.",
    {0: [(2, "den zweiten Satz „Das stimmt für jede Zahl“ für den Fehler gehalten", "1 + 1"), (3, "die Schlusszeile genannt, weil dort „alle Zahlen“ steht", "3")], 1: [(1, "die verbotene Zahl 1 als Lösung genommen", "1"), (4, "aus 2x + 3 = 7 nur 7 − 3 gerechnet und nicht durch 2 geteilt", "7 - 3")]}), form="fehler_detektiv", lp=LP, idee="fehler_nicht_alle_glieder")
neu(T, "scheinloesung", "sicherung", "begruenden", W(
    "Kim löst (x + 2)/(x − 5) = 7/(x − 5). Sie multipliziert mit (x − 5), erhält x + 2 = 7 und damit x = 5. Zur Probe setzt sie x = 5 ein: „7/0 = 7/0, das stimmt also: L = {5}.“ Welche Aussage ist richtig?",
    "L = { }, denn die einzige Zahl, die beim Umformen herauskommt, macht den Nenner 0.",
    [("L = {5}, denn auf beiden Seiten steht bei x = 5 dasselbe, nämlich 7/0.", "gleiches Aussehen mit „stimmt“ verwechselt; durch 0 darf man nicht teilen, die Aussage 7/0 = 7/0 hat keinen Wert"),
     ("L = ℚ \\ {5}, denn ohne die 5 sind beide Seiten für jede andere Zahl gleich.", "gedacht, die Gleichung gelte für alle zugelassenen Zahlen; für x ≠ 5 ist x + 2 = 7 falsch, also sind die Seiten verschieden"),
     ("L = {5}, denn 7 : 0 ist 0, und 0 = 0 stimmt, die Probe geht also auf.", "7 : 0 mit 0 gleichgesetzt; die Division durch 0 ist nicht erklärt")],
    "Die Definitionsmenge ist D = ℚ \\ {5}, weil der Nenner x − 5 nicht 0 werden darf. Die Umformung liefert x = 5, aber 5 gehört nicht zu D. Für x = 5 sind beide Seiten nicht definiert, es gibt keine wahre Aussage. "
    "Für jedes x ≠ 5 ist die Gleichung gleichwertig zu x + 2 = 7, also falsch. Damit ist L = { }, und x = 5 ist eine Scheinlösung.",
    lambda: all(bruch_gl("(x+2)/(x-5)", "F(7)/(x-5)", x)[0] != bruch_gl("(x+2)/(x-5)", "F(7)/(x-5)", x)[1] for x in range(-20, 21) if x != 5) and bruch_gl("(x+2)/(x-5)", "F(7)/(x-5)", 5) is None), lp=LP, idee="probe_nenner_null")
neu(T, "scheinloesung", "sicherung", "darstellung", L(
    "Die Gleichung (x − 6)/(x + 3) = 0 hat die Lösung x = □. Die Gleichung (x − 4)/(x − 4) = 0 hat □ Lösungen.",
    "x = □ und □ Lösungen", [6, 0], ["6", "0"], ["12 / 2", "3 - 3"],
    "Ein Bruch ist 0, wenn der Zähler 0 ist und der Nenner nicht 0 ist. Bei (x − 6)/(x + 3) = 0 ist der Zähler für x = 6 gleich 0, und der Nenner ist dort 9, also ist x = 6 Lösung. Bei (x − 4)/(x − 4) ist der Zähler nur für x = 4 gleich 0, aber dort ist auch der Nenner 0. Für alle anderen Zahlen ist der Bruch 1. Also gibt es keine Lösung.",
    {0: [(-3, "den Nenner gleich 0 gesetzt statt den Zähler", "-3"), (3, "x + 3 = 0 und x − 6 = 0 vermischt und die Zahl 3 genommen", "6 - 3")],
     1: [(1, "den Bruch als 1 gekürzt und gedacht, es gebe genau eine Lösung", "1"), (4, "x = 4 als Lösung genommen, obwohl der Nenner dort 0 ist", "4")]}),
    lp=LP, idee="bruch_null")
# ───────── verhaeltnis ─────────
neu(T, "verhaeltnis", "test", "transfer", L(
    "Zwei Zahlen verhalten sich wie 2 : 3. Addiert man zu beiden Zahlen 10, verhalten sich die neuen Zahlen wie 3 : 4. Die ursprünglichen Zahlen sind □ und □.",
    "kleinere Zahl □, größere Zahl □", [20, 30], ["10 * 2", "10 * 3"], ["50 - 30", "40 - 10"],
    "Die Zahlen sind 2k und 3k. Nach dem Addieren gilt (2k + 10) : (3k + 10) = 3 : 4, über Kreuz 4 · (2k + 10) = 3 · (3k + 10), also 8k + 40 = 9k + 30 und k = 10. Die Zahlen sind 20 und 30. Probe: 30 : 40 = 3 : 4.",
    {0: [(10, "den Faktor k als Zahl angegeben", "10"), (2, "die Verhältniszahl statt der Zahl angegeben", "2")],
     1: [(3, "die Verhältniszahl statt der Zahl angegeben", "3"), (40, "die neue Zahl nach dem Addieren statt der ursprünglichen angegeben", "30 + 10")]}),
    lp=LP, idee="x_in_beiden_verhaeltnissen")
neu(T, "verhaeltnis", "korrektur", "darstellung", W(
    "In einer Farbmischung verhalten sich die roten zu den blauen Teilen wie 3 : 5. Welchen Anteil der ganzen Mischung macht das Rot aus?",
    "3/8",
    [("3/5", "das Verhältnis Rot : Blau als Anteil an der Mischung gelesen; die 5 Teile Blau gehören nicht zum Rot"),
     ("5/8", "den Anteil des Blau genommen statt des Rot"),
     ("3/2", "Rot durch die Differenz 5 − 3 geteilt")],
    "Das Verhältnis 3 : 5 vergleicht die Teile Rot und Blau. Die ganze Mischung hat 3 + 5 = 8 Teile, davon sind 3 Teile rot. Der Anteil Rot ist also 3/8 (37,5 %). Das Blau macht 5/8 aus.",
    lambda: F(3, 3 + 5) == F(3, 8) and F(3, 5) != F(3, 8) and F(5, 8) != F(3, 8)), form="bruecke", lp=LP, idee="anteil_aus_verhaeltnis")
neu(T, "verhaeltnis", "korrektur", "umkehr", Z(
    "In einer Obstschale liegen Äpfel und Birnen im Verhältnis 5 : 3. Nachdem 20 Äpfel gegessen wurden, liegen genauso viele Äpfel wie Birnen in der Schale. Wie viele Birnen liegen in der Schale?",
    30, "20 / (5 - 3) * 3", "10 * 3",
    "Zuerst sind es 5k Äpfel und 3k Birnen. Nach dem Essen von 20 Äpfeln gilt 5k − 20 = 3k, also 2k = 20 und k = 10. Es liegen 30 Birnen in der Schale. Probe: 50 Äpfel − 20 = 30, 30 Birnen.",
    [B("20 / (5 - 3) * 5", "die Zahl der Äpfel (50) vor dem Essen angegeben statt der Birnen"),
     B("20 / 5 * 3", "die 20 durch die Verhältniszahl 5 geteilt, statt durch den Unterschied der Verhältniszahlen"),
     B("20 * 3", "die gegessenen 20 Äpfel mit der Verhältniszahl 3 malgenommen")], einheit="Birnen"), form="umkehren", lp=LP, idee="abziehen_gleich")
neu(T, "verhaeltnis", "korrektur", "mehrschritt", W(
    "Ein Foto ist 12 cm breit und 18 cm hoch. Es wird so vergrößert, dass es 30 cm breit ist. Ben rechnet: Die Breite wächst um 18 cm, also wächst die Höhe auch um 18 cm. Ida rechnet: Die Breite wird mit 2,5 malgenommen, also auch die Höhe. Welche Aussage über die neue Höhe stimmt, wenn das Seitenverhältnis gleich bleiben soll?",
    "Die Höhe wird 45 cm, denn beide Seiten werden mit demselben Faktor 2,5 malgenommen.",
    [("Die Höhe wird 36 cm, denn die Höhe wächst genauso um 18 cm wie die Breite.", "additiv statt multiplikativ gerechnet: 18 + 18; gleiches Wachstum in cm ändert das Verhältnis"),
     ("Die Höhe wird 7,2 cm, denn man teilt die Höhe 18 cm durch den Faktor 2,5.", "durch den Faktor geteilt statt malgenommen: 18 : 2,5"),
     ("Die Höhe bleibt 18 cm, denn nur die Breite soll größer werden.", "Vergrößern mit „nur die Breite ändern“ verwechselt")],
    "Soll das Seitenverhältnis gleich bleiben, müssen beide Seiten mit demselben Faktor malgenommen werden: 30 : 12 = 2,5, also 18 · 2,5 = 45 cm Höhe. Bens Rechnung ergäbe 36 cm; dann wäre 36 : 30 = 1,2, aber das alte Verhältnis 18 : 12 = 1,5. Idas Weg stimmt.",
    lambda: F(30, 12) == F("2.5") and 18 * F("2.5") == 45 and F(36, 30) != F(18, 12) and F(45, 30) == F(18, 12)), form="zwei_wege", lp=LP, idee="additiv_oder_multiplikativ")
neu(T, "verhaeltnis", "sicherung", "fehler", L(
    "Lena löst die Verhältnisgleichung 4 : x = 6 : 18 so: Zeile 1: Außenglieder sind 4 und 18, Innenglieder sind x und 6. Zeile 2: Also 4 · x = 6 · 18. Zeile 3: Also x = 108 : 4 = 27. In welcher Zeile steckt der erste Fehler, und welchen Wert hat x richtig?",
    "Fehler in Zeile □, richtig: x = □", [2, 12], ["2", "4 * 18 / 6"], ["1 + 1", "72 / 6"],
    "Außenglieder mal Außenglieder = Innenglieder mal Innenglieder. Zeile 1 stimmt: Außenglieder 4 und 18, Innenglieder x und 6. Also gilt 4 · 18 = x · 6, das heißt 72 = 6x und x = 12 (Zeile 2 ist der Fehler: Lena kreuzt x mit 4). Probe: 4 : 12 = 1 : 3 = 6 : 18.",
    {0: [(3, "die Schlusszeile genannt, weil dort der falsche Wert 27 steht", "3"), (1, "die Zuordnung der Außenglieder in Zeile 1 für falsch gehalten", "1")], 1: [(27, "wie Lena x mit 4 gekreuzt: 6 · 18 : 4", "6 * 18 / 4"), (20, "additiv gerechnet: 6 + 18 − 4", "6 + 18 - 4"), (108, "nur 6 · 18 gerechnet und nicht geteilt", "6 * 18")]}), form="fehler_detektiv", lp=LP, idee="fehler_aussen_innen")
neu(T, "verhaeltnis", "sicherung", "darstellung", Z(
    "Für zwei Zahlen a und b gilt a : b = 7 : 12. Dann gilt (a + b) : b = □ : 12.",
    19, "7 + 12", "(7 + 12) * 12 / 12",
    "Aus a : b = 7 : 12 folgt: Auf 7 Teile von a kommen 12 Teile von b. Zusammen sind a und b dann 7 + 12 = 19 Teile, und b ist 12 Teile. Also gilt (a + b) : b = 19 : 12. Probe mit a = 14 und b = 24: (14 + 24) : 24 = 38 : 24 = 19 : 12.",
    [B("7", "den Zähler 7 unverändert gelassen, obwohl a + b statt a steht"),
     B("12 - 7", "die Differenz der Verhältniszahlen genommen"),
     B("7 + 12 + 12", "die 12 für b doppelt addiert")], einheit=""), form="bruecke", lp=LP, idee="mittelwert_summe")
neu(T, "verhaeltnis", "sicherung", "transfer", Z(
    "Zwei Quadrate haben Seitenlängen im Verhältnis 2 : 3. Das kleinere Quadrat hat den Flächeninhalt 36 cm². Wie groß ist der Flächeninhalt des größeren Quadrats?",
    81, "36 * 3 * 3 / (2 * 2)", "9 * 9",
    "Das kleinere Quadrat hat 36 cm², also die Seitenlänge 6 cm. Die Seiten verhalten sich wie 2 : 3, ein Teil ist 3 cm, die größere Seite ist 9 cm lang. Das größere Quadrat hat 9 · 9 = 81 cm². Die Flächen verhalten sich wie 4 : 9, also nicht wie die Seiten: Beide Seitenlängen werden mit demselben Faktor malgenommen, die Fläche mit dem Faktor zum Quadrat.",
    [B("36 * 3 / 2", "das Seitenverhältnis unmittelbar auf die Flächen übertragen"),
     B("36 * 3", "die Fläche nur mit der größeren Verhältniszahl 3 malgenommen"),
     B("36 * 4", "die Fläche mit dem Quadrat der kleineren Verhältniszahl malgenommen")], einheit="cm²"), lp=LP, idee="flaeche_aus_seitenverhaeltnis")
