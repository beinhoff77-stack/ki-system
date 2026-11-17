"""Einundzwanzigste Runde, Teil A (Zweig bereinigen): Überschneidungen zusammenlegen, Stoff über dem Lehrplan verschieben.

Jeder betroffene Generator hat am Ende einen Abschnitt BEREINIGEN, der nach dem vollständigen Bau (alle früheren Runden)
bereinigen_datei('<thema>') aufruft. Die Datei wird gelesen, ihr Stand vor dem Bereinigen gemerkt (ROH) und die Schritte aus
_br_plan.PLAN['<thema>'] werden angewendet. Danach wird die Datei geschrieben.

Schritte (alle suchen Aufgaben über Lernkarte + regulären Ausdruck auf den Fragetext, wie in _stufen_kl5._passt:
optional Vorsatz 'S2:' und Nachsatz '@@text'; 'n' = erwartete Trefferzahl, sonst mindestens 1):
  entfaellt(lz)                      Lernkarte mit allen Aufgaben (alle Pools) entfällt
  weg(lz, muster, n)                 Aufgaben (alle Pools) entfernen
  her(quelle, lz_q, lz, muster, n)   Übungen/Knobel aus der Lernkarte lz_q des Themas quelle (Stand VOR dem Bereinigen)
                                     in die Lernkarte lz übernehmen; l und t werden angepasst, sonst Zeichen für Zeichen gleich
  karte_her(quelle, lz_q, abschnitt, vertiefung=False, nach=None)
                                     ganze Lernkarte (Karte, Teilfähigkeit, alle Pools) aus quelle übernehmen, Schlüssel bleibt
  vertiefung(lz)                     Lernkarte wird Vertiefung
  neu(lz, g, aufgabe)                neue Übung (Stufe folgt aus g); knobel(lz, aufgabe) neue Knobel-Bordkarte
  ersetze(lz, muster, aufgabe, g=None)  Aufgabe an gleicher Stelle durch eine neue Fassung ersetzen (alter Text → „ersetzt“)
  karte(lz, **felder)                Felder der Lernkarte setzen (nur wo der Auftrag es verlangt)
  umschreiben(lz, muster, [(regex, ersatz)], n)  Texte umformulieren, Lösung bleibt (neuer Fragetext → alter in „ersetzt“)
  innen(lz_q, lz, muster, n)         Aufgaben (alle Pools) innerhalb des Themas in eine andere Lernkarte
  karte_neu(lz, abschnitt, etappe, tf_text, nach, vertiefung)  neue Lernkarte (für abgetrennten Stoff); teilfaehigkeit(lz, text)
  pool(lz, p, aufgabe)               neue Test-/Korrektur-/Sicherungsaufgabe
  inhalt(**felder), abschnitt(alt, neu)  Ziel/Merke/offen des Themas bzw. Titel eines Bereichs anpassen
Danach je geänderter Lernkarte: Übungen ordnen (nie zweimal derselbe Typ hintereinander) und Regeln der Zwanzigsten Runde
prüfen (ohne überzählige: Stufe 1/2/3 mindestens 4/6/8 Übungen mit 2/3/4 Typen, Stufe 3 je Typ höchstens 3, 1–3 Knobel).
"""
import collections
import copy
import json
import re
import runpy
import sys
from fractions import Fraction as Fr
from pathlib import Path

HIER = Path(__file__).resolve().parent
THEMEN = HIER.parent / 'themen'
sys.path.insert(0, str(HIER.parent.parent / 'tools'))
from inhalt_pruefen import STUFE_VON, bauplan, pruefe  # noqa: E402
from _bausatz import rechne  # noqa: E402

ROH = {}          # thema -> Stand vor dem Bereinigen
BERICHT = {}      # thema -> Bericht
_IN_ARBEIT = set()
MIN_ANZ = {1: 4, 2: 6, 3: 8}
MIN_TYP = {1: 2, 2: 3, 3: 4}


