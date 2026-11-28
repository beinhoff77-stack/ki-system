T = "terme.potenzgesetze"
LP = "M6 1 Rationale Zahlen (Potenzen mit ganzzahligen Exponenten, Hoch 0, negative Exponenten)"
REGEL[(T, "negativer_exponent")] = REGEL[(T, "fehler_finden")] = "rr.potenz"
ABG[(T, "negativer_exponent")] = "Die Übungen berechnen negative Exponenten nach Regel; hier werden Werte in einem Bereich gezählt, Exponenten gesucht und Potenzen mit verschiedenen Basen verglichen."
ABG[(T, "fehler_finden")] = "Die Übungen nennen den Fehler in einer Zeile oder das richtige Ergebnis; hier muss die erste fehlerhafte Zeile in einer Rechenkette gefunden werden, und Aussagen über Potenzen werden begründet oder widerlegt."
# ───────── negativer_exponent ─────────# ───────── negativer_exponent ─────────
# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "parameter", L(
    "Die Zahl 2ⁿ liegt zwischen 1/200 und 40 (die Grenzen gehören nicht dazu). Ergänze den kleinsten und den größten ganzen Exponenten n, für den das gilt: kleinstes n = □ und größtes n = □.",
    "kleinstes n = □ und größtes n = □", [-7, 5], ["0 - 7", "5"], ["1 - 8", "10 - 5"],
    "Die Potenzen von 2 mit negativem Exponenten sind 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128, 1/256. Der Wert 1/128 ist noch größer als 1/200, 1/256 aber schon kleiner; das kleinste n ist also −7. Nach oben ist 2⁵ = 32 kleiner als 40, 2⁶ = 64 aber größer; das größte n ist 5.",
    {0: [(-8, "den Wert noch mitgenommen, der schon unter der unteren Grenze liegt", "0 - 8"), (7, "das Minus im Exponenten vergessen", "7")],
     1: [(6, "den Wert noch mitgenommen, der schon über der oberen Grenze liegt", "6"), (-5, "die obere Grenze mit der unteren verwechselt", "0 - 5")]}), lp=LP, idee="zaehlen_im_bereich")

neu(T, "negativer_exponent", "korrektur", "einkleidung", Z(
    "Ein Blatt der Größe A0 hat die Fläche 1 m². Jede Verkleinerung um eine Stufe halbiert die Fläche, ein Blatt der Größe An hat also die Fläche 2⁻ⁿ m². Ab welcher Stufe n hat ein Blatt zum ersten Mal weniger als 1 cm² Fläche? (1 m² sind 10 000 cm².)",
    14, "13 + 1", "14",
    "Gesucht ist das kleinste n mit 2⁻ⁿ m² < 1 cm² = 1/10 000 m², also 2ⁿ > 10 000. Es ist 2¹³ = 8 192 (noch zu klein) und 2¹⁴ = 16 384 (größer als 10 000). Das kleinste n ist 14. Das Blatt A14 hat 1/16 384 m², das sind weniger als 1 cm².",
    [B("13", "die letzte Stufe genommen, bei der die Fläche noch größer als 1 cm² ist"),
     B("7", "mit einem zu kleinen Umrechnungsfaktor zwischen m² und cm² gerechnet"),
     B("15", "eine Stufe zu viel genommen")], einheit=""), form="bruecke", lp=LP, idee="papier_klein")

neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Für welche positive ganze Zahl b gilt b⁻³ = 0,008?",
    5, "125 / 25", "1000 / 8 / 25",
    "b⁻³ = 1/b³. Es ist 0,008 = 8/1 000 = 1/125. Also muss b³ = 125 sein, und wegen 5 · 5 · 5 = 125 ist b = 5. Probe: 5⁻³ = 1/125 = 0,008.",
    [B("8", "die Ziffer 8 aus 0,008 als Basis genommen"),
     B("125", "den Nenner 125 des Bruchs als Basis angegeben, ohne die dritte Wurzel zu ziehen"),
     B("2", "den Dezimalbruch als Würfel einer Dezimalzahl gelesen und nur deren Ziffer übernommen")], einheit=""), form="umkehren", lp=LP, idee="basis_gesucht")

neu(T, "negativer_exponent", "sicherung", "begruenden", W(
    "Welche Strecke ist länger: 2⁻⁵ m oder 5 mm? Welche Aussage stimmt?",
    "2⁻⁵ m ist länger, denn 2⁻⁵ m = 1/32 m, und das sind mehr als 31 mm.",
    [("5 mm ist länger, denn 2⁻⁵ ist ein Bruch mit negativem Exponenten und damit eine winzige Länge, die kleiner als ein Millimeter ist.", "einen negativen Exponenten mit einer winzigen Zahl gleichgesetzt, ohne den Wert auszurechnen"),
     ("Beide sind gleich lang, denn die Hochzahl 5 in 2⁻⁵ m sagt, dass die Länge 5 mm beträgt.", "die Hochzahl als Zahl der Millimeter gelesen"),
     ("5 mm ist länger, denn 2⁻⁵ m = 1/(2 · 5) m, und die Hochzahl macht die Länge kleiner als einen Millimeter.", "den Nenner als 2 · 5 statt 2⁵ gerechnet")],
    "2⁻⁵ = 1/2⁵ = 1/32. Also ist 2⁻⁵ m = 1/32 m = 1 000 mm : 32 = 31,25 mm. Das ist deutlich mehr als 5 mm. Ein negativer Exponent macht die Zahl nicht negativ und nicht „winzig“, sondern bedeutet einen Bruch mit Zähler 1.",
    lambda: F(1000, 32) == F("31.25") and F(1000, 32) > 5 and F(1, 2 * 5) * 1000 != 5), lp=LP, idee="laenge_vergleich")

