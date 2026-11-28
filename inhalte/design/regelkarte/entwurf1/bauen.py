#!/usr/bin/env python3
"""Baut index.html aus vorlage.html: Schriften (vendor/schriften) als data:-Adresse, Regeldaten aus daten/regeln-universum.json (nur die Beispielregeln).
Aufruf aus dem Repo-Wurzelverzeichnis: python3 -I inhalte/design/regelkarte/entwurf1/bauen.py"""
import base64, json, pathlib
hier = pathlib.Path(__file__).resolve().parent
wurzel = hier.parents[3]
D = json.loads((wurzel / 'daten/regeln-universum.json').read_text())
K = json.loads((wurzel / 'inhalte/mathe-profi/regeln-uebersicht/kennungen.json').read_text())
IDS = ['R1', 'R6', 'R7', 'R13', 'I-geld-3']
ideen = {i['id']: {**i, 'planet': p['name']} for p in D['planeten'] for i in p['ideen']}
regeln = {r['id']: r for r in D['regeln']}
aus = {'regeln': {}, 'themen': D['themen'], 'kennung': {}}
for rid in IDS:
    if rid in regeln:
        r = regeln[rid]; e = {'id': rid, 'art': 'Rechenregel', 'nr': r['nr'], 'name': r['name'], 'satz': r['satz'], 'genau': r['genau'], 'fehler': r['fehler'], 'ort': 'Sonne', 'adresse': rid.lower()}
    else:
        i = ideen[rid]; e = {'id': rid, 'art': 'Idee', 'nr': i['nr'], 'name': i['kurz'], 'satz': i['satz'], 'genau': i['genau'], 'fehler': '', 'ort': i['planet'], 'adresse': 'idee-' + rid[2:]}
    e['leiter'] = D['leitern'][rid]; e['zeichnungen'] = D['zeichnungen'].get(rid, []); e['kurz'] = D['kurz'].get(rid, '')
    aus['regeln'][rid] = e; aus['kennung'][e['leiter']['kennung']] = rid
schrift = lambda n: 'data:font/woff2;base64,' + base64.b64encode((wurzel / 'vendor/schriften' / n).read_bytes()).decode()
t = (hier / 'vorlage.html').read_text()
t = t.replace('/*SCHRIFT_SG*/', schrift('space-grotesk.woff2')).replace('/*SCHRIFT_JB*/', schrift('jetbrains-mono.woff2'))
t = t.replace('/*DATEN*/null', json.dumps(aus, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
(hier / 'index.html').write_text(t)
print('index.html', len(t) // 1024, 'KB')
