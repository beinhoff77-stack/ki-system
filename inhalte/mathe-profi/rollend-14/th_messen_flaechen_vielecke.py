T = "messen.flaechen_vielecke"
# ───────── parallelogramm ─────────
a1(T, "parallelogramm", Z(
    "Eine Fensterscheibe hat die Form eines Parallelogramms. Die Grundseite ist 45 cm lang, die Höhe beträgt 30 cm. Wie groß ist die Fläche der Scheibe?",
    1350, "45 * 30", "30 * 45", "Beim Parallelogramm ist die Fläche Grundseite mal Höhe. Die Höhe steht senkrecht auf der Grundseite.",
    "A = g · h = 45 · 30 = 1 350 cm².",
    [B("45 * 30 / 2", "die Formel für das Dreieck benutzt"), B("45 + 30", "Grundseite und Höhe addiert"), B("2 * (45 + 30)", "zweimal die Summe aus Grundseite und Höhe gerechnet")], "cm²"))
a2(T, "parallelogramm", Z(
    "Ein Banner hat die Form eines Parallelogramms. Die Grundseite ist 2,4 m lang, die Höhe ist 1,5 m. Der Stoff kostet 8 € je Quadratmeter. Wie viel Euro kostet der Stoff für das Banner?",
    28.8, "2.4 * 1.5 * 8", "3.6 * 8", "Berechne zuerst die Fläche in m². Dann rechnest du den Preis.",
    "Fläche: 2,4 · 1,5 = 3,6 m². Preis: 3,6 · 8 = 28,80 €.",
    [B("2.4 * 1.5", "nur die Fläche angegeben"), B("2.4 * 8", "die Höhe vergessen"), B("2.4 * 1.5 * 8 / 2", "die Formel für das Dreieck benutzt")], "€"))
a3(T, "parallelogramm", Z(
    "Ein Parallelogramm hat die Fläche 96 cm² und die Seitenlängen 12 cm und 8 cm. Wie groß ist die Summe der beiden zugehörigen Höhen in Zentimetern?",
    20, "96 / 12 + 96 / 8", "8 + 12", "Die Fläche ist Grundseite mal Höhe. Berechne zu jeder der beiden Seiten die zugehörige Höhe.",
    "Zur Seite 12 cm gehört die Höhe 96 : 12 = 8 cm. Zur Seite 8 cm gehört die Höhe 96 : 8 = 12 cm. Summe: 8 + 12 = 20 cm.",
    [B("96 / 8", "nur die Höhe zur Seite 8 cm angegeben"), B("96 / 12", "nur die Höhe zur Seite 12 cm angegeben"), B("96 / (12 + 8)", "die Fläche durch die Summe der Seiten geteilt")], "cm"), g="transfer")
# ───────── dreieck ─────────
a1(T, "dreieck", Z(
    "Ein Segel ist ein Dreieck mit der Grundseite 7 m und der Höhe 4 m. Wie groß ist die Fläche des Segels?",
    14, "7 * 4 / 2", "28 / 2", "Beim Dreieck rechnest du Grundseite mal Höhe und teilst dann durch 2.",
    "Das Rechteck mit denselben Maßen hat 7 · 4 = 28 m². Das Dreieck ist halb so groß: 28 : 2 = 14 m².",
    [B("7 * 4", "nicht durch 2 geteilt"), B("7 + 4", "Grundseite und Höhe addiert"), B("7 * 4 / 4", "durch 4 statt durch 2 geteilt")], "m²"))
a2(T, "dreieck", Z(
    "Eine Wimpelkette hat 8 gleiche Dreiecke aus Stoff. Jedes Dreieck hat die Grundseite 30 cm und die Höhe 40 cm. Wie viele Quadratzentimeter Stoff braucht man für alle Wimpel?",
    4800, "8 * 30 * 40 / 2", "8 * 600", "Berechne zuerst die Fläche eines Wimpels. Dann rechnest du mal 8.",
    "Ein Wimpel: 30 · 40 : 2 = 600 cm². Alle 8 Wimpel: 8 · 600 = 4 800 cm².",
    [B("8 * 30 * 40", "nicht durch 2 geteilt"), B("30 * 40 / 2", "nur einen Wimpel berechnet"), B("8 * (30 + 40) / 2", "Grundseite und Höhe addiert, dann mal 8 und durch 2 geteilt")], "cm²"))
