"""raum.schraegbilder_teil2 (Klasse 7 Realschule): 4 Lernkarten, 12 Aufgaben in neuer Form.

Lernkarten koordinaten, rotation, axialschnitt, koerper_symmetrie. Der Bestand steht in der
Themen-Datei raum.schraegbilder; das Feld „thema" trägt hier den Schlüssel mit `_teil2`,
weil Teil 2 eine eigene Einheit ist. Ohne Zeichnungen.
Feldbedeutung (c mit L1, L2 …, entscheidend, rechnung, a_rechnung): siehe Kopf von teile/zinsen.py.
"""
STAND = "2026-11-27"
TITEL = "Koordinaten, Rotationskörper und Axialschnitt"
PASST_NICHT = ()

HT = "id.flaeche_raum.haut"

AUFGABEN = [
    # ---------------- koordinaten ----------------
    {
        "k": "K7-V145", "karte": "koordinaten", "typ": "LW", "s": 1, "y": "luecken", "regel": HT,
        "text": "Ein Quader liegt mit A im Ursprung, seine Kanten verlaufen auf den Achsen. Die Ecke G(5 | 3 | 4) liegt "
                "gegenüber von A. Die Grundfläche des Quaders hat ① FE. Das Volumen des Quaders ist ② VE.",
        "schablone": "① = □; ② = □",
        "c": ["5 * 3", "L1 * 4"], "erwartet": [15, 60], "entscheidend": 1,
        "h": "Welche Koordinaten gehören zur Grundfläche?",
        "w": "Die Grundfläche liegt in der x-y-Ebene: 5 · 3 = 15 FE. Mit der Höhe 4 (z-Koordinate) ist das Volumen 15 · 4 = 60 VE.",
        "fehlbilder": [{"luecke": 1, "antwort": 20, "rechnung": "5 * 4", "beschreibung": "x und z statt x und y malgenommen"},
                       {"luecke": 2, "antwort": 45, "rechnung": "L1 * 3", "beschreibung": "mit der y- statt mit der z-Koordinate weitergerechnet"}],
    },
    {
        "k": "K7-V146", "karte": "koordinaten", "typ": "UM", "s": 2, "y": "zahl", "regel": HT,
        "text": "In einem Quader mit A im Ursprung, dessen Kanten auf den Achsen verlaufen, ist G(7 | 4 | 3) die Ecke gegenüber von A. "
                "Wie viele Flächeneinheiten hat die Grundfläche?",
        "c": "7 * 4", "erwartet": 28, "einheit": "FE",
        "h": "Welche Koordinaten gehören zur Grundfläche?",
        "w": "Der Quader ist 7 lang und 4 breit; die Höhe 3 gehört nicht zur Grundfläche. "
             "Grundfläche: 7 · 4 = 28 FE.",
        "fehlbilder": [{"antwort": 84, "rechnung": "7 * 4 * 3", "beschreibung": "das Volumen gerechnet"},
                       {"antwort": 22, "rechnung": "2 * (7 + 4)", "beschreibung": "den Umfang der Grundfläche gerechnet"}],
    },
    {
        "k": "K7-V147", "karte": "koordinaten", "typ": "FD", "s": 3, "y": "auswahl", "regel": HT,
        "text": "Ein Quader liegt mit A im Ursprung, ist 5 lang, 3 breit und 2 hoch; B liegt auf der x-Achse, D auf der y-Achse. "
                "Ein Kind sagt: Zeile 1: E liegt senkrecht über A, also E(0 | 0 | 2). "
                "Zeile 2: D liegt auf der y-Achse, also D(3 | 0 | 0). "
                "Zeile 3: H liegt senkrecht über D, also H(3 | 0 | 2). "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Auf welcher Achse hat eine Ecke nur einen Wert ungleich null?",
        "w": "Zeile 1 stimmt. In Zeile 2 sind x und y vertauscht: Auf der y-Achse sind x und z null, D(0 | 3 | 0). "
             "Zeile 3 folgt richtig aus Zeile 2 (2 höher), übernimmt aber den Fehler. Richtig wäre H(0 | 3 | 2).",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: E liegt 2 über dem Ursprung"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2; der Fehler steht schon in Zeile 2"},
        ],
    },
    {
        "k": "K7-V148", "karte": "rotation", "typ": "BR", "s": 2, "y": "auswahl", "regel": HT,
        "text": "Ein Rechteck mit den Seiten 4 cm und 7 cm dreht sich um die 7-cm-Seite. "
                "Welcher Körper entsteht, und mit welchen Maßen?",
        "a": ["ein Zylinder mit r = 4 cm und h = 7 cm",
              "ein Zylinder mit r = 7 cm und h = 4 cm",
              "ein Kegel mit r = 4 cm und h = 7 cm",
              "eine Kugel mit r = 7 cm"],
        "richtig": 0,
        "h": "Stell dir vor, wie sich das Rechteck dreht: Welche Seite bleibt an Ort und Stelle?",
        "w": "Die 7-cm-Seite liegt auf der Achse und wird die Höhe. Die 4-cm-Seite dreht sich im Kreis und wird "
             "der Radius: ein Zylinder mit r = 4 cm und h = 7 cm.",
        "fehlbilder": [
            {"index": 1, "antwort": "ein Zylinder mit r = 7 cm und h = 4 cm", "beschreibung": "Radius und Höhe vertauscht"},
            {"index": 2, "antwort": "ein Kegel mit r = 4 cm und h = 7 cm", "beschreibung": "ein Kegel entsteht aus einem rechtwinkligen Dreieck"},
            {"index": 3, "antwort": "eine Kugel mit r = 7 cm", "beschreibung": "eine Kugel entsteht aus einem Halbkreis"},
        ],
    },
    {
        "k": "K7-V149", "karte": "rotation", "typ": "VW", "s": 1, "y": "auswahl", "regel": HT,
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
        "text": "In einer Werkstatt entsteht ein Kegel, indem ein Pappdreieck mit einem rechten Winkel und den Katheten "
                "5 cm und 12 cm um die 12-cm-Kathete gedreht wird. Wie groß ist der Durchmesser des Kegels?",
        "c": "2 * 5", "erwartet": 10, "einheit": "cm",
        "h": "Welche Kathete bleibt beim Drehen auf der Achse?",
        "w": "Die 12-cm-Kathete liegt auf der Achse und wird die Höhe, die 5-cm-Kathete wird der Radius. "
             "Der Durchmesser ist 2 · 5 cm = 10 cm.",
        "fehlbilder": [{"antwort": 5, "rechnung": "5", "beschreibung": "den Radius genannt"},
                       {"antwort": 24, "rechnung": "2 * 12", "beschreibung": "die Höhe verdoppelt"}],
    },
    {
        "k": "K7-V151", "karte": "axialschnitt", "typ": "LW", "s": 1, "y": "luecken", "regel": HT,
        "text": "Ein Zylinder hat r = 4 cm und h = 9 cm. Der Axialschnitt geht durch die Achse. "
                "Das Schnittrechteck ist ① cm breit. Seine Fläche ist ② cm². Sein Umfang ist ③ cm.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["2 * 4", "L1 * 9", "2 * (L1 + 9)"], "erwartet": [8, 72, 34], "entscheidend": 1,
        "h": "Welche Strecke im Kreis geht durch den Mittelpunkt?",
        "w": "Der Schnitt erfasst den ganzen Durchmesser: 2 · 4 cm = 8 cm. Fläche: 8 · 9 = 72 cm². "
             "Umfang: 2 · (8 + 9) = 34 cm.",
        "fehlbilder": [{"luecke": 1, "antwort": 4, "rechnung": "4", "beschreibung": "den Radius statt des Durchmessers genommen"},
                       {"luecke": 2, "antwort": 36, "rechnung": "4 * 9", "beschreibung": "nur mit dem Radius gerechnet"}],
    },
    {
        "k": "K7-V152", "karte": "axialschnitt", "typ": "ZW", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein Zylinder hat den Durchmesser 10 cm und die Höhe 6 cm; er wird genau durch die Achse geschnitten. "
                "Weg A: Durchmesser mal Höhe. "
                "Weg B: den Schnitt in 10 Streifen von je 1 cm Breite zerlegen und die Flächen der Streifen addieren. "
                "Wie groß ist die Fläche des Axialschnitts?",
        "c": "10 * 6", "erwartet": 60, "einheit": "cm²",
        "h": "Beide Wege müssen dieselbe Fläche ergeben.",
        "w": "Weg A: 10 · 6 = 60 cm². Weg B: Ein Streifen hat 1 · 6 = 6 cm², zehn Streifen haben 60 cm². Der Axialschnitt hat 60 cm².",
        "fehlbilder": [{"antwort": 30, "rechnung": "5 * 6", "beschreibung": "nur mit dem Radius gerechnet"},
                       {"antwort": 120, "rechnung": "10 * 6 * 2", "beschreibung": "beide Hälften noch einmal verdoppelt"}],
    },
    {
        "k": "K7-V153", "karte": "axialschnitt", "typ": "AN", "s": 2, "y": "zahl", "regel": HT,
        "text": "Eine Dose ist ein Zylinder mit r = 3 cm und h = 11 cm. Sie wird längs genau durch die Achse "
                "aufgeschnitten. Wie groß ist eine der beiden entstehenden Schnittflächen?",
        "c": "2 * 3 * 11", "erwartet": 66, "einheit": "cm²",
        "h": "Wie breit ist der Schnitt, wenn er durch die Achse geht?",
        "w": "Die Breite ist 2 · 3 cm = 6 cm, die Höhe 11 cm. Jede Schnittfläche ist 6 · 11 = 66 cm².",
        "fehlbilder": [{"antwort": 33, "rechnung": "3 * 11", "beschreibung": "nur mit dem Radius gerechnet"},
                       {"antwort": 132, "rechnung": "2 * 66", "beschreibung": "beide Schnittflächen zusammengezählt"}],
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
        "h": "Zähle die Symmetrieebenen jedes genannten Körpers.",
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
        "h": "Wie viele Symmetrieebenen hat eine gerade Pyramide über einem Dreieck, wie viele über einem Quadrat?",
        "w": "7 Ebenen heißen n = 7, die Grundfläche ist ein Siebeneck. Ecken: 7 + 1 = 8.",
        "fehlbilder": [{"antwort": 7, "rechnung": "7", "beschreibung": "die Spitze nicht mitgezählt"},
                       {"antwort": 14, "rechnung": "2 * 7", "beschreibung": "die Zahl der Kanten gerechnet"}],
    },
    {
        "k": "K7-V156", "karte": "koerper_symmetrie", "typ": "ZW", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein gerades Prisma hat ein regelmäßiges Sechseck als Grundfläche. "
                "Weg A: die Regel n + 1 für gerade Prismen über regelmäßigen n-Ecken anwenden. "
                "Weg B: die Symmetrieachsen des Sechsecks zählen (durch gegenüberliegende Ecken, durch gegenüberliegende Seitenmitten) und die mittige waagerechte Ebene dazunehmen. "
                "Wie viele Symmetrieebenen hat das Prisma?",
        "c": "6 + 1", "erwartet": 7, "einheit": "Ebenen",
        "h": "Beide Wege müssen dieselbe Zahl ergeben.",
        "w": "Weg A: n + 1 = 6 + 1 = 7. Weg B: 3 Achsen durch gegenüberliegende Ecken und 3 durch gegenüberliegende Seitenmitten geben 6 senkrechte Ebenen, dazu 1 waagerechte: 7.",
        "fehlbilder": [{"antwort": 6, "rechnung": "3 + 3", "beschreibung": "die waagerechte Ebene vergessen"},
                       {"antwort": 9, "rechnung": "3 + 6", "beschreibung": "wie beim Würfel gezählt"}],
    },
]
