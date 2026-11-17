"""Achtzehnte Runde, Teil B (Zweig luecken-kl9): Lehrplan-Lücken in freigegebenen Themen der Klasse 9 schließen.

Die Generatoren bauen zuerst alles wie bisher (gleiche Zufallsstarts, gleiche Reihenfolge). Danach setzt
einbauen(...) eine NEUE Lernkarte an die vorgesehene Stelle (Lernkarten-Liste, Bereich, Teilfähigkeit,
Pflicht/Vertiefung) und hängt ihre Aufgaben hinten an. erweitern(...) ergänzt eine vorhandene Karte um
Schritte und/oder Übungen. Alle Aufgaben entstehen mit eigenem festem Zufallsstart; alles Alte bleibt
Zeichen für Zeichen gleich und steht in derselben Reihenfolge vorn.

Aufgabenliste: Einträge (pool, stufe, art, aufgabe) mit pool in uebung/test/korrektur/sicherung und
art in 'pruefung' (nach Prüfungsvorbild), 'knobel' oder ''. art dient nur der Zählung, nicht der Datei.

Nachweis:  python3 -I inhalte/generatoren/_luecken_kl9.py <thema> [<thema> …]
"""
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _kl9 import THEMEN, _schluessel, start  # noqa: E402

PLAN_NEU = {('uebung', 1): 4, ('uebung', 2): 6, ('uebung', 3): 8, ('test', 2): 1, ('korrektur', 2): 3, ('sicherung', 2): 6}
TEXT_FELDER = ('einstieg', 'fehler', 'regel', 'probe')


def _lesen(thema):
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    return pfad, roh, json.loads(roh)


def _schreiben(pfad, roh, d):
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')


def _woerter(t):
    return len(re.sub(r'[⟦⟧]', '', t).split())


