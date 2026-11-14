#!/usr/bin/env python3
"""Thema abbildungen.aehnlichkeit – Ähnlichkeit und Strahlensätze (Klasse 9)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import *  # noqa: E402,F403

start(909)
FIG = ('Zwei Strahlen mit gemeinsamem Anfangspunkt S werden von zwei parallelen Geraden geschnitten: '
       'die erste Parallele schneidet in A und B, die zweite in A\' und B\' (A, A\' auf dem einen, B, B\' auf dem anderen Strahl; A liegt näher an S).')


def dec(lo, hi, nd=1):
    """zufällige Dezimalzahl mit nd Nachkommastellen"""
    f = 10 ** nd
    return Fr(R.randint(int(lo * f), int(hi * f)), f)


def ok(*xs):
    return all(endlich(x) and Fr(x).denominator in (1, 2, 4, 5, 10, 20, 25, 50, 100) for x in xs)


def cf(x):
    return str(float(x)) if Fr(x).denominator != 1 else str(int(x))


ETAPPEN = [
    {'lernziel': 'streckung', 'titel': 'Zentrische Streckung',
     'regel': 'Bei einer zentrischen Streckung mit Zentrum Z und ⟦Streckfaktor k⟧ gilt ⟦ZP\' = |k| · ZP⟧; alle Strecken werden mit |k| multipliziert. Bei k < 0 liegt P\' auf der ⟦anderen Seite⟧ von Z.',
     'schritte': ['Z(1 | 2), P(4 | 3), k = 2: Vektor von Z nach P ist (3 | 1).', 'Verdoppeln: (6 | 2), also P\' = (1 + 6 | 2 + 2) = ⟦P\'(7 | 4)⟧.'],
     'probe': 'P\' liegt auf dem Strahl ZP, doppelt so weit von Z entfernt ✓',
     'fehler': 'P\' = 2 · P = (8 | 6) ist falsch, wenn Z nicht der Ursprung ist: Man streckt den ⟦Abstand von Z⟧, nicht die Koordinaten von P.'},
    {'lernziel': 'aehnlich', 'titel': 'Ähnliche Figuren',
     'regel': 'Zwei Figuren sind ⟦ähnlich⟧, wenn entsprechende Winkel gleich sind und ⟦alle Seiten im gleichen Verhältnis k⟧ stehen. Für Dreiecke genügen zwei gleiche Winkel.',
     'schritte': ['Dreieck 1: 4 cm, 6 cm, 7 cm. Dreieck 2 ist ähnlich, die kürzeste Seite misst 10 cm: k = 10 : 4 = 2,5.', 'Die anderen Seiten: 6 · 2,5 = ⟦15 cm⟧ und 7 · 2,5 = ⟦17,5 cm⟧.'],
     'probe': '15 : 6 = 2,5 ✓',
     'fehler': 'Zu jeder Seite 6 cm zu addieren (4 → 10, 6 → 12) ist falsch: Bei Ähnlichkeit wird ⟦multipliziert⟧, nicht addiert.'},
    {'lernziel': 'strahlensatz1', 'titel': '1. Strahlensatz (Abschnitte)',
     'regel': 'Werden zwei Strahlen von Parallelen geschnitten, stehen die ⟦Abschnitte auf einem Strahl⟧ im gleichen Verhältnis wie die entsprechenden auf dem anderen: ⟦SA : SA\' = SB : SB\'⟧.',
     'schritte': ['SA = 3 cm, SA\' = 7,5 cm, SB = 4 cm. Gesucht SB\'.', 'SB\' : 4 = 7,5 : 3 = 2,5 ⇒ ⟦SB\' = 10 cm⟧.'],
     'probe': '10 : 4 = 2,5 = 7,5 : 3 ✓',
     'fehler': 'SB\' = SB + (SA\' − SA) = 8,5 cm ist falsch: Die Strecken stehen im gleichen ⟦Verhältnis⟧, nicht im gleichen Abstand.'},
    {'lernziel': 'strahlensatz2', 'titel': '2. Strahlensatz (Parallelen)',
     'regel': 'Die ⟦Parallelstrecken⟧ verhalten sich wie die zugehörigen Abschnitte ⟦ab S⟧: ⟦AB : A\'B\' = SA : SA\'⟧. Nicht mit dem Stück AA\' zwischen den Parallelen rechnen!',
     'schritte': ['SA = 5 cm, AA\' = 3 cm, AB = 4 cm. Gesucht A\'B\'. SA\' = 5 + 3 = 8 cm.', 'A\'B\' : 4 = 8 : 5 ⇒ A\'B\' = 4 · 1,6 = ⟦6,4 cm⟧.'],
     'probe': '6,4 : 4 = 1,6 = 8 : 5 ✓',
     'fehler': 'A\'B\' : AB = AA\' : SA zu rechnen ist falsch: Beim 2. Strahlensatz braucht man Strecken ⟦ab S⟧, also SA\' = SA + AA\'.'},
    {'lernziel': 'flaeche_volumen', 'titel': 'Wirkung auf Fläche und Volumen',
     'regel': 'Werden alle Längen mit k multipliziert, wird der ⟦Flächeninhalt mit k²⟧ und das ⟦Volumen mit k³⟧ multipliziert.',
     'schritte': ['Ein Modell im Maßstab 1 : 20: k = 20. Das Modell hat 300 cm² Bodenfläche.', 'Original: 300 · 20² = 300 · 400 = ⟦120 000 cm²⟧ = 12 m².'],
     'probe': '1 m² = 10 000 cm² ✓',
     'fehler': 'Bei doppelter Seitenlänge auch die doppelte Fläche anzunehmen ist falsch: Die Fläche wächst mit ⟦k² = 4⟧, das Volumen mit k³ = 8.'},
    {'lernziel': 'anwendung', 'titel': 'Strahlensätze anwenden',
     'regel': 'Skizze anfertigen, ⟦Scheitel S und Parallelen⟧ erkennen, Gleichung aufstellen. Steht die Unbekannte in einer Summe, entsteht eine ⟦Bruchgleichung⟧: mit den Nennern multiplizieren.',
     'schritte': ['Ein 2 m hoher Stab wirft 3 m Schatten, ein Baum zur gleichen Zeit 18 m. Strahlen: Sonnenstrahl und Boden, S = Schattenende.', 'h : 2 = 18 : 3 ⇒ h = 2 · 6 = ⟦12 m⟧.'],
     'probe': '12 : 18 = 2 : 3 ✓',
     'fehler': 'h : 18 = 3 : 2 ist falsch zugeordnet: ⟦Höhe zu Höhe⟧ und ⟦Schatten zu Schatten⟧ (oder Höhe zu Schatten auf beiden Seiten gleich).'},
]


def g_streckung(s):
    if s == 1:
        k = R.choice([2, 3, 4, Fr(1, 2), Fr(3, 2), Fr(5, 2)])
        l = Fr(R.randint(2, 20))
        b = k * l
        if not ok(b): return None
        return zahl(f'Eine Strecke der Länge {dz(l)} cm wird zentrisch mit k = {dz(k)} gestreckt. Wie lang ist die Bildstrecke?',
                    f'Bildstrecke = |k| · Strecke = {dz(k)} · {dz(l)} cm = {dz(b)} cm.', 'Alle Längen werden mit |k| multipliziert.', b,
                    f'{cf(k)} * {cf(l)}', einheit='cm')
    if s == 2:
        if R.random() < 0.5:
            zp = Fr(R.randint(2, 12))
            k = R.choice([Fr(3, 2), Fr(5, 2), 2, 3, Fr(1, 2), Fr(1, 4)])
            zpb = zp * k
            if not ok(zpb, k): return None
            return zahl(f'Bei einer zentrischen Streckung mit Zentrum Z ist ZP = {dz(zp)} cm und ZP\' = {dz(zpb)} cm (P\' auf dem Strahl ZP). Bestimme k.',
                        f'k = ZP\' : ZP = {dz(zpb)} : {dz(zp)} = {dz(k)}.', 'Teile die Bildlänge durch die Originallänge.', k, f'{cf(zpb)} / {cf(zp)}')
        k = R.choice([2, 3, -1, -2])
        z = (R.randint(-3, 3), R.randint(-3, 3))
        p = (z[0] + R.randint(-4, 4), z[1] + R.randint(-4, 4))
        if p == z: return None
    else:
        k = R.choice([-2, -3, Fr(-1, 2), Fr(3, 2), Fr(1, 2)])
        z = (R.randint(-4, 4), R.randint(-4, 4))
        p = (z[0] + 2 * R.randint(-3, 3), z[1] + 2 * R.randint(-3, 3))
        if p == z: return None
    q = (z[0] + k * (p[0] - z[0]), z[1] + k * (p[1] - z[1]))
    if any(Fr(c).denominator != 1 for c in q): return None
    return luecken(f'Strecke P({p[0]} | {p[1]}) zentrisch an Z({z[0]} | {z[1]}) mit k = {dz(k)}.'.replace('-', '−'), "P'(□ | □)", 'x- und y-Koordinate',
                   [q[0], q[1]], f'Von Z nach P: ({dz(p[0] - z[0])} | {dz(p[1] - z[1])}); mal {dz(k)}: ({dz(k * (p[0] - z[0]))} | {dz(k * (p[1] - z[1]))}); P\'({dz(q[0])} | {dz(q[1])}).',
                   'Bestimme den Weg von Z nach P, multipliziere mit k und gehe ihn von Z aus.',
                   c=[f'{z[0]} + {cf(k)} * ({p[0]} - ({z[0]}))', f'{z[1]} + {cf(k)} * ({p[1]} - ({z[1]}))'])


def g_aehnlich(s):
    if s == 1:
        a, b = R.randint(2, 9), R.randint(3, 12)
        k = R.choice([2, 3, Fr(3, 2), Fr(5, 2), 4])
        if not ok(k * b): return None
        return zahl(f'Zwei Dreiecke sind ähnlich mit k = {dz(k)}. Eine Seite des kleinen Dreiecks ist {b} cm lang. Wie lang ist die entsprechende Seite des großen?',
                    f'{b} cm · {dz(k)} = {dz(k * b)} cm.', 'Entsprechende Seiten: mit k multiplizieren.', k * b, f'{b} * {cf(k)}', einheit='cm')
    if s == 2:
        a, b, c = sorted(R.sample(range(3, 13), 3))
        if a + b <= c: return None
        k = R.choice([Fr(3, 2), 2, Fr(5, 2), 3, Fr(5, 4)])
        a2 = k * a
        welche = R.choice([b, c])
        if not ok(a2, k * welche): return None
        return zahl(f'Ein Dreieck hat die Seiten {a} cm, {b} cm und {c} cm. In einem ähnlichen Dreieck ist die kürzeste Seite {dz(a2)} cm lang. Wie lang ist die Seite, die {welche} cm entspricht?',
                    f'k = {dz(a2)} : {a} = {dz(k)}; {welche} · {dz(k)} = {dz(k * welche)} cm.', 'Bestimme zuerst k aus den kürzesten Seiten.', k * welche,
                    f'{welche} * ({cf(a2)} / {a})', einheit='cm')
    typ = R.random()
    if typ < 0.5:
        a, b, c = sorted(R.sample(range(3, 13), 3))
        if a + b <= c: return None
        k = R.choice([2, 3, Fr(3, 2)])
        aehn = R.random() < 0.5
        d = 0 if aehn else R.choice([1, 2])
        s2 = (k * a, k * b, k * c + d)
        r = 'ja' if aehn else 'nein'
        return auswahl(f'Dreieck 1: {a} cm, {b} cm, {c} cm. Dreieck 2: {dz(s2[0])} cm, {dz(s2[1])} cm, {dz(s2[2])} cm. Sind sie ähnlich?',
                       f'{"Ja" if aehn else "Nein"}, {"alle" if aehn else "nicht alle"} Seitenverhältnisse sind gleich.',
                       ['Ja, alle Seitenverhältnisse sind gleich.', 'Nein, nicht alle Seitenverhältnisse sind gleich.',
                        'Ja, weil beide Dreiecke drei Seiten haben.', 'Nein, weil die Seiten verschieden lang sind.'],
                       f'{dz(s2[0])} : {a} = {dz(k)}, {dz(s2[1])} : {b} = {dz(k)}, {dz(s2[2])} : {c} = {dz(s2[2] / c) if ok(s2[2] / c) else br(s2[2] / c)}{" – gleich" if aehn else " – verschieden"}.',
                       'Bilde die Verhältnisse entsprechender Seiten (kurz zu kurz, lang zu lang).')
    al, be = R.randint(25, 80), R.randint(25, 80)
    ga = 180 - al - be
    if ga <= 10: return None
    aehn = R.random() < 0.5
    if aehn:
        w2 = (be, ga)
    else:
        w2 = (be, ga + R.choice([-5, 5, 10]))
        if 180 - sum(w2) <= 0: return None
        if sorted([al, be, ga]) == sorted([w2[0], w2[1], 180 - sum(w2)]): return None
    return auswahl(f'Dreieck 1 hat die Winkel {al}° und {be}°. Dreieck 2 hat die Winkel {w2[0]}° und {w2[1]}°. Sind die Dreiecke ähnlich?',
                   f'{"Ja" if aehn else "Nein"}: Der dritte Winkel ist {180 - w2[0] - w2[1]}°{"." if aehn else ", die Winkel stimmen nicht überein."}',
                   [f'{"Nein" if aehn else "Ja"}: Der dritte Winkel ist {180 - w2[0] - w2[1]}°.', 'Das kann man ohne Seitenlängen nicht entscheiden.',
                    'Ja, alle Dreiecke mit spitzen Winkeln sind ähnlich.'],
                   f'Dreieck 1: dritter Winkel {ga}°. Dreieck 2: {180 - w2[0] - w2[1]}°. {"Alle drei Winkel stimmen überein" if aehn else "Die Winkel stimmen nicht überein"}.',
                   'Berechne jeweils den dritten Winkel mit der Winkelsumme 180°.')


def g_strahlensatz1(s):
    sa = Fr(R.randint(2, 9))
    k = R.choice([Fr(3, 2), 2, Fr(5, 2), 3, Fr(5, 4), Fr(7, 4)])
    sb = Fr(R.randint(2, 10))
    sa2, sb2 = k * sa, k * sb
    if not ok(sa2, sb2): return None
    if s == 1:
        return zahl(f'{FIG} SA = {dz(sa)} cm, SA\' = {dz(sa2)} cm, SB = {dz(sb)} cm. Berechne SB\'.',
                    f'SB\' : SB = SA\' : SA = {dz(k)} ⇒ SB\' = {dz(sb)} · {dz(k)} = {dz(sb2)} cm.', 'Setze das Verhältnis auf beiden Strahlen gleich.', sb2,
                    f'{cf(sb)} * {cf(sa2)} / {cf(sa)}', einheit='cm')
    if s == 2:
        return zahl(f'{FIG} SA = {dz(sa)} cm, SB = {dz(sb)} cm, SB\' = {dz(sb2)} cm. Berechne SA\'.',
                    f'SA\' : SA = SB\' : SB = {dz(k)} ⇒ SA\' = {dz(sa)} · {dz(k)} = {dz(sa2)} cm.', 'Welches Verhältnis kennst du vollständig?', sa2,
                    f'{cf(sa)} * {cf(sb2)} / {cf(sb)}', einheit='cm')
    aa = sa2 - sa
    bb = sb2 - sb
    if R.random() < 0.5:
        return zahl(f'{FIG} SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, SB = {dz(sb)} cm. Berechne BB\'.',
                    f'Auch die Abschnitte zwischen den Parallelen stehen im gleichen Verhältnis: BB\' : SB = AA\' : SA ⇒ BB\' = {dz(sb)} · {dz(aa)} : {dz(sa)} = {dz(bb)} cm.',
                    'Der 1. Strahlensatz gilt auch für die Teilstücke AA\' und BB\'.', bb, f'{cf(sb)} * {cf(aa)} / {cf(sa)}', einheit='cm')
    return zahl(f'{FIG} SA\' = {dz(sa2)} cm, AA\' = {dz(aa)} cm, SB\' = {dz(sb2)} cm. Berechne SB.',
                f'SA = {dz(sa2)} − {dz(aa)} = {dz(sa)} cm. SB = SB\' · SA : SA\' = {dz(sb)} cm.', 'Berechne zuerst SA.', sb,
                f'{cf(sb2)} * ({cf(sa2)} - {cf(aa)}) / {cf(sa2)}', einheit='cm')


def g_strahlensatz2(s):
    sa = Fr(R.randint(2, 9))
    k = R.choice([Fr(3, 2), 2, Fr(5, 2), 3, Fr(5, 4), Fr(8, 5)])
    ab = Fr(R.randint(2, 10))
    sa2, ab2 = k * sa, k * ab
    if not ok(sa2, ab2): return None
    aa = sa2 - sa
    if s == 1:
        return zahl(f'{FIG} SA = {dz(sa)} cm, SA\' = {dz(sa2)} cm, AB = {dz(ab)} cm. Berechne A\'B\'.',
                    f'A\'B\' : AB = SA\' : SA = {dz(k)} ⇒ A\'B\' = {dz(ab)} · {dz(k)} = {dz(ab2)} cm.', 'Parallelstrecken verhalten sich wie die Abschnitte ab S.',
                    ab2, f'{cf(ab)} * {cf(sa2)} / {cf(sa)}', einheit='cm')
    if s == 2:
        if R.random() < 0.5:
            return zahl(f'{FIG} SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, AB = {dz(ab)} cm. Berechne A\'B\'.',
                        f'SA\' = {dz(sa)} + {dz(aa)} = {dz(sa2)} cm. A\'B\' = {dz(ab)} · {dz(sa2)} : {dz(sa)} = {dz(ab2)} cm.',
                        'Rechne mit SA\' (ab S), nicht mit AA\'.', ab2, f'{cf(ab)} * ({cf(sa)} + {cf(aa)}) / {cf(sa)}', einheit='cm')
        return zahl(f'{FIG} AB = {dz(ab)} cm, A\'B\' = {dz(ab2)} cm, SA\' = {dz(sa2)} cm. Berechne SA.',
                    f'SA : SA\' = AB : A\'B\' ⇒ SA = {dz(sa2)} · {dz(ab)} : {dz(ab2)} = {dz(sa)} cm.', 'Stelle das Verhältnis mit der Unbekannten auf.', sa,
                    f'{cf(sa2)} * {cf(ab)} / {cf(ab2)}', einheit='cm')
    if R.random() < 0.5:
        falsch = ab * aa / sa
        if not ok(falsch) or falsch == ab2: return None
        return auswahl(f'{FIG} SA = {dz(sa)} cm, AA\' = {dz(aa)} cm, AB = {dz(ab)} cm. Jemand rechnet A\'B\' = {dz(ab)} · {dz(aa)} : {dz(sa)} = {dz(falsch)} cm. Was stimmt?',
                       f'Falsch: Man braucht SA\' = {dz(sa2)} cm, also A\'B\' = {dz(ab2)} cm.',
                       ['Richtig.', f'Falsch: A\'B\' = {dz(ab + aa)} cm.', f'Falsch: A\'B\' = {dz(ab * sa / sa2) if ok(ab * sa / sa2) else br(ab * sa / sa2)} cm.'],
                       f'Beim 2. Strahlensatz stehen die Parallelen im Verhältnis der Abschnitte ab S: A\'B\' = {dz(ab)} · {dz(sa2)} : {dz(sa)} = {dz(ab2)} cm.',
                       'Welche Strecken gehören beim 2. Strahlensatz zusammen?')
    # Bruchgleichung: AA' gesucht
    return zahl(f'{FIG} SA = {dz(sa)} cm, AB = {dz(ab)} cm, A\'B\' = {dz(ab2)} cm. Berechne AA\'.',
                f'(SA + x) : SA = A\'B\' : AB ⇒ ({dz(sa)} + x) : {dz(sa)} = {dz(k)} ⇒ x = {dz(sa)} · {dz(k)} − {dz(sa)} = {dz(aa)} cm.',
                'Nenne AA\' = x; dann ist SA\' = SA + x.', aa, f'{cf(sa)} * {cf(ab2)} / {cf(ab)} - {cf(sa)}', einheit='cm')


def g_flaeche_volumen(s):
    if s == 1:
        k = R.randint(2, 5)
        A = R.randint(2, 30)
        return zahl(f'Alle Längen einer Figur werden mit {k} multipliziert. Die Figur hatte {A} cm² Flächeninhalt. Wie groß ist er jetzt?',
                    f'Fläche · k² = {A} · {k * k} = {dz(A * k * k)} cm².', 'Fläche wächst mit dem Quadrat des Streckfaktors.', A * k * k, f'{A} * {k} ** 2', einheit='cm²')
    if s == 2:
        typ = R.random()
        if typ < 0.4:
            k = R.choice([2, 3, Fr(1, 2), Fr(3, 2)])
            V = R.choice([8, 16, 24, 40, 80])
            v2 = V * Fr(k) ** 3
            if not ok(v2): return None
            return zahl(f'Ein Körper hat {V} cm³ Volumen. Alle Kanten werden mit k = {dz(k)} multipliziert. Wie groß ist das neue Volumen?',
                        f'Volumen · k³ = {V} · {dz(Fr(k) ** 3)} = {dz(v2)} cm³.', 'Volumen wächst mit k³.', v2, f'{V} * {cf(k)} ** 3', einheit='cm³')
        if typ < 0.7:
            k = R.randint(2, 6)
            return zahl(f'Eine Figur wird so vergrößert, dass ihr Flächeninhalt {k * k}-mal so groß ist. Mit welchem Faktor wurden die Längen multipliziert?',
                        f'k² = {k * k} ⇒ k = {k}.', 'Fläche: k². Rückwärts: Wurzel ziehen.', k, f'{k * k} / {k}')
        k = R.randint(2, 4)
        return zahl(f'Ein Würfel wird so vergrößert, dass sein Volumen {k ** 3}-mal so groß ist. Wie oft so groß ist seine Oberfläche?',
                    f'k³ = {k ** 3} ⇒ k = {k}; Oberfläche · k² = {k * k}-mal so groß.', 'Bestimme zuerst k aus dem Volumen.', k * k, f'({k ** 3} / {k} ** 2) ** 2')
    m = R.choice([10, 20, 25, 50, 100])
    A = R.choice([2, 3, 4, 6, 8, 12])
    typ = R.random()
    if typ < 0.5:
        orig = A * m * m
        return zahl(f'Ein Modell im Maßstab 1 : {m} hat eine Grundfläche von {A} cm². Wie groß ist die Grundfläche des Originals in m²?',
                    f'{A} cm² · {m}² = {dz(orig)} cm² = {dz(Fr(orig, 10000))} m².', 'Fläche · k², dann cm² in m² umrechnen (1 m² = 10 000 cm²).',
                    Fr(orig, 10000), f'{A} * {m} ** 2 / 10000', einheit='m²')
    V = R.choice([1, 2, 3, 4, 5])
    m = R.choice([10, 20, 50])
    orig = V * m ** 3
    return zahl(f'Ein Modell im Maßstab 1 : {m} hat {V} cm³ Volumen. Wie groß ist das Volumen des Originals in m³?',
                f'{V} cm³ · {m}³ = {dz(orig)} cm³ = {dz(Fr(orig, 10 ** 6))} m³.', 'Volumen · k³, dann cm³ in m³ (1 m³ = 1 000 000 cm³).',
                Fr(orig, 10 ** 6), f'{V} * {m} ** 3 / 1000000', einheit='m³')


def g_anwendung(s):
    typ = R.random()
    if s == 1 or (s == 2 and typ < 0.4):
        st, sch = R.choice([(1, 2), (2, 3), (Fr(3, 2), 2), (1, Fr(5, 4)), (2, 5), (Fr(1, 2), 1)])
        k = R.randint(3, 15)
        sch2 = sch * k
        h = st * k
        if not ok(h, sch2): return None
        ding = R.choice(['ein Baum', 'ein Turm', 'ein Mast', 'ein Haus'])
        return zahl(f'Ein {dz(st)} m langer Stab wirft einen {dz(sch)} m langen Schatten. Zur gleichen Zeit wirft {ding} einen {dz(sch2)} m langen Schatten. Wie hoch ist er?',
                    f'h : {dz(st)} = {dz(sch2)} : {dz(sch)} ⇒ h = {dz(st)} · {dz(k)} = {dz(h)} m.', 'Höhe zu Höhe wie Schatten zu Schatten.', h,
                    f'{cf(st)} * {cf(sch2)} / {cf(sch)}', einheit='m')
    if s == 2:
        a, b = R.randint(2, 12), R.randint(2, 12)
        k = R.choice([2, 3, Fr(3, 2), Fr(5, 2), 4])
        c = a * k - a
        x = b * (k - 1)
        if not ok(c, x): return None
        return zahl(f'Flussbreite messen: S, A und A\' liegen auf einer Geraden (A am diesseitigen, A\' am jenseitigen Ufer), B und B\' auf einer zweiten Geraden durch S, und AB ∥ A\'B\'. Gemessen: SA = {a} m, SB = {b} m, SB\' = {dz(b * k)} m. Wie breit ist der Fluss (AA\')?',
                    f'(SA + x) : SA = SB\' : SB ⇒ ({a} + x) : {a} = {dz(k)} ⇒ x = {dz(a * k)} − {a} = {dz(c)} m.',
                    'Stelle eine Verhältnisgleichung mit x in einer Summe auf.', c, f'{a} * {cf(b * k)} / {b} - {a}', einheit='m')
    if typ < 0.5:
        # Bruchgleichung x/(x + d) = p/q
        p, q = R.choice([(1, 2), (2, 3), (3, 4), (2, 5), (3, 5), (4, 7), (3, 7)])
        x = R.randint(2, 20) * p
        d = Fr(x * (q - p), p)
        if d.denominator != 1: return None
        return zahl(f'Bei einer Strahlensatzfigur ergibt sich die Gleichung x : (x + {dz(d)}) = {p} : {q}. Löse sie.',
                    f'{q}x = {p}(x + {dz(d)}) ⇒ {q - p}x = {dz(p * d)} ⇒ x = {dz(x)}.', 'Multipliziere über Kreuz (mit beiden Nennern) und löse die lineare Gleichung.',
                    x, f'{p} * {cf(d)} / ({q} - {p})')
    arm = R.choice([Fr(6, 10), Fr(65, 100), Fr(7, 10)])
    daumen = R.choice([Fr(2, 100), Fr(25, 1000), Fr(3, 100)])
    hb = R.choice([10, 15, 20, 25, 30, 40])
    e = hb * arm / daumen
    if not ok(e): return None
    return zahl(f'Mit ausgestrecktem Arm ({dz(arm)} m vom Auge) verdeckt ein {dz(daumen * 100)} cm breiter Daumen genau ein {hb} m hohes Gebäude. Wie weit ist das Gebäude entfernt?',
                f'e : {dz(arm)} = {hb} : {dz(daumen)} ⇒ e = {dz(arm)} · {hb} : {dz(daumen)} = {dz(e)} m.', 'S ist das Auge; Daumen und Gebäude sind die Parallelen.',
                e, f'{cf(arm)} * {hb} / {cf(daumen)}', einheit='m')


GEN = {'streckung': g_streckung, 'aehnlich': g_aehnlich, 'strahlensatz1': g_strahlensatz1, 'strahlensatz2': g_strahlensatz2,
       'flaeche_volumen': g_flaeche_volumen, 'anwendung': g_anwendung}

if __name__ == '__main__':
    bauen('abbildungen.aehnlichkeit',
          'Zentrische Streckung und Ähnlichkeit verstehen, Strahlensätze anwenden und die Wirkung auf Fläche und Volumen berechnen.',
          ['Zentrische Streckung: Längen · |k|, Flächen · k², Volumina · |k|³.', 'Ähnlich: gleiche Winkel, alle Seiten im gleichen Verhältnis.',
           '1. Strahlensatz: SA : SA\' = SB : SB\'.', '2. Strahlensatz: AB : A\'B\' = SA : SA\' (Strecken ab S!).'],
          [('Streckung und Ähnlichkeit', ['streckung', 'aehnlich']), ('Strahlensätze', ['strahlensatz1', 'strahlensatz2']),
           ('Anwenden', ['flaeche_volumen', 'anwendung'])],
          ETAPPEN, GEN,
          meiden={'streckung': ['P(4 | 3) zentrisch an Z(1 | 2) mit k = 2.'], 'strahlensatz1': ['SA = 3 cm, SA\' = 7,5 cm, SB = 4 cm'],
                  'strahlensatz2': ['SA = 5 cm, AA\' = 3 cm, AB = 4 cm'], 'anwendung': ['2 m langer Stab wirft einen 3 m langen Schatten. Zur gleichen Zeit wirft ein Baum einen 18']},
          offen=['Lernkarten „strahlensatz1“, „strahlensatz2“ und „anwendung“ brauchen Zeichnung: Strahlensatzfigur (zwei Strahlen von S, zwei Parallelen, Punkte A, B, A\', B\'). Bisher in jeder Aufgabe als Text beschrieben – das ist lang; eine Skizze würde die Aufgaben deutlich kürzer machen.',
                 'Lernkarte „streckung“: Zeichnung der zentrischen Streckung im Koordinatensystem wäre hilfreich. X-Figur (Parallelen auf verschiedenen Seiten von S) ist ohne Zeichnung nicht enthalten.'])
