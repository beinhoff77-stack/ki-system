#!/usr/bin/env python3
"""EX-App: Stationen der Expeditionen für die Kinderseite (Stempel-Sammlung, Freischalt-Ansicht).

Quelle: inhalte/reise/aufbau-vorschlag.json (expeditionen[] – Reihenfolge = Stationsnummer),
inhalte/expeditionen/*.json (Titel, Klasse, Voraussetzungen), inhalte/themen/*.json (Etappen-Titel),
inhalte/themenliste.json (Thema-ID und Flug-Titel).
Schreibt den Block zwischen den Markern in lernen.js neu. Aufruf: python3 -I tools/ex_stationen.py
"""
import json
import os
import re
import sys

WURZEL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANFANG, ENDE = '// <EX-STATIONEN> (erzeugt von tools/ex_stationen.py – nicht von Hand ändern)', '// </EX-STATIONEN>'


def lade(pfad):
    with open(os.path.join(WURZEL, pfad), encoding='utf-8') as f:
        return json.load(f)


def kurzname(name):
    """Name der Station ohne „-Station“ und Klammer, als ganze Wörter (Sammlung: nie abgeschnitten)."""
    n = re.sub(r'\s*\(.*?\)', '', name)
    n = n.replace('-Südpolstation', '').replace('-Station', '').replace(' Station', '')
    if n.startswith('Amundsen-Scott'):
        return n
    return n.replace('-', ' ')


def main():
    aufbau = lade('inhalte/reise/aufbau-vorschlag.json')
    themen = {t['thema_schluessel']: t for t in lade('inhalte/themenliste.json')}
    stationen = []
    for nr, s in enumerate(aufbau['expeditionen'], 1):
        x = lade(f"inhalte/expeditionen/{s['expedition']}.json")
        vor = []
        for v in x['voraussetzungen']:
            basis = re.sub(r'_teil\d+$', '', v['thema_schluessel'])
            etappen = {e['lernziel']: e['titel'] for e in lade(f'inhalte/themen/{basis}.json')['inhalt']['etappen']}
            if v['lernziel'] not in etappen or basis not in themen:
                sys.exit(f"Voraussetzung nicht gefunden: {s['expedition']} {v}")
            vor.append({'thema': themen[basis]['thema_id'], 'lernziel': v['lernziel'], 'etappe': etappen[v['lernziel']], 'flug': themen[basis]['titel']})
        klasse = min(x['klasse'].values()) if x.get('klasse') else None
        stationen.append({'schluessel': s['expedition'], 'nr': nr, 'station': s['station'], 'kurz': kurzname(s['station']), 'betreiber': s['betreiber'],
                          'breite': round(s['breite'], 4), 'laenge': round(s['laenge'], 4), 'titel': x['titel'], 'klasse': klasse, 'teile': len(x['teile']) if isinstance(x.get('teile'), list) else x.get('teile'), 'vor': vor})
    zeilen = [ANFANG, f"// Quelle Stationen: {aufbau['quellen'].get('stationen', 'COMNAP')}", 'const LERN_EX_STATIONEN = [']
    zeilen += ['  ' + json.dumps(s, ensure_ascii=False, separators=(',', ':')) + ',' for s in stationen]
    zeilen += ['];', ENDE]
    pfad = os.path.join(WURZEL, 'lernen.js')
    with open(pfad, encoding='utf-8') as f:
        text = f.read()
    a, e = text.find(ANFANG), text.find(ENDE)
    if a < 0 or e < 0:
        sys.exit('Marker in lernen.js fehlen')
    neu = text[:a] + '\n'.join(zeilen) + text[e + len(ENDE):]
    if neu != text:
        with open(pfad, 'w', encoding='utf-8') as f:
            f.write(neu)
    print(f'{len(stationen)} Stationen geschrieben')


if __name__ == '__main__':
    main()
