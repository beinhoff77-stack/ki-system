#!/usr/bin/env python3
"""Achtzehnte Runde, Teil B (Zweig luecken-kl10): Lehrplan-Lücken in freigegebenen Themen der Klasse 10 schließen.

Die Generatoren bauen zuerst wie bisher alles (gleiche Zufallsstarts, alle alten Aufgaben wörtlich gleich) und rufen
ganz am Ende diese Hilfen auf:
  karte_einfuegen(...)  – neue Lernkarte hinter einer vorhandenen einfügen (Abschnitt, Teilfähigkeit, Bewertung),
                          ihre Aufgaben (Übung 4/6/8, Test 1, Korrektur 3, Sicherung 6) hinten anhängen.
  karte_erweitern(...)  – eine vorhandene Karte um Schritte der Bildergeschichte und um Übungen ergänzen.
  offen_ergaenzen(...)  – Eintrag unter „offen“ anhängen (alte Einträge bleiben).

Nachweis gegen den freigegebenen Stand:
    python3 -I -B inhalte/generatoren/_luecken_kl10.py <thema> [<git-stand, Standard: origin/lernen-app>]
Prüft: alle alten Aufgaben unverändert an derselben Stelle; neue Aufgaben nur hinten und nur zu neuen oder erweiterten Karten
(bei erweiterten Karten nur Übungen); alte Lernkarten unverändert außer den erweiterten; Abschnitte, Teilfähigkeiten, Bewertung
nur um die neuen Lernziele ergänzt; alte „offen“-Einträge unverändert; alle übrigen Felder gleich.
"""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl10 import THEMEN, _schluessel, _hoch  # noqa: E402

PLAN_NEU = {('uebung', 1): 4, ('uebung', 2): 6, ('uebung', 3): 8, ('test', 2): 1, ('korrektur', 2): 3, ('sicherung', 2): 6}
TYPEN = ('zahl', 'auswahl', 'luecken', 'text')


def laden(thema):
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    return pfad, roh, json.loads(roh)


def schreiben(pfad, roh, d):
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')


def _aufgaben_pruefen_und_anhaengen(d, lernziel, aufgaben, nur_uebung):
    beispiele = {(s['text'] if isinstance(s, dict) else s).strip() for e in d['inhalt']['etappen'] for s in e.get('schritte', [])}
    gesehen = {_schluessel(a) for a in d['aufgaben']}
    z = Counter()
    for a in aufgaben:
        assert a is not None, f'{lernziel}: leere Aufgabe'
        p, s = a.pop('p'), a.pop('s')
        assert a['y'] in TYPEN, a['y']
        assert len(a.get('w', '')) >= 15, f'{lernziel}: Weg fehlt: {a["f"]["text"][:60]}'
        if nur_uebung: assert p == 'uebung', f'{lernziel}: erweiterte Karte bekommt nur Übungen'
        if p == 'uebung':
            assert a.get('h'), f'{lernziel}: Tipp fehlt: {a["f"]["text"][:60]}'
        else:
            a.pop('h', None)
            assert s == 2, f'{lernziel}: {p} muss Stufe 2 sein'
        if a['y'] == 'zahl': assert 'c' in a, f'{lernziel}: c fehlt: {a["f"]["text"][:60]}'
        a['f']['text'] = _hoch(a['f']['text'])
        a['w'] = _hoch(a['w'])
        if 'a' in a: a['a'] = [_hoch(x) for x in a['a']]
        k = _schluessel(a)
        assert k not in gesehen, f'{lernziel}: Dublette: {a["f"]["text"][:70]}'
        assert a['f']['text'].strip() not in beispiele, f'{lernziel}: gleich wie Beispiel'
        gesehen.add(k)
        t = a.pop('t', None) or lernziel
        d['aufgaben'].append({'l': lernziel, 't': t, 'p': p, 's': s, **a})
        z[(p, s)] += 1
    return z


