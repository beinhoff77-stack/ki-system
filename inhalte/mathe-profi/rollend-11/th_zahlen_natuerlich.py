T = "zahlen.natuerlich"


def rd(n, schritt):
    """Runden nach der Schulregel (5 und mehr: aufrunden)."""
    return (n + schritt // 2) // schritt * schritt


# ───────── stellenwert: Umkehren ─────────
Z(T, "stellenwert", "umkehren",
  "Ich denke mir eine Zahl. Ich hänge hinten drei Nullen an. Dann zähle ich 4 Hunderter dazu und ziehe 7 Zehner ab. Jetzt steht 52 330 da. Welche Zahl habe ich mir gedacht?",
  52, "(52330 - 400 + 70) / 1000", "(52330 - 330) / 1000",
  "Mache die Schritte in umgekehrter Reihenfolge rückgängig. Was bewirkt es, wenn man hinten drei Nullen anhängt?",
  "Rückwärts: Die 7 Zehner wurden abgezogen, also 70 wieder dazu: 52 330 + 70 = 52 400. Die 4 Hunderter wurden dazugezählt, also 400 wieder weg: 52 400 − 400 = 52 000. "
  "Die drei angehängten Nullen entfernt man durch 1 000: 52 000 : 1 000 = 52. Probe: 52 000 + 400 − 70 = 52 330.",
  [(520, "52000 / 100", "nur zwei Nullen wieder entfernt (durch 100 geteilt)"),
   (5200, "52000 / 10", "nur eine Null wieder entfernt (durch 10 geteilt)"),
   (52000, "52330 - 400 + 70", "die Schritte richtig rückwärts gerechnet, aber die angehängten Nullen nicht wieder entfernt")],
  "rr.stellenwert")

# ───────── ziffern_zu_zahlwort: Fehler-Detektiv (Große Zahlen lesen: von den Ziffern zum Zahlwort) ─────────
gruppen = "30 400 012".split()
FD(T, "ziffern_zu_zahlwort",
   "Kim liest die Zahl 30 400 012 in Worten vor.",
   [("Von rechts in Dreiergruppen geteilt: 30 | 400 | 012.", gruppen == ["30", "400", "012"] and "".join(gruppen) == "30400012"),
    ("Die mittlere Gruppe 400 spricht er als „vierzigtausend“.", 40 * 1000 == 400 * 1000),
    ("Zusammen sagt er: „dreißig Millionen vierzigtausendzwölf“.", True)],
   "Welche Zahl gehört zu dem Zahlwort, das Kim sagt? Vergleiche sie mit der Zahl in Ziffern.",
   "Die Gruppe 400 steht an der Stelle der Tausender, es sind 400 Tausender, also „vierhunderttausend“. „Vierzigtausend“ wären 40 000. Zeile 3 setzt Kims Wörter richtig zusammen. "
   "Richtig gelesen heißt die Zahl „dreißig Millionen vierhunderttausendzwölf“.",
   "rr.stellenwert", "die Gruppe 400 als „vierzigtausend“ statt als „vierhunderttausend“ gesprochen")

# ───────── strahl_eintragen: Anwenden ─────────
Z(T, "strahl_eintragen", "anwenden",
  "Im Geschichtsraum einer Schule hängt ein Zeitstrahl von 1800 bis 2000. Er ist in 8 gleich lange Abschnitte geteilt, die Teilstriche liegen also gleich weit auseinander. "
  "Ein altes Foto der Schule stammt aus dem Jahr 1913 und soll auf dem Strahl eingetragen werden. Wie viele Jahre liegt 1913 vom nächstgelegenen Teilstrich entfernt?",
  12, "min(1913 - 1900, 1925 - 1913)", "1925 - 1913",
  "Wie viele Jahre umfasst ein Abschnitt? Schreibe dir die Jahre der Teilstriche auf.",
  "Ein Abschnitt umfasst (2000 − 1800) : 8 = 25 Jahre. Die Teilstriche liegen bei 1800, 1825, …, 1900, 1925, … 1913 liegt zwischen 1900 (13 Jahre davor) und 1925 (12 Jahre danach). "
  "Der nächstgelegene Teilstrich ist 1925, der Abstand beträgt 12 Jahre.",
  [(13, "1913 - 1900", "den Teilstrich davor genommen statt des nächstgelegenen"),
   (25, "(2000 - 1800) / 8", "die Länge eines Abschnitts genannt statt des Abstands zum Teilstrich"),
   (113, "1913 - 1800", "den Abstand zum Anfang des Strahls genannt")],
  "id.zahlen.zahlengerade", einheit="Jahre")

# ───────── runden_regel: Fehler-Detektiv ─────────
FD(T, "runden_regel",
   "Kim rundet die Zahl 28 446 auf Hunderter. Er rundet zuerst auf Zehner und dann das Ergebnis auf Hunderter.",
   [("Auf Zehner gerundet: 28 446 ≈ 28 450.", rd(28446, 10) == 28450),
    ("Auf Hunderter gerundet: 28 450 ≈ 28 500.", rd(28450, 100) == 28500),
    ("Also ist 28 446 auf Hunderter gerundet 28 500.", rd(28446, 100) == 28500)],
   "Runde 28 446 selbst direkt auf Hunderter und vergleiche.",
   "Zeile 1 und Zeile 2 sind als Aussagen für sich richtig. Falsch ist erst Zeile 3: Man darf nicht in zwei Schritten runden. Bei 28 446 steht rechts neben der Hunderterstelle die 4, also wird abgerundet. "
   "Richtig ist 28 400.",
   "id.zahlen.buendeln", "in zwei Schritten gerundet (erst auf Zehner, dann auf Hunderter), obwohl nur die Ziffer rechts der Hunderterstelle zählt",
   frage="In welcher Zeile steht zum ersten Mal eine Aussage, die für sich genommen falsch ist?",
   rueck={0: "Diese Zeile ist richtig: 28 446 auf Zehner gerundet ist 28 450. Die erste falsche Aussage steht in Zeile 3.",
          1: "Diese Zeile ist für sich richtig: 28 450 auf Hunderter gerundet ist 28 500. Falsch ist erst die Aussage in Zeile 3, dass damit auch 28 446 auf 28 500 gerundet wird."})

# ───────── runden_sinnvoll: Zwei Wege ─────────
Z(T, "runden_sinnvoll", "zwei_wege",
  "Ein Sportverein erhält in drei Monaten Spenden von 1 452 €, 1 468 € und 1 461 €. Weg A: Jede Spende auf Hunderter runden, dann addieren. "
  "Weg B: Erst genau addieren, dann die Summe auf Hunderter runden. Um wie viel Euro liegt das Ergebnis von Weg A weiter vom genauen Betrag entfernt als das Ergebnis von Weg B?",
  100, "(4500 - 4381) - (4400 - 4381)", "4500 - 4400",
  "Berechne zuerst den genauen Betrag. Dann beide Wege einzeln.",
  "Genauer Betrag: 1 452 + 1 468 + 1 461 = 4 381 €. Weg A: jede Spende wird auf 1 500 € gerundet, zusammen 4 500 €. Weg B: 4 381 € wird auf 4 400 € gerundet. "
  "Abstand zum genauen Betrag: Weg A 119 €, Weg B 19 €. Der Unterschied ist 119 − 19 = 100 €.",
  [(119, "4500 - 4381", "nur den Abstand von Weg A zum genauen Betrag genannt"),
   (19, "4400 - 4381", "nur den Abstand von Weg B zum genauen Betrag genannt"),
   (138, "119 + 19", "die beiden Abstände addiert statt voneinander abgezogen")],
  None, einheit="€")

# ───────── roemisch_schreiben: Anwenden (Jahr römisch schreiben) ─────────
def roemisch(n):
    r = ""
    for w, z in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= w:
            r += z
            n -= w
    return r


opt = ["MDCCCXCVII", "MCMXXII", "MDCCLXXII", "MMXXII"]
assert [roemisch(n) for n in (1897, 1922, 1772, 2022)] == opt
W(T, "roemisch_schreiben", "anwenden",
  "Ein Rathaus wurde im Jahr 1897 gebaut. 125 Jahre später wurde es erneuert. Wie schreibt man das Jahr der Erneuerung mit römischen Zeichen?",
  opt, 3, [o == roemisch(1897 + 125) for o in opt],
  "Rechne zuerst das Jahr aus. Schreibe es dann Stelle für Stelle, bei den Tausendern beginnend.",
  "1 897 + 125 = 2 022. Tausender: 2 000 = MM. Zehner: 20 = XX. Einer: 2 = II. Das Jahr 2022 schreibt man MMXXII.",
  {0: ("das Baujahr 1897 aufgeschrieben, die 125 Jahre vergessen", "1897"),
   1: ("nur 25 statt 125 Jahre dazugerechnet: 1 897 + 25 = 1 922", "1897 + 25"),
   2: ("125 Jahre abgezogen statt dazugezählt: 1 897 − 125 = 1 772", "1897 - 125")},
  None, werte=[1897, 1922, 1772, 2022])

# ───────── dualsystem: Zwei Wege ─────────
Z(T, "dualsystem", "zwei_wege",
  "Eine Zweierzahl ist 1101101. Weg A: Schreibe die Stellenwerte 64, 32, 16, 8, 4, 2, 1 unter die Ziffern und addiere die Stellenwerte der Einsen. "
  "Weg B: Beginne mit der ersten Ziffer. Verdopple bei jeder weiteren Ziffer das bisherige Ergebnis und addiere die neue Ziffer. Welche normale Zahl gehört zur Zweierzahl?",
  109, "64 + 32 + 8 + 4 + 1", "((((((1 * 2 + 1) * 2 + 0) * 2 + 1) * 2 + 1) * 2 + 0) * 2 + 1)",
  "Beide Wege müssen dieselbe Zahl ergeben. Welche Stellen tragen eine 1?",
  "Weg A: Die Einsen stehen bei 64, 32, 8, 4 und 1: 64 + 32 + 8 + 4 + 1 = 109. Weg B: 1; 1 · 2 + 1 = 3; 3 · 2 + 0 = 6; 6 · 2 + 1 = 13; 13 · 2 + 1 = 27; 27 · 2 + 0 = 54; 54 · 2 + 1 = 109. Die Zahl ist 109.",
  [(91, "1 + 2 + 8 + 16 + 64", "die Stellenwerte von links statt von rechts angelegt (1, 2, 4, …)"),
   (218, "128 + 64 + 16 + 8 + 2", "die Stellenwerte um eine Stelle verschoben (Einer = 2)"),
   (1101101, None, "die Ziffern als normale Zahl gelesen")],
  None)
