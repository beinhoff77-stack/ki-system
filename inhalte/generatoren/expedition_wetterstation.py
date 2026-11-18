#!/usr/bin/env python3
"""Expedition „Die Wetterstation“ (Klasse 5) – ganze Zahlen, Mittelwert mit ganzen Zahlen, Zeit.
Aufruf: python3 -I inhalte/generatoren/expedition_wetterstation.py → inhalte/expeditionen/5-wetterstation.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, schreibe, zahl, zt

TAGE = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
TIEF = [-4, 2, -9, -1, 0, -6, -3]
kaltester = TAGE[TIEF.index(min(TIEF))]
MORGEN, MITTAG = -9, 6
mittel = Fr(sum(TIEF), 7)
assert mittel.denominator == 1
START_H, START_M, PRO_H = 6, 40, 3
stunden = Fr(0 - MORGEN, PRO_H)
assert stunden.denominator == 1
ziel_h, ziel_m = START_H + int(stunden), START_M

tabelle = {'typ': 'tabelle', 'kopf': ['Tag', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'], 'zeilen': [['Tiefstwert in °C'] + [zt(t) for t in TIEF]]}
liste = ', '.join(f'{t[:2]} {zt(v)} °C' for t, v in zip(TAGE, TIEF))

teile = [
    auswahl('a', f'Die Tabelle zeigt die Tiefstwerte einer Woche: {liste}. An welchem Tag war es am kältesten?',
            kaltester, ['Samstag', 'Montag', 'Freitag'],
            f'Am kältesten ist die kleinste Zahl. Auf der Zahlengeraden liegt {zt(min(TIEF))} am weitesten links: {kaltester}.',
            'Kälter heißt: weiter links auf der Zahlengeraden.', B('zahlen.ganz', 'ordnen'), grafik=tabelle,
            ordnung=['Montag', kaltester, 'Freitag', 'Samstag']),
    zahl('b', f'Am Mittwoch zeigt das Thermometer morgens {zt(MORGEN)} °C und mittags {zt(MITTAG)} °C. Um wie viel Grad ist es wärmer geworden?',
         MITTAG - MORGEN, f'{MITTAG} - ({MORGEN})',
         f'Von {zt(MORGEN)} °C bis 0 °C sind es {-MORGEN} Grad, dann noch {MITTAG} Grad bis {MITTAG} °C: {-MORGEN} + {MITTAG} = {MITTAG - MORGEN} Grad. '
         f'Als Rechnung: {MITTAG} − ({zt(MORGEN)}) = {MITTAG - MORGEN}.',
         'Rechne in zwei Teilen: bis 0 °C und dann weiter.', B('zahlen.ganz', 'sach'), einheit='Grad'),
    zahl('c', 'Den Mittelwert einer Woche berechnet die Station so: alle sieben Tiefstwerte addieren und die Summe durch 7 teilen. '
              f'Die Werte sind {", ".join(zt(t) for t in TIEF[:-1])} und {zt(TIEF[-1])} (in °C). Wie groß ist der Mittelwert?',
         mittel, '(' + ' + '.join(f'({t})' for t in TIEF) + ') / 7',
         f'Summe: {" + ".join(f"({zt(t)})" if t < 0 else zt(t) for t in TIEF)} = {zt(sum(TIEF))}. '
         f'Geteilt durch 7: ({zt(sum(TIEF))}) : 7 = {zt(mittel)} °C (negativ geteilt durch positiv ergibt negativ).',
         'Fasse erst die positiven und die negativen Werte getrennt zusammen.', B('zahlen.rechengesetze', 'geteilt_ganz'), einheit='°C'),
    luecken('d', f'Am Mittwoch um {START_H}:{START_M:02d} Uhr misst die Station {zt(MORGEN)} °C. Danach wird es jede Stunde gleichmäßig {PRO_H} Grad wärmer. '
                 'Eine Wandergruppe will erst losgehen, wenn das Thermometer 0 °C erreicht. Um wie viel Uhr ist das frühestens?',
            '□:□ Uhr', [ziel_h, ziel_m], [f'{START_H} + {-MORGEN} // {PRO_H}', f'{START_M}'], 'Stunden und Minuten je als ganze Zahl.',
            f'Bis 0 °C fehlen {-MORGEN} Grad. Bei {PRO_H} Grad pro Stunde dauert das {-MORGEN} : {PRO_H} = {int(stunden)} Stunden. '
            f'{START_H}:{START_M:02d} Uhr + {int(stunden)} h = {ziel_h}:{ziel_m:02d} Uhr.',
            'Wie viele Grad fehlen bis 0 °C, und wie lange dauert das?', B('groessen.einheiten', 'zeit')),
]

schreibe(expedition('wetterstation', 'Die Wetterstation',
                    'Auf deiner Reise besuchst du eine Wetterstation in den Bergen. Dort werden jeden Tag die tiefste Temperatur, die Uhrzeiten der Messungen '
                    'und Mittelwerte notiert. Hilf beim Auswerten der Woche.', teile))
