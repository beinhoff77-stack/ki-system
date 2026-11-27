T = "stochastik.grundbegriffe"
AN = "id.daten.anteil"
ST = "id.daten.stufen"
# ───────── begriffe ─────────
_zahl = [2, 3, 3, 5, 8, 8, 2, 7]
_prim = lambda n: n > 1 and all(n % k for k in range(2, n))
neu(T, "begriffe", "bruecke", Z(
    "Ein Glücksrad hat 8 gleich große Felder. Die Tabelle zeigt die Zahl auf jedem Feld. Ein Ergebnis ist das Feld, auf dem das Rad stehen bleibt. Wie viele Ergebnisse gehören zum Gegenereignis von „Die Zahl ist eine Primzahl“?",
    2, "8 - 6", "2", "Zähle Felder, nicht Zahlen. Welche Felder gehören zum Ereignis selbst?",
    "Zum Ereignis gehören die Felder 1, 2, 3, 4, 7 und 8 (Zahlen 2, 3, 3, 5, 2 und 7). Das sind 6 Ergebnisse. Das Gegenereignis enthält alle übrigen Ergebnisse: die Felder 5 und 6, beide mit der Zahl 8. Es hat 8 − 6 = 2 Ergebnisse.",
    [(6, None, "die Ergebnisse des Ereignisses selbst statt des Gegenereignisses gezählt", "6"), (1, None, "verschiedene Zahlen statt Felder gezählt", "1"), (4, None, "die verschiedenen Primzahlen 2, 3, 5 und 7 gezählt", "4")],
    grafik=TAB(["Feld", "1", "2", "3", "4", "5", "6", "7", "8"], ["Zahl", "2", "3", "3", "5", "8", "8", "2", "7"])), g="darstellung", regel=AN)
assert sum(1 for n in _zahl if _prim(n)) == 6 and sum(1 for n in _zahl if not _prim(n)) == 2 and len({n for n in _zahl if not _prim(n)}) == 1 and len({n for n in _zahl if _prim(n)}) == 4
neu(T, "begriffe", "zwei_wege", Z(
    "Ein Glücksrad hat 12 gleich große Felder mit den Zahlen 1 bis 12. Ein Ergebnis ist die Zahl, bei der das Rad stehen bleibt. Ereignis A: „Die Zahl ist durch 3 teilbar“. Ereignis B: „Die Zahl ist größer als 6“. Weg A: Die Zahlen von A und B aufschreiben und doppelte nur einmal zählen. Weg B: Die Anzahl der Zahlen von A und die von B zusammenzählen und die Anzahl der Zahlen abziehen, die in beiden Ereignissen stehen. Wie viele Ergebnisse gehören zum Ereignis „A oder B“ (A, B oder beides)?",
    8, "4 + 6 - 2", "12 - 4", "Welche Zahlen stehen in A und in B zugleich? Sie dürfen nur einmal gezählt werden.",
    "A hat die Zahlen 3, 6, 9, 12 (4 Ergebnisse). B hat die Zahlen 7, 8, 9, 10, 11, 12 (6 Ergebnisse). In beiden stehen 9 und 12. Weg A: 3, 6, 7, 8, 9, 10, 11, 12 sind 8 Zahlen. Weg B: 4 + 6 − 2 = 8. Probe: Das Gegenereignis hat die Zahlen 1, 2, 4, 5. Das sind 4 Zahlen, und 12 − 4 = 8.",
    [(10, None, "die Zahlen aus beiden Ereignissen gezählt und die doppelten nicht abgezogen", "4 + 6"), (2, None, "„und“ statt „oder“ gezählt: nur Zahlen, die in beiden stehen", "2"), (4, None, "das Gegenereignis von „A oder B“ gezählt", "12 - 8")]), g="verknuepfen", regel=AN)
assert len({n for n in range(1, 13) if n % 3 == 0 or n > 6}) == 8 and len({n for n in range(1, 13) if n % 3 == 0 and n > 6}) == 2
# ───────── rel_haeufigkeit ─────────
neu(T, "rel_haeufigkeit", "verfahren_waehlen", W(
    "Ein Reißnagel wird 80-mal geworfen. 28-mal landet er mit der Spitze nach oben. Welche Rechnung gibt die relative Häufigkeit von „Spitze nach oben“ in Prozent?",
    "28 durch 80 teilen und das Ergebnis mit 100 malnehmen",
    [("80 durch 28 teilen und das Ergebnis mit 100 malnehmen", "Gesamtzahl durch die günstige Anzahl geteilt: das Ergebnis wäre über 100 Prozent"),
     ("28 mit 80 malnehmen und durch 100 teilen", "die beiden Zahlen multipliziert, aber keinen Anteil gebildet"),
     ("die Differenz von 80 und 28 durch 80 teilen und das Ergebnis mit 100 malnehmen", "die Würfe mit Spitze nach unten gezählt: das ist die relative Häufigkeit des Gegenereignisses")],
    "Relative Häufigkeit ist ein Anteil. Wovon ist der Teil, und was ist das Ganze?",
    "Der Teil sind 28 Würfe, das Ganze sind 80 Würfe. 28 : 80 = 0,35 und 0,35 · 100 = 35 Prozent. Die anderen Rechnungen geben ungefähr 286 Prozent, 22,4 und 65 Prozent.",
    lambda: abs(28 / 80 * 100 - 35) < 1e-9 and all(abs(v - 35) > 1e-9 for v in (80 / 28 * 100, 28 * 80 / 100, (80 - 28) / 80 * 100))), g="mehrschritt", regel=AN)
