"""Umbau der Themen ohne gym_by (Realschule/IB) auf das neue Muster (Achte Runde, Paket UR, Vorgabe 16.11.;
inhalte/README.md „Verständliche Erklärungen“).

Die Generatoren dieser Themen (_rs.bauen, _ib.bauen) nutzen die alten Beispieltexte der Karten (e['schritte']) beim
Vermeiden von Dopplungen. Darum werden die Aufgaben wie bisher mit den alten Karten erzeugt; erst danach ersetzt
umbau_schreiben() die Erklärfelder (einstieg, woerter, bild, schritte als {text, bild}, fehler, fehler_bild, regel)
und schreibt die Datei neu. So bleiben alle Aufgaben wörtlich gleich. Die alte „probe“ fällt weg; die Kontrolle steht,
wo nötig, als Schritt in der Bildergeschichte.
Gleicher Aufbau wie _umbau_kl7.py / _umbau_kl8.py, eigene Datei, damit die Pakete unabhängig bleiben.
"""
import json
import re
from pathlib import Path

THEMEN = Path(__file__).resolve().parent.parent / 'themen'
PFLICHT = {'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'regel'}
FELDER = PFLICHT | {'fehler_bild'}
VERBOTEN = re.compile(r'\b(offensichtlich|einfach|trivial)\b', re.I)


def pruefe_karte(name, k):
    assert PFLICHT <= set(k) <= FELDER, (name, set(k) ^ PFLICHT)
    assert isinstance(k['bild'], dict) and k['bild'].get('typ'), (name, 'Kartenbild mit typ')
    assert len(k['woerter']) <= 3 and all(len(w) == 2 and w[0] and w[1] for w in k['woerter']), name
    assert 2 <= len(k['schritte']) <= 5 and all(isinstance(s, dict) and s.get('text') for s in k['schritte']), name
    assert any('⟦' in s['text'] for s in k['schritte']), (name, 'Ergebnis in ⟦…⟧')
    for t in [k['einstieg'], k['fehler'], k['regel']] + [s['text'] for s in k['schritte']]:
        assert t.count('⟦') == t.count('⟧'), (name, t)
    for t in [k['einstieg']] + [s['text'] for s in k['schritte']]:
        assert not VERBOTEN.search(t), (name, t)


def ersetze_ganz(k):
    """Ein Schrittbild (oder fehler_bild) MIT „typ“ ist als vollständiges Bild gemeint. Die App führt Bilder gleichen Typs
    aber zusammen ({...vorher, ...neu}). Damit keine alten Felder stehen bleiben, werden Felder des vorigen Zustands,
    die im neuen Bild fehlen, auf null gesetzt."""
    zustand = k['bild']

    def neu(b):
        nonlocal zustand
        if not b:
            return b
        if b.get('typ') and b['typ'] == zustand.get('typ'):
            b = dict(b, **{f: None for f in zustand if f not in b})
        zustand = b if (b.get('typ') and b['typ'] != zustand.get('typ')) else {x: y for x, y in {**zustand, **b}.items() if y is not None}
        return b
    for st in k['schritte']:
        if st.get('bild'):
            st['bild'] = neu(st['bild'])
    if k.get('fehler_bild'):
        k['fehler_bild'] = neu(k['fehler_bild'])


def umbau_schreiben(d, felder, offen=(), weg=()):
    """d: Rückgabe von bauen(); felder: {lernziel: Karte}; offen: neue Einträge für "offen";
    weg: veraltete Einträge in "offen", die durch den Umbau erledigt sind (Anfang des Texts genügt)."""
    et = d['inhalt']['etappen']
    namen = [e['lernziel'] for e in et]
    assert sorted(felder) == sorted(namen), ('UMBAU passt nicht zu den Lernkarten', sorted(set(namen) ^ set(felder)))
    for e in et:
        k = json.loads(json.dumps(felder[e['lernziel']]))
        pruefe_karte(e['lernziel'], k)
        ersetze_ganz(k)
        for f in ('probe', 'fehler_bild', 'zeichnung', 'einstieg_kurz'):
            e.pop(f, None)
        e.update(k)
    alt = [o for o in d.get('offen', []) if not any(o.startswith(w) for w in weg)]
    neu = alt + [o for o in offen if o not in alt]
    if neu:
        d['offen'] = neu
    else:
        d.pop('offen', None)
    pfad = THEMEN / f"{d['thema_schluessel']}.json"
    pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding='utf-8')
    return d


# ---------- Bausteine für Kartenbilder ----------
def ko(x, y, punkte=None, strecken=(), schritt=1, **extra):
    """Koordinatensystem; punkte als {Name: (x, y)} (Name mit _ = ohne Beschriftung)."""
    b = {'typ': 'koordinaten', 'x': list(x), 'y': list(y)}
    if schritt:
        b['schritt_x'] = b['schritt_y'] = schritt
    if punkte:
        b['punkte'] = pkte(punkte)
    if strecken:
        b['strecken'] = [list(s) for s in strecken]
    b.update(extra)
    return b


def pkte(punkte):
    return [{'x': a, 'y': b, 'name': n} for n, (a, b) in punkte.items()]


def rand(*ps):
    """Geschlossener Streckenzug durch die Punkte."""
    return [[*ps[i], *ps[(i + 1) % len(ps)]] for i in range(len(ps))]


def tab(kopf, *zeilen):
    return {'typ': 'tabelle', 'kopf': list(kopf), 'zeilen': [[str(z) for z in r] for r in zeilen]}
