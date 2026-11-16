#!/usr/bin/env python3
"""Thema funktionen.trig – Sinus- und Kosinusfunktion (Klasse 10). Schreibt inhalte/themen/funktionen.trig.json."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403

start(1004)
PI = math.pi


def pi_text(q):
    """Vielfaches von π als Text, z. B. 2π/3, π/6, −π"""
    q = Fr(q)
    if q == 0: return '0'
    z, n = q.numerator, q.denominator
    zt_ = ('−' if z < 0 else '') + ('' if abs(z) == 1 else str(abs(z))) + 'π'
    return zt_ if n == 1 else f'{zt_}/{n}'


def fterm(art, a=1, b=1, d=0):
    """a · sin(b · x) + d als Text (x in Grad)"""
    af = '' if a == 1 else '−' if a == -1 else dz(a) + ' · '
    bx = 'x' if b == 1 else f'{dz(b)}x' if endlich(b) else f'({br(b)})x'
    t = f'{af}{art}({bx})'
    if d: t += f' {plus(d)}'
    return t


def graph(art, a=1, b=1, d=0, c_grad=0, **kw):
    g = {'art': art, 'a': zahlwert_json(a), 'b': zahlwert_json(b), 'c': b * math.radians(c_grad), 'd': zahlwert_json(d)}
    g.update(kw)
    return g


def bild(gs, x=(0, 360), y=None):
    ys = [abs(g['a']) + abs(g['d']) for g in gs]
    m = max(ys + [1])
    if y is None:
        lo = min(g['d'] - abs(g['a']) for g in gs)
        hi = max(g['d'] + abs(g['a']) for g in gs)
        y = (math.floor(min(lo, 0) - 0.5), math.ceil(max(hi, 0) + 0.5))
    return koord(gs, x=x, y=y, grad=True, schritt_x=90 if x[1] - x[0] >= 360 else 45,
                 schritt_y=1 if m <= 6 else 2, streckung=1.4)


ETAPPEN = [
    {'lernziel': 'bogenmass', 'titel': 'Gradmaß und Bogenmaß',
     'regel': 'Das ⟦Bogenmaß⟧ eines Winkels ist die Länge des zugehörigen Bogens am Einheitskreis. ⟦360° entsprechen 2π⟧, also 180° = π. Umrechnen: x = α · π/180°.',
     'schritte': ['60° ins Bogenmaß: 60° · π/180° = π/3.', 'Also ⟦60° = π/3 ≈ 1,05⟧.'],
     'probe': 'π/3 · 180°/π = 60° ✓',
     'fehler': '60° = 60π ist falsch: Man muss durch ⟦180°⟧ teilen: 60/180 = 1/3, also π/3.'},
    {'lernziel': 'werte', 'titel': 'Werte von sin x und cos x',
     'regel': 'sin x und cos x sind die ⟦y- und x-Koordinate⟧ des Punktes am Einheitskreis. Besondere Werte: sin(π/6) = 0,5, sin(π/2) = 1, cos(π) = −1. Taschenrechner bei Bogenmaß auf ⟦RAD⟧ stellen.',
     'schritte': ['sin(5π/6): 5π/6 = 150°, und sin 150° = sin 30°.', 'sin(5π/6) = ⟦0,5⟧.'],
     'probe': 'Der Punkt zu 150° liegt oberhalb der x-Achse: positiv ✓',
     'fehler': 'sin(2) im Gradmodus zu berechnen (≈ 0,035) ist falsch, wenn x = 2 im ⟦Bogenmaß⟧ gemeint ist: sin(2) ≈ 0,909.'},
    {'lernziel': 'periode', 'titel': 'Periode und Periodizität',
     'regel': 'sin und cos wiederholen sich nach ⟦360° = 2π⟧: sin(x + 360°) = sin x. Bei f(x) = sin(b · x) ist die ⟦Periode p = 360° : b⟧ (bzw. 2π : b).',
     'schritte': ['f(x) = sin(3x): p = 360° : 3.', 'p = ⟦120°⟧ = 2π/3.'],
     'probe': 'sin(3 · 120°) = sin 360° = 0 = sin 0 ✓',
     'fehler': 'Bei sin(3x) die Periode 3 · 360° = 1 080° anzunehmen ist falsch: Der Faktor 3 macht die Schwingung ⟦schneller⟧, die Periode wird ⟦kürzer⟧.'},
    {'lernziel': 'parameter', 'titel': 'Amplitude und Verschiebung',
     'regel': 'Bei f(x) = a · sin(b · x) + d ist ⟦|a| die Amplitude⟧ (Streckung in y-Richtung) und ⟦d die Verschiebung⟧ nach oben/unten. Wertemenge: ⟦[d − |a|; d + |a|]⟧.',
     'schritte': ['f(x) = 3 · sin x + 1: Amplitude 3, Mittellinie y = 1.', 'Wertemenge ⟦[−2; 4]⟧, Maximum 4, Minimum −2.'],
     'probe': 'f(90°) = 3 · 1 + 1 = 4 ✓',
     'fehler': 'Bei f(x) = 3 sin x + 1 die Wertemenge [−3; 3] anzugeben ist falsch: Die Mittellinie ist um ⟦d = 1 nach oben⟧ verschoben.'},
    {'lernziel': 'zuordnen', 'titel': 'Graph und Term zuordnen',
     'regel': 'Am Graphen liest du ab: ⟦Mittellinie⟧ (d), ⟦Abstand Maximum–Mittellinie⟧ (|a|), ⟦Länge einer Schwingung⟧ (Periode p, also b = 360° : p) und ob er bei x = 0 mit dem Maximum (cos) oder auf der Mittellinie (sin) startet.',
     'schritte': ['Graph: Mittellinie y = 0, Maximum 2, eine Schwingung von 0° bis 180°, Start auf der Mittellinie steigend.', 'a = 2, b = 360° : 180° = 2: ⟦f(x) = 2 · sin(2x)⟧.'],
     'probe': 'f(45°) = 2 · sin 90° = 2 = Maximum ✓',
     'fehler': 'Die Periode 180° als b = 180 einzusetzen ist falsch: ⟦b = 360° : p⟧ = 2.'},
    {'lernziel': 'eigenschaften', 'titel': 'Nullstellen und Symmetrie',
     'regel': 'sin x hat die Nullstellen ⟦0°, 180°, 360°, …⟧ (k · 180°), cos x die Nullstellen ⟦90°, 270°, …⟧. Der Graph von sin ist ⟦punktsymmetrisch⟧ zum Ursprung, der von cos ⟦achsensymmetrisch⟧ zur y-Achse. cos x = sin(x + 90°).',
     'schritte': ['Nullstellen von cos x zwischen 0° und 360°: Der Punkt am Einheitskreis hat x-Koordinate 0.', 'Bei ⟦90° und 270°⟧.'],
     'probe': 'cos 90° = 0, cos 270° = 0 ✓',
     'fehler': '„cos x hat bei 0° eine Nullstelle“ ist falsch: cos 0° = ⟦1⟧ (Maximum). Die Nullstelle bei 0° hat sin x.'},
    {'lernziel': 'anwendung', 'titel': 'Periodische Vorgänge beschreiben',
     'regel': 'Periodische Vorgänge (Riesenrad, Tageslänge, Gezeiten) beschreibt man mit ⟦h(t) = a · sin(b · t) + d⟧: d = Mittelwert, |a| = halbe Schwankung, b = 360° : Periodendauer.',
     'schritte': ['Riesenrad: Mitte in 20 m Höhe, Radius 18 m, eine Umdrehung in 12 min. Gondel startet unten.', 'h(t) = 20 − 18 · cos(30° · t): nach 4 min h = 20 − 18 · cos 120° = ⟦29 m⟧.'],
     'probe': 't = 6 min: h = 20 + 18 = 38 m (oben) ✓',
     'fehler': 'b = 12 zu nehmen ist falsch: In 12 min läuft der Winkel um ⟦360°⟧, also b = 360° : 12 = 30° pro Minute.'},
]
_E = {e['lernziel']: e for e in ETAPPEN}
_E['werte']['bild'] = bild([graph('sin', name='sin'), graph('cos', name='cos', name_x=150)], x=(0, 360), y=(-1.5, 1.5))
_E['werte']['bild']['schritt_y'] = 0.5
_E['periode']['bild'] = bild([graph('sin', name='sin x'), graph('sin', b=3, name='sin(3x)', name_x=280)], x=(0, 360), y=(-1.5, 1.5))
_E['periode']['bild']['schritt_y'] = 0.5
_E['parameter']['bild'] = bild([graph('sin', a=3, d=1, name='f'), graph('sin', name='sin x', name_x=200)], x=(0, 360), y=(-3, 5))
_E['parameter']['bild']['waagrecht'] = [1]
_E['zuordnen']['bild'] = bild([graph('sin', a=2, b=2)], x=(0, 360), y=(-3, 3))
_E['eigenschaften']['bild'] = bild([graph('cos', name='cos x')], x=(-360, 360), y=(-1.5, 1.5))
_E['eigenschaften']['bild'].update({'schritt_y': 0.5, 'punkte': [{'x': -270, 'y': 0}, {'x': -90, 'y': 0}, {'x': 90, 'y': 0}, {'x': 270, 'y': 0}]})
_E['anwendung']['bild'] = koord([{'art': 'cos', 'a': -18, 'b': 30, 'd': 20, 'bereich': [0, 24]}], x=(0, 24), y=(0, 40), schritt_x=2, schritt_y=5,
                                name_x='t', name_y='h', punkte=[{'x': 4, 'y': 29, 'name': '(4 | 29)'}], streckung=1.4)

GRAD_PI = {30: Fr(1, 6), 45: Fr(1, 4), 60: Fr(1, 3), 90: Fr(1, 2), 120: Fr(2, 3), 135: Fr(3, 4), 150: Fr(5, 6), 180: Fr(1), 210: Fr(7, 6),
           225: Fr(5, 4), 240: Fr(4, 3), 270: Fr(3, 2), 300: Fr(5, 3), 315: Fr(7, 4), 330: Fr(11, 6), 360: Fr(2)}
EXAKT = {0: (0, 1), 30: (Fr(1, 2), None), 90: (1, 0), 150: (Fr(1, 2), None), 180: (0, -1), 210: (Fr(-1, 2), None), 270: (-1, 0), 330: (Fr(-1, 2), None),
         60: (None, Fr(1, 2)), 120: (None, Fr(-1, 2)), 240: (None, Fr(-1, 2)), 300: (None, Fr(1, 2)), 360: (0, 1)}


def pi_luecke(text, q, w, h):
    """Vielfaches von π als Lücke: ganze Zahl → '□ · π', sonst Bruch '□/□ · π'."""
    q = Fr(q)
    if q.denominator == 1:
        return luecken(text, '□ · π', 'Zahl vor π', [q.numerator], w, h, c=[f'{q.numerator}'])
    return luecken(text, '□/□ · π', 'Bruch vor π (gekürzt)', [q.numerator, q.denominator], w, h, c=[f'{q.numerator}', f'{q.denominator}'])


def g_bogenmass(s):
    if s == 1:
        g = R.choice(list(GRAD_PI))
        q = GRAD_PI[g]
        return pi_luecke(f'Gib {g}° im Bogenmaß als Vielfaches von π an.', q, f'{g}° · π/180° = {br(Fr(g, 180))} · π = {pi_text(q)}.',
                         'Teile den Winkel durch 180° und kürze.')
    if s == 2:
        g = R.choice(list(GRAD_PI))
        q = GRAD_PI[g]
        return zahl(f'Wie viel Grad sind {pi_text(q)}?', f'{pi_text(q)} · 180°/π = {br(q)} · 180° = {g}°.', '360° entsprechen 2π. Was entspricht dann π?', g,
                    f'{q.numerator} * 180 / {q.denominator}', einheit='°')
    typ = R.random()
    if typ < 0.4:
        # Bogenlänge am Kreis mit Radius r: b = r · x (x im Bogenmaß)
        r = R.randint(2, 12)
        if R.random() < 0.5:
            x = Fr(R.choice([1, 2, 3, 4, 5, 6]), 2)
            b = r * x
            return zahl(f'Ein Kreis hat den Radius {r} cm. Wie lang ist der Bogen zum Mittelpunktswinkel {dz(x)} (im Bogenmaß)?',
                        f'Am Einheitskreis ist der Bogen {dz(x)} lang; beim Radius {r} cm ist er {r}-mal so lang: b = {r} · {dz(x)} = {dz(b)} cm.',
                        'Das Bogenmaß ist die Bogenlänge am Kreis mit Radius 1. Wie ändert sich der Bogen bei einem größeren Radius?', b, f'{r} * {cf_(x)}', einheit='cm')
        x = Fr(R.choice([1, 3, 5, 7, 9, 11]), R.choice([2, 4, 5]))
        b = r * x
        if not endlich(x) or not endlich(b) or x > 6: return None
        return zahl(f'Ein Kreis hat den Radius {r} cm, ein Bogen ist {dz(b)} cm lang. Wie groß ist der Mittelpunktswinkel im Bogenmaß?',
                    f'x = b : r = {dz(b)} : {r} = {dz(x)}.', 'Bogenlänge = Radius · Winkel im Bogenmaß; nach dem Winkel umstellen.', x, f'{cf_(b)} / {r}')
    if typ < 0.7:
        g = R.randint(1, 359)
        if g in GRAD_PI: return None
        v = gerundet(math.radians(g), 2)
        if v is None: return None
        return zahl(f'Rechne {g}° ins Bogenmaß um. Runde auf zwei Nachkommastellen.', f'{g} · π/180 ≈ {dz(v)}.', 'Multipliziere mit π/180.', v,
                    f'round({g} * {K(PI)} / 180, 2)', tol=0.01)
    x = Fr(R.randint(5, 60), 10)
    v = gerundet(math.degrees(float(x)), 1)
    if v is None: return None
    return zahl(f'Ein Winkel hat im Bogenmaß die Größe {dz(x)}. Wie viel Grad sind das? Runde auf eine Nachkommastelle.', f'{dz(x)} · 180°/π ≈ {dz(v)}°.',
                'Multipliziere mit 180°/π.', v, f'round({float(x)} * 180 / {K(PI)}, 1)', einheit='°', tol=0.1)


# exakte Werte mit Wurzeln: Bezugswinkel → Betrag
ART = {0: '0', 30: '½', 45: '½√2', 60: '½√3', 90: '1'}
GRAD_PI_45 = dict(GRAD_PI)


def exakt_text(f, g):
    """Exakter Wert von sin/cos(g°) als Text (mit Wurzeln)."""
    w = math.sin(math.radians(g)) if f == 'sin' else math.cos(math.radians(g))
    if abs(w) < 1e-9: return '0'
    r = g % 180
    ref = min(r, 180 - r)
    if f == 'cos': ref = 90 - ref
    return ('−' if w < 0 else '') + ART[ref]


def _werte_rechner(s):
    x = Fr(R.randint(1, 60), 10)
    f = R.choice(['sin', 'cos'])
    w = (math.sin if f == 'sin' else math.cos)(float(x))
    v = gerundet(w, 3)
    if v is None: return None
    return zahl(f'Berechne {f}({dz(x)}) (x im Bogenmaß) auf drei Nachkommastellen.', f'Taschenrechner im RAD-Modus: {f}({dz(x)}) ≈ {dz(v)}.',
                'Stelle den Taschenrechner auf Bogenmaß (RAD).', v, f'round({K(w)}, 3)', tol=0.001)


def _werte_einfach(s):
    g = R.choice([k for k in EXAKT if k not in (0, 360)] if s == 2 else [30, 90, 180, 270, 60])
    sn, cs = EXAKT[g]
    f, v = ('sin', sn) if sn is not None else ('cos', cs)
    if sn is not None and cs is not None and R.random() < 0.5: f, v = 'cos', cs
    q = GRAD_PI[g]
    return zahl(f'Gib den exakten Wert von {f}({pi_text(q)}) an.', f'{pi_text(q)} = {g}°; {f} {g}° = {dz(v)}.',
                'Rechne zuerst ins Gradmaß um und denke an den Einheitskreis.', v, cf_(v))


def _werte_wurzel(s):
    g = R.choice([45, 135, 225, 315] + ([30, 60, 120, 150] if s == 2 else [210, 240, 300, 330, 120, 150]))
    f = R.choice(['sin', 'cos'])
    richtig = exakt_text(f, g)
    if richtig.lstrip('−') not in ('½√2', '½√3'): return None
    betrag = richtig.lstrip('−')
    vz = '−' if richtig.startswith('−') else ''
    gegen = '' if vz else '−'
    andere = [gegen + betrag, vz + ('½√3' if betrag == '½√2' else '½√2'), vz + '½', ('√2' if betrag == '½√2' else '√3')]
    q = GRAD_PI[g]
    lage = 'oberhalb' if math.sin(math.radians(g)) > 0 else 'unterhalb'
    seite = 'rechts' if math.cos(math.radians(g)) > 0 else 'links'
    return auswahl(f'Welchen exakten Wert hat {f}({pi_text(q)})?', richtig, andere,
                   f'{pi_text(q)} = {g}°. Der Punkt am Einheitskreis liegt {lage} der x-Achse und {seite} der y-Achse; Bezugswinkel {min(g % 180, 180 - g % 180)}°: {f}({pi_text(q)}) = {richtig}.',
                   'Rechne ins Gradmaß um, bestimme den Bezugswinkel und das Vorzeichen am Einheitskreis.')


def _werte_vorzeichen():
    x = R.choice([Fr(1, 2), 1, Fr(3, 2), 2, Fr(5, 2), 3, Fr(7, 2), 4, Fr(9, 2), 5, Fr(11, 2), 6])
    f = R.choice(['sin', 'cos'])
    w = (math.sin if f == 'sin' else math.cos)(float(x))
    if abs(w) < 0.1: return None
    gr = [(Fr(0), 'π/2 ≈ 1,57'), (Fr(157, 100), 'π ≈ 3,14'), (Fr(314, 100), '3π/2 ≈ 4,71'), (Fr(471, 100), '2π ≈ 6,28')]
    quad = 1 if x < Fr(157, 100) else 2 if x < Fr(314, 100) else 3 if x < Fr(471, 100) else 4
    grenzen = ['0', 'π/2 ≈ 1,57', 'π ≈ 3,14', '3π/2 ≈ 4,71', '2π ≈ 6,28']
    richtig = 'positiv' if w > 0 else 'negativ'
    return auswahl(f'Ist {f}({dz(x)}) (x im Bogenmaß) positiv oder negativ? Entscheide ohne Taschenrechner.', richtig,
                   ['negativ' if w > 0 else 'positiv', 'genau 0', 'Das kann man ohne Taschenrechner nicht entscheiden.'],
                   f'{dz(x)} liegt zwischen {grenzen[quad - 1]} und {grenzen[quad]} ({quad}. Viertel des Einheitskreises). Dort ist {f} {richtig}.',
                   'Vergleiche x mit π/2 ≈ 1,57, π ≈ 3,14 und 3π/2 ≈ 4,71: In welchem Viertel des Einheitskreises liegt der Punkt?')


def g_werte(s):
    # Taschenrechner nur auf Stufe 1–2; Stufe 3: Vorzeichen ohne Rechner und exakte Werte mit Wurzeln
    if s == 1:
        return _werte_einfach(1) if R.random() < 0.6 else _werte_rechner(1)
    if s == 2:
        z = R.random()
        if z < 0.4: return _werte_wurzel(2)
        if z < 0.7: return _werte_einfach(2)
        return _werte_rechner(2)
    return _werte_vorzeichen() if R.random() < 0.6 else _werte_wurzel(3)


def cf_(x):
    x = Fr(x)
    return str(int(x)) if x.denominator == 1 else str(float(x)) if endlich(x) else f'({x.numerator}/{x.denominator})'


def g_periode(s):
    b = R.choice([2, 3, 4, 5, 6, Fr(1, 2), Fr(1, 3), Fr(3, 2)])
    f = R.choice(['sin', 'cos'])
    p = Fr(360) / b
    if s == 1:
        return zahl(f'Welche Periode (in Grad) hat f(x) = {fterm(f, b=b)}?', f'p = 360° : {dz(b) if endlich(b) else br(b)} = {dz(p)}°.', 'Periode = 360° geteilt durch den Faktor vor x.', p,
                    f'360 / {cf_(b)}', einheit='°')
    if s == 2:
        if R.random() < 0.5:
            q = Fr(2) / b
            return pi_luecke(f'Welche Periode hat f(x) = {fterm(f, b=b)} im Bogenmaß? Gib sie als Vielfaches von π an.', q,
                             f'p = 2π : {dz(b) if endlich(b) else br(b)} = {pi_text(q)}.', 'Periode = 2π geteilt durch b.')
        if b < 1 or not endlich(b): return None
        return mit_grafik(zahl(f'Der Graph zeigt f(x) = {f}(b · x) für 0° ≤ x ≤ 360°. Lies die Periode ab und bestimme b.',
                               f'Eine Schwingung dauert {dz(p)}°, also b = 360° : {dz(p)}° = {dz(b)}.', 'Miss die Länge einer vollen Schwingung (z. B. von Maximum zu Maximum).',
                               b, f'360 / {cf_(p)}'), bild([graph(f, b=b)], x=(0, 360), y=(-1.5, 1.5)) | {'schritt_y': 0.5})
    pg = R.choice([90, 120, 180, 240, 720, 60])
    b = Fr(360, pg)
    if R.random() < 0.5:
        return zahl(f'Eine Sinusfunktion f(x) = sin(b · x) soll die Periode {pg}° haben. Bestimme b.', f'b = 360° : {pg}° = {dz(b) if endlich(b) else br(b)}.',
                    'Stelle p = 360° : b nach b um.', b, f'360 / {pg}') if endlich(b) else None
    return auswahl(f'Jemand sagt: „f(x) = sin({dz(b) if endlich(b) else br(b)}x) hat die Periode {dz(360 * b) if endlich(360 * b) else br(360 * b)}°.“ Was stimmt?',
                   f'Falsch: p = 360° : {dz(b) if endlich(b) else br(b)} = {pg}°.', ['Richtig.', f'Falsch: p = {dz(b) if endlich(b) else br(b)}°.', 'Falsch: p = 360°, der Faktor ändert die Periode nicht.'],
                   f'Je größer b, desto schneller die Schwingung und desto kürzer die Periode: p = 360° : b = {pg}°.', 'Wird die Periode durch b länger oder kürzer?')


def g_parameter(s):
    if s == 3 and R.random() < 0.4:
        # Term aus Kennwerten aufstellen
        a, b, d = R.randint(1, 4), R.choice([1, 2, 3, 4]), R.randint(-3, 4)
        M, m, p = d + a, d - a, 360 // b
        return luecken(f'Eine Funktion f(x) = a · sin(b · x) + d (a > 0, b > 0, x in Grad) hat den größten Wert {dz(M)}, den kleinsten Wert {dz(m)} und die Periode {p}°. Bestimme a, b und d.',
                       'f(x) = □ · sin(□ · x) + □', 'a, b und d (d auch negativ)', [a, b, d],
                       f'd = ({dz(M)} + {kl(m)}) : 2 = {dz(d)}; a = ({dz(M)} − {kl(m)}) : 2 = {a}; b = 360° : {p}° = {b}. Also f(x) = {fterm("sin", a, b, d)}.',
                       'Die Mittellinie liegt in der Mitte zwischen größtem und kleinstem Wert; die Amplitude ist der halbe Abstand.',
                       c=[f'({M} - ({m})) / 2', f'360 / {p}', f'({M} + ({m})) / 2'])
    a = R.choice([2, 3, 4, Fr(1, 2), Fr(3, 2), 5])
    d = R.randint(-3, 3)
    f = R.choice(['sin', 'cos'])
    neg = s == 3 and R.random() < 0.5
    aa = -a if neg else a
    lo, hi = d - a, d + a
    if s == 1:
        return zahl(f'Welche Amplitude hat f(x) = {fterm(f, a=aa, d=d)}?', f'Amplitude = |a| = {dz(a)}.', 'Die Amplitude ist der Faktor vor sin bzw. cos (Betrag).', a,
                    f'abs({cf_(aa)})')
    if s == 2 and R.random() < 0.5:
        return mit_grafik(zahl(f'Der Graph zeigt f(x) = a · {f}(x) + d mit a > 0. Lies die Amplitude a ab.', f'Mittellinie y = {dz(d)}, Maximum {dz(hi)}: a = {dz(hi)} − {kl(d)} = {dz(a)}.',
                               'Abstand vom Maximum zur Mittellinie (oder halber Abstand von Maximum zu Minimum).', a, f'({cf_(hi)} - {cf_(lo)}) / 2'),
                          bild([graph(f, a=a, d=d)], x=(0, 360)))
    if Fr(lo).denominator != 1 or Fr(hi).denominator != 1:
        return zahl(f'Welchen größten Wert nimmt f(x) = {fterm(f, a=aa, d=d)} an?', f'Maximum = d + |a| = {dz(d)} + {dz(a)} = {dz(hi)}.',
                    'Der größte Wert liegt eine Amplitude über der Mittellinie.', hi, f'{d} + abs({cf_(aa)})')
    return luecken(f'Gib die Wertemenge von f(x) = {fterm(f, a=aa, d=d)} an.', 'W = [□; □]', 'kleinster und größter Wert', [lo, hi],
                   f'Mittellinie y = {dz(d)}, Amplitude {dz(a)}: W = [{dz(lo)}; {dz(hi)}].', 'Von der Mittellinie aus eine Amplitude nach unten und nach oben.',
                   c=[f'{d} - abs({cf_(aa)})', f'{d} + abs({cf_(aa)})'])


# ---------- Graph und Term zuordnen ----------
# Darstellung einer Funktion: (art, a, b, d, cg) für a · art(b · x + cg°) + d
S1_GRAPHEN = [('sin', 3, 1, 0, 0), ('cos', 2, 1, 0, 0), ('sin', 1, 1, 2, 0), ('sin', -2, 1, 0, 0), ('cos', 1, 1, -1, 0), ('cos', Fr(3, 2), 1, 0, 0)]
_GESEHEN = {}


def zterm(t):
    art, a, b, d, cg = t
    af = '' if a == 1 else '−' if a == -1 else (dz(a) if endlich(Fr(a)) else br(a)) + ' · '
    bx = 'x' if b == 1 else f'{dz(b)}x' if endlich(Fr(b)) else f'({br(b)})x'
    innen = bx + (f' {plus(cg)}°' if cg else '')
    s_ = f'f(x) = {af}{art}({innen})'
    if d: s_ += f' {plus(d)}'
    return s_


def zwert(t, x):
    art, a, b, d, cg = t
    u = math.radians(float(b) * x + cg)
    return float(a) * (math.sin(u) if art == 'sin' else math.cos(u)) + float(d)


def gleich(t1, t2):
    return all(abs(zwert(t1, x) - zwert(t2, x)) < 1e-9 for x in range(0, 721, 15))


def zgraph(t):
    art, a, b, d, cg = t
    return {'art': art, 'a': zahlwert_json(a), 'b': zahlwert_json(b), 'c': math.radians(cg), 'd': zahlwert_json(d)}


def g_zuordnen(s):
    pool, nr = AKT['pool'], AKT['nr']
    if s == 1 and pool == 'uebung':
        t = S1_GRAPHEN[nr % len(S1_GRAPHEN)]
    elif s == 3 and R.random() < 0.45:
        # Verschiebung in x-Richtung
        t = (R.choice(['sin', 'cos']), R.choice([1, 2, 3]), 1, R.choice([0, 0, 1, -1]), R.choice([90, -90, 45, -45, 60, -60]))
    else:
        f = R.choice(['sin', 'cos'])
        a = R.choice([1, 2, 3]) if s < 3 else R.choice([1, 2, 3, -1, -2])
        b = R.choice([1, 2, Fr(1, 2)]) if s > 1 else 1
        d = 0 if s == 1 else R.choice([0, 0, 1, -1, 2])
        if s == 1 and a == 1: a = R.choice([2, 3])
        t = (f, a, b, d, 0)
    # Regel: innerhalb einer Stufe keinen Graphen doppelt
    schon = _GESEHEN.setdefault(s, [])
    if any(gleich(t, u) for u in schon): return None
    f, a, b, d, cg = t
    anders = 'cos' if f == 'sin' else 'sin'
    if cg:
        kand = [(f, a, 1, d, -cg), (anders, a, 1, d, 0), (f, a, 2, d, cg), (f, a, 1, cg, 0), (f, -a, 1, d, 0), (f, a, 1, d, 0)]
    else:
        kand = [(anders, a, b, d, 0), (f, b if isinstance(b, int) and b != a else a + 1, a if isinstance(b, int) and b != a else b, d, 0),
                (f, a, b, -d, 0) if d else (f, a, b, a, 0), (f, -a, b, d, 0)]
    R.shuffle(kand)
    # Regel: Optionen, die zum selben Graphen führen, nie gemeinsam anbieten
    gewaehlt = []
    for k in kand:
        if gleich(k, t) or any(gleich(k, g_) for g_ in gewaehlt): continue
        gewaehlt.append(k)
    if len(gewaehlt) < 3: return None
    p = Fr(360) / b
    if cg:
        start = f'Der Graph ist gegenüber {"a · " if a != 1 else ""}{f}(x) um {abs(cg)}° nach {"links" if cg > 0 else "rechts"} verschoben'
        w = f'Mittellinie y = {dz(d)}, Amplitude {abs(a)}, Periode 360°. {start}: {zterm(t)}.'
        if f == 'sin' and abs(cg) == 90:
            w += f' (Gleichwertig: {"cos x" if cg > 0 else "−cos x"}{" mit Faktor " + str(a) if a != 1 else ""} – diese Schreibweise steht deshalb nicht zur Auswahl.)'
    else:
        w = (f'Mittellinie y = {dz(d)}, Amplitude {abs(a)}, Periode {dz(p)}° (b = {dz(b)}), Start bei x = 0 '
             f'{"auf der Mittellinie" if f == "sin" else "im Maximum" if a > 0 else "im Minimum"}{" fallend" if f == "sin" and a < 0 else ""}: {zterm(t)}.')
    a_ = auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen (x in Grad)?', zterm(t), [zterm(k) for k in gewaehlt], w,
                 'Lies Mittellinie, Amplitude und Periode ab. Wo beginnt der Graph bei x = 0 – und ist er gegenüber sin bzw. cos verschoben?')
    if a_ is None: return None
    schon.append(t)
    return mit_grafik(a_, bild([zgraph(t)], x=(0, 360)))


def g_eigenschaften(s):
    if s == 2 and R.random() < 0.3: return g_eigenschaften(3)
    f = R.choice(['sin', 'cos'])
    if s == 1:
        k0 = R.choice([-720, -360, 0, 360])
        nst = [k0, k0 + 180, k0 + 360] if f == 'sin' else [k0 + 90, k0 + 270]
        return luecken(f'Gib alle Nullstellen von f(x) = {f} x im Bereich {dz(k0)}° ≤ x ≤ {dz(k0 + 360)}° an (in Grad).', '; '.join(f'x{"₁₂₃"[i]} = □°' for i in range(len(nst))),
                       'kleinste zuerst', nst, f'{f} x = 0, wo der Punkt am Einheitskreis {"auf der x-Achse" if f == "sin" else "auf der y-Achse"} liegt: ' + ', '.join(f'{dz(v)}°' for v in nst) + '.',
                       'Wo hat der Punkt am Einheitskreis die Koordinate 0? Die Nullstellen wiederholen sich alle 180°.', c=[str(v) for v in nst])
    if s == 2:
        typ = R.random()
        if typ < 0.4:
            return auswahl(f'Welche Symmetrie hat der Graph von f(x) = {f} x?', 'punktsymmetrisch zum Ursprung' if f == 'sin' else 'achsensymmetrisch zur y-Achse',
                           ['punktsymmetrisch zum Ursprung', 'achsensymmetrisch zur y-Achse', 'keine Symmetrie'],
                           'sin(−x) = −sin x (punktsymmetrisch), cos(−x) = cos x (achsensymmetrisch).', 'Vergleiche f(−x) mit f(x).')
        k = R.randint(-2, 3)
        if f == 'sin':
            xm = 90 + 360 * k
            return zahl(f'An welcher Stelle x zwischen {dz(360 * k)}° und {dz(360 * (k + 1))}° hat sin x ein Maximum?', f'sin x = 1 bei 90° + ({dz(360 * k)}°) = {dz(xm)}° (Periode 360°).',
                        'sin x ist bei 90° maximal; addiere Vielfache der Periode.', xm, f'90 + 360 * ({k})', einheit='°')
        xm = 180 + 360 * k
        return zahl(f'An welcher Stelle x zwischen {dz(360 * k)}° und {dz(360 * (k + 1))}° hat cos x ein Minimum?', f'cos x = −1 bei 180° + ({dz(360 * k)}°) = {dz(xm)}°.',
                    'cos x ist bei 180° minimal; addiere Vielfache der Periode.', xm, f'180 + 360 * ({k})', einheit='°')
    typ = R.random()
    if typ < 0.5:
        sh = R.choice([90, -270, 450])
        return mit_grafik(auswahl(f'Der Graph von cos x entsteht aus dem von sin x durch eine Verschiebung. Welche Aussage ist richtig? (Gezeichnet: sin und cos.)',
                                  'cos x = sin(x + 90°)', ['cos x = sin(x − 90°)', 'cos x = sin x + 1', 'cos x = −sin x'],
                                  'Der cos-Graph ist der sin-Graph um 90° nach links verschoben: cos x = sin(x + 90°). Probe: x = 0: sin 90° = 1 = cos 0°.',
                                  'Setze x = 0 in jede Aussage ein und vergleiche mit cos 0° = 1.'),
                          bild([graph('sin', name='sin'), graph('cos', name='cos', name_x=150)], x=(-180, 360), y=(-1.5, 1.5)) | {'schritt_y': 0.5})
    b = R.choice([2, 3, 4, 5, 6])
    p = 360 // b
    if typ < 0.75:
        f = R.choice(['sin', 'cos'])
        z = Fr(180, b) if f == 'sin' else Fr(90, b)
        return zahl(f'Bestimme die kleinste positive Nullstelle von f(x) = {f}({b}x) (in Grad).',
                    f'{f}(u) = 0 zuerst bei u = {"180°" if f == "sin" else "90°"}; {b}x = {"180°" if f == "sin" else "90°"} ⇒ x = {dz(z)}°.',
                    'Setze u = ' + str(b) + 'x und suche die erste Nullstelle von ' + f + '(u).', z, f'{180 if f == "sin" else 90} / {b}', einheit='°')
    return zahl(f'Wie viele Nullstellen hat f(x) = sin({b}x) im Bereich 0° ≤ x < 360°?', f'Periode {p}°; Nullstellen alle {p // 2}°: 0°, {p // 2}°, …, also {2 * b} Stück.',
                'Wie viele halbe Perioden passen in 360°?', 2 * b, f'360 // ({p} // 2)')


def _gezeiten(s):
    """Wasserstand im Hafen: W(t) = m + s · sin(360°/12,4 · t)."""
    m, sw = R.choice([(2, Fr(3, 2)), (3, 2), (Fr(5, 2), 1), (4, Fr(5, 2)), (3, Fr(3, 2))])
    term = f'W(t) = {dz(m)} + {dz(sw) + " · " if sw != 1 else ""}sin(360°/12,4 · t)'
    satz = f'Der Wasserstand in einem Hafen wird beschrieben durch {term} (t in Stunden nach Mitternacht, W in m).'
    if s == 2:
        frage = R.choice(['hoch', 'tief', 'T'])
        if frage == 'hoch':
            return zahl(f'{satz} Wie hoch steht das Wasser bei Flut höchstens?', f'Größter Wert: {dz(m)} + {dz(sw)} = {dz(m + sw)} m (sin = 1).',
                        'Wann ist der Sinus am größten?', m + sw, f'{cf_(m)} + {cf_(sw)}', einheit='m')
        if frage == 'tief':
            return zahl(f'{satz} Wie hoch steht das Wasser bei Ebbe?', f'Kleinster Wert: {dz(m)} − {dz(sw)} = {dz(m - sw)} m (sin = −1).',
                        'Wann ist der Sinus am kleinsten?', m - sw, f'{cf_(m)} - {cf_(sw)}', einheit='m')
        return zahl(f'{satz} Nach wie vielen Stunden wiederholt sich der Wasserstand?', 'Periode = 360° : (360°/12,4) = 12,4 h.',
                    'Periode = 360° : b.', Fr(124, 10), '360 / (360 / 12.4)', einheit='h')
    t = R.randint(1, 11)
    w = float(m) + float(sw) * math.sin(math.radians(360 / 12.4 * t))
    v = gerundet(w, 1)
    if v is None: return None
    return zahl(f'{satz} Wie hoch steht das Wasser um {t} Uhr? Runde auf eine Nachkommastelle.',
                f'W({t}) = {dz(m)} + {dz(sw)} · sin({dz(round(360 / 12.4 * t, 1))}°) ≈ {dz(v)} m.', 'Setze t ein; Taschenrechner im Gradmodus.',
                v, f'round({K(w)}, 1)', einheit='m', tol=0.1)


def _riesenrad_modell():
    """Modell aus Sachangaben: h(t) = d − a · cos(b° · t)."""
    D = R.choice([20, 24, 30, 36, 40, 50, 60, 70, 80])
    tief = R.choice([1, 2, 3])
    T = R.choice([10, 12, 15, 18, 20, 24, 30, 36, 40])
    a, d, b = D // 2, D // 2 + tief, 360 // T
    return luecken(f'Ein Riesenrad hat den Durchmesser {D} m. Der tiefste Punkt einer Gondel liegt {tief} m über dem Boden, eine Umdrehung dauert {T} min. '
                   f'Die Gondel startet unten. Stelle die Höhe h(t) (t in Minuten) auf.', 'h(t) = □ − □ · cos(□° · t)', 'Mittelhöhe, Radius, Winkel pro Minute',
                   [d, a, b], f'Radius a = {D} : 2 = {a} m; Mittelhöhe d = {a} + {tief} = {d} m; b = 360° : {T} = {b}° pro Minute. Also h(t) = {d} − {a} · cos({b}° · t).',
                   'Die Mitte des Rads liegt einen Radius über dem tiefsten Punkt. In der Umlaufzeit dreht sich das Rad um 360°.',
                   c=[f'{D} // 2 + {tief}', f'{D} // 2', f'360 // {T}'])


def _riesenrad_zeitpunkt():
    """Zeitpunkt bestimmen: d − a · cos(b t) = Ziel mit cos-Wert aus der Tabelle."""
    T = R.choice([8, 12, 16, 20, 24, 30, 36, 40])
    a = R.choice([10, 12, 16, 18, 20, 24, 25, 30])
    d = a + R.choice([1, 2, 3])
    k, winkel = R.choice([(Fr(-1, 2), 120), (0, 90), (Fr(1, 2), 60), (-1, 180)])
    ziel = d - a * k
    b = Fr(360, T)
    t = Fr(winkel) / b
    if not endlich(ziel) or not endlich(t) or not endlich(b): return None
    return zahl(f'Die Höhe einer Riesenradgondel ist h(t) = {d} − {a} · cos({dz(b)}° · t) (t in min, h in m). Nach wie vielen Minuten ist die Gondel zum ersten Mal {dz(ziel)} m hoch?',
                f'{d} − {a} · cos({dz(b)}° · t) = {dz(ziel)} ⇒ cos({dz(b)}° · t) = {dz(k)} ⇒ {dz(b)}° · t = {winkel}° (erster Winkel) ⇒ t = {winkel} : {dz(b)} = {dz(t)} min.',
                'Stelle nach cos(…) um. Für welchen Winkel zwischen 0° und 180° hat cos diesen Wert?', t, f'{winkel} / {cf_(b)}', einheit='min')


def g_anwendung(s):
    if s == 1:
        d, a, T = R.choice([(20, 18, 12), (30, 25, 20), (15, 12, 8), (60, 55, 30), (10, 8, 6)])
        t = R.choice([0, T // 2, T // 4, 3 * T // 4, T])
        h = d - a * round(math.cos(math.radians(360 / T * t)))
        return zahl(f'Die Höhe einer Riesenradgondel ist h(t) = {d} − {a} · cos({dz(Fr(360, T))}° · t) (t in Minuten, h in m). Wie hoch ist sie nach {t} min?',
                    f'h({t}) = {d} − {a} · cos({dz(Fr(360, T) * t)}°) = {dz(h)} m.', 'Setze t ein; cos 0° = 1, cos 90° = 0, cos 180° = −1.', h,
                    f'{d} - {a} * {round(math.cos(math.radians(360 / T * t)))}', einheit='m')
    if s == 2:
        if R.random() < 0.4:
            return _gezeiten(2)
        d, a, T = R.choice([(20, 18, 12), (30, 25, 20), (15, 12, 8), (60, 55, 30), (10, 8, 6), (40, 35, 15)])
        frage = R.choice(['max', 'min', 'T'])
        if frage == 'max':
            return zahl(f'h(t) = {d} − {a} · cos({dz(Fr(360, T))}° · t) beschreibt die Höhe einer Gondel (h in m). Welche größte Höhe erreicht sie?',
                        f'Größte Höhe = {d} + {a} = {d + a} m (cos = −1).', 'Wann ist −cos am größten?', d + a, f'{d} + {a}', einheit='m')
        if frage == 'min':
            return zahl(f'h(t) = {d} − {a} · cos({dz(Fr(360, T))}° · t) beschreibt die Höhe einer Gondel (h in m). Welche kleinste Höhe hat sie?',
                        f'Kleinste Höhe = {d} − {a} = {d - a} m (cos = 1).', 'Wann ist −cos am kleinsten?', d - a, f'{d} - {a}', einheit='m')
        return zahl(f'h(t) = {d} − {a} · cos({dz(Fr(360, T))}° · t) (t in Minuten). Wie lange dauert eine Umdrehung?',
                    f'Periode = 360° : {dz(Fr(360, T))}° = {T} min.', 'Periode = 360° : b.', T, f'360 / {cf_(Fr(360, T))}', einheit='min')
    typ = R.random()
    if typ < 0.25:
        return _riesenrad_modell()
    if typ < 0.5:
        return _riesenrad_zeitpunkt()
    if typ < 0.65:
        return _gezeiten(3)
    if typ < 0.82:
        d, a, T = R.choice([(12, 4, 365), (12, Fr(9, 2), 365), (12, Fr(7, 2), 365)])
        t = R.randint(1, 364)
        w = float(d) + float(a) * math.sin(math.radians(360 / 365 * (t - 80)))
        v = gerundet(w, 1)
        if v is None: return None
        return zahl(f'Die Tageslänge an einem Ort wird modelliert durch L(t) = {d} + {dz(a)} · sin(360°/365 · (t − 80)) (t = Tag des Jahres, L in Stunden). Wie lang ist der Tag t = {t}? Runde auf eine Nachkommastelle.',
                    f'L({t}) = {d} + {dz(a)} · sin({dz(round(360 / 365 * (t - 80), 2))}°) ≈ {dz(v)} h.', 'Setze t ein; Taschenrechner im Gradmodus.', v,
                    f'round({K(w)}, 1)', einheit='h', tol=0.1)
    d, a, T = R.choice([(20, 18, 12), (30, 25, 20), (15, 12, 8), (40, 35, 15)])
    t = R.randint(1, T - 1)
    w = d - a * math.cos(math.radians(360 / T * t))
    v = gerundet(w, 1)
    if v is None or t * 4 % T == 0: return None
    return mit_grafik(zahl(f'h(t) = {d} − {a} · cos({dz(Fr(360, T))}° · t) beschreibt die Höhe einer Gondel (t in min, h in m). Wie hoch ist sie nach {t} min? Runde auf eine Nachkommastelle.',
                           f'h({t}) = {d} − {a} · cos({dz(Fr(360, T) * t)}°) ≈ {dz(v)} m.', 'Setze t ein (Gradmodus). Der Graph hilft beim Schätzen.', v,
                           f'round({K(w)}, 1)', einheit='m', tol=0.1),
                      koord([{'art': 'cos', 'a': -a, 'b': zahlwert_json(Fr(360, T)), 'd': d, 'bereich': [0, T]}], x=(0, T), y=(0, (d + a) // 5 * 5 + 5),
                            name_x='t', name_y='h', streckung=1.4))



# ---------- KLAR: verständliche Fassung der Lernkarten (Runde 7) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
KLAR = {
 'bogenmass': {
  'einstieg': 'Ein Riesenrad dreht sich. Wie weit es sich gedreht hat, kann man als Winkel in Grad angeben – eine Vierteldrehung sind 90°. '
              'Man kann aber auch messen, wie lang der Weg ist, den eine Gondel auf dem Kreis zurücklegt. Hat der Kreis den Radius 1, '
              'ist dieser Weg bei einer halben Drehung genau π ≈ 3,14 lang. Diese Weglänge heißt ⟦Bogenmaß⟧.',
  'woerter': [['Gradmaß', 'Winkel in Grad: eine ganze Drehung sind 360°'],
              ['Einheitskreis', 'ein Kreis mit dem Radius 1'],
              ['π', 'die Kreiszahl, etwa 3,14; der Einheitskreis hat den Umfang 2π'],
              ['Bogenmaß', 'die Länge des Bogens am Einheitskreis, die zu einem Winkel gehört'],
              ['α', 'griechischer Buchstabe „alpha“, Name für einen Winkel in Grad'],
              ['π/3', 'π geteilt durch 3, etwa 1,05']],
  'schritte': ['Eine ganze Drehung sind 360°, und der ganze Umfang des Einheitskreises ist 2π. Also entsprechen 180° genau π.',
               '60° ist der wievielte Teil von 180°? 60 : 180 = 1/3.',
               'Dann ist auch der Bogen ein Drittel von π: 60° entspricht π/3.',
               'Mit π ≈ 3,14 gerechnet: ⟦60° = π/3 ≈ 1,05⟧.'],
  'regel': 'So rechnest du um: ⟦360° entsprechen 2π⟧, also 180° = π. Von Grad ins Bogenmaß: ⟦x = α · π/180°⟧. Zurück ins Gradmaß: mit 180°/π malnehmen.',
  'fehler': '60° = 60π ist falsch: 60π wären genau 30 ganze Runden des Riesenrads. Man muss durch ⟦180°⟧ teilen: 60 : 180 = 1/3, also π/3.'},
 'werte': {
  'einstieg': 'Stell dir das Riesenrad als Kreis mit dem Radius 1 vor, die Mitte im Ursprung eines Koordinatensystems. '
              'Eine Gondel startet rechts auf Höhe der Mitte und fährt gegen den Uhrzeigersinn. Zu jedem Drehwinkel gehört eine Höhe über der Mitte '
              'und ein Abstand nach rechts oder links. Die Höhe heißt ⟦Sinus⟧ des Winkels, der Abstand nach rechts ⟦Kosinus⟧.',
  'woerter': [['Ursprung', 'der Punkt (0 | 0), hier die Mitte des Rads'],
              ['Koordinate', 'eine der beiden Zahlen eines Punktes: erst x (rechts/links), dann y (oben/unten)'],
              ['sin x', 'Sinus von x: die y-Koordinate (Höhe) des Punktes auf dem Einheitskreis'],
              ['cos x', 'Kosinus von x: die x-Koordinate des Punktes; links von der Mitte ist sie negativ'],
              ['5π/6', '5 · π : 6, das entspricht 150°'],
              ['RAD', 'Taschenrechner-Modus für Winkel im Bogenmaß; DEG ist der Gradmodus']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 1.5],
           'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'sin (Höhe)'}, {'art': 'cos', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'cos', 'name_x': 150}],
           'grad': True, 'schritt_x': 90, 'schritt_y': 0.5, 'streckung': 1.4, 'name_x': 'Winkel'},
  'schritte': ['Gesucht ist sin(5π/6). Zuerst ins Gradmaß umrechnen: 5 · 180° : 6 = 150°.',
               'Bei 150° ist die Gondel links oben. Sie ist genauso hoch wie bei 30°, nur auf der anderen Seite, also sin 150° = sin 30°.',
               'Bei 30° ist die Höhe genau die Hälfte des Radius: sin 30° = 0,5.',
               'Also ist ⟦sin(5π/6) = 0,5⟧.'],
  'regel': 'So bestimmst du Werte: sin x ist die ⟦y-Koordinate⟧, cos x die ⟦x-Koordinate⟧ des Punktes am Einheitskreis. '
           'Merke sin(π/6) = 0,5, sin(π/2) = 1 und cos(π) = −1. Für das Bogenmaß den Taschenrechner auf ⟦RAD⟧ stellen.',
  'fehler': 'sin(2) im Gradmodus zu berechnen (≈ 0,035) ist falsch, wenn 2 im ⟦Bogenmaß⟧ gemeint ist: Das Rad hätte sich dann nur um 2° gedreht '
            'statt um etwa 115°. Richtig im RAD-Modus: sin(2) ≈ 0,909.'},
 'periode': {
  'einstieg': 'Nach einer vollen Umdrehung ist die Gondel wieder an derselben Stelle, und alles wiederholt sich. Beim Sinus geschieht das nach 360°. '
              'Dreht sich ein Rad dreimal so schnell, ist eine Runde schon nach einem Drittel vorbei. '
              'Die Länge, nach der sich alles wiederholt, heißt ⟦Periode⟧.',
  'woerter': [['Periode p', 'die Länge, nach der sich der Graph wiederholt'],
              ['Schwingung', 'ein Auf und Ab, das sich wiederholt'],
              ['sin(x + 360°) = sin x', 'nach einer vollen Drehung ist der Wert wieder derselbe'],
              ['sin(3x)', 'erst x mal 3 nehmen, dann den Sinus bilden: die Schwingung läuft dreimal so schnell'],
              ['b', 'der Faktor vor x im Sinus']],
  'schritte': ['Gegeben ist f(x) = sin(3x). Der Faktor vor x ist b = 3.',
               'Für eine volle Schwingung muss 3x von 0° bis 360° laufen. Das ist schon geschafft, wenn x = 120° ist.',
               'Die Periode ist also p = 360° : 3 = ⟦120°⟧.',
               'Im Bogenmaß gerechnet: 2π : 3 = 2π/3.'],
  'regel': 'So berechnest du die Periode: sin und cos wiederholen sich nach ⟦360° = 2π⟧. Bei f(x) = sin(b · x) ist die ⟦Periode p = 360° : b⟧ '
           '(im Bogenmaß 2π : b).',
  'fehler': 'Bei sin(3x) die Periode 3 · 360° = 1 080° anzunehmen ist falsch: Der Faktor 3 macht die Schwingung ⟦schneller⟧ – wie ein Rad, '
            'das sich dreimal so schnell dreht. Die Periode wird ⟦kürzer⟧: 120°.'},
 'parameter': {
  'einstieg': 'An einer Hafenmauer ist eine Markierung. Bei Flut steht das Wasser 4 m über der Markierung, bei Ebbe 2 m darunter. '
              'Der mittlere Wasserstand liegt also 1 m über der Markierung, und das Wasser steigt und fällt um 3 m. '
              'Diese Schwankung um die Mitte heißt ⟦Amplitude⟧.',
  'woerter': [['f(x) = a · sin(b · x) + d', 'die allgemeine Form; a, b und d sind feste Zahlen'],
              ['Amplitude |a|', 'wie weit es von der Mitte nach oben (und nach unten) geht, hier 3'],
              ['|a|', 'Betrag von a: die Zahl ohne Minuszeichen'],
              ['Mittellinie y = d', 'die waagrechte Linie in der Mitte zwischen höchstem und tiefstem Wert, hier y = 1'],
              ['Maximum, Minimum', 'der größte und der kleinste Wert'],
              ['Wertemenge [−2; 4]', 'alle Werte von −2 bis 4, beide Grenzen eingeschlossen']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-3, 5],
           'graphen': [{'art': 'sin', 'a': 3, 'b': 1, 'c': 0.0, 'd': 1, 'name': '3 sin x + 1'}, {'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'sin x', 'name_x': 200}],
           'grad': True, 'schritt_x': 90, 'schritt_y': 1, 'streckung': 1.4, 'waagrecht': [1]},
  'schritte': ['Gegeben ist f(x) = 3 · sin x + 1. Der Sinus allein schwankt zwischen −1 und 1.',
               'Mal 3 genommen schwankt 3 · sin x zwischen −3 und 3. Die Amplitude ist also 3.',
               'Die „+ 1“ schiebt alles um 1 nach oben. Die Mittellinie ist y = 1.',
               'Die Werte liegen zwischen 1 − 3 und 1 + 3: Wertemenge ⟦[−2; 4]⟧, Maximum 4, Minimum −2.'],
  'regel': 'So liest du die Parameter von f(x) = a · sin(b · x) + d: ⟦|a| ist die Amplitude⟧, ⟦d verschiebt nach oben oder unten⟧ (Mittellinie y = d). '
           'Die Wertemenge ist ⟦[d − |a|; d + |a|]⟧.',
  'fehler': 'Bei f(x) = 3 sin x + 1 die Wertemenge [−3; 3] anzugeben ist falsch: Das hieße, das Wasser schwankt um die Markierung herum. '
            'Die Mittellinie liegt aber ⟦1 höher⟧, also [−2; 4].'},
 'zuordnen': {
  'einstieg': 'Ein Messgerät im Hafen zeichnet den Wasserstand als Kurve auf. Aus der Kurve kann man die Rechenvorschrift zurückgewinnen: '
              'Wo liegt die Mitte? Wie weit geht es nach oben? Wie lange dauert ein Auf und Ab? Und wo beginnt die Kurve? '
              'Diese Rechenvorschrift heißt ⟦Funktionsterm⟧.',
  'woerter': [['Funktionsterm', 'die Rechenvorschrift, z. B. 2 · sin(2x)'],
              ['Mittellinie', 'waagrechte Linie in der Mitte zwischen höchstem und tiefstem Punkt; sie liefert d'],
              ['Amplitude', 'Abstand vom höchsten Punkt zur Mittellinie; er liefert |a|'],
              ['Periode p', 'die Länge einer vollen Schwingung; sie liefert b = 360° : p'],
              ['sin oder cos', 'sin startet bei x = 0 auf der Mittellinie und steigt, cos startet im höchsten Punkt']],
  'schritte': ['Die Kurve schwankt um y = 0. Die Mittellinie ist also y = 0, und d = 0.',
               'Der höchste Punkt liegt bei 2. Die Amplitude ist also a = 2.',
               'Eine volle Schwingung reicht von 0° bis 180°. Also ist p = 180° und b = 360° : 180° = 2.',
               'Bei x = 0 startet die Kurve auf der Mittellinie und steigt – das passt zu sin: ⟦f(x) = 2 · sin(2x)⟧.'],
  'regel': 'So findest du den Term: ⟦Mittellinie⟧ ablesen (d), ⟦Abstand Maximum–Mittellinie⟧ (|a|), ⟦Länge einer Schwingung⟧ (p, dann b = 360° : p). '
           'Start auf der Mittellinie steigend: sin. Start im Maximum: cos.',
  'fehler': 'Die Periode 180° als b = 180 einzusetzen ist falsch: sin(180x) würde auf diesen 180° ganze 90 Schwingungen machen. '
            'Richtig ist ⟦b = 360° : p⟧ = 2.'},
 'eigenschaften': {
  'einstieg': 'Wann ist die Gondel genau auf Höhe der Radmitte? Beim Start (0°), nach einer halben Drehung (180°) und nach einer ganzen (360°). '
              'Und wann ist sie genau senkrecht über oder unter der Mitte? Bei 90° und bei 270°. '
              'Stellen, an denen sin oder cos den Wert 0 hat, heißen ⟦Nullstellen⟧.',
  'woerter': [['Nullstelle', 'ein Winkel, bei dem der Wert 0 ist'],
              ['k · 180°', 'alle Vielfachen von 180°: 0°, 180°, 360°, … (k ist eine ganze Zahl)'],
              ['punktsymmetrisch zum Ursprung', 'dreht man den Graphen um (0 | 0) eine halbe Drehung, sieht er gleich aus'],
              ['achsensymmetrisch zur y-Achse', 'spiegelt man den Graphen an der y-Achse, sieht er gleich aus'],
              ['cos x = sin(x + 90°)', 'der cos-Graph ist der sin-Graph, um 90° nach links geschoben']],
  'schritte': ['Gesucht sind die Nullstellen von cos x zwischen 0° und 360°. cos x ist der Abstand nach rechts oder links von der Mitte.',
               'Dieser Abstand ist 0, wenn die Gondel genau senkrecht über oder unter der Mitte steht.',
               'Das ist nach einer Vierteldrehung (90°) und nach einer Dreivierteldrehung (270°) der Fall.',
               'Also hat cos x die Nullstellen ⟦90° und 270°⟧.'],
  'regel': 'Merke die Nullstellen: sin x bei ⟦0°, 180°, 360°, …⟧ (k · 180°), cos x bei ⟦90°, 270°, …⟧. Der sin-Graph ist ⟦punktsymmetrisch⟧ zum Ursprung, '
           'der cos-Graph ⟦achsensymmetrisch⟧ zur y-Achse. Es gilt cos x = sin(x + 90°).',
  'fehler': '„cos x hat bei 0° eine Nullstelle“ ist falsch: Beim Start ist die Gondel ganz rechts, so weit wie möglich von der Mitte weg: cos 0° = ⟦1⟧ (Maximum). '
            'Die Nullstelle bei 0° hat sin x.'},
 'anwendung': {
  'einstieg': 'Jetzt ein echtes Riesenrad: Die Mitte liegt 20 m über dem Boden, der Radius ist 18 m, und eine Umdrehung dauert 12 Minuten. '
              'Eine Gondel steigt unten ein, 2 m über dem Boden. Nach 6 Minuten ist sie ganz oben in 38 m Höhe, nach 12 Minuten wieder unten. '
              'Vorgänge, die sich so immer wiederholen, heißen ⟦periodisch⟧.',
  'woerter': [['periodisch', 'wiederholt sich in gleichen Zeitabständen'],
              ['h(t)', 'Höhe der Gondel in m nach t Minuten'],
              ['30° · t', 'Drehwinkel nach t Minuten: 360° : 12 min = 30° pro Minute'],
              ['20 − 18 · cos(…)', 'das Minus sorgt dafür, dass die Gondel unten startet'],
              ['Mittelwert d', 'die Höhe der Radmitte, 20 m'],
              ['halbe Schwankung |a|', 'der Radius, 18 m'],
              ['Periodendauer', 'die Zeit für eine volle Wiederholung, hier 12 Minuten']],
  'bild': {'typ': 'koordinaten', 'x': [0, 24], 'y': [0, 40], 'graphen': [{'art': 'cos', 'a': -18, 'b': 30, 'd': 20, 'bereich': [0, 24]}],
           'punkte': [{'x': 4, 'y': 29, 'name': '(4 | 29)'}], 'schritt_x': 2, 'schritt_y': 5, 'name_x': 't (min)', 'name_y': 'h (m)', 'streckung': 1.4},
  'schritte': ['Pro Minute dreht sich das Rad um 360° : 12 = 30°. Nach t Minuten ist der Drehwinkel 30° · t.',
               'Die Gondel startet unten, deshalb h(t) = 20 − 18 · cos(30° · t). Probe beim Start: h(0) = 20 − 18 · 1 = 2.',
               'Nach 4 Minuten ist der Drehwinkel 120°, und cos 120° = −0,5.',
               'Also ist h(4) = 20 − 18 · (−0,5) = 20 + 9 = ⟦29 m⟧.'],
  'regel': 'So beschreibst du periodische Vorgänge: ⟦h(t) = a · sin(b · t) + d⟧ (oder mit cos). d = Mittelwert, |a| = halbe Schwankung, '
           '⟦b = 360° : Periodendauer⟧.',
  'fehler': 'b = 12 zu nehmen ist falsch: Dann würde sich das Rad nur um 12° pro Minute drehen und bräuchte 30 Minuten für eine Runde. '
            'In 12 min läuft der Winkel um ⟦360°⟧, also b = 360° : 12 = 30° pro Minute.'},
}

GEN = schoen({'bogenmass': g_bogenmass, 'werte': g_werte, 'periode': g_periode, 'parameter': g_parameter, 'zuordnen': g_zuordnen,
              'eigenschaften': g_eigenschaften, 'anwendung': g_anwendung})

if __name__ == '__main__':
    bauen('funktionen.trig',
          'Sinus- und Kosinusfunktion mit Grad- und Bogenmaß beschreiben, Periode, Amplitude und Verschiebung deuten, Graph und Term zuordnen und periodische Vorgänge modellieren.',
          ['360° = 2π; x = α · π/180°.', 'sin und cos haben die Periode 360° = 2π; sin(b · x) hat die Periode 360° : b.',
           'f(x) = a · sin(b · x) + d: Amplitude |a|, Mittellinie y = d, Wertemenge [d − |a|; d + |a|].', 'sin: Nullstellen k · 180°, punktsymmetrisch; cos: Nullstellen 90° + k · 180°, achsensymmetrisch.'],
          [('Bogenmaß und Werte', ['bogenmass', 'werte']), ('Parameter', ['periode', 'parameter', 'zuordnen']), ('Eigenschaften und Anwendung', ['eigenschaften', 'anwendung'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'bogenmass': ['Gib 60° im Bogenmaß'], 'werte': ['sin(5π/6)'], 'periode': ['f(x) = sin(3x)?'], 'parameter': ['f(x) = 3 · sin(x) + 1'],
                  'anwendung': ['h(t) = 20 − 18 · cos(30° · t) (t in Minuten, h in m). Wie hoch ist sie nach 4 min']},
          offen=['Zeichnungen: Graphen in den Lernkarten „werte“, „periode“, „parameter“, „zuordnen“, „eigenschaften“, „anwendung“; Aufgaben „Graph und Term zuordnen“, „Periode ablesen“, „Amplitude ablesen“ zeigen den Graphen. Die x-Achse ist in Grad beschriftet (grad: true), weil π-Beschriftungen nicht möglich sind; Bogenmaß wird über Umrechnung geübt.',
                 'Verschiebung in x-Richtung: nach der Prüfung als Zuordnungsaufgabe mit Zeichnung (Stufe 3, „zuordnen“) aufgenommen; keine eigene Lernkarte.',
                 'Prüfung eingearbeitet (Runde 3): Bogenlänge, exakte Werte mit Wurzeln (½√2, ½√3), Vorzeichen ohne Rechner, Term aus Kennwerten, Verschiebung in x-Richtung, Riesenrad-Modell aus Sachangaben, Zeitpunkt bestimmen, Gezeiten. Ganzzahlige Vielfache von π als „□ · π“. Zuordnen: kein Graph doppelt je Stufe, gleichwertige Terme nie zusammen als Optionen.',
                 'Vorschlag der Prüfung an den Haupt-Chat (App, nicht Inhalt): x-Achse in Vielfachen von π beschriften (π/2, π, 3π/2) – würde „bogenmass“ und „werte“ anschaulicher machen. Bis dahin Gradbeschriftung.',
                 'Rechenausdruck c: Sinus/Kosinus-Werte als 12-stellige Konstanten mit Toleranz.'])
