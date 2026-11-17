"""Einundzwanzigste Runde, Teil A: Schritte je Thema (Motor: _bereinigen.py). Begründungen im Postfach bereinigen.md."""
from _bereinigen import entfaellt, weg, her, karte_her, vertiefung, neu, knobel, ersetze, karte  # noqa: F401
from _befunde import _z as Z, _l as L  # noqa: F401
from _stufen_kl5 import A  # noqa: F401

PLAN = {}

# ======================= Klasse 5 =======================
# A1: Umkehraufgaben stehen zuerst in zahlen.ganz (Plus/Minus) und zahlen.rechengesetze (Mal/Geteilt).
PLAN['zahlen.ganz'] = [
    her('gleichungen.einfach', 'umkehr_plus', 'umkehraufgabe',
        r'^(Löse 63 = x − 28\.|Welche Rechnung führt zur Lösung von (47 − x = 18|x − 177 = 362)\?|Welche Zahl muss man von 1 000 subtrahieren|'
        r'Fülle die Lücke: 2 345|Löse x \+ 44 = 52 \+ 64\.|Ich denke mir eine Zahl\. Ziehe ich 99)', 7),
]
PLAN['zahlen.rechengesetze'] = [
    her('gleichungen.einfach', 'umkehr_mal', 'umkehraufgabe_mal',
        r'^(Löse x : 4 = 10\.|Löse 72 : x = 9\.|Welche Rechnung führt zur Lösung von x : 6 = 27\?|Ich denke mir eine Zahl, teile sie durch 7|'
        r'Stimmt die Aussage\? „Bei x : 8 = 5|Eine Zahl wird verdoppelt, das Ergebnis verdreifacht)', 6),
]
PLAN['gleichungen.einfach'] = [
    entfaellt('umkehr_plus'),
    entfaellt('umkehr_mal'),
    karte('zwei_schritte', woerter=[['Rechenkette', 'mehrere Rechenschritte hintereinander'],
                                    ['umkehren', 'rückgängig machen: aus plus wird minus, aus mal wird geteilt (Umkehraufgaben, Flüge zu den ganzen Zahlen und zu den Rechengesetzen)']]),
]
