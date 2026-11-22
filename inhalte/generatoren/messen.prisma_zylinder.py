#!/usr/bin/env python3
"""Thema messen.prisma_zylinder – Prismen und Zylinder (Gymnasium Bayern, Klasse 8, LehrplanPLUS M8 7 „Kreis und Zylinder“).

Achtzehnte Runde, Teil A (Zweig luecken-neu). Baut auf messen.koerper_darstellung (Klasse 8: Prismen zählen, Netze, Schrägbilder) und
messen.kreisberechnung (Klasse 8, Buenos Aires: Kreis, Kreisring, Karte „zylinder“ mit V = π · r² · h und O = 2πr² + 2πrh) auf; die Zylinderkarte
dort wird nicht verschoben und nicht wiederholt, sondern hier begründet und vertieft (Grenzfall eines Prismas, Netz, Hohlzylinder, Umstellen).
Lehrplan M8 7: begründen, dass das Volumen gerader Prismen unabhängig von der Form der Grundfläche G · h ist; Zylinderformel als Grenzfall eines
geraden Prismas plausibel machen; Oberflächenformel des Zylinders mithilfe des Netzes begründen; Volumen- und Oberflächenformeln in Sachzusammenhängen
flexibel nutzen, sinnvolle Annahmen treffen. Kein Satz des Pythagoras (erst Klasse 9): alle schrägen Kanten sind angegeben.

Je Lernkarte: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; davon 2 nach Prüfungsvorbild und 1 Knobelaufgabe), 1 Test, 3 Korrektur, 6 Sicherung.
Prüfungsvorbilder (nur Typ und Niveau, eigene Zahlen und Einkleidung): Bayerischer Mathematik-Test 10 (ISB) 2024 B6 (Zylinder, Term auswählen) und 2021 A/B
(Wasser im Messbecher); Bayerischer Mathematik-Test 8 (ISB) 2008 (Restkörper), 2009 A1 (Würfel diagonal geteilt), 2023 A (Volumen in Litern, Höhe gesucht),
2025 A (Maßstab und Volumen); Abschlussprüfung Realschule Bayern 2020 Mathematik I B1 (Prisma mit Trapez-Grundfläche); niveaubestimmende Aufgabe
Sachsen-Anhalt (Trapezprisma, volumengleicher Quader); IQB-Lernaufgabe „Hamsterhaltung“ (Zylinder, Änderung einer Größe).

    python3 -I inhalte/generatoren/messen.prisma_zylinder.py
    python3 -I tools/inhalt_pruefen.py inhalte/themen/messen.prisma_zylinder.json
"""
import math
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
from _luecken_neu import (PI, A, K, P, Z, aufgaben, d, fig, gr, netz_rechtecke, rechne, runde, schraeg_prisma,  # noqa: E402
                          schreiben, toleranz_pi, wahl, z)

ZIEL = HIER.parent / 'themen' / 'messen.prisma_zylinder.json'
META = {'thema_schluessel': 'messen.prisma_zylinder', 'thema_id': 101, 'block_id': 86, 'klasse': {'gym_by': 8, 'rs_by': 9}}
SEED = 7101
PIF = Fr(PI)


def ganz(b):
    out = dict(b)
    for k in ('flaeche', 'rechter_winkel', 'kreise', 'winkel'):
        out.setdefault(k, [])
    return out


def PZ(text, ausdruck, stellen, w, h, einheit, art=None, grafik=None):
    """Aufgabe mit π: Lösung = round(ausdruck, stellen), Toleranz für π ≈ 3,14."""
    c = f'round({ausdruck}, {stellen})'
    wert = rechne(c)
    return Z(text, wert, c, w, h, einheit, art=art, grafik=grafik, toleranz=toleranz_pi(wert, stellen))


def ca(x, stellen=1):
    return z(runde(x, stellen))


def rund_text(stellen, e):
    return {0: f'Runde auf ganze {e}.', 1: f'Runde auf eine Stelle nach dem Komma.', 2: f'Runde auf zwei Stellen nach dem Komma.'}[stellen]


# ---------- Zeichnungen ----------
def prisma_bild(front, tiefe, e='cm', labels=None, hoehe=None, hinten=None, tiefe_text=True):
    """Schrägbild eines Prismas. hoehe = (y0, y1, Text): Maßlinie links neben der vorderen Grundfläche (dort laufen keine Tiefenkanten),
    mit gestrichelten Hilfslinien zu den Ecken. hinten = {i: Text}: Beschriftung an der hinteren Kante i (statt innen in der Fläche)."""
    f = schraeg_prisma(front, tiefe, e, labels=labels or {}, tiefe_text=tiefe_text)
    pk, lin = dict(f['punkte']), list(f['linien'])
    n = len(front)
    for i, t in (hinten or {}).items():
        for l_ in lin:
            if l_[0] == f'_h{i}' and l_[1] == f'_h{(i + 1) % n}': l_[2] = t
    if hoehe:
        y0, y1, t = hoehe
        xs = [float(p[0]) for p in front]
        breite = max(xs) - min(xs) + float(tiefe) * 0.5 / math.sqrt(2)
        xm = min(xs) - 0.12 * breite
        pk['_F'], pk['_H'] = (xm, float(y0)), (xm, float(y1))
        lin.append(['_F', '_H', t, 'gestrichelt'])
        for y, nm in ((y0, '_F'), (y1, '_H')):
            ecke = min((i for i in range(n) if front[i][1] == y), key=lambda i: front[i][0])
            if float(front[ecke][0]) - xm > 1e-6: lin.append([nm, f'_v{ecke}', '', 'gestrichelt'])
    return {**f, 'punkte': {k: [round(float(v[0]), 3), round(float(v[1]), 3)] for k, v in pk.items()}, 'linien': lin}


def dreiecksprisma(g, hg, l, e='cm', mitte=None, lg=True, lh=True):
    xc = Fr(g, 2) if mitte is None else mitte
    return prisma_bild([(0, 0), (g, 0), (xc, hg)], l, e, labels={0: gr(g, e)} if lg else {}, hoehe=(0, hg, gr(hg, e)) if lh else None)


def trapezprisma(a, c, h, l, e='cm', lab=True):
    xd = Fr(a - c, 2)
    return prisma_bild([(0, 0), (a, 0), (xd + c, h), (xd, h)], l, e, labels={0: gr(a, e)} if lab else {}, hinten={2: gr(c, e)} if lab else None,
                       hoehe=(0, h, gr(h, e)) if lab else None)


def vieleck_im_kreis(n, r=3.0, ring=None):
    pk = {'_M': (0, 0)}
    for i in range(n):
        w = math.radians(90 + 360 * i / n)
        pk[f'_e{i}'] = (r * math.cos(w), r * math.sin(w))
    lin = [[f'_e{i}', f'_e{(i + 1) % n}'] for i in range(n)]
    f = fig(pk, lin, [f'_e{i}' for i in range(n)], kreise=[{'m': '_M', 'r': r}])
    return f


def ring_bild(R_, r_, e='cm'):
    w = math.sqrt(0.5)
    pk = {'_M': (0, 0), '_A': (float(R_) * w, float(R_) * w), '_B': (0, -r_), '_ht': (0, float(R_) + 0.5)}
    return fig(pk, [['_M', '_A'], ['_ht', '_ht', 'R = ' + gr(R_, e), 'gestrichelt'], ['_M', '_B', 'r = ' + gr(r_, e)]],
               kreise=[{'m': '_M', 'r': float(R_)}, {'m': '_M', 'r': float(r_)}])


def zylinder_netz(r, h, e='cm', kurz=False):
    """Netz eines Zylinders: Mantel-Rechteck u × h, ein Kreis oben links, einer unten rechts. kurz: nur „u“ und „r“ statt Maßen."""
    u = 2 * math.pi * float(r)
    r_ = float(r)
    pk = {'_a': (0, 0), '_b': (u, 0), '_c': (u, h), '_d': (0, h), '_M': (r_, float(h) + r_), '_N': (u - r_, -r_), '_R': (2 * r_, float(h) + r_),
          '_ht': (r_, float(h) + 2 * r_ + 0.25 * r_)}
    pk['_hu'] = ((u - 2 * r_) / 2, -(0.6 if kurz else 0.35) * r_)
    lin = [['_a', '_b'], ['_b', '_c', gr(h, e)], ['_c', '_d'], ['_d', '_a'], ['_hu', '_hu', 'u' if kurz else f'u ≈ {ca(2 * PIF * r)} {e}', 'gestrichelt']]
    lin += [['_M', '_R']] if kurz else [['_M', '_R'], ['_ht', '_ht', 'r = ' + gr(r, e), 'gestrichelt']]
    return fig(pk, lin, kreise=[{'m': '_M', 'r': r_}, {'m': '_N', 'r': r_}])


def haus(b, w, dh, l, e='m', lab=True):
    front = [(0, 0), (b, 0), (b, w), (Fr(b, 2), w + dh), (0, w)]
    return prisma_bild(front, l, e, labels={0: gr(b, e), 4: gr(w, e)} if lab else {}, hoehe=(w, w + dh, gr(dh, e)) if lab else None)


# ---------- Bilder der Lernkarten ----------
B_PV = prisma_bild([(0, 0), (6, 0), (0, 4)], 20, 'cm', labels={0: '6 cm', 2: '4 cm'})
B_PO = netz_rechtecke([5, 6, 5], 20, 'cm', oben=[(1, [(3, 4)], None)], unten=[(2, [(Fr(18, 5), Fr(-24, 5))], None)], lage=['o', 'u', None])
B_PU = prisma_bild([(1, 0), (5, 0), (6, 3), (0, 3)], 8, 'dm', labels={0: '4 dm'}, hinten={2: '6 dm'}, hoehe=(0, 3, '3 dm'), tiefe_text='? dm')
B_ZV = vieleck_im_kreis(6)
B_ZO = zylinder_netz(3, 8)
B_SA = haus(8, 3, 3, 10)
_SQ = {'_q0': (0, 0), '_q1': (4, 0), '_q2': (4, 4), '_q3': (0, 4), '_M': (7.5, 2), '_K': (7.5 + 16 ** .5 / math.pi ** .5, 2)}
_SQ['_ht'] = (7.5, -1.2)
B_VE = fig(_SQ, [['_q0', '_q1', '4 cm'], ['_q1', '_q2'], ['_q2', '_q3'], ['_q3', '_q0'], ['_M', '_K'], ['_ht', '_ht', 'r ≈ 2,26 cm', 'gestrichelt']], ['_q0', '_q1', '_q2', '_q3'],
           kreise=[{'m': '_M', 'r': round(16 ** .5 / math.pi ** .5, 3)}])

ETAPPEN = [
    {'lernziel': 'prisma_volumen', 'titel': 'Volumen eines Prismas',
     'einstieg': 'Eine Schokoladenschachtel hat dreieckige Enden. Wie viel passt hinein? Wie beim Quader stapelst du gleiche Schichten. Jede Schicht ist so groß wie die ⟦Grundfläche⟧.',
     'woerter': [['gerades Prisma', 'Körper mit zwei gleichen, parallelen Grundflächen; die Seitenflächen stehen senkrecht darauf'],
                 ['Grundfläche G', 'eine der beiden gleichen Endflächen'], ['Körperhöhe h', 'Abstand der beiden Grundflächen']],
     'bild': B_PV,
     'schritte': [{'text': 'Die Schachtel ist ein gerades Prisma. Ihre Grundfläche G ist ein Dreieck.'},
                  {'text': 'G = 6 cm · 4 cm : 2 = 12 cm².'},
                  {'text': 'Die Körperhöhe h ist 20 cm: 20 Schichten zu je 12 cm³.'},
                  {'text': 'V = G · h = 12 cm² · 20 cm = ⟦240 cm³⟧.'},
                  {'text': 'Das klappt für jede Form der Grundfläche, nicht nur für Rechtecke.'}],
     'fehler': 'Nicht alle Kanten malnehmen: 6 · 4 · 20 = 480 cm³ ist der Quader um die Schachtel. Die Schachtel ist halb so groß.',
     'regel': 'Prisma: ⟦V = G · h⟧. Das gilt für jede Form der Grundfläche.'},
    {'lernziel': 'prisma_oberflaeche', 'titel': 'Oberfläche eines Prismas',
     'einstieg': 'Für die Schachtel braucht die Fabrik Karton. Klappt man sie auf, sieht man zwei Dreiecke und einen langen Streifen. Der Streifen heißt ⟦Mantel⟧.',
     'woerter': [['Mantel M', 'alle Seitenflächen zusammen; aufgeklappt ein Rechteck'], ['Umfang u', 'alle Seiten der Grundfläche zusammengezählt']],
     'bild': B_PO,
     'schritte': [{'text': 'Der Mantel M ist ein Rechteck: u lang und h hoch.'},
                  {'text': 'Umfang u = 5 cm + 6 cm + 5 cm = 16 cm.'},
                  {'text': 'Mantel: M = 16 cm · 20 cm = 320 cm².'},
                  {'text': 'Dazu kommen zwei Grundflächen: 2 · 12 cm² = 24 cm².'},
                  {'text': 'O = 24 cm² + 320 cm² = ⟦344 cm²⟧.'}],
     'fehler': 'Der Mantel ist nicht 6 cm · 20 cm. Das ist nur eine Seitenfläche; zum Mantel gehört der ganze Umfang 16 cm.',
     'fehler_bild': ganz({**B_PO, 'flaeche': ['_u1', '_u2', '_o2', '_o1']}),
     'regel': 'Prisma: ⟦O = 2 · G + M⟧. Dabei ist M = u · h, aufgeklappt ein Rechteck.'},
    {'lernziel': 'prisma_umstellen', 'titel': 'Fehlende Größen am Prisma',
     'einstieg': 'Ein Wassertrog soll 120 l fassen. Sein Querschnitt ist ein Trapez mit 15 dm². Wie lang muss er werden? Du ⟦stellst die Formel um⟧.',
     'woerter': [['Querschnitt', 'die Fläche, die man beim Durchschneiden sieht; hier die Grundfläche'], ['umstellen', 'die Formel so umformen, dass die gesuchte Größe allein steht']],
     'bild': B_PU,
     'schritte': [{'text': 'Querschnitt (Trapez): G = (6 + 4) · 3 : 2 = 15 dm².'},
                  {'text': 'Aus V = G · h wird durch Umstellen h = V : G.'},
                  {'text': '120 l = 120 dm³. h = 120 dm³ : 15 dm² = ⟦8 dm⟧.'},
                  {'text': 'Der Trog wird also 8 dm = 80 cm lang.'}],
     'fehler': 'Nicht V · G rechnen. 120 · 15 = 1 800 wäre viel zu groß; gesucht ist, wie oft G in V passt.',
     'regel': 'Umstellen: ⟦h = V : G⟧ und G = V : h. Rechne vorher in passende Einheiten um.'},
    {'lernziel': 'zylinder_volumen', 'titel': 'Zylinder: Volumen begründen',
     'einstieg': 'In Buenos Aires hast du das Volumen einer Dose mit V = π · r² · h berechnet. Warum gilt das? Ein Zylinder ist wie ein Prisma mit ⟦sehr vielen Ecken⟧.',
     'woerter': [['Grenzfall', 'was herauskommt, wenn man immer mehr Ecken nimmt'], ['Hohlzylinder', 'Rohr: großer Zylinder ohne den inneren Zylinder']],
     'bild': B_ZV,
     'schritte': [{'text': 'Ein Prisma mit sechseckiger Grundfläche hat V = G · h.'},
                  {'text': 'Mit 12 oder 24 Ecken ist die Grundfläche fast schon ein Kreis.', 'bild': ganz(vieleck_im_kreis(24))},
                  {'text': 'Im Grenzfall ist die Grundfläche ein Kreis: G = π · r².'},
                  {'text': 'Also gilt ⟦V = G · h = π · r² · h⟧.'},
                  {'text': 'Ein Hohlzylinder ist ein Rohr: großer Zylinder minus innerer Zylinder.', 'bild': ganz(ring_bild(3, 2))}],
     'fehler': 'Beim Rohr nicht (R − r)² rechnen. Abziehen musst du die ganze innere Kreisfläche: π · R² − π · r².',
     'regel': 'Zylinder: ⟦V = π · r² · h⟧, also G · h. Rohr: (π · R² − π · r²) · h.'},
    {'lernziel': 'zylinder_oberflaeche', 'titel': 'Zylinder: Oberfläche über das Netz',
     'einstieg': 'Wie viel Blech braucht eine Dose? Schneidest du sie auf und rollst sie ab, liegen zwei Kreise und ein Rechteck vor dir. Das ist ihr ⟦Netz⟧.',
     'woerter': [['abrollen', 'die gebogene Seite flach auslegen; es entsteht ein Rechteck'], ['Etikett', 'Papier, das nur den Mantel bedeckt']],
     'bild': B_ZO,
     'schritte': [{'text': 'Beim Abrollen wird der Mantel ein Rechteck, u = 2 · π · r breit.'},
                  {'text': 'Mantel: M = 2 · π · 3 cm · 8 cm ≈ 150,8 cm².'},
                  {'text': 'Zwei Kreise: 2 · π · 3² ≈ 56,5 cm².'},
                  {'text': 'O = 56,5 cm² + 150,8 cm² ≈ ⟦207,3 cm²⟧.'},
                  {'text': 'Ein Etikett bedeckt nur den Mantel, also 150,8 cm².'}],
     'fehler': 'Der Mantel ist nicht so breit wie der Durchmesser. Er ist so breit wie der Umfang, also π-mal so breit.',
     'regel': 'Zylinder: ⟦O = 2 · G + M⟧, wie beim Prisma. G = π · r², M = 2 · π · r · h.'},
    {'lernziel': 'sach', 'titel': 'Prismen und Zylinder im Alltag',
     'einstieg': 'Ein Haus besteht aus einem Quader mit einem Satteldach. Für die Heizung zählt der ganze Innenraum. Du zerlegst den Körper und triffst ⟦sinnvolle Annahmen⟧.',
     'woerter': [['umbauter Raum', 'das ganze Volumen eines Gebäudes'], ['Annahme', 'ein vernünftig geschätzter Wert, wenn eine Angabe fehlt']],
     'bild': B_SA,
     'schritte': [{'text': 'Das Haus ist ein Prisma mit fünfeckiger Grundfläche und 10 m lang.'},
                  {'text': 'G: Rechteck 24 m² plus Dreieck 12 m², zusammen 36 m².'},
                  {'text': 'Umbauter Raum: V = 36 m² · 10 m = ⟦360 m³⟧.'},
                  {'text': 'Die Wände sind dick, innen ist weniger Platz. Das bleibt eine Annahme.'}],
     'fehler': 'Das Haus nicht als Quader 8 m · 6 m · 10 m rechnen. Das Dach ist ein dreiseitiges Prisma, kein Quader.',
     'regel': 'Zerlege in Prismen und Zylinder. ⟦Triff Annahmen⟧, wenn Maße fehlen, und nenne sie.'},
    {'lernziel': 'verstehen', 'titel': 'Begründen und beurteilen',
     'einstieg': 'Zwei Vasen sind gleich hoch. Eine hat einen quadratischen Boden, die andere einen runden mit gleich großer Fläche. Sind sie ⟦volumengleich⟧?',
     'woerter': [['volumengleich', 'gleich großes Volumen, auch bei verschiedener Form'], ['Verhältnis', 'wie oft eine Größe in eine andere passt']],
     'bild': B_VE,
     'schritte': [{'text': 'Beide Vasen haben G = 16 cm² und die Höhe h = 30 cm.'},
                  {'text': 'V = G · h: In beide passen ⟦480 cm³⟧. Sie sind volumengleich.'},
                  {'text': 'Doppelter Radius beim Zylinder: G wird 2 · 2 = 4-mal so groß.'},
                  {'text': 'Das Verhältnis der Volumen ist dann auch 4 : 1.'}],
     'fehler': 'Doppelter Radius heißt nicht doppeltes Volumen. Der Radius steht im Quadrat: 4-mal so viel.',
     'regel': 'Gleiche Grundfläche, gleiche Höhe: ⟦gleiches Volumen⟧. Die Form der Grundfläche ist egal.'},
]


