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
    "Beim Lösen von 3/(x − 2) = 1/(x − 2) + 2/(x − 2) multipliziert Jan beide Seiten mit (x − 2) und erhält 3 = 1 + 2. Er sagt: „Jetzt stehen keine Nenner mehr da, also gibt es keine Einschränkung.“ Wie viele der ganzen Zahlen von −5 bis 5 (einschließlich) sind Lösung der Ausgangsgleichung?",
    10, "11 - 1", sum(1 for x in range(-5, 6) if x != 2 and F(3, x - 2) == F(1, x - 2) + F(2, x - 2)),
    "Die Definitionsmenge bestimmt man an der Ausgangsgleichung: Der Nenner x − 2 darf nicht 0 werden, also D = ℚ \\ {2}. Nach dem Malnehmen mit (x − 2) steht 3 = 1 + 2, eine für jedes x wahre Aussage. Also ist jede Zahl aus D eine Lösung, die Zahl 2 aber nicht, weil die Brüche für x = 2 nicht definiert sind. "
    "Von den 11 ganzen Zahlen −5 bis 5 bleiben 10.",
    [B("11", "die Zahl 2 mitgezählt, obwohl für x = 2 der Nenner 0 wird"),
     B("0", "die immer wahre Aussage nach dem Malnehmen als „keine Lösung“ gedeutet"),
     B("1", "nur die verbotene Zahl 2 als Lösung genommen")], einheit="Zahlen"), lp=LP, idee="identitaet_und_D")
neu(T, "definitionsmenge", "korrektur", "darstellung", Z(
    "Für wie viele Zahlen ist die Gleichung 7/(2x − 6) + 1/(x + 3) = 4/(x² − 9) nicht definiert? (Gemeint sind alle rationalen Zahlen x.)",
    2, "1 + 1", len({F(6, 2), F(-3)} | {F(3), F(-3)}),
    "Ein Bruch ist nicht definiert, wenn sein Nenner 0 wird. Erster Nenner: 2x − 6 = 0 für x = 3. Zweiter Nenner: x + 3 = 0 für x = −3. Dritter Nenner: x² − 9 = (x − 3)(x + 3) = 0 für x = 3 oder x = −3. "
    "Der dritte Nenner liefert keine neue Zahl. Ausgeschlossen sind also nur die zwei Zahlen 3 und −3.",
    [B("1 + 1 + 2", "die Lösungen jeder Nennergleichung einzeln gezählt (1 + 1 + 2), ohne doppelte Zahlen zu streichen"),
     B("1 + 1 + 1", "für jeden der drei Nenner nur eine Zahl gezählt, obwohl x² − 9 zwei Nullstellen hat"),
     B("1", "nur die Zahl 3 betrachtet, weil sie in zwei Nennern vorkommt")], einheit="Zahlen"), lp=LP, idee="nenner_zerlegen")
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
    "Ein Drucker allein braucht x Minuten für einen Auftrag, ein zweiter braucht 5 Minuten weniger. Zusammen schaffen sie den Auftrag in 3 Minuten, das gibt die Gleichung 1/x + 1/(x − 5) = 1/3. Wie viele ganze Zahlen von −3 bis 9 (einschließlich) sind als Wert für x erlaubt?",
    11, "13 - 2", sum(1 for x in range(-3, 10) if x not in (0, 5)),
    "Der Nenner x darf nicht 0 sein, der Nenner x − 5 darf nicht 0 sein, also sind 0 und 5 ausgeschlossen. Von den 13 ganzen Zahlen −3 bis 9 bleiben 13 − 2 = 11.",
    [B("13 - 1", "nur einen der beiden Nenner beachtet: nur eine Zahl ausgeschlossen"),
     B("13", "keine Zahl ausgeschlossen"),
     B("13 - 3", "drei Zahlen ausgeschlossen, weil die 3 aus der rechten Seite mitgezählt wurde")], einheit="Zahlen"), form="bruecke", lp=LP, idee="text_zu_D")
