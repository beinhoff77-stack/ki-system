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

# ---------- DURCHSICHT (Neunzehnte Runde, Teil A, Zweig durchsicht-kl6) ----------
# Befund: Stufe 2 war fast überall Stufe 1 mit größeren oder krummen Zahlen, Stufe 3 drei- bis viermal derselbe Fehler-Typ.
# Abhilfe: Wiederholungen ersetzt (c) durch echte Abwandlungen (S2) bzw. andere Gedanken (S3), dazu neue Übungen (d).
from _befunde import Befunde, mit_befunden  # noqa: E402

DS = Befunde('finanzen.zinsen', 19_6_7)
_DZ, _DA, U = DS.Z, DS.A, ('uebung',)

# --- begriffe ---
DS.stufe('begriffe', 'Jemand hat 3 500 € angelegt. Nach einem Jahr sind 3 570 € auf dem Konto. Wie hoch waren die Zinsen?', 2)
DS.ersetze('begriffe', 'Auf einem Sparkonto liegen 4 900 €. Nach einem Jahr gibt die Bank 49 € Zinsen dazu. Wie viel Geld ist dann auf dem Konto?',
           _DZ('Nach einem Jahr sind auf einem Sparkonto 3 090 €. Die Bank hat 90 € Zinsen dazugegeben. Wie viel Geld lag am Anfang auf dem Konto?', 3000, '3090 - 90',
             'Am Ende = Kapital + Zinsen. Also Kapital = 3 090 € − 90 € = 3 000 €.', 'Die Zinsen kamen dazu. Rechne sie wieder weg.', einheit='€'), pools=U)
DS.ersetze('begriffe', 'Auf einem Sparkonto liegen 3 700 €. Nach einem Jahr gibt die Bank 148 € Zinsen dazu. Wie viel Geld ist dann auf dem Konto?',
           _DZ('Auf einem Konto liegen 1 200 €. Im ersten Jahr kommen 24 € Zinsen dazu, im zweiten Jahr 24,48 €. Wie viel Geld ist nach zwei Jahren auf dem Konto?', 1248.48, '1200 + 24 + 24.48',
             'Beide Zinsbeträge kommen zum Kapital dazu: 1 200 € + 24 € + 24,48 € = 1 248,48 €.', 'Zähle das Kapital und beide Zinsbeträge zusammen.', einheit='€'), pools=U)
DS.ersetze('begriffe', 'Jemand sagt: „Bei 4 300 € Kapital bekomme ich 2 % Zinsen.“ Was ist daran ungenau?',
           _DA('Konto A: 2 000 € Kapital, 40 € Zinsen im Jahr. Konto B: 1 000 € Kapital, 30 € Zinsen im Jahr. Welches Konto hat den höheren Zinssatz?',
             'Konto B: 3 % gegen 2 %', ['Konto A, weil es mehr Euro Zinsen gibt', 'Beide haben denselben Zinssatz', 'Das kann man ohne Bank nicht entscheiden'],
             'A: 40 € von 2 000 € sind 2 %. B: 30 € von 1 000 € sind 3 %. Mehr Euro Zinsen heißt nicht höherer Zinssatz.', 'Rechne bei beiden aus, wie viel Prozent die Zinsen vom Kapital sind.'), pools=U)
DS.ersetze('begriffe', 'Jemand sagt: „Bei 2 300 € Kapital bekomme ich 1 % Zinsen.“ Was ist daran ungenau?',
           _DA('Eine Bank zahlt 2 % Zinsen. Nach einem Jahr stehen 5 100 € auf dem Konto. Ein Kind sagt: „Die Zinsen sind 2 % von 5 100 €, also 102 €.“ Was stimmt?',
             'Falsch: Die 2 % gelten für das Kapital am Anfang. 5 100 € sind 102 %, also Kapital 5 000 € und Zinsen 100 €.',
             ['Richtig: 2 % von 5 100 € sind 102 €.', 'Falsch: Die Zinsen sind 2 €.', 'Falsch: Die Zinsen sind 5 100 €.'],
             '5 100 € = Kapital + Zinsen = 102 % des Kapitals. 1 % = 50 €, Kapital 5 000 €, Zinsen 100 €.', 'Worauf bezieht sich der Zinssatz: auf das Geld am Anfang oder am Ende?'), pools=U)
