"""Zehnte Runde (Zweig schwer-kl9): schwerere Übungen nach Prüfungsvorbild an die Themen der Klasse 9 anhängen.

Jeder Generator ruft nach bauen(...) die Funktion anhaengen(datei, seed, liste) auf. Die neuen Aufgaben
entstehen erst danach mit eigenem festen Zufallsstart (seed); alle bisherigen Aufgaben bleiben dadurch
Zeichen für Zeichen gleich und stehen in derselben Reihenfolge vorn in der Datei. Neue Aufgaben: nur Pool
uebung, Stufe 2 oder 3, mit Tipp. Das Feld art ('pruefung', 'knobel' oder '') dient nur dem Bericht und
wird nicht in die Datei geschrieben.

Nachweis „alles Alte unverändert“:  python3 -I inhalte/generatoren/_schwer_kl9.py <thema> [...]
vergleicht inhalte/themen/<thema>.json mit dem Stand auf origin/lernen-app.
"""
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import THEMEN, _schluessel, start  # noqa: E402

BERICHT = Path(os.environ['SCHWER_ZAEHLUNG']) if os.environ.get('SCHWER_ZAEHLUNG') else None  # nur für den Bericht, nicht im Repository


def anhaengen(datei, seed, bauplan):
    """bauplan: Funktion ohne Argumente, die eine Liste (lernziel, stufe, art, aufgabe) liefert.
    Sie wird erst nach start(seed) aufgerufen, damit auch das Mischen der Auswahl-Antworten fest ist."""
    start(seed)
    neue = bauplan()
    lz = [e['lernziel'] for e in datei['inhalt']['etappen']]
    beispiele = set()
    for e in datei['inhalt']['etappen']:
        for s in e.get('schritte', []):
            beispiele.add(re.sub(r'\s+', ' ', s['text'] if isinstance(s, dict) else s))
    gesehen = {_schluessel(a) for a in datei['aufgaben']}
    zaehl = Counter()
    for l, s, art, a in neue:
        assert l in lz, ('Lernkarte gibt es nicht', l)
        assert a is not None, ('Aufgabe nicht gebaut', l)
        assert s in (2, 3), (l, s)
        assert art in ('pruefung', 'knobel', ''), art
        assert a.get('h'), ('Tipp fehlt', l, a['f']['text'][:40])
        assert a['f']['text'].strip() not in beispiele, ('gleich wie Beispiel', l)
        if a['y'] == 'zahl': assert 'c' in a, ('Rechenausdruck fehlt', l, a['f']['text'][:40])
        k = _schluessel(a)
        assert k not in gesehen, ('doppelt', l, a['f']['text'][:60])
        gesehen.add(k)
        t = a.pop('t', None) or l
        datei['aufgaben'].append({'l': l, 't': t, 'p': 'uebung', 's': s, **a})
        zaehl[(l, s, art)] += 1
    for l in lz:
        n3 = sum(v for (x, s, _), v in zaehl.items() if x == l and s == 3)
        n2 = sum(v for (x, s, _), v in zaehl.items() if x == l and s == 2)
        np_ = sum(v for (x, s, a), v in zaehl.items() if x == l and a == 'pruefung')
        nk = sum(v for (x, s, a), v in zaehl.items() if x == l and a == 'knobel')
        assert n3 >= 4 and n2 >= 2 and np_ >= 2, (datei['thema_schluessel'], l, n3, n2, np_)
        print(f'  {l}: +{n3} Stufe 3 ({np_} Prüfungsvorbild, {nk} Knobel), +{n2} Stufe 2')
    pfad = THEMEN / f'{datei["thema_schluessel"]}.json'
    pfad.write_text(json.dumps(datei, ensure_ascii=False, indent=1), encoding='utf-8')
    if BERICHT is None:
        print(f'{pfad.name}: {len(neue)} neue Übungen angehängt, jetzt {len(datei["aufgaben"])} Aufgaben')
        return datei
    try:
        alle = json.loads(BERICHT.read_text(encoding='utf-8'))
    except FileNotFoundError:
        alle = {}
    alle[datei['thema_schluessel']] = {l: {'stufe3': sum(v for (x, s, _), v in zaehl.items() if x == l and s == 3),
                                           'stufe2': sum(v for (x, s, _), v in zaehl.items() if x == l and s == 2),
                                           'pruefung': sum(v for (x, s, a), v in zaehl.items() if x == l and a == 'pruefung'),
                                           'knobel': sum(v for (x, s, a), v in zaehl.items() if x == l and a == 'knobel')} for l in lz}
    BERICHT.write_text(json.dumps(alle, ensure_ascii=False, indent=1, sort_keys=True), encoding='utf-8')
    print(f'{pfad.name}: {len(neue)} neue Übungen angehängt, jetzt {len(datei["aufgaben"])} Aufgaben')
    return datei


def nachweis(thema, basis='origin/lernen-app'):
    alt = json.loads(subprocess.run(['git', 'show', f'{basis}:inhalte/themen/{thema}.json'], capture_output=True,
                                    text=True, check=True).stdout)
    neu = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    n = len(alt['aufgaben'])
    ok_reihe = neu['aufgaben'][:n] == alt['aufgaben']
    neu_set = [json.dumps(a, sort_keys=True, ensure_ascii=False) for a in neu['aufgaben']]
    fehlt = [a for a in alt['aufgaben'] if json.dumps(a, sort_keys=True, ensure_ascii=False) not in neu_set]
    ok_inhalt = alt['inhalt'] == neu['inhalt'] and {k: v for k, v in alt.items() if k != 'aufgaben'} == {k: v for k, v in neu.items() if k != 'aufgaben'}
    rest = neu['aufgaben'][n:]
    ok_rest = all(a['p'] == 'uebung' and a['s'] in (2, 3) for a in rest)
    gut = ok_reihe and not fehlt and ok_inhalt and ok_rest
    print(f'{thema}: {"OK" if gut else "FEHLER"} – {n} alte Aufgaben unverändert und in gleicher Reihenfolge: {ok_reihe}; '
          f'fehlend: {len(fehlt)}; Lernkarten/Kopf gleich: {ok_inhalt}; {len(rest)} neue (nur Übung, Stufe 2/3): {ok_rest}')
    return gut


if __name__ == '__main__':
    sys.exit(0 if all([nachweis(t) for t in sys.argv[1:]]) else 1)
