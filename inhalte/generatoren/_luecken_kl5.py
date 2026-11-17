"""Achtzehnte Runde, Teil B (Zweig luecken-kl5): neue Lernkarten in freigegebenen Themen der Klasse 5.

neue_karte(DATEI, ...) fügt eine Lernkarte im neuen Muster (Vorgabe 16.11.) an einer festen Stelle ein und hängt ihre
Aufgaben HINTER alle bisherigen Aufgaben an:
    Übung 18 (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8), Test 1, Korrektur 3, Sicherung 6 (Test/Korrektur/Sicherung Stufe 2, ohne Tipp).
Die festen Aufgaben (Prüfungsvorbild, Knobelaufgabe) kommen aus Z/A/L/wahl (_schwer_kl5.py), der Rest aus einem
Zufallsgenerator gen(R, stufe) mit eigenem festem Zufallsstart. Alle bisherigen Lernkarten und Aufgaben bleiben
Zeichen für Zeichen gleich (Nachweis: _luecken_kl5_nachweis.py).

Die Karte wird streng nach den Regeln der README geprüft (pruefe_karte aus _umbau_kl5.py): Was das Prüfskript nur
als Hinweis meldet, bricht hier ab.
"""
import json
import random

from _umbau_kl5 import pruefe_karte

PLAN = [('uebung', 1)] * 4 + [('uebung', 2)] * 6 + [('uebung', 3)] * 8 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6


def schluessel(a):
    f = a['f']
    return (str(f.get('text', '')).strip() + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|'
            + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + json.dumps(f.get('grafik'), sort_keys=True))


def mische(R, richtig, falsche):
    """Antworten mischen; (liste, index). Dubletten sind ein Fehler."""
    opts = [richtig] + list(falsche)
    assert 3 <= len(opts) <= 4 and len(set(opts)) == len(opts), opts
    R.shuffle(opts)
    return opts, opts.index(richtig)


def _fest(R, a):
    """Aufgabe aus Z/A/L/wahl (_schwer_kl5.py) in das Dateiformat bringen; Auswahl mit eigenem Zufall mischen."""
    a = dict(a)
    a.pop('s')
    if a['y'] == 'auswahl':
        opts = list(a.pop('_opts')); r = a.pop('_richtig')
        R.shuffle(opts)
        a['a'] = opts; a['o'] = {'index': opts.index(r)}
    return a


def neue_karte(datei, karte, nach, abschnitt, teil, gen, seed, fest=(), vertiefung=False):
    """karte: {lernziel, titel, einstieg, woerter, bild, schritte, fehler, fehler_bild?, regel}
    nach: Lernziel, hinter dem die Karte steht (None = ganz vorn); abschnitt: Titel eines vorhandenen Abschnitts
    oder (titel, nach_abschnitt_titel) für einen neuen; teil: k einer vorhandenen Teilfähigkeit oder (k, text);
    gen(R, s) -> Aufgabe {y, f, a?, o, c?, zahl?, w, h}; fest: Aufgaben aus Z/A/L/wahl (Übungen, Stufe aus 's')."""
    inh = datei['inhalt']
    lz = karte['lernziel']
    fehler = []
    pruefe_karte(lz, {k: v for k, v in karte.items() if k not in ('lernziel', 'titel')}, fehler)
    assert len(karte['titel']) <= 40, karte['titel']
    assert not fehler, 'Regeln verletzt:\n' + '\n'.join(fehler)
    namen = [e['lernziel'] for e in inh['etappen']]
    assert lz not in namen, lz
    pos = 0 if nach is None else namen.index(nach) + 1
    inh['etappen'].insert(pos, {'lernziel': lz, 'titel': karte['titel'], **{k: v for k, v in karte.items() if k not in ('lernziel', 'titel')}})
    namen = [e['lernziel'] for e in inh['etappen']]
    # Abschnitt
    if isinstance(abschnitt, tuple):
        titel, hinter = abschnitt
        i = [a['titel'] for a in inh['abschnitte']].index(hinter)
        inh['abschnitte'].insert(i + 1, {'titel': titel, 'lernziele': [lz]})
    else:
        ab = next(a for a in inh['abschnitte'] if a['titel'] == abschnitt)
        ab['lernziele'] = [x for x in namen if x in ab['lernziele'] or x == lz]
    # Teilfähigkeit
    if isinstance(teil, tuple):
        inh['teilfaehigkeiten'].append({'k': teil[0], 'text': teil[1], 'lernziele': [lz]})
        tk = teil[0]
    else:
        tf = next(t for t in inh['teilfaehigkeiten'] if t['k'] == teil)
        tf['lernziele'] = tf['lernziele'] + [lz]
        tk = teil
    # Bewertung (Reihenfolge wie die Lernkarten)
    bw = inh['bewertung']
    liste = 'lernziele_vertiefung' if vertiefung else 'lernziele_pflicht'
    bw[liste] = [x for x in namen if x in bw[liste] or x == lz]
    # Aufgaben
    R = random.Random(seed)
    gesehen = {schluessel(a) for a in datei['aufgaben']}
    beispiele = {(s['text'] if isinstance(s, dict) else s) for e in inh['etappen'] for s in e['schritte']}
    feste = {1: [], 2: [], 3: []}
    for a in fest:
        feste[a['s']].append(a)
    out = []
    for pool, stufe in PLAN:
        if pool == 'uebung' and feste[stufe]:
            a = _fest(R, feste[stufe].pop(0))
        else:
            for _ in range(5000):
                a = gen(R, stufe)
                if schluessel(a) not in gesehen and a['f']['text'] not in beispiele:
                    break
            else:
                raise SystemExit(f'zu wenige Varianten: {lz} Stufe {stufe}')
        k = schluessel(a)
        assert k not in gesehen, f'Dublette: {a["f"]["text"]}'
        assert a['f']['text'] not in beispiele, a['f']['text']
        gesehen.add(k)
        b = {'l': lz, 't': tk, 'p': pool, 's': stufe}
        b.update({x: a[x] for x in ('y', 'f', 'a', 'o', 'zahl', 'c', 'w', 'h') if x in a})
        if pool != 'uebung':
            b.pop('h', None)
        else:
            assert b.get('h'), b['f']['text']
        assert len(b['w']) >= 15, b['f']['text']
        if b['y'] == 'auswahl':
            assert 3 <= len(b['a']) <= 4 and len(set(b['a'])) == len(b['a']), b['a']
        out.append(b)
    for st in (1, 2, 3):
        assert not feste[st], f'{lz}: zu viele feste Aufgaben auf Stufe {st}'
    datei['aufgaben'] = datei['aufgaben'] + out
    return out
