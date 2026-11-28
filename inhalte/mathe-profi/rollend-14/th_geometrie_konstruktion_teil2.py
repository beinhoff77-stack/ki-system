T = "geometrie.konstruktion_teil2"
# ───────── vierecke: Winkel in symmetrischen Vierecken ─────────
a1(T, "vierecke", Z(
    "Ein Drachen aus Papier hat die Form eines Drachenvierecks ABCD. Die Symmetrieachse ist die Diagonale AC. Der Winkel bei A ist 70° und der Winkel bei C ist 50°. Wie groß ist der Winkel bei B?",
    120, "(360 - 70 - 50) / 2", "(360 - 120) / 2", "Welche beiden Winkel sind gleich groß? Alle vier Winkel zusammen ergeben 360°.",
    "Die Winkel bei B und D sind gleich, weil die Figur symmetrisch zu AC ist. Alle vier Winkel ergeben 360°. Also ist 360° − 70° − 50° = 240° der Rest. Er verteilt sich auf zwei gleiche Winkel: 240° : 2 = 120°.",
    [(240, None, "den Rest nicht auf B und D verteilt, also beide Winkel zusammen angegeben", "360 - 70 - 50"), (30, None, "mit der Winkelsumme 180° statt 360° gerechnet: (180° − 70° − 50°) : 2", "(180 - 70 - 50) / 2"), (145, None, "den Winkel bei C vergessen und den Rest halbiert", "(360 - 70) / 2")], "°"))
a2(T, "vierecke", Z(
    "Ein Fensterrahmen hat die Form eines Parallelogramms ABCD. Der Winkel bei A ist dreimal so groß wie der Winkel bei B. Wie groß ist der Winkel bei A?",
    135, "180 / 4 * 3", "180 - 180 / 4", "Welche Summe haben zwei benachbarte Winkel im Parallelogramm? Aus wie vielen gleichen Teilen besteht diese Summe?",
    "Benachbarte Winkel im Parallelogramm ergeben zusammen 180°. Der Winkel bei A besteht aus 3 Teilen, der Winkel bei B aus 1 Teil, zusammen 4 Teile. Ein Teil ist 180° : 4 = 45°. Der Winkel bei A ist 3 · 45° = 135°. Probe: 135° + 45° = 180°.",
    [(45, None, "den kleineren Winkel bei B angegeben", "180 / 4"), (60, None, "durch 3 statt durch 4 Teile geteilt und den einen Teil als Antwort angegeben", "180 / 3"), (540, None, "dreimal 180° gerechnet", "3 * 180")], "°"))
a3(T, "vierecke", Z(
    "In einer Raute ABCD bildet die Diagonale AC mit der Seite AB einen Winkel von 28°. Sam baut die Raute aus vier gleich langen Holzstäben nach. Wie groß ist der Winkel bei B?",
    124, "180 - 2 * 28", "180 - 56", "Die Diagonale halbiert den Winkel bei A. Welcher Winkel ist ein Nachbar des Winkels bei A?",
    "Die Diagonale AC halbiert den Winkel bei A, also ist der Winkel bei A gleich 2 · 28° = 56°. Benachbarte Winkel in der Raute ergeben zusammen 180°. Der Winkel bei B ist 180° − 56° = 124°.",
    [(152, None, "den Winkel von 28° nicht verdoppelt: 180° − 28°", "180 - 28"), (56, None, "den Winkel bei A statt bei B angegeben", "2 * 28"), (62, None, "den Nachbarwinkel noch einmal halbiert", "(180 - 56) / 2")], "°"), g="verknuepfen")
# ───────── vierecke_konstruieren ─────────
a1(T, "vierecke_konstruieren", Z(
    "Für ein Bastelprojekt sollst du ein Quadrat, eine Raute, ein Rechteck und ein Parallelogramm zeichnen. Jede Figur wird für sich und unabhängig von den anderen mit möglichst wenigen einzelnen Angaben (Seitenlängen oder Winkel) so festgelegt, dass sie bis auf Lage und Drehung eindeutig ist. Wie viele Angaben brauchst du für alle vier Figuren zusammen?",
    8, "1 + 2 + 2 + 3", "3 + 2 + 2 + 1", "Wie viele Bestimmungsstücke braucht jede der vier Figuren einzeln?",
    "Ein Quadrat braucht 1 Stück (die Seite). Eine Raute braucht 2 Stücke, ein Rechteck 2 Stücke, ein Parallelogramm 3 Stücke. Zusammen: 1 + 2 + 2 + 3 = 8 Angaben.",
    [(10, None, "für Raute und Rechteck je 3 Stücke gezählt", "1 + 3 + 3 + 3"), (20, None, "für jede Figur 5 Stücke wie bei einem beliebigen Viereck gezählt", "4 * 5"), (4, None, "nur ein Stück je Figur gezählt", "4 * 1")]))
a2(T, "vierecke_konstruieren", Z(
    "Noa konstruiert ein Drachenviereck ABCD mit der Symmetrieachse AC. Gezeichnet sind schon die Seite AB, der Winkel bei A (100°) und der Winkel bei B (70°). Nun trägt Noa den letzten Winkel bei C an. Wie groß muss dieser Winkel sein?",
    120, "360 - 100 - 2 * 70", "360 - 240", "Welche zwei Winkel sind gleich groß? Bedenke die Winkelsumme im Viereck.",
    "Die Figur ist symmetrisch zu AC, also sind die Winkel bei B und D gleich: 70° und 70°. Alle vier Winkel ergeben 360°. Der Winkel bei C ist 360° − 100° − 70° − 70° = 120°.",
    [(190, None, "den gleich großen Winkel bei D vergessen", "360 - 100 - 70"), (10, None, "mit der Winkelsumme 180° wie im Dreieck gerechnet und dabei den Winkel bei D weggelassen", "180 - 100 - 70"), (95, None, "den Winkel bei D vergessen und den Rest dann nur halbiert", "(360 - 100 - 70) / 2")], "°"))
a3(T, "vierecke_konstruieren", Z(
    "Du konstruierst ein Schild in Form eines Parallelogramms ABCD: Du zeichnest die Seite AB und trägst bei A und bei B die Winkel an. Der stumpfe Winkel bei B ist um 36° kleiner als das Dreifache des spitzen Winkels bei A. Unter welchem Winkel (in Grad) trägst du bei B an?",
    126, "180 - (180 + 36) / 4", "3 * 54 - 36", "Benachbarte Winkel ergeben zusammen 180°. Schreibe den Winkel bei B mit dem Winkel bei A auf.",
    "Es gilt α + β = 180° und β = 3α − 36°. Einsetzen: α + 3α − 36° = 180°, also 4α = 216° und α = 54°. Dann ist β = 180° − 54° = 126°. Probe: 3 · 54° − 36° = 126°.",
    [(54, None, "den spitzen Winkel bei A statt den stumpfen bei B angegeben", "(180 + 36) / 4"), (144, None, "nur 180° − 36° gerechnet", "180 - 36"), (216, None, "den Rest 4α = 216° als Winkel angegeben", "180 + 36")], "°"), g="rueckwaerts")
