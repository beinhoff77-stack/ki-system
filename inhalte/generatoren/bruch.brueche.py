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
     'schritte': ['3/4 von 20 €: Teile die 20 € in 4 gleiche Teile. Ein Viertel: 20 € : 4 = 5 €.', 'Du nimmst 3 solche Teile: 5 € · 3 = ⟦15 €⟧. Das sind drei Viertel.'],
     'bild': streifen(4, 3, '20 €', '3/4 = 15 €'),
     'probe': '15 € ist weniger als 20 € – passt, denn 3/4 ist weniger als ein Ganzes ✓',
     'fehler': '3/4 von 20 € als 20 : 3 · 4 zu rechnen ist falsch: Du teilst durch den ⟦Nenner⟧ (unten) und nimmst mit dem ⟦Zähler⟧ (oben) mal.'},
    {'lernziel': 'anteil_bestimmen', 'titel': 'Welcher Anteil ist das?',
     'regel': 'Der ⟦Anteil⟧ ist ⟦Teil durch Ganzes⟧: Der Teil kommt in den Zähler, das Ganze in den Nenner. Danach ⟦kürzt⟧ man so weit wie möglich.',
     'schritte': ['Von 30 Kindern spielen 12 ein Instrument. Anteil = Teil durch Ganzes: 12/30.', 'Ordne die 30 Kinder in 5 Spalten zu je 6. Die 12 Musiker füllen genau 2 Spalten.',
                  'Zähler und Nenner durch 6 teilen: 12/30 = ⟦2/5⟧.'],
     'bild': raster(5, 6, 12),
     'probe': '2/5 von 30 = 30 : 5 · 2 = 12 ✓',
     'fehler': 'Den Anteil als 30/12 aufzuschreiben ist falsch: Der Teil steht ⟦oben⟧ im Zähler, das Ganze ⟦unten⟧ im Nenner.'},
    {'lernziel': 'ganzes_bestimmen', 'titel': 'Das Ganze aus einem Teil finden',
     'regel': 'Kennst du einen Bruchteil, findest du das ⟦Ganze⟧ rückwärts: ⟦durch den Zähler teilen⟧ – das ist ein Stück –, dann ⟦mit dem Nenner malnehmen⟧.',
     'schritte': ['2/5 der Klasse sind 12 Kinder. Ein Fünftel: 12 : 2 = 6 Kinder.', 'Das Ganze sind fünf Fünftel: 6 · 5 = ⟦30 Kinder⟧.'],
     'probe': '2/5 von 30 = 30 : 5 · 2 = 12 ✓',
     'fehler': 'Das Ganze als 2/5 von 12 auszurechnen ist falsch: Dann bekommst du einen ⟦Teil vom Teil⟧. Rückwärts heißt: ⟦durch den Zähler, mal den Nenner⟧.',
     'bild': streifen(5, 2, '5/5 = ? Kinder', '2/5 = 12 Kinder')},
    {'lernziel': 'erweitern', 'titel': 'Brüche erweitern',
     'regel': '⟦Erweitern⟧ heißt: Zähler und Nenner mit ⟦derselben Zahl⟧ malnehmen. Der Wert bleibt gleich – wie bei einer Schokolade, deren Stücke du noch einmal teilst: Du hast danach mehr, aber kleinere Stücke, und gleich viel Schokolade.',
     'schritte': ['Erweitere 3/4 auf den Nenner 20. Es gilt 4 · 5 = 20.', 'Jedes Viertel wird in 5 Stücke geteilt. Aus 3 Vierteln werden 3 · 5 = 15 Stücke von 20.', 'Also 3/4 = ⟦15/20⟧.'],
     'bild': raster(4, 5, 15),
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
     'probe': 'Ohne Hauptnenner: 3/4 fehlt 1/4 bis zum Ganzen, 5/6 fehlt nur 1/6. Ein Sechstel ist kleiner als ein Viertel, also ist 5/6 näher an 1 und damit größer ✓',
     'fehler': '„3/8 ist größer als 3/5, weil 8 > 5“ ist falsch: Ein größerer Nenner heißt ⟦kleinere Stücke⟧. Bei gleichem Zähler ist der Bruch mit dem ⟦kleineren Nenner⟧ größer.'},
    {'lernziel': 'zahlenstrahl', 'titel': 'Brüche am Zahlenstrahl',
     'regel': 'Am ⟦Zahlenstrahl⟧ teilst du die Strecke von 0 bis 1 in so viele gleiche Teile, wie der ⟦Nenner⟧ angibt. Der ⟦Zähler⟧ sagt, wie viele Teile du von 0 aus nach rechts gehst.',
     'schritte': ['3/5: Teile die Strecke von 0 bis 1 in 5 gleiche Teile.', 'Gehe von 0 aus 3 Teile nach rechts: Dort liegt ⟦3/5⟧.'],
     'fehler': '3/5 beim 5. Strich einzutragen ist falsch: Der 5. Strich nach der 0 ist schon die ⟦1⟧ (5/5). 3/5 liegt beim ⟦3. Strich⟧.',
     'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': 5, 'beschriftet': 'anfang_ende', 'pfeil': 3}},
    {'lernziel': 'verstehen', 'titel': 'Aussagen prüfen, Fehler finden',
     'regel': 'Bevor du eine Aussage über Brüche glaubst, ⟦prüfe sie mit einem Beispiel⟧: Erweitere, kürze oder rechne den Anteil aus. Ein einziges Gegenbeispiel zeigt, dass eine allgemeine Aussage ⟦falsch⟧ ist.',
     'schritte': ['Aussage: „Ein Bruch mit größerem Nenner ist immer größer.“ Teste 1/2 und 1/4.', '1/2 = 2/4 ist größer als 1/4. Das ist ein Gegenbeispiel, die Aussage ist also ⟦falsch⟧.'],
     'fehler': 'Eine Aussage nur mit einem passenden Beispiel „beweisen“ reicht nicht: 1/4 < 3/5 bestätigt die Nenner-Regel zufällig. Ein ⟦Gegenbeispiel⟧ wie 1/2 > 1/4 widerlegt sie.'},
]

MERKE = ['Bruchteil von: durch den Nenner, mal den Zähler.', 'Anteil = Teil : Ganzes, dann kürzen.',
         'Ganzes: durch den Zähler, mal den Nenner.', 'Erweitern und Kürzen ändern den Wert nicht.',
         'Vergleichen: auf den Hauptnenner bringen, dann Zähler vergleichen.']

GROESSEN = [('€', 'Euro'), ('kg', 'Kilogramm'), ('m', 'Meter'), ('l', 'Liter'), ('min', 'Minuten')]
# (Satz mit dem Ganzen, Satz mit dem Bruchteil, Nomen, kleinstes und größtes realistisches Ganzes)
SACHEN = [('Eine Klasse hat {g} Kinder.', '{b} der Kinder fahren mit dem Bus.', 'Kinder', 20, 32),
          ('Ein Buch hat {g} Seiten.', 'Du hast schon {b} der Seiten gelesen.', 'Seiten', 60, 400),
          ('Ein Reisebus hat {g} Plätze.', '{b} der Plätze sind besetzt.', 'Plätze', 30, 60),
          ('In einer Kiste liegen {g} Äpfel.', '{b} der Äpfel sind rot.', 'Äpfel', 24, 120),
          ('Für ein Konzert gibt es {g} Eintrittskarten.', '{b} der Eintrittskarten sind schon verkauft.', 'Eintrittskarten', 100, 900)]
