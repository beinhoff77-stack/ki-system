T = "abbildungen.kongruenz"
D = "id.geometrie.deckungsgleich"
AB = "id.geometrie.abstand"
WI = "id.geometrie.winkel"
# ───────── achsenspiegelung ─────────
neu(T, "achsenspiegelung", "lueckenweg", L(
    "Der Punkt P(2 | 5) wird an der senkrechten Geraden x = 6 gespiegelt. P hat von dieser Geraden den Abstand ①. Der Bildpunkt P' liegt auf der anderen Seite im selben Abstand. Seine x-Koordinate ist ②. Die Strecke PP' ist ③ Einheiten lang.",
    "① = □; ② = □; ③ = □", [4, 10, 8], ["6 - 2", "6 + {1}", "2 * {1}"], ["4", "10", "10 - 2"],
    "Spiegeln heißt: gleich weit auf die andere Seite der Achse. Die y-Koordinate bleibt bei einer senkrechten Achse gleich.",
    "Abstand von P zur Achse: 6 − 2 = 4. P' liegt 4 Einheiten rechts der Achse: x = 6 + 4 = 10, also P'(10 | 5). Die Strecke PP' ist 10 − 2 = 8 Einheiten lang, doppelt so lang wie der Abstand zur Achse.",
    {0: [(8, None, "die x-Koordinate von P zur Lage der Achse addiert", "6 + 2")], 1: [(2, "fb.deckungsgleich.an_koordinatenachse_gespiegelt", "den Bildpunkt wieder auf die Seite von P gelegt", "6 - {1}")], 2: [(4, None, "nur den Abstand von P zur Achse als Länge genommen", "{1}")]}), g="direkt", regel=D)
neu(T, "achsenspiegelung", "anwenden", Z(
    "Auf einem Stadtplan verläuft ein gerader Kanal senkrecht entlang der Geraden x = 1. Ein Café liegt im Punkt A(5 | −2). Ein Zwillingscafé B soll genau gegenüber auf der anderen Kanalseite liegen, als Spiegelbild von A am Kanal. Welche x-Koordinate hat B?",
    -3, "2 * 1 - 5", "1 - (5 - 1)", "Wie weit ist A vom Kanal entfernt? B liegt im gleichen Abstand auf der anderen Seite.",
    "A hat vom Kanal den Abstand 5 − 1 = 4. B liegt 4 Einheiten links vom Kanal: x = 1 − 4 = −3. Die y-Koordinate bleibt −2. B(−3 | −2).",
    [B("-5", "an der y-Achse gespiegelt statt am Kanal", "fb.deckungsgleich.an_koordinatenachse_gespiegelt"), B("1 + 5", "die x-Koordinate von A zum Wert der Achse addiert"), B("3", "den Abstand falsch herum abgetragen und das Vorzeichen vertauscht")]), g="einkleidung", regel=D)
neu(T, "achsenspiegelung", "fehler_detektiv", FD(
    "Das Dreieck mit A(2 | 1), B(5 | 1) und C(2 | 4) wird an der y-Achse gespiegelt. Kim schreibt auf:",
    [("Bei einer Spiegelung an der y-Achse wechselt die x-Koordinate das Vorzeichen, die y-Koordinate bleibt.", True, True),
     ("Also wird A zu A'(−2 | 1), B zu B'(−5 | 1) und C zu C'(−2 | −4).", False, True),
     ("Die Strecke [A'C'] ist dann 5 Einheiten lang, die Strecke [AC] war nur 3 Einheiten lang.", True, True)],
    "Vergleiche die Koordinaten der Bildpunkte mit der Regel aus Zeile 1. Bleibt bei einer Spiegelung die Länge einer Strecke gleich?",
    "Nach der Regel in Zeile 1 bleibt die y-Koordinate gleich, daher ist C'(−2 | 4) richtig und nicht C'(−2 | −4). Der Fehler steckt in Zeile 2. Zeile 3 rechnet mit dem falschen C' richtig weiter. Der Widerspruch (5 und 3 Einheiten) zeigt, dass etwas nicht stimmt, denn eine Spiegelung erhält Längen."), g="fehler", regel=D)
