T = "zahlen.potenzen_basis"
PO, BA = "rr.potenz", "id.zahlen.bausteine"
BM = "fb.potenz.basis_mal_hochzahl"

# ───────── schreibweise ─────────
neu(T, "schreibweise", "zwei_wege", Z(
    "Weg A: Schreibe die Potenz als Produkt gleicher Faktoren und rechne. Weg B: Schreibe 4 als 2 · 2, bilde daraus eine Potenz mit der Basis 2 und rechne diese aus. Berechne 4³ auf zwei Wegen.",
    64, "4 * 4 * 4", "2 ** 6", "Wie oft kommt die 2 insgesamt als Faktor vor, wenn du 4 · 4 · 4 mit 4 = 2 · 2 aufschreibst?",
    "Weg A: 4³ = 4 · 4 · 4 = 64. Weg B: 4³ = (2 · 2) · (2 · 2) · (2 · 2) = 2 · 2 · 2 · 2 · 2 · 2 = 2⁶ = 64.",
    [(12, BM, "Basis mal Hochzahl gerechnet: 4 · 3", "4 * 3"), (81, None, "Basis und Hochzahl vertauscht: 3⁴", "3 ** 4"), (32, None, "mit 2⁵ statt 2⁶ gerechnet (einen Faktor 2 vergessen)", "2 ** 5")]), regel=PO)
neu(T, "schreibweise", "anwenden", Z(
    "Am Tag 1 kennt eine Person ein Geheimnis. An jedem weiteren Tag erzählt jede Person, die es am Vortag neu erfahren hat, das Geheimnis genau drei Personen weiter, die es noch nicht kennen. Alle Empfänger sind verschieden. Wie viele Personen erfahren das Geheimnis am Tag 5 neu?",
    81, "3 ** 4", "3 * 3 * 3 * 3", "Wie viele Personen erfahren es am Tag 2? Am Tag 3? Erkennst du ein Muster mit gleichen Faktoren?",
    "Tag 2: 3 neue Personen, Tag 3: 3 · 3 = 9, Tag 4: 27, Tag 5: 3 · 3 · 3 · 3 = 3⁴ = 81. Der Exponent ist um 1 kleiner als die Nummer des Tages.",
    [(243, None, "mit 3⁵ gerechnet (Exponent gleich der Tagesnummer)", "3 ** 5"), (15, BM, "Basis mal Hochzahl gerechnet (3 · 5) und dabei die Tagesnummer statt der Zahl der Wachstumsschritte genommen", "3 * 5"), (12, BM, "Basis mal Hochzahl gerechnet: 3 · 4", "3 * 4")], "Personen"), g="transfer", regel=PO)

# ───────── berechnen ─────────
neu(T, "berechnen", "umkehren", Z(
    "Welche natürliche Zahl muss im Kästchen stehen? 3 · □² = 75",
    5, "5", "(75 / 3) ** 0.5", "Mache zuerst das Malnehmen mit 3 rückgängig. Welche Zahl mit sich selbst malgenommen ergibt dann das Ergebnis?",
    "3 · □² = 75, also □² = 75 : 3 = 25. Wegen 5 · 5 = 25 ist □ = 5. Probe: 3 · 5² = 3 · 25 = 75.",
    [(25, None, "nur durch 3 geteilt, das Quadrat nicht rückgängig gemacht", "75 / 3"), (12.5, None, "die Hochzahl 2 als Teilen durch 2 gedeutet: 25 : 2", "75 / 3 / 2")]), g="umkehr", regel=PO)
neu(T, "berechnen", "fehler_detektiv", FD(
    "Ben berechnet 5 · 2³ − 3².",
    [("2³ = 2 · 3 = 6, also ist 5 · 2³ = 5 · 6 = 30.", 2 ** 3 == 2 * 3, True),
     ("3² = 3 · 3 = 9.", 3 ** 2 == 9, True, "Zeile 2 ist unabhängig von Zeile 1 und für sich richtig: 3² = 3 · 3 = 9."),
     ("30 − 9 = 21.", 30 - 9 == 21, True, "Zeile 3 rechnet 30 − 9 = 21 für sich richtig, benutzt aber die 30 aus Zeile 1. Der Fehler liegt schon in Zeile 1.")],
    "Prüfe jede Zeile für sich und schreibe jede Potenz als Produkt aus. Welche Zeile enthält zuerst einen Fehler?",
    "2³ = 2 · 2 · 2 = 8, nicht 2 · 3. Richtig: 5 · 8 = 40 und 40 − 9 = 31. Der erste Fehler steht in Zeile 1."), regel=PO)

# ───────── quadrat ─────────
neu(T, "quadrat", "zwei_wege", Z(
    "Weg A: Rechne 15 · 15 schriftlich. Weg B: Zerlege den zweiten Faktor in 10 + 5 und rechne 15 · 10 + 15 · 5. Berechne 15² auf zwei Wegen.",
    225, "15 * 15", "15 * 10 + 15 * 5", "Bei Weg B rechnest du zwei einfachere Malaufgaben und addierst.",
    "Weg A schriftlich: 15 · 1 = 15, das sind 150 (eine Stelle nach links), dann 15 · 5 = 75; 150 + 75 = 225. Weg B: 15 · 10 = 150, 15 · 5 = 75, 150 + 75 = 225.",
    [(30, BM, "Basis mal Hochzahl gerechnet: 15 · 2", "15 * 2"), (150, None, "nur 15 · 10 gerechnet", "15 * 10"), (25, None, "nur die Einerziffer quadriert", "5 * 5")]), regel=PO)
