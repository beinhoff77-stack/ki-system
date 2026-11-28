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
neu(T, "gross_wissenschaftlich", "korrektur", "darstellung", W(
    "Welche Angabe beschreibt die Zahl 3,85 · 10⁷?",
    "38,5 Millionen",
    [("3,85 Millionen", "die Million mit 10⁶ gleichgesetzt, aber 10⁷ ist das Zehnfache davon: der Exponent wurde nicht beachtet"),
     ("385 Millionen", "das Komma beim Vorfaktor nach rechts verschoben, aber den Exponenten dabei nicht verkleinert"),
     ("3,85 Milliarden", "die Milliarde mit 10⁷ verwechselt; 10⁹ ist eine Milliarde")],
    "10⁷ sind zehn Millionen. 3,85 · 10⁷ = 3,85 · 10 Millionen = 38,5 Millionen = 38 500 000. Eine Million ist 10⁶, eine Milliarde 10⁹.",
    lambda: 3.85e7 == 38.5e6 and 3.85e7 != 3.85e6 and 3.85e7 != 385e6 and 3.85e7 != 3.85e9),
    form="bruecke", lp=LP, idee="zehnerpotenz_in_worten")
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
neu(T, "gross_wissenschaftlich", "sicherung", "transfer", Z(
    "Die Zahl 7,5 · 10⁷ wird mit 4 malgenommen. Das Ergebnis wird wieder in wissenschaftlicher Schreibweise a · 10ⁿ geschrieben. Wie groß ist n?",
    8, "7 + 1", "8",
    "7,5 · 4 = 30. Also ist das Ergebnis 30 · 10⁷. Der Vorfaktor 30 ist zu groß für die wissenschaftliche Schreibweise: 30 · 10⁷ = 3 · 10 · 10⁷ = 3 · 10⁸. Der Exponent wird um 1 größer, also n = 8.",
    [B("7", "den Exponenten unverändert gelassen, obwohl der Vorfaktor 30 zu groß ist"),
     B("7 + 4", "den Faktor 4 zum Exponenten addiert"),
     B("7 * 4", "den Exponenten mit dem Faktor 4 malgenommen")]), lp=LP, idee="mal_rechnen_uebertrag")
# ───────── negativer_exponent ─────────
neu(T, "negativer_exponent", "test", "transfer", L(
    "Die Zahl 0,000 04 wird auf zwei Arten mit einer Zehnerpotenz geschrieben. Ergänze die Exponenten: 0,000 04 = 4 · 10^□ und 0,000 04 = 40 · 10^□.",
    "4 · 10^□ und 40 · 10^□", [-5, -6], ["0 - 5", "0 - 6"], ["-5", "0 - 5 - 1"],
    "Die 4 steht an der 5. Stelle hinter dem Komma, also ist 0,000 04 = 4 · 10⁻⁵. Wird der Vorfaktor zehnmal so groß (40 statt 4), muss die Zehnerpotenz zehnmal so klein werden, der Exponent also um 1 kleiner: 40 · 10⁻⁶. Probe: 40 · 0,000 001 = 0,000 04.",
    {0: [(5, "das Minus im Exponenten vergessen", "5"), (-4, "nur die Nullen hinter dem Komma gezählt", "0 - 4")],
     1: [(-5, "den Exponenten vom ersten Vorfaktor unverändert übernommen", "0 - 5"), (-4, "den Exponenten in die falsche Richtung um eins verändert", "0 - 4"), (-7, "den Exponenten um zwei statt um eins verkleinert", "0 - 7")]}), lp=LP, idee="vorfaktor_und_exponent")
