T = "terme.potenzgesetze"
LP = "M6 1 Rationale Zahlen (Potenzen mit ganzzahligen Exponenten, Hoch 0, negative Exponenten)"
ABG[(T, "negativer_exponent")] = "Die Übungen berechnen negative Exponenten nach Regel; hier wird das Muster (jedes Mal halbieren) als Grund genutzt, Werte umgekehrt gesucht und der Wert eines Exponenten verglichen."
ABG[(T, "fehler_finden")] = "Die Übungen nennen den Fehler in einer Zeile oder das richtige Ergebnis; hier muss die erste fehlerhafte Zeile in einer Rechenkette gefunden und mit Begründung berichtigt werden."
# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "begruenden", W(
    "Ein Kind setzt die Reihe 2³ = 8, 2² = 4, 2¹ = 2, 2⁰ = 1 nach rechts fort. Welche Aussage über die nächsten Werte 2⁻¹ und 2⁻² ist richtig?",
    "2⁻¹ = 1/2 und 2⁻² = 1/4, denn bei jedem Schritt nach rechts wird der Wert halbiert.",
    [("2⁻¹ = −2 und 2⁻² = −4, denn ein negativer Exponent macht die Zahl negativ.", "das Minus im Exponenten auf den Wert übertragen; es führt nur im Muster weiter nach rechts, der Wert bleibt positiv"),
     ("2⁻¹ = 0 und 2⁻² = −1, denn bei jedem Schritt wird 1 abgezogen.", "das Muster mit Minus 1 statt durch 2 fortgesetzt: 1 − 1 = 0"),
     ("2⁻¹ = 1/2 und 2⁻² = 1/3, denn die Nenner werden bei jedem Schritt um 1 größer.", "den Nenner additiv fortgesetzt (2, 3) statt zu verdoppeln (2, 4)")],
    "Von 2³ bis 2⁰ wird der Wert bei jedem Schritt nach rechts halbiert: 8, 4, 2, 1. Dieses Muster gilt weiter: 1 : 2 = 1/2 = 2⁻¹ und 1/2 : 2 = 1/4 = 2⁻². "
    "Das Minus im Exponenten macht die Zahl nicht negativ, sondern klein: 2⁻² = 1/2² = 1/4.",
    lambda: F(2) ** -1 == F(1, 2) and F(2) ** -2 == F(1, 4) and F(2) ** -1 != -2 and F(2) ** -1 != 0 and F(2) ** -2 != F(1, 3)), lp=LP)
neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Eine positive Zahl x erfüllt x⁻² = 1/36. Wie heißt x?",
    6, "6", "36 / 6",
    "x⁻² = 1/x² = 1/36, also x² = 36. Die positive Zahl mit dem Quadrat 36 ist x = 6. Probe: 6⁻² = 1/6² = 1/36.",
    [B("36 / 2", "den Nenner 36 durch den Exponenten 2 geteilt, statt die Zahl zu suchen, deren Quadrat 36 ist"),
     B("36", "den Nenner 36 selbst als x gelesen"),
     B("6 * 2", "die Zahl 6 mit dem Exponenten 2 malgenommen")]), form="umkehren", lp=LP)
neu(T, "negativer_exponent", "korrektur", "darstellung", Z(
    "Wie viele Zehntausendstel sind 5⁻⁴?",
    16, "10000 / 625", "16",
    "5⁻⁴ = 1/5⁴ = 1/625. Ein Zehntausendstel ist 1/10 000. Es gilt 1/625 = 16/10 000 (beide Seiten mit 16 erweitert: 625 · 16 = 10 000), also sind es 16 Zehntausendstel. Probe: 16 : 10 000 = 0,0016 und 1 : 625 = 0,0016.",
    [B("5 ** 4", "5⁴ = 625 ausgerechnet und das Minus im Exponenten übersehen"),
     B("5 * 4", "Basis mal Exponent gerechnet"),
     B("10000 / 125", "den Nenner 125 statt 625 genommen: 10 000 durch 125")], einheit="Zehntausendstel"), form="bruecke", lp=LP)