neu(T, "negativer_exponent", "sicherung", "darstellung", L(
    "Zwischen zwei Zehnerpotenzen: Es gilt 10^□ < 3⁻⁷ < 10^□ mit zwei aufeinanderfolgenden ganzen Exponenten.",
    "10^□ < 3⁻⁷ < 10^□", [-4, -3], ["0 - 4", "0 - 3"], ["3 - 7", "4 - 7"],
    "3⁷ = 2 187, also ist 3⁻⁷ = 1/2 187. Es gilt 1 000 < 2 187 < 10 000, daher 1/10 000 < 1/2 187 < 1/1 000. In Zehnerpotenzen: 10⁻⁴ < 3⁻⁷ < 10⁻³. Die Exponenten sind −4 und −3.",
    {0: [(-3, "2 187 für dreistellig gehalten und eine Stelle zu wenig gezählt", "0 - 3"), (-7, "den Exponenten 7 aus 3⁻⁷ als Zehnerexponent übernommen", "0 - 7"), (4, "das Minus im Exponenten vergessen", "4")],
     1: [(-2, "wie bei der unteren Grenze eine Stelle zu wenig gezählt", "0 - 2"), (3, "das Minus im Exponenten vergessen", "3"), (-4, "dieselbe Zehnerpotenz wie unten angegeben, obwohl beide Grenzen verschieden sein müssen", "0 - 4")]}),
    form="bruecke", lp=LP, idee="zwischen_zehnerpotenzen")

# ───────── fehler_finden ─────────
neu(T, "fehler_finden", "test", "fehler", L(
    "Ein Kind soll 2^(3²) berechnen und rechnet: Zeile 1: 2^(3²) = (2³)². Zeile 2: (2³)² = 2⁶. Zeile 3: 2⁶ = 64. Zeile 4: Also ist 2^(3²) = 64. In welcher Zeile steckt der erste Fehler, und welchen Wert hat 2^(3²) richtig?",
    "Fehler in Zeile □, richtig: □", [1, 512], ["1", "8 * 8 * 8"], ["2 - 1", "2 * 2 ** 8"],
    "Zeile 1 ist falsch: 2^(3²) heißt 2 hoch (3²). Die Hochzahl 3² = 9 steht schon fest, es ist also 2⁹ = 512. Die Potenz (2³)² = 8² = 64 ist eine andere Zahl; dort werden die Hochzahlen multipliziert, weil die Klammer 2³ selbst die Basis ist. Die Zeilen 2 bis 4 rechnen mit (2³)² richtig weiter.",
    {0: [(2, "den richtigen Potenzschritt in Zeile 2 für den Fehler gehalten", "1 + 1"), (4, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "2 + 2")],
     1: [(64, "die Potenz (2³)² statt 2^(3²) ausgerechnet, also die Hochzahlen 3 und 2 multipliziert", "(2 ** 3) ** 2"), (32, "die Hochzahlen 3 und 2 addiert", "2 ** 5"), (256, "die Hochzahl 3² um eins zu klein berechnet", "16 * 16")]}),
    form="fehler_detektiv", lp=LP, idee="potenzturm")

neu(T, "fehler_finden", "korrektur", "einkleidung", Z(
    "Ein Kind sagt: „1 m sind 10² cm, also sind 1 m³ genau 10² cm³.“ Richtig ist: 1 m³ = 10ᵏ cm³. Wie groß ist k?",
    6, "2 * 3", "2 + 2 + 2",
    "Ein Würfel mit der Kante 1 m hat die Kante 10² cm. Sein Volumen ist (10²)³ = 10²·³ = 10⁶ cm³. Die Umrechnungszahl 10² wird dreimal mit sich selbst malgenommen, nicht nur einmal. Probe: 100 · 100 · 100 = 1 000 000.",
    [B("2", "den Umrechnungsfaktor der Länge unverändert für das Volumen übernommen"),
     B("2 + 3", "die Hochzahlen addiert statt multipliziert"),
     B("2 ** 3", "die Hochzahl 2 mit 3 potenziert statt malgenommen")], einheit=""), form="bruecke", lp=LP, idee="volumen_potenz")

