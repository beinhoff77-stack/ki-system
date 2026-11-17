"""Zwanzigste Runde, Klasse 5 (Zweig stufen-kl5): echte Stufe 3 und Knobel-Bordkarten.

Jeder Generator der Klasse 5 ruft am Ende stufen_anwenden(DATEI, '<thema>') auf. Die Daten stehen je Thema in
_st5_<thema mit _>.py als KARTEN = {lernziel: {...}}:
  leiter  (s1, s2, s3)        Stufen-Leiter in drei Sätzen (für den Bericht)
  typ     [(muster, g), ...]  Typ für JEDE vorhandene Übung. muster ist ein regulärer Ausdruck auf den Fragetext,
                              optional mit Vorsatz 'S2:' (nur Übungen mit dieser Stufe) und Nachsatz '@@text' (muss in der
                              Aufgabe vorkommen, z. B. in Antworten). Erste passende Regel gilt. Die Stufe folgt aus dem Typ
                              (passt sie nicht, wird umgestuft). g = '-' heißt: überzählig (kein Typ, wird gemeldet).
  neu     [(g, aufgabe)]      neue Übungen (Bausteine Z/A/L aus _befunde), Stufe folgt aus g
  knobel  [aufgabe]           Knobel-Bordkarten (Pool bonus, Typ knobel, Stufe 3)
  knobel_grund  str           falls nur eine Knobel-Bordkarte: Begründung
Automatisch: Ab der dritten Übung mit gleichem Typ und gleichem Satzbau in derselben Stufe wird die Übung „überzählig“
(Typ entfernt, gemeldet; der Haupt-Chat sperrt sie). Danach werden die Übungen jeder Lernkarte so geordnet, dass nie zwei
Übungen desselben Typs (bzw. desselben Satzbaus) direkt hintereinander stehen. Alte Aufgaben ändern sich nur in g und s
(Nachweis: _stufen_kl5_nachweis.py).
"""
import collections
import importlib
import json
import re
import sys
from fractions import Fraction as Fr
from pathlib import Path

import random

from _bausatz import rechne
from _befunde import _l as L, _z as Z  # noqa: F401  (Bausteine für die Datenmodule)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / 'tools'))
from inhalt_pruefen import GEDANKEN, STUFE_VON, bauplan, pruefe  # noqa: E402

S3_TYPEN = GEDANKEN[3]
MIN_ANZ = {1: 4, 2: 6, 3: 8}
MIN_TYP = {1: 2, 2: 3, 3: 4}


def A(text, richtig, falsche, w, h, grafik=None):
    """Auswahl: Position der richtigen Antwort fest aus dem Text gemischt."""
    R = random.Random(text)
    f = [str(x) for x in falsche]
    assert str(richtig) not in f and len(set(f)) == len(f) and 2 <= len(f) <= 3, (text, richtig, f)
    R.shuffle(f)
    i = R.randrange(len(f) + 1)
    f.insert(i, str(richtig))
    a = {'y': 'auswahl', 'f': {'text': text}, 'a': f, 'o': {'index': i}, 'w': w, 'h': h}
    if grafik is not None: a['f']['grafik'] = grafik
    return a


def M(text, start, ende, abschnitte, zahl, w, h, beschriftet='anfang_ende'):
    """Markierung auf dem Zahlenstrahl."""
    schritt = Fr(ende - start, abschnitte)
    i = (Fr(zahl) - start) / schritt
    assert i.denominator == 1 and 0 <= i <= abschnitte, (text, i)
    return {'y': 'markierung', 'f': {'text': text, 'grafik': {'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': abschnitte, 'beschriftet': beschriftet}},
            'o': {'index': int(i)}, 'zahl': zahl, 'w': w, 'h': h}


def P(text, start, ende, abschnitte, pfeil, w, h, beschriftet='anfang_ende'):
    """Pfeil am Zahlenstrahl ablesen (Antwort Zahl)."""
    wert = Fr(start) + pfeil * Fr(ende - start, abschnitte)
    assert wert.denominator == 1
    return Z(text, int(wert), f'{start} + {pfeil} * ({ende} - {start}) // {abschnitte}', w, h,
             grafik={'typ': 'zahlenstrahl', 'start': start, 'ende': ende, 'abschnitte': abschnitte, 'beschriftet': beschriftet, 'pfeil': pfeil})