neu(T, "negativer_exponent", "korrektur", "umkehr", L(
    "Ergänze zwei wahre Gleichungen: 7⁻² = 1/□ und 2^□ = 1/32.",
    "7⁻² = 1/□ und 2^□ = 1/32", [49, -5], ["7 ** 2", "0 - 5"], ["7 * 7", "5 - 10"],
    "7⁻² = 1/7² = 1/49, der Nenner ist 49. Für 1/32 = 1/2⁵ = 2⁻⁵ ist der Exponent −5. Probe: 2⁻⁵ = 1/2⁵ = 1/32.",
    {0: [(14, "Basis mal Exponent gerechnet: 7 · 2", "7 * 2")], 1: [(5, "das Minus im Exponenten vergessen", "5"), (-32, "den Nenner 32 mit Minus als Exponenten genommen", "0 - 32")]}), lp=LP)
neu(T, "negativer_exponent", "sicherung", "transfer", Z(
    "Eine Pflanze verdoppelt jeden Tag ihre Fläche. Heute (Tag 0) hat sie 1 m² = 10 000 cm². Wie viele cm² Fläche hatte sie vor 3 Tagen?",
    1250, "10000 / 2 ** 3", "10000 / 8",
    "Vor einem Tag war die Fläche halb so groß, das entspricht dem Exponenten −1 beim Verdoppeln. Vor 3 Tagen ist die Fläche 10 000 · 2⁻³ = 10 000 · 1/8 = 1 250 cm². Probe: 1 250 · 2 · 2 · 2 = 10 000.",
    [B("10000 * 2 ** 3", "dreimal verdoppelt statt halbiert: 10 000 mal 8"),
     B("10000 / 2 ** 2", "nur 2 Halbierungen statt 3 gerechnet"),
     B("10000 / 2 ** 4", "4 Halbierungen statt 3 gerechnet")], einheit="cm²"), form="anwenden", lp=LP)
neu(T, "negativer_exponent", "sicherung", "darstellung", W(
    "Welche Reihenfolge ordnet die Werte 2⁻³, 2⁰, 2⁻¹ und 2⁻² von klein nach groß?",
    "2⁻³ < 2⁻² < 2⁻¹ < 2⁰",
    [("2⁰ < 2⁻¹ < 2⁻² < 2⁻³", "wie bei positiven Exponenten gedacht: größerer Betrag des Exponenten gibt größeren Wert"),
     ("2⁰ < 2⁻³ < 2⁻² < 2⁻¹", "2⁰ als 0 gelesen und deshalb als kleinsten Wert eingeordnet"),
     ("2⁻¹ < 2⁻² < 2⁻³ < 2⁰", "die Werte 1/2, 1/4, 1/8 in falscher Richtung geordnet und 2⁰ = 1 richtig als größten genommen")],
    "2⁻³ = 1/8, 2⁻² = 1/4, 2⁻¹ = 1/2 und 2⁰ = 1. Von klein nach groß: 1/8 < 1/4 < 1/2 < 1. Bei Nennern wächst der Bruch, wenn der Nenner kleiner wird.",
    lambda: F(2) ** -3 < F(2) ** -2 < F(2) ** -1 < F(2) ** 0 and not (F(2) ** 0 < F(2) ** -1)), form="bruecke", lp=LP)
neu(T, "negativer_exponent", "sicherung", "parameter", Z(
    "In 6⁻¹ wird der Exponent um 2 kleiner: Es entsteht 6⁻³. Durch welche Zahl muss man den Wert von 6⁻¹ teilen, um den Wert von 6⁻³ zu erhalten?",
    36, "6 ** 2", "(1 / 6) / (1 / 216)",
    "6⁻¹ = 1/6 und 6⁻³ = 1/216. Es gilt 1/6 : 36 = 1/216, denn jeder Schritt im Exponenten um 1 nach links teilt durch 6, und zwei Schritte teilen durch 6 · 6 = 36.",
    [B("6 * 2", "Basis mal Änderung des Exponenten gerechnet"),
     B("6 ** 3", "den ganzen neuen Exponenten 3 als Anzahl der Schritte genommen"),
     B("6 + 2", "Basis plus Änderung gerechnet")]), lp=LP)
# ───────── fehler_finden ─────────
neu(T, "fehler_finden", "test", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 3⁻² = 3 · (−2). Zeile 2: 3 · (−2) = −6. Zeile 3: Also ist 3⁻² = −6. In welcher Zeile steckt der erste Fehler? Wie heißt 3⁻² richtig als Bruch?",
    "Fehler in Zeile □, richtig: 3⁻² = 1/□", [1, 9], ["1", "3 ** 2"], ["2 - 1", "9"],
    "Zeile 1 ist falsch: 3⁻² heißt nicht „Basis mal Exponent“. Es gilt 3⁻² = 1/3² = 1/9. Zeile 2 rechnet mit dem falschen Ansatz richtig weiter, Zeile 3 folgt daraus. Probe: 1/9 ist positiv und kleiner als 1, wie es bei einem negativen Exponenten sein muss.",
    {0: [(3, "die letzte Zeile genannt, weil das Ergebnis falsch aussieht", "3")], 1: [(6, "Basis mal Exponent als Nenner genommen: 3 · 2", "3 * 2"), (-9, "dem Nenner das Minus aus dem Exponenten gegeben: −3²", "0 - 3 ** 2"), (3, "nur die Basis 3 als Nenner genommen", "3")]}), form="fehler_detektiv", lp=LP)
