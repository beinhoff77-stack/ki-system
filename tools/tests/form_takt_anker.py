"""Zählt die Anker der FT-S-Text-Patches (supabase/migrations/20261203_ft_s_form_takt.sql) in den aus den Migrationsdateien
REKONSTRUIERTEN Funktionstexten – ohne Datenbank.

Rekonstruktion: je Funktion die jüngste vollständige `create or replace function` (in Einspiel-Reihenfolge, die von den Dateiköpfen abweicht,
wo nötig: 22.11. WD-S 2, WD-S 3, WD-4b, WD-S 4, FP-S, FP-S 2, FP-S 3), danach alle späteren Text-Patches (replace(d, alt, neu), *_ersetzen(...),
Patch-Plan von BD-S2). Gibt es keine vollständige Fassung im Repo (einheit_lesen_intern), entsteht eine TEIL-Rekonstruktion aus den eingefügten
Stücken. Live kann abweichen – maßgeblich ist die Zählung gegen die Live-Datenbank (Tabelle in inhalte/plan/form-takt-bau.md).

Geprüft je Anker: (1) alt steht so oft da wie erwartet, (2) neu steht nicht da, (3) alt ist nicht im neuen Text enthalten (sonst erkennt der
zweite Lauf „fertig“ nicht), (4) nach dem Einbau: alt 0-mal, neu wie erwartet (= Zustand „fertig“), (5) zweiter Einbau ändert nichts.
Aufruf:  python3 -I tools/tests/form_takt_anker.py            -> Prüfung, Ausgabe OK oder Fehler
         python3 -I tools/tests/form_takt_anker.py --tabelle  -> Markdown-Tabelle aller Anker (für den Bericht)
         python3 -I tools/tests/form_takt_anker.py --zeige schule.karte_landet  -> rekonstruierter Text
         python3 -I tools/tests/form_takt_anker.py --json     -> schreibt inhalte/plan/form-takt-anker.json (Anker-Liste für die Live-Zählung)
"""
import re
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
MIG = WURZEL / 'supabase/migrations'
FT = MIG / '20261203_ft_s_form_takt.sql'
VORRANG = {  # Einspiel-Reihenfolge laut Dateiköpfen, wo sie vom Dateinamen abweicht
    '20261122_wd_s_wiederholungen.sql': '20261122_a1', '20261122_wd_s3_frische_aufgaben.sql': '20261122_a2',
    '20261122_wd_4b_stau_strecken.sql': '20261122_a3', '20261122_wd_s4_nacharbeit_921.sql': '20261122_a4',
    '20261122_fp_s_faire_punkte.sql': '20261122_a5', '20261122_fp_s2_nacharbeit_924.sql': '20261122_a6',
    '20261122_fp_s3_nacharbeit_929.sql': '20261122_a7'}


def dateien(bis=None):
    fs = sorted((p for p in MIG.glob('*.sql')), key=lambda p: VORRANG.get(p.name, p.name))
    return [p for p in fs if (bis is None or p.name < bis) and p.name != FT.name]


def literal(t, i):
    """Liest ein SQL-Literal ab Position i. Gibt (Wert, Ende) zurück oder None."""
    m = re.compile(r'\$(\w*)\$').match(t, i)
    if m:
        tag = m.group(0); j = t.index(tag, m.end())
        return t[m.end():j], j + len(tag)
    if t.startswith(("E'", "e'"), i):
        j, out = i + 2, []
        while True:
            c = t[j]
            if c == '\\':
                n = t[j + 1]; out.append({'n': '\n', 't': '\t', '\\': '\\', "'": "'"}.get(n, n)); j += 2
            elif c == "'":
                if t[j + 1:j + 2] == "'": out.append("'"); j += 2
                else: return ''.join(out), j + 1
            else: out.append(c); j += 1
    if t.startswith("'", i):
        j, out = i + 1, []
        while True:
            c = t[j]
            if c == "'":
                if t[j + 1:j + 2] == "'": out.append("'"); j += 2
                else: return ''.join(out), j + 1
            else: out.append(c); j += 1
    return None


