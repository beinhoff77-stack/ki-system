#!/usr/bin/env python3
"""Thema raum.pyramide_kegel_kugel – Pyramide, Kegel, Kugel (Klasse 10)."""
import math
import sys
from math import isqrt, pi, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403

start(1006)
PI = K(pi)
TRIPEL = sorted({(a, b, isqrt(a * a + b * b)) for a in range(1, 30) for b in range(1, 30) if isqrt(a * a + b * b) ** 2 == a * a + b * b and a != b})


def cf(x):
    x = Fr(x)
    return str(int(x)) if x.denominator == 1 else str(float(x)) if endlich(x) else f'({x.numerator}/{x.denominator})'


# ---------- Figuren ----------
def kegel_schnitt(r, h, s=None, lr='r', lh='h', ls='s'):
    """Achsenschnitt eines Kegels (gleichschenkliges Dreieck) mit Beschriftung."""
    return {'typ': 'figur', 'punkte': {'S': [0, h], 'A': [-r, 0], 'B': [r, 0], 'M': [0, 0]}, 'flaeche': ['A', 'B', 'S'],
            'linien': [['A', 'B', ''], ['A', 'S', ''], ['B', 'S', ls], ['M', 'B', lr], ['M', 'S', lh, 'gestrichelt']],
            'rechter_winkel': [['M', 'B', 'S']], 'label': 'Achsenschnitt eines Kegels'}


def pyr_schnitt(a, h, lh='h', la='a/2', ls='hₛ'):
    """Dreieck aus Höhe h, halber Grundkante und Seitenhöhe hₛ einer quadratischen Pyramide."""
    return {'typ': 'figur', 'punkte': {'S': [0, h], 'M': [0, 0], 'F': [a / 2, 0], '_G': [-a / 2, 0]}, 'flaeche': ['_G', 'F', 'S'],
            'linien': [['_G', 'F', ''], ['_G', 'S', ''], ['S', 'F', ls], ['M', 'F', la], ['M', 'S', lh, 'gestrichelt']],
            'rechter_winkel': [['M', 'F', 'S']], 'label': 'Schnitt durch die Pyramide: Höhe, halbe Grundkante, Seitenhöhe'}


def sektor(s_, phi, ls='s', lphi='φ'):
    """Kegelmantel abgewickelt: Kreissektor mit Radius s und Mittelpunktswinkel phi (als Vieleck angenähert)."""
    pk = {'Z': [0, 0]}
    n = max(8, int(phi / 10))
    for i in range(n + 1):
        w = math.radians(90 - phi / 2 + phi * i / n)
        pk[f'_{i}'] = [round(s_ * math.cos(w), 4), round(s_ * math.sin(w), 4)]
    fl = ['Z'] + [f'_{i}' for i in range(n + 1)]
    lin = [['Z', '_0', ls], ['Z', f'_{n}', '']] + [[f'_{i}', f'_{i + 1}', ''] for i in range(n)]
    return {'typ': 'figur', 'punkte': pk, 'flaeche': fl, 'linien': lin, 'winkel': [['Z', '_0', f'_{n}', lphi]],
            'label': 'Abgewickelter Kegelmantel: Kreissektor'}


def pyr_schraeg(a, h, la=None, lh=None):
    """Schrägbild einer quadratischen Pyramide (Kanten nach hinten · ½ unter 45°, verdeckte Kanten gestrichelt)."""
    t = round(a / 2 * math.cos(math.radians(45)), 2)
    A, B, C, D = [0, 0], [a, 0], [a + t, t], [t, t]
    F = [round((a + t) / 2, 2), round(t / 2, 2)]
    S = [F[0], round(F[1] + h, 2)]
    return {'typ': 'figur', 'punkte': {'A': A, 'B': B, 'C': C, 'D': D, 'F': F, 'S': S},
            'linien': [['A', 'B', la or f'a = {dz(a)} cm'], ['B', 'C', ''], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'],
                       ['S', 'A'], ['S', 'B'], ['S', 'C'], ['S', 'D', '', 'gestrichelt'], ['F', 'S', lh or f'h = {dz(h)} cm', 'gestrichelt'],
                       ['A', 'C', '', 'gestrichelt'], ['B', 'D', '', 'gestrichelt']],
            'label': 'Schrägbild einer quadratischen Pyramide (verdeckte Kanten gestrichelt)'}


def pyr_netz(a, hs, la=None, lhs=None):
    """Netz einer quadratischen Pyramide: Quadrat mit vier angesetzten gleichschenkligen Dreiecken."""
    m = a / 2
    pk = {'_A': [0, 0], '_B': [a, 0], '_C': [a, a], '_D': [0, a], '_S1': [m, -hs], '_S2': [a + hs, m], '_S3': [m, a + hs], '_S4': [-hs, m], '_M': [m, 0]}
    lin = [['_A', '_B', la or f'a = {dz(a)} cm'], ['_B', '_C', ''], ['_C', '_D', ''], ['_D', '_A', ''],
           ['_A', '_S1', ''], ['_S1', '_B', ''], ['_B', '_S2', ''], ['_S2', '_C', ''], ['_C', '_S3', ''], ['_S3', '_D', ''], ['_D', '_S4', ''], ['_S4', '_A', ''],
           ['_M', '_S1', lhs or f'hₛ = {dz(hs)} cm', 'gestrichelt']]
    return {'typ': 'figur', 'punkte': pk, 'flaeche': ['_A', '_S1', '_B', '_S2', '_C', '_S3', '_D', '_S4'], 'linien': lin,
            'rechter_winkel': [['_M', '_B', '_S1']], 'label': 'Netz einer quadratischen Pyramide'}


def kugel_bild(r, lr='r'):
    return {'typ': 'figur', 'punkte': {'M': [0, 0], '_P': [r, 0], '_O': [0, r], '_U': [0, -r]}, 'kreise': [{'m': 'M', 'r': r}],
            'linien': [['M', '_P', lr], ['_O', '_U', '', 'gestrichelt']], 'label': 'Kugel mit Mittelpunkt M und Radius r'}


