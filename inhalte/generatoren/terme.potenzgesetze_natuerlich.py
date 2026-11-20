#!/usr/bin/env python3
"""Thema terme.potenzgesetze_natuerlich – Potenzgesetze (natürliche Exponenten), Flug A der Sechsundzwanzigsten Runde.

Die vier Lernkarten kommen mit ihren Lernziel-Schlüsseln aus terme.umformen; Umzug, Ersatz und Zuzug aus terme.potenzgesetze
stehen in _potenz_teilen.py (flug_a).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _potenz_teilen import flug_a  # noqa: E402

if __name__ == '__main__':
    flug_a()
