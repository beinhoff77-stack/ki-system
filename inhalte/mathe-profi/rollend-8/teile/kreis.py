"""geometrie.kreis (Klasse 7): 6 Lernkarten, 18 Aufgaben in neuer Form.

Ohne Zeichnungen: Jede Figur ist im Text beschrieben (Bauteile werden nicht neu eingeführt).
"""
STAND = "2026-11-27"
TITEL = "Kreis, Thales und Tangenten"
PASST_NICHT = ()

AB = "id.geometrie.abstand"
DG = "id.geometrie.deckungsgleich"

AUFGABEN = [
    # ---------------- thales ----------------
    {
        "k": "K7-V046", "karte": "thales", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Im Dreieck ABC ist [AB] ein Durchmesser des Kreises, C liegt auf dem Kreis. Bei A sind 28°. "
                "Nach dem Satz des Thales ist der Winkel bei C ① °. "
                "Für den Winkel bei B bleiben 180° − ① ° − 28° = ② °.",
        "schablone": "① = □; ② = □",
        "c": ["90", "180 - 90 - 28"], "erwartet": [90, 62],
        "h": "C liegt auf dem Thaleskreis.",
        "w": "Bei C ist ein rechter Winkel, also 90°. Dann bleiben 180° − 90° − 28° = 62° für den Winkel bei B.",
        "fehlbilder": [{"luecke": 2, "antwort": 152, "beschreibung": "nur den rechten Winkel abgezogen"}],
    },
    {
        "k": "K7-V047", "karte": "thales", "typ": "UM", "s": 2, "y": "zahl", "regel": DG,
        "text": "Im Dreieck ABC liegt C auf dem Kreis über dem Durchmesser [AB]. "
                "Der Winkel bei B ist doppelt so groß wie der Winkel bei A. Wie groß ist der Winkel bei A?",
        "c": "90 // 3", "erwartet": 30, "einheit": "°",
        "h": "Die Winkel bei A und B ergeben zusammen 90°.",
        "w": "Bei C sind 90°, also bleiben für A und B zusammen 90°. Mit β = 2α folgt 3α = 90°, also α = 30°.",
        "fehlbilder": [{"antwort": 60, "beschreibung": "den doppelten Winkel genannt"},
                       {"antwort": 45, "beschreibung": "beide Winkel gleich groß angenommen"}],
    },
    {
        "k": "K7-V048", "karte": "thales", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind untersucht ein Dreieck ABC. "
                "Zeile 1: A und B liegen auf dem Kreis, die Strecke [AB] geht aber nicht durch den Mittelpunkt. "
                "Zeile 2: Der Punkt C liegt ebenfalls auf dem Kreis. "
                "Zeile 3: Nach dem Satz des Thales ist der Winkel bei C deshalb 90°. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Welche Bedingung muss die Strecke [AB] erfüllen?",
        "w": "Zeile 1 und 2 beschreiben nur die Lage der Punkte. Der Satz des Thales gilt aber erst, wenn [AB] ein "
             "Durchmesser ist. Ohne das ist der Winkel bei C meist kein rechter.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, sie beschreibt nur die Lage"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig, C darf auf dem Kreis liegen"},
        ],
    },
    # ---------------- umkehrung ----------------
    {
        "k": "K7-V049", "karte": "umkehrung", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Bei C ist ein rechter Winkel, und es ist A(1 | 2) und B(9 | 2). Dann liegt C auf dem Kreis über [AB]. "
                "Sein Mittelpunkt ist die Mitte von [AB], also M(① | 2). Die Strecke [AB] ist ② lang; "
                "der Radius ist halb so groß.",
        "schablone": "① = □; ② = □",
        "c": ["(1 + 9) // 2", "9 - 1"], "erwartet": [5, 8],
        "h": "Die Mitte liegt genau zwischen den beiden x-Werten.",
        "w": "Die Mitte von 1 und 9 ist (1 + 9) : 2 = 5, also M(5 | 2). [AB] ist 9 − 1 = 8 lang, der Radius ist 4.",
        "fehlbilder": [{"luecke": 1, "antwort": 4, "beschreibung": "den Radius statt der Mitte eingesetzt"}],
    },
    {
        "k": "K7-V050", "karte": "umkehrung", "typ": "BR", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Ein Satz lautet: „Der Punkt C liegt auf dem Kreis über dem Durchmesser [AB].“ "
                "Was folgt daraus für das Dreieck ABC?",
        "a": ["Bei C sind 90°.", "Bei A sind 90°.", "Alle drei Winkel sind gleich groß.", "Das Dreieck ist gleichseitig."],
        "richtig": 0,
        "h": "Der rechte Winkel liegt an der Ecke, die auf dem Kreis liegt.",
        "w": "Nach dem Satz des Thales ist der Winkel an der Ecke auf dem Kreis ein rechter: bei C sind 90°. "
             "Über die anderen Winkel sagt der Satz nichts.",
        "fehlbilder": [
            {"index": 1, "antwort": "Bei A sind 90°.", "beschreibung": "A liegt auf dem Durchmesser, nicht auf dem Kreisbogen"},
            {"index": 2, "antwort": "Alle drei Winkel sind gleich groß.", "beschreibung": "das wäre ein gleichseitiges Dreieck mit 60°"},
            {"index": 3, "antwort": "Das Dreieck ist gleichseitig.", "beschreibung": "mit einem rechten Winkel ist das unmöglich"},
        ],
    },
    {
        "k": "K7-V051", "karte": "umkehrung", "typ": "AN", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Tischler prüft, ob eine Ecke seines Bretts genau 90° hat. Die gegenüberliegende Kante ist "
                "50 cm lang. Er sticht in deren Mitte ein und misst von dort bis zur Ecke. "
                "Welchen Abstand muss er finden, wenn der Winkel genau 90° ist?",
        "c": "50 // 2", "erwartet": 25, "einheit": "cm",
        "h": "Bei genau 90° liegt die Ecke auf dem Thaleskreis über der Kante.",
        "w": "Der Kreis über der 50 cm langen Kante hat den Radius 50 cm : 2 = 25 cm. Liegt die Ecke auf diesem "
             "Kreis, ist der Winkel 90°, der Abstand muss also 25 cm sein.",
        "fehlbilder": [{"antwort": 50, "beschreibung": "die ganze Kante als Abstand genommen"},
                       {"antwort": 100, "beschreibung": "verdoppelt statt halbiert"}],
    },
    # ---------------- beweis ----------------
    {
        "k": "K7-V052", "karte": "beweis", "typ": "VW", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Du sollst zeigen, dass bei jedem Punkt C auf dem Thaleskreis ein rechter Winkel entsteht. "
                "Welches Vorgehen ist ein Beweis?",
        "a": ["mit den gleich langen Radien MA, MB und MC argumentieren",
              "zwanzig Beispiele zeichnen und nachmessen",
              "ein besonders großes Dreieck zeichnen und messen",
              "den Satz in einem Buch nachlesen"],
        "richtig": 0,
        "h": "Ein Beweis muss für alle Punkte gelten, nicht nur für die gemessenen.",
        "w": "MA, MB und MC sind Radien, also gleich lang. Daraus ergeben sich zwei gleichschenklige Dreiecke, "
             "und die Winkelsumme führt auf 90° bei C – für jeden Punkt C. Messen liefert nur eine Vermutung.",
        "fehlbilder": [
            {"index": 1, "antwort": "zwanzig Beispiele zeichnen und nachmessen", "beschreibung": "Beispiele zeigen nur diese zwanzig Fälle"},
            {"index": 2, "antwort": "ein besonders großes Dreieck zeichnen und messen", "beschreibung": "ein Beispiel bleibt ein Beispiel, auch ein großes"},
            {"index": 3, "antwort": "den Satz in einem Buch nachlesen", "beschreibung": "Nachlesen ersetzt die Begründung nicht"},
        ],
    },
    {
        "k": "K7-V053", "karte": "beweis", "typ": "ZW", "s": 2, "y": "zahl", "regel": DG,
        "text": "Im Dreieck ABC ist [AB] ein Durchmesser, der Winkel bei A ist 40°. "
                "Weg A: 180° − 90° − 40° rechnen. "
                "Weg B: Im gleichschenkligen Dreieck AMC ist der Winkel bei M 100°, also ist der Winkel BMC 80°; "
                "im gleichschenkligen Dreieck BMC sind die beiden Basiswinkel gleich groß. "
                "Wie groß ist der Winkel bei B?",
        "c": "180 - 90 - 40", "erwartet": 50, "einheit": "°",
        "h": "Beide Wege müssen denselben Winkel ergeben.",
        "w": "Weg A: 180° − 90° − 40° = 50°. Weg B: (180° − 80°) : 2 = 50°. Beide Wege geben 50°.",
        "fehlbilder": [{"antwort": 40, "beschreibung": "den Winkel bei A abgeschrieben"},
                       {"antwort": 80, "beschreibung": "den Winkel bei M genannt"}],
    },
    {
        "k": "K7-V054", "karte": "beweis", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind schreibt: Zeile 1: Ich habe in zwanzig Dreiecken über einem Durchmesser den Winkel bei C "
                "gemessen. Zeile 2: Jedes Mal kamen 90° heraus. "
                "Zeile 3: Damit ist der Satz des Thales bewiesen. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Was zeigen zwanzig Beispiele, und was zeigen sie nicht?",
        "w": "Zeile 1 und 2 beschreiben eine saubere Messreihe. Sie gilt aber nur für diese zwanzig Dreiecke. "
             "Ein Beweis muss für alle Punkte C gelten; dafür braucht man die gleich langen Radien.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, Messen ist erlaubt"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig, das Ergebnis stimmt ja"},
        ],
    },
    # ---------------- lage ----------------
    {
        "k": "K7-V055", "karte": "lage", "typ": "LW", "s": 1, "y": "luecken", "regel": AB,
        "text": "Ein Kreis hat den Radius 5 cm. Eine Gerade hat vom Mittelpunkt den Abstand 8 cm. "
                "Der Abstand ist also ① cm größer als der Radius. "
                "Damit hat die Gerade mit dem Kreis ② Punkte gemeinsam.",
        "schablone": "① = □; ② = □",
        "c": ["8 - 5", "0"], "erwartet": [3, 0],
        "h": "Vergleiche den Abstand mit dem Radius.",
        "w": "8 cm − 5 cm = 3 cm, der Abstand ist größer als der Radius. Die Gerade ist eine Passante und hat "
             "keinen Punkt mit dem Kreis gemeinsam.",
        "fehlbilder": [{"luecke": 2, "antwort": 2, "beschreibung": "wie bei einer Sekante gezählt"}],
    },
    {
        "k": "K7-V056", "karte": "lage", "typ": "VW", "s": 2, "y": "auswahl", "regel": AB,
        "text": "Gegeben sind ein Kreis mit dem Radius 6 cm und eine Gerade g. Du sollst herausfinden, ob g "
                "Passante, Tangente oder Sekante ist. Welches Vorgehen führt zum Ziel?",
        "a": ["den Abstand des Mittelpunkts von g bestimmen und mit 6 cm vergleichen",
              "die Länge der Geraden g messen",
              "den Umfang des Kreises berechnen",
              "den Abstand des Mittelpunkts zu einem beliebigen Punkt von g messen"],
        "richtig": 0,
        "h": "Entscheidend ist der kürzeste Abstand zur Geraden.",
        "w": "Man vergleicht den Abstand des Mittelpunkts von der Geraden mit dem Radius: größer heißt Passante, "
             "gleich Tangente, kleiner Sekante.",
        "fehlbilder": [
            {"index": 1, "antwort": "die Länge der Geraden g messen", "beschreibung": "eine Gerade hat keine Länge"},
            {"index": 2, "antwort": "den Umfang des Kreises berechnen", "beschreibung": "der Umfang sagt nichts über die Lage der Geraden"},
            {"index": 3, "antwort": "den Abstand des Mittelpunkts zu einem beliebigen Punkt von g messen",
             "beschreibung": "ein beliebiger Punkt liegt meist weiter weg als der Lotfußpunkt"},
        ],
    },
    {
        "k": "K7-V057", "karte": "lage", "typ": "AN", "s": 3, "y": "zahl", "regel": AB,
        "text": "Ein kreisrunder Teich hat den Durchmesser 24 m. Ein gerader Zaun soll so verlaufen, dass er den "
                "Teichrand genau berührt. Welchen Abstand muss der Zaun von der Mitte des Teichs haben?",
        "c": "24 // 2", "erwartet": 12, "einheit": "m",
        "h": "Berühren heißt: Abstand gleich Radius.",
        "w": "Der Radius ist 24 m : 2 = 12 m. Eine Tangente hat genau den Abstand des Radius, also 12 m.",
        "fehlbilder": [{"antwort": 24, "beschreibung": "den Durchmesser als Abstand genommen"},
                       {"antwort": 48, "beschreibung": "den Durchmesser verdoppelt"}],
    },
    # ---------------- tangente ----------------
    {
        "k": "K7-V058", "karte": "tangente", "typ": "LW", "s": 1, "y": "luecken", "regel": AB,
        "text": "Von einem Punkt P außerhalb eines Kreises gehen zwei Tangenten aus. In jedem Berührpunkt bildet "
                "die Tangente mit dem Berührradius einen Winkel von ① °. Im Viereck aus P, den beiden "
                "Berührpunkten und dem Mittelpunkt ist die Winkelsumme 360°. "
                "Ist der Winkel bei P 40°, so bleiben beim Mittelpunkt 360° − ① ° − ① ° − 40° = ② °.",
        "schablone": "① = □; ② = □",
        "c": ["90", "360 - 90 - 90 - 40"], "erwartet": [90, 140],
        "h": "Tangente und Berührradius stehen senkrecht aufeinander.",
        "w": "An beiden Berührpunkten sind es 90°. 360° − 90° − 90° − 40° = 140° beim Mittelpunkt.",
        "fehlbilder": [{"luecke": 2, "antwort": 230, "beschreibung": "nur einen rechten Winkel abgezogen"}],
    },
    {
        "k": "K7-V059", "karte": "tangente", "typ": "UM", "s": 2, "y": "zahl", "regel": AB,
        "text": "Von einem Punkt P gehen zwei Tangenten an einen Kreis. Zwischen den beiden Berührradien liegt "
                "beim Mittelpunkt ein Winkel von 110°. Wie groß ist der Winkel bei P?",
        "c": "360 - 90 - 90 - 110", "erwartet": 70, "einheit": "°",
        "h": "Im Viereck sind die Winkel an den Berührpunkten je 90°.",
        "w": "360° − 90° − 90° − 110° = 70°. Bei P ist der Winkel 70°.",
        "fehlbilder": [{"antwort": 110, "beschreibung": "den Winkel beim Mittelpunkt abgeschrieben"},
                       {"antwort": 250, "beschreibung": "die rechten Winkel nicht abgezogen"}],
    },
    {
        "k": "K7-V060", "karte": "tangente", "typ": "ZW", "s": 2, "y": "zahl", "regel": AB,
        "text": "Von einem Punkt P gehen zwei Tangenten an einen Kreis; die Berührpunkte heißen B und B'. "
                "Der Weg von B über P nach B' ist 24 cm lang. "
                "Weg A: die beiden Tangentenabschnitte von P sind gleich lang. "
                "Weg B: die Figur ist an der Geraden PM gespiegelt. Wie lang ist die Strecke [PB]?",
        "c": "24 // 2", "erwartet": 12, "einheit": "cm",
        "h": "Beide Wege sagen dasselbe über [PB] und [PB'].",
        "w": "Weg A: beide Abschnitte sind gleich lang, also 24 cm : 2 = 12 cm. Weg B: die Spiegelung an PM "
             "bildet [PB] auf [PB'] ab, deshalb sind sie gleich lang. Beide Wege geben 12 cm.",
        "fehlbilder": [{"antwort": 24, "beschreibung": "den ganzen Weg als einen Abschnitt genommen"},
                       {"antwort": 48, "beschreibung": "verdoppelt statt halbiert"}],
    },
    # ---------------- umkreis_inkreis ----------------
    {
        "k": "K7-V061", "karte": "umkreis_inkreis", "typ": "LW", "s": 1, "y": "luecken", "regel": AB,
        "text": "Ein Dreieck hat die Ecken A(0 | 0), B(8 | 0) und C(0 | 6). Der Umkreismittelpunkt ist der "
                "Schnittpunkt der Mittelsenkrechten. Die Mittelsenkrechte von [AB] ist die Senkrechte durch "
                "x = ① , die Mittelsenkrechte von [AC] die Waagerechte durch y = ② .",
        "schablone": "① = □; ② = □",
        "c": ["8 // 2", "6 // 2"], "erwartet": [4, 3],
        "h": "Jede Mittelsenkrechte geht durch die Mitte ihrer Strecke.",
        "w": "Die Mitte von [AB] ist (4 | 0), die Mitte von [AC] ist (0 | 3). Der Umkreismittelpunkt ist M(4 | 3).",
        "fehlbilder": [{"luecke": 1, "antwort": 8, "beschreibung": "die Ecke statt der Mitte genommen"}],
    },
    {
        "k": "K7-V062", "karte": "umkreis_inkreis", "typ": "BR", "s": 2, "y": "auswahl", "regel": AB,
        "text": "Ein Satz lautet: „Dieser Punkt hat zu allen drei Seiten des Dreiecks denselben Abstand.“ "
                "Welcher Punkt ist gemeint, und wie findet man ihn?",
        "a": ["der Inkreismittelpunkt, als Schnitt der Winkelhalbierenden",
              "der Umkreismittelpunkt, als Schnitt der Mittelsenkrechten",
              "der Schwerpunkt, als Schnitt der Seitenhalbierenden",
              "der Höhenschnittpunkt, als Schnitt der Höhen"],
        "richtig": 0,
        "h": "Gleicher Abstand zu zwei Seiten heißt: auf der Winkelhalbierenden.",
        "w": "Gleicher Abstand zu den Seiten gehört zu den Winkelhalbierenden; ihr Schnittpunkt ist der "
             "Inkreismittelpunkt. Gleicher Abstand zu den Ecken gehört zu den Mittelsenkrechten und zum Umkreis.",
        "fehlbilder": [
            {"index": 1, "antwort": "der Umkreismittelpunkt, als Schnitt der Mittelsenkrechten",
             "beschreibung": "der hat gleichen Abstand zu den Ecken, nicht zu den Seiten"},
            {"index": 2, "antwort": "der Schwerpunkt, als Schnitt der Seitenhalbierenden",
             "beschreibung": "der Schwerpunkt hat zu den Seiten verschiedene Abstände"},
            {"index": 3, "antwort": "der Höhenschnittpunkt, als Schnitt der Höhen",
             "beschreibung": "die Höhen haben mit gleichem Abstand nichts zu tun"},
        ],
    },
    {
        "k": "K7-V063", "karte": "umkreis_inkreis", "typ": "FD", "s": 3, "y": "auswahl", "regel": AB,
        "text": "Ein Kind sucht den Mittelpunkt des Inkreises. "
                "Zeile 1: Der Inkreis berührt alle drei Seiten des Dreiecks. "
                "Zeile 2: Sein Mittelpunkt hat deshalb zu allen drei Seiten denselben Abstand. "
                "Zeile 3: Also zeichnet man die drei Mittelsenkrechten und nimmt ihren Schnittpunkt. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Welche Linien gehören zu gleichem Abstand von Seiten?",
        "w": "Zeile 1 und 2 stimmen. Gleicher Abstand zu den Seiten führt auf die Winkelhalbierenden. "
             "Die Mittelsenkrechten geben den Umkreismittelpunkt.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, so ist der Inkreis bestimmt"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig, Berühren heißt gleicher Abstand"},
        ],
    },
]
