T = "messen.flaechen_vielecke"
LP = "M6 2 Flächeninhalt und Volumen (Flächeninhalt von Parallelogramm, Dreieck und Trapez; zusammengesetzte Figuren)"
REGEL[(T, "dreieck")] = REGEL[(T, "zusammengesetzt")] = REGEL[(T, "verstehen")] = "id.flaeche_raum.aus_dem_rechteck"
REGEL[(T, "rueckwaerts")] = "id.flaeche_raum.aus_dem_rechteck"
ABG[(T, "dreieck")] = "Die Übungen setzen g und h in g · h : 2 ein; hier wird erklärt, warum zwei gleiche Dreiecke ein Parallelogramm ergeben, warum die Lage der Spitze keine Rolle spielt, was ein Teilverhältnis der Grundseite bewirkt und warum +50 % und −50 % sich nicht aufheben; das Dreieck wird auch über Koordinaten berechnet."
ABG[(T, "rueckwaerts")] = "Die Übungen stellen die Flächenformel nach h oder g um; hier wird begründet, warum ein Parallelogramm einem Rechteck gleicher Fläche entspricht und zwei Trapeze ein Parallelogramm ergeben, und eine Schranke für die Fläche erkannt."
ABG[(T, "zusammengesetzt")] = "Die Übungen zerlegen eine vorgegebene Figur; hier wird eine Teilfläche rückwärts gesucht, doppelt gezählte Stücke werden erkannt, ein Viereck über Koordinaten zerlegt und Fläche und Umfang beim Zerschneiden unterschieden."
ABG[(T, "verstehen")] = "Die Übungen rechnen mit verdoppelten Maßen; hier wird erklärt, wie Fläche und Umfang beim Strecken wachsen, wie groß ein Anteil ist, wie sich ein Zuwachs der Höhe oder der Seite auswirkt und warum Höhen sich zur Breite ergänzen."
# ───────── dreieck ─────────
neu(T, "dreieck", "test", "transfer", L(
    "Im Koordinatensystem sind die Punkte A(0|0), B(10|0), C(5|4) und D(17|4) gegeben (eine Einheit ist 1 cm). Gib den Flächeninhalt der beiden Dreiecke ABC und ABD an.",
    "ABC: □ cm², ABD: □ cm²", [20, 20], ["10 * 4 / 2", "10 * 4 / 2"], ["2 * 10", "40 / 2"],
    "Beide Dreiecke haben die Grundseite AB auf der x-Achse, AB = 10 cm. Die Höhe ist für beide der Abstand von C und D zur x-Achse, also die y-Koordinate 4 cm; sie liegt bei ABD außerhalb des Dreiecks, zählt aber genauso. A = 10 · 4 : 2 = 20 cm² für beide Dreiecke. Die x-Koordinaten (5 und 17) ändern die Fläche nicht.",
    {0: [(40, "das Halbieren vergessen: 10 · 4", "10 * 4"), (10, "die x-Koordinate von C als Grundseite genommen: 5 · 4 : 2", "5 * 4 / 2")],
     1: [(34, "die x-Koordinate von D als Grundseite genommen: 17 · 4 : 2", "17 * 4 / 2"), (68, "die x-Koordinate von D als Grundseite ohne Halbieren: 17 · 4", "17 * 4")]}),
    lp=LP, idee="hoehe_ausserhalb")
