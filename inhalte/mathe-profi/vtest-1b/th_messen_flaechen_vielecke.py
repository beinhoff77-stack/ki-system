T = "messen.flaechen_vielecke"
LP = "M6 2 Flächeninhalt und Volumen (Flächeninhalt von Parallelogramm, Dreieck und Trapez; zusammengesetzte Figuren)"
REGEL[(T, "dreieck")] = REGEL[(T, "zusammengesetzt")] = REGEL[(T, "verstehen")] = "id.flaeche_raum.aus_dem_rechteck"
REGEL[(T, "rueckwaerts")] = "id.flaeche_raum.aus_dem_rechteck"
ABG[(T, "dreieck")] = "Die Übungen setzen g und h in g · h : 2 ein; hier wird erklärt, warum zwei gleiche Dreiecke ein Parallelogramm ergeben, warum die Höhe und nicht die schräge Seite zählt, auch wenn sie außen liegt, und das Dreieck über Koordinaten berechnet."
ABG[(T, "rueckwaerts")] = "Die Übungen stellen die Flächenformel nach h oder g um; hier wird begründet, warum ein Parallelogramm einem Rechteck gleicher Fläche entspricht und zwei Trapeze ein Parallelogramm ergeben, und in Sachsituationen umgerechnet."
ABG[(T, "zusammengesetzt")] = "Die Übungen zerlegen eine vorgegebene Figur; hier wird ein Trapez auf zwei Arten zerlegt, Ecken werden abgeschnitten und eine Teilfläche rückwärts gesucht."
ABG[(T, "verstehen")] = "Die Übungen rechnen mit verdoppelten Maßen; hier wird erklärt, warum Schieben die Fläche nicht ändert, wie ein Dreieck oder Trapez zu einem Parallelogramm gehört und was sich bei Umfang und Fläche ändert."
# ───────── dreieck ─────────
neu(T, "dreieck", "test", "transfer", L(
    "Im Koordinatensystem sind die Punkte A(0|0), B(10|0), C(5|4) und D(17|4) gegeben (eine Einheit ist 1 cm). Gib den Flächeninhalt der beiden Dreiecke ABC und ABD an.",
    "ABC: □ cm², ABD: □ cm²", [20, 20], ["10 * 4 / 2", "10 * 4 / 2"], ["2 * 10", "40 / 2"],
    "Beide Dreiecke haben die Grundseite AB auf der x-Achse, AB = 10 cm. Die Höhe ist für beide der Abstand von C und D zur x-Achse, also die y-Koordinate 4 cm; sie liegt bei ABD außerhalb des Dreiecks, zählt aber genauso. A = 10 · 4 : 2 = 20 cm² für beide Dreiecke. Die x-Koordinaten (5 und 17) ändern die Fläche nicht.",
    {0: [(40, "das Halbieren vergessen: 10 · 4", "10 * 4"), (10, "die x-Koordinate von C als Grundseite genommen: 5 · 4 : 2", "5 * 4 / 2")],
     1: [(34, "die x-Koordinate von D als Grundseite genommen: 17 · 4 : 2", "17 * 4 / 2"), (68, "die x-Koordinate von D als Grundseite ohne Halbieren: 17 · 4", "17 * 4")]}),
    lp=LP, idee="hoehe_ausserhalb")
neu(T, "dreieck", "korrektur", "mehrschritt", Z(
    "Das Dreieck ABC hat die Ecken A(1|1), B(9|1) und C(12|6) (eine Einheit ist 1 cm). Ben legt das kleinste Rechteck mit achsenparallelen Seiten um das Dreieck; es hat 55 cm². Dann zieht er die beiden überstehenden Dreiecke ab. Wie viele cm² muss er insgesamt von den 55 cm² abziehen?",
    35, "11 * 5 / 2 + 3 * 5 / 2", "55 - 20",
    "Das Rechteck reicht von x = 1 bis x = 12 und von y = 1 bis y = 6, es ist 11 cm breit und 5 cm hoch. Überstehend sind zwei rechtwinklige Dreiecke: eines mit den Katheten 11 und 5 (11 · 5 : 2 = 27,5 cm²) und eines mit den Katheten 3 und 5 (3 · 5 : 2 = 7,5 cm²). Zusammen sind das 35 cm². Es bleiben 55 − 35 = 20 cm², das ist die Fläche des Dreiecks.",
    [B("55 - 35", "die Fläche des Dreiecks (20 cm²) angegeben statt der abzuziehenden Fläche"),
     B("11 * 5 / 2", "nur das große überstehende Dreieck abgezogen"),
     B("3 * 5 / 2 + 11 * 5", "das große überstehende Dreieck ohne Halbieren gerechnet")], einheit="cm²"), form="zwei_wege", lp=LP, idee="ergaenzen_rechteck")
