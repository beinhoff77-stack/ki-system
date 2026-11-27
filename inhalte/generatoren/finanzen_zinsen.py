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

META = {'thema_schluessel': 'finanzen.zinsen', 'thema_id': 71, 'block_id': 52, 'klasse': {'gym_by': 6, 'rs_by': 7, 'ib_myp': 4}}
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

DS.fuer_nutzer('finanzen.zinsen überschneidet sich mit bruch.prozent / zinsen (Jahres-, Monats-, Kapital-Aufgaben in beiden Flügen).')
baue = mit_befunden(baue, DS)
# ---- DURCHSICHT ENDE ----

# ---------- STUFEN (Zwanzigste Runde, Zweig stufen-kl6) ----------
from _stufen_kl6 import Stufen, stufen_datei  # noqa: E402

ST = Stufen('finanzen.zinsen', 20_6_7)
SZ, SA, SN, SK, STB = ST.Z, ST.A, ST.neu, ST.knobel, ST.typ_bau
E = '€'

lz = 'begriffe'
ST.leiter(lz, 'Kapital, Zinssatz und Zinsen in einem Text erkennen und den Kontostand nach einem Jahr angeben.', 'Kontostand vorwärts und rückwärts, zwei Jahre, Zinsen aus der Differenz.',
          'Ungenaue Sprache begründen, Zinssätze vergleichen, Grundwert-Falle deuten, doppeltes Kapital, Zinsen aus dem Endstand rückwärts, Bruch als Zinssatz.')
STB(lz, 2, 'Auf einem Konto liegen 1 200', 'mehrschritt'); STB(lz, 2, 'Jemand hat 3 500', 'umkehr')
STB(lz, 3, 'Jemand sagt', 'begruenden'); STB(lz, 3, 'Eine Bank zahlt 2', 'fehler')
SN(lz, SZ('einkleidung', 'Auf einem Sparbuch lagen 600 €. Am Jahresende schreibt die Bank 12 € Zinsen gut. Wie viel Geld ist jetzt darauf?', 612, '600 + 12', '600 € + 12 € = 612 €.', 'Die Zinsen kommen zum Kapital dazu.', einheit=E))
SN(lz, SZ('direkt', 'Auf einem Sparbuch liegen 1 000 €. Nach einem Jahr kommen 20 € Zinsen dazu. Wie viel Geld ist dann darauf?', 1020, '1000 + 20', '1 000 € + 20 € = 1 020 €.', 'Kapital plus Zinsen.', einheit=E))
SN(lz, SA('erkennen', 'Welche Angabe ist ein Zinssatz?', '2,5 %', ['2,50 €', '250 €'], 'Der Zinssatz ist ein Prozentsatz. Kapital und Zinsen sind Beträge in Euro.', 'Ein Zinssatz hat das Zeichen %.'))
SN(lz, SZ('rueckwaerts', 'Nach einem Jahr mit 2 % Zinsen sind 3 060 € auf dem Konto. Wie viel Euro Zinsen gab es?', 60, '3060 - 3060 / 1.02', '3 060 € sind 102 % des Kapitals, also Kapital 3 000 € und Zinsen 60 €.', 'Wie viel Prozent sind 3 060 €?', einheit=E))
SN(lz, SZ('parameter', 'Bei welchem Zinssatz bringt jedes Kapital in einem Jahr genau ein Zwanzigstel des Kapitals als Zinsen?', 5, '100 / 20', '1/20 = 5/100 = 5 %.', 'Schreibe 1/20 als Prozent.', einheit='%'))
SN(lz, SA('pruefung', 'Auf einem Konto liegen 4 000 €, die Bank zahlt 3 % im Jahr, am Jahresende kommen 120 € dazu. Welche Zuordnung stimmt?', 'Kapital 4 000 €, Zinssatz 3 %, Zinsen 120 €',
          ['Kapital 120 €, Zinssatz 4 000 €, Zinsen 3 %', 'Kapital 4 000 €, Zinssatz 120 €, Zinsen 3 %'], 'Das eingezahlte Geld ist das Kapital, der Prozentsatz der Zinssatz, der Betrag, der dazukommt, die Zinsen.', 'Welche Angabe ist ein Prozentsatz?'))
SN(lz, SZ('verknuepfen', 'Die Zinsen eines Jahres sind 1/40 des Kapitals. Wie hoch ist der Zinssatz?', 2.5, '100 / 40', '1/40 = 2,5/100 = 2,5 %.', 'Erweitere 1/40 auf den Nenner 100.', einheit='%'))
SK(lz, SZ('knobel', 'Zwei Geschwister haben zusammen 3 000 € auf zwei Konten zu 2 % und zu 3 %. Zusammen bekommen sie 75 € Zinsen. Wie viel Euro liegen auf dem 3-%-Konto?', 1500, '(75 - 3000 * 0.02) / 0.01',
          'Lägen alle 3 000 € zu 2 %, gäbe es 60 €. Die 15 € mehr kommen vom 1 % Unterschied auf dem 3-%-Konto: 15 € sind 1 % von 1 500 €.', 'Rechne zuerst so, als läge alles zu 2 %.', einheit=E))
