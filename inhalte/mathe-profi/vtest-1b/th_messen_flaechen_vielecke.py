T = "messen.flaechen_vielecke"
LP = "M6 2 Flächeninhalt und Volumen (Flächeninhalt von Parallelogramm, Dreieck und Trapez; zusammengesetzte Figuren)"
ABG[(T, "dreieck")] = "Die Übungen setzen g und h in g · h : 2 ein; hier wird begründet, warum die Höhe und nicht die schräge Seite zählt, auch wenn sie außen liegt, und das Dreieck über Koordinaten und zwei Wege berechnet."
ABG[(T, "rueckwaerts")] = "Die Übungen stellen die Flächenformel nach h oder g um; hier wird begründet, warum kein Winkel nötig ist, in Sachsituationen umgerechnet und ein Umstellfehler gefunden."
ABG[(T, "zusammengesetzt")] = "Die Übungen zerlegen eine vorgegebene Figur; hier werden Zerlegen und Ergänzen verglichen, eine Teilfläche rückwärts gesucht und ein Fehler beim Dreieck-Teil gefunden."
ABG[(T, "verstehen")] = "Die Übungen rechnen mit verdoppelten Maßen; hier wird erklärt, wie sich die Fläche bei Faktoren und Prozenten ändert, flächengleiche Figuren gefunden und ein Fehler beim Verdoppeln richtiggestellt."
IDEEN[(T, "dreieck")] = ['begruenden_ablenker', 'zwei_wege', 'umkehr', 'darstellung_wechseln', 'modell_aufstellen', 'fehler_finden_richtigstellen', 'was_waere_wenn']
IDEEN[(T, "rueckwaerts")] = ['begruenden_ablenker', 'umkehr', 'umkehr', 'darstellung_wechseln', 'modell_aufstellen', 'fehler_finden_richtigstellen', 'was_waere_wenn']
IDEEN[(T, "zusammengesetzt")] = ['begruenden_ablenker', 'zwei_wege', 'umkehr', 'zerlegen_ergaenzen', 'modell_aufstellen', 'fehler_finden_richtigstellen', 'darstellung_wechseln']
IDEEN[(T, "verstehen")] = ['begruenden_ablenker', 'umkehr', 'groessenvergleich', 'was_waere_wenn', 'was_waere_wenn', 'fehler_finden_richtigstellen', 'darstellung_wechseln']
# ───────── dreieck ─────────
neu(T, "dreieck", "test", "begruenden", W(
    "Die Punkte C und D liegen auf einer Parallelen zur Strecke AB. Der Abstand der Parallelen ist 4 cm, und AB ist 10 cm lang. Das Dreieck ABC ist gleichschenklig: C liegt senkrecht über der Mitte von AB. Das Dreieck ABD ist stumpfwinklig: D liegt 7 cm rechts von B auf der Parallelen. Ein Kind sagt: „ABD ist größer, denn seine Seite AD ist viel länger.“ Welche Aussage ist richtig?",
    "Beide haben 20 cm², denn Grundseite und Höhe sind bei beiden gleich.",
    [("ABD ist größer, denn je länger eine Seite ist, desto größer ist die Fläche.", "die Länge der Seite AD mit der Höhe verwechselt"),
     ("ABD ist kleiner, denn seine Höhe liegt außerhalb des Dreiecks und zählt nicht mit.", "die Höhe außerhalb für ungültig gehalten; auch dort gilt: Grundseite mal Höhe durch 2"),
     ("ABC ist größer, denn ein gleichschenkliges Dreieck hat die größere Fläche.", "gedacht, dass Symmetrie die Fläche vergrößert")],
    "Als Grundseite nimmt man AB = 10 cm. Die zugehörige Höhe ist der Abstand von C und D zur Geraden AB, also 4 cm, für beide Dreiecke. Es gilt A = 10 · 4 : 2 = 20 cm² für ABC und für ABD. "
    "Die Höhe darf wie bei ABD außen liegen. Die Länge der schrägen Seite AD ändert nichts: Man kann C parallel zu AB verschieben, ohne dass sich der Flächeninhalt ändert.",
    lambda: 10 * 4 / 2 == 20 and 10 * 4 / 2 == 20 and 10 * 4 / 2 != 10 * 4 and 20 != 10 * 4 / 2 * 0), lp=LP)
