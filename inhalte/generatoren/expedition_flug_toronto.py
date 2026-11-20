#!/usr/bin/env python3
"""Expedition „Flug nach Toronto“ (Klasse 5) – Zeitspannen, Zeitverschiebung mit ganzen Zahlen, Zählprinzip, Dreisatz, Massen.
Aufruf: python3 -I inhalte/generatoren/expedition_flug_toronto.py → inhalte/expeditionen/5-flug_toronto.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401

AB_H, AB_M, DAUER_H, DAUER_M = 10, 15, 9, 40
an_min = (AB_H * 60 + AB_M + DAUER_H * 60 + DAUER_M)
an_h, an_m = divmod(an_min, 60)
assert AB_M + DAUER_M < 60  # Lösungsweg ohne Übertrag
VERSCH = -6
to_h = an_h + VERSCH
assert (an_h, an_m) == (19, 55) and to_h == 13
HOSEN, SHIRTS, PULLIS = 3, 4, 2
WAESCHE_KG, WAESCHE_DOLLAR, NEU_KG = 3, 12, 5
waesche = Fr(WAESCHE_DOLLAR, WAESCHE_KG) * NEU_KG
FAHRT_H, FAHRT_M, SCHLUSS = 1, 30, 16          # Fahrt vom Flughafen zum Hotel, Wäscherei nimmt bis 16:00 Uhr an
hotel_min = to_h * 60 + an_m + FAHRT_H * 60 + FAHRT_M
hotel_h, hotel_m = divmod(hotel_min, 60)
assert hotel_min < SCHLUSS * 60 and (hotel_h, hotel_m) == (15, 25)
d_ant = [f'Ja: Ihr seid um {hotel_h}:{hotel_m:02d} Uhr im Hotel, das Waschen kostet {zt(waesche)} Dollar.',
         f'Nein: Ihr seid erst um {hotel_h + 1}:{hotel_m:02d} Uhr im Hotel.',
         f'Ja: Ihr seid um {hotel_h}:{hotel_m:02d} Uhr im Hotel, das Waschen kostet {WAESCHE_DOLLAR * NEU_KG} Dollar.',
         f'Ja: Ihr seid um {hotel_h}:{hotel_m:02d} Uhr im Hotel, das Waschen kostet {WAESCHE_DOLLAR + NEU_KG - WAESCHE_KG} Dollar.']
assert len(set(d_ant)) == 4
KOFFER_G, ERLAUBT_G = 25300, 23000
teilsachen = {'Schuhe': 1200, 'Hose': 900, 'Pullover': 600, 'Buch': 500}
kombis = [('Schuhe', 'Hose'), ('Schuhe', 'Pullover', 'Buch'), ('Schuhe', 'Hose', 'Buch'), ('Hose', 'Pullover')]
reicht = [k for k in kombis if KOFFER_G - sum(teilsachen[t] for t in k) <= ERLAUBT_G]
beste = min(reicht, key=lambda k: sum(teilsachen[t] for t in k))
# kein anderer Teil der Sachen (auch außerhalb der Antworten) bringt mit weniger Gewicht unter 23 kg
from itertools import combinations
alle = [c for r in range(1, 5) for c in combinations(teilsachen, r) if KOFFER_G - sum(teilsachen[t] for t in c) <= ERLAUBT_G]
assert min(sum(teilsachen[t] for t in c) for c in alle) == sum(teilsachen[t] for t in beste)
assert len([c for c in alle if sum(teilsachen[t] for t in c) == sum(teilsachen[t] for t in beste)]) == 1
txt = lambda k: ', '.join(k[:-1]) + ' und ' + k[-1]

teile = [
    luecken('a', f'Der Flug startet in Berlin um {AB_H}:{AB_M:02d} Uhr und dauert {DAUER_H} h {DAUER_M} min. Wie spät ist es bei der Landung nach Berliner Zeit?',
            '□:□ Uhr', [an_h, an_m], [f'({AB_H} * 60 + {AB_M} + {DAUER_H} * 60 + {DAUER_M}) // 60', f'{AB_M} + {DAUER_M}'],
            'Stunden und Minuten je als ganze Zahl.',
            f'{AB_H}:{AB_M:02d} Uhr + {DAUER_H} h = {AB_H + DAUER_H}:{AB_M:02d} Uhr. Dazu {DAUER_M} min: {AB_M} + {DAUER_M} = {AB_M + DAUER_M} min, '
            f'also {an_h}:{an_m:02d} Uhr.',
            'Addiere erst die Stunden, dann die Minuten. 60 Minuten sind eine Stunde.', B('groessen.einheiten', 'zeit')),
    luecken('b', f'In Toronto gehen die Uhren anders. Für diesen Reisetag gilt (Annahme): Toronto-Zeit = Berliner Zeit + ({zt(VERSCH)} h), also 6 Stunden weniger. '
                 f'In Berlin ist es bei der Landung {an_h}:{an_m:02d} Uhr. Wie spät ist es in Toronto?',
            '□:□ Uhr', [to_h, an_m], [f'{an_h} + ({VERSCH})', f'{an_m}'], 'Stunden und Minuten je als ganze Zahl.',
            f'{an_h} + ({zt(VERSCH)}) = {an_h} − {-VERSCH} = {to_h}. Die Minuten bleiben: {to_h}:{an_m:02d} Uhr.',
            'Eine negative Zahl addieren heißt: abziehen.', B('zahlen.ganz', 'sach')),
    zahl('c', f'Im Koffer sind {HOSEN} Hosen, {SHIRTS} T-Shirts und {PULLIS} Pullover. Ein Outfit besteht aus je einer Hose, einem T-Shirt und einem Pullover. '
              'Wie viele verschiedene Outfits gibt es?',
         HOSEN * SHIRTS * PULLIS, f'{HOSEN} * {SHIRTS} * {PULLIS}',
         f'Zu jeder Hose passen {SHIRTS} T-Shirts: {HOSEN} · {SHIRTS} = {HOSEN * SHIRTS}. Zu jeder dieser Kombinationen passen {PULLIS} Pullover: '
         f'{HOSEN * SHIRTS} · {PULLIS} = {HOSEN * SHIRTS * PULLIS}.',
         'Zählprinzip: die Anzahlen malnehmen.', B('stochastik.kombinatorik', 'zaehlprinzip')),
    auswahl('d', f'Ihr landet um {to_h}:{an_m:02d} Uhr Toronto-Zeit. Von der Landung bis zur Ankunft im Hotel vergehen insgesamt {FAHRT_H} h {FAHRT_M} min – einschließlich Aussteigen, Gepäckabholen und Fahrt. Die Hotelwäscherei nimmt nur bis {SCHLUSS}:00 Uhr Wäsche an; '
                 f'{WAESCHE_KG} kg Wäsche kosten dort {WAESCHE_DOLLAR} Dollar. Ihr wollt noch heute {NEU_KG} kg Wäsche abgeben. Schafft ihr das, und was kostet es?',
            d_ant[0], d_ant[1:],
            f'Ankunft im Hotel: {to_h}:{an_m:02d} Uhr + {FAHRT_H} h {FAHRT_M} min = {hotel_h}:{hotel_m:02d} Uhr – vor {SCHLUSS}:00 Uhr. '
            f'1 kg kostet {WAESCHE_DOLLAR} : {WAESCHE_KG} = {WAESCHE_DOLLAR // WAESCHE_KG} Dollar, {NEU_KG} kg kosten {NEU_KG} · {WAESCHE_DOLLAR // WAESCHE_KG} = {zt(waesche)} Dollar.',
            'Rechne erst die Ankunft im Hotel aus, dann den Preis für 1 kg.', B('groessen.proportional', 'dreisatz'), ordnung=d_ant),
    auswahl('e', f'Nach der Reise wiegt der Koffer mit der gewaschenen Wäsche und den Andenken für den Rückflug {zt(KOFFER_G // 1000)} kg {KOFFER_G % 1000} g, erlaubt sind {ERLAUBT_G // 1000} kg. '
                 'Du kannst herausnehmen: Schuhe (1 kg 200 g), Hose (900 g), Pullover (600 g), Buch (500 g). '
                 'Du willst so wenig Gewicht wie möglich herausnehmen. Was nimmst du heraus?',
            txt(beste), [txt(k) for k in kombis if k != beste],
            f'Herausnehmen musst du mindestens {zt(KOFFER_G)} g − {zt(ERLAUBT_G)} g = {zt(KOFFER_G - ERLAUBT_G)} g. '
            'Schuhe und Hose: 2 100 g – zu wenig. Hose und Pullover: 1 500 g – zu wenig. Schuhe, Hose und Buch: 2 600 g – reicht, ist aber mehr als nötig. '
            'Schuhe, Pullover und Buch: 1 200 g + 600 g + 500 g = 2 300 g – genau so viel wie nötig.',
            'Rechne alles in Gramm um. Wie viel Gramm sind zu viel?', B('groessen.einheiten', 'masse'), ordnung=[txt(k) for k in kombis]),
]

schreibe(expedition('flug_toronto', 'Flug nach Toronto',
                    'Deine Familie fliegt von Berlin nach Toronto. Du planst den Reisetag: Wann landet ihr, wann seid ihr im Hotel, schafft ihr es noch zur Wäscherei – '
                    'und passt am Ende alles wieder in den Koffer? '
                    'Im Flugzeug sind 23 kg Gepäck erlaubt.', teile))
