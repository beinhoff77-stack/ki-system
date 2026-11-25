import json, sys, re, glob, collections
sys.path.insert(0, '/tmp/lpw')
import lk_map as M, rs_daten as D
FULL = json.load(open('/tmp/lpw/lk_full.json'))
LK = json.load(open('/tmp/lpw/lk_db.json'))
ET = {}; TT = {}; TS = {}
for f in glob.glob('/tmp/lp/inhalte/themen/*.json'):
    d = json.load(open(f)); t = d['thema_id']
    ET[t] = [e['lernziel'] for e in d['inhalt'].get('etappen', [])]
    TS[t] = d['thema_schluessel']
TL = {x['thema_id']: x for x in json.load(open('/tmp/lp/inhalte/themenliste.json'))}
for t in TL: TT[t] = TL[t]['titel']
STILL = {12, 27, 40, 41, 48, 72, 77, 78, 82, 83}
Q = {q['id']: q for q in FULL['q']}
E = {e['id']: e for e in FULL['e']}
ZDB = collections.defaultdict(dict)
for z in FULL['z']: ZDB[z['e']][z['t']] = z['b']

def parse(txt):
    out = {}
    for line in txt.strip().splitlines():
        note = ''
        if '#' in line: line, note = line.split('#', 1)
        parts = line.split()
        eid = int(parts[0]); h = parts[1]; et = parts[2]
        plus = [int(p[1:]) for p in parts[3:] if p.startswith('+')]
        minus = [int(p[1:]) for p in parts[3:] if p.startswith('-')]
        out[eid] = dict(haupt=None if h == '-' else int(h), etappen=[] if et == '-' else et.split(','), plus=plus, minus=minus, notiz=note.strip())
    return out
MAP = {'rs': parse(M.RS), 'gym': parse(M.GYM), 'ib': parse(M.IB)}
# Prüfen: Etappen existieren
fehler = []
for s, m in MAP.items():
    for eid, x in m.items():
        if eid not in E: fehler.append(('eintrag fehlt', s, eid)); continue
        for et in x['etappen']:
            if et not in ET.get(x['haupt'], []): fehler.append(('etappe', s, eid, x['haupt'], et))
        if x['haupt'] in STILL: fehler.append(('still haupt', eid))
# RS: Hauptthema muss dem LP-RS-Vorschlag entsprechen (außer bewusste Nachträge)
RSN = {}
for q, txt in D.P.items():
    if q in (3, 4): continue
    for line in txt.strip().splitlines():
        pfad, eid, alt, neu, bef, note = line.split('|')
        RSN[int(eid)] = {int(x[:-1]): ('haupt' if x[-1] == 'h' else 'neben') for x in neu.split(',')} if neu not in ('-', '') else {}
for eid, x in MAP['rs'].items():
    h = [t for t, b in RSN.get(eid, {}).items() if b == 'haupt']
    if (h[0] if h else None) != x['haupt'] and eid not in (297, 298, 944, 871, 909, 937, 734, 749, 781, 1007): fehler.append(('rs haupt weicht', eid, h, x['haupt']))
# Vollständigkeit: alle Kompetenzpunkte der Basisquellen
for s, qs in (('rs', (7, 8, 24, 25, 12, 26, 13, 14, 15, 16)), ('gym', (1, 2, 3, 4, 5, 6)), ('ib', (18, 19, 20, 21, 22, 23))):
    for e in FULL['e']:
        if e['q'] in qs and e['art'] in ('kompetenz', 'thema') and not e['arch'] and e['id'] not in MAP[s]:
            fehler.append(('punkt ohne zeile', s, e['id']))
print('Fehler:', len(fehler)); [print(f) for f in fehler[:60]]

# ---------- Vorher/Nachher je Punkt
# RS: Vorherstand = nach LP-RS-Korrektur (rs_korrektur_2211.sql, Gruppe I) bzw. DB für II/III
RS_SQL_Q = {7, 8, 24, 12, 13, 15}
def vorher(s, eid):
    if s == 'rs' and E[eid]['q'] in RS_SQL_Q: return dict(RSN.get(eid, {}))
    return dict(ZDB.get(eid, {}))
