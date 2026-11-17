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


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'lesen': {
  'einstieg': 'Auf einem Spielzeug steht: „für Kinder von 3 bis unter 6 Jahren“. Erlaubt sind also 3-Jährige, 4-Jährige, 5-Jährige – und jedes Alter dazwischen, etwa 5 Jahre und 11 Monate. Wer schon 6 ist, gehört nicht mehr dazu. Für so einen lückenlosen Bereich gibt es in Mathe eine Kurzschrift: das ⟦Intervall⟧ [3; 6[.',
  'woerter': [['Intervall', 'ein lückenloser Zahlenbereich zwischen zwei Grenzen'], ['Grenze', 'die Zahl am Anfang oder am Ende des Bereichs'],
              ['[ … ] nach innen', 'die eckige Klammer zeigt zur Zahl hin: die Grenze gehört dazu'], ['] … [ nach außen', 'die Klammer zeigt von der Zahl weg: die Grenze gehört nicht dazu'],
              ['−2 ≤ x < 5', 'alle Zahlen x von −2 (mit −2) bis 5 (ohne 5)'], ['Punkt / Kreis im Bild', 'gefüllter Punkt: Grenze gehört dazu; leerer Kreis: gehört nicht dazu']],
  'schritte': ['Gegeben ist das Intervall [−2; 5[.', 'Links zeigt die Klammer zur −2 hin. Also gehört −2 dazu (gefüllter Punkt).',
               'Rechts zeigt die Klammer von der 5 weg. Also gehört 5 nicht dazu (leerer Kreis).', 'In Zeichen heißt das ⟦−2 ≤ x < 5⟧: alle Zahlen von −2 bis knapp unter 5.'],
  'regel': 'So liest du ein ⟦Intervall⟧: Schau jede ⟦Klammer⟧ einzeln an. Zeigt sie zur Zahl hin, gehört die Grenze dazu (≤). Zeigt sie von ihr weg, gehört sie nicht dazu (<).',
  'fehler': ']1; 4] heißt nicht 1 ≤ x ≤ 4. Die linke Klammer zeigt ⟦nach außen⟧, also gehört 1 nicht dazu: 1 < x ≤ 4. Wie bei „über 1 Jahr bis 4 Jahre“: Wer genau 1 Jahr alt ist, ist noch nicht dabei.'},
 'schreiben': {
  'einstieg': 'An der Achterbahn steht: „Mitfahren ab 140 cm.“ Eine obere Grenze gibt es nicht – auch sehr große Menschen dürfen mitfahren. Für „ohne Ende nach oben“ benutzt man das Zeichen ∞, gesprochen ⟦unendlich⟧.',
  'woerter': [['≥ und ≤', '„größer oder gleich“ bzw. „kleiner oder gleich“: die Grenze gehört dazu'], ['> und <', '„größer als“ bzw. „kleiner als“: die Grenze gehört nicht dazu'],
              ['∞', 'unendlich: der Bereich hört nach oben nie auf'], ['−∞', 'minus unendlich: der Bereich hört nach unten nie auf'], ['unbegrenzt', 'auf dieser Seite gibt es keine Grenze']],
  'schritte': ['Mitfahren darf, wer mindestens 140 cm groß ist. In Zeichen: x ≥ 140.', 'Die 140 gehört dazu, also zeigt die Klammer zur 140 hin: [140; …',
               'Nach oben gibt es keine Grenze. Dort steht ∞, und bei ∞ zeigt die Klammer immer nach außen.', 'Das Intervall heißt ⟦[140; ∞[⟧.'],
  'regel': 'So schreibst du ein Intervall: Bei ≤ und ≥ zeigt die Klammer ⟦nach innen⟧, bei < und > ⟦nach außen⟧. Ist der Bereich auf einer Seite ⟦unbegrenzt⟧, schreibst du −∞ oder ∞ – immer mit Klammer nach außen.',
  'fehler': 'x > 3 ist nicht [3; ∞]. Die 3 gehört nicht dazu, also ]3; … . Und ∞ ist keine Zahl, die man je erreicht – deshalb zeigt die Klammer dort ⟦immer⟧ nach außen: ]3; ∞[.'},
 'enthalten': {
  'einstieg': 'Ein Spiel ist „für Kinder über 1 bis einschließlich 3 Jahre“. Wer genau 1 Jahr alt ist, gehört nicht dazu, wer genau 3 ist, schon. Dazwischen passt jedes Alter, auch 2 Jahre und 4 Monate. Ein Intervall enthält also nicht nur ganze Zahlen, sondern ⟦unendlich viele⟧ Zahlen.',
  'woerter': [['ganze Zahlen', '…, −2, −1, 0, 1, 2, … – Zahlen ohne Komma'], ['enthalten', 'die Zahl liegt im Bereich'],
              ['unendlich viele', 'man kann sie nie fertig aufzählen, z. B. 0,5; 0,51; 0,501; …']],
  'schritte': ['Frage: Welche ganzen Zahlen liegen in ]−1; 3]?', 'Links zeigt die Klammer von der −1 weg. Also gehört −1 nicht dazu.',
               'Dann kommen 0, 1 und 2. Rechts zeigt die Klammer zur 3 hin, also gehört auch 3 dazu.', 'Gezählt: 0, 1, 2, 3 – das sind ⟦4⟧ ganze Zahlen.'],
  'regel': 'So prüfst du eine Zahl: Liegt sie ⟦zwischen den Grenzen⟧, gehört sie dazu. Ist sie genau eine Grenze, entscheidet die ⟦Klammer⟧.',
  'fehler': 'In ]−1; 3] liegen nicht nur 0, 1, 2 und 3. Auch 0,5 oder 2,99 gehören dazu – wie ein Kind mit 2 Jahren und 4 Monaten. Ein Intervall enthält ⟦unendlich viele⟧ Zahlen.'},
 'beurteilen': {
  'einstieg': 'Im Schwimmbad steht: „Eintritt frei für Kinder unter 4 Jahren.“ Dein Bruder hat heute seinen 4. Geburtstag. Muss er zahlen? Ja – „unter 4“ heißt: Die 4 gehört nicht dazu. Um so etwas sicher zu entscheiden, liest du Grenzen und Klammern genau und suchst notfalls ein ⟦Gegenbeispiel⟧.',
  'woerter': [['Aussage', 'ein Satz, der entweder wahr oder falsch ist'], ['Gegenbeispiel', 'ein einziger Fall, in dem die Aussage nicht stimmt – dann ist sie falsch']],
  'schritte': ['Aussage: „4 liegt in [0; 4[.“', 'Schau auf die rechte Grenze 4: Dort zeigt die Klammer von der 4 weg.',
               'Also gehört 4 nicht zum Intervall – wie beim Bruder an seinem 4. Geburtstag.', 'Die Aussage ist ⟦falsch⟧.'],
  'regel': 'So prüfst du eine Aussage über ein Intervall: ⟦Grenzen⟧ und ⟦Klammern⟧ genau lesen. Ein einziges ⟦Gegenbeispiel⟧ genügt, um eine Aussage zu widerlegen.'},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


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


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