neu(T, "dreieck", "korrektur", "mehrschritt", Z(
    "Das Dreieck ABC hat die Ecken A(1|1), B(9|1) und C(13|6) (eine Einheit ist 1 cm). Ben legt das kleinste Rechteck mit achsenparallelen Seiten um das Dreieck; es hat 60 cm². Dann zieht er die beiden überstehenden Dreiecke ab. Wie viele cm² muss er insgesamt von den 60 cm² abziehen?",
    40, "12 * 5 / 2 + 4 * 5 / 2", "60 - 20",
    "Das Rechteck reicht von x = 1 bis x = 13 und von y = 1 bis y = 6, es ist 12 cm breit und 5 cm hoch. Überstehend sind zwei rechtwinklige Dreiecke: eines mit den Katheten 12 und 5 (12 · 5 : 2 = 30 cm²) und eines mit den Katheten 4 und 5 (4 · 5 : 2 = 10 cm²). Zusammen sind das 40 cm². Es bleiben 60 − 40 = 20 cm², das ist die Fläche des Dreiecks.",
    [B("60 - 40", "die Fläche des Dreiecks angegeben statt der abzuziehenden Fläche"),
     B("12 * 5 / 2", "nur das große überstehende Dreieck abgezogen"),
     B("4 * 5 / 2 + 12 * 5", "das große überstehende Dreieck ohne Halbieren gerechnet")], einheit="cm²"), form="zwei_wege", lp=LP, idee="ergaenzen_rechteck")
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
    "Im Koordinatensystem ist das Dreieck ABC mit A(0|0), B(10|0) und C(3|8) gegeben (eine Einheit ist 1 cm). Die Höhe von C trifft die Seite AB im Punkt H(3|0) und zerlegt das Dreieck in zwei Teile. Ein Kind überlegt: Zeile 1: Das Dreieck ABC hat 10 · 8 : 2 = 40 cm². Zeile 2: Die Höhe zerlegt das Dreieck in zwei gleich große Teile. Zeile 3: Das Dreieck AHC hat also 20 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist das Dreieck AHC richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 12], ["2", "3 * 8 / 2"], ["3 - 1", "24 / 2"],
    "Zeile 1 stimmt. In Zeile 2 steckt der Fehler: Die Höhe halbiert das Dreieck nur, wenn sie genau in der Mitte der Grundseite steht. Hier ist AH = 3 cm und HB = 7 cm. Beide Teile haben die Höhe 8 cm, ihre Flächen verhalten sich wie die Grundseiten 3 : 7. Das Dreieck AHC hat 3 · 8 : 2 = 12 cm², das Dreieck HBC hat 7 · 8 : 2 = 28 cm², zusammen 40 cm².",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3"), (1, "Zeile 1 genannt, obwohl dort die Fläche richtig berechnet wird", "1")],
     1: [(20, "die Behauptung aus Zeile 2 übernommen und die Hälfte der Fläche genommen", "40 / 2"), (28, "die Fläche des größeren Teils statt des Dreiecks AHC angegeben", "7 * 8 / 2"), (40, "die Fläche des ganzen Dreiecks angegeben", "10 * 8 / 2")]}), form="fehler_detektiv", lp=LP, idee="hoehe_teilt_nicht_gleich")
neu(T, "dreieck", "sicherung", "begruenden", Z(
    "Ein Dreieck ABC hat den Flächeninhalt 66 cm². Auf der Seite AB liegt ein Punkt P so, dass die Strecke AP nur ein Sechstel von AB lang ist. Wie groß ist das Dreieck APC?",
    11, "66 / 6", "66 * 1 / 6",
    "Die Dreiecke APC und ABC haben dieselbe Höhe, nämlich den Abstand von C zur Geraden AB. Ihre Grundseiten AP und AB verhalten sich wie 1 : 6. Also verhalten sich auch die Flächen wie 1 : 6: 66 : 6 = 11 cm². Probe: Das Dreieck PBC hat dann 55 cm², und 11 + 55 = 66.",
    [B("66 / 3", "AP für ein Drittel von AB gehalten"),
     B("66 / 2", "AP für die Hälfte von AB gehalten"),
     B("66 - 11", "die Fläche des restlichen Dreiecks PBC angegeben")], einheit="cm²"), lp=LP, idee="teilverhaeltnis_hoehe")
neu(T, "dreieck", "sicherung", "darstellung", Z(
    "Ein Dreieck hat die Grundseite 8 cm und die Höhe 6 cm. Die Grundseite wird um die Hälfte länger, die Höhe wird um die Hälfte kürzer. Wie groß ist die neue Fläche?",
    18, "12 * 3 / 2", "8 * 6 / 2 * 3 / 4",
    "Alt: 8 · 6 : 2 = 24 cm². Neu: Die Grundseite ist 8 + 4 = 12 cm lang, die Höhe ist 6 − 3 = 3 cm. Die neue Fläche ist 12 · 3 : 2 = 18 cm². Sie ist kleiner als vorher: Mehr und weniger um dieselbe Hälfte gleichen sich nicht aus, denn die Hälfte bezieht sich auf verschiedene Ausgangswerte (1,5 · 0,5 = 0,75).",
    [B("8 * 6 / 2", "angenommen, dass sich die beiden Veränderungen aufheben und die Fläche gleich bleibt"),
     B("12 * 6 / 2", "nur die Grundseite verändert"),
     B("8 * 3 / 2", "nur die Höhe verändert")], einheit="cm²"), form="bruecke", lp=LP, idee="plus_minus_ausgleich")