SK(lz, SZ('knobel', 'Ein Konto bringt 50 € Zinsen im Jahr. Wäre der Zinssatz um 1 Prozentpunkt höher, wären es 75 €. Wie groß ist das Kapital?', 2500, '25 * 100',
          '1 Prozentpunkt mehr bringt 25 € mehr. 1 % des Kapitals sind also 25 €, das Kapital 2 500 € (und der Zinssatz 2 %).', 'Wie viel Euro ist 1 % des Kapitals?', einheit=E))

lz = 'rollen'
ST.leiter(lz, 'Erkennen, wer in einer Situation Zinsen zahlt oder bekommt.', 'Situationen mit Freunden, Krediten und Angeboten beurteilen, Zinsen aus Rückzahlung.',
          'Warum Banken zahlen können, Zinsspanne, Fehlvorstellung beim Kredit, Sparen und Kredit gleichzeitig, rückwärts zum Kredit, Ratenkauf, Prüfungsfrage.')
STB(lz, 2, 'Du leihst dir', 'umkehr'); STB(lz, 3, 'Die Bank zahlt dir', 'begruenden'); STB(lz, 3, 'Ein Kind sagt', 'fehler'); STB(lz, 3, 'Jemand hat 1 000', 'verknuepfen')
SN(lz, SZ('direkt', 'Du leihst dir 200 € und zahlst 210 € zurück. Wie viel Euro Zinsen zahlst du?', 10, '210 - 200', '210 € − 200 € = 10 € Zinsen.', 'Was zahlst du mehr zurück?', einheit=E))
SN(lz, SZ('rueckwaerts', 'Jemand zahlt für einen Kredit nach einem Jahr 5 % Zinsen und insgesamt 2 100 € zurück. Wie hoch war der Kredit?', 2000, '2100 / 1.05', '2 100 € sind 105 % des Kredits, also 1 % = 20 € und der Kredit 2 000 €.', 'Wie viel Prozent des Kredits sind 2 100 €?', einheit=E))
SN(lz, SZ('parameter', 'Eine Bank zahlt Sparern 1 % und verlangt für Kredite p %. Verleiht sie 10 000 € Spargeld, sollen ihr 300 € bleiben. Wie groß ist p?', 4, '(300 + 100) / 100',
          'An die Sparer gehen 100 €. Die Bank braucht 300 € + 100 € = 400 € Kreditzinsen, das sind 4 % von 10 000 €.', 'Wie viel muss die Bank insgesamt einnehmen?', einheit='%'))
SN(lz, SA('pruefung', 'Ein Kind legt Geld aufs Sparbuch, ein Vater nimmt einen Kredit auf. Was stimmt?', 'Das Kind bekommt Zinsen, der Vater zahlt Zinsen.', ['Das Kind zahlt, der Vater bekommt Zinsen.', 'Beide bekommen Zinsen.', 'Beide zahlen Zinsen.'],
          'Die Bank benutzt das Geld des Kindes (sie zahlt), der Vater benutzt das Geld der Bank (er zahlt).', 'Wer benutzt wessen Geld?'))
SN(lz, SZ('transfer', 'Ein Fahrrad kostet 600 €. Beim Ratenkauf zahlt man 12 Raten zu je 53 €. Wie viel Euro kostet der Ratenkauf mehr?', 36, '12 * 53 - 600', '12 · 53 € = 636 €. 636 € − 600 € = 36 € – das sind die Zinsen.', 'Rechne alle Raten zusammen.', einheit=E))
SK(lz, SZ('knobel', 'Ein Kredit über 1 000 € kostet 10 % Zinsen im Jahr. Nach einem Jahr zahlt man 500 € zurück. Der Rest wird im zweiten Jahr wieder mit 10 % verzinst. Wie viel schuldet man nach zwei Jahren?', 660, '(1000 * 1.1 - 500) * 1.1',
          'Nach einem Jahr: 1 100 €. Nach der Zahlung: 600 €. Im zweiten Jahr 10 % dazu: 660 €.', 'Rechne Jahr für Jahr.', einheit=E))
SK(lz, SZ('knobel', 'Ein Kind möchte in einem Jahr genau 300 € haben. Das Sparbuch zahlt 2 %. Wie viel muss es heute einzahlen? Runde auf Cent.', 294.12, 'round(300 / 1.02, 2)',
          '300 € sollen 102 % sein. 100 % = 300 € : 102 · 100 = 30 000 € : 102 ≈ 294,118 €, auf Cent gerundet 294,12 €. (Nicht 300 € − 6 €, denn die 2 % beziehen sich auf den kleineren Betrag.)', 'Wie viel Prozent des eingezahlten Geldes sind 300 €?', einheit=E))