def ausdruck(t, i, var):
    """term (|| term)* ; term = Literal | Variable. Gibt (Wert, Ende) oder None."""
    teile = []
    while True:
        while t[i].isspace(): i += 1
        r = literal(t, i)
        if r is None:
            m = re.compile(r'[a-z_][a-z0-9_]*').match(t, i)
            w = var(m.group(0), i) if m and callable(var) else (var.get(m.group(0)) if m else None)
            if w is None: return None
            r = (w, m.end())
        teile.append(r[0]); i = r[1]
        j = i
        while t[j].isspace(): j += 1
        if t.startswith('||', j): i = j + 2; continue
        return ''.join(teile), i


def klammer_ende(t, i):
    """i zeigt auf '('; Ende der passenden Klammer ('...' beachtet)."""
    tiefe = 0
    while True:
        c = t[i]
        if c == "'":
            i = literal(t, i)[1]; continue
        if c == '(': tiefe += 1
        elif c == ')':
            tiefe -= 1
            if tiefe == 0: return i
        i += 1


def argzahl(params):
    params = params.strip()
    if not params: return 0
    tiefe, n = 0, 1
    for c in params:
        if c == '(': tiefe += 1
        elif c == ')': tiefe -= 1
        elif c == ',' and tiefe == 0: n += 1
    return n


def schluessel(name_sig):
    """'schule.x(bigint, text)' oder 'schule.x' -> (name, argzahl|None)"""
    m = re.match(r'\s*((?:schule|api)\.\w+)\s*(?:\((.*)\))?\s*$', name_sig, re.S)
    return m.group(1), (argzahl(m.group(2)) if m.group(2) is not None else None)


def ereignisse2(p):
    """Zuweisungen an Text-Variablen in Reihenfolge; Rückgabe: Funktion (name, pos) -> letzter Wert davor."""
    t = p.read_text(encoding='utf-8')
    zuw = []
    def nachschlagen(name, pos):
        w = None
        for q, n, v in zuw:
            if q < pos and n == name: w = v
        return w
    for m in re.finditer(r"\b(v_\w+|alt|neu)\s+(?:constant\s+)?text\s*:=\s*|\b(v_\w+)\s*:=\s*", t):
        name = m.group(1) or m.group(2)
        if t[m.end()] in "'$Ee":
            r = ausdruck(t, m.end(), nachschlagen)
            if r: zuw.append((m.start(), name, r[0]))
    return nachschlagen


def rekonstruieren(gesucht, bis=None, protokoll=None):
    """gesucht: {schluessel: (name, argzahl)}. Gibt {schluessel: (text, quelle, vollstaendig, log)}."""
    stand = {}
    for p in dateien(bis):
        t = p.read_text(encoding='utf-8')
        var_all = ereignisse2(p)
        ev = ereignisse_mit_var(p, var_all)
        ziel = None
        for pos, art, k, w in ev:
            if art == 'basis':
                stand[k] = {'text': w, 'quelle': p.name, 'voll': True, 'log': [f'{p.name}: vollständige Fassung']}
            elif art == 'ziel':
                ziel = k
            elif art == 'kopie':
                q, z = k
                stand[z] = dict(stand[q], log=stand[q]['log'] + [f'{p.name}: Kopie von {q[0]}'], quelle=p.name)
                ziel = None
            elif art in ('ersetze', 'ersetze_fn'):
                zk = ziel if art == 'ersetze' else k
                paare = [w] if art == 'ersetze' else w
                if zk is None: continue
                if isinstance(zk, list):
                    for z1 in zk:
                        for s1 in [s for s in stand if s[0] == z1[0]]:
                            for alt, neu in paare: stand[s1]['text'] = stand[s1]['text'].replace(alt, neu); stand[s1]['log'].append(f'{p.name}: ersetzt (Schleife) {alt[:50]!r}')
                    continue
                kand = [s for s in stand if s[0] == zk[0] and (zk[1] is None or s[1] == zk[1])]
                if not kand and zk[1] is not None and (zk[0], None) in stand:
                    stand[zk] = stand.pop((zk[0], None)); kand = [zk]
                if not kand:
                    kand = [(zk[0], zk[1])]
                    stand[kand[0]] = {'text': '', 'quelle': None, 'voll': False, 'log': []}
                for s in kand:
                    for alt, neu in paare:
                        x = stand[s]
                        n = x['text'].count(alt)
                        if n == 0:
                            if x['voll']:
                                x['log'].append(f'{p.name}: Stelle NICHT gefunden: {alt[:60]!r}')
                                continue
                            x['text'] += '\n/* (aus unbekannter Fassung) */ ' + alt
                            x['log'].append(f'{p.name}: Stelle aus unbekanntem Grundtext angenommen: {alt[:50]!r}')
                        x['text'] = x['text'].replace(alt, neu)
                        x['log'].append(f'{p.name}: ersetzt ({n}x) {alt[:50]!r}')
            elif art == 'unlesbar' and ziel is not None and protokoll is not None:
                protokoll.append(f'{p.name}: unlesbarer Patch an {ziel}: {w[:80]!r}')
    return stand


