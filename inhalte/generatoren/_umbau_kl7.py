"""Umbau Klasse 7 auf das neue Muster (Achte Runde, Vorgabe 16.11.; inhalte/README.md „Verständliche Erklärungen“).

Der Abschnitt UMBAU eines Generators überschreibt die Erklärfelder der Lernkarten ERST NACH dem Erzeugen der Aufgaben.
Grund: Die Generatoren nutzen die Beispieltexte der Karten (KLAR aus Runde 7) beim Vermeiden von Dopplungen. KLAR bleibt deshalb stehen;
UMBAU ersetzt danach einstieg, woerter, bild, schritte (als {text, bild}), fehler, fehler_bild und regel. So bleiben alle Aufgaben wörtlich gleich.
Die alte „probe“ fällt weg (die Kontrolle steht, wo nötig, als Schritt in der Bildergeschichte).
Gleicher Aufbau wie _umbau_kl8.py (Paket U8), eigene Datei, damit die Pakete unabhängig bleiben.
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
    assert len(k['woerter']) <= 3 and all(len(w) == 2 and w[0] and w[1] for w in k['woerter']), name
    assert 2 <= len(k['schritte']) <= 5 and all(isinstance(s, dict) and s.get('text') for s in k['schritte']), name
    assert any('⟦' in s['text'] for s in k['schritte']), (name, 'Ergebnis in ⟦…⟧')
    for t in [k['einstieg'], k['fehler'], k['regel']] + [s['text'] for s in k['schritte']]:
        assert t.count('⟦') == t.count('⟧'), (name, t)
    for t in [k['einstieg']] + [s['text'] for s in k['schritte']]:
        assert not VERBOTEN.search(t), (name, t)


def ersetze_ganz(k):
    """Ein Schrittbild (oder fehler_bild) MIT „typ“ ist als vollständiges Bild gemeint. Die App führt Bilder gleichen Typs aber
    zusammen ({...vorher, ...neu}). Damit keine alten Felder (z. B. Winkel zu Punkten, die es nicht mehr gibt) stehen bleiben,
    werden Felder des vorigen Zustands, die im neuen Bild fehlen, auf null gesetzt."""
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


def umbau(d, felder, offen=()):
    et = d['inhalt']['etappen']
    namen = [e['lernziel'] for e in et]
    assert sorted(felder) == sorted(namen), ('UMBAU passt nicht zu den Lernkarten', sorted(set(namen) ^ set(felder)))
    for e in et:
        k = felder[e['lernziel']]
        pruefe_karte(e['lernziel'], k)
        ersetze_ganz(k)
        e.pop('probe', None)
        e.pop('fehler_bild', None)
        e.update(k)
    if offen:
        d['offen'] = list(d.get('offen', [])) + [o for o in offen if o not in d.get('offen', [])]
    return d


def mit_umbau(baue, felder, offen=()):
    def baue_umbau(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        umbau(d, felder, offen)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        return d
    return baue_umbau
