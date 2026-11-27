T = "messen.koerper_berechnung"
# ───────── quader ─────────
a1(T, "quader", Z(
    "Für ein Kantenmodell aus Draht wird ein Würfel mit der Kantenlänge 7 cm gebaut. Jede Kante des Würfels ist ein Drahtstück. Wie viele Zentimeter Draht braucht man insgesamt?",
    84, "12 * 7", "4 * 7 + 4 * 7 + 4 * 7", "Wie viele Kanten hat ein Würfel? Alle Kanten sind gleich lang.",
    "Ein Würfel hat 12 Kanten, jede ist 7 cm lang. Draht: 12 · 7 = 84 cm.",
    [B("6 * 7", "die 6 Flächen statt der 12 Kanten gezählt"), B("8 * 7", "die 8 Ecken statt der 12 Kanten gezählt"), B("4 * 7", "nur die 4 Kanten einer Sorte gezählt")], "cm"))
a2(T, "quader", Z(
    "Aus einem 1,5 m langen Draht wird das Kantenmodell eines Quaders gebaut. Der Quader ist 12 cm lang, 8 cm breit und 5 cm hoch. Wie viele Zentimeter Draht bleiben übrig?",
    50, "150 - 4 * (12 + 8 + 5)", "150 - 100", "Wie viele Kanten gleicher Länge gibt es von jeder Sorte? Rechne zuerst in Zentimetern.",
    "Von jeder Sorte (Länge, Breite, Höhe) gibt es 4 Kanten. Draht für das Modell: 4 · (12 + 8 + 5) = 4 · 25 = 100 cm. 1,5 m = 150 cm. Es bleiben 150 − 100 = 50 cm übrig.",
    [B("4 * (12 + 8 + 5)", "den verbrauchten Draht statt des Rests angegeben"), B("150 - (12 + 8 + 5)", "von jeder Sorte nur eine Kante gezählt"), B("150 - 4 * (12 + 8)", "die vier Höhenkanten vergessen")], "cm"))
a3(T, "quader", Z(
    "Ein Quader ist 9 cm lang und 6 cm breit. Sein Volumen ist 270 cm³. Wie viele Zentimeter Draht braucht man für ein Kantenmodell dieses Quaders?",
    80, "4 * (9 + 6 + 270 / (9 * 6))", "4 * 20", "Berechne zuerst die fehlende Höhe aus dem Volumen. Danach zählst du alle 12 Kanten.",
    "Höhe: 270 : (9 · 6) = 270 : 54 = 5 cm. Von jeder Sorte gibt es 4 Kanten: 4 · (9 + 6 + 5) = 4 · 20 = 80 cm.",
    [B("9 + 6 + 270 / (9 * 6)", "nur 3 Kanten gezählt"), B("4 * (9 + 6)", "die Höhe vergessen"), B("270 / (9 * 6)", "nur die Höhe angegeben")], "cm"), g="verknuepfen")
# ───────── oberflaeche ─────────
a1(T, "oberflaeche", Z(
    "Ein Spielwürfel aus Holz mit der Kantenlänge 7 cm wird rundum lackiert. Wie groß ist die Fläche, die lackiert wird?",
    294, "6 * 7 * 7", "6 * 49", "Ein Würfel hat 6 gleich große Flächen. Wie groß ist eine Fläche?",
    "Eine Fläche ist ein Quadrat: 7 · 7 = 49 cm². Sechs Flächen: 6 · 49 = 294 cm².",
    [B("6 * 7", "die Kantenlänge statt der Fläche mit 6 malgenommen"), B("7 * 7", "nur eine Fläche angegeben"), B("4 * 7 * 7", "nur 4 Seitenflächen gezählt")], "cm²"))
a2(T, "oberflaeche", Z(
    "Ein Schrank ist ein Quader: 1,2 m breit, 0,5 m tief und 2 m hoch. Die Vorderseite, die beiden Seitenwände und die Decke werden gestrichen. Die Rückwand steht an der Wand, der Boden ist unten. Wie viele Quadratmeter werden gestrichen?",
    5, "1.2 * 2 + 2 * (0.5 * 2) + 1.2 * 0.5", "2.4 + 2 + 0.6", "Welche Flächen werden gestrichen? Berechne jede einzeln, auch die beiden gleichen Seitenwände.",
    "Vorderseite: 1,2 · 2 = 2,4 m². Zwei Seitenwände: 2 · (0,5 · 2) = 2 m². Decke: 1,2 · 0,5 = 0,6 m². Zusammen 2,4 + 2 + 0,6 = 5 m².",
    [B("2 * (1.2 * 2 + 0.5 * 2 + 1.2 * 0.5)", "alle 6 Flächen gezählt"), B("1.2 * 2 + 2 * (0.5 * 2)", "die Decke vergessen"), B("1.2 * 2 + 0.5 * 2 + 1.2 * 0.5", "nur eine Seitenwand gezählt")], "m²"))
