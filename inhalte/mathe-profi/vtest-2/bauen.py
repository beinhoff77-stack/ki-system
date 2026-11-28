"""Baut inhalte/mathe-profi/vtest-2/*.json aus den Modulen th_*.py (Aufruf: python3 -I inhalte/mathe-profi/vtest-2/bauen.py)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib
import kern
for m in ('th_zinsen', 'th_umformen', 'th_umformen2', 'th_kreis', 'th_natuerlich'):
    importlib.import_module(m).bauen()
kern.schreiben()
print('gebaut:', {k: len(v) for k, v in kern.ERGEBNIS.items()})

# ---- feste Prüfungen (Vorprüfung: Länge/Position der richtigen Möglichkeit, Anteil Auswahl) -------------------------------
alle = [x for xs in kern.ERGEBNIS.values() for x in xs]
au = [x for x in alle if x['aufgabe']['y'] == 'auswahl']
fehler = []
laengste = [x['kennung'] for x in au if (lambda L, i: L[i] == max(L) and L.count(max(L)) == 1)([len(m) for m in x['aufgabe']['a']], x['aufgabe']['o']['index'])]
if len(laengste) > 0.35 * len(au): fehler.append(f'richtige Möglichkeit ist in {len(laengste)} von {len(au)} Auswahlaufgaben die eindeutig längste (erlaubt höchstens 35 %)')
platz = [sum(1 for x in au if x['aufgabe']['o']['index'] == p) for p in range(4)]
if max(platz) > 0.34 * len(au) or min(platz) < 0.16 * len(au): fehler.append(f'Plätze der richtigen Möglichkeit ungleich verteilt: {platz}')
if len(au) > 0.5 * len(alle): fehler.append(f'zu viele Auswahlaufgaben: {len(au)} von {len(alle)}')
tau = [x for x in au if x['pool'] == 'test']
if len(tau) > 7: fehler.append(f'zu viele Auswahlaufgaben im Test-Pool: {len(tau)}')
ide = {}
for x in alle: ide.setdefault(x['lernkarte'], []).append(x['idee'])
for lz, v in ide.items():
    if len(set(v)) < 5 or max(v.count(i) for i in v) > 2: fehler.append(f'{lz}: Ideen {len(set(v))} verschieden, höchstens zweimal gleich verlangt')

# ---- Muster-Prüfungen (zweite Vorprüfung): denn/weil-Einzelgänger, Sammel-Möglichkeit, Absolutwörter ----------------------
import re as _re
_BEG = _re.compile(r'\b(denn|weil)\b')
_ABS = _re.compile(r'\b(immer|nie|nur|jede[rsm]?|stets|alle|kein[e]?|niemals|egal)\b', _re.I)
_SAM = _re.compile(r'^(Beide|Sie sind gleich|Gleich|Alle|Keine)\b')
def _anteil(liste, rx):
    return sum(1 for o in liste if rx.search(o)) / max(1, len(liste))
ri = [(x['aufgabe']['a'][x['aufgabe']['o']['index']]) for x in au]
fa = [m for x in au for i, m in enumerate(x['aufgabe']['a']) if i != x['aufgabe']['o']['index']]
for name, rx, grenze in (('denn/weil', _BEG, 0.12), ('Absolutwörter', _ABS, 0.12)):
    d = _anteil(fa, rx) - _anteil(ri, rx)
    if abs(d) > grenze: fehler.append(f'{name}: falsche Möglichkeiten {100*_anteil(fa, rx):.0f} %, richtige {100*_anteil(ri, rx):.0f} % (Unterschied höchstens {int(100*grenze)} Punkte)')
    for x in au:
        o = x['aufgabe']['a']; r = x['aufgabe']['o']['index']
        mit = [bool(rx.search(m)) for m in o]
        if mit.count(mit[r]) == 1 and len(o) >= 4:      # die richtige ist die einzige mit / einzige ohne
            fehler.append(f'{x["kennung"]}: die richtige Möglichkeit ist als einzige {"mit" if mit[r] else "ohne"} {name}')
        if name == 'denn/weil' and mit.count(False) == 1 and not mit[r] and len(o) >= 4:
            pass
sam = [(x['kennung'], bool(_SAM.search(m)), i == x['aufgabe']['o']['index']) for x in au for i, m in enumerate(x['aufgabe']['a'])]
sam = [s for s in sam if s[1]]
if len(sam) >= 5 and sum(1 for s in sam if s[2]) < 0.25 * len(sam):
    fehler.append(f'Sammel-Möglichkeit („Beide …“, „Gleich …“) ist systematisch falsch: {sum(1 for s in sam if s[2])} richtig von {len(sam)}')
print('Sammel-Möglichkeiten', len(sam), 'davon richtig', sum(1 for s in sam if s[2]), '| denn/weil falsch/richtig %.0f/%.0f %%' % (100*_anteil(fa, _BEG), 100*_anteil(ri, _BEG)), '| Absolutwörter falsch/richtig %.0f/%.0f %%' % (100*_anteil(fa, _ABS), 100*_anteil(ri, _ABS)))
print('Auswahl', len(au), '| Test-Auswahl', len(tau), '| Plätze A-D', platz, '| richtige am längsten', len(laengste))
if fehler:
    print('FEHLER in den festen Prüfungen:'); [print('  ', f) for f in fehler]; raise SystemExit(1)
print('feste Prüfungen: ok')