PUNKTE = []
for s, m in MAP.items():
    for eid, x in m.items():
        alt = vorher(s, eid)
        neu = {}
        for t, b in alt.items():
            if t in x['minus'] or t in STILL: continue
            neu[t] = 'neben'
        if x['haupt']: neu[x['haupt']] = 'haupt'
        for t in x['plus']: neu.setdefault(t, 'neben')
        veraltet = [t for t in alt if t not in neu]
        e = E[eid]; q = Q[e['q']]
        PUNKTE.append(dict(schulart=s, quelle=e['q'], klasse=q['j'], zweig=q['zw'], eintrag_id=eid, pfad=e['pfad'],
                           haupt=x['haupt'], etappen=x['etappen'], alt=alt, neu=neu, veraltet=veraltet, notiz=x['notiz']))
print('Punkte', collections.Counter(p['schulart'] for p in PUNKTE))

# ---------- Spuren (Schulart × Gruppe) und Rolle je Punkt
def ib_klasse(p):
    pf = p['pfad']
    for pre, k in (('O45S', 4), ('O45E', 4), ('P1:', 1), ('P2:', 2), ('P3:', 3)):
        if pf.startswith(pre): return k
    return p['klasse']
for p in PUNKTE:
    if p['schulart'] == 'ib': p['klasse'] = ib_klasse(p)
def spuren(p):
    s, zw, pf = p['schulart'], p['zweig'], p['pfad']
    if s == 'gym': return ['gym_by']
    if s == 'rs': return ['rs_I', 'rs_II_III'] if zw == 'allgemein' else [zw]
    if zw == 'myp_beide' and not (pf.startswith('O45') ): return ['ib_standard', 'ib_extended']
    if zw == 'myp_standard' or pf.startswith('O45S'): return ['ib_standard']
    return ['ib_extended']
SP = collections.defaultdict(list)
for p in PUNKTE:
    p['spuren'] = spuren(p)
    for sp in p['spuren']: SP[sp].append(p)
# erste Klasse je (Spur, Thema, Etappe) und je (Spur, Thema)
ERST = {}
for sp, ps in SP.items():
    for p in ps:
        t = p['haupt']
        if not t: continue
        for et in (p['etappen'] or ['*']):
            k = (sp, t, et); ERST[k] = min(ERST.get(k, 99), p['klasse'])
        k = (sp, t, None); ERST[k] = min(ERST.get(k, 99), p['klasse'])
for p in PUNKTE:
    t = p['haupt']
    if not t: p['rolle'] = None; p['etappen_neu'] = []; continue
    sp = p['spuren'][0]
    neu_et = [et for et in p['etappen'] if ERST[(sp, t, et)] == p['klasse']]
    erst_thema = ERST[(sp, t, None)] == p['klasse']
    p['etappen_neu'] = neu_et
    p['rolle'] = 'neu' if erst_thema else 'weitergefuehrt'
print('Rollen', collections.Counter((p['schulart'], p['rolle']) for p in PUNKTE))

# ---------- Klassenlage: erste Klasse mit Hauptbezug je Spur gegen hinterlegte Klasse
JG = {t['id']: (t['j'] or {}) for t in FULL['th']}
KF = {t['id']: (t['kf'] or {}) for t in FULL['th']}
SPUR_KEY = {'gym_by': 'gym_by', 'rs_I': 'rs_by', 'rs_II_III': 'rs_by', 'ib_standard': 'ib_myp', 'ib_extended': 'ib_myp'}
LAGE = []
for t in sorted(TT):
    if t in STILL: continue
    row = dict(thema=t, titel=TT[t])
    for sp in ('gym_by', 'rs_I', 'rs_II_III', 'ib_standard', 'ib_extended'):
        ks = sorted({p['klasse'] for p in SP[sp] if p['haupt'] == t})
        nk = sorted({p['klasse'] for p in SP[sp] if p['neu'].get(t) == 'neben'} - set(ks))
        etk = collections.defaultdict(list)
        for p in SP[sp]:
            if p['haupt'] == t:
                for et in p['etappen']:
                    if ERST[(sp, t, et)] == p['klasse'] and et not in etk[p['klasse']]: etk[p['klasse']].append(et)
        row[sp] = dict(klassen=ks, neben=nk, etappen_je_klasse={str(k): v for k, v in sorted(etk.items())}, hinterlegt=JG[t].get(SPUR_KEY[sp]))
    LAGE.append(row)
