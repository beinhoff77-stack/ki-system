#!/usr/bin/env python3
"""Thema finanzen.zinseszins – Zinseszins (ohne Lehrplan-Zuordnung, Niveau Klasse 9/10)."""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _ib import *  # noqa: E402,F403
from _rsib2 import PLAN2, art3  # noqa: E402

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
    art = R.choice({1: ['z1', 'k1'], 2: ['k2', 'z2', 'k3'], 3: ['k3', 'z2', 'einfach_diff']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['kn'], 2: ['zinsen', 'kn_abnahme', 'zinsen'], 3: ['kn_abnahme', 'zinsen', 'kn']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['k0_1'], 2: ['k0_n', 'p_1'], 3: ['p_2', 'k0_n', 'p_2']}[s])  # Durchsicht 19
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
    art = R.choice({1: ['schneller', 'verdopplung_klein'], 2: ['verdopplung'], 3: ['angebot_bonus', 'verdopplung', 'faustregel']}[s])  # Durchsicht 19
    if art == 'schneller':
        K0, p, n = R.choice([1000, 2000, 5000]), R.choice([3, 4, 5]), R.choice([2, 3])
        zz, ez = K0 * Fr(100 + p, 100) ** n, K0 + K0 * Fr(p, 100) * n
        r = 'Mit Zinseszins.'
        return auswahl(f'{dz(K0)} € werden {n} Jahre mit {p} % angelegt. Womit ist am Ende mehr Geld da: mit einfachen Zinsen oder mit Zinseszins?', r,
                       ['Mit einfachen Zinsen.', 'Bei beiden gleich viel.', 'Das hängt vom Anfangskapital ab.'],
                       f'Einfach: {eu(ez)}. Zinseszins: {eu(cent(zz) or zz)}. Beim Zinseszins werden auch die Zinsen verzinst.', 'Werden die Zinsen im zweiten Jahr mitverzinst?')
    if art in ('verdopplung', 'verdopplung_klein'):
        p = R.choice([3, 4, 5, 6, 7, 8, 9, 10, 12]) if art == 'verdopplung' else R.choice([10, 12, 15, 20])
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


# ---------- DURCHSICHT (Neunzehnte Runde, Teil B, Zweig durchsicht-rsib-2) ----------
# Prüfungsvorbilder: Abschlussprüfung Realschule Bayern Mathematik I/II (Wachstum/Abnahme: „Um wie viel Prozent … pro Jahr?“,
# Anfangswert berechnen, Probieren für die Laufzeit), IB MYP (compound interest: Vergleich von Angeboten, unterjährige Verzinsung). Eigene Zahlen.
def jahr3(art):
    if art == 'einzahlung':
        K0, p, E = R.choice([1000, 2000, 1500, 800]), R.choice([Fr(2), Fr(3), Fr(4), Fr(5)]), R.choice([200, 500, 1000])
        q = 1 + p / 100
        k2 = (K0 * q + E) * q
        if (k2 * 100).denominator != 1: return None
        return zahl(f'{dz(K0)} € werden mit {pt(p)} Zinseszins angelegt. Nach einem Jahr zahlt man {dz(E)} € dazu. Wie hoch ist das Kapital nach 2 Jahren?',
                    f'Nach Jahr 1: {dz(K0)} € · {qtxt(p)} = {eu(K0 * q)}. Plus {dz(E)} € = {eu(K0 * q + E)}. Nach Jahr 2: {eu(K0 * q + E)} · {qtxt(p)} = {eu(k2)}.',
                    'Verzinse zuerst ein Jahr, addiere dann die Einzahlung und verzinse die Summe.', k2, f'({K0} * {float(q)} + {E}) * {float(q)}', einheit='€')
    # zinsen_rueck: aus den Zinsen im 2. Jahr das Anfangskapital
    K0, p = R.choice([1000, 2000, 2500, 4000, 5000, 800]), R.choice([Fr(2), Fr(4), Fr(5), Fr(10)])
    q = 1 + p / 100
    z2 = K0 * q * p / 100
    if (z2 * 100).denominator != 1: return None
    return zahl(f'Bei {pt(p)} Zinseszins gab es im zweiten Jahr {eu(z2)} Zinsen. Wie hoch war das Anfangskapital?',
                f'Zinsen im 2. Jahr = K₁ · {dz(p / 100)}, also K₁ = {eu(z2)} : {dz(p / 100)} = {eu(K0 * q)}. K₀ = {eu(K0 * q)} : {qtxt(p)} = {eu(K0)}.',
                'Die Zinsen im 2. Jahr gehören zum Kapital nach dem 1. Jahr. Rechne zweimal rückwärts.', K0, f'{float(z2)} / {float(p / 100)} / {float(q)}', einheit='€')


def faktor3(art):
    if art == 'plus_minus':
        p = R.choice([10, 20, 25, 50])
        g = (1 + Fr(p, 100)) * (1 - Fr(p, 100))
        return zahl(f'Ein Preis steigt um {p} % und sinkt danach um {p} %. Mit welchem Faktor wurde er insgesamt multipliziert?',
                    f'{dz(1 + Fr(p, 100))} · {dz(1 - Fr(p, 100))} = {dz(g)}. Der Preis ist danach um {dz((1 - g) * 100)} % niedriger als vorher – nicht gleich.',
                    'Beide Faktoren multiplizieren, nicht die Prozente verrechnen.', g, f'{1 + p / 100} * {1 - p / 100}')
    # halbjahr
    p = R.choice([2, 4, 6, 8])
    h = Fr(p, 2)
    g_h = (1 + h / 100) ** 2
    return auswahl(f'Bank A zahlt jährlich {p} % Zinsen. Bank B zahlt jedes halbe Jahr {dz(h)} % Zinsen, die mitverzinst werden. Welche Bank bringt nach einem Jahr mehr?', 'Bank B',
                   ['Bank A', 'Beide gleich viel', 'Das hängt vom Kapital ab.'],
                   f'A: Faktor {dz(1 + Fr(p, 100))}. B: {dz(1 + h / 100)}² = {dz(g_h)}. Bei B werden die Zinsen des ersten Halbjahrs im zweiten mitverzinst.',
                   'Vergleiche die Gesamtfaktoren für ein Jahr.')


