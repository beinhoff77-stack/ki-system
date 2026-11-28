T = "geometrie.konstruktion"
D = "id.geometrie.deckungsgleich"
WI = "id.geometrie.winkel"
OHNE_UNGL = "Dreiecksungleichung (zwei Seiten zusammen länger als die dritte): keine Regel des Katalogs trägt den Lösungsweg"
OHNE_SATZ = "Satz und Kehrsatz (Logik, Gegenbeispiel): keine Regel des Katalogs trägt den Lösungsweg"
# ───────── gleichschenklig ─────────
neu(T, "gleichschenklig", "lueckenweg", L(
    "Ein gleichschenkliges Dreieck hat an der Spitze den Winkel 40°. Die beiden Basiswinkel zusammen messen ①°. Jeder Basiswinkel misst ②°. Ein Basiswinkel und der Winkel an der Spitze zusammen messen ③°.",
    "① = □; ② = □; ③ = □", [140, 70, 110], ["180 - 40", "{1} / 2", "{2} + 40"], ["140", "70", "110"],
    "Die Winkelsumme im Dreieck ist 180°. Die Basiswinkel sind gleich groß.",
    "Die Basiswinkel zusammen: 180° − 40° = 140°. Jeder Basiswinkel: 140° : 2 = 70°. Ein Basiswinkel plus Spitzenwinkel: 70° + 40° = 110°.",
    {0: [(40, None, "den Winkel an der Spitze als Summe der Basiswinkel genommen", "40")], 1: [(140, None, "die Summe der Basiswinkel nicht geteilt", "{1}")], 2: [(180, None, "alle drei Winkel addiert", "{1} + 40")]}), g="direkt", regel=WI)
neu(T, "gleichschenklig", "anwenden", Z(
    "Der Giebel eines Hauses ist ein gleichschenkliges Dreieck. An der Dachtraufe, also an der Basis, misst jeder Winkel 38°. Wie groß ist der Winkel am First an der Spitze?",
    104, "180 - 2 * 38", "180 - 38 - 38", "Beide Basiswinkel sind gleich groß, beide kommen in die Winkelsumme.",
    "Die zwei Basiswinkel zusammen messen 2 · 38° = 76°. Der Winkel an der Spitze ist 180° − 76° = 104°.",
    [B("180 - 38", "nur einen Basiswinkel von 180° abgezogen"), B("2 * 38", "nur die beiden Basiswinkel zusammengezählt"), B("(180 - 38) / 2", "wie beim Berechnen des Basiswinkels gerechnet, obwohl dieser schon bekannt ist")], einheit="°"), g="einkleidung", regel=WI)
neu(T, "gleichschenklig", "fehler_detektiv", FD(
    "Ein gleichschenkliges Dreieck hat die Basiswinkel 52°. Kim berechnet den Winkel an der Spitze:",
    [("Im gleichschenkligen Dreieck sind die beiden Basiswinkel gleich groß.", True, True),
     ("Beide Basiswinkel zusammen messen 52° + 52° = 104°.", 52 + 52 == 104, True),
     ("Von der Winkelsumme bleibt nach einem Basiswinkel der Rest übrig, also misst der Winkel an der Spitze 128°.", 180 - 52 == 76, True)],
    "Wie viele Winkel gehören zur Summe von 180°? Welche kennst du schon?",
    "Von den 180° müssen beide Basiswinkel abgezogen werden: 180° − 104° = 76°. Kim hat in Zeile 3 nur einen Basiswinkel abgezogen. Die Zeilen 1 und 2 sind richtig."), g="fehler", regel=WI)
# ───────── kongruenzsatz ─────────
neu(T, "kongruenzsatz", "anwenden", W(
    "Zwei Zimmerleute bauen dreieckige Dachrahmen aus Balken. Kim gibt vor: zwei Balken mit 5 m und 7 m Länge, die an der Ecke einen Winkel von 40° einschließen. Welcher Kongruenzsatz sichert, dass alle so gebauten Rahmen deckungsgleich sind?",
    "SWS: zwei Seiten und der eingeschlossene Winkel", [("SSS: drei Seiten", "es ist nur von zwei Seiten die Rede"), ("WSW: eine Seite und zwei anliegende Winkel", "es ist nur ein Winkel gegeben"), ("SsW: zwei Seiten und der Winkel der größeren Seite gegenüber", "der Winkel liegt zwischen den Seiten und nicht der größeren gegenüber")],
    "Wo liegt der gegebene Winkel: zwischen den zwei gegebenen Seiten oder gegenüber einer von ihnen?",
    "Gegeben sind zwei Seiten (5 m und 7 m) und der Winkel zwischen ihnen. Das ist der Satz SWS: Alle Dreiecke mit diesen Angaben sind deckungsgleich.",
    lambda: True), g="einkleidung", regel=D)
