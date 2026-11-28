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
    "Der Wert der Potenz (2/3)ⁿ ist 9/4. Welche ganze Zahl muss n sein?",
    -2, "0 - 2", "2 - 4",
    "(2/3)ⁿ = 9/4 verlangt einen Wert größer als 1, also ein negatives n. Ein negativer Exponent kehrt die Basis um: (2/3)⁻² = (3/2)² = 9/4. Also ist n = −2. Probe: (2/3)² = 4/9, und der Kehrwert davon ist 9/4.",
    [B("2", "das Minus im Exponenten vergessen und ohne Kehrwert gerechnet"),
     B("4", "den Nenner 4 als Exponenten genommen"),
     B("0 - 4", "den Nenner 4 mit Minus als Exponenten genommen")]), lp=LP, idee="kehrwert_basis")
neu(T, "negativer_exponent", "sicherung", "begruenden", W(
    "Ein Kind setzt die Reihe 3³ = 27, 3² = 9, 3¹ = 3, 3⁰ = 1 nach rechts fort. Welche Aussage über die nächsten Werte 3⁻¹ und 3⁻² ist richtig?",
    "3⁻¹ = 1/3 und 3⁻² = 1/9, denn es wird jedes Mal durch 3 geteilt.",
    [("3⁻¹ = −3 und 3⁻² = −9, denn ein negativer Exponent macht die Zahl negativ.", "das Minus im Exponenten auf den Wert übertragen; es führt nur im Muster weiter nach rechts, der Wert bleibt positiv"),
     ("3⁻¹ = 0 und 3⁻² = −1, denn bei jedem Schritt wird 1 abgezogen.", "das Muster mit Minus 1 statt durch 3 fortgesetzt: 1 − 1 = 0"),
     ("3⁻¹ = 1/3 und 3⁻² = 1/6, denn die Nenner werden bei jedem Schritt um 3 größer.", "den Nenner additiv fortgesetzt (3, 6) statt zu verdreifachen (3, 9)")],
    "Von 3³ bis 3⁰ wird der Wert bei jedem Schritt nach rechts durch 3 geteilt: 27, 9, 3, 1. Dieses Muster gilt weiter: 1 : 3 = 1/3 = 3⁻¹ und 1/3 : 3 = 1/9 = 3⁻². Das Minus im Exponenten macht die Zahl nicht negativ, sondern klein.",
    lambda: F(3) ** -1 == F(1, 3) and F(3) ** -2 == F(1, 9) and F(3) ** -2 != F(1, 6) and F(3) ** -1 != -3), lp=LP, idee="muster_fortsetzen")
neu(T, "negativer_exponent", "sicherung", "darstellung", W(
    "Welche Reihenfolge ordnet die Werte 2⁻³, 3⁻², 10⁻¹ und 4⁻¹ von klein nach groß?",
    "10⁻¹ < 3⁻² < 2⁻³ < 4⁻¹",
    [("4⁻¹ < 2⁻³ < 3⁻² < 10⁻¹", "die Reihenfolge umgekehrt: erst die größte Potenz, dann die kleinere"),
     ("2⁻³ < 3⁻² < 4⁻¹ < 10⁻¹", "nach dem Betrag des Exponenten geordnet: je kleiner der Exponent, desto größer der Wert"),
     ("3⁻² < 2⁻³ < 10⁻¹ < 4⁻¹", "die ersten beiden Werte falsch verglichen und 10⁻¹ in die Mitte gesetzt")],
    "2⁻³ = 1/8 = 0,125; 3⁻² = 1/9 ≈ 0,111; 10⁻¹ = 1/10 = 0,1; 4⁻¹ = 1/4 = 0,25. Von klein nach groß: 0,1 < 0,111 < 0,125 < 0,25, also 10⁻¹ < 3⁻² < 2⁻³ < 4⁻¹. Bei Stammbrüchen ist der Wert umso kleiner, je größer der Nenner ist.",
    lambda: F(1, 10) < F(1, 9) < F(1, 8) < F(1, 4) and F(3) ** -2 == F(1, 9) and F(10) ** -1 == F(1, 10)), lp=LP, idee="ordnen_zwei_basen")
neu(T, "negativer_exponent", "sicherung", "transfer", Z(
    "Eine Pflanze verdoppelt jeden Tag ihre Fläche. Am Tag n hat sie 10 000 · 2ⁿ cm² Fläche, heute ist n = 0. An welchem Tag n hatte die Pflanze nur 1 250 cm²?",
    -3, "0 - 3", "0 - (10000 // 1250 - 5)",
    "10 000 · 2ⁿ = 1 250 gibt 2ⁿ = 1 250 : 10 000 = 1/8. Es gilt 1/8 = 2⁻³, also ist n = −3. Die Pflanze hatte die kleine Fläche vor 3 Tagen. Probe: 10 000 · 2⁻³ = 10 000 : 8 = 1 250.",
    [B("3", "das Minus im Exponenten vergessen: n = 3 hieße in 3 Tagen"),
     B("8", "den Faktor 8 statt des Exponenten genommen"),
     B("0 - 8", "den Faktor 8 mit Minus als Exponenten genommen")]), lp=LP, idee="exponent_gesucht")
