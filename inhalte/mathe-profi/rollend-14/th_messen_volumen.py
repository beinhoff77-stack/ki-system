T = "messen.volumen"
# ───────── einheitswuerfel ─────────
a1(T, "einheitswuerfel", Z(
    "Eine Schachtel ist innen 5 cm lang, 4 cm breit und 3 cm hoch. Kim füllt sie ganz mit Würfeln, die 1 cm Kante haben. Wie viele Würfel passen hinein?",
    60, "5 * 4 * 3", "20 * 3", "Wie viele Würfel liegen in der untersten Schicht? Wie viele Schichten passen übereinander?",
    "Eine Schicht hat 5 · 4 = 20 Würfel. Es passen 3 Schichten hinein: 20 · 3 = 60 Würfel.",
    [B("5 * 4", "nur die unterste Schicht gezählt"), B("5 + 4 + 3", "die Kantenlängen addiert"), B("2 * (5 * 4 + 5 * 3 + 4 * 3)", "die Oberfläche statt der Würfelzahl berechnet")]))
a2(T, "einheitswuerfel", Z(
    "Ein Quader ist aus Würfeln gebaut: 6 Würfel in der Länge, 3 in der Breite und 2 Schichten übereinander. Sam nimmt die oberste Schicht ganz weg. Wie viele Würfel bleiben liegen?",
    18, "6 * 3 * 2 - 6 * 3", "6 * 3 * (2 - 1)", "Wie viele Würfel hat eine Schicht? Wie viele Schichten bleiben übrig?",
    "Eine Schicht hat 6 · 3 = 18 Würfel. Von 2 Schichten bleibt 1 Schicht. Es bleiben 18 Würfel liegen.",
    [B("6 * 3 * 2", "die Würfel vor dem Wegnehmen angegeben"), B("6 * 3 * 2 - 6", "nur eine Reihe statt einer Schicht weggenommen"), B("6 * 3 - 2", "die Zahl der Schichten von den Würfeln einer Schicht abgezogen")]))
a3(T, "einheitswuerfel", Z(
    "Ein Quader besteht aus 5 · 4 · 3 kleinen Würfeln. Er wird außen ganz angemalt, auch unten. Wie viele kleine Würfel haben dann keine angemalte Fläche?",
    6, "(5 - 2) * (4 - 2) * (3 - 2)", "3 * 2 * 1", "Welche kleinen Würfel liegen ganz innen? Wie viele Schichten bleiben in jeder Richtung ohne die äußeren?",
    "Außen liegen in jeder Richtung 2 Schichten. Es bleiben 5 − 2 = 3, 4 − 2 = 2 und 3 − 2 = 1 Würfel. Innen liegen 3 · 2 · 1 = 6 kleine Würfel.",
    [B("5 * 4 * 3", "alle Würfel gezählt"), B("5 * 4 * 3 - 3 * 2 * 1", "die Zahl der angemalten Würfel angegeben"), B("4 * 3 * 2", "nur eine Schicht je Richtung abgezogen")]), g="transfer")
# ───────── quader ─────────
a1(T, "quader", Z(
    "Ein Umzugskarton ist 40 cm lang, 25 cm breit und 20 cm hoch. Wie groß ist sein Volumen?",
    20000, "40 * 25 * 20", "1000 * 20", "Das Volumen eines Quaders ist Länge mal Breite mal Höhe.",
    "Grundfläche: 40 · 25 = 1 000 cm². Volumen: 1 000 · 20 = 20 000 cm³.",
    [B("40 * 25", "nur die Grundfläche angegeben"), B("40 + 25 + 20", "die Kanten addiert"), B("2 * (40 * 25 + 40 * 20 + 25 * 20)", "die Oberfläche statt des Volumens berechnet")], "cm³"))
a2(T, "quader", Z(
    "Ein Schwimmbecken ist 8 m lang und 4,5 m breit. Das Wasser steht 1,5 m hoch. Wie viel Kubikmeter Wasser sind im Becken?",
    54, "8 * 4.5 * 1.5", "4.5 * 8 * 1.5", "Das Wasser bildet einen Quader. Seine Höhe ist die Wasserhöhe.",
    "Grundfläche: 8 · 4,5 = 36 m². Volumen: 36 · 1,5 = 54 m³.",
    [B("8 * 4.5", "nur die Grundfläche angegeben"), B("8 + 4.5 + 1.5", "die Kantenlängen addiert"), B("8 * 4.5 * 1.5 * 1000", "das Ergebnis in Liter statt in Kubikmeter angegeben")], "m³"))
