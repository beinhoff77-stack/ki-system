#!/usr/bin/env python3
"""Thema finanzen.zinseszins – Zinseszins (ohne Lehrplan-Zuordnung, Niveau Klasse 9/10)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403

start(7210)

SAETZE = [Fr(1), Fr(2), Fr(3), Fr(4), Fr(5), Fr(3, 2), Fr(5, 2), Fr(6), Fr(8), Fr(10)]


def pt(p):
    return dz(p) + ' %'


def cent(x):
    """Auf Cent runden (kaufmännisch); gibt Fraction zurück. None, wenn zu nah an der Rundungsgrenze."""
    v = gerundet(float(x), 2)
    return None if v is None else Fr(str(v))


def qtxt(p):
    return dz(1 + Fr(p) / 100)


ETAPPEN = [
    {'lernziel': 'jahr', 'titel': 'Zinsen Jahr für Jahr',
     'regel': 'Beim ⟦Zinseszins⟧ (compound interest) werden die Zinsen am Jahresende ⟦zum Kapital addiert⟧ und im nächsten Jahr ⟦mitverzinst⟧. Zinsen eines Jahres = Kapital · p %.',
     'schritte': ['Anfangskapital 1 000 €, Zinssatz 5 % pro Jahr.', 'Jahr 1: 5 % von 1 000 € = 50 € → 1 050 €.', 'Jahr 2: 5 % von 1 050 € = 52,50 € → ⟦1 102,50 €⟧.'],
     'probe': 'Im zweiten Jahr gibt es mehr Zinsen (52,50 € > 50 €), weil die 50 € mitverzinst werden ✓',
     'bild': {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': 'Start', 'wert': 1000}, {'name': 'Jahr 1', 'wert': 1050}, {'name': 'Jahr 2', 'wert': 1102.5}], 'y_start': 900, 'zahlen': True},
     'fehler': 'Im 2. Jahr wieder 50 € Zinsen zu rechnen (Ergebnis 1 100 €) ist falsch: Das wären ⟦einfache Zinsen⟧. Beim Zinseszins wird das ⟦neue Kapital⟧ 1 050 € verzinst.'},
    {'lernziel': 'faktor', 'titel': 'Der Wachstumsfaktor q',
     'regel': 'Statt Zinsen auszurechnen und zu addieren, multipliziert man mit dem ⟦Wachstumsfaktor⟧ (growth factor) ⟦q = 1 + p/100⟧: bei 4 % ist q = 1,04. Bei einer ⟦Abnahme⟧ um p % ist q = 1 − p/100, z. B. 0,85 bei −15 %.',
     'schritte': ['Zinssatz 3 %: q = 1 + 3/100 = 1,03.', '2 000 € · 1,03 = ⟦2 060 €⟧ nach einem Jahr.'],
     'probe': '3 % von 2 000 € = 60 €; 2 000 + 60 = 2 060 ✓',
     'fehler': 'Bei 3 % mit q = 1,3 zu rechnen ist falsch: 1,3 bedeutet ⟦+30 %⟧. 3 % sind 0,03, also q = ⟦1,03⟧.'},
    {'lernziel': 'formel', 'titel': 'Kapital nach n Jahren',
     'regel': 'Nach n Jahren mit gleichem Zinssatz gilt: ⟦Kₙ = K₀ · qⁿ⟧ (K₀ Anfangskapital, q Wachstumsfaktor). Geldbeträge rundet man am Ende auf ⟦Cent⟧ (zwei Nachkommastellen).',
     'schritte': ['K₀ = 5 000 €, p = 2 %, n = 6 Jahre.', 'K₆ = 5 000 € · 1,02⁶ ≈ 5 000 € · 1,126162.', 'K₆ ≈ ⟦5 630,81 €⟧.'],
     'probe': 'Mehr als 5 000 € + 6 · 100 € = 5 600 € (einfache Zinsen) ✓',
     'fehler': 'K₆ = 5 000 · 1,02 · 6 = 30 600 € ist falsch: Der Faktor wird ⟦sechsmal multipliziert⟧ (Potenz 1,02⁶), nicht mit 6 malgenommen.'},
    {'lernziel': 'rueck', 'titel': 'Rückwärts rechnen',
     'regel': 'Gesucht ist das ⟦Anfangskapital⟧: ⟦K₀ = Kₙ : qⁿ⟧. Gesucht ist der ⟦Zinssatz⟧: q = Kₙ : K₀ für ein Jahr, bei zwei Jahren ⟦q = √(K₂ : K₀)⟧, dann p = (q − 1) · 100.',
     'schritte': ['Nach 2 Jahren bei 5 % sind 2 205 € auf dem Konto.', 'K₀ = 2 205 € : 1,05² = 2 205 € : 1,1025 = ⟦2 000 €⟧.'],
     'probe': '2 000 · 1,05 · 1,05 = 2 205 ✓',
     'fehler': 'K₀ = 2 205 € − 2 · 5 % · 2 205 € ist falsch: Prozente beziehen sich auf den ⟦Grundwert am Anfang⟧. Rückwärts wird ⟦durch qⁿ geteilt⟧.'},
    {'lernziel': 'vergleich', 'titel': 'Angebote vergleichen',
     'regel': 'Zinseszins wächst ⟦schneller⟧ als einfache Zinsen, weil auch die Zinsen Zinsen bringen – je länger, desto deutlicher. Zum Vergleich von Angeboten rechnet man den ⟦Endbetrag⟧ aus. Wie lange es bis zur ⟦Verdopplung⟧ dauert, findet man durch Probieren mit qⁿ ≥ 2.',
     'schritte': ['Bei 7 %: 1,07¹⁰ ≈ 1,967 < 2, 1,07¹¹ ≈ 2,105 ≥ 2.', 'Das Kapital hat sich nach ⟦11 Jahren⟧ erstmals verdoppelt.'],
     'probe': 'Faustregel: 72 : 7 ≈ 10,3 – passt ungefähr ✓',
     'fehler': '„Bei 5 % verdoppelt sich das Geld nach 20 Jahren, weil 20 · 5 % = 100 %“ ist falsch: Das gilt nur für einfache Zinsen. Mit Zinseszins reicht 1,05¹⁵ ≈ 2,08 – also ⟦15 Jahre⟧.'},
]


def g_jahr(s):
    K0 = R.choice([500, 800, 1000, 1200, 1500, 2000, 2500, 4000, 5000]) if s < 3 else R.choice([600, 750, 1250, 2400, 3200])
    p = R.choice([Fr(2), Fr(3), Fr(4), Fr(5), Fr(6)]) if s == 1 else R.choice(SAETZE)
    q = 1 + p / 100
    art = R.choice({1: ['z1', 'k1'], 2: ['k2', 'z2', 'k1'], 3: ['k3', 'z2', 'einfach_diff']}[s])
    if art == 'z1':
        z = K0 * p / 100
        return zahl(f'{dz(K0)} € werden mit {pt(p)} pro Jahr verzinst. Wie viel Zinsen gibt es im ersten Jahr?', f'{pt(p)} von {dz(K0)} € = {dz(K0)} · {dz(p / 100)} = {eu(z)}.',
                    'Zinsen = Kapital · p : 100.', z, f'{K0} * {float(p)} / 100', einheit='€')
    if art == 'k1':
        return zahl(f'{dz(K0)} € werden ein Jahr lang mit {pt(p)} verzinst. Wie hoch ist das Kapital nach einem Jahr?', f'Zinsen: {eu(K0 * p / 100)}. Kapital: {eu(K0 * q)}.',
                    'Kapital plus Zinsen des Jahres.', K0 * q, f'{K0} * (1 + {float(p)} / 100)', einheit='€')
    if art in ('k2', 'k3'):
        n = 2 if art == 'k2' else 3
        ks = [K0 * q ** i for i in range(n + 1)]
        if not all((k * 100).denominator == 1 for k in ks): return None
        return zahl(f'{dz(K0)} € werden mit {pt(p)} Zinseszins angelegt. Wie hoch ist das Kapital nach {n} Jahren? Rechne Jahr für Jahr.',
                    ' '.join(f'Jahr {i}: {eu(ks[i - 1])} + {eu(ks[i - 1] * p / 100)} = {eu(ks[i])}.' for i in range(1, n + 1)),
                    'Verzinse jedes Jahr das neue Kapital.', ks[-1], f'{K0} * (1 + {float(p)} / 100) ** {n}', einheit='€')
    if art == 'z2':
        z2 = K0 * q * p / 100
        if (z2 * 100).denominator != 1: return None
        return zahl(f'{dz(K0)} € werden mit {pt(p)} Zinseszins angelegt. Wie viel Zinsen gibt es im zweiten Jahr?', f'Nach Jahr 1: {eu(K0 * q)}. Zinsen im Jahr 2: {pt(p)} davon = {eu(z2)}.',
                    'Im zweiten Jahr wird das Kapital nach dem ersten Jahr verzinst.', z2, f'{K0} * (1 + {float(p)} / 100) * {float(p)} / 100', einheit='€')
    n = R.choice([2, 3])
    zz = K0 * q ** n - K0
    ez = K0 * p / 100 * n
    d = zz - ez
    if (d * 100).denominator != 1: return None
    return zahl(f'{dz(K0)} € liegen {n} Jahre bei {pt(p)}. Wie viel mehr bringt Zinseszins als einfache Zinsen (jedes Jahr nur Zinsen vom Anfangskapital)?',
                f'Zinseszins: {eu(K0 * q ** n)} − {dz(K0)} € = {eu(zz)}. Einfach: {n} · {eu(K0 * p / 100)} = {eu(ez)}. Unterschied: {eu(d)}.',
                'Berechne beide Zinsbeträge und vergleiche.', d, f'{K0} * (1 + {float(p)} / 100) ** {n} - {K0} - {K0} * {float(p)} / 100 * {n}', einheit='€')


def g_faktor(s):
    art = R.choice({1: ['q', 'q'], 2: ['q', 'p', 'abnahme_q'], 3: ['abnahme_p', 'p', 'gesamt']}[s])
    p = R.choice(SAETZE + [Fr(12), Fr(15), Fr(1, 2), Fr(7, 2)])
    if art == 'q':
        return zahl(f'Wie groß ist der Wachstumsfaktor q bei einem Zinssatz von {pt(p)}?', f'q = 1 + {dz(p)}/100 = 1 + {dz(p / 100)} = {qtxt(p)}.',
                    'q = 1 + p/100.', 1 + p / 100, f'1 + {float(p)} / 100')
    if art == 'p':
        return zahl(f'Ein Kapital wird jedes Jahr mit dem Faktor q = {qtxt(p)} multipliziert. Wie hoch ist der Zinssatz in %?', f'q − 1 = {dz(p / 100)} = {pt(p)}.',
                    'Ziehe 1 ab und rechne in Prozent um.', p, f'({float(1 + p / 100)} - 1) * 100', einheit='%')
    if art == 'abnahme_q':
        a = R.choice([5, 10, 15, 20, 25, 30, 12, 8])
        return zahl(f'Ein Auto verliert jedes Jahr {a} % seines Werts. Mit welchem Faktor wird der Wert jedes Jahr multipliziert?', f'Es bleiben {100 - a} %: q = 1 − {dz(Fr(a, 100))} = {dz(Fr(100 - a, 100))}.',
                    'Abnahme: q = 1 − p/100.', Fr(100 - a, 100), f'1 - {a} / 100')
    if art == 'abnahme_p':
        a = R.choice([5, 10, 15, 20, 25, 30, 12, 8])
        return zahl(f'Der Wert einer Maschine wird jährlich mit q = {dz(Fr(100 - a, 100))} multipliziert. Um wie viel Prozent sinkt der Wert pro Jahr?',
                    f'1 − {dz(Fr(100 - a, 100))} = {dz(Fr(a, 100))} = {a} %.', 'q < 1 bedeutet Abnahme. Was fehlt zu 1?', a, f'(1 - {(100 - a) / 100}) * 100', einheit='%')
    p1, p2 = R.sample([Fr(2), Fr(3), Fr(4), Fr(5), Fr(10)], 2)
    ges = (1 + p1 / 100) * (1 + p2 / 100)
    return zahl(f'Ein Guthaben wird im ersten Jahr mit {pt(p1)}, im zweiten mit {pt(p2)} verzinst. Mit welchem Faktor wurde es insgesamt multipliziert?',
                f'{qtxt(p1)} · {qtxt(p2)} = {dz(ges)}.', 'Die beiden Faktoren werden multipliziert, nicht die Prozente addiert.', ges, f'(1 + {float(p1)} / 100) * (1 + {float(p2)} / 100)')


def g_formel(s):
    K0 = R.choice([1000, 2000, 2500, 3000, 5000, 8000, 10000, 1500, 4000])
    p = R.choice(SAETZE)
    n = R.randint(3, 6) if s == 1 else R.randint(4, 15)
    q = 1 + p / 100
    Kn = K0 * q ** n
    art = R.choice({1: ['kn'], 2: ['kn', 'kn', 'zinsen'], 3: ['kn_abnahme', 'zinsen', 'kn']}[s])
    if art == 'kn_abnahme':
        a = R.choice([10, 15, 20, 25])
        W0 = R.choice([12000, 18000, 24000, 30000])
        n = R.randint(2, 6)
        W = W0 * Fr(100 - a, 100) ** n
        v = cent(W)
        if v is None: return None
        return zahl(f'Ein Auto kostet neu {dz(W0)} € und verliert jedes Jahr {a} % seines Werts. Wie viel ist es nach {n} Jahren noch wert? (auf Cent)',
                    f'W = {dz(W0)} € · {dz(Fr(100 - a, 100))}^{n} ≈ {eu(v)}.', 'Abnahme: Faktor q = 1 − p/100.', v, f'round({W0} * {(100 - a) / 100} ** {n}, 2)', einheit='€', tol=0.01)
    v = cent(Kn)
    if v is None: return None
    if art == 'kn':
        return zahl(f'{dz(K0)} € werden {n} Jahre mit {pt(p)} Zinseszins angelegt. Wie hoch ist das Endkapital? (auf Cent)',
                    f'Kₙ = {dz(K0)} € · {qtxt(p)}^{n} ≈ {eu(v)}.', 'Kₙ = K₀ · qⁿ – den Faktor potenzieren.', v,
                    f'round({K0} * (1 + {float(p)} / 100) ** {n}, 2)', einheit='€', tol=0.01)
    z = cent(Kn - K0)
    if z is None: return None
    return zahl(f'{dz(K0)} € werden {n} Jahre mit {pt(p)} Zinseszins angelegt. Wie viel Zinsen bringt das insgesamt? (auf Cent)',
                f'Endkapital ≈ {eu(v)}. Zinsen: {eu(v)} − {dz(K0)} € = {eu(z)}.', 'Endkapital minus Anfangskapital.', z,
                f'round({K0} * (1 + {float(p)} / 100) ** {n} - {K0}, 2)', einheit='€', tol=0.01)


def g_rueck(s):
    art = R.choice({1: ['k0_1'], 2: ['k0_n', 'p_1', 'k0_1'], 3: ['p_2', 'k0_n', 'p_2']}[s])
    K0 = R.choice([1000, 2000, 2500, 4000, 5000, 8000, 10000, 1600, 3200])
    p = R.choice([Fr(2), Fr(3), Fr(4), Fr(5), Fr(10), Fr(5, 2)])
    q = 1 + p / 100
    if art == 'k0_1':
        K1 = K0 * q
        return zahl(f'Nach einem Jahr mit {pt(p)} Zinsen sind {eu(K1)} auf dem Konto. Wie viel wurde eingezahlt?', f'K₀ = {eu(K1)} : {qtxt(p)} = {dz(K0)} €.',
                    'Rückwärts: durch q teilen.', K0, f'{float(K1)} / (1 + {float(p)} / 100)', einheit='€')
    if art == 'k0_n':
        n = R.choice([2, 3])
        Kn = K0 * q ** n
        if (Kn * 100).denominator != 1: return None
        return zahl(f'Nach {n} Jahren mit {pt(p)} Zinseszins sind {eu(Kn)} auf dem Konto. Wie hoch war das Anfangskapital?', f'K₀ = {eu(Kn)} : {qtxt(p)}^{n} = {eu(Kn)} : {dz(q ** n)} = {dz(K0)} €.',
                    'Durch qⁿ teilen.', K0, f'{float(Kn)} / (1 + {float(p)} / 100) ** {n}', einheit='€')
    if art == 'p_1':
        K1 = K0 * q
        return zahl(f'Aus {dz(K0)} € werden in einem Jahr {eu(K1)}. Wie hoch ist der Zinssatz in %?', f'q = {eu(K1)} : {dz(K0)} € = {qtxt(p)}, also {pt(p)}.',
                    'Neues Kapital durch altes Kapital ergibt q.', p, f'({float(K1)} / {K0} - 1) * 100', einheit='%')
    K2 = K0 * q ** 2
    if (K2 * 100).denominator != 1: return None
    return zahl(f'Aus {dz(K0)} € werden in zwei Jahren mit gleichem Zinssatz {eu(K2)}. Wie hoch ist der Zinssatz in %?',
                f'q² = {eu(K2)} : {dz(K0)} € = {dz(q * q)}, q = √{dz(q * q)} = {qtxt(p)}, also {pt(p)}.', 'Erst q² bestimmen, dann die Wurzel ziehen.',
                p, f'{float(p)}', einheit='%')


def g_vergleich(s):
    art = R.choice({1: ['schneller', 'verdopplung_klein'], 2: ['angebot', 'verdopplung', 'schneller'], 3: ['angebot_bonus', 'verdopplung', 'faustregel']}[s])
    if art == 'schneller':
        K0, p, n = R.choice([1000, 2000, 5000]), R.choice([3, 4, 5]), R.choice([2, 3])
        zz, ez = K0 * Fr(100 + p, 100) ** n, K0 + K0 * Fr(p, 100) * n
        r = 'Mit Zinseszins.'
        return auswahl(f'{dz(K0)} € werden {n} Jahre mit {p} % angelegt. Womit ist am Ende mehr Geld da: mit einfachen Zinsen oder mit Zinseszins?', r,
                       ['Mit einfachen Zinsen.', 'Bei beiden gleich viel.', 'Das hängt vom Anfangskapital ab.'],
                       f'Einfach: {eu(ez)}. Zinseszins: {eu(cent(zz) or zz)}. Beim Zinseszins werden auch die Zinsen verzinst.', 'Werden die Zinsen im zweiten Jahr mitverzinst?')
    if art in ('verdopplung', 'verdopplung_klein'):
        p = R.choice([4, 5, 6, 8, 10]) if art == 'verdopplung' else R.choice([10, 12, 15, 20])
        q = 1 + p / 100
        n = math.ceil(math.log(2) / math.log(q))
        if abs(q ** n - 2) < 1e-4: return None
        return zahl(f'Nach wie vielen ganzen Jahren hat sich ein Kapital bei {p} % Zinseszins erstmals mindestens verdoppelt?',
                    f'{dz(round(q, 2))}^{n - 1} ≈ {dz(round(q ** (n - 1), 3))} < 2, aber {dz(round(q, 2))}^{n} ≈ {dz(round(q ** n, 3))} ≥ 2. Also nach {n} Jahren.',
                    'Probiere: qⁿ ≥ 2. Starte z. B. bei 72 : p.', n, f'{n}')
    if art == 'faustregel':
        p = R.choice([3, 4, 6, 8, 9, 12])
        return zahl(f'Faustregel: Ein Kapital verdoppelt sich bei p % Zinseszins nach etwa 72 : p Jahren. Nach etwa wie vielen Jahren bei {p} %?',
                    f'72 : {p} = {dz(Fr(72, p))} Jahre (Genau: 1,{p:02d}ⁿ ≥ 2 bei n = {math.ceil(math.log(2) / math.log(1 + p / 100))}).',
                    'Teile 72 durch den Zinssatz.', Fr(72, p), f'72 / {p}')
    K0 = R.choice([2000, 5000, 10000])
    n = R.choice([3, 4, 5])
    pA, pB = R.sample([2, 3, 4], 2)
    if art == 'angebot':
        A, B = K0 * Fr(100 + pA, 100) ** n, K0 * Fr(100 + pB, 100) ** n
        r = 'Bank A' if A > B else 'Bank B'
        return auswahl(f'{dz(K0)} € sollen {n} Jahre angelegt werden. Bank A bietet {pA} % Zinseszins, Bank B {pB} % Zinseszins. Welche Bank ist besser?', r,
                       ['Bank A', 'Bank B', 'Beide gleich'], f'A: {eu(cent(A) or A)}, B: {eu(cent(B) or B)}. Höherer Zinssatz bei gleicher Laufzeit gewinnt.',
                       'Vergleiche die Endbeträge (oder einfach die Zinssätze).')
    bonus = R.choice([50, 100, 150, 200])
    p1, p2 = 2, 3
    A = K0 * Fr(100 + p1, 100) ** n + bonus
    B = K0 * Fr(100 + p2, 100) ** n
    if abs(A - B) < 5: return None
    r = 'Angebot A' if A > B else 'Angebot B'
    return auswahl(f'{dz(K0)} € für {n} Jahre. Angebot A: {p1} % Zinseszins und ein Bonus von {bonus} €, der am Ende ausgezahlt wird. Angebot B: {p2} % Zinseszins ohne Bonus. Was bringt mehr?', r,
                   ['Angebot A', 'Angebot B', 'Beide gleich'],
                   f'A: {eu(cent(K0 * Fr(100 + p1, 100) ** n) or 0)} + {bonus} € = {eu(cent(A) or A)}. B: {eu(cent(B) or B)}. Mehr bringt {r[-1]}.',
                   'Rechne beide Endbeträge aus – der Bonus zählt einmal.')


GEN = schoen({'jahr': g_jahr, 'faktor': g_faktor, 'formel': g_formel, 'rueck': g_rueck, 'vergleich': g_vergleich})

bauen('finanzen.zinseszins',
      'Kapital mit Zinseszins berechnen, den Wachstumsfaktor nutzen, rückwärts rechnen und Angebote vergleichen.',
      ['Zinseszins (compound interest): Zinsen werden mitverzinst.',
       'Wachstumsfaktor q = 1 + p/100 (Abnahme: q = 1 − p/100).',
       'Kₙ = K₀ · qⁿ; rückwärts K₀ = Kₙ : qⁿ.',
       'Geldbeträge am Ende auf Cent runden.'],
      [('Verzinsen', ['jahr', 'faktor', 'formel']), ('Rückwärts und vergleichen', ['rueck', 'vergleich'])],
      ETAPPEN, GEN,
      offen=['Ohne Lehrplan-Zuordnung; Niveau Klasse 9/10 angenommen (Potenzen mit Taschenrechner, Rundung auf Cent mit Toleranz 0,01). Logarithmen zur Laufzeit-Berechnung nicht verwendet – Verdopplungszeit durch Probieren.',
             'Feld klasse: {"zusatz": 10} statt {} (Prüfskript verlangt einen Eintrag) – siehe FRAGE im Postfach.',
             'Überschneidung möglich mit bruch.prozent / Wachstum (Gymnasium Klasse 7 bzw. funktionen.exponential_log Klasse 10); hier eigenständig mit Zinsen.'])