ETAPPEN = [
    {'lernziel': 'pyr_volumen', 'titel': 'Volumen einer Pyramide',
     'regel': 'Jede Pyramide hat ⟦ein Drittel⟧ des Volumens eines Prismas mit gleicher Grundfläche und Höhe: ⟦V = ⅓ · G · h⟧. Anschaulich: Ein Würfel lässt sich in ⟦drei gleiche Pyramiden⟧ zerlegen, deren gemeinsame Spitze eine Würfelecke ist – jede hat eine Würfelfläche als Grundfläche und die Kante als Höhe.',
     'schritte': ['Quadratische Pyramide, a = 6 cm, h = 10 cm: G = 6 · 6 = 36 cm².', 'V = ⅓ · 36 · 10 = ⟦120 cm³⟧.'],
     'probe': 'Quaderförmiges Prisma mit gleicher Grundfläche und Höhe: 36 cm² · 10 cm = 360 cm³; ein Drittel davon sind 120 cm³ ✓',
     'fehler': 'V = G · h = 360 cm³ ist falsch: Bei Pyramiden fehlt der Faktor ⟦⅓⟧.'},
    {'lernziel': 'pyr_oberflaeche', 'titel': 'Oberfläche einer Pyramide',
     'regel': 'O = G + M. Bei der quadratischen Pyramide besteht der ⟦Mantel aus 4 Dreiecken⟧ mit der ⟦Seitenhöhe hₛ⟧: M = 4 · ½ · a · hₛ. hₛ folgt aus ⟦hₛ² = h² + (a/2)²⟧.',
     'schritte': ['a = 6 cm, h = 4 cm: hₛ² = 4² + 3² = 25 ⇒ hₛ = 5 cm.', 'O = 36 + 4 · ½ · 6 · 5 = 36 + 60 = ⟦96 cm²⟧.'],
     'probe': 'hₛ ist länger als h ✓',
     'fehler': 'Mit der Körperhöhe h statt der ⟦Seitenhöhe hₛ⟧ zu rechnen ist falsch: Die Dreiecke des Mantels sind schräg, ihre Höhe ist hₛ.'},
    {'lernziel': 'kegel_volumen', 'titel': 'Volumen eines Kegels',
     'regel': 'Ein Kegel ist eine „Pyramide mit kreisförmiger Grundfläche“: ⟦V = ⅓ · π · r² · h⟧.',
     'schritte': ['r = 3 cm, h = 8 cm: V = ⅓ · π · 9 · 8 = 24π cm³.', 'V ≈ ⟦75,4 cm³⟧.'],
     'probe': 'Zylinder mit gleichem r und h: 72π ≈ 226 cm³, ein Drittel ✓',
     'fehler': 'V = ⅓ · π · 3 · 8 ist falsch: Der Radius wird ⟦quadriert⟧ (Grundfläche π r²).'},
    {'lernziel': 'kegel_mantel', 'titel': 'Mantel und Oberfläche des Kegels',
     'regel': 'Abgewickelt ist der Mantel ein ⟦Kreissektor⟧ mit Radius s (Mantellinie). Sein Bogen ist so lang wie der Grundkreisumfang 2πr, deshalb ⟦M = π · r · s⟧ und ⟦Mittelpunktswinkel φ = 360° · r : s⟧. O = πr² + πrs.',
     'schritte': ['r = 3 cm, h = 4 cm: s = √(9 + 16) = 5 cm.', 'M = π · 3 · 5 = 15π ≈ ⟦47,1 cm²⟧; φ = 360° · 3/5 = ⟦216°⟧.'],
     'probe': 'Sektoranteil 216/360 = 3/5 = r/s ✓',
     'fehler': 'M = π · r · h ist falsch: Der Mantel wird mit der ⟦Mantellinie s⟧ berechnet, nicht mit der Höhe.'},
    {'lernziel': 'kugel', 'titel': 'Volumen und Oberfläche der Kugel',
     'regel': '⟦V = ⁴⁄₃ · π · r³⟧ und ⟦O = 4 · π · r²⟧. Ist V oder O gegeben, löst du nach r auf (dritte bzw. Quadratwurzel).',
     'schritte': ['r = 6 cm: V = ⁴⁄₃ · π · 216 = 288π cm³.', 'V ≈ ⟦904,8 cm³⟧; O = 4π · 36 = 144π ≈ ⟦452,4 cm²⟧.'],
     'probe': 'Die Kugel passt in einen Würfel mit 12 cm Kante (1 728 cm³) ✓',
     'fehler': 'V = ⁴⁄₃ · π · r² ist falsch: Ein Volumen hat die Einheit cm³, also ⟦r³⟧.'},
    {'lernziel': 'sachkontext', 'titel': 'Körper in Sachaufgaben',
     'regel': 'Zusammengesetzte Körper zerlegen und die Teilvolumina ⟦addieren oder abziehen⟧. Fehlende Längen mit ⟦Pythagoras⟧, Winkel mit ⟦tan, sin, cos⟧ im Achsenschnitt bestimmen.',
     'schritte': ['Eistüte: Kegel r = 2,5 cm, h = 10 cm, darauf eine Halbkugel r = 2,5 cm.', 'V = ⅓π · 6,25 · 10 + ⅔π · 15,625 ≈ 65,4 + 32,7 = ⟦98,2 cm³⟧.'],
     'probe': 'Halbkugel = halbes Kugelvolumen ✓',
     'fehler': 'Die Halbkugel mit dem vollen Kugelvolumen zu rechnen ist falsch: Es ist ⟦die Hälfte⟧, also ⅔ · π · r³.'},
    {'lernziel': 'verstehen', 'titel': 'Zusammenhänge verstehen',
     'regel': 'Gleiche Grundfläche und gleiche Höhe ⇒ ⟦gleiches Volumen⟧ (Prinzip von Cavalieri). Pyramide/Kegel = ⅓ Prisma/Zylinder. Längen · k ⇒ ⟦Flächen · k², Volumina · k³⟧.',
     'schritte': ['Ein Kegel hat doppelten Radius wie ein anderer, gleiche Höhe.', 'Grundfläche · 4, also ⟦Volumen · 4⟧ (nicht · 8, die Höhe bleibt).'],
     'probe': '⅓π(2r)²h = 4 · ⅓πr²h ✓',
     'fehler': 'Bei doppeltem Radius das doppelte Kegelvolumen anzunehmen ist falsch: r steht ⟦im Quadrat⟧.'},
]
_E = {e['lernziel']: e for e in ETAPPEN}
_E['pyr_volumen']['bild'] = pyr_schraeg(6, 10)
_E['pyr_oberflaeche']['bild'] = pyr_schnitt(6, 4, 'h = 4', 'a/2 = 3', 'hₛ = ?')
_E['kegel_volumen']['bild'] = kegel_schnitt(3, 8, lr='r = 3', lh='h = 8', ls='s')
_E['kegel_mantel']['bild'] = sektor(5, 216, 's = 5', 'φ = 216°')
_E['kugel']['bild'] = kugel_bild(6, 'r = 6')
_E['sachkontext']['bild'] = {'typ': 'figur', 'punkte': {'_S': [0, -10], '_A': [-2.5, 0], '_B': [2.5, 0], '_M': [0, 0], **{f'_{i}': [round(2.5 * math.cos(math.pi * i / 12), 4), round(2.5 * math.sin(math.pi * i / 12), 4)] for i in range(13)}},
                              'flaeche': ['_A', '_S', '_B'] + [f'_{i}' for i in range(13)],
                              'linien': [['_A', '_S', ''], ['_B', '_S', ''], ['_M', '_B', 'r = 2,5'], ['_M', '_S', 'h = 10', 'gestrichelt']] + [[f'_{i}', f'_{i + 1}', ''] for i in range(12)],
                              'label': 'Eistüte im Schnitt: Kegel mit Halbkugel'}