DS.neu('begriffe', 3, _DZ('Ein Kapital bringt in einem Jahr 45 € Zinsen. Wie viel Euro Zinsen bringt das doppelte Kapital beim selben Zinssatz?', 90, '45 * 2',
                        'Gleicher Zinssatz, doppeltes Kapital: Die Zinsen verdoppeln sich. 2 · 45 € = 90 €.', 'Was passiert mit dem Prozentwert, wenn der Grundwert doppelt so groß ist?', einheit='€'))

# --- rollen ---
DS.ersetze('rollen', 'Deine Eltern legen 1 400 € als Festgeld bei einer Bank an. Wer zahlt oder bekommt Zinsen?',
           _DA('Ein Kind leiht sich bei der Bank 400 € und zahlt nach einem Jahr 420 € zurück. Wer bekommt die 20 €?', 'Die Bank',
             ['Das Kind', 'Niemand, das Geld verschwindet', 'Der Staat'], 'Das Kind benutzt das Geld der Bank. Dafür zahlt es 20 € Zinsen an die Bank.', 'Wer hat das Geld hergegeben?'), pools=U)
DS.ersetze('rollen', 'Ein Ladenbesitzer leiht sich 4 600 € von der Bank für neue Regale. Wer zahlt oder bekommt Zinsen?',
           _DA('Bei welchem Angebot zahlst du Zinsen?', 'Handy auf Raten mit 5 % Zinsen', ['Sparbuch mit 1 % Zinsen', 'Festgeld mit 2 % Zinsen', 'Geld in der Spardose'],
             'Nur beim Ratenkauf benutzt du fremdes Geld. Beim Sparbuch und beim Festgeld bekommst du Zinsen, bei der Spardose gibt es keine.', 'Wo benutzt du Geld, das dir nicht gehört?'), pools=U)
for _t in ('Du leihst dir 3 000 € von der Bank. Nach einem Jahr zahlst du 3 270 € zurück. Wie viel Zinsen hast du gezahlt?',
           'Du leihst dir 2 500 € von der Bank. Nach einem Jahr zahlst du 2 700 € zurück. Wie viel Zinsen hast du gezahlt?',
           'Du leihst dir 1 500 € von der Bank. Nach einem Jahr zahlst du 1 635 € zurück. Wie viel Zinsen hast du gezahlt?'):
    DS.stufe('rollen', _t, 2)
DS.neu('rollen', 3, _DZ('Eine Bank zahlt 1 % Zinsen für Spargeld und verlangt 6 % für Kredite. Sie verleiht 10 000 € Spargeld als Kredit. Wie viel Euro bleiben der Bank nach einem Jahr?',
                      500, '10000 * 6 / 100 - 10000 * 1 / 100', 'Sie bekommt 6 % von 10 000 € = 600 € und zahlt 1 % = 100 € an die Sparer. Es bleiben 500 €.',
                      'Rechne aus, was die Bank bekommt und was sie bezahlt.', einheit='€'))
DS.neu('rollen', 3, _DA('Ein Kind sagt: „Bei einem Kredit bekomme ich Zinsen, denn ich bekomme ja Geld.“ Was stimmt?',
                      'Falsch: Wer fremdes Geld benutzt, zahlt Zinsen.', ['Richtig.', 'Falsch: Bei einem Kredit gibt es nie Zinsen.', 'Richtig, aber nur bei großen Beträgen.'],
                      'Beim Kredit benutzt das Kind das Geld der Bank. Dafür zahlt es Zinsen – es bekommt keine.', 'Wem gehört das Geld beim Kredit?'))
DS.neu('rollen', 3, _DZ('Jemand hat 1 000 € auf dem Sparkonto zu 1 % und gleichzeitig 1 000 € Kredit zu 8 %. Wie viel Euro verliert er in einem Jahr durch die Zinsen?',
                      70, '1000 * 8 / 100 - 1000 * 1 / 100', 'Er zahlt 80 € Kreditzinsen und bekommt 10 € Sparzinsen. 80 € − 10 € = 70 € Verlust.',
                      'Vergleiche die Zinsen, die er zahlt, mit denen, die er bekommt.', einheit='€'))