neu(T, "quadrat", "bruecke", Z(
    "Aus Plättchen wird ein Quadrat gelegt, 9 Plättchen lang und 9 Plättchen breit. Wie viele Plättchen liegen nicht am Rand, also im Inneren?",
    49, "9 * 9 - (4 * 9 - 4)", "(9 - 2) ** 2", "Das Innere ist wieder ein Quadrat. Wie viele Plättchen lang ist es? Am Rand fehlt auf jeder Seite eine Reihe.",
    "Innen bleibt ein Quadrat, das auf jeder Seite eine Reihe weniger hat: 9 − 2 = 7. 7² = 49 Plättchen. Kontrolle: Alle 9² = 81, Rand 4 · 9 − 4 = 32, 81 − 32 = 49.",
    [(77, None, "nur die 4 Ecken abgezogen", "81 - 4"), (45, None, "den Rand mit vier Seiten zu je 9 Plättchen abgezogen (Ecken doppelt gezählt)", "81 - 36"), (63, None, "nur zwei gegenüberliegende Randreihen entfernt: 9 · 7", "9 * 7")], "Plättchen"), g="verknuepfen", regel=PO)

# ───────── vertauschen ─────────
neu(T, "vertauschen", "umkehren", Z(
    "Für welche Hochzahl gilt 3 hoch □ = 81?",
    4, "4", "81 / 27 + 1", "Wie oft muss die 3 als Faktor stehen, damit 81 herauskommt? Die Hochzahl sagt, wie oft die Basis als Faktor vorkommt.",
    "3 · 3 = 9, 9 · 3 = 27, 27 · 3 = 81: Die 3 steht 4-mal als Faktor da, also 3⁴ = 81. Nicht verwechseln: 4³ ist 4 · 4 · 4 = 64. Probe: 3⁴ = 81.",
    [(3, None, "Basis und Hochzahl vertauscht: die Basis 3 als Hochzahl genommen", "3"), (27, None, "81 durch 3 geteilt", "81 / 3"), (9, None, "die Zahl als Hochzahl genommen, die mit sich selbst malgenommen 81 ergibt", "9")]), g="umkehr", regel=PO)
neu(T, "vertauschen", "fehler_detektiv", FD(
    "Mia vergleicht 3⁴ und 4³.",
    [("3⁴ = 3 · 3 · 3 · 3 = 81.", 3 ** 4 == 81, True, "Zeile 1 stimmt: 3 · 3 · 3 · 3 = 81. Der Fehler steckt später."),
     ("4³ = 4 · 4 · 4 = 64.", 4 ** 3 == 64, True, "Zeile 2 stimmt: 4 · 4 · 4 = 64. Der Fehler steckt später."),
     ("Also sind die beiden Potenzen gleich, weil nur Basis und Hochzahl getauscht sind.", 3 ** 4 == 4 ** 3, True)],
    "Prüfe jede Zeile für sich: Stimmt die Rechnung, und stimmt der Schluss daraus? Welche Zeile enthält zuerst einen Fehler?",
    "81 und 64 sind verschieden. Beim Vertauschen von Basis und Hochzahl ändert sich der Wert im Allgemeinen. Der erste Fehler steht in Zeile 3."), regel=PO)

# ───────── zehner ─────────
neu(T, "zehner", "zwei_wege", Z(
    "Weg A: Schreibe 10⁵ als Zahl und multipliziere. Weg B: Überlege, wie viele Nullen man an 36 anhängt. Berechne 36 · 10⁵ auf zwei Wegen.",
    3600000, "36 * 10 ** 5", "36 * 100000", "Wie viele Nullen hat die Zahl 10⁵?",
    "Weg A: 10⁵ = 100 000, 36 · 100 000 = 3 600 000. Weg B: Die Hochzahl 5 sagt: fünf Nullen anhängen. 36 mit fünf Nullen: 3 600 000.",
    [(360000, None, "nur vier Nullen angehängt", "36 * 10 ** 4"), (36000000, None, "sechs Nullen angehängt", "36 * 10 ** 6"), (1800, BM, "Basis mal Hochzahl gerechnet: 36 · (10 · 5)", "36 * (10 * 5)")]), regel=PO)