# ---------- Aufgaben-Generatoren ----------
TRI = [(6, 4, 5), (8, 3, 5), (16, 6, 10), (12, 8, 10), (24, 5, 13), (10, 12, 13), (18, 12, 15)]   # gleichschenklig: Grundseite, Höhe, Schenkel
TRAP = [(10, 4, 4, 5), (16, 4, 8, 10), (14, 2, 8, 10), (11, 5, 4, 5), (12, 6, 4, 5), (20, 8, 8, 10)]   # a, c, h, Schenkel
RECHT = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)]


def gen_prisma_volumen(R, st):
    if st == 1:
        art = wahl(R, 'pv1', ['dreieck', 'trapez'])
        if art == 'dreieck':
            g, hg = R.choice([(6, 4), (8, 3), (10, 6), (12, 5), (4, 3), (9, 4)])
            l = R.randint(5, 20)
            G = Fr(g * hg, 2)
            return Z(f'Ein gerades Prisma hat als Grundfläche ein Dreieck mit g = {g} cm und Höhe {hg} cm. Die Körperhöhe ist {l} cm. Berechne das Volumen.', G * l,
                     f'{g} * {hg} / 2 * {l}', f'G = {g} · {hg} : 2 = {z(G)} cm². V = G · h = {z(G)} · {l} = {z(G * l)} cm³.', 'Erst die Grundfläche, dann mal die Körperhöhe.', 'cm³',
                     grafik=dreiecksprisma(g, hg, l))
        a, c, h, s = R.choice(TRAP)
        l = R.choice([10, 15, 20, 25, 30])
        G = Fr((a + c) * h, 2)
        return Z(f'Ein gerades Prisma hat als Grundfläche ein Trapez (a = {a} cm, c = {c} cm, h = {h} cm). Es ist {l} cm lang. Wie groß ist sein Volumen?', G * l,
                 f'({a} + {c}) * {h} / 2 * {l}', f'G = ({a} + {c}) · {h} : 2 = {z(G)} cm². V = {z(G)} · {l} = {z(G * l)} cm³.', 'Trapezfläche mal Körperhöhe.', 'cm³',
                 grafik=trapezprisma(a, c, h, l))
    if st == 2:
        art = wahl(R, 'pv2', ['g_gegeben', 'liter', 'l_form', 'dez', 'parallelogramm'])
        if art == 'g_gegeben':
            G, h = R.randint(12, 80), R.randint(3, 15)
            return Z(f'Ein Prisma hat eine Grundfläche von {G} cm² und eine Körperhöhe von {h} cm. Wie groß ist sein Volumen?', G * h, f'{G} * {h}',
                     f'V = G · h = {G} · {h} = {G * h} cm³. Die Form der Grundfläche spielt keine Rolle.', 'V = G · h.', 'cm³')
        if art == 'liter':
            a, c, h = R.choice([(20, 12, 15), (24, 16, 18), (18, 12, 15), (22, 14, 16), (20, 14, 18)])
            l = R.choice([50, 80, 100, 120])
            V = Fr((a + c) * h, 2) * l
            return Z(f'Ein Blumenkasten hat einen trapezförmigen Querschnitt (oben {a} cm, unten {c} cm breit, {h} cm hoch) und ist {l} cm lang. Wie viele Liter Erde passen hinein?',
                     V / 1000, f'({a} + {c}) * {h} / 2 * {l} / 1000', f'G = ({a} + {c}) · {h} : 2 = {z(Fr((a + c) * h, 2))} cm². V = {z(Fr((a + c) * h, 2))} · {l} = {z(V)} cm³ = {z(V / 1000)} l.',
                     '1 l = 1 000 cm³.', 'l')
        if art == 'l_form':
            a, b, c_, e_, t = R.randint(6, 10), R.randint(5, 9), R.randint(2, 4), R.randint(2, 4), R.randint(5, 12)
            if c_ >= a or e_ >= b: return gen_prisma_volumen(R, st)
            G = a * e_ + c_ * (b - e_)
            return Z(f'Ein Winkelprofil aus Beton hat eine L-förmige Grundfläche: unten {a} dm breit und {e_} dm hoch, links {b} dm hoch und {c_} dm breit. Es ist {t} dm lang. Volumen?',
                     G * t, f'({a} * {e_} + {c_} * ({b} - {e_})) * {t}', f'G = {a} · {e_} + {c_} · ({b} − {e_}) = {G} dm². V = {G} · {t} = {G * t} dm³.',
                     'Die L-Form ist die Grundfläche. Zerlege sie in zwei Rechtecke.', 'dm³',
                     grafik=prisma_bild([(0, 0), (a, 0), (a, e_), (c_, e_), (c_, b), (0, b)], t, 'dm', labels={0: gr(a, 'dm'), 5: gr(b, 'dm')}))
        if art == 'dez':
            g, hg = Fr(R.choice([25, 35, 45, 15]), 10), R.choice([2, 4, 6])
            l = R.choice([8, 12, 20])
            G = g * hg / 2
            return Z(f'Ein Dreiecksprisma: Grundfläche mit g = {gr(g, "m")} und Dreieckshöhe {hg} m, Körperhöhe {l} m. Wie groß ist das Volumen?', G * l, f'{d(g)} * {hg} / 2 * {l}',
                     f'G = {z(g)} · {hg} : 2 = {gr(G, "m²")}. V = {z(G)} · {l} = {gr(G * l, "m³")}.', 'Erst G, dann mal h.', 'm³')
        g, hg, l = R.randint(4, 10), R.randint(3, 8), R.randint(5, 15)
        return Z(f'Ein gerades Prisma hat ein Parallelogramm als Grundfläche (g = {g} cm, Höhe {hg} cm) und ist {l} cm hoch. Berechne das Volumen.', g * hg * l, f'{g} * {hg} * {l}',
                 f'G = {g} · {hg} = {g * hg} cm². V = {g * hg} · {l} = {g * hg * l} cm³.', 'Parallelogramm: g · h.', 'cm³')
    art = wahl(R, 'pv3', ['schnitt', 'fehler', 'vergleich', 'sechseck', 'graben'])
    if art == 'schnitt':
        a, b, c = R.choice([(6, 4, 10), (8, 5, 12), (10, 6, 15), (12, 4, 9)])
        return Z(f'Ein Quader ({a} cm · {b} cm · {c} cm) wird längs entlang einer Diagonale der Vorderfläche ({a} cm · {b} cm) durchgesägt. Wie groß ist das Volumen eines Teils?',
                 Fr(a * b * c, 2), f'{a} * {b} / 2 * {c}', f'Jedes Teil ist ein Dreiecksprisma mit G = {a} · {b} : 2 = {z(Fr(a * b, 2))} cm² und h = {c} cm: V = {z(Fr(a * b * c, 2))} cm³ – die Hälfte des Quaders.',
                 'Welche Grundfläche hat jedes Teil?', 'cm³')
    if art == 'fehler':
        g, hg, l = R.choice([(6, 4, 10), (8, 5, 12), (10, 3, 9)])
        return A(R, f'Ein Dreiecksprisma (g = {g} cm, Dreieckshöhe {hg} cm, Körperhöhe {l} cm). Max rechnet V = {g} · {hg} · {l} = {g * hg * l} cm³. Was stimmt?',
                 f'Falsch: G ist ein Dreieck, also V = {g} · {hg} : 2 · {l} = {z(Fr(g * hg * l, 2))} cm³.',
                 ['Richtig, beim Prisma multipliziert man drei Längen.', f'Falsch: V = ({g} + {hg}) · {l} = {(g + hg) * l} cm³.', f'Falsch: V = {g} · {hg} · {l} : 3 = {z(Fr(g * hg * l, 3))} cm³.'],
                 'Max hat den Quader um das Prisma berechnet. Die Dreiecksfläche ist nur halb so groß wie g · h.', 'Wie groß ist die Grundfläche?')
    if art == 'vergleich':
        g, hg, l = R.choice([(6, 4, 10), (8, 6, 12), (10, 4, 9)])
        return A(R, f'Prisma A: Dreieck (g = {g} cm, Höhe {hg} cm) als Grundfläche, Körperhöhe {2 * l} cm. Prisma B: Rechteck {g} cm · {hg} cm, Körperhöhe {l} cm. Was stimmt?',
                 'Beide haben das gleiche Volumen.', ['A hat das doppelte Volumen.', 'B hat das doppelte Volumen.', 'B hat das vierfache Volumen.'],
                 f'A: {z(Fr(g * hg, 2))} · {2 * l} = {g * hg * l} cm³. B: {g * hg} · {l} = {g * hg * l} cm³. Halbe Grundfläche, doppelte Höhe: gleiches Volumen.', 'Rechne beide aus.')
    if art == 'sechseck':
        t, l = R.choice([(Fr(69, 10), 18), (Fr(72, 10), 17), (Fr(65, 10), 15), (Fr(7), 12)])
        return Z(f'Die Grundfläche eines Bleistifts ist ein regelmäßiges Sechseck. Es besteht aus 6 gleichen Dreiecken mit je {gr(t, "mm²")}. Der Stift ist {l} cm lang. Volumen in mm³?',
                 6 * t * l * 10, f'6 * {d(t)} * {l} * 10', f'G = 6 · {z(t)} = {gr(6 * t, "mm²")}. h = {l} cm = {l * 10} mm. V = {z(6 * t)} · {l * 10} = {gr(6 * t * l * 10, "mm³")}.',
                 'Körperhöhe in mm umrechnen.', 'mm³')
    a, c, h = R.choice([(Fr(3), Fr(1), Fr(1)), (Fr(4), Fr(2), Fr(3, 2)), (Fr(5), Fr(2), Fr(2)), (Fr(6), Fr(3), Fr(1))])
    l = R.choice([20, 50, 100])
    V = (a + c) * h / 2 * l
    return Z(f'Ein Graben hat einen trapezförmigen Querschnitt: oben {z(a)} m, unten {z(c)} m breit, {z(h)} m tief. Er ist {l} m lang. Wie viele m³ Erde wurden ausgehoben?', V,
             f'({d(a)} + {d(c)}) * {d(h)} / 2 * {l}', f'G = ({z(a)} + {z(c)}) · {z(h)} : 2 = {gr((a + c) * h / 2, "m²")}. V = {z((a + c) * h / 2)} · {l} = {gr(V, "m³")}.',
             'Querschnitt mal Länge.', 'm³')


def gen_prisma_oberflaeche(R, st):
    if st == 1:
        art = wahl(R, 'po1', ['dreieck', 'mantel'])
        g, hg, s = R.choice(TRI)
        l = R.choice([10, 12, 15, 20])
        if art == 'dreieck':
            O = g * hg + (g + 2 * s) * l
            return Z(f'Ein Dreiecksprisma: Grundfläche gleichschenklig (g = {g} cm, Höhe {hg} cm, Schenkel {s} cm), Körperhöhe {l} cm. Berechne die Oberfläche.', O,
                     f'2 * {g} * {hg} / 2 + ({g} + 2 * {s}) * {l}', f'2 · G = 2 · {g} · {hg} : 2 = {g * hg} cm². u = {g} + {s} + {s} = {g + 2 * s} cm, M = {g + 2 * s} · {l} = {(g + 2 * s) * l} cm². O = {O} cm².',
                     'O = 2 · G + u · h.', 'cm²', grafik=dreiecksprisma(g, hg, l))
        return Z(f'Ein Prisma hat eine Grundfläche mit dem Umfang {g + 2 * s} cm und ist {l} cm hoch. Wie groß ist sein Mantel?', (g + 2 * s) * l, f'{g + 2 * s} * {l}',
                 f'M = u · h = {g + 2 * s} · {l} = {(g + 2 * s) * l} cm².', 'Der Mantel ist ein Rechteck: Umfang mal Höhe.', 'cm²')
    if st == 2:
        art = wahl(R, 'po2', ['trapez', 'recht', 'offen', 'dez', 'netz'])
        if art == 'trapez':
            a, c, h, s = R.choice(TRAP)
            l = R.choice([10, 20, 25, 30])
            O = (a + c) * h + (a + c + 2 * s) * l
            return Z(f'Ein Prisma hat ein Trapez als Grundfläche (a = {a} cm, c = {c} cm, h = {h} cm, Schenkel je {s} cm). Es ist {l} cm lang. Berechne die Oberfläche.', O,
                     f'({a} + {c}) * {h} + ({a} + {c} + 2 * {s}) * {l}', f'2 · G = 2 · ({a} + {c}) · {h} : 2 = {(a + c) * h} cm². u = {a + c + 2 * s} cm, M = {(a + c + 2 * s) * l} cm². O = {O} cm².',
                     'Zwei Trapeze plus Mantel.', 'cm²', grafik=trapezprisma(a, c, h, l))
        if art == 'recht':
            p, q, r = R.choice(RECHT)
            l = R.choice([10, 15, 20])
            O = p * q + (p + q + r) * l
            return Z(f'Ein Keil hat als Grundfläche ein rechtwinkliges Dreieck ({p} cm und {q} cm am rechten Winkel, lange Seite {r} cm). Er ist {l} cm lang. Oberfläche?', O,
                     f'2 * {p} * {q} / 2 + ({p} + {q} + {r}) * {l}', f'2 · G = {p * q} cm². M = ({p} + {q} + {r}) · {l} = {(p + q + r) * l} cm². O = {O} cm².', 'O = 2 · G + u · h.', 'cm²')
        if art == 'offen':
            a, c, h, s = R.choice(TRAP)
            l = R.choice([40, 50, 60])
            O = (a + c) * h + (c + 2 * s) * l
            return Z(f'Eine Futterrinne ist oben offen. Ihr Querschnitt ist ein Trapez (oben {a} cm, unten {c} cm, {h} cm hoch, Schrägen je {s} cm), sie ist {l} cm lang. Wie viel cm² Blech braucht sie?',
                     O, f'({a} + {c}) * {h} + ({c} + 2 * {s}) * {l}', f'Stirnseiten: 2 · ({a} + {c}) · {h} : 2 = {(a + c) * h} cm². Boden und Schrägen: ({c} + {s} + {s}) · {l} = {(c + 2 * s) * l} cm². '
                     f'Oben offen, also ohne {a} · {l}. Zusammen {O} cm².', 'Welche Seite des Mantels fehlt?', 'cm²')
        if art == 'dez':
            g, hg, s = R.choice([(Fr(3), Fr(2), Fr(5, 2)), (Fr(16, 10), Fr(6, 10), Fr(1)), (Fr(24, 10), Fr(9, 10), Fr(15, 10))])
            l = R.choice([2, 3, 4])
            O = g * hg + (g + 2 * s) * l
            return Z(f'Ein Zelt (mit Boden) ist ein Dreiecksprisma: Grundseite {gr(g, "m")}, Höhe {gr(hg, "m")}, Schrägen je {gr(s, "m")}, Länge {l} m. Wie viel m² Stoff braucht es?', O,
                     f'{d(g)} * {d(hg)} + ({d(g)} + 2 * {d(s)}) * {l}', f'2 · G = {z(g)} · {z(hg)} = {gr(g * hg, "m²")}. M = ({z(g)} + {z(s)} + {z(s)}) · {l} = {gr((g + 2 * s) * l, "m²")}. O = {gr(O, "m²")}.',
                     'Boden gehört zum Mantel.', 'm²')
        g, hg, s = R.choice(TRI)
        l = R.choice([10, 15, 20])
        return Z(f'Im Netz eines Prismas ist der Mantel ein Rechteck {g + 2 * s} cm · {l} cm. Die beiden Grundflächen sind Dreiecke mit g = {g} cm und Höhe {hg} cm. Wie groß ist das Netz?',
                 (g + 2 * s) * l + g * hg, f'{g + 2 * s} * {l} + 2 * {g} * {hg} / 2', f'Mantel: {(g + 2 * s) * l} cm². Dreiecke: 2 · {g} · {hg} : 2 = {g * hg} cm². Zusammen {(g + 2 * s) * l + g * hg} cm².',
                 'Netz = Mantel + 2 Grundflächen.', 'cm²', grafik=netz_rechtecke([s, g, s], l, 'cm', oben=[(1, [(Fr(g, 2), hg)], None)],
                                                                                   unten=[(2, [(Fr(g * g, 2 * s), -Fr(g * hg, s))], None)], lage=['o', 'u', None]))
    art = wahl(R, 'po3', ['schnitt', 'farbe', 'u_aus_m', 'aussage', 'haus'])
    if art == 'schnitt':
        a, b, c = R.choice([(6, 4, 10), (8, 6, 12), (12, 5, 10), (8, 6, 20)])
        diag = {(6, 4): None, (8, 6): 10, (12, 5): 13}
        r = diag.get((a, b))
        if r is None: return gen_prisma_oberflaeche(R, st)
        return Z(f'Ein Quader ({a} cm · {b} cm · {c} cm) wird entlang der Diagonale der Fläche {a} cm · {b} cm in zwei Keile gesägt. Die Diagonale ist {r} cm lang. Um wie viel cm² sind beide Teile '
                 f'zusammen größer als der Quader?', 2 * r * c, f'2 * {r} * {c}', f'Durch den Schnitt entstehen zwei neue Rechtecke {r} cm · {c} cm: 2 · {r} · {c} = {2 * r * c} cm² mehr.',
                 'Welche Flächen kommen beim Sägen dazu?', 'cm²')
    if art == 'farbe':
        g, hg, s = R.choice([(8, 3, 5), (6, 4, 5), (16, 6, 10)])
        l = R.choice([20, 30, 40])
        O = g * hg + (g + 2 * s) * l
        k = R.choice([Fr(1, 10), Fr(2, 10)])
        return Z(f'Eine Holzschachtel (Dreiecksprisma: g = {g} cm, Höhe {hg} cm, Schenkel {s} cm, Länge {l} cm) wird außen lackiert. 1 ml Lack reicht für 10 cm². Wie viel ml braucht man?',
                 Fr(O, 10), f'({g} * {hg} + ({g} + 2 * {s}) * {l}) / 10', f'O = {g * hg} + {(g + 2 * s) * l} = {O} cm². Lack: {O} : 10 = {z(Fr(O, 10))} ml.', 'Erst die Oberfläche.', 'ml')
    if art == 'u_aus_m':
        u, l = R.randint(12, 40), R.choice([5, 8, 10, 12, 20])
        return Z(f'Der Mantel eines Prismas hat {u * l} cm² und das Prisma ist {l} cm hoch. Wie groß ist der Umfang der Grundfläche?', u, f'{u * l} / {l}',
                 f'M = u · h, also u = M : h = {u * l} : {l} = {u} cm.', 'Stelle M = u · h nach u um.', 'cm')
    if art == 'aussage':
        return A(R, 'Ein Prisma wird doppelt so hoch, die Grundfläche bleibt gleich. Was gilt für die Oberfläche?', 'Nur der Mantel verdoppelt sich, die Oberfläche wird weniger als doppelt so groß.',
                 ['Die Oberfläche verdoppelt sich genau.', 'Die Oberfläche vervierfacht sich.', 'Die Oberfläche bleibt gleich.'],
                 'O = 2 · G + u · h: 2 · G bleibt gleich, nur u · h verdoppelt sich. Darum wächst O, aber nicht auf das Doppelte.', 'Welche Teile von O hängen von h ab?')
    b, w, dh, s, l = R.choice([(8, 3, 3, 5, 10), (6, 3, 4, 5, 12), (12, 4, 8, 10, 15)])
    D = 2 * s * l
    return Z(f'Ein Haus ist {b} m breit und {l} m lang. Das Satteldach hat zwei rechteckige Dachflächen, jede {s} m breit (vom First zur Traufe) und {l} m lang. Wie viele m² Dachziegel braucht man?',
             D, f'2 * {s} * {l}', f'Zwei Rechtecke: 2 · {s} · {l} = {D} m².', 'Das Dach besteht aus zwei Rechtecken.', 'm²')


