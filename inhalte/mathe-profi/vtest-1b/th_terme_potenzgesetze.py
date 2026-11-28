T = "terme.potenzgesetze"
LP = "M6 1 Rationale Zahlen (Potenzen mit ganzzahligen Exponenten, Hoch 0, negative Exponenten)"
REGEL[(T, "negativer_exponent")] = REGEL[(T, "fehler_finden")] = "rr.potenz"
ABG[(T, "negativer_exponent")] = "Die Übungen berechnen negative Exponenten nach Regel; hier werden Werte in einem Bereich gezählt, Exponenten gesucht und Potenzen mit verschiedenen Basen verglichen."
ABG[(T, "fehler_finden")] = "Die Übungen nennen den Fehler in einer Zeile oder das richtige Ergebnis; hier muss die erste fehlerhafte Zeile in einer Rechenkette gefunden werden, und Aussagen über Potenzen werden begründet oder widerlegt."
# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "parameter", Z(
    "Für wie viele ganze Zahlen n von −4 bis 4 (einschließlich) liegt der Wert von 2ⁿ zwischen 1/10 und 3? (Die Grenzen 1/10 und 3 gehören nicht dazu.)",
    5, "5", sum(1 for n in range(-4, 5) if F(1, 10) < F(2) ** n < 3),
    "Die Werte von 2ⁿ sind für n = −4 bis 4: 1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8, 16. Zwischen 1/10 = 0,1 und 3 liegen 1/8, 1/4, 1/2, 1 und 2, das sind 5 Werte. 1/16 = 0,0625 ist kleiner als 0,1, und 4 ist größer als 3.",
    [B("2", "nur die Exponenten 0 und 1 beachtet; negative Exponenten wurden als negative Werte abgetan"),
     B("4", "den Wert vergessen, der knapp über der unteren Grenze liegt"),
     B("6", "auch den Wert mitgezählt, der noch unter der unteren Grenze liegt")], einheit="Zahlen"), lp=LP, idee="zaehlen_im_bereich")
neu(T, "negativer_exponent", "korrektur", "umkehr", L(
    "Ergänze zwei wahre Gleichungen: 7⁻² = 1/□ und 2^□ = 1/32.",
    "7⁻² = 1/□ und 2^□ = 1/32", [49, -5], ["7 ** 2", "0 - 5"], ["7 * 7", "5 - 10"],
    "7⁻² = 1/7² = 1/49, der Nenner ist 49. Für 1/32 = 1/2⁵ = 2⁻⁵ ist der Exponent −5. Probe: 2⁻⁵ = 1/2⁵ = 1/32.",
    {0: [(14, "Basis mal Exponent gerechnet: 7 · 2", "7 * 2")], 1: [(5, "das Minus im Exponenten vergessen", "5"), (-32, "den Nenner 32 mit Minus als Exponenten genommen", "0 - 32")]}), lp=LP, idee="einsetzen_luecken")
neu(T, "negativer_exponent", "korrektur", "darstellung", Z(
    "Wie viele Zehntausendstel sind 5⁻⁴?",
    16, "10000 / 625", "16",
    "5⁻⁴ = 1/5⁴ = 1/625. Ein Zehntausendstel ist 1/10 000. Es gilt 1/625 = 16/10 000 (beide Seiten mit 16 erweitert: 625 · 16 = 10 000), also sind es 16 Zehntausendstel. Probe: 16 : 10 000 = 0,0016 und 1 : 625 = 0,0016.",
    [B("5 ** 4", "5⁴ = 625 ausgerechnet und das Minus im Exponenten übersehen"),
     B("5 * 4", "Basis mal Exponent gerechnet"),
     B("10000 / 125", "den Nenner 125 statt 625 genommen: 10 000 durch 125")], einheit="Zehntausendstel"), form="bruecke", lp=LP, idee="umrechnen_bruch")
neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Wie viele der Zahlen 3⁻⁴, 4⁻³, 10⁻² und 1⁻⁶ sind kleiner als 1/50?",
    3, "3", sum(1 for v in (F(1, 81), F(1, 64), F(1, 100), F(1)) if v < F(1, 50)),
    "3⁻⁴ = 1/81, 4⁻³ = 1/64 und 10⁻² = 1/100 sind kleiner als 1/50, denn bei gleichem Zähler ist der Bruch mit dem größeren Nenner kleiner. 1⁻⁶ = 1/1⁶ = 1 ist größer. Es sind also 3 Zahlen.",
    [B("3 + 1", "auch die Zahl 1⁻⁶ mitgezählt, weil negative Hochzahlen immer kleine Zahlen ergeben"),
     B("3 - 1", "die mittlere der drei kleinen Zahlen für größer als die Grenze gehalten"),
     B("3 - 2", "nur 10⁻² gezählt, weil nur dort eine Zehnerpotenz vorkommt")], einheit="Zahlen"), lp=LP, idee="kleiner_als_grenze")
