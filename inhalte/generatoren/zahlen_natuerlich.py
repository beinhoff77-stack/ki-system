#!/usr/bin/env python3
"""Thema zahlen.natuerlich – Natürliche Zahlen und Stellenwertsysteme (Gymnasium Bayern, Klasse 5). Zwölfte Runde.

Lernkarten unverändert aus inhalte/klar/zahlen.natuerlich.json (Lernziele, Reihenfolge, Titel wie inhalte/klar/quelle.md); neu sind nur die Aufgaben.
Je Lernkarte 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8), 1 Test, 3 Korrektur, 6 Sicherung. Die bisherigen Aufgaben liegen nur in der Datenbank
und bleiben dort; die neuen kommen beim Einspielen dazu (einheit_abgleichen(…, 'lassen')).

Stufe 3 läuft je Lernkarte reihum durch feste Aufgabenarten („ARTEN“): mindestens zwei nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern,
Probeunterricht Gymnasium 5, Kurztests/Musterschulaufgaben Kl. 5) und mindestens eine Knobelaufgabe. Eigene Zahlen und Einkleidungen.
Alle Lösungen werden hier berechnet (Zahlwörter, römische Zahlen, Runden, Anzahlen durch Aufzählen).
"""
import sys
from itertools import permutations
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _bausatz as _b  # noqa: E402
from _auffuellen import A, L, Z, baue, etappen_aus_klar, g4 as zt  # noqa: E402

META = {'thema_schluessel': 'zahlen.natuerlich', 'thema_id': 15, 'block_id': 49, 'klasse': {'gym_by': 5}}
TITEL = [('stellenwert', 'Welchen Wert hat eine Ziffer?'), ('zahlwort_zu_ziffern', 'Große Zahlen schreiben'),
         ('ziffern_zu_zahlwort', 'Große Zahlen lesen'), ('strahl_ablesen', 'Zahlenstrahl ablesen'),
         ('strahl_eintragen', 'Zahl am Zahlenstrahl finden'), ('vergleichen', 'Welche Zahl ist größer?'),
         ('runden_regel', 'Runden'), ('runden_uebertrag', 'Runden mit der 9'), ('runden_sinnvoll', 'Wann darf man runden?'),
         ('unendlich', 'Gibt es eine größte natürliche Zahl?'), ('roemisch_schreiben', 'Römische Zahlen schreiben'),
         ('roemisch_system', 'Warum sind römische Zahlen anders?')]
ETAPPEN = etappen_aus_klar(META['thema_schluessel'], TITEL)
PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 6 + [('uebung', 3)] * 8 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6
HF = 'Trage in jedes Feld eine Zahl ein.'

