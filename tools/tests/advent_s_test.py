"""Test für ADVENT-S (Adventskalender, Server): Migration 20261209_advent_s.sql, Pakete tools/tests/aus/advent_s_*.sql, Werkzeug tools/advent_belegung_sql.py.

Teil 1 (immer): Pakete auf dem Stand, Einspiel-Paket = Migration byteidentisch, erste Anweisung = Zeitgrenzen, kein BEGIN/COMMIT, bestehende Pakete unter
  tools/tests/aus/ unverändert gegenüber origin/lernen-app (md5), keine Vornamen/Schlüssel in den neuen Dateien.
Teil 2 (nur mit lokalem Postgres; NACHBAU, NICHT die echte Datenbank) – je Lauf ohne ICU (C) und mit ICU (en-US wie live, de-DE):
  Probe rollt zurück, Einspielen, Zweitlauf ändert nichts, Verhalten (Tageswechsel Australien, Grenzen 1.12./24.12./25.12./31.12./1.1./6.1./7.1. in beiden
  Einstellungen, höchstens 2 am Tag, je Türchen eine eigene Etappe, Nachbessern, ältestes zuerst, Zukunftstür zu, doppeltes Öffnen gleichzeitig,
  Sterne genau einmal, kein Inhalt geschlossener Türen in Kind-Antworten, fremdes Kind, Gutscheine, Krampus, Tausch mit Verboten und Gleichzeitigkeit,
  Belegung nur geschlossener Türen, Schalter), Negativfälle des Pakets, Belegungs-Werkzeug.
ATTRAPPE: Landung und „Sitzt wieder!“ werden als Zeilen in schule.karte_stand nachgestellt (sitzt, sitzt_am, landung_art, landung.am) – so, wie
  karte_buchen/landung_speichern sie live schreiben; die echte Landelogik läuft hier nicht. schule.sterne ist eine vereinfachte Tabelle mit derselben
  Prüfregel und demselben eindeutigen Schlüssel. Die Uhr (schule.advent_jetzt) wird im Nachbau nach dem Einspielen ersetzt.
Aufruf: python3 -I tools/tests/advent_s_test.py   (endet mit OK; RB_PG_ICU=de-DE prüft nur diese eine Variante)
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WURZEL / 'tools/tests'))
sys.path.insert(0, str(WURZEL / 'tools'))
import advent_pakete as AP  # noqa: E402
import regelbezug_sql_test as T  # noqa: E402

AUS = WURZEL / 'tools/tests/aus'
MIG = AP.MIGRATION
GRUND_ALT = ['uebung', 'test', 'ort', 'einloesung', 'korrektur_hand', 'bonus', 'expedition', 'wdh', 'etappe_abgelegt', 'flug_abgelegt', 'landung']


# ---------------------------------------------------------------- Teil 1
def teil1():
    p = subprocess.run([sys.executable, '-I', 'tools/tests/advent_pakete.py', '--pruefen'], capture_output=True, text=True, cwd=str(WURZEL))
    assert p.returncode == 0, p.stderr
    probe = (AUS / 'advent_s_probe.sql').read_text(encoding='utf-8')
    einsp = (AUS / 'advent_s_einspielen.sql').read_text(encoding='utf-8')
    assert einsp == MIG.read_text(encoding='utf-8'), 'Einspiel-Paket = Migration'
    for t in (probe, einsp):
        erste = [z for z in t.splitlines() if z.strip() and not z.startswith('--')][0]
        assert erste.startswith("select set_config('lock_timeout', '3s', true), set_config('statement_timeout'"), erste
        assert not re.search(r'(?im)^\s*(begin|commit|rollback)\s*;', t), 'kein BEGIN/COMMIT'
        assert '$rbpaketinhalt$' not in t
    assert probe.count('ADVENT-S PROBELAUF bestanden') == 1 and probe.count('ADVENT-S PROBELAUF NICHT bestanden') == 1 and 'PROBELAUF' not in einsp
    assert f'n_fn_soll constant int := {AP.funktionen_soll()};' in probe and "'sterne_unveraendert', st_ok" in probe and 'sterne_unveraendert\', true' not in probe
    ts = (WURZEL / 'supabase/functions/lernen-api/index.ts').read_text(encoding='utf-8')
    assert "schule_advent_oeffnen: ['lernender_id', 'client_id', 'erwartet_nr?']," in ts and "schule_advent_oeffnen: 'erwartet_nr = " in ts
    # bestehende Pakete byteidentisch zu origin/lernen-app
    alt = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'origin/lernen-app', 'tools/tests/aus/'], capture_output=True, text=True, cwd=str(WURZEL))
    if alt.returncode == 0 and alt.stdout.strip():
        n = 0
        for name in alt.stdout.split():
            if name.startswith('tools/tests/aus/advent_s_'):    # die eigenen Pakete (noch nicht eingespielt, Urteil 1215 direkt nachgebessert)
                continue
            b = subprocess.run(['git', 'show', f'origin/lernen-app:{name}'], capture_output=True, cwd=str(WURZEL)).stdout
            assert hashlib.md5(b).hexdigest() == hashlib.md5((WURZEL / name).read_bytes()).hexdigest(), f'{name} verändert'
            n += 1
        print(f'Teil 1: {n} bestehende Pakete unter tools/tests/aus/ (außer advent_s_*) byteidentisch zu origin/lernen-app')
    doku = (WURZEL / 'inhalte/design/advent/server.md').read_text(encoding='utf-8')
    for f, m in AP.bestand_md5().items():
        assert f'`schule.{f}` `{m}`' in doku, f'server.md: md5 von {f} nicht auf dem Stand'
    # öffentliches Repo: keine Schlüssel in den neuen Dateien
    neu = ['supabase/migrations/20261209_advent_s.sql', 'tools/tests/aus/advent_s_probe.sql', 'tools/tests/advent_pakete.py',
           'tools/advent_belegung_sql.py', 'inhalte/design/advent/server.md', 'inhalte/design/advent/belegung-beispiel.json']
    for n in neu:
        t = (WURZEL / n).read_text(encoding='utf-8')
        assert not re.search(r'(?i)(sk_live|service_role|eyJhbGci|BEGIN PRIVATE)', t), n
    print('Teil 1 bestanden: Pakete auf dem Stand, Einspiel-Paket = Migration, Zeitgrenzen zuerst, kein BEGIN/COMMIT')
    return probe, einsp


# ---------------------------------------------------------------- Nachbau
def nachbau_sql():
    zg = (WURZEL / 'supabase/migrations/20261114_w150_lern_zugaenge_plan.sql').read_text(encoding='utf-8')
    zg = zg[:zg.index('-- Bestehende Funktionen auf die neuen Prüfungen umstellen')]
    grund = ', '.join(f"'{g}'" for g in GRUND_ALT)
    return f"""
create role anon nologin; create role authenticated nologin; create role council_mcp nologin;
create schema schule; create schema api; create schema council; create schema extensions;
grant usage on schema api, schule to council_mcp;
create table council.zugaenge (schluessel_hash text, aktiv boolean, rechte text[]);
create or replace function council.zugang(p text, r text) returns bigint language sql as $$ select null::bigint $$;
create table schule.lernender (id bigserial primary key, ist_test boolean not null default false, aktiv boolean not null default true, zeitzone text, anzeigename text);
create table schule.zugang (lernender_id bigint, nutzer_ref text);
create table schule.regel (schluessel text primary key, wert jsonb not null, hinweis text);
create table schule.sterne (id bigserial primary key, lernender_id bigint not null, menge int not null, grund text not null, bezug text, am timestamptz not null default now(),
  unique (lernender_id, grund, bezug));
alter table schule.sterne add constraint sterne_grund_check check (grund = any (array[{grund}]));
create table schule.karte_stand (lernender_id bigint not null, einheit_id bigint not null, lernziel text not null, sitzt boolean not null default false, sitzt_am timestamptz,
  landung_art text, landung jsonb, gesetzt_am timestamptz, primary key (lernender_id, einheit_id, lernziel));
{zg}
insert into schule.lernender (ist_test, zeitzone, anzeigename) values
  (false, 'Australia/Melbourne', 'Kind 1'), (false, 'Australia/Adelaide', 'Kind 2'), (true, 'Australia/Melbourne', 'Testkind'), (false, null, 'Kind 4'), (false, 'Australia/Melbourne', 'Kind 5'), (false, 'Australia/Melbourne', 'Kind 6');
update schule.lernender set aktiv = false where id = 5;
insert into schule.lern_login (name, rolle, lernender_id, code_hash) values ('Mama', 'eltern', null, 'h1'), ('Kind 1', 'kind', 1, 'h2'), ('Kind 2', 'kind', 2, 'h3'),
  ('Testkind', 'kind', 3, 'h4'), ('Lehrer', 'lehrer', null, 'h5'), ('Kind 4', 'kind', 4, 'h6'), ('Kind 6', 'kind', 6, 'h7');
insert into schule.lern_sitzung (token_hash, login_id, laeuft_ab) select x.t, l.id, now() + interval '30 days' from (values ('e', 'h1'), ('k1', 'h2'), ('k2', 'h3'), ('k3', 'h4'), ('t', 'h5'), ('k4', 'h6'), ('k6', 'h7')) x(t, h)
  join schule.lern_login l on l.code_hash = x.h;
insert into schule.sterne (lernender_id, menge, grund, bezug) values (1, 10, 'uebung', 'aufgabe:1'), (2, 80, 'landung', 'landung:1:a');
"""


UHR = """create table if not exists public.testzeit (t timestamptz);
insert into public.testzeit select now() where not exists (select 1 from public.testzeit);
create or replace function schule.advent_jetzt() returns timestamptz language sql stable set search_path to '' as $f$ select coalesce((select t from public.testzeit limit 1), now()) $f$;
"""


class DB:
    def __init__(self, icu):
        if icu: os.environ['RB_PG_ICU'] = icu
        else: os.environ.pop('RB_PG_ICU', None)
        self.pg = T.PG(T.pg_bin())
        self.icu = icu

    def roh(self, text):
        f = Path(self.pg.dir) / f'x{threading.get_ident()}.sql'
        f.write_text(text, encoding='utf-8'); os.chmod(f, 0o644)
        p = subprocess.run([f'{self.pg.bin}/psql', '-h', self.pg.dir, '-p', self.pg.port, '-U', 'postgres', '-X', '-q', '-v', 'ON_ERROR_STOP=1', '-1', '-f', str(f),
                            '-t', '-A'], capture_output=True, text=True)
        return p.returncode, p.stdout, p.stderr

    def sql(self, text):
        rc, out, err = self.roh(text)
        assert rc == 0, err[-3000:]
        return out.strip()

    def fehler(self, text, erwartet):
        rc, out, err = self.roh(text)
        assert rc != 0 and erwartet in err, (erwartet, err[-1500:])
        return err

    def ende(self):
        self.pg.ende()


def api(db, schluessel, aktion, daten=None, fehler=None):
    q = f"set role council_mcp;\nselect api.schule_{aktion}('lern:{schluessel}', $j${json.dumps(daten or {}, ensure_ascii=False)}$j$::jsonb)::text;"
    if fehler:
        return db.fehler(q, fehler)
    return json.loads(db.sql(q))


def zeit(db, ts):
    db.sql(f"update public.testzeit set t = '{ts}'::timestamptz;")


def regel(db, k, w):
    db.sql(f"update schule.regel set wert = '{w}'::jsonb where schluessel = '{k}';")


ETAPPE = [0]


def landen(db, l, ts, e=None, lz=None, art='sauber'):
    """ATTRAPPE einer eigenen Landung bzw. „Sitzt wieder!“: wie karte_buchen + landung_speichern (sitzt, sitzt_am, landung_art, landung.am)."""
    if e is None:
        ETAPPE[0] += 1; e, lz = 900 + ETAPPE[0], f'lz{ETAPPE[0]}'
    db.sql(f"""insert into schule.karte_stand (lernender_id, einheit_id, lernziel, sitzt, sitzt_am, landung_art, landung)
