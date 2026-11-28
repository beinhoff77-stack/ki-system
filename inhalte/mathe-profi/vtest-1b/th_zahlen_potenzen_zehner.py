T = "zahlen.potenzen_zehner"
LP = "M6 1 Rationale Zahlen (Zehnerpotenzen, wissenschaftliche Schreibweise, Vorsilben)"
REGEL[(T, "gross_wissenschaftlich")] = "rr.stellenwert"
REGEL[(T, "negativer_exponent")] = "rr.potenz"
REGEL[(T, "vorsilben_klein")] = "id.verhaeltnisse.groesse"
REGEL[(T, "vergleichen_pruefen")] = "id.zahlen.schreibweisen"
ABG[(T, "gross_wissenschaftlich")] = "Die Übungen schreiben eine große Zahl als a · 10ⁿ; hier wird ein Fehler beim Komma-Verschieben gefunden, eine Fehlvorstellung zu den Nullen geklärt, rückwärts geschlossen und die Bedingung für den Vorfaktor begründet."
ABG[(T, "negativer_exponent")] = "Die Übungen schreiben 10⁻ⁿ als Dezimalzahl; hier werden Vorfaktor und Exponent zusammen betrachtet, in Stücken gedacht, rückwärts gerechnet und die Fehlvorstellung „Minus macht negativ“ geklärt."
ABG[(T, "vorsilben_klein")] = "Die Übungen wandeln eine Einheit um; hier werden Modelle und Zeichnungen vergrößert, Maßzahl und Länge unterschieden, Verhältnisse über Einheiten gebildet und eine fehlerhafte Umrechnungskette berichtigt."
ABG[(T, "vergleichen_pruefen")] = "Die Übungen vergleichen zwei einfache Zehnerpotenzen; hier werden nicht normierte Zahlen geordnet, Verhältnisse in Potenzform gebildet, ein Fehler beim Angleichen der Exponenten gefunden und der Vergleich begründet."
# ───────── gross_wissenschaftlich ─────────
neu(T, "gross_wissenschaftlich", "test", "fehler", L(
    "Ein Kind soll 23,1 · 10⁴ in wissenschaftliche Schreibweise bringen und rechnet: Zeile 1: Ich muss das Komma verschieben. Zeile 2: 23,1 = 2,31 · 10. Zeile 3: Die Zahl bleibt dieselbe, also bleibt der Exponent 4: 23,1 · 10⁴ = 2,31 · 10⁴. In welcher Zeile steckt der erste Fehler? Welcher Exponent gehört richtig an die 10?",
    "Fehler in Zeile □, richtig: 23,1 · 10⁴ = 2,31 · 10^□", [3, 5], ["3", "4 + 1"], ["2 + 1", "5"],
    "Zeile 1 sagt nur, was getan wird. Zeile 2 stimmt (2,31 · 10 = 23,1). In Zeile 3 wird die Zehn aus Zeile 2 vergessen: 23,1 · 10⁴ = 2,31 · 10 · 10⁴ = 2,31 · 10⁵. Wird das Komma um eine Stelle nach links geschoben, muss der Exponent um 1 größer werden, sonst ändert sich der Wert der Zahl.",
    {0: [(2, "Zeile 2 genannt, weil dort das Komma verschoben wird, obwohl diese Zeile stimmt", "2"), (1, "Zeile 1 genannt, obwohl dort nur das Vorgehen steht", "1")], 1: [(4, "den Exponenten unverändert übernommen", "4"), (3, "den Exponenten beim Verschieben des Kommas verkleinert", "4 - 1"), (14, "die Zehn zum Exponenten addiert", "4 + 10")]}), form="fehler_detektiv", lp=LP, idee="komma_ausgleich")
neu(T, "gross_wissenschaftlich", "korrektur", "darstellung", L(
    "Eine Zahl a · 10ⁿ ist in wissenschaftlicher Schreibweise geschrieben (a zwischen 1 und 10, n eine ganze Zahl). Sie ist größer als 5 000 und kleiner als 80 000. Dann ist der kleinste mögliche Exponent n = □ und der größte mögliche Exponent n = □.",
    "kleinstes n = □, größtes n = □", [3, 4], ["4 - 1", "5 - 1"], ["2 + 1", "8 / 2"],
    "Für n = 3 steht a · 1 000 da, und für a zwischen 5 und 10 liegt das zwischen 5 000 und 10 000: möglich. Für n = 2 wäre die Zahl kleiner als 1 000, also zu klein. Für n = 4 steht a · 10 000 da; mit a unter 8 liegt das unter 80 000: möglich. Für n = 5 wäre die Zahl mindestens 100 000 und damit zu groß. Also gilt n = 3 oder n = 4.",
    {0: [(4, "den Exponenten der oberen Grenze als kleinsten genommen", "4"), (2, "den Exponenten um eins zu klein bestimmt", "3 - 1")],
     1: [(5, "die Zahl der Ziffern von 80 000 als Exponenten genommen", "5"), (3, "den größten Exponenten gleich dem kleinsten gesetzt", "3")]}),
    form="bruecke", lp=LP, idee="bereich_exponent")