lz = 'jahreszinsen'
ST.leiter(lz, 'Jahreszinsen mit Z = K · p/100 berechnen; die Formel erkennen.', 'Guthaben und Rückzahlung, zusammengelegtes Kapital, mehrere Jahre mit Abheben, Zinssatz aus Zinsen.',
          'Fehler deuten, Zinssatz für gleiche Zinsen, Vertauschen von Kapital und Zinssatz begründen, rückwärts zum Kapital, Bruchteile verknüpfen, Hochrechnen, Prüfungsaufgabe.')
STB(lz, 2, 'Berechne die Jahreszinsen', 'direkt', neu_s=1); STB(lz, 2, 'Zwei Geschwister', 'mehrschritt'); STB(lz, 2, 'Jemand legt 5', 'mehrschritt')
STB(lz, 3, 'Bank A', 'mehrschritt', neu_s=2); STB(lz, 3, 'Bei welchem Zinssatz', 'parameter'); STB(lz, 3, 'Herr A', 'begruenden')
SN(lz, SA('erkennen', 'Welche Formel gibt die Jahreszinsen Z aus Kapital K und Zinssatz p?', 'Z = K · p/100', ['Z = K : p', 'Z = K + p'], 'Zinsen sind p Prozent vom Kapital: K · p/100.', 'Zinsen sind ein Prozentwert.'))
SN(lz, SZ('direkt', 'Wie viel Euro Zinsen bringen 600 € bei 3 % in einem Jahr?', 18, '600 * 3 / 100', '1 % = 6 €, 3 % = 18 €.', 'Rechne erst 1 % aus.', einheit=E))
SN(lz, SZ('umkehr', 'Welcher Zinssatz bringt für 800 € in einem Jahr genau 24 € Zinsen?', 3, '24 / 800 * 100', '1 % von 800 € sind 8 €. 24 € sind 3 %.', 'Wie viel ist 1 %?', einheit='%'))
SN(lz, SZ('rueckwaerts', 'Nach einem Jahr zu 5 % sind 2 625 € auf dem Konto. Wie viel wurde eingezahlt?', 2500, '2625 / 1.05', '2 625 € sind 105 %. 1 % = 25 €, eingezahlt 2 500 €.', 'Wie viel Prozent sind 2 625 €?', einheit=E))
SN(lz, SZ('verknuepfen', 'Von 2 400 € Erspartem liegen 3/4 zu 2 %, der Rest zu 4 %. Wie viel Euro Zinsen gibt es zusammen in einem Jahr?', 60, '1800 * 2 / 100 + 600 * 4 / 100', '3/4 = 1 800 € bringen 36 €, 600 € bringen 24 €. Zusammen 60 €.', 'Teile zuerst das Geld auf.', einheit=E))
SN(lz, SZ('pruefung', 'Ein Kind hat 1 200 € gespart. Es legt 2/3 davon ein Jahr lang zu 3 % an, den Rest behält es. Wie viel Geld hat es nach dem Jahr insgesamt?', 1224, '800 * 1.03 + 400',
          'Angelegt: 800 €, Zinsen 24 €. Zusammen 800 € + 24 € + 400 € = 1 224 €.', 'Berechne zuerst den angelegten Betrag.', einheit=E))
SN(lz, SZ('transfer', 'Bei einer Bank bringen 4 000 € in einem Jahr 120 € Zinsen. Wie viel Euro Zinsen brächten 6 500 € bei derselben Bank?', 195, '6500 * 120 / 4000', 'Zinssatz: 120 : 4 000 = 3 %. 3 % von 6 500 € = 195 €.', 'Bestimme zuerst den Zinssatz.', einheit=E))
SN(lz, SA('begruenden', 'Stimmt die Aussage? „Bei 1 % Zinsen bekommt man für je 100 € einen Euro im Jahr.“', 'Ja: 1 % heißt 1 von 100.', ['Nein, 10 €.', 'Nein, 1 % sind immer 1 € – egal wie viel Kapital.'], '1 % = 1/100. Je 100 € gibt es 1 €.', 'Was heißt „Prozent“?'))
SK(lz, SZ('knobel', 'Ein Kapital bringt bei 3 % in einem Jahr 36 € mehr Zinsen als bei 2 %. Wie groß ist das Kapital?', 3600, '36 * 100', 'Der Unterschied ist 1 % des Kapitals. 1 % sind 36 €, also 3 600 €.', 'Was bedeutet der Unterschied zwischen 3 % und 2 %?', einheit=E))
SK(lz, SZ('knobel', 'Lea legt 1 000 € zu 2 % an, Tom 900 € zu 3 %. Nach einem Jahr: Um wie viel Euro hat Lea mehr auf dem Konto als Tom?', 93, '1000 * 1.02 - 900 * 1.03',
          'Lea: 1 020 €. Tom: 927 €. Tom bekommt zwar mehr Zinsen (27 € gegen 20 €), aber Lea hatte 100 € mehr Kapital. Lea hat 93 € mehr.', 'Vergleiche die Endstände, nicht nur die Zinsen.', einheit=E))

