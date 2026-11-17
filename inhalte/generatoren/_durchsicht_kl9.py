"""Neunzehnte Runde, Teil A (Zweig durchsicht-kl9): Gesamtdurchsicht der Klasse-9-Themen.

Jeder Generator bekommt am Ende einen Abschnitt DURCHSICHT mit einer eigenen Befunde-Liste (Bausteine und Regeln wie in
_befunde.py: stufe / loesung / ersetze / neu, eigener fester Zufallsstart) und optional Lernkarten-Verbesserungen (karten).
Beides wird erst NACH allen bisherigen Bauschritten auf die fertige Datei angewendet; alles andere bleibt Zeichen für Zeichen gleich.

Nachweis:  python3 -I inhalte/generatoren/_durchsicht_kl9.py <thema> [...]   (gegen origin/lernen-app)
"""
import collections
import difflib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _befunde import Befunde, befunde_datei  # noqa: E402,F401
from _luecken_kl9 import _karte_pruefen  # noqa: E402

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
WURZEL = THEMEN.parent.parent


def durchsicht(thema, bf, karten=None):
    """bf: Befunde-Liste der Neunzehnten Runde; karten: {lernziel: {feld: neuer Wert}} (einstieg, woerter, bild, schritte, fehler, fehler_bild, regel, probe)."""
    befunde_datei(thema, bf)
    if not karten: return
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d = json.loads(roh)
    for lz, felder in karten.items():
        e = next(x for x in d['inhalt']['etappen'] if x['lernziel'] == lz)
        for k, v in felder.items():
            assert k in ('einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe'), k
            assert e.get(k) != v, (lz, k, 'unverändert')
            e[k] = v
        _karte_pruefen(e)
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    print(f'  DURCHSICHT {thema}: Lernkarten verbessert: {", ".join(f"{lz} ({", ".join(f)})" for lz, f in karten.items())}')


def stufen(thema):
    d = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    z = collections.Counter((a['l'], a['s']) for a in d['aufgaben'] if a['p'] == 'uebung')
    return {e['lernziel']: (z[(e['lernziel'], 1)], z[(e['lernziel'], 2)], z[(e['lernziel'], 3)]) for e in d['inhalt']['etappen']}


def nachweis(thema, stand='origin/lernen-app'):
    pfad = f'inhalte/themen/{thema}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{stand}:{pfad}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((WURZEL / pfad).read_text(encoding='utf-8'))
    k = lambda a: json.dumps(a, ensure_ascii=False, sort_keys=True)
    ok = True
    ai, ni = alt['inhalt'], neu['inhalt']
    if k({x: v for x, v in alt.items() if x not in ('aufgaben', 'inhalt')}) != k({x: v for x, v in neu.items() if x not in ('aufgaben', 'inhalt')}) \
            or k({x: v for x, v in ai.items() if x != 'etappen'}) != k({x: v for x, v in ni.items() if x != 'etappen'}):
        ok = False; print('FEHLER: Kopf, offen, Bereiche oder Bewertung geändert')
    if [e['lernziel'] for e in ai['etappen']] != [e['lernziel'] for e in ni['etappen']]:
        ok = False; print('FEHLER: Lernkarten-Liste geändert')
    for ea, en in zip(ai['etappen'], ni['etappen']):
        f = sorted(x for x in set(ea) | set(en) if ea.get(x) != en.get(x))
        if f:
            print(f'  KARTE    {ea["lernziel"]}: {f}')
            if set(f) - {'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe'}: ok = False; print('    FEHLER: Feld nicht erlaubt')
    A, N = alt['aufgaben'], neu['aufgaben']
    sm = difflib.SequenceMatcher(a=[k(a) for a in A], b=[k(a) for a in N], autojunk=False)
    z = collections.Counter()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        if tag == 'replace':
            alt_b, neu_b = list(A[i1:i2]), list(N[j1:j2])
            paare = []
            if len(alt_b) == len(neu_b):
                paare = list(zip(alt_b, neu_b)); neu_b = []
            else:  # gleich lange Paare über Lernkarte + Fragetext finden, Rest sind neue Aufgaben
                for a in alt_b:
                    b = next((x for x in neu_b if (x['l'], x['p'], x['f']['text']) == (a['l'], a['p'], a['f']['text'])), None)
                    if b is None: ok = False; print(f'FEHLER: Aufgabe verschwunden: {a["f"]["text"][:80]}'); continue
                    neu_b.remove(b); paare.append((a, b))
            for b in neu_b:
                z['neu'] += 1
                print(f'  NEU      {b["l"]}/{b["p"]} s{b["s"]}: „{b["f"]["text"][:100]}“')
                if b['p'] != 'uebung': ok = False
            for a, b in paare:
                if a['f'] != b['f'] or a.get('a') != b.get('a'):
                    z['ersetzt'] += 1
                    print(f'  ERSETZT  {a["l"]}/{a["p"]} s{a["s"]}: „{a["f"]["text"][:100]}“ → s{b["s"]} „{b["f"]["text"][:100]}“')
                    if (a['l'], a['p'], a['t']) != (b['l'], b['p'], b['t']): ok = False; print('    FEHLER: Lernkarte/Pool geändert')
                else:
                    f = sorted(x for x in set(a) | set(b) if a.get(x) != b.get(x))
                    art = 'stufe' if f == ['s'] else 'loesung'
                    z[art] += 1
                    print(f'  {art.upper():8} {a["l"]}/{a["p"]}: „{a["f"]["text"][:90]}“ {f}' + (f' ({a["s"]}→{b["s"]})' if 's' in f else ''))
                    if set(f) - {'s', 'o', 'h', 'w', 'c'}: ok = False; print('    FEHLER: unerlaubtes Feld')
        elif tag == 'insert':
            for b in N[j1:j2]:
                z['neu'] += 1
                print(f'  NEU      {b["l"]}/{b["p"]} s{b["s"]}: „{b["f"]["text"][:100]}“')
                if b['p'] != 'uebung': ok = False
        else:
            ok = False; print(f'FEHLER: {tag} {i1}-{i2} → {j1}-{j2}')
    st = stufen(thema)
    zu_wenig = {l: s for l, s in st.items() if min(s) < 3}
    if zu_wenig: ok = False; print('FEHLER: weniger als 3 Übungen je Stufe:', zu_wenig)
    print(f'{thema}: Stufe {z["stufe"]}, Lösung/Tipp/Weg {z["loesung"]}, ersetzt {z["ersetzt"]}, neu {z["neu"]}; Übungen je Stufe {st} – {"NACHWEIS OK" if ok else "NACHWEIS FEHLER"}')
    return ok


if __name__ == '__main__':
    sys.exit(0 if all([nachweis(t) for t in sys.argv[1:]]) else 1)
