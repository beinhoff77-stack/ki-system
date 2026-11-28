# Vergleichsblätter Entwurf 2 | Umsetzung (echte App-Ansichten). Aufruf: python3 -I vergleich.py
# Die Bilder der Umsetzung entstehen mit: ADV_BILDER=1 node --test --test-name-pattern "^ADV Bilder" tests/lernen.test.cjs
from PIL import Image, ImageDraw, ImageFont
import pathlib
h = pathlib.Path(__file__).parent; E = h.parent / 'entwurf2' / 'bilder'
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
except Exception: F = ImageFont.load_default()
def reihe(bilder, titel, hoehe=None):
    ims = [Image.open(p).convert('RGB') for p in bilder]
    if hoehe: ims = [im.crop((0, 0, im.width, min(hoehe, im.height))) for im in ims]
    H = max(i.height for i in ims) + 28; W = sum(i.width for i in ims) + 12 * (len(ims) - 1)
    r = Image.new('RGB', (W, H), 'white'); d = ImageDraw.Draw(r); x = 0
    for im, t in zip(ims, titel): d.text((x + 4, 6), t, fill='#111', font=F); r.paste(im, (x, 28)); x += im.width + 12
    return r
def stapel(reihen, ziel):
    W = max(r.width for r in reihen); H = sum(r.height for r in reihen) + 16 * (len(reihen) - 1)
    o = Image.new('RGB', (W, H), 'white'); y = 0
    for r in reihen: o.paste(r, (0, y)); y += r.height + 16
    o.save(h / ziel); print(ziel, o.size)
stapel([reihe([E / 'tuer-390-hell.png', h / 'tuer-390-hell.png', E / 'tuer24-390-dunkel.png', h / 'tuer24-390-dunkel.png', E / 'tuer6-390-hell.png', h / 'tuer6-390-hell.png'],
              ['Entwurf 2 · Tür', 'Umsetzung · Tür', 'Entwurf 2 · Tür 24', 'Umsetzung · Tür 24', 'Entwurf 2 · Tür 6', 'Umsetzung · Tür 6'], 844),
        reihe([E / 'inhalt-geschenk-390-hell.png', h / 'inhalt-gutschein-390-hell.png', E / 'inhalt-krampus-390-dunkel.png', h / 'inhalt-krampus-390-dunkel.png', E / 'inhalt-jackpot-390-hell.png', h / 'inhalt-jackpot-390-hell.png'],
              ['Entwurf 2 · Gutschein', 'Umsetzung · Gutschein', 'Entwurf 2 · Krampus', 'Umsetzung · Krampus', 'Entwurf 2 · Jackpot', 'Umsetzung · Jackpot'], 844)], 'vergleich-tuer-entwurf2-umsetzung-390.png')
stapel([reihe([E / 'kalender-390-hell.png', h / 'kalender-390-hell.png', E / 'kalender-390-dunkel.png', h / 'kalender-390-dunkel.png'], ['Entwurf 2 · hell', 'Umsetzung · hell', 'Entwurf 2 · Nacht', 'Umsetzung · Nacht'], 1100)], 'vergleich-kalender-entwurf2-umsetzung-390.png')
stapel([reihe([E / 'karte-v5-390-hell.png', h / 'karte-390-hell.png', E / 'karte-v5-390-dunkel.png', h / 'karte-390-dunkel.png'], ['Entwurf 2 · v5 hell', 'Umsetzung · hell', 'Entwurf 2 · v5 Nacht', 'Umsetzung · Nacht']),
        reihe([E / 'karte-v5-1280-hell.png', h / 'karte-1280-hell.png'], ['Entwurf 2 · v5 1280 hell', 'Umsetzung · 1280 hell'])], 'vergleich-karte-entwurf2-umsetzung.png')