neu(T, "definitionsmenge", "sicherung", "fehler", L(
    "Mara bestimmt die Definitionsmenge von 5/(x² − 25) = 3/(x − 5) so: Zeile 1: Aus x² − 25 = 0 folgt x = 5, also ist nur 5 verboten. Zeile 2: Aus x − 5 = 0 folgt x = 5. Zeile 3: Also ist D = ℚ \\ {5}. In welcher Zeile steckt der erste Fehler, und wie viele Zahlen sind richtig aus D ausgeschlossen?",
    "Fehler in Zeile □, ausgeschlossene Zahlen: □", [1, 2], ["1", "1 + 1"], ["3 - 2", "2"],
    "x² − 25 = (x − 5)(x + 5) ist 0 für x = 5 und für x = −5. Zeile 1 ist falsch: Es ist nicht nur 5 verboten, auch −5 macht den Nenner 0. Zeile 2 ist richtig (x − 5 = 0 gilt nur für 5). Zeile 3 übernimmt den Fehler. Richtig ist D = ℚ \\ {−5; 5}, also sind zwei Zahlen ausgeschlossen.",
    {1: [(1, "nur die 5 gezählt, wie in Zeile 3", "1"), (3, "für jeden Nenner eine Zahl gezählt: drei Nenner-Gleichungen", "1 + 1 + 1"), (4, "die Lösungen beider Nenner einzeln addiert, ohne die doppelte 5 zu streichen", "2 + 1 + 1")]}), form="fehler_detektiv", lp=LP, idee="fehler_x_quadrat")
neu(T, "definitionsmenge", "sicherung", "transfer", W(
    "Kinder teilen sich die Kosten von 36 € für ein Taxi gleichmäßig; es sind x Kinder. Kommen 3 weitere Kinder mit, zahlt jedes Kind 2 € weniger. Welche Gleichung beschreibt das, und welche Zahlen sind für x ausgeschlossen?",
    "36/x − 36/(x + 3) = 2 mit D = ℚ \\ {−3; 0}",
    [("36/x − 36/(x + 3) = 2 mit D = ℚ \\ {0}", "den zweiten Nenner x + 3 nicht beachtet; für x = −3 ist 36/(x + 3) nicht definiert"),
     ("36/x + 36/(x + 3) = 2 mit D = ℚ \\ {−3; 0}", "die beiden Kosten addiert; das Kind zahlt mit den Zusatzkindern weniger, der Unterschied ist 2 €"),
     ("36/(x − 3) − 36/x = 2 mit D = ℚ \\ {0; 3}", "die 3 weiteren Kinder abgezogen statt dazugezählt; mit 3 Kindern mehr sind es x + 3 Kinder")],
    "Mit x Kindern zahlt jedes 36/x €. Mit 3 weiteren Kindern sind es x + 3 Kinder, und jedes zahlt 36/(x + 3) €, das sind 2 € weniger: 36/x − 36/(x + 3) = 2. "
    "Die Nenner x und x + 3 dürfen nicht 0 sein, also D = ℚ \\ {−3; 0}. Probe mit x = 6: 36/6 − 36/9 = 6 − 4 = 2.",
    lambda: F(36, 6) - F(36, 9) == 2 and F(36, 6) + F(36, 9) != 2 and F(36, 3) - F(36, 6) != 2), form="bruecke", lp=LP, idee="modell_aufstellen")
# ───────── ueber_kreuz ─────────
def _kreuz_zahl():
    # (A) (x+2)/4 = 3/(x-1)  ja; (B) 1/x + 1/2 = 3/(x-1) nein; (C) 5/(x+1) = 2 ja (2 = 2/1); (D) 6/(x-2) = 4/x + 1 nein; (E) (2x)/3 = 5/(x+1) ja
    erlaubt = {"A": (1, 1), "B": (2, 1), "C": (1, 1), "D": (1, 2), "E": (1, 1)}   # Anzahl der obersten Brüche links/rechts: nur (1, 1) erlaubt
    return sum(1 for v in erlaubt.values() if v == (1, 1))


