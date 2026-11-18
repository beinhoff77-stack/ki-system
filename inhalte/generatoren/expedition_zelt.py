#!/usr/bin/env python3
"""Expedition „Zelt“ (Klasse 8): Prisma erkennen · Prismavolumen · Prismaoberfläche · Ungleichung mit Entscheidung.
Aufruf: python3 -I inhalte/generatoren/expedition_zelt.py → inhalte/expeditionen/8-zelt.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

G, H, L, S = Fr('2.4'), Fr('1.6'), 3, 2
assert (G / 2) ** 2 + H ** 2 == S ** 2          # schräge Seite wirklich 2 m
dreieck = G * H / 2
assert dreieck == Fr('1.92') and dreieck * L == Fr('5.76')
O = 2 * dreieck + G * L + 2 * S * L
assert O == Fr('23.04')
# d) kleinste Länge aus 3 / 3,2 / 3,5 m mit Bodenfläche ≥ 5 · 1,5 m²
laengen = [Fr(3), Fr('3.2'), Fr('3.5')]
passend = [x for x in laengen if G * x >= 5 * Fr('1.5')]
assert passend[0] == Fr('3.2') and G * 3 == Fr('7.2') < Fr('7.5') <= G * Fr('3.2') == Fr('7.68')

KD, PV, PO, U = B('messen.koerper_darstellung', 'prisma'), B('messen.prisma_zylinder', 'prisma_volumen'), B('messen.prisma_zylinder', 'prisma_oberflaeche'), B('gleichungen.ungleichungen', 'sachaufgabe')
front = {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [2.4, 0], '_C': [1.2, 1.6], '_F': [1.2, 0]}, 'flaeche': ['_A', '_B', '_C'],
         'linien': [['_A', '_B', '2,4 m'], ['_B', '_C', '2 m'], ['_C', '_A', '2 m'], ['_C', '_F', '1,6 m', 'gestrichelt']], 'rechter_winkel': [['_F', '_B', '_C']]}
schreibe({
    'schluessel': '8-zelt', 'titel': 'Zelt',
    'einleitung': 'Für ein Zeltlager näht eine Gruppe ein eigenes Firstzelt. Von vorn sieht es aus wie ein gleichschenkliges Dreieck: unten 2,4 m breit, 1,6 m hoch, die beiden schrägen Seiten sind je 2 m lang. '
                  'Das Zelt ist 3 m lang und hat einen eingenähten Boden.',
    'voraussetzungen': [KD, PV, PO, U],
    'teile': [
        zahl('a', 'Zuerst baut die Gruppe ein Modell des Zelts aus Holzstäben und Steckverbindern: An jeder Kante des Körpers liegt ein Stab, an jeder Ecke sitzt ein Verbinder. '
                  'Wie viele Teile (Stäbe und Verbinder zusammen) braucht das Modell?',
             15, '9 + 6',
             'Gegeben: Das Zelt ist ein Prisma mit dreieckiger Grundfläche. Gesucht: Kanten + Ecken. Ansatz: 2 Dreiecke mit je 3 Ecken und 3 Kanten, dazu 3 Längskanten. '
             'Rechnung: Ecken 3 + 3 = 6; Kanten 3 + 3 + 3 = 9; 9 + 6 = 15. Antwort: Das Modell braucht 15 Teile.',
             'Welcher Körper ist das? Zähle vorderes Dreieck, hinteres Dreieck und die Verbindungen dazwischen.', KD),
        zahl('b', 'Das vordere Dreieck ist unten 2,4 m breit und 1,6 m hoch, das Zelt ist 3 m lang. Wie viel Luft (in m³) ist im Zelt?', Fr('5.76'), '2.4 * 1.6 / 2 * 3',
             'Gegeben: Dreieck g = 2,4 m, h = 1,6 m, Länge 3 m. Gesucht: Volumen. Ansatz: V = Grundfläche · Höhe des Prismas, Grundfläche = g · h : 2. '
             'Rechnung: 2,4 · 1,6 : 2 = 1,92 m²; 1,92 · 3 = 5,76. Antwort: Im Zelt sind 5,76 m³ Luft.',
             'Die Grundfläche ist das Dreieck vorn – nicht der Boden.', PV, einheit='m³', toleranz=0.01, grafik=front),
        zahl('c', 'Wie viele m² Stoff braucht man für das ganze Zelt – zwei Giebeldreiecke, zwei schräge Dachseiten (je 2 m breit, 3 m lang) und den Boden (2,4 m breit, 3 m lang)? Nähte bleiben unberücksichtigt.',
             Fr('23.04'), '2 * 1.92 + 2.4 * 3 + 2 * 2 * 3',
             'Gegeben: Dreieck 1,92 m², Dachseiten 2 m × 3 m, Boden 2,4 m × 3 m. Gesucht: Oberfläche. Ansatz: O = 2 · Dreieck + Boden + 2 · Dachseite. '
             'Rechnung: 3,84 + 7,2 + 12 = 23,04. Antwort: Man braucht 23,04 m² Stoff.',
             'Zähle alle fünf Flächen des Prismas auf und addiere sie.', PO, einheit='m²', toleranz=0.01),
        auswahl('d', 'Für die nächste Fahrt soll ein ähnliches Zelt mit ebenfalls 2,4 m Breite für 5 Personen genäht werden. Jede Person braucht mindestens 1,5 m² Bodenfläche. '
                     'Als Länge stehen 3 m, 3,2 m und 3,5 m zur Auswahl. Welche Länge ist die kürzeste, die ausreicht?',
                '3,2 m', ['3 m', '3,5 m', 'Keine der drei Längen reicht aus.'],
                'Gegeben: Breite 2,4 m, 5 Personen, je mindestens 1,5 m². Gesucht: kleinste ausreichende Länge x. Ansatz: 2,4 · x ≥ 5 · 1,5 = 7,5. '
                'Rechnung: x ≥ 7,5 : 2,4 = 3,125. 3 m: 7,2 m² – zu wenig; 3,2 m: 7,68 m² – reicht; 3,5 m: 8,4 m² – reicht auch, ist aber länger. '
                'Antwort: 3,2 m ist die kürzeste Länge, die ausreicht.',
                'Stelle die Ungleichung für die Bodenfläche auf und prüfe alle drei Längen.', U, pos=1),
    ],
})
