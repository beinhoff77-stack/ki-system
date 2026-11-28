T = "stochastik.grundbegriffe"
# ───────── begriffe ─────────
a1(T, "begriffe", Z(
    "Aus einem Beutel mit fünf verschiedenfarbigen Kugeln (rot, blau, gelb, grün, weiß) werden nacheinander zwei Kugeln ohne Zurücklegen gezogen. Die Reihenfolge der Farben zählt. Wie viele Ergebnisse hat der Ergebnisraum?",
    20, "5 * 4", "4 + 4 + 4 + 4 + 4", "Wie viele Möglichkeiten gibt es für die erste Kugel? Wie viele bleiben dann für die zweite?",
    "Für die erste Kugel gibt es 5 Möglichkeiten, für die zweite danach noch 4. Das sind 5 · 4 = 20 Ergebnisse, zum Beispiel (rot | blau) und (blau | rot).",
    [B("5 * 5", "mit Zurücklegen gerechnet"), B("5 * 4 / 2", "die Reihenfolge nicht beachtet"), B("5 + 4", "die Möglichkeiten addiert statt multipliziert")], "Ergebnisse"))
a2(T, "begriffe", Z(
    "Ein Würfel mit den Augenzahlen 1 bis 6 und eine Münze (Seiten „Wappen“ und „Zahl“) werden einmal geworfen. Ein Ergebnis ist ein Paar aus Augenzahl und Münzseite, zum Beispiel (5 | Wappen). Wie viele Ergebnisse gehören zum Ereignis „Die Augenzahl ist größer als 4 oder die Münze zeigt Wappen“?",
    8, "2 * 2 + 6 - 2", "12 - 4", "Zähle zuerst die Ergebnisse mit Würfelzahl 5 oder 6. Zähle dann die Ergebnisse mit Wappen. Was wurde doppelt gezählt?",
    "Augenzahl größer als 4: Das sind 5 und 6, jeweils mit Wappen oder Zahl, also 4 Ergebnisse. Wappen: 6 Ergebnisse (jede Augenzahl mit Wappen). Doppelt gezählt: (5 | Wappen) und (6 | Wappen), also 2. Zusammen 4 + 6 − 2 = 8. Probe: Nicht dazu gehören nur die Augenzahlen 1 bis 4 mit der Münzseite Zahl, das sind 4 von 12 Ergebnissen.",
    [B("4 + 6", "die Ergebnisse, die zu beiden Teilen gehören, doppelt gezählt"), B("2", "nur die Ergebnisse gezählt, die beide Bedingungen erfüllen („und“ statt „oder“)"), B("4", "nur die Bedingung mit der Würfelzahl berücksichtigt")], "Ergebnisse"))
a3(T, "begriffe", Z(
    "Ein Glücksrad hat 30 gleich große Felder mit den Nummern 1 bis 30. Ereignis A: „Die Nummer ist ein Vielfaches von 3“. Ereignis B: „Die Nummer ist ein Vielfaches von 5“. Wie viele Ergebnisse gehören zu genau einem der beiden Ereignisse (zu A oder zu B, aber nicht zu beiden)?",
    12, "(10 - 2) + (6 - 2)", "10 + 6 - 2 * 2", "Zähle die Vielfachen von 3 und die von 5. Welche Nummern stehen in beiden Gruppen?",
    "A: 3, 6, …, 30, das sind 10. B: 5, 10, …, 30, das sind 6. In beiden stehen 15 und 30, also 2. Nur A: 10 − 2 = 8. Nur B: 6 − 2 = 4. Genau eines der beiden: 8 + 4 = 12 Ergebnisse.",
    [B("10 + 6 - 2", "die Ergebnisse von „A oder B“ (auch beide) angegeben"), B("10 + 6", "die Ergebnisse in beiden Gruppen doppelt gezählt"), B("2", "nur die Nummern in beiden Gruppen angegeben")], "Ergebnisse"), g="verknuepfen")
# ───────── rel_haeufigkeit ─────────
a1(T, "rel_haeufigkeit", Z(
    "Sam wirft beim Training 40-mal einen Basketball auf den Korb und trifft 28-mal. Wie groß ist die relative Häufigkeit der Treffer in Prozent?",
    70, "28 / 40 * 100", "28 * 2.5", "Relative Häufigkeit = Zahl der Treffer geteilt durch Zahl der Versuche. Dann in Prozent umrechnen.",
    "28 : 40 = 0,7. Als Prozent: 0,7 · 100 = 70 %. Sam trifft in 70 % der Fälle.",
    [B("28 / 40", "als Dezimalzahl angegeben und nicht in Prozent umgerechnet"), B("12 / 40 * 100", "die Fehlwürfe statt der Treffer verwendet"), B("28 / 100 * 40", "durch 100 geteilt und mit 40 malgenommen")], "%"))
a2(T, "rel_haeufigkeit", Z(
    "Kim würfelt in zwei Serien. In der ersten Serie sind es 50 Würfe, dabei fällt 18-mal die Sechs. In der zweiten Serie sind es 150 Würfe, dabei fällt 21-mal die Sechs. Wie groß ist die relative Häufigkeit der Sechs über beide Serien zusammen in Prozent?",
    19.5, "(18 + 21) / (50 + 150) * 100", "39 / 2", "Zähle die Sechsen aller Würfe zusammen und teile durch die Zahl aller Würfe.",
    "Sechsen: 18 + 21 = 39. Würfe: 50 + 150 = 200. Relative Häufigkeit: 39 : 200 = 0,195 = 19,5 %.",
    [B("(18 / 50 + 21 / 150) / 2 * 100", "den Mittelwert der beiden Prozentsätze genommen: die Serien sind verschieden lang"), B("21 / 150 * 100", "nur die zweite Serie berücksichtigt"), B("(18 + 21) / (50 + 150)", "als Dezimalzahl angegeben und nicht in Prozent umgerechnet")], "%"))