a3(T, "quader", Z(
    "Ein Würfel mit 8 cm Kante und ein Quader mit 16 cm Länge und 8 cm Breite haben genau dasselbe Volumen. Wie hoch ist der Quader?",
    4, "8 * 8 * 8 / (16 * 8)", "(8 * 8 * 8) / (16 * 8)", "Berechne zuerst das Volumen des Würfels. Dann fehlt beim Quader nur die Höhe.",
    "Würfel: 8 · 8 · 8 = 512 cm³. Die Grundfläche des Quaders ist 16 · 8 = 128 cm². Höhe: 512 : 128 = 4 cm.",
    [B("8 * 8 * 8 / 16", "nur durch die Länge geteilt"), B("16 * 8 / 8", "das Volumen des Würfels nicht benutzt"), B("8 * 8 * 8 - 16 * 8", "die Grundfläche vom Volumen abgezogen")], "cm"), g="rueckwaerts")
# ───────── einheiten ─────────
a1(T, "einheiten", Z(
    "Ein Regenwassertank fasst 3,6 m³. Wie viele Kubikdezimeter sind das?",
    3600, "3.6 * 1000", "3.6 * 10 * 10 * 10", "Bei Volumen ist jeder Schritt zur nächsten Einheit mal oder durch 1 000. Von m³ nach dm³ ist es ein Schritt.",
    "1 m³ = 1 000 dm³. Also 3,6 m³ = 3,6 · 1 000 = 3 600 dm³.",
    [B("3.6 * 100", "mit 100 wie bei Flächen gerechnet"), B("3.6 * 1000000", "zwei Schritte statt einem gerechnet"), B("3.6 / 1000", "geteilt statt malgenommen")], "dm³"))
a2(T, "einheiten", Z(
    "Sam hat 0,8 m³ Sand. Eine Schubkarre fasst 40 dm³. Wie viele volle Schubkarren ergibt der Sand?",
    20, "0.8 * 1000 / 40", "800 / 40", "Rechne zuerst die Kubikmeter in Kubikdezimeter um. Dann teilst du.",
    "0,8 m³ = 800 dm³. Dann 800 : 40 = 20 Schubkarren.",
    [B("0.8 / 40", "ohne Umrechnung geteilt"), B("0.8 * 100 / 40", "mit 100 statt mit 1 000 umgerechnet"), B("0.8 * 1000 * 40", "malgenommen statt geteilt")]))
a3(T, "einheiten", Z(
    "Tank A fasst 0,004 m³, Tank B fasst 3,2 dm³ und Tank C fasst 2 500 cm³. Um wie viele Kubikzentimeter ist der größte Tank größer als der kleinste?",
    1500, "0.004 * 1000000 - 2500", "4000 - 2500", "Schreibe alle drei Angaben in derselben Einheit, am besten in cm³. Dann suchst du den größten und den kleinsten Tank.",
    "0,004 m³ = 4 000 cm³ und 3,2 dm³ = 3 200 cm³. Tank C hat 2 500 cm³. Der größte Tank ist A, der kleinste ist C: 4 000 − 2 500 = 1 500 cm³.",
    [B("4 - 2.5", "die Zahlen ohne Umrechnung verglichen"), B("4000 - 3200", "den mittleren statt den kleinsten Tank genommen"), B("0.004 * 1000 - 2500", "mit 1 000 statt mit 1 000 000 umgerechnet")], "cm³"), g="verknuepfen")
# ───────── liter ─────────
a1(T, "liter", Z(
    "Eine Regentonne ist innen 50 cm lang, 40 cm breit und 60 cm hoch. Wie viele Liter passen hinein, wenn sie ganz voll ist?",
    120, "50 * 40 * 60 / 1000", "120000 / 1000", "Berechne das Volumen in cm³. Ein Liter sind 1 000 cm³.",
    "Volumen: 50 · 40 · 60 = 120 000 cm³. Mit 1 l = 1 000 cm³ sind das 120 000 : 1 000 = 120 Liter.",
    [B("50 * 40 * 60", "das Volumen in cm³ als Liter angegeben"), B("50 * 40 * 60 / 100", "durch 100 statt durch 1 000 geteilt"), B("50 * 40 * 60 / 1000000", "durch eine Million geteilt")], "l"))
a2(T, "liter", Z(
    "Kim füllt 6 Liter Saft aus einem Kanister in Becher. In jeden Becher kommen 250 ml. Wie viele Becher werden voll?",
    24, "6 * 1000 / 250", "6000 / 250", "Rechne die Liter in Milliliter um. Dann teilst du.",
    "6 l = 6 000 ml. 6 000 : 250 = 24 Becher.",
    [B("6 / 250", "ohne Umrechnung geteilt"), B("6 * 100 / 250", "mit 100 statt mit 1 000 umgerechnet"), B("6 * 1000 * 250", "malgenommen statt geteilt")]))
