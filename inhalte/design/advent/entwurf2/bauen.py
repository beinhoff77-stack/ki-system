# Baut entwurf2/index.html aus entwurf1/index.html + teile/*.css + teile/*.js (spätere Funktionen ersetzen gleichnamige frühere).
# Aufruf: python3 inhalte/design/advent/entwurf2/bauen.py
import pathlib, re
hier = pathlib.Path(__file__).parent
alt = (hier.parent / 'entwurf1' / 'index.html').read_text()
css = ''.join(p.read_text() for p in sorted((hier / 'teile').glob('*.css')))
js = ''.join(p.read_text() for p in sorted((hier / 'teile').glob('*.js')))
neu = alt.replace('<title>Adventskalender + Weihnachts-Ebene – Entwurf 1 (Designer)</title>', '<title>Adventskalender + Weihnachts-Ebene – Entwurf 2 (Grafik)</title>')
neu = neu.replace('<!-- Entwurf, kein App-Code.', '<!-- Entwurf 2 (grafische Überarbeitung von Entwurf 1; Quellen in teile/, gebaut mit bauen.py). Entwurf, kein App-Code.', 1)
i = neu.rindex('</style>'); neu = neu[:i] + '\n/* ================= ENTWURF 2 ================= */\n' + css + neu[i:]
i = neu.rindex('\nzeichne();'); neu = neu[:i] + '\n// ================= ENTWURF 2 =================\n' + js + neu[i:]
# Schalterliste: Sonderfälle mit v4, neue Zustände
neu = neu.replace('<a href="#s=karte&v=1&tag=6">6.12.</a><a href="#s=karte&v=1&tag=24">24.12.</a><a href="#s=karte&v=1&tag=31">31.12.</a>', '<a href="#s=karte&v=4&tag=6">6.12.</a><a href="#s=karte&v=4&tag=24">24.12.</a><a href="#s=karte&v=4&tag=31">31.12.</a>')
for a, b in [('<a href="#s=tuer-krampus">Krampus (zu)</a>', '<a href="#s=tuer-krampus">Krampus (zu)</a><a href="#s=tuer&tag=6">Tür 6 (zu)</a><a href="#s=tuer&tag=24">Tür 24 (zu)</a><a href="#s=tuer&auf=1">Tür halb offen (Standbild)</a><a href="#s=inhalt-sterne">Nur Sterne</a>')]:
    neu = neu.replace(a, b)
(hier / 'index.html').write_text(neu)
print('ok', len(neu))