neu(T, "dreieck", "korrektur", "darstellung", Z(
    "Zwei gleiche Dreiecke werden so aneinandergelegt, dass ein Parallelogramm mit der Grundseite 12 cm und der Höhe 7 cm entsteht. Wie groß ist die Fläche eines der beiden Dreiecke?",
    42, "12 * 7 / 2", "84 / 2",
    "Das Parallelogramm hat A = 12 · 7 = 84 cm². Es besteht aus zwei gleichen Dreiecken, jedes hat also die Hälfte: 84 : 2 = 42 cm². Genau deshalb wird bei der Dreiecksformel g · h durch 2 geteilt.",
    [B("12 * 7", "die Fläche des ganzen Parallelogramms angegeben"),
     B("12 + 7", "Grundseite und Höhe addiert"),
     B("12 * 7 / 4", "durch 4 statt durch 2 geteilt")], einheit="cm²"), lp=LP, idee="zwei_dreiecke_parallelogramm")
neu(T, "dreieck", "korrektur", "darstellung", W(
    "Das Dreieck ABC hat die Ecken A(0|0), B(8|0) und C(3|5) (eine Einheit ist 1 cm). Welche Rechnung gibt seinen Flächeninhalt in cm²?",
    "8 · 5 : 2",
    [("8 · 3 : 2", "die x-Koordinate von C als Höhe genommen"),
     ("8 · 5", "das Halbieren vergessen"),
     ("5 · 3 : 2", "die Koordinaten von C als Grundseite und Höhe genommen")],
    "Die Grundseite AB liegt auf der x-Achse und ist 8 cm lang. Die Höhe ist der Abstand von C zur x-Achse, also die y-Koordinate 5 cm. Es gilt A = 8 · 5 : 2 = 20 cm². Die x-Koordinate 3 von C sagt nur, wo die Spitze liegt, nicht wie hoch sie ist.",
    lambda: abs(0 * (0 - 5) + 8 * (5 - 0) + 3 * (0 - 0)) / 2 == 8 * 5 / 2 and 8 * 3 / 2 != 20 and 8 * 5 != 20 and 5 * 3 / 2 != 20), form="bruecke", lp=LP, idee="formel_aus_koordinaten")
