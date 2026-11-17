#!/usr/bin/env python3
"""Thema messen.kreisberechnung – Kreisberechnungen (Gymnasium Bayern, Klasse 8)."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _bausatz import PI, PIF, A, Z, baue, cz, mit_bild, runde, sicher_rundbar, zt  # noqa: E402

META = {'thema_schluessel': 'messen.kreisberechnung', 'thema_id': 51, 'block_id': 84, 'klasse': {'gym_by': 8, 'rs_by': 9}}
RUNDE = 'Runde auf eine Nachkommastelle.'
TIPP_PI = 'Rechne mit der π-Taste und runde erst am Ende.'

ETAPPEN = [
    {'lernziel': 'umfang', 'titel': 'Kreisumfang berechnen',
     'regel': 'Leg eine Schnur einmal um eine Dose und miss sie: Sie ist gut ⟦dreimal so lang⟧ wie der Durchmesser der Dose – genauer 3,14…-mal. Diese Zahl heißt ⟦π⟧ (Pi). Es gilt ⟦u = π · d = 2 · π · r⟧.',
     'schritte': ['Eine Dose hat den Radius r = 4 cm. Wie lang muss das Etikett sein?', 'u = 2 · π · 4 cm = 8π cm', 'u ≈ ⟦25,1 cm⟧'],
     'probe': 'Überschlag: d = 8 cm, dreimal so viel sind 24 cm – passt zu 25,1 cm ✓',
     'fehler': 'u = π · r ist falsch: Man braucht den ⟦Durchmesser⟧ (d = 2r). Bei r = 4 cm ist u = π · 8 cm ≈ 25,1 cm, nicht 12,6 cm.',
     'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_P': [4, 0], '_Q': [0, -4], '_R': [0, 4]}, 'linien': [['M', '_P', 'r = 4 cm'], ['_Q', '_R', 'd = 8 cm', 'gestrichelt']], 'kreise': [{'m': 'M', 'r': 4}]},
     '_verbot': ['r = 4 cm']},
    {'lernziel': 'flaeche', 'titel': 'Flächeninhalt eines Kreises',
     'regel': 'Schneide einen Kreis wie eine Torte in viele schmale Stücke und lege sie abwechselnd mit der Spitze nach oben und nach unten nebeneinander. Es entsteht fast ein ⟦Rechteck⟧: so lang wie der halbe Umfang (π · r) und so hoch wie der Radius r. Also ist ⟦A = π · r · r = π · r²⟧.',
     'schritte': ['Eine Pizza hat den Durchmesser 30 cm, also r = 15 cm.', 'Zuerst quadrieren: r² = 15 cm · 15 cm = 225 cm².', 'A = π · 225 cm² ≈ ⟦706,9 cm²⟧'],
     'probe': 'Überschlag: Das Quadrat um die Pizza hat 30 · 30 = 900 cm². Der Kreis füllt gut drei Viertel davon: etwa 700 cm² ✓',
     'fehler': 'A = π · d² ist falsch: In die Formel gehört der ⟦Radius⟧. Mit d = 30 cm käme π · 900 ≈ 2 827 cm² heraus – viermal zu viel, die Pizza wäre größer als ihr eigener Karton.',
     '_verbot': ['Durchmesser 30 cm, also r = 15']},
    {'lernziel': 'exakt', 'titel': 'Exakt rechnen mit π',
     'regel': 'Statt zu runden, kannst du Ergebnisse ⟦exakt als Vielfaches von π⟧ angeben, z. B. A = 16π cm². Das ist genauer und oft einfacher zu rechnen.',
     'schritte': ['r = 3 cm', 'u = 2 · π · 3 = ⟦6π cm⟧', 'A = π · 3² = ⟦9π cm²⟧'],
     'fehler': 'Bei r = 3 ist A nicht 6π: Dann hätte man 2 · 3 statt ⟦3²⟧ gerechnet. Das ist der Umfang, nicht die Fläche.',
     '_verbot': ['r = 3 cm']},
    {'lernziel': 'verstehen', 'titel': 'Wie ändern sich Umfang und Fläche?',
     'regel': 'Der Umfang wächst ⟦wie r⟧: doppelter Radius, doppelter Umfang. Die Fläche wächst ⟦wie r²⟧: doppelter Radius, ⟦vierfache⟧ Fläche.',
     'schritte': ['Eine große Pizza (d = 30 cm) oder zwei kleine (je d = 20 cm)?', 'Groß: π · 15² = 225π cm². Zwei kleine: 2 · π · 10² = 200π cm².',
                  'Die eine große Pizza ist ⟦größer⟧, obwohl 2 · 20 cm mehr sind als 30 cm. Die Fläche wächst mit ⟦r²⟧.'],
     'probe': 'Dreifacher Radius: r = 2 cm gibt 4π cm², r = 6 cm gibt 36π cm². 36π : 4π = 9 = 3² ✓',
     'fehler': 'Doppelter Radius heißt nicht doppelte Fläche: π · (2r)² = π · 4r². Die Fläche wird ⟦vervierfacht⟧.'},
    {'lernziel': 'sektor', 'titel': 'Kreisausschnitt: Bogen und Fläche',
     'regel': 'Ein ⟦Kreisausschnitt⟧ mit Mittelpunktswinkel α ist der Anteil α/360° vom ganzen Kreis: ⟦Bogen b = α/360° · 2πr⟧, ⟦Fläche A = α/360° · πr²⟧.',
     'schritte': ['Ein Tortenstück: r = 6 cm, Mittelpunktswinkel α = 120°. Anteil: 120° von 360° = 1/3 der Torte.', 'Bogen: 1/3 · 2π · 6 cm = 4π cm ≈ 12,6 cm.',
                  'Fläche: 1/3 · π · 6² cm² = ⟦12π cm² ≈ 37,7 cm²⟧.'],
     'fehler': 'Der Anteil eines 90°-Ausschnitts ist nicht 90/100. Ein ganzer Kreis hat ⟦360°⟧: Der Anteil ist 90/360 = 1/4.',
     'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_s0': [6.0, 0.0], '_s1': [5.64, 2.05], '_s2': [4.6, 3.86], '_s3': [3.0, 5.2], '_s4': [1.04, 5.91], '_s5': [-1.04, 5.91], '_s6': [-3.0, 5.2]},
              'flaeche': ['M', '_s0', '_s1', '_s2', '_s3', '_s4', '_s5', '_s6'], 'linien': [['M', '_s0', 'r = 6 cm'], ['M', '_s6']], 'winkel': [['M', '_s0', '_s6', '120°']], 'kreise': [{'m': 'M', 'r': 6}]},
     '_verbot': ['r = 6 cm, α = 120°', 'r = 6 cm, Mittelpunktswinkel']},
    {'lernziel': 'zusammengesetzt', 'titel': 'Kreisring und Kreisabschnitt',
     'regel': '⟦Kreisring⟧: großer Kreis minus kleiner Kreis, A = π · (R² − r²). ⟦Kreisabschnitt⟧ (Segment) bei 90°: Viertelkreis minus rechtwinkliges Dreieck, A = πr²/4 − r²/2.',
     'schritte': ['Ring: R = 5 cm, r = 3 cm', 'A = π · (25 − 9) cm² = 16π cm²', 'A ≈ ⟦50,3 cm²⟧'],
     'fehler': 'Beim Ring ist A nicht π · (5 − 3)² = 4π. Man muss erst ⟦jeden⟧ Radius quadrieren und dann subtrahieren: π · (25 − 9).',
     'bild': {'typ': 'figur', 'punkte': {'M': [0, 0], '_P': [5, 0], '_Q': [0, 3]}, 'linien': [['M', '_P', 'R = 5 cm'], ['M', '_Q', 'r = 3 cm']], 'kreise': [{'m': 'M', 'r': 5}, {'m': 'M', 'r': 3}]},
     '_verbot': ['R = 5 cm, r = 3 cm']},
    {'lernziel': 'zylinder', 'titel': 'Zylinder: Volumen und Oberfläche',
     'regel': 'Ein Zylinder ist ein „rundes Prisma“: ⟦V = π · r² · h⟧ (Grundfläche mal Höhe). Mantel M = 2πr · h, Oberfläche ⟦O = 2πr² + 2πrh⟧.',
     'schritte': ['r = 2 cm, h = 10 cm', 'V = π · 4 · 10 cm³ = 40π cm³ ≈ 125,7 cm³', 'O = 2π · 4 + 2π · 2 · 10 = 48π cm² ≈ ⟦150,8 cm²⟧'],
     'fehler': 'Die Oberfläche ist nicht nur der Mantel 2πrh: Es fehlen ⟦Boden und Deckel⟧ (2 · πr²).',
     '_verbot': ['r = 2 cm, h = 10 cm']},
]


# ---- KLAR (verständliche Erklärungen, Runde 7) ----
KLAR = {
 'umfang': {
  'einstieg': 'Für eine Dose soll ein Etikett gedruckt werden, das genau einmal herumreicht. Wie lang muss es sein? Mit dem Lineal kann man um eine Rundung schlecht messen. Man kann die Länge aber aus dem Radius ausrechnen. Die Länge einmal um den Kreis heißt ⟦Umfang⟧.',
  'woerter': [['Umfang u', 'die Länge einmal um den Kreis herum'], ['Radius r', 'Abstand von der Mitte zum Rand'], ['Durchmesser d', 'Strecke quer durch die Mitte: d = 2r'],
              ['π (Pi)', 'die Zahl 3,14159…: so oft passt der Durchmesser in den Umfang'], ['≈', 'ungefähr gleich (gerundet)']],
  'schritte': ['Eine Dose hat den Radius r = 4 cm. Wie lang muss das Etikett sein?', 'Der Durchmesser ist doppelt so lang wie der Radius: d = 8 cm.',
               'Der Umfang ist π-mal so lang wie der Durchmesser: u = π · 8 cm = 8π cm.', 'Mit π ≈ 3,14 gerundet: u ≈ ⟦25,1 cm⟧.'],
  'regel': 'So berechnest du den ⟦Umfang⟧: ⟦u = π · d = 2 · π · r⟧. Hast du den Radius, verdopple ihn zuerst.'},
 'flaeche': {
  'einstieg': 'Eine Pizzeria bietet Pizzen mit 30 cm Durchmesser an. Wie viel Pizza ist das eigentlich? Gemeint ist die Fläche des Kreises, also wie viel Platz die Pizza auf dem Teller bedeckt. Sie heißt ⟦Flächeninhalt des Kreises⟧.',
  'woerter': [['Flächeninhalt A', 'wie viel Platz eine Figur bedeckt, in cm²'], ['r²', '„r Quadrat“: r mal r'], ['π · r²', 'π mal r mal r – zuerst r² rechnen, dann mit π malnehmen']],
  'schritte': ['Eine Pizza hat den Durchmesser 30 cm. Der Radius ist die Hälfte: r = 15 cm.', 'Zuerst quadrieren: r² = 15 cm · 15 cm = 225 cm².',
               'Dann mit π malnehmen: A = π · 225 cm² ≈ ⟦706,9 cm²⟧.'],
  'regel': 'So berechnest du die ⟦Kreisfläche⟧: Radius bestimmen, quadrieren, mit π malnehmen: ⟦A = π · r²⟧. Hast du d, halbiere ihn zuerst.'},
 'exakt': {
  'einstieg': 'π hat unendlich viele Nachkommastellen. Jedes Runden macht ein Ergebnis ein bisschen ungenau. Lässt man π als Zeichen stehen, bleibt das Ergebnis genau, etwa „9π cm²“. So ein Ergebnis heißt ⟦exakt⟧.',
  'woerter': [['exakt', 'ganz genau, ohne Runden'], ['6π', '6 mal π – das Malzeichen lässt man weg'], ['Vielfaches von π', 'eine Zahl mal π, z. B. 9π']],
  'schritte': ['Ein Kreis hat den Radius r = 3 cm.', 'Umfang: u = 2 · π · 3 cm. Die Zahlen werden zuerst zusammengerechnet: 2 · 3 = 6, also ⟦u = 6π cm⟧.',
               'Fläche: A = π · 3² cm². Es ist 3² = 9, also ⟦A = 9π cm²⟧.'],
  'regel': 'So rechnest du ⟦exakt⟧: Alle Zahlen ausrechnen und π als Zeichen stehen lassen, z. B. A = 16π cm². Erst wenn eine Kommazahl gefragt ist, mit π ≈ 3,14 malnehmen.'},
 'verstehen': {
  'einstieg': 'Im Angebot: eine große Pizza mit 30 cm Durchmesser oder zwei kleine mit je 20 cm, zum gleichen Preis. Zwei kleine klingt nach mehr. Doch die Fläche wächst nicht so wie der Durchmesser. Wer die Fläche vergleicht, kann gut ⟦Größen vergleichen⟧.',
  'woerter': [['wächst wie r', 'doppelter Radius → doppelter Wert'], ['wächst wie r²', 'doppelter Radius → vierfacher Wert'], ['vervierfachen', 'mal 4 nehmen']],
  'schritte': ['Eine große Pizza (d = 30 cm) oder zwei kleine (je d = 20 cm)?', 'Groß: Der Radius ist 15 cm, die Fläche π · 15² = 225π cm².',
               'Zwei kleine: Jede hat den Radius 10 cm. Zusammen ist die Fläche 2 · π · 10² = 200π cm².', 'Die eine große Pizza ist ⟦größer⟧, weil die Fläche mit ⟦r²⟧ wächst.']},
 'sektor': {
  'einstieg': 'Eine runde Torte wird in Stücke geschnitten. Ein Stück hat eine Spitze in der Mitte und einen gebogenen Rand außen. Wie viel Torte es ist, hängt vom Winkel an der Spitze ab. So ein Stück heißt ⟦Kreisausschnitt⟧.',
  'woerter': [['Kreisausschnitt', 'ein „Tortenstück“ des Kreises'], ['Mittelpunktswinkel α', 'der Winkel an der Spitze in der Kreismitte'],
              ['Bogen b', 'der gebogene Rand außen am Stück'], ['α/360°', 'der Anteil des Stücks am ganzen Kreis']]},
 'zusammengesetzt': {
  'einstieg': 'Ein Donut ist ein großer Kreis, aus dem in der Mitte ein kleiner Kreis fehlt. Seine Fläche ist also „groß minus klein“. So eine Form heißt ⟦Kreisring⟧. Auch andere Figuren setzt man so aus Kreisteilen zusammen.',
  'woerter': [['Kreisring', 'Fläche zwischen zwei Kreisen mit derselben Mitte'], ['R und r', 'R ist der große Radius, r der kleine'],
              ['Kreisabschnitt (Segment)', 'Teil eines Kreises, der von einer geraden Linie abgeschnitten wird'], ['Viertelkreis', 'ein Kreisausschnitt mit 90°']],
  'schritte': ['Ein Ring hat außen R = 5 cm und innen r = 3 cm.', 'Großer Kreis: π · 5² = 25π cm². Kleiner Kreis: π · 3² = 9π cm².',
               'Den kleinen Kreis abziehen: 25π − 9π = 16π cm².', 'Gerundet: A ≈ ⟦50,3 cm²⟧.']},
 'zylinder': {
  'einstieg': 'Wie viel passt in eine Dose, und wie viel Blech braucht man für sie? Die Dose ist wie ein Stapel aus vielen dünnen Kreisscheiben. Darum rechnet man: Fläche des Bodens mal Höhe. Der Rauminhalt heißt ⟦Volumen⟧, das Blech ist die ⟦Oberfläche⟧.',
  'woerter': [['Volumen V', 'wie viel in einen Körper hineinpasst, in cm³'], ['Grundfläche', 'der Kreis unten: π · r²'], ['Mantel M', 'das abgewickelte Etikett: 2πr · h'],
              ['Oberfläche O', 'Boden + Deckel + Mantel'], ['cm³', 'Kubikzentimeter, Einheit für Volumen']],
  'schritte': ['Eine Dose hat r = 2 cm und h = 10 cm.', 'Volumen: Grundfläche π · 2² = 4π cm², mal Höhe 10 cm ergibt 40π cm³ ≈ 125,7 cm³.',
               'Boden und Deckel: 2 · 4π = 8π cm². Mantel: 2π · 2 · 10 = 40π cm².', 'Oberfläche: 8π + 40π = 48π cm² ≈ ⟦150,8 cm²⟧.']},
}

for _e in ETAPPEN:
    _e.update(KLAR.get(_e['lernziel'], {}))
# ---- KLAR ENDE ----


def rz(x, text, c, w, h, einheit):
    a = Z(text, runde(x, 1), f'round({c}, 1)', w, h, einheit)
    a['o']['toleranz'] = 0.1   # wer mit 3,14 statt der π-Taste rechnet, liegt höchstens in der letzten Stelle daneben
    return a


def ok(x): return sicher_rundbar(x, 1)


def z1(x):
    """Auf eine Nachkommastelle gerundet, immer mit einer Nachkommastelle geschrieben."""
    t = zt(runde(x, 1))
    return t if ',' in t else t + ',0'


def zahl_r(R, st):
    if st == 1: return Fr(R.randint(1, 15))
    if st == 2: return Fr(R.randint(10, 150), 10) if R.random() < .5 else Fr(R.randint(2, 30))
    return Fr(R.randint(5, 250), 10)


KONTEXT_R = {'Ein Fahrradrad': (30, 36), 'Ein runder Esstisch': (45, 75), 'Eine Pizza': (13, 18), 'Eine Wanduhr': (10, 20)}


def g_umfang(R, st):
    if st <= 2 and R.random() < .2:
        ding, d, k = R.choice([('einer Dose', 8, 1), ('einem Teller', 25, 1), ('einem Eimer', 30, 1), ('einer Tasse', 9, 1)])
        u = runde(PIF * d, 1)
        return A(R, f'Du misst bei {ding} den Umfang u = {zt(u)} cm und den Durchmesser d = {d} cm. Was ergibt u : d ungefähr?', '3,14',
                 ['2', '0,32', '6,28'], f'{zt(u)} : {d} ≈ 3,14. Das ist π – bei jedem Kreis gleich.', 'Teile den Umfang durch den Durchmesser.')
    if st == 3 and R.random() < .3:
        d_cm, strecke, einh = R.choice([(70, 1000, '1 km'), (66, 1000, '1 km'), (20, 50, '50 m'), (60, 500, '500 m'), (24, 100, '100 m')])
        n = int(Fr(strecke * 100) / (PIF * d_cm))
        return Z(f'Ein Rad mit {d_cm} cm Durchmesser rollt {einh} weit. Wie viele volle Umdrehungen macht es?', n, f'{strecke * 100} // ({PI} * {d_cm})',
                 f'Eine Umdrehung = Umfang = π · {d_cm} cm ≈ {z1(PIF * d_cm)} cm. {zt(strecke * 100)} cm : {z1(PIF * d_cm)} cm ≈ {zt(runde(Fr(strecke * 100) / (PIF * d_cm), 1))} → {n} volle Umdrehungen.',
                 'Bei einer Umdrehung rollt das Rad einen Umfang weit. Rechne alles in cm.')
    while True:
        r = zahl_r(R, st)
        u = 2 * PIF * r
        if ok(u) and ok(u / (2 * PIF)): break
    if st == 3 and R.random() < .5:
        u0 = runde(u, 1)
        r0 = u0 / (2 * PIF)
        if not ok(r0): return g_umfang(R, st)
        return rz(r0, f'Ein Kreis hat den Umfang {zt(u0)} cm. Berechne den Radius. {RUNDE}', f'{cz(u0)} / (2 * {PI})',
                  f'u = 2πr → r = u : (2π) = {zt(u0)} : (2π) ≈ {z1(r0)} cm.', 'Stelle u = 2πr nach r um.', 'cm')
    if R.random() < .4:
        d = 2 * r
        return rz(PIF * d, f'Ein Kreis hat den Durchmesser {zt(d)} cm. Berechne den Umfang. {RUNDE}', f'{PI} * {cz(d)}',
                  f'u = π · d = π · {zt(d)} ≈ {z1(PIF * d)} cm.', TIPP_PI, 'cm')
    kontext = R.choice(['', '', 'Ein Fahrradrad', 'Ein runder Esstisch', 'Eine Pizza', 'Eine Wanduhr']) if st >= 2 else ''
    if kontext:
        lo, hi = KONTEXT_R[kontext]
        while True:
            r = Fr(R.randint(lo, hi)) if R.random() < .6 else Fr(R.randint(lo * 10, hi * 10), 10)
            u = 2 * PIF * r
            if ok(u): break
    text = f'{kontext} hat den Radius {zt(r)} cm. Wie lang ist der Umfang? {RUNDE}' if kontext else f'Berechne den Umfang eines Kreises mit r = {zt(r)} cm. {RUNDE}'
    return rz(u, text, f'2 * {PI} * {cz(r)}', f'u = 2 · π · {zt(r)} ≈ {z1(u)} cm.', TIPP_PI, 'cm')


def g_flaeche(R, st):
    if st == 3 and R.random() < .35:
        D, d = R.choice([(32, 22), (30, 20), (36, 24), (28, 20), (30, 22)])
        AG, AK = PIF * Fr(D, 2) ** 2, 2 * PIF * Fr(d, 2) ** 2
        gross = AG > AK
        ri = f'bei der großen ({zt(runde(AG, 0))} cm² gegen {zt(runde(AK, 0))} cm²)' if gross else f'bei den zwei kleinen ({zt(runde(AK, 0))} cm² gegen {zt(runde(AG, 0))} cm²)'
        fa = [f'bei den zwei kleinen ({2 * d} cm > {D} cm)' if gross else f'bei der großen ({D} cm Durchmesser)', 'gleich viel', 'Das kann man ohne Preis pro Stück nicht sagen.']
        return A(R, f'Eine Pizza mit {D} cm Durchmesser kostet 10 €, zwei Pizzen mit je {d} cm kosten zusammen auch 10 €. Wo bekommst du mehr Pizza?', ri, fa,
                 f'Groß: π · {zt(Fr(D, 2))}² ≈ {zt(runde(AG, 0))} cm². Zwei kleine: 2 · π · {zt(Fr(d, 2))}² ≈ {zt(runde(AK, 0))} cm². Es zählt die Fläche, nicht der Durchmesser.',
                 'Vergleiche die Flächen, nicht die Durchmesser.')
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
                  f'r = {zt(d)} : 2 = {zt(r)} cm. A = π · {zt(r)}² ≈ {z1(a)} cm².', 'Zuerst den Radius bestimmen.', 'cm²')
    return rz(a, f'Berechne den Flächeninhalt eines Kreises mit r = {zt(r)} cm. {RUNDE}', f'{PI} * {cz(r)} ** 2',
              f'A = π · {zt(r)}² = π · {zt(r * r)} ≈ {z1(a)} cm².', 'Erst r² berechnen, dann mal π.', 'cm²')


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
    if st == 3 and R.random() < .4:
        if R.random() < .6:
            r_ = R.choice([3, 4, 5, 6, 8, 9, 10, 12])
            al = R.choice([30, 45, 60, 90, 120, 135, 150, 180, 240, 270])
            if R.random() < .5:
                b = Fr(al, 360) * 2 * r_
                if not (b.denominator in (1, 2, 4, 5)): return g_sektor(R, st)
                return Z(f'Ein Kreisausschnitt mit r = {r_} cm hat die Bogenlänge {zt(b)}π cm. Wie groß ist der Mittelpunktswinkel?', al, f'{cz(b)} / (2 * {r_}) * 360',
                         f'Ganzer Umfang: 2π · {r_} = {2 * r_}π cm. Anteil: {zt(b)}π : {2 * r_}π = {zt(b / (2 * r_))}. Winkel: {zt(b / (2 * r_))} · 360° = {al}°.',
                         'Welcher Anteil des ganzen Umfangs ist der Bogen?', '°')
            a = Fr(al, 360) * r_ * r_
            if not (a.denominator in (1, 2, 4, 5)): return g_sektor(R, st)
            return Z(f'Ein Kreisausschnitt mit r = {r_} cm hat den Flächeninhalt {zt(a)}π cm². Wie groß ist der Mittelpunktswinkel?', al, f'{cz(a)} / {r_ * r_} * 360',
                     f'Ganzer Kreis: π · {r_}² = {r_ * r_}π cm². Anteil: {zt(a)}π : {r_ * r_}π = {zt(a / (r_ * r_))}. Winkel: {zt(a / (r_ * r_))} · 360° = {al}°.',
                     'Welcher Anteil der ganzen Kreisfläche ist der Ausschnitt?', '°')
        L_, inn, al = R.choice([(50, 10, 120), (45, 10, 110), (60, 15, 100), (55, 12, 120)])
        x = Fr(al, 360) * PIF * (L_ * L_ - inn * inn)
        a_ = Z(f'Ein Scheibenwischer ist {L_} cm lang und überstreicht {al}°. Die inneren {inn} cm wischen nicht. Wie groß ist die gewischte Fläche? Runde auf ganze cm².',
               runde(x, 0), f'round({al} / 360 * {PI} * ({L_} ** 2 - {inn} ** 2), 0)',
               f'Gewischt wird ein Ausschnitt aus einem Kreisring: {al}/360 · π · ({L_}² − {inn}²) = {al}/360 · π · {L_ * L_ - inn * inn} ≈ {zt(runde(x, 0))} cm².',
               'Ausschnitt eines Kreisrings: Anteil · π · (R² − r²).', 'cm²', toleranz=1)
        return a_
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
                  f'b = {al}/360 · 2π · {zt(r)} ≈ {z1(b)} cm.', 'Bogen = Anteil · Umfang.', 'cm')
    return rz(a, f'Ein Kreisausschnitt hat r = {zt(r)} cm und α = {al}°. Berechne seinen Flächeninhalt. {RUNDE}', f'{al} / 360 * {PI} * {cz(r)} ** 2',
              f'A = {al}/360 · π · {zt(r)}² ≈ {z1(a)} cm².', 'Fläche = Anteil · ganze Kreisfläche.', 'cm²')


RING = {'n': 0}


def ring_bild(R2, r1):
    return {'typ': 'figur', 'punkte': {'M': [0, 0], '_P': [R2, 0], '_Q': [0, r1]}, 'linien': [['M', '_P', f'R = {R2} cm'], ['M', '_Q', f'r = {r1} cm']],
            'kreise': [{'m': 'M', 'r': R2}, {'m': 'M', 'r': r1}]}


def g_zusammengesetzt(R, st):
    while True:
        if (st == 1 or (st == 2 and R.random() < .5)) and RING['n'] < 8:
            RING['n'] += 1
            R2, r1 = sorted(R.sample(range(1, 16), 2), reverse=True)
            a = PIF * (R2 * R2 - r1 * r1)
            if ok(a):
                return mit_bild(rz(a, f'Ein Kreisring hat den Außenradius {R2} cm und den Innenradius {r1} cm. Berechne seinen Flächeninhalt. {RUNDE}', f'{PI} * ({R2} ** 2 - {r1} ** 2)',
                                   f'A = π · ({R2}² − {r1}²) = π · {R2 * R2 - r1 * r1} ≈ {z1(a)} cm².', 'Großer Kreis minus kleiner Kreis.', 'cm²'), ring_bild(R2, r1))
        elif st <= 2:
            r = R.randint(2, 15)
            a = PIF * r * r / 4 - Fr(r * r, 2)
            if ok(a):
                gr = {'typ': 'figur', 'punkte': {'M': [0, 0], 'A': [r, 0], 'B': [0, r]}, 'flaeche': ['M', 'A', 'B'], 'linien': [['M', 'A', f'r = {r} cm'], ['M', 'B'], ['A', 'B', '', 'gestrichelt']],
                      'rechter_winkel': [['M', 'A', 'B']], 'kreise': [{'m': 'M', 'r': r}]}
                return mit_bild(rz(a, f'Ein Viertelkreis hat r = {r} cm. Man schneidet das rechtwinklige Dreieck aus den beiden Radien und der Sehne ab. Wie groß ist der Rest (Kreisabschnitt)? {RUNDE}',
                                   f'{PI} * {r} ** 2 / 4 - {r} ** 2 / 2', f'Viertelkreis π · {r}² : 4, Dreieck {r} · {r} : 2 = {zt(Fr(r * r, 2))}. A ≈ {z1(a)} cm².',
                                   'Viertelkreis minus Dreieck. Im Bild ist das Dreieck markiert; gesucht ist das Stück zwischen Sehne und Bogen.', 'cm²'), gr)
        else:
            art = R.choice(['quadrat', 'halbkreis', 'stadion'])
            a_ = R.randint(2, 20)
            if art == 'quadrat':
                x = a_ * a_ - PIF * Fr(a_, 2) ** 2
                if ok(x):
                    h_ = a_ / 2
                    gr = {'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [a_, 0], 'C': [a_, a_], 'D': [0, a_], '_M': [h_, h_]},
                          'linien': [['A', 'B', f'{a_} cm'], ['B', 'C'], ['C', 'D'], ['D', 'A']], 'kreise': [{'m': '_M', 'r': h_}]}
                    return mit_bild(rz(x, f'In ein Quadrat mit Seitenlänge {a_} cm wird ein Kreis gezeichnet, der alle vier Seiten berührt. Wie groß ist die Fläche außerhalb des Kreises im Quadrat? {RUNDE}',
                                       f'{a_} ** 2 - {PI} * ({a_} / 2) ** 2', f'Quadrat {a_ * a_} cm², Kreis mit r = {zt(Fr(a_, 2))}: π · {zt(Fr(a_, 2))}². Differenz ≈ {z1(x)} cm².',
                                       'Der Kreis hat den Durchmesser = Seitenlänge.', 'cm²'), gr)
            elif art == 'halbkreis':
                x = PIF * a_ + 2 * a_
                if ok(x):
                    return rz(x, f'Ein Halbkreis hat den Radius {a_} cm. Wie lang ist sein Rand (Bogen und Durchmesser zusammen)? {RUNDE}', f'{PI} * {a_} + 2 * {a_}',
                              f'Halber Umfang π · {a_}, dazu der Durchmesser {2 * a_} cm. Zusammen ≈ {z1(x)} cm.', 'Der gerade Rand gehört auch dazu.', 'cm')
            else:
                l = R.randint(5, 40)
                x = 2 * l + 2 * PIF * a_
                if ok(x):
                    return rz(x, f'Eine Laufbahn besteht aus zwei geraden Stücken von je {l} m und zwei Halbkreisen mit Radius {a_} m. Wie lang ist eine Runde? {RUNDE}',
                              f'2 * {l} + 2 * {PI} * {a_}', f'Gerade: 2 · {l} = {2 * l} m. Zwei Halbkreise = ein Kreis: 2π · {a_}. Zusammen ≈ {z1(x)} m.',
                              'Zwei Halbkreise ergeben zusammen einen ganzen Kreis.', 'm')


def g_zylinder(R, st):
    while True:
        r, h = (Fr(R.randint(1, 10)), Fr(R.randint(2, 20))) if st < 3 else (Fr(R.randint(10, 100), 10), Fr(R.randint(20, 300), 10))
        V, M, O = PIF * r * r * h, 2 * PIF * r * h, 2 * PIF * r * r + 2 * PIF * r * h
        if ok(V) and ok(M) and ok(O): break
    was = R.choice(['V', 'M', 'O'] if st > 1 else ['V', 'M'])
    if st >= 2 and R.random() < .25:
        ding, r0, L0 = R.choice([('Eine zylindrische Vase', 5, 1), ('Eine zylindrische Vase', 4, 1), ('Ein Regenfass', 30, 200), ('Ein Messbecher', 5, 1), ('Ein Regenfass', 35, 250)])
        h0 = Fr(L0 * 1000) / (PIF * r0 * r0)
        if not ok(h0): return g_zylinder(R, st)
        frage = f'{ding} hat den Radius {r0} cm und soll {L0} l fassen. Wie hoch muss sie mindestens sein? {RUNDE}' if 'Vase' in ding or 'Mess' in ding else \
            f'{ding} mit r = {r0} cm enthält {L0} l Wasser. Wie hoch steht das Wasser? {RUNDE}'
        return rz(h0, frage, f'{L0} * 1000 / ({PI} * {r0} ** 2)',
                  f'{L0} l = {zt(L0 * 1000)} cm³. V = π · r² · h → h = V : (π · r²) = {zt(L0 * 1000)} : (π · {r0 * r0}) ≈ {z1(h0)} cm.',
                  'Rechne Liter in cm³ um und stelle V = π · r² · h nach h um.', 'cm')
    if st == 3 and R.random() < .35:
        L = R.choice([1, 2, 5]) * 1000
        r0, h0 = Fr(R.randint(3, 12)), Fr(R.randint(5, 30))
        V0 = PIF * r0 * r0 * h0
        if not ok(V0): return g_zylinder(R, st)
        return rz(V0 / 1000, f'Eine zylinderförmige Dose hat r = {zt(r0)} cm und h = {zt(h0)} cm. Wie viele Liter passen hinein? Runde auf eine Nachkommastelle.',
                  f'{PI} * {cz(r0)} ** 2 * {cz(h0)} / 1000', f'V = π · {zt(r0)}² · {zt(h0)} ≈ {z1(V0)} cm³ = {z1(V0 / 1000)} l (1 l = 1000 cm³).',
                  'Rechne in cm³ und teile durch 1000.', 'l') if ok(V0 / 1000) else g_zylinder(R, st)
    if was == 'V':
        return rz(V, f'Ein Zylinder hat r = {zt(r)} cm und h = {zt(h)} cm. Berechne sein Volumen. {RUNDE}', f'{PI} * {cz(r)} ** 2 * {cz(h)}',
                  f'V = π · {zt(r)}² · {zt(h)} ≈ {z1(V)} cm³.', 'Grundfläche π · r² mal Höhe.', 'cm³')
    if was == 'M':
        return rz(M, f'Ein Zylinder hat r = {zt(r)} cm und h = {zt(h)} cm. Berechne seine Mantelfläche. {RUNDE}', f'2 * {PI} * {cz(r)} * {cz(h)}',
                  f'M = 2π · {zt(r)} · {zt(h)} ≈ {z1(M)} cm².', 'Mantel = Umfang des Grundkreises · Höhe.', 'cm²')
    return rz(O, f'Ein Zylinder hat r = {zt(r)} cm und h = {zt(h)} cm. Berechne seine Oberfläche. {RUNDE}', f'2 * {PI} * {cz(r)} ** 2 + 2 * {PI} * {cz(r)} * {cz(h)}',
              f'O = 2π · {zt(r)}² + 2π · {zt(r)} · {zt(h)} ≈ {z1(O)} cm².', 'Zwei Kreise plus Mantel.', 'cm²')


def g_verstehen(R, st):
    k = R.choice([2, 3, 4, 5, 10])
    wort = {2: 'verdoppelt', 3: 'verdreifacht', 4: 'vervierfacht', 5: 'verfünffacht', 10: 'verzehnfacht'}[k]
    if st >= 2 and R.random() < .3:
        f, wort2 = R.choice([(Fr(1, 2), 'Der Durchmesser wird halbiert'), (Fr(3, 2), 'Der Radius wird mit 1,5 multipliziert'), (Fr(2), 'Der Durchmesser wird verdoppelt'),
                             (Fr(1, 10), 'Der Radius wird auf ein Zehntel verkleinert')])
        return Z(f'{wort2}. Mit welchem Faktor ändert sich der Flächeninhalt?', f * f, f'{cz(f)} ** 2',
                 f'Der Radius ändert sich mit dem Faktor {zt(f)}. Die Fläche wächst wie r²: {zt(f)}² = {zt(f * f)}.', 'Die Fläche hängt von r² ab. Quadriere den Faktor.')
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


# ---------- UMBAU: neues Muster (Achte Runde, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl8.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl8 import mit_umbau  # noqa: E402

_K = lambda r, linien, **k: {'typ': 'figur', 'punkte': {'M': [0, 0], '_P': [r, 0], '_Q': [-r, 0]}, 'linien': linien, 'kreise': [{'m': 'M', 'r': r}], **k}
_SEK = {"M": [0, 0], "_s0": [6.0, 0.0], "_s1": [5.64, 2.05], "_s2": [4.6, 3.86], "_s3": [3.0, 5.2], "_s4": [1.04, 5.91], "_s5": [-1.04, 5.91], "_s6": [-3.0, 5.2]}
_ZY = {'_a': [0, 0], '_b': [12.57, 0], '_c': [12.57, 10], '_d': [0, 10], '_M': [2, 12], '_N': [2, -2]}
UMBAU = {
 'umfang': {
  'einstieg': 'Für eine Dose soll ein Etikett einmal herumreichen. Um eine Rundung misst du schlecht mit dem Lineal, aber du kannst rechnen. Die Länge einmal herum heißt ⟦Umfang⟧.',
  'woerter': [['Umfang', 'die Länge einmal um den Kreis'], ['Durchmesser', 'einmal quer durch die Mitte: d = 2r'], ['π', 'die Kreiszahl, etwa 3,14']],
  'bild': _K(4, [['M', '_P', 'r = 4 cm']]),
  'schritte': [{'text': 'Die Dose hat den Radius r = 4 cm.'},
               {'text': 'Der Durchmesser ist doppelt so lang: d = 8 cm.', 'bild': {'linien': [['_Q', '_P', 'd = 8 cm']]}},
               {'text': 'Der Umfang ist π-mal der Durchmesser: u = π · 8 cm.'},
               {'text': 'Mit π ≈ 3,14 gerechnet: u ≈ ⟦25,1 cm⟧.'}],
  'fehler': 'u = π · r ist falsch. Dann reicht das Etikett nur halb herum: 12,6 cm statt 25,1 cm. Man braucht den ⟦Durchmesser⟧.',
  'regel': 'Umfang: ⟦u = π · d = 2 · π · r⟧. Hast du den Radius, verdopple ihn zuerst.'},
 'flaeche': {
  'einstieg': 'Eine Pizzeria bietet Pizzen mit 30 cm Durchmesser an. Wie viel Pizza ist das? Gemeint ist die Fläche auf dem Teller, der ⟦Flächeninhalt⟧ des Kreises.',
  'woerter': [['Flächeninhalt', 'wie viel Platz eine Figur bedeckt'], ['r²', 'r mal r, gelesen „r Quadrat“'], ['≈', '„ungefähr gleich“']],
  'bild': _K(15, [['_Q', '_P', 'd = 30 cm']]),
  'schritte': [{'text': 'Durchmesser 30 cm, also Radius r = 15 cm.', 'bild': {'linien': [['M', '_P', 'r = 15 cm']]}},
               {'text': 'Zuerst quadrieren: r² = 15 · 15 = 225 cm².'},
               {'text': 'Dann mal π: A = π · 225 cm² ≈ ⟦706,9 cm²⟧.'}],
  'fehler': 'A = π · d² ist falsch: Das wären 2 827 cm², viermal zu viel. In die Formel gehört der ⟦Radius⟧.',
  'regel': 'Kreisfläche: ⟦A = π · r²⟧. Hast du den Durchmesser, halbiere ihn zuerst.'},
 'exakt': {
  'einstieg': 'π hat unendlich viele Nachkommastellen, jedes Runden macht ungenau. Lässt man π als Zeichen stehen, bleibt das Ergebnis genau, etwa 9π cm². So ein Ergebnis heißt ⟦exakt⟧.',
  'woerter': [['exakt', 'ganz genau, ohne Runden'], ['6π', '6 mal π – π bleibt als Zeichen stehen']],
  'bild': _K(3, [['M', '_P', 'r = 3 cm']]),
  'schritte': [{'text': 'Ein Kreis hat den Radius r = 3 cm.'},
               {'text': 'Umfang: 2 · π · 3 cm. Nur die Zahlen rechnen: ⟦u = 6π cm⟧.'},
               {'text': 'Fläche: π · 3² cm². Es ist 3² = 9, also ⟦A = 9π cm²⟧.'}],
  'fehler': 'A = 6π ist falsch: Da wurde 2 · 3 statt ⟦3²⟧ gerechnet. Das ist der Umfang, nicht die Fläche.',
  'regel': 'Exakt heißt: ⟦π als Zeichen stehen lassen⟧. Nur wenn eine Kommazahl gefragt ist, mit π ≈ 3,14 rechnen.'},
 'verstehen': {
  'einstieg': 'Gleicher Preis: eine große Pizza mit 30 cm Durchmesser oder zwei kleine mit je 20 cm. Zwei kleine klingt nach mehr. Entscheidend ist aber der ⟦Flächeninhalt⟧.',
  'woerter': [['Flächeninhalt', 'wie viel Pizza auf dem Teller liegt'], ['225π', '225 mal π']],
  'bild': {'typ': 'figur', 'punkte': {'_A': [0, 0], '_a': [15, 0], '_B': [28, 6], '_b': [38, 6], '_C': [28, -14], '_c': [38, -14]},
           'linien': [['_A', '_a', 'r = 15'], ['_B', '_b', 'r = 10'], ['_C', '_c', 'r = 10']], 'kreise': [{'m': '_A', 'r': 15}, {'m': '_B', 'r': 10}, {'m': '_C', 'r': 10}]},
  'schritte': [{'text': 'Groß: r = 15 cm, Fläche π · 15² = 225π cm².'},
               {'text': 'Klein: r = 10 cm, Fläche π · 10² = 100π cm².'},
               {'text': 'Zwei kleine zusammen: 2 · 100π = 200π cm².'},
               {'text': '225π ist mehr: ⟦Die große Pizza ist größer.⟧'}],
  'fehler': 'Doppelter Radius heißt nicht doppelte Fläche, sondern ⟦vierfache⟧: π · (2r)² = 4 · π · r².',
  'regel': 'Die Fläche wächst ⟦mit r²⟧. Doppelter Radius: doppelter Umfang, aber vierfache Fläche.'},
 'sektor': {
  'einstieg': 'Ein Tortenstück hat eine Spitze in der Mitte und einen gebogenen Rand. Wie viel Torte es ist, hängt vom Winkel an der Spitze ab. So ein Stück heißt ⟦Kreisausschnitt⟧.',
  'woerter': [['Kreisausschnitt', 'ein Tortenstück aus dem Kreis'], ['Mittelpunktswinkel α', 'der Winkel an der Spitze in der Mitte'], ['Bogen b', 'der gebogene Rand außen']],
  'bild': {"typ": "figur", "punkte": _SEK, "flaeche": list(_SEK), "linien": [["M", "_s0", "r = 6 cm"], ["M", "_s6"]], "winkel": [["M", "_s0", "_s6", "120°"]], "kreise": [{"m": "M", "r": 6}]},
  'schritte': [{'text': 'Tortenstück: r = 6 cm, Mittelpunktswinkel α = 120°.'},
               {'text': '120° von 360° ist 1/3 der Torte.'},
               {'text': 'Bogen b = 1/3 · 2π · 6 cm = 4π cm.'},
               {'text': 'Fläche: 1/3 · π · 6² = ⟦12π cm²⟧ ≈ 37,7 cm².'}],
  'fehler': 'Der Anteil von 90° ist nicht 90/100. Ein ganzer Kreis hat ⟦360°⟧, also 90/360 = 1/4.',
  'regel': 'Ausschnitt = ⟦α/360° vom ganzen Kreis⟧. Das gilt für den Bogen und für die Fläche.'},
 'zusammengesetzt': {
  'einstieg': 'Ein Donut ist ein großer Kreis, aus dem in der Mitte ein kleiner fehlt. Seine Fläche ist also groß minus klein. So eine Form heißt ⟦Kreisring⟧.',
  'woerter': [['Kreisring', 'großer Kreis ohne den kleinen Kreis in der Mitte'], ['R', 'der äußere Radius; r ist der innere']],
  'bild': {"typ": "figur", "punkte": {"M": [0, 0], "_P": [5, 0], "_Q": [0, 3]}, "linien": [["M", "_P", "R = 5 cm"], ["M", "_Q", "r = 3 cm"]], "kreise": [{"m": "M", "r": 5}, {"m": "M", "r": 3}]},
  'schritte': [{'text': 'Der Ring hat außen R = 5 cm und innen r = 3 cm.'},
               {'text': 'Groß: π · 5² = 25π cm². Klein: π · 3² = 9π cm².'},
               {'text': 'Abziehen: 25π − 9π = 16π cm² ≈ ⟦50,3 cm²⟧.'}],
  'fehler': 'π · (5 − 3)² = 4π ist falsch. Erst ⟦jeden⟧ Radius quadrieren, dann abziehen: π · (25 − 9).',
  'regel': 'Kreisring: ⟦großer Kreis minus kleiner Kreis⟧. Ein Kreisabschnitt bei 90° ist Viertelkreis minus Dreieck.'},
 'zylinder': {
  'einstieg': 'Wie viel passt in eine Dose, und wie viel Blech braucht sie? Die Dose ist wie ein Stapel dünner Kreisscheiben: Bodenfläche mal Höhe. Das ist ihr ⟦Volumen⟧.',
  'woerter': [['Volumen', 'der Rauminhalt: wie viel hineinpasst'], ['Oberfläche', 'Boden, Deckel und Mantel zusammen'], ['Mantel', 'die gebogene Seite – flach ist sie ein Rechteck']],
  'bild': {'typ': 'figur', 'punkte': _ZY, 'linien': [['_a', '_b', 'u ≈ 12,6 cm'], ['_b', '_c', 'h = 10 cm'], ['_c', '_d'], ['_d', '_a']], 'kreise': [{'m': '_M', 'r': 2}, {'m': '_N', 'r': 2}]},
  'schritte': [{'text': 'Eine Dose hat r = 2 cm und h = 10 cm.'},
               {'text': 'Volumen: π · 2² · 10 = 40π cm³ ≈ 125,7 cm³.'},
               {'text': 'Boden und Deckel: 2 · π · 2² = 8π cm².'},
               {'text': 'Mantel: 2 · π · 2 · 10 = 40π cm².', 'bild': {'flaeche': ['_a', '_b', '_c', '_d']}},
               {'text': 'Oberfläche: 8π + 40π = 48π cm² ≈ ⟦150,8 cm²⟧.'}],
  'fehler': 'Die Oberfläche ist nicht nur der Mantel. Es fehlen ⟦Boden und Deckel⟧, zusammen 2 · π · r².',
  'regel': 'Zylinder: ⟦V = π · r² · h⟧. Die Oberfläche ist O = 2πr² + 2πrh.'},
}
UMBAU_OFFEN = []
baue = mit_umbau(baue, UMBAU, UMBAU_OFFEN)


# ---- SCHWER (Zehnte Runde: schwerere Aufgaben nach Prüfungsvorbild, siehe _schwer_kl8.py) ----
# Vorbilder (Typ und Niveau, nicht Wortlaut/Zahlen): RS-Jahrgangsstufentest 8 2014 (zwei Pizzagrößen mit Preis vergleichen),
# VERA-8 2026 (Uferlänge/Fläche eines Sees mit Karte und Maßstab schätzen; bei gleichem Zaun größte Fläche), BMT10 2024 (Volumenterm eines Zylinders auswählen),
# BMT10 2021 (Wasserhöhe in einem Gefäß), BMT8 2025 (Maßstab: Flächen-/Volumenverhältnis), Känguru Kl. 7/8 (Kreisteile in Quadraten, Seil um eine Kugel).
from _schwer_kl8 import Neu, mit_schwer  # noqa: E402
from _bausatz import PI  # noqa: E402

SW = Neu(10_8_10)
T1, T01 = 0.1, 0.01

# umfang
SW.z('umfang', 2, 'Ein Kreis hat den Umfang 50 cm. Berechne den Durchmesser. Runde auf eine Nachkommastelle.', 15.9, f'50 / {PI}', 'd = u : π = 50 : π ≈ 15,9 cm.',
     'u = π · d. Stelle nach d um.', einheit='cm', toleranz=T1)
SW.z('umfang', 2, 'Eine runde Tischdecke mit 1,4 m Durchmesser bekommt rundherum eine Borte. Wie viele Meter Borte braucht man? Runde auf zwei Nachkommastellen.', 4.40, f'{PI} * 1.4',
     'u = π · d = π · 1,4 m ≈ 4,40 m.', 'Die Borte ist so lang wie der Umfang.', einheit='m', toleranz=T01)
SW.z('umfang', 3, 'Ein See ist auf einer Karte im Maßstab 1 : 50 000 ungefähr ein Kreis mit 8 cm Durchmesser. Wie lang ist sein Ufer in Wirklichkeit ungefähr? Runde auf eine Nachkommastelle.',
     12.6, f'{PI} * 8 * 50000 / 100000', 'Wirklicher Durchmesser: 8 cm · 50 000 = 400 000 cm = 4 km. Ufer ≈ π · 4 km ≈ 12,6 km.',
     'Rechne zuerst den echten Durchmesser in km aus.', einheit='km', toleranz=T1, art='P')
SW.z('umfang', 3, 'An einem Riesenrad hängen 20 Gondeln in gleichen Abständen. Entlang des Rands sind zwei Gondeln 9,4 m voneinander entfernt. Welchen Durchmesser hat das Rad etwa? Runde auf ganze Meter.',
     60, f'20 * 9.4 / {PI}', 'Umfang ≈ 20 · 9,4 m = 188 m. d = u : π = 188 : π ≈ 59,8 m, also etwa 60 m.', 'Wie lang ist der ganze Rand?', einheit='m', toleranz=1, art='P')
SW.z('umfang', 3, 'Ein Seil liegt straff um einen Ball mit Radius 10 cm. Es wird um 1 m verlängert und so gelegt, dass es überall gleich weit vom Ball absteht. Wie groß ist dieser Abstand? Runde auf eine Nachkommastelle.',
     15.9, f'100 / (2 * {PI})', 'Neuer Umfang = alter Umfang + 100 cm. Da u = 2πr, wächst r um 100 : (2π) ≈ 15,9 cm – egal wie groß der Ball ist.',
     'Wie ändert sich r, wenn u um 100 cm wächst?', einheit='cm', toleranz=T1, art='K')
SW.a('umfang', 3, 'Was ist länger: der Umfang eines Kreises mit d = 10 cm oder die Umfänge von zwei Kreisen mit je d = 5 cm zusammen?', 'Beide sind gleich lang.',
     ['der große Kreis', 'die zwei kleinen Kreise', 'Das kann man ohne π nicht sagen.'],
     'Großer Kreis: π · 10. Zwei kleine: 2 · π · 5 = π · 10. Der Umfang ist proportional zum Durchmesser.', 'Rechne beide Umfänge mit π als Zeichen aus.', art='K')

# flaeche
SW.z('flaeche', 2, 'Ein runder Teppich hat den Durchmesser 2,4 m. Berechne seine Fläche. Runde auf zwei Nachkommastellen.', 4.52, f'{PI} * 1.2**2', 'r = 1,2 m. A = π · 1,2² ≈ 4,52 m².',
     'Erst den Radius bestimmen.', einheit='m²', toleranz=T01)
SW.a('flaeche', 2, 'Was ist größer: ein Quadrat mit 4 cm Seitenlänge oder ein Kreis mit 2,5 cm Radius?', 'der Kreis', ['das Quadrat', 'Beide sind gleich groß.'],
     'Quadrat: 16 cm². Kreis: π · 2,5² ≈ 19,6 cm². Der Kreis ist größer.', 'Berechne beide Flächen.')
SW.a('flaeche', 3, 'Kleine Pizza: 26 cm Durchmesser für 7 €. Große Pizza: 39 cm Durchmesser für 14 €. Wo bekommst du mehr Pizza pro Euro?', 'bei der großen (etwa 85 cm² pro €)',
     ['bei der kleinen (etwa 76 cm² pro €)', 'gleich viel, weil die große doppelt so viel kostet', 'bei der kleinen, weil 39 cm nicht das Doppelte von 26 cm ist'],
     'Klein: π · 13² ≈ 531 cm², 531 : 7 ≈ 76 cm² pro €. Groß: π · 19,5² ≈ 1 195 cm², 1 195 : 14 ≈ 85 cm² pro €. Die große lohnt sich mehr.',
     'Berechne beide Flächen und teile durch den Preis.', art='P')
SW.z('flaeche', 3, 'Mit 20 m Zaun soll ein Beet eingezäunt werden – als Quadrat oder als Kreis. Wie viele m² Fläche hat der Kreis mehr? Runde auf eine Nachkommastelle.', 6.8,
     f'(20 / (2 * {PI}))**2 * {PI} - 5**2', 'Quadrat: Seite 5 m, A = 25 m². Kreis: r = 20 : (2π) ≈ 3,18 m, A ≈ 31,8 m². Unterschied ≈ 6,8 m².',
     'Bestimme beim Kreis zuerst den Radius aus dem Umfang.', einheit='m²', toleranz=T1, art='P')
SW.z('flaeche', 3, 'In einen Kreis mit r = 6 cm legt man zwei Kreise mit r = 3 cm nebeneinander. Welcher Anteil des großen Kreises bleibt frei? Gib ihn als Dezimalzahl an.', 0.5,
     '(36 - 2 * 9) / 36', 'Großer Kreis: 36π. Kleine Kreise: 2 · 9π = 18π. Frei: 18π, also 18π : 36π = 0,5 – die Hälfte.', 'Rechne mit π als Zeichen. Es kürzt sich weg.', art='K')
SW.z('flaeche', 3, 'Bei einem Kreis haben Umfang (in cm) und Flächeninhalt (in cm²) dieselbe Maßzahl. Wie groß ist sein Radius?', 2, '2',
     '2 · π · r = π · r². Teilen durch π · r: 2 = r. Probe: u = 4π, A = 4π.', 'Setze die Formeln gleich und teile durch π · r.', einheit='cm', art='K')

# exakt
SW.z('exakt', 2, 'Ein Kreis hat den Durchmesser 9 cm. Gib den Umfang exakt an: u = □ · π cm. Welche Zahl gehört in das Kästchen?', 9, '9', 'u = π · d = 9π cm.',
     'Mit dem Durchmesser ist u = π · d.')
SW.z('exakt', 2, 'Ein Kreis hat den Flächeninhalt 49π cm². Wie groß ist sein Durchmesser?', 14, '2 * 7', 'r² = 49 ⇔ r = 7 cm. d = 14 cm.', 'Erst r aus r² = 49, dann verdoppeln.', einheit='cm')
SW.l('exakt', 3, 'Eine Figur besteht aus einem Quadrat (Seite 8 cm) und einem aufgesetzten Halbkreis über der oberen Seite. Gib den Umfang der Figur exakt an.', 'u = □ + □ · π cm',
     [24, 4], ['3 * 8', '8 / 2'], 'Drei Quadratseiten: 3 · 8 = 24 cm (die obere liegt innen). Halbkreisbogen: π · 8 : 2 = 4π cm. u = 24 + 4π cm.',
     'Welche Seiten gehören zum Rand? Der Halbkreis hat den halben Umfang eines Kreises mit d = 8 cm.', 'Je Lücke eine ganze Zahl.', art='P')
SW.l('exakt', 3, 'Dieselbe Figur (Quadrat mit Seite 8 cm, oben ein Halbkreis): Gib den Flächeninhalt exakt an.', 'A = □ + □ · π cm²', [64, 8], ['8 * 8', '4**2 / 2'],
     'Quadrat: 64 cm². Halbkreis mit r = 4 cm: π · 16 : 2 = 8π cm². A = 64 + 8π cm².', 'Der Radius des Halbkreises ist 4 cm.', 'Je Lücke eine ganze Zahl.', art='P')
SW.z('exakt', 3, 'Ein Kreis hat den Umfang 12π cm. Ein zweiter Kreis hat doppelt so viel Fläche. Gib die Fläche des zweiten Kreises exakt an: A = □ · π cm². Welche Zahl?', 72, '2 * 6**2',
     'r = 6 cm, A₁ = 36π cm². Doppelte Fläche: 72π cm². (Achtung: nicht den Radius verdoppeln – das gäbe die vierfache Fläche.)', 'Bestimme zuerst A₁.', art='K')
SW.z('exakt', 3, 'Ein Draht der Länge 8π cm wird zu einem Quadrat gebogen. Gib die Seitenlänge exakt an: s = □ · π cm. Welche Zahl?', 2, '8 / 4',
     'Der Draht ist der Umfang: 4 · s = 8π cm ⇔ s = 2π cm (≈ 6,28 cm).', 'π bleibt als Zeichen stehen, du teilst nur die Zahl davor.', art='K')

# verstehen
SW.z('verstehen', 2, 'Der Durchmesser eines Kreises wird halbiert. Mit welchem Faktor ändert sich der Flächeninhalt?', 0.25, '0.5**2', 'Halber Durchmesser heißt halber Radius: Fläche · 0,5² = · 0,25.',
     'Die Fläche hängt von r² ab.')
SW.z('verstehen', 2, 'Der Umfang eines Kreises wird verdoppelt. Mit welchem Faktor ändert sich der Flächeninhalt?', 4, '2**2', 'Doppelter Umfang heißt doppelter Radius. Fläche · 2² = · 4.',
     'Was passiert mit r, wenn u doppelt so groß wird?')
SW.a('verstehen', 3, 'Eine Pizza mit 30 cm Durchmesser kostet doppelt so viel wie eine mit 15 cm. Ist die große Pizza günstiger?', 'Ja: Sie hat die vierfache Fläche zum doppelten Preis.',
     ['Nein: Doppelter Preis für doppelte Größe ist gleich teuer.', 'Nein: Die kleine hat mehr Rand.', 'Das kann man ohne π nicht sagen.'],
     'Doppelter Durchmesser gibt 2² = 4-fache Fläche. Für den doppelten Preis bekommt man also viermal so viel Pizza.', 'Wie ändert sich die Fläche bei doppeltem Durchmesser?', art='P')
SW.z('verstehen', 3, 'Ein runder Turm wird im Maßstab 1 : 50 als Modell gebaut. Wie viel Mal so groß ist die Grundfläche des echten Turms?', 2500, '50**2',
     'Jede Länge ist 50-mal so groß, also auch der Radius. Fläche: 50² = 2 500-mal so groß.', 'Die Fläche hängt vom Quadrat des Radius ab.', art='P')
SW.z('verstehen', 3, 'Der Radius eines Kreises wächst um 10 %. Um wie viel Prozent wächst sein Flächeninhalt?', 21, '(1.1**2 - 1) * 100',
     'Neuer Radius 1,1 · r. Fläche · 1,1² = · 1,21. Das ist ein Zuwachs um 21 %, nicht um 10 % oder 20 %.', 'Rechne mit dem Faktor 1,1.', einheit='%', art='K')
SW.z('verstehen', 3, 'Der Radius eines Kreises wird um 1 cm vergrößert. Um wie viel wächst der Umfang? Runde auf zwei Nachkommastellen.', 6.28, f'2 * {PI} * 1',
     'u = 2πr. Neuer Umfang 2π(r + 1) = 2πr + 2π. Er wächst um 2π ≈ 6,28 cm – bei jedem Kreis, egal wie groß.', 'Rechne 2π(r + 1) aus.', einheit='cm', toleranz=T01, art='K')

# sektor
SW.z('sektor', 2, 'Ein Kreisausschnitt hat r = 10 cm und α = 36°. Berechne die Bogenlänge. Runde auf eine Nachkommastelle.', 6.3, f'2 * {PI} * 10 * 36 / 360',
     'b = 2π · 10 · 36/360 = 2π ≈ 6,3 cm.', '36° ist ein Zehntel des Vollkreises.', einheit='cm', toleranz=T1)
SW.z('sektor', 2, 'Eine Pizza mit 30 cm Durchmesser wird in 8 gleiche Stücke geschnitten. Wie groß ist ein Stück? Runde auf eine Nachkommastelle.', 88.4, f'{PI} * 15**2 / 8',
     'Ganze Pizza: π · 15² ≈ 706,9 cm². Ein Achtel ≈ 88,4 cm².', 'Radius 15 cm. Dann durch 8.', einheit='cm²', toleranz=T1)
SW.z('sektor', 3, 'Der Minutenzeiger einer Uhr ist 12 cm lang. Welchen Weg legt seine Spitze in 20 Minuten zurück? Runde auf eine Nachkommastelle.', 25.1, f'2 * {PI} * 12 / 3',
     '20 Minuten sind ein Drittel der Stunde (120°). Weg = 2π · 12 : 3 = 8π ≈ 25,1 cm.', 'Welcher Teil des Kreises ist das?', einheit='cm', toleranz=T1, art='P')
SW.z('sektor', 3, 'In einem Kreisdiagramm stehen 15 % für „Bus“. Wie groß ist der Mittelpunktswinkel dieses Kreisausschnitts?', 54, '0.15 * 360',
     '15 % von 360° = 0,15 · 360° = 54°.', 'Der ganze Kreis sind 100 % = 360°.', einheit='°', art='P')
SW.z('sektor', 3, 'Ein Kreisausschnitt mit r = 6 cm hat denselben Flächeninhalt wie ein ganzer Kreis mit r = 2 cm. Wie groß ist sein Mittelpunktswinkel?', 40, '4 / 36 * 360',
     'Kleiner Kreis: 4π. Großer Kreis: 36π. Anteil 4π : 36π = 1/9. α = 360° : 9 = 40°.', 'Rechne mit π als Zeichen.', einheit='°', art='K')
SW.z('sektor', 3, 'Ein Viertelkreis hat r = 4 cm. Wie lang ist sein ganzer Rand (Bogen und beide Radien)? Runde auf eine Nachkommastelle.', 14.3, f'2 * {PI} * 4 / 4 + 2 * 4',
     'Bogen: 2π · 4 : 4 = 2π ≈ 6,28 cm. Dazu zwei Radien: 8 cm. Rand ≈ 14,3 cm.', 'Der Rand besteht nicht nur aus dem Bogen.', einheit='cm', toleranz=T1, art='K')

# zusammengesetzt
SW.z('zusammengesetzt', 2, 'Ein Kreisring hat den Außendurchmesser 10 cm und den Innendurchmesser 6 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 50.3,
     f'{PI} * (5**2 - 3**2)', 'Radien 5 cm und 3 cm. A = π · (25 − 9) = 16π ≈ 50,3 cm².', 'Achtung: Durchmesser gegeben – erst halbieren.', einheit='cm²', toleranz=T1)
SW.z('zusammengesetzt', 2, 'Ein Halbkreis hat den Durchmesser 12 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 56.5, f'{PI} * 6**2 / 2',
     'r = 6 cm. Halber Kreis: π · 36 : 2 ≈ 56,5 cm².', 'Radius bestimmen, Kreisfläche halbieren.', einheit='cm²', toleranz=T1)
SW.z('zusammengesetzt', 3, 'Ein Fenster besteht aus einem Rechteck (1 m breit, 1,5 m hoch) mit einem aufgesetzten Halbkreis (Durchmesser 1 m). Berechne die Glasfläche. Runde auf zwei Nachkommastellen.',
     1.89, f'1 * 1.5 + {PI} * 0.5**2 / 2', 'Rechteck: 1,5 m². Halbkreis: π · 0,5² : 2 ≈ 0,39 m². Zusammen ≈ 1,89 m².', 'Zerlege in Rechteck und Halbkreis.',
     einheit='m²', toleranz=T01, art='P')
SW.z('zusammengesetzt', 3, 'Ein Sportplatz besteht aus einem Rechteck (80 m × 60 m) und je einem Halbkreis an den beiden 60-m-Seiten. Wie groß ist die Rasenfläche? Runde auf ganze m².', 7627,
     f'80 * 60 + {PI} * 30**2', 'Die zwei Halbkreise (r = 30 m) ergeben zusammen einen Kreis: π · 900 ≈ 2 827 m². Dazu 4 800 m². Gesamt ≈ 7 627 m².',
     'Zwei Halbkreise sind ein ganzer Kreis.', einheit='m²', toleranz=1, art='P')
SW.z('zusammengesetzt', 3, 'In einem Quadrat mit Seitenlänge 10 cm wird an jeder Ecke ein Viertelkreis mit Radius 5 cm ausgeschnitten. Wie groß ist die Restfläche? Runde auf eine Nachkommastelle.', 21.5,
     f'100 - {PI} * 25', 'Vier Viertelkreise mit r = 5 cm sind zusammen ein ganzer Kreis: 25π ≈ 78,5 cm². Rest: 100 − 78,5 ≈ 21,5 cm².', 'Wie viele ganze Kreise ergeben die vier Viertel?',
     einheit='cm²', toleranz=T1, grafik={'typ': 'figur', 'punkte': {'A': [0, 0], 'B': [10, 0], 'C': [10, 10], 'D': [0, 10]}, 'flaeche': ['A', 'B', 'C', 'D'],
                                        'linien': [['A', 'B', '10 cm']], 'kreise': [{'m': 'A', 'r': 5}, {'m': 'B', 'r': 5}, {'m': 'C', 'r': 5}, {'m': 'D', 'r': 5}]}, art='K')
SW.z('zusammengesetzt', 3, 'Zwei Kreise mit r = 2 cm liegen nebeneinander und berühren sich. Ein Rechteck umschließt beide genau. Wie groß ist die Fläche im Rechteck außerhalb der Kreise? Runde auf eine Nachkommastelle.',
     6.9, f'8 * 4 - 2 * {PI} * 4', 'Rechteck: 8 cm × 4 cm = 32 cm². Kreise: 2 · π · 4 = 8π ≈ 25,1 cm². Rest ≈ 6,9 cm².', 'Wie lang und wie breit ist das Rechteck?', einheit='cm²', toleranz=T1, art='K')

# zylinder
SW.z('zylinder', 2, 'Eine Dose hat den Durchmesser 8 cm und die Höhe 11 cm. Berechne ihr Volumen. Runde auf ganze cm³.', 553, f'{PI} * 4**2 * 11', 'V = π · 4² · 11 ≈ 552,9 ≈ 553 cm³.',
     'Erst den Radius bestimmen.', einheit='cm³', toleranz=1)
SW.z('zylinder', 2, 'Eine Litfaßsäule (Zylinder) hat den Durchmesser 1,2 m und ist 3 m hoch. Nur die Mantelfläche wird beklebt. Wie viel m² sind das? Runde auf eine Nachkommastelle.', 11.3,
     f'{PI} * 1.2 * 3', 'Mantel = Umfang · Höhe = π · 1,2 · 3 ≈ 11,3 m².', 'Der Mantel ist ein aufgerolltes Rechteck: Umfang mal Höhe.', einheit='m²', toleranz=T1)
SW.a('zylinder', 3, 'Ein Zylinder hat den Durchmesser 6 cm und die Höhe 10 cm. Welcher Term gibt sein Volumen an?', 'π · 3² · 10', ['π · 6² · 10', '2 · π · 3 · 10', 'π · 6 · 10'],
     'V = π · r² · h mit r = 3 cm: π · 3² · 10 = 90π cm³. 2 · π · 3 · 10 ist die Mantelfläche, π · 6² · 10 nimmt den Durchmesser statt des Radius.',
     'Welcher Term enthält r² und h?', art='P')
SW.z('zylinder', 3, 'Ein zylinderförmiges Glas hat innen den Radius 3 cm und ist 8 cm hoch mit Wasser gefüllt. Man gießt 100 cm³ dazu. Um wie viel cm steigt der Wasserspiegel? Runde auf eine Nachkommastelle.',
     3.5, f'100 / ({PI} * 9)', 'Grundfläche: π · 3² ≈ 28,3 cm². Anstieg: 100 : 28,3 ≈ 3,5 cm. Die 8 cm braucht man nicht.', 'Das zusätzliche Wasser bildet einen flachen Zylinder.',
     einheit='cm', toleranz=T1, art='P')
SW.a('zylinder', 3, 'Zylinder A hat r = 2 cm und h = 8 cm. Zylinder B hat r = 4 cm und h = 2 cm. Welcher hat das größere Volumen?', 'Beide sind gleich groß.',
     ['A, weil er höher ist.', 'B, weil er breiter ist.', 'Das kann man ohne Taschenrechner nicht sagen.'],
     'A: π · 4 · 8 = 32π. B: π · 16 · 2 = 32π. Doppelter Radius vervierfacht die Grundfläche, ein Viertel der Höhe gleicht das aus.', 'Rechne mit π als Zeichen.', art='K')
SW.a('zylinder', 3, 'Ein Blatt (20 cm × 30 cm) wird zu einem Zylindermantel gerollt: einmal mit der 30-cm-Seite als Umfang (Höhe 20 cm), einmal mit der 20-cm-Seite als Umfang (Höhe 30 cm). Welcher Zylinder fasst mehr?',
     'der mit 30 cm Umfang', ['der mit 20 cm Umfang', 'Beide fassen gleich viel, das Blatt ist dasselbe.', 'Das hängt vom Material ab.'],
     'Umfang 30: r ≈ 4,77 cm, V ≈ π · 22,8 · 20 ≈ 1 432 cm³. Umfang 20: r ≈ 3,18 cm, V ≈ π · 10,1 · 30 ≈ 955 cm³. Der Radius geht quadratisch ein.',
     'Bestimme jeweils r aus dem Umfang und vergleiche π · r² · h.', art='K')

baue = mit_schwer(baue, SW)
# ---- SCHWER ENDE ----

# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, mit_befunden  # noqa: E402

BF = Befunde('messen.kreisberechnung', 13_8_10)
# b) gerundetes Ergebnis ohne Toleranz und ohne Einheit
BF.loesung('sektor', 'Ein Kreisausschnitt hat den Mittelpunktswinkel 30°. Wie viel Prozent des Kreises sind das? (Runde auf eine Nachkommastelle.)',
           o={'wert': 8.3, 'einheit': '%', 'toleranz': 0.1})
# a) gleicher Typ wie Stufe 1 bzw. 2
BF.stufe('umfang', 'Ein Kreis hat den Durchmesser 43,2 cm. Berechne den Umfang. Runde auf eine Nachkommastelle.', 1)
for _t in ['Ein Zylinder hat r = 7,4 cm und h = 28,7 cm. Berechne seine Oberfläche. Runde auf eine Nachkommastelle.',
           'Ein Zylinder hat r = 9 cm und h = 2,3 cm. Berechne seine Oberfläche. Runde auf eine Nachkommastelle.',
           'Ein Zylinder hat r = 1,6 cm und h = 7,5 cm. Berechne seine Oberfläche. Runde auf eine Nachkommastelle.']:
    BF.stufe('zylinder', _t, 2)
BF.nicht_umgesetzt('flaeche S3 Pizzavergleich (3×)', 'Kein Fehler; Übungsreihe zum selben Typ mit verschiedenen Zahlen, Ablenker gut.')
BF.nicht_umgesetzt('verstehen S2 „Jemand rechnet A = 2 · π · r …“ (3×)', 'Kein Fehler; Übungsreihe mit verschiedenen Zahlen.')

baue = mit_befunden(baue, BF)
# ---- BEFUNDE ENDE ----

# ---- LÜCKEN (Achtzehnte Runde, Teil B: Karte „umfang“ um den Schritt „Warum etwa 3,14?“ erweitert, siehe _luecken_kl8.py) ----
# LehrplanPLUS M8 7: Kreiszahl π näherungsweise bestimmen (Messen; Vielecke innen und außen). Liste klasse8.json, Dringlichkeit niedrig.
from _bausatz import Z as _Z  # noqa: E402
from _luecken_kl8 import Luecken, mit_luecken  # noqa: E402

LK = Luecken('messen.kreisberechnung', 18_8_7)
_H = 3.464  # 4 · √3/2, Ecken des Sechsecks im Kreis mit r = 4
_SCHRITT_PI = {
    'text': 'Warum etwa 3,14? Sechseck innen hat 3 · d, Quadrat außen 4 · d.',
    'bild': {'typ': 'figur', 'kreise': [{'m': 'M', 'r': 4}],
             'punkte': {'M': [0, 0], '_S1': [4, 0], '_S2': [2, _H], '_S3': [-2, _H], '_S4': [-4, 0], '_S5': [-2, -_H], '_S6': [2, -_H],
                        '_Q1': [4, 4], '_Q2': [-4, 4], '_Q3': [-4, -4], '_Q4': [4, -4]},
             'linien': [['_S1', '_S2'], ['_S2', '_S3'], ['_S3', '_S4'], ['_S4', '_S5'], ['_S5', '_S6'], ['_S6', '_S1', 'innen: 3 · d'],
                        ['_Q1', '_Q2'], ['_Q2', '_Q3'], ['_Q3', '_Q4'], ['_Q4', '_Q1', 'außen: 4 · d', 'gestrichelt']]},
}
_AUF = [
    ('uebung', 1, lambda: _Z('Um einen runden Teller wird ein Faden gelegt: 75,4 cm. Der Durchmesser ist 24 cm. Welchen Näherungswert für π ergibt das? Runde auf zwei Nachkommastellen.',
                             Fr(157, 50), 'round(754 / 240, 2)', 'π = Umfang : Durchmesser = 75,4 : 24 ≈ 3,1417 ≈ 3,14.',
                             'π ist das Verhältnis von Umfang zu Durchmesser.', toleranz=0.01)),
    ('uebung', 1, lambda: _Z('Um einen Kreis mit d = 6 cm liegt ein Quadrat, das ihn außen berührt. Wie lang ist der Umfang des Quadrats?', 24, '4 * 6',
                             'Jede Quadratseite ist so lang wie der Durchmesser: 4 · 6 cm = 24 cm. Der Kreisumfang (≈ 18,8 cm) ist kürzer.',
                             'Wie lang ist eine Seite des Quadrats im Vergleich zum Durchmesser?', einheit='cm')),
    ('uebung', 2, lambda: _Z('In einen Kreis mit r = 5 cm ist ein regelmäßiges Sechseck gezeichnet. Seine Seiten sind so lang wie der Radius. Wie lang ist sein Umfang?', 30, '6 * 5',
                             '6 Seiten zu je 5 cm: 30 cm. Das sind 3 · d (d = 10 cm). Der Kreis ist etwas länger, π ist also größer als 3.',
                             'Ein regelmäßiges Sechseck im Kreis besteht aus 6 gleichseitigen Dreiecken.', einheit='cm')),
    ('uebung', 2, lambda: LK.A('Ein Sechseck innen im Kreis hat den Umfang 3 · d, ein Quadrat außen herum 4 · d. Was folgt daraus für π?', 'π liegt zwischen 3 und 4.',
                               ['π ist genau 3,5.', 'π ist kleiner als 3.', 'π ist größer als 4.'],
                               'Der Kreis liegt zwischen den beiden Vielecken, also ist sein Umfang länger als 3 · d und kürzer als 4 · d. π liegt zwischen 3 und 4; genauer ist π ≈ 3,14.',
                               'Welche Figur ist länger, welche kürzer als der Kreis?')),
    ('uebung', 3, lambda: _Z('Ein Fahrradreifen hat 70 cm Durchmesser. Bei einer Umdrehung rollt das Rad 2,20 m weit. Welchen Näherungswert für π ergibt das? Runde auf zwei Nachkommastellen.',
                             Fr(157, 50), 'round(220 / 70, 2)', 'Eine Umdrehung ist ein Umfang: 220 cm. π ≈ 220 : 70 ≈ 3,1429 ≈ 3,14. Gleiche Einheit verwenden: 2,20 m = 220 cm.',
                             'Rechne beide Längen in cm. Was legt das Rad bei einer Umdrehung zurück?', toleranz=0.01)),
    ('uebung', 3, lambda: LK.A('Ein regelmäßiges Achteck innen im Kreis hat etwa den Umfang 3,06 · d. Jemand behauptet: „π = 3 genügt doch.“ Was stimmt?',
                               'Nein: Schon das Achteck innen ist länger als 3 · d, der Kreis ist noch länger.',
                               ['Ja: 3,06 ist fast 3.', 'Ja: Das Sechseck hat genau 3 · d.', 'Nein: π ist größer als 4.'],
                               'Je mehr Ecken das innere Vieleck hat, desto näher kommt sein Umfang an den Kreis: 3 · d (Sechseck), 3,06 · d (Achteck), … bis π · d ≈ 3,14 · d. '
                               'π ist also sicher größer als 3,06.', 'Liegt der Kreis innerhalb oder außerhalb des Achtecks? Welche Linie ist dann länger?')),
]
LK.erweitere('umfang', 4, _SCHRITT_PI, _AUF)
baue = mit_luecken(baue, LK)
# ---- LÜCKEN ENDE ----


# ---- DURCHSICHT (Neunzehnte Runde, Teil A: Gesamtdurchsicht Kl. 8, siehe _durchsicht_kl8.py) ----
from _durchsicht_kl8 import Durchsicht, mit_durchsicht  # noqa: E402

DSX = Durchsicht('messen.kreisberechnung', 19_8_12)
# Gleiche Aufgabenart wie die Stufe darunter → umgestuft
DSX.stufe('umfang', 'Ein Kreis hat den Durchmesser 36 cm. Berechne den Umfang. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('umfang', 'Ein Kreis hat den Durchmesser 3,4 cm. Berechne den Umfang. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('umfang', 'Berechne den Umfang eines Kreises mit r = 9,2 cm. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('umfang', 'Du misst bei einem Eimer den Umfang u = 94,2 cm und den Durchmesser d = 30 cm. Was ergibt u : d ungefähr?', 1)
DSX.stufe('umfang', 'Ein Kreis hat den Umfang 74,8 cm. Berechne den Radius. Runde auf eine Nachkommastelle.', 2)
DSX.stufe('flaeche', 'Berechne den Flächeninhalt eines Kreises mit r = 17 cm. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('flaeche', 'Berechne den Flächeninhalt eines Kreises mit r = 12 cm. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('flaeche', 'Berechne den Flächeninhalt eines Kreises mit r = 2 cm. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('flaeche', 'Berechne den Flächeninhalt eines Kreises mit r = 14 cm. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('flaeche', 'Ein Kreis hat den Flächeninhalt 36π cm². Wie groß ist sein Radius?', 2)
DSX.stufe('exakt', 'Ein Kreis hat den Durchmesser 9 cm. Gib den Umfang exakt an: u = □ · π cm. Welche Zahl gehört in das Kästchen?', 1)
DSX.stufe('sektor', 'Ein Kreisausschnitt hat r = 1,9 cm und α = 210°. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 2)
DSX.stufe('zusammengesetzt', 'Ein Kreisring hat den Außenradius 11 cm und den Innenradius 7 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zusammengesetzt', 'Ein Kreisring hat den Außenradius 15 cm und den Innenradius 12 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zusammengesetzt', 'Ein Kreisring hat den Außenradius 14 cm und den Innenradius 12 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zusammengesetzt', 'Ein Kreisring hat den Außenradius 15 cm und den Innenradius 13 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zylinder', 'Ein Zylinder hat r = 4 cm und h = 7 cm. Berechne seine Mantelfläche. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zylinder', 'Ein Zylinder hat r = 5 cm und h = 7 cm. Berechne seine Mantelfläche. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zylinder', 'Ein Zylinder hat r = 1 cm und h = 5 cm. Berechne sein Volumen. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zylinder', 'Ein Zylinder hat r = 4 cm und h = 4 cm. Berechne sein Volumen. Runde auf eine Nachkommastelle.', 1)
DSX.stufe('zylinder', 'Ein Regenfass mit r = 35 cm enthält 250 l Wasser. Wie hoch steht das Wasser? Runde auf eine Nachkommastelle.', 2)
# flaeche: Stufe 2 war nur „r einsetzen“ wie Stufe 1 → Umkehrung und Verknüpfung; dreimal Pizza-Vergleich → einer ersetzt
DSX.ersetze('flaeche', 'Berechne den Flächeninhalt eines Kreises mit r = 4,5 cm. Runde auf eine Nachkommastelle.', DSX.Z(
    'Ein runder Teich hat den Flächeninhalt 78,5 m². Wie groß ist sein Radius? Runde auf eine Nachkommastelle.', 5, '5',
    'A = π · r², also r² = 78,5 : π ≈ 25. Die Zahl, die mit sich selbst malgenommen 25 ergibt, ist 5. Der Radius ist etwa 5,0 m.',
    'Rechne rückwärts: erst durch π teilen, dann die Zahl suchen, deren Quadrat herauskommt.', einheit='m', toleranz=0.1))
DSX.ersetze('flaeche', 'Berechne den Flächeninhalt eines Kreises mit r = 9,5 cm. Runde auf eine Nachkommastelle.', DSX.Z(
    'Ein Kreis hat den Umfang 31,4 cm. Berechne seinen Flächeninhalt. Runde auf eine Nachkommastelle.', 78.5, 'round(31.4 * 31.4 / (4 * 3.14159265), 1)',
    'Aus dem Umfang den Radius: r = 31,4 : (2 · π) ≈ 5 cm. Dann A = π · r² ≈ π · 25 ≈ 78,5 cm².',
    'Berechne zuerst den Radius aus dem Umfang.', einheit='cm²', toleranz=0.1))
DSX.ersetze('flaeche', 'Eine Pizza mit 32 cm Durchmesser kostet 10 €, zwei Pizzen mit je 22 cm kosten zusammen auch 10 €. Wo bekommst du mehr Pizza?', DSX.Z(
    'Ein Kreis soll genauso viel Fläche haben wie ein Quadrat mit 10 cm Seitenlänge. Welchen Radius braucht er? Runde auf eine Nachkommastelle.', 5.6, '5.6',
    'Das Quadrat hat 100 cm². Also π · r² = 100, r² = 100 : π ≈ 31,8. Da 5,6 · 5,6 ≈ 31,4 und 5,7 · 5,7 ≈ 32,5 sind, ist r ≈ 5,6 cm.',
    'Setze π · r² gleich der Quadratfläche und rechne rückwärts.', einheit='cm', toleranz=0.1))
# exakt: dreimal Kreisring in Folge → einer ersetzt durch Fehler finden
DSX.ersetze('exakt', 'Ein Kreisring hat den Außenradius 12 cm und den Innenradius 8 cm. Gib den Flächeninhalt exakt an: A = □ · π cm².', DSX.Z(
    'Lea rechnet für einen Kreis mit d = 10 cm: A = π · 10² = 100π cm². Berichtige: A = □ · π cm². Welche Zahl gehört in das Kästchen?', 25, '(10 / 2) ** 2',
    'Lea hat den Durchmesser quadriert. Richtig ist der Radius r = 5 cm: A = π · 5² = 25π cm².', 'In die Flächenformel gehört der Radius.'))
# verstehen: dreimal derselbe Formelfehler, viermal derselbe Vergleich → ersetzt
DSX.ersetze('verstehen', 'Ein Kreis hat r = 2 cm. Jemand rechnet A = 2 · π · 2. Was ist der Fehler?', DSX.Z(
    'Ein Kreis hat den Flächeninhalt 20 cm². Sein Radius wird verdoppelt. Wie groß ist der neue Flächeninhalt?', 80, '20 * 2 ** 2',
    'Doppelter Radius heißt vierfache Fläche: 4 · 20 cm² = 80 cm².', 'Die Fläche wächst mit r².', einheit='cm²'))
DSX.ersetze('verstehen', 'Welcher Kreis hat den größeren Flächeninhalt: einer mit r = 7 cm oder einer mit u = 65 cm?', DSX.Z(
    'Ein Kreis soll doppelt so viel Fläche bekommen. Mit welcher Zahl muss man seinen Radius malnehmen? Runde auf zwei Nachkommastellen.', 1.41, '1.41',
    'Die Fläche wächst mit dem Quadrat des Faktors. Gesucht ist k mit k · k = 2: 1,41 · 1,41 ≈ 1,99, 1,42 · 1,42 ≈ 2,02. Also k ≈ 1,41 – nicht 2.',
    'Welche Zahl ergibt mit sich selbst malgenommen 2?', toleranz=0.01))
DSX.ersetze('verstehen', 'Welcher Kreis hat den größeren Flächeninhalt: einer mit r = 4 cm oder einer mit u = 79 cm?', DSX.Z(
    'Ein großer Kreis hat 9-mal so viel Fläche wie ein kleiner Kreis mit r = 2 cm. Welchen Radius hat der große Kreis?', 6, '2 * 3',
    '9-fache Fläche heißt Radius mal 3, denn 3² = 9. Also r = 3 · 2 cm = 6 cm.', 'Rechne rückwärts: Welcher Faktor ergibt quadriert 9?', einheit='cm'))
# zusammengesetzt: zweimal Laufbahn in Folge → einer ersetzt
DSX.ersetze('zusammengesetzt', 'Eine Laufbahn besteht aus zwei geraden Stücken von je 11 m und zwei Halbkreisen mit Radius 8 m. Wie lang ist eine Runde? Runde auf eine Nachkommastelle.', DSX.Z(
    'Ein Kreisring soll 100 cm² groß sein. Der Innenradius ist 3 cm. Wie groß muss der Außenradius sein? Runde auf eine Nachkommastelle.', 6.4, '6.4',
    'π · R² − π · 3² = 100, also R² = 100 : π + 9 ≈ 31,8 + 9 = 40,8. Da 6,4 · 6,4 ≈ 41,0 und 6,3 · 6,3 ≈ 39,7 sind, ist R ≈ 6,4 cm.',
    'Ringfläche = große Kreisfläche minus kleine. Rechne rückwärts.', einheit='cm', toleranz=0.1))
DSX.stufen('umfang', 'S1 und S2 dieselbe Rechnung u = π · d; S3 teils nur Umkehrung', 'S1 Umfang aus d oder r, u : d; S2 Sachkontext, Umkehrung, Sechseck/Quadrat; S3 Umdrehungen, Maßstab, Seil-Rätsel, π-Näherung begründen')
DSX.stufen('flaeche', 'S1 und S2 dieselbe Rechnung π · r²; S3 dreimal Pizza-Vergleich', 'S1 Fläche aus r oder d; S2 Umkehrung, aus dem Umfang, Vergleich mit Quadrat; S3 Preisvergleich, Zaun, gleiche Fläche wie Quadrat, Anteil, gleiche Maßzahl')
DSX.stufen('exakt', 'S3 dreimal Kreisring', 'S1 Umfang exakt; S2 Umkehrung, Fläche aus d; S3 Umfang → Fläche, Kreisring, Fehler berichtigen, Figur, Draht')
DSX.stufen('verstehen', 'S2 dreimal derselbe Fehler; S3 viermal derselbe Vergleich', 'S1 Faktor bei Vergrößerung; S2 Fehler erkennen, Faktor 1,5, Fläche nach Verdopplung; S3 Vergleich r gegen u, Faktor für doppelte Fläche, rückwärts, Prozent, Maßstab')
DSX.stufen('sektor', 'S3 enthielt eine reine Formelaufgabe', 'S1 Anteil des Kreises; S2 Fläche und Bogen mit Formel; S3 Winkel rückwärts, Scheibenwischer, Uhr, Diagramm, ganzer Rand')
DSX.stufen('zusammengesetzt', 'S1 und S2 dieselbe Kreisring-Rechnung; S3 zweimal Laufbahn', 'S1 Kreisring; S2 Kreisabschnitt, Durchmesser statt Radius, Halbkreis; S3 Figuren zerlegen, Laufbahn, Ring rückwärts, Fenster, Sportplatz')
DSX.stufen('zylinder', 'S1 und S2 dieselbe Formel; S3 Regenfass wie S2', 'S1 Volumen, Mantel; S2 Oberfläche, Höhe rückwärts, Sachkontext; S3 Term wählen, Wasserspiegel, Vergleich, Blatt rollen')
baue = mit_durchsicht(baue, DSX)
# ---- DURCHSICHT ENDE ----

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Kreis', ['umfang', 'flaeche', 'exakt', 'verstehen']), ('Teile von Kreisen', ['sektor', 'zusammengesetzt']), ('Zylinder', ['zylinder'])],
         'Umfang und Flächeninhalt von Kreisen, Kreisausschnitten und Kreisringen berechnen – gerundet und exakt mit π – sowie Volumen und Oberfläche von Zylindern.',
         ['u = 2πr = πd, A = πr².', 'Ausschnitt: Anteil α/360° von Umfang bzw. Fläche.', 'Zylinder: V = πr²h, O = 2πr² + 2πrh.'],
         offen=['Kreisabschnitt (Segment) nur beim Mittelpunktswinkel 90°: Für andere Winkel braucht man Trigonometrie (spätere Jahrgangsstufe).',
                'Zylinder und Halbkreis-Ränder kann die App nicht zeichnen (keine Körper, keine Kreisbögen); Kreis, Ring, Ausschnitt (als Vieleck genähert) und Quadrat mit Inkreis sind gezeichnet.'])
