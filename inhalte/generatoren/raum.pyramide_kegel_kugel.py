#!/usr/bin/env python3
"""Thema raum.pyramide_kegel_kugel – Pyramide, Kegel, Kugel (Klasse 10)."""
import math
import sys
from math import isqrt, pi, sqrt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import *  # noqa: E402,F403
from _schwer_kl10 import ergaenzen  # noqa: E402

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

# ---------- Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild ----------
# Eigener Zufallsstart (nur zum Mischen der Antworten); wird erst NACH bauen(...) aufgerufen, alte Aufgaben bleiben gleich.
# Vorbilder (Typ und Niveau, eigene Zahlen und Einkleidung): Realschul-Abschlussprüfung Bayern Mathematik I (2021 A 3.3: Lage eines Punkts so,
# dass zwei Volumina gleich sind; 2021 B 2.6: Anteil in Prozent; 2024 B 4.5: Volumenverhältnis bei gleicher Spitze; Beispielaufgabe A 4 ohne
# Taschenrechner: Pyramide mit Spitze über einer Ecke), Abitur Bayern 2025 Prüfungsteil A Geometrie (Würfel durch Ebene geteilt; Punkt auf
# einer Kante so, dass die Pyramide ein vorgegebenes Volumen hat), ZP10 NRW ohne Hilfsmittel (Höhe aus G und V; Aussage „doppelte Höhe“ prüfen),
# Bayerischer Mathematik-Test 10 2010 (Kopfüberlegung mit π ≈ 3), Schulaufgabe Gymnasium Bayern Kl. 10 (Kugeln im Wasser: läuft es über?).
def schwer():
    start(10015)
    N = []
    P = math.pi

    def neu(l, s, a):
        a['l'], a['s'] = l, s
        N.append(a)

    def rz(wahr, nd):
        return gerundet(wahr, nd), f'round({K(wahr)}, {nd})'

    # --- pyr_volumen ---
    neu('pyr_volumen', 2, zahl('Eine Pyramide hat die Grundfläche 32 cm² und das Volumen 96 cm³. Wie hoch ist sie?', 'h = 3V : G = 3 · 96 : 32 = 9 cm.',
                               'Stelle V = 1/3 · G · h nach h um.', 9, '3 * 96 / 32', einheit='cm'))
    neu('pyr_volumen', 2, zahl('In einem Würfel mit der Kante 6 cm steht eine Pyramide: Grundfläche ist der Würfelboden, die Spitze liegt in der Mitte der Deckfläche. Berechne ihr Volumen.',
                               'G = 6² = 36 cm², h = 6 cm (Würfelhöhe). V = 1/3 · 36 · 6 = 72 cm³.', 'Wie hoch ist die Pyramide, wenn die Spitze in der Deckfläche liegt?', 72, '36 * 6 / 3', einheit='cm³'))
    neu('pyr_volumen', 3, zahl('Von einem Würfel mit der Kante 6 cm wird eine Ecke abgeschnitten: Der Schnitt geht durch die drei Nachbarecken dieser Ecke. Welches Volumen hat das abgeschnittene Stück?',
                               'Das Stück ist eine Pyramide. Grundfläche: rechtwinkliges Dreieck mit den Katheten 6 cm, also G = 1/2 · 6 · 6 = 18 cm². Höhe: die dritte Kante, 6 cm. V = 1/3 · 18 · 6 = 36 cm³ (ein Sechstel des Würfels).',
                               'Das abgeschnittene Stück ist eine Pyramide mit dreieckiger Grundfläche. Welche Kante steht senkrecht darauf?', 36, '(6 * 6 / 2) * 6 / 3', einheit='cm³'))
    neu('pyr_volumen', 3, zahl('Ein Würfel hat die Kante 4 cm, unten das Quadrat ABCD, darüber E über A. Der Punkt S liegt auf der Kante [AE] im Abstand x von A. Für welches x hat die Pyramide ABCDS das Volumen 8 cm³?',
                               'Grundfläche ABCD = 16 cm², Höhe = AS = x (die Kante [AE] steht senkrecht auf dem Boden). 1/3 · 16 · x = 8 ⇒ x = 1,5 cm.',
                               'Die Spitze liegt über A. Wie hoch ist die Pyramide dann?', 1.5, '3 * 8 / 16', einheit='cm'))
    neu('pyr_volumen', 3, luecken('Zwei Pyramiden haben dieselbe Spitze, ihre Grundflächen liegen in derselben Ebene. Die Grundflächen sind 12 cm² und 30 cm² groß. In welchem Verhältnis stehen die Volumina (kleinere zuerst, gekürzt)?',
                                  '□ : □', 'Zwei ganze Zahlen', [2, 5], 'Gleiche Spitze und gleiche Grundebene: gleiche Höhe h. V₁ : V₂ = (1/3 · 12 · h) : (1/3 · 30 · h) = 12 : 30 = 2 : 5.',
                                  'Was haben beide Pyramiden gemeinsam?', c=['12 // 6', '30 // 6']))
    neu('pyr_volumen', 3, zahl('Wie viele gleich große quadratische Pyramiden, deren Spitzen im Mittelpunkt eines Würfels liegen, füllen den Würfel genau aus?',
                               'Jede Würfelfläche ist Grundfläche einer Pyramide mit der Höhe a/2: V = 1/3 · a² · a/2 = a³/6. Sechs Flächen, sechs Pyramiden: 6 · a³/6 = a³.',
                               'Verbinde den Mittelpunkt mit allen Ecken. Über jeder Würfelfläche entsteht eine Pyramide.', 6, '6'))

    # --- pyr_oberflaeche ---
    neu('pyr_oberflaeche', 2, zahl('Eine quadratische Pyramide hat die Grundkante 10 cm und die Seitenhöhe 13 cm. Berechne ihre Oberfläche.',
                                   'G = 100 cm², M = 4 · 1/2 · 10 · 13 = 260 cm². O = 360 cm².', 'Oberfläche = Grundfläche + vier Dreiecke.', 360, '10 ** 2 + 2 * 10 * 13', einheit='cm²'))
    neu('pyr_oberflaeche', 2, zahl('Eine quadratische Pyramide mit der Grundkante 10 cm hat die Mantelfläche 240 cm². Wie groß ist die Seitenhöhe?',
                                   'M = 4 · 1/2 · 10 · hₛ = 20 · hₛ = 240 ⇒ hₛ = 12 cm.', 'Stelle M = 4 · 1/2 · a · hₛ nach hₛ um.', 12, '240 / 20', einheit='cm'))
    w, c = rz(math.degrees(math.atan(3 / 4)), 1)
    neu('pyr_oberflaeche', 3, zahl('Eine quadratische Pyramide hat die Grundkante 8 cm und die Höhe 3 cm. Unter welchem Winkel ist eine Seitenfläche gegen die Grundfläche geneigt? Runde auf eine Nachkommastelle.',
                                   f'Schnitt durch die Spitze und die Mitten zweier Gegenseiten: rechtwinkliges Dreieck mit Höhe 3 cm und halber Grundkante 4 cm. tan ε = 3 : 4 ⇒ ε ≈ {dz(w)}°.',
                                   'Zeichne das Dreieck aus Höhe, halber Grundkante und Seitenhöhe.', w, c, einheit='°', tol=0.1))
    w, c = rz(36 * math.sqrt(3), 1)
    neu('pyr_oberflaeche', 3, zahl('Ein regelmäßiges Tetraeder (vier gleichseitige Dreiecke) hat die Kantenlänge 6 cm. Berechne seine Oberfläche. Runde auf eine Nachkommastelle.',
                                   f'Höhe eines Dreiecks: h = √(6² − 3²) = √27 cm. Ein Dreieck: 1/2 · 6 · √27 ≈ 15,59 cm². Vier Dreiecke: ≈ {dz(w)} cm².',
                                   'Berechne die Höhe eines gleichseitigen Dreiecks mit Pythagoras.', w, c, einheit='cm²', tol=0.1))
    neu('pyr_oberflaeche', 3, zahl('Die Oberfläche einer quadratischen Pyramide mit der Grundkante 6 cm ist dreimal so groß wie ihre Grundfläche. Wie lang ist die Seitenhöhe?',
                                   'G = 36 cm², O = 108 cm², also M = 72 cm². M = 4 · 1/2 · 6 · hₛ = 12 · hₛ = 72 ⇒ hₛ = 6 cm.', 'Wie groß ist der Mantel, wenn O = 3 · G?', 6, '(3 * 36 - 36) / 12', einheit='cm'))
    neu('pyr_oberflaeche', 3, auswahl('Eine quadratische Pyramide hat a = 6 cm und h = 4 cm. Jemand rechnet die Mantelfläche als 4 · 1/2 · 6 · 4 = 48 cm². Was stimmt?',
                                      'Falsch: In die Dreiecksfläche gehört die Seitenhöhe hₛ = 5 cm, also M = 60 cm².',
                                      ['Richtig.', 'Falsch: M = 6² + 48 = 84 cm².', 'Falsch: M = 1/3 · 6² · 4 = 48 cm³.'],
                                      'Die Seitenflächen sind Dreiecke mit der Höhe hₛ, nicht h. hₛ² = 4² + 3² = 25 ⇒ hₛ = 5 cm. M = 4 · 1/2 · 6 · 5 = 60 cm².',
                                      'Welche Höhe hat ein Seitendreieck?'))

    # --- kegel_volumen ---
    neu('kegel_volumen', 2, zahl('Ein Kegel hat die Grundfläche 24 cm² und das Volumen 64 cm³. Wie hoch ist er?', 'h = 3V : G = 3 · 64 : 24 = 8 cm.',
                                 'Hier brauchst du π nicht: Die Grundfläche ist schon gegeben.', 8, '3 * 64 / 24', einheit='cm'))
    neu('kegel_volumen', 2, zahl('Ein Zylinder und ein Kegel haben denselben Radius und dieselbe Höhe. Der Zylinder fasst 1,2 l. Wie viel Liter fasst der Kegel?',
                                 'V_Kegel = 1/3 · V_Zylinder = 1,2 : 3 = 0,4 l.', 'Vergleiche die Formeln von Zylinder und Kegel.', 0.4, '1.2 / 3', einheit='l'))
    neu('kegel_volumen', 3, bruch_luecke('Ein kegelförmiges Glas (Spitze unten) ist bis zur halben Höhe mit Saft gefüllt. Welcher Anteil des Glasvolumens ist gefüllt?', Fr(1, 8),
                                         'Der Saft bildet einen kleineren Kegel mit halber Höhe und – nach dem Strahlensatz – halbem Radius. V = 1/3 · π · (r/2)² · h/2 = 1/8 · (1/3 · π · r² · h).',
                                         'Wie groß ist der Radius der Saftoberfläche? Denk an den Strahlensatz.', c=['1', '2 ** 3']))
    neu('kegel_volumen', 3, zahl('Schätze ohne Taschenrechner mit π ≈ 3: Wie viele Liter fasst ein Kegel mit dem Radius 10 cm und der Höhe 30 cm?',
                                 'V ≈ 1/3 · 3 · 10² · 30 = 3 000 cm³ = 3 l.', '1 l = 1 000 cm³.', 3, '3 * 100 * 30 / 3 / 1000', einheit='l'))
    neu('kegel_volumen', 3, zahl('Ein Kegel ist genauso hoch, wie sein Radius lang ist, und hat das Volumen 72π cm³. Wie groß ist der Radius?',
                                 '1/3 · π · r² · r = 72π ⇒ r³ = 216 ⇒ r = 6 cm.', 'Setze h = r ein; dann steht r³ in der Formel.', 6, '6 + (6 ** 3 - 3 * 72)', einheit='cm'))
    neu('kegel_volumen', 3, zahl('Ein Kegel und eine Kugel haben denselben Radius r und dasselbe Volumen. Die Höhe des Kegels ist wie viel-mal so groß wie r?',
                                 '1/3 · π · r² · h = 4/3 · π · r³ ⇒ h = 4r.', 'Setze die beiden Volumenformeln gleich und kürze.', 4, '4'))

    # --- kegel_mantel ---
    neu('kegel_mantel', 2, luecken('Ein Kegel hat r = 6 cm und s = 10 cm. Gib seine Oberfläche als Vielfaches von π an (in cm²).', '□ · π', 'Zahl vor π', [96],
                                   'O = π · r² + π · r · s = 36π + 60π = 96π cm².', 'Oberfläche = Grundkreis + Mantel.', c=['6 ** 2 + 6 * 10']))
    neu('kegel_mantel', 2, zahl('Ein Kegel hat den Radius 5 cm und die Mantelfläche 60π cm². Wie lang ist die Mantellinie s?', 'π · 5 · s = 60π ⇒ s = 12 cm.',
                                'Setze in M = π · r · s ein und kürze π.', 12, '60 / 5', einheit='cm'))
    w, c = rz(math.sqrt(75), 1)
    neu('kegel_mantel', 3, zahl('Der Mantel eines Kegels ist abgewickelt ein Halbkreis mit dem Radius 10 cm. Wie hoch ist der Kegel? Runde auf eine Nachkommastelle.',
                                f'Mantellinie s = 10 cm. Bogen des Halbkreises = Umfang des Grundkreises: π · 10 = 2π · r ⇒ r = 5 cm. h = √(10² − 5²) = √75 ≈ {dz(w)} cm.',
                                'Der Bogen des Halbkreises wird zum Grundkreis.', w, c, einheit='cm', tol=0.1))
    neu('kegel_mantel', 3, zahl('Wie groß ist der Öffnungswinkel eines Kegels (Winkel an der Spitze im Achsenschnitt), dessen abgewickelter Mantel genau ein Halbkreis ist?',
                                'Halbkreis: Bogen π · s = 2π · r ⇒ s = 2r. Im Achsenschnitt: sin(α/2) = r : s = 1/2 ⇒ α/2 = 30° ⇒ α = 60°.',
                                'Zeige zuerst s = 2r. Dann hilft der Sinus im halben Achsenschnitt.', 60, '2 * 30', einheit='°'))
    neu('kegel_mantel', 3, zahl('Ein Kegel mit dem Radius 5 cm hat die Oberfläche 90π cm². Wie lang ist seine Mantellinie?', '25π + 5π · s = 90π ⇒ 5s = 65 ⇒ s = 13 cm.',
                                'Oberfläche = π r² + π r s. Kürze π.', 13, '(90 - 25) / 5', einheit='cm'))
    r = 56 / (2 * P)
    w, c = rz(28 * math.sqrt(400 + r * r), 0)
    neu('kegel_mantel', 3, zahl('Ein Partyhut (Kegelmantel ohne Boden) soll 20 cm hoch sein und unten 56 cm Umfang haben. Wie viel cm² Papier braucht man mindestens? Runde auf ganze cm².',
                                f'r = 56 : (2π) ≈ 8,91 cm. s = √(20² + r²) ≈ 21,90 cm. M = π · r · s = 28 · s ≈ {dz(w)} cm² (denn π · r = 56 : 2 = 28).',
                                'Bestimme r aus dem Umfang, dann s mit Pythagoras.', w, c, einheit='cm²', tol=1))

    # --- kugel ---
    neu('kugel', 2, luecken('Gib das Volumen einer Halbkugel mit dem Radius 6 cm als Vielfaches von π an (in cm³).', '□ · π', 'Zahl vor π', [144],
                            'V = 1/2 · 4/3 · π · 6³ = 2/3 · 216 · π = 144π cm³.', 'Halbe Kugel: 1/2 · 4/3 = 2/3.', c=['2 * 216 // 3']))
    neu('kugel', 2, zahl('Eine Kugel hat die Oberfläche 100π cm². Wie groß ist ihr Radius?', '4π r² = 100π ⇒ r² = 25 ⇒ r = 5 cm.', 'Kürze π und teile durch 4.', 5, '5 + (4 * 5 ** 2 - 100)', einheit='cm'))
    neu('kugel', 3, zahl('Ein zylindrisches Glas (Innenradius 5 cm) enthält Wasser. Drei Kugeln mit dem Radius 2 cm werden hineingelegt und sind ganz unter Wasser. Um wie viel cm steigt der Wasserspiegel?',
                         'Kugelvolumen: 3 · 4/3 · π · 2³ = 32π cm³. Das Wasser steigt um h mit π · 5² · h = 32π ⇒ h = 32 : 25 = 1,28 cm.',
                         'Das verdrängte Wasser bildet einen flachen Zylinder mit dem Radius des Glases.', 1.28, '3 * 4 * 8 / 3 / 25', einheit='cm'))
    neu('kugel', 3, zahl('Bei einer Kugel ist die Maßzahl des Volumens (in cm³) gleich der Maßzahl der Oberfläche (in cm²). Wie groß ist der Radius?',
                         '4/3 · π · r³ = 4 · π · r² ⇒ r/3 = 1 ⇒ r = 3 cm.', 'Setze die Formeln gleich und teile durch 4 · π · r².', 3, '3', einheit='cm'))
    w, c = rz(2 ** (1 / 3), 2)
    neu('kugel', 3, zahl('Eine Kugel soll das doppelte Volumen haben. Mit welchem Faktor muss man den Radius multiplizieren? Runde auf zwei Nachkommastellen.',
                         f'Volumen ~ r³: k³ = 2 ⇒ k = ∛2 ≈ {dz(w)}. (Nicht 2: das gäbe das 8-fache Volumen.)', 'Wie wirkt sich der Faktor k beim Radius auf r³ aus?', w, c, tol=0.01))
    r = 70 / (2 * P)
    w, c = rz(4 / 3 * P * r ** 3 / 1000, 2)
    neu('kugel', 3, zahl('Ein Ball hat (am dicksten Kreis gemessen) den Umfang 70 cm. Wie viele Liter Luft passen hinein? Runde auf zwei Nachkommastellen.',
                         f'r = 70 : (2π) ≈ 11,14 cm. V = 4/3 · π · r³ ≈ {dz(round(4 / 3 * P * r ** 3, 0))} cm³ ≈ {dz(w)} l.',
                         'Bestimme zuerst den Radius aus dem Umfang. 1 l = 1 000 cm³.', w, c, einheit='l', tol=0.01))

    # --- sachkontext ---
    w, c = rz(2 * math.sqrt(3 * 12 / (2 * P)), 2)
    neu('sachkontext', 2, zahl('Ein kegelförmiger Sandhaufen ist 2 m hoch und enthält 12 m³ Sand. Welchen Durchmesser hat er unten? Runde auf zwei Nachkommastellen.',
                               f'r² = 3V : (π h) = 36 : (2π) ≈ 5,73 ⇒ r ≈ 2,39 m ⇒ d ≈ {dz(w)} m.', 'Stelle die Kegelformel nach r² um. Gefragt ist der Durchmesser.', w, c, einheit='m', tol=0.01))
    w, c = rz(78 * P, 1)
    neu('sachkontext', 2, zahl('Ein Werkstück ist ein Zylinder (r = 3 cm, h = 10 cm) mit einer kegelförmigen Bohrung von oben (gleicher Radius, 4 cm tief). Berechne das Volumen des Werkstücks. Runde auf eine Nachkommastelle.',
                               f'Zylinder 90π cm³ minus Kegel 1/3 · π · 9 · 4 = 12π cm³: 78π ≈ {dz(w)} cm³.', 'Vom Zylinder wird der Kegel abgezogen.', w, c, einheit='cm³', tol=0.1))
    w, c = rz(math.sqrt(250), 2)
    neu('sachkontext', 3, zahl('Eine Pyramide hat das Rechteck ABCD (AB = 12 cm, BC = 5 cm) als Grundfläche. Die Spitze S liegt senkrecht über D, DS = 9 cm. Wie lang ist die längste Kante [BS]? Runde auf zwei Nachkommastellen.',
                               f'BD ist die Diagonale des Rechtecks: BD = √(12² + 5²) = 13 cm. Dreieck BDS ist rechtwinklig bei D: BS = √(13² + 9²) = √250 ≈ {dz(w)} cm.',
                               'Erst die Diagonale BD, dann das rechtwinklige Dreieck BDS.', w, c, einheit='cm', tol=0.01))
    w, c = rz(math.degrees(math.atan(9 / 13)), 1)
    neu('sachkontext', 3, zahl('Pyramide wie eben: Rechteck ABCD mit AB = 12 cm, BC = 5 cm, Spitze S senkrecht über D, DS = 9 cm. Wie groß ist der Winkel ∢DBS? Runde auf eine Nachkommastelle.',
                               f'Im rechtwinkligen Dreieck BDS: tan(∢DBS) = DS : BD = 9 : 13 ⇒ ∢DBS ≈ {dz(w)}°.', 'BD = 13 cm (Diagonale). Welche Seiten liegen am Winkel bei B?', w, c, einheit='°', tol=0.1))
    w, c = rz(1 / 3 * P * 64 * math.sqrt(80), 1)
    neu('sachkontext', 3, zahl('Aus einem Kreis mit Radius 12 cm wird ein Sektor mit 240° ausgeschnitten und zu einem Kegelmantel gerollt. Welches Volumen hat der Kegel? Runde auf eine Nachkommastelle.',
                               f's = 12 cm. Bogen = 240/360 · 2π · 12 = 16π = 2π · r ⇒ r = 8 cm. h = √(12² − 8²) = √80 ≈ 8,94 cm. V = 1/3 · π · 64 · √80 ≈ {dz(w)} cm³.',
                               'Der Sektorradius wird zur Mantellinie, der Bogen zum Grundkreisumfang.', w, c, einheit='cm³', tol=0.1))
    w, c = rz((1 - 4 / 3 * P * 125 / 1000) * 100, 1)
    neu('sachkontext', 3, zahl('Aus einem Holzwürfel mit 10 cm Kantenlänge wird die größtmögliche Kugel gedrechselt. Wie viel Prozent des Holzes werden zu Spänen? Runde auf eine Nachkommastelle.',
                               f'Die Kugel hat r = 5 cm: V ≈ 523,6 cm³ von 1 000 cm³, also 52,4 %. Abfall: ≈ {dz(w)} %.', 'Der größte Kugeldurchmesser ist die Kantenlänge.', w, c, einheit='%', tol=0.1))

    # --- verstehen ---
    neu('verstehen', 2, auswahl('Bei einem Kegel wird nur die Höhe verdoppelt. Wie ändert sich das Volumen?', 'Es verdoppelt sich.', ['Es vervierfacht sich.', 'Es wird 8-mal so groß.', 'Es bleibt gleich.'],
                                'V = 1/3 · π · r² · h: h steht ohne Quadrat in der Formel, also Faktor 2.', 'Mit welcher Potenz steht h in der Formel?'))
    neu('verstehen', 2, auswahl('Ein Prisma und eine Pyramide haben dieselbe Grundfläche und dieselbe Höhe. Wie groß ist das Volumen der Pyramide?', 'ein Drittel des Prismavolumens',
                                ['die Hälfte des Prismavolumens', 'genauso groß', 'zwei Drittel des Prismavolumens'], 'V_Pyramide = 1/3 · G · h, V_Prisma = G · h.', 'Vergleiche die Formeln.'))
    neu('verstehen', 3, auswahl('Zwei Pyramiden haben dieselbe Grundfläche und dieselbe Höhe. Die eine ist gerade, die andere schief (Spitze nicht über der Mitte). Was gilt für die Volumina?',
                                'Sie sind gleich groß.', ['Die gerade Pyramide hat das größere Volumen.', 'Die schiefe Pyramide hat das größere Volumen.', 'Das hängt von der Neigung ab.'],
                                'Prinzip von Cavalieri: In jeder Höhe sind die Querschnitte gleich groß, also auch die Volumina. V = 1/3 · G · h gilt für beide.',
                                'Vergleiche die Querschnittsflächen in gleicher Höhe.'))
    w, c = rz((1.1 ** 3 - 1) * 100, 1)
    neu('verstehen', 3, zahl('Alle Längen eines Kegels werden um 10 % vergrößert. Um wie viel Prozent wächst sein Volumen? Runde auf eine Nachkommastelle.',
                             f'Längenfaktor 1,1 ⇒ Volumenfaktor 1,1³ = 1,331. Das Volumen wächst um {dz(w)} %.', 'Volumen ~ Länge³.', w, c, einheit='%', tol=0.1))
    neu('verstehen', 3, zahl('Ein Kegel und ein Zylinder haben dieselbe Grundfläche und dasselbe Volumen. Wie viel-mal so hoch wie der Zylinder ist der Kegel?',
                             '1/3 · G · h_K = G · h_Z ⇒ h_K = 3 · h_Z.', 'Setze die Volumenformeln gleich.', 3, '3'))
    neu('verstehen', 3, auswahl('Jemand sagt: „Eine Halbkugel hat die halbe Oberfläche der Kugel, also 2πr².“ Was stimmt?', 'Falsch: Dazu kommt die Schnittfläche πr², zusammen 3πr².',
                                ['Richtig.', 'Falsch: Die Oberfläche ist 4πr².', 'Falsch: Die Oberfläche ist 2/3 · πr³.'],
                                'Die gewölbte Fläche ist 2πr². Die Halbkugel hat aber auch eine ebene Kreisfläche πr² als Boden: O = 3πr².',
                                'Welche Flächen begrenzen eine Halbkugel?'))
    return N


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_datei  # noqa: E402

