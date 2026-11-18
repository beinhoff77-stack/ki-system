#!/usr/bin/env python3
"""Thema zahlen.rationale_exponenten – Rationale Exponenten und n-te Wurzel (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(903)
HOCH = str.maketrans('0123456789−-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻')


def wz(n, a):
    """n-te Wurzel als Text, z. B. ⁴√81"""
    if n == 2: return f'√{a}'
    return f'{str(n).translate(HOCH)}√{a}'


def ex(q):
    """Exponent als Text: x^(2/3), x^3"""
    q = Fr(q)
    return str(q.numerator).replace('-', '−') if q.denominator == 1 else f'({br(q)})'


def pot(b, q):
    return f'{b}^{ex(q)}'


ETAPPEN = [
    {'lernziel': 'nte_wurzel', 'titel': 'n-te Wurzeln berechnen',
     'regel': 'Für a ≥ 0 ist ⟦ⁿ√a⟧ die nicht-negative Zahl, deren n-te Potenz a ergibt. n heißt ⟦Wurzelexponent⟧, a heißt Radikand.',
     'schritte': ['⁴√625: Welche Zahl hoch 4 ergibt 625?', '5⁴ = 25 · 25 = 625, also ⁴√625 = ⟦5⟧.'],
     'probe': '5 · 5 · 5 · 5 = 625 ✓',
     'fehler': '⁴√625 = 625 : 4 ist falsch: Der Wurzelexponent sagt, ⟦wie oft⟧ eine Zahl mit sich selbst multipliziert wird – nicht, wodurch man teilt.'},
    {'lernziel': 'potenz_wert', 'titel': 'Potenzen mit Bruch-Exponent berechnen',
     'regel': 'Warum ist 27^(1/3) die dritte Wurzel? Weil (27^(1/3))³ = 27^(1/3 · 3) = 27¹ = 27. Also gilt für a > 0: ⟦a^(m/n) = (ⁿ√a)^m⟧ – der ⟦Nenner⟧ ist die Wurzel, der ⟦Zähler⟧ die Potenz. Ein negativer Exponent bedeutet ⟦Kehrwert⟧: a^(−m/n) = 1 / a^(m/n).',
     'schritte': ['27^(2/3): Nenner 3 heißt dritte Wurzel: ³√27 = 3.', 'Zähler 2 heißt quadrieren: 3² = ⟦9⟧.'],
     'probe': '9³ = 729 = 27² ✓',
     'fehler': '27^(2/3) = 27 · 2 : 3 = 18 ist falsch: Der Nenner bedeutet ⟦Wurzel⟧, der Zähler ⟦Potenz⟧ – man multipliziert nicht mit dem Bruch.'},
    {'lernziel': 'umwandeln', 'titel': 'Wurzeln als Potenzen schreiben',
     'regel': '⟦ⁿ√(x^m) = x^(m/n)⟧ für x ≥ 0: Der Wurzelexponent wird zum ⟦Nenner⟧, der Exponent unter der Wurzel zum ⟦Zähler⟧. Den Bruch kürzen.',
     'schritte': ['⁶√(x⁴): Wurzelexponent 6 in den Nenner, Exponent 4 in den Zähler: x^(4/6).', 'Kürzen: ⟦x^(2/3)⟧.'],
     'probe': '(x^(2/3))³ = x² und (⁶√(x⁴))³ = √(x⁴) = x² ✓',
     'fehler': '⁶√(x⁴) = x^(6/4) ist falsch: Zähler und Nenner sind ⟦vertauscht⟧. Der Wurzelexponent gehört in den Nenner.'},
    {'lernziel': 'zusammenfassen', 'titel': 'Potenzen und Wurzeln zusammenfassen',
     'regel': 'Die Potenzgesetze gelten auch für Bruch-Exponenten (Basis > 0): ⟦x^p · x^q = x^(p+q)⟧, ⟦x^p : x^q = x^(p−q)⟧, ⟦(x^p)^q = x^(p·q)⟧.',
     'schritte': ['√x · ³√x = x^(1/2) · x^(1/3) = x^(1/2 + 1/3).', '1/2 + 1/3 = 3/6 + 2/6 = 5/6, also ⟦x^(5/6) = ⁶√(x⁵)⟧.'],
     'probe': '(x^(5/6))⁶ = x⁵ ✓',
     'fehler': 'x^(1/2) · x^(1/3) = x^(1/6) ist falsch: Beim Multiplizieren werden die Exponenten ⟦addiert⟧, nicht multipliziert.'},
    {'lernziel': 'gleichung_exp', 'titel': 'Gleichungen mit Bruch-Exponent (x > 0)',
     'regel': 'Bei x^(m/n) = c (x > 0) potenzierst du beide Seiten mit dem ⟦Kehrwert⟧ n/m: x = ⟦c^(n/m)⟧. Bei xⁿ = c ist die positive Lösung ⁿ√c.',
     'schritte': ['x^(3/2) = 64 mit x > 0: beide Seiten hoch 2/3.', 'x = 64^(2/3) = (³√64)² = 4² = ⟦16⟧.'],
     'probe': '16^(3/2) = (√16)³ = 4³ = 64 ✓',
     'fehler': 'x^(3/2) = 64 ⇒ x = 64 · 2/3 ist falsch: Man ⟦potenziert⟧ mit dem Kehrwert des Exponenten, man multipliziert nicht.'},
    {'lernziel': 'verstehen', 'titel': 'Aussagen über Potenzen prüfen',
     'regel': 'Bruch-Exponenten sind nur für ⟦Basen ≥ 0⟧ (negative Exponenten: > 0) erklärt. Ein negativer Exponent macht das Ergebnis ⟦nicht negativ⟧, sondern zum Kehrwert.',
     'schritte': ['Behauptung: 25^(−1/2) = −5.', '25^(−1/2) = 1 / 25^(1/2) = 1/√25 = ⟦1/5⟧. Die Behauptung ist falsch.'],
     'probe': '(1/5)² = 1/25 = 25^(−1) ✓',
     'fehler': '9^(1/2) = 4,5 ist falsch: Hoch 1/2 bedeutet ⟦Quadratwurzel⟧, nicht halbieren. 9^(1/2) = 3.'},
]

# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'nte_wurzel': {
  'einstieg': 'In einer Schale wachsen Bakterien. In jeder Stunde wird ihre Anzahl mit derselben Zahl malgenommen. Nach 4 Stunden sind es 625-mal so viele wie am Anfang. Mit welcher Zahl wird pro Stunde malgenommen? Gesucht ist eine Zahl, die viermal mit sich selbst malgenommen 625 ergibt: die ⟦vierte Wurzel⟧ aus 625.',
  'woerter': [['Faktor', 'eine Zahl, mit der man malnimmt'],
              ['5⁴', 'gelesen „5 hoch 4“: 5 · 5 · 5 · 5'],
              ['⁴√625', 'gelesen „vierte Wurzel aus 625“: die Zahl, die hoch 4 genommen 625 ergibt'],
              ['Wurzelexponent n', 'die kleine Zahl links oben am Wurzelzeichen: wie oft malgenommen wird'],
              ['ⁿ√a', 'die n-te Wurzel aus a'],
              ['Radikand', 'die Zahl unter dem Wurzelzeichen']],
  'schritte': ['Gesucht ist ⁴√625: Welche Zahl ergibt viermal mit sich selbst malgenommen 625?',
               'Probiere die 5: 5 · 5 = 25, und 25 · 25 = 625. Das sind vier Fünfen.',
               'Also ist 5⁴ = 625 und damit ⁴√625 = ⟦5⟧.',
               'Für die Bakterien heißt das: Ihre Anzahl wird jede Stunde mit 5 malgenommen.'],
  'regel': 'So findest du ⁿ√a (für a ≥ 0): Suche die Zahl ohne Minus, die ⟦n-mal mit sich selbst malgenommen⟧ a ergibt. Die kleine Zahl n heißt ⟦Wurzelexponent⟧, a heißt ⟦Radikand⟧.',
  'fehler': '⁴√625 = 625 : 4 ≈ 156 ist falsch: Der Wurzelexponent sagt, ⟦wie oft⟧ eine Zahl mit sich selbst malgenommen wird – nicht, wodurch man teilt. Mit dem Faktor 156 pro Stunde gäbe es nach 4 Stunden fast 600 Millionen-mal so viele Bakterien.'},
 'potenz_wert': {
  'einstieg': 'Andere Bakterien werden jede Stunde 3-mal so viele. In 3 Stunden sind es 27-mal so viele, denn 3 · 3 · 3 = 27. Und nach 2 der 3 Stunden? 9-mal so viele. Dafür schreibt man „27 hoch 2/3“: Die 3 unten teilt die 27 in drei gleiche Schritte auf, die 2 oben sagt, dass zwei davon gegangen werden. Das ist eine ⟦Potenz mit Bruch-Exponent⟧.',
  'woerter': [['Exponent', 'die hochgestellte Zahl einer Potenz'],
              ['27^(2/3)', 'gelesen „27 hoch zwei Drittel“'],
              ['Zähler / Nenner', 'die Zahl über / unter dem Bruchstrich; bei 2/3 ist 2 der Zähler, 3 der Nenner'],
              ['Kehrwert', 'der umgedrehte Bruch: von 5 ist es 1/5, von 2/3 ist es 3/2'],
              ['a^(−1/2)', 'ein Minus im Exponenten: der Kehrwert von a^(1/2)']],
  'schritte': ['Gesucht ist 27^(2/3). Der Nenner 3 bedeutet: die dritte Wurzel ziehen.',
               '³√27 = 3, denn 3 · 3 · 3 = 27. Das ist der Faktor für einen Schritt.',
               'Der Zähler 2 bedeutet: diesen Faktor zweimal nehmen, also 3² = 3 · 3 = 9.',
               'Also ist 27^(2/3) = ⟦9⟧: Nach 2 Stunden gibt es 9-mal so viele Bakterien.'],
  'regel': 'So rechnest du a^(m/n) (für a > 0): Der ⟦Nenner⟧ n sagt, welche Wurzel du ziehst, der ⟦Zähler⟧ m, hoch wie viel du danach nimmst: ⟦a^(m/n) = (ⁿ√a)^m⟧. Ein Minus im Exponenten bedeutet ⟦Kehrwert⟧: a^(−m/n) = 1 / a^(m/n).',
  'fehler': '27^(2/3) = 27 · 2 : 3 = 18 ist falsch: Der Nenner bedeutet ⟦Wurzel⟧, der Zähler ⟦Potenz⟧ – man nimmt nicht mit dem Bruch mal. Probe mit den Bakterien: zwei Stunden mit Faktor 3 ergeben 3 · 3 = 9, nicht 18.'},
 'umwandeln': {
  'einstieg': 'Für dieselbe Uhrzeit gibt es zwei Schreibweisen: „halb drei“ und „14:30“. Auch Wurzeln kann man anders schreiben, nämlich als Potenz mit einem Bruch im Exponenten. Die Quadratwurzel aus einer Zahl ist dieselbe Zahl hoch ein halb. Dieses ⟦Umschreiben⟧ lohnt sich, weil man mit Potenzen gut weiterrechnen kann.',
  'woerter': [['x^(1/2)', 'dasselbe wie √x'],
              ['⁶√(x⁴)', 'die sechste Wurzel aus x hoch 4'],
              ['kürzen', 'Zähler und Nenner durch dieselbe Zahl teilen: 4/6 = 2/3'],
              ['x ≥ 0', 'x ist nicht negativ']],
  'schritte': ['Gesucht ist ⁶√(x⁴), geschrieben als Potenz.',
               'Die kleine 6 am Wurzelzeichen wird zum Nenner des Exponenten.',
               'Die 4 unter der Wurzel wird zum Zähler. So entsteht x^(4/6).',
               'Den Bruch kürzen: 4/6 = 2/3. Also ist ⁶√(x⁴) = ⟦x^(2/3)⟧.'],
  'regel': 'So schreibst du eine Wurzel als Potenz (für x ≥ 0): ⟦ⁿ√(x^m) = x^(m/n)⟧. Der Wurzelexponent kommt in den ⟦Nenner⟧, der Exponent unter der Wurzel in den ⟦Zähler⟧. Danach den Bruch kürzen.',
  'fehler': '⁶√(x⁴) = x^(6/4) ist falsch: Zähler und Nenner sind ⟦vertauscht⟧. Merkhilfe: Das Wurzelzeichen „teilt“ – sein Exponent gehört in den Nenner.'},
 'zusammenfassen': {
  'einstieg': 'Zurück zu den Bakterien. Erst wachsen sie eine halbe Stunde, dann noch eine Drittelstunde. Zusammen sind das 1/2 + 1/3 = 5/6 Stunde. Beim Rechnen heißt das: Bei gleicher Basis werden die Exponenten ⟦addiert⟧ – genau wie bei 2³ · 2² = 2⁵.',
  'woerter': [['Basis', 'die Zahl unten bei einer Potenz; bei x^(1/2) ist es x'],
              ['Potenzgesetze', 'Rechenregeln für Potenzen mit gleicher Basis'],
              ['(x^p)^q', 'eine Potenz noch einmal hoch q nehmen'],
              ['x^(p+q)', 'x hoch (p + q): die Exponenten wurden zusammengezählt']],
  'schritte': ['Gesucht ist √x · ³√x, zusammengefasst zu einer Potenz (x > 0).',
               'Beide Wurzeln als Potenz schreiben: x^(1/2) · x^(1/3).',
               'Gleiche Basis beim Malnehmen: Exponenten addieren. 1/2 + 1/3 = 3/6 + 2/6 = 5/6.',
               'Ergebnis: ⟦x^(5/6) = ⁶√(x⁵)⟧.'],
  'regel': 'So fasst du zusammen (Basis > 0): Wurzeln zuerst als Potenzen schreiben. Dann gelten die ⟦Potenzgesetze⟧: beim Malnehmen Exponenten ⟦addieren⟧ (x^p · x^q = x^(p+q)), beim Teilen ⟦subtrahieren⟧ (x^p : x^q = x^(p−q)), bei einer Potenz einer Potenz ⟦malnehmen⟧ ((x^p)^q = x^(p·q)).',
  'fehler': 'x^(1/2) · x^(1/3) = x^(1/6) ist falsch: Beim Malnehmen werden die Exponenten ⟦addiert⟧, nicht malgenommen. Eine halbe und eine Drittelstunde sind zusammen 5/6 Stunde, nicht 1/6.'},
 'gleichung_exp': {
  'einstieg': 'Jetzt geht es rückwärts: Nach anderthalb Stunden sind es 64-mal so viele Bakterien. Mit welchem Faktor wachsen sie pro Stunde? Gesucht ist die Zahl, die hoch 3/2 genommen 64 ergibt. Man löst diese ⟦Gleichung⟧, indem man das Hochnehmen rückgängig macht.',
  'woerter': [['x', 'die gesuchte Zahl, hier der Faktor pro Stunde'],
              ['x^(3/2) = 64', 'die Frage: Welche Zahl x ergibt hoch 3/2 genau 64?'],
              ['Kehrwert', '3/2 umgedreht ist 2/3'],
              ['x > 0', 'nur Lösungen größer als 0 sind gesucht']],
  'schritte': ['Die Gleichung heißt x^(3/2) = 64, gesucht ist x > 0.',
               'Nimm beide Seiten hoch 2/3, also hoch dem Kehrwert von 3/2. Links bleibt x übrig, weil 3/2 · 2/3 = 1 ist.',
               'Rechts rechnen: 64^(2/3) = (³√64)² = 4² = 16.',
               'Also ist ⟦x = 16⟧: Die Bakterien werden pro Stunde 16-mal so viele.'],
  'regel': 'So löst du x^(m/n) = c (für x > 0): Beide Seiten mit dem ⟦Kehrwert⟧ n/m potenzieren. Dann ist ⟦x = c^(n/m)⟧. Bei xⁿ = c ist die positive Lösung ⁿ√c.',
  'fehler': 'x^(3/2) = 64 ⇒ x = 64 · 2/3 ≈ 42,7 ist falsch: Man ⟦potenziert⟧ mit dem Kehrwert, man nimmt nicht mal. Probe: 42,7 hoch 3/2 ist etwa 279, nicht 64.'},
 'verstehen': {
  'einstieg': 'Ein Minus im Exponenten heißt beim Wachstum: zurück in die Vergangenheit. Werden Bakterien pro Stunde 25-mal so viele, dann waren es eine halbe Stunde früher nur ein Fünftel so viele. Ein Minus im Exponenten macht also nichts negativ – es bildet den ⟦Kehrwert⟧.',
  'woerter': [['25^(−1/2)', '25 hoch minus ein halb, also 1 / 25^(1/2)'],
              ['Behauptung', 'eine Aussage, die du prüfen sollst'],
              ['Kehrwert', 'der umgedrehte Bruch: von 5 ist es 1/5']],
  'schritte': ['Behauptung: 25^(−1/2) = −5. Stimmt das?',
               'Das Minus im Exponenten bedeutet Kehrwert: 25^(−1/2) = 1 / 25^(1/2).',
               '25^(1/2) ist die Quadratwurzel: √25 = 5.',
               'Also ist 25^(−1/2) = ⟦1/5⟧. Die Behauptung ist falsch.'],
  'regel': 'So prüfst du Aussagen über Potenzen: Bruch-Exponenten sind nur für ⟦Basen ≥ 0⟧ erklärt (bei negativem Exponenten nur für Basen > 0). Ein Minus im Exponenten bedeutet ⟦Kehrwert⟧, nicht „Ergebnis negativ“. Hoch 1/2 bedeutet ⟦Quadratwurzel⟧.',
  'fehler': '9^(1/2) = 4,5 ist falsch: Hoch 1/2 bedeutet ⟦Quadratwurzel⟧, nicht halbieren. 9^(1/2) = 3, denn 3 · 3 = 9.'},
}
klar(ETAPPEN, KLAR)
# ---- KLAR ENDE ----
# ---- UMBAU (neues Muster, Runde 8, Vorgabe 16.11.) ----
def _zeile(*w): return [['Anzahl ·', *w]]
UMBAU = {
 'nte_wurzel': {
  'einstieg': 'Bakterien werden jede Stunde mit derselben Zahl malgenommen. Nach 4 Stunden sind es 625-mal so viele. Gesucht ist die ⟦vierte Wurzel⟧ aus 625.',
  'woerter': [['vierte Wurzel', 'die Zahl, die viermal mit sich selbst malgenommen die Zahl ergibt; Zeichen ⁴√'],
              ['Wurzelexponent', 'die kleine Zahl am Wurzelzeichen, hier 4'],
              ['5⁴', '5 · 5 · 5 · 5']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stunde', '0', '1', '2', '3', '4'], 'zeilen': _zeile('1', '?', '?', '?', '625')},
  'schritte': [{'text': 'Der Wurzelexponent 4 sagt: viermal mit derselben Zahl malnehmen.'},
               {'text': 'Probiere 5: Stunde für Stunde 5, 25, 125 und 625.',
                'bild': {'zeilen': _zeile('1', '5', '25', '125', '625')}},
               {'text': 'Also 5⁴ = 625 und ⁴√625 = ⟦5⟧. Pro Stunde mal 5.'}],
  'fehler': '⁴√625 ist nicht 625 : 4 ≈ 156. Mit Faktor 156 pro Stunde gäbe es nach 4 Stunden fast 600 Millionen-mal so viele.',
  'fehler_bild': {'zeilen': _zeile('1', '156', '24 336', '…', 'fast 600 Mio.')},
  'regel': 'ⁿ√a ist die Zahl ohne Minus, die hoch n genau a ergibt. Die kleine Zahl n heißt ⟦Wurzelexponent⟧.'},
 'potenz_wert': {
  'einstieg': 'Bakterien werden in 3 Stunden 27-mal so viele. Wie viele sind es nach 2 der 3 Stunden? Das beschreibt eine ⟦Potenz mit Bruch-Exponent⟧: 27^(2/3).',
  'woerter': [['27^(2/3)', 'gelesen „27 hoch zwei Drittel“'],
              ['Exponent', 'die Hochzahl, hier der Bruch 2/3']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stunde', '0', '1', '2', '3'], 'zeilen': _zeile('1', '?', '?', '27')},
  'schritte': [{'text': 'Der Nenner 3 im Exponent heißt: dritte Wurzel. ³√27 = 3 pro Stunde.',
                'bild': {'zeilen': _zeile('1', '3', '?', '27')}},
               {'text': 'Der Zähler 2 heißt: zwei Stunden, also 3² = 9.',
                'bild': {'zeilen': _zeile('1', '3', '9', '27')}},
               {'text': 'Also ist 27^(2/3) = ⟦9⟧: nach 2 Stunden 9-mal so viele.'}],
  'fehler': '27^(2/3) ist nicht 27 · 2 : 3 = 18. Zwei Stunden mit Faktor 3 ergeben 3 · 3 = 9, nicht 18.',
  'fehler_bild': {'zeilen': _zeile('1', '3', '18?', '27')},
  'regel': 'Nenner = Wurzel, Zähler = Potenz: a^(m/n) = (ⁿ√a)^m. Ein Minus im Exponenten heißt ⟦Kehrwert⟧.'},
 'umwandeln': {
  'einstieg': '„Halb drei“ und „14:30“ meinen dieselbe Uhrzeit. Auch eine Wurzel kann man anders schreiben, nämlich als Potenz. Dieses ⟦Umschreiben⟧ hilft beim Weiterrechnen.',
  'woerter': [['x^(1/2)', 'x hoch ein halb, dasselbe wie √x'],
              ['Umschreiben', 'dieselbe Zahl in einer anderen Schreibweise angeben']],
  'bild': {'typ': 'tabelle', 'kopf': ['Wurzel', 'Potenz'], 'zeilen': [['√x', 'x^(1/2)'], ['³√x', 'x^(1/3)'], ['⁶√(x⁴)', '?']]},
  'schritte': [{'text': 'Bekannt ist √x = x^(1/2). Gesucht ist ⁶√(x⁴) als Potenz.'},
               {'text': 'Der Wurzelexponent 6 wird der Nenner, die 4 der Zähler: x^(4/6).',
                'bild': {'zeilen': [['√x', 'x^(1/2)'], ['³√x', 'x^(1/3)'], ['⁶√(x⁴)', 'x^(4/6)']]}},
               {'text': 'Bruch kürzen: 4/6 = 2/3. Also ⁶√(x⁴) = ⟦x^(2/3)⟧.',
                'bild': {'zeilen': [['√x', 'x^(1/2)'], ['³√x', 'x^(1/3)'], ['⁶√(x⁴)', 'x^(2/3)']]}}],
  'fehler': '⁶√(x⁴) ist nicht x^(6/4): Zähler und Nenner sind vertauscht. Das Wurzelzeichen teilt – sein Exponent gehört nach unten.',
  'fehler_bild': {'zeilen': [['√x', 'x^(1/2)'], ['³√x', 'x^(1/3)'], ['⁶√(x⁴)', 'x^(6/4)?']]},
  'regel': 'ⁿ√(x^m) = x^(m/n): Der Wurzelexponent kommt in den ⟦Nenner⟧. Danach den Bruch kürzen.'},
 'zusammenfassen': {
  'einstieg': 'Bakterien wachsen erst eine halbe Stunde, dann eine Drittelstunde. Zusammen sind das 5/6 Stunde. Bei gleicher Basis werden die Exponenten ⟦addiert⟧.',
  'woerter': [['Basis', 'die Zahl unten, die hoch genommen wird, hier x'],
              ['Potenzgesetz', 'eine Rechenregel für Potenzen mit gleicher Basis']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': 6, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Gesucht ist √x · ³√x als eine Potenz.'},
               {'text': 'Als Potenzen geschrieben: x^(1/2) · x^(1/3).',
                'bild': {'boegen': [{'von': 0, 'bis': 0.5, 'name': '1/2'}]}},
               {'text': 'Potenzgesetz: Beim Malnehmen die Exponenten addieren: 1/2 + 1/3 = 5/6.',
                'bild': {'boegen': [{'von': 0, 'bis': 0.5, 'name': '1/2'}, {'von': 0.5, 'bis': 0.8333, 'name': '1/3'}],
                         'punkte': [{'wert': 0.8333, 'name': '5/6'}]}},
               {'text': 'Ergebnis: √x · ³√x = ⟦x^(5/6)⟧.'}],
  'fehler': 'x^(1/2) · x^(1/3) ist nicht x^(1/6). Exponenten werden addiert, nicht malgenommen. Halbe plus Drittelstunde sind 5/6 Stunde.',
  'fehler_bild': {'punkte': [{'wert': 0.8333, 'name': '5/6'}, {'wert': 0.1667, 'name': '1/6?'}]},
  'regel': 'Gleiche Basis: beim Malnehmen Exponenten ⟦addieren⟧. Beim Teilen subtrahieren, bei (x^p)^q malnehmen.'},
 'gleichung_exp': {
  'einstieg': 'Nach anderthalb Stunden sind es 64-mal so viele Bakterien. Mit welchem Faktor x pro Stunde? Gesucht ist x mit x^(3/2) = 64: eine ⟦Gleichung⟧.',
  'woerter': [['Kehrwert', 'der umgedrehte Bruch: von 3/2 ist es 2/3'],
              ['potenzieren', 'hoch eine Zahl nehmen']],
  'bild': {'typ': 'tabelle', 'kopf': ['x (Faktor)', '4', '9', '?'], 'zeilen': [['x^(3/2)', '?', '?', '64']]},
  'schritte': [{'text': 'Gesucht ist x > 0 mit x^(3/2) = 64.'},
               {'text': 'Beide Seiten mit dem Kehrwert 2/3 potenzieren. Links bleibt x.'},
               {'text': 'Rechts: 64^(2/3) = (³√64)² = 4² = 16.',
                'bild': {'kopf': ['x (Faktor)', '4', '9', '16'], 'zeilen': [['x^(3/2)', '8', '27', '64']]}},
               {'text': 'Also ist ⟦x = 16⟧: pro Stunde 16-mal so viele.'}],
  'fehler': 'x ist nicht 64 · 2/3 ≈ 42,7. Man potenziert mit dem Kehrwert und nimmt nicht mal. Probe: 42,7^(3/2) ≈ 279.',
  'fehler_bild': {'kopf': ['x (Faktor)', '16', '42,7?'], 'zeilen': [['x^(3/2)', '64', '≈ 279']]},
  'regel': 'Potenziere beide Seiten mit dem ⟦Kehrwert⟧ des Exponenten. Aus x^(m/n) = c wird x = c^(n/m).'},
 'verstehen': {
  'einstieg': 'Bakterien werden pro Stunde 25-mal so viele. Eine halbe Stunde früher waren es nur 1/5 so viele. Ein Minus im Exponenten bildet den ⟦Kehrwert⟧.',
  'woerter': [['Kehrwert', '1 geteilt durch die Zahl: von 5 ist es 1/5'],
              ['25^(−1/2)', 'gelesen „25 hoch minus ein halb“'],
              ['Behauptung', 'eine Aussage, die man prüft']],
  'bild': {'typ': 'tabelle', 'kopf': ['Stunde', '−1/2', '0', '1/2', '1'], 'zeilen': _zeile('?', '1', '?', '25')},
  'schritte': [{'text': 'Behauptung: 25^(−1/2) = −5. Stimmt das?'},
               {'text': 'Das Minus im Exponenten heißt Kehrwert: 25^(−1/2) = 1 : 25^(1/2).'},
               {'text': 'Hoch 1/2 ist die Quadratwurzel: √25 = 5.', 'bild': {'zeilen': _zeile('?', '1', '5', '25')}},
               {'text': 'Also 25^(−1/2) = ⟦1/5⟧. Die Behauptung ist falsch.', 'bild': {'zeilen': _zeile('1/5', '1', '5', '25')}}],
  'fehler': '9^(1/2) ist nicht 4,5. Hoch 1/2 heißt Quadratwurzel, nicht halbieren: 9^(1/2) = 3, denn 3 · 3 = 9.',
  'regel': 'Ein Minus im Exponenten heißt ⟦Kehrwert⟧, nicht negativ. Hoch 1/2 heißt Quadratwurzel. Bruch-Exponenten gibt es nur für Basen ≥ 0.'},
}
umbau(ETAPPEN, UMBAU)
# ---- UMBAU ENDE ----


def g_nte_wurzel(s):
    if s == 1:
        n = R.choice([3, 4])
        r = R.randint(2, 5 if n == 3 else 4)
    elif s == 2:
        if R.random() < 0.5:
            n, r = R.choice([4, 5, 6]), Fr(R.randint(1, 5), 10)
            a = r ** n
            return zahl(f'Berechne {wz(n, dz(a))}.', f'{dz(r)}^{n} = {dz(a)}, also {wz(n, dz(a))} = {dz(r)}.',
                        'Ziehe die Wurzel ohne Komma; die Nachkommastellen werden durch ' + str(n) + ' geteilt.', r,
                        f'{float(a)} / {float(r)} ** {n - 1}')
        n = R.choice([2, 3, 4, 5])
        k = R.randint(2, 4)
        b = R.randint(2, {2: 9, 3: 5, 4: 3, 5: 2}[n] if k < 4 else 2)
        if b ** (n * k) > 10 ** 7: return None
        return zahl(f'Berechne {wz(n, "(" + str(b) + "^" + str(n * k) + ")")}.',
                    f'{b}^{n * k} = ({b}^{k})^{n}, also {wz(n, "(" + str(b) + "^" + str(n * k) + ")")} = {b}^{k} = {dz(b ** k)}.',
                    'Teile den Exponenten unter der Wurzel durch den Wurzelexponenten.', b ** k, f'{b} ** ({n * k} // {n})')
    else:
        if R.random() < 0.5:
            n1, n2 = R.sample([3, 4, 5], 2)
            r1, r2 = R.randint(2, 4), R.randint(2, 4)
            k = R.randint(2, 5)
            e = k * r1 - r2
            return zahl(f'Berechne {k} · {wz(n1, dz(r1 ** n1))} − {wz(n2, dz(r2 ** n2))}.',
                        f'{wz(n1, dz(r1 ** n1))} = {r1}, {wz(n2, dz(r2 ** n2))} = {r2}; {k} · {r1} − {r2} = {e}.',
                        'Berechne jede Wurzel einzeln, dann Punkt vor Strich.', e,
                        f'{k} * ({r1 ** n1} / {r1} ** {n1 - 1}) - {r2 ** n2} / {r2} ** {n2 - 1}')
        n = R.choice([4, 5, 6])
        b = R.choice([2, 4, 5]) if n != 6 else 2
        a = Fr(1, b ** n)
        return zahl(f'Berechne {wz(n, "(1/" + dz(b ** n) + ")")} als Dezimalzahl.',
                    f'{b}^{n} = {dz(b ** n)}, also {wz(n, "(1/" + dz(b ** n) + ")")} = 1/{b} = {dz(Fr(1, b))}.',
                    'Ziehe die Wurzel aus Zähler und Nenner einzeln.', Fr(1, b), f'1 / ({b ** n} / {b} ** {n - 1})')
    a = r ** n
    return zahl(f'Berechne {wz(n, dz(a))}.', f'{r}^{n} = {dz(a)}, also {wz(n, dz(a))} = {r}.',
                'Welche Zahl ergibt ' + str(n) + '-mal mit sich selbst multipliziert den Radikanden?', r, f'{a} / {r} ** {n - 1}')


def g_potenz_wert(s):
    if s >= 2 and R.random() < 0.3:
        n, m = R.choice([(3, 2), (4, 3), (2, 3), (3, 4), (2, 5), (5, 2), (4, 5)])
        r = R.randint(2, {2: 6, 3: 4, 4: 3, 5: 2}[n])
        a = r ** n
        A_ = f'erst {wz(n, dz(a))} = {r}, dann {r}^{m} = {dz(r ** m)}'
        B_ = f'erst {dz(a)}^{m} = {dz(a ** m)}, dann {wz(n, dz(a ** m))} = {dz(r ** m)}'
        return auswahl(f'{pot(dz(a), Fr(m, n))}: Weg A: {A_}. Weg B: {B_}. Was stimmt?',
                       'Beide Wege sind richtig; A ist im Kopf leichter.',
                       ['Nur A ist richtig.', 'Nur B ist richtig.', 'Keiner: man rechnet ' + dz(a) + ' · ' + str(m) + ' : ' + str(n) + '.'],
                       f'(ⁿ√a)^m = ⁿ√(a^m). Beide Wege führen zu {dz(r ** m)}. Erst die Wurzel ziehen hält die Zahlen klein.',
                       'Prüfe, ob beide Wege dasselbe Ergebnis liefern.')
    n = R.choice([2, 3, 4]) if s < 3 else R.choice([2, 3, 4, 5])
    r = R.randint(2, {2: 12, 3: 5, 4: 3, 5: 2}[n])
    m = 1 if s == 1 else R.randint(2, 3 if n > 2 else 5)
    if Fr(m, n).denominator != n: return None
    a = r ** n
    if s == 3:
        e = Fr(1, r ** m)
        t = f'Berechne {pot(dz(a), Fr(-m, n))}.'
        w = f'{pot(dz(a), Fr(-m, n))} = 1 / {pot(dz(a), Fr(m, n))} = 1 / ({wz(n, dz(a))})^{m} = 1 / {r}^{m} = {br(e)}.'
        h = 'Negativer Exponent: Kehrwert bilden. Dann Wurzel (Nenner) und Potenz (Zähler).'
        if endlich(e):
            return zahl(t + ' Gib das Ergebnis als Dezimalzahl an.', w[:-1] + f' = {dz(e)}.', h, e, f'1 / {r} ** {m}')
        return luecken(t, '1/□', 'Nenner', [r ** m], w, h, c=[f'{r} ** {m}'])
    e = r ** m
    return zahl(f'Berechne {pot(dz(a), Fr(m, n))}.',
                f'Nenner {n}: {wz(n, dz(a))} = {r}' + (f'; Zähler {m}: {r}^{m} = {dz(e)}.' if m > 1 else '; Zähler 1: Ergebnis ' + dz(e) + '.'),
                'Der Nenner des Exponenten gibt die Wurzel an, der Zähler die Potenz.', e, f'{r} ** {m}')


def g_umwandeln(s):
    if s == 1:
        n = R.randint(2, 9)
        if R.random() < 0.5:
            return luecken(f'Schreibe {wz(n, "x") if n > 2 else "√x"} (x ≥ 0) als Potenz.', 'x^(□/□)', 'Zähler / Nenner', [1, n],
                           f'{"√x" if n == 2 else wz(n, "x")} = x^(1/{n}): Wurzelexponent {n} wird Nenner.',
                           'Welche Zahl gehört in den Nenner: der Wurzelexponent oder die Hochzahl?', c=['1', f'{n}'])
        m = R.randint(2, 9)
        if Fr(m, n).denominator != n: return None
        return luecken(f'Schreibe {wz(n, "(x" + str(m).translate(HOCH) + ")")} (x ≥ 0) als Potenz mit Bruch-Exponent.', 'x^(□/□)',
                       'Zähler / Nenner', [m, n], f'Wurzelexponent {n} in den Nenner, Exponent {m} in den Zähler: x^({m}/{n}).',
                       'Der Wurzelexponent wird zum Nenner.', c=[f'{m}', f'{n}'])
    if s == 2:
        n, m = R.randint(3, 12), R.randint(2, 10)
        q = Fr(m, n)
        if q.denominator in (1, n): return None
        return luecken(f'Schreibe {wz(n, "(x" + str(m).translate(HOCH) + ")")} (x ≥ 0) als Potenz. Kürze den Exponenten.', 'x^(□/□)',
                       'Zähler / Nenner (gekürzt)', [q.numerator, q.denominator],
                       f'x^({m}/{n}), gekürzt x^({q.numerator}/{q.denominator}).', 'Erst umschreiben, dann den Bruch im Exponenten kürzen.',
                       c=[f'{m} // {m // q.numerator}', f'{n} // {n // q.denominator}'])
    if R.random() < 0.5:
        n, m = R.randint(2, 7), R.randint(2, 7)
        if Fr(m, n).denominator != n: return None
        richtig = wz(n, f'(x{str(m).translate(HOCH)})') if n > 2 else f'√(x{str(m).translate(HOCH)})'
        falsch = [wz(m, f'(x{str(n).translate(HOCH)})') if m > 2 else f'√(x{str(n).translate(HOCH)})', f'x{str(m).translate(HOCH)} : {n}',
                  f'{n} · √(x{str(m).translate(HOCH)})']
        return auswahl(f'Welcher Term ist gleich x^({m}/{n}) für x ≥ 0?', richtig, falsch,
                       f'Nenner {n} wird zum Wurzelexponenten, Zähler {m} zum Exponenten unter der Wurzel: x^({m}/{n}) = {richtig}.',
                       'Welche Zahl wird zum Wurzelexponenten?')
    n = R.randint(2, 8)
    return luecken(f'Schreibe 1/{wz(n, "x") if n > 2 else "√x"} (x > 0) als Potenz.', 'x^(□/□)', 'Zähler (mit Vorzeichen) / Nenner',
                   [-1, n], f'1/{wz(n, "x") if n > 2 else "√x"} = 1/x^(1/{n}) = x^(−1/{n}).',
                   'Ein Bruch mit Potenz im Nenner lässt sich mit negativem Exponenten schreiben.', c=['-1', f'{n}'])


def g_zusammenfassen(s):
    def q_txt(q):
        return f'x^({br(q)})' if q.denominator > 1 else f'x^{dz(q)}'
    if s >= 2 and R.random() < 0.3:
        if R.random() < 0.5:
            n = R.choice([2, 3, 4])
            r = R.randint(2, {2: 12, 3: 5, 4: 3}[n])
            teiler = [d for d in range(2, r ** n) if (r ** n) % d == 0 and d != r and (r ** n) // d != r]
            if not teiler: return None
            a = R.choice(teiler)
            b = r ** n // a
            return zahl(f'Berechne {pot(dz(a), Fr(1, n))} · {pot(dz(b), Fr(1, n))}.',
                        f'Gleicher Exponent: {pot(dz(a), Fr(1, n))} · {pot(dz(b), Fr(1, n))} = ({dz(a)} · {dz(b)})^({br(Fr(1, n))}) = {pot(dz(r ** n), Fr(1, n))} = {r}.',
                        'Gleicher Exponent: erst die Basen multiplizieren.', r, f'({a} * {b}) / {r} ** {n - 1}')
        r = R.choice([2, 3])
        N = R.choice([6, 4]) if r == 3 else R.choice([6, 4, 8])
        a = r ** N
        if a > 10 ** 4: return None
        z1 = R.randint(2, N - 1)
        p_ = Fr(z1, N)
        q_ = p_ - Fr(1, N) * R.randint(1, z1 - 1) if z1 > 1 else None
        if q_ is None or q_ <= 0: return None
        e = p_ - q_
        if (e * N).denominator != 1: return None
        erg = r ** int(e * N)
        return zahl(f'Berechne {pot(dz(a), p_)} : {pot(dz(a), q_)}.',
                    f'Gleiche Basis: Exponenten subtrahieren: {br(p_)} − {br(q_)} = {br(e)}. {pot(dz(a), e)} = {dz(erg)}, denn {dz(a)} = {r}^{N}.',
                    'Gleiche Basis: Beim Teilen werden die Exponenten subtrahiert.', erg, f'{r} ** {int(e * N)}')
    typ = R.choice({1: 'm', 2: 'mdp', 3: 'wk'}[s])
    if typ == 'm':
        p, q = Fr(R.randint(1, 5), R.randint(2, 6)), Fr(R.randint(1, 5), R.randint(2, 6))
        e, t, w = p + q, f'{q_txt(p)} · {q_txt(q)}', 'addiert'
    elif typ == 'd':
        p, q = Fr(R.randint(1, 9), R.randint(2, 6)), Fr(R.randint(1, 5), R.randint(2, 6))
        e, t, w = p - q, f'{q_txt(p)} : {q_txt(q)}', 'subtrahiert'
    elif typ == 'p':
        p, q = Fr(R.randint(1, 5), R.randint(2, 6)), Fr(R.randint(1, 5), R.randint(2, 6))
        e, t, w = p * q, f'({q_txt(p)})^({br(q)})', 'multipliziert'
    elif typ == 'w':
        n1, n2 = R.sample([2, 3, 4, 5, 6], 2)
        m1 = R.randint(1, 3)
        p, q = Fr(m1, n1), Fr(1, n2)
        if p.denominator != n1: return None
        w1 = ('√' if n1 == 2 else wz(n1, '')) + (f'(x{str(m1).translate(HOCH)})' if m1 > 1 else 'x')
        w2 = ('√' if n2 == 2 else wz(n2, '')) + 'x'
        e, t, w = p + q, f'{w1} · {w2}', 'addiert'
    else:
        n1, n2 = R.sample([2, 3, 4, 5], 2)
        p, q = Fr(1, n1), Fr(1, n2)
        w1 = ('√' if n1 == 2 else wz(n1, '')) + 'x'
        w2 = ('√' if n2 == 2 else wz(n2, '')) + 'x'
        e, t, w = p - q, f'{w1} : {w2}', 'subtrahiert'
    if p.denominator == 1 or q.denominator == 1 or e.denominator == 1 or e == 0: return None
    tipp = ('Schreibe Wurzeln als Potenzen und wende das passende Potenzgesetz an.' if typ in 'wk' else
            {'m': 'Gleiche Basis: Beim Malnehmen werden die Exponenten addiert.', 'd': 'Gleiche Basis: Beim Teilen werden die Exponenten subtrahiert.',
             'p': 'Potenz einer Potenz: Die Exponenten werden multipliziert.'}[typ])
    return luecken(f'Fasse zu einer Potenz zusammen (x > 0): {t}.', 'x^(□/□)', 'Zähler (mit Vorzeichen) / Nenner, gekürzt',
                   [e.numerator, e.denominator],
                   f'Exponenten {w}: {br(p)} und {br(q)} ergibt {br(e)}, also x^({br(e)}).',
                   tipp,
                   c=[f'{e.numerator}', f'{e.denominator}'])


def g_gleichung_exp(s):
    if s == 1:
        n = R.choice([2, 3, 4, 5])
        r = R.randint(2, {2: 15, 3: 6, 4: 4, 5: 3}[n])
        c = r ** n
        return zahl(f'Löse x^{n} = {dz(c)} für x > 0.', f'x = {wz(n, dz(c))} = {r}, denn {r}^{n} = {dz(c)}.',
                    'Ziehe auf beiden Seiten die passende Wurzel.', r, f'{c} / {r} ** {n - 1}')
    typ = R.random()
    if s == 2 and typ < 0.35 or s == 3 and typ < 0.1:
        n = R.choice([2, 3, 4])
        c = R.randint(2, {2: 15, 3: 6, 4: 4}[n])
        x = c ** n
        return zahl(f'Löse x^(1/{n}) = {c} für x > 0.', f'Beide Seiten hoch {n}: x = {c}^{n} = {dz(x)}.',
                    'Mit welcher Zahl musst du potenzieren, damit links nur x steht?', x, f'{c} ** {n}')
    if s == 3 and typ < 0.45:
        k = R.randint(2, 5)
        m, n = R.choice([(3, 2), (2, 3), (3, 4), (4, 3)])
        r = R.randint(2, {2: 5, 3: 4, 4: 3}[n])
        x, c = r ** n, r ** m
        return zahl(f'Löse {k} · x^({m}/{n}) = {dz(k * c)} für x > 0.',
                    f'Erst durch {k} teilen: x^({m}/{n}) = {dz(c)}. Dann hoch {n}/{m}: x = ({wz(m, dz(c))})^{n} = {r}^{n} = {dz(x)}.',
                    'Bringe zuerst die Potenz allein auf eine Seite.', x, f'{r} ** {n}')
    if s == 3 and typ < 0.7:
        n = R.choice([3, 5])
        r = R.randint(2, 6 if n == 3 else 3)
        return zahl(f'Löse x^{n} = −{dz(r ** n)}.',
                    f'Ungerader Exponent: Es gibt genau eine Lösung, und sie ist negativ. (−{r})^{n} = −{dz(r ** n)}, also x = −{r}.',
                    'Bei ungeradem Exponenten bleibt das Minuszeichen erhalten.', -r, f'-({r ** n} / {r} ** {n - 1})')
    m, n = R.choice([(3, 2), (2, 3), (3, 4), (4, 3), (5, 2), (2, 5), (3, 5)])
    r = R.randint(2, {2: 6, 3: 4, 4: 3, 5: 2}[n] if n != 2 else 5)
    # x = r^n  ⇒  x^(m/n) = r^m
    x, c = r ** n, r ** m
    return zahl(f'Löse x^({m}/{n}) = {dz(c)} für x > 0.',
                f'Beide Seiten hoch {n}/{m}: x = {dz(c)}^({n}/{m}) = ({wz(m, dz(c))})^{n} = {r}^{n} = {dz(x)}.',
                'Potenziere mit dem Kehrwert des Exponenten.', x, f'{r} ** {n}')


def g_verstehen(s):
    typ = R.choice({1: 'ab', 2: 'abcd', 3: 'cde'}[s])
    if typ == 'a':
        r = R.randint(2, 12)
        a = r * r
        return auswahl(f'Was ist {a}^(−1/2)?', f'1/{r}', [f'−{r}', f'−{dz(Fr(a, 2))}', f'{dz(Fr(a, 2))}'],
                       f'{a}^(−1/2) = 1 / {a}^(1/2) = 1/√{a} = 1/{r}.', 'Negativer Exponent: Kehrwert. Hoch 1/2: Quadratwurzel.')
    if typ == 'b':
        r = R.randint(2, 15)
        a = r * r
        if a % 2: a2 = dz(Fr(a, 2))
        else: a2 = dz(a // 2)
        return auswahl(f'Jemand rechnet {a}^(1/2) = {a2}. Was stimmt?', f'Falsch, {a}^(1/2) = √{a} = {r}.',
                       ['Richtig, hoch 1/2 bedeutet halbieren.', f'Falsch, {a}^(1/2) = {dz(a * a)}.', f'Falsch, {a}^(1/2) = −{r}.'],
                       f'Hoch 1/2 bedeutet Quadratwurzel: √{a} = {r}, denn {r}² = {a}.', 'Was bedeutet der Nenner 2 im Exponenten?')
    if typ == 'c':
        n = R.choice([3, 5])
        r = R.randint(2, 4)
        a = r ** n
        return auswahl(f'Ist (−{a})^(1/{n}) nach der Definition aus dem Unterricht erklärt?',
                       'Nein, Bruch-Exponenten sind nur für nicht-negative Basen definiert.',
                       [f'Ja, (−{a})^(1/{n}) = −{r}.', f'Ja, (−{a})^(1/{n}) = {r}.', f'Ja, (−{a})^(1/{n}) = −{br(Fr(a, n))}.'],
                       f'Zwar ist (−{r})^{n} = −{a}, aber die Schreibweise a^(1/n) ist nur für a ≥ 0 festgelegt – sonst entstünden Widersprüche (z. B. (−8)^(1/3) und (−8)^(2/6)).',
                       'Für welche Basen ist a^(1/n) festgelegt?')
    if typ == 'd':
        n, k = R.randint(2, 5), R.randint(2, 3)
        return auswahl(f'Welche Aussage gilt für x ≥ 0?', f'x^({k}/{k * n}) = x^(1/{n})',
                       [f'x^({k}/{k * n}) = x^{k}', f'x^({k}/{k * n}) = x^({k * n}/{k})', f'x^({k}/{k * n}) = {k} · x^(1/{n})'],
                       f'Den Bruch im Exponenten darf man kürzen: {k}/{k * n} = 1/{n}.', 'Kann man den Bruch im Exponenten kürzen?')
    r = R.randint(2, 4)
    m, n = R.choice([(2, 3), (3, 2), (3, 4), (2, 5)])
    if n == 2: r = R.randint(2, 9)
    a = r ** n
    return auswahl(f'Jemand rechnet {a}^({m}/{n}) = {a} · {m} : {n}. Was ist richtig?', f'{a}^({m}/{n}) = {dz(r ** m)}',
                   [f'{a}^({m}/{n}) = {br(Fr(a * m, n))}', f'{a}^({m}/{n}) = {br(Fr(a * n, m))}', f'{a}^({m}/{n}) = {dz(r * m)}'],
                   f'Nenner {n}: {wz(n, a)} = {r}; Zähler {m}: {r}^{m} = {dz(r ** m)}.', 'Nenner = Wurzel, Zähler = Potenz.')


import re  # noqa: E402


def _hoch(t):
    return re.sub(r'\^(\d+)', lambda m_: m_.group(1).translate(HOCH), t)


def _schoen(g):
    def f(s):
        a = g(s)
        if a:
            a['f']['text'] = _hoch(a['f']['text'])
            a['w'] = _hoch(a['w'])
            if 'a' in a: a['a'] = [_hoch(x) for x in a['a']]
        return a
    return f


GEN = {'nte_wurzel': g_nte_wurzel, 'potenz_wert': g_potenz_wert, 'umwandeln': g_umwandeln, 'zusammenfassen': g_zusammenfassen,
       'gleichung_exp': g_gleichung_exp, 'verstehen': g_verstehen}
GEN = {k: _schoen(v) for k, v in GEN.items()}

# ---------- Zehnte Runde (schwer-kl9): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Abschnitt mit eigenem festen Zufallsstart (anhaengen(..., 9903, ...)), läuft erst nach bauen():
# alle bisherigen Aufgaben bleiben unverändert. Vorbilder: Bayerischer Mathematik-Test 10 (ISB; Terme mit Potenzen
# und negativen/gebrochenen Exponenten ohne Taschenrechner vereinfachen, Schnittstellen zweier Potenzfunktionen
# durch Gleichsetzen), Illustrierende Aufgaben Realschule 9 (Behauptungen beurteilen). Zahlen und Wortlaut eigen.
from _schwer_kl9 import anhaengen  # noqa: E402


def schwer():
    P, K, O = 'pruefung', 'knobel', ''
    L = 'Zahlen in die Felder eintragen'
    return [
        # nte_wurzel
        ('nte_wurzel', 3, P, zahl('Berechne ohne Taschenrechner ⁴√0,0016 · ³√1 000.', '⁴√0,0016 = 0,2, denn 0,2⁴ = 0,0016. ³√1 000 = 10. Also 0,2 · 10 = 2.',
                                  'Ziehe beide Wurzeln einzeln. Tipp: 2⁴ = 16.', 2, '(0.0016 / 0.008) * (1000 / 100)')),
        ('nte_wurzel', 3, P, zahl('Berechne ohne Taschenrechner ⁵√(2⁵ · 3⁵).', '2⁵ · 3⁵ = (2 · 3)⁵ = 6⁵. Also ⁵√(6⁵) = 6. Man muss 7 776 gar nicht ausrechnen.',
                                  'Fasse 2⁵ · 3⁵ zu einer Potenz zusammen.', 6, '2 * 3')),
        ('nte_wurzel', 3, K, zahl('Für welche natürliche Zahl n gilt ⁿ√1 024 = 2?', 'Gesucht ist n mit 2ⁿ = 1 024. Verdoppeln: 2, 4, 8, …, 512, 1 024 – das ist 2¹⁰. Also n = 10.',
                                  'Rückwärts denken: Wie oft musst du 2 mit sich selbst malnehmen, um 1 024 zu erhalten?', 10, '5 * 2')),
        ('nte_wurzel', 3, O, zahl('Berechne ³√(√64).', 'Von innen nach außen: √64 = 8, dann ³√8 = 2. (Das ist die sechste Wurzel aus 64.)',
                                  'Rechne zuerst die innere Wurzel aus.', 2, '8 / 4')),
        ('nte_wurzel', 2, O, zahl('Berechne ⁴√10 000.', '10⁴ = 10 000, also ⁴√10 000 = 10.', 'Zähle die Nullen.', 10, '10000 / 1000')),
        ('nte_wurzel', 2, O, zahl('Berechne ³√0,027.', '0,3³ = 0,027, also ³√0,027 = 0,3.', 'Denke an 3³ = 27 und an die Nachkommastellen.', 0.3, '0.027 / 0.09')),
        # potenz_wert
        ('potenz_wert', 3, P, luecken('Berechne ohne Taschenrechner 8^(−2/3) + 4^(−1/2).', '□/□', 'Zähler und Nenner eintragen', [3, 4],
                                      '8^(−2/3) = 1/(³√8)² = 1/4 und 4^(−1/2) = 1/√4 = 1/2. Zusammen 1/4 + 2/4 = 3/4.',
                                      'Minus im Exponenten heißt Kehrwert. Berechne beide Summanden einzeln.', ['1 + 2', '4'])),
        ('potenz_wert', 3, P, zahl('Berechne ohne Taschenrechner 0,25^(−1/2).', '0,25^(1/2) = √0,25 = 0,5. Das Minus heißt Kehrwert: 1 : 0,5 = 2.',
                                   'Erst die Wurzel, dann den Kehrwert.', 2, '1 / 0.5')),
        ('potenz_wert', 3, K, auswahl('Welche Zahl ist größer: 2^(1/2) oder 3^(1/3)?', '3^(1/3)', ['2^(1/2)', 'Beide sind gleich groß.'],
                                      'Beide hoch 6 nehmen: (2^(1/2))⁶ = 2³ = 8 und (3^(1/3))⁶ = 3² = 9. Wegen 9 > 8 ist 3^(1/3) größer.',
                                      'Nimm beide Zahlen hoch 6 – dann verschwinden die Brüche im Exponenten.')),
        ('potenz_wert', 3, O, zahl('Berechne 0,001^(−2/3).', '0,001^(1/3) = 0,1. Hoch 2: 0,01. Kehrwert: 1 : 0,01 = 100.',
                                   'Nenner 3: dritte Wurzel, Zähler 2: quadrieren, Minus: Kehrwert.', 100, '1 / 0.1 ** 2')),
        ('potenz_wert', 2, O, zahl('Berechne 125^(2/3).', '³√125 = 5, dann 5² = 25.', 'Erst die dritte Wurzel, dann quadrieren.', 25, '(125 / 25) ** 2')),
        ('potenz_wert', 2, O, luecken('Berechne 9^(−1/2).', '□/□', 'Zähler und Nenner eintragen', [1, 3], '9^(−1/2) = 1/√9 = 1/3.',
                                      'Minus im Exponenten heißt Kehrwert.', ['1', '9 // 3'])),
        # umwandeln
        ('umwandeln', 3, P, luecken('Schreibe ³√(x⁶ · y³) für x, y ≥ 0 ohne Wurzelzeichen.', 'x^□ · y^□', L, [2, 1],
                                    '³√(x⁶ · y³) = x^(6/3) · y^(3/3) = x² · y.', 'Teile jeden Exponenten durch den Wurzelexponenten 3.', ['6 // 3', '3 // 3'])),
        ('umwandeln', 3, P, luecken('Schreibe 1/³√(x²) für x > 0 als Potenz.', 'x^(□/□)', L, [-2, 3],
                                    '³√(x²) = x^(2/3). Der Kehrwert hat ein Minus im Exponenten: x^(−2/3).', 'Erst die Wurzel als Potenz schreiben, dann der Kehrwert.', ['-2', '3'])),
        ('umwandeln', 3, K, auswahl('Welcher Term ist für x > 0 NICHT gleich x^(1/2)?', '√x · ⁴√x', ['⁴√(x²)', 'x : √x', '(x²)^(1/4)'],
                                    '√x · ⁴√x = x^(1/2 + 1/4) = x^(3/4). Die anderen: ⁴√(x²) = x^(2/4), x : √x = x^(1 − 1/2), (x²)^(1/4) = x^(2/4) – alle gleich x^(1/2).',
                                    'Schreibe jeden Term als Potenz von x und vergleiche die Exponenten.')),
        ('umwandeln', 3, O, luecken('Schreibe √(x · √x) für x ≥ 0 als Potenz.', 'x^(□/□)', L, [3, 4],
                                    'Innen: x · √x = x^(1 + 1/2) = x^(3/2). Außen: (x^(3/2))^(1/2) = x^(3/4).', 'Von innen nach außen umwandeln.', ['3', '4'])),
        ('umwandeln', 2, O, auswahl('Welcher Term ist gleich x^(3/5) für x ≥ 0?', '⁵√(x³)', ['³√(x⁵)', 'x³ : 5', '5 · √(x³)'],
                                    'Der Nenner 5 wird zum Wurzelexponenten, der Zähler 3 zum Exponenten unter der Wurzel.', 'Nenner = Wurzel, Zähler = Potenz.')),
        ('umwandeln', 2, O, luecken('Schreibe 1/x³ für x > 0 als Potenz.', 'x^□', 'den Exponenten eintragen', [-3],
                                    '1/x³ = x^(−3): Der Kehrwert hat ein Minus im Exponenten.', 'Kehrwert heißt Minus im Exponenten.', ['-3'])),
        # zusammenfassen
        ('zusammenfassen', 3, P, luecken('Vereinfache für x > 0: (x^(2/3))³ · √x.', 'x^(□/□)', L, [5, 2],
                                         '(x^(2/3))³ = x². Dann x² · x^(1/2) = x^(5/2).', 'Erst die Klammer potenzieren (Exponenten malnehmen), dann Exponenten addieren.', ['5', '2'])),
        ('zusammenfassen', 3, P, luecken('Vereinfache für x > 0: x⁴ : ³√x.', 'x^(□/□)', L, [11, 3],
                                         'x⁴ : x^(1/3) = x^(4 − 1/3) = x^(11/3).', 'Beim Teilen die Exponenten subtrahieren: 4 = 12/3.', ['12 - 1', '3'])),
        ('zusammenfassen', 3, K, zahl('Berechne 2^(1/3) · 4^(1/3).', 'Gleicher Exponent: 2^(1/3) · 4^(1/3) = (2 · 4)^(1/3) = 8^(1/3) = 2.',
                                      'Die Basen sind verschieden, aber die Exponenten gleich. Welches Potenzgesetz passt?', 2, '(2 * 4) / 4')),
        ('zusammenfassen', 3, O, zahl('Berechne 27^(1/2) · 3^(1/2).', '27^(1/2) · 3^(1/2) = (27 · 3)^(1/2) = √81 = 9.',
                                      'Gleiche Exponenten: Basen malnehmen.', 9, '(27 * 3) / 9')),
        ('zusammenfassen', 2, O, luecken('Fasse zu einer Potenz zusammen (x > 0): √x · √x · √x.', 'x^(□/□)', L, [3, 2],
                                         'x^(1/2 + 1/2 + 1/2) = x^(3/2).', 'Schreibe √x = x^(1/2) und addiere die Exponenten.', ['3', '2'])),
        ('zusammenfassen', 2, O, zahl('Berechne 5^(3/4) · 5^(1/4).', 'Exponenten addieren: 3/4 + 1/4 = 1, also 5¹ = 5.', 'Gleiche Basis: Exponenten addieren.', 5, '5 ** 1')),
        # gleichung_exp
        ('gleichung_exp', 3, P, zahl('Die Graphen von y = x^(1/2) und y = x/4 (x ≥ 0) schneiden sich bei x = 0 und an einer weiteren Stelle. Bei welchem x?',
                                     'Gleichsetzen: √x = x/4. Beide Seiten quadrieren: x = x²/16, also x² = 16x und (x ≠ 0) x = 16. Probe: √16 = 4 = 16/4.',
                                     'Setze die beiden Terme gleich und quadriere.', 16, '4 ** 2')),
        ('gleichung_exp', 3, P, zahl('Löse 5 · x^(2/3) − 3 = 17 für x > 0.', '5 · x^(2/3) = 20, also x^(2/3) = 4. Hoch 3/2: x = 4^(3/2) = (√4)³ = 8.',
                                     'Erst x^(2/3) allein stellen, dann mit dem Kehrwert 3/2 potenzieren.', 8, '(20 / 5) ** 3 / 8')),
        ('gleichung_exp', 3, K, zahl('Für welches x > 0 gilt x^(1/2) = 2 · x^(1/3)?', 'Durch x^(1/3) teilen: x^(1/2 − 1/3) = x^(1/6) = 2. Hoch 6: x = 2⁶ = 64. Probe: √64 = 8 = 2 · ³√64.',
                                     'Bringe alle x-Potenzen auf eine Seite (teilen) und fasse die Exponenten zusammen.', 64, '2 ** 6')),
        ('gleichung_exp', 3, O, zahl('Löse x^(−1/2) = 0,2 für x > 0.', 'x^(−1/2) = 1/√x = 0,2, also √x = 1 : 0,2 = 5 und x = 25.',
                                     'Das Minus heißt Kehrwert. Bestimme zuerst √x.', 25, '(1 / 0.2) ** 2')),
        ('gleichung_exp', 2, O, zahl('Löse x^(2/5) = 4 für x > 0.', 'Hoch 5/2: x = 4^(5/2) = (√4)⁵ = 2⁵ = 32.', 'Potenziere mit dem Kehrwert 5/2.', 32, '2 ** 5')),
        ('gleichung_exp', 2, O, zahl('Löse 2 · x^(1/2) = 14 für x > 0.', 'Durch 2 teilen: x^(1/2) = 7. Quadrieren: x = 49.', 'Erst x^(1/2) allein stellen, dann quadrieren.', 49, '(14 / 2) ** 2')),
        # verstehen
        ('verstehen', 3, P, auswahl('Jemand behauptet: „(a^(1/2))² = a gilt für jede reelle Zahl a.“ Was stimmt?',
                                    'Falsch: Für a < 0 ist a^(1/2) nicht definiert; die Aussage gilt nur für a ≥ 0.',
                                    ['Richtig: Hoch 1/2 und hoch 2 heben sich immer auf.', 'Falsch: Es kommt immer −a heraus.', 'Falsch: Es gilt nur für a > 1.'],
                                    'Bruch-Exponenten sind nur für Basen ≥ 0 erklärt. Gegenbeispiel a = −4: (−4)^(1/2) gibt es nicht. Für a ≥ 0 stimmt es, z. B. (9^(1/2))² = 3² = 9.',
                                    'Suche ein Gegenbeispiel mit einer negativen Zahl.')),
        ('verstehen', 3, P, auswahl('Welche Gleichung ist für x > 0 falsch?', 'x^(1/2) + x^(1/2) = x',
                                    ['x^(1/2) · x^(1/2) = x', 'x^(−1) = 1/x', '(x^(1/3))³ = x'],
                                    'x^(1/2) + x^(1/2) = 2√x, nicht x. Probe mit x = 4: 2 + 2 = 4 stimmt zufällig, aber mit x = 9: 3 + 3 = 6 ≠ 9.',
                                    'Prüfe jede Gleichung mit einer Zahl, z. B. x = 9.')),
        ('verstehen', 3, K, auswahl('Für welche Zahlen x > 0 gilt x^(1/2) > x?', 'für 0 < x < 1', ['für x > 1', 'für alle x > 0', 'für kein x'],
                                    'Beispiel x = 0,25: √0,25 = 0,5 > 0,25. Beispiel x = 4: √4 = 2 < 4. Bei x = 1 sind beide gleich. Die Wurzel ist nur zwischen 0 und 1 größer.',
                                    'Probiere je eine Zahl unter 1 und über 1.')),
        ('verstehen', 3, O, auswahl('Jemand rechnet 16^(−1/4) = −2. Was stimmt?', 'Falsch: 16^(−1/4) = 1/⁴√16 = 1/2.',
                                    ['Richtig, das Minus kommt vor das Ergebnis.', 'Falsch: 16^(−1/4) = −4.', 'Falsch: 16^(−1/4) = 1/4.'],
                                    'Ein Minus im Exponenten heißt Kehrwert: 16^(−1/4) = 1 : 16^(1/4) = 1 : 2 = 1/2. 1/4 wäre 16^(−1/2).',
                                    'Minus im Exponenten heißt Kehrwert, nicht negatives Ergebnis.')),
        ('verstehen', 2, O, auswahl('Welche Aussage gilt für x ≥ 0?', 'x^0,5 = √x', ['x^0,5 = x : 2', 'x^0,5 = 1/x²', 'x^0,5 = x − 0,5'],
                                    '0,5 = 1/2, und hoch 1/2 bedeutet Quadratwurzel.', 'Schreibe 0,5 als Bruch.')),
        ('verstehen', 2, O, auswahl('Welchen Wert hat 7^(−2)?', '1/49', ['−49', '−14', '49'],
                                    '7^(−2) = 1/7² = 1/49. Das Minus im Exponenten macht den Kehrwert, nicht eine negative Zahl.', 'Minus im Exponenten heißt Kehrwert.')),
    ]


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('zahlen.rationale_exponenten', 13_9_3)
# a) „Weg A / Weg B“ steht im selben Typ auf Stufe 2
BF.stufe('potenz_wert', '27^(4/3): Weg A: erst ³√27 = 3, dann 3⁴ = 81. Weg B: erst 27⁴ = 531 441, dann ³√531 441 = 81. Was stimmt?', 2)
# c) Lösung mit 9 Nachkommastellen: Eingabe unzumutbar → Lücke 1/□ wie bei 81^(−5/2)
BF.ersetze('potenz_wert', 'Berechne 64^(−3/2). Gib das Ergebnis als Dezimalzahl an.', BF.L(
    'Berechne 64^(−3/2). Gib das Ergebnis als Bruch an.', '1/□', [512], ['8 ** 3'],
    '64^(−3/2) = 1 / 64^(3/2) = 1 / (√64)³ = 1 / 8³ = 1/512.',
    'Negativer Exponent: Kehrwert bilden. Dann Wurzel (Nenner) und Potenz (Zähler).', hinweis='Nenner'))
# d) negative Lösung passt nicht zur Lernkarte „Gleichungen mit Bruch-Exponent (x > 0)“ → Gleichung mit Bruch-Exponent
BF.ersetze('gleichung_exp', 'Löse x⁵ = −243.', BF.Z(
    'Löse x^(5/3) = 243 für x > 0.', 27, '3 ** 3',
    'Beide Seiten hoch 3/5: x = 243^(3/5) = (⁵√243)³ = 3³ = 27. Probe: 27^(5/3) = (∛27)⁵ = 3⁵ = 243.',
    'Hoch den Kehrwert des Exponenten nehmen: (x^(5/3))^(3/5) = x.'))
# a) Grundaufgabe bzw. gleicher Typ wie Stufe 2
BF.stufe('gleichung_exp', 'Löse x^(1/2) = 6 für x > 0.', 2)
BF.stufe('verstehen', 'Welche Aussage gilt für x ≥ 0?', 2, enthaelt='x^(3/9) = x^(1/3)')

# ---- BEFUNDE ENDE ----


# ---------- Achtzehnte Runde, Teil B (Zweig luecken-kl9): Sachaufgaben (Modellieren) als Stufe-3-Gruppe ----------
# Lücke aus inhalte/pruefung/aufbau/klasse9.json: Sachaufgaben zu Potenzen mit rationalen Exponenten fehlten (Volumen ↔ Kantenlänge,
# Formeln aus Biologie und Physik). Eigener Zufallsstart, alles Alte bleibt unverändert.
from _luecken_kl9 import erweitern  # noqa: E402


def sach_exponenten():
    L = []

    def neu(l, a):
        a['l'] = l
        L.append(('uebung', 3, '', a))
    neu('nte_wurzel', zahl('Ein würfelförmiger Behälter fasst 512 cm³. Wie lang ist eine Kante?', 'Kante a mit a³ = 512, also a = ³√512 = 8 cm, denn 8 · 8 · 8 = 512.',
                           'Volumen eines Würfels: a³. Welche Zahl hoch 3 ergibt 512?', 8, '2 ** 3', einheit='cm'))
    neu('nte_wurzel', zahl('Ein Guthaben wächst in 4 Jahren auf das 1,4641-Fache, jedes Jahr mit demselben Faktor. Wie groß ist der Faktor pro Jahr?',
                           'Faktor q mit q⁴ = 1,4641, also q = ⁴√1,4641 = 1,1 (Probe: 1,1² = 1,21 und 1,21² = 1,4641). Das sind 10 % Zinsen pro Jahr.',
                           'Viermal derselbe Faktor: q · q · q · q = 1,4641.', Fr(11, 10), '11 / 10'))
    neu('potenz_wert', zahl('Für den Grundumsatz eines Säugetiers gilt etwa E = 70 · m^(3/4) (m in kg, E in kcal pro Tag). Berechne E für ein Tier mit 16 kg.',
                            '16^(3/4) = (⁴√16)³ = 2³ = 8. E = 70 · 8 = 560 kcal pro Tag.', 'm^(3/4) = (⁴√m)³. Rechne zuerst die vierte Wurzel.', 560, '70 * 2 ** 3',
                            einheit='kcal'))
    neu('gleichung_exp', zahl('Nach der Formel E = 70 · m^(3/4) hat ein Tier den Grundumsatz 1 890 kcal pro Tag. Wie schwer ist es (in kg)?',
                              '70 · m^(3/4) = 1 890 ⇒ m^(3/4) = 27 ⇒ m = 27^(4/3) = (³√27)⁴ = 3⁴ = 81 kg.',
                              'Teile zuerst durch 70. Dann hoch 4/3 nehmen.', 81, '3 ** 4', einheit='kg'))
    neu('potenz_wert', zahl('Für Planeten gilt näherungsweise a = T^(2/3) (T: Umlaufzeit in Jahren, a: Abstand zur Sonne in Erdabständen). Ein Planet braucht 8 Jahre. '
                            'Wie weit ist er von der Sonne entfernt (in Erdabständen)?', 'a = 8^(2/3) = (³√8)² = 2² = 4.', 'T^(2/3) = (³√T)².', 4, '2 ** 2'))
    neu('verstehen', auswahl('Ein Würfel soll das doppelte Volumen bekommen. Um wie viel Prozent wird seine Kante länger?', 'um etwa 26 %',
                             ['um 100 %', 'um 50 %', 'um etwa 41 %'],
                             'Neue Kante = alte Kante · ³√2 = alte Kante · 2^(1/3) ≈ alte Kante · 1,26, also etwa 26 % länger. 41 % gehört zu √2 (doppelte Fläche).',
                             'Das Volumen wächst mit der dritten Potenz der Kante. Welcher Faktor hoch 3 ergibt 2?'))
    return L

if __name__ == '__main__':
    d = bauen('zahlen.rationale_exponenten',
          'n-te Wurzeln berechnen, Wurzeln und Potenzen mit rationalen Exponenten ineinander umwandeln und zusammenfassen.',
          ['ⁿ√a (a ≥ 0) ist die nicht-negative Zahl b mit bⁿ = a.', 'a^(m/n) = ⁿ√(a^m) = (ⁿ√a)^m für a ≥ 0 (bei negativem Exponenten a > 0).',
           'a^(−q) = 1/a^q.', 'Potenzgesetze gelten auch für Bruch-Exponenten.'],
          [('n-te Wurzel', ['nte_wurzel', 'potenz_wert']), ('Umwandeln und Zusammenfassen', ['umwandeln', 'zusammenfassen']),
           ('Gleichungen und Verstehen', ['gleichung_exp', 'verstehen'])],
          ETAPPEN, GEN,
          meiden={'nte_wurzel': ['⁴√625.'], 'potenz_wert': ['27^(2/3).'], 'umwandeln': ['⁶√(x⁴)'], 'zusammenfassen': ['√x · ³√x.', 'x^(1/2) · x^(1/3).'],
                  'gleichung_exp': ['= 64 für'], 'verstehen': ['25^(−1/2)', '9^(1/2)']},
          offen=['Exponenten werden als Text „x^(2/3)“ geschrieben, weil die App keine Hochstellung von Brüchen kann. Falls eine Formel-Darstellung kommt, Texte umstellen.',
                 'Gleichungen xⁿ = c: Lösungsanzahl und negative Lösungen stehen ausführlich im Thema gleichungen.potenz; hier nur als Stufe-3-Aufgabe mit ungeradem n (Prüfvorschlag x³ = −125).'])
    anhaengen(d, 9903, schwer)
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    erweitern('zahlen.rationale_exponenten', None, 18_9_8, sach_exponenten)  # Achtzehnte Runde: Sachaufgaben (Stufe 3) an mehreren Karten


# ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl9) ----
from _durchsicht_kl9 import Befunde as _DSB, durchsicht  # noqa: E402

DS = _DSB('zahlen.rationale_exponenten', 19_9_10)
# nte_wurzel: Wurzel aus Brüchen und Rechenketten sind Stufe 2
for _t in ('Berechne ⁴√(1/16) als Dezimalzahl.', 'Berechne ⁵√(1/32) als Dezimalzahl.', 'Berechne ⁴√(1/625) als Dezimalzahl.', 'Berechne ⁶√(1/64) als Dezimalzahl.',
           'Berechne 5 · ⁴√81 − ⁵√243.', 'Berechne 4 · ³√27 − ⁵√32.'):
    DS.stufe('nte_wurzel', _t, 2)
# umwandeln: „Welcher Term ist gleich x^(m/n)?“ steht schon auf Stufe 2
for _t in ('Welcher Term ist gleich x^(7/6) für x ≥ 0?', 'Welcher Term ist gleich x^(5/2) für x ≥ 0?', 'Welcher Term ist gleich x^(7/4) für x ≥ 0?'):
    DS.stufe('umwandeln', _t, 2)
# zusammenfassen: Teilen von Wurzeln ist die Abwandlung des Beispiels (Stufe 2)
for _t in ('Fasse zu einer Potenz zusammen (x > 0): ⁴√x : √x.', 'Fasse zu einer Potenz zusammen (x > 0): ⁵√x : ³√x.'):
    DS.stufe('zusammenfassen', _t, 2)
# gleichung_exp: x^(1/n) = c ist Stufe 1, x^(m/n) = c wie im Beispiel Stufe 2
for _t in ('Löse x^(1/3) = 3 für x > 0.', 'Löse x^(1/2) = 5 für x > 0.', 'Löse x^(1/4) = 2 für x > 0.', 'Löse x^(1/4) = 3 für x > 0.', 'Löse x^(1/2) = 6 für x > 0.'):
    DS.stufe('gleichung_exp', _t, 1)
for _t in ('Löse x^(4/3) = 256 für x > 0.', 'Löse x^(5/3) = 243 für x > 0.'):
    DS.stufe('gleichung_exp', _t, 2)
# verstehen: Exponent kürzen ist Stufe 1; zwei der fünf gleichen Fehlerfinden auf Stufe 2
DS.stufe('verstehen', 'Welche Aussage gilt für x ≥ 0?', 1, anzahl=6)
for _t in ('Jemand rechnet 4^(3/2) = 4 · 3 : 2. Was ist richtig?', 'Jemand rechnet 32^(2/5) = 32 · 2 : 5. Was ist richtig?'):
    DS.stufe('verstehen', _t, 2)

if __name__ == '__main__':
    durchsicht('zahlen.rationale_exponenten', DS)


# ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl9) ----
from _stufen_kl9 import Stufen, stufen  # noqa: E402

ST = Stufen('zahlen.rationale_exponenten', 20_9_10)
Z, A, L = ST.Z, ST.A, ST.L
_B = '□/□'

# nte_wurzel
ST.stufenleiter('nte_wurzel', 'ⁿ√a für Potenzen natürlicher Zahlen angeben.',
                'Dezimalzahlen, Brüche, Potenzen unter der Wurzel, Rechenketten, a rückwärts, Würfel im Alltag.',
                'Produkte unter der Wurzel, verschachtelte Wurzeln, n suchen, Fehler „durch n teilen“, Wachstumsfaktor, mehrteilige Aufgabe.')
ST.typ('nte_wurzel', '/^Berechne [³⁴]√\\d+\\.$/', 'direkt')
ST.typ('nte_wurzel', 'Berechne ohne Taschenrechner', 'verknuepfen')
ST.typ('nte_wurzel', 'Berechne ³√(√', 'verknuepfen')
ST.typ('nte_wurzel', '/^Berechne/', 'mehrschritt')
ST.typ('nte_wurzel', 'Für welche natürliche Zahl n', 'parameter')
ST.typ('nte_wurzel', 'Ein würfelförmiger Behälter', 'einkleidung')
ST.typ('nte_wurzel', 'Ein Guthaben', 'transfer')
ST.neu('nte_wurzel', 'erkennen', A('Was bedeutet ⁵√32 = 2?', '2⁵ = 32', ['32 : 5 = 2', '2 · 5 = 32', '5² = 32'],
       'ⁿ√a = b heißt: b hoch n ergibt a. 2 · 2 · 2 · 2 · 2 = 32.', 'Lies die Wurzel rückwärts als Potenz.'))
ST.neu('nte_wurzel', 'umkehr', Z('Für welche Zahl a gilt ⁴√a = 3?', 81, '3 ** 4',
       'Rückwärts: a = 3⁴ = 3 · 3 · 3 · 3 = 81.', 'Rückwärts: hoch 4.'))
ST.neu('nte_wurzel', 'fehler', A('Jemand rechnet ⁴√16 = 4, weil 16 : 4 = 4. Was stimmt?', 'Falsch: ⁴√16 = 2, denn 2⁴ = 16.', ['Richtig.', 'Falsch: ⁴√16 = 8.', 'Falsch: ⁴√16 = 64.'],
       'Die vierte Wurzel sucht die Zahl, die viermal mit sich malgenommen 16 ergibt: 2 · 2 · 2 · 2. 4⁴ wäre 256.', 'Mach die Probe mit der Potenz.'))
ST.neu('nte_wurzel', 'begruenden', A('Stimmt: ⁶√64 = √(³√64)?', 'Ja, beide ergeben 2.', ['Nein, links 2, rechts 4.', 'Nein, links 8, rechts 2.', 'Nur ungefähr.'],
       '³√64 = 4 und √4 = 2. ⁶√64 = 2, denn 2⁶ = 64. Allgemein: Wurzelexponenten werden malgenommen.', 'Rechne innen zuerst.'))
ST.neu('nte_wurzel', 'pruefung', L('Berechne a) ³√125, b) ⁴√0,0001 als Bruch 1/□, c) ⁵√(1/32) als Bruch.', 'a) □; b) 1/□; c) □/□', [5, 10, 1, 2], ['5', '10', '1', '2'],
       'a) 5³ = 125. b) 0,1⁴ = 0,0001, also 1/10. c) (1/2)⁵ = 1/32.', 'Probiere einfache Zahlen.'))
ST.knobel('nte_wurzel', A('Welche Zahl ist größer: ⁵√5 oder ³√3?', '³√3', ['⁵√5', 'Beide sind gleich.', 'Das kann man nicht entscheiden.'],
          'Beide hoch 15 nehmen: (⁵√5)¹⁵ = 5³ = 125 und (³√3)¹⁵ = 3⁵ = 243. Wegen 243 > 125 ist ³√3 größer (≈ 1,442 gegen ≈ 1,380).',
          'Mit welcher Potenz verschwinden beide Wurzeln?'))
ST.knobel('nte_wurzel', Z('Für wie viele natürliche Zahlen n ≥ 1 ist ⁿ√(2¹²) eine natürliche Zahl?', 6, '6',
          'ⁿ√(2¹²) ist natürlich, wenn n ein Teiler von 12 ist: n = 1, 2, 3, 4, 6, 12. Dann ergibt sich 2^(12 : n). Für andere n nicht: Ist ⁿ√(2¹²) = m natürlich, dann ist mⁿ = 2¹². Dann hat m keinen anderen Primfaktor als 2, also m = 2^j und j · n = 12; n teilt 12. Also 6 Zahlen.',
          'Welche n teilen den Exponenten 12?'))

# potenz_wert
ST.stufenleiter('potenz_wert', 'a^(1/n) als n-te Wurzel ausrechnen.',
                'a^(m/n) über Wurzel und Potenz, zwei Rechenwege vergleichen, negative Exponenten, Basis rückwärts.',
                'Summen ohne Taschenrechner, Vergleich zweier Potenzen, Formeln aus Biologie und Astronomie, Fehler (16³)/4, Bedingung für n, mehrteilige Aufgabe.')
ST.typ('potenz_wert', 'Berechne 4^(1/2)', 'direkt')
ST.typ('potenz_wert', '/^Berechne \\d+\\^\\(1\\/\\d\\)\\.$/', 'direkt')
ST.typ('potenz_wert', '/Weg A/', 'darstellung')
ST.typ('potenz_wert', 'Berechne ohne Taschenrechner', 'verknuepfen')
ST.typ('potenz_wert', '/^Berechne [\\d,]+\\^\\(−?\\d\\/\\d\\)/', 'mehrschritt')
ST.typ('potenz_wert', 'Welche Zahl ist größer', 'begruenden')
ST.typ('potenz_wert', '/^(Für den Grundumsatz|Für Planeten)/', 'transfer')
ST.neu('potenz_wert', 'erkennen', A('Was bedeutet der Nenner 3 im Exponenten von 8^(2/3)?', 'Ziehe die dritte Wurzel.', ['Teile durch 3.', 'Nimm mal 3.', 'Nimm hoch 3.'],
       'Nenner = Wurzel, Zähler = Potenz: 8^(2/3) = (³√8)² = 4.', 'Hoch 1/3 heißt dritte Wurzel.'))
ST.neu('potenz_wert', 'erkennen', A('Welcher Term ist gleich 9^(1/2)?', '√9', ['9 : 2', '9²', '1/9'],
       'Hoch 1/2 heißt Quadratwurzel: 9^(1/2) = √9 = 3.', 'Was bedeutet der Nenner 2?'))
ST.neu('potenz_wert', 'umkehr', Z('Für welche Zahl a gilt a^(1/2) = 7?', 49, '7 ** 2',
       'a^(1/2) = √a = 7, also a = 49.', 'Rückwärts: quadrieren.'))
ST.neu('potenz_wert', 'fehler', A('Jemand rechnet 16^(3/4) = 16³ : 4 = 1 024. Was stimmt?', 'Falsch: Der Nenner 4 heißt vierte Wurzel: (⁴√16)³ = 2³ = 8.', ['Richtig.', 'Falsch: 16^(3/4) = 12.', 'Falsch: 16^(3/4) = 64.'],
       'Nicht durch 4 teilen, sondern die vierte Wurzel ziehen: ⁴√16 = 2, dann hoch 3.', 'Was bedeutet der Nenner?'))
ST.neu('potenz_wert', 'parameter', Z('Für wie viele natürliche Zahlen n ≥ 1 ist 64^(1/n) eine natürliche Zahl?', 4, '4',
       '64 = 2⁶. 64^(1/n) = 2^(6 : n) ist natürlich für n = 1, 2, 3, 6 (Ergebnisse 64, 8, 4, 2). Für n = 4 und n = 5 liegt das Ergebnis zwischen 2 und 3 (2⁴ = 16 < 64 < 81 = 3⁴, 2⁵ = 32 < 64 < 243 = 3⁵), für n ≥ 7 zwischen 1 und 2 (2⁷ = 128 > 64). Also 4 Zahlen.', 'Schreibe 64 als Zweierpotenz.'))
ST.neu('potenz_wert', 'pruefung', L('Berechne a) 25^(1/2), b) 27^(2/3), c) 16^(−1/4) als Bruch 1/□.', 'a) □; b) □; c) 1/□', [5, 9, 2], ['5', '3 ** 2', '2'],
       'a) √25 = 5. b) (³√27)² = 3² = 9. c) 1 : ⁴√16 = 1/2.', 'Nenner = Wurzel, Zähler = Potenz, Minus = Kehrwert.'))
ST.knobel('potenz_wert', Z('Berechne (2^(1/2) · 8^(1/2))^(1/2).', 2, '2',
          'Innen: 2^(1/2) · 8^(1/2) = (2 · 8)^(1/2) = 16^(1/2) = 4. Dann 4^(1/2) = 2.', 'Fasse innen zuerst zusammen.'))
ST.knobel('potenz_wert', A('Welche Zahl ist am kleinsten: 2^(1/2), 3^(1/3) oder 6^(1/6)?', '6^(1/6)', ['2^(1/2)', '3^(1/3)', 'alle gleich'],
          'Alle hoch 6: 2³ = 8, 3² = 9, 6¹ = 6. Am kleinsten ist 6, also 6^(1/6) ≈ 1,35.', 'Mit welcher Potenz verschwinden alle Brüche im Exponenten?'))

# umwandeln
ST.stufenleiter('umwandeln', 'ⁿ√(x^m) als x^(m/n) schreiben.',
                'Exponenten kürzen, rückwärts in eine Wurzel übersetzen, Kehrwerte als negative Exponenten, Formeln umschreiben.',
                'Mehrere Variablen, verschachtelte Wurzeln, Fehler „Zähler und Nenner vertauscht“, n gesucht, Oberfläche als Potenz von V, mehrteilige Aufgabe.')
ST.typ('umwandeln', '/^Schreibe [²³⁴⁵⁶⁷⁸⁹]?√\\(?x[²³⁴⁵⁶⁷⁸⁹]*\\)? \\(x ≥ 0\\) als Potenz( mit Bruch-Exponent)?\\.$/', 'direkt')
ST.typ('umwandeln', 'Welcher Term ist gleich', 'umkehr')
ST.typ('umwandeln', '/^(Schreibe ³√\\(x⁶|Schreibe 1\\/³√|Schreibe √\\(x)/', 'verknuepfen')
ST.typ('umwandeln', '/^Schreibe 1\\/[⁶⁸]?√x/', 'mehrschritt')
ST.typ('umwandeln', '/^(Schreibe ¹?[⁰¹²³⁴⁵⁶⁷⁸⁹]?√|Schreibe 1\\/x³)/', 'mehrschritt')
ST.typ('umwandeln', 'Welcher Term ist für x > 0 NICHT', 'begruenden')
ST.neu('umwandeln', 'erkennen', A('Welcher Exponent gehört zu ⁵√x?', '1/5', ['5', '−5', '5/2'],
       '⁵√x = x^(1/5): Der Wurzelexponent wird Nenner.', 'Wohin kommt der Wurzelexponent?'))
ST.neu('umwandeln', 'einkleidung', L('Für die Kante eines Würfels gilt a = ³√V. Schreibe das als Potenz von V.', 'a = V^(□/□)', [1, 3], ['1', '3'],
       'Der Wurzelexponent 3 wird Nenner: ³√V = V^(1/3).', 'Wurzelexponent in den Nenner.'))
ST.neu('umwandeln', 'fehler', A('Jemand schreibt ⁵√(x²) = x^(5/2). Was stimmt?', 'Falsch: x^(2/5); der Wurzelexponent gehört in den Nenner.', ['Richtig.', 'Falsch: x^(10).', 'Falsch: x^(2/10).'],
       'ⁿ√(x^m) = x^(m/n): hier m = 2, n = 5.', 'Was steht im Nenner?'))
ST.neu('umwandeln', 'parameter', Z('Für welche natürliche Zahl n gilt ⁿ√(x⁶) = x² für alle x > 0?', 3, '6 // 2',
       'ⁿ√(x⁶) = x^(6/n) = x² heißt 6 : n = 2, also n = 3.', 'Schreibe die Wurzel als Potenz.'))
ST.neu('umwandeln', 'transfer', L('Für einen Würfel gilt a = V^(1/3). Schreibe seine Oberfläche O = 6a² als Term in V.', 'O = 6 · V^(□/□)', [2, 3], ['2', '3'],
       'a² = (V^(1/3))² = V^(2/3). Also O = 6 · V^(2/3).', 'Setze a ein und rechne mit Potenzgesetzen.'))
ST.neu('umwandeln', 'pruefung', L('a) ⁴√(x³) = x^(□/□); b) x^(−1/2) = 1/ⁿ√x mit n = □; c) √x · x = x^(□/□) (x > 0).', 'a) □/□; b) □; c) □/□', [3, 4, 2, 3, 2],
       ['3', '4', '2', '3', '2'], 'a) x^(3/4). b) x^(−1/2) = 1/√x, also n = 2. c) x^(1/2 + 1) = x^(3/2).', 'Wurzelexponent in den Nenner, Minus heißt Kehrwert.'))
ST.knobel('umwandeln', L('Schreibe √(x · √(x · √x)) für x > 0 als Potenz von x.', 'x^(□/□)', [7, 8], ['7', '8'],
          'Von innen: x · √x = x^(3/2). √ davon: x^(3/4). Mal x: x^(7/4). √ davon: x^(7/8).', 'Arbeite dich von innen nach außen.'))
ST.knobel('umwandeln', Z('Berechne ⁴√(⁴√(2³²)).', 4, '2 ** 2',
          'Zweimal die vierte Wurzel ist die 16. Wurzel: 2^(32/16) = 2² = 4.', 'Schreibe jede Wurzel als Potenz.'))

# zusammenfassen
ST.stufenleiter('zusammenfassen', 'x^(a) · x^(b) zu x^(a + b) zusammenfassen.',
                'Teilen, gleiche Exponenten bei verschiedenen Basen, Wurzeln vorher umschreiben, fehlenden Exponenten ergänzen.',
                'Potenzen von Potenzen, Fehler beim Malnehmen der Exponenten, Aussagen prüfen, Exponent r gesucht, rückwärts ergänzen, mehrteilige Aufgabe.')
ST.typ('zusammenfassen', '/^Fasse zu einer Potenz zusammen \\(x > 0\\): x\\^\\(\\d\\/\\d\\) · /', 'direkt', s=1)
ST.typ('zusammenfassen', '/^(Vereinfache|Berechne \\d+\\^\\(1\\/\\d\\) · \\d+\\^)/', 'verknuepfen', s=3)
ST.typ('zusammenfassen', '/^(Fasse|Berechne)/', 'mehrschritt')
ST.neu('zusammenfassen', 'erkennen', A('Welches Gesetz gilt für x^(1/2) · x^(1/3)?', 'Exponenten addieren: x^(5/6)', ['Exponenten malnehmen: x^(1/6)', 'Basen malnehmen: x²^(5/6)', 'Exponenten subtrahieren'],
       'Gleiche Basis, malnehmen: Exponenten addieren. 1/2 + 1/3 = 5/6.', 'Wie bei x² · x³.'))
ST.neu('zusammenfassen', 'direkt', L('Schreibe x^(1/3) · x^(1/3) als eine Potenz (x > 0).', 'x^(□/□)', [2, 3], ['2', '3'],
       '1/3 + 1/3 = 2/3.', 'Exponenten addieren.'))
ST.neu('zusammenfassen', 'umkehr', L('Ergänze: x^(1/2) · x^(□/□) = x (x > 0).', '□/□', [1, 2], ['1', '2'],
       'x = x¹. 1 − 1/2 = 1/2.', 'Welcher Exponent fehlt bis 1?'))
ST.neu('zusammenfassen', 'darstellung', A('Welche Wurzel ist gleich x^(1/2) · x^(1/4) (x > 0)?', '⁴√(x³)', ['⁸√x', '⁴√x', '√(x³)'],
       '1/2 + 1/4 = 3/4, und x^(3/4) = ⁴√(x³).', 'Erst zusammenfassen, dann in eine Wurzel übersetzen.'))
ST.neu('zusammenfassen', 'fehler', A('Jemand rechnet (x^(1/2))^(1/3) = x^(5/6). Was stimmt?', 'Falsch: Potenz einer Potenz heißt Exponenten malnehmen: x^(1/6).', ['Richtig.', 'Falsch: x^(2/3).', 'Falsch: x^(3/2).'],
       '(x^p)^q = x^(p · q) = x^(1/6). Addiert wird nur bei x^p · x^q.', 'Malnehmen oder addieren?'))
ST.neu('zusammenfassen', 'begruenden', A('Stimmt: √x · ³√x · ⁶√x = x für x > 0?', 'Ja, denn 1/2 + 1/3 + 1/6 = 1.', ['Nein, das ergibt x^(1/6).', 'Nein, das ergibt x^(1/36).', 'Nur für x = 1.'],
       'Exponenten addieren: 3/6 + 2/6 + 1/6 = 6/6 = 1. Also x¹ = x.', 'Schreibe alle Wurzeln als Potenzen.'))
ST.neu('zusammenfassen', 'parameter', L('Für welche Zahl r gilt x^r · x^(1/4) = √x (x > 0)?', 'r = □/□', [1, 4], ['1', '4'],
       '√x = x^(1/2). r + 1/4 = 1/2, also r = 1/4.', 'Schreibe √x als Potenz.'))
ST.neu('zusammenfassen', 'rueckwaerts', L('Ergänze: x^(5/6) : x^(□/□) = x^(1/2) (x > 0).', '□/□', [1, 3], ['1', '3'],
       '5/6 − r = 1/2 = 3/6, also r = 2/6 = 1/3.', 'Beim Teilen werden Exponenten subtrahiert.'))
ST.neu('zusammenfassen', 'pruefung', L('a) √x · ⁴√x = x^(□/□); b) x : ³√x = x^(□/□); c) 8^(1/3) · 8^(1/3) = □.', 'a) □/□; b) □/□; c) □', [3, 4, 2, 3, 4], ['3', '4', '2', '3', '2 * 2'],
       'a) 1/2 + 1/4 = 3/4. b) 1 − 1/3 = 2/3. c) 8^(2/3) = 4.', 'Wurzeln zuerst als Potenzen schreiben.'))
ST.knobel('zusammenfassen', Z('Berechne 2^(1/2) · 2^(1/4) · 2^(1/8) · 2^(1/8).', 2, '2',
          'Exponenten addieren: 1/2 + 1/4 + 1/8 + 1/8 = 4/8 + 2/8 + 1/8 + 1/8 = 1. Ergebnis 2¹ = 2.', 'Addiere die Exponenten mit gemeinsamem Nenner.'))
ST.knobel('zusammenfassen', Z('Für welches x > 0 gilt √x · ³√x = 32?', 64, '2 ** 6',
          'x^(1/2 + 1/3) = x^(5/6) = 32 = 2⁵. Also x^(1/6) = 2 und x = 2⁶ = 64. Probe: √64 · ³√64 = 8 · 4 = 32.', 'Fasse links zusammen und schreibe 32 als Potenz.'))

# gleichung_exp
ST.stufenleiter('gleichung_exp', 'xⁿ = c oder x^(1/n) = c in einem Schritt lösen.',
                'x^(m/n) = c mit dem Kehrwert lösen, vorher umformen, c rückwärts, Seitenlänge aus Fläche.',
                'Schnittpunkte, zwei Potenzen in einer Gleichung, negative Exponenten, Fehler „Wurzel statt Quadrat“, Lösbarkeit begründen, Formeln rückwärts.')
ST.typ('gleichung_exp', '/^Löse x(\\^\\(1\\/\\d\\)|[²³⁴⁵]) = \\d+ für x > 0\\.$/', 'direkt')
ST.typ('gleichung_exp', '/^Löse (x\\^\\(\\d\\/\\d\\)|\\d · x\\^|5 · x)/', 'mehrschritt')
ST.typ('gleichung_exp', '/^(Die Graphen|Für welches x|Löse x\\^\\(−)/', 'verknuepfen')
ST.typ('gleichung_exp', 'Nach der Formel', 'transfer')
ST.neu('gleichung_exp', 'erkennen', A('Womit potenzierst du bei x^(3/4) = 8 beide Seiten?', 'mit 4/3', ['mit 3/4', 'mit −3/4', 'mit 4'],
       'Der Kehrwert hebt den Exponenten auf: (x^(3/4))^(4/3) = x.', 'Denk an den Kehrwert.'))
ST.neu('gleichung_exp', 'einkleidung', Z('Für die Seite eines Quadrats gilt a = A^(1/2). Die Seite ist 1,2 m lang. Wie groß ist A?', 1.44, '1.2 ** 2',
       'A^(1/2) = 1,2 ⇒ A = 1,2² = 1,44 m².', 'Quadriere beide Seiten.', einheit='m²'))
ST.neu('gleichung_exp', 'umkehr', Z('Für welche Zahl c hat x^(2/3) = c die Lösung x = 27?', 9, '3 ** 2',
       'c = 27^(2/3) = (³√27)² = 9.', 'Setze 27 ein.'))
ST.neu('gleichung_exp', 'fehler', A('Jemand löst x^(1/2) = 9 mit x = 3. Was stimmt?', 'Falsch: Quadrieren ergibt x = 81.', ['Richtig.', 'Falsch: x = 4,5.', 'Falsch: x = 18.'],
       'x^(1/2) = √x = 9 heißt x = 9² = 81. Probe: √81 = 9. Mit x = 3 wäre √3 ≈ 1,73.', 'Mach die Probe.'))
ST.neu('gleichung_exp', 'begruenden', A('Hat x^(1/2) = −3 eine Lösung (x ≥ 0)?', 'Nein, x^(1/2) = √x ist nie negativ.', ['Ja, x = 9.', 'Ja, x = −9.', 'Ja, x = −1,5.'],
       'Für x ≥ 0 ist √x ≥ 0. Eine negative Zahl kann nie herauskommen. Quadrieren würde die Scheinlösung 9 liefern: √9 = 3 ≠ −3.', 'Kann eine Quadratwurzel negativ sein?'))
ST.neu('gleichung_exp', 'parameter', Z('Für welche positive Zahl k haben x^(1/2) = k und x^(1/3) = k dieselbe Lösung x?', 1, '1',
       'Dieselbe Lösung heißt x^(1/2) = x^(1/3). Beide Seiten hoch 6: x³ = x². Für x > 0 durch x² teilen: x = 1. Also k = 1^(1/2) = 1.', 'Wann sind Quadrat- und Kubikwurzel gleich?'))
ST.neu('gleichung_exp', 'pruefung', L('Löse für x > 0: a) x^(1/4) = 2, b) x^(3/2) = 27, c) 4 · x^(1/3) = 20.', 'a) □; b) □; c) □', [16, 9, 125], ['2 ** 4', '3 ** 2', '5 ** 3'],
       'a) x = 2⁴ = 16. b) x = 27^(2/3) = 9. c) x^(1/3) = 5, x = 125.', 'Mit dem Kehrwert des Exponenten potenzieren.'))
ST.knobel('gleichung_exp', Z('Löse x^(1/2) + x^(1/4) = 6 für x > 0.', 16, '2 ** 4',
          'Es gilt x^(1/2) = (x^(1/4))². Gesucht ist also eine positive Zahl x^(1/4), deren Quadrat plus sie selbst 6 ergibt: 2² + 2 = 6. Also x^(1/4) = 2 und x = 2⁴ = 16. Es gibt keine andere Lösung: Wird x größer, werden beide Summanden größer, wird x kleiner, beide kleiner. Probe: √16 + ⁴√16 = 4 + 2 = 6.',
          'Schreibe x^(1/2) als Quadrat von x^(1/4).'))
ST.knobel('gleichung_exp', Z('Für die Oberfläche eines Würfels gilt O = 6 · V^(2/3) (O in cm², V in cm³). Für welches Volumen ist O = 54 cm²?', 27, '3 ** 3',
          'V^(2/3) = 9 ⇒ V = 9^(3/2) = (√9)³ = 27 cm³. Probe: Kante 3 cm, Oberfläche 6 · 9 = 54 cm².', 'Teile zuerst durch 6.', einheit='cm³'))

# verstehen
ST.stufenleiter('verstehen', 'Hoch 1/2 als Wurzel und Minus im Exponenten als Kehrwert erkennen.',
                'Negative Bruch-Exponenten ausrechnen, Basis rückwärts, Schreibweisen wechseln, Wachstum in Viertelstunden.',
                'Fehler „hoch 3/2 ist mal 3 : 2“, Allaussagen prüfen, falsche Gleichungen finden, Vergleich mit x, Würfelkante bei doppeltem Volumen, mehrteilige Aufgabe.')
ST.typ('verstehen', '/^Jemand rechnet \\d+\\^\\(1\\/2\\)/', 'erkennen')
ST.typ('verstehen', '/^(Was ist \\d+\\^\\(−1\\/2\\)\\?|Welche Aussage gilt|Ist \\(−32\\))/', 'erkennen', s=1)
ST.typ('verstehen', 'Ist (−32)', 'erkennen')
ST.typ('verstehen', '/^(Was ist|Welchen Wert hat)/', 'mehrschritt')
ST.typ('verstehen', '/^Jemand rechnet \\d+\\^\\(\\d\\/\\d\\) = /', 'fehler')
ST.typ('verstehen', 'Jemand rechnet 16^(−1/4)', 'fehler')
ST.typ('verstehen', 'Jemand behauptet', 'begruenden')
ST.typ('verstehen', 'Welche Gleichung', 'verknuepfen')
ST.typ('verstehen', 'Für welche Zahlen x', 'parameter')
ST.typ('verstehen', 'Ein Würfel soll', 'transfer')
ST.neu('verstehen', 'direkt', L('Berechne 36^(−1/2) als Bruch.', _B, [1, 6], ['1', '6'],
       'Minus heißt Kehrwert: 1 : 36^(1/2) = 1 : 6 = 1/6.', 'Erst die Wurzel, dann der Kehrwert.'))
ST.neu('verstehen', 'einkleidung', Z('Für die Kante eines Würfels gilt a = V^(1/3). Ein Würfel hat 125 cm³ Volumen. Wie lang ist seine Kante?', 5, '5',
       'a = 125^(1/3) = ³√125 = 5 cm, denn 5 · 5 · 5 = 125.', 'Hoch 1/3 heißt dritte Wurzel.', einheit='cm'))
ST.neu('verstehen', 'umkehr', Z('Für welche Basis a > 0 gilt a^(−1/2) = 1/5?', 25, '5 ** 2',
       'a^(−1/2) = 1/√a = 1/5, also √a = 5 und a = 25.', 'Kehrwert auf beiden Seiten.'))
ST.neu('verstehen', 'darstellung', A('Welche Schreibweise ist gleich 1/√x (x > 0)?', 'x^(−1/2)', ['x^(1/2)', 'x^(−2)', '−x^(1/2)'],
       '√x = x^(1/2), Kehrwert: x^(−1/2).', 'Minus im Exponenten heißt Kehrwert.'))
ST.neu('verstehen', 'mehrschritt', L('Berechne 4^(−3/2) als Bruch.', _B, [1, 8], ['1', '8'],
       '4^(3/2) = (√4)³ = 8. Kehrwert: 1/8.', 'Erst 4^(3/2), dann der Kehrwert.'))
ST.neu('verstehen', 'pruefung', L('Berechne a) 27^(−1/3) = 1/□, b) 0,01^(1/2) = 1/□, c) 32^(2/5) = □.', 'a) 1/□; b) 1/□; c) □', [3, 10, 4], ['3', '10', '2 ** 2'],
       'a) 1 : ³√27 = 1/3. b) √0,01 = 0,1 = 1/10. c) (⁵√32)² = 2² = 4.', 'Nenner = Wurzel, Minus = Kehrwert.'))
ST.knobel('verstehen', A('Welche Zahl ist größer: 2^(−1/2) oder 3^(−1/3)?', '2^(−1/2)', ['3^(−1/3)', 'Beide sind gleich.', 'Das kann man nicht entscheiden.'],
          'Kehrwerte: 2^(−1/2) = 1/2^(1/2) und 3^(−1/3) = 1/3^(1/3). Hoch 6: 2^(1/2) → 8, 3^(1/3) → 9, also 2^(1/2) < 3^(1/3). Beim Kehrwert dreht sich der Vergleich um: 2^(−1/2) ist größer.',
          'Vergleiche erst die Zahlen ohne Minus im Exponenten.'))
ST.knobel('verstehen', Z('Berechne (1/27)^(−2/3).', 9, '3 ** 2',
          'Minus heißt Kehrwert: (1/27)^(−2/3) = 27^(2/3). Dann (³√27)² = 3² = 9.', 'Zwei Fallen: das Minus und der Bruch als Basis.'))

if __name__ == '__main__':
    stufen('zahlen.rationale_exponenten', ST)