neu(T, "negativer_exponent", "sicherung", "begruenden", W(
    "Ein Kind sagt: „2⁻⁴ ist größer als 2⁻³, denn 4 ist größer als 3.“ Welche Aussage über das Kind stimmt?",
    "Das Kind irrt, denn 2⁻⁴ = 1/16 ist kleiner als 2⁻³ = 1/8.",
    [("Das Kind hat recht, denn die größere Hochzahl ergibt die größere Zahl.", "Hochzahl und Wert gleichgesetzt, obwohl das Minus das Verhältnis umdreht"),
     ("Die beiden Zahlen sind gleich groß, denn bei einer negativen Hochzahl zählt nur die Basis.", "den Einfluss der Hochzahl auf die Größe der Zahl übersehen"),
     ("Das Kind hat recht, denn 2⁻⁴ = 1/16 ist größer als 2⁻³ = 1/8.", "die beiden Brüche falsch verglichen, weil 16 größer ist als 8")],
    "2⁻³ = 1/2³ = 1/8 und 2⁻⁴ = 1/2⁴ = 1/16. Je größer der Betrag der negativen Hochzahl, desto kleiner ist der Wert: Bei jedem Schritt nach rechts im Muster wird durch 2 geteilt. 1/16 ist die Hälfte von 1/8.",
    lambda: F(1, 16) < F(1, 8) and F(2) ** -4 < F(2) ** -3 and F(2) ** -4 == F(1, 16)), lp=LP, idee="vergleich_begruenden")
neu(T, "negativer_exponent", "sicherung", "darstellung", W(
    "Welche der folgenden Potenzen hat den Wert 0,125?",
    "2⁻³",
    [("2⁻⁸", "die Hochzahl 8 aus dem Nenner 8 abgelesen, statt die Potenz 2³ = 8 zu erkennen"),
     ("8⁻²", "Basis und Hochzahl aus 0,125 = 1/8 falsch zugeordnet: 8⁻² = 1/64"),
     ("3⁻²", "eine Potenz mit dem Wert 1/9 verwechselt")],
    "0,125 = 125/1000 = 1/8, und 8 = 2³. Also ist 0,125 = 1/2³ = 2⁻³. Die anderen: 2⁻⁸ = 1/256, 8⁻² = 1/64, 3⁻² = 1/9.",
    lambda: F("0.125") == F(2) ** -3 and F(2) ** -8 != F("0.125") and F(8) ** -2 != F("0.125") and F(3) ** -2 != F("0.125")), lp=LP, idee="dezimal_zu_potenz")
neu(T, "negativer_exponent", "sicherung", "transfer", Z(
    "Wie viele Stücke der Größe 10⁻⁴ ergeben zusammen die Größe 10⁻¹?",
    1000, "10000 / 10", "1000",
    "10⁻¹ = 1/10 und 10⁻⁴ = 1/10 000. Man fragt, wie oft 1/10 000 in 1/10 passt: 1/10 sind 1 000/10 000, also passen 1 000 Stücke. Probe: 1 000 · 1/10 000 = 1/10.",
    [B("4 - 1", "die Hochzahlen voneinander abgezogen und die Differenz als Zahl der Stücke genommen"),
     B("10000 / 10 / 10", "einmal zu oft durch 10 geteilt"),
     B("10000", "den Nenner 10 000 als Zahl der Stücke genommen")], einheit="Stücke"), lp=LP, idee="stuecke_passen")
# ───────── fehler_finden ─────────
neu(T, "fehler_finden", "test", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 2⁻² + 2⁻² = 2⁻⁴. Zeile 2: 2⁻⁴ = 1/2⁴. Zeile 3: 1/2⁴ = 1/16. Zeile 4: Also ist 2⁻² + 2⁻² = 1/16. In welcher Zeile steckt der erste Fehler? Wie heißt die Summe richtig als Bruch mit dem Zähler 1?",
    "Fehler in Zeile □, richtig: 2⁻² + 2⁻² = 1/□", [1, 2], ["1", "2"], ["4 - 3", "1 + 1"],
    "Zeile 1 ist falsch: Beim Addieren werden die Hochzahlen nicht addiert. 2⁻² = 1/4, also ist 2⁻² + 2⁻² = 1/4 + 1/4 = 2/4 = 1/2. Die Zeilen 2 bis 4 rechnen mit 2⁻⁴ richtig weiter. Probe: 1/16 ist viel zu klein, die Summe zweier Viertel ist ein Halb.",
    {0: [(2, "den Schritt in Zeile 2 für den Fehler gehalten", "1 + 1"), (4, "die Schlusszeile genannt, weil dort der falsche Wert steht", "2 + 2")],
     1: [(4, "nur eine der beiden Potenzen berechnet und die Summe vergessen", "4"), (16, "wie in Zeile 3 Hochzahlen addiert und 2⁴ berechnet", "2 * 2 * 2 * 2"), (8, "2⁻² + 2⁻² als 2⁻³ gelesen und den Nenner 2³ genommen", "2 * 2 * 2")]}),
    form="fehler_detektiv", lp=LP, idee="exponenten_addiert")