# ---------- Schritte (Datenform) ----------
def entfaellt(lz): return ('entfaellt', lz)
def weg(lz, muster, n=None): return ('weg', lz, muster, n)
def her(quelle, lz_q, lz, muster, n=None, auto=False): return ('her', quelle, lz_q, lz, muster, n, auto)  # auto: nur übernehmen, was die Grenzen einhält
def karte_her(quelle, lz_q, abschnitt, vertiefung=False, nach=None, vor=None): return ('karte_her', quelle, lz_q, abschnitt, vertiefung, nach, vor)
def innen(lz_q, lz, muster, n=None): return ('innen', lz_q, lz, muster, n)             # Aufgaben (alle Pools) in eine andere Karte desselben Themas
def karte_neu(lz, abschnitt, etappe, tf_text, nach=None, vertiefung=False): return ('karte_neu', lz, abschnitt, etappe, tf_text, nach, vertiefung)
def teilfaehigkeit(lz, text): return ('teilfaehigkeit', lz, text)
def pool(lz, p, aufgabe): return ('pool', lz, p, aufgabe)                               # neue Test-/Korrektur-/Sicherungsaufgabe (Stufe 2, ohne Tipp)
def vertiefung(lz): return ('vertiefung', lz)
def neu(lz, g, aufgabe): return ('neu', lz, g, aufgabe)
def knobel(lz, aufgabe): return ('knobel', lz, aufgabe)
def ersetze(lz, muster, aufgabe, g=None, n=1): return ('ersetze', lz, muster, aufgabe, g, n)
def karte(lz, **felder): return ('karte', lz, felder)
def umschreiben(lz, muster, ersetzungen, n=None, felder=('f.text', 'f.schablone', 'f.hinweis', 'a', 'w', 'h')):
    """Texte einer Aufgabe per (regex, ersatz)-Liste umformulieren; Lösung (o, c), Pool, Stufe, Typ und Grafik bleiben.
    Ändert sich der Fragetext, kommt der alte in „ersetzt“; sonst wird nur der Lösungsweg/Tipp geführt."""
    return ('umschreiben', lz, muster, ersetzungen, n, felder)
def inhalt(**felder): return ('inhalt', felder)          # ziel, merke, offen (Liste) usw. des Themas
def abschnitt(alt, neu_titel): return ('abschnitt', alt, neu_titel)


def passt(muster, a):
    s = None
    if re.match(r'^S[123]:', muster): s, muster = int(muster[1]), muster[3:]
    extra = None
    if '@@' in muster: muster, extra = muster.split('@@', 1)
    if s is not None and a.get('s') != s: return False
    if not re.search(muster, a['f']['text']): return False
    if extra and extra not in json.dumps(a, ensure_ascii=False): return False
    return True


def _generator(thema):
    for n in (thema + '.py', thema.replace('.', '_') + '.py'):
        if (HIER / n).exists(): return HIER / n
    raise FileNotFoundError(thema)


def roh(thema):
    """Stand des Themas vor dem Bereinigen (baut es bei Bedarf im selben Prozess)."""
    if thema not in ROH:
        assert thema not in _IN_ARBEIT, f'Kreis beim Bauen: {thema}'
        _IN_ARBEIT.add(thema)
        runpy.run_path(str(_generator(thema)), run_name='__main__')
        _IN_ARBEIT.discard(thema)
        if thema not in ROH:  # Thema ohne eigenen Bereinigen-Abschnitt
            ROH[thema] = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    return copy.deepcopy(ROH[thema])


def _pruefe_neu(a, texte):
    t = a['f']['text']
    assert t not in texte, f'Text schon vorhanden: {t}'
    assert a.get('w') and len(a['w']) >= 15, t
    if a['y'] == 'zahl': assert rechne(a['c']) == Fr(str(a['o']['wert'])), (t, a['c'], a['o'])
    if a['y'] == 'auswahl': assert len(set(a['a'])) == len(a['a']) and 3 <= len(a['a']) <= 4, t
    if a['y'] == 'luecken':
        for c, v in zip(a['c'], a['o']['werte']): assert rechne(c) == Fr(v), (t, c, v)


