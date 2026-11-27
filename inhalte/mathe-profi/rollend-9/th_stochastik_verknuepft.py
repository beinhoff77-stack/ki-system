T = "stochastik.verknuepft"
AN = "id.daten.anteil"
BA = "id.zahlen.bausteine"
ST = "id.daten.stufen"
def teiler(n):
    return {d for d in range(1, n + 1) if n % d == 0}
TAF = ["", "B", "nicht B", "Summe"]

# ───────── elemente ─────────
neu(T, "elemente", "verfahren_waehlen", W(
    "Du sollst die Menge A aller Teiler von 18 vollständig aufzählen. Welche Vorgehensweise führt sicher zum Ziel?",
    "Jede Zahl von 1 bis 18 prüfen: Geht 18 : n ohne Rest auf? Alle Zahlen, bei denen das gilt, aufschreiben.",
    [("Nur die Zahlen von 1 bis 9 prüfen, denn größere Zahlen können keine Teiler von 18 sein.", "die Zahl 18 selbst als Teiler vergessen: Jede Zahl ist Teiler ihrer selbst", None, lambda: 18 % 18 == 0),
     ("Die Vielfachen von 18 aufschreiben: 18, 36, 54, …", "Teiler und Vielfache verwechselt", None, lambda: 36 not in teiler(18)),
     ("Nur die Primfaktoren 2 und 3 aufschreiben.", "nur die Primfaktoren genannt: Teiler wie 6, 9 und 18 fehlen dann", None, lambda: {2, 3} != teiler(18))],
    "Ein Teiler geht ohne Rest auf. Welche Zahlen kommen als Teiler überhaupt in Frage?",
    "Ein Teiler n von 18 geht ohne Rest auf, also 18 : n ohne Rest. Prüft man alle n von 1 bis 18, entdeckt man 1, 2, 3, 6, 9 und 18. So wird keiner vergessen, auch 18 selbst nicht. Vielfache sind etwas anderes, und die Primfaktoren 2 und 3 sind nur zwei der Teiler.",
    lambda: {n for n in range(1, 19) if 18 % n == 0} == teiler(18) == {1, 2, 3, 6, 9, 18}), g="erkennen", regel=BA)
neu(T, "elemente", "umkehren", Z(
    "Die Menge A enthält alle Vielfachen von 6, die höchstens so groß sind wie die natürliche Zahl n. Die Vielfachen beginnen bei 6. A hat genau 5 Elemente. Welches ist der kleinste mögliche Wert von n?",
    30, "6 * 5", lambda: min(n for n in range(1, 100) if len([k for k in range(6, n + 1, 6)]) == 5),
    "Schreibe die ersten Vielfachen von 6 auf. Das fünfte ist die kleinste mögliche Obergrenze.",
    "Die Vielfachen von 6 sind 6, 12, 18, 24, 30. Das fünfte Vielfache ist 5 · 6 = 30. Bei n = 30 hat A genau fünf Elemente, bei n = 29 nur vier.",
    [(36, None, "das sechste Vielfache genommen", "6 * 6"), (5, None, "die Zahl der Elemente als Obergrenze genommen", "5"), (35, None, "die größte mögliche Obergrenze genannt, nicht die kleinste", "6 * 5 + 5")]), regel=None)
neu(T, "elemente", "fehler_detektiv", FD(
    "Anna bestimmt A = die Primzahlen zwischen 10 und 30.",
    [("Zu prüfen sind die Zahlen von 11 bis 29.", True, None),
     ("Prim sind 11, 13, 17, 19, 21, 23 und 29.", False, None),
     ("A hat deshalb 7 Elemente.", False, True)],
    "Prüfe jede genannte Zahl anhand der Definition einer Primzahl.",
    "21 = 3 · 7 ist keine Primzahl. Richtig ist A = {11; 13; 17; 19; 23; 29} mit 6 Elementen. Zeile 3 folgt aus der falschen Zeile 2."), regel=BA)

# ───────── schnitt ─────────
neu(T, "schnitt", "lueckenweg", L(
    "A = die Teiler von 18 (6 Elemente), B = die Teiler von 24 (8 Elemente). A ∩ B enthält die gemeinsamen Teiler und hat ① Elemente. Dann hat A ∪ B ② Elemente. Also liegen nur in A ③ Elemente.",
    KOMM(3), [4, 10, 2], ["4", "6 + 8 - {1}", "6 - {1}"],
    [lambda: len(teiler(18) & teiler(24)), lambda: len(teiler(18) | teiler(24)), lambda: len(teiler(18) - teiler(24))],
    "Schreibe zuerst die Teiler von 18 und die Teiler von 24 auf und streiche, was in beiden steht.",
    "Teiler von 18: 1, 2, 3, 6, 9, 18. Teiler von 24: 1, 2, 3, 4, 6, 8, 12, 24. Gemeinsam sind 1, 2, 3, 6, das sind 4 Zahlen. A ∪ B: 6 + 8 − 4 = 10. Nur in A: 6 − 4 = 2 (9 und 18).",
    {0: [(6, None, "alle Elemente von A gezählt", "6"), (8, None, "alle Elemente von B gezählt", "8")],
     1: [(14, None, "die Elemente beider Mengen ohne Abzug der gemeinsamen addiert", "6 + 8")],
     2: [(4, None, "die gemeinsamen Elemente statt der Elemente nur in A genannt", "{1}")]}), regel=None)
