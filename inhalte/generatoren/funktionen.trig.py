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


def g_bogenmass(s):
    if s == 1:
        g = R.choice(list(GRAD_PI))
        q = GRAD_PI[g]
        return luecken(f'Gib {g}° im Bogenmaß als Vielfaches von π an.', '□/□ · π', 'Bruch vor π (gekürzt; bei ganzen Zahlen Nenner 1)', [q.numerator, q.denominator],
                       f'{g}° · π/180° = {br(Fr(g, 180))} · π = {pi_text(q)}.', 'Teile den Winkel durch 180° und kürze.',
                       c=[f'{g} // {math.gcd(g, 180)}', f'180 // {math.gcd(g, 180)}'])
    if s == 2:
        g = R.choice(list(GRAD_PI))
        q = GRAD_PI[g]
        return zahl(f'Wie viel Grad sind {pi_text(q)}?', f'{pi_text(q)} · 180°/π = {br(q)} · 180° = {g}°.', 'Ersetze π durch 180°.', g, f'{q.numerator} * 180 / {q.denominator}', einheit='°')
    if R.random() < 0.5:
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


def g_werte(s):
    if s == 1 or (s == 2 and R.random() < 0.5):
        g = R.choice([k for k in EXAKT if k not in (0, 360)] if s == 2 else [30, 90, 180, 270, 60])
        sn, cs = EXAKT[g]
        f, v = ('sin', sn) if sn is not None else ('cos', cs)
        if sn is not None and cs is not None and R.random() < 0.5: f, v = 'cos', cs
        q = GRAD_PI[g]
        return zahl(f'Gib den exakten Wert von {f}({pi_text(q)}) an.', f'{pi_text(q)} = {g}°; {f} {g}° = {dz(v)}.',
                    'Rechne zuerst ins Gradmaß um und denke an den Einheitskreis.', v, cf_(v))
    x = Fr(R.randint(1, 60), 10)
    f = R.choice(['sin', 'cos'])
    w = (math.sin if f == 'sin' else math.cos)(float(x))
    v = gerundet(w, 3)
    if v is None: return None
    return zahl(f'Berechne {f}({dz(x)}) (x im Bogenmaß) auf drei Nachkommastellen.', f'Taschenrechner im RAD-Modus: {f}({dz(x)}) ≈ {dz(v)}.',
                'Stelle den Taschenrechner auf Bogenmaß (RAD).', v, f'round({K(w)}, 3)', tol=0.001)


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
            return luecken(f'Welche Periode hat f(x) = {fterm(f, b=b)} im Bogenmaß? Gib sie als Vielfaches von π an.', '□/□ · π',
                           'Bruch vor π (gekürzt; bei ganzen Zahlen Nenner 1)', [q.numerator, q.denominator],
                           f'p = 2π : {dz(b) if endlich(b) else br(b)} = {pi_text(q)}.', 'Periode = 2π geteilt durch b.', c=[f'{q.numerator}', f'{q.denominator}'])
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


def g_zuordnen(s):
    f = R.choice(['sin', 'cos'])
    a = R.choice([1, 2, 3]) if s < 3 else R.choice([1, 2, 3, -1, -2])
    b = R.choice([1, 2, Fr(1, 2)]) if s > 1 else 1
    d = 0 if s == 1 else R.choice([0, 0, 1, -1, 2])
    if s == 1 and a == 1: a = R.choice([2, 3])
    richtig = 'f(x) = ' + fterm(f, a, b, d)
    andere = ['f(x) = ' + fterm('cos' if f == 'sin' else 'sin', a, b, d),
              'f(x) = ' + fterm(f, b if isinstance(b, int) and b != a else a + 1, a if isinstance(b, int) and b != a else b, d),
              'f(x) = ' + fterm(f, a, b, -d) if d else 'f(x) = ' + fterm(f, a, b, a),
              'f(x) = ' + fterm(f, -a, b, d)]
    R.shuffle(andere)
    p = Fr(360) / b
    a_ = auswahl('Welcher Funktionsterm gehört zum gezeichneten Graphen (x in Grad)?', richtig, andere,
                 f'Mittellinie y = {dz(d)}, Amplitude {abs(a)}, Periode {dz(p)}° (b = {dz(b)}), Start bei x = 0 {"auf der Mittellinie" if f == "sin" else "im Maximum" if a > 0 else "im Minimum"}{" fallend" if f == "sin" and a < 0 else ""}: {richtig}.',
                 'Lies Mittellinie, Amplitude und Periode ab. Wo beginnt der Graph bei x = 0?')
    return mit_grafik(a_, bild([graph(f, a, b, d)], x=(0, 360)))


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


