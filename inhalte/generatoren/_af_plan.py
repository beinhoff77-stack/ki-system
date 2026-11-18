"""Plan der Vierundzwanzigsten Runde (Zweig aufloesen) – je Zielthema die Schritte für _aufloesen.aufloesen_datei.

Bausteine wie in _bereinigen (karte_her, karte_neu, neu, knobel, pool, karte, weg, ersetze, umschreiben).
Neue Aufgaben: Z (Zahl), L (Lücken) aus _befunde, A (Auswahl, Position fest aus dem Text gemischt) aus _stufen_kl5.
Jede Lösung wird beim Bauen nachgerechnet (c bzw. Lückenausdrücke).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bereinigen import (karte, karte_her, karte_neu, ersetze, umschreiben, weg, neu, knobel, pool, abschnitt, vertiefung)  # noqa: E402,F401
from _befunde import _z as Z, _l as L  # noqa: E402,F401
from _stufen_kl5 import A  # noqa: E402,F401

PLAN = {}


def W(lz, anfang, neuer_weg, n=1):
    """Nur den Lösungsweg einer umgezogenen Aufgabe neu schreiben (z. B. ohne Gleichung mit Buchstaben)."""
    return umschreiben(lz, '^' + re.escape(anfang), [(r'(?s)\A.*\Z', neuer_weg)], n, felder=('w',))


# =====================================================================================================================
# bruch.brueche (Kl. 6) ← groessen.verhaeltnisse: kuerzen (B, als verhaeltnis_kuerzen), gleichwertig (B). Vertiefung (nur IB).
# Lösungswege mit Buchstaben-Gleichungen (lineare Gleichungen erst Kl. 7) umgeschrieben; 40 % (Prozent erst später in Kl. 6) ersetzt.
# =====================================================================================================================
PLAN['bruch.brueche'] = [
    karte_her('groessen.verhaeltnisse', 'verhaeltnis_kuerzen', 'Erweitern und kürzen', vertiefung=True, nach='kuerzen'),
    karte_her('groessen.verhaeltnisse', 'gleichwertig', 'Erweitern und kürzen', vertiefung=True, nach='verhaeltnis_kuerzen'),
    W('verhaeltnis_kuerzen', 'In einer Gruppe ist das Verhältnis Mädchen : Jungen = 2 : 3. Kommen 2 Mädchen dazu',
      'Bei 2 : 3 haben die Jungen 1 Teil mehr als die Mädchen. Mit 2 neuen Mädchen sind es gleich viele, also ist 1 Teil = 2 Kinder. '
      'Vorher: 2 · 2 = 4 Mädchen und 3 · 2 = 6 Jungen, zusammen 10. Probe: 6 : 6 = 1 : 1.'),
    W('verhaeltnis_kuerzen', 'Zwei Zahlen stehen im Verhältnis 3 : 5. Addiert man zu jeder 4',
      'Probiere gleichwertige Paare zu 3 : 5 und addiere jeweils 4: 3 und 5 → 7 : 9; 6 und 10 → 10 : 14 = 5 : 7; '
      '9 und 15 → 13 : 19; 12 und 20 → 16 : 24 = 2 : 3. Also 12 und 20.'),
    W('gleichwertig', 'Sirup und Wasser wurden im Verhältnis 1 : 5 gemischt.',
      'Der Sirup bleibt gleich, nur das Wasser wächst: vorher 5 Teile, nachher 7 Teile. Die 2 Teile mehr sind 100 ml, '
      'also ist 1 Teil = 50 ml. Das ist der Sirup. Probe: 50 : 350 = 1 : 7.'),
    W('gleichwertig', 'Für welche positive Zahl x sind x : 6 und 6 : (x + 5) gleichwertig?',
      'Probiere kleine Zahlen: x = 2 → 2 : 6 = 1 : 3, aber 6 : 7 nicht. x = 3 → 3 : 6 = 1 : 2, aber 6 : 8 = 3 : 4. '
      'x = 4 → 4 : 6 = 2 : 3 und 6 : 9 = 2 : 3. Also x = 4.'),
    ersetze('gleichwertig', r'^Ein Teil ist 40 % des Ganzen', L(
        'In einer Klasse sind 2/5 der Kinder Mädchen, die anderen sind Jungen. Gib das Verhältnis Mädchen : Jungen an.', '□ : □', [2, 3], ['2', '5 - 2'],
        'Von 5 gleichen Teilen der Klasse sind 2 Teile Mädchen und 5 − 2 = 3 Teile Jungen. Also Mädchen : Jungen = 2 : 3.',
        'Teile die Klasse in 5 gleiche Teile. Wie viele davon sind Jungen?', hinweis='Zwei ganze Zahlen, vollständig gekürzt.')),
]


# =====================================================================================================================
# groessen.proportional (Kl. 5) ← groessen.verhaeltnisse: aenderung (B). Vertiefung (nur IB), am Ende hinter sach.
# Ersetzt: Prozentpunkte (Prozent erst Kl. 6) und Ungleichung mit r (Ungleichungen erst Kl. 8). Knobel-Lösungsweg ohne Gleichung.
# =====================================================================================================================
PLAN['groessen.proportional'] = [
    karte_her('groessen.verhaeltnisse', 'aenderung', 'Anwenden', vertiefung=True, nach='sach'),
    ersetze('aenderung', r'^Ein Handyakku zeigt 80 %', Z(
        'Eine Seilbahn fährt von der Talstation auf 600 m Höhe zur Bergstation auf 1 800 m Höhe. Sie steigt jede Sekunde um 5 m. Wie viele Minuten dauert die Fahrt?',
        4, '(1800 - 600) / 5 / 60', 'Höhenunterschied: 1 800 m − 600 m = 1 200 m. Bei 5 m pro Sekunde: 1 200 : 5 = 240 Sekunden. 240 s = 4 min.',
        'Rechne zuerst aus, wie viele Meter die Bahn insgesamt steigt. Achte auf Sekunden und Minuten.', einheit='min')),
    ersetze('aenderung', r'^Ein Becken enthält 100 l\. Für welche Zuflussraten r', Z(
        'Ein Becken enthält 100 l. Es fließen r Liter pro Minute zu. Für welchen Wert von r sind nach 10 Minuten genau 150 l darin?',
        5, '(150 - 100) / 10', 'In 10 Minuten müssen 150 − 100 = 50 l dazukommen. 50 : 10 = 5, also r = 5 Liter pro Minute.',
        'Wie viele Liter müssen in den 10 Minuten insgesamt dazukommen?')),
    W('aenderung', 'Kerze A ist 20 cm hoch und brennt in 4 Stunden ganz ab',
      'A wird pro Stunde 20 : 4 = 5 cm kürzer, B nur 15 : 5 = 3 cm. A holt also jede Stunde 2 cm auf. Am Anfang ist A 5 cm höher: '
      '5 : 2 = 2,5 Stunden. Dann sind beide 7,5 cm hoch (20 − 12,5 und 15 − 7,5).'),
]


# =====================================================================================================================
# stochastik.verknuepft (Kl. 9) ← mengen.grundbegriffe: elemente (C), schnitt, venn, verstehen (B; als mengen_verstehen)
#                                ← stochastik.bedingt: rueckschluss (B). Alle Vertiefung (nur IB).
# elemente/schnitt als Einstieg vor verknuepfen (doppelt-rsib: Einstiegskarte vor verknuepfen); venn und mengen_verstehen nach
# additionssatz (∪ ist dann aus verknuepfen bekannt; die Karte vereinigung mit n(A) entfällt, daher n(A) als neues Wort).
# =====================================================================================================================
PLAN['stochastik.verknuepft'] = [
    karte_her('mengen.grundbegriffe', 'elemente', 'Ereignisse verknüpfen', vertiefung=True, vor='verknuepfen'),
    karte_her('mengen.grundbegriffe', 'schnitt', 'Ereignisse verknüpfen', vertiefung=True, vor='verknuepfen'),
    karte_her('mengen.grundbegriffe', 'venn', 'Ereignisse verknüpfen', vertiefung=True, nach='additionssatz'),
    karte_her('mengen.grundbegriffe', 'mengen_verstehen', 'Ereignisse verknüpfen', vertiefung=True, nach='venn'),
    karte('mengen_verstehen', woerter=[['n(A)', 'die Anzahl der Elemente von A'],
                                       ['Gegenbeispiel', 'ein Beispiel, bei dem die Aussage nicht stimmt'],
                                       ['Teilmenge', 'A ⊆ B: Jedes Element von A liegt auch in B']]),
    karte_her('stochastik.bedingt', 'rueckschluss', 'Bedingte Wahrscheinlichkeit und Verstehen', vertiefung=True, nach='bedingt'),
    karte('rueckschluss', woerter=[['gemeldet', 'das Prüfgerät schlägt Alarm'],
                                   ['P(A | B)', 'andere Schreibweise für P_B(A): Wahrscheinlichkeit von A, wenn B schon eingetreten ist']]),
    abschnitt('Ereignisse verknüpfen', 'Mengen und Ereignisse verknüpfen'),
]
