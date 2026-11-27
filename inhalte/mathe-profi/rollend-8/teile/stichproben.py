"""daten.stichproben (Klasse 7 Realschule): 5 Lernkarten, 15 Aufgaben in neuer Form."""
STAND = "2026-11-27"
TITEL = "Stichproben"
PASST_NICHT = ()

TG = "id.daten.teil_ganzes"

AUFGABEN = [
    # ---------------- begriffe ----------------
    {
        "k": "K7-V091", "karte": "begriffe", "typ": "LW", "s": 1, "y": "luecken", "regel": TG,
        "text": "Eine Schule hat 480 Kinder. Für eine Umfrage wird jedes achte Kind befragt. "
                "Der Stichprobenumfang ist n = 480 : 8 = ①. Nicht befragt werden 480 − ① = ② Kinder.",
        "schablone": "① = □; ② = □",
        "c": ["480 // 8", "480 - 480 // 8"], "erwartet": [60, 420],
        "h": "Teile die Gesamtzahl durch 8.",
        "w": "480 : 8 = 60 befragte Kinder, das ist die Stichprobe. Die Grundgesamtheit sind alle 480 Kinder; "
             "420 werden nicht befragt.",
        "fehlbilder": [{"luecke": 2, "antwort": 60, "beschreibung": "die Stichprobe noch einmal genannt"}],
    },
    {
        "k": "K7-V092", "karte": "begriffe", "typ": "UM", "s": 2, "y": "zahl", "regel": TG,
        "text": "Bei einer Umfrage ist der Stichprobenumfang n = 45. Das ist genau ein Fünftel der "
                "Grundgesamtheit. Wie groß ist die Grundgesamtheit?",
        "c": "45 * 5", "erwartet": 225, "einheit": "Personen",
        "h": "Die Stichprobe ist ein Fünftel, die Grundgesamtheit sind fünf Fünftel.",
        "w": "45 · 5 = 225. Die Grundgesamtheit umfasst 225 Personen, befragt wurden 45 davon.",
        "fehlbilder": [{"antwort": 9, "beschreibung": "durch 5 geteilt statt malgenommen"},
                       {"antwort": 180, "beschreibung": "nur die nicht Befragten gerechnet"}],
    },
    {
        "k": "K7-V093", "karte": "begriffe", "typ": "BR", "s": 2, "y": "auswahl", "regel": TG,
        "text": "Ein Satz lautet: „Alle 1 200 Mitglieder des Vereins wurden befragt.“ "
                "Wie heißt das mit den Fachwörtern?",
        "a": ["eine Vollerhebung",
              "eine Stichprobe aus der Grundgesamtheit",
              "eine repräsentative Stichprobe von 1 200 aus mehr Mitgliedern",
              "eine Hochrechnung auf 1 200 Mitglieder"],
        "richtig": 0,
        "h": "Was heißt es, wenn niemand ausgelassen wird?",
        "w": "Wird die ganze Grundgesamtheit befragt, ist das eine Vollerhebung. Eine Stichprobe ist immer nur "
             "ein Teil, und hochgerechnet werden muss dann nichts mehr.",
        "fehlbilder": [
            {"index": 1, "antwort": "eine Stichprobe aus der Grundgesamtheit", "beschreibung": "eine Stichprobe lässt immer einen Teil aus"},
            {"index": 2, "antwort": "eine repräsentative Stichprobe von 1 200 aus mehr Mitgliedern", "beschreibung": "es gibt keine weiteren Mitglieder"},
            {"index": 3, "antwort": "eine Hochrechnung auf 1 200 Mitglieder", "beschreibung": "wer alle befragt, muss nicht hochrechnen"},
        ],
    },
    # ---------------- hochrechnen ----------------
    {
        "k": "K7-V094", "karte": "hochrechnen", "typ": "LW", "s": 1, "y": "luecken", "regel": TG,
        "text": "In einer Stichprobe von 60 Kindern fahren 24 mit dem Rad. Auf 100 Kinder gerechnet sind das "
                "24 · 100 : 60 = ① Prozent. Bei 850 Kindern schätzt man ① · 850 : 100 = ② Kinder.",
        "schablone": "① = □; ② = □",
        "c": ["24 * 100 // 60", "(24 * 100 // 60) * 850 // 100"], "erwartet": [40, 340],
        "h": "Erst den Anteil in Prozent, dann auf die große Gruppe anwenden.",
        "w": "24 : 60 = 0,4, also 40 %. 40 % von 850 sind 340 Kinder. Das Ergebnis ist eine Schätzung.",
        "fehlbilder": [{"luecke": 2, "antwort": 20400, "beschreibung": "die Zahl der Stichprobe mal die Grundgesamtheit genommen"}],
    },
    {
        "k": "K7-V095", "karte": "hochrechnen", "typ": "ZW", "s": 2, "y": "zahl", "regel": TG,
        "text": "In einer Stichprobe von 50 Personen sind 12 Linkshänder, die Grundgesamtheit hat 900 Personen. "
                "Weg A: den Anteil 12 : 50 = 0,24 bilden und mit 900 malnehmen. "
                "Weg B: 900 : 50 = 18 rechnen, die Grundgesamtheit ist also 18-mal so groß, dann 12 · 18. "
                "Wie viele Linkshänder schätzt man?",
        "c": "12 * (900 // 50)", "erwartet": 216, "einheit": "Personen",
        "h": "Beide Wege müssen dieselbe Schätzung ergeben.",
        "w": "Weg A: 0,24 · 900 = 216. Weg B: 900 : 50 = 18 und 12 · 18 = 216. Man schätzt etwa 216 Linkshänder.",
        "fehlbilder": [{"antwort": 10800, "beschreibung": "12 mit 900 malgenommen, ohne den Anteil zu bilden"},
                       {"antwort": 18, "beschreibung": "beim Vergrößerungsfaktor stehen geblieben"}],
    },
    {
        "k": "K7-V096", "karte": "hochrechnen", "typ": "AN", "s": 3, "y": "zahl", "regel": TG,
        "text": "Eine Gemeinde mit 7 200 Einwohnern befragt 120 Personen. 45 von ihnen nutzen den Bus. "
                "Wie viele Busnutzer schätzt man in der ganzen Gemeinde?",
        "c": "45 * 7200 // 120", "erwartet": 2700, "einheit": "Einwohner",
        "h": "Erst den Anteil der Stichprobe, dann auf alle Einwohner hochrechnen.",
        "w": "45 : 120 = 0,375, also 37,5 %. 0,375 · 7 200 = 2 700 Einwohner. Das ist eine Schätzung.",
        "fehlbilder": [{"antwort": 324000, "beschreibung": "45 mit 7 200 malgenommen, ohne den Anteil zu bilden"},
                       {"antwort": 60, "beschreibung": "die Gemeinde durch die Stichprobe geteilt"}],
    },
    # ---------------- repraesentativ ----------------
    {
        "k": "K7-V097", "karte": "repraesentativ", "typ": "BR", "s": 2, "y": "auswahl", "regel": TG,
        "text": "Ein Satz lautet: „Die Stichprobe ist repräsentativ.“ Was muss dafür gelten?",
        "a": ["Sie ist zufällig ausgewählt und groß genug.",
              "Sie ist vor allem möglichst groß.",
              "Sie besteht aus Freiwilligen.",
              "Sie enthält nur Personen, die sich für das Thema interessieren."],
        "richtig": 0,
        "h": "Zwei Bedingungen müssen zusammen gelten.",
        "w": "Repräsentativ heißt: zufällig ausgewählt und groß genug. Größe allein genügt nicht, "
             "und Freiwillige sind eine einseitige Auswahl.",
        "fehlbilder": [
            {"index": 1, "antwort": "Sie ist vor allem möglichst groß.", "beschreibung": "auch eine große Stichprobe kann einseitig sein"},
            {"index": 2, "antwort": "Sie besteht aus Freiwilligen.", "beschreibung": "Freiwillige haben meist eine starke Meinung"},
            {"index": 3, "antwort": "Sie enthält nur Personen, die sich für das Thema interessieren.", "beschreibung": "das ist gerade die einseitige Auswahl"},
        ],
    },
    {
        "k": "K7-V098", "karte": "repraesentativ", "typ": "VW", "s": 2, "y": "auswahl", "regel": TG,
        "text": "Du willst wissen, wie viele Kinder einer Schule ein Instrument spielen. "
                "Welches Vorgehen gibt die beste Stichprobe?",
        "a": ["in jeder Klasse einige Kinder zufällig auswählen",
              "alle Kinder des Schulorchesters befragen",
              "nur die Kinder befragen, die freiwillig antworten wollen",
              "die ersten 20 Kinder vor dem Musikraum befragen"],
        "richtig": 0,
        "h": "Woher kommt eine einseitige Auswahl?",
        "w": "Nur die zufällige Auswahl über alle Klassen ist repräsentativ. Orchester und Musikraum liefern zu "
             "viele musizierende Kinder, und Freiwillige haben meist eine starke Meinung.",
        "fehlbilder": [
            {"index": 1, "antwort": "alle Kinder des Schulorchesters befragen", "beschreibung": "dort spielen fast alle ein Instrument"},
            {"index": 2, "antwort": "nur die Kinder befragen, die freiwillig antworten wollen", "beschreibung": "Freiwillige sind keine zufällige Auswahl"},
            {"index": 3, "antwort": "die ersten 20 Kinder vor dem Musikraum befragen", "beschreibung": "am Musikraum sind Musizierende zu stark vertreten"},
        ],
    },
    {
        "k": "K7-V099", "karte": "repraesentativ", "typ": "FD", "s": 3, "y": "auswahl", "regel": TG,
        "text": "Ein Kind beurteilt eine Umfrage. Zeile 1: Es wurden 500 Personen befragt. "
                "Zeile 2: Alle 500 waren Mitglieder eines Sportvereins. "
                "Zeile 3: Weil 500 viele sind, ist die Umfrage repräsentativ. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Genügt eine große Zahl allein?",
        "w": "Zeile 1 und 2 beschreiben nur die Stichprobe. Sie ist einseitig: Vereinsmitglieder treiben fast alle "
             "Sport. Auch 500 Befragte helfen dann nicht.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile nennt nur den Umfang"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile beschreibt die Auswahl richtig"},
        ],
    },
    # ---------------- fehlerquellen ----------------
    {
        "k": "K7-V100", "karte": "fehlerquellen", "typ": "VW", "s": 2, "y": "auswahl", "regel": TG,
        "text": "Eine Frage lautet: „Finden Sie nicht auch, dass der Pausenhof dringend erneuert werden muss?“ "
                "Wie sollte man stattdessen fragen?",
        "a": ["„Soll der Pausenhof erneuert werden?“",
              "„Warum muss der Pausenhof erneuert werden?“",
              "„Sind Sie gegen eine Erneuerung, obwohl alle dafür sind?“",
              "„Wie dringend ist die Erneuerung des Pausenhofs?“"],
        "richtig": 0,
        "h": "Eine neutrale Frage legt keine Antwort nahe.",
        "w": "Neutral ist die offene Form: „Soll der Pausenhof erneuert werden?“ Die anderen Formulierungen "
             "setzen die Erneuerung schon voraus oder drängen zu einer Antwort.",
        "fehlbilder": [
            {"index": 1, "antwort": "„Warum muss der Pausenhof erneuert werden?“", "beschreibung": "setzt voraus, dass er erneuert werden muss"},
            {"index": 2, "antwort": "„Sind Sie gegen eine Erneuerung, obwohl alle dafür sind?“", "beschreibung": "setzt die Befragten unter Druck"},
            {"index": 3, "antwort": "„Wie dringend ist die Erneuerung des Pausenhofs?“", "beschreibung": "lässt die Antwort „gar nicht nötig“ nicht zu"},
        ],
    },
    {
        "k": "K7-V101", "karte": "fehlerquellen", "typ": "AN", "s": 2, "y": "zahl", "regel": TG,
        "text": "Bei einer Online-Abstimmung stimmen 8 400 von 12 000 Teilnehmenden mit Ja. "
                "Wie viel Prozent sind das?",
        "c": "8400 * 100 // 12000", "erwartet": 70, "einheit": "%",
        "h": "Anteil bilden und mit 100 malnehmen.",
        "w": "8 400 : 12 000 = 0,7, also 70 %. Aussagekräftig ist die Zahl trotzdem nicht: es haben nur "
             "Freiwillige abgestimmt, und die haben meist eine starke Meinung.",
        "fehlbilder": [{"antwort": 30, "beschreibung": "den Anteil der Nein-Stimmen gerechnet"},
                       {"antwort": 7, "beschreibung": "beim Anteil 0,7 das Prozentzeichen verrutscht"}],
    },
    {
        "k": "K7-V102", "karte": "fehlerquellen", "typ": "FD", "s": 3, "y": "auswahl", "regel": TG,
        "text": "Ein Kind prüft eine Umfrage. Zeile 1: Die Frage war neutral gestellt. "
                "Zeile 2: Angeschrieben wurden 300 zufällig ausgewählte Personen. "
                "Zeile 3: Geantwortet haben nur die 40 Personen, die Lust dazu hatten – das Ergebnis ist deshalb "
                "genauso gut. In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Wer antwortet am Ende wirklich?",
        "w": "Zeile 1 und 2 stimmen. Antworten am Ende nur Freiwillige, ist die Auswahl wieder einseitig – "
             "auch wenn vorher zufällig ausgewählt wurde.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "eine neutrale Frage ist richtig"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "die zufällige Auswahl ist richtig"},
        ],
    },
    # ---------------- aussagen ----------------
    {
        "k": "K7-V103", "karte": "aussagen", "typ": "ZW", "s": 2, "y": "zahl", "regel": TG,
        "text": "In Stichprobe A mögen 6 von 10 Kindern das Essen, in Stichprobe B 230 von 500. "
                "Weg A: beide Anteile in Prozent umrechnen und voneinander abziehen. "
                "Weg B: 6 von 10 als 300 von 500 schreiben und mit 230 vergleichen. "
                "Um wie viele Prozentpunkte liegt A über B?",
        "c": "6 * 100 // 10 - 230 * 100 // 500", "erwartet": 14, "einheit": "Prozentpunkte",
        "h": "Rechne beide Anteile auf dieselbe Grundlage.",
        "w": "A: 6 : 10 = 60 %. B: 230 : 500 = 46 %. 60 − 46 = 14 Prozentpunkte. "
             "Weg B: 300 gegen 230 von 500 – derselbe Unterschied.",
        "fehlbilder": [{"antwort": 70, "beschreibung": "die Differenz der Anzahlen genommen"},
                       {"antwort": 46, "beschreibung": "nur den Anteil von B genannt"}],
    },
    {
        "k": "K7-V104", "karte": "aussagen", "typ": "AN", "s": 2, "y": "zahl", "regel": TG,
        "text": "Eine Stichprobe von 200 Haushalten ergibt 30 % mit Haustier. Die Gemeinde hat 4 500 Haushalte. "
                "Wie viele Haushalte mit Haustier schätzt man?",
        "c": "30 * 4500 // 100", "erwartet": 1350, "einheit": "Haushalte",
        "h": "Der Anteil der Stichprobe wird auf alle übertragen.",
        "w": "30 % von 4 500 sind 1 350 Haushalte. Weil der Wert aus nur 200 Haushalten geschätzt ist, "
             "kann der wahre Wert davon abweichen.",
        "fehlbilder": [{"antwort": 60, "beschreibung": "30 % von 200 gerechnet"},
                       {"antwort": 135, "beschreibung": "beim Prozentschritt eine Stelle verloren"}],
    },
    {
        "k": "K7-V105", "karte": "aussagen", "typ": "UM", "s": 2, "y": "zahl", "regel": TG,
        "text": "In einer Stichprobe liegt der Anteil bei 40 %. Hochgerechnet ergibt das 360 Personen. "
                "Wie groß ist die Grundgesamtheit?",
        "c": "360 * 100 // 40", "erwartet": 900, "einheit": "Personen",
        "h": "40 % entsprechen 360 Personen; gesucht sind 100 %.",
        "w": "1 % sind 360 : 40 = 9 Personen. 100 % sind 9 · 100 = 900 Personen.",
        "fehlbilder": [{"antwort": 144, "beschreibung": "40 % von 360 gerechnet"},
                       {"antwort": 400, "beschreibung": "den Prozentsatz als Anzahl genommen"}],
    },
]