neu(T, "gross_wissenschaftlich", "korrektur", "umkehr", Z(
    "Eine Zahl a · 10ⁿ ist in wissenschaftlicher Schreibweise geschrieben. Verdoppelt man sie, erhält man 1,6 · 10¹⁰. Wie groß ist n bei der ursprünglichen Zahl?",
    9, "10 - 1", "9",
    "Die ursprüngliche Zahl ist die Hälfte von 1,6 · 10¹⁰, also 0,8 · 10¹⁰. Der Vorfaktor 0,8 ist kleiner als 1: 0,8 · 10¹⁰ = 8 · 10⁹. Die ursprüngliche Zahl ist also 8 · 10⁹ und n = 9. Probe: 2 · 8 · 10⁹ = 16 · 10⁹ = 1,6 · 10¹⁰.",
    [B("10", "nur den Vorfaktor halbiert und den Exponenten unverändert gelassen"),
     B("11", "den Exponenten beim Halbieren vergrößert statt verkleinert"),
     B("8", "den Exponenten um eins zu klein gesetzt")]), form="umkehren", lp=LP, idee="rueckwaerts_halbieren")
neu(T, "gross_wissenschaftlich", "korrektur", "darstellung", W(
    "Kim sagt: „In der Zahl 3,5 · 10⁶ stehen sechs Nullen, denn im Exponenten steht die 6.“ Welche Aussage stimmt?",
    "Kim irrt, denn ausgeschrieben ist 3,5 · 10⁶ = 3 500 000, und dort stehen nicht sechs, sondern nur fünf Nullen.",
    [("Kim hat recht, denn der Exponent gibt bei jeder Zahl der Form a · 10ⁿ die Zahl der Nullen an.", "den Exponenten allgemein als Zahl der Nullen gedeutet; die Ziffern des Vorfaktors nehmen aber Stellen weg"),
     ("Kim hat recht, denn in 3 500 000 stehen sechs Nullen, wenn man die 5 mitzählt.", "die Ziffer 5 als Null mitgezählt"),
     ("Kim irrt, denn der Exponent gibt die Zahl der Ziffern an, und dort stehen sechs Ziffern.", "den Exponenten als Zahl der Ziffern gedeutet; es sind sieben Ziffern")],
    "3,5 · 10⁶ = 3,5 · 1 000 000 = 3 500 000. Das Komma wandert um 6 Stellen nach rechts: Die 5 füllt die erste Stelle auf, danach stehen noch fünf Nullen. Der Exponent gibt die Zahl der Stellen an, um die das Komma wandert, nicht die Zahl der Nullen.",
    lambda: 3.5e6 == 3500000 and str(3500000).count("0") == 5), lp=LP, idee="nullen_fehlvorstellung")
neu(T, "gross_wissenschaftlich", "sicherung", "umkehr", Z(
    "Ein Buch hat etwa 4 · 10⁵ Zeichen. Ein Speicher fasst 2 · 10⁹ Zeichen. Wie viele solcher Bücher passen höchstens in den Speicher?",
    5000, "2000000000 / 400000", "2000000000 / 400000",
    "2 · 10⁹ = 2 000 000 000 und 4 · 10⁵ = 400 000. Es passen 2 000 000 000 : 400 000 = 5 000 Bücher. Mit Potenzen: 2 : 4 = 0,5 und 10⁹ : 10⁵ = 10⁴, also 0,5 · 10⁴ = 5 000.",
    [B("500", "den Exponenten um eins zu klein gerechnet"),
     B("50000", "den Exponenten um eins zu groß gerechnet"),
     B("20000", "die Vorfaktoren falsch herum geteilt")], einheit="Bücher"), lp=LP, idee="passt_wie_oft")
neu(T, "gross_wissenschaftlich", "sicherung", "begruenden", W(
    "Warum ist 0,5 · 10⁸ keine wissenschaftliche Schreibweise der Zahl 50 000 000?",
    "Der Vorfaktor 0,5 ist kleiner als 1, wissenschaftlich wäre 5 · 10⁷.",
    [("Der Exponent 8 ist zu groß; man darf höchstens 10⁷ verwenden.", "eine Höchstgrenze für den Exponenten erfunden; Exponenten dürfen beliebig groß sein"),
     ("0,5 · 10⁸ ist eine andere Zahl als 50 000 000; richtig wäre 0,05 · 10⁸.", "den Wert falsch gerechnet: 0,5 · 10⁸ ist bereits 50 000 000, nur der Vorfaktor passt nicht"),
     ("Der Vorfaktor muss eine ganze Zahl sein; 0,5 ist keine ganze Zahl.", "verlangt, dass der Vorfaktor ganzzahlig ist; auch Dezimalzahlen zwischen 1 und 10 sind erlaubt")],
    "0,5 · 10⁸ = 50 000 000 ist richtig als Wert. Es fehlt nur die Bedingung 1 ≤ a < 10: 0,5 ist kleiner als 1. Man verschiebt das Komma um eine Stelle nach rechts und verkleinert den Exponenten: 5 · 10⁷ = 50 000 000.",
    lambda: 0.5 * 10 ** 8 == 5 * 10 ** 7 == 50000000 and not 1 <= 0.5 < 10 and 1 <= 5 < 10 and 1 <= 2.5 < 10), lp=LP, idee="bedingung_begruenden")