values ({l}, {e}, '{lz}', true, '{ts}'::timestamptz, '{art}', jsonb_build_object('am', '{ts}'::timestamptz))
on conflict (lernender_id, einheit_id, lernziel) do update set sitzt = true, sitzt_am = excluded.sitzt_am, landung_art = excluded.landung_art, landung = excluded.landung;""")
    return e, lz


def wieder_offen(db, l, e, lz):
    db.sql(f"update schule.karte_stand set sitzt = false where lernender_id = {l} and einheit_id = {e} and lernziel = '{lz}';")


def zahl(db, q):
    return int(db.sql(q))


def tueren_inhalt(l, n, marke='GEHEIM'):
    t = []
    for nr in range(1, 25):
        m = f'{marke}-{l}-{nr}'
        if nr == 1: x = {'art': 'bild', 'motiv': 'koala', 'text': m, 'sterne': 50}
        elif nr == 2: x = {'art': 'gutschein', 'titel': m, 'text': 'Gutschein'}
        elif nr == 3: x = {'art': 'sterne', 'variante': 'jackpot', 'sterne': 1111, 'titel': m}
        elif nr == 4: x = {'art': 'krampus', 'titel': m, 'text': 'kleine Pflicht'}
        elif nr == 5: x = {'art': 'sterne', 'variante': 'niete', 'sterne': 1, 'text': m}
        elif nr == 6: x = {'art': 'karte', 'motiv': 'nikolaus', 'text': m}
        elif nr == 7: x = {'art': 'gutschein', 'variante': 'tausch', 'titel': m}
        elif nr == 8: x = {'art': 'leer', 'text': m}
        elif nr == 24: x = {'art': 'karte', 'motiv': 'heiligabend', 'text': m, 'sterne': 2000}
        else: x = {'art': 'gutschein', 'titel': m, 'sterne': 10}
        x['nr'] = nr
        t.append(x)
    return t


def kein_geheimnis(db, l, ausgabe, wo):
    """Kein Inhalt eines (zum Zeitpunkt) GESCHLOSSENEN Türchens in einer Kind-Antwort. Inhalte geöffneter Türen des Geschwisters dürfen nur über den
    Tausch erscheinen (Angebot, getauschte Gutscheine) – sie sind geöffnet, also kein Geheimnis mehr."""
    offen = set(tuple(int(y) for y in x.split(':')) for x in db.sql("select coalesce(string_agg(lernender_id || ':' || nr, ' '), '') from schule.advent_tuer;").split())
    s = json.dumps(ausgabe, ensure_ascii=False) if not isinstance(ausgabe, str) else ausgabe
    for m in re.findall(r'GEHEIM-(\d+)-(\d+)', s):
        k, nr = int(m[0]), int(m[1])
        assert (k, nr) in offen, f'{wo}: Inhalt geschlossener Tür {k}/{nr} beim Kind {l}'
        if k != l:
            assert 'tausch' in wo or 'gutschein' in wo or 'einloesen' in wo, f'{wo}: Inhalt einer Tür des Geschwisters ({k}/{nr}) außerhalb des Tauschs'
    return s


def parallel(db, auftraege):
    """Mehrere Verbindungen gleichzeitig (je eine psql-Sitzung); Rückgabe: Liste (rc, out, err)."""
    erg = [None] * len(auftraege)

    def lauf(i, q):
        erg[i] = db.roh(q)
    th = [threading.Thread(target=lauf, args=(i, q)) for i, q in enumerate(auftraege)]
    for t in th: t.start()
    for t in th: t.join()
    return erg


def zustand(db):
    return db.sql("""select md5(string_agg(x, '|' order by x collate "C")) from (
  select concat(p.oid::regprocedure::text, md5(p.prosrc), p.provolatile, p.prosecdef::text, coalesce(p.proconfig::text, ''), coalesce(p.proacl::text, '')) x
    from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname in ('schule', 'api')
  union all select concat(c.relname, c.relacl::text, c.relrowsecurity::text) from pg_class c join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule'
  union all select concat(conname, pg_get_constraintdef(oid)) from pg_constraint where connamespace = 'schule'::regnamespace
  union all select concat(schluessel, wert::text, hinweis) from schule.regel
  union all select concat(c.relname, a.attname, format_type(a.atttypid, a.atttypmod)) from pg_attribute a join pg_class c on c.oid = a.attrelid
    join pg_namespace n on n.oid = c.relnamespace where n.nspname = 'schule' and a.attnum > 0 and not a.attisdropped) q;""")


# ---------------------------------------------------------------- Teil 2: Einspielen
def kurz(err, bestanden=True):
    """Erste Zeile des Probe-Berichts: „ADVENT-S PROBELAUF [NICHT ]bestanden … KURZ {…}“ -> (Zeile, KURZ als dict)."""
    i = err.index('ADVENT-S PROBELAUF')
    zeile = err[i:].splitlines()[0]
    kopf = 'ADVENT-S PROBELAUF bestanden, ALLES zurückgerollt (nichts eingespielt). KURZ {' if bestanden else 'ADVENT-S PROBELAUF NICHT bestanden ('
    assert zeile.startswith(kopf) and len(zeile) < 600, zeile[:700]
    return zeile, json.loads(zeile[zeile.index('KURZ {') + 5:])


def einspielen(db, probe, einsp):
    db.sql(nachbau_sql())
    n_fn = AP.funktionen_soll()
    assert n_fn == 38, n_fn
    err = db.fehler(probe, 'ADVENT-S PROBELAUF bestanden')
    zeile, k = kurz(err)
    assert k == {'befunde': 0, 'hinweise': 1, 'tabellen': 6, 'funktionen': n_fn, 'funktionen_soll': n_fn, 'aktiv': 0, 'tausch': 0, 'sterne_unveraendert': True,
                 'karte_unveraendert': True, 'zeitzone_fehlt': [4], 'landungen': '0/0'}, k
    assert 'HINWEISE: ZEITZONE FEHLT/UNGÜLTIG: lernender 4' in err and 'BEFUNDE: keine' in err and 'weicht vom Repo ab' not in err, err[-1500:]
    assert 'Sterne Zeilen 2/2, Summe 90/90' in err, err[-1500:]
    assert db.sql("select count(*) from pg_class where relname like 'advent\\_%';") == '0', 'Probe hat etwas zurückgelassen'
    db.pg.paket(probe, erwartet_fehler='ADVENT-S PROBELAUF bestanden')          # auch als ein execute im do-Block (wie der Projektleiter)
    db.pg.paket(einsp)
    z1 = zustand(db)
    err = db.pg.paket(einsp, erwartet_fehler='ADVENT-S ABBRUCH (schon da: ')   # Zweitlauf: Abbruch, kein Weiterlaufen auf schon Vorhandenem
    assert zustand(db) == z1, 'Zweitlauf hat etwas geändert'
    err = db.fehler(probe, 'ADVENT-S ABBRUCH (schon da: ')                      # Probe nach dem Einspielen: derselbe Abbruch, nicht „bestanden“
    assert 'PROBELAUF bestanden' not in err.split('CONTEXT')[0] and 'schule.advent_tuer (relkind r)' in err and 'schule.regel advent_aktiv' in err, err[-800:]
    assert zustand(db) == z1
    # Rechte: nur council_mcp darf die Aktionen, niemand die Tabellen
    assert db.sql("select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'api' and p.proname like 'schule\\_advent\\_%' "
                  "and has_function_privilege('council_mcp', p.oid, 'execute') and not has_function_privilege('anon', p.oid, 'execute') "
                  "and not has_function_privilege('authenticated', p.oid, 'execute') and p.prosecdef and p.proconfig::text = '{\"search_path=\\\"\\\"\"}';") == '11'
    assert db.sql("select count(*) from pg_proc p join pg_namespace n on n.oid = p.pronamespace where n.nspname = 'schule' and p.proname like 'advent\\_%' "
                  "and (has_function_privilege('anon', p.oid, 'execute') or has_function_privilege('council_mcp', p.oid, 'execute'));") == '0'
    assert db.sql("select count(*) from pg_class c where c.relname like 'advent\\_%' and c.relkind = 'r' and c.relrowsecurity "
                  "and not has_table_privilege('anon', c.oid, 'select') and not has_table_privilege('council_mcp', c.oid, 'select');") == '6'
    db.fehler("set role council_mcp; select * from schule.advent_belegung;", 'permission denied')
    db.fehler("set role council_mcp; insert into schule.advent_tuer (jahr) values (2026);", 'permission denied')
    db.sql(UHR)
    print(f'Einspielen: Probe „bestanden“ mit KURZ-Zeile ({len(zeile)} Zeichen, {n_fn} Funktionen, Sterne echt verglichen, Zeitzone fehlt als Hinweis), rollt zurück; '
          'Einspielen; Zweitlauf und Probe danach brechen ab („schon da“), nichts geändert; Rechte wie im Bestand')


def belegen_alle(db):
    for l in (1, 2, 3):
        r = api(db, 'e', 'advent_belegung_setzen', {'lernender_id': l, 'tueren': tueren_inhalt(l, 24)})
        assert r['kinder'][0]['gesetzt'] == 24, r
    # beide zugleich (gleicher Inhalt, gleiche Tür)
    r = api(db, 'e', 'advent_belegung_setzen', {'lernender_ids': [1, 2], 'tueren': [{'nr': 10, 'art': 'gutschein', 'titel': 'BEIDE-0-10', 'sterne': 20}]})
    assert [k['gesetzt'] for k in r['kinder']] == [1, 1], r
    r = api(db, 'e', 'advent_belegung_setzen', {'lernender_ids': [1, 2], 'tueren': [{'nr': 10, 'art': 'gutschein', 'titel': 'BEIDE-0-10', 'sterne': 20}]})
    assert [k['unveraendert'] for k in r['kinder']] == [1, 1], r
    api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 4, 'tueren': [{'nr': 1, 'art': 'leer'}]})


KIND_AKTIONEN = ('advent_stand', 'advent_oeffnen', 'advent_tuer_lesen', 'advent_gutscheine', 'advent_einloesen', 'advent_tauschen')


def schalter_und_zugriff(db):
    zeit(db, '2026-12-03 10:00+11')
    landen(db, 1, '2026-12-03 09:00+11')
    s0 = zahl(db, "select count(*) from schule.sterne;")
    for w, kind in (('0', 'k1'), ('2', 'k1')):
        regel(db, 'advent_aktiv', w)
        for a in KIND_AKTIONEN:
            d = {'lernender_id': 1, 'client_id': 'c-aus', 'nr': 1, 'gutschein_id': 1, 'tauschkarte_id': 1, 'mein_gutschein_id': 2, 'fremder_gutschein_id': 3}
            r = api(db, kind, a, d)
            assert r == {'ok': True, 'aktiv': False, 'grund': 'nicht_aktiv'}, (w, a, r)
    assert zahl(db, "select count(*) from schule.sterne;") == s0 and zahl(db, "select count(*) from schule.advent_tuer;") == 0, 'Schalter aus bucht nichts'
    # 2 = nur Testkind
    assert api(db, 'k3', 'advent_stand', {'lernender_id': 3})['aktiv'] is True
    regel(db, 'advent_aktiv', '1')
    # Eltern-Funktionen gehen auch bei Schalter aus (Füllen vor dem Start) – oben schon belegt
    # fremdes Kind: weder lesen noch öffnen
    for a in KIND_AKTIONEN:
        api(db, 'k1', a, {'lernender_id': 2, 'client_id': 'x', 'nr': 1, 'gutschein_id': 1}, fehler='Kein Zugriff auf diesen Lernenden')
    for a in ('advent_eltern', 'advent_belegung_lesen', 'advent_belegung_setzen', 'advent_gutschein_eltern', 'advent_protokoll'):
        api(db, 'k1', a, {'lernender_id': 1, 'tueren': [{'nr': 1, 'art': 'leer'}], 'gutschein_id': 1, 'aktion': 'einloesen'}, fehler='Nur Eltern')
        api(db, 't', a, {'lernender_id': 1, 'tueren': [{'nr': 1, 'art': 'leer'}], 'gutschein_id': 1, 'aktion': 'einloesen'}, fehler='Nur Eltern')
    api(db, 'k1', 'advent_stand', {}, fehler='lernender_id fehlt')
    api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1}, fehler='client_id fehlt')
    api(db, 'xx', 'advent_stand', {'lernender_id': 1}, fehler='Nicht angemeldet')
    # Eltern öffnen nicht für ein echtes Kind (nur Testkind)
    api(db, 'e', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'e1'}, fehler='nur fürs Testkind')
    api(db, 't', 'advent_oeffnen', {'lernender_id': 2, 'client_id': 'e1'}, fehler='nur fürs Testkind')
    api(db, 'e', 'advent_tauschen', {'lernender_id': 1, 'client_id': 'e1', 'tauschkarte_id': 1, 'mein_gutschein_id': 2, 'fremder_gutschein_id': 3}, fehler='nur fürs Testkind')
    api(db, 'e', 'advent_einloesen', {'lernender_id': 1, 'gutschein_id': 1}, fehler='nur fürs Testkind')
    api(db, 't', 'advent_einloesen', {'lernender_id': 2, 'gutschein_id': 1}, fehler='nur fürs Testkind')
    # Zeitzone fehlt: klarer Grund, kein Berliner Rückfall
    r = api(db, 'k4', 'advent_stand', {'lernender_id': 4})
    assert r['aktiv'] is False and r['grund'] == 'zeitzone_fehlt', r
    assert api(db, 'k4', 'advent_oeffnen', {'lernender_id': 4, 'client_id': 'z'})['grund'] == 'zeitzone_fehlt'
    api(db, 'e', 'advent_stand', {'lernender_id': 5}, fehler='Kind nicht gefunden')    # inaktiv
    print('Schalter 0/2: alle 6 Kind-Aktionen „nicht aktiv“, nichts gebucht; fremdes Kind abgewiesen; Eltern-Aktionen nur Eltern; Zeitzone fehlt -> zeitzone_fehlt')


def tageslauf(db):
    """Kind 1 (Melbourne, Sommerzeit UTC+11) und Kind 2 (Adelaide, Sommerzeit UTC+10:30)."""
    db.sql("delete from schule.karte_stand;")
    # vor dem Start: Landung am 30.11. 23:50 Ortszeit
    zeit(db, '2026-11-30 23:55+11')
    landen(db, 1, '2026-11-30 23:50+11')
    r = api(db, 'k1', 'advent_stand', {'lernender_id': 1})
    assert r['aktiv'] is False and r['grund'] == 'vor_start' and r['start'] == '2026-12-01' and r['menue'] == {'kalender': False, 'gutscheine': False}, r
    assert api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'v1'})['grund'] == 'vor_start'
    # 1.12. 00:10 Ortszeit: die Landung von 23:50 zählt NICHT (anderer Tag)
    zeit(db, '2026-12-01 00:10+11')
    r = api(db, 'k1', 'advent_stand', {'lernender_id': 1})
    assert r['aktiv'] and r['heute'] == '2026-12-01' and r['etappen_heute'] == 0 and r['moeglich_heute'] == 1 and r['frei_heute'] == 0 and r['braucht_etappe'], r
    assert [t['zustand'] for t in r['tueren'][:3]] == ['heute', 'morgen', 'zu'], r['tueren'][:3]
    kein_geheimnis(db, 1, r, 'stand')
    assert api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd1a'})['grund'] == 'keine_etappe'
    e1, lz1 = landen(db, 1, '2026-12-01 00:05+11')
    r = api(db, 'k1', 'advent_stand', {'lernender_id': 1})
    assert r['frei_heute'] == 1 and r['bereit'] and r['tueren'][0]['zustand'] == 'bereit', r
    s0 = zahl(db, "select coalesce(sum(menge), 0) from schule.sterne where lernender_id = 1;")
    r = api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd1b'})
    assert r['geoeffnet'] and r['tuer']['nr'] == 1 and r['tuer']['art'] == 'bild' and r['tuer']['motiv'] == 'koala' and r['tuer']['sterne'] == 50 \
        and r['tuer']['sterne_gutgeschrieben'] and not r['tuer']['nachgeholt'] and r['tuer']['tag'] == '2026-12-01', r
    kein_geheimnis(db, 1, r, 'oeffnen')
    r2 = api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd1b'})       # gleicher Tipp noch einmal
    assert r2['wiederholt'] and r2['tuer']['nr'] == 1, r2
    assert api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd1c'})['grund'] == 'alles_offen'   # Tür 2 ist Zukunft
    assert zahl(db, "select coalesce(sum(menge), 0) from schule.sterne where lernender_id = 1;") == s0 + 50
    assert zahl(db, "select count(*) from schule.sterne where lernender_id = 1 and grund = 'advent';") == 1
    # 5.12.: Türen 2–5 fällig, älteste zuerst, je Türchen eine eigene Etappe, höchstens 2
    zeit(db, '2026-12-05 18:00+11')
    r = api(db, 'k1', 'advent_stand', {'lernender_id': 1})
    assert [t['zustand'] for t in r['tueren'][:7]] == ['offen', 'nachholen', 'nachholen', 'nachholen', 'heute', 'morgen', 'zu'], r['tueren'][:7]
    assert r['moeglich_heute'] == 2 and r['frei_heute'] == 0 and r['naechste_nr'] == 2
    kein_geheimnis(db, 1, r, 'stand 5.12.')
    e2, lz2 = landen(db, 1, '2026-12-05 17:00+11')
    r = api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd5a'})
    assert r['tuer']['nr'] == 2 and r['tuer']['nachgeholt'] and r['tuer']['gutschein']['art'] == 'gutschein' and r['naechste_nr'] == 3 and r['frei_heute'] == 0, r
    assert api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd5b'})['grund'] == 'keine_etappe', 'zwei Türchen brauchen zwei Etappen'
    landen(db, 1, '2026-12-05 17:30+11')
    r = api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd5c'})
    assert r['tuer']['nr'] == 3 and r['tuer']['variante'] == 'jackpot' and r['tuer']['sterne'] == 1111 and r['moeglich_heute'] == 0, r
    landen(db, 1, '2026-12-05 17:45+11')
    r = api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd5d'})
    assert r['grund'] == 'limit' and r['letzte_nr'] == 3, r
    r = api(db, 'k1', 'advent_stand', {'lernender_id': 1})
    assert r['offen_heute'] == 2 and r['moeglich_heute'] == 0 and not r['bereit'] and r['tueren'][5]['zustand'] == 'morgen' and r['tueren'][3]['zustand'] == 'nachholen', r
    # Tür der Zukunft geht nie auf: Tür 6 bleibt am 5.12. zu (auch mit vielen Etappen)
    assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 1 and nr >= 6;") == 0
    # 6.12.: Nachbessern zählt („Sitzt wieder!“ = neue Landezeit derselben Etappe), dieselbe Etappe am selben Tag nur einmal
    zeit(db, '2026-12-06 12:00+11')
    wieder_offen(db, 1, e1, lz1)
    landen(db, 1, '2026-12-06 11:00+11', e1, lz1, 'sauber')
    r = api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd6a'})
    assert r['geoeffnet'] and r['tuer']['nr'] == 4 and r['tuer']['art'] == 'krampus', r
    wieder_offen(db, 1, e1, lz1)
    landen(db, 1, '2026-12-06 11:30+11', e1, lz1, 'sauber')
    assert api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd6b'})['grund'] == 'keine_etappe', 'dieselbe Etappe am selben Tag zweimal'
    # Setzung („Kann er“): sitzt_am neu, aber keine neue Landung (landung.am alt) -> zählt nicht
    db.sql(f"update schule.karte_stand set sitzt_am = '2026-12-06 11:40+11', gesetzt_am = '2026-12-06 11:40+11' where lernender_id = 1 and einheit_id = {e2};")
    assert api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd6c'})['grund'] == 'keine_etappe', 'Setzung zählt nicht'
    # gesetzte Landung ohne landung_art zählt nicht
    db.sql("insert into schule.karte_stand values (1, 777, 'gesetzt', true, '2026-12-06 11:50+11', null, null, '2026-12-06 11:50+11');")
    assert api(db, 'k1', 'advent_oeffnen', {'lernender_id': 1, 'client_id': 'd6d'})['grund'] == 'keine_etappe'
    # Adelaide (UTC+10:30): Etappe 23:50 und 00:10 Ortszeit
    zeit(db, '2026-12-03 23:55+10:30')
    landen(db, 2, '2026-12-03 23:50+10:30')
    r = api(db, 'k2', 'advent_stand', {'lernender_id': 2})
    assert r['heute'] == '2026-12-03' and r['ortszeit'] == '2026-12-03T23:55' and r['frei_heute'] == 1, r
    assert api(db, 'k2', 'advent_oeffnen', {'lernender_id': 2, 'client_id': 'a1'})['tuer']['nr'] == 1
    zeit(db, '2026-12-04 00:15+10:30')
    landen(db, 2, '2026-12-04 00:10+10:30')
    landen(db, 2, '2026-12-03 23:52+10:30')                      # gestern, nicht genutzt: verfällt mit Mitternacht
    r = api(db, 'k2', 'advent_stand', {'lernender_id': 2})
    assert r['heute'] == '2026-12-04' and r['offen_heute'] == 0 and r['etappen_heute'] == 1 and r['frei_heute'] == 1 and r['moeglich_heute'] == 2, r
    r = api(db, 'k2', 'advent_oeffnen', {'lernender_id': 2, 'client_id': 'a2'})
    assert r['tuer']['nr'] == 2 and r['tuer']['tag'] == '2026-12-04' and r['tuer']['nachgeholt'], r
    assert api(db, 'k2', 'advent_oeffnen', {'lernender_id': 2, 'client_id': 'a3'})['grund'] == 'keine_etappe'
    # in Berliner Zeit wäre 23:50 Adelaide derselbe Tag (13:20 UTC) – der Server rechnet mit Adelaide
    assert db.sql("select tag from schule.advent_tuer where lernender_id = 2 and nr = 1;") == '2026-12-03'
    print('Tageslauf: vor Start zu, 1.12. 00:10 zählt Landung von 23:50 nicht, Bereit/Heute/Morgen/Nachholen, ältestes zuerst, je Türchen eigene Etappe, '
          'höchstens 2, Zukunftstür zu, Nachbessern zählt (einmal je Tag), Setzung zählt nicht, Adelaide 23:50/00:10 getrennte Tage')


def gleichzeitig(db):
    """Zwei Verbindungen, ein freies Türchen: gleiche und verschiedene client_id."""
    zeit(db, '2026-12-07 10:00+11')
    for runde, (c1, c2) in enumerate((('g1', 'g1'), ('g2', 'g3'))):
        landen(db, 1, f'2026-12-07 0{runde + 8}:00+11')
        vor_t = zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 1;")
        vor_s = zahl(db, "select count(*) from schule.sterne where lernender_id = 1;")
        q = lambda c: (f"set role council_mcp;\nselect api.schule_advent_oeffnen('lern:k1', '{{\"lernender_id\": 1, \"client_id\": \"{c}\"}}'::jsonb)::text;\n"
                       "select pg_sleep(0.6);")
        erg = parallel(db, [q(c1), q(c2)])
        assert all(e[0] == 0 for e in erg), erg
        antw = [json.loads(e[1].strip().splitlines()[0]) for e in erg]
        offen = [a for a in antw if a.get('geoeffnet') and not a.get('wiederholt')]
        assert len(offen) == 1, antw
        anders = [a for a in antw if a is not offen[0]][0]
        if c1 == c2: assert anders['wiederholt'] and anders['tuer']['nr'] == offen[0]['tuer']['nr'], antw
        else: assert anders['geoeffnet'] is False and anders['grund'] in ('keine_etappe', 'limit'), antw
        assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 1;") == vor_t + 1
        assert zahl(db, "select count(*) from schule.sterne where lernender_id = 1;") <= vor_s + 1
    # viele gleichzeitige Klicks mit zwei freien Etappen: genau 2 Türchen (Tageslimit), nie mehr
    zeit(db, '2026-12-08 10:00+11')
    landen(db, 1, '2026-12-08 09:00+11'); landen(db, 1, '2026-12-08 09:10+11'); landen(db, 1, '2026-12-08 09:20+11')
    q = lambda c: f"set role council_mcp;\nselect api.schule_advent_oeffnen('lern:k1', '{{\"lernender_id\": 1, \"client_id\": \"{c}\"}}'::jsonb)::text;"
    erg = parallel(db, [q(f'p{i}') for i in range(6)])
    assert all(e[0] == 0 for e in erg), erg
    assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 1 and tag = '2026-12-08';") == 2
    assert zahl(db, "select count(*) from schule.advent_tuer t where lernender_id = 1 and t.sterne > 0 and not t.sterne_gebucht;") == 0
    # Sterne genau einmal: je geöffneter Tür mit Sternen genau eine Buchung in der richtigen Höhe
    assert db.sql("""select count(*) from schule.advent_tuer t where t.sterne > 0 and (select count(*) from schule.sterne s where s.lernender_id = t.lernender_id
                     and s.grund = 'advent' and s.bezug = 'advent:' || t.jahr || ':' || t.nr and s.menge = t.sterne) <> 1;""") == '0'
    assert db.sql("select count(*) from schule.sterne s where s.grund = 'advent' and not exists (select 1 from schule.advent_tuer t where t.lernender_id = s.lernender_id "
                  "and s.bezug = 'advent:' || t.jahr || ':' || t.nr);") == '0'
    print('Gleichzeitig (zwei Verbindungen): gleiche client_id -> eine Tür + Wiederholung, verschiedene -> eine Tür; 6 Klicks mit 3 Etappen -> 2 Türchen; Sterne genau einmal')


def oeffnen_q(schluessel, l, cid, erwartet=None, schlaf=0.0):
    d = {'lernender_id': l, 'client_id': cid}
    if erwartet is not None: d['erwartet_nr'] = erwartet
    return f"set role council_mcp;\nselect api.schule_advent_oeffnen('lern:{schluessel}', $j${json.dumps(d)}$j$::jsonb)::text;\n" + (f"select pg_sleep({schlaf});" if schlaf else '')


def erwartet(db):
    """Öffnen an die angezeigte Tür gebunden (Urteil 1215, Auflage 1). Testkind 3: Gerät A = Kind-App (k3), Gerät B = Eltern-App (e, fürs Testkind erlaubt)."""
    zeit(db, '2026-12-09 20:00+11')
    landen(db, 3, '2026-12-09 19:00+11'); landen(db, 3, '2026-12-09 19:10+11')
    r = api(db, 'k3', 'advent_stand', {'lernender_id': 3})
    assert r['naechste_nr'] == 1 and r['frei_heute'] == 2, r                # beide Geräte zeigen „Tür 1 öffnen“
    st0 = zahl(db, "select coalesce(sum(menge), 0) from schule.sterne where lernender_id = 3;")
    # ungültige erwartet_nr: Fehler, nichts geöffnet
    for falsch in (0, 25, -1, 1.5, 'x', '1a', True, [1], {'nr': 1}):
        api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'ef', 'erwartet_nr': falsch}, fehler='erwartet_nr: 1 bis 24')
    assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 3;") == 0
    # falsche erwartete Tür: nichts geöffnet, grund andere_tuer + Stand
    r = api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'e0', 'erwartet_nr': 2})
    assert r['ok'] and r['aktiv'] and r['geoeffnet'] is False and r['grund'] == 'andere_tuer' and r['erwartet_nr'] == 2 and r['naechste_nr'] == 1 \
        and r['frei_heute'] == 2 and r['stand']['naechste_nr'] == 1 and len(r['stand']['tueren']) == 24 and 'tuer' not in r, r
    kein_geheimnis(db, 3, r, 'oeffnen andere_tuer')
    assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 3;") == 0
    # Gerät A öffnet Tür 1 (richtige erwartete Tür)
    a1 = api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'A1', 'erwartet_nr': 1})
    assert a1['geoeffnet'] and not a1['wiederholt'] and a1['schon_offen'] is False and a1['tuer']['nr'] == 1 and a1['tuer']['sterne_gutgeschrieben'] and 'sterne_gutgeschrieben' not in a1, a1
    # Gerät B (andere client_id) tippt „Tür 1 öffnen“: Tür 1 als schon offen, Tür 2 bleibt zu, keine Buchung
    b1 = api(db, 'e', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'B1', 'erwartet_nr': 1})
    assert b1['geoeffnet'] and b1['wiederholt'] and b1['schon_offen'] is True and b1['tuer'] == a1['tuer'] and b1['naechste_nr'] == 2 and b1['frei_heute'] == 1 \
        and b1['stand']['tueren'][0]['zustand'] == 'offen' and b1['stand']['tueren'][1]['zustand'] == 'bereit', b1
    kein_geheimnis(db, 3, b1, 'oeffnen schon_offen')
    assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 3;") == 1
    assert zahl(db, "select coalesce(sum(menge), 0) from schule.sterne where lernender_id = 3;") == st0 + 50
    # Wiederholungen: gleiche client_id (A1) -> wiederholt, nicht schon_offen; B1 noch einmal -> wieder schon_offen; nichts Neues
    a1b = api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'A1', 'erwartet_nr': 1})
    assert a1b['wiederholt'] and a1b['schon_offen'] is False and a1b['tuer'] == a1['tuer'] and 'stand' not in a1b, a1b
    assert api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'A1'})['tuer']['nr'] == 1              # auch ohne erwartet_nr
    assert api(db, 'e', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'B1', 'erwartet_nr': 1})['schon_offen'] is True
    assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 3;") == 1
    # jetzt zeigt B „Tür 2 öffnen“ (aus dem mitgelieferten Stand): öffnet Tür 2 mit der zweiten Etappe; Erwartung als Text „2“ geht auch
    b2 = api(db, 'e', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'B2', 'erwartet_nr': '2'})
    assert b2['geoeffnet'] and not b2['wiederholt'] and b2['tuer']['nr'] == 2 and b2['moeglich_heute'] == 0, b2
    # Limit erreicht: Erwartung einer offenen Tür -> schon_offen (nicht limit); Erwartung der nächsten -> limit wie bisher
    assert api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'A2', 'erwartet_nr': 2})['schon_offen'] is True
    r = api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'A3', 'erwartet_nr': 3})
    assert r['geoeffnet'] is False and r['grund'] == 'limit', r
    # 10.12.: ohne erwartet_nr wie bisher (heutiger App-Stand): älteste fällige Tür; erwartet_nr null = fehlt
    zeit(db, '2026-12-10 20:00+11')
    landen(db, 3, '2026-12-10 19:00+11')
    r = api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'F1'})
    assert r['geoeffnet'] and r['tuer']['nr'] == 3 and r['schon_offen'] is False, r
    landen(db, 3, '2026-12-10 19:05+11')
    r = api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'F2', 'erwartet_nr': None})
    assert r['geoeffnet'] and r['tuer']['nr'] == 4, r
    # Zukunftstür erwartet (veraltete Anzeige) -> andere_tuer; ohne freie Etappe und richtige Erwartung -> keine_etappe wie bisher
    zeit(db, '2026-12-11 20:00+11')
    r = api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'Z1', 'erwartet_nr': 15})
    assert r['grund'] == 'andere_tuer' and r['naechste_nr'] == 5, r
    assert api(db, 'k3', 'advent_oeffnen', {'lernender_id': 3, 'client_id': 'Z2', 'erwartet_nr': 5})['grund'] == 'keine_etappe'
    # zwei Geräte GLEICHZEITIG, zwei freie Etappen, beide zeigen „Tür 5“: genau eine Tür geht auf, das andere Gerät bekommt Tür 5 als schon offen
    landen(db, 3, '2026-12-11 19:00+11'); landen(db, 3, '2026-12-11 19:10+11')
    erg = parallel(db, [oeffnen_q('k3', 3, 'P1', 5, 0.5), oeffnen_q('e', 3, 'P2', 5, 0.5)])
    assert all(e[0] == 0 for e in erg), erg
    antw = [json.loads(e[1].strip().splitlines()[0]) for e in erg]
    neu = [x for x in antw if x['geoeffnet'] and not x['wiederholt']]
    alt = [x for x in antw if x.get('schon_offen')]
    assert len(neu) == 1 and len(alt) == 1 and neu[0]['tuer']['nr'] == 5 and alt[0]['tuer']['nr'] == 5, antw
    assert zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 3 and tag = '2026-12-11';") == 1, 'nur Tür 5, nicht Tür 6'
    # Gegenprobe ohne erwartet_nr (alter App-Stand): dieselbe Lage öffnet zwei Türen – genau das verhindert erwartet_nr
    zeit(db, '2026-12-12 10:00+11')
    landen(db, 3, '2026-12-12 09:00+11'); landen(db, 3, '2026-12-12 09:10+11')
    erg = parallel(db, [oeffnen_q('k3', 3, 'Q1', None, 0.5), oeffnen_q('e', 3, 'Q2', None, 0.5)])
    assert sorted(json.loads(e[1].strip().splitlines()[0])['tuer']['nr'] for e in erg) == [6, 7], erg
    assert db.sql("""select count(*) from schule.advent_tuer t where t.lernender_id = 3 and t.sterne > 0 and (select count(*) from schule.sterne s
                     where s.lernender_id = 3 and s.grund = 'advent' and s.bezug = 'advent:' || t.jahr || ':' || t.nr and s.menge = t.sterne) <> 1;""") == '0'
    print('Erwartete Tür: falsche -> andere_tuer + Stand (nichts auf), richtige -> öffnet, zweites Gerät -> schon_offen (keine Buchung, Tür 2 bleibt zu), '
          'Wiederholung gleiche client_id, Limit/Zukunft/keine Etappe, fehlend/null wie bisher, 9 ungültige Werte abgewiesen; gleichzeitig mit zwei Etappen: eine Tür')


def gid(db, l, nr):
    return zahl(db, f"select g.id from schule.advent_gutschein g join schule.advent_tuer t on t.id = g.tuer_id where t.lernender_id = {l} and t.nr = {nr};")


def oeffne_bis(db, l, schluessel, bis_nr, tag):
    """Öffnet Türchen von Kind l bis bis_nr (je Öffnung eine Etappe; Tage ab tag)."""
    d = 0
    while zahl(db, f"select count(*) from schule.advent_tuer where lernender_id = {l} and nr <= {bis_nr};") < bis_nr:
        zeit(db, f'2026-12-{tag + d:02d} 20:00+11')
        for _ in range(2):
            landen(db, l, f'2026-12-{tag + d:02d} 19:{_:02d}+11')
            r = api(db, schluessel, 'advent_oeffnen', {'lernender_id': l, 'client_id': f'ob-{l}-{tag + d}-{_}'})
            kein_geheimnis(db, l, r, 'oeffnen')
        d += 1


def gutscheine(db):
    zeit(db, '2026-12-09 20:00+11')
    g2 = gid(db, 1, 2)
    r = api(db, 'k1', 'advent_gutscheine', {'lernender_id': 1})
    kein_geheimnis(db, 1, r, 'gutscheine')
    assert [g['id'] for g in r['gutscheine']][0] == g2 and r['krampus'][0]['art'] == 'krampus' and r['zaehler']['krampus_offen'] == 1, r
    r = api(db, 'k1', 'advent_einloesen', {'lernender_id': 1, 'gutschein_id': g2})
    assert r['gutschein']['zustand'] == 'eingeloest' and r['gutschein']['eingeloest_von'] == 'kind' and not r['wiederholt'], r
    assert api(db, 'k1', 'advent_einloesen', {'lernender_id': 1, 'gutschein_id': g2})['wiederholt']
    r = api(db, 'e', 'advent_eltern', {})
    k1 = [k for k in r['kinder'] if k['lernender_id'] == 1][0]
    g = [x for x in k1['gutscheine'] if x['id'] == g2][0]
    assert g['eingeloest_von'] == 'kind:Kind 1' and g['eingeloest_am'], g
    r = api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': g2, 'aktion': 'zurueckholen'})
    assert r['gutschein']['zustand'] == 'offen' and r['gutschein']['zurueckgeholt_von'] == 'eltern:Mama' and 'eingeloest_am' not in r['gutschein'], r
    assert api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': g2, 'aktion': 'zurueckholen'})['unveraendert']
    r = api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': g2, 'aktion': 'einloesen'})
    assert r['gutschein']['zustand'] == 'eingeloest' and r['gutschein']['eingeloest_von'] == 'eltern:Mama', r
    api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': g2, 'aktion': 'zurueckholen'})
    # Krampus: nur Eltern
    gk = gid(db, 1, 4)
    api(db, 'k1', 'advent_einloesen', {'lernender_id': 1, 'gutschein_id': gk}, fehler='Krampus-Aufgaben haken nur Mama oder Papa ab')
    api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': gk, 'aktion': 'einloesen'}, fehler='Krampus-Aufgabe: erledigt oder noch_nicht')
    api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': g2, 'aktion': 'erledigt'}, fehler='nur bei Krampus')
    assert api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': gk, 'aktion': 'erledigt'})['gutschein']['zustand'] == 'erledigt'
    assert api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': gk, 'aktion': 'noch_nicht'})['gutschein']['zustand'] == 'offen'
    api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': gk, 'aktion': 'erledigt'})
    api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': gk, 'aktion': 'loeschen'}, fehler='aktion: einloesen')
    # fremder Gutschein mit eigener lernender_id
    g2b = gid(db, 2, 2) if zahl(db, "select count(*) from schule.advent_tuer where lernender_id = 2 and nr = 2;") else None
    assert g2b
    api(db, 'k1', 'advent_einloesen', {'lernender_id': 1, 'gutschein_id': g2b}, fehler='Gutschein nicht gefunden')
    api(db, 'k1', 'advent_einloesen', {'lernender_id': 1, 'gutschein_id': 999999}, fehler='Gutschein nicht gefunden')
    print('Gutscheine: Kind löst selbst ein, Eltern sehen wer/wann, holen zurück, schalten aus; Krampus nur Eltern (erledigt/noch nicht); fremde abgewiesen')


def tausch(db):
    zeit(db, '2026-12-12 20:00+11')
    oeffne_bis(db, 2, 'k2', 9, 12)
    oeffne_bis(db, 1, 'k1', 9, 12)
    zeit(db, '2026-12-16 20:00+11')
    karte, x, y = gid(db, 1, 7), gid(db, 1, 9), gid(db, 2, 9)
    d = {'lernender_id': 1, 'tauschkarte_id': karte, 'mein_gutschein_id': x, 'fremder_gutschein_id': y, 'client_id': 't1'}
    assert api(db, 'k1', 'advent_tauschen', d) == {'ok': True, 'aktiv': True, 'getauscht': False, 'grund': 'tausch_aus'}
    r = api(db, 'k1', 'advent_gutscheine', {'lernender_id': 1})
    assert r['tausch'] == {'aktiv': False, 'tauschkarten': 1, 'geschwister': []}, r['tausch']
    api(db, 'k1', 'advent_einloesen', {'lernender_id': 1, 'gutschein_id': karte}, fehler='beim Tauschen verbraucht')
    regel(db, 'advent_tausch', '1')
    r = api(db, 'k1', 'advent_gutscheine', {'lernender_id': 1})
    gs = r['tausch']['geschwister']
    assert [g['lernender_id'] for g in gs] == [2, 4], gs          # alle anderen Kinder der Familie (nicht das Testkind)
    assert gs[0]['name'] == 'Kind 2' and y in [g['id'] for g in gs[0]['gutscheine']], gs
    assert all(g['id'] != gid(db, 2, 4) and g['id'] != gid(db, 2, 7) for g in gs[0]['gutscheine']), 'Krampus/Tauschkarte nicht im Angebot'
    # Gutscheinjahr (Urteil 1215, Auflage 5): offener Gutschein des Geschwisters aus einem früheren Advent steht nicht im Angebot und ist nicht tauschbar
    alt_g = zahl(db, """with t as (insert into schule.advent_tuer (jahr, lernender_id, nr, tag, client_id, von, inhalt, sterne, sterne_gebucht, nachgeholt, ausl_einheit, ausl_lernziel, ausl_sitzt_am)
      values (2025, 2, 9, '2025-12-09', 'alt-2025', 'test', '{"art": "gutschein"}', 0, false, false, 1, 'alt', '2025-12-09') returning id)
      insert into schule.advent_gutschein (tuer_id, jahr, nr, herkunft_lernender_id, lernender_id, art, titel) select t.id, 2025, 9, 2, 2, 'gutschein', 'ALT-2025' from t returning id;""")
    r = api(db, 'k1', 'advent_gutscheine', {'lernender_id': 1})
    angebot = [g['id'] for g in r['tausch']['geschwister'][0]['gutscheine']]
    assert alt_g not in angebot and y in angebot, (alt_g, angebot)
    api(db, 'k1', 'advent_tauschen', {**d, 'fremder_gutschein_id': alt_g, 'client_id': 'talt'}, fehler='nur Gutscheine aus diesem Advent')
    assert zahl(db, f"select lernender_id from schule.advent_gutschein where id = {alt_g};") == 2
    db.sql(f"delete from schule.advent_gutschein where id = {alt_g}; delete from schule.advent_tuer where client_id = 'alt-2025';")   # nur Nachbau-Testzeilen
    s = kein_geheimnis(db, 1, r, 'tausch-angebot')         # Geschwister-Gutscheine sind geöffnete Türen des Geschwisters
    # Verbote
    gk1, gk2, g2_1, g2_2 = gid(db, 1, 4), gid(db, 2, 4), gid(db, 1, 2), gid(db, 2, 2)
    api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': g2_2, 'aktion': 'einloesen'})
    karte2 = gid(db, 2, 7)
    for falsch, msg in (({'mein_gutschein_id': gk1}, 'nur normale Gutscheine'), ({'fremder_gutschein_id': gk2}, 'nur normale Gutscheine'),
                        ({'fremder_gutschein_id': g2_2}, 'nur offene Gutscheine'), ({'fremder_gutschein_id': karte2}, 'nur normale Gutscheine'),
                        ({'mein_gutschein_id': karte}, 'drei verschiedene'), ({'tauschkarte_id': g2_1}, 'keine Tauschkarte von dir'),
                        ({'tauschkarte_id': karte2}, 'keine Tauschkarte von dir'), ({'fremder_gutschein_id': g2_1}, 'Gutschein des Geschwisters nicht gefunden'),
                        ({'fremder_gutschein_id': 999999}, 'Gutschein des Geschwisters nicht gefunden')):
        api(db, 'k1', 'advent_tauschen', {**d, **falsch, 'client_id': 'tf'}, fehler=msg)
    api(db, 'e', 'advent_gutschein_eltern', {'gutschein_id': g2_1, 'aktion': 'einloesen'})
    api(db, 'k1', 'advent_tauschen', {**d, 'mein_gutschein_id': g2_1, 'client_id': 'tf'}, fehler='nur offene Gutscheine')
    # Testkind gehört nicht zur Familie
    oeffne_bis(db, 3, 'k3', 9, 12)
    zeit(db, '2026-12-16 20:00+11')
    api(db, 'k3', 'advent_tauschen', {'lernender_id': 3, 'tauschkarte_id': gid(db, 3, 7), 'mein_gutschein_id': gid(db, 3, 9), 'fremder_gutschein_id': y, 'client_id': 'tt'},
        fehler='nur mit dem Geschwister')
    assert zahl(db, "select count(*) from schule.advent_tausch;") == 0
    # gelungener Tausch
    r = api(db, 'k1', 'advent_tauschen', d)
    assert r['getauscht'] and not r['wiederholt'] and r['tausch']['gegeben_id'] == x and r['tausch']['bekommen_id'] == y, r
    assert db.sql(f"select string_agg(id || ':' || lernender_id || ':' || zustand, ' ' order by id) from schule.advent_gutschein where id in ({karte}, {x}, {y});") == \
        ' '.join(f'{i}:{o}:{z}' for i, o, z in sorted(((karte, 1, 'verbraucht'), (x, 2, 'offen'), (y, 1, 'offen'))))
    assert api(db, 'k1', 'advent_tauschen', d)['wiederholt'], 'gleiche client_id'
    api(db, 'k1', 'advent_tauschen', {**d, 'mein_gutschein_id': y, 'fremder_gutschein_id': x, 'client_id': 't2'}, fehler='schon verbraucht')
    r = api(db, 'k2', 'advent_gutscheine', {'lernender_id': 2})
    gx = [g for g in r['gutscheine'] if g['id'] == x][0]
    assert gx['getauscht'] and 'herkunft_lernender_id' not in gx and y not in [g['id'] for g in r['gutscheine']], r
    p = api(db, 'e', 'advent_protokoll', {'anzahl': 5})['eintraege']
    assert p[0]['aktion'] in ('tausch', 'getauscht_von_geschwister') and {p[0]['aktion'], p[1]['aktion']} == {'tausch', 'getauscht_von_geschwister'}, p[:2]
    # Gleichzeitigkeit 1: Kind 2 löst Y2 ein, während Kind 1 genau Y2 eintauscht -> genau eines gelingt
    # neue Tauschkarten für Kind 1 über weitere (noch geschlossene) Türen
    api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 1, 'tueren': [{'nr': 11, 'art': 'gutschein', 'variante': 'tausch', 'titel': 'GEHEIM-1-11'}]})
    api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 1, 'tueren': [{'nr': 12, 'art': 'gutschein', 'variante': 'tausch', 'titel': 'GEHEIM-1-12'}]})
    oeffne_bis(db, 1, 'k1', 12, 16)
    oeffne_bis(db, 2, 'k2', 12, 16)
    zeit(db, '2026-12-19 20:00+11')
    k11, k12, x2, y2 = gid(db, 1, 11), gid(db, 1, 12), gid(db, 1, 10), gid(db, 2, 10)
    q1 = (f"set role council_mcp;\nselect api.schule_advent_tauschen('lern:k1', '{json.dumps({'lernender_id': 1, 'tauschkarte_id': k11, 'mein_gutschein_id': x2, 'fremder_gutschein_id': y2, 'client_id': 'pp1'})}'::jsonb)::text;\nselect pg_sleep(0.4);")
    q2 = f"set role council_mcp;\nselect api.schule_advent_einloesen('lern:k2', '{json.dumps({'lernender_id': 2, 'gutschein_id': y2})}'::jsonb)::text;"
    erg = parallel(db, [q1, q2])
    ok = [e for e in erg if e[0] == 0]
    st = db.sql(f"select lernender_id || ':' || zustand from schule.advent_gutschein where id = {y2};")
    assert st in ('1:offen', '2:eingeloest'), st
    if st == '1:offen': assert erg[0][0] == 0 and erg[1][0] != 0 and 'Gutschein nicht gefunden' in erg[1][2], erg
    else: assert erg[1][0] == 0 and erg[0][0] != 0 and 'nur offene Gutscheine' in erg[0][2], erg
    # Gleichzeitigkeit 2: zwei Tausche mit derselben Tauschkarte (verschiedene client_id) -> genau einer
    ys = [gid(db, 2, n) for n in (11, 12)]
    qs = [f"set role council_mcp;\nselect api.schule_advent_tauschen('lern:k1', '{json.dumps({'lernender_id': 1, 'tauschkarte_id': k12, 'mein_gutschein_id': y, 'fremder_gutschein_id': yy, 'client_id': 'pq' + str(i)})}'::jsonb)::text;\nselect pg_sleep(0.3);"
          for i, yy in enumerate(ys)]
    erg = parallel(db, qs)
    assert sorted(e[0] for e in erg) == [0, 3], erg
    assert zahl(db, f"select count(*) from schule.advent_tausch where tauschkarte_id = {k12};") == 1
    # Summenprobe: jeder Gutschein hat genau einen Besitzer, verbrauchte Karten = Tausche
    assert zahl(db, "select count(*) from schule.advent_gutschein where art = 'tausch' and zustand = 'verbraucht';") == zahl(db, "select count(*) from schule.advent_tausch;")
    print('Tausch: Schalter aus -> tausch_aus; Verbote (Krampus, eingelöst, Tauschkarte, gleiche IDs, fremde Karte, Testkind, Gutschein aus früherem Advent) abgewiesen; '
          'Angebot nur aus diesem Advent; Tausch tauscht genau zwei, '
          'Karte verbraucht, Protokoll beide Kinder; Wiederholung; gleichzeitig Einlösen/Tauschen und zwei Tausche: genau einer')


def einmal_oeffnen(db, l, schluessel, ts, cid):
    landen(db, l, ts)
    return api(db, schluessel, 'advent_oeffnen', {'lernender_id': l, 'client_id': cid})


def grenzen(db):
    """Kind 6 (Melbourne, UTC+11): 24.12., 25.12., 31.12./1.1., 6.1./7.1. in drei Einstellungen."""
    api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 6, 'tueren': [{'nr': n, 'art': 'gutschein', 'titel': f'G6-{n}'} if n % 2 == 0 else {'nr': n, 'art': 'leer'} for n in range(1, 25)]})
    zeit(db, '2026-12-24 12:00+11')
    r = api(db, 'k6', 'advent_stand', {'lernender_id': 6})
    assert r['phase'] == 'laeuft' and r['tueren'][23]['zustand'] == 'heute' and r['tueren'][22]['zustand'] == 'nachholen', r['tueren'][20:]
    assert einmal_oeffnen(db, 6, 'k6', '2026-12-24 11:00+11', 'b24')['tuer']['nr'] == 1
    zeit(db, '2026-12-25 10:00+11')
    r = api(db, 'k6', 'advent_stand', {'lernender_id': 6})
    assert r['phase'] == 'nachholen' and r['tag_nr'] == 25 and all(t['zustand'] != 'heute' for t in r['tueren']) and r['tueren'][23]['zustand'] == 'nachholen' \
        and r['tueren'][1]['zustand'] == 'nachholen' and r['moeglich_heute'] == 2, r
    assert einmal_oeffnen(db, 6, 'k6', '2026-12-25 09:00+11', 'b25')['tuer']['nr'] == 2
    for name, nb, sb in (('C 31.12./6.1.', '2026-12-31', '2027-01-06'), ('A 31.12./31.12.', '2026-12-31', '2026-12-31'), ('B 6.1./6.1.', '2027-01-06', '2027-01-06')):
        regel(db, 'advent_nachholen_bis', f'"{nb}"'); regel(db, 'advent_sichtbar_bis', f'"{sb}"')
        zeit(db, '2026-12-31 23:59+11')
        if name.startswith('C'):       # am 31.12. nur ansehen (Öffnen dort prüfen A und B; höchstens 2 am Tag)
            r = api(db, 'k6', 'advent_stand', {'lernender_id': 6})
            assert r['aktiv'] and r['phase'] == 'nachholen' and r['moeglich_heute'] == 2, (name, r)
        else:
            r = einmal_oeffnen(db, 6, 'k6', '2026-12-31 23:58+11', f'g31-{name}')
            assert r['geoeffnet'], (name, r)
        zeit(db, '2027-01-01 00:01+11')
        r = api(db, 'k6', 'advent_stand', {'lernender_id': 6})
        if nb == '2026-12-31' and sb == '2026-12-31':
            assert r['aktiv'] is False and r['grund'] == 'vorbei' and r['menue'] == {'kalender': False, 'gutscheine': True} and r['gutscheine']['offen'] >= 1, (name, r)
            assert api(db, 'k6', 'advent_oeffnen', {'lernender_id': 6, 'client_id': 'n1'})['grund'] == 'vorbei'
            assert api(db, 'k6', 'advent_tuer_lesen', {'lernender_id': 6, 'nr': 1}) == {'ok': True, 'aktiv': False, 'grund': 'vorbei'}
        elif nb == '2026-12-31':
            assert r['aktiv'] and r['phase'] == 'nur_ansehen' and r['menue']['kalender'] and 'verfallen' in [t['zustand'] for t in r['tueren']], (name, r)
            landen(db, 6, '2027-01-01 00:00+11')
            assert api(db, 'k6', 'advent_oeffnen', {'lernender_id': 6, 'client_id': 'n2'})['grund'] == 'nachholen_vorbei'
            assert api(db, 'k6', 'advent_tuer_lesen', {'lernender_id': 6, 'nr': 1})['tuer']['nr'] == 1
        else:
            assert r['aktiv'] and r['phase'] == 'nachholen', (name, r)
            assert einmal_oeffnen(db, 6, 'k6', '2027-01-01 00:00+11', f'g1-{name}')['geoeffnet']
            zeit(db, '2027-01-06 23:59+11')
            assert einmal_oeffnen(db, 6, 'k6', '2027-01-06 23:58+11', f'g6-{name}')['geoeffnet']
            zeit(db, '2027-01-07 00:01+11')
            landen(db, 6, '2027-01-07 00:00+11')
            r = api(db, 'k6', 'advent_stand', {'lernender_id': 6})
            assert r['aktiv'] is False and r['grund'] == 'vorbei' and r['menue']['gutscheine'], r
            assert api(db, 'k6', 'advent_oeffnen', {'lernender_id': 6, 'client_id': 'n3'})['grund'] == 'vorbei'
        # nach dem Ende: „Meine Gutscheine“ bleibt, solange einer offen ist; Einlösen geht
        if not r['aktiv']:
            g = api(db, 'k6', 'advent_gutscheine', {'lernender_id': 6})
            assert g['aktiv'] and g['menue']['gutscheine'] and g['zaehler']['offen'] >= 1, g
    # alle einlösen -> Menü weg
    zeit(db, '2027-01-07 00:01+11')
    for x in api(db, 'k6', 'advent_gutscheine', {'lernender_id': 6})['gutscheine']:
        if x['zustand'] == 'offen': api(db, 'k6', 'advent_einloesen', {'lernender_id': 6, 'gutschein_id': x['id']})
    r = api(db, 'k6', 'advent_stand', {'lernender_id': 6})
    assert r['menue'] == {'kalender': False, 'gutscheine': False}, r
    assert api(db, 'k6', 'advent_gutscheine', {'lernender_id': 6})['menue']['gutscheine'] is False
    regel(db, 'advent_nachholen_bis', '"2027-01-06"'); regel(db, 'advent_sichtbar_bis', '"2027-01-06"')
    # ungültige Einstellung: klarer Fehler
    regel(db, 'advent_sichtbar_bis', '"2026-12-30"')
    api(db, 'k6', 'advent_stand', {'lernender_id': 6}, fehler='Einstellung in schule.regel ungültig')
    regel(db, 'advent_sichtbar_bis', '"2027-01-06"')
    print('Grenzen: 24.12. heute, 25.12. nur nachholen, 31.12. 23:59/1.1. 00:01 in A (Ende 31.12.), B (6.1.), C (nachholen 31.12., sichtbar 6.1. -> verfallen), '
          '6.1. 23:59/7.1. 00:01; danach Gutscheine bis alle eingelöst')


def belegung(db):
    zeit(db, '2026-12-19 20:00+11')
    vor = db.sql("select md5(string_agg(b::text, '|' order by nr)) from schule.advent_belegung b where lernender_id = 1;")
    api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 1, 'tueren': [{'nr': 20, 'art': 'leer'}, {'nr': 1, 'art': 'leer'}]}, fehler='schon offene Türchen bleiben')
    assert db.sql("select md5(string_agg(b::text, '|' order by nr)) from schule.advent_belegung b where lernender_id = 1;") == vor, 'nichts geändert'
    r = api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 1, 'nur_geschlossene': True, 'tueren': [{'nr': 20, 'art': 'leer'}, {'nr': 1, 'art': 'leer'}]})
    assert r['kinder'][0] == {'lernender_id': 1, 'gesetzt': 1, 'unveraendert': 0, 'uebersprungen_offen': [1]}, r
    t1 = api(db, 'k1', 'advent_tuer_lesen', {'lernender_id': 1, 'nr': 1})['tuer']
    assert t1['art'] == 'bild' and t1['text'] == 'GEHEIM-1-1', 'Geöffnetes bleibt'
    for t, msg in (({'nr': 25, 'art': 'leer'}, 'nr muss 1 bis 24'), ({'nr': 1.5, 'art': 'leer'}, 'nr muss 1 bis 24'), ({'nr': 21, 'art': 'foto'}, 'art muss'),
                   ({'nr': 21, 'art': 'sterne', 'sterne': 6000}, 'sterne ganze Zahl'), ({'nr': 21, 'art': 'sterne', 'sterne': 1.5}, 'sterne ganze Zahl'),
                   ({'nr': 21, 'art': 'sterne', 'sterne': '5'}, 'sterne ganze Zahl'), ({'nr': 21, 'art': 'gutschein'}, 'braucht einen titel'),
                   ({'nr': 21, 'art': 'krampus', 'titel': ' '}, 'braucht einen titel'), ({'nr': 21, 'art': 'bild'}, 'bild braucht ein motiv'),
                   ({'nr': 21, 'art': 'sterne', 'variante': 'doppelt'}, 'variante bei sterne'), ({'nr': 21, 'art': 'karte', 'variante': 'jackpot'}, 'variante nur bei'),
                   ({'nr': 21, 'art': 'leer', 'fuer': 'beide'}, 'unbekanntes Feld'), ({'nr': 21, 'art': 'bild', 'motiv': 'Koala!'}, 'motiv als Schlüssel'),
                   ({'nr': 21, 'art': 'leer', 'titel': 'x' * 81}, 'höchstens 80'), ({'nr': 21, 'art': 'leer', 'text': 'x' * 301}, 'höchstens 300')):
        api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 1, 'tueren': [t]}, fehler=msg)
    api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 1, 'tueren': [{'nr': 21, 'art': 'leer'}, {'nr': 21, 'art': 'leer'}]}, fehler='Tür 21 doppelt')
    api(db, 'e', 'advent_belegung_setzen', {'lernender_ids': [1, 1], 'tueren': [{'nr': 21, 'art': 'leer'}]}, fehler='Kind doppelt')
    api(db, 'e', 'advent_belegung_setzen', {'tueren': [{'nr': 21, 'art': 'leer'}]}, fehler='welche Kinder')
    api(db, 'e', 'advent_belegung_setzen', {'lernender_id': 5, 'tueren': [{'nr': 21, 'art': 'leer'}]}, fehler='Kind nicht gefunden')
    # Eltern sehen alles (auch geschlossene), das Kind nie
    b = api(db, 'e', 'advent_belegung_lesen', {'lernender_id': 1})
    assert b['kinder'][0]['tueren'][22]['belegung']['titel'] == 'GEHEIM-1-23' and b['kinder'][0]['tueren'][0]['offen'], b['kinder'][0]['tueren'][22]
    alle = api(db, 'e', 'advent_belegung_lesen', {})
    assert [k['lernender_id'] for k in alle['kinder']] == [1, 2, 3, 4, 6], [k['lernender_id'] for k in alle['kinder']]
    u = api(db, 'e', 'advent_eltern', {'protokoll': 3})
    assert len(u['protokoll']) == 3 and [k['lernender_id'] for k in u['kinder']] == [1, 2, 3, 4, 6] and u['ohne_teilnahme'] == [], u['ohne_teilnahme']
    k4 = [k for k in u['kinder'] if k['lernender_id'] == 4][0]
    assert k4['lage']['grund'] == 'zeitzone_fehlt', k4
    print('Belegung: geöffnete Türchen bleiben (Abbruch ohne Änderung bzw. überspringen), 15 ungültige Einträge abgewiesen, Eltern sehen alles')


def geheim(db):
    """Jede Kind-Aktion: kein Inhalt geschlossener Türen (Kind 1, 2, Testkind)."""
    zeit(db, '2026-12-19 20:00+11')
    n = 0
    for l, k in ((1, 'k1'), (2, 'k2'), (3, 'k3')):
        for a, d in (('advent_stand', {}), ('advent_gutscheine', {}), ('advent_tuer_lesen', {'nr': 1}), ('advent_oeffnen', {'client_id': f'gh{l}'})):
            r = api(db, k, a, {'lernender_id': l, **d}); kein_geheimnis(db, l, r, a); n += 1
        for nr in range(1, 25):
            q = f"set role council_mcp;\nselect api.schule_advent_tuer_lesen('lern:{k}', '{{\"lernender_id\": {l}, \"nr\": {nr}}}'::jsonb)::text;"
            rc, out, err = db.roh(q)
            kein_geheimnis(db, l, out + err, f'tuer_lesen {nr}'); n += 1
            offen = zahl(db, f"select count(*) from schule.advent_tuer where lernender_id = {l} and nr = {nr};")
            assert (rc == 0) == bool(offen) and (offen or 'ist noch zu' in err), (l, nr, rc, err[-200:])
        g = api(db, k, 'advent_gutscheine', {'lernender_id': l})
        for x in g['gutscheine']:
            r = db.roh(f"set role council_mcp;\nselect api.schule_advent_einloesen('lern:{k}', '{{\"lernender_id\": {l}, \"gutschein_id\": {x['id']}}}'::jsonb)::text;")
            kein_geheimnis(db, l, r[1] + r[2], 'einloesen'); n += 1
        r = db.roh(f"set role council_mcp;\nselect api.schule_advent_tauschen('lern:{k}', '{{\"lernender_id\": {l}, \"tauschkarte_id\": 1, \"mein_gutschein_id\": 2, \"fremder_gutschein_id\": 3, \"client_id\": \"gx\"}}'::jsonb)::text;")
        kein_geheimnis(db, l, r[1] + r[2], 'tauschen'); n += 1
    # alle Kind-Funktionen ohne Schalter erst recht nicht
    print(f'Geheim: {n} Kind-Antworten (alle 6 Kind-Aktionen, Kind 1/2/Testkind, jede Tür) ohne Inhalt geschlossener Türen')


def nichts_da(db, ausser=()):
    t = db.sql("select coalesce(string_agg(relname, ' ' order by relname), '') from pg_class where relname like 'advent\\_%' and relkind = 'r';").split()
    assert sorted(t) == sorted(ausser), t
    assert db.sql("select count(*) from pg_proc where proname like 'advent\\_%' or proname like 'schule\\_advent\\_%';") == ('1' if 'api' in ausser else '0')
    assert 'advent' not in db.sql("select pg_get_constraintdef(oid) from pg_constraint where conname = 'sterne_grund_check';")


def negativ(db, probe, einsp):
    db.sql(nachbau_sql())
    grund = ', '.join(f"'{g}'" for g in GRUND_ALT)
    faelle = [
        ('Prüfregel anders', "alter table schule.sterne drop constraint sterne_grund_check; alter table schule.sterne add constraint sterne_grund_check check (grund = any (array[" + grund + ", 'neu']));",
         'sterne_grund_check unerwartet', "alter table schule.sterne drop constraint sterne_grund_check; alter table schule.sterne add constraint sterne_grund_check check (grund = any (array[" + grund + "]));", ()),
        ('Prüfregel fehlt', "alter table schule.sterne drop constraint sterne_grund_check;", 'sterne_grund_check unerwartet: fehlt',
         "alter table schule.sterne add constraint sterne_grund_check check (grund = any (array[" + grund + "]));", ()),
        ('zugriff fehlt', "alter function schule.zugriff(text, bigint) rename to zugriff_weg;", 'Funktion fehlt: schule.zugriff', "alter function schule.zugriff_weg(text, bigint) rename to zugriff;", ()),
        ('ist_eltern fehlt', "alter function schule.ist_eltern(text) rename to ist_eltern_weg;", 'Funktion fehlt: schule.ist_eltern', "alter function schule.ist_eltern_weg(text) rename to ist_eltern;", ()),
        ('regel fehlt', "alter table schule.regel rename to regel_weg;", 'Tabelle fehlt: schule.regel', "alter table schule.regel_weg rename to regel;", ()),
        ('zeitzone fehlt', "alter table schule.lernender rename column zeitzone to zz;", 'Spalte fehlt: schule.lernender.zeitzone', "alter table schule.lernender rename column zz to zeitzone;", ()),
        ('anzeigename fehlt', "alter table schule.lernender rename column anzeigename to an;", 'Spalte fehlt: schule.lernender.anzeigename', "alter table schule.lernender rename column an to anzeigename;", ()),
        ('landung fehlt', "alter table schule.karte_stand rename column landung to ld;", 'Spalte fehlt: schule.karte_stand.landung', "alter table schule.karte_stand rename column ld to landung;", ()),
        ('eindeutiger Schlüssel fehlt', "alter table schule.sterne drop constraint sterne_lernender_id_grund_bezug_key;", 'eindeutiger Schlüssel (lernender_id, grund, bezug) fehlt',
         "alter table schule.sterne add constraint sterne_lernender_id_grund_bezug_key unique (lernender_id, grund, bezug);", ()),
        # Mischstand (Urteil 1215, Auflage 3): irgendein Advent-Objekt schon da -> Abbruch mit Liste, nichts geändert
        ('Mischstand: eine Tabelle', "create table schule.advent_tuer (id bigint, jahr smallint);", 'ADVENT-S ABBRUCH (schon da: 1 Advent-Objekte)', "drop table schule.advent_tuer;", ('advent_tuer',)),
        ('Mischstand: Tabelle wie die echte', "create table schule.advent_belegung (jahr smallint, lernender_id bigint, nr smallint, art text, variante text, titel text, text text, "
         "sterne integer, motiv text, geaendert_am timestamptz, geaendert_von text);", 'schule.advent_belegung (relkind r)', "drop table schule.advent_belegung;", ('advent_belegung',)),
        ('Mischstand: Index', "create table schule.x_hilf (a int); create index advent_gutschein_kind on schule.x_hilf (a);", 'schule.advent_gutschein_kind (relkind i)',
         "drop table schule.x_hilf;", ()),
        ('Mischstand: api-Funktion', "create function api.schule_advent_stand(p_schluessel text, p_daten jsonb) returns jsonb language sql as $$ select '{}'::jsonb $$;",
         'api.schule_advent_stand(text,jsonb)', "drop function api.schule_advent_stand(text, jsonb);", ('api',)),
        ('Mischstand: interne Funktion', "create function schule.advent_jetzt() returns timestamptz language sql as $$ select now() $$;", 'schule.advent_jetzt()',
         "drop function schule.advent_jetzt();", ('api',)),
        ('Mischstand: Regel', "insert into schule.regel values ('advent_aktiv', '0', 'x');", 'schule.regel advent_aktiv', "delete from schule.regel where schluessel = 'advent_aktiv';", ()),
        ('Mischstand: Regel ungültig', "insert into schule.regel values ('advent_start', '\"abc\"', 'x');", 'schule.regel advent_start', "delete from schule.regel where schluessel = 'advent_start';", ()),
        ('Mischstand: Prüfregel schon mit advent', "alter table schule.sterne drop constraint sterne_grund_check; alter table schule.sterne add constraint sterne_grund_check check (grund = any (array[" + grund + ", 'advent']));",
         'sterne_grund_check enthält advent', "alter table schule.sterne drop constraint sterne_grund_check; alter table schule.sterne add constraint sterne_grund_check check (grund = any (array[" + grund + "]));", ()),
        ('Mischstand: mehrere', "create table schule.advent_protokoll (id bigint); insert into schule.regel values ('advent_tausch', '1', 'x');", 'ADVENT-S ABBRUCH (schon da: 2 Advent-Objekte)',
         "drop table schule.advent_protokoll; delete from schule.regel where schluessel = 'advent_tausch';", ('advent_protokoll',)),
    ]
    for name, vor, msg, zurueck, ausser in faelle:
        db.sql(vor)
        z0 = zustand(db) if 'regel_weg' not in vor else None      # (ohne schule.regel lässt sich der Zustand so nicht erheben)
        err = db.pg.paket(einsp, erwartet_fehler=msg)
        assert z0 is None or zustand(db) == z0, name
        err = db.pg.paket(probe, erwartet_fehler=msg)           # die Probe meldet denselben Abbruch (nicht „bestanden“)
        assert 'PROBELAUF' not in err.split('CONTEXT')[0], (name, err[-600:])
        db.sql(zurueck)
        nichts_da(db)
        assert db.sql("select count(*) from schule.regel where schluessel like 'advent\\_%';") == '0'
    # Sperre auf schule.sterne durch eine laufende Lern-Transaktion: lock_timeout -> Abbruch, nichts geändert
    erg = parallel(db, ["begin; lock table schule.sterne in row exclusive mode; select pg_sleep(5); commit;",
                        "select pg_sleep(0.5);\n" + einsp])
    assert erg[0][0] == 0 and erg[1][0] != 0 and 'lock timeout' in erg[1][2], erg[1][2][-400:]
    nichts_da(db)
    print(f'Negativfälle Paket: {len(faelle) + 1} (Prüfregel anders/fehlt, Funktionen/Tabelle/Spalten fehlen, eindeutiger Schlüssel fehlt, Mischstand: Tabelle, Index, '
          'api-/interne Funktion, Regel, Prüfregel mit advent, mehrere; Sperre -> lock_timeout): jeweils Abbruch, nichts geändert; Probe meldet denselben Abbruch')
    probe_befund(db, probe)
    # danach läuft es sauber durch
    db.pg.paket(einsp)


def probe_befund(db, probe):
    """Probe bricht bei künstlichem Befund mit „NICHT bestanden“ ab (Urteil 1215, Auflage 2) – und rollt trotzdem alles zurück."""
    z0 = zustand(db)
    s0 = db.sql("select count(*) || '/' || sum(menge) from schule.sterne;")
    # 1. schule.sterne ändert sich während des Einspielens (künstlich: Trigger auf schule.regel bucht einen Stern) -> sterne_unveraendert = false
    db.sql("""create function public.t_stern() returns trigger language plpgsql as $f$ begin
  if new.schluessel = 'advent_tausch' then insert into schule.sterne (lernender_id, menge, grund, bezug) values (1, 7, 'bonus', 'probe:kuenstlich'); end if; return new; end $f$;
