#!/usr/bin/env python3
"""Expedition „Der Zeltplatz“ (Klasse 5) – Koordinaten, Rechteckfläche, Dreisatz, Abstand zu Punkt und Gerade.
Aufruf: python3 -I inhalte/generatoren/expedition_zeltplatz.py → inhalte/expeditionen/5-zeltplatz.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401

KAST = 10                       # 1 Kästchen = 10 m
BREITE_K, HOEHE_K = 8, 5        # Platz von (0 | 0) bis (8 | 5)
FEUER = (6, 3)
flaeche = BREITE_K * KAST * HOEHE_K * KAST
QM, PREIS, NEU_QM = 100, 12, 150
preis_neu = Fr(PREIS, QM) * NEU_QM
MIN_FEUER, MIN_BACH = 30, 20    # in m


def d_achse(p, q):
    assert p[0] == q[0] or p[1] == q[1]
    return (abs(p[0] - q[0]) + abs(p[1] - q[1])) * KAST


def name(p):
    return f'({zt(p[0])} | {zt(p[1])})'


opt_d = [(6, 1), (4, 3), (2, 3), (6, 5)]
ok_d = [p for p in opt_d if d_achse(p, FEUER) >= MIN_FEUER]
opt_e = [(2, 1), (1, 3), (6, 0), (4, 3)]


def ok_beide(p):
    if p[1] * KAST < MIN_BACH: return False      # Abstand zum Bach = y-Wert · 10 m
    return d_achse(p, FEUER) >= MIN_FEUER


ok_e = [p for p in opt_e if ok_beide(p)]
assert len(ok_d) == 1 and len(ok_e) == 1 and ok_d[0] not in opt_e

plan = {'typ': 'koordinaten', 'x': [-1, 9], 'y': [-1, 6], 'schritt_x': 1, 'schritt_y': 1,
        'punkte': [{'x': FEUER[0], 'y': FEUER[1], 'name': 'F'}],
        'strecken': [[0, 0, BREITE_K, 0], [BREITE_K, 0, BREITE_K, HOEHE_K], [BREITE_K, HOEHE_K, 0, HOEHE_K], [0, HOEHE_K, 0, 0]]}

teile = [
    luecken('a', 'Der Plan zeigt den Zeltplatz und die Feuerstelle F. Welche Koordinaten hat F?', '(□ | □)', list(FEUER), [str(FEUER[0]), str(FEUER[1])],
            'Erst die x-Koordinate, dann die y-Koordinate.', f'F liegt {FEUER[0]} Kästchen nach rechts und {FEUER[1]} Kästchen nach oben: F {name(FEUER)}.',
            'Erst nach rechts zählen, dann nach oben.', B('geometrie.grundbegriffe', 'koordinaten'), grafik=plan),
    zahl('b', f'Der Zeltplatz ist {BREITE_K * KAST} m lang und {HOEHE_K * KAST} m breit. Wie groß ist sein Flächeninhalt?',
         flaeche, f'{BREITE_K * KAST} * {HOEHE_K * KAST}', f'Flächeninhalt = Länge · Breite = {BREITE_K * KAST} m · {HOEHE_K * KAST} m = {zt(flaeche)} m².',
         'Länge mal Breite.', B('messen.flaechen', 'rechteck'), einheit='m²'),
    zahl('c', f'Für {QM} m² Stellfläche zahlt man {PREIS} € pro Nacht. Was kostet eine Stellfläche von {NEU_QM} m² pro Nacht?',
         preis_neu, f'{PREIS} / 2 * 3',
         f'Geschickt über 50 m²: 50 m² kosten {PREIS} € : 2 = {PREIS // 2} €. {NEU_QM} m² sind 3 · 50 m²: 3 · {PREIS // 2} € = {zt(preis_neu)} €.',
         f'Welche Zwischengröße passt in {QM} und in {NEU_QM}?', B('groessen.proportional', 'dreisatz'), einheit='€'),
    auswahl('d', f'Zelte müssen mindestens {MIN_FEUER} m von der Feuerstelle F {name(FEUER)} entfernt sein (1 Kästchen = {KAST} m). Welcher Platz ist erlaubt?',
            name(ok_d[0]), [name(p) for p in opt_d if p not in ok_d],
            f'{MIN_FEUER} m sind 3 Kästchen. Erlaubt ist alles außerhalb der Kreisfläche um F mit 3 Kästchen Radius (auf dem Rand auch). '
            f'(2 | 3) liegt 4 Kästchen links von F – erlaubt. (6 | 1), (4 | 3) und (6 | 5) sind nur 2 Kästchen von F entfernt.',
            'Zähle für jeden Platz die Kästchen bis F.', B('geometrie.ortslinien', 'kreislinie'), ordnung=[name(p) for p in opt_d]),
    auswahl('e', f'Am unteren Rand (auf der x-Achse) fließt ein Bach. Zelte brauchen mindestens {MIN_BACH} m Abstand zum Bach und mindestens {MIN_FEUER} m '
                 f'zur Feuerstelle F {name(FEUER)}. Welcher Platz erfüllt beide Regeln?',
            name(ok_e[0]), [name(p) for p in opt_e if p not in ok_e],
            f'Abstand zum Bach = y-Koordinate · {KAST} m. {MIN_BACH} m Abstand heißt: y mindestens 2 – alle Punkte auf oder über der Parallelen y = 2. '
            '(2 | 1) und (6 | 0) liegen zu nah am Bach. (4 | 3) ist nur 2 Kästchen (20 m) von F entfernt. '
            f'{name(ok_e[0])} liegt {ok_e[0][1] * KAST} m vom Bach und {d_achse(ok_e[0], FEUER) // KAST} Kästchen ({d_achse(ok_e[0], FEUER)} m) von F entfernt – beides erfüllt.',
            'Prüfe zuerst den Abstand zum Bach, dann den zur Feuerstelle.', B('geometrie.ortslinien', 'parallelen'), ordnung=[name(p) for p in opt_e]),
]

schreibe(expedition('zeltplatz', 'Der Zeltplatz',
                    f'Am Zeltplatz hängt ein Plan mit Koordinatensystem; ein Kästchen sind {KAST} m. Der Platz ist ein Rechteck von (0 | 0) bis ({BREITE_K} | {HOEHE_K}). '
                    'Ihr sucht einen guten Platz für euer Zelt.', teile))