BF = Befunde('raum.pyramide_kegel_kugel', 13_10_6)
# a) nur große Zahlen, derselbe Gedanke wie Stufe 1 (V = 1/3 · G · h)
BF.stufe('sachkontext', 'Eine quadratische Pyramide (als Modell eines Bauwerks) hat die Grundkante 230 m und die Höhe 146 m. Berechne das Volumen auf ganze m³.', 2)
# c) dreimal dieselbe Aufgabe (12-/24-/100-Eck), Antwort immer gleich → zwei andere Stufe-1-Fragen
BF.ersetze('verstehen', 'Eine Pyramide hat als Grundfläche ein regelmäßiges 100-Eck. Was passiert, wenn man die Eckenzahl immer weiter erhöht?', BF.Z(
    'Wie viele Ecken hat eine Pyramide, deren Grundfläche ein regelmäßiges 12-Eck ist?', 13, '12 + 1',
    'Die Grundfläche hat 12 Ecken, dazu kommt die Spitze: 12 + 1 = 13 Ecken.', 'Zähle die Ecken der Grundfläche und die Spitze.'))
BF.ersetze('verstehen', 'Eine Pyramide hat als Grundfläche ein regelmäßiges 12-Eck. Was passiert, wenn man die Eckenzahl immer weiter erhöht?', BF.A(
    'Welcher Körper hat genau eine Spitze und eine kreisförmige Grundfläche?', 'Kegel', ['Zylinder', 'Kugel', 'Pyramide'],
    'Der Kegel hat eine Kreisfläche als Grundfläche und eine Spitze. Der Zylinder hat zwei Kreisflächen, die Pyramide ein Vieleck als Grundfläche, die Kugel weder Grundfläche noch Spitze.',
    'Stell dir eine Eiswaffel vor.'))