# --- jahreszinsen ---
DS.stufe('jahreszinsen', 'Jemand legt 1 500 € für ein Jahr zu 4 % an. Wie viel Geld ist nach dem Jahr auf dem Konto?', 2)
DS.ersetze('jahreszinsen', 'Berechne die Jahreszinsen für 9 440 € bei 8 % Jahreszinssatz.',
           _DZ('Für einen Kredit über 1 200 € verlangt die Bank 7 % Jahreszinsen. Wie viel muss man nach einem Jahr insgesamt zurückzahlen?', 1284, '1200 + 1200 * 7 / 100',
             '7 % von 1 200 € sind 84 €. Zurück gehen Kredit und Zinsen: 1 200 € + 84 € = 1 284 €.', 'Rechne die Zinsen aus und zähle den Kredit dazu.', einheit='€'), pools=U)
DS.ersetze('jahreszinsen', 'Berechne die Jahreszinsen für 4 520 € bei 6 % Jahreszinssatz.',
           _DZ('Zwei Geschwister legen 800 € und 1 200 € an, beide zu 3 % Jahreszinsen. Wie viel Euro Zinsen bekommen sie zusammen?', 60, '(800 + 1200) * 3 / 100',
             'Geschickt: zusammen 2 000 €, davon 3 % sind 60 €. (Einzeln: 24 € + 36 € = 60 €.)', 'Du kannst die Beträge erst zusammenzählen.', einheit='€'), pools=U)
DS.ersetze('jahreszinsen', 'Berechne die Jahreszinsen für 8 270 € bei 3 % Jahreszinssatz.',
           _DZ('Jemand legt 5 000 € zu 2 % an und hebt die Zinsen jedes Jahr ab. Wie viel Euro Zinsen hat er nach 3 Jahren insgesamt abgehoben?', 300, '3 * 5000 * 2 / 100',
             'Das Kapital bleibt 5 000 €, jedes Jahr gibt es 2 % = 100 €. In 3 Jahren: 300 €.', 'Wie viel Zinsen gibt es in einem Jahr?', einheit='€'), pools=U)
DS.ersetze('jahreszinsen', 'Bank A zahlt 3 %, Bank B 6 % Jahreszinsen. Wie viel Euro mehr bringen 1 700 € bei Bank B in einem Jahr?',
           _DZ('Bei welchem Zinssatz bringen 2 500 € in einem Jahr genauso viele Zinsen wie 5 000 € bei 3 %?', 6, '5000 * 3 / 2500',
             '5 000 € bei 3 % bringen 150 €. Halbes Kapital braucht den doppelten Zinssatz: 150 € von 2 500 € sind 6 %.', 'Rechne zuerst die Zinsen für 5 000 € aus.', einheit='%'), pools=U)
DS.neu('jahreszinsen', 3, _DA('Herr A legt 3 000 € zu 4 % an, Frau B 4 000 € zu 3 %. Wer bekommt mehr Zinsen?', 'Beide gleich viel: 120 €',
                            ['Herr A, weil sein Zinssatz höher ist', 'Frau B, weil ihr Kapital größer ist'],
                            '3 000 · 4/100 = 120 € und 4 000 · 3/100 = 120 €. Kapital und Prozentzahl wurden nur vertauscht.', 'Rechne beide Zinsen aus.'))

# --- jahreszinsen_komma ---
DS.stufe('jahreszinsen_komma', '2 920 € liegen ein Jahr zu 0,5 % auf einem Konto. Wie viel Geld ist danach darauf?', 2)
DS.ersetze('jahreszinsen_komma', 'Berechne die Jahreszinsen für 2 700 € bei 3,5 % Jahreszinssatz.',
           _DZ('Bank A zahlt 2,5 %, Bank B 2,25 % Jahreszinsen. Wie viel Euro mehr bringt Bank A für 4 000 € in einem Jahr?', 10, '4000 * 2.5 / 100 - 4000 * 2.25 / 100',
             'A: 40 € · 2,5 = 100 €. B: 40 € · 2,25 = 90 €. Unterschied 10 € (oder gleich 0,25 % von 4 000 €).', 'Rechne 1 % von 4 000 € aus, dann beide Zinsen.', einheit='€'), pools=U)