lz = 'jahreszinsen_komma'
ST.leiter(lz, 'Jahreszinsen bei Zinssätzen mit Komma berechnen; den Zinssatz als Rechenzahl erkennen.', 'Bankvergleich, Kredit, Guthaben, Zinssatz mit Komma aus Zinsen bestimmen.',
          'Fehler beim Malnehmen mit dem Prozentsatz deuten, Kapital rückwärts, Überschlag begründen, gleicher Ertrag, Gebühren, Zinssatzerhöhung, kleines Kapital für 1 €.')
STB(lz, 2, 'Berechne die Jahreszinsen', 'direkt', neu_s=1); STB(lz, 2, 'Bank A', 'mehrschritt')
STB(lz, 3, 'Bei 2,5 %', 'rueckwaerts'); STB(lz, 3, 'Für 4 000 €', 'umkehr', neu_s=2); STB(lz, 3, 'Ohne genau', 'begruenden')
SN(lz, SA('erkennen', 'Mit welcher Zahl nimmst du das Kapital mal, um 2,5 % Zinsen zu erhalten?', '0,025', ['2,5', '0,25', '25'], '2,5 % = 2,5/100 = 0,025.', 'Prozent heißt „durch 100“.'))
SN(lz, SZ('direkt', 'Wie viel Euro Zinsen bringen 2 000 € bei 1,5 % in einem Jahr?', 30, '2000 * 1.5 / 100', '1 % = 20 €, 1,5 % = 30 €.', 'Rechne erst 1 %, dann mal 1,5.', einheit=E))
SN(lz, SZ('umkehr', 'Welcher Zinssatz bringt für 400 € in einem Jahr genau 9 € Zinsen?', 2.25, '9 / 400 * 100', '1 % = 4 €. 9 € : 4 € = 2,25, also 2,25 %.', 'Wie viel ist 1 % von 400 €?', einheit='%'))
SN(lz, SZ('parameter', 'Für welchen Zinssatz bringen 800 € genauso viel Zinsen wie 600 € bei 2 %?', 1.5, '600 * 2 / 800', '600 € bei 2 % bringen 12 €. 12 € von 800 € sind 1,5 %.', 'Rechne zuerst die Zinsen für 600 € aus.', einheit='%'))
SN(lz, SZ('verknuepfen', 'Ein Kind bekommt 2,5 % Zinsen auf 1 600 € und gibt davon 3/4 aus. Wie viel Euro der Zinsen bleiben übrig?', 10, '1600 * 2.5 / 100 / 4', 'Zinsen: 40 €. Übrig ist 1/4 davon: 10 €.', 'Berechne zuerst die Zinsen.', einheit=E))
SN(lz, SZ('pruefung', 'Bank A zahlt 2,25 %, verlangt aber 5 € Gebühr im Jahr. Bank B zahlt 1,75 % ohne Gebühr. Wie viel Euro mehr bekommt man für 1 600 € bei der besseren Bank?', 3, '(1600 * 2.25 / 100 - 5) - 1600 * 1.75 / 100',
          'A: 36 € − 5 € = 31 €. B: 28 €. A ist besser, um 3 €.', 'Ziehe bei A die Gebühr ab.', einheit=E))
SN(lz, SZ('transfer', 'Eine Bank erhöht den Zinssatz von 1,2 % auf 1,5 %. Wie viel Euro mehr Zinsen gibt es dadurch für 5 000 € im Jahr?', 15, '5000 * 0.3 / 100', 'Der Unterschied sind 0,3 Prozentpunkte. 1 % = 50 €, 0,3 % = 15 €.', 'Rechne nur mit dem Unterschied.', einheit=E))
SN(lz, SZ('transfer', 'Wie viel Euro muss man zu 0,5 % anlegen, um im Jahr genau 1 € Zinsen zu bekommen?', 200, '1 / 0.5 * 100', '0,5 % sind 1 €, also 1 % = 2 € und 100 % = 200 €.', 'Wie viel Euro wären 1 %?', einheit=E))
SK(lz, SZ('knobel', 'Bank A zahlt 1,8 % ohne Gebühr, Bank B 2,3 % bei 10 € Gebühr im Jahr. Ab welchem Kapital (in vollen 100 €) bekommt man bei Bank B mehr?', 2100, '2100',
          'B bringt 0,5 Prozentpunkte mehr, muss aber 10 € Gebühr ausgleichen. 0,5 % = 10 € gilt bei 2 000 €. Erst darüber lohnt sich B: ab 2 100 €.', 'Wann gleichen die 0,5 Prozentpunkte genau die Gebühr aus?', einheit=E))
SK(lz, SZ('knobel', 'Ein Kapital ist in einem Jahr mit 2,5 % Zinsen auf 820 € gewachsen. Wie groß war es am Anfang?', 800, '820 / 1.025', 'Am Ende sind Kapital und Zinsen zusammen 102,5 % des Anfangskapitals. 820 € : 102,5 = 8 € sind 1 %, also war das Kapital 800 € (Probe: 2,5 % von 800 € sind 20 €).', 'Wie viel Prozent des Anfangskapitals sind 820 €?', einheit=E))