def _passt(regel, a):
    muster, g = regel
    s = None
    if re.match(r'^S[123]:', muster): s, muster = int(muster[1]), muster[3:]
    extra = None
    if '@@' in muster: muster, extra = muster.split('@@', 1)
    if s is not None and a['s'] != s: return False
    if not re.search(muster, a['f']['text']): return False
    if extra and extra not in json.dumps(a, ensure_ascii=False): return False
    return True


def _pruefe_neu(a, g, texte):
    t = a['f']['text']
    assert t not in texte, f'Text schon vorhanden: {t}'
    assert a.get('h') and len(a['w']) >= 15, t
    if a['y'] == 'zahl':
        assert rechne(a['c']) == Fr(str(a['o']['wert'])), (t, a['c'], a['o'])
    if a['y'] == 'auswahl':
        assert len(set(a['a'])) == len(a['a']), t
    if a['y'] == 'markierung':
        gr = a['f']['grafik']; assert Fr(gr['start']) + a['o']['index'] * Fr(gr['ende'] - gr['start'], gr['abschnitte']) == Fr(a['zahl']), t
    if a['y'] == 'luecken':
        for c, v in zip(a['c'], a['o']['werte']): assert rechne(c) == Fr(v), (t, c, v)


def _ordnen(xs):
    """Greedy: nie zweimal derselbe Typ (ohne Typ: derselbe Satzbau) hintereinander; häufigster Rest zuerst."""
    def key(a): return a.get('g') or ('~' + bauplan(a))
    rest = list(xs)
    out = []
    while rest:
        zaehl = collections.Counter(key(a) for a in rest)
        vk, vb = (key(out[-1]), bauplan(out[-1])) if out else (None, None)
        kand = [a for a in rest if key(a) != vk and bauplan(a) != vb] or rest
        best = max(kand, key=lambda a: (zaehl[key(a)], -a['s'], -rest.index(a)))
        out.append(best)
        rest.remove(best)
    return out