def g_anwendung(s):
    if s == 1:
        d, a, T = R.choice([(20, 18, 12), (30, 25, 20), (15, 12, 8), (60, 55, 30), (10, 8, 6)])
        t = R.choice([0, T // 2, T // 4, 3 * T // 4, T])
        h = d - a * round(math.cos(math.radians(360 / T * t)))
        return zahl(f'Die Höhe einer Riesenradgondel ist h(t) = {d} − {a} · cos({dz(Fr(360, T))}° · t) (t in Minuten, h in m). Wie hoch ist sie nach {t} min?',
                    f'h({t}) = {d} − {a} · cos({dz(Fr(360, T) * t)}°) = {dz(h)} m.', 'Setze t ein; cos 0° = 1, cos 90° = 0, cos 180° = −1.', h,
                    f'{d} - {a} * {round(math.cos(math.radians(360 / T * t)))}', einheit='m')
    if s == 2:
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
    if typ < 0.5:
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


GEN = schoen({'bogenmass': g_bogenmass, 'werte': g_werte, 'periode': g_periode, 'parameter': g_parameter, 'zuordnen': g_zuordnen,
              'eigenschaften': g_eigenschaften, 'anwendung': g_anwendung})

if __name__ == '__main__':
    bauen('funktionen.trig',
          'Sinus- und Kosinusfunktion mit Grad- und Bogenmaß beschreiben, Periode, Amplitude und Verschiebung deuten, Graph und Term zuordnen und periodische Vorgänge modellieren.',
          ['360° = 2π; x = α · π/180°.', 'sin und cos haben die Periode 360° = 2π; sin(b · x) hat die Periode 360° : b.',
           'f(x) = a · sin(b · x) + d: Amplitude |a|, Mittellinie y = d, Wertemenge [d − |a|; d + |a|].', 'sin: Nullstellen k · 180°, punktsymmetrisch; cos: Nullstellen 90° + k · 180°, achsensymmetrisch.'],
          [('Bogenmaß und Werte', ['bogenmass', 'werte']), ('Parameter', ['periode', 'parameter', 'zuordnen']), ('Eigenschaften und Anwendung', ['eigenschaften', 'anwendung'])],
          ETAPPEN, GEN,
          meiden={'bogenmass': ['Gib 60° im Bogenmaß'], 'werte': ['sin(5π/6)'], 'periode': ['f(x) = sin(3x)?'], 'parameter': ['f(x) = 3 · sin(x) + 1'],
                  'anwendung': ['h(t) = 20 − 18 · cos(30° · t) (t in Minuten, h in m). Wie hoch ist sie nach 4 min']},
          offen=['Zeichnungen: Graphen in den Lernkarten „werte“, „periode“, „parameter“, „zuordnen“, „eigenschaften“, „anwendung“; Aufgaben „Graph und Term zuordnen“, „Periode ablesen“, „Amplitude ablesen“ zeigen den Graphen. Die x-Achse ist in Grad beschriftet (grad: true), weil π-Beschriftungen nicht möglich sind; Bogenmaß wird über Umrechnung geübt.',
                 'Verschiebung in x-Richtung (Parameter c) ist nicht enthalten: lehrplan_gym nennt nur „Sinus- und Kosinusfunktion“; a, b und d decken die Wirkung der Parameter ab. Bitte bei der Prüfung bestätigen.',
                 'Rechenausdruck c: Sinus/Kosinus-Werte als 12-stellige Konstanten mit Toleranz.'])