abw = []
for r in LAGE:
    for sp in ('gym_by', 'rs_I', 'ib_standard'):
        x = r[sp]
        if x['klassen'] and x['hinterlegt'] != x['klassen'][0]: abw.append((sp, r['thema'], r['titel'][:30], 'hinterlegt', x['hinterlegt'], 'Lehrplan', x['klassen']))
        if not x['klassen'] and x['hinterlegt'] is not None: abw.append((sp, r['thema'], r['titel'][:30], 'hinterlegt', x['hinterlegt'], 'kein Hauptpunkt', x['neben']))
for a in abw: print(a)

# ---------- Wirkung auf thema_jahrgang (Ableitung wie in der DB: jede Zuordnung aus aktiver Basisquelle, klasse_fest gewinnt)
def jahrgang(zmap):
    res = {}
    for t in TT:
        der = {}
        for eid, tz in zmap.items():
            if t not in tz: continue
            e = E[eid]; q = Q[e['q']]
            if not q['a'] or q['r'] != 'basis' or e['arch']: continue
            der[q['s']] = min(der.get(q['s'], 99), q['j'])
        j = dict(der); j.update(KF.get(t, {}))
        res[t] = {k: v for k, v in j.items() if v is not None}
    return res
Z_ALT = {eid: dict(tz) for eid, tz in ZDB.items()}
# RS-Gruppe-I nach LP-RS einrechnen (Vorherstand für LK)
for eid, tz in RSN.items():
    if E[eid]['q'] in RS_SQL_Q: Z_ALT[eid] = dict(tz)
Z_NEU = {eid: dict(tz) for eid, tz in Z_ALT.items()}
for p in PUNKTE:
    if p['schulart'] == 'rs' and p['quelle'] not in RS_SQL_Q: continue   # II/III nur Bericht
    Z_NEU[p['eintrag_id']] = {t: b for t, b in p['neu'].items()}
    for t in p['veraltet']: Z_NEU[p['eintrag_id']][t] = 'neben'   # veraltet bleibt als Neben stehen (kein Löschen)
JA, JN = jahrgang(Z_ALT), jahrgang(Z_NEU)
for t in sorted(TT):
    if JA[t] != JN[t]: print('Klasse ändert sich', t, TT[t][:30], JA[t], '->', JN[t])

# ---------- Aufbau
V = FULL.get('v') or LK['v']
def klasse_ab(sp, t):
    r = next((r for r in LAGE if r['thema'] == t), None)
    if not r: return None
    x = r[sp]
    if x['klassen']: return x['klassen'][0]
    if x['neben']: return x['neben'][0]
    return None
SPUREN = ('gym_by', 'rs_I', 'rs_II_III', 'ib_standard', 'ib_extended')
VERSTOSS = []
for v in V:
    t, b, art = v['t'], v['b'], v['art']
    if t in STILL or b in STILL: continue
    for sp in SPUREN:
        kt, kb = klasse_ab(sp, t), klasse_ab(sp, b)
        if kt is None: continue
        if kb is None: VERSTOSS.append(dict(spur=sp, thema=t, braucht=b, art=art, kt=kt, kb=None, befund='Voraussetzung ist in dieser Spur kein Lehrplanstoff'))
        elif kb > kt: VERSTOSS.append(dict(spur=sp, thema=t, braucht=b, art=art, kt=kt, kb=kb, befund='Voraussetzung liegt später'))
print('Verstöße', collections.Counter((x['spur'], x['befund'][:20]) for x in VERSTOSS))
# 3b Reihenfolge der Etappen im Thema gegen Klasse
REIHE = []
for r in LAGE:
    t = r['thema']
    for sp in SPUREN:
        ek = {}
        for k, ets in r[sp]['etappen_je_klasse'].items():
            for et in ets: ek[et] = int(k)
        seq = [et for et in ET.get(t, []) if et in ek]
        for i, a in enumerate(seq):
            for bb in seq[i+1:]:
                if ek[bb] < ek[a]: REIHE.append(dict(spur=sp, thema=t, frueher_im_thema=a, klasse_a=ek[a], spaeter_im_thema=bb, klasse_b=ek[bb]))