neu(T, "ueber_kreuz", "test", "pruefung", Z(
    "Bei wie vielen dieser fünf Gleichungen darf man sofort über Kreuz multiplizieren, also a/b = c/d in a · d = c · b umwandeln? (A) (x + 2)/4 = 3/(x − 1); (B) 1/x + 1/2 = 3/(x − 1); (C) 5/(x + 1) = 2; (D) 6/(x − 2) = 4/x + 1; (E) (2x)/3 = 5/(x + 1).",
    3, "1 + 1 + 1", _kreuz_zahl(),
    "Über Kreuz geht, wenn auf jeder Seite genau ein Bruch steht. (A) ja. (B) nein: links steht eine Summe zweier Brüche. (C) ja: die Zahl 2 ist der Bruch 2/1, es entsteht 5 · 1 = 2(x + 1). (D) nein: rechts steht ein Bruch plus 1. (E) ja: links steht der Bruch (2x)/3. Das sind 3 Gleichungen: A, C und E.",
    [B("1 + 1", "die Gleichung mit der ganzen Zahl 2 nicht mitgezählt, weil auf der rechten Seite kein Bruch zu stehen schien"),
     B("1 + 1 + 1 + 1", "auch eine Gleichung mit einer Summe auf einer Seite mitgezählt"),
     B("1 + 1 + 1 + 1 + 1", "bei allen fünf Gleichungen über Kreuz gerechnet, auch bei den Summen")], einheit="Gleichungen"),
    form="verfahren_waehlen", lp=LP, idee="wann_erlaubt")
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
     ("4/(x − 4) = 2/(x − 2)", "die beiden Nenner vertauscht; für x = 6 steht links das Doppelte von rechts")],
    "Man setzt x = 6 ein. 4/(6 − 2) = 1 und 2/(6 − 4) = 1: Beide Seiten sind gleich, die erste Gleichung hat die Lösung 6. Bei den anderen steht links 4/(6 − 2) = 1 gegen 2/10, 4/8 gegen 2/2 und 4/2 gegen 2/4.",
    lambda: F(4, 6 - 2) == F(2, 6 - 4) and F(4, 6 - 2) != F(2, 6 + 4) and F(4, 6 + 2) != F(2, 6 - 4) and F(4, 6 - 4) != F(2, 6 - 2)), lp=LP, idee="gleichung_zur_loesung")
neu(T, "ueber_kreuz", "korrektur", "mehrschritt", W(
    "Zwei Kinder lösen 2/(x − 1) = 3/(x + 4). Kim multipliziert über Kreuz. Jo multipliziert beide Seiten mit dem Produkt der Nenner, also mit (x − 1)(x + 4), und kürzt. Welche Aussage stimmt?",
    "Beide erhalten 2(x + 4) = 3(x − 1) und damit x = 11.",
    [("Jo erhält 2(x − 1) = 3(x + 4) und damit x = −14, Kim erhält x = 11.", "Jos Weg falsch gedeutet: Beim Malnehmen mit (x − 1)(x + 4) kürzt sich links x − 1 weg, es bleibt 2(x + 4)"),
     ("Nur Kims Weg ist erlaubt; Jos Weg führt zu keiner Lösung.", "geglaubt, das Malnehmen mit dem Produkt der Nenner sei verboten; es ist eine erlaubte Umformung, solange der Faktor nicht 0 ist"),
     ("Beide erhalten 2(x − 1) = 3(x + 4) und damit x = −14.", "die Zähler mit den eigenen Nennern malgenommen statt mit den Nennern der anderen Seite")],
    "Jo: 2/(x − 1) · (x − 1)(x + 4) = 2(x + 4) und 3/(x + 4) · (x − 1)(x + 4) = 3(x − 1). Das ist genau die Gleichung, die Kim über Kreuz erhält. Lösen: 2x + 8 = 3x − 3, also x = 11. "
    "Probe: 2/10 = 0,2 und 3/15 = 0,2. Die Zahl 11 liegt in D = ℚ \\ {−4; 1}.",
    lambda: F(2, 11 - 1) == F(3, 11 + 4) and 2 * (11 + 4) == 3 * (11 - 1) and 2 * (-14 - 1) == 3 * (-14 + 4) and F(2, -14 - 1) != F(3, -14 + 4) and 2 * (-14 + 4) != 3 * (-14 - 1)), form="zwei_wege", lp=LP, idee="zwei_wege")