a3(T, "oberflaeche", Z(
    "Ein Quader ist 6 cm lang und 4 cm breit. Seine Oberfläche ist 148 cm² groß. Wie hoch ist der Quader in Zentimetern?",
    5, "(148 / 2 - 6 * 4) / (6 + 4)", "(148 - 2 * 24) / (2 * (6 + 4))", "Die Oberfläche ist 2 · (l · b + l · h + b · h). Was bleibt übrig, wenn du die beiden Grundflächen abziehst?",
    "Boden und Deckel: 2 · 6 · 4 = 48 cm². Der Rest 148 − 48 = 100 cm² sind die vier Seitenflächen: 2 · 6 · h + 2 · 4 · h = 20h. Also 20h = 100 und h = 5 cm. Probe: 2 · (24 + 30 + 20) = 148.",
    [B("(148 - 6 * 4) / (2 * (6 + 4))", "nur eine Grundfläche abgezogen"), B("(148 - 2 * 6 * 4) / (6 + 4)", "den Mantel mit 1 · (l + b) statt 2 · (l + b) gerechnet"), B("148 / (2 * (6 + 4))", "die Grundflächen gar nicht abgezogen")], "cm"), g="rueckwaerts")
# ───────── sachaufgaben ─────────
a1(T, "sachaufgaben", Z(
    "Ein offenes Becken im Garten hat die Form eines Quaders: 12 m lang, 6 m breit und 1,5 m tief. Boden und die vier Wände werden mit Folie ausgekleidet. Wie viele Quadratmeter Folie werden gebraucht?",
    126, "12 * 6 + 2 * (12 * 1.5) + 2 * (6 * 1.5)", "72 + 36 + 18", "Das Becken hat oben keine Fläche. Berechne den Boden und die vier Wände, die Wände paarweise.",
    "Boden: 12 · 6 = 72 m². Zwei lange Wände: 2 · (12 · 1,5) = 36 m². Zwei kurze Wände: 2 · (6 · 1,5) = 18 m². Zusammen 72 + 36 + 18 = 126 m².",
    [B("2 * (12 * 6) + 2 * (12 * 1.5) + 2 * (6 * 1.5)", "oben eine Deckfläche mitgezählt"), B("12 * 6", "nur den Boden gerechnet"), B("2 * 12 * 1.5 + 2 * 6 * 1.5", "den Boden vergessen")], "m²"))
a2(T, "sachaufgaben", Z(
    "Ein Zimmer ist 6 m lang, 4 m breit und 2,5 m hoch. Die vier Wände werden gestrichen. Die Tür (2 m²) und das Fenster (3 m²) werden nicht gestrichen. Ein Eimer Farbe reicht für 12 m². Wie viele Eimer muss man mindestens kaufen?",
    4, "(2 * (6 * 2.5) + 2 * (4 * 2.5) - 2 - 3 + 11) // 12", "4", "Berechne die Fläche der vier Wände und ziehe Tür und Fenster ab. Teile durch 12 und überlege, wie viele ganze Eimer nötig sind.",
    "Wände: 2 · (6 · 2,5) + 2 · (4 · 2,5) = 30 + 20 = 50 m². Ohne Tür und Fenster: 50 − 5 = 45 m². 45 : 12 = 3,75. Man braucht ganze Eimer, also 4 Eimer.",
    [B("(2 * (6 * 2.5) + 2 * (4 * 2.5) - 2 - 3) / 12", "das Ergebnis 3,75 nicht aufgerundet"), B("2 * (6 * 2.5) + 2 * (4 * 2.5) - 2 - 3", "die Fläche 45 m² statt der Eimerzahl angegeben"), B("(2 * (6 * 2.5) + 2 * (4 * 2.5) + 6 * 4 - 2 - 3) / 12", "die Decke mitgestrichen")], "Eimer"))
