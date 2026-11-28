T = "trigo.rechtwinklig"
RW = "id.geometrie.rechtwinklig"
ZW = "Sinus, Kosinus, Tangens: die einzige Regel der Einheit im Katalog (rechtwinkliges Dreieck, Lage der Seiten) trägt nur das Zuordnen der Seiten, das Rechnen mit dem Verhältnis nicht"
OHNE_B = "Beziehungen zwischen Sinus, Kosinus und Tangens: keine Regel des Katalogs trägt den Lösungsweg"
OHNE_S = "Steigung und Winkel einer Geraden (Tangens als Steigung): keine Regel des Katalogs trägt den Lösungsweg"
# ───────── seiten ─────────
neu(T, "seiten", "verfahren_waehlen", W(
    "Im Dreieck ABC liegt der rechte Winkel bei C. Welche Seite ist die Gegenkathete des Winkels α bei A?",
    "a (die Seite BC)", [("b (die Seite AC)", "b liegt am Winkel α an, ist also die Ankathete"), ("c (die Seite AB)", "c liegt dem rechten Winkel gegenüber, ist also die Hypotenuse")],
    "Die Gegenkathete liegt dem Winkel gegenüber, ohne ihn zu berühren.",
    "Bei A liegt der Winkel α. Gegenüber von A liegt die Seite a = BC. Sie berührt A nicht und ist keine Hypotenuse. Also ist a die Gegenkathete von α.",
    lambda: True), g="erkennen", regel=RW)
neu(T, "seiten", "verfahren_waehlen", W(
    "Im Dreieck ABC liegt der rechte Winkel bei C. Welche Seite ist zugleich Gegenkathete von β (bei B) und Ankathete von α (bei A)?",
    "b (die Seite AC)", [("a (die Seite BC)", "a ist die Gegenkathete von α und die Ankathete von β, also genau umgekehrt"), ("c (die Seite AB)", "c ist die Hypotenuse, die weder Gegenkathete noch Ankathete ist")],
    "Zeichne das Dreieck. Welche Seite liegt gegenüber von B? Berührt diese Seite A?",
    "Gegenüber von B liegt die Seite b = AC. Sie berührt A, ist also Ankathete von α. Damit ist b Gegenkathete von β und Ankathete von α.",
    lambda: True), g="mehrschritt", regel=RW)
# ───────── verhaeltnisse ─────────
neu(T, "verhaeltnisse", "lueckenweg", L(
    "In einem rechtwinkligen Dreieck ist die Hypotenuse 35 cm lang, es gilt sin α = 0,6 und cos α = 0,8. Die Gegenkathete von α ist ① cm lang. Die Ankathete von α ist ② cm lang. Der Umfang des Dreiecks ist ③ cm.",
    "① = □; ② = □; ③ = □", [21, 28, 84], ["21", "28", "35 + {1} + {2}"], ["0.6 * 35", "0.8 * 35", "35 + 0.6 * 35 + 0.8 * 35"],
    "Der Sinus ist Gegenkathete durch Hypotenuse, der Kosinus ist Ankathete durch Hypotenuse. Stelle um.",
    "Gegenkathete = sin α · Hypotenuse = 0,6 · 35 = 21. Ankathete = cos α · Hypotenuse = 0,8 · 35 = 28. Umfang: 35 + 21 + 28 = 84. Probe: 21² + 28² = 441 + 784 = 1225 = 35².",
    {0: [(28, None, "mit dem Kosinus statt mit dem Sinus gerechnet", "0.8 * 35")], 1: [(21, None, "mit dem Sinus statt mit dem Kosinus gerechnet", "0.6 * 35")], 2: [(49, None, "die Hypotenuse im Umfang vergessen", "{1} + {2}")]}), regel=RW, zweifel=ZW)
neu(T, "verhaeltnisse", "anwenden", Z(
    "Ein Hang bildet mit der Waagerechten einen Winkel α mit tan α = 0,75. Die Strecke waagerecht gemessen ist 32 m lang. Wie hoch liegt der Hangpunkt über dem Ausgangspunkt?",
    24, "24", "0.75 * 32", "Der Tangens ist Gegenkathete durch Ankathete. Welche Seite ist die Waagerechte, welche die Höhe?",
    "tan α = Gegenkathete : Ankathete. Die Höhe ist die Gegenkathete: 0,75 · 32 = 24 m.",
    [BR("32 / 0.75", "durch den Tangens geteilt statt mit ihm malgenommen", None, 1), B("32 - 0.75", "den Tangenswert von der Länge abgezogen"), B("32 + 0.75", "den Tangenswert zur Länge addiert")], einheit="m"), g="einkleidung", regel=RW, zweifel=ZW)