neu(T, "fehler_finden", "korrektur", "darstellung", W(
    "Ein Kind rechnet: Zeile 1: (−3)² = (−3) · (−3). Zeile 2: (−3) · (−3) = −9. Zeile 3: −3² = −9. Zeile 4: Also sind (−3)² und −3² gleich. In welcher Zeile steckt der erste Fehler?",
    "In Zeile 2, weil minus mal minus plus ergibt: (−3) · (−3) = 9.",
    [("In Zeile 1, weil man bei (−3)² nur 3 mal 2 rechnen darf, denn die Klammer ändert nichts.", "Potenz als Mal gedeutet (3 · 2) und den Aufbau mit zwei gleichen Faktoren nicht erkannt"),
     ("In Zeile 3, weil −3² gleich 9 sein muss, denn die Klammer ist unwichtig.", "die Klammer für unwichtig gehalten; −3² = −(3 · 3) = −9 ist richtig, nur (−3)² = 9"),
     ("In Zeile 4, weil 9 und −9 verschieden sind; die Zeilen 1 bis 3 stimmen.", "den ersten Fehler beim Schluss gesucht; Zeile 2 ist schon falsch, danach ist alles Folgefehler")],
    "Zeile 1 ist richtig: Das Quadrat von (−3) sind zwei Faktoren (−3). Zeile 2 ist falsch: Minus mal minus ist plus, also (−3) · (−3) = 9. Zeile 3 ist richtig: −3² = −(3 · 3) = −9, die Klammer fehlt. "
    "Deshalb sind (−3)² = 9 und −3² = −9 verschieden; Zeile 4 ist nur eine Folge des Fehlers in Zeile 2.",
    lambda: (-3) * (-3) == 9 and -3 ** 2 == -9 and (-3) ** 2 != -3 ** 2, pos=1), form="fehler_detektiv", lp=LP)
neu(T, "fehler_finden", "korrektur", "mehrschritt", L(
    "Ein Kind rechnet: Zeile 1: 5⁰ = 0. Zeile 2: Also ist 5⁰ + 5⁰ = 0. Zeile 3: Und 5⁰ · 7 = 0. In welcher Zeile steckt der erste Fehler? Wie viel ist 5⁰ · 7 richtig?",
    "Fehler in Zeile □, richtig: 5⁰ · 7 = □", [1, 7], ["1", "7"], ["2 - 1", "1 * 7"],
    "Hoch 0 ergibt 1, nicht 0: 5⁰ = 1 (im Muster 25, 5, 1 wird jedes Mal durch 5 geteilt). Zeile 1 ist der Fehler; Zeile 2 und 3 folgen daraus. Richtig: 5⁰ · 7 = 1 · 7 = 7.",
    {0: [(3, "die letzte Zeile genannt, weil dort das Ergebnis 0 für 5⁰ · 7 steht", "3")], 1: [(0, "das falsche Ergebnis 5⁰ = 0 übernommen: 0 · 7", "0 * 7"), (35, "die Basis 5 statt 5⁰ = 1 genommen: 5 · 7", "5 * 7"), (12, "Basis plus 7 gerechnet: 5 + 7", "5 + 7")]}), form="fehler_detektiv", lp=LP)
neu(T, "fehler_finden", "korrektur", "einkleidung", Z(
    "In einem Datenblatt steht: Dicke der Folie 10⁻³ m. Ein Kind sagt: „Das sind −1000 m.“ Wie viele Nanometer ist die Folie dick? (1 Nanometer = 10⁻⁹ m)",
    1000000, "10 ** 9 / 10 ** 3", "1000000000 / 1000",
    "10⁻³ m = 1/1000 m ist positiv und klein, nicht −1000 m. Ein Nanometer ist 1/1 000 000 000 m. Die Folie ist (1/1000) : (1/1 000 000 000) = 1 000 000 000 : 1000 = 1 000 000 Nanometer dick.",
    [B("10 ** 3", "10³ statt 10⁻³ gerechnet und das Minus übersehen"),
     B("9 - 3", "die Exponenten 9 und 3 abgezogen und das Ergebnis 6 als Zahl genommen"),
     B("10 ** 9", "den Umrechnungsfaktor 10⁹ als Ergebnis genommen")], einheit="Nanometer"), lp=LP)