neu(T, "schnitt", "bruecke", Z(
    "Die Tabelle zeigt für die Zahlen von 1 bis 8, ob sie in A (gerade Zahlen) und ob sie in B (durch 3 teilbare Zahlen) liegen. Wie viele dieser Zahlen liegen in A, aber nicht in B?",
    3, "4 - 1", lambda: len([n for n in range(1, 9) if n % 2 == 0 and n % 3 != 0]),
    "Lies zuerst alle Zahlen in A ab. Streiche dann die, die auch in B liegen.",
    "In A liegen 2, 4, 6 und 8. In B liegt von 1 bis 8 nur die 3 und die 6. Die 6 liegt in beiden. Nur in A liegen 2, 4 und 8, also 3 Zahlen.",
    [(4, None, "alle Zahlen in A gezählt", "4"), (1, None, "nur die Zahl gezählt, die in beiden liegt", "1"), (5, None, "alle Zahlen in A oder B gezählt", "4 + 2 - 1")],
    grafik=TAB(["Zahl", "1", "2", "3", "4", "5", "6", "7", "8"], ["in A", "nein", "ja", "nein", "ja", "nein", "ja", "nein", "ja"], ["in B", "nein", "nein", "ja", "nein", "nein", "ja", "nein", "nein"])), g="darstellung", regel=None)
neu(T, "schnitt", "umkehren", Z(
    "A besteht aus den Vielfachen von 4 bis 40. B besteht aus den Vielfachen einer natürlichen Zahl k bis 40, wobei die Vielfachen bei k beginnen und k mindestens 2 ist. B hat genau 4 Elemente, und es gilt A ∩ B = {20; 40}. Bestimme k.",
    10, "40 / 4", lambda: [k for k in range(2, 41) if len(range(k, 41, k)) == 4 and {m for m in range(k, 41, k)} & {m for m in range(4, 41, 4)} == {20, 40}][0],
    "Wie groß ist k, wenn B vier Vielfache bis 40 hat? Prüfe dann, ob 20 und 40 dazugehören und ob die Zahlen in B auch durch 4 teilbar sind.",
    "Vier Vielfache bis 40 haben nur k = 10 (10, 20, 30, 40) und k = 9 (9, 18, 27, 36). Für k = 9 liegt nur 36 in A. Für k = 10 liegen 20 und 40 in A. Also ist k = 10.",
    [(4, None, "die Zahl der Elemente von B genannt", "4"), (20, None, "das kleinste gemeinsame Element genommen", "20"), (5, None, "k passt zum Schnitt, aber B hätte dann acht Elemente", "40 / 8")]), g="rueckwaerts", regel=None)

# ───────── verknuepfen ─────────
neu(T, "verknuepfen", "lueckenweg", L(
    "Aus den Zahlen von 1 bis 30 wird eine gezogen. A: „Die Zahl ist durch 4 teilbar.“ (7 Zahlen) B: „Die Zahl ist durch 6 teilbar.“ (5 Zahlen) In A ∩ B liegen die Vielfachen von 12, das sind ① Zahlen. Dann liegen in A ∪ B ② Zahlen. Also gehören zu keinem der beiden Ereignisse ③ Zahlen.",
    KOMM(3), [2, 10, 20], ["30 // 12", "7 + 5 - {1}", "30 - {2}"],
    [lambda: len([n for n in range(1, 31) if n % 4 == 0 and n % 6 == 0]), lambda: len([n for n in range(1, 31) if n % 4 == 0 or n % 6 == 0]), lambda: len([n for n in range(1, 31) if n % 4 and n % 6])],
    "Zähle zuerst die Zahlen, die in beiden Ereignissen liegen. Sie wurden bei 7 + 5 mehrfach mitgezählt.",
    "Durch 4 und 6 teilbar sind 12 und 24, das sind 2 Zahlen. A ∪ B: 7 + 5 − 2 = 10. Weder A noch B: 30 − 10 = 20.",
    {0: [(1, None, "nur die Zahl 12 gefunden und die Zahl 24 übersehen", "1")],
     1: [(12, None, "die Elemente von A und B ohne Abzug addiert", "7 + 5")],
     2: [(23, None, "nur die Zahlen aus A abgezogen", "30 - 7"), (18, None, "die Zahl der gemeinsamen Elemente nicht beachtet", "30 - 12")]}), regel=None)
neu(T, "verknuepfen", "zwei_wege", Z(
    "Aus den Zahlen von 1 bis 40 wird eine gezogen. A: „Die Zahl ist durch 3 teilbar.“ B: „Die Zahl ist durch 5 teilbar.“ Wie viele Zahlen gehören weder zu A noch zu B? Weg A: Prüfe die Zahlen von 1 bis 40 der Reihe nach. Weg B: Zähle A, B und A ∩ B und nimm das Gegenereignis.",
    21, "40 - (13 + 8 - 2)", lambda: len([n for n in range(1, 41) if n % 3 and n % 5]),
    "Beide Wege müssen dieselbe Anzahl ergeben. Beachte die Zahlen, die in A und in B liegen.",
    "Weg A: Weder durch 3 noch durch 5 teilbar sind 1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38. Das sind 21 Zahlen. Weg B: In A liegen 13 Zahlen, in B liegen 8 Zahlen, in A ∩ B liegen 2 Zahlen (15 und 30). In A ∪ B liegen 13 + 8 − 2 = 19 Zahlen. Also 40 − 19 = 21.",
    [(19, None, "A und B abgezogen, aber die doppelt gezählten Zahlen nicht wieder dazugerechnet", "40 - 13 - 8"), (27, None, "nur die Zahlen aus A abgezogen", "40 - 13"), (17, None, "die gemeinsamen Zahlen zusätzlich abgezogen", "40 - 13 - 8 - 2")]), regel=None)
