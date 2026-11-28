T = "terme.umformen"
# ───────── zusammenfassen ─────────
neu(T, "zusammenfassen", "lueckenweg", L(
    "Du fasst 9x + 3y − 2x + 5y zusammen. Das Ergebnis hat die Form ① · x + ② · y. Für x = 2 und y = 1 hat der Term den Wert ③.",
    "① = □; ② = □; ③ = □", [7, 8, 22], ["9 - 2", "3 + 5", "{1} * 2 + {2} * 1"], ["7", "8", "9 * 2 + 3 * 1 - 2 * 2 + 5 * 1"],
    "Fasse nur gleichartige Glieder zusammen: die mit x und die mit y. Setze die Zahlen für x und y erst am Ende ein.",
    "x-Glieder: 9x − 2x = 7x. y-Glieder: 3y + 5y = 8y. Der Term ist 7x + 8y. Für x = 2 und y = 1: 7 · 2 + 8 · 1 = 22. Probe mit dem Ausgangsterm: 18 + 3 − 4 + 5 = 22.",
    {0: [(11, None, "die Glieder 9x und 2x addiert, obwohl vor 2x ein Minus steht", "9 + 2")], 1: [(-2, None, "die y-Glieder subtrahiert statt addiert", "3 - 5")], 2: [(23, None, "für x und y die Werte vertauscht eingesetzt", "{1} * 1 + {2} * 2")]}), g="direkt", regel="rr.tauschen")
neu(T, "zusammenfassen", "anwenden", Z(
    "Kim kauft 3 Erwachsenen- und 2 Kinderkarten für einen Freizeitpark, Alex kauft 5 Erwachsenen- und 4 Kinderkarten. Eine Erwachsenenkarte kostet a €, eine Kinderkarte b €. Zusammen zahlen sie 3a + 2b + 5a + 4b. Wie viel Euro sind das für a = 12 und b = 7?",
    138, "8 * 12 + 6 * 7", "3 * 12 + 2 * 7 + 5 * 12 + 4 * 7", "Fasse erst zusammen: Wie viele Erwachsenenkarten sind es insgesamt, wie viele Kinderkarten?",
    "Erwachsenenkarten: 3a + 5a = 8a. Kinderkarten: 2b + 4b = 6b. Zusammen 8a + 6b. Für a = 12 und b = 7: 8 · 12 + 6 · 7 = 96 + 42 = 138 €.",
    [B("14 * 12 * 7", "alle Glieder zu einem Glied mit ab zusammengefasst"), B("14 * 12", "alle Glieder zu 14a zusammengefasst, b nicht mehr beachtet"), B("8 * 12 + 4 * 7", "das Glied 2b nicht mitgezählt")], einheit="€"), g="einkleidung", regel="rr.tauschen")
neu(T, "zusammenfassen", "fehler_detektiv", FD(
    "Kim soll 6x + 5y − 2x + y zusammenfassen und schreibt auf:",
    [("Gleichartig sind 6x und −2x sowie 5y und y.", True, True),
     ("6x − 2x = 4x.", True, True),
     ("5y + y = 5y, denn ein einzelnes y hat keine Zahl davor.", False, True),
     ("Das Ergebnis ist 4x + 5y.", gl("6*x+5*y-2*x+y", "4*x+5*y"), True)],
    "Welche Zahl steht vor einem einzelnen y? Prüfe es mit y = 1: y ist dann 1 · y.",
    "Ein einzelnes y bedeutet 1y. Also gilt 5y + y = 5y + 1y = 6y. Das richtige Ergebnis ist 4x + 6y. Der Fehler steckt in Zeile 3. Zeile 4 übernimmt ihn.",
    frage="In welcher Zeile passiert der erste Fehler?"), g="fehler", regel="rr.tauschen")
# ───────── produkte ─────────
neu(T, "produkte", "anwenden", Z(
    "Eine Reisebox ist ein Quader mit den Kanten 2a, 3a und a (in Zentimetern). Das Volumen ist das Produkt der drei Kanten. Wie groß ist das Volumen in Kubikzentimetern für a = 5?",
    750, "2 * 5 * 3 * 5 * 5", "6 * 5 ** 3", "Vereinfache das Produkt zuerst: Zahlen mal Zahlen, gleiche Buchstaben zu einer Potenz.",
    "2a · 3a · a = (2 · 3) · (a · a · a) = 6a³. Für a = 5: 6 · 5³ = 6 · 125 = 750 cm³.",
    [B("6 * 5 ** 2", "aus a · a · a nur a² gemacht"), B("(6 * 5) ** 3", "die Zahl 6 mit in die Potenz genommen"), B("2 * 5 + 3 * 5 + 5", "die Kanten addiert statt malgenommen")], einheit="cm³"), g="einkleidung", regel="rr.tauschen",
    zweifel="Produkte tauschen und zusammenfassen: rr.tauschen; die Lernkarte nennt rr.vorzeichen, hier kommen aber keine negativen Zahlen vor")