lz = 'zinssatz'
ST.leiter(lz, 'Zinssatz = Zinsen durch Kapital mal 100 bei glatten Zahlen; die Rechnung erkennen.', 'Zinssatz aus Kontostand oder Rückzahlung, Banken vergleichen, Zinsen zu anderem Kapital.',
          'Fehler deuten, halbes Jahr, Zinsen ohne Zinseszins über Jahre, Prozentpunkte, Aussage begründen, rückwärts über zwei Jahre, Bruchteile, Prüfungsaufgabe.')
STB(lz, 2, '1 700', 'direkt', neu_s=1); STB(lz, 2, 'Ein Konto wächst', 'mehrschritt'); STB(lz, 2, 'Bank A', 'mehrschritt')
STB(lz, 3, 'Für 5 000', 'verknuepfen')
SN(lz, SZ('einkleidung', 'Ein Sparbuch mit 900 € bringt im Jahr 13,50 € Zinsen. Wie hoch ist der Zinssatz?', 1.5, '13.5 / 900 * 100', '1 % von 900 € sind 9 €. 13,50 € : 9 € = 1,5, also 1,5 %.', 'Wie viel ist 1 % von 900 €?', einheit='%'))
SN(lz, SA('erkennen', 'Wie berechnest du den Zinssatz aus Zinsen und Kapital?', 'Zinsen : Kapital · 100', ['Kapital : Zinsen · 100', 'Zinsen · Kapital'], 'Der Zinssatz ist der Anteil der Zinsen am Kapital in Prozent.', 'Was steht beim Anteil oben?'))
SN(lz, SZ('direkt', 'Für 100 € gibt es im Jahr 3 € Zinsen. Wie hoch ist der Zinssatz?', 3, '3 / 100 * 100', '3 € von 100 € sind 3 %.', 'Prozent heißt „von hundert“.', einheit='%'))
SN(lz, SZ('umkehr', 'Ein Kapital von 2 500 € bringt 3 % Zinsen. Welches Kapital bringt bei diesem Zinssatz 45 € Zinsen?', 1500, '45 / 3 * 100', '3 % sind 45 €, also 1 % = 15 € und das Kapital 1 500 €.', 'Der Zinssatz bleibt gleich – gesucht ist das Kapital.', einheit=E))
SN(lz, SA('begruenden', 'Stimmt die Aussage? „Eine Bank, die mehr Euro Zinsen zahlt, hat auch den höheren Zinssatz.“', 'Nein, das hängt vom Kapital ab.', ['Ja, immer.', 'Ja, außer bei Krediten.'],
          'Beispiel: 60 € für 2 000 € sind 3 %, 75 € für 3 000 € nur 2,5 %.', 'Suche ein Gegenbeispiel mit verschiedenem Kapital.'))
SN(lz, SZ('rueckwaerts', 'Jemand hebt die Zinsen jedes Jahr ab. Nach zwei Jahren hat er für 1 600 € insgesamt 96 € Zinsen bekommen. Wie hoch war der Zinssatz?', 3, '96 / 2 / 1600 * 100', 'Ein Jahr: 48 €. 48 € von 1 600 € = 3 %.', 'Wie viel gab es in einem Jahr?', einheit='%'))
SN(lz, SZ('parameter', 'Bei welchem Zinssatz sind die Zinsen eines Jahres genau ein Viertel von 10 % des Kapitals?', 2.5, '10 / 4', 'Ein Viertel von 10 % ist 2,5 %.', 'Was ist ein Viertel von 10?', einheit='%'))
SN(lz, SZ('pruefung', 'Herr A legt 2 400 € an und erhält 60 € Zinsen. Frau B legt 3 200 € an und erhält 72 € Zinsen. Um wie viele Prozentpunkte ist der bessere Zinssatz höher?', 0.25, '60 / 2400 * 100 - 72 / 3200 * 100',
          'A: 60 : 2 400 = 2,5 %. B: 72 : 3 200 = 2,25 %. Unterschied 0,25 Prozentpunkte.', 'Berechne beide Zinssätze.'))
SK(lz, SZ('knobel', 'Die Zinsen werden jedes Jahr abgehoben. Bei welchem Zinssatz sind sie nach 25 Jahren zusammen so viel wie das Kapital?', 4, '100 / 25',
          'In 25 Jahren sollen die Zinsen 100 % des Kapitals ergeben. Jedes Jahr also 100 % : 25 = 4 %.', 'Wie viel Prozent muss es pro Jahr sein?', einheit='%'))
SK(lz, SZ('knobel', '2 000 € bringen in 8 Monaten 40 € Zinsen. Wie hoch ist der Jahreszinssatz?', 3, '40 / 8 * 12 / 2000 * 100', 'Für 8 Monate 40 €, also je Monat 5 € und für ein ganzes Jahr 12 · 5 € = 60 €. 60 € von 2 000 € sind 3 % – das ist der Jahreszinssatz.', 'Rechne zuerst die Zinsen für ein ganzes Jahr aus.', einheit='%'))