def gen_prisma_umstellen(R, st):
    if st == 1:
        G, h = R.randint(12, 60), R.randint(3, 20)
        if wahl(R, 'pu1', ['h', 'G']) == 'h':
            return Z(f'Ein Prisma hat das Volumen {G * h} cm³ und die Grundfläche {G} cm². Wie hoch ist es?', h, f'{G * h} / {G}', f'h = V : G = {G * h} : {G} = {h} cm.', 'Stelle V = G · h nach h um.', 'cm')
        return Z(f'Ein Prisma hat das Volumen {G * h} cm³ und ist {h} cm hoch. Wie groß ist seine Grundfläche?', G, f'{G * h} / {h}', f'G = V : h = {G * h} : {h} = {G} cm².', 'Stelle nach G um.', 'cm²')
    if st == 2:
        art = wahl(R, 'pu2', ['liter', 'seite', 'trapez_l', 'dez'])
        if art == 'liter':
            G, h = R.choice([(400, 25), (250, 40), (600, 30), (500, 12), (800, 15)])
            return Z(f'Ein Gefäß in Prismaform hat eine Grundfläche von {G} cm² und fasst {z(Fr(G * h, 1000))} l. Wie hoch ist es?', h, f'{d(Fr(G * h, 1000))} * 1000 / {G}',
                     f'{z(Fr(G * h, 1000))} l = {z(G * h)} cm³. h = {z(G * h)} : {G} = {h} cm.', 'Liter in cm³ umrechnen.', 'cm')
        if art == 'seite':
            g, hg, l = R.randint(3, 12), R.randint(2, 10), R.randint(4, 15)
            if (g * hg) % 2: g += 1
            V = g * hg * l // 2
            return Z(f'Ein Dreiecksprisma hat das Volumen {V} cm³ und die Körperhöhe {l} cm. Das Dreieck ist {hg} cm hoch. Wie lang ist seine Grundseite?', g, f'2 * {V} / {l} / {hg}',
                     f'G = V : h = {V} : {l} = {z(Fr(V, l))} cm². Dreieck: g · {hg} : 2 = {z(Fr(V, l))}, also g = 2 · {z(Fr(V, l))} : {hg} = {g} cm.', 'Erst G, dann die Grundseite.', 'cm')
        if art == 'trapez_l':
            a, c, h = R.choice([(Fr(2), Fr(1), Fr(20)), (Fr(3), Fr(1), Fr(25)), (Fr(2), Fr(1), Fr(30))])
            G = (a + c) / 2 * h
            b = R.choice([4, 5, 6, 8])
            return Z(f'Ein Becken ist {z(h)} m lang, vorn {z(c)} m und hinten {z(a)} m tief; seine Seitenwand ist ein Trapez. Es fasst {z(G * b)} m³. Wie breit ist es?', b,
                     f'{d(G * b)} / (({d(a)} + {d(c)}) / 2 * {d(h)})', f'G = ({z(a)} + {z(c)}) : 2 · {z(h)} = {gr(G, "m²")}. Breite = V : G = {z(G * b)} : {z(G)} = {b} m.',
                     'Die Trapezfläche ist die Grundfläche, die Breite die Körperhöhe.', 'm')
        G, h = Fr(R.randint(12, 90), 10), R.choice([4, 5, 8])
        return Z(f'Ein Prisma hat {gr(G * h, "m³")} Volumen und ist {h} m hoch. Wie groß ist die Grundfläche?', G, f'{d(G * h)} / {h}', f'G = {z(G * h)} : {h} = {gr(G, "m²")}.', 'G = V : h.', 'm²')
    art = wahl(R, 'pu3', ['quader_gleich', 'rinne', 'kathete', 'füllung', 'gewicht'])
    if art == 'quader_gleich':
        a, c, h, l = R.choice([(10, 4, 6, 20), (8, 4, 5, 12), (12, 6, 4, 15)])
        V = Fr((a + c) * h, 2) * l
        qa, qb = R.choice([(10, 6), (8, 5), (12, 5)])
        if (V / (qa * qb)).denominator not in (1, 2, 4, 5, 10): return gen_prisma_umstellen(R, st)
        return Z(f'Ein Trapezprisma (a = {a} cm, c = {c} cm, h = {h} cm, Länge {l} cm) soll in einen volumengleichen Quader mit der Grundfläche {qa} cm · {qb} cm umgeformt werden. Wie hoch wird der Quader?',
                 V / (qa * qb), f'({a} + {c}) * {h} / 2 * {l} / ({qa} * {qb})', f'V = ({a} + {c}) · {h} : 2 · {l} = {z(V)} cm³. Höhe: {z(V)} : {qa * qb} = {z(V / (qa * qb))} cm.',
                 'Volumen bleibt gleich.', 'cm')
    if art == 'rinne':
        a, c, h = R.choice([(12, 6, 5), (10, 4, 5), (14, 8, 6)])
        G = Fr((a + c) * h, 2)
        L_ = R.choice([3, 6, 9])
        lcm = Fr(L_ * 1000, 1) / G
        if lcm.denominator not in (1, 2, 4, 5, 10, 20, 25): return gen_prisma_umstellen(R, st)
        return Z(f'Eine Regenrinne hat einen trapezförmigen Querschnitt (oben {a} cm, unten {c} cm, {h} cm tief). Wie lang muss ein Stück sein, das {L_} l Wasser fasst? Gib die Länge in cm an.',
                 lcm, f'{L_} * 1000 / (({a} + {c}) * {h} / 2)', f'G = ({a} + {c}) · {h} : 2 = {z(G)} cm². {L_} l = {z(L_ * 1000)} cm³. Länge = {z(L_ * 1000)} : {z(G)} = {z(lcm)} cm.',
                 'Länge = Volumen : Querschnitt.', 'cm')
    if art == 'kathete':
        p, q = R.choice([(4, 6), (3, 8), (5, 6), (6, 10)])
        l = R.choice([10, 20, 15])
        V = Fr(p * q, 2) * l
        return Z(f'Ein Keil (rechtwinkliges Dreieck als Grundfläche) hat {z(V)} cm³ und ist {l} cm lang. Eine Seite am rechten Winkel ist {p} cm. Wie lang ist die andere?', q,
                 f'2 * {d(V)} / {l} / {p}', f'G = {z(V)} : {l} = {z(Fr(p * q, 2))} cm². {p} · b : 2 = {z(Fr(p * q, 2))}, also b = {q} cm.', 'Erst G, dann die zweite Seite am rechten Winkel.', 'cm')
    if art == 'füllung':
        G = R.choice([1500, 2400, 1200, 3000])
        V = R.choice([30, 36, 45, 60])
        h = Fr(V * 1000, G)
        if h.denominator not in (1, 2, 4, 5): return gen_prisma_umstellen(R, st)
        return Z(f'In ein Gefäß mit einer Grundfläche von {z(G)} cm² werden {V} l Wasser gefüllt. Wie hoch steht das Wasser?', h, f'{V} * 1000 / {G}',
                 f'{V} l = {z(V * 1000)} cm³. h = {z(V * 1000)} : {z(G)} = {z(h)} cm.', 'h = V : G.', 'cm')
    l = R.choice([2, 3, 4])
    m = R.choice([Fr(24, 10), Fr(25, 10)])
    a, c, h = Fr(4, 10), Fr(2, 10), Fr(5, 10)
    G = (a + c) / 2 * h
    return Z(f'Ein Betonbalken mit Trapezquerschnitt (oben 40 cm, unten 20 cm, 50 cm hoch) wiegt {z(G * l * m)} t. 1 m³ Beton wiegt {z(m)} t. Wie lang ist der Balken?', l,
             f'{d(G * l * m)} / {d(m)} / (({d(a)} + {d(c)}) / 2 * {d(h)})', f'V = {z(G * l * m)} : {z(m)} = {gr(G * l, "m³")}. G = (0,4 + 0,2) : 2 · 0,5 = {gr(G, "m²")}. Länge = {z(G * l)} : {z(G)} = {l} m.',
             'Erst das Volumen aus dem Gewicht, dann durch G.', 'm')


def _zyl(R, gross=False):
    r = R.choice([2, 3, 4, 5, 6, Fr(5, 2), Fr(7, 2)] if not gross else [20, 25, 30, 35, 40])
    h = R.choice([4, 5, 6, 8, 10, 12, 15] if not gross else [60, 80, 90, 100])
    return Fr(r), Fr(h)


def gen_zylinder_volumen(R, st):
    if st == 1:
        art = wahl(R, 'zv1', ['durchmesser', 'liter'])
        if art == 'durchmesser':
            r, h = _zyl(R)
            return PZ(f'Ein Zylinder hat den Durchmesser {gr(2 * r, "cm")} und die Höhe {gr(h, "cm")}. Berechne das Volumen. {rund_text(1, "cm³")}', f'{PI} * {d(r)} ** 2 * {d(h)}', 1,
                      f'r = {z(2 * r)} : 2 = {z(r)} cm. V = π · {z(r)}² · {z(h)} = {z(r * r * h)}π ≈ {ca(PIF * r * r * h)} cm³.', 'Erst den Radius bestimmen.', 'cm³')
        r, h = _zyl(R, True)
        return PZ(f'Eine Regentonne ist zylinderförmig: Radius {gr(r, "cm")}, Höhe {gr(h, "cm")}. Wie viele Liter fasst sie? Runde auf ganze Liter.', f'{PI} * {d(r)} ** 2 * {d(h)} / 1000', 0,
                  f'V = π · {z(r)}² · {z(h)} ≈ {z(runde(PIF * r * r * h, 0))} cm³ ≈ {z(runde(PIF * r * r * h / 1000, 0))} l.', '1 000 cm³ = 1 l.', 'l')
    if st == 2:
        art = wahl(R, 'zv2', ['rohr', 'h_aus_v', 'halb', 'exakt', 'dm'])
        if art == 'rohr':
            R_, r_, h = R.choice([(5, 4, 100), (3, 2, 50), (6, 5, 200), (10, 8, 50), (4, 3, 80)])
            return PZ(f'Ein Rohr hat außen den Radius {R_} cm, innen {r_} cm und ist {h} cm lang. Wie viel cm³ Material hat es? {rund_text(0, "cm³")}', f'{PI} * ({R_} ** 2 - {r_} ** 2) * {h}', 0,
                      f'V = (π · {R_}² − π · {r_}²) · {h} = π · {R_ * R_ - r_ * r_} · {h} ≈ {z(runde(PIF * (R_ * R_ - r_ * r_) * h, 0))} cm³.', 'Großer Zylinder minus innerer Zylinder.', 'cm³')
        if art == 'h_aus_v':
            r = R.choice([2, 3, 4, 5, 10])
            h = R.choice([5, 6, 8, 10, 12, 20])
            return Z(f'Ein Zylinder mit Radius {r} cm hat das Volumen {r * r * h}π cm³. Wie hoch ist er?', h, f'{r * r * h} / {r} ** 2',
                     f'V = π · r² · h, also h = V : (π · r²) = {r * r * h}π : ({r * r}π) = {h} cm.', 'Das π kürzt sich weg.', 'cm')
        if art == 'halb':
            r, l = R.choice([(5, 25), (6, 30), (4, 20), (Fr(11, 2), 28)])
            r = Fr(r)
            return PZ(f'Eine Kuchenform ist ein halber Zylinder: Radius {gr(r, "cm")}, Länge {l} cm. Wie viel Teig passt hinein? {rund_text(0, "cm³")}', f'{PI} * {d(r)} ** 2 / 2 * {l}', 0,
                      f'Grundfläche: Halbkreis π · {z(r)}² : 2. V = π · {z(r * r)} : 2 · {l} ≈ {z(runde(PIF * r * r / 2 * l, 0))} cm³.', 'Halbkreis als Grundfläche.', 'cm³')
        if art == 'exakt':
            r, h = R.randint(2, 6), R.randint(2, 10)
            return A(R, f'Welcher Term gibt das Volumen eines Zylinders mit r = {r} cm und h = {h} cm exakt an?', f'{r * r * h}π cm³',
                     [f'{2 * r * h}π cm³', f'{r * h}π cm³', f'{4 * r * r * h}π cm³'], f'V = π · {r}² · {h} = {r * r * h}π cm³. ' + (f'Der Mantel 2 · π · {r} · {h} hat hier zufällig dieselbe Zahl, ist aber eine Fläche in cm². ' if r == 2 else f'{2 * r * h}π wäre der Mantel, ') + f'{4 * r * r * h}π käme mit d statt r heraus.',
                     'V = π · r² · h.')
        r, h = Fr(R.choice([5, 10, 15]), 10), Fr(R.choice([3, 4, 6]))
        return PZ(f'Ein Topf (zylinderförmig) hat innen den Durchmesser {gr(2 * r, "dm")} und ist {gr(h, "dm")} hoch. Wie viele Liter passen hinein? {rund_text(1, "l")}',
                  f'{PI} * {d(r)} ** 2 * {d(h)}', 1, f'r = {z(r)} dm. V = π · {z(r)}² · {z(h)} ≈ {ca(PIF * r * r * h)} dm³ = {ca(PIF * r * r * h)} l.', 'In dm gerechnet ist dm³ gleich Liter.', 'l')
    art = wahl(R, 'zv3', ['vergleich', 'umfuellen', 'kanister', 'verhaeltnis', 'rohr_l'])
    if art == 'vergleich':
        r, h = R.choice([(2, 9), (3, 4), (4, 9), (3, 16)])
        return A(R, f'Zylinder A hat r = {r} cm und h = {h} cm. Zylinder B hat r = {2 * r} cm und h = {Fr(h, 4) if h % 4 == 0 else z(Fr(h, 4))} cm. Was stimmt?', 'Beide haben das gleiche Volumen.',
                 ['B hat das doppelte Volumen.', 'B hat das halbe Volumen.', 'B hat das vierfache Volumen.'],
                 f'A: π · {r}² · {h} = {r * r * h}π. B: π · {2 * r}² · {z(Fr(h, 4))} = {z(4 * r * r * Fr(h, 4))}π. Doppelter Radius (·4), Viertel der Höhe (: 4): gleich.', 'Rechne beide als Vielfache von π.')
    if art == 'umfuellen':
        r1, h1, r2 = R.choice([(4, 9, 6), (6, 4, 4), (3, 16, 4), (5, 8, 10)])
        h2 = Fr(r1 * r1 * h1, r2 * r2)
        return Z(f'Wasser steht in einem Zylinder (r = {r1} cm) {h1} cm hoch. Es wird in einen Zylinder mit r = {r2} cm umgefüllt. Wie hoch steht es dort?', h2, f'{r1} ** 2 * {h1} / {r2} ** 2',
                 f'V = π · {r1}² · {h1} = {r1 * r1 * h1}π. Neue Höhe: {r1 * r1 * h1}π : ({r2 * r2}π) = {z(h2)} cm.', 'Das Volumen bleibt; π kürzt sich.', 'cm')
    if art == 'kanister':
        V = R.choice([10, 5, 20])
        r = R.choice([10, 12, 15])
        return PZ(f'Ein zylinderförmiger Behälter soll {V} l fassen. Sein Radius ist {r} cm. Wie hoch muss er mindestens sein? {rund_text(1, "cm")}', f'{V} * 1000 / ({PI} * {r} ** 2)', 1,
                  f'{V} l = {z(V * 1000)} cm³. h = V : (π · r²) = {z(V * 1000)} : (π · {r * r}) ≈ {ca(Fr(V * 1000) / (PIF * r * r))} cm.', 'Stelle V = π · r² · h nach h um.', 'cm')
    if art == 'verhaeltnis':
        k = R.choice([2, 3])
        return A(R, f'Der Radius eines Zylinders wird {"verdoppelt" if k == 2 else "verdreifacht"}, die Höhe bleibt. Wie verändert sich das Volumen?', f'{k * k}-mal so groß',
                 [f'{k}-mal so groß', f'{k * k + k}-mal so groß', f'{k ** 3}-mal so groß'], f'V = π · r² · h: Der Radius steht im Quadrat, also {k} · {k} = {k * k}.', 'r steht im Quadrat.')
    R_, r_, l = R.choice([(Fr(5, 2), Fr(2), 500), (Fr(3), Fr(5, 2), 1000), (Fr(1), Fr(8, 10), 2000)])
    return PZ(f'Ein Gartenschlauch ist {z(l)} cm lang, innen hat er den Radius {gr(r_, "cm")}. Wie viele Liter Wasser sind im vollen Schlauch? {rund_text(1, "l")}', f'{PI} * {d(r_)} ** 2 * {l} / 1000', 1,
              f'Nur der Innenraum zählt: V = π · {z(r_)}² · {l} ≈ {z(runde(PIF * r_ * r_ * l, 0))} cm³ ≈ {ca(PIF * r_ * r_ * l / 1000)} l.', 'Wasser ist nur innen im Schlauch.', 'l')


