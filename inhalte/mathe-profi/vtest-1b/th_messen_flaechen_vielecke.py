T = "messen.flaechen_vielecke"
LP = "M6 2 Flächeninhalt und Volumen (Flächeninhalt von Parallelogramm, Dreieck und Trapez; zusammengesetzte Figuren)"
REGEL[(T, "dreieck")] = REGEL[(T, "zusammengesetzt")] = REGEL[(T, "verstehen")] = "id.flaeche_raum.aus_dem_rechteck"
REGEL[(T, "rueckwaerts")] = "id.flaeche_raum.aus_dem_rechteck"
ABG[(T, "dreieck")] = "Die Übungen setzen g und h in g · h : 2 ein; hier wird das Mittendreieck bestimmt, Teilverhältnisse der Grundseite genutzt, die Fläche bei +50 % und −50 % verglichen, die Höhe als Teiler geprüft und die Zerlegung eines Parallelogramms gelesen."
ABG[(T, "rueckwaerts")] = "Die Übungen stellen die Flächenformel nach h oder g um; hier werden Verhältnisse und Einheiten einbezogen, ein Parallelogramm zu einem Rechteck umgebaut, Gleichungen mit g · g gelöst und Ganzzahligkeit untersucht."
ABG[(T, "zusammengesetzt")] = "Die Übungen zerlegen eine vorgegebene Figur; hier wird eine Überlappung zurückgerechnet, eine Rahmenbreite gesucht, ein Eckdreieck über Ergänzen bestimmt, Fläche und Umfang beim Zerschneiden unterschieden und ein Viereck über Koordinaten verändert."
ABG[(T, "verstehen")] = "Die Übungen rechnen mit verdoppelten Maßen; hier wird erklärt, warum gegenüberliegende Dreiecke zusammen die halbe Fläche haben, wie sich ein Zuwachs der Höhe oder der Seite auswirkt und warum eine Strecke eine Fläche nicht halbiert."
# ───────── dreieck ─────────
# ───────── dreieck ─────────
# ───────── dreieck ─────────
neu(T, "dreieck", "test", "transfer", Z(
    "Das Dreieck ABC hat den Flächeninhalt 96 cm². Die Punkte M, N und P sind die Mitten der Seiten AB, AC und BC. Wie groß ist das Dreieck MNP?",
    24, "96 / 4", "96 - 3 * 96 / 4",
    "Die drei Strecken MN, NP und MP zerlegen das Dreieck ABC in vier gleich große Dreiecke: Jede Strecke ist halb so lang wie die gegenüberliegende Seite, und die drei Eckdreiecke AMN, MBP und NPC sind deckungsgleich mit dem mittleren Dreieck MNP. Also hat MNP genau ein Viertel der Fläche: 96 : 4 = 24 cm². Probe: 4 · 18 cm² = 96 cm².",
    [B("96 / 2", "die Hälfte der Fläche angenommen"),
     B("96 / 3", "ein Drittel der Fläche angenommen, weil drei Mittelpunkte gegeben sind"),
     B("96 / 8", "ein Achtel der Fläche angenommen")], einheit="cm²"), lp=LP, idee="mittendreieck")

neu(T, "dreieck", "korrektur", "mehrschritt", Z(
    "Ein Dreieck ABC hat den Flächeninhalt 66 cm². Auf der Seite AB liegt ein Punkt P so, dass die Strecke AP nur ein Sechstel von AB lang ist. Wie groß ist das Dreieck APC?",
    11, "66 / 6", "66 * 1 / 6",
    "Die Dreiecke APC und ABC haben dieselbe Höhe, nämlich den Abstand von C zur Geraden AB. Ihre Grundseiten AP und AB verhalten sich wie 1 : 6. Also verhalten sich auch die Flächen wie 1 : 6: 66 : 6 = 11 cm². Probe: Das Dreieck PBC hat dann 55 cm², und 11 + 55 = 66.",
    [B("66 / 3", "AP für ein Drittel von AB gehalten"),
     B("66 / 2", "AP für die Hälfte von AB gehalten"),
     B("66 - 11", "die Fläche des restlichen Dreiecks PBC angegeben")], einheit="cm²"), form="bruecke", lp=LP, idee="teilverhaeltnis_hoehe")

