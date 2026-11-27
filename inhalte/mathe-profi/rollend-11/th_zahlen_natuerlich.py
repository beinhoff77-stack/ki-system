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

# ───────── ziffern_zu_zahlwort: Fehler-Detektiv ─────────
FD(T, "ziffern_zu_zahlwort",
   "Kim schreibt das Zahlwort „dreißig Millionen vierhunderttausendzwölf“ mit Ziffern.",
   [("„dreißig Millionen“ sind 30 000 000.", 30 * 1000000 == 30000000),
    ("„vierhunderttausend“ sind 40 000, zusammen 30 040 000.", 400 * 1000 == 40000 and 30000000 + 40000 == 30040000),
    ("„zwölf“ sind 12, zusammen 30 040 012.", 30040000 + 12 == 30040012)],
   "Rechne jede Zeile einzeln nach.",
   "In Zeile 2 sind „vierhunderttausend“ 400 · 1 000 = 400 000, nicht 40 000. Zeile 3 rechnet mit dem falschen Wert richtig weiter. Richtig: 30 000 000 + 400 000 + 12 = 30 400 012.",
   "rr.stellenwert", "bei „vierhunderttausend“ eine Null zu wenig geschrieben: 40 000 statt 400 000")

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
   "Kim möchte die Zahl 28 446 auf Hunderter runden und geht in Schritten vor.",
   [("Auf Zehner gerundet: 28 446 ≈ 28 450.", rd(28446, 10) == 28450),
    ("Auf Hunderter gerundet: 28 450 ≈ 28 500.", rd(28450, 100) == 28500),
    ("Also ist 28 446 auf Hunderter gerundet 28 500.", rd(28446, 100) == 28500)],
   "Runde 28 446 selbst direkt auf Hunderter und vergleiche.",
   "Zeile 1 und Zeile 2 sind für sich richtig gerundet. Aber das Ergebnis darf nicht in zwei Schritten gerundet werden: Bei 28 446 steht rechts neben der Hunderterstelle die 4, also wird abgerundet. "
   "Richtig ist 28 400.",
   "id.zahlen.buendeln", "in zwei Schritten gerundet (erst auf Zehner, dann auf Hunderter), obwohl nur die Ziffer rechts der Hunderterstelle zählt")

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
  "id.zahlen.buendeln", einheit="€")

# ───────── roemisch_schreiben: Anwenden ─────────
Z(T, "roemisch_schreiben", "anwenden",
  "Über dem Tor eines Rathauses steht das Baujahr MDCCCXCVII. 125 Jahre später wurde das Rathaus erneuert. In welchem Jahr (mit Ziffern geschrieben) war das?",
  2022, "1000 + 500 + 300 + 90 + 7 + 125", "1897 + 125",
  "Zerlege die römische Zahl in Gruppen. Ein kleines Zeichen vor einem größeren wird abgezogen.",
  "MDCCCXCVII = M (1 000) + D (500) + CCC (300) + XC (100 − 10 = 90) + VII (7) = 1 897. 1 897 + 125 = 2 022. Das Rathaus wurde 2022 erneuert.",
  [(2042, "1000 + 500 + 300 + 110 + 7 + 125", "XC als 110 gelesen statt als 90, also 1 000 + 500 + 300 + 110 + 7 + 125"),
   (1897, "1000 + 500 + 300 + 90 + 7", "das Baujahr richtig gelesen, aber die 125 Jahre vergessen"),
   (1772, "1897 - 125", "125 Jahre abgezogen statt addiert")],
  "id.zahlen.schreibweisen")

# ───────── dualsystem: Zwei Wege ─────────
Z(T, "dualsystem", "zwei_wege",
  "Welche normale Zahl gehört zur Zweierzahl 1101101? Weg A: Schreibe die Stellenwerte 64, 32, 16, 8, 4, 2, 1 unter die Ziffern und addiere die Stellenwerte der Einsen. "
  "Weg B: Beginne mit der ersten Ziffer. Verdopple bei jeder weiteren Ziffer das bisherige Ergebnis und addiere die neue Ziffer.",
  109, "64 + 32 + 8 + 4 + 1", "((((((1 * 2 + 1) * 2 + 0) * 2 + 1) * 2 + 1) * 2 + 0) * 2 + 1)",
  "Beide Wege müssen dieselbe Zahl ergeben. Welche Stellen tragen eine 1?",
  "Weg A: Die Einsen stehen bei 64, 32, 8, 4 und 1: 64 + 32 + 8 + 4 + 1 = 109. Weg B: 1; 1 · 2 + 1 = 3; 3 · 2 + 0 = 6; 6 · 2 + 1 = 13; 13 · 2 + 1 = 27; 27 · 2 + 0 = 54; 54 · 2 + 1 = 109. Die Zahl ist 109.",
  [(91, "1 + 2 + 8 + 16 + 64", "die Stellenwerte von links statt von rechts angelegt (1, 2, 4, …)"),
   (218, "128 + 64 + 16 + 8 + 2", "die Stellenwerte um eine Stelle verschoben (Einer = 2)"),
   (1101101, None, "die Ziffern als normale Zahl gelesen")],
  "id.zahlen.schreibweisen")
