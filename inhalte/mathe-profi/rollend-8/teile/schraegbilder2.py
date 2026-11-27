"""raum.schraegbilder_teil2 (Klasse 7 Realschule): 4 Lernkarten, 12 Aufgaben in neuer Form.

Lernkarten koordinaten, rotation, axialschnitt, koerper_symmetrie. Der Bestand steht in der
Themen-Datei raum.schraegbilder; das Feld „thema" trägt hier den Schlüssel mit `_teil2`,
weil Teil 2 eine eigene Einheit ist. Ohne Zeichnungen.
"""
STAND = "2026-11-27"
TITEL = "Koordinaten, Rotationskörper und Axialschnitt"
PASST_NICHT = ()

HT = "id.flaeche_raum.haut"

AUFGABEN = [
    # ---------------- koordinaten ----------------
    {
        "k": "K7-V145", "karte": "koordinaten", "typ": "LW", "s": 1, "y": "luecken", "regel": HT,
        "text": "Ein Quader liegt mit A im Ursprung und ist 5 lang, 3 breit und 2 hoch. Es ist C(5 | 3 | 0), "
                "und G liegt senkrecht über C. Die Summe der Koordinaten von C ist 5 + 3 + 0 = ①. "
                "Bei G kommt die Höhe des Quaders dazu, seine Koordinatensumme ist ②.",
        "schablone": "① = □; ② = □",
        "c": ["5 + 3 + 0", "5 + 3 + 2"], "erwartet": [8, 10],
        "h": "G liegt so hoch wie der Quader.",
        "w": "C(5 | 3 | 0) hat die Summe 8. G liegt 2 höher: G(5 | 3 | 2) mit der Summe 10.",
        "fehlbilder": [{"luecke": 2, "antwort": 8, "beschreibung": "die Höhe nicht dazugezählt"}],
    },
    {
        "k": "K7-V146", "karte": "koordinaten", "typ": "UM", "s": 2, "y": "zahl", "regel": HT,
        "text": "In einem Quader mit A im Ursprung ist G(7 | 4 | 3) die Ecke gegenüber von A. "
                "Wie viele Flächeneinheiten hat die Grundfläche?",
        "c": "7 * 4", "erwartet": 28, "einheit": "FE",
        "h": "Die ersten beiden Koordinaten geben Länge und Breite.",
        "w": "Der Quader ist 7 lang und 4 breit; die Höhe 3 gehört nicht zur Grundfläche. "
             "Grundfläche: 7 · 4 = 28 FE.",
        "fehlbilder": [{"antwort": 84, "beschreibung": "das Volumen gerechnet"},
                       {"antwort": 14, "beschreibung": "den Umfang gerechnet"}],
    },
    {
        "k": "K7-V147", "karte": "koordinaten", "typ": "FD", "s": 3, "y": "auswahl", "regel": HT,
        "text": "Ein Quader liegt mit A im Ursprung, ist 5 lang, 3 breit und 2 hoch; D liegt auf der y-Achse. "
                "Ein Kind sagt: Zeile 1: E liegt senkrecht über A, also E(0 | 0 | 2). "
                "Zeile 2: D liegt auf der y-Achse, also D(0 | 3 | 0). "
                "Zeile 3: H liegt über D, also H(0 | 0 | 2). "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Vergleiche die Koordinaten von H mit denen von E.",
        "w": "Zeile 1 und 2 stimmen. H liegt über D, also H(0 | 3 | 2). In Zeile 3 stehen die Koordinaten von E.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: E liegt 2 über dem Ursprung"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: auf der y-Achse sind x und z null"},
        ],
    },
    # ---------------- rotation ----------------
    {
        "k": "K7-V148", "karte": "rotation", "typ": "BR", "s": 2, "y": "auswahl", "regel": HT,
        "text": "Ein Rechteck mit den Seiten 4 cm und 7 cm dreht sich um die 7-cm-Seite. "
                "Welcher Körper entsteht, und mit welchen Maßen?",
        "a": ["ein Zylinder mit r = 4 cm und h = 7 cm",
              "ein Zylinder mit r = 7 cm und h = 4 cm",
              "ein Kegel mit r = 4 cm und h = 7 cm",
              "eine Kugel mit r = 7 cm"],
        "richtig": 0,
        "h": "Die Seite auf der Achse wird zur Höhe.",
        "w": "Die 7-cm-Seite liegt auf der Achse und wird die Höhe. Die 4-cm-Seite dreht sich im Kreis und wird "
             "der Radius: ein Zylinder mit r = 4 cm und h = 7 cm.",
        "fehlbilder": [
            {"index": 1, "antwort": "ein Zylinder mit r = 7 cm und h = 4 cm", "beschreibung": "Radius und Höhe vertauscht"},
            {"index": 2, "antwort": "ein Kegel mit r = 4 cm und h = 7 cm", "beschreibung": "ein Kegel entsteht aus einem rechtwinkligen Dreieck"},
            {"index": 3, "antwort": "eine Kugel mit r = 7 cm", "beschreibung": "eine Kugel entsteht aus einem Halbkreis"},
        ],
    },
    {
        "k": "K7-V149", "karte": "rotation", "typ": "VW", "s": 2, "y": "auswahl", "regel": HT,
        "text": "Du sollst eine Kugel durch Drehen erzeugen. Welche Fläche nimmst du, und um welche Achse?",
        "a": ["einen Halbkreis um seinen Durchmesser",
              "einen Viertelkreis um eine seiner geraden Kanten",
              "ein Rechteck um eine Seite",
              "ein rechtwinkliges Dreieck um eine Kathete"],
        "richtig": 0,
        "h": "Welche Umrisslinie gehört zur Kugel?",
        "w": "Ein Halbkreis, der um seinen Durchmesser gedreht wird, ergibt die Kugel. Das Rechteck gibt einen "
             "Zylinder, das rechtwinklige Dreieck einen Kegel, der Viertelkreis nur eine halbe Kugel.",
        "fehlbilder": [
            {"index": 1, "antwort": "einen Viertelkreis um eine seiner geraden Kanten", "beschreibung": "daraus wird nur eine halbe Kugel"},
            {"index": 2, "antwort": "ein Rechteck um eine Seite", "beschreibung": "daraus wird ein Zylinder"},
            {"index": 3, "antwort": "ein rechtwinkliges Dreieck um eine Kathete", "beschreibung": "daraus wird ein Kegel"},
        ],
    },
    {
        "k": "K7-V150", "karte": "rotation", "typ": "AN", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein rechtwinkliges Dreieck mit den Katheten 5 cm und 12 cm dreht sich um die 12-cm-Kathete. "
                "Wie groß ist der Durchmesser des entstehenden Kegels?",
        "c": "2 * 5", "erwartet": 10, "einheit": "cm",
        "h": "Die Kathete auf der Achse wird zur Höhe, die andere zum Radius.",
        "w": "Die 12-cm-Kathete liegt auf der Achse und wird die Höhe, die 5-cm-Kathete wird der Radius. "
             "Der Durchmesser ist 2 · 5 cm = 10 cm.",
        "fehlbilder": [{"antwort": 5, "beschreibung": "den Radius genannt"},
                       {"antwort": 24, "beschreibung": "die Höhe verdoppelt"}],
    },
    # ---------------- axialschnitt ----------------
    {
        "k": "K7-V151", "karte": "axialschnitt", "typ": "LW", "s": 1, "y": "luecken", "regel": HT,
        "text": "Ein Zylinder hat r = 4 cm und h = 9 cm. Der Axialschnitt geht durch die Achse und erfasst den "
                "ganzen Durchmesser: 2 · 4 cm = ① cm. Das Rechteck ist also ① cm breit und 9 cm hoch; "
                "seine Fläche ist ② cm².",
        "schablone": "① = □; ② = □",
        "c": ["2 * 4", "2 * 4 * 9"], "erwartet": [8, 72],
        "h": "Der Schnitt ist 2r breit, nicht r.",
        "w": "Der Durchmesser ist 8 cm, die Höhe 9 cm. Die Schnittfläche ist 8 · 9 = 72 cm².",
        "fehlbilder": [{"luecke": 2, "antwort": 36, "beschreibung": "nur mit dem Radius gerechnet"}],
    },
    {
        "k": "K7-V152", "karte": "axialschnitt", "typ": "ZW", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein Zylinder hat den Durchmesser 10 cm und die Höhe 6 cm. Weg A: Durchmesser mal Höhe. "
                "Weg B: zwei Rechtecke mit r = 5 cm und h = 6 cm nebeneinanderlegen. "
                "Wie groß ist die Fläche des Axialschnitts?",
        "c": "10 * 6", "erwartet": 60, "einheit": "cm²",
        "h": "Beide Wege müssen dieselbe Fläche ergeben.",
        "w": "Weg A: 10 · 6 = 60 cm². Weg B: 2 · (5 · 6) = 60 cm². Der Axialschnitt hat 60 cm².",
        "fehlbilder": [{"antwort": 30, "beschreibung": "nur mit dem Radius gerechnet"},
                       {"antwort": 120, "beschreibung": "beide Hälften noch einmal verdoppelt"}],
    },
    {
        "k": "K7-V153", "karte": "axialschnitt", "typ": "AN", "s": 3, "y": "zahl", "regel": HT,
        "text": "Eine Dose ist ein Zylinder mit r = 3 cm und h = 11 cm. Sie wird längs genau durch die Achse "
                "aufgeschnitten. Wie groß ist eine der beiden entstehenden Schnittflächen?",
        "c": "2 * 3 * 11", "erwartet": 66, "einheit": "cm²",
        "h": "Der Schnitt geht durch die Achse und erfasst den ganzen Durchmesser.",
        "w": "Die Breite ist 2 · 3 cm = 6 cm, die Höhe 11 cm. Jede Schnittfläche ist 6 · 11 = 66 cm².",
        "fehlbilder": [{"antwort": 33, "beschreibung": "nur mit dem Radius gerechnet"},
                       {"antwort": 132, "beschreibung": "beide Schnittflächen zusammengezählt"}],
    },
    # ---------------- koerper_symmetrie ----------------
    {
        "k": "K7-V154", "karte": "koerper_symmetrie", "typ": "BR", "s": 2, "y": "auswahl", "regel": HT,
        "text": "Ein Körper hat 9 Symmetrieebenen. Welcher Körper ist das?",
        "a": ["ein Würfel",
              "ein Quader mit drei verschiedenen Kantenlängen",
              "eine quadratische Säule, die kein Würfel ist",
              "eine gerade Pyramide über einem Quadrat"],
        "richtig": 0,
        "h": "Je mehr Kanten gleich lang sind, desto mehr Ebenen.",
        "w": "Der Würfel hat 9 Symmetrieebenen: 3 mittige und 6 diagonale. Der Quader hat 3, die quadratische "
             "Säule 5, die gerade Pyramide über einem Quadrat 4.",
        "fehlbilder": [
            {"index": 1, "antwort": "ein Quader mit drei verschiedenen Kantenlängen", "beschreibung": "der hat nur 3 Ebenen"},
            {"index": 2, "antwort": "eine quadratische Säule, die kein Würfel ist", "beschreibung": "die hat 5 Ebenen"},
            {"index": 3, "antwort": "eine gerade Pyramide über einem Quadrat", "beschreibung": "die hat 4 Ebenen, eine je Seite des Quadrats"},
        ],
    },
    {
        "k": "K7-V155", "karte": "koerper_symmetrie", "typ": "UM", "s": 2, "y": "zahl", "regel": HT,
        "text": "Eine gerade Pyramide über einem regelmäßigen n-Eck hat 7 Symmetrieebenen. "
                "Wie viele Ecken hat diese Pyramide?",
        "c": "7 + 1", "erwartet": 8, "einheit": "Ecken",
        "h": "Bei dieser Pyramide gibt es genau n Symmetrieebenen.",
        "w": "7 Ebenen heißen n = 7, die Grundfläche ist ein Siebeneck. Ecken: 7 + 1 = 8.",
        "fehlbilder": [{"antwort": 7, "beschreibung": "die Spitze nicht mitgezählt"},
                       {"antwort": 14, "beschreibung": "die Zahl der Kanten gerechnet"}],
    },
    {
        "k": "K7-V156", "karte": "koerper_symmetrie", "typ": "ZW", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein gerades Prisma hat ein regelmäßiges Sechseck als Grundfläche. "
                "Weg A: die Regel n + 1 für gerade Prismen über regelmäßigen n-Ecken anwenden. "
                "Weg B: die senkrechten Ebenen zählen und die mittige waagerechte dazunehmen. "
                "Wie viele Symmetrieebenen hat das Prisma?",
        "c": "6 + 1", "erwartet": 7, "einheit": "Ebenen",
        "h": "Zu den senkrechten Ebenen kommt eine waagerechte.",
        "w": "Weg A: n + 1 = 6 + 1 = 7. Weg B: 6 senkrechte Ebenen und 1 waagerechte, zusammen 7.",
        "fehlbilder": [{"antwort": 6, "beschreibung": "die waagerechte Ebene vergessen"},
                       {"antwort": 9, "beschreibung": "wie beim Würfel gezählt"}],
    },
]
