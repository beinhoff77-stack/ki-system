#!/usr/bin/env python3
"""Thema geometrie.konstruktion – Konstruktionen, Kongruenz und Beweise (Gymnasium Bayern, Klasse 7)."""
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl7 import A, Z, baue, figur, zt  # noqa: E402

META = {'thema_schluessel': 'geometrie.konstruktion', 'thema_id': 44, 'block_id': 80, 'klasse': {'gym_by': 7, 'rs_by': 6}}


def dreieck(al, be, c=6.0):
    """Punkte A, B, C eines Dreiecks mit den Winkeln α (bei A) und β (bei B), Seite c = AB (nur fürs Bild, gerundet)."""
    ga = 180 - al - be
    b = c * math.sin(math.radians(be)) / math.sin(math.radians(ga))
    C = (round(b * math.cos(math.radians(al)), 2), round(b * math.sin(math.radians(al)), 2))
    return {'A': [0, 0], 'B': [c, 0], 'C': list(C)}


def dreieck_bild(al, be, wtexte=('α', 'β', 'γ'), seiten=None):
    p = dreieck(al, be)
    lin = [['A', 'B', (seiten or {}).get('c', '')], ['B', 'C', (seiten or {}).get('a', '')], ['C', 'A', (seiten or {}).get('b', '')]]
    lin = [[u, v, t] if t else [u, v] for u, v, t in lin]
    w = [['A', 'B', 'C', wtexte[0]], ['B', 'C', 'A', wtexte[1]], ['C', 'A', 'B', wtexte[2]]]
    w = [x for x in w if x[3]]
    return figur(p, linien=lin, flaeche=['A', 'B', 'C'], winkel=w)


