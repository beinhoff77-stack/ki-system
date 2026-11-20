#!/usr/bin/env python3
"""Thema terme.potenzgesetze_ganzzahlig – Potenzgesetze mit ganzzahligen Exponenten (Gym 8, M8 4), Flug B der Sechsundzwanzigsten Runde.

Lernkarten und Aufgaben stehen in _potenz_teilen_b.py (ETAPPEN_B, AUFGABEN_B); Startbestand sind die 29 Aufgaben mit negativen
Exponenten aus den vier Potenz-Lernkarten (Flug A, bis dahin terme.umformen).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _potenz_teilen_b import flug_b  # noqa: E402

if __name__ == '__main__':
    flug_b()
