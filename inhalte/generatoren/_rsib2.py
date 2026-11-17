"""Neunzehnte Runde, Teil B, Chat 2 (Zweig durchsicht-rsib-2): gemeinsame Bausteine.

PLAN2: je Lernkarte 20 Übungen (Stufe 1: 6, Stufe 2: 6, Stufe 3: 8), dazu 1 Test, 3 Korrektur, 6 Sicherung.
slot3(): Nummer der gerade gebauten Stufe-3-Übung (0 … 7), sonst None. Die Generatoren legen damit fest:
  slot 0 und 1 = Aufgabe nach Prüfungsvorbild, slot 2 = Knobelaufgabe, slot 3 … 7 = abwechselnd die übrigen Stufe-3-Arten.
"""
from _ib import AKT, R

PLAN2 = ([('uebung', 1)] * 6 + [('uebung', 2)] * 6 + [('uebung', 3)] * 8
         + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6)


def slot3():
    if AKT['pool'] != 'uebung' or AKT['nr'] < 12:
        return None
    return AKT['nr'] - 12


def art3(pruef1, pruef2, knobel, rest):
    """Art der Stufe-3-Übung nach ihrem Platz: zwei Prüfungsvorbilder, eine Knobelaufgabe, danach reihum der Rest."""
    k = slot3()
    if k == 0: return pruef1
    if k == 1: return pruef2
    if k == 2: return knobel
    alle = list(rest)
    if k is None: return R.choice(alle)
    return alle[(k - 3) % len(alle)] if R.random() < .7 else R.choice(alle)