create trigger t_stern after insert on schule.regel for each row execute function public.t_stern();""")
    err = db.pg.paket(probe, erwartet_fehler='ADVENT-S PROBELAUF NICHT bestanden (1 Befunde)')
    zeile, k = kurz(err, bestanden=False)
    assert k['befunde'] == 1 and k['sterne_unveraendert'] is False and k['tabellen'] == 6 and k['aktiv'] == 0, k
    assert 'BEFUNDE: schule.sterne verändert (Zeilen 2 -> 3, Summe 90 -> 97, Inhalt anders)' in err and 'PROBELAUF bestanden' not in err.split('CONTEXT')[0], err[-1200:]
    db.sql("drop trigger t_stern on schule.regel; drop function public.t_stern();")
    # 2. Bestandsfunktion weicht vom Repo ab (künstlich: Kommentar im Rumpf von schule.sieht) -> Befund, nicht „nur Hinweis“
    d = db.sql("select pg_get_functiondef('schule.sieht'::regproc);")
    db.sql(d.replace('$$', '$$ -- anders', 1) if '$$' in d else d.replace('$function$', '$function$ -- anders', 1))
    err = db.pg.paket(probe, erwartet_fehler='ADVENT-S PROBELAUF NICHT bestanden (1 Befunde)')
    assert 'Bestandsfunktion schule.sieht weicht vom Repo ab' in err and kurz(err, False)[1]['sterne_unveraendert'] is True, err[-1200:]
    db.sql(d)
    db.pg.paket(probe, erwartet_fehler='ADVENT-S PROBELAUF bestanden')
    nichts_da(db)
    assert zustand(db) == z0 and db.sql("select count(*) || '/' || sum(menge) from schule.sterne;") == s0, 'Probe hat etwas zurückgelassen'
    print('Probe mit künstlichem Befund (Stern während des Laufs gebucht; Bestandsfunktion abweichend): jeweils „NICHT bestanden“ mit Befund, nichts zurückgelassen')


def main():
    probe, einsp = teil1()
    if not T.pg_bin():
        print('Teil 2 übersprungen (kein Postgres)'); print('OK'); return
    varianten = [os.environ['RB_PG_ICU']] if os.environ.get('RB_PG_ICU') else [None, 'en-US', 'de-DE']
    for icu in varianten:
        print(f'--- Nachbau {"ICU " + icu if icu else "ohne ICU (C)"} ---')
        db = DB(icu)
        try:
            assert ('icu' if icu else 'libc') == db.sql("select case datlocprovider when 'i' then 'icu' else 'libc' end from pg_database where datname = current_database();")
            ETAPPE[0] = 0
            einspielen(db, probe, einsp)
            belegen_alle(db)
            schalter_und_zugriff(db)
            tageslauf(db)
            gleichzeitig(db)
            erwartet(db)
            gutscheine(db)
            tausch(db)
            grenzen(db)
            belegung(db)
            geheim(db)
            belegung_werkzeug(db, einsp)
        finally:
            db.ende()
        db = DB(icu)
        try:
            negativ(db, probe, einsp)
        finally:
            db.ende()
    print('OK')


def werkzeug(*args):
    return subprocess.run([sys.executable, '-I', 'tools/advent_belegung_sql.py', *args], capture_output=True, text=True, cwd=str(WURZEL))


def belegung_werkzeug(db, einsp):
    bsp = json.loads((WURZEL / 'inhalte/design/advent/belegung-beispiel.json').read_text(encoding='utf-8'))
    with tempfile.TemporaryDirectory() as td:
        def bauen(d, name='b.json'):
            f = Path(td) / name
            f.write_text(json.dumps(d, ensure_ascii=False), encoding='utf-8')
            return werkzeug(str(f), '--aus', td)
        p = bauen(bsp)
        assert p.returncode == 0, p.stderr
        probe = (Path(td) / 'advent_belegung_probe.sql').read_text(encoding='utf-8')
        einsp_b = (Path(td) / 'advent_belegung_einspielen.sql').read_text(encoding='utf-8')
        assert [z for z in einsp_b.splitlines() if not z.startswith('--')][0].startswith("select set_config('lock_timeout'")
        vor = db.sql("select md5(string_agg(b::text, '|' order by lernender_id, nr)) from schule.advent_belegung b;")
        offen1 = db.sql("select string_agg(nr::text, ', ' order by nr) from schule.advent_tuer where lernender_id = 1;")
        tv = db.sql("select md5(string_agg(t::text, '|' order by id)) from schule.advent_tuer t;")
        err = db.pg.paket(probe, erwartet_fehler='ADVENT-BELEGUNG PROBELAUF bestanden')
        assert db.sql("select md5(string_agg(b::text, '|' order by lernender_id, nr)) from schule.advent_belegung b;") == vor
        out = db.pg.paket(einsp_b)
        i = out.index('ADVENT-BELEGUNG eingespielt. KURZ: ')
        assert f'übersprungen (schon offen) [{offen1}]' in out[i:], out[i:i + 600]
        assert db.sql("select md5(string_agg(t::text, '|' order by id)) from schule.advent_tuer t;") == tv, 'geöffnete Türchen unverändert'
        assert db.sql("select titel from schule.advent_belegung where lernender_id = 2 and nr = 3;") == 'Kinoabend' or '3' in db.sql("select string_agg(nr::text, ',') from schule.advent_tuer where lernender_id = 2;")
        out = db.pg.paket(einsp_b)
        assert re.search(r'Kind 1: 0 gesetzt, \d+ unverändert', out) and re.search(r'Kind 2: 0 gesetzt', out), out[-600:]
        # Paket bricht ab: falsches Jahr, fehlendes Kind, andere Fassung von advent_belegen
        for aend, msg in (({'jahr': 2027}, 'passt nicht zur Einstellung'), ({'kinder': {'Kind 1': 1, 'Kind 2': 99}}, 'fehlt oder ist nicht aktiv'),
                          ({'kinder': {'Kind 1': 1, 'Kind 2': 5}}, 'fehlt oder ist nicht aktiv')):
            p = bauen({**bsp, **aend})
            assert p.returncode == 0, p.stderr
            db.pg.paket((Path(td) / 'advent_belegung_einspielen.sql').read_text(encoding='utf-8'), erwartet_fehler=msg)
        d = db.sql("select pg_get_functiondef('schule.advent_belegen(bigint[], jsonb, boolean, text)'::regprocedure);")
        db.sql(d.replace("declare e jsonb", "declare -- geändert\n  e jsonb", 1))
        db.pg.paket(einsp_b, erwartet_fehler='andere Fassung')
        db.pg.paket(einsp, erwartet_fehler='ADVENT-S ABBRUCH (schon da: ')    # Migration läuft nicht über einen Bestand (Auflage 3)
        db.sql(d)                                                         # ursprüngliche Fassung zurück
        db.pg.paket(einsp_b)
        # Tür 6 und 24 fest „karte“ (Urteil 1215, Auflage 6 – nur im Werkzeug): Abbruch, bevor ein Paket entsteht
        for f in ('advent_belegung_probe.sql', 'advent_belegung_einspielen.sql'): (Path(td) / f).unlink()
        n6 = 0
        for aend, msg in ((lambda d: d['tueren'][5].update(art='gutschein', titel='x'), 'Tür 6 für Kind 1: art „gutschein“ – Tür 6 und Tür 24 sind fest eine Karte'),
                          (lambda d: d['tueren'][23].update(art='sterne', variante='jackpot', sterne=1111), 'Tür 24 für Kind 1: art „sterne“'),
                          (lambda d: d['tueren'][23].update(art='bild', motiv='stern'), 'Tür 24 für Kind 2: art „bild“'),
                          (lambda d: d['tueren'][5].update(sterne=50), 'Tür 6 für Kind 1: Karte ohne Sterne'),
                          (lambda d: d['tueren'].append({'nr': 6, 'fuer': 'Kind 9', 'art': 'leer'}) or d['kinder'].update({'Kind 9': 9}) or d['tueren'][5].update(fuer=['Kind 1', 'Kind 2']),
                           'Tür 6 für Kind 9: art „leer“')):
            d = json.loads(json.dumps(bsp)); aend(d)
            pr = bauen(d)
            assert pr.returncode == 1 and msg in pr.stderr, (msg, pr.stderr)
            assert not (Path(td) / 'advent_belegung_einspielen.sql').exists(), 'kein Paket bei Abbruch'
            n6 += 1
        d = json.loads(json.dumps(bsp)); d['tueren'] = [t for t in d['tueren'] if t['nr'] not in (6, 24)]
        pr = bauen(d)                                                     # 6/24 nicht in der Datei: bleibt in der Datenbank, wie es ist (Hinweis)
        assert pr.returncode == 0 and 'HINWEIS: Tür 6 für Kind 1 nicht in der Datei' in pr.stderr and 'HINWEIS: Tür 24 für Kind 2' in pr.stderr, pr.stderr
        assert bsp['tueren'][23]['art'] == 'karte' and bsp['tueren'][23]['sterne'] > 0                 # 24 = Karte mit Sternen (Jackpot) ist erlaubt
        # Werkzeug weist ab
        n = 0
        for aend, msg in ((lambda d: d['tueren'].append({'nr': 1, 'fuer': 'Kind 1', 'art': 'leer'}), 'doppelt belegt'),
                          (lambda d: d['tueren'][0].update(motiv='einhorn'), 'motiv „einhorn“ unbekannt'),
                          (lambda d: d['tueren'][0].update(fuer='Kind 3'), 'fuer ='),
                          (lambda d: d['tueren'][0].update(sterne=6000), 'sterne ganze Zahl'),
                          (lambda d: d['tueren'][0].update(art='foto'), 'art bild'),
                          (lambda d: d['tueren'][1].update(titel=''), 'braucht einen titel'),
                          (lambda d: d['tueren'][0].update(farbe='rot'), 'nur die Felder'),
                          (lambda d: d.update(jahr='2026'), 'jahr: ganze Zahl'),
                          (lambda d: d['kinder'].update({'Kind 3': 1}), 'lernender_id doppelt'),
                          (lambda d: d['tueren'][1].update(text='x $advbeljson$ y'), '$advbel')):
            d = json.loads(json.dumps(bsp)); aend(d)
            p = bauen(d)
            assert p.returncode == 1 and msg in p.stderr, (msg, p.stderr); n += 1
        p = werkzeug('inhalte/design/advent/belegung-beispiel.json', '--aus', str(WURZEL / 'tools'))
        assert p.returncode == 1 and 'liegt im Repo' in p.stderr
        kopie = WURZEL / 'inhalte/design/advent/_test_belegung.json'
        kopie.write_text(json.dumps(bsp), encoding='utf-8')
        try:
            p = werkzeug(str(kopie))
            assert p.returncode == 1 and 'liegt im Repo' in p.stderr
        finally:
            kopie.unlink()
    print(f'Belegungs-Werkzeug: Probe rollt zurück, Einspielen überspringt geöffnete Türchen, Zweitlauf 0 gesetzt; Paket bricht ab (Jahr, Kind fehlt/inaktiv, andere Fassung); '
          f'{n + 2} ungültige Eingaben/Orte abgewiesen; Tür 6/24 nicht Karte (bzw. 6 mit Sternen): {n6} Abbrüche ohne Paket, fehlend nur Hinweis, 24 Karte + Sterne erlaubt')


if __name__ == '__main__':
    main()