def gen_zylinder_oberflaeche(R, st):
    if st == 1:
        art = wahl(R, 'zo1', ['mantel', 'ganz'])
        r, h = _zyl(R)
        if art == 'mantel':
            return PZ(f'Ein Zylinder hat r = {gr(r, "cm")} und h = {gr(h, "cm")}. Wie groß ist sein Mantel? {rund_text(1, "cm²")}', f'2 * {PI} * {d(r)} * {d(h)}', 1,
                      f'M = 2 · π · r · h = 2 · π · {z(r)} · {z(h)} = {z(2 * r * h)}π ≈ {ca(2 * PIF * r * h)} cm².', 'Umfang mal Höhe.', 'cm²', grafik=zylinder_netz(r, h, kurz=True))
        return PZ(f'Ein Zylinder hat r = {gr(r, "cm")} und h = {gr(h, "cm")}. Berechne seine Oberfläche. {rund_text(1, "cm²")}', f'2 * {PI} * {d(r)} ** 2 + 2 * {PI} * {d(r)} * {d(h)}', 1,
                  f'O = 2 · π · {z(r)}² + 2 · π · {z(r)} · {z(h)} = {z(2 * r * r + 2 * r * h)}π ≈ {ca(PIF * (2 * r * r + 2 * r * h))} cm².', 'Zwei Kreise plus Mantel.', 'cm²')
    if st == 2:
        art = wahl(R, 'zo2', ['offen', 'etikett', 'durchmesser', 'rohr', 'litfass'])
        if art == 'offen':
            r, h = _zyl(R)
            return PZ(f'Ein Becher (Zylinder ohne Deckel) hat r = {gr(r, "cm")} und h = {gr(h, "cm")}. Wie viel cm² Material braucht er? {rund_text(1, "cm²")}', f'{PI} * {d(r)} ** 2 + 2 * {PI} * {d(r)} * {d(h)}', 1,
                      f'Nur ein Kreis: π · {z(r)}² + Mantel 2 · π · {z(r)} · {z(h)} = {z(r * r + 2 * r * h)}π ≈ {ca(PIF * (r * r + 2 * r * h))} cm².', 'Ohne Deckel fällt ein Kreis weg.', 'cm²')
        if art == 'etikett':
            d_, h = R.choice([(Fr(66, 10), 8), (Fr(74, 10), 10), (Fr(10), 6), (Fr(8), 9)])
            return PZ(f'Eine Dose hat den Durchmesser {gr(d_, "cm")}. Ihr Etikett ist {h} cm hoch und geht genau einmal herum. Wie groß ist das Etikett? {rund_text(1, "cm²")}',
                      f'{PI} * {d(d_)} * {h}', 1, f'Breite = Umfang = π · d = π · {z(d_)} cm. Etikett: π · {z(d_)} · {h} ≈ {ca(PIF * d_ * h)} cm².', 'Das Etikett ist der Mantel.', 'cm²')
        if art == 'durchmesser':
            r, h = _zyl(R)
            return PZ(f'Ein Zylinder hat den Durchmesser {gr(2 * r, "cm")} und die Höhe {gr(h, "cm")}. Wie groß ist seine Oberfläche? {rund_text(0, "cm²")}',
                      f'2 * {PI} * {d(r)} ** 2 + 2 * {PI} * {d(r)} * {d(h)}', 0, f'r = {z(r)} cm. O = 2 · π · {z(r)}² + 2 · π · {z(r)} · {z(h)} ≈ {z(runde(PIF * (2 * r * r + 2 * r * h), 0))} cm².',
                      'Erst den Radius.', 'cm²')
        if art == 'rohr':
            r, l = R.choice([(Fr(5), 200), (Fr(4), 150), (Fr(10), 100), (Fr(6), 250)])
            return PZ(f'Ein Rohr (r = {gr(r, "cm")}, Länge {l} cm) soll außen gestrichen werden. Wie viel cm² sind das? Die Enden sind offen. {rund_text(0, "cm²")}', f'2 * {PI} * {d(r)} * {l}', 0,
                      f'Nur der Mantel: 2 · π · {z(r)} · {l} ≈ {z(runde(2 * PIF * r * l, 0))} cm².', 'Welche Flächen hat ein offenes Rohr?', 'cm²')
        r, h = R.choice([(Fr(6, 10), 3), (Fr(7, 10), Fr(35, 10)), (Fr(5, 10), 3)])
        h = Fr(h)
        return PZ(f'Eine Litfaßsäule hat den Radius {gr(r, "m")} und ist {gr(h, "m")} hoch beklebbar. Wie viel m² Werbefläche hat sie? {rund_text(1, "m²")}', f'2 * {PI} * {d(r)} * {d(h)}', 1,
                  f'Werbefläche = Mantel: 2 · π · {z(r)} · {z(h)} ≈ {ca(2 * PIF * r * h)} m².', 'Nur die Seite wird beklebt.', 'm²')
    art = wahl(R, 'zo3', ['radius_aus_u', 'hoehe_aus_m', 'vergleich', 'halb', 'zwei_rollen'])
    if art == 'radius_aus_u':
        r = R.choice([2, 3, 4, 5, 10])
        h = R.choice([6, 8, 10, 12])
        return Z(f'Das Netz eines Zylinders hat einen Mantel von {2 * r}π cm Breite und {h} cm Höhe. Wie groß ist der Radius der Kreise?', r, f'{2 * r} / 2',
                 f'Die Breite des Mantels ist der Umfang: 2 · π · r = {2 * r}π, also r = {r} cm.', 'Breite des Mantels = Umfang des Kreises.', 'cm')
    if art == 'hoehe_aus_m':
        r, h = R.choice([(2, 9), (3, 7), (5, 6), (4, 10)])
        return Z(f'Ein Zylinder mit r = {r} cm hat einen Mantel von {2 * r * h}π cm². Wie hoch ist er?', h, f'{2 * r * h} / (2 * {r})', f'M = 2 · π · r · h = {2 * r}π · h = {2 * r * h}π, also h = {h} cm.',
                 'Stelle M = 2 · π · r · h nach h um.', 'cm')
    if art == 'vergleich':
        r, h = R.choice([(2, 6), (3, 4), (4, 4)])
        return A(R, f'Zylinder A: r = {r} cm, h = {2 * h} cm. Zylinder B: r = {2 * r} cm, h = {h} cm. Welcher hat den größeren Mantel?', 'Beide haben den gleichen Mantel.',
                 ['A', 'B', 'Das kann man ohne Zahlenwerte für π nicht sagen.'], f'A: 2 · π · {r} · {2 * h} = {4 * r * h}π. B: 2 · π · {2 * r} · {h} = {4 * r * h}π. Gleich groß.', 'Rechne beide als Vielfache von π.')
    if art == 'halb':
        r, l = R.choice([(Fr(1), 10), (Fr(3, 2), 8), (Fr(2), 12)])
        return PZ(f'Ein Folientunnel für Gemüse ist ein halber Zylinder (r = {gr(r, "m")}, Länge {l} m), vorn und hinten offen, der Boden ist die Erde. Wie viel m² Folie braucht man? {rund_text(1, "m²")}',
                  f'{PI} * {d(r)} * {l}', 1, f'Nur der halbe Mantel: (2 · π · {z(r)} · {l}) : 2 = {z(r * l)}π ≈ {ca(PIF * r * l)} m².', 'Welcher Teil des Zylinders ist aus Folie?', 'm²')
    return A(R, 'Ein Blatt Papier (20 cm · 30 cm) wird einmal zu einer Röhre mit 30 cm Umfang und einmal zu einer mit 20 cm Umfang gerollt (ohne Überlappung). Was gilt für die Mantelflächen?',
             'Beide Mäntel sind 600 cm² groß.', ['Die Röhre mit 30 cm Umfang hat den größeren Mantel.', 'Die Röhre mit 20 cm Umfang hat den größeren Mantel.', 'Man braucht π, um es zu entscheiden.'],
             'Der Mantel ist in beiden Fällen das ganze Blatt: 20 · 30 = 600 cm².', 'Was ist der Mantel?')


def gen_sach(R, st):
    if st == 1:
        art = wahl(R, 'sa1', ['haus', 'tonne'])
        if art == 'haus':
            b, w, dh, l = R.choice([(8, 3, 3, 10), (10, 6, 4, 12), (6, 3, 2, 8), (12, 5, 4, 15)])
            G = b * w + Fr(b * dh, 2)
            return Z(f'Ein Haus ist {b} m breit, {l} m lang, die Wände sind {w} m hoch, das Satteldach ist {dh} m hoch. Wie groß ist der umbaute Raum?', G * l,
                     f'({b} * {w} + {b} * {dh} / 2) * {l}', f'G = {b} · {w} + {b} · {dh} : 2 = {z(G)} m². V = {z(G)} · {l} = {z(G * l)} m³.', 'Fünfeck als Grundfläche.', 'm³', grafik=haus(b, w, dh, l))
        r, h = R.choice([(30, 90), (25, 80), (40, 100), (35, 90)])
        return PZ(f'Eine Regentonne ist ein Zylinder mit Durchmesser {2 * r} cm und Höhe {h} cm. Wie viele Liter fasst sie? Runde auf ganze Liter.', f'{PI} * {r} ** 2 * {h} / 1000', 0,
                  f'r = {r} cm. V = π · {r}² · {h} ≈ {z(runde(PIF * r * r * h, 0))} cm³ ≈ {z(runde(PIF * r * r * h / 1000, 0))} l.', 'Radius, Volumen, Liter.', 'l')
    if st == 2:
        art = wahl(R, 'sa2', ['pool', 'treppe', 'zelt', 'baum', 'saeule'])
        if art == 'pool':
            t1, t2, l, b = R.choice([(Fr(1), Fr(2), 20, 8), (Fr(1), Fr(3, 2), 16, 6), (Fr(1, 2), Fr(2), 25, 10), (Fr(1, 2), Fr(3, 2), 12, 6), (Fr(1), Fr(3), 25, 12)])
            V = (t1 + t2) / 2 * l * b
            return Z(f'Ein Becken ist {l} m lang und {b} m breit. Der Boden ist schräg: vorn {z(t1)} m tief, hinten {z(t2)} m. Wie viele Liter Wasser fasst es?', V * 1000,
                     f'({d(t1)} + {d(t2)}) / 2 * {l} * {b} * 1000', f'Seitenfläche (Trapez): ({z(t1)} + {z(t2)}) : 2 · {l} = {z((t1 + t2) / 2 * l)} m². V = {z((t1 + t2) / 2 * l)} · {b} = {z(V)} m³ = {z(V * 1000)} l.',
                     'Die Seitenfläche ist die Grundfläche.', 'l')
        if art == 'treppe':
            s, h, b = R.choice([(Fr(3, 10), Fr(15, 100), Fr(1)), (Fr(25, 100), Fr(2, 10), Fr(12, 10)), (Fr(3, 10), Fr(2, 10), Fr(15, 10)), (Fr(3, 10), Fr(15, 100), Fr(2))])
            n = 3
            G = s * h * (1 + 2 + 3)
            return Z(f'Eine Betontreppe hat {n} Stufen, jede {gr(s * 100, "cm")} tief und {gr(h * 100, "cm")} hoch, und ist {gr(b, "m")} breit. Wie viele m³ Beton sind es?', G * b,
                     f'{d(s)} * {d(h)} * (1 + 2 + 3) * {d(b)}', f'Seitenfläche: Stufen aus 1 + 2 + 3 = 6 Rechtecken {z(s)} m · {z(h)} m = {gr(G, "m²")}. V = {z(G)} · {z(b)} = {gr(G * b, "m³")}.',
                     'Die treppenförmige Seitenfläche ist die Grundfläche.', 'm³')
        if art == 'zelt':
            g, hg, l = R.choice([(Fr(2), Fr(15, 10), 3), (Fr(24, 10), Fr(16, 10), 2), (Fr(3), Fr(2), 4), (Fr(18, 10), Fr(12, 10), 2), (Fr(4), Fr(2), 5)])
            return Z(f'Ein Zelt ist ein Dreiecksprisma: unten {gr(g, "m")} breit, {gr(hg, "m")} hoch, {l} m lang. Wie viel m³ Luft ist darin?', g * hg / 2 * l,
                     f'{d(g)} * {d(hg)} / 2 * {l}', f'G = {z(g)} · {z(hg)} : 2 = {gr(g * hg / 2, "m²")}. V = {z(g * hg / 2)} · {l} = {gr(g * hg / 2 * l, "m³")}.', 'Dreieck mal Länge.', 'm³')
        if art == 'baum':
            dm, l = R.choice([(Fr(4, 10), 8), (Fr(5, 10), 10), (Fr(6, 10), 12), (Fr(3, 10), 6), (Fr(8, 10), 15)])
            return PZ(f'Ein Baumstamm ist etwa {gr(dm, "m")} dick und {l} m lang. Nimm an, er ist ein Zylinder. Wie viel m³ Holz hat er ungefähr? {rund_text(2, "m³")}',
                      f'{PI} * ({d(dm)} / 2) ** 2 * {l}', 2, f'Annahme Zylinder mit r = {z(dm / 2)} m: V = π · {z(dm / 2)}² · {l} ≈ {z(runde(PIF * (dm / 2) ** 2 * l, 2))} m³.',
                      'Durchmesser halbieren.', 'm³')
        r, h, n = R.choice([(Fr(2, 10), 3, 4), (Fr(3, 10), 4, 6), (Fr(25, 100), Fr(5, 2), 8), (Fr(15, 100), 3, 10), (Fr(2, 10), Fr(7, 2), 6)])
        h = Fr(h)
        return PZ(f'Für eine Halle werden {n} runde Betonsäulen gegossen (Radius {gr(r * 100, "cm")}, Höhe {gr(h, "m")}). Wie viel m³ Beton braucht man? {rund_text(2, "m³")}',
                  f'{n} * {PI} * {d(r)} ** 2 * {d(h)}', 2, f'Eine Säule: π · {z(r)}² · {z(h)} m³. {n} Säulen ≈ {z(runde(n * PIF * r * r * h, 2))} m³.', 'Radius in m umrechnen.', 'm³')
    art = wahl(R, 'sa3', ['zeit', 'kosten', 'dosen_hoehe', 'balken', 'tank'])
    if art == 'zeit':
        r, h, q = R.choice([(Fr(1), Fr(1), 10), (Fr(15, 10), Fr(1), 20), (Fr(2), Fr(12, 10), 25)])
        return PZ(f'Ein runder Pool (Radius {gr(r, "m")}) wird {gr(h, "m")} hoch mit Wasser gefüllt. Der Schlauch liefert {q} l pro Minute. Wie viele Minuten dauert es? {rund_text(0, "Minuten")}',
                  f'{PI} * {d(r)} ** 2 * {d(h)} * 1000 / {q}', 0, f'V = π · {z(r)}² · {z(h)} ≈ {ca(PIF * r * r * h, 3)} m³ ≈ {z(runde(PIF * r * r * h * 1000, 0))} l. Zeit: {z(runde(PIF * r * r * h * 1000, 0))} : {q} ≈ {z(runde(PIF * r * r * h * 1000 / q, 0))} Minuten.',
                  'Volumen in Liter, dann durch die Liter pro Minute.', 'min')
    if art == 'kosten':
        b, w, dh, l, p = R.choice([(8, 3, 3, 10, 450), (10, 3, 4, 12, 500), (6, 3, 2, 9, 480)])
        G = b * w + Fr(b * dh, 2)
        return Z(f'Für einen Neubau rechnet man mit {p} € je m³ umbauten Raum. Das Haus ist {b} m breit, {l} m lang, {w} m hoch bis zum Dach, das Satteldach ist {dh} m hoch. Was kostet es ungefähr?',
                 G * l * p, f'({b} * {w} + {b} * {dh} / 2) * {l} * {p}', f'G = {b} · {w} + {b} · {dh} : 2 = {z(G)} m². V = {z(G * l)} m³. Kosten: {z(G * l)} · {p} € = {z(G * l * p)} €.',
                 'Erst der umbaute Raum.', '€')
    if art == 'dosen_hoehe':
        V, r = R.choice([(400, 4), (330, 3), (500, 5)])
        return PZ(f'Eine Getränkedose soll {V} ml fassen und innen den Radius {r} cm haben. Wie hoch muss sie innen mindestens sein? {rund_text(1, "cm")}', f'{V} / ({PI} * {r} ** 2)', 1,
                  f'{V} ml = {V} cm³. h = V : (π · r²) = {V} : (π · {r * r}) ≈ {ca(Fr(V) / (PIF * r * r))} cm.', 'h = V : (π · r²).', 'cm')
    if art == 'balken':
        a, b, l, r = R.choice([(20, 20, 100, 5), (30, 20, 120, 6), (40, 30, 200, 10)])
        return PZ(f'In einen Holzbalken ({a} cm · {b} cm · {l} cm) wird der Länge nach eine halbrunde Rinne (Radius {r} cm) gefräst. Wie viel cm³ Holz bleiben? {rund_text(0, "cm³")}',
                  f'{a} * {b} * {l} - {PI} * {r} ** 2 / 2 * {l}', 0, f'Balken: {z(a * b * l)} cm³. Rinne: π · {r}² : 2 · {l} ≈ {z(runde(PIF * r * r / 2 * l, 0))} cm³. Rest ≈ {z(runde(a * b * l - PIF * r * r / 2 * l, 0))} cm³.',
                  'Quader minus halber Zylinder.', 'cm³')
    r, l, f = R.choice([(Fr(1), 4, Fr(3, 4)), (Fr(8, 10), 3, Fr(1, 2)), (Fr(12, 10), 5, Fr(1, 4))])
    return PZ(f'Ein liegender Öltank ist ein Zylinder (Radius {gr(r, "m")}, Länge {l} m). Er ist {"zu drei Vierteln" if f == Fr(3, 4) else ("zur Hälfte" if f == Fr(1, 2) else "zu einem Viertel")} '
              f'voll. Wie viele Liter sind darin? Runde auf ganze Liter.', f'{PI} * {d(r)} ** 2 * {l} * {d(f)} * 1000', 0,
              f'Ganzer Tank: π · {z(r)}² · {l} ≈ {ca(PIF * r * r * l, 3)} m³. Davon {"drei Viertel" if f == Fr(3, 4) else ("die Hälfte" if f == Fr(1, 2) else "ein Viertel")}: ≈ {z(runde(PIF * r * r * l * f * 1000, 0))} l.', 'Erst der ganze Tank, dann der Anteil.', 'l')


