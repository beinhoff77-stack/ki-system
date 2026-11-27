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
        "text": "Vier Kinder haben 6, 8, 11 und 15 Punkte. Zusammen sind das ① Punkte. "
                "Bei gerechter Verteilung bekommt jedes Kind ② Punkte. "
                "Das Kind mit den meisten Punkten gibt dafür ③ Punkte ab.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["6 + 8 + 11 + 15", "L1 // 4", "15 - L2"], "erwartet": [40, 10, 5], "entscheidend": 2,
        "h": "Erst alles zusammenzählen, dann gleichmäßig auf die Kinder verteilen.",
        "w": "Die Summe ist 40 Punkte. Auf 4 Kinder verteilt: 40 : 4 = 10 Punkte für jedes Kind. "
             "Das Kind mit 15 Punkten gibt 15 − 10 = 5 Punkte ab.",
        "fehlbilder": [{"luecke": 2, "antwort": 20, "rechnung": "L1 // 2", "beschreibung": "durch 2 statt durch 4 geteilt"},
                       {"luecke": 3, "antwort": 9, "rechnung": "15 - 6", "beschreibung": "mit dem kleinsten Wert statt mit dem Mittelwert verglichen"}],
    },
    {
        "k": "K7-V065", "karte": "mittelwert", "typ": "ZW", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Fünf Messwerte sind 12; 12; 12; 14 und 20. Weg A: alle Werte addieren und durch 5 teilen. "
                "Weg B: 12 als Schätzwert nehmen, die Abweichungen der Werte von 12 addieren, diese Summe durch 5 teilen "
                "und das Ergebnis zu 12 addieren. Wie groß ist der Mittelwert?",
        "c": "(12 * 3 + 14 + 20) // 5", "erwartet": 14,
        "h": "Beide Wege müssen denselben Mittelwert ergeben.",
        "w": "Weg A: 12 + 12 + 12 + 14 + 20 = 70, also 70 : 5 = 14. Weg B: Die Abweichungen von 12 sind 0, 0, 0, 2 und 8, "
             "zusammen 10. 10 : 5 = 2, und 12 + 2 = 14. Beide Wege geben 14.",
        "fehlbilder": [{"antwort": 70, "rechnung": "12 * 3 + 14 + 20", "beschreibung": "bei der Summe stehen geblieben"},
                       {"antwort": 12, "rechnung": "12", "beschreibung": "den häufigsten Wert genannt"}],
    },
    {
        "k": "K7-V066", "karte": "mittelwert", "typ": "AN", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Eine Klasse sammelt an fünf Tagen 18, 24, 15, 30 und 23 Pfandflaschen. "
                "Wie viele Flaschen sind das im Mittel pro Tag?",
        "c": "(18 + 24 + 15 + 30 + 23) // 5", "erwartet": 22, "einheit": "Flaschen",
        "h": "Summe durch Anzahl der Tage.",
        "w": "18 + 24 + 15 + 30 + 23 = 110 Flaschen. 110 : 5 = 22 Flaschen pro Tag.",
        "fehlbilder": [{"antwort": 110, "rechnung": "18 + 24 + 15 + 30 + 23", "beschreibung": "die Summe genannt"},
                       {"antwort": 23, "rechnung": "23", "beschreibung": "einen einzelnen Tag genannt"}],
    },
    # ---------------- mittel_tabelle ----------------
    {
        "k": "K7-V067", "karte": "mittel_tabelle", "typ": "BR", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "In einer Tabelle steht: Note 1 kommt 2-mal vor, Note 2 kommt 5-mal vor, Note 3 kommt 3-mal vor. "
                "Welche Rechnung gibt die Durchschnittsnote?",
        "a": ["(1 · 2 + 2 · 5 + 3 · 3) : 10", "(1 + 2 + 3) : 3", "(2 + 5 + 3) : 3", "(1 · 2 + 2 · 5 + 3 · 3) : 3"],
        "richtig": 0,
        "a_rechnung": ["(1*2+2*5+3*3)/10", "(1+2+3)/3", "(2+5+3)/3", "(1*2+2*5+3*3)/3"], "a_wert": 2.1,
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
                "Weg B: den Anteil jedes Werts an den zehn Werten bestimmen (3/10, 2/10, 5/10), jeden Wert mit seinem "
                "Anteil malnehmen und addieren. Wie groß ist der Mittelwert?",
        "c": "(4 * 3 + 6 * 2 + 10 * 5) / 10", "erwartet": 7.4,
        "h": "Beide Wege müssen denselben Mittelwert ergeben.",
        "w": "Weg A: 4 · 3 = 12, 6 · 2 = 12 und 10 · 5 = 50, zusammen 74. 74 : 10 = 7,4. "
             "Weg B: 4 · 0,3 + 6 · 0,2 + 10 · 0,5 = 1,2 + 1,2 + 5 = 7,4.",
        "fehlbilder": [{"antwort": 74, "rechnung": "4 * 3 + 6 * 2 + 10 * 5", "beschreibung": "bei der Summe stehen geblieben"},
                       {"antwort": 6.67, "rechnung": "(4 + 6 + 10) / 3", "beschreibung": "nur (4 + 6 + 10) : 3 gerechnet"}],
    },
    {
        "k": "K7-V069", "karte": "mittel_tabelle", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "In einer Tabelle kommt der Wert 5 dreimal vor und der Wert 8 zweimal. Dazu kommt ein weiterer "
                "Wert, der einmal vorkommt. Der Mittelwert aller sechs Werte ist 7. Wie groß ist der sechste Wert?",
        "c": "7 * 6 - (5 * 3 + 8 * 2)", "erwartet": 11,
        "h": "Rechne zuerst die Summe aller sechs Werte.",
        "w": "Die Summe ist 7 · 6 = 42. Bekannt sind 5 · 3 + 8 · 2 = 31. Der sechste Wert ist 42 − 31 = 11.",
        "fehlbilder": [{"antwort": 7, "rechnung": "7", "beschreibung": "den Mittelwert als fehlenden Wert genommen"},
                       {"antwort": 42, "rechnung": "7 * 6", "beschreibung": "die Summe genannt"}],
    },
    # ---------------- mittel_rueckwaerts ----------------
    {
        "k": "K7-V070", "karte": "mittel_rueckwaerts", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "In vier Tests hat jemand im Mittel 10 Punkte erreicht. Die ersten drei Tests hatten 7, 12 und "
                "8 Punkte. Wie viele Punkte hatte der vierte Test?",
        "c": "10 * 4 - (7 + 12 + 8)", "erwartet": 13,
        "h": "Wie hängen Mittelwert, Anzahl und Summe zusammen?",
        "w": "Summe aller vier Tests: 10 · 4 = 40 Punkte. Bekannt sind 7 + 12 + 8 = 27. "
             "Der vierte Test hatte 40 − 27 = 13 Punkte.",
        "fehlbilder": [{"antwort": 10, "rechnung": "10", "beschreibung": "den Mittelwert als fehlenden Wert angenommen"},
                       {"antwort": 40, "rechnung": "10 * 4", "beschreibung": "die Gesamtsumme genannt"}],
    },
    {
        "k": "K7-V071", "karte": "mittel_rueckwaerts", "typ": "AN", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Eine Läuferin ist an vier Trainingstagen im Mittel 8 km pro Tag gelaufen. "
                "Am fünften Tag läuft sie 13 km. Um wie viele Kilometer steigt der Mittelwert pro Tag "
                "durch den fünften Tag?",
        "c": "(8 * 4 + 13) / 5 - 8", "erwartet": 1, "einheit": "km",
        "h": "Rechne zuerst, wie viele Kilometer es an den ersten vier Tagen zusammen waren.",
        "w": "Die ersten vier Tage: 8 · 4 = 32 km. Mit dem fünften Tag: 32 + 13 = 45 km. Neuer Mittelwert: 45 : 5 = 9 km. "
             "Er steigt um 9 − 8 = 1 km.",
        "fehlbilder": [{"antwort": 5, "rechnung": "13 - 8", "beschreibung": "den fünften Tag mit dem alten Mittelwert verglichen"},
                       {"antwort": 9, "rechnung": "(8 * 4 + 13) / 5", "beschreibung": "den neuen Mittelwert genannt, nicht den Anstieg"}],
    },
    {
        "k": "K7-V072", "karte": "mittel_rueckwaerts", "typ": "BR", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "Ein Satz lautet: „Der Mittelwert von sechs Zahlen ist 12.“ Die Summe der sechs Zahlen heißt S. "
                "Welche Gleichung sagt dasselbe?",
        "a": ["S : 6 = 12", "S · 6 = 12", "S + 6 = 12", "S : 12 = 12"],
        "richtig": 0,
        "a_rechnung": ["72/6", "72*6", "72+6", "72/12"], "a_wert": 12,
        "h": "Wie wird ein Mittelwert aus der Summe berechnet?",
        "w": "Der Mittelwert ist die Summe geteilt durch die Anzahl: S : 6 = 12. Daraus folgt S = 12 · 6 = 72.",
        "fehlbilder": [
            {"index": 1, "antwort": "S · 6 = 12", "beschreibung": "mit der Anzahl malgenommen statt geteilt"},
            {"index": 2, "antwort": "S + 6 = 12", "beschreibung": "die Anzahl addiert statt zu teilen"},
            {"index": 3, "antwort": "S : 12 = 12", "beschreibung": "durch den Mittelwert statt durch die Anzahl geteilt"},
        ],
    },
]
