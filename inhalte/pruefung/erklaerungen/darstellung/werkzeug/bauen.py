#!/usr/bin/env python3
"""Baut ../entwurf.html aus entwurf-vorlage.html und den echten Lernkarten (inhalte/themen). Aufruf: python3 bauen.py"""
import json, os
hier = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(hier, '../../../../..'))
liste = {t['thema_schluessel']: t for t in json.load(open(os.path.join(root, 'inhalte/themenliste.json')))}
ZEICHNUNG = {('zahlen.ganz', 'deuten'): 'thermometer', ('zahlen.ganz', 'betrag'): 'betrag', ('bruch.brueche', 'bruchteil_von'): 'bruchteil', ('funktionen.linear', 'ablesen'): 'gerade'}
# Kürzungsvorschlag (als solcher im Entwurf gekennzeichnet)
KURZ = {('zahlen.ganz', 'deuten'): 'Im Winter wird es manchmal kälter als 0 Grad. Für solche Werte ⟦unter null⟧ schreibt man ein Minus vor die Zahl. Diese Zahlen heißen ⟦negative Zahlen⟧.'}
daten = {'themen': {}}
for k in ['zahlen.ganz', 'bruch.brueche', 'funktionen.linear']:
    d = json.load(open(os.path.join(root, 'inhalte/themen', k + '.json'))); t = liste[k]
    et = []
    for e in d['inhalt']['etappen']:
        auf = [a for a in d['aufgaben'] if a['l'] == e['lernziel'] and a['p'] == 'uebung' and a['y'] in ('zahl', 'auswahl')]
        auf.sort(key=lambda a: a.get('s', 2))
        x = {f: e[f] for f in ('lernziel', 'titel', 'regel', 'schritte', 'fehler', 'probe', 'einstieg', 'woerter', 'bild') if f in e}
        if (k, e['lernziel']) in ZEICHNUNG: x['zeichnung'] = ZEICHNUNG[(k, e['lernziel'])]
        if (k, e['lernziel']) in KURZ: x['einstieg_kurz'] = KURZ[(k, e['lernziel'])]
        if x.get('bild', {}).get('typ') != 'zahlenstrahl' and 'bild' in x: x['bild'] = {'typ': x['bild']['typ']}
        if auf: x['aufgabe'] = {f: auf[0][f] for f in ('f', 'y', 'a', 'o', 'w') if f in auf[0]}
        et.append(x)
    daten['themen'][k] = {'titel': t['titel'], 'ort': t.get('ort', ''), 'klasse': t['klasse']['gym_by'], 'abschnitte': d['inhalt'].get('abschnitte'), 'etappen': et}
v = open(os.path.join(hier, 'entwurf-vorlage.html')).read().replace('/*DATEN*/', json.dumps(daten, ensure_ascii=False))
open(os.path.join(hier, '..', 'entwurf.html'), 'w').write(v); print('entwurf.html', len(v) // 1024, 'KB')