neu(T, "kongruenzsatz", "verfahren_waehlen", W(
    "Welche dieser Angaben legt genau ein Dreieck fest (alle so konstruierten Dreiecke sind deckungsgleich)?",
    "c = 6 cm, α = 50°, β = 70°",
    [("α = 40°, β = 60°, γ = 80°", "nur Winkel: die Größe des Dreiecks bleibt offen"), ("a = 3 cm, b = 4 cm, c = 8 cm", "aus diesen Seiten lässt sich gar kein Dreieck bauen"), ("a = 5 cm, b = 7 cm, α = 40° (α liegt der Seite a gegenüber)", "der Winkel liegt der kleineren Seite gegenüber, es gibt zwei verschiedene Dreiecke")],
    "Prüfe jede Angabe: Gibt es einen Kongruenzsatz dazu? Die Seiten müssen außerdem ein Dreieck ergeben.",
    "Bei c = 6 cm, α = 50° und β = 70° liegen die Winkel an der gegebenen Seite: Das ist WSW, das Dreieck ist festgelegt. Drei Winkel allein legen nur die Form fest. Bei 3 cm, 4 cm und 8 cm ist 3 + 4 = 7 < 8, es gibt kein Dreieck. Bei SsW müsste der Winkel der größeren Seite (7 cm) gegenüberliegen; hier liegt er der kleineren gegenüber (a = 5 cm < b = 7 cm). Zeichnet man b = 7 cm und bei A den Winkel 40°, hat C vom freien Schenkel nur etwa 4,5 cm Abstand: Der Kreis um C mit Radius a = 5 cm schneidet den Schenkel in zwei Punkten, es gibt zwei verschiedene Dreiecke.",
    lambda: 3 + 4 < 8 and 7 * math.sin(math.radians(40)) < 5 < 7), g="mehrschritt", regel=D)
neu(T, "kongruenzsatz", "fehler_detektiv", FD(
    "Zwei Dreiecke haben jeweils die Winkel 50°, 60° und 70°. Alex will ihre Umfänge vergleichen und schreibt auf:",
    [("Beide Dreiecke haben die Winkel 50°, 60° und 70°.", True, True),
     ("Alle drei Winkel stimmen überein, also sind die Dreiecke deckungsgleich.", False, True),
     ("Deckungsgleiche Dreiecke haben denselben Umfang, also haben beide Dreiecke denselben Umfang.", True, True)],
    "Ein großes und ein kleines Dreieck können dieselben Winkel haben. Welche Angabe fehlt, damit die Größe festgelegt ist?",
    "Gleiche Winkel legen nur die Form fest, nicht die Größe: Ein kleines und ein großes Dreieck können dieselben Winkel haben. Für Deckungsgleichheit braucht man mindestens eine passende Seite (etwa WSW). Der Fehler steckt in Zeile 2. Zeile 3 ist aus Zeile 2 richtig gefolgert.",
    rueck={2: "Diese Zeile ist für sich richtig: Deckungsgleiche Dreiecke haben denselben Umfang. Falsch war schon Zeile 2, deshalb darf man diese Regel hier nicht anwenden."}), g="fehler", regel=D)
