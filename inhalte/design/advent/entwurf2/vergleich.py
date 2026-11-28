# Vergleichsbilder alt (Entwurf 1) | neu (Entwurf 2). Aufruf: python3 vergleich.py
from PIL import Image, ImageDraw, ImageFont
import pathlib
h = pathlib.Path(__file__).parent; A = h.parent / 'entwurf1' / 'bilder'; N = h / 'bilder'
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
    o.save(N / ziel); print(ziel, o.size)
for v in ['4', '5']:
    for g in ['hell', 'dunkel']:
        stapel([reihe([A / f'karte-v{v}-390-{g}.png', N / f'karte-v{v}-390-{g}.png'], [f'ALT · Entwurf 1 · v{v} {g}', f'NEU · Entwurf 2 · v{v} {g}'])], f'vergleich-karte-v{v}-alt-neu-390-{g}.png')
stapel([reihe([A / 'tuer-390-hell.png', A / 'tuer-krampus-390-dunkel.png'], ['ALT · Tür', 'ALT · Krampus-Tür'], 620),
        reihe([N / 'tuer-390-hell.png', N / 'tuer-krampus-390-dunkel.png', N / 'tuer6-390-hell.png', N / 'tuer24-390-dunkel.png', N / 'tuer-auf-390-hell.png'], ['NEU · Tür', 'NEU · Krampus-Tür', 'NEU · Tür 6', 'NEU · Tür 24', 'NEU · halb offen (Standbild)'], 620)], 'vergleich-tuer-alt-neu-390.png')
inh = ['inhalt-geschenk-390-hell', 'inhalt-krampus-390-dunkel', 'inhalt-jackpot-390-hell', 'inhalt-niete-390-dunkel']
tt = ['Gutschein', 'Krampus', 'Jackpot', 'Niete']
stapel([reihe([A / (n + '.png') for n in inh], ['ALT · ' + t for t in tt], 600), reihe([N / (n + '.png') for n in inh], ['NEU · ' + t for t in tt], 600)], 'vergleich-inhalte-alt-neu-390.png')
stapel([reihe([A / 'kalender-390-hell.png', N / 'kalender-390-hell.png', A / 'kalender-390-dunkel.png', N / 'kalender-390-dunkel.png'], ['ALT · hell', 'NEU · hell', 'ALT · Nacht', 'NEU · Nacht'], 1000)], 'vergleich-kalender-alt-neu-390.png')
stapel([reihe([A / 'gutscheine-390-hell.png', N / 'gutscheine-390-hell.png', N / 'gutscheine-390-dunkel.png'], ['ALT · hell', 'NEU · hell', 'NEU · Nacht'])], 'vergleich-gutscheine-alt-neu-390.png')