neu(T, "gross_wissenschaftlich", "sicherung", "transfer", W(
    "Welche der beiden Zahlen 9,9 · 10⁶ und 1,0 · 10⁷ ist größer? Welche Aussage stimmt?",
    "1,0 · 10⁷ ist größer, denn 10⁷ ist zehnmal 10⁶, und 9,9 ist kleiner als zehn.",
    [("9,9 · 10⁶ ist größer, denn die Zahl 9,9 ist größer als die Zahl 1,0.", "nur die Vorfaktoren verglichen"),
     ("Beide sind gleich groß, denn 9,9 ist fast zehn und zehnmal 10⁶ ist 10⁷.", "„fast gleich“ mit „gleich“ verwechselt"),
     ("Man kann sie nicht vergleichen, denn die beiden Zahlen haben verschiedene Exponenten.", "geglaubt, Zahlen mit verschiedenen Exponenten ließen sich nicht ordnen")],
    "Mit demselben Exponenten geschrieben ist 1,0 · 10⁷ = 10 · 10⁶. Dann steht 10 gegen 9,9: 1,0 · 10⁷ ist ein wenig größer. In wissenschaftlicher Schreibweise ist der Vorfaktor immer kleiner als 10; deshalb entscheidet zuerst der Exponent, und erst bei gleichem Exponenten der Vorfaktor.",
    lambda: F("9.9") * 10 ** 6 < F("1.0") * 10 ** 7 and F("9.9") * 10 ** 6 != F("1.0") * 10 ** 7), lp=LP, idee="groesser_ueber_exponent")
# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "transfer", L(
    "Die Zahl 0,000 04 wird auf zwei Arten mit einer Zehnerpotenz geschrieben. Ergänze die Exponenten: 0,000 04 = 4 · 10^□ und 0,000 04 = 40 · 10^□.",
    "4 · 10^□ und 40 · 10^□", [-5, -6], ["0 - 5", "0 - 6"], ["-5", "0 - 5 - 1"],
    "Die 4 steht an der 5. Stelle hinter dem Komma, also ist 0,000 04 = 4 · 10⁻⁵. Wird der Vorfaktor zehnmal so groß (40 statt 4), muss die Zehnerpotenz zehnmal so klein werden, der Exponent also um 1 kleiner: 40 · 10⁻⁶. Probe: 40 · 0,000 001 = 0,000 04.",
    {0: [(5, "das Minus im Exponenten vergessen", "5"), (-4, "nur die Nullen hinter dem Komma gezählt", "0 - 4")],
     1: [(-5, "den Exponenten vom ersten Vorfaktor unverändert übernommen", "0 - 5"), (-4, "den Exponenten in die falsche Richtung um eins verändert", "0 - 4"), (-7, "den Exponenten um zwei statt um eins verkleinert", "0 - 7")]}), lp=LP, idee="vorfaktor_und_exponent")
neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Man startet bei 4 000 und teilt immer wieder durch zehn. Nach wie vielen Teilungen ist das Ergebnis zum ersten Mal kleiner als 0,000 000 1?",
    11, "3 + 8", "11",
    "4 000 = 4 · 10³ und 0,000 000 1 = 10⁻⁷. Jede Teilung durch zehn senkt den Exponenten um 1. Nach 10 Teilungen ist das Ergebnis 4 · 10⁻⁷ = 0,000 000 4 und noch größer als 10⁻⁷. Nach 11 Teilungen ist es 4 · 10⁻⁸ = 0,000 000 04 und damit zum ersten Mal kleiner.",
    [B("3 + 7", "schon gestoppt, als die Zehnerpotenz erreicht war, obwohl der Wert dann noch größer als die Grenze ist"),
     B("7", "nur die Stellen der kleinen Zahl gezählt"),
     B("7 - 3", "die Exponenten der beiden Zahlen voneinander abgezogen")], einheit="Teilungen"), form="umkehren", lp=LP, idee="teilungen_zaehlen")
neu(T, "negativer_exponent", "korrektur", "umkehr", W(
    "Ein Ganzes wird in eine Million gleiche Stücke zerlegt. Ein Stück ist 10⁻⁶ vom Ganzen. Welche Aussage stimmt?",
    "Zehn solche Stücke zusammen sind ein Hunderttausendstel vom Ganzen.",
    [("Zehn solche Stücke zusammen sind ein Millionstel vom Ganzen.", "geglaubt, dass sich der Wert beim Zusammenlegen nicht ändert"),
     ("Hundert solche Stücke zusammen sind ein Hunderttausendstel vom Ganzen.", "beim Zusammenlegen um eine Stufe zu weit gegangen"),
     ("Zehn solche Stücke zusammen sind ein Zehnmillionstel vom Ganzen.", "beim Zusammenlegen in die falsche Richtung gerechnet: mehr Stücke ergeben etwas Größeres")],
    "Ein Stück ist 10⁻⁶ = 0,000 001. Zehn Stücke sind 10 · 10⁻⁶ = 10⁻⁵ = 0,000 01, also ein Hunderttausendstel. Hundert Stücke wären 10⁻⁴, ein Zehntausendstel. Mehr Stücke ergeben immer einen größeren Anteil, nie einen kleineren.",
    lambda: 10 * F(10) ** -6 == F(10) ** -5 == F(1, 100000) and 100 * F(10) ** -6 != F(10) ** -5 and 10 * F(10) ** -6 != F(10) ** -6 and 10 * F(10) ** -6 > F(10) ** -6), lp=LP, idee="groessenvorstellung_stuecke")