a3(T, "dreieck", Z(
    "Ein Dreieck hat die Grundseite 14 cm und die Höhe 5 cm. Ein zweites Dreieck hat denselben Flächeninhalt, aber die Grundseite 10 cm. Wie hoch ist das zweite Dreieck?",
    7, "14 * 5 / 10", "70 / 10", "Das erste Dreieck hat die Fläche 14 · 5 : 2. Für das zweite gilt dieselbe Fläche mit der Grundseite 10 cm.",
    "Fläche: 14 · 5 : 2 = 35 cm². Zweites Dreieck: 2 · 35 : 10 = 7 cm. Probe: 10 · 7 : 2 = 35.",
    [B("14 * 5 / 2 / 10", "die Fläche nicht wieder verdoppelt"), B("14 * 5", "das Produkt der ersten Maße als Höhe angegeben"), B("14 * 5 / 2", "die Fläche statt der Höhe angegeben")], "cm"), g="transfer")
# ───────── trapez ─────────
a1(T, "trapez", Z(
    "Die Giebelwand eines Schuppens ist ein Trapez. Die parallelen Seiten sind 10 m und 6 m lang, die Höhe ist 3 m. Wie groß ist die Wandfläche?",
    24, "(10 + 6) * 3 / 2", "16 * 3 / 2", "Beim Trapez addierst du die parallelen Seiten, multiplizierst mit der Höhe und teilst durch 2.",
    "(10 + 6) · 3 : 2 = 16 · 3 : 2 = 48 : 2 = 24 m².",
    [B("10 * 6 * 3 / 2", "die parallelen Seiten malgenommen"), B("(10 + 6) * 3", "nicht durch 2 geteilt"), B("(10 + 6) / 2", "die Höhe vergessen")], "m²"))
a2(T, "trapez", Z(
    "Eine Tischplatte hat die Form eines Trapezes. Die parallelen Seiten sind 1,2 m und 0,8 m lang, der Abstand zwischen ihnen ist 0,5 m. Lack kostet 12 € je Quadratmeter. Wie viel Euro kostet der Lack für die Platte?",
    6, "(1.2 + 0.8) * 0.5 / 2 * 12", "0.5 * 12", "Berechne zuerst die Fläche der Platte. Dann rechnest du den Preis.",
    "Fläche: (1,2 + 0,8) · 0,5 : 2 = 0,5 m². Preis: 0,5 · 12 = 6 €.",
    [B("(1.2 + 0.8) * 0.5 / 2", "nur die Fläche angegeben"), B("(1.2 + 0.8) * 0.5 * 12", "nicht durch 2 geteilt"), B("1.2 * 0.8 * 0.5 / 2 * 12", "die parallelen Seiten malgenommen")], "€"))
a3(T, "trapez", Z(
    "Ein Trapez hat die Fläche 54 cm² und die Höhe 6 cm. Eine der parallelen Seiten ist 11 cm lang. Wie lang ist die andere parallele Seite?",
    7, "54 * 2 / 6 - 11", "18 - 11", "Zweimal die Fläche geteilt durch die Höhe ist die Summe der parallelen Seiten.",
    "Summe der parallelen Seiten: 2 · 54 : 6 = 18 cm. Die andere Seite: 18 − 11 = 7 cm.",
    [B("54 * 2 / 6 / 2", "die Summe der parallelen Seiten halbiert"), B("54 * 2 / 6", "die Summe der Seiten als andere Seite angegeben"), B("54 * 2 / 6 + 11", "die bekannte Seite addiert statt abgezogen")], "cm"), g="rueckwaerts")
# ───────── rueckwaerts ─────────
a1(T, "rueckwaerts", Z(
    "Ein Beet hat die Form eines Parallelogramms und ist 96 m² groß. Die Seite am Weg ist 12 m lang. Wie breit ist das Beet, gemessen als Abstand senkrecht zum Weg?",
    8, "96 / 12", "96 / 12", "Die Fläche ist Grundseite mal Höhe. Teile die Fläche durch die Seite am Weg.",
    "Die Seite am Weg ist die Grundseite. h = A : g = 96 : 12 = 8 m. Probe: 12 · 8 = 96.",
    [B("96 * 12", "mit der Grundseite malgenommen"), B("96 / 12 / 2", "zusätzlich durch 2 geteilt"), B("96 - 12", "die Grundseite abgezogen")], "m"))