DS.ersetze('jahreszinsen_komma', 'Berechne die Jahreszinsen für 2 300 € bei 2,2 % Jahreszinssatz.',
           _DZ('Ein Kredit über 2 000 € kostet 4,5 % Jahreszinsen. Wie viel muss man nach einem Jahr insgesamt zurückzahlen?', 2090, '2000 + 2000 * 4.5 / 100',
             '1 % sind 20 €, 4,5 % sind 90 €. Zurück: 2 000 € + 90 € = 2 090 €.', 'Erst die Zinsen, dann den Kredit dazuzählen.', einheit='€'), pools=U)
DS.ersetze('jahreszinsen_komma', 'Berechne die Jahreszinsen für 4 100 € bei 4,5 % Jahreszinssatz.',
           _DZ('Auf einem Konto liegen 840 € zu 1,5 % Jahreszinsen. Wie viel Geld ist nach einem Jahr darauf?', 852.6, '840 + 840 * 1.5 / 100',
             '1 % sind 8,40 €, 1,5 % sind 12,60 €. 840 € + 12,60 € = 852,60 €.', 'Zinsen ausrechnen und zum Kapital zählen.', einheit='€'), pools=U)
DS.ersetze('jahreszinsen_komma', 'Jemand rechnet für 1 480 € bei 1,3 %: 1 % = 14,80 €, dann 14,80 € · 0,013 = 0,19 €. Was stimmt?',
           _DZ('Bei 2,5 % Jahreszinsen bekommt jemand nach einem Jahr 30 € Zinsen. Wie viel Geld hat er angelegt?', 1200, '30 / 2.5 * 100',
             '2,5 % sind 30 €, also 1 % = 30 € : 2,5 = 12 €. 100 % = 1 200 €.', 'Rechne rückwärts über 1 %.', einheit='€'), pools=U)
DS.ersetze('jahreszinsen_komma', 'Jemand rechnet für 2 570 € bei 2,5 %: 1 % = 25,70 €, dann 25,70 € · 0,025 = 0,64 €. Was stimmt?',
           _DZ('Für 4 000 € gibt es in einem Jahr 70 € Zinsen. Wie hoch ist der Jahreszinssatz?', 1.75, '70 / 4000 * 100',
             '1 % von 4 000 € sind 40 €. 70 € : 40 € = 1,75. Der Zinssatz ist 1,75 %.', 'Wie oft passt 1 % in die Zinsen?', einheit='%'), pools=U)
DS.neu('jahreszinsen_komma', 3, _DA('Ohne genau zu rechnen: Was bringt in einem Jahr die meisten Zinsen?', '1 % von 10 000 €',
                                  ['10 % von 900 €', '2,5 % von 3 000 €', '0,5 % von 15 000 €'],
                                  '1 % von 10 000 € = 100 €; 10 % von 900 € = 90 €; 2,5 % von 3 000 € = 75 €; 0,5 % von 15 000 € = 75 €.', 'Rechne jeweils 1 % im Kopf aus.'))

# --- zinssatz ---
DS.ersetze('zinssatz', '4 400 € bringen in einem Jahr 264 € Zinsen. Wie hoch ist der Jahreszinssatz in Prozent?',
           _DZ('Ein Konto wächst in einem Jahr von 2 500 € auf 2 575 €. Wie hoch ist der Jahreszinssatz?', 3, '(2575 - 2500) / 2500 * 100',
             'Zinsen: 2 575 € − 2 500 € = 75 €. 75 € von 2 500 € sind 3 %.', 'Rechne zuerst die Zinsen in Euro aus.', einheit='%'), pools=U)
