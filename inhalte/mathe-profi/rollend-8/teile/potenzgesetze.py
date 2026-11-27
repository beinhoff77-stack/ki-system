"""terme.potenzgesetze (Klasse 7 Realschule / 6 Gymnasium): 3 Lernkarten, 9 Aufgaben in neuer Form.

Bei nur drei Lernkarten reichen neun Plätze nicht für alle Formen. Vorrang hatte die Vorgabe
„je zweimal Umkehren, Zwei Wege, Brücke, Anwenden“; dafür steht hier ein Lückenweg und kein
Fehler-Detektiv – die Lernkarte fehler_finden besteht im Bestand schon aus Fehlersuche
(drei Aufgaben vom Typ „fehler“).
"""
STAND = "2026-11-27"
TITEL = "Potenzen"
PASST_NICHT = ()

HZ = "id.zahlen.hoch_zurueck"

AUFGABEN = [
    # ---------------- potenz_begriff ----------------
    {
        "k": "K7-V106", "karte": "potenz_begriff", "typ": "LW", "s": 1, "y": "luecken", "regel": HZ,
        "text": "Bei 3⁴ ist die Basis 3 und der Exponent 4. Ausgeschrieben heißt das 3 · 3 · 3 · 3. "
                "Rechne von links: 3 · 3 = ①, dann ① · 3 = 27 und 27 · 3 = ②.",
        "schablone": "① = □; ② = □",
        "c": ["3 * 3", "3 ** 4"], "erwartet": [9, 81],
        "h": "Rechne Schritt für Schritt, immer mal 3.",
        "w": "3 · 3 = 9, dann 9 · 3 = 27 und 27 · 3 = 81. Also ist 3⁴ = 81 – und nicht 3 · 4 = 12.",
        "fehlbilder": [{"luecke": 2, "antwort": 12, "beschreibung": "Basis mal Exponent gerechnet"}],
    },
    {
        "k": "K7-V107", "karte": "potenz_begriff", "typ": "UM", "s": 2, "y": "zahl", "regel": HZ,
        "text": "Eine Potenz mit der Basis 2 hat den Wert 64. Welchen Wert hat die Potenz mit demselben "
                "Exponenten, aber der Basis 3?",
        "c": "3 ** 6", "erwartet": 729,
        "h": "Finde zuerst den Exponenten: Wie oft muss 2 als Faktor stehen, damit 64 herauskommt?",
        "w": "2⁶ = 64, der Exponent ist also 6. Dann ist 3⁶ = 729.",
        "fehlbilder": [{"antwort": 96, "beschreibung": "64 mit dem Verhältnis der Basen malgenommen"},
                       {"antwort": 6, "beschreibung": "den Exponenten als Antwort genannt"}],
    },
    {
        "k": "K7-V108", "karte": "potenz_begriff", "typ": "AN", "s": 2, "y": "zahl", "regel": HZ,
        "text": "Ein Blatt Papier wird fünfmal in der Mitte gefaltet. Jede Faltung verdoppelt die Zahl der Lagen, "
                "vor dem Falten ist es eine Lage. Wie viele Lagen sind es danach?",
        "c": "2 ** 5", "erwartet": 32, "einheit": "Lagen",
        "h": "Jede Faltung verdoppelt: 2 · 2 · 2 · …",
        "w": "Fünf Verdopplungen ergeben 2⁵ = 32 Lagen. 5 · 2 = 10 wäre falsch, der Exponent zählt die Faktoren.",
        "fehlbilder": [{"antwort": 10, "beschreibung": "Anzahl der Faltungen mit 2 malgenommen"},
                       {"antwort": 25, "beschreibung": "Basis und Exponent getauscht"}],
    },
    # ---------------- negativer_exponent ----------------
    {
        "k": "K7-V109", "karte": "negativer_exponent", "typ": "BR", "s": 2, "y": "auswahl", "regel": HZ,
        "text": "Welche Zahl gehört zu 5⁻²?",
        "a": ["1/25", "−25", "−1/25", "1/10"], "richtig": 0,
        "h": "Ein negativer Exponent bedeutet Kehrbruch.",
        "w": "5⁻² = 1/5² = 1/25. Das Minus im Exponenten macht die Zahl nicht negativ, sondern bildet den Kehrbruch.",
        "fehlbilder": [
            {"index": 1, "antwort": "−25", "beschreibung": "das Minus als Vorzeichen des Ergebnisses gelesen"},
            {"index": 2, "antwort": "−1/25", "beschreibung": "Kehrbruch gebildet und zusätzlich ein Minus gesetzt"},
            {"index": 3, "antwort": "1/10", "beschreibung": "Basis mal Exponent gerechnet statt 5²"},
        ],
    },
    {
        "k": "K7-V110", "karte": "negativer_exponent", "typ": "ZW", "s": 2, "y": "zahl", "regel": HZ,
        "text": "Berechne 4⁻¹ + 4⁰. Weg A: beide Potenzen einzeln bestimmen und addieren. "
                "Weg B: 4⁻¹ als Kehrbruch schreiben und 4⁰ = 1 dazunehmen.",
        "c": "1 / 4 + 1", "erwartet": 1.25,
        "h": "Jede Zahl hoch 0 ist 1.",
        "w": "4⁻¹ = 1/4 und 4⁰ = 1. Zusammen: 1/4 + 1 = 1,25. Beide Wege führen zum selben Ergebnis.",
        "fehlbilder": [{"antwort": 0.25, "beschreibung": "4⁰ als 0 gerechnet"},
                       {"antwort": 5, "beschreibung": "4⁻¹ als 4 und 4⁰ als 1 gerechnet"}],
    },
    {
        "k": "K7-V111", "karte": "negativer_exponent", "typ": "UM", "s": 2, "y": "zahl", "regel": HZ,
        "text": "Eine Potenz mit der Basis 3 hat den Wert 1/27. Wie groß ist der Exponent?",
        "c": "0 - 3", "erwartet": -3,
        "h": "1/27 ist der Kehrbruch von 27.",
        "w": "27 = 3³, also ist 1/27 = 3⁻³. Der Exponent ist −3.",
        "fehlbilder": [{"antwort": 3, "beschreibung": "das Minus vergessen"},
                       {"antwort": 27, "beschreibung": "den Wert statt des Exponenten genannt"}],
    },
    # ---------------- fehler_finden ----------------
    {
        "k": "K7-V112", "karte": "fehler_finden", "typ": "ZW", "s": 2, "y": "zahl", "regel": HZ,
        "text": "Jemand behauptet 2⁻³ = −8. Weg A: 2⁻³ als Kehrbruch von 2³ schreiben. "
                "Weg B: bei 2¹ anfangen und immer wieder durch 2 teilen. Wie groß ist 2⁻³ wirklich?",
        "c": "1 / 8", "erwartet": 0.125,
        "h": "Ein Minus im Exponenten bildet den Kehrbruch, es macht keine negative Zahl.",
        "w": "Weg A: 2⁻³ = 1/2³ = 1/8. Weg B: 2; 1; 1/2; 1/4; 1/8. Beide Wege geben 1/8 = 0,125, nicht −8.",
        "fehlbilder": [{"antwort": -8, "beschreibung": "das Minus als Vorzeichen des Ergebnisses gelesen"},
                       {"antwort": 8, "beschreibung": "den Kehrbruch nicht gebildet"}],
    },
    {
        "k": "K7-V113", "karte": "fehler_finden", "typ": "AN", "s": 3, "y": "zahl", "regel": HZ,
        "text": "Ein Bakterium teilt sich jede halbe Stunde; aus einem werden dabei immer zwei. "
                "Wie viele Bakterien sind es nach 4 Stunden?",
        "c": "2 ** 8", "erwartet": 256, "einheit": "Bakterien",
        "h": "Rechne zuerst, wie viele Teilungen in 4 Stunden passen.",
        "w": "In 4 Stunden liegen 8 Teilungen. Also 2⁸ = 256 Bakterien. 2 · 8 = 16 wäre falsch.",
        "fehlbilder": [{"antwort": 16, "beschreibung": "Basis mal Zahl der Teilungen gerechnet"},
                       {"antwort": 8, "beschreibung": "die Zahl der Teilungen genannt"}],
    },
    {
        "k": "K7-V114", "karte": "fehler_finden", "typ": "BR", "s": 2, "y": "auswahl", "regel": HZ,
        "text": "Ein Satz lautet: „Die Zahl minus zwei wird quadriert, das Ergebnis ist 4.“ "
                "Welche Schreibweise passt dazu?",
        "a": ["(−2)²", "−2²", "−(2²)", "2⁻²"], "richtig": 0,
        "h": "Eine negative Basis steht in Klammern.",
        "w": "Nur in (−2)² wird die −2 selbst quadriert: (−2) · (−2) = 4. Ohne Klammern gilt das Quadrat nur für "
             "die 2, also ist −2² = −4. Und 2⁻² ist der Kehrbruch 1/4.",
        "fehlbilder": [
            {"index": 1, "antwort": "−2²", "beschreibung": "ohne Klammern wird nur die 2 quadriert: −4"},
            {"index": 2, "antwort": "−(2²)", "beschreibung": "dasselbe wie −2², also −4"},
            {"index": 3, "antwort": "2⁻²", "beschreibung": "negativer Exponent, das ergibt 1/4"},
        ],
    },
]