neu(T, "negativer_exponent", "korrektur", "umkehr", Z(
    "Man startet bei 1 000 und teilt immer wieder durch zehn. Nach wie vielen Teilungen ist das Ergebnis zum ersten Mal kleiner als 0,000 001?",
    10, "3 + 7", "10",
    "1 000 = 10³. Jede Teilung durch 10 senkt den Exponenten um 1. 0,000 001 = 10⁻⁶. Nach 9 Teilungen ist das Ergebnis 10⁻⁶, also genau 0,000 001 und noch nicht kleiner. Nach 10 Teilungen ist es 10⁻⁷ und damit zum ersten Mal kleiner.",
    [B("9", "schon beim Erreichen des Wertes gestoppt, obwohl dieser nicht kleiner, sondern gleich ist"),
     B("6", "nur die Nullen der kleinen Zahl gezählt"),
     B("7", "den Exponenten des Ergebnisses statt der Teilungen genannt")], einheit="Teilungen"), form="umkehren", lp=LP, idee="teilungen_zaehlen")
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
    "Man nimmt ein Millionstel von einem Tausendstel. Wie viele Nullen stehen zwischen dem Komma und der 1, wenn man das Ergebnis als Dezimalzahl schreibt?",
    8, "6 + 3 - 1", "9 - 1",
    "Ein Millionstel ist 10⁻⁶, ein Tausendstel ist 10⁻³. Ein Millionstel von einem Tausendstel ist 10⁻⁶ · 10⁻³ = 10⁻⁹ = 0,000 000 001. Die 1 steht an der neunten Stelle, davor stehen 8 Nullen.",
    [B("9", "den Exponenten als Zahl der Nullen genommen"),
     B("5 + 2", "die Nullen der beiden Dezimalzahlen zusammengezählt"),
     B("6 * 3", "die Hochzahlen malgenommen statt addiert")], einheit="Nullen"), lp=LP, idee="zehnerpotenzen_verketten")
neu(T, "negativer_exponent", "sicherung", "darstellung", W(
    "Welche Gleichung ist wahr?",
    "0,0004 = 4 · 10⁻⁴",
    [("0,0004 = 4 · 10⁻³", "den Exponenten um eins zu klein gezählt: die Stelle der 4 hinter dem Komma falsch bestimmt"),
     ("0,0004 = 4 · 10⁻⁵", "den Exponenten um eins zu groß gezählt: ein Nullen-Platz zu viel"),
     ("0,0004 = 0,4 · 10⁻⁴", "den Vorfaktor verkleinert, ohne den Exponenten anzupassen")],
    "Die 4 steht an der 4. Stelle hinter dem Komma: 0,0004 = 4 · 10⁻⁴. Mit dem Vorfaktor 0,4 müsste der Exponent −3 sein (0,4 · 10⁻³ = 0,0004); 0,4 · 10⁻⁴ ist nur 0,00004.",
    lambda: abs(4e-4 - 0.0004) < 1e-15 and abs(4e-3 - 0.0004) > 1e-9 and abs(4e-5 - 0.0004) > 1e-9 and abs(0.4e-4 - 0.0004) > 1e-9), lp=LP, idee="gleichung_wahr")
neu(T, "negativer_exponent", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 10⁻³ bedeutet 1 : 10³, also 1 : 1 000. Zeile 2: Der Exponent ist negativ, also ist auch die Zahl 10⁻³ negativ, nämlich −0,001. Zeile 3: Also ist 10⁻³ · 1 000 = −0,001 · 1 000 = −1. In welcher Zeile steckt der erste Fehler? Wie viel ist 10⁻³ · 1 000 richtig?",
    "Fehler in Zeile □, richtig: 10⁻³ · 1 000 = □", [2, 1], ["2", "1 + 0"], ["1 + 1", "1000 / 1000"],
    "Zeile 1 stimmt: 10⁻³ = 1 : 1 000 = 0,001. In Zeile 2 steckt der Fehler: Das Minus im Exponenten macht die Zahl nicht negativ, sondern klein. 10⁻³ = 0,001 ist positiv. Zeile 3 folgt aus dem Fehler. Richtig: 10⁻³ · 1 000 = 0,001 · 1 000 = 1.",
    {0: [(1, "Zeile 1 genannt, obwohl dort die Bedeutung richtig angegeben ist", "1"), (3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(-1, "das Minus aus dem Exponenten mit in die Zahl genommen", "0 - 1"), (0, "die kleine Zahl mit dem Tausendfachen als null gerechnet", "0"), (-3, "den Exponenten als Ergebnis genommen", "0 - 3")]}), form="fehler_detektiv", lp=LP, idee="minus_macht_negativ")
