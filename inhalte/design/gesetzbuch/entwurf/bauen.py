#!/usr/bin/env python3
"""Setzt die Entwürfe aus teile/ zu je einer HTML-Datei zusammen (Schriften und Inhalt eingebettet, kein Nachladen).
Aufruf im Ordner entwurf/:  python3 bauen.py   · vorher bei neuem Inhalt des Mathe-Profis:  python3 inhalt_lesen.py"""
import base64, json, pathlib, re
hier = pathlib.Path(__file__).resolve().parent; teile = hier / 'teile'; repo = hier.parents[3]
lies = lambda n: (teile / n).read_text(encoding='utf-8')
def schrift(name, datei, gewicht):
    b = base64.b64encode((repo / 'vendor' / 'schriften' / datei).read_bytes()).decode()
    return f'@font-face {{ font-family: "{name}"; src: url(data:font/woff2;base64,{b}) format("woff2"); font-weight: {gewicht}; font-display: block; }}\n'
schriften = schrift('Space Grotesk', 'space-grotesk.woff2', '300 700') + schrift('JetBrains Mono', 'jetbrains-mono.woff2', '100 800')
inhalt = json.loads(lies('inhalt.json'))
seiten = {'uebersicht-a': ('a', ''), 'uebersicht-b': ('b', ''), 'gesetz': ('a', 'regel/R6'), 'zeichnungen': ('a', 'zeichnungen')}
for datei, (ueb, start) in seiten.items():
    html = f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Entwurf: Regel-Universum</title>
<!-- ENTWURF des Designers, nicht die App. Gebaut aus entwurf/teile/ mit bauen.py – bitte dort ändern.
     Mathe-Inhalt wörtlich vom Mathe-Profi (origin/mathe-profi {inhalt['stand']}), gelesen mit inhalt_lesen.py. -->
<style>
{schriften}{lies('grund.css')}
{lies('seiten.css')}</style></head>
<body data-g="nacht">
<header class="kopf" id="kopf"></header>
<main id="seite"></main>
<script>
const INHALT = {json.dumps(inhalt, ensure_ascii=False, separators=(',', ':'))};
const START = {json.dumps(start)};
{lies('ideen.js')}
{lies('zeichnen.js')}
{lies('zeichnen2.js')}
{lies('zeichnen3.js')}
{lies(ueb + '.js')}
{lies('gemeinsam.js')}
zeige();
</script></body></html>
'''
    (hier / (datei + '.html')).write_text(html, encoding='utf-8'); print(datei + '.html', len(html) // 1024, 'kB')