neu(T, "produkte", "umkehren", W(
    "Welches Produkt ergibt −12a²b?",
    "3a · (−4ab)", [("(−3a) · (−4ab)", "Minus mal Minus gibt Plus, das Ergebnis wäre 12a²b"), ("(−3a) · 4a", "kein b im Ergebnis, a² ohne b"), ("3a · 4b", "das Ergebnis wäre 12ab")],
    "Zerlege −12a²b in Faktoren: Welche Vorzeichen, Zahlen und Buchstaben müssen links zusammenkommen? Prüfe jedes Angebot durch Ausrechnen.",
    "3a · (−4ab) = −12a²b: Plus mal Minus gibt Minus, 3 · 4 = 12 und a · a · b = a²b. Die anderen Produkte ergeben (−3a) · (−4ab) = 12a²b, (−3a) · 4a = −12a² und 3a · 4b = 12ab.",
    lambda: gl("3*a*(-4*a*b)", "-12*a*a*b") and not gl("(-3*a)*(-4*a*b)", "-12*a*a*b") and not gl("(-3*a)*(4*a)", "-12*a*a*b") and not gl("3*a*(4*b)", "-12*a*a*b")), g="umkehr", regel="rr.vorzeichen")
neu(T, "produkte", "umkehren", Z(
    "Eine natürliche Zahl a erfüllt 3a · 4a = 300. Wie groß ist a?",
    5, "5", next(a for a in range(1, 100) if 3 * a * 4 * a == 300), "Vereinfache zuerst das Produkt auf der linken Seite. Welche natürliche Zahl mal sich selbst ergibt das Ergebnis?",
    "3a · 4a = 12a². Aus 12a² = 300 folgt a² = 25. Nur die natürliche Zahl 5 hat das Quadrat 25. Probe: 3 · 5 · 4 · 5 = 15 · 20 = 300.",
    [B("25", "a² = 25 gelesen und 25 als Ergebnis genommen"), B("25 / 2", "den Wert 25 halbiert statt die Zahl zu suchen, die mit sich selbst malgenommen 25 ergibt")]), g="rueckwaerts", regel="rr.tauschen",
    zweifel="Produkt vereinfachen (tauschen) und zurückrechnen; keine Regel des Katalogs für das Umkehren von a² in dieser Klassenstufe")
# ───────── minusklammer ─────────
neu(T, "minusklammer", "lueckenweg", L(
    "Du löst die Klammer in 11x − (4x − 6) + 3 auf und fasst zusammen. Das Ergebnis hat die Form ① · x + ②. Für x = 2 hat der Term den Wert ③.",
    "① = □; ② = □; ③ = □", [7, 9, 23], ["11 - 4", "6 + 3", "{1} * 2 + {2}"], ["7", "9", "11 * 2 - (4 * 2 - 6) + 3"],
    "Ein Minus vor der Klammer ändert die Vorzeichen aller Glieder in der Klammer. Achte besonders auf das zweite Glied.",
    "−(4x − 6) = −4x + 6. Dann: 11x − 4x + 6 + 3 = 7x + 9. Für x = 2: 7 · 2 + 9 = 23. Probe mit dem Ausgangsterm: 22 − (8 − 6) + 3 = 22 − 2 + 3 = 23.",
    {0: [(15, None, "die x-Glieder addiert", "11 + 4")], 1: [(-3, "fb.minusklammer.nur_erstes_zeichen", "nur das erste Vorzeichen in der Klammer gewechselt, die 6 blieb negativ", "-6 + 3")], 2: [(25, None, "x = 2 beim falschen Glied eingesetzt: 7 + 9 · 2 statt 7 · 2 + 9", "{1} + {2} * 2")]}), g="direkt", regel="rr.minusklammer")
