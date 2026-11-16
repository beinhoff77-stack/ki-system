#!/usr/bin/env python3
"""Thema finanzen.zinsen – Einfache Zinsen (Gymnasium Bayern, Klasse 6). Runde 9: Aufgaben auffüllen.

Lernkarten unverändert aus inhalte/klar/finanzen.zinsen.json; neu sind nur die Aufgaben.
Modell wie auf den Karten: fester Jahreszinssatz, gleichbleibendes Kapital, keine Zinsen auf Zinsen. Alle Beträge sind exakte Cent-Beträge.
"""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _auffuellen import A, Z, baue, etappen_aus_klar, eur, g4, zt  # noqa: E402

META = {'thema_schluessel': 'finanzen.zinsen', 'thema_id': 71, 'block_id': 52, 'klasse': {'gym_by': 6}}
TITEL = [('begriffe', 'Die drei Größen'), ('rollen', 'Wer zahlt, wer bekommt?'), ('jahreszinsen', 'Jahreszinsen berechnen'),
         ('jahreszinsen_komma', 'Zinssatz mit Komma'), ('zinssatz', 'Zinssatz finden'), ('kapital', 'Kapital finden'),
         ('monatszinsen', 'Zinsen für Monate'), ('zeitanteil', 'Halbes Jahr, Vierteljahr')]
ETAPPEN = etappen_aus_klar(META['thema_schluessel'], TITEL)


def e(x): return g4(eur(x)) + ' €'
def pz(p): return zt(Fr(str(p))) + ' %'
def cent(x): return Fr(x) * 100 == int(Fr(x) * 100)
def ps(p): return str(p)  # Prozentzahl im Rechenausdruck (z. B. 2.5)


# ---------------- Die drei Größen ----------------
def g_begriffe(R, s):
    K = R.randint(5, 60) * 100
    p = R.randint(1, 6)
    Zi = K * p // 100
    if s == 1:
        frage = R.choice(['Kapital', 'Zinsen', 'Jahreszinssatz'])
        richtig = {'Kapital': e(K), 'Zinsen': e(Zi), 'Jahreszinssatz': pz(p)}[frage]
        alle = [e(K), e(Zi), pz(p), e(K + Zi)]
        return A(R, f'Jemand legt {e(K)} für ein Jahr auf ein Sparkonto. Die Bank zahlt {pz(p)} Zinsen pro Jahr, das sind {e(Zi)}. Was ist hier {"das" if frage == "Kapital" else "der" if frage == "Jahreszinssatz" else "die"} {frage}?',
                 richtig, [x for x in alle if x != richtig],
                 f'Kapital = angelegtes Geld: {e(K)}. Jahreszinssatz = Prozentsatz: {pz(p)}. Zinsen = Betrag in Euro: {e(Zi)}.',
                 'Kapital und Zinsen sind Beträge in Euro, der Zinssatz ist ein Prozentsatz.')
    if s == 2:
        return Z(f'Auf einem Sparkonto liegen {e(K)}. Nach einem Jahr gibt die Bank {e(Zi)} Zinsen dazu. Wie viel Geld ist dann auf dem Konto?', K + Zi, f'{K} + {Zi}',
                 f'Kapital plus Zinsen: {e(K)} + {e(Zi)} = {e(K + Zi)}.', 'Die Zinsen kommen zum Kapital dazu.', einheit='€')
    art = R.choice(['rueck', 'fehler'])
    if art == 'rueck':
        return Z(f'Jemand hat {e(K)} angelegt. Nach einem Jahr sind {e(K + Zi)} auf dem Konto. Wie hoch waren die Zinsen?', Zi, f'{K + Zi} - {K}',
                 f'Zinsen = neuer Kontostand − Kapital = {e(K + Zi)} − {e(K)} = {e(Zi)}.', 'Was ist dazugekommen?', einheit='€')
    return A(R, f'Jemand sagt: „Bei {e(K)} Kapital bekomme ich {pz(p)} Zinsen.“ Was ist daran ungenau?',
             f'{pz(p)} ist der Zinssatz; die Zinsen sind ein Betrag: {e(Zi)}.',
             ['Nichts, Zinsen und Zinssatz sind dasselbe.', f'Die Zinsen sind {e(K)}.', f'Der Zinssatz ist {e(Zi)}.'],
             f'Der Zinssatz {pz(p)} ist ein Prozentsatz. Die Zinsen sind {pz(p)} von {e(K)} = {e(Zi)}.', 'Prozentsatz oder Betrag in Euro?')