def _seitenkante():
    a = R.choice([4, 6, 8, 10, 12])
    if R.random() < 0.5:
        h = R.randint(3, 12)
        k2 = h * h + a * a / 2
        k = sqrt(k2)
        v = gerundet(k, 1)
        if v is None or k2 == int(k) ** 2: return None
        return mit_grafik(zahl(f'Eine quadratische Pyramide hat die Grundkante a = {a} cm und die Höhe h = {h} cm. Wie lang ist eine Seitenkante? Runde auf eine Nachkommastelle.',
                               f'Halbe Diagonale der Grundfläche: (d/2)² = ({a}/2)² + ({a}/2)² = {dz(Fr(a * a, 2))}. Seitenkante: k² = h² + (d/2)² = {h * h} + {dz(Fr(a * a, 2))} = {dz(k2)} ⇒ k ≈ {dz(v)} cm.',
                               'Die Seitenkante geht von einer Ecke zur Spitze. Der Fußpunkt der Höhe liegt in der Mitte der Diagonale: zweimal Pythagoras.',
                               v, f'round({K(k)}, 1)', einheit='cm', tol=0.1),
                          pyr_schraeg(a, h, lh=f'h = {h} cm'))
    k = R.randint(a // 2 + 3, a + 6)
    h2 = k * k - a * a / 2
    if h2 <= 0: return None
    h = sqrt(h2)
    v = gerundet(h, 1)
    if v is None: return None
    return mit_grafik(zahl(f'Eine quadratische Pyramide hat die Grundkante a = {a} cm, jede Seitenkante ist {k} cm lang. Wie hoch ist die Pyramide? Runde auf eine Nachkommastelle.',
                           f'(d/2)² = ({a}/2)² + ({a}/2)² = {dz(Fr(a * a, 2))}. h² = k² − (d/2)² = {k * k} − {dz(Fr(a * a, 2))} = {dz(h2)} ⇒ h ≈ {dz(v)} cm.',
                           'Rechtwinkliges Dreieck aus Höhe, halber Diagonale und Seitenkante – die halbe Diagonale erst mit Pythagoras bestimmen.',
                           v, f'round({K(h)}, 1)', einheit='cm', tol=0.1),
                      pyr_schraeg(a, h, lh='h = ?'))


def g_pyr_volumen(s):
    if s == 1:
        a, h = R.randint(2, 12), R.choice([3, 6, 9, 12, 15])
        V = Fr(a * a * h, 3)
        return mit_grafik(zahl(f'Eine quadratische Pyramide hat die Grundkante a = {a} cm und die Höhe h = {h} cm. Berechne ihr Volumen.',
                               f'G = {a}² = {a * a} cm²; V = ⅓ · {a * a} · {h} = {dz(V)} cm³.', 'Erst die Grundfläche, dann V = ⅓ · G · h.', V,
                               f'{a} ** 2 * {h} / 3', einheit='cm³'),
                          {'typ': 'figur', 'punkte': {'S': [a / 2, h], 'A': [0, 0], 'B': [a, 0], '_H': [a / 2, 0]}, 'flaeche': ['A', 'B', 'S'],
                           'linien': [['A', 'B', f'a = {a} cm'], ['A', 'S', ''], ['B', 'S', ''], ['_H', 'S', f'h = {h} cm', 'gestrichelt']], 'rechter_winkel': [['_H', 'B', 'S']]})
    if s == 2:
        if R.random() < 0.5:
            l, b, h = R.randint(3, 12), R.randint(2, 10), R.randint(2, 20)
            V = Fr(l * b * h, 3)
            if not endlich(V): return None
            return zahl(f'Eine Pyramide hat eine rechteckige Grundfläche ({l} cm × {b} cm) und die Höhe {h} cm. Berechne ihr Volumen.',
                        f'V = ⅓ · {l} · {b} · {h} = {dz(V)} cm³.', 'Grundfläche = Länge · Breite.', V, f'{l} * {b} * {h} / 3', einheit='cm³')
        a, h = R.randint(2, 12), R.randint(2, 20)
        V = Fr(a * a * h, 3)
        if V.denominator != 1: return None
        return zahl(f'Eine quadratische Pyramide mit Grundkante {a} cm hat das Volumen {dz(V)} cm³. Wie hoch ist sie?',
                    f'h = 3V : G = 3 · {dz(V)} : {a * a} = {h} cm.', 'Stelle V = ⅓ · G · h nach h um.', h, f'3 * {cf(V)} / {a} ** 2', einheit='cm')
    if R.random() < 0.5:
        return _seitenkante()
    g, gh = R.randint(3, 12), R.randint(2, 10)
    h = R.choice([3, 6, 9, 12])
    G = Fr(g * gh, 2)
    V = G * h / 3
    if not endlich(V): return None
    return zahl(f'Eine Pyramide hat als Grundfläche ein Dreieck mit Grundseite {g} cm und Höhe {gh} cm. Die Pyramide ist {h} cm hoch. Berechne ihr Volumen.',
                f'G = ½ · {g} · {gh} = {dz(G)} cm²; V = ⅓ · {dz(G)} · {h} = {dz(V)} cm³.', 'Die Grundfläche ist ein Dreieck: G = ½ · g · h_g.', V,
                f'{g} * {gh} / 2 * {h} / 3', einheit='cm³')


def g_pyr_oberflaeche(s):
    p, q, r = R.choice([t for t in TRIPEL if t[2] <= 25])
    halb, h = (p, q) if R.random() < 0.5 else (q, p)
    a = 2 * halb
    if s == 1:
        return mit_grafik(zahl(f'Eine quadratische Pyramide hat die Grundkante a = {a} cm und die Höhe h = {h} cm. Berechne die Seitenhöhe hₛ.',
                               f'hₛ² = h² + (a/2)² = {h * h} + {halb * halb} = {r * r} ⇒ hₛ = {r} cm.', 'Rechtwinkliges Dreieck aus h, a/2 und hₛ (siehe Zeichnung).',
                               r, f'({h} ** 2 + {halb} ** 2) / {r}', einheit='cm'),
                          pyr_schnitt(a, h, f'h = {h}', f'a/2 = {halb}', 'hₛ = ?'))
    if s == 2 and not (AKT['pool'] != 'uebung' and AKT['nr'] == 0):
        M = 2 * a * r
        return mit_grafik(zahl(f'Eine quadratische Pyramide hat die Grundkante {a} cm und die Seitenhöhe {r} cm. Berechne die Mantelfläche. (Die Zeichnung zeigt das Netz.)',
                               f'M = 4 · ½ · {a} · {r} = {M} cm².', 'Der Mantel besteht aus 4 gleichen Dreiecken (im Netz um das Quadrat herum).', M, f'4 * {a} * {r} / 2', einheit='cm²'),
                          pyr_netz(a, r, lhs=f'hₛ = {r} cm'))
    O = a * a + 2 * a * r
    return mit_grafik(zahl(f'Eine quadratische Pyramide hat die Grundkante {a} cm und die Höhe {h} cm. Berechne ihre Oberfläche.',
                           f'hₛ = √({h}² + {halb}²) = {r} cm; O = {a}² + 4 · ½ · {a} · {r} = {a * a} + {2 * a * r} = {dz(O)} cm².',
                           'Erst hₛ mit Pythagoras, dann O = G + M.', O, f'{a} ** 2 + 2 * {a} * ({h} ** 2 + {halb} ** 2) / {r}', einheit='cm²'),
                      pyr_schnitt(a, h, f'h = {h}', f'a/2 = {halb}', 'hₛ'))


def g_kegel_volumen(s):
    r, h = R.randint(2, 12), R.randint(3, 20)
    V = pi * r * r * h / 3
    if s == 1:
        v = gerundet(V, 1)
        if v is None: return None
        return mit_grafik(zahl(f'Ein Kegel hat den Radius r = {r} cm und die Höhe h = {h} cm. Berechne sein Volumen auf eine Nachkommastelle.',
                               f'V = ⅓ · π · {r}² · {h} = {dz(Fr(r * r * h, 3)) if endlich(Fr(r * r * h, 3)) else br(Fr(r * r * h, 3))}π ≈ {dz(v)} cm³.',
                               'V = ⅓ · π · r² · h; den Radius quadrieren.', v, f'round({r} ** 2 * {h} * {PI} / 3, 1)', einheit='cm³', tol=0.1),
                          kegel_schnitt(r, h, lr=f'r = {r}', lh=f'h = {h}', ls=''))
    if s == 2:
        d = 2 * r
        v = gerundet(V, 1)
        if v is None: return None
        return zahl(f'Ein kegelförmiger Trichter hat oben den Durchmesser {d} cm und ist {h} cm tief. Wie viel Flüssigkeit fasst er (in cm³, eine Nachkommastelle)?',
                    f'r = {d} : 2 = {r} cm; V = ⅓ · π · {r * r} · {h} ≈ {dz(v)} cm³.', 'Achtung: gegeben ist der Durchmesser.', v,
                    f'round(({d} / 2) ** 2 * {h} * {PI} / 3, 1)', einheit='cm³', tol=0.1)
    rr = R.randint(2, 10)
    # Höhe zwischen dem 0,8- und 3-Fachen des Radius, Volumen auf ganze cm³
    Vg = round(pi * rr * rr * rr * R.uniform(0.8, 3) / 3)
    hh = 3 * Vg / (pi * rr * rr)
    v = gerundet(hh, 1)
    if v is None or not (0.8 * rr <= hh <= 3 * rr): return None
    return zahl(f'Ein Kegel mit dem Radius {rr} cm hat das Volumen {dz(Vg)} cm³. Wie hoch ist er (eine Nachkommastelle)?',
                f'h = 3V : (π r²) = 3 · {dz(Vg)} : (π · {rr * rr}) ≈ {dz(v)} cm.', 'Stelle V = ⅓ · π · r² · h nach h um.', v,
                f'round(3 * {Vg} / ({PI} * {rr} ** 2), 1)', einheit='cm', tol=0.1)


def g_kegel_mantel(s):
    p, q, sl = R.choice([t for t in TRIPEL if t[2] <= 30])
    r, h = (p, q) if R.random() < 0.5 else (q, p)
    if s == 1:
        if R.random() < 0.5:
            return mit_grafik(zahl(f'Ein Kegel hat den Radius {r} cm und die Höhe {h} cm. Wie lang ist die Mantellinie s?',
                                   f's² = r² + h² = {r * r} + {h * h} = {sl * sl} ⇒ s = {sl} cm.', 'Pythagoras im Achsenschnitt.', sl,
                                   f'({r} ** 2 + {h} ** 2) / {sl}', einheit='cm'), kegel_schnitt(r, h, lr=f'r = {r}', lh=f'h = {h}', ls='s = ?'))
        phi = Fr(360 * r, sl)
        if not endlich(phi): return None
        return mit_grafik(zahl(f'Der Mantel eines Kegels (r = {r} cm, s = {sl} cm) wird abgewickelt. Wie groß ist der Mittelpunktswinkel φ des Kreissektors?',
                               f'Bogenlänge = 2π · {r}; Anteil am Kreis mit Radius {sl}: {r}/{sl}. φ = 360° · {r}/{sl} = {dz(phi)}°.',
                               'Der Bogen des Sektors ist so lang wie der Umfang des Grundkreises.', phi, f'360 * {r} / {sl}', einheit='°'),
                          sektor(sl, float(phi), f's = {sl}', 'φ = ?'))
    M = pi * r * sl
    O = pi * r * r + M
    if AKT['pool'] in ('korrektur', 'sicherung') and AKT['nr'] == 0:
        s = 3
        wahl_o = True
    else:
        wahl_o = R.random() < 0.6
    if s == 2:
        v = gerundet(M, 1)
        if v is None: return None
        return zahl(f'Ein Kegel hat den Radius {r} cm und die Mantellinie {sl} cm. Berechne die Mantelfläche auf eine Nachkommastelle.',
                    f'M = π · r · s = π · {r} · {sl} = {r * sl}π ≈ {dz(v)} cm².', 'M = π · r · s.', v, f'round({PI} * {r} * {sl}, 1)', einheit='cm²', tol=0.1)
    if wahl_o:
        v = gerundet(O, 1)
        if v is None: return None
        return mit_grafik(zahl(f'Ein Kegel hat den Radius {r} cm und die Höhe {h} cm. Berechne seine Oberfläche auf eine Nachkommastelle.',
                               f's = √({r}² + {h}²) = {sl} cm; O = π · {r}² + π · {r} · {sl} = {r * r + r * sl}π ≈ {dz(v)} cm².', 'Erst s mit Pythagoras, dann O = πr² + πrs.',
                               v, f'round({PI} * {r} ** 2 + {PI} * {r} * ({r} ** 2 + {h} ** 2) / {sl}, 1)', einheit='cm²', tol=0.1),
                          kegel_schnitt(r, h, lr=f'r = {r}', lh=f'h = {h}', ls='s'))
    phi = R.choice([90, 120, 144, 180, 216, 240, 270, 300])
    sl2 = R.randint(5, 20)
    rr = Fr(phi * sl2, 360)
    if not endlich(rr): return None
    return mit_grafik(zahl(f'Aus einem Kreissektor mit Radius {sl2} cm und Mittelpunktswinkel {phi}° wird ein Kegelmantel gerollt. Welchen Radius hat der Grundkreis?',
                           f'r = s · φ / 360° = {sl2} · {phi}/360 = {dz(rr)} cm.', 'Sektorbogen = Grundkreisumfang: 2πr = 2πs · φ/360°.', rr,
                           f'{sl2} * {phi} / 360', einheit='cm'), sektor(sl2, phi, f's = {sl2}', f'φ = {phi}°'))


def g_kugel(s):
    r = R.randint(1, 15) if s < 3 else R.choice([Fr(R.randint(5, 50), 10)])
    if s == 1:
        if R.random() < 0.5:
            v = gerundet(4 * pi * float(r) ** 3 / 3, 1)
            if v is None: return None
            return mit_grafik(zahl(f'Berechne das Volumen einer Kugel mit dem Radius {dz(r)} cm auf eine Nachkommastelle.', f'V = ⁴⁄₃ · π · {dz(r)}³ ≈ {dz(v)} cm³.',
                                   'V = ⁴⁄₃ · π · r³.', v, f'round(4 * {PI} * {cf(r)} ** 3 / 3, 1)', einheit='cm³', tol=0.1), kugel_bild(float(r), f'r = {dz(r)}'))
        v = gerundet(4 * pi * float(r) ** 2, 1)
        if v is None: return None
        return zahl(f'Berechne die Oberfläche einer Kugel mit dem Radius {dz(r)} cm auf eine Nachkommastelle.', f'O = 4 · π · {dz(r)}² ≈ {dz(v)} cm².',
                    'O = 4 · π · r².', v, f'round(4 * {PI} * {cf(r)} ** 2, 1)', einheit='cm²', tol=0.1)
    if s == 2:
        if R.random() < 0.5:
            name, dd = R.choice([('Ein Fußball', '22'), ('Ein Tennisball', '6,7'), ('Eine Murmel', '1,6'), ('Ein Wasserball', '40'), ('Eine Weihnachtskugel', '8'),
                                 ('Ein Basketball', '24'), ('Eine Kugel beim Kugelstoßen', '11')])
            d = Fr(dd.replace(',', '.'))
        else:
            name, d = 'Eine Kugel', Fr(R.randint(3, 60))
        rr = d / 2
        art = R.choice(['V', 'O'])
        w = 4 * pi * float(rr) ** 3 / 3 if art == 'V' else 4 * pi * float(rr) ** 2
        v = gerundet(w, 1)
        if v is None: return None
        return zahl(f'{name} hat {"etwa " if name != "Eine Kugel" else ""}{dz(d)} cm Durchmesser. Berechne ' + ('das Volumen' if art == 'V' else 'die Oberfläche') + ' auf eine Nachkommastelle.',
                    f'r = {dz(rr)} cm; ' + (f'V = ⁴⁄₃ · π · {dz(rr)}³ ≈ {dz(v)} cm³.' if art == 'V' else f'O = 4 · π · {dz(rr)}² ≈ {dz(v)} cm².'),
                    'Erst den Radius bestimmen (halber Durchmesser).', v,
                    f'round(4 * {PI} * {cf(rr)} ** 3 / 3, 1)' if art == 'V' else f'round(4 * {PI} * {cf(rr)} ** 2, 1)',
                    einheit='cm³' if art == 'V' else 'cm²', tol=0.1)
    if R.random() < 0.5:
        V = R.randint(100, 5000)
        rr = (3 * V / (4 * pi)) ** (1 / 3)
        v = gerundet(rr, 2)
        if v is None: return None
        return zahl(f'Eine Kugel hat das Volumen {dz(V)} cm³. Berechne ihren Radius auf zwei Nachkommastellen.', f'r³ = 3V : (4π) = {dz(3 * V)} : (4π) ⇒ r = ∛(…) ≈ {dz(v)} cm.',
                    'Stelle V = ⁴⁄₃πr³ nach r³ um und ziehe die dritte Wurzel.', v, f'round({K(rr)}, 2)', einheit='cm', tol=0.01)
    if R.random() < 0.4:
        # Globus: Durchmesser aus der Oberfläche
        d_ = R.choice([20, 25, 30, 32, 34, 40, 50])
        O = round(pi * d_ * d_)
        rr = sqrt(O / (4 * pi))
        v = gerundet(2 * rr, 1)
        if v is None: return None
        return zahl(f'Ein Globus hat eine Oberfläche von {dz(O)} cm². Welchen Durchmesser hat er? Runde auf eine Nachkommastelle.',
                    f'r² = O : (4π) = {dz(O)} : (4π) ⇒ r ≈ {dz(round(rr, 2))} cm, also d = 2r ≈ {dz(v)} cm.',
                    'Erst den Radius aus O = 4πr², dann verdoppeln.', v, f'round(2 * {K(rr)}, 1)', einheit='cm', tol=0.1)
    O = R.randint(50, 3000)
    rr = sqrt(O / (4 * pi))
    v = gerundet(rr, 2)
    if v is None: return None
    return zahl(f'Eine Kugel hat die Oberfläche {dz(O)} cm². Berechne ihren Radius auf zwei Nachkommastellen.', f'r² = O : (4π) = {dz(O)} : (4π) ⇒ r ≈ {dz(v)} cm.',
                'Stelle O = 4πr² nach r um.', v, f'round({K(rr)}, 2)', einheit='cm', tol=0.01)


def _eistuete():
    r, h = Fr(R.choice([20, 25, 30, 35]), 10), R.choice([8, 10, 12])
    V = pi * float(r) ** 2 * h / 3 + 2 * pi * float(r) ** 3 / 3
    v = gerundet(V, 1)
    if v is None: return None
    return zahl(f'Eine Eistüte ist ein Kegel (r = {dz(r)} cm, h = {h} cm), oben ist eine Halbkugel Eis mit gleichem Radius. Berechne das Gesamtvolumen (eine Nachkommastelle).',
                f'V = ⅓π · {dz(r)}² · {h} + ⅔π · {dz(r)}³ ≈ {dz(v)} cm³.', 'Kegel plus halbe Kugel.', v,
                f'round({PI} * {cf(r)} ** 2 * {h} / 3 + 2 * {PI} * {cf(r)} ** 3 / 3, 1)', einheit='cm³', tol=0.1)


def _hohlkugel():
    ding, d, wand, stoff = R.choice([('Christbaumkugel aus Glas', 8, Fr(2, 10), 'Glas'), ('Hohlkugel aus Stahl', 10, Fr(5, 10), 'Stahl'),
                                     ('Kugel aus Kunststoff', 12, Fr(1, 2), 'Kunststoff'), ('Bojenkugel aus Kunststoff', 40, 1, 'Kunststoff'),
                                     ('Hohlkugel aus Aluminium', 20, 1, 'Aluminium')])
    ra = Fr(d, 2)
    ri = ra - wand
    V = 4 * pi * (float(ra) ** 3 - float(ri) ** 3) / 3
    v = gerundet(V, 1)
    if v is None: return None
    return zahl(f'Eine {ding} hat außen {d} cm Durchmesser, die Wand ist {dz(wand)} cm dick. Wie viel cm³ {stoff} stecken in der Wand? Runde auf eine Nachkommastelle.',
                f'Außenradius {dz(ra)} cm, Innenradius {dz(ra)} − {dz(wand)} = {dz(ri)} cm. V = ⁴⁄₃π · ({dz(ra)}³ − {dz(ri)}³) ≈ {dz(v)} cm³.',
                'Volumen der ganzen Kugel minus Volumen des Hohlraums. Der Innenradius ist um die Wanddicke kleiner.', v,
                f'round(4 * {PI} * ({cf(ra)} ** 3 - {cf(ri)} ** 3) / 3, 1)', einheit='cm³', tol=0.1)


def _dach():
    a, hd = R.choice([(8, 3), (10, 4), (12, 5), (6, 4), (9, 6), (11, 4), (7, 3)])
    hs = sqrt(hd * hd + (a / 2) ** 2)
    M = 2 * a * hs
    v = gerundet(M, 1)
    if v is None: return None
    return mit_grafik(zahl(f'Ein Pavillon hat ein Dach in Form einer quadratischen Pyramide: Grundkante {a} m, Dachhöhe {hd} m. Wie viel m² Dachfläche müssen gedeckt werden? Runde auf eine Nachkommastelle.',
                           f'hₛ = √({hd}² + {dz(Fr(a, 2))}²) ≈ {dz(round(hs, 2))} m. Dachfläche = Mantel = 4 · ½ · {a} · hₛ ≈ {dz(v)} m².',
                           'Die Dachfläche ist nur der Mantel (ohne Grundfläche). Erst die Seitenhöhe mit Pythagoras.', v,
                           f'round({K(M)}, 1)', einheit='m²', tol=0.1),
                      pyr_schnitt(a, hd, f'h = {hd} m', f'a/2 = {dz(Fr(a, 2))} m', 'hₛ'))


def g_sachkontext(s):
    if s == 1:
        d = Fr(R.randint(4, 20), 2)
        r = d / 2
        h = max(Fr(1, 2), Fr(round(float(r) * R.choice([0.5, 0.6, 0.7]) * 2), 2))  # Schüttwinkel von Sand etwa 30°–35°
        V = pi * float(r) ** 2 * float(h) / 3
        v = gerundet(V, 2)
        if v is None: return None
        return mit_grafik(zahl(f'Ein kegelförmiger Sandhaufen hat unten {dz(d)} m Durchmesser und ist {dz(h)} m hoch. Wie viel m³ Sand sind es (zwei Nachkommastellen)?',
                               f'r = {dz(r)} m; V = ⅓ · π · {dz(r)}² · {dz(h)} ≈ {dz(v)} m³.', 'Kegelvolumen; Radius ist der halbe Durchmesser.', v,
                               f'round({cf(r)} ** 2 * {cf(h)} * {PI} / 3, 2)', einheit='m³', tol=0.01),
                          kegel_schnitt(float(r), float(h), lr=f'r = {dz(r)} m', lh=f'h = {dz(h)} m', ls=''))
    typ = R.random()
    if s == 2:
        nr = AKT['nr']
        if nr % 3 != 1:
            return R.choice([_eistuete, _hohlkugel, _dach])()
        if False:
            r, h = Fr(R.choice([20, 25, 30, 35]), 10), R.choice([8, 10, 12])
            V = pi * float(r) ** 2 * h / 3 + 2 * pi * float(r) ** 3 / 3
            v = gerundet(V, 1)
            if v is None: return None
            return zahl(f'Eine Eistüte ist ein Kegel (r = {dz(r)} cm, h = {h} cm), oben ist eine Halbkugel Eis mit gleichem Radius. Berechne das Gesamtvolumen (eine Nachkommastelle).',
                        f'V = ⅓π · {dz(r)}² · {h} + ⅔π · {dz(r)}³ ≈ {dz(v)} cm³.', 'Kegel plus halbe Kugel.', v,
                        f'round({PI} * {cf(r)} ** 2 * {h} / 3 + 2 * {PI} * {cf(r)} ** 3 / 3, 1)', einheit='cm³', tol=0.1)
        r, H, hd = R.choice([3, 4, 5, 6]), R.choice([10, 12, 15, 20]), R.choice([3, 4, 5, 6])
        V = pi * r * r * H + pi * r * r * hd / 3
        v = gerundet(V, 0)
        if v is None: return None
        return zahl(f'Ein Turm besteht aus einem Zylinder (r = {r} m, h = {H} m) mit einem kegelförmigen Dach (gleicher Radius, Dachhöhe {hd} m). Berechne das umbaute Volumen auf ganze m³.',
                    f'V = π · {r}² · {H} + ⅓ · π · {r}² · {hd} ≈ {dz(v)} m³.', 'Zylinder plus Kegel.', v, f'round({PI} * {r} ** 2 * {H} + {PI} * {r} ** 2 * {hd} / 3, 0)', einheit='m³', tol=1)
    if typ < 0.4:
        r, h = R.randint(2, 10), R.randint(3, 20)
        w = math.degrees(math.atan(r / h)) * 2
        v = gerundet(w, 1)
        if v is None: return None
        return mit_grafik(zahl(f'Ein Kegel hat den Radius {r} cm und die Höhe {h} cm. Wie groß ist sein Öffnungswinkel (Winkel an der Spitze im Achsenschnitt, eine Nachkommastelle)?',
                               f'tan(α/2) = r : h = {r}/{h} ⇒ α/2 ≈ {dz(round(w / 2, 2))}° ⇒ α ≈ {dz(v)}°.', 'Im halben Achsenschnitt ist tan(halber Winkel) = r : h.', v,
                               f'round({K(w)}, 1)', einheit='°', tol=0.1), kegel_schnitt(r, h, lr=f'r = {r}', lh=f'h = {h}', ls=''))
    if typ < 0.7:
        r = R.choice([2, 3, 4, 5])
        dichte = R.choice([(Fr(786, 100), 'Stahl'), (Fr(27, 10), 'Aluminium'), (Fr(113, 10), 'Blei'), (Fr(89, 10), 'Kupfer')])
        m = 4 * pi * r ** 3 / 3 * float(dichte[0])
        v = gerundet(m, 0)
        if v is None: return None
        return zahl(f'Eine Kugel aus {dichte[1]} (Dichte {dz(dichte[0])} g/cm³) hat {2 * r} cm Durchmesser. Wie schwer ist sie (auf ganze Gramm)?',
                    f'V = ⁴⁄₃ · π · {r}³ ≈ {dz(round(4 * pi * r ** 3 / 3, 1))} cm³; m = V · {dz(dichte[0])} ≈ {dz(v)} g.', 'Masse = Volumen · Dichte.', v,
                    f'round(4 * {PI} * {r} ** 3 / 3 * {cf(dichte[0])}, 0)', einheit='g', tol=1)
    a, h = R.choice([(230, 146), (215, 143), (35, 21), (147, 92)])
    V = a * a * h / 3
    return zahl(f'Eine quadratische Pyramide (als Modell eines Bauwerks) hat die Grundkante {a} m und die Höhe {h} m. Berechne das Volumen auf ganze m³.',
                f'V = ⅓ · {a}² · {h} ≈ {dz(round(V))} m³.', 'V = ⅓ · G · h.', round(V), f'round({a} ** 2 * {h} / 3, 0)', einheit='m³', tol=1)


VER = {2: 'verdoppelt', 3: 'verdreifacht', 4: 'vervierfacht', 5: 'verfünffacht'}


def g_verstehen(s):
    typ = R.choice({1: 'abc', 2: 'abcde', 3: 'def'}[s])
    if typ == 'a':
        k = R.randint(2, 5)
        welche = R.choice(['Radius', 'Höhe'])
        f = k * k if welche == 'Radius' else k
        return auswahl(f'Bei einem Kegel wird nur {"der Radius" if welche == "Radius" else "die Höhe"} {VER[k]}. Wie ändert sich das Volumen?', f'Es wird {f}-mal so groß.',
                       [f'Es wird {k}-mal so groß.' if f != k else f'Es wird {k * k}-mal so groß.', f'Es wird {k ** 3}-mal so groß.', 'Es bleibt gleich.'],
                       f'V = ⅓πr²h: ' + (f'r · {k} ⇒ r² · {k * k}.' if welche == 'Radius' else f'h · {k} ⇒ V · {k}.'), 'Welche Größe steht im Quadrat?')
    if typ == 'b':
        return auswahl('Ein Kegel und ein Zylinder haben dieselbe Grundfläche und dieselbe Höhe. Wie verhalten sich ihre Volumina?', 'Der Kegel hat ein Drittel des Zylindervolumens.',
                       ['Beide sind gleich groß.', 'Der Kegel hat die Hälfte des Zylindervolumens.', 'Der Kegel hat zwei Drittel des Zylindervolumens.'],
                       'V_Kegel = ⅓ · G · h, V_Zylinder = G · h.', 'Vergleiche die beiden Formeln.')
    if typ == 'c':
        n = R.choice([6, 12, 24, 100])
        return auswahl(f'Eine Pyramide hat als Grundfläche ein regelmäßiges {n}-Eck. Was passiert, wenn man die Eckenzahl immer weiter erhöht?',
                       'Sie nähert sich einem Kegel; V = ⅓ · G · h gilt weiterhin.', ['Sie nähert sich einem Zylinder.', 'Ihr Volumen wird unendlich groß.', 'Sie nähert sich einer Kugel.'],
                       'Die Grundfläche nähert sich einem Kreis – der Kegel ist der Grenzfall der Pyramide. Darum gilt auch für ihn V = ⅓ · G · h.',
                       'Welche Form nimmt die Grundfläche an?')
    if typ == 'd':
        k = R.randint(2, 4)
        art = R.choice(['Volumen', 'Oberfläche'])
        f = k ** 3 if art == 'Volumen' else k * k
        return auswahl(f'Der Radius einer Kugel wird {VER[k]}. Wie ändert sich {"das Volumen" if art == "Volumen" else "die Oberfläche"}?', f'{f}-mal so groß',
                       [f'{k}-mal so groß', f'{k * k if art == "Volumen" else k ** 3}-mal so groß', f'{2 * k}-mal so groß'],
                       f'{art} ~ r{"³" if art == "Volumen" else "²"}: Faktor {k}{"³" if art == "Volumen" else "²"} = {f}.', 'Mit welcher Potenz steht r in der Formel?')
    if typ == 'e':
        r = R.randint(2, 9)
        return auswahl(f'Jemand rechnet die Mantelfläche eines Kegels mit r = {r} cm und h = {r + R.randint(1, 5)} cm als M = π · r · h. Was stimmt?',
                       'Falsch: In M = π · r · s steht die Mantellinie s, nicht die Höhe h.',
                       ['Richtig.', 'Falsch: M = 2π · r · h.', 'Falsch: M = π · r² · h.'],
                       'Der abgewickelte Mantel ist ein Kreissektor mit Radius s; s ist länger als h (s² = r² + h²).', 'Wie lang ist der Radius des abgewickelten Mantels?')
    return auswahl('Eine Kugel passt genau in einen Zylinder (gleicher Radius, Höhe = Durchmesser). Welcher Anteil des Zylinders wird von der Kugel ausgefüllt?', 'zwei Drittel',
                   ['ein Drittel', 'die Hälfte', 'drei Viertel'], 'V_Zylinder = πr² · 2r = 2πr³; V_Kugel = ⁴⁄₃πr³ = ⅔ · 2πr³.', 'Setze h = 2r in die Zylinderformel ein.')



# ---------- KLAR: Lernkarten im neuen Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst nach dem Bauen der Aufgaben eingesetzt (bauen(..., klar=KLAR)), die Aufgaben bleiben wörtlich gleich.
# Muster: einstieg (≤ 35 Wörter) → Kartenbild → Schritte als {text, bild} (Bildergeschichte) → „Pass auf!“ (fehler + fehler_bild) → MERKE (regel).
import math as _m
_BODEN = {'A': [0, 0], 'B': [6, 0], 'C': [8.12, 2.12], 'D': [2.12, 2.12]}
_PYR_L = [['A', 'B', 'a = 6 cm'], ['B', 'C', ''], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt'],
          ['S', 'A'], ['S', 'B'], ['S', 'C'], ['S', 'D', '', 'gestrichelt'], ['F', 'S', 'h = 10 cm', 'gestrichelt']]
_KISTE_P = {'A2': [0, 10], 'B2': [6, 10], 'C2': [8.12, 12.12], 'D2': [2.12, 12.12]}
_KISTE_L = [['A', 'A2', ''], ['B', 'B2', ''], ['C', 'C2', ''], ['D', 'D2', '', 'gestrichelt'],
            ['A2', 'B2', ''], ['B2', 'C2', ''], ['C2', 'D2', ''], ['D2', 'A2', '']]
_PYR = {'typ': 'figur', 'punkte': _BODEN | {'F': [4.06, 1.06], 'S': [4.06, 11.06]}, 'linien': _PYR_L,
        'label': 'Zelt als Pyramide: a = 6 cm, h = 10 cm'}
_KISTE = {'punkte': _BODEN | _KISTE_P | {'F': [4.06, 1.06], 'S': [4.06, 11.06]},
          'linien': [['A', 'B', 'a = 6 cm'], ['B', 'C', ''], ['A', 'D', '', 'gestrichelt'], ['D', 'C', '', 'gestrichelt']] + _KISTE_L,
          'flaeche': [], 'label': 'Kiste mit gleichem Boden und gleicher Höhe: 360 cm³'}

def _schnitt(hs, h='h = 4'):
    return {'typ': 'figur', 'punkte': {'S': [0, 4], 'M': [0, 0], 'F': [3.0, 0], '_G': [-3.0, 0]}, 'flaeche': ['_G', 'F', 'S'],
            'linien': [['_G', 'F', ''], ['_G', 'S', ''], ['S', 'F', hs], ['M', 'F', 'a/2 = 3'], ['M', 'S', h, 'gestrichelt']],
            'rechter_winkel': [['M', 'F', 'S']], 'label': 'Schnitt durch die Mitte des Zelts'}

def _achse(r, h, s='s', mit_zyl=False, label='Achsenschnitt des Kegels'):
    p = {'S': [0, h], 'A': [-r, 0], 'B': [r, 0], 'M': [0, 0]}
    l = [['A', 'B', ''], ['A', 'S', ''], ['B', 'S', s], ['M', 'B', f'r = {r}'], ['M', 'S', f'h = {h}', 'gestrichelt']]
    if mit_zyl:
        p |= {'A2': [-r, h], 'B2': [r, h]}
        l += [['A', 'A2', ''], ['B', 'B2', ''], ['A2', 'B2', '']]
    return {'typ': 'figur', 'punkte': p, 'flaeche': ['A', 'B', 'S'], 'linien': l, 'winkel': [],
            'rechter_winkel': [['M', 'B', 'S']], 'label': label}

_SEK_P = {'Z': [0, 0]} | {f'_{i}': [round(5 * _m.cos(_m.radians(-18 + 216 * i / 21)), 4), round(5 * _m.sin(_m.radians(-18 + 216 * i / 21)), 4)] for i in range(22)}
_SEKTOR = {'typ': 'figur', 'punkte': _SEK_P, 'flaeche': list(_SEK_P),
           'linien': [['Z', '_0', 's = 5'], ['Z', '_21', '']] + [[f'_{i}', f'_{i + 1}', ''] for i in range(21)],
           'rechter_winkel': [], 'winkel': [['Z', '_0', '_21', 'φ = 216°']], 'label': 'Ausgerollter Mantel: Kreissektor mit Radius s'}

_HALB = {f'_{i}': [round(2.5 * _m.cos(_m.radians(15 * i)), 4), round(2.5 * _m.sin(_m.radians(15 * i)), 4)] for i in range(13)}
_TUETE_P = {'_S': [0, -10], '_A': [-2.5, 0], '_B': [2.5, 0], '_M': [0, 0]} | _HALB
_TUETE_L = [['_A', '_S', ''], ['_B', '_S', ''], ['_M', '_B', 'r = 2,5'], ['_M', '_S', 'h = 10', 'gestrichelt']] + [[f'_{i}', f'_{i + 1}', ''] for i in range(12)]

_ZWEI = {'typ': 'figur', 'punkte': {'A': [-1, 0], 'B': [1, 0], 'S': [0, 3], 'M1': [0, 0], 'C': [3, 0], 'D': [7, 0], 'T': [5, 3], 'M2': [5, 0]},
         'linien': [['A', 'B', ''], ['S', 'A', ''], ['S', 'B', ''], ['M1', 'B', 'r'], ['C', 'D', ''], ['T', 'C', ''], ['T', 'D', ''], ['M2', 'D', '2r']],
         'label': 'Gleiche Höhe, doppelter Radius'}

KLAR = {
 'pyr_volumen': {
  'einstieg': 'Ein Zelt hat einen quadratischen Boden und läuft oben spitz zu. Eine Kiste mit gleichem Boden und gleicher Höhe fasst dreimal so viel. '
              'So ein Körper heißt ⟦Pyramide⟧.',
  'woerter': [['Pyramide', 'ein Vieleck als Boden, Dreiecke als Seiten, oben eine Spitze'],
              ['Grundfläche G', 'der Boden; beim Quadrat G = a · a'],
              ['Höhe h', 'der senkrechte Abstand von der Spitze zum Boden']],
  'bild': _PYR,
  'schritte': [{'text': 'Das Zelt hat a = 6 cm. Die Höhe h ist 10 cm.'},
               {'text': 'Grundfläche G = 6 · 6 = 36 cm².', 'bild': {'flaeche': ['A', 'B', 'C', 'D'], 'label': 'Grundfläche G = 36 cm²'}},
               {'text': 'Eine Kiste mit gleichem Boden und gleicher Höhe fasst 36 · 10 = 360 cm³.', 'bild': _KISTE},
               {'text': 'Die Pyramide fasst ein Drittel davon: V = 1/3 · 360 = ⟦120 cm³⟧.',
                'bild': {'punkte': _PYR['punkte'], 'linien': _PYR_L, 'flaeche': [], 'label': 'Pyramide: ein Drittel der Kiste'}}],
  'fehler': 'V = G · h = 360 cm³ ist falsch. Das wäre die ganze Kiste. Die Pyramide läuft spitz zu und fasst nur ⟦ein Drittel⟧.',
  'fehler_bild': {'typ': 'figur', 'punkte': _KISTE['punkte'], 'linien': _KISTE['linien'] + _PYR_L[4:],
                  'label': 'Kiste 360 cm³, Pyramide darin nur 120 cm³'},
  'regel': 'Eine Pyramide fasst ein Drittel des passenden Prismas. Formel: ⟦V = 1/3 · G · h⟧.'},
 'pyr_oberflaeche': {
  'einstieg': 'Das Zelt bekommt neuen Stoff. Man braucht den Boden und vier schräge Dreieckswände. '
              'Alle Flächen zusammen heißen ⟦Oberfläche⟧.',
  'woerter': [['Oberfläche O', 'alle Außenflächen zusammen'],
              ['Mantel M', 'alle Seitenflächen ohne den Boden'],
              ['Seitenhöhe hₛ', 'die Höhe eines Seitendreiecks, schräg gemessen']],
  'bild': _schnitt('hₛ = ?'),
  'schritte': [{'text': 'Mit a = 6 cm und h = 4 cm suchen wir die Seitenhöhe hₛ.'},
               {'text': 'Pythagoras im Schnitt: hₛ² = 4² + 3² = 25, also hₛ = 5.', 'bild': _schnitt('hₛ = 5')},
               {'text': 'Ein Seitendreieck hat 6 · 5 : 2 = 15 cm². Mantel M: 60 cm².',
                'bild': {'punkte': {'P': [0, 0], 'Q': [6, 0], 'T': [3, 5], 'H': [3, 0]}, 'flaeche': ['P', 'Q', 'T'],
                         'linien': [['P', 'Q', 'a = 6'], ['P', 'T', ''], ['Q', 'T', ''], ['H', 'T', 'hₛ = 5', 'gestrichelt']],
                         'rechter_winkel': [['H', 'Q', 'T']], 'label': 'Ein Seitendreieck: 15 cm²'}},
               {'text': 'Mit Boden: Oberfläche O = 36 + 60 = ⟦96 cm²⟧.'}],
  'fehler': 'Mit h = 4 cm statt ⟦hₛ = 5 cm⟧ zu rechnen ist falsch. Die Wände sind schräg und deshalb länger. Der Stoff würde nicht reichen.',
  'fehler_bild': _schnitt('hₛ = 5: schräg', 'h = 4: senkrecht'),
  'regel': 'Oberfläche ist Boden plus Mantel: O = G + M. Der Mantel sind vier Dreiecke. ⟦hₛ² = h² + (a/2)²⟧.'},
 'kegel_volumen': {
  'einstieg': 'Eine Waffeltüte ist unten spitz und oben rund. Sie fasst ein Drittel eines Bechers mit gleichem Kreis und gleicher Höhe. '
              'So ein Körper heißt ⟦Kegel⟧.',
  'woerter': [['Kegel', 'ein Kreis als Boden und oben eine Spitze'],
              ['Radius r', 'der Abstand von der Kreismitte zum Rand'],
              ['Zylinder', 'ein Körper wie eine Dose oder ein Becher']],
  'bild': _achse(3, 8),
  'schritte': [{'text': 'Der Kegel hat den Radius r = 3 cm. Er ist 8 cm hoch.'},
               {'text': 'Grundfläche: π · 3² = 9π cm².'},
               {'text': 'Ein Zylinder mit gleichem Kreis und gleicher Höhe fasst 9π · 8 = 72π cm³.',
                'bild': _achse(3, 8, mit_zyl=True, label='Zylinder um den Kegel: 72π cm³')},
               {'text': 'Der Kegel fasst ein Drittel: 24π cm³ ≈ ⟦75,4 cm³⟧.', 'bild': _achse(3, 8, label='Kegel: ein Drittel davon')}],
  'fehler': 'V = π · r² · h ist falsch. Das ist der ganze Zylinder. Der Kegel fasst nur ⟦ein Drittel⟧ davon.',
  'fehler_bild': _achse(3, 8, mit_zyl=True, label='π · r² · h ist der Zylinder, nicht der Kegel'),
  'regel': 'Ein Kegel fasst ein Drittel des passenden Zylinders. ⟦V = 1/3 · π · r² · h⟧.'},
 'kegel_mantel': {
  'einstieg': 'Man schneidet eine Waffeltüte an der Seite auf und rollt sie flach aus. Es entsteht ein Kreisstück wie ein Tortenstück. '
              'Es heißt ⟦Kreissektor⟧.',
  'woerter': [['Mantellinie s', 'die schräge Strecke von der Spitze zum Rand'],
              ['Kreissektor', 'ein Kreisstück wie ein Tortenstück'],
              ['Mittelpunktswinkel φ', 'der Winkel an der Spitze des Tortenstücks']],
  'bild': _SEKTOR,
  'schritte': [{'text': 'Bei r = 3 und h = 4 suchen wir die Mantellinie s.', 'bild': _achse(3, 4, 's = ?')},
               {'text': 'Pythagoras: s² = 3² + 4² = 25. Also s = 5 cm.', 'bild': _achse(3, 4, 's = 5')},
               {'text': 'Ausgerollt ist der Mantel ein Kreissektor mit dem Radius s = 5 cm.', 'bild': _SEKTOR},
               {'text': 'Mantel: M = π · r · s = 15π ≈ ⟦47,1 cm²⟧.'},
               {'text': 'Mittelpunktswinkel φ = 360° · 3 : 5 = 216°.'}],
  'fehler': 'M = π · r · h ist falsch. Ausgerollt wird die schräge Seite, die ⟦Mantellinie s⟧. Die Höhe h ist kürzer.',
  'fehler_bild': _achse(3, 4, 's = 5: wird ausgerollt', label='h = 4 ist kürzer als s = 5'),
  'regel': 'Der Mantel ist ein Kreissektor mit Radius s. ⟦M = π · r · s⟧. Winkel: φ = 360° · r : s.'},
 'kugel': {
  'einstieg': 'Ein Fußball ist rund. Jeder Punkt der Hülle ist gleich weit vom Mittelpunkt entfernt. '
              'So ein Körper heißt ⟦Kugel⟧. Für alles genügt der Radius.',
  'woerter': [['Kugel', 'alle Punkte der Hülle sind gleich weit vom Mittelpunkt M entfernt'],
              ['r³', 'r · r · r'],
              ['Volumen V', 'wie viel hineinpasst, in cm³']],
  'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_P': [6, 0], '_O': [0, 6], '_U': [0, -6]}, 'kreise': [{'m': 'M', 'r': 6}],
           'linien': [['M', '_P', 'r = 6'], ['_O', '_U', '', 'gestrichelt']], 'label': 'Kugel mit Mittelpunkt M und Radius r'},
  'schritte': [{'text': 'Radius r = 6 cm. Zuerst r³ = 216.'},
               {'text': 'Volumen V = ⁴⁄₃ · π · 216 = 288π ≈ ⟦904,8 cm³⟧.'},
               {'text': 'Oberfläche mit r² = 36: O = 4 · π · 36 ≈ 452,4 cm².'},
               {'text': 'Probe: Der Würfel um die Kugel fasst 1 728 cm³. Gut die Hälfte passt.',
                'bild': {'punkte': {'M': [0, 0], '_P': [6, 0], 'W1': [-6, -6], 'W2': [6, -6], 'W3': [6, 6], 'W4': [-6, 6]},
                         'linien': [['M', '_P', 'r = 6'], ['W1', 'W2', '12 cm'], ['W2', 'W3', ''], ['W3', 'W4', ''], ['W4', 'W1', '']],
                         'label': 'Kugel im Würfel mit 12 cm Kante'}}],
  'fehler': 'V = ⁴⁄₃ · π · r² ist falsch. Ein Volumen hat die Einheit cm³. Also braucht es ⟦r³⟧.',
  'regel': 'Bei der Kugel genügt der Radius. ⟦V = ⁴⁄₃ · π · r³⟧ und O = 4 · π · r².'},
 'sachkontext': {
  'einstieg': 'In der Eisdiele gibt es eine Waffeltüte mit einer halben Kugel Eis darauf. Man zerlegt sie in bekannte Teile. '
              'So etwas ist ein ⟦zusammengesetzter Körper⟧.',
  'woerter': [['zusammengesetzter Körper', 'ein Körper aus bekannten Teilen, z. B. Kegel plus Halbkugel'],
              ['Halbkugel', 'eine halbe Kugel: 2/3 · π · r³'],
              ['Teilvolumen', 'das Volumen eines Teils']],
  'bild': {'typ': 'figur', 'punkte': _TUETE_P, 'flaeche': ['_A', '_S', '_B'] + [f'_{i}' for i in range(13)], 'linien': _TUETE_L,
           'label': 'Eistüte im Schnitt: Kegel mit Halbkugel'},
  'schritte': [{'text': 'Die Tüte ist ein Kegel: r = 2,5 cm und h = 10 cm.', 'bild': {'flaeche': ['_A', '_S', '_B'], 'label': 'Teil 1: Kegel'}},
               {'text': 'Kegel: 1/3 · π · 2,5² · 10 ≈ 65,45 cm³.'},
               {'text': 'Darauf sitzt eine Halbkugel mit demselben Radius.',
                'bild': {'flaeche': [f'_{i}' for i in range(13)], 'label': 'Teil 2: Halbkugel'}},
               {'text': 'Halbkugel: die Hälfte von ⁴⁄₃ · π · 2,5³ ≈ 32,72 cm³.'},
               {'text': 'Teilvolumen addieren: 65,45 + 32,72 ≈ ⟦98,2 cm³⟧.',
                'bild': {'flaeche': ['_A', '_S', '_B'] + [f'_{i}' for i in range(13)], 'label': 'Ganze Portion ≈ 98,2 cm³'}}],
  'fehler': 'Die Halbkugel mit dem ganzen Kugelvolumen zu rechnen ist falsch. Auf der Tüte sitzt nur ⟦die Hälfte⟧: 2/3 · π · r³.',
  'fehler_bild': {'typ': 'figur', 'punkte': _TUETE_P, 'flaeche': ['_A', '_S', '_B'], 'linien': _TUETE_L, 'kreise': [{'m': '_M', 'r': 2.5}],
                  'label': 'Die ganze Kugel wäre zu viel'},
  'regel': 'Zerlege den Körper in bekannte Teile. Teilvolumen ⟦addieren oder abziehen⟧. Fehlende Längen mit Pythagoras oder tan, sin, cos.'},
 'verstehen': {
  'einstieg': 'Zwei Spitzbecher sind gleich hoch. Der große hat den doppelten Radius. Er fasst nicht doppelt, sondern viermal so viel. '
              'Das erklärt das ⟦Vergrößern mit dem Faktor k⟧.',
  'woerter': [['Faktor k', 'die Zahl, mit der Längen malgenommen werden'],
              ['k²', 'k · k'],
              ['k³', 'k · k · k']],
  'bild': _ZWEI,
  'schritte': [{'text': 'Zwei Kegel sind gleich hoch. Der zweite hat den doppelten Radius.'},
               {'text': 'Grundfläche: π · (2r)² = 4 · π · r². Sie ist viermal so groß.', 'bild': {'label': 'Grundfläche: viermal so groß'}},
               {'text': 'Die Höhe bleibt gleich. Also wird auch das Volumen ⟦viermal so groß⟧.'},
               {'text': 'Alle Längen mal Faktor k = 2: Flächen mal k², Volumen mal k³.'}],
  'fehler': 'Doppelter Radius heißt nicht doppeltes Volumen. r steht ⟦im Quadrat⟧. Der Boden wird in zwei Richtungen doppelt so breit.',
  'fehler_bild': {'typ': 'tabelle', 'kopf': ['Radius', 'Grundfläche', 'Volumen'],
                  'zeilen': [['r', 'π · r²', 'V'], ['2r', '4 · π · r²', '4 · V']]},
  'regel': 'Längen mal k: Flächen mal k², Volumen mal k³. Gleiche Querschnitte in jeder Höhe bedeuten ⟦gleiches Volumen⟧ (Cavalieri).'},
}