neu(T, "negativer_exponent", "korrektur", "darstellung", Z(
    "Eine Zehnerpotenz 10ⁿ ist 1 000-mal so klein wie 0,000 01. Wie groß ist n?",
    -8, "0 - 8", "0 - 5 - 3",
    "0,000 01 = 10⁻⁵. 1 000-mal so klein heißt durch 1 000 = 10³ teilen: 10⁻⁵ : 10³ = 10⁻⁸. Probe: 0,000 01 : 1 000 = 0,000 000 01, die 1 steht an der achten Stelle.",
    [B("8", "das Minus im Exponenten vergessen"),
     B("0 - 2", "den Exponenten von 1 000 addiert statt abgezogen"),
     B("0 - 15", "die Hochzahlen malgenommen statt abgezogen")]), form="bruecke", lp=LP, idee="skalierung_rueckwaerts")
neu(T, "negativer_exponent", "sicherung", "parameter", Z(
    "Man nimmt ein Hundertstel von einem Millionstel und davon noch ein Tausendstel. Wie viele Nullen stehen zwischen dem Komma und der 1, wenn man das Ergebnis als Dezimalzahl schreibt?",
    10, "2 + 6 + 3 - 1", "11 - 1",
    "Ein Hundertstel ist 10⁻², ein Millionstel ist 10⁻⁶, ein Tausendstel ist 10⁻³. Hintereinander ausgeführt: 10⁻² · 10⁻⁶ · 10⁻³ = 10⁻¹¹ = 0,000 000 000 01. Die 1 steht an der elften Stelle, davor stehen 10 Nullen.",
    [B("11", "den Exponenten als Zahl der Nullen genommen"),
     B("1 + 5 + 2", "die Nullen der drei Dezimalzahlen zusammengezählt"),
     B("2 * 6 * 3", "die Hochzahlen malgenommen statt addiert")], einheit="Nullen"), lp=LP, idee="zehnerpotenzen_verketten")
neu(T, "negativer_exponent", "sicherung", "darstellung", Z(
    "Man startet bei 10⁻⁷ und multipliziert immer wieder mit 10, bis man bei 10¹ ankommt. Nach der Hälfte dieser Schritte steht die Zehnerpotenz 10ⁿ da. Wie groß ist n?",
    -3, "0 - 7 + 8 / 2", "(0 - 7 + 1) / 2",
    "Von 10⁻⁷ bis 10¹ steigt der Exponent von −7 auf 1, das sind 8 Schritte. Nach der Hälfte, also nach 4 Schritten, ist der Exponent −7 + 4 = −3. Die Zehnerpotenz in der Mitte ist 10⁻³, nicht die Zahl in der Mitte zwischen den Werten. Probe: Von 10⁻⁷ bis 10⁻³ sind es 4 Schritte, von 10⁻³ bis 10¹ auch.",
    [B("3", "das Minus im Exponenten vergessen"),
     B("0 - 8 / 2", "die Hälfte der Schrittzahl selbst als Exponenten genommen"),
     B("0 - 7 + 1", "die beiden Exponenten addiert statt die Mitte zu bilden")]), form=None, lp=LP, idee="mitte_der_potenzen")
neu(T, "negativer_exponent", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 10⁻³ bedeutet 1 : 10³, also 1 : 1 000. Zeile 2: Der Exponent ist negativ, also ist auch die Zahl 10⁻³ negativ, nämlich −0,001. Zeile 3: Also ist 10⁻³ · 1 000 = −0,001 · 1 000 = −1. In welcher Zeile steckt der erste Fehler? Wie viel ist 10⁻³ · 1 000 richtig?",
    "Fehler in Zeile □, richtig: 10⁻³ · 1 000 = □", [2, 1], ["2", "1 + 0"], ["1 + 1", "1000 / 1000"],
    "Zeile 1 stimmt: 10⁻³ = 1 : 1 000 = 0,001. In Zeile 2 steckt der Fehler: Das Minus im Exponenten macht die Zahl nicht negativ, sondern klein. 10⁻³ = 0,001 ist positiv. Zeile 3 folgt aus dem Fehler. Richtig: 10⁻³ · 1 000 = 0,001 · 1 000 = 1.",
    {0: [(1, "Zeile 1 genannt, obwohl dort die Bedeutung richtig angegeben ist", "1"), (3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(-1, "das Minus aus dem Exponenten mit in die Zahl genommen", "0 - 1"), (0, "die kleine Zahl mit dem Tausendfachen als null gerechnet", "0"), (-3, "den Exponenten als Ergebnis genommen", "0 - 3")]}), form="fehler_detektiv", lp=LP, idee="minus_macht_negativ")