DS.ersetze('zinssatz', '3 500 € bringen in einem Jahr 280 € Zinsen. Wie hoch ist der Jahreszinssatz in Prozent?',
           _DZ('Für einen Kredit über 800 € zahlt man nach einem Jahr 856 € zurück. Wie hoch ist der Jahreszinssatz?', 7, '(856 - 800) / 800 * 100',
             'Zinsen: 856 € − 800 € = 56 €. 1 % von 800 € sind 8 €, 56 : 8 = 7. Also 7 %.', 'Wie viel Euro mehr als geliehen wird zurückgezahlt?', einheit='%'), pools=U)
DS.ersetze('zinssatz', '4 700 € bringen in einem Jahr 329 € Zinsen. Wie hoch ist der Jahreszinssatz in Prozent?',
           _DA('Bank A zahlt 60 € Zinsen für 2 000 €, Bank B 75 € Zinsen für 3 000 €. Welche Bank hat den höheren Zinssatz?', 'Bank A: 3 % gegen 2,5 %',
             ['Bank B, weil sie mehr Euro zahlt', 'Beide gleich'], 'A: 60 : 2 000 = 3 %. B: 75 : 3 000 = 2,5 %. Bank A ist besser, obwohl sie weniger Euro zahlt.', 'Rechne beide Zinssätze aus.'), pools=U)
DS.ersetze('zinssatz', 'Jemand rechnet für 2 000 € und 120 € Zinsen: 2 000 : 120 = 16,7 %. Was stimmt?',
           _DZ('1 200 € bringen in einem halben Jahr 18 € Zinsen. Wie hoch ist der Jahreszinssatz?', 3, '18 * 2 / 1200 * 100',
             'In einem ganzen Jahr wären es 36 €. 36 € von 1 200 € sind 3 %.', 'Der Jahreszinssatz gilt für ein ganzes Jahr.', einheit='%'), pools=U)
DS.ersetze('zinssatz', 'Jemand rechnet für 1 400 € und 42 € Zinsen: 1 400 : 42 = 33,3 %. Was stimmt?',
           _DZ('Ein Konto bringt 2 % Zinsen im Jahr. Die Zinsen werden jedes Jahr abgehoben. Nach wie vielen Jahren sind sie zusammen so viel wie das Kapital?', 50, '100 / 2',
             'Jedes Jahr gibt es 2 % des Kapitals. 100 % sind erreicht nach 100 : 2 = 50 Jahren.', 'Wie viele Male 2 % ergeben 100 %?'), pools=U)
DS.ersetze('zinssatz', 'Jemand rechnet für 4 900 € und 392 € Zinsen: 4 900 : 392 = 12,5 %. Was stimmt?',
           _DZ('Für 5 000 € gibt es in einem Jahr 150 € Zinsen. Eine andere Bank zahlt 1 Prozentpunkt mehr. Wie viel Euro Zinsen gäbe es dort?', 200, '5000 * (150 / 5000 * 100 + 1) / 100',
             'Zinssatz hier: 150 € von 5 000 € = 3 %. Andere Bank: 4 %, also 200 €.', 'Bestimme erst den Zinssatz.', einheit='€'), pools=U)

# --- kapital ---
DS.stufe('kapital', 'Jemand möchte bei 2 % Jahreszinssatz in einem Jahr 42,60 € Zinsen bekommen. Wie viel Geld muss er anlegen?', 2)
DS.ersetze('kapital', 'Bei 3 % Jahreszinssatz bringt ein Kapital in einem Jahr 124,20 € Zinsen. Wie groß ist das Kapital?',
           _DZ('Für einen Kredit zahlt man bei 5 % Jahreszinsen 45 € Zinsen im Jahr. Wie hoch war der Kredit?', 900, '45 / 5 * 100',
             '5 % sind 45 €, 1 % sind 9 €, 100 % sind 900 €.', 'Rechne über 1 %.', einheit='€'), pools=U)
