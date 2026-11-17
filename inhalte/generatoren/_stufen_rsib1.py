"""Zwanzigste Runde, Zusatz Realschule/IB, Chat 1 (Zweig stufen-rsib-1).

Gleiche Werkzeuge wie Klasse 9 (siehe _stufen_kl9.py): Stufen, stufen, nachweis, dump.
    python3 -I _stufen_rsib1.py dump <thema>
    python3 -I _stufen_rsib1.py nachweis <thema>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _stufen_kl9 import Stufen, stufen, nachweis, dump  # noqa: E402,F401

if __name__ == '__main__':
    {'dump': dump, 'nachweis': nachweis}[sys.argv[1]](sys.argv[2])