# ───────── vorsilben_klein ─────────
neu(T, "vorsilben_klein", "test", "transfer", L(
    "Ein Filter lässt nur Teilchen durch, die kürzer als 0,2 µm sind. Vier Teilchen werden geprüft: A ist 90 nm lang, B ist 0,15 µm lang, C ist 0,0002 mm lang, D ist 20 nm lang. (1 nm = 10⁻⁹ m, 1 µm = 10⁻⁶ m, 1 mm = 10⁻³ m.) Es kommen □ Teilchen durch den Filter, und das längste davon ist □ nm lang.",
    "□ Teilchen kommen durch, das längste ist □ nm lang", [3, 150], ["4 - 1", "0.15 * 1000"], ["1 + 2", "15 * 10"],
    "Die Grenze ist 0,2 µm = 200 nm. A mit 90 nm ist kürzer, B mit 0,15 µm = 150 nm ist kürzer, C mit 0,0002 mm = 0,2 µm = 200 nm ist genau so lang wie die Grenze und kommt nicht durch, D mit 20 nm ist kürzer. Es kommen also A, B und D durch, das sind 3 Teilchen. Das längste davon ist B mit 150 nm.",
    {0: [(4, "auch das Teilchen mitgezählt, das genau so lang wie die Grenze ist", "4"), (2, "nur die Maßzahlen mit der Grenze verglichen, ohne die Einheiten anzugleichen", "2")],
     1: [(200, "die Länge des Teilchens genommen, das genau auf der Grenze liegt", "200"), (90, "das Teilchen mit der größten Maßzahl in Nanometern genommen, ohne umzurechnen", "90")]}),
    lp=LP, idee="filter_entscheiden")
neu(T, "vorsilben_klein", "korrektur", "darstellung", W(
    "Tom sagt: „800 nm sind länger als 2 µm, denn 800 ist größer als 2.“ Welche Aussage stimmt?",
    "Tom irrt, denn 800 nm sind 0,8 µm, und das ist nicht länger, sondern kürzer als 2 µm.",
    [("Tom hat recht, denn die Einheit spielt beim Vergleich von Längen keine Rolle.", "Maßzahl und Länge gleichgesetzt; die Einheit entscheidet mit"),
     ("Tom hat recht, denn ein Nanometer ist eine größere Einheit als ein Mikrometer.", "Nano und Mikro in der Größe vertauscht"),
     ("Die beiden Längen sind gleich lang, denn 800 nm und 2 µm sind nur verschieden aufgeschrieben.", "die beiden Längen für gleich gehalten, obwohl der Faktor zwischen den Einheiten nicht zu den Maßzahlen passt")],
    "1 µm = 1 000 nm. Also sind 800 nm = 0,8 µm. 0,8 µm sind kürzer als 2 µm. Die Maßzahl allein sagt nichts über die Länge: Man muss erst in dieselbe Einheit umrechnen. Nano ist tausendmal kleiner als Mikro.",
    lambda: F(800) * F(10) ** -9 < 2 * F(10) ** -6 and F(800) * F(10) ** -9 == F("0.8") * F(10) ** -6 and F(10) ** -9 < F(10) ** -6), form="bruecke", lp=LP, idee="maszahl_statt_laenge")
neu(T, "vorsilben_klein", "korrektur", "umkehr", Z(
    "Ein Virus ist 4 500 nm lang. In Millimetern schreibt man die Länge als 4,5 · 10ⁿ mm. Wie groß ist n? (1 nm = 10⁻⁹ m, 1 mm = 10⁻³ m)",
    -3, "0 - 3", "3 - 6",
    "1 mm = 10⁶ nm. 4 500 nm = 4 500 : 1 000 000 mm = 0,0045 mm. Das Komma steht dann hinter der ersten Ziffer, es ist drei Stellen nach rechts gewandert: 0,0045 = 4,5 · 10⁻³. Also ist n = −3.",
    [B("3", "das Minus im Exponenten vergessen"),
     B("0 - 6", "nur den Faktor zwischen Nanometer und Millimeter als Exponenten genommen"),
     B("0 - 9", "die Hochzahl der Vorsilbe Nano als Exponenten genommen")]), form="umkehren", lp=LP, idee="umrechnen_wissenschaftlich")
neu(T, "vorsilben_klein", "korrektur", "umkehr", W(
    "Ein Sandkorn ist etwa 0,5 mm groß. Ein Staubkorn ist etwa hundertmal kleiner. Welche Angabe passt zur Größe des Staubkorns?",
    "etwa 5 µm, denn 0,5 mm sind 500 µm, und ein Hundertstel davon sind 5 µm.",
    [("etwa 0,005 µm, denn 0,5 geteilt durch 100 ist 0,005, und µm ist die Einheit für kleine Körner.", "nur die Maßzahl geteilt und die Einheit gewechselt, ohne umzurechnen"),
     ("etwa 50 µm, denn 0,5 mm sind 500 µm, und ein Zehntel davon sind 50 µm.", "um den Faktor zehn statt hundert verkleinert"),
     ("etwa 5 nm, denn von Millimeter nach Nanometer geht man eine Stufe weiter und teilt durch hundert.", "die Einheiten nach der Größe der Maßzahl und nicht nach dem Faktor zwischen ihnen gewählt")],
    "0,5 mm = 500 µm, denn 1 mm = 1 000 µm. Hundertmal kleiner heißt durch 100 teilen: 500 µm : 100 = 5 µm. Zwischen Millimeter und Nanometer liegt der Faktor eine Million, nicht hundert.",
    lambda: F(5, 10) * 1000 / 100 == 5 and F(5, 1000) != 5 and F(5, 10) * 1000 / 10 != 5), lp=LP, idee="verhaeltnis_einheiten")