# Einheit -> (Genitiv des Ganzen, Frage nach dem Ganzen)
GANZES = {'€': ('eines Geldbetrags', 'Wie groß ist der ganze Betrag?'), 'kg': ('eines Mehlvorrats', 'Wie viel wiegt der ganze Vorrat?'),
          'm': ('einer Strecke', 'Wie lang ist die ganze Strecke?'), 'l': ('eines Wasservorrats', 'Wie viele Liter sind es insgesamt?'),
          'min': ('einer Zeitspanne', 'Wie lang ist die ganze Zeitspanne?')}


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
        z, n = fl(Fr(z, n))
        if n == 1: return g_von(1)
        g = n * R.randint(2, 12)
        e, _ = R.choice(GROESSEN)
        r = Fr(g, n) * z
        return {'y': 'zahl', 'f': {'text': f'Berechne {bruchtext(z, n)} von {g} {e}.'}, 'o': {'wert': wert(r), 'einheit': e}, 'c': f'{g} / {n} * {z}',
                'w': f'{g} {e} : {n} = {zt(Fr(g, n))} {e}' + (f', dann · {z} = {zt(r)} {e}.' if z > 1 else f'. Das ist 1/{n} von {g} {e}.'), 'h': 'Teile zuerst durch den Nenner.'}
    if st == 2:
        z, n = fl(Fr(*echt(R, 12)))
        ganz, teil, nomen, lo, hi = R.choice(SACHEN)
        moegl = [g for g in range(lo, hi + 1) if g % n == 0]
        if n < 2 or not moegl: return g_von(2)
        g = R.choice(moegl)
        r = Fr(g, n) * z
        w = f'{zt(g)} : {n} = {zt(Fr(g, n))} {nomen}' + (f', dann · {z} = {zt(r)} {nomen}.' if z > 1 else '.')
        return {'y': 'zahl', 'f': {'text': ganz.format(g=zt(g)) + ' ' + teil.format(b=bruchtext(z, n)) + f' Wie viele {nomen} sind das?'}, 'o': {'wert': wert(r)},
                'c': f'{g} / {n} * {z}', 'w': w, 'h': 'Erst ein Stück ausrechnen (durch den Nenner), dann mit dem Zähler malnehmen.'}
    art = R.randrange(3)
    if art == 0:
        n = R.choice([2, 3, 4, 5, 6, 10, 12, 15, 20])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        r = Fr(60, n) * z
        return {'y': 'zahl', 'f': {'text': f'Wie viele Minuten sind {bruchtext(z, n)} Stunde?'}, 'o': {'wert': wert(r), 'einheit': 'min'}, 'c': f'60 / {n} * {z}',
                'w': f'1 h = 60 min. 60 : {n} = {zt(Fr(60, n))}' + (f', · {z} = {zt(r)} min.' if z > 1 else ' min.'), 'h': 'Rechne mit 60 Minuten als Ganzem.'}
    if art == 1:
        n = R.choice([2, 4, 5, 8, 10, 20, 25])
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        e, k, kl_e = R.choice([('kg', 1000, 'g'), ('km', 1000, 'm'), ('m', 100, 'cm'), ('l', 1000, 'ml')])
        r = Fr(k, n) * z
        return {'y': 'zahl', 'f': {'text': f'Wie viele {kl_e} sind {bruchtext(z, n)} {e}?'}, 'o': {'wert': wert(r), 'einheit': kl_e}, 'c': f'{k} / {n} * {z}',
                'w': f'1 {e} = {zt(k)} {kl_e}. {zt(k)} : {n} = {zt(Fr(k, n))}' + (f', · {z} = {zt(r)} {kl_e}.' if z > 1 else f' {kl_e}.'), 'h': f'Rechne zuerst 1 {e} in {kl_e} um.'}
    n1, n2 = R.choice([(2, 4), (3, 6), (4, 8), (2, 5), (3, 4), (4, 5), (2, 3)])
    g = n1 * n2 * R.randint(2, 5)
    a, b = Fr(1, n1), Fr(1, n2)
    rest = g - g * a - g * b
    return {'y': 'zahl', 'f': {'text': f'Von {g} € Erspartem gibt ein Kind 1/{n1} für Bücher und 1/{n2} für Kino aus. Wie viel Euro bleiben übrig?'}, 'o': {'wert': wert(rest), 'einheit': '€'},
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


def bild_anteil(n, k):
    """Flächendiagramm mit n gleichen Teilen, k gefärbt: (Bild, Name der Form im Genitiv)."""
    formen = (['streifen', 'kreis'] if n <= 12 else []) + [(sp, n // sp) for sp in range(2, n) if n % sp == 0 and 2 <= n // sp <= 6 and sp <= 8]
    f = R.choice(formen)
    lab = f'{n} gleich große Teile, {k} davon gefärbt'
    if f == 'streifen': return streifen(n, k, dx=1.0 if n > 8 else 1.5, label='Streifen: ' + lab), 'des Streifens'
    if f == 'kreis': return kreisteile(n, k, label='Kreis: ' + lab), 'des Kreises'
    sp, ze = f
    return raster(sp, ze, k, label='Rechteck: ' + lab), ('des Quadrats' if sp == ze else 'des Rechtecks')


def g_anteil(st):
    if st == 1 or (st == 2 and R.random() < .5) or (st == 3 and R.random() < .25):
        if st == 1:
            n = R.randint(3, 12)
            k = R.randint(1, n - 1)
            while gcd(k, n) > 1: k = R.randint(1, n - 1)
        else:
            n = R.choice([6, 8, 9, 10, 12, 15, 16, 18, 20, 24])
            k = R.randint(2, n - 2)
            while gcd(k, n) == 1: k = R.randint(2, n - 2)
        bild, wovon = bild_anteil(n, k)
        weiss = st == 3 or (st == 1 and R.random() < .35)
        t = n - k if weiss else k
        x = Fr(t, n)
        a = luecke_bruch(x, f'Welcher Anteil {wovon} ist {"weiß (nicht gefärbt)" if weiss else "gefärbt"}?',
                         (f'Weiß sind {n} − {k} = {t} von {n} gleich großen Teilen: {t}/{n}' if weiss else f'Gefärbt sind {k} von {n} gleich großen Teilen: {k}/{n}')
                         + (f' = {bruch(x)} (gekürzt mit {gcd(t, n)}).' if gcd(t, n) > 1 else '.'),
                         'Zähle alle Teile (Nenner) und die gesuchten Teile (Zähler).' + (' Kürze danach.' if st > 1 else ''), f'{t} / {n}')
        a['f']['grafik'] = bild
        return a
    if st == 2:
        n = R.choice([12, 15, 16, 18, 20, 24, 25, 27, 28, 30, 32])
        t = R.randint(2, n - 2)
        while gcd(t, n) == 1: t = R.randint(2, n - 2)
        x = Fr(t, n)
        dinge = R.choice([('Kindern', 'fahren', 'mit dem Rad zur Schule'), ('Losen', 'sind', 'Gewinne'), ('Tagen im Monat', 'regnet es an', ''),
                          ('Fragen', 'beantwortet ein Kind', 'richtig'), ('Plätzen', 'sind', 'besetzt')])
        if dinge[0] == 'Tagen im Monat':
            if n < 28: return g_anteil(2)
            txt = f'Ein Monat hat {n} Tage. An {t} Tagen regnet es. Welcher Anteil der Tage ist das?'
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
        gen, frage = GANZES[e]
        if R.random() < .5:
            return {'y': 'zahl', 'f': {'text': f'1/{n} {gen} sind {t} {e}. {frage}'},
                    'o': {'wert': t * n, 'einheit': e}, 'c': f'{t} * {n}',
                    'w': f'Ein Teil (1/{n}) sind {t} {e}, das Ganze sind {n} solche Stücke: {t} · {n} = {t * n} {e}.', 'h': 'Das Ganze besteht aus so vielen Stücken, wie der Nenner sagt.'}
        if t * n > 300: return g_ganzes(1)
        return {'y': 'zahl', 'f': {'text': f'{t} Kinder sind 1/{n} aller Kinder auf dem Schulhof. Wie viele Kinder sind auf dem Schulhof?'},
                'o': {'wert': t * n}, 'c': f'{t} * {n}', 'w': f'{t} Kinder sind 1/{n}, also alle: {t} · {n} = {t * n} Kinder.', 'h': 'Ein Stück mal Nenner ergibt das Ganze.'}
    if st == 2:
        n = R.randint(3, 12)
        z = R.randint(2, n - 1)
        while gcd(z, n) > 1: z = R.randint(2, n - 1) if n > 3 else 2
        k = R.randint(2, 15)
        t = z * k
        e, _ = R.choice(GROESSEN)
        gen, frage = GANZES[e]
        return {'y': 'zahl', 'f': {'text': f'{z}/{n} {gen} sind {t} {e}. {frage}'}, 'o': {'wert': k * n, 'einheit': e}, 'c': f'{t} / {z} * {n}',
                'w': f'Ein Teil (1/{n}): {t} : {z} = {k} {e}. Das Ganze: {k} · {n} = {k * n} {e}.', 'h': 'Teile durch den Zähler, dann nimm mit dem Nenner mal.'}
    art = R.randrange(3)
    n = R.choice([4, 5, 6, 8, 10])
    z = R.randint(2, n - 1)
    while gcd(z, n) > 1: z = R.randint(2, n - 1)
    if art == 0:
        k = R.randint(1, 24 // n) if n <= 12 else 1
        if k * n < 6: return g_ganzes(3)
        t = z * k
        return {'y': 'zahl', 'f': {'text': f'Ein Wanderer hat {z}/{n} seines Weges geschafft. Das sind {t} km. Wie lang ist der ganze Weg?'}, 'o': {'wert': k * n, 'einheit': 'km'},
                'c': f'{t} / {z} * {n}', 'w': f'{t} km : {z} = {k} km (das ist 1/{n}). · {n} = {k * n} km.', 'h': 'Rückwärts rechnen: durch den Zähler, mal den Nenner.'}
    if art == 1:
        k = R.randint(3, 30)
        t = z * k
        return {'y': 'zahl', 'f': {'text': f'{z}/{n} der Plätze eines Kinos sind besetzt, das sind {t} Plätze. Wie viele Plätze sind noch frei?'}, 'o': {'wert': k * n - t},
                'c': f'{t} / {z} * {n} - {t}', 'w': f'Alle Plätze: {t} : {z} · {n} = {k * n}. Frei: {k * n} − {t} = {k * n - t}.', 'h': 'Berechne zuerst alle Plätze, dann ziehe die besetzten ab.'}
    k = R.randint(1, 100 // n) * 10
    if k * n < 100: return g_ganzes(3)
    t = z * k
    return {'y': 'zahl', 'f': {'text': f'Ein Wassertank ist zu {z}/{n} gefüllt und enthält {zt(t)} l. Wie viele Liter passen in den vollen Tank?'}, 'o': {'wert': k * n, 'einheit': 'l'},
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
    art = R.randrange(4)
    if art == 3:
        return kuerzbar_frage()
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


def primteiler(x): return [p for p in range(2, x + 1) if x % p == 0 and all(p % q for q in range(2, p))]


def kuerzbar_frage():
    """Kann man a/b kürzen? Etwa die Hälfte nicht kürzbar (teilerfremd, aber beide keine Primzahlen)."""
    while True:
        a, b = sorted(R.sample(range(8, 50), 2))
        if a in primteiler(a) or b in primteiler(b): continue
        g = gcd(a, b)
        if (R.random() < .5) != (g == 1): continue
        pa = [p for p in primteiler(a) if b % p]
        pb = [p for p in primteiler(b) if a % p]
        if g == 1:
            if not pa or not pb: continue
            r = f'Nein, {a} und {b} haben keinen gemeinsamen Teiler außer 1.'
            falsch = [f'Ja, durch {R.choice(pa)}.', f'Ja, durch {R.choice(pb)}.']
            w = f'Teiler von {a} (außer 1): ' + ', '.join(str(d) for d in range(2, a + 1) if a % d == 0) + f'. Keiner davon teilt {b}. Also kann man {a}/{b} nicht kürzen.'
        else:
            p = max(primteiler(g))
            if not pa: continue
            r = f'Ja, durch {p}.'
            falsch = ['Nein, sie haben keinen gemeinsamen Teiler außer 1.', f'Ja, durch {R.choice(pa)}.']
            w = f'{a} = {p} · {a // p} und {b} = {p} · {b // p}. Beide sind durch {p} teilbar: {a}/{b} = {a // p}/{b // p}.'
        return {**wahl(R, r, falsch, 3), 'f': {'text': f'Kann man {a}/{b} kürzen?'}, 'w': w,
                'h': 'Zerlege Zähler und Nenner in Faktoren. Gibt es einen Teiler, der in beiden steckt?'}


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
            while gcd(z, n) > 1: z = R.randint(1, n - 1)
            return mark(Fr(z, n), 0, 1, n * k, f'Markiere {z}/{n} am Zahlenstrahl (von 0 bis 1, {n * k} gleiche Teile).',
                        f'{z}/{n} = {z * k}/{n * k}. Also beim {z * k}. Strich nach der 0.', f'Erweitere {z}/{n} so, dass der Nenner {n * k} ist.')
        n = R.randint(2, 6)
        z = R.randint(n + 1, 2 * n - 1)
        if gcd(z, n) > 1: return g_strahl(2)
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
        return {'y': 'luecken', 'f': {'text': f'Der Zahlenstrahl von 0 bis 1 ist in {N} gleiche Teile geteilt. Auf welchen Bruch zeigt der Pfeil?',
                                      'schablone': '□/□', 'hinweis': HB + ' Vollständig gekürzt.',
                                      'grafik': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': N, 'beschriftet': 'anfang_ende', 'pfeil': int(idx)}}, 'o': {'werte': [z, n]}, 'c': [f'{idx} / {N} * {n}', f'{n}'],
                'w': f'Der Pfeil zeigt auf den {idx}. Strich nach der 0, also auf {idx}/{N}. Gekürzt: {z}/{n}.', 'h': 'Zähle die Striche bis zum Pfeil, schreibe Strich-Nummer / Anzahl der Teile und kürze dann.'}
    if art == 1:
        n = R.randint(2, 5)
        z = R.randint(1, n - 1)
        while gcd(z, n) > 1: z = R.randint(1, n - 1)
        x = 1 + Fr(z, n)
        return mark(x, 1, 2, n, f'Markiere {bruch(x)} am Zahlenstrahl (von 1 bis 2, {n} gleiche Teile).',
                    f'{bruch(x)} = 1 + {z}/{n}. Von der 1 aus {teile(z)} nach rechts.', 'Wie viele Ganze stecken in dem Bruch? Starte bei der 1.')
    n = R.choice([3, 4, 5, 6])
    z = R.randint(1, n - 1)
    while gcd(z, n) > 1: z = R.randint(1, n - 1)
    return mark(Fr(z, n), 0, 2, 4 * n, f'Markiere {z}/{n} am Zahlenstrahl (von 0 bis 2, {2 * n * 2} gleiche Teile).',
                f'Von 0 bis 1 sind es {2 * n} Teile, jeder ist 1/{2 * n}. {z}/{n} = {2 * z}/{2 * n}: beim {2 * z}. Strich.',
                'Wie viele Teile liegen zwischen 0 und 1? Damit erweiterst du den Bruch.')


# ---------- 8 Verstehen ----------
def brillen_aussage():
    """Realistisch: 1/4 bis 1/2 einer Klasse mit 20 bis 32 Kindern trägt eine Brille."""
    zb, nb = R.choice([(1, 4), (1, 3), (2, 5), (1, 2), (3, 8), (2, 7), (3, 10), (5, 12), (4, 9)])
    N = R.choice([x for x in range(20, 33) if x % nb == 0])
    t = N * zb // nb
    if R.random() < .5:
        return (f'In einer Klasse mit {N} Kindern tragen {t} eine Brille. Der Anteil ist {N}/{t}.', False,
                f'Nein, der Teil kommt in den Zähler, das Ganze in den Nenner: {t}/{N} = {zb}/{nb}.')
    return (f'In einer Klasse mit {N} Kindern tragen {t} eine Brille. Der Anteil ist {zb}/{nb}.', True,
            f'Ja: Anteil {t}/{N}, gekürzt mit {N // nb}: {zb}/{nb}.')


def g_verstehen(st):
    z, n = echt(R, 9)
    z, n = fl(Fr(z, n))
    if n == 1: return g_verstehen(st)
    k = R.randint(2, 6)
    if st == 1:
        aussagen = [
            (f'{z}/{n} und {z * k}/{n * k} sind gleich groß.', True, f'Ja, {z * k}/{n * k} ist {z}/{n} mit {k} erweitert.'),
            (f'{z}/{n} und {z + k}/{n + k} sind gleich groß.', False,
             f'Nein. {z + k}/{n + k} entsteht aus {z}/{n}, wenn man zu Zähler und Nenner {k} addiert – das ist kein Erweitern. '
             f'{z}/{n} = {z * kgv(n, n + k) // n}/{kgv(n, n + k)}, {z + k}/{n + k} = {(z + k) * kgv(n, n + k) // (n + k)}/{kgv(n, n + k)}.'),
            (f'1/{n} ist größer als 1/{n + k}.', True, f'Ja, bei 1/{n} ist das Ganze in weniger, also größere Stücke geteilt.'),
            (f'1/{n + k} ist größer als 1/{n}, weil {n + k} > {n}.', False, f'Nein, mehr Teile bedeuten kleinere Stücke: 1/{n + k} < 1/{n}.'),
        ]
    elif st == 2:
        g = n * R.randint(3, 12)
        aussagen = [
            (f'{z}/{n} von {g} sind {g // n * z}.', True, f'Ja: {g} : {n} = {g // n}' + (f', · {z} = {g // n * z}.' if z > 1 else '.')),
            (f'{z}/{n} von {g} sind {g // n * (z + 1) if z + 1 < n else g // n * z + 1}.', False, f'Nein: {g} : {n} = {g // n}' + (f', · {z} = {g // n * z}.' if z > 1 else '.')
             + (f' {g // n * (z + 1)} wären {z + 1}/{n}.' if z + 1 < n else '')),
            brillen_aussage(),
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
              offen=['Lehrplan „Anteile mit Flächendiagrammen veranschaulichen“: Flächendiagramme (Streifen, Rechteck-Raster, Kreis in gleiche Teile) sind jetzt in den Lernkarten und in den Aufgaben zu anteil_bestimmen eingebaut. Es fehlt nur noch das Selbst-Färben durch das Kind (kann die App nicht).',
                     'Prüfung (Aufgaben, anteil_bestimmen) schlug für „Anteil am Bild“ ein Kreisdiagramm mit zwei Sektoren (gefärbt/weiß) vor. Abweichend umgesetzt mit Bildtyp figur und sichtbaren gleich großen Teilen (Kreis, Streifen, Raster): Ohne Teilungslinien kann ein Kind den Anteil nicht ablesen, nur schätzen.',
                     'Brüche stehen im Text als 3/4 (Schrägstrich). Falls die App echte Bruchdarstellung bekommt, Texte umstellen.',
                     'Bei Markierungen mit Dritteln/Sechsteln fehlt das Feld „zahl“, weil 1/3 keine endliche Dezimalzahl ist; der Index wird vom Programm exakt berechnet.'])

# ---------- KARTEN: Lernkarten nach dem neuen Muster (Achte Runde, Vorgabe 16.11., Paket U6) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_kl6.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_kl6 import umbau  # noqa: E402

KARTEN = {
 'bruchteil_von': {
  'einstieg': 'In der Klassenkasse liegen 20 €. Drei Viertel davon sollen für Getränke ausgegeben werden. Das ist ein ⟦Bruchteil⟧ von 20 €.',
  'woerter': [['Bruchteil', 'ein Teil eines Ganzen, z. B. 3/4 von 20 €'],
              ['Nenner', 'die Zahl unter dem Strich: in wie viele gleiche Teile du das Ganze teilst'],
              ['Zähler', 'die Zahl über dem Strich: wie viele Teile du nimmst']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 0, 'ganzes': '20 €'},
  'schritte': [{'text': 'Der Nenner 4 sagt: Teile die 20 € in 4 gleiche Teile.'},
               {'text': 'Ein Teil ist 20 € : 4 = 5 €.', 'bild': {'gefaerbt': 1, 'teil_text': '5 €'}},
               {'text': 'Der Zähler 3 sagt: Nimm 3 Teile. 3 · 5 € = ⟦15 €⟧.', 'bild': {'gefaerbt': 3, 'teil_text': '15 €'}}],
  'fehler': 'Erst durch 3, dann mal 4 ergibt etwa 26,67 €. Das ist mehr, als in der Kasse liegt!',
  'regel': 'Erst durch den ⟦Nenner⟧, dann mal den Zähler. So sind 3/4 von 20 € genau 15 €.'},
 'anteil_bestimmen': {
  'einstieg': 'Von den 30 Kindern der Klasse spielen 12 ein Instrument. Sie gründen eine Band für das Fest. Welcher ⟦Anteil⟧ der Klasse ist das?',
  'woerter': [['Anteil', 'Teil durch Ganzes, als Bruch geschrieben'],
              ['kürzen', 'Zähler und Nenner durch dieselbe Zahl teilen; der Wert bleibt gleich']],
  'bild': {'typ': 'bruchstreifen', 'teile': 30, 'gefaerbt': 0, 'ganzes': '30 Kinder'},
  'schritte': [{'text': '12 von 30 Kindern spielen ein Instrument. Das ist der Bruch 12/30.', 'bild': {'gefaerbt': 12, 'teil_text': '12 Kinder'}},
               {'text': 'Fasse je 6 Kinder zusammen. Dann gibt es 5 Gruppen, 2 davon spielen.',
                'bild': {'zeilen': [{'teile': 5, 'gefaerbt': 2, 'teil_text': '2 von 5'}]}},
               {'text': 'Das heißt: durch 6 kürzen. Der Anteil ist ⟦2/5⟧.'}],
  'fehler': '30/12 hieße „30 von 12“. Dann gäbe es mehr Musiker als Kinder. Der Teil steht oben, das Ganze unten.',
  'regel': 'Anteil ist ⟦Teil durch Ganzes⟧. Der Teil kommt in den Zähler, das Ganze in den Nenner. Dann kürzen.'},
 'ganzes_bestimmen': {
  'einstieg': 'Die Band sagt: „Wir sind 2/5 der Klasse, nämlich 12 Kinder“. Wie viele Kinder hat die Klasse? Du suchst rückwärts das ⟦Ganze⟧.',
  'woerter': [['Ganze', 'alles zusammen, hier die ganze Klasse'],
              ['rückwärts', 'vom bekannten Teil zurück zum Ganzen rechnen']],
  'bild': {'typ': 'bruchstreifen', 'teile': 5, 'gefaerbt': 2, 'teil_text': '12 Kinder', 'ganzes': '? Kinder'},
  'schritte': [{'text': '2 Fünftel sind 12 Kinder. Ein Fünftel sind 12 : 2 = 6 Kinder.', 'bild': {'gefaerbt': 1, 'teil_text': '6 Kinder'}},
               {'text': 'Die ganze Klasse hat 5 Fünftel: 6 · 5 = ⟦30 Kinder⟧.', 'bild': {'gefaerbt': 5, 'teil_text': '', 'ganzes': '30 Kinder'}}],
  'fehler': '2/5 von 12 sind 4,8 Kinder – weniger als die Band selbst! Rückwärts heißt: durch den Zähler, mal den Nenner.',
  'regel': 'Rückwärts teilst du ⟦durch den Zähler⟧ und nimmst mal den Nenner. So kommst du vom Teil zum Ganzen.'},
 'erweitern': {
  'einstieg': 'Eine Tafel Schokolade hat 4 Riegel, du bekommst 3. Dann wird jeder Riegel in 5 Stücke gebrochen. Du hast mehr Stücke, aber gleich viel Schokolade: ⟦Erweitern⟧.',
  'woerter': [['Erweitern', 'Zähler und Nenner mit derselben Zahl malnehmen; der Wert bleibt gleich']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4'},
  'schritte': [{'text': 'Du hast 3 von 4 Riegeln, also 3/4 der Tafel.'},
               {'text': 'Jeder Riegel wird in 5 Stücke gebrochen: 4 · 5 = 20 Stücke.',
                'bild': {'zeilen': [{'teile': 20, 'gefaerbt': 0}]}},
               {'text': 'Deine 3 Riegel sind jetzt 3 · 5 = 15 Stücke. Also 3/4 = ⟦15/20⟧.',
                'bild': {'zeilen': [{'teile': 20, 'gefaerbt': 15, 'teil_text': '15/20'}]}}],
  'fehler': '3/4 = 3/20 ist falsch: Dann hättest du nur 3 kleine Stücke. Zähler und Nenner werden mit derselben Zahl malgenommen.',
  'fehler_bild': {'zeilen': [{'teile': 20, 'gefaerbt': 3, 'teil_text': '3/20'}]},
  'regel': 'Beim Erweitern nimmst du ⟦Zähler und Nenner⟧ mit derselben Zahl mal. Der Wert bleibt gleich.'},
 'kuerzen': {
  'einstieg': 'Von 24 Muffins sind 18 gegessen. „18 von 24“ ist unhandlich. Mit Gruppen zu je 6 Muffins sind 3 von 4 Gruppen weg: ⟦Kürzen⟧.',
  'woerter': [['Kürzen', 'Zähler und Nenner durch dieselbe Zahl teilen; der Wert bleibt gleich'],
              ['vollständig gekürzt', 'Zähler und Nenner haben keinen gemeinsamen Teiler außer 1 mehr']],
  'bild': {'typ': 'bruchstreifen', 'teile': 24, 'gefaerbt': 18, 'teil_text': '18 Muffins'},
  'schritte': [{'text': '18 von 24 Muffins sind gegessen. Das ist 18/24.'},
               {'text': '18 und 24 lassen sich beide durch 6 teilen.'},
               {'text': 'Je 6 Muffins bilden eine Gruppe: 3 von 4 Gruppen sind gegessen.',
                'bild': {'zeilen': [{'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4'}]}},
               {'text': 'Vollständig gekürzt ist 18/24 = ⟦3/4⟧.'}],
  'fehler': '18/24 = 9/12 stimmt, ist aber nicht vollständig gekürzt. 9 und 12 lassen sich noch durch 3 teilen: 3/4.',
  'fehler_bild': {'zeilen': [{'teile': 12, 'gefaerbt': 9, 'teil_text': '9/12'}]},
  'regel': 'Beim Kürzen teilst du ⟦Zähler und Nenner⟧ durch dieselbe Zahl. Kürze, bis es nicht mehr geht.'},
 'vergleichen': {
  'einstieg': 'Vom Apfelkuchen ist noch 3/4 übrig, vom Schokokuchen 5/6. Die Stücke sind verschieden groß. Schneidest du beide gleich fein, heißt die Stückzahl ⟦Hauptnenner⟧.',
  'woerter': [['Hauptnenner', 'die kleinste Zahl, in die beide Nenner passen']],
  'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4', 'zeilen': [{'teile': 6, 'gefaerbt': 5, 'teil_text': '5/6'}]},
  'schritte': [{'text': '12 steht in der Viererreihe und in der Sechserreihe. 12 ist der Hauptnenner.'},
               {'text': 'Erweitere beide: 3/4 = 9/12 und 5/6 = 10/12.',
                'bild': {'teile': 12, 'gefaerbt': 9, 'teil_text': '9/12', 'zeilen': [{'teile': 12, 'gefaerbt': 10, 'teil_text': '10/12'}]}},
               {'text': '10 Stücke sind mehr als 9. Also ist ⟦5/6 größer⟧.'}],
  'fehler': '„3/8 ist größer als 3/5, weil 8 > 5“ ist falsch. Achtel sind kleinere Stücke als Fünftel.',
  'fehler_bild': {'teile': 8, 'gefaerbt': 3, 'teil_text': '3/8', 'zeilen': [{'teile': 5, 'gefaerbt': 3, 'teil_text': '3/5'}]},
  'regel': 'Bei gleichem Nenner gewinnt der größere ⟦Zähler⟧. Sonst erweiterst du zuerst auf den Hauptnenner.'},
 'zahlenstrahl': {
  'einstieg': 'Der Weg zur Festwiese ist 1 km lang. 4 Schilder teilen ihn in 5 gleich lange Stücke. So eine Linie mit Strichen heißt ⟦Zahlenstrahl⟧.',
  'woerter': [['Zahlenstrahl', 'eine Linie, auf der die Zahlen der Reihe nach in gleichen Abständen liegen']],
  'bild': {'typ': 'zahlenstrahl', 'start': 0, 'ende': 1, 'abschnitte': 5, 'beschriftet': 'anfang_ende'},
  'schritte': [{'text': 'Der Nenner 5 sagt: Teile die Strecke von 0 bis 1 in 5 Stücke.'},
               {'text': 'Der Zähler 3 sagt: Geh 3 Stücke nach rechts.',
                'bild': {'boegen': [{'von': 0, 'bis': 0.2}, {'von': 0.2, 'bis': 0.4}, {'von': 0.4, 'bis': 0.6}]}},
               {'text': 'Beim 3. Strich liegt ⟦3/5⟧.', 'bild': {'punkte': [{'wert': 0.6, 'name': '3/5', 'zahl': False}]}}],
  'fehler': '3/5 beim 5. Strich ist falsch. Dort bist du schon an der Festwiese, also bei 1.',
  'fehler_bild': {'boegen': [], 'punkte': [{'wert': 1, 'name': '5/5 = 1', 'zahl': False}]},
  'regel': 'Der ⟦Nenner⟧ teilt die Strecke, der Zähler zählt die Stücke. Zähle von 0 aus nach rechts.'},
 'verstehen': {
  'einstieg': 'Ein Kind sagt: „1/4 Pizza ist mehr als 1/2, denn 4 > 2“. Legst du beide Stücke nebeneinander, siehst du: falsch. Ein Beispiel gegen eine Aussage heißt ⟦Gegenbeispiel⟧.',
  'woerter': [['Gegenbeispiel', 'ein Beispiel, das zeigt: Die Aussage stimmt nicht immer']],
  'bild': {'typ': 'bruchstreifen', 'teile': 2, 'gefaerbt': 1, 'teil_text': '1/2', 'zeilen': [{'teile': 4, 'gefaerbt': 1, 'teil_text': '1/4'}]},
  'schritte': [{'text': 'Die Aussage: Ein Bruch mit größerem Nenner ist größer.'},
               {'text': 'Teste 1/2 und 1/4: 1/2 = 2/4, und 2/4 ist mehr als 1/4.',
                'bild': {'teile': 4, 'gefaerbt': 2, 'teil_text': '1/2 = 2/4'}},
               {'text': 'Das ist ein Gegenbeispiel. Die Aussage ist ⟦falsch⟧.'}],
  'fehler': 'Ein passendes Beispiel beweist nichts: 1/4 < 3/5 passt nur zufällig. Ein einziges Gegenbeispiel widerlegt die Aussage.',
  'regel': 'Prüfe Aussagen ⟦mit Zahlen⟧. Ein einziges Gegenbeispiel genügt, um sie zu widerlegen.'},
}

umbau(DATEI, KARTEN)



# ---------- SCHWER (Zehnte Runde, Zweig schwer-kl6): je Lernkarte 2 Übungen Stufe 2 + 4 Übungen Stufe 3 ----------
# Läuft nach allen bisherigen Aufgaben mit eigenem Zufallsstart; die bisherigen Aufgaben bleiben unverändert.
# Prüfungsvorbilder: Bayerischer Mathematik-Test Jgst. 8 (ISB) 2023 Aufg. 5a (fehlender Restanteil), 2024 Aufg. 3b/3c (Aussagen zu
# Anteilen prüfen, „ein Drittel“; Gesamtzahl aus Anzahl und Anteil), 2025 Aufg. 6d (gleicher Anteil, verschiedene Gesamtzahlen);
# Jahrgangsstufentest Realschule Jgst. 6 (ISB) 2024 Nr. 16 (Ganzes aus gleichen Teilen); Känguru 5/6 (2021): Mischungen vergleichen,
# Anteil einer Fläche; IQB VERA-8 „Anteile in geometrischen Objekten“: Falle Verhältnis statt Anteil.
from _schwer_kl6 import ergaenzen, zahl, wahl, luecken, anteil, mark  # noqa: E402

_JA_NEIN = 'Rechne beide Seiten mit Zahlen nach, bevor du entscheidest.'


def _br():
    return {
        'bruchteil_von': [
            (2, lambda R: zahl('Wie viele Gramm sind 3/5 von 2 kg?', 1200, '2000 / 5 * 3', 'Rechne 2 kg zuerst in Gramm um.',
                               '2 kg = 2 000 g. 2 000 g : 5 = 400 g. 400 g · 3 = 1 200 g.', einheit='g')),
            (2, lambda R: zahl('Ein Tag hat 24 Stunden. Ein Kind schläft 3/8 des Tages. Wie viele Stunden sind das?', 9, '24 / 8 * 3',
                               'Durch den Nenner teilen, mit dem Zähler malnehmen.', '24 h : 8 = 3 h. 3 h · 3 = 9 h.', einheit='h')),
            (3, lambda R: zahl('Ein Schulfest bringt 360 € ein. 1/4 davon bekommt die Klassenkasse, 2/5 der Förderverein, '
                               'den Rest ein Tierheim. Wie viel Euro bekommt das Tierheim?', 126, '360 - 360 / 4 - 360 / 5 * 2',
                               'Rechne zuerst die beiden Teile aus und ziehe sie von 360 € ab.',
                               '1/4 von 360 € = 90 €. 2/5 von 360 € = 144 €. 360 € − 90 € − 144 € = 126 €.', einheit='€')),
            (3, lambda R: zahl('Von 48 Kindern fahren 1/3 mit dem Bus. Von den übrigen Kindern kommt die Hälfte mit dem Rad. '
                               'Wie viele Kinder kommen mit dem Rad?', 16, '(48 - 48 / 3) / 2',
                               'Achtung: Die Hälfte bezieht sich nur auf die übrigen Kinder, nicht auf alle 48.',
                               '1/3 von 48 = 16 Kinder fahren Bus. Übrig: 48 − 16 = 32. Die Hälfte davon: 32 : 2 = 16 Kinder.')),
            (3, lambda R: zahl('Was ist mehr: 2/3 von 90 € oder 3/4 von 80 €? Gib den Unterschied in Euro an.', 0,
                               '90 / 3 * 2 - 80 / 4 * 3', 'Rechne beide Bruchteile einzeln aus.',
                               '2/3 von 90 € = 60 €. 3/4 von 80 € = 60 €. Beide sind gleich, der Unterschied ist 0 €.', einheit='€')),
            (3, lambda R: zahl('Ein Kind rechnet 3/5 von 40 m so: 40 · 5 : 3. Welches Ergebnis ist richtig? Gib es in Metern an.', 24,
                               '40 / 5 * 3', 'Welche Zahl gehört zum Teilen, welche zum Malnehmen?',
                               'Richtig: durch den Nenner 5 teilen, mit dem Zähler 3 malnehmen. 40 m : 5 = 8 m, 8 m · 3 = 24 m. '
                               'Das Kind hat Zähler und Nenner vertauscht.', einheit='m')),
        ],
        'anteil_bestimmen': [
            (2, lambda R: anteil('Welcher Anteil eines Tages sind 8 Stunden?', 8, 24, 'Ein Tag hat 24 Stunden.',
                                 'Anteil = 8/24. Durch 8 kürzen: 1/3.')),
            (2, lambda R: anteil('Welcher Anteil von 2 kg sind 250 g?', 250, 2000, 'Rechne beide Angaben in dieselbe Einheit um.',
                                 '2 kg = 2 000 g. Anteil = 250/2 000. Durch 250 kürzen: 1/8.')),
            (3, lambda R: anteil('Ein Saft wird aus 2 Teilen Sirup und 3 Teilen Wasser gemischt. Welcher Anteil der Mischung ist Sirup?', 2, 5,
                                 'Wie viele Teile hat die ganze Mischung?',
                                 'Die Mischung hat 2 + 3 = 5 Teile, davon 2 Teile Sirup. Anteil 2/5 (nicht 2/3 – das wäre Sirup im Vergleich zu Wasser).')),
            (3, lambda R: anteil('In der 6a sind 12 von 30 Kindern im Sportverein, in der 6b 9 von 20 Kindern. '
                                 'Welcher Anteil aller Kinder beider Klassen ist im Sportverein?', 21, 50,
                                 'Zähle alle Vereinskinder und alle Kinder zusammen. Brüche einfach addieren geht hier nicht.',
                                 'Im Verein: 12 + 9 = 21 Kinder. Alle: 30 + 20 = 50 Kinder. Anteil 21/50.')),
            (3, lambda R: anteil('Ein Kind gibt 1/3 seines Taschengelds aus und danach die Hälfte vom Rest. Welcher Anteil des Taschengelds ist noch übrig?',
                                 1, 3, 'Probiere mit einem Betrag, z. B. 30 €.',
                                 'Mit 30 €: 1/3 sind 10 €, Rest 20 €. Die Hälfte davon (10 €) wird ausgegeben. Übrig 10 € von 30 €, also 1/3.')),
            (3, lambda R: zahl('In einer Dose liegen 3 rote und 5 blaue Kugeln. Wie viele rote Kugeln musst du dazulegen, '
                               'damit genau die Hälfte aller Kugeln rot ist?', 2, '5 - 3',
                               'Bei der Hälfte gibt es gleich viele rote wie blaue Kugeln.',
                               'Die Hälfte ist rot, wenn es gleich viele rote wie blaue sind: 5 rote. Es fehlen 5 − 3 = 2 rote Kugeln.')),
        ],
        'ganzes_bestimmen': [
            (2, lambda R: zahl('18 Seiten sind 3/8 eines Hefts. Wie viele Seiten hat das Heft?', 48, '18 / 3 * 8',
                               'Durch den Zähler teilen, mit dem Nenner malnehmen.', '18 : 3 = 6 Seiten sind 1/8. 6 · 8 = 48 Seiten.')),
            (2, lambda R: zahl('Nach 2/5 der Fahrt hat ein Bus 60 km geschafft. Wie lang ist die ganze Fahrt?', 150, '60 / 2 * 5',
                               'Wie viele km sind 1/5 der Fahrt?', '60 km : 2 = 30 km sind 1/5. 30 km · 5 = 150 km.', einheit='km')),
            (3, lambda R: zahl('Ein Riesenrad hat 20 gleiche Gondeln. 4 Gondeln haben zusammen 24 Sitzplätze. '
                               'Wie viele Sitzplätze hat das ganze Riesenrad?', 120, '24 / 4 * 20',
                               'Welcher Anteil des Riesenrads sind 4 Gondeln? Oder: Wie viele Plätze hat eine Gondel?',
                               '4 von 20 Gondeln sind 1/5 des Rads. 24 Plätze · 5 = 120 Plätze. (Oder: 24 : 4 = 6 Plätze je Gondel, 6 · 20 = 120.)')),
            (3, lambda R: zahl('Bei einer Umfrage nannten 45 Kinder Fußball als Lieblingssport. Das waren 3/8 aller Befragten. '
                               'Wie viele Befragte nannten etwas anderes?', 75, '45 / 3 * 8 - 45',
                               'Bestimme zuerst, wie viele Kinder insgesamt befragt wurden.',
                               '45 : 3 = 15 sind 1/8. Alle: 15 · 8 = 120 Kinder. Etwas anderes: 120 − 45 = 75 Kinder.')),
            (3, lambda R: zahl('Ein Kind gibt 1/4 seines Geldes aus und hat danach noch 27 €. Wie viel Geld hatte es vorher?', 36, '27 / 3 * 4',
                               'Die 27 € sind nicht 1/4, sondern der Rest. Welcher Anteil ist der Rest?',
                               'Übrig sind 3/4 des Geldes = 27 €. 27 € : 3 = 9 € sind 1/4. 9 € · 4 = 36 €.', einheit='€')),
            (3, lambda R: zahl('Ein Kind rechnet: „2/3 sind 16 Liter, also ist das Ganze 2/3 von 16 Litern.“ Wie viele Liter ist das Ganze wirklich?', 24,
                               '16 / 2 * 3', 'Rückwärts: durch den Zähler, mal den Nenner.',
                               '16 l : 2 = 8 l sind 1/3. 8 l · 3 = 24 l. 2/3 von 16 l wären weniger als 16 l – das kann nicht das Ganze sein.', einheit='l')),
        ],
        'erweitern': [
            (2, lambda R: luecken('Ergänze: 7/12 = □/60', '□', 'Trage den Zähler ein.', [35], ['7 * (60 // 12)'],
                                  'Mit welcher Zahl wird 12 zu 60?', '12 · 5 = 60, also auch 7 · 5 = 35. 7/12 = 35/60.')),
            (2, lambda R: luecken('Erweitere 5/8 so, dass der Nenner 1 000 ist.', '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite.',
                                  [625, 1000], ['5 * 125', '8 * 125'], 'Mit welcher Zahl wird 8 zu 1 000?', '8 · 125 = 1 000, also 5 · 125 = 625. 5/8 = 625/1 000.')),
            (3, lambda R: luecken('Bringe 2/3 und 3/4 auf den kleinsten gemeinsamen Nenner.', '2/3 = □/□;  3/4 = □/□',
                                  'Zähler und Nenner der beiden erweiterten Brüche eintragen.', [8, 12, 9, 12], ['2 * 4', '3 * 4', '3 * 3', '4 * 3'],
                                  'Suche die kleinste Zahl, die in der Dreier- und in der Viererreihe steht.',
                                  'Kleinster gemeinsamer Nenner: 12. 2/3 mit 4 erweitern: 8/12. 3/4 mit 3 erweitern: 9/12.')),
            (3, lambda R: luecken('Erweitere 3/5 so, dass Zähler und Nenner zusammen 48 ergeben.', '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite.',
                                  [18, 30], ['3 * (48 // 8)', '5 * (48 // 8)'], 'Bei 3/5 sind Zähler und Nenner zusammen 8. Wie oft passt 8 in 48?',
                                  '3 + 5 = 8 und 48 : 8 = 6. Mit 6 erweitern: 18/30. Probe: 18 + 30 = 48.')),
            (3, lambda R: luecken('Ein Bruch wurde mit 4 erweitert. Jetzt heißt er 12/28. Wie hieß er vorher?', '□/□',
                                  'Zähler ins erste Kästchen, Nenner ins zweite.', [3, 7], ['12 // 4', '28 // 4'],
                                  'Rückwärts: Was ist das Gegenteil von „mit 4 erweitern“?', 'Zähler und Nenner durch 4 teilen: 12 : 4 = 3, 28 : 4 = 7. Vorher 3/7.')),
            (3, lambda R: wahl(R, 'Welcher Bruch ist NICHT gleich 3/4?', '9/16', ['6/8', '15/20', '75/100'],
                               'Prüfe bei jedem Bruch: Wurden Zähler und Nenner mit derselben Zahl malgenommen?',
                               '6/8 (mal 2), 15/20 (mal 5), 75/100 (mal 25) sind gleich 3/4. Bei 9/16 wurde der Zähler mal 3, der Nenner mal 4 genommen.')),
        ],
        'kuerzen': [
            (2, lambda R: anteil('Kürze 42/56 vollständig.', 42, 56, 'Der größte gemeinsame Teiler von 42 und 56 steht in der Siebenerreihe.',
                                 'ggT(42, 56) = 14. 42 : 14 = 3, 56 : 14 = 4. Also 3/4.')),
            (2, lambda R: anteil('Kürze 64/80 vollständig.', 64, 80, 'Kürze schrittweise, z. B. zuerst durch 8.',
                                 '64/80 durch 8: 8/10, durch 2: 4/5. (Oder gleich durch 16.)')),
            (3, lambda R: anteil('Ein Fußballspiel dauert 90 Minuten. Eine Mannschaft hat 54 Minuten lang den Ball. '
                                 'Welcher Anteil der Spielzeit ist das? Vollständig gekürzt.', 54, 90,
                                 'Teil durch Ganzes, dann kürzen.', 'Anteil 54/90. ggT = 18: 54 : 18 = 3, 90 : 18 = 5. Also 3/5.')),
            (3, lambda R: zahl('Wie viele der Brüche 1/12, 2/12, 3/12, …, 11/12 lassen sich NICHT kürzen?', 4, '11 - 7',
                               'Ein Bruch lässt sich kürzen, wenn Zähler und 12 einen gemeinsamen Teiler haben (2 oder 3).',
                               'Kürzbar sind die Zähler 2, 3, 4, 6, 8, 9, 10 (7 Stück). Nicht kürzbar: 1, 5, 7, 11 – also 4 Brüche.')),
            (3, lambda R: wahl(R, 'Ein Kind „kürzt“ 16/64, indem es in Zähler und Nenner die 6 streicht. Es erhält 1/4. Was stimmt?',
                               'Das Ergebnis stimmt zufällig, aber Ziffern streichen ist kein Kürzen.',
                               ['So darf man immer kürzen.', 'Das Ergebnis ist falsch, richtig ist 4/16.', 'Das Ergebnis ist falsch, 16/64 lässt sich nicht kürzen.'],
                               'Kürze 16/64 richtig: durch welche Zahl kann man Zähler und Nenner teilen?',
                               '16/64 durch 16 gekürzt ist wirklich 1/4. Ziffern streichen klappt aber meist nicht, z. B. 12/24 wäre nach Streichen der 2 dann 1/4 – richtig ist 1/2.')),
            (3, lambda R: anteil('Kürze vollständig, am besten vor dem Ausrechnen: (12 · 25)/(15 · 40)', 12 * 25, 15 * 40,
                                 'Zerlege die Zahlen in Faktoren und kürze gleiche Faktoren oben und unten.',
                                 '12 · 25 = 300, 15 · 40 = 600. 300/600 = 1/2. Mit Faktoren: 12/40 = 3/10 und 25/15 = 5/3, zusammen (3 · 5)/(10 · 3) = 1/2.')),
        ],
        'vergleichen': [
            (2, lambda R: wahl(R, 'Welcher Bruch ist größer: 5/8 oder 7/12?', '5/8', ['7/12', 'Beide sind gleich groß'],
                               'Hauptnenner von 8 und 12 ist 24.', '5/8 = 15/24 und 7/12 = 14/24. 15 > 14, also ist 5/8 größer.', n=3)),
            (2, lambda R: wahl(R, 'Welcher Bruch ist kleiner: 4/9 oder 1/2?', '4/9', ['1/2', 'Beide sind gleich groß'],
                               'Wie viele Neuntel wären genau die Hälfte?', 'Hauptnenner 18: 4/9 = 8/18 und 1/2 = 9/18. 8 < 9, also ist 4/9 kleiner.', n=3)),
            (3, lambda R: wahl(R, 'Drei Saftmischungen: A aus 1 Teil Sirup und 3 Teilen Wasser, B aus 2 Teilen Sirup und 5 Teilen Wasser, '
                                  'C aus 3 Teilen Sirup und 8 Teilen Wasser. Welche Mischung schmeckt am stärksten nach Sirup?',
                               'B', ['A', 'C', 'Alle gleich stark'],
                               'Bestimme für jede Mischung den Anteil Sirup an der ganzen Mischung und vergleiche.',
                               'Anteile Sirup: A 1/4, B 2/7, C 3/11. Hauptnenner 308: A 77/308, B 88/308, C 84/308. Am meisten Sirup hat B.')),
            (3, lambda R: zahl('Welche natürliche Zahl kannst du für □ einsetzen, damit 2/5 < □/10 < 3/5 gilt?', 5, '(4 + 6) // 2',
                               'Erweitere 2/5 und 3/5 auf den Nenner 10.', '2/5 = 4/10 und 3/5 = 6/10. Zwischen 4/10 und 6/10 liegt nur 5/10, also □ = 5.')),
            (3, lambda R: wahl(R, 'Ordne 2/3, 3/5 und 5/8 der Größe nach. Welcher Bruch steht in der Mitte?', '5/8', ['2/3', '3/5'],
                               'Hauptnenner von 3, 5 und 8 ist 120.', '2/3 = 80/120, 3/5 = 72/120, 5/8 = 75/120. Reihenfolge: 3/5 < 5/8 < 2/3. In der Mitte: 5/8.', n=3)),
            (3, lambda R: wahl(R, 'Ein Kind sagt: „3/4 < 4/5 < 5/6.“ Stimmt das?',
                               'Ja: Bis zum Ganzen fehlen 1/4, 1/5 und 1/6 – und 1/6 ist am kleinsten.',
                               ['Nein, alle drei sind gleich groß.', 'Nein, 3/4 ist am größten.', 'Nein, das kann man ohne Hauptnenner nicht entscheiden.'],
                               'Wie viel fehlt jedem Bruch bis zu 1?',
                               '3/4 fehlt 1/4, 4/5 fehlt 1/5, 5/6 fehlt 1/6. Je weniger fehlt, desto größer der Bruch. Die Reihenfolge stimmt.')),
        ],
        'zahlenstrahl': [
            (2, lambda R: mark('Markiere 3/2 am Zahlenstrahl (von 0 bis 3, 12 gleiche Teile).', 0, 3, 12, 6,
                               'Wie viele Teile kommen auf die Strecke von 0 bis 1?', 'Von 0 bis 1 sind es 4 Teile, jeder Teil ist 1/4. 3/2 = 6/4, also 6 Teile nach rechts.', Fr(3, 2))),
            (2, lambda R: mark('Markiere 2/5 am Zahlenstrahl (von 0 bis 1, 10 gleiche Teile).', 0, 1, 10, 4,
                               'Erweitere 2/5 auf Zehntel.', '2/5 = 4/10. Also 4 Teile von 0 aus nach rechts.', Fr(2, 5))),
            (3, lambda R: mark('Markiere die Zahl, die genau in der Mitte zwischen 1/4 und 1/2 liegt (Zahlenstrahl von 0 bis 1, 8 gleiche Teile).', 0, 1, 8, 3,
                               'Schreibe 1/4 und 1/2 in Achteln.', '1/4 = 2/8 und 1/2 = 4/8. Die Mitte ist 3/8, also der 3. Strich.', Fr(3, 8))),
            (3, lambda R: mark('Markiere die Zahl, die um 3/10 größer ist als 3/2 (Zahlenstrahl von 0 bis 2, 10 gleiche Teile).', 0, 2, 10, 9,
                               'Jeder Teil ist hier 2/10 = 1/5 lang. Schreibe die gesuchte Zahl in Zehnteln.',
                               '3/2 + 3/10 = 15/10 + 3/10 = 18/10. Jeder Teil ist 2/10, also 18 : 2 = 9 Teile nach rechts.', Fr(9, 5))),
            (3, lambda R: zahl('Auf einem Zahlenstrahl ist die Strecke von 0 bis 1 in 6 gleiche Teile geteilt. Beim wievielten Strich nach der 0 liegt 4/3?', 8,
                               '4 * 6 // 3', 'Ein Teil ist 1/6. Schreibe 4/3 in Sechsteln.', '4/3 = 8/6. Also beim 8. Strich nach der 0.')),
            (3, lambda R: zahl('Auf einem Zahlenstrahl liegt 3/5 genau beim 9. Strich nach der 0. In wie viele gleiche Teile ist die Strecke von 0 bis 1 geteilt?', 15,
                               '9 * 5 // 3', 'Rückwärts: 3/5 = 9/□. Mit welcher Zahl wurde erweitert?', '3/5 = 9/15 (mit 3 erweitert). Die Strecke von 0 bis 1 hat 15 Teile.')),
        ],
        'verstehen': [
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „3/4 von 20 ist dasselbe wie 4/3 von 20.“', 'Nein: 3/4 von 20 = 15, 4/3 von 20 ist mehr als 20.',
                               ['Ja, es kommen dieselben Zahlen vor.', 'Das kann man nicht entscheiden.'], _JA_NEIN,
                               '3/4 von 20 = 20 : 4 · 3 = 15. 4/3 ist mehr als ein Ganzes, also ist 4/3 von 20 mehr als 20.', n=3)),
            (2, lambda R: wahl(R, 'Stimmt die Aussage? „Ein Bruch mit dem Zähler 1 und einem Nenner größer als 2 ist kleiner als 1/2.“',
                               'Ja: Bei mehr als 2 Teilen ist jedes Stück kleiner als eine Hälfte.',
                               ['Nein, Gegenbeispiel 1/3.', 'Das kann man nicht entscheiden.'], _JA_NEIN,
                               '1/3, 1/4, 1/5 … – je größer der Nenner, desto kleiner das Stück. Alle sind kleiner als 1/2.', n=3)),
            (3, lambda R: wahl(R, 'In einer Klasse spielen 9 von 28 Kindern ein Instrument. Lisa sagt: „Das ist mehr als ein Drittel der Klasse.“ Stimmt das?',
                               'Nein: 9/28 ist knapp weniger als 1/3.',
                               ['Ja: 9/28 ist mehr als 1/3.', 'Ja: 9 ist ein Drittel von 27, und 28 ist mehr.', 'Es ist genau ein Drittel.'],
                               'Vergleiche 9/28 und 1/3 mit dem Hauptnenner 84.',
                               '9/28 = 27/84 und 1/3 = 28/84. 27/84 < 28/84, also ist es etwas weniger als ein Drittel. (Ein Drittel von 28 wären 9 1/3 Kinder.)')),
            (3, lambda R: wahl(R, 'In der Klasse A (16 Kinder) lesen 1/2 der Kinder gern, in der Klasse B (30 Kinder) 1/3. Max sagt: '
                                  '„In A lesen mehr Kinder gern, weil 1/2 größer ist als 1/3.“ Stimmt das?',
                               'Nein: In A sind es 8 Kinder, in B 10 Kinder.',
                               ['Ja, ein größerer Anteil heißt immer mehr Kinder.', 'Ja, in A sind es 8, in B nur 3 Kinder.', 'Beide Klassen haben gleich viele Leser.'],
                               'Rechne die Anzahlen aus. Die Klassen sind verschieden groß.',
                               '1/2 von 16 = 8, 1/3 von 30 = 10. Der größere Anteil gehört hier zur kleineren Anzahl, weil Klasse A kleiner ist.')),
            (3, lambda R: wahl(R, 'Stimmt die Aussage? „Zwischen 1/3 und 1/2 liegt kein weiterer Bruch.“', 'Nein, zum Beispiel liegt 5/12 dazwischen.',
                               ['Ja, 1/3 und 1/2 sind Nachbarn.', 'Nein, zum Beispiel liegt 2/3 dazwischen.', 'Nein, zum Beispiel liegt 1/4 dazwischen.'],
                               'Schreibe beide Brüche mit dem Nenner 12.',
                               '1/3 = 4/12 und 1/2 = 6/12. Dazwischen liegt 5/12. (Zwischen zwei Brüchen liegt sogar immer ein weiterer.)')),
            (3, lambda R: wahl(R, 'Ein Kind „erweitert“ 2/3 so: (2 + 4)/(3 + 4) = 6/7. Was ist der Fehler?',
                               'Erweitern heißt malnehmen, nicht addieren: Mit 4 erweitert ist 2/3 = 8/12.',
                               ['Es gibt keinen Fehler.', 'Man darf nur den Nenner verändern.', 'Man hätte 4 abziehen müssen.'],
                               'Vergleiche 2/3 und 6/7: Sind sie gleich groß?',
                               '2/3 = 14/21, 6/7 = 18/21 – verschieden. Beim Erweitern werden Zähler und Nenner mit derselben Zahl malgenommen: 8/12.')),
        ],
    }


ergaenzen(DATEI, _br(), seed=6021)


# ---- BEFUNDE (Dreizehnte Runde: Befundliste aus Runde 10 abarbeiten, siehe _befunde.py) ----
from _befunde import Befunde, befunde_anwenden  # noqa: E402

BF = Befunde('bruch.brueche', 13_6_2)
# a) Standardumrechnung → Stufe 2
BF.stufe('bruchteil_von', 'Wie viele Minuten sind 3/4 Stunde?', 2)
BF.stufe('bruchteil_von', 'Wie viele g sind 3/8 kg?', 2)
# a) Grundform → Stufe 1
BF.stufe('erweitern', 'Erweitere 1/10 auf den Nenner 100.', 1)
BF.stufe('verstehen', 'Stimmt die Aussage? „1/2 ist größer als 1/3.“', 1)
BF.stufe('verstehen', 'Stimmt die Aussage? „1/2 ist größer als 1/5.“', 1)
# a) Hauptnenner 36 nötig → Stufe 2
BF.stufe('verstehen', 'Stimmt die Aussage? „1/9 und 4/12 sind gleich groß.“', 2)
# d) verlangt Subtraktion ungleichnamiger Brüche (Stoff von bruch.rechnen, die Lernkarte erklärt nur Vergleichen) → Vergleichsaufgabe
BF.ersetze('vergleichen', 'Um wie viel ist 5/6 größer als 4/7?', BF.A(
    'Welcher Bruch liegt näher an 1: 5/6 oder 6/7?', '6/7', ['5/6', 'Beide liegen gleich nah an 1.'],
    'Bis 1 fehlen bei 5/6 noch 1/6, bei 6/7 nur 1/7. 1/7 ist kleiner als 1/6, also liegt 6/7 näher an 1. (Probe mit Hauptnenner 42: 35/42 < 36/42.)',
    'Wie viel fehlt jeweils bis zum Ganzen? Vergleiche die fehlenden Stücke.'))
BF.nicht_umgesetzt('zahlenstrahl: Markierungen mit Dritteln/Sechsteln ohne Feld „zahl“', 'Von Hand geprüft und richtig (laut Befund); kein Mangel.')

befunde_anwenden(DATEI, BF)
# ---- BEFUNDE ENDE ----


# ---------- LUECKEN (Achtzehnte Runde, Teil B, Zweig luecken-kl6) ----------
# Läuft nach allen bisherigen Abschnitten mit eigenem Zufallsstart; vorhandene Karten und Aufgaben bleiben unverändert.
# Lehrplan: LehrplanPLUS Gymnasium Bayern M6 1.1 (Hauptnenner „ggf. per Primfaktorzerlegung“; Brüche als Zahlen, ℕ/ℤ/ℚ, positive und negative
# Bruchzahlen am Zahlenstrahl begründet ordnen), M6 1.3/1.4 (gemischte Zahlen). Prüfungsvorbilder: Grundwissentest Mathematik Jgst. 7 der
# Realschule (ISB) 2013 Nr. 2 (Zahl in der Mitte zwischen zwei Zahlen) und Nr. 5 („ein Fünftel der Zahl 3“: Bruch als Quotient),
# 2015 Nr. 2 (Bruch mit vorgegebenem Nenner zwischen zwei Brüchen), 2022 Nr. 3 (Brüche ordnen), 2024 Nr. 5 (Menge aus einem Anteil).
from _luecken_kl6 import karte_neu, karte_erweitern, zahl, wahl, mark, gemischt, bruch as lbruch  # noqa: E402


def _gem_aufgaben():
    U = 'uebung'
    def b(t, E, h, w): return lambda R: lbruch(t, E, h, w)
    def g(t, E, h, w): return lambda R: gemischt(t, E, h, w)
    UM = 'Ganze mal Nenner, dann den Zähler dazuzählen.'
    ZU = 'Teile Zähler durch Nenner. Das Ergebnis sind die Ganzen, der Rest ist der neue Zähler.'
    return [
        (U, 1, b('Schreibe 3 1/2 als unechten Bruch.', '3 + 1/2', UM, '3 Ganze sind 6/2. Dazu 1/2: 7/2.')),
        (U, 1, b('Schreibe 1 2/5 als unechten Bruch.', '1 + 2/5', UM, '1 Ganzes sind 5/5. Dazu 2/5: 7/5.')),
        (U, 1, g('Schreibe 9/4 als gemischte Zahl.', '9/4', ZU, '9 : 4 = 2 Rest 1. Also 9/4 = 2 1/4.')),
        (U, 1, g('Schreibe 7/3 als gemischte Zahl.', '7/3', ZU, '7 : 3 = 2 Rest 1. Also 7/3 = 2 1/3.')),
        (U, 2, b('Schreibe 4 5/6 als unechten Bruch.', '4 + 5/6', UM, '4 · 6 = 24 Sechstel. 24 + 5 = 29. Also 29/6.')),
        (U, 2, g('Schreibe 23/8 als gemischte Zahl.', '23/8', ZU, '23 : 8 = 2 Rest 7. Also 23/8 = 2 7/8.')),
        (U, 2, g('Schreibe 18/4 als gemischte Zahl. Kürze den Restbruch.', '18/4', 'Teile mit Rest. Prüfe danach, ob der Restbruch kürzbar ist.',
                 '18 : 4 = 4 Rest 2, also 4 2/4. Gekürzt: 4 1/2.')),
        (U, 2, lambda R: wahl(R, 'Welche Zahl ist größer: 2 3/5 oder 13/5?', 'Beide sind gleich groß.', ['2 3/5', '13/5'],
                              'Schreibe 2 3/5 als unechten Bruch.', '2 3/5 = 10/5 + 3/5 = 13/5. Beide Zahlen sind gleich.', n=3)),
        (U, 2, lambda R: wahl(R, 'Zwischen welchen ganzen Zahlen liegt 47/6?', 'zwischen 7 und 8', ['zwischen 4 und 5', 'zwischen 6 und 7', 'zwischen 8 und 9'],
                              'Wie oft passt 6 in 47?', '47 : 6 = 7 Rest 5, also 47/6 = 7 5/6. Das liegt zwischen 7 und 8.')),
        (U, 2, lambda R: zahl('Wie viele Viertelstunden sind 3 1/4 Stunden?', 13, '(3 + 1/4) * 4', 'Eine Stunde hat 4 Viertelstunden.',
                              '3 Stunden sind 12 Viertelstunden, dazu 1 Viertelstunde: 13.')),
        (U, 3, lambda R: zahl('Ein Rezept braucht 1 3/4 Becher Mehl. Ein Becher fasst 200 g. Wie viele Gramm Mehl sind das?', 350, '(1 + 3/4) * 200',
                              'Ein ganzer Becher sind 200 g. Wie viel sind 3/4 Becher?', '1 Becher = 200 g. 3/4 Becher = 150 g. Zusammen 350 g.', einheit='g')),
        (U, 3, g('Gib die gemischte Zahl mit dem Nenner 8 an, die zwischen 13/4 und 7/2 liegt.', '27/8',
                 'Schreibe beide Brüche mit dem Nenner 8.', '13/4 = 26/8 und 7/2 = 28/8. Dazwischen liegt 27/8 = 3 3/8.')),
        (U, 3, g('Welche Zahl liegt genau in der Mitte zwischen 1 1/2 und 4? Gib sie als gemischte Zahl an.', '(3/2 + 4) / 2',
                 'Der Abstand ist 4 − 1 1/2. Die Mitte ist die Hälfte davon weiter.', 'Abstand 2 1/2, die Hälfte ist 1 1/4. 1 1/2 + 1 1/4 = 2 3/4.')),
        (U, 3, g('Bilde mit den Ziffern 2, 3 und 5 (je einmal) eine gemischte Zahl mit echtem Bruch, z. B. 2 3/5. Welche ist die größte?', '5 + 2/3',
                 'Die größte Ziffer gehört zu den Ganzen. Welcher echte Bruch aus den beiden anderen Ziffern ist möglich?',
                 'Ganze 5. Echter Bruch aus 2 und 3: nur 2/3 (3/2 ist unecht). Also 5 2/3.')),
        (U, 3, b('Ein Kind schreibt 3 2/5 = 6/5, weil 3 · 2 = 6. Wie heißt der unechte Bruch richtig?', '3 + 2/5',
                 '3 2/5 heißt 3 + 2/5. Wie viele Fünftel sind 3 Ganze?', '3 Ganze = 15 Fünftel. 15 + 2 = 17. Richtig ist 17/5, nicht 6/5.')),
        (U, 3, g('Ein Kind schreibt 17/4 = 3 5/4. Wie heißt die gemischte Zahl richtig?', '17/4',
                 'Der Restbruch einer gemischten Zahl muss kleiner als 1 sein.', '5/4 ist noch mehr als 1. 17 : 4 = 4 Rest 1, also 4 1/4.')),
        (U, 3, lambda R: zahl('Ein Band ist 5 1/4 m lang. Wie viele Stücke von je 1/4 m kann man abschneiden?', 21, '(5 + 1/4) * 4',
                              'Wie viele Viertel sind 5 1/4?', '5 1/4 = 21/4. Also 21 Stücke zu je 1/4 m.')),
        (U, 3, lambda R: wahl(R, 'Welche Aussage über 2 1/2 stimmt?', '2 1/2 = 5/2', ['2 1/2 = 2 · 1/2', '2 1/2 = 3/2', '2 1/2 = 21/2'],
                              'Schreibe 2 1/2 als 2 + 1/2.', '2 + 1/2 = 4/2 + 1/2 = 5/2. 2 · 1/2 wäre nur 1, und 21/2 wäre 10 1/2.')),
        ('test', 2, b('Schreibe 2 2/3 als unechten Bruch.', '2 + 2/3', '', '2 · 3 = 6 Drittel, dazu 2: 8/3.')),
        ('korrektur', 2, b('Schreibe 1 5/8 als unechten Bruch.', '1 + 5/8', '', '8 Achtel + 5 Achtel = 13/8.')),
        ('korrektur', 2, g('Schreibe 11/5 als gemischte Zahl.', '11/5', '', '11 : 5 = 2 Rest 1. Also 2 1/5.')),
        ('korrektur', 2, b('Schreibe 3 3/7 als unechten Bruch.', '3 + 3/7', '', '3 · 7 = 21 Siebtel, dazu 3: 24/7.')),
        ('sicherung', 2, b('Schreibe 5 1/3 als unechten Bruch.', '5 + 1/3', '', '5 · 3 = 15 Drittel, dazu 1: 16/3.')),
        ('sicherung', 2, g('Schreibe 19/6 als gemischte Zahl.', '19/6', '', '19 : 6 = 3 Rest 1. Also 3 1/6.')),
        ('sicherung', 2, b('Schreibe 2 4/9 als unechten Bruch.', '2 + 4/9', '', '2 · 9 = 18 Neuntel, dazu 4: 22/9.')),
        ('sicherung', 2, g('Schreibe 15/7 als gemischte Zahl.', '15/7', '', '15 : 7 = 2 Rest 1. Also 2 1/7.')),
        ('sicherung', 2, b('Schreibe 6 1/2 als unechten Bruch.', '6 + 1/2', '', '6 · 2 = 12 Halbe, dazu 1: 13/2.')),
        ('sicherung', 2, g('Schreibe 25/8 als gemischte Zahl.', '25/8', '', '25 : 8 = 3 Rest 1. Also 3 1/8.')),
    ]


_GEM = {
    'lernziel': 'gemischte_zahlen', 'titel': 'Gemischte Zahlen umwandeln',
    'einstieg': 'Nach dem Fest bleiben 2 ganze Pizzen und 3/4 Pizza übrig. Man schreibt kurz 2 3/4 Pizzen. So eine Zahl heißt ⟦gemischte Zahl⟧.',
    'woerter': [['gemischte Zahl', 'Ganze und ein Bruch zusammen: 2 3/4 heißt 2 + 3/4'],
                ['unechter Bruch', 'ein Bruch mit Zähler größer als der Nenner, z. B. 11/4']],
    'bild': {'typ': 'bruchstreifen', 'teile': 4, 'gefaerbt': 4, 'ganzes': '1 Pizza', 'teil_text': '1. Pizza',
             'zeilen': [{'teile': 4, 'gefaerbt': 4, 'teil_text': '2. Pizza'}, {'teile': 4, 'gefaerbt': 3, 'teil_text': '3/4'}]},
    'schritte': [
        {'text': 'Jede ganze Pizza hat 4 Viertel. 2 Pizzen sind 8 Viertel.'},
        {'text': 'Dazu kommen noch 3 Viertel: 8 + 3 = 11 Viertel.',
         'bild': {'zeilen': [{'teile': 4, 'gefaerbt': 4, 'teil_text': '8/4'}, {'teile': 4, 'gefaerbt': 3, 'teil_text': '+ 3/4'}]}},
        {'text': 'Also ist 2 3/4 = ⟦11/4⟧. Das ist ein unechter Bruch.'},
        {'text': 'Rückwärts: 11 : 4 = 2 Rest 3. Also 11/4 = ⟦2 3/4⟧.'},
    ],
    'fehler': '2 3/4 heißt nicht 2 · 3/4. Zwei Pizzen und drei Viertel sind 2 + 3/4, also mehr als 2 Pizzen.',
    'fehler_bild': {'teile': 4, 'gefaerbt': 4, 'teil_text': '2 · 3/4 = 6/4', 'zeilen': [{'teile': 4, 'gefaerbt': 2, 'teil_text': 'nur 1 1/2 Pizzen'}]},
    'regel': 'Gemischte Zahl in Bruch: ⟦Ganze mal Nenner plus Zähler⟧. Rückwärts teilst du mit Rest.',
    'probe': '11/4 = 8/4 + 3/4 = 2 + 3/4 = 2 3/4.',
}


def _zb_aufgaben():
    U = 'uebung'
    def m(t, a, e, n, i, h, w, z): return lambda R: mark(t, a, e, n, i, h, w, z)
    def b(t, E, h, w): return lambda R: lbruch(t, E, h, w)
    LINKS = 'Weiter links am Zahlenstrahl heißt kleiner.'
    return [
        (U, 1, m('Markiere −1/2 am Zahlenstrahl (von −1 bis 1, 8 gleiche Teile).', -1, 1, 8, 2, 'Ein Teil ist 1/4 lang. −1/2 liegt links von 0.',
                 'Von −1 aus: −3/4, −1/2 – das ist der 2. Strich.', Fr(-1, 2))),
        (U, 1, m('Markiere −3/4 am Zahlenstrahl (von −1 bis 1, 8 gleiche Teile).', -1, 1, 8, 1, 'Ein Teil ist 1/4 lang. Zähle von 0 nach links.',
                 '−3/4 ist drei Viertel links von 0, also der 1. Strich nach −1.', Fr(-3, 4))),
        (U, 1, lambda R: wahl(R, 'Welche Zahl ist kleiner: −1/3 oder 1/4?', '−1/3', ['1/4', 'Beide sind gleich groß.'], LINKS,
                              'Jede negative Zahl ist kleiner als jede positive Zahl. Also ist −1/3 kleiner.', n=3)),
        (U, 1, b('Schreibe 5 : 8 als Bruch.', '5 / 8', 'Der Bruchstrich bedeutet „geteilt durch“.', 'Der Bruchstrich heißt „geteilt durch“: 5 : 8 = 5/8.')),
        (U, 2, lambda R: wahl(R, 'Ordne −2/3, −3/4 und −1/2 der Größe nach. Welche Zahl ist am kleinsten?', '−3/4', ['−2/3', '−1/2'],
                              'Vergleiche zuerst 3/4, 2/3 und 1/2. Bei negativen Zahlen dreht sich die Reihenfolge um.',
                              '3/4 > 2/3 > 1/2. Also liegt −3/4 am weitesten links: −3/4 < −2/3 < −1/2.', n=3)),
        (U, 2, lambda R: wahl(R, 'Welche Zahl ist größer: −5/6 oder −7/8?', '−5/6', ['−7/8', 'Beide sind gleich groß.'],
                              'Hauptnenner 24. Die Zahl mit dem kleineren Betrag liegt näher bei 0.',
                              '5/6 = 20/24 und 7/8 = 21/24. −20/24 liegt näher bei 0, also ist −5/6 größer.', n=3)),
        (U, 2, m('Markiere −1 1/4 am Zahlenstrahl (von −2 bis 0, 8 gleiche Teile).', -2, 0, 8, 3, 'Ein Teil ist 1/4 lang. −1 1/4 liegt zwischen −2 und −1.',
                 '−1 1/4 = −5/4. Von −2 aus: −7/4, −6/4, −5/4 – der 3. Strich.', Fr(-5, 4))),
        (U, 2, lambda R: gemischt('Schreibe 7 : 3 zuerst als Bruch und dann als gemischte Zahl.', '7 / 3', 'Der Bruchstrich heißt „geteilt durch“. Dann teilen mit Rest.',
                                  '7 : 3 = 7/3. 7 : 3 = 2 Rest 1, also 2 1/3.')),
        (U, 2, lambda R: wahl(R, 'Welche dieser Zahlen ist eine ganze Zahl?', '−8/4', ['3/4', '−1/2', '5/3'],
                              'Kürze oder teile: Geht die Division ohne Rest auf?', '−8/4 = −8 : 4 = −2. Das ist eine ganze Zahl. Die anderen gehen nicht auf.')),
        (U, 2, lambda R: wahl(R, 'Stimmt die Aussage? „Jede natürliche Zahl kann man als Bruch schreiben.“', 'Ja, zum Beispiel 5 = 5/1 = 10/2.',
                              ['Nein, natürliche Zahlen sind keine Brüche.', 'Nur gerade Zahlen.'],
                              'Denke an den Nenner 1.', 'Jede natürliche Zahl n ist n/1. Deshalb gehören alle natürlichen Zahlen zu den rationalen Zahlen.', n=3)),
        (U, 3, b('Welche Zahl liegt genau in der Mitte zwischen −3/4 und 1/4?', '(-3/4 + 1/4) / 2', 'Der Abstand ist 1. Geh von −3/4 die Hälfte davon nach rechts.',
                 'Abstand: 1/4 − (−3/4) = 1. Die Hälfte ist 1/2. −3/4 + 1/2 = −1/4.')),
        (U, 3, lambda R: wahl(R, 'Welcher Term hat den gleichen Wert wie „ein Viertel von 3“?', '3 : 4', ['4 : 3', '3 · 4', '1/4 : 3'],
                              'Ein Viertel von 3 sind 3 · 1/4. Das ist 3/4.', '3 · 1/4 = 3/4 = 3 : 4. Dagegen: 4 : 3 = 4/3, 3 · 4 = 12, 1/4 : 3 = 1/12.')),
        (U, 3, lambda R: wahl(R, 'Ordne −1/2, 1/3, −2/3 und 1/4 der Größe nach, mit der kleinsten Zahl zuerst. Welche Zahl steht an zweiter Stelle?', '−1/2',
                              ['−2/3', '1/4', '1/3'], 'Zuerst die negativen Zahlen. Die mit dem größeren Betrag ist kleiner.',
                              '−2/3 < −1/2 < 1/4 < 1/3. An zweiter Stelle steht −1/2.')),
        (U, 3, lambda R: wahl(R, 'Welche Zahl kommt direkt nach 1/2?', 'Keine: Zwischen zwei Brüchen liegt immer noch ein Bruch.', ['2/2', '1/3', '3/4'],
                              'Suche einen Bruch zwischen 1/2 und deinem Kandidaten.',
                              'Zwischen 1/2 und 3/4 liegt z. B. 5/8, dazwischen wieder 9/16 … Brüche haben keinen Nachfolger.')),
        (U, 3, lambda R: zahl('Wie viele Brüche mit dem Nenner 6 liegen zwischen −1 und 0? (Die Grenzen zählen nicht.)', 5, '6 - 1',
                              'Schreibe −1 als −6/6.', 'Es sind −5/6, −4/6, −3/6, −2/6 und −1/6, also 5 Brüche.')),
        (U, 3, lambda R: wahl(R, 'Ein Kind sagt: „−2/5 ist kleiner als −3/5, weil 2 kleiner ist als 3.“ Was stimmt?', 'Falsch: −3/5 liegt weiter links, also −3/5 < −2/5.',
                              ['Richtig.', 'Falsch: Beide Zahlen sind gleich groß.', 'Falsch: Negative Brüche kann man nicht vergleichen.'], LINKS,
                              'Bei negativen Zahlen ist die mit dem größeren Betrag kleiner: 3/5 > 2/5, also −3/5 < −2/5.')),
        (U, 3, m('Ein Thermometer zeigt −3/4 °C. Es wird noch 1/4 °C kälter. Markiere die neue Temperatur (Zahlenstrahl von −2 bis 0, 8 gleiche Teile).',
                 -2, 0, 8, 4, 'Kälter heißt: nach links. Ein Teil ist 1/4.', '−3/4 − 1/4 = −1. −1 liegt beim 4. Strich nach −2.', -1)),
        (U, 3, lambda R: wahl(R, 'Welche Zahl ist am kleinsten: −7/2, −3 oder −13/4?', '−7/2', ['−3', '−13/4'],
                              'Schreibe alle Zahlen mit dem Nenner 4.', '−7/2 = −14/4, −3 = −12/4, −13/4. Am weitesten links: −14/4 = −7/2.', n=3)),
        ('test', 2, m('Markiere −1/4 am Zahlenstrahl (von −1 bis 1, 8 gleiche Teile).', -1, 1, 8, 3, '', 'Von −1 aus: −3/4, −1/2, −1/4 – der 3. Strich.', Fr(-1, 4))),
        ('korrektur', 2, lambda R: wahl(R, 'Welche Zahl ist größer: −2/3 oder −1/3?', '−1/3', ['−2/3', 'Beide sind gleich groß.'], '',
                                        '−1/3 liegt näher bei 0, also weiter rechts. −1/3 ist größer.', n=3)),
        ('korrektur', 2, b('Schreibe 7 : 9 als Bruch.', '7 / 9', '', 'Der Bruchstrich heißt „geteilt durch“: 7 : 9 = 7/9.')),
        ('korrektur', 2, m('Markiere −3/2 am Zahlenstrahl (von −2 bis 0, 4 gleiche Teile).', -2, 0, 4, 1, '', 'Ein Teil ist 1/2. −3/2 = −1 1/2 ist der 1. Strich nach −2.', Fr(-3, 2))),
        ('sicherung', 2, m('Markiere −1/2 am Zahlenstrahl (von −2 bis 2, 8 gleiche Teile).', -2, 2, 8, 3, '', 'Ein Teil ist 1/2. Von −2 aus: −3/2, −1, −1/2 – der 3. Strich.', Fr(-1, 2))),
        ('sicherung', 2, lambda R: wahl(R, 'Welche Zahl ist kleiner: −1/4 oder −1/5?', '−1/4', ['−1/5', 'Beide sind gleich groß.'], '',
                                        '1/4 > 1/5, also liegt −1/4 weiter links und ist kleiner.', n=3)),
        ('sicherung', 2, b('Schreibe 11 : 4 als Bruch.', '11 / 4', '', 'Der Bruchstrich heißt „geteilt durch“: 11 : 4 = 11/4.')),
        ('sicherung', 2, m('Markiere −1 1/2 am Zahlenstrahl (von −2 bis 1, 6 gleiche Teile).', -2, 1, 6, 1, '', 'Ein Teil ist 1/2. −1 1/2 ist der 1. Strich nach −2.', Fr(-3, 2))),
        ('sicherung', 2, lambda R: wahl(R, 'Welche Zahl ist größer: −3/8 oder −1/2?', '−3/8', ['−1/2', 'Beide sind gleich groß.'], '',
                                        '1/2 = 4/8 > 3/8. −3/8 liegt näher bei 0 und ist größer.', n=3)),
        ('sicherung', 2, b('Schreibe 2 : 7 als Bruch.', '2 / 7', '', 'Der Bruchstrich heißt „geteilt durch“: 2 : 7 = 2/7.')),
    ]


_ZB = {
    'lernziel': 'zahlbereiche', 'titel': 'Brüche als Zahlen, auch negativ',
    'einstieg': 'Das Thermometer zeigt −1/2 °C, eine halbe Stufe unter null. Brüche gibt es also auch links von 0. Alle Brüche zusammen heißen ⟦rationale Zahlen⟧.',
    'woerter': [['rationale Zahlen', 'alle positiven und negativen Brüche, auch die ganzen Zahlen; Zeichen ℚ'],
                ['Quotient', 'Ergebnis einer Division: 3/4 = 3 : 4']],
    'bild': {'typ': 'zahlenstrahl', 'start': -2, 'ende': 2, 'abschnitte': 8, 'beschriftet': 'anfang_ende'},
    'schritte': [
        {'text': '−3/4 liegt links von 0, genauso weit wie 3/4 rechts.',
         'bild': {'punkte': [{'wert': -0.75, 'name': '−3/4'}, {'wert': 0.75, 'name': '3/4'}]}},
        {'text': 'Jetzt kommt −1/2 dazu. Weiter links heißt kleiner.',
         'bild': {'punkte': [{'wert': -0.75, 'name': '−3/4'}, {'wert': -0.5, 'name': '−1/2'}, {'wert': 0.75, 'name': '3/4'}]}},
        {'text': 'Also gilt ⟦−3/4 < −1/2⟧, obwohl 3/4 größer ist als 1/2.'},
        {'text': 'Jeder Bruch ist ein Quotient: 3/4 = 3 : 4 (3 Pizzen, 4 Kinder).'},
    ],
    'fehler': '−3/4 ist nicht größer als −1/2. Am Thermometer ist −3/4 °C kälter als −1/2 °C.',
    'fehler_bild': {'punkte': [{'wert': -0.75, 'name': '−3/4: kälter'}, {'wert': -0.5, 'name': '−1/2'}]},
    'regel': 'Am Zahlenstrahl ist die Zahl ⟦weiter links⟧ kleiner. Jeder Bruch ist ein Quotient: a/b = a : b.',
    'probe': '−3/4 = −0,75 und −1/2 = −0,5: −0,75 liegt weiter links.',
}


def _vgl_aufgaben():
    return [
        (None, 2, lambda R: zahl('Bestimme den Hauptnenner von 5/12 und 7/18 mit der Primfaktorzerlegung.', 36, '2 * 2 * 3 * 3',
                                 '12 = 2 · 2 · 3 und 18 = 2 · 3 · 3. Jeder Faktor so oft, wie er höchstens vorkommt.', '2 · 2 · 3 · 3 = 36.')),
        (None, 2, lambda R: zahl('Bestimme den Hauptnenner von 3/8 und 5/12 mit der Primfaktorzerlegung.', 24, '2 * 2 * 2 * 3',
                                 '8 = 2 · 2 · 2 und 12 = 2 · 2 · 3.', 'Drei Zweien (von der 8) und eine Drei (von der 12): 2 · 2 · 2 · 3 = 24.')),
        (None, 2, lambda R: zahl('Bestimme den Hauptnenner von 7/15 und 9/20 mit der Primfaktorzerlegung.', 60, '2 * 2 * 3 * 5',
                                 '15 = 3 · 5 und 20 = 2 · 2 · 5.', 'Zwei Zweien, eine Drei, eine Fünf: 2 · 2 · 3 · 5 = 60.')),
        (None, 3, lambda R: wahl(R, 'Welcher Bruch ist größer: 7/12 oder 11/18?', '11/18', ['7/12', 'Beide sind gleich groß.'],
                                 'Hauptnenner über die Primfaktoren: 12 = 2 · 2 · 3, 18 = 2 · 3 · 3.',
                                 'Hauptnenner 36. 7/12 = 21/36 und 11/18 = 22/36. Also ist 11/18 größer.', n=3)),
        (None, 3, lambda R: zahl('Bestimme den Hauptnenner von 1/6, 3/8 und 4/9.', 72, '2 * 2 * 2 * 3 * 3',
                                 'Zerlege 6, 8 und 9 in Primfaktoren.', '6 = 2 · 3, 8 = 2 · 2 · 2, 9 = 3 · 3. Drei Zweien und zwei Dreien: 72.')),
        (None, 3, lambda R: lbruch('Gib den Bruch mit dem Nenner 24 an, der genau in der Mitte zwischen 5/12 und 1/2 liegt.', '(5/12 + 1/2) / 2',
                                   'Schreibe beide Brüche mit dem Nenner 24.', '5/12 = 10/24 und 1/2 = 12/24. In der Mitte liegt 11/24.')),
    ]


karte_neu(DATEI, _GEM, _gem_aufgaben(), seed=6181, nach='kuerzen', teil_text='Gemischte Zahlen und unechte Brüche umwandeln')
karte_erweitern(DATEI, 'vergleichen', _vgl_aufgaben(), seed=6182,
                schritte_einfuegen=[(1, {'text': 'Oder mit der Primfaktorzerlegung: 4 = 2 · 2 und 6 = 2 · 3.'}),
                                    (2, {'text': 'Jeder Faktor so oft wie nötig: 2 · 2 · 3 = ⟦12⟧.'})],
                woerter_dazu=[['Primfaktorzerlegung', 'eine Zahl als Produkt von Primzahlen schreiben: 12 = 2 · 2 · 3']])
karte_neu(DATEI, _ZB, _zb_aufgaben(), seed=6183, vor='verstehen', teil_text='Brüche als Zahlen: negative Brüche ordnen, Bruch als Quotient')


if __name__ == '__main__':
    schreibe(DATEI)