def formel3(art):
    if art == 'laufzeit_vergleich':
        for _ in range(50):
            K0 = R.choice([2000, 5000, 10000])
            (n1, p1), (n2, p2) = R.sample([(10, Fr(2)), (8, Fr(5, 2)), (6, Fr(3)), (12, Fr(3, 2)), (5, Fr(4))], 2)
            a, b = K0 * (1 + p1 / 100) ** n1, K0 * (1 + p2 / 100) ** n2
            if abs(a - b) > 20: break
        else:
            return None
        r = 'Angebot A' if a > b else 'Angebot B'
        return auswahl(f'{dz(K0)} € sollen angelegt werden. Angebot A: {n1} Jahre zu {pt(p1)} Zinseszins. Angebot B: {n2} Jahre zu {pt(p2)} Zinseszins. Welches Angebot bringt am Ende mehr Geld?', r,
                       ['Angebot A', 'Angebot B', 'Beide gleich viel'],
                       f'A: {dz(K0)} € · {qtxt(p1)}^{n1} ≈ {eu(cent(a) or round(float(a), 2))}. B: {dz(K0)} € · {qtxt(p2)}^{n2} ≈ {eu(cent(b) or round(float(b), 2))}. Mehr bringt {r}.',
                       'Berechne beide Endkapitalien mit Kₙ = K₀ · qⁿ.')
    # zinsen_im_jahr
    K0, p, n = R.choice([2000, 5000, 10000]), R.choice([Fr(2), Fr(3), Fr(4), Fr(5)]), R.randint(4, 8)
    q = 1 + p / 100
    z = K0 * q ** (n - 1) * p / 100
    zc = cent(z)
    if zc is None: return None
    return zahl(f'{dz(K0)} € werden mit {pt(p)} Zinseszins angelegt. Wie viel Zinsen gibt es genau im {n}. Jahr? (auf Cent)',
                f'Am Anfang des {n}. Jahres: K_{n - 1} = {dz(K0)} € · {qtxt(p)}^{n - 1} ≈ {eu(cent(K0 * q ** (n - 1)) or 0)}. Zinsen im {n}. Jahr: {pt(p)} davon ≈ {eu(zc)}.',
                f'Im {n}. Jahr wird das Kapital nach {n - 1} Jahren verzinst.', zc, f'round({K0} * {float(q)} ** {n - 1} * {float(p)} / 100, 2)', einheit='€', tol=0.01)


def rueck3(art):
    if art == 'ziel':
        Z, p, n = R.choice([5000, 10000, 20000]), R.choice([Fr(2), Fr(3), Fr(4), Fr(5)]), R.randint(3, 8)
        q = 1 + p / 100
        k0 = cent(Z / q ** n)
        if k0 is None: return None
        return zahl(f'Wie viel Geld muss man heute zu {pt(p)} Zinseszins anlegen, um nach {n} Jahren {dz(Z)} € zu haben? (auf Cent)',
                    f'K₀ = Kₙ : qⁿ = {dz(Z)} € : {qtxt(p)}^{n} ≈ {eu(k0)}.', 'Rückwärts: durch qⁿ teilen.', k0, f'round({Z} / {float(q)} ** {n}, 2)', einheit='€', tol=0.01)
    # wie_lange
    K0, p, n = R.choice([1000, 2000, 5000]), R.choice([Fr(3), Fr(4), Fr(5), Fr(6)]), R.randint(3, 7)
    q = 1 + p / 100
    kn = cent(K0 * q ** n)
    if kn is None: return None
    return zahl(f'Ein Kapital von {dz(K0)} € wuchs bei {pt(p)} Zinseszins auf {eu(kn)}. Wie viele Jahre lag es auf dem Konto?',
                f'{eu(kn)} : {dz(K0)} € ≈ {dz(round(float(kn / K0), 4))}. Probieren: {qtxt(p)}^{n} ≈ {dz(round(float(q ** n), 4))}. Also {n} Jahre.',
                'Teile Endkapital durch Anfangskapital und probiere, welche Potenz von q das ergibt.', n, f'{n}')


def vergleich3(art):
    if art == 'zwei_autos':
        for _ in range(50):
            wa, pa = R.choice([30000, 36000, 40000]), R.choice([20, 25, 30])
            wb, pb = R.choice([20000, 24000, 25000]), R.choice([5, 10, 15])
            n = next((n for n in range(1, 30) if wb * (1 - Fr(pb, 100)) ** n > wa * (1 - Fr(pa, 100)) ** n), None)
            if n and 2 <= n <= 8: break
        else:
            return None
        fa, fb = 1 - Fr(pa, 100), 1 - Fr(pb, 100)
        return zahl(f'Auto A kostet neu {dz(wa)} € und verliert jedes Jahr {pa} % seines Werts. Auto B kostet neu {dz(wb)} € und verliert jedes Jahr {pb} %. Nach wie vielen ganzen Jahren ist Auto B erstmals mehr wert als Auto A?',
                    f'A: {dz(wa)} € · {dz(fa)}ⁿ, B: {dz(wb)} € · {dz(fb)}ⁿ. n = {n - 1}: A ≈ {eu(round(float(wa * fa ** (n - 1))))}, B ≈ {eu(round(float(wb * fb ** (n - 1))))}. '
                    f'n = {n}: A ≈ {eu(round(float(wa * fa ** n)))}, B ≈ {eu(round(float(wb * fb ** n)))}. Also nach {n} Jahren.',
                    'Stelle für beide Autos Wert = Neupreis · qⁿ auf und probiere Jahr für Jahr.', n, f'{n}')
    if art == 'halbierung':
        p = R.choice([8, 10, 12, 15, 20, 25, 30, 35, 40])
        f = 1 - Fr(p, 100)
        n = next(n for n in range(1, 50) if f ** n < Fr(1, 2))
        return zahl(f'Ein Auto verliert jedes Jahr {p} % seines Werts. Nach wie vielen ganzen Jahren ist es erstmals weniger als die Hälfte wert?',
                    f'q = {dz(f)}. {dz(f)}^{n - 1} ≈ {dz(round(float(f ** (n - 1)), 3))} ≥ 0,5, aber {dz(f)}^{n} ≈ {dz(round(float(f ** n), 3))} < 0,5. Also nach {n} Jahren.',
                    'Probiere qⁿ mit q = 1 − p/100, bis es unter 0,5 fällt.', n, f'{n}')
    # kreuzung: einfache Zinsen mit höherem Satz gegen Zinseszins
    pe, pz = R.choice([(6, 5), (5, 4), (8, 6), (10, 8)])
    n = next(n for n in range(1, 200) if (1 + Fr(pz, 100)) ** n > 1 + Fr(pe * n, 100))
    return zahl(f'Angebot A: {pe} % einfache Zinsen pro Jahr (immer vom Anfangskapital). Angebot B: {pz} % Zinseszins. Ab welchem Jahr hat man mit B mehr Geld als mit A?',
                f'A: Faktor 1 + {dz(Fr(pe, 100))} · n. B: {qtxt(pz)}ⁿ. Für n = {n - 1}: A {dz(round(1 + pe * (n - 1) / 100, 3))}, B ≈ {dz(round(float((1 + Fr(pz, 100)) ** (n - 1)), 3))}. '
                f'Für n = {n}: A {dz(round(1 + pe * n / 100, 3))}, B ≈ {dz(round(float((1 + Fr(pz, 100)) ** n), 3))}. Ab Jahr {n} ist B besser.',
                'Rechne für beide Angebote den Faktor nach n Jahren aus und probiere.', n, f'{n}')