UMBAU = {
 'lesen': {
  'einstieg': 'Auf einem Spielzeug steht: „für Kinder von 3 bis unter 6 Jahren“. Jedes Alter dazwischen passt, wer 6 ist, nicht mehr. Kurz schreibt man das als ⟦Intervall⟧ [3; 6[.',
  'woerter': [['Intervall', 'ein lückenloser Zahlenbereich zwischen zwei Grenzen'], ['[3; 6[', 'alle Zahlen von 3 bis knapp unter 6'], ['Grenze', 'die Zahl am Rand des Bereichs']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 8, 'abschnitte': 8, 'beschriftet': 'alle'},
  'schritte': [{'text': 'Die linke Klammer zeigt zur 3 hin: Die Grenze 3 gehört dazu.', 'bild': {'punkte': [{'wert': 3, 'name': '3 dabei'}]}},
               {'text': 'Die rechte Klammer zeigt von der 6 weg: 6 gehört nicht dazu.', 'bild': {'punkte': [{'wert': 3, 'name': '3 dabei'}, {'wert': 6, 'name': '6 nicht'}]}},
               {'text': 'Dazwischen ist alles dabei: ⟦3 ≤ x < 6⟧.', 'bild': {'bereich': {'von': 3, 'bis': 6}}}],
  'fehler': ']3; 6[ ist etwas anderes: Ein Kind, das genau 3 ist, wäre dann nicht dabei. Die Klammer bei der 3 zeigt dort ⟦nach außen⟧.',
  'fehler_bild': {'punkte': [{'wert': 3, 'name': '3 nicht'}, {'wert': 6, 'name': '6 nicht'}]},
  'regel': 'Zeigt die Klammer ⟦zur Zahl hin⟧, gehört die Grenze dazu. Zeigt sie weg, gehört sie nicht dazu.'},
 'schreiben': {
  'einstieg': 'An der Achterbahn steht: „Mitfahren ab 140 cm.“ Nach oben gibt es keine Grenze. Für „ohne Ende“ schreibt man ∞, gesprochen ⟦unendlich⟧.',
  'woerter': [['∞', '„unendlich“: Der Bereich hört nie auf'], ['x ≥ 140', 'x ist 140 oder mehr']],
  'bild': {'typ': 'zahlenstrahl', 'start': 100, 'ende': 200, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Mindestens 140 cm heißt: x ≥ 140.', 'bild': {'punkte': [{'wert': 140, 'name': '140'}], 'bereich': {'von': 140, 'bis': 200}}},
               {'text': 'Die 140 gehört dazu, die Klammer zeigt zu ihr hin: [140.'},
               {'text': 'Nach oben steht ∞, mit Klammer nach außen: ⟦[140; ∞[⟧.'}],
  'fehler': ']140; ∞[ wäre falsch: Wer genau 140 cm misst, dürfte dann nicht mitfahren. Bei ∞ zeigt die Klammer ⟦immer⟧ nach außen.',
  'fehler_bild': {'punkte': [{'wert': 140, 'name': '140 nicht?'}]},
  'regel': 'Bei ≤ und ≥ zeigt die Klammer ⟦nach innen⟧, sonst nach außen. Bei ∞ und −∞ zeigt sie immer nach außen.'},
 'enthalten': {
  'einstieg': 'Ein Spiel ist „für Kinder über 1 bis einschließlich 3 Jahre“. Wer genau 1 ist, gehört nicht dazu, wer genau 3 ist, schon. Das Intervall dazu ist ⟦]1; 3]⟧.',
  'woerter': [[']1; 3]', 'alle Zahlen über 1 bis einschließlich 3'], ['einschließlich', 'mit dabei']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 5, 'abschnitte': 10, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Die 1 gehört nicht dazu, die Klammer zeigt weg.', 'bild': {'punkte': [{'wert': 1, 'name': '1 nicht'}]}},
               {'text': 'Die 3 gehört dazu, die Klammer zeigt zu ihr hin.', 'bild': {'punkte': [{'wert': 1, 'name': '1 nicht'}, {'wert': 3, 'name': '3 dabei'}], 'bereich': {'von': 1, 'bis': 3}}},
               {'text': 'Ganze Zahlen darin sind 2 und 3. Das sind ⟦2 ganze Zahlen⟧.', 'bild': {'punkte': [{'wert': 1, 'name': '1 nicht'}, {'wert': 2, 'name': '2'}, {'wert': 3, 'name': '3 dabei'}]}},
               {'text': 'Dazu kommen alle Zahlen dazwischen, etwa 2,5. Das sind ⟦unendlich viele⟧.'}],
  'fehler': 'Ein Intervall enthält nicht nur ganze Zahlen. Ein Kind mit 2 Jahren und 6 Monaten passt auch – das ist 2,5.',
  'fehler_bild': {'punkte': [{'wert': 1, 'name': '1 nicht'}, {'wert': 2.5, 'name': '2,5 auch'}, {'wert': 3, 'name': '3 dabei'}]},
  'regel': 'Eine Zahl gehört dazu, wenn sie ⟦zwischen den Grenzen⟧ liegt. Liegt sie genau auf einer Grenze, entscheidet die Klammer.'},
 'beurteilen': {
  'einstieg': 'Im Schwimmbad steht: „Eintritt frei unter 4 Jahren.“ Dein Bruder wird heute 4 – muss er zahlen? Solche Aussagen prüfst du an Grenzen und Klammern, oft mit einem ⟦Gegenbeispiel⟧.',
  'woerter': [['Gegenbeispiel', 'ein Fall, bei dem die Aussage nicht stimmt'], ['[0; 4[', 'alle Zahlen von 0 bis knapp unter 4']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 6, 'abschnitte': 6, 'beschriftet': 'alle', 'bereich': {'von': 0, 'bis': 4}},
  'schritte': [{'text': 'Aussage: „4 liegt in [0; 4[.“ Dann hätte der Bruder freien Eintritt.'},
               {'text': 'Die Klammer bei der 4 zeigt weg. Die 4 gehört nicht dazu.', 'bild': {'punkte': [{'wert': 4, 'name': '4 nicht'}]}},
               {'text': 'Die 4 ist ein Gegenbeispiel. Die Aussage ist ⟦falsch⟧ – er zahlt.'}],
  'fehler': '[2; 5] und ]2; 5[ sind nicht gleich. Sie unterscheiden sich an den ⟦Grenzen⟧: Die 2 und die 5 gehören nur zum ersten.',
  'regel': 'Lies ⟦Grenzen und Klammern⟧ genau. Ein einziges Gegenbeispiel genügt, um eine Aussage zu widerlegen.'},
}
UMBAU_OFFEN = ['Umbau 16.11.: Die Lernkarten zeigen Intervalle jetzt auf dem Zahlenstrahl mit „bereich“ und benannten Punkten („3 dabei“, „6 nicht“). '
               'App-Wunsch: Endpunkte des Bereichs als gefüllter bzw. leerer Kreis (z. B. "bereich": {"von": 3, "bis": 6, "links": "zu", "rechts": "offen"}) und ein Pfeil für „bis ∞“.']
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): Eigene Prüfungsaufgaben nur zu Intervallen wurden nicht gefunden. Vorbild sind
# BMT10 2022 (Schnitt- und Vereinigungsmenge von Lösungsmengen), Schulaufgaben-Typ Kl. 8 (Lösungsmenge einer Ungleichung als Intervall),
# BMT8 2025 (Aussage begründet widerlegen) und Sachbedingungen mit „ab / bis einschließlich / unter“ wie in VERA-Sachaufgaben.
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402

SW = Neu(10_8_8)

# lesen
SW.a('lesen', 2, 'Was bedeutet das Intervall ]−∞; 2,5]?', 'x ≤ 2,5', ['x < 2,5', 'x ≥ 2,5', '−∞ ≤ x ≤ 2,5'],
     'Links unbegrenzt, rechts gehört 2,5 dazu (Klammer zeigt zur Zahl): x ≤ 2,5.', 'Lies jede Klammer einzeln.')
SW.a('lesen', 2, 'Was bedeutet das Intervall [−1,5; 0[?', '−1,5 ≤ x < 0', ['−1,5 < x ≤ 0', '−1,5 ≤ x ≤ 0', '−1,5 < x < 0'],
     'Links zeigt die Klammer zur −1,5: dabei. Rechts zeigt sie von der 0 weg: nicht dabei.', 'Zur Zahl hin: dabei. Von der Zahl weg: nicht dabei.')
SW.a('lesen', 3, 'Im Zoo gilt: Kinder ab 6 Jahren bis einschließlich 14 Jahren zahlen den Kinderpreis. Jugendliche über 14 bis unter 18 Jahren zahlen den Jugendpreis. Welches Intervall beschreibt das Alter (in Jahren) für den Jugendpreis?',
     ']14; 18[', ['[14; 18[', ']14; 18]', '[6; 18['],
     '„über 14“: 14 gehört nicht dazu (14-Jährige zahlen den Kinderpreis). „unter 18“: 18 gehört nicht dazu. Also ]14; 18[.', 'Wer genau 14 ist, zahlt welchen Preis?', art='P')
SW.a('lesen', 3, 'Welche Zahlen liegen in [−2; 5[, aber nicht in [−2; 1]?', ']1; 5[', ['[1; 5[', ']1; 5]', '[−2; 1['],
     'Aus [−2; 5[ fallen alle Zahlen von −2 bis 1 (mit 1) weg. Übrig bleibt alles über 1 bis unter 5: ]1; 5[.', 'Zeichne beide Bereiche auf einen Zahlenstrahl. Gehört die 1 zum Rest?', art='P')
SW.z('lesen', 3, 'Das Intervall [a; a + 3[ enthält genau die ganzen Zahlen 4, 5 und 6. a ist eine ganze Zahl. Welche?', 4, '4',
     'Die kleinste ganze Zahl im Intervall ist a selbst (Klammer zur Zahl). Also a = 4. Dann [4; 7[: 4, 5, 6 – die 7 gehört nicht dazu.', 'Welche Grenze gehört dazu, welche nicht?', art='K')
SW.z('lesen', 3, 'Wie viele Zahlen mit genau einer Nachkommastelle (z. B. 1,3) liegen im Intervall ]1; 2[?', 9, '9',
     '1,1; 1,2; …; 1,9 – das sind 9 Zahlen. 1,0 und 2,0 haben keine echte Nachkommastelle und sind außerdem Grenzen, die nicht dazugehören.',
     'Zähle 1,1; 1,2; … auf.', art='K')

# schreiben
SW.a('schreiben', 2, 'Schreibe als Intervall: alle Zahlen, die kleiner als 0,5 sind.', ']−∞; 0,5[', [']−∞; 0,5]', ']0,5; ∞[', '[−∞; 0,5['],
     'x < 0,5: nach links unbegrenzt, 0,5 gehört nicht dazu. Bei −∞ zeigt die Klammer immer nach außen.', '„kleiner als“: Grenze nicht dabei.')