neu(T, "fehler_finden", "sicherung", "fehler", W(
    "Ein Kind rechnet: Zeile 1: 4⁻² = 1/(4 · 2). Zeile 2: 1/(4 · 2) = 1/8. Zeile 3: Also 4⁻² + 4⁻² = 2/8. Zeile 4: 2/8 = 1/4. In welcher Zeile steckt der erste Fehler?",
    "In Zeile 1, weil 4⁻² = 1/4² = 1/16 ist, nicht 1/(4 · 2).",
    [("In Zeile 2, weil 4 · 2 = 6 ist und nicht 8.", "4 · 2 falsch gerechnet; 4 · 2 = 8 stimmt"),
     ("In Zeile 3, weil man zwei gleiche Brüche nicht addieren darf.", "gedacht, gleiche Brüche lassen sich nicht addieren; 1/8 + 1/8 = 2/8 ist richtig gerechnet"),
     ("In Zeile 4, weil 2/8 = 1/8 gilt.", "2/8 falsch gekürzt; 2/8 = 1/4 stimmt")],
    "Zeile 1 ist falsch: 4⁻² = 1/4² = 1/16, im Nenner steht 4 mal 4, nicht 4 mal 2. Zeile 2 bis 4 sind mit dem falschen Ansatz richtig weitergerechnet: 1/(4 · 2) = 1/8, 1/8 + 1/8 = 2/8 = 1/4. "
    "Richtig wäre 4⁻² + 4⁻² = 1/16 + 1/16 = 1/8.",
    lambda: F(4) ** -2 == F(1, 16) and F(4) ** -2 != F(1, 8) and 4 * 2 == 8 and F(1, 8) + F(1, 8) == F(2, 8) and F(2, 8) == F(1, 4) and F(2, 8) != F(1, 8), pos=0), form="fehler_detektiv", lp=LP)
neu(T, "fehler_finden", "sicherung", "begruenden", W(
    "Ein Kind soll begründen, warum 5⁰ = 1 gilt. Welche Begründung ist richtig?",
    "Im Muster 5³ = 125, 5² = 25, 5¹ = 5 wird bei jedem Schritt nach rechts durch 5 geteilt; 5 : 5 = 1, also ist 5⁰ = 1.",
    [("5⁰ = 0, denn 0 mal die Basis 5 ist 0.", "den Exponenten 0 als Faktor gelesen: 0 · 5 = 0, obwohl der Exponent die Anzahl der Faktoren angibt"),
     ("5⁰ = 5, denn mit dem Exponenten 0 bleibt die Basis unverändert.", "Exponent 0 als „nichts tun“ gelesen und die Basis 5 behalten"),
     ("5⁰ = −1, denn der Exponent 0 dreht das Vorzeichen um.", "ein Vorzeichenwechsel aus dem Exponenten erfunden; −1 kommt im Muster nicht vor")],
    "Das Muster 125, 25, 5 teilt bei jedem Schritt nach rechts durch 5. Der nächste Wert ist 5 : 5 = 1, und der Exponent ist dann 0. Das passt zur Regel, dass jede Basis ungleich 0 mit Exponent 0 den Wert 1 hat.",
    lambda: 5 ** 3 // 5 == 25 and 25 // 5 == 5 and 5 // 5 == 1 and 5 ** 0 == 1 and 5 ** 0 != 0 and 5 ** 0 != 5), lp=LP)
neu(T, "fehler_finden", "sicherung", "umkehr", Z(
    "Ein Kind soll a in 5ᵃ = 1/25 bestimmen und schreibt a = 2. Welche Zahl ist richtig?",
    -2, "0 - 2", "2 - 4",
    "1/25 = 1/5² = 5⁻². Also ist a = −2. Das Kind hat das Minus vergessen: 5² ist 25, nicht 1/25. Probe: 5⁻² = 1/5² = 1/25.",
    [B("2", "das Minus im Exponenten vergessen"),
     B("25", "den Nenner 25 selbst als Exponenten genommen"),
     B("0 - 25", "den Nenner 25 mit Minus als Exponenten genommen")]), lp=LP)