print('Reihenfolge-Hinweise', len(REIHE), collections.Counter(x['spur'] for x in REIHE))
if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'zeige':
    for x in REIHE:
        if x['spur'] == 'rs_I': print(x)
    for x in VERSTOSS: print(x)

# ---------- Teilen (Regel 14:25): Maßstab Gym, sonst RS I, sonst IB
STAND = json.load(open('/tmp/lpw/lk_stand.json'))
ERL = collections.defaultdict(set)
for k, t, lz in STAND['erledigt']: ERL[(k, t)].add(lz)
FLUG = {(k, t) for k, t in STAND['flug']}
def massstab(r):
    for sp in ('gym_by', 'rs_I', 'ib_standard'):
        if r[sp]['klassen']: return sp
    return None
TEILEN, GRENZ = [], []
for r in LAGE:
    t = r['thema']; sp = massstab(r)
    if not sp: continue
    ek = {int(k): v for k, v in r[sp]['etappen_je_klasse'].items()}
    ks = sorted(ek)
    andere = {}
    for sp2 in SPUREN:
        if sp2 == sp: continue
        e2 = {int(k): v for k, v in r[sp2]['etappen_je_klasse'].items()}
        sp_later = [(k, len(v)) for k, v in sorted(e2.items())[1:] if len(v) >= 3]
        if sp_later: andere[sp2] = sp_later
    teile = []
    if len(ks) >= 2:
        for k in ks[1:]:
            n = len(ek[k])
            if n >= 3: teile.append(k)
            elif n >= 1: GRENZ.append(dict(thema=t, titel=TT[t], spur=sp, klasse=k, etappen=ek[k], art='nur %d Etappe(n) in späterer Klasse' % n))
    if teile:
        TEILEN.append(dict(thema=t, titel=TT[t], spur=sp, teile=[dict(klasse=k, etappen=ek[k]) for k in ks], teilen_ab=teile, andere_spuren=andere))
    elif andere:
        GRENZ.append(dict(thema=t, titel=TT[t], spur=sp, klasse=None, etappen=None, art='andere Lage in ' + ', '.join(f"{a} (Kl. {', '.join(str(k)+': '+str(n)+' Et.' for k, n in v)})" for a, v in andere.items())))
for x in TEILEN: print('TEILEN', x['thema'], x['titel'], x['spur'], [(p['klasse'], len(p['etappen'])) for p in x['teile']], x['andere_spuren'])
for x in GRENZ: print('GRENZ', x['thema'], x['titel'][:30], x['spur'], x['klasse'], x['art'][:90])

# ---------- Stand je Kind (nur Nummern)
KINDER = [1, 2]
def stand_teile(t, sp):
    r = next(r for r in LAGE if r['thema'] == t)
    ek = {int(k): v for k, v in r[sp]['etappen_je_klasse'].items()}
    out = []
    for k, ets in sorted(ek.items()):
        out.append(dict(klasse=k, etappen=ets, je_kind={str(kid): len(set(ets) & ERL[(kid, t)]) for kid in KINDER}))
    return out
for g in GRENZ:
    sps = [s for s in SPUREN if s != g['spur'] and next(r for r in LAGE if r['thema'] == g['thema'])[s]['etappen_je_klasse']]
    g['teile_je_spur'] = {s: stand_teile(g['thema'], s) for s in [g['spur']] + sps}
    g['flug_geschafft'] = [k for k in KINDER if (k, g['thema']) in FLUG]
# Nachtrag Lernstand Punkt 6: Themen mit Lernstand, die in der Kinder-Spur (Gym) auf mehrere Klassen verteilt sind
VERTEILT = []
for r in LAGE:
    t = r['thema']; ks = r['gym_by']['klassen']
    for kid in KINDER:
        if not ERL[(kid, t)] and (kid, t) not in FLUG: continue
        if len(ks) >= 2:
            VERTEILT.append(dict(kind=kid, thema=t, je_klasse=[dict(klasse=x['klasse'], verlangt=len(x['etappen']), erledigt=x['je_kind'][str(kid)]) for x in stand_teile(t, 'gym_by')]))
