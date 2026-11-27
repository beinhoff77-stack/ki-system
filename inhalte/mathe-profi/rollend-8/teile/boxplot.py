"""daten.boxplot (Klasse 7): 6 Lernkarten, 18 Aufgaben in neuer Form.

Ohne Zeichnungen: Boxplots sind über ihre fünf Kennwerte im Text beschrieben.
Feldbedeutung (c mit L1, L2 …, entscheidend, rechnung, a_rechnung): siehe Kopf von teile/zinsen.py.
"""
STAND = "2026-11-27"
TITEL = "Median, Quartile und Boxplot"
PASST_NICHT = ()

KZ = "id.daten.kennzahl"

AUFGABEN = [
    # ---------------- median ----------------
    {
        "k": "K7-V073", "karte": "median", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Die sechs Werte 10; 4; 16; 6; 12; 8 sollen ihren Median bekommen. Man ordnet sie zuerst der Größe nach. "
                "Dann stehen in der Mitte zwei Werte; ihre Summe ist ①. "
                "Der Median ist die Hälfte davon: ②. "
                "Er liegt um ③ über dem kleinsten Wert.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["8 + 10", "L1 // 2", "L2 - 4"], "erwartet": [18, 9, 5], "entscheidend": 1,
        "h": "Ordne zuerst, dann suche die Mitte.",
        "w": "Geordnet: 4; 6; 8; 10; 12; 16. In der Mitte stehen 8 und 10, ihre Summe ist 18. Der Median ist 18 : 2 = 9. "
             "Der kleinste Wert ist 4, also liegt der Median um 9 − 4 = 5 darüber.",
        "fehlbilder": [{"luecke": 1, "antwort": 22, "rechnung": "16 + 6", "beschreibung": "die mittleren Plätze der ungeordneten Liste genommen"},
                       {"luecke": 2, "antwort": 11, "rechnung": "(16 + 6) // 2", "beschreibung": "mit den Werten der ungeordneten Mitte weitergerechnet"}],
    },
    {
        "k": "K7-V074", "karte": "median", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Fünf Werte stehen der Größe nach geordnet da: 2; 5; x; 11; 14. Der Median ist um 4 größer als der zweite Wert. "
                "Wie groß ist x?",
        "c": "5 + 4", "erwartet": 9,
        "h": "Welche Stelle in einer Reihe aus fünf geordneten Werten ist die Mitte?",
        "w": "Der Median ist der dritte Wert, also x. Er ist 5 + 4 = 9. Die Reihenfolge stimmt dann auch: 9 liegt "
             "zwischen 5 und 11.",
        "fehlbilder": [{"antwort": 4, "rechnung": "4", "beschreibung": "nur den Zuschlag genannt"},
                       {"antwort": 11, "rechnung": "11", "beschreibung": "den vierten Wert genommen"}],
    },
    {
        "k": "K7-V075", "karte": "median", "typ": "FD", "s": 3, "y": "auswahl", "regel": KZ,
        "text": "Ein Kind bestimmt den Median von 8; 2; 11; 5; 14. "
                "Zeile 1: Der Median ist der mittlere Wert der der Größe nach geordneten Liste. "
                "Zeile 2: In der Mitte der Liste 8; 2; 11; 5; 14 steht die 11, also ist der Median 11. "
                "Zeile 3: Es sind fünf Werte, deshalb gibt es genau einen mittleren Wert. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Bestimme den Median selbst und vergleiche.",
        "w": "Zeile 1 stimmt. Zeile 2 ordnet die Liste nicht: Geordnet ist 2; 5; 8; 11; 14, der mittlere Wert ist 8. "
             "Zeile 3 ist für sich richtig: bei fünf Werten gibt es einen mittleren Wert.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, so ist der Median bestimmt"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile ist richtig: bei ungerader Anzahl gibt es einen mittleren Wert"},
        ],
    },
    {
        "k": "K7-V076", "karte": "kennwerte", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Fünf Kinder haben 3, 7, 7, 9 und 14 Bücher. Zusammen sind das ① Bücher. "
                "Der Mittelwert ist ② Bücher. "
                "Das Kind mit den meisten Büchern hat ③ Bücher mehr als der Mittelwert.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["3 + 7 + 7 + 9 + 14", "L1 // 5", "14 - L2"], "erwartet": [40, 8, 6], "entscheidend": 2,
        "h": "Summe durch Anzahl.",
        "w": "3 + 7 + 7 + 9 + 14 = 40 und 40 : 5 = 8 Bücher. Das größte Kind hat 14 − 8 = 6 Bücher mehr. "
             "Der häufigste Wert wäre 7, die Spannweite 11.",
        "fehlbilder": [{"luecke": 2, "antwort": 7, "rechnung": "7", "beschreibung": "den häufigsten Wert als Mittelwert genommen"},
                       {"luecke": 3, "antwort": 11, "rechnung": "14 - 3", "beschreibung": "mit dem kleinsten Wert statt mit dem Mittelwert verglichen"}],
    },
    {
        "k": "K7-V077", "karte": "kennwerte", "typ": "ZW", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Sechs Zeiten sind 21; 25; 19; 30; 25 und 22 Sekunden. Weg A: größten und kleinsten Wert suchen "
                "und voneinander abziehen. Weg B: alle Werte ordnen und die Abstände zwischen je zwei "
                "benachbarten Werten addieren. Wie groß ist die Spannweite?",
        "c": "30 - 19", "erwartet": 11, "einheit": "s",
        "h": "Beide Wege müssen dieselbe Spannweite ergeben.",
        "w": "Weg A: Der größte Wert ist 30 s, der kleinste 19 s: 30 − 19 = 11 s. Weg B: geordnet 19; 21; 22; 25; 25; 30, "
             "die Abstände sind 2, 1, 3, 0 und 5, zusammen 11 s.",
        "fehlbilder": [{"antwort": 30, "rechnung": "30", "beschreibung": "den größten Wert genannt"},
                       {"antwort": 25, "rechnung": "25", "beschreibung": "den häufigsten Wert genannt"}],
    },
    {
        "k": "K7-V078", "karte": "kennwerte", "typ": "AN", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Ein Verein notiert an sechs Tagen die Besucherzahlen 24, 30, 24, 31, 24 und 29. "
                "Um wie viel liegt der Mittelwert über dem häufigsten Wert?",
        "c": "(24 * 3 + 30 + 31 + 29) // 6 - 24", "erwartet": 3,
        "h": "Rechne erst den Mittelwert, dann suche den häufigsten Wert.",
        "w": "Die Summe ist 162, der Mittelwert 162 : 6 = 27. Der häufigste Wert ist 24 (dreimal). "
             "27 − 24 = 3.",
        "fehlbilder": [{"antwort": 27, "rechnung": "(24 * 3 + 30 + 31 + 29) // 6", "beschreibung": "den Mittelwert genannt"},
                       {"antwort": 7, "rechnung": "31 - 24", "beschreibung": "die Spannweite genommen"}],
    },
    # ---------------- mittel_median ----------------
    {
        "k": "K7-V079", "karte": "mittel_median", "typ": "BR", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "Ein Satz lautet: „Bei diesen Daten ist der Mittelwert größer als der Median.“ "
                "Welche Zahlenreihe passt dazu?",
        "a": ["1; 2; 3; 4; 30", "2; 3; 4; 5; 6", "1; 2; 3; 4; 5", "1; 30; 31; 32; 33"],
        "richtig": 0,
        "h": "Rechne bei jeder Reihe Mittelwert und Median aus.",
        "w": "Reihe 1: Mittelwert 40 : 5 = 8, Median 3 – der Mittelwert ist größer. Reihe 2 und 3: Mittelwert und Median "
             "sind gleich (4 bzw. 3). Reihe 4: Mittelwert 127 : 5 = 25,4, Median 31 – der Mittelwert ist kleiner.",
        "fehlbilder": [
            {"index": 1, "antwort": "2; 3; 4; 5; 6", "beschreibung": "gleichmäßig verteilt: Mittelwert und Median sind beide 4"},
            {"index": 2, "antwort": "1; 2; 3; 4; 5", "beschreibung": "gleichmäßig verteilt: Mittelwert und Median sind beide 3"},
            {"index": 3, "antwort": "1; 30; 31; 32; 33", "beschreibung": "ein sehr kleiner Wert zieht den Mittelwert unter den Median"},
        ],
    },
    {
        "k": "K7-V080", "karte": "mittel_median", "typ": "VW", "s": 1, "y": "auswahl", "regel": KZ,
        "text": "In einer Gruppe verdienen fünf Personen 1 800 €, 1 900 €, 2 000 €, 2 100 € und 12 000 €. "
                "Du sollst den Verdienst angeben, der zu den meisten Personen der Gruppe passt. Welches Vorgehen passt?",
        "a": ["den Median nehmen, weil ein Ausreißer dabei ist",
              "den Mittelwert nehmen, weil er alle Werte benutzt",
              "die Spannweite nehmen",
              "den größten Wert nehmen"],
        "richtig": 0,
        "h": "Vergleiche die fünf Werte miteinander: Was fällt auf?",
        "w": "Der Median ist 2 000 €, der Mittelwert 3 960 €. Vier der fünf Personen verdienen rund 2 000 €; "
             "der Median beschreibt die Gruppe deshalb besser.",
        "fehlbilder": [
            {"index": 1, "antwort": "den Mittelwert nehmen, weil er alle Werte benutzt",
             "beschreibung": "der Ausreißer zieht ihn auf 3 960 €, das verdient niemand in der Gruppe"},
            {"index": 2, "antwort": "die Spannweite nehmen", "beschreibung": "die Spannweite beschreibt die Streuung, nicht die Mitte"},
            {"index": 3, "antwort": "den größten Wert nehmen", "beschreibung": "das ist gerade der Ausreißer"},
        ],
    },
    {
        "k": "K7-V081", "karte": "mittel_median", "typ": "FD", "s": 3, "y": "auswahl", "regel": KZ,
        "text": "Ein Kind vergleicht Mittelwert und Median von 8; 11; 11; 14; 101. "
                "Zeile 1: Der Median ist der Mittelwert aus kleinstem und größtem Wert: (8 + 101) : 2 = 54,5. "
                "Zeile 2: Der Mittelwert aller fünf Werte ist 145 : 5 = 29. "
                "Zeile 3: Also liegt der Median weit über dem Mittelwert. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Ordne die Werte und suche den mittleren.",
        "w": "Zeile 1 ist falsch: Der Median ist der mittlere Wert der geordneten Liste, also 11. "
             "Zeile 2 ist richtig (8 + 11 + 11 + 14 + 101 = 145). Zeile 3 folgt richtig aus Zeile 1 und 2 – "
             "mit dem richtigen Median 11 läge der Median dagegen weit unter dem Mittelwert.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: die Summe ist 145, geteilt durch 5 sind 29"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus den Werten 54,5 und 29"},
        ],
    },
    {
        "k": "K7-V082", "karte": "quartile", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Acht Werte stehen geordnet da: 2; 5; 7; 9; 11; 14; 18; 21. Die untere Hälfte besteht aus den vier "
                "kleinsten Werten. Die beiden mittleren Werte dieser Hälfte haben die Summe ①. Ihr Median ist Q₁ = ②. "
                "Q₃ ist der Median der oberen Hälfte: ③. Der Abstand von Q₁ bis Q₃ ist ④.",
        "schablone": "① = □; ② = □; ③ = □; ④ = □",
        "c": ["5 + 7", "L1 // 2", "(14 + 18) // 2", "L3 - L2"], "erwartet": [12, 6, 16, 10], "entscheidend": 3,
        "h": "Q₁ und Q₃ sind die Mediane der beiden Hälften.",
        "w": "Untere Hälfte 2; 5; 7; 9: mittlere Werte 5 und 7, Summe 12, Q₁ = 6. Obere Hälfte 11; 14; 18; 21: "
             "mittlere Werte 14 und 18, Q₃ = 16. Abstand: 16 − 6 = 10.",
        "fehlbilder": [{"luecke": 2, "antwort": 5, "rechnung": "5", "beschreibung": "den zweiten Wert genommen statt den Median der Hälfte"},
                       {"luecke": 3, "antwort": 14, "rechnung": "14", "beschreibung": "den zweiten Wert der oberen Hälfte genommen statt den Median"}],
    },
    {
        "k": "K7-V083", "karte": "quartile", "typ": "ZW", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Neun Werte stehen geordnet da: 1; 2; 4; 5; 7; 8; 10; 11; 15. "
                "Weg A: den Median streichen und von der unteren Hälfte den Median nehmen. "
                "Weg B: die Stelle (9 + 1) : 4 = 2,5 ausrechnen, an der ein Viertel der Reihe erreicht ist, "
                "und den Wert in der Mitte zwischen dem 2. und dem 3. Wert nehmen. Wie groß ist Q₁?",
        "c": "(2 + 4) // 2", "erwartet": 3,
        "h": "Beide Wege müssen denselben Wert ergeben.",
        "w": "Weg A: Der Median ist 7. Die untere Hälfte ist 1; 2; 4; 5, ihr Median ist (2 + 4) : 2 = 3. "
             "Weg B: Zwischen dem 2. Wert (2) und dem 3. Wert (4) liegt die Mitte 3. "
             "Beide Wege geben hier 3.",
        "fehlbilder": [{"antwort": 4, "rechnung": "4", "beschreibung": "den dritten Wert genommen statt die Mitte zwischen zweitem und drittem"},
                       {"antwort": 2, "rechnung": "2", "beschreibung": "den zweiten Wert als Q₁ genommen"}],
    },
    {
        "k": "K7-V084", "karte": "quartile", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Bei einem Datensatz ist Q₁ = 14, und die Box eines Boxplots ist 12 Einheiten breit. "
                "Wie groß ist Q₃?",
        "c": "14 + 12", "erwartet": 26,
        "h": "Was misst die Breite der Box?",
        "w": "Die Breite der Box ist Q₃ − Q₁. Also ist Q₃ = 14 + 12 = 26.",
        "fehlbilder": [{"antwort": 2, "rechnung": "14 - 12", "beschreibung": "die Breite abgezogen statt dazugezählt"},
                       {"antwort": 12, "rechnung": "12", "beschreibung": "die Breite als Q₃ genannt"}],
    },
    # ---------------- boxplot ----------------
    {
        "k": "K7-V085", "karte": "boxplot", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Ein Boxplot zeigt: kleinster Wert 8, Q₁ = 16, Median 22, Q₃ = 30, größter Wert 40. "
                "Die Box ist ① Einheiten breit. Der ganze Boxplot (von ganz links bis ganz rechts) ist ② Einheiten lang. "
                "Die beiden Antennen zusammen sind ③ Einheiten lang.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["30 - 16", "40 - 8", "L2 - L1"], "erwartet": [14, 32, 18], "entscheidend": 3,
        "h": "Ziehe jeweils die beiden Randwerte voneinander ab.",
        "w": "Die Box ist 30 − 16 = 14 breit, der ganze Boxplot 40 − 8 = 32 lang. Für die Antennen bleibt 32 − 14 = 18: "
             "links 16 − 8 = 8, rechts 40 − 30 = 10.",
        "fehlbilder": [{"luecke": 3, "antwort": 10, "rechnung": "40 - 30", "beschreibung": "nur die rechte Antenne gerechnet"},
                       {"luecke": 3, "antwort": 46, "rechnung": "L2 + L1", "beschreibung": "Box und Gesamtlänge addiert statt abgezogen"}],
    },
    {
        "k": "K7-V086", "karte": "boxplot", "typ": "BR", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "In einem Boxplot liegt der Median bei 23 und Q₃ bei 30. Welcher Satz passt dazu?",
        "a": ["Etwa drei Viertel der Werte sind höchstens 30.",
              "Etwa drei Viertel der Werte sind höchstens 23.",
              "Genau 30 Werte liegen in der Box.",
              "Der größte Wert ist 30."],
        "richtig": 0,
        "h": "Was bedeutet die Lage von Q₃?",
        "w": "Links von Q₃ liegen drei Viertel der Werte, also sind etwa 75 % höchstens 30. "
             "Links vom Median liegt die Hälfte.",
        "fehlbilder": [
            {"index": 1, "antwort": "Etwa drei Viertel der Werte sind höchstens 23.", "beschreibung": "am Median liegt die Hälfte, nicht drei Viertel"},
            {"index": 2, "antwort": "Genau 30 Werte liegen in der Box.", "beschreibung": "30 ist ein Messwert, keine Anzahl"},
            {"index": 3, "antwort": "Der größte Wert ist 30.", "beschreibung": "rechts von Q₃ geht die Antenne noch weiter"},
        ],
    },
    {
        "k": "K7-V087", "karte": "boxplot", "typ": "AN", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Ein Boxplot zeigt die Wartezeiten von 40 Personen. Q₃ liegt bei 25 Minuten. "
                "Wie viele Personen haben etwa länger als 25 Minuten gewartet?",
        "c": "40 // 4", "erwartet": 10, "einheit": "Personen",
        "h": "Welcher Anteil der Werte liegt rechts von Q₃?",
        "w": "Rechts von Q₃ liegt ein Viertel der Daten: 40 : 4 = 10 Personen.",
        "fehlbilder": [{"antwort": 20, "rechnung": "40 // 2", "beschreibung": "die Hälfte genommen, das gilt für den Median"},
                       {"antwort": 25, "rechnung": "25", "beschreibung": "die Wartezeit als Anzahl genommen"}],
    },
    # ---------------- vergleichen ----------------
    {
        "k": "K7-V088", "karte": "vergleichen", "typ": "VW", "s": 1, "y": "auswahl", "regel": KZ,
        "text": "Zwei Klassen haben Laufzeiten gemessen, beide Boxplots liegen vor. Du sollst sagen, welche Klasse "
                "in der Mitte schneller ist. Welches Vorgehen passt?",
        "a": ["die Mediane der beiden Boxplots vergleichen",
              "die Spannweiten vergleichen",
              "die längsten Antennen vergleichen",
              "die Anzahl der Kinder vergleichen"],
        "richtig": 0,
        "h": "Lies noch einmal, was genau verglichen werden soll.",
        "w": "Die Mitte beschreibt der Median. Spannweite und Antennen zeigen die Streuung; die Anzahl der Kinder "
             "sagt über die Zeiten nichts.",
        "fehlbilder": [
            {"index": 1, "antwort": "die Spannweiten vergleichen", "beschreibung": "die Spannweite beschreibt die Streuung"},
            {"index": 2, "antwort": "die längsten Antennen vergleichen", "beschreibung": "Antennen zeigen die äußeren Viertel, nicht die Mitte"},
            {"index": 3, "antwort": "die Anzahl der Kinder vergleichen", "beschreibung": "ein Boxplot zeigt die Anzahl gar nicht"},
        ],
    },
    {
        "k": "K7-V089", "karte": "vergleichen", "typ": "AN", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Klasse A hat den Median 24 s, ihre Box reicht von 22 s bis 26 s. Klasse B hat den Median 22 s, "
                "ihre Box reicht von 18 s bis 27 s. Um wie viele Sekunden ist die Box von B breiter als die von A?",
        "c": "(27 - 18) - (26 - 22)", "erwartet": 5, "einheit": "s",
        "h": "Rechne beide Boxbreiten einzeln aus.",
        "w": "Box A: 26 − 22 = 4 s. Box B: 27 − 18 = 9 s. 9 − 4 = 5 s: in B streuen die Zeiten mehr.",
        "fehlbilder": [{"antwort": 9, "rechnung": "27 - 18", "beschreibung": "nur die Box von B gerechnet"},
                       {"antwort": 2, "rechnung": "24 - 22", "beschreibung": "die Mediane verglichen"}],
    },
    {
        "k": "K7-V090", "karte": "vergleichen", "typ": "FD", "s": 3, "y": "auswahl", "regel": KZ,
        "text": "Ein Kind vergleicht zwei Boxplots. Zeile 1: Klasse A hat die Spannweite 20, Klasse B die "
                "Spannweite 12. Zeile 2: Gemessen an der Spannweite streuen die Werte bei A also stärker. "
                "Zeile 3: Deshalb hat Klasse A mehr Kinder als Klasse B. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Sagt eine Spannweite etwas über die Anzahl der Kinder?",
        "w": "Zeile 1 und 2 stimmen. Die Spannweite zeigt nur, wie weit die Werte auseinanderliegen. "
             "Über die Anzahl der Kinder sagt ein Boxplot nichts.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile liest nur ab"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: größere Spannweite heißt mehr Streuung"},
        ],
    },
]
