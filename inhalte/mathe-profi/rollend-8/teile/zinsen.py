"""finanzen.zinsen (Klasse 7 Realschule / 6 Gymnasium): 8 Lernkarten, 24 Aufgaben in neuer Form.

Mischung je Lernkarte: höchstens ein Lückenweg (Stufe 1, zählt nein), höchstens ein Fehler-Detektiv,
mindestens eine zählende Aufgabe aus Umkehren / Zwei Wege / Brücke / Verfahren wählen / Anwenden.
Alle Lernkarten haben im Bestand eigene Sachaufgaben; „Anwenden" steht deshalb dort, wo es den Stoff
weiterträgt (Monate und Zeitanteil), nicht als Pflichtfüllung.

Felder, die über den ersten Stand hinaus geprüft werden (Selbstprüfung nach den Maßstäben der Gegenprüfung):
  c bei Lückenwegen: Ausdrücke mit L1, L2 … = die schon berechneten früheren Lücken;
  entscheidend: Nummer der Lücke an der entscheidenden Stelle (dazu muss ein Fehlbild existieren);
  rechnung im Fehlbild: Ausdruck, der genau die gespeicherte Fehlantwort ergibt;
  a_rechnung / a_wert bei Auswahl mit Rechnungen: alle Antworten rechnerisch verschieden.
"""
STAND = "2026-11-27"
TITEL = "Zinsen"
PASST_NICHT = ()

P = "id.verhaeltnisse.prozent"