# ───────── mittelsenkrechte ─────────
neu(T, "mittelsenkrechte", "anwenden", Z(
    "Zwei Bergstationen liegen im Koordinatensystem bei A(−6 | 2) und B(12 | 2). Ein Wanderweg soll überall gleich weit von A und B entfernt sein und verläuft senkrecht (parallel zur y-Achse). Er liegt auf der Geraden x = k. Wie groß ist k?",
    3, "(-6 + 12) / 2", "-6 + (12 - (-6)) / 2", "Der Weg liegt auf der Mittelsenkrechten von AB. Sie geht durch die Mitte der Strecke.",
    "Die Mittelsenkrechte von AB geht durch den Mittelpunkt von [AB]. Die x-Koordinate der Mitte ist (−6 + 12) : 2 = 3. Der Weg liegt auf der Geraden x = 3.",
    [B("(12 - (-6)) / 2", "die halbe Länge der Strecke statt die Lage der Mitte genommen", "fb.abstand.halbe_laenge_statt_mitte"), B("12 - (-6)", "die ganze Länge der Strecke genommen"), B("-6 + 12", "die beiden x-Koordinaten nicht halbiert")]), g="einkleidung", regel=AB)
neu(T, "mittelsenkrechte", "umkehren", Z(
    "Im Dreieck ABC liegt der Punkt C auf der Mittelsenkrechten der Seite [AB]. Es gilt AB = 12 cm. Der Umfang des Dreiecks beträgt 30 cm. Wie lang ist die Seite [AC]?",
    9, "(30 - 12) / 2", 9, "Jeder Punkt auf der Mittelsenkrechten ist von A und B gleich weit entfernt. Was folgt für AC und BC?",
    "C liegt auf der Mittelsenkrechten, also gilt AC = BC. Der Umfang ist AB + AC + BC = 30. Mit AB = 12 bleiben für AC und BC zusammen 18 cm, also AC = 9 cm.",
    [B("30 - 12", "AC und BC zusammen als Länge von AC genommen"), B("12 / 2", "die halbe Länge von AB genommen"), B("30 / 2", "den halben Umfang genommen")], einheit="cm"), g="rueckwaerts", regel=AB)
# ───────── winkelhalbierende ─────────
neu(T, "winkelhalbierende", "anwenden", Z(
    "Im Dreieck ABC gilt α = 68° und β = 52°. Die Winkelhalbierende von γ teilt den Winkel γ in zwei gleich große Teile. Wie groß ist der Winkel zwischen dieser Winkelhalbierenden und der Seite [AC]?",
    30, "(180 - 68 - 52) / 2", "(180 - 120) / 2", "Berechne zuerst γ mit der Winkelsumme im Dreieck. Halbiere dann.",
    "γ = 180° − 68° − 52° = 60°. Die Winkelhalbierende teilt γ in zwei Teile zu je 30°. Der gesuchte Winkel ist 30°.",
    [B("180 - 68 - 52", "den Winkel γ selbst angegeben, ohne zu halbieren"), B("68 / 2", "den Winkel α halbiert"), B("(180 - 68 - 52) / 4", "zweimal halbiert")], einheit="°"), g="mehrschritt", regel=WI,
    zweifel="Winkelsumme im Dreieck trägt die Rechnung (id.geometrie.winkel, Ausnahme der Themenliste); die Lernkarte nennt id.geometrie.abstand")
neu(T, "winkelhalbierende", "verfahren_waehlen", W(
    "Ein Café soll von zwei sich kreuzenden Straßen gleich weit entfernt sein und außerdem von den Bushaltestellen H1 und H2 gleich weit entfernt. Wie findest du alle möglichen Orte?",
    "Schneide die Mittelsenkrechte von [H1H2] mit jeder der beiden Winkelhalbierenden der Straßen und sammle alle Treffer",
    [("Schnitt aus der Mittelsenkrechten der beiden Straßen und der Winkelhalbierenden von [H1H2]", "die beiden Linien vertauscht"), ("Schnitt zweier Winkelhalbierender", "Haltestellen sind Punkte, bei ihnen hilft keine Winkelhalbierende"), ("Schnitt zweier Mittelsenkrechter", "Straßen sind Geraden, bei ihnen hilft keine Mittelsenkrechte")],
    "Gleich weit von zwei Geraden entfernt und gleich weit von zwei Punkten entfernt sind zwei verschiedene Bedingungen. Welche Linie gehört zu welcher?",
    "Gleicher Abstand zu zwei sich kreuzenden Geraden: eine der beiden Winkelhalbierenden der Geraden (es gibt zwei, senkrecht zueinander). Gleicher Abstand zu zwei Punkten: Mittelsenkrechte der Strecke zwischen den Punkten. Der gesuchte Ort liegt auf der Mittelsenkrechten und auf einer der beiden Winkelhalbierenden, also in den Treffern beider Schnitte. Sonderfälle: Ist die Mittelsenkrechte parallel zu einer Winkelhalbierenden, gibt es dort keinen Treffer; fällt sie mit einer zusammen (zum Beispiel Straßen x- und y-Achse, Haltestellen (1|0) und (0|1)), erfüllen alle Punkte dieser Geraden die Bedingung.",
    lambda: True), g="verknuepfen", regel=AB)