neu(T, "verknuepfen", "fehler_detektiv", FD(
    "Aus den Zahlen von 1 bis 20 wird zufällig eine gezogen, jede Zahl mit derselben Wahrscheinlichkeit. A: „durch 2 teilbar“, B: „durch 3 teilbar“. Ben bestimmt P(A und nicht B).",
    [("A hat 10 Elemente, B hat 6 Elemente.", True, None),
     ("A ∩ B besteht aus 6, 12 und 18.", True, None),
     ("Nur in A liegen 10 − 3 = 7 Zahlen.", True, None),
     ("P(A und nicht B) = 7 : 20 = 0,45.", False, None)],
    "Wo steckt der erste Rechenfehler? Prüfe jede Zeile einzeln, beginne oben.",
    "In den Zeilen 1 bis 3 stimmt alles. In Zeile 4 ist 7 : 20 = 0,35 und nicht 0,45."), regel=None)

# ───────── additionssatz ─────────
neu(T, "additionssatz", "lueckenweg", L(
    "Von 50 Kindern spielen 22 Fußball (A), 16 Tennis (B) und 8 beides. Mindestens eine der beiden Sportarten spielen ① Kinder. Dann spielen keine der beiden Sportarten ② Kinder. Also gilt für ein zufällig gewähltes Kind P(weder A noch B) = ③ %.",
    KOMM(3), [30, 20, 40], ["22 + 16 - 8", "50 - {1}", "{2} * 100 / 50"],
    ["(22 - 8) + (16 - 8) + 8", "(50 - 22) - (16 - 8)", "(50 - 22 - 16 + 8) / 50 * 100"],
    "Der Additionssatz: P(A ∪ B) = P(A) + P(B) − P(A ∩ B). Das Gegenereignis zu „mindestens eine“ ist „keine“.",
    "A ∪ B: 22 + 16 − 8 = 30 Kinder. Keine Sportart: 50 − 30 = 20 Kinder. P = 20 : 50 = 0,4 = 40 %.",
    {0: [(38, None, "die Kinder beider Sportarten ohne Abzug der doppelt gezählten addiert", "22 + 16")],
     1: [(12, None, "von allen Kindern die Summe ohne Abzug abgezogen", "50 - (22 + 16)")],
     2: [(60, None, "den Anteil für mindestens eine Sportart statt für keine angegeben", "{1} * 100 / 50")]}), regel=AN)
neu(T, "additionssatz", "anwenden", Z(
    "In einer Umfrage nutzen 62 % der Befragten einen Streamingdienst für Filme, 45 % nutzen einen für Musik, und 30 % nutzen beide. Wie viel Prozent der Befragten nutzen keinen der beiden Dienste?",
    23, "100 - (62 + 45 - 30)", lambda: F(100) - (F(62) + F(45) - F(30)),
    "Wer beide Dienste nutzt, wird bei 62 + 45 doppelt gezählt. Ziehe das ab, bevor du das Gegenereignis bildest.",
    "Mindestens einen Dienst nutzen 62 % + 45 % − 30 % = 77 %. Keinen nutzen 100 % − 77 % = 23 %.",
    [(77, None, "den Anteil für mindestens einen Dienst angegeben", "62 + 45 - 30"), (-7, None, "vom Ganzen beide Anteile abgezogen, ohne die Überschneidung zu beachten", "100 - 62 - 45"), (-37, None, "von 100 die Summe der drei Prozentwerte abgezogen", "100 - 62 - 45 - 30")], "%"), g="einkleidung", regel=None)
neu(T, "additionssatz", "umkehren", Z(
    "Für zwei Ereignisse A und B gilt P(A) = 0,6, P(B) = 0,5 und P(Ā ∩ B̄) = 0,1. Das heißt, mit der Wahrscheinlichkeit 0,1 tritt weder A noch B ein. Berechne P(A ∩ B).",
    0.2, "0.6 + 0.5 - (1 - 0.1)", lambda: F(6, 10) + F(5, 10) - (1 - F(1, 10)),
    "Was sagt P(Ā ∩ B̄) über P(A ∪ B)? Welche Regel verbindet das mit P(A ∩ B)?",
    "P(A ∪ B) = 1 − 0,1 = 0,9. Aus 0,9 = 0,6 + 0,5 − P(A ∩ B) folgt P(A ∩ B) = 1,1 − 0,9 = 0,2.",
    [(0.9, None, "P(A ∪ B) angegeben", "1 - 0.1"), (0.1, None, "die gegebene Wahrscheinlichkeit für weder noch übernommen", "0.1"), (1.1, None, "P(A) und P(B) addiert", "0.6 + 0.5")]), g="rueckwaerts", regel=None)

# ───────── venn ─────────
neu(T, "venn", "lueckenweg", L(
    "In einer Klasse mit 26 Kindern lesen 14 gern Krimis (A), 9 lesen gern Fantasy (B), und 4 lesen beides. Im Venn-Diagramm stehen nur im Kreis A ① Kinder. Dann stehen nur im Kreis B ② Kinder. Also stehen außerhalb beider Kreise ③ Kinder.",
    KOMM(3), [10, 5, 7], ["14 - 4", "9 - 4", "26 - {1} - 4 - {2}"],
    ["10", "5", "26 - (14 + 9 - 4)"],
    "Die vier Kinder im Schnitt zählen zu A und zu B. Zähle sie nur einmal.",
    "Nur A: 14 − 4 = 10. Nur B: 9 − 4 = 5. In den Kreisen liegen 10 + 4 + 5 = 19 Kinder, außerhalb liegen 26 − 19 = 7 Kinder.",
    {0: [(14, None, "alle Kinder aus A genommen, auch die im Schnitt", "14")],
     1: [(9, None, "alle Kinder aus B genommen, auch die im Schnitt", "9")],
     2: [(12, None, "von allen Kindern nur die aus A abgezogen", "26 - 14"), (3, None, "von allen Kindern die Summe von A und B abgezogen, ohne den Schnitt zurückzugeben", "26 - 14 - 9")]}), regel=None)