# a) gleicher Typ wie Stufe 2 („Radius ver-n-facht – wie ändert sich …?“)
BF.stufe('verstehen', 'Der Radius einer Kugel wird verdreifacht. Wie ändert sich das Volumen?', 2)
BF.stufe('verstehen', 'Der Radius einer Kugel wird vervierfacht. Wie ändert sich das Volumen?', 2)
# b) Schreibweise „64/3π“ mehrdeutig → „64π/3“
BF.loesung('kegel_volumen', 'Ein Kegel hat den Radius r = 2 cm und die Höhe h = 16 cm. Berechne sein Volumen auf eine Nachkommastelle.',
           w='V = ⅓ · π · 2² · 16 = 64π/3 ≈ 67,0 cm³.')
BF.loesung('kegel_volumen', 'Ein Kegel hat den Radius r = 11 cm und die Höhe h = 19 cm. Berechne sein Volumen auf eine Nachkommastelle.',
           w='V = ⅓ · π · 11² · 19 = 2 299π/3 ≈ 2 407,5 cm³.')
# b) zwei Nachkommastellen verlangt, Weg zeigt nur eine
BF.loesung('kugel', 'Eine Kugel hat das Volumen 4 312 cm³. Berechne ihren Radius auf zwei Nachkommastellen.',
           w='r³ = 3V : (4π) = 12 936 : (4π) ⇒ r = ∛(…) ≈ 10,10 cm.')

