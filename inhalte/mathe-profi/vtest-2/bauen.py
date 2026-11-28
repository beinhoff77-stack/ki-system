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
