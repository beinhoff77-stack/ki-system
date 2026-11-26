#!/usr/bin/env python3
"""Setzt den Entwurf des Übungsbildschirms zu einer HTML-Datei zusammen (Schriften eingebettet, kein Nachladen).
Die Zeichnung der Regel kommt unverändert aus dem Regel-Universum (../../gesetzbuch/entwurf/teile). Aufruf:  python3 bauen.py"""
import base64, json, pathlib
hier = pathlib.Path(__file__).resolve().parent; repo = hier.parents[3]; ru = hier.parents[1] / 'gesetzbuch' / 'entwurf' / 'teile'
def schrift(name, datei, gewicht):
    b = base64.b64encode((repo / 'vendor' / 'schriften' / datei).read_bytes()).decode()
    return f'@font-face {{ font-family: "{name}"; src: url(data:font/woff2;base64,{b}) format("woff2"); font-weight: {gewicht}; font-display: block; }}\n'
regel = next(r for r in json.loads((ru / 'inhalt.json').read_text(encoding='utf-8'))['regeln'] if r['id'] == 'R2')
regel = {k: regel[k] for k in ('id', 'nr', 'name', 'satz', 'genau')}
html = f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, interactive-widget=resizes-content">
<title>Entwurf: Übungsbildschirm</title>
<!-- ENTWURF des Designers, nicht die App. Gebaut aus entwurf/teile/ mit bauen.py – bitte dort ändern. -->
<style>
{schrift('Space Grotesk', 'space-grotesk.woff2', '300 700')}{schrift('JetBrains Mono', 'jetbrains-mono.woff2', '100 800')}{(hier / 'teile' / 'uebung.css').read_text(encoding='utf-8')}</style></head>
<body data-g="nacht"><div id="app"></div>
<script>
const REGEL = {json.dumps(regel, ensure_ascii=False)};
{(ru / 'zeichnen.js').read_text(encoding='utf-8')}
{(ru / 'zeichnen2.js').read_text(encoding='utf-8')}
{(hier / 'teile' / 'uebung.js').read_text(encoding='utf-8')}
</script></body></html>
'''
(hier / 'uebung.html').write_text(html, encoding='utf-8'); print('uebung.html', len(html) // 1024, 'kB')
