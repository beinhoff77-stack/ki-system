"""Zehnte Runde, Klasse 6 (Zweig schwer-kl6): schwerere Übungen nach Prüfungsvorbild ergänzen.

Jeder Generator der Klasse 6 hat am Ende einen Abschnitt SCHWER. Er läuft NACH dem Erzeugen aller bisherigen
Aufgaben und nach dem Umbau der Lernkarten und benutzt einen eigenen festen Zufallsstart. Die bisherigen
Aufgaben bleiben dadurch Zeichen für Zeichen gleich; die neuen Aufgaben werden hinten angehängt (Pool uebung).

Aufbau eines Eintrags in NEU: {lernziel: [(stufe, funktion), ...]}; funktion(R) liefert ein Aufgaben-Objekt
ohne l/t/p/s (also y, f, a, o, c, h, w). Die Lösungen berechnet die Funktion selbst.
Nachweis „alte Aufgaben unverändert“: _schwer_kl6_nachweis.py.
"""
import json
import random

from _basis import Fr, zt, wert  # noqa: F401

MIN_S3, MIN_S2 = 4, 2


def _schluessel(a):
    """Wie tools/inhalt_pruefen.py: Text + Antworten + Schablone + Grafik."""
    f = a['f']
    return (f['text'].strip() + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|'
            + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + json.dumps(f.get('grafik'), sort_keys=True))


def ergaenzen(datei, neu, seed):
    R = random.Random(seed)
    alt = datei['aufgaben']
    gesehen = {_schluessel(a) for a in alt}
    reihenfolge = [e['lernziel'] for e in datei['inhalt']['etappen']]
    assert sorted(neu) == sorted(reihenfolge), ('NEU passt nicht zu den Lernkarten', sorted(set(neu) ^ set(reihenfolge)))
    tf = {}
    for a in alt:
        tf.setdefault(a['l'], a['t'])
    dazu = []
    for lz in reihenfolge:
        n = {2: 0, 3: 0}
        for stufe, fn in neu[lz]:
            a = fn(R)
            assert a.get('h') and a.get('w'), (lz, a)
            assert a['y'] in ('zahl', 'auswahl', 'luecken', 'text', 'markierung'), (lz, a)
            if a['y'] in ('zahl', 'luecken'):
                assert 'c' in a, (lz, 'Rechenausdruck c fehlt', a['f']['text'])
            k = _schluessel(a)
            assert k not in gesehen, (lz, 'doppelt', a['f']['text'])
            gesehen.add(k)
            n[stufe] = n.get(stufe, 0) + 1
            dazu.append({'l': lz, 't': tf[lz], 'p': 'uebung', 's': stufe, **a})
        assert n[3] >= MIN_S3 and n[2] >= MIN_S2, (lz, n)
    datei['aufgaben'] = alt + dazu
    return datei


# ---------- Bausteine ----------
def zahl(text, w, c, h, weg, einheit=None, toleranz=None, grafik=None):
    o = {'wert': wert(w)}
    if einheit: o['einheit'] = einheit
    if toleranz is not None: o['toleranz'] = toleranz
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    return {'y': 'zahl', 'f': f, 'o': o, 'c': c, 'h': h, 'w': weg}


def wahl(R, text, richtig, falsche, h, weg, grafik=None, n=4):
    opts = [richtig]
    for x in falsche:
        if x not in opts: opts.append(x)
        if len(opts) == n: break
    assert len(opts) >= 3, (text, opts)
    R.shuffle(opts)
    f = {'text': text}
    if grafik: f['grafik'] = grafik
    return {'y': 'auswahl', 'f': f, 'a': opts, 'o': {'index': opts.index(richtig)}, 'h': h, 'w': weg}


def luecken(text, schablone, hinweis, werte, c, h, weg, grafik=None):
    f = {'text': text, 'schablone': schablone, 'hinweis': hinweis}
    if grafik: f['grafik'] = grafik
    assert schablone.count('□') == len(werte) == len(c)
    return {'y': 'luecken', 'f': f, 'o': {'werte': [int(x) for x in werte]}, 'c': c, 'h': h, 'w': weg}


def bruch_luecke(text, x, c_z, c_n, h, weg, grafik=None):
    """Ergebnis als gekürzter Bruch □/□ (Zähler, Nenner)."""
    x = Fr(x)
    return luecken(text, '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.',
                   [x.numerator, x.denominator], [c_z, c_n], h, weg, grafik)


def anteil(text, teil, ganzes, h, weg, grafik=None):
    """Anteil teil/ganzes vollständig gekürzt als □/□; c teilt beide durch den ggT."""
    from math import gcd
    g = gcd(teil, ganzes)
    return luecken(text, '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt.',
                   [teil // g, ganzes // g], [f'{teil} // {g}', f'{ganzes} // {g}'], h, weg, grafik)


def mark(text, start, ende, abschnitte, index, h, weg, zahlwert=None):
    """Markierung am Zahlenstrahl; zahlwert (endliche Dezimalzahl) zum Nachrechnen, sonst weglassen."""
    a = {'y': 'markierung', 'f': {'text': text, 'grafik': {'typ': 'zahlenstrahl', 'start': start, 'ende': ende,
                                                            'abschnitte': abschnitte, 'beschriftet': 'anfang_ende'}},
         'o': {'index': index}, 'h': h, 'w': weg}
    if zahlwert is not None:
        a['zahl'] = wert(zahlwert)
        a['c'] = f'{start} + ({ende} - {start}) * {index} / {abschnitte}'
    return a