DS.ersetze('kapital', 'Bei 4 % Jahreszinssatz bringt ein Kapital in einem Jahr 38,80 € Zinsen. Wie groß ist das Kapital?',
           _DZ('Bei 2,5 % Jahreszinssatz gibt es in einem Jahr 50 € Zinsen. Wie groß ist das Kapital?', 2000, '50 / 2.5 * 100',
             '1 % sind 50 € : 2,5 = 20 €. 100 % sind 2 000 €.', 'Teile die Zinsen durch 2,5, dann mal 100.', einheit='€'), pools=U)
DS.ersetze('kapital', 'Jemand rechnet: 111,30 € Zinsen bei 3 %, also Kapital = 111,30 € · 3 = 333,90 €. Was stimmt?',
           _DZ('Nach einem Jahr mit 4 % Zinsen sind 1 040 € auf dem Konto. Wie viel Geld wurde eingezahlt?', 1000, '1040 / 104 * 100',
             'Kapital + 4 % sind 104 % = 1 040 €. 1 % = 10 €, 100 % = 1 000 €.', 'Auf dem Konto liegen Kapital und Zinsen zusammen. Wie viel Prozent sind das?', einheit='€'), pools=U)
DS.ersetze('kapital', 'Jemand rechnet: 32,40 € Zinsen bei 2 %, also Kapital = 32,40 € · 2 = 64,80 €. Was stimmt?',
           _DZ('Bank A zahlt 2 %, Bank B 5 %. Jemand will 100 € Zinsen im Jahr. Wie viel Euro weniger muss er bei Bank B anlegen als bei Bank A?', 3000, '100 / 2 * 100 - 100 / 5 * 100',
             'Bank A: 100 € sind 2 %, Kapital 5 000 €. Bank B: 100 € sind 5 %, Kapital 2 000 €. Unterschied 3 000 €.', 'Bestimme das Kapital für beide Banken.', einheit='€'), pools=U)
DS.neu('kapital', 3, _DZ('Ein Kapital bringt bei 4 % Jahreszinssatz in einem halben Jahr 30 € Zinsen. Wie groß ist das Kapital?', 1500, '30 * 2 / 4 * 100',
                       'Ein ganzes Jahr brächte 60 €. 4 % sind 60 €, 1 % = 15 €, 100 % = 1 500 €.', 'Rechne erst die Zinsen für ein ganzes Jahr aus.', einheit='€'))

# --- monatszinsen ---
for _t in ('Jemand leiht sich 6 100 € für 2 Monate zu 3 % Jahreszinssatz. Wie viel muss er am Ende insgesamt zurückzahlen?',
           'Jemand leiht sich 10 500 € für 4 Monate zu 5 % Jahreszinssatz. Wie viel muss er am Ende insgesamt zurückzahlen?'):
    DS.stufe('monatszinsen', _t, 2)
DS.ersetze('monatszinsen', 'Berechne die Zinsen für 9 800 € bei 6 % Jahreszinssatz für 4 Monate.',
           _DZ('Vom 1. März bis zum 1. September liegen 2 400 € zu 3 % Jahreszinssatz auf einem Konto. Wie viel Euro Zinsen gibt es?', 36, '2400 * 3 / 100 * 6 / 12',
             'März bis September sind 6 Monate. Jahreszinsen 72 €, davon 6/12: 36 €.', 'Zähle zuerst die Monate.', einheit='€'), pools=U)
DS.ersetze('monatszinsen', 'Jemand rechnet für 1 700 € zu 6 % und 7 Monate: 7 · 102 € = 714 €. Was stimmt?',
           _DZ('Wie viele Monate muss man 6 000 € zu 4 % Jahreszinssatz anlegen, um 60 € Zinsen zu bekommen?', 3, '60 / (6000 * 4 / 100) * 12',
             'Ein Jahr bringt 240 €. 60 € sind ein Viertel davon, also 3 Monate.', 'Rechne zuerst die Zinsen für ein ganzes Jahr aus.'), pools=U)
DS.neu('monatszinsen', 3, _DA('Was bringt mehr Zinsen: 3 000 € für 8 Monate zu 3 % oder 3 000 € für 1 Jahr zu 2 %?', 'Beide gleich viel: 60 €',
                            ['8 Monate zu 3 %, weil 3 % mehr ist', '1 Jahr zu 2 %, weil die Zeit länger ist'],
                            '8 Monate zu 3 %: 90 € · 8/12 = 60 €. 1 Jahr zu 2 %: 60 €.', 'Rechne beide Zinsen aus.'))
