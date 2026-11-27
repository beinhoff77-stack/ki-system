"""Neunzehnte Runde, Teil A (Zweig durchsicht-kl5): Gesamtdurchsicht Klasse 5 – Nachbesserungen.

Baut auf _befunde.py (Dreizehnte Runde) auf. Jeder betroffene Generator bekommt am Ende einen Abschnitt DURCHSICHT,
der NACH allen bisherigen Bauschritten auf die fertige Datei angewendet wird:
  stufe(...)    a) nur Feld s ändern                          (Treffer über Lernkarte + Fragetext; enthaelt darf eine Prüffunktion sein)
  loesung(...)  b) o / h / w / c berichtigen, Frage bleibt
  ersetze(...)  c) Aufgabe durch eine bessere mit NEUER Frage ersetzen (gleiche Stelle und Pool) – alter Text kommt in „ersetzt“
  neu(...)      d) zusätzliche Übung (hinter der letzten Aufgabe der Lernkarte)
  karte(...)    e) Lernkarte verbessern (einstieg, woerter, bild, schritte, fehler, fehler_bild, regel, probe) – streng nach README geprüft;
                   Lernziel, Titel und Reihenfolge bleiben. vorher/nachher-Satz kommt in den Bericht.
Alle übrigen Aufgaben und Karten bleiben Zeichen für Zeichen gleich (Nachweis: _durchsicht_kl5_nachweis.py).
Bericht je Thema: /tmp/durchsicht_<thema>.json (Zähler, ersetzt, Karten, für den Nutzer).
"""
import collections
import json
from pathlib import Path

from _befunde import Befunde
from _umbau_kl5 import pruefe_karte


class Durchsicht(Befunde):
    def __init__(self, thema, seed):
        super().__init__(thema, seed)
        self.karten = []        # (lz, felder, vorher_nachher)

    def _treffer(self, d, lz, text, enthaelt, pools):
        out = []
        for i, a in enumerate(d['aufgaben']):
            if a['l'] != lz or a['f']['text'] != text: continue
            if pools and a['p'] not in pools: continue
            if callable(enthaelt):
                if not enthaelt(a): continue
            elif enthaelt and enthaelt not in json.dumps(a, ensure_ascii=False): continue
            out.append(i)
        return out

    def karte(self, lz, vorher_nachher, **felder):
        assert set(felder) <= {'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe'}, felder
        self.karten.append((lz, felder, vorher_nachher))

    def anwenden(self, d):
        for lz, felder, _ in self.karten:
            e = next(x for x in d['inhalt']['etappen'] if x['lernziel'] == lz)
            neu = dict(e)
            neu.update(felder)
            for k in [k for k, v in felder.items() if v is None]:
                neu.pop(k)
            f = []
            pruefe_karte(lz, {k: v for k, v in neu.items() if k not in ('lernziel', 'titel', 'probe')}, f)
            assert not f, 'Karte verletzt Regeln:\n' + '\n'.join(f)
            e.clear(); e.update(neu)
        self.zaehler['karten verbessert'] = len(self.karten)
        super().anwenden(d)
        # mindestens 4 Übungen je Stufe (Neunzehnte Runde)
        st = collections.Counter((a['l'], a['s']) for a in d['aufgaben'] if a['p'] == 'uebung')
        for e in d['inhalt']['etappen']:
            for s in (1, 2, 3):
                assert st[(e['lernziel'], s)] >= 4, f'{self.thema}/{e["lernziel"]}: nur {st[(e["lernziel"], s)]} Übungen auf Stufe {s}'
        return d

    def bericht(self):
        z = self.zaehler
        return (f'{self.thema}: umgestuft {z["umgestuft"]}, berichtigt {z["berichtigt"]}, ersetzt {z["ersetzt"]}, neu {z["neu"]}, '
                f'Lernkarten verbessert {len(self.karten)}')


def durchsicht_anwenden(datei, ds):
    ds.anwenden(datei)
    print('  DURCHSICHT ' + ds.bericht())
    (Path('/tmp') / f'durchsicht_{ds.thema}.json').write_text(json.dumps(
        {'zaehler': dict(ds.zaehler), 'ersetzt': ds.ersetzt, 'karten': [(lz, vn) for lz, _, vn in ds.karten],
         'nutzer': ds.nutzer, 'nicht': ds.nicht}, ensure_ascii=False, indent=1))
    return datei


def mit_durchsicht(baue, ds):
    """Für Generatoren, deren baue(...) die Datei selbst schreibt (Muster mit_befunden in _befunde.py)."""
    from _befunde import THEMEN

    def baue_durchsicht(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        durchsicht_anwenden(d, ds)
        (THEMEN / f"{meta['thema_schluessel']}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        return d
    return baue_durchsicht