neu(T, "dreieck", "korrektur", "darstellung", Z(
    "Ein Dreieck hat die Grundseite 8 cm und die Höhe 6 cm. Die Grundseite wird um die Hälfte länger, die Höhe wird um die Hälfte kürzer. Wie groß ist die neue Fläche?",
    18, "12 * 3 / 2", "8 * 6 / 2 * 3 / 4",
    "Alt: 8 · 6 : 2 = 24 cm². Neu: Die Grundseite ist 8 + 4 = 12 cm lang, die Höhe ist 6 − 3 = 3 cm. Die neue Fläche ist 12 · 3 : 2 = 18 cm². Sie ist kleiner als vorher: Mehr und weniger um dieselbe Hälfte gleichen sich nicht aus, denn die Hälfte bezieht sich auf verschiedene Ausgangswerte (1,5 · 0,5 = 0,75).",
    [B("8 * 6 / 2", "angenommen, dass sich die beiden Veränderungen aufheben und die Fläche gleich bleibt"),
     B("12 * 6 / 2", "nur die Grundseite verändert"),
     B("8 * 3 / 2", "nur die Höhe verändert")], einheit="cm²"), form="bruecke", lp=LP, idee="plus_minus_ausgleich")

neu(T, "dreieck", "sicherung", "fehler", L(
    "Im Koordinatensystem ist das Dreieck ABC mit A(0|0), B(10|0) und C(3|8) gegeben (eine Einheit ist 1 cm). Die Höhe von C trifft die Seite AB im Punkt H(3|0) und zerlegt das Dreieck in zwei Teile. Ein Kind überlegt: Zeile 1: Das Dreieck ABC hat 10 · 8 : 2 = 40 cm². Zeile 2: Die Höhe zerlegt das Dreieck in zwei gleich große Teile. Zeile 3: Das Dreieck AHC hat also 20 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist das Dreieck AHC richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 12], ["2", "3 * 8 / 2"], ["3 - 1", "24 / 2"],
    "Zeile 1 stimmt. In Zeile 2 steckt der Fehler: Die Höhe halbiert das Dreieck nur, wenn sie genau in der Mitte der Grundseite steht. Hier ist AH = 3 cm und HB = 7 cm. Beide Teile haben die Höhe 8 cm, ihre Flächen verhalten sich wie die Grundseiten 3 : 7. Das Dreieck AHC hat 3 · 8 : 2 = 12 cm², das Dreieck HBC hat 7 · 8 : 2 = 28 cm², zusammen 40 cm².",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3"), (1, "Zeile 1 genannt, obwohl dort die Fläche richtig berechnet wird", "1")],
     1: [(20, "die Behauptung aus Zeile 2 übernommen und die Hälfte der Fläche genommen", "40 / 2"), (28, "die Fläche des größeren Teils statt des Dreiecks AHC angegeben", "7 * 8 / 2"), (40, "die Fläche des ganzen Dreiecks angegeben", "10 * 8 / 2")]}), form="fehler_detektiv", lp=LP, idee="hoehe_teilt_nicht_gleich")

neu(T, "dreieck", "sicherung", "darstellung", Z(
    "Zwei gleiche Dreiecke werden so aneinandergelegt, dass ein Parallelogramm mit der Grundseite 12 cm und der Höhe 7 cm entsteht. Wie groß ist die Fläche eines der beiden Dreiecke?",
    42, "12 * 7 / 2", "84 / 2",
    "Das Parallelogramm hat A = 12 · 7 = 84 cm². Es besteht aus zwei gleichen Dreiecken, jedes hat also die Hälfte: 84 : 2 = 42 cm². Genau deshalb wird bei der Dreiecksformel g · h durch 2 geteilt.",
    [B("12 * 7", "die Fläche des ganzen Parallelogramms angegeben"),
     B("12 + 7", "Grundseite und Höhe addiert"),
     B("12 * 7 / 4", "durch 4 statt durch 2 geteilt")], einheit="cm²"), lp=LP, idee="zwei_dreiecke_parallelogramm")