neu(T, "dreieck", "sicherung", "fehler", L(
    "Ein Kind berechnet ein Dreieck mit der Grundseite 10 cm, der Höhe 6 cm und der schrägen Seite 7 cm so: Zeile 1: Die Höhe steht senkrecht auf der Grundseite und ist 6 cm lang. Zeile 2: A = g · s : 2 = 10 · 7 : 2 = 35. Zeile 3: Der Flächeninhalt ist 35 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist der Flächeninhalt richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 30], ["2", "10 * 6 / 2"], ["3 - 1", "30"],
    "Zeile 1 stimmt. In Zeile 2 wurde die schräge Seite statt der Höhe genommen. Die Höhe ist 6 cm, also gilt A = 10 · 6 : 2 = 30 cm². Zeile 3 übernimmt das falsche Ergebnis. Die schräge Seite ist länger als die Höhe und darf in der Formel nicht stehen.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(35, "mit der schrägen Seite statt der Höhe gerechnet: 10 · 7 : 2", "10 * 7 / 2"), (60, "das Halbieren vergessen: 10 · 6", "10 * 6"), (42, "Höhe mal schräge Seite gerechnet: 6 · 7", "6 * 7")]}), form="fehler_detektiv", lp=LP, idee="schraege_seite_fehler")
neu(T, "dreieck", "sicherung", "begruenden", W(
    "Das Dreieck ABD hat die Ecken A(0|0), B(9|0) und D(15|6) (eine Einheit ist 1 cm). Ein Kind sagt: „Die Höhe liegt hier außerhalb des Dreiecks, deshalb darf man nicht Grundseite mal Höhe durch 2 rechnen.“ Welche Aussage stimmt?",
    "Das Kind irrt: Die Fläche ist 9 · 6 : 2 = 27 cm², denn man kann D parallel zu AB verschieben, ohne dass sich Grundseite und Höhe ändern.",
    [("Das Kind hat recht, denn bei einer Höhe außerhalb gilt nur die Rechnung mit der schrägen Seite AD.", "die Höhe außerhalb für ungültig gehalten; auch dort ist es der senkrechte Abstand zur Grundseite"),
     ("Das Kind irrt: Die Fläche ist 9 · 6 = 54 cm², denn bei einer Höhe außerhalb wird nicht halbiert.", "gedacht, das Halbieren entfällt, wenn die Höhe außen liegt; es gilt dieselbe Formel"),
     ("Das Kind hat recht, denn die Fläche lässt sich dann nur über Koordinaten bestimmen.", "geglaubt, die Formel gelte nur für Dreiecke mit Höhe innen")],
    "Die Grundseite AB liegt auf der x-Achse, AB = 9 cm. Die Höhe von D ist der Abstand zur x-Achse, 6 cm, auch wenn der Fußpunkt (15|0) außerhalb von AB liegt. A = 9 · 6 : 2 = 27 cm². Verschiebt man D parallel zu AB (zum Beispiel nach (4|6)), ändern sich Grundseite und Höhe nicht, also auch nicht die Fläche.",
    lambda: 9 * 6 / 2 == 27 and abs(0 * (0 - 6) + 9 * (6 - 0) + 15 * (0 - 0)) / 2 == 27 and 9 * 6 != 27), lp=LP, idee="scherung_begruenden")
neu(T, "dreieck", "sicherung", "umkehr", Z(
    "Der Flächeninhalt eines Dreiecks ist 36 cm². Seine Höhe ist doppelt so lang wie die zugehörige Grundseite. Wie lang ist die Grundseite?",
    6, "6", "36 / 6",
    "Mit g für die Grundseite ist h = 2g. Dann gilt A = g · 2g : 2 = g · g = 36. Also ist g = 6 cm und h = 12 cm. Probe: 6 · 12 : 2 = 36.",
    [B("36 / 2", "36 durch 2 geteilt und als Grundseite genommen"),
     B("36 / 4", "36 durch 4 geteilt, weil von „doppelt“ und „halb“ die 2 zweimal gezählt wurde"),
     B("12", "die Höhe statt der Grundseite angegeben")], einheit="cm"), form="umkehren", lp=LP, idee="quadrat_aus_hoehe")
# ───────── rueckwaerts ─────────
neu(T, "rueckwaerts", "test", "rueckwaerts", Z(
    "Ein Feld hat die Form eines Parallelogramms ABCD. Im Koordinatensystem (eine Einheit ist 1 m) ist A(0|0) und B(300|0); die Seite DC verläuft parallel zur x-Achse. Das Feld ist 4,5 ha groß (1 ha = 10 000 m²). Welche y-Koordinate hat der Punkt D?",
    150, "4.5 * 10000 / 300", "45000 / 300",
    "4,5 ha = 45 000 m². Die Grundseite AB ist 300 m lang, die Höhe ist der Abstand der Seite DC von der x-Achse, also die y-Koordinate von D. Aus A = g · h folgt h = 45 000 : 300 = 150 m. Probe: 300 · 150 = 45 000 m².",
    [B("45000 / 300 / 2", "wie bei einem Dreieck durch 2 geteilt"),
     B("4500 / 300", "die Hektar mit dem falschen Faktor in m² umgerechnet (um eine Null zu wenig)"),
     B("4.5 / 300 * 100", "die Hektar nicht in m² umgerechnet")], einheit="m"), lp=LP, idee="hoehe_aus_flaeche")
neu(T, "rueckwaerts", "korrektur", "umkehr", Z(
    "Ein Parallelogramm hat den Flächeninhalt 98 cm². Seine Höhe ist halb so lang wie die zugehörige Grundseite. Wie lang ist die Grundseite?",
    14, "14", "196 / 14",
    "Mit g für die Grundseite ist h = g : 2. Dann gilt A = g · g : 2 = 98, also g · g = 196 und g = 14 cm. Die Höhe ist 7 cm. Probe: 14 · 7 = 98.",
    [B("98 / 14", "die Höhe 7 statt der Grundseite angegeben"),
     B("98 / 2", "98 durch 2 geteilt und als Grundseite genommen"),
     B("98 / 4", "98 durch 4 geteilt, weil von „halb“ die 2 zweimal gezählt wurde")], einheit="cm"), form="umkehren", lp=LP, idee="gleichung_g_mal_g")
neu(T, "rueckwaerts", "korrektur", "darstellung", Z(
    "Ein Parallelogramm hat die Grundseite 12 cm, die schräge Nachbarseite 9 cm und den Flächeninhalt 96 cm². Es wird zu einem Rechteck mit derselben Grundseite und demselben Flächeninhalt umgebaut: Ein Dreieck wird auf der einen Seite abgeschnitten und auf der anderen Seite wieder angesetzt. Wie hoch ist das Rechteck?",
    8, "96 / 12", "8",
    "Das Rechteck hat dieselbe Grundseite 12 cm und dieselbe Fläche 96 cm². Seine Höhe ist 96 : 12 = 8 cm. Das ist zugleich die Höhe des Parallelogramms. Die schräge Seite 9 cm spielt keine Rolle: Beim Umbauen ändert sich nur die Form, nicht Grundseite, Höhe und Fläche.",
    [B("9", "die schräge Seite als Höhe genommen"),
     B("96 / 12 / 2", "wie bei einem Dreieck durch 2 geteilt"),
     B("96 - 12", "die Grundseite von der Fläche abgezogen")], einheit="cm"), lp=LP, idee="parallelogramm_zu_rechteck")
neu(T, "rueckwaerts", "korrektur", "darstellung", L(
    "Zwei gleiche Trapeze mit den parallelen Seiten 5 cm und 9 cm und der Höhe 4 cm werden zu einem Parallelogramm zusammengelegt. Die Grundseite des Parallelogramms ist □ cm lang. Ein einzelnes Trapez hat die Fläche □ cm².",
    "Grundseite □ cm, Trapez □ cm²", [14, 28], ["5 + 9", "(5 + 9) * 4 / 2"], ["14", "56 / 2"],
    "Legt man das zweite Trapez umgedreht an das erste, ergeben die parallelen Seiten zusammen die Grundseite 5 + 9 = 14 cm; die Höhe bleibt 4 cm. Das Parallelogramm hat 14 · 4 = 56 cm², ein Trapez die Hälfte: 28 cm². So entsteht die Trapezformel (a + c) · h : 2.",
    {0: [(9, "nur die längere parallele Seite genommen", "9"), (45, "die parallelen Seiten malgenommen: 5 · 9", "5 * 9")],
     1: [(56, "das Halbieren vergessen: 14 · 4", "(5 + 9) * 4"), (36, "nur die längere Seite mit der Höhe malgenommen: 9 · 4", "9 * 4"), (20, "nur die kürzere Seite mit der Höhe malgenommen: 5 · 4", "5 * 4")]}),
    form="bruecke", lp=LP, idee="trapez_zu_parallelogramm")
neu(T, "rueckwaerts", "sicherung", "fehler", L(
    "Ein Kind berechnet die Höhe eines Parallelogramms mit A = 54 cm² und der Grundseite 9 cm so: Zeile 1: Es gilt A = g · h. Zeile 2: Also ist h = A · g = 54 · 9 = 486. Zeile 3: Die Höhe ist 486 cm. In welcher Zeile steckt der erste Fehler? Wie lang ist die Höhe richtig?",
    "Fehler in Zeile □, richtig: h = □ cm", [2, 6], ["2", "54 / 9"], ["3 - 1", "6"],
    "Zeile 1 stimmt. In Zeile 2 wurde falsch umgestellt: Aus A = g · h folgt h = A : g, nicht A · g. Richtig ist h = 54 : 9 = 6 cm. Zeile 3 übernimmt das unsinnige Ergebnis 486 cm. Probe: 9 · 6 = 54.",
    {0: [(3, "die Schlusszeile genannt, weil dort der unsinnige Wert 486 steht", "3")], 1: [(486, "mal statt geteilt gerechnet: 54 · 9", "54 * 9"), (3, "zusätzlich noch durch 2 geteilt: 54 : 9 : 2", "54 / 9 / 2"), (63, "Fläche und Grundseite addiert: 54 + 9", "54 + 9")]}), form="fehler_detektiv", lp=LP, idee="umstellfehler")
neu(T, "rueckwaerts", "sicherung", "umkehr", L(
    "Ein Dreieck hat den Flächeninhalt 40 cm² und die Grundseite 10 cm. Ergänze: Seine Höhe ist □ cm. Ein zweites Dreieck mit derselben Höhe und dem doppelten Flächeninhalt hat die Grundseite □ cm.",
    "Höhe □ cm, zweite Grundseite □ cm", [8, 20], ["2 * 40 / 10", "2 * 80 / 8"], ["80 / 10", "10 * 2"],
    "Höhe des ersten Dreiecks: h = 2 · A : g = 2 · 40 : 10 = 8 cm. Das zweite Dreieck hat A = 80 cm² und h = 8 cm, also g = 2 · 80 : 8 = 20 cm. Bei gleicher Höhe und doppelter Fläche ist die Grundseite doppelt so lang.",
    {0: [(4, "das Verdoppeln vergessen: 40 : 10", "40 / 10"), (400, "Fläche mal Grundseite gerechnet: 40 · 10", "40 * 10")], 1: [(10, "die Fläche nicht verdoppelt: 2 · 40 : 8", "2 * 40 / 8"), (5, "durch 2 geteilt statt doppelt gerechnet: 40 : 8", "40 / 8")]}), lp=LP, idee="grundseite_hoehe_gegenlaeufig")
neu(T, "rueckwaerts", "sicherung", "begruenden", W(
    "Ein Parallelogramm hat die Grundseite 8 cm, die schräge Nachbarseite 6 cm und den Flächeninhalt 48 cm². Welche Aussage über das Parallelogramm stimmt?",
    "Es ist ein Rechteck, denn die Höhe 48 : 8 = 6 cm ist genauso lang wie die schräge Seite.",
    [("Es ist ein schiefes Parallelogramm, denn die schräge Seite ist immer länger als die Höhe.", "geglaubt, die schräge Seite sei immer länger; nur bei einem Rechteck sind beide gleich lang"),
     ("Ein solches Parallelogramm gibt es nicht, denn die Höhe darf nicht so lang wie die schräge Seite sein.", "gedacht, die Höhe müsse kürzer als die schräge Seite sein; gleich lang ist beim Rechteck möglich"),
     ("Es ist ein Rechteck, denn die Fläche 48 ist durch die Grundseite 8 teilbar.", "die Teilbarkeit als Begründung genommen; entscheidend ist der Vergleich von Höhe und schräger Seite")],
    "Aus A = g · h folgt h = 48 : 8 = 6 cm. Die Höhe steht senkrecht auf der Grundseite und ist nie länger als die schräge Seite. Sie ist genau dann gleich lang, wenn die schräge Seite selbst senkrecht steht, das Parallelogramm also ein Rechteck ist. Hier sind beide 6 cm lang.",
    lambda: F(48, 8) == 6 and F(48, 8) <= 6 and F(48, 8) == 6 != 7), lp=LP, idee="hoehe_gleich_schraege")
# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "test", "transfer", Z(
    "Ein Quadrat hat die Seitenlänge 12 cm. An jeder der vier Ecken wird ein gleichschenklig-rechtwinkliges Dreieck mit den Katheten 3 cm abgeschnitten. Wie groß ist der Flächeninhalt der übrig bleibenden Figur?",
    126, "144 - 4 * 3 * 3 / 2", "144 - 18",
    "Das Quadrat hat 12 · 12 = 144 cm². Jedes abgeschnittene Dreieck hat 3 · 3 : 2 = 4,5 cm², vier Dreiecke haben 18 cm². Es bleiben 144 − 18 = 126 cm².",
    [B("144 - 4 * 3 * 3", "das Halbieren vergessen: vier Quadrate mit der Seite 3 abgezogen"),
     B("144 - 3 * 3 / 2", "nur eine Ecke abgezogen"),
     B("144 - 4 * 3", "für jede Ecke nur die Seite 3 abgezogen")], einheit="cm²"), lp=LP, idee="ecken_abschneiden")
