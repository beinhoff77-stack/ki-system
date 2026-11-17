"""Zwanzigste Runde, Klasse 9 (Zweig stufen-kl9): Aufgabentyp „g“ je Übung, echte Stufe 3, Knobel-Bordkarten.

Aufruf am Ende eines Generators (nach allen früheren Runden):
    ST = Stufen('thema', seed)
    ST.typ('lernziel', 'Textanfang oder /regex/', 'g')      # Typ setzen; die Stufe folgt aus dem Typ
    ST.neu('lernziel', 'g', aufgabe)                         # neue Übung (Bausteine Z/A/L aus _befunde)
    ST.knobel('lernziel', aufgabe)                           # Knobel-Bordkarte (Pool bonus)
    stufen('thema', ST)

Regeln, die hier zusätzlich zum Prüfskript gelten:
- Jede alte Übung bekommt einen Typ. Ab der dritten Übung mit gleichem Typ und gleichem Satzbau je Stufe heißt sie „überzählig“:
  sie bleibt unverändert (ohne g) in der Datei und wird gemeldet; der Haupt-Chat sperrt sie.
- Ebenso überzählig: auf Stufe 3 die vierte und weitere Übung desselben Typs.
- Neue Übungen stehen hinter den alten Übungen ihrer Lernkarte; die Übungen einer Lernkarte werden so geordnet,
  dass nie zwei desselben Typs und nie zwei mit gleichem Satzbau direkt hintereinander stehen.

Kommandozeile:
    python3 -I _stufen_kl9.py dump <thema>       Übersicht je Lernkarte (Muster, Stufe, Vorschlag)
    python3 -I _stufen_kl9.py nachweis <thema>   Vergleich mit origin/lernen-app und Mengenprüfung
"""
import collections
import json
import random
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _befunde import Befunde, _z, _l  # noqa: E402
from _bausatz import jw  # noqa: E402,F401

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
GEDANKEN = {1: ('direkt', 'erkennen'), 2: ('mehrschritt', 'einkleidung', 'umkehr', 'darstellung'),
            3: ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung')}
STUFE_VON = {g: s for s, gs in GEDANKEN.items() for g in gs}
ZAHL = re.compile(r'[−-]?\d+(?:[  ]\d{3})*(?:[,.]\d+)?')
MIN_N = {1: 4, 2: 6, 3: 8}
MIN_T = {1: 2, 2: 3, 3: 4}


def bauplan(a):
    return re.sub(r'\s+', ' ', ZAHL.sub('#', str((a.get('f') or {}).get('text', '')))).strip()


class Stufen:
    def __init__(self, thema, seed):
        self.thema = thema
        self.B = Befunde(thema, seed)      # nur für A(…) mit eigenem Zufall
        self.Z, self.L = _z, _l
        self.regeln = []                   # (lz, muster, g)
        self.neue = []                     # (lz, g, aufgabe)
        self.bonus = []                    # (lz, aufgabe)
        self.leiter = {}                   # lz: (s1, s2, s3)
        self.vorbild = []                  # Quellen der Prüfungsvorbilder

    def A(self, *a, **k): return self.B.A(*a, **k)

    def typ(self, lz, muster, g):
        assert g in STUFE_VON, g
        self.regeln.append((lz, muster, g))

    def neu(self, lz, g, aufgabe):
        assert g in STUFE_VON, g
        self.neue.append((lz, g, aufgabe))

    def knobel(self, lz, aufgabe):
        assert aufgabe.get('h') and len(aufgabe.get('w', '')) >= 60, ('Knobel braucht Tipp und ausführlichen Weg', aufgabe['f']['text'])
        self.bonus.append((lz, aufgabe))

    def stufenleiter(self, lz, s1, s2, s3):
        self.leiter[lz] = (s1, s2, s3)


def _passt(muster, text):
    if muster.startswith('/') and muster.endswith('/'): return re.search(muster[1:-1], text) is not None
    return text.startswith(muster)


def anwenden(d, st):
    auf = d['aufgaben']
    lzs = list(dict.fromkeys(a['l'] for a in auf))
    tf = {a['l']: a['t'] for a in auf if a['p'] == 'uebung'}
    benutzt = collections.Counter()
    ueberzaehlig = []
    ohne = [f'{a["l"]} S{a["s"]}: „{a["f"]["text"]}“' for a in auf if a['p'] == 'uebung'
            and not any(lz == a['l'] and _passt(m, a['f']['text']) for lz, m, g in st.regeln)]
    assert not ohne, 'kein Typ für:\n' + '\n'.join(ohne)
    for a in auf:
        if a['p'] != 'uebung': continue
        treffer = [(i, g) for i, (lz, m, g) in enumerate(st.regeln) if lz == a['l'] and _passt(m, a['f']['text'])]
        i, g = treffer[0]
        benutzt[i] += 1
        a['_g'] = g
    for i, r in enumerate(st.regeln):
        assert benutzt[i], f'Regel ohne Treffer: {r}'
    # überzählig bestimmen: je Lernkarte, Stufe, Typ, Satzbau höchstens 2; Stufe 3 je Typ höchstens 3
    for lz in lzs:
        gruppen, je_typ3 = collections.Counter(), collections.Counter()
        for a in auf:
            if a['l'] != lz or a['p'] != 'uebung': continue
            g = a.pop('_g'); s = STUFE_VON[g]
            schl = (s, g, bauplan(a))
            if gruppen[schl] >= 2 or (s == 3 and je_typ3[g] >= 3):
                ueberzaehlig.append((lz, a['s'], a['f']['text']))
                continue
            gruppen[schl] += 1
            if s == 3: je_typ3[g] += 1
            a['s'] = s
            a['g'] = g
    # neue Übungen und Knobel-Bordkarten
    neu_je = collections.defaultdict(list)
    for lz, g, x in st.neue:
        x = dict(x); x.update({'l': lz, 't': tf[lz], 'p': 'uebung', 's': STUFE_VON[g], 'g': g})
        assert x.get('h'), ('Tipp fehlt', x['f']['text'])
        neu_je[lz].append(x)
    for lz, x in st.bonus:
        x = dict(x); x.update({'l': lz, 't': tf[lz], 'p': 'bonus', 's': 3, 'g': 'knobel'})
        neu_je[lz].append(x)
    texte = {a['f']['text'] for a in auf}
    for xs in neu_je.values():
        for x in xs:
            assert x['f']['text'] not in texte, ('Text gibt es schon', x['f']['text'])
            texte.add(x['f']['text'])
    # einsortieren: alte Übungen der Lernkarte behalten ihre Plätze, neue kommen hinter die letzte Aufgabe der Lernkarte
    neu_auf = []
    for lz in lzs:
        alle = [a for a in auf if a['l'] == lz]
        ue = [a for a in alle if a['p'] == 'uebung'] + [x for x in neu_je[lz] if x['p'] == 'uebung']
        ue = ordnen(ue, lz)
        it = iter(ue)
        for a in alle:
            neu_auf.append(next(it) if a['p'] == 'uebung' else a)
        rest = list(it)
        neu_auf.extend(rest)
        neu_auf.extend(x for x in neu_je[lz] if x['p'] == 'bonus')
    d['aufgaben'] = neu_auf
    return d, ueberzaehlig


def _laeufe_ok(seq):
    lauf, vor = 0, None
    for a in seq:
        b = bauplan(a)
        lauf = lauf + 1 if b == vor else 1
        vor = b
        if lauf >= 3: return False
    return True


def ordnen(ue, lz):
    """Übungen mit Typ: nie zweimal derselbe Typ oder derselbe Satzbau direkt hintereinander.
    Überzählige (ohne Typ) werden so verteilt, dass nie drei gleich gebaute hintereinander stehen."""
    out = []
    rest = [a for a in ue if a.get('g')]
    while rest:
        vor = out[-1] if out else None
        def ok(a):
            return vor is None or (a['g'] != vor.get('g') and bauplan(a) != bauplan(vor))
        zahl = collections.Counter(a['g'] for a in rest)
        kand = [a for a in rest if ok(a)]
        if not kand:
            raise AssertionError(f'{lz}: lässt sich nicht ohne gleiche Typen hintereinander ordnen: ' + ', '.join(a['g'] for a in rest))
        kand.sort(key=lambda a: (-zahl[a['g']], a['s']))
        out.append(kand[0]); rest.remove(kand[0])
    for a in [a for a in ue if not a.get('g')]:
        stufe_ende = max([i + 1 for i, x in enumerate(out) if x['s'] <= a['s']] or [0])
        for pos in list(range(stufe_ende, -1, -1)) + list(range(stufe_ende + 1, len(out) + 1)):
            versuch = out[:pos] + [a] + out[pos:]
            if _laeufe_ok(versuch): out = versuch; break
        else:
            raise AssertionError(f'{lz}: überzählige Übungen lassen sich nicht verteilen')
    return out


def pruefen(d, thema):
    """Mengenregeln der Zwanzigsten Runde auf den Übungen mit Typ (überzählige ohne g zählen nicht)."""
    fehler = []
    lzs = list(dict.fromkeys(a['l'] for a in d['aufgaben']))
    for lz in lzs:
        ue = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung']
        mit = [a for a in ue if a.get('g')]
        for s in (1, 2, 3):
            xs = [a for a in mit if a['s'] == s]
            typen = collections.Counter(a['g'] for a in xs)
            if len(xs) < MIN_N[s]: fehler.append(f'{lz}: Stufe {s} hat {len(xs)} Übungen mit Typ, mindestens {MIN_N[s]}')
            if len(typen) < MIN_T[s]: fehler.append(f'{lz}: Stufe {s} hat {len(typen)} Typen {dict(typen)}, mindestens {MIN_T[s]}')
            if s == 3 and any(n > 3 for n in typen.values()): fehler.append(f'{lz}: Stufe 3 mehr als 3 je Typ {dict(typen)}')
            bau = collections.Counter((a['g'], bauplan(a)) for a in xs)
            for (g, b), n in bau.items():
                if n > 2: fehler.append(f'{lz}: Stufe {s} {g} {n}× „{b[:50]}“')
        for x, y in zip(ue, ue[1:]):
            if x.get('g') and x.get('g') == y.get('g'): fehler.append(f'{lz}: zweimal {x["g"]} hintereinander')
        nb = sum(1 for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'bonus')
        if not 1 <= nb <= 3: fehler.append(f'{lz}: {nb} Knobel-Bordkarten')
    return fehler


def stufen(thema, st):
    pfad = THEMEN / f'{thema}.json'
    roh = pfad.read_text(encoding='utf-8')
    d, ueber = anwenden(json.loads(roh), st)
    f = pruefen(d, thema)
    assert not f, '\n'.join(f)
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + ('\n' if roh.endswith('\n') else ''), encoding='utf-8')
    bericht = {'thema': thema, 'ueberzaehlig': ueber, 'leiter': st.leiter, 'vorbild': st.vorbild,
               'neu': len(st.neue), 'knobel': len(st.bonus)}
    (Path('/home/claude/werk/stufen') / f'{thema}.json').parent.mkdir(parents=True, exist_ok=True)
    (Path('/home/claude/werk/stufen') / f'{thema}.json').write_text(json.dumps(bericht, ensure_ascii=False, indent=1))
    print(f'  STUFEN {thema}: neu {len(st.neue)}, Knobel {len(st.bonus)}, überzählig {len(ueber)}')