def _filter(g, s, teil, nicht=False):
    for _ in range(120):
        t = g(s)
        if t and ((teil in t['f']['text']) != nicht): return t
    return None


def g2_jahr(s):
    if s == 1: return g_jahr(1)
    if s == 2: return _filter(g_jahr, R.choice([2, 3]), 'nach einem Jahr', nicht=True)
    art = art3('einfach_diff', 'einzahlung', 'zinsen_rueck', ['einfach_diff', 'einzahlung', 'zinsen_rueck', 'einfach_diff', 'einzahlung'])
    if art == 'einfach_diff': return _filter(g_jahr, 3, 'einfache Zinsen')
    return jahr3(art)


def g2_faktor(s):
    if s == 1: return g_faktor(1)
    if s == 2: return _filter(g_faktor, R.choice([2, 3]), 'insgesamt', nicht=True)
    art = art3('gesamt', 'plus_minus', 'halbjahr', ['gesamt', 'plus_minus', 'halbjahr', 'gesamt', 'plus_minus'])
    if art == 'gesamt': return _filter(g_faktor, 3, 'insgesamt')
    return faktor3(art)


def g2_formel(s):
    if s < 3: return g_formel(s)
    art = art3('auto', 'laufzeit_vergleich', 'zinsen_im_jahr', ['auto', 'laufzeit_vergleich', 'zinsen_im_jahr', 'auto', 'zinsen_im_jahr'])
    if art == 'auto': return _filter(g_formel, 3, 'verliert')
    return formel3(art)


def g2_rueck(s):
    if s < 3: return g_rueck(s)
    art = art3('p_2', 'ziel', 'wie_lange', ['p_2', 'ziel', 'wie_lange', 'k0_drei', 'ziel'])
    if art == 'p_2': return _filter(g_rueck, 3, 'gleichem Zinssatz')
    if art == 'k0_drei': return _filter(g_rueck, 3, 'Anfangskapital')
    return rueck3(art)


def g2_vergleich(s):
    if s == 1: return g_vergleich(1)
    if s == 2:
        teil = AKT['nr'] % 2 if AKT['pool'] == 'uebung' else R.random() < 0.5
        return g_vergleich(2) if teil else vergleich3('halbierung')
    art = art3('angebot_bonus', 'zwei_autos', 'kreuzung', ['angebot_bonus', 'zwei_autos', 'kreuzung', 'faustregel', 'zwei_autos'])
    if art == 'angebot_bonus': return _filter(g_vergleich, 3, 'Bonus')
    if art == 'faustregel': return _filter(g_vergleich, 3, 'Faustregel')
    return vergleich3(art)


GEN = schoen({'jahr': g2_jahr, 'faktor': g2_faktor, 'formel': g2_formel, 'rueck': g2_rueck, 'vergleich': g2_vergleich})

# ---------- UMBAU: neues Muster (Achte Runde, Paket UR, Vorgabe 16.11.) ----------
# Wird erst NACH dem Erzeugen der Aufgaben eingesetzt (siehe _umbau_rest.py) – die Aufgaben bleiben wörtlich gleich.
from _umbau_rest import umbau_schreiben  # noqa: E402

from _umbau_rest import tab  # noqa: E402


def _s(werte, y_start=900):
    return {'typ': 'saeulen', 'einheit': '€', 'werte': [{'name': n, 'wert': w} for n, w in werte], 'y_start': y_start, 'zahlen': True}