a2(T, "rueckwaerts", Z(
    "Ein dreieckiger Wimpel hat die Fläche 60 cm² und ist 8 cm hoch, gemessen senkrecht zu der Seite, mit der er an der Schnur befestigt ist. An einer Schnur hängen 12 solche Wimpel lückenlos nebeneinander, jeweils mit der Befestigungsseite an der Schnur. Wie lang ist das Schnurstück, an dem alle Wimpel hängen, in Zentimetern?",
    180, "12 * 2 * 60 / 8", "12 * 15", "Berechne zuerst die Befestigungsseite eines Wimpels: zweimal die Fläche, geteilt durch die Höhe.",
    "Dreieck: A = g · h : 2. Also g = 2 · 60 : 8 = 15 cm. Für 12 Wimpel: 12 · 15 = 180 cm. Probe: 15 · 8 : 2 = 60.",
    [B("12 * 60 / 8", "die Fläche vor dem Teilen nicht verdoppelt"), B("2 * 60 / 8", "nur die Seite eines Wimpels angegeben"), B("12 * 60 * 8 / 2", "die Fläche mit der Höhe malgenommen und durch 2 geteilt, dann mal 12")], "cm"))
a3(T, "rueckwaerts", Z(
    "Ein Rechteck ist 6 cm breit und 12 cm lang. Ein Dreieck hat denselben Flächeninhalt und die Grundseite 16 cm. Wie hoch ist das Dreieck?",
    9, "2 * 6 * 12 / 16", "144 / 16", "Berechne die Fläche des Rechtecks. Beim Dreieck rechnest du dann zweimal die Fläche geteilt durch die Grundseite.",
    "Rechteck: 6 · 12 = 72 cm². Dreieck: 2 · 72 : 16 = 9 cm. Probe: 16 · 9 : 2 = 72.",
    [B("6 * 12 / 16", "die Fläche vor dem Teilen nicht verdoppelt"), B("6 * 12 * 16 / 2", "die Fläche mit der Grundseite malgenommen und durch 2 geteilt"), B("6 * 12 - 16", "die Grundseite von der Fläche abgezogen")], "cm"), g="verknuepfen")
# ───────── zusammengesetzt ─────────
a1(T, "zusammengesetzt", Z(
    "Ein Zimmer ist ein Rechteck von 8 m mal 5 m. An einer Seite hat es einen Erker, der ein Quadrat mit 2 m Seitenlänge ist. Wie groß ist die Bodenfläche mit dem Erker?",
    44, "8 * 5 + 2 * 2", "40 + 4", "Zerlege den Grundriss in ein Rechteck und ein Quadrat. Berechne beide Flächen.",
    "Rechteck: 8 · 5 = 40 m². Erker: 2 · 2 = 4 m². Zusammen 40 + 4 = 44 m².",
    [B("8 * 5", "den Erker vergessen"), B("2 * 2", "nur den Erker gerechnet"), B("8 * 5 - 2 * 2", "den Erker abgezogen statt addiert")], "m²"))
a2(T, "zusammengesetzt", Z(
    "Ein Spielfeld ist ein Rechteck von 20 m mal 12 m. In einer Ecke liegt ein Beet in Form eines rechtwinkligen Dreiecks mit den Katheten 6 m und 4 m. Dort darf man nicht spielen. Wie groß ist die Spielfläche?",
    228, "20 * 12 - 6 * 4 / 2", "240 - 12", "Berechne das ganze Rechteck. Ziehe dann die Fläche des Dreiecks ab. Das Dreieck ist halb so groß wie ein Rechteck mit denselben Maßen.",
    "Rechteck: 20 · 12 = 240 m². Dreieck: 6 · 4 : 2 = 12 m². Spielfläche: 240 − 12 = 228 m².",
    [B("20 * 12", "das Beet nicht abgezogen"), B("20 * 12 - 6 * 4", "das Dreieck wie ein Rechteck abgezogen"), B("20 * 12 + 6 * 4 / 2", "das Beet dazugezählt statt abgezogen")], "m²"))
a3(T, "zusammengesetzt", Z(
    "Ein Bild ist 40 cm breit und 30 cm hoch. Es hat einen Rahmen, der rundherum 5 cm breit ist. Wie groß ist die Fläche des Rahmens ohne das Bild?",
    800, "(40 + 2 * 5) * (30 + 2 * 5) - 40 * 30", "50 * 40 - 40 * 30", "Der Rahmen macht das Rechteck auf jeder Seite größer. Berechne das Außenrechteck und ziehe das Bild ab.",
    "Außen: (40 + 10) · (30 + 10) = 50 · 40 = 2 000 cm². Bild: 40 · 30 = 1 200 cm². Rahmen: 2 000 − 1 200 = 800 cm².",
    [B("(40 + 5) * (30 + 5) - 40 * 30", "den Rahmen nur auf einer Seite gerechnet"), B("2 * 5 * (40 + 30)", "die vier Ecken vergessen"), B("(40 - 2 * 5) * (30 - 2 * 5)", "40 cm mal 30 cm als Außenmaße gelesen und das Innenrechteck 30 · 20 berechnet")], "cm²"), g="transfer")
