#!/usr/bin/env python3
"""Prüfskript für Themen-Dateien (Werkstatt #150, Lernen Schule).

Aufruf:  python3 -I tools/inhalt_pruefen.py inhalte/themen/<datei>.json [...]
         python3 -I tools/inhalt_pruefen.py --alle

Prüft Aufbau, Mindestmengen je Lernkarte, Antworttypen, Dubletten und rechnet jede
Aufgabe mit Feld "c" (Rechenausdruck) exakt nach. Exit-Code 0 = alles gut, 1 = Fehler.
Format und Regeln: inhalte/README.md
"""
import ast
import json
import operator
import re
import sys
from fractions import Fraction
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
POOLS = ('uebung', 'test', 'korrektur', 'sicherung', 'bonus')
TYPEN = ('zahl', 'auswahl', 'text', 'luecken', 'markierung')
MIN = {'uebung': 12, 'test': 1, 'korrektur': 3, 'sicherung': 6, 'bonus': 0}
MAX_BONUS = 3               # Knobel-Bordkarten je Lernkarte (freiwillig, zählen weder für „sitzt“ noch für den Test)
# Bau-Auftrag F: Aufgabentyp „g“ (der Gedanke einer Bordkarte). Die Stufe folgt aus dem Typ, nicht aus der Größe der Zahlen.
GEDANKEN = {
    1: ('direkt', 'erkennen'),
    2: ('mehrschritt', 'einkleidung', 'umkehr', 'darstellung'),
    3: ('rueckwaerts', 'verknuepfen', 'begruenden', 'fehler', 'transfer', 'parameter', 'pruefung'),
}
BONUS_TYP = 'knobel'
STUFE_VON = {g: st for st, gs in GEDANKEN.items() for g in gs}
MIN_TYPEN = {1: 2, 2: 3, 3: 4}  # verschiedene Typen je Stufe, wenn alle Übungen einer Lernkarte „g“ haben
MAX_GLEICH_GEBAUT = 2          # höchstens so viele Aufgaben desselben Typs je Stufe mit gleichem Satzbau
ZAHL = re.compile(r'[−-]?\d+(?:[ \u202f]\d{3})*(?:[,.]\d+)?')


def bauplan(a):
    """Fragetext ohne Zahlen – zwei Aufgaben mit gleichem Bauplan sind „gleich gebaut“."""
    return re.sub(r'\s+', ' ', ZAHL.sub('#', str((a.get('f') or {}).get('text', '')))).strip()
MIN_JE_STUFE = 3            # Übungen: mindestens 3 je Stufe 1, 2, 3
SLUG = re.compile(r'^[a-z][a-z0-9_]{1,30}$')
BILDER = ('zahlenstrahl', 'stellentafel', 'koordinaten', 'figur', 'saeulen', 'kreisdiagramm', 'tabelle', 'boxplot', 'baum', 'thermometer', 'bruchstreifen')

# ---------- exakter Rechner für das Feld "c" ----------
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
       ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod}
FUNK = {'abs': abs, 'min': min, 'max': max, 'round': lambda x, n=0: round(float(x), int(n))}


def rechne(ausdruck):
    def ev(n):
        if isinstance(n, ast.Expression): return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return Fraction(str(n.value)) if isinstance(n.value, float) else Fraction(n.value)
        if isinstance(n, ast.BinOp) and type(n.op) in OPS: return OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow):
            b, e = ev(n.left), ev(n.right)
            if e.denominator != 1: raise ValueError('nur ganzzahlige Exponenten')
            return b ** int(e)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.USub, ast.UAdd)):
            return -ev(n.operand) if isinstance(n.op, ast.USub) else ev(n.operand)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in FUNK and not n.keywords:
            r = FUNK[n.func.id](*[ev(a) for a in n.args])
            return Fraction(str(r)) if isinstance(r, float) else r
        raise ValueError(f'nicht erlaubt: {ast.dump(n)[:60]}')
    return ev(ast.parse(str(ausdruck), mode='eval'))