_J = [('Start', 1000), ('Jahr 1', 1050), ('Jahr 2', 1102.5)]
_F = [('J0', 5000), ('J1', 5100), ('J2', 5202), ('J3', 5306.04), ('J4', 5412.16), ('J5', 5520.40), ('J6', 5630.81)]
_QK = ['Zinssatz', 'Rechnung', 'q']
_RK = ['', 'Start', 'Jahr 1', 'Jahr 2']
_VK = ['n', '8', '9', '10', '11']
UMBAU = {
    'jahr': {
        'einstieg': 'Du legst 1 000 € auf ein Sparkonto mit 5 % Zinsen. Nach einem Jahr kommen die Zinsen aufs Konto. '
                    'Im zweiten Jahr gibt es auch Zinsen auf diese Zinsen: ⟦Zinseszins⟧.',
        'woerter': [['Zinseszins', 'Zinsen werden zum Kapital addiert und im nächsten Jahr mitverzinst'],
                    ['Kapital', 'das Geld auf dem Konto']],
        'bild': _s(_J[:1]),
        'schritte': [
            {'text': 'Jahr 1: 5 % von 1 000 € sind 50 € Zinsen.'},
            {'text': 'Das Kapital ist jetzt 1 050 €.', 'bild': _s(_J[:2])},
            {'text': 'Jahr 2: 5 % von 1 050 € sind 52,50 €.'},
            {'text': 'Nach zwei Jahren: ⟦1 102,50 €⟧.', 'bild': _s(_J)},
        ],
        'fehler': 'Im 2. Jahr wieder nur 50 € ist falsch, das wären ⟦einfache Zinsen⟧. Verzinst wird das neue Kapital 1 050 €.',
        'fehler_bild': _s(_J[:2] + [('falsch', 1100)]),
        'regel': 'Zinseszins: Zinsen kommen zum Kapital und werden ⟦mitverzinst⟧. Zinsen eines Jahres = Kapital · p %.',
    },
    'faktor': {
        'einstieg': 'Statt jedes Jahr Zinsen auszurechnen und zu addieren, geht es schneller. '
                    'Du nimmst das Kapital mit einer einzigen Zahl mal. Sie heißt ⟦Wachstumsfaktor⟧.',
        'woerter': [['Wachstumsfaktor q', 'q = 1 + p/100; bei 3 % ist q = 1,03'],
                    ['Zinssatz p', 'wie viel Prozent Zinsen es pro Jahr gibt']],
        'bild': tab(_QK, ['3 %', '?', '?']),
        'schritte': [
            {'text': 'Zinssatz p = 3 %, also 3/100 = 0,03.'},
            {'text': 'Wachstumsfaktor q = 1 + 0,03 = 1,03.', 'bild': tab(_QK, ['3 %', '1 + 0,03', '1,03'])},
            {'text': '2 000 € · 1,03 = ⟦2 060 €⟧ nach einem Jahr.'},
            {'text': 'Bei 15 % Abnahme ist q = 1 − 0,15 = 0,85.', 'bild': tab(_QK, ['3 %', '1 + 0,03', '1,03'], ['−15 %', '1 − 0,15', '0,85'])},
        ],
        'fehler': 'q = 1,3 bei 3 % ist falsch, das wären ⟦30 %⟧. 3 % sind 0,03, also q = 1,03.',
        'fehler_bild': tab(_QK, ['3 %', '1 + 0,3 ✗', '1,3 ✗']),
        'regel': '⟦q = 1 + p/100⟧. Mal q ersetzt das Ausrechnen und Addieren der Zinsen.',
    },
    'formel': {
        'einstieg': 'Du lässt 5 000 € sechs Jahre mit 2 % Zinsen auf dem Konto. Jedes Jahr wird mit 1,02 malgenommen, sechsmal hintereinander. '
                    'Kurz schreibt man das als ⟦Potenz⟧ 1,02⁶.',
        'woerter': [['K₀', 'das Anfangskapital'], ['Kₙ', 'das Kapital nach n Jahren'],
                    ['Potenz', '1,02⁶ heißt: sechsmal 1,02 malnehmen']],
        'bild': _s(_F[:1], 4800),
        'schritte': [
            {'text': 'Formel: Kₙ = K₀ · qⁿ.'},
            {'text': 'Hier ist K₀ = 5 000 €, q = 1,02 und n = 6.'},
            {'text': 'K₆ = 5 000 € · 1,02⁶ ≈ 5 000 € · 1,126162.', 'bild': _s(_F, 4800)},
            {'text': 'Auf Cent gerundet: ⟦5 630,81 €⟧.'},
        ],
        'fehler': '5 000 · 1,02 · 6 ist falsch. Der Faktor wird ⟦sechsmal malgenommen⟧, als Potenz 1,02⁶.',
        'regel': '⟦Kₙ = K₀ · qⁿ⟧. Am Ende auf Cent runden.',
    },
    'rueck': {
        'einstieg': 'Auf dem Konto sind nach 2 Jahren mit 5 % Zinsen 2 205 €. Wie viel wurde am Anfang eingezahlt? '
                    'Du rechnest ⟦rückwärts⟧: teilen statt malnehmen.',
        'woerter': [['Anfangskapital', 'das Geld, das am Anfang eingezahlt wurde: K₀']],
        'bild': tab(_RK, ['Kapital', '?', '?', '2 205 €']),
        'schritte': [
            {'text': 'Vorwärts wäre K₂ = K₀ · 1,05².'},
            {'text': 'Anfangskapital rückwärts: K₀ = 2 205 € : 1,05².'},
            {'text': '1,05² = 1,1025, also K₀ = ⟦2 000 €⟧.', 'bild': tab(_RK, ['Kapital', '2 000 €', '2 100 €', '2 205 €'])},
        ],
        'fehler': '2 205 € minus 2 · 5 % von 2 205 € ist falsch. Rückwärts wird ⟦durch qⁿ geteilt⟧.',
        'regel': 'Anfangskapital: ⟦K₀ = Kₙ : qⁿ⟧. Zinssatz für ein Jahr: q = K₁ : K₀, dann p = (q − 1) · 100.',
    },
    'vergleich': {
        'einstieg': 'Wann hat sich dein Geld verdoppelt? Mit einfachen Zinsen dauert es lange. Mit Zinseszins geht es schneller. '
                    'Die ⟦Verdopplung⟧ findest du durch Probieren.',
        'woerter': [['Verdopplung', 'das Kapital ist doppelt so groß: qⁿ ≥ 2'],
                    ['einfachen Zinsen', 'jedes Jahr Zinsen nur vom Startkapital']],
        'bild': tab(_VK, ['1,07ⁿ', '?', '?', '?', '?']),
        'schritte': [
            {'text': 'Bei 7 % gilt q = 1,07. 1,07¹⁰ ≈ 1,967 ist noch kleiner als 2.', 'bild': tab(_VK, ['1,07ⁿ', '1,718', '1,838', '1,967', '?'])},
            {'text': '1,07¹¹ ≈ 2,105, das ist mehr als 2.', 'bild': tab(_VK, ['1,07ⁿ', '1,718', '1,838', '1,967', '2,105 ✓'])},
            {'text': 'Nach ⟦11 Jahren⟧ hat sich das Kapital erstmals verdoppelt.'},
            {'text': 'Abnahme 20 %: q = 0,8. Erst 0,8⁴ ≈ 0,41 < 0,5, also ⟦4 Jahre⟧.'},
        ],
        'fehler': '„Bei 5 % nach 20 Jahren, weil 20 · 5 % = 100 %“ gilt nur für einfache Zinsen. Mit Zinseszins reichen ⟦15 Jahre⟧.',
        'regel': 'Zinseszins wächst ⟦schneller⟧ als einfache Zinsen. Verdopplung: n probieren, bis qⁿ ≥ 2.',
    },
}
UMBAU_OFFEN = []
UMBAU_WEG = []
# ---------- Ende UMBAU ----------


d = bauen('finanzen.zinseszins',
      'Kapital mit Zinseszins berechnen, den Wachstumsfaktor nutzen, rückwärts rechnen und Angebote vergleichen.',
      ['Zinseszins (compound interest): Zinsen werden mitverzinst.',
       'Wachstumsfaktor q = 1 + p/100 (Abnahme: q = 1 − p/100).',
       'Kₙ = K₀ · qⁿ; rückwärts K₀ = Kₙ : qⁿ.',
       'Geldbeträge am Ende auf Cent runden.'],
      [('Verzinsen', ['jahr', 'faktor', 'formel']), ('Rückwärts und vergleichen', ['rueck', 'vergleich'])],
      ETAPPEN, GEN,
      offen=['Ohne Lehrplan-Zuordnung; Niveau Klasse 9/10 angenommen (Potenzen mit Taschenrechner, Rundung auf Cent mit Toleranz 0,01). Logarithmen zur Laufzeit-Berechnung nicht verwendet – Verdopplungszeit durch Probieren.',
             'Feld klasse: {"zusatz": 10} statt {} (Prüfskript verlangt einen Eintrag) – siehe FRAGE im Postfach.',
             'Überschneidung möglich mit bruch.prozent / Wachstum (Gymnasium Klasse 7 bzw. funktionen.exponential_log Klasse 10); hier eigenständig mit Zinsen.'], plan=PLAN2)