neu(T, "fehler_finden", "korrektur", "darstellung", Z(
    "Ein Kind behauptet: „Man darf Basis und Hochzahl vertauschen: aᵇ = bᵃ.“ Für wie viele Paare (a | b) ganzer Zahlen mit 1 < a < b ≤ 12 stimmt das tatsächlich?",
    1, "2 - 1", "1",
    "Man probiert alle Paare: 2³ = 8 und 3² = 9, 2⁴ = 16 und 4² = 16 (gleich!), 2⁵ = 32 und 5² = 25, 3⁴ = 81 und 4³ = 64, und alle weiteren Paare liefern verschiedene Werte, weil bei größerer Basis und Hochzahl die größere Hochzahl bei der kleineren Basis stärker wächst. Es gibt genau ein Paar: (2 | 4). Die Behauptung gilt also nicht allgemein.",
    [B("2", "auch das vertauschte Paar (4 | 2) gezählt, obwohl a kleiner als b sein soll"),
     B("0", "keinen Treffer gefunden, weil nur die ersten Paare probiert wurden"),
     B("2 + 1", "Paare mit gleichem Wert verwechselt und auch die Paare mit nahezu gleichem Wert gezählt")], einheit="Paare"), lp=LP, idee="potenzen_vertauscht")

neu(T, "fehler_finden", "sicherung", "umkehr", Z(
    "Für wie viele Paare (a | b) ganzer Zahlen von −50 bis 50 gilt (a + b)² = a² + b²?",
    201, "101 + 101 - 1", "101 * 101 - 100 * 100",
    "Es ist (a + b)² = a² + 2ab + b². Die Gleichung gilt genau dann, wenn 2ab = 0 ist, also wenn a = 0 oder b = 0 ist. Für a = 0 gibt es 101 Paare (b von −50 bis 50), für b = 0 ebenfalls 101; das Paar, bei dem beide Zahlen null sind, ist doppelt gezählt: 101 + 101 − 1 = 201. Probe: Von den 101 · 101 = 10 201 Paaren haben 100 · 100 = 10 000 weder a noch b gleich null.",
    [B("101 + 101", "das Paar, bei dem beide Zahlen null sind, doppelt gezählt"),
     B("101 + 101 - 2", "das Paar, bei dem beide Zahlen null sind, gar nicht gezählt"),
     B("101", "nur den Fall betrachtet, dass die erste Zahl null ist")], einheit="Paare"), lp=LP, idee="binom_paare")

neu(T, "fehler_finden", "sicherung", "begruenden", W(
    "Für zwei positive Zahlen a und b vergleicht man (a + b)² mit a² + b². Welche Aussage stimmt immer?",
    "(a + b)² ist größer als a² + b², denn (a + b)² enthält zusätzlich das doppelte Produkt a · b.",
    [("(a + b)² ist genauso groß wie a² + b², denn man darf die Hochzahl auf jeden Summanden verteilen.", "die Hochzahl wie bei einem Produkt auf die Summanden verteilt"),
     ("(a + b)² ist kleiner als a² + b², denn beim Addieren vor dem Quadrieren werden die Zahlen kleiner.", "gedacht, das Addieren vor dem Quadrieren verkleinere die Zahl"),
     ("Das hängt von a und b ab: Mal ist die eine Seite größer, mal die andere, denn nur bei gleichen Zahlen lässt sich vergleichen.", "geglaubt, ohne Zahlenwerte lasse sich keine Aussage machen")],
    "(a + b)² = (a + b) · (a + b) = a² + 2ab + b². Bei positiven Zahlen ist 2ab > 0, also ist (a + b)² immer größer als a² + b². Zahlenprobe: a = 3, b = 4 gibt 49 gegen 25.",
    lambda: all((a + b) ** 2 > a ** 2 + b ** 2 for a in (1, 2, 3, 7) for b in (1, 4, 5, 9)) and (3 + 4) ** 2 == 49 and 3 ** 2 + 4 ** 2 == 25), lp=LP, idee="binom_groesser")

# ───────── vorrat ─────────
neu(T, "fehler_finden", "korrektur", "mehrschritt", Z(
    "Ein Kind kürzt (2⁶ − 2⁴) : 2⁴ zu 2⁶ − 1 = 63. Ein zweites Kind rechnet erst 2⁶ − 2⁴ = 48 aus und teilt dann durch 2⁴. Wie groß ist (2⁶ − 2⁴) : 2⁴ richtig?",
    3, "48 / 16", "2 ** 2 - 1",
    "Der zweite Weg ist richtig: 2⁶ − 2⁴ = 64 − 16 = 48, und 48 : 16 = 3. Das erste Kind teilt nur den zweiten Summanden durch 2⁴ und lässt den ersten stehen. Beim Teilen einer Differenz muss man beide Glieder teilen: 2⁶ : 2⁴ − 2⁴ : 2⁴ = 2² − 1 = 3.",
    [B("63", "das falsche Ergebnis des ersten Kindes übernommen"),
     B("2 ** 2", "nur 2⁶ durch 2⁴ geteilt und die Subtraktion vergessen"),
     B("64 - 16", "nur die Klammer ausgerechnet und nicht durch 2⁴ geteilt")], einheit=""), form="zwei_wege", lp=LP, idee="differenz_teilen")