ETAPPEN = [
    {'lernziel': 'parallelen', 'titel': 'Winkel an Parallelen',
     'regel': 'Wird ein Paar ⟦paralleler⟧ Geraden von einer dritten Geraden geschnitten, sind ⟦Stufenwinkel⟧ gleich groß (wie verschoben: gleiche Lage an beiden Kreuzungen) und ⟦Wechselwinkel⟧ gleich groß (Z-Form: auf verschiedenen Seiten). Das gilt ⟦nur⟧, wenn die Geraden parallel sind.',
     'schritte': ['g und h sind parallel. Bei S ist α = 55°.', 'β liegt bei T in derselben Lage wie α bei S (rechts oberhalb): Stufenwinkel, also ⟦β = 55°⟧.', 'γ liegt bei T links unterhalb, α bei S rechts oberhalb – Z-Form: Wechselwinkel, also ⟦γ = 55°⟧.'],
     'fehler': 'Auch bei nicht parallelen Geraden gleiche Stufenwinkel annehmen. Sind g und h nicht parallel, ist β im Allgemeinen ⟦anders⟧ als α. Umgekehrt gilt: Sind Stufenwinkel gleich, dann sind die Geraden parallel.',
     'bild': {'typ': 'figur', 'punkte': {'_g1': [-1, 0], '_g2': [8, 0], '_h1': [-1, 3], '_h2': [8, 3], 'S': [2, 0], 'T': [4.1, 3], '_t1': [0.6, -2], '_t2': [5.5, 5]}, 'linien': [['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['_t1', '_t2']], 'winkel': [['S', '_g2', 'T', 'α = 55°'], ['T', '_h2', '_t2', 'β'], ['T', '_h1', 'S', 'γ']]},
     '_verbot': ['α = 55°']},
    {'lernziel': 'winkelsumme', 'titel': 'Winkel im Dreieck berechnen',
     'regel': 'In jedem Dreieck ist die ⟦Winkelsumme 180°⟧: α + β + γ = 180°. Warum? Zeichne durch C die Parallele zu [AB]. Links von C taucht α noch einmal auf, rechts β (⟦Wechselwinkel⟧). Zusammen mit γ bilden sie einen ⟦gestreckten Winkel⟧, also 180°.',
     'schritte': ['α = 50°, β = 75°', 'γ = 180° − 50° − 75°', '⟦γ = 55°⟧'],
     'fehler': 'γ = 360° − 50° − 75° ist falsch: 360° ist die Winkelsumme im ⟦Viereck⟧. Im Dreieck sind es 180°.',
     'bild': {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [6, 0], 'C': [4.55, 5.42], '_l': [1, 5.42], '_r': [8, 5.42]}, 'flaeche': ['A', 'B', 'C'], 'linien': [['A', 'B'], ['B', 'C'], ['C', 'A'], ['_l', '_r', 'Parallele zu [AB]', 'gestrichelt']], 'winkel': [['A', 'B', 'C', 'α'], ['B', 'C', 'A', 'β'], ['C', '_l', 'A', 'α'], ['C', 'B', '_r', 'β'], ['C', 'A', 'B', 'γ']]},
     '_verbot': ['α = 50°, β = 75°']},
    {'lernziel': 'gleichschenklig', 'titel': 'Gleichschenklige Dreiecke',
     'regel': 'Im ⟦gleichschenkligen Dreieck⟧ sind die beiden ⟦Basiswinkel⟧ gleich groß. Im ⟦gleichseitigen⟧ Dreieck sind alle Winkel 60°.',
     'schritte': ['Spitzenwinkel γ = 40°', 'Basiswinkel zusammen: 180° − 40° = 140°', 'Je Basiswinkel: 140° : 2 = ⟦70°⟧'],
     'fehler': 'Bei γ = 40° sind die Basiswinkel nicht je 40°: Nur die ⟦beiden Basiswinkel⟧ sind gleich, der Spitzenwinkel ist anders.',
     'bild': figur({'A': [0, 0], 'B': [4, 0], 'C': [2, 5.49]}, linien=[['A', 'B', 'Basis'], ['B', 'C', 'Schenkel'], ['C', 'A', 'Schenkel']], flaeche=['A', 'B', 'C'],
                   winkel=[['A', 'B', 'C', '70°'], ['B', 'C', 'A', '70°'], ['C', 'A', 'B', '40°']]),
     '_verbot': ['γ = 40°']},
    {'lernziel': 'kongruenzsatz', 'titel': 'Welcher Kongruenzsatz passt?',
     'regel': 'Dreiecke sind ⟦kongruent⟧ (deckungsgleich), wenn sie übereinstimmen in: ⟦SSS⟧ (drei Seiten), ⟦SWS⟧ (zwei Seiten und eingeschlossener Winkel), ⟦WSW⟧ (eine Seite, zwei Winkel) oder ⟦SsW⟧ (zwei Seiten und der Winkel gegenüber der ⟦größeren⟧ Seite).',
     'schritte': ['Gegeben: b = 5 cm, c = 7 cm, α = 40°', 'α liegt zwischen b und c (bei A).', 'Kongruenzsatz ⟦SWS⟧ – das Dreieck ist eindeutig.'],
     'fehler': 'Drei gleiche Winkel (WWW) reichen nicht: Die Dreiecke haben dann zwar dieselbe Form, können aber ⟦verschieden groß⟧ sein.',
     '_verbot': ['b = 5 cm, c = 7 cm, α = 40°']},
    {'lernziel': 'konstruierbar', 'titel': 'Ist das Dreieck konstruierbar?',
     'regel': 'Ein Dreieck aus drei Seiten gibt es nur, wenn ⟦je zwei Seiten zusammen länger⟧ sind als die dritte (Dreiecksungleichung). Zwei gegebene Winkel müssen zusammen ⟦weniger als 180°⟧ ergeben.',
     'schritte': ['a = 3 cm, b = 4 cm, c = 8 cm', '3 cm + 4 cm = 7 cm < 8 cm', 'Die Kreisbögen treffen sich nicht: ⟦nicht konstruierbar⟧.'],
     'fehler': 'Bei a = 3 cm, b = 5 cm, c = 8 cm entsteht kein Dreieck: 3 + 5 = 8 ist ⟦nicht größer⟧ als 8. Die Punkte lägen alle auf einer Linie.',
     '_verbot': ['a = 3 cm, b = 4 cm, c = 8 cm']},
    {'lernziel': 'vierecke', 'titel': 'Winkel in symmetrischen Vierecken',
     'regel': 'Winkelsumme im Viereck: ⟦360°⟧. ⟦Parallelogramm⟧: gegenüberliegende Winkel gleich, benachbarte zusammen 180°. ⟦Drachenviereck⟧: die beiden Winkel neben der Symmetrieachse sind gleich. ⟦Gleichschenkliges Trapez⟧: die Winkel an einer Grundseite sind gleich.',
     'schritte': ['Parallelogramm ABCD mit α = 65°', 'γ = α = 65°; β = 180° − 65° = ⟦115°⟧', 'δ = β = 115°. Probe: 65 + 115 + 65 + 115 = 360 ✓'],
     'fehler': 'Im Parallelogramm ist β nicht ebenfalls 65°: ⟦Benachbarte⟧ Winkel ergänzen sich zu 180°, nur ⟦gegenüberliegende⟧ sind gleich.',
     'bild': figur({'A': [0, 0], 'B': [5, 0], 'C': [6.27, 2.72], 'D': [1.27, 2.72]}, linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']], flaeche=['A', 'B', 'C', 'D'],
                   winkel=[['A', 'B', 'D', '65°'], ['B', 'C', 'A', 'β']]),
     '_verbot': ['α = 65°']},
    {'lernziel': 'satz_kehrsatz', 'titel': 'Satz und Kehrsatz',
     'regel': 'Ein Satz hat die Form ⟦„Wenn A, dann B.“⟧ Beim ⟦Kehrsatz⟧ werden Voraussetzung und Behauptung vertauscht: „Wenn B, dann A.“ Ein Kehrsatz ist ⟦nicht automatisch wahr⟧ – ein Gegenbeispiel genügt, um ihn zu widerlegen.',
     'schritte': ['Satz: Wenn ein Viereck ein Quadrat ist, dann hat es vier rechte Winkel. (wahr)', 'Kehrsatz: Wenn ein Viereck vier rechte Winkel hat, dann ist es ein Quadrat.', 'Gegenbeispiel: Rechteck 2 cm × 5 cm. Der Kehrsatz ist ⟦falsch⟧.'],
     'fehler': 'Aus „der Satz ist wahr“ folgt nicht „der Kehrsatz ist wahr“. Jeder Kehrsatz muss ⟦eigens geprüft⟧ werden.'},
]


ZYK = {}


def zyklus(name, liste):
    ZYK[name] = ZYK.get(name, -1) + 1
    return liste[ZYK[name] % len(liste)]


LAGE = {'ro': 'rechts oberhalb', 'lo': 'links oberhalb', 'lu': 'links unterhalb', 'ru': 'rechts unterhalb'}


def par_bild(al, marken, parallel=True, be=None):
    """Zwei Geraden g (unten) und h (oben), geschnitten von einer Geraden durch S und T. marken: [(Punkt 'S'/'T', Lage, Text)]."""
    c, sn = math.cos(math.radians(al)), math.sin(math.radians(al))
    tx = round(2 + 3 * c / sn, 2)
    pk = {'S': [2, 0], 'T': [tx, 3], '_t1': [round(2 - 2 * c / sn, 2), -2], '_t2': [round(tx + 2 * c / sn, 2), 5],
          '_g1': [-2, 0], '_g2': [round(max(tx, 2) + 4, 2), 0]}
    if parallel or be is None:
        pk['_h1'] = [-2, 3]; pk['_h2'] = [round(max(tx, 2) + 4, 2), 3]
    else:  # h nicht parallel: um T gedreht, sodass β (rechts oberhalb) = be
        d = be - al
        k = math.tan(math.radians(d))
        pk['_h1'] = [round(tx - 4, 2), round(3 - 4 * k, 2)]; pk['_h2'] = [round(tx + 4, 2), round(3 + 4 * k, 2)]
    unten = {'S': '_t1', 'T': 'S'}; oben = {'S': 'T', 'T': '_t2'}; links = {'S': '_g1', 'T': '_h1'}; rechts = {'S': '_g2', 'T': '_h2'}
    w = []
    for P, lage, txt in marken:
        a, b = {'ro': (rechts[P], oben[P]), 'lo': (oben[P], links[P]), 'lu': (links[P], unten[P]), 'ru': (unten[P], rechts[P])}[lage]
        w.append([P, a, b, txt])
    return figur(pk, linien=[['_g1', '_g2', 'g'], ['_h1', '_h2', 'h'], ['_t1', '_t2']], winkel=w)


def wert_lage(al, lage):
    return al if lage in ('ro', 'lu') else 180 - al


ART = {('ro', 'ro'): 'Stufenwinkel', ('lo', 'lo'): 'Stufenwinkel', ('lu', 'lu'): 'Stufenwinkel', ('ru', 'ru'): 'Stufenwinkel',
       ('ro', 'lu'): 'Wechselwinkel', ('lu', 'ro'): 'Wechselwinkel', ('lo', 'ru'): 'Wechselwinkel', ('ru', 'lo'): 'Wechselwinkel'}


def g_parallelen(R, st):
    al = R.choice(range(35, 146, 5))
    if al == 90: al = 70
    if st == 1:
        lage_s = 'ro'
        lage_t = zyklus('par1', ['ro', 'lu', 'ro', 'lu'])
        art = ART[(lage_s, lage_t)]
        a = Z(f'g ∥ h. Bei S ist α = {al}° (rechts oberhalb). Wie groß ist β bei T ({LAGE[lage_t]})?', al, f'{al}',
              f'β und α sind {art} an Parallelen, also gleich groß: β = {al}°.', 'Stufenwinkel: gleiche Lage. Wechselwinkel: Z-Form. Beide sind an Parallelen gleich groß.', '°')
        a['f']['grafik'] = par_bild(al, [('S', 'ro', f'{al}°'), ('T', lage_t, 'β')])
        return a
    if st == 2:
        art = zyklus('par2', ['wert', 'name', 'wert', 'parallel?'])
        if art == 'wert':
            lage_s, lage_t = R.choice(list(LAGE)), R.choice(list(LAGE))
            x = wert_lage(al, lage_t) if lage_s == 'ro' else None
            a_s = wert_lage(al, lage_s)
            x = wert_lage(al, lage_t)
            w = f'An S liegt rechts oberhalb {al}°, die Nebenwinkel sind {180 - al}°, der Scheitelwinkel ist {al}°. Bei T sind die Winkel in gleicher Lage gleich (Stufenwinkel): β = {x}°.'
            a = Z(f'g ∥ h. Bei S ist der markierte Winkel {a_s}° ({LAGE[lage_s]}). Wie groß ist β bei T ({LAGE[lage_t]})?', x, f'{x}',
                  w, 'Bestimme erst alle vier Winkel bei S (Nebenwinkel: 180° minus, Scheitelwinkel: gleich). Bei T ist es genauso.', '°')
            a['f']['grafik'] = par_bild(al, [('S', lage_s, f'{a_s}°'), ('T', lage_t, 'β')])
            return a
        if art == 'name':
            paar = R.choice(list(ART) + [('ro', 'lo'), ('ro', 'ru'), ('lu', 'lo')])
            r = ART.get(paar, 'keins von beiden')
            a = A(R, f'g ∥ h. Welche Winkel-Beziehung haben der Winkel bei S ({LAGE[paar[0]]}) und der Winkel bei T ({LAGE[paar[1]]})?', r,
                  [x for x in ['Stufenwinkel', 'Wechselwinkel', 'Scheitelwinkel', 'keins von beiden'] if x != r],
                  f'{LAGE[paar[0]]} bei S und {LAGE[paar[1]]} bei T: ' + ('gleiche Lage → Stufenwinkel.' if r == 'Stufenwinkel' else 'Z-Form (gegenüberliegende Seiten) → Wechselwinkel.' if r == 'Wechselwinkel'
                                                                     else 'weder gleiche Lage noch Z-Form; diese Winkel ergänzen sich zu 180°.') + ' Scheitelwinkel liegen am selben Schnittpunkt.',
                  'Stufenwinkel: gleiche Lage an beiden Kreuzungen. Wechselwinkel: Z-Form.')
            a['f']['grafik'] = par_bild(al, [('S', paar[0], '1'), ('T', paar[1], '2')])
            return a
        be = al + R.choice([0, 0, 5, -5, 10, -10])
        par = be == al
        r = 'Ja, die Stufenwinkel sind gleich groß.' if par else 'Nein, die Stufenwinkel sind verschieden groß.'
        a = A(R, f'Eine Gerade schneidet g in S unter {al}° und h in T unter {be}° (beide Winkel rechts oberhalb). Sind g und h parallel?', r,
              ['Nein, die Stufenwinkel sind verschieden groß.' if par else 'Ja, die Stufenwinkel sind gleich groß.', 'Ja, zwei Geraden sind immer parallel.',
               'Das kann man ohne Länge nicht entscheiden.'],
              f'Stufenwinkel {al}° und {be}°: ' + ('gleich → g ∥ h (Kehrsatz).' if par else 'verschieden → g und h sind nicht parallel.'),
              'Sind Stufenwinkel gleich, sind die Geraden parallel – und umgekehrt.')
        a['f']['grafik'] = par_bild(al, [('S', 'ro', f'{al}°'), ('T', 'ro', f'{be}°')], parallel=par, be=be)
        return a
    art = zyklus('par3', ['gleichung', 'fehler', 'gleichung', 'fehler'])
    if art == 'gleichung':
        k, d = R.choice([2, 3, 4]), R.choice(range(5, 31, 5))
        x = R.choice([v for v in range(10, 50, 5) if 20 < k * v + d < 160])
        w = k * x + d
        neben = R.random() < .5
        if neben:
            return Z(f'g ∥ h. Bei S ist ein Winkel ({k}x + {d})° groß (rechts oberhalb), bei T der Winkel links oberhalb {180 - w}°. Berechne x.', x, f'(180 - {180 - w} - {d}) / {k}',
                     f'Links oberhalb bei T ist Nebenwinkel des Stufenwinkels: ({k}x + {d})° + {180 - w}° = 180° → {k}x = {w - d}° → x = {x}.',
                     'Der Winkel links oberhalb bei T ergänzt den Stufenwinkel zu 180°.')
        return Z(f'g ∥ h. Zwei Wechselwinkel sind ({k}x + {d})° und {w}° groß. Berechne x.', x, f'({w} - {d}) / {k}',
                 f'Wechselwinkel sind gleich: {k}x + {d} = {w} → {k}x = {w - d} → x = {x}.', 'Wechselwinkel an Parallelen sind gleich groß. Stelle eine Gleichung auf.')
    fall = R.choice([
        ('Stufenwinkel sind immer gleich groß.', 'Falsch: Nur wenn die beiden Geraden parallel sind.'),
        ('Wechselwinkel ergänzen sich an Parallelen zu 180°.', 'Falsch: Wechselwinkel an Parallelen sind gleich groß.'),
        ('Sind zwei Stufenwinkel gleich groß, dann sind die Geraden parallel.', 'Richtig: Das ist der Kehrsatz, und er gilt.'),
        ('Nebenwinkel sind immer gleich groß.', 'Falsch: Nebenwinkel ergänzen sich zu 180°.'),
        ('Scheitelwinkel sind gleich groß, auch wenn keine Parallelen da sind.', 'Richtig: Scheitelwinkel liegen an derselben Kreuzung.')])
    alle = ['Falsch: Nur wenn die beiden Geraden parallel sind.', 'Falsch: Wechselwinkel an Parallelen sind gleich groß.', 'Richtig: Das ist der Kehrsatz, und er gilt.',
            'Falsch: Nebenwinkel ergänzen sich zu 180°.', 'Richtig: Scheitelwinkel liegen an derselben Kreuzung.', 'Richtig: Das gilt für alle Winkel an Geraden.']
    return A(R, f'Jemand sagt: „{fall[0]}“ Was stimmt?', fall[1], R.sample([x for x in alle if x != fall[1]], 3), fall[1],
             'Denke an das Bild mit zwei Geraden und einer Geraden, die beide schneidet.')


def g_winkelsumme(R, st):
    while True:
        al, be = R.randint(20, 120), R.randint(20, 120)
        if al + be < 160: break
    ga = 180 - al - be
    if st == 1:
        a = Z(f'In einem Dreieck ist α = {al}° und β = {be}°. Berechne γ.', ga, f'180 - {al} - {be}', f'γ = 180° − {al}° − {be}° = {ga}°.',
              'Die drei Winkel ergeben zusammen 180°.', '°')
        a['f']['grafik'] = dreieck_bild(al, be, (f'{al}°', f'{be}°', 'γ'))
        return a
    if st == 2:
        art = zyklus('ws2', ['aussen', 'recht', 'begruendung'])
        if art == 'aussen':
            return Z(f'Ein Außenwinkel bei C ist der Nebenwinkel von γ. Berechne ihn für α = {al}° und β = {be}°.', al + be, f'{al} + {be}',
                     f'Außenwinkel bei C = α + β = {al}° + {be}° = {al + be}°. (Probe: 180° − γ = 180° − {ga}° = {al + be}°)', 'Außenwinkel = 180° − Innenwinkel, oder Summe der beiden anderen Innenwinkel.', '°')
        if art == 'begruendung':
            seite = R.choice(['links', 'rechts'])
            r = 'Wechselwinkel zu α' if seite == 'links' else 'Wechselwinkel zu β'
            wert = al if seite == 'links' else be
            a = A(R, f'Im Dreieck ist α = {al}° und β = {be}°. Durch C ist die Parallele zu [AB] gezeichnet. {seite.capitalize()} von C entsteht zwischen Parallele und Dreiecksseite ein Winkel von {wert}°. Warum?',
                  r, ['Stufenwinkel zu γ', 'Nebenwinkel von γ', 'Scheitelwinkel von ' + ('β' if seite == 'links' else 'α')],
                  f'Die Parallele durch C und [AB] werden von der Seite {"[AC]" if seite == "links" else "[BC]"} geschnitten: Z-Form, also {r}. Mit γ zusammen ergibt das 180°.',
                  'Welche Gerade schneidet die beiden Parallelen? Liegen die Winkel in Z-Form?')
            p = dreieck(al, be)
            C = p['C']
            p['_l'] = [round(C[0] - 3, 2), C[1]]; p['_r'] = [round(C[0] + 3, 2), C[1]]
            a['f']['grafik'] = figur(p, linien=[['A', 'B'], ['B', 'C'], ['C', 'A'], ['_l', '_r', 'Parallele', 'gestrichelt']], flaeche=['A', 'B', 'C'],
                                     winkel=[['A', 'B', 'C', f'{al}°'], ['B', 'C', 'A', f'{be}°'], ['C', '_l', 'A', f'{al}°' if seite == 'links' else ''], ['C', 'B', '_r', f'{be}°' if seite == 'rechts' else '']])
            a['f']['grafik']['winkel'] = [w for w in a['f']['grafik']['winkel'] if w[3]]
            return a
        a2 = R.randint(15, 75)
        a = Z(f'Ein Dreieck ist bei C rechtwinklig, α = {a2}°. Berechne β.', 90 - a2, f'180 - 90 - {a2}', f'β = 180° − 90° − {a2}° = {90 - a2}°.',
              'Ein rechter Winkel hat 90°.', '°')
        a['f']['grafik'] = figur(dreieck(a2, 90 - a2), linien=[['A', 'B'], ['B', 'C'], ['C', 'A']], flaeche=['A', 'B', 'C'],
                                 rechter_winkel=[['C', 'A', 'B']], winkel=[['A', 'B', 'C', f'{a2}°'], ['B', 'C', 'A', 'β']])
        return a
    if zyklus('ws3', ['verh', 'fehler']) == 'fehler':
        a2 = R.randint(20, 70); s1, s2 = R.randint(95, 130), R.randint(95, 130)
        fall = R.choice([
            (f'Ein Dreieck kann zwei stumpfe Winkel haben, zum Beispiel {s1}° und {s2}°.', f'Falsch: {s1}° + {s2}° = {s1 + s2}° ist schon mehr als 180°.',
             [f'Richtig: Der dritte Winkel ist dann {360 - s1 - s2 if 360 - s1 - s2 > 0 else 10}°.', 'Richtig: Stumpfe Winkel sind in Dreiecken erlaubt.', 'Falsch: Ein Dreieck hat nie einen stumpfen Winkel.']),
            (f'In einem rechtwinkligen Dreieck ist α = {a2}°, also β = {180 - a2}°.', f'Falsch: β = 180° − 90° − {a2}° = {90 - a2}°.',
             [f'Richtig: β = 180° − {a2}° = {180 - a2}°.', f'Falsch: β = 90° + {a2}° = {90 + a2}°.', f'Falsch: β = {a2}°, weil beide spitzen Winkel gleich sind.']),
            (f'Ein Dreieck hat die Winkel {a2}°, {a2 + 30}° und {180 - 2 * a2 - 20}°.', f'Falsch: Die Summe ist {180 + 10}°, nicht 180°.',
             ['Richtig: Alle drei Winkel sind kleiner als 180°.', f'Richtig: {a2}° + {a2 + 30}° + {180 - 2 * a2 - 20}° = 180°.', 'Falsch: Ein Winkel ist zu klein.'])])
        return A(R, f'Jemand sagt: „{fall[0]}“ Was stimmt?', fall[1], fall[2], fall[1], 'Rechne die Winkelsumme nach.')
    k = R.choice([2, 3, 4])
    while True:
        x = R.randint(10, 50)
        rest = 180 - x - k * x
        if rest > 0 and rest != x: break
    return Z(f'In einem Dreieck ist β {k}-mal so groß wie α, und γ = {rest}°. Wie groß ist α?', x, f'(180 - {rest}) / ({k} + 1)',
             f'α + {k}α + {rest}° = 180° → {k + 1}α = {180 - rest}° → α = {x}°.', 'Schreibe β mit α und stelle eine Gleichung auf.', '°')


def g_gleichschenklig(R, st):
    if st == 1:
        g = R.choice(range(20, 161, 2))
        b = (180 - g) // 2
        a = Z(f'Ein gleichschenkliges Dreieck hat den Spitzenwinkel γ = {g}°. Wie groß ist ein Basiswinkel?', b, f'(180 - {g}) / 2', f'(180° − {g}°) : 2 = {b}°.',
              'Die beiden Basiswinkel sind gleich groß.', '°')
        a['f']['grafik'] = figur(dreieck(b, b), linien=[['A', 'B'], ['B', 'C'], ['C', 'A']], flaeche=['A', 'B', 'C'], winkel=[['C', 'A', 'B', f'{g}°'], ['A', 'B', 'C', '?']])
        return a
    if st == 2 and zyklus('gs2', ['basis', 'stumpf']) == 'stumpf':
        g = R.choice(range(96, 171, 2))
        return Z(f'Ein gleichschenkliges Dreieck hat einen Winkel von {g}°. Wie groß sind die beiden anderen Winkel? Gib einen davon an.', (180 - g) // 2, f'(180 - {g}) / 2',
                 f'{g}° ist stumpf. Zwei solche Winkel hätten zusammen mehr als 180°, also kann {g}° kein Basiswinkel sein – er ist der Spitzenwinkel. Basiswinkel: (180° − {g}°) : 2 = {(180 - g) // 2}°.',
                 'Kann ein stumpfer Winkel zweimal im Dreieck vorkommen?', '°')
    if st == 2:
        b = R.randint(20, 85)
        a = Z(f'Ein gleichschenkliges Dreieck hat den Basiswinkel {b}°. Wie groß ist der Spitzenwinkel?', 180 - 2 * b, f'180 - 2 * {b}',
              f'Zwei Basiswinkel: 2 · {b}° = {2 * b}°. Spitzenwinkel: 180° − {2 * b}° = {180 - 2 * b}°.', 'Es gibt zwei gleich große Basiswinkel.', '°')
        a['f']['grafik'] = figur(dreieck(b, b), linien=[['A', 'B'], ['B', 'C'], ['C', 'A']], flaeche=['A', 'B', 'C'], winkel=[['A', 'B', 'C', f'{b}°'], ['C', 'A', 'B', '?']])
        return a
    art = zyklus('gs3', ['aussen_spitze', 'aussen', 'zwei', 'aussen_spitze', 'gleichseitig'])
    if art == 'aussen_spitze':
        w = R.choice(range(20, 179, 2))
        return Z(f'Der Außenwinkel an der Spitze eines gleichschenkligen Dreiecks ist {w}°. Wie groß ist ein Basiswinkel?', Fr(w, 2), f'{w} / 2',
                 f'Spitzenwinkel = 180° − {w}° = {180 - w}°. Basiswinkel = (180° − {180 - w}°) : 2 = {zt(Fr(w, 2))}°. Kurz: Der Außenwinkel ist die Summe der beiden Basiswinkel.',
                 'Erst den Spitzenwinkel aus dem Nebenwinkel bestimmen.', '°')
    if art == 'aussen':
        w = R.choice(range(100, 171, 2))
        return Z(f'Bei einem gleichschenkligen Dreieck ist der Außenwinkel an einem Basiswinkel {w}°. Wie groß ist der Spitzenwinkel?', 180 - 2 * (180 - w),
                 f'180 - 2 * (180 - {w})', f'Basiswinkel = 180° − {w}° = {180 - w}°. Spitzenwinkel = 180° − 2 · {180 - w}° = {180 - 2 * (180 - w)}°.',
                 'Erst den Basiswinkel aus dem Nebenwinkel bestimmen.', '°')
    if art == 'zwei':
        g = R.choice([20, 30, 36, 40, 44, 50, 60, 70, 80, 100])
        return Z(f'Ein Dach ist im Querschnitt ein gleichschenkliges Dreieck. Der Winkel am First beträgt {g}°. Wie steil ist das Dach (Winkel zwischen Dachfläche und waagrechtem Boden)?',
                 Fr(180 - g, 2), f'(180 - {g}) / 2', f'Die Dachneigung ist ein Basiswinkel: (180° − {g}°) : 2 = {zt(Fr(180 - g, 2))}°.', 'Der Winkel am First ist der Spitzenwinkel.', '°')
    n = R.choice([2, 3, 4])
    return Z(f'Wie groß ist die Summe aller Innenwinkel in einer Figur aus {n} gleichseitigen Dreiecken, die zu einem Streifen aneinandergelegt sind? (Zähle jedes Dreieck einzeln.)',
             180 * n, f'180 * {n}', f'Jedes Dreieck hat 180°: {n} · 180° = {180 * n}°. Jeder einzelne Winkel ist 60°.', 'Jedes Dreieck hat die Winkelsumme 180°.', '°')


SAETZE = ['SSS', 'SWS', 'WSW', 'SsW', 'nicht eindeutig']
NE = 'keiner – mit diesen Angaben ist das Dreieck nicht eindeutig festgelegt'


def ssw_fall(R, fall):
    """SsW-Lage: Winkel α bei A, Seite c = AB, Seite a = BC (gegenüber α). Liefert (a, c, α)."""
    for _ in range(500):
        c = R.randint(5, 12); al = R.choice(range(20, 71, 5)); h = c * math.sin(math.radians(al))
        if fall == 'eindeutig':
            a = R.randint(c, c + 4); return a, c, al
        if fall == 'zwei':
            a = R.randint(2, c - 1)
            if h + 0.4 < a: return a, c, al
        if fall == 'kein':
            a = R.randint(2, c - 1)
            if a < h - 0.4: return a, c, al
        if fall == 'recht':
            c = R.choice([6, 8, 10, 12]); return c // 2, c, 30


SSW_ANTW = {'eindeutig': 'genau ein Dreieck (SsW: der Winkel liegt der längeren Seite gegenüber)', 'zwei': 'zwei verschiedene Dreiecke',
            'recht': 'genau ein (rechtwinkliges) Dreieck', 'kein': 'kein Dreieck'}


def g_kongruenzsatz(R, st):
    if st == 3:
        fall = zyklus('ssw3', ['zwei', 'eindeutig', 'kein', 'recht'])
        a, c, al = ssw_fall(R, fall)
        h = c * math.sin(math.radians(al))
        w = {'eindeutig': f'a = {a} cm ist nicht kürzer als c = {c} cm: Der Kreis um B schneidet den freien Schenkel von α nur einmal.',
             'zwei': f'a = {a} cm ist kürzer als c = {c} cm, aber länger als der Abstand von B zum freien Schenkel (≈ {zt(Fr(str(round(h, 1))))} cm): Der Kreis um B schneidet zweimal.',
             'kein': f'Der Abstand von B zum freien Schenkel ist ≈ {zt(Fr(str(round(h, 1))))} cm, a = {a} cm ist kürzer: Der Kreis um B erreicht den Schenkel nicht.',
             'recht': f'Der Abstand von B zum freien Schenkel ist bei α = 30° genau c : 2 = {a} cm: Der Kreis berührt den Schenkel nur in einem Punkt, dort ist der Winkel 90°.'}[fall]
        return A(R, f'Gegeben: a = {a} cm, c = {c} cm, α = {al}° (α liegt a gegenüber). Wie viele Dreiecke gibt es?', SSW_ANTW[fall],
                 [v for k, v in SSW_ANTW.items() if k != fall], w, 'Zeichne c und α. Schlage um B einen Kreis mit Radius a: Wie oft trifft er den freien Schenkel?')
    a, b, c = sorted(R.sample(range(3, 12), 3))
    w1, w2 = R.sample(range(25, 80, 5), 2)
    art = R.choice(SAETZE if st > 1 else SAETZE[:3])
    seiten = R.sample(['a', 'b', 'c'], 3)
    win = {'a': 'α', 'b': 'β', 'c': 'γ'}
    if art == 'SSS':
        if a + b <= c: c = a + b - 1
        txt, gr = f'a = {a} cm, b = {b} cm, c = {c} cm', 'Drei Seiten gegeben.'
    elif art == 'SWS':
        s1, s2 = seiten[0], seiten[1]; zw = [x for x in 'abc' if x not in (s1, s2)][0]
        txt, gr = f'{s1} = {a} cm, {s2} = {b} cm, {win[zw]} = {w1}°', f'{win[zw]} liegt zwischen {s1} und {s2} (eingeschlossener Winkel).'
    elif art == 'WSW':
        s = seiten[0]; andere = [x for x in 'abc' if x != s]
        txt, gr = f'{s} = {a} cm, {win[andere[0]]} = {w1}°, {win[andere[1]]} = {w2}°', 'Eine Seite und zwei Winkel gegeben (der dritte Winkel folgt aus der Winkelsumme).'
    elif art == 'SsW':
        txt, gr = f'a = {a} cm, c = {c} cm, γ = {w1}°', f'γ liegt gegenüber der größeren Seite c = {c} cm.'
    else:
        if R.random() < .5:
            txt, gr = f'α = {w1}°, β = {w2}°, γ = {180 - w1 - w2}°', 'Nur drei Winkel: Form fest, Größe nicht.'
        else:
            a2, c2, al2 = ssw_fall(R, 'zwei')
            txt, gr = f'a = {a2} cm, c = {c2} cm, α = {al2}°', 'α liegt gegenüber der kleineren Seite a – hier gibt es zwei verschiedene Dreiecke.'
    return A(R, f'Gegeben: {txt}. Welcher Kongruenzsatz garantiert ein eindeutiges Dreieck?', art if art != 'nicht eindeutig' else NE,
             [x if x != 'nicht eindeutig' else NE for x in SAETZE if x != art][:3], gr,
             'Zähle Seiten und Winkel. Liegt der Winkel zwischen den Seiten oder gegenüber?')


def g_konstruierbar(R, st):
    if st == 1:
        a, b = R.randint(2, 9), R.randint(2, 9)
        c = R.choice([a + b + R.randint(0, 3), max(a, b) + R.randint(1, min(a, b) - 1) if min(a, b) > 1 else a + b + 1])
        ok = a + b > c and a + c > b and b + c > a
        r = 'Ja, je zwei Seiten sind zusammen länger als die dritte.' if ok else 'Nein, zwei Seiten sind zusammen nicht länger als die dritte.'
        return A(R, f'Kann man ein Dreieck mit a = {a} cm, b = {b} cm und c = {c} cm konstruieren?', r,
                 ['Nein, zwei Seiten sind zusammen nicht länger als die dritte.' if ok else 'Ja, je zwei Seiten sind zusammen länger als die dritte.',
                  'Ja, mit drei Seiten geht es immer.', 'Nein, alle Seiten müssen gleich lang sein.'],
                 f'{min(a, b)} + {max(a, b)} = {a + b} {">" if a + b > c else "≤"} {c}.' + ('' if ok else ' Die Kreisbögen schneiden sich nicht.'),
                 'Prüfe: Sind die beiden kürzeren Seiten zusammen länger als die längste?')
    if st == 2 and zyklus('ko2', ['winkel', 'max', 'min']) == 'winkel':
        c = R.randint(3, 9)
        al = R.choice(range(30, 131, 5)); be = R.choice([180 - al - R.choice([5, 10, 20, 40]), 180 - al, 180 - al + R.choice([5, 10, 15]), 180 - al - 1])
        ok = al + be < 180
        r = f'Ja, γ = 180° − {al}° − {be}° = {180 - al - be}°.' if ok else f'Nein, {al}° + {be}° = {al + be}° ist nicht kleiner als 180°.'
        return A(R, f'Kann man ein Dreieck mit c = {c} cm, α = {al}° und β = {be}° konstruieren?', r,
                 [f'Nein, {al}° + {be}° = {al + be}° ist nicht kleiner als 180°.' if ok else f'Ja, γ = 180° − {al}° − {be}° = {180 - al - be}°.',
                  'Ja, mit einer Seite und zwei Winkeln geht es immer (WSW).', f'Nein, die Seite c = {c} cm ist zu kurz.'],
                 f'α + β = {al + be}°' + (f' < 180°, γ = {180 - al - be}°.' if ok else ' – die freien Schenkel schneiden sich nicht (oberhalb von AB).'),
                 'Zwei Winkel eines Dreiecks müssen zusammen weniger als 180° haben.')
    if st == 2:
        a, b = R.randint(2, 12), R.randint(2, 12)
        if ZYK['ko2'] % 3 == 1:
            return Z(f'Zwei Seiten eines Dreiecks sind {a} cm und {b} cm lang. Die dritte Seite ist ganzzahlig. Wie lang kann sie höchstens sein?', a + b - 1, f'{a} + {b} - 1',
                     f'Die dritte Seite muss kürzer als {a} + {b} = {a + b} cm sein. Größte ganze Zahl: {a + b - 1} cm.', 'Dreiecksungleichung: c < a + b.', 'cm')
        if a == b: b += 1
        return Z(f'Zwei Seiten eines Dreiecks sind {a} cm und {b} cm lang. Die dritte Seite ist ganzzahlig. Wie lang muss sie mindestens sein?', abs(a - b) + 1, f'abs({a} - {b}) + 1',
                 f'Die dritte Seite muss länger als {max(a, b)} − {min(a, b)} = {abs(a - b)} cm sein. Kleinste ganze Zahl: {abs(a - b) + 1} cm.', 'Auch die längere der beiden gegebenen Seiten muss kürzer sein als die anderen beiden zusammen.', 'cm')
    a, b = R.randint(3, 10), R.randint(3, 10)
    lo, hi = abs(a - b) + 1, a + b - 1
    return Z(f'Zwei Seiten eines Dreiecks sind {a} cm und {b} cm lang. Wie viele verschiedene ganzzahlige Längen (in cm) sind für die dritte Seite möglich?', hi - lo + 1,
             f'({a} + {b} - 1) - (abs({a} - {b}) + 1) + 1', f'Möglich: {abs(a - b)} < c < {a + b}, also c = {lo}, …, {hi}. Das sind {hi - lo + 1} Längen.',
             'Bestimme die kleinste und die größte mögliche ganze Länge.')


def g_vierecke(R, st):
    if st == 1:
        al = R.choice(range(40, 141, 5))
        if al == 90: al = 75
        a = Z(f'In einem Parallelogramm ABCD ist α = {al}°. Wie groß ist β?', 180 - al, f'180 - {al}', f'Benachbarte Winkel ergänzen sich zu 180°: β = 180° − {al}° = {180 - al}°.',
              'Benachbarte Winkel im Parallelogramm ergeben zusammen 180°.', '°')
        dx = round(3 / math.tan(math.radians(al)), 2)
        a['f']['grafik'] = figur({'A': [0, 0], 'B': [5, 0], 'C': [5 + dx, 3], 'D': [dx, 3]}, linien=[['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A']], flaeche=['A', 'B', 'C', 'D'],
                                 winkel=[['A', 'B', 'D', f'{al}°'], ['B', 'C', 'A', 'β']])
        return a
    if st == 2:
        art = R.choice(['drachen', 'trapez', 'raute'])
        if art == 'drachen':
            a_, c_ = R.choice(range(50, 131, 5)), R.choice(range(30, 101, 5))
            b = Fr(360 - a_ - c_, 2)
            return Z(f'Ein Drachenviereck ABCD ist symmetrisch zur Diagonalen AC. Es ist α = {a_}° und γ = {c_}°. Wie groß ist β (= δ)?', b, f'(360 - {a_} - {c_}) / 2',
                     f'β = δ (liegen symmetrisch). 2β = 360° − {a_}° − {c_}° = {360 - a_ - c_}° → β = {zt(b)}°.', 'Winkelsumme im Viereck 360°, β und δ sind gleich.', '°')
        if art == 'trapez':
            al = R.choice(range(40, 86, 5))
            return Z(f'In einem gleichschenkligen Trapez ABCD (AB ∥ CD) ist α = {al}°. Wie groß ist γ?', 180 - al, f'180 - {al}',
                     f'β = α = {al}° (gleiche Winkel an der Grundseite AB). γ = 180° − β = {180 - al}° (Winkel an derselben Schenkelseite ergänzen sich zu 180°).', 'Winkel an einem Schenkel ergänzen sich zu 180°.', '°')
        al = R.choice(range(40, 141, 5))
        return Z(f'In einer Raute ABCD ist α = {al}°. Die Diagonale AC halbiert α. Wie groß ist der Winkel zwischen AC und der Seite AB?', Fr(al, 2), f'{al} / 2',
                 f'Die Diagonalen einer Raute sind Symmetrieachsen und halbieren die Winkel: {al}° : 2 = {zt(Fr(al, 2))}°.', 'Diagonalen einer Raute sind Winkelhalbierende.', '°')
    a_, b_, c_ = R.randint(60, 120), R.randint(60, 120), R.randint(60, 120)
    d = 360 - a_ - b_ - c_
    if d <= 0: return g_vierecke(R, st)
    return Z(f'In einem Viereck ist α = {a_}°, β = {b_}° und γ = {c_}°. Berechne δ.', d, f'360 - {a_} - {b_} - {c_}', f'δ = 360° − {a_}° − {b_}° − {c_}° = {d}°.',
             'Ein Viereck lässt sich in zwei Dreiecke zerlegen: 2 · 180° = 360°.', '°')


KEHR = [  # Satz, Kehrsatz, Kehrsatz wahr?, Gegenbeispiel, falsche Gegenbeispiele (erfüllen beide Teile bzw. den Wenn-Teil des Kehrsatzes nicht)
    ('Wenn ein Viereck ein Quadrat ist, dann hat es vier gleich lange Seiten.', 'Wenn ein Viereck vier gleich lange Seiten hat, dann ist es ein Quadrat.', False, 'eine Raute mit 60°-Winkel',
     ['ein Quadrat mit 3 cm Seitenlänge', 'ein Rechteck 2 cm × 5 cm']),
    ('Wenn ein Dreieck gleichseitig ist, dann sind alle Winkel 60°.', 'Wenn in einem Dreieck alle Winkel 60° sind, dann ist es gleichseitig.', True, '',
     ['ein Dreieck mit den Winkeln 50°, 60° und 70°', 'ein gleichschenkliges Dreieck mit 40° an der Spitze']),
    ('Wenn ein Dreieck gleichschenklig ist, dann hat es zwei gleich große Winkel.', 'Wenn ein Dreieck zwei gleich große Winkel hat, dann ist es gleichschenklig.', True, '',
     ['ein Dreieck mit den Winkeln 30°, 60° und 90°', 'ein gleichseitiges Dreieck']),
    ('Wenn ein Viereck ein Rechteck ist, dann sind seine Diagonalen gleich lang.', 'Wenn die Diagonalen eines Vierecks gleich lang sind, dann ist es ein Rechteck.', False, 'ein gleichschenkliges Trapez',
     ['ein Quadrat', 'eine Raute mit 60°-Winkel']),
    ('Wenn ein Viereck eine Raute ist, dann stehen die Diagonalen senkrecht aufeinander.', 'Wenn die Diagonalen eines Vierecks senkrecht aufeinander stehen, dann ist es eine Raute.', False,
     'ein Drachenviereck, das keine Raute ist', ['ein Quadrat', 'ein Rechteck 2 cm × 5 cm']),
    ('Wenn ein Viereck ein Parallelogramm ist, dann halbieren sich seine Diagonalen.', 'Wenn sich die Diagonalen eines Vierecks halbieren, dann ist es ein Parallelogramm.', True, '',
     ['ein Drachenviereck, das keine Raute ist', 'ein Rechteck 2 cm × 5 cm']),
    ('Wenn zwei Dreiecke kongruent sind, dann haben sie gleich große Winkel.', 'Wenn zwei Dreiecke gleich große Winkel haben, dann sind sie kongruent.', False,
     'zwei verschieden große gleichseitige Dreiecke', ['zwei deckungsgleiche Dreiecke', 'ein Dreieck mit 30°, 60°, 90° und eines mit 45°, 45°, 90°']),
    ('Wenn eine Zahl durch 4 teilbar ist, dann ist sie gerade.', 'Wenn eine Zahl gerade ist, dann ist sie durch 4 teilbar.', False, 'die Zahl 6', ['die Zahl 8', 'die Zahl 7']),
    ('Wenn ein Dreieck einen rechten Winkel hat, dann sind die beiden anderen Winkel zusammen 90°.', 'Wenn in einem Dreieck zwei Winkel zusammen 90° sind, dann hat es einen rechten Winkel.', True, '',
     ['ein Dreieck mit den Winkeln 40°, 60° und 80°', 'ein Dreieck mit den Winkeln 90°, 45° und 45°']),
    ('Wenn ein Viereck ein Rechteck ist, dann hat es vier rechte Winkel.', 'Wenn ein Viereck vier rechte Winkel hat, dann ist es ein Rechteck.', True, '',
     ['ein Quadrat', 'eine Raute mit 60°-Winkel']),
    ('Wenn eine Zahl durch 6 teilbar ist, dann ist sie durch 3 teilbar.', 'Wenn eine Zahl durch 3 teilbar ist, dann ist sie durch 6 teilbar.', False, 'die Zahl 9', ['die Zahl 12', 'die Zahl 8']),
    ('Wenn ein Viereck eine Raute ist, dann ist es ein Parallelogramm.', 'Wenn ein Viereck ein Parallelogramm ist, dann ist es eine Raute.', False,
     'ein Parallelogramm mit den Seiten 3 cm und 6 cm', ['ein Quadrat', 'ein Drachenviereck, das keine Raute ist']),
    ('Wenn ein Dreieck gleichseitig ist, dann ist es gleichschenklig.', 'Wenn ein Dreieck gleichschenklig ist, dann ist es gleichseitig.', False,
     'ein Dreieck mit den Seiten 5 cm, 5 cm und 3 cm', ['ein Dreieck mit den Seiten 4 cm, 4 cm und 4 cm', 'ein Dreieck mit den Seiten 3 cm, 4 cm und 5 cm']),
    ('Wenn ein Viereck ein Quadrat ist, dann ist es ein Rechteck.', 'Wenn ein Viereck ein Rechteck ist, dann ist es ein Quadrat.', False, 'ein Rechteck 2 cm × 5 cm',
     ['ein Quadrat mit 4 cm Seitenlänge', 'eine Raute mit 60°-Winkel']),
]


def gr(t): return t[0].upper() + t[1:]


def g_satz_kehrsatz(R, st):
    satz, kehr, wahr, gegen, falsche = R.choice(KEHR)
    if st == 2: st = R.choice([1, 2, 2, 3])
    if st == 1:
        andere = [k for s, k, *_ in KEHR if k != kehr]
        return A(R, f'Wie lautet der Kehrsatz zu: „{satz}“', kehr, [satz] + R.sample(andere, 2), f'Voraussetzung und Behauptung werden vertauscht: „{kehr}“',
                 'Tausche den Wenn-Teil und den Dann-Teil.')
    if st == 2:
        r = 'Der Kehrsatz ist wahr.' if wahr else f'Der Kehrsatz ist falsch, Gegenbeispiel: {gegen}.'
        f = [f'Der Kehrsatz ist falsch, Gegenbeispiel: {g}.' for g in falsche]
        f += ['Der Kehrsatz ist wahr.'] if not wahr else ['Der Kehrsatz ist falsch, weil Kehrsätze nie stimmen.']
        w = r + (f' {gr(gegen)} erfüllt den Wenn-Teil des Kehrsatzes, aber nicht den Dann-Teil.' if not wahr else
                 f' {gr(falsche[0])} und {falsche[1]} sind keine Gegenbeispiele: Bei ihnen ist die Voraussetzung nicht erfüllt oder die Behauptung doch erfüllt.')
        return A(R, f'Satz: „{satz}“ Ist der Kehrsatz „{kehr}“ wahr?', r, f, w, 'Ein Gegenbeispiel muss den Wenn-Teil des Kehrsatzes erfüllen, den Dann-Teil aber nicht.')
    if wahr:
        return A(R, f'Ein Schüler sagt: „Der Satz ‚{satz}‘ ist wahr, also ist auch der Kehrsatz wahr.“ Ist die Begründung richtig?', 'Nein: Die Begründung ist falsch, auch wenn der Kehrsatz hier zufällig stimmt.',
                 ['Ja, ein Kehrsatz ist immer wahr, wenn der Satz wahr ist.', 'Ja, weil man den Satz nur umdrehen muss.', 'Nein, denn der Satz selbst ist falsch.'],
                 'Aus der Wahrheit eines Satzes folgt nichts über den Kehrsatz; er muss eigens bewiesen werden.', 'Gibt es Sätze, deren Kehrsatz falsch ist?')
    return A(R, f'Widerlege den Kehrsatz: „{kehr}“ Welches Gegenbeispiel passt?', gr(gegen), [gr(g) for g in falsche],
             f'{gr(gegen)} erfüllt die Voraussetzung, aber nicht die Behauptung. {gr(falsche[0])} erfüllt beide oder die Voraussetzung nicht.',
             'Das Gegenbeispiel muss den Wenn-Teil erfüllen, den Dann-Teil nicht.')


GEN = {'parallelen': g_parallelen, 'winkelsumme': g_winkelsumme, 'gleichschenklig': g_gleichschenklig, 'kongruenzsatz': g_kongruenzsatz, 'konstruierbar': g_konstruierbar,
       'vierecke': g_vierecke, 'satz_kehrsatz': g_satz_kehrsatz}

# Verständliche Fassung (Runde 7, Maßstab inhalte/README.md „Verständliche Erklärungen“):
# Alltagssituation zuerst (einstieg), jedes neue Wort erklärt (woerter), Beispiel in kleinen Schritten, Merksatz am Ende (regel).
# Situationen: Straßen auf dem Stadtplan, Giebel eines Gartenhauses, Dreiecke aus Holzleisten, Drachen und Scherengitter, Regen und nasse Straße.
KLAR = {
 'parallelen': {
  'einstieg': 'Auf einem Stadtplan laufen zwei Straßen schnurgerade nebeneinander her, ohne sich je zu treffen. Eine dritte Straße kreuzt beide schräg. An beiden Kreuzungen sehen die Ecken genau gleich aus: Sie haben dieselben Winkel. Diese gleichen Winkel heißen ⟦Stufenwinkel⟧ und ⟦Wechselwinkel⟧.',
  'woerter': [['Gerade', 'eine gerade Linie ohne Anfang und Ende'], ['parallel', 'zwei Geraden, die überall gleich weit voneinander entfernt sind und sich nie treffen'],
              ['α, β, γ', 'griechische Buchstaben (Alpha, Beta, Gamma) als Namen für Winkel'], ['S, T', 'die beiden Kreuzungspunkte'],
              ['Stufenwinkel', 'Winkel an den beiden Kreuzungen in derselben Lage, zum Beispiel jeweils rechts oberhalb'],
              ['Wechselwinkel', 'Winkel auf verschiedenen Seiten; verbindet man sie, entsteht ein „Z“']],
  'schritte': ['g und h sind parallel. Eine dritte Gerade schneidet g im Punkt S und h im Punkt T. Bei S ist α = 55°.',
               'β liegt bei T an derselben Stelle wie α bei S, nämlich rechts oberhalb. Das sind Stufenwinkel, also ⟦β = 55°⟧.',
               'γ liegt bei T links unterhalb, α bei S rechts oberhalb. Verbindet man die beiden, entsteht ein Z: Das sind Wechselwinkel, also ⟦γ = 55°⟧.'],
  'regel': 'So nutzt du Winkel an Parallelen: Werden zwei ⟦parallele⟧ Geraden von einer dritten geschnitten, sind ⟦Stufenwinkel⟧ (gleiche Lage) und ⟦Wechselwinkel⟧ (Z-Form) gleich groß. Das gilt ⟦nur⟧, wenn die Geraden wirklich parallel sind.',
  'fehler': 'Sind g und h nicht parallel – wie zwei Straßen, die aufeinander zulaufen –, dann sind die Stufenwinkel im Allgemeinen ⟦verschieden⟧. Umgekehrt gilt: Sind Stufenwinkel gleich groß, dann sind die Geraden parallel.'},
 'winkelsumme': {
  'einstieg': 'Ein Gartenhaus bekommt ein Dach mit dreieckigem Giebel. Der Zimmermann misst unten links 50° und unten rechts 75°. Den Winkel ganz oben muss er nicht messen – er kann ihn ausrechnen. In jedem Dreieck ergeben die drei Winkel zusammen gleich viel: Das ist die ⟦Winkelsumme⟧.',
  'woerter': [['Winkelsumme', 'alle Winkel innen im Dreieck zusammengezählt'], ['A, B, C', 'die Ecken des Dreiecks; α liegt bei A, β bei B, γ bei C'],
              ['[AB]', 'die Strecke von A nach B'], ['gestreckter Winkel', 'ein Winkel von 180°; er sieht aus wie eine gerade Linie']],
  'schritte': ['Im Dreieck sind zwei Winkel bekannt: α = 50° und β = 75°.',
               'Alle drei Winkel ergeben zusammen 180°. Für γ bleibt also: γ = 180° − 50° − 75°.',
               'Ausrechnen: 180° − 125° = ⟦55°⟧.',
               'Warum 180°? Zieh durch C eine Parallele zu [AB]. Links von C taucht α wieder auf, rechts β (Wechselwinkel). Zusammen mit γ liegen sie auf einer geraden Linie, also 180°.'],
  'regel': 'So berechnest du einen fehlenden Winkel im Dreieck: Ziehe die beiden bekannten Winkel von 180° ab. Denn in jedem Dreieck ist die ⟦Winkelsumme 180°⟧: α + β + γ = 180°.',
  'fehler': 'γ = 360° − 50° − 75° ist falsch. 360° ist die Winkelsumme im ⟦Viereck⟧ – so viel wie eine volle Drehung. Im Dreieck sind es 180°, eine halbe Drehung.'},
 'gleichschenklig': {
  'einstieg': 'Der Giebel des Gartenhauses ist gleichmäßig gebaut: Die beiden schrägen Dachseiten sind gleich lang. Darum sind auch die beiden Winkel unten gleich groß – das Dach ist auf beiden Seiten gleich steil. So ein Dreieck heißt ⟦gleichschenklig⟧.',
  'woerter': [['Schenkel', 'die beiden gleich langen Seiten (die Dachseiten)'], ['Basis', 'die dritte Seite (unten)'], ['Basiswinkel', 'die beiden Winkel an der Basis; sie sind gleich groß'],
              ['Spitzenwinkel', 'der Winkel oben zwischen den Schenkeln'], ['gleichseitig', 'alle drei Seiten gleich lang; dann sind alle Winkel 60°']],
  'schritte': ['Der Spitzenwinkel oben ist γ = 40°.',
               'Für die beiden Basiswinkel bleiben zusammen 180° − 40° = 140°.',
               'Die Basiswinkel sind gleich groß, also teilt man durch 2: 140° : 2 = ⟦70°⟧.',
               'Probe: 70° + 70° + 40° = 180°. ✓'],
  'regel': 'So rechnest du im ⟦gleichschenkligen Dreieck⟧: Die beiden ⟦Basiswinkel⟧ sind gleich groß. Kennst du den Spitzenwinkel, ziehst du ihn von 180° ab und teilst den Rest durch 2. Im ⟦gleichseitigen⟧ Dreieck sind alle Winkel 60°.',
  'fehler': 'Bei γ = 40° sind die Basiswinkel nicht auch je 40°. Nur die ⟦beiden Basiswinkel⟧ sind gleich – so wie beim Giebel nur die beiden unteren Ecken gleich steil sind und die Spitze anders aussieht.'},
 'kongruenzsatz': {
  'einstieg': 'Zwei Freunde wollen am Telefon genau dasselbe Dreieck aus Holzleisten bauen. Was muss der eine dem anderen sagen, damit beide Dreiecke garantiert gleich werden? Manchmal reichen drei Angaben, manchmal nicht. Die Regeln dafür heißen ⟦Kongruenzsätze⟧.',
  'woerter': [['kongruent', 'deckungsgleich: die Dreiecke passen genau aufeinander'], ['a, b, c', 'die Seiten des Dreiecks; a liegt gegenüber von A, b gegenüber von B, c gegenüber von C'],
              ['eindeutig', 'es gibt nur ein einziges Dreieck mit diesen Angaben'], ['S und W', 'S steht für eine Seite, W für einen Winkel'],
              ['SSS, SWS, WSW, SsW', 'die vier Kongruenzsätze: welche Seiten und Winkel man angeben muss'], ['eingeschlossener Winkel', 'der Winkel, der zwischen den beiden gegebenen Seiten liegt']],
  'schritte': ['Gegeben sind b = 5 cm, c = 7 cm und α = 40°.',
               'Wo liegt α? Bei der Ecke A. Dort treffen sich die Seiten b und c.',
               'Der Winkel liegt also zwischen den beiden gegebenen Seiten: Seite – Winkel – Seite.',
               'Der passende Kongruenzsatz ist ⟦SWS⟧. Mit diesen Angaben gibt es nur ein einziges Dreieck.'],
  'regel': 'So findest du den ⟦Kongruenzsatz⟧: ⟦SSS⟧ – drei Seiten. ⟦SWS⟧ – zwei Seiten und der Winkel dazwischen. ⟦WSW⟧ – eine Seite und zwei Winkel. ⟦SsW⟧ – zwei Seiten und der Winkel gegenüber der ⟦größeren⟧ Seite. Passt einer davon, ist das Dreieck eindeutig.',
  'fehler': 'Drei Winkel (WWW) reichen nicht. Sagt der Freund nur „60°, 60°, 60°“, kann das Dreieck aus 10-cm-Leisten oder aus 1-m-Leisten sein: gleiche Form, aber ⟦verschieden groß⟧.'},
 'konstruierbar': {
  'einstieg': 'Du hast drei Holzleisten: 3 cm, 4 cm und 8 cm lang. Legst du die beiden kurzen an die Enden der langen, reichen sie nicht bis zueinander – es entsteht kein Dreieck. Ob man aus gegebenen Stücken ein Dreieck bauen kann, fragt man so: Ist es ⟦konstruierbar⟧?',
  'woerter': [['konstruierbar', 'man kann das Dreieck mit Zirkel und Lineal zeichnen'], ['Dreiecksungleichung', 'je zwei Seiten zusammen müssen länger sein als die dritte'],
              ['Kreisbogen', 'ein Stück Kreis, mit dem Zirkel gezeichnet; alle seine Punkte sind gleich weit vom Einstichpunkt entfernt']],
  'schritte': ['Gegeben sind a = 3 cm, b = 4 cm und c = 8 cm.',
               'Zeichne c = 8 cm. Um die beiden Enden schlägst du Kreisbögen mit 3 cm und mit 4 cm.',
               'Die beiden kurzen Seiten sind zusammen 3 cm + 4 cm = 7 cm. Das ist weniger als 8 cm, deshalb treffen sich die Kreisbögen nicht.',
               'Es gibt keinen dritten Eckpunkt: ⟦nicht konstruierbar⟧.'],
  'regel': 'So prüfst du, ob ein Dreieck ⟦konstruierbar⟧ ist: Aus drei Seiten nur, wenn ⟦je zwei Seiten zusammen länger⟧ sind als die dritte. Zwei gegebene Winkel müssen zusammen ⟦weniger als 180°⟧ ergeben, sonst bleibt nichts für den dritten Winkel.',
  'fehler': 'Bei a = 3 cm, b = 5 cm und c = 8 cm entsteht auch kein Dreieck: 3 + 5 = 8 ist ⟦nicht größer⟧ als 8. Die beiden kurzen Leisten lägen flach auf der langen – alle Ecken auf einer Linie.'},
 'vierecke': {
  'einstieg': 'Ein Drachen zum Steigenlassen hat vier Ecken und ist links und rechts gleich gebaut. Ein Scherengitter am Gartentor besteht aus schiefen Vierecken, deren gegenüberliegende Seiten parallel sind. Bei solchen Vierecken hängen die Winkel nach festen Regeln zusammen. Für alle Vierecke gilt eine feste ⟦Winkelsumme im Viereck⟧.',
  'woerter': [['Parallelogramm', 'Viereck, bei dem gegenüberliegende Seiten parallel sind (wie beim Scherengitter)'],
              ['Drachenviereck', 'Viereck, das an einer Diagonale achsensymmetrisch ist (wie der Drachen)'],
              ['gleichschenkliges Trapez', 'Viereck mit zwei parallelen Seiten (Grundseiten) und zwei gleich langen schrägen Seiten'],
              ['benachbart / gegenüberliegend', 'Winkel nebeneinander an einer Seite / Winkel an entgegengesetzten Ecken'], ['δ', 'Delta, griechischer Buchstabe für den vierten Winkel (bei D)'],
              ['spitz / stumpf', 'kleiner als 90° / größer als 90°'], ['Diagonale', 'Verbindungsstrecke zweier gegenüberliegender Ecken']],
  'schritte': ['Im Parallelogramm ABCD ist α = 65°.',
               'Gegenüberliegende Winkel sind gleich groß. γ liegt gegenüber von α, also ist γ = 65°.',
               'Benachbarte Winkel ergänzen sich zu 180°. β liegt neben α: β = 180° − 65° = ⟦115°⟧. Genauso ist δ = 115°.',
               'Probe mit der Winkelsumme: 65° + 115° + 65° + 115° = 360°. ✓'],
  'regel': 'So berechnest du Winkel in Vierecken: Die ⟦Winkelsumme im Viereck⟧ ist ⟦360°⟧. Im ⟦Parallelogramm⟧ sind gegenüberliegende Winkel gleich, benachbarte ergeben 180°. Im ⟦Drachenviereck⟧ sind die beiden Winkel gleich, die nicht auf der Symmetrieachse liegen. Im ⟦gleichschenkligen Trapez⟧ sind die beiden Winkel an einer Grundseite gleich.',
  'fehler': 'Im Parallelogramm ist β nicht auch 65°. ⟦Benachbarte⟧ Winkel ergänzen sich zu 180°, nur ⟦gegenüberliegende⟧ sind gleich. Beim Scherengitter sieht man es: Wird eine Ecke spitzer, wird die Ecke daneben stumpfer.'},
 'satz_kehrsatz': {
  'einstieg': 'Ein Satz aus dem Alltag: „Wenn es regnet, dann ist die Straße nass.“ Das stimmt. Dreht man ihn um, heißt er: „Wenn die Straße nass ist, dann regnet es.“ Das stimmt nicht immer – vielleicht war nur die Straßenreinigung da. Der umgedrehte Satz heißt ⟦Kehrsatz⟧.',
  'woerter': [['Satz', 'eine bewiesene Aussage der Form „Wenn …, dann …“'], ['Voraussetzung', 'der Wenn-Teil'], ['Behauptung', 'der Dann-Teil'],
              ['Kehrsatz', 'Wenn-Teil und Dann-Teil vertauscht'], ['Gegenbeispiel', 'ein Fall, in dem der Wenn-Teil stimmt, der Dann-Teil aber nicht']],
  'schritte': ['Der Satz lautet: Wenn ein Viereck ein Quadrat ist, dann hat es vier rechte Winkel. Er ist wahr.',
               'Für den Kehrsatz vertauscht man Wenn-Teil und Dann-Teil: Wenn ein Viereck vier rechte Winkel hat, dann ist es ein Quadrat.',
               'Suche ein Gegenbeispiel: ein Viereck mit vier rechten Winkeln, das kein Quadrat ist. Ein Rechteck mit den Seiten 2 cm und 5 cm passt.',
               'Ein Gegenbeispiel genügt: Der Kehrsatz ist ⟦falsch⟧.'],
  'regel': 'So prüfst du einen ⟦Kehrsatz⟧: Vertausche Voraussetzung und Behauptung („Wenn B, dann A“). Er ist ⟦nicht automatisch wahr⟧. Ein einziges Gegenbeispiel widerlegt ihn; dass er stimmt, muss man eigens begründen.',
  'fehler': 'Aus „der Satz ist wahr“ folgt nicht „der Kehrsatz ist wahr“ – sonst würde jede nasse Straße Regen bedeuten. Jeder Kehrsatz muss ⟦eigens geprüft⟧ werden.'},
}
for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))