umbau_schreiben(d, UMBAU, UMBAU_OFFEN, weg=UMBAU_WEG)


# ---- STUFEN (Zwanzigste Runde, Zusatz Realschule/IB, Zweig stufen-rsib-2) ----
from _stufen_rsib2 import Stufen, stufen  # noqa: E402

ST = Stufen('finanzen.zinseszins', 20_2_10)
Z, A, L = ST.Z, ST.A, ST.L
ST.vorbild += ['ISB Bayern, Muster-Abschlussprüfung Realschule Mathematik II (Muster 2022, Aufgabe B 2: Wachstum, „nach wie vielen Jahren erstmals …“, auf ganze Jahre runden) – https://www.isb.bayern.de/fileadmin/user_upload/Realschule/Mathematik/Weiterentwicklung_Abschlusspruefung/Muster-Abschlusspruefungen_II/mii_muster2022_b1b2.pdf',
               'IQB, Illustrierende Lernaufgabe Sek. I „Zinseszins“ (Fehlvorstellung lineares statt exponentielles Weiterrechnen; nur Art) – https://www.iqb.hu-berlin.de/media/exercise_files/Lernaufgaben_Mathematik_Sek_I/Zinseszins_Aufgabe.pdf']

# jahr
ST.stufenleiter('jahr', 'Zinsen und Kapital nach einem Jahr berechnen.',
                'Zwei Jahre Schritt für Schritt, Tabelle Jahr für Jahr, Kapital aus den Zinsen eines Jahres.',
                'Zinseszins gegen einfache Zinsen, Einzahlung zwischendurch, Anfangskapital aus Zinsen im 2. Jahr, Fehler „zweimal die gleichen Zinsen“, wachsende Zinsen begründen.')
ST.typ('jahr', '/^/', 'direkt', s=1)
ST.typ('jahr', '/^/', 'mehrschritt', s=2)
ST.typ('jahr', '/Wie viel mehr bringt/', 'verknuepfen')
ST.typ('jahr', '/zahlt man/', 'transfer')
ST.typ('jahr', '/^/', 'rueckwaerts', s=3)
ST.neu('jahr', 'erkennen', A('Was bedeutet Zinseszins?', 'Die Zinsen werden dem Kapital zugeschlagen und im nächsten Jahr mitverzinst.',
       ['Man bekommt jedes Jahr die gleichen Zinsen.', 'Die Zinsen werden jedes Jahr ausgezahlt.', 'Der Zinssatz steigt jedes Jahr.'],
       'Beim Zinseszins wächst die Grundlage: Zinsen bringen selbst wieder Zinsen.', 'Was passiert mit den Zinsen nach dem ersten Jahr?'))
ST.neu('jahr', 'einkleidung', Z('Für ein Kind werden 500 € mit 4 % Zinseszins angelegt. Wie viel ist nach 2 Jahren auf dem Konto?', 540.8, '500*1.04**2',
       'Jahr 1: 500 € + 20 € = 520 €. Jahr 2: 520 € + 20,80 € = 540,80 €.', 'Rechne Jahr für Jahr.', einheit='€'))
ST.neu('jahr', 'umkehr', Z('Bei 5 % Zinsen gab es im ersten Jahr 30 € Zinsen. Wie hoch war das Kapital?', 600, '30/0.05', '5 % sind 30 €, also 1 % = 6 € und 100 % = 600 €.', 'Von 5 % auf 100 % schließen.', einheit='€'))
ST.neu('jahr', 'darstellung', L('2 000 € zu 5 % Zinseszins. Fülle die Tabelle aus.', 'Jahr 1: Zinsen □ €, Kapital □ €; Jahr 2: Zinsen □ €, Kapital □ €', [100, 2100, 105, 2205],
       ['2000*0.05', '2000*1.05', '2100*0.05', '2000*1.05**2'], 'Jahr 1: 100 € Zinsen, 2 100 €. Jahr 2: 5 % von 2 100 € = 105 €, 2 205 €.', 'Im 2. Jahr wird vom neuen Kapital gerechnet.'))
ST.neu('jahr', 'fehler', A('1 000 € liegen 2 Jahre bei 5 % Zinseszins. Jemand rechnet: „2 · 50 € = 100 € Zinsen, also 1 100 €.“ Was stimmt?', 'Falsch: Es sind 1 102,50 €.',
       ['Richtig.', 'Falsch: Es sind 1 105 €.', 'Falsch: Es sind 1 050 €.'], 'Im 2. Jahr gibt es 5 % von 1 050 € = 52,50 €. Zusammen 1 102,50 €.', 'Wovon werden die Zinsen im 2. Jahr berechnet?'))
ST.neu('jahr', 'begruenden', A('Stimmt: Beim Zinseszins (Zinssatz größer als 0) sind die Zinsen jedes Jahr größer als im Jahr davor?', 'Ja, weil das Kapital jedes Jahr größer wird.',
       ['Nein, sie sind jedes Jahr gleich.', 'Nein, sie werden kleiner.', 'Nur bei Zinssätzen über 10 %.'],
       'Zinsen = p % vom aktuellen Kapital. Das Kapital wächst jedes Jahr um die Zinsen, also wachsen auch die nächsten Zinsen.', 'Wovon hängen die Zinsen eines Jahres ab?'))
ST.knobel('jahr', L('Ein Kapital bringt mit Zinseszins im ersten Jahr 40 € und im zweiten Jahr 42 € Zinsen. Wie hoch sind Zinssatz und Anfangskapital?', 'p = □ %; K₀ = □ €', [5, 800],
          ['(42/40 - 1)*100', '40/0.05'],
          'Die Zinsen des 2. Jahres sind die des 1. Jahres mal q: 42 : 40 = 1,05, also p = 5 %. Dann sind 40 € genau 5 % von K₀: K₀ = 800 €.', 'Wie hängen die Zinsen zweier aufeinanderfolgender Jahre zusammen?'))
ST.knobel('jahr', A('Was bringt mehr: ein Jahr zu 10 % oder zwei Jahre zu je 5 % Zinseszins?', 'zwei Jahre zu je 5 % (Faktor 1,1025 statt 1,10)', ['ein Jahr zu 10 %', 'beides gleich viel', 'Das hängt vom Kapital ab.'],
          '1,05 · 1,05 = 1,1025 > 1,10. Im zweiten Jahr werden die Zinsen des ersten Jahres mitverzinst: 5 % von 5 % = 0,25 % zusätzlich – unabhängig vom Kapital.', 'Vergleiche die Faktoren.'))