neu(T, "vorsilben_klein", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 1 nm = 10⁻⁹ m. Zeile 2: 1 µm = 10⁻⁶ m. Zeile 3: Also ist 10⁻⁶ : 10⁻⁹ = 10⁻³. Zeile 4: Also sind 1 µm gleich 10⁻³ nm. In welcher Zeile steckt der erste Fehler? Wie viele Nanometer sind 1 µm richtig?",
    "Fehler in Zeile □, richtig: 1 µm = □ nm", [3, 1000], ["3", "10 ** 3"], ["2 + 1", "1000"],
    "Zeile 1 und Zeile 2 sind richtig. In Zeile 3 ist die Rechnung falsch: 10⁻⁶ : 10⁻⁹ = 10⁻⁶ · 10⁹ = 10³, nicht 10⁻³. Also sind 1 µm gleich 10³ nm = 1000 nm. Zeile 4 folgt aus dem Fehler in Zeile 3.",
    {0: [(4, "die Schlusszeile genannt, weil dort der falsche Wert 10⁻³ steht", "4"), (1, "Zeile 1 genannt, obwohl dort die Vorsilbe richtig steht", "1")], 1: [(-3, "das falsche Ergebnis 10⁻³ als Zahl −3 genommen", "0 - 3"), (1, "die Vorsilben als Faktor 1 gelesen", "1"), (1000000, "mit 10⁶ gerechnet statt 10³", "10 ** 6")]}), form="fehler_detektiv", lp=LP, idee="fehler_kette")
neu(T, "vorsilben_klein", "sicherung", "rueckwaerts", W(
    "Ein Staubkorn ist 0,03 mm lang. Dieselbe Länge soll als 30 □m geschrieben werden. Welche Vorsilbe gehört in die Lücke?",
    "Mikro (µm), denn 0,03 mm sind 30 µm, und die Einheit µm ist tausendmal kleiner als mm.",
    [("Nano (nm), denn die Einheit muss kleiner werden, und Nano ist die kleinste Vorsilbe.", "nur auf „kleiner“ geachtet und den Faktor zwischen den Einheiten nicht geprüft"),
     ("Milli (mm), denn aus 0,03 wird 30, wenn man das Komma verschiebt, und die Einheit bleibt dabei dieselbe.", "die Maßzahl umgeschrieben und die Einheit nicht gewechselt"),
     ("Zenti (cm), denn eine größere Maßzahl gehört zu einer größeren Einheit.", "Größe der Einheit und Maßzahl gleichgesetzt; zu einer größeren Maßzahl gehört eine kleinere Einheit")],
    "Aus 0,03 mm wird 30 mal etwas: Die Maßzahl wird 1 000-mal größer, also muss die Einheit 1 000-mal kleiner sein. Ein Millimeter ist 1 000 Mikrometer, also 0,03 mm = 30 µm. Nanometer wären eine Million Mal kleiner als Millimeter, Zentimeter sind größer.",
    lambda: F(3, 100) * 1000 == 30 and F(3, 100) * 10 ** 6 != 30), lp=LP, idee="vorsilbe_gesucht")
neu(T, "vorsilben_klein", "sicherung", "darstellung", W(
    "Welche Angabe beschreibt dieselbe Länge wie 0,000 004 m?",
    "4 µm, denn 0,000 004 m sind 4 · 10⁻⁶ m, und 10⁻⁶ m ist ein Mikrometer.",
    [("4 nm, denn die Vier steht an der sechsten Stelle hinter dem Komma, und dazu gehört die Vorsilbe Nano.", "die Stelle der Ziffer mit der Vorsilbe verwechselt; Nano steht für 10⁻⁹, nicht für die sechste Stelle"),
     ("40 µm, denn 0,000 004 m = 40 · 10⁻⁷ m, und Mikro steht für 10⁻⁷.", "die Hochzahl der Vorsilbe Mikro falsch angegeben"),
     ("4 mm, denn ein Millimeter ist ein Millionstel Meter, und 0,000 004 sind vier Millionstel.", "Milli und Mikro vertauscht; ein Millimeter ist ein Tausendstel Meter")],
    "0,000 004 m = 4 · 10⁻⁶ m, denn die 4 steht an der sechsten Stelle hinter dem Komma. Die Vorsilbe Mikro steht für 10⁻⁶, also sind das 4 µm. Nano steht für 10⁻⁹, Milli für 10⁻³.",
    lambda: F(4) * F(10) ** -6 == F(4, 10 ** 6) and F(4) * F(10) ** -9 != F(4, 10 ** 6) and F(4) * F(10) ** -3 != F(4, 10 ** 6)), lp=LP, idee="vorsilbe_zehnerpotenz")
