#!/usr/bin/env python3
"""Expedition „Die Römerstraße“ (Klasse 5) – römische Zahlen, Längen, Zahlenstrahl, Vielfache.
Aufruf: python3 -I inhalte/generatoren/expedition_roemerstrasse.py → inhalte/expeditionen/5-roemerstrasse.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401

STEIN = 'CXLIV'
meilen = roemisch_wert(STEIN)
M_LANG = 1480                      # eine römische Meile ≈ 1 480 m
gesamt_m = meilen * M_LANG
km, m = divmod(gesamt_m, 1000)
ENDE, ABSCHN, PFEIL = 120, 8, 5
rast = ENDE * PFEIL // ABSCHN
BRUNNEN, WACHE = 12, 18
beide = lcm(BRUNNEN, WACHE)

teile = [
    zahl('a', f'Auf einem Meilenstein steht {STEIN}. Welche Zahl ist das?', meilen, '100 + 40 + 4',
         f'C = 100, XL = 50 − 10 = 40, IV = 5 − 1 = 4. Zusammen 100 + 40 + 4 = {meilen}.',
         'Steht ein kleineres Zeichen vor einem größeren, wird es abgezogen.', B('zahlen.natuerlich', 'roemisch_system')),
    luecken('b', f'Der Meilenstein zeigt, wie weit diese Stelle vom Anfang der Straße (Meile 0) entfernt ist – gewandert bist du selbst nur ein kurzes Stück. '
                 f'Eine römische Meile ist etwa {zt(M_LANG)} m lang. Wie weit ist es von Meile 0 bis zu diesem Stein? Gib das Ergebnis in km und m an.',
            '□ km □ m', [km, m], [f'{meilen} * {M_LANG} // 1000', f'{meilen} * {M_LANG} - 1000 * ({meilen} * {M_LANG} // 1000)'],
            'Je Lücke eine ganze Zahl.',
            f'{meilen} · {zt(M_LANG)} m = {zt(gesamt_m)} m. 1 000 m = 1 km, also {zt(gesamt_m)} m = {km} km {m} m.',
            'Rechne zuerst alles in Metern aus.', B('groessen.einheiten', 'laenge')),
    zahl('c', f'Die Wanderkarte zeigt die Straße als Zahlenstrahl von Meile 0 bis Meile {ENDE} mit {ABSCHN} gleichen Abschnitten. '
              'Der Pfeil zeigt auf einen Rastplatz. Bei welcher Meile liegt er?',
         rast, f'{ENDE} // {ABSCHN} * {PFEIL}',
         f'Ein Abschnitt ist {ENDE} : {ABSCHN} = {ENDE // ABSCHN} Meilen lang. Der Pfeil liegt {PFEIL} Abschnitte nach der 0: {PFEIL} · {ENDE // ABSCHN} = {rast}.',
         'Wie viele Meilen ist ein Abschnitt lang?', B('zahlen.natuerlich', 'strahl_ablesen'),
         grafik={'typ': 'zahlenstrahl', 'start': 0, 'ende': ENDE, 'abschnitte': ABSCHN, 'beschriftet': 'anfang_ende', 'pfeil': PFEIL}),
    zahl('d', f'Ab Meile 0 steht alle {BRUNNEN} Meilen ein Brunnen und alle {WACHE} Meilen ein Wachposten. Du willst die erste Nacht an einer Stelle '
              'verbringen, an der es beides gibt – aber nicht schon bei Meile 0. Bei welcher Meile ist das?',
         beide, f'{beide}',
         f'Brunnen: {", ".join(str(BRUNNEN * i) for i in range(1, 5))}, … Wachposten: {", ".join(str(WACHE * i) for i in range(1, 4))}, … '
         f'Die erste Zahl in beiden Listen ist {beide}.',
         f'Schreib die Vielfachen von {BRUNNEN} und von {WACHE} auf.', B('zahlen.teilbarkeit', 'vielfache')),
]
assert beide == 36 and rast == 75

schreibe(expedition('roemerstrasse', 'Die Römerstraße',
                    'Bei Rom wanderst du ein Stück auf einer alten Römerstraße. Am Rand stehen Meilensteine mit römischen Zahlen. '
                    'Eine römische Meile ist etwa 1 480 m lang.', teile))
