"""zahlen.potenzen_zehner (Klasse 7 Realschule / 6 Gymnasium): 7 Lernkarten, 21 Aufgaben in neuer Form.

Alle Lücken sind ganze Zahlen (Exponenten, Stellenzahlen, Vielfache) – Dezimalzahlen stehen nur im Text.
Die Lernkarte vergleichen_pruefen hat im Bestand schon drei Aufgaben vom Typ „fehler“; dort stehen deshalb
Verfahren wählen, Zwei Wege und Anwenden statt eines weiteren Fehler-Detektivs.
"""
STAND = "2026-11-27"
TITEL = "Zehnerpotenzen und wissenschaftliche Schreibweise"
PASST_NICHT = ()

POT = "rr.potenz"
BUE = "id.zahlen.buendeln"

AUFGABEN = [
    # ---------------- zehnerpotenz ----------------
    {
        "k": "K7-V025", "karte": "zehnerpotenz", "typ": "LW", "s": 1, "y": "luecken", "regel": POT,
        "text": "10⁴ bedeutet 10 · 10 · 10 · 10. Jeder Faktor 10 schiebt die 1 eine Stelle nach links. "
                "Hinter der 1 stehen deshalb ① Nullen, und 10⁴ ist die Zahl ②.",
        "schablone": "① = □; ② = □",
        "c": ["4", "10 ** 4"], "erwartet": [4, 10000],
        "h": "Zähle die Faktoren 10.",
        "w": "Es sind vier Faktoren 10, also vier Nullen hinter der 1: 10⁴ = 10 000.",
        "fehlbilder": [{"luecke": 2, "antwort": 40, "beschreibung": "10 mit dem Exponenten malgenommen"}],
    },
    {
        "k": "K7-V026", "karte": "zehnerpotenz", "typ": "UM", "s": 2, "y": "zahl", "regel": POT,
        "text": "Ein Lager hat 10ⁿ Fächer, nämlich 100 000. Ein größeres Lager hat 10ⁿ⁺¹ Fächer. "
                "Wie viele Fächer hat das größere Lager?",
        "c": "10 ** (5 + 1)", "erwartet": 1000000, "einheit": "Fächer",
        "h": "Lies zuerst n ab, dann rechne mit n + 1.",
        "w": "100 000 ist eine 1 mit 5 Nullen, also n = 5. Dann ist 10⁶ = 1 000 000 Fächer.",
        "fehlbilder": [{"antwort": 100001, "beschreibung": "1 dazugezählt statt den Exponenten um 1 erhöht"},
                       {"antwort": 6, "beschreibung": "den Exponenten als Antwort genannt"}],
    },
    {
        "k": "K7-V027", "karte": "zehnerpotenz", "typ": "FD", "s": 3, "y": "auswahl", "regel": POT,
        "text": "Ein Kind erklärt 10⁶. Zeile 1: Der Exponent 6 sagt, wie viele Nullen hinter der 1 stehen. "
                "Zeile 2: Also ist 10⁶ = 1 000 000. "
                "Zeile 3: Damit ist 10⁶ sechsmal so groß wie 10. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Rechne einmal 1 000 000 : 10.",
        "w": "Zeile 1 und 2 stimmen. 1 000 000 : 10 = 100 000, also ist 10⁶ hunderttausendmal so groß wie 10. "
             "Der Exponent zählt die Faktoren, nicht das Vielfache.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: der Exponent zählt die Nullen"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: eine 1 mit sechs Nullen"},
        ],
    },
    # ---------------- gross_wissenschaftlich ----------------
    {
        "k": "K7-V028", "karte": "gross_wissenschaftlich", "typ": "LW", "s": 1, "y": "luecken", "regel": POT,
        "text": "Die Zahl 62 000 soll wissenschaftlich geschrieben werden. Das Komma kommt hinter die erste Ziffer: 6,2. "
                "Dabei wandert es ① Stellen nach links. Die Zehnerpotenz 10 hoch ① ist die Zahl ②.",
        "schablone": "① = □; ② = □",
        "c": ["4", "10 ** 4"], "erwartet": [4, 10000],
        "h": "Zähle, um wie viele Stellen das Komma wandert.",
        "w": "Von 62 000 zu 6,2 wandert das Komma 4 Stellen nach links. 10⁴ = 10 000, und 6,2 · 10 000 = 62 000.",
        "fehlbilder": [{"luecke": 1, "antwort": 5, "beschreibung": "die Ziffern gezählt statt die Stellen, die das Komma wandert"}],
    },
    {
        "k": "K7-V029", "karte": "gross_wissenschaftlich", "typ": "BR", "s": 2, "y": "auswahl", "regel": POT,
        "text": "Welche Schreibweise von 7 300 000 ist die wissenschaftliche?",
        "a": ["73 · 10⁵", "7,3 · 10⁶", "0,73 · 10⁷", "7,3 · 10⁵"], "richtig": 1,
        "h": "Vor dem Komma muss genau eine Ziffer von 1 bis 9 stehen.",
        "w": "7 300 000 = 7,3 · 10⁶. Die ersten und dritten Formen haben denselben Wert, sind aber nicht "
             "wissenschaftlich. 7,3 · 10⁵ wäre nur 730 000.",
        "fehlbilder": [
            {"index": 0, "antwort": "73 · 10⁵", "beschreibung": "zwei Ziffern vor dem Komma"},
            {"index": 2, "antwort": "0,73 · 10⁷", "beschreibung": "eine Null vor dem Komma"},
            {"index": 3, "antwort": "7,3 · 10⁵", "beschreibung": "zwei Stellen zu wenig gezählt"},
        ],
    },
    {
        "k": "K7-V030", "karte": "gross_wissenschaftlich", "typ": "FD", "s": 3, "y": "auswahl", "regel": POT,
        "text": "Ein Kind schreibt 48 500 wissenschaftlich. Zeile 1: Komma hinter die erste Ziffer: 4,85. "
                "Zeile 2: Von 48 500 bis 4,85 wandert das Komma 4 Stellen nach links. "
                "Zeile 3: Weil es nach links wandert, ist der Exponent negativ: 4,85 · 10⁻⁴. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Prüfe grob: Ist 48 500 groß oder klein?",
        "w": "Zeile 1 und 2 stimmen. 48 500 ist eine große Zahl, der Exponent ist deshalb positiv: 4,85 · 10⁴. "
             "Negative Exponenten gehören zu Zahlen unter 1.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: eine Ziffer vor dem Komma"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: es sind 4 Stellen"},
        ],
    },
    # ---------------- vorsilben_gross ----------------
    {
        "k": "K7-V031", "karte": "vorsilben_gross", "typ": "LW", "s": 1, "y": "luecken", "regel": BUE,
        "text": "Ein Kraftwerk leistet 3 GW. Giga bedeutet 10⁹, also sind das 3 · 10⁹ Watt. "
                "Eine Million ist 10⁶; in Millionen Watt sind das ①. Ein Kilowatt ist 10³ Watt; in Kilowatt sind es ②.",
        "schablone": "① = □; ② = □",
        "c": ["3 * 10 ** 9 // 10 ** 6", "3 * 10 ** 9 // 10 ** 3"], "erwartet": [3000, 3000000],
        "h": "Teile die Wattzahl einmal durch 10⁶ und einmal durch 10³.",
        "w": "3 GW = 3 000 000 000 W. Das sind 3 000 Millionen Watt und 3 000 000 kW.",
        "fehlbilder": [{"luecke": 2, "antwort": 3000, "beschreibung": "Kilo und Mega verwechselt"}],
    },
    {
        "k": "K7-V032", "karte": "vorsilben_gross", "typ": "AN", "s": 2, "y": "zahl", "regel": BUE,
        "text": "Ein Rechenzentrum braucht 12 MW Leistung. Ein Windrad liefert 3 000 kW. "
                "Wie viele Windräder braucht man dafür?",
        "c": "12 * 10 ** 6 // (3000 * 10 ** 3)", "erwartet": 4, "einheit": "Windräder",
        "h": "Rechne beide Angaben zuerst in Watt um.",
        "w": "12 MW = 12 000 000 W und 3 000 kW = 3 000 000 W. 12 000 000 : 3 000 000 = 4 Windräder.",
        "fehlbilder": [{"antwort": 250, "beschreibung": "Mega und Kilo gleich behandelt"},
                       {"antwort": 4000, "beschreibung": "die Einheiten nicht angeglichen"}],
    },
    {
        "k": "K7-V033", "karte": "vorsilben_gross", "typ": "FD", "s": 3, "y": "auswahl", "regel": BUE,
        "text": "Ein Kind rechnet 7 TB in Byte um. Zeile 1: Tera bedeutet 10¹². "
                "Zeile 2: Also sind 7 TB = 7 · 10¹² Byte. "
                "Zeile 3: Das sind 7 000 Millionen Byte. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Wie viele Nullen hat eine Million?",
        "w": "Zeile 1 und 2 stimmen. Eine Million ist 10⁶, und 7 · 10¹² : 10⁶ = 7 · 10⁶. "
             "Es sind also 7 000 000 Millionen Byte; 7 000 Millionen wären nur 7 · 10⁹.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: Tera ist 10¹²"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: die Vorsilbe wird durch die Potenz ersetzt"},
        ],
    },
    # ---------------- negativer_exponent ----------------
    {
        "k": "K7-V034", "karte": "negativer_exponent", "typ": "LW", "s": 1, "y": "luecken", "regel": POT,
        "text": "Von 10⁰ = 1 geht es durch 10 weiter: 10⁻¹ = 0,1 und 10⁻² = 0,01. "
                "Bei 10⁻ⁿ steht die 1 an der n-ten Stelle nach dem Komma. "
                "Bei 10⁻⁵ hat die Zahl ① Stellen nach dem Komma, davon ② Nullen vor der 1.",
        "schablone": "① = □; ② = □",
        "c": ["5", "5 - 1"], "erwartet": [5, 4],
        "h": "Schreibe 10⁻⁵ einmal als Dezimalzahl hin.",
        "w": "10⁻⁵ = 0,00001. Nach dem Komma stehen 5 Stellen; die ersten 4 sind Nullen, dann kommt die 1.",
        "fehlbilder": [{"luecke": 2, "antwort": 5, "beschreibung": "die 1 mitgezählt"}],
    },
    {
        "k": "K7-V035", "karte": "negativer_exponent", "typ": "ZW", "s": 2, "y": "zahl", "regel": POT,
        "text": "Wie viele Nullen stehen bei 10⁻⁴ zwischen dem Komma und der 1? "
                "Weg A: vom Exponenten 1 abziehen. Weg B: die Zahl hinschreiben und die Nullen zählen.",
        "c": "4 - 1", "erwartet": 3,
        "h": "Die 1 steht an der vierten Stelle nach dem Komma.",
        "w": "Weg A: 4 − 1 = 3. Weg B: 10⁻⁴ = 0,0001, zwischen Komma und 1 stehen 3 Nullen.",
        "fehlbilder": [{"antwort": 4, "beschreibung": "die Stelle der 1 mitgezählt"},
                       {"antwort": 5, "beschreibung": "eine Null zu viel gezählt"}],
    },
    {
        "k": "K7-V036", "karte": "negativer_exponent", "typ": "FD", "s": 3, "y": "auswahl", "regel": POT,
        "text": "Ein Kind sagt zu 10⁻² : Zeile 1: Der Exponent ist negativ. "
                "Zeile 2: Also ist die Zahl kleiner als 1. "
                "Zeile 3: Deshalb ist 10⁻² = −0,01. "
                "In welcher Zeile steckt der Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 2,
        "h": "Kann eine Zahl kleiner als 1 und trotzdem größer als null sein?",
        "w": "Zeile 1 und 2 stimmen. 10⁻² = 0,01 liegt zwischen null und 1. "
             "Ein negativer Exponent macht die Zahl klein, nicht negativ.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, sie liest nur den Exponenten ab"},
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile ist richtig: 10⁻² liegt unter 1"},
        ],
    },
    # ---------------- klein_wissenschaftlich ----------------
    {
        "k": "K7-V037", "karte": "klein_wissenschaftlich", "typ": "LW", "s": 1, "y": "luecken", "regel": POT,
        "text": "Die Zahl 0,00036 soll wissenschaftlich geschrieben werden. Das Komma kommt hinter die erste Ziffer "
                "ungleich null: 3,6. Dabei wandert es ① Stellen nach rechts. Die Zehnerpotenz 10 hoch ① ist ②.",
        "schablone": "① = □; ② = □",
        "c": ["4", "10 ** 4"], "erwartet": [4, 10000],
        "h": "Zähle die Stellen, die das Komma nach rechts wandert.",
        "w": "0,00036 = 3,6 · 10⁻⁴. Das Komma wandert 4 Stellen nach rechts, 10⁴ = 10 000, "
             "und 3,6 : 10 000 ergibt wieder 0,00036.",
        "fehlbilder": [{"luecke": 1, "antwort": 3, "beschreibung": "nur die Nullen nach dem Komma gezählt"}],
    },
    {
        "k": "K7-V038", "karte": "klein_wissenschaftlich", "typ": "UM", "s": 2, "y": "zahl", "regel": POT,
        "text": "Eine Zahl ist 2,5 · 10⁻³. Wie viele Stellen hat diese Zahl nach dem Komma?",
        "c": "3 + 1", "erwartet": 4,
        "h": "Schreibe die Zahl als Dezimalzahl hin.",
        "w": "2,5 · 10⁻³ = 0,0025. Die 2 steht an der 3. Stelle, die 5 an der 4. Stelle: 4 Stellen nach dem Komma.",
        "fehlbilder": [{"antwort": 3, "beschreibung": "nur den Exponenten genommen"},
                       {"antwort": 2, "beschreibung": "die Nullen nicht mitgezählt"}],
    },
    {
        "k": "K7-V039", "karte": "klein_wissenschaftlich", "typ": "BR", "s": 2, "y": "auswahl", "regel": POT,
        "text": "Welche Dezimalzahl gehört zu 8,4 · 10⁻⁵?",
        "a": ["0,000084", "0,00084", "0,0000084", "840 000"], "richtig": 0,
        "h": "Die erste Ziffer steht an der fünften Stelle nach dem Komma.",
        "w": "Bei 10⁻⁵ steht die 8 an der 5. Stelle nach dem Komma: 0,000084.",
        "fehlbilder": [
            {"index": 1, "antwort": "0,00084", "beschreibung": "eine Stelle zu wenig, das wäre 8,4 · 10⁻⁴"},
            {"index": 2, "antwort": "0,0000084", "beschreibung": "eine Stelle zu viel, das wäre 8,4 · 10⁻⁶"},
            {"index": 3, "antwort": "840 000", "beschreibung": "den Exponenten positiv gelesen"},
        ],
    },
    # ---------------- vorsilben_klein ----------------
    {
        "k": "K7-V040", "karte": "vorsilben_klein", "typ": "LW", "s": 1, "y": "luecken", "regel": BUE,
        "text": "Ein Bakterium ist 2 µm lang. Mikro bedeutet 10⁻⁶ m, Milli bedeutet 10⁻³ m. "
                "Ein Millimeter besteht aus ① Mikrometern. Das Bakterium ist der ②-te Teil eines Millimeters.",
        "schablone": "① = □; ② = □",
        "c": ["10 ** 3", "10 ** 3 // 2"], "erwartet": [1000, 500],
        "h": "Mikro ist tausendmal kleiner als Milli.",
        "w": "10⁻³ : 10⁻⁶ = 10³ = 1 000, ein Millimeter hat also 1 000 µm. "
             "1 000 : 2 = 500: das Bakterium ist der 500-te Teil eines Millimeters.",
        "fehlbilder": [{"luecke": 1, "antwort": 1000000, "beschreibung": "Mikrometer mit Metern verglichen"}],
    },
    {
        "k": "K7-V041", "karte": "vorsilben_klein", "typ": "AN", "s": 2, "y": "zahl", "regel": BUE,
        "text": "Eine Schutzfolie ist 250 nm dick. Wie viele solche Folien ergeben übereinander genau 1 mm?",
        "c": "10 ** 6 // 250", "erwartet": 4000, "einheit": "Folien",
        "h": "Rechne beide Längen in Nanometer um.",
        "w": "1 mm = 10⁻³ m = 10⁶ nm. 10⁶ : 250 = 4 000 Folien.",
        "fehlbilder": [{"antwort": 4, "beschreibung": "Nano wie Mikro behandelt"},
                       {"antwort": 4000000, "beschreibung": "Millimeter und Meter verwechselt"}],
    },
    {
        "k": "K7-V042", "karte": "vorsilben_klein", "typ": "VW", "s": 2, "y": "auswahl", "regel": BUE,
        "text": "Eine Messung dauert 7 ms. Welche Rechnung gibt die Zeit in Sekunden?",
        "a": ["7 · 10⁻³ s", "7 · 10³ s", "7 : 10⁻³ s", "7 · 10⁻⁶ s"], "richtig": 0,
        "h": "Milli bedeutet 10⁻³.",
        "w": "7 ms = 7 · 10⁻³ s = 0,007 s.",
        "fehlbilder": [
            {"index": 1, "antwort": "7 · 10³ s", "beschreibung": "Vorsilbe als Vergrößerung gelesen"},
            {"index": 2, "antwort": "7 : 10⁻³ s", "beschreibung": "geteilt statt malgenommen, das ergibt 7 000 s"},
            {"index": 3, "antwort": "7 · 10⁻⁶ s", "beschreibung": "Milli mit Mikro verwechselt"},
        ],
    },
    # ---------------- vergleichen_pruefen ----------------
    {
        "k": "K7-V043", "karte": "vergleichen_pruefen", "typ": "VW", "s": 2, "y": "auswahl", "regel": POT,
        "text": "Du sollst 3 · 10⁷ und 8 · 10⁶ vergleichen. Welches Vorgehen führt sicher zum Ziel?",
        "a": ["zuerst die Exponenten vergleichen, bei Gleichheit die Zahl davor",
              "zuerst die Zahlen vor der Zehnerpotenz vergleichen",
              "die Exponenten addieren und die Summen vergleichen",
              "die Ziffern beider Zahlen zählen"],
        "richtig": 0,
        "h": "Welcher Teil entscheidet über die Größenordnung?",
        "w": "7 ist größer als 6, also ist 3 · 10⁷ = 30 000 000 größer als 8 · 10⁶ = 8 000 000. "
             "Die Zahl vor der Potenz entscheidet nur bei gleichem Exponenten.",
        "fehlbilder": [
            {"index": 1, "antwort": "zuerst die Zahlen vor der Zehnerpotenz vergleichen",
             "beschreibung": "dann käme hier 8 · 10⁶ heraus, obwohl es die kleinere Zahl ist"},
            {"index": 2, "antwort": "die Exponenten addieren und die Summen vergleichen",
             "beschreibung": "Addieren hat mit dem Vergleich nichts zu tun"},
            {"index": 3, "antwort": "die Ziffern beider Zahlen zählen",
             "beschreibung": "funktioniert nur bei ausgeschriebenen Zahlen, nicht in dieser Schreibweise"},
        ],
    },
    {
        "k": "K7-V044", "karte": "vergleichen_pruefen", "typ": "ZW", "s": 2, "y": "zahl", "regel": POT,
        "text": "Wie oft passt 4 · 10³ in 2 · 10⁵? Weg A: beide Zahlen ausschreiben und teilen. "
                "Weg B: 2 : 4 rechnen und 10⁵ : 10³ dazunehmen.",
        "c": "2 * 10 ** 5 // (4 * 10 ** 3)", "erwartet": 50,
        "h": "Teile die Zahlen davor und die Zehnerpotenzen getrennt.",
        "w": "Weg A: 200 000 : 4 000 = 50. Weg B: 2 : 4 = 0,5 und 10⁵ : 10³ = 100, also 0,5 · 100 = 50.",
        "fehlbilder": [{"antwort": 100, "beschreibung": "nur die Zehnerpotenzen geteilt"},
                       {"antwort": 500, "beschreibung": "beim Teilen der Zahlen davor verrechnet"}],
    },
    {
        "k": "K7-V045", "karte": "vergleichen_pruefen", "typ": "AN", "s": 3, "y": "zahl", "regel": POT,
        "text": "Zwei Landkreise werden zusammengelegt. Der eine hat 3 · 10⁵ Einwohner, der andere 7 · 10⁴. "
                "Wie viele Einwohner hat der neue Landkreis?",
        "c": "3 * 10 ** 5 + 7 * 10 ** 4", "erwartet": 370000, "einheit": "Einwohner",
        "h": "Schreibe beide Zahlen zuerst normal hin.",
        "w": "3 · 10⁵ = 300 000 und 7 · 10⁴ = 70 000. Zusammen sind das 370 000 Einwohner.",
        "fehlbilder": [{"antwort": 1000000, "beschreibung": "die Zahlen davor und die Exponenten einzeln addiert"},
                       {"antwort": 310000, "beschreibung": "die zweite Zahl mit 10³ gelesen"}],
    },
]