# ───────── oberflaeche ─────────
a1(T, "oberflaeche", Z(
    "Ein Geschenk ist ein Quader: 25 cm lang, 12 cm breit und 6 cm hoch. Es wird rundherum in Papier eingepackt, ohne dass sich das Papier überlappt. Wie viele Quadratzentimeter Papier braucht man mindestens?",
    1044, "2 * (25 * 12 + 25 * 6 + 12 * 6)", "2 * 522", "Ein Quader hat drei Paare gleicher Flächen. Berechne jede Sorte einmal und verdopple die Summe.",
    "Boden und Deckel: 25 · 12 = 300. Vorder- und Rückseite: 25 · 6 = 150. Die beiden Seiten: 12 · 6 = 72. Summe: 522. Doppelt: 1 044 cm².",
    [B("25 * 12 * 6", "das Volumen statt der Oberfläche berechnet"), B("25 * 12 + 25 * 6 + 12 * 6", "die drei Flächensorten nur einmal gezählt"), B("2 * (25 * 12 + 25 * 6)", "ein Flächenpaar vergessen")], "cm²"))
a2(T, "oberflaeche", Z(
    "Eine Dachrinne ist 2 m lang. Ihr Querschnitt ist ein Rechteck, 12 cm breit und 8 cm hoch. Die Rinne ist oben offen, ihre beiden Enden sind mit Blech verschlossen. Wie viele Quadratzentimeter Blech werden für Boden, beide Seitenwände und beide Enden gebraucht?",
    5792, "12 * 200 + 2 * 8 * 200 + 2 * 12 * 8", "2400 + 3200 + 192", "Rechne in cm: 2 m sind 200 cm. Berechne Boden, zwei lange Seitenwände und zwei kleine Endflächen.",
    "Boden: 12 · 200 = 2 400 cm². Zwei Seitenwände: 2 · 8 · 200 = 3 200 cm². Zwei Enden: 2 · 12 · 8 = 192 cm². Zusammen 2 400 + 3 200 + 192 = 5 792 cm².",
    [B("2 * 12 * 200 + 2 * 8 * 200 + 2 * 12 * 8", "einen Deckel mitgerechnet"), B("12 * 200 + 2 * 8 * 200", "die beiden Enden vergessen"), B("12 * 200 + 2 * 12 * 8", "die Seitenwände vergessen")], "cm²"))
a3(T, "oberflaeche", Z(
    "Ein Würfel hat die Oberfläche 54 cm². Zwei solche Würfel werden mit je einer ganzen Fläche zu einem Quader zusammengeklebt. Wie groß ist die Oberfläche des Quaders?",
    90, "2 * 54 - 2 * (54 / 6)", "108 - 18", "Wie groß ist eine Würfelfläche? Beim Zusammenkleben verschwinden zwei Würfelflächen.",
    "Eine Würfelfläche: 54 : 6 = 9 cm². Beide Würfel: 2 · 54 = 108 cm². Beim Kleben verschwinden 2 · 9 = 18 cm². Oberfläche: 108 − 18 = 90 cm².",
    [B("2 * 54", "die Klebeflächen nicht abgezogen"), B("2 * 54 - 54 / 6", "nur eine Klebefläche abgezogen"), B("2 * 54 - 54", "eine ganze Würfeloberfläche abgezogen")], "cm²"), g="transfer")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Ein dreieckiges Blumenbeet hat die Grundseite 10 m und die Höhe 7 m. Ein zweites Beet bekommt dieselbe Grundseite, aber die doppelte Höhe. Wie groß ist die Fläche des zweiten Beets?",
    70, "10 * 14 / 2", "10 * 7 / 2 * 2", "Wie ändert sich die Fläche, wenn die Höhe doppelt so groß wird? Du kannst auch neu rechnen.",
    "Die neue Höhe ist 14 m. Fläche: 10 · 14 : 2 = 70 m². Die Fläche hat sich verdoppelt (vorher 35 m²).",
    [B("10 * 7 / 2", "die Fläche des ersten Beets angegeben"), B("10 * 7 / 2 * 4", "die Fläche vervierfacht"), B("10 * 7 / 2 + 10", "die Grundseite zur alten Fläche addiert")], "m²"))