# ───────── rueckwaerts ─────────
neu(T, "rueckwaerts", "test", "rueckwaerts", Z(
    "Ein Feld hat die Form eines Parallelogramms ABCD. Im Koordinatensystem (eine Einheit ist 1 m) ist A(0|0) und B(300|0); die Seite DC verläuft parallel zur x-Achse. Das Feld ist 4,5 ha groß (1 ha = 10 000 m²). Welche y-Koordinate hat der Punkt D, wenn D oberhalb der x-Achse liegt?",
    150, "4.5 * 10000 / 300", "45000 / 300",
    "4,5 ha = 45 000 m². Die Grundseite AB ist 300 m lang, die Höhe ist der Abstand der Seite DC von der x-Achse, also die y-Koordinate von D. Aus A = g · h folgt h = 45 000 : 300 = 150 m. Probe: 300 · 150 = 45 000 m².",
    [B("45000 / 300 / 2", "wie bei einem Dreieck durch 2 geteilt"),
     B("4500 / 300", "die Hektar mit dem falschen Faktor in m² umgerechnet (um eine Null zu wenig)"),
     B("4.5 / 300 * 100", "die Hektar nicht in m² umgerechnet")], einheit="m"), lp=LP, idee="hoehe_aus_flaeche")
neu(T, "rueckwaerts", "korrektur", "umkehr", Z(
    "Ein Parallelogramm hat den Flächeninhalt 50 cm². Seine Höhe ist halb so lang wie die zugehörige Grundseite. Wie lang ist die Grundseite?",
    10, "10", "100 / 10",
    "Mit g für die Grundseite ist h = g : 2. Dann gilt A = g · g : 2 = 50, also g · g = 100 und g = 10 cm. Die Höhe ist 5 cm. Probe: 10 · 5 = 50.",
    [B("50 / 10", "die Höhe 5 statt der Grundseite angegeben"),
     B("50 / 2", "50 durch 2 geteilt und als Grundseite genommen"),
     B("50 / 4", "50 durch 4 geteilt, weil von „halb“ die 2 zweimal gezählt wurde")], einheit="cm"), form="umkehren", lp=LP, idee="gleichung_g_mal_g")
neu(T, "rueckwaerts", "korrektur", "darstellung", Z(
    "Ein Parallelogramm hat die Grundseite 12 cm, die Höhe 8 cm und die schräge Nachbarseite 10 cm. Es wird zu einem Rechteck umgebaut: Ein rechtwinkliges Dreieck mit den Katheten 8 cm und 6 cm wird auf der einen Seite abgeschnitten und auf der anderen Seite wieder angesetzt. Wie groß ist die Fläche des Rechtecks?",
    96, "12 * 8", "12 * 8 - 6 * 8 / 2 + 6 * 8 / 2",
    "Das abgeschnittene Dreieck wird auf der anderen Seite wieder angesetzt, die Fläche bleibt also gleich. Das Rechteck hat dieselbe Grundseite 12 cm und dieselbe Höhe 8 cm wie das Parallelogramm: A = 12 · 8 = 96 cm². Die schräge Seite 10 cm und die Kathete 6 cm spielen für die Fläche keine Rolle. Probe: Das Dreieck hat 6 · 8 : 2 = 24 cm², es geht auf der einen Seite weg und kommt auf der anderen dazu.",
    [B("12 * 10", "die schräge Seite statt der Höhe genommen"),
     B("12 * 8 - 6 * 8 / 2", "das abgeschnittene Dreieck nicht wieder angesetzt"),
     B("12 * 8 / 2", "wie bei einem Dreieck durch 2 geteilt")], einheit="cm²"), lp=LP, idee="parallelogramm_zu_rechteck")
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
neu(T, "rueckwaerts", "sicherung", "mehrschritt", Z(
    "Für wie viele ganze Zahlen c von −5 bis 15 (einschließlich) hat das Dreieck mit den Ecken A(0|0), B(10|0) und C(c|7) den Flächeninhalt 35 cm²? (Eine Einheit ist 1 cm.)",
    21, "15 - (0 - 5) + 1", "21",
    "Die Grundseite AB ist 10 cm lang und liegt auf der x-Achse. Die Höhe ist der Abstand von C zur x-Achse, also 7 cm, ganz gleich, welche x-Koordinate c hat. Die Fläche ist immer 10 · 7 : 2 = 35 cm². Also passt jede der 15 − (−5) + 1 = 21 ganzen Zahlen von −5 bis 15.",
    [B("1", "nur die Zahl c = 5 gezählt, bei der die Spitze genau über der Mitte der Grundseite liegt"),
     B("15 - (0 - 5)", "die Zahl der Schritte statt der Zahlen gezählt"),
     B("15 + 1", "nur die Zahlen von 0 bis 15 gezählt")], einheit="Zahlen"), form="bruecke", lp=LP, idee="lage_der_spitze_zaehlen")