neu(T, "venn", "bruecke", Z(
    "Die Tabelle zählt, wie viele Kinder einer Klasse in welchem Bereich eines Venn-Diagramms liegen. A: „spielt Fußball“, B: „schwimmt“. Wie viele Kinder gehören nicht zu B?",
    14, "9 + 5", lambda: 25 - (4 + 7),
    "Nicht zu B gehören die Kinder, die nur in A liegen, und die Kinder außerhalb beider Kreise.",
    "Nicht in B liegen die Bereiche „nur A“ und „keines“: 9 + 5 = 14 Kinder. Probe: Zu B gehören 4 + 7 = 11 Kinder, und 25 − 11 = 14.",
    [(13, None, "nur die Kinder in A gezählt", "9 + 4"), (5, None, "nur den Bereich außerhalb beider Kreise gezählt", "5"), (18, None, "alle Bereiche außer „nur B“ gezählt", "9 + 4 + 5")],
    grafik=TAB(["Bereich", "nur A", "A und B", "nur B", "keines"], ["Kinder", "9", "4", "7", "5"])), g="darstellung", regel=None)
neu(T, "venn", "anwenden", Z(
    "Bei einer Befragung von 40 Personen mögen 26 Pizza, 22 mögen Pasta, und 5 mögen keins von beiden. Wie viele Personen mögen beides?",
    13, "26 + 22 - (40 - 5)", lambda: 26 + 22 - (40 - 5),
    "Wie viele Personen mögen mindestens eins von beiden? Was passiert beim Addieren von 26 und 22?",
    "Mindestens eins mögen 40 − 5 = 35 Personen. Bei 26 + 22 = 48 werden die Personen, die beides mögen, doppelt gezählt: 48 − 35 = 13.",
    [(35, None, "die Zahl der Personen für mindestens eins angegeben", "40 - 5"), (48, None, "die Summe beider Gruppen ohne Abzug genommen", "26 + 22"), (9, None, "nur die Personen gezählt, die Pasta, aber keine Pizza mögen", "40 - 5 - 26")]), g="transfer", regel=None)

# ───────── mengen_verstehen ─────────
neu(T, "mengen_verstehen", "verfahren_waehlen", W(
    "Die Menge A hat 8 Elemente und die Menge B hat 5 Elemente. Du sollst herausfinden, wie viele Elemente A ∪ B haben kann, wenn du sonst nichts weißt. Welche Vorgehensweise führt zum Ziel?",
    "Die kleinste und die größte mögliche Überschneidung betrachten: Liegt B ganz in A, sind es 8 + 5 − 5 = 8 Elemente. Ohne gemeinsames Element sind es 8 + 5 = 13. Also mindestens 8 und höchstens 13 Elemente.",
    [("Die Elemente beider Mengen addieren: A ∪ B hat immer 13 Elemente.", "die Überschneidung nicht beachtet", None, lambda: True),
     ("Nur die kleinere Menge betrachten: A ∪ B hat höchstens 5 Elemente.", "die kleinere Menge als Obergrenze genommen", None, lambda: True),
     ("Die Zahlen der Elemente multiplizieren: A ∪ B hat 8 · 5 = 40 Elemente.", "die Zahlen der Elemente multipliziert", None, lambda: 8 * 5 == 40)],
    "Fange mit der kleinstmöglichen und der größtmöglichen Überschneidung an.",
    "Liegt B ganz in A, dann hat A ∪ B nur 8 Elemente. Haben A und B kein gemeinsames Element, dann hat A ∪ B 8 + 5 = 13 Elemente. Dazwischen ist alles möglich. Die Vereinigung hat also mindestens 8 und höchstens 13 Elemente.",
    lambda: {8 + 5 - k for k in range(0, 6)} == set(range(8, 14))), g="erkennen", regel=None)
neu(T, "mengen_verstehen", "umkehren", Z(
    "A hat 9 Elemente, B hat 8 Elemente, und A ∪ B hat 14 Elemente. Wie viele Elemente hat A ∩ B?",
    3, "9 + 8 - 14", lambda: len(set(range(1, 10)) & set(range(7, 15))),
    "Bei 9 + 8 werden die Elemente in A ∩ B doppelt gezählt.",
    "Es gilt 14 = 9 + 8 − |A ∩ B|. Also ist |A ∩ B| = 17 − 14 = 3.",
    [(17, None, "die Elemente von A und B addiert", "9 + 8"), (5, None, "von den Elementen der Vereinigung die Elemente von A abgezogen", "14 - 9"), (6, None, "von den Elementen der Vereinigung die Elemente von B abgezogen", "14 - 8")]), regel=None)
neu(T, "mengen_verstehen", "fehler_detektiv", FD(
    "A hat 12 Elemente, B hat 7 Elemente, A ∩ B hat 4 Elemente. Jana bestimmt, wie viele Elemente A ∪ B hat.",
    [("Nur in A liegen 12 − 4 = 8 Elemente.", True, None),
     ("Nur in B liegen 7 − 4 = 3 Elemente.", True, None),
     ("A ∪ B besteht nur aus den Elementen, die nur in A oder nur in B liegen.", False, None),
     ("Also hat die Vereinigung 11 Elemente.", False, True)],
    "Prüfe jede Zeile gegen die Angaben: Welche Elemente gehören zu A ∪ B?",
    "Zeile 3 vergisst die 4 Elemente von A ∩ B. Richtig ist 8 + 3 + 4 = 15. Zeile 4 folgt aus der falschen Zeile 3: 8 + 3 = 11."), regel=None)

