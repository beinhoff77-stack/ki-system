"""daten.kennwerte (Klasse 7 Realschule / 6 Gymnasium): 3 Lernkarten, 9 Aufgaben in neuer Form.

Bei nur drei Lernkarten reichen neun Plätze nicht für alle Formen. Vorrang hatte die Vorgabe
„jede der Formen Umkehren, Zwei Wege, Brücke, Anwenden mindestens zweimal“; dafür steht hier
nur ein Lückenweg und kein Fehler-Detektiv (der Bestand hat in jeder Lernkarte schon eine
Aufgabe vom Typ „fehler“).
"""
STAND = "2026-11-27"
TITEL = "Mittelwert"
PASST_NICHT = ()

KZ = "id.daten.kennzahl"

AUFGABEN = [
    # ---------------- mittelwert ----------------
    {
        "k": "K7-V064", "karte": "mittelwert", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Vier Kinder haben 6, 8, 11 und 15 Punkte. Zusammen sind das 6 + 8 + 11 + 15 = ① Punkte. "
                "Bei gerechter Verteilung bekommt jedes Kind ① : 4 = ② Punkte.",
        "schablone": "① = □; ② = □",
        "c": ["6 + 8 + 11 + 15", "(6 + 8 + 11 + 15) // 4"], "erwartet": [40, 10],
        "h": "Erst alles zusammenzählen, dann durch die Anzahl teilen.",
        "w": "Die Summe ist 40 Punkte. Auf 4 Kinder verteilt: 40 : 4 = 10 Punkte für jedes Kind.",
        "fehlbilder": [{"luecke": 2, "antwort": 20, "beschreibung": "durch 2 statt durch 4 geteilt"}],
    },
    {
        "k": "K7-V065", "karte": "mittelwert", "typ": "ZW", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Fünf Messwerte sind 12; 12; 12; 14 und 20. Weg A: alle Werte addieren und durch 5 teilen. "
                "Weg B: die drei gleichen Werte als 3 · 12 zusammenfassen und dann 14 und 20 dazu. "
                "Wie groß ist der Mittelwert?",
        "c": "(12 * 3 + 14 + 20) // 5", "erwartet": 14,
        "h": "Beide Wege müssen dieselbe Summe ergeben.",
        "w": "Weg A: 12 + 12 + 12 + 14 + 20 = 70, also 70 : 5 = 14. Weg B: 36 + 14 + 20 = 70, dasselbe Ergebnis.",
        "fehlbilder": [{"antwort": 70, "beschreibung": "bei der Summe stehen geblieben"},
                       {"antwort": 12, "beschreibung": "den häufigsten Wert genannt"}],
    },
    {
        "k": "K7-V066", "karte": "mittelwert", "typ": "AN", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Eine Klasse sammelt an fünf Tagen 18, 24, 15, 30 und 23 Pfandflaschen. "
                "Wie viele Flaschen sind das im Mittel pro Tag?",
        "c": "(18 + 24 + 15 + 30 + 23) // 5", "erwartet": 22, "einheit": "Flaschen",
        "h": "Summe durch Anzahl der Tage.",
        "w": "18 + 24 + 15 + 30 + 23 = 110 Flaschen. 110 : 5 = 22 Flaschen pro Tag.",
        "fehlbilder": [{"antwort": 110, "beschreibung": "die Summe genannt"},
                       {"antwort": 23, "beschreibung": "einen einzelnen Tag genannt"}],
    },
    # ---------------- mittel_tabelle ----------------
    {
        "k": "K7-V067", "karte": "mittel_tabelle", "typ": "BR", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "In einer Tabelle steht: Note 1 kommt 2-mal vor, Note 2 kommt 5-mal vor, Note 3 kommt 3-mal vor. "
                "Welche Rechnung gibt die Durchschnittsnote?",
        "a": ["(1 · 2 + 2 · 5 + 3 · 3) : 10", "(1 + 2 + 3) : 3", "(2 + 5 + 3) : 3", "(1 · 2 + 2 · 5 + 3 · 3) : 3"],
        "richtig": 0,
        "h": "Jede Note zählt so oft, wie sie vorkommt.",
        "w": "Note mal Anzahl: 2 + 10 + 9 = 21. Es sind 10 Noten, also 21 : 10 = 2,1.",
        "fehlbilder": [
            {"index": 1, "antwort": "(1 + 2 + 3) : 3", "beschreibung": "die Häufigkeiten weggelassen"},
            {"index": 2, "antwort": "(2 + 5 + 3) : 3", "beschreibung": "nur die Häufigkeiten addiert"},
            {"index": 3, "antwort": "(1 · 2 + 2 · 5 + 3 · 3) : 3", "beschreibung": "durch die Zahl der Spalten geteilt statt durch die Zahl der Noten"},
        ],
    },
    {
        "k": "K7-V068", "karte": "mittel_tabelle", "typ": "ZW", "s": 2, "y": "zahl", "regel": KZ,
        "text": "In einer Tabelle kommt der Wert 4 dreimal vor, der Wert 6 zweimal und der Wert 10 fünfmal. "
                "Weg A: jeden Wert mal seine Anzahl, addieren und durch 10 teilen. "
                "Weg B: alle zehn Werte einzeln hinschreiben und addieren. Wie groß ist der Mittelwert?",
        "c": "(4 * 3 + 6 * 2 + 10 * 5) / 10", "erwartet": 7.4,
        "h": "Beide Wege müssen dieselbe Summe ergeben.",
        "w": "Weg A: 4 · 3 = 12, 6 · 2 = 12 und 10 · 5 = 50, zusammen 74. 74 : 10 = 7,4. Weg B gibt dieselben 74.",
        "fehlbilder": [{"antwort": 74, "beschreibung": "bei der Summe stehen geblieben"},
                       {"antwort": 6.67, "beschreibung": "nur (4 + 6 + 10) : 3 gerechnet"}],
    },
    {
        "k": "K7-V069", "karte": "mittel_tabelle", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "In einer Tabelle kommt der Wert 5 dreimal vor und der Wert 8 zweimal. Dazu kommt ein weiterer "
                "Wert, der einmal vorkommt. Der Mittelwert aller sechs Werte ist 7. Wie groß ist der sechste Wert?",
        "c": "7 * 6 - (5 * 3 + 8 * 2)", "erwartet": 11,
        "h": "Rechne zuerst die Summe aller sechs Werte.",
        "w": "Die Summe ist 7 · 6 = 42. Bekannt sind 5 · 3 + 8 · 2 = 31. Der sechste Wert ist 42 − 31 = 11.",
        "fehlbilder": [{"antwort": 7, "beschreibung": "den Mittelwert als fehlenden Wert genommen"},
                       {"antwort": 42, "beschreibung": "die Summe genannt"}],
    },
    # ---------------- mittel_rueckwaerts ----------------
    {
        "k": "K7-V070", "karte": "mittel_rueckwaerts", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "In vier Tests hat jemand im Mittel 10 Punkte erreicht. Die ersten drei Tests hatten 7, 12 und "
                "8 Punkte. Wie viele Punkte hatte der vierte Test?",
        "c": "10 * 4 - (7 + 12 + 8)", "erwartet": 13,
        "h": "Summe = Mittelwert · Anzahl.",
        "w": "Summe aller vier Tests: 10 · 4 = 40 Punkte. Bekannt sind 7 + 12 + 8 = 27. "
             "Der vierte Test hatte 40 − 27 = 13 Punkte.",
        "fehlbilder": [{"antwort": 10, "beschreibung": "den Mittelwert als fehlenden Wert angenommen"},
                       {"antwort": 40, "beschreibung": "die Gesamtsumme genannt"}],
    },
    {
        "k": "K7-V071", "karte": "mittel_rueckwaerts", "typ": "AN", "s": 3, "y": "zahl", "regel": KZ,
        "text": "Eine Läuferin will an fünf Trainingstagen im Mittel 9 km pro Tag laufen. An den ersten vier Tagen "
                "lief sie 6, 9, 7 und 10 km. Wie viele Kilometer muss sie am fünften Tag laufen?",
        "c": "9 * 5 - (6 + 9 + 7 + 10)", "erwartet": 13, "einheit": "km",
        "h": "Rechne zuerst, wie viele Kilometer insgesamt nötig sind.",
        "w": "Insgesamt nötig: 9 · 5 = 45 km. Gelaufen sind 6 + 9 + 7 + 10 = 32 km. "
             "Am fünften Tag fehlen 45 − 32 = 13 km.",
        "fehlbilder": [{"antwort": 9, "beschreibung": "den Mittelwert als Tagesstrecke genommen"},
                       {"antwort": 45, "beschreibung": "die Gesamtstrecke genannt"}],
    },
    {
        "k": "K7-V072", "karte": "mittel_rueckwaerts", "typ": "BR", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "Ein Satz lautet: „Der Mittelwert von sechs Zahlen ist 12.“ Was weiß man damit sicher?",
        "a": ["Die Summe der sechs Zahlen ist 72.",
              "Jede der sechs Zahlen ist 12.",
              "Die größte der sechs Zahlen ist 12.",
              "Alle sechs Zahlen liegen zwischen 6 und 12."],
        "richtig": 0,
        "h": "Summe = Mittelwert · Anzahl.",
        "w": "Aus dem Mittelwert folgt nur die Summe: 12 · 6 = 72. Die einzelnen Zahlen können sehr "
             "verschieden sein, auch größer als 12.",
        "fehlbilder": [
            {"index": 1, "antwort": "Jede der sechs Zahlen ist 12.", "beschreibung": "das wäre ein Sonderfall, nicht die Regel"},
            {"index": 2, "antwort": "Die größte der sechs Zahlen ist 12.", "beschreibung": "Werte über dem Mittelwert sind erlaubt"},
            {"index": 3, "antwort": "Alle sechs Zahlen liegen zwischen 6 und 12.", "beschreibung": "der Mittelwert sagt nichts über die Spannweite"},
        ],
    },
]