# ───────── fehler_finden ─────────
neu(T, "fehler_finden", "test", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 2⁻³ = 1/2³. Zeile 2: 1/2³ = 1/8. Zeile 3: 1/8 + 1/8 = 2/16. Zeile 4: 2/16 = 1/8, also ist 2⁻³ + 2⁻³ = 1/8. In welcher Zeile steckt der erste Fehler? Wie heißt 2⁻³ + 2⁻³ richtig als Bruch?",
    "Fehler in Zeile □, richtig: 2⁻³ + 2⁻³ = 1/□", [3, 4], ["3", "8 / 2"], ["4 - 1", "4"],
    "Die Zeilen 1 und 2 stimmen: 2⁻³ = 1/2³ = 1/8. In Zeile 3 werden bei der Addition gleichnamiger Brüche die Nenner addiert; richtig bleibt der Nenner stehen und die Zähler werden addiert: 1/8 + 1/8 = 2/8. Das ist 1/4. Zeile 4 rechnet mit dem falschen Wert richtig weiter (2/16 = 1/8). Probe: 2 · 2⁻³ = 2 · 1/8 = 1/4.",
    {1: [(8, "den Nenner 8 stehen gelassen, wie das Ergebnis in Zeile 4", "8"), (16, "wie in Zeile 3 die Nenner addiert: 8 + 8", "8 + 8"), (2, "die Anzahl der Summanden als Nenner genommen", "2")]}), form="fehler_detektiv", lp=LP, idee="brueche_addieren")
neu(T, "fehler_finden", "korrektur", "darstellung", W(
    "Ein Kind behauptet: „(−3)² und −3² sind dasselbe, weil ja beide Male die 3 zweimal vorkommt.“ Welche Aussage über die beiden Werte ist richtig?",
    "(−3)² = 9 und −3² = −9; sie sind verschieden, denn bei (−3)² gehört das Minus mit zur Potenz.",
    [("(−3)² = −9 und −3² = −9; sie sind gleich, denn minus mal minus bleibt minus, das Vorzeichen ändert sich nie.", "minus mal minus als minus gerechnet und (−3) · (−3) = −9 behauptet"),
     ("(−3)² = 9 und −3² = 9; sie sind gleich, denn das Quadrat macht jede Zahl positiv, auch mit dem Minus davor.", "das Quadrat auch auf das Minus vor der 3 bezogen, obwohl ohne Klammer nur die 3 zum Quadrat genommen wird"),
     ("(−3)² = −9 und −3² = 9; sie sind verschieden, denn die Klammer dreht das Vorzeichen des Ergebnisses um.", "die Rollen vertauscht: Mit Klammer ist das Ergebnis positiv, ohne Klammer negativ")],
    "(−3)² = (−3) · (−3) = 9, denn minus mal minus ist plus. Bei −3² gehört der Exponent nur zur 3: −3² = −(3 · 3) = −9. Ohne Klammer wird zuerst potenziert, dann das Minus angewendet. Darum sind 9 und −9 verschieden.",
    lambda: (-3) * (-3) == 9 and -3 ** 2 == -9 and (-3) ** 2 != -3 ** 2), lp=LP, idee="vorzeichen_klammer")
neu(T, "fehler_finden", "korrektur", "umkehr", W(
    "Ein Kind behauptet: „Wenn der Exponent negativ ist, ist die Potenz immer negativ.“ Welches Beispiel zeigt, dass die Behauptung nicht stimmt?",
    "2⁻¹ = 1/2 ist positiv, obwohl der Exponent −1 negativ ist.",
    [("2³ = 8 ist positiv, obwohl die Behauptung etwas anderes sagt.", "ein Beispiel mit positivem Exponenten genommen; die Behauptung handelt nur von negativen Exponenten"),
     ("(−2)⁻¹ = −1/2 ist negativ, obwohl der Exponent negativ ist.", "ein Beispiel genommen, das die Behauptung bestätigt, nicht widerlegt"),
     ("2⁰ = 1 ist positiv, obwohl der Exponent nicht positiv ist.", "den Exponenten 0 für negativ gehalten; 0 ist weder positiv noch negativ")],
    "Ein Gegenbeispiel muss einen negativen Exponenten haben und trotzdem eine positive Potenz liefern. 2⁻¹ = 1/2 erfüllt das. Die negative Zahl (−2)⁻¹ = −1/2 bestätigt die Behauptung nur für eine negative Basis; 2³ und 2⁰ haben keinen negativen Exponenten.",
    lambda: F(2) ** -1 > 0 and F(-2) ** -1 < 0 and 2 ** 3 > 0 and 2 ** 0 > 0), lp=LP, idee="gegenbeispiel")