# faktor
ST.stufenleiter('faktor', 'Wachstumsfaktor q = 1 + p/100 bilden und erkennen, ob Zunahme oder Abnahme.',
                'Zinssatz aus q, Abnahmefaktor, Rechnung zu einem Text, mit q rechnen.',
                'Faktoren verketten, +20 % / −20 %, halbjährliche Zinsen, Fehler „+10 % +10 % = +20 %“, Prozentsatz aus Gesamtfaktor.')
ST.typ('faktor', '/^/', 'direkt', s=1)
ST.typ('faktor', '/Zinssatz in %|Um wie viel Prozent/', 'umkehr')
ST.typ('faktor', '/^/', 'einkleidung', s=2)
ST.typ('faktor', '/im zweiten mit/', 'verknuepfen')
ST.typ('faktor', '/sinkt danach/', 'transfer')
ST.typ('faktor', '/^/', 'begruenden', s=3)
ST.neu('faktor', 'erkennen', A('Welcher Faktor beschreibt eine Abnahme?', '0,92', ['1,08', '1,2', '2'], 'Ein Faktor kleiner als 1 verkleinert: 0,92 heißt −8 %.', 'Größer oder kleiner als 1?'))
ST.neu('faktor', 'direkt', Z('Ein Preis von 50 € steigt um 6 %. Rechne mit dem Faktor: Wie hoch ist der neue Preis?', 53, '50*1.06', '50 € · 1,06 = 53 €.', 'q = 1 + 6/100.', einheit='€'))
ST.neu('faktor', 'mehrschritt', Z('1 000 € werden 2 Jahre lang mit dem Faktor q = 1,05 verzinst. Wie hoch ist das Kapital danach?', 1102.5, '1000*1.05**2',
       '1 000 € · 1,05 · 1,05 = 1 102,50 €.', 'Zweimal mit q multiplizieren.', einheit='€'))
ST.neu('faktor', 'darstellung', A('Welche Rechnung passt zu: „Der Wert W sinkt jedes Jahr um 12 %“ (Wert nach einem Jahr)?', 'W · 0,88', ['W · 1,12', 'W − 0,12', 'W · 0,12'],
       '100 % − 12 % = 88 %, also Faktor 0,88. W · 0,12 wäre nur der Verlust.', 'Wie viel Prozent bleiben übrig?'))
ST.neu('faktor', 'fehler', A('Ein Preis steigt zweimal hintereinander um 10 %. Jemand sagt: „Insgesamt sind das 20 %.“ Was stimmt?', 'Falsch: 1,1 · 1,1 = 1,21, also 21 %.',
       ['Richtig.', 'Falsch: Es sind 100 %.', 'Falsch: Es sind 11 %.'], 'Die zweite Erhöhung bezieht sich auf den schon erhöhten Preis. Faktoren werden multipliziert, nicht Prozente addiert.', 'Multipliziere die Faktoren.'))
ST.neu('faktor', 'rueckwaerts', Z('Nach zwei gleichen prozentualen Erhöhungen wurde ein Preis insgesamt mit 1,21 multipliziert. Um wie viel Prozent stieg er jedes Mal?', 10, '(1.1 - 1)*100',
       'q · q = 1,21 ⇒ q = 1,1 (denn 1,1² = 1,21). Also 10 % pro Erhöhung.', 'Welche Zahl ergibt mit sich selbst multipliziert 1,21?', einheit='%'))
ST.knobel('faktor', Z('Ein Preis sinkt um 20 %. Um wie viel Prozent muss er danach steigen, damit er wieder so hoch ist wie vorher?', 25, '(1/0.8 - 1)*100',
          'Nach der Senkung: Faktor 0,8. Gesucht q mit 0,8 · q = 1 ⇒ q = 1,25. Also +25 %, weil sich die Erhöhung auf den kleineren Preis bezieht.', 'Mit welchem Faktor kommt man von 0,8 wieder auf 1?', einheit='%'))
ST.knobel('faktor', A('Eine Bank zahlt statt 12 % pro Jahr jeden Monat 1 %, die mitverzinst werden. Ist das im Jahr mehr oder weniger als 12 %?', 'mehr (etwa 12,7 %)',
          ['weniger', 'genau 12 %', 'genau 13 %'],
          'Jahresfaktor 1,01¹² ≈ 1,1268. Jeder Monatszins wird in den Folgemonaten mitverzinst, darum kommt etwas mehr als 12 % heraus.', 'Rechne mit Faktoren: 12-mal 1,01.'))

# formel
ST.stufenleiter('formel', 'Kₙ = K₀ · qⁿ einsetzen und ausrechnen.',
                'Gesamtzinsen, Wertverlust, Zinssatz aus der Formel ablesen, Formel zu einem Text.',
                'Zwei Angebote vergleichen, Zinsen genau eines Jahres, Fehler „mal n statt hoch n“, Zinssatz zu einem Endkapital, Proportionalität zu K₀, mehrteilige Prüfungsaufgabe.')
ST.typ('formel', '/^/', 'direkt', s=1)
ST.typ('formel', '/Auto/', 'einkleidung')
ST.typ('formel', '/^/', 'mehrschritt', s=2)
ST.typ('formel', '/Angebot A/', 'transfer')
ST.typ('formel', '/^/', 'verknuepfen', s=3)
ST.neu('formel', 'erkennen', A('Welcher Term gibt das Kapital nach 7 Jahren bei 3 % Zinseszins an (K₀ = 1 000 €)?', '1 000 · 1,03⁷', ['1 000 · 1,03 · 7', '1 000 · 0,03⁷', '1 000 + 7 · 30'],
       'Kₙ = K₀ · qⁿ mit q = 1,03 und n = 7.', 'Wie oft wird mit q multipliziert?'))