neu(T, "rueckwaerts", "sicherung", "begruenden", W(
    "Ein Parallelogramm hat die Seiten 10 cm und 7 cm. Kann sein Flächeninhalt 84 cm² betragen? Welche Aussage stimmt?",
    "Nein, denn die Höhe ist nicht länger als die Nachbarseite, die Fläche also höchstens 10 · 7 = 70 cm².",
    [("Ja, denn die Höhe auf die Seite 10 cm wäre dann 84 : 10 = 8,4 cm, und das ist eine mögliche Höhe.", "eine Höhe für möglich gehalten, die länger als die Nachbarseite ist"),
     ("Ja, aber nur als Rechteck, denn dann hat das Parallelogramm seine größte mögliche Fläche.", "übersehen, dass das Rechteck die größte Fläche liefert, und die Grenze trotzdem überschritten"),
     ("Ja, denn 10 · 7 = 70 ist die Mindestfläche, die jedes Parallelogramm mit diesen Seiten hat.", "höchste und niedrigste mögliche Fläche vertauscht")],
    "Die Höhe auf die Seite 10 cm ist höchstens so lang wie die andere Seite 7 cm; gleich lang ist sie nur beim Rechteck. Also ist A = 10 · h höchstens 10 · 7 = 70 cm². Das Rechteck hat die größte Fläche, ein schief gedrücktes Parallelogramm hat weniger. 84 cm² sind nicht möglich: Die Höhe müsste 8,4 cm lang sein und wäre länger als die Seite 7 cm.",
    lambda: 10 * 7 == 70 and 84 > 70 and F(84, 10) > 7), lp=LP, idee="schranke_flaeche")
# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "test", "rueckwaerts", L(
    "Eine Figur besteht aus einem Rechteck (9 cm breit, 3 cm hoch) und einem Dreieck, das darauf sitzt und ebenfalls die Grundseite 9 cm hat. Die ganze Figur hat 63 cm². Das Dreieck ist □ cm hoch, die ganze Figur ist □ cm hoch.",
    "Dreieck □ cm hoch, ganze Figur □ cm hoch", [8, 11], ["2 * (63 - 27) / 9", "3 + 8"], ["72 / 9", "11"],
    "Das Rechteck hat 9 · 3 = 27 cm². Für das Dreieck bleiben 63 − 27 = 36 cm². Aus 9 · h : 2 = 36 folgt h = 2 · 36 : 9 = 8 cm. Die ganze Figur ist 3 + 8 = 11 cm hoch. Probe: 27 + 9 · 8 : 2 = 27 + 36 = 63.",
    {0: [(4, "das Verdoppeln beim Dreieck vergessen", "(63 - 27) / 9"), (7, "die ganze Fläche durch die Grundseite geteilt, ohne das Rechteck abzuziehen", "63 / 9")],
     1: [(8, "nur die Höhe des Dreiecks angegeben", "8"), (7, "die ganze Fläche durch die Breite geteilt, ohne zu zerlegen", "63 / 9")]}), lp=LP, idee="rueckwaerts_gesamtflaeche")
neu(T, "zusammengesetzt", "korrektur", "umkehr", Z(
    "Aus einer Ecke eines Rechtecks (14 cm lang, 9 cm breit) wird ein kleines Rechteck herausgeschnitten, das 4 cm lang ist (entlang der langen Seite gemessen). Die Restfläche beträgt 102 cm². Wie breit ist das herausgeschnittene Stück (entlang der kurzen Seite gemessen)?",
    6, "(14 * 9 - 102) / 4", "24 / 4",
    "Das große Rechteck hat 14 · 9 = 126 cm². Weggenommen wurden 126 − 102 = 24 cm². Das Stück ist 4 cm lang, also ist es 24 : 4 = 6 cm breit. Probe: 126 − 4 · 6 = 102.",
    [B("102 / 4", "die Restfläche statt der weggenommenen Fläche durch 4 geteilt"),
     B("126 / 4", "die Fläche des ganzen Rechtecks durch 4 geteilt"),
     B("126 - 102", "die weggenommene Fläche 24 als Breite angegeben")], einheit="cm"), form="umkehren", lp=LP, idee="rest_rueckwaerts")