# ───────── vorsilben_klein ─────────
neu(T, "vorsilben_klein", "test", "transfer", L(
    "Ein Bakterium ist 8 µm lang. Ein Modell davon ist 1 000-mal so lang und damit □ mm lang. Ein Molekül ist 0,5 nm lang. Ein Modell davon ist 10 000 000-mal so lang und damit □ mm lang. (1 nm = 10⁻⁹ m, 1 µm = 10⁻⁶ m, 1 mm = 10⁻³ m)",
    "Bakterienmodell: □ mm; Molekülmodell: □ mm", [8, 5], ["8 * 1000 / 1000", "5 * 10 ** 6 / 10 ** 6"], ["8", "5"],
    "Bakterium: 8 µm · 1 000 = 8 000 µm. Weil 1 mm = 1 000 µm ist, sind das 8 mm. Molekül: 0,5 nm · 10 000 000 = 5 000 000 nm. Weil 1 mm = 1 000 000 nm ist, sind das 5 mm. Erst vergrößern, dann die Einheit wechseln.",
    {0: [(8000, "nur mit dem Faktor malgenommen und die Einheit nicht gewechselt", "8 * 1000"), (8000000, "mit einer Million statt mit tausend malgenommen und die Einheit nicht gewechselt", "8 * 10 ** 6")],
     1: [(5000000, "nur mit dem Faktor malgenommen und die Einheit nicht gewechselt", "5 * 10 ** 6"), (5000, "die Nanometer wie Mikrometer in Millimeter umgerechnet", "5 * 10 ** 6 / 1000")]},
    ), lp=LP, idee="modell_vergroessern")
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
neu(T, "vorsilben_klein", "korrektur", "darstellung", Z(
    "Eine Mücke wiegt etwa 2 mg, ein Pollenkorn etwa 20 µg. Wie viele Pollenkörner wiegen zusammen so viel wie eine Mücke? (1 mg = 1 000 µg)",
    100, "2 * 1000 / 20", "2000 / 20",
    "2 mg = 2 000 µg. Ein Pollenkorn wiegt 20 µg. 2 000 : 20 = 100. Man muss beide Gewichte in derselben Einheit angeben, bevor man teilt. Probe: 100 · 20 µg = 2 000 µg = 2 mg.",
    [B("200 / 20", "die Mücke mit nur 200 µg gerechnet, die Einheit um eine Stufe zu klein umgerechnet"),
     B("2 * 1000", "nur die Mücke umgerechnet und nicht durch das Gewicht eines Korns geteilt"),
     B("2000 * 20", "malgenommen statt geteilt")], einheit="Pollenkörner"), form="bruecke", lp=LP, idee="verhaeltnis_einheiten")
neu(T, "vorsilben_klein", "sicherung", "fehler", L(
    "Ein Kind rechnet: Zeile 1: 1 nm = 10⁻⁹ m. Zeile 2: 1 µm = 10⁻⁶ m. Zeile 3: Also ist 10⁻⁶ : 10⁻⁹ = 10⁻³. Zeile 4: Also sind 1 µm gleich 10⁻³ nm. In welcher Zeile steckt der erste Fehler? Wie viele Nanometer sind 1 µm richtig?",
    "Fehler in Zeile □, richtig: 1 µm = □ nm", [3, 1000], ["3", "10 ** 3"], ["2 + 1", "1000"],
    "Zeile 1 und Zeile 2 sind richtig. In Zeile 3 ist die Rechnung falsch: 10⁻⁶ : 10⁻⁹ = 10⁻⁶ · 10⁹ = 10³, nicht 10⁻³. Also sind 1 µm gleich 10³ nm = 1000 nm. Zeile 4 folgt aus dem Fehler in Zeile 3.",
    {0: [(4, "die Schlusszeile genannt, weil dort der falsche Wert 10⁻³ steht", "4"), (1, "Zeile 1 genannt, obwohl dort die Vorsilbe richtig steht", "1")], 1: [(-3, "das falsche Ergebnis 10⁻³ als Zahl −3 genommen", "0 - 3"), (1, "die Vorsilben als Faktor 1 gelesen", "1"), (1000000, "mit 10⁶ gerechnet statt 10³", "10 ** 6")]}), form="fehler_detektiv", lp=LP, idee="fehler_kette")
