"""raum.schraegbilder, Teil 1 (Klasse 7 Realschule): 4 Lernkarten, 12 Aufgaben in neuer Form.

Lernkarten pyramide, lage, wahre_groesse, raumwinkel. Ohne Zeichnungen: Körper und Kanten sind
im Text beschrieben. Die Lernkarte lage ist durchgehend qualitativ, dort gibt es keinen Lückenweg.
"""
STAND = "2026-11-27"
TITEL = "Pyramiden, Lage und Schrägbild"
PASST_NICHT = ()

HT = "id.flaeche_raum.haut"

AUFGABEN = [
    # ---------------- pyramide ----------------
    {
        "k": "K7-V133", "karte": "pyramide", "typ": "LW", "s": 1, "y": "luecken", "regel": HT,
        "text": "Eine Pyramide hat ein Sechseck als Grundfläche, also n = 6. "
                "Ecken: 6 + 1 = ①. Kanten: 2 · 6 = ②. Flächen: so viele wie Ecken.",
        "schablone": "① = □; ② = □",
        "c": ["6 + 1", "2 * 6"], "erwartet": [7, 12],
        "h": "Die eine Ecke mehr ist die Spitze.",
        "w": "Ecken: 6 am Boden und die Spitze, also 7. Kanten: 6 am Boden und 6 zur Spitze, also 12. "
             "Flächen: 6 Dreiecke und die Grundfläche, also auch 7.",
        "fehlbilder": [{"luecke": 2, "antwort": 6, "beschreibung": "nur die Bodenkanten gezählt"}],
    },
    {
        "k": "K7-V134", "karte": "pyramide", "typ": "UM", "s": 2, "y": "zahl", "regel": HT,
        "text": "Eine Pyramide hat 16 Kanten. Wie viele Ecken hat sie?",
        "c": "16 // 2 + 1", "erwartet": 9, "einheit": "Ecken",
        "h": "Die Hälfte der Kanten liegt am Boden.",
        "w": "2n = 16, also n = 8: die Grundfläche ist ein Achteck. Ecken: 8 + 1 = 9.",
        "fehlbilder": [{"antwort": 8, "beschreibung": "die Spitze nicht mitgezählt"},
                       {"antwort": 17, "beschreibung": "zu den Kanten 1 dazugezählt"}],
    },
    {
        "k": "K7-V135", "karte": "pyramide", "typ": "FD", "s": 3, "y": "auswahl", "regel": HT,
        "text": "Ein Kind beschreibt eine fünfseitige Pyramide. Zeile 1: Die Grundfläche ist ein Fünfeck, also n = 5. "
                "Zeile 2: Sie hat 5 + 1 = 6 Ecken und 2 · 5 = 10 Kanten. "
                "Zeile 3: Flächen hat sie 5, nämlich die fünf Dreiecke. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Welche Fläche fehlt in der Zählung?",
        "w": "Zeile 1 und 2 stimmen. Zu den fünf Dreiecken kommt die Grundfläche dazu: 5 + 1 = 6 Flächen.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: fünfseitig heißt n = 5"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: 6 Ecken und 10 Kanten"},
        ],
    },
    # ---------------- lage ----------------
    {
        "k": "K7-V136", "karte": "lage", "typ": "BR", "s": 2, "y": "auswahl", "regel": HT,
        "text": "In einem Quader ABCDEFGH laufen die Kanten AB und CG. Sie haben keinen gemeinsamen Punkt und "
                "auch nicht dieselbe Richtung. Wie heißt diese Lage?",
        "a": ["windschief", "parallel", "schneidend", "deckungsgleich"], "richtig": 0,
        "h": "Kein gemeinsamer Punkt und nicht dieselbe Richtung.",
        "w": "Zwei Geraden im Raum ohne gemeinsamen Punkt und ohne gleiche Richtung heißen windschief. "
             "AB läuft unten nach rechts, CG hinten senkrecht nach oben, und sie treffen sich nicht.",
        "fehlbilder": [
            {"index": 1, "antwort": "parallel", "beschreibung": "parallel verlangt dieselbe Richtung"},
            {"index": 2, "antwort": "schneidend", "beschreibung": "schneidend verlangt einen gemeinsamen Punkt"},
            {"index": 3, "antwort": "deckungsgleich", "beschreibung": "das beschreibt Figuren, nicht die Lage zweier Geraden"},
        ],
    },
    {
        "k": "K7-V137", "karte": "lage", "typ": "VW", "s": 2, "y": "auswahl", "regel": HT,
        "text": "Du sollst entscheiden, ob zwei Kanten eines Quaders parallel sind. "
                "Welches Vorgehen führt zum Ziel?",
        "a": ["prüfen, ob sie dieselbe Richtung haben",
              "prüfen, ob sie sich nicht schneiden",
              "prüfen, ob sie gleich lang sind",
              "prüfen, ob sie zur selben Seitenfläche gehören"],
        "richtig": 0,
        "h": "Ohne Schnittpunkt heißt im Raum nicht automatisch parallel.",
        "w": "Parallel verlangt dieselbe Richtung. Kein Schnittpunkt genügt nicht, denn windschiefe Kanten "
             "schneiden sich auch nicht. Länge und Seitenfläche entscheiden gar nicht.",
        "fehlbilder": [
            {"index": 1, "antwort": "prüfen, ob sie sich nicht schneiden", "beschreibung": "windschiefe Kanten schneiden sich auch nicht"},
            {"index": 2, "antwort": "prüfen, ob sie gleich lang sind", "beschreibung": "gleich lange Kanten können windschief sein"},
            {"index": 3, "antwort": "prüfen, ob sie zur selben Seitenfläche gehören", "beschreibung": "in einer Fläche können sie sich auch schneiden"},
        ],
    },
    {
        "k": "K7-V138", "karte": "lage", "typ": "UM", "s": 2, "y": "auswahl", "regel": HT,
        "text": "Zwei Kanten eines Quaders sind windschief. Was weiß man damit sicher über sie?",
        "a": ["Sie liegen in keiner gemeinsamen Ebene.",
              "Sie sind gleich lang.",
              "Sie schneiden sich in genau einem Punkt.",
              "Sie haben dieselbe Richtung."],
        "richtig": 0,
        "h": "Was wäre bei parallelen oder bei schneidenden Kanten anders?",
        "w": "Windschiefe Geraden liegen in keiner gemeinsamen Ebene: sie treffen sich nicht und haben nicht "
             "dieselbe Richtung. Über ihre Längen sagt das nichts.",
        "fehlbilder": [
            {"index": 1, "antwort": "Sie sind gleich lang.", "beschreibung": "die Länge hat mit der Lage nichts zu tun"},
            {"index": 2, "antwort": "Sie schneiden sich in genau einem Punkt.", "beschreibung": "dann wären sie schneidend"},
            {"index": 3, "antwort": "Sie haben dieselbe Richtung.", "beschreibung": "dann wären sie parallel"},
        ],
    },
    # ---------------- wahre_groesse ----------------
    {
        "k": "K7-V139", "karte": "wahre_groesse", "typ": "LW", "s": 1, "y": "luecken", "regel": HT,
        "text": "Im Schrägbild ist eine Kante nach hinten mit q = 0,5 gezeichnet; gezeichnet ist sie 3 cm lang. "
                "Ihre wahre Länge ist 3 cm : 0,5 = ① cm. Eine Kante parallel zur Zeichenebene ist 4 cm gezeichnet "
                "und deshalb auch wahr 4 cm lang. Zusammen sind beide wahren Längen ② cm.",
        "schablone": "① = □; ② = □",
        "c": ["3 / (1 / 2)", "3 / (1 / 2) + 4"], "erwartet": [6, 10],
        "h": "Nach hinten teilst du durch q; parallel zur Zeichenebene bleibt die Länge echt.",
        "w": "3 cm : 0,5 = 6 cm wahre Länge. Die andere Kante bleibt 4 cm. Zusammen 10 cm.",
        "fehlbilder": [{"luecke": 1, "antwort": 1.5, "beschreibung": "mit q malgenommen statt geteilt"}],
    },
    {
        "k": "K7-V140", "karte": "wahre_groesse", "typ": "ZW", "s": 2, "y": "zahl", "regel": HT,
        "text": "Eine Kante nach hinten ist wahr 8 cm lang und wird mit q = 0,5 gezeichnet. "
                "Weg A: 8 cm mit q malnehmen. Weg B: die Hälfte von 8 cm nehmen. "
                "Wie lang ist die Kante im Schrägbild?",
        "c": "8 * 1 / 2", "erwartet": 4, "einheit": "cm",
        "h": "Beim Zeichnen nimmst du mal q, beim Zurückrechnen teilst du durch q.",
        "w": "Weg A: 8 cm · 0,5 = 4 cm. Weg B: die Hälfte von 8 cm ist 4 cm. Im Schrägbild ist sie 4 cm lang.",
        "fehlbilder": [{"antwort": 16, "beschreibung": "durch q geteilt statt malgenommen"},
                       {"antwort": 8, "beschreibung": "die Verkürzung vergessen"}],
    },
    {
        "k": "K7-V141", "karte": "wahre_groesse", "typ": "AN", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein Quader ist 10 cm lang, 6 cm tief und 4 cm hoch. Im Schrägbild wird die Tiefe mit q = 0,5 "
                "gezeichnet. Wie lang wird die Tiefenkante im Schrägbild?",
        "c": "6 * 1 / 2", "erwartet": 3, "einheit": "cm",
        "h": "Nur die Kanten nach hinten werden verkürzt.",
        "w": "6 cm · 0,5 = 3 cm. Länge und Höhe bleiben mit 10 cm und 4 cm in wahrer Größe.",
        "fehlbilder": [{"antwort": 5, "beschreibung": "die Länge verkürzt statt der Tiefe"},
                       {"antwort": 12, "beschreibung": "durch q geteilt statt malgenommen"}],
    },
    # ---------------- raumwinkel ----------------
    {
        "k": "K7-V142", "karte": "raumwinkel", "typ": "BR", "s": 2, "y": "auswahl", "regel": HT,
        "text": "Ein gerades Prisma hat ein regelmäßiges Sechseck als Grundfläche. Zwei benachbarte Seitenflächen "
                "treffen sich an einer senkrechten Kante. Wie groß ist der Winkel zwischen ihnen?",
        "a": ["120°", "90°", "60°", "108°"], "richtig": 0,
        "h": "Der Winkel ist der Innenwinkel der Grundfläche.",
        "w": "Im regelmäßigen Sechseck ist jeder Innenwinkel 120°. Beim geraden Prisma ist das auch der Winkel "
             "zwischen zwei benachbarten Seitenflächen.",
        "fehlbilder": [
            {"index": 1, "antwort": "90°", "beschreibung": "das gilt nur beim Quader"},
            {"index": 2, "antwort": "60°", "beschreibung": "60° ist der Winkel im gleichseitigen Dreieck"},
            {"index": 3, "antwort": "108°", "beschreibung": "108° gehört zum regelmäßigen Fünfeck"},
        ],
    },
    {
        "k": "K7-V143", "karte": "raumwinkel", "typ": "AN", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein Pavillon ist ein gerades Prisma mit einem regelmäßigen Fünfeck als Grundfläche. "
                "Wie groß ist der Winkel zwischen zwei benachbarten Seitenwänden?",
        "c": "(5 - 2) * 180 // 5", "erwartet": 108, "einheit": "°",
        "h": "Rechne den Innenwinkel des regelmäßigen Fünfecks.",
        "w": "Die Innenwinkelsumme ist (5 − 2) · 180° = 540°, jeder Innenwinkel also 540° : 5 = 108°. "
             "Das ist auch der Winkel zwischen den Seitenwänden.",
        "fehlbilder": [{"antwort": 72, "beschreibung": "den Außenwinkel 360° : 5 gerechnet"},
                       {"antwort": 90, "beschreibung": "wie beim Quader 90° angenommen"}],
    },
    {
        "k": "K7-V144", "karte": "raumwinkel", "typ": "ZW", "s": 2, "y": "zahl", "regel": HT,
        "text": "Ein gerades Prisma hat ein regelmäßiges Achteck als Grundfläche. "
                "Weg A: die Innenwinkelsumme (8 − 2) · 180° durch 8 teilen. "
                "Weg B: 360° : 8 = 45° als Außenwinkel bestimmen und 180° − 45° rechnen. "
                "Wie groß ist der Winkel zwischen zwei benachbarten Seitenflächen?",
        "c": "(8 - 2) * 180 // 8", "erwartet": 135, "einheit": "°",
        "h": "Beide Wege geben denselben Innenwinkel.",
        "w": "Weg A: (8 − 2) · 180° = 1 080°, geteilt durch 8 sind 135°. Weg B: 180° − 45° = 135°.",
        "fehlbilder": [{"antwort": 45, "beschreibung": "den Außenwinkel als Antwort genommen"},
                       {"antwort": 1080, "beschreibung": "bei der Innenwinkelsumme stehen geblieben"}],
    },
]