# ---- BEFUNDE ENDE ----

# ---------- Achtzehnte Runde (Zweig luecken-kl10): Volumen schiefer Prismen ----------
# Lücke laut Aufbau-Prüfung (inhalte/pruefung/aufbau/klasse10.json): LehrplanPLUS M10 5 verlangt, ausgehend von geraden Prismen plausibel zu
# machen, dass auch für schiefe Prismen V = G · h gilt (z. B. mit dem Prinzip von Cavalieri). Die Karte „verstehen“ bekommt dazu einen
# fünften Schritt mit Zeichnung (gerades und schiefes Prisma von der Seite, gleich breit und gleich hoch) und 6 Übungen.
# Läuft ganz am Ende mit eigenem Zufallsstart; alle alten Aufgaben bleiben gleich.
# Prüfungsvorbild (Typ und Niveau, eigene Zahlen): Körperberechnungen in Sachkontexten mit Längen und Winkeln (LehrplanPLUS M10 5,
# Schulaufgaben Jgst. 10): Höhe eines schiefen Körpers aus Seitenkante und Neigungswinkel.
SCHRITT_SCHIEF = {
    'text': 'Schiefes Prisma: wie ein schräg geschobener Stapel gleicher Platten, also ⟦V = G · h⟧.',
    'bild': {'typ': 'figur',
             'punkte': {'_A': [0, 0], '_B': [2, 0], '_C': [2, 3], '_D': [0, 3], '_E': [4, 0], '_F': [6, 0], '_G': [7.5, 3], '_H': [5.5, 3], '_L': [5.5, 0],
                        '_a1': [0, 1], '_b1': [2, 1], '_a2': [0, 2], '_b2': [2, 2], '_e1': [4.5, 1], '_f1': [6.5, 1], '_e2': [5, 2], '_f2': [7, 2]},
             'linien': [['_A', '_B', 'G'], ['_B', '_C', 'h'], ['_C', '_D', ''], ['_D', '_A', ''], ['_E', '_F', 'G'], ['_F', '_G', ''], ['_G', '_H', ''], ['_H', '_E', ''],
                        ['_H', '_L', 'h', 'gestrichelt'], ['_a1', '_b1', '', 'gestrichelt'], ['_a2', '_b2', '', 'gestrichelt'],
                        ['_e1', '_f1', '', 'gestrichelt'], ['_e2', '_f2', '', 'gestrichelt']],
             'rechter_winkel': [['_L', '_F', '_H']],
             'label': 'gerade und schief: gleiche Platten'}}