neu(T, "zusammengesetzt", "korrektur", "darstellung", L(
    "Eine rechteckige Flagge ist 12 cm lang und 8 cm hoch. Ein Kreuz aus zwei 2 cm breiten Streifen verläuft einmal über die ganze Länge und einmal über die ganze Höhe der Flagge. Wer die beiden Streifen einzeln berechnet und die Flächen addiert, rechnet □ cm² zu viel. Die Fläche des Kreuzes ist □ cm².",
    "zu viel gerechnet: □ cm², Kreuz: □ cm²", [4, 36], ["2 * 2", "12 * 2 + 8 * 2 - 2 * 2"], ["4", "96 - 10 * 6"],
    "Der waagerechte Streifen hat 12 · 2 = 24 cm², der senkrechte 8 · 2 = 16 cm², zusammen 40 cm². Das Quadrat in der Mitte (2 · 2 = 4 cm²) gehört zu beiden Streifen und wird doppelt gezählt: Man rechnet 4 cm² zu viel. Das Kreuz hat 40 − 4 = 36 cm². Kontrolle: Außerhalb des Kreuzes liegen vier Ecken, zusammen (12 − 2) · (8 − 2) = 60 cm², und 96 − 60 = 36 cm².",
    {0: [(2, "die Breite eines Streifens als doppelt gezählte Fläche genommen", "2"), (8, "das Quadrat in der Mitte zweimal gerechnet", "2 * 2 * 2")],
     1: [(40, "die beiden Streifen einfach addiert", "12 * 2 + 8 * 2"), (32, "das Quadrat in der Mitte zweimal abgezogen", "12 * 2 + 8 * 2 - 2 * 2 * 2"), (24, "nur den langen Streifen berechnet", "12 * 2")]}),
    lp=LP, idee="flaggenkreuz")
neu(T, "zusammengesetzt", "korrektur", "darstellung", W(
    "Ein Rechteck (10 cm lang, 6 cm breit) wird mit einem geraden Schnitt in zwei Rechtecke zerlegt, die 2 cm und 4 cm breit sind. Welche Aussage stimmt?",
    "Die Flächen der beiden Teile ergeben zusammen 60 cm², ihre Umfänge zusammen sind aber größer als der Umfang des Rechtecks, denn an der Schnittlinie kommen zwei Randstücke dazu.",
    [("Flächen und Umfänge der beiden Teile ergeben zusammen genau die Werte des ganzen Rechtecks, denn beim Zerschneiden geht nichts verloren und es kommt nichts dazu.", "Fläche und Umfang gleich behandelt; die Schnittkanten zählen bei beiden Teilen zum Rand"),
     ("Die Flächen der beiden Teile ergeben zusammen weniger als 60 cm², denn an der Schnittlinie geht etwas verloren.", "geglaubt, beim Schneiden gehe Fläche verloren"),
     ("Die Umfänge der beiden Teile ergeben zusammen genau den Umfang des Rechtecks, aber die Flächen sind zusammen größer als 60 cm², denn jedes Teil wird einzeln gemessen.", "Fläche und Umfang vertauscht")],
    "Das Rechteck hat 10 · 6 = 60 cm² und den Umfang 2 · (10 + 6) = 32 cm. Die Teile haben 10 · 2 = 20 cm² und 10 · 4 = 40 cm², zusammen 60 cm². Ihre Umfänge sind 2 · (10 + 2) = 24 cm und 2 · (10 + 4) = 28 cm, zusammen 52 cm und damit mehr als 32 cm: Die Schnittlinie (10 cm) zählt bei beiden Teilen zum Rand.",
    lambda: 10 * 6 == 10 * 2 + 10 * 4 and 2 * (10 + 2) + 2 * (10 + 4) == 52 and 52 > 2 * (10 + 6) and 10 * 2 + 10 * 4 == 60), form="bruecke", lp=LP, idee="schnitt_umfang")