# ---------------- Wer zahlt, wer bekommt? ----------------
FAELLE = [('Du nimmst bei der Bank einen Kredit für ein Fahrrad auf.', 'Du zahlst Zinsen.'),
          ('Du legst dein Geld auf ein Sparkonto mit Zinsen.', 'Du bekommst Zinsen.'),
          ('Du steckst dein Geld in eine Spardose.', 'Es gibt keine Zinsen.'),
          ('Deine Freundin leiht dir Geld und will nur genau den Betrag zurück.', 'Es gibt keine Zinsen.'),
          ('Deine Eltern legen Geld als Festgeld bei einer Bank an.', 'Sie bekommen Zinsen.'),
          ('Ein Ladenbesitzer leiht sich Geld von der Bank für neue Regale.', 'Er zahlt Zinsen.'),
          ('Du kaufst ein Handy auf Raten, und der Händler verlangt Zinsen.', 'Du zahlst Zinsen.'),
          ('Oma legt Geld auf ein Tagesgeldkonto mit Zinsen.', 'Sie bekommt Zinsen.'),
          ('Du versteckst Geld in einer Schublade.', 'Es gibt keine Zinsen.'),
          ('Eine Familie nimmt einen Kredit für ein Auto auf.', 'Sie zahlt Zinsen.')]


def g_rollen(R, s):
    if s in (1, 2):
        f, r = R.choice(FAELLE)
        b = R.randint(2, 50) * 100
        opts = {'Du zahlst Zinsen.', 'Du bekommst Zinsen.', 'Es gibt keine Zinsen.'} if r.startswith(('Du', 'Es')) or 'Du' in f else set()
        wer = r.split()[0]
        if wer in ('Sie', 'Er'):
            opts = {f'{wer} zahlt Zinsen.' if wer == 'Er' else 'Sie zahlen Zinsen.' if 'Eltern' in f else 'Sie zahlt Zinsen.',
                    f'{wer} bekommt Zinsen.' if wer == 'Er' else 'Sie bekommen Zinsen.' if 'Eltern' in f else 'Sie bekommt Zinsen.', 'Es gibt keine Zinsen.'}
        text = f.replace('Geld', f'{e(b)}', 1) if s == 2 else f
        return A(R, f'{text} Wer zahlt oder bekommt Zinsen?', r, sorted(opts - {r}),
                 'Wer fremdes Geld benutzt, zahlt Zinsen. Wer sein Geld verzinst anlegt, bekommt Zinsen. Liegt das Geld nur herum oder ist kein Zins vereinbart, gibt es keine.',
                 'Wer benutzt hier das Geld eines anderen?')
    art = R.choice(['kredit', 'bank'])
    K = R.randint(5, 50) * 100
    p = R.randint(2, 9)
    if art == 'kredit':
        return Z(f'Du leihst dir {e(K)} von der Bank. Nach einem Jahr zahlst du {e(K + K * p // 100)} zurück. Wie viel Zinsen hast du gezahlt?', K * p // 100,
                 f'{K + K * p // 100} - {K}', f'Zurückgezahlt minus geliehen: {e(K + K * p // 100)} − {e(K)} = {e(K * p // 100)}. Die bekommt die Bank.',
                 'Was zahlst du mehr zurück, als du bekommen hast?', einheit='€')
    return A(R, f'Die Bank zahlt dir für dein Sparkonto Zinsen. Warum kann sie das?', 'Sie verleiht dein Geld weiter und verlangt dafür höhere Zinsen.',
             ['Sie druckt das Geld selbst.', 'Das schreibt der Staat so vor.', 'Sie verschenkt Geld an alle Kunden.'],
             'Die Bank benutzt dein Geld, zum Beispiel für Kredite an andere. Dafür zahlt sie dir Zinsen und verlangt von den Kreditnehmern mehr.',
             'Wer benutzt dein Geld, während es auf der Bank liegt?')