neu(T, "minusklammer", "anwenden", Z(
    "Kim hat 400 € Reisegeld. Für eine Zugfahrt zahlt sie (3x + 15) €, dabei ist x die Zahl der Fahrtstunden, 15 € sind eine feste Gebühr. Der Rest ist 400 − (3x + 15). Wie viel Euro bleiben bei 20 Stunden Fahrt übrig?",
    325, "400 - (3 * 20 + 15)", "385 - 3 * 20", "Löse zuerst die Klammer auf. Das Minus davor wirkt auf beide Glieder in der Klammer.",
    "400 − (3x + 15) = 400 − 3x − 15 = 385 − 3x. Für x = 20: 385 − 60 = 325 €. Probe: Die Fahrt kostet 3 · 20 + 15 = 75 €, und 400 − 75 = 325 €.",
    [B("400 - 3 * 20 + 15", "das Minus nur auf das erste Glied der Klammer bezogen", "fb.minusklammer.nur_erstes_zeichen"), B("400 - 3 * 20", "die feste Gebühr vergessen"), B("400 + 3 * 20 + 15", "das Minus vor der Klammer überhaupt nicht beachtet")], einheit="€"), g="einkleidung", regel="rr.minusklammer")
neu(T, "minusklammer", "fehler_detektiv", FD(
    "Alex löst die Klammer in 9a − (2a + 7b − 3) auf und schreibt auf:",
    [("Das Minus vor der Klammer ändert alle Vorzeichen in der Klammer.", True, True),
     ("9a − (2a + 7b − 3) = 9a − 2a − 7b − 3.", gl("9*a-(2*a+7*b-3)", "9*a-2*a-7*b-3"), True),
     ("Zusammengefasst ist das 7a − 7b − 3.", True, gl("9*a-2*a-7*b-3", "7*a-7*b-3"))],
    "Wie lautet die Klammer nach dem Auflösen, wenn bei jedem Glied das Vorzeichen wechselt? Was passiert mit −3?",
    "Aus −(−3) wird +3. Richtig ist 9a − 2a − 7b + 3 = 7a − 7b + 3. Der Fehler steckt in Zeile 2: Das letzte Vorzeichen wurde nicht gewechselt. Zeile 3 rechnet mit diesem Fehler richtig weiter."), g="fehler", regel="rr.minusklammer")
# ───────── ausmultiplizieren ─────────
neu(T, "ausmultiplizieren", "anwenden", Z(
    "Eine Gruppe von 6 Personen bucht ein Hostel. Pro Person kostet das Paket (45 + 12n) €, dabei ist n die Zahl der Zusatznächte. Der Gesamtpreis ist 6 · (45 + 12n). Wie viel Euro zahlt die Gruppe bei 3 Zusatznächten?",
    486, "6 * (45 + 12 * 3)", "6 * 45 + 6 * 12 * 3", "Der Faktor 6 gilt für jedes Glied in der Klammer. Du kannst auch erst die Klammer ausrechnen und dann mit 6 malnehmen.",
    "Ausmultiplizieren: 6 · (45 + 12n) = 270 + 72n. Für n = 3: 270 + 216 = 486 €. Probe: Pro Person 45 + 36 = 81 €, für 6 Personen 486 €.",
    [B("6 * 45 + 12 * 3", "den Faktor 6 nur mit dem ersten Glied in der Klammer malgenommen", "fb.ausmultiplizieren.nur_erster_summand"), B("45 + 12 * 3", "den Faktor 6 für die Gruppe vergessen"), B("6 + 45 + 12 * 3", "die Zahl der Personen dazugezählt statt malgenommen")], einheit="€"), g="einkleidung", regel="rr.ausmultiplizieren")
neu(T, "ausmultiplizieren", "zwei_wege", Z(
    "Berechne 8 · 197 auf zwei Wegen. Weg A: Schriftlich malnehmen. Weg B: 197 als 200 − 3 schreiben und 8 · (200 − 3) ausmultiplizieren. Welches Ergebnis ist richtig?",
    1576, "8 * 197", "8 * 200 - 8 * 3", "Bei Weg B: Der Faktor 8 trifft beide Glieder in der Klammer, auch das zweite mit seinem Minus.",
    "Weg B: 8 · (200 − 3) = 8 · 200 − 8 · 3 = 1 600 − 24 = 1 576. Weg A schriftlich: 8 · 7 = 56, schreibe 6 und merke 5; 8 · 9 = 72 und 5 dazu sind 77, schreibe 7 und merke 7; 8 · 1 = 8 und 7 dazu sind 15. Das Ergebnis ist 1 576. Beide Wege stimmen überein.",
    [B("8 * 200 - 3", "den Faktor 8 nur mit der 200 malgenommen", "fb.ausmultiplizieren.nur_erster_summand"), B("8 * 203", "aus dem Minus in der Klammer ein Plus gemacht"), B("200 - 3 * 8", "den Faktor 8 nur mit dem zweiten Glied in der Klammer malgenommen")]), g="mehrschritt", regel="rr.ausmultiplizieren")