# ───────── rueckwaerts ─────────
neu(T, "rueckwaerts", "test", "rueckwaerts", Z(
    "Ein Trapez hat die Höhe 6 cm und den Flächeninhalt 60 cm². Die parallelen Seiten verhalten sich wie 3 : 2. Wie lang ist die längere parallele Seite?",
    12, "(2 * 60 / 6) * 3 / 5", "20 * 3 / 5",
    "Aus A = (a + c) · h : 2 folgt a + c = 2 · A : h = 120 : 6 = 20 cm. Die 20 cm werden im Verhältnis 3 : 2 geteilt, das sind 5 Teile zu je 4 cm. Die längere Seite hat 3 Teile: a = 12 cm, die kürzere c = 8 cm. Probe: (12 + 8) · 6 : 2 = 60 cm².",
    [B("(2 * 60 / 6) * 2 / 5", "die kürzere der beiden Seiten angegeben"),
     B("2 * 60 / 6", "die Summe der beiden parallelen Seiten als längere Seite genommen"),
     B("2 * 60 / 6 / 2", "beide Seiten gleich lang angenommen, also die halbe Summe")], einheit="cm"), lp=LP, idee="trapez_verhaeltnis")

neu(T, "rueckwaerts", "korrektur", "einkleidung", Z(
    "Ein dreieckiges Segel hat den Flächeninhalt 6 m². Seine Höhe ist 250 cm. Wie lang ist die zugehörige Grundseite in Zentimetern?",
    480, "2 * 6 / 2.5 * 100", "120000 / 250",
    "Aus A = g · h : 2 folgt g = 2 · A : h. Die Maße müssen in derselben Einheit stehen: 6 m² = 60 000 cm², also g = 2 · 60 000 cm² : 250 cm = 480 cm. Probe in Metern: 4,8 m · 2,5 m : 2 = 6 m².",
    [B("2 * 6 / 2.5 * 10", "mit einem um eine Zehnerpotenz zu kleinen Faktor von Metern auf Zentimeter umgerechnet"),
     B("6 / 2.5 * 100", "die Fläche nicht verdoppelt, weil das Dreieck als Rechteck behandelt wurde"),
     B("2 * 6 / 2.5 * 1000", "mit einem um eine Zehnerpotenz zu großen Faktor umgerechnet")], einheit="cm"), form="bruecke", lp=LP, idee="einheit_segel")

neu(T, "rueckwaerts", "korrektur", "umkehr", Z(
    "Ein Parallelogramm und ein Dreieck haben dieselbe Grundseite und dieselbe Höhe 8 cm. Das Parallelogramm ist 28 cm² größer als das Dreieck. Wie lang ist die Grundseite?",
    7, "2 * 28 / 8", "28 / (8 - 4)",
    "Das Parallelogramm hat g · 8 cm², das Dreieck g · 8 : 2 = g · 4 cm². Der Unterschied ist g · 8 − g · 4 = g · 4 cm², also die Hälfte des Parallelogramms. Aus g · 4 = 28 folgt g = 7 cm. Probe: Parallelogramm 54 cm², Dreieck 28 cm², Unterschied 28 cm².",
    [B("28 * 2", "die Fläche des Parallelogramms als Grundseite genommen"),
     B("28 - 8", "den Unterschied der Flächen um die Höhe vermindert"),
     B("28 / 4 * 2", "mit dem Vierfachen statt mit der Höhe 8 gerechnet")], einheit="cm"), lp=LP, idee="differenz_flaechen_g")

neu(T, "rueckwaerts", "sicherung", "umkehr", Z(
    "Ein Parallelogramm hat den Flächeninhalt 50 cm². Seine Höhe ist halb so lang wie die zugehörige Grundseite. Wie lang ist die Grundseite?",
    10, "10", "100 / 10",
    "Mit g für die Grundseite ist h = g : 2. Dann gilt A = g · g : 2 = 50, also g · g = 100 und g = 10 cm. Die Höhe ist 5 cm. Probe: 10 · 5 = 50.",
    [B("50 / 10", "die Höhe 5 statt der Grundseite angegeben"),
     B("50 / 2", "50 durch 2 geteilt und als Grundseite genommen"),
     B("50 / 4", "50 durch 4 geteilt, weil von „halb“ die 2 zweimal gezählt wurde")], einheit="cm"), form="umkehren", lp=LP, idee="gleichung_g_mal_g")

