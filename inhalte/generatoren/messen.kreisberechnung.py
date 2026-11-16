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

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Kreis', ['umfang', 'flaeche', 'exakt', 'verstehen']), ('Teile von Kreisen', ['sektor', 'zusammengesetzt']), ('Zylinder', ['zylinder'])],
         'Umfang und Flächeninhalt von Kreisen, Kreisausschnitten und Kreisringen berechnen – gerundet und exakt mit π – sowie Volumen und Oberfläche von Zylindern.',
         ['u = 2πr = πd, A = πr².', 'Ausschnitt: Anteil α/360° von Umfang bzw. Fläche.', 'Zylinder: V = πr²h, O = 2πr² + 2πrh.'],
         offen=['Kreisabschnitt (Segment) nur beim Mittelpunktswinkel 90°: Für andere Winkel braucht man Trigonometrie (spätere Jahrgangsstufe).',
                'Zylinder und Halbkreis-Ränder kann die App nicht zeichnen (keine Körper, keine Kreisbögen); Kreis, Ring, Ausschnitt (als Vieleck genähert) und Quadrat mit Inkreis sind gezeichnet.'])