# ───────── symmetrie ─────────
neu(T, "symmetrie", "lueckenweg", L(
    "Ein regelmäßiges Sechseck hat ① Symmetrieachsen. Ein regelmäßiges Zwölfeck hat ② Symmetrieachsen. ③ ist die Summe der beiden Achsenzahlen der einzelnen Figuren (nicht die Achsen einer zusammengesetzten Figur).",
    "① = □; ② = □; ③ = □", [6, 12, 18], ["6", "12", "{1} + {2}"], ["6", "12", "6 + 12"],
    "Ein regelmäßiges n-Eck hat n Symmetrieachsen. Bei geradem n gehen sie durch gegenüberliegende Ecken oder durch gegenüberliegende Seitenmitten. Addiere für die letzte Lücke die Anzahlen der beiden einzelnen Figuren.",
    "Ein regelmäßiges n-Eck hat n Symmetrieachsen. Sechseck: 6, Zwölfeck: 12, zusammen 6 + 12 = 18.",
    {0: [(3, None, "nur die Achsen durch gegenüberliegende Ecken gezählt", "3")], 1: [(6, None, "nur die Achsen durch gegenüberliegende Ecken gezählt", "6")], 2: [(72, None, "die beiden Achsenzahlen malgenommen statt addiert", "{1} * {2}")]}, ), g="direkt", regel=D)
neu(T, "symmetrie", "anwenden", Z(
    "Auf Reisen siehst du drei Verkehrsschilder: ein Vorfahrt-gewähren-Schild (gleichseitiges Dreieck), ein Stoppschild (regelmäßiges Achteck) und ein Vorfahrtstraßen-Schild (Quadrat, auf der Spitze stehend). Wie viele Symmetrieachsen haben die drei Schilder zusammen? Bunte Zeichen und Schrift bleiben unbeachtet, nur die Umrissform zählt.",
    15, "3 + 8 + 4", 15, "Zähle für jede Umrissform die Achsen. Ein regelmäßiges Vieleck mit n Ecken hat n Achsen.",
    "Gleichseitiges Dreieck: 3 Achsen. Regelmäßiges Achteck: 8 Achsen. Quadrat: 4 Achsen (zwei Mittellinien und zwei Diagonalen). Zusammen 3 + 8 + 4 = 15 Achsen.",
    [B("3 + 4 + 4", "beim Achteck nur die Hälfte der Achsen gezählt"), B("3 + 8 + 2", "beim Quadrat die Diagonalen nicht gezählt"), B("3 + 8 + 4 + 4", "die Achsen des Quadrats doppelt gezählt")], einheit="Achsen"), g="mehrschritt", regel=D)
neu(T, "symmetrie", "fehler_detektiv", FD(
    "Alex untersucht ein Rechteck, das kein Quadrat ist, und schreibt auf:",
    [("Ein Rechteck hat zwei Paare gleich langer Seiten.", True, True),
     ("Die beiden Diagonalen sind gleich lang, also sind sie auch Symmetrieachsen.", False, True),
     ("Zusammen mit den zwei Mittellinien hat das Rechteck 4 Symmetrieachsen.", False, True)],
    "Falte ein Rechteck gedanklich entlang einer Diagonalen. Passen die beiden Hälften genau aufeinander?",
    "Faltet man ein Rechteck (das kein Quadrat ist) an einer Diagonalen, passen die Hälften nicht aufeinander. Nur die beiden Mittellinien sind Symmetrieachsen, also hat es 2 Achsen. Der Fehler steckt in Zeile 2. Zeile 3 rechnet mit der falschen Aussage weiter."), g="fehler", regel=D)
# ───────── vierecke_ordnen ─────────
neu(T, "vierecke_ordnen", "bruecke", W(
    "Ein Viereck hat vier gleich lange Seiten. Seine Diagonalen stehen senkrecht aufeinander und halbieren sich. Die Diagonalen sind aber verschieden lang. Welches Viereck ist es?",
    "eine Raute, die kein Quadrat ist", [("ein Rechteck", "ein Rechteck hat gleich lange Diagonalen"), ("ein Drachen, der keine Raute ist", "ein Drachen hat zwei verschieden lange Seitenpaare und die Diagonalen halbieren sich nicht beide"), ("ein Quadrat", "ein Quadrat hat gleich lange Diagonalen")],
    "Gehe im Haus der Vierecke nach den Eigenschaften vor: Vier gleich lange Seiten, senkrechte Diagonalen, verschieden lange Diagonalen.",
    "Vier gleich lange Seiten und sich halbierende, senkrechte Diagonalen passen zur Raute. Gleich lange Diagonalen hätte nur das Quadrat. Da sie verschieden lang sind, ist es eine Raute, die kein Quadrat ist.",
    lambda: True), g="darstellung", regel=D)