# ---------------- Hilfen ----------------
_E = ['', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn',
      'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
_Z = ['', '', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']


def _bis999(n, ende=False):
    h, r = divmod(n, 100)
    s = (_E[h] + 'hundert') if h else ''
    if r == 1 and ende: s += 'eins'
    elif r < 20: s += _E[r]
    else: s += (_E[r % 10] + 'und' if r % 10 else '') + _Z[r // 10]
    return s


def zw(n):
    """Zahlwort (deutsche Rechtschreibung, Gruppen ab Million mit Leerzeichen): 3 040 500 → drei Millionen vierzigtausendfünfhundert."""
    if n == 0: return 'null'
    mrd, rest = divmod(n, 10 ** 9)
    mio, rest = divmod(rest, 10 ** 6)
    tsd, ein = divmod(rest, 1000)
    teile = []
    if mrd: teile.append('eine Milliarde' if mrd == 1 else _bis999(mrd) + ' Milliarden')
    if mio: teile.append('eine Million' if mio == 1 else _bis999(mio) + ' Millionen')
    hinten = (_bis999(tsd) + 'tausend' if tsd else '') + (_bis999(ein, ende=True) if ein else '')
    if hinten: teile.append(hinten)
    return ' '.join(teile)


_ROEM = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def roem(n):
    s = ''
    for w, z in _ROEM:
        while n >= w: s += z; n -= w
    return s


def roem_wert(s):
    w = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum(-w[a] if i + 1 < len(s) and w[a] < w[s[i + 1]] else w[a] for i, a in enumerate(s))


def runde(n, stelle):
    return (n + stelle // 2) // stelle * stelle


STELLEN = {1: 'Einer', 10: 'Zehner', 100: 'Hunderter', 1000: 'Tausender', 10 ** 4: 'Zehntausender', 10 ** 5: 'Hunderttausender', 10 ** 6: 'Millionen'}
STELLE_KURZ = {1: 'Einerstelle', 10: 'Zehnerstelle', 100: 'Hunderterstelle', 1000: 'Tausenderstelle', 10 ** 4: 'Zehntausenderstelle',
               10 ** 5: 'Hunderttausenderstelle', 10 ** 6: 'Millionenstelle', 10 ** 7: 'Zehnmillionenstelle'}
ZAEHLER = {}


def art(lz, arten):
    """Stufe 3: Aufgabenarten reihum, damit jede Art (Prüfungsvorbild, Knobel) sicher vorkommt."""
    i = ZAEHLER.get(lz, 0)
    ZAEHLER[lz] = i + 1
    return arten[i % len(arten)]


def ziffer_an(n, stelle): return n // stelle % 10


def zahl_mit(R, stellen, nullen=0):
    """Zufallszahl mit genau `stellen` Ziffern und mindestens `nullen` Nullen (nicht vorne)."""
    while True:
        z = [R.randint(1, 9)] + [R.randint(0, 9) for _ in range(stellen - 1)]
        for i in R.sample(range(1, stellen), nullen): z[i] = 0
        n = int(''.join(map(str, z)))
        gruppen = [n // 10 ** 9 % 1000, n // 10 ** 6 % 1000]
        if any(g > 1 and g % 100 == 1 for g in gruppen): continue   # „…hundertein Millionen“ vermeiden
        if str(n).count('0') >= nullen: return n


# ---------------- 1 Stellenwert ----------------
def g_stellenwert(R, s):
    if s == 1:
        n = zahl_mit(R, R.choice([4, 5]))
        st = R.choice([10, 100, 1000] + ([10 ** 4] if n >= 10 ** 4 else []))
        d = ziffer_an(n, st)
        if d == 0: return g_stellenwert(R, 1)
        return Z(f'Welchen Wert hat die Ziffer {d} an der {STELLE_KURZ[st]} von {zt(n)}?', d * st, f'{d} * {st}',
                 f'Die {d} steht bei den {STELLEN[st]}n. Sie ist {d} · {zt(st)} = {zt(d * st)} wert.', 'Trag die Zahl in eine Stellenwerttafel ein.')
    if s == 2:
        k = R.choice(['wert', 'ziffer', 'zerlegen', 'aendern'])
        n = zahl_mit(R, R.choice([6, 7, 8]), nullen=1)
        if k == 'wert':
            st = R.choice([10 ** 4, 10 ** 5, 10 ** 6] if n >= 10 ** 6 else [1000, 10 ** 4, 10 ** 5])
            d = ziffer_an(n, st)
            if d == 0: return g_stellenwert(R, 2)
            return Z(f'Welchen Wert hat die Ziffer an der {STELLE_KURZ[st]} von {zt(n)}?', d * st, f'{d} * {st}',
                     f'An der {STELLE_KURZ[st]} steht die {d}. Ihr Wert: {d} · {zt(st)} = {zt(d * st)}.', 'Zähle von rechts: E, Z, H, T, ZT, HT, M …')
        if k == 'ziffer':
            st = R.choice([10 ** 4, 10 ** 5] + ([10 ** 6] if n >= 10 ** 6 else []))
            return Z(f'Welche Ziffer steht in {zt(n)} an der {STELLE_KURZ[st]}?', ziffer_an(n, st), f'{n} // {st} % 10',
                     f'Von rechts: Einer, Zehner, Hunderter, Tausender … An der {STELLE_KURZ[st]} steht {ziffer_an(n, st)}.', 'Schreibe die Zahl in eine Stellenwerttafel.')
        if k == 'zerlegen':
            m = zahl_mit(R, 4, nullen=R.choice([0, 1]))
            w = [ziffer_an(m, 10 ** i) for i in (3, 2, 1, 0)]
            return L(f'Zerlege {zt(m)} in Stellenwerte.', '□ T + □ H + □ Z + □ E', w, [f'{m} // {10 ** i} % 10' for i in (3, 2, 1, 0)],
                     f'{zt(m)} = {w[0]} Tausender + {w[1]} Hunderter + {w[2]} Zehner + {w[3]} Einer.', 'Lies die Ziffern von links nach rechts ab.', HF)
        st = R.choice([100, 1000, 10 ** 4])
        if ziffer_an(n, st) == 9: return g_stellenwert(R, 2)
        return Z(f'In {zt(n)} wird die Ziffer an der {STELLE_KURZ[st]} um 1 größer. Um wie viel wird die Zahl größer?', st, f'{n + st} - {n}',
                 f'1 mehr an der {STELLE_KURZ[st]} heißt {zt(st)} mehr: {zt(n)} + {zt(st)} = {zt(n + st)}.', 'Was ist eine Einheit an dieser Stelle wert?')
    a = art('stellenwert', ['probeunterricht', 'karten', 'ziffernzahl', 'tauschen'])
    if a == 'probeunterricht':
        m, ht, zt_, z = R.randint(2, 9), R.randint(11, 19), R.randint(1, 9), R.randint(1, 9)
        wert = m * 10 ** 6 + ht * 10 ** 5 + zt_ * 10 ** 4 + z * 10
        return Z(f'Schreibe als Zahl: {m} M {ht} HT {zt_} ZT {z} Z (M = Millionen, HT = Hunderttausender, ZT = Zehntausender, Z = Zehner)',
                 wert, f'{m} * 10**6 + {ht} * 10**5 + {zt_} * 10**4 + {z} * 10',
                 f'{ht} HT sind 1 M und {ht - 10} HT. Zusammen: {m + 1} M {ht - 10} HT {zt_} ZT 0 T 0 H {z} Z 0 E = {zt(wert)}.',
                 f'{ht} Hunderttausender sind mehr als 10 – es gibt einen Übertrag zu den Millionen.')
    if a == 'karten':
        d, e = R.sample(range(1, 10), 2)
        karten = [f'{d}{e}', f'{d}{e}0', f'{d}0{e}', f'{d}00']
        R.shuffle(karten)
        groesst = max(int(''.join(p)) for p in permutations(karten))
        return Z(f'Die Zahlenkarten {", ".join(karten)} werden nebeneinandergelegt, jede genau einmal. Welche Zahl ist die größte, die man legen kann?',
                 groesst, str(groesst), f'Alle Karten beginnen mit {d}. Entscheidend ist, welche Reihenfolge vorne größere Ziffern ergibt. Probiert man alle 24 Reihenfolgen, ist {zt(groesst)} am größten.',
                 'Vergleiche zwei Karten, indem du sie in beiden Reihenfolgen nebeneinanderlegst, z. B. 45|450 und 450|45.')
    if a == 'ziffernzahl':
        bis = R.choice([99, 150, 200, 250, 300, 999])
        anzahl = sum(len(str(i)) for i in range(1, bis + 1))
        return Z(f'Ein Buch hat {zt(bis)} Seiten. Wie viele Ziffern braucht man, um alle Seitenzahlen von 1 bis {zt(bis)} zu drucken?', anzahl,
                 ' + '.join(f'{k} * {n}' for k, n in [(1, min(bis, 9)), (2, max(0, min(bis, 99) - 9)), (3, max(0, bis - 99))] if n),
                 f'1 bis 9: {min(bis, 9)} Ziffern. 10 bis {min(bis, 99)}: {max(0, min(bis, 99) - 9)} Zahlen mit 2 Ziffern. '
                 + (f'100 bis {zt(bis)}: {bis - 99} Zahlen mit 3 Ziffern. ' if bis > 99 else '') + f'Zusammen {zt(anzahl)}.',
                 'Zähle getrennt: einstellige, zweistellige und dreistellige Seitenzahlen.')
    n = zahl_mit(R, 5)
    t = str(n)
    i, j = sorted(R.sample(range(5), 2))
    if t[i] >= t[j] or (i == 0 and t[j] == '0'): return g_stellenwert(R, 3)
    neu = t[:i] + t[j] + t[i + 1:j] + t[i] + t[j + 1:]
    return Z(f'In {zt(n)} werden die Ziffern {t[i]} und {t[j]} vertauscht. Um wie viel wird die Zahl größer?', int(neu) - n, f'{int(neu)} - {n}',
             f'Neue Zahl: {zt(int(neu))}. Unterschied: {zt(int(neu))} − {zt(n)} = {zt(int(neu) - n)}.', 'Schreibe die neue Zahl auf und ziehe die alte ab.')


# ---------------- 2 Zahlwort → Ziffern ----------------
def g_zahlwort_zu_ziffern(R, s):
    if s == 1:
        n = zahl_mit(R, R.choice([4, 5, 6]), nullen=R.choice([1, 2]))
        return Z(f'Schreibe als Zahl: {zw(n)}', n, str(n), f'In Dreiergruppen: {zt(n)}. Leere Stellen bekommen eine 0.', 'Schreibe zuerst die Tausender, dann drei Ziffern für den Rest.')
    if s == 2:
        n = zahl_mit(R, R.choice([7, 8, 9]), nullen=R.choice([3, 4, 5]))
        return Z(f'Schreibe als Zahl: {zw(n)}', n, str(n), f'Millionen | Tausender | Einer: {zt(n)}. Jede Gruppe nach der ersten hat drei Ziffern.',
                 'Mach dir drei Kästchen: Millionen, Tausender, Einer. Fülle fehlende Stellen mit 0.')
    a = art('zahlwort_zu_ziffern', ['gemischt', 'nullen', 'nachfolger', 'knobel'])
    if a == 'gemischt':
        mrd, mio, rest = R.randint(2, 9), R.choice([5, 7, 12, 30, 400]), R.choice([60, 7, 800, 15])
        n = mrd * 10 ** 9 + mio * 10 ** 6 + rest
        return Z(f'Schreibe als Zahl: {mrd} Milliarden {mio} Millionen {rest}', n, f'{mrd} * 10**9 + {mio} * 10**6 + {rest}',
                 f'Milliarden | Millionen | Tausender | Einer: {mrd} | {mio:03d} | 000 | {rest:03d}. Also {zt(n)}.', 'Für die Tausender wurde nichts gesagt: dort stehen drei Nullen.')
    if a == 'nullen':
        n = zahl_mit(R, R.choice([8, 9, 10]), nullen=R.choice([4, 5, 6]))
        return Z(f'Wie viele Nullen hat die Zahl „{zw(n)}“, wenn man sie mit Ziffern schreibt?', str(n).count('0'), str(str(n).count('0')),
                 f'Mit Ziffern: {zt(n)}. Darin stehen {str(n).count("0")} Nullen.', 'Schreibe die Zahl zuerst in Dreiergruppen auf.')
    if a == 'nachfolger':
        k = R.choice([3, 4, 5])
        n = R.randint(1, 9) * 10 ** (3 * k // 3 + 3) + 10 ** (3 * k // 3) - 1
        return Z(f'Welche Zahl folgt direkt auf „{zw(n)}“? Schreibe sie mit Ziffern.', n + 1, f'{n} + 1',
                 f'{zt(n)} + 1 = {zt(n + 1)}. Alle Neunen werden zu Nullen, die Stelle davor wird um 1 größer.', 'Schreibe die Zahl zuerst mit Ziffern und zähle 1 dazu.')
    d, k = R.randint(2, 9), R.choice([6, 7, 8])
    n = int(str(d) * k)
    return Z(f'Eine {k}-stellige Zahl besteht nur aus gleichen Ziffern. Ihre Quersumme ist {d * k}. Wie heißt die Zahl?', n, str(n),
             f'{k} gleiche Ziffern mit Summe {d * k}: jede Ziffer ist {d * k} : {k} = {d}. Die Zahl ist {zt(n)}.', 'Wie groß muss jede der Ziffern sein?')


# ---------------- 3 Ziffern → Zahlwort ----------------
def _falsch_lesen(n):
    t = str(n)
    kand = [n * 10, n // 10 if n % 10 == 0 else n * 100, int(t.replace('0', '', 1)) if '0' in t[1:] else n + 10 ** (len(t) - 1)]
    return [zw(k) for k in kand if k != n]


def g_ziffern_zu_zahlwort(R, s):
    if s == 1:
        n = zahl_mit(R, R.choice([5, 6]), nullen=R.choice([1, 2]))
        return A(R, f'Wie liest man {zt(n)}?', zw(n), _falsch_lesen(n), f'Dreiergruppen: {zt(n)}. Also: {zw(n)}.', 'Teile die Zahl von rechts in Dreiergruppen.')
    if s == 2:
        n = zahl_mit(R, R.choice([7, 8, 9]), nullen=R.choice([3, 4]))
        return A(R, f'Wie liest man {zt(n)}?', zw(n), _falsch_lesen(n), f'Gruppen: {zt(n)}. Gelesen: {zw(n)}.', 'Erst die Millionen, dann die Tausender, dann der Rest. 000-Gruppen überspringst du.')
    a = art('ziffern_zu_zahlwort', ['zeitung', 'gelesen', 'milliarde', 'zehn'])
    if a == 'zeitung':
        g, z = R.choice([(2, 4), (1, 7), (3, 5), (6, 2), (12, 5), (4, 8)])
        n = g * 10 ** 6 + z * 10 ** 5
        return Z(f'In der Zeitung steht: „rund {g},{z} Millionen Besucher“. Schreibe die Zahl ohne Komma mit Ziffern.', n, f'{g} * 10**6 + {z} * 10**5',
                 f'{g},{z} Millionen sind {g} Millionen und {z} Hunderttausend: {zt(n)}.', 'Die Ziffer nach dem Komma gehört zu den Hunderttausendern.')
    if a == 'gelesen':
        n = R.randint(2, 9) * 10 ** 9 + R.randint(1, 9) * R.choice([10 ** 5, 10 ** 4, 10 ** 3]) + R.choice([0, R.randint(1, 99)])
        return Z(f'Welche Zahl wird so gelesen: „{zw(n)}“? Schreibe sie mit Ziffern.', n, str(n),
                 f'Milliarden | Millionen | Tausender | Einer: {zt(n)}. Die Millionen-Gruppe ist 000.', 'Achte auf die leere Millionen-Gruppe.')
    if a == 'milliarde':
        n = 10 ** 9 + R.choice([1000, 10 ** 6, 100, 10 ** 5])
        falsch = [zw(10 ** 9 + 10 ** 6 if n != 10 ** 9 + 10 ** 6 else 10 ** 9 + 1000), zw(10 ** 6 + n % 10 ** 6 if n % 10 ** 6 else 10 ** 6 + 1000), zw(n * 10)]
        return A(R, f'Welches Zahlwort gehört zu {zt(n)}?', zw(n), falsch, f'{zt(n)}: eine Milliarde und {zw(n - 10 ** 9)}. Zusammen: {zw(n)}.',
                 'Zähle die Dreiergruppen. Vier Gruppen: Milliarden, Millionen, Tausender, Einer.')
    wort, d = R.choice([('zehn', 10), ('zwanzig', 20), ('dreißig', 30), ('vierzig', 40), ('fünfzig', 50)])
    n = d * 10 ** 6 + d * 1000 + d
    return Z(f'Lies die Zahl {zt(n)}. Wie oft kommt im Zahlwort das Wort „{wort}“ vor?', zw(n).count(wort), str(zw(n).count(wort)),
             f'{zt(n)} heißt „{zw(n)}“. Darin steht „{wort}“ {zw(n).count(wort)}-mal.', 'Lies jede Dreiergruppe einzeln.')


# ---------------- 4 Zahlenstrahl ablesen ----------------
def _strahl(start, ende, ab, pfeil):
    return {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': ab, 'beschriftet': 'anfang_ende', 'pfeil': pfeil}


def g_strahl_ablesen(R, s):
    if s == 1:
        ab = R.choice([4, 5, 8, 10])
        ende = ab * R.choice([2, 5, 20, 25, 50])
        p = R.randint(1, ab - 1)
        w = ende // ab
        a = Z('Welche Zahl zeigt der Pfeil?', p * w, f'0 + {p} * ({ende} - 0) // {ab}', f'Abschnittswert: {zt(ende)} : {ab} = {zt(w)}. Pfeil: {p} Abschnitte, also {p} · {zt(w)} = {zt(p * w)}.',
              'Rechne zuerst den Abschnittswert aus.')
        return _b.mit_bild(a, _strahl(0, ende, ab, p))
    if s == 2:
        ab = R.choice([4, 5, 8, 10])
        w = R.choice([5, 25, 50, 100, 250])
        start = R.choice([100, 200, 500, 1000, 2000, 5000])
        ende = start + ab * w
        p = R.randint(1, ab - 1)
        a = Z('Welche Zahl zeigt der Pfeil?', start + p * w, f'{start} + {p} * ({ende} - {start}) // {ab}',
              f'Abschnittswert: ({zt(ende)} − {zt(start)}) : {ab} = {zt(w)}. Pfeil: {zt(start)} + {p} · {zt(w)} = {zt(start + p * w)}.',
              'Der Strahl beginnt nicht bei 0. Vergiss die Anfangszahl nicht.')
        return _b.mit_bild(a, _strahl(start, ende, ab, p))
    a = art('strahl_ablesen', ['gross', 'eng', 'knobel', 'fehler'])
    if a == 'gross':
        ab = R.choice([6, 8, 12])
        w = R.choice([250_000, 500_000, 125_000])
        p = R.randint(1, ab - 1)
        ende = ab * w
        x = Z('Welche Zahl zeigt der Pfeil?', p * w, f'{p} * {ende} // {ab}', f'Abschnittswert: {zt(ende)} : {ab} = {zt(w)}. Pfeil: {p} · {zt(w)} = {zt(p * w)}.',
              'Große Zahlen: Rechne den Abschnittswert in Tausendern, z. B. 3 000 Tausender : 12.')
        return _b.mit_bild(x, _strahl(0, ende, ab, p))
    if a == 'eng':
        start = R.choice([2400, 7800, 12_500, 39_900])
        ab = R.choice([4, 5, 8])
        w = R.choice([5, 10, 25, 50])
        p = R.randint(1, ab - 1)
        ende = start + ab * w
        x = Z('Welche Zahl zeigt der Pfeil?', start + p * w, f'{start} + {p} * ({ende} - {start}) // {ab}',
              f'Von {zt(start)} bis {zt(ende)} sind es {zt(ende - start)}, auf {ab} Abschnitte: {zt(w)} je Abschnitt. Pfeil: {zt(start + p * w)}.',
              'Rechne zuerst den Unterschied zwischen Ende und Anfang aus.')
        return _b.mit_bild(x, _strahl(start, ende, ab, p))
    if a == 'knobel':
        w = R.choice([25, 50, 75, 100, 125])
        i, j = sorted(R.sample(range(2, 9), 2))
        start = R.choice([0, 100, 200, 300, 500, 1000])
        return Z(f'Auf einem Zahlenstrahl mit gleich großen Abschnitten steht am {i}. Strich nach dem Anfang die Zahl {zt(start + i * w)} und am {j}. Strich die Zahl {zt(start + j * w)}. Bei welcher Zahl beginnt der Strahl?',
                 start, f'{start + i * w} - {i} * ({start + j * w} - {start + i * w}) // ({j} - {i})',
                 f'Zwischen Strich {i} und {j} liegen {j - i} Abschnitte mit zusammen {zt((j - i) * w)}: Abschnittswert {zt(w)}. Anfang: {zt(start + i * w)} − {i} · {zt(w)} = {zt(start)}.',
                 'Bestimme zuerst den Abschnittswert aus den beiden bekannten Strichen.')
    start, w, ab = R.choice([(200, 100, 5), (300, 50, 6), (1000, 250, 4), (400, 200, 5)])
    p = R.randint(2, ab - 1)
    ende = start + ab * w
    falsch_wert = p * w
    if falsch_wert == start + p * w: return g_strahl_ablesen(R, 3)
    x = A(R, f'Jemand liest am Pfeil {zt(falsch_wert)} ab. Was ist falsch?', f'Die Anfangszahl fehlt: richtig ist {zt(start)} + {p} · {zt(w)} = {zt(start + p * w)}.',
          ['Nichts, das stimmt.', f'Der Abschnittswert ist {zt(ende // ab)}, also {zt(p * (ende // ab))}.', f'Man zählt die Striche mit: {zt(start + (p + 1) * w)}.'],
          f'Abschnittswert: ({zt(ende)} − {zt(start)}) : {ab} = {zt(w)}. Gezählt wird ab der Anfangszahl: {zt(start + p * w)}.', 'Wo beginnt der Zahlenstrahl?')
    return _b.mit_bild(x, _strahl(start, ende, ab, p))


# ---------------- 5 Zahl am Zahlenstrahl finden ----------------
def _M(text, start, ende, ab, ziel, w, h):
    idx = (ziel - start) * ab // (ende - start)
    assert start + idx * (ende - start) // ab == ziel
    return _b.M(text, start, ende, ab, idx, w, h)


def g_strahl_eintragen(R, s):
    if s == 1:
        ab = R.choice([5, 10])
        ende = ab * R.choice([2, 5, 20, 50])
        w = ende // ab
        z = w * R.randint(1, ab - 1)
        if (ende, z) == (100, 70): return g_strahl_eintragen(R, 1)
        return _M(f'Tippe die Markierung an, an der {zt(z)} liegt.', 0, ende, ab, z, f'Abschnittswert: {zt(ende)} : {ab} = {zt(w)}. {zt(z)} : {zt(w)} = {z // w}: {z // w} Abschnitte nach dem Anfang.',
                  'Rechne zuerst den Abschnittswert aus.')
    if s == 2:
        ab = R.choice([4, 5, 8, 10])
        w = R.choice([5, 25, 50, 100, 500])
        start = R.choice([100, 300, 1000, 2000, 5000])
        ende = start + ab * w
        k = R.randint(1, ab - 1)
        z = start + k * w
        return _M(f'Tippe die Markierung an, an der {zt(z)} liegt.', start, ende, ab, z,
                  f'Abschnittswert: ({zt(ende)} − {zt(start)}) : {ab} = {zt(w)}. ({zt(z)} − {zt(start)}) : {zt(w)} = {k} Abschnitte nach dem Anfang.',
                  'Zieh zuerst die Anfangszahl ab.')
    a = art('strahl_eintragen', ['gross', 'mitte', 'spiegel', 'abschnitte'])
    if a == 'gross':
        start = R.choice([300_000, 1_200_000, 40_000])
        ab = 8
        w = R.choice([5000, 25_000, 2500])
        k = R.randint(1, 7)
        return _M(f'Tippe die Markierung an, an der {zt(start + k * w)} liegt.', start, start + ab * w, ab, start + k * w,
                  f'Abschnittswert: {zt(ab * w)} : {ab} = {zt(w)}. ({zt(start + k * w)} − {zt(start)}) : {zt(w)} = {k}.', 'Rechne mit Tausendern, wenn die Zahlen groß sind.')
    if a == 'mitte':
        w, ab = R.choice([(50, 10), (25, 8), (100, 10), (250, 8)])
        start = R.choice([0, 500, 1000])
        i, j = R.sample(range(0, ab + 1, 2), 2)
        m = start + (i + j) // 2 * w
        return _M(f'Tippe die Zahl an, die genau in der Mitte zwischen {zt(start + min(i, j) * w)} und {zt(start + max(i, j) * w)} liegt.', start, start + ab * w, ab, m,
                  f'Mitte: ({zt(start + min(i, j) * w)} + {zt(start + max(i, j) * w)}) : 2 = {zt(m)}.', 'Die Mitte liegt gleich viele Abschnitte von beiden Zahlen entfernt.')
    if a == 'spiegel':
        w, ab = R.choice([(50, 10), (100, 10), (25, 8), (200, 10)])
        start = R.choice([0, 100, 400])
        mi = R.randint(3, ab - 3)
        d = R.randint(1, min(mi, ab - mi))
        m, links = start + mi * w, start + (mi - d) * w
        return _M(f'{zt(links)} liegt {d} Abschnitt{"e" if d > 1 else ""} links von {zt(m)}. Tippe die Zahl an, die genau so weit rechts von {zt(m)} liegt.', start, start + ab * w, ab, m + d * w,
                  f'Abschnittswert {zt(w)}. {zt(m)} + {d} · {zt(w)} = {zt(m + d * w)}.', 'Geh von der Mitte aus gleich viele Abschnitte nach rechts.')
    start, w = R.choice([(2000, 250), (500, 125), (10_000, 2500), (300, 75)])
    k = R.randint(2, 9)
    return Z(f'Ein Zahlenstrahl beginnt bei {zt(start)}, ein Abschnitt ist {zt(w)} wert. Wie viele Abschnitte nach dem Anfang liegt {zt(start + k * w)}?', k,
             f'({start + k * w} - {start}) // {w}', f'({zt(start + k * w)} − {zt(start)}) : {zt(w)} = {zt(k * w)} : {zt(w)} = {k}.', 'Erst die Anfangszahl abziehen, dann durch den Abschnittswert teilen.')


# ---------------- 6 Vergleichen ----------------
def g_vergleichen(R, s):
    if s == 1:
        a = zahl_mit(R, R.choice([4, 5]))
        b = int(str(a)[:-1]) if R.random() < .5 else zahl_mit(R, len(str(a)))
        if a == b or str(a)[0] == str(b)[0] and len(str(a)) == len(str(b)): return g_vergleichen(R, 1)
        g = max(a, b)
        return A(R, f'Welche Zahl ist größer: {zt(a)} oder {zt(b)}?', zt(g), [zt(min(a, b)), 'Beide sind gleich groß.'],
                 f'{"Mehr Ziffern: " if len(str(a)) != len(str(b)) else "Erste Ziffer von links entscheidet: "}{zt(g)} ist größer.', 'Zähle zuerst die Ziffern.')
    if s == 2:
        a = zahl_mit(R, R.choice([5, 6, 7]))
        t = list(str(a))
        i = R.randint(2, len(t) - 1)
        t[i] = str((int(t[i]) + R.randint(1, 8)) % 10)
        b = int(''.join(t))
        if a == b: return g_vergleichen(R, 2)
        zeichen = '<' if a < b else '>'
        return A(R, f'Welches Zeichen gehört zwischen {zt(a)} □ {zt(b)}?', zeichen, ['>' if zeichen == '<' else '<', '='],
                 f'Von links vergleichen: Der erste Unterschied ist an der {i + 1}. Stelle. Also {zt(a)} {zeichen} {zt(b)}.', 'Vergleiche Ziffer für Ziffer von links.')
    k = art('vergleichen', ['einsetzen', 'ordnen', 'knobel_groesst', 'knobel_qs'])
    if k == 'einsetzen':
        a = zahl_mit(R, 5)
        t = str(a)
        pos = R.randint(2, 3)
        moegl = [d for d in range(10) if int(t[:pos] + str(d) + t[pos + 1:]) > a]
        if not moegl or len(moegl) == 10: return g_vergleichen(R, 3)
        luecke = t[:pos] + '□' + t[pos + 1:]
        return Z(f'Für □ wird eine Ziffer eingesetzt. Für wie viele Ziffern (0 bis 9) gilt {luecke[:2] + ' ' + luecke[2:]} > {zt(a)}?', len(moegl), str(len(moegl)),
                 f'Die ersten Ziffern sind gleich. An der Lückenstelle steht bei {zt(a)} die {t[pos]}. Größer wird es mit '
                 + (f'{", ".join(map(str, moegl))}' if moegl else 'keiner Ziffer') + f' – das sind {len(moegl)}. (Bei {t[pos]} entscheidet der Rest.)',
                 'Vergleiche von links: Ab der Lücke entscheidet die eingesetzte Ziffer. Prüfe auch die Ziffer, die gleich ist.')
    if k == 'ordnen':
        b = zahl_mit(R, 6)
        t = str(b)
        zahlen = {b, int(t[0] + t[2] + t[1] + t[3:]), int(t[:3] + t[4] + t[3] + t[5]), int(t[:-1])}
        zahlen = sorted(zahlen)
        if len(zahlen) < 4: return g_vergleichen(R, 3)
        liste = sorted(zahlen, key=lambda x: R.random())
        return Z(f'Ordne von klein nach groß: {"; ".join(zt(x) for x in liste)}. Welche Zahl steht an dritter Stelle?', zahlen[2], str(zahlen[2]),
                 f'Geordnet: {" < ".join(zt(x) for x in zahlen)}. An dritter Stelle: {zt(zahlen[2])}.', 'Zuerst nach der Zahl der Ziffern, dann von links Ziffer für Ziffer.')
    if k == 'knobel_groesst':
        g = R.choice([70_000, 50_000, 34_000, 90_000, 61_000])
        best = max(n for n in range(g - 3000, g) if len(set(str(n))) == 5)
        return Z(f'Wie heißt die größte fünfstellige Zahl mit lauter verschiedenen Ziffern, die kleiner ist als {zt(g)}?', best, str(best),
                 f'Vorne muss es so groß wie möglich, aber unter {zt(g)} bleiben. Dann von links jeweils die größte noch freie Ziffer: {zt(best)}.',
                 'Geh Stelle für Stelle von links vor und nimm jeweils die größte erlaubte Ziffer.')
    q = R.choice([5, 7, 10, 12])
    st = R.choice([5, 6])
    best = min(n for n in range(10 ** (st - 1), 10 ** (st - 1) + 10 ** 4) if sum(map(int, str(n))) == q)
    return Z(f'Wie heißt die kleinste {st}-stellige Zahl mit der Quersumme {q}?', best, str(best),
             f'Vorne mindestens eine 1, die restliche Quersumme möglichst weit hinten: {zt(best)}.', 'Kleine Ziffern nach vorne, die großen nach hinten.')


# ---------------- 7 Runden ----------------
def g_runden_regel(R, s):
    if s == 1:
        n = zahl_mit(R, 4)
        st = R.choice([10, 100])
        if (n, st) == (3472, 100): return g_runden_regel(R, 1)
        r = runde(n, st)
        if len(str(r)) != len(str(n)) or ziffer_an(n, st) == 9: return g_runden_regel(R, 1)
        return Z(f'Runde {zt(n)} auf {STELLEN[st]}.', r, f'({n} + {st // 2}) // {st} * {st}',
                 f'Rechts von der {STELLE_KURZ[st]} steht {ziffer_an(n, st // 10)}: {"aufrunden" if ziffer_an(n, st // 10) >= 5 else "abrunden"}. {zt(n)} ≈ {zt(r)}.',
                 'Schau auf die Ziffer rechts neben der Rundungsstelle.')
    if s == 2:
        n = zahl_mit(R, R.choice([6, 7]))
        st = R.choice([1000, 10 ** 4, 10 ** 5])
        if ziffer_an(n, st) == 9: return g_runden_regel(R, 2)
        r = runde(n, st)
        return Z(f'Runde {zt(n)} auf {STELLEN[st]}.', r, f'({n} + {st // 2}) // {st} * {st}',
                 f'Rechts von der {STELLE_KURZ[st]} steht {ziffer_an(n, st // 10)}: {"aufrunden" if ziffer_an(n, st // 10) >= 5 else "abrunden"}. {zt(n)} ≈ {zt(r)}.',
                 'Markiere die Rundungsstelle und schau eine Stelle weiter rechts.')
    k = art('runden_regel', ['welche', 'auswahl', 'groesste', 'anzahl'])
    if k == 'welche':
        ziel = R.choice([350_000, 120_000, 780_000, 460_000])
        st = 10 ** 4
        opts = [ziel - 5001, ziel - 5000, ziel + 4999 + 1, ziel - 15_000]
        richtig = [o for o in opts if runde(o, st) == ziel]
        if len(richtig) != 1: return g_runden_regel(R, 3)
        return A(R, f'Welche Zahl ergibt auf Zehntausender gerundet {zt(ziel)}?', zt(richtig[0]), [zt(o) for o in opts if o != richtig[0]],
                 f'{zt(richtig[0])}: Rechts von der Zehntausenderstelle steht eine Ziffer, die auf {zt(ziel)} führt. Die anderen werden zu {", ".join(zt(runde(o, st)) for o in opts if o != richtig[0])}.',
                 'Runde jede Zahl auf Zehntausender und vergleiche.')
    if k == 'auswahl':
        n = zahl_mit(R, 6)
        if ziffer_an(n, 100) == 9: return g_runden_regel(R, 3)
        r = runde(n, 100)
        falsch = [n // 100 * 100 if r != n // 100 * 100 else r + 100, n // 10 * 10, int(str(r)[:-2])]
        return A(R, f'Runde {zt(n)} auf Hunderter. Welche Lösung stimmt?', zt(r), [zt(f) for f in falsch],
                 f'Hunderterstelle: {ziffer_an(n, 100)}, rechts daneben {ziffer_an(n, 10)}: {"aufrunden" if ziffer_an(n, 10) >= 5 else "abrunden"}. Dahinter alles 0: {zt(r)}.',
                 'Hinter der Rundungsstelle wird alles zu 0 – die Zahl wird nicht kürzer.')
    if k == 'groesste':
        z = R.choice([5300, 2700, 9100, 48_000, 120_000])
        st = 100 if z < 10_000 else 1000
        groesst = max(n for n in range(z - st, z + st) if runde(n, st) == z)
        kleinst = min(n for n in range(z - st, z + st) if runde(n, st) == z)
        if R.random() < .5:
            return Z(f'Wie heißt die größte natürliche Zahl, die auf {STELLEN[st]} gerundet {zt(z)} ergibt?', groesst, str(groesst),
                     f'Ab {zt(z + st // 2)} würde man auf {zt(z + st)} runden. Die größte ist {zt(groesst)}.', 'Ab welcher Zahl wird schon auf den nächsten Wert gerundet?')
        return Z(f'Wie heißt die kleinste natürliche Zahl, die auf {STELLEN[st]} gerundet {zt(z)} ergibt?', kleinst, str(kleinst),
                 f'{zt(kleinst - 1)} wird abgerundet, {zt(kleinst)} schon aufgerundet. Die kleinste ist {zt(kleinst)}.', 'Ab welcher Zahl wird auf diesen Wert aufgerundet?')
    z, st = R.choice([(80, 10), (300, 100), (4000, 1000), (650, 10), (1200, 100)])
    anz = sum(1 for n in range(1, z + st) if runde(n, st) == z)
    return Z(f'Wie viele natürliche Zahlen ergeben auf {STELLEN[st]} gerundet {zt(z)}?', anz, str(anz),
             f'Von {zt(z - st // 2)} bis {zt(z + st // 2 - 1)}: das sind {anz} Zahlen.', 'Bestimme die kleinste und die größte passende Zahl.')


# ---------------- 8 Runden mit der 9 ----------------
def _neun(R, stellen, st):
    while True:
        n = zahl_mit(R, stellen)
        t = list(str(n))
        i = len(t) - len(str(st))
        t[i] = '9'
        if i > 0 and R.random() < .6: t[i - 1] = '9'
        t[i + 1] = str(R.randint(5, 9))
        n = int(''.join(t))
        if runde(n, st) != n: return n


def g_runden_uebertrag(R, s):
    if s == 1:
        st = R.choice([10, 100])
        n = _neun(R, 4, st)
        if n == 2995: return g_runden_uebertrag(R, 1)
        r = runde(n, st)
        return Z(f'Runde {zt(n)} auf {STELLEN[st]}.', r, f'({n} + {st // 2}) // {st} * {st}',
                 f'An der {STELLE_KURZ[st]} steht 9, rechts daneben {ziffer_an(n, st // 10)}: aufrunden. Aus der 9 wird 10, 1 geht nach links weiter: {zt(r)}.',
                 'Wird aus der 9 eine 10, geht 1 zur nächsten Stelle links.')
    if s == 2:
        st = R.choice([100, 1000, 10 ** 4])
        n = _neun(R, R.choice([5, 6, 7]), st)
        r = runde(n, st)
        return Z(f'Runde {zt(n)} auf {STELLEN[st]}.', r, f'({n} + {st // 2}) // {st} * {st}',
                 f'Aufrunden an der {STELLE_KURZ[st]} (dort 9): Übertrag nach links. {zt(n)} ≈ {zt(r)}.', 'Denk an das Zählen von 99 auf 100.')
    k = art('runden_uebertrag', ['auswahl', 'welche', 'nullen', 'fehler'])
    if k == 'auswahl':
        n = R.choice([99_951, 199_960, 49_970, 999_650, 29_982])
        st = 100 if n % 1000 > 900 else 1000
        r = runde(n, st)
        falsch = [n // st * st, int(str(n // st) + str(st)[:-1] + '0'), r - st]
        return A(R, f'Runde {zt(n)} auf {STELLEN[st]}. Welche Lösung stimmt?', zt(r), [zt(f) for f in falsch],
                 f'Rechts neben der Rundungsstelle steht {ziffer_an(n, st // 10)}: aufrunden. Die Neunen werden zu Nullen, vorne kommt 1 dazu: {zt(r)}.',
                 'Aus 9 + 1 wird 10: Schreib 0 und gib 1 nach links weiter – so lange, bis keine 9 mehr kommt.')
    if k == 'welche':
        ziel = R.choice([400_000, 100_000, 700_000, 30_000])
        st = 1000
        opts = [ziel - 501, ziel - 500, ziel + 500, ziel - 1500]
        richtig = [o for o in opts if runde(o, st) == ziel]
        if len(richtig) != 1: return g_runden_uebertrag(R, 3)
        return A(R, f'Welche Zahl ergibt auf Tausender gerundet {zt(ziel)}?', zt(richtig[0]), [zt(o) for o in opts if o != richtig[0]],
                 f'{zt(richtig[0])} wird aufgerundet (Hunderterziffer 5), und der Übertrag läuft bis {zt(ziel)}. Die anderen ergeben {", ".join(zt(runde(o, st)) for o in opts if o != richtig[0])}.',
                 'Runde jede Zahl auf Tausender.')
    if k == 'nullen':
        n = R.choice([9_999_950, 999_960, 99_995, 49_999_700, 1_999_980])
        st = 100 if n % 1000 >= 900 and n % 100 >= 50 else 10
        r = runde(n, st)
        return Z(f'Runde {zt(n)} auf {STELLEN[st]}. Wie viele Nullen hat das Ergebnis?', str(r).count('0'), str(str(r).count('0')),
                 f'{zt(n)} ≈ {zt(r)}: Der Übertrag läuft durch alle Neunen. Das Ergebnis hat {str(r).count("0")} Nullen.', 'Schreibe das gerundete Ergebnis ganz aus.')
    n = R.choice([6975, 3896, 1998, 8997, 4995])
    st = 10
    r = runde(n, st)
    t = str(n)
    falsch_text = t[:2] + '(10)0'
    return A(R, f'Jemand rundet {zt(n)} auf Zehner und schreibt „{falsch_text}“. Was ist richtig?', zt(r),
             [falsch_text.replace('(10)', '10'), zt(n // 10 * 10), zt(r + 100)],
             f'Aus {t[2]} Zehnern + 1 werden {int(t[:3]) + 1} Zehner: {zt(r)}. Eine Stelle kann nie „10“ enthalten.',
             'Eine Stelle kann nur eine Ziffer von 0 bis 9 haben. Was passiert mit der 10?')


# ---------------- 9 Wann darf man runden? ----------------
JA = ['die Zahl der Zuschauer bei einem Fußballspiel', 'die Einwohnerzahl einer Stadt', 'die Entfernung von München nach Berlin', 'die Zahl der Haare auf dem Kopf',
      'die Länge eines Flusses', 'die Zahl der Besucher eines Freizeitparks im Jahr', 'die Höhe eines Berges in einer Erzählung', 'die Zahl der Bäume in einem Wald']
NEIN = ['die Telefonnummer der Oma', 'die Geheimzahl (PIN) einer Karte', 'die Hausnummer', 'die Postleitzahl', 'die Zimmernummer im Hotel', 'der Code eines Zahlenschlosses',
        'die Nummer des Sitzplatzes im Zug', 'die Kontonummer']


def g_runden_sinnvoll(R, s):
    if s == 1:
        if R.random() < .5:
            k = R.choice(JA)
            return A(R, f'Ist Runden hier sinnvoll: {k}?', 'Ja, ungefähr reicht.', ['Nein, die Zahl muss genau stimmen.', 'Nein, man darf nie runden.'],
                     f'Bei {k} reicht ein ungefährer Wert.', 'Muss die Zahl genau stimmen, oder reicht ungefähr?')
        k = R.choice(NEIN)
        return A(R, f'Ist Runden hier sinnvoll: {k}?', 'Nein, die Zahl muss genau stimmen.', ['Ja, ungefähr reicht.', 'Ja, auf Hunderter.'],
                 f'{k[0].upper() + k[1:]} muss genau stimmen, sonst ist sie nutzlos.', 'Was passiert, wenn die Zahl nur ungefähr stimmt?')
    if s == 2:
        k = R.choice(['angabe', 'paar'])
        if k == 'angabe':
            n = zahl_mit(R, 7)
            g = runde(n, 10 ** 5)
            mio, rest = divmod(g, 10 ** 6)
            angabe = f'etwa {mio},{rest // 10 ** 5} Millionen' if rest else f'etwa {mio} Millionen'
            return A(R, f'Eine Stadt hat {zt(n)} Einwohner. Welche Angabe für eine Zeitungsüberschrift ist sinnvoll gerundet?', angabe,
                     [f'etwa {zt(runde(n, 10))}', f'etwa {zt(n // 10 ** 6)} Millionen' if rest else f'etwa {zt(n // 10 ** 6 + 1)} Millionen', f'genau {zt(n)}'],
                     f'Für eine Überschrift genügt ein grober Wert: auf Hunderttausender gerundet {zt(g)}, also {angabe}.', 'Eine Überschrift soll man sich leicht merken können.')
        j, n = R.choice(JA), R.choice(NEIN)
        return A(R, 'Bei welcher Zahl ist Runden sinnvoll?', j, [n, R.choice([x for x in NEIN if x != n])],
                 f'{j[0].upper() + j[1:]}: ungefähr reicht. Nummern und Codes müssen genau stimmen.', 'Welche Zahl ist eine Menge, welche eine Nummer?')
    k = art('runden_sinnvoll', ['hoechstens', 'mindestens', 'unterschied', 'aufzug'])
    if k in ('hoechstens', 'mindestens'):
        z = R.choice([45_000, 72_000, 18_000, 63_000, 9000])
        st = 1000
        werte = [n for n in range(z - st, z + st) if runde(n, st) == z]
        if k == 'hoechstens':
            return Z(f'In der Zeitung steht: „rund {zt(z)} Zuschauer“ (auf Tausender gerundet). Wie viele Zuschauer waren es höchstens?', max(werte), str(max(werte)),
                     f'Auf {zt(z)} gerundet werden die Zahlen von {zt(min(werte))} bis {zt(max(werte))}. Höchstens {zt(max(werte))}.', 'Ab welcher Zahl würde man schon auf den nächsten Tausender runden?')
        return Z(f'In der Zeitung steht: „rund {zt(z)} Zuschauer“ (auf Tausender gerundet). Wie viele Zuschauer waren es mindestens?', min(werte), str(min(werte)),
                 f'Auf {zt(z)} gerundet werden die Zahlen von {zt(min(werte))} bis {zt(max(werte))}. Mindestens {zt(min(werte))}.', 'Ab welcher Zahl wird auf diesen Wert aufgerundet?')
    if k == 'unterschied':
        z, st = R.choice([(300, 100), (5000, 1000), (80, 10), (20_000, 10_000)])
        werte = [n for n in range(1, z + st) if runde(n, st) == z]
        return Z(f'Zwei Zahlen ergeben auf {STELLEN[st]} gerundet beide {zt(z)}. Wie groß kann ihr Unterschied höchstens sein?', max(werte) - min(werte), f'{max(werte)} - {min(werte)}',
                 f'Die kleinste mögliche Zahl ist {zt(min(werte))}, die größte {zt(max(werte))}. Unterschied: {zt(max(werte) - min(werte))}.', 'Nimm die kleinste und die größte Zahl, die zu diesem Rundungswert passen.')
    pers, kg, last = R.choice([(8, 80, 630), (6, 70, 400), (10, 70, 680), (5, 90, 450)])
    maxi = pers * (kg + 4)
    sicher = maxi <= last
    return A(R, f'Ein Aufzug trägt höchstens {last} kg. {pers} Personen wiegen „jeweils rund {kg} kg“ (auf Zehner gerundet). Kann man sicher sein, dass der Aufzug nicht überladen ist?',
             'Ja, sicher.' if sicher else 'Nein: Jeder kann bis zu ' + str(kg + 4) + f' kg wiegen, zusammen bis zu {zt(maxi)} kg.',
             ['Ja, ' + str(pers) + ' · ' + str(kg) + f' kg = {zt(pers * kg)} kg.', 'Nein, gerundete Zahlen kann man nie verwenden.', f'Ja, gerundete Werte sind immer zu groß.'],
             f'„Rund {kg} kg“ heißt {kg - 5} bis {kg + 4} kg. Im schlimmsten Fall {pers} · {kg + 4} kg = {zt(maxi)} kg. ' + ('Das ist noch erlaubt.' if sicher else f'Das ist mehr als {last} kg.'),
             'Rechne mit dem größten Gewicht, das hinter „rund“ stecken kann.')


# ---------------- 10 Keine größte Zahl ----------------
def g_unendlich(R, s):
    if s == 1:
        n = R.choice([10 ** k - 1 for k in range(3, 7)] + [R.randint(1, 9) * 10 ** k + 10 ** (k - 1) - 1 for k in range(3, 6)])
        if n == 999_999_999: return g_unendlich(R, 1)
        if R.random() < .5:
            return Z(f'Wie heißt der Nachfolger von {zt(n)}?', n + 1, f'{n} + 1', f'{zt(n)} + 1 = {zt(n + 1)}.', 'Nachfolger heißt: 1 dazuzählen.')
        m = n + 1
        return Z(f'Wie heißt der Vorgänger von {zt(m)}?', m - 1, f'{m} - 1', f'{zt(m)} − 1 = {zt(m - 1)}.', 'Vorgänger heißt: 1 abziehen.')
    if s == 2:
        k = R.choice(['groesst', 'kleinst', 'nachfolger_gross'])
        st = R.randint(5, 9)
        if k == 'groesst':
            return Z(f'Wie heißt die größte {st}-stellige Zahl?', 10 ** st - 1, f'10**{st} - 1', f'Lauter Neunen: {zt(10 ** st - 1)}. Ihr Nachfolger hat schon {st + 1} Stellen.', 'Welche Ziffer ist die größte?')
        if k == 'kleinst':
            return Z(f'Wie heißt die kleinste {st}-stellige Zahl?', 10 ** (st - 1), f'10**{st - 1}', f'Eine 1 und dahinter Nullen: {zt(10 ** (st - 1))}.', 'Vorne darf keine 0 stehen.')
        n = R.randint(1, 9) * 10 ** st + 10 ** (st - 2) - 1
        return Z(f'Wie heißt der Nachfolger von {zt(n)}?', n + 1, f'{n} + 1', f'{zt(n)} + 1 = {zt(n + 1)}. Die Neunen werden zu Nullen.', 'Achte auf die Neunen am Ende.')
    k = art('unendlich', ['nachfolger', 'zwischen', 'behauptung', 'anzahl'])
    if k == 'nachfolger':
        n = R.randint(2, 9) * 10 ** 6 + R.choice([99_999, 999_999 - 10 ** 5 * R.randint(1, 8)])
        return Z(f'Gib den Nachfolger von {zt(n)} an.', n + 1, f'{n} + 1', f'{zt(n)} + 1 = {zt(n + 1)}: Alle Neunen am Ende werden zu Nullen.', 'Von rechts: 9 + 1 = 10, Übertrag nach links.')
    if k == 'zwischen':
        a, b = R.choice([(999, 10_000), (99, 1000), (9999, 100_000), (100, 1000)])
        return Z(f'Wie viele natürliche Zahlen liegen zwischen {zt(a)} und {zt(b)}? Die beiden Zahlen selbst zählen nicht mit.', b - a - 1, f'{b} - {a} - 1',
                 f'Von {zt(a + 1)} bis {zt(b - 1)}: {zt(b - 1)} − {zt(a + 1)} + 1 = {zt(b - a - 1)} Zahlen.', 'Vorsicht: b − a zählt die Schritte, nicht die Zahlen dazwischen.')
    if k == 'behauptung':
        x = R.choice(['eine Milliarde Milliarden', 'eine Zahl mit hundert Neunen', 'eine Billion', 'die Zahl, die ein Computer gerade noch speichern kann'])
        return A(R, f'Jemand sagt: „Die größte natürliche Zahl ist {x}.“ Stimmt das?', 'Nein: Zählt man 1 dazu, erhält man eine größere natürliche Zahl.',
                 ['Ja, größer geht es nicht.', 'Ja, aber nur ungefähr.', 'Nein, die größte ist 999 999 999.'],
                 f'Zu jeder natürlichen Zahl, auch zu {x}, gibt es den Nachfolger (+ 1). Darum gibt es keine größte.', 'Was passiert, wenn du 1 dazuzählst?')
    st = R.randint(3, 7)
    return Z(f'Wie viele natürliche Zahlen haben genau {st} Stellen?', 9 * 10 ** (st - 1), f'10**{st} - 10**{st - 1}',
             f'Von {zt(10 ** (st - 1))} bis {zt(10 ** st - 1)}: {zt(10 ** st)} − {zt(10 ** (st - 1))} = {zt(9 * 10 ** (st - 1))} Zahlen.', 'Kleinste und größte Zahl mit dieser Stellenzahl bestimmen.')


# ---------------- 11 Römische Zahlen schreiben ----------------
def _T(text, antwort, w, h):
    return {'y': 'text', 'f': {'text': text}, 'o': {'text': antwort}, 'w': w, 'h': h}


def _zerlegung(n):
    teile = [n // 1000 * 1000, n // 100 % 10 * 100, n // 10 % 10 * 10, n % 10]
    return ' + '.join(zt(t) for t in teile if t)


def g_roemisch_schreiben(R, s):
    if s == 1:
        n = R.randint(4, 49)
        if n == 39: return g_roemisch_schreiben(R, 1)
        if R.random() < .5:
            return _T(f'Schreibe {n} als römische Zahl.', roem(n), f'Zerlegt: {n} = {_zerlegung(n)}. Jeden Teil übersetzen: {roem(n)}.', 'Zerlege in Zehner und Einer. Denk an IV, IX, XL.')
        return Z(f'Welche Zahl ist {roem(n)}?', n, str(roem_wert(roem(n))), f'Zeichen von links lesen: {roem(n)} = {_zerlegung(n)} = {n}.', 'Steht ein kleineres Zeichen vor einem größeren, wird es abgezogen.')
    if s == 2:
        n = R.randint(50, 3999)
        if len(roem(n)) > 12: return g_roemisch_schreiben(R, 2)
        if R.random() < .5:
            return _T(f'Schreibe {zt(n)} als römische Zahl.', roem(n), f'{zt(n)} = {_zerlegung(n)} → {roem(n)}.', 'Erst die Tausender, dann Hunderter, Zehner, Einer – jeweils einzeln übersetzen.')
        return Z(f'Welche Zahl ist {roem(n)}?', n, str(roem_wert(roem(n))), f'{roem(n)} = {_zerlegung(n)} = {zt(n)}.', 'Lies von links. Erlaubte Paare: IV, IX, XL, XC, CD, CM.')
    k = art('roemisch_schreiben', ['jahr', 'auswahl', 'meiste', 'rechnen'])
    if k == 'jahr':
        j = R.randint(1490, 1999)
        return Z(f'Über einem Tor steht die Jahreszahl {roem(j)}. Welches Jahr ist das?', j, str(roem_wert(roem(j))), f'{roem(j)} = {_zerlegung(j)} = {j}.',
                 'Teile in Gruppen: M…, dann C/D, dann X/L, dann I/V.')
    if k == 'auswahl':
        n = R.choice([490, 99, 45, 1990, 999, 4, 49, 1444, 2900, 95])
        falsch = {490: ['XD', 'CCCCXC', 'LD'], 99: ['IC', 'XCVIIII', 'IXC'], 45: ['VL', 'XXXXV', 'XLIIIII'], 1990: ['MXM', 'MCMLXXXX', 'MCMXCX'],
                  999: ['IM', 'CMXCIX ', 'DCCCCXCIX'], 4: ['IIII', 'VI', 'IIV'], 49: ['IL', 'XLVIIII', 'XXXXIX'], 1444: ['MCDXLIIII', 'MCCCCXLIV', 'MCDXXXXIV'],
                  2900: ['MMDCCCC', 'MMCMM', 'CMMM'], 95: ['VC', 'LXXXXV', 'XCIIIII']}[n]
        falsch = [f.strip() for f in falsch if f.strip() != roem(n)]
        return A(R, f'Welche römische Schreibweise ist richtig für {zt(n)}?', roem(n), falsch,
                 f'{zt(n)} = {_zerlegung(n)} → {roem(n)}. Abziehen gibt es nur bei IV, IX, XL, XC, CD, CM; kein Zeichen viermal.',
                 'Zerlege in Tausender, Hunderter, Zehner, Einer und übersetze jeden Teil.')
    if k == 'meiste':
        bis = R.choice([50, 100, 200, 500])
        lang = max(range(1, bis + 1), key=lambda x: (len(roem(x)), x))
        return Z(f'Welche Zahl von 1 bis {bis} braucht als römische Zahl die meisten Zeichen?', lang, str(roem_wert(roem(lang))),
                 f'{zt(lang)} = {roem(lang)} hat {len(roem(lang))} Zeichen – mehr hat keine Zahl bis {bis}. Je Stelle am längsten ist die 8 (VIII, LXXX, DCCC).',
                 'Welche Ziffer braucht römisch die meisten Zeichen? Probiere 8, 38, 88 …')
    a, b = R.randint(11, 60), R.randint(11, 60)
    return _T(f'Rechne und schreibe das Ergebnis römisch: {roem(a)} + {roem(b)}', roem(a + b), f'{roem(a)} = {a}, {roem(b)} = {b}. {a} + {b} = {a + b} = {roem(a + b)}.',
              'Übersetze beide Zahlen, rechne und übersetze zurück.')


# ---------------- 12 Stellenwertsystem und römisch ----------------
def g_roemisch_system(R, s):
    if s == 1:
        if R.random() < .5:
            d = R.randint(2, 9)
            n = int(str(d) * 4)
            st = R.choice([1000, 100, 10])
            return Z(f'Welchen Wert hat die Ziffer {d} an der {STELLE_KURZ[st]} von {zt(n)}?', d * st, f'{d} * {st}', f'An der {STELLE_KURZ[st]}: {d} · {zt(st)} = {zt(d * st)}.',
                     'Im Zehnersystem hängt der Wert von der Stelle ab.')
        zeichen, wert = R.choice([('X', 10), ('C', 100), ('M', 1000), ('L', 50), ('V', 5)])
        n = roem_wert(zeichen * 2) if zeichen in 'XCM' else wert + R.choice([1, 2, 3])
        rz = roem(n)
        if zeichen not in rz: return g_roemisch_system(R, 1)
        return Z(f'Wie viel ist das Zeichen {zeichen} in der Zahl {rz} wert?', wert, str(wert), f'Ein römisches Zeichen hat immer seinen Grundwert: {zeichen} = {wert}.',
                 'Römische Zeichen ändern ihren Wert nicht mit der Stelle.')
    if s == 2:
        k = R.choice(['groesst', 'null'])
        if k == 'groesst':
            d = R.randint(2, 9)
            zahlen = []
            for pos in R.sample(range(4), 3):
                while True:
                    z = [R.randint(1, 9)] + [R.randint(0, 9) for _ in range(3)]
                    z[pos] = d
                    if z.count(d) == 1 and z[0] != 0: break
                zahlen.append(int(''.join(map(str, z))))
            wert = lambda z: d * 10 ** (len(str(z)) - 1 - str(z).index(str(d)))
            best = max(zahlen, key=wert)
            return A(R, f'In welcher Zahl hat die Ziffer {d} den größten Wert?', zt(best), [zt(z) for z in zahlen if z != best],
                     'Werte der Ziffer: ' + ', '.join(f'{zt(z)}: {zt(wert(z))}' for z in zahlen) + f'. Am größten in {zt(best)}.', 'Alle Zahlen sind vierstellig. Je weiter links die Ziffer steht, desto mehr ist sie wert.')
        n = R.choice([205, 3007, 1040, 608, 2050, 1009, 3600])
        return A(R, f'Warum braucht {zt(n)} mit Ziffern eine 0, die römische Schreibweise {roem(n)} aber nicht?',
                 'Die 0 hält im Stellenwertsystem eine leere Stelle frei. Römische Zeichen haben feste Werte und brauchen keinen Platzhalter.',
                 ['Die Römer kannten die Zahl nicht.', 'Römische Zahlen sind immer kürzer.', 'Die 0 ist im Zehnersystem nichts wert und könnte wegfallen.'],
                 f'Ohne 0 würde aus {zt(n)} eine andere Zahl. Römisch gibt es keine Stellen, also auch keine leeren.', 'Was passiert, wenn man die 0 weglässt?')
    k = art('roemisch_system', ['aussage', 'zeichen_zaehlen', 'tauschen', 'anhaengen'])
    if k == 'aussage':
        return A(R, 'Welche Aussage über römische Zahlen stimmt?', 'Das Zeichen X ist immer 10 wert; es wird je nach Lage addiert oder abgezogen.',
                 ['Das Zeichen X ist ganz links mehr wert als ganz rechts.', 'Römische Zahlen brauchen eine 0 als Platzhalter.', 'Jede römische Zahl ist kürzer als die Zahl mit Ziffern.'],
                 'Römische Zeichen haben feste Grundwerte. XIX = 10 + (10 − 1): beide X sind 10 wert, das I wird abgezogen.', 'Prüfe jede Aussage an einem Beispiel wie XIX oder 1 888.')
    if k == 'zeichen_zaehlen':
        n = R.choice([3333, 2888, 1777, 3838, 2333, 1888])
        return L(f'Wie viele Zeichen braucht {zt(n)} mit Ziffern und wie viele als römische Zahl?', 'Ziffern: □; römisch: □', [len(str(n)), len(roem(n))],
                 [str(len(str(n))), str(len(roem(n)))], f'{zt(n)} hat {len(str(n))} Ziffern. Römisch: {roem(n)} – das sind {len(roem(n))} Zeichen.', 'Schreibe die römische Zahl auf und zähle.', HF)
    if k == 'tauschen':
        a, b = R.choice([('X', 'I'), ('V', 'I'), ('L', 'X'), ('C', 'X'), ('D', 'C'), ('M', 'C')])
        vorher, nachher = a + b, b + a
        return Z(f'Vertauscht man in {vorher} die beiden Zeichen, entsteht {nachher}. Um wie viel wird der Wert kleiner?', roem_wert(vorher) - roem_wert(nachher),
                 f'{roem_wert(vorher)} - {roem_wert(nachher)}', f'{vorher} = {roem_wert(vorher)}, {nachher} = {roem_wert(nachher)}. Unterschied: {roem_wert(vorher) - roem_wert(nachher)}.',
                 'Steht das kleinere Zeichen links, wird es abgezogen.')
    z = R.choice(['XX', 'CC', 'MM'])
    return A(R, f'Hängt man an die Zahl 20 rechts eine 0 an, wird sie zehnmal so groß. Was passiert, wenn man an {z} rechts ein {z[0]} anhängt?',
             f'Der Wert wächst nur um {roem_wert(z[0])}: {z}{z[0]} = {roem_wert(z + z[0])}.',
             [f'Der Wert wird zehnmal so groß: {zt(roem_wert(z) * 10)}.', f'Der Wert verdoppelt sich: {zt(roem_wert(z) * 2)}.', 'Das ist nicht erlaubt.'],
             f'{z} = {roem_wert(z)}. Das neue {z[0]} zählt einfach {roem_wert(z[0])} dazu: {roem_wert(z + z[0])}. Römisch verschiebt sich nichts – es gibt keine Stellen.',
             'Ein römisches Zeichen hat immer denselben Wert, egal wo es steht.')


GEN = {'stellenwert': g_stellenwert, 'zahlwort_zu_ziffern': g_zahlwort_zu_ziffern, 'ziffern_zu_zahlwort': g_ziffern_zu_zahlwort,
       'strahl_ablesen': g_strahl_ablesen, 'strahl_eintragen': g_strahl_eintragen, 'vergleichen': g_vergleichen, 'runden_regel': g_runden_regel,
       'runden_uebertrag': g_runden_uebertrag, 'runden_sinnvoll': g_runden_sinnvoll, 'unendlich': g_unendlich,
       'roemisch_schreiben': g_roemisch_schreiben, 'roemisch_system': g_roemisch_system}
# Beispiele der Lernkarten nicht als Aufgabe wiederholen
VERBOT = {'stellenwert': ['von 4 052'], 'zahlwort_zu_ziffern': ['zwölf Millionen achttausend'], 'ziffern_zu_zahlwort': ['3 040 500'],
          'vergleichen': ['90 909', '90 990'], 'runden_regel': ['3 472 auf'], 'runden_uebertrag': ['2 995 auf'], 'roemisch_schreiben': ['Schreibe 39 ']}

if __name__ == '__main__':
    d = baue(META, ETAPPEN, GEN,
             [('Stellenwerte und große Zahlen', ['stellenwert', 'zahlwort_zu_ziffern', 'ziffern_zu_zahlwort']),
              ('Zahlenstrahl und Vergleichen', ['strahl_ablesen', 'strahl_eintragen', 'vergleichen']),
              ('Runden', ['runden_regel', 'runden_uebertrag', 'runden_sinnvoll']),
              ('Zahlsysteme', ['unendlich', 'roemisch_schreiben', 'roemisch_system'])],
             'Große natürliche Zahlen lesen, schreiben und am Zahlenstrahl darstellen, vergleichen und runden; das Zehnersystem mit römischen Zahlen vergleichen.',
             ['Der Wert einer Ziffer hängt von ihrer Stelle ab.', 'Große Zahlen in Dreiergruppen: Milliarden | Millionen | Tausender | Einer.',
              'Zahlenstrahl: erst den Abschnittswert bestimmen.', 'Runden: 0–4 ab, 5–9 auf.', 'Zu jeder natürlichen Zahl gibt es einen Nachfolger.',
              'Römische Zeichen haben feste Werte; Abziehen nur bei IV, IX, XL, XC, CD, CM.'],
             verbot=VERBOT, plan=PLAN, seed=15012,
             offen=['Zwölfte Runde: Thema stammt aus der Zeit vor dem Bausatz; die bisherigen Aufgaben liegen nur in der Datenbank. Dieser Generator erzeugt neue Aufgaben '
                    '(je Lernkarte 18 Übungen 4/6/8, 1 Test, 3 Korrektur, 6 Sicherung), die beim Einspielen mit einheit_abgleichen(…, \'lassen\') dazukommen. '
                    'Dubletten zu den alten Aufgaben ließen sich nicht prüfen; Beispielzahlen der Lernkarten (quelle.md) sind ausgeschlossen.',
                    'Römische Zahlen als Textantwort (Groß-/Kleinschreibung egal) nur bis 12 Zeichen; längere als Auswahl.'])
    d['autor'] = 'Claude (Zwölfte Runde, Generator zahlen_natuerlich.py)'
    d['inhalt']['quellen']['aufgaben'] = 'Vom Generator erzeugt und berechnet (Zwölfte Runde); Stufe 3 teils nach Prüfungsvorbild (Jahrgangsstufentest 6 Bayern, Probeunterricht Gym 5), eigene Zahlen.'
    # ---- DURCHSICHT (Neunzehnte Runde, Zweig durchsicht-kl5, siehe _durchsicht_kl5.py) ----
    from _durchsicht_kl5 import Durchsicht, durchsicht_anwenden
    DS = Durchsicht('zahlen.natuerlich', 19_5_1)
    # a) Stufe 3 mit gleichem Gedanken wie Stufe 2, nur größere Zahlen → Stufe 2
    DS.stufe('strahl_ablesen', 'Welche Zahl zeigt der Pfeil?', 2, enthaelt=lambda x: x['s'] == 3, anzahl=4)
    for _t in ['Tippe die Markierung an, an der 140 000 liegt.', 'Tippe die Markierung an, an der 1 300 000 liegt.']:
        DS.stufe('strahl_eintragen', _t, 2)
    for _t in ['Gib den Nachfolger von 2 099 999 an.', 'Gib den Nachfolger von 9 099 999 an.']:
        DS.stufe('unendlich', _t, 2)
    for _t in ['Über einem Tor steht die Jahreszahl MCMXXXI. Welches Jahr ist das?', 'Über einem Tor steht die Jahreszahl MDCCXCIX. Welches Jahr ist das?']:
        DS.stufe('roemisch_schreiben', _t, 2)
    # c) Zwei richtige Antworten: „etwa 8 Millionen“ ist ebenfalls sinnvoll gerundet (auf Millionen). Neue Frage legt die Rundungsstelle fest.
    _alt = 'Eine Stadt hat {} Einwohner. Welche Angabe für eine Zeitungsüberschrift ist sinnvoll gerundet?'
    for _n, _pool in [(8495588, 'uebung'), (8212268, 'uebung'), (3080713, 'uebung'), (8181056, 'uebung'), (6205029, 'korrektur'), (5240931, 'sicherung')]:
        _g = runde(_n, 10 ** 5)
        _ab = _n // 10 ** 5 * 10 ** 5
        _falsch = _g + 10 ** 5 if _ab == _g else _ab
        _mio = lambda x: f'etwa {x // 10 ** 6},{x % 10 ** 6 // 10 ** 5} Millionen' if x % 10 ** 6 else f'etwa {x // 10 ** 6} Millionen'
        DS.ersetze('runden_sinnvoll', _alt.format(zt(_n)), DS.A(
            f'Eine Stadt hat {zt(_n)} Einwohner. Für die Zeitung wird auf Hunderttausender gerundet. Welche Angabe ist richtig?',
            _mio(_g), [_mio(_falsch), f'etwa {zt(runde(_n, 10))}', f'genau {zt(_n)}'],
            f'Rundungsstelle: Hunderttausender. Rechts daneben steht {_n // 10 ** 4 % 10}, also {"aufrunden" if _g > _ab else "abrunden"}: {zt(_g)}, das sind {_mio(_g)[5:]}.',
            'Suche die Hunderttausenderstelle und schau die Ziffer rechts daneben an.'), pools=(_pool,))
    # d) Stufe 3 bei strahl_ablesen: rückwärts denken statt größerer Zahlen
    DS.neu('strahl_ablesen', 3, DS.Z(
        'Ein Zahlenstrahl hat gleich große Abschnitte. Zwei Abschnitte nach dem Anfang steht 300, sechs Abschnitte nach dem Anfang steht 500. Welche Zahl steht neun Abschnitte nach dem Anfang?',
        650, '500 + 3 * ((500 - 300) // 4)', 'Von 300 bis 500 sind es 4 Abschnitte: 200 : 4 = 50 je Abschnitt. Von 6 bis 9 sind es 3 Abschnitte: 500 + 3 · 50 = 650.',
        'Wie viele Abschnitte liegen zwischen 300 und 500? Wie viel ist dann einer wert?'))
    DS.neu('strahl_ablesen', 3, DS.Z(
        'Ein Zahlenstrahl beginnt bei 1 000 und hat 8 gleich große Abschnitte. Drei Abschnitte nach dem Anfang steht 1 450. Bei welcher Zahl endet der Strahl?',
        2200, '1000 + 8 * ((1450 - 1000) // 3)', 'Bis 1 450 sind es 450 in 3 Abschnitten: 450 : 3 = 150 je Abschnitt. Ende: 1 000 + 8 · 150 = 2 200.',
        'Rechne zuerst aus, wie viel ein Abschnitt wert ist.'))
    durchsicht_anwenden(d, DS)
    # ---- DURCHSICHT ENDE ----
    # ---- STUFEN (Zwanzigste Runde, Zweig stufen-kl5, siehe _stufen_kl5.py und _st5_zahlen_natuerlich.py) ----
    from _stufen_kl5 import stufen_anwenden
    stufen_anwenden(d, 'zahlen.natuerlich')
    # ---- STUFEN ENDE ----
    pfad = Path(__file__).resolve().parent.parent / 'themen' / 'zahlen.natuerlich.json'
    import json
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


# ---- AUFLOESEN (Vierundzwanzigste Runde, Zweig aufloesen, siehe _aufloesen.py und _af_plan.py) ----
if __name__ == '__main__':
    from _aufloesen import aufloesen_datei
    aufloesen_datei('zahlen.natuerlich')
# ---- AUFLOESEN ENDE ----