a3(T, "sachaufgaben", Z(
    "Ein Regal ist ein Quader: 1,5 m breit, 0,6 m tief und 2 m hoch. Es hat keine Vorderseite. Rückwand: eine dünne Platte, 4 € je m². Boden, Decke und die beiden Seitenwände: Holz, 12 € je m². Wie viel Euro kosten alle Platten zusammen?",
    62.4, "(2 * (1.5 * 0.6) + 2 * (0.6 * 2)) * 12 + 1.5 * 2 * 4", "4.2 * 12 + 3 * 4", "Teile die Flächen nach dem Preis. Welche Flächen sind Holz, welche ist die dünne Platte?",
    "Holz: Boden und Decke 2 · 1,5 · 0,6 = 1,8 m², zwei Seitenwände 2 · 0,6 · 2 = 2,4 m², zusammen 4,2 m². Preis: 4,2 · 12 = 50,4 €. Rückwand: 1,5 · 2 = 3 m², Preis: 3 · 4 = 12 €. Zusammen 50,4 + 12 = 62,4 €.",
    [B("(2 * (1.5 * 0.6) + 2 * (0.6 * 2)) * 12", "die Rückwand vergessen"), B("(2 * (1.5 * 0.6) + 2 * (0.6 * 2) + 1.5 * 2) * 12", "die Rückwand zum Holzpreis gerechnet"), B("(2 * (1.5 * 0.6) + 2 * (0.6 * 2) + 2 * (1.5 * 2)) * 12", "Vorderseite und Rückwand zum Holzpreis gerechnet")], "€"), g="verknuepfen")
# ───────── zusammengesetzt ─────────
a1(T, "zusammengesetzt", Z(
    "Ein Holzwürfel hat 6 cm Kantenlänge. Von oben nach unten wird ein quadratisches Loch mit 2 cm Seitenlänge ganz durchgebohrt. Wie groß ist die Oberfläche des durchbohrten Würfels, mit den Wänden im Loch?",
    256, "6 * 6 * 6 - 2 * (2 * 2) + 4 * (2 * 6)", "208 + 48", "Berechne die Oberfläche des Würfels. Zwei Öffnungen fallen weg, dafür kommen die Wände im Loch dazu.",
    "Würfel: 6 · 36 = 216 cm². Die zwei Öffnungen (je 2 · 2 = 4 cm²) fallen weg: 216 − 8 = 208 cm². Das Loch hat 4 Wände, jede 2 · 6 = 12 cm²: 48 cm². Zusammen 208 + 48 = 256 cm².",
    [B("6 * 6 * 6", "das Loch nicht beachtet"), B("6 * 6 * 6 - 2 * (2 * 2)", "die Wände im Loch vergessen"), B("6 * 6 * 6 + 4 * (2 * 6)", "die Öffnungen nicht abgezogen")], "cm²"))
a2(T, "zusammengesetzt", Z(
    "Auf einen Quader (6 cm lang, 4 cm breit, 3 cm hoch) wird ein Würfel mit 2 cm Kantenlänge geklebt. Der Würfel liegt mit seiner ganzen Unterseite auf der oberen Fläche des Quaders. Wie groß ist die Oberfläche des neuen Körpers?",
    124, "2 * (6 * 4 + 6 * 3 + 4 * 3) + 6 * 2 * 2 - 2 * (2 * 2)", "108 + 24 - 8", "Berechne beide Oberflächen einzeln. Wie groß ist die Fläche, an der beide Körper sich berühren?",
    "Quader: 2 · (24 + 18 + 12) = 108 cm². Würfel: 6 · 4 = 24 cm². Berührfläche: 2 · 2 = 4 cm². Sie fällt beim Quader und beim Würfel weg: 108 + 24 − 2 · 4 = 124 cm².",
    [B("2 * (6 * 4 + 6 * 3 + 4 * 3) + 6 * 2 * 2", "die Berührfläche nicht abgezogen"), B("2 * (6 * 4 + 6 * 3 + 4 * 3) + 6 * 2 * 2 - 2 * 2", "die Berührfläche nur einmal abgezogen"), B("2 * (6 * 4 + 6 * 3 + 4 * 3) - 2 * 2", "den Würfel nicht dazugezählt, aber die Berührfläche vom Quader abgezogen")], "cm²"))