# ───────── vergleichen_pruefen ─────────
neu(T, "vergleichen_pruefen", "test", "transfer", L(
    "Gegeben sind drei Zahlen: A = 5 · 10⁻⁶, B = 0,2 · 10⁻⁴ und C = 30 · 10⁻⁷. Welche Zahl ist die kleinste, welche die größte? Trage jeweils die Nummer ein (1 = A, 2 = B, 3 = C).",
    "kleinste Zahl: □, größte Zahl: □", [3, 2], ["3", "1 + 1"], ["1 + 2", "2"],
    "Alle drei Zahlen mit dem Exponenten −7: A = 50 · 10⁻⁷, B = 0,2 · 10⁻⁴ = 200 · 10⁻⁷, C = 30 · 10⁻⁷. Die kleinste ist C (30), die größte ist B (200). Ausgeschrieben: A = 0,000 005, B = 0,000 02, C = 0,000 003.",
    {0: [(2, "nur die Vorfaktoren verglichen: 0,2 ist der kleinste Vorfaktor", "2"), (1, "die mittlere Zahl A genannt, ohne alle Zahlen auf einen gemeinsamen Exponenten zu bringen", "1")],
     1: [(3, "nur die Vorfaktoren verglichen: 30 ist der größte Vorfaktor", "3"), (1, "die mittlere Zahl A genannt, ohne alle Zahlen auf einen gemeinsamen Exponenten zu bringen", "1")]}), lp=LP, idee="normalisieren_ordnen")
neu(T, "vergleichen_pruefen", "korrektur", "darstellung", W(
    "Welche Aussage über die Zahlen 3 · 10⁻⁵ und 0,3 · 10⁻⁴ stimmt?",
    "Sie sind gleich, denn der Vorfaktor wird zehnmal kleiner und die Zehnerpotenz zehnmal größer.",
    [("0,3 · 10⁻⁴ ist kleiner, denn 0,3 ist kleiner als 3, und auf den Exponenten kommt es nicht an.", "nur die Vorfaktoren verglichen"),
     ("0,3 · 10⁻⁴ ist zehnmal so groß, denn −4 ist um eins größer als −5.", "nur die Exponenten verglichen und den Vorfaktor nicht beachtet"),
     ("Die beiden Zahlen sind verschieden, denn sie haben verschiedene Vorfaktoren und verschiedene Exponenten.", "geglaubt, dass verschiedene Schreibweisen immer verschiedene Zahlen bedeuten")],
    "0,3 · 10⁻⁴ = 0,3 · 10 · 10⁻⁵ = 3 · 10⁻⁵. Wird der Vorfaktor kleiner, muss die Zehnerpotenz im gleichen Maß größer werden, wenn die Zahl dieselbe bleiben soll. Ausgeschrieben: 0,000 03 in beiden Fällen.",
    lambda: F("0.3") * F(10) ** -4 == 3 * F(10) ** -5 and F("0.3") < 3), form="bruecke", lp=LP, idee="gleiche_zahl")
neu(T, "vergleichen_pruefen", "korrektur", "umkehr", W(
    "Ohne genau zu rechnen: Etwa wie oft passt die Länge 4,8 · 10⁻⁷ m in die Länge 2,1 · 10⁻⁴ m?",
    "etwa 400-mal, denn der Quotient der Vorfaktoren ist ungefähr 0,4 und die Zehnerpotenzen ergeben 10³.",
    [("etwa 40-mal, denn der Quotient der Vorfaktoren ist ungefähr 0,4 und die Zehnerpotenzen ergeben 10².", "den Unterschied der Exponenten um eins zu klein bestimmt"),
     ("etwa 4 000-mal, denn der Quotient der Vorfaktoren ist ungefähr 4 und die Zehnerpotenzen ergeben 10³.", "die Vorfaktoren falsch herum geteilt"),
     ("etwa 0,4-mal, denn der Quotient der Vorfaktoren ist ungefähr 0,4 und die Zehnerpotenzen fallen weg.", "die Exponenten beim Teilen nicht beachtet")],
    "Es geht um 2,1 · 10⁻⁴ : (4,8 · 10⁻⁷). Die Vorfaktoren: 2,1 : 4,8 ist etwa 0,4. Die Zehnerpotenzen: 10⁻⁴ : 10⁻⁷ = 10³. Zusammen etwa 0,4 · 10³ = 400. Genau sind es etwa 437,5.",
    lambda: 300 < F("2.1") * F(10) ** -4 / (F("4.8") * F(10) ** -7) < 500), lp=LP, idee="groessenordnung_quotient")