neu(T, "rel_haeufigkeit", "umkehren", Z(
    "Ein Würfel wird in einer ersten Serie mehrmals geworfen. Die Sechs fällt 15-mal, ihre relative Häufigkeit ist 20 Prozent. In einer zweiten Serie wird derselbe Würfel noch 25-mal geworfen, dabei fällt die Sechs wieder 15-mal. Wie groß ist die relative Häufigkeit der Sechs in beiden Serien zusammen (in Prozent)?",
    30, "(15 + 15) / (15 * 100 / 20 + 25) * 100", "30 / 100 * 100", "Wie viele Würfe hatte die erste Serie? Zähle dann alle Sechsen und alle Würfe zusammen.",
    "Erste Serie: 15 : n = 0,2, also n = 15 : 0,2 = 75 Würfe. Beide Serien: 75 + 25 = 100 Würfe und 15 + 15 = 30 Sechsen. Relative Häufigkeit: 30 : 100 = 0,3, das sind 30 Prozent. Probe: 20 Prozent von 75 sind 15.",
    [(40, None, "die beiden relativen Häufigkeiten 20 und 60 Prozent gemittelt, ohne die Zahl der Würfe zu beachten", "(20 + 60) / 2"), (60, None, "nur die zweite Serie betrachtet: 15 von 25", "15 / 25 * 100"), (20, None, "nur die erste Serie betrachtet", "15 / 75 * 100")], "%"), g="rueckwaerts", regel=AN)
# ───────── darstellen ─────────
neu(T, "darstellen", "anwenden", Z(
    "Bei einem Spiel wird zuerst eine Münze geworfen. Fällt Zahl, ist das Spiel zu Ende. Fällt Wappen, wird danach ein Würfel mit den Zahlen 1 bis 6 geworfen. Das Spiel wird als Baumdiagramm gezeichnet. Wie viele Wege führen vom Start bis zu einem Ende?",
    7, "1 + 6", "6 * 1 + 1", "Zeichne den Baum. Wie viele Wege gehen durch den Ast „Wappen“, wie viele durch den Ast „Zahl“?",
    "Der Ast „Zahl“ endet sofort: 1 Weg. Der Ast „Wappen“ teilt sich in 6 Äste für den Würfel: 6 Wege. Zusammen sind es 1 + 6 = 7 Wege. Nicht 2 · 6, denn nach „Zahl“ wird nicht gewürfelt.",
    [(12, None, "auch nach „Zahl“ noch gewürfelt: Münze und Würfel in jedem Fall", "2 * 6"), (8, None, "die Äste der zweiten Stufe und der ersten Stufe gezählt statt der Wege", "2 + 6"), (6, None, "den Weg über „Zahl“ vergessen", "6")]), g="einkleidung", regel=None)
neu(T, "darstellen", "fehler_detektiv", FD(
    "Kim zieht zweimal hintereinander eine Kugel aus einer Urne mit den Kugeln 1, 2, 3 und 4. Die gezogene Kugel wird nicht zurückgelegt. Kim zeichnet das Baumdiagramm und zählt.",
    [("Beim ersten Zug gibt es 4 Möglichkeiten.", len(range(1, 5)) == 4, True),
     ("Die gezogene Kugel bleibt draußen. Beim zweiten Zug gibt es nur noch 3 Möglichkeiten.", 4 - 1 == 3, True),
     ("Das Baumdiagramm hat 12 Wege, denn 4 mal 3 sind 12.", len(list(itertools.permutations(range(1, 5), 2))) == 12, True),
     ("Zum Ereignis „Die Summe ist 6“ gehören die Wege (2 | 4), (4 | 2) und (3 | 3). Das sind 3 Wege.",
      len([p for p in itertools.permutations(range(1, 5), 2) if sum(p) == 6]) == 3, False)],
    "Prüfe jede Zeile einzeln: Passt sie zu der Regel, dass die Kugel nicht zurückgelegt wird?",
    "Zeile 1 bis 3 stimmen: 4 · 3 = 12 Wege. In Zeile 4 steht der Weg (3 | 3). Kugel 3 ist nach dem ersten Zug draußen und kann nicht noch einmal gezogen werden. Zur Summe 6 gehören nur (2 | 4) und (4 | 2), also 2 Wege. Die Summe 6 allein reicht nicht: Der Weg muss im Baum vorkommen."), g="fehler", regel=None)