a3(T, "zusammengesetzt", Z(
    "Aus einem Quader (5 cm lang, 4 cm breit, 3 cm hoch) wird an einer Ecke ein Würfel mit 2 cm Kantenlänge herausgesägt. Wie viele Quadratzentimeter ist die Oberfläche des Körpers nach dem Heraussägen größer als vorher? Gib den Unterschied an.",
    0, "3 * 2 * 2 - 3 * 2 * 2", "0", "Welche Flächen gehen an der Ecke verloren? Welche neuen Flächen entstehen im Ausschnitt? Vergleiche ihre Größen.",
    "An der Ecke verschwinden 3 Quadrate des Quaders (je 2 · 2 = 4 cm²), zusammen 12 cm². Im Ausschnitt entstehen 3 neue Quadrate (je 4 cm²), zusammen 12 cm². Die Oberfläche bleibt gleich: 12 − 12 = 0 cm² mehr. Das gilt, solange der Würfel an einer Ecke herausgeschnitten wird.",
    [B("3 * 2 * 2", "nur die neuen Flächen gezählt, die alten nicht abgezogen"), B("6 * 2 * 2", "sechs neue Flächen gezählt"), B("2 * 2", "nur eine neue Fläche gezählt")], "cm²"), g="begruenden")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Kim sagt: „Wenn man bei einem Würfel die Kante verdoppelt, wird auch die Oberfläche doppelt so groß.“ Ein Würfel hat die Kantenlänge 3 cm. Die Kante wird auf 6 cm verdoppelt. Wie groß ist die neue Oberfläche in cm²?",
    216, "6 * 6 * 6", "54 * 4", "Berechne die neue Oberfläche direkt mit der neuen Kante. Vergleiche mit der alten Oberfläche.",
    "Neue Oberfläche: 6 · 6 · 6 = 216 cm². Alte Oberfläche: 6 · 3 · 3 = 54 cm². 216 : 54 = 4. Die Oberfläche wird 4-mal so groß, nicht 2-mal. Kims Aussage stimmt nicht.",
    [B("2 * 6 * 3 * 3", "die alte Oberfläche verdoppelt (Kims Annahme)"), B("8 * 6 * 3 * 3", "mit dem Faktor 8 für das Volumen gerechnet"), B("6 * 6", "nur eine Fläche des neuen Würfels")], "cm²"))
a2(T, "verstehen", Z(
    "Ein Quader ist 4 cm lang, 3 cm breit und 2 cm hoch. Die Höhe wird auf 4 cm verdoppelt, Länge und Breite bleiben gleich. Um wie viele Quadratzentimeter wird die Oberfläche größer?",
    28, "2 * (4 * 3 + 4 * 4 + 3 * 4) - 2 * (4 * 3 + 4 * 2 + 3 * 2)", "80 - 52", "Berechne die Oberfläche vorher und nachher. Bilde dann die Differenz.",
    "Vorher: 2 · (12 + 8 + 6) = 52 cm². Nachher: 2 · (12 + 16 + 12) = 80 cm². Unterschied: 80 − 52 = 28 cm². Die Oberfläche wird nicht doppelt so groß.",
    [B("2 * (4 * 3 + 4 * 4 + 3 * 4)", "die neue Oberfläche statt des Unterschieds angegeben"), B("2 * (4 * 3 + 4 * 2 + 3 * 2)", "die alte Oberfläche angegeben: so viel, als wäre sie verdoppelt"), B("4 * 3 * 4 - 4 * 3 * 2", "den Zuwachs des Volumens statt der Oberfläche angegeben")], "cm²"))
a3(T, "verstehen", Z(
    "Zwei Quader haben beide das Volumen 120 cm³. Quader A ist 10 cm lang, 4 cm breit und 3 cm hoch. Quader B ist 6 cm lang, 5 cm breit und 4 cm hoch. Um wie viele Quadratzentimeter ist die Oberfläche von A größer als die von B?",
    16, "2 * (10 * 4 + 10 * 3 + 4 * 3) - 2 * (6 * 5 + 6 * 4 + 5 * 4)", "164 - 148", "Gleiches Volumen bedeutet nicht gleiche Oberfläche. Berechne beide Oberflächen einzeln.",
    "A: 2 · (40 + 30 + 12) = 164 cm². B: 2 · (30 + 24 + 20) = 148 cm². Unterschied: 164 − 148 = 16 cm². Beide Volumina sind gleich (10 · 4 · 3 = 120 = 6 · 5 · 4), aber der gedrungenere Quader B hat die kleinere Oberfläche.",
    [B("2 * (10 * 4 + 10 * 3 + 4 * 3)", "nur die Oberfläche von A angegeben"), B("2 * (6 * 5 + 6 * 4 + 5 * 4)", "nur die Oberfläche von B angegeben"), B("120 - 120", "wegen des gleichen Volumens einen Unterschied von 0 angenommen")], "cm²"), g="pruefung")
