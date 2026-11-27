"""abbildungen.determinanten2 (Klasse 7 Realschule): 6 Lernkarten, 18 Aufgaben in neuer Form.

Ohne Zeichnungen: Punkte und Pfeile stehen als Koordinaten im Text.
Jede Determinante ist im Prüfprogramm nachgerechnet; bei den Vielecken zusätzlich über eine zweite
Rechnung (Trapez bzw. Zerlegung) im Lösungsweg geprüft.
"""
STAND = "2026-11-27"
TITEL = "Determinanten und Flächen"
PASST_NICHT = ()

DG = "id.geometrie.deckungsgleich"

AUFGABEN = [
    # ---------------- det_berechnen ----------------
    {
        "k": "K7-V115", "karte": "det_berechnen", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Die Vektoren sind a = (5 | 3) und b = (2 | 7). Über Kreuz malnehmen: 5 · 7 = ① und 3 · 2 = 6. "
                "Die Determinante ist ① − 6 = ②.",
        "schablone": "① = □; ② = □",
        "c": ["5 * 7", "5 * 7 - 3 * 2"], "erwartet": [35, 29],
        "h": "Oben links mal unten rechts, dann minus unten links mal oben rechts.",
        "w": "5 · 7 = 35 und 3 · 2 = 6. Die Determinante ist 35 − 6 = 29.",
        "fehlbilder": [{"luecke": 2, "antwort": 41, "beschreibung": "die beiden Produkte addiert"}],
    },
    {
        "k": "K7-V116", "karte": "det_berechnen", "typ": "UM", "s": 2, "y": "zahl", "regel": DG,
        "text": "Für a = (6 | 2) und b = (x | 5) ist die Determinante 26. Wie groß ist x?",
        "c": "(6 * 5 - 26) // 2", "erwartet": 2,
        "h": "Schreibe die Determinante als Gleichung auf.",
        "w": "6 · 5 − 2 · x = 26, also 30 − 2x = 26 und 2x = 4. Damit ist x = 2.",
        "fehlbilder": [{"antwort": 4, "beschreibung": "beim letzten Schritt nicht durch 2 geteilt"},
                       {"antwort": 28, "beschreibung": "26 und 2 addiert"}],
    },
    {
        "k": "K7-V117", "karte": "det_berechnen", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind berechnet die Determinante von a = (6 | 4) und b = (2 | 5). "
                "Zeile 1: Über Kreuz malnehmen: 6 · 5 = 30 und 4 · 2 = 8. "
                "Zeile 2: Zwischen den beiden Produkten steht ein Plus. "
                "Zeile 3: Also ist die Determinante 30 + 8 = 38. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Welches Rechenzeichen steht zwischen den beiden Produkten?",
        "w": "Zeile 1 stimmt. Zwischen den Produkten steht immer ein Minus: 30 − 8 = 22.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: beide Kreuzprodukte stimmen"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile rechnet nur mit dem falschen Zeichen aus Zeile 2 weiter"},
        ],
    },
    # ---------------- parallelogramm ----------------
    {
        "k": "K7-V118", "karte": "parallelogramm", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Ein Parallelogramm hat A(0 | 0), B(6 | 2) und D(1 | 5). Die Pfeile sind AB = (6 | 2) und "
                "AD = (1 | 5). Über Kreuz: 6 · 5 = ① und 2 · 1 = 2. Die Fläche ist ① − 2 = ② FE.",
        "schablone": "① = □; ② = □",
        "c": ["6 * 5", "6 * 5 - 2 * 1"], "erwartet": [30, 28],
        "h": "Erst beide Produkte, dann die Differenz.",
        "w": "6 · 5 = 30 und 2 · 1 = 2. Die Determinante ist 30 − 2 = 28, das Parallelogramm hat 28 FE.",
        "fehlbilder": [{"luecke": 2, "antwort": 32, "beschreibung": "die Produkte addiert"}],
    },
    {
        "k": "K7-V119", "karte": "parallelogramm", "typ": "ZW", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Parallelogramm hat A(1 | 2), B(7 | 2), C(9 | 6) und D(3 | 6). "
                "Weg A: Determinante aus AB = (6 | 0) und AD = (2 | 4). "
                "Weg B: Grundseite [AB] ist 6 lang, die Höhe ist 4; Grundseite mal Höhe. "
                "Wie groß ist die Fläche?",
        "c": "6 * 4 - 0 * 2", "erwartet": 24, "einheit": "FE",
        "h": "Beide Wege müssen dieselbe Fläche ergeben.",
        "w": "Weg A: 6 · 4 − 0 · 2 = 24. Weg B: 6 · 4 = 24. Die Fläche ist 24 FE.",
        "fehlbilder": [{"antwort": 12, "beschreibung": "wie beim Dreieck halbiert"},
                       {"antwort": 20, "beschreibung": "Grundseite und Höhe addiert und verdoppelt"}],
    },
    {
        "k": "K7-V120", "karte": "parallelogramm", "typ": "AN", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Beet hat die Form eines Parallelogramms mit den Ecken A(0 | 0), B(8 | 0), C(10 | 3) und "
                "D(2 | 3). Eine Flächeneinheit entspricht 1 m². Wie viele Quadratmeter hat das Beet?",
        "c": "8 * 3 - 0 * 2", "erwartet": 24, "einheit": "m²",
        "h": "Bilde zuerst die Pfeile AB und AD.",
        "w": "AB = (8 | 0) und AD = (2 | 3). Determinante: 8 · 3 − 0 · 2 = 24. Das Beet hat 24 m².",
        "fehlbilder": [{"antwort": 12, "beschreibung": "halbiert, als wäre es ein Dreieck"},
                       {"antwort": 30, "beschreibung": "mit den Punkten gerechnet statt mit den Pfeilen"}],
    },
    # ---------------- dreieck ----------------
    {
        "k": "K7-V121", "karte": "dreieck", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Ein Dreieck hat A(0 | 0), B(6 | 1) und C(2 | 5). Die Pfeile sind AB = (6 | 1) und AC = (2 | 5). "
                "Die Determinante ist 6 · 5 − 1 · 2 = ①. Das Dreieck ist die Hälfte davon: ① : 2 = ② FE.",
        "schablone": "① = □; ② = □",
        "c": ["6 * 5 - 1 * 2", "(6 * 5 - 1 * 2) // 2"], "erwartet": [28, 14],
        "h": "Das Dreieck ist das halbe Parallelogramm.",
        "w": "Die Determinante ist 30 − 2 = 28. Das Dreieck hat 28 : 2 = 14 FE.",
        "fehlbilder": [{"luecke": 2, "antwort": 28, "beschreibung": "das Halbieren vergessen"}],
    },
    {
        "k": "K7-V122", "karte": "dreieck", "typ": "BR", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Ein Satz lautet: „Die Determinante aus AB und AC ist 23.“ "
                "Wie groß ist dann die Fläche des Dreiecks ABC?",
        "a": ["11,5 FE", "23 FE", "46 FE", "nicht bestimmbar"], "richtig": 0,
        "h": "Das Dreieck ist halb so groß wie das Parallelogramm.",
        "w": "Die Determinante gibt die Fläche des Parallelogramms: 23 FE. Das Dreieck ist die Hälfte, "
             "also 11,5 FE.",
        "fehlbilder": [
            {"index": 1, "antwort": "23 FE", "beschreibung": "das Halbieren vergessen"},
            {"index": 2, "antwort": "46 FE", "beschreibung": "verdoppelt statt halbiert"},
            {"index": 3, "antwort": "nicht bestimmbar", "beschreibung": "die Determinante genügt, man braucht die Punkte nicht"},
        ],
    },
    {
        "k": "K7-V123", "karte": "dreieck", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind berechnet die Fläche des Dreiecks ABC mit AB = (7 | 2) und AC = (3 | 6). "
                "Zeile 1: Die Determinante ist 7 · 6 − 2 · 3 = 36. "
                "Zeile 2: Das ist die Fläche des zugehörigen Parallelogramms. "
                "Zeile 3: Also hat das Dreieck auch 36 FE. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Wie groß ist das Dreieck im Vergleich zum Parallelogramm?",
        "w": "Zeile 1 und 2 stimmen. Das Dreieck ist die Hälfte: 36 : 2 = 18 FE.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: 42 − 6 = 36"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: die Determinante gibt das Parallelogramm"},
        ],
    },
    # ---------------- umlaufsinn ----------------
    {
        "k": "K7-V124", "karte": "umlaufsinn", "typ": "BR", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Für ein Dreieck ergibt die Determinante −19. Welcher Satz passt dazu?",
        "a": ["Die Ecken laufen im Uhrzeigersinn, die Fläche ist 9,5 FE.",
              "Die Fläche ist −9,5 FE.",
              "Die drei Punkte liegen auf einer Geraden.",
              "Die Fläche ist 19 FE."],
        "richtig": 0,
        "h": "Flächen sind nie negativ.",
        "w": "Das Minus zeigt nur die Reihenfolge der Ecken. Die Fläche ist der halbe Betrag: 19 : 2 = 9,5 FE.",
        "fehlbilder": [
            {"index": 1, "antwort": "Die Fläche ist −9,5 FE.", "beschreibung": "eine Fläche kann nicht negativ sein"},
            {"index": 2, "antwort": "Die drei Punkte liegen auf einer Geraden.", "beschreibung": "das gilt nur bei der Determinante 0"},
            {"index": 3, "antwort": "Die Fläche ist 19 FE.", "beschreibung": "das Halbieren vergessen"},
        ],
    },
    {
        "k": "K7-V125", "karte": "umlaufsinn", "typ": "VW", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Du hast für ein Viereck die Determinante −30 erhalten. Wie gehst du weiter vor?",
        "a": ["den Betrag nehmen und festhalten, dass die Ecken im Uhrzeigersinn benannt sind",
              "das Ergebnis als negative Fläche aufschreiben",
              "die Rechnung als falsch verwerfen und neu beginnen",
              "die Determinante mit vertauschten Spalten noch einmal rechnen und beide Werte addieren"],
        "richtig": 0,
        "h": "Was bedeutet das Vorzeichen?",
        "w": "Das Minus zeigt den Umlaufsinn. Man nimmt den Betrag, hier 30, und hält fest, dass die Ecken im "
             "Uhrzeigersinn benannt sind.",
        "fehlbilder": [
            {"index": 1, "antwort": "das Ergebnis als negative Fläche aufschreiben", "beschreibung": "Flächen sind nie negativ"},
            {"index": 2, "antwort": "die Rechnung als falsch verwerfen und neu beginnen", "beschreibung": "die Rechnung ist richtig, nur die Reihenfolge der Ecken ist anders"},
            {"index": 3, "antwort": "die Determinante mit vertauschten Spalten noch einmal rechnen und beide Werte addieren",
             "beschreibung": "beim Vertauschen kehrt sich nur das Vorzeichen um, die Summe wäre 0"},
        ],
    },
    {
        "k": "K7-V126", "karte": "umlaufsinn", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind rechnet mit AB = (2 | 5) und AC = (6 | 1). "
                "Zeile 1: Die Determinante ist 2 · 1 − 5 · 6 = −28. "
                "Zeile 2: Das Minus zeigt, dass A, B und C im Uhrzeigersinn liegen. "
                "Zeile 3: Die Fläche des Dreiecks ist deshalb −14 FE. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Kann eine Fläche negativ sein?",
        "w": "Zeile 1 und 2 stimmen. Flächen sind nie negativ: man nimmt den Betrag, also 28 : 2 = 14 FE.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: 2 − 30 = −28"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig, so ist das Vorzeichen zu deuten"},
        ],
    },
    # ---------------- viereck ----------------
    {
        "k": "K7-V127", "karte": "viereck", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Ein Viereck hat A(0 | 0), B(6 | 2), C(5 | 6) und D(1 | 4). Die Diagonale AC teilt es in die "
                "Dreiecke ABC und ACD. Für ABC: 6 · 6 − 2 · 5 = ①. Für ACD: 5 · 4 − 6 · 1 = 14. "
                "Die Fläche ist (① + 14) : 2 = ② FE.",
        "schablone": "① = □; ② = □",
        "c": ["6 * 6 - 2 * 5", "(6 * 6 - 2 * 5 + 14) // 2"], "erwartet": [26, 20],
        "h": "Erst beide Determinanten, dann addieren und halbieren.",
        "w": "Für ABC: 36 − 10 = 26. Für ACD: 20 − 6 = 14. Zusammen 40, halbiert 20 FE.",
        "fehlbilder": [{"luecke": 2, "antwort": 40, "beschreibung": "das Halbieren vergessen"}],
    },
    {
        "k": "K7-V128", "karte": "viereck", "typ": "ZW", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Viereck hat A(0 | 0), B(4 | 0), C(4 | 3) und D(0 | 3). "
                "Weg A: mit der Diagonale AC in zwei Dreiecke zerlegen, beide Determinanten addieren und halbieren. "
                "Weg B: es ist ein Rechteck, also Länge mal Breite. Wie groß ist die Fläche?",
        "c": "4 * 3", "erwartet": 12, "einheit": "FE",
        "h": "Beide Wege müssen dieselbe Fläche ergeben.",
        "w": "Weg A: Dreieck ABC gibt 12, Dreieck ACD gibt 12, zusammen 24, halbiert 12. "
             "Weg B: 4 · 3 = 12. Die Fläche ist 12 FE.",
        "fehlbilder": [{"antwort": 24, "beschreibung": "bei Weg A das Halbieren vergessen"},
                       {"antwort": 6, "beschreibung": "nur ein Dreieck gerechnet"}],
    },
    {
        "k": "K7-V129", "karte": "viereck", "typ": "AN", "s": 3, "y": "zahl", "regel": DG,
        "text": "Ein Grundstück hat die Ecken A(0 | 0), B(10 | 0), C(10 | 6) und D(0 | 4). "
                "Eine Flächeneinheit entspricht 1 m². Wie viele Quadratmeter hat das Grundstück?",
        "c": "((10 * 6 - 0 * 10) + (10 * 4 - 6 * 0)) // 2", "erwartet": 50, "einheit": "m²",
        "h": "Teile das Viereck mit der Diagonale AC in zwei Dreiecke.",
        "w": "Dreieck ABC: 10 · 6 − 0 · 10 = 60. Dreieck ACD: 10 · 4 − 6 · 0 = 40. Zusammen 100, halbiert 50 m². "
             "Probe als Trapez: (4 + 6) : 2 · 10 = 50.",
        "fehlbilder": [{"antwort": 100, "beschreibung": "das Halbieren vergessen"},
                       {"antwort": 60, "beschreibung": "nur das Dreieck ABC gerechnet"}],
    },
    # ---------------- vieleck ----------------
    {
        "k": "K7-V130", "karte": "vieleck", "typ": "VW", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Ein Fünfeck ABCDE soll von A aus in Dreiecke zerlegt werden. "
                "Welche Determinanten rechnest du?",
        "a": ["AB mit AC, AC mit AD, AD mit AE",
              "AB mit AD, AD mit AE",
              "AB mit AC, AB mit AD, AB mit AE",
              "AB mit AC, AC mit AE"],
        "richtig": 0,
        "h": "Immer zwei benachbarte Pfeile.",
        "w": "Von A aus entstehen die Dreiecke ABC, ACD und ADE. Dazu nimmt man immer zwei benachbarte Pfeile: "
             "AB mit AC, AC mit AD, AD mit AE.",
        "fehlbilder": [
            {"index": 1, "antwort": "AB mit AD, AD mit AE", "beschreibung": "das Dreieck ABC fehlt, ein Pfeil wurde übersprungen"},
            {"index": 2, "antwort": "AB mit AC, AB mit AD, AB mit AE", "beschreibung": "immer von AB aus: Stücke zählen doppelt"},
            {"index": 3, "antwort": "AB mit AC, AC mit AE", "beschreibung": "AD fehlt, damit fehlt ein Dreieck"},
        ],
    },
    {
        "k": "K7-V131", "karte": "vieleck", "typ": "UM", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Fünfeck hat die Fläche 27 FE. Zwei der drei Determinanten von A aus sind 12 und 19. "
                "Wie groß ist die dritte?",
        "c": "27 * 2 - (12 + 19)", "erwartet": 23,
        "h": "Die Summe aller Determinanten ist die doppelte Fläche.",
        "w": "Die Summe der Determinanten ist 2 · 27 = 54. Bekannt sind 12 + 19 = 31. Die dritte ist "
             "54 − 31 = 23.",
        "fehlbilder": [{"antwort": -4, "beschreibung": "mit der Fläche statt mit der doppelten Fläche gerechnet"},
                       {"antwort": 31, "beschreibung": "die Summe der beiden bekannten genannt"}],
    },
    {
        "k": "K7-V132", "karte": "vieleck", "typ": "AN", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Grundstück hat die Form eines Fünfecks mit A(0 | 0), B(8 | 0), C(10 | 5), D(4 | 8) und "
                "E(0 | 5). Eine Flächeneinheit entspricht 1 m². Wie viele Quadratmeter hat das Grundstück?",
        "c": "((8 * 5 - 0 * 10) + (10 * 8 - 5 * 4) + (4 * 5 - 8 * 0)) // 2", "erwartet": 60, "einheit": "m²",
        "h": "Von A aus zerlegen und immer zwei benachbarte Pfeile nehmen.",
        "w": "AB mit AC: 40. AC mit AD: 60. AD mit AE: 20. Zusammen 120, halbiert 60 m².",
        "fehlbilder": [{"antwort": 120, "beschreibung": "das Halbieren vergessen"},
                       {"antwort": 50, "beschreibung": "ein Dreieck übersprungen"}],
    },
]