# ---------------- Kommandozeile ----------------
def _alt(thema):
    roh = subprocess.run(['git', 'show', f'origin/lernen-app:inhalte/themen/{thema}.json'], capture_output=True, text=True, check=True,
                         cwd=THEMEN.parent.parent).stdout
    return json.loads(roh)


def _schl(a):
    return json.dumps({k: v for k, v in a.items() if k not in ('g', 's')}, ensure_ascii=False, sort_keys=True)


def nachweis(thema):
    alt, neu = _alt(thema), json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    ok = True
    if json.dumps(alt['inhalt'], sort_keys=True) != json.dumps(neu['inhalt'], sort_keys=True): ok = False; print('FEHLER: inhalt (Lernkarten) geändert')
    for k in alt:
        if k not in ('inhalt', 'aufgaben') and alt[k] != neu.get(k): ok = False; print(f'FEHLER: Feld {k} geändert')
    pool = collections.Counter(_schl(a) for a in neu['aufgaben'])
    ums = collections.Counter()
    alt_s = {}
    for a in alt['aufgaben']:
        k = _schl(a)
        if pool[k] <= 0: ok = False; print('FEHLER: alte Aufgabe fehlt/geändert:', a['l'], a['p'], a['f']['text'][:70]); continue
        pool[k] -= 1
        alt_s.setdefault(k, []).append(a.get('s'))
    neue = [a for a in neu['aufgaben'] if pool[_schl(a)] > 0 and not pool.subtract({_schl(a): 1})]
    # Umstufungen zählen
    nk = collections.defaultdict(list)
    for a in neu['aufgaben']: nk[_schl(a)].append(a.get('s'))
    for k, ss in alt_s.items():
        a_s, n_s = sorted(ss), sorted(nk[k])[:len(ss)]
        ums['umgestuft'] += sum(1 for x, y in zip(a_s, n_s) if x != y)
    for a in neue:
        if not a.get('g'): ok = False; print('FEHLER: neue Aufgabe ohne Typ:', a['f']['text'][:60])
    for a in alt['aufgaben']:
        if 'g' in a: ok = False; print('Hinweis: alte Aufgabe hatte schon g')
    f = pruefen(neu, thema)
    for x in f: ok = False; print('FEHLER', x)
    mitg = sum(1 for a in neu['aufgaben'] if a['p'] == 'uebung' and a.get('g'))
    ohneg = sum(1 for a in neu['aufgaben'] if a['p'] == 'uebung' and not a.get('g'))
    print(f'{thema}: neu {sum(1 for a in neue if a["p"] == "uebung")} Übungen + {sum(1 for a in neue if a["p"] == "bonus")} Knobel, '
          f'umgestuft {ums["umgestuft"]}, Übungen mit Typ {mitg}, überzählig (ohne Typ) {ohneg} – ' + ('NACHWEIS OK' if ok else 'NACHWEIS FEHLER'))
    return ok