def gen_verstehen(R, st):
    if st == 1:
        art = wahl(R, 've1', ['h_doppelt', 'formel', 'g_doppelt'])
        if art == 'g_doppelt':
            k = R.choice([2, 3])
            return A(R, f'Die Grundfläche eines Prismas wird {"doppelt" if k == 2 else "dreimal"} so groß, die Höhe bleibt gleich. Wie ändert sich das Volumen?', f'{k}-mal so groß',
                     [f'{k * k}-mal so groß', 'gleich', 'halb so groß'], f'V = G · h: G wird {k}-mal so groß, also auch V.', 'Was steht in der Formel V = G · h?')
        if art == 'h_doppelt':
            k = R.choice([2, 3])
            return A(R, f'Ein Prisma wird {"doppelt" if k == 2 else "dreimal"} so hoch, die Grundfläche bleibt gleich. Wie ändert sich das Volumen?', f'{k}-mal so groß',
                     [f'{k * k}-mal so groß', 'gleich', f'{k ** 3}-mal so groß'], f'V = G · h: h wird {k}-mal so groß, also auch V.', 'Was steht in der Formel V = G · h?')
        return A(R, 'Welche Formel gilt für das Volumen jedes geraden Prismas?', 'V = G · h', ['V = a · b · c', 'V = u · h', 'V = G · h : 2'],
                 'Grundfläche mal Körperhöhe – unabhängig von der Form von G. a · b · c gilt nur für Quader, u · h ist der Mantel.', 'Schichten aus Grundflächen.')
    if st == 2:
        art = wahl(R, 've2', ['radius', 'fehler_mantel', 'gleich', 'halbieren'])
        if art == 'radius':
            V = R.choice([50, 80, 120, 200])
            k, txt = R.choice([(4, 'doppelt so groß'), (Fr(1, 4), 'halb so groß'), (9, 'dreimal so groß')])
            return Z(f'Ein Zylinder hat {V} cm³. Sein Radius wird {txt}, die Höhe bleibt. Wie groß ist das neue Volumen?', V * k, f'{V} * {d(k)}',
                     f'r steht im Quadrat: Faktor {"2 · 2 = 4" if k == 4 else ("0,5 · 0,5 = 0,25" if k == Fr(1, 4) else "3 · 3 = 9")}. Neues Volumen: {z(V * k)} cm³.', 'r² – der Faktor wird quadriert.', 'cm³')
        if art == 'fehler_mantel':
            d_, h = R.choice([(6, 10), (8, 5), (10, 12)])
            return A(R, f'Nina rechnet den Mantel eines Zylinders (d = {d_} cm, h = {h} cm) so: M = 2 · π · {d_} · {h}. Was stimmt?', f'Falsch: Mit d heißt es M = π · {d_} · {h}.',
                     ['Richtig.', f'Falsch: M = π · {d_}² · {h}.', f'Falsch: M = 2 · {d_} · {h}.'], f'2 · π · r = π · d. Nina hat d statt r eingesetzt und damit den Mantel verdoppelt.', 'Wie hängen r und d zusammen?')
        if art == 'gleich':
            G, h = R.choice([(24, 10), (30, 12), (50, 8)])
            return A(R, f'Ein Prisma mit dreieckiger Grundfläche und ein Zylinder haben beide G = {G} cm² und h = {h} cm. Was stimmt?', f'Beide haben {G * h} cm³.',
                     ['Der Zylinder hat mehr Volumen, weil er rund ist.', 'Das Prisma hat mehr Volumen, weil es Ecken hat.', 'Man braucht den Radius, um es zu entscheiden.'],
                     f'V = G · h gilt für beide: {G} · {h} = {G * h} cm³.', 'V = G · h für jede Grundfläche.')
        V = R.choice([60, 90, 150])
        return Z(f'Ein Prisma hat {V} cm³. Die Grundfläche wird verdoppelt und die Höhe halbiert. Wie groß ist das neue Volumen?', V, f'{V} * 2 / 2',
                 f'V = G · h: · 2 und : 2 heben sich auf. Es bleibt {V} cm³.', 'Was passiert mit G · h?', 'cm³')
    art = wahl(R, 've3', ['prozent', 'modell', 'aussagen', 'rollen'])
    if art == 'prozent':
        p = R.choice([10, 20, 50])
        f = (1 + Fr(p, 100)) ** 2
        return Z(f'Der Radius eines Zylinders wird um {p} % größer, die Höhe bleibt. Um wie viel Prozent wächst das Volumen?', (f - 1) * 100, f'((1 + {p} / 100) ** 2 - 1) * 100',
                 f'Neuer Radius: {z(1 + Fr(p, 100))} · r. Volumen-Faktor: {z(1 + Fr(p, 100))}² = {z(f)}. Das Volumen wächst um {z((f - 1) * 100)} %.', 'r steht im Quadrat.', '%')
    if art == 'modell':
        k = R.choice([2, 3])
        wort = {2: 'verdoppelt', 3: 'verdreifacht'}[k]
        return A(R, f'Alle Längen eines Prismas werden {wort}: die Seiten der Grundfläche, ihre Höhe und die Körperhöhe. Wie ändert sich das Volumen?', f'{k ** 3}-mal so groß',
                 [f'{k}-mal so groß', f'{k * k}-mal so groß', f'{k * k + k}-mal so groß'], f'G wird {k} · {k} = {k * k}-mal so groß, h wird {k}-mal so groß: V wird {k * k} · {k} = {k ** 3}-mal so groß.',
                 'Wie ändert sich zuerst die Grundfläche?')
    if art == 'aussagen':
        return A(R, 'Welche Aussage ist richtig?', 'Verdoppelt man Radius und Höhe eines Zylinders, wird das Volumen 8-mal so groß.',
                 ['Verdoppelt man den Radius, verdoppelt sich das Volumen.', 'Ein Zylinder hat immer mehr Volumen als ein Prisma mit gleicher Höhe.', 'Die Oberfläche eines Zylinders ist nur sein Mantel.'],
                 'V = π · r² · h: 2 · 2 · 2 = 8. Doppelter Radius allein gibt 4-faches Volumen; Zylinder und Prisma mit gleichem G und h sind gleich groß; zur Oberfläche gehören auch zwei Kreise.',
                 'Prüfe jede Aussage mit der Formel.')
    return A(R, 'Ein Blatt (20 cm · 30 cm) wird einmal zu einer Röhre mit 30 cm Umfang (20 cm hoch) und einmal mit 20 cm Umfang (30 cm hoch) gerollt. Welche Röhre fasst mehr?',
             'Die mit 30 cm Umfang.', ['Die mit 20 cm Umfang.', 'Beide fassen gleich viel.', 'Das hängt vom Papier ab.'],
             'r = u : (2π). V = π · r² · h = u² · h : (4π): 30² · 20 = 18 000 gegen 20² · 30 = 12 000 (jeweils : 4π). Die weitere Röhre fasst mehr.', 'Der Umfang geht ins Quadrat ein.')


GEN = {'prisma_volumen': gen_prisma_volumen, 'prisma_oberflaeche': gen_prisma_oberflaeche, 'prisma_umstellen': gen_prisma_umstellen, 'zylinder_volumen': gen_zylinder_volumen,
       'zylinder_oberflaeche': gen_zylinder_oberflaeche, 'sach': gen_sach, 'verstehen': gen_verstehen}


def fest(R):
    F = {}
    F['prisma_volumen'] = [
        Z('Ein Holzwürfel mit 8 cm Kante wird entlang der Diagonalen zweier gegenüberliegender Seitenflächen in zwei gleiche Keile gesägt. Wie groß ist das Volumen eines Keils?', 256,
          '8 * 8 / 2 * 8', 'Jeder Keil ist ein Dreiecksprisma: G = 8 · 8 : 2 = 32 cm², h = 8 cm. V = 32 · 8 = 256 cm³ – die Hälfte des Würfels (512 cm³).', 'Welche Grundfläche hat ein Keil?', 'cm³', art=P,
          grafik=prisma_bild([(0, 0), (8, 0), (0, 8)], 8, 'cm', labels={0: '8 cm', 2: '8 cm'})),
        Z('Ein Prisma hat ein Trapez als Grundfläche: Die parallelen Seiten sind 10 cm und 4 cm lang, ihr Abstand ist 5 cm. Die Körperhöhe ist 12 cm. Berechne das Volumen.', 420,
          '(10 + 4) * 5 / 2 * 12', 'G = (10 + 4) · 5 : 2 = 35 cm². V = 35 · 12 = 420 cm³.', 'Trapezfläche, dann mal die Körperhöhe.', 'cm³', art=P, grafik=trapezprisma(10, 4, 5, 12)),
        A(R, 'Die Grundfläche eines Prismas wird verdreifacht, seine Höhe gedrittelt. Was passiert mit dem Volumen?', 'Es bleibt gleich.',
          ['Es wird dreimal so groß.', 'Es wird neunmal so groß.', 'Es wird ein Drittel so groß.'], 'V = G · h. Mal 3 und durch 3 heben sich auf.', 'Setze 3 · G und h : 3 in die Formel ein.', art=K)]
    F['prisma_oberflaeche'] = [
        Z('Ein Prisma hat ein Trapez als Grundfläche (a = 12 cm, c = 6 cm, h = 4 cm, Schenkel je 5 cm) und ist 20 cm lang. Berechne die Oberfläche.', 632, '2 * (12 + 6) * 4 / 2 + (12 + 6 + 5 + 5) * 20',
          'G = (12 + 6) · 4 : 2 = 36 cm², 2 · G = 72 cm². u = 12 + 6 + 5 + 5 = 28 cm, M = 28 · 20 = 560 cm². O = 632 cm².', 'O = 2 · G + u · h.', 'cm²', art=P, grafik=trapezprisma(12, 6, 4, 20)),
        Z('Fünf Würfel mit 2 cm Kante werden zu einem Kreuz (wie ein Pluszeichen) zusammengeklebt, alle in einer Ebene. Wie groß ist die Oberfläche des Körpers?', 88, '(5 * 6 - 2 * 4) * 2 * 2',
          'Fünf Würfel haben 30 Quadrate. Vier Klebestellen verdecken je 2 Quadrate: 30 − 8 = 22 Quadrate zu je 4 cm² = 88 cm². Als Prisma: G = 5 · 4 = 20 cm², u = 12 · 2 = 24 cm, O = 40 + 24 · 2 = 88 cm².',
          'Das Kreuz ist ein Prisma mit kreuzförmiger Grundfläche.', 'cm²', art=P),
        Z('Ein Quader (10 cm · 6 cm · 4 cm) wird parallel zur kleinsten Seitenfläche in zwei gleiche Hälften gesägt. Um wie viel cm² ist die Oberfläche beider Hälften zusammen größer als vorher?', 48,
          '2 * 6 * 4', 'Durch den Schnitt entstehen zwei neue Flächen von je 6 cm · 4 cm = 24 cm². Zusammen 48 cm² mehr.', 'Welche Flächen entstehen beim Sägen neu?', 'cm²', art=K)]
    F['prisma_umstellen'] = [
        Z('Ein Wassertrog hat laut Hersteller 360 l Volumen. Sein Querschnitt (Trapez) hat eine Fläche von 18 dm². Wie lang ist der Trog?', 20, '360 / 18',
          '360 l = 360 dm³. Länge = V : G = 360 : 18 = 20 dm.', 'Liter sind dm³.', 'dm', art=P),
        Z('Ein Trapezprisma (a = 10 cm, c = 6 cm, h = 5 cm, Länge 12 cm) wird zu einem volumengleichen Quader mit der Grundfläche 8 cm · 6 cm umgeformt. Wie hoch ist der Quader?', 10,
          '(10 + 6) * 5 / 2 * 12 / (8 * 6)', 'V = (10 + 6) · 5 : 2 · 12 = 480 cm³. Höhe des Quaders: 480 : 48 = 10 cm.', 'Das Volumen bleibt gleich.', 'cm', art=P),
        Z('Ein Dreiecksprisma hat 240 cm³ und ist 20 cm lang. Sein Dreieck ist rechtwinklig; eine Seite am rechten Winkel ist 4 cm. Wie lang ist die andere?', 6, '2 * 240 / 20 / 4',
          'G = 240 : 20 = 12 cm². Rechtwinkliges Dreieck: 4 · b : 2 = 12, also b = 6 cm.', 'Erst G, dann die zweite Seite.', 'cm', art=K)]
    F['zylinder_volumen'] = [
        A(R, 'Ein Zylinder hat die Höhe 8 und den Radius 3. Welcher Term gibt sein Volumen an?', '72π', ['48π', '24π', '144π'],
          'V = π · 3² · 8 = 72π. 48π ist der Mantel (2 · π · 3 · 8), 24π wäre π · 3 · 8, 144π käme mit 2 · 72π heraus.', 'V = π · r² · h.', art=P),
        PZ('Ein zylinderförmiger Messbecher hat innen den Radius 4 cm. Das Wasser steht 10 cm hoch. Wie viele ml Wasser sind das? Runde auf ganze ml.', f'{PI} * 4 ** 2 * 10', 0,
           'V = π · 4² · 10 = 160π ≈ 503 cm³ = 503 ml.', '1 cm³ = 1 ml.', 'ml', art=P),
        A(R, 'Ein Blatt (20 cm · 30 cm) wird einmal mit der langen, einmal mit der kurzen Seite als Umfang zu einer Röhre gerollt. Welche Röhre hat das größere Volumen?', 'Die mit 30 cm Umfang.',
          ['Die mit 20 cm Umfang.', 'Beide gleich, das Blatt ist dasselbe.', 'Das kann man nicht entscheiden.'],
          'V = u² · h : (4π): 30² · 20 = 18 000 gegen 20² · 30 = 12 000. Der Umfang geht im Quadrat ein, die Höhe nur einfach.', 'Drücke r durch den Umfang aus.', art=K)]
    F['zylinder_oberflaeche'] = [
        A(R, 'Ein Zylinder hat die Höhe 8 und den Radius 3. Welcher Term gibt seine Oberfläche an?', '66π', ['48π', '57π', '72π'],
          'O = 2 · π · 3² + 2 · π · 3 · 8 = 18π + 48π = 66π. 48π ist nur der Mantel, 57π hat nur einen Kreis, 72π ist das Volumen.', 'Zwei Kreise plus Mantel.', art=P),
        A(R, 'Ein Zylinder hat die Höhe 8 und den Radius 3. Welcher Term gibt seinen Mantel an?', '48π', ['24π', '72π', '96π'],
          'M = 2 · π · r · h = 2 · π · 3 · 8 = 48π. Mit d statt r käme 96π heraus.', 'Umfang mal Höhe.', art=P),
        Z('Ein Zylinder hat den Radius 4 cm. Sein Mantel ist genauso groß wie die beiden Kreisflächen zusammen. Wie hoch ist der Zylinder?', 4, '2 * 4 ** 2 / (2 * 4)',
          'Mantel = 2 · π · 4 · h, Kreise = 2 · π · 4² = 32π. Aus 8π · h = 32π folgt h = 4 cm: Der Zylinder ist so hoch wie sein Radius.', 'Setze M = 2 · G an und kürze π.', 'cm', art=K)]
    F['sach'] = [
        PZ('In einen Holzquader (20 cm · 10 cm · 50 cm) wird der Länge nach (50 cm) eine durchgehende Bohrung mit 3 cm Radius gemacht. Wie viel cm³ Holz bleiben? Runde auf ganze cm³.',
           f'20 * 10 * 50 - {PI} * 3 ** 2 * 50', 0, 'Quader: 10 000 cm³. Bohrung: π · 3² · 50 = 450π ≈ 1 414 cm³. Rest ≈ 8 586 cm³.', 'Quader minus Zylinder.', 'cm³', art=P),
        Z('Ein Trog ist ein Trapezprisma (oben 40 cm, unten 100 cm, 20 cm hoch, 35 cm lang). Sein Wasser wird in einen Quader mit 50 cm · 40 cm Grundfläche gegossen. Wie hoch steht es dort?', 24.5,
          '(40 + 100) * 20 / 2 * 35 / (50 * 40)', 'G = (40 + 100) · 20 : 2 = 1 400 cm². V = 1 400 · 35 = 49 000 cm³. Höhe: 49 000 : 2 000 = 24,5 cm.', 'Volumen bleibt gleich.', 'cm', art=P),
        PZ('Dosen (Durchmesser 6,6 cm, Höhe 12 cm) werden stehend in Reihen in einen Karton (40 cm · 30 cm · 12 cm) gestellt, so viele wie passen. '
           'Wie viel Prozent des Kartons bleiben Luft? Runde auf ganze Prozent.', f'(40 * 30 * 12 - 24 * {PI} * 3.3 ** 2 * 12) / (40 * 30 * 12) * 100', 0,
           '6 Dosen nebeneinander (6 · 6,6 = 39,6 cm), 4 Reihen (4 · 6,6 = 26,4 cm): 24 Dosen. Dosen: 24 · π · 3,3² · 12 ≈ 9 853 cm³. Karton: 14 400 cm³. Luft ≈ 4 547 cm³ ≈ 32 %.', 'Erst die Anzahl der Dosen pro Reihe.', '%', art=K)]
    F['verstehen'] = [
        A(R, 'Ein zylinderförmiger Wasserturm wird im Maßstab 1 : 10 als Modell gebaut. Wie viel mal so viel Wasser fasst der echte Turm?', '1 000-mal so viel',
          ['10-mal so viel', '100-mal so viel', '30-mal so viel'], 'Radius und Höhe sind je 10-mal so groß: 10² · 10 = 1 000.', 'Wie oft kommt der Faktor 10 in π · r² · h vor?', art=P),
        Z('Ein Käfig hat einen zylinderförmigen Wassertank (r = 5 cm, h = 12 cm). Der Radius wird verdoppelt, die Höhe halbiert. Um welchen Faktor ändert sich das Volumen?', 2, '2 ** 2 / 2',
          'Radius · 2 bringt den Faktor 4, Höhe : 2 den Faktor 0,5. Zusammen 4 · 0,5 = 2: doppeltes Volumen.', 'Faktor für r² und Faktor für h malnehmen.', None, art=P),
        PZ('In einen Würfel mit 10 cm Kante wird ein Zylinder gestellt, der genau hineinpasst (Durchmesser und Höhe 10 cm). Wie viel Prozent des Würfels füllt er aus? Runde auf eine Stelle nach dem Komma.',
           f'{PI} * 5 ** 2 * 10 / 1000 * 100', 1, 'Zylinder: π · 5² · 10 = 250π ≈ 785,4 cm³. Würfel: 1 000 cm³. Anteil ≈ 78,5 % (genau π : 4).', 'Rechne beide Volumen aus.', '%', art=K)]
    return F