# ---------------- Jahreszinsen ----------------
def g_jahreszinsen(R, s):
    if s == 1:
        K, p = R.randint(2, 30) * 100, R.randint(1, 9)
        return Z(f'Berechne die Jahreszinsen für {e(K)} bei {pz(p)} Jahreszinssatz.', Fr(K * p, 100), f'{K} * {p} / 100',
                 f'1 % von {e(K)} sind {e(Fr(K, 100))}. {pz(p)} sind {e(Fr(K, 100))} · {p} = {e(Fr(K * p, 100))}.', 'Rechne zuerst 1 % aus.', einheit='€')
    if s == 2:
        K, p = R.randint(110, 999) * 10, R.randint(2, 8)
        return Z(f'Berechne die Jahreszinsen für {e(K)} bei {pz(p)} Jahreszinssatz.', Fr(K * p, 100), f'{K} * {p} / 100',
                 f'Z = {e(K)} · {p}/100. 1 % sind {e(Fr(K, 100))}, also {p} % = {e(Fr(K * p, 100))}.', 'Z = K · p/100. Erst 1 %, dann mal p.', einheit='€')
    art = R.choice(['stand', 'vergleich', 'fehler'])
    K, p = R.randint(10, 80) * 100, R.randint(2, 6)
    if art == 'stand':
        return Z(f'Jemand legt {e(K)} für ein Jahr zu {pz(p)} an. Wie viel Geld ist nach dem Jahr auf dem Konto?', K + Fr(K * p, 100), f'{K} + {K} * {p} / 100',
                 f'Zinsen: {e(Fr(K * p, 100))}. Kontostand: {e(K)} + {e(Fr(K * p, 100))} = {e(K + Fr(K * p, 100))}.', 'Erst die Zinsen, dann dazuzählen.', einheit='€')
    if art == 'vergleich':
        q = p + R.randint(1, 3)
        return Z(f'Bank A zahlt {pz(p)}, Bank B {pz(q)} Jahreszinsen. Wie viel Euro mehr bringen {e(K)} bei Bank B in einem Jahr?', Fr(K * (q - p), 100),
                 f'{K} * {q} / 100 - {K} * {p} / 100', f'Bank B: {e(Fr(K * q, 100))}, Bank A: {e(Fr(K * p, 100))}. Unterschied: {e(Fr(K * (q - p), 100))}.',
                 'Rechne beide Zinsen aus und ziehe ab.', einheit='€')
    return A(R, f'Jemand rechnet: {pz(p)} von {e(K)} sind {e(p)}. Was stimmt?', f'Falsch: {e(p)} gibt es für je 100 €, also sind es {e(Fr(K * p, 100))}.',
             ['Richtig: p % sind p Euro.', f'Falsch: Es sind {e(K * p)}.', f'Falsch: Es sind {e(Fr(K, p))}.'],
             f'1 % von {e(K)} sind {e(Fr(K, 100))}. Also {pz(p)} = {e(Fr(K * p, 100))}.', 'Für wie viele Euro gibt es je ' + e(p) + '?')


# ---------------- Zinssatz mit Komma ----------------
KOMMA = [Fr(1, 2), Fr(3, 2), Fr(5, 2), Fr(7, 2), Fr(9, 2), Fr(6, 5), Fr(9, 5), Fr(11, 5), Fr(13, 10), Fr(17, 10), Fr(21, 10), Fr(13, 4), Fr(11, 4)]


def g_jahreszinsen_komma(R, s):
    p = R.choice(KOMMA[:5] if s == 1 else KOMMA)
    pd = zt(p)
    K = R.randint(4, 60) * 100 if s < 3 else R.randint(40, 300) * 10
    Zi = K * p / 100
    if not cent(Zi): return g_jahreszinsen_komma(R, s)
    if s in (1, 2):
        return Z(f'Berechne die Jahreszinsen für {e(K)} bei {pd} % Jahreszinssatz.', Zi, f'{K} / 100 * {float(p)}',
                 f'1 % von {e(K)} sind {e(Fr(K, 100))}. Mal {pd}: {e(Fr(K, 100))} · {pd} = {e(Zi)}.', 'Erst 1 % ausrechnen, dann mit der Prozentzahl malnehmen.', einheit='€')
    art = R.choice(['stand', 'fehler'])
    if art == 'stand':
        return Z(f'{e(K)} liegen ein Jahr zu {pd} % auf einem Konto. Wie viel Geld ist danach darauf?', K + Zi, f'{K} + {K} / 100 * {float(p)}',
                 f'Zinsen: {e(Fr(K, 100))} · {pd} = {e(Zi)}. Kontostand: {e(K)} + {e(Zi)} = {e(K + Zi)}.', 'Erst die Zinsen ausrechnen, dann dazuzählen.', einheit='€')
    return A(R, f'Jemand rechnet für {e(K)} bei {pd} %: 1 % = {e(Fr(K, 100))}, dann {e(Fr(K, 100))} · {zt(p / 100)} = {e(Fr(K, 100) * p / 100)}. Was stimmt?',
             f'Falsch: Mit der Prozentzahl {pd} malnehmen, das ergibt {e(Zi)}.', ['Richtig, so rechnet man mit Kommazahlen.', f'Falsch: Es sind {e(K * p)}.'],
             f'Nach dem 1-%-Schritt nimmt man mit {pd} mal, nicht mit {zt(p / 100)}: {e(Fr(K, 100))} · {pd} = {e(Zi)}.', 'Wie oft nimmst du 1 % bei ' + pd + ' %?')