def vorschlag(a):
    t, s = a['f']['text'], a['s']
    sach = re.search(r'\b(cm|m|km|Liter|€|kg|g|Kiste|Karton|Würfel|Leiter|Turm|Schiff|Rampe|Straße|Weg|Garten|Feld|Grundstück|Becher|Baum|Fluss|Gondel|Hafen)\b', t)
    if s == 1: return 'erkennen' if (a['y'] == 'auswahl' or re.match(r'(Welche|Welcher|Wie viele|Ist |Was gilt|Gib den Punkt)', t)) else 'direkt'
    if s == 2:
        if a['f'].get('grafik') or re.search(r'Bild|Graph|Tabelle|Abbildung', t): return 'darstellung'
        if re.search(r'Für welche|Bestimme [a-z]\b|hat den Wert|rückwärts|Welches x|gesucht', t): return 'umkehr'
        if sach: return 'einkleidung'
        return 'mehrschritt'
    if re.search(r'Jemand|Was ist falsch|Fehler|Was hat .* falsch', t): return 'fehler'
    if re.search(r'Stimmt|behauptet|Welche Aussage|NICHT|begründ|Ohne zu rechnen|Was gilt|immer|Kann ', t): return 'begruenden'
    if re.search(r'Für welche[ns]? (Wert|Zahl|a|b|c|k|n)|für alle|Parameter', t): return 'parameter'
    if sach: return 'transfer'
    return 'verknuepfen'


def dump(thema):
    d = json.loads((THEMEN / f'{thema}.json').read_text(encoding='utf-8'))
    for lz in dict.fromkeys(a['l'] for a in d['aufgaben']):
        e = next(x for x in d['inhalt']['etappen'] if x['lernziel'] == lz)
        print(f'\n#### {lz} | {e["titel"]}\n  BSP: ' + ' / '.join(x['text'] if isinstance(x, dict) else str(x) for x in e.get('schritte', []))[:300])
        ue = [a for a in d['aufgaben'] if a['l'] == lz and a['p'] == 'uebung']
        gr = collections.OrderedDict()
        for a in ue: gr.setdefault((a['s'], bauplan(a)), []).append(a)
        for (s, b), xs in sorted(gr.items(), key=lambda kv: kv[0][0]):
            print(f'  S{s} {len(xs)}× [{vorschlag(xs[0])}] {xs[0]["f"]["text"][:150]}')


if __name__ == '__main__':
    {'dump': dump, 'nachweis': nachweis}[sys.argv[1]](sys.argv[2])