neu(T, "ueber_kreuz", "sicherung", "fehler", L(
    "Ben löst 10/(x + 2) = 6/x so: Zeile 1: Über Kreuz: 10 · x = 6 · (x + 2). Zeile 2: Ausmultiplizieren: 10x = 6x + 2. Zeile 3: Also 4x = 2 und x = 0,5. In welcher Zeile steckt der erste Fehler, und welche Lösung hat die Gleichung richtig?",
    "Fehler in Zeile □, richtig: x = □", [2, 3], ["2", "12 / (10 - 6)"], ["1 + 1", "3"],
    "Zeile 1 ist richtig. In Zeile 2 ist 6 · (x + 2) = 6x + 12, nicht 6x + 2: Die 6 muss mit beiden Gliedern der Klammer malgenommen werden. Richtig: 10x = 6x + 12, 4x = 12, x = 3. Probe: 10/(3 + 2) = 2 und 6/3 = 2. Mit Bens Ergebnis x = 0,5 wäre 10/2,5 = 4, aber 6/0,5 = 12.",
    {1: [(-5, "falsch gekreuzt: 10(x + 2) = 6x gibt x = −5", "20 / (6 - 10)"), (12, "aus 4x = 12 gleich x = 12 gelesen", "12"), (2, "die Zeilennummer des Fehlers als Lösung angegeben", "1 + 1")]}), form="fehler_detektiv", lp=LP, idee="fehler_ausmultiplizieren")

def _zaehle_ohne_loesung():
    n = 0
    for k in range(-4, 5):
        # 4/(x-1) = k/(x+2): (4 - k)x = -k - 8
        a, b = 4 - k, -k - 8
        ok = (b == 0) if a == 0 else (F(b, a) not in (1, -2))
        n += 0 if ok else 1
    return n
_ZWEIT_K = _zaehle_ohne_loesung()
neu(T, "ueber_kreuz", "sicherung", "parameter", Z(
    "Für wie viele ganze Zahlen k von −4 bis 4 (einschließlich) hat die Gleichung 4/(x − 1) = k/(x + 2) mindestens eine Lösung?",
    7, "9 - 2", 9 - _zaehle_ohne_loesung(),
    "Über Kreuz: 4(x + 2) = k(x − 1), also (4 − k)x = −k − 8. Für k = 4 steht 0 · x = −12: keine Lösung. Für k = 0 folgt 4x = −8, also x = −2. Das ist aber ausgeschlossen (Nenner x + 2), eine Scheinlösung: keine Lösung. "
    "Für alle anderen k aus dem Bereich gibt es x = (−k − 8)/(4 − k), und dieses x ist weder 1 noch −2. Von den 9 Zahlen −4 bis 4 haben also 9 − 2 = 7 eine Lösung (alle außer 0 und 4).",
    [B("8", "nur k = 4 als Zahl ohne Lösung gefunden und die Scheinlösung bei k = 0 übersehen"),
     B("9", "geglaubt, dass sich für jedes k eine Lösung findet"),
     B("9 - 1 - 1 - 1", "einen weiteren Wert von k ausgeschlossen, für den es doch eine Lösung gibt")], einheit="Zahlen"), lp=LP, idee="parameter_keine_loesung")