neu(T, "rueckwaerts", "sicherung", "parameter", Z(
    "Ein Dreieck hat die Grundseite 9 cm. Für wie viele ganze Höhen h von 1 cm bis 16 cm ist sein Flächeninhalt eine ganze Zahl in cm²?",
    8, "16 / 2", "4 * 2",
    "Die Fläche ist 9 · h : 2. Weil 9 ungerade ist, muss h gerade sein, damit durch 2 ohne Rest geteilt werden kann. Gerade Höhen von 1 bis 20 sind 2, 4, 6, …, 16, das sind 8. Bei ungeradem h kommt eine halbe Zahl heraus, etwa 4,5 cm² für h = 1.",
    [B("16", "alle Höhen gezählt, obwohl bei ungeraden Höhen eine halbe Zahl herauskommt"),
     B("16 / 4", "nur die durch eine größere Zahl teilbaren Höhen gezählt"),
     B("16 / 2 - 1", "die größte gerade Höhe nicht mitgezählt")], einheit="Höhen"), lp=LP, idee="ganzzahl_dreieck")


# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "test", "rueckwaerts", Z(
    "Zwei Quadrate mit den Seitenlängen 8 cm und 6 cm liegen so übereinander, dass ihre gemeinsame Fläche wieder ein Quadrat ist. Zusammen bedecken sie 91 cm². Wie lang ist die Seite des gemeinsamen Quadrats?",
    3, "(8 * 8 + 6 * 6 - 91) / 3", "3",
    "Die beiden Flächen 64 cm² und 36 cm² ergeben zusammen 100 cm². Das gemeinsame Stück wurde dabei doppelt gezählt. Bedeckt sind nur 91 cm², also ist das gemeinsame Quadrat 100 cm² − 91 cm² = 9 cm² groß. Seine Seite ist 3 cm, denn 3 · 3 = 9. Probe: 64 + 36 − 9 = 91.",
    [B("8 * 8 + 6 * 6 - 91", "die Fläche des gemeinsamen Quadrats als Seitenlänge angegeben"),
     B("91 - 64", "nur die Fläche des großen Quadrats vom Ergebnis abgezogen"),
     B("8 - 6", "den Unterschied der Seitenlängen genommen")], einheit="cm"), lp=LP, idee="ueberlappung")

neu(T, "zusammengesetzt", "korrektur", "umkehr", Z(
    "Ein Bilderrahmen ist außen 20 cm breit und 16 cm hoch und überall gleich breit. Die freie Bildfläche innen ist 192 cm² groß. Wie breit ist der Rahmen?",
    2, "(20 - 16) / 2", "(16 - 12) / 2",
    "Ist x die Rahmenbreite, so ist das Bild (20 − 2x) cm breit und (16 − 2x) cm hoch. Probiert man x = 2, dann ist das Bild 16 cm breit und 12 cm hoch, und 16 · 12 = 192 cm². Also ist der Rahmen 2 cm breit. Die Rahmenfläche ist 20 · 16 − 192 = 128 cm².",
    [B("20 - 16", "den Unterschied der Außenmaße als Rahmenbreite genommen"),
     B("(20 - 16) / 4", "den Unterschied der Außenmaße geviertelt"),
     B("(20 - 16) / 2 + 1", "eine Rahmenbreite zu viel angenommen")], einheit="cm"), form="umkehren", lp=LP, idee="rahmen_breite")