a3(T, "liter", Z(
    "Ein Becken ist 3 m lang, 2 m breit und 1,2 m hoch. Es ist leer. Pro Minute fließen 40 Liter hinein. Nach wie vielen Minuten steht das Wasser 0,5 m hoch?",
    75, "3 * 2 * 0.5 * 1000 / 40", "3000 / 40", "Wie viele Kubikmeter Wasser sind bei 0,5 m Höhe im Becken? Rechne in Liter um.",
    "Bei 0,5 m Höhe sind es 3 · 2 · 0,5 = 3 m³ = 3 000 Liter. 3 000 : 40 = 75 Minuten.",
    [B("3 * 2 * 1.2 * 1000 / 40", "die Zeit bis zum Rand berechnet"), B("3 * 2 * 0.5 / 40", "ohne Umrechnung in Liter geteilt"), B("3 * 2 * 0.5 * 100 / 40", "mit 100 statt mit 1 000 umgerechnet")], "Minuten"), g="verknuepfen")
# ───────── rueckwaerts ─────────
a1(T, "rueckwaerts", Z(
    "Ein quaderförmiger Karton fasst 3 600 cm³. Er ist 20 cm lang und 15 cm breit. Wie hoch ist er?",
    12, "3600 / (20 * 15)", "3600 / 300", "Teile das Volumen durch die Grundfläche.",
    "Grundfläche: 20 · 15 = 300 cm². Höhe: 3 600 : 300 = 12 cm. Probe: 300 · 12 = 3 600.",
    [B("3600 / 20", "nur durch die Länge geteilt"), B("3600 / 15", "nur durch die Breite geteilt"), B("3600 - 20 * 15", "die Grundfläche vom Volumen abgezogen")], "cm"))
a2(T, "rueckwaerts", Z(
    "Ein Sandkasten ist 2 m lang und 1,5 m breit. Hinein kommen 0,6 m³ Sand, glatt verteilt. Wie viele Zentimeter hoch liegt der Sand?",
    20, "0.6 / (2 * 1.5) * 100", "(0.6 / 3) * 100", "Teile das Volumen durch die Grundfläche. Das Ergebnis ist zuerst in Metern.",
    "Grundfläche: 2 · 1,5 = 3 m². Höhe: 0,6 : 3 = 0,2 m = 20 cm.",
    [B("0.6 / (2 * 1.5)", "die Höhe in Metern statt in Zentimetern angegeben"), B("0.6 / 2 * 100", "nur durch die Länge geteilt"), B("0.6 / 1.5 * 100", "nur durch die Breite geteilt")], "cm"))
a3(T, "rueckwaerts", Z(
    "Eine quaderförmige Dose ist innen 12 cm lang und 5 cm breit. Sie soll 1,5 Liter fassen. Damit der Deckel passt, muss oben 2 cm Platz bleiben. Wie hoch muss die Dose innen mindestens sein?",
    27, "1500 / (12 * 5) + 2", "25 + 2", "1 Liter sind 1 000 cm³. Berechne zuerst die Höhe für 1,5 Liter. Was kommt wegen des Deckels dazu?",
    "1,5 l = 1 500 cm³. Grundfläche: 12 · 5 = 60 cm². Höhe für den Inhalt: 1 500 : 60 = 25 cm. Dazu 2 cm Platz: 27 cm.",
    [B("1500 / (12 * 5)", "den Platz für den Deckel vergessen"), B("1500 / (12 * 5) - 2", "den Platz abgezogen statt addiert"), B("1500 / 12 + 2", "nur durch die Länge geteilt")], "cm"), g="rueckwaerts")
# ───────── zusammengesetzt ─────────
a1(T, "zusammengesetzt", Z(
    "Ein Sockel besteht aus zwei Teilen. Unten liegt ein Quader mit 3 dm Länge, 2 dm Breite und 1 dm Höhe. Obendrauf steht ein Würfel mit 2 dm Kante. Wie groß ist das Volumen des ganzen Sockels?",
    14, "3 * 2 * 1 + 2 * 2 * 2", "6 + 8", "Berechne das Volumen jedes Teils einzeln. Dann addierst du.",
    "Quader: 3 · 2 · 1 = 6 dm³. Würfel: 2 · 2 · 2 = 8 dm³. Zusammen 6 + 8 = 14 dm³.",
    [B("3 * 2 * 1", "nur den Quader gerechnet"), B("2 * 2 * 2", "nur den Würfel gerechnet"), B("3 * 2 * 1 * 2 * 2 * 2", "die beiden Volumen malgenommen statt addiert")], "dm³"))