neu(T, "zusammengesetzt", "sicherung", "fehler", L(
    "Aus einem Rechteck (14 cm lang, 10 cm breit) wird an einer Ecke ein kleines Rechteck (6 cm · 4 cm) herausgeschnitten. Ein Kind rechnet: Zeile 1: Das große Rechteck hat 14 · 10 = 140 cm². Zeile 2: Das kleine Rechteck hat 6 · 4 = 24 cm² und wird zum großen dazugezählt. Zeile 3: Also hat die Figur 140 + 24 = 164 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist die Figur richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 116], ["2", "14 * 10 - 6 * 4"], ["3 - 1", "116"],
    "Zeile 1 stimmt. In Zeile 2 steckt der Fehler: Das herausgeschnittene Stück fehlt in der Figur und muss abgezogen werden. Richtig: 140 − 24 = 116 cm². Zeile 3 rechnet mit dem falschen Vorzeichen weiter.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3"), (1, "Zeile 1 genannt, obwohl dort die Rechteckfläche richtig steht", "1")],
     1: [(164, "das herausgeschnittene Stück dazugezählt statt abgezogen", "14 * 10 + 6 * 4"), (24, "nur die Fläche des herausgeschnittenen Stücks angegeben", "6 * 4"), (136, "nur die Höhe des Stücks abgezogen", "14 * 10 - 4")]}), form="fehler_detektiv", lp=LP, idee="ergaenzen_vorzeichen")
neu(T, "zusammengesetzt", "sicherung", "darstellung", W(
    "Eine Figur ist 9 cm breit und 7 cm hoch. Unten rechts fehlt ein Rechteck von 3 cm Breite und 2 cm Höhe. Welche Rechnung gibt den Flächeninhalt der Figur in cm² richtig an?",
    "6 · 7 + 3 · 5",
    [("9 · 7 − 3 · 5", "das fehlende Stück falsch bemessen: Es ist 2 cm hoch, nicht 5 cm"),
     ("6 · 7 + 3 · 2", "das rechte Stück mit der Höhe des fehlenden Stücks gerechnet statt mit der Resthöhe"),
     ("9 · 5 + 3 · 2", "das fehlende Stück dazugezählt statt weggelassen")],
    "Die Figur lässt sich in zwei Rechtecke zerlegen: links 6 cm breit und 7 cm hoch, rechts 3 cm breit und 7 − 2 = 5 cm hoch. Das ergibt 6 · 7 + 3 · 5 = 42 + 15 = 57 cm². Gleichwertig ist die Ergänzung: 9 · 7 − 3 · 2 = 63 − 6 = 57 cm².",
    lambda: 6 * 7 + 3 * 5 == 9 * 7 - 3 * 2 == 57 and 9 * 7 - 3 * 5 != 57 and 6 * 7 + 3 * 2 != 57 and 9 * 5 + 3 * 2 != 57), lp=LP, idee="zerlegen_rechnungen")
neu(T, "zusammengesetzt", "sicherung", "transfer", Z(
    "Das Viereck ABCD hat die Ecken A(0|0), B(6|0), C(8|5) und D(0|3) (eine Einheit ist 1 cm). Die Ecke D wird um 2 cm nach oben auf (0|5) verschoben, die anderen drei Ecken bleiben. Um wie viel cm² wächst die Fläche?",
    8, "2 * 8 / 2", "(15 + 5 * 8 / 2) - 27",
    "Die Diagonale AC teilt das Viereck in die Dreiecke ABC und ACD. Das Dreieck ABC bleibt unverändert (6 · 5 : 2 = 15 cm²). Beim Dreieck ACD liegt die Grundseite AD auf der y-Achse und wird 2 cm länger, die Höhe ist die x-Koordinate von C, also 8 cm. Die Fläche wächst um 2 · 8 : 2 = 8 cm². Kontrolle: vorher 15 + 3 · 8 : 2 = 27 cm², nachher 15 + 5 · 8 : 2 = 35 cm².",
    [B("2 * 8", "das Halbieren vergessen"),
     B("2 * 5 / 2", "die y-Koordinate von C statt der x-Koordinate als Höhe genommen"),
     B("15 + 5 * 8 / 2", "die neue Fläche statt des Zuwachses angegeben")], einheit="cm²"), lp=LP, idee="koordinaten_viereck")
