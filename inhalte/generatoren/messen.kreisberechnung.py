#!/usr/bin/env python3
"""Thema messen.kreisberechnung – Kreisberechnungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import PI, PIF, A, Z, baue, cz, runde, sicher_rundbar, zt  # noqa: E402

META = {'thema_schluessel': 'messen.kreisberechnung', 'thema_id': 51, 'block_id': 84, 'klasse': {'gym_by': 8, 'rs_by': 9}}
RUNDE = 'Runde auf eine Nachkommastelle.'
TIPP_PI = 'Rechne mit der π-Taste und runde erst am Ende.'

ETAPPEN = [
    {'lernziel': 'umfang', 'titel': 'Kreisumfang berechnen',
     'regel': 'Der ⟦Umfang⟧ eines Kreises ist etwa 3,14-mal so lang wie sein Durchmesser. Diese Zahl heißt ⟦π⟧ (Pi). Es gilt ⟦u = π · d = 2 · π · r⟧.',
     'schritte': ['r = 4 cm', 'u = 2 · π · 4 cm = 8π cm', 'u ≈ ⟦25,1 cm⟧'],
     'fehler': 'u = π · r ist falsch: Man braucht den ⟦Durchmesser⟧ (d = 2r). Bei r = 4 cm ist u = π · 8 cm ≈ 25,1 cm, nicht 12,6 cm.',
     '_verbot': ['r = 4 cm']},
    {'lernziel': 'flaeche', 'titel': 'Flächeninhalt eines Kreises',
     'regel': 'Der ⟦Flächeninhalt⟧ eines Kreises ist ⟦A = π · r²⟧. Zuerst r quadrieren, dann mit π multiplizieren.',
     'schritte': ['d = 10 cm, also r = 5 cm', 'A = π · 5² cm² = 25π cm²', 'A ≈ ⟦78,5 cm²⟧'],
     'fehler': 'A = π · d² ist falsch: In die Formel gehört der ⟦Radius⟧. Mit d = 10 cm käme 314 cm² heraus – viermal zu viel.',
     '_verbot': ['d = 10 cm']},
    {'lernziel': 'exakt', 'titel': 'Exakt rechnen mit π',
     'regel': 'Statt zu runden, kannst du Ergebnisse ⟦exakt als Vielfaches von π⟧ angeben, z. B. A = 16π cm². Das ist genauer und oft einfacher zu rechnen.',
     'schritte': ['r = 3 cm', 'u = 2 · π · 3 = ⟦6π cm⟧', 'A = π · 3² = ⟦9π cm²⟧'],
     'fehler': 'Bei r = 3 ist A nicht 6π: Dann hätte man 2 · 3 statt ⟦3²⟧ gerechnet. Das ist der Umfang, nicht die Fläche.',
     '_verbot': ['r = 3 cm']},
    {'lernziel': 'sektor', 'titel': 'Kreisausschnitt: Bogen und Fläche',
     'regel': 'Ein ⟦Kreisausschnitt⟧ mit Mittelpunktswinkel α ist der Anteil α/360° vom ganzen Kreis: ⟦Bogen b = α/360° · 2πr⟧, ⟦Fläche A = α/360° · πr²⟧.',
     'schritte': ['r = 6 cm, α = 120°: Anteil 120/360 = 1/3', 'b = 1/3 · 12π cm = 4π cm ≈ 12,6 cm', 'A = 1/3 · 36π cm² = ⟦12π cm² ≈ 37,7 cm²⟧'],
     'fehler': 'Der Anteil eines 90°-Ausschnitts ist nicht 90/100. Ein ganzer Kreis hat ⟦360°⟧: Der Anteil ist 90/360 = 1/4.',
     '_verbot': ['r = 6 cm, α = 120°']},
    {'lernziel': 'zusammengesetzt', 'titel': 'Kreisring und Kreisabschnitt',
     'regel': '⟦Kreisring⟧: großer Kreis minus kleiner Kreis, A = π · (R² − r²). ⟦Kreisabschnitt⟧ (Segment) bei 90°: Viertelkreis minus rechtwinkliges Dreieck, A = πr²/4 − r²/2.',
     'schritte': ['Ring: R = 5 cm, r = 3 cm', 'A = π · (25 − 9) cm² = 16π cm²', 'A ≈ ⟦50,3 cm²⟧'],
     'fehler': 'Beim Ring ist A nicht π · (5 − 3)² = 4π. Man muss erst ⟦jeden⟧ Radius quadrieren und dann subtrahieren: π · (25 − 9).',
     '_verbot': ['R = 5 cm, r = 3 cm']},
    {'lernziel': 'zylinder', 'titel': 'Zylinder: Volumen und Oberfläche',
     'regel': 'Ein Zylinder ist ein „rundes Prisma“: ⟦V = π · r² · h⟧ (Grundfläche mal Höhe). Mantel M = 2πr · h, Oberfläche ⟦O = 2πr² + 2πrh⟧.',
     'schritte': ['r = 2 cm, h = 10 cm', 'V = π · 4 · 10 cm³ = 40π cm³ ≈ 125,7 cm³', 'O = 2π · 4 + 2π · 2 · 10 = 48π cm² ≈ ⟦150,8 cm²⟧'],
     'fehler': 'Die Oberfläche ist nicht nur der Mantel 2πrh: Es fehlen ⟦Boden und Deckel⟧ (2 · πr²).',
     '_verbot': ['r = 2 cm, h = 10 cm']},
    {'lernziel': 'verstehen', 'titel': 'Wie ändern sich Umfang und Fläche?',
     'regel': 'Der Umfang wächst ⟦wie r⟧: doppelter Radius, doppelter Umfang. Die Fläche wächst ⟦wie r²⟧: doppelter Radius, ⟦vierfache⟧ Fläche.',
     'schritte': ['r = 2 cm: A = 4π cm². r = 6 cm (dreifach): A = 36π cm².', '36π : 4π = 9 = 3²', 'Dreifacher Radius → ⟦neunfache Fläche⟧'],
     'fehler': 'Doppelter Radius heißt nicht doppelte Fläche: π · (2r)² = π · 4r². Die Fläche wird ⟦vervierfacht⟧.'},
]


def rz(x, text, c, w, h, einheit):
    return Z(text, runde(x, 1), f'round({c}, 1)', w, h, einheit)


def ok(x): return sicher_rundbar(x, 1)


def z1(x):
    """Auf eine Nachkommastelle gerundet, immer mit einer Nachkommastelle geschrieben."""
    t = z1((x, 1))
    return t if ',' in t else t + ',0'


def zahl_r(R, st):
    if st == 1: return Fr(R.randint(1, 15))
    if st == 2: return Fr(R.randint(10, 150), 10) if R.random() < .5 else Fr(R.randint(2, 30))
    return Fr(R.randint(5, 250), 10)


def g_umfang(R, st):
    while True:
        r = zahl_r(R, st)
        u = 2 * PIF * r
        if ok(u) and ok(u / (2 * PIF)): break
    if st == 3 and R.random() < .5:
        u0 = runde(u, 1)
        r0 = u0 / (2 * PIF)
        if not ok(r0): return g_umfang(R, st)
        return rz(r0, f'Ein Kreis hat den Umfang {zt(u0)} cm. Berechne den Radius. {RUNDE}', f'{cz(u0)} / (2 * {PI})',
                  f'u = 2πr → r = u : (2π) = {zt(u0)} : (2π) ≈ {z1((r0, 1))} cm.', 'Stelle u = 2πr nach r um.', 'cm')
    if R.random() < .4:
        d = 2 * r
        return rz(PIF * d, f'Ein Kreis hat den Durchmesser {zt(d)} cm. Berechne den Umfang. {RUNDE}', f'{PI} * {cz(d)}',
                  f'u = π · d = π · {zt(d)} ≈ {z1((PIF * d, 1))} cm.', TIPP_PI, 'cm')
    kontext = R.choice(['', 'Ein Fahrradreifen', 'Ein runder Tisch', 'Eine Uhr']) if st >= 2 else ''
    text = f'{kontext} hat den Radius {zt(r)} cm. Wie lang ist der Umfang? {RUNDE}' if kontext else f'Berechne den Umfang eines Kreises mit r = {zt(r)} cm. {RUNDE}'
    return rz(u, text, f'2 * {PI} * {cz(r)}', f'u = 2 · π · {zt(r)} ≈ {z1((u, 1))} cm.', TIPP_PI, 'cm')


def g_flaeche(R, st):
    while True:
        r = zahl_r(R, st)
        a = PIF * r * r
        if ok(a): break
    if st == 3 and R.random() < .5:
        k = R.randint(2, 20)
        return Z(f'Ein Kreis hat den Flächeninhalt {k * k}π cm². Wie groß ist sein Radius?', k, f'{k * k} / {k}',
                 f'π · r² = {k * k}π → r² = {k * k} → r = {k} cm (denn {k} · {k} = {k * k}).', 'Teile durch π. Welche Zahl mal sich selbst ergibt den Rest?', 'cm')
    if R.random() < .4:
        d = 2 * r
        return rz(a, f'Ein Kreis hat den Durchmesser {zt(d)} cm. Berechne den Flächeninhalt. {RUNDE}', f'{PI} * ({cz(d)} / 2) ** 2',
                  f'r = {zt(d)} : 2 = {zt(r)} cm. A = π · {zt(r)}² ≈ {z1((a, 1))} cm².', 'Zuerst den Radius bestimmen.', 'cm²')
    return rz(a, f'Berechne den Flächeninhalt eines Kreises mit r = {zt(r)} cm. {RUNDE}', f'{PI} * {cz(r)} ** 2',
              f'A = π · {zt(r)}² = π · {zt(r * r)} ≈ {z1((a, 1))} cm².', 'Erst r² berechnen, dann mal π.', 'cm²')


def g_exakt(R, st):
    if st == 1:
        r = R.randint(1, 15)
        if R.random() < .5:
            return Z(f'Ein Kreis hat r = {r} cm. Gib den Umfang exakt an: u = □ · π cm. Welche Zahl gehört in das Kästchen?', 2 * r, f'2 * {r}',
                     f'u = 2 · π · {r} = {2 * r}π cm.', 'u = 2 · π · r. Rechne 2 · r.')
        return Z(f'Ein Kreis hat r = {r} cm. Gib den Flächeninhalt exakt an: A = □ · π cm². Welche Zahl gehört in das Kästchen?', r * r, f'{r} ** 2',
                 f'A = π · {r}² = {r * r}π cm².', 'A = π · r². Rechne r².')
    if st == 2:
        d = R.randint(2, 30)
        r = Fr(d, 2)
        if R.random() < .5:
            return Z(f'Ein Kreis hat den Durchmesser {d} cm. Gib den Flächeninhalt exakt an: A = □ · π cm². Welche Zahl gehört in das Kästchen?', r * r, f'({d} / 2) ** 2',
                     f'r = {zt(r)} cm. A = π · {zt(r)}² = {zt(r * r)}π cm².', 'Erst den Radius bestimmen, dann quadrieren.')
        k = R.randint(2, 40)
        return Z(f'Ein Kreis hat den Umfang {2 * k}π cm. Wie groß ist sein Radius?', k, f'{2 * k} / 2',
                 f'2πr = {2 * k}π → r = {k} cm.', 'Vergleiche 2 · π · r mit dem gegebenen Umfang.', 'cm')
    k = R.randint(2, 12)
    if R.random() < .5:
        return Z(f'Ein Kreis hat den Umfang {2 * k}π cm. Gib seinen Flächeninhalt exakt an: A = □ · π cm².', k * k, f'({2 * k} / 2) ** 2',
                 f'2πr = {2 * k}π → r = {k}. A = π · {k}² = {k * k}π cm².', 'Bestimme erst r aus dem Umfang.')
    R2, r1 = sorted(R.sample(range(1, 13), 2), reverse=True)
    return Z(f'Ein Kreisring hat den Außenradius {R2} cm und den Innenradius {r1} cm. Gib den Flächeninhalt exakt an: A = □ · π cm².', R2 * R2 - r1 * r1, f'{R2} ** 2 - {r1} ** 2',
             f'A = π · ({R2}² − {r1}²) = π · ({R2 * R2} − {r1 * r1}) = {R2 * R2 - r1 * r1}π cm².', 'Großer Kreis minus kleiner Kreis.')


WINKEL = [30, 36, 40, 45, 60, 72, 90, 120, 135, 150, 180, 210, 240, 270, 300]


def g_sektor(R, st):
    while True:
        al = R.choice(WINKEL[:8] if st == 1 else WINKEL)
        r = Fr(R.randint(2, 15)) if st < 3 else Fr(R.randint(10, 150), 10)
        teil = Fr(al, 360)
        b, a = teil * 2 * PIF * r, teil * PIF * r * r
        if ok(b) and ok(a): break
    if st == 1:
        return Z(f'Ein Kreisausschnitt hat den Mittelpunktswinkel {al}°. Welcher Anteil des Kreises ist das? Gib ihn als Dezimalzahl an.' if Fr(al, 360).denominator in (2, 4, 5, 8, 10, 20, 40) else
                 f'Ein Kreisausschnitt hat den Mittelpunktswinkel {al}°. Wie viel Prozent des Kreises sind das? (Runde auf eine Nachkommastelle.)',
                 teil if Fr(al, 360).denominator in (2, 4, 5, 8, 10, 20, 40) else runde(teil * 100, 1),
                 f'{al} / 360' if Fr(al, 360).denominator in (2, 4, 5, 8, 10, 20, 40) else f'round({al} / 360 * 100, 1)',
                 f'Anteil = {al}° : 360° = ' + (zt(teil) if teil.denominator in (2, 4, 5, 8, 10, 20, 40) else f'{teil.numerator}/{teil.denominator} ≈ {z1(teil * 100)} %') + '.', 'Teile den Winkel durch 360°.')
    if R.random() < .5:
        return rz(b, f'Ein Kreisausschnitt hat r = {zt(r)} cm und α = {al}°. Berechne die Bogenlänge. {RUNDE}', f'{al} / 360 * 2 * {PI} * {cz(r)}',
                  f'b = {al}/360 · 2π · {zt(r)} ≈ {z1((b, 1))} cm.', 'Bogen = Anteil · Umfang.', 'cm')
    return rz(a, f'Ein Kreisausschnitt hat r = {zt(r)} cm und α = {al}°. Berechne seinen Flächeninhalt. {RUNDE}', f'{al} / 360 * {PI} * {cz(r)} ** 2',
              f'A = {al}/360 · π · {zt(r)}² ≈ {z1((a, 1))} cm².', 'Fläche = Anteil · ganze Kreisfläche.', 'cm²')


def g_zusammengesetzt(R, st):
    while True:
        if st == 1 or (st == 2 and R.random() < .5):
            R2, r1 = sorted(R.sample(range(1, 16), 2), reverse=True)
            a = PIF * (R2 * R2 - r1 * r1)
            if ok(a):
                return rz(a, f'Ein Kreisring hat den Außenradius {R2} cm und den Innenradius {r1} cm. Berechne seinen Flächeninhalt. {RUNDE}', f'{PI} * ({R2} ** 2 - {r1} ** 2)',
                          f'A = π · ({R2}² − {r1}²) = π · {R2 * R2 - r1 * r1} ≈ {z1((a, 1))} cm².', 'Großer Kreis minus kleiner Kreis.', 'cm²')
        elif st == 2:
            r = R.randint(2, 15)
            a = PIF * r * r / 4 - Fr(r * r, 2)
            if ok(a):
                return rz(a, f'Ein Viertelkreis hat r = {r} cm. Man schneidet das rechtwinklige Dreieck aus den beiden Radien und der Sehne ab. Wie groß ist der Rest (Kreisabschnitt)? {RUNDE}',
                          f'{PI} * {r} ** 2 / 4 - {r} ** 2 / 2', f'Viertelkreis π · {r}² : 4, Dreieck {r} · {r} : 2 = {zt(Fr(r * r, 2))}. A ≈ {z1((a, 1))} cm².',
                          'Viertelkreis minus Dreieck.', 'cm²')
        else:
            art = R.choice(['quadrat', 'halbkreis', 'stadion'])
            a_ = R.randint(2, 20)
            if art == 'quadrat':
                x = a_ * a_ - PIF * Fr(a_, 2) ** 2
                if ok(x):
                    return rz(x, f'In ein Quadrat mit Seitenlänge {a_} cm wird ein Kreis gezeichnet, der alle vier Seiten berührt. Wie groß ist die Fläche außerhalb des Kreises im Quadrat? {RUNDE}',
                              f'{a_} ** 2 - {PI} * ({a_} / 2) ** 2', f'Quadrat {a_ * a_} cm², Kreis mit r = {zt(Fr(a_, 2))}: π · {zt(Fr(a_, 2))}². Differenz ≈ {z1((x, 1))} cm².',
                              'Der Kreis hat den Durchmesser = Seitenlänge.', 'cm²')
            elif art == 'halbkreis':
                x = PIF * a_ + 2 * a_
                if ok(x):
                    return rz(x, f'Ein Halbkreis hat den Radius {a_} cm. Wie lang ist sein Rand (Bogen und Durchmesser zusammen)? {RUNDE}', f'{PI} * {a_} + 2 * {a_}',
                              f'Halber Umfang π · {a_}, dazu der Durchmesser {2 * a_} cm. Zusammen ≈ {z1((x, 1))} cm.', 'Der gerade Rand gehört auch dazu.', 'cm')
            else:
                l = R.randint(5, 40)
                x = 2 * l + 2 * PIF * a_
                if ok(x):
                    return rz(x, f'Eine Laufbahn besteht aus zwei geraden Stücken von je {l} m und zwei Halbkreisen mit Radius {a_} m. Wie lang ist eine Runde? {RUNDE}',
                              f'2 * {l} + 2 * {PI} * {a_}', f'Gerade: 2 · {l} = {2 * l} m. Zwei Halbkreise = ein Kreis: 2π · {a_}. Zusammen ≈ {z1((x, 1))} m.',
                              'Zwei Halbkreise ergeben zusammen einen ganzen Kreis.', 'm')


def g_zylinder(R, st):
    while True:
        r, h = (Fr(R.randint(1, 10)), Fr(R.randint(2, 20))) if st < 3 else (Fr(R.randint(10, 100), 10), Fr(R.randint(20, 300), 10))
        V, M, O = PIF * r * r * h, 2 * PIF * r * h, 2 * PIF * r * r + 2 * PIF * r * h
        if ok(V) and ok(M) and ok(O): break
    was = R.choice(['V', 'M', 'O'] if st > 1 else ['V', 'M'])
    if st == 3 and R.random() < .35:
        L = R.choice([1, 2, 5]) * 1000
        r0, h0 = Fr(R.randint(3, 12)), Fr(R.randint(5, 30))
        V0 = PIF * r0 * r0 * h0
        if not ok(V0): return g_zylinder(R, st)
        return rz(V0 / 1000, f'Eine zylinderförmige Dose hat r = {zt(r0)} cm und h = {zt(h0)} cm. Wie viele Liter passen hinein? Runde auf eine Nachkommastelle.',
                  f'{PI} * {cz(r0)} ** 2 * {cz(h0)} / 1000', f'V = π · {zt(r0)}² · {zt(h0)} ≈ {z1((V0, 1))} cm³ = {z1((V0 / 1000, 1))} l (1 l = 1000 cm³).',
                  'Rechne in cm³ und teile durch 1000.', 'l') if ok(V0 / 1000) else g_zylinder(R, st)
    if was == 'V':
        return rz(V, f'Ein Zylinder hat r = {zt(r)} cm und h = {zt(h)} cm. Berechne sein Volumen. {RUNDE}', f'{PI} * {cz(r)} ** 2 * {cz(h)}',
                  f'V = π · {zt(r)}² · {zt(h)} ≈ {z1((V, 1))} cm³.', 'Grundfläche π · r² mal Höhe.', 'cm³')
    if was == 'M':
        return rz(M, f'Ein Zylinder hat r = {zt(r)} cm und h = {zt(h)} cm. Berechne seine Mantelfläche. {RUNDE}', f'2 * {PI} * {cz(r)} * {cz(h)}',
                  f'M = 2π · {zt(r)} · {zt(h)} ≈ {z1((M, 1))} cm².', 'Mantel = Umfang des Grundkreises · Höhe.', 'cm²')
    return rz(O, f'Ein Zylinder hat r = {zt(r)} cm und h = {zt(h)} cm. Berechne seine Oberfläche. {RUNDE}', f'2 * {PI} * {cz(r)} ** 2 + 2 * {PI} * {cz(r)} * {cz(h)}',
              f'O = 2π · {zt(r)}² + 2π · {zt(r)} · {zt(h)} ≈ {z1((O, 1))} cm².', 'Zwei Kreise plus Mantel.', 'cm²')


def g_verstehen(R, st):
    k = R.choice([2, 3, 4, 5, 10])
    wort = {2: 'verdoppelt', 3: 'verdreifacht', 4: 'vervierfacht', 5: 'verfünffacht', 10: 'verzehnfacht'}[k]
    if st == 1:
        was = R.choice(['Umfang', 'Flächeninhalt'])
        r = k if was == 'Umfang' else k * k
        return Z(f'Der Radius eines Kreises wird {wort}. Mit welchem Faktor ändert sich der {was}?', r, f'{k}' if was == 'Umfang' else f'{k} ** 2',
                 f'{"u = 2πr wächst wie r: Faktor " + str(k) if was == "Umfang" else "A = πr² wächst wie r²: Faktor " + str(k) + "² = " + str(k * k)}.',
                 'Setze für r einmal 1 und einmal ' + str(k) + ' ein und vergleiche.')
    if st == 2:
        r = R.randint(2, 12)
        fehl = R.choice(['2pr', 'pd2', 'pr'])
        wahl = {'2pr': (f'A = 2 · π · {r}', 'Das ist die Formel für den Umfang, nicht für die Fläche.'),
                'pd2': (f'A = π · {2 * r}²', 'Statt des Radius wurde der Durchmesser quadriert.'),
                'pr': (f'u = π · {r}', 'Für den Umfang braucht man den Durchmesser: u = π · d = π · ' + str(2 * r) + '.')}
        t, g = wahl[fehl]
        opts = ['Das ist die Formel für den Umfang, nicht für die Fläche.', 'Statt des Radius wurde der Durchmesser quadriert.',
                'Für den Umfang braucht man den Durchmesser: u = π · d = π · ' + str(2 * r) + '.', 'Die Rechnung ist richtig.']
        return A(R, f'Ein Kreis hat r = {r} cm. Jemand rechnet {t}. Was ist der Fehler?', g, [o for o in opts if o != g], f'{g} Richtig: u = 2π · {r}, A = π · {r}².',
                 'Vergleiche mit u = 2πr und A = πr².')
    r1 = R.randint(3, 12); u2 = R.randint(15, 80)
    r2 = Fr(u2) / (2 * PIF)
    gross = 'Der Kreis mit r = ' + str(r1) + ' cm' if r1 > r2 else 'Der Kreis mit u = ' + str(u2) + ' cm'
    if abs(r1 - r2) < Fr(1, 5): return g_verstehen(R, st)
    return A(R, f'Welcher Kreis hat den größeren Flächeninhalt: einer mit r = {r1} cm oder einer mit u = {u2} cm?', gross,
             ['Der Kreis mit u = ' + str(u2) + ' cm' if r1 > r2 else 'Der Kreis mit r = ' + str(r1) + ' cm', 'Beide sind gleich groß.', 'Das kann man nicht vergleichen.'],
             f'Aus u = {u2} cm folgt r = {u2} : (2π) ≈ {zt(runde(r2, 2))} cm. Der größere Radius gibt die größere Fläche.', 'Berechne aus dem Umfang den Radius.')


GEN = {'umfang': g_umfang, 'flaeche': g_flaeche, 'exakt': g_exakt, 'sektor': g_sektor, 'zusammengesetzt': g_zusammengesetzt, 'zylinder': g_zylinder, 'verstehen': g_verstehen}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Kreis', ['umfang', 'flaeche', 'exakt', 'verstehen']), ('Teile von Kreisen', ['sektor', 'zusammengesetzt']), ('Zylinder', ['zylinder'])],
         'Umfang und Flächeninhalt von Kreisen, Kreisausschnitten und Kreisringen berechnen – gerundet und exakt mit π – sowie Volumen und Oberfläche von Zylindern.',
         ['u = 2πr = πd, A = πr².', 'Ausschnitt: Anteil α/360° von Umfang bzw. Fläche.', 'Zylinder: V = πr²h, O = 2πr² + 2πrh.'],
         offen=['Gerundete Ergebnisse: Die Aufgaben verlangen „auf eine Nachkommastelle runden“ und rechnen mit dem π-Wert des Taschenrechners. '
                'Rechnet ein Kind mit 3,14, weicht das Ergebnis manchmal in der letzten Stelle ab. Bitte prüfen, ob die App bei Zahl-Antworten eine Toleranz zulässt.',
                'Kreisabschnitt (Segment) nur beim Mittelpunktswinkel 90°: Für andere Winkel braucht man Trigonometrie (spätere Jahrgangsstufe).',
                'Kreise, Ausschnitte und Zylinder werden nur in Worten beschrieben; Skizzen wären hilfreich (Zeichenfunktion fehlt).'])