GESCHAFFT_FEHLT = []
for kid, t in FLUG:
    r = next((r for r in LAGE if r['thema'] == t), None)
    if not r: continue
    for sp in ('gym_by',):
        for x in stand_teile(t, sp):
            fehlt = [e for e in x['etappen'] if e not in ERL[(kid, t)]]
            if fehlt: GESCHAFFT_FEHLT.append(dict(kind=kid, thema=t, spur=sp, klasse=x['klasse'], fehlt=fehlt))
print('verteilt', VERTEILT); print('geschafft, aber offen', GESCHAFFT_FEHLT)

# ---------- Korrektur-SQL (Gym, IB; RS-Nachtrag nur Gruppe I und RS 5/6)
def scope(p):
    return p['schulart'] in ('gym', 'ib') or p['quelle'] in RS_SQL_Q
q_ = lambda s: "'" + s.replace("'", "''") + "'"
def beg(p, t):
    if t == p['haupt']:
        r = {'neu': 'neu', 'weitergefuehrt': 'weitergeführt'}[p['rolle']]
        return q_(f"LK-D 22.11.2026: {r}; Etappen: {', '.join(p['etappen']) or 'ganzes Thema'}" + (f"; {p['notiz']}" if p['notiz'] else ''))
    return q_("LK-D 22.11.2026: Nebenbezug" + (f"; {p['notiz']}" if p['notiz'] else ''))
S_DEM, S_ALT, S_PRO, S_INS = [], [], [], []
ERWARTET = []
for p in PUNKTE:
    if not scope(p): continue
    e, alt, neu = p['eintrag_id'], p['alt'], p['neu']
    for t, b in neu.items(): ERWARTET.append((e, t, b))
    for t, b in alt.items():
        if b == 'haupt' and neu.get(t) != 'haupt':
            S_DEM.append(f"update schule.zuordnung set bezug = 'neben' where eintrag_id = {e} and thema_id = {t} and bezug = 'haupt';")
    for t in p['veraltet']:
        S_ALT.append(f"update schule.zuordnung set bezug = 'neben', pruefstatus = 'klaerungsbedarf', begruendung = {q_('LK-D 22.11.2026: veraltet (Thema stillgelegt oder ersetzt), nicht mehr werten')} where eintrag_id = {e} and thema_id = {t} and (bezug <> 'neben' or pruefstatus <> 'klaerungsbedarf');")
    for t, b in neu.items():
        if t in alt and alt[t] != b and b == 'haupt':
            S_PRO.append(f"update schule.zuordnung set bezug = 'haupt', begruendung = {beg(p, t)}, pruefstatus = 'geprueft' where eintrag_id = {e} and thema_id = {t} and bezug <> 'haupt';")
        elif t not in alt:
            S_INS.append(f"({e}, {t}, '{b}', {beg(p, t)})")