neu(T, "dreieck", "korrektur", "mehrschritt", Z(
    "Das Dreieck ABC hat die Ecken A(1|1), B(9|1) und C(12|6) (eine Einheit ist 1 cm). Anna rechnet mit AB als Grundseite. Ben legt das kleinste Rechteck mit achsenparallelen Seiten um das Dreieck und zieht die beiden überstehenden Dreiecke ab. Wie viele cm² hat das Dreieck?",
    20, "8 * 5 / 2", "11 * 5 - 11 * 5 / 2 - 3 * 5 / 2",
    "Anna: Die Grundseite AB ist 8 cm lang, die Höhe ist der Abstand von C zur Geraden y = 1, also 5 cm. A = 8 · 5 : 2 = 20 cm². Ben: Das Rechteck ist 11 cm breit und 5 cm hoch, also 55 cm². "
    "Die beiden überstehenden Dreiecke haben 11 · 5 : 2 = 27,5 cm² und 3 · 5 : 2 = 7,5 cm². Es bleiben 55 − 27,5 − 7,5 = 20 cm². Beide Wege liefern dasselbe.",
    [B("8 * 5", "das Halbieren vergessen: Grundseite mal Höhe"),
     B("11 * 5 / 2", "mit der Breite 11 des Rechtecks als Grundseite gerechnet"),
     B("3 * 5 / 2", "nur das kleinere überstehende Dreieck berechnet")], einheit="cm²"), form="zwei_wege", lp=LP)
neu(T, "dreieck", "korrektur", "umkehr", Z(
    "Der Flächeninhalt eines Dreiecks ist 36 cm². Seine Höhe ist doppelt so lang wie die zugehörige Grundseite. Wie lang ist die Grundseite?",
    6, "6", "36 / 6",
    "Mit g für die Grundseite ist h = 2g. Dann gilt A = g · 2g : 2 = g · g = 36. Also ist g = 6 cm und h = 12 cm. Probe: 6 · 12 : 2 = 36.",
    [B("36 / 2", "36 durch 2 geteilt und als Grundseite genommen"),
     B("36 / 4", "36 durch 4 geteilt, weil von „doppelt“ und „halb“ die 2 zweimal gezählt wurde"),
     B("12", "die Höhe statt der Grundseite angegeben")], einheit="cm"), form="umkehren", lp=LP)
neu(T, "dreieck", "korrektur", "darstellung", W(
    "Das Dreieck ABC hat die Ecken A(0|0), B(8|0) und C(3|5) (eine Einheit ist 1 cm). Welche Rechnung gibt seinen Flächeninhalt in cm²?",
    "8 · 5 : 2",
    [("8 · 3 : 2", "die x-Koordinate von C als Höhe genommen"),
     ("8 · 5", "das Halbieren vergessen"),
     ("5 · 3 : 2", "die Koordinaten von C als Grundseite und Höhe genommen")],
    "Die Grundseite AB liegt auf der x-Achse und ist 8 cm lang. Die Höhe ist der Abstand von C zur x-Achse, also die y-Koordinate 5 cm. Es gilt A = 8 · 5 : 2 = 20 cm². Die x-Koordinate 3 von C sagt nur, wo die Spitze liegt, nicht wie hoch sie ist.",
    lambda: abs(0 * (0 - 5) + 8 * (5 - 0) + 3 * (0 - 0)) / 2 == 8 * 5 / 2 and 8 * 3 / 2 != 20 and 8 * 5 != 20 and 5 * 3 / 2 != 20), form="bruecke", lp=LP)
neu(T, "dreieck", "sicherung", "transfer", Z(
    "Ein Grundstück hat die Form eines Dreiecks. Eine Seite von 24 m liegt an der Straße. Die gegenüberliegende Ecke ist 15 m von der Straßenlinie entfernt (senkrecht gemessen). Für Rasen zahlt man 3,50 € je m². Wie viel Euro kostet der Rasen für das ganze Grundstück?",
    630, "24 * 15 / 2 * 3.5", "180 * 3.5",
    "Das Grundstück ist ein Dreieck mit g = 24 m und h = 15 m: A = 24 · 15 : 2 = 180 m². Der Rasen kostet 180 · 3,50 € = 630 €.",
    [B("24 * 15 * 3.5", "das Halbieren des Dreiecks vergessen"),
     B("24 * 15 / 2", "nur die Fläche in m² angegeben, nicht den Preis"),
     B("24 + 15 + 3.5", "alle Zahlen der Aufgabe addiert")], einheit="€"), form="anwenden", lp=LP)