DS.neu('monatszinsen', 3, _DZ('Jemand bekommt für 4 Monate 20 € Zinsen. Wie viel Euro Zinsen bekäme er für ein ganzes Jahr?', 60, '20 * 12 / 4',
                            'Ein Jahr hat 3-mal 4 Monate. 3 · 20 € = 60 €.', 'Wie oft passen 4 Monate in ein Jahr?', einheit='€'))

# --- zeitanteil ---
DS.stufe('zeitanteil', 'Wie viele Monate sind ein Vierteljahr?', 1)
DS.ersetze('zeitanteil', '5 800 € liegen ein halbes Jahr zu 2 % Jahreszinssatz auf einem Konto. Wie viel Zinsen gibt es?',
           _DZ('1 600 € liegen ein Vierteljahr zu 3 % Jahreszinssatz auf einem Konto. Wie viel Geld ist danach auf dem Konto?', 1612, '1600 + 1600 * 3 / 100 / 4',
             'Jahreszinsen 48 €, ein Viertel davon 12 €. Auf dem Konto: 1 600 € + 12 € = 1 612 €.', 'Erst die Zinsen, dann zum Kapital zählen.', einheit='€'), pools=U)
DS.ersetze('zeitanteil', '3 400 € liegen ein halbes Jahr zu 2 % Jahreszinssatz auf einem Konto. Wie viel Zinsen gibt es?',
           _DZ('Ein Kredit über 2 000 € zu 6 % Jahreszinssatz wird nach einem halben Jahr zurückgezahlt. Wie viel muss man insgesamt zurückzahlen?', 2060, '2000 + 2000 * 6 / 100 / 2',
             'Jahreszinsen 120 €, für ein halbes Jahr 60 €. Zurück: 2 060 €.', 'Halbe Zeit, halbe Zinsen.', einheit='€'), pools=U)
DS.ersetze('zeitanteil', 'Jemand rechnet für 6 000 € zu 2 % und ein halbes Jahr: 120 € · 6 = 720 €. Was stimmt?',
           _DZ('Ein Kapital bringt bei 2 % in einem halben Jahr 25 € Zinsen. Wie viel Euro Zinsen bringt es in einem Vierteljahr?', 12.5, '25 / 2',
             'Ein Vierteljahr ist die Hälfte eines halben Jahres. 25 € : 2 = 12,50 €.', 'Vergleiche die beiden Zeiten miteinander.', einheit='€'), pools=U)
DS.ersetze('zeitanteil', 'Jemand rechnet für 4 500 € zu 4 % und ein halbes Jahr: 180 € · 6 = 1 080 €. Was stimmt?',
           _DA('Angebot A: ein halbes Jahr zu 4 %. Angebot B: ein ganzes Jahr zu 2 %. Bei welchem gibt es für 1 000 € mehr Zinsen?', 'Beide gleich viel: 20 €',
             ['A, weil 4 % mehr sind', 'B, weil die Zeit länger ist'], 'A: 40 € für ein Jahr, halbes Jahr 20 €. B: 2 % von 1 000 € = 20 €.', 'Rechne beide Zinsen aus.'), pools=U)
DS.neu('zeitanteil', 3, _DA('2 000 € liegen zu 3 % Jahreszinssatz auf einem Konto. Wie lange muss das Geld liegen, damit es 15 € Zinsen gibt?', 'ein Vierteljahr',
                          ['ein halbes Jahr', 'ein ganzes Jahr', 'einen Monat'], 'Ein Jahr bringt 60 €. 15 € sind ein Viertel davon, also ein Vierteljahr.', 'Rechne zuerst die Jahreszinsen aus.'))

DS.fuer_sebastian('finanzen.zinsen überschneidet sich mit bruch.prozent / zinsen (Jahres-, Monats-, Kapital-Aufgaben in beiden Flügen).')
baue = mit_befunden(baue, DS)
# ---- DURCHSICHT ENDE ----


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