GEN = schoen({'pyr_volumen': g_pyr_volumen, 'pyr_oberflaeche': g_pyr_oberflaeche, 'kegel_volumen': g_kegel_volumen, 'kegel_mantel': g_kegel_mantel,
              'kugel': g_kugel, 'sachkontext': g_sachkontext, 'verstehen': g_verstehen})

if __name__ == '__main__':
    bauen('raum.pyramide_kegel_kugel',
          'Volumen und Oberfläche von Pyramide, Kegel und Kugel berechnen, die Kegelformeln begründen und Körper in Sachzusammenhängen untersuchen.',
          ['Pyramide und Kegel: V = ⅓ · G · h.', 'Quadratische Pyramide: hₛ² = h² + (a/2)², O = a² + 2 · a · hₛ.',
           'Kegel: s² = r² + h², M = π r s, O = π r² + π r s, Sektorwinkel φ = 360° · r/s.', 'Kugel: V = ⁴⁄₃ π r³, O = 4 π r².'],
          [('Pyramide', ['pyr_volumen', 'pyr_oberflaeche']), ('Kegel', ['kegel_volumen', 'kegel_mantel']), ('Kugel', ['kugel']),
           ('Anwenden und Verstehen', ['sachkontext', 'verstehen'])],
          ETAPPEN, GEN, klar=KLAR,
          meiden={'pyr_volumen': ['Grundkante a = 6 cm und die Höhe h = 10 cm'], 'pyr_oberflaeche': ['Grundkante a = 6 cm und die Höhe h = 4 cm'],
                  'kegel_volumen': ['Radius r = 3 cm und die Höhe h = 8 cm'], 'kegel_mantel': ['Radius 3 cm und die Höhe 4 cm', 'r = 3 cm, s = 5 cm'],
                  'kugel': ['Radius 6 cm']},
          offen=['Prüfung eingearbeitet (Runde 3): Karte „pyr_volumen“ mit Würfel-Zerlegung und korrigierter Probe (Quader statt Würfel); Schrägbild der Pyramide in „pyr_volumen“ und bei der Seitenkante, Netz der Pyramide bei der Mantelfläche. Neue Aufgaben: Seitenkante/Höhe über zwei Pythagoras-Schritte, Durchmesser eines Globus aus der Oberfläche, Hohlkugel, Pyramidendach; Oberfläche aus a und h bzw. r und h in Test/Korrektur/Sicherung; realistische Kegelhöhen; Turm-Aufgaben höchstens ein Drittel je Pool.',
                 'Zeichnungen: Achsenschnitt des Kegels, Schnittdreieck der Pyramide (h, a/2, hₛ), abgewickelter Kegelmantel als Kreissektor (Bogen als Vieleck angenähert), Kugel mit Radius, Eistüte im Schnitt – in Lernkarten und passenden Aufgaben.',
                 'Schrägbild und Netz der quadratischen Pyramide jetzt mit „figur“. Weiter nicht möglich: Schrägbild des Kegels (Ellipse für den Grundkreis) und Zeichnen durch das Kind.',
                 'Prinzip von Cavalieri und „Kegel als Grenzfall der Pyramide“ nur als Verstehensfragen (ohne Zeichnung). Extremwerte an Körpern (umfang) weggelassen – nicht im lehrplan_gym.',
                 'Gerundete Ergebnisse mit Toleranz (0,1 bzw. 0,01; bei ganzen Zahlen 1); π als 12-stellige Konstante in c.'])
