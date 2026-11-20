"""Zehnte Runde (Zweig schwer-kl10): schwerere Übungen nach Prüfungsvorbild für die Themen der Klasse 10.

Die Generatoren bauen zuerst wie bisher alle Aufgaben (unverändert, gleicher Zufallsstart) und hängen
danach mit ergaenzen(...) die neuen Übungen an. Die neuen Aufgaben haben einen eigenen festen Zufallsstart
(nur für das Mischen der Antworten), ihre Lösungen werden im Generator berechnet.

Nachweis „alte Aufgaben unverändert“:
    python3 -I inhalte/generatoren/_schwer_kl10.py <thema> [<git-stand, Standard: origin/lernen-app>]
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import THEMEN, R, _schluessel, _hoch  # noqa: E402

TYPEN = ('zahl', 'auswahl', 'luecken', 'text')


def ergaenzen(datei, neue, hoch=True, soll=(4, 2)):
    """neue: Liste von Aufgaben {'l': lernziel, 's': 2|3, 'y': …, 'f': …, 'o': …, 'w': …, 'h': …, 'c'?: …}.
    Hängt sie als Übungen an die schon gebaute Datei an und schreibt sie neu. Prüft: Tipp, Weg, Typ, Dubletten
    im ganzen Thema und je Lernkarte mindestens soll[0] neue Stufe-3- und soll[1] neue Stufe-2-Übungen."""
    thema = datei['thema_schluessel']
    lz = [e['lernziel'] for e in datei['inhalt']['etappen']]
    beispiele = {(s['text'] if isinstance(s, dict) else s).strip() for e in datei['inhalt']['etappen'] for s in e.get('schritte', [])}
    gesehen = {_schluessel(a) for a in datei['aufgaben']}
    zahl = {(l, s): 0 for l in lz for s in (2, 3)}
    for a in neue:
        assert a is not None, f'{thema}: leere Aufgabe'
        l, s = a.pop('l'), a.pop('s')
        assert l in lz, f'{thema}: unbekannte Lernkarte {l}'
        assert s in (2, 3), f'{thema}/{l}: Stufe {s}'
        assert a['y'] in TYPEN, f'{thema}/{l}: Typ {a["y"]}'
        assert a.get('h') and len(a.get('w', '')) >= 15, f'{thema}/{l}: Tipp oder Weg fehlt: {a["f"]["text"][:50]}'
        if a['y'] == 'zahl': assert 'c' in a, f'{thema}/{l}: c fehlt: {a["f"]["text"][:50]}'
        if hoch:
            a['f']['text'] = _hoch(a['f']['text'])
            a['w'] = _hoch(a['w'])
            if 'a' in a: a['a'] = [_hoch(x) for x in a['a']]
        k = _schluessel(a)
        assert k not in gesehen, f'{thema}/{l}: Dublette: {a["f"]["text"][:60]}'
        assert a['f']['text'].strip() not in beispiele, f'{thema}/{l}: gleich wie Beispiel'
        gesehen.add(k)
        t = a.pop('t', None) or l
        datei['aufgaben'].append({'l': l, 't': t, 'p': 'uebung', 's': s, **a})
        zahl[(l, s)] += 1
    for l in lz:
        assert zahl[(l, 3)] >= soll[0] and zahl[(l, 2)] >= soll[1], f'{thema}/{l}: neu Stufe 3: {zahl[(l, 3)]}, Stufe 2: {zahl[(l, 2)]}'
    pfad = THEMEN / f'{thema}.json'
    pfad.write_text(json.dumps(datei, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{pfad.name}: {len(neue)} neue Übungen angehängt, jetzt {len(datei["aufgaben"])} Aufgaben')
    return datei


def nachweis(thema, stand='origin/lernen-app'):
    """Jede Aufgabe des alten Stands steht unverändert (gleiche Reihenfolge, gleiche Felder) am Anfang der neuen Datei;
    Lernkarten, Abschnitte und übrige Felder sind gleich. Gibt die Zahl der neuen Aufgaben je Lernkarte und Stufe aus."""
    rel = f'inhalte/themen/{thema}.json'
    wurzel = THEMEN.parent.parent
    alt = json.loads(subprocess.run(['git', '-C', str(wurzel), 'show', f'{stand}:{rel}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    ja, na = alt['aufgaben'], neu['aufgaben']
    fehler = [i for i, a in enumerate(ja) if i >= len(na) or json.dumps(a, sort_keys=True, ensure_ascii=False) != json.dumps(na[i], sort_keys=True, ensure_ascii=False)]
    alt_texte = {json.dumps(a, sort_keys=True, ensure_ascii=False) for a in ja}
    fehlt = [a['f']['text'][:60] for a in ja if json.dumps(a, sort_keys=True, ensure_ascii=False) not in {json.dumps(b, sort_keys=True, ensure_ascii=False) for b in na}]
    rest_gleich = {k: alt[k] == neu[k] for k in alt if k != 'aufgaben'}
    rest_gleich.update({k: False for k in neu if k not in alt})
    zusatz = na[len(ja):]
    neu_alt = sum(1 for a in zusatz if json.dumps(a, sort_keys=True, ensure_ascii=False) in alt_texte)
    from collections import Counter
    z = Counter((a['l'], a['p'], a['s']) for a in zusatz)
    ok = not fehler and not fehlt and all(rest_gleich.values()) and neu_alt == 0 and all(a['p'] == 'uebung' for a in zusatz)
    print(f'{thema}: alt {len(ja)} Aufgaben, neu {len(na)} (+{len(zusatz)}); alte Aufgaben an gleicher Stelle unverändert: {"ja" if not fehler else f"NEIN {fehler[:5]}"}; '
          f'jede alte Aufgabe vorhanden: {"ja" if not fehlt else f"NEIN {fehlt[:3]}"}; übrige Felder gleich: {"ja" if all(rest_gleich.values()) else [k for k, v in rest_gleich.items() if not v]}')
    for e in neu['inhalt']['etappen']:
        l = e['lernziel']
        s3 = sum(1 for a in na if a['l'] == l and a['p'] == 'uebung' and a['s'] == 3)
        print(f'  {l}: neu Stufe 2: {z[(l, "uebung", 2)]}, Stufe 3: {z[(l, "uebung", 3)]}; Stufe-3-Übungen gesamt: {s3}')
    print('NACHWEIS OK' if ok else 'NACHWEIS FEHLGESCHLAGEN')
    return ok


if __name__ == '__main__':
    sys.exit(0 if nachweis(*sys.argv[1:]) else 1)