neu(T, "zehner", "anwenden", Z(
    "Licht legt in einer Sekunde etwa 3 · 10⁵ Kilometer zurück. Wie viele Kilometer legt es in 10 Sekunden etwa zurück?",
    3000000, "3 * 10 ** 5 * 10", "3 * 10 ** 6", "Zehn Sekunden sind das Zehnfache. Was passiert mit einer Zehnerpotenz, wenn man mit 10 malnimmt?",
    "In 10 Sekunden: 3 · 10⁵ · 10 = 3 · 10⁶ = 3 000 000 km. Die Strecke ist also etwa 3 000 000 km lang.",
    [(300000, None, "die Zeit nicht beachtet", "3 * 10 ** 5"), (30000000, None, "eine Null zu viel angehängt", "3 * 10 ** 7"), (30, None, "3 · 10 gerechnet", "3 * 10")], "km"), g="transfer", regel=PO)

# ───────── negativ ─────────
neu(T, "negativ", "zwei_wege", Z(
    "Weg A: Schreibe (−3) · (−3) · (−3) und rechne Schritt für Schritt. Weg B: Bestimme das Vorzeichen daran, wie viele negative Faktoren es sind, und rechne dann 3³. Berechne (−3)³ auf zwei Wegen.",
    -27, "(-3) * (-3) * (-3)", "-(3 ** 3)", "Wie viele Faktoren (−3) gibt es? Wann ist ein Produkt negativ?",
    "Weg A: (−3) · (−3) = 9, 9 · (−3) = −27. Weg B: Drei negative Faktoren, das Produkt ist negativ. 3³ = 27, also −27.",
    [(27, "fb.vorzeichen.falsches_zeichen", "das Vorzeichen vergessen", "3 ** 3"), (-9, BM, "Basis mal Hochzahl gerechnet: (−3) · 3", "(-3) * 3"), (9, None, "nur die ersten beiden Faktoren gerechnet", "(-3) * (-3)")]), regel="rr.vorzeichen")
neu(T, "negativ", "fehler_detektiv", FD(
    "Lena berechnet −2⁴ + (−2)⁴.",
    [("−2⁴ bedeutet, dass 2⁴ negativ genommen wird: −2⁴ = −(2 · 2 · 2 · 2) = −16.", -(2 ** 4) == -16, True, "Zeile 1 stimmt: Bei −2⁴ wird nur 2⁴ negativ genommen, −(2 · 2 · 2 · 2) = −16. Der Fehler steckt später."),
     ("(−2)⁴ = (−2) · (−2) · (−2) · (−2) = −16.", (-2) ** 4 == -16, True),
     ("Also ist die Summe −16 + (−16) = −32.", -16 + (-16) == -32, True, "Zeile 3 rechnet −16 + (−16) = −32 für sich richtig, benutzt aber das falsche Ergebnis aus Zeile 2. Der Fehler liegt schon in Zeile 2.")],
    "Prüfe jede Zeile für sich und zähle bei jedem Produkt die negativen Faktoren. Welche Zeile enthält zuerst einen Fehler?",
    "Zwei negative Faktoren ergeben plus, vier ebenso: (−2)⁴ = 16. Richtig: −16 + 16 = 0. Der erste Fehler steht in Zeile 2."), regel="rr.vorzeichen")

# ───────── sach ─────────
neu(T, "sach", "bruecke", Z(
    "Die Tabelle zeigt, wie viele Blätter eine Seerose an den ersten vier Tagen hat. Die Verdopplung geht jeden Tag so weiter. Wie viele Blätter hat die Seerose am Tag 9?",
    256, "2 ** 8", "2 * 2 * 2 * 2 * 2 * 2 * 2 * 2", "Erkenne das Muster in der Tabelle: Womit wird von Tag zu Tag malgenommen? Wie oft passiert das bis Tag 9?",
    "Die Zahl wird jeden Tag mit 2 malgenommen. Von Tag 1 bis Tag 9 wird 8-mal verdoppelt: 2⁸ = 256 Blätter.",
    [(512, None, "9-mal verdoppelt: 2⁹", "2 ** 9"), (18, BM, "Basis mal Hochzahl gerechnet (2 · 9) und dabei die Tagesnummer statt der Zahl der Wachstumsschritte genommen", "2 * 9"), (16, BM, "Basis mal Hochzahl gerechnet: 2 · 8", "2 * 8")], "Blätter",
    grafik=TAB(["Tag", "Blätter"], ["1", "1"], ["2", "2"], ["3", "4"], ["4", "8"])), regel=PO)
neu(T, "sach", "umkehren", Z(
    "Eine Bakterienkultur verdoppelt ihre Zahl jede Stunde. Nach 8 Stunden sind es 1 280 Bakterien. Wie viele Bakterien waren es am Anfang?",
    5, "1280 / 2 ** 8", "1280 / 256", "Wie viele Verdopplungen gab es? Mache sie rückgängig oder teile durch den Faktor.",
    "In 8 Stunden wurde 8-mal verdoppelt, die Zahl wurde mit 2⁸ = 256 malgenommen. Am Anfang: 1 280 : 256 = 5. Probe: 5 · 256 = 1 280.",
    [(160, None, "durch 8 statt durch 2⁸ geteilt", "1280 / 8"), (10, None, "nur 7 Verdopplungen rückgängig gemacht", "1280 / 2 ** 7"), (640, None, "nur eine Verdopplung rückgängig gemacht", "1280 / 2")]), g="rueckwaerts", regel=PO)