# ───────── konstruierbar ─────────
neu(T, "konstruierbar", "anwenden", Z(
    "Zwei Zeltstangen sind 4 m und 9 m lang. Mit einer dritten Stange, deren Länge eine ganze Zahl in Metern ist, soll ein Dreieck entstehen. Wie lang darf die dritte Stange höchstens sein?",
    12, "4 + 9 - 1", max(c for c in range(1, 40) if 4 + 9 > c and 4 + c > 9 and 9 + c > 4), "Je zwei Seiten müssen zusammen länger sein als die dritte. Welche Bedingung gilt für die längste Seite?",
    "Die dritte Seite c muss kürzer sein als 4 + 9 = 13 (und länger als 9 − 4 = 5). Die größte ganze Zahl unter 13 ist 12. Bei 13 würden die Stangen flach aufeinanderliegen.",
    [B("4 + 9", "die Summe selbst erlaubt, obwohl dann nur eine flache Figur entsteht"), B("9 - 4", "den Unterschied als größte Länge genommen"), B("9", "die längste gegebene Stange als Grenze genommen")], einheit="m"), g="mehrschritt", ohne=OHNE_UNGL)
neu(T, "konstruierbar", "lueckenweg", L(
    "Zwei Seiten eines Dreiecks sind 5 cm und 8 cm lang. Die dritte Seite c muss kürzer als ① cm sein und länger als ② cm. Wenn c eine ganze Zahl in Zentimetern ist, gibt es ③ Möglichkeiten.",
    "① = □; ② = □; ③ = □", [13, 3, 9], ["5 + 8", "8 - 5", "{1} - {2} - 1"], ["13", "3", "9"],
    "Je zwei Seiten müssen zusammen länger sein als die dritte. Die dritte Seite liegt zwischen der Summe und dem Unterschied der beiden anderen.",
    "c < 5 + 8 = 13 und c > 8 − 5 = 3. Ganze Zahlen von 4 bis 12 (genau c = 4, 5, 6, 7, 8, 9, 10, 11, 12): Das sind 12 − 4 + 1 = 9 Möglichkeiten (13 − 3 − 1 = 9).",
    {0: [(3, None, "den Unterschied statt der Summe der Seiten genommen", "8 - 5")], 1: [(13, None, "die Summe statt des Unterschieds genommen", "5 + 8")], 2: [(10, None, "nur 13 − 3 gerechnet und die Grenzen nicht beachtet", "{1} - {2}")]}), g="direkt", ohne=OHNE_UNGL)
neu(T, "konstruierbar", "verfahren_waehlen", W(
    "Kim behauptet: „Aus Stäben von 3 cm, 4 cm und 7 cm kann man ein Dreieck bilden, denn 3 + 4 = 7.“ Was stimmt?",
    "Es entsteht kein Dreieck: Die zwei kürzeren Stäbe müssen zusammen länger sein als der längste. Bei 3 + 4 = 7 liegen sie flach aufeinander.",
    [("Es entsteht ein Dreieck, denn die zwei kürzeren Stäbe sind zusammen nicht kürzer als der längste.", "„nicht kürzer“ genügt nicht, sie müssen länger sein"), ("Es entsteht ein sehr flaches, aber echtes Dreieck.", "aus einem flachen Stab-Paar wird kein Dreieck mit drei Ecken"),
     ("Es entsteht kein Dreieck, weil 7 eine Primzahl ist.", "Primzahlen haben mit der Konstruierbarkeit nichts zu tun")],
    "Prüfe die Bedingung für die längste Seite: Müssen die beiden anderen zusammen länger sein, oder reicht gleich lang?",
    "Ein Dreieck braucht: zwei Seiten zusammen länger als die dritte. Hier gilt 3 + 4 = 7, nicht länger. Die beiden kurzen Stäbe würden genau auf dem langen Stab liegen, die drei Ecken fallen auf eine Gerade.",
    lambda: 3 + 4 == 7), g="pruefung", ohne=OHNE_UNGL)
# ───────── planfigur ─────────
neu(T, "planfigur", "anwenden", Z(
    "Eine Konstruktionsbeschreibung lautet: 1. Zeichne [AB] mit 7 cm. 2. Zeichne um A einen Kreis mit 5 cm Radius. 3. Zeichne um B einen Kreis mit 6 cm Radius. 4. Ein Schnittpunkt der Kreise ist C. Wie groß ist der Umfang des Dreiecks ABC?",
    18, "7 + 5 + 6", 18, "Der Punkt C liegt auf beiden Kreisen. Welche Entfernungen hat C von A und von B?",
    "C liegt auf dem Kreis um A, also ist AC = 5 cm, und auf dem Kreis um B, also ist BC = 6 cm. Mit AB = 7 cm ist der Umfang 7 + 5 + 6 = 18 cm.",
    [B("5 + 6", "die Seite [AB] vergessen"), B("7 + 5", "die Seite [BC] vergessen"), B("7 * 5 * 6", "die drei Längen malgenommen statt addiert")], einheit="cm"), g="einkleidung", regel=D)
