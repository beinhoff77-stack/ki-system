"""Korrektur neuer Aufgaben Kl. 7 (Prüfung nach der Zwanzigsten Runde und dem Bereinigen).

Wird als letzter Schritt eines Generators aufgerufen: korrektur_datei(thema, REGELN).
Eine Regel trifft Aufgaben über Lernkarte und Fragetext (regulärer Ausdruck) und ändert sie mit einer Funktion
(Aufgabe -> None, ändert an Ort und Stelle). Jede Regel muss genau `n` Aufgaben treffen. Geändert werden dürfen nur neue
Aufgaben (Fragetext gab es im Stand 4eda8cb in keiner Themendatei); g, s, p, l und y bleiben. Lösungen (Feld o) rechnet die
Funktion selbst aus den Zahlen der Aufgabe nach, wo sie sie ändert.
"""
import json
import re
import subprocess
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
THEMEN = WURZEL / 'inhalte' / 'themen'
_VORHER = None


def texte_vorher(stand='4eda8cb'):
    global _VORHER
    if _VORHER is None:
        g = lambda *a: subprocess.run(['git', '-C', str(WURZEL), *a], capture_output=True, check=True, text=True).stdout
        _VORHER = set()
        for f in g('ls-tree', '--name-only', stand, 'inhalte/themen/').split():
            if f.endswith('.json'):
                _VORHER |= {a['f']['text'] for a in json.loads(g('show', f'{stand}:{f}')).get('aufgaben', [])}
    return _VORHER


def regel(lz, muster, fn, n=1, pool=None):
    return (lz, muster, fn, n, pool)


def ersetze_in(feld, alt, neu, regex=False):
    """Hilfsfunktion: ersetzt in einem Textfeld ('text', 'w', 'h' oder 'a<i>' für Antwortoption i); alt muss vorkommen."""
    def f(a):
        if feld.startswith('a') and feld != 'a':
            i = int(feld[1:]); s = a['a'][i]
        elif feld == 'text': s = a['f']['text']
        else: s = a[feld]
        t = re.sub(alt, neu, s) if regex else s.replace(alt, neu)
        assert t != s, f'Ersetzung ohne Wirkung in {feld}: {alt[:50]}'
        if feld.startswith('a') and feld != 'a': a['a'][i] = t
        elif feld == 'text': a['f']['text'] = t
        else: a[feld] = t
    return f


def mehrere(*fs):
    def f(a):
        for x in fs: x(a)
    return f


def korrektur_datei(thema, regeln):
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    alt = texte_vorher()
    zaehl = 0
    for lz, muster, fn, n, pool in regeln:
        treffer = [a for a in d['aufgaben'] if a['l'] == lz and re.search(muster, a['f']['text']) and (pool is None or a['p'] == pool)]
        assert len(treffer) == n, f'KORREKTUR {thema}/{lz}: „{muster}“ trifft {len(treffer)} statt {n}'
        for a in treffer:
            assert a['p'] in ('uebung', 'bonus') and a['f']['text'] not in alt, f'KORREKTUR {thema}: alte Aufgabe getroffen: {a["f"]["text"][:60]}'
            vorher = {k: a.get(k) for k in ('g', 's', 'p', 'l', 'y')}
            fn(a)
            assert {k: a.get(k) for k in ('g', 's', 'p', 'l', 'y')} == vorher, f'KORREKTUR {thema}: g/s/p/l/y geändert'
            assert a['f']['text'] not in alt, f'KORREKTUR {thema}: neuer Text gleicht einer alten Aufgabe'
            zaehl += 1
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'  KORREKTUR {thema}: {zaehl} Aufgaben geändert')
    return d