def _ordnen(xs):
    """Wie in den Stufen-Modulen: nie zweimal derselbe Typ (ohne Typ: derselbe Satzbau) hintereinander."""
    def key(a): return a.get('g') or ('~' + bauplan(a))
    rest, out = list(xs), []
    while rest:
        zaehl = collections.Counter(key(a) for a in rest)
        vk, vb = (key(out[-1]), bauplan(out[-1])) if out else (None, None)
        kand = [a for a in rest if key(a) != vk and bauplan(a) != vb] or rest
        best = max(kand, key=lambda a: (zaehl[key(a)], -a['s'], -rest.index(a)))
        out.append(best)
        rest.remove(best)
    return out


def _tf(d, lz):
    return next(t['k'] for t in d['inhalt']['teilfaehigkeiten'] if lz in t.get('lernziele', []))


def _karte_entfernen(d, lz):
    inh = d['inhalt']
    inh['etappen'] = [e for e in inh['etappen'] if e['lernziel'] != lz]
    for a in inh['abschnitte']: a['lernziele'] = [x for x in a['lernziele'] if x != lz]
    inh['abschnitte'] = [a for a in inh['abschnitte'] if a['lernziele']]
    bw = inh['bewertung']
    for k in ('lernziele_pflicht', 'lernziele_vertiefung'): bw[k] = [x for x in bw.get(k, []) if x != lz]
    for t in inh['teilfaehigkeiten']: t['lernziele'] = [x for x in t.get('lernziele', []) if x != lz]
    inh['teilfaehigkeiten'] = [t for t in inh['teilfaehigkeiten'] if t.get('lernziele')]
    weg_ = [a for a in d['aufgaben'] if a['l'] == lz]
    d['aufgaben'] = [a for a in d['aufgaben'] if a['l'] != lz]
    return weg_