# ───────── seite ─────────
w1, c1 = rd("1.5 * tan(28)", 2)
neu(T, "seite", "anwenden", Z(
    "Eine Seilbahn steigt unter einem Winkel von 28° zur Waagerechten an. Waagerecht gemessen legt sie 1,5 km zurück. Welchen Höhenunterschied überwindet sie? Runde auf zwei Dezimalstellen.",
    w1, c1, "round(1.5 * tan(28), 2)", "Die waagerechte Strecke ist die Ankathete des Winkels, der Höhenunterschied die Gegenkathete. Welches Verhältnis verbindet beide?",
    "tan 28° = Höhe : 1,5 km, also Höhe = 1,5 · tan 28° ≈ 1,5 · 0,5317 ≈ 0,80 km.",
    [BR("1.5 / tan(28)", "durch den Tangens geteilt statt malgenommen", None, 2), BR("1.5 * sin(28)", "den Sinus statt den Tangens genommen", None, 2), BR("1.5 * cos(28)", "den Kosinus statt den Tangens genommen", None, 2)], einheit="km", toleranz=0.01), g="einkleidung", regel=RW, zweifel=ZW)
w2, c2 = rd("0.9 / sin(12)", 2)
neu(T, "seite", "umkehren", Z(
    "Eine Rampe soll einen Höhenunterschied von 0,9 m überwinden und mit der Waagerechten einen Winkel von 12° bilden. Wie lang ist die Rampe (die schräge Strecke)? Runde auf zwei Dezimalstellen.",
    w2, c2, "round(0.9 / sin(12), 2)", "Die Höhe ist die Gegenkathete des Winkels, die Rampe die Hypotenuse. Welches Verhältnis passt?",
    "sin 12° = 0,9 : Länge, also Länge = 0,9 : sin 12° ≈ 0,9 : 0,2079 ≈ 4,33 m.",
    [BR("0.9 * sin(12)", "mit dem Sinus malgenommen statt geteilt", None, 2), BR("0.9 / cos(12)", "den Kosinus statt den Sinus genommen", None, 2), BR("0.9 / tan(12)", "den Tangens statt den Sinus genommen", None, 2)], einheit="m", toleranz=0.01), g="rueckwaerts", regel=RW, zweifel=ZW)
# ───────── winkel ─────────
w3, c3 = rd("atan(15 / 28)", 1)
neu(T, "winkel", "anwenden", Z(
    "Eine Treppenstufe ist 15 cm hoch und 28 cm tief. Unter welchem Winkel zur Waagerechten steigt die Treppe an? Runde auf eine Dezimalstelle (in Grad).",
    w3, c3, "round(atan(15 / 28), 1)", "Stufenhöhe und Stufentiefe sind die Katheten. Welches Verhältnis kennst du, und wie kommst du von ihm zum Winkel?",
    "tan α = 15 : 28 ≈ 0,5357. Mit der Umkehrfunktion des Tangens: α ≈ 28,2°.",
    [BR("atan(28 / 15)", "die Katheten vertauscht", None, 1), BR("asin(15 / 28)", "den Sinus statt den Tangens genommen", None, 1), BR("15 / 28", "das Verhältnis selbst als Winkel genommen", None, 1)], einheit="°", toleranz=0.1), g="einkleidung", regel=RW, zweifel=ZW)
# ───────── beziehungen ─────────
neu(T, "beziehungen", "anwenden", Z(
    "Ein spitzer Winkel α hat sin α = 0,28. Wie groß ist cos α?",
    0.96, "0.96", "round((1 - 0.28 ** 2) ** 0.5, 2)", "Für jeden spitzen Winkel gilt (sin α)² + (cos α)² = 1. Stelle um und ziehe die Wurzel.",
    "(cos α)² = 1 − 0,28² = 1 − 0,0784 = 0,9216. Die Wurzel ist 0,96. Probe: 0,96² = 0,9216.",
    [B("1 - 0.28", "von 1 abgezogen, ohne zu quadrieren und die Wurzel zu ziehen"), B("1 - 0.28 ** 2", "die Wurzel nicht gezogen"), B("0.28", "den Sinus als Kosinus angegeben")]), g="mehrschritt", ohne=OHNE_B)
neu(T, "beziehungen", "verfahren_waehlen", W(
    "Es gilt sin 70° ≈ 0,9397. Für welchen Winkel hat der Kosinus denselben Wert?",
    "für 20°", [("für 70°", "derselbe Winkel hat Sinus und Kosinus nicht gleich, nur bei 45°"), ("für 110°", "180° − 70°, das gilt für den Sinus, nicht für den Kosinus im spitzen Bereich"), ("für 160°", "90° + 70° ist keine Ergänzung zu 90°")],
    "In einem rechtwinkligen Dreieck ist die Gegenkathete des einen spitzen Winkels die Ankathete des anderen. Die beiden spitzen Winkel ergeben zusammen 90°.",
    "Die beiden spitzen Winkel eines rechtwinkligen Dreiecks ergänzen sich zu 90°. Es gilt sin α = cos(90° − α). Mit α = 70° folgt sin 70° = cos 20°.",
    lambda: abs(math.sin(math.radians(70)) - math.cos(math.radians(20))) < 1e-9 and abs(math.sin(math.radians(70)) - math.cos(math.radians(70))) > 0.1), g="begruenden", ohne=OHNE_B)
