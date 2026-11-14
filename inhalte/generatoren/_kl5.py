"""Gemeinsame Helfer für Themen-Generatoren (Werkstatt #150)."""
import json
import random
from pathlib import Path

THEMEN = Path(__file__).resolve().parent.parent / 'themen'


def zt(n):
    """Zahl deutsch: Minus als −, Tausender mit geschütztem Leerzeichen, Dezimalkomma."""
    if isinstance(n, float) and n.is_integer(): n = int(n)
    s = f'{abs(n):,}'.replace(',', ' ').replace('.', ',') if isinstance(n, int) else f'{abs(n):,}'.replace(',', ' ').replace('.', ',')
    return ('−' if n < 0 else '') + s


def kl(n):
    """Negative Zahl in Klammern (für Rechnungen)."""
    return f'({zt(n)})' if n < 0 else zt(n)


def mische(R, richtig, falsche):
    """Antworten mischen; gibt (liste, index_der_richtigen) zurück. Dubletten sind ein Fehler."""
    opts = [richtig] + list(falsche)
    assert len(set(opts)) == len(opts), opts
    R.shuffle(opts)
    return opts, opts.index(richtig)


_RUND = {'n': 0}


def mische_rund(R, richtig, falsche):
    """Wie mische, aber die richtige Antwort wandert reihum über alle Plätze (gleich verteilt, nie gehäuft auf Platz 1)."""
    f = list(falsche)
    assert len(set([richtig] + f)) == len(f) + 1, [richtig] + f
    R.shuffle(f)
    i = _RUND['n'] % (len(f) + 1)
    _RUND['n'] += 1
    f.insert(i, richtig)
    return f, i


def baue(R, etappen, gen, teil, je_stufe=6, test=1, korrektur=3, sicherung=6):
    """Je Lernkarte: je_stufe Übungen pro Stufe 1–3, dazu Test/Korrektur/Sicherung auf Stufe 2. Alle verschieden."""
    plan = [('uebung', s) for s in (1, 2, 3) for _ in range(je_stufe)] + [('test', 2)] * test + [('korrektur', 2)] * korrektur + [('sicherung', 2)] * sicherung
    out = []
    gesehen = set()                                   # Dubletten über das ganze Thema
    beispiele = {x for e in etappen for x in e['schritte']}
    for e in etappen:
        lz = e['lernziel']
        for pool, stufe in plan:
            for _ in range(3000):
                a = gen[lz](stufe)
                # gleiche Frage mit anders gemischten Antworten zählt als Dublette
                k = a['f']['text'] + '|' + json.dumps(sorted(map(str, a.get('a') or [])), ensure_ascii=False) + '|' + json.dumps(a['f'].get('grafik'), sort_keys=True) + '|' + json.dumps(a['f'].get('schablone'), ensure_ascii=False)
                if k not in gesehen and a['f']['text'] not in beispiele: break
            else:
                raise SystemExit(f'zu wenige Varianten: {lz} Stufe {stufe}')
            gesehen.add(k)
            if pool != 'uebung': a.pop('h', None)
            out.append({'l': lz, 't': teil[lz], 'p': pool, 's': stufe, **a})
    return out


def schreibe(datei, name):
    THEMEN.mkdir(parents=True, exist_ok=True)
    (THEMEN / name).write_text(json.dumps(datei, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{name}: {len(datei["inhalt"]["etappen"])} Lernkarten, {len(datei["aufgaben"])} Aufgaben')
