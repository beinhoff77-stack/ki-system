#!/usr/bin/env python3
"""Siebte Runde: baut EINE Datei index.html mit allen Ansichten (Übersicht, Durch die Klassen, Regelseite, Idee,
Arbeitsweise, Einzelregel, Suche, Lehrer-Blatt). Schriften und Inhalt eingebettet, kein Nachladen aus dem Netz.
Aufruf im Ordner entwurf7/:  python3 bauen.py

Quellen (nur gelesen, nichts davon wird hier verändert):
- ../entwurf/teile/: inhalt.json (Mathe-Profi, eingelesen in Runde 6), Zeichnungen zeichnen*.js, ideen.js, grund.css
- inhalte/mathe-profi/regeln-uebersicht/kennungen.json: Klassen je Schulart, Themen, Fehlbilder (Lehrer-Blatt)
- inhalte/mathe-profi/schritt1/: Aufgaben mit Regel-Kennung (Beispielaufgaben im Lehrer-Blatt)
- teile/kurz.json: Kurzbeschreibungen, gekürzt vom Designer, vom Mathe-Profi zu prüfen
"""
import base64, json, pathlib
hier = pathlib.Path(__file__).resolve().parent; teile = hier / 'teile'; alt = hier.parent / 'entwurf' / 'teile'; repo = hier.parents[3]
mp = repo / 'inhalte' / 'mathe-profi'
lies = lambda p: p.read_text(encoding='utf-8')
def schrift(name, datei, gewicht):
    b = base64.b64encode((repo / 'vendor' / 'schriften' / datei).read_bytes()).decode()
    return f'@font-face {{ font-family: "{name}"; src: url(data:font/woff2;base64,{b}) format("woff2"); font-weight: {gewicht}; font-display: block; }}\n'
schriften = schrift('Space Grotesk', 'space-grotesk.woff2', '300 700') + schrift('JetBrains Mono', 'jetbrains-mono.woff2', '100 800')
inhalt = json.loads(lies(alt / 'inhalt.json'))
kurz = json.loads(lies(teile / 'kurz.json'))['texte']

# Lehrer-Blatt: Kennungen (Klassen je Schulart, Themen, Fehlbilder) und Beispielaufgaben je Rechenregel
ken = {k['kennung']: k for k in json.loads(lies(mp / 'regeln-uebersicht' / 'kennungen.json'))['kennungen']}
etik = json.loads(lies(mp / 'schritt1' / 'etiketten.json'))['aufgaben']
zuord = {a['kennung_aufgabe']: a['regel'] for a in json.loads(lies(mp / 'schritt1' / 'kennungen-zuordnung.json'))['aufgaben']}
dateien = {}
lehrer = {}
for rid, L in inhalt['leitern'].items():
    if not rid.startswith('R'): continue
    k = ken.get(L['kennung'], {})
    aufgaben = []
    for e in etik:  # Reihenfolge in etiketten.json = Reihenfolge in <thema>.neu.json
        if zuord.get(e['kennung']) != L['kennung'] or len(aufgaben) >= 3: continue
        if e['thema'] not in dateien:
            p = mp / 'schritt1' / (e['thema'] + '.neu.json'); dateien[e['thema']] = json.loads(lies(p)) if p.exists() else []
        liste = [x for x in etik if x['thema'] == e['thema']]; i = liste.index(e); a = dateien[e['thema']][i] if i < len(dateien[e['thema']]) else None
        if not a: continue
        o = a.get('o', {}); loesung = ', '.join(str(w) for w in o['werte']) if 'werte' in o else str(o['wert']) if 'wert' in o else a['a'][o['index']] if 'index' in o and a.get('a') else ''
        aufgaben.append({'kennung': e['kennung'], 'klasse': e.get('klasse'), 'lernkarte': e.get('lernkarte'), 'thema': e['thema'], 'text': a['f']['text'], 'auswahl': a.get('a'), 'loesung': loesung, 'weg': a.get('w', '')})
    lehrer[rid] = {'kennung': L['kennung'], 'klassen': k.get('klassen', {}), 'grundlage': k.get('klassen_grundlage', ''), 'themen': k.get('themen', []), 'fehlbilder': k.get('fehlbilder', []), 'aufgaben': aufgaben}

daten = {'inhalt': inhalt, 'kurz': {k: v['text'] for k, v in kurz.items()}, 'lehrer': lehrer}
html = f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Entwurf: Regel-Universum</title>
<!-- ENTWURF des Designers (siebte Runde), nicht die App. Gebaut mit entwurf7/bauen.py – bitte in entwurf7/teile ändern.
     Mathe-Inhalt wörtlich vom Mathe-Profi (origin/mathe-profi {inhalt['stand']}); Kurzbeschreibungen gekürzt vom Designer (teile/kurz.json). -->
<style>
{schriften}{lies(alt / 'grund.css')}
{lies(teile / 'stil.css')}</style></head>
<body data-g="hell">
<header class="kopf" id="kopf"></header>
<main id="seite"></main>
<script>
const DATEN = {json.dumps(daten, ensure_ascii=False, separators=(',', ':'))};
const INHALT = DATEN.inhalt;
{lies(alt / 'ideen.js')}
{lies(alt / 'zeichnen.js')}
{lies(alt / 'zeichnen2.js')}
{lies(alt / 'zeichnen3.js')}
{lies(teile / 'app.js')}
</script></body></html>
'''
(hier / 'index.html').write_text(html, encoding='utf-8'); print('index.html', len(html) // 1024, 'kB', '· Beispielaufgaben:', {k: len(v['aufgaben']) for k, v in lehrer.items()})
