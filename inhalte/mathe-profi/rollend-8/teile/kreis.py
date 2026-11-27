"""geometrie.kreis (Klasse 7): 6 Lernkarten, 18 Aufgaben in neuer Form.

Ohne Zeichnungen: Jede Figur ist im Text beschrieben (Bauteile werden nicht neu eingeführt).
Feldbedeutung (c mit L1, L2 …, entscheidend, rechnung, a_rechnung): siehe Kopf von teile/zinsen.py.
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
                "Der Winkel bei C ist ①°. Der Winkel bei B ist ②°. Der Nebenwinkel des Winkels bei B ist ③°.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["90", "180 - L1 - 28", "180 - L2"], "erwartet": [90, 62, 118], "entscheidend": 2,
        "h": "Wo liegt C in Bezug auf den Durchmesser?",
        "w": "Nach dem Satz des Thales sind es bei C 90°. Dann bleiben 180° − 90° − 28° = 62° für den Winkel bei B. "
             "Der Nebenwinkel ergänzt auf 180°: 180° − 62° = 118°.",
        "fehlbilder": [{"luecke": 2, "antwort": 152, "rechnung": "180 - 28", "beschreibung": "den rechten Winkel nicht abgezogen"},
                       {"luecke": 3, "antwort": 62, "rechnung": "L2", "beschreibung": "den Winkel bei B selbst statt seines Nebenwinkels genannt"}],
    },
    {
        "k": "K7-V047", "karte": "thales", "typ": "UM", "s": 2, "y": "zahl", "regel": DG,
        "text": "Im Dreieck ABC liegt C auf dem Kreis über dem Durchmesser [AB]. "
                "Der Winkel bei B ist doppelt so groß wie der Winkel bei A. Wie groß ist der Winkel bei A?",
        "c": "90 // 3", "erwartet": 30, "einheit": "°",
        "h": "Die Winkel bei A und B ergeben zusammen 90°.",
        "w": "Bei C sind 90°, also bleiben für A und B zusammen 90°. Mit β = 2α folgt 3α = 90°, also α = 30°.",
        "fehlbilder": [{"antwort": 60, "rechnung": "2 * 30", "beschreibung": "den doppelten Winkel genannt"},
                       {"antwort": 45, "rechnung": "90 // 2", "beschreibung": "beide Winkel gleich groß angenommen"}],
    },
    {
        "k": "K7-V048", "karte": "thales", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind untersucht ein Dreieck ABC, dessen Ecken A, B und C auf einem Kreis liegen. "
                "Die Strecke [AB] geht nicht durch den Mittelpunkt. "
                "Zeile 1: Weil A und B auf dem Kreis liegen, ist [AB] ein Durchmesser. "
                "Zeile 2: Also gilt für den Punkt C der Satz des Thales. "
                "Zeile 3: Der Winkel bei C ist deshalb 90°. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Welche Bedingung muss die Strecke [AB] erfüllen?",
        "w": "Zeile 1 ist falsch: Ein Durchmesser geht durch den Mittelpunkt, [AB] tut das hier nicht. "
             "Die Zeilen 2 und 3 folgen richtig aus der falschen Zeile 1. Ohne Durchmesser ist der Winkel bei C meist kein rechter.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile folgt richtig aus Zeile 1: wäre [AB] ein Durchmesser, gälte Thales"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2: nach Thales wären es 90°"},
        ],
    },
    # ---------------- umkehrung ----------------
    {
        "k": "K7-V049", "karte": "umkehrung", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Bei C ist ein rechter Winkel, und es ist A(1 | 2) und B(9 | 2). Nach der Umkehrung des Satzes von Thales "
                "liegt C auf dem Kreis über [AB]. Der Mittelpunkt M hat die x-Koordinate ①. "
                "Der Radius ist ② lang. Der höchste Punkt des Kreises hat die y-Koordinate ③.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["(1 + 9) // 2", "L1 - 1", "2 + L2"], "erwartet": [5, 4, 6], "entscheidend": 2,
        "h": "Der Mittelpunkt liegt genau zwischen A und B.",
        "w": "Die Mitte von 1 und 9 ist (1 + 9) : 2 = 5, also M(5 | 2). Der Radius ist der Abstand von M zu A: 5 − 1 = 4. "
             "Der höchste Punkt liegt 4 über M: y = 2 + 4 = 6.",
        "fehlbilder": [{"luecke": 2, "antwort": 8, "rechnung": "9 - 1", "beschreibung": "die ganze Strecke [AB] als Radius genommen"},
                       {"luecke": 3, "antwort": 10, "rechnung": "2 + 8", "beschreibung": "mit dem falschen Radius 8 weitergerechnet"}],
    },
    {
        "k": "K7-V050", "karte": "umkehrung", "typ": "BR", "s": 2, "y": "auswahl", "regel": DG,
        "text": "In einem Koordinatensystem sind A(−3 | 0) und B(3 | 0) gegeben. "
                "Bei welchem Punkt C hat das Dreieck ABC bei C einen rechten Winkel?",
        "a": ["C(0 | 3)", "C(3 | 3)", "C(0 | 4)", "C(2 | 2)"],
        "richtig": 0,
        "h": "Wie weit ist C vom Mittelpunkt der Strecke [AB] entfernt, und wie weit müsste er es sein?",
        "w": "Der Kreis über [AB] hat den Mittelpunkt (0 | 0) und den Radius 3. Nur C(0 | 3) liegt darauf. "
             "Bei C(3 | 3) liegt der rechte Winkel bei B, C(0 | 4) liegt außerhalb des Kreises (Winkel kleiner als 90°), "
             "C(2 | 2) innerhalb (Winkel größer als 90°).",
        "fehlbilder": [
            {"index": 1, "antwort": "C(3 | 3)", "beschreibung": "hier ist der rechte Winkel bei B, nicht bei C"},
            {"index": 2, "antwort": "C(0 | 4)", "beschreibung": "C liegt außerhalb des Kreises, der Winkel ist kleiner als 90°"},
            {"index": 3, "antwort": "C(2 | 2)", "beschreibung": "C liegt innerhalb des Kreises, der Winkel ist größer als 90°"},
        ],
    },
    {
        "k": "K7-V051", "karte": "umkehrung", "typ": "AN", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Tischler prüft ein dreieckiges Brettstück ABC. Die Kante [AB] ist 50 cm lang. "
                "Er will wissen, ob bei C genau 90° sind. Dazu sticht er in die Mitte von [AB] ein und misst "
                "von dort bis zur Ecke C. Welchen Abstand muss er finden, wenn der Winkel bei C genau 90° ist?",
        "c": "50 // 2", "erwartet": 25, "einheit": "cm",
        "h": "Welcher Kreis gehört zu rechten Winkeln über [AB]?",
        "w": "Der Kreis über der 50 cm langen Kante hat den Radius 50 cm : 2 = 25 cm. Liegt die Ecke C auf diesem "
             "Kreis, ist der Winkel 90°, der Abstand muss also 25 cm sein.",
        "fehlbilder": [{"antwort": 50, "rechnung": "50", "beschreibung": "die ganze Kante als Abstand genommen"},
                       {"antwort": 100, "rechnung": "50 * 2", "beschreibung": "verdoppelt statt halbiert"}],
    },
    # ---------------- beweis ----------------
    {
        "k": "K7-V052", "karte": "beweis", "typ": "VW", "s": 1, "y": "auswahl", "regel": DG,
        "text": "Du sollst zeigen, dass bei jedem Punkt C auf dem Thaleskreis ein rechter Winkel entsteht. "
                "Welches Vorgehen ist ein Beweis?",
        "a": ["mit den gleich langen Radien MA, MB und MC argumentieren",
              "zwanzig Beispiele zeichnen und nachmessen",
              "ein besonders großes Dreieck zeichnen und messen",
              "den Satz in einem Buch nachlesen"],
        "richtig": 0,
        "h": "Welches Vorgehen deckt auch einen Punkt C ab, den du nie gezeichnet hast?",
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
        "fehlbilder": [{"antwort": 40, "rechnung": "40", "beschreibung": "den Winkel bei A abgeschrieben"},
                       {"antwort": 80, "rechnung": "180 - 100", "beschreibung": "den Winkel BMC genannt"}],
    },
    {
        "k": "K7-V054", "karte": "beweis", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind schreibt: Zeile 1: Ich habe in zwanzig Dreiecken über einem Durchmesser den Winkel bei C "
                "gemessen. Zeile 2: Jedes Mal kamen 90° heraus. "
                "Zeile 3: Damit ist der Satz des Thales bewiesen. "
                "In welcher Zeile steckt der erste Fehler?",
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
                "Man schiebt die Gerade um 6 cm zum Mittelpunkt hin. Ihr neuer Abstand ist ① cm. "
                "Der Unterschied zum Radius beträgt ② cm. "
                "Die Anzahl der gemeinsamen Punkte von Gerade und Kreis ist ③.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["8 - 6", "5 - L1", "1 + min(1, max(-1, L2))"], "erwartet": [2, 3, 2], "entscheidend": 3,
        "h": "Vergleiche den neuen Abstand mit dem Radius.",
        "w": "Neuer Abstand: 8 cm − 6 cm = 2 cm. Das sind 5 cm − 2 cm = 3 cm weniger als der Radius. "
             "Ist der Abstand kleiner als der Radius, schneidet die Gerade den Kreis in 2 Punkten (Sekante).",
        "fehlbilder": [{"luecke": 1, "antwort": 14, "rechnung": "8 + 6", "beschreibung": "in die falsche Richtung geschoben"},
                       {"luecke": 3, "antwort": 0, "rechnung": "0", "beschreibung": "wie bei einer Passante gezählt"}],
    },
    {
        "k": "K7-V056", "karte": "lage", "typ": "VW", "s": 1, "y": "auswahl", "regel": AB,
        "text": "Gegeben sind ein Kreis mit dem Radius 6 cm und eine Gerade g. Du sollst herausfinden, ob g "
                "Passante, Tangente oder Sekante ist. Welches Vorgehen führt zum Ziel?",
        "a": ["den Abstand des Mittelpunkts von g bestimmen und mit 6 cm vergleichen",
              "die Länge der Geraden g messen",
              "den Umfang des Kreises berechnen",
              "den Abstand des Mittelpunkts zu einem beliebigen Punkt von g messen"],
        "richtig": 0,
        "h": "Was ändert sich, wenn man die Gerade immer weiter vom Mittelpunkt wegschiebt?",
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
        "k": "K7-V057", "karte": "lage", "typ": "AN", "s": 2, "y": "zahl", "regel": AB,
        "text": "Ein kreisrunder Teich hat den Durchmesser 24 m. Ein gerader Zaun soll so verlaufen, dass er den "
                "Teichrand an genau einer Stelle berührt. Welchen Abstand muss der Zaun von der Mitte des Teichs haben?",
        "c": "24 // 2", "erwartet": 12, "einheit": "m",
        "h": "Wie viele Punkte soll der Zaun mit dem Teichrand gemeinsam haben?",
        "w": "Der Radius ist 24 m : 2 = 12 m. Eine Tangente hat genau den Abstand des Radius, also 12 m.",
        "fehlbilder": [{"antwort": 24, "rechnung": "24", "beschreibung": "den Durchmesser als Abstand genommen"},
                       {"antwort": 48, "rechnung": "24 * 2", "beschreibung": "den Durchmesser verdoppelt"}],
    },
    # ---------------- tangente ----------------
    {
        "k": "K7-V058", "karte": "tangente", "typ": "LW", "s": 1, "y": "luecken", "regel": AB,
        "text": "Von einem Punkt P außerhalb eines Kreises gehen zwei Tangenten aus. In jedem Berührpunkt bildet "
                "die Tangente mit dem Berührradius einen Winkel von ①°. Im Viereck aus P, den beiden "
                "Berührpunkten und dem Mittelpunkt M ist die Winkelsumme 360°. "
                "Ist der Winkel bei P gleich 40°, so ist der Winkel bei M gleich ②°. "
                "Die Gerade MP halbiert ihn; jede Hälfte hat ③°.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["90", "360 - 2 * L1 - 40", "L2 // 2"], "erwartet": [90, 140, 70], "entscheidend": 2,
        "h": "Wie stehen Tangente und Berührradius zueinander?",
        "w": "An beiden Berührpunkten sind es 90°. 360° − 90° − 90° − 40° = 140° bei M. Die Hälfte davon ist 70°.",
        "fehlbilder": [{"luecke": 2, "antwort": 230, "rechnung": "360 - 90 - 40", "beschreibung": "nur einen rechten Winkel abgezogen"},
                       {"luecke": 3, "antwort": 140, "rechnung": "L2", "beschreibung": "das Halbieren vergessen"}],
    },
    {
        "k": "K7-V059", "karte": "tangente", "typ": "UM", "s": 2, "y": "zahl", "regel": AB,
        "text": "Von einem Punkt P gehen zwei Tangenten an einen Kreis. Zwischen den beiden Berührradien liegt "
                "beim Mittelpunkt ein Winkel von 110°. Wie groß ist der Winkel bei P?",
        "c": "360 - 90 - 90 - 110", "erwartet": 70, "einheit": "°",
        "h": "Zeichne das Viereck aus P, den beiden Berührpunkten und dem Mittelpunkt.",
        "w": "Im Viereck sind die Winkel an den Berührpunkten je 90°. 360° − 90° − 90° − 110° = 70°. Bei P ist der Winkel 70°.",
        "fehlbilder": [{"antwort": 110, "rechnung": "110", "beschreibung": "den Winkel beim Mittelpunkt abgeschrieben"},
                       {"antwort": 250, "rechnung": "360 - 110", "beschreibung": "die rechten Winkel nicht abgezogen"}],
    },
    {
        "k": "K7-V060", "karte": "tangente", "typ": "ZW", "s": 2, "y": "zahl", "regel": AB,
        "text": "Von einem Punkt P gehen zwei Tangenten an einen Kreis mit dem Mittelpunkt M; die Berührpunkte heißen B und B'. "
                "Der Weg von B über P nach B' ist 24 cm lang. "
                "Weg A: die Regel anwenden, dass die beiden Tangentenabschnitte von P gleich lang sind. "
                "Weg B: die Dreiecke PMB und PMB' vergleichen (gemeinsame Seite [PM], gleiche Radien, je ein rechter Winkel). "
                "Wie lang ist die Strecke [PB]?",
        "c": "24 // 2", "erwartet": 12, "einheit": "cm",
        "h": "Beide Wege sagen dasselbe über [PB] und [PB'].",
        "w": "Weg A: beide Abschnitte sind gleich lang, also 24 cm : 2 = 12 cm. Weg B: Die Dreiecke PMB und PMB' stimmen in "
             "[PM], im Radius und im rechten Winkel überein (kongruent), deshalb ist [PB] = [PB']. Beide Wege geben 12 cm.",
        "fehlbilder": [{"antwort": 24, "rechnung": "24", "beschreibung": "den ganzen Weg als einen Abschnitt genommen"},
                       {"antwort": 48, "rechnung": "24 * 2", "beschreibung": "verdoppelt statt halbiert"}],
    },
    # ---------------- umkreis_inkreis ----------------
    {
        "k": "K7-V061", "karte": "umkreis_inkreis", "typ": "LW", "s": 1, "y": "luecken", "regel": AB,
        "text": "Ein Dreieck hat die Ecken A(0 | 0), B(8 | 0) und C(0 | 6). Der Umkreismittelpunkt M ist der "
                "Schnittpunkt der Mittelsenkrechten. Die Mittelsenkrechte von [AB] ist die Senkrechte durch "
                "x = ①, die Mittelsenkrechte von [AC] die Waagerechte durch y = ②. "
                "Von A aus muss man zu M also ① nach rechts und ② nach oben gehen, zusammen ③ Einheiten auf den Achsen.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["8 // 2", "6 // 2", "L1 + L2"], "erwartet": [4, 3, 7], "entscheidend": 1,
        "h": "Jede Mittelsenkrechte geht durch die Mitte ihrer Strecke.",
        "w": "Die Mitte von [AB] ist (4 | 0), die Mitte von [AC] ist (0 | 3). Der Umkreismittelpunkt ist M(4 | 3). "
             "Der Weg von A aus: 4 + 3 = 7 Einheiten.",
        "fehlbilder": [{"luecke": 1, "antwort": 8, "rechnung": "8", "beschreibung": "die Ecke statt der Mitte genommen"},
                       {"luecke": 2, "antwort": 6, "rechnung": "6", "beschreibung": "die Ecke statt der Mitte genommen"}],
    },
    {
        "k": "K7-V062", "karte": "umkreis_inkreis", "typ": "BR", "s": 2, "y": "auswahl", "regel": AB,
        "text": "Ein Kind zeichnet in ein Dreieck die drei Winkelhalbierenden und nimmt ihren Schnittpunkt S. "
                "Dann zeichnet es um S einen Kreis, der eine der drei Seiten berührt. "
                "Welche Eigenschaft hat dieser Kreis?",
        "a": ["Er berührt alle drei Seiten des Dreiecks (Inkreis).",
              "Er geht durch alle drei Ecken des Dreiecks (Umkreis).",
              "Er berührt nur die gewählte Seite und schneidet die beiden anderen.",
              "Sein Mittelpunkt liegt immer auf der längsten Seite."],
        "richtig": 0,
        "h": "Was haben alle Punkte einer Winkelhalbierenden gemeinsam?",
        "w": "S hat zu allen drei Seiten denselben Abstand. Ein Kreis um S, der eine Seite berührt, hat diesen Abstand als "
             "Radius und berührt deshalb auch die anderen beiden Seiten: der Inkreis. Durch die Ecken geht der Umkreis, "
             "dessen Mittelpunkt auf den Mittelsenkrechten liegt.",
        "fehlbilder": [
            {"index": 1, "antwort": "Er geht durch alle drei Ecken des Dreiecks (Umkreis).",
             "beschreibung": "der Umkreis gehört zu den Mittelsenkrechten, nicht zu den Winkelhalbierenden"},
            {"index": 2, "antwort": "Er berührt nur die gewählte Seite und schneidet die beiden anderen.",
             "beschreibung": "S ist von allen drei Seiten gleich weit entfernt, der Kreis berührt alle"},
            {"index": 3, "antwort": "Sein Mittelpunkt liegt immer auf der längsten Seite.",
             "beschreibung": "S liegt im Inneren des Dreiecks, nicht auf einer Seite"},
        ],
    },
    {
        "k": "K7-V063", "karte": "umkreis_inkreis", "typ": "FD", "s": 3, "y": "auswahl", "regel": AB,
        "text": "Ein Kind sucht den Mittelpunkt des Inkreises. "
                "Zeile 1: Der Inkreis geht durch alle drei Ecken des Dreiecks. "
                "Zeile 2: Sein Mittelpunkt hat deshalb zu allen drei Ecken denselben Abstand. "
                "Zeile 3: Also zeichnet man die drei Mittelsenkrechten und nimmt ihren Schnittpunkt. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Berührt der Inkreis die Seiten oder geht er durch die Ecken?",
        "w": "Zeile 1 ist falsch: Der Inkreis berührt die drei Seiten. Durch die Ecken geht der Umkreis. "
             "Die Zeilen 2 und 3 folgen richtig aus Zeile 1 und beschreiben dann den Umkreis.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile folgt richtig aus Zeile 1: Punkte, die durch die Ecken gehen, haben gleichen Abstand zu den Ecken"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2: gleicher Abstand zu den Ecken gehört zu den Mittelsenkrechten"},
        ],
    },
]