neu(T, "ueber_kreuz", "sicherung", "einkleidung", Z(
    "In einer Gruppe sind 9 Jungen. Es kommen Mädchen dazu, danach sind genau zwei Drittel der Gruppe Mädchen. Wie viele Mädchen sind dazugekommen?",
    18, "9 * 2 / (3 - 2)", "9 / (3 / 2 - 1)",
    "Mit x neuen Mädchen sind es x + 9 Kinder. Der Anteil der Mädchen ist x/(x + 9) = 2/3. Über Kreuz: 3x = 2(x + 9), also 3x = 2x + 18 und x = 18. Probe: 18/(18 + 9) = 18/27 = 2/3. Die Mädchen gehören auch in den Nenner des Anteils.",
    [B("9 * 2 / 3", "die Mädchen im Nenner vergessen: x gleich 9 mal 2 geteilt durch 3 gesetzt"),
     B("9 / (3 - 2)", "die Klammer nicht ausmultipliziert: 3x = 2x + 9 gibt x = 9"),
     B("27 / (2 - 3)", "über Kreuz falsch gekreuzt: 2x = 3(x + 9) gibt x = −27")], einheit="Mädchen"), form="bruecke", lp=LP, idee="modell_aufstellen")
# ───────── scheinloesung ─────────
neu(T, "scheinloesung", "test", "transfer", Z(
    "Wie viele ganze Zahlen von −2 bis 5 (einschließlich) liegen in der Lösungsmenge von (x² − 6x + 9)/(x − 3) = x − 3?",
    7, "8 - 1", sum(1 for x in range(-2, 6) if x != 3 and F(x * x - 6 * x + 9, x - 3) == x - 3),
    "Der Zähler ist eine binomische Formel: x² − 6x + 9 = (x − 3)². Für x ≠ 3 gilt (x − 3)²/(x − 3) = x − 3, die Gleichung ist also für jede Zahl aus D wahr: L = ℚ \\ {3}. "
    "Von den 8 ganzen Zahlen −2, −1, 0, 1, 2, 3, 4, 5 gehört die 3 nicht dazu. Es bleiben 7 Zahlen.",
    [B("8", "die ausgeschlossene Zahl 3 mitgezählt"),
     B("0", "geglaubt, dass es wegen des verbotenen Wertes 3 keine Lösung gibt"),
     B("1", "geglaubt, dass nur die Zahl 3 als Lösung zählt")], einheit="Zahlen"), lp=LP, idee="identitaet")
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
neu(T, "scheinloesung", "korrektur", "umkehr", Z(
    "Für welche Zahl b ist x = 4 eine Scheinlösung der Gleichung (2x + b)/(x − 4) = 17/(x − 4)?",
    9, "17 - 2 * 4", "17 - 8",
    "Mal (x − 4): 2x + b = 17, also b = 17 − 2x. Der Kandidat ist eine Scheinlösung, wenn er der verbotene Wert 4 ist: b = 17 − 2 · 4 = 9. Probe: Für b = 9 gilt 2x + 9 = 17, also x = 4, und die 4 liegt nicht in D.",
    [B("17 - 4", "den Faktor 2 vor dem x übersehen: b = 17 − x gerechnet"),
     B("17 + 2 * 4", "17 + 8 gerechnet: das Vorzeichen von 2x falsch gesetzt"),
     B("17 - 2", "17 − 2 gerechnet: nur 2 statt 2 · 4 abgezogen")]), lp=LP, idee="scheinloesung_erzeugen")
