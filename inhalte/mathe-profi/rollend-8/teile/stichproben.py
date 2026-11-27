"""daten.stichproben (Klasse 7 Realschule): 5 Lernkarten, 15 Aufgaben in neuer Form.
Feldbedeutung (c mit L1, L2 …, entscheidend, rechnung, a_rechnung): siehe Kopf von teile/zinsen.py.
"""
STAND = "2026-11-27"
TITEL = "Stichproben"
PASST_NICHT = ()

TG = "id.daten.teil_ganzes"

AUFGABEN = [
    # ---------------- begriffe ----------------
    {
        "k": "K7-V091", "karte": "begriffe", "typ": "LW", "s": 1, "y": "luecken", "regel": TG,
        "text": "Eine Schule hat 480 Kinder. Für eine Umfrage wird jedes achte Kind befragt. "
                "Der Stichprobenumfang ist n = ①. Nicht befragt werden ② Kinder.",
        "schablone": "① = □; ② = □",
        "c": ["480 // 8", "480 - L1"], "erwartet": [60, 420], "entscheidend": 1,
        "h": "Jedes achte Kind: Wie oft passt 8 in die Gesamtzahl?",
        "w": "480 : 8 = 60 befragte Kinder, das ist die Stichprobe. Die Grundgesamtheit sind alle 480 Kinder; "
             "480 − 60 = 420 werden nicht befragt.",
        "fehlbilder": [{"luecke": 1, "antwort": 8, "rechnung": "8", "beschreibung": "den Abstand „jedes achte“ als Stichprobenumfang genommen"},
                       {"luecke": 2, "antwort": 60, "rechnung": "L1", "beschreibung": "die Stichprobe noch einmal genannt"}],
    },
    {
        "k": "K7-V092", "karte": "begriffe", "typ": "UM", "s": 2, "y": "zahl", "regel": TG,
        "text": "Bei einer Umfrage ist der Stichprobenumfang n = 45. Das ist genau ein Fünftel der "
                "Grundgesamtheit. Wie groß ist die Grundgesamtheit?",
        "c": "45 * 5", "erwartet": 225, "einheit": "Personen",
        "h": "Wie viele Stichproben dieser Größe passen in die ganze Gruppe?",
        "w": "45 · 5 = 225. Die Grundgesamtheit umfasst 225 Personen, befragt wurden 45 davon.",
        "fehlbilder": [{"antwort": 9, "rechnung": "45 // 5", "beschreibung": "durch 5 geteilt statt malgenommen"},
                       {"antwort": 180, "rechnung": "45 * 4", "beschreibung": "nur die nicht Befragten gerechnet"}],
    },
    {
        "k": "K7-V093", "karte": "begriffe", "typ": "BR", "s": 2, "y": "auswahl", "regel": TG,
        "text": "Ein Bericht schreibt kurz: n = 60 und N = 480 (n ist der Stichprobenumfang, N die Größe der Grundgesamtheit). "
                "Welcher Satz sagt dasselbe?",
        "a": ["Aus 480 Personen wurden 60 ausgewählt und befragt.",
              "Aus 60 Personen wurden 480 ausgewählt und befragt.",
              "Es wurden 60 % von 480 Personen befragt.",
              "Alle 480 Personen wurden befragt."],
        "richtig": 0,
        "h": "Lies nach, was n und was N bedeutet.",
        "w": "N = 480 ist die Grundgesamtheit, n = 60 die Stichprobe: aus 480 Personen wurden 60 befragt. "
             "60 % von 480 wären 288 Personen, und bei einer Befragung aller 480 wäre n = 480.",
        "fehlbilder": [
            {"index": 1, "antwort": "Aus 60 Personen wurden 480 ausgewählt und befragt.", "beschreibung": "n und N vertauscht"},
            {"index": 2, "antwort": "Es wurden 60 % von 480 Personen befragt.", "beschreibung": "die Zahl 60 als Prozentsatz gelesen statt als Anzahl"},
            {"index": 3, "antwort": "Alle 480 Personen wurden befragt.", "beschreibung": "eine Vollerhebung hätte n = N"},
        ],
    },
    {
        "k": "K7-V094", "karte": "hochrechnen", "typ": "LW", "s": 1, "y": "luecken", "regel": TG,
        "text": "In einer Stichprobe von 60 Kindern fahren 24 mit dem Rad. Auf 100 Kinder gerechnet sind das "
                "① Prozent. Bei 850 Kindern insgesamt schätzt man ② Radfahrer.",
        "schablone": "① = □; ② = □",
        "c": ["24 * 100 // 60", "L1 * 850 // 100"], "erwartet": [40, 340], "entscheidend": 2,
        "h": "Erst den Anteil in Prozent, dann auf die große Gruppe anwenden.",
        "w": "24 : 60 = 0,4, also 40 %. 40 % von 850 sind 340 Kinder. Das Ergebnis ist eine Schätzung.",
        "fehlbilder": [{"luecke": 2, "antwort": 20400, "rechnung": "24 * 850", "beschreibung": "die 24 Radfahrer mit 850 malgenommen, ohne den Anteil zu bilden"},
                       {"luecke": 2, "antwort": 24, "rechnung": "24", "beschreibung": "die Zahl der Radfahrer aus der Stichprobe übernommen"}],
    },
    {
        "k": "K7-V095", "karte": "hochrechnen", "typ": "ZW", "s": 2, "y": "zahl", "regel": TG,
        "text": "In einer Stichprobe von 50 zufällig ausgewählten Personen sind 12 Linkshänder, die Grundgesamtheit hat 900 Personen. "
                "Weg A: den Anteil 12 : 50 = 0,24 bilden und mit 900 malnehmen. "
                "Weg B: 900 : 50 = 18 rechnen, die Grundgesamtheit ist also 18-mal so groß, dann 12 · 18. "
                "Wie viele Linkshänder schätzt man?",
        "c": "12 * (900 // 50)", "erwartet": 216, "einheit": "Personen",
        "h": "Beide Wege müssen dieselbe Schätzung ergeben.",
        "w": "Weg A: 0,24 · 900 = 216. Weg B: 900 : 50 = 18 und 12 · 18 = 216. Man schätzt etwa 216 Linkshänder.",
        "fehlbilder": [{"antwort": 10800, "rechnung": "12 * 900", "beschreibung": "12 mit 900 malgenommen, ohne den Anteil zu bilden"},
                       {"antwort": 18, "rechnung": "900 // 50", "beschreibung": "beim Vergrößerungsfaktor stehen geblieben"}],
    },
    {
        "k": "K7-V096", "karte": "hochrechnen", "typ": "AN", "s": 2, "y": "zahl", "regel": TG,
        "text": "Eine Gemeinde mit 7 200 Einwohnern befragt 120 zufällig ausgewählte Personen. 45 von ihnen nutzen den Bus. "
                "Wie viele Busnutzer schätzt man in der ganzen Gemeinde?",
        "c": "45 * 7200 // 120", "erwartet": 2700, "einheit": "Einwohner",
        "h": "Erst den Anteil der Stichprobe, dann auf alle Einwohner hochrechnen.",
        "w": "45 : 120 = 0,375, also 37,5 %. 0,375 · 7 200 = 2 700 Einwohner. Das ist eine Schätzung.",
        "fehlbilder": [{"antwort": 324000, "rechnung": "45 * 7200", "beschreibung": "45 mit 7 200 malgenommen, ohne den Anteil zu bilden"},
                       {"antwort": 60, "rechnung": "7200 // 120", "beschreibung": "die Gemeinde durch die Stichprobe geteilt"}],
    },
    # ---------------- repraesentativ ----------------
    {
        "k": "K7-V097", "karte": "repraesentativ", "typ": "BR", "s": 2, "y": "auswahl", "regel": TG,
        "text": "Eine Schule hat 1 000 Kinder: 520 Mädchen und 480 Jungen. In einer Stichprobe von 100 Kindern sind "
                "70 Mädchen und 30 Jungen. Was legt der Vergleich der beiden Verteilungen nahe?",
        "a": ["Die Stichprobe bildet die Schule nicht gut ab, sie ist vermutlich nicht repräsentativ.",
              "Die Stichprobe ist sicher repräsentativ, weil mehr Mädchen als Jungen dabei sind.",
              "Die Stichprobe ist repräsentativ, weil 100 eine runde Zahl ist.",
              "Die Schule hat 70 Mädchen."],
        "richtig": 0,
        "h": "Berechne in beiden Fällen den Anteil der Mädchen.",
        "w": "In der Schule sind 52 % Mädchen, in der Stichprobe 70 %. Ein so großer Unterschied spricht dafür, dass die "
             "Auswahl einseitig war. Eine runde Zahl macht eine Stichprobe nicht repräsentativ.",
        "fehlbilder": [
            {"index": 1, "antwort": "Die Stichprobe ist sicher repräsentativ, weil mehr Mädchen als Jungen dabei sind.", "beschreibung": "in der Schule sind auch mehr Mädchen, aber nicht so viele"},
            {"index": 2, "antwort": "Die Stichprobe ist repräsentativ, weil 100 eine runde Zahl ist.", "beschreibung": "die runde Zahl sagt nichts über die Auswahl"},
            {"index": 3, "antwort": "Die Schule hat 70 Mädchen.", "beschreibung": "70 ist der Wert aus der Stichprobe, nicht aus der Schule"},
        ],
    },
    {
        "k": "K7-V098", "karte": "repraesentativ", "typ": "VW", "s": 1, "y": "auswahl", "regel": TG,
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
        "text": "Ein Kind beurteilt eine Umfrage, bei der 500 Mitglieder eines Sportvereins zu ihrer Freizeit befragt wurden. "
                "Zeile 1: Eine Stichprobe ist repräsentativ, wenn sie nur groß genug ist. "
                "Zeile 2: 500 Befragte sind eine große Stichprobe. "
                "Zeile 3: Also ist diese Umfrage repräsentativ für alle Menschen der Stadt. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Genügt eine große Zahl allein?",
        "w": "Zeile 1 ist falsch: Repräsentativ heißt zufällig ausgewählt und groß genug. Vereinsmitglieder treiben fast alle "
             "Sport, die Auswahl ist einseitig. Die Zeilen 2 und 3 folgen richtig aus Zeile 1.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist für sich richtig: 500 ist eine große Zahl"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus den Zeilen 1 und 2"},
        ],
    },
    # ---------------- fehlerquellen ----------------
    {
        "k": "K7-V100", "karte": "fehlerquellen", "typ": "VW", "s": 1, "y": "auswahl", "regel": TG,
        "text": "Eine Frage lautet: „Finden Sie nicht auch, dass der Pausenhof dringend erneuert werden muss?“ "
                "Wie sollte man stattdessen fragen?",
        "a": ["„Soll der Pausenhof erneuert werden?“",
              "„Warum muss der Pausenhof erneuert werden?“",
              "„Sind Sie gegen eine Erneuerung, obwohl alle dafür sind?“",
              "„Wie dringend ist die Erneuerung des Pausenhofs?“"],
        "richtig": 0,
        "h": "Welche Frage setzt nichts voraus?",
        "w": "Neutral ist die Frage ohne Vorannahme: „Soll der Pausenhof erneuert werden?“ Die anderen Formulierungen "
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
                "Wie viel Prozent der Teilnehmenden sind das?",
        "c": "8400 * 100 // 12000", "erwartet": 70, "einheit": "%",
        "h": "Anteil bilden und mit 100 malnehmen.",
        "w": "8 400 : 12 000 = 0,7, also 70 %. Aussagekräftig ist die Zahl trotzdem nicht: es haben nur "
             "Freiwillige abgestimmt, und die haben meist eine starke Meinung.",
        "fehlbilder": [{"antwort": 30, "rechnung": "100 - 70", "beschreibung": "den Anteil der Nein-Stimmen gerechnet"},
                       {"antwort": 7, "rechnung": "8400 // 1200", "beschreibung": "das Komma bei 0,7 falsch verschoben"}],
    },
    {
        "k": "K7-V102", "karte": "fehlerquellen", "typ": "FD", "s": 3, "y": "auswahl", "regel": TG,
        "text": "Ein Kind prüft eine Umfrage. Zeile 1: Die Frage war neutral gestellt. "
                "Zeile 2: Angeschrieben wurden 300 zufällig ausgewählte Personen. "
                "Zeile 3: Geantwortet haben nur die 40 Personen, die Lust dazu hatten – das Ergebnis ist deshalb "
                "genauso gut. In welcher Zeile steckt der erste Fehler?",
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
        "h": "Beide Wege müssen denselben Unterschied zeigen.",
        "w": "A: 6 : 10 = 60 %. B: 230 : 500 = 46 %. 60 − 46 = 14 Prozentpunkte. "
             "Weg B: 300 gegen 230 von 500 – derselbe Unterschied.",
        "fehlbilder": [{"antwort": 70, "rechnung": "300 - 230", "beschreibung": "die Differenz der Anzahlen genommen"},
                       {"antwort": 46, "rechnung": "230 * 100 // 500", "beschreibung": "nur den Anteil von B genannt"}],
    },
    {
        "k": "K7-V104", "karte": "aussagen", "typ": "AN", "s": 2, "y": "zahl", "regel": TG,
        "text": "Eine Stichprobe von 200 Haushalten ergibt 30 % mit Haustier. Die Gemeinde hat 4 500 Haushalte, die Stichprobe gilt als repräsentativ. "
                "Wie viele Haushalte mit Haustier schätzt man?",
        "c": "30 * 4500 // 100", "erwartet": 1350, "einheit": "Haushalte",
        "h": "Der Anteil der Stichprobe wird auf alle übertragen.",
        "w": "30 % von 4 500 sind 1 350 Haushalte. Weil der Wert aus nur 200 Haushalten geschätzt ist, "
             "kann der wahre Wert davon abweichen.",
        "fehlbilder": [{"antwort": 60, "rechnung": "30 * 200 // 100", "beschreibung": "30 % von 200 gerechnet"},
                       {"antwort": 135, "rechnung": "4500 * 3 // 100", "beschreibung": "3 % statt 30 % gerechnet"}],
    },
    {
        "k": "K7-V105", "karte": "aussagen", "typ": "UM", "s": 2, "y": "zahl", "regel": TG,
        "text": "In einer Stichprobe haben 40 % ein Haustier. Hochgerechnet auf die Grundgesamtheit sind das 360 Personen "
                "mit Haustier. Wie groß ist die Grundgesamtheit?",
        "c": "360 * 100 // 40", "erwartet": 900, "einheit": "Personen",
        "h": "40 % entsprechen 360 Personen; gesucht sind 100 %.",
        "w": "1 % sind 360 : 40 = 9 Personen. 100 % sind 9 · 100 = 900 Personen.",
        "fehlbilder": [{"antwort": 144, "rechnung": "360 * 40 // 100", "beschreibung": "40 % von 360 gerechnet"},
                       {"antwort": 14400, "rechnung": "360 * 40", "beschreibung": "360 mit der Prozentzahl 40 malgenommen"}],
    },
]
