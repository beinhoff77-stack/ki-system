#!/usr/bin/env python3
"""Thema gleichungen.lgs2 – Lineare Gleichungssysteme mit 2 Unbekannten (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, L, Z, baue, cz, einsetzen, eur, kl, lin, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'gleichungen.lgs2', 'thema_id': 6, 'block_id': 59, 'klasse': {'gym_by': 8, 'rs_by': 9}}

ETAPPEN = [
    {'lernziel': 'pruefen', 'titel': 'Ist das Zahlenpaar eine Lösung?',
     'regel': 'Ein Zahlenpaar (x | y) ist ⟦Lösung⟧ des Gleichungssystems, wenn es ⟦beide⟧ Gleichungen erfüllt. Prüfe durch Einsetzen in I und in II.',
     'schritte': ['I: x + y = 5   II: 2x − y = 1   Paar (2 | 3)', 'I: 2 + 3 = 5 ✓   II: 4 − 3 = 1 ✓', '⟦(2 | 3) ist Lösung.⟧'],
     'fehler': 'Erfüllt (4 | 1) nur x + y = 5, ist es ⟦keine⟧ Lösung des Systems: In II gilt 8 − 1 = 7 ≠ 1. Beide Gleichungen müssen stimmen.',
     '_verbot': ['x + y = 5']},
    {'lernziel': 'grafisch', 'titel': 'Gleichungssystem grafisch lösen',
     'regel': 'Jede lineare Gleichung mit x und y beschreibt eine ⟦Gerade⟧. Ein Punkt auf der Geraden erfüllt die Gleichung. Der ⟦Schnittpunkt⟧ liegt auf beiden Geraden – er ist die Lösung des Systems.',
     'schritte': ['I: x + y = 5 umstellen zu y = −x + 5. II: 2x − y = 1 umstellen zu y = 2x − 1.', 'Beide Geraden zeichnen. Sie schneiden sich in S(2 | 3).', '⟦L = {(2 | 3)}⟧'],
     'probe': 'I: 2 + 3 = 5 ✓   II: 4 − 3 = 1 ✓',
     'fehler': 'Ungenau ablesen und nicht prüfen. Liegt der Schnittpunkt zwischen den Kästchen, ist abgelesen nur eine Schätzung. Setze das Paar ⟦immer in beide Gleichungen⟧ ein; stimmt es nicht genau, rechne mit einem Verfahren.',
     'bild': {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-2, 6], 'graphen': [{'art': 'linear', 'm': -1, 't': 5, 'name': 'I'}, {'art': 'linear', 'm': 2, 't': -1, 'name': 'II'}],
              'punkte': [{'x': 2, 'y': 3, 'name': 'S(2 | 3)'}]}},
    {'lernziel': 'einsetzen', 'titel': 'Einsetzungsverfahren',
     'regel': 'Ist eine Gleichung nach einer Variablen aufgelöst (z. B. y = …), ⟦setzt du diesen Term⟧ in die andere Gleichung ein. Dann bleibt eine Gleichung mit nur einer Variablen.',
     'schritte': ['I: y = 2x − 1   II: 3x + y = 9', 'I in II: 3x + (2x − 1) = 9 → 5x = 10 → x = 2', 'x in I: y = 2 · 2 − 1 = 3. ⟦L = {(2 | 3)}⟧'],
     'fehler': 'Beim Einsetzen die ⟦Klammer⟧ nicht vergessen: 3x − (2x − 1) ist 3x − 2x + 1, nicht 3x − 2x − 1.',
     '_verbot': ['y = 2x − 1']},
    {'lernziel': 'gleichsetzen', 'titel': 'Gleichsetzungsverfahren',
     'regel': 'Sind ⟦beide⟧ Gleichungen nach derselben Variablen aufgelöst, setzt du die rechten Seiten ⟦gleich⟧. Das ist die Frage: Für welches x sind beide y-Werte gleich?',
     'schritte': ['Fahrradverleih A: y = 2x + 10, Verleih B: y = 4x + 4 (x Stunden, y Preis in €). Wann kosten beide gleich viel?',
                  'Gleichsetzen: 2x + 10 = 4x + 4 → 6 = 2x → x = 3.', 'y = 2 · 3 + 10 = 16. ⟦L = {(3 | 16)}⟧: Bei 3 Stunden kosten beide 16 €.'],
     'probe': 'B: 4 · 3 + 4 = 16 ✓',
     'fehler': 'Mit x = 3 ist die Aufgabe nicht fertig: Die Lösung ist ein ⟦Zahlenpaar⟧. Setze x noch ein, um y zu bestimmen – sonst weißt du nicht, wie viel die 3 Stunden kosten.',
     '_verbot': ['y = 2x + 10']},
    {'lernziel': 'addition', 'titel': 'Additionsverfahren',
     'regel': 'Stell dir zwei Waagen im Gleichgewicht vor. Legst du den Inhalt beider linken Schalen zusammen und den beider rechten auch, bleibt es im Gleichgewicht. Deshalb darfst du ⟦Gleichungen addieren⟧. Multipliziere vorher so, dass vor einer Variablen ⟦Gegenzahlen⟧ stehen – dann ⟦fällt sie weg⟧.',
     'schritte': ['I: 2x + 3y = 12   II: x − y = 1', 'II · 3 ergibt II′: 3x − 3y = 3. Jetzt stehen +3y und −3y da.', 'I + II′: 5x = 15 → x = 3. In II: 3 − y = 1 → y = 2. ⟦L = {(3 | 2)}⟧'],
     'probe': 'I: 6 + 6 = 12 ✓   II: 3 − 2 = 1 ✓',
     'fehler': 'Wer II mit 3 multipliziert, muss ⟦jedes⟧ Glied multiplizieren – auch die rechte Seite: 3x − 3y = 3, nicht 3x − 3y = 1.',
     '_verbot': ['2x + 3y = 12']},
    {'lernziel': 'verfahren', 'titel': 'Welches Verfahren ist geschickt?',
     'regel': 'Alle Verfahren führen zum Ziel. ⟦Gleichsetzen⟧, wenn beide Gleichungen nach derselben Variablen aufgelöst sind. ⟦Einsetzen⟧, wenn eine aufgelöst ist. ⟦Addition⟧, wenn vor einer Variablen Gegenzahlen oder Vielfache stehen.',
     'schritte': ['I: 4x + 5y = 3   II: 2x − 5y = 9', 'Vor y stehen 5 und −5: Gegenzahlen.', 'Am geschicktesten: ⟦Additionsverfahren⟧.'],
     'fehler': 'Bei I: y = 3x und II: y = x + 4 musst du nichts umstellen. Hier erst nach x aufzulösen kostet ⟦unnötige⟧ Schritte – gleichsetzen ist schneller.',
     '_verbot': ['4x + 5y = 3']},
    {'lernziel': 'loesbarkeit', 'titel': 'Wie viele Lösungen hat das System?',
     'regel': 'Jede Gleichung ist eine Gerade, die Lösung ist ihr Schnittpunkt. Fällt beim Rechnen ⟦x und y⟧ weg, entscheidet die Rest-Aussage: ⟦falsch⟧ (z. B. 1 = −3) heißt keine Lösung – die Geraden sind parallel. ⟦Wahr⟧ (z. B. 0 = 0) heißt unendlich viele Lösungen – beide Gleichungen beschreiben dieselbe Gerade.',
     'schritte': ['I: y = 2x + 1   II: y = 2x − 3', 'Gleichsetzen: 2x + 1 = 2x − 3 → 1 = −3', 'Falsche Aussage: ⟦keine Lösung⟧ (parallele Geraden).'],
     'fehler': 'Bei 0 = 0 ist nicht „x = 0“ die Lösung. Die Aussage ist ⟦immer⟧ wahr: Jedes Paar, das eine Gleichung erfüllt, erfüllt auch die andere – unendlich viele Lösungen.',
     'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-5, 5], 'graphen': [{'art': 'linear', 'm': 2, 't': 1, 'name': 'I'}, {'art': 'linear', 'm': 2, 't': -3, 'name': 'II'}]},
     '_verbot': ['y = 2x + 1']},
    {'lernziel': 'sachaufgabe', 'titel': 'Sachaufgaben mit zwei Unbekannten',
     'regel': 'Lege für die beiden gesuchten Größen ⟦Variablen⟧ fest (x, y). Übersetze jede Information in ⟦eine Gleichung⟧, löse das System und antworte im Satz.',
     'schritte': ['In einem Stall sind Hühner (x) und Kaninchen (y): 10 Köpfe, 28 Beine.', 'I: x + y = 10   II: 2x + 4y = 28', 'II − 2 · I: 2y = 8 → y = 4, x = 6. ⟦6 Hühner, 4 Kaninchen⟧'],
     'probe': 'Ohne Gleichungen: Alle 10 Tiere heben 2 Beine hoch – das sind 20 Beine. Am Boden bleiben 28 − 20 = 8 Beine, und das sind nur die Kaninchen, je 2. Also 8 : 2 = 4 Kaninchen ✓ Genau das rechnet II − 2 · I.',
     'fehler': 'Die Beine-Gleichung ist nicht x + y = 28: Ein Huhn hat ⟦2⟧, ein Kaninchen ⟦4⟧ Beine. Jede Information braucht die passenden Faktoren.',
     '_verbot': ['10 Köpfe, 28 Beine']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'pruefen': {
  'einstieg': 'Im Schreibwarenladen weißt du zwei Dinge: Ein Heft und ein Stift kosten zusammen 5 €. Und zwei Hefte kosten 1 € mehr als ein Stift. Welche Preise passen zu beiden Angaben gleichzeitig? Zwei Gleichungen, die zusammen gelten sollen, bilden ein ⟦Gleichungssystem⟧.',
  'woerter': [['Gleichungssystem', 'zwei (oder mehr) Gleichungen, die gleichzeitig stimmen sollen'], ['x, y', 'zwei Unbekannte: hier x = Heftpreis und y = Stiftpreis in €'],
              ['I, II', 'die Nummern der beiden Gleichungen'], ['(2 | 3)', 'Zahlenpaar: x = 2 und y = 3'], ['Lösung', 'ein Zahlenpaar, das beide Gleichungen erfüllt']],
  'schritte': ['Die Angaben als Gleichungen: I: x + y = 5 und II: 2x − y = 1.', 'Probiere das Paar (2 | 3), also Heft 2 € und Stift 3 €. In I: 2 + 3 = 5 – stimmt.',
               'In II: 2 · 2 − 3 = 4 − 3 = 1 – stimmt auch.', 'Beide Gleichungen sind erfüllt: ⟦(2 | 3) ist die Lösung.⟧'],
  'regel': 'So prüfst du ein Zahlenpaar: x und y in ⟦beide⟧ Gleichungen einsetzen. Nur wenn ⟦beide⟧ stimmen, ist das Paar eine ⟦Lösung⟧ des ⟦Gleichungssystems⟧.',
  'fehler': 'Erfüllt (4 | 1) nur x + y = 5, ist es ⟦keine⟧ Lösung: In II gilt 8 − 1 = 7 ≠ 1. Der Preis würde zur ersten Angabe passen, aber nicht zur zweiten. Beide Gleichungen müssen stimmen.'},
 'grafisch': {
  'einstieg': 'Zur Angabe „Heft und Stift kosten zusammen 5 €“ passen viele Preispaare: 1 € und 4 €, 2 € und 3 €, 2,50 € und 2,50 € … Trägt man alle passenden Paare ein, liegen sie auf einer geraden Linie. Zur zweiten Angabe gehört eine zweite Linie. Das Paar, das zu beiden passt, ist ihr ⟦Schnittpunkt⟧.',
  'woerter': [['Gerade', 'gerade Linie, auf der alle passenden Paare (x | y) einer Gleichung liegen'], ['nach y umstellen', 'so umformen, dass y allein steht, z. B. y = −x + 5'],
              ['S(2 | 3)', 'der Schnittpunkt S mit x = 2 und y = 3'], ['L = {(2 | 3)}', 'die Lösungsmenge enthält genau das Paar (2 | 3)']],
  'schritte': ['I: x + y = 5 nach y umstellen: Auf beiden Seiten x abziehen ergibt y = −x + 5.',
               'II: 2x − y = 1 nach y umstellen: y dazuzählen und 1 abziehen ergibt y = 2x − 1.', 'Beide Geraden zeichnen. Sie schneiden sich im Punkt S(2 | 3).',
               'Der Schnittpunkt liegt auf beiden Geraden: ⟦L = {(2 | 3)}⟧.']},
 'einsetzen': {
  'einstieg': 'Manchmal steht eine Angabe schon fertig da, etwa: „Ein Stift kostet 1 € weniger als zwei Hefte“, also y = 2x − 1. Dann schreibst du in der anderen Gleichung statt y genau diesen Ausdruck hin. Danach kommt nur noch x vor. Dieses Vorgehen heißt ⟦Einsetzungsverfahren⟧.',
  'woerter': [['Einsetzungsverfahren', 'eine nach y aufgelöste Gleichung in die andere einsetzen'], ['aufgelöst nach y', 'y steht allein auf einer Seite: y = …'],
              ['Variable', 'ein Buchstabe für eine unbekannte Zahl, hier x und y']],
  'schritte': ['I: y = 2x − 1 (Stiftpreis). II: 3x + y = 9 (drei Hefte und ein Stift kosten 9 €).', 'In II statt y den Ausdruck aus I einsetzen, mit Klammer: 3x + (2x − 1) = 9.',
               'Zusammenfassen: 5x − 1 = 9. 1 dazuzählen und durch 5 teilen: x = 2.', 'x = 2 in I einsetzen: y = 2 · 2 − 1 = 3. ⟦L = {(2 | 3)}⟧ – Heft 2 €, Stift 3 €.']},
 'gleichsetzen': {
  'einstieg': 'Zwei Fahrradverleihe haben unterschiedliche Preise: A verlangt 10 € Grundgebühr und 2 € pro Stunde, B nur 4 € Grundgebühr, aber 4 € pro Stunde. Bei kurzen Touren ist B billiger, bei langen A. Bei welcher Dauer kosten beide gleich viel? Dann ist Preis A gleich Preis B – so arbeitet das ⟦Gleichsetzungsverfahren⟧.',
  'woerter': [['Gleichsetzungsverfahren', 'zwei nach y aufgelöste Gleichungen gleichsetzen'], ['y = 2x + 10', 'Preis y in € bei Verleih A für x Stunden'], ['(3 | 16)', '3 Stunden, 16 €']],
  'schritte': ['A: y = 2x + 10, B: y = 4x + 4 (x Stunden, y Preis in €). Gesucht: Wann kosten beide gleich viel?',
               'Gleich viel heißt: Die beiden rechten Seiten sind gleich, also 2x + 10 = 4x + 4.', 'Auf beiden Seiten 2x und 4 abziehen: 6 = 2x, also x = 3.',
               'x = 3 in A einsetzen: y = 2 · 3 + 10 = 16. ⟦L = {(3 | 16)}⟧ – bei 3 Stunden kosten beide 16 €.']},
 'addition': {
  'einstieg': 'Stell dir zwei Waagen vor, die beide im Gleichgewicht sind. Legst du den Inhalt der beiden linken Schalen zusammen und den der beiden rechten auch, bleibt es im Gleichgewicht. Genauso darf man zwei Gleichungen zusammenzählen. Geschickt gemacht, fällt dabei eine Unbekannte weg – das ist das ⟦Additionsverfahren⟧.',
  'woerter': [['Additionsverfahren', 'zwei Gleichungen addieren, sodass eine Variable wegfällt'], ['Gegenzahlen', 'Zahlen, die zusammen 0 ergeben, z. B. 3 und −3'],
              ['II · 3', 'jedes Glied von Gleichung II mal 3'], ['II′', 'die veränderte Gleichung II']],
  'schritte': ['I: 2x + 3y = 12 und II: x − y = 1.', 'Ziel: Vor y sollen Gegenzahlen stehen. Dazu II mal 3 nehmen: II′: 3x − 3y = 3.',
               'I und II′ addieren: 3y und −3y ergeben 0. Es bleibt 5x = 15, also x = 3.', 'x = 3 in II einsetzen: 3 − y = 1, also y = 2. ⟦L = {(3 | 2)}⟧'],
  'regel': 'So gehst du vor: die Gleichungen so ⟦malnehmen⟧, dass vor einer Variablen ⟦Gegenzahlen⟧ stehen. Dann die Gleichungen ⟦addieren⟧ – diese Variable ⟦fällt weg⟧.',
  'fehler': 'Wer II mit 3 multipliziert, muss ⟦jedes⟧ Glied multiplizieren – auch die rechte Seite: 3x − 3y = 3, nicht 3x − 3y = 1. Sonst wird nur eine Waagschale verdreifacht, und das Gleichgewicht ist weg.'},
 'verfahren': {
  'einstieg': 'Zu einem Ziel führen oft mehrere Wege – mit dem Rad, zu Fuß oder mit dem Bus. Alle kommen an, aber einer ist meist am schnellsten. Bei Gleichungssystemen ist es genauso: Einsetzen, Gleichsetzen und Addieren führen alle zur Lösung. Welches ⟦Verfahren⟧ am wenigsten Arbeit macht, siehst du an der Form der Gleichungen.',
  'woerter': [['Verfahren', 'ein fester Lösungsweg (Einsetzen, Gleichsetzen, Addition)'], ['Vielfache', 'z. B. sind 2, 4, 6 Vielfache von 2']],
  'schritte': ['I: 4x + 5y = 3, II: 2x − 5y = 9.', 'Keine der Gleichungen ist nach x oder y aufgelöst. Einsetzen oder Gleichsetzen bräuchte erst Umformungen.',
               'Vor y stehen 5 und −5. Das sind Gegenzahlen: Beim Addieren fällt y sofort weg.', 'Am geschicktesten ist hier das ⟦Additionsverfahren⟧.']},
 'loesbarkeit': {
  'einstieg': 'Zwei Sonnenblumen wachsen beide 2 cm pro Tag. Die eine ist heute 4 cm größer als die andere. Werden sie je gleich groß? Nein – der Abstand bleibt immer 4 cm. So etwas gibt es auch bei Gleichungssystemen: Dann hat das System ⟦keine Lösung⟧. Es kann sogar ⟦unendlich viele⟧ Lösungen haben.',
  'woerter': [['parallel', 'Geraden mit gleicher Steigung, die sich nie treffen'], ['Aussage wahr / falsch', '0 = 0 ist wahr, 1 = −3 ist falsch'],
              ['unendlich viele Lösungen', 'beide Gleichungen beschreiben dieselbe Gerade; jeder Punkt darauf passt']],
  'schritte': ['I: y = 2x + 1, II: y = 2x − 3. Beide Geraden steigen gleich stark (2 pro Schritt nach rechts).', 'Gleichsetzen: 2x + 1 = 2x − 3.',
               'Auf beiden Seiten 2x abziehen: 1 = −3. Das x ist verschwunden, und die Aussage ist falsch.', 'Das System hat ⟦keine Lösung⟧ – die Geraden sind parallel und treffen sich nie.']},
 'sachaufgabe': {
  'einstieg': 'Auf einem Bauernhof zählst du 10 Köpfe und 28 Beine. Es gibt nur Hühner und Kaninchen. Wie viele sind es von jeder Sorte? Zwei Unbekannte und zwei Angaben – daraus wird ein Gleichungssystem. Solche Textaufgaben heißen ⟦Sachaufgaben⟧.',
  'woerter': [['Variable festlegen', 'aufschreiben, wofür x und y stehen: x = Hühner, y = Kaninchen'], ['II − 2 · I', 'von Gleichung II das Doppelte von Gleichung I abziehen'],
              ['Antwortsatz', 'das Ergebnis in Worten zur Frage']],
  'schritte': ['Festlegen: x = Anzahl der Hühner, y = Anzahl der Kaninchen.', 'Köpfe: x + y = 10 (I). Beine: Huhn 2, Kaninchen 4, also 2x + 4y = 28 (II).',
               'II minus zweimal I: 4y − 2y = 28 − 20, also 2y = 8 und y = 4.', 'Dann ist x = 10 − 4 = 6. Antwort: ⟦6 Hühner und 4 Kaninchen⟧.']},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def g2(a, b):
    """a·x + b·y als Text."""
    s = lin(a, 0) if a else ''
    if b:
        t = lin(b, 0, 'y')
        s = t if not s else s + (' − ' if b < 0 else ' + ') + (t.lstrip('−'))
    return s or '0'


def gl(a, b, c):
    return f'{g2(a, b)} = {zt(c)}'


def sys_text(e1, e2):
    return f'I: {e1}   II: {e2}'


def nz(R, lo=-6, hi=6):
    return R.choice([k for k in range(lo, hi + 1) if k])


def frage(R, x, y, text, weg, h, ccx, ccy):
    """Meist das ganze Zahlenpaar als Lücke, manchmal nur eine Variable."""
    if R.random() < .75:
        return L(f'{text} Gib die Lösung an.', 'x = □; y = □', [x, y], [ccx, ccy], weg, h, hinweis='Trage x und y ein.')
    if R.random() < .5:
        return Z(f'{text} Gib x an.', x, ccx, weg, h)
    return Z(f'{text} Gib y an.', y, ccy, weg, h)


def g_pruefen(R, st):
    while True:
        x, y = R.randint(-6, 8), R.randint(-6, 8)
        a1, b1, a2, b2 = nz(R), nz(R), nz(R), nz(R)
        if a1 * b2 - a2 * b1: break
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    T = sys_text(gl(a1, b1, c1), gl(a2, b2, c2))
    def erf(p, q): return (a1 * p + b1 * q == c1, a2 * p + b2 * q == c2)
    if st == 3:
        kand = [(x, y), (y, x), (x + 1, y), (x, y - 1)]
        p, q = R.choice(kand)
        e = erf(p, q)
        if p == x and q == y: richtig = 'Ja, beide Gleichungen sind erfüllt.'
        elif e == (True, False): richtig = 'Nein, nur Gleichung I ist erfüllt.'
        elif e == (False, True): richtig = 'Nein, nur Gleichung II ist erfüllt.'
        else: richtig = 'Nein, keine der beiden Gleichungen ist erfüllt.'
        alle = ['Ja, beide Gleichungen sind erfüllt.', 'Nein, nur Gleichung I ist erfüllt.', 'Nein, nur Gleichung II ist erfüllt.', 'Nein, keine der beiden Gleichungen ist erfüllt.']
        return A(R, f'Gegeben: {T}. Ist ({zt(p)} | {zt(q)}) eine Lösung?', richtig, [s for s in alle if s != richtig],
                 f'I: {zt(a1 * p + b1 * q)} {"=" if e[0] else "≠"} {zt(c1)}. II: {zt(a2 * p + b2 * q)} {"=" if e[1] else "≠"} {zt(c2)}.',
                 'Setze x und y in jede Gleichung einzeln ein.')
    # falsche Paare: erfüllen nur eine Gleichung oder sind vertauscht
    falsch = []
    for p in range(x - 6, x + 7):
        if b1 and (c1 - a1 * p) % b1 == 0:
            q = (c1 - a1 * p) // b1
            if (p, q) != (x, y): falsch.append((p, q))
    R.shuffle(falsch)
    falsch = falsch[:2] + [(y, x)] if (y, x) != (x, y) else falsch[:3]
    falsch = [f for f in falsch if erf(*f) != (True, True)]
    return A(R, f'Gegeben: {T}. Welches Zahlenpaar ist die Lösung?', f'({zt(x)} | {zt(y)})', [f'({zt(p)} | {zt(q)})' for p, q in falsch] + [f'({zt(x + 1)} | {zt(y)})'],
             f'({zt(x)} | {zt(y)}) erfüllt I: {zt(c1)} = {zt(c1)} und II: {zt(c2)} = {zt(c2)}. Andere Paare erfüllen höchstens eine Gleichung.',
             'Ein Paar, das nur eine Gleichung erfüllt, ist keine Lösung.')


def g_einsetzen(R, st):
    h = 'Setze den Term für y (oder x) in die andere Gleichung ein. Klammern setzen!'
    while True:
        x, y = R.randint(-6, 8), R.randint(-6, 8)
        if st == 1:
            m, t = nz(R, -4, 5), 0
            a, b = R.randint(1, 5), R.choice([1, 2, -1])
        else:
            m, t = nz(R, -4, 5), nz(R, -9, 9)
            a, b = nz(R, -5, 6), nz(R, -4, 4)
        y = m * x + t
        if a + b * m != 0 and abs(y) <= 40: break
    c = a * x + b * y
    if st == 3 and R.random() < .5:
        # nach x aufgelöst
        x2, y2 = y, x
        T = sys_text(f'x = {lin(m, t, "y")}', gl(b, a, c))
        vor = {1: '', -1: '−'}.get(b, f'{zt(b)} · ')
        weg = (f'I in II: {vor}({lin(m, t, "y")}) {"+" if a > 0 else "−"} {lin(abs(a), 0, "y")} = {zt(c)} → {lin(b * m + a, b * t, "y")} = {zt(c)} → y = {zt(y2)}. '
               f'In I: x = {zt(x2)}. L = {{({zt(x2)} | {zt(y2)})}}.')
        return frage(R, x2, y2, f'Löse mit dem Einsetzungsverfahren: {T}.', weg, h, f'({m}) * ({y2}) + ({t})', f'({c} - ({b}) * ({t})) / (({b}) * ({m}) + ({a}))')
    T = sys_text(f'y = {lin(m, t)}', gl(a, b, c))
    weg = (f'I in II: {g2(a, 0)} {"+" if b > 0 else "−"} {"" if abs(b) == 1 else str(abs(b)) + " · "}({lin(m, t)}) = {zt(c)} → '
           f'{lin(a + b * m, b * t)} = {zt(c)} → x = {zt(x)}. In I: y = {einsetzen(lin(m, t), x) + " = " if einsetzen(lin(m, t), x).strip("()") != zt(y) else ""}{zt(y)}. L = {{({zt(x)} | {zt(y)})}}.')
    return frage(R, x, y, f'Löse mit dem Einsetzungsverfahren: {T}.', weg, h, f'({c} - ({b}) * ({t})) / (({a}) + ({b}) * ({m}))', f'({m}) * ({x}) + ({t})')


def g_gleichsetzen(R, st):
    h = 'Setze die beiden rechten Seiten gleich und löse nach x.'
    while True:
        x = R.randint(-6, 8)
        m1, m2 = nz(R, -5, 5), nz(R, -5, 5)
        t1 = nz(R, -9, 9)
        if m1 == m2: continue
        y = m1 * x + t1
        t2 = y - m2 * x
        if abs(y) <= 40 and abs(t2) <= 30: break
    if st == 1:
        m2, t2 = 0 if R.random() < .3 else m2, t2
        if m2 == 0: t2 = y
    if st == 3:
        # zweite Gleichung erst umstellen: k·y = k·m2·x + k·t2  (k ≠ 1)  oder  y − m2x = t2
        k = R.choice([2, 3, -2])
        T = sys_text(f'y = {lin(m1, t1)}', gl(-k * m2, k, k * t2))
        weg = (f'II nach y auflösen: y = {lin(m2, t2)}. Gleichsetzen: {lin(m1, t1)} = {lin(m2, t2)} → {lin(m1 - m2, 0)} = {zt(t2 - t1)}' + ('' if m1 - m2 == 1 else f' → x = {zt(x)}') + f'. In I: y = {zt(y)}. L = {{({zt(x)} | {zt(y)})}}.')
    else:
        T = sys_text(f'y = {lin(m1, t1)}', f'y = {lin(m2, t2)}')
        weg = f'{lin(m1, t1)} = {lin(m2, t2)} → {lin(m1 - m2, 0)} = {zt(t2 - t1)}' + ('' if m1 - m2 == 1 else f' → x = {zt(x)}') + f'. In I: y = {zt(y)}. L = {{({zt(x)} | {zt(y)})}}.'
    return frage(R, x, y, f'Löse mit dem Gleichsetzungsverfahren: {T}.', weg, h if st < 3 else 'Löse zuerst Gleichung II nach y auf.',
                 f'({t2} - ({t1})) / (({m1}) - ({m2}))', f'({m1}) * ({x}) + ({t1})')


def g_addition(R, st):
    h = 'Sorge dafür, dass vor x oder y Gegenzahlen stehen. Dann addiere die Gleichungen.'
    while True:
        x, y = R.randint(-6, 8), R.randint(-6, 8)
        if st == 1:
            a1, a2, b1 = nz(R), nz(R), R.randint(1, 6)
            b2 = -b1
            k1, k2 = 1, 1
        elif st == 2:
            a1, b1 = nz(R), nz(R)
            k = R.choice([2, 3, -2, -3])
            a2, b2 = nz(R), -b1 // 1
            b2 = Fr(-b1, k)
            if b2.denominator != 1: continue
            b2 = int(b2); k1, k2 = 1, k
        else:
            a1, b1, a2, b2 = nz(R), nz(R), nz(R), nz(R)
            k1, k2 = abs(b2), abs(b1)
            if b1 * b2 > 0: k2 = -k2
        if a1 * b2 - a2 * b1 and (k1 * b1 + k2 * b2 == 0): break
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    T = sys_text(gl(a1, b1, c1), gl(a2, b2, c2))
    A_ = k1 * a1 + k2 * a2; C_ = k1 * c1 + k2 * c2
    teil = []
    if k1 != 1: teil.append(f'I · {kl(k1)}: {gl(k1 * a1, k1 * b1, k1 * c1)}')
    if k2 != 1: teil.append(f'II · {kl(k2)}: {gl(k2 * a2, k2 * b2, k2 * c2)}')
    add = f'Addieren: {lin(A_, 0)} = {zt(C_)}' + ('' if A_ == 1 else f' → x = {zt(x)}')
    ein = f'x = {zt(x)} in I: {zt(a1)} · {kl(x)} {"+" if b1 > 0 else "−"} {lin(abs(b1), 0, "y")} = {zt(c1)} → {lin(b1, 0, "y")} = {zt(c1 - a1 * x)}' + ('' if b1 == 1 else f' → y = {zt(y)}')
    weg = ('. '.join(teil) + '. ' if teil else '') + add + '. ' + ein + f'. L = {{({zt(x)} | {zt(y)})}}.'
    return frage(R, x, y, f'Löse mit dem Additionsverfahren: {T}.', weg, h,
                 f'({k1} * ({c1}) + ({k2}) * ({c2})) / ({k1} * ({a1}) + ({k2}) * ({a2}))', f'({c1} - ({a1}) * ({x})) / ({b1})')


ANTW = ['genau eine Lösung', 'keine Lösung', 'unendlich viele Lösungen']
LAGE = {'genau eine Lösung': 'Sie schneiden sich in genau einem Punkt.', 'keine Lösung': 'Sie sind parallel und verschieden.',
        'unendlich viele Lösungen': 'Sie sind identisch (liegen aufeinander).'}


def g_loesbarkeit(R, st):
    if st >= 2 and R.random() < .3:
        art = R.choice(ANTW)
        if R.random() < .5:
            return A(R, f'Ein Gleichungssystem hat {art}. Was bedeutet das für die beiden Geraden?', LAGE[art],
                     [v for k, v in LAGE.items() if k != art] + ['Sie schneiden sich im Ursprung.'],
                     f'Jede Lösung ist ein gemeinsamer Punkt beider Geraden. {art[0].upper() + art[1:]}: {LAGE[art]}',
                     'Die Lösungen sind die gemeinsamen Punkte der Geraden.')
        m = nz(R, -3, 3); t1 = R.randint(-3, 3)
        t2 = {'genau eine Lösung': None, 'keine Lösung': t1 + R.choice([-3, -2, 2, 3]), 'unendlich viele Lösungen': t1}[art]
        m2 = m if t2 is not None else R.choice([k for k in (-2, -1, 1, 2, 3) if k != m])
        if t2 is None: t2 = R.randint(-3, 3)
        gr = {'typ': 'koordinaten', 'x': [-4, 4], 'y': [-8, 8], 'graphen': [{'art': 'linear', 'm': m, 't': t1, 'name': 'I'}, {'art': 'linear', 'm': m2, 't': t2, 'name': 'II'}]}
        return mit_bild(A(R, 'Das Bild zeigt die Geraden zu den Gleichungen I und II. Wie viele Lösungen hat das System?', art, [a for a in ANTW if a != art],
                          f'{LAGE[art]} Also {art}.' + (' (Beide Gleichungen beschreiben dieselbe Gerade – man sieht nur eine Linie.)' if art == ANTW[2] else ''),
                          'Schneiden sich die Geraden, sind sie parallel oder liegen sie aufeinander?'), gr)
    if st == 3 and R.random() < .6:
        # Parameter so bestimmen, dass keine Lösung
        a1, b1 = nz(R, -5, 5), nz(R, -5, 5); k = R.choice([2, 3, -2, -1])
        c1 = R.randint(-9, 9); c2 = k * c1 + R.choice([1, 2, 3, -1, -4])
        T = sys_text(gl(a1, b1, c1), f'{g2(k * a1, 0)} + a · y = {zt(c2)}')
        return Z(f'{T}. Für welchen Wert von a hat das Gleichungssystem keine Lösung?', k * b1, f'{k} * ({b1})',
                 f'Keine Lösung, wenn II die linke Seite von I mal {kl(k)} ist, die rechte Seite aber nicht: a = {kl(k)} · {kl(b1)} = {zt(k * b1)}. '
                 f'Dann steht rechts {zt(c2)} statt {zt(k * c1)}.', 'Vergleiche die Faktoren vor x. Mit welcher Zahl wurde I multipliziert?')
    art = R.choice(ANTW)
    if st == 1:
        m = nz(R, -4, 4); t1 = R.randint(-9, 9)
        if art == ANTW[0]:
            m2 = R.choice([k for k in range(-4, 5) if k != m]); t2 = R.randint(-9, 9)
        elif art == ANTW[1]:
            m2, t2 = m, t1 + R.choice([1, 2, 3, -2, -5])
        else:
            m2, t2 = m, t1
        e2 = f'y = {lin(m2, t2)}' if art != ANTW[2] else f'{g2(-2 * m, 2)} = {zt(2 * t1)}'
        T = sys_text(f'y = {lin(m, t1)}', e2)
        grund = {ANTW[0]: 'Verschiedene Steigungen: Die Geraden schneiden sich in einem Punkt.', ANTW[1]: f'Gleichsetzen ergibt {zt(t1)} = {zt(t2)}: falsch. Parallele Geraden.',
                 ANTW[2]: 'II durch 2 geteilt und nach y aufgelöst ergibt genau I. Beide Gleichungen beschreiben dieselbe Gerade.'}[art]
    else:
        a1, b1 = nz(R), nz(R); c1 = R.randint(-12, 12); k = R.choice([2, 3, -2, -1, -3])
        if art == ANTW[0]:
            a2, b2 = k * a1 + R.choice([1, -1, 2]), k * b1; c2 = R.randint(-12, 12)
        elif art == ANTW[1]:
            a2, b2, c2 = k * a1, k * b1, k * c1 + R.choice([1, 2, -3, 5])
        else:
            a2, b2, c2 = k * a1, k * b1, k * c1
        T = sys_text(gl(a1, b1, c1), gl(a2, b2, c2))
        grund = {ANTW[0]: f'Die linke Seite von II ist kein Vielfaches der linken Seite von I: Es gibt genau ein Lösungspaar.',
                 ANTW[1]: f'I · {kl(k)} ergibt links dasselbe wie II, rechts aber {zt(k * c1)} statt {zt(c2)}: Widerspruch.',
                 ANTW[2]: f'II ist genau I · {kl(k)}: Beide Gleichungen haben dieselben Lösungen.'}[art]
    return A(R, f'Wie viele Lösungen hat {T}?', art, [a for a in ANTW if a != art], grund,
             'Vergleiche die beiden Gleichungen: Ist eine ein Vielfaches der anderen – links, rechts, oder beides?')


VERF = ['Einsetzungsverfahren', 'Gleichsetzungsverfahren', 'Additionsverfahren']


EFFIZIENZ = [
    ('addition', 'Einsetzungsverfahren', 'Man muss erst eine Gleichung umstellen und bekommt Brüche; addieren lässt y sofort wegfallen.',
     ['Das Einsetzungsverfahren geht hier nicht.', 'Es ist nicht umständlicher.', 'Weil man beim Einsetzen immer Klammern braucht.']),
    ('gleich', 'Additionsverfahren', 'Beide sind schon nach y aufgelöst: Gleichsetzen spart das Umordnen.',
     ['Das Additionsverfahren geht hier nicht.', 'Es ist nicht umständlicher.', 'Weil beim Addieren immer x wegfällt.']),
    ('ein', 'Additionsverfahren', 'Eine Gleichung ist schon nach y aufgelöst: Einsetzen spart das Umordnen und Multiplizieren.',
     ['Das Additionsverfahren geht hier nicht.', 'Es ist nicht umständlicher.', 'Weil man beim Addieren keine Gegenzahlen bekommen kann.']),
]


def g_verfahren(R, st):
    if st == 3 and R.random() < .6:
        art, gewaehlt, richtig, falsch = R.choice(EFFIZIENZ)
        x, y = R.randint(-4, 6), R.randint(-4, 6)
        if art == 'addition':
            a1, a2, b = R.choice([3, 5, 7]), R.choice([2, 4, 5]), R.choice([2, 3, 4])
            T = sys_text(gl(a1, b, a1 * x + b * y), gl(a2, -b, a2 * x - b * y))
        elif art == 'gleich':
            m1, m2 = R.sample([k for k in range(-4, 5) if k], 2)
            T = sys_text(f'y = {lin(m1, y - m1 * x)}', f'y = {lin(m2, y - m2 * x)}')
        else:
            m = nz(R, -4, 4); a, b = R.choice([2, 3, 5]), R.choice([3, 4, -3])
            T = sys_text(f'y = {lin(m, y - m * x)}', gl(a, b, a * x + b * y))
        return A(R, f'Bei {T} wählt jemand das {gewaehlt}. Warum ist das umständlich?', richtig, falsch,
                 f'{richtig} Alle Verfahren führen zum Ziel, aber das passende spart Schritte.', 'Wie sehen die Gleichungen aus? Was müsste man zuerst tun?')
    art = R.choice(VERF if st >= 2 else ['Gleichsetzungsverfahren', 'Additionsverfahren'])
    x, y = R.randint(-5, 7), R.randint(-5, 7)
    if art == 'Gleichsetzungsverfahren':
        m1, m2 = R.sample([k for k in range(-5, 6) if k], 2)
        var = R.choice(['x', 'y'])
        if var == 'y':
            T = sys_text(f'y = {lin(m1, y - m1 * x)}', f'y = {lin(m2, y - m2 * x)}')
        else:
            T = sys_text(f'x = {lin(m1, x - m1 * y, "y")}', f'x = {lin(m2, x - m2 * y, "y")}')
        grund = f'Beide Gleichungen sind nach {var} aufgelöst: rechte Seiten gleichsetzen.'
    elif art == 'Einsetzungsverfahren':
        m = nz(R, -4, 4)
        while True:
            a, b = nz(R, -5, 5), nz(R, -5, 5)
            if abs(b) != abs(a * m) and a != 0: break
        T = sys_text(f'y = {lin(m, y - m * x)}', gl(a, b, a * x + b * y)) if R.random() < .5 else sys_text(gl(a, b, a * x + b * y), f'y = {lin(m, y - m * x)}')
        grund = 'Eine Gleichung ist schon nach y aufgelöst, die andere nicht: einsetzen.'
    else:
        a1, a2, b1 = nz(R), nz(R), R.randint(2, 7)
        if abs(a1) == 1 or abs(a2) == 1: a1, a2 = a1 * 2, a2 * 3
        if st >= 2 and R.random() < .5:
            # Vielfache statt Gegenzahlen: II erst multiplizieren
            k = R.choice([2, 3])
            T = sys_text(gl(a1, k * b1, a1 * x + k * b1 * y), gl(a2, -b1, a2 * x - b1 * y))
            grund = f'Vor y stehen {k * b1} und −{b1}: Nach II · {k} sind es Gegenzahlen, dann addieren.'
        else:
            T = sys_text(gl(a1, b1, a1 * x + b1 * y), gl(a2, -b1, a2 * x - b1 * y))
            grund = f'Vor y stehen {b1} und −{b1}: Addieren lässt y sofort wegfallen.'
    return A(R, f'Welches Verfahren ist für {T} am geschicktesten?', art, [v for v in VERF if v != art], grund,
             'Schau, ob eine Gleichung schon nach x oder y aufgelöst ist, und ob Gegenzahlen vorkommen.')


def g_sachaufgabe(R, st):
    art = R.choice({1: ['zahlen', 'tiere', 'muenzen', 'aufstellen'], 2: ['eintritt', 'tiere', 'muenzen', 'aufstellen'], 3: ['eintritt', 'tarif', 'fitness', 'mischung']}[st])
    if art == 'aufstellen':
        p1, p2 = R.choice([(9, Fr(9, 2)), (12, 6), (8, 5), (15, 9), (10, 7)])
        x, y = R.randint(2, 10), R.randint(2, 12)
        n, G = x + y, p1 * x + p2 * y
        ri = f'x + y = {n}; {zt(p1)}x + {zt(p2)}y = {zt(G)}'
        fa = [f'x + y = {zt(G)}; {zt(p1)}x + {zt(p2)}y = {n}', f'{zt(p1)}x + y = {n}; x + {zt(p2)}y = {zt(G)}', f'x + y = {n}; {zt(p2)}x + {zt(p1)}y = {zt(G)}']
        return A(R, f'Eine Gruppe aus {n} Personen zahlt {eur(G)} € Eintritt. Erwachsene zahlen {eur(p1)} €, Kinder {eur(p2)} €. Welches Gleichungssystem passt (x Erwachsene, y Kinder)?',
                 ri, fa, f'Personen: x + y = {n}. Geld: {eur(p1)} € je Erwachsener und {eur(p2)} € je Kind ergibt {zt(p1)}x + {zt(p2)}y = {zt(G)}. (Lösung: {x} Erwachsene, {y} Kinder.)',
                 'Eine Gleichung zählt die Personen, die andere das Geld.')
    if art == 'fitness':
        g1, p1 = R.choice([20, 25, 30]), R.choice([2, 3])
        p2 = p1 + R.choice([2, 3])
        n = R.randint(3, 8)
        g2_ = g1 - (p2 - p1) * n
        if g2_ <= 0: return g_sachaufgabe(R, st)
        return Z(f'Fitnessstudio A kostet {g1} € im Monat plus {p1} € pro Besuch, Studio B {g2_} € im Monat plus {p2} € pro Besuch. Bei wie vielen Besuchen im Monat kosten beide gleich viel?', n,
                 f'({g1} - {g2_}) / ({p2} - {p1})', f'I: y = {lin(p1, g1)}, II: y = {lin(p2, g2_)}. Gleichsetzen: {lin(p1, g1)} = {lin(p2, g2_)} → {g1 - g2_} = {lin(p2 - p1, 0)} → x = {n}. '
                 f'Kosten dann: y = {p1} · {n} + {g1} = {p1 * n + g1} €.', 'Stelle für jedes Studio y = Grundbetrag + Preis · x auf und setze gleich.')
    if art == 'zahlen':
        a, b = sorted(R.sample(range(3, 60), 2), reverse=True)
        return Z(f'Die Summe zweier Zahlen ist {a + b}, ihre Differenz ist {a - b}. Wie heißt die größere Zahl?', a, f'({a + b} + {a - b}) / 2',
                 f'I: x + y = {a + b}, II: x − y = {a - b}. I + II: 2x = {2 * a} → x = {a}. In I: y = {a + b} − {a} = {b}.', 'Stelle zwei Gleichungen auf und addiere sie.')
    if art == 'tiere':
        x, y = R.randint(3, 25), R.randint(2, 20)
        k = x + y; bn = 2 * x + 4 * y
        if R.random() < .5:
            return Z(f'Auf einem Hof leben Hühner und Kaninchen, zusammen {k} Tiere mit {bn} Beinen. Wie viele Kaninchen sind es?', y, f'({bn} - 2 * {k}) / 2',
                     f'I: x + y = {k}, II: 2x + 4y = {bn}. II − 2 · I: 2y = {bn - 2 * k} → y = {y}. Hühner: x = {k} − {y} = {x}.', 'Hühner haben 2, Kaninchen 4 Beine.')
        return Z(f'Auf einem Hof leben Hühner und Kaninchen, zusammen {k} Tiere mit {bn} Beinen. Wie viele Hühner sind es?', x, f'{k} - ({bn} - 2 * {k}) / 2',
                 f'I: x + y = {k}, II: 2x + 4y = {bn}. II − 2 · I: 2y = {bn - 2 * k} → y = {y}, x = {k} − {y} = {x}.', 'Hühner haben 2, Kaninchen 4 Beine.')
    if art == 'muenzen':
        w1, w2 = R.choice([(2, 1), (Fr(1, 2), Fr(1, 5)), (2, Fr(1, 2)), (1, Fr(1, 2))])
        x, y = R.randint(3, 20), R.randint(3, 20)
        n, W = x + y, w1 * x + w2 * y
        n1, n2 = {Fr(2): '2-€', Fr(1): '1-€', Fr(1, 2): '50-Cent', Fr(1, 5): '20-Cent'}[Fr(w1)], {Fr(2): '2-€', Fr(1): '1-€', Fr(1, 2): '50-Cent', Fr(1, 5): '20-Cent'}[Fr(w2)]
        return Z(f'In einer Spardose sind {n} Münzen, nur {n1}- und {n2}-Stücke, zusammen {eur(W)} €. Wie viele {n1}-Stücke sind es?', x,
                 f'({cz(W)} - {cz(w2)} * {n}) / ({cz(w1)} - {cz(w2)})',
                 f'I: x + y = {n}, II: {g2(w1, w2)} = {zt(W)}. y = {n} − x einsetzen: {lin(Fr(w1) - Fr(w2), 0)} = {zt(W - Fr(w2) * n)}' + ('' if Fr(w1) - Fr(w2) == 1 else f' → x = {x}') + f'. Andere Sorte: y = {n} − {x} = {y}.',
                 'x = Anzahl der wertvolleren Münzen. Eine Gleichung für die Anzahl, eine für den Wert.')
    if art == 'eintritt':
        p1, p2 = R.choice([(12, 7), (9, 5), (15, 8), (Fr(21, 2), 6), (8, Fr(9, 2)), (14, 9)])
        x, y = R.randint(2, 30), R.randint(2, 40)
        n, G = x + y, p1 * x + p2 * y
        return Z(f'Eine Eintrittskarte kostet für Erwachsene {eur(p1)} €, für Kinder {eur(p2)} €. Eine Gruppe aus {n} Personen zahlt {eur(G)} €. Wie viele Kinder sind dabei?', y,
                 f'({cz(p1)} * {n} - {cz(G)}) / ({cz(p1)} - {cz(p2)})',
                 f'I: x + y = {n}, II: {eur(p1)}x + {eur(p2)}y = {eur(G)}. x = {n} − y einsetzen: {eur(Fr(p1) * n)} − {eur(Fr(p1) - Fr(p2))}y = {eur(G)} → y = {y}. Erwachsene: x = {n} − {y} = {x}.',
                 'x = Erwachsene, y = Kinder. Eine Gleichung für die Personen, eine für den Preis.')
    if art == 'tarif':
        g1, p1 = R.choice([20, 30, 35, 40, 50]), R.choice([30, 35, 40, 45])
        p2 = p1 + R.choice([5, 10, 15])
        t = Fr(R.randint(1, 8) * 2 + R.choice([0, 1]), 2)
        gB = g1 + (p1 - p2) * t
        if gB < 0 or gB.denominator != 1: return g_sachaufgabe(R, st)
        return Z(f'Handwerker A berechnet {g1} € Anfahrt und {p1} € pro Stunde, Handwerker B {zt(gB)} € Anfahrt und {p2} € pro Stunde. Nach wie vielen Stunden kosten beide gleich viel?', t,
                 f'({g1} - {cz(gB)}) / ({p2} - {p1})', f'I: y = {lin(p1, g1)}, II: y = {lin(p2, gB)}. Gleichsetzen: {lin(p1 - p2, 0)} = {zt(gB - g1)} → x = {zt(t)} h. Kosten dann: y = {eur(p1 * t + g1)} €.',
                 'Stelle für jeden Handwerker eine Gleichung y = Anfahrt + Preis · x auf und setze gleich.', einheit='h')
    # Mischung (realistische Preise: Nüsse 8–20 €/kg, Kaffee 10–30 €/kg)
    sorte = R.choice([('Erdnüsse', 'Cashewkerne', [(8, 20), (9, 18), (10, 16)]), ('Kaffee der Sorte A', 'Kaffee der Sorte B', [(12, 24), (14, 28), (10, 22), (15, 30)])])
    k1, k2 = R.choice(sorte[2])
    x, y = R.randint(2, 12), R.randint(2, 12)
    m, P = x + y, k1 * x + k2 * y
    return Z(f'Ein Händler mischt {sorte[0]} zu {k1} € pro kg mit {sorte[1]} zu {k2} € pro kg. Er erhält {m} kg Mischung im Wert von {P} €. Wie viel kg der billigeren Sorte verwendet er?', x,
             f'({k2} * {m} - {P}) / ({k2} - {k1})', f'I: x + y = {m}, II: {k1}x + {k2}y = {P}. y = {m} − x: {k1}x + {k2 * m} − {k2}x = {P} → {lin(k1 - k2, 0)} = {zt(P - k2 * m)} → x = {x}. Teurere Sorte: y = {m} − {x} = {y}.',
             'Eine Gleichung für die Masse, eine für den Preis.', einheit='kg')


def g_grafisch(R, st):
    while True:
        x, y = R.randint(-3, 4), R.randint(-3, 5)
        ms = [-3, -2, -1, Fr(-1, 2), Fr(1, 2), 1, 2, 3] if st >= 2 else [-2, -1, 1, 2]
        m1, m2 = R.sample(ms, 2)
        t1, t2 = y - m1 * x, y - m2 * x
        if Fr(t1).denominator == 1 and Fr(t2).denominator == 1 and abs(t1) <= 8 and abs(t2) <= 8: break
    f = lambda m: float(m) if Fr(m).denominator != 1 else int(m)
    gr = {'typ': 'koordinaten', 'x': [x - 4, x + 4], 'y': [y - 6, y + 6],
          'graphen': [{'art': 'linear', 'm': f(m1), 't': int(t1), 'name': 'I'}, {'art': 'linear', 'm': f(m2), 't': int(t2), 'name': 'II'}]}
    def gleich(m, t):
        if Fr(m).denominator == 2:   # 2y = 2m·x + 2t  →  −(2m)x + 2y = 2t
            return gl(int(-2 * m), 2, int(2 * t))
        return gl(int(-m), 1, int(t)) if R.random() < .5 else f'y = {lin(m, t)}'
    T = sys_text(gleich(m1, t1), gleich(m2, t2))
    probe = f'Probe: I und II mit x = {zt(x)}, y = {zt(y)} erfüllt.'
    if st == 3 and R.random() < .5:
        # ein Kandidat ist abgelesen – prüfen, ob er stimmt
        p, q = R.choice([(x, y), (x + 1, y), (x, y + 1)])
        ok = (p, q) == (x, y)
        return mit_bild(A(R, f'Gegeben: {T}. Jemand liest am Bild den Schnittpunkt ({zt(p)} | {zt(q)}) ab. Stimmt das?',
                          'Ja, das Paar erfüllt beide Gleichungen.' if ok else f'Nein, richtig ist ({zt(x)} | {zt(y)}).',
                          ['Nein, richtig ist (' + zt(y) + ' | ' + zt(x) + ').' if (y, x) != (x, y) else 'Nein, richtig ist (0 | 0).',
                           'Ja, das Paar erfüllt beide Gleichungen.' if not ok else f'Nein, richtig ist ({zt(x + 1)} | {zt(y)}).', 'Das kann man am Bild nicht entscheiden.'],
                          f'Der Schnittpunkt ist ({zt(x)} | {zt(y)}). {probe}', 'Setze das abgelesene Paar in beide Gleichungen ein.'), gr)
    return mit_bild(L(f'Lies die Lösung des Gleichungssystems {T} am Schnittpunkt ab.', 'S(□ | □)', [x, y], [str(x), str(y)],
                      f'Die Geraden schneiden sich in S({zt(x)} | {zt(y)}). L = {{({zt(x)} | {zt(y)})}}. {probe}',
                      'Suche den Punkt, der auf beiden Geraden liegt. Erst nach rechts/links (x), dann nach oben/unten (y).', hinweis='Trage x und y des Schnittpunkts ein.'), gr)


GEN = {'grafisch': g_grafisch, 'pruefen': g_pruefen, 'einsetzen': g_einsetzen, 'gleichsetzen': g_gleichsetzen, 'addition': g_addition,
       'loesbarkeit': g_loesbarkeit, 'verfahren': g_verfahren, 'sachaufgabe': g_sachaufgabe}


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

def _pr(*z):
    return {'typ': 'tabelle', 'kopf': ['Paar', 'I: x + y = 5', 'II: 2x − y = 1'], 'zeilen': [list(r) for r in z]}


def _add(*z):
    return {'typ': 'tabelle', 'kopf': ['', 'links', 'rechts'], 'zeilen': [list(r) for r in z]}


def _hof(a, b, c, d):
    return {'typ': 'tabelle', 'kopf': ['', 'Hühner', 'Kaninchen', 'zusammen'], 'zeilen': [['Köpfe', a, b, '10'], ['Beine', c, d, '28']]}


_HEFT = {'typ': 'koordinaten', 'x': [-1, 5], 'y': [-2, 6], 'graphen': [{'art': 'linear', 'm': -1, 't': 5, 'name': 'I'}, {'art': 'linear', 'm': 2, 't': -1, 'name': 'II'}], 'name_x': 'Heft', 'name_y': 'Stift'}
UMBAU = {
 'pruefen': {
  'einstieg': 'Im Laden weißt du: Heft und Stift kosten zusammen 5 €. Zwei Hefte kosten 1 € mehr als ein Stift. Zwei Angaben, die zusammen gelten sollen, bilden ein ⟦Gleichungssystem⟧.',
  'woerter': [['Gleichungssystem', 'zwei Gleichungen, die gleichzeitig stimmen sollen'], ['I', 'die erste Gleichung; II ist die zweite'], ['(2 | 3)', 'Zahlenpaar: x = 2 (Heft) und y = 3 (Stift)']],
  'bild': _pr(('(2 | 3)', '?', '?')),
  'schritte': [{'text': 'Als Gleichungen: I: x + y = 5, II: 2x − y = 1.'},
               {'text': '(2 | 3) heißt: Heft 2 €, Stift 3 €.'},
               {'text': 'In I: 2 + 3 = 5 ✓', 'bild': _pr(('(2 | 3)', '5 ✓', '?'))},
               {'text': 'In II: 2 · 2 − 3 = 1 ✓', 'bild': _pr(('(2 | 3)', '5 ✓', '1 ✓'))},
               {'text': 'Beide stimmen: ⟦(2 | 3) ist die Lösung⟧.'}],
  'fehler': '(4 | 1) passt nur zu I. In II gilt 8 − 1 = 7, nicht 1. Ein Paar muss ⟦beide⟧ Gleichungen erfüllen.',
  'fehler_bild': _pr(('(2 | 3)', '5 ✓', '1 ✓'), ('(4 | 1)', '5 ✓', '7 ✗')),
  'regel': 'Setze das Paar in ⟦beide Gleichungen⟧ ein. Nur wenn beide stimmen, ist es eine Lösung.'},
 'grafisch': {
  'einstieg': 'Zu „Heft und Stift kosten zusammen 5 €“ passen viele Preispaare. Eingezeichnet liegen sie auf einer Geraden, die zweite Angabe gibt eine zweite. Das Paar, das zu beiden passt, ist der ⟦Schnittpunkt⟧.',
  'woerter': [['Gerade', 'auf ihr liegen alle passenden Paare einer Gleichung'], ['Schnittpunkt', 'der Punkt, der auf beiden Geraden liegt'], ['nach y umstellen', 'so umformen, dass y allein links steht']],
  'bild': _HEFT,
  'schritte': [{'text': 'I nach y umstellen: y = −x + 5. Das ist die Gerade I.'},
               {'text': 'II nach y umstellen: y = 2x − 1. Das ist die Gerade II.'},
               {'text': 'Sie schneiden sich in S(2 | 3). Also ⟦L = {(2 | 3)}⟧.', 'bild': {'punkte': [{'x': 2, 'y': 3, 'name': 'S(2 | 3)'}], 'senkrecht': [2], 'waagrecht': [3]}}],
  'fehler': 'Liegt S zwischen den Kästchen, ist abgelesen nur geschätzt. Setze das Paar zur Kontrolle in ⟦beide Gleichungen⟧ ein.',
  'regel': 'Die Lösung ist der ⟦Schnittpunkt⟧ der beiden Geraden. Kontrolliere ihn durch Einsetzen.'},
 'einsetzen': {
  'einstieg': 'Manchmal steht eine Angabe schon fertig da: Ein Stift kostet 1 € weniger als zwei Hefte. Diesen Term setzt du für y in die andere Gleichung. Das heißt ⟦Einsetzungsverfahren⟧.',
  'woerter': [['Einsetzungsverfahren', 'den Term für y in die andere Gleichung einsetzen'], ['Term', 'ein Rechenausdruck, z. B. 2x − 1']],
  'bild': {**_HEFT, 'y': [-2, 10], 'graphen': [{'art': 'linear', 'm': 2, 't': -1, 'name': 'I'}, {'art': 'linear', 'm': -3, 't': 9, 'name': 'II'}]},
  'schritte': [{'text': 'I: y = 2x − 1. II: 3x + y = 9.'},
               {'text': 'Den Term in II einsetzen, mit Klammer: 3x + (2x − 1) = 9.'},
               {'text': 'Zusammenfassen: 5x − 1 = 9, also 5x = 10 und x = 2.'},
               {'text': 'x = 2 in I: y = 3. Also ⟦L = {(2 | 3)}⟧.', 'bild': {'punkte': [{'x': 2, 'y': 3, 'name': '(2 | 3)'}]}}],
  'fehler': 'Die ⟦Klammer⟧ zählt: 3x − (2x − 1) = 3x − 2x + 1. Ohne Klammer stünde dort fälschlich − 1.',
  'regel': 'Steht y = … schon da, ⟦setzt du diesen Term ein⟧. Dann bleibt eine Gleichung mit nur x.'},
 'gleichsetzen': {
  'einstieg': 'Verleih A kostet 10 € plus 2 € pro Stunde, Verleih B 4 € plus 4 € pro Stunde. Wann kosten beide gleich viel? Dann ist Preis A gleich Preis B: ⟦Gleichsetzungsverfahren⟧.',
  'woerter': [['Gleichsetzungsverfahren', 'die beiden Terme für y gleichsetzen'], ['Zahlenpaar', 'die Lösung (x | y), hier Stunden und Preis']],
  'bild': {'typ': 'koordinaten', 'x': [0, 6], 'y': [0, 30], 'graphen': [{'art': 'linear', 'm': 2, 't': 10, 'name': 'A'}, {'art': 'linear', 'm': 4, 't': 4, 'name': 'B'}], 'schritt_y': 5, 'name_x': 'h', 'name_y': '€'},
  'schritte': [{'text': 'A: y = 2x + 10. B: y = 4x + 4.'},
               {'text': 'Gleich viel heißt gleichsetzen: 2x + 10 = 4x + 4.'},
               {'text': '2x und 4 abziehen: 6 = 2x, also x = 3.', 'bild': {'senkrecht': [3]}},
               {'text': 'y = 2 · 3 + 10 = 16. Das Zahlenpaar ist ⟦(3 | 16)⟧.', 'bild': {'punkte': [{'x': 3, 'y': 16, 'name': '(3 | 16)'}]}}],
  'fehler': 'Mit x = 3 ist nicht Schluss: Die Lösung ist ein ⟦Zahlenpaar⟧. Erst y = 16 sagt, was die 3 Stunden kosten.',
  'regel': 'Steht zweimal y = …, ⟦setzt du die Terme gleich⟧. Dann x ausrechnen und für y einsetzen.'},
 'addition': {
  'einstieg': 'Zwei Waagen sind im Gleichgewicht. Legst du beide linken Schalen zusammen und beide rechten auch, bleibt es im Gleichgewicht. So darfst du Gleichungen addieren: das ⟦Additionsverfahren⟧.',
  'woerter': [['Additionsverfahren', 'zwei Gleichungen zusammenzählen, damit eine Variable wegfällt'], ['Gegenzahlen', 'gleiche Zahl, anderes Vorzeichen: 3 und −3']],
  'bild': _add(('I', '2x + 3y', '12'), ('II', 'x − y', '1')),
  'schritte': [{'text': 'I: 2x + 3y = 12, II: x − y = 1.'},
               {'text': 'II mal 3: 3x − 3y = 3. Vor y stehen jetzt Gegenzahlen.', 'bild': _add(('I', '2x + 3y', '12'), ('3 · II', '3x − 3y', '3'))},
               {'text': 'Addieren: 5x = 15, also x = 3.', 'bild': _add(('I', '2x + 3y', '12'), ('3 · II', '3x − 3y', '3'), ('Summe', '5x', '15'))},
               {'text': 'Aus II folgt y = 2. ⟦L = {(3 | 2)}⟧.'}],
  'fehler': 'Mal 3 gilt für ⟦jedes⟧ Glied, auch rechts: 3x − 3y = 3, nicht = 1. Sonst wird nur eine Waagschale verdreifacht.',
  'fehler_bild': _add(('I', '2x + 3y', '12'), ('3 · II', '3x − 3y', '1 ?')),
  'regel': 'Mach vor einer Variablen ⟦Gegenzahlen⟧, dann addiere. Diese Variable fällt weg.'},
 'verfahren': {
  'einstieg': 'Zur Schule kommst du mit dem Rad, zu Fuß oder mit dem Bus. Alle kommen an, einer ist am schnellsten. Bei Gleichungssystemen siehst du das schnellste ⟦Verfahren⟧ an der Form.',
  'woerter': [['Verfahren', 'ein fester Rechenweg: Einsetzen, Gleichsetzen oder Addieren'], ['Gegenzahlen', 'gleiche Zahl, anderes Vorzeichen: 5 und −5']],
  'bild': {'typ': 'tabelle', 'kopf': ['Form', 'Verfahren'], 'zeilen': [['zweimal y = …', 'Gleichsetzen'], ['einmal y = …', 'Einsetzen'], ['Gegenzahlen', 'Addieren']]},
  'schritte': [{'text': 'I: 4x + 5y = 3, II: 2x − 5y = 9.'},
               {'text': 'Keine Gleichung ist nach x oder y aufgelöst.'},
               {'text': 'Vor y stehen 5 und −5, also Gegenzahlen.'},
               {'text': 'Am geschicktesten ist hier ⟦Addieren⟧: y fällt sofort weg.'}],
  'fehler': 'Bei y = 3x und y = x + 4 erst umzustellen kostet unnötig Zeit. Beide sind schon nach y aufgelöst: ⟦gleichsetzen⟧.',
  'regel': 'Wähle das Verfahren nach der ⟦Form der Gleichungen⟧. Zweimal y = …: gleichsetzen. Einmal: einsetzen. Gegenzahlen: addieren.'},
 'loesbarkeit': {
  'einstieg': 'Zwei Sonnenblumen wachsen beide 2 cm pro Tag, eine ist 4 cm größer. Sie werden nie gleich groß. Dann hat das Gleichungssystem ⟦keine Lösung⟧.',
  'woerter': [['parallel', 'gleich steil – die Geraden treffen sich nie'], ['unendlich viele Lösungen', 'beide Gleichungen beschreiben dieselbe Gerade']],
  'bild': {'typ': 'koordinaten', 'x': [-3, 3], 'y': [-5, 5], 'graphen': [{'art': 'linear', 'm': 2, 't': 1, 'name': 'I'}, {'art': 'linear', 'm': 2, 't': -3, 'name': 'II'}]},
  'schritte': [{'text': 'I: y = 2x + 1, II: y = 2x − 3.'},
               {'text': 'Gleichsetzen: 2x + 1 = 2x − 3. 2x abziehen: 1 = −3.'},
               {'text': 'Das ist falsch. Die Geraden sind parallel: ⟦keine Lösung⟧.'},
               {'text': 'Kommt dagegen 0 = 0 heraus, gibt es unendlich viele Lösungen.', 'bild': {'graphen': [{'art': 'linear', 'm': 2, 't': 1, 'name': 'I = II'}]}}],
  'fehler': 'Bei 0 = 0 ist nicht x = 0 die Lösung. Die Aussage stimmt ⟦immer⟧: Es gibt unendlich viele Lösungen.',
  'regel': 'Fällt x weg, entscheidet der Rest: ⟦falsch heißt keine Lösung⟧. Wahr, wie 0 = 0, heißt unendlich viele.'},
 'sachaufgabe': {
  'einstieg': 'Auf einem Hof zählst du 10 Köpfe und 28 Beine, nur Hühner und Kaninchen. Wie viele sind es von jeder Sorte? So eine Textaufgabe ist eine ⟦Sachaufgabe⟧.',
  'woerter': [['Sachaufgabe', 'eine Rechenaufgabe als Geschichte'], ['Variable', 'ein Buchstabe für eine gesuchte Zahl, hier x und y']],
  'bild': _hof('x', 'y', '2x', '4y'),
  'schritte': [{'text': 'Variable festlegen: x Hühner, y Kaninchen.'},
               {'text': 'Köpfe: x + y = 10. Beine: 2x + 4y = 28.'},
               {'text': 'Beine minus zweimal Köpfe: 2y = 8, also y = 4.'},
               {'text': 'Dann ist x = 6. Antwort: ⟦6 Hühner und 4 Kaninchen⟧.', 'bild': _hof('6', '4', '12', '16')}],
  'fehler': 'Die Beine-Gleichung ist nicht x + y = 28: Ein Huhn hat ⟦2⟧ Beine, ein Kaninchen 4.',
  'regel': 'Für jede gesuchte Größe eine ⟦Variable⟧, für jede Angabe eine Gleichung. Dann lösen und im Satz antworten.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): Grundwissen 8 bayerischer Gymnasien (Textaufgaben, die auf ein LGS führen;
# grafisch und rechnerisch mit keiner/einer/unendlich vielen Lösungen), Schulaufgaben-Typ Kl. 8 (Tarifvergleich, Altersrätsel, Preisaufgabe,
# Multiplizieren beider Gleichungen beim Additionsverfahren), BMT8 2024 (Rückwärts: Zahl so wählen, dass ein Paar Lösung ist),
# Mathematik-Wettbewerbe (Ziffernrätsel, geschicktes Addieren/Subtrahieren symmetrischer Gleichungen).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_6)
_k = lambda **k: {'typ': 'koordinaten', **k}
_l = lambda m, t, name=None: {'art': 'linear', 'm': m, 't': t, **({'name': name} if name else {})}
_HZ = 'Je Lücke eine ganze Zahl.'

# pruefen
SW.a('pruefen', 2, 'Welches Zahlenpaar erfüllt Gleichung I: 2x + y = 5, aber NICHT Gleichung II: x − y = 1?', '(1 | 3)', ['(2 | 1)', '(0 | −1)', '(3 | 2)'],
     '(1 | 3): I: 2 + 3 = 5 ✓, II: 1 − 3 = −2 ✗. (2 | 1) erfüllt beide, (0 | −1) und (3 | 2) erfüllen I nicht.', 'Prüfe jedes Paar zuerst in I, dann in II.')
SW.a('pruefen', 2, 'Ist (−2 | 0,5) eine Lösung von I: x + 4y = 0 und II: 3x − 2y = −7?', 'Ja, beide Gleichungen sind erfüllt.',
     ['Nein, nur Gleichung I ist erfüllt.', 'Nein, nur Gleichung II ist erfüllt.', 'Nein, keine der beiden Gleichungen ist erfüllt.'],
     'I: −2 + 4 · 0,5 = −2 + 2 = 0 ✓. II: 3 · (−2) − 2 · 0,5 = −6 − 1 = −7 ✓.', 'Setze x = −2 und y = 0,5 in beide Gleichungen ein.')
SW.z('pruefen', 3, 'Das Zahlenpaar (3 | −2) soll Lösung von I: 2x + y = 4 und II: x − 4y = c sein. Bestimme c.', 11, '3 - 4 * (-2)',
     'I stimmt: 6 − 2 = 4. In II einsetzen: c = 3 − 4 · (−2) = 3 + 8 = 11.', 'Setze das Paar in II ein. Achte auf minus mal minus.', art='P')
SW.a('pruefen', 3, 'Ein Rechteck ist 4 cm länger als breit. Sein Umfang ist 36 cm. Welches Gleichungssystem passt (x = Länge, y = Breite)?', 'x = y + 4;  2x + 2y = 36',
     ['x = y + 4;  x + y = 36', 'y = x + 4;  2x + 2y = 36', 'x = 4y;  2x + 2y = 36'],
     '„4 cm länger als breit“: Länge = Breite + 4, also x = y + 4. Umfang = 2 · Länge + 2 · Breite = 36.', 'Übersetze jeden Satz einzeln. Was ist der Umfang eines Rechtecks?', art='P')
SW.z('pruefen', 3, 'Das Zahlenpaar (a | 2a) ist Lösung von I: 3x + y = 15 und II: x − y = b. Bestimme b.', -3, '3 - 6',
     'In I: 3a + 2a = 15 ⇔ a = 3. Das Paar ist (3 | 6). In II: b = 3 − 6 = −3.', 'Bestimme zuerst a mit Gleichung I.', art='K')
SW.z('pruefen', 3, 'Wie viele Zahlenpaare aus positiven ganzen Zahlen erfüllen die Gleichung x + 2y = 9?', 4, '1 + 1 + 1 + 1',
     'y = 1: x = 7. y = 2: x = 5. y = 3: x = 3. y = 4: x = 1. Bei y = 5 wäre x negativ. Also 4 Paare. Eine Gleichung allein hat viele Lösungen.',
     'Probiere y = 1, 2, 3, … und berechne x.', art='K')

# grafisch
SW.l('grafisch', 2, 'Lies den Schnittpunkt der beiden Geraden ab.', 'S(□ | □)', [2, 3], ['2', '3'], 'Die Geraden y = 0,5x + 2 und y = −x + 5 schneiden sich in (2 | 3). Probe: 0,5 · 2 + 2 = 3 und −2 + 5 = 3.',
     'Suche den gemeinsamen Punkt und lies x und y ab.', _HZ, grafik=_k(x=[-2, 6], y=[-1, 6], graphen=[_l(0.5, 2, 'g'), _l(-1, 5, 'h')]))
SW.a('grafisch', 2, 'Die beiden Geraden eines Gleichungssystems sind gezeichnet. Wie viele Lösungen hat das System?', 'keine Lösung', ['genau eine Lösung', 'unendlich viele Lösungen', 'zwei Lösungen'],
     'Die Geraden sind parallel (gleiche Steigung) und verschieden. Sie haben keinen gemeinsamen Punkt.', 'Haben die Geraden einen gemeinsamen Punkt?',
     grafik=_k(x=[-4, 4], y=[-5, 5], graphen=[_l(1, 1, 'g'), _l(1, -2, 'h')]))
SW.l('grafisch', 3, 'Die Geraden g: y = 2x − 1 und h: y = −x + 1,5 schneiden sich ungefähr bei (0,8 | 0,7). Berechne die x-Koordinate genau (gekürzter Bruch).', 'x = □/□', [5, 6], ['5', '6'],
     'Gleichsetzen: 2x − 1 = −x + 1,5 ⇔ 3x = 2,5 ⇔ x = 2,5/3 = 5/6 ≈ 0,83. Am Bild kann man das nur ungefähr ablesen.',
     'Ablesen ist hier ungenau. Rechne mit Gleichsetzen.', 'Zähler und Nenner je als ganze Zahl.',
     grafik=_k(x=[-2, 3], y=[-3, 3], graphen=[_l(2, -1, 'g'), _l(-1, 1.5, 'h')]), art='P')
SW.a('grafisch', 3, 'Welches Gleichungssystem gehört zu den gezeichneten Geraden?', 'I: x + y = 3;  II: 2x − y = 0',
     ['I: x + y = 3;  II: x − 2y = 0', 'I: x − y = 3;  II: 2x − y = 0', 'I: x + y = −3;  II: 2x + y = 0'],
     'Die fallende Gerade geht durch (0 | 3) und (3 | 0): y = −x + 3, also x + y = 3. Die steigende durch (0 | 0) und (1 | 2): y = 2x, also 2x − y = 0.',
     'Bestimme zu jeder Geraden y = m · x + t und forme um.', grafik=_k(x=[-2, 4], y=[-2, 5], graphen=[_l(-1, 3), _l(2, 0)]), art='P')
SW.a('grafisch', 3, 'Die Gerade g: y = x + 1 ist gezeichnet. Mit welcher zweiten Gleichung hat das System KEINE Lösung?', 'y = x − 3', ['y = −x + 1', '2y = 2x + 2', 'y = 2x + 1'],
     'Keine Lösung heißt: parallel, aber verschieden. y = x − 3 hat dieselbe Steigung 1. 2y = 2x + 2 ist dieselbe Gerade wie g (unendlich viele Lösungen).',
     'Welche Gerade ist parallel zu g, aber nicht gleich?', grafik=_k(x=[-4, 4], y=[-4, 5], graphen=[_l(1, 1, 'g')]), art='K')
SW.l('grafisch', 3, 'Gerade g geht durch A(0 | 4) und B(4 | 0), Gerade h durch C(0 | −2) und D(2 | 0). Denke dir die Geraden durch die Punkte. Wo schneiden sie sich?', 'S(□ | □)',
     [3, 1], ['(4 + 2) / 2', '-3 + 4'], 'g: y = −x + 4, h: y = x − 2. Gleichsetzen: −x + 4 = x − 2 ⇔ x = 3, y = 1. S(3 | 1).',
     'Bestimme aus den Punkten die beiden Geradengleichungen.', _HZ,
     grafik=_k(x=[-1, 5], y=[-3, 5], punkte=[{'x': 0, 'y': 4, 'name': 'A'}, {'x': 4, 'y': 0, 'name': 'B'}, {'x': 0, 'y': -2, 'name': 'C'}, {'x': 2, 'y': 0, 'name': 'D'}]), art='K')

# einsetzen
SW.l('einsetzen', 2, 'Löse mit dem Einsetzungsverfahren: I: x = 2y   II: 3x − 4y = 10. Gib die Lösung an.', 'x = □; y = □', [10, 5], ['2 * 5', '10 / 2'],
     'x = 2y in II: 6y − 4y = 10 ⇔ y = 5. x = 2 · 5 = 10.', 'Ersetze x in II durch 2y.', _HZ)
SW.l('einsetzen', 2, 'Löse mit dem Einsetzungsverfahren: I: y = 0,5x + 1   II: 2x − 2y = 4. Gib die Lösung an.', 'x = □; y = □', [6, 4], ['6', '0.5 * 6 + 1'],
     '2x − 2(0,5x + 1) = 4 ⇔ 2x − x − 2 = 4 ⇔ x = 6. y = 3 + 1 = 4.', 'Setze den Term für y in Klammern ein.', _HZ)
SW.z('einsetzen', 3, 'Ein Vater ist dreimal so alt wie seine Tochter. Zusammen sind sie 52 Jahre alt. Wie alt ist die Tochter?', 13, '52 / 4',
     'I: v = 3t, II: v + t = 52. Einsetzen: 3t + t = 52 ⇔ t = 13. Der Vater ist 39.', 'Stelle zwei Gleichungen auf. Eine ist schon nach v aufgelöst.', einheit='Jahre', art='P')
SW.l('einsetzen', 3, 'Löse: I: 2x + 3y = 7   II: x − 2y = 0. Gib die Lösung an.', 'x = □; y = □', [2, 1], ['2', '1'],
     'II umstellen: x = 2y. In I: 4y + 3y = 7 ⇔ y = 1. x = 2. Probe: 4 + 3 = 7.', 'Stelle zuerst die einfachere Gleichung nach x um.', _HZ, art='P')
SW.a('einsetzen', 3, 'Löse: I: y = 3x − 2   II: 6x − 2y = 4. Wie viele Lösungen gibt es?', 'unendlich viele', ['keine', 'genau eine: (0 | −2)', 'genau eine: (1 | 1)'],
     'Einsetzen: 6x − 2(3x − 2) = 4 ⇔ 6x − 6x + 4 = 4 ⇔ 4 = 4. Immer wahr: Beide Gleichungen beschreiben dieselbe Gerade.',
     'Rechne zu Ende. Was bleibt übrig, wenn x wegfällt?', art='K')
SW.a('einsetzen', 3, 'Ben setzt I: y = 2x + 1 in II: 4x − 3y = 7 ein und schreibt: 4x − 3 · 2x + 1 = 7. Was stimmt?', 'Falsch: 2x + 1 muss in Klammern. Richtig ist x = −5.',
     ['Richtig; es folgt x = −3.', 'Falsch: Man muss y in I einsetzen.', 'Falsch: Richtig ist x = 5.'],
     'Richtig: 4x − 3(2x + 1) = 7 ⇔ 4x − 6x − 3 = 7 ⇔ −2x = 10 ⇔ x = −5, y = −9. Ohne Klammer wird nur 2x mit 3 multipliziert.',
     'Was passiert mit der 1, wenn man −3 · (2x + 1) rechnet?', art='K')

# gleichsetzen
SW.l('gleichsetzen', 2, 'Löse mit dem Gleichsetzungsverfahren: I: x = 3y − 1   II: x = y + 5. Gib die Lösung an.', 'x = □; y = □', [8, 3], ['3 + 5', '6 / 2'],
     '3y − 1 = y + 5 ⇔ 2y = 6 ⇔ y = 3. x = 3 + 5 = 8.', 'Hier ist zweimal x = … gegeben. Setze die rechten Seiten gleich.', _HZ)
SW.l('gleichsetzen', 2, 'Löse mit dem Gleichsetzungsverfahren: I: y = 0,5x + 3   II: y = −0,5x + 1. Gib die Lösung an.', 'x = □; y = □', [-2, 2], ['-2', '0.5 * (-2) + 3'],
     '0,5x + 3 = −0,5x + 1 ⇔ x = −2. y = −1 + 3 = 2.', 'Setze die Terme gleich und sammle x links.', _HZ)
SW.z('gleichsetzen', 3, 'Handytarif A: 9 € im Monat plus 0,05 € pro Minute. Tarif B: 0,11 € pro Minute ohne Grundgebühr. Bei wie vielen Minuten kosten beide gleich viel?', 150, '9 / 0.06',
     'A: y = 0,05x + 9, B: y = 0,11x. Gleichsetzen: 0,05x + 9 = 0,11x ⇔ 9 = 0,06x ⇔ x = 150.', 'Stelle für jeden Tarif y = … auf.', einheit='min', art='P')
SW.z('gleichsetzen', 3, 'Zwei Wanderer sind 18 km voneinander entfernt und gehen gleichzeitig aufeinander zu: A mit 4 km/h, B mit 5 km/h. Nach wie vielen Stunden treffen sie sich?', 2, '18 / 9',
     'Ort von A ab Start A: s = 4t. Ort von B: s = 18 − 5t. Gleichsetzen: 4t = 18 − 5t ⇔ 9t = 18 ⇔ t = 2.', 'Miss beide Orte vom Startpunkt von A aus.', einheit='h', art='P')
SW.a('gleichsetzen', 3, 'Löse: I: 2y = 4x + 6   II: 3y = 6x − 3. Was ergibt sich?', 'keine Lösung', ['genau eine Lösung', 'unendlich viele Lösungen', 'x = 0, y = 3'],
     'Nach y auflösen: I: y = 2x + 3, II: y = 2x − 1. Gleichsetzen: 2x + 3 = 2x − 1 ⇔ 3 = −1. Falsch – keine Lösung (parallele Geraden).',
     'Löse zuerst beide Gleichungen nach y auf.', art='K')
SW.z('gleichsetzen', 3, 'Für welchen Wert von t schneiden sich y = 2x + t und y = −x + 7 an der Stelle x = 3?', -2, '(-3 + 7) - 2 * 3',
     'Die zweite Gerade hat bei x = 3 den Wert 4. Also 2 · 3 + t = 4 ⇔ t = −2.', 'Berechne den y-Wert des Schnittpunkts mit der Geraden ohne t.', art='K')

# addition
SW.l('addition', 2, 'Löse mit dem Additionsverfahren: I: 2x + 3y = 12   II: 2x − y = 4. Gib die Lösung an.', 'x = □; y = □', [3, 2], ['3', '2'],
     'I − II: 4y = 8 ⇔ y = 2. In II: 2x − 2 = 4 ⇔ x = 3.', 'Ziehe II von I ab, dann fällt x weg.', _HZ)
SW.l('addition', 2, 'Löse mit dem Additionsverfahren: I: 3x + 2y = 7   II: x − 2y = 5. Gib die Lösung an.', 'x = □; y = □', [3, -1], ['12 / 4', '(3 - 5) / 2'],
     'I + II: 4x = 12 ⇔ x = 3. In II: 3 − 2y = 5 ⇔ y = −1.', '2y und −2y sind schon Gegenzahlen.', _HZ)
SW.l('addition', 3, 'Löse: I: 3x + 4y = 10   II: 2x − 3y = 1. Gib die Lösung an.', 'x = □; y = □', [2, 1], ['34 / 17', '(10 - 6) / 4'],
     'I · 3 und II · 4: 9x + 12y = 30 und 8x − 12y = 4. Addieren: 17x = 34 ⇔ x = 2. In I: 6 + 4y = 10 ⇔ y = 1.', 'Multipliziere beide Gleichungen, bis bei y Gegenzahlen stehen.', _HZ, art='P')
SW.l('addition', 3, 'Löse: I: 0,5x + 0,25y = 2   II: x − y = 1. Gib die Lösung an.', 'x = □; y = □', [3, 2], ['9 / 3', '3 - 1'],
     'I · 4: 2x + y = 8. Plus II: 3x = 9 ⇔ x = 3. In II: 3 − y = 1 ⇔ y = 2.', 'Mache zuerst die Kommazahlen in I zu ganzen Zahlen.', _HZ, art='P')
SW.z('addition', 3, 'I: 4x + 6y = 10   II: 3x − 2y = 1. Mit welcher Zahl muss man II multiplizieren, damit beim Addieren y wegfällt?', 3, '6 / 2',
     'In I steht 6y, in II −2y. −2y · 3 = −6y ist die Gegenzahl von 6y.', 'Welche Zahl macht aus −2y die Gegenzahl von 6y?', art='K')
SW.l('addition', 3, 'Löse geschickt: I: 37x + 63y = 163   II: 63x + 37y = 137. Gib die Lösung an.', 'x = □; y = □', [1, 2], ['(3 - 1) / 2', '(3 + 1) / 2'],
     'I + II: 100x + 100y = 300 ⇔ x + y = 3. II − I: 26x − 26y = −26 ⇔ x − y = −1. Daraus x = 1, y = 2.', 'Addiere I und II. Ziehe dann I von II ab. Was fällt auf?', _HZ, art='K')

# verfahren
SW.a('verfahren', 2, 'Welches Verfahren ist für I: x = 4 − 2y   II: 3x + y = 7 am geschicktesten?', 'Einsetzungsverfahren', ['Gleichsetzungsverfahren', 'Additionsverfahren'],
     'I ist schon nach x aufgelöst. Den Term 4 − 2y setzt man direkt in II ein.', 'Ist eine Gleichung schon nach einer Variablen aufgelöst?')
SW.a('verfahren', 2, 'Welches Verfahren ist für I: 2x + y = 5   II: 2x − 3y = 1 am geschicktesten?', 'Additionsverfahren', ['Gleichsetzungsverfahren', 'Einsetzungsverfahren'],
     'Beide Gleichungen haben 2x. Zieht man II von I ab, fällt x sofort weg.', 'Stehen bei einer Variablen gleiche Zahlen?')
SW.a('verfahren', 3, 'Bei I: y = 3x − 1   II: y = 3x + 2 sagt Lea: „Ich muss gar nicht rechnen.“ Warum?', 'Gleiche Steigung, verschiedener Achsenabschnitt: keine Lösung.',
     ['Weil beide Gleichungen mit y beginnen.', 'Weil die Lösung x = 0 sofort sichtbar ist.', 'Weil die Geraden identisch sind.'],
     'Beide Geraden haben die Steigung 3, schneiden die y-Achse aber bei −1 und 2. Sie sind parallel und verschieden – das System hat keine Lösung.',
     'Vergleiche Steigungen und Achsenabschnitte.', art='P')
SW.a('verfahren', 3, 'I: 5x + 3y = 1   II: 2x − 4y = 6. Welcher erste Schritt erzeugt beim Additionsverfahren Gegenzahlen vor x?', 'I · 2 und II · (−5)',
     ['I · 2 und II · 5', 'I · (−2) und II · (−5)', 'I · 5 und II · 2'],
     'I · 2: 10x + …, II · (−5): −10x + … – Gegenzahlen. Bei II · 5 stünden zweimal +10x, beim Addieren würde x nicht wegfallen.', 'Gegenzahlen haben gleichen Betrag, aber verschiedenes Vorzeichen.', art='P')
SW.z('verfahren', 3, 'I: x + y = 10   II: x − y = 2   III: 2x + 3y = c. Für welches c hat das System aus allen drei Gleichungen eine Lösung?', 24, '2 * 6 + 3 * 4',
     'Aus I und II (addieren): 2x = 12, x = 6, y = 4. III muss für (6 | 4) gelten: c = 12 + 12 = 24.', 'Löse zuerst I und II. Die Lösung muss auch III erfüllen.', art='K')
SW.l('verfahren', 3, 'I: 3x + 5y = 21   II: 5x + 3y = 19. Addiere und subtrahiere die Gleichungen geschickt. Was ergibt sich für x + y und x − y?', 'x + y = □; x − y = □', [5, -1],
     ['40 / 8', '-2 / 2'], 'I + II: 8x + 8y = 40 ⇔ x + y = 5. II − I: 2x − 2y = −2 ⇔ x − y = −1. Daraus x = 2, y = 3.', 'Bei vertauschten Zahlen hilft Addieren und Subtrahieren.', _HZ, art='K')

# loesbarkeit
SW.a('loesbarkeit', 2, 'Wie viele Lösungen hat I: x − y = 2   II: y − x = −2?', 'unendlich viele Lösungen', ['keine Lösung', 'genau eine Lösung'],
     'II mal (−1): x − y = 2. Das ist Gleichung I. Beide Gleichungen beschreiben dieselbe Gerade.', 'Multipliziere II mit −1 und vergleiche.')
SW.a('loesbarkeit', 2, 'Wie viele Lösungen hat I: y = 0,5x + 1   II: x − 2y = 4?', 'keine Lösung', ['unendlich viele Lösungen', 'genau eine Lösung'],
     'II nach y: −2y = −x + 4 ⇔ y = 0,5x − 2. Gleiche Steigung 0,5, verschiedene Achsenabschnitte: parallel, keine Lösung.', 'Löse II nach y auf.')
SW.z('loesbarkeit', 3, 'I: 3x − y = 4   II: 6x − 2y = □. Welche Zahl muss im Kästchen stehen, damit das System unendlich viele Lösungen hat?', 8, '2 * 4',
     'II muss das Doppelte von I sein: 6x − 2y = 8. Bei jeder anderen Zahl wären die Geraden parallel und verschieden.', 'Womit wurde die linke Seite von I multipliziert?', art='P')
SW.a('loesbarkeit', 3, 'Für welche Werte von a hat I: ax + 2y = 6   II: 3x + y = 5 genau eine Lösung?', 'für alle a ≠ 6', ['nur für a = 6', 'für alle a', 'für kein a'],
     'II · 2: 6x + 2y = 10. Für a = 6 wären die Geraden parallel (6 ≠ 10, keine Lösung). Für jedes andere a schneiden sie sich in genau einem Punkt.',
     'Bringe y in beiden Gleichungen auf dieselbe Zahl. Wann sind die Geraden parallel?', art='P')
SW.a('loesbarkeit', 3, 'Ein lineares Gleichungssystem hat die Lösungen (1 | 2) und (3 | 6). Wie viele Lösungen hat es?', 'unendlich viele', ['genau zwei', 'genau eine', 'keine'],
     'Zwei Geraden haben entweder keinen, genau einen oder unendlich viele gemeinsame Punkte. Zwei gemeinsame Punkte gibt es nur, wenn die Geraden gleich sind.',
     'Wie viele Punkte können zwei Geraden gemeinsam haben?', art='K')
SW.a('loesbarkeit', 3, 'Wie viele Lösungen hat das System aus I: x + y = 5, II: 2x + 2y = 10 und III: x − y = 1?', 'genau eine', ['keine', 'unendlich viele', 'genau zwei'],
     'I und II beschreiben dieselbe Gerade. Mit III: x + y = 5 und x − y = 1 ergibt x = 3, y = 2. Genau eine Lösung (3 | 2).', 'Vergleiche I und II zuerst.', art='K')

# sachaufgabe
SW.z('sachaufgabe', 2, 'Kinokarten kosten für Erwachsene 9 € und für Kinder 6 €. 7 Personen zahlen zusammen 51 €. Wie viele Erwachsene sind dabei?', 3, '(51 - 6 * 7) / 3',
     'e + k = 7, 9e + 6k = 51. Mit k = 7 − e: 9e + 42 − 6e = 51 ⇔ 3e = 9 ⇔ e = 3.', 'Stelle eine Gleichung für die Anzahl und eine für den Preis auf.', einheit='Erwachsene')
SW.z('sachaufgabe', 2, 'Die Summe zweier Zahlen ist 40. Die eine ist dreimal so groß wie die andere. Wie heißt die kleinere Zahl?', 10, '40 / 4',
     'a + b = 40, a = 3b. 3b + b = 40 ⇔ b = 10. Die Zahlen sind 30 und 10.', 'Nenne die kleinere Zahl b. Dann ist die größere 3b.')
SW.z('sachaufgabe', 3, 'Klasse A kauft 3 Pizzen und 5 Getränke für 37 €. Klasse B zahlt für 2 Pizzen und 8 Getränke 34 €. Was kostet eine Pizza?', 9, '17 - 4 * 2',
     '3p + 5g = 37 und 2p + 8g = 34 ⇔ p + 4g = 17. p = 17 − 4g in I: 51 − 12g + 5g = 37 ⇔ g = 2. p = 9.', 'Teile die zweite Gleichung zuerst durch 2.', einheit='€', art='P')
SW.z('sachaufgabe', 3, 'Eine Mutter ist 26 Jahre älter als ihr Sohn. In 4 Jahren ist sie dreimal so alt wie er. Wie alt ist der Sohn heute?', 9, '(26 + 4 - 12) / 2',
     'm = s + 26 und m + 4 = 3(s + 4). Einsetzen: s + 30 = 3s + 12 ⇔ 18 = 2s ⇔ s = 9. Probe: Mutter 35, in 4 Jahren 39 = 3 · 13.',
     'In 4 Jahren sind beide 4 Jahre älter – auch der Sohn.', einheit='Jahre', art='P')
SW.z('sachaufgabe', 3, 'Ein Bleistift und ein Heft kosten zusammen 2,30 €. Das Heft kostet 1,10 € mehr als der Bleistift. Was kostet der Bleistift?', 0.6, '(2.30 - 1.10) / 2',
     'b + h = 2,30 und h = b + 1,10. Also 2b + 1,10 = 2,30 ⇔ b = 0,60 €. Nicht 1,20 €: Dann wäre das Heft 2,30 € und alles zusammen 3,50 €.',
     'Stelle zwei Gleichungen auf, statt zu raten. Mach die Probe.', einheit='€', art='K')
SW.z('sachaufgabe', 3, 'Eine zweistellige Zahl hat die Quersumme 11. Vertauscht man ihre Ziffern, wird die Zahl um 27 größer. Wie heißt die Zahl?', 47, '10 * 4 + 7',
     'Zehner a, Einer b: a + b = 11 und (10b + a) − (10a + b) = 27 ⇔ 9b − 9a = 27 ⇔ b − a = 3. Also b = 7, a = 4: Zahl 47 (74 − 47 = 27).',
     'Schreibe die Zahl als 10a + b und die vertauschte als 10b + a.', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('gleichungen.lgs2', 13_8_6)
# c) Grammatik in der Frage („mit Cashewkerne“)
BF.ersetze('sachaufgabe', 'Ein Händler mischt Erdnüsse zu 10 € pro kg mit Cashewkerne zu 16 € pro kg. Er erhält 13 kg Mischung im Wert von 178 €. Wie viel kg der billigeren Sorte verwendet er?',
           BF.Z('Ein Händler mischt Erdnüsse zu 10 € pro kg mit Cashewkernen zu 16 € pro kg. Er erhält 13 kg Mischung im Wert von 178 €. Wie viel kg der billigeren Sorte verwendet er?',
                5, '(16 * 13 - 178) / (16 - 10)',
                'I: x + y = 13, II: 10x + 16y = 178. y = 13 − x: 10x + 208 − 16x = 178 → −6x = −30 → x = 5. Teurere Sorte: y = 13 − 5 = 8.',
                'Eine Gleichung für die Masse, eine für den Preis.', einheit='kg'))
# a) gleicher Typ wie Stufe 2
BF.stufe('sachaufgabe', 'Eine Eintrittskarte kostet für Erwachsene 15 €, für Kinder 8 €. Eine Gruppe aus 45 Personen zahlt 563 €. Wie viele Kinder sind dabei?', 2)
BF.stufe('sachaufgabe', 'Eine Eintrittskarte kostet für Erwachsene 8 €, für Kinder 4,50 €. Eine Gruppe aus 55 Personen zahlt 303,50 €. Wie viele Kinder sind dabei?', 2)
BF.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: −2x + y = −3   II: y = x − 3 am Schnittpunkt ab.', 2)
BF.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: y = x − 2   II: y = −x am Schnittpunkt ab.', 2)

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('gleichungen.lgs2', 19_8_11)
# Gleiche Aufgabenart wie die Stufe darunter → umgestuft
DSX.stufe('pruefen', 'Gegeben: I: −4x − 3y = −15   II: −x + 4y = 20. Welches Zahlenpaar ist die Lösung?', 1)
DSX.stufe('pruefen', 'Gegeben: I: −5x + 6y = 16   II: x + y = 10. Welches Zahlenpaar ist die Lösung?', 1)
DSX.stufe('pruefen', 'Gegeben: I: 2x − 6y = 20   II: 2x − 3y = 8. Welches Zahlenpaar ist die Lösung?', 1)
DSX.stufe('pruefen', 'Gegeben: I: 4x − y = 24   II: 4x − 4y = 24. Welches Zahlenpaar ist die Lösung?', 1)
DSX.stufe('pruefen', 'Gegeben: I: −6x − 4y = −38   II: 5x − 6y = 13. Welches Zahlenpaar ist die Lösung?', 1)
DSX.stufe('pruefen', 'Gegeben: I: −x − 3y = −2   II: 2x + y = 4. Welches Zahlenpaar ist die Lösung?', 1)
DSX.stufe('pruefen', 'Gegeben: I: −4x − 3y = −2   II: −3x − 6y = −24. Ist (6 | −4) eine Lösung?', 2)
DSX.stufe('pruefen', 'Gegeben: I: −4x + 5y = −58   II: 6x − 3y = 60. Ist (−6 | 7) eine Lösung?', 2)
DSX.stufe('pruefen', 'Gegeben: I: −2x − 3y = −4   II: 4x − y = 36. Ist (8 | −4) eine Lösung?', 2)
DSX.stufe('pruefen', 'Gegeben: I: x − 2y = −13   II: 5x − y = −11. Ist (6 | −1) eine Lösung?', 2)
DSX.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: y = −3x − 1   II: y = −x + 1 am Schnittpunkt ab.', 1)
DSX.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: y = −x + 4   II: y = 2x + 4 am Schnittpunkt ab.', 1)
DSX.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: −2x + y = 5   II: y = 3x + 5 am Schnittpunkt ab.', 1)
DSX.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: y = 3x − 1   II: 2x + y = 4 am Schnittpunkt ab.', 1)
DSX.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: −2x + y = −3   II: y = x − 3 am Schnittpunkt ab.', 1)
DSX.stufe('grafisch', 'Lies die Lösung des Gleichungssystems I: y = x − 2   II: y = −x am Schnittpunkt ab.', 1)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = x + 2   II: 6x + y = −5. Gib die Lösung an.', 1)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = −x + 7   II: 4x − 3y = −49. Gib die Lösung an.', 1)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = 5x + 2   II: x − 2y = 23. Gib die Lösung an.', 1)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = 5x − 5   II: −4x − 2y = 80. Gib y an.', 1)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = −2x − 9   II: −x − 4y = 57. Gib die Lösung an.', 1)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = −x + 3   II: −2x + 4y = −6. Gib die Lösung an.', 1)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: x = 3y + 6   II: 2x − 5y = 11. Gib die Lösung an.', 2)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = 5x − 1   II: x + 4y = 59. Gib die Lösung an.', 2)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: y = −4x − 7   II: −3x + 2y = −91. Gib die Lösung an.', 2)
DSX.stufe('einsetzen', 'Löse mit dem Einsetzungsverfahren: I: x = −2y − 9   II: x + y = −16. Gib die Lösung an.', 2)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = 3x − 4   II: y = −x + 28. Gib y an.', 1)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = −2x + 5   II: y = 5x − 30. Gib die Lösung an.', 1)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = x − 8   II: y = 4x + 10. Gib die Lösung an.', 1)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = −4x − 4   II: y = x − 19. Gib die Lösung an.', 1)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = −3x − 5   II: y = −4x − 1. Gib x an.', 1)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = −5x + 3   II: y = 2x + 24. Gib die Lösung an.', 1)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = x − 6   II: 9x + 3y = −30. Gib die Lösung an.', 2)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = −2x + 5   II: 6x − 2y = −50. Gib die Lösung an.', 2)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = −3x + 4   II: 10x − 2y = −40. Gib die Lösung an.', 2)
DSX.stufe('gleichsetzen', 'Löse mit dem Gleichsetzungsverfahren: I: y = −x + 1   II: −2x + 2y = 18. Gib die Lösung an.', 2)
DSX.stufe('addition', 'Löse mit dem Additionsverfahren: I: −4x − 3y = 11   II: −2x + y = −7. Gib die Lösung an.', 2)
DSX.stufe('addition', 'Löse mit dem Additionsverfahren: I: −6x + 2y = 2   II: 3x + y = −5. Gib die Lösung an.', 2)
DSX.stufe('addition', 'Löse mit dem Additionsverfahren: I: −6x + 3y = 24   II: −3x − 2y = −9. Gib die Lösung an.', 2)
DSX.stufe('addition', 'Löse mit dem Additionsverfahren: I: 6x − 6y = 18   II: 6x − y = −2. Gib die Lösung an.', 2)
DSX.stufe('addition', 'Löse mit dem Additionsverfahren: I: 5x + 4y = 63   II: −5x − 2y = −49. Gib x an.', 1)
DSX.stufe('verfahren', 'Welches Verfahren ist für I: 3x + 10y = 5   II: 2x − 5y = −20 am geschicktesten?', 2)
DSX.stufe('verfahren', 'Welches Verfahren ist für I: 5x + 2y = −9   II: −4x − 2y = 6 am geschicktesten?', 1)
DSX.stufe('loesbarkeit', 'Ein Gleichungssystem hat keine Lösung. Was bedeutet das für die beiden Geraden?', 2)
DSX.stufe('loesbarkeit', 'Wie viele Lösungen hat I: −3x − y = 5   II: 5x + 2y = 2?', 2)
# grafisch: Stufe 2 braucht eigene Gedanken (Umstellen zum Zeichnen, Probe)
DSX.neu('grafisch', 2, DSX.A(
    'Du willst I: 2x + y = 7 und II: x − y = −1 zeichnen. Welche Geraden zeichnest du?',
    'y = −2x + 7 und y = x + 1', ['y = 2x + 7 und y = x − 1', 'y = −2x + 7 und y = −x − 1', 'y = 2x − 7 und y = x + 1'],
    'I: 2x auf die andere Seite, y = −2x + 7. II: x − y = −1, also y = x + 1.', 'Stelle jede Gleichung nach y um.'))
DSX.neu('grafisch', 2, DSX.A(
    'Tim liest am Bild den Schnittpunkt (2 | 3) ab. Das System ist I: x + 2y = 8, II: 3x − y = 4. Was zeigt die Probe?',
    'I stimmt, II nicht: Tim hat ungenau abgelesen.', ['Beide stimmen: (2 | 3) ist die Lösung.', 'II stimmt, I nicht.', 'Keine Gleichung stimmt.'],
    'I: 2 + 2 · 3 = 8 ✓. II: 3 · 2 − 3 = 3, nicht 4 ✗. Ein abgelesener Punkt ist nur dann die Lösung, wenn beide Gleichungen stimmen.', 'Setze (2 | 3) in beide Gleichungen ein.'))
# sachaufgabe: zweimal wiederholte Einkleidung ersetzt
DSX.ersetze('sachaufgabe', 'Eine Eintrittskarte kostet für Erwachsene 8 €, für Kinder 4,50 €. Eine Gruppe aus 55 Personen zahlt 303,50 €. Wie viele Kinder sind dabei?', DSX.Z(
    'Ein Rechteck hat den Umfang 30 cm. Es ist doppelt so lang wie breit. Wie lang ist es?', 10, '10',
    'x = Länge, y = Breite: x = 2y und 2x + 2y = 30. Einsetzen: 4y + 2y = 30, also y = 5 und x = 10. Das Rechteck ist 10 cm lang.',
    'Eine Gleichung für „doppelt so lang“, eine für den Umfang.', einheit='cm'))
DSX.ersetze('sachaufgabe', 'Auf einem Hof leben Hühner und Kaninchen, zusammen 37 Tiere mit 110 Beinen. Wie viele Kaninchen sind es?', DSX.Z(
    'Eine Jugendherberge hat 40 Zimmer, nur Doppel- und Einzelzimmer, mit zusammen 64 Betten. Wie viele Doppelzimmer gibt es?', 24, '64 - 40',
    'x Doppelzimmer, y Einzelzimmer: x + y = 40 und 2x + y = 64. Subtrahieren: x = 24. Es gibt 24 Doppelzimmer (und 16 Einzelzimmer).',
    'Eine Gleichung für die Zimmer, eine für die Betten.'))
DSX.stufen('pruefen', 'S1 und S2 dieselbe Frage „Welches Paar ist die Lösung?“; S3 nur „Ist (a | b) eine Lösung?“',
           'S1 Lösung auswählen; S2 nur eine Gleichung erfüllt, Kommazahl, „Ist (a | b) Lösung?“ mit Teilantwort; S3 Parameter c, Text → System, (a | 2a), Lösungen zählen')
DSX.stufen('grafisch', 'S1 und S2 dieselbe Ableseaufgabe', 'S1 ablesen; S2 beide Gleichungen erst umstellen, Umstellen zum Zeichnen, Probe am abgelesenen Punkt, Lösungsanzahl am Bild; S3 Ablesefehler finden, Bruch-Schnittpunkt, System zum Bild, Gerade ohne Lösung')
DSX.stufen('einsetzen', 'S1–S3 dieselbe Rechnung, nur andere Zahlen', 'S1 y = … einsetzen; S2 erst x = … oder Kommazahl; S3 Sachaufgabe, selbst umstellen, unendlich viele Lösungen, Klammerfehler finden')
DSX.stufen('gleichsetzen', 'S1–S3 dieselbe Rechnung, nur andere Zahlen', 'S1 zweimal y = …; S2 x = …, Kommazahlen, II erst umstellen; S3 Tarifvergleich, Treffpunkt, keine Lösung, Parameter t')
DSX.stufen('addition', 'S2 und S3 teils dieselbe Rechnung', 'S1 Gegenzahlen schon da; S2 eine Gleichung multiplizieren; S3 beide multiplizieren, Kommazahlen, Faktor finden, geschickt addieren')
DSX.stufen('verfahren', 'S3 enthielt eine reine Auswahlfrage', 'S1 Form erkennen; S2 Einsetzen, x = …, Gegenzahlen erst herstellen; S3 begründen, warum ein Verfahren umständlich ist, Faktoren wählen, drei Gleichungen')
DSX.stufen('loesbarkeit', 'S3 enthielt S2-Aufgaben', 'S1 y = …-Form vergleichen; S2 Vielfache erkennen, Bedeutung am Bild; S3 Parameter, Kästchen, zwei Lösungen ⇒ unendlich viele, drei Gleichungen')
DSX.stufen('sachaufgabe', 'S2 wiederholte Eintritt- und Hühner-Aufgaben', 'S1 Standard-Einkleidung; S2 Kommabeträge, neue Einkleidungen (Rechteck, Zimmer); S3 Mischung, Alter, Ziffern, Bleistift-Falle')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Grundidee', ['pruefen', 'grafisch']), ('Lösungsverfahren', ['einsetzen', 'gleichsetzen', 'addition', 'verfahren']),
          ('Verstehen und Anwenden', ['loesbarkeit', 'sachaufgabe'])],
         'Lineare Gleichungssysteme mit zwei Unbekannten rechnerisch lösen, Lösbarkeit begründen, das passende Verfahren wählen und Sachaufgaben lösen.',
         ['Lösung = Zahlenpaar (x | y), das beide Gleichungen erfüllt.',
          'Gleichsetzen, Einsetzen oder Addieren – Ziel: eine Gleichung mit nur einer Variablen.',
          'Falsche Aussage (0 = 5): keine Lösung. Wahre Aussage (0 = 0): unendlich viele Lösungen.'],
         offen=['Prüfvorschlag „grafisch lösen“ (Karte pruefen) ist in der neuen Karte „grafisch“ umgesetzt.'])