SW.a('schreiben', 2, 'Schreibe −4 ≤ x < −1,5 als Intervall.', '[−4; −1,5[', [']−4; −1,5]', '[−4; −1,5]', '[−1,5; −4['],
     '≤ bei −4: Klammer zur Zahl. < bei −1,5: Klammer von der Zahl weg. Die kleinere Zahl steht links.', 'Die kleinere Grenze steht immer links.')
SW.a('schreiben', 3, 'Ein Gerät darf bei −10 °C bis 40 °C betrieben werden, 40 °C selbst ist aber schon zu warm. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?',
     '[−10; 40[', [']−10; 40]', '[−10; 40]', '[40; −10['], '−10 °C ist erlaubt (Klammer zur Zahl), 40 °C nicht (Klammer weg).', 'Übersetze erst in eine Ungleichung.', art='P')
SW.a('schreiben', 3, 'Löse 2x − 3 > 4 und schreibe die Lösungsmenge als Intervall.', ']3,5; ∞[', ['[3,5; ∞[', ']−∞; 3,5[', ']0,5; ∞['],
     '2x > 7 ⇔ x > 3,5. Die 3,5 gehört nicht dazu: ]3,5; ∞[.', 'Erst lösen, dann schreiben.', art='P')
SW.a('schreiben', 3, 'Schreibe als Intervall: alle Zahlen, deren Abstand zur Zahl 2 höchstens 3 beträgt.', '[−1; 5]', [']−1; 5[', '[2; 5]', '[−3; 3]'],
     'Von 2 aus 3 nach links: −1, 3 nach rechts: 5. „Höchstens“: Grenzen gehören dazu. [−1; 5].', 'Gehe vom Mittelpunkt 2 aus in beide Richtungen.', art='K')
SW.a('schreiben', 3, 'Schreibe als Intervall: alle Zahlen, die nicht negativ sind.', '[0; ∞[', [']0; ∞[', ']−∞; 0]', ']−∞; 0['],
     '„Nicht negativ“ heißt: positiv oder 0. Die 0 gehört dazu: [0; ∞[.', 'Ist 0 negativ?', art='K')

# enthalten
SW.z('enthalten', 2, 'Wie viele ganze Zahlen liegen im Intervall ]−2,5; 3,5]?', 6, '3 - (-2) + 1', 'Ganze Zahlen von −2 bis 3: −2, −1, 0, 1, 2, 3 – das sind 6.',
     'Die Grenzen sind keine ganzen Zahlen. Suche die kleinste und größte ganze Zahl dazwischen.')
SW.a('enthalten', 2, 'Welche Zahl liegt NICHT im Intervall ]−3; 1]?', '−3', ['−2,9', '0', '1'], 'Die Klammer bei −3 zeigt weg: −3 gehört nicht dazu. −2,9, 0 und 1 liegen darin.',
     'Prüfe besonders die Grenzen.')
SW.a('enthalten', 3, 'Welche Zahlen liegen in ]−1; 4] und gleichzeitig in [2; 6[?', '[2; 4]', [']−1; 6[', ']2; 4[', '[2; 4['],
     'Gemeinsamer Teil: ab 2 (aus dem zweiten Intervall, 2 dabei) bis 4 (aus dem ersten, 4 dabei). Also [2; 4].', 'Größere linke Grenze, kleinere rechte Grenze. Klammern mitnehmen.', art='P')
SW.a('enthalten', 3, 'Welche Zahlen liegen in [−3; 0[ oder in [0; 2]?', '[−3; 2]', ['[−3; 0[', ']−3; 2[', '[−3; 2] ohne die 0'],
     'Das erste Intervall endet knapp vor 0, das zweite beginnt mit 0. Zusammen ist es lückenlos von −3 bis 2: [−3; 2].', '„oder“: Es genügt, in einem der Intervalle zu liegen. Wo liegt die 0?', art='P')
SW.z('enthalten', 3, 'Das Intervall ]a; 7] enthält genau 4 ganze Zahlen. a ist eine ganze Zahl. Bestimme a.', 3, '7 - 4',
     'Die 7 gehört dazu. Vier ganze Zahlen: 7, 6, 5, 4. Also gehört 3 nicht mehr dazu – das ist die offene Grenze a = 3.', 'Zähle von 7 abwärts. Die Grenze a gehört nicht dazu.', art='K')
SW.z('enthalten', 3, 'Wie viele Brüche mit dem Nenner 4 (1/4, 2/4, 3/4, …) liegen im Intervall ]0; 2[?', 7, '8 - 1',
     '2 = 8/4. Dazwischen liegen 1/4, 2/4, …, 7/4 – also 7 Brüche. 0/4 und 8/4 sind die Grenzen und gehören nicht dazu.', 'Schreibe die Grenzen als Viertel.', art='K')

# beurteilen
SW.a('beurteilen', 2, 'Welche Aussage über ]2; 3[ ist richtig?', 'Es enthält keine ganze Zahl.', ['Es enthält genau eine Zahl.', '2,999 liegt nicht darin.', 'Es ist leer.'],
     'Zwischen 2 und 3 liegen unendlich viele Zahlen (2,5; 2,999 …), aber keine ganze: 2 und 3 gehören nicht dazu.', 'Denke an Kommazahlen zwischen 2 und 3.')
SW.a('beurteilen', 2, 'Stimmt die Aussage: „]−∞; 0[ enthält genau alle negativen Zahlen“?', 'Ja.', ['Nein, die 0 fehlt noch.', 'Nein, −∞ gehört auch dazu.', 'Nein, nur die ganzen negativen Zahlen.'],
     ']−∞; 0[ heißt x < 0. Das sind genau die negativen Zahlen. 0 ist nicht negativ, −∞ ist keine Zahl.', 'Übersetze in eine Ungleichung.')
SW.a('beurteilen', 3, 'Tim sagt: „Im Intervall [0; 1] liegen nur die Zahlen 0 und 1.“ Was stimmt?', 'Falsch: Auch 0,5 oder 0,01 liegen darin – unendlich viele Zahlen.',
     ['Richtig: Die Klammern zeigen nur auf 0 und 1.', 'Falsch: 0 und 1 gehören nicht dazu.', 'Richtig: Ein Intervall enthält nur ganze Zahlen.'],
     '[0; 1] bedeutet 0 ≤ x ≤ 1. Jede Zahl dazwischen gehört dazu, z. B. 0,5. Ein Gegenbeispiel widerlegt Tims Aussage.', 'Suche eine Zahl zwischen 0 und 1.', art='P')
SW.a('beurteilen', 3, 'Lisa sagt: „]1; 5[ ist länger als [1; 5], weil die Klammern nach außen zeigen.“ Was stimmt?', 'Falsch: Beide sind 4 lang. Die Klammern ändern nur, ob 1 und 5 dazugehören.',
     ['Richtig: ]1; 5[ ist länger.', 'Falsch: [1; 5] ist länger, weil die Grenzen dazugehören.', 'Falsch: ]1; 5[ ist 3 lang.'],
     'Länge = rechte Grenze − linke Grenze = 5 − 1 = 4, bei beiden. Einzelne Punkte haben keine Länge.', 'Wie berechnet man die Länge eines Intervalls?', art='P')
SW.a('beurteilen', 3, 'Welche Zahlen enthält das Intervall [5; 5]?', 'genau die Zahl 5', ['keine Zahl', 'alle Zahlen ab 5', 'unendlich viele Zahlen'],
     '[5; 5] bedeutet 5 ≤ x ≤ 5. Das erfüllt nur x = 5. (]5; 5[ wäre dagegen leer.)', 'Schreibe als Ungleichung.', art='K')