def luecken_kl10():
    start(18040)
    U = []

    def neu(s, a):
        assert a is not None
        a['p'], a['s'] = 'uebung', s
        U.append(a)

    G, h = 12, 5
    neu(1, zahl(f'Ein schiefes Prisma hat die Grundfläche {G} cm² und die Höhe {h} cm. Wie groß ist sein Volumen?',
                f'Auch beim schiefen Prisma gilt V = G · h = {G} cm² · {h} cm = {G * h} cm³.', 'Schief oder gerade: Was zählt, ist die Höhe senkrecht zur Grundfläche.',
                G * h, f'{G} * {h}', einheit='cm³'))
    g_, hd, H = 6, 4, 10
    neu(2, zahl(f'Ein schiefes Prisma hat ein Dreieck als Grundfläche (Grundseite {g_} cm, zugehörige Höhe {hd} cm). Der Abstand von Grund- und Deckfläche beträgt {H} cm. Wie groß ist das Volumen?',
                f'G = {g_} · {hd} : 2 = {g_ * hd // 2} cm². V = G · h = {g_ * hd // 2} · {H} = {g_ * hd // 2 * H} cm³.',
                'Berechne zuerst die Dreiecksfläche. Die Höhe des Prismas ist der Abstand der beiden Dreiecke.', g_ * hd // 2 * H, f'{g_} * {hd} / 2 * {H}', einheit='cm³'))
    neu(2, auswahl('Ein gerades und ein schiefes Prisma haben dieselbe Grundfläche und beide den Abstand 8 cm zwischen Grund- und Deckfläche. Die Seitenkanten des schiefen Prismas sind 10 cm lang. Was gilt für die Volumina?',
                   'Beide haben dasselbe Volumen.', ['Das schiefe Prisma hat das größere Volumen, weil seine Kanten länger sind.', 'Das schiefe Prisma hat das kleinere Volumen, weil es schräg steht.',
                                                     'Das schiefe Prisma hat ein Drittel des Volumens.'],
                   'In jeder Höhe sind die Querschnitte gleich groß (Cavalieri). Beide haben V = G · 8 cm. Die schräge Kante von 10 cm ist nicht die Höhe.',
                   'Vergleiche die Querschnitte in jeder Höhe.'))
    G, s, w = 20, 10, 30
    wahr = G * s * math.cos(math.radians(w))
    v = gerundet(wahr, 0)
    neu(3, zahl(f'Ein schiefes Prisma hat die Grundfläche {G} cm². Seine Seitenkanten sind {s} cm lang und um {w}° gegen die Senkrechte geneigt. Wie groß ist sein Volumen? Runde auf ganze cm³.',
                f'Höhe h = {s} · cos {w}° ≈ {dz(round(s * math.cos(math.radians(w)), 3))} cm (rechtwinkliges Dreieck aus Kante, Höhe und Verschiebung). V = G · h ≈ {G} · {dz(round(s * math.cos(math.radians(w)), 3))} ≈ {dz(v)} cm³.',
                'Die Höhe ist nicht die Kante. Zeichne das rechtwinklige Dreieck aus Kante und Höhe; der Winkel liegt an der Senkrechten.',
                v, f'round({G} * {s} * {K(math.cos(math.radians(w)))})', einheit='cm³', tol=1))
    G, s, h = 10, 13, 12
    neu(3, auswahl(f'Bei einem schiefen Prisma ist G = {G} cm², die schräge Seitenkante {s} cm und die Höhe {h} cm. Jemand rechnet V = G · {s} cm = {G * s} cm³. Was stimmt?',
                   f'Falsch: V = G · h = {G} · {h} = {G * h} cm³; die Kante ist nicht die Höhe.',
                   ['Richtig.', f'Falsch: V = 1/3 · G · h = {G * h // 3} cm³.', f'Falsch: V = G · ({s} − {h}) = {G * (s - h)} cm³.'],
                   f'Das Volumen hängt von der Höhe senkrecht zur Grundfläche ab, nicht von der schrägen Kante: V = {G} · {h} = {G * h} cm³. 1/3 gehört zu Pyramide und Kegel.',
                   'Welche Länge steht in V = G · h?'))
    n, d, dicke = 20, Fr(26, 10), Fr(22, 10)
    hc = n * dicke / 10
    wahr = math.pi * float(d / 2) ** 2 * float(hc)
    v = gerundet(wahr, 1)
    neu(3, zahl(f'Ein Stapel aus {n} gleichen Münzen (Durchmesser {dz(d)} cm, Dicke {dz(dicke)} mm) wird schräg verschoben. Wie groß ist das Volumen des schiefen Stapels? Runde auf eine Nachkommastelle.',
                f'Schräg verschieben ändert keine Schicht (Cavalieri): wie ein Zylinder mit r = {dz(d / 2)} cm und h = {n} · {dz(dicke)} mm = {dz(hc)} cm. V = π · {dz(d / 2)}² · {dz(hc)} ≈ {dz(v)} cm³.',
                'Wie hoch ist der Stapel? Ändert das Verschieben die Fläche einer Münze?', v, f'round({PI} * {float(d / 2)} ** 2 * {float(hc)}, 1)', einheit='cm³', tol=0.1))
    return U


def luecken_einbauen():
    from _luecken_kl10 import karte_erweitern, offen_ergaenzen
    karte_erweitern('raum.pyramide_kegel_kugel', 'verstehen', [SCHRITT_SCHIEF], luecken_kl10())
    offen_ergaenzen('raum.pyramide_kegel_kugel', 'Achtzehnte Runde (luecken-kl10): Karte „verstehen“ um einen Schritt zu schiefen Prismen (V = G · h, Cavalieri; '
                    'Zeichnung: gerades und schiefes Prisma von der Seite, gleich breit und gleich hoch) und 6 Übungen ergänzt (LehrplanPLUS M10 5). '
                    'Rotationskörper stehen in raum.schraegbilder (seit D2 Klasse 10). Schrägbild und Netz des Kegels bleiben offen (App).')


if __name__ == '__main__':
    datei = bauen('raum.pyramide_kegel_kugel',
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
    ergaenzen(datei, schwer())
    befunde_datei(BF.thema, BF)  # BEFUNDE: erst nach der Zehnten Runde anwenden
    luecken_einbauen()  # Achtzehnte Runde (luecken-kl10): verstehen um schiefe Prismen erweitert – ganz am Ende


# ---------- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl10) ----------
# Gesamtdurchsicht Klasse 10: jede Lernkarte und jede Aufgabe gelesen und nachgerechnet. Läuft ganz am Ende auf der fertigen Datei.
# Stufe 1 = vorgerechnetes Beispiel mit anderen Zahlen, Stufe 2 = Abwandlung/Umkehrung, Stufe 3 = anderer Gedanke.
def durchsicht():
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _durchsicht_kl10 import Durchsicht
    D = Durchsicht('raum.pyramide_kegel_kugel', 19090)
    # pyr_volumen: Dreieck als Grundfläche ist nur eine andere Grundfläche, kein neuer Gedanke → Stufe 2
    D.stufe([13, 15], 2, 'Eine Pyramide hat als Grundfläche ein Dreieck')
    # pyr_oberflaeche: Oberfläche aus a und h ist genau das vorgerechnete Beispiel der Karte → Stufe 1;
    # Aufgabe 41 hatte sogar die Zahlen der Karte (a = 6, h = 4) → ersetzt durch andere Zahlen
    D.stufe([40, 42, 43, 44, 45], 1, 'Eine quadratische Pyramide hat die Grundkante')
    D.ersetze(41, 'Eine quadratische Pyramide hat die Grundkante 6 cm und die Höhe 4 cm',
              D.Z('Eine quadratische Pyramide hat die Grundkante 12 cm und die Höhe 8 cm. Berechne ihre Oberfläche.', 384, '12 ** 2 + 2 * 12 * 10',
                  'hₛ = √(8² + 6²) = 10 cm; O = 12² + 4 · ½ · 12 · 10 = 144 + 240 = 384 cm².', 'Erst hₛ mit Pythagoras, dann O = G + M.', einheit='cm²',
                  grafik={'typ': 'figur', 'punkte': {'S': [0, 8], 'M': [0, 0], 'F': [6.0, 0], '_G': [-6.0, 0]}, 'flaeche': ['_G', 'F', 'S'],
                          'linien': [['_G', 'F', ''], ['_G', 'S', ''], ['S', 'F', 'hₛ'], ['M', 'F', 'a/2 = 6'], ['M', 'S', 'h = 8', 'gestrichelt']],
                          'rechter_winkel': [['M', 'F', 'S']], 'label': 'Schnitt durch die Pyramide: Höhe, halbe Grundkante, Seitenhöhe'}), s=1)
    # kegel_volumen: Höhe aus dem Volumen ist eine Umkehrung → Stufe 2
    D.stufe(range(68, 74), 2, 'Ein Kegel mit dem Radius')
    # kegel_mantel: Oberfläche aus r und h = Kette der Karte (s, dann M) plus Boden → Stufe 2; Sektor → Grundkreis = Umkehrung der Winkelformel → Stufe 2
    D.stufe([96, 97, 99, 100], 2, 'Ein Kegel hat den Radius')
    D.stufe([98, 101], 2, 'Aus einem Kreissektor')
    # kugel: Radius aus Volumen/Oberfläche ist eine Umkehrung → Stufe 2
    D.stufe([124, 125, 128, 129], 2, 'Eine Kugel hat')
    D.stufe([126, 127], 2, 'Ein Globus')
    # sachkontext: Pyramidenvolumen mit großen Zahlen ist kein anderer Gedanke → Stufe 2
    D.stufe([153, 157], 2, 'Eine quadratische Pyramide (als Modell')
    # verstehen: Fehler „π · r · h“ ist auf Stufe 2 schon dreimal da → Stufe 2
    D.stufe([180, 184, 185], 2, 'Jemand rechnet die Mantelfläche eines Kegels')
    D.fuer_sebastian('raum.pyramide_kegel_kugel/verstehen: Zwei Übungen haben denselben Fragetext („Bei einem Kegel wird nur die Höhe verdoppelt. …“, Stufe 1 und Stufe 2). '
                     'Nicht ersetzt, weil die Sperre nach Fragetext beide träfe – eine davon bitte löschen oder umformulieren lassen.')
    D.fuer_sebastian('raum.pyramide_kegel_kugel: Schrägbild und Netz von Pyramide und Kegel (M10 5) fehlen als eigene Aufgaben; '
                     'die App kann Kegel-Schrägbilder und Kegelnetze nicht zeichnen (App-Wunsch).')
    D.anwenden()


if __name__ == '__main__':
    durchsicht()  # Neunzehnte Runde (durchsicht-kl10) – ganz am Ende


# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl10) ----------
def stufen():
    import math as _m
    import sys as _sys
    _sys.path.insert(0, str(Path(__file__).resolve().parent))
    from _stufen_kl10 import Stufen
    S = Stufen('raum.pyramide_kegel_kugel', 2090)
    Z, A, L, ZR = S.Z, S.A, S.L, S.ZR
    pi = _m.pi

    # --- pyr_volumen ---
    S.stufenleiter('pyr_volumen', 'V = 1/3 · G · h für quadratische Pyramiden anwenden; Formel und Höhe erkennen.',
                   'Höhe aus dem Volumen, rechteckige und dreieckige Grundflächen, Pyramide im Würfel.',
                   'Höhe und Seitenkanten mit Pythagoras, Würfelecke abschneiden, x als Parameter, Volumenverhältnisse begründen, Fehler „ohne 1/3“, Prüfungsaufgabe.')
    S.g('pyr_volumen', direkt=[0, 1, 2, 3, 4, 5], umkehr=[6, 7, 10, 196], mehrschritt=[8, 9, 11, 13, 15], einkleidung=[197],
        verknuepfen=[12, 16], pruefung=[14, 17], transfer=[198, 201], parameter=[199], begruenden=[200])
    S.ueberzaehlig(15, 17)
    S.neu('pyr_volumen', 'erkennen', A('Welche Formel gilt für das Volumen jeder Pyramide?', 'V = 1/3 · G · h', ['V = G · h', 'V = 1/2 · G · h', 'V = 1/3 · a · h'],
                                       'Eine Pyramide fasst ein Drittel des Prismas mit gleicher Grundfläche und Höhe.', 'Denke an das Zelt und die Kiste.'))
    S.neu('pyr_volumen', 'erkennen', A('Was ist bei einer Pyramide die Höhe h?', 'der senkrechte Abstand der Spitze von der Grundfläche', ['die Länge einer Seitenkante', 'die Höhe eines Seitendreiecks', 'die Länge einer Grundkante'],
                                       'h wird senkrecht gemessen, von der Spitze bis zur Grundfläche.', 'Wie misst man die Höhe eines Zelts?'))
    S.neu('pyr_volumen', 'fehler', A('Jemand berechnet das Volumen einer quadratischen Pyramide (a = 6 cm, h = 5 cm) als 6 · 6 · 5 = 180 cm³. Was stimmt?', 'Falsch: Es fehlt der Faktor 1/3; V = 60 cm³.',
                                     ['Richtig.', 'Falsch: V = 1/2 · 180 = 90 cm³.', 'Falsch: V = 6 · 5 = 30 cm³.'], '180 cm³ ist das Volumen des Quaders mit gleicher Grundfläche und Höhe. Die Pyramide fasst ein Drittel.',
                                     'Was passt in die Kiste, was ins Zelt?'))
    S.bonus('pyr_volumen', L('Eine Pyramide wird auf halber Höhe parallel zur Grundfläche durchgeschnitten. Welcher Anteil ihres Volumens liegt im oberen Teil?', '□/□', [1, 8], ['1', '8'],
                             'Der obere Teil ist eine kleine Pyramide mit halber Höhe und halben Grundkanten. Grundfläche ein Viertel, Höhe die Hälfte: 1/4 · 1/2 = 1/8.',
                             'Wie ändern sich Grundfläche und Höhe der kleinen Pyramide?', hinweis='gekürzter Bruch'))
    S.bonus('pyr_volumen', Z('In einem Würfel mit der Kante 6 cm verbindet man vier Ecken, von denen keine zwei an derselben Kante liegen, zu einem Tetraeder. Welches Volumen hat es?', 72, '216 - 4 * 36',
                             'Vom Würfel (216 cm³) werden vier Eckpyramiden abgeschnitten, jede mit V = 1/3 · (1/2 · 6 · 6) · 6 = 36 cm³. Übrig: 216 − 144 = 72 cm³ – genau ein Drittel des Würfels.',
                             'Was wird vom Würfel weggeschnitten?', einheit='cm³'))

    # --- pyr_oberflaeche ---
    S.stufenleiter('pyr_oberflaeche', 'Seitenhöhe mit Pythagoras und Oberfläche O = G + M wie im Beispiel; Bestandteile erkennen.',
                   'Mantel aus der Seitenhöhe, Seitenhöhe rückwärts, Dächer und Zelte.',
                   'Neigungswinkel, Tetraeder, Oberfläche als Vielfaches der Grundfläche, Höhe als Parameter, Begründen hₛ > h, Farbbedarf, Oberfläche aus Seitenkanten wie in der Prüfung.')
    S.g('pyr_oberflaeche', direkt=[28, 29, 30, 31, 32, 33, 40, 41, 42, 43, 44, 45], darstellung=[34, 35, 36, 37, 38, 39], mehrschritt=[202], umkehr=[203],
        verknuepfen=[204], transfer=[205], rueckwaerts=[206], fehler=[207])
    S.ueberzaehlig(29)
    S.neu('pyr_oberflaeche', 'erkennen', A('Woraus besteht die Oberfläche einer quadratischen Pyramide?', 'aus dem Quadrat und vier Dreiecken', ['aus vier Dreiecken', 'aus zwei Quadraten und vier Rechtecken', 'aus fünf Quadraten'],
                                           'Oberfläche = Grundfläche (Quadrat) + Mantel (vier gleiche Dreiecke).', 'Denke an das Zelt mit Boden.'))
    S.neu('pyr_oberflaeche', 'erkennen', A('Welche Strecke braucht man für den Flächeninhalt eines Seitendreiecks?', 'die Seitenhöhe hₛ', ['die Höhe h der Pyramide', 'die Seitenkante', 'die Diagonale der Grundfläche'],
                                           'Dreiecksfläche = Grundseite · Höhe : 2; die Höhe des Seitendreiecks ist hₛ.', 'Welche Höhe gehört zum Dreieck selbst?'))
    S.neu('pyr_oberflaeche', 'einkleidung', Z('Ein Zeltdach (quadratische Pyramide, Grundkante 4 m, Seitenhöhe 3 m) wird ohne Boden mit Stoff bespannt. Wie viel m² Stoff braucht man?', 24, '4 * 4 * 3 / 2',
                                              'Vier Dreiecke: 4 · (4 · 3 : 2) = 24 m².', 'Nur der Mantel, kein Boden.', einheit='m²'))
    S.neu('pyr_oberflaeche', 'einkleidung', Z('Ein Turmdach ist eine quadratische Pyramide mit Grundkante 6 m und Höhe 4 m. Wie viel m² Dachfläche hat es?', 60, '4 * 6 * 5 / 2',
                                              'hₛ = √(4² + 3²) = 5 m. Mantel 4 · (6 · 5 : 2) = 60 m².', 'Erst die Seitenhöhe, dann vier Dreiecke.', einheit='m²'))
    S.neu('pyr_oberflaeche', 'parameter', Z('Für welche Höhe h hat eine quadratische Pyramide mit Grundkante 10 cm die Seitenhöhe 13 cm?', 12, '12',
                                            'hₛ² = h² + 5² ⇒ 169 = h² + 25 ⇒ h² = 144 ⇒ h = 12 cm.', 'Stelle den Pythagoras mit h auf.', einheit='cm'))
    S.neu('pyr_oberflaeche', 'begruenden', A('Kann die Seitenhöhe hₛ einer Pyramide kleiner sein als ihre Höhe h?', 'Nein: hₛ ist die Hypotenuse im Dreieck aus h und a/2, also länger als h.',
                                             ['Ja, bei sehr flachen Pyramiden.', 'Ja, bei sehr spitzen Pyramiden.', 'Nein, beide sind immer gleich lang.'],
                                             'hₛ² = h² + (a/2)² > h², weil a/2 > 0.', 'Welche Seite im rechtwinkligen Dreieck ist die längste?'))
    S.neu('pyr_oberflaeche', 'pruefung', ZR('Eine quadratische Pyramide hat die Grundkante 8 cm, ihre Seitenkanten sind 9 cm lang. Berechne die Oberfläche. Runde auf eine Nachkommastelle.', 64 + 4 * 8 * _m.sqrt(65) / 2, 1,
                                            'Seitenhöhe im Seitendreieck: hₛ = √(9² − 4²) = √65 ≈ 8,06 cm. M = 4 · (8 · 8,06 : 2) ≈ 129,0 cm²; O = 64 + 129,0 = 193,0 cm².',
                                            'Die Seitenhöhe liegt im Seitendreieck: Seitenkante und halbe Grundkante.', einheit='cm²'))
    S.neu('pyr_oberflaeche', 'transfer', Z('Ein Dach in Form einer quadratischen Pyramide hat die Grundkante 10 m und die Seitenhöhe 13 m. Ein Liter Farbe reicht für 8 m². Wie viele ganze Liter braucht man mindestens für die vier Dachflächen?',
                                           33, '33', 'Mantel 4 · (10 · 13 : 2) = 260 m². 260 : 8 = 32,5, also 33 Liter.', 'Erst die Fläche, dann aufrunden.', einheit='l'))
    S.bonus('pyr_oberflaeche', ZR('Eine quadratische Pyramide hat lauter gleich lange Kanten (4 cm). Wie groß ist ihre Oberfläche? Runde auf eine Nachkommastelle.', 16 + 16 * _m.sqrt(3), 1,
                                  'Die Seitenflächen sind gleichseitige Dreiecke mit der Fläche √3/4 · 16 ≈ 6,93 cm². O = 16 + 4 · 6,93 ≈ 43,7 cm².', 'Welche Form haben die Seitenflächen?', einheit='cm²'))
    S.bonus('pyr_oberflaeche', ZR('Auf jede Fläche eines Würfels (Kante 2 cm) wird eine quadratische Pyramide mit der Höhe 1 cm gesetzt. Wie groß ist die Oberfläche des neuen Körpers? Runde auf eine Nachkommastelle.',
                                  24 * _m.sqrt(2), 1, 'Die Würfelflächen liegen innen. Jede Pyramide: hₛ = √(1² + 1²) = √2, Mantel 4 · (2 · √2 : 2) = 4√2. Sechs Pyramiden: 24√2 ≈ 33,9 cm².',
                                  'Welche Flächen sind außen sichtbar?', einheit='cm²'))

    # --- kegel_volumen ---
    S.stufenleiter('kegel_volumen', 'V = 1/3 · π · r² · h anwenden; Formel und nötige Größen erkennen.',
                   'Durchmesser statt Radius, Höhe rückwärts, Kegel als Drittel eines Zylinders.',
                   'Halbe Füllhöhe, Schätzen, h = r als Parameter, Kegel und Kugel vergleichen, Fehler mit dem Durchmesser, Begründen, Radius rückwärts, Waffel wie in der Prüfung.')
    S.g('kegel_volumen', direkt=[56, 57, 58, 59, 60, 61], einkleidung=[62, 63, 64, 65, 66, 67], umkehr=[68, 69, 70, 71, 72, 73, 208], darstellung=[209],
        verknuepfen=[210, 213], transfer=[211], parameter=[212])
    S.neu('kegel_volumen', 'erkennen', A('Welche Formel gilt für das Volumen eines Kegels?', 'V = 1/3 · π · r² · h', ['V = π · r² · h', 'V = 1/3 · π · r · h', 'V = 1/2 · π · r² · h'],
                                         'Ein Kegel fasst ein Drittel des Zylinders mit gleichem Radius und gleicher Höhe.', 'Denke an die Waffeltüte und den Becher.'))
    S.neu('kegel_volumen', 'erkennen', A('Welche Größe braucht man außer dem Radius, um das Volumen eines Kegels zu berechnen?', 'die Höhe h', ['den Umfang', 'den Mittelpunktswinkel', 'nichts weiter'],
                                         'V = 1/3 · π · r² · h: r und h.', 'Welche Buchstaben stehen in der Formel?'))
    S.neu('kegel_volumen', 'fehler', A('Jemand berechnet einen Kegel mit d = 10 cm und h = 6 cm: V = 1/3 · π · 10² · 6 ≈ 628 cm³. Was stimmt?', 'Falsch: Der Radius ist 5 cm; V = 1/3 · π · 25 · 6 ≈ 157 cm³.',
                                       ['Richtig.', 'Falsch: V = π · 10² · 6 ≈ 1 885 cm³.', 'Falsch: V = 1/3 · π · 10 · 6 ≈ 63 cm³.'], 'In die Formel gehört der Radius, nicht der Durchmesser – sonst wird V viermal zu groß.',
                                       'Ist 10 cm der Radius?'))
    S.neu('kegel_volumen', 'begruenden', A('Ein Kegel und ein Zylinder haben denselben Radius; der Kegel ist dreimal so hoch. Was gilt für die Volumina?', 'Beide sind gleich groß.',
                                           ['Der Kegel ist dreimal so groß.', 'Der Zylinder ist dreimal so groß.', 'Der Kegel ist neunmal so groß.'],
                                           'V_Kegel = 1/3 · π · r² · 3h = π · r² · h = V_Zylinder.', 'Setze 3h in die Kegelformel ein.'))
    S.neu('kegel_volumen', 'pruefung', ZR('Eine Eiswaffel (Kegel) ist 12 cm hoch, ihre Mantellinie ist 13 cm lang. Wie viel cm³ Eis passen hinein (bis zum Rand)? Runde auf ganze cm³.', pi * 25 * 12 / 3, 0,
                                          'r = √(13² − 12²) = 5 cm. V = 1/3 · π · 25 · 12 = 100π ≈ 314 cm³.', 'Bestimme zuerst den Radius mit Pythagoras.', einheit='cm³'))
    S.neu('kegel_volumen', 'rueckwaerts', Z('Ein kegelförmiger Sandhaufen enthält 100π m³ Sand und ist 12 m hoch. Wie groß ist sein Radius?', 5, '5',
                                            '1/3 · π · r² · 12 = 100π ⇒ 4r² = 100 ⇒ r² = 25 ⇒ r = 5 m.', 'Setze ein und teile durch π.', einheit='m'))
    S.bonus('kegel_volumen', ZR('Ein kegelförmiges Glas (Spitze unten) ist genau halb voll. Welcher Anteil der Glashöhe ist mit Saft gefüllt? Runde auf zwei Nachkommastellen.', 0.5 ** (1 / 3), 2,
                                'Der Saft bildet einen kleineren, ähnlichen Kegel mit Radius k · r und Höhe k · h. Sein Volumen ist 1/3 · π · (k · r)² · (k · h) = k³ · (1/3 · π · r² · h), '
                                'also k³-mal das Glasvolumen. k³ = 1/2 ⇒ k = ∛0,5 ≈ 0,79. Bei 79 % der Höhe ist das Glas schon halb voll.',
                                'Wie hängt das Volumen ähnlicher Kegel vom Streckfaktor ab?'))
    S.bonus('kegel_volumen', Z('Ein Kegel wird auf halber Höhe parallel zur Grundfläche zerschnitten. Wievielmal so groß ist das Volumen des unteren Stücks wie das der oberen Spitze?', 7, '8 - 1',
                               'Die Spitze ist ein Kegel mit halbem Radius und halber Höhe: 1/8 des Volumens. Unten bleiben 7/8. Verhältnis 7.', 'Welchen Anteil hat die kleine Spitze?'))

    # --- kegel_mantel ---
    S.stufenleiter('kegel_mantel', 'Mantellinie mit Pythagoras und Mittelpunktswinkel φ = 360° · r : s bestimmen; Kreissektor erkennen.',
                   'Mantelfläche M = π · r · s, Oberfläche, Radius aus einem Sektor, Mantellinie rückwärts.',
                   'Halbkreis-Mantel, Öffnungswinkel, s aus der Oberfläche, Partyhut, Fehler φ = 360° · s : r, Verhältnis als Parameter, Viertelkreis-Mantel wie in der Prüfung.')
    S.g('kegel_mantel', direkt=[84, 89, 85, 86, 87, 88], mehrschritt=[90, 91, 92, 93, 94, 95, 96, 97, 99, 100], umkehr=[98, 101, 215], darstellung=[214],
        verknuepfen=[216], transfer=[217, 219], rueckwaerts=[218])
    S.ueberzaehlig(89, 92, 93, 94, 95)
    S.neu('kegel_mantel', 'erkennen', A('Welche Form hat der abgewickelte Mantel eines Kegels?', 'ein Kreissektor', ['ein Rechteck', 'ein Kreis', 'ein Dreieck'],
                                        'Aufgeschnitten und flach ausgerollt wird die Waffeltüte zu einem „Tortenstück“.', 'Denke an die aufgeschnittene Waffeltüte.'))
    S.neu('kegel_mantel', 'erkennen', A('Welche Strecke ist der Radius des abgewickelten Mantels?', 'die Mantellinie s', ['der Radius r der Grundfläche', 'die Höhe h', 'der Durchmesser'],
                                        'Jeder Punkt des Rands ist im ausgerollten Mantel s von der Spitze entfernt.', 'Wie weit ist der Rand von der Spitze entfernt?'))
    S.neu('kegel_mantel', 'fehler', A('Jemand berechnet für r = 4 cm und s = 8 cm den Mittelpunktswinkel des Mantels als φ = 360° · 8 : 4 = 720°. Was stimmt?', 'Falsch: φ = 360° · r : s = 180°.',
                                      ['Richtig.', 'Falsch: φ = 360° · 4 · 8 = 11 520°.', 'Falsch: φ = 8 : 4 = 2°.'], 'Der Sektor ist kleiner als der volle Kreis (r < s). 720° ist unmöglich.', 'Kann ein Sektor mehr als 360° haben?'))
    S.neu('kegel_mantel', 'parameter', Z('Für welches Verhältnis s : r ist der abgewickelte Mantel eines Kegels genau ein Viertelkreis?', 4, '360 // 90',
                                         'φ = 360° · r : s = 90° ⇒ r : s = 1 : 4 ⇒ s : r = 4.', 'Setze φ = 90° in die Formel ein.'))
    S.neu('kegel_mantel', 'begruenden', A('Kann der abgewickelte Mantel eines Kegels ein voller Kreis sein?', 'Nein: Dann wäre r = s und die Höhe 0.', ['Ja, bei sehr flachen Kegeln.', 'Ja, wenn r = h ist.', 'Nein, er ist immer ein Halbkreis.'],
                                          'φ = 360° hieße r = s. Dann h = √(s² − r²) = 0 – das wäre kein Kegel mehr.', 'Was folgt aus φ = 360° für r und s?'))
    S.neu('kegel_mantel', 'pruefung', ZR('Aus einem Viertelkreis mit dem Radius 20 cm wird ein Kegelmantel gerollt. Berechne die Höhe des Kegels. Runde auf eine Nachkommastelle.', _m.sqrt(400 - 25), 1,
                                         's = 20 cm. Bogenlänge 2π · 20 : 4 = 10π = Umfang 2πr ⇒ r = 5 cm. h = √(20² − 5²) ≈ 19,4 cm.', 'Der Bogen des Sektors wird zum Umfang des Grundkreises.', einheit='cm'))
    S.bonus('kegel_mantel', Z('Ein Kegel hat den Öffnungswinkel 60° (Winkel an der Spitze im Axialschnitt). Welchen Mittelpunktswinkel hat sein abgewickelter Mantel?', 180, '360 // 2',
                              'Halber Öffnungswinkel 30°: r : s = sin 30° = 1/2. φ = 360° · r : s = 180° – ein Halbkreis.', 'Betrachte das rechtwinklige Dreieck aus h, r und s.', einheit='°'))
    S.bonus('kegel_mantel', ZR('Eine Ameise läuft auf dem Mantel eines Kegels (s = 6 cm, r = 2 cm) von einem Punkt des Randes einmal um den Kegel herum zurück zum selben Punkt. Wie lang ist der kürzeste Weg? Runde auf eine Nachkommastelle.',
                               2 * 6 * _m.sin(_m.radians(60)), 1, 'Abwickeln: Sektor mit s = 6 cm und φ = 360° · 2 : 6 = 120°. Der kürzeste Weg ist die gerade Strecke zwischen den beiden Randpunkten. Sie ist die Grundseite eines gleichschenkligen Dreiecks mit Schenkeln 6 cm und 120° an der Spitze. '
                               'Die Höhe teilt es in zwei rechtwinklige Dreiecke mit 60° an der Spitze: halbe Strecke = 6 · sin 60° ≈ 5,20 cm, ganze Strecke = 2 · 6 · sin 60° ≈ 10,4 cm.',
                               'Wickle den Mantel ab – auf dem flachen Papier ist der kürzeste Weg gerade.', einheit='cm'))

    # --- kugel ---
    S.stufenleiter('kugel', 'Volumen und Oberfläche einer Kugel aus dem Radius berechnen; erkennen, dass der Radius genügt.',
                   'Durchmesser statt Radius, Bälle und Globen, Radius rückwärts, Ergebnisse als Vielfaches von π.',
                   'Wasserspiegel, V = O als Parameter, doppeltes Volumen, Umfang → Liter, Fehler r², Verhältnis V : O begründen, Dichte wie in der Prüfung, Kugeln in einer Schachtel.')
    S.g('kugel', direkt=[112, 113, 114, 115, 116, 117], mehrschritt=[118, 121, 119, 120, 122], einkleidung=[123, 126, 127], umkehr=[124, 125, 128, 129, 221], darstellung=[220],
        transfer=[222], parameter=[223], verknuepfen=[224], rueckwaerts=[225])
    S.ueberzaehlig(117, 120, 121, 122, 125, 127, 129)
    S.neu('kugel', 'erkennen', A('Welche Größe genügt, um Volumen und Oberfläche einer Kugel zu berechnen?', 'der Radius', ['die Höhe', 'der Umfang und die Höhe', 'nur das Gewicht'],
                                 'V = 4/3 · π · r³ und O = 4 · π · r² – nur r kommt vor.', 'Welche Buchstaben stehen in den Formeln?'))
    S.neu('kugel', 'erkennen', A('Welche Einheit hat das Volumen einer Kugel, deren Radius in cm angegeben ist?', 'cm³', ['cm²', 'cm', 'cm⁴'], 'r³ hat die Einheit cm · cm · cm = cm³.', 'Volumen ist dreidimensional.'))
    S.neu('kugel', 'fehler', A('Jemand berechnet das Volumen einer Kugel mit r = 3 cm als 4/3 · π · 3² ≈ 37,7 cm³. Was stimmt?', 'Falsch: Es muss r³ heißen: 4/3 · π · 27 ≈ 113,1 cm³.',
                               ['Richtig.', 'Falsch: 4 · π · 3² ≈ 113,1 cm³ ist das Volumen.', 'Falsch: 4/3 · π · 3 ≈ 12,6 cm³.'],
                               'Ein Volumen braucht drei Längen: r³. (4πr² wäre zufällig dieselbe Zahl – aber das ist die Oberfläche in cm², weil r = 3.)', 'Welche Einheit muss herauskommen?'))
    S.neu('kugel', 'begruenden', A('Man verdoppelt den Radius einer Kugel. Was passiert mit dem Verhältnis Volumen : Oberfläche?', 'Es verdoppelt sich, denn V : O = r : 3.',
                                   ['Es bleibt gleich.', 'Es vervierfacht sich.', 'Es halbiert sich.'], '(4/3 · π · r³) : (4 · π · r²) = r : 3. Doppeltes r, doppeltes Verhältnis.', 'Teile die beiden Formeln durcheinander.'))
    S.neu('kugel', 'pruefung', ZR('Eine Holzkugel (Dichte 0,7 g/cm³) hat den Durchmesser 10 cm. Wie schwer ist sie? Runde auf ganze Gramm.', 4 / 3 * pi * 125 * 0.7, 0,
                                  'r = 5 cm, V = 4/3 · π · 125 ≈ 523,6 cm³. Masse 523,6 · 0,7 ≈ 367 g.', 'Masse = Volumen · Dichte.', einheit='g'))
    S.neu('kugel', 'transfer', ZR('Acht gleiche Kugeln mit r = 1 cm liegen in einer würfelförmigen Schachtel mit der Kante 4 cm. Wie viel Prozent des Schachtelvolumens nehmen sie ein? Runde auf eine Nachkommastelle.',
                                  8 * 4 / 3 * pi / 64 * 100, 1, '8 · 4/3 · π ≈ 33,5 cm³; Schachtel 64 cm³. Anteil ≈ 52,4 % – genau so viel wie eine einzige große Kugel im Würfel.', 'Vergleiche die Volumina.', einheit='%'))
    S.bonus('kugel', A('Eine Kugel und ein Würfel haben dieselbe Oberfläche. Welcher Körper hat das größere Volumen?', 'die Kugel', ['der Würfel', 'Beide haben dasselbe Volumen.'],
                       'Beispiel: O = 4π ≈ 12,57 cm². Kugel: r = 1, V ≈ 4,19 cm³. Würfel: 6a² = 12,57 ⇒ a ≈ 1,45, V ≈ 3,04 cm³. Die Kugel umschließt bei gleicher Hülle am meisten Volumen.',
                       'Rechne ein Beispiel mit r = 1.'))
    S.bonus('kugel', Z('Wie viele Kugeln mit r = 1 cm haben zusammen dasselbe Volumen wie eine Kugel mit r = 3 cm?', 27, '3 ** 3',
                       'Volumen wächst mit r³: 3³ = 27. Aber Achtung: In die große Kugel passen gar nicht 27 kleine hinein – zwischen Kugeln bleiben Lücken.', 'Wie hängt das Volumen vom Radius ab?'))

    # --- sachkontext ---
    S.stufenleiter('sachkontext', 'Einen Körper in der Sachsituation erkennen und sein Volumen berechnen; Teilkörper benennen.',
                   'Zusammengesetzte Körper addieren oder abziehen, Hohlkugeln, Dachflächen, Größen rückwärts.',
                   'Öffnungswinkel mit tan, Dichte, schiefe Pyramide wie in der Prüfung, Sektor → Kegel, Späne beim Drechseln, Fehler „ganze Kugel statt Halbkugel“.')
    S.g('sachkontext', direkt=[140, 141, 142, 143, 144, 145], mehrschritt=[146, 149, 151, 227], einkleidung=[147, 150, 148, 152, 153, 157], umkehr=[226],
        verknuepfen=[154, 155, 231], transfer=[156, 230], pruefung=[228, 229])
    S.ueberzaehlig(150, 151, 153, 157)
    S.neu('sachkontext', 'erkennen', A('Ein Turm besteht aus einem Zylinder mit einem kegelförmigen Dach. Wie berechnet man sein Volumen?', 'Zylindervolumen + Kegelvolumen', ['nur das Zylindervolumen', 'Zylindervolumen − Kegelvolumen', 'Zylindervolumen · Kegelvolumen'],
                                       'Zusammengesetzte Körper: Teilvolumen addieren.', 'Aus welchen Teilen besteht der Turm?'))
    S.neu('sachkontext', 'erkennen', A('Welche Formel gehört zum Volumen einer Halbkugel?', '2/3 · π · r³', ['4/3 · π · r³', '2 · π · r²', '1/3 · π · r³'], 'Die Hälfte von 4/3 · π · r³.', 'Halbiere die Kugelformel.'))
    S.neu('sachkontext', 'fehler', A('Eine Eistüte: Kegel (r = 3 cm, h = 10 cm) mit einer Halbkugel Eis. Jemand rechnet V = 1/3 · π · 9 · 10 + 4/3 · π · 27 ≈ 207 cm³. Was stimmt?',
                                     'Falsch: Oben sitzt nur eine Halbkugel (2/3 · π · 27); V ≈ 94,2 + 56,5 ≈ 150,8 cm³.', ['Richtig.', 'Falsch: Der Kegel hat π · 9 · 10.', 'Falsch: Man muss die Volumina abziehen.'],
                                     'Mit der ganzen Kugel wäre das Eis doppelt so viel.', 'Wie viel von der Kugel sitzt auf der Tüte?'))
    S.bonus('sachkontext', L('In einem Zylinder (r = 3 cm, h = 6 cm) liegt eine Kugel mit r = 3 cm. Der Rest wird mit Wasser bis zum Rand gefüllt. Welcher Anteil des Zylinders ist Wasser?', '□/□', [1, 3], ['1', '3'],
                             'Zylinder: π · 9 · 6 = 54π; Kugel: 4/3 · π · 27 = 36π. Wasser 18π, also 18/54 = 1/3 (Archimedes: Kugel = 2/3 des Zylinders).', 'Berechne beide Volumina als Vielfache von π.', hinweis='gekürzter Bruch'))
    S.bonus('sachkontext', Z('Eine Kugel mit r = 6 cm wird ganz in ein zylindrisches Glas (Innenradius 8 cm) mit Wasser getaucht. Um wie viel cm steigt der Wasserspiegel?', 4.5, '4 * 216 / (3 * 64)',
                             'Verdrängtes Volumen 4/3 · π · 216 = 288π. Steighöhe 288π : (π · 64) = 4,5 cm.', 'Das Kugelvolumen verteilt sich als Zylinderschicht.', einheit='cm'))

    # --- verstehen ---
    S.stufenleiter('verstehen', 'Körper und Volumenformeln erkennen; einfache Folgen einer Längenänderung angeben.',
                   'Flächen und Volumina beim Strecken mit k, k² und k³, Sachsituationen mit Maßstab, Streckfaktor rückwärts.',
                   'Fehler „π · r · h“ und bei Halbkugel und schiefem Prisma, Archimedes, Cavalieri begründen, Prozentänderung, Term deuten, schiefe Prismen mit Trigonometrie.')
    S.g('verstehen', erkennen=[168, 170, 172, 233], direkt=[169, 171, 173, 238, 232], mehrschritt=[174, 179, 181, 183, 175, 176, 239], fehler=[177, 178, 180, 184, 185, 237, 242],
        verknuepfen=[182, 241], begruenden=[234, 240], transfer=[235, 243], rueckwaerts=[236])
    S.ueberzaehlig(232, 179, 183, 175, 178)
    S.neu('verstehen', 'einkleidung', Z('Ein Modellauto ist im Maßstab 1 : 10 gebaut. Wievielmal so viel Lack (Fläche) braucht das echte Auto?', 100, '10 ** 2', 'Flächen wachsen mit k² = 10² = 100.', 'Wie ändern sich Flächen beim Vergrößern mit k?'))
    S.neu('verstehen', 'einkleidung', Z('Eine Orange hat den doppelten Durchmesser einer Mandarine (beide kugelförmig). Wievielmal so viel Volumen hat sie?', 8, '2 ** 3', 'Volumen wächst mit k³ = 2³ = 8.', 'Wie ändert sich das Volumen bei doppeltem Radius?'))
    S.neu('verstehen', 'umkehr', Z('Das Volumen einer Kugel wird 27-mal so groß. Mit welchem Faktor wurde der Radius multipliziert?', 3, '3', 'k³ = 27 ⇒ k = 3.', 'Welche Zahl hoch drei ergibt 27?'))
    S.bonus('verstehen', L('Ein Kegel, eine Halbkugel und ein Zylinder haben alle den Radius r und die Höhe r. In welchem Verhältnis stehen ihre Volumina (Kegel : Halbkugel : Zylinder)?', '□ : □ : □', [1, 2, 3], ['1', '2', '3'],
                           'Kegel 1/3 · π · r³, Halbkugel 2/3 · π · r³, Zylinder π · r³. Verhältnis 1/3 : 2/3 : 1 = 1 : 2 : 3.', 'Schreibe alle drei als Vielfaches von π · r³.', hinweis='kleinste ganze Zahlen'))
    S.bonus('verstehen', ZR('Bei einem Kegel wird der Radius um 20 % größer und die Höhe um 20 % kleiner. Um wie viel Prozent ändert sich das Volumen? (Zunahme positiv) Runde auf eine Nachkommastelle.', (1.2 ** 2 * 0.8 - 1) * 100, 1,
                            'V ∼ r² · h: 1,2² · 0,8 = 1,44 · 0,8 = 1,152. Das Volumen wächst um 15,2 % – der Radius zählt doppelt.', 'Wie gehen r und h in die Formel ein?', einheit='%'))
    S.anwenden()


if __name__ == '__main__':
    stufen()  # Zwanzigste Runde (stufen-kl10) – ganz am Ende


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('raum.pyramide_kegel_kugel')
# ---- BEREINIGEN ENDE ----