lz = 'kapital'
ST.leiter(lz, 'Kapital aus Zinsen und Zinssatz über 1 % bestimmen; die Rechnung erkennen.', 'Kredit aus Zinsen, Zinssatz mit Komma, gewünschte Zinsen, Zinsen zu anderem Kapital.',
          'Fehler deuten, Kapital aus dem Endstand, Banken vergleichen, halbes Jahr, Aussage begründen, gleiche Zinsen, Monatszinsen als Ziel, Zinsen aus dem Endstand.')
STB(lz, 2, 'Bei 6 %', 'direkt', neu_s=1); STB(lz, 2, 'Bei 2,5 %', 'mehrschritt'); STB(lz, 2, 'Jemand möchte', 'einkleidung')
STB(lz, 3, 'Bank A', 'transfer'); STB(lz, 3, 'Ein Kapital bringt', 'verknuepfen')
SN(lz, SA('erkennen', 'Wie berechnest du das Kapital K aus den Zinsen Z und dem Zinssatz p?', 'K = Z · 100 : p', ['K = Z · p : 100', 'K = Z + p'], 'Über 1 %: Z : p ist 1 %, mal 100 ergibt das Kapital.', 'Gehe über 1 %.'))
SN(lz, SZ('direkt', '1 % Zinsen sind 8 €. Wie groß ist das Kapital?', 800, '8 * 100', '1 % = 8 €, also 100 % = 800 €.', '100 % sind hundertmal so viel.', einheit=E))
SN(lz, SZ('umkehr', '2 400 € bringen 72 € Zinsen. Wie viel Euro Zinsen brächten 3 000 € beim gleichen Zinssatz?', 90, '3000 * 72 / 2400', 'Zinssatz: 72 : 2 400 = 3 %. 3 % von 3 000 € = 90 €.', 'Bestimme zuerst den Zinssatz.', einheit=E))
SN(lz, SZ('mehrschritt', 'Bei 1,5 % bekommt man in einem Jahr 33 € Zinsen. Wie groß ist das Kapital?', 2200, '33 / 1.5 * 100', '1 % = 33 € : 1,5 = 22 €, Kapital 2 200 €.', 'Teile durch 1,5, um 1 % zu erhalten.', einheit=E))
SN(lz, SZ('einkleidung', 'Oma bekommt für ihr Sparbuch bei 0,5 % genau 15 € Zinsen im Jahr. Wie viel Geld liegt darauf?', 3000, '15 / 0.5 * 100', '0,5 % = 15 €, also 1 % = 30 € und das Kapital 3 000 €.', 'Wie viel ist 1 %?', einheit=E))
SN(lz, SA('begruenden', 'Stimmt die Aussage? „Bei einem kleineren Zinssatz braucht man mehr Kapital für dieselben Zinsen.“', 'Ja, z. B. 30 € Zinsen: bei 3 % braucht man 1 000 €, bei 2 % 1 500 €.', ['Nein, man braucht weniger.', 'Nein, das Kapital ist immer gleich.'],
          'Kapital = Zinsen · 100 : p. Wird p kleiner, wird das Kapital größer.', 'Rechne ein Beispiel mit zwei Zinssätzen.'))
SN(lz, SZ('parameter', 'Für welches Kapital K sind 3 % von K genauso viel wie 5 % von 1 500 €?', 2500, '1500 * 5 / 3', '5 % von 1 500 € = 75 €. 3 % von K = 75 € ergibt K = 2 500 €.', 'Rechne zuerst 5 % von 1 500 € aus.', einheit=E))
SN(lz, SZ('pruefung', 'Jemand möchte jeden Monat 25 € Zinsen bekommen. Die Bank zahlt 2 % im Jahr. Wie viel Geld muss er anlegen?', 15000, '25 * 12 / 2 * 100', 'Im Jahr 300 €. 2 % = 300 € heißt 1 % = 150 €, Kapital 15 000 €.', 'Wie viel Zinsen braucht er im Jahr?', einheit=E))
SN(lz, SZ('transfer', 'Ein Konto ist in einem Jahr mit 2,5 % Zinsen auf 1 230 € angewachsen. Wie viel Euro Zinsen waren es?', 30, '1230 - 1230 / 1.025', '1 230 € sind 102,5 %. Kapital 1 200 €, Zinsen 30 €.', 'Bestimme zuerst das Kapital.', einheit=E))
SK(lz, SZ('knobel', 'Zwei Beträge ergeben zusammen 6 000 €. Der eine liegt zu 2 %, der andere zu 4 %. Beide bringen gleich viele Zinsen. Wie groß ist der größere Betrag?', 4000, '6000 * 2 / 3',
          'Der Betrag zu 2 % muss doppelt so groß sein wie der zu 4 %. Also 4 000 € und 2 000 € (beide bringen 80 €).', 'Wie müssen sich die Beträge verhalten, wenn ein Zinssatz doppelt so groß ist?', einheit=E))
SK(lz, SZ('knobel', 'Ein Kapital bringt in 3 Monaten bei 2,4 % Jahreszins 18 € Zinsen. Wie groß ist das Kapital?', 3000, '18 * 4 / 2.4 * 100', 'Ein Jahr brächte 4 · 18 € = 72 €. 2,4 % = 72 € ergibt 1 % = 30 € und das Kapital 3 000 €.', 'Rechne zuerst die Jahreszinsen aus.', einheit=E))