a2(T, "zusammengesetzt", Z(
    "Ein Holzquader ist 10 cm lang, 8 cm breit und 6 cm hoch. Durch die Mitte wird von oben nach unten ein Loch mit quadratischem Querschnitt gebohrt: 3 cm mal 3 cm, ganz durch. Wie groß ist das Volumen des Holzes, das übrig bleibt?",
    426, "10 * 8 * 6 - 3 * 3 * 6", "480 - 54", "Berechne das Volumen des ganzen Quaders und das des Lochs. Das Loch geht über die ganze Höhe.",
    "Ganzer Quader: 10 · 8 · 6 = 480 cm³. Loch: 3 · 3 · 6 = 54 cm³. Rest: 480 − 54 = 426 cm³.",
    [B("10 * 8 * 6", "das Loch nicht abgezogen"), B("10 * 8 * 6 - 3 * 3", "nur die Fläche des Lochs abgezogen"), B("10 * 8 * 6 + 3 * 3 * 6", "das Loch dazugezählt statt abgezogen")], "cm³"))
a3(T, "zusammengesetzt", Z(
    "Ein offener Betontrog hat außen die Maße 5 m Länge, 3 m Breite und 2 m Höhe. Innen ist er ausgehöhlt: 4 m lang, 2 m breit und 1,5 m tief. Wie viele Kubikmeter Beton stecken in dem Trog?",
    18, "5 * 3 * 2 - 4 * 2 * 1.5", "30 - 12", "Der Trog ist ein großer Quader, aus dem der Hohlraum fehlt. Berechne beide Volumen.",
    "Außen: 5 · 3 · 2 = 30 m³. Hohlraum: 4 · 2 · 1,5 = 12 m³. Beton: 30 − 12 = 18 m³.",
    [B("5 * 3 * 2", "den Hohlraum nicht abgezogen"), B("4 * 2 * 1.5", "nur den Hohlraum gerechnet"), B("5 * 3 * 2 - 4 * 2 * 2", "den Hohlraum 2 m statt 1,5 m tief gerechnet")], "m³"), g="transfer")
# ───────── verstehen ─────────
a1(T, "verstehen", Z(
    "Ein Schrank ist 1,9 m hoch, 0,6 m breit und 0,5 m tief. Zum Überschlag rundet Kim auf 2 m, 0,5 m und 0,5 m. Wie viele Kubikmeter ergibt der Überschlag?",
    0.5, "2 * 0.5 * 0.5", "2 * 0.25", "Beim Überschlag rechnest du mit den gerundeten Kanten: Länge mal Breite mal Höhe.",
    "Mit den gerundeten Werten: 2 · 0,5 · 0,5 = 0,5 m³. Das genaue Volumen (0,57 m³) liegt nahe dabei.",
    [B("2 + 0.5 + 0.5", "die gerundeten Kanten addiert"), B("2 * 0.5", "nur zwei der drei Kanten malgenommen"), B("1.9 * 0.6 * 0.5", "genau gerechnet statt überschlagen")], "m³"))
a2(T, "verstehen", Z(
    "Ein Quader hat das Volumen 20 cm³. Seine Länge und seine Breite werden jeweils verdoppelt. Die Höhe bleibt gleich. Wie groß ist jetzt das Volumen?",
    80, "20 * 2 * 2", "20 * 4", "Wie oft passt der alte Quader in den neuen? Die Länge wird doppelt so groß und die Breite auch.",
    "Der Faktor 2 wirkt zweimal: 2 · 2 = 4. Das neue Volumen ist 20 · 4 = 80 cm³.",
    [B("20 * 2", "den Faktor nur einmal angewendet"), B("20 * 2 * 2 * 2", "auch die Höhe verdoppelt"), B("20 + 2 + 2", "die 2 addiert statt malgenommen")], "cm³"))
a3(T, "verstehen", Z(
    "Ein Quader ist 2 cm lang, 3 cm breit und 4 cm hoch. Kim sagt: „Halbiere ich alle drei Kanten, wird auch das Volumen halbiert.“ Kim rechnet deshalb mit 12 cm³. Um wie viele Kubikzentimeter ist Kims Wert zu groß?",
    9, "24 / 2 - 24 / 8", "12 - 3", "Das Volumen des Quaders ist 24 cm³. Halbierst du jede der drei Kanten, wirkt der Faktor ein halbes dreimal.",
    "Der Faktor 1/2 wirkt dreimal: 24 · 1/8 = 3 cm³. Kims Wert 12 cm³ ist 12 − 3 = 9 cm³ zu groß.",
    [B("24 / 2", "Kims falschen Wert angegeben"), B("24 / 8", "das richtige neue Volumen angegeben"), B("24 / 4", "nur zwei Kanten halbiert")], "cm³"), g="fehler")