neu(T, "ausmultiplizieren", "umkehren", Z(
    "Welche Zahl gehört in das Kästchen, damit 5 · (2x + □) = 10x + 35 für jede Zahl x stimmt?",
    7, "35 // 5", 7, "Der Faktor 5 muss mit jedem Glied der Klammer malgenommen den passenden Summanden rechts ergeben.",
    "Ausmultipliziert: 5 · 2x = 10x und 5 · □ = 35. Also ist □ = 35 : 5 = 7. Probe: 5 · (2x + 7) = 10x + 35.",
    [B("35", "den Summanden rechts einfach abgeschrieben"), B("35 - 5", "den Faktor 5 abgezogen statt durch ihn geteilt"), B("35 * 5", "mit dem Faktor 5 malgenommen statt geteilt")]), g="rueckwaerts", regel="rr.ausmultiplizieren")
# ───────── aequivalenz ─────────
neu(T, "aequivalenz", "anwenden", W(
    "Kim berechnet den Preis einer Taxifahrt mit 2(x + 5) − x, Alex mit x + 10. Welche Aussage über die beiden Terme ist mathematisch richtig begründet?",
    "Sie sind äquivalent: 2(x + 5) − x = 2x + 10 − x = x + 10.",
    [("Sie sind äquivalent, denn für x = 0 ergeben beide Terme 10.", "ein einziges Beispiel beweist keine Äquivalenz"), ("Sie sind nicht äquivalent: 2(x + 5) − x = 2x + 5 − x = x + 5.", "die Klammer wurde nur mit dem ersten Glied malgenommen")],
    "Äquivalent heißt: für jede Zahl gleich. Forme den ersten Term um und vergleiche mit dem zweiten.",
    "2(x + 5) − x = 2x + 10 − x = x + 10. Das ist der Term von Alex, die beiden Terme sind also für jede Zahl x gleich. Ein Beispiel allein (x = 0) würde das nicht beweisen.",
    lambda: gl("2*(x+5)-x", "x+10") and not gl("2*(x+5)-x", "x+5")), g="einkleidung", regel="id.algebra.term")
neu(T, "aequivalenz", "umkehren", W(
    "Kim behauptet: „3x + 6 und 9x sind äquivalent.“ Welche Probe zeigt, dass das nicht stimmt?",
    "Für x = 0 ergibt der erste Term 6 und der zweite 0. Die Werte sind verschieden.",
    [("Für x = 1 ergeben beide Terme 9. Also sind sie nicht äquivalent.", "gleiche Werte bei einer Zahl widerlegen die Äquivalenz nicht"), ("Für x = 1 ergeben beide Terme 9. Also sind sie äquivalent.", "aus einem Beispiel mit gleichen Werten auf Äquivalenz geschlossen"), ("3x + 6 hat zwei Glieder und 9x nur eines. Also sind sie nicht äquivalent.", "die Anzahl der Glieder entscheidet nicht über Äquivalenz")],
    "Für „nicht äquivalent“ reicht eine einzige Zahl, bei der die beiden Terme verschiedene Werte haben. Probiere kleine Zahlen.",
    "Für x = 0: 3 · 0 + 6 = 6 und 9 · 0 = 0. Die Werte sind verschieden, die Terme sind nicht äquivalent. Bei x = 1 sind beide Werte 9; das reicht nicht, um etwas zu zeigen.",
    lambda: 3 * 0 + 6 != 9 * 0 and 3 * 1 + 6 == 9 * 1 and not gl("3*x+6", "9*x")), g="pruefung", regel="id.algebra.term")
neu(T, "aequivalenz", "umkehren", Z(
    "Für welchen Wert von k sind die Terme 13(x + 4) und 13x + k äquivalent?",
    52, "13 * 4", 52, "Multipliziere die Klammer aus. Die Terme müssen für jede Zahl x denselben Wert haben.",
    "13(x + 4) = 13x + 52. Damit 13x + k für jedes x denselben Wert hat, muss k = 52 sein. Probe: Für x = 1 sind beide Werte 65.",
    [B("4", "nur die Zahl in der Klammer übernommen"), B("13 + 4", "die Zahlen addiert statt malgenommen"), B("13 * 4 * 13", "mit dem Faktor 13 doppelt malgenommen")]), g="rueckwaerts", regel="rr.ausmultiplizieren")