# ───────── vierfeld ─────────
neu(T, "vierfeld", "lueckenweg", L(
    "Von 120 Gästen eines Festes haben 70 gegessen (A), 45 von ihnen haben auch getrunken (B). Insgesamt haben 60 getrunken. In der Vierfeldertafel steht bei „A und nicht B“ die Zahl ①. Dann ist die Summe der drei Innenfelder „A und nicht B“, „A und B“ und „nicht A und B“ gleich ②. Also steht bei „weder A noch B“ die Zahl ③.",
    KOMM(3), [25, 85, 35], ["70 - 45", "{1} + 45 + (60 - 45)", "120 - {2}"],
    ["25", "70 + 60 - 45", "120 - (70 + 60 - 45)"],
    "Trage 120, 70, 60 und 45 in die Tafel ein. Rechne dann Zeile für Zeile.",
    "A und nicht B: 70 − 45 = 25. Nur B: 60 − 45 = 15. Die drei Innenfelder zusammen: 25 + 45 + 15 = 85. Weder noch: 120 − 85 = 35.",
    {0: [(70, None, "die ganze Zeile von A genommen", "70"), (15, None, "die Gäste genommen, die nur getrunken haben", "60 - 45")],
     1: [(130, None, "70 und 60 ohne Abzug der doppelt gezählten addiert", "70 + 60")],
     2: [(50, None, "von allen Gästen nur die Gäste mit A abgezogen", "120 - 70"), (60, None, "von allen Gästen nur die Gäste mit B abgezogen", "120 - 60")]}), regel=None)
neu(T, "vierfeld", "bruecke", Z(
    "Die Tabelle zählt 120 Schüler in vier getrennten Gruppen. A: „fährt mit dem Rad“, B: „fährt mit dem Bus“. Du trägst die Zahlen in eine Vierfeldertafel ein. Welche Zahl steht dann in der Summenzeile in der Spalte B?",
    40, "18 + 22", lambda: 120 - (32 + 48),
    "In der Spalte B stehen die Schüler mit B, ob mit oder ohne A.",
    "Zu B gehören die Gruppen „A und B“ und „nur B“: 18 + 22 = 40. Probe: 120 − 32 − 48 = 40.",
    [(22, None, "nur die Gruppe „nur B“ genommen", "22"), (18, None, "nur die Gruppe „A und B“ genommen", "18"), (50, None, "die Summe der Zeile von A genommen", "32 + 18")],
    grafik=TAB(["Gruppe", "nur A", "A und B", "nur B", "keines"], ["Schüler", "32", "18", "22", "48"])), g="darstellung", regel=None)
neu(T, "vierfeld", "umkehren", Z(
    "In einer Vierfeldertafel stehen 200 Personen. 120 haben das Merkmal A, 100 haben das Merkmal B, und 30 haben weder A noch B. Wie viele Personen haben A und B?",
    50, "120 + 100 - (200 - 30)", lambda: 120 + 100 - (200 - 30),
    "Was weißt du über die Zahl der Personen mit mindestens einem Merkmal? Was passiert beim Addieren von 120 und 100?",
    "A oder B haben 200 − 30 = 170 Personen. Aus 170 = 120 + 100 − x folgt x = 220 − 170 = 50.",
    [(170, None, "die Zahl der Personen mit mindestens einem Merkmal angegeben", "200 - 30"), (220, None, "die Zahlen für A und B addiert", "120 + 100"), (70, None, "nur die Personen mit A, aber ohne B berechnet", "170 - 100")]), g="rueckwaerts", regel=None)

# ───────── tafel_wkeit ─────────
neu(T, "tafel_wkeit", "lueckenweg", L(
    "Die Tafel zeigt 200 Personen. A: „fährt Rad“, B: „fährt Bus“. Eine Person wird zufällig ausgewählt, jede mit derselben Wahrscheinlichkeit. Dann ist P(A) = ① %. Weiter ist P(B) = ② %. Also ist P(A ∪ B) = ③ %.",
    KOMM(3), [40, 45, 67], ["80 * 100 / 200", "90 * 100 / 200", "{1} + {2} - 36 * 100 / 200"],
    ["(36 + 44) / 200 * 100", "(36 + 54) / 200 * 100", "(36 + 44 + 54) / 200 * 100"],
    "Lies die Summen am Rand der Tafel ab. Teile durch 200 und rechne in Prozent um.",
    "A hat die Summe 80: 80 : 200 = 40 %. B hat die Summe 90: 90 : 200 = 45 %. P(A ∩ B) = 36 : 200 = 18 %. P(A ∪ B) = 40 % + 45 % − 18 % = 67 %.",
    {0: [(80, None, "die Anzahl statt des Prozentwerts angegeben", "80")],
     1: [(90, None, "die Anzahl statt des Prozentwerts angegeben", "90")],
     2: [(85, None, "die beiden Prozentwerte ohne Abzug des Schnitts addiert", "{1} + {2}"), (18, None, "nur die Wahrscheinlichkeit für den Schnitt genannt", "36 * 100 / 200")]},
    grafik=TAB(TAF, ["A", "36", "44", "80"], ["nicht A", "54", "66", "120"], ["Summe", "90", "110", "200"])), regel=AN)