neu(T, "zusammengesetzt", "korrektur", "mehrschritt", Z(
    "In einem Rechteck ABCD (12 cm lang, 8 cm hoch) ist M die Mitte der Seite BC und N die Mitte der Seite CD. Wie groß ist das Dreieck AMN?",
    36, "12 * 8 - 24 - 12 - 24", "96 - 60",
    "Das Rechteck hat 12 · 8 = 96 cm². Außerhalb des Dreiecks AMN liegen drei Dreiecke: ABM mit 12 · 4 : 2 = 24 cm², MCN mit 4 · 6 : 2 = 12 cm² und ADN mit 8 · 6 : 2 = 24 cm². Zusammen sind das 60 cm². Das Dreieck AMN hat 96 − 60 = 36 cm².",
    [B("12 * 8 / 2", "die Hälfte des Rechtecks angenommen"),
     B("24 + 12 + 24", "die drei Ergänzungsdreiecke zusammen statt des Rests angegeben"),
     B("12 * 8 / 4", "ein Viertel des Rechtecks angenommen")], einheit="cm²"), form="bruecke", lp=LP, idee="eck_dreieck")

neu(T, "zusammengesetzt", "sicherung", "darstellung", W(
    "Ein Rechteck wird mit einem geraden Schnitt parallel zu einer Seite in zwei Rechtecke zerlegt. Welche Aussage über Fläche und Umfang stimmt immer?",
    "Die beiden Teile haben zusammen dieselbe Fläche wie das Rechteck, aber einen größeren Umfang, denn der Schnitt gehört zum Rand beider Teile.",
    [("Die beiden Teile haben zusammen dieselbe Fläche und denselben Umfang wie das Rechteck, denn beim Zerschneiden geht nichts verloren.", "gedacht, auch der Umfang bleibe beim Zerschneiden erhalten"),
     ("Die beiden Teile haben zusammen denselben Umfang, aber eine größere Fläche als das Rechteck, denn an der Schnittstelle kommt Fläche dazu.", "Fläche und Umfang verwechselt"),
     ("Die beiden Teile haben zusammen eine kleinere Fläche und einen kleineren Umfang, denn der Schnitt nimmt etwas weg.", "gedacht, der Schnitt entferne Fläche und Rand")],
    "Die Fläche bleibt beim Zerschneiden erhalten, denn die zwei Teile füllen das Rechteck genau aus. Beim Umfang kommt die Schnittlinie dazu, und zwar zweimal, weil sie bei beiden Teilen am Rand liegt. Beispiel: Ein Rechteck 10 cm · 6 cm hat 60 cm² und den Umfang 32 cm. Geschnitten in 4 cm und 6 cm Breite entstehen zusammen 60 cm², aber die Umfänge 20 cm und 24 cm, zusammen 44 cm.",
    lambda: all(a * b == x * b + (a - x) * b and 2 * (x + b) + 2 * (a - x + b) == 2 * (a + b) + 2 * b > 2 * (a + b) for a in (10, 7, 12) for b in (6, 3, 5) for x in (1, 2, 4))), form="bruecke", lp=LP, idee="schnitt_umfang")

neu(T, "zusammengesetzt", "sicherung", "transfer", Z(
    "Das Viereck ABCD hat die Ecken A(0|0), B(6|0), C(8|5) und D(0|3) (eine Einheit ist 1 cm). Die Ecke D wird um 2 cm nach oben auf (0|5) verschoben, die anderen drei Ecken bleiben. Um wie viel cm² wächst die Fläche?",
    8, "2 * 8 / 2", "(15 + 5 * 8 / 2) - 27",
    "Die Diagonale AC teilt das Viereck in die Dreiecke ABC und ACD. Das Dreieck ABC bleibt unverändert (6 · 5 : 2 = 15 cm²). Beim Dreieck ACD liegt die Grundseite AD auf der y-Achse und wird 2 cm länger, die Höhe ist die x-Koordinate von C, also 8 cm. Die Fläche wächst um 2 · 8 : 2 = 8 cm². Kontrolle: vorher 15 + 3 · 8 : 2 = 27 cm², nachher 15 + 5 · 8 : 2 = 35 cm².",
    [B("2 * 8", "das Halbieren vergessen"),
     B("2 * 5 / 2", "die y-Koordinate von C statt der x-Koordinate als Höhe genommen"),
     B("15 + 5 * 8 / 2", "die neue Fläche statt des Zuwachses angegeben")], einheit="cm²"), lp=LP, idee="koordinaten_viereck")