def ereignisse_mit_var(p, var):
    t = p.read_text(encoding='utf-8')
    ev = []
    for m in re.finditer(r'create\s+or\s+replace\s+function\s+((?:schule|api)\.\w+)\s*\(', t, re.I):
        e = klammer_ende(t, m.end() - 1)
        n = argzahl(t[m.end():e])
        a = re.compile(r'\bas\s+(\$\w*\$)', re.I).search(t, e)
        tag = a.group(1); j = t.index(tag, a.end())
        ev.append((m.start(), 'basis', (m.group(1).lower(), n), ' AS $function$' + t[a.end():j] + '$function$\n'))
    for m in re.finditer(r"pg_get_functiondef\('((?:schule|api)\.[^']*)'::regproc(?:edure)?\)", t):
        ev.append((m.start(), 'ziel', schluessel(m.group(1)), None))
    for m in re.finditer(r"pronamespace = '(schule|api)'::regnamespace and p\.proname = '(\w+)'", t):
        ev.append((m.start(), 'ziel', (m.group(1) + '.' + m.group(2), None), None))
    if p.name.startswith('20261116_w150_r3_'):   # Schleife über drei Funktionen (pg_get_functiondef(r.oid))
        ev.append((t.index('pg_get_functiondef(r.oid)'), 'ziel', [('api.schule_lernstand', None), ('api.schule_wiederholung', None), ('schule.etappen_stand', None)], None))
    if p.name.startswith('20261120_i2_'):        # schule.mischkarten wird als mischkarten_waehlen behalten
        ev.append((t.index("d := replace(d, 'FUNCTION schule.mischkarten('"), 'kopie', (('schule.mischkarten', 3), ('schule.mischkarten_waehlen', 3)), None))
    for m in re.finditer(r"(?<![a-z_])replace\(\s*(d|v_def|d0)\s*,", t):
        if t[:m.start()].rstrip().endswith('length('): continue   # Zählausdruck, kein Ersetzen
        r1 = ausdruck(t, m.end(), var)
        ok = False
        if r1:
            i = r1[1]
            while t[i].isspace(): i += 1
            if t[i] == ',':
                r2 = ausdruck(t, i + 1, var)
                if r2: ev.append((m.start(), 'ersetze', None, (r1[0], r2[0]))); ok = True
        if not ok: ev.append((m.start(), 'unlesbar', None, t[m.start():m.start() + 120]))
    for m in re.finditer(r"pg_temp\.\w+_ersetzen\('([^']+)',\s*'[^']*',\s*array\[", t):
        ziel, i, alt, neu = schluessel(m.group(1)), m.end(), [], []
        for liste in (alt, neu):
            while True:
                r = ausdruck(t, i, var); liste.append(r[0]); i = r[1]
                while t[i].isspace(): i += 1
                if t[i] == ',': i += 1; continue
                i += 1; break
            if liste is alt: i = t.index('array[', i) + 6
        ev.append((m.start(), 'ersetze_fn', ziel, list(zip(alt, neu))))
    if p.name.startswith('20261202_bd_s2'):
        for m in re.finditer(r"jsonb_build_object\('f', '([^']+)', 'p', jsonb_build_array\(", t):
            ziel, i, paare = schluessel(m.group(1)), m.end(), []
            while True:
                while t[i].isspace(): i += 1
                if not t.startswith('jsonb_build_array(', i): break
                i += len('jsonb_build_array(')
                r1 = ausdruck(t, i, var); i = r1[1] + 1
                r2 = ausdruck(t, i, var); i = r2[1]
                i = t.index(')', i) + 1
                paare.append((r1[0], r2[0]))
                while t[i].isspace(): i += 1
                if t[i] == ',': i += 1
            ev.append((m.start(), 'ersetze_fn', ziel, paare))
    ev.sort(key=lambda x: x[0])
    return ev