# ───────── verstehen ─────────
neu(T, "verstehen", "test", "transfer", L(
    "Ein Rechteck ist 10 cm lang und 5 cm breit. Jede Seite wird um 20 % länger. Die Fläche wird dadurch um □ % größer, der Umfang um □ cm größer.",
    "Fläche □ % größer, Umfang □ cm größer", [44, 6], ["(12 * 6 - 50) * 2", "2 * 2 + 2 * 1"], ["144 - 100", "36 - 30"],
    "Die neuen Seiten sind 12 cm und 6 cm lang. Die Fläche wird 12 · 6 = 72 cm² statt 10 · 5 = 50 cm². Die Zunahme ist 22 cm², das sind 22 : 50 = 0,44 = 44 %. Der Umfang wird 2 · (12 + 6) = 36 cm statt 30 cm, er wächst um 6 cm (um 20 %). Die Fläche wächst stärker als die Seiten, weil beide Seiten länger werden: 1,2 · 1,2 = 1,44.",
    {0: [(20, "die Prozentzahl der Seiten für die Fläche übernommen", "20"), (40, "die beiden Prozentsätze der Länge und der Breite addiert", "20 + 20")],
     1: [(3, "nur die Zunahme einer Länge und einer Breite gezählt", "2 + 1"), (4, "nur die Zunahme der beiden Längen gezählt", "2 + 2")]}), lp=LP, idee="streckung_prozent")
neu(T, "verstehen", "korrektur", "darstellung", Z(
    "Ein Trapez mit den parallelen Seiten 12 cm und 6 cm und der Höhe 4 cm liegt in einem Rechteck, das 12 cm lang und 4 cm hoch ist. Wie viel Prozent des Rechtecks füllt das Trapez aus?",
    75, "(12 + 6) * 4 / 2 * 100 / (12 * 4)", "36 / 48 * 100",
    "Das Trapez hat (12 + 6) · 4 : 2 = 36 cm², das Rechteck hat 12 · 4 = 48 cm². Der Anteil ist 36 : 48 = 3/4 = 75 %. Die übrigen 25 % sind die beiden Dreiecke an den Seiten.",
    [B("25", "den freien Rest statt des ausgefüllten Teils angegeben"),
     B("50", "angenommen, das Trapez fülle genau die Hälfte aus"),
     B("(12 + 6) * 4 / 2", "die Fläche des Trapezes statt des Anteils angegeben")], einheit="%"), lp=LP, idee="anteil_im_rechteck")
neu(T, "verstehen", "korrektur", "umkehr", Z(
    "Bei einem Parallelogramm ist die Höhe 3 cm kürzer als die Grundseite. Der Flächeninhalt beträgt 54 cm². Wie lang ist die Grundseite?",
    9, "9", "6 + 3",
    "Gesucht sind zwei Zahlen g und h mit g · h = 54, die sich um 3 unterscheiden. Mögliche Paare: 1 · 54, 2 · 27, 3 · 18, 6 · 9. Nur 9 und 6 unterscheiden sich um 3. Also ist die Grundseite 9 cm lang und die Höhe 6 cm. Probe: 9 · 6 = 54 und 9 − 6 = 3.",
    [B("6", "die Höhe statt der Grundseite angegeben"),
     B("54 / 3", "durch den Unterschied geteilt"),
     B("6 + 3 + 3", "den Unterschied zweimal addiert")], einheit="cm"), form="umkehren", lp=LP, idee="differenz_paar")
neu(T, "verstehen", "korrektur", "umkehr", Z(
    "Ein Dreieck hat die Grundseite 16 cm. Seine Höhe wird um 1 cm länger. Um wie viel cm² wächst die Fläche?",
    8, "16 * 1 / 2", "56 - 48",
    "Die Fläche ist g · h : 2. Wird die Höhe um 1 cm länger, wächst die Fläche um 16 · 1 : 2 = 8 cm², ganz gleich, wie hoch das Dreieck vorher war. Beispiel: Bei h = 6 cm sind es 16 · 6 : 2 = 48 cm², bei h = 7 cm sind es 16 · 7 : 2 = 56 cm², das sind 8 cm² mehr.",
    [B("16", "das Halbieren vergessen"),
     B("1", "den Zuwachs der Höhe als Zuwachs der Fläche genommen"),
     B("16 / 2 + 1", "zum Zuwachs der Fläche noch den Zuwachs der Höhe addiert")], einheit="cm²"), lp=LP, idee="zuwachs_dreieck")