def datei():
    auf, anz = aufgaben(ETAPPEN, GEN, fest, SEED)
    lz = [e['lernziel'] for e in ETAPPEN]
    return {
        **META, 'autor': 'Claude (Achtzehnte Runde, Teil A; Generator messen.prisma_zylinder.py)',
        'inhalt': {
            'ziel': 'Volumen gerader Prismen mit V = G · h begründen und berechnen, Oberflächen über das Netz bestimmen, Formeln umstellen, die Zylinderformeln als Grenzfall des Prismas '
                    'und über das Netz begründen und vertiefen (Hohlzylinder, Mantel, offene Körper) und Prismen und Zylinder in Sachsituationen mit sinnvollen Annahmen nutzen.',
            'merke': ['Prisma: V = G · h, O = 2 · G + M mit M = u · h.', 'Umstellen: h = V : G, G = V : h.', 'Zylinder: V = π · r² · h (Grenzfall des Prismas).',
                      'Zylinder: O = 2 · π · r² + 2 · π · r · h; der Mantel ist aufgeklappt ein Rechteck u · h.', 'Doppelter Radius: 4-faches Volumen.'],
            'abschnitte': [{'titel': 'Prismen', 'lernziele': ['prisma_volumen', 'prisma_oberflaeche', 'prisma_umstellen']},
                           {'titel': 'Zylinder', 'lernziele': ['zylinder_volumen', 'zylinder_oberflaeche']},
                           {'titel': 'Anwenden und begründen', 'lernziele': ['sach', 'verstehen']}],
            'etappen': ETAPPEN,
            'teilfaehigkeiten': [{'k': e['lernziel'], 'text': e['titel'], 'lernziele': [e['lernziel']]} for e in ETAPPEN],
            'bewertung': {'lernziele_pflicht': lz, 'lernziele_vertiefung': [], 'testaufgaben_je_lernziel': 1, 'hilfen_im_test': False},
            'quellen': {'erklaerungen': 'Eigene Fassung (Claude).',
                        'begriffe': 'Fachbegriffe nach LehrplanPLUS Bayern, Gymnasium M8 7 „Kreis und Zylinder“ (https://www.lehrplanplus.bayern.de/fachlehrplan/gymnasium/8/mathematik).',
                        'pruefungsvorbilder': 'Typ und Niveau nach: Bayerischer Mathematik-Test 10 (ISB) 2024 B6 (Zylinder, Term auswählen), 2021 A/B (Wasser im Messbecher); '
                                              'Bayerischer Mathematik-Test 8 (ISB) 2008 (Restkörper), 2009 A1 (Würfel diagonal geteilt), 2023 A (Volumen in Litern, Höhe gesucht), '
                                              '2025 A (Maßstab und Volumen); Abschlussprüfung Realschule Bayern 2020 Mathematik I B1 (Prisma mit Trapez-Grundfläche); niveaubestimmende '
                                              'Aufgabe Sachsen-Anhalt Schuljahrgang 7/8 (Trapezprisma, volumengleicher Quader); IQB-Lernaufgabe „Hamsterhaltung“ (Zylinder, Änderung '
                                              'einer Größe); VERA-8 2012 Modul C („Würfelkörper“). Eigene Zahlen und Einkleidung.'},
        },
        'aufgaben': auf,
        'offen': ['Die Karte „zylinder“ in messen.kreisberechnung (Buenos Aires) bleibt dort; hier wird auf sie verwiesen und vertieft (Grenzfall, Netz, Hohlzylinder, Umstellen).',
                  'Zylinder sind liegend im Schrägbild gezeichnet (vordere Grundfläche als Kreis in wahrer Größe, Achse unter 45° halb so lang); die hintere Kreislinie ist ganz gezeichnet.',
                  'Kein Satz des Pythagoras (erst Klasse 9): schräge Kanten und Diagonalen sind immer angegeben.'],
    }, anz


# ---- STUFEN (Zwanzigste Runde: echte Stufe 3 und Knobel-Bordkarten, siehe _stufen_kl8.py) ----
from _stufen_kl8 import Stufen, stufen_auf_datei  # noqa: E402

ST = Stufen('messen.prisma_zylinder', 20_8_12)
SA, SZ, SL = ST.A, ST.Z, ST.L
def T(lz, *regeln):
    for m, g in regeln: ST.typ(lz, m, g)
SPI = '3.14159265'

# --- prisma_volumen ---
ST.leiter('prisma_volumen', 'V = G · h für Prismen mit Dreieck- oder Trapez-Grundfläche anwenden',
          'L-Profil zerlegen, Sachprismen (Blumenkasten), Parallelogramm, Höhe aus dem Volumen',
          'Würfel und Quader durchsägen, Graben wie in einer Prüfung, Veränderungen begründen, Formelfehler beim Dreieck, Bleistift-Sechseck verknüpfen')
T('prisma_volumen', (r'^Ein gerades Prisma hat als Grundfläche|Grundfläche von 26 cm²', 'direkt'), (r'Blumenkasten', 'einkleidung'), (r'Winkelprofil|Dreiecksprisma: Grundfläche|Parallelogramm', 'mehrschritt'),
  (r'Holzwürfel|durchgesägt', 'transfer'), (r'parallelen Seiten sind 10', 'rueckwaerts'), (r'verdreifacht|Prisma A', 'begruenden'), (r'Graben', 'pruefung'), (r'Max', 'fehler'), (r'Bleistift', 'verknuepfen'))
ST.neu('prisma_volumen', 'erkennen', SA('Welche Formel gilt für das Volumen eines geraden Prismas mit dreieckiger Grundfläche (g, h_D) und Körperhöhe h?', 'V = g · h_D : 2 · h', ['V = g · h_D · h', 'V = g · h', 'V = (g + h_D) · h'],
    'Grundfläche (Dreieck g · h_D : 2) mal Körperhöhe.', 'Erst die Dreiecksfläche, dann mal Körperhöhe.'))
ST.neu('prisma_volumen', 'umkehr', SZ('Ein Prisma hat 120 cm³ Volumen; seine Grundfläche ist ein Dreieck mit g = 6 cm und Höhe 4 cm. Wie hoch ist das Prisma?', 10, '120 / (6 * 4 / 2)', 'G = 6 · 4 : 2 = 12 cm². h = 120 : 12 = 10 cm.', 'Berechne zuerst die Grundfläche.', einheit='cm'))
ST.knobel('prisma_volumen', SZ('Aus einem Würfel mit 6 cm Kante wird entlang einer Kante ein Dreiecksprisma herausgeschnitten: Grundfläche ein rechtwinkliges Dreieck mit 2 cm und 3 cm am rechten Winkel, Länge 6 cm. Wie groß ist das Restvolumen?', 198, '6**3 - 2 * 3 / 2 * 6',
    'Würfel 216 cm³. Herausgeschnitten: (2 · 3 : 2) · 6 = 18 cm³. Rest 198 cm³.', 'Das herausgeschnittene Stück ist selbst ein Prisma.', einheit='cm³'))
ST.knobel('prisma_volumen', SZ('Drei Prismen haben dieselbe Höhe, ihre Grundflächen verhalten sich wie 1 : 2 : 3. Zusammen haben sie 360 cm³. Wie groß ist das Volumen des größten?', 180, '360 * 3 / 6',
    'Bei gleicher Höhe verhalten sich die Volumen wie die Grundflächen: 1 + 2 + 3 = 6 Teile zu je 60 cm³. Das größte hat 180 cm³.', 'Wie hängen die Volumen zusammen, wenn h gleich ist?', einheit='cm³'))

# --- prisma_oberflaeche ---
ST.leiter('prisma_oberflaeche', 'Mantel aus Umfang · Höhe und Oberfläche eines Dreiecksprismas berechnen',
          'Trapezprismen, offene Rinne, Zelt mit Boden, Mantel aus dem Netz, Keil',
          'Würfelkreuz, durchgesägter Quader, Lackbedarf, Dach, Höhe verdoppelt begründen, Umfang rückwärts')
T('prisma_oberflaeche', (r'Wie groß ist sein Mantel|^Ein Dreiecksprisma: Grundfläche gleichschenklig', 'direkt'), (r'Futterrinne|Zelt', 'einkleidung'), (r'Im Netz', 'darstellung'),
  (r'und ist 20 cm lang', 'pruefung'), (r'Trapez als Grundfläche|Keil hat', 'mehrschritt'), (r'Kreuz|Haus|Keile', 'transfer'), (r'gesägt|Holzschachtel', 'verknuepfen'),
  (r'doppelt so hoch', 'begruenden'), (r'Mantel eines Prismas hat', 'rueckwaerts'))
ST.neu('prisma_oberflaeche', 'erkennen', SA('Woraus besteht die Oberfläche eines Prismas?', 'aus den zwei Grundflächen und dem Mantel', ['nur aus dem Mantel', 'aus einer Grundfläche und dem Mantel', 'aus den Seitenkanten'],
    'O = 2 · G + M: unten, oben und die Seitenflächen.', 'Denk an das Netz.'))
ST.knobel('prisma_oberflaeche', SZ('Ein Würfel mit 3 cm Kante wird in 27 Würfel mit 1 cm Kante zersägt. Um wie viel cm² ist die Oberfläche aller kleinen Würfel zusammen größer als die des großen?', 108, '27 * 6 - 6 * 9',
    'Kleine Würfel: 27 · 6 = 162 cm². Großer Würfel: 6 · 9 = 54 cm². Unterschied 108 cm² – das sind die neuen Schnittflächen.', 'Berechne beide Oberflächen getrennt.', einheit='cm²'))
ST.knobel('prisma_oberflaeche', SZ('Zwei Quader mit 2 cm × 3 cm × 4 cm werden mit ihren größten Flächen aneinandergeklebt. Wie groß ist die Oberfläche des neuen Körpers?', 80, '2 * 2 * (6 + 8 + 12) - 2 * 12',
    'Ein Quader: 2 · (6 + 8 + 12) = 52 cm². Zwei: 104 cm². Beim Kleben verschwinden zwei Flächen von je 3 · 4 = 12 cm²: 104 − 24 = 80 cm².', 'Welche Flächen sind nach dem Kleben nicht mehr außen?', einheit='cm²'))

# --- prisma_umstellen ---
ST.leiter('prisma_umstellen', 'aus V und h die Grundfläche bzw. aus V und G die Höhe berechnen',
          'Liter umrechnen (Gefäß), Seite aus dem Volumen, passende Grundfläche erkennen',
          'Trog und Rinne modellieren, volumengleicher Quader, rückwärts zur Dreiecksseite, Masse des Balkens wie in einer Prüfung, vertauschte Division als Fehler')
T('prisma_umstellen', (r'^Ein Prisma hat (das Volumen|[\d,]+ m³ Volumen)', 'direkt'), (r'Gefäß in Prismaform|Grundfläche von 1 200', 'einkleidung'), (r'Dreiecksprisma hat das Volumen 150|Becken', 'mehrschritt'),
  (r'Wassertrog|Regenrinne', 'transfer'), (r'volumengleichen Quader', 'verknuepfen'), (r'rechtwinklig|Keil', 'rueckwaerts'), (r'Betonbalken', 'pruefung'))
ST.neu('prisma_umstellen', 'erkennen', SA('Welche Umstellung von V = G · h gibt die Höhe?', 'h = V : G', ['h = G : V', 'h = V · G', 'h = V − G'], 'Durch G teilen: V : G = h.', 'Welche Rechnung macht „· G“ rückgängig?'))
ST.neu('prisma_umstellen', 'umkehr', SZ('Ein Prisma mit quadratischer Grundfläche ist 8 cm hoch und hat 200 cm³ Volumen. Wie lang ist eine Quadratseite?', 5, '5', 'G = 200 : 8 = 25 cm², Seite 5 cm.', 'Erst G, dann die Seite.', einheit='cm'))
ST.neu('prisma_umstellen', 'darstellung', SA('Ein Prisma hat 96 cm³ Volumen und ist 8 cm hoch. Welche Grundfläche passt?', 'ein Rechteck 3 cm × 4 cm', ['ein Quadrat mit 4 cm Seite', 'ein Dreieck mit g = 3 cm und Höhe 4 cm', 'ein Rechteck 6 cm × 4 cm'],
    'G = 96 : 8 = 12 cm². Nur 3 · 4 = 12 passt (Quadrat 16, Dreieck 6, Rechteck 24).', 'Berechne G und prüfe jede Figur.'))
ST.neu('prisma_umstellen', 'fehler', SA('Ein Prisma hat 72 cm³ und G = 9 cm². Jemand rechnet h = 9 : 72 = 0,125 cm. Was stimmt?', 'Falsch: h = V : G = 72 : 9 = 8 cm.', ['Richtig.', 'Falsch: h = 72 · 9 cm.', 'Falsch: h = 72 − 9 cm.'],
    'Probe: 9 · 0,125 = 1,125 ≠ 72. Mit 8 cm: 9 · 8 = 72 ✓.', 'Mach die Probe mit V = G · h.'))
