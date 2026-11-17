"""Zweiundzwanzigste Runde (18.11., Auftrag des Lehrers): mehr Textaufgaben in Klasse 8.

Wird NACH allen bisherigen Bauschritten eingesetzt: baue = mit_text(baue, TX) bzw. text_auf_datei(TX, d).

Textaufgabe = Sachsituation in ganzen Sätzen; das Kind liest Gegebenes und Gesuchtes heraus, übersetzt in Mathematik,
löst und antwortet im Sachzusammenhang.
- Alte Aufgaben zählen als Textaufgabe, wenn ihr Typ einkleidung/transfer ist (Zählung des Lehrers) oder wenn ihr
  Fragetext eine Sachsituation enthält (Regel sach(), je Thema mit eigenen Mustern; Liste im Bericht).
- u(lz, g, aufgabe, huerde=None)  neue Text-Übung (Stufe aus g). huerde: ueberfluessig | fehlend | deuten | zwei | entscheidung
- s(lz, aufgabe) / k(lz, aufgabe) neue Textaufgabe für Sicherung bzw. Korrektur (Stufe 2, ohne Tipp).
- ausnahme(lz, grund)             Lernkarte, bei der weniger Textaufgaben fachlich sinnvoll sind.
Überzählig: Ist der Anteil des Themas unter 40 % oder hätte ein Typ auf Stufe 3 mehr als 3 Aufgaben, verlieren alte
reine Rechenaufgaben ihr g (nicht gelöscht; beim Einspielen gesperrt). Mindestmengen 4/6/8 und Typen 2/3/4 bleiben.
Alte Aufgaben bleiben sonst Zeichen für Zeichen gleich.
"""
import collections
import json
import re
from fractions import Fraction as Fr
from pathlib import Path

from _befunde import THEMEN, _l
from _bausatz import jw, rechne
from _stufen_kl8 import Stufen, MIND
from inhalt_pruefen import STUFE_VON, bauplan

TXT = {'einkleidung', 'transfer'}
HUERDEN = {'ueberfluessig', 'fehlend', 'deuten', 'zwei', 'entscheidung'}
import random

KONTEXT = re.compile(
    r'€|\bEuro\b|\bCent\b|\bkm\b|km/h|\bkg\b|\bLiter\b|\b\d+ ?l\b|\bml\b|Minute|Stunde|\bTag(e|en)?\b|Woche|Monat|Jahr|Tarif|Handy|Taxi|Kerze|Pumpe|Becken|Tank|'
    r'Fahrt|Fahrrad|\bRad\b|Bus\b|Zug|Klasse|Schüler|Kinder|Freund|Preis|kostet|zahlt|Konto|Gewinn|Wasser|Pizza|Garten|Zaun|Dose|Glas|Kiste|Packung|Karton|'
    r'Beet|Tisch|Rohr|Turm|Zelt|Pool|Schwimmbad|Becher|Kanne|Eimer|Paket|Maler|Arbeiter|Bagger|Maschine|Lkw|Auto|Läufer|Wanderer|Rezept|Kuchen|Torte|'
    r'\bSpiel(e|en)?\b|Umfrage|Verein|Mannschaft|Team|Laden|Kino|Konzert|Ticket|Eintritt|Miete|Strom|Handwerker|Fliesen|Farbe|Futter|Pferd|'
    r'Ballon|Flugzeug|Schiff|Boot|Brücke|Straße|Weg\b|Stadt|Dorf|Karte|Maßstab|Temperatur|°C|Thermometer|Messwert|Geschwindigkeit|Sportplatz|Laufbahn|Rasen|'
    r'Fenster|Tür|Dach|Wand|Zimmer|\bRaum\b|Haus|Schachtel|Verpackung|Blech|Folie|Stoff|Seil|Schnur|Draht|Uhr|Reifen|Teller|Brunnen|Silo|Kanal|Regen|'
    r'Tropfen|Vase|Aquarium|Kerzen|Sitz|Party|Feier|Ausflug|Reise|Urlaub|Flug|Hotel|Fähre|Strand|Markt|Obst|Äpfel|Saft')


def ist_sach(text):
    """Grobe Vorauswahl: Sachwort und mindestens zwei Sätze bzw. 90 Zeichen. Würfel, Münze, Urne und Glücksrad allein sind
    ein Modell, keine Sachsituation – sie zählen nicht."""
    return bool(KONTEXT.search(text)) and (len(re.findall(r'[.?!]', text)) >= 2 or len(text) >= 90)