neu(T, "dreieck", "sicherung", "fehler", L(
    "Ein Kind berechnet ein Dreieck mit der Grundseite 10 cm, der Höhe 6 cm und der schrägen Seite 7 cm so: Zeile 1: Die Höhe steht senkrecht auf der Grundseite und ist 6 cm lang. Zeile 2: A = g · s : 2 = 10 · 7 : 2 = 35. Zeile 3: Der Flächeninhalt ist 35 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist der Flächeninhalt richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 30], ["2", "10 * 6 / 2"], ["3 - 1", "30"],
    "Zeile 1 stimmt. In Zeile 2 wurde die schräge Seite statt der Höhe genommen. Die Höhe ist 6 cm, also gilt A = 10 · 6 : 2 = 30 cm². Zeile 3 übernimmt das falsche Ergebnis. Die schräge Seite ist länger als die Höhe und darf in der Formel nicht stehen.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(35, "mit der schrägen Seite statt der Höhe gerechnet: 10 · 7 : 2", "10 * 7 / 2"), (60, "das Halbieren vergessen: 10 · 6", "10 * 6"), (42, "Höhe mal schräge Seite gerechnet: 6 · 7", "6 * 7")]}), form="fehler_detektiv", lp=LP)
neu(T, "dreieck", "sicherung", "darstellung", W(
    "Das Dreieck ABC hat die Ecken A(0|0), B(10|0) und C(2|4) (eine Einheit ist 1 cm). Für welchen Punkt P hat das Dreieck ABP denselben Flächeninhalt wie ABC?",
    "P(7|4)",
    [("P(2|8)", "die Höhe verdoppelt; die Fläche wird dadurch doppelt so groß"),
     ("P(5|2)", "die Höhe halbiert; die Fläche wird dadurch halb so groß"),
     ("P(4|10)", "die Grundseite 10 als Höhe genommen")],
    "ABC hat die Grundseite AB = 10 cm und die Höhe 4 cm: A = 10 · 4 : 2 = 20 cm². Jeder Punkt P mit y-Koordinate 4 hat dieselbe Höhe 4 cm über AB, also dieselbe Fläche. Das ist P(7|4). Verschiebt man C parallel zu AB, ändert sich die Fläche nicht.",
    lambda: all(abs(10 * y) / 2 == 20 for (x, y) in [(7, 4)]) and abs(10 * 8) / 2 != 20 and abs(10 * 2) / 2 != 20 and abs(10 * 10) / 2 != 20), lp=LP)
# ───────── rueckwaerts ─────────
neu(T, "rueckwaerts", "test", "begruenden", W(
    "Ein Parallelogramm hat den Flächeninhalt 48 cm². Seine Grundseite a ist 8 cm lang, die schräge Nachbarseite b ist 7 cm lang. Ein Kind sagt: „Die Höhe zu a ist 7 cm, denn das ist die andere Seite.“ Welche Aussage über die Höhe h zu a ist richtig?",
    "h = 6 cm, denn h = A : a = 48 : 8; die Höhe ist kürzer als die schräge Seite.",
    [("h = 7 cm, denn die Höhe ist immer so lang wie die Nachbarseite b des Parallelogramms.", "die schräge Nachbarseite mit der Höhe verwechselt; die Höhe steht senkrecht, die Seite ist schräg"),
     ("h lässt sich nicht bestimmen, denn der Winkel zwischen a und b fehlt in der Aufgabe.", "geglaubt, dass man den Winkel braucht; aus A = a · h folgt h = A : a ohne Winkel"),
     ("h = 3 cm, denn man teilt 48 durch 8 und noch einmal durch 2, wie beim Dreieck.", "die Dreiecksformel benutzt und noch einmal durch 2 geteilt")],
    "Für das Parallelogramm gilt A = a · h. Daraus folgt h = A : a = 48 : 8 = 6 cm. Das passt dazu, dass die Höhe kürzer ist als die schräge Seite b = 7 cm: Eine senkrechte Strecke ist kürzer als eine schräge Strecke zwischen denselben Parallelen. Probe: 8 · 6 = 48.",
    lambda: 48 / 8 == 6 and 6 < 7 and 48 / 8 / 2 == 3 and 8 * 6 == 48 and 8 * 7 != 48), lp=LP)
neu(T, "rueckwaerts", "korrektur", "umkehr", Z(
    "Ein Parallelogramm hat den Flächeninhalt 98 cm². Seine Höhe ist halb so lang wie die zugehörige Grundseite. Wie lang ist die Grundseite?",
    14, "14", "98 / 7",
    "Mit g für die Grundseite ist h = g : 2. Dann gilt A = g · g : 2 = 98, also g · g = 196 und g = 14 cm. Die Höhe ist 7 cm. Probe: 14 · 7 = 98.",
    [B("98 / 2", "98 durch 2 geteilt und als Grundseite genommen"),
     B("98 / 14", "die Höhe 7 statt der Grundseite angegeben"),
     B("98 / 4", "durch 4 geteilt, weil die 2 aus „halb“ doppelt gezählt wurde")], einheit="cm"), form="umkehren", lp=LP)
neu(T, "rueckwaerts", "korrektur", "umkehr", Z(
    "Ein trapezförmiges Fenster hat die parallelen Seiten 90 cm und 150 cm und einen Flächeninhalt von 9 600 cm². Wie hoch ist das Fenster (Abstand der parallelen Seiten)?",
    80, "2 * 9600 / (90 + 150)", "9600 / 120",
    "Für das Trapez gilt A = (a + c) · h : 2. Also ist h = 2 · A : (a + c) = 2 · 9 600 : 240 = 80 cm. Probe: (90 + 150) · 80 : 2 = 9 600.",
    [B("9600 / 240", "das Verdoppeln der Fläche vergessen: 9 600 durch 240"),
     B("2 * 9600 / 150", "nur durch die längere parallele Seite geteilt"),
     B("9600 / 150", "nur durch die längere parallele Seite geteilt und das Verdoppeln vergessen")], einheit="cm"), form="bruecke", lp=LP)
neu(T, "rueckwaerts", "korrektur", "darstellung", W(
    "Ein Dreieck hat den Flächeninhalt 35 cm² und die Grundseite 7 cm. Mit h für die zugehörige Höhe soll der Sachverhalt als Gleichung geschrieben werden. Welche Gleichung ist richtig?",
    "7 · h : 2 = 35",
    [("7 · h = 35", "das Halbieren des Dreiecks vergessen"),
     ("7 + h : 2 = 35", "die Grundseite zur halben Höhe addiert statt malgenommen"),
     ("7 · h · 2 = 35", "das Halbieren durch ein Verdoppeln ersetzt")],
    "Für das Dreieck gilt A = g · h : 2. Mit A = 35 und g = 7 heißt das 7 · h : 2 = 35. Daraus folgt 7 · h = 70 und h = 10 cm. Probe: 7 · 10 : 2 = 35.",
    lambda: 7 * 10 / 2 == 35 and 7 * 10 != 35 and 7 + 10 / 2 != 35 and 7 * 10 * 2 != 35), form="bruecke", lp=LP)
neu(T, "rueckwaerts", "sicherung", "transfer", Z(
    "Ein Feld hat die Form eines Parallelogramms und ist 4,5 ha groß (1 ha = 10 000 m²). Eine der beiden parallelen Seiten ist 300 m lang. In welchem Abstand (in m) liegen die beiden parallelen Seiten?",
    150, "45000 / 300", "4.5 * 10000 / 300",
    "4,5 ha = 45 000 m². Für das Parallelogramm gilt A = g · h, also h = A : g = 45 000 : 300 = 150 m. Probe: 300 · 150 = 45 000.",
    [B("450000 / 300", "die Hektarzahl mit dem Zehnfachen von 10 000 m² umgerechnet"),
     B("45000 / 300 / 2", "zusätzlich durch 2 geteilt wie beim Dreieck"),
     B("45000 / 300 * 2", "mit 2 malgenommen statt durch 2 geteilt")], einheit="m"), form="anwenden", lp=LP)
neu(T, "rueckwaerts", "sicherung", "fehler", L(
    "Ein Kind berechnet die Höhe eines Parallelogramms mit A = 54 cm² und der Grundseite 9 cm so: Zeile 1: Es gilt A = g · h. Zeile 2: Also ist h = A · g = 54 · 9 = 486. Zeile 3: Die Höhe ist 486 cm. In welcher Zeile steckt der erste Fehler? Wie lang ist die Höhe richtig?",
    "Fehler in Zeile □, richtig: h = □ cm", [2, 6], ["2", "54 / 9"], ["3 - 1", "6"],
    "Zeile 1 stimmt. In Zeile 2 wurde falsch umgestellt: Aus A = g · h folgt h = A : g, nicht A · g. Richtig ist h = 54 : 9 = 6 cm. Zeile 3 übernimmt das unsinnige Ergebnis 486 cm. Probe: 9 · 6 = 54.",
    {0: [(3, "die Schlusszeile genannt, weil dort der unsinnige Wert 486 steht", "3")], 1: [(486, "mal statt geteilt gerechnet: 54 · 9", "54 * 9"), (3, "zusätzlich noch durch 2 geteilt: 54 : 9 : 2", "54 / 9 / 2"), (63, "Fläche und Grundseite addiert: 54 + 9", "54 + 9")]}), form="fehler_detektiv", lp=LP)
neu(T, "rueckwaerts", "sicherung", "umkehr", L(
    "Ein Dreieck hat den Flächeninhalt 40 cm² und die Grundseite 10 cm. Ergänze: Seine Höhe ist □ cm. Ein zweites Dreieck mit derselben Höhe und dem doppelten Flächeninhalt hat die Grundseite □ cm.",
    "Höhe □ cm, zweite Grundseite □ cm", [8, 20], ["2 * 40 / 10", "2 * 80 / 8"], ["80 / 10", "10 * 2"],
    "Höhe des ersten Dreiecks: h = 2 · A : g = 2 · 40 : 10 = 8 cm. Das zweite Dreieck hat A = 80 cm² und h = 8 cm, also g = 2 · 80 : 8 = 20 cm. Bei gleicher Höhe und doppelter Fläche ist die Grundseite doppelt so lang.",
    {0: [(4, "das Verdoppeln vergessen: 40 : 10", "40 / 10"), (400, "Fläche mal Grundseite gerechnet: 40 · 10", "40 * 10")], 1: [(10, "die Fläche nicht verdoppelt: 2 · 40 : 8", "2 * 40 / 8"), (5, "durch 2 geteilt statt doppelt gerechnet: 40 : 8", "40 / 8")]}), lp=LP)
# ───────── zusammengesetzt ─────────
neu(T, "zusammengesetzt", "test", "begruenden", W(
    "Eine L-förmige Figur entsteht aus einem Rechteck (10 cm breit, 8 cm hoch), dem oben rechts ein Rechteck von 4 cm Breite und 3 cm Höhe fehlt. Anna zerlegt die Figur in zwei Rechtecke, Ben ergänzt sie zu einem großen Rechteck und zieht das fehlende Stück ab. Welche Aussage ist richtig?",
    "Beide kommen auf 68 cm²: Anna 10 · 5 + 6 · 3, Ben 10 · 8 − 4 · 3.",
    [("Ben erhält mehr als Anna, denn er rechnet mit der größeren Fläche 80 cm².", "den Zwischenwert 80 mit dem Ergebnis verwechselt; das fehlende Stück muss noch abgezogen werden"),
     ("Beide kommen auf 92 cm²: Ben rechnet 80 + 12.", "das fehlende Stück addiert statt abgezogen"),
     ("Anna erhält 68 cm², Ben aber 12 cm², weil er nur das fehlende Stück berechnet.", "das fehlende Stück als Ergebnis genommen")],
    "Anna: Der untere Streifen ist 10 cm breit und 5 cm hoch (8 − 3), der obere linke Teil ist 6 cm breit (10 − 4) und 3 cm hoch: 50 + 18 = 68 cm². Ben: Das große Rechteck hat 80 cm², das fehlende Stück 4 · 3 = 12 cm²: 80 − 12 = 68 cm². Zerlegen und Ergänzen liefern denselben Wert.",
    lambda: 10 * 5 + 6 * 3 == 68 == 10 * 8 - 4 * 3 and 80 + 12 != 68 and 12 != 68), lp=LP)
neu(T, "zusammengesetzt", "korrektur", "mehrschritt", Z(
    "Der Grundriss eines Pavillons hat die Ecken A(0|0), B(8|0), C(8|5), D(4|8) und E(0|5) (eine Einheit ist 1 m). Anna zerlegt ihn in ein Rechteck und ein Dreieck. Ben ergänzt ihn zum Rechteck mit den Ecken (0|0), (8|0), (8|8) und (0|8) und zieht zwei Dreiecke ab. Wie viele m² hat der Grundriss?",
    52, "8 * 5 + 8 * 3 / 2", "8 * 8 - 2 * (4 * 3 / 2)",
    "Anna: Das Rechteck ABCE ist 8 m breit und 5 m hoch, also 40 m². Das Dreieck CDE hat die Grundseite 8 m und die Höhe 3 m, also 8 · 3 : 2 = 12 m². Zusammen 52 m². "
    "Ben: Das ergänzte Quadrat hat 64 m². Die zwei abgezogenen Dreiecke haben je 4 · 3 : 2 = 6 m². Es bleiben 64 − 12 = 52 m².",
    [B("8 * 5", "das Dreieck vergessen: nur das Rechteck"),
     B("8 * 8 - 4 * 3 / 2", "nur ein Dreieck abgezogen"),
     B("8 * 5 + 8 * 3", "beim Dreieck das Halbieren vergessen")], einheit="m²"), form="zwei_wege", lp=LP)
neu(T, "zusammengesetzt", "korrektur", "umkehr", Z(
    "Aus einer Ecke eines Rechtecks (14 cm lang, 9 cm breit) wird ein kleines Rechteck herausgeschnitten, das 4 cm lang ist (entlang der langen Seite gemessen). Die Restfläche beträgt 102 cm². Wie breit ist das herausgeschnittene Stück (entlang der kurzen Seite gemessen)?",
    6, "(14 * 9 - 102) / 4", "24 / 4",
    "Das große Rechteck hat 14 · 9 = 126 cm². Weggenommen wurden 126 − 102 = 24 cm². Das Stück ist 4 cm lang, also ist es 24 : 4 = 6 cm breit. Probe: 126 − 4 · 6 = 102.",
    [B("102 / 4", "die Restfläche statt der weggenommenen Fläche durch 4 geteilt"),
     B("126 / 4", "die Fläche des ganzen Rechtecks durch 4 geteilt"),
     B("126 - 102", "die weggenommene Fläche 24 als Breite angegeben")], einheit="cm"), form="umkehren", lp=LP)
neu(T, "zusammengesetzt", "korrektur", "darstellung", W(
    "Eine Figur ist 9 cm breit und 7 cm hoch. Unten rechts fehlt ein Rechteck von 3 cm Breite und 2 cm Höhe. Vier Kinder berechnen den Flächeninhalt. Welche der Rechnungen ist falsch?",
    "9 · 7 − 3 · 5",
    [("9 · 7 − 3 · 2", "eine richtige Rechnung gewählt: Ergänzen zum Rechteck und fehlendes Stück abziehen"),
     ("9 · 5 + 6 · 2", "eine richtige Rechnung gewählt: oberer Streifen 9 breit, 5 hoch und unten links 6 breit, 2 hoch"),
     ("6 · 7 + 3 · 5", "eine richtige Rechnung gewählt: linker Streifen 6 breit, 7 hoch und rechts daneben 3 breit, 5 hoch")],
    "Die Figur hat 9 · 7 − 3 · 2 = 57 cm². Zerlegt man sie in einen oberen Streifen (9 · 5 = 45) und ein Stück unten links (6 · 2 = 12), kommt man auf 57. Ebenso mit dem linken Streifen 6 · 7 = 42 und dem rechten Teil 3 · 5 = 15: 57. "
    "In 9 · 7 − 3 · 5 wird als Höhe des fehlenden Stücks 5 statt 2 genommen: 63 − 15 = 48. Das ist die falsche Rechnung.",
    lambda: 9 * 7 - 3 * 2 == 57 and 9 * 5 + 6 * 2 == 57 and 6 * 7 + 3 * 5 == 57 and 9 * 7 - 3 * 5 != 57), form="bruecke", lp=LP)
neu(T, "zusammengesetzt", "sicherung", "transfer", Z(
    "Der Boden eines Zimmers ist 6 m lang und 5 m breit. In einer Ecke steht ein quadratischer Kamin mit 1,5 m Seitenlänge, unter dem kein Boden verlegt wird. Parkett kostet 40 € je m². Wie viel Euro kostet das Parkett für die freie Bodenfläche?",
    1110, "(6 * 5 - 1.5 * 1.5) * 40", "27.75 * 40",
    "Die freie Fläche ist 6 · 5 − 1,5 · 1,5 = 30 − 2,25 = 27,75 m². Das Parkett kostet 27,75 · 40 € = 1 110 €.",
    [B("6 * 5 * 40", "den Kamin nicht abgezogen"),
     B("(6 * 5 - 1.5) * 40", "nur 1,5 statt 1,5 mal 1,5 abgezogen"),
     B("1.5 * 1.5 * 40", "nur die Kaminfläche berechnet")], einheit="€"), form="anwenden", lp=LP)
neu(T, "zusammengesetzt", "sicherung", "fehler", L(
    "Ein Kind berechnet ein Fünfeck aus einem Rechteck (12 cm breit, 5 cm hoch) und einem Dreieck darauf mit der Grundseite 12 cm und der Höhe 4 cm. Zeile 1: Rechteck: 12 · 5 = 60 cm². Zeile 2: Dreieck: 12 · 4 = 48 cm². Zeile 3: Gesamt: 60 + 48 = 108 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist die Figur richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [2, 84], ["2", "12 * 5 + 12 * 4 / 2"], ["3 - 1", "60 + 24"],
    "Zeile 1 stimmt. In Zeile 2 fehlt das Halbieren: Das Dreieck hat 12 · 4 : 2 = 24 cm². Gesamt: 60 + 24 = 84 cm². Zeile 3 rechnet mit dem falschen Dreieck richtig weiter.",
    {0: [(3, "die Schlusszeile genannt, weil dort das falsche Ergebnis steht", "3")], 1: [(108, "das Dreieck ohne Halbieren gerechnet: 60 + 48", "60 + 12 * 4"), (72, "das Dreieck mit 12 statt 24 gerechnet: 60 + 12", "60 + 12"), (48, "nur das Dreieck ohne Halbieren angegeben", "12 * 4")]}), form="fehler_detektiv", lp=LP)
neu(T, "zusammengesetzt", "sicherung", "darstellung", Z(
    "Das Viereck ABCD hat die Ecken A(0|0), B(6|0), C(6|4) und D(0|2) (eine Einheit ist 1 cm). Wie viele cm² hat es?",
    18, "(2 + 4) * 6 / 2", "6 * 2 + 6 * 2 / 2",
    "AD und BC sind parallel (beide senkrecht), 2 cm und 4 cm lang, ihr Abstand ist 6 cm. Als Trapez: A = (2 + 4) · 6 : 2 = 18 cm². Oder zerlegt: Rechteck 6 · 2 = 12 cm² und darüber ein Dreieck mit der Grundseite 6 cm und der Höhe 2 cm = 6 cm²: zusammen 18 cm².",
    [B("6 * 4", "das Rechteck bis zur höchsten Ecke genommen"),
     B("6 * 2", "nur das Rechteck bis zur niedrigeren Ecke genommen"),
     B("(2 + 4) * 6", "das Halbieren vergessen")], einheit="cm²"), lp=LP)
# ───────── verstehen ─────────
neu(T, "verstehen", "test", "begruenden", W(
    "Bei einem Parallelogramm wird die Grundseite verdreifacht und die zugehörige Höhe halbiert. Welche Aussage über den neuen Flächeninhalt ist richtig?",
    "Er wird das 1,5-fache, denn die Faktoren multiplizieren sich: 3 · ½.",
    [("Er bleibt gleich, denn dreimal so lang und halb so hoch gleichen sich aus.", "den Faktor 3 und den Faktor ½ als sich aufhebend gedeutet"),
     ("Er wird das 2,5-fache, denn 3 − ½ = 2,5.", "die Faktoren subtrahiert statt multipliziert"),
     ("Er wird das 3,5-fache, denn 3 + ½ = 3,5.", "die Faktoren addiert statt multipliziert")],
    "Der Flächeninhalt ist A = g · h. Mit 3g und h/2 ist der neue Inhalt 3g · h/2 = 1,5 · g · h. Wenn zwei Maße gleichzeitig verändert werden, multiplizieren sich die Faktoren. Beispiel: g = 4, h = 6 gibt A = 24; neu 12 · 3 = 36 = 1,5 · 24.",
    lambda: 3 * F(1, 2) == F(3, 2) and 3 * F(1, 2) != 1 and 3 - F(1, 2) != F(3, 2) and 3 + F(1, 2) != F(3, 2) and 12 * 3 == 36 == F(3, 2) * 24), lp=LP)
neu(T, "verstehen", "korrektur", "umkehr", Z(
    "Die Grundseite eines Dreiecks wird verlängert, die Höhe bleibt gleich. Dabei wächst der Flächeninhalt von 24 cm² auf 60 cm². Das Wievielfache der alten Grundseite ist die neue Grundseite?",
    2.5, "60 / 24", "5 / 2",
    "Bei gleicher Höhe ist der Flächeninhalt proportional zur Grundseite: A = g · h : 2. Der Faktor ist 60 : 24 = 2,5. Beispiel: g = 8, h = 6 gibt 24; mit g = 20 und h = 6 ist A = 60. Die neue Grundseite ist das 2,5-fache.",
    [B("60 - 24", "den Unterschied der Flächeninhalte als Faktor genommen"),
     B("24 / 60", "den Quotienten verkehrt herum gebildet"),
     B("60 / 24 * 2", "mit 2 malgenommen, weil die Dreiecksformel doppelt angewendet wurde")]), form="umkehren", lp=LP)
neu(T, "verstehen", "korrektur", "darstellung", W(
    "Ein Rechteck ist 6 cm lang und 4 cm breit. Welche der folgenden Figuren hat denselben Flächeninhalt wie das Rechteck?",
    "ein Trapez mit den parallelen Seiten 8 cm und 4 cm und dem Abstand 4 cm",
    [("ein Parallelogramm mit der Grundseite 6 cm und der schrägen Nachbarseite 4 cm", "die schräge Seite als Höhe genommen; die Höhe ist kürzer als die schräge Seite"),
     ("ein Dreieck mit der Grundseite 6 cm und der Höhe 4 cm", "das Halbieren vergessen: das Dreieck hat nur die halbe Fläche"),
     ("ein Dreieck mit der Grundseite 8 cm und der Höhe 4 cm", "die Grundseite 8 mit dem Trapez verwechselt; das Dreieck hat nur 16 cm²")],
    "Das Rechteck hat 6 · 4 = 24 cm². Das Trapez hat (8 + 4) · 4 : 2 = 24 cm². Das schräge Parallelogramm hat die Höhe unter 4 cm, also weniger als 24 cm². Die Dreiecke haben 6 · 4 : 2 = 12 cm² und 8 · 4 : 2 = 16 cm².",
    lambda: (8 + 4) * 4 / 2 == 6 * 4 and 6 * 4 / 2 != 24 and 8 * 4 / 2 != 24 and 6 * 3.9 < 24), form="bruecke", lp=LP)
neu(T, "verstehen", "korrektur", "darstellung", Z(
    "Ein Rechteck ist 12 cm lang und 5 cm breit. Es wird zu einem Parallelogramm verformt: Die Seiten bleiben gleich lang, aber die Höhe über der 12-cm-Seite ist nur noch 4 cm. Um wie viel Prozent ist der Flächeninhalt kleiner geworden?",
    20, "(60 - 48) / 60 * 100", "100 - 4 / 5 * 100",
    "Das Rechteck hat 12 · 5 = 60 cm², das Parallelogramm 12 · 4 = 48 cm². Der Unterschied ist 12 cm², das sind 12 : 60 = 0,2 = 20 % von 60 cm². Man sieht es auch an der Höhe: 4 von 5 sind 80 %, also fehlen 20 %.",
    [B("5 - 4", "den Höhenunterschied 1 als Prozentzahl gelesen"),
     B("4 / 5 * 100", "die verbleibenden 80 % als Abnahme angegeben"),
     B("60 - 48", "den Unterschied in cm² als Prozentzahl gelesen")], einheit="%"), lp=LP)
neu(T, "verstehen", "sicherung", "parameter", Z(
    "Bei einem Dreieck wird die Grundseite um 20 % verlängert und die Höhe ebenfalls um 20 % verlängert. Um wie viel Prozent wächst der Flächeninhalt?",
    44, "1.2 * 1.2 * 100 - 100", "144 - 100",
    "Die Grundseite wird das 1,2-fache, die Höhe auch. Der Flächeninhalt wird das 1,2 · 1,2 = 1,44-fache, also 144 % des alten Wertes. Er wächst um 44 %. Beispiel: g = 10, h = 10 gibt 50; mit 12 und 12 ist es 72, und 72 : 50 = 1,44.",
    [B("20 + 20", "die Prozentzahlen addiert"),
     B("20 * 20", "die Prozentzahlen multipliziert"),
     B("120 * 120 / 100", "den neuen Wert 144 % als Zunahme angegeben")], einheit="%"), lp=LP)
neu(T, "verstehen", "sicherung", "fehler", L(
    "Ein Kind überlegt: Zeile 1: Ein Quadrat hat die Seitenlänge 5 cm, also A = 25 cm². Zeile 2: Die Seite wird verdoppelt und ist dann 10 cm lang. Zeile 3: Also wird auch die Fläche verdoppelt, A = 50 cm². In welcher Zeile steckt der erste Fehler? Wie groß ist die Fläche des neuen Quadrats richtig?",
    "Fehler in Zeile □, richtig: A = □ cm²", [3, 100], ["3", "10 * 10"], ["2 + 1", "4 * 25"],
    "Zeile 1 und Zeile 2 stimmen. In Zeile 3 wird die Fläche nur verdoppelt. Beide Maße des Quadrats werden doppelt so lang, die Fläche wird deshalb 2 · 2 = 4-mal so groß: 10 · 10 = 100 cm², das sind 4 · 25.",
    {0: [(2, "Zeile 2 genannt, obwohl dort die Seite richtig verdoppelt wird", "2")], 1: [(50, "die Fläche nur verdoppelt: 2 · 25", "2 * 25"), (20, "Seite mal 2 als Fläche gerechnet: 10 · 2", "10 * 2"), (40, "Seite mal 4 als Fläche gerechnet: 10 · 4", "10 * 4")]}), form="fehler_detektiv", lp=LP)
neu(T, "verstehen", "sicherung", "darstellung", Z(
    "Ein Dreieck und ein Parallelogramm haben dieselbe Grundseite. Das Dreieck ist doppelt so hoch wie das Parallelogramm. Das Wievielfache des Flächeninhalts des Parallelogramms ist der Flächeninhalt des Dreiecks?",
    1, "2 / 2", "1",
    "Mit g und h für das Parallelogramm gilt A = g · h. Das Dreieck hat die Grundseite g und die Höhe 2h: A = g · 2h : 2 = g · h. Beide Flächen sind gleich groß, das Dreieck ist das 1-fache. Anschaulich: Zwei gleiche Dreiecke ergeben ein Parallelogramm.",
    [B("2", "die doppelte Höhe beachtet, das Halbieren beim Dreieck vergessen"),
     B("1 / 2", "nur das Halbieren beachtet und die doppelte Höhe vergessen"),
     B("2 * 2", "doppelte Höhe und Halbieren als zwei Verdoppelungen gerechnet")]), form="bruecke", lp=LP)