GYM_LB = sorted(e['id'] for e in FULL['e'] if e['q'] in (1, 2, 3, 4, 5, 6) and e['art'] in ('lernbereich', 'unterbereich'))
SCOPE_Q = sorted({p['quelle'] for p in PUNKTE if scope(p)})
SQL = f"""-- LK-D (22.11.2026): Zuordnung Gymnasium 5–10 und IB MYP 1–5 je Lehrplanpunkt, dazu Nachtrag Realschule (Gruppe I, RS 5/6).
-- Bericht: inhalte/pruefung/lehrplan/lk_pruefung_2211.md · Daten je Punkt (rolle, etappen): lk_daten_2211.json.
-- Erst NACH rs_korrektur_2211.sql einspielen (Schritt 0 prüft das). In EINER Transaktion (psql -1).
-- Nur INSERT und UPDATE auf schule.zuordnung und schule.eintrag. Kein DROP, kein DELETE; schule.thema bleibt unverändert.
-- Veraltete Zuordnungen (stillgelegte oder ersetzte Themen) werden auf Nebenbezug mit pruefstatus 'klaerungsbedarf' gesetzt.
-- Rolle (neu/weitergeführt) und Etappen stehen in begruendung der geänderten Zeilen; die Felder rolle/etappen füllt LK-S aus der JSON.
-- Klassen ändern sich nicht (Rauchtest c, simuliert und im Probelauf geprüft) – wichtig, weil die Kinder im Gymnasium lernen.

do $$ begin
  if not exists (select 1 from schule.zuordnung where eintrag_id = 864 and thema_id = 30 and bezug = 'haupt') then
    raise exception 'Schritt 0: rs_korrektur_2211.sql ist noch nicht eingespielt';
  end if;
  perform set_config('lk.jahrgang_vorher', (select jsonb_object_agg(id::text, schule.thema_jahrgang(id)) from schule.thema)::text, true);
end $$;

-- 1) Hauptbezüge, die nicht Haupt bleiben, zuerst auf Neben (eindeutiger Hauptbezug je Eintrag)
""" + "\n".join(S_DEM) + """

-- 2) Veraltete Zuordnungen kennzeichnen (kein Löschen)
""" + "\n".join(S_ALT) + """

-- 3) Nebenbezüge zu Hauptbezügen
""" + "\n".join(S_PRO) + """

-- 4) Fehlende Zuordnungen ergänzen
insert into schule.zuordnung (eintrag_id, thema_id, bezug, begruendung, pruefstatus)
select v.e, v.t, v.b, v.g, 'geprueft' from (values
""" + ",\n".join("  " + r for r in S_INS) + """
) v(e, t, b, g)
where exists (select 1 from schule.eintrag where id = v.e) and exists (select 1 from schule.thema where id = v.t)
on conflict (eintrag_id, thema_id) do nothing;

-- 5) Gymnasium: Lern- und Unterbereiche geprüft (Titel, Stunden gegen LehrplanPLUS vom 22.11.). Punkte nicht (DB teilt feiner als das Original).
update schule.eintrag set pruefstatus = 'geprueft' where id in (""" + ", ".join(map(str, GYM_LB)) + """) and pruefstatus <> 'geprueft';

-- 6) Rauchtest (liest nur)
do $$
declare v_txt text; v_n int;
begin
  -- a) jede erwartete Zuordnung mit erwartetem Bezug
  select string_agg(v.e || '/' || v.t || ':' || v.b, ', ') into v_txt from (values """ + ", ".join(f"({e},{t},'{b}')" for e, t, b in ERWARTET) + """) v(e, t, b)
   where not exists (select 1 from schule.zuordnung z where z.eintrag_id = v.e and z.thema_id = v.t and z.bezug = v.b);
  if v_txt is not null then raise exception 'Rauchtest a: erwartete Zuordnung fehlt: %', v_txt; end if;
  -- b) Punkte ohne Hauptbezug: nur die beiden IB-Wiederholungskapitel (640, 660)
  select string_agg(e.id::text, ', ' order by e.id) into v_txt from schule.eintrag e
   where e.quelle_id in (""" + ", ".join(map(str, SCOPE_Q)) + """) and e.art in ('kompetenz', 'thema') and not e.archiviert
     and not exists (select 1 from schule.zuordnung z where z.eintrag_id = e.id and z.bezug = 'haupt');
  if coalesce(v_txt, '') <> '640, 660' then raise exception 'Rauchtest b: Punkte ohne Hauptthema weichen ab: %', v_txt; end if;
  -- c) Klassen aller Themen unverändert
  if coalesce(current_setting('lk.jahrgang_vorher', true), '') = '' then raise exception 'Rauchtest c: kein Vorherstand (nicht in einer Transaktion)'; end if;
  select string_agg(t.id::text, ', ') into v_txt from schule.thema t
   where schule.thema_jahrgang(t.id) is distinct from (current_setting('lk.jahrgang_vorher')::jsonb -> t.id::text);
  if v_txt is not null then raise exception 'Rauchtest c: Klasse geändert bei Thema %', v_txt; end if;
  -- d) kein Hauptbezug auf stillgelegte Themen in den bearbeiteten Quellen
  select count(*) into v_n from schule.zuordnung z join schule.eintrag e on e.id = z.eintrag_id
   where e.quelle_id in (""" + ", ".join(map(str, SCOPE_Q)) + """) and z.bezug = 'haupt' and z.thema_id in (""" + ", ".join(map(str, sorted(STILL))) + """);
  if v_n > 0 then raise exception 'Rauchtest d: % Hauptbezüge auf stillgelegte Themen', v_n; end if;
  raise notice 'Rauchtest LK-D bestanden';
end $$;
"""
open('/tmp/lp/inhalte/pruefung/lehrplan/lk_korrektur_2211.sql', 'w').write(SQL)
print('SQL', len(S_DEM), len(S_ALT), len(S_PRO), len(S_INS), 'erwartet', len(ERWARTET), 'quellen', SCOPE_Q)