neu(T, "tafel_wkeit", "bruecke", Z(
    "Die Tafel zeigt Wahrscheinlichkeiten. Das Feld „?“ ist nicht gefüllt. Mit welcher Wahrscheinlichkeit trifft genau eines der beiden Ereignisse A und B zu, also A oder B, aber nicht beide? Gib das Ergebnis in Prozent an.",
    54, "(0.6 - 0.24 + 0.18) * 100", lambda: F(100) * ((F(42, 100) - F(24, 100)) + (F(6, 10) - F(24, 100))),
    "Das Feld „?“ ergibt sich aus der Zeilensumme von A. Genau eines heißt: „A und nicht B“ plus „nicht A und B“.",
    "Aus der Zeile A folgt „A und nicht B“ = 0,6 − 0,24 = 0,36. „Nicht A und B“ ist 0,18. Genau eines trifft zu mit 0,36 + 0,18 = 0,54, also mit 54 %.",
    [(78, None, "alle drei Felder genommen, auch das Feld für beide", "24 + 36 + 18"), (36, None, "nur das Feld „?“ genommen", "36"), (42, None, "die Wahrscheinlichkeit von B genommen", "42")],
    "%", grafik=TAB(TAF, ["A", "0,24", "?", "0,6"], ["nicht A", "0,18", "0,22", "0,4"], ["Summe", "0,42", "0,58", "1"])), g="darstellung", regel=None)
neu(T, "tafel_wkeit", "zwei_wege", Z(
    "Die Tafel zeigt 250 Personen. Eine Person wird zufällig ausgewählt, jede mit derselben Wahrscheinlichkeit. Mit welcher Wahrscheinlichkeit trifft genau eines der Merkmale A und B zu? Gib das Ergebnis in Prozent an. Weg A: Addiere die Felder „A und nicht B“ und „nicht A und B“. Weg B: Nimm P(A) + P(B) und ziehe P(A ∩ B) zweimal ab.",
    48, "(55 + 65) * 100 / 250", lambda: F(100) * (F(100, 250) + F(110, 250) - 2 * F(45, 250)),
    "Beide Wege müssen dasselbe Ergebnis liefern. Der Schnitt steckt in P(A) und in P(B).",
    "Weg A: 55 + 65 = 120, also 120 : 250 = 48 %. Weg B: P(A) = 100 : 250 = 40 %, P(B) = 110 : 250 = 44 %, P(A ∩ B) = 45 : 250 = 18 %. 40 % + 44 % − 2 · 18 % = 48 %.",
    [(66, None, "P(A ∪ B) statt genau eines angegeben", "(45 + 55 + 65) * 100 / 250"), (84, None, "P(A) und P(B) addiert", "(100 + 110) * 100 / 250"), (18, None, "nur P(A ∩ B) angegeben", "45 * 100 / 250")],
    "%", grafik=TAB(TAF, ["A", "45", "55", "100"], ["nicht A", "65", "85", "150"], ["Summe", "110", "140", "250"])), g="verknuepfen", regel=AN)

# ───────── bedingt ─────────
neu(T, "bedingt", "lueckenweg", L(
    "In einer Klasse mit 20 Kindern haben 12 ein Haustier (A). Von den zwölf Kindern mit Haustier sind drei Jungen. Insgesamt sind 15 Kinder Mädchen (B). Unter den Kindern mit Haustier sind ① Mädchen. Also ist P_A(B) = ② %. Dann ist P_B(A) = ③ %.",
    KOMM(3), [9, 75, 60], ["12 - 3", "{1} * 100 / 12", "{1} * 100 / 15"],
    ["12 - 3", "9 / 12 * 100", "9 / 15 * 100"],
    "Die Mädchen mit Haustier gehören zu A und zu B. P_A(B) betrachtet nur die Kinder mit Haustier. P_B(A) betrachtet nur die Mädchen.",
    "Mädchen mit Haustier: 12 − 3 = 9. P_A(B) = 9 : 12 = 75 %. P_B(A) = 9 : 15 = 60 %.",
    {0: [(3, None, "die Jungen mit Haustier genannt statt der Mädchen", "3"), (12, None, "alle Kinder mit Haustier genannt", "12")],
     1: [(25, None, "den Anteil der Jungen statt der Mädchen angegeben (3 von 12 Kindern mit Haustier)", "(12 - {1}) * 100 / 12"), (45, None, "durch alle 20 Kinder der Klasse geteilt", "{1} * 100 / 20")],
     2: [(75, None, "Bedingung und Ereignis vertauscht: durch die 12 Kinder mit Haustier statt durch die 15 Mädchen geteilt", "{1} * 100 / 12"), (45, None, "durch alle 20 Kinder der Klasse geteilt", "{1} * 100 / 20")]}), regel=AN)
neu(T, "bedingt", "bruecke", Z(
    "Das Baumdiagramm gehört zu einem zweistufigen Zufallsexperiment. Berechne P_B(A), also die Wahrscheinlichkeit für A unter der Bedingung B, als Dezimalzahl.",
    0.75, "0.5 * 0.6 / (0.5 * 0.6 + 0.5 * 0.2)", lambda: F(3, 10) / (F(3, 10) + F(1, 10)),
    "Welche beiden Pfade enden bei B? P_B(A) ist der Anteil des Pfads über A an diesen beiden Pfaden.",
    "Pfad A und B: 0,5 · 0,6 = 0,3. Pfad nicht A und B: 0,5 · 0,2 = 0,1. P(B) = 0,3 + 0,1 = 0,4. P_B(A) = 0,3 : 0,4 = 0,75.",
    [(0.6, None, "P_A(B) statt P_B(A) abgelesen", "0.6"), (0.3, None, "nur P(A ∩ B) angegeben", "0.5 * 0.6"), (0.5, None, "P(A) angegeben", "0.5")],
    grafik={"typ": "baum", "aeste": [{"text": "A", "p": "0,5", "aeste": [{"text": "B", "p": "0,6"}, {"text": "B̄", "p": "0,4"}]}, {"text": "Ā", "p": "0,5", "aeste": [{"text": "B", "p": "0,2"}, {"text": "B̄", "p": "0,8"}]}]}), g="darstellung", regel=ST)