# ───────── verstehen ─────────
neu(T, "verstehen", "test", "begruenden", W(
    "In einem Rechteck (12 cm lang, 8 cm breit) liegt ein Punkt P. Er wird mit allen vier Ecken verbunden, dabei entstehen vier Dreiecke. Welche Aussage über die beiden Dreiecke, die an den langen Seiten liegen, stimmt?",
    "Sie haben zusammen immer 48 cm², egal wo P liegt, denn ihre Höhen ergeben zusammen die Breite 8 cm.",
    [("Sie haben zusammen nur dann 48 cm², wenn P in der Mitte liegt, denn sonst sind ihre Höhen verschieden.", "gedacht, verschiedene Höhen änderten die Summe der Flächen; die Höhen ergeben immer zusammen die Breite"),
     ("Sie haben zusammen immer 24 cm², egal wo P liegt, denn jedes Dreieck ist ein Viertel des Rechtecks.", "angenommen, die vier Dreiecke seien gleich groß"),
     ("Sie haben zusammen 96 cm², denn sie füllen das ganze Rechteck aus.", "vergessen, dass noch zwei weitere Dreiecke an den kurzen Seiten liegen")],
    "Die beiden Dreiecke haben je die Grundseite 12 cm. Ihre Höhen sind die Abstände von P zu den beiden langen Seiten und ergeben zusammen die Breite 8 cm. Die Flächen sind 12 · h₁ : 2 und 12 · h₂ : 2, zusammen 12 · (h₁ + h₂) : 2 = 12 · 8 : 2 = 48 cm², also die Hälfte des Rechtecks, wo P auch liegt.",
    lambda: all(F(12 * y, 2) + F(12 * (8 - y), 2) == 48 for y in range(1, 8)) and 48 * 2 == 12 * 8), lp=LP, idee="hoehen_ergaenzen")

neu(T, "verstehen", "korrektur", "umkehr", Z(
    "Bei einem Parallelogramm ist die Höhe 3 cm kürzer als die Grundseite. Der Flächeninhalt beträgt 54 cm². Wie lang ist die Grundseite?",
    9, "9", "6 + 3",
    "Gesucht sind zwei Zahlen g und h mit g · h = 54, die sich um 3 unterscheiden. Mögliche Paare: 1 · 54, 2 · 27, 3 · 18, 6 · 9. Nur 9 und 6 unterscheiden sich um 3. Also ist die Grundseite 9 cm lang und die Höhe 6 cm. Probe: 9 · 6 = 54 und 9 − 6 = 3.",
    [B("6", "die Höhe statt der Grundseite angegeben"),
     B("54 / 3", "durch den Unterschied geteilt"),
     B("6 + 3 + 3", "den Unterschied zweimal addiert")], einheit="cm"), form="umkehren", lp=LP, idee="differenz_paar")

neu(T, "verstehen", "korrektur", "darstellung", Z(
    "Ein Quadrat wird auf jeder Seite um 1 cm länger. Dadurch wächst seine Fläche um 25 cm². Wie lang war die Seite vorher?",
    12, "(25 - 1) / 2", "(25 + 1) / 2 - 1",
    "Die alte Seite sei a. Die neue Fläche ist (a + 1) · (a + 1), die alte a · a. Der Zuwachs besteht aus zwei Streifen (a · 1 und a · 1) und einem kleinen Eckquadrat (1 · 1): 2a + 1 = 25. Also ist 2a = 24 und a = 12 cm. Probe: 13 · 13 − 12 · 12 = 169 − 144 = 25.",
    [B("25", "den Zuwachs als Seitenlänge genommen"),
     B("25 - 1", "das Eckquadrat abgezogen, aber nicht durch 2 geteilt"),
     B("(25 - 1) / 2 + 1", "die neue Seitenlänge statt der alten angegeben")], einheit="cm"), form="bruecke", lp=LP, idee="zuwachs_quadrat")