def zahlwert(v):
    if isinstance(v, bool) or not isinstance(v, (int, float)): raise ValueError('keine Zahl')
    return Fraction(str(v)) if isinstance(v, float) else Fraction(v)


# ---------- Prüfung ----------
def pruefe(pfad):
    fehler, warn = [], []
    F = lambda m: fehler.append(m)
    W = lambda m: warn.append(m)
    try:
        d = json.loads(Path(pfad).read_text(encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        return [f'JSON nicht lesbar: {e}'], [], {}

    for k in ('thema_schluessel', 'thema_id', 'block_id', 'klasse', 'autor', 'inhalt', 'aufgaben'):
        if k not in d: F(f'Feld "{k}" fehlt')
    if fehler: return fehler, warn, {}
    inh, auf = d['inhalt'], d['aufgaben']
    if not isinstance(d['klasse'], dict) or not d['klasse']: F('"klasse" muss z. B. {"gym_by": 8} sein')

    # Inhalt
    for k in ('ziel', 'merke', 'abschnitte', 'etappen', 'teilfaehigkeiten', 'bewertung'):
        if k not in inh: F(f'inhalt.{k} fehlt')
    if fehler: return fehler, warn, {}
    et = inh['etappen']
    lz = [e.get('lernziel') for e in et]
    if len(et) < 3: F('mindestens 3 Lernkarten (etappen)')
    if len(set(lz)) != len(lz): F('Lernziele (etappen[].lernziel) doppelt')
    for e in et:
        n = e.get('lernziel')
        if not n or not SLUG.match(n): F(f'Lernziel "{n}": nur a–z, 0–9, _ (2–31 Zeichen)')
        for k in ('titel', 'regel', 'schritte', 'fehler'):
            if not e.get(k): F(f'Karte {n}: "{k}" fehlt oder leer')
        if e.get('einstieg') is not None and (not isinstance(e['einstieg'], str) or len(e['einstieg']) < 60):
            F(f'Karte {n}: "einstieg" muss ein Text mit einer Alltagssituation sein (mindestens 60 Zeichen)')
        if e.get('woerter') is not None and not (isinstance(e['woerter'], list) and all(isinstance(w, list) and len(w) == 2 and all(isinstance(x, str) and x for x in w) for w in e['woerter'])):
            F(f'Karte {n}: "woerter" muss eine Liste aus [Wort, Erklärung] sein')
        if e.get('schritte') is not None and (not isinstance(e['schritte'], list) or len(e['schritte']) < 2):
            F(f'Karte {n}: "schritte" braucht mindestens 2 Schritte (vorgerechnetes Beispiel)')
        # Vorgabe 16.11. (inhalte/README.md „Verständliche Erklärungen“): Schritte als Text oder {text, bild}; falsches Format = Fehler, zu lang = Warnung.
        sch = e.get('schritte') if isinstance(e.get('schritte'), list) else []
        neu = any(isinstance(x, dict) for x in sch)
        for i, x in enumerate(sch):
            if isinstance(x, dict):
                if not isinstance(x.get('text'), str) or not x['text'].strip(): F(f'Karte {n}: Schritt {i + 1} braucht "text"')
                if set(x) - {'text', 'bild'}: F(f'Karte {n}: Schritt {i + 1} hat unbekannte Felder {sorted(set(x) - {"text", "bild"})}')
                if x.get('bild') is not None:
                    if not isinstance(x['bild'], dict): F(f'Karte {n}: Schritt {i + 1}: "bild" muss ein Objekt sein')
                    elif x['bild'].get('typ') is not None and x['bild']['typ'] not in BILDER: F(f'Karte {n}: Schritt {i + 1}: bild.typ "{x["bild"]["typ"]}" gibt es nicht')
                    elif x['bild'].get('typ') is None and not e.get('bild'): F(f'Karte {n}: Schritt {i + 1} ergänzt ein Kartenbild, aber die Karte hat kein "bild"')
            elif not isinstance(x, str) or not x.strip(): F(f'Karte {n}: Schritt {i + 1} muss Text oder {{text, bild}} sein')
        fb = e.get('fehler_bild')
        if fb is not None:
            if not isinstance(fb, dict): F(f'Karte {n}: "fehler_bild" muss ein Objekt sein')
            elif fb.get('typ') is not None and fb['typ'] not in BILDER: F(f'Karte {n}: fehler_bild.typ "{fb["typ"]}" gibt es nicht')
            elif fb.get('typ') is None and not e.get('bild'): F(f'Karte {n}: fehler_bild ergänzt ein Kartenbild, aber die Karte hat kein "bild"')
        if neu:
            wz = lambda t: len(re.findall(r'\S+', re.sub(r'[⟦⟧]', '', str(t or ''))))
            saetze = lambda t: [x for x in re.split(r'(?<=[.!?])\s+', re.sub(r'[⟦⟧]', '', str(t or ''))) if x.strip()]
            kl = min([v for v in (d.get('klasse') or {}).values() if isinstance(v, (int, float))] or [5]); smax = 15 if kl <= 6 else 20
            if not e.get('einstieg'): W(f'Karte {n}: "einstieg" fehlt')
            elif wz(e['einstieg']) > 35: W(f'Karte {n}: einstieg hat {wz(e["einstieg"])} Wörter (höchstens 35)')
            if not e.get('bild'): W(f'Karte {n}: Kartenbild fehlt (oder unter "offen" begründen)')
            if len(e.get('woerter') or []) > 3: W(f'Karte {n}: {len(e["woerter"])} neue Wörter (höchstens 3)')
            texte = ' '.join([str(e.get('einstieg') or '')] + [x['text'] if isinstance(x, dict) else str(x) for x in sch]).lower()
            for w in e.get('woerter') or []:
                kern = str(w[0]).split(' (')[0].strip().lower()
                if kern and kern not in texte: W(f'Karte {n}: Wort "{w[0]}" kommt in einstieg und schritten nicht vor')
            if len(sch) > 5: W(f'Karte {n}: {len(sch)} Schritte (höchstens 5)')
            for i, x in enumerate(sch):
                t = x['text'] if isinstance(x, dict) else x
                if wz(t) > 15: W(f'Karte {n}: Schritt {i + 1} hat {wz(t)} Wörter (höchstens 15)')
            if wz(e.get('fehler')) > 30: W(f'Karte {n}: fehler hat {wz(e.get("fehler"))} Wörter (höchstens 30)')
            if wz(e.get('regel')) > 25: W(f'Karte {n}: regel hat {wz(e.get("regel"))} Wörter (höchstens 25)')
            rs = saetze(e.get('regel'))
            if rs and wz(rs[0]) > 12: W(f'Karte {n}: erster Satz der regel hat {wz(rs[0])} Wörter (als „Kurz gesagt“ höchstens 12)')
            for k in ('einstieg', 'fehler', 'regel'):
                for sa in saetze(e.get(k)):
                    if wz(sa) > smax: W(f'Karte {n}: Satz in "{k}" hat {wz(sa)} Wörter (höchstens {smax}): {sa[:50]}…')
                if str(e.get(k) or '').count('⟦') > 2: W(f'Karte {n}: mehr als 2 Markierungen ⟦…⟧ in "{k}"')
            if re.search('[¼½¾⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞]', json.dumps(e, ensure_ascii=False)): W(f'Karte {n}: Unicode-Bruchzeichen – bitte a/b schreiben')
        if len(e.get('titel', '')) > 40: W(f'Karte {n}: Titel über 40 Zeichen')
        for k in ('regel', 'fehler', 'probe'):
            if str(e.get(k, '')).count('⟦') != str(e.get(k, '')).count('⟧'): F(f'Karte {n}: ⟦ ⟧ in "{k}" nicht paarig')
        b = e.get('bild')
        if b is not None and b.get('typ') not in BILDER: F(f'Karte {n}: bild.typ "{b.get("typ")}" gibt es nicht (nur {", ".join(BILDER)})')
    abs_lz = [x for a in inh['abschnitte'] for x in a.get('lernziele', [])]
    if sorted(abs_lz) != sorted(lz): F('abschnitte[].lernziele müssen jedes Lernziel genau einmal enthalten')
    bw = inh['bewertung']
    pfl, vt = bw.get('lernziele_pflicht', []), bw.get('lernziele_vertiefung', [])
    if sorted(pfl + vt) != sorted(lz): F('bewertung.lernziele_pflicht + lernziele_vertiefung = alle Lernziele, jedes einmal')
    tf_k = {t.get('k') for t in inh['teilfaehigkeiten']}
    tf_lz = [x for t in inh['teilfaehigkeiten'] for x in t.get('lernziele', [])]
    if sorted(tf_lz) != sorted(lz): F('teilfaehigkeiten[].lernziele müssen jedes Lernziel genau einmal enthalten')

    # Aufgaben
    zaehl = {(l, p): 0 for l in lz for p in POOLS}
    stufen = {(l, s): 0 for l in lz for s in (1, 2, 3)}
    gesehen = set()
    beispiele = {re.sub(r'\s+', ' ', s['text'] if isinstance(s, dict) else s) for e in et for s in e.get('schritte', []) if isinstance(s, (str, dict)) and (not isinstance(s, dict) or isinstance(s.get('text'), str))}
    for i, a in enumerate(auf):
        wo = f'Aufgabe {i + 1} ({a.get("l")}/{a.get("p")})'
        for k in ('l', 't', 'p', 's', 'y', 'f', 'o', 'w'):
            if k not in a: F(f'{wo}: Feld "{k}" fehlt')
        if any(k not in a for k in ('l', 'p', 'y', 'f', 'o')): continue
        if a['l'] not in lz: F(f'{wo}: Lernziel "{a["l"]}" hat keine Karte'); continue
        if a['t'] not in tf_k: F(f'{wo}: Teilfähigkeit "{a["t"]}" nicht in inhalt.teilfaehigkeiten')
        if a['p'] not in POOLS: F(f'{wo}: p muss {POOLS} sein'); continue
        if a['y'] not in TYPEN: F(f'{wo}: y muss {TYPEN} sein'); continue
        if a.get('s') not in (1, 2, 3): F(f'{wo}: s (Stufe) muss 1, 2 oder 3 sein')
        g = a.get('g')
        if g is not None:
            if g != BONUS_TYP and g not in STUFE_VON: F(f'{wo}: unbekannter Aufgabentyp g „{g}“ (Liste: inhalte/README.md „Stufen und Aufgabentypen“)')
            elif g == BONUS_TYP and a['p'] != 'bonus': F(f'{wo}: Typ „knobel“ nur im Pool „bonus“')
            elif g != BONUS_TYP and a.get('s') in (1, 2, 3) and STUFE_VON[g] != a['s']: F(f'{wo}: Typ „{g}“ gehört zu Stufe {STUFE_VON[g]}, nicht zu Stufe {a["s"]}')
        if a['p'] == 'bonus':
            if g != BONUS_TYP: F(f'{wo}: Bonus-Bordkarten brauchen g „knobel“')
            if a.get('s') != 3: F(f'{wo}: Bonus-Bordkarten haben Stufe 3')
            if not a.get('h'): F(f'{wo}: Bonus-Bordkarten brauchen einen Tipp "h" (verrät die Idee nicht)')
        zaehl[(a['l'], a['p'])] += 1
        if a['p'] == 'uebung' and a.get('s') in (1, 2, 3): stufen[(a['l'], a['s'])] += 1
        if a['p'] == 'uebung' and not a.get('h'): F(f'{wo}: Übungen brauchen einen Tipp "h"')
        if a['p'] not in ('uebung', 'bonus') and a.get('h'): F(f'{wo}: Test/Korrektur/Sicherung ohne Tipp "h"')
        if len(str(a.get('w', ''))) < 15: F(f'{wo}: Lösungsweg "w" zu kurz')
        f, o, y = a['f'], a['o'], a['y']
        text = str(f.get('text', '')).strip()
        if not text: F(f'{wo}: f.text fehlt')
        schl = text + '|' + json.dumps(a.get('a'), ensure_ascii=False) + '|' + json.dumps(f.get('schablone'), ensure_ascii=False) + '|' + json.dumps(f.get('grafik'), sort_keys=True)
        if schl in gesehen: F(f'{wo}: doppelt: „{text[:60]}“')
        gesehen.add(schl)
        if text in beispiele: F(f'{wo}: gleich wie ein Beispiel aus der Erklärung')
        if re.search(r'(?<![\d,.])\d{5,}', text):
            W(f'{wo}: große Zahl ohne Leerzeichen-Gliederung („20 000“ statt „20000“)')
        if y == 'zahl':
            if 'wert' not in o: F(f'{wo}: o.wert fehlt'); continue
            try: zahlwert(o['wert'])
            except ValueError: F(f'{wo}: o.wert muss eine Zahl sein'); continue
            if 'c' not in a: W(f'{wo}: kein Rechenausdruck "c" – Lösung nicht nachgerechnet')
        elif y == 'auswahl':
            opts = a.get('a')
            if not isinstance(opts, list) or not 3 <= len(opts) <= 4: F(f'{wo}: a = 3–4 Antworten'); continue
            if len(set(map(str, opts))) != len(opts): F(f'{wo}: Antworten doppelt')
            if not isinstance(o.get('index'), int) or not 0 <= o['index'] < len(opts): F(f'{wo}: o.index ungültig')
        elif y == 'text':
            if not str(o.get('text', '')).strip(): F(f'{wo}: o.text fehlt')
            if len(str(o.get('text', ''))) > 20: W(f'{wo}: Textantwort lang – Tippfehler-Risiko, lieber auswahl')
        elif y == 'luecken':
            s = f.get('schablone', '')
            if not s or 'werte' not in o: F(f'{wo}: f.schablone und o.werte nötig'); continue
            if s.count('□') != len(o['werte']): F(f'{wo}: Anzahl □ ({s.count("□")}) ≠ Anzahl werte ({len(o["werte"])})')
            if not f.get('hinweis'): W(f'{wo}: f.hinweis fehlt (wie eintragen?)')
        elif y == 'markierung':
            g = f.get('grafik') or {}
            if g.get('typ') != 'zahlenstrahl': F(f'{wo}: markierung nur mit f.grafik.typ "zahlenstrahl"'); continue
            try:
                st, en, n = zahlwert(g['start']), zahlwert(g['ende']), int(g['abschnitte'])
                idx = o['index']
                if not 0 <= idx <= n: F(f'{wo}: o.index außerhalb 0–{n}')
                if 'zahl' in a:
                    soll = st + (en - st) * idx / n
                    if soll != zahlwert(a['zahl']): F(f'{wo}: Markierung {idx} liegt bei {soll}, nicht bei {a["zahl"]}')
            except (KeyError, ValueError, TypeError): F(f'{wo}: grafik braucht start, ende, abschnitte; o.index')
        g = f.get('grafik')
        if g is not None and y != 'markierung' and g.get('typ') not in BILDER: F(f'{wo}: f.grafik.typ "{g.get("typ")}" gibt es nicht')
        if 'c' in a:
            try:
                if y == 'luecken':
                    ist_l = [rechne(c) for c in a['c']] if isinstance(a['c'], list) else None
                    if ist_l is None or [zahlwert(v) for v in o['werte']] != ist_l:
                        F(f'{wo}: c (Liste) ergibt {[float(x) for x in ist_l or []]}, Lösung ist {o["werte"]}')
                else:
                    ist = rechne(a['c'])
                    soll = None
                    if y == 'zahl': soll = zahlwert(o['wert'])
                    elif y == 'markierung': soll = zahlwert(a.get('zahl', 0)) if 'zahl' in a else None
                    if soll is not None and ist != soll:
                        F(f'{wo}: Nachrechnung „{a["c"]}“ = {float(ist):g}, Lösung ist {float(soll):g}')
            except Exception as e:  # noqa: BLE001
                F(f'{wo}: c nicht rechenbar: {e}')
    for (l, p), n in zaehl.items():
        if n < MIN[p]: F(f'Lernkarte {l}: {n} × {p}, mindestens {MIN[p]}')
    for (l, s), n in stufen.items():
        if n < MIN_JE_STUFE: F(f'Lernkarte {l}: {n} Übungen auf Stufe {s}, mindestens {MIN_JE_STUFE}')
    # Bau-Auftrag F: Stufen und Aufgabentypen
    gleich_gruppen = 0
    for l in lz:
        if zaehl[(l, 'bonus')] > MAX_BONUS: F(f'Lernkarte {l}: {zaehl[(l, "bonus")]} Bonus-Bordkarten, höchstens {MAX_BONUS}')
        ue = [a for a in auf if isinstance(a, dict) and a.get('l') == l and a.get('p') == 'uebung']
        mit_g = [a for a in ue if a.get('g') is not None]
        je = {s: (sum(1 for a in ue if a.get('s') == s and a.get('g') is not None), sum(1 for a in ue if a.get('s') == s and a.get('g') is None)) for s in (1, 2, 3)}
        W(f'Lernkarte {l}: Übungen je Stufe mit g / ohne g: ' + ' · '.join(f'S{s} {m}/{o}' for s, (m, o) in je.items()))
        if ue and len(mit_g) == len(ue):
            for s in (1, 2, 3):
                typen = {a['g'] for a in ue if a.get('s') == s}
                if len(typen) < MIN_TYPEN[s]: F(f'Lernkarte {l}: Stufe {s} hat {len(typen)} verschiedene Typen ({", ".join(sorted(typen)) or "keine"}), mindestens {MIN_TYPEN[s]}')
                bau = {}
                for a in ue:
                    if a.get('s') == s: bau.setdefault((a['g'], bauplan(a)), []).append(a)
                for (g, b), xs in bau.items():
                    if len(xs) > MAX_GLEICH_GEBAUT: F(f'Lernkarte {l}: Stufe {s}, Typ „{g}“: {len(xs)} Aufgaben mit gleichem Satzbau („{b[:50]}“), höchstens {MAX_GLEICH_GEBAUT}')
        # „gleich gebaut hintereinander“: 3 oder mehr Übungen dieser Lernkarte in Folge mit gleichem Bauplan
        lauf, vor = 0, None
        for a in ue + [None]:
            b = bauplan(a) if a is not None else None
            if b is not None and b == vor: lauf += 1
            else:
                if lauf >= 3: gleich_gruppen += 1; W(f'Lernkarte {l}: {lauf} gleich gebaute Übungen hintereinander („{vor[:50]}“)')
                lauf, vor = 1, b
    info = {'lernkarten': len(lz), 'aufgaben': len(auf), **{p: sum(n for (l, q), n in zaehl.items() if q == p) for p in POOLS},
            'nachgerechnet': sum(1 for a in auf if 'c' in a), 'mit_typ': sum(1 for a in auf if isinstance(a, dict) and a.get('g') is not None),
            'gleich_gebaut_hintereinander': gleich_gruppen}
    return fehler, warn, info


def main(argv):
    pfade = sorted((WURZEL / 'inhalte' / 'themen').glob('*.json')) if argv[1:] == ['--alle'] else [Path(p) for p in argv[1:]]
    if not pfade: print(__doc__); return 1
    gesamt = 0
    for p in pfade:
        f, w, info = pruefe(p)
        print(f'\n== {p.name}: {"OK" if not f else f"{len(f)} FEHLER"}  {json.dumps(info, ensure_ascii=False)}')
        for m in f[:60]: print('  FEHLER  ' + m)
        if len(f) > 60: print(f'  … und {len(f) - 60} weitere')
        for m in w[:15]: print('  Hinweis ' + m)
        if len(w) > 15: print(f'  … und {len(w) - 15} weitere Hinweise')
        gesamt += len(f)
        if info: print(f'  Gruppen „gleich gebaut hintereinander“: {info.get("gleich_gebaut_hintereinander", 0)}')
    return 1 if gesamt else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
