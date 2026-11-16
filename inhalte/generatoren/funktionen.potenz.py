#!/usr/bin/env python3
"""Thema funktionen.potenz – Potenzfunktionen (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(908)
H = HOCHZ


def nz(n):
    return R.choice([i for i in range(-n, n + 1) if i != 0])


def xn(n):
    if n < 0: return 'x⁻' + str(-n).translate(H)
    return 'x' if n == 1 else f'x{str(n).translate(H)}'


def fa(a, n):
    """a·xⁿ als Text"""
    af = '' if a == 1 else '−' if a == -1 else dz(a)
    return f'{af}{xn(n)}'


ETAPPEN = [
    {'lernziel': 'werte', 'titel': 'Funktionswerte von a · xⁿ',
     'regel': 'Bei f(x) = a · xⁿ zuerst ⟦potenzieren⟧, dann mit a multiplizieren. Negative x-Werte in ⟦Klammern⟧ einsetzen: Gerade Potenz → positiv, ungerade → negativ.',
     'schritte': ['f(x) = −2x³, gesucht f(−3): (−3)³ = −27.', 'f(−3) = −2 · (−27) = ⟦54⟧.'],
     'probe': 'Vorzeichen: − mal − ergibt + ✓',
     'fehler': 'Erst −2 · (−3) = 6 und dann 6³ = 216 zu rechnen ist falsch: ⟦Potenz vor Punkt⟧. Richtig: (−3)³ = −27, dann −2 · (−27) = 54.'},
    {'lernziel': 'symmetrie', 'titel': 'Symmetrie erkennen',
     'regel': 'n gerade: Graph ⟦achsensymmetrisch zur y-Achse⟧, f(−x) = f(x). n ungerade: ⟦punktsymmetrisch zum Ursprung⟧, f(−x) = −f(x).',
     'schritte': ['f(x) = 0,5x⁴: n = 4 gerade, also achsensymmetrisch.', 'Aus f(2) = 8 folgt ohne Rechnen ⟦f(−2) = 8⟧.'],
     'probe': '0,5 · (−2)⁴ = 0,5 · 16 = 8 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-2, 10], 'graphen': [{'art': 'potenz', 'a': 0.5, 'n': 4, 'name': 'f'}], 'punkte': [{'x': 2, 'y': 8, 'name': '(2 | 8)'}, {'x': -2, 'y': 8, 'name': '(−2 | 8)'}]},
     'fehler': '„y = x³ ist achsensymmetrisch zur y-Achse“ ist falsch: (−2)³ = −8, aber 2³ = 8. Bei ⟦ungeradem⟧ n ist der Graph punktsymmetrisch.'},
    {'lernziel': 'verlauf', 'titel': 'Verlauf und gemeinsame Punkte',
     'regel': 'y = xⁿ verläuft für ⟦n gerade⟧ von links oben nach rechts oben und durch (−1 | 1), (0 | 0), (1 | 1); für ⟦n ungerade⟧ von links unten nach rechts oben und durch (−1 | −1), (0 | 0), (1 | 1). ⟦a < 0⟧ spiegelt an der x-Achse.',
     'schritte': ['y = −x⁵: n = 5 ungerade, also y = x⁵ von links unten nach rechts oben.', 'a = −1 spiegelt an der x-Achse: ⟦von links oben nach rechts unten⟧.'],
     'probe': 'x = 2: −32 (unten), x = −2: 32 (oben) ✓',
     'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [-3, 3], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'x²'}, {'art': 'potenz', 'a': 1, 'n': 3, 'name': 'x³'}, {'art': 'potenz', 'a': 1, 'n': 4, 'name': 'x⁴'}], 'punkte': [{'x': -1, 'y': 1}, {'x': 1, 'y': 1}, {'x': -1, 'y': -1}, {'x': 0, 'y': 0}]},
     'fehler': '„Alle Potenzfunktionen y = xⁿ gehen durch (−1 | 1)“ ist falsch: Für ungerades n ist (−1)ⁿ = ⟦−1⟧.'},
    {'lernziel': 'parameter', 'titel': 'a oder n aus einem Punkt bestimmen',
     'regel': 'Liegt P(u | v) auf y = a · xⁿ, gilt ⟦v = a · uⁿ⟧. Ist n bekannt, teilst du durch uⁿ. Ist a = 1, suchst du die ⟦Hochzahl⟧ mit uⁿ = v.',
     'schritte': ['y = a · x³ geht durch P(2 | −24): −24 = a · 8.', 'a = −24 : 8 = ⟦−3⟧, also y = −3x³.'],
     'probe': '−3 · 2³ = −24 ✓',
     'fehler': '−24 = a · 2³ ⇒ a = −24 : 6 ist falsch: 2³ = 2 · 2 · 2 = ⟦8⟧, nicht 2 · 3.'},
    {'lernziel': 'negativ', 'titel': 'Potenzfunktionen mit x⁻ⁿ',
     'regel': '⟦y = x⁻ⁿ = 1/xⁿ⟧ ist für ⟦x ≠ 0⟧ definiert. Die Achsen sind Asymptoten. n gerade: achsensymmetrisch, n ungerade: punktsymmetrisch.',
     'schritte': ['f(x) = x⁻², gesucht f(4): f(4) = 1/4².', 'f(4) = 1/16 = ⟦0,0625⟧.'],
     'probe': '0,0625 · 16 = 1 ✓',
     'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-4, 4], 'graphen': [{'art': 'potenz', 'a': 1, 'n': -2, 'name': 'x⁻²'}, {'art': 'potenz', 'a': 1, 'n': -1, 'name': 'x⁻¹'}]},
     'fehler': 'f(4) = 4⁻² = −16 ist falsch: Ein negativer Exponent bedeutet ⟦Kehrwert⟧, nicht negatives Ergebnis: 4⁻² = 1/16.'},
    {'lernziel': 'wurzelfunktion', 'titel': 'Wurzelfunktionen und Umkehrung',
     'regel': 'y = x^(1/2) = √x und y = x^(1/3) = ∛x sind für ⟦x ≥ 0⟧ definiert. Sie sind die ⟦Umkehrfunktionen⟧ von y = x² bzw. y = x³ (für x ≥ 0): Aus y wird x zurückgerechnet. Im Bild: Der Graph von √x ist der Graph von x², ⟦gespiegelt an der Geraden y = x⟧ – x und y tauschen die Rollen.',
     'bild': {'typ': 'koordinaten', 'x': [0, 4], 'y': [0, 4], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'x²', 'bereich': [0, 2]}, {'art': 'wurzel', 'name': '√x'}], 'strecken': [[0, 0, 4, 4, 'gestrichelt']], 'punkte': [{'x': 2, 'y': 4, 'name': '(2 | 4)'}, {'x': 4, 'y': 2, 'name': '(4 | 2)'}]},
     'schritte': ['f(x) = x³ (x ≥ 0). Für welches x ist f(x) = 64?', 'Umkehrung: x = ∛64 = ⟦4⟧.'],
     'probe': '4³ = 64 ✓',
     'fehler': '„√x ist für alle x definiert“ ist falsch: √(−4) gibt es nicht. Die Wurzelfunktion hat die ⟦Definitionsmenge x ≥ 0⟧.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'werte': {
  'einstieg': 'Eine Rechenmaschine bekommt eine Zahl, nimmt sie dreimal mit sich selbst mal und verdoppelt das Ergebnis mit umgekehrtem Vorzeichen. Was kommt bei −3 heraus? Die Reihenfolge der Rechenschritte entscheidet. Eine solche Maschine der Form a · xⁿ heißt ⟦Potenzfunktion⟧.',
  'woerter': [['Potenzfunktion', 'eine Funktion der Form f(x) = a · xⁿ'],
              ['xⁿ', 'x n-mal mit sich selbst malgenommen'],
              ['a', 'die Zahl vor der Potenz, mit der am Ende malgenommen wird'],
              ['f(−3)', 'das Ergebnis der Maschine bei der Eingabe −3'],
              ['Potenz vor Punkt', 'erst hoch n rechnen, dann malnehmen']],
  'schritte': ['Die Maschine heißt f(x) = −2x³. Eingabe: x = −3.',
               'Zuerst die Potenz, mit Klammer: (−3)³ = (−3) · (−3) · (−3) = −27.',
               'Dann mit a = −2 malnehmen: −2 · (−27).',
               'Minus mal Minus ergibt Plus: f(−3) = ⟦54⟧.'],
  'regel': 'So berechnest du f(x) = a · xⁿ: Zuerst ⟦potenzieren⟧, dann mit a malnehmen. Negative Zahlen in ⟦Klammern⟧ einsetzen. Bei gerader Hochzahl wird das Ergebnis der Potenz positiv, bei ungerader bleibt es negativ.',
  'fehler': 'Erst −2 · (−3) = 6 und dann 6³ = 216 zu rechnen ist falsch: ⟦Potenz vor Punkt⟧. Die Maschine potenziert zuerst: (−3)³ = −27, dann −2 · (−27) = 54.'},
 'symmetrie': {
  'einstieg': 'Die Maschine f(x) = 0,5x⁴ liefert für 2 und für −2 dasselbe Ergebnis, denn vier Minuszeichen heben sich auf. Zeichnet man ihren Graphen, sind die linke und die rechte Hälfte Spiegelbilder – wie zwei Schmetterlingsflügel. Diese Eigenschaft heißt ⟦Symmetrie⟧.',
  'woerter': [['achsensymmetrisch zur y-Achse', 'die linke Hälfte ist das Spiegelbild der rechten; f(−x) = f(x)'],
              ['punktsymmetrisch zum Ursprung', 'nach einer halben Drehung um (0 | 0) liegt der Graph wieder auf sich; f(−x) = −f(x)'],
              ['Ursprung', 'der Punkt (0 | 0)'],
              ['f(−x)', 'das Ergebnis bei der Gegenzahl von x']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-2, 10], 'graphen': [{'art': 'potenz', 'a': 0.5, 'n': 4, 'name': 'f(x) = 0,5x⁴'}], 'punkte': [{'x': 2, 'y': 8, 'name': 'f(2) = 8'}, {'x': -2, 'y': 8, 'name': 'Spiegelpunkt f(−2) = 8'}]},
  'schritte': ['Die Funktion heißt f(x) = 0,5x⁴. Die Hochzahl 4 ist gerade.',
               'Bei gerader Hochzahl ist (−x)⁴ = x⁴. Also ist f(−x) = f(x): Der Graph ist achsensymmetrisch zur y-Achse.',
               'Bekannt ist f(2) = 0,5 · 16 = 8.',
               'Der Spiegelpunkt hat denselben y-Wert, also ohne Rechnen ⟦f(−2) = 8⟧.'],
  'regel': 'So erkennst du die ⟦Symmetrie⟧ von y = a · xⁿ: Ist ⟦n gerade⟧, ist der Graph ⟦achsensymmetrisch zur y-Achse⟧, f(−x) = f(x). Ist ⟦n ungerade⟧, ist er ⟦punktsymmetrisch zum Ursprung⟧, f(−x) = −f(x).',
  'fehler': '„y = x³ ist achsensymmetrisch zur y-Achse“ ist falsch: (−2)³ = −8, aber 2³ = 8 – die Spiegelpunkte haben verschiedene Höhen. Bei ⟦ungeradem⟧ n ist der Graph punktsymmetrisch.'},
 'verlauf': {
  'einstieg': 'Wer den Graphen von links nach rechts mit dem Finger nachfährt, sieht: Manche Potenzfunktionen kommen von oben und gehen nach oben, andere kommen von unten und gehen nach oben. Außerdem gehen alle durch bestimmte feste Punkte. Das nennt man den ⟦Verlauf⟧ des Graphen.',
  'woerter': [['Verlauf', 'woher der Graph links kommt und wohin er rechts geht'],
              ['gemeinsame Punkte', 'Punkte, durch die alle Graphen einer Gruppe gehen'],
              ['an der x-Achse spiegeln', 'oben und unten vertauschen; passiert bei a < 0']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [-3, 3], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'y = x²'}, {'art': 'potenz', 'a': 1, 'n': 3, 'name': 'y = x³'}, {'art': 'potenz', 'a': 1, 'n': 4, 'name': 'y = x⁴'}], 'punkte': [{'x': -1, 'y': 1, 'name': '(−1 | 1) bei geradem n'}, {'x': 1, 'y': 1, 'name': '(1 | 1) bei allen'}, {'x': -1, 'y': -1, 'name': '(−1 | −1) bei ungeradem n'}, {'x': 0, 'y': 0, 'name': '(0 | 0) bei allen'}]},
  'schritte': ['Die Funktion heißt y = −x⁵. Die Hochzahl 5 ist ungerade.',
               'Ohne das Minus verläuft y = x⁵ von links unten nach rechts oben.',
               'Das Minus vor x⁵ (a = −1) spiegelt den Graphen an der x-Achse: Oben und unten tauschen.',
               'Also verläuft y = −x⁵ ⟦von links oben nach rechts unten⟧.'],
  'regel': 'So beschreibst du den Verlauf von y = xⁿ: Bei ⟦n gerade⟧ von links oben nach rechts oben, durch (−1 | 1), (0 | 0), (1 | 1). Bei ⟦n ungerade⟧ von links unten nach rechts oben, durch (−1 | −1), (0 | 0), (1 | 1). Ist ⟦a < 0⟧, wird an der x-Achse gespiegelt.',
  'fehler': '„Alle Potenzfunktionen y = xⁿ gehen durch (−1 | 1)“ ist falsch: Für ungerades n bleibt ein Minus übrig, (−1)ⁿ = ⟦−1⟧. Im Bild geht y = x³ durch (−1 | −1).'},
 'parameter': {
  'einstieg': 'Eine Maschine der Form a · x³ ist bekannt bis auf die Zahl a. Man weiß nur: Gibt man 2 ein, kommt −24 heraus. Daraus lässt sich a zurückrechnen. Die einstellbare Zahl a heißt ⟦Parameter⟧.',
  'woerter': [['Parameter', 'eine Zahl in der Funktion, die man bestimmen oder einstellen kann'],
              ['P(2 | −24)', 'Eingabe 2, Ergebnis −24'],
              ['uⁿ', 'die Eingabe u hoch n']],
  'schritte': ['Die Funktion heißt y = a · x³, der Punkt P(2 | −24) liegt auf dem Graphen.',
               'Den Punkt einsetzen: −24 = a · 2³.',
               'Die Potenz ausrechnen: 2³ = 2 · 2 · 2 = 8, also −24 = a · 8.',
               'Durch 8 teilen: a = −24 : 8 = ⟦−3⟧. Die Funktion heißt y = −3x³.'],
  'regel': 'So bestimmst du einen Parameter: Liegt P(u | v) auf y = a · xⁿ, gilt ⟦v = a · uⁿ⟧. Ist n bekannt, teilst du v durch uⁿ und erhältst a. Ist a = 1, suchst du die ⟦Hochzahl⟧ n mit uⁿ = v.',
  'fehler': '−24 = a · 2³ ⇒ a = −24 : 6 ist falsch: 2³ = 2 · 2 · 2 = ⟦8⟧, nicht 2 · 3.'},
 'negativ': {
  'einstieg': 'Teilen sich 1 kg Gummibärchen auf immer mehr Kinder auf, bekommt jedes immer weniger, aber nie ganz null. Bei null Kindern gibt es gar keine Rechnung. Solche Maschinen sehen aus wie x hoch einer negativen Zahl. Sie heißen ⟦Potenzfunktionen mit negativem Exponenten⟧.',
  'woerter': [['x⁻ⁿ', '1 geteilt durch xⁿ, also der Kehrwert'],
              ['Kehrwert', '1 geteilt durch die Zahl, z. B. von 16 ist es 1/16'],
              ['x ≠ 0', 'x darf nicht 0 sein, denn durch 0 teilt man nicht'],
              ['Asymptote', 'eine Gerade, der sich der Graph immer weiter nähert, ohne sie zu erreichen']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-4, 4], 'graphen': [{'art': 'potenz', 'a': 1, 'n': -2, 'name': 'y = x⁻² (gerade)'}, {'art': 'potenz', 'a': 1, 'n': -1, 'name': 'y = x⁻¹ (ungerade)'}]},
  'schritte': ['Die Funktion heißt f(x) = x⁻². Gesucht ist f(4).',
               'Der negative Exponent bedeutet Kehrwert: 4⁻² = 1 / 4².',
               '4² = 16, also f(4) = 1/16.',
               'Als Dezimalzahl: f(4) = ⟦0,0625⟧.'],
  'regel': 'So gehst du mit ⟦y = x⁻ⁿ = 1/xⁿ⟧ um: Rechne den Kehrwert von xⁿ aus. Die Funktion gibt es nur für ⟦x ≠ 0⟧. Die beiden Achsen sind Asymptoten. Bei geradem n ist der Graph achsensymmetrisch, bei ungeradem punktsymmetrisch.',
  'fehler': 'f(4) = 4⁻² = −16 ist falsch: Ein negativer Exponent bedeutet ⟦Kehrwert⟧, nicht negatives Ergebnis: 4⁻² = 1/16 – wenig, aber mehr als null.'},
 'wurzelfunktion': {
  'einstieg': 'Eine Maschine rechnet hoch 3: Aus 4 macht sie 64. Jetzt liegt die 64 vor, und man will wissen, welche Zahl hineingesteckt wurde. Dafür braucht man eine Maschine, die rückwärts arbeitet. Sie heißt ⟦Umkehrfunktion⟧ – hier die Wurzelfunktion.',
  'woerter': [['Umkehrfunktion', 'die Funktion, die eine andere rückgängig macht'],
              ['√x = x^(1/2)', 'die Quadratwurzel als Funktion'],
              ['∛x = x^(1/3)', 'die dritte Wurzel als Funktion'],
              ['Definitionsmenge', 'alle x, die man einsetzen darf; hier x ≥ 0'],
              ['Gerade y = x', 'die schräge Linie, an der Funktion und Umkehrfunktion Spiegelbilder sind']],
  'bild': {'typ': 'koordinaten', 'x': [0, 4], 'y': [0, 4], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'y = x² (vorwärts)', 'bereich': [0, 2]}, {'art': 'wurzel', 'name': 'y = √x (rückwärts)'}], 'strecken': [[0, 0, 4, 4, 'gestrichelt']], 'punkte': [{'x': 2, 'y': 4, 'name': '2 → 4'}, {'x': 4, 'y': 2, 'name': '4 → 2'}]},
  'schritte': ['Die Funktion heißt f(x) = x³ für x ≥ 0. Gefragt: Für welches x ist f(x) = 64?',
               'Rückwärts gedacht: Gesucht ist die Zahl, die hoch 3 genau 64 ergibt.',
               'Das macht die Umkehrfunktion: x = ∛64.',
               'Wegen 4 · 4 · 4 = 64 ist x = ⟦4⟧.'],
  'regel': 'So nutzt du Wurzelfunktionen: y = √x und y = ∛x sind die ⟦Umkehrfunktionen⟧ von y = x² und y = x³ (für x ≥ 0) – sie rechnen von y zurück auf x. Sie gelten hier für ⟦x ≥ 0⟧. Im Bild ist der Graph der Umkehrfunktion das ⟦Spiegelbild an der Geraden y = x⟧.',
  'fehler': '„√x ist für alle x definiert“ ist falsch: √(−4) gibt es nicht, denn keine Zahl mal sich selbst ergibt −4. Die Wurzelfunktion hat die ⟦Definitionsmenge x ≥ 0⟧.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
_G = lambda n, name, a=1: {'art': 'potenz', 'a': a, 'n': n, 'name': name}
UMBAU = {
 'werte': {
  'einstieg': 'Eine Rechenmaschine nimmt eine Zahl hoch 3 und dann mal −2. Was kommt bei −3 heraus? So eine Maschine heißt ⟦Potenzfunktion⟧.',
  'woerter': [['Potenzfunktion', 'eine Funktion der Form f(x) = a · xⁿ'],
              ['f(−3)', 'das Ergebnis der Maschine bei der Eingabe −3'],
              ['Potenz vor Punkt', 'erst hoch rechnen, dann malnehmen']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-60, 60], 'schritt_y': 20, 'graphen': [_G(3, 'y = −2x³', -2)]},
  'schritte': [{'text': 'Die Maschine heißt f(x) = −2x³. Die Eingabe ist x = −3.'},
               {'text': 'Potenz vor Punkt: zuerst (−3)³ = −27.'},
               {'text': 'Dann mal −2: f(−3) = −2 · (−27) = ⟦54⟧.', 'bild': {'punkte': [{'x': -3, 'y': 54, 'name': '(−3 | 54)'}]}}],
  'fehler': 'Erst −2 · (−3) = 6 und dann 6³ = 216 ist falsch. Die Maschine potenziert zuerst, dann nimmt sie mal.',
  'regel': 'Erst ⟦potenzieren⟧, dann mit a malnehmen. Negative Zahlen setzt du in Klammern ein.'},
 'symmetrie': {
  'einstieg': 'Manche Graphen sehen aus wie Schmetterlingsflügel. Die linke Hälfte ist das Spiegelbild der rechten. Diese Eigenschaft heißt ⟦Symmetrie⟧.',
  'woerter': [['achsensymmetrisch', 'links und rechts der y-Achse spiegelgleich: f(−x) = f(x)'],
              ['punktsymmetrisch', 'nach einer halben Drehung um (0 | 0) gleich: f(−x) = −f(x)'],
              ['f(−x)', 'das Ergebnis bei der Gegenzahl von x']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-2, 10], 'graphen': [_G(4, 'y = 0,5x⁴', 0.5)]},
  'schritte': [{'text': 'f(x) = 0,5x⁴ hat den geraden Exponenten 4.'},
               {'text': '(−x)⁴ = x⁴, also f(−x) = f(x): achsensymmetrisch zur y-Achse.'},
               {'text': 'f(2) = 0,5 · 16 = 8, also ohne Rechnen ⟦f(−2) = 8⟧.',
                'bild': {'punkte': [{'x': 2, 'y': 8, 'name': 'f(2) = 8'}, {'x': -2, 'y': 8, 'name': 'f(−2) = 8'}]}},
               {'text': 'Bei ungeradem Exponenten wäre der Graph punktsymmetrisch zum Ursprung.'}],
  'fehler': 'y = x³ ist nicht achsensymmetrisch. 2³ = 8, aber (−2)³ = −8: Die Spiegelpunkte sind verschieden hoch.',
  'fehler_bild': {'y': [-10, 10], 'graphen': [_G(3, 'y = x³')],
                  'punkte': [{'x': 2, 'y': 8, 'name': '(2 | 8)'}, {'x': -2, 'y': -8, 'name': '(−2 | −8)'}]},
  'regel': 'Gerader Exponent: ⟦achsensymmetrisch⟧ zur y-Achse. Ungerader Exponent: punktsymmetrisch zum Ursprung.'},
 'verlauf': {
  'einstieg': 'Fahre einen Graphen mit dem Finger von links nach rechts nach. Kommst du von oben oder von unten? Wohin gehst du? Das beschreibt den ⟦Verlauf⟧.',
  'woerter': [['Verlauf', 'woher der Graph links kommt und wohin er rechts geht'],
              ['an der x-Achse spiegeln', 'oben und unten vertauschen']],
  'bild': {'typ': 'koordinaten', 'x': [-2, 2], 'y': [-3, 3], 'graphen': [_G(2, 'y = x²'), _G(3, 'y = x³')]},
  'schritte': [{'text': 'Gerader Exponent: von links oben nach rechts oben, wie y = x².'},
               {'text': 'Ungerader Exponent: von links unten nach rechts oben, wie y = x³.'},
               {'text': 'Das Minus in y = −x⁵ heißt: y = x⁵ an der x-Achse spiegeln.',
                'bild': {'graphen': [_G(5, 'y = x⁵'), _G(5, 'y = −x⁵', -1)]}},
               {'text': 'Also verläuft y = −x⁵ ⟦von links oben nach rechts unten⟧.'}],
  'fehler': 'Nicht alle y = xⁿ gehen durch (−1 | 1). Bei ungeradem n ist (−1)ⁿ = −1.',
  'fehler_bild': {'graphen': [_G(2, 'y = x²'), _G(3, 'y = x³')],
                  'punkte': [{'x': -1, 'y': 1, 'name': '(−1 | 1)'}, {'x': -1, 'y': -1, 'name': '(−1 | −1)'}]},
  'regel': 'Gerades n: beide Enden oben. Ungerades n: links unten, rechts oben. ⟦a < 0⟧ spiegelt an der x-Achse.'},
 'parameter': {
  'einstieg': 'Von einer Maschine a · x³ fehlt nur die Zahl a. Bekannt ist: Aus 2 wird −24. Daraus rechnest du den ⟦Parameter⟧ a zurück.',
  'woerter': [['Parameter', 'eine Zahl in der Funktion, die man bestimmen kann'],
              ['P(2 | −24)', 'Eingabe 2, Ergebnis −24']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-30, 30], 'schritt_y': 10, 'punkte': [{'x': 2, 'y': -24, 'name': 'P(2 | −24)'}]},
  'schritte': [{'text': 'P(2 | −24) einsetzen: −24 = a · 2³.'},
               {'text': '2³ = 2 · 2 · 2 = 8, also −24 = a · 8.'},
               {'text': 'Durch 8 teilen: ⟦a = −3⟧. Die Funktion heißt y = −3x³.', 'bild': {'graphen': [_G(3, 'y = −3x³', -3)]}}],
  'fehler': '2³ ist nicht 2 · 3 = 6. Hoch 3 heißt dreimal mit sich selbst malnehmen: 2³ = 8.',
  'regel': 'Punkt einsetzen: ⟦v = a · uⁿ⟧, dann nach a auflösen.'},
 'negativ': {
  'einstieg': 'Teilen sich immer mehr Kinder 1 kg Gummibärchen, bekommt jedes immer weniger, aber nie null. Solche Maschinen haben einen ⟦negativen Exponenten⟧.',
  'woerter': [['x⁻²', '1 geteilt durch x², also 1/x²'],
              ['Kehrwert', '1 geteilt durch die Zahl'],
              ['Asymptoten', 'Linien, denen der Graph immer näher kommt, ohne sie zu erreichen']],
  'bild': {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-1, 4], 'graphen': [_G(-2, 'y = x⁻²')]},
  'schritte': [{'text': 'x⁻² ist der Kehrwert von x². Also f(4) = 1 : 4².'},
               {'text': '4² = 16, also ⟦f(4) = 1/16 = 0,0625⟧.', 'bild': {'punkte': [{'x': 4, 'y': 0.0625, 'name': 'f(4)'}]}},
               {'text': 'Die Achsen sind Asymptoten: Der Graph kommt ihnen nahe, berührt sie aber nie.'}],
  'fehler': '4⁻² ist nicht −16. Ein Minus im Exponenten heißt Kehrwert, nicht negativ: 4⁻² = 1/16.',
  'regel': 'x⁻ⁿ ist der ⟦Kehrwert⟧ 1/xⁿ. Für x = 0 gibt es keinen Wert.'},
 'wurzelfunktion': {
  'einstieg': 'Eine Maschine rechnet hoch 3: Aus 2 wird 8. Liegt nur die 8 vor, rechnet eine zweite Maschine rückwärts. Sie heißt ⟦Umkehrfunktion⟧.',
  'woerter': [['Umkehrfunktion', 'die Funktion, die eine andere rückgängig macht'],
              ['∛x', 'die dritte Wurzel, gleich x^(1/3)'],
              ['x ≥ 0', 'nur Zahlen ohne Minus sind erlaubt']],
  'bild': {'typ': 'koordinaten', 'x': [0, 8], 'y': [0, 8], 'graphen': [_G(3, 'y = x³', 1) | {'bereich': [0, 2]}],
           'strecken': [[0, 0, 8, 8, 'gestrichelt']]},
  'schritte': [{'text': 'f(x) = x³ für x ≥ 0. Gesucht ist x mit x³ = 8.'},
               {'text': 'Rückwärts gedacht: Welche Zahl hoch 3 ergibt 8?'},
               {'text': 'Das macht die Umkehrfunktion ∛x: ∛8 = ⟦2⟧, denn 2³ = 8.',
                'bild': {'graphen': [_G(3, 'y = x³', 1) | {'bereich': [0, 2]}, _G(1 / 3, 'y = ∛x')],
                         'punkte': [{'x': 2, 'y': 8, 'name': '2 → 8'}, {'x': 8, 'y': 2, 'name': '8 → 2'}]}},
               {'text': 'Im Bild: ∛x ist x³, gespiegelt an der Linie y = x.'}],
  'fehler': '„√x gibt es für alle x“ ist falsch. √(−4) gibt es nicht, denn keine Zahl mal sich selbst ergibt −4.',
  'regel': 'Die ⟦Umkehrfunktion⟧ rechnet von y zurück auf x. √x und ∛x kehren x² und x³ für x ≥ 0 um.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def kos(graphen, x=(-3, 3), y=(-4, 4), **extra):
    g = {'typ': 'koordinaten', 'x': list(x), 'y': list(y), 'graphen': graphen}
    g.update(extra)
    return g


def g_werte(s):
    if s == 3 and R.random() < 0.35:
        if R.random() < 0.5:
            n = R.choice([4, 6])
            u = R.choice([2, 3]) if n == 4 else 2
            v = -(u ** n)
            return auswahl(f'f(x) = −{xn(n)}. Jemand rechnet f(−{u}) = (−(−{u})){str(n).translate(H)} = {dz(u ** n)}. Was stimmt?',
                           f'Falsch: f(−{u}) = −(−{u}){str(n).translate(H)} = {dz(v)}.',
                           ['Richtig.', f'Falsch: f(−{u}) = {dz(-u * n)}.', f'Falsch: f(−{u}) = {dz(u * n)}.'],
                           f'Erst potenzieren: (−{u}){str(n).translate(H)} = {dz(u ** n)}, dann das Minus davor: {dz(v)}.',
                           'Was wird zuerst gerechnet: die Potenz oder das Minus davor?')
        a, n, u = R.choice([-2, -3, -4]), 3, R.choice([-2, -3])
        v = a * u ** n
        return auswahl(f'Berechne f({dz(u)}) für f(x) = {fa(a, n)}.', dz(v),
                       [dz(-v), dz((a * u) ** n), dz(a * u * n)],
                       f'({dz(u)})³ = {dz(u ** 3)}; f({dz(u)}) = {dz(a)} · ({dz(u ** 3)}) = {dz(v)}.',
                       'Potenz vor Punkt: Erst (−x)³, dann mit a multiplizieren.')
    if s == 1:
        n, a, u = R.randint(2, 4), R.randint(1, 5), R.randint(1, 4)
    elif s == 2:
        n, a, u = R.randint(2, 5), nz(5), nz(3)
    else:
        if R.random() < 0.6:
            n = R.randint(2, 5)
            a = R.choice([2, 4, 8, -2, -4, 3])
            u = Fr(R.choice([-5, -1, 1, 3, 5]), 10) if n < 4 else Fr(R.choice([-1, 1]), 2)
            if R.random() < 0.4: u = Fr(R.choice([-1, 1]), 4)
        else:
            n, a, u = R.choice([3, 5]), R.choice([-1, -2, -3]), R.choice([-3, -2])
            if n == 5: u = -2
    v = a * Fr(u) ** n
    return zahl(f'Berechne f({dz(u)}) für f(x) = {fa(a, n)}.', f'{kl(u)}{str(n).translate(H)} = {dz(Fr(u) ** n)}; f({dz(u)}) = {dz(a)} · {kl(Fr(u) ** n)} = {dz(v)}.',
                'Erst potenzieren, dann mit a multiplizieren. Klammern um negative Zahlen!', v, f'({a}) * ({float(u) if not isinstance(u, int) else u}) ** {n}')


SYM = ['achsensymmetrisch zur y-Achse', 'punktsymmetrisch zum Ursprung', 'keine dieser Symmetrien']


def g_symmetrie(s):
    n = R.randint(2, 9)
    a = nz(5)
    if s == 1:
        r = SYM[0] if n % 2 == 0 else SYM[1]
        return auswahl(f'Welche Symmetrie hat der Graph von y = {fa(a, n)}?', r, SYM,
                       f'n = {n} ist {"gerade" if n % 2 == 0 else "ungerade"}, also {r}.', 'Ist der Exponent gerade oder ungerade?')
    u = R.randint(1, 3)
    v = a * u ** n
    if s == 2:
        if R.random() < 0.5:
            n = R.randint(2, 5)
            a = R.choice([Fr(1, 2), 1, -1, 2, Fr(-1, 2)])
            r = SYM[0] if n % 2 == 0 else SYM[1]
            return bild(auswahl('Welche Symmetrie hat der gezeigte Graph?', r, SYM,
                                f'Der Graph gehört zu y = {fa(a, n)}. ' + ('Die linke Hälfte ist das Spiegelbild der rechten an der y-Achse.' if n % 2 == 0 else
                                                                          'Dreht man den Graphen um 180° um den Ursprung, liegt er wieder auf sich selbst.'),
                                'Klappe das Bild an der y-Achse oder drehe es um den Ursprung.'),
                        kos([{'art': 'potenz', 'a': wert(Fr(a)), 'n': n}], y=(-5, 5)))
        g = v if n % 2 == 0 else -v
        return zahl(f'Für f(x) = a · {xn(n)} gilt f({u}) = {dz(v)}. Bestimme f(−{u}) ohne a zu berechnen.',
                    f'n = {n} {"gerade: f(−x) = f(x)" if n % 2 == 0 else "ungerade: f(−x) = −f(x)"}, also f(−{u}) = {dz(g)}.',
                    'Nutze die Symmetrie des Graphen.', g, f'({v}) * (-1) ** {n}')
    typ = R.random()
    if typ < 0.35:
        m = R.randint(1, 4) * 2 + 1
        return auswahl(f'Jemand behauptet: „y = {fa(a, m)} ist achsensymmetrisch zur y-Achse, weil {fa(a, m)} für x = 1 und x = −1 gleich groß ist.“ Was stimmt?',
                       f'Falsch: f(1) = {dz(a)}, f(−1) = {dz(-a)}; der Graph ist punktsymmetrisch.',
                       ['Richtig, das ist die Bedingung für Achsensymmetrie.', 'Falsch: Der Graph ist zu keiner Achse und keinem Punkt symmetrisch.',
                        'Richtig, alle Potenzfunktionen sind achsensymmetrisch.'],
                       f'f(−1) = {dz(a)} · (−1){str(m).translate(H)} = {dz(-a)} ≠ {dz(a)} = f(1). Ungerader Exponent: punktsymmetrisch zum Ursprung.',
                       'Rechne f(1) und f(−1) wirklich aus.')
    if typ < 0.7:
        n1, n2 = R.sample(range(1, 8), 2)
        if n1 < n2: n1, n2 = n2, n1
        term = f'{xn(n1)} {"+" if R.random() < 0.5 else "−"} {xn(n2)}'
        if n1 % 2 == 0 and n2 % 2 == 0: r = SYM[0]
        elif n1 % 2 == 1 and n2 % 2 == 1: r = SYM[1]
        else: r = SYM[2]
        sig = -1 if '−' in term else 1
        f1, fm1 = 1 + sig, (-1) ** n1 + sig * (-1) ** n2
        return auswahl(f'Welche Symmetrie hat der Graph von y = {term}?', r, SYM,
                       f'{"Beide Exponenten gerade" if r == SYM[0] else "Beide Exponenten ungerade" if r == SYM[1] else "Ein gerader und ein ungerader Exponent"}: {r}. Probe: f(1) = {dz(f1)}, f(−1) = {dz(fm1)}.',
                       'Untersuche jeden Summanden: Sind alle Exponenten gerade, alle ungerade oder gemischt?')
    n1, n2 = R.sample(range(2, 9), 2)
    if n1 % 2 == n2 % 2: return None
    g = n1 if n1 % 2 == 0 else n2
    return auswahl(f'Welcher Graph ist achsensymmetrisch zur y-Achse: y = {xn(n1)} + 1 oder y = {xn(n2)} + 1?', f'y = {xn(g)} + 1',
                   [f'y = {xn(n1 + n2 - g)} + 1', 'beide', 'keiner'],
                   f'Bei y = {xn(g)} + 1 ist der Exponent gerade; die Verschiebung um 1 nach oben ändert die Achsensymmetrie nicht.',
                   'Eine Verschiebung nach oben erhält die Achsensymmetrie zur y-Achse.')


VERL = {(0, 1): 'von links oben nach rechts oben', (0, -1): 'von links unten nach rechts unten',
        (1, 1): 'von links unten nach rechts oben', (1, -1): 'von links oben nach rechts unten'}


def g_verlauf(s):
    n = R.randint(2, 9)
    a = R.choice([1, -1]) if s == 1 else nz(6)
    if s == 1 or (s == 2 and R.random() < 0.5):
        r = VERL[(n % 2, 1 if a > 0 else -1)]
        return auswahl(f'Wie verläuft der Graph von y = {fa(a, n)}?', r, list(VERL.values()),
                       f'n = {n} {"gerade" if n % 2 == 0 else "ungerade"}, a {"> 0" if a > 0 else "< 0"}: {r}.',
                       'Was passiert für große positive und große negative x-Werte?')
    if s == 2 or R.random() < 0.25:
        while True:
            fs = [(R.choice([1, -1]), R.randint(2, 5)) for _ in range(3)]
            if len(set(fs)) == 3 and len({VERL[(n_ % 2, a_)] for a_, n_ in fs}) >= 2: break
        namen = ['g', 'h', 'k']
        k = R.randrange(3)
        a, n = fs[k]
        return bild(auswahl(f'Welcher Graph gehört zu y = {fa(a, n)}?', f'Graph {namen[k]}', [f'Graph {x}' for x in namen],
                            f'y = {fa(a, n)}: n = {n} {"gerade" if n % 2 == 0 else "ungerade"}, a {"> 0" if a > 0 else "< 0"}, also {VERL[(n % 2, a)]}; durch (1 | {dz(a)}) und (−1 | {dz(a * (-1) ** n)}).',
                            'Prüfe den Verlauf und die Punkte bei x = 1 und x = −1.'),
                    kos([{'art': 'potenz', 'a': fs[i][0], 'n': fs[i][1], 'name': namen[i]} for i in range(3)], x=(-2, 2), y=(-4, 4)))
    typ = R.random()
    if typ < 0.3:
        p = R.choice(['(−1 | 1)', '(−1 | −1)'])
        ger = p == '(−1 | 1)'
        r = 'alle mit geradem n' if ger else 'alle mit ungeradem n'
        m = R.randint(2, 9)
        return auswahl(f'Welche Graphen der Form y = xⁿ (n natürlich, n ≥ 2) gehen durch {p}? Denke z. B. an n = {m}.', r,
                       ['alle mit geradem n', 'alle mit ungeradem n', 'alle', 'keiner'],
                       f'(−1)ⁿ ist 1 für gerades n und −1 für ungerades n. Also gehen {r.replace("alle mit", "die Graphen mit")} durch {p}.',
                       'Berechne (−1)ⁿ für ein gerades und ein ungerades n.')
    n1, n2 = R.sample(range(2, 8), 2)
    lo, hi = min(n1, n2), max(n1, n2)
    if typ < 0.65:
        u = Fr(1, 2)
        if R.random() < 0.5:
            return auswahl(f'Welcher Graph liegt für 0 < x < 1 weiter oben: y = {xn(n1)} oder y = {xn(n2)}?', f'y = {xn(lo)}',
                           [f'y = {xn(hi)}', 'beide gleich', 'Das hängt von x ab.'],
                           f'Zwischen 0 und 1 wird die Zahl beim Potenzieren kleiner, z. B. 0,5{str(lo).translate(H)} = {dz(u ** lo)} > 0,5{str(hi).translate(H)} = {dz(u ** hi)}.',
                           'Setze probeweise x = 0,5 ein.')
        return auswahl(f'Für x = 0,5: Ist x{str(n1).translate(H)} oder x{str(n2).translate(H)} größer?', f'x{str(lo).translate(H)}',
                       [f'x{str(hi).translate(H)}', 'beide gleich groß', 'Das kann man nicht sagen.'],
                       f'0,5{str(lo).translate(H)} = {dz(u ** lo)} und 0,5{str(hi).translate(H)} = {dz(u ** hi)}: Mit jedem weiteren Faktor 0,5 wird die Zahl kleiner.',
                       'Rechne beide Werte aus.')
    return auswahl(f'Welcher Graph liegt für x > 1 weiter oben: y = {xn(n1)} oder y = {xn(n2)}?', f'y = {xn(hi)}',
                   [f'y = {xn(lo)}', 'beide gleich', 'Das hängt von x ab.'],
                   f'Für x > 1 wird die Zahl mit jedem weiteren Faktor größer, z. B. 2{str(hi).translate(H)} = {dz(2 ** hi)} > 2{str(lo).translate(H)} = {dz(2 ** lo)}.',
                   'Setze probeweise x = 2 ein.')


def g_parameter(s):
    if s == 1:
        n, a, u = R.randint(2, 3), nz(6), R.choice([1, 2, 3, -1, -2])
        v = a * u ** n
        return zahl(f'y = a · {xn(n)} geht durch P({dz(u)} | {dz(v)}). Bestimme a.', f'{dz(v)} = a · {kl(u)}{str(n).translate(H)} = {"" if u ** n == 1 else "−" if u ** n == -1 else dz(u ** n)}a ⇒ a = {dz(a)}.',
                    'Setze den Punkt ein und teile durch die Potenz.', a, f'({v}) / ({u}) ** {n}')
    if s == 2:
        u = R.choice([2, 3, 4, 5, Fr(1, 2)])
        n = R.randint(2, 6 if u in (2, Fr(1, 2)) else 4)
        v = Fr(u) ** n
        if R.random() < 0.5:
            a = nz(4)
            vv = a * v
            return zahl(f'y = a · {xn(n)} geht durch P({dz(u)} | {dz(vv)}). Bestimme a.', f'{dz(vv)} = a · {dz(v)} ⇒ a = {dz(a)}.',
                        'Berechne zuerst die Potenz, dann teilen.', a, f'({float(vv)}) / ({float(u)}) ** {n}')
        return zahl(f'y = xⁿ geht durch P({dz(u)} | {dz(v)}). Bestimme den Exponenten n.', f'{dz(u)}ⁿ = {dz(v)}; probieren: {dz(u)}{str(n).translate(H)} = {dz(v)}, also n = {n}.',
                    'Multipliziere die Basis so oft mit sich selbst, bis das Ergebnis erreicht ist.', n, f'{n}')
    n = R.randint(2, 4)
    a = nz(4)
    u1, u2 = R.sample([1, 2, 3, -1, -2], 2)
    if abs(u1) == abs(u2): return None
    v1, v2 = a * u1 ** n, a * u2 ** n
    return zahl(f'Der Graph von y = a · xⁿ geht durch P({dz(u1)} | {dz(v1)}) und Q({dz(u2)} | {dz(v2)}). Bestimme n.',
                f'Quotient: {dz(v2)} : {kl(v1)} = ({dz(u2)} : {kl(u1)})ⁿ = {br(Fr(v2, v1))} ⇒ n = {n} (dann a = {dz(a)}).',
                'Teile die beiden Gleichungen durcheinander, dann fällt a weg.', n, f'{n}')


def g_negativ(s):
    if s == 1:
        n, u = R.randint(1, 3), R.choice([2, 4, 5, 10])
        v = Fr(1, u ** n)
        return zahl(f'Berechne f({u}) für f(x) = {xn(-n)}. Gib das Ergebnis als Dezimalzahl an.', f'f({u}) = 1/{u}{str(n).translate(H)} = 1/{dz(u ** n)} = {dz(v)}.',
                    'Negativer Exponent: Kehrwert der Potenz.', v, f'1 / {u} ** {n}')
    typ = R.random()
    if s == 2:
        if typ < 0.4:
            n, u = R.randint(1, 4), Fr(1, R.choice([2, 3, 4]))
            v = 1 / u ** n
            return zahl(f'Berechne f({br(u)}) für f(x) = {xn(-n)}.', f'f({br(u)}) = 1/({br(u)}){str(n).translate(H)} = {dz(v)}.',
                        'Der Kehrwert eines Bruchs: Zähler und Nenner tauschen.', v, f'1 / (1 / {u.denominator}) ** {n}')
        n = R.randint(1, 6)
        a = R.choice([1, 1, -1, 2, 3, -2, Fr(1, 2)])
        r = SYM[0] if n % 2 == 0 else SYM[1]
        return auswahl(f'Welche Symmetrie hat der Graph von y = {fa(a, -n)}?', r, SYM,
                       f'{xn(-n)} = 1/{xn(n)}; n = {n} {"gerade" if n % 2 == 0 else "ungerade"}: {r}.' + (f' Der Faktor {dz(a)} ändert daran nichts.' if a != 1 else ''),
                       'Wie bei xⁿ entscheidet, ob n gerade ist.')
    if typ < 0.25:
        n = R.randint(1, 5)
        return auswahl(f'Für welche x ist f(x) = {xn(-n)} definiert?', 'für alle x ≠ 0', ['für alle x', 'für alle x > 0', 'für alle x ≥ 0'],
                       f'{xn(-n)} = 1/x{str(n).translate(H)}; durch 0 darf man nicht teilen, also x ≠ 0.', 'Schreibe die Potenz als Bruch.')
    if typ < 0.5:
        n = R.randint(2, 4)
        u = R.choice([2, 3, 4, 5])
        return auswahl(f'Jemand rechnet {u}{"⁻" + str(n).translate(H)} = −{dz(u ** n)}. Was stimmt?', f'Falsch: {u}{"⁻" + str(n).translate(H)} = 1/{dz(u ** n)}',
                       ['Richtig', f'Falsch: {u}{"⁻" + str(n).translate(H)} = −1/{dz(u ** n)}', f'Falsch: {u}{"⁻" + str(n).translate(H)} = −{dz(u * n)}'],
                       f'Ein negativer Exponent bedeutet Kehrwert: {u}{"⁻" + str(n).translate(H)} = 1/{u}{str(n).translate(H)} = 1/{dz(u ** n)} > 0.',
                       'Was bedeutet ein negatives Vorzeichen im Exponenten?')
    if typ < 0.75:
        n = R.randint(1, 4)
        seite = R.choice(['x > 0', 'x < 0']) if n % 2 else 'x > 0'
        if n % 2 and seite == 'x < 0':
            r, f2 = 'y wird beliebig klein (stark negativ).', 'y wird beliebig groß.'
        else:
            r, f2 = 'y wird beliebig groß.', 'y wird beliebig klein (stark negativ).'
        return bild(auswahl(f'Was passiert mit y = {xn(-n)} für x nahe 0, {seite}?', r, [f2, 'y kommt 0 beliebig nahe.', 'y wird genau 1.'],
                            f'Setze z. B. x = {"0,01" if seite == "x > 0" else "−0,01"} ein: 1/({"0,01" if seite == "x > 0" else "−0,01"}){str(n).translate(H)} ist betragsmäßig sehr groß'
                            + (', und negativ.' if r.startswith('y wird beliebig klein') else ', und positiv.') + ' Die y-Achse ist Asymptote.',
                            'Setze eine Zahl sehr nahe bei 0 ein.'),
                    kos([{'art': 'potenz', 'a': 1, 'n': -n}], x=(-4, 4), y=(-4, 4)) if R.random() < 0.5 else None)
    n = R.randint(1, 4)
    return auswahl(f'Was passiert mit y = {xn(-n)} für sehr große x?', 'y kommt der x-Achse beliebig nahe (bleibt aber positiv).',
                   ['y wird beliebig groß.', 'y wird negativ.', 'y wird genau 0.'],
                   f'1/x{str(n).translate(H)} wird für große x sehr klein, aber nie 0: Die x-Achse ist Asymptote.',
                   'Setze z. B. x = 100 ein.')


def g_wurzelfunktion(s):
    if s == 1:
        n = R.choice([2, 3])
        r = R.randint(2, 12 if n == 2 else 6)
        return zahl(f'f(x) = x{str(n).translate(H)} für x ≥ 0. Für welches x ist f(x) = {dz(r ** n)}?',
                    f'x{str(n).translate(H)} = {dz(r ** n)} ⇒ x = {"√" if n == 2 else "∛"}{dz(r ** n)} = {r} (x ≥ 0).',
                    'Rechne mit der Umkehrung (Wurzel) zurück.', r, f'{r ** n} / {r} ** {n - 1}')
    typ = R.random()
    if s == 2:
        if typ < 0.5:
            n = R.choice([2, 3])
            r = R.randint(2, 15 if n == 2 else 6)
            return zahl(f'Berechne f({dz(r ** n)}) für f(x) = x^(1/{n}).', f'x^(1/{n}) = {"√x" if n == 2 else "∛x"}; f({dz(r ** n)}) = {r}.',
                        'Hoch 1/n bedeutet n-te Wurzel.', r, f'{r ** n} / {r} ** {n - 1}')
        a, n = R.randint(2, 5), R.choice([2, 3])
        r = R.randint(2, 6)
        v = a * r ** n
        return zahl(f'f(x) = {a}x{str(n).translate(H)} für x ≥ 0. Für welches x ist f(x) = {dz(v)}?',
                    f'{a}x{str(n).translate(H)} = {dz(v)} ⇒ x{str(n).translate(H)} = {dz(r ** n)} ⇒ x = {r}.',
                    'Erst durch a teilen, dann die Wurzel ziehen.', r, f'({v} / {a}) / {r} ** {n - 1}')
    if typ < 0.15:
        return bild(auswahl('Im Bild siehst du y = x² (für x ≥ 0), y = √x und die Gerade y = x. Wie liegen die beiden Kurven zueinander?',
                            'Spiegelbildlich zur Geraden y = x.', ['Spiegelbildlich zur x-Achse.', 'Spiegelbildlich zur y-Achse.', 'Sie sind parallel verschoben.'],
                            'Bei der Umkehrfunktion tauschen x und y die Rollen. Das ist eine Spiegelung an y = x: (2 | 4) wird zu (4 | 2).',
                            'Vergleiche einen Punkt auf x² mit dem passenden Punkt auf √x.'),
                    {'typ': 'koordinaten', 'x': [0, 5], 'y': [0, 5], 'graphen': [{'art': 'potenz', 'a': 1, 'n': 2, 'name': 'x²', 'bereich': [0, 2.2]}, {'art': 'wurzel', 'name': '√x'}],
                     'strecken': [[0, 0, 5, 5, 'gestrichelt']]})
    if typ < 0.3:
        u = R.randint(2, 5)
        return auswahl(f'Der Punkt ({u} | {dz(u ** 3)}) liegt auf y = x³. Welcher Punkt liegt auf y = ∛x?', f'({dz(u ** 3)} | {u})',
                       [f'({u} | {dz(u ** 3)})', f'({u} | {dz(Fr(u ** 3, 3)) if u ** 3 % 3 == 0 else dz(-u)})', f'({dz(u ** 3)} | {dz(-u)})'],
                       f'Umkehrfunktion: x und y tauschen. ∛{dz(u ** 3)} = {u}, also ({dz(u ** 3)} | {u}).',
                       'Was passiert mit x- und y-Koordinate bei der Umkehrung?')
    if typ < 0.5:
        return auswahl('Welche Funktion ist die Umkehrfunktion von f(x) = x² für x ≥ 0?', 'g(x) = √x',
                       ['g(x) = x^(−2)', 'g(x) = x / 2', 'g(x) = −x²'],
                       'Die Umkehrfunktion macht das Quadrieren rückgängig: Aus y = x² folgt x = √y. Also g(x) = √x = x^(1/2).',
                       'Welche Rechnung macht das Quadrieren rückgängig?')
    if typ < 0.7:
        n = R.choice([2, 4])
        return auswahl(f'Für welche x ist f(x) = x^(1/{n}) definiert?', 'für alle x ≥ 0', ['für alle x', 'für alle x ≠ 0', 'für alle x > 0'],
                       f'x^(1/{n}) ist die {n}. Wurzel; sie ist nur für x ≥ 0 erklärt.', 'Aus welchen Zahlen kann man eine Wurzel ziehen?')
    u, v = R.randint(2, 9), None
    v = u * u
    return auswahl(f'Der Punkt ({u} | {v}) liegt auf dem Graphen von y = x². Welcher Punkt liegt dann auf dem Graphen von y = √x?',
                   f'({v} | {u})', [f'({u} | {v})', f'({dz(-u)} | {v})', f'({v} | {dz(-u)})'],
                   f'Bei der Umkehrfunktion werden x und y vertauscht: √{v} = {u}, also ({v} | {u}).',
                   'Was passiert mit x- und y-Koordinate bei der Umkehrung?')


GEN = {'werte': g_werte, 'symmetrie': g_symmetrie, 'verlauf': g_verlauf, 'parameter': g_parameter, 'negativ': g_negativ,
       'wurzelfunktion': g_wurzelfunktion}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9908, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; 2009: Graph einer
# Potenzfunktion über Symmetrie ergänzen, Schnittpunkte zweier Potenzgraphen durch Gleichsetzen; 2023: Wertemenge
# einer Wurzelfunktion; 2024: f(x) = 3/x mit Rechteck konstanter Fläche und Punkt auf y = x; 2025: Funktionswert im
# Sachzusammenhang deuten). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402


def schwer():
    P, Kn, O = 'pruefung', 'knobel', ''
    graph = {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-9, 2], 'graphen': [{'art': 'potenz', 'a': -0.5, 'n': 4}], 'punkte': [{'x': 2, 'y': -8, 'name': 'P'}]}
    return [
        # werte
        ('werte', 3, P, zahl('Berechne ohne Taschenrechner f(0,5) für f(x) = 16x⁴.', '0,5⁴ = 0,0625 (= 1/16). f(0,5) = 16 · 1/16 = 1.',
                             'Schreibe 0,5 als 1/2: (1/2)⁴ = 1/16.', 1, '16 * 0.5 ** 4')),
        ('werte', 3, P, zahl('Die Leistung eines Windrads wächst mit der dritten Potenz der Windgeschwindigkeit: P(v) = 0,5 · v³ (P in kW, v in m/s). Welche Leistung liefert es bei 6 m/s?',
                             'P(6) = 0,5 · 6³ = 0,5 · 216 = 108 kW.', 'Erst 6³, dann mal 0,5.', 108, '0.5 * 6 ** 3', einheit='kW')),
        ('werte', 3, Kn, zahl('Für f(x) = x⁵ gilt f(2) = 32. Berechne f(−2) + f(0) + f(2), ohne eine Potenz neu auszurechnen.',
                              'Ungerader Exponent: f(−2) = −f(2) = −32. f(0) = 0. Summe: −32 + 0 + 32 = 0.', 'Was passiert bei ungeradem Exponenten mit dem Vorzeichen?', 0,
                              '-32 + 0 + 32')),
        ('werte', 3, O, zahl('Für f(x) = 2x³: Um welchen Faktor wird der Funktionswert größer, wenn man x verdreifacht?', 'f(3x) = 2 · (3x)³ = 27 · 2x³ = 27 · f(x). Faktor 27.',
                             'Probiere mit x = 1 und x = 3 und vergleiche.', 27, '3 ** 3')),
        ('werte', 2, O, zahl('Berechne f(−1) für f(x) = 4x⁶.', '(−1)⁶ = 1, also f(−1) = 4.', 'Gerader Exponent: das Minus verschwindet.', 4, '4 * (-1) ** 6')),
        ('werte', 2, O, zahl('Berechne f(10) für f(x) = 0,003x⁴.', '10⁴ = 10 000, mal 0,003 ergibt 30.', 'Erst potenzieren, dann malnehmen.', 30, '0.003 * 10 ** 4')),
        # symmetrie
        ('symmetrie', 3, P, zahl('Der Graph von y = a · x⁵ geht durch (2 | 8). Welchen y-Wert hat er bei x = −2?',
                                 'Ungerader Exponent: Der Graph ist punktsymmetrisch zum Ursprung. Zu (2 | 8) gehört (−2 | −8).', 'Spiegle den Punkt am Ursprung.', -8, '-1 * 8')),
        ('symmetrie', 3, P, zahl('Der Graph von f(x) = a · x⁴ geht durch (−3 | 162). Welchen Wert hat f(3)?',
                                 'Gerader Exponent: achsensymmetrisch zur y-Achse, also f(3) = f(−3) = 162. (Es ist a = 2.)', 'Spiegle an der y-Achse – a musst du dafür nicht kennen.',
                                 162, '2 * 3 ** 4')),
        ('symmetrie', 3, Kn, auswahl('Der Graph einer Funktion f ist achsensymmetrisch zur y-Achse und zugleich punktsymmetrisch zum Ursprung. Was folgt daraus?',
                                     'f(x) = 0 für alle x', ['f(x) = x²', 'f(x) = x³', 'So eine Funktion kann es nicht geben.'],
                                     'Achsensymmetrie: f(−x) = f(x). Punktsymmetrie: f(−x) = −f(x). Beides zusammen: f(x) = −f(x), also f(x) = 0. Nur die x-Achse selbst hat beide Symmetrien.',
                                     'Schreibe beide Bedingungen für f(−x) auf und setze sie gleich.')),
        ('symmetrie', 3, O, auswahl('Welche Symmetrie hat der Graph von y = x⁴ − 3x² + 1?', 'achsensymmetrisch zur y-Achse', ['punktsymmetrisch zum Ursprung', 'keine dieser Symmetrien', 'beide Symmetrien'],
                                    'Alle Exponenten sind gerade (4, 2 und 0 beim Zahlglied), darum ändert −x nichts.', 'Prüfe die Exponenten aller Summanden; das Zahlglied zählt als x⁰.')),
        ('symmetrie', 2, O, auswahl('Welche Symmetrie hat der Graph von y = −2x³?', 'punktsymmetrisch zum Ursprung', ['achsensymmetrisch zur y-Achse', 'keine Symmetrie'],
                                    'Ungerader Exponent 3: punktsymmetrisch zum Ursprung; das Minus ändert daran nichts.', 'Gerader oder ungerader Exponent?')),
        ('symmetrie', 2, O, auswahl('Der Graph von f(x) = x⁶ geht durch (2 | 64). Welcher Punkt liegt dann auch auf dem Graphen?', '(−2 | 64)', ['(−2 | −64)', '(2 | −64)', '(64 | 2)'],
                                    'Gerader Exponent: achsensymmetrisch zur y-Achse, also auch (−2 | 64).', 'Spiegle an der y-Achse.')),
        # verlauf
        ('verlauf', 3, P, luecken('Die Graphen von y = x³ und y = 4x schneiden sich in drei Punkten. Gib ihre x-Koordinaten an.', 'x₁ = □; x₂ = □; x₃ = □', 'der Größe nach', [-2, 0, 2],
                                  'Gleichsetzen: x³ = 4x ⇔ x(x² − 4) = 0 ⇔ x = 0 oder x = ±2. Schnittpunkte (−2 | −8), (0 | 0), (2 | 8).',
                                  'Setze gleich, bring alles auf eine Seite und klammere x aus.', ['-2', '0', '2'])),
        ('verlauf', 3, P, bild(auswahl('Welcher Term gehört zum gezeichneten Graphen? (P liegt auf dem Graphen.)', 'y = −0,5x⁴', ['y = 0,5x⁴', 'y = −0,5x³', 'y = −2x⁴'],
                                       'Beide Enden zeigen nach unten: gerader Exponent, a < 0. Punktprobe P(2 | −8): −0,5 · 16 = −8 ✓, aber −2 · 16 = −32.',
                                       'Verlauf der Enden → Exponent und Vorzeichen; dann die Punktprobe mit P.'), graph)),
        ('verlauf', 3, Kn, zahl('Wie viele gemeinsame Punkte haben die Graphen von y = x³ und y = x²?',
                                'x³ = x² ⇔ x²(x − 1) = 0 ⇔ x = 0 oder x = 1. Zwei gemeinsame Punkte: (0 | 0) und (1 | 1). (−1 | ·) passt nicht: (−1)³ = −1, aber (−1)² = 1.',
                                'Nicht durch x² teilen – ausklammern. Prüfe auch x = −1.', 2, '1 + 1')),
        ('verlauf', 3, O, auswahl('Welcher Graph verläuft von links oben nach rechts unten?', 'y = −x⁵', ['y = −x⁴', 'y = x⁵', 'y = x⁴'],
                                  'Ungerader Exponent: die Enden zeigen in verschiedene Richtungen; a < 0 spiegelt y = x⁵ an der x-Achse: links oben, rechts unten.',
                                  'Erst gerade/ungerade, dann das Vorzeichen von a.')),
        ('verlauf', 2, O, auswahl('Durch welchen Punkt gehen alle Graphen y = xⁿ (n natürlich, n ≥ 1)?', '(1 | 1)', ['(−1 | 1)', '(1 | 0)', '(0 | 1)'],
                                  '1ⁿ = 1 für jedes n. (−1 | 1) gilt nur für gerades n.', 'Setze x = 1 ein.')),
        ('verlauf', 2, O, auswahl('Wie verläuft der Graph von y = −x⁶?', 'Beide Enden zeigen nach unten.', ['links unten, rechts oben', 'Beide Enden zeigen nach oben.', 'links oben, rechts unten'],
                                  'Gerader Exponent: beide Enden gleich; das Minus spiegelt nach unten.', 'Gerader Exponent und a < 0.')),
        # parameter
        ('parameter', 3, P, zahl('Der Graph von y = a · x³ geht durch P(−2 | 4). Bestimme a.', '4 = a · (−2)³ = −8a ⇒ a = −0,5.', 'Achte auf (−2)³ = −8.', -0.5, '4 / (-8)')),
        ('parameter', 3, P, zahl('Der Graph von y = a · x⁴ geht durch (1 | 3). Welchen Funktionswert hat er bei x = 2?', 'Aus (1 | 3): a = 3. Dann f(2) = 3 · 2⁴ = 48.',
                                 'Bestimme zuerst a mit dem Punkt bei x = 1.', 48, '3 * 2 ** 4')),
        ('parameter', 3, Kn, zahl('Der Graph von y = xⁿ geht durch (3 | 243). Bestimme n.', '3, 9, 27, 81, 243: Das ist 3⁵. Also n = 5.', 'Multipliziere 3 so oft mit sich selbst, bis 243 herauskommt.',
                                  5, '2 + 3')),
        ('parameter', 3, O, zahl('Der Graph von y = a · xⁿ geht durch (1 | 2) und (2 | 64). Bestimme n.', 'Aus (1 | 2): a = 2. Dann 2 · 2ⁿ = 64 ⇒ 2ⁿ = 32 ⇒ n = 5.',
                                 'Der Punkt mit x = 1 verrät a sofort.', 5, '10 // 2')),
        ('parameter', 2, O, zahl('Der Graph von y = a · x² geht durch (3 | 18). Bestimme a.', '18 = a · 9 ⇒ a = 2.', 'Punkt einsetzen.', 2, '18 / 9')),
        ('parameter', 2, O, zahl('Der Graph von y = a · x⁵ geht durch (1 | −4). Bestimme a.', '1⁵ = 1, also a = −4.', 'Setze x = 1 ein.', -4, '-4 / 1')),
        # negativ
        ('negativ', 3, P, zahl('Gegeben ist f(x) = 4 · x⁻¹ für x > 0. Der Punkt Q(a | f(a)), der Ursprung und die Achsen begrenzen ein Rechteck. Wie groß ist sein Flächeninhalt für a = 5?',
                               'Breite a = 5, Höhe f(5) = 4/5. Fläche 5 · 4/5 = 4. (Für jedes a gilt a · 4/a = 4.)', 'Breite ist a, Höhe ist f(a).', 4, '5 * 4 / 5')),
        ('negativ', 3, P, zahl('Für welches a > 0 liegt der Punkt Q(a | 9 · a⁻¹) auf der Geraden y = x?', '9/a = a ⇔ a² = 9 ⇔ a = 3 (a > 0).', 'x- und y-Koordinate müssen gleich sein.', 3, '9 / 3')),
        ('negativ', 3, Kn, auswahl('Für welche x liegt der Graph von y = x⁻⁴ über dem Graphen von y = x⁻²?', 'für 0 < |x| < 1', ['für |x| > 1', 'für alle x ≠ 0', 'für kein x'],
                                   'Beispiel x = 0,5: 0,5⁻⁴ = 16 > 0,5⁻² = 4. Beispiel x = 2: 2⁻⁴ = 1/16 < 2⁻² = 1/4. Bei x = ±1 sind beide 1.',
                                   'Probiere x = 0,5 und x = 2. Denke an die Kehrwerte.')),
        ('negativ', 3, O, zahl('Berechne f(0,5) für f(x) = 2 · x⁻³.', '0,5⁻³ = 1/0,125 = 8, also f(0,5) = 2 · 8 = 16.', 'x⁻³ ist 1 : x³.', 16, '2 / 0.5 ** 3')),
        ('negativ', 2, O, luecken('Berechne f(3) für f(x) = x⁻².', '□/□', 'Zähler und Nenner eintragen', [1, 9], '3⁻² = 1/3² = 1/9.', 'Minus im Exponenten heißt Kehrwert.', ['1', '3 ** 2'])),
        ('negativ', 2, O, auswahl('Welcher Punkt liegt auf dem Graphen von y = x⁻¹?', '(4 | 0,25)', ['(4 | −4)', '(−4 | 0,25)', '(0 | 0)'],
                                  '4⁻¹ = 1/4 = 0,25. Bei x = −4 wäre y = −0,25; x = 0 ist nicht erlaubt.', 'Rechne 1 : x.')),
        # wurzelfunktion
        ('wurzelfunktion', 3, P, auswahl('Welche Wertemenge hat die Funktion f mit f(x) = √x + 2 (x ≥ 0)?', 'W = {y | y ≥ 2}', ['W = {y | y ≥ 0}', 'W = ℝ', 'W = {y | y ≤ 2}'],
                                         '√x nimmt alle Werte ≥ 0 an, plus 2 ergibt alle Werte ≥ 2. Der kleinste Wert f(0) = 2.', 'Was ist der kleinste Wert von √x? Was passiert durch „+ 2“?')),
        ('wurzelfunktion', 3, P, zahl('Für die Schwingungsdauer eines Pendels gilt näherungsweise T = 2 · √l (T in s, l in m). Wie lang ist ein Pendel mit T = 3 s?',
                                      '3 = 2 · √l ⇒ √l = 1,5 ⇒ l = 1,5² = 2,25 m.', 'Erst durch 2 teilen, dann quadrieren.', 2.25, '(3 / 2) ** 2', einheit='m')),
        ('wurzelfunktion', 3, Kn, auswahl('Wie oft schneiden sich die Graphen von y = √x und y = x?', 'zweimal', ['einmal', 'gar nicht', 'unendlich oft'],
                                          '√x = x ⇔ x = x² ⇔ x(x − 1) = 0: x = 0 und x = 1. Dazwischen liegt √x über x (z. B. √0,25 = 0,5).',
                                          'Quadriere beide Seiten und löse. Prüfe die Lösungen.')),
        ('wurzelfunktion', 3, O, zahl('Der Punkt (a | 5) liegt auf dem Graphen von y = √x. Bestimme a.', '√a = 5 ⇒ a = 25.', 'Umkehren: Quadrieren.', 25, '5 ** 2')),
        ('wurzelfunktion', 2, O, zahl('Berechne f(64) für f(x) = ∛x.', '4³ = 64, also f(64) = 4.', 'Welche Zahl hoch 3 ergibt 64?', 4, '64 / 16')),
        ('wurzelfunktion', 2, O, auswahl('Welche Funktion ist die Umkehrfunktion von f(x) = x³ (x ≥ 0)?', 'g(x) = ∛x', ['g(x) = x⁻³', 'g(x) = x : 3', 'g(x) = 3x'],
                                         'Die dritte Wurzel macht das Hoch-3 rückgängig: ∛(x³) = x.', 'Welche Rechnung macht „hoch 3“ rückgängig?')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('funktionen.potenz', 13_9_8)
# a) eher Stufe 2; c) Beinahe-Dublette (dieselbe Frage einmal als Zahl-, einmal als Auswahl-Aufgabe)
BF.stufe('werte', 'Berechne f(−2) für f(x) = −2x³.', 2, enthaelt='"y": "zahl"')
BF.ersetze('werte', 'Berechne f(−2) für f(x) = −2x³.', BF.A(
    'Welches Vorzeichen hat f(−5) für f(x) = −2x³? Entscheide, ohne den Wert auszurechnen.', 'positiv', ['negativ', 'null'],
    '(−5)³ ist negativ (ungerader Exponent). Mal −2 wird daraus eine positive Zahl: f(−5) = −2 · (−125) = 250 > 0.',
    'Ungerader Exponent: Das Vorzeichen bleibt. Was macht dann der Faktor −2?'), enthaelt='"y": "auswahl"', s=2)
# a) vier fast gleiche Varianten auf Stufe 3 → zwei davon Stufe 2
BF.stufe('verlauf', 'Welcher Graph liegt für 0 < x < 1 weiter oben: y = x² oder y = x⁷?', 2)
BF.stufe('verlauf', 'Welcher Graph liegt für x > 1 weiter oben: y = x⁷ oder y = x²?', 2)
# a) Standard → Stufe 2
BF.stufe('negativ', 'Für welche x ist f(x) = x⁻³ definiert?', 2)

# ---- BEFUNDE ENDE ----

if __name__ == '__main__':
    d = bauen('funktionen.potenz',
          'Potenzfunktionen y = a · xⁿ untersuchen: Werte, Symmetrie, Verlauf, Parameter; Erweiterung auf negative und rationale Exponenten.',
          ['n gerade: achsensymmetrisch, durch (−1 | 1) und (1 | 1). n ungerade: punktsymmetrisch, durch (−1 | −1) und (1 | 1).',
           'a < 0 spiegelt an der x-Achse, |a| streckt oder staucht.', 'x⁻ⁿ = 1/xⁿ, nur für x ≠ 0.', 'x^(1/2) = √x und x^(1/3) = ∛x sind für x ≥ 0 die Umkehrungen von x² und x³.'],
          [('Natürliche Exponenten', ['werte', 'symmetrie', 'verlauf']), ('Parameter', ['parameter']),
           ('Erweiterung des Potenzbegriffs', ['negativ', 'wurzelfunktion'])],
          ETAPPEN, GEN,
          meiden={'werte': ['f(−3) für f(x) = −2x³'], 'symmetrie': ['f(2) = 8'], 'verlauf': ['y = −x⁵?'], 'parameter': ['P(2 | −24)'],
                  'negativ': ['f(4) für f(x) = x^(−2)'], 'wurzelfunktion': ['f(x) = 64?']},
          offen=['Negative Exponenten werden jetzt hochgestellt geschrieben (x⁻², wie in der Regel); bitte in der App prüfen, ob „⁻“ gut lesbar ist.'])
    anhaengen(d, 9908, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