ST.neu('formel', 'direkt', Z('Berechne das Kapital nach 2 Jahren: 800 € zu 5 % Zinseszins.', 882, '800*1.05**2', '800 € · 1,05² = 800 € · 1,1025 = 882 €.', 'K₂ = K₀ · q².', einheit='€'))
ST.neu('formel', 'umkehr', Z('In der Rechnung K₈ = 3 000 € · 1,025⁸ steckt ein Zinssatz. Wie groß ist er in %?', 2.5, '(1.025 - 1)*100', 'q = 1,025 = 1 + 2,5/100, also p = 2,5 %.', 'Lies q ab.', einheit='%'))
ST.neu('formel', 'darstellung', A('Welche Rechnung passt zu: „4 500 € werden 6 Jahre mit 3,5 % Zinseszins angelegt“?', '4 500 · 1,035⁶', ['4 500 · 1,035 · 6', '4 500 · 0,035⁶', '4 500 · 1,35⁶'],
       'q = 1 + 3,5/100 = 1,035, n = 6: K₆ = 4 500 · 1,035⁶.', 'Bilde zuerst q.'))
ST.neu('formel', 'fehler', A('2 000 € liegen 3 Jahre bei 5 % Zinseszins. Jemand rechnet 2 000 · 1,05 · 3 = 6 300 €. Was stimmt?', 'Falsch: Man muss potenzieren: 2 000 · 1,05³ = 2 315,25 €.',
       ['Richtig.', 'Falsch: 2 000 · 0,05 · 3 = 300 €.', 'Falsch: 2 000 + 3 · 1,05 = 2 003,15 €.'],
       '„Mal 3“ verdreifacht das Geld. Richtig wird dreimal mit 1,05 multipliziert: 1,05³ = 1,157625.', 'Wie oft wird mit q multipliziert?'))
ST.neu('formel', 'parameter', Z('Für welchen ganzzahligen Zinssatz p werden aus 1 000 € in 2 Jahren genau 1 166,40 €?', 8, '(1.08 - 1)*100',
       'q² = 1 166,40 : 1 000 = 1,1664. 1,08² = 1,1664 ⇒ q = 1,08, p = 8 %.', 'Teile durch K₀ und suche q.', einheit='%'))
ST.neu('formel', 'begruenden', A('Stimmt: Legt man bei gleichem Zinssatz und gleicher Laufzeit doppelt so viel Geld an, hat man am Ende doppelt so viel?', 'Ja, Kₙ = K₀ · qⁿ ist proportional zu K₀.',
       ['Nein, wegen des Zinseszinses mehr als doppelt so viel.', 'Nein, weniger als doppelt so viel.', 'Nur bei einer Laufzeit von einem Jahr.'],
       'qⁿ hängt nicht von K₀ ab. Verdoppelt man K₀, verdoppelt sich das Produkt K₀ · qⁿ.', 'Wo steht K₀ in der Formel?'))
ST.neu('formel', 'pruefung', L('Ein Betrag von 2 000 € wird zu 5 % Zinseszins angelegt. a) Wie hoch ist das Kapital nach 2 Jahren? b) Nach wie vielen ganzen Jahren sind erstmals mehr als 2 400 € auf dem Konto?',
       'a) □ €; b) □ Jahre', [2205, 4], ['2000*1.05**2', '4'],
       'a) 2 000 · 1,05² = 2 205 €. b) Nach 3 Jahren 2 315,25 €, nach 4 Jahren 2 431,01 €: erstmals nach 4 Jahren über 2 400 €.', 'Für b) rechne Jahr für Jahr weiter.'))
ST.knobel('formel', A('Zwei Konten: A hat 1 000 € zu 4 %, B hat 1 040 € zu 4 % (beide Zinseszins). Wie verhält sich der Unterschied der Kontostände in den folgenden Jahren?', 'Er wächst jedes Jahr um 4 %.',
          ['Er bleibt immer 40 €.', 'Er wird kleiner.', 'Er verdoppelt sich jedes Jahr.'],
          'Unterschied nach n Jahren: 1 040 · 1,04ⁿ − 1 000 · 1,04ⁿ = 40 · 1,04ⁿ. Er wird also wie ein eigenes Kapital mitverzinst.', 'Klammere 1,04ⁿ aus.'))
ST.knobel('formel', Z('Ein Kapital wächst mit 10 % Zinseszins. Nach 2 Jahren beträgt es 1 210 €. Wie viel beträgt es nach 4 Jahren?', 1464.1, '1210*1.1**2',
          'Von Jahr 2 bis Jahr 4 kommen noch zwei Faktoren 1,1 dazu: 1 210 € · 1,21 = 1 464,10 €. Das Anfangskapital braucht man dafür nicht.', 'Rechne von Jahr 2 aus weiter.', einheit='€'))

# rueck
ST.stufenleiter('rueck', 'Anfangskapital nach einem Jahr durch Teilen durch q.',
                'Zinssatz aus Anfangs- und Endkapital, Anfangskapital nach zwei Jahren, Rückrechnung in einer Sachsituation.',
                'Zinssatz über zwei Jahre, heute anlegen für ein Ziel, Laufzeit bestimmen, Fehler „Zinsen abziehen“, „+25 % ist nicht −25 %“.')
ST.typ('rueck', '/^/', 'direkt', s=1)
ST.typ('rueck', '/Zinssatz in %/', 'umkehr', s=2)
ST.typ('rueck', '/^/', 'mehrschritt', s=2)
ST.typ('rueck', '/Zinssatz in %/', 'rueckwaerts')
ST.typ('rueck', '/heute/', 'verknuepfen')
ST.typ('rueck', '/Wie viele Jahre/', 'transfer')
ST.typ('rueck', '/^/', 'mehrschritt', s=3)
ST.neu('rueck', 'erkennen', A('Wie kommt man vom Endkapital Kₙ zurück zum Anfangskapital K₀?', 'durch qⁿ teilen', ['p % abziehen', 'mit qⁿ multiplizieren', 'n · p % abziehen'],
       'Kₙ = K₀ · qⁿ ⇒ K₀ = Kₙ : qⁿ.', 'Kehre die Rechnung um.'))
ST.neu('rueck', 'direkt', Z('Ein Kapital ist durch 3 % Zinsen in einem Jahr auf 2 060 € gewachsen. Wie hoch war es vorher?', 2000, '2060/1.03', '2 060 € : 1,03 = 2 000 €.', 'Teile durch q.', einheit='€'))
ST.neu('rueck', 'einkleidung', Z('Ein Fahrrad kostet nach einer Preiserhöhung um 8 % jetzt 540 €. Was kostete es vorher?', 500, '540/1.08', '540 € : 1,08 = 500 €.', 'Der alte Preis ist 100 %.', einheit='€'))
ST.neu('rueck', 'darstellung', A('Nach 3 Jahren mit 10 % Zinseszins sind 1 331 € auf dem Konto. Welche Rechnung liefert das Anfangskapital?', '1 331 : 1,1³', ['1 331 − 3 · 133,10', '1 331 · 0,9³', '1 331 : 1,3'],
       'K₀ = K₃ : q³ = 1 331 : 1,331 = 1 000 €. 0,9³ wäre eine Abnahme um 10 % pro Jahr – das ist nicht die Umkehrung.', 'Welche Rechnung macht K₀ · 1,1³ rückgängig?'))
