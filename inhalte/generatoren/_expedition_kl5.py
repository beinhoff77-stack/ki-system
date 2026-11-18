"""Gemeinsame Bausteine für die Expeditionen der Klasse 5 (Werkstatt-Wunsch 176, Auftrag „Expeditionen“).

Jeder Generator expedition_<name>.py baut seine Teile mit diesen Hilfen und schreibt inhalte/expeditionen/5-<name>.json.
Alle Lösungen rechnet das Programm; schreibe() prüft zusätzlich jede Nachrechnung „c“ mit dem Rechner des Prüfskripts.
"""
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WURZEL / 'tools'))
from inhalt_pruefen import rechne  # noqa: E402

AUTOR = 'Claude (Expeditionen Klasse 5)'


def zt(x):
    """Zahl deutsch: Tausendertrennung mit Leerzeichen, Dezimalkomma, Minus −."""
    x = Fr(x)
    neg = x < 0
    x = abs(x)
    if x.denominator == 1:
        s = f'{x.numerator:,}'.replace(',', ' ')
    else:
        g, r = divmod(x.numerator, x.denominator)
        nach = f'{float(Fr(r, x.denominator)):.6f}'[2:].rstrip('0')
        s = f'{g:,}'.replace(',', ' ') + ',' + nach
    return ('−' if neg else '') + s


def B(thema, lz):
    return {'thema_schluessel': thema, 'lernziel': lz}


def zahl(k, text, wert, c, w, h, bezug, einheit=None, grafik=None):
    assert rechne(c) == Fr(wert), (k, c, wert)
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    o = {'wert': int(wert) if Fr(wert).denominator == 1 else float(wert)}
    if einheit: o['einheit'] = einheit
    return {'k': k, 'y': 'zahl', 'f': f, 'o': o, 'c': c, 'w': w, 'h': h, 'bezug': bezug}


def auswahl(k, text, richtig, falsche, w, h, bezug, grafik=None, ordnung=None):
    """Antworten in fester Reihenfolge: ordnung = Liste aller Antworten (richtig muss darin vorkommen), sonst richtig an Position 0 + falsche."""
    alle = ordnung or [richtig] + list(falsche)
    assert richtig in alle and len(set(alle)) == len(alle) and 2 <= len(alle) <= 4, (k, alle)
    assert set(alle) == {richtig, *falsche}, (k, 'ordnung passt nicht zu richtig/falsche')
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    return {'k': k, 'y': 'auswahl', 'f': f, 'a': alle, 'o': {'index': alle.index(richtig)}, 'w': w, 'h': h, 'bezug': bezug}


def luecken(k, text, schablone, werte, c, hinweis, w, h, bezug, grafik=None):
    assert schablone.count('□') == len(werte) == len(c), k
    assert [rechne(x) for x in c] == [Fr(v) for v in werte], (k, c, werte)
    f = {'text': text, 'schablone': schablone, 'hinweis': hinweis}
    if grafik: f['grafik'] = grafik
    return {'k': k, 'y': 'luecken', 'f': f, 'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h, 'bezug': bezug}


def roemisch_wert(s):
    W = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    for i, ch in enumerate(s):
        v = W[ch]
        n += -v if i + 1 < len(s) and W[s[i + 1]] > v else v
    return n


_E = ['', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn',
      'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
_Z = ['', '', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']


def _bis999(n):
    h, r = divmod(n, 100)
    s = (_E[h] + 'hundert') if h else ''
    if r < 20: s += _E[r]
    else:
        z, e = divmod(r, 10)
        s += (_E[e] + 'und' if e else '') + _Z[z]
    return s


def zahlwort(n):
    """Zahlwort für 1 ≤ n < 1 000 000 (z. B. 531441 → fünfhunderteinunddreißigtausendvierhunderteinundvierzig)."""
    assert 0 < n < 1_000_000
    t, r = divmod(n, 1000)
    s = (_bis999(t) + 'tausend') if t else ''
    s += _bis999(r)
    return s + 's' if r % 100 == 1 else s


def schreibe(d):
    ziel = WURZEL / 'inhalte' / 'expeditionen' / f'{d["schluessel"]}.json'
    assert 3 <= len(d['teile']) <= 5
    vs = {(v['thema_schluessel'], v['lernziel']) for v in d['voraussetzungen']}
    for t in d['teile']:
        assert (t['bezug']['thema_schluessel'], t['bezug']['lernziel']) in vs, t['k']
    assert len({v[0] for v in vs}) >= 3, 'mindestens 3 verschiedene Themen'
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'geschrieben: {ziel.name} ({len(d["teile"])} Teile)')


def expedition(name, titel, einleitung, teile, grafik=None):
    """Voraussetzungen = die Bezüge der Teile in ihrer Reihenfolge (ohne Doppelte)."""
    vor = []
    for t in teile:
        if t['bezug'] not in vor: vor.append(t['bezug'])
    d = {'schluessel': f'5-{name}', 'klasse': {'gym_by': 5}, 'titel': titel, 'autor': AUTOR, 'einleitung': einleitung}
    if grafik: d['grafik'] = grafik
    d['voraussetzungen'] = vor
    d['teile'] = teile
    return d
