#!/usr/bin/env python3
"""Expedition „Das Aquarium“ (Klasse 5) – Quader, Oberfläche ohne Deckel, Gleichung aufstellen, Preise vergleichen.
Aufruf: python3 -I inhalte/generatoren/expedition_aquarium.py → inhalte/expeditionen/5-aquarium.json"""
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _expedition_kl5 import B, auswahl, expedition, luecken, roemisch_wert, schreibe, zahl, zahlwort, zt  # noqa: E402,F401

L, BR, H = 60, 30, 40
kanten = 4 * (L + BR + H)
glas = L * BR + 2 * L * H + 2 * BR * H
PUMPE, GESAMT, PFLANZEN = 41, 59, 3
pflanze = Fr(GESAMT - PUMPE, PFLANZEN)
assert pflanze.denominator == 1
A_JE, A_PRO, B_PAUSCH = 4, 1000, 40
preis_a = Fr(A_JE * glas, A_PRO)
diff = B_PAUSCH - preis_a
assert diff > 0
antworten = [f'Glaserei A, sie ist {zt(diff)} € günstiger.', f'Glaserei B, sie ist {zt(diff)} € günstiger.', 'Beide kosten gleich viel.', f'Glaserei A, sie ist {zt(preis_a)} € günstiger.']

teile = [
    zahl('a', f'Das Aquarium ist ein Quader: {L} cm lang, {BR} cm breit und {H} cm hoch. Ein Rahmen aus Aluminium läuft an allen Kanten entlang. '
              'Wie viele cm Aluminium braucht man?',
         kanten, f'4 * ({L} + {BR} + {H})', f'Ein Quader hat je 4 Kanten in Länge, Breite und Höhe: 4 · ({L} + {BR} + {H}) cm = 4 · {L + BR + H} cm = {kanten} cm.',
         'Wie viele Kanten hat ein Quader, und wie viele davon sind gleich lang?', B('messen.koerper_berechnung', 'quader'), einheit='cm'),
    zahl('b', f'Das Aquarium ({L} cm lang, {BR} cm breit, {H} cm hoch) hat keinen Deckel. Wie viele cm² Glas braucht man für Boden und Seiten?',
         glas, f'{L} * {BR} + 2 * {L} * {H} + 2 * {BR} * {H}',
         f'Boden: {L} · {BR} = {zt(L * BR)} cm². Vorne und hinten: 2 · {L} · {H} = {zt(2 * L * H)} cm². Links und rechts: 2 · {BR} · {H} = {zt(2 * BR * H)} cm². '
         f'Zusammen {zt(glas)} cm² (der Deckel fehlt).',
         'Welche der sechs Flächen fehlt?', B('messen.koerper_berechnung', 'sachaufgaben'), einheit='cm²'),
    zahl('c', f'Für {PFLANZEN} gleich teure Wasserpflanzen und eine Pumpe für {PUMPE} € zahlst du zusammen {GESAMT} €. Wie viel kostet eine Pflanze?',
         pflanze, f'({GESAMT} - {PUMPE}) / {PFLANZEN}',
         f'Gleichung: {PFLANZEN} · □ + {PUMPE} = {GESAMT}. Rückwärts: {GESAMT} − {PUMPE} = {GESAMT - PUMPE}, dann {GESAMT - PUMPE} : {PFLANZEN} = {zt(pflanze)}. '
         f'Eine Pflanze kostet {zt(pflanze)} €. Probe: {PFLANZEN} · {zt(pflanze)} + {PUMPE} = {GESAMT}.',
         'Schreib eine Gleichung mit einem Kästchen für den Preis einer Pflanze.', B('gleichungen.einfach', 'aufstellen'), einheit='€'),
    auswahl('d', f'Für {zt(glas)} cm² Glas gibt es zwei Angebote: Glaserei A verlangt {A_JE} € je {zt(A_PRO)} cm², Glaserei B {B_PAUSCH} € für alles. '
                 'Welches Angebot nimmst du?',
            antworten[0], antworten[1:],
            f'A: {zt(glas)} cm² sind {glas // A_PRO} · {zt(A_PRO)} cm², also {glas // A_PRO} · {A_JE} € = {zt(preis_a)} €. B: {B_PAUSCH} €. '
            f'A ist um {B_PAUSCH} € − {zt(preis_a)} € = {zt(diff)} € günstiger.',
            f'Wie oft passen {zt(A_PRO)} cm² in {zt(glas)} cm²?', B('groessen.proportional', 'einheit'), ordnung=antworten),
]

schreibe(expedition('aquarium', 'Das Aquarium',
                    'Auf deiner Reise hilfst du in einem Zoogeschäft. Ihr plant ein neues Aquarium in Quaderform ohne Deckel, '
                    f'{L} cm lang, {BR} cm breit und {H} cm hoch. Dafür braucht ihr Glas, einen Rahmen, Pflanzen und eine Pumpe.', teile))