neu(T, "fehler_finden", "korrektur", "mehrschritt", Z(
    "Anna rechnet (2 + 3)² = 2² + 3² = 4 + 9 = 13. Ben rechnet (2 + 3)² = 5 · 5 = 25. Um wie viel unterscheiden sich die beiden Ergebnisse?",
    12, "5 * 5 - (2 ** 2 + 3 ** 2)", "25 - 13",
    "Das Quadrat einer Summe ist nicht die Summe der Quadrate: (2 + 3)² heißt 5² = 25. Bens Weg ist richtig. Anna hat den Exponenten auf jeden Summanden verteilt. Der Unterschied ist 25 − 13 = 12 (das ist 2 · 2 · 3, der „fehlende“ Mischteil).",
    [B("2 ** 2 + 3 ** 2", "Annas Ergebnis 13 als Unterschied angegeben"),
     B("5 * 5", "Bens Ergebnis 25 als Unterschied angegeben"),
     B("5 * 5 + 2 ** 2 + 3 ** 2", "beide Ergebnisse addiert statt voneinander abgezogen")]), form="zwei_wege", lp=LP, idee="potenz_von_summe")
neu(T, "fehler_finden", "sicherung", "fehler", W(
    "Ein Kind rechnet: Zeile 1: (2/3)⁻² = (3/2)². Zeile 2: (3/2)² = 3²/2 = 9/2. Zeile 3: 9/2 = 4,5. Zeile 4: Also ist (2/3)⁻² = 4,5. In welcher Zeile steckt der erste Fehler?",
    "In Zeile 2, weil das Quadrat auch für den Nenner gilt: (3/2)² = 9/4.",
    [("In Zeile 1, weil ein negativer Exponent nicht den Kehrwert bildet.", "geglaubt, der negative Exponent bilde nicht den Kehrwert; (2/3)⁻² = (3/2)² stimmt"),
     ("In Zeile 3, weil 9/2 gleich 4 ist.", "9/2 falsch in eine Dezimalzahl verwandelt; 9 : 2 = 4,5 stimmt"),
     ("In Zeile 4, weil das Ergebnis eines negativen Exponenten kleiner als 1 sein muss.", "gedacht, ein negativer Exponent mache jeden Wert kleiner als 1; bei einem Bruch kleiner als 1 als Basis wird der Wert größer")],
    "Zeile 1 ist richtig: Ein negativer Exponent bildet den Kehrwert, (2/3)⁻² = (3/2)². In Zeile 2 wird nur der Zähler quadriert: richtig ist (3/2)² = 3²/2² = 9/4. Zeile 3 rechnet 9/2 = 4,5 richtig, Zeile 4 übernimmt den Fehler. Richtig: (2/3)⁻² = 9/4 = 2,25.",
    lambda: F(2, 3) ** -2 == F(9, 4) and F(3, 2) ** 2 == F(9, 4) and F(3, 2) ** 2 != F(9, 2) and F(9, 2) == F("4.5") and F(9, 2) != 4, pos=1), form="fehler_detektiv", lp=LP, idee="kehrwert_bruch")
neu(T, "fehler_finden", "sicherung", "begruenden", W(
    "Ein Kind soll begründen, welchen Wert 5⁰ hat. Welche Begründung ist richtig?",
    "5⁰ = 1, denn im Muster 125, 25, 5 teilt man jedes Mal durch 5, und 5 : 5 = 1.",
    [("5⁰ = 1, denn 5 mal 0 ergibt 0, und dazu zählt man die 1 am Anfang.", "eine Rechnung mit Basis mal Exponent erfunden, die zufällig auf 1 kommt; sie erklärt nichts"),
     ("5⁰ = 5, denn beim Exponenten 0 bleibt die Basis 5 unverändert stehen.", "Exponent 0 als „nichts tun“ gelesen und die Basis 5 behalten"),
     ("5⁰ = 0, denn der Exponent 0 zeigt an, dass keine 5 mehr vorhanden ist.", "den Exponenten 0 als „kein Wert“ gelesen und die Potenz gleich 0 gesetzt")],
    "Das Muster 125, 25, 5 teilt bei jedem Schritt nach rechts durch 5. Der nächste Wert ist 5 : 5 = 1, und der Exponent ist dann 0. Das passt zur Regel, dass jede Basis ungleich 0 mit Exponent 0 den Wert 1 hat. Die Rechnung 5 · 0 + 1 liefert nur zufällig 1.",
    lambda: 5 ** 3 // 5 == 25 and 25 // 5 == 5 and 5 // 5 == 1 and 5 ** 0 == 1 and 5 ** 0 != 0 and 5 ** 0 != 5), lp=LP, idee="hoch_null_begruenden")
neu(T, "fehler_finden", "sicherung", "umkehr", Z(
    "Eine Potenz mit der Basis 5 hat den Wert 0,04. Wie lautet ihr ganzzahliger Exponent a in 5^a = 0,04?",
    -2, "0 - 2", "2 - 4",
    "0,04 = 4/100 = 1/25 = 1/5² = 5⁻². Also ist a = −2. Probe: 5⁻² = 1/5² = 1/25 = 0,04.",
    [B("2", "das Minus im Exponenten vergessen: 5² = 25"),
     B("4", "die Nachkommastelle 4 selbst als Exponenten genommen"),
     B("0 - 25", "den Nenner 25 mit Minus als Exponenten genommen")]), lp=LP, idee="exponent_aus_dezimal")