def plan_lesen():
    """Patch-Plan aus der FT-S-Migration: [(signatur, [(alt, neu, soll), ...]), ...]"""
    t = FT.read_text(encoding='utf-8')
    plan = []
    for m in re.finditer(r"jsonb_build_object\('f', '([^']+)', 'p', jsonb_build_array\(", t):
        i, paare = m.end(), []
        while True:
            while t[i].isspace(): i += 1
            if not t.startswith('jsonb_build_array(', i): break
            i += len('jsonb_build_array(')
            r1 = ausdruck(t, i, {}); i = r1[1]
            while t[i] in ', \n': i += 1
            r2 = ausdruck(t, i, {}); i = r2[1]
            n = re.compile(r'\s*,\s*(\d+)\)').match(t, i); i = n.end()
            paare.append((r1[0], r2[0], int(n.group(1))))
            while t[i].isspace(): i += 1
            if t[i] == ',': i += 1
        plan.append((m.group(1), paare))
    return plan


def finde(stand, sig):
    name, n = schluessel(sig)
    if n is not None and (name, n) in stand: return stand[(name, n)]
    k = [x for x in stand if x[0] == name and (n is None or x[1] == n or x[1] is None)]
    voll = [x for x in k if stand[x]['voll']]
    if len(voll) == 1: return stand[voll[0]]
    return stand[k[0]] if len(k) == 1 else None


def main():
    import sys
    stand = rekonstruieren(None)
    plan = plan_lesen()
    if '--json' in sys.argv:
        import json
        d = [{'f': s, 'alt': a, 'neu': n, 'soll': k} for s, p in plan for a, n, k in p]
        (WURZEL / 'inhalte/plan/form-takt-anker.json').write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding='utf-8'); print(len(d), 'Anker geschrieben'); return
    if '--zeige' in sys.argv:
        x = finde(stand, sys.argv[sys.argv.index('--zeige') + 1]); print('\n'.join(x['log'])); print(x['text']); return
    fehler, zeilen, n_anker = [], [], 0
    for sig, paare in plan:
        x = finde(stand, sig)
        if x is None: fehler.append(f'{sig}: keine Rekonstruktion'); continue
        d = x['text']
        for alt, neu, soll in paare:
            n_anker += 1
            if d.count(alt) != soll: fehler.append(f'{sig}: alt {d.count(alt)}x statt {soll}x: {alt[:50]!r}')
            if d.count(neu) != 0: fehler.append(f'{sig}: neu steht schon da: {neu[:50]!r}')
            if alt in neu: fehler.append(f'{sig}: alt ist im neuen Text enthalten: {alt[:50]!r}')
            zeilen.append((sig, alt, soll, 'voll' if x['voll'] else 'TEIL', x['quelle'] or '–'))
        d2 = d
        for alt, neu, soll in paare: d2 = d2.replace(alt, neu)
        for alt, neu, soll in paare:
            if d2.count(alt) != 0 or d2.count(neu) != soll: fehler.append(f'{sig}: nach dem Einbau nicht „fertig“: {alt[:50]!r}')
        d3 = d2
        for alt, neu, soll in paare:
            if d3.count(alt) == soll and d3.count(neu) == 0: d3 = d3.replace(alt, neu)
        if d3 != d2: fehler.append(f'{sig}: zweiter Einbau ändert den Text')
    if '--tabelle' in sys.argv:
        print('| Nr | Funktion (Signatur) | alter Text (wörtlich) | erwartet | Rekonstruktion |')
        print('|---|---|---|---|---|')
        for i, (sig, alt, soll, art, q) in enumerate(zeilen, 1):
            a = alt.replace('|', '\\|').replace('\n', '⏎')
            print(f'| {i} | `{sig}` | `{a}` | {soll} | {art} ({q}) |')
        return
    if fehler:
        print('\n'.join(fehler)); sys.exit(1)
    teil = sorted({sig for sig, *_ , art, q in zeilen if art == 'TEIL'})
    print(f'OK – {len(plan)} Funktionen, {n_anker} Anker; Teil-Rekonstruktion (Grundtext nicht im Repo): {", ".join(teil) or "keine"}')


if __name__ == '__main__':
    main()