AUFGABEN = [
    # ---------------- begriffe ----------------
    {
        "k": "K7-V001", "karte": "begriffe", "typ": "LW", "s": 1, "y": "luecken", "regel": P,
        "text": "Auf einem Sparkonto liegen 1 500 €. Die Bank zahlt 2 % Zinsen im Jahr. "
                "1 % des Kapitals sind ① €. Die Zinsen für ein Jahr sind ② €. "
                "Mit den Zinsen stehen nach dem Jahr ③ € auf dem Konto.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["1500 // 100", "2 * L1", "1500 + L2"], "erwartet": [15, 30, 1530], "entscheidend": 2,
        "h": "Erst ein Prozent, dann das Vielfache.",
        "w": "1 % von 1 500 € sind 15 €. 2 % sind 2 · 15 € = 30 €. Die Zinsen kommen zum Kapital dazu: 1 500 € + 30 € = 1 530 €.",
        "fehlbilder": [{"luecke": 2, "antwort": 2, "rechnung": "2", "beschreibung": "den Zinssatz als Zinsbetrag in Euro genommen"},
                       {"luecke": 3, "antwort": 1470, "rechnung": "1500 - L2", "beschreibung": "die Zinsen abgezogen statt dazugezählt"}],
    },
    {
        "k": "K7-V002", "karte": "begriffe", "typ": "BR", "s": 2, "y": "auswahl", "regel": P,
        "text": "Ein Konto wird kurz so beschrieben: K = 800 €, p = 5 %, Z = 40 € (Z sind die Zinsen für ein Jahr). "
                "Welcher Satz sagt dasselbe?",
        "a": ["Die Bank zahlt 40 % Zinsen auf 800 €.",
              "Für 800 € bekommt man im Jahr 40 € Zinsen.",
              "Die Bank zahlt im Jahr 5 € Zinsen.",
              "Nach einem Jahr stehen 840 % auf dem Konto."],
        "richtig": 1,
        "h": "Lies nach, welche Größe in Euro steht und welche in Prozent.",
        "w": "K = 800 € ist das Kapital, p = 5 % der Zinssatz, Z = 40 € der Zinsbetrag für ein Jahr. "
             "5 % von 800 € sind wirklich 40 €.",
        "fehlbilder": [
            {"index": 0, "antwort": "Die Bank zahlt 40 % Zinsen auf 800 €.",
             "beschreibung": "den Zinsbetrag als Zinssatz gelesen"},
            {"index": 2, "antwort": "Die Bank zahlt im Jahr 5 € Zinsen.",
             "beschreibung": "den Zinssatz als Betrag in Euro gelesen"},
            {"index": 3, "antwort": "Nach einem Jahr stehen 840 % auf dem Konto.",
             "beschreibung": "Euro und Prozent vertauscht"},
        ],
    },
    {
        "k": "K7-V003", "karte": "begriffe", "typ": "FD", "s": 3, "y": "auswahl", "regel": P,
        "text": "Ein Kind erklärt ein Konto mit K = 2 400 € und p = 3 %. "
                "Zeile 1: Das Kapital ist der Betrag auf dem Konto, also 2 400 €. "
                "Zeile 2: Der Zinssatz 3 % bedeutet, dass es im Jahr 3 € Zinsen gibt. "
                "Zeile 3: Die Zinsen für ein Jahr sind deshalb 3 €. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Prüfe, ob 3 % von 2 400 € wirklich nur 3 € sind.",
        "w": "Zeile 1 stimmt. Zeile 2 ist falsch: 3 % heißt 3 € für je 100 € Kapital. In 2 400 € stecken 24 Hunderter, "
             "also 24 · 3 € = 72 €. Zeile 3 folgt richtig aus Zeile 2, übernimmt aber deren Fehler.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: das Kapital ist der Betrag auf dem Konto"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2; der Fehler steht schon in Zeile 2"},
        ],
    },
    # ---------------- rollen ----------------
    {
        "k": "K7-V004", "karte": "rollen", "typ": "VW", "s": 1, "y": "auswahl", "regel": P,
        "text": "Eine Familie hat einen Kredit über 2 000 € zu 6 % und ein Sparkonto mit 500 € zu 1 %. "
                "Gefragt ist nur, wie viel Zinsen die Familie im Jahr für den Kredit an die Bank zahlen muss. "
                "Welche Rechnung passt?",
        "a": ["2 000 € · 6 : 100 = 120 €",
              "2 000 € · 6 : 100 − 500 € · 1 : 100 = 115 €",
              "500 € · 1 : 100 = 5 €",
              "2 000 € · 6 : 100 + 500 € · 1 : 100 = 125 €"],
        "richtig": 0,
        "a_rechnung": ["2000*6/100", "2000*6/100 - 500*1/100", "500*1/100", "2000*6/100 + 500*1/100"], "a_wert": 120,
        "h": "Zinsen zahlt man nur für geliehenes Geld.",
        "w": "Für den Kredit zahlt die Familie 2 000 € · 6 : 100 = 120 €. Die 5 € vom Sparkonto bekommt sie, "
             "sie zahlt sie nicht. Gefragt ist nur das Gezahlte: 120 €.",
        "fehlbilder": [
            {"index": 1, "antwort": "2 000 € · 6 : 100 − 500 € · 1 : 100 = 115 €",
             "beschreibung": "bekommene Zinsen von gezahlten abgezogen, obwohl nur das Gezahlte gefragt ist"},
            {"index": 2, "antwort": "500 € · 1 : 100 = 5 €",
             "beschreibung": "das Sparkonto genommen, bei dem man Zinsen bekommt"},
            {"index": 3, "antwort": "2 000 € · 6 : 100 + 500 € · 1 : 100 = 125 €",
             "beschreibung": "alle Zinsen zusammengezählt, ohne auf „zahlen“ und „bekommen“ zu achten"},
        ],
    },
    {
        "k": "K7-V005", "karte": "rollen", "typ": "UM", "s": 2, "y": "auswahl", "regel": P,
        "text": "Am Ende eines Jahres sind einer Person 18 € Zinsen gutgeschrieben worden. "
                "Sie hat die Zinsen also bekommen. Welche Lage passt dazu?",
        "a": ["Sie hat Geld verzinst angelegt.",
              "Sie hat einen Kredit aufgenommen.",
              "Sie hat Geld in einer Spardose.",
              "Sie hat Geld verliehen, ohne Zinsen zu verlangen."],
        "richtig": 0,
        "h": "Wer zahlt hier die Zinsen, und wer bekommt sie?",
        "w": "Gutgeschriebene Zinsen bekommt man. Das passt zum verzinsten Anlegen. Bei einem Kredit zahlt man "
             "Zinsen, in der Spardose und beim zinslosen Verleihen gibt es keine.",
        "fehlbilder": [
            {"index": 1, "antwort": "Sie hat einen Kredit aufgenommen.",
             "beschreibung": "bei einem Kredit zahlt man Zinsen, man bekommt sie nicht"},
            {"index": 2, "antwort": "Sie hat Geld in einer Spardose.",
             "beschreibung": "in der Spardose benutzt niemand das Geld, es gibt keine Zinsen"},
            {"index": 3, "antwort": "Sie hat Geld verliehen, ohne Zinsen zu verlangen.",
             "beschreibung": "ohne Zinssatz gibt es keine Gutschrift"},
        ],
    },
    {
        "k": "K7-V006", "karte": "rollen", "typ": "FD", "s": 3, "y": "auswahl", "regel": P,
        "text": "Ein Kind sagt: Zeile 1: Wer einen Kredit hat, zahlt Zinsen. "
                "Zeile 2: Wer Geld auf einem Sparkonto hat, bekommt Zinsen. "
                "Zeile 3: Wer Geld in einer Spardose hat, bekommt auch Zinsen. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Frage bei jeder Zeile: Wer benutzt das Geld, und wer bezahlt dafür?",
        "w": "Zeile 1 und 2 stimmen. Das Geld in der Spardose benutzt niemand, deshalb gibt es dafür keine Zinsen.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: für geliehenes Geld zahlt man Zinsen"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: die Bank benutzt das Geld und zahlt dafür"},
        ],
    },
    # ---------------- jahreszinsen ----------------
    {
        "k": "K7-V007", "karte": "jahreszinsen", "typ": "LW", "s": 1, "y": "luecken", "regel": P,
        "text": "Ein Kapital von 2 500 € wird mit 3 % verzinst. 1 % des Kapitals sind ① €. "
                "Die Zinsen für ein Jahr sind ② €. Sie werden jedes Jahr abgehoben, das Kapital bleibt gleich. "
                "Nach zwei Jahren hat die Bank insgesamt ③ € Zinsen gezahlt.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["2500 // 100", "3 * L1", "2 * L2"], "erwartet": [25, 75, 150], "entscheidend": 2,
        "h": "Erst ein Prozent, dann das Vielfache.",
        "w": "1 % von 2 500 € sind 25 €. 3 % sind 3 · 25 € = 75 €. Weil die Zinsen abgehoben werden, kommt jedes Jahr "
             "derselbe Betrag: 2 · 75 € = 150 €.",
        "fehlbilder": [{"luecke": 2, "antwort": 3, "rechnung": "3", "beschreibung": "die Prozentzahl als Zinsbetrag genommen"},
                       {"luecke": 3, "antwort": 75, "rechnung": "L2", "beschreibung": "nur ein Jahr gerechnet"}],
    },
    {
        "k": "K7-V008", "karte": "jahreszinsen", "typ": "ZW", "s": 2, "y": "zahl", "regel": P,
        "text": "Ein Kapital von 1 200 € wird mit 6 % verzinst. Weg A: 1 % sind 12 €, davon nimmst du 6-mal. "
                "Weg B: 1 200 · 6 = 7 200, dann durch 100 teilen. Wie hoch sind die Jahreszinsen?",
        "c": "1200 * 6 // 100", "erwartet": 72, "einheit": "€",
        "h": "Beide Wege müssen denselben Betrag ergeben.",
        "w": "Weg A: 6 · 12 € = 72 €. Weg B: 7 200 : 100 = 72 €. Die Jahreszinsen sind 72 €.",
        "fehlbilder": [{"antwort": 7200, "rechnung": "1200 * 6", "beschreibung": "bei Weg B das Teilen durch 100 vergessen"},
                       {"antwort": 12, "rechnung": "1200 / 100", "beschreibung": "beim 1-%-Schritt stehen geblieben"}],
    },
    {
        "k": "K7-V009", "karte": "jahreszinsen", "typ": "FD", "s": 3, "y": "auswahl", "regel": P,
        "text": "Ein Kind rechnet die Jahreszinsen für 900 € bei 4 % und danach den Kontostand. "
                "Zeile 1: 1 % von 900 € sind 90 €. "
                "Zeile 2: 4 % sind 4 · 90 € = 360 €. "
                "Zeile 3: Nach einem Jahr stehen 900 € + 360 € = 1 260 € auf dem Konto. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Rechne Zeile 1 selbst nach.",
        "w": "Zeile 1 ist falsch: 1 % von 900 € sind 900 € : 100 = 9 €. Die Zeilen 2 und 3 rechnen mit dem falschen Wert "
             "richtig weiter. Mit 9 € ergeben sich 36 € Zinsen und 936 € auf dem Konto.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile folgt richtig aus Zeile 1: 4 · 90 € = 360 €"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2: 900 € + 360 € = 1 260 €"},
        ],
    },
    # ---------------- jahreszinsen_komma ----------------
    {
        "k": "K7-V010", "karte": "jahreszinsen_komma", "typ": "LW", "s": 1, "y": "luecken", "regel": P,
        "text": "Ein Kapital von 1 600 € wird mit 2,5 % verzinst. 1 % des Kapitals sind ① €. "
                "Die Hälfte davon ist der Betrag für 0,5 %: ② €. "
                "Die Zinsen für ein Jahr sind ③ €.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["1600 // 100", "L1 // 2", "2 * L1 + L2"], "erwartet": [16, 8, 40], "entscheidend": 3,
        "h": "2,5 % sind 2 % und noch 0,5 % dazu.",
        "w": "1 % von 1 600 € sind 16 €, 0,5 % sind 8 €. 2,5 % sind 2 · 16 € + 8 € = 40 €.",
        "fehlbilder": [{"luecke": 3, "antwort": 32, "rechnung": "2 * L1", "beschreibung": "den Betrag für 0,5 % vergessen"},
                       {"luecke": 3, "antwort": 24, "rechnung": "L1 + L2", "beschreibung": "nur 1 % und 0,5 % zusammengezählt"}],
    },
    {
        "k": "K7-V011", "karte": "jahreszinsen_komma", "typ": "AN", "s": 2, "y": "zahl", "regel": P,
        "text": "Ein Verein legt 4 000 € für ein Jahr zu 1,5 % an. Mit den Zinsen sollen Trikots bezahlt werden, "
                "ein Trikot kostet 20 €. Wie viele ganze Trikots kann der Verein davon bezahlen?",
        "c": "(4000 * 15 // 1000) // 20", "erwartet": 3, "einheit": "Trikots",
        "h": "Rechne zuerst die Jahreszinsen, dann teile durch den Preis.",
        "w": "1 % von 4 000 € sind 40 €. 1,5 % sind 40 € + 20 € = 60 €. 60 € : 20 € = 3 Trikots.",
        "fehlbilder": [{"antwort": 2, "rechnung": "4000 // 100 // 20", "beschreibung": "nur 1 % statt 1,5 % gerechnet"},
                       {"antwort": 30, "rechnung": "(4000 * 15 // 100) // 20", "beschreibung": "1,5 % als 15 % gelesen"}],
    },
    {
        "k": "K7-V012", "karte": "jahreszinsen_komma", "typ": "FD", "s": 3, "y": "auswahl", "regel": P,
        "text": "Ein Kind rechnet 3,5 % von 1 400 €. Zeile 1: 1 % von 1 400 € sind 14 €. "
                "Zeile 2: Jetzt mit 0,035 malnehmen: 14 € · 0,035 = 0,49 €. "
                "Zeile 3: 0,49 € sind weniger als ein Euro. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Nach dem 1-%-Schritt nimmst du mit der Prozentzahl mal.",
        "w": "Zeile 1 stimmt. Falsch ist Zeile 2: Nach dem 1-%-Schritt nimmst du mit 3,5 mal, also 14 € · 3,5 = 49 €. "
             "Zeile 3 folgt richtig aus Zeile 2 (0,49 € sind wirklich weniger als ein Euro), übernimmt aber den Fehler.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: 1 400 € : 100 = 14 €"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2; der Fehler steht schon in Zeile 2"},
        ],
    },
    # ---------------- zinssatz ----------------
    {
        "k": "K7-V013", "karte": "zinssatz", "typ": "LW", "s": 1, "y": "luecken", "regel": P,
        "text": "Für ein Kapital von 600 € gibt es im Jahr 24 € Zinsen. "
                "1 % des Kapitals sind ① €. Der Zinssatz ist ② %. "
                "Bei diesem Zinssatz bringen 2 500 € im Jahr ③ € Zinsen.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["600 // 100", "24 // L1", "L2 * (2500 // 100)"], "erwartet": [6, 4, 100], "entscheidend": 2,
        "h": "Wie oft passt 1 % in die Zinsen?",
        "w": "1 % von 600 € sind 6 €. In 24 € stecken 24 : 6 = 4 solche Schritte, der Zinssatz ist 4 %. "
             "Für 2 500 € sind 1 % genau 25 €, also 4 · 25 € = 100 €.",
        "fehlbilder": [{"luecke": 2, "antwort": 25, "rechnung": "600 / 24", "beschreibung": "Kapital durch Zinsen geteilt statt umgekehrt"},
                       {"luecke": 3, "antwort": 25, "rechnung": "2500 // 100", "beschreibung": "nur 1 % des neuen Kapitals genannt"}],
    },
    {
        "k": "K7-V014", "karte": "zinssatz", "typ": "ZW", "s": 2, "y": "zahl", "regel": P,
        "text": "Ein Kapital von 750 € bringt im Jahr 30 € Zinsen. Weg A: 1 % sind 7,50 €, und in 30 € stecken "
                "30 : 7,50 Schritte. Weg B: 30 : 750 = 0,04, das mal 100. Wie hoch ist der Zinssatz in Prozent?",
        "c": "30 * 100 // 750", "erwartet": 4, "einheit": "%",
        "h": "Beide Wege führen zur gleichen Prozentzahl.",
        "w": "Weg A: 30 : 7,50 = 4. Weg B: 0,04 · 100 = 4. Der Zinssatz ist 4 %.",
        "fehlbilder": [{"antwort": 25, "rechnung": "750 / 30", "beschreibung": "750 : 30 gerechnet, also falsch herum"},
                       {"antwort": 7.5, "rechnung": "750 / 100", "beschreibung": "den 1-%-Betrag als Antwort genommen"}],
    },
    {
        "k": "K7-V015", "karte": "zinssatz", "typ": "FD", "s": 3, "y": "auswahl", "regel": P,
        "text": "Ein Kind sucht den Zinssatz für 800 € Kapital und 32 € Zinsen. "
                "Zeile 1: Der Zinssatz ist Zinsen durch Kapital, mal 100. "
                "Zeile 2: Also ist der Zinssatz 800 : 32 · 100 = 2 500 %. "
                "Zeile 3: 2 500 % wären für ein Sparkonto unmöglich viel. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Vergleiche, was in Zeile 1 vorne steht und was in Zeile 2 vorne steht.",
        "w": "Zeile 1 stimmt. Zeile 2 setzt die Zahlen falsch ein: Die Zinsen stehen vorne, also 32 : 800 · 100 = 4. "
             "Der Zinssatz ist 4 %. Zeile 3 folgt richtig aus Zeile 2: 2 500 % wären unmöglich viel.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, sie beschreibt das Vorgehen"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2; sie zeigt nur, dass das Ergebnis nicht stimmen kann"},
        ],
    },
    # ---------------- kapital ----------------
    {
        "k": "K7-V016", "karte": "kapital", "typ": "LW", "s": 1, "y": "luecken", "regel": P,
        "text": "Ein Kapital bringt bei 5 % im Jahr 45 € Zinsen. 1 % des Kapitals sind ① €. "
                "Das Kapital selbst ist ② €. "
                "Bei 3 % würde dasselbe Kapital im Jahr ③ € Zinsen bringen.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["45 // 5", "100 * L1", "3 * L1"], "erwartet": [9, 900, 27], "entscheidend": 2,
        "h": "Rechne über 1 %.",
        "w": "5 % sind 45 €, also ist 1 % ein Fünftel davon: 9 €. Das Kapital sind 100 %: 9 € · 100 = 900 €. "
             "3 % davon sind 3 · 9 € = 27 €.",
        "fehlbilder": [{"luecke": 2, "antwort": 225, "rechnung": "45 * 5", "beschreibung": "mit 5 malgenommen statt geteilt"},
                       {"luecke": 3, "antwort": 45, "rechnung": "5 * L1", "beschreibung": "mit dem alten Zinssatz weitergerechnet"}],
    },
    {
        "k": "K7-V017", "karte": "kapital", "typ": "BR", "s": 2, "y": "auswahl", "regel": P,
        "text": "Ein Satz lautet: „3 % eines Kapitals sind 54 €.“ Welche Rechnung gibt das Kapital?",
        "a": ["54 € : 3 · 100", "54 € · 3 : 100", "54 € · 3", "54 € : 100 : 3"],
        "richtig": 0,
        "a_rechnung": ["54/3*100", "54*3/100", "54*3", "54/100/3"], "a_wert": 1800,
        "h": "Gehe über 1 %: erst ein Prozent, dann hundert Prozent.",
        "w": "1 % sind 54 € : 3 = 18 €. 100 % sind 18 € · 100 = 1 800 €. Die Rechnung ist 54 € : 3 · 100.",
        "fehlbilder": [
            {"index": 1, "antwort": "54 € · 3 : 100", "beschreibung": "wie bei den Jahreszinsen gerechnet, also in die falsche Richtung"},
            {"index": 2, "antwort": "54 € · 3", "beschreibung": "nur mit der Prozentzahl malgenommen"},
            {"index": 3, "antwort": "54 € : 100 : 3", "beschreibung": "zweimal geteilt statt über 1 % zu 100 % hochzurechnen"},
        ],
    },
    {
        "k": "K7-V018", "karte": "kapital", "typ": "VW", "s": 1, "y": "auswahl", "regel": P,
        "text": "Gesucht ist das Kapital. Bekannt sind die Jahreszinsen 60 € und der Zinssatz 4 %. "
                "Welches Vorgehen führt zum Ziel?",
        "a": ["Zinsen durch den Zinssatz, dann mal 100",
              "Zinsen mal den Zinssatz, dann durch 100",
              "Zinsen mal 100, dann mal den Zinssatz",
              "Zinssatz durch die Zinsen, dann mal 100"],
        "richtig": 0,
        "a_rechnung": ["60/4*100", "60*4/100", "60*100*4", "4/60*100"], "a_wert": 1500,
        "h": "Der Weg geht über 1 %.",
        "w": "60 € : 4 = 15 € sind 1 %. 15 € · 100 = 1 500 € sind das Kapital.",
        "fehlbilder": [
            {"index": 1, "antwort": "Zinsen mal den Zinssatz, dann durch 100",
             "beschreibung": "das ist der Weg für die Jahreszinsen, nicht für das Kapital"},
            {"index": 2, "antwort": "Zinsen mal 100, dann mal den Zinssatz",
             "beschreibung": "zweimal vergrößert statt einmal geteilt"},
            {"index": 3, "antwort": "Zinssatz durch die Zinsen, dann mal 100",
             "beschreibung": "Zinsen und Zinssatz vertauscht"},
        ],
    },
    # ---------------- monatszinsen ----------------
    {
        "k": "K7-V019", "karte": "monatszinsen", "typ": "LW", "s": 1, "y": "luecken", "regel": P,
        "text": "Ein Kapital von 3 000 € wird mit 2 % verzinst. Die Jahreszinsen sind ① €. "
                "Ein einzelner Monat bringt ② €. "
                "Für 4 Monate bekommt man ③ € Zinsen.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["3000 * 2 // 100", "L1 // 12", "4 * L2"], "erwartet": [60, 5, 20], "entscheidend": 3,
        "h": "Ein Jahr hat 12 Monate.",
        "w": "Die Jahreszinsen sind 3 000 € · 2 : 100 = 60 €. Ein Monat bringt 60 € : 12 = 5 €. 4 Monate bringen 4 · 5 € = 20 €.",
        "fehlbilder": [{"luecke": 3, "antwort": 240, "rechnung": "4 * L1", "beschreibung": "die Jahreszinsen mit 4 malgenommen statt den Zeitanteil zu nehmen"},
                       {"luecke": 2, "antwort": 720, "rechnung": "12 * L1", "beschreibung": "mit 12 malgenommen statt durch 12 geteilt"}],
    },
    {
        "k": "K7-V020", "karte": "monatszinsen", "typ": "UM", "s": 2, "y": "zahl", "regel": P,
        "text": "Ein Kapital von 1 800 € ist mit 4 % verzinst. Für eine bestimmte Zahl von Monaten wurden "
                "24 € Zinsen berechnet, jeder Monat brachte gleich viel. Für wie viele Monate war das?",
        "c": "24 * 12 // (1800 * 4 // 100)", "erwartet": 4, "einheit": "Monate",
        "h": "Rechne zuerst, wie viel ein einzelner Monat bringt.",
        "w": "Jahreszinsen: 1 800 € · 4 : 100 = 72 €. Ein Monat bringt 72 € : 12 = 6 €. 24 € : 6 € = 4 Monate.",
        "fehlbilder": [{"antwort": 3, "rechnung": "72 // 24", "beschreibung": "Jahreszinsen durch die Zinsen geteilt, also falsch herum"},
                       {"antwort": 6, "rechnung": "72 // 12", "beschreibung": "den Monatsbetrag als Antwort genommen"}],
    },
    {
        "k": "K7-V021", "karte": "monatszinsen", "typ": "AN", "s": 3, "y": "zahl", "regel": P,
        "text": "Eine Werkstatt leiht sich 6 000 € zu 9 % im Jahr und zahlt nach 8 Monaten das geliehene Geld "
                "samt den Zinsen für diese Zeit auf einmal zurück. Wie viel Euro zahlt sie insgesamt zurück?",
        "c": "6000 + (6000 * 9 // 100) * 8 // 12", "erwartet": 6360, "einheit": "€",
        "h": "Erst die Zinsen für 8 Monate, dann das geliehene Geld dazu.",
        "w": "Jahreszinsen: 6 000 € · 9 : 100 = 540 €. Für 8 Monate: 540 € · 8 : 12 = 360 €. "
             "Zurück zu zahlen sind 6 000 € + 360 € = 6 360 €.",
        "fehlbilder": [{"antwort": 360, "rechnung": "540 * 8 // 12", "beschreibung": "nur die Zinsen genannt, das geliehene Geld fehlt"},
                       {"antwort": 6540, "rechnung": "6000 + 540", "beschreibung": "die Jahreszinsen genommen, nicht die für 8 Monate"}],
    },
    # ---------------- zeitanteil ----------------
    {
        "k": "K7-V022", "karte": "zeitanteil", "typ": "VW", "s": 1, "y": "auswahl", "regel": P,
        "text": "Ein Kapital von 2 000 € ist mit 3 % verzinst, die Zinsen werden erst am Ende gezahlt. "
                "Gesucht sind die Zinsen für ein halbes Jahr. Welche Rechnung passt?",
        "a": ["2 000 € · 3 : 100 : 2", "2 000 € · 3 : 100 · 2", "2 000 € · 3 : 100 : 6", "2 000 € · 3 : 100 · 6"],
        "richtig": 0,
        "a_rechnung": ["2000*3/100/2", "2000*3/100*2", "2000*3/100/6", "2000*3/100*6"], "a_wert": 30,
        "h": "Ein halbes Jahr bringt die Hälfte der Jahreszinsen.",
        "w": "Jahreszinsen: 60 €. Ein halbes Jahr: 60 € : 2 = 30 €. Also durch 2 teilen.",
        "fehlbilder": [
            {"index": 1, "antwort": "2 000 € · 3 : 100 · 2", "beschreibung": "verdoppelt statt halbiert"},
            {"index": 2, "antwort": "2 000 € · 3 : 100 : 6", "beschreibung": "durch die Zahl der Monate geteilt statt durch 2"},
            {"index": 3, "antwort": "2 000 € · 3 : 100 · 6", "beschreibung": "mit der Zahl der Monate malgenommen"},
        ],
    },
    {
        "k": "K7-V023", "karte": "zeitanteil", "typ": "AN", "s": 2, "y": "zahl", "regel": P,
        "text": "Ein Jugendlicher legt 1 200 € aus einem Ferienjob für ein Vierteljahr zu 2 % an; das Geld bleibt "
                "angelegt. Ein Fahrrad für 300 € will er allein aus den Zinsen und eigenem Taschengeld bezahlen. "
                "Wie viel Euro muss er zu den Zinsen aus dem Taschengeld dazulegen?",
        "c": "300 - (1200 * 2 // 100) // 4", "erwartet": 294, "einheit": "€",
        "h": "Ein Vierteljahr bringt ein Viertel der Jahreszinsen.",
        "w": "Jahreszinsen: 1 200 € · 2 : 100 = 24 €. Ein Vierteljahr: 24 € : 4 = 6 €. "
             "Es fehlen 300 € − 6 € = 294 €.",
        "fehlbilder": [{"antwort": 276, "rechnung": "300 - 24", "beschreibung": "die Jahreszinsen abgezogen statt die für ein Vierteljahr"},
                       {"antwort": 6, "rechnung": "24 // 4", "beschreibung": "den Zinsbetrag genannt statt des fehlenden Rests"}],
    },
    {
        "k": "K7-V024", "karte": "zeitanteil", "typ": "FD", "s": 3, "y": "auswahl", "regel": P,
        "text": "Ein Kind rechnet die Zinsen für ein halbes Jahr bei 2 200 € und 3 %. "
                "Zeile 1: Die Jahreszinsen sind 66 €. Zeile 2: Ein halbes Jahr sind 6 von 12 Monaten. "
                "Zeile 3: Also sind die Zinsen für ein halbes Jahr 66 € · 6 = 396 €. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Vergleiche das Ergebnis mit den Jahreszinsen: Kann ein halbes Jahr mehr bringen als ein ganzes?",
        "w": "Zeile 1 und 2 stimmen. In Zeile 3 muss man 6/12 des Jahresbetrags nehmen: 66 € : 2 = 33 €. "
             "Das Sechsfache wären die Zinsen für sechs Jahre.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: 2 200 € · 3 : 100 = 66 €"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: ein halbes Jahr hat 6 Monate"},
        ],
    },
]
