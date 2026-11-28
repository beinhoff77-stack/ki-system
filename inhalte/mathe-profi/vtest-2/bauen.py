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
print('Auswahl', len(au), '| Test-Auswahl', len(tau), '| Plätze A-D', platz, '| richtige am längsten', len(laengste))
if fehler:
    print('FEHLER in den festen Prüfungen:'); [print('  ', f) for f in fehler]; raise SystemExit(1)
print('feste Prüfungen: ok')