neu(T, "verstehen", "sicherung", "fehler", L(
    "Ein Rechteck ABCD hat die Ecken A(0|0), B(14|0), C(14|6) und D(0|6) (eine Einheit ist 1 cm). Der Punkt M ist die Mitte der Seite BC. Ein Kind überlegt: Zeile 1: Das Rechteck hat 14 · 6 = 84 cm². Zeile 2: Die Strecke von A nach M teilt das Rechteck in zwei gleich große Teile. Zeile 3: Das Dreieck ABM hat also 42 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist das Dreieck ABM richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 21], ["2", "14 * 3 / 2"], ["3 - 1", "84 / 4"],
    "Zeile 1 stimmt. In Zeile 2 steckt der Fehler: Nur die Diagonale von A nach C halbiert das Rechteck. Die Strecke AM führt zur Mitte der Seite BC und schneidet ein kleineres Stück ab. Das Dreieck ABM hat die Grundseite AB = 14 cm und die Höhe BM = 3 cm: 14 · 3 : 2 = 21 cm², ein Viertel des Rechtecks. Der Rest, das Trapez AMCD, hat 63 cm².",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3"), (1, "Zeile 1 genannt, obwohl dort die Rechteckfläche richtig steht", "1")],
     1: [(42, "die Hälfte des Rechtecks als Fläche des Dreiecks übernommen", "84 / 2"), (63, "die Fläche des Trapezes AMCD statt des Dreiecks angegeben", "84 - 14 * 3 / 2"), (84, "die Fläche des ganzen Rechtecks angegeben", "14 * 6")]}), form="fehler_detektiv", lp=LP, idee="strecke_halbiert_nicht")
neu(T, "verstehen", "sicherung", "begruenden", W(
    "In einem Rechteck (12 cm lang, 8 cm breit) liegt ein Punkt P. Er wird mit allen vier Ecken verbunden, dabei entstehen vier Dreiecke. Welche Aussage über die beiden Dreiecke, die an den langen Seiten liegen, stimmt?",
    "Sie haben zusammen immer 48 cm², egal wo P liegt, denn ihre Höhen ergeben zusammen die Breite 8 cm.",
    [("Sie haben zusammen nur dann 48 cm², wenn P in der Mitte liegt, denn sonst sind ihre Höhen verschieden.", "gedacht, verschiedene Höhen änderten die Summe der Flächen; die Höhen ergeben immer zusammen die Breite"),
     ("Sie haben zusammen immer 24 cm², egal wo P liegt, denn jedes Dreieck ist ein Viertel des Rechtecks.", "angenommen, die vier Dreiecke seien gleich groß"),
     ("Sie haben zusammen 96 cm², denn sie füllen das ganze Rechteck aus.", "vergessen, dass noch zwei weitere Dreiecke an den kurzen Seiten liegen")],
    "Die beiden Dreiecke haben je die Grundseite 12 cm. Ihre Höhen sind die Abstände von P zu den beiden langen Seiten und ergeben zusammen die Breite 8 cm. Die Flächen sind 12 · h₁ : 2 und 12 · h₂ : 2, zusammen 12 · (h₁ + h₂) : 2 = 12 · 8 : 2 = 48 cm², also die Hälfte des Rechtecks, wo P auch liegt.",
    lambda: all(F(12 * y, 2) + F(12 * (8 - y), 2) == 48 for y in range(1, 8)) and 48 * 2 == 12 * 8), lp=LP, idee="hoehen_ergaenzen")
neu(T, "verstehen", "sicherung", "darstellung", Z(
    "Ein Quadrat wird auf jeder Seite um 1 cm länger. Dadurch wächst seine Fläche um 25 cm². Wie lang war die Seite vorher?",
    12, "(25 - 1) / 2", "(25 + 1) / 2 - 1",
    "Die alte Seite sei a. Die neue Fläche ist (a + 1) · (a + 1), die alte a · a. Der Zuwachs besteht aus zwei Streifen (a · 1 und a · 1) und einem kleinen Eckquadrat (1 · 1): 2a + 1 = 25. Also ist 2a = 24 und a = 12 cm. Probe: 13 · 13 − 12 · 12 = 169 − 144 = 25.",
    [B("25", "den Zuwachs als Seitenlänge genommen"),
     B("25 - 1", "das Eckquadrat abgezogen, aber nicht durch 2 geteilt"),
     B("(25 - 1) / 2 + 1", "die neue Seitenlänge statt der alten angegeben")], einheit="cm"), form="bruecke", lp=LP, idee="zuwachs_quadrat")