# ---------------- Zinssatz finden ----------------
def g_zinssatz(R, s):
    K = R.randint(2, 50) * 100
    p = Fr(R.randint(1, 8)) if s == 1 else R.choice([Fr(R.randint(1, 8)), Fr(R.randint(3, 15), 2)])
    Zi = K * p / 100
    if not cent(Zi): return g_zinssatz(R, s)
    if s in (1, 2):
        return Z(f'{e(K)} bringen in einem Jahr {e(Zi)} Zinsen. Wie hoch ist der Jahreszinssatz in Prozent?', p, f'{float(Zi)} / {K} * 100',
                 f'Anteil: {e(Zi)} : {e(K)} = {zt(Zi / K)}. Mal 100: {zt(p)} %.', 'p = (Z : K) · 100.', einheit='%')
    art = R.choice(['besser', 'fehler', 'kredit'])
    if art == 'besser':
        K2 = R.randint(2, 50) * 100
        q = Fr(R.randint(1, 8))
        if q == p: q += 1
        Z2 = K2 * q / 100
        bes = 'Angebot A' if p > q else 'Angebot B'
        return A(R, f'Angebot A: {e(K)} bringen {e(Zi)} Zinsen im Jahr. Angebot B: {e(K2)} bringen {e(Z2)}. Welches hat den höheren Zinssatz?', bes,
                 ['Angebot B' if bes == 'Angebot A' else 'Angebot A', 'Beide gleich'],
                 f'A: {e(Zi)} : {e(K)} · 100 = {zt(p)} %. B: {e(Z2)} : {e(K2)} · 100 = {zt(q)} %. Höher: {bes}.', 'Vergleiche die Prozentsätze, nicht die Euro-Beträge.')
    if art == 'kredit':
        return Z(f'Für einen Kredit über {e(K)} zahlt jemand nach einem Jahr {e(Zi)} Zinsen. Welcher Jahreszinssatz in Prozent war vereinbart?', p, f'{float(Zi)} / {K} * 100',
                 f'p = {e(Zi)} : {e(K)} · 100 = {zt(p)} %.', 'Zinsen durch Kapital, dann mal 100.', einheit='%')
    return A(R, f'Jemand rechnet für {e(K)} und {e(Zi)} Zinsen: {g4(K)} : {g4(Zi)} = {zt(round(K / Zi, 1))} %. Was stimmt?',
             f'Falsch herum gerechnet: {e(Zi)} : {e(K)} · 100 = {zt(p)} %.', ['Richtig, Kapital durch Zinsen.', f'Falsch: Es sind {zt(Zi)} %.'],
             f'Der Zinssatz ist der Anteil der Zinsen am Kapital: {g4(Zi)} : {g4(K)} = {zt(Zi / K)}, mal 100 = {zt(p)} %.', 'Zinsen durch Kapital, nicht umgekehrt.')