neu(T, "verstehen", "sicherung", "fehler", L(
    "Ein Rechteck ABCD hat die Ecken A(0|0), B(14|0), C(14|6) und D(0|6) (eine Einheit ist 1 cm). Der Punkt M ist die Mitte der Seite BC. Ein Kind überlegt: Zeile 1: Das Rechteck hat 14 · 6 = 84 cm². Zeile 2: Die Strecke von A nach M teilt das Rechteck in zwei gleich große Teile. Zeile 3: Das Dreieck ABM hat also 42 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist das Dreieck ABM richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 21], ["2", "14 * 3 / 2"], ["3 - 1", "84 / 4"],
    "Zeile 1 stimmt. In Zeile 2 steckt der Fehler: Nur die Diagonale von A nach C halbiert das Rechteck. Die Strecke AM führt zur Mitte der Seite BC und schneidet ein kleineres Stück ab. Das Dreieck ABM hat die Grundseite AB = 14 cm und die Höhe BM = 3 cm: 14 · 3 : 2 = 21 cm², ein Viertel des Rechtecks. Der Rest, das Trapez AMCD, hat 63 cm².",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3"), (1, "Zeile 1 genannt, obwohl dort die Rechteckfläche richtig steht", "1")],
     1: [(42, "die Hälfte des Rechtecks als Fläche des Dreiecks übernommen", "84 / 2"), (63, "die Fläche des Trapezes AMCD statt des Dreiecks angegeben", "84 - 14 * 3 / 2"), (84, "die Fläche des ganzen Rechtecks angegeben", "14 * 6")]}), form="fehler_detektiv", lp=LP, idee="strecke_halbiert_nicht")

neu(T, "verstehen", "sicherung", "umkehr", Z(
    "Ein Dreieck hat die Grundseite 16 cm. Seine Höhe wird um 1 cm länger. Um wie viel cm² wächst die Fläche?",
    8, "16 * 1 / 2", "56 - 48",
    "Die Fläche ist g · h : 2. Wird die Höhe um 1 cm länger, wächst die Fläche um 16 · 1 : 2 = 8 cm², ganz gleich, wie hoch das Dreieck vorher war. Beispiel: Bei h = 6 cm sind es 16 · 6 : 2 = 48 cm², bei h = 7 cm sind es 16 · 7 : 2 = 56 cm², das sind 8 cm² mehr.",
    [B("16", "das Halbieren vergessen"),
     B("1", "den Zuwachs der Höhe als Zuwachs der Fläche genommen"),
     B("16 / 2 + 1", "zum Zuwachs der Fläche noch den Zuwachs der Höhe addiert")], einheit="cm²"), lp=LP, idee="zuwachs_dreieck")


# ───────── vorrat ─────────
neu(T, "rueckwaerts", "sicherung", "fehler", L(
    "Ein Kind berechnet die Höhe eines Parallelogramms mit A = 54 cm² und der Grundseite 9 cm so: Zeile 1: Es gilt A = g · h. Zeile 2: Also ist h = A · g = 54 · 9 = 486. Zeile 3: Die Höhe ist 486 cm. In welcher Zeile steckt der erste Fehler? Wie lang ist die Höhe richtig?",
    "Fehler in Zeile □, richtig: h = □ cm", [2, 6], ["2", "54 / 9"], ["3 - 1", "6"],
    "Zeile 1 stimmt. In Zeile 2 wurde falsch umgestellt: Aus A = g · h folgt h = A : g, nicht A · g. Richtig ist h = 54 : 9 = 6 cm. Zeile 3 übernimmt das unsinnige Ergebnis 486 cm. Probe: 9 · 6 = 54.",
    {0: [(3, "die Schlusszeile genannt, weil dort der unsinnige Wert 486 steht", "3")], 1: [(486, "mal statt geteilt gerechnet: 54 · 9", "54 * 9"), (3, "zusätzlich noch durch 2 geteilt: 54 : 9 : 2", "54 / 9 / 2"), (63, "Fläche und Grundseite addiert: 54 + 9", "54 + 9")]}), form="fehler_detektiv", lp=LP, idee="umstellfehler")

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