def stufen_anwenden(d, thema):
    mod = importlib.import_module('_st5_' + thema.replace('.', '_'))
    KARTEN = mod.KARTEN
    ue_l = list(dict.fromkeys(a['l'] for a in d['aufgaben'] if a['p'] == 'uebung'))
    assert set(KARTEN) == set(ue_l), f'Lernkarten fehlen/zu viel: {set(ue_l) ^ set(KARTEN)}'
    texte = {a['f']['text'] for a in d['aufgaben']}
    tf = {}
    for lz in ue_l:
        tf[lz] = next((t['k'] for t in d['inhalt']['teilfaehigkeiten'] if lz in t.get('lernziele', [])), None) \
            or collections.Counter(a['t'] for a in d['aufgaben'] if a['l'] == lz).most_common(1)[0][0]
    bericht = {'thema': thema, 'karten': {}}
    neue_ue, bonus = {}, {}
    for lz in ue_l:
        k = KARTEN[lz]
        ue = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung']
        vorher = {s: sum(1 for a in ue if a['s'] == s) for s in (1, 2, 3)}
        umgestuft, ueber = [], []
        fehlt = [f'S{a["s"]} „{a["f"]["text"]}“' for a in ue if not any(_passt(r, a) for r in k['typ'])]
        assert not fehlt, f'{thema}/{lz}: kein Typ für ' + ' | '.join(fehlt)
        for a in ue:
            regel = next((r for r in k['typ'] if _passt(r, a)), None)
            g = regel[1]
            if g == '-':
                a.pop('g', None); ueber.append(a['f']['text']); continue
            assert g in STUFE_VON, (lz, g)
            if STUFE_VON[g] != a['s']:
                umgestuft.append((a['f']['text'], a['s'], STUFE_VON[g])); a['s'] = STUFE_VON[g]
            a['g'] = g
        # automatisch überzählig: dritte und weitere Übung mit gleichem Typ und Satzbau je Stufe
        grp = collections.defaultdict(list)
        for a in ue:
            if a.get('g'): grp[(a['s'], a['g'], bauplan(a))].append(a)
        for xs in grp.values():
            for a in xs[2:]:
                del a['g']; ueber.append(a['f']['text'])
        neu = []
        for g, n in k.get('neu', []):
            _pruefe_neu(n, g, texte); texte.add(n['f']['text'])
            neu.append({'l': lz, 't': tf[lz], 'p': 'uebung', 's': STUFE_VON[g], 'g': g, **json.loads(json.dumps(n))})
        kn = []
        for n in k.get('knobel', []):
            _pruefe_neu(n, 'knobel', texte); texte.add(n['f']['text'])
            kn.append({'l': lz, 't': tf[lz], 'p': 'bonus', 's': 3, 'g': 'knobel', **json.loads(json.dumps(n))})
        assert 1 <= len(kn) <= 2, (lz, 'Knobel')
        assert len(kn) == 2 or k.get('knobel_grund'), (lz, 'Begründung für nur eine Knobel-Bordkarte fehlt')
        alle = ue + neu
        aktiv = [a for a in alle if a.get('g')]
        nach = {s: collections.Counter(a['g'] for a in aktiv if a['s'] == s) for s in (1, 2, 3)}
        for s in (1, 2, 3):
            assert sum(nach[s].values()) >= MIN_ANZ[s], f'{thema}/{lz}: Stufe {s} hat {sum(nach[s].values())} (ohne überzählige), mindestens {MIN_ANZ[s]} – {dict(nach[s])}'
            assert len(nach[s]) >= MIN_TYP[s], f'{thema}/{lz}: Stufe {s} hat Typen {dict(nach[s])}, mindestens {MIN_TYP[s]}'
        zuviel = {g: n for g, n in nach[3].items() if n > 3}
        assert not zuviel, f'{thema}/{lz}: Stufe 3 je Typ höchstens 3: {zuviel}'
        neue_ue[lz] = _ordnen(alle)
        bonus[lz] = kn
        bericht['karten'][lz] = {'leiter': k['leiter'], 'vorher': vorher, 'nachher': {s: dict(nach[s]) for s in (1, 2, 3)},
                                 'neu': len(neu), 'knobel': len(kn), 'knobel_grund': k.get('knobel_grund'),
                                 'umgestuft': umgestuft, 'ueberzaehlig': ueber, 's3_ueber_3': zuviel}
    # neu ordnen: Übungen einer Lernkarte an der Stelle ihrer ersten Übung, Knobel direkt danach
    out, fertig = [], set()
    for a in d['aufgaben']:
        if a['p'] == 'uebung':
            if a['l'] in fertig: continue
            fertig.add(a['l']); out.extend(neue_ue[a['l']]); out.extend(bonus[a['l']])
        else:
            out.append(a)
    d['aufgaben'][:] = out
    # Gegenprobe wie nach dem Sperren: überzählige Übungen weg, dann muss das Prüfskript ohne Fehler durchlaufen
    probe = json.loads(json.dumps(d))
    probe['aufgaben'] = [a for a in probe['aufgaben'] if not (a['p'] == 'uebung' and 'g' not in a)]
    pf = Path('/tmp') / f'stufen_probe_{thema}.json'
    pf.write_text(json.dumps(probe, ensure_ascii=False))
    f, w, info = pruefe(pf)
    assert not f, 'Probe ohne überzählige: ' + '; '.join(f[:8])
    bericht['probe_ohne_ueberzaehlige'] = info
    (Path('/tmp') / f'stufen_{thema}.json').write_text(json.dumps(bericht, ensure_ascii=False, indent=1))
    z = lambda key: sum(len(v[key]) if isinstance(v[key], list) else v[key] for v in bericht['karten'].values())  # noqa: E731
    print(f'  STUFEN {thema}: neu {z("neu")}, Knobel {z("knobel")}, umgestuft {z("umgestuft")}, überzählig {z("ueberzaehlig")}')
    return d