neu(T, "scheinloesung", "sicherung", "fehler", L(
    "Ina löst 5/(x − 1) + 2 = 7/(x − 1) so: Zeile 1: Mal (x − 1) gibt 5 + 2 = 7. Zeile 2: Das stimmt für jede Zahl. Zeile 3: Also sind alle Zahlen Lösung. In welcher Zeile steckt der erste Fehler, und welche Zahl ist die einzige Lösung der Gleichung?",
    "Fehler in Zeile □, einzige Lösung: x = □", [1, 2], ["1", "2"], ["4 - 3", "(7 - 5) / 1"],
    "Beim Malnehmen mit (x − 1) muss jedes Glied malgenommen werden, auch die 2: 5 + 2(x − 1) = 7. Das gibt 2x + 3 = 7, also x = 2. Die 2 liegt in D = ℚ \\ {1}. Probe: 5/1 + 2 = 7 und 7/1 = 7. Zeile 1 ist der Fehler; Zeile 2 und 3 folgen daraus.",
    {1: [(1, "die verbotene Zahl 1 als Lösung genommen", "1"), (4, "aus 2x + 3 = 7 nur 7 − 3 gerechnet und nicht durch 2 geteilt", "7 - 3")]}), form="fehler_detektiv", lp=LP, idee="fehler_nicht_alle_glieder")
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
    "Aus x²/(x − 2) = 4/(x − 2) folgt nach dem Malnehmen mit (x − 2) die Gleichung x² = 4. Der Kandidat, der nicht zur Definitionsmenge gehört, ist x = □. Die Lösung der Gleichung ist x = □.",
    "verbotener Kandidat: □, Lösung: □", [2, -2], ["2", "-2"], ["4 / 2", "0 - 2"],
    "Aus x² = 4 folgen die Kandidaten x = 2 und x = −2. Der Nenner x − 2 ist für x = 2 gleich 0, also ist 2 verboten (Scheinlösung). Die Zahl −2 gehört zu D = ℚ \\ {2}: Probe 4/(−4) = −1 und 4/(−4) = −1. Die Lösung ist x = −2.",
    {0: [(4, "das Quadrat 4 selbst als Kandidat genommen", "2 * 2"), (0, "gar keinen Kandidaten als verboten erkannt", "0")],
     1: [(-4, "das Quadrat mit Minuszeichen als Lösung genommen", "-2 * 2")]}), form="bruecke", lp=LP, idee="zwei_kandidaten")
# ───────── verhaeltnis ─────────
neu(T, "verhaeltnis", "test", "parameter", Z(
    "Zwei Zahlen verhalten sich wie 5 : 7. Addiert man zu jeder der beiden Zahlen 6, verhalten sich die neuen Zahlen wie 3 : 4. Welche der beiden ursprünglichen Zahlen ist die kleinere?",
    30, "5 * 6", next(a for a in range(1, 400) for b in [F(7 * a, 5)] if b.denominator == 1 and F(a + 6, b + 6) == F(3, 4)),
    "Die Zahlen sind 5k und 7k. Nach dem Addieren gilt (5k + 6) : (7k + 6) = 3 : 4. Außenglieder mal Innenglieder: 4(5k + 6) = 3(7k + 6), also 20k + 24 = 21k + 18 und k = 6. "
    "Die Zahlen sind 30 und 42. Probe: 36 : 48 = 3 : 4. Die kleinere Zahl ist 30.",
    [B("7 * 6", "die größere der beiden Zahlen (42) angegeben"),
     B("5 * 6 + 6", "die kleinere neue Zahl 36 statt der ursprünglichen angegeben"),
     B("6", "nur den Faktor k = 6 angegeben")]), form="umkehren", lp=LP, idee="verhaeltnis_nach_addition")
neu(T, "verhaeltnis", "korrektur", "darstellung", W(
    "In einer Farbmischung verhalten sich die roten zu den blauen Teilen wie 3 : 5. Welchen Anteil der ganzen Mischung macht das Rot aus?",
    "3/8",
    [("3/5", "das Verhältnis Rot : Blau als Anteil an der Mischung gelesen; die 5 Teile Blau gehören nicht zum Rot"),
     ("5/8", "den Anteil des Blau genommen statt des Rot"),
     ("3/2", "Rot durch die Differenz 5 − 3 geteilt")],
    "Das Verhältnis 3 : 5 vergleicht die Teile Rot und Blau. Die ganze Mischung hat 3 + 5 = 8 Teile, davon sind 3 Teile rot. Der Anteil Rot ist also 3/8 (37,5 %). Das Blau macht 5/8 aus.",
    lambda: F(3, 3 + 5) == F(3, 8) and F(3, 5) != F(3, 8) and F(5, 8) != F(3, 8)), form="bruecke", lp=LP, idee="anteil_aus_verhaeltnis")