SW.a('beurteilen', 3, 'Welche Aussage über JEDES Intervall [a; b] mit a < b ist FALSCH?', 'Es enthält mindestens eine ganze Zahl.',
     ['Es enthält unendlich viele Zahlen.', 'Es enthält a und b.', 'Es ist genauso lang wie ]a; b[.'],
     'Gegenbeispiel: [0,2; 0,8] enthält keine ganze Zahl. Die anderen Aussagen stimmen immer.', 'Suche ein kurzes Intervall zwischen zwei ganzen Zahlen.', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('zahlen.intervalle', 13_8_8)
# c) Beinahe-Dublette (Aquarium zweimal) → andere Grenzenart
BF.ersetze('lesen', 'Ein Aquarium braucht Wasser von mindestens 24 °C bis höchstens 28 °C. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?', BF.A(
    'Ein Impfstoff muss im Kühlschrank bei mehr als 2 °C, aber höchstens 8 °C gelagert werden. Welches Intervall beschreibt die erlaubten Temperaturen (in °C)?', ']2; 8]',
    ['[2; 8]', ']2; 8[', '[2; 8['],
    'In Zeichen: 2 < x ≤ 8. „mehr als“: Grenze gehört nicht dazu, Klammer nach außen. „höchstens“: Grenze gehört dazu, Klammer nach innen. Intervall: ]2; 8].',
    'Übersetze jedes Wort an einer Grenze: gehört die Zahl dazu oder nicht?'))
# a) reine Übersetzung ohne Zusatzschritt → Stufe 2
BF.stufe('schreiben', 'Schreibe als Intervall: alle Zahlen zwischen −5 und −3, beide Grenzen eingeschlossen.', 2)
BF.stufe('schreiben', 'Schreibe als Intervall: alle Zahlen zwischen −9 und −1, beide Grenzen eingeschlossen.', 2)
BF.stufe('schreiben', 'Schreibe als Intervall: alle Zahlen zwischen −12 und 8, beide Grenzen ausgeschlossen.', 2)
BF.nicht_umgesetzt('enthalten S1 „Welche Zahl liegt im Intervall [1; 7]?“ hat nur 3 Antworten', 'Zulässig und richtig; kein Fehler.')
BF.fuer_sebastian('zahlen.intervalle: lehrplan_gym der Karten ist leer – das Thema hat keine eigene LehrplanPLUS-Zeile (Inhalt gehört zu Ungleichungen, Kl. 8). Karten-Text nicht geändert.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DS = Durchsicht('zahlen.intervalle', 19_8_3)
# schreiben: eine Ungleichung mit einer Grenze in ein Intervall übersetzen ist Stufe 1; in Worten gegebene Grenze ist Stufe 2
for _t in ['Schreibe x ≤ 5 als Intervall.', 'Schreibe x ≥ −3 als Intervall.', 'Schreibe x > 6 als Intervall.', 'Schreibe x ≥ −8 als Intervall.', 'Schreibe x ≥ 7 als Intervall.']:
    DS.stufe('schreiben', _t, 1)
DS.stufe('schreiben', 'Schreibe als Intervall: alle Zahlen, die mindestens −12 sind.', 2)
DS.stufen('schreiben', 'S1/S2 weitgehend dieselbe Übersetzung x ≥ a; S3 teils Worte wie S2',
          'S1 Ungleichung → Intervall; S2 in Worten, Fehler finden, Dezimalgrenzen; S3 Sachkontext, Ungleichung erst lösen, Abstand, „nicht negativ“')
# beurteilen: „Welche Aussage ist FALSCH?“ mit Zufallsintervall ist auf Stufe 2 und 3 derselbe Gedanke
for _t in ['Welche Aussage über ]−7; 6[ ist FALSCH?', 'Welche Aussage über ]−5; 0] ist FALSCH?', 'Welche Aussage über [−3; 9] ist FALSCH?', 'Welche Aussage über [−8; 3[ ist FALSCH?']:
    DS.stufe('beurteilen', _t, 2)
DS.stufen('beurteilen', 'S1 richtige Aussage wählen; S2 und S3 dieselbe „FALSCH“-Aufgabe mit anderem Intervall',
          'S1 richtige Aussage wählen; S2 falsche Aussage finden, Sonderfälle ]2; 3[ und ]−∞; 0[; S3 Fehlvorstellungen (nur Grenzen, Länge), [5; 5], Aussage über jedes Intervall')
DS.stufen('lesen', 'S1 Intervall in Ungleichung; S2 Bild lesen, ∞, Dezimalgrenzen; S3 Sachkontext, Differenz zweier Intervalle, Parameter a, Anzahl Dezimalzahlen')
DS.stufen('enthalten', 'S1 Zahl im Intervall wählen; S2 ganze Zahlen zählen; S3 Schnitt und Vereinigung, Länge, Parameter, Brüche zählen')
baue = mit_durchsicht(baue, DS)
# ---- DURCHSICHT ENDE ----

# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, mit_stufen  # noqa: E402

ST = Stufen('zahlen.intervalle', 20_8_2)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)

# --- lesen ---
ST.leiter('lesen', 'Intervallschreibweise in Worte/Ungleichung übersetzen, Intervall am Bild erkennen',
          'Sachgrenzen („ab“, „bis einschließlich“) als Intervall, Intervall aus Anfang und Länge, Ungleichungspaar ↔ Intervall',
          'Mengen verknüpfen (ohne, zugleich), Parameter, Fehler beim Lesen deuten, Unendlichkeit begründen, rückwärts aus Mitte und Länge')
T('lesen', (r'^Was bedeutet', 'direkt'), (r'^Welches Intervall zeigt', 'erkennen'), (r'Zoo|Nachkommastelle', 'transfer'),
  (r'aber nicht in', 'verknuepfen'), (r'\[a; a \+ 3\[', 'parameter'), (r'Aquarium|Karussell|Impfstoff|Paket', 'einkleidung'))
ST.neu('lesen', 'umkehr', SA('Ein Intervall beginnt bei −2 (gehört dazu) und ist 5 lang; das rechte Ende gehört nicht dazu. Welches Intervall ist es?', '[−2; 3[', ['[−2; 3]', ']−2; 3[', '[−2; 7['],
    'Rechtes Ende: −2 + 5 = 3. Links gehört −2 dazu: [ ; rechts nicht: 3[.', 'Rechne zuerst das rechte Ende aus.'))
ST.neu('lesen', 'darstellung', SA('Welches Intervall beschreibt „x ≥ −1 und zugleich x < 4“?', '[−1; 4[', [']−1; 4]', '[−1; 4]', ']−∞; 4['],
    'x ≥ −1: −1 gehört dazu. x < 4: 4 gehört nicht dazu. Zusammen [−1; 4[.', 'Übersetze jede Ungleichung in eine Grenze mit Klammer.'))
ST.neu('lesen', 'fehler', SA('Jemand liest ]−3; 2] als „alle Zahlen von −3 bis 2, beide gehören dazu“. Was ist falsch?', 'Die −3 gehört nicht dazu, nur die 2.',
    ['Nichts, das stimmt.', 'Die 2 gehört nicht dazu, nur die −3.', 'Keine der beiden Grenzen gehört dazu.'],
    'Bei −3 zeigt die Klammer nach außen ( ] ): −3 gehört nicht dazu. Bei 2 zeigt sie nach innen ( ] am Ende ): 2 gehört dazu.', 'Schau jede Klammer einzeln an: zeigt sie zur Zahl hin oder weg?'))
ST.neu('lesen', 'begruenden', SA('Stimmt die Aussage: „Jedes Intervall ]a; b[ mit a < b enthält unendlich viele Zahlen“?', 'Ja: Zwischen zwei verschiedenen Zahlen liegen immer unendlich viele weitere.',
    ['Nein, nur wenn b − a größer als 1 ist.', 'Nein, ohne die Grenzen bleibt nichts übrig.', 'Ja, aber es sind nur ganze Zahlen.'],
    'Zwischen a und b liegt die Mitte, zwischen a und der Mitte wieder eine Mitte usw. – das hört nie auf. Ganz kleine Intervalle wie ]0; 0,001[ enthalten also unendlich viele Zahlen.', 'Denk an die Mitte zwischen zwei Zahlen – und dann wieder an eine Mitte.'))
ST.neu('lesen', 'rueckwaerts', SZ('Ein Intervall [a; b] hat die Mitte 3 und die Länge 10. Bestimme a.', -2, '3 - 10 / 2',
    'Von der Mitte aus geht es je die halbe Länge, also 5, nach links und rechts: a = 3 − 5 = −2, b = 8.', 'Wie weit ist die Mitte von jeder Grenze entfernt?'))
ST.neu('lesen', 'pruefung', SA('A = [−4; 1[ und B = ]−1; 3]. Welche Menge enthält genau die Zahlen, die in A oder in B (oder in beiden) liegen?', '[−4; 3]', [']−1; 1[', '[−4; 3[', ']−4; 3]'],
    'A reicht von −4 (dabei) bis 1, B von −1 bis 3 (dabei). Die Teile überlappen, zusammen also von −4 bis 3, beide Enden dabei: [−4; 3]. ]−1; 1[ wären nur die gemeinsamen Zahlen.', 'Zeichne beide Intervalle untereinander an einen Zahlenstrahl.'))
ST.knobel('lesen', SZ('Wie viele Intervalle [a; b] mit ganzen Zahlen a und b und 0 ≤ a < b ≤ 5 gibt es?', 15, '6 * 5 / 2',
    'Man wählt zwei verschiedene Zahlen aus 0, 1, 2, 3, 4, 5; die kleinere ist a, die größere b. Für a = 0 gibt es 5 Möglichkeiten für b, für a = 1 vier, … für a = 4 eine: 5 + 4 + 3 + 2 + 1 = 15.',
    'Ordne nach der linken Grenze a und zähle für jedes a die möglichen b.'))
ST.knobel('lesen', SZ('Das Intervall [a; b] enthält genau 5 ganze Zahlen, das Intervall ]a; b[ genau 3. Wie lang ist das Intervall?', 4, '5 - 1',
    'Lässt man die Grenzen weg, fallen genau 2 ganze Zahlen weg – also sind a und b selbst ganze Zahlen. [a; b] enthält dann a, a + 1, …, b, das sind b − a + 1 = 5 Zahlen. Also b − a = 4.',
    'Warum fallen beim Weglassen der Grenzen genau zwei ganze Zahlen weg?'))

# --- schreiben ---
ST.leiter('schreiben', 'eine Doppelungleichung als Intervall schreiben, die passende Schreibweise erkennen',
          'Zahlenbereiche aus Worten, Sachbereiche und gelöste Ungleichungen als Intervall',
          'Abstand und „nicht negativ“ deuten, Brüche/Dezimalzahlen verknüpfen, Parameter, rückwärts umrechnen, begründen, wann es kein einziges Intervall gibt')
T('schreiben', (r'^Schreibe (?!als)', 'direkt'), (r'^Jemand schreibt', 'fehler'), (r'^Schreibe als Intervall: alle Zahlen, deren Abstand|nicht negativ', 'transfer'),
  (r'^Schreibe als Intervall', 'darstellung'), (r'^Ein Gerät', 'einkleidung'), (r'^Löse', 'mehrschritt'))
ST.neu('schreiben', 'erkennen', SA('Welche Schreibweise passt zu „x liegt zwischen 1 und 2, 1 gehört dazu, 2 nicht“?', '[1; 2[', [']1; 2]', '[1; 2]', ']1; 2['],
    'Gehört eine Grenze dazu, zeigt die Klammer zur Zahl hin. Also links [1, rechts 2[.', 'Welche Grenze gehört dazu?'))
ST.neu('schreiben', 'verknuepfen', SA('Schreibe als Intervall: alle Zahlen, die größer als 1/4 und höchstens 3/4 sind (mit Dezimalzahlen).', ']0,25; 0,75]', ['[0,25; 0,75[', ']0,25; 0,75[', '[0,25; 0,75]'],
    '1/4 = 0,25 (gehört nicht dazu), 3/4 = 0,75 (gehört dazu): ]0,25; 0,75].', 'Wandle die Brüche um und entscheide für jede Grenze.'))
ST.neu('schreiben', 'parameter', SZ('Für welche Zahl k ist [k; 2k] ein Intervall der Länge 6?', 6, '12 - 6',
    'Länge = rechte Grenze − linke Grenze = 2k − k = k. Also k = 6, das Intervall ist [6; 12].', 'Schreibe die Länge mit k.'))
ST.neu('schreiben', 'rueckwaerts', SA('Jede Zahl eines Intervalls wird verdoppelt, dann wird 1 addiert. Heraus kommt [−1; 7]. Wie hieß das Intervall vorher?', '[−1; 3]', ['[−2; 6]', '[0; 4]', '[−1; 7]'],
    'Rückwärts: erst 1 abziehen, dann halbieren. −1 → −2 → −1; 7 → 6 → 3. Also [−1; 3].', 'Mach die Schritte in umgekehrter Reihenfolge rückgängig.'))
ST.neu('schreiben', 'pruefung', SZ('Schreibe die Zahlen, die mindestens 2,5 und kleiner als 7 sind, als Intervall und gib seine Länge an.', 4.5, '7 - 25 / 10',
    'Das Intervall ist [2,5; 7[. Seine Länge ist 7 − 2,5 = 4,5 (ob die Grenzen dazugehören, ändert die Länge nicht).', 'Länge = rechte Grenze − linke Grenze.'))
ST.neu('schreiben', 'begruenden', SA('Kann man „alle Zahlen außer 0“ als ein einziges Intervall schreiben?', 'Nein: Es sind zwei getrennte Teile, ]−∞; 0[ und ]0; ∞[.',
    ['Ja: ]−∞; ∞[.', 'Ja: ]0; ∞[.', 'Ja: [−∞; ∞].'], 'Ein Intervall hat keine Lücke. „Alle außer 0“ hat bei 0 ein Loch, deshalb braucht man zwei Intervalle.', 'Hat ein Intervall Lücken?'))
ST.knobel('schreiben', SZ('Für welche Zahlen x liegt x² im Intervall [4; 9]? Die Lösung besteht aus zwei Intervallen. Wie lang sind beide zusammen?', 2, '(3 - 2) + (-2 - (-3))',
    'x² zwischen 4 und 9 gilt für 2 ≤ x ≤ 3, aber auch für negative x: (−3)² = 9, (−2)² = 4. Also [−3; −2] und [2; 3]. Jedes ist 1 lang, zusammen 2.',
    'Vergiss die negativen Zahlen nicht.'))
ST.knobel('schreiben', SZ('Wie viele Intervalle [a; b] mit ganzen Grenzen haben die Länge 5 und enthalten die Zahl 0?', 6, '0 - (-5) + 1',
    'b = a + 5. 0 liegt darin, wenn a ≤ 0 ≤ a + 5, also −5 ≤ a ≤ 0. Für a gibt es −5, −4, −3, −2, −1, 0: sechs Intervalle.', 'Lass das Intervall wie ein Fenster über den Zahlenstrahl gleiten.'))

# --- enthalten ---
ST.leiter('enthalten', 'prüfen, ob eine Zahl im Intervall liegt, Länge eines Intervalls',
          'ganze Zahlen im Intervall zählen, Sachlänge, aus der Anzahl eine Grenze bestimmen',
          'Schnitt und Vereinigung, Parameter, Zählfehler deuten, Teilmenge begründen, Brüche zählen, Prüfungsaufgabe mit zwei Mengen')
T('enthalten', (r'^Welche Zahl liegt|^Markiere', 'erkennen'), (r'^Wie viele ganze Zahlen', 'mehrschritt'), (r'Wie lang ist es', 'mehrschritt'),
  (r'gleichzeitig|oder in', 'verknuepfen'), (r'\]a; 7\]', 'parameter'), (r'Brüche', 'transfer'))
ST.neu('enthalten', 'direkt', SZ('Wie lang ist das Intervall [−2; 5]?', 7, '5 - (-2)', 'Länge = rechte Grenze − linke Grenze = 5 − (−2) = 7.', 'Rechne rechte minus linke Grenze.'))
ST.neu('enthalten', 'einkleidung', SZ('Ein Parkhaus lässt Autos von 1,50 m bis 2,10 m Höhe hinein. Wie viele Zentimeter umfasst dieser Bereich?', 60, '210 - 150',
    'Das Intervall ist [1,5; 2,1] (in m), seine Länge 0,6 m = 60 cm.', 'Rechne in Zentimetern: 210 − 150.', einheit='cm'))
ST.neu('enthalten', 'umkehr', SZ('Das Intervall [−3; b] enthält genau 8 ganze Zahlen; b ist ganz. Bestimme b.', 4, '-3 + 8 - 1',
    'Die ganzen Zahlen sind −3, −2, …, b. Das sind b − (−3) + 1 = b + 4 Zahlen. b + 4 = 8 ⇒ b = 4.', 'Zähle von −3 an acht ganze Zahlen ab.'))
ST.neu('enthalten', 'fehler', SA('Jemand zählt die ganzen Zahlen in ]−2; 3[ so: −2, −1, 0, 1, 2, 3 – also 6. Was stimmt?', 'Falsch: −2 und 3 gehören nicht dazu, es sind 4.',
    ['Richtig, es sind 6.', 'Falsch: Es sind 5, nur die 3 fehlt.', 'Falsch: Es sind 3.'],
    'Beide Klammern zeigen nach außen: −2 und 3 gehören nicht dazu. Übrig bleiben −1, 0, 1, 2.', 'Schau dir beide Klammern an.'))
ST.neu('enthalten', 'begruenden', SA('Stimmt die Aussage: „Liegt eine Zahl in [1; 4], dann liegt sie auch in ]0; 5[“?', 'Ja: [1; 4] liegt ganz innerhalb von ]0; 5[.',
    ['Nein: 1 und 4 gehören nicht zu ]0; 5[.', 'Nein: ]0; 5[ ist kürzer.', 'Nur für ganze Zahlen.'],
    'Jede Zahl x mit 1 ≤ x ≤ 4 erfüllt auch 0 < x < 5, denn 0 < 1 und 4 < 5. Auch 1 und 4 selbst liegen also in ]0; 5[.', 'Vergleiche die Grenzen beider Intervalle.'))
ST.neu('enthalten', 'pruefung', SZ('Gegeben sind A = [−6; 2[ und B = ]−1; 5]. Wie viele ganze Zahlen liegen in A und zugleich in B?', 2, '1 - 0 + 1',
    'Gemeinsam ist ]−1; 2[. Ganze Zahlen darin: 0 und 1. Das sind zwei.', 'Bestimme zuerst den gemeinsamen Teil der beiden Intervalle.'))
ST.knobel('enthalten', SZ('Wie viele Zahlen mit höchstens zwei Nachkommastellen liegen im Intervall ]0; 1[?', 99, '99 - 1 + 1',
    'Jede solche Zahl lässt sich als Hundertstel schreiben: 0,01; 0,02; …; 0,99 (0,1 ist 0,10 usw.). Das sind 99 Zahlen; 0 und 1 gehören nicht dazu.',
    'Schreibe jede Zahl mit genau zwei Nachkommastellen.'))
ST.knobel('enthalten', SZ('Ein Intervall hat die Länge 2,5 und enthält seine Grenzen. Wie viele ganze Zahlen enthält es mindestens?', 2, '2',
    'Egal wo das Intervall liegt: Von der linken Grenze aus kommt nach höchstens 1 die erste ganze Zahl, nach einer weiteren Einheit die zweite – zusammen höchstens 2 ≤ 2,5. Also immer mindestens 2. Beispiel mit genau 2: [0,1; 2,6] enthält 1 und 2.',
    'Wie weit muss man von einer beliebigen Stelle höchstens gehen, bis zwei ganze Zahlen kommen?'))

# --- beurteilen ---
ST.leiter('beurteilen', 'eine richtige Aussage über ein Intervall erkennen',
          'die falsche Aussage finden, Sachgrenzen und Zahlenstrahl-Bilder beurteilen, Mitte bestimmen und prüfen',
          'allgemeine Aussagen begründen, Sonderfall [a; a], Fehler deuten, Parameter, Brüche, Schnittmenge wie in einer Prüfung')
T('beurteilen', (r'^Tim|^Lisa|JEDES', 'begruenden'), (r'ist richtig\?$', 'erkennen'), (r'FALSCH\?$', 'umkehr'), (r'^Stimmt die Aussage', 'direkt'), (r'\[5; 5\]', 'transfer'))
ST.neu('beurteilen', 'einkleidung', SA('Ein Schwimmkurs ist für Kinder von 6 bis unter 10 Jahren. Welche Aussage stimmt?', 'Ein Kind mit 6 Jahren darf mit, eines mit 10 nicht.',
    ['Beide dürfen mit.', 'Keines der beiden darf mit.', 'Ein Kind mit 10 darf mit, eines mit 6 nicht.'], 'Das Alter liegt in [6; 10[: 6 gehört dazu, 10 nicht.', 'Schreibe die Altersgrenze als Intervall.'))
ST.neu('beurteilen', 'darstellung', SA('Am Zahlenstrahl ist bei 1 ein leerer Kreis, bei 4 ein ausgefüllter Punkt, dazwischen ist die Strecke dick. Welche Aussage stimmt?', 'Das ist ]1; 4]: 4 gehört dazu, 1 nicht.',
    ['Das ist [1; 4[.', 'Das ist [1; 4].', 'Das ist ]1; 4[.'], 'Leerer Kreis: Grenze gehört nicht dazu. Ausgefüllter Punkt: Grenze gehört dazu.', 'Was bedeuten leerer Kreis und ausgefüllter Punkt?'))
ST.neu('beurteilen', 'mehrschritt', SA('Liegt die Mitte des Intervalls [−3; 7] im Intervall ]0; 2]?', 'Ja, die Mitte ist 2 und 2 gehört dazu.', ['Nein, die Mitte ist 5.', 'Nein, die Mitte ist 2, aber 2 gehört nicht dazu.', 'Ja, die Mitte ist 1.'],
    'Mitte: (−3 + 7) : 2 = 2. In ]0; 2] gehört die 2 dazu.', 'Erst die Mitte berechnen, dann die Klammer bei 2 ansehen.'))
ST.neu('beurteilen', 'fehler', SA('Jemand sagt: „−2,5 liegt in [−2; 3], weil −2,5 größer als −2 ist.“ Was ist falsch?', '−2,5 ist kleiner als −2, liegt also links davon und nicht im Intervall.',
    ['Nichts, die Aussage stimmt.', '−2,5 liegt nicht darin, weil es keine ganze Zahl ist.', 'Die Grenze −2 gehört nicht dazu.'],
    'Bei negativen Zahlen ist die mit dem größeren Betrag die kleinere: −2,5 < −2. Damit liegt −2,5 außerhalb.', 'Wo liegt −2,5 am Zahlenstrahl – links oder rechts von −2?'))
ST.neu('beurteilen', 'parameter', SA('Für welche Zahlen a ist die Aussage „3 liegt in ]a; 5]“ wahr?', 'für alle a < 3', ['für alle a ≤ 3', 'für alle a > 3', 'nur für a = 3'],
    '3 liegt in ]a; 5], wenn a < 3 ≤ 5. Für a = 3 gehört die 3 wegen der offenen Klammer nicht dazu.', 'Probiere a = 3 und a = 2,9.'))
ST.neu('beurteilen', 'verknuepfen', SA('Welche Aussage über das Intervall ]−1/2; 1/3[ ist richtig?', '0,3 liegt darin.', ['−0,6 liegt darin.', '0,4 liegt darin.', '−1/2 liegt darin.'],
    '−1/2 = −0,5 und 1/3 ≈ 0,333. 0,3 liegt dazwischen. −0,6 ist zu klein, 0,4 zu groß, −1/2 ist die ausgeschlossene Grenze.', 'Wandle die Grenzen in Dezimalzahlen um.'))
ST.neu('beurteilen', 'pruefung', SA('Gegeben sind A = [0; 4] und B = ]2; 6[. Welche Aussage ist richtig?', 'Die gemeinsamen Zahlen bilden ]2; 4].', ['Die gemeinsamen Zahlen bilden [2; 4].', 'Die 2 liegt in beiden.', 'Die 6 liegt in B.'],
    'Gemeinsam: größer als 2 (wegen B) und höchstens 4 (wegen A): ]2; 4]. Die 2 gehört nicht zu B, die 6 auch nicht.', 'Zeichne beide Intervalle untereinander.'))
ST.knobel('beurteilen', SA('A = [0; 3], B = [2; 5] und C = [4; 7]. Welche Aussage stimmt?', 'Keine Zahl liegt in allen drei, aber jede Zahl aus [0; 7] liegt in mindestens einem.',
    ['Die 3 liegt in allen drei.', 'Es gibt eine Zahl in [0; 7], die in keinem liegt.', 'Die Zahlen, die in genau zwei Intervallen liegen, bilden [2; 5].'],
    'A und C haben keine gemeinsame Zahl (3 < 4), also liegt keine Zahl in allen drei. A und B überlappen von 2 bis 3, B und C von 4 bis 5 – dadurch gibt es keine Lücke von 0 bis 7. In genau zwei Intervallen liegen nur [2; 3] und [4; 5], nicht ganz [2; 5].',
    'Zeichne die drei Intervalle übereinander und such Lücken und Überlappungen.'))
ST.knobel('beurteilen', SZ('In wie vielen der Intervalle [1; 2], [1; 3], [1; 4], …, [1; 100] liegt die Zahl 37,5?', 63, '100 - 38 + 1',
    '37,5 liegt in [1; n], wenn n ≥ 37,5 ist, also für n = 38, 39, …, 100. Das sind 100 − 38 + 1 = 63 Intervalle.', 'Für welche rechten Grenzen n ist 37,5 dabei?'))
baue = mit_stufen(baue, ST)
# ---- STUFEN ENDE ----

# ---------- TEXT: Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers) – mehr Textaufgaben, siehe _text_kl8.py ----------
from _text_kl8 import Text, mit_text, text_auf_datei  # noqa: E402
TX = Text('zahlen.intervalle', 22_8_2)
TZ, TA, TL, TW = TX.Z, TX.A, TX.L, TX.W

_JN = ['Ja', 'Nein']

# --- lesen ---
TX.u('lesen', 'direkt', TX.A('Am Freibad steht: „Wassertemperatur [22; 26] °C“. Was bedeutet das?', 'von 22 °C bis 26 °C, beide Grenzen gehören dazu',
    ['über 22 °C und unter 26 °C', 'nur 22 °C oder 26 °C', 'von 22 °C bis unter 26 °C'],
    TW('[22; 26].', 'Bedeutung.', 'Eckige Klammer nach innen: Grenze gehört dazu.', 'Beide Klammern zeigen nach innen.', 'Gemeint sind 22 °C bis 26 °C, beide eingeschlossen.'), 'Zeigen die Klammern zur Zahl hin oder von ihr weg?'))
TX.u('lesen', 'pruefung', TX.A('Im Kletterpark gilt: Parcours A für Kinder ab 1,10 m und kleiner als 1,40 m, Parcours B ab 1,30 m. Ein Kind ist 1,35 m groß. Welche Parcours darf es benutzen?',
    'A und B', ['nur A', 'nur B', 'keinen'],
    TW('A: [1,10; 1,40[ m, B: [1,30; ∞[ m, Kind 1,35 m.', 'erlaubte Parcours.', 'Für jeden Parcours prüfen, ob 1,35 im Intervall liegt.', '1,10 ≤ 1,35 < 1,40 ✓; 1,35 ≥ 1,30 ✓.', 'Das Kind darf A und B benutzen.'),
    'Prüfe jede Bedingung einzeln.'), huerde='zwei')
TX.u('lesen', 'begruenden', TX.A('Ein Paketdienst: Päckchen bis einschließlich 2 kg kosten 4 €, Pakete im Bereich ]2; 5] kg kosten 6 €. Ein Paket wiegt genau 2 kg. Jemand sagt: „Das kostet 6 €.“ Was stimmt?',
    'Falsch: 2 kg gehört nicht zu ]2; 5], es kostet 4 €.', ['Richtig: 2 liegt in ]2; 5].', 'Richtig: Ab 2 kg kostet es 6 €.', 'Falsch: Es kostet 10 €.'],
    TW('Päckchen bis einschließlich 2 kg; Pakete ]2; 5] kg.', 'Preis für genau 2 kg.', 'Die Klammer bei 2 zeigt nach außen: 2 gehört nicht dazu.', '2 kg fällt unter „bis einschließlich 2 kg“.', 'Die Aussage ist falsch; das Paket kostet 4 €.'),
    'Gehört die 2 zum Intervall ]2; 5]?'), huerde='entscheidung')
TX.s('lesen', TX.A('Ein Thermostat hält die Raumtemperatur im Intervall [19; 21] °C. Welche Temperatur liegt NICHT darin?', '21,5 °C', ['19 °C', '20,5 °C', '21 °C'],
    TW('[19; 21].', 'Temperatur außerhalb.', 'Beide Grenzen gehören dazu.', '21,5 > 21.', '21,5 °C liegt nicht darin.')))
TX.s('lesen', TX.A('Der Jugendtarif gilt für das Alter [14; 18[. Darf eine 18-Jährige den Jugendtarif nutzen?', 'Nein', ['Ja', 'Nur am Geburtstag'],
    TW('[14; 18[.', 'Gehört 18 dazu?', 'Die Klammer bei 18 zeigt nach außen.', '18 gehört nicht dazu.', 'Nein, mit 18 gilt der Jugendtarif nicht mehr.')))
TX.k('lesen', TX.A('Nach dem Umschalten ist eine Ampel im Zeitraum [0; 25[ Sekunden grün. Ist sie nach genau 25 Sekunden noch grün?', 'Nein', ['Ja', 'Das kann man nicht sagen'],
    TW('[0; 25[.', 'Ist 25 dabei?', 'Klammer bei 25 nach außen.', '25 gehört nicht dazu.', 'Nein, nach genau 25 Sekunden ist sie nicht mehr grün.')))

# --- schreiben ---
TX.u('schreiben', 'direkt', TX.A('In einem Kühlschrank soll es über 0 °C und höchstens 7 °C kalt sein. Schreibe diese Temperaturen als Intervall.', ']0; 7]', ['[0; 7]', ']0; 7[', '[0; 7['],
    TW('über 0, höchstens 7.', 'Intervall.', '„über“: Klammer nach außen; „höchstens“: Klammer nach innen.', ']0; 7].', 'Das Intervall ist ]0; 7].'), 'Gehört 0 °C dazu, gehört 7 °C dazu?'))
TX.u('schreiben', 'einkleidung', TX.A('Ein Handgepäckstück darf höchstens 8 kg wiegen. Schreibe alle erlaubten Gewichte (mehr als 0 kg) als Intervall.', ']0; 8]', ['[0; 8[', ']0; 8[', '[8; ∞['],
    TW('mehr als 0 kg, höchstens 8 kg.', 'Intervall.', '„mehr als“ nach außen, „höchstens“ nach innen.', ']0; 8].', 'Erlaubt ist ]0; 8] kg.'), 'Darf das Gepäck genau 8 kg wiegen?'))
TX.u('schreiben', 'darstellung', TX.A('Im Fahrplan steht: Der Bus fährt ab 6 Uhr bis vor 9 Uhr alle 10 Minuten. Schreibe diese Zeitspanne (in Stunden) als Intervall.', '[6; 9[', ['[6; 9]', ']6; 9[', ']6; 9]'],
    TW('ab 6 Uhr, bis vor 9 Uhr.', 'Intervall.', '„ab“ nach innen, „bis vor“ nach außen.', '[6; 9[.', 'Die Zeitspanne ist [6; 9[.'), 'Fährt um genau 9 Uhr noch ein Bus im 10-Minuten-Takt?'))
TX.u('schreiben', 'pruefung', TX.A('Medikament A darf bei 15 °C bis 25 °C gelagert werden, Medikament B bei mehr als 20 °C bis 30 °C. In welchem Temperaturbereich kann man beide zusammen lagern?',
    ']20; 25]', ['[15; 30]', '[20; 25]', ']20; 25['],
    TW('A: [15; 25], B: ]20; 30].', 'Bereich für beide.', 'Nur Zahlen, die in beiden Intervallen liegen.', 'Unten: über 20 (wegen B). Oben: höchstens 25 (wegen A).', 'Beide zusammen gehen bei ]20; 25] °C.'),
    'Welche Temperaturen erfüllen beide Bedingungen?'), huerde='zwei')
TX.u('schreiben', 'begruenden', TX.A('Auf einer Straße gilt: mindestens 60 km/h, höchstens 120 km/h. Jemand schreibt die erlaubten Geschwindigkeiten als ]60; 120[. Was stimmt?',
    'Falsch: Richtig ist [60; 120], die Grenzen gehören dazu.', ['Richtig.', 'Falsch: Richtig ist [60; 120[.', 'Falsch: Richtig ist ]60; 120].'],
    TW('„mindestens 60“, „höchstens 120“.', 'Ist ]60; 120[ richtig?', '„mindestens“ und „höchstens“ schließen die Grenze ein.', 'Beide Klammern müssen nach innen zeigen.', 'Falsch; richtig ist [60; 120].'),
    'Darf man genau 60 km/h fahren?'), huerde='entscheidung')
TX.s('schreiben', TX.A('Schreibe „für Kinder ab 3 Jahren bis einschließlich 12 Jahren“ als Intervall.', '[3; 12]', [']3; 12]', '[3; 12[', ']3; 12['],
    TW('ab 3, bis einschließlich 12.', 'Intervall.', 'Beide Grenzen gehören dazu.', '[3; 12].', 'Das Intervall ist [3; 12].')))
TX.s('schreiben', TX.A('Ein Ofen backt Pizza bei mehr als 250 °C. Schreibe diese Temperaturen als Intervall.', ']250; ∞[', ['[250; ∞[', ']−∞; 250[', ']250; ∞]'],
    TW('mehr als 250.', 'Intervall.', '„mehr als“: nach außen; nach oben offen.', ']250; ∞[.', 'Das Intervall ist ]250; ∞[.')))
TX.k('schreiben', TX.A('Schreibe „Fahrräder mit einer Rahmenhöhe ab 50 cm bis unter 56 cm“ als Intervall.', '[50; 56[', ['[50; 56]', ']50; 56[', ']50; 56]'],
    TW('ab 50, unter 56.', 'Intervall.', '„ab“ nach innen, „unter“ nach außen.', '[50; 56[.', 'Das Intervall ist [50; 56[.')))

# --- enthalten ---
TX.u('enthalten', 'erkennen', TX.A('Ein Aufzug trägt Lasten im Bereich ]0; 630] kg. Welche Last ist zu schwer?', '631 kg', ['630 kg', '600 kg', '450 kg'],
    TW(']0; 630] kg.', 'Last außerhalb.', '630 gehört dazu, alles darüber nicht.', '631 > 630.', '631 kg ist zu schwer.'), 'Gehört 630 dazu?'))
TX.u('enthalten', 'einkleidung', TZ('Eine Parkuhr nimmt Parkzeiten von 15 bis 120 Minuten an, beide Grenzen erlaubt, nur volle Minuten. Wie viele verschiedene Parkzeiten gibt es?', '120 - 15 + 1',
    TW('[15; 120], nur ganze Minuten.', 'Anzahl der Parkzeiten.', 'Ganze Zahlen von 15 bis 120 zählen: Ende − Anfang + 1.', '120 − 15 + 1 = 106.', 'Es gibt 106 Parkzeiten.'), 'Wie zählst du alle ganzen Zahlen von a bis b?'))
TX.u('enthalten', 'mehrschritt', TZ('Ein Thermometer im Gewächshaus zeigt nur ganze Grad. Für Tomaten ist ]12; 30[ °C gut. Wie viele angezeigte Temperaturen sind gut?', '29 - 13 + 1',
    TW(']12; 30[, ganze Grad.', 'Anzahl der guten Werte.', 'Grenzen gehören nicht dazu: von 13 bis 29 zählen.', '29 − 13 + 1 = 17.', 'Es sind 17 Temperaturen.'), 'Welche ist die kleinste und die größte ganze Zahl im Intervall?'))
TX.u('enthalten', 'pruefung', TZ('Im Kino gibt es Ermäßigung für Jugendliche unter 16 Jahren und für Rentner ab 65 Jahren; der Film ist ab 12 Jahren. Wie viele ganze Alter von 12 bis 70 bekommen eine Ermäßigung?', '(15 - 12 + 1) + (70 - 65 + 1)',
    TW('Film ab 12; ermäßigt [12; 16[ und [65; 70].', 'Anzahl der ermäßigten Alter.', 'Beide Bereiche einzeln zählen, dann addieren.', '12, 13, 14, 15 (4) und 65 bis 70 (6).', 'Es sind 10 Alter.'),
    'Zwei Bereiche – zähle sie getrennt.'), huerde='zwei')
TX.u('enthalten', 'begruenden', TX.A('Brötchen sollen 55 g bis 65 g wiegen, beide Grenzen erlaubt. Ein Brötchen wiegt 54,9 g. Darf es verkauft werden?', 'Nein, 54,9 liegt nicht in [55; 65].', ['Ja, gerundet sind es 55 g.', 'Ja, 54,9 liegt in [55; 65].', 'Nein, weil es mehr als 65 g wiegt.'],
    TW('[55; 65], 54,9 g.', 'Liegt 54,9 im Intervall?', 'Mit der linken Grenze vergleichen.', '54,9 < 55.', 'Nein, das Brötchen ist zu leicht.'), 'Ist 54,9 mindestens 55?'), huerde='entscheidung')
TX.u('enthalten', 'rueckwaerts', TZ('Ein Aufzug darf höchstens 630 kg tragen; man rechnet mit 75 kg pro Person. Die erlaubte Personenzahl sind die ganzen Zahlen im Intervall [1; b]. Wie groß ist b?', '630 // 75',
    TW('höchstens 630 kg, 75 kg pro Person.', 'größte erlaubte Personenzahl b.', '630 : 75 und abrunden.', '630 : 75 = 8,4.', 'b = 8: Es dürfen höchstens 8 Personen mitfahren.'), 'Darf die 9. Person noch mit?'), huerde='deuten')
TX.s('enthalten', TZ('Eine Karussellfahrt ist für Kinder von 4 bis einschließlich 10 Jahren. Wie viele ganze Altersjahre sind das?', '10 - 4 + 1',
    TW('[4; 10].', 'Anzahl der Alter.', 'Ende − Anfang + 1.', '10 − 4 + 1 = 7.', 'Es sind 7 Altersjahre.')))
TX.s('enthalten', TZ('Ein Bus braucht laut Plan zwischen 18 und 25 Minuten. Wie viele Minuten Spielraum sind das?', '25 - 18',
    TW('[18; 25].', 'Länge des Intervalls.', 'rechte − linke Grenze.', '25 − 18 = 7.', 'Der Spielraum ist 7 Minuten.'), einheit='min'))
TX.k('enthalten', TZ('Eine Kühlbox hält Temperaturen im Bereich ]−2; 6] °C. Wie viele ganze Temperaturen liegen darin?', '6 - (-1) + 1',
    TW(']−2; 6].', 'Anzahl ganzer Temperaturen.', '−2 gehört nicht dazu: von −1 bis 6 zählen.', '6 − (−1) + 1 = 8.', 'Es sind 8 ganze Temperaturen.')))

# --- beurteilen ---
TX.u('beurteilen', 'direkt', TX.A('Vor einer Unterführung steht: „Fahrzeughöhe ]0; 2,5] m“. Darf ein genau 2,5 m hoher Lieferwagen durchfahren?', 'Ja', ['Nein', 'Nur langsam'],
    TW(']0; 2,5].', 'Gehört 2,5 dazu?', 'Klammer bei 2,5 zeigt nach innen.', '2,5 gehört dazu.', 'Ja, er darf durchfahren.'), 'Wohin zeigt die Klammer bei 2,5?'))
TX.u('beurteilen', 'einkleidung', TX.A('Ein Spielzeug ist für Kinder von 3 bis unter 6 Jahren, also [3; 6[. Welche Aussage stimmt?', 'Ein Kind mit 3 Jahren gehört zur Zielgruppe.',
    ['Ein Kind mit 6 Jahren gehört zur Zielgruppe.', 'Nur Kinder mit genau 3, 4 oder 5 Jahren und 0 Monaten.', 'Ein Kind mit 2 Jahren und 11 Monaten gehört dazu.'],
    TW('[3; 6[.', 'richtige Aussage.', 'Grenze 3 gehört dazu, 6 nicht; dazwischen alle Werte.', '3 ✓, 6 ✗, 2,9 ✗.', 'Ein Kind mit 3 Jahren gehört dazu.'), 'Welche Grenze gehört dazu?'))
TX.u('beurteilen', 'mehrschritt', TX.A('Der Wetterbericht sagt Tagestemperaturen im Bereich ]18; 25] °C voraus. Liegt die Mitte dieses Bereichs über 21 °C?', 'Ja, die Mitte ist 21,5 °C.', ['Nein, die Mitte ist 21 °C.', 'Nein, die Mitte ist 7 °C.', 'Ja, die Mitte ist 25 °C.'],
    TW(']18; 25].', 'Mitte und Vergleich.', 'Mitte = (linke + rechte Grenze) : 2.', '(18 + 25) : 2 = 21,5.', 'Ja, die Mitte ist 21,5 °C.'), 'Wie berechnest du die Mitte zweier Zahlen?'))
TX.u('beurteilen', 'pruefung', TX.A('Ein Wanderweg ist mit einer Gehzeit von 3 bis 5 Stunden ausgeschildert. Er ist 14 km lang und hat 4 Rastplätze. Eine Gruppe braucht 5 Stunden und 15 Minuten. Liegt sie im angegebenen Bereich?',
    'Nein, 5,25 h liegt nicht in [3; 5].', ['Ja, 5 Stunden und 15 Minuten sind 5,15 h.', 'Ja, die Rastplätze zählen nicht mit.', 'Nein, weil 14 km zu lang sind.'],
    TW('[3; 5] h, Gruppe 5 h 15 min. Länge und Rastplätze spielen keine Rolle.', 'Liegt die Zeit im Bereich?', 'Minuten in Stunden umrechnen und vergleichen.', '15 min = 0,25 h; 5,25 > 5.', 'Nein, die Gruppe war langsamer.'),
    'Wie viele Stunden sind 15 Minuten?'), huerde='ueberfluessig')
TX.u('beurteilen', 'transfer', TX.A('Ein Onlineshop liefert versandkostenfrei bei einem Bestellwert im Intervall [50; ∞[ €. Jemand bestellt für 49,90 € und sagt: „Gerundet sind das 50 €, also ist der Versand gratis.“ Was stimmt?',
    'Falsch: 49,90 liegt nicht im Intervall, der Versand kostet.', ['Richtig: Man darf runden.', 'Richtig: 49,90 liegt in [50; ∞[.', 'Falsch: Erst ab 51 € ist er gratis.'],
    TW('[50; ∞[, Bestellung 49,90 €.', 'Ist der Versand gratis?', 'Exakt vergleichen, nicht runden.', '49,90 < 50.', 'Nein, die Bestellung liegt knapp darunter.'), 'Ist 49,90 mindestens 50?'), huerde='entscheidung')
TX.u('beurteilen', 'verknuepfen', TZ('Im Freizeitpark liegt die Wartezeit an einer Bahn im Intervall ]10; 20] Minuten. Sie ist eine ganze Zahl und ein Vielfaches von 7. Wie viele Minuten wartet man?', '14',
    TW(']10; 20], Vielfaches von 7.', 'Wartezeit.', 'Vielfache von 7 aufzählen und mit dem Intervall vergleichen.', '7 (zu klein), 14 ✓, 21 (zu groß).', 'Man wartet 14 Minuten.'), 'Welche Vielfachen von 7 kennst du?', einheit='min'), huerde='zwei')
TX.s('beurteilen', TX.A('Ein Hotel bietet den Check-in im Intervall [15; 22[ Uhr an. Ist ein Check-in um genau 22 Uhr möglich?', 'Nein', ['Ja', 'Nur mit Anmeldung'],
    TW('[15; 22[.', 'Gehört 22 dazu?', 'Klammer bei 22 nach außen.', '22 gehört nicht dazu.', 'Nein.')))
TX.s('beurteilen', TX.A('Eine Gartenlampe darf bei Temperaturen im Intervall [−20; 40] °C betrieben werden. Welche Aussage stimmt?', 'Bei −20 °C darf sie leuchten.', ['Bei −21 °C darf sie leuchten.', 'Bei 41 °C darf sie leuchten.', 'Bei 40 °C darf sie nicht leuchten.'],
    TW('[−20; 40].', 'richtige Aussage.', 'Beide Grenzen gehören dazu.', '−20 ✓, −21 ✗, 41 ✗, 40 ✓.', '−20 °C ist erlaubt.')))
TX.k('beurteilen', TX.A('Eine Bergbahn fährt bei Wind bis einschließlich 60 km/h. Fährt sie bei genau 60 km/h Wind?', 'Ja', ['Nein', 'Nur talwärts'],
    TW('Wind ≤ 60 km/h, also [0; 60].', 'Fährt sie bei 60?', '„bis einschließlich“ schließt 60 ein.', '60 gehört dazu.', 'Ja, sie fährt.')))
baue = mit_text(baue, TX)
# ---- TEXT ENDE ----

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