ST.neu('rueck', 'fehler', A('Nach 2 Jahren mit 10 % Zinseszins sind 1 210 € auf dem Konto. Jemand rechnet 1 210 − 2 · 121 = 968 €. Was stimmt?', 'Falsch: 1 210 : 1,1² = 1 000 €.',
       ['Richtig.', 'Falsch: 1 210 − 2 · 100 = 1 010 €.', 'Falsch: 1 210 · 0,8 = 968 € ist auch richtig.'],
       'Die Zinsen wurden vom kleineren Kapital berechnet. Rückwärts teilt man durch q²: 1 210 : 1,21 = 1 000. Probe: 1 000 → 1 100 → 1 210.', 'Mache die Probe vorwärts.'))
ST.neu('rueck', 'begruenden', A('Ein Kapital ist um 25 % gestiegen. Stimmt: Um zurückzurechnen, zieht man 25 % vom neuen Wert ab?', 'Nein: Man teilt durch 1,25, das sind nur 20 % weniger.',
       ['Ja.', 'Nein: Man zieht 125 % ab.', 'Nein: Man teilt durch 0,75.'], 'Beispiel 100 € → 125 €. 25 % von 125 € sind 31,25 €, das ergäbe 93,75 €. 125 : 1,25 = 100 – das sind 20 % weniger als 125.', 'Probiere es mit 100 €.'))
ST.knobel('rueck', Z('Ein Kapital wuchs in 2 Jahren mit gleichem Zinssatz (Zinseszins) um insgesamt 44 %. Wie hoch war der Zinssatz?', 20, '(1.2 - 1)*100',
          'Gesamtfaktor 1,44 = q² ⇒ q = 1,2. Der Zinssatz war 20 % – nicht 22 %, weil die Zinsen des ersten Jahres mitverzinst werden.', 'Welcher Faktor ergibt quadriert 1,44?', einheit='%'))
ST.knobel('rueck', Z('Nach 3 Jahren mit 10 % Zinseszins sind 2 662 € auf dem Konto. Wie viel Zinsen gab es im ersten Jahr?', 200, '2662/1.1**3*0.1',
          'K₀ = 2 662 : 1,331 = 2 000 €. Zinsen im ersten Jahr: 10 % von 2 000 € = 200 €.', 'Bestimme zuerst das Anfangskapital.', einheit='€'))

# vergleich
ST.stufenleiter('vergleich', 'Verdopplungszeit durch Probieren, einfache Zinsen gegen Zinseszins.',
                'Halbierungszeit bei Wertverlust, Tabelle über mehrere Jahre, Zinssatz zu einer Verdopplungszeit.',
                'Angebote mit Bonus, zwei Autos, wann Zinseszins einfache Zinsen überholt, Faustregel 72 : p, Fehler „100 : p“.')
ST.typ('vergleich', '/einfachen Zinsen oder mit Zinseszins/', 'erkennen')
ST.typ('vergleich', '/^/', 'direkt', s=1)
ST.typ('vergleich', '/Auto verliert/', 'einkleidung')
ST.typ('vergleich', '/^/', 'mehrschritt', s=2)
ST.typ('vergleich', '/Bonus/', 'verknuepfen')
ST.typ('vergleich', '/Ab welchem Jahr/', 'begruenden')
ST.typ('vergleich', '/^/', 'transfer', s=3)
ST.neu('vergleich', 'umkehr', A('Ein Kapital hat sich mit Zinseszins in 10 Jahren etwa verdoppelt. Welcher Zinssatz passt am besten?', '7 %', ['5 %', '10 %', '20 %'],
       '1,05¹⁰ ≈ 1,63, 1,07¹⁰ ≈ 1,97, 1,10¹⁰ ≈ 2,59. Am nächsten an 2 liegt 7 %.', 'Rechne q¹⁰ für die Angebote aus.'))
ST.neu('vergleich', 'darstellung', L('1 000 € zu 10 % Zinseszins. Trage das Kapital nach 1, 2 und 3 Jahren ein.', '□ €; □ €; □ €', [1100, 1210, 1331], ['1000*1.1', '1000*1.1**2', '1000*1.1**3'],
       '1 000 · 1,1 = 1 100; · 1,1 = 1 210; · 1,1 = 1 331.', 'Jedes Jahr mit 1,1 multiplizieren.'))
ST.neu('vergleich', 'fehler', A('Jemand sagt: „Bei 6 % Zinseszins verdoppelt sich ein Kapital nach 100 : 6 ≈ 17 Jahren.“ Was stimmt?', 'Falsch: Schon nach 12 Jahren (1,06¹² ≈ 2,01).',
       ['Richtig.', 'Falsch: nach 6 Jahren.', 'Falsch: nach 20 Jahren.'],
       '100 : 6 gilt für einfache Zinsen. Mit Zinseszins: 1,06¹¹ ≈ 1,90, 1,06¹² ≈ 2,01. Die Faustregel 72 : 6 = 12 passt.', 'Rechne 1,06ⁿ für einige n aus.'))
ST.knobel('vergleich', Z('Konto A: 1 000 € zu 10 %. Konto B: 2 000 € zu 3 % (beide Zinseszins). Nach wie vielen ganzen Jahren hat A erstmals mehr Geld als B?', 11, '11',
          'Nach 10 Jahren: A ≈ 2 593,74 €, B ≈ 2 687,83 € – B liegt noch vorn. Nach 11 Jahren: A ≈ 2 853,12 €, B ≈ 2 768,47 € – jetzt liegt A vorn. Der höhere Zinssatz holt den doppelten Startbetrag ein.',
          'Rechne beide Konten für einige Jahre aus.', einheit='Jahre'))
ST.knobel('vergleich', A('Was bringt mehr: 70 Jahre lang 1 % Zinseszins oder einmalig 70 % Zinsen?', '70 Jahre 1 % Zinseszins (etwa Verdopplung, +100 %)', ['einmalig 70 %', 'beides gleich', 'Das hängt vom Kapital ab.'],
          'Faustregel: Verdopplung nach 72 : 1 = 72 Jahren; genauer 1,01⁷⁰ ≈ 2,007. Das sind etwa +100 % statt +70 %.', 'Denke an die Faustregel 72 : p.'))

if __name__ == '__main__':
    stufen('finanzen.zinseszins', ST)