def anwenden(d, thema, plan):
    b = BERICHT.setdefault(thema, {'thema': thema, 'entfaellt': [], 'weg': [], 'her': [], 'karte_her': [], 'vertiefung': [],
                                    'neu': [], 'knobel': [], 'ersetzt': [], 'karte': [], 'verworfen': []})
    texte = lambda: {a['f']['text'] for a in d['aufgaben']}  # noqa: E731
    geaendert = set()
    for op in plan:
        art = op[0]
        if art == 'entfaellt':
            lz = op[1]
            assert any(e['lernziel'] == lz for e in d['inhalt']['etappen']), (thema, lz)
            xs = _karte_entfernen(d, lz)
            b['entfaellt'].append({'lz': lz, 'aufgaben': len(xs), 'texte': [a['f']['text'] for a in xs]})
        elif art == 'weg':
            _, lz, muster, n = op
            xs = [a for a in d['aufgaben'] if a['l'] == lz and passt(muster, a)]
            assert xs and (n is None or len(xs) == n), f'{thema}/{lz} weg „{muster}“: {len(xs)} Treffer, erwartet {n}'
            ids = {id(a) for a in xs}
            d['aufgaben'] = [a for a in d['aufgaben'] if id(a) not in ids]
            b['weg'] += [{'lz': lz, 'p': a['p'], 's': a['s'], 'g': a.get('g'), 'text': a['f']['text']} for a in xs]
            geaendert.add(lz)
        elif art == 'her':
            _, quelle, lz_q, lz, muster, n, auto = op
            q = roh(quelle)
            xs = [a for a in q['aufgaben'] if a['l'] == lz_q and a['p'] in ('uebung', 'bonus') and passt(muster, a)]
            assert xs and (n is None or len(xs) == n), f'{thema}/{lz} her {quelle}/{lz_q} „{muster}“: {len(xs)} Treffer, erwartet {n}'
            tf = _tf(d, lz)
            # einfügen hinter der letzten Übung/Knobel der Ziel-Lernkarte
            letzte = max(i for i, a in enumerate(d['aufgaben']) if a['l'] == lz and a['p'] in ('uebung', 'bonus'))
            neu_ = []
            vorhanden = texte()
            for a in xs:
                if a['f']['text'] in vorhanden:
                    b['verworfen'].append({'lz': lz, 'quelle': f'{quelle}/{lz_q}', 'text': a['f']['text'], 'grund': 'Fragetext schon im Thema'}); continue
                if a['p'] == 'uebung' and not a.get('g'):
                    b['verworfen'].append({'lz': lz, 'quelle': f'{quelle}/{lz_q}', 'text': a['f']['text'], 'grund': 'überzählig (ohne Typ)'}); continue
                if auto:
                    ziel = [x for x in d['aufgaben'] if x['l'] == lz] + neu_
                    zue = [x for x in ziel if x['p'] == 'uebung' and x.get('g')]
                    grund = None
                    if a['p'] == 'bonus' and sum(1 for x in ziel if x['p'] == 'bonus') >= 3: grund = 'schon 3 Knobel-Bordkarten'
                    elif a['p'] == 'uebung' and a['s'] == 3 and sum(1 for x in zue if x['s'] == 3 and x['g'] == a['g']) >= 3: grund = f'Stufe 3 hat schon 3 × „{a["g"]}“'
                    elif a['p'] == 'uebung' and sum(1 for x in zue if x['s'] == a['s'] and x['g'] == a['g'] and bauplan(x) == bauplan(a)) >= 2: grund = 'schon 2 gleich gebaute Übungen dieses Typs'
                    if grund:
                        b['verworfen'].append({'lz': lz, 'quelle': f'{quelle}/{lz_q}', 'text': a['f']['text'], 'grund': grund}); continue
                a = copy.deepcopy(a); a['l'] = lz; a['t'] = tf
                neu_.append(a); vorhanden.add(a['f']['text'])
                b['her'].append({'lz': lz, 'quelle': f'{quelle}/{lz_q}', 'p': a['p'], 's': a['s'], 'g': a.get('g'), 'text': a['f']['text']})
            d['aufgaben'][letzte + 1:letzte + 1] = neu_
            geaendert.add(lz)
        elif art == 'karte_her':
            _, quelle, lz_q, abschnitt, vt, nach, vor = op
            q = roh(quelle)
            e = copy.deepcopy(next(e for e in q['inhalt']['etappen'] if e['lernziel'] == lz_q))
            assert all(x['lernziel'] != lz_q for x in d['inhalt']['etappen']), f'{thema}: Lernziel {lz_q} schon vorhanden'
            et = d['inhalt']['etappen']
            if vor is not None: pos = next(i for i, x in enumerate(et) if x['lernziel'] == vor)
            else: pos = len(et) if nach is None else next(i for i, x in enumerate(et) if x['lernziel'] == nach) + 1
            et.insert(pos, e)
            ab = next((a for a in d['inhalt']['abschnitte'] if a['titel'] == abschnitt), None)
            if ab is None:
                ab = {'titel': abschnitt, 'lernziele': []}; d['inhalt']['abschnitte'].append(ab)
            if vor is not None and vor in ab['lernziele']: ab['lernziele'].insert(ab['lernziele'].index(vor), lz_q)
            elif nach is not None and nach in ab['lernziele']: ab['lernziele'].insert(ab['lernziele'].index(nach) + 1, lz_q)
            else: ab['lernziele'].append(lz_q)
            d['inhalt']['bewertung']['lernziele_vertiefung' if vt else 'lernziele_pflicht'].append(lz_q)
            tq = copy.deepcopy(next(t for t in q['inhalt']['teilfaehigkeiten'] if lz_q in t.get('lernziele', [])))
            tq['lernziele'] = [lz_q]
            k0 = tq['k']; i = 2
            while any(t['k'] == tq['k'] for t in d['inhalt']['teilfaehigkeiten']): tq['k'] = f'{k0}_{i}'; i += 1
            d['inhalt']['teilfaehigkeiten'].append(tq)
            xs = [copy.deepcopy(a) for a in q['aufgaben'] if a['l'] == lz_q]
            vorhanden = texte()
            for a in xs:
                assert a['f']['text'] not in vorhanden, f'{thema}: Text aus {quelle}/{lz_q} schon vorhanden: {a["f"]["text"]}'
                a['t'] = tq['k']
            # Pools in der Reihenfolge der Ziel-Datei: Übungen/Knobel hinter die Übungen der vorigen Karte, Rest ans Ende
            d['aufgaben'] += xs
            b['karte_her'].append({'lz': lz_q, 'quelle': quelle, 'abschnitt': abschnitt, 'vertiefung': vt, 'aufgaben': len(xs), 'texte': [a['f']['text'] for a in xs]})
            geaendert.add(lz_q)
        elif art == 'innen':
            _, lz_q, lz, muster, anz = op
            xs = [a for a in d['aufgaben'] if a['l'] == lz_q and passt(muster, a)]
            assert xs and (anz is None or len(xs) == anz), f'{thema}/{lz_q} innen „{muster}“: {len(xs)} Treffer, erwartet {anz}'
            tf = _tf(d, lz)
            for a in xs:
                a['l'] = lz; a['t'] = tf
                b.setdefault('innen', []).append({'von': lz_q, 'lz': lz, 'p': a['p'], 's': a['s'], 'g': a.get('g'), 'text': a['f']['text']})
            geaendert |= {lz_q, lz}
        elif art == 'karte_neu':
            _, lz, abschnitt, etappe, tf_text, nach, vt = op
            et = d['inhalt']['etappen']
            pos = len(et) if nach is None else next(i for i, x in enumerate(et) if x['lernziel'] == nach) + 1
            et.insert(pos, {'lernziel': lz, **copy.deepcopy(etappe)})
            ab = next(a for a in d['inhalt']['abschnitte'] if a['titel'] == abschnitt)
            if nach in ab['lernziele']: ab['lernziele'].insert(ab['lernziele'].index(nach) + 1, lz)
            else: ab['lernziele'].append(lz)
            d['inhalt']['bewertung']['lernziele_vertiefung' if vt else 'lernziele_pflicht'].append(lz)
            d['inhalt']['teilfaehigkeiten'].append({'k': lz, 'text': tf_text, 'lernziele': [lz]})
            b.setdefault('karte_neu', []).append({'lz': lz, 'abschnitt': abschnitt, 'vertiefung': vt})
        elif art == 'teilfaehigkeit':
            next(t for t in d['inhalt']['teilfaehigkeiten'] if op[1] in t['lernziele'])['text'] = op[2]
        elif art == 'pool':
            _, lz, p, n = op
            assert p in ('test', 'korrektur', 'sicherung') and 'h' not in n
            _pruefe_neu(n, texte())
            d['aufgaben'].append({'l': lz, 't': _tf(d, lz), 'p': p, 's': 2, **copy.deepcopy(n)})
            b['neu'].append({'lz': lz, 'p': p, 's': 2, 'g': None, 'text': n['f']['text']})
        elif art == 'vertiefung':
            lz = op[1]; bw = d['inhalt']['bewertung']
            assert lz in bw['lernziele_pflicht'], (thema, lz)
            bw['lernziele_pflicht'].remove(lz); bw.setdefault('lernziele_vertiefung', []).append(lz)
            b['vertiefung'].append(lz)
        elif art in ('neu', 'knobel'):
            if art == 'neu': _, lz, g, n = op
            else: _, lz, n = op; g = 'knobel'
            _pruefe_neu(n, texte())
            a = {'l': lz, 't': _tf(d, lz), 'p': 'uebung' if art == 'neu' else 'bonus', 's': 3 if g == 'knobel' else STUFE_VON[g], 'g': g,
                 **copy.deepcopy(n)}
            idx = [i for i, x in enumerate(d['aufgaben']) if x['l'] == lz and x['p'] in ('uebung', 'bonus')]
            if idx: d['aufgaben'].insert(max(idx) + 1, a)
            else:  # neue Karte: hinter die Übungen/Knobel der vorigen Karte
                lzs = [e['lernziel'] for e in d['inhalt']['etappen']]
                vorige = set(lzs[:lzs.index(lz)])
                idx = [i for i, x in enumerate(d['aufgaben']) if x['l'] in vorige and x['p'] in ('uebung', 'bonus')]
                d['aufgaben'].insert(max(idx) + 1 if idx else 0, a)
            b[art].append({'lz': lz, 's': a['s'], 'g': g, 'text': n['f']['text']})
            geaendert.add(lz)
        elif art == 'ersetze':
            _, lz, muster, n, g, anz = op
            xs = [(i, a) for i, a in enumerate(d['aufgaben']) if a['l'] == lz and passt(muster, a)]
            assert len(xs) == anz, f'{thema}/{lz} ersetze „{muster}“: {len(xs)} Treffer, erwartet {anz}'
            for i, alt in xs:
                vorhanden = texte() - {alt['f']['text']}
                _pruefe_neu(n, vorhanden)
                a = {k: alt[k] for k in ('l', 't', 'p', 's') if k in alt}
                if alt.get('g'): a['g'] = alt['g']
                if g: a['g'] = g; a['s'] = STUFE_VON[g] if g != 'knobel' else 3
                a.update(copy.deepcopy(n))
                d['aufgaben'][i] = a
                b['ersetzt'].append({'lz': lz, 'p': alt['p'], 'alt': alt['f']['text'], 'neu': n['f']['text']})
            geaendert.add(lz)
        elif art == 'karte':
            _, lz, felder = op
            e = next(e for e in d['inhalt']['etappen'] if e['lernziel'] == lz)
            for k, v in felder.items():
                if v is None: e.pop(k, None)
                else: e[k] = v
            b['karte'].append({'lz': lz, 'felder': sorted(felder)})
        elif art == 'umschreiben':
            _, lz, muster, ers, anz, felder = op
            xs = [a for a in d['aufgaben'] if a['l'] == lz and passt(muster, a)]
            assert xs and (anz is None or len(xs) == anz), f'{thema}/{lz} umschreiben „{muster}“: {len(xs)} Treffer, erwartet {anz}'
            for a in xs:
                alt_text = a['f']['text']; vorher = json.dumps(a, ensure_ascii=False, sort_keys=True)
                def sub(t):
                    for rx, r in ers: t = re.sub(rx, r, t)
                    return t
                for fld in felder:
                    if fld.startswith('f.'):
                        k = fld[2:]
                        if isinstance(a['f'].get(k), str): a['f'][k] = sub(a['f'][k])
                    elif fld == 'a' and isinstance(a.get('a'), list): a['a'] = [sub(x) if isinstance(x, str) else x for x in a['a']]
                    elif isinstance(a.get(fld), str): a[fld] = sub(a[fld])
                assert json.dumps(a, ensure_ascii=False, sort_keys=True) != vorher, f'{thema}/{lz}: umschreiben ändert nichts an „{alt_text}“'
                if a.get('y') == 'auswahl': assert len(set(a['a'])) == len(a['a']), a['a']
                if a['f']['text'] != alt_text:
                    assert sum(1 for x in d['aufgaben'] if x['f']['text'] == a['f']['text']) == 1, f'neuer Text doppelt: {a["f"]["text"]}'
                    b['ersetzt'].append({'lz': lz, 'p': a['p'], 'alt': alt_text, 'neu': a['f']['text']})
                else:
                    b.setdefault('loesungsweg', []).append({'lz': lz, 'p': a['p'], 'text': alt_text})
            geaendert.add(lz)
        elif art == 'inhalt':
            for k, v in op[1].items(): d['inhalt'][k] = v
            b.setdefault('inhalt', []).append(sorted(op[1]))
        elif art == 'abschnitt':
            ab = next(a for a in d['inhalt']['abschnitte'] if a['titel'] == op[1])
            ab['titel'] = op[2]
            b.setdefault('abschnitt', []).append([op[1], op[2]])
        else:
            raise ValueError(art)
    # Übungen je geänderter Lernkarte ordnen: an der Stelle der ersten Übung der Karte, Knobel direkt danach
    for lz in geaendert:
        ue = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung']
        bo = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'bonus']
        ids = {id(a) for a in ue + bo}
        i0 = min(i for i, a in enumerate(d['aufgaben']) if id(a) in ids)
        rest = [a for a in d['aufgaben'] if id(a) not in ids]
        vor = sum(1 for a in d['aufgaben'][:i0] if id(a) not in ids)
        d['aufgaben'] = rest[:vor] + _ordnen(ue) + bo + rest[vor:]
    # Regeln der Zwanzigsten Runde je geänderter Lernkarte
    for lz in geaendert:
        ue = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung' and a.get('g')]
        for s in (1, 2, 3):
            c = collections.Counter(a['g'] for a in ue if a['s'] == s)
            assert sum(c.values()) >= MIN_ANZ[s], f'{thema}/{lz}: Stufe {s} hat {sum(c.values())} Übungen mit Typ, mindestens {MIN_ANZ[s]} – {dict(c)}'
            assert len(c) >= MIN_TYP[s], f'{thema}/{lz}: Stufe {s} hat Typen {dict(c)}, mindestens {MIN_TYP[s]}'
            if s == 3:
                zu = {g: n for g, n in c.items() if n > 3}
                assert not zu, f'{thema}/{lz}: Stufe 3 je Typ höchstens 3: {zu}'
            grp = collections.Counter((a['g'], bauplan(a)) for a in ue if a['s'] == s)
            zu = {k: n for k, n in grp.items() if n > 2}
            assert not zu, f'{thema}/{lz}: Stufe {s}, mehr als 2 gleich gebaute Übungen eines Typs: {zu}'
        kn = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'bonus']
        assert 1 <= len(kn) <= 3, f'{thema}/{lz}: {len(kn)} Knobel-Bordkarten'
    return d