neu(T, "vorsilben_klein", "sicherung", "darstellung", Z(
    "Eine Zelle ist 12 µm lang. Auf einer Zeichnung ist sie 5 000-mal vergrößert. Wie lang ist die Zeichnung in Zentimetern? (1 cm = 10 000 µm)",
    6, "12 * 5000 / 10000", "60000 / 10000",
    "12 µm · 5 000 = 60 000 µm. Weil 1 cm = 10 000 µm ist, sind das 60 000 : 10 000 = 6 cm. Probe: 6 cm = 60 000 µm, und 60 000 : 5 000 = 12 µm.",
    [B("60000", "nur mit dem Faktor malgenommen und die Einheit nicht gewechselt"),
     B("60", "in Millimeter statt in Zentimeter umgerechnet"),
     B("12 * 5000 / 100000", "die Einheit um eine Stufe zu groß gewählt")], einheit="cm"), lp=LP, idee="skalierung_zeichnung")
neu(T, "vorsilben_klein", "sicherung", "begruenden", W(
    "Ein Kind sagt: „Ein Mikrometer ist tausendmal kleiner als ein Millimeter, also muss die Maßzahl in Mikrometern tausendmal kleiner sein als in Millimetern.“ Welche Aussage stimmt?",
    "Das stimmt nicht: Die Maßzahl in Mikrometern ist tausendmal größer, denn man braucht tausendmal so viele der kleineren Einheiten.",
    [("Das stimmt: Die Maßzahl in Mikrometern ist tausendmal kleiner, denn kleinere Einheiten haben kleinere Maßzahlen.", "Größe der Einheit und Maßzahl gleichgesetzt; mit einer kleineren Einheit braucht man mehr davon"),
     ("Das stimmt nicht: Die Maßzahl bleibt gleich, denn die Länge ändert sich beim Umrechnen nicht.", "Länge und Maßzahl verwechselt; die Länge bleibt gleich, die Maßzahl ändert sich"),
     ("Das stimmt nicht: Die Maßzahl in Mikrometern ist hundertmal größer, denn ein Mikrometer ist hundertmal kleiner als ein Millimeter.", "den Faktor zwischen Milli und Mikro falsch angegeben; es ist ein Faktor tausend")],
    "1 mm = 1000 µm. Dieselbe Länge wird in der kleineren Einheit durch eine größere Maßzahl angegeben: 2 mm sind 2000 µm. Die Maßzahl wird tausendmal größer, nicht kleiner. Die Länge selbst bleibt gleich.",
    lambda: 2 * 1000 == 2000 and F(10) ** -3 / F(10) ** -6 == 1000), lp=LP, idee="maszahl_gegenlaeufig")
# ───────── vergleichen_pruefen ─────────
neu(T, "vergleichen_pruefen", "test", "transfer", L(
    "Gegeben sind drei Zahlen: A = 5 · 10⁻⁶, B = 0,2 · 10⁻⁴ und C = 30 · 10⁻⁷. Welche Zahl ist die kleinste, welche die größte? Trage jeweils die Nummer ein (1 = A, 2 = B, 3 = C).",
    "kleinste Zahl: □, größte Zahl: □", [3, 2], ["3", "1 + 1"], ["1 + 2", "2"],
    "Alle drei Zahlen mit dem Exponenten −7: A = 50 · 10⁻⁷, B = 0,2 · 10⁻⁴ = 200 · 10⁻⁷, C = 30 · 10⁻⁷. Die kleinste ist C (30), die größte ist B (200). Ausgeschrieben: A = 0,000 005, B = 0,000 02, C = 0,000 003.",
    {0: [(2, "nur die Vorfaktoren verglichen: 0,2 ist der kleinste Vorfaktor", "2"), (1, "A für die kleinste gehalten, weil der Exponent −6 der größte ist", "1")],
     1: [(3, "nur die Vorfaktoren verglichen: 30 ist der größte Vorfaktor", "3"), (1, "A für die größte gehalten, weil der Exponent −6 der größte ist", "1")]}), lp=LP, idee="normalisieren_ordnen")
