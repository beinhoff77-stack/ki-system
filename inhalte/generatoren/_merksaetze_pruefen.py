#!/usr/bin/env python3
"""Prüfung Siebzehnte Runde (Zweig merksaetze), nur Themen mit gym_by-Klasse.

Aufruf: python3 -I inhalte/generatoren/_merksaetze_pruefen.py [inhalte/themen/<datei>.json …]   (Standard: alle Themen)
1. „Kurz gesagt“: erster Satz der regel (Satzende . ! ? vor Leerzeichen oder Textende, nicht nach z. B., d. h., u. a., bzw., ca., usw., vgl.)
   mit mehr als 12 Wörtern oder mehr als 90 Zeichen.
2. Koordinaten-Bilder (Karte, jeder Schrittzustand, fehler_bild): Namen von Graphen, Punkten, Kreisen, Pfeilen, deren Ankerpunkte
   näher als 1 Einheit beieinander liegen (Graphname wie in der App bei name_x, sonst x_max − 12 % der Breite).
Ausgabe: je Fund eine Zeile, am Ende die Zahl der Funde; Rückgabewert 1, wenn etwas gefunden wurde.
"""
import glob
import json
import math
import re
import sys

ABK=('z. B.','d. h.','u. a.','bzw.','ca.','usw.','vgl.')
def erster(t):
    t=t.replace('⟦','').replace('⟧','')
    for m in re.finditer(r'[.!?](?=\s|$)',t):
        vor=t[:m.end()]
        if any(vor.endswith(a) for a in ABK): continue
        nach=t[m.end():]
        if re.search(r'(^|\s)z\.$',vor) and nach.startswith(' B.'): continue
        if re.search(r'(^|\s)d\.$',vor) and nach.startswith(' h.'): continue
        if re.search(r'(^|\s)u\.$',vor) and nach.startswith(' a.'): continue
        return vor
    return t
def wert(g, x):
    a = g.get('a', 1); art = g.get('art')
    try:
        if art == 'linear': return g.get('m', 1) * x + g.get('t', 0)
        if art == 'poly': return sum(c * x ** i for i, c in enumerate(g.get('k', [])))
        if art == 'hyperbel': return a / (x + g.get('b', 0)) + g.get('c', 0)
        if art == 'potenz': return a * x ** g.get('n', 2)
        if art == 'wurzel': return a * math.sqrt(x)
        if art in ('sin', 'cos', 'tan'):
            w = g.get('b', 1) * (x if g.get('bogen') else math.radians(x)) + g.get('c', 0)
            return a * getattr(math, art)(w) + g.get('d', 0)
        if art == 'exp': return a * g.get('b', 2) ** x + g.get('c', 0)
        if art == 'log': return math.log(x) / math.log(g.get('b', 10))
        if art == 'betrag': return a * abs(x - g.get('b', 0)) + g.get('c', 0)
        if art == 'glocke': return a * math.exp(-((x - g.get('mu', 0)) ** 2) / (2 * g.get('sigma', 1) ** 2))
    except (ValueError, ZeroDivisionError, OverflowError): return None
def namen(b):
    x0, x1 = (b.get('x') or [-5, 5]); y0, y1 = (b.get('y') or [-5, 5]); aus = []
    for g in b.get('graphen') or []:
        if g.get('name'):
            xn = g.get('name_x', x1 - (x1 - x0) * 0.12); yn = wert(g, xn)
            if yn is not None and y0 < yn < y1: aus.append(('Graph', g['name'], xn, yn))
    for p in b.get('punkte') or []:
        if p.get('name'): aus.append(('Punkt', p['name'], p['x'], p['y']))
    for k in b.get('kreise') or []:
        if k.get('name'): m = k.get('m', [0, 0]); aus.append(('Kreis', k['name'], m[0] + k['r'] * .71, m[1] + k['r'] * .71))
    for v in b.get('pfeile') or []:
        if len(v) > 4 and v[4]: aus.append(('Pfeil', v[4], (v[0] + v[2]) / 2, (v[1] + v[3]) / 2))
    return aus
def merge(z, b):
    if not b: return z
    if not z or (b.get('typ') and b.get('typ') != z.get('typ')): return b
    return {**z, **b}
def pruefe(pfad, nur_gym=True):
    d = json.load(open(pfad)); funde = []
    if nur_gym and 'gym_by' not in d['klasse']: return funde
    for e in d['inhalt']['etappen']:
        z = e.get('bild'); bilder = [('Karte', z)]
        for i, s in enumerate(e.get('schritte') or []):
            if isinstance(s, dict) and s.get('bild') is not None: z = merge(z, s['bild'])
            bilder.append((f'Schritt {i+1}', z))
        if e.get('fehler_bild'): bilder.append(('fehler_bild', merge(z, e['fehler_bild'])))
        gesehen = set()
        for wo, b in bilder:
            if not b or b.get('typ') != 'koordinaten': continue
            n = namen(b)
            for i in range(len(n)):
                for j in range(i + 1, len(n)):
                    a, c = n[i], n[j]; dist = math.hypot(a[2] - c[2], a[3] - c[3])
                    if dist < 1:
                        key = (a[:2], c[:2], round(dist, 2))
                        funde.append((d['thema_schluessel'], e['lernziel'], wo, a[0], a[1], c[0], c[1], round(dist, 2), key in gesehen)); gesehen.add(key)
    return funde


def main(dateien):
    funde = 0
    for p in dateien or sorted(glob.glob('inhalte/themen/*.json')):
        d = json.load(open(p, encoding='utf-8'))
        if 'gym_by' not in (d.get('klasse') or {}): continue
        for e in d['inhalt']['etappen']:
            s = erster(e['regel'])
            if len(s.split()) > 12 or len(s) > 90:
                funde += 1; print(f'KURZ  {d["thema_schluessel"]} / {e["lernziel"]}: {len(s.split())} Wörter, {len(s)} Zeichen: {s}')
        for f in pruefe(p):
            if not f[8]: funde += 1; print(f'NAMEN {f[0]} / {f[1]} / {f[2]}: {f[3]} „{f[4]}“ und {f[5]} „{f[6]}“ nur {f[7]} Einheiten auseinander')
    print(f'{funde} Funde')
    return 1 if funde else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