neu(T, "fehler_finden", "korrektur", "darstellung", W(
    "Ein Kind behauptet: „10⁻² = 0,2, denn man setzt die Hochzahl 2 hinter das Komma.“ Welche Aussage über die Zahl 10⁻² ist richtig?",
    "10⁻² = 0,01, denn 10⁻² = 1/10² = 1/100.",
    [("10⁻² = 0,2, denn die Hochzahl 2 kommt an die erste Stelle hinter dem Komma.", "die Hochzahl als Ziffer hinter dem Komma gelesen"),
     ("10⁻² = −100, denn ein negativer Exponent macht die Zahl negativ.", "negativen Exponenten als negative Zahl gedeutet"),
     ("10⁻² = 0,001, denn man schreibt zwei Nullen hinter das Komma und dann die 1.", "die Nullen nach dem Komma gezählt statt den Stellenwert 1/100 zu nutzen")],
    "10⁻² = 1/10² = 1/100 = 0,01: Die 1 steht an der zweiten Stelle hinter dem Komma, vor ihr steht eine Null. Das Kind hat die Hochzahl als Ziffer gelesen.",
    lambda: F(10) ** -2 == F("0.01") and F("0.01") != F("0.2") and F("0.01") != F("0.001")), lp=LP, idee="dezimal_stellen")
neu(T, "fehler_finden", "korrektur", "umkehr", W(
    "Ein Kind behauptet: „Wenn der Exponent negativ ist, ist die Potenz immer negativ.“ Welches Beispiel zeigt, dass die Behauptung nicht stimmt?",
    "2⁻¹ = 1/2 ist positiv, obwohl der Exponent −1 negativ ist.",
    [("2³ = 8 ist positiv, obwohl die Behauptung etwas anderes sagt.", "ein Beispiel mit positivem Exponenten gewählt, das die Behauptung nicht berührt"),
     ("2⁰ = 1 ist positiv, obwohl der Exponent nicht positiv ist.", "den Exponenten 0 als negativ angesehen; er ist weder positiv noch negativ"),
     ("2⁻¹ = −2 ist negativ, das passt zur Behauptung und widerlegt sie nicht.", "den negativen Exponenten als Vorzeichen des Werts gerechnet")],
    "Ein Gegenbeispiel muss einen negativen Exponenten haben und einen positiven Wert. 2⁻¹ = 1/2 ist positiv und hat den Exponenten −1. 2³ hat keinen negativen Exponenten, 2⁰ auch nicht, und 2⁻¹ = −2 ist falsch gerechnet.",
    lambda: F(2) ** -1 == F(1, 2) and F(2) ** -1 > 0 and F(2) ** -1 != -2), lp=LP, idee="gegenbeispiel")
neu(T, "fehler_finden", "korrektur", "mehrschritt", Z(
    "Anna rechnet (3 + 4)² = 3² + 4². Ben rechnet (3 + 4)² = 7 · 7. Um wie viel ist das Ergebnis von Anna falsch?",
    24, "49 - 25", "(3 + 4) ** 2 - (3 ** 2 + 4 ** 2)",
    "Bens Weg ist richtig: (3 + 4)² = 7² = 49. Annas Weg quadriert die beiden Summanden einzeln und addiert: 3² + 4² = 9 + 16 = 25. Das Quadrat einer Summe ist nicht die Summe der Quadrate. Der Unterschied ist 49 − 25 = 24.",
    [B("49 + 25", "beide Ergebnisse addiert statt voneinander abgezogen"),
     B("25", "das falsche Ergebnis von Anna als Unterschied angegeben"),
     B("3 * 4", "den fehlenden Anteil 3 · 4 nur einmal statt zweimal berechnet")], einheit=""), form="zwei_wege", lp=LP, idee="potenz_von_summe")