zaehl = sum(1 for achsen in {"Quadrat": 4, "Rechteck": 2, "Raute": 2, "Parallelogramm": 0, "Drachen": 1, "gleichschenkliges Trapez": 1}.values() if achsen >= 1)
neu(T, "vierecke_ordnen", "anwenden", Z(
    "Bei einem Puzzle-Spiel liegen sechs Vierecke bereit: Quadrat, Rechteck, Raute, Parallelogramm (ein allgemeines Parallelogramm, das weder Rechteck noch Raute ist), Drachen und gleichschenkliges Trapez. Kim soll alle heraussuchen, die mindestens eine Symmetrieachse haben. Wie viele sind das?",
    5, "5", zaehl, "Prüfe jedes Viereck einzeln: Gibt es eine Gerade, an der man die Figur falten kann, sodass beide Hälften genau aufeinanderliegen?",
    "Quadrat, Rechteck, Raute, Drachen und gleichschenkliges Trapez haben mindestens eine Symmetrieachse. Das Parallelogramm (ohne rechten Winkel und ohne gleich lange Nachbarseiten) hat keine, nur eine Punktsymmetrie. Es sind 5 Vierecke.",
    [B("6", "das Parallelogramm mitgezählt, weil die Diagonalen als Achsen gelten", "fb.deckungsgleich.diagonale_als_achse"), B("4", "das gleichschenklige Trapez nicht gezählt"), B("3", "nur Quadrat, Rechteck und Raute gezählt")], einheit="Vierecke"), g="pruefung", regel=D)
# ───────── eigenschaften ─────────
neu(T, "eigenschaften", "anwenden", Z(
    "Kim zeichnet ein Dreieck ABC mit α = 52° und β = 71°. Sie spiegelt es an einer Geraden und verschiebt das Bild danach um einige Einheiten. Wie groß ist der Winkel γ' im Bilddreieck A'B'C'?",
    57, "180 - 52 - 71", "180 - (52 + 71)", "Welche Größen ändern sich bei Spiegeln und Verschieben, und welche bleiben gleich? Berechne γ aus der Winkelsumme.",
    "Spiegeln und Verschieben erhalten alle Winkel. Also ist γ' = γ = 180° − 52° − 71° = 57°.",
    [B("180 - 52", "nur einen Winkel von 180° abgezogen"), B("71", "den Winkel β übernommen"), B("360 - 52 - 71", "vom Vollwinkel 360° statt von 180° gerechnet")], einheit="°"), g="mehrschritt", regel=WI,
    zweifel="Winkelsumme im Dreieck plus Erhaltung der Winkel; Ausnahme der Themenliste (id.geometrie.winkel), die Lernkarte nennt id.geometrie.deckungsgleich")
neu(T, "eigenschaften", "fehler_detektiv", FD(
    "Ein Dreieck ABC ist gegen den Uhrzeigersinn beschriftet. Es wird einmal gespiegelt, dann noch einmal an einer anderen Achse gespiegelt und schließlich verschoben. Kim schreibt auf:",
    [("Eine Verschiebung ändert den Umlaufsinn nicht.", True, True),
     ("Die erste Spiegelung kehrt den Umlaufsinn um: A'B'C' ist im Uhrzeigersinn beschriftet.", True, True),
     ("Die zweite Spiegelung kehrt ihn noch einmal um: A''B''C'' ist wieder gegen den Uhrzeigersinn beschriftet.", True, True),
     ("Also ist das Endbild nach dem Verschieben im Uhrzeigersinn beschriftet.", False, False)],
    "Zähle, wie oft der Umlaufsinn insgesamt umgekehrt wird. Gerade oder ungerade Zahl?",
    "Zwei Spiegelungen kehren den Umlaufsinn zweimal um, das Verschieben ändert nichts. Das Endbild ist wieder gegen den Uhrzeigersinn beschriftet. Die Zeilen 1 bis 3 sind richtig. Der Fehler steckt in Zeile 4: Sie passt nicht zu Zeile 3.",
    rueck=None), g="fehler", regel=D)
