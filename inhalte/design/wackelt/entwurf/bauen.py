#!/usr/bin/env python3
"""Baut aus teile/ die eine Datei wackelt.html – ohne Netz, Schriften eingebettet.
   Aufruf: python3 bauen.py   (im Ordner entwurf/)"""
import base64, pathlib

hier = pathlib.Path(__file__).parent
repo = hier.parents[3]
lies = lambda n: (hier / 'teile' / n).read_text(encoding='utf-8')


def schrift(name, datei, gewicht):
    b = base64.b64encode((repo / 'vendor' / 'schriften' / datei).read_bytes()).decode()
    return (f'@font-face {{ font-family: "{name}"; src: url(data:font/woff2;base64,{b}) format("woff2"); '
            f'font-weight: {gewicht}; font-display: block; }}\n')


schriften = schrift('Space Grotesk', 'space-grotesk.woff2', '300 700') + schrift('JetBrains Mono', 'jetbrains-mono.woff2', '100 800')

html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Was wackelt? – Entwurf</title>
<style>
{schriften}{lies('wackelt.css')}</style>
</head>
<body>
<div class="seite" id="seite"></div>
<script>
{lies('daten.js')}
{lies('befund.js')}
{lies('wackelt.js')}
</script>
</body>
</html>
'''

ziel = hier / 'wackelt.html'
ziel.write_text(html, encoding='utf-8')
print(f'{ziel.name} {len(html.encode()) // 1024} kB')
