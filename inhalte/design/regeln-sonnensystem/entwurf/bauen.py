#!/usr/bin/env python3
"""Setzt die Entwürfe aus den Teilen zu je einer HTML-Datei zusammen (Schriften eingebettet, kein Nachladen).
Aufruf im Ordner entwurf/:  python3 bauen.py   (liest die Schriften aus vendor/schriften/ des Repos)"""
import base64, pathlib
hier = pathlib.Path(__file__).resolve().parent; teile = hier / 'teile'; repo = hier.parents[3]
def schrift(name, datei, gewicht):
    b = base64.b64encode((repo / 'vendor' / 'schriften' / datei).read_bytes()).decode()
    return f'@font-face {{ font-family: "{name}"; src: url(data:font/woff2;base64,{b}) format("woff2"); font-weight: {gewicht}; font-display: block; }}\n'
schriften = schrift('Space Grotesk', 'space-grotesk.woff2', '300 700') + schrift('JetBrains Mono', 'jetbrains-mono.woff2', '100 800')
ZURUECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
seiten = {'uebersicht-a': ('Regeln am Himmel – Fassung A „Sonnensystem“', 'a'), 'uebersicht-b': ('Regeln am Himmel – Fassung B „Planetenreihe“', 'b'),
          'regel-karte': ('Regel-Karte – Verteilen und Minusklammer', 'karte'), 'wege': ('Drei Wege zur Regel', 'wege')}
for datei, (titel, kern) in seiten.items():
    lies = lambda n: (teile / n).read_text(encoding='utf-8')
    html = f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Entwurf: {titel}</title>
<!-- ENTWURF des Designers, nicht die App. Gebaut aus entwurf/teile/ mit bauen.py – bitte dort ändern. Alle Zustände und Orte sind erfunden. -->
<style>
{schriften}{lies('grund.css')}
{lies(kern + '.css')}</style></head>
<body data-g="nacht">
{lies(kern + '.html').replace('ZURUECK', ZURUECK)}
<script>
{lies('daten.js')}
{lies('gemeinsam.js')}
{lies(kern + '.js')}
</script></body></html>
'''
    (hier / (datei + '.html')).write_text(html, encoding='utf-8'); print(datei + '.html', len(html) // 1024, 'kB')