neu(T, "vergleichen_pruefen", "korrektur", "darstellung", Z(
    "Wie viele der Zahlen 5 · 10⁵, 50 · 10⁴, 0,5 · 10⁶ und 5 000 000 · 10⁻² sind gleich 500 000?",
    3, "1 + 1 + 1", "3",
    "5 · 10⁵ = 500 000. 50 · 10⁴ = 500 000. 0,5 · 10⁶ = 500 000. Aber 5 000 000 · 10⁻² = 50 000, denn 10⁻² teilt durch 100. Es sind 3 Zahlen gleich 500 000.",
    [B("1 + 1 + 1 + 1", "auch die vierte Zahl mitgezählt, ohne durch 100 zu teilen"),
     B("1", "nur die wissenschaftliche Schreibweise gezählt"),
     B("1 + 1", "die Zahl mit dem Vorfaktor kleiner als 1 und die mit dem großen Vorfaktor nicht mitgezählt")], einheit="Zahlen"), lp=LP, idee="gleiche_zahl")
neu(T, "vergleichen_pruefen", "korrektur", "darstellung", W(
    "Probe A enthält 4 · 10⁻⁶ g Salz, Probe B enthält 2 · 10⁻⁵ g Salz. Welche Aussage stimmt?",
    "Probe B enthält fünfmal so viel wie Probe A, denn 2 · 10⁻⁵ = 20 · 10⁻⁶.",
    [("Probe A enthält mehr als Probe B, denn 4 ist größer als 2.", "nur die Vorfaktoren verglichen"),
     ("Probe B enthält zehnmal so viel wie Probe A, denn die Exponenten unterscheiden sich um eins.", "die Vorfaktoren nicht beachtet"),
     ("Beide Proben enthalten gleich viel, denn die beiden Angaben unterscheiden sich nur in der Schreibweise.", "die Angaben für verschiedene Schreibweisen derselben Menge gehalten")],
    "Man schreibt B mit demselben Exponenten wie A: 2 · 10⁻⁵ = 20 · 10⁻⁶. Dann steht bei B der Vorfaktor 20, bei A der Vorfaktor 4. 20 : 4 = 5, also hat B fünfmal so viel. Ausgeschrieben: 0,000 004 g gegen 0,000 02 g.",
    lambda: F(2) * F(10) ** -5 / (4 * F(10) ** -6) == 5 and F(4) * F(10) ** -6 < F(2) * F(10) ** -5), lp=LP, idee="verhaeltnis_potenzform")
neu(T, "vergleichen_pruefen", "korrektur", "umkehr", Z(
    "Für wie viele ganze Zahlen k liegt k · 10⁻⁵ zwischen 3 · 10⁻⁴ und 5 · 10⁻⁴? Die beiden Grenzen selbst zählen nicht mit.",
    19, "49 - 31 + 1", "(50 - 30) - 1",
    "3 · 10⁻⁴ = 30 · 10⁻⁵ und 5 · 10⁻⁴ = 50 · 10⁻⁵. Gesucht sind die ganzen Zahlen k mit 30 < k < 50, also k = 31 bis 49. Das sind 49 − 31 + 1 = 19 Zahlen.",
    [B("20", "eine der beiden Grenzen mitgezählt"),
     B("21", "beide Grenzen mitgezählt"),
     B("1", "die Exponenten nicht angeglichen und nur die Zahl zwischen den Vorfaktoren gezählt")], einheit="Zahlen"), form="umkehren", lp=LP, idee="raster_grenzen")
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
