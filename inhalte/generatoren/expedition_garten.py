#!/usr/bin/env python3
"""Expedition „Gemüsegarten“ (Klasse 8): Trapezfläche · Produktgleichheit · Funktionswert · Ungleichung mit Entscheidung.
Aufruf: python3 -I inhalte/generatoren/expedition_garten.py → inhalte/expeditionen/8-garten.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

A = Fr(8 + 5, 2) * 4
assert A == 26
assert 12 * 8 == 96 and Fr(96, 16) == 6
W = lambda t: 200 - 15 * t
assert W(8) == 80 and W(12) == 20 and W(13) < 20
t_max = max(t for t in range(30) if W(t) >= 20)
assert t_max == 12

T, P, F, U = B('messen.flaechen_vielecke', 'trapez'), B('groessen.indirekt', 'produkt'), B('funktionen.grundbegriffe', 'funktionswert'), B('gleichungen.ungleichungen', 'sachaufgabe')
fig = {'typ': 'figur', 'punkte': {'_A': [0, 0], '_B': [8, 0], '_C': [6.5, 4], '_D': [1.5, 4], '_F': [1.5, 0]},
       'flaeche': ['_A', '_B', '_C', '_D'], 'linien': [['_A', '_B', '8 m'], ['_B', '_C', ''], ['_C', '_D', '5 m'], ['_D', '_A', ''], ['_D', '_F', '4 m', 'gestrichelt']],
       'rechter_winkel': [['_F', '_B', '_D']]}
schreibe({
    'schluessel': '8-garten', 'titel': 'Gemüsegarten',
    'einleitung': 'Im Schulgarten bekommt deine Klasse ein trapezförmiges Beet. Dort sollen Salatpflanzen in gleich langen Reihen wachsen. '
                  'Gegossen wird mit Regenwasser aus einer großen Tonne, solange es nicht regnet.',
    'voraussetzungen': [T, P, F, U],
    'teile': [
        zahl('a', 'Das Beet ist ein Trapez: Die parallelen Seiten sind 8 m und 5 m lang, ihr Abstand beträgt 4 m. Wie groß ist das Beet?', A, '(8 + 5) / 2 * 4',
             'Gegeben: a = 8 m, c = 5 m, h = 4 m. Gesucht: Flächeninhalt. Ansatz: A = (a + c) : 2 · h. Rechnung: 13 : 2 · 4 = 26. Antwort: Das Beet ist 26 m² groß.',
             'Mittelwert der parallelen Seiten mal Abstand.', T, einheit='m²', grafik=fig),
        zahl('b', 'Es sollen 96 Salatpflanzen gesetzt werden, in jede Reihe gleich viele. Bei 12 Reihen stehen 8 Pflanzen in jeder Reihe. '
                  'Das Beet bekommt aber 16 Reihen. Wie viele Pflanzen kommen dann in jede Reihe?', 6, '96 / 16',
             'Gegeben: 96 Pflanzen, 12 Reihen zu je 8. Gesucht: Pflanzen pro Reihe bei 16 Reihen. Ansatz: Reihen · Pflanzen pro Reihe = 96 bleibt gleich. '
             'Rechnung: 96 : 16 = 6. Antwort: In jede Reihe kommen 6 Pflanzen.',
             'Welches Produkt bleibt gleich, wenn sich die Reihenzahl ändert?', P),
        zahl('c', 'In der Regentonne sind 200 Liter. Jeden Tag werden 15 Liter zum Gießen entnommen; nach t Tagen sind noch W(t) = 200 − 15 · t Liter darin. '
                  'Wie viele Liter sind nach 8 Tagen noch in der Tonne?', W(8), '200 - 15 * 8',
             'Gegeben: W(t) = 200 − 15t. Gesucht: W(8). Ansatz: 8 für t einsetzen. Rechnung: 200 − 120 = 80. Antwort: Nach 8 Tagen sind noch 80 l in der Tonne.',
             'Setze t = 8 in den Term ein.', F, einheit='l'),
        auswahl('d', 'Nach t Tagen ohne Regen sind noch 200 − 15 · t Liter in der Tonne. Für heiße Tage sollen immer mindestens 20 Liter in Reserve bleiben. '
                     'Der Wetterbericht sagt 12 Tage ohne Regen voraus. Reicht das Wasser zum Gießen, ohne die Reserve anzugreifen?',
                'Ja: Nach 12 Tagen sind noch genau 20 Liter darin – die Reserve bleibt.',
                ['Nein: Die Tonne ist nach 12 Tagen leer.', 'Nein: Schon nach 10 Tagen ist die Reserve angebrochen.', 'Ja: Es würde sogar 14 Tage reichen.'],
                'Gegeben: 200 − 15t, mindestens 20 l. Gesucht: Reicht es 12 Tage? Ansatz: 200 − 15t ≥ 20. Rechnung: −15t ≥ −180 ⇒ t ≤ 12 (Zeichen dreht sich). '
                'Nach 12 Tagen: 200 − 180 = 20 l; nach 10 Tagen sind es noch 50 l, für 14 Tage bräuchte man 210 l, es sind aber nur 200 l da. Antwort: Ja, genau 12 Tage reicht es.',
                'Stelle eine Ungleichung mit „mindestens 20 Liter“ auf.', U),
    ],
})