# ───────── anwendung ─────────
w4, c4 = rd("38 / tan(4)", 0)
neu(T, "anwendung", "anwenden", Z(
    "Vom Leuchtturm in Kroatien, dessen Spitze 38 m über dem Meer liegt, sieht man ein Boot unter einem Tiefenwinkel von 4°. Wie weit ist das Boot vom Fuß des Leuchtturms entfernt? Runde auf ganze Meter.",
    w4, c4, "round(38 / tan(4))", "Der Tiefenwinkel ist genauso groß wie der Winkel am Boot im Dreieck. Welche Seiten sind bekannt, welche gesucht?",
    "Im rechtwinkligen Dreieck gilt tan 4° = 38 : Entfernung. Also Entfernung = 38 : tan 4° ≈ 38 : 0,06993 ≈ 543 m.",
    [BR("38 * tan(4)", "mit dem Tangens malgenommen statt geteilt", None, 0), BR("38 / cos(4)", "den Kosinus statt den Tangens genommen", None, 0), BR("38 / sin(4)", "den Sinus statt den Tangens genommen", None, 0)], einheit="m", toleranz=1), g="einkleidung", regel=RW, zweifel=ZW)
neu(T, "anwendung", "fehler_detektiv", FD(
    "Alex berechnet im rechtwinkligen Dreieck (Hypotenuse 20 cm, α = 40°) die Ankathete von α:",
    [("Die Ankathete liegt am Winkel an, deshalb gilt cos α = Ankathete : Hypotenuse.", True, True),
     ("Also ist die Ankathete gleich 20 : cos 40°.", False, True),
     ("Das sind etwa 26,1 cm.", True, True),
     ("Die Ankathete wäre länger als die Hypotenuse mit 20 cm.", True, True)],
    "Stelle cos α = Ankathete : Hypotenuse nach der Ankathete um. Muss die Ankathete länger oder kürzer als die Hypotenuse sein?",
    "Aus cos α = Ankathete : Hypotenuse folgt Ankathete = cos α · Hypotenuse = cos 40° · 20 ≈ 15,3 cm. In Zeile 2 wurde geteilt statt malgenommen. Zeile 4 zeigt den Widerspruch: Eine Kathete ist nie länger als die Hypotenuse."), g="fehler", regel=RW, zweifel=ZW)
# ───────── schnittwinkel ─────────
w5, c5 = rd("atan(0.12)", 1)
neu(T, "schnittwinkel", "anwenden", Z(
    "Eine Straße in Norwegen hat 12 % Steigung, das heißt 12 m Höhenunterschied auf 100 m waagerechte Strecke. Unter welchem Winkel steigt sie gegenüber der Waagerechten an? Runde auf eine Dezimalstelle (in Grad).",
    w5, c5, "round(atan(12 / 100), 1)", "Die Steigung ist das Verhältnis von Höhe zu waagerechter Strecke, also der Tangens des Winkels.",
    "tan α = 12 : 100 = 0,12. Mit der Umkehrfunktion: α ≈ 6,8°. Bei 12 % Steigung ist der Winkel also viel kleiner als 12°.",
    [B("12", "die Prozentzahl als Winkel in Grad genommen"), BR("atan(12)", "12 statt 0,12 in den Tangens eingesetzt", None, 1), BR("atan(100 / 12)", "Höhe und Strecke vertauscht", None, 1)], einheit="°", toleranz=0.1), g="einkleidung", ohne=OHNE_S)
w6, c6 = rd("atan(3) - atan(1)", 1)
neu(T, "schnittwinkel", "anwenden", Z(
    "Die Geraden y = x und y = 3x schneiden sich im Ursprung. Unter welchem Winkel schneiden sie sich? Runde auf eine Dezimalstelle (in Grad).",
    w6, c6, "round(atan(3) - atan(1), 1)", "Jede Gerade bildet mit der x-Achse einen Winkel, dessen Tangens die Steigung ist. Der Schnittwinkel ist der Unterschied.",
    "Die Gerade y = x hat den Winkel 45° zur x-Achse, die Gerade y = 3x den Winkel arctan 3 ≈ 71,6°. Der Schnittwinkel ist 71,6° − 45° = 26,6°.",
    [BR("atan(3)", "nur den Winkel der steileren Geraden genommen", None, 1), BR("atan(3 - 1)", "die Steigungen subtrahiert und davon den Winkel genommen", None, 1), B("3 - 1", "den Unterschied der Steigungen als Winkel genommen")], einheit="°", toleranz=0.1), g="mehrschritt", ohne=OHNE_S)