neu(T, "planfigur", "verfahren_waehlen", W(
    "Du sollst ein Dreieck ABC mit c = 6 cm, α = 35° (bei A) und β = 70° (bei B) konstruieren. Welche Reihenfolge der Schritte ist richtig?",
    "Strecke [AB] mit 6 cm zeichnen. Bei A den Winkel 35° antragen und bei B den Winkel 70° antragen. Der Schnittpunkt der beiden freien Schenkel ist C.",
    [("Strecke [AB] mit 6 cm zeichnen. Um A einen Kreis mit 35 cm und um B einen Kreis mit 70 cm Radius zeichnen.", "Winkelangaben als Radien benutzt"), ("Bei A den Winkel 35° zeichnen, bei B den Winkel 70° zeichnen. Danach die Strecke [AB] von 6 cm in das entstandene Dreieck einpassen.", "ohne die Seite zu beginnen geht es nicht, die Größe wäre offen"),
     ("Strecke [AB] mit 6 cm zeichnen. Bei A den Winkel 70° und bei B den Winkel 35° antragen.", "die Winkel an den falschen Ecken angetragen: 70° gehört zu β bei B, 35° zu α bei A")],
    "Beginne mit der Seite, die du kennst. Welcher Winkel gehört an welche Ecke?",
    "Mit der gegebenen Seite beginnen: [AB] = 6 cm. Dann α = 35° bei A und β = 70° bei B antragen. Die Schenkel schneiden sich in C. Das ist die Konstruktion nach WSW.",
    lambda: True), g="mehrschritt", regel=D)
neu(T, "planfigur", "umkehren", Z(
    "Ein Dreieck soll aus der Seite c = 10 cm und den Winkeln α = 50° und γ = 70° konstruiert werden. Zum Antragen an der Seite c braucht man die Winkel an ihren beiden Enden. Wie groß ist der Winkel β bei B?",
    60, "180 - 50 - 70", 60, "Von den drei Winkeln liegt einer nicht an der Seite c. Welchen Winkel kannst du mit der Winkelsumme berechnen?",
    "Die Winkelsumme im Dreieck ist 180°. β = 180° − 50° − 70° = 60°. Jetzt kann man bei A den Winkel 50° und bei B den Winkel 60° an die Seite [AB] antragen.",
    [B("180 - 70", "nur einen der beiden bekannten Winkel abgezogen"), B("50 + 70", "die beiden bekannten Winkel addiert"), B("360 - 50 - 70", "von 360° statt von 180° abgezogen")], einheit="°"), g="rueckwaerts", regel=WI)
# ───────── satz_kehrsatz ─────────
neu(T, "satz_kehrsatz", "anwenden", W(
    "Der Satz lautet: „Wenn eine Zahl durch 6 teilbar ist, dann ist sie gerade.“ Welche Aussage nennt den Kehrsatz und beurteilt ihn richtig?",
    "Kehrsatz: „Wenn eine Zahl gerade ist, dann ist sie durch 6 teilbar.“ Er ist falsch, denn 8 ist gerade, aber nicht durch 6 teilbar.",
    [("Kehrsatz: „Wenn eine Zahl nicht durch 6 teilbar ist, dann ist sie nicht gerade.“ Er ist wahr.", "Wenn und Dann nicht vertauscht, sondern beide verneint"), ("Kehrsatz: „Wenn eine Zahl gerade ist, dann ist sie durch 6 teilbar.“ Er ist wahr, denn der Satz ist wahr.", "aus der Wahrheit des Satzes auf den Kehrsatz geschlossen"),
     ("Kehrsatz: „Wenn eine Zahl durch 6 teilbar ist, dann ist sie durch 2 teilbar.“ Er ist wahr.", "den Satz nur umformuliert statt Wenn und Dann vertauscht")],
    "Beim Kehrsatz werden Wenn-Teil und Dann-Teil vertauscht. Suche danach eine gerade Zahl, die nicht durch 6 teilbar ist.",
    "Der Satz hat die Form „Wenn A, dann B“ mit A: durch 6 teilbar und B: gerade. Der Kehrsatz heißt „Wenn B, dann A“. Er ist falsch: 8 ist gerade, aber 8 : 6 geht nicht auf. Ein Gegenbeispiel genügt.",
    lambda: 8 % 2 == 0 and 8 % 6 != 0 and all(n % 2 == 0 for n in range(0, 100, 6))), g="einkleidung", ohne=OHNE_SATZ)