neu(T, "vergleichen_pruefen", "korrektur", "umkehr", Z(
    "Wie viele Zehnerpotenzen 10ⁿ (n eine ganze Zahl, auch negativ oder null) liegen zwischen 0,000 000 3 und 40 000? Die beiden Grenzen selbst zählen nicht mit.",
    11, "4 + 6 + 1", "5 + 6",
    "0,000 000 3 = 3 · 10⁻⁷ und 40 000 = 4 · 10⁴. Die Zehnerpotenz 10⁻⁷ ist kleiner als 3 · 10⁻⁷ und gehört nicht dazu, 10⁻⁶ ist größer und gehört dazu. Oben ist 10⁴ = 10 000 kleiner als 40 000 und gehört dazu, 10⁵ ist größer. Die Exponenten −6 bis 4 sind 4 + 6 + 1 = 11 Zahlen (die 0 gehört dazu).",
    [B("4 + 6", "die Zehnerpotenz 10⁰ nicht mitgezählt"),
     B("4 + 7 + 1", "auch die Zehnerpotenz mitgezählt, die knapp unter der unteren Grenze liegt"),
     B("4 * 6", "die beiden Exponenten malgenommen")], einheit="Zehnerpotenzen"), form="umkehren", lp=LP, idee="raster_grenzen")
neu(T, "vergleichen_pruefen", "sicherung", "fehler", L(
    "Ein Kind vergleicht 6 · 10⁻⁷ und 4 · 10⁻⁶ und rechnet: Zeile 1: Ich schreibe beide Zahlen mit dem Exponenten −7. Zeile 2: Dann ist 4 · 10⁻⁶ = 0,4 · 10⁻⁷, denn das Komma geht eine Stelle nach links. Zeile 3: Also ist 6 · 10⁻⁷ größer als 4 · 10⁻⁶. In welcher Zeile steckt der erste Fehler? Welcher Vorfaktor gehört richtig vor 10⁻⁷?",
    "Fehler in Zeile □, richtig: 4 · 10⁻⁶ = □ · 10⁻⁷", [2, 40], ["2", "4 * 10"], ["1 + 1", "400 / 10"],
    "Zeile 1 sagt nur, was getan wird. In Zeile 2 steckt der Fehler: 10⁻⁷ ist zehnmal kleiner als 10⁻⁶, deshalb muss der Vorfaktor zehnmal größer werden: 4 · 10⁻⁶ = 40 · 10⁻⁷. Zeile 3 folgt aus dem Fehler. Richtig ist: 4 · 10⁻⁶ ist größer als 6 · 10⁻⁷.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3"), (1, "Zeile 1 genannt, obwohl dort nur das Vorgehen steht", "1")], 1: [(4, "den Vorfaktor unverändert übernommen", "4"), (400, "den Vorfaktor um zwei Stellen verschoben statt um eine", "4 * 100")]}), form="fehler_detektiv", lp=LP, idee="angleichen_richtung")
neu(T, "vergleichen_pruefen", "sicherung", "umkehr", Z(
    "Eine Zahl wird mit 10⁻⁴ malgenommen und ergibt 0,006. Welche Zahl war es?",
    60, "0.006 * 10000", "6 * 10000 / 1000",
    "Malnehmen mit 10⁻⁴ heißt durch 10 000 teilen. Rückwärts muss man mit 10 000 malnehmen: 0,006 · 10 000 = 60. Probe: 60 · 10⁻⁴ = 60 : 10 000 = 0,006.",
    [B("0.006 * 100", "mit 100 statt mit 10 000 malgenommen"),
     B("0.006 * 1000", "mit 1 000 statt mit 10 000 malgenommen"),
     B("6 * 100", "die Ziffer 6 mit 100 malgenommen")]), lp=LP, idee="faktor_rueckwaerts")
neu(T, "vergleichen_pruefen", "sicherung", "begruenden", W(
    "Warum ist 9 · 10⁻⁶ größer als 4 · 10⁻⁷? Welche Begründung stimmt?",
    "Man kann beide mit 10⁻⁶ vergleichen, denn 4 · 10⁻⁷ = 0,4 · 10⁻⁶ ist kleiner und 9 · 10⁻⁶ ist größer.",
    [("Die Zahl mit dem größeren Betrag im Exponenten ist immer die größere, denn −7 liegt weiter von null entfernt als −6.", "den Betrag des negativen Exponenten für die Größe gehalten; 10⁻⁷ ist kleiner als 10⁻⁶"),
     ("Die Vorfaktoren entscheiden immer allein, denn der Exponent ist nur eine Schreibhilfe.", "den Exponenten für unwichtig gehalten"),
     ("Die beiden Zahlen lassen sich gar nicht vergleichen, denn die Vorfaktoren 9 und 4 sind verschieden.", "geglaubt, nur Zahlen mit gleichem Vorfaktor ließen sich vergleichen")],
    "4 · 10⁻⁷ ist ein Zehntel von 4 · 10⁻⁶, also ist 4 · 10⁻⁷ = 0,4 · 10⁻⁶. Beide Zahlen haben nun den Exponenten −6, und die Vorfaktoren 0,4 und 9 zeigen: 9 · 10⁻⁶ ist größer. Ausgeschrieben: 0,000 009 gegen 0,000 000 4.",
    lambda: F(9) * F(10) ** -6 > 4 * F(10) ** -7 and 4 * F(10) ** -7 == F("0.4") * F(10) ** -6), lp=LP, idee="referenz_vergleich")