neu(T, "verstehen", "korrektur", "darstellung", Z(
    "Ein Trapez mit den parallelen Seiten 12 cm und 6 cm und der Höhe 4 cm liegt in einem Rechteck, das 12 cm lang und 4 cm hoch ist. Wie viel Prozent des Rechtecks füllt das Trapez aus?",
    75, "(12 + 6) * 4 / 2 * 100 / (12 * 4)", "36 / 48 * 100",
    "Das Trapez hat (12 + 6) · 4 : 2 = 36 cm², das Rechteck hat 12 · 4 = 48 cm². Der Anteil ist 36 : 48 = 3/4 = 75 %. Die übrigen 25 % sind die beiden Dreiecke an den Seiten.",
    [B("25", "den freien Rest statt des ausgefüllten Teils angegeben"),
     B("50", "angenommen, das Trapez fülle genau die Hälfte aus"),
     B("(12 + 6) * 4 / 2", "die Fläche des Trapezes statt des Anteils angegeben")], einheit="%"), lp=LP, idee="anteil_im_rechteck")

neu(T, "rueckwaerts", "korrektur", "darstellung", L(
    "Zwei gleiche Trapeze mit den parallelen Seiten 5 cm und 9 cm und der Höhe 4 cm werden zu einem Parallelogramm zusammengelegt. Die Grundseite des Parallelogramms ist □ cm lang. Ein einzelnes Trapez hat die Fläche □ cm².",
    "Grundseite □ cm, Trapez □ cm²", [14, 28], ["5 + 9", "(5 + 9) * 4 / 2"], ["14", "56 / 2"],
    "Legt man das zweite Trapez umgedreht an das erste, ergeben die parallelen Seiten zusammen die Grundseite 5 + 9 = 14 cm; die Höhe bleibt 4 cm. Das Parallelogramm hat 14 · 4 = 56 cm², ein Trapez die Hälfte: 28 cm². So entsteht die Trapezformel (a + c) · h : 2.",
    {0: [(9, "nur die längere parallele Seite genommen", "9"), (45, "die parallelen Seiten malgenommen: 5 · 9", "5 * 9")],
     1: [(56, "das Halbieren vergessen: 14 · 4", "(5 + 9) * 4"), (36, "nur die längere Seite mit der Höhe malgenommen: 9 · 4", "9 * 4"), (20, "nur die kürzere Seite mit der Höhe malgenommen: 5 · 4", "5 * 4")]}),
    form="bruecke", lp=LP, idee="trapez_zu_parallelogramm")

neu(T, "rueckwaerts", "sicherung", "darstellung", Z(
    "Ein Parallelogramm hat die Grundseite 12 cm, die Höhe 8 cm und die schräge Nachbarseite 10 cm. Es wird zu einem Rechteck umgebaut: Ein rechtwinkliges Dreieck mit den Katheten 8 cm und 6 cm wird auf der einen Seite abgeschnitten und auf der anderen Seite wieder angesetzt. Wie groß ist die Fläche des Rechtecks?",
    96, "12 * 8", "12 * 8 - 6 * 8 / 2 + 6 * 8 / 2",
    "Das abgeschnittene Dreieck wird auf der anderen Seite wieder angesetzt, die Fläche bleibt also gleich. Das Rechteck hat dieselbe Grundseite 12 cm und dieselbe Höhe 8 cm wie das Parallelogramm: A = 12 · 8 = 96 cm². Die schräge Seite 10 cm und die Kathete 6 cm spielen für die Fläche keine Rolle. Probe: Das Dreieck hat 6 · 8 : 2 = 24 cm², es geht auf der einen Seite weg und kommt auf der anderen dazu.",
    [B("12 * 10", "die schräge Seite statt der Höhe genommen"),
     B("12 * 8 - 6 * 8 / 2", "das abgeschnittene Dreieck nicht wieder angesetzt"),
     B("12 * 8 / 2", "wie bei einem Dreieck durch 2 geteilt")], einheit="cm²"), lp=LP, idee="parallelogramm_zu_rechteck")
