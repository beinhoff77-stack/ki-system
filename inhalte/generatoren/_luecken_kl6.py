"""Achtzehnte Runde, Teil B, Klasse 6 (Zweig luecken-kl6): Lehrplan-Lücken in freigegebenen Themen schließen.

Jeder betroffene Generator hat am Ende einen Abschnitt LUECKEN. Er läuft NACH allen bisherigen Abschnitten (auch SCHWER der Zehnten Runde)
mit eigenem festem Zufallsstart. Vorhandene Lernkarten und Aufgaben bleiben Zeichen für Zeichen gleich; neue Aufgaben werden hinten angehängt.

- karte_neu: neue Lernkarte an einer festen Stelle einfügen (etappen, abschnitte, teilfaehigkeiten, bewertung) und ihre 28 Aufgaben anhängen
  (Übung Stufe 1: 4, Stufe 2: 6, Stufe 3: 8; 1 Test, 3 Korrektur, 6 Sicherung).
- karte_erweitern: vorhandene Lernkarte um Schritte/Wörter ergänzen und Übungen anhängen (nur wo der Auftrag das so vorsieht).
Nachweis: _luecken_kl6_nachweis.py.
"""
import random

from _basis import Fr, wert  # noqa: F401
from _schwer_kl6 import _schluessel, zahl, wahl, luecken, anteil, mark  # noqa: F401

PLAN_NEU = {('uebung', 1): 4, ('uebung', 2): 6, ('uebung', 3): 8, ('test', 2): 1, ('korrektur', 2): 3, ('sicherung', 2): 6}


def _pruefe(a, pool, lz):
    assert a['y'] in ('zahl', 'auswahl', 'luecken', 'markierung'), (lz, a)
    assert a.get('w'), (lz, 'Lösungsweg fehlt', a['f']['text'])
    if a['y'] in ('zahl', 'luecken'):
        assert 'c' in a, (lz, 'c fehlt', a['f']['text'])
    if pool == 'uebung':
        assert a.get('h'), (lz, 'Tipp fehlt', a['f']['text'])
    else:
        a.pop('h', None)  # Test, Korrektur, Sicherung ohne Tipp
    return a


def _anhaengen(datei, lz, liste, R, gesehen):
    dazu = []
    for pool, stufe, fn in liste:
        a = _pruefe(fn(R), pool, lz)
        k = _schluessel(a)
        assert k not in gesehen, (lz, 'doppelt', a['f']['text'])
        gesehen.add(k)
        dazu.append({'l': lz, 't': lz, 'p': pool, 's': stufe, **a})
    datei['aufgaben'] += dazu
    return dazu


def karte_neu(datei, karte, aufgaben, seed, nach=None, vor=None, teil_text=None, vertiefung=False):
    """karte: fertige Lernkarte (lernziel, titel, einstieg, woerter, bild, schritte, fehler, fehler_bild, regel, probe).
    aufgaben: Liste aus (pool, stufe, funktion(R) -> Aufgabe ohne l/t/p/s). nach/vor: Lernziel, neben das die Karte kommt."""
    R = random.Random(seed)
    inh = datei['inhalt']
    lz = karte['lernziel']
    et = inh['etappen']
    assert lz not in [e['lernziel'] for e in et], lz
    bezug = nach or vor
    i = [e['lernziel'] for e in et].index(bezug) + (1 if nach else 0)
    et.insert(i, karte)
    for ab in inh['abschnitte']:
        if bezug in ab['lernziele']:
            j = ab['lernziele'].index(bezug) + (1 if nach else 0)
            ab['lernziele'].insert(j, lz)
            break
    else:
        raise AssertionError(('Abschnitt nicht gefunden', bezug))
    tf = inh['teilfaehigkeiten']
    k = [t['k'] for t in tf].index(bezug) + (1 if nach else 0) if bezug in [t['k'] for t in tf] else len(tf)
    tf.insert(k, {'k': lz, 'text': teil_text or karte['titel'], 'lernziele': [lz]})
    bw = inh['bewertung']
    ziel = bw['lernziele_vertiefung'] if vertiefung else bw['lernziele_pflicht']
    reihe = [e['lernziel'] for e in et]
    ziel.append(lz)
    ziel.sort(key=reihe.index)
    zaehl = {}
    for pool, stufe, _ in aufgaben:
        zaehl[(pool, stufe)] = zaehl.get((pool, stufe), 0) + 1
    assert zaehl == PLAN_NEU, (lz, zaehl)
    gesehen = {_schluessel(a) for a in datei['aufgaben']}
    _anhaengen(datei, lz, aufgaben, R, gesehen)
    return datei


def karte_erweitern(datei, lz, aufgaben, seed, schritte_einfuegen=(), woerter_dazu=()):
    """Vorhandene Karte: Schritte an Position einfügen ((index, schritt), aufsteigend), Wörter anhängen, Übungen anhängen."""
    R = random.Random(seed)
    karte = next(e for e in datei['inhalt']['etappen'] if e['lernziel'] == lz)
    for idx, s in schritte_einfuegen:
        karte['schritte'].insert(idx, s)
    if woerter_dazu:
        karte.setdefault('woerter', []).extend([list(w) for w in woerter_dazu])
    gesehen = {_schluessel(a) for a in datei['aufgaben']}
    _anhaengen(datei, lz, [(('uebung' if p is None else p), s, fn) for p, s, fn in aufgaben], R, gesehen)
    return datei


# ---------- Bausteine ----------
def _rechne(E):
    """Derselbe Rechner wie im Prüfskript (tools/inhalt_pruefen.py), damit Lösung und Nachrechnung übereinstimmen."""
    import importlib.util
    from pathlib import Path
    pfad = Path(__file__).resolve().parent.parent.parent / 'tools' / 'inhalt_pruefen.py'
    spec = importlib.util.spec_from_file_location('_inhalt_pruefen', pfad)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.rechne(E)

_HG = 'Ganze ins erste Kästchen, dann Zähler und Nenner des Restbruchs (vollständig gekürzt).'


def gemischt(text, E, h, weg, grafik=None):
    """Ergebnis des Rechenausdrucks E (> 1, nicht ganz) als gemischte Zahl □ □/□. c rechnet Ganze, Zähler, Nenner aus E nach."""
    x = Fr(_rechne(E))
    z, n = x.numerator, x.denominator
    assert x > 1 and n > 1, (text, x)
    return luecken(text, '□ □/□', _HG, [z // n, z % n, n], [f'({E}) // 1', f'(({E}) - ({E}) // 1) * {n}', f'{n}'], h, weg, grafik)


def bruch(text, E, h, weg, grafik=None):
    """Ergebnis des Rechenausdrucks E als vollständig gekürzter Bruch □/□ (Minus in den Zähler). c rechnet Zähler und Nenner aus E nach."""
    x = Fr(_rechne(E))
    return luecken(text, '□/□', 'Zähler ins erste Kästchen, Nenner ins zweite. Vollständig gekürzt; ein Minus gehört in den Zähler.',
                   [x.numerator, x.denominator], [f'({E}) * {x.denominator}', f'{x.denominator}'], h, weg, grafik)
