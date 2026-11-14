#!/usr/bin/env python3
"""Thema bruch.brueche – Brüche und Anteile (Klasse 6)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _basis import *  # noqa: E402,F403

R = random.Random(21)
E = eintrag_laden('bruch.brueche')
HB = 'Zähler ins erste Kästchen, Nenner ins zweite.'

ETAPPEN = [
    {'lernziel': 'bruchteil_von', 'titel': 'Bruchteil einer Größe berechnen',
     'regel': 'Ein Bruch wie 3/4 besteht aus ⟦Zähler⟧ (oben, 3) und ⟦Nenner⟧ (unten, 4). So berechnest du 3/4 von einer Größe: ⟦durch den Nenner teilen⟧, dann ⟦mit dem Zähler malnehmen⟧.',
     'schritte': ['3/4 von 20 €: Zuerst 20 € : 4 = 5 €. Das ist ein Viertel.', 'Dann 5 € · 3 = ⟦15 €⟧. Das sind drei Viertel.'],
     'probe': '15 € ist weniger als 20 € – passt, denn 3/4 ist weniger als ein Ganzes ✓',
     'fehler': '3/4 von 20 € als 20 : 3 · 4 zu rechnen ist falsch: Du teilst durch den ⟦Nenner⟧ (unten) und nimmst mit dem ⟦Zähler⟧ (oben) mal.'},
    {'lernziel': 'anteil_bestimmen', 'titel': 'Welcher Anteil ist das?',
     'regel': 'Der ⟦Anteil⟧ ist ⟦Teil durch Ganzes⟧: Der Teil kommt in den Zähler, das Ganze in den Nenner. Danach ⟦kürzt⟧ man so weit wie möglich.',
     'schritte': ['Von 30 Kindern spielen 12 ein Instrument. Anteil: 12/30.', 'Zähler und Nenner durch 6 teilen: 12/30 = ⟦2/5⟧.'],
     'probe': '2/5 von 30 = 30 : 5 · 2 = 12 ✓',
     'fehler': 'Den Anteil als 30/12 aufzuschreiben ist falsch: Der Teil steht ⟦oben⟧ im Zähler, das Ganze ⟦unten⟧ im Nenner.'},
    {'lernziel': 'ganzes_bestimmen', 'titel': 'Das Ganze aus einem Teil finden',
     'regel': 'Kennst du einen Bruchteil, findest du das ⟦Ganze⟧ rückwärts: ⟦durch den Zähler teilen⟧ – das ist ein Stück –, dann ⟦mit dem Nenner malnehmen⟧.',
     'schritte': ['2/5 der Klasse sind 12 Kinder. Ein Fünftel: 12 : 2 = 6 Kinder.', 'Das Ganze sind fünf Fünftel: 6 · 5 = ⟦30 Kinder⟧.'],
     'probe': '2/5 von 30 = 30 : 5 · 2 = 12 ✓',
     'fehler': 'Das Ganze als 2/5 von 12 auszurechnen ist falsch: Dann bekommst du einen ⟦Teil vom Teil⟧. Rückwärts heißt: ⟦durch den Zähler, mal den Nenner⟧.'},
    {'lernziel': 'erweitern', 'titel': 'Brüche erweitern',
     'regel': '⟦Erweitern⟧ heißt: Zähler und Nenner mit ⟦derselben Zahl⟧ malnehmen. Der Wert des Bruchs bleibt gleich, nur die Stücke werden kleiner und es werden mehr.',
     'schritte': ['Erweitere 3/4 auf den Nenner 20. Es gilt 4 · 5 = 20.', 'Also auch den Zähler mal 5: 3 · 5 = 15. Ergebnis: 3/4 = ⟦15/20⟧.'],
     'probe': '15/20 durch 5 gekürzt ergibt wieder 3/4 ✓',
     'fehler': '3/4 = 3/20 ist falsch: Wer nur den Nenner ändert, verändert den Wert. ⟦Zähler und Nenner⟧ werden mit derselben Zahl malgenommen.'},
    {'lernziel': 'kuerzen', 'titel': 'Brüche vollständig kürzen',
     'regel': '⟦Kürzen⟧ heißt: Zähler und Nenner durch ⟦dieselbe Zahl⟧ teilen. ⟦Vollständig gekürzt⟧ ist ein Bruch, wenn Zähler und Nenner keinen gemeinsamen Teiler außer 1 mehr haben.',
     'schritte': ['Kürze 18/24. Der größte gemeinsame Teiler von 18 und 24 ist 6.', '18 : 6 = 3 und 24 : 6 = 4, also 18/24 = ⟦3/4⟧.'],
     'probe': '3/4 mit 6 erweitert ergibt 18/24 ✓',
     'fehler': '18/24 = 9/12 ist richtig gekürzt, aber ⟦nicht vollständig⟧: 9 und 12 haben noch den Teiler 3. Ganz gekürzt: 3/4.'},
    {'lernziel': 'vergleichen', 'titel': 'Brüche vergleichen',
     'regel': 'Gleicher Nenner: Der Bruch mit dem ⟦größeren Zähler⟧ ist größer. Verschiedene Nenner: Erst beide Brüche auf den ⟦Hauptnenner⟧ erweitern (das kleinste gemeinsame Vielfache der Nenner), dann die Zähler vergleichen.',
     'schritte': ['Vergleiche 3/4 und 5/6. Hauptnenner von 4 und 6 ist 12.', '3/4 = 9/12 und 5/6 = 10/12. Weil 10 > 9, ist ⟦5/6 größer⟧.'],
     'fehler': '„3/8 ist größer als 3/5, weil 8 > 5“ ist falsch: Ein größerer Nenner heißt ⟦kleinere Stücke⟧. Bei gleichem Zähler ist der Bruch mit dem ⟦kleineren Nenner⟧ größer.'},
    {'lernziel': 'zahlenstrahl', 'titel': 'Brüche am Zahlenstrahl',
     'regel': 'Am ⟦Zahlenstrahl⟧ teilst du die Strecke von 0 bis 1 in so viele gleiche Teile, wie der ⟦Nenner⟧ angibt. Der ⟦Zähler⟧ sagt, wie viele Teile du von 0 aus nach rechts gehst.',
     'schritte': ['3/5: Teile die Strecke von 0 bis 1 in 5 gleiche Teile.', 'Gehe von 0 aus 3 Teile nach rechts: Dort liegt ⟦3/5⟧.'],
     'fehler': '3/5 beim 5. Strich einzutragen ist falsch: Der 5. Strich nach der 0 ist schon die ⟦1⟧ (5/5). 3/5 liegt beim ⟦3. Strich⟧.',
     'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': 5, 'beschriftet': 'anfang_ende'}},
    {'lernziel': 'verstehen', 'titel': 'Aussagen prüfen, Fehler finden',
     'regel': 'Bevor du eine Aussage über Brüche glaubst, ⟦prüfe sie mit einem Beispiel⟧: Erweitere, kürze oder rechne den Anteil aus. Ein einziges Gegenbeispiel zeigt, dass eine allgemeine Aussage ⟦falsch⟧ ist.',
     'schritte': ['Aussage: „Ein Bruch mit größerem Nenner ist immer größer.“ Teste 1/2 und 1/4.', '1/2 = 2/4 ist größer als 1/4. Das ist ein Gegenbeispiel, die Aussage ist also ⟦falsch⟧.'],
     'fehler': 'Eine Aussage nur mit einem passenden Beispiel „beweisen“ reicht nicht: 1/4 < 3/5 bestätigt die Nenner-Regel zufällig. Ein ⟦Gegenbeispiel⟧ wie 1/2 > 1/4 widerlegt sie.'},
]

MERKE = ['Bruchteil von: durch den Nenner, mal den Zähler.', 'Anteil = Teil : Ganzes, dann kürzen.',
         'Ganzes: durch den Zähler, mal den Nenner.', 'Erweitern und Kürzen ändern den Wert nicht.',
         'Vergleichen: auf den Hauptnenner bringen, dann Zähler vergleichen.']

GROESSEN = [('€', 'Euro'), ('kg', 'Kilogramm'), ('m', 'Meter'), ('l', 'Liter'), ('min', 'Minuten')]
SACHEN = [('Kinder', 'einer Klasse mit', 'Kinder'), ('Seiten', 'eines Buches mit', 'Seiten'), ('Plätze', 'eines Busses mit', 'Plätzen'),
          ('Äpfel', 'einer Kiste mit', 'Äpfeln'), ('Tickets', 'eines Kontingents von', 'Tickets')]


def bruchtext(z, n): return f'{z}/{n}'


def teile(k): return '1 Teil' if k == 1 else f'{k} Teile'


def echt(R, nmax):
    n = R.randint(2, nmax)
    z = R.randint(1, n - 1)
    return z, n


def fl(x):
    """Bruch für Lücken: (Zähler, Nenner) vollständig gekürzt."""
    x = Fr(x)
    return x.numerator, x.denominator


# ---------- 1 Bruchteil von ----------
def g_von(st):
    if st == 1:
        n = R.randint(2, 10)
        z = 1 if R.random() < .4 else R.randint(1, n - 1)
        g = n * R.randint(2, 12)
        e, _ = R.choice(GROESSEN)
        r = Fr(g, n) * z
        return {'y': 'zahl', 'f': {'text': f'Berechne {bruchtext(z, n)} von {g} {e}.'}, 'o': {'wert': wert(r), 'einheit': e}, 'c': f'{g} / {n} * {z}',
                'w': f'{g} {e} : {n} = {zt(Fr(g, n))} {e}' + (f', dann · {z} = {zt(r)} {e}.' if z > 1 else f'. Das ist 1/{n} von {g} {e}.'), 'h': 'Teile zuerst durch den Nenner.'}
    if st == 2:
        z, n = echt(R, 12)
        if gcd(z, n) > 1: z, n = fl(Fr(z, n))
        if n < 2: return g_von(2)
        g = n * R.randint(5, 40)
        art = R.choice(SACHEN)
        r = Fr(g, n) * z
        return {'y': 'zahl', 'f': {'text': f'{bruchtext(z, n)} der {art[0]} {art[1]} {g} {art[2]} – wie viele {art[0]} sind das?'}, 'o': {'wert': wert(r)}, 'c': f'{g} / {n} * {z}',
                'w': f'{g} : {n} = {zt(Fr(g, n))}, dann · {z} = {zt(r)} {art[0]}.', 'h': 'Erst ein Stück ausrechnen (durch den Nenner), dann mit dem Zähler malnehmen.'}
    art = R.randrange(3)
    if art == 0:
        n = R.choice([2, 3, 4, 5, 6, 10, 12, 15, 20])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        return {'y': 'zahl', 'f': {'text': f'Wie viele Minuten sind {bruchtext(z, n)} Stunde?'}, 'o': {'wert': wert(Fr(60, n) * z), 'einheit': 'min'}, 'c': f'60 / {n} * {z}',
                'w': f'1 h = 60 min. 60 : {n} = {zt(Fr(60, n))}, · {z} = {zt(Fr(60, n) * z)} min.', 'h': 'Rechne mit 60 Minuten als Ganzem.'}
    if art == 1:
        n = R.choice([2, 4, 5, 8, 10, 20, 25])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        e, k, kl_e = R.choice([('kg', 1000, 'g'), ('km', 1000, 'm'), ('m', 100, 'cm'), ('l', 1000, 'ml')])
        return {'y': 'zahl', 'f': {'text': f'Wie viele {kl_e} sind {bruchtext(z, n)} {e}?'}, 'o': {'wert': wert(Fr(k, n) * z), 'einheit': kl_e}, 'c': f'{k} / {n} * {z}',
                'w': f'1 {e} = {zt(k)} {kl_e}. {zt(k)} : {n} = {zt(Fr(k, n))}, · {z} = {zt(Fr(k, n) * z)} {kl_e}.', 'h': f'Rechne zuerst 1 {e} in {kl_e} um.'}
    n1, n2 = R.choice([(2, 4), (3, 6), (4, 8), (2, 5), (3, 4), (4, 5), (2, 3)])
    g = n1 * n2 * R.randint(2, 10)
    a, b = Fr(1, n1), Fr(1, n2)
    rest = g - g * a - g * b
    return {'y': 'zahl', 'f': {'text': f'Von {g} € Taschengeld gibt ein Kind 1/{n1} für Bücher und 1/{n2} für Kino aus. Wie viel Euro bleiben übrig?'}, 'o': {'wert': wert(rest), 'einheit': '€'},
            'c': f'{g} - {g} / {n1} - {g} / {n2}',
            'w': f'1/{n1} von {g} € = {zt(g * a)} €, 1/{n2} von {g} € = {zt(g * b)} €. Übrig: {g} − {zt(g * a)} − {zt(g * b)} = {zt(rest)} €.',
            'h': 'Berechne beide Bruchteile einzeln und ziehe sie vom Ganzen ab.'}


# ---------- 2 Anteil bestimmen ----------
FORMEN = ['Rechteck', 'Kreis', 'Quadrat', 'Streifen']
FARBEN = ['blau', 'rot', 'grün', 'gelb']


def luecke_bruch(x, text, w, h, c_ausdruck):
    z, n = fl(x)
    return {'y': 'luecken', 'f': {'text': text, 'schablone': '□/□', 'hinweis': HB + ' Vollständig gekürzt.'}, 'o': {'werte': [z, n]},
            'c': [f'({c_ausdruck}) * {n}', f'{n}'], 'w': w, 'h': h}


def g_anteil(st):
    if st == 1:
        n = R.randint(3, 12)
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        form, farbe = R.choice(FORMEN), R.choice(FARBEN)
        if R.random() < .5:
            return luecke_bruch(Fr(z, n), f'Ein {form} ist in {n} gleich große Teile geteilt. {teile(z)} {'ist' if z == 1 else 'sind'} {farbe}. Welcher Anteil ist {farbe}?',
                                f'{z} von {n} gleich großen Teilen: Anteil {z}/{n}.', 'Teil durch Ganzes: gefärbte Teile durch alle Teile.', f'{z} / {n}')
        return luecke_bruch(Fr(n - z, n), f'Ein {form} ist in {n} gleich große Teile geteilt. {teile(z)} {'ist' if z == 1 else 'sind'} {farbe}, der Rest ist weiß. Welcher Anteil ist weiß?',
                            f'Weiß: {n} − {z} = {teile(n - z)}, Anteil {bruch(Fr(n - z, n))}.', 'Zähle zuerst, wie viele Teile weiß sind.', f'({n} - {z}) / {n}')
    if st == 2:
        n = R.choice([12, 15, 16, 18, 20, 24, 25, 27, 28, 30, 32])
        t = R.randint(2, n - 2)
        while gcd(t, n) == 1: t = R.randint(2, n - 2)
        x = Fr(t, n)
        dinge = R.choice([('Kindern', 'fahren', 'mit dem Rad zur Schule'), ('Losen', 'sind', 'Gewinne'), ('Tagen im Monat', 'regnet es an', ''),
                          ('Fragen', 'beantwortet ein Kind', 'richtig'), ('Plätzen', 'sind', 'besetzt')])
        if dinge[0] == 'Tagen im Monat':
            txt = f'Von {n} Tagen regnet es an {t} Tagen. Welcher Anteil der Tage ist das?'
        elif dinge[0] == 'Fragen':
            txt = f'Von {n} Fragen beantwortet ein Kind {t} richtig. Welcher Anteil ist richtig?'
        else:
            txt = f'Von {n} {dinge[0]} {dinge[1]} {t} {dinge[2]}. Welcher Anteil ist das?'
        g = gcd(t, n)
        return luecke_bruch(x, txt, f'Anteil {t}/{n}. Kürzen mit {g}: {bruch(x)}.', 'Teil in den Zähler, Ganzes in den Nenner, dann kürzen.', f'{t} / {n}')
    art = R.randrange(3)
    if art == 0:
        m = R.choice([5, 10, 12, 15, 20, 24, 30, 36, 40, 45, 48, 50])
        return luecke_bruch(Fr(m, 60), f'Welcher Anteil einer Stunde sind {m} Minuten?', f'1 h = 60 min. Anteil {m}/60 = {bruch(Fr(m, 60))}.',
                            'Beide Größen in derselben Einheit: 1 h = 60 min.', f'{m} / 60')
    if art == 1:
        g = R.choice([50, 100, 125, 150, 200, 250, 300, 400, 500, 600, 750, 800])
        e, k, kl_e = R.choice([('kg', 1000, 'g'), ('km', 1000, 'm'), ('l', 1000, 'ml')])
        return luecke_bruch(Fr(g, k), f'Welcher Anteil von 1 {e} sind {g} {kl_e}?', f'1 {e} = {zt(k)} {kl_e}. Anteil {g}/{zt(k)} = {bruch(Fr(g, k))}.',
                            f'Rechne 1 {e} in {kl_e} um, dann Teil durch Ganzes.', f'{g} / {k}')
    n = R.choice([20, 24, 28, 30, 32])
    a, b = R.randint(3, n // 3), R.randint(3, n // 3)
    rest = n - a - b
    return luecke_bruch(Fr(rest, n), f'Von {n} Kindern kommen {a} mit dem Bus, {b} mit dem Rad, der Rest zu Fuß. Welcher Anteil kommt zu Fuß?',
                        f'Zu Fuß: {n} − {a} − {b} = {rest}. Anteil {rest}/{n} = {bruch(Fr(rest, n))}.', 'Berechne zuerst, wie viele Kinder zu Fuß kommen.', f'({n} - {a} - {b}) / {n}')


# ---------- 3 Ganzes bestimmen ----------
def g_ganzes(st):
    if st == 1:
        n = R.randint(2, 10)
        t = R.randint(2, 15)
        e, _ = R.choice(GROESSEN)
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'1/{n} eines Betrags sind {t} {e}. Wie groß ist das Ganze?'},
                    'o': {'wert': t * n, 'einheit': e}, 'c': f'{t} * {n}',
                    'w': f'Ein Teil (1/{n}) sind {t} {e}, das Ganze sind {n} solche Stücke: {t} · {n} = {t * n} {e}.', 'h': 'Das Ganze besteht aus so vielen Stücken, wie der Nenner sagt.'}
        return {'y': 'zahl', 'f': {'text': f'{t} Kinder sind 1/{n} aller Kinder auf dem Schulhof. Wie viele Kinder sind auf dem Schulhof?'},
                'o': {'wert': t * n}, 'c': f'{t} * {n}', 'w': f'{t} Kinder sind 1/{n}, also alle: {t} · {n} = {t * n} Kinder.', 'h': 'Ein Stück mal Nenner ergibt das Ganze.'}
    if st == 2:
        n = R.randint(3, 12)
        z = R.randint(2, n - 1)
        while gcd(z, n) > 1: z = R.randint(2, n - 1) if n > 3 else 2
        k = R.randint(2, 15)
        t = z * k
        e, _ = R.choice(GROESSEN)
        return {'y': 'zahl', 'f': {'text': f'{z}/{n} eines Ganzen sind {t} {e}. Wie groß ist das Ganze?'}, 'o': {'wert': k * n, 'einheit': e}, 'c': f'{t} / {z} * {n}',
                'w': f'Ein Teil (1/{n}): {t} : {z} = {k} {e}. Das Ganze: {k} · {n} = {k * n} {e}.', 'h': 'Teile durch den Zähler, dann nimm mit dem Nenner mal.'}
    art = R.randrange(3)
    n = R.choice([4, 5, 6, 8, 10])
    z = R.randint(2, n - 1)
    while gcd(z, n) > 1: z = R.randint(2, n - 1)
    k = R.randint(3, 30) * (10 if art != 1 else 1)
    t = z * k
    if art == 0:
        return {'y': 'zahl', 'f': {'text': f'Ein Wanderer hat {z}/{n} seines Weges geschafft. Das sind {zt(t)} m. Wie lang ist der ganze Weg?'}, 'o': {'wert': k * n, 'einheit': 'm'},
                'c': f'{t} / {z} * {n}', 'w': f'{zt(t)} : {z} = {zt(k)} m (das ist 1/{n}). · {n} = {zt(k * n)} m.', 'h': 'Rückwärts rechnen: durch den Zähler, mal den Nenner.'}
    if art == 1:
        return {'y': 'zahl', 'f': {'text': f'{z}/{n} der Plätze eines Kinos sind besetzt, das sind {t} Plätze. Wie viele Plätze sind noch frei?'}, 'o': {'wert': k * n - t},
                'c': f'{t} / {z} * {n} - {t}', 'w': f'Alle Plätze: {t} : {z} · {n} = {k * n}. Frei: {k * n} − {t} = {k * n - t}.', 'h': 'Berechne zuerst alle Plätze, dann ziehe die besetzten ab.'}
    return {'y': 'zahl', 'f': {'text': f'Ein Tank ist zu {z}/{n} gefüllt und enthält {zt(t)} l. Wie viele Liter passen in den vollen Tank?'}, 'o': {'wert': k * n, 'einheit': 'l'},
            'c': f'{t} / {z} * {n}', 'w': f'{zt(t)} : {z} = {zt(k)} l, · {n} = {zt(k * n)} l.', 'h': 'Rechne erst aus, wie viel ein Teil (1/Nenner) ist.'}


# ---------- 4 Erweitern ----------
def g_erweitern(st):
    z, n = echt(R, 9)
    z, n = fl(Fr(z, n))
    if n == 1: return g_erweitern(st)
    k = R.randint(2, 9 if st < 3 else 25)
    if st == 1:
        return {'y': 'luecken', 'f': {'text': f'Erweitere {z}/{n} mit {k}.', 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [z * k, n * k]}, 'c': [f'{z} * {k}', f'{n} * {k}'],
                'w': f'Zähler und Nenner mal {k}: {z}/{n} = {z * k}/{n * k}.', 'h': 'Nimm Zähler und Nenner mit derselben Zahl mal.'}
    if st == 2:
        if R.random() < .5:
            return {'y': 'luecken', 'f': {'text': f'Ergänze: {z}/{n} = □/{n * k}', 'schablone': '□', 'hinweis': 'Trage den fehlenden Zähler ein.'}, 'o': {'werte': [z * k]},
                    'c': [f'{z} * {n * k} / {n}'], 'w': f'{n} · {k} = {n * k}, also auch {z} · {k} = {z * k}.', 'h': 'Mit welcher Zahl wurde der Nenner malgenommen?'}
        return {'y': 'luecken', 'f': {'text': f'Ergänze: {z}/{n} = {z * k}/□', 'schablone': '□', 'hinweis': 'Trage den fehlenden Nenner ein.'}, 'o': {'werte': [n * k]},
                'c': [f'{n} * {z * k} / {z}'], 'w': f'{z} · {k} = {z * k}, also auch {n} · {k} = {n * k}.', 'h': 'Mit welcher Zahl wurde der Zähler malgenommen?'}
    art = R.randrange(3)
    if art == 0:
        n = R.choice([2, 4, 5, 10, 20, 25, 50])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        return {'y': 'luecken', 'f': {'text': f'Erweitere {z}/{n} auf den Nenner 100.', 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [z * 100 // n, 100]},
                'c': [f'{z} * 100 / {n}', '100'], 'w': f'{n} · {100 // n} = 100, also {z} · {100 // n} = {z * 100 // n}: {z}/{n} = {z * 100 // n}/100.', 'h': 'Mit welcher Zahl wird der Nenner zu 100?'}
    if art == 1:
        return {'y': 'zahl', 'f': {'text': f'Mit welcher Zahl wurde {z}/{n} erweitert, wenn {z * k}/{n * k} herauskommt?'}, 'o': {'wert': k}, 'c': f'{n * k} / {n}',
                'w': f'{n * k} : {n} = {k} (und {z * k} : {z} = {k}).', 'h': 'Teile den neuen Nenner durch den alten.'}
    m = R.randint(2, 6)
    r = f'{z * k}/{n * k}'
    return {**wahl(R, r, [f'{z * k}/{n * m}' if m != k else f'{z + k}/{n + k}', f'{z + k}/{n + k}', f'{z}/{n * k}', f'{z * k}/{n}']),
            'f': {'text': f'Welcher Bruch ist gleich {z}/{n}?'}, 'w': f'{z}/{n} mit {k} erweitert: {r}. Bei den anderen wurde nicht Zähler und Nenner mit derselben Zahl malgenommen.',
            'h': 'Prüfe: Wurden Zähler und Nenner mit derselben Zahl malgenommen?'}


# ---------- 5 Kürzen ----------
def g_kuerzen(st):
    z, n = echt(R, 12 if st < 3 else 20)
    z, n = fl(Fr(z, n))
    if n == 1: return g_kuerzen(st)
    k = R.randint(2, 6) if st < 3 else R.choice([6, 8, 9, 12, 15, 18, 24, 25])
    Z, N = z * k, n * k
    if st == 1:
        return {'y': 'luecken', 'f': {'text': f'Kürze {Z}/{N} mit {k}.', 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [z, n]}, 'c': [f'{Z} / {k}', f'{N} / {k}'],
                'w': f'{Z} : {k} = {z} und {N} : {k} = {n}, also {Z}/{N} = {z}/{n}.', 'h': 'Teile Zähler und Nenner durch dieselbe Zahl.'}
    if st == 2:
        return {'y': 'luecken', 'f': {'text': f'Kürze {Z}/{N} vollständig.', 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [z, n]}, 'c': [f'{Z} / {k}', f'{N} / {k}'],
                'w': f'Größter gemeinsamer Teiler von {Z} und {N} ist {k}. {Z}/{N} = {z}/{n}.', 'h': 'Suche den größten gemeinsamen Teiler. Du kannst auch in mehreren Schritten kürzen.'}
    art = R.randrange(3)
    if art == 0:
        return {'y': 'luecken', 'f': {'text': f'Kürze {Z}/{N} vollständig.', 'schablone': '□/□', 'hinweis': HB}, 'o': {'werte': [z, n]}, 'c': [f'{Z} / {k}', f'{N} / {k}'],
                'w': f'Größter gemeinsamer Teiler: {k}. {Z} : {k} = {z}, {N} : {k} = {n}.', 'h': 'Kürze schrittweise, z. B. erst durch 2, 3 oder 5, bis es nicht mehr geht.'}
    if art == 1:
        t = R.choice([d for d in range(2, k) if k % d == 0] or [1])
        if t == 1: return g_kuerzen(3)
        r = 'Nein, man kann noch weiter kürzen.'
        return {**wahl(R, r, ['Ja, das ist vollständig gekürzt.', 'Nein, man hätte erweitern müssen.'], 3),
                'f': {'text': f'Ein Kind kürzt {Z}/{N} zu {Z // t}/{N // t}. Ist der Bruch damit vollständig gekürzt?'},
                'w': f'{Z // t} und {N // t} haben noch den gemeinsamen Teiler {k // t}. Vollständig gekürzt: {z}/{n}.', 'h': 'Haben Zähler und Nenner noch einen gemeinsamen Teiler?'}
    r = f'{z}/{n}'
    return {**wahl(R, r, [f'{Z - k}/{N - k}' if Z > k else f'{z + 1}/{n + 1}', f'{z}/{N}', f'{Z // 2}/{N}' if Z % 2 == 0 else f'{z + 1}/{n}', f'{n}/{z}']),
            'f': {'text': f'Welcher Bruch entsteht, wenn man {Z}/{N} vollständig kürzt?'}, 'w': f'{Z} : {k} = {z}, {N} : {k} = {n}: {r}.',
            'h': 'Teile Zähler und Nenner durch ihren größten gemeinsamen Teiler.'}


# ---------- 6 Vergleichen ----------
def kgv(a, b): return a * b // gcd(a, b)


def zwei_brueche(R, nmax):
    while True:
        z1, n1 = echt(R, nmax); z2, n2 = echt(R, nmax)
        a, b = Fr(z1, n1), Fr(z2, n2)
        if a != b and a.denominator != b.denominator and a.denominator > 1 and b.denominator > 1: return a, b


def g_vergleichen(st):
    if st == 1:
        if R.random() < .5:
            n = R.randint(3, 15)
            z1, z2 = R.sample(range(1, n), 2)
            a, b = bruchtext(z1, n), bruchtext(z2, n)
            r = a if z1 > z2 else b
            return {**wahl(R, r, [b if r == a else a, 'Beide sind gleich groß'], 3), 'f': {'text': f'Welcher Bruch ist größer: {a} oder {b}?'},
                    'w': f'Gleicher Nenner: Der größere Zähler gewinnt. {r} ist größer.', 'h': 'Gleicher Nenner – vergleiche die Zähler.'}
        z = R.randint(1, 5)
        n1, n2 = R.sample(range(z + 1, 13), 2)
        a, b = bruchtext(z, n1), bruchtext(z, n2)
        r = a if n1 < n2 else b
        return {**wahl(R, r, [b if r == a else a, 'Beide sind gleich groß'], 3), 'f': {'text': f'Welcher Bruch ist größer: {a} oder {b}?'},
                'w': f'Gleicher Zähler: Kleinerer Nenner heißt größere Stücke. {r} ist größer.', 'h': 'Gleicher Zähler – welcher Bruch hat die größeren Stücke?'}
    if st == 2:
        a, b = zwei_brueche(R, 10)
        if R.random() < .3:
            hn = kgv(a.denominator, b.denominator)
            return {'y': 'zahl', 'f': {'text': f'Wie heißt der Hauptnenner von {bruch(a)} und {bruch(b)}?'}, 'o': {'wert': hn}, 'c': f'{a.denominator} * {b.denominator} / {gcd(a.denominator, b.denominator)}',
                    'w': f'Das kleinste gemeinsame Vielfache von {a.denominator} und {b.denominator} ist {hn}.', 'h': 'Gehe die Vielfachen des größeren Nenners durch, bis der andere Nenner hineinpasst.'}
        hn = kgv(a.denominator, b.denominator)
        r = bruch(max(a, b))
        return {**wahl(R, r, [bruch(min(a, b)), 'Beide sind gleich groß'], 3), 'f': {'text': f'Welcher Bruch ist größer: {bruch(a)} oder {bruch(b)}?'},
                'w': f'Hauptnenner {hn}: {bruch(a)} = {a.numerator * hn // a.denominator}/{hn}, {bruch(b)} = {b.numerator * hn // b.denominator}/{hn}. Größer: {r}.',
                'h': 'Bringe beide Brüche auf den Hauptnenner.'}
    art = R.randrange(3)
    if art == 0:
        xs = set()
        while len(xs) < 4:
            z, n = echt(R, 12)
            xs.add(Fr(z, n))
        xs = list(xs)
        frage = R.choice(['kleinste', 'größte'])
        r = bruch(min(xs) if frage == 'kleinste' else max(xs))
        return {**wahl(R, r, [bruch(x) for x in xs]), 'f': {'text': f'Welcher ist der {frage} Bruch: ' + ', '.join(bruch(x) for x in xs) + '?'},
                'w': 'Der Größe nach: ' + ' < '.join(bruch(x) for x in sorted(xs)) + f'. Der {frage} ist {r}.', 'h': 'Vergleiche mit 1/2 oder bringe die Brüche auf einen gemeinsamen Nenner.'}
    if art == 1:
        a, b = zwei_brueche(R, 8)
        lo, hi = min(a, b), max(a, b)
        m = (lo + hi) / 2
        falsch = [lo - Fr(1, 2 * lo.denominator * hi.denominator), hi + Fr(1, hi.denominator * 2), Fr(lo.numerator + hi.numerator, lo.denominator + hi.denominator + 5)]
        falsch = [bruch(x) for x in falsch if x > 0 and not lo < x < hi]
        if len(falsch) < 2: return g_vergleichen(3)
        return {**wahl(R, bruch(m), falsch), 'f': {'text': f'Welcher Bruch liegt zwischen {bruch(lo)} und {bruch(hi)}?'},
                'w': f'Die Mitte von {bruch(lo)} und {bruch(hi)} ist {bruch(m)}; sie liegt dazwischen.', 'h': 'Erweitere beide Brüche so weit, dass zwischen den Zählern Platz ist.'}
    a, b = zwei_brueche(R, 12)
    hn = kgv(a.denominator, b.denominator)
    d = abs(a - b)
    z, n = fl(d)
    return {'y': 'luecken', 'f': {'text': f'Um wie viel ist {bruch(max(a, b))} größer als {bruch(min(a, b))}?', 'schablone': '□/□', 'hinweis': HB + ' Vollständig gekürzt.'},
            'o': {'werte': [z, n]}, 'c': [f'({bruch(max(a, b))} - {bruch(min(a, b))}) * {n}', f'{n}'],
            'w': f'Hauptnenner {hn}: {max(a, b).numerator * hn // max(a, b).denominator}/{hn} − {min(a, b).numerator * hn // min(a, b).denominator}/{hn} = {bruch(d)}.',
            'h': 'Bringe beide auf den Hauptnenner und vergleiche die Zähler.'}


# ---------- 7 Zahlenstrahl ----------
def endlich(x):
    try:
        zt(x); return True
    except ValueError:
        return False


def mark(x, start, ende, abschnitte, text, w, h):
    idx = (Fr(x) - start) * abschnitte / (ende - start)
    assert idx.denominator == 1
    a = {'y': 'markierung', 'f': {'text': text, 'grafik': {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': abschnitte, 'beschriftet': 'anfang_ende'}},
         'o': {'index': int(idx)}, 'w': w, 'h': h}
    if endlich(x):
        a['zahl'] = wert(x)
        a['c'] = f'{start} + ({ende} - {start}) * {int(idx)} / {abschnitte}'
    return a


def g_strahl(st):
    if st == 1:
        n = R.randint(2, 10)
        z = R.randint(1, n - 1)
        return mark(Fr(z, n), 0, 1, n, f'Markiere {z}/{n} am Zahlenstrahl (von 0 bis 1, {n} gleiche Teile).',
                    f'Die Strecke von 0 bis 1 ist in {n} Teile geteilt. {z}/{n} liegt beim {z}. Strich nach der 0.', 'Der Nenner sagt, in wie viele Teile geteilt ist. Zähle von 0 aus.')
    if st == 2:
        if R.random() < .5:
            n = R.randint(2, 6)
            k = R.randint(2, 4)
            z = R.randint(1, n - 1)
            return mark(Fr(z, n), 0, 1, n * k, f'Markiere {z}/{n} am Zahlenstrahl (von 0 bis 1, {n * k} gleiche Teile).',
                        f'{z}/{n} = {z * k}/{n * k}. Also beim {z * k}. Strich nach der 0.', f'Erweitere {z}/{n} so, dass der Nenner {n * k} ist.')
        n = R.randint(2, 6)
        z = R.randint(n + 1, 2 * n - 1)
        return mark(Fr(z, n), 0, 2, 2 * n, f'Markiere {z}/{n} am Zahlenstrahl (von 0 bis 2, {2 * n} gleiche Teile).',
                    f'Jeder Teil ist 1/{n}. {z}/{n} liegt beim {z}. Strich nach der 0, also hinter der 1.', f'Von 0 bis 1 sind es {n} Teile. {z}/{n} ist größer als 1.')
    art = R.randrange(3)
    if art == 0:
        N = R.choice([6, 8, 10, 12, 15, 20])
        teiler = [d for d in range(2, N) if N % d == 0]
        n = R.choice(teiler)
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        x = Fr(z, n)
        idx = x * N
        return {'y': 'luecken', 'f': {'text': f'Ein Zahlenstrahl von 0 bis 1 ist in {N} gleiche Teile geteilt. Ein Pfeil zeigt auf den {idx}. Strich nach der 0. Welcher Bruch ist das?',
                                      'schablone': '□/□', 'hinweis': HB + ' Vollständig gekürzt.'}, 'o': {'werte': [z, n]}, 'c': [f'{idx} / {N} * {n}', f'{n}'],
                'w': f'Der Pfeil zeigt auf {idx}/{N}. Gekürzt: {z}/{n}.', 'h': 'Schreibe zuerst Strich-Nummer / Anzahl der Teile und kürze dann.'}
    if art == 1:
        n = R.randint(2, 5)
        z = R.randint(1, n - 1)
        x = 1 + Fr(z, n)
        return mark(x, 1, 2, n, f'Markiere {bruch(x)} am Zahlenstrahl (von 1 bis 2, {n} gleiche Teile).',
                    f'{bruch(x)} = 1 + {z}/{n}. Von der 1 aus {teile(z)} nach rechts.', 'Wie viele Ganze stecken in dem Bruch? Starte bei der 1.')
    n = R.choice([3, 4, 5, 6])
    z = R.randint(1, n - 1)
    k = 2
    return mark(Fr(z, n), 0, 2, 4 * n, f'Markiere {z}/{n} am Zahlenstrahl (von 0 bis 2, {2 * n * 2} gleiche Teile).',
                f'Von 0 bis 1 sind es {2 * n} Teile, jeder ist 1/{2 * n}. {z}/{n} = {2 * z}/{2 * n}: beim {2 * z}. Strich.',
                'Wie viele Teile liegen zwischen 0 und 1? Damit erweiterst du den Bruch.')


# ---------- 8 Verstehen ----------
def g_verstehen(st):
    z, n = echt(R, 9)
    z, n = fl(Fr(z, n))
    if n == 1: return g_verstehen(st)
    k = R.randint(2, 6)
    if st == 1:
        aussagen = [
            (f'{z}/{n} und {z * k}/{n * k} sind gleich groß.', True, f'Ja, {z * k}/{n * k} ist {z}/{n} mit {k} erweitert.'),
            (f'{z}/{n} und {z + k}/{n + k} sind gleich groß.', False, f'Nein, man darf nicht addieren. Mit Hauptnenner sieht man: {bruch(Fr(z, n))} ≠ {bruch(Fr(z + k, n + k))}.'),
            (f'1/{n} ist größer als 1/{n + k}.', True, f'Ja, bei 1/{n} ist das Ganze in weniger, also größere Stücke geteilt.'),
            (f'1/{n + k} ist größer als 1/{n}, weil {n + k} > {n}.', False, f'Nein, mehr Teile bedeuten kleinere Stücke: 1/{n + k} < 1/{n}.'),
        ]
    elif st == 2:
        g = n * R.randint(3, 12)
        aussagen = [
            (f'{z}/{n} von {g} sind {g // n * z}.', True, f'Ja: {g} : {n} = {g // n}, · {z} = {g // n * z}.'),
            (f'{z}/{n} von {g} sind {g * z + n if z > 1 else g // n + z}.', False, f'Nein: {g} : {n} · {z} = {g // n * z}.'),
            (f'Wenn {z * k} von {n * k} Kindern Brille tragen, ist der Anteil {n * k}/{z * k}.', False, f'Nein, der Teil kommt in den Zähler: {z * k}/{n * k} = {z}/{n}.'),
            (f'{z * k}/{n * k} kann man zu {z}/{n} kürzen.', True, f'Ja, Zähler und Nenner durch {k} geteilt.'),
        ]
    else:
        a, b = zwei_brueche(R, 9)
        aussagen = [
            (f'{bruch(a)} ist größer als {bruch(b)}.', a > b, f'Hauptnenner {kgv(a.denominator, b.denominator)}: {bruch(a)} ist {"größer" if a > b else "kleiner"} als {bruch(b)}.'),
            ('Je größer der Nenner, desto größer der Bruch.', False, 'Nein, Gegenbeispiel: 1/2 > 1/3, obwohl 3 > 2.'),
            ('Wenn man Zähler und Nenner um dieselbe Zahl vergrößert, bleibt der Wert gleich.', False, 'Nein, Gegenbeispiel: 1/2 und (1+1)/(2+1) = 2/3 sind verschieden.'),
            (f'Ein Bruch mit Zähler größer als Nenner, wie {n + z}/{n}, ist größer als 1.', True, f'Ja, {n}/{n} = 1, und {n + z}/{n} ist noch {z}/{n} mehr.'),
            (f'{z}/{n} von {n * 6} ist dasselbe wie {n * 6} : {z} · {n}.', False, f'Nein: Bruchteil heißt durch den Nenner, mal den Zähler: {n * 6} : {n} · {z} = {6 * z}.'),
        ]
    s, stimmt, grund = R.choice(aussagen)
    if stimmt and not grund.startswith('Ja'): grund = 'Ja. ' + grund
    if not stimmt and not grund.startswith('Nein'): grund = 'Nein. ' + grund
    gegen = 'Ja, die Aussage stimmt.' if not stimmt else 'Nein, die Aussage ist falsch.'
    return {**wahl(R, grund, [gegen, 'Das kann man nicht entscheiden.'], 3), 'f': {'text': f'Stimmt die Aussage? „{s}“'},
            'w': grund, 'h': 'Prüfe mit einem Beispiel: erweitern, kürzen oder ausrechnen.'}


GEN = {'bruchteil_von': g_von, 'anteil_bestimmen': g_anteil, 'ganzes_bestimmen': g_ganzes, 'erweitern': g_erweitern, 'kuerzen': g_kuerzen,
       'vergleichen': g_vergleichen, 'zahlenstrahl': g_strahl, 'verstehen': g_verstehen}

DATEI = datei(E, 'Anteile als Brüche deuten und berechnen, Brüche erweitern, kürzen, vergleichen und am Zahlenstrahl darstellen.', MERKE,
              [('Anteile verstehen', ['bruchteil_von', 'anteil_bestimmen', 'ganzes_bestimmen']),
               ('Erweitern und kürzen', ['erweitern', 'kuerzen']),
               ('Vergleichen und darstellen', ['vergleichen', 'zahlenstrahl', 'verstehen'])],
              ETAPPEN, GEN,
              offen=['Lehrplan „Anteile mit Flächendiagrammen veranschaulichen“: Flächen sind nur in Worten beschrieben (Rechteck in n Teile, k gefärbt). Lernkarte anteil_bestimmen braucht Zeichnung: gefärbte Rechteck-/Kreisteile zum Ablesen und Selbst-Färben.',
                     'Brüche stehen im Text als 3/4 (Schrägstrich). Falls die App echte Bruchdarstellung bekommt, Texte umstellen.',
                     'Bei Markierungen mit Dritteln/Sechsteln fehlt das Feld „zahl“, weil 1/3 keine endliche Dezimalzahl ist; der Index wird vom Programm exakt berechnet.'])

if __name__ == '__main__':
    schreibe(DATEI)
