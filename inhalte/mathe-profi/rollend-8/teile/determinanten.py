"""abbildungen.determinanten2 (Klasse 7 Realschule): 6 Lernkarten, 18 Aufgaben in neuer Form.

Ohne Zeichnungen: Punkte und Pfeile stehen als Koordinaten im Text.
Jede Determinante ist im Prüfprogramm nachgerechnet; bei den Vielecken zusätzlich über eine zweite
Rechnung (Trapez bzw. Zerlegung) im Lösungsweg geprüft.
Feldbedeutung (c mit L1, L2 …, entscheidend, rechnung, a_rechnung): siehe Kopf von teile/zinsen.py.
"""
STAND = "2026-11-27"
TITEL = "Determinanten und Flächen"
PASST_NICHT = ()

DG = "id.geometrie.deckungsgleich"

AUFGABEN = [
    # ---------------- det_berechnen ----------------
    {
        "k": "K7-V115", "karte": "det_berechnen", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Die Vektoren sind a = (5 | 3) und b = (2 | 7). Das erste Kreuzprodukt (oben links mal unten rechts) ist ①, "
                "das zweite (unten links mal oben rechts) ist ②. Die Determinante ist ③.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["5 * 7", "3 * 2", "L1 - L2"], "erwartet": [35, 6, 29], "entscheidend": 3,
        "h": "Das erste Produkt kommt zuerst, das zweite wird abgezogen.",
        "w": "5 · 7 = 35 und 3 · 2 = 6. Die Determinante ist 35 − 6 = 29.",
        "fehlbilder": [{"luecke": 3, "antwort": 41, "rechnung": "L1 + L2", "beschreibung": "die beiden Produkte addiert"},
                       {"luecke": 3, "antwort": -29, "rechnung": "L2 - L1", "beschreibung": "die Produkte in der falschen Reihenfolge abgezogen"}],
    },
    {
        "k": "K7-V116", "karte": "det_berechnen", "typ": "UM", "s": 2, "y": "zahl", "regel": DG,
        "text": "Für a = (6 | 2) und b = (x | 5) ist die Determinante 26. Wie groß ist x?",
        "c": "(6 * 5 - 26) // 2", "erwartet": 2,
        "h": "Schreibe die Determinante als Gleichung auf.",
        "w": "6 · 5 − 2 · x = 26, also 30 − 2x = 26 und 2x = 4. Damit ist x = 2.",
        "fehlbilder": [{"antwort": 4, "rechnung": "30 - 26", "beschreibung": "beim letzten Schritt nicht durch 2 geteilt"},
                       {"antwort": 28, "rechnung": "26 + 2", "beschreibung": "26 und 2 addiert"}],
    },
    {
        "k": "K7-V117", "karte": "det_berechnen", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind berechnet die Determinante von a = (6 | 4) und b = (2 | 5). "
                "Zeile 1: Über Kreuz malnehmen: 6 · 5 = 30 und 4 · 2 = 8. "
                "Zeile 2: Zwischen den beiden Produkten steht ein Plus. "
                "Zeile 3: Also ist die Determinante 30 + 8 = 38. "
                "In welcher Zeile steckt der erste Fehler?",
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
        "text": "Ein Parallelogramm hat A(0 | 0), B(5 | 2) und D(3 | 4). Die Pfeile sind AB = (5 | 2) und AD = (3 | 4). "
                "Das erste Kreuzprodukt ist ①, das zweite ②. Die Fläche des Parallelogramms ist ③ FE.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["5 * 4", "2 * 3", "L1 - L2"], "erwartet": [20, 6, 14], "entscheidend": 3,
        "h": "Erst beide Produkte, dann die Differenz.",
        "w": "5 · 4 = 20 und 2 · 3 = 6. Die Determinante ist 20 − 6 = 14, das Parallelogramm hat 14 FE.",
        "fehlbilder": [{"luecke": 3, "antwort": 26, "rechnung": "L1 + L2", "beschreibung": "die Produkte addiert"},
                       {"luecke": 2, "antwort": 8, "rechnung": "2 * 4", "beschreibung": "die falschen Zahlen über Kreuz genommen"}],
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
        "fehlbilder": [{"antwort": 12, "rechnung": "6 * 4 // 2", "beschreibung": "wie beim Dreieck halbiert"},
                       {"antwort": 20, "rechnung": "2 * (6 + 4)", "beschreibung": "Grundseite und Höhe addiert und verdoppelt"}],
    },
    {
        "k": "K7-V120", "karte": "parallelogramm", "typ": "AN", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Beet hat die Form eines Parallelogramms mit den Ecken A(0 | 0), B(8 | 0), C(10 | 3) und "
                "D(2 | 3). Eine Flächeneinheit entspricht 1 m². Wie viele Quadratmeter hat das Beet?",
        "c": "8 * 3 - 0 * 2", "erwartet": 24, "einheit": "m²",
        "h": "Bilde zuerst die Pfeile AB und AD.",
        "w": "AB = (8 | 0) und AD = (2 | 3). Determinante: 8 · 3 − 0 · 2 = 24. Das Beet hat 24 m².",
        "fehlbilder": [{"antwort": 12, "rechnung": "8 * 3 // 2", "beschreibung": "halbiert, als wäre es ein Dreieck"},
                       {"antwort": 30, "rechnung": "10 * 3", "beschreibung": "die Koordinaten der Ecke C malgenommen"}],
    },
    # ---------------- dreieck ----------------
    {
        "k": "K7-V121", "karte": "dreieck", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Ein Dreieck hat A(0 | 0), B(6 | 1) und C(2 | 5), die Pfeile sind AB = (6 | 1) und AC = (2 | 5). "
                "Die Determinante ist ①. Das Dreieck hat ② FE. "
                "Eine Flächeneinheit sind 4 m²; das Dreieck hat also ③ m².",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["6 * 5 - 1 * 2", "L1 // 2", "4 * L2"], "erwartet": [28, 14, 56], "entscheidend": 2,
        "h": "Das Dreieck ist das halbe Parallelogramm.",
        "w": "Die Determinante ist 30 − 2 = 28. Das Dreieck hat 28 : 2 = 14 FE, das sind 14 · 4 m² = 56 m².",
        "fehlbilder": [{"luecke": 2, "antwort": 28, "rechnung": "L1", "beschreibung": "das Halbieren vergessen"},
                       {"luecke": 3, "antwort": 112, "rechnung": "4 * L1", "beschreibung": "mit der Determinante statt mit der Dreiecksfläche umgerechnet"}],
    },
    {
        "k": "K7-V122", "karte": "dreieck", "typ": "BR", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Im Dreieck ABC sind die Pfeile AB = (4 | 1) und AC = (1 | 3) gegeben. "
                "Welche Rechnung gibt die Fläche des Dreiecks?",
        "a": ["(4 · 3 − 1 · 1) : 2", "4 · 3 − 1 · 1", "(4 · 1 − 1 · 3) : 2", "(4 · 3 + 1 · 1) : 2"], "richtig": 0,
        "a_rechnung": ["(4*3-1*1)/2", "4*3-1*1", "(4*1-1*3)/2", "(4*3+1*1)/2"], "a_wert": 5.5,
        "h": "Wofür steht die Determinante der beiden Pfeile geometrisch?",
        "w": "Die Determinante 4 · 3 − 1 · 1 = 11 ist die Fläche des Parallelogramms aus den beiden Pfeilen. "
             "Das Dreieck ist die Hälfte: 5,5 FE.",
        "fehlbilder": [
            {"index": 1, "antwort": "4 · 3 − 1 · 1", "beschreibung": "das Halbieren vergessen, das ist die Fläche des Parallelogramms"},
            {"index": 2, "antwort": "(4 · 1 − 1 · 3) : 2", "beschreibung": "die falschen Zahlen über Kreuz genommen"},
            {"index": 3, "antwort": "(4 · 3 + 1 · 1) : 2", "beschreibung": "die Produkte addiert statt abgezogen"},
        ],
    },
    {
        "k": "K7-V123", "karte": "dreieck", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind berechnet die Fläche des Dreiecks ABC mit AB = (7 | 2) und AC = (3 | 6). "
                "Zeile 1: Die Determinante ist 7 · 3 − 2 · 6 = 9. "
                "Zeile 2: Das ist die Fläche des zugehörigen Parallelogramms, also 9 FE. "
                "Zeile 3: Das Dreieck ist die Hälfte davon, also 4,5 FE. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Welche Zahlen gehören über Kreuz zusammen?",
        "w": "Zeile 1 ist falsch: Die Determinante ist 7 · 6 − 2 · 3 = 36 (oben links mal unten rechts). "
             "Die Zeilen 2 und 3 folgen richtig aus dem falschen Wert. Richtig wären 36 FE und 18 FE.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile folgt richtig aus Zeile 1: die Determinante gibt das Parallelogramm"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2: 9 : 2 = 4,5"},
        ],
    },
    {
        "k": "K7-V124", "karte": "umlaufsinn", "typ": "BR", "s": 2, "y": "auswahl", "regel": DG,
        "text": "Für ein Dreieck ABC ergibt die Determinante aus AB und AC den Wert −19. Welcher Satz passt dazu?",
        "a": ["Die Ecken laufen im Uhrzeigersinn, die Fläche ist 9,5 FE.",
              "Die Fläche ist −9,5 FE.",
              "Die drei Punkte liegen auf einer Geraden.",
              "Die Fläche ist 19 FE."],
        "richtig": 0,
        "h": "Überlege, was ein Minus bei einer Fläche bedeuten kann.",
        "w": "Das Minus zeigt nur die Reihenfolge der Ecken. Die Fläche ist der halbe Betrag: 19 : 2 = 9,5 FE.",
        "fehlbilder": [
            {"index": 1, "antwort": "Die Fläche ist −9,5 FE.", "beschreibung": "eine Fläche kann nicht negativ sein"},
            {"index": 2, "antwort": "Die drei Punkte liegen auf einer Geraden.", "beschreibung": "das gilt nur bei der Determinante 0"},
            {"index": 3, "antwort": "Die Fläche ist 19 FE.", "beschreibung": "das Halbieren vergessen"},
        ],
    },
    {
        "k": "K7-V125", "karte": "umlaufsinn", "typ": "VW", "s": 1, "y": "auswahl", "regel": DG,
        "text": "Für ein Dreieck ABC ergibt die Determinante aus AB und AC den Wert 18. "
                "Du willst, dass sich nur das Vorzeichen ändert und der Betrag gleich bleibt. Was änderst du?",
        "a": ["zwei Ecken in der Reihenfolge vertauschen, zum Beispiel B und C",
              "alle Koordinaten mit −1 malnehmen",
              "die Determinante durch 2 teilen",
              "die Koordinaten von A um 1 verschieben"],
        "richtig": 0,
        "h": "Was ändert sich am Umlaufsinn, wenn du zwei Ecken tauschst?",
        "w": "Tauscht man B und C, vertauschen sich die beiden Pfeile, und die Determinante wechselt das Vorzeichen: −18. "
             "Alle Koordinaten mit −1 zu nehmen dreht die Figur um 180°, die Determinante bleibt 18. "
             "Durch 2 teilen halbiert den Betrag, und eine Verschiebung von A ändert die Pfeile und meist den Betrag.",
        "fehlbilder": [
            {"index": 1, "antwort": "alle Koordinaten mit −1 malnehmen", "beschreibung": "beide Pfeile wechseln das Vorzeichen, die Determinante bleibt gleich"},
            {"index": 2, "antwort": "die Determinante durch 2 teilen", "beschreibung": "das ergibt die Dreiecksfläche, das Vorzeichen bleibt"},
            {"index": 3, "antwort": "die Koordinaten von A um 1 verschieben", "beschreibung": "dann sind die Pfeile andere, der Betrag ändert sich meist"},
        ],
    },
    {
        "k": "K7-V126", "karte": "umlaufsinn", "typ": "FD", "s": 3, "y": "auswahl", "regel": DG,
        "text": "Ein Kind rechnet mit AB = (2 | 5) und AC = (6 | 1). "
                "Zeile 1: Die Determinante ist 2 · 1 − 5 · 6 = −28. "
                "Zeile 2: Das Minus zeigt, dass A, B und C im Uhrzeigersinn liegen. "
                "Zeile 3: Die Fläche des Dreiecks ist deshalb −14 FE. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Kann eine Fläche negativ sein?",
        "w": "Zeile 1 und 2 stimmen. Flächen sind nie negativ: man nimmt den Betrag, also 28 : 2 = 14 FE.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: 2 − 30 = −28"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig, so ist das Vorzeichen zu deuten"},
        ],
    },
    {
        "k": "K7-V127", "karte": "viereck", "typ": "LW", "s": 1, "y": "luecken", "regel": DG,
        "text": "Ein Viereck hat A(0 | 0), B(6 | 2), C(5 | 6) und D(1 | 4). Die Diagonale AC teilt es in die "
                "Dreiecke ABC und ACD. Die Determinante für ABC (aus AB und AC) ist ①, die für ACD (aus AC und AD) ist ②. "
                "Die Fläche des Vierecks ist ③ FE.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["6 * 6 - 2 * 5", "5 * 4 - 6 * 1", "(L1 + L2) // 2"], "erwartet": [26, 14, 20], "entscheidend": 3,
        "h": "Beide Determinanten werden addiert, dann wird halbiert.",
        "w": "Für ABC: 36 − 10 = 26. Für ACD: 20 − 6 = 14. Zusammen 40, halbiert 20 FE.",
        "fehlbilder": [{"luecke": 3, "antwort": 40, "rechnung": "L1 + L2", "beschreibung": "das Halbieren vergessen"},
                       {"luecke": 3, "antwort": 13, "rechnung": "L1 // 2", "beschreibung": "nur das Dreieck ABC gerechnet"}],
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
        "fehlbilder": [{"antwort": 24, "rechnung": "12 + 12", "beschreibung": "bei Weg A das Halbieren vergessen"},
                       {"antwort": 6, "rechnung": "12 // 2", "beschreibung": "nur ein Dreieck gerechnet und halbiert"}],
    },
    {
        "k": "K7-V129", "karte": "viereck", "typ": "AN", "s": 3, "y": "zahl", "regel": DG,
        "text": "Ein Grundstück hat die Ecken A(0 | 0), B(10 | 0), C(10 | 6) und D(0 | 4). "
                "Eine Flächeneinheit entspricht 1 m². Wie viele Quadratmeter hat das Grundstück?",
        "c": "((10 * 6 - 0 * 10) + (10 * 4 - 6 * 0)) // 2", "erwartet": 50, "einheit": "m²",
        "h": "Teile das Viereck mit der Diagonale AC in zwei Dreiecke.",
        "w": "Dreieck ABC: 10 · 6 − 0 · 10 = 60. Dreieck ACD: 10 · 4 − 6 · 0 = 40. Zusammen 100, halbiert 50 m². "
             "Probe als Trapez: (4 + 6) : 2 · 10 = 50.",
        "fehlbilder": [{"antwort": 100, "rechnung": "60 + 40", "beschreibung": "das Halbieren vergessen"},
                       {"antwort": 30, "rechnung": "60 // 2", "beschreibung": "nur das Dreieck ABC gerechnet"}],
    },
    # ---------------- vieleck ----------------
    {
        "k": "K7-V130", "karte": "vieleck", "typ": "VW", "s": 1, "y": "auswahl", "regel": DG,
        "text": "Ein Fünfeck ABCDE soll von A aus in Dreiecke zerlegt werden. "
                "Welche Determinanten rechnest du?",
        "a": ["AB mit AC, AC mit AD, AD mit AE",
              "AB mit AD, AD mit AE",
              "AB mit AC, AB mit AD, AB mit AE",
              "AB mit AC, AC mit AE"],
        "richtig": 0,
        "h": "Zeichne ein Fünfeck und die Diagonalen von A aus.",
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
        "text": "Ein konvexes Fünfeck, dessen Ecken gegen den Uhrzeigersinn benannt sind, hat die Fläche 27 FE. "
                "Von A aus wird es in drei Dreiecke zerlegt. Zwei der drei Determinanten sind 12 und 19. "
                "Wie groß ist die dritte?",
        "c": "27 * 2 - (12 + 19)", "erwartet": 23,
        "h": "Wie hängen die drei Dreiecksflächen mit der Fläche des Fünfecks zusammen?",
        "w": "Die Summe der Determinanten ist 2 · 27 = 54. Bekannt sind 12 + 19 = 31. Die dritte ist "
             "54 − 31 = 23.",
        "fehlbilder": [{"antwort": -4, "rechnung": "27 - (12 + 19)", "beschreibung": "mit der Fläche statt mit der doppelten Fläche gerechnet"},
                       {"antwort": 31, "rechnung": "12 + 19", "beschreibung": "die Summe der beiden bekannten genannt"}],
    },
    {
        "k": "K7-V132", "karte": "vieleck", "typ": "AN", "s": 2, "y": "zahl", "regel": DG,
        "text": "Ein Grundstück hat die Form eines Fünfecks mit A(0 | 0), B(8 | 0), C(10 | 5), D(4 | 8) und "
                "E(0 | 5). Eine Flächeneinheit entspricht 1 m². Wie viele Quadratmeter hat das Grundstück?",
        "c": "((8 * 5 - 0 * 10) + (10 * 8 - 5 * 4) + (4 * 5 - 8 * 0)) // 2", "erwartet": 60, "einheit": "m²",
        "h": "Von A aus zerlegen und immer zwei benachbarte Pfeile nehmen.",
        "w": "AB mit AC: 40. AC mit AD: 60. AD mit AE: 20. Zusammen 120, halbiert 60 m².",
        "fehlbilder": [{"antwort": 120, "rechnung": "40 + 60 + 20", "beschreibung": "das Halbieren vergessen"},
                       {"antwort": 50, "rechnung": "(40 + 60) // 2", "beschreibung": "das Dreieck ADE übersprungen"}],
    },
]