ST.knobel('prisma_umstellen', SZ('Ein Aquarium (Grundfläche 50 cm × 30 cm) ist 20 cm hoch mit Wasser gefüllt. Ein Stein mit 3 l Volumen wird ganz eingetaucht. Um wie viele Zentimeter steigt der Wasserspiegel?', 2, '3000 / (50 * 30)',
    'Der Stein verdrängt 3 000 cm³ Wasser. Verteilt auf 1 500 cm² Grundfläche: 3 000 : 1 500 = 2 cm.', 'Das verdrängte Wasser bildet einen flachen Quader.', einheit='cm'))
ST.knobel('prisma_umstellen', SZ('Eine Rinne ist ein Dreiecksprisma, das auf der Kante steht: Querschnitt oben 20 cm breit, 10 cm tief, Länge 30 cm. Sie ist bis zur halben Tiefe gefüllt. Wie viele Liter sind darin?', 0.75, '(10 * 5 / 2) * 30 / 1000',
    'Die Seitenwände sind gerade: Von der Kante unten bis oben (10 cm) wird die Rinne gleichmäßig breiter, von 0 auf 20 cm, also pro cm Höhe um 2 cm. Bei 5 cm Wasserhöhe ist die Wasseroberfläche darum 10 cm breit. Die Wasserfläche ist ein Dreieck mit 10 cm Breite und 5 cm Höhe: 10 · 5 : 2 = 25 cm² – nur ein Viertel des Querschnitts (100 cm²). V = 25 · 30 = 750 cm³ = 0,75 l.',
    'Zeichne den Querschnitt: Wie breit ist die Wasseroberfläche bei halber Tiefe?', einheit='l'))

# --- zylinder_volumen ---
ST.leiter('zylinder_volumen', 'V = π · r² · h berechnen (auch aus d), Volumen als Grundfläche · Höhe erkennen',
          'halbe Zylinder, Rohre, Topf in Litern, Höhe aus exaktem Volumen, exakter Term',
          'Messbecher und Schlauch, Mindesthöhe rückwärts, Vergleiche begründen, Radius verdoppelt, Umfüllen verknüpfen, Mantel statt Volumen als Fehler')
T('zylinder_volumen', (r'Regentonne|^Ein Zylinder hat den Durchmesser', 'direkt'), (r'Kuchenform|Rohr', 'mehrschritt'), (r'Topf', 'einkleidung'), (r'54π', 'umkehr'),
  (r'Welcher Term', 'darstellung'), (r'Messbecher|Gartenschlauch', 'transfer'), (r'Blatt|Zylinder A', 'begruenden'), (r'10 l fassen', 'rueckwaerts'), (r'verdoppelt', 'parameter'),
  (r'umgefüllt', 'verknuepfen'))
ST.neu('zylinder_volumen', 'erkennen', SA('Woraus berechnet man das Volumen eines Zylinders?', 'Grundfläche (Kreis) mal Höhe', ['Umfang mal Höhe', 'Radius mal Höhe', 'Durchmesser mal Höhe'], 'Wie beim Prisma: V = G · h mit G = π · r².', 'Ein Zylinder ist wie ein Prisma mit Kreis als Grundfläche.'))
ST.neu('zylinder_volumen', 'fehler', SA('Für r = 3 cm und h = 10 cm rechnet jemand V = 2 · π · 3 · 10 ≈ 188 cm³. Was ist falsch?', 'Das ist der Mantel; V = π · 9 · 10 ≈ 283 cm³.', ['Nichts.', 'Er hätte d = 6 nehmen müssen.', 'Es fehlt · 2 am Ende.'],
    '2 · π · r · h ist die Mantelfläche (Umfang · Höhe). Für das Volumen braucht man die Kreisfläche π · r².', 'Welche Formel enthält r²?'))
ST.knobel('zylinder_volumen', SZ('Ein Glas (r = 3 cm) steht in einem zylindrischen Gefäß (r = 6 cm). In den Raum zwischen Glas und Gefäßwand wird Wasser 4 cm hoch gefüllt. Wie viel cm³ sind das (π ≈ 3,14)? Runde auf ganze cm³.', 339, 'round(314/100 * (36 - 9) * 4)',
    'Der Wasserkörper ist ein Ring: Querschnitt π · (36 − 9) = 27π cm². Mal 4 cm: 108π ≈ 339 cm³.', 'Welche Form hat die Wasserfläche von oben?', einheit='cm³', toleranz=1))
ST.knobel('zylinder_volumen', SZ('Eine Papierrolle hat außen 10 cm und innen (Pappkern) 2 cm Radius und ist 20 cm breit. Das Papier ist 0,1 mm dick. Wie viele Meter Papier sind etwa aufgerollt (π ≈ 3,14)? Runde auf ganze Meter.', 301, 'round(314/100 * (100 - 4) * 20 / (1/100 * 20) / 100)',
    'Papiervolumen: π · (100 − 4) · 20 ≈ 6 029 cm³. Abgerollt ist es ein langer Streifen: 20 cm breit, 0,01 cm dick, Länge L. 20 · 0,01 · L = 6 029 ⇒ L ≈ 30 144 cm ≈ 301 m.',
    'Das Volumen bleibt gleich, ob aufgerollt oder ausgelegt.', einheit='m', toleranz=1))

# --- zylinder_oberflaeche ---
ST.leiter('zylinder_oberflaeche', 'Mantel und Oberfläche eines Zylinders mit der Formel berechnen',
          'Etikett, Becher ohne Deckel, Rohr außen, Oberfläche aus d, Höhe aus exaktem Mantel, exakte Terme',
          'Mantel = Kreisflächen rückwärts, Vergleich begründen, Folientunnel, Radius aus dem Netz, Kreisflächen vergessen als Fehler, Parameter, Blechbedarf wie in einer Prüfung')
T('zylinder_oberflaeche', (r'^Ein Zylinder hat r = [\d,]+ cm und h = \d+ cm\. (Berechne seine Oberfläche|Wie groß ist sein Mantel)', 'direkt'), (r'Etikett|Rohr|Litfaßsäule', 'einkleidung'),
  (r'Durchmesser \d+ cm und die Höhe|Becher', 'mehrschritt'), (r'42π', 'umkehr'), (r'Welcher Term', 'darstellung'), (r'genauso groß wie die beiden', 'rueckwaerts'),
  (r'Zylinder A|Blatt', 'begruenden'), (r'Folientunnel', 'transfer'), (r'Netz eines Zylinders', 'rueckwaerts'))
ST.neu('zylinder_oberflaeche', 'erkennen', SA('Wie lang ist das Mantelrechteck eines Zylinders?', 'so lang wie der Umfang des Grundkreises', ['so lang wie der Durchmesser', 'so lang wie der Radius', 'so lang wie die Höhe'],
    'Das Rechteck reicht genau einmal um den Kreis herum.', 'Was umschließt das Etikett?'))
ST.neu('zylinder_oberflaeche', 'fehler', SA('Jemand berechnet die Oberfläche eines Zylinders (r = 2 cm, h = 5 cm) als 2 · π · 2 · 5 ≈ 62,8 cm². Was fehlt?', 'die beiden Kreisflächen: + 2 · π · 4 ≈ 25,1 cm², zusammen ≈ 87,9 cm²',
    ['nichts', 'eine Kreisfläche: zusammen ≈ 75,4 cm²', 'die Höhe muss quadriert werden'], 'O = 2 · G + M. Berechnet wurde nur M.', 'Aus welchen Teilen besteht das Netz?'))
ST.neu('zylinder_oberflaeche', 'parameter', SA('Für welche Höhe ist bei r = 3 cm der Mantel genauso groß wie EINE Kreisfläche?', 'h = 1,5 cm', ['h = 3 cm', 'h = 6 cm', 'h = 0,5 cm'],
    '2 · π · r · h = π · r² ⇒ h = r : 2 = 1,5 cm.', 'Setze Mantel und Kreisfläche gleich und teile durch π · r.'))
ST.neu('zylinder_oberflaeche', 'pruefung', SZ('Eine Dose (d = 10 cm, h = 12 cm) wird aus Blech gefertigt; für Falze kommen 10 % dazu. Wie viel cm² Blech braucht man? Runde auf ganze cm².', 587, f'round({SPI} * (2 * 25 + 10 * 12) * 11/10)',
    'O = 2 · π · 25 + π · 10 · 12 = 170π ≈ 534,1 cm². Mit 10 % Zuschlag: 534,1 · 1,1 ≈ 587 cm².', 'Erst die Oberfläche, dann den Zuschlag.', einheit='cm²', toleranz=1))
ST.knobel('zylinder_oberflaeche', SZ('Ein Zylinder (r = 2 cm, h = 10 cm) wird in zwei gleich hohe Zylinder zersägt. Um wie viel cm² wächst die Oberfläche (π ≈ 3,14)? Runde auf eine Nachkommastelle.', 25.1, 'round(2 * 314/100 * 4, 1)',
    'Mantel und alte Deckel bleiben gleich. Neu sind zwei Schnittflächen, je π · 4: zusammen 8π ≈ 25,1 cm².', 'Was ist nach dem Sägen neu außen?', einheit='cm²', toleranz=0.1))
ST.knobel('zylinder_oberflaeche', SZ('Bei einem Zylinder ist der Mantel doppelt so groß wie die beiden Kreisflächen zusammen. Der Radius ist 3 cm. Wie hoch ist er?', 6, '2 * 3',
    'Mantel 2 · π · r · h, Kreisflächen zusammen 2 · π · r². Bedingung: 2πrh = 2 · 2πr². Teilen durch 2πr ergibt h = 2r = 6 cm.', 'Stelle die Gleichung auf und kürze so viel wie möglich.', einheit='cm'))

# --- sach ---
ST.leiter('sach', 'Volumen von Haus und Regentonne als Prisma bzw. Zylinder berechnen',
          'Säulen, Baumstamm, schräges Becken, Zelt, Treppe, Wasserhöhe rückwärts',
          'Bohrung und Rinne verknüpfen, Trog umfüllen, Dosen packen, Füllzeit und Kosten wie in einer Prüfung, Mindesthöhe rückwärts, halbvoller Tank')
T('sach', (r'^Ein Haus ist|^Eine Regentonne ist ein Zylinder', 'direkt'), (r'Betonsäulen|Zelt|[Tt]reppe', 'mehrschritt'), (r'Baumstamm|Becken ist', 'einkleidung'),
  (r'Bohrung|Rinne', 'verknuepfen'), (r'Trog|Dosen|Öltank', 'transfer'), (r'Pool|Neubau', 'pruefung'), (r'330 ml', 'rueckwaerts'))
ST.neu('sach', 'erkennen', SA('Ein Baumstamm soll für eine Rechnung durch einen Körper ersetzt werden. Welcher passt am besten?', 'ein Zylinder', ['ein Quader', 'eine Pyramide', 'eine Kugel'], 'Ein Stamm ist rund und überall etwa gleich dick – wie ein Zylinder.', 'Welche Form hat ein Querschnitt?'))
ST.neu('sach', 'umkehr', SZ('Eine Regentonne hat 0,25 m² Grundfläche und enthält 150 l Wasser. Wie hoch steht das Wasser?', 60, '150 / 25 * 10', '0,25 m² = 25 dm², 150 l = 150 dm³. h = 150 : 25 = 6 dm = 60 cm.', 'Rechne in dm: 1 l = 1 dm³.', einheit='cm'))
ST.knobel('sach', SZ('Ein Becken (25 m × 10 m) ist 2 m tief gefüllt. Eine Pumpe schafft 20 l pro Sekunde. Wie viele Stunden dauert das Leerpumpen? Runde auf eine Nachkommastelle.', 6.9, 'round(25 * 10 * 2 * 1000 / 20 / 3600, 1)',
    '500 m³ = 500 000 l. 500 000 : 20 = 25 000 s. 25 000 : 3 600 ≈ 6,9 h.', 'Rechne in Liter und Sekunden, dann in Stunden um.', einheit='h', toleranz=0.1))
ST.knobel('sach', SZ('Ein liegender zylindrischer Tank (r = 1 m, 4 m lang) ist voll. Pro Minute werden 50 l abgepumpt. Nach wie vielen Minuten ist er halb leer (π ≈ 3,14)? Runde auf ganze Minuten.', 126, 'round(314/100 * 1 * 4 / 2 * 1000 / 50)',
    'V = π · 1² · 4 ≈ 12,56 m³. Die Hälfte: 6,28 m³ = 6 280 l. 6 280 : 50 ≈ 126 Minuten.', 'Die halbe Füllung ist das halbe Volumen – egal ob der Tank liegt.', einheit='min', toleranz=1))

# --- verstehen ---
ST.leiter('verstehen', 'Volumen bei verdoppelter Höhe oder Grundfläche angeben, V = G · h erkennen',
          'Grundfläche und Höhe zugleich ändern, Prisma und Zylinder mit gleichem G und h, Radius verdreifacht, Kerze, Faktor rückwärts',
          'Maßstab und alle Längen verdoppelt, Würfel und Zylinder, Prozent wie in einer Prüfung, Aussagen begründen, Mantelformel mit d als Fehler')
T('verstehen', (r'wird doppelt so hoch|wird (doppelt|dreimal) so groß, die Höhe bleibt gleich', 'direkt'), (r'Welche Formel gilt', 'erkennen'), (r'^Nina', 'fehler'),
  (r'150 cm³|Prisma mit dreieckiger Grundfläche und ein Zylinder|Radius wird dreimal', 'mehrschritt'), (r'Wasserturm|Alle Längen', 'verknuepfen'), (r'Käfig|Würfel mit 10', 'transfer'),
  (r'Blatt|Welche Aussage ist richtig', 'begruenden'), (r'20 %', 'pruefung'))
ST.neu('verstehen', 'einkleidung', SA('Eine Kerze (Zylinder) wird halb so hoch, aber mit doppeltem Durchmesser gegossen. Wie viel Wachs braucht man im Vergleich?', 'doppelt so viel', ['gleich viel', 'halb so viel', 'viermal so viel'],
    'Doppelter Durchmesser: vierfache Grundfläche. Halbe Höhe: halbiert. 4 · 1/2 = 2.', 'Wie ändert sich die Grundfläche?'))
ST.neu('verstehen', 'umkehr', SZ('Das Volumen eines Prismas soll gleich bleiben, die Höhe wird verfünffacht. Durch welche Zahl muss man die Grundfläche teilen?', 5, '5', 'V = G · h: wird h fünfmal so groß, muss G ein Fünftel sein.', 'Was muss mit G passieren, damit G · h gleich bleibt?'))
ST.knobel('verstehen', SZ('Alle Kanten eines Prismas werden um 50 % verlängert. Auf das Wievielfache wächst das Volumen?', 3.375, '(3/2)**3',
    'Jede Länge wird 1,5-mal so groß: Die Grundfläche wächst mit 1,5² = 2,25, das Volumen mit 1,5³ = 3,375.', 'Wie oft steckt der Faktor 1,5 in einem Volumen?'))
ST.knobel('verstehen', SA('Zylinder A hat r = 6 cm und h = 2 cm, Zylinder B hat r = 2 cm und h = 18 cm. Was stimmt?', 'Beide haben dasselbe Volumen, aber B hat den größeren Mantel.',
    ['A hat das größere Volumen und den größeren Mantel.', 'Beide haben dasselbe Volumen und denselben Mantel.', 'B hat das größere Volumen, A den größeren Mantel.'],
    'V_A = π · 36 · 2 = 72π, V_B = π · 4 · 18 = 72π. Mantel A = 2π · 6 · 2 = 24π, Mantel B = 2π · 2 · 18 = 72π.', 'Berechne beide Größen mit π als Zeichen.'))

_datei_alt = datei
def datei():
    d, anz = _datei_alt()
    stufen_auf_datei(ST, d)
    return d, anz
# ---- STUFEN ENDE ----

# ---------- TEXT: Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers) – mehr Textaufgaben, siehe _text_kl8.py ----------
from _text_kl8 import Text, mit_text, text_auf_datei  # noqa: E402
TX = Text('messen.prisma_zylinder', 22_8_12)
TZ, TA, TL, TW = TX.Z, TX.A, TX.L, TX.W

PI = '3.141592653589793'
TX.huerde_alt('zylinder_volumen', r'Wie hoch muss er mindestens sein', 'deuten')
TX.huerde_alt('sach', r'so viele wie passen', 'deuten')
TX.huerde_alt('sach', r'Wie viele Minuten dauert es', 'deuten')

# --- prisma_volumen ---
TX.u('prisma_volumen', 'direkt', TZ('Ein Pralinenkarton hat die Form eines Dreiecksprismas. Die dreieckige Grundfläche ist 24 cm² groß, der Karton ist 15 cm lang. Wie viel cm³ passen hinein?', '24 * 15',
    TW('G = 24 cm², Länge (Höhe des Prismas) 15 cm.', 'Volumen.', 'V = G · h.', 'V = 24 · 15 = 360 cm³.', 'In den Karton passen 360 cm³.'), 'Welche Fläche ist die Grundfläche, welche Länge die Höhe des Prismas?', einheit='cm³'))
TX.u('prisma_volumen', 'einkleidung', TZ('Ein Zelt hat die Form eines Dreiecksprismas. Die Vorderseite ist ein Dreieck mit 2,4 m Breite und 1,5 m Höhe, das Zelt ist 3 m lang. Wie viel m³ Luft sind im Zelt?', '2.4 * 1.5 / 2 * 3',
    TW('Dreieck g = 2,4 m, h = 1,5 m; Länge 3 m.', 'Luftvolumen.', 'G = g · h : 2, dann V = G · Länge.', 'G = 2,4 · 1,5 : 2 = 1,8 m². V = 1,8 · 3 = 5,4 m³.', 'Im Zelt sind 5,4 m³ Luft.'), 'Die Vorderseite ist die Grundfläche.', einheit='m³'))