neu(T, "bedingt", "fehler_detektiv", FD(
    "Die Tafel zeigt 200 Personen. Tom bestimmt P_A(B).",
    [("Die Bedingung ist B, also zählen nur die Personen mit B.", False, None),
     ("Das sind 80 Personen, davon haben 30 auch A.", True, True),
     ("P_A(B) = 30 : 80 = 0,375.", False, True)],
    "Lies die Zeilen der Reihe nach. Wofür steht die Schreibweise P_A(B)?",
    "Bei P_A(B) ist A die Bedingung, nur die 100 Personen mit A zählen. Richtig ist P_A(B) = 30 : 100 = 0,3. Die Zeilen 2 und 3 rechnen mit der falschen Gruppe, aber richtig weiter.",
    rueck={1: "Diese Zeile ist richtig, weil in der Tafel 80 Personen B haben und 30 von ihnen auch A. Sie gehört aber zur falschen Bedingung aus Zeile 1. Der erste Fehler steht früher."},
    grafik=TAB(TAF, ["A", "30", "70", "100"], ["nicht A", "50", "50", "100"], ["Summe", "80", "120", "200"])), regel=AN)

# ───────── rueckschluss ─────────
neu(T, "rueckschluss", "lueckenweg", L(
    "30 % der Äpfel einer Lieferung sind faul. Ein Test erkennt 90 % der faulen Äpfel, meldet aber auch 10 % der guten Äpfel fälschlich als faul. Stelle dir 1 000 Äpfel vor. Faul sind ① Äpfel. Dann meldet der Test ② dieser Äpfel. Also meldet er von den guten Äpfeln ③ fälschlich als faul.",
    KOMM(3), [300, 270, 70], ["1000 * 30 // 100", "{1} * 90 // 100", "(1000 - {1}) * 10 // 100"],
    ["300", "300 * 9 // 10", "700 // 10"],
    "Rechne mit 1 000 Äpfeln. 30 % davon sind faul, die anderen sind gut.",
    "Faul: 30 % von 1 000 = 300. Davon erkannt: 90 % von 300 = 270. Gut sind 700 Äpfel, davon werden 10 % = 70 fälschlich gemeldet.",
    {0: [(30, None, "den Prozentwert als Anzahl genommen", "30"), (700, None, "die guten Äpfel statt der faulen genommen", "1000 - 300")],
     1: [(90, None, "den Prozentwert als Anzahl genommen", "90"), (30, None, "10 % statt 90 % der faulen Äpfel genommen", "{1} * 10 // 100")],
     2: [(30, None, "10 % der faulen statt der guten Äpfel genommen", "{1} * 10 // 100"), (100, None, "10 % von allen Äpfeln genommen", "1000 * 10 // 100")]}), regel=ST)
neu(T, "rueckschluss", "anwenden", Z(
    "2 % der Bauteile einer Fertigung sind defekt. Ein Prüfgerät meldet 95 % der defekten Bauteile, aber auch 4 % der intakten Bauteile fälschlich als defekt. Stelle dir 10 000 Bauteile vor. Wie viele Bauteile meldet das Gerät insgesamt als defekt?",
    582, "10000 * 2 / 100 * 95 / 100 + (10000 - 10000 * 2 / 100) * 4 / 100", lambda: F(190) + F(392),
    "Rechne getrennt: die defekten Bauteile, die erkannt werden, und die intakten Bauteile, die fälschlich gemeldet werden.",
    "Defekt sind 200 Bauteile, davon werden 95 % = 190 gemeldet. Intakt sind 9 800, davon werden 4 % = 392 gemeldet. Insgesamt sind es 190 + 392 = 582.",
    [(190, None, "nur die richtig gemeldeten defekten Bauteile gezählt", "10000 * 2 / 100 * 95 / 100"), (392, None, "nur die fälschlich gemeldeten intakten Bauteile gezählt", "(10000 - 200) * 4 / 100"), (592, None, "alle defekten Bauteile statt der erkannten mit den falschen Meldungen addiert", "200 + 392")]), g="einkleidung", regel=ST)