neu(T, "zusammengesetzt", "korrektur", "umkehr", Z(
    "Aus einer Ecke eines Rechtecks (14 cm lang, 9 cm breit) wird ein kleines Rechteck herausgeschnitten, das 4 cm lang ist (entlang der langen Seite gemessen). Die Restfläche beträgt 102 cm². Wie breit ist das herausgeschnittene Stück (entlang der kurzen Seite gemessen)?",
    6, "(14 * 9 - 102) / 4", "24 / 4",
    "Das große Rechteck hat 14 · 9 = 126 cm². Weggenommen wurden 126 − 102 = 24 cm². Das Stück ist 4 cm lang, also ist es 24 : 4 = 6 cm breit. Probe: 126 − 4 · 6 = 102.",
    [B("102 / 4", "die Restfläche statt der weggenommenen Fläche durch 4 geteilt"),
     B("126 / 4", "die Fläche des ganzen Rechtecks durch 4 geteilt"),
     B("126 - 102", "die weggenommene Fläche 24 als Breite angegeben")], einheit="cm"), form="umkehren", lp=LP, idee="rest_rueckwaerts")
neu(T, "zusammengesetzt", "korrektur", "darstellung", L(
    "Ein Trapez hat die parallelen Seiten 8 cm und 5 cm und die Höhe 4 cm. Eine Diagonale zerlegt es in zwei Dreiecke. Das Dreieck mit der Grundseite 8 cm hat □ cm², das Dreieck mit der Grundseite 5 cm hat □ cm², das Trapez hat zusammen □ cm².",
    "□ cm² und □ cm², zusammen □ cm²", [16, 10, 26], ["8 * 4 / 2", "5 * 4 / 2", "(8 + 5) * 4 / 2"], ["16", "10", "26"],
    "Beide Dreiecke haben die Höhe 4 cm, denn die beiden parallelen Seiten haben den Abstand 4 cm. Das Dreieck mit der Grundseite 8 cm hat 8 · 4 : 2 = 16 cm², das mit der Grundseite 5 cm hat 5 · 4 : 2 = 10 cm². Zusammen 26 cm². Das ist (8 + 5) · 4 : 2, die Trapezformel.",
    {0: [(32, "das Halbieren vergessen: 8 · 4", "8 * 4"), (12, "Grundseite und Höhe addiert: 8 + 4", "8 + 4")],
     1: [(20, "das Halbieren vergessen: 5 · 4", "5 * 4"), (9, "Grundseite und Höhe addiert: 5 + 4", "5 + 4")],
     2: [(52, "beide Dreiecke ohne Halbieren gerechnet: 32 + 20", "8 * 4 + 5 * 4"), (40, "die parallelen Seiten malgenommen: 8 · 5", "8 * 5")]}),
    form="bruecke", lp=LP, idee="trapez_zwei_dreiecke")