neu(T, "verhaeltnis", "korrektur", "umkehr", Z(
    "Zwei Zahlen verhalten sich wie 4 : 7. Die größere Zahl ist um 33 größer als die kleinere. Wie groß ist die größere Zahl?",
    77, "33 / (7 - 4) * 7", "11 * 7",
    "Die Zahlen sind 4 Teile und 7 Teile. Der Unterschied sind 7 − 4 = 3 Teile, und diese 3 Teile sind 33. Ein Teil ist 33 : 3 = 11. Die größere Zahl sind 7 Teile: 7 · 11 = 77. Probe: 77 − 44 = 33 und 44 : 77 = 4 : 7.",
    [B("33 / (7 - 4) * 4", "die kleinere Zahl (44) angegeben statt der größeren"),
     B("33 / 4 * 7", "die 33 durch 4 statt durch den Unterschied 3 der Verhältniszahlen geteilt"),
     B("33 / (7 + 4) * 7", "die 33 durch die Summe der Verhältniszahlen geteilt statt durch ihren Unterschied")]), lp=LP, idee="unterschied_als_teile")
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
    {1: [(27, "wie Lena x mit 4 gekreuzt: 6 · 18 : 4", "6 * 18 / 4"), (20, "additiv gerechnet: 6 + 18 − 4", "6 + 18 - 4"), (108, "nur 6 · 18 gerechnet und nicht geteilt", "6 * 18")]}), form="fehler_detektiv", lp=LP, idee="fehler_aussen_innen")
neu(T, "verhaeltnis", "sicherung", "umkehr", Z(
    "Ein Preisgeld wird im Verhältnis 3 : 5 : 7 an drei Teams verteilt. Das Team mit dem kleinsten Anteil bekommt 90 €. Wie viel Euro beträgt das ganze Preisgeld?",
    450, "90 / 3 * (3 + 5 + 7)", "90 * 5",
    "Das kleinste Team bekommt 3 Teile, das sind 90 €. Ein Teil ist 90 € : 3 = 30 €. Alle Teile zusammen sind 3 + 5 + 7 = 15 Teile, also 15 · 30 € = 450 €. Probe: 150 € + 210 € + 90 € = 450 €.",
    [B("90 * (3 + 5 + 7)", "die 90 € als den Wert eines Teils genommen"),
     B("90 / 3 * 7", "nur den größten Anteil berechnet statt des ganzen Preisgelds"),
     B("90 / 3 * 5", "nur den mittleren Anteil berechnet statt des ganzen Preisgelds")], einheit="€"), form="umkehren", lp=LP, idee="rueckwaerts_aufteilen")
neu(T, "verhaeltnis", "sicherung", "transfer", Z(
    "Für drei Größen a, b und c gilt a : b = 2 : 3 und b : c = 4 : 5. Es ist a = 24. Wie groß ist c?",
    45, "24 / 8 * 15", "24 * 3 / 2 * 5 / 4",
    "Die beiden Verhältnisse haben verschiedene Zahlen für b (3 und 4). Man erweitert auf ein gemeinsames b, nämlich 12: a : b = 8 : 12 und b : c = 12 : 15. Also gilt a : b : c = 8 : 12 : 15. Mit a = 24 ist ein Teil 24 : 8 = 3, und c hat 15 Teile: 15 · 3 = 45. Probe: b = 36, dann 24 : 36 = 2 : 3 und 36 : 45 = 4 : 5.",
    [B("24 * 5 / 2", "die beiden Verhältnisse nicht abgestimmt: die Zahlen 2 und 5 direkt verglichen"),
     B("24 * 3 / 2", "nur b ausgerechnet und dort aufgehört"),
     B("24 * 5 / 4", "a mit dem zweiten Verhältnis verglichen, also die Zahlen 4 und 5 genommen")]), lp=LP, idee="gemeinsames_glied")
