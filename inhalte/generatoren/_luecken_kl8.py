"""Achtzehnte Runde, Teil B (Klasse 8): fehlende Lernkarten in vorhandenen, freigegebenen Themen ergänzen.

Wird NACH allen bisherigen Bauschritten eines Generators eingesetzt (baue = mit_luecken(baue, LK)). Alles Vorhandene bleibt Zeichen für Zeichen gleich:
- neue Lernkarte wird an der genannten Stelle in inhalt.etappen eingefügt (dazu teilfaehigkeiten, abschnitte, bewertung);
- eine vorhandene Karte kann um einen Schritt erweitert werden (nur diese Karte ändert sich);
- neue Aufgaben werden HINTEN an „aufgaben“ angehängt, mit eigenem festen Zufallsstart und eigener Antwort-Positionsverteilung.
Je neue Lernkarte: 18 Übungen (Stufe 1: 4, Stufe 2: 6, Stufe 3: 8 – feste Prüfungsvorbild-/Knobelaufgaben zuerst), 1 Test, 3 Korrektur, 6 Sicherung.
"""
import collections
import json
import random

from _bausatz import THEMEN

PLAN_NEU = [('uebung', 1)] * 4 + [('uebung', 2)] * 6 + [('uebung', 3)] * 8 + [('test', 2)] + [('korrektur', 2)] * 3 + [('sicherung', 2)] * 6
P, K = 'P', 'K'


def _schl(a):
    """Dublettenschlüssel: Text + Zeichnung; Namen und Reihenfolge der Graphen zählen nicht (gleiche Frage mit nur umbenannten Geraden = doppelt)."""
    g = a['f'].get('grafik')
    if isinstance(g, dict) and g.get('graphen'):
        g = {**g, 'graphen': sorted((json.dumps({x: v for x, v in gr.items() if x != 'name'}, sort_keys=True) for gr in g['graphen']))}
    return a['f']['text'] + '|' + json.dumps(g, sort_keys=True, ensure_ascii=False)


class Luecken:
    def __init__(self, thema, seed):
        self.thema, self.seed = thema, seed
        self.R = random.Random(seed)
        self.pos = collections.Counter()
        self.karten = []      # (karte, nach, abschnitt, gen, fest, vertiefung)
        self.erweitert = []   # (lernziel, index, schritt, aufgaben)
        self.zahl = collections.Counter()

    # Auswahl-Aufgabe mit eigener Positionsverteilung (lässt _bausatz.POS unberührt)
    def A(self, text, richtig, falsche, w, h='', grafik=None, art=None):
        richtig = str(richtig)
        f = []
        for x in map(str, falsche):
            if x != richtig and x not in f: f.append(x)
        assert len(f) >= 2, (text, f)
        f = f[:3]
        self.R.shuffle(f)
        n = len(f) + 1
        frei = [i for i in range(n) if self.pos[(n, i)] == min(self.pos[(n, j)] for j in range(n))]
        i = self.R.choice(frei)
        self.pos[(n, i)] += 1
        f.insert(i, richtig)
        a = {'y': 'auswahl', 'f': {'text': text}, 'a': f, 'o': {'index': i}, 'w': w, 'h': h}
        if grafik: a['f']['grafik'] = grafik
        if art: a['_art'] = art
        return a

    def karte(self, karte, nach, abschnitt, gen, fest=(), vertiefung=False):
        """karte: Lernkarte (neues Muster); nach: lernziel, hinter dem sie steht (None = an den Anfang, '*' = ans Ende);
        abschnitt: Titel des Bereichs, in den sie kommt; gen(R, stufe) -> Aufgabe; fest: Funktionen () -> Aufgabe (mit _art P/K)."""
        self.karten.append((karte, nach, abschnitt, gen, list(fest), vertiefung))

    def erweitere(self, lernziel, index, schritt, aufgaben=()):
        """Schritt an Position index in die vorhandene Karte einfügen; aufgaben: Liste (pool, stufe, Funktion () -> Aufgabe)."""
        self.erweitert.append((lernziel, index, schritt, list(aufgaben)))

    def anwenden(self, d):
        inh = d['inhalt']
        gesehen = {_schl(a) for a in d['aufgaben']}
        neu = []
        for lz, idx, schritt, aufg in self.erweitert:
            e = next(x for x in inh['etappen'] if x['lernziel'] == lz)
            e['schritte'].insert(idx, schritt)
            for pool, st, fn in aufg:
                a = fn()
                a.pop('_art', None)
                assert _schl(a) not in gesehen, a['f']['text']
                gesehen.add(_schl(a))
                neu.append(self._fertig(a, lz, pool, st))
        for karte, nach, abschnitt, gen, fest, vertiefung in self.karten:
            lz = karte['lernziel']
            et = inh['etappen']
            i = 0 if nach is None else (len(et) if nach == '*' else [x['lernziel'] for x in et].index(nach) + 1)
            et.insert(i, karte)
            tf = inh['teilfaehigkeiten']
            j = 0 if nach is None else (len(tf) if nach == '*' else [x['k'] for x in tf].index(nach) + 1)
            tf.insert(j, {'k': lz, 'text': karte['titel'], 'lernziele': [lz]})
            ab = next(x for x in inh['abschnitte'] if x['titel'] == abschnitt)
            if nach in ab['lernziele']: ab['lernziele'].insert(ab['lernziele'].index(nach) + 1, lz)
            else: ab['lernziele'].append(lz)
            bw = inh['bewertung']
            liste = bw['lernziele_vertiefung'] if vertiefung else bw['lernziele_pflicht']
            vorher = [x['lernziel'] for x in et[:i]]
            k = max([liste.index(x) + 1 for x in vorher if x in liste] or [0])
            liste.insert(k, lz)
            beispiele = {s['text'] if isinstance(s, dict) else s for s in karte['schritte']}
            fest = list(fest)
            arten = collections.Counter()
            for pool, st in PLAN_NEU:
                if pool == 'uebung' and st == 3 and fest:
                    a = fest.pop(0)()
                else:
                    for _ in range(4000):
                        a = gen(self.R, st)
                        if a['f']['text'] not in beispiele and _schl(a) not in gesehen: break
                    else:
                        raise SystemExit(f'zu wenige Varianten: {lz} Stufe {st}')
                assert _schl(a) not in gesehen, a['f']['text']
                gesehen.add(_schl(a))
                art = a.pop('_art', None)
                if art: arten[art] += 1
                neu.append(self._fertig(a, lz, pool, st))
            assert arten[P] >= 2 and arten[K] >= 1, (lz, arten)
            self.zahl[lz] = dict(arten)
        d['aufgaben'].extend(neu)

    @staticmethod
    def _fertig(a, lz, pool, st):
        assert len(a['w']) >= 15, a
        if pool == 'uebung': assert a.get('h'), ('Tipp fehlt', a)
        else: a.pop('h', None)
        if not a.get('h'): a.pop('h', None)
        return {'l': lz, 't': lz, 'p': pool, 's': st, **a}


def mit_luecken(baue, lk):
    def baue_luecken(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        lk.anwenden(d)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(f'  LÜCKEN: neue Karten {[k[0]["lernziel"] for k in lk.karten]}, erweitert {[e[0] for e in lk.erweitert]}, '
              f'Aufgaben jetzt {len(d["aufgaben"])}; Vorbild/Knobel {dict(lk.zahl)}')
        return d
    return baue_luecken