TX.u('prisma_volumen', 'mehrschritt', TZ('Ein Schwimmbecken ist 25 m lang und 10 m breit. Am einen Ende ist es 1 m tief, zum anderen Ende hin wird es gleichmäßig bis 3 m tief. Wie viel m³ Wasser passen hinein?', '(1 + 3) / 2 * 25 * 10',
    TW('Länge 25 m, Breite 10 m, Tiefe von 1 m bis 3 m.', 'Volumen des Beckens.', 'Von der Seite gesehen ist das Becken ein Trapez: G = (a + c) : 2 · h; dann · Breite.', 'G = (1 + 3) : 2 · 25 = 50 m². V = 50 · 10 = 500 m³.', 'Es passen 500 m³ Wasser hinein.'),
    'Schau von der Seite auf das Becken: Welche Figur siehst du?', einheit='m³'))
TX.u('prisma_volumen', 'pruefung', TZ('Ein Pferdetrog ist ein Prisma mit trapezförmigem Querschnitt: oben 60 cm, unten 40 cm breit, 30 cm tief und 2 m lang. Er steht auf vier 50 cm hohen Beinen und wiegt 35 kg. Wie viele Liter Wasser fasst er?',
    '(60 + 40) / 2 * 30 * 200 / 1000', TW('Trapez 60 cm / 40 cm, Tiefe 30 cm, Länge 200 cm. Beine und Gewicht spielen keine Rolle.', 'Fassungsvermögen in Litern.', 'G = (a + c) : 2 · h, V = G · Länge, 1 l = 1 000 cm³.',
    'G = 50 · 30 = 1 500 cm². V = 1 500 · 200 = 300 000 cm³ = 300 l.', 'Der Trog fasst 300 l.'), 'Welche Angaben beschreiben den Innenraum des Trogs?', einheit='l'), huerde='ueberfluessig')
TX.u('prisma_volumen', 'rueckwaerts', TZ('Ein Blumenkasten ist ein Quader, 80 cm lang und 20 cm breit. Es sollen 40 l Erde hinein, und oben sollen noch 2 cm frei bleiben. Wie hoch muss der Kasten mindestens sein?', '40000 / (80 * 20) + 2',
    TW('Grundfläche 80 cm · 20 cm, 40 l Erde, 2 cm Rand.', 'Mindesthöhe.', 'Höhe der Erde = V : G, dann den freien Rand dazu.', '40 l = 40 000 cm³. 40 000 : 1 600 = 25 cm. 25 + 2 = 27 cm.', 'Der Kasten muss mindestens 27 cm hoch sein.'),
    'Wie hoch liegt die Erde? Und was kommt dann noch dazu?', einheit='cm'), huerde='zwei')
TX.s('prisma_volumen', TZ('Ein Stück Käse hat die Form eines Dreiecksprismas: Die Grundfläche ist 18 cm² groß, das Stück ist 9 cm lang. Wie viel cm³ Käse sind das?', '18 * 9',
    TW('G = 18 cm², h = 9 cm.', 'Volumen.', 'V = G · h.', 'V = 18 · 9 = 162 cm³.', 'Das Stück hat 162 cm³.'), einheit='cm³'))
TX.k('prisma_volumen', TZ('Ein Kanal hat einen rechteckigen Querschnitt, 4 m breit und 1,5 m tief, und ist 200 m lang. Wie viel m³ Wasser sind darin, wenn er ganz voll ist?', '4 * 1.5 * 200',
    TW('Querschnitt 4 m · 1,5 m, Länge 200 m.', 'Wasservolumen.', 'V = G · Länge.', 'G = 6 m². V = 6 · 200 = 1 200 m³.', 'Im vollen Kanal sind 1 200 m³ Wasser.'), einheit='m³'))

# --- prisma_oberflaeche ---
TX.u('prisma_oberflaeche', 'direkt', TZ('Ein würfelförmiges Geschenk mit 12 cm Kantenlänge wird ganz mit Papier beklebt, ohne Überlappung. Wie viel cm² Papier braucht man?', '6 * 12**2',
    TW('Würfel, a = 12 cm.', 'Oberfläche.', 'O = 6 · a².', 'O = 6 · 144 = 864 cm².', 'Man braucht 864 cm² Papier.'), 'Wie viele gleiche Flächen hat ein Würfel?', einheit='cm²'))
TX.u('prisma_oberflaeche', 'einkleidung', TZ('Ein Aquarium ist ein Quader, 60 cm lang, 30 cm breit und 35 cm hoch, und oben offen. Wie viel cm² Glas hat es?', '60 * 30 + 2 * 60 * 35 + 2 * 30 * 35',
    TW('Quader 60 · 30 · 35 cm, ohne Deckel.', 'Glasfläche.', 'Boden + zwei lange + zwei kurze Seiten.', '1 800 + 2 · 2 100 + 2 · 1 050 = 8 100 cm².', 'Das Aquarium hat 8 100 cm² Glas.'), 'Welche Fläche fehlt, weil es oben offen ist?', einheit='cm²'))
TX.u('prisma_oberflaeche', 'pruefung', TZ('Eine Schokoladenverpackung ist ein Dreiecksprisma. Ihre Grundfläche ist ein gleichseitiges Dreieck mit 6 cm Seitenlänge und 5,2 cm Höhe, die Verpackung ist 20 cm lang. Sie enthält 200 g und kostet 3,49 €. Wie viel cm² Karton braucht man ohne Klebelaschen? Runde auf ganze cm².',
    '2 * 6 * 5.2 / 2 + 3 * 6 * 20', TW('Dreieck g = 6 cm, h = 5,2 cm; drei Rechtecke 6 cm · 20 cm. Gewicht und Preis spielen keine Rolle.', 'Oberfläche.', 'O = 2 · G + M.',
    'G = 6 · 5,2 : 2 = 15,6 cm². 2G = 31,2 cm². M = 3 · 120 = 360 cm². O = 391,2 cm².', 'Man braucht etwa 391 cm² Karton.'), 'Welche Angaben brauchst du für die Flächen der Verpackung?', einheit='cm²', toleranz=1), huerde='ueberfluessig')
TX.u('prisma_oberflaeche', 'begruenden', TX.A('Zwei Geschenkkartons haben beide 1 000 cm³ Volumen: ein Würfel mit 10 cm Kante und ein Quader mit 20 cm × 10 cm × 5 cm. Für welchen braucht man weniger Geschenkpapier?',
    'Für den Würfel: 600 cm² statt 700 cm².', ['Für den Quader, weil er flacher ist.', 'Für beide gleich viel, weil das Volumen gleich ist.', 'Für den Würfel: 100 cm² statt 1 000 cm².'],
    TW('Würfel a = 10 cm; Quader 20 · 10 · 5 cm.', 'Welcher braucht weniger Papier?', 'Beide Oberflächen berechnen.', 'Würfel: 6 · 100 = 600 cm². Quader: 2 · (200 + 100 + 50) = 700 cm².', 'Der Würfel braucht weniger Papier.'),
    'Gleiches Volumen heißt nicht gleiche Oberfläche – rechne beide aus.'), huerde='entscheidung')

# --- prisma_umstellen ---
TX.u('prisma_umstellen', 'direkt', TZ('Ein Milchkarton ist ein Quader mit 50 cm² Grundfläche und fasst 1 l, also 1 000 cm³. Wie hoch ist er?', '1000 / 50',
    TW('G = 50 cm², V = 1 000 cm³.', 'Höhe.', 'V = G · h ⇒ h = V : G.', 'h = 1 000 : 50 = 20 cm.', 'Der Karton ist 20 cm hoch.'), 'Welche Rechnung macht „mal G“ rückgängig?', einheit='cm'))
TX.u('prisma_umstellen', 'pruefung', TZ('Ein Sandkasten ist 1,5 m lang und 1,2 m breit. Der Spielsand soll 20 cm hoch liegen. Ein Sack enthält 25 l Sand. Wie viele Säcke muss man kaufen?', '-(-(15 * 12 * 2) // 25)',
    TW('1,5 m · 1,2 m, Höhe 0,2 m, Sack 25 l.', 'Anzahl der Säcke.', 'Volumen in dm³ (= l), durch 25, aufrunden.', 'V = 15 dm · 12 dm · 2 dm = 360 l. 360 : 25 = 14,4.', 'Man muss 15 Säcke kaufen.'), 'Rechne alle Maße in dm um: 1 dm³ = 1 l.'), huerde='deuten')
TX.u('prisma_umstellen', 'begruenden', TX.A('In ein 45 cm hohes Aquarium mit 80 cm × 35 cm Grundfläche werden 112 l Wasser gefüllt. Die Fische brauchen mindestens 40 cm Wasserhöhe. Reicht das Wasser?',
    'Ja, das Wasser steht genau 40 cm hoch.', ['Nein, es steht nur 35 cm hoch.', 'Ja, es steht 45 cm hoch.', 'Nein, 112 l sind weniger als 40 cm.'],
    TW('G = 80 cm · 35 cm, V = 112 l, Bedingung h ≥ 40 cm.', 'Wasserhöhe und Entscheidung.', 'h = V : G, mit V in cm³.', 'G = 2 800 cm². h = 112 000 : 2 800 = 40 cm.', 'Es reicht genau: Das Wasser steht 40 cm hoch.'),
    'Rechne die Wasserhöhe aus und vergleiche mit 40 cm.'), huerde='entscheidung')

# --- zylinder_volumen ---
TX.u('zylinder_volumen', 'pruefung', TZ('Ein zylinderförmiger Wasserkocher hat innen 8 cm Radius. Er hat 1 800 Watt, das Wasser steht 9 cm hoch. Wie viele Liter Wasser sind darin? Runde auf zwei Nachkommastellen.', f'{PI} * 8**2 * 9 / 1000',
    TW('r = 8 cm, Wasserhöhe 9 cm. Die Leistung spielt keine Rolle.', 'Wassermenge in Litern.', 'V = π · r² · h, 1 l = 1 000 cm³.', 'V = π · 64 · 9 ≈ 1 809,6 cm³ ≈ 1,81 l.', 'Im Kocher sind etwa 1,81 l Wasser.'),
    'Welche Höhe zählt – die des Kochers oder die des Wassers?', einheit='l', toleranz=0.01), huerde='ueberfluessig')

# --- zylinder_oberflaeche ---
TX.u('zylinder_oberflaeche', 'direkt', TZ('Eine Dose hat 3 cm Radius und ist 10 cm hoch. Ein Etikett bedeckt genau den Mantel. Wie viel cm² Papier braucht man? Runde auf ganze cm².', f'2 * {PI} * 3 * 10',
    TW('r = 3 cm, h = 10 cm.', 'Mantelfläche.', 'M = 2 · π · r · h.', 'M = 2 · π · 3 · 10 ≈ 188,5 cm².', 'Das Etikett hat etwa 188 cm².'), 'Das Etikett ist der Mantel – Umfang mal Höhe.', einheit='cm²', toleranz=1))
TX.u('zylinder_oberflaeche', 'transfer', TZ('Eine Küchenrolle hat innen eine Papprolle, 25 cm lang mit 4 cm Durchmesser, an beiden Enden offen. Wie viel cm² Pappe hat die Rolle? Runde auf ganze cm².', f'{PI} * 4 * 25',
    TW('d = 4 cm, Länge 25 cm, offen.', 'Pappfläche.', 'Nur der Mantel, keine Kreise: M = π · d · h.', 'M = π · 4 · 25 ≈ 314 cm².', 'Die Rolle hat etwa 314 cm² Pappe.'), 'Welche Teile eines Zylinders hat die Rolle gar nicht?', einheit='cm²', toleranz=1), huerde='fehlend')
TX.u('zylinder_oberflaeche', 'pruefung', TZ('Für 500 Konservendosen (r = 4 cm, h = 11 cm, mit Boden und Deckel) wird Blech bestellt. Blech wird nur in ganzen m² verkauft. Wie viele m² muss man bestellen?',
    f'-(-(500 * (2 * {PI} * 4**2 + 2 * {PI} * 4 * 11)) // 10000)', TW('r = 4 cm, h = 11 cm, 500 Stück, ganze m².', 'zu bestellende m².', 'O = 2πr² + 2πrh, · 500, in m² (1 m² = 10 000 cm²), aufrunden.',
    'O ≈ 100,5 + 276,5 = 377 cm². 500 · 377 ≈ 188 500 cm² ≈ 18,85 m².', 'Man muss 19 m² bestellen.'), 'Erst eine Dose, dann alle; und wie viele ganze m² reichen?'), huerde='deuten')

# --- verstehen ---
TX.u('verstehen', 'direkt', TZ('Ein Paket ist ein Quader. Ein zweites Paket ist genauso lang und breit, aber doppelt so hoch. Wie viel Mal so viel passt in das zweite Paket?', '2',
    TW('Länge und Breite gleich, Höhe · 2.', 'Faktor des Volumens.', 'V = G · h, G bleibt gleich.', 'Faktor 2.', 'Es passt doppelt so viel hinein.'), 'Was ändert sich an V = G · h?'))
TX.u('verstehen', 'einkleidung', TZ('Ein Hersteller macht seine würfelförmigen Zuckerstücke größer: Jede Kante wird doppelt so lang. Wie viel Mal so viel Zucker steckt in einem neuen Stück?', '2**3',
    TW('Kante · 2.', 'Faktor des Volumens.', 'Alle drei Längen werden verdoppelt.', '2 · 2 · 2 = 8.', 'Ein neues Stück enthält 8-mal so viel Zucker.'), 'Wie viele Längen eines Würfels werden verdoppelt?'))
TX.u('verstehen', 'umkehr', TZ('Ein zylinderförmiger Becher soll bei gleicher Höhe 4-mal so viel fassen. Mit welcher Zahl muss man seinen Radius malnehmen?', '2',
    TW('h gleich, V · 4.', 'Faktor des Radius.', 'V = π · r² · h: Der Radius zählt im Quadrat, k² = 4.', 'k = 2.', 'Der Radius muss doppelt so groß werden.'), 'Welche Zahl ergibt im Quadrat 4?'))
TX.u('verstehen', 'pruefung', TZ('Eine Litfaßsäule wird im Maßstab 1 : 20 als Modell gebaut. Für den Mantel des Modells braucht man 6 ml Farbe. Farbe gibt es in 1-l-Dosen. Wie viele Dosen braucht man für die echte Säule?', '-(-(6 * 20**2) // 1000)',
    TW('Maßstab 1 : 20, Modell 6 ml, Dosen zu 1 l.', 'Anzahl der Dosen.', 'Flächen wachsen mit 20² = 400; dann in l umrechnen und aufrunden.', '6 ml · 400 = 2 400 ml = 2,4 l.', 'Man braucht 3 Dosen.'),
    'Farbe hängt von der Fläche ab – mit welchem Faktor wächst eine Fläche?'), huerde='deuten')
TX.u('verstehen', 'rueckwaerts', TZ('Ein würfelförmiger Eiswürfel hat 27 cm³. Eine neue Form soll Würfel mit 8-mal so viel Volumen machen. Wie lang ist eine Kante des neuen Eiswürfels?', '3 * 2',
    TW('V alt = 27 cm³, V neu = 8 · V alt.', 'Kante des neuen Würfels.', 'Alte Kante a mit a · a · a = 27 suchen; Volumenfaktor 8 = 2 · 2 · 2, also Kante · 2.', 'a alt = 3 cm (3 · 3 · 3 = 27). a neu = 3 · 2 = 6 cm.', 'Die neue Kante ist 6 cm lang.'),
    'Welche Kante hat ein Würfel mit 27 cm³?', einheit='cm'), huerde='fehlend')
TX.s('verstehen', TZ('Ein Aquarium wird in Länge, Breite und Höhe verdoppelt. Wie viel Mal so viel Wasser passt hinein?', '2**3',
    TW('Alle drei Maße · 2.', 'Faktor des Volumens.', 'Jede Länge zählt einmal mit.', '2 · 2 · 2 = 8.', 'Es passt 8-mal so viel Wasser hinein.')))
TX.s('verstehen', TZ('Ein Rohr wird bei gleicher Länge mit doppeltem Innenradius gebaut. Wie viel Mal so viel Wasser passt hinein?', '2**2',
    TW('Länge gleich, r · 2.', 'Faktor des Volumens.', 'V = π · r² · h: r zählt im Quadrat.', '2² = 4.', 'Es passt 4-mal so viel Wasser hinein.')))
TX.k('verstehen', TZ('Ein Karton wird in Länge, Breite und Höhe dreimal so groß gebaut. Wie viel Mal so viel Pappe braucht man?', '3**2',
    TW('Alle Maße · 3.', 'Faktor der Oberfläche.', 'Flächen wachsen mit dem Quadrat.', '3² = 9.', 'Man braucht 9-mal so viel Pappe.')))

_datei_stufen = datei
def datei():
    d, anz = _datei_stufen()
    text_auf_datei(TX, d)
    return d, anz
# ---- TEXT ENDE ----

if __name__ == '__main__':
    d_, anz = datei()
    schreiben(ZIEL, d_, anz)


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('messen.prisma_zylinder')
# ---- BEREINIGEN ENDE ----

# ---- LK (22.11., Nachtrag LK-D 2, siehe _lk_etappen_2211.py): zuletzt, hängt nur an ----
if __name__ == '__main__':
    from _lk_etappen_2211 import lk_anhaengen
    lk_anhaengen('messen.prisma_zylinder')
# ---- LK ENDE ----

# ---- NT-D (22.11., siehe _nt_2211.py): zuletzt, hängt nur Aufgaben an ----
if __name__ == '__main__':
    from _nt_2211 import nt_anhaengen
    nt_anhaengen('messen.prisma_zylinder')
# ---- NT ENDE ----