lz = 'monatszinsen'
ST.leiter(lz, 'Zinsen für ganze Monate mit Jahreszinsen · m/12; den Zeitanteil erkennen.', 'Monatszinsen bei großem Kapital, Zeitraum aus Daten, Rückzahlung eines Kredits, Kapital aus Monatszinsen.',
          'Fehler deuten, Monate rückwärts, Angebote vergleichen, Hochrechnen, höchstens erlaubte Monate, Bruchteil eines Jahres, Prüfungsaufgabe mit Daten.')
STB(lz, 2, 'Berechne die Zinsen für 7 200', 'direkt', neu_s=1); STB(lz, 2, 'Berechne die Zinsen für 10', 'mehrschritt')
STB(lz, 3, 'Wie viele Monate', 'rueckwaerts'); STB(lz, 3, 'Was bringt mehr', 'begruenden')
SN(lz, SA('erkennen', 'Welcher Bruchteil eines Jahres sind 5 Monate?', '5/12', ['5/10', '1/5', '5/100'], 'Ein Jahr hat 12 Monate, 5 Monate sind 5/12.', 'Wie viele Monate hat ein Jahr?'))
SN(lz, SZ('direkt', 'Die Jahreszinsen sind 60 €. Wie viel Zinsen gibt es für einen Monat?', 5, '60 / 12', '60 € : 12 = 5 €.', 'Teile durch die Zahl der Monate eines Jahres.', einheit=E))
SN(lz, SZ('umkehr', 'Für 4 Monate gab es bei 3 % Jahreszins 12 € Zinsen. Wie groß ist das Kapital?', 1200, '12 * 3 / 3 * 100', 'Ein Jahr brächte 3 · 12 € = 36 €. 3 % = 36 €, also Kapital 1 200 €.', 'Rechne zuerst die Jahreszinsen aus.', einheit=E))
SN(lz, SZ('parameter', '2 400 € liegen zu 5 % Jahreszins. Wie viele volle Monate darf das Geld höchstens liegen, damit es nicht mehr als 40 € Zinsen gibt?', 4, '40 // (2400 * 5 / 100 / 12)',
          'Im Jahr 120 €, im Monat 10 €. 40 € reichen für 4 Monate.', 'Wie viel bringt ein Monat?'))
SN(lz, SZ('verknuepfen', 'Ein Kredit über 1 800 € zu 6 % Jahreszins läuft 2/3 eines Jahres. Wie viel Euro Zinsen fallen an?', 72, '1800 * 6 / 100 * 2 / 3', 'Jahreszinsen: 108 €. Davon 2/3: 72 €.', 'Wie viel sind die Jahreszinsen?', einheit=E))
SN(lz, SZ('pruefung', 'Ein Kind legt am 1. Februar 1 500 € zu 2,4 % Jahreszins an und hebt am 1. Dezember alles ab. Wie viel Euro bekommt es?', 1530, '1500 + 1500 * 2.4 / 100 * 10 / 12',
          'Februar bis Dezember sind 10 Monate. Jahreszinsen 36 €, für 10 Monate 30 €. Ausgezahlt: 1 530 €.', 'Zähle zuerst die Monate.', einheit=E))
SN(lz, SZ('transfer', 'Für 7 Monate gibt es 14 € Zinsen. Wie viel Euro wären es für 1 1/2 Jahre, wenn die Zinsen nicht mitverzinst werden?', 36, '14 / 7 * 18', 'Je Monat 2 €. 1 1/2 Jahre sind 18 Monate: 36 €.', 'Wie viel bringt ein Monat?', einheit=E))
SK(lz, SZ('knobel', 'Jemand legt 3 600 € zu 4 % Jahreszins an. Nach wie vielen vollen Monaten hat er zum ersten Mal mehr als 100 € Zinsen?', 9, '9', 'Je Monat 3 600 € · 4 % : 12 = 12 €. Nach 8 Monaten 96 €, nach 9 Monaten 108 €.', 'Wie viel bringt ein Monat?'))
SK(lz, SA('knobel', 'Was bringt mehr Zinsen: 6 Monate zu 4 % oder 8 Monate zu 3 % (gleiches Kapital)?', 'Beide bringen gleich viel.', ['6 Monate zu 4 %', '8 Monate zu 3 %'],
          '6/12 von 4 % sind 2 %, 8/12 von 3 % sind auch 2 % des Kapitals. Kürzere Zeit wird durch den höheren Zinssatz genau ausgeglichen.', 'Rechne aus, wie viel Prozent des Kapitals es jeweils sind.'))

lz = 'zeitanteil'
ST.leiter(lz, 'Zinsen für ein halbes Jahr und ein Vierteljahr; wissen, wie viele Monate das sind.', 'Dreivierteljahr, Guthaben und Kredite für Teile eines Jahres, Kapital aus Halbjahreszinsen, anderthalb Jahre.',
          'Fehler deuten, Halbjahr auf Vierteljahr umrechnen, Angebote begründen, Dauer rückwärts, Zinssatz für 1 % im Vierteljahr, Drittel und Dreiviertel, Prüfungsaufgabe.')