class Text:
    def __init__(self, thema, seed):
        self.thema = thema
        self.R = random.Random(seed)
        self.pos = collections.Counter()
        self.neue = []          # (lz, pool, g, aufgabe, huerde)
        self.ja, self.nein = [], []   # (lz, regex) Sachsituation ja / nein für alte Aufgaben
        self.ausnahmen = {}
        self.alt_huerden = []
        self.ueberzaehlig = []
        self.bericht_daten = {}

    # ---------- Bausteine (Lösung wird aus c berechnet) ----------
    @staticmethod
    def W(gegeben, gesucht, ansatz, rechnung, antwort):
        """Lösungsweg in Schritten: gegeben · gesucht · Ansatz · Rechnung · Antwortsatz."""
        return f'Gegeben: {gegeben} Gesucht: {gesucht} Ansatz: {ansatz} Rechnung: {rechnung} Antwort: {antwort}'

    @staticmethod
    def Z(text, c, w, h='', einheit=None, toleranz=None):
        if toleranz is not None and not c.startswith('round('):
            n = len(str(toleranz).split('.')[1]) if '.' in str(toleranz) else 0
            c = f'round({c}, {n})' if n else f'round({c})'
        wert = rechne(c)
        assert wert.denominator in (1, 2, 4, 5, 8, 10, 20, 25, 50, 100, 1000) or toleranz is not None, f'keine endliche Dezimalzahl: {c} = {wert} ({text})'
        o = {'wert': jw(wert)}
        if einheit: o['einheit'] = einheit
        if toleranz is not None: o['toleranz'] = toleranz
        return {'y': 'zahl', 'f': {'text': text}, 'o': o, 'c': c, 'w': w, 'h': h}

    def A(self, text, richtig, falsche, w, h=''):
        richtig = str(richtig)
        f = []
        for x in map(str, falsche):
            if x != richtig and x not in f: f.append(x)
        assert 2 <= len(f) <= 3, (text, f)
        self.R.shuffle(f)
        n = len(f) + 1
        frei = [i for i in range(n) if self.pos[(n, i)] == min(self.pos[(n, j)] for j in range(n))]
        i = self.R.choice(frei)
        self.pos[(n, i)] += 1
        f.insert(i, richtig)
        return {'y': 'auswahl', 'f': {'text': text}, 'a': f, 'o': {'index': i}, 'w': w, 'h': h}

    @staticmethod
    def L(text, schablone, c, w, h='', hinweis='Je Lücke eine ganze Zahl.'):
        werte = [rechne(x) for x in c]
        assert all(v.denominator == 1 for v in werte), (text, werte)
        return _l(text, schablone, [int(v) for v in werte], c, w, h, hinweis=hinweis)

    # ---------- Einträge ----------
    def u(self, lz, g, aufgabe, huerde=None):
        assert g in STUFE_VON and g not in ('knobel',), g
        assert huerde is None or huerde in HUERDEN, huerde
        assert aufgabe.get('h'), f'Tipp fehlt: {aufgabe["f"]["text"]}'
        self.neue.append((lz, 'uebung', g, aufgabe, huerde))

    def s(self, lz, aufgabe):
        self.neue.append((lz, 'sicherung', None, aufgabe, None))

    def k(self, lz, aufgabe):
        self.neue.append((lz, 'korrektur', None, aufgabe, None))

    def sach(self, lz, muster):
        self.ja.append((lz, re.compile(muster)))

    def keine_sach(self, lz, muster):
        self.nein.append((lz, re.compile(muster)))

    def huerde_alt(self, lz, muster, art):
        """Alte Stufe-3-Sachaufgabe, die schon eine Hürde hat (zählt für „mindestens zwei mit Hürde“)."""
        assert art in HUERDEN, art
        self.alt_huerden.append((lz, re.compile(muster), art))

    def ausnahme(self, lz, grund):
        self.ausnahmen[lz] = grund

    def _alt_sach(self, a):
        t = a['f']['text']
        if any(lz in ('*', a['l']) and rx.search(t) for lz, rx in self.nein): return False
        if a.get('g') in TXT: return True
        if any(lz in ('*', a['l']) and rx.search(t) for lz, rx in self.ja): return True
        return ist_sach(t)

    # ------------------------------------------------------------------
    def anwenden(self, d):
        auf = d['aufgaben']
        karten = [e['lernziel'] for e in d['inhalt']['etappen']]
        tf = {e['lernziel']: next((t['k'] for t in d['inhalt']['teilfaehigkeiten'] if e['lernziel'] in t.get('lernziele', [])), e['lernziel'])
              for e in d['inhalt']['etappen']}
        for a in auf:
            a['_text'] = a['p'] in ('uebung', 'sicherung', 'korrektur') and self._alt_sach(a)
            if a['p'] == 'uebung' and a['s'] == 3 and a['_text']:
                a['_huerde'] = next((art for lz, rx, art in self.alt_huerden if lz == a['l'] and rx.search(a['f']['text'])), None)
        for lz, rx, art in self.alt_huerden:
            assert any(a['l'] == lz and a.get('_huerde') and rx.search(a['f']['text']) for a in auf), f'Hürde alt nicht gefunden: {lz} {rx.pattern}'
        vorher = self._zaehle(auf, karten)
        lehrer_vorher = {lz: {s: sum(1 for a in auf if a['l'] == lz and a['p'] == 'uebung' and a.get('g') in TXT and a['s'] == s) for s in (1, 2, 3)} for lz in karten}
        # neue Aufgaben
        texte = {a['f']['text'] for a in auf}
        neu_je = collections.defaultdict(list)
        for lz, pool, g, n, hu in self.neue:
            assert lz in karten, lz
            assert n['f']['text'] not in texte, f'schon vorhanden: {n["f"]["text"]}'
            texte.add(n['f']['text'])
            a = {'l': lz, 't': tf[lz], 'p': pool, 's': STUFE_VON[g] if g else 2, **({'g': g} if g else {}), **json.loads(json.dumps(n))}
            if pool != 'uebung': a.pop('h', None)
            assert len(a['w']) >= 40, a
            a['_text'] = True; a['_neu'] = True; a['_huerde'] = hu
            neu_je[lz].append(a)
        # Stufe 3: je Typ höchstens 3 – alte Rechenaufgabe desselben Typs wird überzählig
        for lz in karten:
            for n in [a for a in neu_je[lz] if a['p'] == 'uebung' and a['s'] == 3]:
                mit = [a for a in auf if a['l'] == lz and a['p'] == 'uebung' and a.get('g') == n['g'] and a['s'] == 3] + \
                      [a for a in neu_je[lz] if a is not n and a.get('g') == n['g'] and a['s'] == 3 and neu_je[lz].index(a) < neu_je[lz].index(n)]
                if len(mit) >= 3:
                    kand = [a for a in mit if not a['_text'] and not a.get('_neu')]
                    assert kand, f'{self.thema}/{lz}: Stufe 3 Typ {n["g"]} schon 3-mal als Textaufgabe – anderen Typ wählen ({n["f"]["text"][:60]})'
                    self._weg(kand[-1], 'Stufe 3 je Typ höchstens 3')
        # einfügen: Übungen nach der letzten alten Übung der Karte, Sicherung/Korrektur ans Ende ihres Pools in der Karte
        for lz in karten:
            for pool in ('uebung', 'sicherung', 'korrektur'):
                neu = [a for a in neu_je[lz] if a['p'] == pool]
                if not neu: continue
                idx = [i for i, a in enumerate(auf) if a['l'] == lz and a['p'] == pool]
                pos = (idx[-1] + 1) if idx else len(auf)
                auf[pos:pos] = neu
        # Anteil des Themas auf mindestens 40 %: alte Rechenaufgaben ohne Sachsituation werden überzählig
        while True:
            ue = [a for a in auf if a['p'] == 'uebung' and 'g' in a]
            anteil = Fr(sum(a['_text'] for a in ue), len(ue))
            if anteil >= Fr(2, 5): break
            kand = []
            for lz in karten:
                k = [a for a in ue if a['l'] == lz]
                for s in (1, 2, 3):
                    ks = [a for a in k if a['s'] == s]
                    typen = collections.Counter(a['g'] for a in ks)
                    if len(ks) <= MIND[s][0]: continue
                    for a in ks:
                        if a['_text'] or a.get('_neu'): continue
                        if typen[a['g']] == 1 and len(typen) <= MIND[s][1]: continue
                        quote = Fr(sum(x['_text'] for x in k), len(k))
                        kand.append((quote, -len(ks) + MIND[s][0], -typen[a['g']], -auf.index(a), a))
            assert kand, f'{self.thema}: Anteil {float(anteil):.0%} – keine alte Rechenaufgabe mehr überzählig machbar, mehr Textaufgaben nötig'
            kand.sort(key=lambda x: x[:4])
            self._weg(kand[0][-1], 'Anteil 40 %')
        # Reihenfolge der Übungen je Lernkarte (nie zwei gleiche Typen hintereinander)
        for lz in karten:
            idx = [i for i, a in enumerate(auf) if a['l'] == lz and a['p'] == 'uebung']
            neu = Stufen.ordne([auf[i] for i in idx])
            for i, a in zip(idx, neu): auf[i] = a
        nachher = self._zaehle(auf, karten)
        self._pruefe(auf, karten, nachher)
        self.bericht_daten = {'vorher': vorher, 'lehrer_vorher': lehrer_vorher, 'nachher': nachher, 'ausnahmen': self.ausnahmen,
                              'ueberzaehlig': self.ueberzaehlig,
                              'neu': {lz: collections.Counter(f"{a['p']}{a['s'] if a['p'] == 'uebung' else ''}" for a in neu_je[lz]) for lz in karten},
                              'huerden': {lz: [a['_huerde'] for a in neu_je[lz] if a.get('_huerde')] for lz in karten},
                              'alt_sach': [(a['l'], a['p'], a.get('g'), a['f']['text']) for a in auf if a['_text'] and not a.get('_neu') and a.get('g') not in TXT],
                              'beispiele': {lz: {s: [a['f']['text'] for a in neu_je[lz] if a['p'] == 'uebung' and a['s'] == s] for s in (1, 2, 3)} for lz in karten}}
        for a in auf:
            for k in ('_text', '_neu', '_huerde'): a.pop(k, None)
        return d

    def _weg(self, a, grund):
        self.ueberzaehlig.append((a['l'], a['s'], a['g'], grund, a['f']['text']))
        del a['g']

    def _zaehle(self, auf, karten):
        z = {}
        for lz in karten:
            ue = [a for a in auf if a['l'] == lz and a['p'] == 'uebung' and 'g' in a]
            z[lz] = {'text': {s: sum(1 for a in ue if a['s'] == s and a['_text']) for s in (1, 2, 3)},
                     'alle': {s: sum(1 for a in ue if a['s'] == s) for s in (1, 2, 3)},
                     'sicherung': sum(1 for a in auf if a['l'] == lz and a['p'] == 'sicherung' and a['_text']),
                     'korrektur': sum(1 for a in auf if a['l'] == lz and a['p'] == 'korrektur' and a['_text'])}
        return z

    def _pruefe(self, auf, karten, z):
        for lz in karten:
            ue = [a for a in auf if a['l'] == lz and a['p'] == 'uebung' and 'g' in a]
            je = {s: collections.Counter(a['g'] for a in ue if a['s'] == s) for s in (1, 2, 3)}
            for s, (n, k) in MIND.items():
                assert sum(je[s].values()) >= n and len(je[s]) >= k, f'{self.thema}/{lz}: Stufe {s} hat {dict(je[s])}'
            assert max(je[3].values()) <= 3, f'{self.thema}/{lz}: Stufe 3 je Typ höchstens 3: {dict(je[3])}'
            alle = [a for a in auf if a['l'] == lz and a['p'] == 'uebung']
            for x, y in zip(alle, alle[1:]):
                assert not ('g' in x and x.get('g') == y.get('g')), f'{self.thema}/{lz}: zwei gleiche Typen hintereinander'
            t = z[lz]['text']
            if lz not in self.ausnahmen:
                assert t[1] >= 1 and t[2] >= 3 and t[3] >= 4 and sum(t.values()) >= 8, f'{self.thema}/{lz}: Textaufgaben je Stufe {t}'
                hu = [a for a in auf if a['l'] == lz and a['p'] == 'uebung' and 'g' in a and a.get('_huerde') and a['s'] == 3]
                assert len(hu) >= 2, f'{self.thema}/{lz}: nur {len(hu)} Stufe-3-Textaufgaben mit Hürde'
                assert z[lz]['sicherung'] >= 2 and z[lz]['korrektur'] >= 1, f'{self.thema}/{lz}: Sicherung/Korrektur {z[lz]}'
        ue = [a for a in auf if a['p'] == 'uebung' and 'g' in a]
        self.anteil = sum(a['_text'] for a in ue) / len(ue)
        assert self.anteil >= 0.4, self.anteil

    def bericht(self):
        return f'{self.thema}: neu {len(self.neue)}, überzählig {len(self.ueberzaehlig)}, Anteil Textaufgaben {self.anteil:.0%}'

    def schreibe_bericht(self):
        self.bericht_daten['anteil'] = self.anteil
        Path('/tmp').joinpath(f'text_{self.thema}.json').write_text(json.dumps(self.bericht_daten, ensure_ascii=False, indent=1))
        print('  TEXT ' + self.bericht())


def mit_text(baue, tx):
    def baue_text(meta, *args, **kwargs):
        d = baue(meta, *args, **kwargs)
        tx.anwenden(d)
        pfad = THEMEN / f"{meta['thema_schluessel']}.json"
        pfad.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        tx.schreibe_bericht()
        return d
    return baue_text


def text_auf_datei(tx, d):
    tx.anwenden(d)
    tx.schreibe_bericht()
    return d