neu(T, "satz_kehrsatz", "umkehren", W(
    "Der Satz „Wenn ein Viereck ein Quadrat ist, dann sind seine Diagonalen gleich lang“ ist wahr. Sein Kehrsatz ist falsch. Welches Viereck ist ein Gegenbeispiel zum Kehrsatz?",
    "ein Rechteck mit den Seiten 3 cm und 4 cm", [("eine Raute mit der Seite 5 cm, die kein Quadrat ist", "bei dieser Raute, die kein Quadrat ist, sind die Diagonalen verschieden lang"), ("ein Parallelogramm mit den Seiten 3 cm und 5 cm und einem Winkel von 60°", "bei diesem Parallelogramm sind die Diagonalen verschieden lang (7 cm und etwa 4,36 cm)"), ("ein Quadrat mit der Seite 4 cm", "ein Quadrat erfüllt den Kehrsatz, es widerlegt ihn nicht")],
    "Der Kehrsatz lautet: Wenn die Diagonalen gleich lang sind, ist das Viereck ein Quadrat. Gesucht ist ein Viereck mit gleich langen Diagonalen, das kein Quadrat ist.",
    "Beim Rechteck sind die beiden Diagonalen gleich lang. Hat das Rechteck unterschiedliche Seiten (3 cm und 4 cm), ist es kein Quadrat. Damit ist der Kehrsatz widerlegt. Bei der angebotenen Raute (kein Quadrat) und bei dem Parallelogramm mit 3 cm, 5 cm und 60° sind die Diagonalen verschieden lang.",
    lambda: abs(math.sqrt(9 + 25 + 15) - math.sqrt(9 + 25 - 15)) > 1), g="begruenden", ohne=OHNE_SATZ)
saetze = {"gleichseitiges Dreieck / alle Winkel 60°": True, "durch 10 teilbar / durch 5 teilbar": False, "vier gleich lange Seiten / Raute": True, "durch 4 teilbar / gerade": False}
neu(T, "satz_kehrsatz", "anwenden", Z(
    "Wie viele dieser vier Sätze bleiben wahr, wenn man sie umkehrt? (1) Wenn ein Dreieck gleichseitig ist, dann sind alle seine Winkel 60° groß. (2) Wenn eine Zahl durch 10 teilbar ist, dann ist sie durch 5 teilbar. (3) Wenn ein Viereck eine Raute ist, dann hat es vier gleich lange Seiten. (4) Wenn eine Zahl durch 4 teilbar ist, dann ist sie gerade.",
    2, "2", sum(saetze.values()), "Kehre jeden Satz um und suche ein Gegenbeispiel. Eine Zahl, die durch 5, aber nicht durch 10 teilbar ist, hilft bei Satz (2).",
    "Die Kehrsätze: (1) Wenn alle Winkel 60° sind, ist das Dreieck gleichseitig: wahr. (2) Wenn eine Zahl durch 5 teilbar ist, ist sie durch 10 teilbar: falsch (Gegenbeispiel 15). (3) Wenn ein Viereck vier gleich lange Seiten hat, ist es eine Raute: wahr. (4) Wenn eine Zahl gerade ist, ist sie durch 4 teilbar: falsch (Gegenbeispiel 6). Zwei Sätze bleiben wahr.",
    [B("4", "alle vier Sätze für umkehrbar gehalten"), B("0", "keinen Kehrsatz für wahr gehalten"), B("3", "bei einem der falschen Kehrsätze das Gegenbeispiel übersehen")]), g="pruefung", ohne=OHNE_SATZ)