neu(T, "zusammengesetzt", "korrektur", "mehrschritt", L(
    "Ein gleichschenkliges Trapez ist unten 14 cm und oben 8 cm breit und 5 cm hoch. Schneidet man links und rechts je ein gleiches Dreieck ab, bleibt ein Rechteck übrig. Jedes abgeschnittene Dreieck hat die Grundseite □ cm. Das Trapez hat die Fläche □ cm².",
    "Grundseite □ cm, Trapez □ cm²", [3, 55], ["(14 - 8) / 2", "8 * 5 + 2 * 3 * 5 / 2"], ["3", "(14 + 8) * 5 / 2"],
    "Das Rechteck ist 8 cm breit. Von der unteren Breite 14 cm bleiben 14 − 8 = 6 cm für die beiden Dreiecke, also je 3 cm. Rechteck: 8 · 5 = 40 cm². Jedes Dreieck: 3 · 5 : 2 = 7,5 cm². Zusammen 40 + 15 = 55 cm². Das stimmt mit (14 + 8) · 5 : 2 = 55 überein.",
    {0: [(6, "die ganze Differenz genommen statt der Hälfte für jedes Dreieck", "14 - 8"), (11, "die obere Breite von der unteren abgezogen und die Höhe addiert: 14 − 3", "14 - 3")],
     1: [(40, "nur das Rechteck berechnet", "8 * 5"), (70, "die untere Breite mit der Höhe malgenommen: 14 · 5", "14 * 5"), (22, "die Summe der parallelen Seiten statt der Fläche angegeben", "14 + 8")]}),
    form="bruecke", lp=LP, idee="trapez_rechteck_dreiecke")
