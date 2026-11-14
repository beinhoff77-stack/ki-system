#!/usr/bin/env python3
"""Thema zahlen.intervalle – Intervalle (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import A, M, Z, baue, cz, mit_bild, zt  # noqa: E402

META = {'thema_schluessel': 'zahlen.intervalle', 'thema_id': 69, 'block_id': 61, 'klasse': {'gym_by': 8, 'rs_by': 7}}

ETAPPEN = [
    {'lernziel': 'lesen', 'titel': 'Intervalle lesen',
     'regel': 'Ein ⟦Intervall⟧ ist ein lückenloser Zahlenbereich. [a; b] heißt: a ≤ x ≤ b. Zeigt eine Klammer ⟦nach außen⟧, gehört die Grenze ⟦nicht⟧ dazu. Wie im Alltag: „Ab 3 Jahren“ – die 3 gehört dazu. „Unter 5 Jahren“ – die 5 gehört nicht dazu.',
     'schritte': ['[−2; 5[: Links zeigt die Klammer nach innen, −2 gehört dazu (gefüllter Punkt).', 'Rechts zeigt die Klammer nach außen, 5 gehört nicht dazu (leerer Kreis).', 'Also ⟦−2 ≤ x < 5⟧.'],
     'fehler': ']1; 4] heißt nicht 1 ≤ x ≤ 4. Die linke Klammer zeigt ⟦nach außen⟧, also gehört 1 nicht dazu: 1 < x ≤ 4.',
     'bild': {'typ': 'figur', 'punkte': {'_l': [-3.5, 0], '_r': [6.5, 0], '−2': [-2, 0], '_e': [5, 0]},
              'linien': [['_l', '_r', '', 'gestrichelt'], ['−2', '_e']], 'kreise': [{'m': [5, 0], 'r': 0.2, 'name': '5'}]}},
    {'lernziel': 'schreiben', 'titel': 'Zahlenbereiche als Intervall schreiben',
     'regel': '≤ und ≥ → Klammer ⟦nach innen⟧. < und > → Klammer ⟦nach außen⟧. Ist der Bereich nach einer Seite unbegrenzt, schreibst du ⟦−∞⟧ oder ⟦∞⟧ (unendlich) mit Klammer nach außen.',
     'schritte': ['Achterbahn: Mitfahren darf, wer ⟦mindestens⟧ 140 cm groß ist. Nach oben gibt es keine Grenze: x ≥ 140.',
                  'Die 140 gehört dazu: Klammer nach innen. Nach oben unbegrenzt: ∞ mit Klammer nach außen.', 'Intervall: ⟦[140; ∞[⟧'],
     'fehler': 'x > 3 ist nicht [3; ∞]. Die 3 gehört nicht dazu, also ]3; …, und bei ∞ steht ⟦immer⟧ eine Klammer nach außen: ]3; ∞[.'},
    {'lernziel': 'enthalten', 'titel': 'Welche Zahlen liegen im Intervall?',
     'regel': 'Eine Zahl liegt im Intervall, wenn sie ⟦zwischen den Grenzen⟧ liegt. Bei den Grenzen selbst entscheidet die ⟦Klammer⟧.',
     'schritte': ['Welche ganzen Zahlen liegen in ]−1; 3]?', '−1 nicht (Klammer außen), dann 0, 1, 2, 3 (Klammer innen).', 'Das sind ⟦4⟧ ganze Zahlen.'],
     'fehler': 'In ]−1; 3] liegen nicht nur ganze Zahlen: Auch 0,5 oder 2,99 gehören dazu. Ein Intervall enthält ⟦unendlich viele⟧ Zahlen.',
     '_verbot': [']−1; 3]']},
    {'lernziel': 'beurteilen', 'titel': 'Aussagen über Intervalle prüfen',
     'regel': 'Prüfe eine Aussage, indem du die ⟦Grenzen⟧ und die ⟦Klammern⟧ genau liest. Ein Gegenbeispiel genügt, um eine Aussage zu widerlegen.',
     'schritte': ['Aussage: „4 liegt in [0; 4[.“', 'Die rechte Klammer zeigt nach außen, 4 gehört nicht dazu.', 'Die Aussage ist ⟦falsch⟧.'],
     'fehler': '„[2; 5] und ]2; 5[ sind gleich“ ist falsch: Sie unterscheiden sich in den ⟦Grenzen⟧ 2 und 5.'},
]


def iv(lo, hi, li, ri):
    l = '[' if li else ']'
    r = ']' if ri else '['
    return f'{l}{"−∞" if lo is None else zt(lo)}; {"∞" if hi is None else zt(hi)}{r}'


def ug(lo, hi, li, ri):
    if lo is None and hi is None: return 'alle Zahlen'
    if lo is None: return f'x {"≤" if ri else "<"} {zt(hi)}'
    if hi is None: return f'x {"≥" if li else ">"} {zt(lo)}'
    return f'{zt(lo)} {"≤" if li else "<"} x {"≤" if ri else "<"} {zt(hi)}'


def drin(x, lo, hi, li, ri):
    if lo is not None and (x < lo or (x == lo and not li)): return False
    if hi is not None and (x > hi or (x == hi and not ri)): return False
    return True


def zufall_iv(R, st, unendlich=None):
    if unendlich is None: unendlich = st >= 2 and R.random() < .35
    if st == 3 and R.random() < .4:
        lo, hi = sorted(R.sample([Fr(k, 2) for k in range(-16, 17)], 2))
    else:
        lo, hi = map(Fr, sorted(R.sample(range(-9, 10), 2)))
    li, ri = R.random() < .5, R.random() < .5
    if unendlich:
        if R.random() < .5: lo, li = None, False
        else: hi, ri = None, False
    return lo, hi, li, ri


def bild(lo, hi, li, ri):
    """Intervall am Zahlenstrahl (Behelf mit Bildtyp figur): gefüllter Punkt = Grenze gehört dazu, leerer Kreis = gehört nicht dazu."""
    a = (lo if lo is not None else hi - 4)
    b = (hi if hi is not None else lo + 4)
    xa, xb = float(a) - 2.5, float(b) + 2.5
    P = {'_l': [xa, 0], '_r': [xb, 0]}
    lin = [['_l', '_r', '', 'gestrichelt']]
    kr = []
    ends = []
    for wert, dazu, rand in ((lo, li, '_l'), (hi, ri, '_r')):
        if wert is None:
            ends.append(rand); continue
        if dazu:
            P[zt(wert)] = [float(wert), 0]; ends.append(zt(wert))
        else:
            k = '_a' if rand == '_l' else '_b'
            P[k] = [float(wert), 0]; ends.append(k)
            kr.append({'m': [float(wert), 0], 'r': 0.25, 'name': zt(wert)})
    lin.append([ends[0], ends[1]])
    g = {'typ': 'figur', 'punkte': P, 'linien': lin}
    if kr: g['kreise'] = kr
    return g


def varianten(lo, hi, li, ri):
    """Typische Verwechslungen: Klammern vertauscht/umgedreht."""
    v = []
    if lo is not None: v.append((lo, hi, not li, ri))
    if hi is not None: v.append((lo, hi, li, not ri))
    if lo is not None and hi is not None: v.append((lo, hi, not li, not ri))
    if lo is None: v.append((hi, None, ri, False))
    if hi is None: v.append((None, lo, False, li))
    return v


def iv_fehler(lo, hi, li, ri):
    """Typischer Fehler: Klammer bei ∞ nach innen."""
    if hi is None: return iv(lo, hi, li, ri)[:-1] + ']'
    if lo is None: return '[' + iv(lo, hi, li, ri)[1:]
    return None


SACH_LESEN = [
    ('Auf dem Karussell dürfen Kinder mitfahren, die mindestens {a} m und kleiner als {b} m sind. Welches Intervall beschreibt die erlaubten Größen (in m)?', True, False,
     [(Fr(110, 100), Fr(140, 100)), (Fr(100, 100), Fr(130, 100)), (Fr(120, 100), Fr(150, 100))]),
    ('Ein Kühlschrank soll über {a} °C und höchstens {b} °C haben. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?', False, True,
     [(Fr(2), Fr(7)), (Fr(3), Fr(8)), (Fr(1), Fr(6))]),
    ('Ein Paket kostet den Normalpreis, wenn es mehr als {a} kg und bis einschließlich {b} kg wiegt. Welches Intervall beschreibt diese Gewichte (in kg)?', False, True,
     [(Fr(2), Fr(5)), (Fr(5), Fr(10)), (Fr(1), Fr(2))]),
    ('Ein Kinderticket gibt es ab {a} Jahren und für alle unter {b} Jahren. Welches Intervall beschreibt das Alter (in Jahren)?', True, False,
     [(Fr(6), Fr(14)), (Fr(4), Fr(15)), (Fr(6), Fr(16))]),
    ('Ein Aquarium braucht Wasser von mindestens {a} °C bis höchstens {b} °C. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?', True, True,
     [(Fr(24), Fr(28)), (Fr(22), Fr(26)), (Fr(23), Fr(27))]),
    ('Eine Bewertung „gut“ gibt es für mehr als {a} Punkte bis unter {b} Punkte. Welches Intervall beschreibt diese Punktzahlen?', False, False,
     [(Fr(30), Fr(40)), (Fr(40), Fr(50)), (Fr(25), Fr(35))]),
]


def g_lesen(R, st):
    if st == 3:
        t, li, ri, werte = R.choice(SACH_LESEN)
        lo, hi = R.choice(werte)
        I = iv(lo, hi, li, ri)
        return A(R, t.format(a=zt(lo), b=zt(hi)), I, [iv(*v) for v in varianten(lo, hi, li, ri)],
                 f'In Zeichen: {ug(lo, hi, li, ri)}. {"„mindestens“/„ab“/„bis einschließlich“: Grenze gehört dazu, Klammer nach innen. " if li or ri else ""}'
                 f'{"„über“/„mehr als“/„unter“/„kleiner als“: Grenze gehört nicht dazu, Klammer nach außen. " if not (li and ri) else ""}Intervall: {I}.',
                 'Übersetze jedes Wort an einer Grenze: gehört die Zahl dazu oder nicht?')
    lo, hi, li, ri = zufall_iv(R, st)
    if R.random() < .45:
        I = iv(lo, hi, li, ri)
        falsch = [iv(*v) for v in varianten(lo, hi, li, ri)]
        if iv_fehler(lo, hi, li, ri): falsch.append(iv_fehler(lo, hi, li, ri))
        return mit_bild(A(R, 'Welches Intervall zeigt das Bild? (Gefüllter Punkt: Grenze gehört dazu. Leerer Kreis: gehört nicht dazu. Strecke bis zum Rand: unbegrenzt.)',
                          I, falsch,
                          f'{"Linke Grenze gehört dazu" if li else ("links unbegrenzt" if lo is None else "linke Grenze gehört nicht dazu")}, '
                          f'{"rechte Grenze gehört dazu" if ri else ("rechts unbegrenzt" if hi is None else "rechte Grenze gehört nicht dazu")}: {I}.',
                          'Gefüllter Punkt → Klammer nach innen. Leerer Kreis → Klammer nach außen.'), bild(lo, hi, li, ri))
    I = iv(lo, hi, li, ri)
    w = (f'Linke Grenze {"−∞" if lo is None else zt(lo)}: ' + ('nach unten unbegrenzt' if lo is None else ('gehört dazu' if li else 'gehört nicht dazu')) +
         f'; rechte Grenze {"∞" if hi is None else zt(hi)}: ' + ('nach oben unbegrenzt' if hi is None else ('gehört dazu' if ri else 'gehört nicht dazu')) + f'. Also {ug(lo, hi, li, ri)}.')
    return A(R, f'Was bedeutet das Intervall {I}?', ug(lo, hi, li, ri), [ug(*v) for v in varianten(lo, hi, li, ri)], w,
             'Klammer nach innen: Grenze gehört dazu (≤). Klammer nach außen: Grenze gehört nicht dazu (<).')


WORTE = [
    ('alle Zahlen, die mindestens {a} sind', lambda a, b: (a, None, True, False)),
    ('alle Zahlen, die höchstens {a} sind', lambda a, b: (None, a, False, True)),
    ('alle Zahlen, die größer als {a} sind', lambda a, b: (a, None, False, False)),
    ('alle Zahlen, die kleiner als {a} sind', lambda a, b: (None, a, False, False)),
    ('alle Zahlen zwischen {a} und {b}, beide Grenzen eingeschlossen', lambda a, b: (a, b, True, True)),
    ('alle Zahlen zwischen {a} und {b}, beide Grenzen ausgeschlossen', lambda a, b: (a, b, False, False)),
    ('alle Zahlen ab {a} (einschließlich) und kleiner als {b}', lambda a, b: (a, b, True, False)),
    ('alle Zahlen größer als {a} bis einschließlich {b}', lambda a, b: (a, b, False, True)),
]


def g_schreiben(R, st):
    if st == 3:
        wort, f = R.choice(WORTE)
        a, b = map(Fr, sorted(R.sample(range(-12, 13), 2)))
        t = f(a, b)
        text = f'Schreibe als Intervall: {wort.format(a=zt(a), b=zt(b))}.'
        return A(R, text, iv(*t), ([iv_fehler(*t)] if iv_fehler(*t) else []) + [iv(*v) for v in varianten(*t)] + ([iv(t[0], t[1], not t[2], not t[3])] if None not in t[:2] else []),
                 f'In Zeichen: {ug(*t)}. Als Intervall: {iv(*t)}.', '„mindestens“ und „höchstens“ schließen die Grenze ein, „größer/kleiner als“ nicht.')
    lo, hi, li, ri = zufall_iv(R, st, unendlich=(st == 2 and R.random() < .5) or (st == 1 and R.random() < .3))
    if st == 2 and R.random() < .35:
        richtig = iv(lo, hi, li, ri)
        v = R.choice(varianten(lo, hi, li, ri) + ([None] if iv_fehler(lo, hi, li, ri) else []))
        falsch_iv = iv_fehler(lo, hi, li, ri) if v is None else iv(*v)
        ok = R.random() < .25
        gez = richtig if ok else falsch_iv
        opts = ['Richtig.', f'Falsch: richtig ist {richtig}.']
        if not ok:
            fehler_wo = ('bei ∞ steht immer eine Klammer nach außen' if v is None else
                         'die Klammer an einer Grenze zeigt in die falsche Richtung')
            opts[1] = f'Falsch: {fehler_wo}, richtig ist {richtig}.'
        ab = [f'Falsch: richtig ist {x}.' for x in [iv(*u) for u in varianten(lo, hi, li, ri)] if x not in (gez, richtig)]
        richtige = opts[0] if ok else opts[1]
        return A(R, f'Jemand schreibt {ug(lo, hi, li, ri)} als {gez}. Was stimmt?', richtige, [o for o in opts if o != richtige] + ab,
                 f'{ug(lo, hi, li, ri)} → {richtig}.' + ('' if ok else f' Gezeigt war {gez}.'),
                 'Übersetze selbst und vergleiche Klammer für Klammer.')
    falsch = [iv(*v) for v in varianten(lo, hi, li, ri)]
    if iv_fehler(lo, hi, li, ri): falsch.insert(0, iv_fehler(lo, hi, li, ri))
    return A(R, f'Schreibe {ug(lo, hi, li, ri)} als Intervall.', iv(lo, hi, li, ri), falsch,
             f'{ug(lo, hi, li, ri)} → {iv(lo, hi, li, ri)}.', '≤ / ≥: Klammer nach innen. < / >: Klammer nach außen. Bei ∞ immer nach außen.')


def ganze_in(lo, hi, li, ri):
    import math
    a = math.ceil(lo) if li else math.floor(lo) + 1
    b = math.floor(hi) if ri else math.ceil(hi) - 1
    return a, b


def g_enthalten(R, st):
    if st == 1:
        lo, hi, li, ri = zufall_iv(R, 1, unendlich=False)
        if hi - lo < 2: hi = lo + 3
        kand = sorted({lo, hi, lo - 1, hi + 1, (lo + hi) / 2, lo + Fr(1, 2)})
        rein = [x for x in kand if drin(x, lo, hi, li, ri)]
        raus = [x for x in kand if not drin(x, lo, hi, li, ri)]
        x0 = R.choice(rein)
        return A(R, f'Welche Zahl liegt im Intervall {iv(lo, hi, li, ri)}?', zt(x0), [zt(x) for x in R.sample(raus, min(3, len(raus)))],
                 f'{iv(lo, hi, li, ri)} bedeutet {ug(lo, hi, li, ri)}. {zt(x0)} erfüllt das.',
                 'Prüfe besonders die Grenzen: Welche Klammer steht dort?')
    if st == 2:
        lo, hi, li, ri = zufall_iv(R, 2, unendlich=False)
        if R.random() < .3:
            lo, hi = lo + Fr(R.choice([0, 1]), 2), hi
            if lo >= hi: hi = lo + 4
        a, b = ganze_in(lo, hi, li, ri)
        n = b - a + 1
        if n < 1: return g_enthalten(R, 2)
        return Z(f'Wie viele ganze Zahlen liegen im Intervall {iv(lo, hi, li, ri)}?', n, f'{b} - ({a}) + 1',
                 f'Die kleinste ganze Zahl darin ist {zt(a)}, die größte {zt(b)}. Anzahl: {zt(b)} − {"(" + zt(a) + ")" if a < 0 else zt(a)} + 1 = {n}.',
                 'Finde die kleinste und die größte ganze Zahl im Intervall. Achte auf die Klammern.')
    # Stufe 3: Schnitt zweier Intervalle, am Zahlenstrahl markieren oder Länge
    if R.random() < .4:
        return schnitt(R)
    lo, hi, li, ri = zufall_iv(R, 1, unendlich=False)
    if hi - lo < 2: hi = lo + 3
    if R.random() < .6:
        a, b = ganze_in(lo, hi, li, ri)
        welche = R.choice(['kleinste', 'größte'])
        x = a if welche == 'kleinste' else b
        return M(f'Markiere am Zahlenstrahl die {welche} ganze Zahl, die im Intervall {iv(lo, hi, li, ri)} liegt.', -10, 10, 20, int(x) + 10,
                 f'{iv(lo, hi, li, ri)} bedeutet {ug(lo, hi, li, ri)}. Die {welche} ganze Zahl darin ist {zt(x)}.',
                 'Gehört die Grenze dazu? Wenn nicht, gehe eine ganze Zahl weiter nach innen.')
    lo, hi = lo + Fr(R.choice([0, 1, -1]), 2), hi + Fr(R.choice([0, 1]), 2)
    return Z(f'Das Intervall {iv(lo, hi, li, ri)} ist ein Stück des Zahlenstrahls. Wie lang ist es?', hi - lo, f'{cz(hi)} - ({cz(lo)})',
             f'Länge = rechte Grenze − linke Grenze = {zt(hi)} − {"(" + zt(lo) + ")" if lo < 0 else zt(lo)} = {zt(hi - lo)}. Die Klammern ändern die Länge nicht.',
             'Rechne rechte Grenze minus linke Grenze.')


def schnitt(R):
    if R.random() < .2:
        a = Fr(R.randint(-6, 6))
        return A(R, f'Welche Zahlen liegen in ]−∞; {zt(a)}] und gleichzeitig in [{zt(a)}; ∞[?', f'nur die {zt(a)}',
                 ['keine Zahl', 'alle Zahlen', f']−∞; {zt(a)}['],
                 f'Im ersten Intervall: x ≤ {zt(a)}. Im zweiten: x ≥ {zt(a)}. Beides gilt nur für x = {zt(a)}.',
                 'Schreibe beide Intervalle als Ungleichung. Welche Zahl erfüllt beide?')
    while True:
        a, c, b, d = sorted(R.sample(range(-9, 10), 4))
        li, ri, lj, rj = (R.random() < .5 for _ in range(4))
        # I = [a; d], J = [c... ]: überlappend: I = (a, b'), J = (c', d)
        I = (Fr(a), Fr(b), li, ri)
        J = (Fr(c), Fr(d), lj, rj)
        if c < b: break
    S = (Fr(c), Fr(b), lj, ri)   # Schnitt: von c bis b
    richtig = iv(*S)
    falsch = [iv(Fr(a), Fr(d), li, rj), iv(Fr(c), Fr(b), not lj, ri), iv(Fr(c), Fr(b), lj, not ri)]
    return A(R, f'Welche Zahlen liegen in {iv(*I)} und gleichzeitig in {iv(*J)}?', richtig, falsch,
             f'{iv(*I)}: {ug(*I)}. {iv(*J)}: {ug(*J)}. Beides gilt von {zt(c)} ({"dazu" if lj else "nicht dazu"}, Grenze aus dem zweiten Intervall) '
             f'bis {zt(b)} ({"dazu" if ri else "nicht dazu"}, Grenze aus dem ersten): {richtig}.',
             'Der gemeinsame Teil beginnt bei der größeren linken Grenze und endet bei der kleineren rechten Grenze.')


def aussagen(R):
    """Liefert eine Liste (Text, wahr?) mit berechneten Wahrheitswerten."""
    lo, hi, li, ri = zufall_iv(R, 2, unendlich=False)
    if hi - lo < 2: hi = lo + 3
    I = iv(lo, hi, li, ri)
    a, b = ganze_in(lo, hi, li, ri)
    out = []
    for x in (lo, hi, lo + 1, hi + 1, lo - Fr(1, 2)):
        out.append((f'{zt(x)} liegt in {I}.', drin(x, lo, hi, li, ri)))
    n = b - a + 1
    k = R.choice([n, n + 1, n - 1, hi - lo])
    out.append((f'{I} enthält genau {zt(k)} ganze Zahlen.', k == n))
    J = (lo, hi, not li, ri)
    out.append((f'{I} und {iv(*J)} enthalten dieselben Zahlen.', False))
    out.append((f'{I} enthält unendlich viele Zahlen.', True))
    out.append((f'{I} bedeutet {ug(lo, hi, li, ri)}.', True))
    v = R.choice(varianten(lo, hi, li, ri))
    out.append((f'{I} bedeutet {ug(*v)}.', False))
    out.append((f'Die kleinste Zahl in {I} ist {zt(lo)}.', li))
    return I, out


def g_beurteilen(R, st):
    while True:
        I, al = aussagen(R)
        wahr = [t for t, w in al if w]; falsch = [t for t, w in al if not w]
        if len(wahr) >= 3 and len(falsch) >= 3: break
    if st == 1 or (st == 2 and R.random() < .5):
        t = R.choice(wahr)
        return A(R, f'Welche Aussage über {I} ist richtig?', t, R.sample(falsch, 3), f'Richtig ist: {t} Die anderen Aussagen scheitern an einer Grenze oder Klammer.',
                 'Prüfe jede Aussage an den Grenzen des Intervalls.')
    t = R.choice(falsch)
    hinweis = ''
    if 'kleinste Zahl' in t:
        hinweis = ' Gehört die linke Grenze nicht dazu, gibt es keine kleinste Zahl: Man kann ihr beliebig nahe kommen.'
    return A(R, f'Welche Aussage über {I} ist FALSCH?', t, R.sample(wahr, 3), f'Falsch ist: {t}{hinweis}',
             'Suche ein Gegenbeispiel – meist an einer Grenze.')


GEN = {'lesen': g_lesen, 'schreiben': g_schreiben, 'enthalten': g_enthalten, 'beurteilen': g_beurteilen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Schreibweise', ['lesen', 'schreiben']), ('Zahlen im Intervall', ['enthalten', 'beurteilen'])],
         'Zahlenbereiche mit offenen und geschlossenen Grenzen als Intervall lesen und schreiben.',
         ['[ ] nach innen: Grenze gehört dazu. ] [ nach außen: Grenze gehört nicht dazu.',
          'Bei −∞ und ∞ steht immer eine Klammer nach außen.',
          'Ein Intervall enthält unendlich viele Zahlen, nicht nur ganze.'],
         offen=['Intervall am Zahlenstrahl ist mit dem Bildtyp „figur“ nachgebaut (Behelf): gefüllter Punkt = Grenze gehört dazu, leerer Kreis = gehört nicht dazu, Strecke bis zum Rand = unbegrenzt. '
                'Ein eigener Bildtyp „intervall“ (Zahlenstrahl mit Endpunkten und Pfeil) wäre klarer – Vorschlag für den Haupt-Chat.',
                'Prüf-Vorschlag „FALSCH fett anzeigen“ nicht umgesetzt: Aufgabentexte werden ohne Hervorhebung angezeigt; das wäre App-Code. FALSCH steht weiter in Großbuchstaben.',
                'Lehrplanbezug: Intervalle werden in gleichungen.ungleichungen gebraucht; dieses Thema sollte im Plan davor stehen (Reihenfolge legt der Haupt-Chat fest).'])
