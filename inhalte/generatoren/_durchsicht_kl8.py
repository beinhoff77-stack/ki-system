"""Neunzehnte Runde, Teil A (Klasse 8): Gesamtdurchsicht – Korrekturen an freigegebenen Themen.

Baut auf _befunde.Befunde auf (stufe / loesung / ersetze, Treffer über Lernkarte + genauen Fragetext) und ergänzt:
- neu(...)    zusätzliche Übung; wird HINTEN an „aufgaben“ angehängt (alte Reihenfolge bleibt), eigener Zufallsstart;
- karte(...)  Lernkarte verbessern (einstieg, woerter, bild, schritte, fehler, fehler_bild, regel, probe); lernziel, titel und Reihenfolge bleiben;
- stufen(...) je Lernkarte ein Satz „worin sich die Stufen unterscheiden“ (vorher → nachher) für den Bericht.
Wird NACH allen bisherigen Bauschritten eingesetzt: baue = mit_durchsicht(baue, DS). Nachweis: _durchsicht_nachweis.py.
"""
import collections
import json
from pathlib import Path

from _befunde import Befunde, THEMEN

KARTENFELDER = {'einstieg', 'woerter', 'bild', 'schritte', 'fehler', 'fehler_bild', 'regel', 'probe'}


class Durchsicht(Befunde):
    def __init__(self, thema, seed):
        super().__init__(thema, seed)
        self.karten = {}       # lz -> (felder, vorher_nachher)
        self.stufen_satz = {}  # lz -> (vorher, nachher)
        self.pos = collections.Counter()

    def A(self, text, richtig, falsche, w, h, grafik=None, index=None):
        """Auswahl mit gleichmäßig verteilter Position der richtigen Antwort (eigene Zählung)."""
        if index is None:
            n = min(len({str(x) for x in falsche if str(x) != str(richtig)}), 3) + 1
            frei = [i for i in range(n) if self.pos[(n, i)] == min(self.pos[(n, j)] for j in range(n))]
            index = self.R.choice(frei)
            self.pos[(n, index)] += 1
        return super().A(text, richtig, falsche, w, h, grafik=grafik, index=index)

    def karte(self, lz, meldung, **felder):
        assert set(felder) <= KARTENFELDER, felder
        self.karten[lz] = (felder, meldung)

    def stufen(self, lz, vorher, nachher=None):
        self.stufen_satz[lz] = (vorher, nachher or vorher)

    def anwenden(self, d):
        zusatz, self.zusatz = self.zusatz, []
        super().anwenden(d)           # stufe / loesung / ersetze (an Ort und Stelle)
        self.zusatz = zusatz
        texte = {a['f']['text'] for a in d['aufgaben']}
        tf = {e['lernziel']: next((t['k'] for t in d['inhalt']['teilfaehigkeiten'] if e['lernziel'] in t.get('lernziele', [])), e['lernziel'])
              for e in d['inhalt']['etappen']}
        for lz, s, n in self.zusatz:
            assert n['f']['text'] not in texte, f'schon vorhanden: {n["f"]["text"]}'
            texte.add(n['f']['text'])
            a = {'l': lz, 't': tf[lz], 'p': 'uebung', 's': s, **json.loads(json.dumps(n))}
            assert a.get('h') and len(a['w']) >= 15, a
            d['aufgaben'].append(a)
        self.zaehler['neu'] = len(self.zusatz)
        for e in d['inhalt']['etappen']:
            if e['lernziel'] in self.karten:
                felder, _ = self.karten[e['lernziel']]
                for k, v in felder.items():
                    if v is None: e.pop(k, None)
                    else: e[k] = v
                # Felder in der üblichen Reihenfolge belassen: nichts weiter zu tun (dict-Update ändert die Reihenfolge vorhandener Schlüssel nicht)
        self.zaehler['karten'] = len(self.karten)
        st = collections.Counter((a['l'], a['s']) for a in d['aufgaben'] if a['p'] == 'uebung')
        for e in d['inhalt']['etappen']:
            for s in (1, 2, 3):
                assert st[(e['lernziel'], s)] >= 3, f'{self.thema}/{e["lernziel"]}: nur {st[(e["lernziel"], s)]} Übungen auf Stufe {s}'
        return d

    def bericht(self):
        z = self.zaehler
        return (f'{self.thema}: umgestuft {z["umgestuft"]}, berichtigt {z["berichtigt"]}, ersetzt {z["ersetzt"]}, neu {z["neu"]}, '
                f'Lernkarten verbessert {z["karten"]}')


def mit_durchsicht(baue, ds):
    def baue_durchsicht(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        ds.anwenden(d)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('  DURCHSICHT ' + ds.bericht())
        Path('/tmp').joinpath(f'durchsicht_{ds.thema}.json').write_text(json.dumps(
            {'ersetzt': ds.ersetzt, 'karten': {k: v[1] for k, v in ds.karten.items()}, 'stufen': ds.stufen_satz, 'zaehler': dict(ds.zaehler),
             'nutzer': ds.nutzer}, ensure_ascii=False, indent=1))
        return d
    return baue_durchsicht