a2(T, "verstehen", Z(
    "Ein Rechteck ist 9 cm lang und 6 cm hoch. Ein Parallelogramm hat dieselbe Grundseite 9 cm und dieselbe Höhe 6 cm. Seine schräge Seite ist 8 cm lang. Wie groß ist die Fläche des Parallelogramms?",
    54, "9 * 6", "6 * 9", "Beim Parallelogramm zählt die Höhe, nicht die schräge Seite. Die Höhe steht senkrecht auf der Grundseite.",
    "Das Parallelogramm hat dieselbe Grundseite und Höhe wie das Rechteck. Gleiche Fläche: 9 · 6 = 54 cm². Die schräge Seite ist für die Fläche nicht wichtig.",
    [B("9 * 8", "die schräge Seite als Höhe benutzt"), B("9 * 6 / 2", "durch 2 geteilt"), B("2 * (9 + 8)", "einen Umfang berechnet")], "cm²"))
a3(T, "verstehen", Z(
    "Kim berechnet ein Trapez mit den parallelen Seiten 8 cm und 4 cm und der Höhe 5 cm so: „8 · 4 · 5 : 2 = 80 cm².“ Um wie viele Quadratzentimeter ist Kims Ergebnis zu groß?",
    50, "8 * 4 * 5 / 2 - (8 + 4) * 5 / 2", "80 - 30", "Welche Formel gilt beim Trapez? Berechne die richtige Fläche und vergleiche mit Kims 80.",
    "Richtig: (8 + 4) · 5 : 2 = 30 cm². Kim hat die Seiten malgenommen statt addiert und kommt auf 80 cm². Unterschied: 80 − 30 = 50 cm².",
    [B("8 * 4 * 5 / 2", "Kims falsche Fläche angegeben"), B("(8 + 4) * 5 / 2", "die richtige Fläche angegeben"), B("8 * 4 * 5 / 2 - (8 + 4) * 5", "die richtige Fläche ohne Teilen durch 2 berechnet (60 statt 30)")], "cm²"), g="fehler")
# ───────── drachen_raute ─────────
a1(T, "drachen_raute", Z(
    "Ein Papierdrache hat die Diagonalen 60 cm und 40 cm. Wie groß ist die Fläche des Drachens?",
    1200, "60 * 40 / 2", "2400 / 2", "Beim Drachen rechnest du: erste Diagonale mal zweite Diagonale, geteilt durch 2.",
    "A = e · f : 2 = 60 · 40 : 2 = 2 400 : 2 = 1 200 cm².",
    [B("60 * 40", "nicht durch 2 geteilt"), B("60 + 40", "die Diagonalen addiert"), B("60 * 40 / 4", "durch 4 statt durch 2 geteilt")], "cm²"))
a2(T, "drachen_raute", Z(
    "Eine Fliese hat die Form einer Raute mit den Diagonalen 18 cm und 10 cm. Zwei gleiche Fliesen liegen nebeneinander. Wie groß ist ihre gesamte Fläche?",
    180, "2 * (18 * 10 / 2)", "2 * 90", "Berechne zuerst die Fläche einer Fliese. Dann verdoppelst du.",
    "Eine Fliese: 18 · 10 : 2 = 90 cm². Zwei Fliesen: 2 · 90 = 180 cm².",
    [B("18 * 10 / 2", "nur eine Fliese berechnet"), B("2 * 18 * 10", "die Fläche nicht durch 2 geteilt"), B("2 * (18 + 10)", "die Diagonalen addiert")], "cm²"))
a3(T, "drachen_raute", Z(
    "Eine Raute hat die Fläche 120 cm². Die eine Diagonale ist 24 cm lang. Ein Rechteck hat als Seitenlängen genau die beiden Diagonalen der Raute. Wie groß ist der Umfang des Rechtecks in Zentimetern?",
    68, "2 * (24 + 2 * 120 / 24)", "2 * 34", "Berechne zuerst die andere Diagonale: zweimal die Fläche, geteilt durch die bekannte Diagonale. Dann bestimmst du den Umfang des Rechtecks.",
    "Fläche der Raute: e · f : 2 = 120, also f = 2 · 120 : 24 = 10 cm. Das Rechteck hat die Seiten 24 cm und 10 cm. Umfang: 2 · (24 + 10) = 68 cm.",
    [B("2 * (24 + 120 / 24)", "die Fläche vor dem Teilen nicht verdoppelt"), B("24 + 2 * 120 / 24", "nur die halbe Summe der Seiten statt des Umfangs angegeben"), B("24 * 2 * 120 / 24", "die Fläche des Rechtecks statt des Umfangs angegeben")], "cm"), g="rueckwaerts")