def karte_einfuegen(thema, etappe, nach, aufgaben, vertiefung=False):
    """etappe: vollständige Lernkarte im neuen Muster. aufgaben: Liste mit 'p' und 's' je Aufgabe (ohne 'l')."""
    pfad, roh, d = laden(thema)
    inh = d['inhalt']
    lz = [e['lernziel'] for e in inh['etappen']]
    neu = etappe['lernziel']
    assert neu not in lz and nach in lz
    assert len(etappe['titel']) <= 40
    for k in ('titel', 'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'regel'):
        assert etappe.get(k), f'{neu}: Feld {k} fehlt'
    i = lz.index(nach)
    inh['etappen'].insert(i + 1, etappe)
    for ab in inh['abschnitte']:
        if nach in ab['lernziele']:
            ab['lernziele'].insert(ab['lernziele'].index(nach) + 1, neu)
    tf = inh['teilfaehigkeiten']
    j = next(n for n, t in enumerate(tf) if nach in t['lernziele'])
    tf.insert(j + 1, {'k': neu, 'text': etappe['titel'], 'lernziele': [neu]})
    bw = inh['bewertung']
    liste = bw['lernziele_vertiefung'] if vertiefung else bw['lernziele_pflicht']
    if nach in liste: liste.insert(liste.index(nach) + 1, neu)
    else: liste.append(neu)
    z = _aufgaben_pruefen_und_anhaengen(d, neu, aufgaben, nur_uebung=False)
    assert dict(z) == PLAN_NEU, f'{neu}: {dict(z)} statt {PLAN_NEU}'
    schreiben(pfad, roh, d)
    print(f'{pfad.name}: neue Lernkarte {neu} nach {nach} ({sum(z.values())} Aufgaben), jetzt {len(d["aufgaben"])} Aufgaben')


def karte_erweitern(thema, lernziel, schritte_neu, uebungen, einfuegen_vor=None, felder=None):
    """schritte_neu: Liste {text, bild?}, hinten angehängt (oder vor Index einfuegen_vor). uebungen: nur Pool 'uebung'.
    felder: optional weitere Felder der Karte, die ersetzt werden (z. B. 'regel')."""
    pfad, roh, d = laden(thema)
    e = next(x for x in d['inhalt']['etappen'] if x['lernziel'] == lernziel)
    if einfuegen_vor is None: e['schritte'] += schritte_neu
    else: e['schritte'][einfuegen_vor:einfuegen_vor] = schritte_neu
    assert len(e['schritte']) <= 6, f'{lernziel}: {len(e["schritte"])} Schritte'
    e.update(felder or {})
    z = _aufgaben_pruefen_und_anhaengen(d, lernziel, uebungen, nur_uebung=True)
    schreiben(pfad, roh, d)
    print(f'{pfad.name}: Karte {lernziel} um {len(schritte_neu)} Schritt(e) und {sum(z.values())} Übungen erweitert {dict(sorted(z.items()))}')


def offen_ergaenzen(thema, eintrag):
    pfad, roh, d = laden(thema)
    d.setdefault('offen', []).append(eintrag)
    schreiben(pfad, roh, d)


# ---------- Nachweis ----------
def _k(x): return json.dumps(x, ensure_ascii=False, sort_keys=True)


def nachweis(thema, stand='origin/lernen-app'):
    rel = f'inhalte/themen/{thema}.json'
    wurzel = THEMEN.parent.parent
    alt = json.loads(subprocess.run(['git', '-C', str(wurzel), 'show', f'{stand}:{rel}'], capture_output=True, check=True, text=True).stdout)
    neu = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    ok, msg = True, []

    def fehler(m):
        nonlocal ok
        ok = False
        msg.append('FEHLER ' + m)

    # übrige Felder
    for k in sorted(set(alt) | set(neu)):
        if k in ('aufgaben', 'inhalt', 'offen'): continue
        if _k(alt.get(k)) != _k(neu.get(k)): fehler(f'Feld {k} geändert')
    ai, ni = alt['inhalt'], neu['inhalt']
    for k in sorted(set(ai) | set(ni)):
        if k in ('etappen', 'abschnitte', 'teilfaehigkeiten', 'bewertung'): continue
        if _k(ai.get(k)) != _k(ni.get(k)): fehler(f'inhalt.{k} geändert')
    # Lernkarten
    alz = [e['lernziel'] for e in ai['etappen']]
    nlz = [e['lernziel'] for e in ni['etappen']]
    neue_lz = [x for x in nlz if x not in alz]
    if [x for x in nlz if x in alz] != alz: fehler('alte Lernkarten fehlen oder sind umsortiert')
    ae = {e['lernziel']: e for e in ai['etappen']}
    ne = {e['lernziel']: e for e in ni['etappen']}
    erweitert = []
    for l in alz:
        if l in ne and _k(ae[l]) != _k(ne[l]):
            erweitert.append(l)
            felder = sorted(x for x in set(ae[l]) | set(ne[l]) if _k(ae[l].get(x)) != _k(ne[l].get(x)))
            alt_s, neu_s = ae[l]['schritte'], ne[l]['schritte']
            behalten = all(_k(s) in {_k(t) for t in neu_s} for s in alt_s)
            msg.append(f'  Karte {l} erweitert: Felder {felder}; Schritte {len(alt_s)} → {len(neu_s)}, alle alten Schritte erhalten: {"ja" if behalten else "NEIN"}')
            if not behalten: fehler(f'{l}: alter Schritt verändert')
    # Abschnitte, Teilfähigkeiten, Bewertung: ohne die neuen Lernziele gleich
    ohne = lambda xs: [x for x in xs if x not in neue_lz]  # noqa: E731
    if _k([[a['titel'], a['lernziele']] for a in ai['abschnitte']]) != _k([[a['titel'], ohne(a['lernziele'])] for a in ni['abschnitte']]): fehler('abschnitte anders geändert')
    if _k(ai['teilfaehigkeiten']) != _k([t for t in ni['teilfaehigkeiten'] if t['k'] not in neue_lz]): fehler('teilfaehigkeiten anders geändert')
    ab, nb = ai['bewertung'], ni['bewertung']
    if _k({k: (ohne(v) if isinstance(v, list) else v) for k, v in nb.items()}) != _k(ab): fehler('bewertung anders geändert')
    # offen
    ao, no = alt.get('offen', []), neu.get('offen', [])
    if no[:len(ao)] != ao: fehler('alte offen-Einträge geändert')
    # Aufgaben
    A, N = alt['aufgaben'], neu['aufgaben']
    abw = [i for i, a in enumerate(A) if i >= len(N) or _k(a) != _k(N[i])]
    if abw: fehler(f'alte Aufgaben verändert/verschoben an Stelle {abw[:5]}')
    zusatz = N[len(A):]
    for a in zusatz:
        if a['l'] in neue_lz: continue
        if a['l'] in erweitert and a['p'] == 'uebung': continue
        fehler(f'neue Aufgabe zu {a["l"]}/{a["p"]} passt zu keiner neuen oder erweiterten Karte')
    z = Counter((a['l'], a['p'], a['s']) for a in zusatz)
    print(f'{thema}: alt {len(A)} Aufgaben, neu {len(N)} (+{len(zusatz)}); alte Aufgaben an gleicher Stelle unverändert: {"ja" if not abw else "NEIN"}')
    print(f'  neue Lernkarten: {neue_lz or "–"}; erweiterte Lernkarten: {erweitert or "–"}; neue offen-Einträge: {len(no) - len(ao)}')
    for m in msg: print(m)
    for l in neue_lz + erweitert:
        teile = ', '.join(f'{p}/s{s}: {n}' for (ll, p, s), n in sorted(z.items()) if ll == l)
        print(f'  {l}: {teile}')
    print('NACHWEIS OK' if ok else 'NACHWEIS FEHLGESCHLAGEN')
    return ok


if __name__ == '__main__':
    sys.exit(0 if nachweis(*sys.argv[1:]) else 1)
