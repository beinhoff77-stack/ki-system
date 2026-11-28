"""Baut inhalte/mathe-profi/vtest-2/*.json aus den Modulen th_*.py (Aufruf: python3 -I inhalte/mathe-profi/vtest-2/bauen.py)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import kern
import th_zinsen
import importlib
for m in ('th_umformen', 'th_umformen2', 'th_kreis', 'th_natuerlich'):
    try:
        mod = importlib.import_module(m)
    except ModuleNotFoundError:
        continue
    th_zinsen.bauen() if False else None
th_zinsen.bauen()
for m in ('th_umformen', 'th_umformen2', 'th_kreis', 'th_natuerlich'):
    try:
        importlib.import_module(m).bauen()
    except ModuleNotFoundError:
        pass
kern.schreiben()
print('gebaut:', {k: len(v) for k, v in kern.ERGEBNIS.items()})
