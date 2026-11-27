"""daten.boxplot (Klasse 7): 6 Lernkarten, 18 Aufgaben in neuer Form.

Ohne Zeichnungen: Boxplots sind über ihre fünf Kennwerte im Text beschrieben.
"""
STAND = "2026-11-27"
TITEL = "Median, Quartile und Boxplot"
PASST_NICHT = ()

KZ = "id.daten.kennzahl"

AUFGABEN = [
    # ---------------- median ----------------
    {
        "k": "K7-V073", "karte": "median", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Die Werte 10; 3; 15; 6 werden geordnet: 3; 6; 10; 15. Es sind vier Werte, in der Mitte stehen "
                "6 und 10. Der Median ist (6 + 10) : 2 = ①. Die Spannweite ist 15 − 3 = ②.",
        "schablone": "① = □; ② = □",
        "c": ["(6 + 10) // 2", "15 - 3"], "erwartet": [8, 12],
        "h": "Bei gerader Anzahl liegt der Median zwischen den beiden mittleren Werten.",
        "w": "Der Median ist (6 + 10) : 2 = 8. Die Spannweite ist 15 − 3 = 12.",
        "fehlbilder": [{"luecke": 1, "antwort": 10, "beschreibung": "nur den dritten Wert genommen"}],
    },
    {
        "k": "K7-V074", "karte": "median", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Fünf Werte stehen geordnet da: 2; 5; x; 11; 14. Der Median ist um 4 größer als der zweite Wert. "
                "Wie groß ist x?",
        "c": "5 + 4", "erwartet": 9,
        "h": "Bei fünf geordneten Werten ist der dritte der Median.",
        "w": "Der Median ist der dritte Wert, also x. Er ist 5 + 4 = 9. Die Reihenfolge stimmt dann auch: 9 liegt "
             "zwischen 5 und 11.",
        "fehlbilder": [{"antwort": 4, "beschreibung": "nur den Zuschlag genannt"},
                       {"antwort": 11, "beschreibung": "den vierten Wert genommen"}],
    },
    {
        "k": "K7-V075", "karte": "median", "typ": "FD", "s": 3, "y": "auswahl", "regel": KZ,
        "text": "Ein Kind bestimmt den Median von 8; 2; 11; 5; 14. Zeile 1: Der Median ist der mittlere Wert. "
                "Zeile 2: In der Mitte dieser Liste steht die 11, also ist der Median 11. "
                "Zeile 3: Es sind fünf Werte, deshalb gibt es genau einen mittleren Wert. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Was muss vor dem Ablesen passieren?",
        "w": "Zeile 1 und 3 stimmen. Vor dem Ablesen muss man ordnen: 2; 5; 8; 11; 14. Der mittlere Wert ist 8.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, so ist der Median bestimmt"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile ist richtig: bei ungerader Anzahl gibt es einen mittleren Wert"},
        ],
    },
    # ---------------- kennwerte ----------------
    {
        "k": "K7-V076", "karte": "kennwerte", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Fünf Kinder haben 3, 7, 7, 9 und 14 Bücher. Zusammen sind das ① Bücher. "
                "Der Mittelwert ist ① : 5 = ② Bücher.",
        "schablone": "① = □; ② = □",
        "c": ["3 + 7 + 7 + 9 + 14", "(3 + 7 + 7 + 9 + 14) // 5"], "erwartet": [40, 8],
        "h": "Summe durch Anzahl.",
        "w": "3 + 7 + 7 + 9 + 14 = 40 und 40 : 5 = 8 Bücher. Der Modalwert wäre 7, die Spannweite 11.",
        "fehlbilder": [{"luecke": 2, "antwort": 7, "beschreibung": "den häufigsten Wert als Mittelwert genommen"}],
    },
    {
        "k": "K7-V077", "karte": "kennwerte", "typ": "ZW", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Sechs Zeiten sind 21; 25; 19; 30; 25 und 22 Sekunden. Weg A: größten und kleinsten Wert suchen "
                "und voneinander abziehen. Weg B: alle Werte ordnen und die beiden Randwerte vergleichen. "
                "Wie groß ist die Spannweite?",
        "c": "30 - 19", "erwartet": 11, "einheit": "s",
        "h": "Die Spannweite ist der Abstand zwischen größtem und kleinstem Wert.",
        "w": "Der größte Wert ist 30 s, der kleinste 19 s: 30 − 19 = 11 s. Beide Wege führen zu denselben Randwerten.",
        "fehlbilder": [{"antwort": 30, "beschreibung": "den größten Wert genannt"},
                       {"antwort": 25, "beschreibung": "den häufigsten Wert genannt"}],
    },
    {
        "k": "K7-V078", "karte": "kennwerte", "typ": "AN", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Ein Verein notiert an sechs Tagen die Besucherzahlen 24, 30, 24, 31, 24 und 29. "
                "Um wie viel liegt der Mittelwert über dem häufigsten Wert?",
        "c": "(24 * 3 + 30 + 31 + 29) // 6 - 24", "erwartet": 3,
        "h": "Rechne erst den Mittelwert, dann suche den häufigsten Wert.",
        "w": "Die Summe ist 162, der Mittelwert 162 : 6 = 27. Der häufigste Wert ist 24 (dreimal). "
             "27 − 24 = 3.",
        "fehlbilder": [{"antwort": 27, "beschreibung": "den Mittelwert genannt"},
                       {"antwort": 7, "beschreibung": "die Spannweite genommen"}],
    },
    # ---------------- mittel_median ----------------
    {
        "k": "K7-V079", "karte": "mittel_median", "typ": "BR", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "Ein Satz lautet: „Bei diesen Daten beschreibt der Median die Mitte besser als der Mittelwert.“ "
                "Welche Lage passt dazu?",
        "a": ["Ein einzelner sehr großer Wert zieht den Mittelwert nach oben.",
              "Alle Werte liegen dicht beieinander.",
              "Es gibt genau zwei verschiedene Werte.",
              "Die Anzahl der Werte ist gerade."],
        "richtig": 0,
        "h": "Welcher der beiden Kennwerte reagiert stark auf einen Ausreißer?",
        "w": "Ein Ausreißer zieht den Mittelwert zu sich, der Median bleibt in der Mitte der geordneten Liste. "
             "Liegen alle Werte dicht beieinander, sind beide Kennwerte ähnlich.",
        "fehlbilder": [
            {"index": 1, "antwort": "Alle Werte liegen dicht beieinander.", "beschreibung": "dann sind Median und Mittelwert fast gleich"},
            {"index": 2, "antwort": "Es gibt genau zwei verschiedene Werte.", "beschreibung": "die Zahl der verschiedenen Werte entscheidet nicht"},
            {"index": 3, "antwort": "Die Anzahl der Werte ist gerade.", "beschreibung": "das ändert nur die Berechnung des Medians, nicht seine Aussagekraft"},
        ],
    },
    {
        "k": "K7-V080", "karte": "mittel_median", "typ": "VW", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "In einer Gruppe verdienen fünf Personen 1 800 €, 1 900 €, 2 000 €, 2 100 € und 12 000 €. "
                "Du sollst den typischen Verdienst angeben. Welches Vorgehen passt?",
        "a": ["den Median nehmen, weil ein Ausreißer dabei ist",
              "den Mittelwert nehmen, weil er alle Werte benutzt",
              "die Spannweite nehmen",
              "den größten Wert nehmen"],
        "richtig": 0,
        "h": "Schau, ob ein Wert weit außerhalb der anderen liegt.",
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
                "Zeile 1: Der Mittelwert ist 145 : 5 = 29. Zeile 2: Der Median ist 11. "
                "Zeile 3: Also liegen die meisten Werte bei etwa 29. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Zähle, wie viele Werte wirklich in der Nähe von 29 liegen.",
        "w": "Zeile 1 und 2 stimmen. Vier der fünf Werte liegen zwischen 8 und 14. Der Mittelwert 29 entsteht nur "
             "durch den Ausreißer 101; die meisten Werte liegen bei etwa 11.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: die Summe ist 145"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: der dritte von fünf Werten ist 11"},
        ],
    },
    # ---------------- quartile ----------------
    {
        "k": "K7-V082", "karte": "quartile", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Acht Werte stehen geordnet da: 2; 4; 8; 10; 12; 14; 18; 20. Die untere Hälfte ist 2; 4; 8; 10, "
                "ihr Median ist Q₁ = (4 + 8) : 2 = ①. Die obere Hälfte ist 12; 14; 18; 20, "
                "ihr Median ist Q₃ = (14 + 18) : 2 = ②.",
        "schablone": "① = □; ② = □",
        "c": ["(4 + 8) // 2", "(14 + 18) // 2"], "erwartet": [6, 16],
        "h": "Q₁ und Q₃ sind die Mediane der beiden Hälften.",
        "w": "Q₁ = (4 + 8) : 2 = 6 und Q₃ = (14 + 18) : 2 = 16. Zwischen beiden liegt die mittlere Hälfte der Werte.",
        "fehlbilder": [{"luecke": 1, "antwort": 4, "beschreibung": "den zweiten Wert genommen statt den Median der Hälfte"}],
    },
    {
        "k": "K7-V083", "karte": "quartile", "typ": "ZW", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Neun Werte stehen geordnet da: 1; 2; 4; 5; 7; 8; 10; 11; 15. "
                "Weg A: den Median streichen und von der unteren Hälfte den Median nehmen. "
                "Weg B: die vier kleinsten Werte nehmen und deren Median bilden. Wie groß ist Q₁?",
        "c": "(2 + 4) // 2", "erwartet": 3,
        "h": "Bei ungerader Anzahl gehört der Median zu keiner der beiden Hälften.",
        "w": "Der Median ist 7. Die untere Hälfte ist 1; 2; 4; 5, ihr Median ist (2 + 4) : 2 = 3. "
             "Beide Wege nehmen dieselben vier Werte.",
        "fehlbilder": [{"antwort": 4, "beschreibung": "einen der mittleren Werte genommen statt ihres Mittels"},
                       {"antwort": 2, "beschreibung": "den zweiten Wert als Q₁ genommen"}],
    },
    {
        "k": "K7-V084", "karte": "quartile", "typ": "UM", "s": 2, "y": "zahl", "regel": KZ,
        "text": "Bei einem Datensatz ist Q₁ = 14, und die Box eines Boxplots ist 12 Einheiten breit. "
                "Wie groß ist Q₃?",
        "c": "14 + 12", "erwartet": 26,
        "h": "Die Box reicht von Q₁ bis Q₃.",
        "w": "Die Breite der Box ist Q₃ − Q₁. Also ist Q₃ = 14 + 12 = 26.",
        "fehlbilder": [{"antwort": 2, "beschreibung": "die Breite abgezogen statt dazugezählt"},
                       {"antwort": 12, "beschreibung": "die Breite als Q₃ genannt"}],
    },
    # ---------------- boxplot ----------------
    {
        "k": "K7-V085", "karte": "boxplot", "typ": "LW", "s": 1, "y": "luecken", "regel": KZ,
        "text": "Ein Boxplot zeigt: kleinster Wert 8, Q₁ = 16, Median 22, Q₃ = 30, größter Wert 40. "
                "Die Box reicht von 16 bis 30, ist also ① Einheiten breit. "
                "Die rechte Antenne reicht von 30 bis 40, ist also ② Einheiten lang.",
        "schablone": "① = □; ② = □",
        "c": ["30 - 16", "40 - 30"], "erwartet": [14, 10],
        "h": "Ziehe jeweils die beiden Randwerte voneinander ab.",
        "w": "Die Box ist 30 − 16 = 14 breit, die rechte Antenne 40 − 30 = 10 lang. In der Box liegt die mittlere "
             "Hälfte der Werte, in der Antenne ein Viertel.",
        "fehlbilder": [{"luecke": 2, "antwort": 32, "beschreibung": "von 8 bis 40 gerechnet, das ist die Spannweite"}],
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
        "k": "K7-V087", "karte": "boxplot", "typ": "AN", "s": 3, "y": "zahl", "regel": KZ,
        "text": "Ein Boxplot zeigt die Wartezeiten von 40 Personen. Q₃ liegt bei 25 Minuten. "
                "Wie viele Personen haben etwa länger als 25 Minuten gewartet?",
        "c": "40 // 4", "erwartet": 10, "einheit": "Personen",
        "h": "Rechts von Q₃ liegt ein Viertel der Werte.",
        "w": "Rechts von Q₃ liegt ein Viertel der Daten: 40 : 4 = 10 Personen.",
        "fehlbilder": [{"antwort": 20, "beschreibung": "die Hälfte genommen, das gilt für den Median"},
                       {"antwort": 25, "beschreibung": "die Wartezeit als Anzahl genommen"}],
    },
    # ---------------- vergleichen ----------------
    {
        "k": "K7-V088", "karte": "vergleichen", "typ": "VW", "s": 2, "y": "auswahl", "regel": KZ,
        "text": "Zwei Klassen haben Laufzeiten gemessen, beide Boxplots liegen vor. Du sollst sagen, welche Klasse "
                "in der Mitte schneller ist. Welches Vorgehen passt?",
        "a": ["die Mediane der beiden Boxplots vergleichen",
              "die Spannweiten vergleichen",
              "die längsten Antennen vergleichen",
              "die Anzahl der Kinder vergleichen"],
        "richtig": 0,
        "h": "Welcher Kennwert beschreibt die Mitte?",
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
        "fehlbilder": [{"antwort": 9, "beschreibung": "nur die Box von B gerechnet"},
                       {"antwort": 2, "beschreibung": "die Mediane verglichen"}],
    },
    {
        "k": "K7-V090", "karte": "vergleichen", "typ": "FD", "s": 3, "y": "auswahl", "regel": KZ,
        "text": "Ein Kind vergleicht zwei Boxplots. Zeile 1: Klasse A hat die Spannweite 20, Klasse B die "
                "Spannweite 12. Zeile 2: Bei A streuen die Werte also stärker. "
                "Zeile 3: Deshalb hat Klasse A mehr Kinder als Klasse B. "
                "In welcher Zeile steckt der Fehler?",
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
