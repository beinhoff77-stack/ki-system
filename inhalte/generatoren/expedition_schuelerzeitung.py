#!/usr/bin/env python3
"""Expedition „Schülerzeitung“ (Klasse 8): Bruchterm auswerten · Bruchgleichung · waagrechte Asymptote deuten · lineare Funktionen schneiden mit Entscheidung.
Aufruf: python3 -I inhalte/generatoren/expedition_schuelerzeitung.py → inhalte/expeditionen/8-schuelerzeitung.json"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _exp8 import B, PI, zt, zahl, luecken, auswahl, schreibe  # noqa: E402,F401

FIX, ST, VK = 180, Fr('0.6'), Fr('1.5')
k = lambda x: FIX / Fr(x) + ST  # noqa: E731
assert k(150) == Fr('1.8') and k(450) == 1
assert all(k(x) > ST for x in range(1, 100001, 7))
# d) Gewinngrenze E(x) = 1,5x, K(x) = 180 + 0,6x
grenze = Fr(FIX) / (VK - ST)
assert grenze == 200
assert VK * 160 - (FIX + ST * 160) == -36
assert min(x for x in range(1, 1000) if VK * x >= FIX + ST * x) == 200

T, E, A, S = B('terme.bruchterme', 'termwert'), B('gleichungen.bruch', 'ein_bruch'), B('funktionen.gebrochen', 'asymptoten'), B('funktionen.linear', 'schnittpunkte')
graph = {'typ': 'koordinaten', 'x': [0, 600], 'y': [0, 3], 'schritt_x': 100, 'schritt_y': 0.5,
         'graphen': [{'art': 'hyperbel', 'a': FIX, 'b': 0, 'c': 0.6, 'bereich': [60, 600], 'name': 'k'}],
         'name_x': 'Hefte', 'name_y': '€ pro Heft'}
schreibe({
    'schluessel': '8-schuelerzeitung', 'titel': 'Schülerzeitung',
    'einleitung': 'Eure Schülerzeitung wird in einer Druckerei gedruckt. Für jede Ausgabe zahlt ihr einmalig 180 € für das Einrichten der Maschine und zusätzlich 0,60 € pro gedrucktem Heft. '
                  'Je mehr Hefte gedruckt werden, desto weniger kostet deshalb ein einzelnes Heft: Bei x Heften sind es k(x) = 180/x + 0,6 Euro pro Heft.',
    'voraussetzungen': [T, E, A, S],
    'teile': [
        zahl('a', 'Wie viel Euro kostet ein einzelnes Heft, wenn 150 Hefte gedruckt werden?', Fr('1.8'), '180 / 150 + 0.6',
             'Gegeben: k(x) = 180/x + 0,6, x = 150. Gesucht: k(150). Ansatz: einsetzen. Rechnung: 180 : 150 = 1,20; 1,20 + 0,60 = 1,80. '
             'Antwort: Ein Heft kostet dann 1,80 €.',
             'Setze 150 für x ein und rechne den Bruch zuerst aus.', T, einheit='€', toleranz=0.01),
        zahl('b', 'Ein Heft soll in der Herstellung genau 1 € kosten. Wie viele Hefte müssen dafür gedruckt werden?', 450, '180 / (1 - 0.6)',
             'Gegeben: 180/x + 0,6 = 1, x > 0. Gesucht: x. Ansatz: 0,6 abziehen, dann mit x multiplizieren. Rechnung: 180/x = 0,4 ⇒ 180 = 0,4x ⇒ x = 450. '
             'Probe: 180 : 450 + 0,6 = 0,4 + 0,6 = 1 ✓. Antwort: Es müssen 450 Hefte gedruckt werden.',
             'Bringe zuerst den Bruch allein auf eine Seite.', E),
        auswahl('c', 'Der Graph zeigt die Kosten pro Heft. Jemand meint: „Wenn wir nur genug Hefte drucken, kostet ein Heft irgendwann weniger als 50 Cent.“ Stimmt das?',
                'Nein: Die Kosten pro Heft kommen 0,60 € beliebig nahe, sinken aber nie darunter.',
                ['Ja: Bei mehr als 1 000 Heften kostet ein Heft weniger als 50 Cent.', 'Ja: Die Kosten pro Heft sinken immer weiter, bis fast auf 0 €.',
                 'Nein: Ab 450 Heften bleiben die Kosten pro Heft genau bei 1 €.'],
                'Gegeben: k(x) = 180/x + 0,6. Gesucht: Kann k(x) < 0,50 werden? Ansatz: Wie verhält sich 180/x für sehr große x? '
                'Rechnung: 180/x wird beliebig klein, bleibt aber positiv; also ist k(x) immer größer als 0,6. Die Gerade y = 0,6 ist die waagrechte Asymptote. '
                'Antwort: Nein, unter 0,60 € pro Heft kommt man nie.',
                'Was passiert mit 180/x, wenn x sehr groß wird? Was bleibt übrig?', A, grafik=graph),
        auswahl('d', 'Ihr verkauft jedes Heft für 1,50 € und lasst genau so viele Hefte drucken, wie vorbestellt sind. Für x Hefte nehmt ihr dann E(x) = 1,5x Euro ein, die Kosten sind K(x) = 180 + 0,6x Euro. '
                     'Für die nächste Ausgabe gibt es 160 Vorbestellungen. Was sollte die Redaktion tun?',
                'Mehr Vorbestellungen sammeln: Bei 160 Heften gibt es 36 € Verlust, erst ab 200 Heften keinen Verlust mehr.',
                ['Drucken: Bei 160 Heften bleibt ein kleiner Gewinn übrig.', 'Drucken: 1,50 € ist mehr als 0,60 €, also lohnt sich jedes verkaufte Heft sofort.',
                 'Mehr Vorbestellungen sammeln: Erst ab 450 Heften gibt es keinen Verlust.'],
                'Gegeben: E(x) = 1,5x, K(x) = 180 + 0,6x, 160 Vorbestellungen. Gesucht: Lohnt sich der Druck? Ansatz: Schnittpunkt E(x) = K(x) und Wert bei 160. '
                'Rechnung: 1,5x = 180 + 0,6x ⇒ 0,9x = 180 ⇒ x = 200. Bei 160: E = 240 €, K = 276 €, also 36 € Verlust. '
                'Antwort: Mit 160 Heften macht die Zeitung Verlust; es braucht mindestens 200 verkaufte Hefte (bei genau 200 weder Gewinn noch Verlust).',
                'Wo schneiden sich die Geraden von E und K? Liegt 160 davor oder dahinter?', S, pos=0),
    ],
})
