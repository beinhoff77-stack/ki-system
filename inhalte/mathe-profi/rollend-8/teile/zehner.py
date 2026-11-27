"""zahlen.potenzen_zehner (Klasse 7 Realschule / 6 Gymnasium): 7 Lernkarten, 21 Aufgaben in neuer Form.

Alle Lücken sind ganze Zahlen (Exponenten, Stellenzahlen, Vielfache) – Dezimalzahlen stehen nur im Text.
Die Lernkarte vergleichen_pruefen hat im Bestand schon drei Aufgaben vom Typ „fehler“; dort stehen deshalb
Verfahren wählen, Zwei Wege und Anwenden statt eines weiteren Fehler-Detektivs.
Feldbedeutung (c mit L1, L2 …, entscheidend, rechnung, a_rechnung): siehe Kopf von teile/zinsen.py.
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
        "text": "Die Zahl 100 000 000 ist eine 1 mit vielen Nullen. Man schreibt sie als 10 hoch ①. "
                "Nimmt man die Zahl dreimal hintereinander mit 10 mal, schreibt man das Ergebnis als 10 hoch ②. "
                "Das Ergebnis ist ③-mal so groß wie die alte Zahl.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["8", "L1 + 3", "10 ** (L2 - L1)"], "erwartet": [8, 11, 1000], "entscheidend": 2,
        "h": "Zähle die Nullen. Jeder Faktor 10 hängt eine Null an.",
        "w": "Hinter der 1 stehen 8 Nullen, also 10⁸. Drei Faktoren 10 mehr geben 10¹¹. "
             "Die Exponenten werden addiert (8 + 3), nicht malgenommen. 10¹¹ : 10⁸ = 10³ = 1 000.",
        "fehlbilder": [{"luecke": 1, "antwort": 9, "rechnung": "9", "beschreibung": "die Ziffern statt der Nullen gezählt"},
                       {"luecke": 2, "antwort": 24, "rechnung": "L1 * 3", "beschreibung": "die Exponenten malgenommen statt addiert"}],
    },
    {
        "k": "K7-V026", "karte": "zehnerpotenz", "typ": "UM", "s": 2, "y": "zahl", "regel": POT,
        "text": "Ein Lager hat 10ⁿ Fächer, nämlich 100 000. Ein größeres Lager hat 10ⁿ⁺¹ Fächer. "
                "Wie viele Fächer hat das größere Lager?",
        "c": "10 ** (5 + 1)", "erwartet": 1000000, "einheit": "Fächer",
        "h": "Lies zuerst n ab, dann rechne mit n + 1.",
        "w": "100 000 ist eine 1 mit 5 Nullen, also n = 5. Dann ist 10⁶ = 1 000 000 Fächer.",
        "fehlbilder": [{"antwort": 100001, "rechnung": "100000 + 1", "beschreibung": "1 dazugezählt statt den Exponenten um 1 erhöht"},
                       {"antwort": 6, "rechnung": "5 + 1", "beschreibung": "den neuen Exponenten als Antwort genannt"}],
    },
    {
        "k": "K7-V027", "karte": "zehnerpotenz", "typ": "FD", "s": 3, "y": "auswahl", "regel": POT,
        "text": "Ein Kind erklärt 10⁶. Zeile 1: Der Exponent 6 sagt, mit wie viel man 10 malnimmt: 10⁶ = 10 · 6. "
                "Zeile 2: Also ist 10⁶ = 60. "
                "Zeile 3: Damit ist 10⁶ sechsmal so groß wie 10. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Schreibe 10³ einmal ausführlich auf.",
        "w": "Zeile 1 ist falsch: Der Exponent zählt die Faktoren 10, 10⁶ = 10 · 10 · 10 · 10 · 10 · 10 = 1 000 000. "
             "Die Zeilen 2 und 3 folgen richtig aus dem Fehler: 10 · 6 = 60, und 60 ist sechsmal 10.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile folgt richtig aus Zeile 1: 10 · 6 = 60"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2: 60 ist sechsmal so groß wie 10"},
        ],
    },
    # ---------------- gross_wissenschaftlich ----------------
    {
        "k": "K7-V028", "karte": "gross_wissenschaftlich", "typ": "LW", "s": 1, "y": "luecken", "regel": POT,
        "text": "Die Zahl 62 000 soll als 6,2 · 10 hoch ① geschrieben werden. "
                "Die Zehnerpotenz 10 hoch ① ist ausgeschrieben die Zahl ②. "
                "Die zehnmal so große Zahl 620 000 hat bei gleicher Ziffernfolge den Exponenten ③.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["4", "10 ** L1", "L1 + 1"], "erwartet": [4, 10000, 5], "entscheidend": 1,
        "h": "Zähle, um wie viele Stellen das Komma wandert.",
        "w": "Von 62 000 zu 6,2 wandert das Komma 4 Stellen nach links, also 10⁴ = 10 000; 6,2 · 10 000 = 62 000. "
             "Die zehnmal so große Zahl braucht eine Stelle mehr: 6,2 · 10⁵ = 620 000.",
        "fehlbilder": [{"luecke": 1, "antwort": 5, "rechnung": "5", "beschreibung": "die Ziffern gezählt statt die Stellen, die das Komma wandert"},
                       {"luecke": 3, "antwort": 4, "rechnung": "L1", "beschreibung": "den Exponenten nicht angepasst"}],
    },
    {
        "k": "K7-V029", "karte": "gross_wissenschaftlich", "typ": "BR", "s": 2, "y": "auswahl", "regel": POT,
        "text": "Welche Schreibweise von 7 300 000 ist die wissenschaftliche?",
        "a": ["73 · 10⁵", "7,3 · 10⁶", "0,73 · 10⁷", "7,3 · 10⁵"], "richtig": 1,
        "h": "Prüfe die Form: Wie viele Ziffern stehen vor dem Komma?",
        "w": "7 300 000 = 7,3 · 10⁶. Die erste und die dritte Form haben denselben Wert, sind aber nicht "
             "wissenschaftlich (zwei Ziffern bzw. eine Null vor dem Komma). 7,3 · 10⁵ wäre nur 730 000.",
        "fehlbilder": [
            {"index": 0, "antwort": "73 · 10⁵", "beschreibung": "zwei Ziffern vor dem Komma"},
            {"index": 2, "antwort": "0,73 · 10⁷", "beschreibung": "eine Null vor dem Komma"},
            {"index": 3, "antwort": "7,3 · 10⁵", "beschreibung": "eine Stelle zu wenig gezählt"},
        ],
    },
    {
        "k": "K7-V030", "karte": "gross_wissenschaftlich", "typ": "FD", "s": 3, "y": "auswahl", "regel": POT,
        "text": "Ein Kind schreibt 48 500 wissenschaftlich. Zeile 1: Komma hinter die erste Ziffer: 4,85. "
                "Zeile 2: Von 48 500 bis 4,85 wandert das Komma 5 Stellen nach links. "
                "Zeile 3: Also ist 48 500 = 4,85 · 10⁵. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Zähle die Stellen zwischen den beiden Kommastellungen selbst nach.",
        "w": "Zeile 1 stimmt. In Zeile 2 sind es nur 4 Stellen (48 500 → 4,85). Zeile 3 folgt richtig aus Zeile 2, "
             "übernimmt aber die falsche 5. Richtig ist 4,85 · 10⁴.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig: eine Ziffer vor dem Komma"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2; der Fehler steht schon in Zeile 2"},
        ],
    },
    # ---------------- vorsilben_gross ----------------
    {
        "k": "K7-V031", "karte": "vorsilben_gross", "typ": "LW", "s": 1, "y": "luecken", "regel": BUE,
        "text": "Mega bedeutet 10⁶. Giga ist tausendmal so viel wie Mega. Ein Kraftwerk leistet 3 GW. "
                "Das sind 3 · 10 hoch ① Watt. In Megawatt sind es ② MW. In Kilowatt sind es ③ kW.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["9", "3 * 10 ** (L1 - 6)", "L2 * 1000"], "erwartet": [9, 3000, 3000000], "entscheidend": 1,
        "h": "Giga steht eine Stufe über Mega. Kilo ist tausendmal kleiner als Mega.",
        "w": "Giga = 1 000 · 10⁶ = 10⁹, also 3 GW = 3 · 10⁹ W. In MW: 3 · 10⁹ : 10⁶ = 3 000 MW. "
             "1 MW sind 1 000 kW, also 3 000 · 1 000 = 3 000 000 kW.",
        "fehlbilder": [{"luecke": 1, "antwort": 18, "rechnung": "6 * 3", "beschreibung": "die Exponenten malgenommen statt Tausend aufgesetzt"},
                       {"luecke": 3, "antwort": 3000, "rechnung": "3 * 10 ** 9 // 10 ** 6", "beschreibung": "Kilo und Mega verwechselt, wie bei ② gerechnet"}],
    },
    {
        "k": "K7-V032", "karte": "vorsilben_gross", "typ": "AN", "s": 2, "y": "zahl", "regel": BUE,
        "text": "Ein Rechenzentrum braucht 12 MW Leistung. Ein Windrad liefert 3 000 kW. "
                "Wie viele Windräder braucht man dafür?",
        "c": "12 * 10 ** 6 // (3000 * 10 ** 3)", "erwartet": 4, "einheit": "Windräder",
        "h": "Rechne beide Angaben zuerst in Watt um.",
        "w": "12 MW = 12 000 000 W und 3 000 kW = 3 000 000 W. 12 000 000 : 3 000 000 = 4 Windräder.",
        "fehlbilder": [{"antwort": 250, "rechnung": "3000 / 12", "beschreibung": "falsch herum geteilt"},
                       {"antwort": 0.004, "rechnung": "12 / 3000", "beschreibung": "die Einheiten nicht angeglichen"}],
    },
    {
        "k": "K7-V033", "karte": "vorsilben_gross", "typ": "FD", "s": 3, "y": "auswahl", "regel": BUE,
        "text": "Ein Kind rechnet 7 TB in Byte um. Zeile 1: Tera bedeutet 10⁹. "
                "Zeile 2: Also sind 7 TB = 7 · 10⁹ Byte. "
                "Zeile 3: Das sind 7 000 Millionen Byte. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 0,
        "h": "Tera steht über Giga (10⁹).",
        "w": "Zeile 1 ist falsch: Tera bedeutet 10¹², nicht 10⁹. Die Zeilen 2 und 3 folgen richtig aus dem Fehler "
             "(7 · 10⁹ sind 7 000 Millionen). Richtig wären 7 · 10¹² Byte, also 7 000 000 Millionen.",
        "fehlbilder": [
            {"index": 1, "antwort": "In Zeile 2", "beschreibung": "diese Zeile folgt richtig aus Zeile 1: die Vorsilbe wird durch die Potenz ersetzt"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2: 7 · 10⁹ sind 7 000 · 10⁶"},
        ],
    },
    # ---------------- negativer_exponent ----------------
    {
        "k": "K7-V034", "karte": "negativer_exponent", "typ": "LW", "s": 1, "y": "luecken", "regel": POT,
        "text": "Die Zahl 0,000001 schreibt man als 10 hoch minus ①. "
                "Zwischen dem Komma und der 1 stehen ② Nullen. "
                "Eine 10 000-mal so große Zahl schreibt man als 10 hoch minus ③.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["6", "L1 - 1", "L1 - 4"], "erwartet": [6, 5, 2], "entscheidend": 2,
        "h": "Die Stelle der 1 nach dem Komma ist der Exponent ohne Minus.",
        "w": "Die 1 steht an der 6. Stelle nach dem Komma: 10⁻⁶. Davor stehen 5 Nullen. "
             "Mal 10 000 = mal 10⁴ macht aus 10⁻⁶ die Zahl 10⁻².",
        "fehlbilder": [{"luecke": 2, "antwort": 6, "rechnung": "L1", "beschreibung": "die 1 mitgezählt"},
                       {"luecke": 3, "antwort": 10, "rechnung": "L1 + 4", "beschreibung": "zu 6 noch 4 addiert statt 4 abzuziehen"}],
    },
    {
        "k": "K7-V035", "karte": "negativer_exponent", "typ": "ZW", "s": 2, "y": "zahl", "regel": POT,
        "text": "Wie viele Nullen stehen bei 10⁻⁴ zwischen dem Komma und der 1? "
                "Weg A: vom Exponenten 1 abziehen. Weg B: die Zahl hinschreiben und die Nullen zählen.",
        "c": "4 - 1", "erwartet": 3,
        "h": "Schreibe 10⁻¹, 10⁻² und 10⁻³ als Dezimalzahlen hin.",
        "w": "Weg A: 4 − 1 = 3. Weg B: 10⁻⁴ = 0,0001, zwischen Komma und 1 stehen 3 Nullen.",
        "fehlbilder": [{"antwort": 4, "rechnung": "4", "beschreibung": "die Stelle der 1 mitgezählt"},
                       {"antwort": 5, "rechnung": "4 + 1", "beschreibung": "eins addiert statt abgezogen"}],
    },
    {
        "k": "K7-V036", "karte": "negativer_exponent", "typ": "FD", "s": 3, "y": "auswahl", "regel": POT,
        "text": "Ein Kind sagt zu 10⁻² : Zeile 1: Der Exponent ist negativ. "
                "Zeile 2: Also ist die Zahl negativ. "
                "Zeile 3: Deshalb ist 10⁻² = −0,01. "
                "In welcher Zeile steckt der erste Fehler?",
        "a": ["In Zeile 1", "In Zeile 2", "In Zeile 3"], "richtig": 1,
        "h": "Wie ist 10⁻¹ aus 10⁰ = 1 entstanden?",
        "w": "Zeile 1 stimmt. Zeile 2 ist falsch: Ein negativer Exponent macht die Zahl klein, nicht negativ. "
             "10⁻² = 0,01. Zeile 3 folgt richtig aus Zeile 2.",
        "fehlbilder": [
            {"index": 0, "antwort": "In Zeile 1", "beschreibung": "diese Zeile ist richtig, sie liest nur den Exponenten ab"},
            {"index": 2, "antwort": "In Zeile 3", "beschreibung": "diese Zeile folgt richtig aus Zeile 2; der Fehler steht schon in Zeile 2"},
        ],
    },
    # ---------------- klein_wissenschaftlich ----------------
    {
        "k": "K7-V037", "karte": "klein_wissenschaftlich", "typ": "LW", "s": 1, "y": "luecken", "regel": POT,
        "text": "Die Zahl 0,00036 schreibt man wissenschaftlich als 3,6 · 10 hoch minus ①. "
                "Die zehnmal so große Zahl hat bei gleicher Ziffernfolge den Exponenten minus ②. "
                "Die tausendmal kleinere Zahl hat den Exponenten minus ③.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["4", "L1 - 1", "L1 + 3"], "erwartet": [4, 3, 7], "entscheidend": 1,
        "h": "Zähle die Stellen, die das Komma nach rechts wandert.",
        "w": "0,00036 = 3,6 · 10⁻⁴ (das Komma wandert 4 Stellen). Zehnmal so groß ist 0,0036 = 3,6 · 10⁻³. "
             "Tausendmal kleiner ist 0,00000036 = 3,6 · 10⁻⁷.",
        "fehlbilder": [{"luecke": 1, "antwort": 3, "rechnung": "3", "beschreibung": "nur die Nullen nach dem Komma gezählt"},
                       {"luecke": 2, "antwort": 5, "rechnung": "L1 + 1", "beschreibung": "in die falsche Richtung angepasst"}],
    },
    {
        "k": "K7-V038", "karte": "klein_wissenschaftlich", "typ": "UM", "s": 2, "y": "zahl", "regel": POT,
        "text": "Eine Zahl ist 2,5 · 10⁻³. Wie viele Stellen hat diese Zahl nach dem Komma?",
        "c": "3 + 1", "erwartet": 4,
        "h": "Schreibe die Zahl als Dezimalzahl hin.",
        "w": "2,5 · 10⁻³ = 0,0025. Die 2 steht an der 3. Stelle, die 5 an der 4. Stelle: 4 Stellen nach dem Komma.",
        "fehlbilder": [{"antwort": 3, "rechnung": "3", "beschreibung": "nur den Exponenten genommen"},
                       {"antwort": 2, "rechnung": "2", "beschreibung": "nur die Ziffern 2 und 5 gezählt, die Nullen nicht"}],
    },
    {
        "k": "K7-V039", "karte": "klein_wissenschaftlich", "typ": "BR", "s": 2, "y": "auswahl", "regel": POT,
        "text": "Welche Dezimalzahl gehört zu 8,4 · 10⁻⁵?",
        "a": ["0,000084", "0,00084", "0,0000084", "840 000"], "richtig": 0,
        "a_rechnung": ["84/10**6", "84/10**5", "84/10**7", "840000"], "a_wert": 0.000084,
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
        "text": "Milli bedeutet 10⁻³, Mikro bedeutet 10⁻⁶. Ein Millimeter besteht aus ① Mikrometern. "
                "Ein Bakterium ist 2 µm lang. Hintereinander passen ② Bakterien in einen Millimeter "
                "und ③ Bakterien in einen Meter.",
        "schablone": "① = □; ② = □; ③ = □",
        "c": ["10 ** 3", "L1 // 2", "L2 * 1000"], "erwartet": [1000, 500, 500000], "entscheidend": 1,
        "h": "Vergleiche die beiden Exponenten.",
        "w": "10⁻³ : 10⁻⁶ = 10³ = 1 000, ein Millimeter hat also 1 000 µm. 1 000 : 2 = 500 Bakterien in einem Millimeter. "
             "Ein Meter hat 1 000 mm: 500 · 1 000 = 500 000 Bakterien.",
        "fehlbilder": [{"luecke": 1, "antwort": 1000000, "rechnung": "10 ** 6", "beschreibung": "Mikrometer mit Metern verglichen"},
                       {"luecke": 2, "antwort": 2000, "rechnung": "L1 * 2", "beschreibung": "mit 2 malgenommen statt durch 2 geteilt"}],
    },
    {
        "k": "K7-V041", "karte": "vorsilben_klein", "typ": "AN", "s": 2, "y": "zahl", "regel": BUE,
        "text": "Eine Schutzfolie ist 250 nm dick. Wie viele solche Folien ergeben übereinander genau 1 mm?",
        "c": "10 ** 6 // 250", "erwartet": 4000, "einheit": "Folien",
        "h": "Rechne beide Längen in Nanometer um.",
        "w": "1 mm = 10⁻³ m = 10⁶ nm. 10⁶ : 250 = 4 000 Folien.",
        "fehlbilder": [{"antwort": 4, "rechnung": "1000 / 250", "beschreibung": "Nano wie Mikro behandelt (1 000 statt 10⁶)"},
                       {"antwort": 4000000, "rechnung": "10 ** 9 // 250", "beschreibung": "Millimeter und Meter verwechselt"}],
    },
    {
        "k": "K7-V042", "karte": "vorsilben_klein", "typ": "VW", "s": 1, "y": "auswahl", "regel": BUE,
        "text": "Eine Messung dauert 7 ms. Welche Rechnung gibt die Zeit in Sekunden?",
        "a": ["7 · 10⁻³ s", "7 · 10³ s", "7 · 10⁻² s", "7 · 10⁻⁶ s"], "richtig": 0,
        "a_rechnung": ["7/1000", "7*1000", "7/100", "7/10**6"], "a_wert": 0.007,
        "h": "Milli bedeutet 10⁻³.",
        "w": "7 ms = 7 · 10⁻³ s = 0,007 s.",
        "fehlbilder": [
            {"index": 1, "antwort": "7 · 10³ s", "beschreibung": "Vorsilbe als Vergrößerung gelesen"},
            {"index": 2, "antwort": "7 · 10⁻² s", "beschreibung": "Milli mit Zenti verwechselt, das ergibt 0,07 s"},
            {"index": 3, "antwort": "7 · 10⁻⁶ s", "beschreibung": "Milli mit Mikro verwechselt"},
        ],
    },
    # ---------------- vergleichen_pruefen ----------------
    {
        "k": "K7-V043", "karte": "vergleichen_pruefen", "typ": "VW", "s": 1, "y": "auswahl", "regel": POT,
        "text": "Du sollst 3 · 10⁷ und 8 · 10⁶ vergleichen (beide in wissenschaftlicher Schreibweise). "
                "Welches Vorgehen führt sicher zum Ziel?",
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
        "fehlbilder": [{"antwort": 100, "rechnung": "10 ** 5 // 10 ** 3", "beschreibung": "nur die Zehnerpotenzen geteilt"},
                       {"antwort": 500, "rechnung": "200000 // 400", "beschreibung": "bei 4 · 10³ eine Null vergessen"}],
    },
    {
        "k": "K7-V045", "karte": "vergleichen_pruefen", "typ": "AN", "s": 2, "y": "zahl", "regel": POT,
        "text": "Zwei Landkreise werden zusammengelegt. Der eine hat 3 · 10⁵ Einwohner, der andere 7 · 10⁴. "
                "Wie viele Einwohner hat der neue Landkreis?",
        "c": "3 * 10 ** 5 + 7 * 10 ** 4", "erwartet": 370000, "einheit": "Einwohner",
        "h": "Schreibe beide Zahlen zuerst normal hin.",
        "w": "3 · 10⁵ = 300 000 und 7 · 10⁴ = 70 000. Zusammen sind das 370 000 Einwohner.",
        "fehlbilder": [{"antwort": 1000000, "rechnung": "(3 + 7) * 10 ** 5", "beschreibung": "die Zahlen davor addiert und die erste Zehnerpotenz behalten"},
                       {"antwort": 307000, "rechnung": "3 * 10 ** 5 + 7 * 10 ** 3", "beschreibung": "die zweite Zahl mit 10³ gelesen"}],
    },
]