if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Winkel', ['parallelen', 'winkelsumme', 'gleichschenklig', 'vierecke']), ('Kongruenz und Konstruktion', ['kongruenzsatz', 'konstruierbar']), ('Beweisen', ['satz_kehrsatz'])],
         'Winkel an Parallelen nutzen, die Winkelsumme begründen, Winkel in Dreiecken und symmetrischen Vierecken berechnen, Kongruenzsätze anwenden, Konstruierbarkeit prüfen und zwischen Satz und Kehrsatz unterscheiden.',
         ['An Parallelen: Stufenwinkel und Wechselwinkel sind gleich groß.', 'Winkelsumme: Dreieck 180°, Viereck 360°.', 'Gleichschenklig: Basiswinkel gleich.', 'Kongruenzsätze: SSS, SWS, WSW, SsW. WWW reicht nicht.',
          'Dreiecksungleichung: je zwei Seiten zusammen länger als die dritte.'],
         offen=['Konstruieren mit Zirkel und Lineal (Konstruktionsschritte, Planfigur, Ortslinien) kann die App nicht abfragen, weil das Kind nicht zeichnen kann. '
                'Gebaut wurden Winkelberechnungen mit Zeichnung, Kongruenzsätze, Konstruierbarkeit und Satz/Kehrsatz.',
                'Mittelsenkrechte und Winkelhalbierende als Ortslinien sind Stoff von geometrie.ortslinien (Klasse 5) und hier nicht wiederholt.'])
