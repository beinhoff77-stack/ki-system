#!/usr/bin/env python3
"""Thema funktionen.trig – Sinus- und Kosinusfunktion (Klasse 10). Schreibt inhalte/themen/funktionen.trig.json."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403
from _schwer_kl10 import ergaenzen  # noqa: E402

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



# ---------- KLAR: Lernkarten im neuen Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
# Muster: einstieg (≤ 35 Wörter) → Kartenbild → Schritte als {text, bild} (Bildergeschichte) → „Pass auf!“ (fehler + fehler_bild) → MERKE (regel).
_KREIS = {'typ': 'koordinaten', 'x': [-1.5, 1.5], 'y': [-1.5, 1.5], 'kreise': [{'m': [0, 0], 'r': 1}], 'schritt_x': 0.5, 'schritt_y': 0.5}
_GRAD = {'grad': True, 'schritt_x': 90, 'streckung': 1.4}
KLAR = {
 'bogenmass': {
  'einstieg': 'Ein Riesenrad dreht sich. Statt in Grad kann man messen, wie weit eine Gondel auf dem Kreis fährt. '
              'Beim Radius 1 ist eine halbe Drehung π lang: Das ist das ⟦Bogenmaß⟧.',
  'woerter': [['Bogenmaß', 'die Länge des Bogens am Einheitskreis, die zum Winkel gehört'],
              ['Einheitskreis', 'ein Kreis mit dem Radius 1'],
              ['π', 'die Kreiszahl, etwa 3,14']],
  'bild': _KREIS | {'strecken': [[0, 0, 1, 0]]},
  'schritte': [{'text': 'Am Einheitskreis ist der ganze Umfang 2π. Also gehören 180° zu π.'},
               {'text': '60° ist ein Drittel von 180°, denn 60 : 180 = 1/3.',
                'bild': {'strecken': [[0, 0, 1, 0], [0, 0, 0.5, 0.866]], 'punkte': [{'x': 0.5, 'y': 0.866, 'name': '60°'}]}},
               {'text': 'Der Bogen ist dann ein Drittel von π: ⟦60° = π/3⟧ ≈ 1,05.'}],
  'fehler': '60° = 60π ist falsch. Das wären 30 ganze Runden. Man muss durch ⟦180°⟧ teilen: 60 : 180 = 1/3.',
  'regel': '360° entsprechen 2π, also 180° = π. Umrechnen: ⟦Bogenmaß = Grad · π : 180°⟧.'},
 'werte': {
  'einstieg': 'Eine Gondel fährt auf einem Kreis mit Radius 1 um die Mitte. Ihre Höhe über der Mitte heißt ⟦Sinus⟧ des Drehwinkels. '
              'Ihr Abstand nach rechts heißt ⟦Kosinus⟧.',
  'woerter': [['Sinus', 'sin x: die Höhe (y-Koordinate) des Punktes am Kreis'],
              ['Kosinus', 'cos x: der Abstand nach rechts (x-Koordinate); links der Mitte negativ'],
              ['RAD', 'Rechnermodus für das Bogenmaß; DEG ist der Gradmodus']],
  'bild': _KREIS | {'strecken': [[0, 0, 1, 0]]},
  'schritte': [{'text': '5π/6 ist im Gradmaß 5 · 180° : 6 = 150°.'},
               {'text': 'Bei 150° ist die Gondel links oben, so hoch wie bei 30°.',
                'bild': {'punkte': [{'x': -0.866, 'y': 0.5, 'name': '150°'}, {'x': 0.866, 'y': 0.5, 'name': '30°'}],
                         'strecken': [[0, 0, 1, 0], [-0.866, 0, -0.866, 0.5, 'gestrichelt'], [0.866, 0, 0.866, 0.5, 'gestrichelt']]}},
               {'text': 'Bei 30° ist die Höhe genau der halbe Radius: ⟦sin(5π/6) = 0,5⟧.'},
               {'text': 'Der Rechner im RAD-Modus zeigt für sin(5π/6) ebenfalls 0,5.'}],
  'fehler': 'sin(2) im Gradmodus ergibt 0,035. Das wären nur 2°. Gemeint sind 2 im Bogenmaß, etwa 115°. Im ⟦RAD⟧-Modus: sin(2) ≈ 0,909.',
  'fehler_bild': {'punkte': [{'x': -0.416, 'y': 0.909, 'name': '2 (≈ 115°)'}, {'x': 0.999, 'y': 0.035, 'name': '2°'}],
                  'strecken': [[0, 0, 1, 0], [0, 0, -0.416, 0.909]]},
  'regel': 'sin x ist die Höhe, cos x der Abstand nach rechts. Merke ⟦sin(π/6) = 0,5⟧ und cos(π) = −1.'},
 'periode': {
  'einstieg': 'Nach einer vollen Umdrehung ist die Gondel wieder am Start, und alles wiederholt sich. Beim Sinus geschieht das nach 360°. '
              'Dieser Abstand heißt ⟦Periode⟧.',
  'woerter': [['Periode', 'die Länge, nach der sich der Graph wiederholt'],
              ['Schwingung', 'ein Auf und Ab, das sich wiederholt']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-1.5, 1.5], 'schritt_y': 0.5, **_GRAD,
           'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'sin x'}]},
  'schritte': [{'text': 'f(x) = sin(3x): Der Faktor vor x ist b = 3.'},
               {'text': 'Eine Schwingung ist fertig, wenn 3x = 360° ist, also bei x = 120°.',
                'bild': {'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'sin x'},
                                     {'art': 'sin', 'a': 1, 'b': 3, 'c': 0.0, 'd': 0, 'name': 'sin(3x)', 'name_x': 280}], 'senkrecht': [120]}},
               {'text': 'Die Periode ist p = 360° : 3 = ⟦120°⟧, im Bogenmaß 2π/3.'}],
  'fehler': 'Die Periode ist nicht 3 · 360° = 1 080°. Der Faktor 3 macht die Schwingung ⟦schneller⟧, wie ein Rad mit dreifachem Tempo.',
  'regel': 'Bei sin(b · x) gilt: Periode p = 360° : b. Größeres b heißt ⟦kürzere Periode⟧.'},
 'parameter': {
  'einstieg': 'Bei Flut steht das Wasser 4 m über einer Markierung im Hafen. Bei Ebbe steht es 2 m darunter. '
              'Die Mitte liegt 1 m darüber, die Schwankung heißt ⟦Amplitude⟧.',
  'woerter': [['Amplitude', 'wie weit es von der Mitte nach oben und nach unten geht'],
              ['Mittellinie', 'die waagrechte Linie in der Mitte, y = d'],
              ['Wertemenge', 'alle Werte vom kleinsten bis zum größten']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-3, 5], 'schritt_y': 1, **_GRAD,
           'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'sin x', 'name_x': 200}]},
  'schritte': [{'text': 'Gegeben ist 3 · sin x + 1. sin x schwankt von −1 bis 1.'},
               {'text': 'Mal 3 schwankt es von −3 bis 3: Amplitude 3.',
                'bild': {'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'sin x', 'name_x': 200},
                                     {'art': 'sin', 'a': 3, 'b': 1, 'c': 0.0, 'd': 0, 'name': '3 sin x'}]}},
               {'text': 'Plus 1 schiebt alles hoch. Die Mittellinie ist y = 1.',
                'bild': {'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'sin x', 'name_x': 200},
                                     {'art': 'sin', 'a': 3, 'b': 1, 'c': 0.0, 'd': 1, 'name': 'f', 'name_x': 45}], 'waagrecht': [1]}},
               {'text': 'Wertemenge: von 1 − 3 bis 1 + 3, also ⟦[−2; 4]⟧.',
                'bild': {'punkte': [{'x': 90, 'y': 4, 'name': 'größter: 4'}, {'x': 270, 'y': -2, 'name': 'kleinster: −2'}]}}],
  'fehler': 'Die Wertemenge ist nicht [−3; 3]. Das Wasser schwankt nicht um die Markierung, sondern um eine Mitte ⟦1 höher⟧.',
  'fehler_bild': {'punkte': [{'x': 90, 'y': 4, 'name': '4, nicht 3'}, {'x': 270, 'y': -2, 'name': '−2, nicht −3'}]},
  'regel': 'Bei a · sin(b · x) + d ist |a| die Amplitude. d verschiebt nach oben: ⟦Wertemenge [d − |a|; d + |a|]⟧.'},
 'zuordnen': {
  'einstieg': 'Ein Messgerät im Hafen zeichnet den Wasserstand als Kurve auf. Aus der Kurve kann man die Rechenvorschrift zurückgewinnen. '
              'Sie heißt ⟦Funktionsterm⟧.',
  'woerter': [['Funktionsterm', 'die Rechenvorschrift, z. B. 2 · sin(2x)'],
              ['Mittellinie', 'die waagrechte Linie in der Mitte der Kurve'],
              ['Schwingung', 'ein Auf und Ab; ihre Länge ist die Periode']],
  'bild': {'typ': 'koordinaten', 'x': [0, 360], 'y': [-3, 3], 'schritt_y': 1, **_GRAD, 'graphen': [{'art': 'sin', 'a': 2, 'b': 2, 'c': 0.0, 'd': 0}]},
  'schritte': [{'text': 'Die Kurve schwankt um y = 0: Mittellinie y = 0, also d = 0.', 'bild': {'waagrecht': [0]}},
               {'text': 'Der höchste Punkt liegt bei 2: a = 2.', 'bild': {'waagrecht': [0], 'punkte': [{'x': 45, 'y': 2, 'name': '2'}]}},
               {'text': 'Eine Schwingung reicht bis 180°. Also b = 360° : 180° = 2.', 'bild': {'senkrecht': [180]}},
               {'text': 'Start auf der Mittellinie, steigend: Das passt zu sin. ⟦f(x) = 2 · sin(2x)⟧.'}],
  'fehler': 'b = 180 ist falsch. sin(180x) würde auf diesen 180° ganze 90 Schwingungen machen. Richtig ist ⟦b = 360° : p⟧ = 2.',
  'regel': 'Lies Mittellinie, Amplitude und Periode ab. Start auf der Mittellinie: ⟦sin⟧. Start ganz oben: cos.'},
 'eigenschaften': {
  'einstieg': 'Wann steht die Gondel genau senkrecht über oder unter der Radmitte? Dann ist ihr Abstand nach rechts 0. '
              'Solche Stellen heißen ⟦Nullstellen⟧ des Kosinus.',
  'woerter': [['Nullstellen', 'Stellen, an denen der Wert 0 ist'],
              ['achsensymmetrisch', 'an der y-Achse gespiegelt sieht der Graph gleich aus'],
              ['punktsymmetrisch', 'um (0 | 0) halb gedreht sieht der Graph gleich aus']],
  'bild': {'typ': 'koordinaten', 'x': [-360, 360], 'y': [-1.5, 1.5], 'schritt_y': 0.5, **_GRAD,
           'graphen': [{'art': 'cos', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'name': 'cos x', 'name_x': -300}]},
  'schritte': [{'text': 'cos x ist der Abstand der Gondel nach rechts von der Mitte.'},
               {'text': 'Er ist 0, wenn die Gondel genau oben oder unten steht.'},
               {'text': 'Das ist bei 90° und bei 270°: ⟦Nullstellen 90° und 270°⟧.',
                'bild': {'punkte': [{'x': -270, 'y': 0}, {'x': -90, 'y': 0}, {'x': 90, 'y': 0, 'name': '90°'}, {'x': 270, 'y': 0, 'name': '270°'}]}},
               {'text': 'Der cos-Graph ist achsensymmetrisch zur y-Achse, der sin-Graph punktsymmetrisch.'}],
  'fehler': 'cos x hat bei 0° keine Nullstelle. Beim Start ist die Gondel ganz rechts: ⟦cos 0° = 1⟧. Die Nullstelle bei 0° hat sin x.',
  'fehler_bild': {'punkte': [{'x': 0, 'y': 1, 'name': 'cos 0° = 1'}]},
  'regel': 'Nullstellen: sin bei 0°, 180°, 360°; cos bei ⟦90°, 270°⟧. Es gilt cos x = sin(x + 90°).'},
 'anwendung': {
  'einstieg': 'Die Mitte eines Riesenrads ist 20 m hoch, der Radius 18 m. Eine Runde dauert 12 Minuten. Die Gondel startet unten in 2 m Höhe. '
              'Vorgänge, die sich so wiederholen, heißen ⟦periodisch⟧.',
  'woerter': [['periodisch', 'wiederholt sich in gleichen Zeitabständen'],
              ['h(t)', 'die Höhe der Gondel in m nach t Minuten']],
  'bild': {'typ': 'koordinaten', 'x': [0, 24], 'y': [0, 40], 'graphen': [{'art': 'cos', 'a': -18, 'b': 30, 'd': 20, 'bereich': [0, 24]}],
           'schritt_x': 2, 'schritt_y': 5, 'name_x': 'Minuten', 'name_y': 'Höhe', 'streckung': 1.4},
  'schritte': [{'text': 'Pro Minute dreht sich das Rad um 360° : 12 = 30°.'},
               {'text': 'Die Gondel startet unten: h(t) = 20 − 18 · cos(30° · t).', 'bild': {'punkte': [{'x': 0, 'y': 2, 'name': 'Start: 2 m'}]}},
               {'text': 'Nach 4 Minuten ist der Winkel 120°, und cos 120° = −0,5.'},
               {'text': 'h(4) = 20 − 18 · (−0,5) = 20 + 9 = ⟦29 m⟧.',
                'bild': {'punkte': [{'x': 0, 'y': 2, 'name': 'Start: 2 m'}, {'x': 4, 'y': 29, 'name': '4 min: 29 m'}]}}],
  'fehler': 'b = 12 ist falsch. Dann drehte sich das Rad nur 12° pro Minute, eine Runde dauerte 30 Minuten. Richtig ist ⟦b = 30°⟧.',
  'fehler_bild': {'graphen': [{'art': 'cos', 'a': -18, 'b': 30, 'd': 20, 'bereich': [0, 24], 'name': 'b = 30'},
                              {'art': 'cos', 'a': -18, 'b': 12, 'd': 20, 'bereich': [0, 24], 'name': 'b = 12?'}]},
  'regel': 'h(t) = a · sin(b · t) + d beschreibt periodische Vorgänge. d = Mitte, |a| = halbe Schwankung, ⟦b = 360° : Periodendauer⟧.'},
}


# ---------- Fünfzehnte Runde (Zweig nacharbeit): Bogenmaß in den Lernkarten durchgehend mitführen ----------
# Gradmaß bleibt der Einstieg; jede Karte bekommt am Ende einen Schritt im Bogenmaß (Graphen mit π-Achse, "pi": true).
_PI = {'pi': True, 'grad': False, 'schritt_x': round(PI / 2, 6)}
_P = lambda k: round(k * PI, 4)  # noqa: E731  k · π als Zahl für die Zeichnung
KLAR['bogenmass']['schritte'] += [
    {'text': 'Genauso gilt: 90° = π/2, 270° = 3π/2 und 360° = ⟦2π⟧.',
     'bild': {'strecken': [[0, 0, 1, 0]], 'punkte': [{'x': 0, 'y': 1, 'name': 'π/2'}, {'x': -1, 'y': 0, 'name': 'π'}, {'x': 0, 'y': -1, 'name': '3π/2'}]}},
    {'text': 'Ab jetzt steht x meist im Bogenmaß. Die Achse zeigt π/2, π, 3π/2, 2π.',
     'bild': {'x': [0, _P(2)], 'y': [-1.5, 1.5], **_PI, 'schritt_y': 0.5, 'streckung': 1.4, 'kreise': [], 'strecken': [], 'punkte': [],
              'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'bogen': True, 'name': 'sin x'}]}}]
KLAR['periode']['schritte'][2] = {'text': 'Die Periode ist p = 360° : 3 = ⟦120°⟧.'}
KLAR['periode']['schritte'].append(
    {'text': 'Im Bogenmaß: p = 2π : 3 = 2π/3, also ein Drittel von 2π.',
     'bild': {'x': [0, _P(2)], **_PI, 'senkrecht': [_P(Fr(2, 3))],
              'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'bogen': True, 'name': 'sin x'},
                          {'art': 'sin', 'a': 1, 'b': 3, 'c': 0.0, 'd': 0, 'bogen': True, 'name': 'sin(3x)', 'name_x': _P(Fr(14, 9))}]}})
KLAR['periode']['regel'] = 'Periode von sin(b · x): ⟦2π : b⟧ = 360° : b. Größeres b heißt kürzere Periode.'
KLAR['parameter']['schritte'].append(
    {'text': 'Im Bogenmaß: größter Wert 4 bei x = π/2, kleinster −2 bei 3π/2.',
     'bild': {'x': [0, _P(2)], **_PI,
              'graphen': [{'art': 'sin', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'bogen': True, 'name': 'sin x', 'name_x': _P(Fr(10, 9))},
                          {'art': 'sin', 'a': 3, 'b': 1, 'c': 0.0, 'd': 1, 'bogen': True, 'name': 'f', 'name_x': _P(Fr(1, 4))}],
              'punkte': [{'x': _P(Fr(1, 2)), 'y': 4, 'name': 'π/2: 4'}, {'x': _P(Fr(3, 2)), 'y': -2, 'name': '3π/2: −2'}]}})
KLAR['parameter']['fehler_bild'] = {'punkte': [{'x': _P(Fr(1, 2)), 'y': 4, 'name': '4, nicht 3'}, {'x': _P(Fr(3, 2)), 'y': -2, 'name': '−2, nicht −3'}]}
KLAR['zuordnen']['schritte'].append(
    {'text': 'Im Bogenmaß endet die Schwingung bei π: b = 2π : π = 2.',
     'bild': {'x': [0, _P(2)], **_PI, 'graphen': [{'art': 'sin', 'a': 2, 'b': 2, 'c': 0.0, 'd': 0, 'bogen': True}],
              'senkrecht': [_P(1)], 'punkte': []}})
KLAR['zuordnen']['regel'] = 'Lies Mittellinie, Amplitude und Periode ab. Start auf der Mittellinie: ⟦sin⟧. Start ganz oben: cos. b = 2π : p.'
KLAR['eigenschaften']['schritte'].append(
    {'text': 'Im Bogenmaß: cos hat Nullstellen bei π/2 und 3π/2, sin bei 0 und π.',
     'bild': {'x': [_P(-2), _P(2)], **_PI, 'graphen': [{'art': 'cos', 'a': 1, 'b': 1, 'c': 0.0, 'd': 0, 'bogen': True, 'name': 'cos x', 'name_x': _P(Fr(-5, 3))}],
              'punkte': [{'x': _P(Fr(-3, 2)), 'y': 0}, {'x': _P(Fr(-1, 2)), 'y': 0}, {'x': _P(Fr(1, 2)), 'y': 0, 'name': 'π/2'}, {'x': _P(Fr(3, 2)), 'y': 0, 'name': '3π/2'}]}})
KLAR['eigenschaften']['regel'] = 'Nullstellen: sin bei 0, π, 2π; cos bei ⟦π/2, 3π/2⟧ (90°, 270°). Es gilt cos x = sin(x + π/2).'
KLAR['anwendung']['schritte'].append({'text': 'Im Bogenmaß: 30° = π/6, also h(t) = 20 − 18 · cos(π/6 · t).'})
KLAR['anwendung']['regel'] = 'h(t) = a · sin(b · t) + d. Mitte d, halbe Schwankung |a|. ⟦b = 2π : Periodendauer⟧ oder 360° : Periodendauer.'


GEN = schoen({'bogenmass': g_bogenmass, 'werte': g_werte, 'periode': g_periode, 'parameter': g_parameter, 'zuordnen': g_zuordnen,
              'eigenschaften': g_eigenschaften, 'anwendung': g_anwendung})

# ---------- Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH bauen(...) aufgerufen, alte Aufgaben bleiben gleich.
# Vorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Abitur Bayern 2025 Prüfungsteil A (Analysis 1.5: Parameter a, b einer
# trigonometrischen Funktion aus zwei Punkten), Bayerischer Mathematik-Test 10 2025 (Aufgabe 4b: sin(α + 90°) am Einheitskreis),
# Schulaufgabe Gymnasium Bayern Kl. 10 (Bogenmaß, Kreisausschnitt, Laufbahnen), Grundwissen G9 Kl. 10 (Lösungen von sin x = 0,5 in [0; 2π[,
# allgemeine Sinusfunktion beschreiben), Abitur-IlluPA A5 (Symmetrie eines Produkts). Neue Aufgaben nutzen auch das Bogenmaß
# (Lehrplan: Funktionen im Bogenmaß) und die π-Beschriftung der Achse ("pi": true, seit 15.11.).
def schwer():
    start(10013)
    N = []

    def neu(l, s, a):
        a['l'], a['s'] = l, s
        N.append(a)

    def rz(wahr, nd):
        return gerundet(wahr, nd), f'round({K(wahr)}, {nd})'

    def pq(text, z, n, w, h, c=None):
        """Vielfaches von π als Lücke □/□ · π (gekürzt, Vorzeichen im Zähler)."""
        return luecken(text, '□/□ · π', 'Bruch vor π (gekürzt)', [z, n], w, h, c=c or [str(z), str(n)])

    # --- bogenmass ---
    w, c = rz(180 / PI, 1)
    neu('bogenmass', 2, zahl('Ein Winkel hat im Bogenmaß die Größe 1. Wie viel Grad sind das? Runde auf eine Nachkommastelle.', f'1 · 180° : π ≈ {dz(w)}°.',
                             'Umrechnen: Grad = Bogenmaß · 180° : π.', w, c, einheit='°', tol=0.1))
    neu('bogenmass', 2, pq('Gib −45° im Bogenmaß als Vielfaches von π an.', -1, 4, '−45° · π/180° = −1/4 · π = −π/4.', 'Ein negativer Winkel bleibt negativ.'))
    neu('bogenmass', 3, zahl('Ein Kreisausschnitt mit Radius r hat den Umfang 4r (zwei Radien und der Bogen). Wie groß ist sein Mittelpunktswinkel im Bogenmaß?',
                             'Umfang = r + r + b = 4r ⇒ Bogen b = 2r. Winkel im Bogenmaß x = b : r = 2.', 'Der Umfang besteht aus zwei Radien und dem Bogen.', 2, '(4 - 2) / 1'))
    w, c = rz(40 * PI / 2 / 41, 2)
    neu('bogenmass', 3, zahl('Auf einer Kreisbahn mit Radius 40 m läuft A einen Viertelkreis. B läuft auf der Nachbarbahn mit Radius 41 m genau dieselbe Strecke. Zu welchem Mittelpunktswinkel (Bogenmaß) gehört die Strecke von B? Runde auf zwei Nachkommastellen.',
                             f'Strecke von A: b = 40 · π/2 = 20π m ≈ 62,83 m. Für B: x = b : r = 20π : 41 ≈ {dz(w)}.', 'Berechne erst die Bogenlänge von A, dann x = b : r für B.',
                             w, c, tol=0.01))
    w, c = rz(12 * 2 * PI / 3, 1)
    neu('bogenmass', 3, zahl('Der Minutenzeiger einer Uhr ist 12 cm lang. Welchen Weg legt seine Spitze in 20 Minuten zurück? Runde auf eine Nachkommastelle.',
                             f'20 min sind 1/3 Umdrehung, also x = 2π/3. Bogen b = r · x = 12 · 2π/3 = 8π ≈ {dz(w)} cm.',
                             'Welcher Teil einer vollen Umdrehung sind 20 Minuten?', w, c, einheit='cm', tol=0.1))
    neu('bogenmass', 3, auswahl('Jemand rechnet: „2 im Bogenmaß sind 2 · 180° = 360°.“ Was stimmt?', 'Falsch: 2 · 180° : π ≈ 114,6°.',
                                ['Richtig.', 'Falsch: 2 · π : 180° ≈ 0,03°.', 'Falsch: 2 · 360° = 720°.'],
                                'π (nicht 1) entspricht 180°. Also 2 = 2 · 180°/π ≈ 114,6°. 360° wären 2π ≈ 6,28.', 'Welcher Bogenmaß-Wert entspricht 180°?'))

    # --- werte ---
    neu('werte', 2, zahl('Gib den exakten Wert von sin(−π/2) an.', '−π/2 = −90°. Am Einheitskreis liegt der Punkt ganz unten: sin(−π/2) = −1.',
                         'Drehe am Einheitskreis im Uhrzeigersinn.', -1, '-1'))
    neu('werte', 2, zahl('Gib den exakten Wert von cos(7π/3) an.', '7π/3 = 2π + π/3. Nach einer vollen Drehung gilt cos(7π/3) = cos(π/3) = 0,5.',
                         'Ziehe eine volle Umdrehung 2π ab.', 0.5, '1 / 2'))
    neu('werte', 3, auswahl('Für jeden Winkel α gilt am Einheitskreis: sin(180° − α) = …', 'sin α', ['−sin α', 'cos α', '−cos α'],
                            'Die Punkte zu α und 180° − α liegen spiegelbildlich zur y-Achse. Sie haben dieselbe Höhe, also denselben Sinus.',
                            'Zeichne α und 180° − α am Einheitskreis ein. Was ist gleich?'))
    neu('werte', 3, pq('Für welchen Winkel x mit 0 ≤ x ≤ π gilt cos x = −0,5? Gib x als Vielfaches von π an.', 2, 3,
                       'cos(π/3) = 0,5. cos ist negativ links der y-Achse: x = π − π/3 = 2π/3 (= 120°).', 'Bezugswinkel zu 0,5 ist π/3. Wo ist cos negativ?'))
    neu('werte', 3, zahl('Berechne ohne Taschenrechner: sin(π/6) + cos(π/3) + sin(3π/2).', '0,5 + 0,5 + (−1) = 0.', 'Bestimme jeden Wert am Einheitskreis.', 0, '1/2 + 1/2 - 1'))
    neu('werte', 3, zahl('Für wie viele x mit 0 ≤ x < 2π gilt sin x = cos x?', 'Höhe = Abstand nach rechts, beide mit gleichem Vorzeichen: bei π/4 (45°) und 5π/4 (225°). Das sind 2.',
                         'Am Einheitskreis: Wo sind x- und y-Koordinate gleich?', 2, '2'))

    # --- periode ---
    neu('periode', 2, zahl('Welche Periode hat f(x) = cos(πx) (x im Bogenmaß)?', 'p = 2π : b = 2π : π = 2.', 'Im Bogenmaß gilt p = 2π : b.', 2, '2'))
    neu('periode', 2, luecken('Welche Periode hat f(x) = sin(x/3) (x im Bogenmaß)? Gib sie als Vielfaches von π an.', '□ · π', 'Zahl vor π', [6],
                              'b = 1/3, p = 2π : (1/3) = 6π.', 'Teilen durch 1/3 heißt mal 3.', c=['2 * 3']))
    neu('periode', 3, zahl('f(x) = sin(b · x) (x im Bogenmaß, b > 0) hat die Periode 4π. Bestimme b.', '2π : b = 4π ⇒ b = 2π : 4π = 0,5.',
                           'Stelle 2π : b = 4π nach b um.', 0.5, '2 / 4'))
    neu('periode', 3, zahl('Welche kleinste Periode (in Grad) hat f(x) = sin(2x) + sin(3x)?', 'sin(2x) hat die Periode 180°, sin(3x) die Periode 120°. Beide wiederholen sich gleichzeitig erst nach dem kleinsten gemeinsamen Vielfachen: 360°.',
                           'Bestimme beide Perioden einzeln. Wann passen beide wieder zusammen?', 360, '2 * 180'))
    neu('periode', 3, zahl('Eine Funktion f hat die Periode 8, und es gilt f(3) = 5. Welchen Wert hat f(27)?', '27 = 3 + 3 · 8. Nach drei Perioden wiederholt sich der Wert: f(27) = f(3) = 5.',
                           'Wie viele ganze Perioden liegen zwischen 3 und 27?', 5, '5'))
    neu('periode', 3, auswahl('Jemand sagt: „Verdoppelt man in sin(b · x) den Wert von b, verdoppelt sich die Periode.“ Was stimmt?', 'Falsch: Die Periode halbiert sich.',
                              ['Richtig.', 'Falsch: Die Periode bleibt gleich.', 'Falsch: Die Amplitude verdoppelt sich.'],
                              'p = 2π : b. Doppeltes b im Nenner gibt die halbe Periode: Die Schwingung läuft doppelt so schnell.', 'Setze b = 1 und b = 2 in p = 2π : b ein.'))

    # --- parameter ---
    neu('parameter', 2, zahl('Welchen kleinsten Wert nimmt f(x) = −3 · sin(x) + 1 an?', 'Amplitude |−3| = 3, Mittellinie y = 1. Kleinster Wert: 1 − 3 = −2.',
                             'Das Minus vor der 3 spiegelt nur; die Amplitude ist 3.', -2, '1 - 3'))
    neu('parameter', 2, zahl('f(x) = 2 · cos(x) + d hat den größten Wert 7. Bestimme d.', 'Größter Wert d + 2 = 7 ⇒ d = 5.', 'Der größte Wert ist Mittellinie plus Amplitude.', 5, '7 - 2'))
    neu('parameter', 3, luecken('Der Graph von g(x) = a · cos(x) + b (x im Bogenmaß) geht durch die Punkte (0 | 5) und (π | −1). Bestimme a und b.', 'a = □; b = □', 'Zwei Zahlen',
                                [3, 2], 'cos 0 = 1: a + b = 5. cos π = −1: −a + b = −1. Addieren: 2b = 4 ⇒ b = 2, dann a = 3.',
                                'Setze beide Punkte ein. Du erhältst zwei Gleichungen.', c=['(5 + 1) // 2', '(5 - 1) // 2']))
    neu('parameter', 3, luecken('Gib die Wertemenge von f(x) = 2 · sin(0,5 · (x + π)) − 1 an.', 'W = [□; □]', 'Kleinster und größter Wert',
                                [-3, 1], 'Die Klammer ändert nur Periode und Verschiebung. Amplitude 2, Mittellinie y = −1: W = [−3; 1].',
                                'Welche Parameter beeinflussen die Wertemenge überhaupt?', c=['-1 - 2', '-1 + 2']))
    neu('parameter', 3, auswahl('Für welche Zahlen d hat f(x) = 2 · sin(x) + d keine Nullstelle?', 'für d > 2 oder d < −2', ['nur für d > 2', 'für alle d ≠ 0', 'für d ≥ 2 oder d ≤ −2'],
                                'f nimmt alle Werte zwischen d − 2 und d + 2 an. Keine Nullstelle, wenn 0 nicht dazwischen liegt: d − 2 > 0 oder d + 2 < 0. Bei d = ±2 berührt der Graph die x-Achse.',
                                'Wie sieht die Wertemenge aus? Wann liegt 0 nicht darin?'))
    neu('parameter', 3, zahl('f(x) = a · sin(x) (x im Bogenmaß) hat an der Stelle x = 3π/2 den Wert 3. Bestimme a.', 'sin(3π/2) = −1, also a · (−1) = 3 ⇒ a = −3.',
                             'Welchen Wert hat sin(3π/2)?', -3, '3 / (-1)'))

    # --- zuordnen ---
    neu('zuordnen', 2, auswahl('Der Graph von sin x wird in y-Richtung mit dem Faktor 3 gestreckt und danach um 1 nach unten verschoben. Welcher Term gehört dazu?',
                               'f(x) = 3 · sin(x) − 1', ['f(x) = sin(3x) − 1', 'f(x) = 3 · sin(x − 1)', 'f(x) = 3 · (sin(x) − 1)'],
                               'Streckung in y-Richtung: Faktor vor sin. Verschiebung nach unten: − 1 am Ende. 3 · (sin x − 1) wäre erst verschoben, dann gestreckt (Mittellinie −3).',
                               'Welcher Parameter streckt in y-Richtung, welcher verschiebt nach oben/unten?'))
    neu('zuordnen', 2, auswahl('Welcher Term hat die Periode π und die Amplitude 2 (x im Bogenmaß)?', 'f(x) = 2 · sin(2x)', ['f(x) = 2 · sin(0,5x)', 'f(x) = sin(2x) + 2', 'f(x) = 2 · sin(πx)'],
                               'Amplitude 2: Faktor 2 vor sin. Periode π = 2π : b ⇒ b = 2. sin(πx) hätte die Periode 2.', 'Periode im Bogenmaß: p = 2π : b.'))
    neu('zuordnen', 3, auswahl('Wie entsteht der Graph von g(x) = 2 · sin(0,5 · (x + π)) − 1 aus dem Graphen von sin x?',
                               'In y-Richtung mit 2 und in x-Richtung mit 2 strecken, um π nach links und um 1 nach unten verschieben.',
                               ['In y-Richtung mit 2 strecken, in x-Richtung mit 0,5 stauchen, um π nach rechts und um 1 nach unten verschieben.',
                                'In y-Richtung mit 0,5 und in x-Richtung mit 2 strecken, um π nach links und um 1 nach oben verschieben.',
                                'In y-Richtung mit 2 strecken, um π nach links und um 1 nach unten verschieben; die Periode bleibt 2π.'],
                               'a = 2: Streckung in y-Richtung. b = 0,5: Periode 2π : 0,5 = 4π, also Streckung in x-Richtung mit 2. x + π: Verschiebung nach links. − 1: nach unten.',
                               'Geh die Parameter einzeln durch: a, b, die Zahl in der Klammer, die Zahl am Ende.'))
    neu('zuordnen', 3, auswahl('Der Graph von sin x wird um π/2 nach rechts verschoben. Welcher einfachere Term beschreibt denselben Graphen?', 'f(x) = −cos(x)',
                               ['f(x) = cos(x)', 'f(x) = −sin(x)', 'f(x) = sin(x) − π/2'],
                               'sin(x − π/2) ist bei x = 0 gleich sin(−π/2) = −1, also Start im Minimum wie −cos x. Probe bei x = π/2: sin 0 = 0 = −cos(π/2).',
                               'Setze x = 0 und x = π/2 ein und vergleiche.'))
    neu('zuordnen', 3, luecken('Eine Funktion f(x) = a · cos(b · x) + d (x im Bogenmaß, a > 0, b > 0) hat einen Hochpunkt bei (0 | 5). Der nächste Tiefpunkt liegt bei (π | 1). Bestimme a, b und d.',
                               'a = □; b = □; d = □', 'Drei Zahlen', [2, 1, 3],
                               'Mittellinie d = (5 + 1) : 2 = 3, Amplitude a = (5 − 1) : 2 = 2. Vom Hoch- zum Tiefpunkt ist eine halbe Periode: p = 2π ⇒ b = 1.',
                               'Vom Hochpunkt bis zum nächsten Tiefpunkt ist eine halbe Periode.', c=['(5 - 1) // 2', '2 // 2', '(5 + 1) // 2']))
    g = koord([{'art': 'cos', 'a': -2, 'b': 1, 'c': 0, 'd': 1, 'bogen': True}], x=(0, round(2 * PI, 4)), y=(-2, 4), pi=True, schritt_y=1)
    neu('zuordnen', 3, mit_grafik(auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen (x im Bogenmaß)?', 'f(x) = −2 · cos(x) + 1',
                                          ['f(x) = 2 · cos(x) + 1', 'f(x) = −2 · sin(x) + 1', 'f(x) = −cos(2x) + 1'],
                                          'Mittellinie y = 1 (Mitte zwischen −1 und 3), Amplitude 2, Periode 2π. Bei x = 0 liegt ein Tiefpunkt: Start im Minimum, also −2 · cos(x) + 1.',
                                          'Lies Mittellinie, Amplitude und Periode ab. Wo liegt der Graph bei x = 0?'), g))

    # --- eigenschaften ---
    neu('eigenschaften', 2, pq('Bestimme die kleinste positive Nullstelle von f(x) = cos(2x) (x im Bogenmaß).', 1, 4,
                               'cos u = 0 zuerst bei u = π/2. 2x = π/2 ⇒ x = π/4.', 'Ersetze 2x durch u und suche die erste Nullstelle von cos u.'))
    neu('eigenschaften', 2, pq('An welcher Stelle zwischen 2π und 4π hat sin x einen Hochpunkt? Gib sie als Vielfaches von π an.', 5, 2,
                               'Hochpunkt bei π/2, dann alle 2π wieder: π/2 + 2π = 5π/2.', 'Addiere zur ersten Hochstelle π/2 eine Periode.'))
    neu('eigenschaften', 3, pq('Die Gleichung sin x = 0,5 hat im Intervall [0; 2π[ zwei Lösungen. Gib die größere an.', 5, 6,
                               'sin(π/6) = 0,5. Der zweite Punkt gleicher Höhe liegt spiegelbildlich zur y-Achse: π − π/6 = 5π/6.',
                               'Am Einheitskreis gibt es zwei Punkte mit der Höhe 0,5.'))
    neu('eigenschaften', 3, auswahl('Welche Symmetrie hat der Graph von f(x) = sin(x) · cos(x)?', 'punktsymmetrisch zum Ursprung', ['achsensymmetrisch zur y-Achse', 'keine Symmetrie', 'achsensymmetrisch zur Geraden x = π'],
                                    'f(−x) = sin(−x) · cos(−x) = (−sin x) · cos x = −f(x). Das ist Punktsymmetrie zum Ursprung.',
                                    'Berechne f(−x) mit sin(−x) = −sin x und cos(−x) = cos x.'))
    neu('eigenschaften', 3, luecken('Bestimme die Stelle und den Wert des größten Funktionswerts von f(x) = 3 − 2 · sin(x) im Intervall [0; 2π[.', 'x = □/□ · π; y = □',
                                    'Stelle als Vielfaches von π, dann der Wert', [3, 2, 5],
                                    'f ist am größten, wenn sin x am kleinsten ist: sin x = −1 bei x = 3π/2. Dann f = 3 − 2 · (−1) = 5.',
                                    'Wegen des Minus vor der 2: Wann ist sin x am kleinsten?', c=['3', '2', '3 + 2']))
    neu('eigenschaften', 3, zahl('Wie viele Schnittpunkte haben die Graphen von y = sin x und y = 0,1 · x (x im Bogenmaß)?',
                                 'Schnitt nur, wo |0,1x| ≤ 1, also −10 ≤ x ≤ 10. Rechts: einer zwischen 0 und π, zwei im Bogen zwischen 2π ≈ 6,3 und 3π ≈ 9,4 (Gerade dort bei 0,6 bis 0,9). Links genauso (Punktsymmetrie), dazu x = 0. Zusammen 7.',
                                 'sin x bleibt zwischen −1 und 1. Wie weit reicht die Gerade in diesem Streifen? Skizziere.', 7, '1 + 2 * 3'))

    # --- anwendung ---
    neu('anwendung', 2, zahl('Die Temperatur an einem Sommertag wird durch T(t) = 18 − 6 · cos(π/12 · t) beschrieben (t in Stunden nach Mitternacht, T in °C). Wie hoch ist die Höchsttemperatur?',
                             'cos ist mindestens −1. Dann T = 18 − 6 · (−1) = 24 °C.', 'Wann ist 18 − 6 · cos(…) am größten?', 24, '18 + 6', einheit='°C'))
    neu('anwendung', 2, zahl('T(t) = 18 − 6 · cos(π/12 · t) (t in Stunden nach Mitternacht). Um wie viel Uhr ist es am wärmsten?',
                             'Am wärmsten bei cos(π/12 · t) = −1, also π/12 · t = π ⇒ t = 12. Das ist 12 Uhr.', 'cos ist −1 beim Winkel π.', 12, '12', einheit='Uhr'))
    neu('anwendung', 3, luecken('In einer Stadt dauert der längste Tag 16 Stunden, der kürzeste 8 Stunden. Die Tageslänge wird durch T(t) = a · sin(b · t) + d beschrieben (a > 0). Bestimme a und d.',
                                'a = □; d = □', 'Zwei Zahlen', [4, 12], 'd = (16 + 8) : 2 = 12 (Mittelwert), a = (16 − 8) : 2 = 4 (halbe Schwankung).',
                                'd ist die Mitte zwischen größtem und kleinstem Wert, a die halbe Differenz.', c=['(16 - 8) // 2', '(16 + 8) // 2']))
    w, c = rz(365 / 3, 1)
    neu('anwendung', 3, zahl('Die Tageslänge (in h) wird durch T(t) = 12 + 4 · sin(2π/365 · t) beschrieben (t in Tagen). An wie vielen Tagen im Jahr ist der Tag länger als 14 Stunden? Runde auf eine Nachkommastelle.',
                             f'12 + 4 · sin u > 14 ⇔ sin u > 0,5 ⇔ π/6 < u < 5π/6. Das ist ein Drittel einer Periode (2π/3 von 2π): 365 : 3 ≈ {dz(w)} Tage.',
                             'Für welche Winkel u ist sin u > 0,5? Welcher Anteil einer ganzen Periode ist das?', w, c, einheit='Tage', tol=0.1))
    w, c = rz(10 * 2 / 3, 1)
    neu('anwendung', 3, zahl('Die Höhe einer Gondel ist h(t) = 30 − 25 · cos(36° · t) (t in min, h in m). Wie viele Minuten einer Umdrehung ist die Gondel höher als 17,5 m? Runde auf eine Nachkommastelle.',
                             f'30 − 25 · cos u > 17,5 ⇔ cos u < 0,5 ⇔ 60° < u < 300°. Das sind 240° von 360°, also 2/3 der Umlaufzeit 360 : 36 = 10 min: ≈ {dz(w)} min.',
                             'Für welche Winkel ist cos u < 0,5? Welcher Anteil einer Umdrehung ist das?', w, c, einheit='min', tol=0.1))
    neu('anwendung', 3, auswahl('h(t) = 30 − 25 · cos(36° · t) (t in min). Jemand tippt für t = 2 in den Taschenrechner „30 − 25 · cos(72)“ im RAD-Modus und erhält etwa 54,2 m. Was stimmt?',
                                'Falsch: Der Winkel 72° steht in Grad, der Rechner muss im DEG-Modus sein; richtig sind etwa 22,3 m.',
                                ['Richtig.', 'Falsch: Man muss cos(36) · 2 rechnen.', 'Falsch: Der Rechner muss im RAD-Modus sein; richtig sind etwa 22,3 m.'],
                                f'36° · 2 = 72°. Im DEG-Modus: cos 72° ≈ 0,309, h ≈ 30 − 7,7 ≈ 22,3 m. Im RAD-Modus wird cos(72 im Bogenmaß) ≈ {dz(round(math.cos(72), 3))} gerechnet – ein ganz anderer Winkel.',
                                'In welcher Einheit steht der Winkel in der Formel?'))
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('funktionen.trig', 13_10_4)
# a) Einschritt-Aufgabe bzw. gleicher Typ wie Stufe 1 → Stufe 2
BF.stufe('periode', 'Eine Sinusfunktion f(x) = sin(b · x) soll die Periode 90° haben. Bestimme b.', 2)
BF.stufe('periode', 'Jemand sagt: „f(x) = sin(0,5x) hat die Periode 180°.“ Was stimmt?', 2)
# a) reine Taschenrechner-Aufgaben stehen gleich auf Stufe 1 und 2 → Stufe 1
BF.stufe('werte', 'Berechne sin(2,7) (x im Bogenmaß) auf drei Nachkommastellen.', 1)
BF.stufe('werte', 'Berechne cos(4,4) (x im Bogenmaß) auf drei Nachkommastellen.', 1)
BF.nicht_umgesetzt('periode, parameter, zuordnen, eigenschaften, anwendung: fast nur Gradmaß statt Bogenmaß (LehrplanPLUS M10 3, Abitur)',
                   'Kein Fehler in einzelnen Aufgaben; ein Umstellen aller alten Aufgaben auf Bogenmaß wäre ein Umbau der Karten. Runde 10 hat Bogenmaß-Aufgaben ergänzt (siehe „für Sebastian“).')
BF.fuer_sebastian('funktionen.trig: Die alten Aufgaben arbeiten fast nur im Gradmaß; LehrplanPLUS M10 3 und Abitur nutzen das Bogenmaß. Die Begründung unter „offen“ (keine π-Beschriftung) ist seit 15.11. überholt. Karten/alte Aufgaben auf Bogenmaß umstellen?')

# ---- BEFUNDE ENDE ----


# ---- Fünfzehnte Runde (Zweig nacharbeit): je Lernkarte 8 neue Übungen im Bogenmaß (Stufe 1: 2, Stufe 2: 3, Stufe 3: 3) ----
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH Zehnter Runde und Befunden angehängt, alte Aufgaben bleiben gleich.
def nacharbeit():
    start(15004)
    N = []

    def neu(l, s, a):
        assert a is not None, 'zu wenige Antworten'
        a['l'], a['s'] = l, s
        N.append(a)

    def rz(wahr, nd):
        w = gerundet(wahr, nd)
        assert w is not None
        return w, f'round({K(wahr)}, {nd})'

    def pq(text, z, n, w, h, c=None):
        return luecken(text, '□/□ · π', 'Bruch vor π (gekürzt)', [z, n], w, h, c=c or [str(z), str(n)])

    def pk(text, k, w, h, c=None):
        return luecken(text, '□ · π', 'Zahl vor π', [k], w, h, c=c or [str(k)])

    def gb(gs, x1=2, y=None, **kw):
        return koord([dict(g, bogen=True) for g in gs], x=(0, round(x1 * PI, 4)), y=y, pi=True, schritt_y=1, **kw)

    # --- bogenmass ---
    neu('bogenmass', 1, pq('Gib 210° im Bogenmaß als Vielfaches von π an.', 7, 6, '210° · π/180° = 210/180 · π = 7/6 · π = 7π/6.',
                           'Teile durch 180° und kürze.', c=['210 // 30', '180 // 30']))
    neu('bogenmass', 1, zahl('Wie viel Grad sind 5π/9?', '5π/9 = 5 · 180° : 9 = 100°.', 'Ersetze π durch 180°.', 100, '5 * 180 / 9', einheit='°'))
    w, c = rz(2.5 * 180 / PI, 1)
    neu('bogenmass', 2, zahl('Ein Winkel hat im Bogenmaß die Größe 2,5. Wie viel Grad sind das? Runde auf eine Nachkommastelle.',
                             f'2,5 · 180° : π ≈ {dz(w)}°.', 'Grad = Bogenmaß · 180° : π.', w, c, einheit='°', tol=0.1))
    neu('bogenmass', 2, pq('Gib −120° im Bogenmaß als Vielfaches von π an.', -2, 3, '−120° · π/180° = −120/180 · π = −2/3 · π = −2π/3.',
                           'Ein negativer Winkel bleibt negativ. Kürze 120/180.', c=['-120 // 60', '180 // 60']))
    neu('bogenmass', 2, auswahl('Welcher Winkel ist am größten?', '3π/4', ['2 (im Bogenmaß)', '100°', '1,5 (im Bogenmaß)'],
                                '3π/4 = 135°. 2 im Bogenmaß ≈ 114,6°, 1,5 im Bogenmaß ≈ 85,9°. Am größten ist 3π/4.', 'Rechne alles in Grad um: · 180° : π.'))
    w, c = rz(8 * 3 * PI / 4, 1)
    neu('bogenmass', 3, zahl('Ein Kreis hat den Radius 8 cm. Wie lang ist der Bogen zum Mittelpunktswinkel 3π/4? Runde auf eine Nachkommastelle.',
                             f'Bogenlänge = Radius · Winkel im Bogenmaß = 8 · 3π/4 = 6π ≈ {dz(w)} cm.', 'Im Bogenmaß gilt: b = r · x.', w, c, einheit='cm', tol=0.1))
    w, c = rz(100 / 30, 2)
    neu('bogenmass', 3, zahl('Ein Rad mit dem Radius 30 cm rollt 1 m weit, ohne zu rutschen. Um welchen Winkel (im Bogenmaß) hat es sich gedreht? Runde auf zwei Nachkommastellen.',
                             f'Der abgerollte Weg ist der Bogen: x = b : r = 100 cm : 30 cm ≈ {dz(w)}.', 'Rechne 1 m in cm um. Winkel = Bogen : Radius.', w, c, tol=0.01))
    neu('bogenmass', 3, auswahl('Der Minutenzeiger einer Uhr dreht sich von 12:00 Uhr bis 12:40 Uhr. Um welchen Winkel dreht er sich (im Bogenmaß)?', '4π/3',
                                ['2π/3', '3π/4', '40π'], '40 Minuten sind 2/3 einer Stunde: 2/3 · 360° = 240°. 240° = 240/180 · π = 4π/3.',
                                'Welcher Anteil einer vollen Drehung (2π) sind 40 Minuten?'))
    # --- werte ---
    neu('werte', 1, zahl('Gib den exakten Wert von cos(π) an.', 'π = 180°: Der Punkt liegt am Einheitskreis ganz links. cos(π) = −1.', 'cos ist der Abstand nach rechts.', -1, '-1'))
    neu('werte', 1, zahl('Gib den exakten Wert von sin(π/2) an.', 'π/2 = 90°: Der Punkt liegt ganz oben. sin(π/2) = 1.', 'sin ist die Höhe am Einheitskreis.', 1, '1'))
    neu('werte', 2, zahl('Gib den exakten Wert von cos(5π/3) an.', '5π/3 = 300°. Der Punkt liegt rechts unten, so weit rechts wie bei 60°: cos(5π/3) = 0,5.',
                         'Rechne in Grad um und vergleiche mit 60°.', Fr(1, 2), '1/2'))
    neu('werte', 2, zahl('Gib den exakten Wert von sin(11π/6) an.', '11π/6 = 330°. Der Punkt liegt rechts unten, so tief wie bei 30° hoch: sin(11π/6) = −0,5.',
                         '330° fehlen 30° bis zur vollen Runde.', Fr(-1, 2), '-1/2'))
    neu('werte', 2, auswahl('Welcher Wert ist am größten?', 'cos(π/6)', ['sin(π/6)', 'sin(5π/4)', 'cos(π)'],
                            'cos(π/6) = ½√3 ≈ 0,87; sin(π/6) = 0,5; sin(5π/4) = −½√2 ≈ −0,71; cos(π) = −1.', 'Bestimme jeden Wert am Einheitskreis.'))
    neu('werte', 3, zahl('Berechne ohne Taschenrechner: cos(π) + 2 · sin(π/6) + cos(2π).', '−1 + 2 · 0,5 + 1 = 1.', 'Bestimme jeden Wert am Einheitskreis.', 1, '-1 + 2 * 1/2 + 1'))
    neu('werte', 3, pq('Die Gleichung sin x = −0,5 hat im Intervall [π; 2π] zwei Lösungen. Gib die kleinere als Vielfaches von π an.', 7, 6,
                       'sin(π/6) = 0,5. Die Höhe −0,5 hat der Punkt bei π + π/6 = 7π/6 und bei 2π − π/6 = 11π/6. Die kleinere ist 7π/6.',
                       'Am Einheitskreis gibt es unten zwei Punkte mit der Höhe −0,5.'))
    neu('werte', 3, auswahl('Jemand rechnet sin(π/2) im DEG-Modus und erhält etwa 0,027. Was stimmt?', 'Falsch: π/2 steht im Bogenmaß; im RAD-Modus ergibt sich 1.',
                            ['Richtig: sin(π/2) ≈ 0,027.', 'Falsch: Das Ergebnis ist 0,5.', 'Falsch: Das Ergebnis ist 0.'],
                            'Im DEG-Modus wird π/2 ≈ 1,57 als 1,57° gelesen, sin(1,57°) ≈ 0,027. Gemeint ist der Winkel π/2 = 90°: sin(π/2) = 1.',
                            'In welcher Einheit steht π/2?'))
    # --- periode ---
    neu('periode', 1, pk('Welche Periode hat f(x) = sin(x) im Bogenmaß? Gib sie als Vielfaches von π an.', 2, 'Eine volle Umdrehung sind 360° = 2π. Periode 2π.', 'Wie viel sind 360° im Bogenmaß?'))
    neu('periode', 1, pq('Welche Periode hat f(x) = sin(4x) im Bogenmaß? Gib sie als Vielfaches von π an.', 1, 2, 'p = 2π : b = 2π : 4 = π/2.', 'Im Bogenmaß gilt p = 2π : b.',
                         c=['2 // 2', '4 // 2']))
    neu('periode', 2, zahl('Welche Periode hat f(x) = sin(2πx) (x im Bogenmaß)?', 'p = 2π : b = 2π : 2π = 1.', 'Hier ist b = 2π.', 1, '2 / 2'))
    neu('periode', 2, pk('Welche Periode hat f(x) = cos(2x/3) (x im Bogenmaß)? Gib sie als Vielfaches von π an.', 3, 'b = 2/3, also p = 2π : 2/3 = 2π · 3/2 = 3π.',
                         'Durch einen Bruch teilt man, indem man mit dem Kehrwert malnimmt.', c=['2 * 3 // 2']))
    neu('periode', 2, mit_grafik(auswahl('Der Graph zeigt f(x) = sin(b · x) (x im Bogenmaß). Wie groß ist b?', '2', ['1', '0,5', '4'],
                                         'Eine Schwingung reicht von 0 bis π, die Periode ist π. b = 2π : π = 2.', 'Lies die Periode ab: Wo ist die erste Schwingung fertig?'),
                                 gb([{'art': 'sin', 'a': 1, 'b': 2, 'c': 0, 'd': 0}], y=(-2, 2))))
    neu('periode', 3, zahl('f(x) = cos(b · x) (x im Bogenmaß, b > 0) hat die Periode π/3. Bestimme b.', '2π : b = π/3 ⇒ b = 2π : π/3 = 2 · 3 = 6.', 'Setze in p = 2π : b ein.', 6, '2 * 3'))
    neu('periode', 3, pk('Welche kleinste Periode hat f(x) = sin(x) + cos(2x) (x im Bogenmaß)? Gib sie als Vielfaches von π an.', 2,
                         'sin x hat die Periode 2π, cos(2x) die Periode π. Beide wiederholen sich gleichzeitig erst nach 2π.',
                         'Bestimme beide Perioden. Wann wiederholen sich beide zugleich?'))
    neu('periode', 3, zahl('Ein Pendel schwingt nach s(t) = 5 · sin(π/2 · t) (t in s, x im Bogenmaß). Wie viele Sekunden dauert eine volle Schwingung?',
                           'p = 2π : b = 2π : π/2 = 4 s.', 'Hier ist b = π/2.', 4, '2 * 2', einheit='s'))
    # --- parameter ---
    neu('parameter', 1, zahl('Welche Amplitude hat f(x) = 4 · sin(x) − 2 (x im Bogenmaß)?', 'Die Amplitude ist der Faktor vor sin: 4. Die −2 verschiebt nur nach unten.',
                             'Welche Zahl steht vor sin?', 4, '4'))
    neu('parameter', 1, zahl('Welchen größten Wert hat f(x) = 2 · cos(x) + 3 (x im Bogenmaß)?', 'Mittellinie 3, Amplitude 2: größter Wert 3 + 2 = 5.',
                             'Größter Wert = Mittellinie + Amplitude.', 5, '3 + 2'))
    neu('parameter', 2, zahl('Welchen Wert hat f(x) = 2 · sin(x) − 1 an der Stelle x = 3π/2?', 'sin(3π/2) = −1, also f(3π/2) = 2 · (−1) − 1 = −3.',
                             '3π/2 = 270°: Wo liegt der Punkt am Einheitskreis?', -3, '2 * (-1) - 1'))
    neu('parameter', 2, luecken('Gib die Wertemenge von f(x) = 3 · cos(2x) − 1 an (x im Bogenmaß).', 'W = [□; □]', 'Kleinster und größter Wert', [-4, 2],
                                'Amplitude 3, Mittellinie y = −1: von −1 − 3 = −4 bis −1 + 3 = 2. Der Faktor 2 vor x ändert nur die Periode.',
                                'Mittellinie minus und plus Amplitude.', c=['-1 - 3', '-1 + 3']))
    neu('parameter', 2, auswahl('An welcher Stelle im Intervall [0; 2π[ nimmt f(x) = 2 · sin(x) + 1 seinen kleinsten Wert an?', 'x = 3π/2', ['x = π/2', 'x = π', 'x = 0'],
                                'f ist am kleinsten, wenn sin x = −1 ist. Das ist bei 3π/2 (270°) der Fall: f(3π/2) = −1.', 'Wann ist sin x am kleinsten?'))
    neu('parameter', 3, luecken('f(x) = a · sin(x) + d (x im Bogenmaß) hat bei x = π/2 den Wert 7 und bei x = 3π/2 den Wert −1. Bestimme a und d.', 'a = □; d = □', 'Zwei Zahlen', [4, 3],
                                'sin(π/2) = 1 und sin(3π/2) = −1: a + d = 7 und −a + d = −1. Addieren: 2d = 6, d = 3; dann a = 4.',
                                'Setze beide Stellen ein und löse das Gleichungssystem.', c=['(7 - (-1)) // 2', '(7 + (-1)) // 2']))
    neu('parameter', 3, zahl('f(x) = a · cos(x) + 2 (x im Bogenmaß, a > 0) hat den kleinsten Wert −3. Welchen Wert hat f(π/3)?',
                             'Kleinster Wert 2 − a = −3 ⇒ a = 5. f(π/3) = 5 · cos(π/3) + 2 = 5 · 0,5 + 2 = 4,5.', 'Bestimme zuerst a aus dem kleinsten Wert.',
                             Fr(9, 2), '5 * 1/2 + 2'))
    neu('parameter', 3, auswahl('Für welche Werte von a hat f(x) = a · cos(x) + 1 (x im Bogenmaß) Nullstellen?', 'für a ≥ 1 oder a ≤ −1',
                                ['nur für a > 1', 'für alle a ≠ 0', 'für a > 1 oder a < −1'],
                                'Der kleinste Wert ist 1 − |a|. Nullstellen gibt es, wenn er höchstens 0 ist: |a| ≥ 1. Bei |a| = 1 berührt der Graph die x-Achse.',
                                'Wann reicht die Kurve bis zur x-Achse hinunter?'))
    # --- zuordnen ---
    neu('zuordnen', 1, mit_grafik(auswahl('Welcher Term gehört zum gezeichneten Graphen (x im Bogenmaß)?', 'f(x) = cos(x)', ['f(x) = sin(x)', 'f(x) = −cos(x)', 'f(x) = −sin(x)'],
                                          'Der Graph startet bei x = 0 ganz oben (y = 1) und hat die Periode 2π: cos x.', 'Wo liegt der Graph bei x = 0?'),
                                  gb([{'art': 'cos', 'a': 1, 'b': 1, 'c': 0, 'd': 0}], y=(-2, 2))))
    neu('zuordnen', 1, mit_grafik(auswahl('Welcher Term gehört zum gezeichneten Graphen (x im Bogenmaß)?', 'f(x) = 3 · sin(x)', ['f(x) = sin(3x)', 'f(x) = sin(x) + 3', 'f(x) = 3 · cos(x)'],
                                          'Start auf der Mittellinie y = 0, steigend: sin. Höchster Wert 3, Periode 2π: 3 · sin(x).', 'Lies den höchsten Wert und die Periode ab.'),
                                  gb([{'art': 'sin', 'a': 3, 'b': 1, 'c': 0, 'd': 0}], y=(-4, 4))))
    neu('zuordnen', 2, mit_grafik(auswahl('Welcher Term gehört zum gezeichneten Graphen (x im Bogenmaß)?', 'f(x) = sin(2x) + 1',
                                          ['f(x) = sin(0,5x) + 1', 'f(x) = 2 · sin(x) + 1', 'f(x) = cos(2x) + 1'],
                                          'Mittellinie y = 1, Amplitude 1, eine Schwingung bis π: b = 2π : π = 2. Start auf der Mittellinie, steigend: sin(2x) + 1.',
                                          'Lies Mittellinie, Amplitude und Periode ab.'),
                                  gb([{'art': 'sin', 'a': 1, 'b': 2, 'c': 0, 'd': 1}], y=(-1, 3))))
    neu('zuordnen', 2, auswahl('Welcher Term hat die Periode 4π und die Mittellinie y = 2 (x im Bogenmaß)?', 'f(x) = sin(0,5x) + 2',
                               ['f(x) = sin(4x) + 2', 'f(x) = 2 · sin(0,5x)', 'f(x) = sin(2x) + 2'],
                               'Periode 4π ⇒ b = 2π : 4π = 0,5. Mittellinie y = 2 ⇒ + 2.', 'Rechne b = 2π : p aus.'))
    neu('zuordnen', 2, mit_grafik(auswahl('Welcher Term gehört zum gezeichneten Graphen (x im Bogenmaß)?', 'f(x) = −2 · sin(x)', ['f(x) = 2 · sin(x)', 'f(x) = −2 · cos(x)', 'f(x) = −sin(2x)'],
                                          'Start auf der Mittellinie y = 0, aber fallend; tiefster Wert −2 bei π/2, Periode 2π: −2 · sin(x).', 'Steigt oder fällt der Graph bei x = 0?'),
                                  gb([{'art': 'sin', 'a': -2, 'b': 1, 'c': 0, 'd': 0}], y=(-3, 3))))
    neu('zuordnen', 3, luecken('Eine Funktion f(x) = a · sin(b · x) + d (x im Bogenmaß, a > 0, b > 0) hat einen Hochpunkt bei (π/4 | 6). Der nächste Tiefpunkt liegt bei (3π/4 | 0). Bestimme a, b und d.',
                               'a = □; b = □; d = □', 'Drei Zahlen', [3, 2, 3],
                               'd = (6 + 0) : 2 = 3, a = (6 − 0) : 2 = 3. Vom Hoch- zum Tiefpunkt ist eine halbe Periode: π/2, also p = π und b = 2π : π = 2. Probe: sin(2 · π/4) = 1.',
                               'Vom Hochpunkt bis zum nächsten Tiefpunkt ist eine halbe Periode.', c=['(6 - 0) // 2', '2 // 1', '(6 + 0) // 2']))
    neu('zuordnen', 3, mit_grafik(auswahl('Welcher Term gehört zum gezeichneten Graphen (x im Bogenmaß)?', 'f(x) = 2 · cos(0,5x)',
                                          ['f(x) = 2 · cos(2x)', 'f(x) = 0,5 · cos(2x)', 'f(x) = 2 · sin(0,5x)'],
                                          'Start ganz oben bei 2: cos mit Amplitude 2. Eine Schwingung reicht bis 4π: b = 2π : 4π = 0,5.',
                                          'Lies die Periode genau ab: Wo ist der Graph wieder ganz oben?'),
                                  gb([{'art': 'cos', 'a': 2, 'b': 0.5, 'c': 0, 'd': 0}], x1=4, y=(-3, 3))))
    neu('zuordnen', 3, auswahl('Wie entsteht der Graph von g(x) = sin(x − π/3) + 2 aus dem Graphen von sin x?', 'um π/3 nach rechts und um 2 nach oben verschoben',
                               ['um π/3 nach links und um 2 nach oben verschoben', 'um π/3 nach rechts und um 2 nach unten verschoben', 'mit dem Faktor 2 gestreckt und um π/3 nach rechts verschoben'],
                               'x − π/3: Derselbe Wert kommt π/3 später, also nach rechts. + 2 schiebt nach oben.', 'Bei x − c wandert der Graph nach rechts.'))
    # --- eigenschaften ---
    neu('eigenschaften', 1, pk('Wo hat sin x (x im Bogenmaß) die kleinste positive Nullstelle? Gib sie als Vielfaches von π an.', 1,
                               'sin x ist die Höhe. Sie ist nach 0 erst wieder bei 180° = π gleich 0.', 'Wann ist die Gondel wieder auf Höhe der Mitte?'))
    neu('eigenschaften', 1, pq('An welcher Stelle im Intervall [0; 2π[ hat sin x einen Tiefpunkt? Gib sie als Vielfaches von π an.', 3, 2,
                               'Ganz unten ist der Punkt bei 270° = 3π/2.', 'Wann ist die Höhe am kleinsten?'))
    neu('eigenschaften', 2, pq('Bestimme die kleinste positive Nullstelle von f(x) = sin(3x) (x im Bogenmaß).', 1, 3,
                               'sin u = 0 zuerst wieder bei u = π. 3x = π ⇒ x = π/3.', 'Ersetze 3x durch u.'))
    neu('eigenschaften', 2, zahl('Wie viele Nullstellen hat cos x im Intervall [0; 4π] (x im Bogenmaß)?', 'Nullstellen bei π/2, 3π/2, 5π/2 und 7π/2: Das sind 4.',
                                 'In jeder Periode 2π hat cos zwei Nullstellen.', 4, '2 * 2'))
    neu('eigenschaften', 2, auswahl('Welche Aussage stimmt (x im Bogenmaß)?', 'cos(−π/3) = cos(π/3)',
                                    ['cos(−π/3) = −cos(π/3)', 'sin(−π/3) = sin(π/3)', 'cos(4π/3) = cos(π/3)'],
                                    'Der cos-Graph ist achsensymmetrisch zur y-Achse: cos(−x) = cos x. sin ist punktsymmetrisch: sin(−x) = −sin x. cos(4π/3) = −0,5, cos(π/3) = 0,5.',
                                    'Welcher Graph ist achsensymmetrisch zur y-Achse?'))
    neu('eigenschaften', 3, luecken('Die Gleichung cos x = 0,5 hat im Intervall [0; 2π[ zwei Lösungen. Gib beide als Vielfache von π an, die kleinere zuerst.',
                                    'x₁ = □/□ · π; x₂ = □/□ · π', 'Zwei Brüche vor π (gekürzt)', [1, 3, 5, 3],
                                    'cos(π/3) = 0,5. Der zweite Punkt gleicher Rechts-Lage liegt gespiegelt an der x-Achse: 2π − π/3 = 5π/3.',
                                    'Am Einheitskreis gibt es zwei Punkte mit dem Abstand 0,5 nach rechts.', c=['1', '3', '6 - 1', '3']))
    neu('eigenschaften', 3, zahl('Wie viele Lösungen hat die Gleichung sin(2x) = 0,5 im Intervall [0; 2π[ (x im Bogenmaß)?',
                                 'Mit u = 2x läuft u von 0 bis 4π, also zwei volle Perioden. In jeder Periode hat sin u = 0,5 zwei Lösungen: zusammen 4.',
                                 'Ersetze 2x durch u. Welchen Bereich durchläuft u?', 4, '2 * 2'))
    neu('eigenschaften', 3, auswahl('Welche Symmetrie hat der Graph von f(x) = x · sin(x) (x im Bogenmaß)?', 'achsensymmetrisch zur y-Achse',
                                    ['punktsymmetrisch zum Ursprung', 'keine Symmetrie', 'achsensymmetrisch zur Geraden x = π'],
                                    'f(−x) = (−x) · sin(−x) = (−x) · (−sin x) = x · sin x = f(x). Das ist Achsensymmetrie zur y-Achse.',
                                    'Berechne f(−x) mit sin(−x) = −sin x.'))
    # --- anwendung ---
    neu('anwendung', 1, zahl('Der Wasserstand in einem Hafen ist h(t) = 3 + 2 · sin(π/6 · t) (t in Stunden, h in m). Wie hoch steht das Wasser bei t = 0?',
                             'sin(0) = 0, also h(0) = 3 + 0 = 3 m.', 'Setze t = 0 ein.', 3, '3 + 2 * 0', einheit='m'))
    neu('anwendung', 1, zahl('h(t) = 3 + 2 · sin(π/6 · t) (t in Stunden, h in m). Wie hoch steht das Wasser höchstens?', 'sin ist höchstens 1: 3 + 2 · 1 = 5 m.',
                             'Mittellinie plus Amplitude.', 5, '3 + 2', einheit='m'))
    neu('anwendung', 2, zahl('h(t) = 3 + 2 · sin(π/6 · t) (t in Stunden). Nach wie vielen Stunden wiederholt sich der Wasserstand?', 'p = 2π : π/6 = 12 Stunden.',
                             'Im Bogenmaß gilt p = 2π : b.', 12, '2 * 6', einheit='h'))
    neu('anwendung', 2, zahl('h(t) = 3 + 2 · sin(π/6 · t) (t in Stunden, h in m). Wie hoch steht das Wasser nach 1 Stunde?', 'sin(π/6) = 0,5: h(1) = 3 + 2 · 0,5 = 4 m.',
                             'π/6 = 30°.', 4, '3 + 2 * 1/2', einheit='m'))
    neu('anwendung', 2, luecken('Ein Riesenrad braucht 8 Minuten für eine Umdrehung. Bestimme b in h(t) = a · sin(b · t) + d (t in min, b im Bogenmaß).', 'b = □/□ · π',
                                'Bruch vor π (gekürzt)', [1, 4], 'Eine Umdrehung ist 2π in 8 Minuten: b = 2π : 8 = π/4.', 'b = 2π : Periodendauer.', c=['1', '8 // 2']))
    w, c = rz(25 - 20 * math.cos(PI / 10 * 13), 1)
    neu('anwendung', 3, zahl('Die Höhe einer Gondel ist h(t) = 25 − 20 · cos(π/10 · t) (t in min, h in m). Wie hoch ist sie nach 13 Minuten? Runde auf eine Nachkommastelle.',
                             f'π/10 · 13 = 1,3π (234°). cos(1,3π) ≈ −0,588, h ≈ 25 + 11,76 ≈ {dz(w)} m. Rechner im RAD-Modus!',
                             'Setze t = 13 ein und rechne im RAD-Modus.', w, c, einheit='m', tol=0.1))
    w, c = rz(20 / 3, 1)
    neu('anwendung', 3, zahl('h(t) = 25 − 20 · cos(π/10 · t) (t in min, h in m). Wie viele Minuten einer Umdrehung ist die Gondel höher als 35 m? Runde auf eine Nachkommastelle.',
                             f'25 − 20 · cos u > 35 ⇔ cos u < −0,5 ⇔ 2π/3 < u < 4π/3. Das ist 1/3 einer Periode; die Umlaufzeit ist 2π : π/10 = 20 min: ≈ {dz(w)} min.',
                             'Für welche Winkel ist cos u < −0,5? Welcher Anteil einer Umdrehung ist das?', w, c, einheit='min', tol=0.1))
    neu('anwendung', 3, zahl('T(t) = 15 + 8 · sin(π/12 · (t − 9)) (t in Stunden nach Mitternacht, T in °C). Um wie viel Uhr ist es am wärmsten?',
                             'Am wärmsten bei sin(…) = 1, also π/12 · (t − 9) = π/2 ⇒ t − 9 = 6 ⇒ t = 15. Das ist 15 Uhr.', 'sin ist 1 beim Winkel π/2.', 15, '9 + 6', einheit='Uhr'))
    return N


def nacharbeit_anhaengen(thema, neue):
    """Hängt die Übungen der Fünfzehnten Runde an (alte Aufgaben bleiben unverändert und in derselben Reihenfolge)."""
    import json
    from _kl10 import THEMEN, _schluessel, _hoch
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    lz = [e['lernziel'] for e in d['inhalt']['etappen']]
    beispiele = {(s['text'] if isinstance(s, dict) else s).strip() for e in d['inhalt']['etappen'] for s in e.get('schritte', [])}
    gesehen = {_schluessel(a) for a in d['aufgaben']}
    zahl_ = {(l, s): 0 for l in lz for s in (1, 2, 3)}
    for a in neue:
        l, s = a.pop('l'), a.pop('s')
        assert l in lz and s in (1, 2, 3)
        assert a.get('h') and len(a.get('w', '')) >= 15, a['f']['text']
        if a['y'] == 'zahl': assert 'c' in a
        a['f']['text'] = _hoch(a['f']['text']); a['w'] = _hoch(a['w'])
        if 'a' in a: a['a'] = [_hoch(x) for x in a['a']]
        k = _schluessel(a)
        assert k not in gesehen, f'Dublette: {a["f"]["text"]}'
        assert a['f']['text'].strip() not in beispiele
        gesehen.add(k)
        d['aufgaben'].append({'l': l, 't': a.pop('t', None) or l, 'p': 'uebung', 's': s, **a})
        zahl_[(l, s)] += 1
    for l in lz:
        assert (zahl_[(l, 1)], zahl_[(l, 2)], zahl_[(l, 3)]) == (2, 3, 3), f'{l}: {zahl_}'
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'{pfad.name}: {len(neue)} Bogenmaß-Übungen (Fünfzehnte Runde) angehängt, jetzt {len(d["aufgaben"])} Aufgaben')

# ---------- Achtzehnte Runde (Zweig luecken-kl10): Verschiebung in x-Richtung, beliebige Winkel ----------
# Lücken laut Aufbau-Prüfung (inhalte/pruefung/aufbau/klasse10.json): LehrplanPLUS M10 3 verlangt die Wirkung von a, b, c und d bei
# a · sin(b · (x + c)) + d und das Zurückführen von Winkeln über 2π und negativer Winkel auf 0 bis 2π.
# Neue Lernkarte „verschiebung_x“ nach „parameter“; „zuordnen“ um Übungen mit c erweitert; „periode“ um einen Schritt und Übungen zu
# beliebigen Winkeln. Läuft ganz am Ende (eigener Zufallsstart, nur zum Mischen der Antworten); alle alten Aufgaben bleiben gleich.
# Prüfungsvorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Abitur Bayern Prüfungsteil A (Term einer Sinusfunktion aus Eigenschaften),
# Grundwissen G9 Jgst. 10 bayerischer Gymnasien (allgemeine Sinusfunktion a · sin(b(x + c)) + d beschreiben, Werte beliebiger Winkel ohne Rechner),
# Modellierungsaufgaben Gezeiten/Temperatur mit Phasenverschiebung.
def _bterm(T, form='faktor', name='f(x) = '):
    """T = (art, a, b, c, d): a · art(b · (x + c·π)) + d als Text (x im Bogenmaß)."""
    art, a, b, c, d = T
    c = Fr(c)
    af = '' if a == 1 else '−' if a == -1 else dz(a) + ' · '
    pm = lambda q: ('+ ' if q > 0 else '− ') + pi_text(abs(q))  # noqa: E731
    if b == 1:
        innen = 'x' + (f' {pm(c)}' if c else '')
    elif form == 'ausmult':
        innen = f'{dz(b)}x' + (f' {pm(b * c)}' if c else '')
    else:
        innen = f'{dz(b)} · (x {pm(c)})' if c else f'{dz(b)}x'
    t = f'{name}{af}{art}({innen})'
    if d: t += f' {plus(d)}'
    return t


def _bwert(T, x):
    art, a, b, c, d = T
    u = float(b) * (x + float(c) * PI)
    return float(a) * (math.sin(u) if art == 'sin' else math.cos(u)) + float(d)


def _bgleich(T1, T2):
    return all(abs(_bwert(T1, k / 7) - _bwert(T2, k / 7)) < 1e-9 for k in range(-60, 61))


def _bgraph(T, **kw):
    art, a, b, c, d = T
    g = {'art': art, 'a': zahlwert_json(a), 'b': zahlwert_json(b), 'c': round(float(b * Fr(c)) * PI, 6), 'd': zahlwert_json(d), 'bogen': True}
    g.update(kw)
    return g


def _bbild(Ts, x1=2, y=None, **kw):
    return koord([_bgraph(T) for T in Ts], x=(0, round(x1 * PI, 4)), y=y, pi=True, schritt_y=1, streckung=1.4, **kw)


_KREIS_SCHRITT = {'typ': 'koordinaten', 'x': [-1.5, 1.5], 'y': [-1.5, 1.5], 'grad': False, 'pi': False, 'schritt_x': 0.5, 'schritt_y': 0.5,
                  'streckung': None, 'graphen': [], 'senkrecht': [], 'kreise': [{'m': [0, 0], 'r': 1}]}

KARTE_VERSCHIEBUNG = {
    'lernziel': 'verschiebung_x', 'titel': 'Verschiebung in x-Richtung',
    'einstieg': 'Zwei Gondeln fahren im selben Riesenrad, B eine Viertelrunde hinter A. B erreicht jede Höhe etwas später. '
                'Ihre Höhenkurve ist dieselbe, nur zur Seite geschoben: eine ⟦Verschiebung in x-Richtung⟧.',
    'woerter': [['Verschiebung in x-Richtung', 'der ganze Graph rutscht nach links oder nach rechts, seine Form bleibt'],
                ['c', 'die Zahl in der Klammer bei sin(x + c); sie gibt an, wie weit der Graph rutscht']],
    'bild': _bbild([('sin', 1, 1, 0, 0)], y=(-1.5, 1.5)) | {'schritt_y': 0.5, 'graphen': [_bgraph(('sin', 1, 1, 0, 0), name='sin x', name_x=round(PI * 1.2, 4))]},
    'schritte': [
        {'text': 'Bei f(x) = sin(x − π/2) ist die Klammer erst bei x = π/2 null.',
         'bild': {'graphen': [_bgraph(('sin', 1, 1, 0, 0), name='sin x', name_x=round(PI * 1.2, 4)), _bgraph(('sin', 1, 1, Fr(-1, 2), 0), name='f', name_x=round(PI * 1.75, 4))],
                  'punkte': [{'x': 0, 'y': 0, 'name': 'Start'}, {'x': round(PI / 2, 4), 'y': 0, 'name': 'Start f'}]}},
        {'text': 'Jeder Wert von sin x kommt bei f um π/2 später: ⟦Verschiebung nach rechts⟧.',
         'bild': {'punkte': [{'x': round(PI / 2, 4), 'y': 1, 'name': 'Hoch'}, {'x': round(PI, 4), 'y': 1, 'name': 'Hoch f'}],
                  'pfeile': [[round(PI / 2, 4), 1, round(PI, 4), 1, '']]}},
        {'text': 'Bei sin(x + π/2) kommt alles früher: Der Graph rückt ⟦nach links⟧.',
         'bild': {'graphen': [_bgraph(('sin', 1, 1, 0, 0), name='sin x', name_x=round(PI * 1.2, 4)), _bgraph(('sin', 1, 1, Fr(1, 2), 0), name='g', name_x=round(PI * 0.8, 4))],
                  'punkte': [{'x': round(PI / 2, 4), 'y': 1, 'name': 'Hoch'}, {'x': 0, 'y': 1, 'name': 'Hoch neu'}], 'pfeile': [[round(PI / 2, 4), 1, 0, 1, '']]}},
        {'text': 'Rückwärts: Startet die Kurve steigend bei π/4, ist c = −π/4: ⟦sin(x − π/4)⟧.',
         'bild': {'graphen': [_bgraph(('sin', 1, 1, Fr(-1, 4), 0), name='f', name_x=round(PI * 1.9, 4))], 'pfeile': [],
                  'punkte': [{'x': round(PI / 4, 4), 'y': 0, 'name': 'π/4'}]}}],
    'fehler': 'Bei sin(x − π/2) nach links zu schieben ist falsch. Gondel B kommt später dran, nicht früher: Minus heißt ⟦nach rechts⟧.',
    'fehler_bild': {'graphen': [_bgraph(('sin', 1, 1, Fr(-1, 2), 0), name='richtig', name_x=round(PI * 1.75, 4)),
                                _bgraph(('sin', 1, 1, Fr(1, 2), 0), name='falsch', name_x=round(PI * 0.8, 4))], 'punkte': [], 'pfeile': []},
    'regel': 'Bei sin(x + c) wird der Graph um c verschoben. ⟦Plus: nach links⟧, Minus: nach rechts. Vorher b ausklammern.'}


def luecken_kl10():
    """Liefert (neue Karte mit Aufgaben, Übungen für „zuordnen“, neuer Schritt und Übungen für „periode“)."""
    start(18010)
    V, Z, P = [], [], []

    def neu(liste, p, s, a):
        assert a is not None, 'zu wenige verschiedene Antworten'
        a['p'], a['s'] = p, s
        liste.append(a)

    def pq(text, q, w, h):
        q = Fr(q)
        return luecken(text, '□/□ · π', 'Bruch vor π (gekürzt)', [q.numerator, q.denominator], w, h, c=[str(q.numerator), str(q.denominator)])

    def richt(c):
        return 'nach links' if c > 0 else 'nach rechts'

    def richtung(T, form='faktor', grund=None):
        """Um wie viel und wohin ist a · art(b(x + c)) + d gegenüber a · art(bx) + d verschoben?"""
        art, a, b, c, d = T
        c = Fr(c)
        ohne = _bterm((art, a, b, 0, d), name='')
        richtig = f'um {pi_text(abs(c))} {richt(c)}'
        falsch = [f'um {pi_text(abs(c))} {richt(-c)}']
        if b != 1:
            falsch += [f'um {pi_text(abs(b * c))} {richt(c)}', f'um {pi_text(abs(b * c))} {richt(-c)}']
        else:
            falsch += [f'um {pi_text(abs(c))} nach {"oben" if c > 0 else "unten"}', f'um {pi_text(2 * abs(c))} {richt(c)}']
        if form == 'ausmult':
            w = f'Ausklammern: {_bterm(T, "ausmult", "")} = {_bterm(T, "faktor", "")}. Also c = {pi_text(c)}: {richtig}.'
        else:
            w = f'In der Klammer steht x {"+" if c > 0 else "−"} {pi_text(abs(c))}. {"Plus" if c > 0 else "Minus"} heißt {richt(c)}: {richtig}.'
        return auswahl(f'Um wie viel und in welche Richtung ist der Graph von {_bterm(T, form)} gegenüber dem Graphen von y = {ohne} verschoben?',
                       richtig, falsch, w, grund or ('Klammere zuerst den Faktor vor x aus.' if form == 'ausmult' else 'Plus in der Klammer heißt nach links, Minus nach rechts.'))

    def term_aus_text(art, c, d, a=1):
        T = (art, a, 1, Fr(c), d)
        txt = f'Der Graph von {"" if a == 1 else dz(a) + " · "}{art} x wird um {pi_text(abs(Fr(c)))} {richt(Fr(c))}'
        if d: txt += f' und um {dz(abs(d))} nach {"oben" if d > 0 else "unten"}'
        txt += ' verschoben. Welcher Term gehört zum neuen Graphen?'
        kand = [(art, a, 1, -Fr(c), d), (art, a, 1, Fr(c), -d) if d else (art, a, 1, 2 * Fr(c), 0), ('cos' if art == 'sin' else 'sin', a, 1, Fr(c), d)]
        falsch = [_bterm(k, name='') for k in kand if not _bgleich(k, T)]
        # „verschoben um c nach oben statt in x-Richtung“: c außerhalb der Klammer
        falsch.append(f'{"" if a == 1 else dz(a) + " · "}{art}(x) {"+" if Fr(c) > 0 else "−"} {pi_text(abs(Fr(c)))}' + (f' {plus(d)}' if d else ''))
        return auswahl(txt, _bterm(T, name=''), falsch[:3],
                       f'Nach {"links" if Fr(c) > 0 else "rechts"} um {pi_text(abs(Fr(c)))}: x {"+" if Fr(c) > 0 else "−"} {pi_text(abs(Fr(c)))} in die Klammer'
                       + (f'; {"nach oben" if d > 0 else "nach unten"} um {dz(abs(d))}: {plus(d)} am Ende.' if d else '.'),
                       'Verschiebung in x-Richtung: in die Klammer. Verschiebung nach oben/unten: ans Ende.')

    def graph_auswahl(T, kand, w, h):
        falsch = []
        for k in kand:
            if _bgleich(k, T) or any(_bgleich(k, f) for f in falsch): continue
            falsch.append(k)
        assert len(falsch) >= 3, T
        a_ = auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen (x im Bogenmaß)?', _bterm(T, name=''), [_bterm(k, name='') for k in falsch[:3]], w, h)
        art, a, b, c, d = T
        lo, hi = d - abs(a), d + abs(a)
        return mit_grafik(a_, _bbild([T], y=(math.floor(min(lo, 0) - 1), math.ceil(max(hi, 0) + 1))))

    def hochpunkt(T):
        """Erster Hochpunkt in [0; 2π[ von a · art(x + c) + d (b = 1, a > 0)."""
        art, a, b, c, d = T
        assert b == 1 and a > 0
        basis = Fr(1, 2) if art == 'sin' else Fr(0)
        x = (basis - Fr(c)) % 2
        return luecken(f'Bestimme den ersten Hochpunkt von {_bterm(T)} im Intervall [0; 2π[.', 'H(□/□ · π | □)', 'Stelle als Bruch vor π, dann der y-Wert',
                       [x.numerator, x.denominator, a + d],
                       f'{art} ist am größten, wenn die Klammer {pi_text(basis) if basis else "0"} ist: x {"+" if Fr(c) > 0 else "−"} {pi_text(abs(Fr(c)))} = {pi_text(basis) if basis else "0"} ⇒ x = {pi_text(x)}. '
                       f'y = {dz(a)} · 1 {plus(d)} = {dz(a + d)}.',
                       f'{art} hat sein Maximum, wenn die Klammer {pi_text(basis) if basis else "0"} ist.',
                       c=[str(x.numerator), str(x.denominator), f'{a} + ({d})'])

    def wertemenge(T):
        art, a, b, c, d = T
        lo, hi = d - abs(a), d + abs(a)
        return luecken(f'Gib die Wertemenge von {_bterm(T)} an.', 'W = [□; □]', 'kleinster und größter Wert', [lo, hi],
                       f'Die Verschiebung in x-Richtung ändert die Werte nicht. Amplitude {abs(a)}, Mittellinie y = {dz(d)}: W = [{dz(lo)}; {dz(hi)}].',
                       'Ändert eine Verschiebung nach links oder rechts den größten und kleinsten Wert?', c=[f'{d} - {abs(a)}', f'{d} + {abs(a)}'])

    def nullstelle(T):
        """kleinste positive Nullstelle von art(b(x + c)) (sin)."""
        art, a, b, c, d = T
        assert art == 'sin' and d == 0
        k = 0
        while True:
            x = Fr(k, b) - Fr(c)
            if x > 0: break
            k += 1
        return pq(f'Bestimme die kleinste positive Nullstelle von {_bterm(T)}.', x,
                  f'sin ist 0, wenn die Klammer ein Vielfaches von π ist: {_bterm((art, 1, b, c, 0), name="")[4:-1]} = {pi_text(Fr(k))} ⇒ x = {pi_text(x)}'
                  + (f' (kleinere Vielfache ergeben x ≤ 0).' if k else '.'),
                  'Setze die Klammer gleich 0, π, 2π, … und löse nach x auf.')

    def grad_wert(art, cg, x):
        u = x + cg
        v = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0), 360: (0, 1)}[u % 360 if u % 360 else 0]
        w_ = v[0] if art == 'sin' else v[1]
        return zahl(f'Gegeben ist f(x) = {art}(x {plus(cg)}°). Welchen Wert hat f an der Stelle x = {x}°?',
                    f'f({x}°) = {art}({x}° {plus(cg)}°) = {art}({u}°) = {dz(w_)}.', 'Rechne zuerst die Klammer aus.', w_, str(w_))

    # ===== neue Lernkarte verschiebung_x =====
    # Stufe 1
    neu(V, 'uebung', 1, richtung(('sin', 1, 1, Fr(-1, 4), 0)))
    neu(V, 'uebung', 1, zahl('Um wie viel Grad ist der Graph von f(x) = cos(x + 60°) gegenüber dem Graphen von cos x nach links verschoben?',
                             'In der Klammer steht + 60°. Plus heißt nach links: um 60°.', 'Plus in der Klammer heißt nach links.', 60, '60', einheit='°'))
    T = ('sin', 1, 1, Fr(1, 4), 0)
    neu(V, 'uebung', 1, graph_auswahl(T, [('sin', 1, 1, Fr(-1, 4), 0), ('cos', 1, 1, Fr(1, 4), 0), ('sin', 1, 1, Fr(3, 4), 0), ('sin', 1, 1, 0, 0)],
                                      'Der Hochpunkt liegt bei π/4 statt bei π/2 wie bei sin x. Alles kommt π/4 früher: Verschiebung um π/4 nach links, f(x) = sin(x + π/4).',
                                      'Wo liegt der erste Hochpunkt? Vergleiche mit sin x (Hochpunkt bei π/2).'))
    neu(V, 'uebung', 1, pq('Bestimme die kleinste Stelle x ≥ 0, an der f(x) = sin(x − π/3) den Wert 0 hat.', Fr(1, 3),
                           'Die Klammer ist bei x = π/3 gleich 0, und sin 0 = 0. Kleinere x ≥ 0 geben eine negative Klammer zwischen −π/3 und 0, dort ist sin nicht 0. Also x = π/3.',
                           'Für welches x ist die Klammer gleich 0?'))
    # Stufe 2
    neu(V, 'uebung', 2, richtung(('sin', 1, 2, Fr(-1, 4), 0), 'ausmult'))
    neu(V, 'uebung', 2, term_aus_text('cos', Fr(-1, 3), 0))
    neu(V, 'uebung', 2, hochpunkt(('sin', 2, 1, Fr(-1, 6), 1)))
    neu(V, 'uebung', 2, wertemenge(('cos', 3, 1, Fr(1, 5), -2)))
    T = ('cos', 1, 1, Fr(-1, 4), 1)
    neu(V, 'uebung', 2, graph_auswahl(T, [('cos', 1, 1, Fr(1, 4), 1), ('sin', 1, 1, Fr(-1, 4), 1), ('cos', 1, 1, 0, 1), ('cos', 1, 1, Fr(-1, 4), -1)],
                                      'Mittellinie y = 1, Amplitude 1, Periode 2π. Der höchste Punkt liegt bei π/4 statt bei 0: cos um π/4 nach rechts, f(x) = cos(x − π/4) + 1.',
                                      'cos startet im Hochpunkt. Wo liegt hier der erste Hochpunkt?'))
    neu(V, 'uebung', 2, grad_wert('sin', -30, 120))
    # Stufe 3 – Prüfungsvorbild: Term aus Hoch- und Tiefpunkt (Abitur Bayern, Prüfungsteil A)
    a_, c_, d_ = 2, Fr(1, 4), 3
    xh, xt = c_ + Fr(1, 2), c_ + Fr(3, 2)
    neu(V, 'uebung', 3, luecken(f'Die Funktion f(x) = a · sin(x − c) + d (a > 0, 0 < c < π, x im Bogenmaß) hat den Hochpunkt ({pi_text(xh)} | {d_ + a_}) '
                                f'und den nächsten Tiefpunkt ({pi_text(xt)} | {d_ - a_}). Bestimme a, c und d.', 'a = □; c = □/□ · π; d = □', 'a, c als Bruch vor π, d',
                                [a_, c_.numerator, c_.denominator, d_],
                                f'd = ({d_ + a_} + {d_ - a_}) : 2 = {d_}; a = ({d_ + a_} − {d_ - a_}) : 2 = {a_}. sin ist am größten bei π/2: {pi_text(xh)} − c = π/2 ⇒ c = {pi_text(c_)}. '
                                f'Probe Tiefpunkt: {pi_text(xt)} − {pi_text(c_)} = 3π/2 ✓.',
                                'Mittellinie und Amplitude aus den y-Werten; c aus der Stelle des Hochpunkts (sin ist bei π/2 am größten).',
                                c=[f'({d_ + a_} - {d_ - a_}) // 2', str(c_.numerator), str(c_.denominator), f'({d_ + a_} + {d_ - a_}) // 2']))
    # Stufe 3 – Prüfungsvorbild: Modell Gezeiten mit Verschiebung
    A_, H_, M_ = 2, 4, 3
    neu(V, 'uebung', 3, luecken(f'In einem Hafen ist um {H_} Uhr Hochwasser. Der Wasserstand schwankt zwischen {M_ - A_} m und {M_ + A_} m, von Hochwasser zu Hochwasser vergehen 12 Stunden. '
                                'Ergänze das Modell (t in Stunden nach Mitternacht, h in m).', 'h(t) = □ · cos(π/6 · (t − □)) + □', 'Amplitude, Uhrzeit des Hochwassers, Mittelwert',
                                [A_, H_, M_],
                                f'Mittelwert ({M_ - A_} + {M_ + A_}) : 2 = {M_}, Amplitude {M_ + A_} − {M_} = {A_}. Periode 12 h passt zu π/6, denn 2π : 12 = π/6. '
                                f'cos ist am größten, wenn die Klammer 0 ist: bei t = {H_}. Also h(t) = {A_} · cos(π/6 · (t − {H_})) + {M_}.',
                                'cos hat seinen größten Wert, wenn die Klammer 0 ist. Wann soll das sein?', c=[f'({M_ + A_} - {M_ - A_}) // 2', str(H_), f'({M_ + A_} + {M_ - A_}) // 2']))
    # Stufe 3 – Knobelaufgabe
    neu(V, 'uebung', 3, luecken('Für welche Zahl c mit 0 < c < 2π gilt sin(x + c) = −sin x für jedes x? Gib c als Vielfaches von π an.', 'c = □ · π', 'Zahl vor π', [1],
                                'Um eine halbe Periode verschoben, liegt jeder Hochpunkt dort, wo vorher ein Tiefpunkt war: sin(x + π) = −sin x. Also c = π. Probe x = π/2: sin(3π/2) = −1 = −sin(π/2) ✓.',
                                'Welche Verschiebung macht aus jedem Hochpunkt einen Tiefpunkt?', c=['2 // 2']))
    neu(V, 'uebung', 3, auswahl('Jemand sagt: „Der Graph von f(x) = sin(3x + π) ist gegenüber dem Graphen von sin(3x) um π nach links verschoben.“ Was stimmt?',
                                'Falsch: um π/3 nach links, denn 3x + π = 3 · (x + π/3).',
                                ['Richtig.', 'Falsch: um π nach rechts.', 'Falsch: um 3π nach links.'],
                                'Erst den Faktor 3 ausklammern: sin(3x + π) = sin(3 · (x + π/3)). Die Verschiebung ist π/3 nach links.',
                                'Klammere den Faktor vor x aus. Was steht dann neben x?'))
    neu(V, 'uebung', 3, nullstelle(('sin', 1, 2, Fr(1, 3), 0)))
    neu(V, 'uebung', 3, zahl('Die Temperatur an einem Frühlingstag wird beschrieben durch T(t) = 12 + 5 · sin(π/12 · (t − 10)) (t in Stunden nach Mitternacht, T in °C). '
                             'Um wie viel Uhr ist es am kältesten?',
                             'sin ist am kleinsten (−1), wenn die Klammer −π/2 ist: π/12 · (t − 10) = −π/2 ⇒ t − 10 = −6 ⇒ t = 4. '
                             'Um 4 Uhr ist es am kältesten: T = 12 − 5 = 7 °C.', 'sin hat den Wert −1 bei −π/2 (oder 3π/2). Setze die Klammer gleich diesem Winkel.',
                             4, '10 - 6', einheit='Uhr'))
    T = ('sin', 2, 1, Fr(-1, 4), 1)
    neu(V, 'uebung', 3, graph_auswahl(T, [('sin', 2, 1, Fr(1, 4), 1), ('cos', 2, 1, Fr(-1, 4), 1), ('sin', 2, 1, Fr(-1, 2), 1), ('sin', 1, 1, Fr(-1, 4), 2)],
                                      'Mittellinie y = 1 (Mitte zwischen −1 und 3), Amplitude 2. Steigend durch die Mittellinie bei π/4: sin um π/4 nach rechts, f(x) = 2 · sin(x − π/4) + 1.',
                                      'Lies Mittellinie und Amplitude ab. Wo kreuzt der Graph die Mittellinie steigend?'))
    T1 = ('sin', 1, 2, Fr(-1, 6), 0)
    neu(V, 'uebung', 3, auswahl('Der Graph von sin x wird zuerst um π/3 nach rechts verschoben und danach in x-Richtung auf die Hälfte gestaucht (Periode π). Welcher Term gehört dazu?',
                                _bterm(T1, 'ausmult', ''), [_bterm(('sin', 1, 2, Fr(-1, 3), 0), 'faktor', ''), _bterm(('sin', 1, 2, Fr(1, 6), 0), 'ausmult', ''), 'sin(0,5x − π/3)'],
                                'Nach dem Verschieben: sin(x − π/3). Stauchen heißt, x durch 2x zu ersetzen: sin(2x − π/3) = sin(2 · (x − π/6)). '
                                'Das Stauchen halbiert auch die Verschiebung.',
                                'Beim Stauchen wird jedes x durch 2x ersetzt – auch das x in der Klammer.'))
    # Test, Korrektur, Sicherung (ohne Tipp, Stufe 2)
    neu(V, 'test', 2, richtung(('sin', 1, 1, Fr(1, 6), 0)))
    neu(V, 'korrektur', 2, richtung(('cos', 1, 3, Fr(-1, 3), 0), 'ausmult'))
    neu(V, 'korrektur', 2, term_aus_text('sin', Fr(1, 4), 2))
    neu(V, 'korrektur', 2, hochpunkt(('cos', 3, 1, Fr(-1, 3), -1)))
    neu(V, 'sicherung', 2, richtung(('cos', 1, 1, Fr(-2, 3), 0)))
    neu(V, 'sicherung', 2, zahl('Um wie viel Grad ist der Graph von f(x) = sin(x − 45°) gegenüber dem Graphen von sin x nach rechts verschoben?',
                                'In der Klammer steht − 45°. Minus heißt nach rechts: um 45°.', 'Minus in der Klammer heißt nach rechts.', 45, '45', einheit='°'))
    neu(V, 'sicherung', 2, nullstelle(('sin', 1, 1, Fr(1, 4), 0)))
    neu(V, 'sicherung', 2, wertemenge(('sin', 2, 1, Fr(-1, 7), 4)))
    neu(V, 'sicherung', 2, term_aus_text('cos', Fr(-1, 6), -1))
    neu(V, 'sicherung', 2, grad_wert('cos', 30, 150))

    # ===== zuordnen: Übungen mit Verschiebung c =====
    T = ('sin', 1, 1, Fr(-1, 3), 0)
    neu(Z, 'uebung', 1, graph_auswahl(T, [('sin', 1, 1, Fr(1, 3), 0), ('cos', 1, 1, Fr(-1, 3), 0), ('sin', 1, 1, 0, 0), ('sin', 1, 1, Fr(-2, 3), 0)],
                                      'Der Graph kreuzt die x-Achse steigend bei π/3 statt bei 0: sin um π/3 nach rechts, f(x) = sin(x − π/3).',
                                      'Wo beginnt eine Schwingung (steigend auf der Mittellinie)?'))
    T = ('cos', 2, 1, Fr(1, 3), 0)
    neu(Z, 'uebung', 2, graph_auswahl(T, [('cos', 2, 1, Fr(-1, 3), 0), ('sin', 2, 1, Fr(1, 3), 0), ('cos', 1, 1, Fr(1, 3), 0), ('cos', 2, 1, Fr(2, 3), 0)],
                                      'Amplitude 2. Der Hochpunkt, den cos bei 0 hat, liegt hier bei −π/3 (der nächste bei 5π/3): cos um π/3 nach links, f(x) = 2 · cos(x + π/3).',
                                      'cos hat bei 0 einen Hochpunkt. Wo liegt hier der Hochpunkt, der 0 am nächsten ist?'))
    T = ('sin', 3, 1, Fr(-1, 6), 1)
    xh = Fr(1, 2) + Fr(1, 6)
    g = _bbild([T], y=(-3, 5)) | {'punkte': [{'x': round(float(xh) * PI, 4), 'y': 4, 'name': 'H(2π/3 | 4)'}]}
    neu(Z, 'uebung', 2, mit_grafik(luecken('Der Graph gehört zu f(x) = a · sin(x − c) + d mit a > 0 und 0 < c < π. Bestimme a, c und d.', 'a = □; c = □/□ · π; d = □',
                                           'a, c als Bruch vor π, d', [3, 1, 6, 1],
                                           'Größter Wert 4, kleinster −2: d = (4 + (−2)) : 2 = 1, a = (4 − (−2)) : 2 = 3. sin ist bei π/2 am größten: 2π/3 − c = π/2 ⇒ c = π/6.',
                                           'Mittellinie und Amplitude aus größtem und kleinstem Wert; c aus der Lage des Hochpunkts.',
                                           c=['(4 - (-2)) // 2', '1', '6', '(4 + (-2)) // 2']), g))
    T = ('cos', 2, 2, Fr(-1, 3), 1)
    g = _bbild([T], y=(-2, 4)) | {'punkte': [{'x': round(PI / 3, 4), 'y': 3, 'name': 'H(π/3 | 3)'}]}
    neu(Z, 'uebung', 3, mit_grafik(luecken('Der Graph gehört zu f(x) = a · cos(b · (x − c)) + d mit a > 0, b > 0 und 0 < c < π/2. Bestimme a, b, c und d.',
                                           'a = □; b = □; c = □/□ · π; d = □', 'a, b, c als Bruch vor π, d', [2, 2, 1, 3, 1],
                                           'Werte von −1 bis 3: d = 1, a = 2. Von Hochpunkt zu Hochpunkt ist es π: b = 2π : π = 2. cos hat bei 0 einen Hochpunkt, hier liegt er bei π/3: c = π/3.',
                                           'Periode von Hochpunkt zu Hochpunkt ablesen; c ist die Stelle des Hochpunkts.',
                                           c=['(3 - (-1)) // 2', '2 // 1', '1', '3', '(3 + (-1)) // 2']), g))
    neu(Z, 'uebung', 3, auswahl('Eine Kurve startet bei x = π/3 steigend auf der Mittellinie y = 0, hat die Amplitude 1 und die Periode π. Jemand schreibt dafür f(x) = sin(2x − π/3). Was stimmt?',
                                'Falsch: Richtig ist sin(2 · (x − π/3)) = sin(2x − 2π/3).',
                                ['Richtig.', 'Falsch: Richtig ist sin(2x + π/3).', 'Falsch: Richtig ist sin(0,5x − π/3).'],
                                'Periode π ⇒ b = 2. Start bei π/3 ⇒ x − π/3 in der Klammer, danach erst mal 2: sin(2 · (x − π/3)). Bei sin(2x − π/3) läge der Start bei π/6.',
                                'Setze x = π/3 in sin(2x − π/3) ein. Ist die Klammer dann 0?'))
    neu(Z, 'uebung', 3, auswahl('Welcher Term beschreibt denselben Graphen wie f(x) = cos(x − π/2)?', 'sin(x)', ['−sin(x)', 'cos(x) − π/2', '−cos(x)'],
                                'cos startet im Hochpunkt bei 0; um π/2 nach rechts liegt der Hochpunkt bei π/2. Dort hat auch sin x seinen Hochpunkt, und bei 0 sind beide 0: f(x) = sin x.',
                                'Setze x = 0 und x = π/2 ein und vergleiche mit den Angeboten.'))

    # ===== periode: beliebige Winkel =====
    schritt = {'text': 'Volle Runden zählen nicht: 9π/4 wirkt wie π/4, −π/2 wie 3π/2.',
               'bild': _KREIS_SCHRITT | {'strecken': [[0, 0, 0.7071, 0.7071], [0, 0, 0, -1]],
                                         'punkte': [{'x': 0.7071, 'y': 0.7071, 'name': '9π/4'}, {'x': 0, 'y': -1, 'name': '−π/2'}]}}

    def wert_beliebig(f, q, p='uebung', s=1):
        q = Fr(q)
        r = q % 2
        g = int(r * 180)
        v = {0: (0, 1), 30: (Fr(1, 2), None), 90: (1, 0), 150: (Fr(1, 2), None), 180: (0, -1), 210: (Fr(-1, 2), None), 270: (-1, 0), 330: (Fr(-1, 2), None),
             60: (None, Fr(1, 2)), 120: (None, Fr(-1, 2)), 240: (None, Fr(-1, 2)), 300: (None, Fr(1, 2))}[g]
        w_ = v[0] if f == 'sin' else v[1]
        assert w_ is not None
        runden = (q - r) / 2
        return zahl(f'Gib den exakten Wert von {f}({pi_text(q)}) an.',
                    f'{pi_text(q)} {"−" if runden > 0 else "+"} {pi_text(abs(runden) * 2)} = {pi_text(r)} ({"volle Runde" if abs(runden) == 1 else f"{dz(abs(runden))} volle Runden"} '
                    f'{"weg" if runden > 0 else "dazu"}). {f}({pi_text(r)}) = {f} {g}° = {dz(w_)}.',
                    'Zähle volle Runden (2π) weg oder dazu, bis der Winkel zwischen 0 und 2π liegt.', w_, cf_(w_))

    neu(P, 'uebung', 1, wert_beliebig('sin', Fr(5, 2)))
    neu(P, 'uebung', 2, wert_beliebig('cos', Fr(-1, 3)))
    neu(P, 'uebung', 2, pq('Gib den Winkel zwischen 0 und 2π an, der am Einheitskreis zum selben Punkt gehört wie −3π/4.', Fr(5, 4),
                           '−3π/4 + 2π = −3π/4 + 8π/4 = 5π/4.', 'Ein negativer Winkel dreht im Uhrzeigersinn. Zähle eine volle Runde 2π dazu.'))
    neu(P, 'uebung', 3, wert_beliebig('sin', Fr(-17, 6)))
    q1, q2 = Fr(100), Fr(-101, 2)
    r2 = q2 % 2
    neu(P, 'uebung', 3, zahl('Berechne ohne Taschenrechner: cos(100π) + sin(−101π/2).',
                             f'100π sind 50 volle Runden: cos(100π) = cos 0 = 1. −101π/2 + 52π = {pi_text(r2)}: sin({pi_text(r2)}) = −1. Summe: 1 + (−1) = 0.',
                             'Führe beide Winkel durch volle Runden (2π) auf 0 bis 2π zurück.', 0, '1 + (-1)'))
    neu(P, 'uebung', 3, auswahl('Welche Aussage gilt für jedes x?', 'cos(x − 2π) = cos x', ['sin(x + π) = sin x', 'sin(−x) = sin x', 'cos(x + π) = cos x'],
                                'Eine volle Runde rückwärts (−2π) führt zum selben Punkt: cos(x − 2π) = cos x. Eine halbe Runde (π) wechselt das Vorzeichen, und sin(−x) = −sin x.',
                                'Prüfe jede Aussage mit x = π/2 oder x = 0.'))
    return V, Z, (schritt, P)


def luecken_einbauen():
    from _luecken_kl10 import karte_einfuegen, karte_erweitern, offen_ergaenzen
    V, Z, (schritt, P) = luecken_kl10()
    karte_einfuegen('funktionen.trig', KARTE_VERSCHIEBUNG, 'parameter', V)
    karte_erweitern('funktionen.trig', 'zuordnen', [], Z,
                    felder={'regel': 'Lies Mittellinie, Amplitude und Periode ab. Start auf der Mittellinie: ⟦sin⟧. Start ganz oben: cos. b = 2π : p. Start verschoben? Dann c ablesen.'})
    karte_erweitern('funktionen.trig', 'periode', [schritt], P)
    offen_ergaenzen('funktionen.trig', 'Achtzehnte Runde (luecken-kl10): neue Lernkarte „verschiebung_x“ (Parameter c, LehrplanPLUS M10 3) nach „parameter“; '
                    '„zuordnen“ um Übungen mit c erweitert (Merksatz um „Start verschoben? Dann c ablesen.“ ergänzt); „periode“ um einen Schritt '
                    '(Winkel über 2π und negative Winkel am Einheitskreis) und Übungen ergänzt. Der Eintrag „Verschiebung in x-Richtung: … keine eigene Lernkarte“ ist damit überholt.')


if __name__ == '__main__':
    datei = bauen('funktionen.trig',
          'Sinus- und Kosinusfunktion mit Grad- und Bogenmaß beschreiben, Periode, Amplitude und Verschiebung deuten, Graph und Term zuordnen und periodische Vorgänge modellieren.',
          ['360° = 2π; x = α · π/180°.', 'sin und cos haben die Periode 360° = 2π; sin(b · x) hat die Periode 360° : b.',
           'f(x) = a · sin(b · x) + d: Amplitude |a|, Mittellinie y = d, Wertemenge [d − |a|; d + |a|].', 'sin: Nullstellen k · 180°, punktsymmetrisch; cos: Nullstellen 90° + k · 180°, achsensymmetrisch.'],
          [('Bogenmaß und Werte', ['bogenmass', 'werte']), ('Parameter', ['periode', 'parameter', 'zuordnen']), ('Eigenschaften und Anwendung', ['eigenschaften', 'anwendung'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'bogenmass': ['Gib 60° im Bogenmaß'], 'werte': ['sin(5π/6)'], 'periode': ['f(x) = sin(3x)?'], 'parameter': ['f(x) = 3 · sin(x) + 1'],
                  'anwendung': ['h(t) = 20 − 18 · cos(30° · t) (t in Minuten, h in m). Wie hoch ist sie nach 4 min']},
          offen=['Zeichnungen: Graphen in den Lernkarten „werte“, „periode“, „parameter“, „zuordnen“, „eigenschaften“, „anwendung“; Aufgaben „Graph und Term zuordnen“, „Periode ablesen“, „Amplitude ablesen“ zeigen den Graphen. Bogenmaß (Fünfzehnte Runde): Die Lernkarten führen nach dem Gradmaß-Einstieg das Bogenmaß mit (Graphen mit π-Achse, pi: true); je Lernkarte 8 Übungen im Bogenmaß. Die älteren Aufgaben-Graphen bleiben in Grad beschriftet.',
                 'Verschiebung in x-Richtung: nach der Prüfung als Zuordnungsaufgabe mit Zeichnung (Stufe 3, „zuordnen“) aufgenommen; keine eigene Lernkarte.',
                 'Prüfung eingearbeitet (Runde 3): Bogenlänge, exakte Werte mit Wurzeln (½√2, ½√3), Vorzeichen ohne Rechner, Term aus Kennwerten, Verschiebung in x-Richtung, Riesenrad-Modell aus Sachangaben, Zeitpunkt bestimmen, Gezeiten. Ganzzahlige Vielfache von π als „□ · π“. Zuordnen: kein Graph doppelt je Stufe, gleichwertige Terme nie zusammen als Optionen.',
                 'Rechenausdruck c: Sinus/Kosinus-Werte als 12-stellige Konstanten mit Toleranz.'])
    ergaenzen(datei, schwer())
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    nacharbeit_anhaengen('funktionen.trig', nacharbeit())  # Fünfzehnte Runde: Bogenmaß-Übungen, ganz am Ende
    luecken_einbauen()  # Achtzehnte Runde (luecken-kl10): neue Karte verschiebung_x, zuordnen und periode erweitert – ganz am Ende