neu(T, "zusammengesetzt", "sicherung", "fehler", L(
    "Ein Kind berechnet ein Fünfeck aus einem Rechteck (12 cm breit, 5 cm hoch) und einem Dreieck darauf mit der Grundseite 12 cm und der Höhe 4 cm. Zeile 1: Rechteck: 12 · 5 = 60 cm². Zeile 2: Dreieck: 12 · 4 = 48 cm². Zeile 3: Gesamt: 60 + 48 = 108 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist die Figur richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 84], ["2", "12 * 5 + 12 * 4 / 2"], ["3 - 1", "60 + 24"],
    "Zeile 1 stimmt. In Zeile 2 fehlt das Halbieren: Das Dreieck hat 12 · 4 : 2 = 24 cm². Gesamt: 60 + 24 = 84 cm². Zeile 3 rechnet mit dem falschen Dreieck richtig weiter.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(108, "das Dreieck ohne Halbieren gerechnet: 60 + 48", "60 + 12 * 4"), (72, "das Dreieck mit 12 statt 24 gerechnet: 60 + 12", "60 + 12"), (48, "nur das Dreieck ohne Halbieren angegeben", "12 * 4")]}), form="fehler_detektiv", lp=LP, idee="halbieren_vergessen")
neu(T, "zusammengesetzt", "sicherung", "darstellung", W(
    "Eine Figur ist 9 cm breit und 7 cm hoch. Unten rechts fehlt ein Rechteck von 3 cm Breite und 2 cm Höhe. Welche Rechnung gibt den Flächeninhalt der Figur in cm² richtig an?",
    "6 · 7 + 3 · 5",
    [("9 · 7 − 3 · 5", "das fehlende Stück falsch bemessen: Es ist 2 cm hoch, nicht 5 cm"),
     ("6 · 7 + 3 · 2", "das rechte Stück mit der Höhe des fehlenden Stücks gerechnet statt mit der Resthöhe"),
     ("9 · 5 + 3 · 2", "das fehlende Stück dazugezählt statt weggelassen")],
    "Die Figur lässt sich in zwei Rechtecke zerlegen: links 6 cm breit und 7 cm hoch, rechts 3 cm breit und 7 − 2 = 5 cm hoch. Das ergibt 6 · 7 + 3 · 5 = 42 + 15 = 57 cm². Gleichwertig ist die Ergänzung: 9 · 7 − 3 · 2 = 63 − 6 = 57 cm².",
    lambda: 6 * 7 + 3 * 5 == 9 * 7 - 3 * 2 == 57 and 9 * 7 - 3 * 5 != 57 and 6 * 7 + 3 * 2 != 57 and 9 * 5 + 3 * 2 != 57), lp=LP, idee="zerlegen_rechnungen")
neu(T, "zusammengesetzt", "sicherung", "transfer", Z(
    "Das Viereck ABCD hat die Ecken A(0|0), B(10|0), C(7|6) und D(1|6) (eine Einheit ist 1 cm). Wie viele cm² hat es?",
    48, "(10 + 6) * 6 / 2", "10 * 6 - 3 * 6 / 2 - 1 * 6 / 2",
    "AB und DC liegen auf Parallelen zur x-Achse im Abstand 6 cm: AB = 10 cm, DC = 7 − 1 = 6 cm. Das Viereck ist ein Trapez mit A = (10 + 6) · 6 : 2 = 48 cm². Kontrolle durch Ergänzen: Rechteck 10 · 6 = 60 cm², abzüglich der Dreiecke links (1 · 6 : 2 = 3 cm²) und rechts (3 · 6 : 2 = 9 cm²): 60 − 12 = 48 cm².",
    [B("(10 + 7) * 6 / 2", "die x-Koordinate 7 von C statt der Länge DC genommen"),
     B("(10 + 6) * 6", "das Halbieren vergessen"),
     B("10 * 6 / 2", "nur das Dreieck über AB berechnet")], einheit="cm²"), form="zwei_wege", lp=LP, idee="koordinaten_trapez")
# ───────── verstehen ─────────
neu(T, "verstehen", "test", "rueckwaerts", Z(
    "Zwei gleiche Trapeze werden zu einem Parallelogramm mit der Höhe 4 cm zusammengelegt. Das Parallelogramm hat den Flächeninhalt 72 cm². Eine der beiden parallelen Seiten eines Trapezes ist 10 cm lang. Wie lang ist die andere parallele Seite?",
    8, "72 / 4 - 10", "18 - 10",
    "Legt man zwei gleiche Trapeze zusammen, ist die Grundseite des Parallelogramms die Summe der beiden parallelen Seiten a + c. Mit A = (a + c) · h folgt a + c = 72 : 4 = 18 cm. Eine Seite ist 10 cm, die andere also 18 − 10 = 8 cm. Probe: Ein Trapez hat (10 + 8) · 4 : 2 = 36 cm².",
    [B("72 / 4", "die Grundseite des Parallelogramms (18 cm) als andere parallele Seite angegeben"),
     B("72 / 4 + 10", "die bekannte Seite zur Grundseite des Parallelogramms addiert"),
     B("72 / 4 / 2", "die Grundseite des Parallelogramms durch 2 geteilt")], einheit="cm"), lp=LP, idee="trapez_doppelt")
neu(T, "verstehen", "korrektur", "darstellung", W(
    "Ein Rechteck ist 9 cm lang und 4 cm hoch. Man schiebt die obere Seite um 6 cm nach rechts, die untere Seite bleibt liegen, die Höhe bleibt 4 cm. Welche Aussage über die Fläche der neuen Figur stimmt?",
    "Die Fläche bleibt 36 cm², denn Grundseite und Höhe bleiben gleich.",
    [("Die Fläche wird größer, denn die schrägen Seiten sind länger als 4 cm.", "die Länge der schrägen Seiten mit der Höhe verwechselt"),
     ("Die Fläche wird kleiner, denn die Figur ist jetzt schief.", "gedacht, eine schiefe Figur habe weniger Fläche; entscheidend ist die Höhe"),
     ("Die Fläche wird 60 cm², denn die Figur ist jetzt 15 cm breit und 4 cm hoch.", "die verschobene Breite zur Grundseite addiert; die Grundseite bleibt 9 cm")],
    "Die Grundseite bleibt 9 cm, die Höhe bleibt 4 cm. Ein Parallelogramm hat A = g · h = 9 · 4 = 36 cm², genau wie das Rechteck vorher. Anschaulich: Das Dreieck, das links wegfällt, kommt rechts wieder dazu.",
    lambda: 9 * 4 == 36 and (9 + 6) * 4 == 60 and 9 * 4 == 9 * 4), lp=LP, idee="schiebung_flaeche")
neu(T, "verstehen", "korrektur", "umkehr", Z(
    "Ein Dreieck hat die Grundseite 10 cm und die Höhe 6 cm. Ein Rechteck mit derselben Fläche ist 4 cm breit. Wie lang ist das Rechteck?",
    7.5, "10 * 6 / 2 / 4", "30 / 4",
    "Das Dreieck hat 10 · 6 : 2 = 30 cm². Das Rechteck mit 30 cm² und der Breite 4 cm hat die Länge 30 : 4 = 7,5 cm. Probe: 7,5 · 4 = 30.",
    [B("10 * 6 / 4", "das Halbieren beim Dreieck vergessen"),
     B("10 * 6 / 2", "die Fläche des Dreiecks als Länge des Rechtecks angegeben"),
     B("10 / 4", "nur die Grundseite durch die Breite geteilt")], einheit="cm"), lp=LP, idee="dreieck_zu_rechteck")
neu(T, "verstehen", "korrektur", "darstellung", Z(
    "Ein Dreieck und ein Parallelogramm haben dieselbe Grundseite. Das Dreieck ist doppelt so hoch wie das Parallelogramm. Das Wievielfache des Flächeninhalts des Parallelogramms ist der Flächeninhalt des Dreiecks?",
    1, "2 / 2", "1",
    "Mit g und h für das Parallelogramm gilt A = g · h. Das Dreieck hat die Grundseite g und die Höhe 2h: A = g · 2h : 2 = g · h. Beide Flächen sind gleich groß, das Dreieck ist das 1-fache. Anschaulich: Zwei gleiche Dreiecke ergeben ein Parallelogramm.",
    [B("2", "die doppelte Höhe beachtet, das Halbieren beim Dreieck vergessen"),
     B("1 / 2", "nur das Halbieren beachtet und die doppelte Höhe vergessen"),
     B("2 * 2", "doppelte Höhe und Halbieren als zwei Verdoppelungen gerechnet")]), form="bruecke", lp=LP, idee="dreieck_halbes_parallelogramm")
neu(T, "verstehen", "sicherung", "fehler", L(
    "Ein Kind überlegt: Zeile 1: Ein Quadrat hat die Seitenlänge 5 cm, also A = 25 cm². Zeile 2: Die Seite wird verdoppelt und ist dann 10 cm lang. Zeile 3: Also wird auch die Fläche verdoppelt, A = 50 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist die Fläche des neuen Quadrats richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [3, 100], ["3", "10 * 10"], ["2 + 1", "4 * 25"],
    "Zeile 1 und Zeile 2 stimmen. In Zeile 3 wird die Fläche nur verdoppelt. Beide Maße des Quadrats werden doppelt so lang, die Fläche wird deshalb 2 · 2 = 4-mal so groß: 10 · 10 = 100 cm², das sind 4 · 25.",
    {0: [(2, "Zeile 2 genannt, obwohl dort die Seite richtig verdoppelt wird", "2")], 1: [(50, "die Fläche nur verdoppelt: 2 · 25", "2 * 25"), (20, "Seite mal 2 als Fläche gerechnet: 10 · 2", "10 * 2"), (40, "Seite mal 4 als Fläche gerechnet: 10 · 4", "10 * 4")]}), form="fehler_detektiv", lp=LP, idee="verdoppeln_fehler")
neu(T, "verstehen", "sicherung", "begruenden", W(
    "Ein Rechteck mit den Seiten 6 cm und 4 cm wird zu einem Parallelogramm schief gedrückt, dessen Seiten ebenfalls 6 cm und 4 cm lang sind. Welche Aussage über Umfang und Fläche stimmt?",
    "Der Umfang bleibt 20 cm, aber die Fläche wird kleiner, denn die Höhe wird kleiner als 4 cm.",
    [("Beides bleibt gleich, denn die Seitenlängen bleiben gleich.", "Fläche und Umfang verwechselt; der Umfang hängt nur von den Seitenlängen ab, die Fläche auch von der Höhe"),
     ("Beides wird kleiner, denn eine schiefe Figur ist kleiner.", "gedacht, der Umfang schrumpfe mit; er bleibt gleich, solange die Seiten gleich lang sind"),
     ("Der Umfang wird größer, die Fläche bleibt gleich, denn die schrägen Seiten sind länger als die Höhe.", "die schrägen Seiten länger als die Höhe genannt, aber ihre Länge ändert sich nicht")],
    "Der Umfang ist 2 · 6 + 2 · 4 = 20 cm und hängt nur von den Seitenlängen ab; er bleibt gleich. Die Fläche ist Grundseite mal Höhe. Die Grundseite bleibt 6 cm, aber die Höhe ist jetzt kleiner als die schräge Seite 4 cm, zum Beispiel 3 cm. Dann ist die Fläche kleiner als 24 cm², zum Beispiel 18 cm².",
    lambda: 2 * 6 + 2 * 4 == 20 and 6 * 3 < 6 * 4 and 6 * 3.9 < 24), lp=LP, idee="umfang_oder_flaeche")
neu(T, "verstehen", "sicherung", "darstellung", W(
    "Ein Rechteck ist 6 cm lang und 4 cm breit. Welche der folgenden Figuren hat denselben Flächeninhalt wie das Rechteck?",
    "ein Trapez mit den parallelen Seiten 8 cm und 4 cm und dem Abstand 4 cm",
    [("ein Parallelogramm mit der Grundseite 6 cm und der schrägen Nachbarseite 4 cm", "die schräge Seite als Höhe genommen; die Höhe ist kürzer als die schräge Seite"),
     ("ein Dreieck mit der Grundseite 6 cm und der Höhe 4 cm", "das Halbieren vergessen: das Dreieck hat nur die halbe Fläche"),
     ("ein Dreieck mit der Grundseite 8 cm und der Höhe 4 cm", "die Grundseite 8 mit dem Trapez verwechselt; das Dreieck hat nur 16 cm²")],
    "Das Rechteck hat 6 · 4 = 24 cm². Das Trapez hat (8 + 4) · 4 : 2 = 24 cm². Das schräge Parallelogramm hat die Höhe unter 4 cm, also weniger als 24 cm². Die Dreiecke haben 6 · 4 : 2 = 12 cm² und 8 · 4 : 2 = 16 cm².",
    lambda: (8 + 4) * 4 / 2 == 6 * 4 and 6 * 4 / 2 != 24 and 8 * 4 / 2 != 24 and 6 * 3.9 < 24), form="bruecke", lp=LP, idee="flaechengleiche_figuren")