neu(T, "rueckschluss", "zwei_wege", Z(
    "20 % der Bauteile einer Fertigung sind defekt. Ein Prüfgerät meldet 90 % der defekten Bauteile, aber auch 5 % der intakten Bauteile fälschlich als defekt. Bei einem Bauteil meldet das Gerät „defekt“. Mit welcher Wahrscheinlichkeit ist es wirklich defekt? Gib das Ergebnis in Prozent an, auf ganze Prozent gerundet. Weg A: Stelle dir 1 000 Bauteile vor und zähle. Weg B: Rechne mit den Pfaden eines Baumdiagramms.",
    82, RC(180 / 220 * 100, 0), lambda: F(round(F(2, 10) * F(9, 10) / (F(2, 10) * F(9, 10) + F(8, 10) * F(5, 100)) * 100)),
    "Beide Wege müssen auf ganze Prozent gerundet dasselbe ergeben. Überlege, welche Gruppe hier die Bedingung bildet.",
    "Weg A: Von 1 000 Bauteilen sind 200 defekt, 180 davon werden gemeldet. Von den 800 intakten werden 40 gemeldet. Gemeldet werden 220, davon sind 180 defekt: 180 : 220 ≈ 0,818. Weg B: 0,2 · 0,9 = 0,18 und 0,8 · 0,05 = 0,04. Dann ist 0,18 : 0,22 ≈ 0,818. Das sind etwa 82 %.",
    [(90, None, "die Erkennungsrate der defekten Bauteile angegeben", "180 * 100 / 200"), (18, None, "die Wahrscheinlichkeit für defekt und gemeldet angegeben", "180 * 100 / 1000"), (22, None, "den Anteil aller gemeldeten Bauteile angegeben", "220 * 100 / 1000")], "%"), g="verknuepfen", regel=ST)

# ───────── verstehen ─────────
neu(T, "verstehen", "verfahren_waehlen", W(
    "Für zwei Ereignisse gilt P(A) = 0,6 und P(B) = 0,7. Mehr ist nicht bekannt. Du sollst P(A ∩ B) so gut wie möglich eingrenzen. Welche Vorgehensweise führt zum Ziel?",
    "Mit dem Additionssatz und P(A ∪ B) ≤ 1 die untere Grenze bestimmen: 0,6 + 0,7 − 1 = 0,3. Die obere Grenze ist die kleinere der beiden Wahrscheinlichkeiten, 0,6. Ergebnis: 0,3 ≤ P(A ∩ B) ≤ 0,6. Der genaue Wert ist offen.",
    [("P(A) und P(B) malnehmen: P(A ∩ B) = 0,6 · 0,7 = 0,42.", "die Wahrscheinlichkeiten multipliziert, obwohl nicht bekannt ist, ob die Ereignisse unabhängig sind", None, lambda: True),
     ("Annehmen, dass A und B keine gemeinsamen Ergebnisse haben: P(A ∩ B) = 0.", "die Summe 0,6 + 0,7 = 1,3 über 1 nicht beachtet: dann müssen sich A und B überschneiden", None, lambda: F(6, 10) + F(7, 10) > 1),
     ("P(A) und P(B) addieren: P(A ∩ B) = 0,6 + 0,7 = 1,3.", "Schnitt und Vereinigung verwechselt: eine Wahrscheinlichkeit über 1 ist unmöglich", None, lambda: F(13, 10) > 1)],
    "P(A ∪ B) darf nicht größer als 1 sein. Was folgt daraus für den Schnitt? Und der Schnitt kann nie größer sein als jede der beiden Mengen.",
    "Aus P(A ∪ B) = 0,6 + 0,7 − P(A ∩ B) ≤ 1 folgt P(A ∩ B) ≥ 0,3. Außerdem liegt A ∩ B in A und in B, also ist P(A ∩ B) ≤ 0,6. Genaueres weißt du nicht, die Ereignisse könnten auch abhängig sein.",
    lambda: F(6, 10) + F(7, 10) - 1 == F(3, 10) and min(F(6, 10), F(7, 10)) == F(6, 10)), g="erkennen", regel=None)
neu(T, "verstehen", "zwei_wege", Z(
    "Ein fairer Würfel wird zweimal unabhängig geworfen, alle 36 Zahlenpaare sind gleich wahrscheinlich. Wie viele der 36 möglichen Zahlenpaare haben die Augensumme mindestens 10? Weg A: Schreibe die passenden Paare auf. Weg B: Nimm das Gegenereignis „Augensumme höchstens 9“.",
    6, "36 - 30", lambda: sum(1 for a in range(1, 7) for b in range(1, 7) if a + b >= 10),
    "Beide Wege müssen dieselbe Anzahl ergeben. Beim Gegenereignis zählst du die Paare nach der Augensumme.",
    "Weg A: Summe 10 mit (4|6), (5|5), (6|4), Summe 11 mit (5|6), (6|5), Summe 12 mit (6|6). Das sind 6 Paare. Weg B: Für die Summen 2 bis 9 gibt es 1 + 2 + 3 + 4 + 5 + 6 + 5 + 4 = 30 Paare. 36 − 30 = 6.",
    [(3, None, "nur die Paare mit der Augensumme genau 10 gezählt", "3"), (5, None, "die Paare mit der Augensumme 12 vergessen", "3 + 2"), (30, None, "die Anzahl des Gegenereignisses angegeben", "36 - 6")]), regel=None)
neu(T, "verstehen", "fehler_detektiv", FD(
    "In einer Urne liegen 3 rote und 2 blaue Kugeln. Es wird zweimal ohne Zurücklegen gezogen, bei jedem Zug hat jede noch vorhandene Kugel dieselbe Wahrscheinlichkeit. Mia bestimmt P(zwei rote Kugeln).",
    [("Beim ersten Zug ist die Wahrscheinlichkeit für rot 3/5.", True, None),
     ("Beim zweiten Zug liegen 4 Kugeln in der Urne, davon 3 rote: 3/4.", False, None),
     ("P(zwei rote Kugeln) = 3/5 · 3/4 = 9/20.", False, True)],
    "Lies die Zeilen der Reihe nach. Prüfe jede Zeile gegen die Beschreibung des Ziehens.",
    "Nach einer roten Kugel bleiben 2 rote unter 4 Kugeln, also 2/4. Richtig ist P = 3/5 · 2/4 = 6/20 = 3/10. Zeile 3 rechnet mit der falschen Zeile 2 richtig weiter."), regel=ST)
