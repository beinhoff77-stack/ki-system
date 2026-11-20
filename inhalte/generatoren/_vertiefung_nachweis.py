#!/usr/bin/env python3
"""Nachweis Vierzehnte Runde, Teil 2: Gegenüber <git-ref> (Standard origin/lernen-app) hat sich in der Themendatei nur
inhalt.bewertung geändert (Lernkarten aus lernziele_pflicht nach lernziele_vertiefung). Aufgaben, Lernkarten-Texte und alles andere sind gleich.

Aufruf: python3 -I inhalte/generatoren/_vertiefung_nachweis.py <thema_schluessel> [<git-ref>]
"""
import json
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]


def main(schluessel, ref='origin/lernen-app'):
    rel = f'inhalte/themen/{schluessel}.json'
    alt = json.loads(subprocess.run(['git', '-C', str(WURZEL), 'show', f'{ref}:{rel}'], capture_output=True, text=True, check=True).stdout)
    neu = json.loads((WURZEL / rel).read_text(encoding='utf-8'))
    fehler = []
    for k in set(alt) | set(neu):
        if k == 'inhalt': continue
        if alt.get(k) != neu.get(k): fehler.append(f'Feld „{k}“ geändert')
    for k in set(alt['inhalt']) | set(neu['inhalt']):
        if k == 'bewertung': continue
        if alt['inhalt'].get(k) != neu['inhalt'].get(k): fehler.append(f'inhalt.{k} geändert')
    ba, bn = alt['inhalt']['bewertung'], neu['inhalt']['bewertung']
    alle = lambda b: sorted(b['lernziele_pflicht'] + b['lernziele_vertiefung'])
    if alle(ba) != alle(bn): fehler.append('Menge der Lernziele in bewertung geändert')
    if {k: v for k, v in ba.items() if not k.startswith('lernziele_')} != {k: v for k, v in bn.items() if not k.startswith('lernziele_')}:
        fehler.append('andere Felder in bewertung geändert')
    print(f'{schluessel}: Aufgaben ({len(neu["aufgaben"])}) und Lernkarten unverändert: {"JA" if not fehler else "NEIN"}; '
          f'Pflicht {bn["lernziele_pflicht"]}, Vertiefung {bn["lernziele_vertiefung"]}')
    for f in fehler: print('  FEHLER:', f)
    return 1 if fehler else 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