# ---------------- Kapital finden ----------------
def g_kapital(R, s):
    p = R.randint(2, 8) if s == 1 else R.choice([R.randint(2, 8), R.randint(2, 8)])
    K = R.randint(3, 60) * 100 if s == 1 else R.randint(30, 500) * 10
    Zi = Fr(K * p, 100)
    if not cent(Zi) or (s == 1 and Zi.denominator != 1): return g_kapital(R, s)
    if s in (1, 2):
        return Z(f'Bei {pz(p)} Jahreszinssatz bringt ein Kapital in einem Jahr {e(Zi)} Zinsen. Wie groß ist das Kapital?', K, f'{float(Zi)} * 100 / {p}',
                 f'1 % = {e(Zi)} : {p} = {e(Zi / p)}. 100 % = {e(Zi / p)} · 100 = {e(K)}.', 'Rechne erst aus, wie viel 1 % ist.', einheit='€')
    art = R.choice(['sparziel', 'fehler'])
    if art == 'sparziel':
        return Z(f'Jemand möchte bei {pz(p)} Jahreszinssatz in einem Jahr {e(Zi)} Zinsen bekommen. Wie viel Geld muss er anlegen?', K, f'{float(Zi)} * 100 / {p}',
                 f'1 % = {e(Zi)} : {p} = {e(Zi / p)}. Kapital = 100 % = {e(K)}.', 'K = Z · 100 : p.', einheit='€')
    return A(R, f'Jemand rechnet: {e(Zi)} Zinsen bei {pz(p)}, also Kapital = {e(Zi)} · {p} = {e(Zi * p)}. Was stimmt?',
             f'Falsch: {pz(p)} von {e(Zi * p)} wären nur rund {e(Zi * p * p / 100)}. Richtig sind {e(K)}.',
             ['Richtig, man nimmt mit dem Zinssatz mal.', f'Falsch: Das Kapital ist {e(Zi)}.'],
             f'Rückwärts: 1 % = {e(Zi)} : {p} = {e(Zi / p)}, 100 % = {e(K)}. Probe: {pz(p)} von {e(K)} = {e(Zi)} ✓', 'Probe: Rechne die Zinsen für das angebliche Kapital aus.')


# ---------------- Zinsen für Monate ----------------
def g_monatszinsen(R, s):
    m = R.choice([1, 2, 3, 4, 5, 7, 8, 9, 10, 11]) if s > 1 else R.choice([1, 2, 3, 4, 6])
    K = R.randint(6, 80) * 100 if s == 1 else R.randint(12, 120) * 100
    p = R.randint(2, 6)
    J = Fr(K * p, 100)
    Zi = J * m / 12
    if not cent(Zi): return g_monatszinsen(R, s)
    if s in (1, 2):
        return Z(f'Berechne die Zinsen für {e(K)} bei {pz(p)} Jahreszinssatz für {m} Monat{"e" if m > 1 else ""}.', Zi, f'{K} * {p} / 100 * {m} / 12',
                 f'Jahreszinsen: {e(J)}. {m} Monat{"e" if m > 1 else ""} = {m}/12 Jahr: {e(J)} · {m} : 12 = {e(Zi)}.', 'Erst die Jahreszinsen, dann den Anteil m/12.', einheit='€')
    art = R.choice(['kredit', 'fehler'])
    if art == 'kredit':
        return Z(f'Jemand leiht sich {e(K)} für {m} Monate zu {pz(p)} Jahreszinssatz. Wie viel muss er am Ende insgesamt zurückzahlen?', K + Zi, f'{K} + {K} * {p} / 100 * {m} / 12',
                 f'Jahreszinsen {e(J)}, für {m} Monate {e(Zi)}. Zurück: {e(K)} + {e(Zi)} = {e(K + Zi)}.', 'Zinsen für die Monate ausrechnen und zum Kredit dazuzählen.', einheit='€')
    return A(R, f'Jemand rechnet für {e(K)} zu {pz(p)} und {m} Monate: {m} · {e(J)} = {e(m * J)}. Was stimmt?',
             f'Falsch: {e(J)} gelten für ein ganzes Jahr. Für {m} Monate sind es {e(Zi)}.',
             ['Richtig, man nimmt die Jahreszinsen mal die Monate.', f'Falsch: Es sind {e(J)}.'],
             f'{m} Monate sind {m}/12 eines Jahres: {e(J)} · {m} : 12 = {e(Zi)}. {e(m * J)} wären die Zinsen für {m} Jahre.', 'Der Zinssatz gilt für ein Jahr.')


# ---------------- Halbes Jahr, Vierteljahr ----------------
TEIL = {'ein halbes Jahr': Fr(1, 2), 'ein Vierteljahr': Fr(1, 4), 'ein Dreivierteljahr': Fr(3, 4)}