def bereinigen_datei(thema):
    from _br_plan import PLAN
    pfad = THEMEN / f'{thema}.json'
    roh_text = pfad.read_text(encoding='utf-8')
    d = json.loads(roh_text)
    ROH[thema] = copy.deepcopy(d)
    anwenden(d, thema, PLAN[thema])
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh_text.endswith('\n') else ''), encoding='utf-8')
    # Gegenprobe wie nach dem Sperren: ohne überzählige Übungen muss das Prüfskript fehlerfrei sein
    probe = copy.deepcopy(d)
    probe['aufgaben'] = [a for a in probe['aufgaben'] if not (a['p'] == 'uebung' and 'g' not in a)]
    pf = Path('/tmp') / f'bereinigen_probe_{thema}.json'
    pf.write_text(json.dumps(probe, ensure_ascii=False))
    f, w, info = pruefe(pf)
    assert not f, f'{thema} Probe ohne überzählige: ' + '; '.join(f[:8])
    (Path('/tmp') / f'bereinigen_{thema}.json').write_text(json.dumps(BERICHT.get(thema, {}), ensure_ascii=False, indent=1))
    print(f'  BEREINIGEN {thema}: ' + ', '.join(f'{k} {len(v)}' for k, v in BERICHT.get(thema, {}).items() if isinstance(v, list) and v))
    return d
