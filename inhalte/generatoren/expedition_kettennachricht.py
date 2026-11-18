#!/usr/bin/env python3
"""Expedition „Die Kettennachricht“ (Klasse 5) – Potenzen, große Zahlen lesen und vergleichen, Zeitspannen.
Aufruf: python3 -I inhalte/generatoren/expedition_kettennachricht.py → inhalte/expeditionen/5-kettennachricht.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401

JE = 3
runde = lambda n: JE ** n
erste_ueber_1000 = next(n for n in range(1, 30) if runde(n) > 1000)
R12 = runde(12)
MIN_JE, RUNDEN = 17, 12
h, m = divmod(MIN_JE * RUNDEN, 60)
STADT = 600000
assert erste_ueber_1000 == 7 and R12 == 531441 and runde(13) == 1594323 and (h, m) == (3, 24)
wort = zahlwort(R12)
assert wort == 'fünfhunderteinunddreißigtausendvierhunderteinundvierzig'
falsch_w = [zahlwort(513441), 'fünf Millionen dreihunderteinundvierzigtausendvierhunderteinundvierzig', zahlwort(531414)]
pot = ['3⁴', '4³', '3 · 4', '4 + 3']
e_ant = [f'Nein: In Runde 13 bräuchte man {zt(runde(13))} neue Personen – mehr, als die Stadt Einwohner hat.',
         f'Ja: In Runde 13 sind es nur {zt(R12)} Personen.', 'Ja: Die Zahl der Personen bleibt ab Runde 12 gleich.', 'Nein: Schon in Runde 5 sind es mehr als 600 000.']

tabelle = {'typ': 'tabelle', 'kopf': ['Runde', '1', '2', '3', '4'], 'zeilen': [['neue Personen'] + [zt(runde(n)) for n in range(1, 5)]]}

teile = [
    auswahl('a', 'In Runde 4 bekommen 3 · 3 · 3 · 3 = 81 Personen das Foto. Welche Schreibweise passt dazu?', pot[0], pot[1:],
            '3 · 3 · 3 · 3: Die 3 kommt viermal als Faktor vor. Basis 3, Exponent 4: 3⁴ = 81. 4³ wäre 4 · 4 · 4 = 64.',
            'Welche Zahl wird malgenommen, und wie oft?', B('zahlen.potenzen_basis', 'schreibweise'), grafik=tabelle, ordnung=pot),
    zahl('b', 'In Runde 4 sind es 3⁴ = 81 neue Personen, in Runde 5 schon 3⁵, in Runde 6 dann 3⁶. In welcher Runde bekommen zum ersten Mal mehr als 1 000 Personen das Foto?',
         erste_ueber_1000, f'{erste_ueber_1000}',
         f'3⁵ = 243, 3⁶ = 729, 3⁷ = {zt(runde(7))}. Erst in Runde {erste_ueber_1000} sind es mehr als 1 000.',
         'Nimm immer wieder mal 3: 81, 243, …', B('zahlen.potenzen_basis', 'berechnen')),
    auswahl('c', f'In Runde 12 wären es 3¹² = {zt(R12)} Personen. Wie liest man diese Zahl?', wort, falsch_w,
            f'Dreiergruppen von rechts: {zt(R12)} = 531 Tausender und 441 Einer: fünfhunderteinunddreißigtausend vierhunderteinundvierzig.',
            'Teile die Zahl in Dreiergruppen und lies zuerst die Tausendergruppe.', B('zahlen.natuerlich', 'ziffern_zu_zahlwort'),
            ordnung=[falsch_w[0], wort, falsch_w[1], falsch_w[2]]),
    luecken('d', f'Jede Runde dauert {MIN_JE} Minuten. Wie lange dauern {RUNDEN} Runden? Gib das Ergebnis in Stunden und Minuten an.',
            '□ h □ min', [h, m], [f'{MIN_JE} * {RUNDEN} // 60', f'{MIN_JE} * {RUNDEN} - 60 * ({MIN_JE} * {RUNDEN} // 60)'], 'Je Lücke eine ganze Zahl.',
            f'{RUNDEN} · {MIN_JE} min = {MIN_JE * RUNDEN} min. 3 · 60 min = 180 min, es bleiben {MIN_JE * RUNDEN} − 180 = {m} min: {h} h {m} min.',
            'Rechne erst alle Minuten aus, dann in Stunden um.', B('groessen.einheiten', 'zeit')),
    auswahl('e', f'Eine Stadt hat {zt(STADT)} Einwohner. In Runde 12 bekommen {zt(R12)} Personen das Foto, in Runde 13 wären es {zt(runde(13))}. '
                 'Kann die Kettennachricht bis Runde 13 weiterlaufen, wenn nur Menschen aus dieser Stadt mitmachen?',
            e_ant[0], e_ant[1:],
            f'{zt(runde(13))} hat sieben Stellen, {zt(STADT)} nur sechs: {zt(runde(13))} > {zt(STADT)}. Allein in Runde 13 bräuchte man mehr neue Personen, '
            'als die Stadt Einwohner hat – die Kette muss vorher abbrechen.',
            'Vergleiche zuerst die Zahl der Stellen.', B('zahlen.natuerlich', 'vergleichen'), ordnung=e_ant),
]

schreibe(expedition('kettennachricht', 'Die Kettennachricht',
                    'In einem Reise-Chat wird ein Foto weitergeleitet. In Runde 1 schickt eine Person es an 3 andere. In jeder weiteren Runde schickt '
                    'jede neue Person es an 3 Personen, die es noch nicht haben. Die Tabelle zeigt die ersten Runden.', teile))