# ---------- Lieferdateien: JSON und Tabellen
GYM_ORIG = {1: {'1.1': 7, '1.2': 5, '2': 5, '3.1': 7, '3.2': 5, '4.1': 5, '4.2': 5}, 2: {'1.1': 4, '1.2': 3, '1.3': 5, '1.4': 3, '1.5': 4, '2.1': 4, '2.2': 5, '3': 5},
            3: {'1.1': 4, '1.2': 5, '2.1': 3, '2.2': 4, '3': 4, '4': 3, '5': 9}, 4: {'1': 3, '2': 5, '3': 3, '4': 5, '5': 4, '6': 3, '7': 4},
            5: {'1': 5, '2.1': 5, '2.2': 3, '3': 2, '4': 3, '5': 4, '6': 3, '7.1': 4, '7.2': 2}, 6: {'1': 5, '2': 4, '3': 7, '4': 3, '5': 7}}
TXT = {e['id']: e for e in LK['e']}
def befund(p):
    ah = [t for t, b in p['alt'].items() if b == 'haupt' and t not in STILL]
    if not p['haupt']: return 'wiederholung' if p['schulart'] == 'ib' else 'luecke'
    if not ah: return 'ergaenzt'
    return 'ok' if ah[0] == p['haupt'] else 'umgehaengt'
for p in PUNKTE: p['befund'] = befund(p)
def lbkey(p):
    pf = p['pfad'].split('/')[0]
    if p['schulart'] == 'ib': pf = p['pfad'].split('.')[0]
    return pf
def lbtitel(p):
    if p['schulart'] == 'rs':
        for (q, pf, eid, tdb, tor, *_ ) in D.LB:
            if q == p['quelle'] and pf == lbkey(p): return tor
    if p['schulart'] == 'gym':
        e = next((e for e in LK['e'] if e['q'] == p['quelle'] and e['pfad'] == lbkey(p)), None)
        return e['text'] if e else None
    return None
def lbstd(p):
    if p['schulart'] == 'rs':
        for (q, pf, eid, tdb, tor, sd, so, *_ ) in D.LB:
            if q == p['quelle'] and pf == lbkey(p): return so
    if p['schulart'] == 'gym':
        e = next((e for e in LK['e'] if e['q'] == p['quelle'] and e['pfad'] == lbkey(p)), None)
        return e['std'] if e else None
    return None
OUT = []
for p in PUNKTE:
    OUT.append(dict(schulart=p['schulart'], quelle=p['quelle'], klasse=p['klasse'], zweig=p['zweig'], spuren=p['spuren'],
                    lernbereich=dict(pfad=lbkey(p), titel=lbtitel(p), stunden=lbstd(p)), punkt=p['pfad'], eintrag_id=p['eintrag_id'],
                    thema=p['haupt'], thema_titel=TT.get(p['haupt']), bezug='haupt' if p['haupt'] else None, rolle=p['rolle'], etappen=p['etappen'], etappen_neu_in_dieser_klasse=p['etappen_neu'],
                    neben=sorted(t for t, b in p['neu'].items() if b == 'neben'), vorher=p['alt'], veraltet=p['veraltet'], befund=p['befund'], notiz=p['notiz'] or None,
                    korrektur_sql=scope(p)))
KETTE = []
VMAP = collections.defaultdict(list)
for v in V:
    if v['t'] not in STILL and v['b'] not in STILL: VMAP[v['t']].append((v['b'], v['art']))
for r in LAGE:
    t = r['thema']
    for sp in SPUREN:
        x = r[sp]
        if not x['klassen']: continue
        ek = x['etappen_je_klasse']
        bauf = [f"{TT[b]} ({'Kl. ' + str(klasse_ab(sp, b)) if klasse_ab(sp, b) else 'nicht in dieser Schulart'}{', hart' if a == 'hart' else ''})" for b, a in VMAP[t]]
        weiter = [f"Kl. {k}: {', '.join(ek[k])}" for k in sorted(ek, key=int) if int(k) != x['klassen'][0]]
        txt = (f"baut auf {'; '.join(bauf)}" if bauf else 'keine Voraussetzung') + f" · neu in Kl. {x['klassen'][0]}" + (f" · wird weitergeführt in {'; '.join(weiter)}" if weiter else '')
        KETTE.append(dict(spur=sp, thema=t, titel=TT[t], kette=txt))
