"""Gemeinsame Helfer für die Expeditionen Klasse 8 (Werkstatt-Wunsch 176, Auftrag „Expeditionen“, Zweig expedition-kl8).

Jede Expedition hat ihren eigenen Generator expedition_<name>.py; hier stehen nur Zahlformat, Bausteine und Schreiben.
Alle Lösungen werden mit Fraction exakt berechnet; der Rechenausdruck c wird beim Schreiben mit demselben Rechner
wie in tools/inhalt_pruefen.py nachgerechnet."""
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools'))
from inhalt_pruefen import rechne, zahlwert  # noqa: E402

AUTOR = 'Claude (Auftrag Expeditionen Klasse 8)'
PI = '3.141592653589793'


def zt(x, stellen=None):
    """Zahl deutsch: Dezimalkomma, Minus −, Tausender mit schmalem Leerzeichen ab 10 000."""
    x = Fr(x)
    if stellen is not None:
        s = f'{float(x):.{stellen}f}'
    elif x.denominator == 1:
        s = str(x.numerator)
    else:
        s = f'{float(x):.6f}'.rstrip('0').rstrip('.')
    ganz, _, rest = s.lstrip('-').partition('.')
    if len(ganz) > 4: ganz = f'{int(ganz):,}'.replace(',', ' ')
    s = ('−' if s.startswith('-') else '') + ganz + (',' + rest if rest else '')
    return s


def jw(x):
    x = Fr(x)
    return x.numerator if x.denominator == 1 else float(x)


def B(thema, lz): return {'thema_schluessel': thema, 'lernziel': lz}


def zahl(k, text, wert, c, w, h, bezug, einheit=None, toleranz=None, grafik=None):
    assert rechne(c) == Fr(wert), f'Teil {k}: {c} = {rechne(c)}, Lösung {wert}'
    o = {'wert': jw(wert)}
    if einheit: o['einheit'] = einheit
    if toleranz is not None: o['toleranz'] = toleranz
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    return {'k': k, 'y': 'zahl', 'f': f, 'o': o, 'c': c, 'w': w, 'h': h, 'bezug': bezug}


def luecken(k, text, schablone, hinweis, werte, c, w, h, bezug, grafik=None):
    assert [rechne(x) for x in c] == [Fr(v) for v in werte], f'Teil {k}: {c} ≠ {werte}'
    f = {'text': text, 'schablone': schablone, 'hinweis': hinweis}
    if grafik: f['grafik'] = grafik
    return {'k': k, 'y': 'luecken', 'f': f, 'o': {'werte': [jw(v) for v in werte]}, 'c': c, 'w': w, 'h': h, 'bezug': bezug}


def auswahl(k, text, richtig, falsch, w, h, bezug, grafik=None, pos=0):
    """Antworten: richtig an Stelle pos, falsche in gegebener Reihenfolge."""
    a = list(falsch); a.insert(pos, richtig)
    assert len(set(a)) == len(a) and 2 <= len(a) <= 4
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    return {'k': k, 'y': 'auswahl', 'f': f, 'a': a, 'o': {'index': pos}, 'w': w, 'h': h, 'bezug': bezug}


def schreibe(exp):
    ziel = WURZEL / 'inhalte' / 'expeditionen' / f'{exp["schluessel"]}.json'
    exp = {'schluessel': exp['schluessel'], 'klasse': {'gym_by': 8}, 'titel': exp['titel'], 'autor': AUTOR, **{k: v for k, v in exp.items() if k not in ('schluessel', 'titel')}}
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(json.dumps(exp, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(f'geschrieben: {ziel.name} ({len(exp["teile"])} Teile)')
