"""Nachweis Zwanzigste Runde, Klasse 6 (Zweig stufen-kl6).

python3 -I inhalte/generatoren/_stufen_kl6_nachweis.py <thema>
1. Gegen origin/lernen-app: Kopf, inhalt (Lernkarten) unverändert; jede alte Aufgabe ist noch da und unterscheidet sich höchstens in g und s;
   nur Übungen wurden innerhalb ihrer Lernkarte umsortiert; neue Aufgaben sind Übungen oder Bonus mit g.
2. Prüfung „nach dem Sperren“: Kopie ohne die überzähligen Übungen (Übungen ohne g) durch tools/inhalt_pruefen.py –
   dort greifen alle Typ-Regeln (jede Übung hat g).
3. Übersicht je Lernkarte: Übungen je Stufe und Typ (ohne überzählige), Zahl der überzähligen, Bonus.
"""
import collections
import json
import subprocess
import sys
import tempfile
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def schluessel(a):
    return json.dumps({k: v for k, v in a.items() if k not in ('g', 's')}, ensure_ascii=False, sort_keys=True)


def main(thema, stand='origin/lernen-app'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    F = []
    if {k: v for k, v in alt.items() if k != 'aufgaben'} != {k: v for k, v in neu.items() if k != 'aufgaben'}:
        F.append('Kopf oder Lernkarten geändert')
    rest = collections.Counter(schluessel(a) for a in neu['aufgaben'])
    s_neu = {}
    for a in neu['aufgaben']: s_neu.setdefault(schluessel(a), []).append(a)
    umgestuft = 0
    for a in alt['aufgaben']:
        k = schluessel(a)
        if rest[k] <= 0: F.append(f'alte Aufgabe fehlt oder geändert: {a["l"]}: {a["f"]["text"][:70]}'); continue
        rest[k] -= 1
        b = s_neu[k].pop(0)
        if b['s'] != a['s']:
            umgestuft += 1
            if a['p'] != 'uebung': F.append(f'Stufe außerhalb der Übungen geändert: {a["f"]["text"][:60]}')
        if 'g' in b and a['p'] != 'uebung': F.append(f'g außerhalb der Übungen: {a["f"]["text"][:60]}')
    neue = [a for k, xs in s_neu.items() for a in xs]
    for a in neue:
        if a['p'] not in ('uebung', 'bonus') or 'g' not in a: F.append(f'neue Aufgabe nicht Übung/Bonus mit g: {a["f"]["text"][:60]}')
    # Reihenfolge: Nicht-Übungen behalten ihre Plätze relativ zueinander; Übungen bleiben in ihrer Lernkarte
    nicht_ue_alt = [schluessel(a) for a in alt['aufgaben'] if a['p'] != 'uebung']
    nicht_ue_neu = [schluessel(a) for a in neu['aufgaben'] if a['p'] not in ('uebung', 'bonus')]
    if nicht_ue_alt != nicht_ue_neu: F.append('Reihenfolge von Test/Korrektur/Sicherung geändert')
    lz_folge = lambda d: [a['l'] for a in d['aufgaben']]
    blk = lambda xs: [x for i, x in enumerate(xs) if i == 0 or xs[i - 1] != x]
    if blk(lz_folge(alt)) != blk(lz_folge(neu)): F.append('Aufgaben einer Lernkarte stehen nicht mehr zusammen')
    # Kopie ohne überzählige
    ueber = [a for a in neu['aufgaben'] if a['p'] == 'uebung' and 'g' not in a]
    kopie = dict(neu, aufgaben=[a for a in neu['aufgaben'] if not (a['p'] == 'uebung' and 'g' not in a)])
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / f'{thema}.json'
        p.write_text(json.dumps(kopie, ensure_ascii=False, indent=1), encoding='utf-8')
        r = subprocess.run([sys.executable, '-I', str(WURZEL / 'tools/inhalt_pruefen.py'), str(p)], capture_output=True, text=True)
    erste = [z for z in r.stdout.splitlines() if z.startswith('==') or 'FEHLER' in z]
    print('  ohne überzählige: ' + ' | '.join(erste[:12]))
    if r.returncode != 0: F.append('Prüfskript meldet Fehler, wenn die überzähligen gesperrt sind')
    print(f'{thema}: umgestuft {umgestuft}, neue Übungen {sum(1 for a in neue if a["p"] == "uebung")}, Knobel {sum(1 for a in neue if a["p"] == "bonus")}, überzählig {len(ueber)}')
    for e in neu['inhalt']['etappen']:
        lz = e['lernziel']
        ue = [a for a in neu['aufgaben'] if a['l'] == lz and a['p'] == 'uebung' and 'g' in a]
        z = {s: collections.Counter(a['g'] for a in ue if a['s'] == s) for s in (1, 2, 3)}
        bon = sum(1 for a in neu['aufgaben'] if a['l'] == lz and a['p'] == 'bonus')
        ub = sum(1 for a in ueber if a['l'] == lz)
        print(f'  {lz}: ' + ' · '.join(f'S{s} {sum(c.values())} ({", ".join(f"{g} {n}" for g, n in c.items())})' for s, c in z.items()) + f' · überzählig {ub} · Knobel {bon}')
        for s, mn in ((1, 4), (2, 6), (3, 8)):
            if sum(z[s].values()) < mn: F.append(f'{lz}: Stufe {s} hat {sum(z[s].values())} Übungen mit g, Auftrag verlangt {mn}')
        if any(n > 3 for n in z[3].values()): F.append(f'{lz}: Stufe 3 mehr als 3 eines Typs')
        if bon < 1: F.append(f'{lz}: keine Knobel-Bordkarte')
    if F:
        print('FEHLER:'); [print('  ' + f) for f in F]; return 1
    print('NACHWEIS OK'); return 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