def _karte_pruefen(e):
    for k in ('lernziel', 'titel', 'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'regel'):
        assert e.get(k), (e.get('lernziel'), 'Feld fehlt', k)
    assert re.fullmatch(r'[a-z0-9_]+', e['lernziel']) and len(e['titel']) <= 40, e['titel']
    assert _woerter(e['einstieg']) <= 35, ('einstieg zu lang', _woerter(e['einstieg']))
    assert len(e['woerter']) <= 3
    alles = e['einstieg'] + ' ' + ' '.join(s['text'] for s in e['schritte'])
    for w, _ in e['woerter']:
        assert w in alles, ('Wort kommt nicht vor', w)
    assert 2 <= len(e['schritte']) <= 5
    for s in e['schritte']:
        assert _woerter(s['text']) <= 15, ('Schritt zu lang', s['text'])
    assert _woerter(e['fehler']) <= 30, ('fehler zu lang', _woerter(e['fehler']))
    assert _woerter(e['regel']) <= 25, ('regel zu lang', _woerter(e['regel']))
    erster = re.split(r'(?<=[.!?])\s', e['regel'])[0]
    assert _woerter(erster) <= 12, ('erster Satz der regel zu lang', erster)


def _aufgaben_dazu(d, liste, lernziele_neu=(), plan=None):
    """Hängt die Aufgaben an; prüft Dubletten, Tipp-Regeln und (für neue Karten) den Plan."""
    lz = [e['lernziel'] for e in d['inhalt']['etappen']]
    beispiele = {re.sub(r'\s+', ' ', s['text'] if isinstance(s, dict) else s).strip()
                 for e in d['inhalt']['etappen'] for s in e.get('schritte', [])}
    gesehen = {_schluessel(a) for a in d['aufgaben']}
    z = Counter()
    for pool, s, art, a in liste:
        assert a is not None, 'Aufgabe nicht gebaut'
        l = a.pop('l')
        assert l in lz, l
        assert pool in ('uebung', 'test', 'korrektur', 'sicherung') and s in (1, 2, 3) and art in ('pruefung', 'knobel', '')
        if pool == 'uebung':
            assert a.get('h'), ('Tipp fehlt', a['f']['text'][:50])
        else:
            assert s == 2 and art == '', (pool, s)
            a.pop('h', None)
        assert len(a.get('w', '')) >= 15, ('Weg fehlt', a['f']['text'][:50])
        if a['y'] == 'zahl': assert 'c' in a, ('c fehlt', a['f']['text'][:50])
        if a['y'] == 'auswahl': assert 3 <= len(a['a']) <= 4
        assert a['f']['text'].strip() not in beispiele, ('gleich wie Beispiel', a['f']['text'][:50])
        k = _schluessel(a)
        assert k not in gesehen, ('doppelt', l, a['f']['text'][:70])
        gesehen.add(k)
        t = a.pop('t', None) or l
        d['aufgaben'].append({'l': l, 't': t, 'p': pool, 's': s, **a})
        z[(l, pool, s, art)] += 1
    for l in lernziele_neu:
        ist = Counter()
        for (x, p, s, _), v in z.items():
            if x == l: ist[(p, s)] += v
        assert dict(ist) == (plan or PLAN_NEU), (l, dict(ist))
        npr = sum(v for (x, p, s, a), v in z.items() if x == l and a == 'pruefung' and p == 'uebung' and s == 3)
        nkn = sum(v for (x, p, s, a), v in z.items() if x == l and a == 'knobel')
        assert npr >= 2 and nkn >= 1, (l, npr, nkn)
    return z


def _bericht(thema, z):
    for l in sorted({k[0] for k in z}):
        teile = Counter()
        for (x, p, s, a), v in z.items():
            if x == l:
                teile[f'{p} S{s}'] += v
                if a: teile[a] += v
        print(f'  {thema}/{l}: ' + ', '.join(f'{k} {v}' for k, v in sorted(teile.items())))


def einbauen(thema, karte, nach, seed, bauplan, pflicht=True, text=None, vertiefung_grund=None):
    """karte: neue Lernkarte (dict). nach: lernziel, hinter das sie kommt (None = ans Ende, letzter Bereich).
    bauplan(): Liste (pool, stufe, art, aufgabe) mit aufgabe['l'] = karte['lernziel']; läuft nach start(seed)."""
    _karte_pruefen(karte)
    pfad, roh, d = _lesen(thema)
    i = d['inhalt']
    lz = [e['lernziel'] for e in i['etappen']]
    neu = karte['lernziel']
    assert neu not in lz, neu
    pos = (lz.index(nach) + 1) if nach else len(lz)
    i['etappen'].insert(pos, karte)
    # Bereich: hinter „nach“ im selben Bereich, sonst ans Ende des letzten Bereichs
    if nach:
        ab = next(a for a in i['abschnitte'] if nach in a['lernziele'])
        ab['lernziele'].insert(ab['lernziele'].index(nach) + 1, neu)
    else:
        i['abschnitte'][-1]['lernziele'].append(neu)
    # Teilfähigkeit
    tf = {'k': neu, 'text': text or karte['titel'], 'lernziele': [neu]}
    ks = [t['k'] for t in i['teilfaehigkeiten']]
    i['teilfaehigkeiten'].insert((ks.index(nach) + 1) if nach in ks else len(ks), tf)
    # Pflicht oder Vertiefung
    b = i['bewertung']
    liste = b['lernziele_pflicht'] if pflicht else b.setdefault('lernziele_vertiefung', [])
    liste.insert((liste.index(nach) + 1) if nach in liste else len(liste), neu)
    if not pflicht and vertiefung_grund:
        d.setdefault('offen', []).append(vertiefung_grund)
    start(seed)
    z = _aufgaben_dazu(d, bauplan(), lernziele_neu=[neu])
    _schreiben(pfad, roh, d)
    _bericht(thema, z)
    print(f'{pfad.name}: Lernkarte {neu} nach {nach} eingebaut, jetzt {len(i["etappen"])} Karten, {len(d["aufgaben"])} Aufgaben')
    return d


def erweitern(thema, lernziel, seed, bauplan=None, schritt=None, felder=None):
    """Vorhandene Karte erweitern: schritt (dict) wird hinten angehängt, felder (dict) ersetzen Kartenfelder
    (z. B. ein vollständiges fehler_bild, damit es zum neuen letzten Schritt passt). bauplan wie bei einbauen."""
    pfad, roh, d = _lesen(thema)
    e = next(x for x in d['inhalt']['etappen'] if x['lernziel'] == lernziel) if lernziel else None  # None: nur Übungen an mehreren Karten
    if schritt:
        e['schritte'].append(schritt)
    for k, v in (felder or {}).items():
        e[k] = v
    if schritt or felder:
        _karte_pruefen(e) if e.get('einstieg') else None
    z = Counter()
    if bauplan:
        start(seed)
        z = _aufgaben_dazu(d, bauplan())
    _schreiben(pfad, roh, d)
    _bericht(thema, z)
    print(f'{pfad.name}: Karte {lernziel or "(mehrere)"} erweitert ({"Schritt, " if schritt else ""}{sum(z.values())} Aufgaben), jetzt {len(d["aufgaben"])} Aufgaben')
    return d


# ---------- Nachweis ----------
def nachweis(thema, basis='origin/lernen-app'):
    alt = json.loads(subprocess.run(['git', 'show', f'{basis}:inhalte/themen/{thema}.json'], capture_output=True, text=True, check=True).stdout)
    _, _, neu = _lesen(thema)
    n = len(alt['aufgaben'])
    fehler = []
    if neu['aufgaben'][:n] != alt['aufgaben']:
        fehler.append('alte Aufgaben nicht unverändert/gleiche Reihenfolge')
    for k in alt:
        if k not in ('aufgaben', 'inhalt', 'offen') and alt[k] != neu.get(k): fehler.append(f'Kopf {k} geändert')
    if alt.get('offen', []) != neu.get('offen', [])[:len(alt.get('offen', []))]: fehler.append('offen geändert')
    ai, ni = alt['inhalt'], neu['inhalt']
    for k in ai:
        if k not in ('etappen', 'abschnitte', 'teilfaehigkeiten', 'bewertung') and ai[k] != ni[k]: fehler.append(f'inhalt.{k} geändert')
    alt_lz = [e['lernziel'] for e in ai['etappen']]
    neu_lz = [e['lernziel'] for e in ni['etappen']]
    dazu = [l for l in neu_lz if l not in alt_lz]
    if [l for l in neu_lz if l in alt_lz] != alt_lz: fehler.append('Reihenfolge der alten Karten geändert')
    geaendert = []
    for e in ai['etappen']:
        f = next(x for x in ni['etappen'] if x['lernziel'] == e['lernziel'])
        if f != e:
            geaendert.append(e['lernziel'] + ' (' + ', '.join(k for k in sorted(set(e) | set(f)) if e.get(k) != f.get(k)) + ')')

    def ohne(xs, key=None):
        return [x for x in xs if (x[key] if key else x) not in dazu]
    for a, b in zip(ai['abschnitte'], ni['abschnitte']):
        if a['titel'] != b['titel'] or [l for l in b['lernziele'] if l not in dazu] != a['lernziele']: fehler.append('Bereiche anders als nur ergänzt')
    if len(ai['abschnitte']) != len(ni['abschnitte']): fehler.append('Zahl der Bereiche geändert')
    if ohne(ni['teilfaehigkeiten'], 'k') != ai['teilfaehigkeiten']: fehler.append('Teilfähigkeiten anders als nur ergänzt')
    for k in ai['bewertung']:
        v = ni['bewertung'].get(k)
        if isinstance(v, list):
            if ohne(v) != ai['bewertung'][k]: fehler.append(f'bewertung.{k} anders als nur ergänzt')
        elif v != ai['bewertung'][k]: fehler.append(f'bewertung.{k} geändert')
    neu_a = neu['aufgaben'][n:]
    je = Counter((a['l'], a['p'], a['s']) for a in neu_a)
    for (l, p, s) in je:
        if l not in dazu and p != 'uebung': fehler.append(f'{l}: neue {p}-Aufgabe an alter Karte')
    print(f'{thema}: {"NACHWEIS OK" if not fehler else "FEHLER: " + "; ".join(fehler)}')
    print(f'  {n} alte Aufgaben unverändert vorn; neue Karten: {dazu or "keine"}; erweiterte Karten: {geaendert or "keine"}; {len(neu_a)} neue Aufgaben')
    for l in sorted({k[0] for k in je}):
        print('   ', l, ', '.join(f'{p} S{s}: {v}' for (x, p, s), v in sorted(je.items()) if x == l))
    return not fehler


if __name__ == '__main__':
    sys.exit(0 if all([nachweis(t) for t in sys.argv[1:]]) else 1)
