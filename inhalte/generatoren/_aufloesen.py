"""Vierundzwanzigste Runde (Zweig aufloesen): Realschul-/IB-Themen auflösen, wo der Stoff schon da ist.

Grundlage: inhalte/pruefung/klassen/doppelt-rsib.md (Teil 2, Teil 3a) und der Auftrag in inhalte/AUFTRAEGE.md.

Jeder Zielthemen-Generator hat am Ende einen Abschnitt AUFLOESEN, der nach dem vollständigen Bau (alle früheren Runden,
auch BEREINIGEN) aufloesen_datei('<thema>') aufruft. Die Schritte stehen in _af_plan.PLAN['<thema>'] und benutzen dieselben
Bausteine wie die Einundzwanzigste Runde (_bereinigen: karte_her, karte_neu, neu, knobel, pool, karte, weg, vertiefung …).

Unterschied zu _bereinigen: Quelle für karte_her/her ist die Themendatei des aufgelösten Themas, wie sie auf der Platte liegt
(sie bleibt unverändert), OHNE überzählige Übungen (Übungen ohne Typ g). Zwei Lernkarten bekommen im Zielthema einen neuen
Schlüssel, weil der alte dort schon vergeben ist (UMBENENNEN).

Nach dem Anwenden: Regeln der Zwanzigsten Runde je geänderter Lernkarte (prüft _bereinigen.anwenden), Prüfskript ohne
überzählige Übungen fehlerfrei, und Nachweis: jede Aufgabe, die vorher in der Datei stand und nicht ausdrücklich entfernt
wurde, steht danach Zeichen für Zeichen gleich darin.
"""
import collections
import copy
import json
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
THEMEN = HIER.parent / 'themen'
sys.path.insert(0, str(HIER))
import _bereinigen as BR  # noqa: E402
from inhalt_pruefen import pruefe  # noqa: E402  (Pfad setzt _bereinigen)

UMBENENNEN = {('groessen.verhaeltnisse', 'kuerzen'): 'verhaeltnis_kuerzen',
              ('mengen.grundbegriffe', 'verstehen'): 'mengen_verstehen'}
BERICHT = {}


def quelle(thema):
    """Aufgelöstes Thema, wie es auf der Platte liegt, ohne überzählige Übungen; Lernziele ggf. umbenannt."""
    d = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    d['aufgaben'] = [a for a in d['aufgaben'] if not (a['p'] == 'uebung' and not a.get('g'))]
    for (t, alt), neu in UMBENENNEN.items():
        if t != thema: continue
        inh = d['inhalt']
        for e in inh['etappen']:
            if e['lernziel'] == alt: e['lernziel'] = neu
        for ab in inh['abschnitte']: ab['lernziele'] = [neu if x == alt else x for x in ab['lernziele']]
        for k in ('lernziele_pflicht', 'lernziele_vertiefung'):
            inh['bewertung'][k] = [neu if x == alt else x for x in inh['bewertung'].get(k, [])]
        for tf in inh['teilfaehigkeiten']:
            tf['lernziele'] = [neu if x == alt else x for x in tf.get('lernziele', [])]
            if tf['k'] == alt: tf['k'] = neu
        for a in d['aufgaben']:
            if a['l'] == alt: a['l'] = neu
            if a.get('t') == alt: a['t'] = neu
    return d


def _schluessel(a): return json.dumps(a, ensure_ascii=False, sort_keys=True)


def aufloesen_datei(thema):
    from _af_plan import PLAN
    pfad = THEMEN / f'{thema}.json'
    roh_text = pfad.read_text(encoding='utf-8')
    d = json.loads(roh_text)
    vorher = copy.deepcopy(d)
    alt_roh, alt_bericht = BR.roh, BR.BERICHT
    BR.roh = lambda q: quelle(q)
    BR.BERICHT = BERICHT
    try:
        BR.anwenden(d, thema, PLAN[thema])
    finally:
        BR.roh, BR.BERICHT = alt_roh, alt_bericht
    # Nachweis: alte Aufgaben unverändert (bis auf ausdrücklich entfernte)
    b = BERICHT.get(thema, {})
    entfernt = collections.Counter((x['lz'], x['text']) for x in b.get('weg', []))
    nachher = collections.Counter(_schluessel(a) for a in d['aufgaben'])
    fehlt = []
    for a in vorher['aufgaben']:
        k = _schluessel(a)
        if nachher[k] > 0: nachher[k] -= 1; continue
        if entfernt[(a['l'], a['f']['text'])] > 0: entfernt[(a['l'], a['f']['text'])] -= 1; continue
        fehlt.append(a['f']['text'])
    assert not fehlt, f'{thema}: alte Aufgaben verändert: {fehlt[:3]}'
    alt_karten = {e['lernziel']: e for e in vorher['inhalt']['etappen']}
    geaendert_karten = {x['lz'] for x in b.get('karte', [])}
    for e in d['inhalt']['etappen']:
        if e['lernziel'] in alt_karten and e['lernziel'] not in geaendert_karten:
            assert e == alt_karten[e['lernziel']], f'{thema}: Lernkarte {e["lernziel"]} unbeabsichtigt geändert'
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh_text.endswith('\n') else ''), encoding='utf-8')
    probe = copy.deepcopy(d)
    probe['aufgaben'] = [a for a in probe['aufgaben'] if not (a['p'] == 'uebung' and 'g' not in a)]
    pf = Path('/tmp') / f'aufloesen_probe_{thema}.json'
    pf.write_text(json.dumps(probe, ensure_ascii=False))
    f, w, info = pruefe(pf)
    assert not f, f'{thema} Probe ohne überzählige: ' + '; '.join(f[:8])
    (Path('/tmp') / f'aufloesen_{thema}.json').write_text(json.dumps(b, ensure_ascii=False, indent=1))
    print(f'  AUFLOESEN {thema}: ' + ', '.join(f'{k} {len(v)}' for k, v in b.items() if isinstance(v, list) and v))
    return d
