"""Vierundzwanzigste Runde (Zweig aufloesen), Teil B: neue Lernkarten in bestehenden Flügen.

Aus doppelt-rsib.md Teil 3a (statt vier neuer Themen) und Teil 3b (Dualsystem):
  abbildungen.aehnlichkeit  + bildgerade   „Bildgerade und Bildparabel“      (RS M9 LB2 I)  Vertiefung
  abbildungen.aehnlichkeit  + schwerpunkt  „Schwerpunkt eines Dreiecks“      (RS M9 LB2 I)  Vertiefung
  trigo.rechtwinklig        + schnittwinkel „Schnittwinkel zweier Geraden“   (RS M10 LB1 I) Vertiefung
  trigo.allgemein           + additionstheoreme „Additionstheoreme“          (RS M10 LB1 I) Vertiefung
  abbildungen.matrizen      + abstand      „Abstand Punkt–Gerade“            (RS M10 LB1 I) Pflicht im (freiwilligen) RS-Flug
  zahlen.natuerlich         + dualsystem   „Zahlen im Zweiersystem“          (RS M5 1.2)    Pflicht

Jede Lösung rechnet dieses Programm (Feld c bzw. Lückenausdrücke werden beim Bauen nachgerechnet). Gerundete Winkel und
Sinuswerte: exakter Wert aus math, im Ausdruck c als round(<Wert>, n) wie in den anderen Trigonometrie-Flügen.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bereinigen import karte_neu, neu, knobel, pool  # noqa: E402
from _befunde import _z as Z, _l as L  # noqa: E402
from _stufen_kl5 import A  # noqa: E402


def ohne_tipp(a):
    a = dict(a); a.pop('h', None); return a


def zt(x):
    """Zahl in deutscher Schreibweise (Dezimalkomma, Minuszeichen, Tausender mit Leerzeichen)."""
    if isinstance(x, float) and x.is_integer(): x = int(x)
    s = f'{abs(x):,}'.replace(',', ' ') if isinstance(x, int) else str(abs(x)).replace('.', ',')
    return ('−' if x < 0 else '') + s


def karte_ops(thema_lz, abschnitt, etappe, tf, nach, vertiefung, uebungen, knobels, test, korrektur, sicherung):
    lz = thema_lz
    ops = [karte_neu(lz, abschnitt, etappe, tf, nach=nach, vertiefung=vertiefung)]
    ops += [neu(lz, g, a) for g, a in uebungen]
    ops += [knobel(lz, a) for a in knobels]
    ops += [pool(lz, 'test', ohne_tipp(test))]
    ops += [pool(lz, 'korrektur', ohne_tipp(a)) for a in korrektur]
    ops += [pool(lz, 'sicherung', ohne_tipp(a)) for a in sicherung]
    return ops


# =====================================================================================================================
# 1) Dualsystem – zahlen.natuerlich (Kl. 5), nach roemisch_system. Ohne Potenzschreibweise (Potenzen kommen erst später in Kl. 5),
#    ohne Teilen mit Rest: Umrechnen durch Abziehen der größten passenden Stellenwerte.
# =====================================================================================================================
def dual(n): return format(n, 'b')


def dual_c(s):
    """Rechenausdruck für den Wert einer Zweierzahl, z. B. '1*16 + 0*8 + 1*4 + 1*2 + 0*1'."""
    k = len(s)
    return ' + '.join(f'{z}*{2 ** (k - 1 - i)}' for i, z in enumerate(s))


def dual_w(s):
    k = len(s)
    teile = [2 ** (k - 1 - i) for i, z in enumerate(s) if z == '1']
    return ' + '.join(zt(t) for t in teile), sum(teile)


def zu_dual_w(n):
    rest, schritte = n, []
    while rest:
        w = 1 << (rest.bit_length() - 1)
        schritte.append(f'{zt(rest)} − {zt(w)} = {zt(rest - w)}')
        rest -= w
    return 'Ziehe immer den größten passenden Stellenwert ab: ' + '; '.join(schritte) + f'. Eine 1 an diesen Stellen, sonst 0: {dual(n)}.'


def W_Z(text, s, h):
    summe_text, wert = dual_w(s)
    return Z(text, wert, dual_c(s), f'Stellenwerte unter den Einsen addieren: {summe_text} = {zt(wert)}.', h)


def T(text, antwort, w, h):
    """Antworttyp text: Zweierzahlen als Ziffernfolge (eine Zahl-Antwort würde die App mit Tausender-Leerzeichen anzeigen)."""
    assert set(antwort) <= set('01') and len(w) >= 15
    return {'y': 'text', 'f': {'text': text}, 'o': {'text': antwort}, 'w': w, 'h': h}


def W_D(text, n, h, vorspann=''):
    return T(text, dual(n), vorspann + zu_dual_w(n), h)


H_LESEN = 'Schreibe die Stellenwerte 1, 2, 4, 8, … von rechts nach links über die Ziffern.'
H_SCHREIBEN = 'Welcher ist der größte Stellenwert (1, 2, 4, 8, 16, …), der noch hineinpasst?'

DUAL_KARTE = {
    'titel': 'Zahlen im Zweiersystem',
    'einstieg': 'Ein Computer kennt nur zwei Zeichen: Strom an (1) oder Strom aus (0). Trotzdem kann er jede Zahl schreiben. '
                'Er benutzt das ⟦Zweiersystem⟧.',
    'woerter': [['Zweiersystem', 'ein Stellenwertsystem mit nur den Ziffern 0 und 1; man sagt auch Dualsystem'],
                ['Stellenwerte', 'im Zweiersystem von rechts 1, 2, 4, 8, 16, …: jede Stelle ist doppelt so viel wert'],
                ['Zweierzahl', 'eine Zahl, die im Zweiersystem geschrieben ist, z. B. 10110']],
    'bild': {'typ': 'stellentafel', 'stellen': ['16', '8', '4', '2', '1'], 'ziffern': [1, 0, 1, 1, 0]},
    'schritte': [{'text': 'Die Zweierzahl 10110 steht in der Tafel.'},
                 {'text': 'Die Stellenwerte verdoppeln sich von rechts nach links: 1, 2, 4, 8, 16.'},
                 {'text': 'Eine 1 steht bei 16, bei 4 und bei 2.', 'bild': {'markiert': 0}},
                 {'text': 'Zusammen: 16 + 4 + 2 = ⟦22⟧. Die Zweierzahl 10110 ist also 22.'}],
    'fehler': '10110 ist hier nicht zehntausendeinhundertzehn. Im Zweiersystem ist die erste 1 nur ⟦16⟧ wert.',
    'regel': 'Im Zweiersystem gibt es nur ⟦0 und 1⟧. Addiere die Stellenwerte, unter denen eine 1 steht.',
}

DUAL = karte_ops(
    'dualsystem', 'Zahlsysteme', DUAL_KARTE, 'Zahlen im Zweiersystem lesen und schreiben', 'roemisch_system', False,
    [('direkt', W_Z('Welche Zahl ist die Zweierzahl 1011?', '1011', H_LESEN)),
     ('direkt', W_Z('Welche Zahl ist die Zweierzahl 11001?', '11001', H_LESEN)),
     ('erkennen', A('Welche Ziffern gibt es im Zweiersystem?', 'nur 0 und 1', ['0 bis 9', 'nur 1 und 2', '0, 1 und 2'],
                    'Im Zweiersystem hat jede Stelle nur zwei Möglichkeiten: 0 (aus) oder 1 (an).', 'Denke an Strom an und Strom aus.')),
     ('erkennen', Z('Wie viel ist die 1 in der Zweierzahl 100000 wert?', 32, '2*2*2*2*2',
                    'Von rechts: 1, 2, 4, 8, 16, 32. Die 1 steht an der sechsten Stelle von rechts, sie ist 32 wert.', H_LESEN)),
     ('umkehr', W_D('Schreibe die Zahl 13 im Zweiersystem.', 13, H_SCHREIBEN)),
     ('umkehr', W_D('Schreibe die Zahl 20 im Zweiersystem.', 20, H_SCHREIBEN)),
     ('mehrschritt', Z('Rechne die Zweierzahlen 101 und 110 in normale Zahlen um und addiere die beiden Ergebnisse.', 11, '(4 + 1) + (4 + 2)',
                       '101 ist 4 + 1 = 5, 110 ist 4 + 2 = 6. Zusammen 5 + 6 = 11.', 'Rechne jede Zweierzahl einzeln um.')),
     ('mehrschritt', Z('Welche Zahl ist größer: die Zweierzahl 1110 oder die Zweierzahl 10001? Gib die größere als normale Zahl an.', 17,
                       'max(8 + 4 + 2, 16 + 1)', '1110 ist 8 + 4 + 2 = 14. 10001 ist 16 + 1 = 17. Die größere ist 17.',
                       'Mehr Stellen heißt nicht immer mehr Ziffern 1. Rechne beide um.')),
     ('einkleidung', Z('Eine Reihe aus 5 Lampen zeigt eine Zweierzahl: An heißt 1, aus heißt 0. Die Lampen stehen von links für 16, 8, 4, 2 und 1. '
                       'Es leuchten die Lampen für 16, 2 und 1. Welche Zahl zeigt die Reihe?', 19, '16 + 2 + 1',
                       'Leuchtende Lampen: 16 + 2 + 1 = 19. Die Reihe zeigt 10011.', 'Addiere die Werte der leuchtenden Lampen.')),
     ('darstellung', Z('Die Stellentafel zeigt eine Zweierzahl. Welche Zahl ist es?', 37, dual_c('100101'),
                       'Einsen stehen bei 32, 4 und 1: 32 + 4 + 1 = 37.', 'Addiere die Stellenwerte über den Einsen.',
                       grafik={'typ': 'stellentafel', 'stellen': ['32', '16', '8', '4', '2', '1'], 'ziffern': [1, 0, 0, 1, 0, 1]})),
     ('rueckwaerts', T('Zu einer Zahl wird 1 addiert. Das Ergebnis ist im Zweiersystem 10000. Wie heißt die Zahl im Zweiersystem?', dual(16 - 1),
                       '10000 ist 16. Die Zahl davor ist 15 = 8 + 4 + 2 + 1, im Zweiersystem 1111.', 'Rechne 10000 zuerst in eine normale Zahl um.')),
     ('rueckwaerts', Z('Eine Zahl wird verdoppelt. Das Ergebnis ist die Zweierzahl 10110. Welche Zahl war es? Gib sie als normale Zahl an.', 11,
                       '(16 + 4 + 2) // 2', '10110 ist 16 + 4 + 2 = 22. Die Hälfte davon ist 11.', 'Rechne zuerst das Ergebnis um, dann gehe zurück.')),
     ('begruenden', A('Stimmt die Aussage? „Jede Zweierzahl, die auf 0 endet, ist eine gerade Zahl.“',
                      'Ja: Alle Stellenwerte außer der 1 ganz rechts sind gerade Zahlen.',
                      ['Nein, nur wenn sie auch mit 1 anfängt.', 'Nur bei Zweierzahlen mit mehr als drei Stellen.'],
                      'Steht rechts eine 0, addiert man nur Stellenwerte wie 2, 4, 8, 16. Eine Summe gerader Zahlen ist gerade.',
                      'Welche Stellenwerte sind ungerade?')),
     ('begruenden', A('Stimmt die Aussage? „Hängt man an eine Zweierzahl rechts eine 0 an, wird ihr Wert doppelt so groß.“',
                      'Ja: Jede Ziffer rückt eine Stelle nach links und ist dort doppelt so viel wert.',
                      ['Nein, der Wert wird zehnmal so groß.', 'Nein, der Wert bleibt gleich.'],
                      'Beispiel: 101 ist 5, 1010 ist 10. Jede 1 rückt auf einen doppelt so großen Stellenwert.',
                      'Probiere es mit 101 aus.')),
     ('fehler', A('Ein Kind rechnet die Zweierzahl 1001 so um: 1 + 0 + 0 + 1 = 2. Was hat es falsch gemacht?',
                  'Es hat die Stellenwerte vergessen: Die linke 1 ist 8 wert, also 8 + 1 = 9.',
                  ['Es hat richtig gerechnet.', 'Es hätte 1 001 lesen müssen: tausendeins.', 'Es hätte die Ziffern malnehmen müssen.'],
                  'Im Zweiersystem zählt die Stelle: 1001 hat Einsen bei 8 und bei 1. 8 + 1 = 9.', 'Welchen Wert hat die Stelle ganz links?')),
     ('verknuepfen', W_D('Schreibe die römische Zahl XXI im Zweiersystem.', 21, 'Rechne zuerst die römische Zahl um.', vorspann='XXI = 10 + 10 + 1 = 21. ')),
     ('transfer', Z('Eine Anzeige hat 5 Lampen. An heißt 1, aus heißt 0. Welche ist die größte Zahl, die sie als Zweierzahl zeigen kann?', 31,
                    '16 + 8 + 4 + 2 + 1', 'Am meisten ist es, wenn alle Lampen leuchten: 11111 ist 16 + 8 + 4 + 2 + 1 = 31.',
                    'Welche Zweierzahl mit 5 Stellen ist die größte?')),
     ('transfer', Z('Wie viele Stellen hat die Zahl 100 im Zweiersystem?', 7, str(len(dual(100))),
                    'Stellenwerte: 1, 2, 4, 8, 16, 32, 64, 128. 64 passt noch in 100, 128 nicht mehr. Von 1 bis 64 sind es 7 Stellen. '
                    f'(100 ist im Zweiersystem {dual(100)}.)', 'Welcher ist der größte Stellenwert, der noch in 100 passt?'))],
    [Z('Wie viele der Zahlen von 1 bis 31 haben im Zweiersystem genau eine Ziffer 1?', 5, str(sum(1 for n in range(1, 32) if dual(n).count('1') == 1)),
       'Genau eine 1 haben nur die Stellenwerte selbst: 1, 2, 4, 8 und 16. Das sind 5 Zahlen.', 'Wie sieht eine Zweierzahl mit genau einer 1 aus?'),
     Z('Für eine Waage gibt es je ein Gewichtsstück mit 1 g, 2 g, 4 g, 8 g und 16 g. Damit werden genau 27 g abgewogen. Wie viele Gewichtsstücke liegen auf der Waage?',
       4, str(dual(27).count('1')),
       f'27 g: erst 16 g (Rest 11 g), dann 8 g (Rest 3 g), dann 2 g (Rest 1 g), dann 1 g. Das sind 4 Stücke – so viele Einsen hat {dual(27)}.',
       'Die Gewichte sind genau die Stellenwerte des Zweiersystems.')],
    W_Z('Welche Zahl ist die Zweierzahl 1101?', '1101', H_LESEN),
    [W_Z('Welche Zahl ist die Zweierzahl 10101?', '10101', H_LESEN), W_D('Schreibe die Zahl 9 im Zweiersystem.', 9, H_SCHREIBEN),
     W_D('Schreibe die Zahl 26 im Zweiersystem.', 26, H_SCHREIBEN)],
    [W_Z('Welche Zahl ist die Zweierzahl 111?', '111', H_LESEN), W_Z('Welche Zahl ist die Zweierzahl 10010?', '10010', H_LESEN),
     W_Z('Welche Zahl ist die Zweierzahl 11110?', '11110', H_LESEN), W_D('Schreibe die Zahl 12 im Zweiersystem.', 12, H_SCHREIBEN),
     W_D('Schreibe die Zahl 17 im Zweiersystem.', 17, H_SCHREIBEN), W_D('Schreibe die Zahl 28 im Zweiersystem.', 28, H_SCHREIBEN)])


# =====================================================================================================================
# 2) Bildgerade und Bildparabel – abbildungen.aehnlichkeit (Kl. 9), nach streckung. Zentrum immer O(0 | 0).
#    P(x | y) → P′(k · x | k · y). Gerade y = m · x + t → y = m · x + k · t. Parabel y = a · x² → y = (a : k) · x².
# =====================================================================================================================
def bg(m, t, k, text=None):
    tk = t * k
    assert float(tk).is_integer() and float(m).is_integer()
    text = text or f'Die Gerade g: y = {gt(m, t)} wird mit dem Zentrum O(0 | 0) und k = {zt(k)} gestreckt. Gib die Bildgerade an.'
    return L(text, 'y = □x + □', [int(m), int(tk)], [f'{m}', f'{t} * {k}'],
             f'Die Bildgerade ist parallel, die Steigung bleibt {zt(m)}. Der y-Achsenabschnitt wird mal {zt(k)} genommen: {zt(t)} · {zt(k)} = {zt(tk)}. '
             f'Also y = {gt(m, tk)}.', 'Was passiert mit der Steigung, was mit dem y-Achsenabschnitt?', hinweis='Zwei ganze Zahlen, auch negative.')


def gt(m, t):
    m_s = '' if m == 1 else ('−' if m == -1 else zt(m))
    s = f'{m_s}x'
    if t: s += f' + {zt(t)}' if t > 0 else f' − {zt(-t)}'
    return s


BILDGERADE_KARTE = {
    'titel': 'Bildgerade und Bildparabel',
    'einstieg': 'Ein Beamer vergrößert eine Folie mit einer Geraden. Der Beamer steht im Ursprung O. '
                'Die vergrößerte Gerade heißt ⟦Bildgerade⟧. Sie läuft parallel zur alten.',
    'woerter': [['Bildgerade', 'die Gerade, auf der alle gestreckten Punkte einer Geraden liegen'],
                ['Zentrum O', 'der Ursprung (0 | 0) als Zentrum der Streckung'],
                ['Bildparabel', 'die Kurve aus allen gestreckten Punkten einer Parabel']],
    'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [-1, 8], 'graphen': [{'art': 'linear', 'm': 1, 't': 1, 'name': 'g'}]},
    'schritte': [{'text': 'g: y = x + 1 wird von O aus mit k = 3 gestreckt.'},
                 {'text': 'Der Punkt (0 | 1) auf g wird zu (0 | 3).', 'bild': {'punkte': [{'x': 0, 'y': 1, 'name': 'P'}, {'x': 0, 'y': 3, 'name': "P'"}]}},
                 {'text': 'Die Bildgerade ist parallel zu g. Die Steigung bleibt also 1.'},
                 {'text': "Also ⟦g': y = x + 3⟧.", 'bild': {'graphen': [{'art': 'linear', 'm': 1, 't': 1, 'name': 'g'}, {'art': 'linear', 'm': 1, 't': 3, 'name': "g'"}]}}],
    'fehler': 'y = 3x + 3 ist falsch. Die Steigung bleibt gleich, weil Bild und Gerade ⟦parallel⟧ sind. Nur t wird mal 3 genommen.',
    'fehler_bild': {'graphen': [{'art': 'linear', 'm': 1, 't': 1, 'name': 'g'}, {'art': 'linear', 'm': 3, 't': 3, 'name': 'falsch'}]},
    'regel': 'Die Bildgerade ist ⟦parallel⟧, ihr y-Achsenabschnitt ist k-mal so groß. Aus y = a · x² wird y = (a : k) · x².',
}

BILDGERADE = karte_ops(
    'bildgerade', 'Streckung und Ähnlichkeit', BILDGERADE_KARTE, 'Bildgerade und Bildparabel bei zentrischer Streckung an O', 'streckung', True,
    [('direkt', bg(2, 1, 3)),
     ('direkt', bg(-1, 4, 0.5)),
     ('erkennen', A('Eine Gerade wird mit dem Zentrum O gestreckt. Wie liegt die Bildgerade zur Geraden?',
                    'parallel – geht die Gerade durch O, ist das Bild sogar dieselbe Gerade',
                    ['senkrecht', 'Sie schneiden sich immer in O.', 'nur für k > 1 parallel, sonst senkrecht'],
                    'Jeder Punkt wandert auf seinem Strahl von O weg. Die Steigung bleibt gleich, also sind Gerade und Bild parallel.',
                    'Denke an den Beamer: Wird die Gerade schräger?')),
     ('erkennen', A('Welche Gerade bleibt bei einer Streckung mit dem Zentrum O und k = 2 genau an ihrem Platz?', 'y = 3x',
                    ['y = 3x + 1', 'y = 2', 'y = x + 2'],
                    'Nur eine Gerade durch O bleibt gleich: Ihr y-Achsenabschnitt ist 0, und 0 · 2 = 0. Das ist y = 3x.',
                    'Welcher y-Achsenabschnitt ändert sich beim Malnehmen nicht?')),
     ('mehrschritt', A('Die Parabel y = x² wird mit dem Zentrum O und k = 2 gestreckt. Welche Gleichung hat die Bildparabel?', 'y = 0,5x²',
                       ['y = 2x²', 'y = 4x²', 'y = x² + 2'],
                       '(1 | 1) wird zu (2 | 2), (2 | 4) wird zu (4 | 8). Für x = 2 ist y = 2 = 0,5 · 2². Allgemein: a : k = 1 : 2 = 0,5.',
                       'Strecke zwei Punkte der Parabel und prüfe, welche Gleichung passt.')),
     ('mehrschritt', L('Die Parabel y = 3x² wird mit dem Zentrum O und k = 3 gestreckt. Gib die Bildparabel an.', 'y = □x²', [1], ['3 // 3'],
                       '(1 | 3) wird zu (3 | 9), und 9 = 1 · 3². Allgemein a : k = 3 : 3 = 1: Das Bild ist die Normalparabel y = x².',
                       'Strecke den Punkt (1 | 3) und setze ihn ein.', hinweis='Eine ganze Zahl.')),
     ('umkehr', Z('Die Gerade y = 2x + 5 wurde mit dem Zentrum O gestreckt. Die Bildgerade ist y = 2x + 15. Wie groß ist k?', 3, '15 / 5',
                  'Der y-Achsenabschnitt wird mal k genommen: 5 · k = 15, also k = 3.', 'Vergleiche die y-Achsenabschnitte.')),
     ('umkehr', Z('Die Parabel y = 6x² wurde mit dem Zentrum O gestreckt. Das Bild ist y = 2x². Wie groß ist k?', 3, '6 / 2',
                  'Aus y = a · x² wird y = (a : k) · x². 6 : k = 2, also k = 3.', 'Wie hängt die Zahl vor x² im Bild mit k zusammen?')),
     ('einkleidung', Z('Auf einer Folie liegt ein Strich entlang y = 0,5x + 2 (in cm). Ein Beamer vergrößert vom Ursprung aus mit k = 4. '
                       'In welcher Höhe trifft der vergrößerte Strich die y-Achse?', 8, '2 * 4',
                       'Der y-Achsenabschnitt 2 cm wird mal 4 genommen: 8 cm.', 'Was passiert mit dem y-Achsenabschnitt?', einheit='cm')),
     ('darstellung', A('Im Bild siehst du g: y = x − 1 und drei weitere Geraden. Welche ist das Bild von g bei einer Streckung mit dem Zentrum O und k = 2?',
                       'Gerade 1', ['Gerade 2', 'Gerade 3'],
                       'Das Bild ist parallel zu g (Steigung 1) und schneidet die y-Achse bei −1 · 2 = −2: y = x − 2. Das ist Gerade 1.',
                       'Welche Gerade ist parallel zu g?',
                       grafik={'typ': 'koordinaten', 'x': [-3, 5], 'y': [-4, 5],
                               'graphen': [{'art': 'linear', 'm': 1, 't': -1, 'name': 'g'}, {'art': 'linear', 'm': 1, 't': -2, 'name': '1'},
                                           {'art': 'linear', 'm': 2, 't': -2, 'name': '2'}, {'art': 'linear', 'm': 1, 't': -0.5, 'name': '3'}]})),
     ('rueckwaerts', L('Bei einer Streckung mit dem Zentrum O und k = 2 entsteht die Bildgerade y = −3x + 8. Welche Gleichung hatte die Gerade vorher?',
                       'y = □x + □', [-3, 4], ['-3', '8 // 2'],
                       'Die Steigung bleibt −3. Der y-Achsenabschnitt war vorher 8 : 2 = 4. Also y = −3x + 4.',
                       'Rückwärts: Durch k teilen statt mal k nehmen.', hinweis='Zwei ganze Zahlen, auch negative.')),
     ('rueckwaerts', L('Bei einer Streckung mit dem Zentrum O und k = 4 entsteht die Bildparabel y = x². Welche Parabel war es vorher?', 'y = □x²', [4], ['1 * 4'],
                       'Aus y = a · x² wird y = (a : 4) · x². Damit a : 4 = 1 ist, muss a = 4 sein: y = 4x².',
                       'Welche Zahl a ergibt geteilt durch 4 die Zahl 1?', hinweis='Eine ganze Zahl.')),
     ('verknuepfen', L('Die Gerade g: y = 2x + 3 wird mit dem Zentrum O und k = −1 gestreckt. Gib die Bildgerade an.', 'y = □x + □', [2, -3], ['2', '3 * (-1)'],
                       'k = −1 ist eine Punktspiegelung an O. Die Steigung bleibt 2, der y-Achsenabschnitt wird 3 · (−1) = −3: y = 2x − 3.',
                       'Welche Abbildung ist eine Streckung mit k = −1?', hinweis='Zwei ganze Zahlen, auch negative.')),
     ('verknuepfen', Z('Die Gerade y = x + 2 wird mit dem Zentrum O und k = 3 gestreckt. Wie weit liegen Gerade und Bildgerade auf der y-Achse auseinander?',
                       4, '2 * 3 - 2', 'Die Gerade schneidet die y-Achse bei 2, das Bild bei 2 · 3 = 6. Abstand auf der y-Achse: 6 − 2 = 4.',
                       'Bestimme beide y-Achsenabschnitte.')),
     ('begruenden', A('Stimmt die Aussage? „Bei einer Streckung mit dem Zentrum O bleibt jede Gerade durch O an ihrem Platz.“',
                      'Ja: Jeder Punkt wandert auf seinem Strahl von O aus und bleibt damit auf der Geraden.',
                      ['Nein, sie wird steiler.', 'Nur für k > 1.'],
                      'Eine Gerade durch O hat den y-Achsenabschnitt 0, und 0 · k = 0. Steigung und Achsenabschnitt bleiben gleich.',
                      'Wie groß ist der y-Achsenabschnitt einer Geraden durch O?')),
     ('fehler', A('Jemand streckt y = 2x + 1 mit dem Zentrum O und k = 3 und schreibt y = 6x + 3. Was stimmt?',
                  'Falsch: Die Steigung bleibt 2. Richtig ist y = 2x + 3.', ['Richtig.', 'Falsch: Richtig ist y = 6x + 1.'],
                  'Bild und Gerade sind parallel, die Steigung ändert sich nicht. Nur der y-Achsenabschnitt wird mal 3 genommen.',
                  'Prüfe mit einem Punkt: Wohin kommt (1 | 3)?')),
     ('parameter', Z('Für welches k wird die Gerade y = 0,5x − 2 bei einer Streckung mit dem Zentrum O auf y = 0,5x + 6 abgebildet?', -3, '6 / (-2)',
                     'Der y-Achsenabschnitt wird mal k genommen: (−2) · k = 6, also k = −3.', 'Vergleiche die y-Achsenabschnitte, auch das Vorzeichen.')),
     ('transfer', A('Ein Brückenbogen hat die Form y = −0,02x² (in m, Scheitel im Ursprung). Ein Modell entsteht durch eine Streckung mit dem Zentrum O und k = 0,1. '
                    'Welche Gleichung hat der Bogen des Modells?', 'y = −0,2x²', ['y = −0,002x²', 'y = −0,02x²', 'y = −2x²'],
                    'Aus y = a · x² wird y = (a : k) · x². −0,02 : 0,1 = −0,2. Das Modell ist kleiner, sein Bogen deshalb stärker gekrümmt.',
                    'Teile die Zahl vor x² durch k.'))],
    [Z('Eine Parabel y = a · x² wird mit dem Zentrum O und k = 2 gestreckt, das Bild noch einmal mit dem Zentrum O und k = 3. Am Ende entsteht y = x². Wie groß war a?',
       6, '1 * 2 * 3', 'Erst wird a durch 2 geteilt, dann durch 3, zusammen durch 6. a : 6 = 1, also a = 6.',
       'Zwei Streckungen nacheinander: Wie oft und wodurch wird a geteilt?'),
     Z('Die Gerade g: y = x + 1 wird mit dem Zentrum O und k = 3 gestreckt. g schneidet die x-Achse in A, die Bildgerade in A′. Wie weit liegen A und A′ auseinander?',
       2, '-1 - (-3)', 'g: y = x + 1 hat die Nullstelle −1. Die Bildgerade y = x + 3 hat die Nullstelle −3. Abstand: 2. '
       'Auch ohne Bildgerade: A(−1 | 0) wird zu A′(−3 | 0).', 'A liegt auf der x-Achse. Wohin kommt ein Punkt der x-Achse?')],
    bg(3, -2, 2),
    [bg(-2, 1, 5), bg(1, 4, 0.5), bg(4, -3, -1)],
    [bg(2, -1, 4), bg(-1, 6, 0.5), bg(3, 2, -2), bg(-3, -2, 3), bg(1, -5, 2), bg(5, 1, 7)])


# =====================================================================================================================
# 3) Schwerpunkt eines Dreiecks – abbildungen.aehnlichkeit (Kl. 9), nach bildgerade. Rechnen mit Koordinaten (Mittelwert der Ecken).
# =====================================================================================================================
def sp(A_, B_, C_):
    return ((A_[0] + B_[0] + C_[0]) // 3, (A_[1] + B_[1] + C_[1]) // 3)


def pt(p): return f'({zt(p[0])} | {zt(p[1])})'


def sp_aufg(A_, B_, C_, text=None, h='Addiere die drei x-Werte und teile durch 3, ebenso die y-Werte.', grafik=None):
    assert (A_[0] + B_[0] + C_[0]) % 3 == 0 and (A_[1] + B_[1] + C_[1]) % 3 == 0
    S = sp(A_, B_, C_)
    text = text or f'Berechne den Schwerpunkt des Dreiecks mit A{pt(A_)}, B{pt(B_)} und C{pt(C_)}.'
    return L(text, 'S(□ | □)', list(S), [f'({A_[0]} + {B_[0]} + {C_[0]}) // 3', f'({A_[1]} + {B_[1]} + {C_[1]}) // 3'],
             f'x: ({zt(A_[0])} + {zt(B_[0])} + {zt(C_[0])}) : 3 = {zt(S[0])}. y: ({zt(A_[1])} + {zt(B_[1])} + {zt(C_[1])}) : 3 = {zt(S[1])}. Also S{pt(S)}.',
             h, hinweis='Zwei ganze Zahlen, auch negative.', grafik=grafik)


SCHWERPUNKT_KARTE = {
    'titel': 'Schwerpunkt eines Dreiecks',
    'einstieg': 'Ein Dreieck aus Pappe lässt sich auf einer Bleistiftspitze balancieren. Der Punkt liegt dort, '
                'wo sich drei besondere Strecken treffen. Er heißt ⟦Schwerpunkt⟧.',
    'woerter': [['Seitenhalbierende', 'die Strecke von einer Ecke zur Mitte der gegenüberliegenden Seite'],
                ['Mittelpunkt', 'die Mitte einer Strecke: x-Werte addieren und halbieren, ebenso die y-Werte'],
                ['Schwerpunkt S', 'der Treffpunkt der drei Seitenhalbierenden']],
    'bild': {'typ': 'koordinaten', 'x': [-1, 7], 'y': [-1, 7], 'strecken': [[0, 0, 6, 0], [6, 0, 3, 6], [3, 6, 0, 0]],
             'punkte': [{'x': 0, 'y': 0, 'name': 'A'}, {'x': 6, 'y': 0, 'name': 'B'}, {'x': 3, 'y': 6, 'name': 'C'}]},
    'schritte': [{'text': 'Das Dreieck hat die Ecken A(0 | 0), B(6 | 0) und C(3 | 6).'},
                 {'text': 'x-Werte addieren und durch 3 teilen: (0 + 6 + 3) : 3 = 3.'},
                 {'text': 'Ebenso die y-Werte: (0 + 0 + 6) : 3 = 2.'},
                 {'text': 'Der Schwerpunkt ist ⟦S(3 | 2)⟧. Er liegt auf der Seitenhalbierenden von C zur Mitte (3 | 0).',
                  'bild': {'strecken': [[0, 0, 6, 0], [6, 0, 3, 6], [3, 6, 0, 0], [3, 6, 3, 0, 'gestrichelt']],
                           'punkte': [{'x': 0, 'y': 0, 'name': 'A'}, {'x': 6, 'y': 0, 'name': 'B'}, {'x': 3, 'y': 6, 'name': 'C'}, {'x': 3, 'y': 2, 'name': 'S'}]}}],
    'fehler': 'Durch 2 teilen ist falsch: (0 + 6 + 3) : 2 = 4,5. Ein Dreieck hat ⟦drei⟧ Ecken, also teilst du durch 3.',
    'regel': 'Schwerpunkt: ⟦Mittelwert der drei Ecken⟧, getrennt für x und y. S teilt jede Seitenhalbierende im Verhältnis 2 : 1.',
}

SCHWERPUNKT = karte_ops(
    'schwerpunkt', 'Streckung und Ähnlichkeit', SCHWERPUNKT_KARTE, 'Schwerpunkt eines Dreiecks mit Koordinaten berechnen', 'bildgerade', True,
    [('direkt', sp_aufg((0, 0), (9, 0), (3, 6))),
     ('direkt', sp_aufg((-2, 1), (4, 3), (1, 5))),
     ('erkennen', A('Wo schneiden sich die drei Seitenhalbierenden eines Dreiecks?', 'im Schwerpunkt',
                    ['im Umkreismittelpunkt', 'im Inkreismittelpunkt', 'auf der längsten Seite'],
                    'Die Seitenhalbierenden treffen sich im Schwerpunkt. Der Umkreismittelpunkt ist der Schnittpunkt der Mittelsenkrechten.',
                    'Welche Linien gehören zum Umkreis, welche zum Schwerpunkt?')),
     ('erkennen', A('Welcher Punkt ist der Mittelpunkt der Strecke von A(2 | 3) nach B(8 | 7)?', '(5 | 5)', ['(10 | 10)', '(6 | 4)', '(3 | 2)'],
                    'x: (2 + 8) : 2 = 5. y: (3 + 7) : 2 = 5. Der Mittelpunkt ist (5 | 5).', 'Addiere und halbiere, getrennt für x und y.')),
     ('mehrschritt', sp_aufg((1, -2), (7, 4), (-2, 7))),
     ('mehrschritt', Z('Wie lang ist die Seitenhalbierende von C(4 | 9) zur Mitte der Seite [AB] mit A(0 | 0) und B(8 | 0)?', 9, '9 - 0',
                       'Mitte von [AB]: ((0 + 8) : 2 | 0) = (4 | 0). Von (4 | 0) bis C(4 | 9) geht es senkrecht nach oben: Länge 9.',
                       'Berechne zuerst die Mitte von [AB].')),
     ('umkehr', L('Ein Dreieck hat die Ecken A(0 | 0), B(6 | 0) und den Schwerpunkt S(3 | 4). Wo liegt C?', 'C(□ | □)', [3, 12], ['3 * 3 - 0 - 6', '3 * 4 - 0 - 0'],
                  'Die drei x-Werte ergeben zusammen 3 · 3 = 9, also x von C = 9 − 0 − 6 = 3. Die y-Werte ergeben 3 · 4 = 12, also y von C = 12. C(3 | 12).',
                  'Wie groß muss die Summe der x-Werte sein?', hinweis='Zwei ganze Zahlen.')),
     ('umkehr', L('Von einem Dreieck kennt man A(2 | 1), B(8 | 3) und den Schwerpunkt S(4 | 4). Gib C an.', 'C(□ | □)', [2, 8], ['3 * 4 - 2 - 8', '3 * 4 - 1 - 3'],
                  'Summe der x-Werte: 3 · 4 = 12, also x = 12 − 2 − 8 = 2. Summe der y-Werte: 12, also y = 12 − 1 − 3 = 8. C(2 | 8).',
                  'Rückwärts: erst mal 3, dann die bekannten Werte abziehen.', hinweis='Zwei ganze Zahlen.')),
     ('einkleidung', sp_aufg((0, 0), (90, 0), (45, 60),
                             text='Eine dreieckige Tischplatte hat die Ecken (0 | 0), (90 | 0) und (45 | 60) (in cm). Unter welchem Punkt muss ein einzelnes Tischbein stehen, damit die Platte nicht kippt?',
                             h='Die Platte balanciert im Schwerpunkt.')),
     ('darstellung', sp_aufg((0, 0), (6, 0), (0, 9), text='Lies die Ecken des Dreiecks ab und gib seinen Schwerpunkt an.',
                             h='Lies die drei Ecken genau ab und bilde die Mittelwerte.',
                             grafik={'typ': 'koordinaten', 'x': [-1, 7], 'y': [-1, 10], 'strecken': [[0, 0, 6, 0], [6, 0, 0, 9], [0, 9, 0, 0]],
                                     'punkte': [{'x': 0, 'y': 0, 'name': 'A'}, {'x': 6, 'y': 0, 'name': 'B'}, {'x': 0, 'y': 9, 'name': 'C'}]})),
     ('rueckwaerts', Z('Der Schwerpunkt S liegt 5 cm von der Mitte einer Seite entfernt, auf der Seitenhalbierenden. Wie lang ist diese Seitenhalbierende?', 15, '5 * 3',
                       'S teilt die Seitenhalbierende im Verhältnis 2 : 1. Das kürzere Stück (zur Seitenmitte) ist 1 von 3 Teilen: 5 cm. Ganz: 3 · 5 cm = 15 cm.',
                       'In wie viele gleiche Teile teilt S die Seitenhalbierende?', einheit='cm')),
     ('rueckwaerts', L('Ein Dreieck hat den Schwerpunkt S(2 | 2). Zwei Ecken sind A(−1 | 0) und B(5 | −1). Wo liegt C?', 'C(□ | □)', [2, 7],
                       ['3 * 2 - (-1) - 5', '3 * 2 - 0 - (-1)'],
                       'Summe der x-Werte: 3 · 2 = 6, also x = 6 − (−1) − 5 = 2. Summe der y-Werte: 6, also y = 6 − 0 − (−1) = 7. C(2 | 7).',
                       'Wie groß muss die Summe der y-Werte sein?', hinweis='Zwei ganze Zahlen, auch negative.')),
     ('verknuepfen', Z('Das Dreieck A(0 | 0), B(6 | 0), C(3 | 6) wird vom Schwerpunkt S aus in die drei Dreiecke ABS, BCS und CAS zerlegt. Wie groß ist der Flächeninhalt von ABS?',
                       6, '6 * 2 / 2', 'S = ((0 + 6 + 3) : 3 | (0 + 0 + 6) : 3) = (3 | 2). ABS hat die Grundseite 6 und die Höhe 2: 6 · 2 : 2 = 6. '
                       '(Das ganze Dreieck hat 6 · 6 : 2 = 18, jedes Teildreieck ein Drittel davon.)', 'Bestimme zuerst S, dann Grundseite und Höhe von ABS.')),
     ('verknuepfen', L('Der Schwerpunkt S des Dreiecks A(0 | 0), B(6 | 0), C(0 | 9) wird mit dem Zentrum O(0 | 0) und k = 3 gestreckt. Wo liegt S′?', "S'(□ | □)", [6, 9],
                       ['3 * ((0 + 6 + 0) // 3)', '3 * ((0 + 0 + 9) // 3)'],
                       'S = (6 : 3 | 9 : 3) = (2 | 3). Mit k = 3 von O aus: S′(6 | 9).', 'Erst S berechnen, dann strecken.', hinweis='Zwei ganze Zahlen.')),
     ('begruenden', A('Stimmt die Aussage? „Der Schwerpunkt eines Dreiecks liegt immer innerhalb des Dreiecks.“',
                      'Ja: Er liegt auf jeder Seitenhalbierenden, und die verlaufen im Inneren.',
                      ['Nein, bei stumpfwinkligen Dreiecken liegt er außen.', 'Nur bei gleichseitigen Dreiecken.'],
                      'Jede Seitenhalbierende verbindet eine Ecke mit einem Punkt der Gegenseite und liegt deshalb im Dreieck. '
                      'Außen liegen kann der Umkreismittelpunkt, nicht der Schwerpunkt.', 'Wo verläuft eine Seitenhalbierende?')),
     ('fehler', A('Jemand berechnet den Schwerpunkt von A(0 | 0), B(4 | 0), C(2 | 6) so: S = ((0 + 4 + 2) : 2 | (0 + 0 + 6) : 2) = (3 | 3). Was stimmt?',
                  'Falsch: Man teilt durch 3. Richtig ist S(2 | 2).', ['Richtig.', 'Falsch: Man teilt durch 6. Richtig ist S(1 | 1).'],
                  'Drei Ecken, also durch 3: (0 + 4 + 2) : 3 = 2 und (0 + 0 + 6) : 3 = 2.', 'Wie viele Ecken hat ein Dreieck?')),
     ('parameter', Z('Ein Dreieck hat die Ecken A(0 | 0), B(6 | 0) und C(c | 9). Für welches c liegt der Schwerpunkt auf der y-Achse?', -6, '0 - 0 - 6',
                     'Auf der y-Achse ist der x-Wert 0: (0 + 6 + c) : 3 = 0, also 6 + c = 0 und c = −6.', 'Welchen x-Wert hat ein Punkt auf der y-Achse?')),
     ('transfer', sp_aufg((0, 0), (4, 0), (2, 3),
                          text='Drei gleich schwere Kinder sitzen auf den Ecken einer leichten dreieckigen Plattform bei (0 | 0), (4 | 0) und (2 | 3) (in m). '
                               'Über welchem Punkt muss die Plattform gestützt werden, damit sie nicht kippt?',
                          h='Drei gleich schwere Kinder: Der Ausgleichspunkt ist der Mittelwert ihrer Plätze.'))],
    [Z('Ein Dreieck hat die Ecken A(0 | 0), B(12 | 0) und C(0 | 12). Wie viele Punkte mit ganzzahligen Koordinaten liegen auf der Strecke von C zum Schwerpunkt S, C und S eingeschlossen?',
       5, str(math.gcd(4, 8) + 1),
       'S = (12 : 3 | 12 : 3) = (4 | 4). Von C(0 | 12) nach S(4 | 4) geht es 4 nach rechts und 8 nach unten, also in 4 gleichen Schritten (1 | −2): '
       '(0 | 12), (1 | 10), (2 | 8), (3 | 6), (4 | 4). Das sind 5 Punkte.', 'Bestimme S und zerlege den Weg von C nach S in möglichst viele gleiche ganzzahlige Schritte.'),
     L('Die Mittelpunkte der drei Seiten eines Dreiecks sind (2 | 0), (6 | 3) und (1 | 3). Wo liegt der Schwerpunkt des Dreiecks?', 'S(□ | □)', [3, 2],
       ['(2 + 6 + 1) // 3', '(0 + 3 + 3) // 3'],
       'Jede Ecke kommt in genau zwei Seitenmitten vor. Die Summe der drei Mitten ist deshalb gleich der Summe der drei Ecken. '
       'Also ist S auch der Mittelwert der Mitten: ((2 + 6 + 1) : 3 | (0 + 3 + 3) : 3) = (3 | 2).',
       'Wie hängt die Summe der drei Seitenmitten mit der Summe der Ecken zusammen?', hinweis='Zwei ganze Zahlen.')],
    sp_aufg((3, 1), (9, 2), (0, 6)),
    [sp_aufg((-3, 0), (5, 2), (1, 7)), sp_aufg((0, -4), (8, 2), (4, 5)), sp_aufg((2, 2), (10, 2), (-3, 8))],
    [sp_aufg((1, 1), (5, 1), (3, 7)), sp_aufg((-2, -2), (4, 0), (7, 5)), sp_aufg((0, 3), (6, -3), (3, 9)),
     sp_aufg((4, 0), (10, 4), (1, 8)), sp_aufg((-5, 1), (0, 6), (2, -4)), sp_aufg((6, 6), (12, 0), (0, 3))])


# =====================================================================================================================
# 4) Schnittwinkel zweier Geraden – trigo.rechtwinklig (Kl. 9), nach anwendung. Steigungswinkel: tan α = m (α = tan⁻¹ m);
#    Schnittwinkel: Unterschied der Steigungswinkel, über 90° davon 180° minus. Winkel auf eine Dezimale (Toleranz 0,1).
# =====================================================================================================================
def deg(m): return math.degrees(math.atan(m))


def wink(x, n=1):
    return round(x, n)


def sw(m1, m2):
    d = abs(deg(m1) - deg(m2))
    return 180 - d if d > 90 else d


def sw_aufg(m1, m2, text=None):
    exakt = sw(m1, m2)
    w = wink(exakt)
    a1, a2 = deg(m1), deg(m2)
    text = text or f'Berechne den Schnittwinkel der Geraden y = {zt(m1)}x und y = {zt(m2)}x auf eine Dezimale.'
    weg = (f'tan α = {zt(m1)} ⇒ α ≈ {zt(round(a1, 2))}°; tan β = {zt(m2)} ⇒ β ≈ {zt(round(a2, 2))}°. '
           f'Unterschied ≈ {zt(round(abs(a1 - a2), 2))}°' + (f', über 90°: 180° − {zt(round(abs(a1 - a2), 2))}° ≈ {zt(w)}°.' if abs(a1 - a2) > 90 else f' ≈ {zt(w)}°.'))
    return Z(text, w, f'{exakt!r}', weg, 'Berechne zuerst beide Steigungswinkel mit tan⁻¹.', einheit='°', toleranz=0.1)


SCHNITT_KARTE = {
    'titel': 'Schnittwinkel zweier Geraden',
    'einstieg': 'Zwei gerade Straßen kreuzen sich auf einer Karte. Wie spitz ist die Kreuzung? '
                'Aus den Steigungen der beiden Geraden berechnest du den ⟦Schnittwinkel⟧.',
    'woerter': [['Steigungswinkel α', 'der Winkel zwischen x-Achse und Gerade; es gilt tan α = m'],
                ['Schnittwinkel', 'der kleinere der beiden Winkel zwischen zwei Geraden, höchstens 90°']],
    'bild': {'typ': 'koordinaten', 'x': [-1, 6], 'y': [-1, 6],
             'graphen': [{'art': 'linear', 'm': 2, 't': 0, 'name': 'g'}, {'art': 'linear', 'm': 0.5, 't': 0, 'name': 'h'}]},
    'schritte': [{'text': 'g: y = 2x hat tan α = 2, also α ≈ 63,43°.'},
                 {'text': 'h: y = 0,5x hat tan β = 0,5, also β ≈ 26,57°.'},
                 {'text': 'Schnittwinkel: 63,43° − 26,57° ≈ ⟦36,9°⟧.'}],
    'fehler': 'Die Steigungen abziehen ist falsch: tan⁻¹(2 − 0,5) ≈ 56,3°. Man zieht die ⟦Winkel⟧ voneinander ab, nicht die Steigungen.',
    'regel': 'Steigungswinkel: ⟦tan α = m⟧. Schnittwinkel = Unterschied der Steigungswinkel; über 90° nimm 180° minus den Wert.',
}

SCHNITTWINKEL = karte_ops(
    'schnittwinkel', 'Anwenden', SCHNITT_KARTE, 'Steigungswinkel und Schnittwinkel von Geraden', 'anwendung', True,
    [('direkt', Z('Berechne den Steigungswinkel der Geraden y = 3x + 1 auf eine Dezimale.', wink(deg(3)), repr(deg(3)),
                  f'tan α = 3 ⇒ α = tan⁻¹(3) ≈ {zt(wink(deg(3)))}°. Der y-Achsenabschnitt spielt keine Rolle.', 'Nur die Steigung m zählt: tan α = m.',
                  einheit='°', toleranz=0.1)),
     ('direkt', Z('Berechne den Steigungswinkel der Geraden y = 0,8x − 2 auf eine Dezimale.', wink(deg(0.8)), repr(deg(0.8)),
                  f'tan α = 0,8 ⇒ α = tan⁻¹(0,8) ≈ {zt(wink(deg(0.8)))}°.', 'Nur die Steigung m zählt: tan α = m.', einheit='°', toleranz=0.1)),
     ('erkennen', A('Eine Gerade hat den Steigungswinkel 45°. Welche Steigung hat sie?', '1', ['45', '0,45', '0,5'],
                    'tan 45° = 1: Auf 1 nach rechts geht es 1 nach oben.', 'Denke an ein gleichschenklig-rechtwinkliges Steigungsdreieck.')),
     ('erkennen', A('Welche Gerade hat den größeren Steigungswinkel: y = 2x oder y = 3x?', 'y = 3x', ['y = 2x', 'Beide haben denselben.'],
                    'Je größer die (positive) Steigung, desto steiler die Gerade und desto größer der Steigungswinkel.', 'Welche Gerade ist steiler?')),
     ('mehrschritt', sw_aufg(3, 1)),
     ('mehrschritt', sw_aufg(2, 0.25, 'Berechne den Schnittwinkel der Geraden y = 2x + 1 und y = 0,25x − 3 auf eine Dezimale.')),
     ('umkehr', Z('Eine Gerade durch den Ursprung hat den Steigungswinkel 30°. Gib ihre Steigung auf zwei Dezimalen an.', round(math.tan(math.radians(30)), 2),
                  repr(math.tan(math.radians(30))), 'm = tan 30° ≈ 0,58.', 'Rückwärts: m = tan α.', toleranz=0.01)),
     ('umkehr', Z('Eine steigende Gerade schneidet die x-Achse unter 60°. Gib ihre Steigung auf zwei Dezimalen an.', round(math.tan(math.radians(60)), 2),
                  repr(math.tan(math.radians(60))), 'm = tan 60° ≈ 1,73.', 'Rückwärts: m = tan α.', toleranz=0.01)),
     ('einkleidung', Z('Eine Rampe steigt auf 4 m waagrecht um 1 m an. Ein Weg daneben steigt auf 4 m waagrecht um 2 m an. Unter welchem Winkel laufen die beiden auseinander? '
                       'Runde auf eine Dezimale.', wink(sw(0.5, 0.25)), repr(sw(0.5, 0.25)),
                       f'Steigungen 1 : 4 = 0,25 und 2 : 4 = 0,5. Winkel ≈ {zt(round(deg(0.25), 2))}° und ≈ {zt(round(deg(0.5), 2))}°. '
                       f'Unterschied ≈ {zt(wink(sw(0.5, 0.25)))}°.', 'Bestimme zuerst beide Steigungen.', einheit='°', toleranz=0.1)),
     ('darstellung', Z('Lies die Steigungen der beiden Geraden im Bild ab. Unter welchem Winkel schneiden sie sich?', 90, repr(sw(1, -1)),
                       'g steigt mit m = 1 (α = 45°), h fällt mit m = −1 (β = −45°). Unterschied 45° − (−45°) = 90°.', 'Geh von einem Punkt 1 nach rechts.',
                       einheit='°', toleranz=0.1,
                       grafik={'typ': 'koordinaten', 'x': [-2, 5], 'y': [-2, 5],
                               'graphen': [{'art': 'linear', 'm': 1, 't': 1, 'name': 'g'}, {'art': 'linear', 'm': -1, 't': 3, 'name': 'h'}]})),
     ('rueckwaerts', Z('Eine Gerade g hat die Steigung 1. Eine steilere Gerade h schneidet g unter 30°. Welche Steigung hat h? Runde auf zwei Dezimalen.',
                       round(math.tan(math.radians(75)), 2), repr(math.tan(math.radians(75))),
                       'g: α = 45°. h ist steiler: 45° + 30° = 75°. m = tan 75° ≈ 3,73.', 'Welchen Steigungswinkel hat g?', toleranz=0.01)),
     ('rueckwaerts', Z('Eine steigende Gerade h schneidet die x-Achse unter 20°. Wie groß ist ihre Steigung? Runde auf zwei Dezimalen.',
                       round(math.tan(math.radians(20)), 2), repr(math.tan(math.radians(20))),
                       'Die x-Achse hat den Steigungswinkel 0°. h hat also 20°: m = tan 20° ≈ 0,36.', 'Welchen Steigungswinkel hat die x-Achse?', toleranz=0.01)),
     ('verknuepfen', Z('Die Geraden y = 0,5x und y = −2x + 5 schneiden sich. Wie groß ist der Schnittwinkel?', 90, repr(sw(0.5, -2)),
                       f'α ≈ {zt(round(deg(0.5), 2))}°, β ≈ {zt(round(deg(-2), 2))}°. Unterschied 26,57° − (−63,43°) = 90°. '
                       'Passt: 0,5 · (−2) = −1, die Geraden stehen senkrecht.', 'Vergleiche auch mit der Regel m₁ · m₂ = −1.', einheit='°', toleranz=0.1)),
     ('verknuepfen', Z('Eine Gerade geht durch A(0 | 1) und B(4 | 4). Unter welchem Winkel schneidet sie die x-Achse? Runde auf eine Dezimale.',
                       wink(deg(0.75)), repr(deg(0.75)), f'm = (4 − 1) : (4 − 0) = 0,75. α = tan⁻¹(0,75) ≈ {zt(wink(deg(0.75)))}°.',
                       'Berechne zuerst die Steigung aus den zwei Punkten.', einheit='°', toleranz=0.1)),
     ('begruenden', A('Stimmt die Aussage? „Parallele Geraden haben denselben Steigungswinkel.“',
                      'Ja: Gleiche Steigung heißt gleiches tan α, also gleicher Winkel.',
                      ['Nein, der Winkel hängt auch vom y-Achsenabschnitt ab.', 'Nur wenn beide durch den Ursprung gehen.'],
                      'Der Steigungswinkel hängt nur von m ab (tan α = m). Parallele Geraden haben dasselbe m.', 'Wovon hängt tan α ab?')),
     ('fehler', A('Jemand berechnet den Schnittwinkel von y = 4x und y = −x so: 76,0° − (−45,0°) = 121,0°. Was stimmt?',
                  'Falsch: Über 90° nimmt man 180° − 121,0° = 59,0°.', ['Richtig.', 'Falsch: Man muss 76,0° + 45,0° = 121,0° rechnen, das Ergebnis bleibt.'],
                  'Der Schnittwinkel ist der kleinere der beiden Winkel und höchstens 90°: 180° − 121,0° = 59,0°.', 'Wie groß darf ein Schnittwinkel höchstens sein?')),
     ('parameter', Z('Die Gerade y = m · x (m > 0) ist flacher als y = x und schneidet sie unter 15°. Wie groß ist m? Runde auf zwei Dezimalen.',
                     round(math.tan(math.radians(30)), 2), repr(math.tan(math.radians(30))),
                     'y = x hat 45°. Flacher um 15°: 30°. m = tan 30° ≈ 0,58.', 'Welchen Steigungswinkel muss die gesuchte Gerade haben?', toleranz=0.01)),
     ('transfer', Z('Ein Dach hat zwei Flächen. Die linke steigt mit 50 % zum First an, die rechte fällt mit 100 % wieder ab. Wie groß ist der Winkel am First zwischen den Dachflächen? '
                    'Runde auf eine Dezimale.', wink(180 - deg(0.5) - deg(1)), repr(180 - deg(0.5) - deg(1)),
                    f'Links: tan α = 0,5 ⇒ α ≈ {zt(round(deg(0.5), 2))}°. Rechts: tan β = 1 ⇒ β = 45°. Im Dreieck aus Dachflächen und Boden: '
                    f'180° − 26,57° − 45° ≈ {zt(wink(180 - deg(0.5) - deg(1)))}°.', 'Zeichne das Dreieck aus beiden Dachflächen und dem Dachboden.', einheit='°', toleranz=0.1))],
    [Z('Die Geraden y = 2x und y = 3x schneiden sich unter dem Winkel δ. Die Gerade y = 3x und eine noch steilere Gerade y = m · x schneiden sich unter demselben Winkel δ. '
       'Wie groß ist m? Runde auf eine Dezimale.', round(math.tan(math.radians(2 * deg(3) - deg(2))), 1), repr(math.tan(math.radians(2 * deg(3) - deg(2)))),
       f'δ ≈ {zt(round(deg(3), 2))}° − {zt(round(deg(2), 2))}° ≈ {zt(round(deg(3) - deg(2), 2))}°. Die steilere Gerade hat ≈ {zt(round(2 * deg(3) - deg(2), 2))}°, '
       'also m = tan(≈ 79,70°) ≈ 5,5.', 'Addiere δ zum Steigungswinkel von y = 3x.', toleranz=0.1),
     Z('Eine steigende Gerade durch den Ursprung bildet mit der x-Achse und mit der y-Achse gleich große Winkel. Welche Steigung hat sie?', 1, repr(math.tan(math.radians(45))),
       'Die beiden Winkel ergeben zusammen 90°, sind also je 45°. m = tan 45° = 1.', 'Wie groß ist der Winkel zwischen x-Achse und y-Achse?', toleranz=0.01)],
    sw_aufg(4, 1),
    [sw_aufg(2, 1), sw_aufg(5, 0.5), sw_aufg(1.5, 0.2)],
    [sw_aufg(3, 0.5), sw_aufg(4, 2), sw_aufg(1, 0.1), sw_aufg(6, 1.2), sw_aufg(0.6, 0.3), sw_aufg(2.5, 0.4)])


# =====================================================================================================================
# 5) Additionstheoreme – trigo.allgemein (Kl. 9), nach einheitskreis. Werte aus 3-4-5 und 7-24-25 Dreiecken (exakte Dezimalzahlen).
# =====================================================================================================================
from fractions import Fraction as Fr  # noqa: E402

W1 = (Fr('0.6'), Fr('0.8'))    # (sin, cos)
W2 = (Fr('0.8'), Fr('0.6'))
W3 = (Fr('0.28'), Fr('0.96'))
W4 = (Fr('0.96'), Fr('0.28'))


def zf(x): return zt(float(x)) if x.denominator != 1 else zt(int(x))


def add_aufg(a, b, art, text=None, h='Schreibe zuerst die passende Formel hin, dann setze ein.', grafik=None):
    sa, ca = a; sb, cb = b
    if art == 'sin':
        wert = sa * cb + ca * sb
        c = f'{float(sa)} * {float(cb)} + {float(ca)} * {float(sb)}'
        w = f'sin(α + β) = sin α · cos β + cos α · sin β = {zf(sa)} · {zf(cb)} + {zf(ca)} · {zf(sb)} = {zf(sa * cb)} + {zf(ca * sb)} = {zf(wert)}.'
    else:
        wert = ca * cb - sa * sb
        c = f'{float(ca)} * {float(cb)} - {float(sa)} * {float(sb)}'
        w = f'cos(α + β) = cos α · cos β − sin α · sin β = {zf(ca)} · {zf(cb)} − {zf(sa)} · {zf(sb)} = {zf(ca * cb)} − {zf(sa * sb)} = {zf(wert)}.'
    text = text or (f'Es gilt sin α = {zf(sa)}, cos α = {zf(ca)}, sin β = {zf(sb)} und cos β = {zf(cb)}. Berechne {art}(α + β).')
    return Z(text, wert, c, w, h, grafik=grafik)


ADD_KARTE = {
    'titel': 'Additionstheoreme',
    'einstieg': 'Du kennst sin 30° und sin 45°. Aber wie groß ist sin 75°? Man kann es aus den beiden bekannten Winkeln zusammensetzen. '
                'Das erlauben die ⟦Additionstheoreme⟧.',
    'woerter': [['Additionstheorem', 'Formel für sin(α + β) oder cos(α + β) aus den Werten von α und β'],
                ['sin(α + β)', 'der Sinus des ganzen Winkels α + β – nicht dasselbe wie sin α + sin β']],
    'bild': {'typ': 'tabelle', 'kopf': ['', 'α', 'β'], 'zeilen': [['sin', '0,6', '0,28'], ['cos', '0,8', '0,96']]},
    'schritte': [{'text': 'Gegeben: sin α = 0,6, cos α = 0,8, sin β = 0,28 und cos β = 0,96.'},
                 {'text': 'Formel: sin(α + β) = sin α · cos β + cos α · sin β.'},
                 {'text': 'Einsetzen: 0,6 · 0,96 + 0,8 · 0,28 = 0,576 + 0,224.'},
                 {'text': 'Also ist ⟦sin(α + β) = 0,8⟧.'}],
    'fehler': 'sin(α + β) ist nicht sin α + sin β: 0,6 + 0,28 = 0,88 statt 0,8. Den Sinus darf man ⟦nicht aufteilen⟧.',
    'regel': '⟦sin(α + β) = sin α · cos β + cos α · sin β⟧. Dazu gilt cos(α + β) = cos α · cos β − sin α · sin β.',
}

ADDITION = karte_ops(
    'additionstheoreme', 'Einheitskreis und Fläche', ADD_KARTE, 'Additionstheoreme für Sinus und Kosinus anwenden', 'einheitskreis', True,
    [('direkt', add_aufg(W1, W4, 'sin')),
     ('direkt', add_aufg(W2, W3, 'cos')),
     ('erkennen', A('Welche Formel ist richtig?', 'sin(α + β) = sin α · cos β + cos α · sin β',
                    ['sin(α + β) = sin α + sin β', 'sin(α + β) = sin α · sin β + cos α · cos β', 'sin(α + β) = sin α · cos α + sin β · cos β'],
                    'Beim Sinus mischen sich sin und cos: sin α · cos β + cos α · sin β.', 'In jedem Produkt steht ein α und ein β.')),
     ('erkennen', A('Welcher Term ist gleich cos(α + β)?', 'cos α · cos β − sin α · sin β',
                    ['cos α · cos β + sin α · sin β', 'cos α + cos β', 'sin α · cos β − cos α · sin β'],
                    'Beim Kosinus stehen zuerst die beiden Kosinus, dann wird das Produkt der Sinus abgezogen.', 'Achte auf das Rechenzeichen in der Mitte.')),
     ('mehrschritt', add_aufg(W2, W4, 'sin', text='α und β sind spitze Winkel mit sin α = 0,8 und sin β = 0,96. Berechne zuerst cos α und cos β, dann sin(α + β).',
                              h='cos α = √(1 − sin² α).')),
     ('mehrschritt', Z('Es gilt sin 30° = 0,5, cos 30° ≈ 0,866, sin 60° ≈ 0,866 und cos 60° = 0,5. Berechne mit dem Additionstheorem sin(30° + 60°) auf zwei Dezimalen.',
                       1, '0.5 * 0.5 + 0.866 * 0.866',
                       'sin 30° · cos 60° + cos 30° · sin 60° = 0,5 · 0,5 + 0,866 · 0,866 ≈ 0,25 + 0,75 = 1,00. Passt: sin 90° = 1.',
                       'Setze in sin α · cos β + cos α · sin β ein.', toleranz=0.01)),
     ('umkehr', Z('Es gilt sin(α + β) = 0,8, sin α = 0,6, cos α = 0,8 und cos β = 0,96. Wie groß ist sin β?', Fr('0.28'), '(0.8 - 0.6 * 0.96) / 0.8',
                  '0,8 = 0,6 · 0,96 + 0,8 · sin β = 0,576 + 0,8 · sin β. Also 0,8 · sin β = 0,224 und sin β = 0,28.', 'Setze alles Bekannte in die Formel ein und löse nach sin β auf.')),
     ('umkehr', Z('Es gilt cos(α + β) = 0, cos α = 0,6, cos β = 0,8 und sin β = 0,6. Wie groß ist sin α?', Fr('0.8'), '(0.6 * 0.8 - 0) / 0.6',
                  '0 = 0,6 · 0,8 − sin α · 0,6 = 0,48 − 0,6 · sin α. Also sin α = 0,48 : 0,6 = 0,8.', 'Setze in cos α · cos β − sin α · sin β ein.')),
     ('einkleidung', Z('Ein 10 m langer Kranarm wird erst um α (sin α = 0,8, cos α = 0,6) und dann noch um β (sin β = 0,28, cos β = 0,96) angehoben. '
                       'Er steht dann unter dem Winkel α + β zur Waagrechten. Wie hoch liegt seine Spitze über dem Drehpunkt?', Fr('9.36'),
                       '10 * (0.8 * 0.96 + 0.6 * 0.28)', 'Höhe = 10 m · sin(α + β). sin(α + β) = 0,8 · 0,96 + 0,6 · 0,28 = 0,768 + 0,168 = 0,936. Höhe 9,36 m.',
                       'Die Höhe ist 10 m · sin(α + β).', einheit='m')),
     ('darstellung', add_aufg(W4, W2, 'cos', text='Die Tabelle zeigt sin und cos der Winkel α und β. Berechne cos(α + β).', h='Lies die vier Werte ab und setze ein.',
                              grafik={'typ': 'tabelle', 'kopf': ['', 'α', 'β'], 'zeilen': [['sin', '0,96', '0,8'], ['cos', '0,28', '0,6']]})),
     ('rueckwaerts', Z('α und β sind spitze Winkel. Es gilt sin α = 0,6, cos α = 0,8 und sin(α + β) = 1. Wie groß ist cos β?', Fr('0.6'), '0.6',
                       'sin(α + β) = 1 heißt α + β = 90°, also β = 90° − α. Dann ist cos β = cos(90° − α) = sin α = 0,6. '
                       'Probe: sin β = 0,8 und 0,6 · 0,6 + 0,8 · 0,8 = 0,36 + 0,64 = 1.', 'Für welchen Winkel ist der Sinus 1?')),
     ('rueckwaerts', Z('α ist ein spitzer Winkel mit cos α = 0,8. Außerdem gilt sin(α + α) = 0,96. Wie groß ist sin α?', Fr('0.6'), '0.96 / (2 * 0.8)',
                       'sin(α + α) = sin α · cos α + cos α · sin α = 2 · sin α · 0,8 = 1,6 · sin α = 0,96. Also sin α = 0,6.',
                       'Setze β = α in die Formel ein.')),
     ('verknuepfen', Z('Berechne sin 75° mit sin 75° = sin(45° + 30°). Runde auf drei Dezimalen.', round(math.sin(math.radians(75)), 3), repr(math.sin(math.radians(75))),
                       'sin 45° · cos 30° + cos 45° · sin 30° = √2/2 · √3/2 + √2/2 · 1/2 ≈ 0,612 + 0,354 ≈ 0,966.',
                       'Nimm die exakten Werte vom Einheitskreis für 30° und 45°.', toleranz=0.001)),
     ('verknuepfen', Z('Berechne cos 75° mit cos 75° = cos(45° + 30°). Runde auf drei Dezimalen.', round(math.cos(math.radians(75)), 3), repr(math.cos(math.radians(75))),
                       'cos 45° · cos 30° − sin 45° · sin 30° = √2/2 · √3/2 − √2/2 · 1/2 ≈ 0,612 − 0,354 ≈ 0,259.',
                       'Nimm die exakten Werte vom Einheitskreis für 30° und 45°.', toleranz=0.001)),
     ('begruenden', A('Stimmt die Aussage? „sin(α + β) = sin α + sin β gilt für alle Winkel.“',
                      'Nein: Für α = β = 90° ist sin 180° = 0, aber sin 90° + sin 90° = 2.', ['Ja, man darf den Sinus aufteilen.', 'Nur für spitze Winkel.'],
                      'Ein Gegenbeispiel genügt. Auch für spitze Winkel stimmt es nicht: sin 60° ≈ 0,866, aber sin 30° + sin 30° = 1.',
                      'Probiere ein Gegenbeispiel mit bekannten Winkeln.')),
     ('fehler', A('Jemand rechnet mit cos α = 0,8, sin α = 0,6, cos β = 0,6 und sin β = 0,8: cos(α + β) = 0,8 · 0,6 + 0,6 · 0,8 = 0,96. Was stimmt?',
                  'Falsch: Vor sin α · sin β gehört ein Minus. Richtig ist 0,48 − 0,48 = 0.', ['Richtig.', 'Falsch: Richtig ist cos α + cos β = 1,4.'],
                  'cos(α + β) = cos α · cos β − sin α · sin β = 0,48 − 0,48 = 0. Passt: Hier ist α + β = 90°.', 'Welches Rechenzeichen steht in der Formel für cos(α + β)?')),
     ('parameter', Z('Für welchen spitzen Winkel β gilt sin(60° + β) = 1?', 30, '90 - 60',
                     'Der Sinus ist 1 bei 90°: 60° + β = 90°, also β = 30°. Probe mit der Formel: sin 60° · cos 30° + cos 60° · sin 30° = 0,75 + 0,25 = 1.',
                     'Bei welchem Winkel hat der Sinus den Wert 1?', einheit='°')),
     ('transfer', Z('Ein Roboterarm hat zwei Teile. Das erste ist um α gegen die Waagrechte geneigt (sin α = 0,6, cos α = 0,8). '
                    'Das zweite Teil ist 5 m lang und knickt um weitere β nach oben ab (sin β = 0,8, cos β = 0,6); es steht damit unter α + β zur Waagrechten. '
                    'Wie weit reicht das zweite Teil waagrecht?', 0, '5 * (0.8 * 0.6 - 0.6 * 0.8)',
                    'Waagrecht: 5 m · cos(α + β). cos(α + β) = 0,8 · 0,6 − 0,6 · 0,8 = 0. Das zweite Teil reicht 0 m weit, es steht senkrecht (α + β = 90°).',
                    'Die waagrechte Reichweite ist 5 m · cos(α + β).', einheit='m'))],
    [Z('Berechne ohne Taschenrechner: 4 · sin 15° · cos 15°.', 1, '2 * 0.5',
       'sin 30° = sin(15° + 15°) = 2 · sin 15° · cos 15°. Also 4 · sin 15° · cos 15° = 2 · sin 30° = 2 · 0,5 = 1.', 'Schreibe sin 30° als sin(15° + 15°).'),
     Z('α ist spitz mit sin α = 0,6. Berechne sin(3α), also sin(α + α + α).', Fr('0.936'), '(2 * 0.6 * 0.8) * 0.8 + (0.8 * 0.8 - 0.6 * 0.6) * 0.6',
       'cos α = 0,8. sin 2α = 2 · 0,6 · 0,8 = 0,96, cos 2α = 0,64 − 0,36 = 0,28. sin 3α = sin 2α · cos α + cos 2α · sin α = 0,768 + 0,168 = 0,936.',
       'Rechne erst sin(α + α) und cos(α + α), dann noch einmal + α.')],
    add_aufg(W3, W1, 'sin'),
    [add_aufg(W2, W1, 'sin'), add_aufg(W3, W4, 'cos'), add_aufg(W4, W1, 'sin')],
    [add_aufg(W1, W3, 'cos'), add_aufg(W2, W4, 'cos'), add_aufg(W3, W2, 'sin'), add_aufg(W4, W3, 'sin'), add_aufg(W1, W1, 'cos'), add_aufg(W3, W3, 'sin')])


# =====================================================================================================================
# 6) Abstand Punkt–Gerade – abbildungen.matrizen (RS Gruppe I, Kl. 10), nach skalarprodukt. Pflicht im Flug.
#    g durch O mit Richtungsvektor u = (4 | 3) (Steigung 0,75); Lotfußpunkt F mit (P − F) · u = 0; Abstand = |PF|.
# =====================================================================================================================
U = (4, 3)
N = (-3, 4)   # senkrecht zu U, Länge 5


def lot(P):
    t = Fr(P[0] * U[0] + P[1] * U[1], 25)
    F = (t * U[0], t * U[1])
    PF = (P[0] - F[0], P[1] - F[1])
    d2 = PF[0] ** 2 + PF[1] ** 2
    return t, F, PF, d2


def ab_aufg(P, text=None, h='Setze F = (4t | 3t) an und rechne mit (P − F) · u = 0.'):
    t, F, PF, d2 = lot(P)
    d = math.isqrt(int(d2))
    assert t.denominator == 1 and d * d == d2, (P, t, d2)
    text = text or f'Die Gerade g geht durch O(0 | 0) mit dem Richtungsvektor u = (4 | 3). Berechne den Abstand des Punktes P{pt(P)} von g.'
    t = int(t)
    w = (f'F = (4t | 3t). (P − F) · u = ({zt(P[0])} − 4t) · 4 + ({zt(P[1])} − 3t) · 3 = {zt(4 * P[0] + 3 * P[1])} − 25t = 0 ⇒ t = {zt(t)}, F{pt((4 * t, 3 * t))}. '
         f'PF = ({zt(int(F[0] - P[0]))} | {zt(int(F[1] - P[1]))}), Länge √({zt(int(PF[0] ** 2))} + {zt(int(PF[1] ** 2))}) = {zt(d)}.')
    return Z(text, d, f'(({P[0]} - 4 * {t}) ** 2 + ({P[1]} - 3 * {t}) ** 2) // {d}', w, h)


def P_aus(t, s): return (t * U[0] + s * N[0], t * U[1] + s * N[1])


ABSTAND_KARTE = {
    'titel': 'Abstand Punkt–Gerade',
    'einstieg': 'Ein Leuchtturm steht neben einer geraden Küstenstraße. Wie weit ist er von der Straße entfernt? '
                'Gemeint ist der kürzeste Weg, senkrecht zur Straße. Das ist der ⟦Abstand⟧.',
    'woerter': [['Abstand Punkt–Gerade', 'die Länge des kürzesten Wegs vom Punkt zur Geraden; dieser Weg steht senkrecht auf ihr'],
                ['Lotfußpunkt F', 'der Punkt, an dem der senkrechte Weg die Gerade trifft'],
                ['Richtungsvektor u', 'ein Pfeil, der in Richtung der Geraden zeigt']],
    'bild': {'typ': 'koordinaten', 'x': [-4, 8], 'y': [-1, 12], 'schritt_x': 2, 'schritt_y': 2,
             'graphen': [{'art': 'linear', 'm': 0.75, 't': 0, 'name': 'g'}], 'punkte': [{'x': -2, 'y': 11, 'name': 'P'}]},
    'schritte': [{'text': 'g geht durch O mit u = (4 | 3). Gesucht ist der Abstand von P(−2 | 11).'},
                 {'text': 'F liegt auf g, also F = (4t | 3t). Senkrecht heißt: (P − F) · u = 0.'},
                 {'text': '(−2 − 4t) · 4 + (11 − 3t) · 3 = 25 − 25t = 0, also t = 1 und F(4 | 3).',
                  'bild': {'punkte': [{'x': -2, 'y': 11, 'name': 'P'}, {'x': 4, 'y': 3, 'name': 'F'}]}},
                 {'text': 'PF = (6 | −8) hat die Länge √(36 + 64) = ⟦10⟧.',
                  'bild': {'punkte': [{'x': -2, 'y': 11, 'name': 'P'}, {'x': 4, 'y': 3, 'name': 'F'}], 'strecken': [[-2, 11, 4, 3, 'gestrichelt']]}}],
    'fehler': 'Der Abstand ist nicht |OP| = √(4 + 121) ≈ 11,2. Gemessen wird ⟦senkrecht⟧ zur Geraden, nicht zu irgendeinem Punkt auf ihr.',
    'regel': 'Abstand = Länge von ⟦PF⟧. F liegt auf g, und PF steht senkrecht auf g: (P − F) · u = 0.',
}

ABSTAND = karte_ops(
    'abstand', 'Skalarprodukt', ABSTAND_KARTE, 'Abstand eines Punktes von einer Geraden berechnen', 'skalarprodukt', False,
    [('direkt', ab_aufg(P_aus(2, -1))),
     ('direkt', Z('Die Gerade g geht durch O mit u = (4 | 3). Der Lotfußpunkt von P(5 | 10) ist F(8 | 6). Wie groß ist der Abstand von P zu g?', 5, '((5 - 8) ** 2 + (10 - 6) ** 2) // 5',
                  'PF = (8 − 5 | 6 − 10) = (3 | −4). Länge √(9 + 16) = √25 = 5.', 'Berechne die Länge des Vektors PF.')),
     ('erkennen', A('Welcher Weg vom Punkt P zur Geraden g gibt den Abstand an?', 'der Weg, der senkrecht auf g steht',
                    ['der waagrechte Weg', 'der Weg zum Ursprung', 'der Weg parallel zu g'],
                    'Der senkrechte Weg ist der kürzeste. Jeder schräge Weg ist eine Hypotenuse und damit länger.', 'Welcher Weg ist der kürzeste?')),
     ('erkennen', A('Steht der Vektor PF = (3 | −4) senkrecht auf u = (4 | 3)?', 'Ja', ['Nein', 'Das kann man nicht prüfen.'],
                    'Skalarprodukt: 3 · 4 + (−4) · 3 = 12 − 12 = 0. Also senkrecht.', 'Berechne das Skalarprodukt.')),
     ('mehrschritt', ab_aufg(P_aus(1, 3))),
     ('mehrschritt', ab_aufg(P_aus(3, -1))),
     ('umkehr', L('Der Lotfußpunkt von P auf g (durch O mit u = (4 | 3)) ist F(8 | 6). P hat von g den Abstand 5 und liegt oberhalb von g. Gib P an.', 'P(□ | □)', [5, 10],
                  ['8 + (-3)', '6 + 4'], 'Senkrecht zu u = (4 | 3) ist (−3 | 4), Länge 5. Nach oben: P = F + (−3 | 4) = (5 | 10).',
                  'Welcher Vektor der Länge 5 steht senkrecht auf (4 | 3)?', hinweis='Zwei ganze Zahlen.')),
     ('umkehr', L('Der Lotfußpunkt von P auf g (durch O mit u = (4 | 3)) ist F(−4 | −3). P hat von g den Abstand 10 und liegt oberhalb von g. Gib P an.', 'P(□ | □)', [-10, 5],
                  ['-4 + 2 * (-3)', '-3 + 2 * 4'], 'Senkrecht zu u nach oben zeigt (−3 | 4) mit der Länge 5. Doppelt so lang ergibt 10: P = (−4 − 6 | −3 + 8) = (−10 | 5).',
                  'Welcher Vektor der Länge 5 steht senkrecht auf u und zeigt nach oben?', hinweis='Zwei ganze Zahlen, auch negative.')),
     ('einkleidung', ab_aufg(P_aus(2, 3), text='Ein gerader Wanderweg führt von O(0 | 0) in Richtung u = (4 | 3) (Einheit 100 m). Eine Hütte steht bei H(−1 | 18). '
                                                 'Wie weit ist die Hütte vom Weg entfernt (in 100 m)?', h='Gesucht ist der Abstand der Hütte vom Weg.')),
     ('darstellung', Z('Im Bild siehst du die Gerade g: y = 0,75x und den Punkt P(0 | 5). Wie weit ist P von g entfernt?', 4, '4',
                       'u = (4 | 3). F = (4t | 3t): (0 − 4t) · 4 + (5 − 3t) · 3 = 15 − 25t = 0 ⇒ t = 0,6, F(2,4 | 1,8). PF = (2,4 | −3,2), Länge √(5,76 + 10,24) = √16 = 4.',
                       'Lies P ab und nimm u = (4 | 3) als Richtung von g.',
                       grafik={'typ': 'koordinaten', 'x': [-2, 6], 'y': [-1, 6], 'graphen': [{'art': 'linear', 'm': 0.75, 't': 0, 'name': 'g'}],
                               'punkte': [{'x': 0, 'y': 5, 'name': 'P'}]})),
     ('rueckwaerts', Z('Ein Punkt P auf der y-Achse liegt oberhalb von g: y = 0,75x und hat von g den Abstand 4. Gib die y-Koordinate von P an.', 5, '4 * 5 // 4',
                       'P(0 | p). F = (4t | 3t) mit (0 − 4t) · 4 + (p − 3t) · 3 = 0 ⇒ t = 3p : 25. PF hat dann die Länge 4p : 5 = 0,8p. 0,8p = 4 ⇒ p = 5.',
                       'Rechne allgemein mit P(0 | p) und setze die Länge gleich 4.')),
     ('rueckwaerts', L('F(4 | 3) ist der Lotfußpunkt von P auf g (durch O mit u = (4 | 3)). Der Abstand ist 15, P liegt unterhalb von g. Gib P an.', 'P(□ | □)', [13, -9],
                       ['4 + 3 * 3', '3 + 3 * (-4)'], 'Senkrecht zu u nach unten: (3 | −4), Länge 5. Dreimal so lang ergibt 15: P = (4 + 9 | 3 − 12) = (13 | −9).',
                       'Welcher Vektor der Länge 5 steht senkrecht auf u und zeigt nach unten?', hinweis='Zwei ganze Zahlen, auch negative.')),
     ('verknuepfen', Z('Wie groß ist der Flächeninhalt des Dreiecks mit O(0 | 0), A(8 | 6) und P(−3 | 4)?', 25, '10 * 5 / 2',
                       'Grundseite [OA]: Länge √(64 + 36) = 10. Höhe = Abstand von P zur Geraden OA: F = O, denn (−3 | 4) · (8 | 6) = 0; Höhe 5. Fläche 10 · 5 : 2 = 25.',
                       'Nimm [OA] als Grundseite. Die Höhe ist der Abstand von P zur Geraden OA.')),
     ('verknuepfen', ab_aufg((-6, 8), text='Ein Kreis um M(−6 | 8) berührt die Gerade g durch O mit u = (4 | 3). Wie groß ist sein Radius?',
                             h='Der Radius zum Berührpunkt steht senkrecht auf der Tangente.')),
     ('begruenden', A('Stimmt die Aussage? „Liegt P auf der Geraden g, dann ist sein Abstand von g gleich 0.“', 'Ja: Dann ist F = P, und PF hat die Länge 0.',
                      ['Nein, der Abstand ist dann unendlich.', 'Nur wenn g durch den Ursprung geht.'],
                      'Der kürzeste Weg von einem Punkt auf g zu g hat die Länge 0.', 'Wo liegt der Lotfußpunkt, wenn P schon auf g liegt?')),
     ('fehler', A('Jemand berechnet den Abstand von P(5 | 10) zur Geraden g: y = 0,75x als |OP| = √(25 + 100) ≈ 11,2. Was stimmt?',
                  'Falsch: Gemessen wird senkrecht zu g. Mit F(8 | 6) ist der Abstand 5.', ['Richtig.', 'Falsch: Der Abstand ist die y-Koordinate 10.'],
                  'O ist irgendein Punkt auf g, nicht der nächste. Der Lotfußpunkt ist F(8 | 6), PF = (3 | −4) hat die Länge 5.', 'Steht OP senkrecht auf g?')),
     ('parameter', Z('Für welches c > 0 hat der Punkt P(c | 0) von der Geraden g: y = 0,75x den Abstand 6?', 10, '6 / 0.6',
                     'F = (4t | 3t) mit (c − 4t) · 4 + (0 − 3t) · 3 = 4c − 25t = 0 ⇒ t = 4c : 25. PF = (9c : 25 | −12c : 25), Länge 15c : 25 = 0,6c. 0,6c = 6 ⇒ c = 10.',
                     'Rechne mit P(c | 0) allgemein und setze die Länge gleich 6.')),
     ('transfer', ab_aufg(P_aus(2, 4), text='Ein Schiff fährt von O(0 | 0) geradeaus in Richtung u = (4 | 3) (Einheit km). Ein Leuchtturm steht bei L(−4 | 22). '
                                              'Wie nah kommt das Schiff dem Leuchtturm höchstens?', h='Am nächsten ist das Schiff am Lotfußpunkt.'))],
    [Z('Wie viele Punkte mit ganzzahligen Koordinaten im Quadrat 0 ≤ x ≤ 10, 0 ≤ y ≤ 10 haben von der Geraden y = 0,75x genau den Abstand 1?',
       sum(1 for x in range(11) for y in range(11) if abs(3 * x - 4 * y) == 5), str(sum(1 for x in range(11) for y in range(11) if abs(3 * x - 4 * y) == 5)),
       'Der Abstand von P(x | y) zu g ist |3x − 4y| : 5 (wie in den Aufgaben: PF hat die Länge |3x − 4y| : 5). Abstand 1 heißt 3x − 4y = 5 oder 3x − 4y = −5. '
       'Im Quadrat: (3 | 1), (7 | 4) und (1 | 2), (5 | 5), (9 | 8). Das sind 5 Punkte.', 'Zeige zuerst: Der Abstand von P(x | y) ist |3x − 4y| : 5.'),
     Z('Die Geraden g: y = 0,75x und h: y = 0,75x − 5 sind parallel. Wie weit sind sie voneinander entfernt?', 4, '4',
       'Nimm den Punkt (0 | −5) auf h und berechne seinen Abstand von g: F = (4t | 3t) mit (0 − 4t) · 4 + (−5 − 3t) · 3 = −15 − 25t = 0 ⇒ t = −0,6, F(−2,4 | −1,8). '
       'PF = (−2,4 | 3,2), Länge 4.', 'Wähle einen bequemen Punkt auf h und berechne seinen Abstand von g.')],
    ab_aufg(P_aus(1, -1)),
    [ab_aufg(P_aus(3, 2)), ab_aufg(P_aus(-1, 1)), ab_aufg(P_aus(2, -2))],
    [ab_aufg(P_aus(1, 1)), ab_aufg(P_aus(4, 1)), ab_aufg(P_aus(-2, 2)), ab_aufg(P_aus(1, -3)), ab_aufg(P_aus(3, 3)), ab_aufg(P_aus(-1, -2))])
