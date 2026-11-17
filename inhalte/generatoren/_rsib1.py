"""Neunzehnte Runde, Teil B, Chat 1 (Zweig durchsicht-rsib-1): Durchsicht der Realschul-/IB-Themen.

Die Generatoren erzeugen ihre Aufgaben unverändert (gleicher Zufallsstart). Danach wendet nachtrag() die Ergebnisse
der Durchsicht an:
  - umstufen:  {alter Fragetext: neue Stufe}           (nur Feld s)
  - berichtigen: {alter Fragetext: {Feld: neuer Wert}} (o, h, w, c, a … bei gleicher Frage)
  - ersetzen:  {alter Fragetext: neue Aufgabe}          (neue Frage an derselben Stelle; alter Text kommt in die Liste „ersetzt“)
  - neu:       {lernziel: [Aufgaben]}                   (neue Übungen, hinter den Übungen der Lernkarte eingefügt)
  - karten:    {lernziel: {Feld: Wert}}                 (Erklärfelder einer Lernkarte)
Alle Lösungen mit Rechenausdruck werden nachgerechnet; Dopplungen im ganzen Thema sind verboten.
Die Bausteine Z/A/L legen die Stelle der richtigen Antwort aus dem Fragetext fest (kein gemeinsamer Zufall),
damit die Aufgaben der Generatoren unberührt bleiben.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

HIER = Path(__file__).resolve().parent
THEMEN = HIER.parent / 'themen'
_spec = importlib.util.spec_from_file_location('inhalt_pruefen_rsib1', HIER.parent.parent / 'tools' / 'inhalt_pruefen.py')
_ip = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ip)
rechne = _ip.rechne


def _wert(x):
    x = Fraction(x) if not isinstance(x, float) else Fraction(str(x))
    return int(x) if x.denominator == 1 else float(x)


def Z(s, text, wert, c, w, h, einheit=None, tol=None, grafik=None):
    """Zahl-Aufgabe; wert wird aus c nachgerechnet (ohne Toleranz exakt)."""
    a = {'s': s, 'y': 'zahl', 'f': {'text': text}, 'o': {'wert': _wert(wert)}, 'c': c, 'w': w, 'h': h}
    if einheit: a['o']['einheit'] = einheit
    if tol is not None: a['o']['toleranz'] = tol
    if grafik: a['f']['grafik'] = grafik
    return a


def A(s, text, richtig, falsche, w, h, grafik=None):
    """Auswahl; Stelle der richtigen Antwort aus dem Text (stabil, gleichmäßig verteilt)."""
    opts = [str(f) for f in falsche if str(f) != str(richtig)]
    assert len(opts) == len(set(opts)) and 2 <= len(opts) <= 3, (text, opts)
    i = int(hashlib.md5(text.encode()).hexdigest(), 16) % (len(opts) + 1)
    opts.insert(i, str(richtig))
    a = {'s': s, 'y': 'auswahl', 'f': {'text': text}, 'a': opts, 'o': {'index': i}, 'w': w, 'h': h}
    if grafik: a['f']['grafik'] = grafik
    return a


def L(s, text, schablone, werte, c, w, h, hinweis='Trage die Zahlen ein.', grafik=None):
    a = {'s': s, 'y': 'luecken', 'f': {'text': text, 'schablone': schablone, 'hinweis': hinweis},
         'o': {'werte': [int(v) for v in werte]}, 'c': list(c), 'w': w, 'h': h}
    if grafik: a['f']['grafik'] = grafik
    return a


def _pruefen(a):
    if a['y'] == 'zahl':
        ist = rechne(a['c'])
        soll = Fraction(str(a['o']['wert']))
        assert ist == soll, f'Zahl falsch: {a["f"]["text"]} | {a["c"]} = {float(ist)} ≠ {soll}'
    elif a['y'] == 'luecken' and 'c' in a:
        ist = [rechne(c) for c in a['c']]
        assert ist == [Fraction(v) for v in a['o']['werte']], f'Lücken falsch: {a["f"]["text"]} {ist}'
    assert len(a['w']) >= 15 and a.get('h'), a['f']['text']


def nachtrag(d, neu=None, umstufen=None, berichtigen=None, ersetzen=None, karten=None, offen_neu=(), offen_weg=()):
    neu, umstufen, berichtigen, ersetzen, karten = neu or {}, umstufen or {}, berichtigen or {}, ersetzen or {}, karten or {}
    auf = d['aufgaben']
    lz = [e['lernziel'] for e in d['inhalt']['etappen']]
    texte = [a['f']['text'] for a in auf]
    for t in list(umstufen) + list(berichtigen) + list(ersetzen):
        assert texte.count(t) == 1, ('alter Text nicht eindeutig gefunden', t, texte.count(t))
    log = {'umgestuft': [], 'berichtigt': [], 'ersetzt': [], 'neu': {}}
    for i, a in enumerate(auf):
        t = a['f']['text']
        if t in umstufen:
            log['umgestuft'].append((a['l'], t, a['s'], umstufen[t]))
            a['s'] = umstufen[t]
        if t in berichtigen:
            a.update(berichtigen[t])
            _pruefen(a) if a['p'] == 'uebung' else None
            log['berichtigt'].append((a['l'], t))
        if t in ersetzen:
            n = dict(ersetzen[t])
            s = n.pop('s')
            if a['p'] == 'uebung':
                _pruefen(n)
            else:
                n = {k: v for k, v in n.items() if k != 'h'}
            auf[i] = {'l': a['l'], 't': a['t'], 'p': a['p'], 's': s if a['p'] == 'uebung' else 2, **n}
            log['ersetzt'].append((a['l'], t))
    for l, liste in neu.items():
        assert l in lz, l
        letzte = max(i for i, a in enumerate(auf) if a['l'] == l and a['p'] == 'uebung')
        einfuegen = []
        for n in liste:
            n = dict(n)
            s = n.pop('s')
            _pruefen(n)
            einfuegen.append({'l': l, 't': l, 'p': 'uebung', 's': s, **n})
        auf[letzte + 1:letzte + 1] = einfuegen
        log['neu'][l] = [x['s'] for x in einfuegen]
    for e in d['inhalt']['etappen']:
        if e['lernziel'] in karten:
            e.update(karten[e['lernziel']])
    # Dopplungen und Mindestzahlen (Teil B: Stufe 1 ≥ 4, Stufe 2 ≥ 6, Stufe 3 ≥ 8)
    gesehen = set()
    for a in auf:
        k = a['f']['text'] + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|' + json.dumps(a['f'].get('schablone'), ensure_ascii=False) + '|' + json.dumps(a['f'].get('grafik'), sort_keys=True)
        assert k not in gesehen, ('doppelt', a['f']['text'])
        gesehen.add(k)
    for l in lz:
        st = [sum(1 for a in auf if a['l'] == l and a['p'] == 'uebung' and a['s'] == s) for s in (1, 2, 3)]
        assert st[0] >= 4 and st[1] >= 6 and st[2] >= 8, (l, st)
    if offen_neu or offen_weg:
        alt = [o for o in d.get('offen', []) if not any(o.startswith(w) for w in offen_weg)]
        d['offen'] = alt + [o for o in offen_neu if o not in alt]
        if not d['offen']: d.pop('offen')
    pfad = THEMEN / f"{d['thema_schluessel']}.json"
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
    (HIER.parent.parent / 'tools').exists()
    print(f"{pfad.name}: Durchsicht rsib-1 – umgestuft {len(log['umgestuft'])}, berichtigt {len(log['berichtigt'])}, "
          f"ersetzt {len(log['ersetzt'])}, neu {sum(len(v) for v in log['neu'].values())}")
    return log