STB(lz, 2, '5 000 €', 'mehrschritt'); STB(lz, 2, '500 €', 'direkt', neu_s=1)
STB(lz, 3, 'Ein Kapital bringt', 'transfer'); STB(lz, 3, 'Angebot A', 'begruenden'); STB(lz, 3, '2 000 €', 'rueckwaerts')
SN(lz, SZ('umkehr', 'Ein halbes Jahr bringt bei 4 % Jahreszins genau 50 € Zinsen. Wie groß ist das Kapital?', 2500, '50 * 2 / 4 * 100', 'Ein Jahr: 100 €. 4 % = 100 €, Kapital 2 500 €.', 'Rechne zuerst die Jahreszinsen aus.', einheit=E))
SN(lz, SZ('mehrschritt', '3 000 € liegen 1 1/2 Jahre zu 2 % Jahreszins, die Zinsen werden jedes Jahr abgehoben. Wie viel Euro Zinsen gibt es insgesamt?', 90, '3000 * 2 / 100 * 1.5', 'Ein Jahr: 60 €, ein halbes Jahr: 30 €. Zusammen 90 €.', 'Zerlege in 1 Jahr und 1/2 Jahr.', einheit=E))
SN(lz, SZ('einkleidung', 'Ein Kind legt 800 € Geburtstagsgeld für ein Vierteljahr zu 2 % Jahreszins an. Wie viel Euro Zinsen bekommt es?', 4, '800 * 2 / 100 / 4', 'Jahreszinsen 16 €, ein Viertel davon 4 €.', 'Ein Vierteljahr ist ein Viertel der Jahreszinsen.', einheit=E))
SN(lz, SZ('parameter', 'Bei welchem Jahreszinssatz bringt ein Vierteljahr genau 1 % des Kapitals?', 4, '1 * 4', 'Ein Vierteljahr bringt ein Viertel der Jahreszinsen. Ein Viertel von 4 % ist 1 %.', 'Wie oft passt ein Vierteljahr in ein Jahr?', einheit='%'))
SN(lz, SZ('verknuepfen', 'Ein Kapital bringt in 1/3 Jahr 16 € Zinsen. Wie viel Euro bringt es in 3/4 Jahr?', 36, '16 * 3 * 3 / 4', 'Ein Jahr: 3 · 16 € = 48 €. 3/4 davon: 36 €.', 'Rechne über ein ganzes Jahr.', einheit=E))
SN(lz, SZ('pruefung', 'Eine Firma leiht sich 24 000 € zu 5 % Jahreszins für ein Vierteljahr. Wie viel muss sie zurückzahlen?', 24300, '24000 + 24000 * 5 / 100 / 4', 'Jahreszinsen 1 200 €, für ein Vierteljahr 300 €. Zurück: 24 300 €.', 'Kredit plus Zinsen.', einheit=E))
SN(lz, SA('transfer', 'Was bringt mehr: ein Vierteljahr zu 8 % oder ein halbes Jahr zu 3 % (gleiches Kapital)?', 'ein Vierteljahr zu 8 %', ['ein halbes Jahr zu 3 %', 'Beide bringen gleich viel.'],
          'Vierteljahr zu 8 %: 2 % des Kapitals. Halbes Jahr zu 3 %: 1,5 %.', 'Wie viel Prozent des Kapitals sind es jeweils?'))
SK(lz, SZ('knobel', '2 000 € liegen erst ein Vierteljahr zu 6 % Jahreszins und danach (ohne die Zinsen) noch ein halbes Jahr zu 4 % Jahreszins. Wie viel Euro Zinsen gibt es insgesamt?', 70, '2000 * 6 / 100 / 4 + 2000 * 4 / 100 / 2',
         'Vierteljahr zu 6 %: Jahreszinsen 120 €, ein Viertel davon 30 €. Halbes Jahr zu 4 %: Jahreszinsen 80 €, die Hälfte 40 €. Zusammen 70 €.', 'Rechne beide Zeitabschnitte getrennt.', einheit=E))
SK(lz, SZ('knobel', 'Wie viele Tage muss ein Kapital von 36 000 € zu 5 % Jahreszins liegen, damit es 100 € Zinsen gibt? (Rechne mit 360 Tagen im Jahr.)', 20, '100 / (36000 * 5 / 100 / 360)',
          'Jahreszinsen: 1 800 €. Je Tag 1 800 € : 360 = 5 €. Für 100 € braucht es 20 Tage.', 'Wie viel bringt ein Tag?'))


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
    stufen_datei('finanzen.zinsen', ST)


# ---- BEREINIGEN (Einundzwanzigste Runde) ----
if __name__ == '__main__':
    from _bereinigen import bereinigen_datei
    bereinigen_datei('finanzen.zinsen')
# ---- BEREINIGEN ENDE ----