KEIN_PFLICHT = {sp: sorted(r['thema'] for r in LAGE if not r[sp]['klassen']) for sp in SPUREN}
json.dump(dict(auftrag='LK-D', stand='2026-11-22', hinweis='Kurzfassungen und Titel; keine Lehrplantexte wörtlich. rolle: neu = erste Klasse des Themas in dieser Spur, weitergefuehrt = spätere Klasse. etappen = Lernziel-Schlüssel aus inhalte/themen; etappen_neu_in_dieser_klasse = erstmals verlangt. IB = Orientierung (Schulbuch-Inhaltsverzeichnisse, kein amtlicher Jahresplan).',
               punkte=OUT, lage_je_thema=LAGE, aufbau_kette=KETTE, voraussetzung_verstoesse=VERSTOSS, etappen_reihenfolge_hinweise=REIHE,
               kein_pflichtstoff=KEIN_PFLICHT, teilen=TEILEN, grenzfaelle=GRENZ, kinder=dict(verteilt=VERTEILT, geschafft_aber_spaeter_offen=GESCHAFFT_FEHLT)),
          open('/tmp/lp/inhalte/pruefung/lehrplan/lk_daten_2211.json', 'w'), ensure_ascii=False, indent=1)
# Tabellen
md = []
def tabelle(s, quellen, kopf):
    for q in quellen:
        ps = [p for p in PUNKTE if p['schulart'] == s and p['quelle'] == q]
        if not ps: continue
        if s == 'ib':
            gruppen = collections.OrderedDict()
            for p in ps: gruppen.setdefault((p['klasse'], lbkey(p)), []).append(p)
        else:
            gruppen = collections.OrderedDict()
            for p in ps: gruppen.setdefault((p['klasse'], lbkey(p)), []).append(p)
        md.append(f"\n#### {kopf(q, ps[0])}\n")
        md.append("| LB | Titel | Std. | Punkte Orig./DB | Themen (Rolle) | Lücken |\n|---|---|---|---|---|---|")
        for (kl, pf), gp in gruppen.items():
            th = collections.OrderedDict()
            for p in gp:
                if p['haupt']: th.setdefault(p['haupt'], set()).add(p['rolle'])
            ths = '; '.join(f"{t} {TT[t]} ({'/'.join(sorted('neu' if r == 'neu' else 'weiter' for r in rr))})" for t, rr in th.items())
            orig = GYM_ORIG.get(q, {}).get(pf) if s == 'gym' else None
            if s == 'rs':
                orig = next((no for (qq, p2, eid, tdb, tor, sd, so, nd, no) in D.LB if qq == q and p2 == pf), None)
            lu = ', '.join(p['pfad'] for p in gp if not p['haupt']) or '–'
            md.append(f"| {pf} | {lbtitel(gp[0]) or ''} | {lbstd(gp[0]) or '–'} | {orig if orig is not None else '–'}/{len(gp)} | {ths} | {lu} |")
tabelle('gym', [1, 2, 3, 4, 5, 6], lambda q, p: f"Gymnasium {p['klasse']} (Quelle {q})")
open('/tmp/lpw/lk_tab_gym.md', 'w').write('\n'.join(md)); md.clear()
tabelle('rs', [7, 8, 24, 25, 12, 26, 13, 14, 15, 16], lambda q, p: f"Realschule {p['klasse']}" + ('' if p['zweig'] == 'allgemein' else (' – Gruppe I' if p['zweig'] == 'rs_I' else ' – Gruppe II/III')) + f" (Quelle {q})")
open('/tmp/lpw/lk_tab_rs.md', 'w').write('\n'.join(md)); md.clear()
tabelle('ib', [18, 19, 20, 21, 22, 23], lambda q, p: f"IB MYP (Quelle {q}, {p['zweig']}) – Orientierung")
open('/tmp/lpw/lk_tab_ib.md', 'w').write('\n'.join(md))
print('Befunde', collections.Counter((p['schulart'], p['befund']) for p in PUNKTE))
print('kein Pflicht', {k: len(v) for k, v in KEIN_PFLICHT.items()})