a3(T, "rel_haeufigkeit", Z(
    "Spielerin A trifft bei 24 Würfen 18-mal. Spieler B trifft bei 40 Würfen 25-mal. Um wie viele Prozentpunkte ist die relative Häufigkeit der Treffer bei A größer als bei B?",
    12.5, "18 / 24 * 100 - 25 / 40 * 100", "75 - 62.5", "Die Zahlen der Würfe sind verschieden. Vergleiche deshalb die relativen Häufigkeiten in Prozent.",
    "A: 18 : 24 = 0,75 = 75 %. B: 25 : 40 = 0,625 = 62,5 %. Unterschied: 75 − 62,5 = 12,5 Prozentpunkte. A hat die höhere Trefferquote, obwohl B mehr Treffer hat.",
    [B("18 / 24 - 25 / 40", "den Unterschied als Dezimalzahl statt in Prozentpunkten angegeben"), B("25 - 18", "die absoluten Zahlen der Treffer verglichen"), B("18 / 24 * 100 + 25 / 40 * 100", "die beiden Prozentsätze addiert")], "Prozentpunkte"), g="verknuepfen")
# ───────── darstellen ─────────
a1(T, "darstellen", Z(
    "In einer Klasse mit 25 Kindern sind 14 Mädchen. 9 Kinder tragen eine Brille, darunter 5 Mädchen. Eine Vierfeldertafel zeigt: Mädchen mit Brille, Mädchen ohne Brille, Jungen mit Brille, Jungen ohne Brille. Wie viele Jungen tragen keine Brille?",
    7, "(25 - 14) - (9 - 5)", "11 - 4", "Trage die bekannten Zahlen in eine Vierfeldertafel ein. Rechne zuerst die Zahl der Jungen und die der Jungen mit Brille aus.",
    "Jungen: 25 − 14 = 11. Jungen mit Brille: 9 − 5 = 4. Jungen ohne Brille: 11 − 4 = 7. Probe: Mädchen mit Brille 5 + Mädchen ohne Brille 9 + Jungen mit Brille 4 + Jungen ohne Brille 7 = 25.",
    [B("(25 - 14) - 5", "von den Jungen die Mädchen mit Brille abgezogen"), B("25 - 14", "alle Jungen angegeben"), B("25 - 14 - 9", "von den Jungen alle Brillenträger abgezogen")], "Jungen"))
a2(T, "darstellen", Z(
    "Bei einem Spiel wird zuerst ein Würfel mit den Zahlen 1 bis 6 geworfen. Bei einer geraden Zahl wird danach eine Münze geworfen. Bei einer ungeraden Zahl wird danach ein Würfel mit den Zahlen 1 bis 4 geworfen. Das Spiel wird als Baumdiagramm gezeichnet. Wie viele Wege hat es?",
    18, "3 * 2 + 3 * 4", "6 + 12", "Wie viele Äste gehen von der ersten Verzweigung aus? Zähle für jede Gruppe die Wege getrennt.",
    "Gerade Zahlen: 2, 4, 6 – das sind 3, dann 2 Münzseiten: 3 · 2 = 6 Wege. Ungerade Zahlen: 1, 3, 5 – das sind 3, dann 4 Zahlen: 3 · 4 = 12 Wege. Zusammen 6 + 12 = 18 Wege.",
    [B("3 * 2 + 3", "bei ungeraden Zahlen den zweiten Wurf vergessen"), B("6 * 2 * 4", "alle Zahlen mit 2 und mit 4 malgenommen"), B("6 + 2 + 4", "die Zahlen der Äste addiert")], "Wege"))
a3(T, "darstellen", Z(
    "In einer Gruppe von 100 Personen sind 60 Frauen. 30 Personen kommen mit dem Rad. Unter den Radfahrern sind doppelt so viele Frauen wie Männer. Wie viel Prozent der Männer kommen nicht mit dem Rad?",
    75, "(40 - 30 / 3) / 40 * 100", "30 / 40 * 100", "Zeichne eine Vierfeldertafel mit „Frau / Mann“ und „Rad / nicht Rad“. Wie viele Männer fahren Rad? Rechne mit den 30 Radfahrern in zwei Teilen.",
    "Männer insgesamt: 100 − 60 = 40. Die Radfahrer sind in drei gleiche Teile geteilt: 2 Teile Frauen, 1 Teil Männer. Männer mit Rad: 30 : 3 = 10. Männer ohne Rad: 40 − 10 = 30. Anteil: 30 : 40 = 0,75 = 75 %.",
    [B("10 / 40 * 100", "den Anteil der Männer mit Rad statt ohne Rad angegeben"), B("(100 - 30) / 100 * 100", "alle Personen ohne Rad auf alle Personen bezogen"), B("(40 - 20) / 40 * 100", "20 Männer mit Rad gerechnet (die Frauenzahl der Radfahrer)")], "%"), g="verknuepfen")