neu(T, "fehler_finden", "sicherung", "fehler", W(
    "Ein Kind rechnet: Zeile 1: 4⁻² = 1/4². Zeile 2: 1/4² = 1/(4 · 2) = 1/8. Zeile 3: 1/8 = 0,125. Zeile 4: Also ist 4⁻² = 0,125. In welcher Zeile steckt der erste Fehler?",
    "In Zeile 2, weil 4² = 4 · 4 = 16 ist und nicht 4 · 2.",
    [("In Zeile 1, weil ein negativer Exponent nicht den Kehrwert bildet.", "geglaubt, der negative Exponent bilde nicht den Kehrwert; 4⁻² = 1/4² stimmt"),
     ("In Zeile 3, weil 1/8 gleich 0,12 ist.", "1/8 falsch in eine Dezimalzahl verwandelt; 1/8 = 0,125 stimmt"),
     ("In Zeile 4, weil ein negativer Exponent immer eine negative Zahl ergibt.", "negative Hochzahl als negative Zahl gedeutet")],
    "Zeile 1 ist richtig: 4⁻² = 1/4². In Zeile 2 wird 4² als 4 · 2 gerechnet, richtig ist 4² = 4 · 4 = 16. Zeile 3 rechnet 1/8 = 0,125 richtig, Zeile 4 übernimmt den Fehler. Richtig: 4⁻² = 1/16 = 0,0625.",
    lambda: F(4) ** -2 == F(1, 16) and 4 ** 2 == 16 and 4 * 2 == 8 and F(1, 8) == F("0.125") and F(1, 8) != F("0.12"), pos=1), form="fehler_detektiv", lp=LP, idee="basis_mal_hochzahl")
neu(T, "fehler_finden", "sicherung", "begruenden", W(
    "Ein Kind behauptet: „5⁰ = 0, denn bei 5⁰ ist keine Fünf mehr da.“ Welche Aussage über die Behauptung ist richtig?",
    "Das Kind irrt, denn im Muster 125, 25, 5 teilt man jedes Mal durch 5, und dann folgt 5 : 5 = 1.",
    [("Das Kind hat recht, denn jede Zahl mit der Hochzahl 0 ist gleich 0.", "die Hochzahl 0 mit dem Wert 0 gleichgesetzt"),
     ("Das Kind irrt, denn 5⁰ = 5, weil bei der Hochzahl 0 die Basis stehen bleibt.", "den Exponenten 0 als „nichts ändern“ gelesen und die Basis behalten"),
     ("Das Kind irrt, denn 5⁰ ist gar keine Zahl, weil man nicht null Mal malnehmen kann.", "die Hochzahl 0 für unmöglich gehalten statt als Fortsetzung des Musters verstanden")],
    "Das Muster 125, 25, 5 teilt bei jedem Schritt nach rechts durch 5. Der nächste Wert ist 5 : 5 = 1, und die Hochzahl ist dann 0. Also ist 5⁰ = 1 und nicht 0.",
    lambda: 5 ** 3 // 5 == 25 and 25 // 5 == 5 and 5 // 5 == 1 and 5 ** 0 == 1 and 5 ** 0 != 0 and 5 ** 0 != 5), lp=LP, idee="hoch_null_begruenden")
neu(T, "fehler_finden", "sicherung", "umkehr", L(
    "Ein Kind bestimmt a in 5^a = 0,04 so: Zeile 1: 0,04 = 4/100. Zeile 2: 4/100 = 1/25. Zeile 3: Also 5^a = 1/25 = 5² und damit a = 2. In welcher Zeile steckt der erste Fehler, und welchen Wert hat a richtig?",
    "Fehler in Zeile □, richtig: a = □", [3, -2], ["3", "-2"], ["4 - 1", "0 - 2"],
    "Zeile 1 und 2 stimmen: 0,04 = 4/100 = 1/25. In Zeile 3 steht 1/25 = 5², aber 5² = 25. Richtig ist 1/25 = 1/5² = 5⁻², also a = −2. Probe: 5⁻² = 1/25 = 0,04.",
    {0: [(2, "Zeile 2 für falsch gehalten, obwohl das Kürzen stimmt", "1 + 1"), (1, "Zeile 1 für falsch gehalten, obwohl die Umwandlung in einen Bruch stimmt", "1")],
     1: [(2, "das Minus vergessen, wie in Zeile 3", "2"), (25, "den Nenner 25 als Hochzahl genommen", "25"), (4, "die Ziffer 4 aus 0,04 als Hochzahl genommen", "4")]}),
    form="fehler_detektiv", lp=LP, idee="vorzeichen_vergessen")