def g_zeitanteil(R, s):
    name = R.choice(list(TEIL)[:2]) if s == 1 else R.choice(list(TEIL))
    t = TEIL[name]
    K, p = R.randint(4, 80) * 100, R.randint(2, 6)
    J = Fr(K * p, 100)
    Zi = J * t
    if not cent(Zi): return g_zeitanteil(R, s)
    if s in (1, 2):
        return Z(f'{e(K)} liegen {name} zu {pz(p)} Jahreszinssatz auf einem Konto. Wie viel Zinsen gibt es?', Zi, f'{K} * {p} / 100 * {t.numerator} / {t.denominator}',
                 f'Jahreszinsen: {e(J)}. Für {name}: {e(J)} · {t.numerator}/{t.denominator} = {e(Zi)}.', 'Erst die Jahreszinsen, dann den passenden Anteil nehmen.', einheit='€')
    art = R.choice(['monate', 'fehler'])
    if art == 'monate':
        return A(R, f'Wie viele Monate sind {name}?', str(int(12 * t)), [str(x) for x in {3, 6, 9, 4, 2} - {int(12 * t)}][:3],
                 f'{name[0].upper() + name[1:]} sind {t.numerator}/{t.denominator} von 12 Monaten = {int(12 * t)} Monate.', 'Ein Jahr hat 12 Monate.')
    return A(R, f'Jemand rechnet für {e(K)} zu {pz(p)} und ein halbes Jahr: {e(J)} · 6 = {e(J * 6)}. Was stimmt?',
             f'Falsch: Ein halbes Jahr bringt die Hälfte, also {e(J / 2)}.', ['Richtig, ein halbes Jahr hat 6 Monate.', f'Falsch: Es sind {e(J * 2)}.'],
             f'Die Jahreszinsen {e(J)} gelten für 12 Monate. 6 Monate sind die Hälfte: {e(J / 2)}.', 'Mehr oder weniger Zinsen als in einem ganzen Jahr?')


GEN = {'begriffe': g_begriffe, 'rollen': g_rollen, 'jahreszinsen': g_jahreszinsen, 'jahreszinsen_komma': g_jahreszinsen_komma,
       'zinssatz': g_zinssatz, 'kapital': g_kapital, 'monatszinsen': g_monatszinsen, 'zeitanteil': g_zeitanteil}
VERBOT = {'begriffe': ['2 000 €'], 'jahreszinsen': ['800 € bei 4 %'], 'jahreszinsen_komma': ['1 800 € bei 2,5'],
          'zinssatz': ['600 € bringen in einem Jahr 18 €'], 'kapital': ['36 € Zinsen', '4 % Jahreszinssatz bringt ein Kapital in einem Jahr 36 €'],
          'monatszinsen': ['2 400 € bei 5 %'], 'zeitanteil': ['1 600 € liegen ein halbes Jahr zu 3 %']}

if __name__ == '__main__':
    baue(META, ETAPPEN, GEN,
         [('Was sind Zinsen?', ['begriffe', 'rollen']), ('Jahreszinsen', ['jahreszinsen', 'jahreszinsen_komma']),
          ('Rückwärts rechnen', ['zinssatz', 'kapital']), ('Kürzere Zeit', ['monatszinsen', 'zeitanteil'])],
         'Kapital, Jahreszinssatz und Zinsen unterscheiden, Jahreszinsen berechnen (auch mit Komma-Zinssatz), Zinssatz und Kapital rückwärts bestimmen und Zinsen für Teile eines Jahres berechnen.',
         ['Kapital und Zinsen sind Beträge in Euro, der Zinssatz ist ein Prozentsatz.', 'Jahreszinsen: Z = K · p/100 – erst 1 %, dann mal p.',
          'Rückwärts: p = (Z : K) · 100 und K = Z · 100 : p.', 'Für m Monate: Jahreszinsen · m/12.'],
         verbot=VERBOT,
         offen=['Runde 9: Thema stammt aus der Zeit vor dem Bausatz; die bisherigen Aufgaben liegen nur in der Datenbank. Dieser Generator erzeugt neue Aufgaben, '
                'die beim Einspielen mit einheit_abgleichen(…, \'lassen\') dazukommen. Dubletten zu den alten Aufgaben ließen sich hier nicht prüfen, weil diese nicht im Repository liegen.',
                'Modell wie auf den Karten: fester Jahreszinssatz, gleichbleibendes Kapital, keine Zinsen auf Zinsen (Zinseszins ist ein eigenes Thema).'])
