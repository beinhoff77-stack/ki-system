"""Test für VTEST-S (Verstehen in Tests, Server): tools/tests/vtest_s_einspielen.py, Migration 20261212_vtest_s.sql, Pakete tools/tests/aus/vtest_s_*.sql.

Teil 1 (immer): Pakete und Migration auf dem Stand, Migration = Einspiel-Datei; alte Texte = Stand nach NF-S/TEMPO-S1/FT-S (md5); neuer Text = alter Text + genau die
  Einfügungen (Entfernen aller Einfügungen ergibt den alten Text); in test_starten_intern steht jeder alte Auswahl-Befehl unverändert im else-Zweig von „if v_vt“;
  Klasse V = tools/vtest_pruefen.py; keine Namen, keine Schlüssel.
Teil 2 (nur mit lokalem Postgres; NACHBAU tools/tests/vtest_s_nachbau.py, erfundene Daten – NICHT die echte Datenbank), dreimal: Kollation C, ICU en-US, ICU de-DE:
  Schalter 0 = identisch (gleiche Ergebnisse wie die alten Funktionen in allen Fällen, auch Schalter 2 für ein Nicht-Testkind); Verstehens-Etappe zieht die
  Verstehens-Testaufgabe (Flugtest, Nachtragstest); Korrektur gleicher Art, Rückfälle bei leerem Vorrat; Landung mit/ohne Verstehens-Aufgabe, Tipp zählt nicht,
  Lückenweg zählt nicht, gesperrte Verstehens-Übung zählt nicht; gelandete/wieder geöffnete bleiben; kein Festhängen; gesperrte Aufgaben nie gezogen;
  Testkind-Schalter; Pakete: Probe rollt zurück, Einspielen, Zweitlauf, Voraussetzungen (NF-S, TEMPO-S1, FB-S), Mischstand, ungültige Regel, karte_buchen-Stelle,
  Gegenprobe (verdorbene neue Fassung -> Abbruch).
Aufruf: python3 -I tools/tests/vtest_s_test.py   (endet mit OK)
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
sys.path.insert(0, str(WURZEL / 'tools'))
import fb_einspielen as FB  # noqa: E402
import nf_einspielen as NF  # noqa: E402
import regelbezug_sql_test as T  # noqa: E402
import tempo_einspielen as TE  # noqa: E402
import vtest_s_einspielen as VS  # noqa: E402
import vtest_s_nachbau as NB  # noqa: E402

AUS = WURZEL / 'tools/tests/aus'


def teil1():
    p = subprocess.run([sys.executable, '-I', 'tools/tests/vtest_s_einspielen.py', '--pruefen'], capture_output=True, text=True, cwd=str(WURZEL))
    assert p.returncode == 0, p.stderr
    probe = (AUS / 'vtest_s_probe.sql').read_text(encoding='utf-8')
    einsp = (AUS / 'vtest_s_einspielen.sql').read_text(encoding='utf-8')
    assert VS.MIGRATION.read_text(encoding='utf-8') == einsp
    assert 'PROBELAUF bestanden' in probe and 'PROBELAUF' not in einsp and 'VTEST-S eingespielt' in einsp
    assert probe.count("raise exception 'VTEST-S KURZ % PROBELAUF bestanden") == 1
    assert 'VTEST-S ABBRUCH' not in probe and 'NICHT bestanden' not in einsp
    assert not re.search(r'(?im)^\s*(begin|commit|rollback|savepoint)\s*;', einsp + probe), 'kein BEGIN/COMMIT im Paket'
    assert ' exception when ' not in (einsp + probe).lower(), 'keine Untertransaktion'
    erste = [z for z in probe.split('\n') if not z.startswith('--')][0]
    assert erste.startswith("select set_config('lock_timeout'"), 'Zeitgrenzen zuerst'
    # alte Texte: Stand nach NF-S / TEMPO-S1 / LB-3+FT-S
    assert VS.md5(VS.tsi_alt()) == '7abcd2918f5042142d8720ae044b36c1' == VS.md5(NF.tsi_neu())
    assert VS.md5(VS.es_alt()) == '3f49198f8dbf5c822a0be4650a5ebce5' == VS.md5(TE.neuer_text())
    assert VS.md5(TE.alter_text()) == VS.ES_VOR_TEMPO and VS.md5(NF.tsi_alt()) == VS.TSI_VOR_NF
    assert VS.md5(FB.waehlen_neu()) == VS.FB_W_NEU and VS.md5(FB.mischkarten_neu()) == VS.FB_M_NEU
    import vtest_sql as VSQL  # noqa: E402
    assert VSQL.VTEST_S_TSI == VS.md5(VS.tsi_neu()), 'tools/vtest_sql.py kennt den neuen Stand von test_starten_intern'
    # neuer Text = alter Text + Einfügungen
    for (_, _, _, alt, neu), ein in zip(VS.GEAENDERT, (VS.TSI_EIN, VS.ES_EIN, VS.KL_EIN)):
        a, n = alt(), neu()
        r = n
        for _, e, _ in ein:
            assert n.count(e) == 1 and a.count(e) == 0, e[:60]
            r = r.replace(e, '')
        assert r == a, 'Entfernen der Einfügungen ergibt den alten Text'
        assert VS.md5(n) in einsp and VS.md5(a) in einsp and VS.md5(n) in probe
    # test_starten_intern: jeder alte Auswahl-Befehl steht unverändert im else-Zweig von „if v_vt then“
    n = VS.tsi_neu()
    for anfang, ende in (("        select coalesce(array_agg(a.id order by a.reihenfolge)", "-- VTEST-S (a) Flugtest"),
                         ("          select a.id into v_aid from schule.aufgabe a\n            where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool in ('test', 'korrektur') and a.freigegeben\n              and not exists",
                          "-- VTEST-S (a) Nachtragstest"),
                         ("        select a.id into v_aid from schule.aufgabe a\n          where a.einheit_id = v_einheit and a.variante_gruppe = r.lernziel and a.pool = 'korrektur'", "-- VTEST-S (b) Korrektur")):
        i = n.index(anfang)
        assert n.rfind('if v_vt then', 0, i) > n.rfind('end if; -- VTEST-S', 0, i) and n[:i].rstrip(' ').endswith('else\n'), anfang[:50]
        assert n.index(ende, i) > i
    assert n.count('if v_vt then') == 3 and n.count("v_vt := schule.verstehen_an(p_lernender, 'verstehen_test_an')") == 1
    # Klasse V = Prüfwerkzeug
    import vtest_pruefen as VPR  # noqa: E402
    assert tuple(VPR.V_TYPEN) == VS.V_TYPEN and tuple(VPR.V_FORMEN) == VS.V_FORMEN
    # öffentliches Repo: keine Schlüssel
    alles = einsp + probe + (WURZEL / 'tools/tests/vtest_s_einspielen.py').read_text(encoding='utf-8') + (WURZEL / 'tools/tests/vtest_s_nachbau.py').read_text(encoding='utf-8')
    assert not re.search(r'(?i)(eyJ[a-z0-9]{20}|sk-[a-z0-9]{20}|service_role)', alles)
    print(f'Teil 1 bestanden: Pakete auf dem Stand ({len(einsp.encode())} Bytes), neue Texte = alte + Einfügungen, alte Auswahl im else-Zweig, Klasse V = Prüfwerkzeug')
    return probe, einsp


# ---------- Daten (erfunden) ----------
ETAPPEN1 = ['A', 'B', 'C', 'D']
AUFGABEN = [
    # id, einheit, pool, lz, freigegeben, stufe, typ, form, zaehlt, reihenfolge
    (101, 1, 'test', 'A', True, 2, None, None, None, 10),
    (102, 1, 'test', 'B', False, 2, None, None, None, 20),                      # alte Rechen-Testaufgabe, gesperrt (wie vtest_sql.py)
    (103, 1, 'test', 'B', True, 3, 'fehler', 'fehler_detektiv', 'ja', 80001),
    (104, 1, 'test', 'C', True, 2, None, None, None, 30),
    (105, 1, 'test', 'D', True, 2, None, None, None, 40),                       # Rechen-Testaufgabe NICHT gesperrt
    (106, 1, 'test', 'D', True, 2, 'umkehr', 'umkehren', 'ja', 80002),
    (107, 1, 'test', 'D', False, 2, 'begruenden', None, 'ja', 1),               # gesperrte Verstehens-Testaufgabe (stünde vorn)
    (201, 1, 'korrektur', 'A', True, 2, None, None, None, 100),
    (202, 1, 'korrektur', 'A', True, 2, None, None, None, 101),
    (203, 1, 'korrektur', 'A', True, 2, 'parameter', None, 'ja', -100001),
    (211, 1, 'korrektur', 'B', True, 2, 'umkehr', 'umkehren', 'ja', -100003),
    (212, 1, 'korrektur', 'B', True, 2, 'fehler', 'fehler_detektiv', 'ja', -100002),
    (213, 1, 'korrektur', 'B', True, 2, None, None, None, 110),
    (214, 1, 'korrektur', 'B', False, 2, 'umkehr', None, 'ja', -100009),         # gesperrt
    (221, 1, 'korrektur', 'D', True, 2, None, None, None, 120),
]
for lz, basis, v in (('A', 300, ('begruenden', None)), ('B', 310, ('fehler', None)), ('C', 320, None), ('D', 330, ('mehrschritt', 'zwei_wege'))):
    for i in range(1, 8):
        AUFGABEN.append((basis + i, 1, 'uebung', lz, True, 1 + i % 2, 'direkt' if i % 2 else 'mehrschritt', None, None, basis + i))
    if v: AUFGABEN.append((basis + 8, 1, 'uebung', lz, True, 2, v[0], v[1], 'ja', basis + 8))
AUFGABEN.append((309, 1, 'uebung', 'A', True, 1, 'umkehr', 'lueckenweg', 'nein', 309))       # Lückenweg mit Verstehens-Typ: zählt nie
for i in range(1, 8):
    AUFGABEN.append((340 + i, 2, 'uebung', 'E', True, 1 + i % 2, 'direkt' if i % 2 else 'mehrschritt', None, None, 340 + i))
AUFGABEN.append((348, 2, 'uebung', 'E', False, 2, 'begruenden', None, 'ja', 348))             # gesperrte Verstehens-Übung


KARTEN = ("insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, eigene_loesungen, typen, folge, gezaehlt, faellig_am) values "
          "(1, 1, 'B', true, now() - interval '9 days', 6, '{direkt,mehrschritt}', 6, '{\"311\": \"2026-11-01\", \"312\": \"2026-11-01\", \"313\": \"2026-11-01\", \"314\": \"2026-11-01\", \"315\": \"2026-11-01\", \"316\": \"2026-11-01\"}', now() + interval '5 days'),"
          "(1, 1, 'D', false, now() - interval '9 days', 6, '{direkt,mehrschritt}', 0, '{\"331\": \"2026-11-01\", \"332\": \"2026-11-01\", \"333\": \"2026-11-01\", \"334\": \"2026-11-01\", \"335\": \"2026-11-01\", \"336\": \"2026-11-01\"}', null);\n")


def sqlwert(x):
    return 'null' if x is None else (str(x).lower() if isinstance(x, bool) else (str(x) if isinstance(x, int) else f"'{x}'"))


DATEN = ("insert into schule.lernender (id, ist_test, zeitzone) values (1, false, 'Europe/Berlin'), (2, false, 'UTC'), (3, true, 'Pacific/Auckland');\n"
         "insert into schule.einheit (id, thema_id, block_id, status, inhalt) values "
         "(1, 1, 1, 'freigegeben', '{\"etappen\": [" + ', '.join(f'{{"lernziel": "{x}"}}' for x in ETAPPEN1) + "]}'), "
         "(2, 2, 2, 'freigegeben', '{\"etappen\": [{\"lernziel\": \"E\"}, {\"lernziel\": \"F\"}]}');\n"
         "insert into schule.thema (id) values (1), (2);\n"
         "insert into schule.aufgabe (id, einheit_id, pool, variante_gruppe, freigegeben, stufe, typ, form, zaehlt, reihenfolge, frage) values\n"
         + ',\n'.join('(' + ', '.join(sqlwert(x) for x in a) + f", '{{\"text\": \"Aufgabe {a[0]}\"}}')" for a in AUFGABEN) + ';\n')


def wert(pg, sql):
    return pg.sql('\\pset tuples_only on\n\\pset format unaligned\n' + sql).strip()


def regeln(t=None, l=None):
    s = ''
    if t is not None: s += f"insert into schule.regel (schluessel, wert) values ('verstehen_test_an', '{t}') on conflict (schluessel) do update set wert = excluded.wert;\n"
    if l is not None: s += f"insert into schule.regel (schluessel, wert) values ('verstehen_landung_an', '{l}') on conflict (schluessel) do update set wert = excluded.wert;\n"
    return s


def szen(pg, sql, fragen):
    """sql + Fragen in EINER Transaktion, danach zurückgerollt. fragen: {name: sql-Ausdruck} -> {name: text}."""
    q = '\n'.join(f"select '{k}=' || coalesce(({e})::text, 'NULL');" for k, e in fragen.items())
    out = pg.sql('\\pset tuples_only on\n\\pset format unaligned\n' + sql + '\n' + q + '\nrollback;')
    return {k: re.search(rf'^{k}=(.*)$', out, re.M).group(1) for k in fragen}


def start(l, e, art):
    return (f"(select coalesce((r->'aufgaben')::text, r->>'grund') from (select schule.test_starten_intern({l}, jsonb_build_object('einheit_id', {e}, 'art', '{art}')) r) z)")


def ids(txt):
    """Liste der Aufgaben-IDs aus der Antwort von test_starten_intern (oder der Grund)."""
    if not txt.startswith('['): return txt
    return [a['id'] for a in json.loads(txt)]


def sitzung(l, art, aufgaben, tage, richtig=(), falsch=(), lz_stand=None):
    """abgeschlossene Testsitzung vor `tage` Tagen mit Versuchen (richtig/falsch; die übrigen bleiben unbeantwortet)."""
    s = (f"insert into schule.testsitzung (lernender_id, einheit_id, art, aufgaben, status, gestartet_am, abgeschlossen_am) values "
         f"({l}, 1, '{art}', '{{{','.join(map(str, aufgaben))}}}', 'abgeschlossen', now() - interval '{tage} days', now() - interval '{tage} days' + interval '10 minutes');\n")
    for a, r in [(a, True) for a in richtig] + [(a, False) for a in falsch]:
        s += (f"insert into schule.versuch (lernender_id, aufgabe_id, client_id, richtig, hilfe, anlauf, testsitzung_id, am) values ({l}, {a}, 't{l}-{a}-{tage}', {str(r).lower()}, 0, 1, "
              f"(select max(id) from schule.testsitzung), now() - interval '{tage} days' + interval '5 minutes');\n")
    return s


def stand(l, werte):
    return ''.join(f"insert into schule.lernziel_stand (lernender_id, einheit_id, lernziel, status) values ({l}, {e}, '{lz}', '{st}') "
                   f"on conflict (lernender_id, einheit_id, lernziel) do update set status = excluded.status;\n" for e, lz, st in werte)


Z = [0]


def antwort(l, a, richtig=True, hilfe=0):
    Z[0] += 1
    return (f"insert into schule.versuch (lernender_id, aufgabe_id, client_id, richtig, hilfe, anlauf, am) values ({l}, {a}, 'u{Z[0]}', {str(richtig).lower()}, {hilfe}, 1, "
            f"now() - interval '1 day' + interval '{Z[0]} seconds');\n")


def sitzt(l, e, lz):
    return f"(select sitzt from schule.karte_stand where lernender_id = {l} and einheit_id = {e} and lernziel = '{lz}')"


def es(l, e, lz, feld):
    return f"(schule.etappen_stand({l}, {e})->'{lz}'->'{feld}')"


# Fälle, deren Ergebnis mit Schalter 0 exakt dem alten Stand gleichen muss (Kind 1 = kein Testkind)
def faelle(l=1):
    st_korr = stand(l, [(1, 'A', 'fehler'), (1, 'B', 'fehler'), (1, 'C', 'nachgewiesen'), (1, 'D', 'fehler')])
    flug = sitzung(l, 'blocktest', [101, 103, 104, 106], 5, richtig=[104], falsch=[101, 103])
    wdh = flug + sitzung(l, 'korrektur', [211], 4, falsch=[211]) + sitzung(l, 'korrektur', [212], 3, falsch=[212])
    nachtrag = sitzung(l, 'blocktest', [101, 103, 104], 5, richtig=[101, 103, 104]) + stand(l, [(1, 'A', 'nachgewiesen'), (1, 'B', 'nachgewiesen'), (1, 'C', 'nachgewiesen'), (1, 'D', 'offen')])
    nachtrag_v = (sitzung(l, 'blocktest', [101, 104, 105], 5, richtig=[101, 104, 105])
                  + stand(l, [(1, 'A', 'nachgewiesen'), (1, 'B', 'offen'), (1, 'C', 'nachgewiesen'), (1, 'D', 'nachgewiesen')]))
    v_leer = (sitzung(l, 'blocktest', [101, 103, 104, 106], 5, richtig=[101, 104], falsch=[103]) + sitzung(l, 'korrektur', [211, 212, 221], 4, falsch=[211, 212])
              + stand(l, [(1, 'A', 'nachgewiesen'), (1, 'B', 'fehler'), (1, 'C', 'nachgewiesen'), (1, 'D', 'nachgewiesen')]))
    return {
        'flug': ('', start(l, 1, 'blocktest')),
        'korr': (flug + st_korr, start(l, 1, 'korrektur')),
        'korr_wdh': (wdh + st_korr, start(l, 1, 'korrektur')),
        'nachtrag': (nachtrag, start(l, 1, 'blocktest')),
        'nachtrag_v': (nachtrag_v, start(l, 1, 'blocktest')),
        'korr_v_leer': (v_leer, start(l, 1, 'korrektur')),
        'es1': ('', f'schule.etappen_stand({l}, 1)'), 'es2': ('', f'schule.etappen_stand({l}, 2)'),
        'land_A': (''.join(antwort(l, a) for a in range(301, 307)), sitzt(l, 1, 'A')),
        'land_A_es': (''.join(antwort(l, a) for a in range(301, 307)), f'schule.etappen_stand({l}, 1)'),
    }


def lauf(pg, fall, vor=''):
    sql, frage = fall
    return szen(pg, vor + sql, {'x': frage})['x']


def teil2_locale(probe, einsp, icu):
    if icu: os.environ['RB_PG_ICU'] = icu
    else: os.environ.pop('RB_PG_ICU', None)
    pg = T.PG(T.pg_bin())
    name = icu or 'C'
    try:
        pg.sql(NB.sql() + DATEN)
        koll = wert(pg, "select datcollate || '/' || coalesce(daticulocale, '-') from pg_database where datname = current_database();")
        assert (icu or '-') in koll, koll
        # Bezugsfunktionen im Nachbau = Repo-Stand
        for s, t in VS.bezug():
            assert wert(pg, f"select md5(prosrc) from pg_proc where oid = '{s}'::regprocedure;") == VS.md5(t), s
        alt = {k: lauf(pg, f) for k, f in faelle(1).items()}
        alt3 = {k: lauf(pg, f) for k, f in faelle(3).items()}
        assert ids(alt['flug']) == [101, 104, 105, 103, 106], alt['flug']                     # bisher: alle freigegebenen Test-Aufgaben nach reihenfolge
        assert ids(alt['korr']) == [203, 211, 221], alt['korr']
        assert ids(alt['korr_wdh']) == [203, 213, 221], alt['korr_wdh']
        assert ids(alt['nachtrag']) == [105] and ids(alt['nachtrag_v']) == [103], (alt['nachtrag'], alt['nachtrag_v'])
        assert alt['land_A'] == 'true'
        zustand0 = wert(pg, "select md5(string_agg(p.oid::regprocedure::text || md5(p.prosrc) || coalesce(p.proacl::text, ''), '|' order by p.oid::regprocedure::text)) "
                            "from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule';")
        regel0 = wert(pg, "select coalesce(string_agg(schluessel || '=' || wert::text, ',' order by schluessel), '') from schule.regel;")

        # --- Voraussetzungen und Schutz (je in einer Transaktion, die abbricht)
        neg = [
            ('NF-S fehlt', f"create or replace function schule.test_starten_intern(p_lernender bigint, p_daten jsonb) returns jsonb language plpgsql set search_path to '' as $function${NF.tsi_alt()}$function$;", 'erst NF-S'),
            ('TEMPO-S1 fehlt', f"create or replace function schule.etappen_stand(p_lernender bigint, p_einheit bigint) returns jsonb language sql stable set search_path to '' as $function${TE.alter_text()}$function$;", 'erst TEMPO-S1'),
            ('FB-S fehlt', f"set check_function_bodies = off; create or replace function schule.wdh_aufgabe_waehlen(p_l bigint, p_e bigint, p_lz text, p_misch boolean) returns bigint language sql volatile set search_path to '' as $function${FB.waehlen_alt()}$function$;", 'erst FB-S'),
            ('karte_landet fremd', "create or replace function schule.karte_landet(k schule.karte_stand) returns boolean language sql stable set search_path to '' as $function$ select true $function$;", 'karte_landet(schule.karte_stand) weicht ab'),
            ('karte_landet STRICT', "alter function schule.karte_landet(schule.karte_stand) strict;", 'Eigenschaften'),
            ('Regel ungültig', regeln(t=5), 'ungültigen Wert'),
            ('karte_buchen ohne Stelle', f"create or replace function schule.karte_buchen(p_l bigint, p_aufgabe bigint, p_richtig boolean, p_hilfe smallint, p_zeit timestamp with time zone) returns void language plpgsql set search_path to '' as $$ begin return; end $$;", 'karte_buchen: Stelle'),
            ('Bezug anders', "create or replace function schule.aufgabe_zaehlt(a schule.aufgabe) returns boolean language sql immutable set search_path to '' as $function$ select true $function$;", 'Bezugsfunktion schule.aufgabe_zaehlt'),
        ]
        for titel, vor, meldung in neg:
            for paket, kennung in ((probe, 'VTEST-S PROBELAUF NICHT bestanden'), (einsp, 'VTEST-S ABBRUCH')):
                out = pg.sql(vor + f'\ndo $rbpaket$ begin execute $rbpaketinhalt${paket}$rbpaketinhalt$; end $rbpaket$;', erwartet_fehler=kennung)
                assert meldung in out, (titel, meldung, out[-600:])
        # Gegenprobe: verdorbene neue etappen_stand (ändert die Ausgabe mit Schalter AUS) und verdorbene karte_landet -> Abbruch
        es_v = VS.es_neu().replace("else '{}'::jsonb end /* VTEST-S */", "else '{\"x\": 1}'::jsonb end /* VTEST-S */")
        kl_v = VS.kl_neu().replace('/* VTEST-S */', '/* VTEST-S */ and coalesce(k.folge, 0) > 3')
        karten = KARTEN + ("insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, eigene_loesungen, typen, folge, gezaehlt) values "
                           "(2, 1, 'C', false, 6, '{direkt,mehrschritt}', 3, '{\"321\": \"2026-11-01\"}');\n")
        for var, meldung in (({'schule.etappen_stand(bigint, bigint)': es_v}, 'etappen_stand 6 von 6'), ({'schule.karte_landet(schule.karte_stand)': kl_v}, 'karte_landet 1 von 3')):
            out = pg.sql(karten + f'\ndo $rbpaket$ begin execute $rbpaketinhalt${VS.paket(True, var)}$rbpaketinhalt$; end $rbpaket$;', erwartet_fehler='VTEST-S PROBELAUF NICHT bestanden')
            assert 'mit Schalter AUS weicht ab' in out and meldung in out, out[-800:]
        assert wert(pg, "select md5(string_agg(p.oid::regprocedure::text || md5(p.prosrc) || coalesce(p.proacl::text, ''), '|' order by p.oid::regprocedure::text)) "
                        "from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule';") == zustand0
        print(f'[{name}] Voraussetzungen/Schutz: {len(neg)} Negativfälle je Probe und Einspielen brechen ab; Gegenprobe (2 verdorbene Fassungen) bricht ab')

        # --- Probelauf
        out = pg.paket(probe, erwartet_fehler='PROBELAUF bestanden')
        z = [x for x in out.splitlines() if 'ERROR:' in x][0]
        kurz = json.loads(z[z.index('KURZ ') + 5:z.index(' PROBELAUF')])
        assert kurz['zustand'] == 'alt -> neu' and kurz['abweichungen_aus'] == 0 and kurz['etappen_stand_verglichen'] == 6 and kurz['karten_verglichen'] == 0, kurz
        assert kurz['flugtest_aufgaben_bisher_neu'] == [5, 4] and kurz['test_etappen_verstehen'] == 2, kurz
        pg.sql(probe, erwartet_fehler='PROBELAUF bestanden')
        assert wert(pg, "select md5(string_agg(p.oid::regprocedure::text || md5(p.prosrc) || coalesce(p.proacl::text, ''), '|' order by p.oid::regprocedure::text)) "
                        "from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule';") == zustand0
        assert wert(pg, "select coalesce(string_agg(schluessel || '=' || wert::text, ',' order by schluessel), '') from schule.regel;") == regel0
        # Probe mit Lernständen (Karten, Korrekturen) – auch dann bestanden
        mit = (faelle(1)['korr'][0] + ''.join(antwort(2, a) for a in range(301, 307)) + ''.join(antwort(2, a) for a in (311, 312, 318)))
        out = pg.sql(mit + f'\ndo $rbpaket$ begin execute $rbpaketinhalt${probe}$rbpaketinhalt$; end $rbpaket$;', erwartet_fehler='PROBELAUF bestanden')
        z = [x for x in out.splitlines() if 'ERROR:' in x][0]
        kurz = json.loads(z[z.index('KURZ ') + 5:z.index(' PROBELAUF')]); voll = json.loads(z[z.index(' VOLL ') + 6:])
        assert kurz['karten_verglichen'] == 2 and kurz['korrektur_offen_v_r_unbekannt'] == [3, 2, 1, 0] and kurz['abweichungen_aus'] == 0, kurz
        assert voll['landebereit_bis_auf_verstehen'] == 0 and voll['karten_nie_gelandet'] == 1 and voll['davon_mit_verstehens_uebung'] == 1, voll
        assert voll['verstehen_neue_da'] == 1 and voll['verstehen_rueckfall_rechnen'] == 1 and voll['rechnen_neue_da'] == 1 and voll['davon_verstehen_schon_ok'] == 1, voll
        print(f'[{name}] Probelauf bestanden (leer und mit Lernständen), alles zurückgerollt')

        # --- Einspielen, Zweitlauf
        out = pg.sql(f'do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;\n'
                     "select 'TEMP=' || count(*) from pg_proc p where p.pronamespace = pg_my_temp_schema();")
        assert 'VTEST-S eingespielt KURZ' in out and '"zustand": "alt -> neu"' in out and 'TEMP=0' in out, out[-500:]
        out = pg.paket(einsp)
        assert '"zustand": "neu -> neu (schon eingespielt, nichts geändert)"' in out, out[-500:]
        assert wert(pg, "select string_agg(schluessel || '=' || wert::text, ',' order by schluessel) from schule.regel where schluessel like 'verstehen%';") == 'verstehen_landung_an=0,verstehen_test_an=0'
        for s in VS.SOLL:
            assert wert(pg, f"select has_function_privilege('authenticated', '{s}', 'execute');") == ('t' if s == 'schule.etappen_stand(bigint, bigint)' else 'f'), s
        # Mischstand -> Abbruch
        out = pg.sql(f"create or replace function schule.karte_landet(k schule.karte_stand) returns boolean language sql stable set search_path to '' as $function${VS.kl_alt()}$function$;\n"
                     f'do $rbpaket$ begin execute $rbpaketinhalt${einsp}$rbpaketinhalt$; end $rbpaket$;', erwartet_fehler='VTEST-S ABBRUCH')
        assert 'Mischstand' in out, out[-500:]
        out = pg.sql(f"drop function schule.verstehen_korrektur_art(bigint, bigint, text);\n"
                     f'do $rbpaket$ begin execute $rbpaketinhalt${probe}$rbpaketinhalt$; end $rbpaket$;', erwartet_fehler='VTEST-S PROBELAUF NICHT bestanden')
        assert 'Mischstand' in out, out[-500:]
        print(f'[{name}] Einspielen, Zweitlauf (neu -> neu), Schalter 0, Rechte; Mischstand bricht ab')

        # --- Schalter 0 (und Schalter 2 für ein Nicht-Testkind) = identisch
        for t, l in ((0, 0), (2, 2)):
            neu = {k: lauf(pg, f, regeln(t, l)) for k, f in faelle(1).items()}
            assert neu == alt, (t, {k: (alt[k], neu[k]) for k in alt if alt[k] != neu[k]})
        neu3 = {k: lauf(pg, f, regeln(0, 0)) for k, f in faelle(3).items()}
        assert neu3 == alt3
        print(f'[{name}] Schalter 0 und Schalter 2 (Nicht-Testkind): alle {len(alt)} Fälle identisch zum alten Stand')

        # --- Schalter 1: Tests
        an = {k: lauf(pg, f, regeln(1, 1)) for k, f in faelle(1).items()}
        assert ids(an['flug']) == [101, 103, 104, 106], an['flug']                  # je Etappe eine; Verstehens-Etappen B, D: Verstehen; Reihenfolge der Etappen
        assert ids(an['korr']) == [201, 211, 221], an['korr']                       # A Rechnen falsch -> Rechnen; B Verstehen -> Verstehen; D unbeantwortet V, kein V-Vorrat -> R
        assert ids(an['korr_wdh']) == [201, 211, 221], an['korr_wdh']               # B: V-Vorrat verbraucht -> schon gestellte V (am längsten her: 211), nicht R 213
        assert ids(an['nachtrag']) == [106], an['nachtrag']                         # D offen: Verstehens-Testaufgabe statt Rechen-Testaufgabe 105
        assert ids(an['nachtrag_v']) == [103], an['nachtrag_v']
        assert ids(an['korr_v_leer']) == [211], an['korr_v_leer']
        # Testkind-Schalter 2: Kind 3 bekommt die neue Auswahl
        t3 = {k: lauf(pg, f, regeln(2, 2)) for k, f in faelle(3).items()}
        assert ids(t3['flug']) == [101, 103, 104, 106] and ids(t3['korr']) == [201, 211, 221] and t3['land_A'] == 'false', t3
        # gesperrte Aufgaben nie (alle Fälle, beide Schalter)
        for d in (alt, an, t3):
            for k, v in d.items():
                if v.startswith('['): assert not {102, 107, 214, 348} & set(ids(v)), (k, v)
        # Rückfall Rechnen, wenn die Etappe gar keine Verstehens-Korrektur hat; „Vorrat erschöpft“ nur ohne jede Korrektur-Aufgabe
        r = szen(pg, regeln(1, 1) + sitzung(1, 'blocktest', [101, 103, 104, 106], 5, richtig=[101, 103, 104]) + sitzung(1, 'korrektur', [221], 4, falsch=[221])
                 + stand(1, [(1, 'A', 'nachgewiesen'), (1, 'B', 'nachgewiesen'), (1, 'C', 'nachgewiesen'), (1, 'D', 'fehler')]),
                 {'x': start(1, 1, 'korrektur')})['x']
        assert r == 'vorrat_erschoepft', r
        print(f'[{name}] Schalter 1: Flugtest je Etappe eine (Verstehen statt Rechnen), Nachtragstest, Korrektur gleicher Art + Rückfälle, Testkind-Schalter, gesperrte nie')

        # --- Schalter 1: Landung
        x = szen(pg, regeln(1, 1) + ''.join(antwort(1, a) for a in range(301, 307)),
                 {'s': sitzt(1, 1, 'A'), 'n': es(1, 1, 'A', 'verstehen_noetig'), 'ok': es(1, 1, 'A', 'verstehen_ok'), 'nC': es(1, 1, 'C', 'verstehen_noetig'),
                  'nE': es(1, 2, 'E', 'verstehen_noetig'), 'nF': es(1, 2, 'F', 'verstehen_noetig')})
        assert x == {'s': 'false', 'n': 'true', 'ok': 'false', 'nC': 'false', 'nE': 'false', 'nF': 'false'}, x
        x = szen(pg, regeln(1, 1) + ''.join(antwort(1, a) for a in range(301, 307)) + antwort(1, 308), {'s': sitzt(1, 1, 'A'), 'n': es(1, 1, 'A', 'verstehen_noetig'), 'ok': es(1, 1, 'A', 'verstehen_ok')})
        assert x == {'s': 'true', 'n': 'false', 'ok': 'true'}, x
        # Verstehen zuerst gelöst, dann Rechnen: landet im selben Moment wie bisher
        x = szen(pg, regeln(1, 1) + antwort(1, 308) + ''.join(antwort(1, a) for a in range(301, 306)), {'s': sitzt(1, 1, 'A')})
        assert x['s'] == 'true', x
        # Tipp zählt nicht, Lückenweg zählt nie; danach selbst gelöst -> landet (kein Festhängen)
        x = szen(pg, regeln(1, 1) + ''.join(antwort(1, a) for a in range(301, 307)) + antwort(1, 308, hilfe=1) + antwort(1, 309) + antwort(1, 301),
                 {'s': sitzt(1, 1, 'A'), 'ok': es(1, 1, 'A', 'verstehen_ok')})
        assert x == {'s': 'false', 'ok': 'false'}, x
        x = szen(pg, regeln(1, 1) + ''.join(antwort(1, a) for a in range(301, 307)) + antwort(1, 308, richtig=False) + antwort(1, 308, hilfe=1) + antwort(1, 308),
                 {'s': sitzt(1, 1, 'A')})
        assert x['s'] == 'false', x                                                  # Verstehen jetzt da, aber nach dem Fehler fehlen 3 in Folge
        x = szen(pg, regeln(1, 1) + ''.join(antwort(1, a) for a in range(301, 307)) + antwort(1, 308, richtig=False) + antwort(1, 308, hilfe=1) + antwort(1, 308)
                 + antwort(1, 301) + antwort(1, 302), {'s': sitzt(1, 1, 'A')})
        assert x['s'] == 'true', x
        # Etappe ohne Verstehens-Übung (C) und mit nur gesperrter (E): wie bisher
        x = szen(pg, regeln(1, 1) + ''.join(antwort(1, a) for a in range(321, 327)) + ''.join(antwort(1, a) for a in range(341, 347)),
                 {'c': sitzt(1, 1, 'C'), 'e': sitzt(1, 2, 'E')})
        assert x == {'c': 'true', 'e': 'true'}, x
        # Testkind-Schalter: Kind 1 wie bisher, Kind 3 braucht Verstehen
        x = szen(pg, regeln(2, 2) + ''.join(antwort(1, a) for a in range(301, 307)) + ''.join(antwort(3, a) for a in range(301, 307)),
                 {'k1': sitzt(1, 1, 'A'), 'k3': sitzt(3, 1, 'A'), 'f1': f"(schule.etappen_stand(1, 1)->'A') ? 'verstehen_noetig'", 'n3': es(3, 1, 'A', 'verstehen_noetig')})
        assert x == {'k1': 'true', 'k3': 'false', 'f1': 'false', 'n3': 'true'}, x
        # schon gelandet bleibt gelandet; wieder geöffnet landet ohne Verstehen (nur nie gelandete Etappen)
        gel = KARTEN
        x = szen(pg, regeln(1, 1) + gel + antwort(1, 311) + antwort(1, 317) + antwort(1, 331) + antwort(1, 332) + antwort(1, 333),
                 {'b': sitzt(1, 1, 'B'), 'bn': es(1, 1, 'B', 'verstehen_noetig'), 'd': sitzt(1, 1, 'D'), 'dn': es(1, 1, 'D', 'verstehen_noetig')})
        assert x == {'b': 'true', 'bn': 'false', 'd': 'true', 'dn': 'false'}, x
        # Schalter danach aus: offene Karte landet bei der nächsten Antwort wie bisher
        x = szen(pg, regeln(1, 1) + ''.join(antwort(1, a) for a in range(301, 307)) + regeln(1, 0) + antwort(1, 307), {'s': sitzt(1, 1, 'A')})
        assert x['s'] == 'true', x
        # kein Festhängen: jede Etappe von Einheit 1 und 2 landet, wenn das Kind alle freigegebenen zählenden Übungen einmal selbst löst
        alle = wert(pg, "select string_agg(id::text, ',' order by variante_gruppe, stufe, id) from schule.aufgabe where pool = 'uebung' and freigegeben "
                        "and zaehlt is distinct from 'nein' and einheit_id in (1, 2);")
        x = szen(pg, regeln(1, 1) + ''.join(antwort(2, int(a)) for a in alle.split(',')),
                 {'n': "(select count(*) from schule.karte_stand where lernender_id = 2 and sitzt)", 'pf': "(select count(*) from schule.karte_stand k where lernender_id = 2 "
                  "and schule.karte_verstehen_pflicht(k, 2, k.einheit_id, k.lernziel) and not schule.karte_verstehen_ok(k))"})
        assert x == {'n': '5', 'pf': '0'}, x
        print(f'[{name}] Schalter 1: Landung nur mit Verstehen (Tipp/Lückenweg zählen nicht), ohne/gesperrte Verstehens-Übung wie bisher, gelandete/wieder geöffnete bleiben, Testkind, kein Festhängen')
    finally:
        pg.ende()


def main():
    probe, einsp = teil1()
    if not T.pg_bin():
        print('Teil 2 übersprungen (kein Postgres)')
    else:
        alt = os.environ.get('RB_PG_ICU')
        try:
            for icu in (None, 'en-US', 'de-DE'):
                teil2_locale(probe, einsp, icu)
        finally:
            if alt is None: os.environ.pop('RB_PG_ICU', None)
            else: os.environ['RB_PG_ICU'] = alt
    print('OK')


if __name__ == '__main__':
    main()
